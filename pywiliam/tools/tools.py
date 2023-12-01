#!/usr/bin/env python
__author__ = "Roger Samsó, Eneko Martin"

import warnings
import time
from datetime import datetime
from pathlib import Path
from argparse import Namespace
# these imports will not be needed in Python 3.9
from typing import Union, List

import pysd

# PySD imports for replaced functions
from pysd.py_backend.model import Model


from . import PROJ_FOLDER
from .logger.logger import log
from .argparser import parser, config
from .config import Params


def get_initial_user_input(args: Union[List, None] = None) -> Namespace:
    """
    Get user input to create the config object.

    Parameters
    ----------
    args: list or None (optional)
        List of user arguments to run the model. If None the arguments
        will be taken from the taken from the system input. Default is None.

    Returns
    -------
    config: argparse.Namespace
        Configuration data object.

    """

    return parser.parse_args(args)


def update_config_from_user_input(user_inputs: Namespace,
                                  base_path: Path = PROJ_FOLDER) -> Params:

    """
    This function takes user inputs and updates the config class attributes
    accordingly.
    The base_path argument is for testing purposes only
    """
    # update configurations from Params class based on user input
    # only if there's a default value set in config.json or the user adds input
    # for that attribute
    config.silent = user_inputs.silent
    config.headless = user_inputs.headless
    config.missing_values = user_inputs.missing_values
    config.plot = user_inputs.plot
    # the progressbar cannot be switched off

    # update configurations from ModelArguments
    if user_inputs.export_file:
        if Path(user_inputs.export_file).is_absolute():
            if Path(user_inputs.export_file).parent.is_dir():
                config.model_arguments.export = Path(
                    user_inputs.export_file).resolve()
            else:
                raise ValueError("Invalid pickle export path {}".format(
                    str(Path(user_inputs.export_file))))
        else:
            pickle_path = base_path.joinpath(user_inputs.export_file).resolve()
            if pickle_path.parent.is_dir():
                config.model_arguments.export = pickle_path
            else:
                raise ValueError("Invalid pickle export path {}".format(
                    str(Path(user_inputs.export_file).resolve())))

    # if not passed by user, external_objects will be None (no default given)
    if user_inputs.external_objects:
        externals_path = base_path.joinpath(
            user_inputs.external_objects).resolve()

        if not externals_path.is_file():
            raise FileNotFoundError(f"{str(externals_path)} does not exist.")

        config.model_arguments.external_objects = externals_path

    # the following have default values (read from config.json)
    config.model_arguments.time_step = user_inputs.time_step
    config.model_arguments.final_time = user_inputs.final_time
    config.model_arguments.return_timestamp = user_inputs.return_timestamp
    config.model_arguments.results_fname = user_inputs.results_fname

    if user_inputs.new_values['param']:
        config.model_arguments.update_params = user_inputs.new_values['param']

    if user_inputs.new_values['initial']:
        config.model_arguments.update_initials = \
            user_inputs.new_values['initial']

    return config


def _rename_old_simulation_results(file_path: Path) -> None:
    """
    This function renames old simulation results with the same name but
    adding date and time at the end of the file name

    :return (str) new file path
    """

    folder = file_path.parent
    fname = file_path.stem
    extension = file_path.suffix

    if file_path.is_file():
        creation_time: str = datetime.fromtimestamp(
            file_path.stat().st_ctime).strftime("%Y%m%d__%H%M%S")
        old_file_new_path = folder.joinpath(fname + "_{}".format(creation_time)
                                            + extension)
        file_path.rename(old_file_new_path)
        log.info(f"File {fname + extension} has been renamed as "
                 f"{old_file_new_path.name}")


def generate_output_path(config: Params) -> None:

    """
    Creates the Path for the netCDF file and updates the
    config.model_parameters.results_fpath field.

    It also creates the results folder, if not present.

    Parameters
    ----------
    config: Params
        Configuration object.

    Returns
    -------
    None


    """
    # If the results folder doesn't exist, create it
    if not config.model.results_folder.exists():
        config.model.results_folder.mkdir(parents=True)

    # generating the output file names
    if not config.model_arguments.results_fname:
        netcdf_path = config.model.results_folder.joinpath(
            "results_{}_{}_{}_{}.nc".format(
                config.model.scenario_file.stem.lower(),
                int(config.model_arguments.initial_time),
                int(config.model_arguments.final_time),
                config.model_arguments.time_step
                ))
    else:
        user_file_stem, user_extension = \
            config.model_arguments.results_fname.split(".")

        if user_extension != "nc":
            netcdf_path = config.model.results_folder.joinpath(
                user_file_stem + ".nc")
            warnings.warn("Results can only be stored in netCDF format. "
                          f"Your results will be stored in {str(netcdf_path)}")
        else:
            netcdf_path = config.model.results_folder.joinpath(
                config.model_arguments.results_fname)

    # updating config parameters
    config.model_arguments.results_fpath = netcdf_path


def run(config: Params, model: Model) -> None:
    """
    Runs the model and stores the results in
    config.model_parameters.results_fpath.

    Parameters
    ----------
    config: Params
        Configuration parameters.
    model: pysd.Model
        Model object.

    Returns
    -------
    None

    """

    # if the file exists, rename the existing one
    _rename_old_simulation_results(config.model_arguments.results_fpath)

    print(
        "\n\nSimulation parameters:\n"
        f"- Scenario file: {config.model.scenario_file.name}\n"
        f"- Initial time: {config.model_arguments.initial_time}\n"
        f"- Final time: {config.model_arguments.final_time}\n"
        f"- Simulation time step: {config.model_arguments.time_step} years "
        f"({config.model_arguments.time_step*365} days)\n"
        f"- Results folder: {config.model.results_folder}")

    if config.model_arguments.update_initials:
        print("- Updated initial conditions:\n\t" + "\n\t".join(
            [par + ": " + str(val) for par, val in
             config.model_arguments.update_initials.items()]))

    sim_start_time = time.time()

    model.run(
        params=config.model_arguments.update_params,
        initial_condition=(config.model_arguments.initial_time,
                           config.model_arguments.update_initials),
        return_columns="all",
        progress=config.progress,
        final_time=config.model_arguments.final_time,
        time_step=config.model_arguments.time_step,
        saveper=config.model_arguments.return_timestamp,
        output_file=config.model_arguments.results_fpath)

    sim_time = time.time() - sim_start_time

    log.info(f"Total simulation time: {(sim_time/60.):.2f} minutes")


def load_model(config: Params) -> Model:
    """
    Load PySD model and changes the paths to load excel data.

    Parameters
    ----------
    config: dict
        Configuration parameters.

    Returns
    -------
    pysd.Model

    """

    # Load PySD model
    return pysd.load(config.model.model_file, initialize=False)


def initialize_model(config: Params, model: Model) -> None:
    """
    Initializes the external objects of the model. If the -e argument is
    passed by the user, external data is loaded from there.

    Parameters
    ----------
    config: Params
        Configurations object.

    model: pysd.Model
        Uninitialized PySD Model object.

    Returns
    -------
    None

    """
    if config.model_arguments.external_objects:
        warnings.warn(
            "You are passing a netCDF file to load external data from. "
            "Please make sure the netCDF file does not include the parameters "
            "you expect to modify in your scenario file. Otherwise those "
            "changes will not take effect.")

    # Modify external elements information
    for element in model._external_elements:
        default_element_files = element.files

        for idx, file_name in enumerate(default_element_files):
            if file_name.startswith("../../scenario_parameters/"):
                element.files[idx] = config.model_arguments.scenario_file

    model.initialize_external_data(
        externals=config.model_arguments.external_objects)
