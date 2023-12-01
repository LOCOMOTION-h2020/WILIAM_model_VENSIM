import pytest
from pathlib import Path

from copy import deepcopy
import pandas as pd

from tools.config import read_config
from tools.tools import load_model


@pytest.fixture(scope="session")
def proj_folder():
    """main folder"""
    return Path(__file__).parent.parent.resolve()


@pytest.fixture(scope="function")
def default_config():
    """read model configuration"""
    return read_config()


@pytest.fixture(scope="function")
def default_config_tmp(tmp_path, default_config):
    """create the default config with tmp_paths"""

    # setting the default results folder to the tests main folder
    default_config.model.results_folder = tmp_path.joinpath("results")
    # creating the temporary results folder directory
    default_config.model.results_folder.mkdir(parents=True, exist_ok=True)

    return default_config


@pytest.fixture()
def model(default_config):
    """pysd model object"""
    return load_model(default_config)


@pytest.fixture()
def doc(model):
    """return model documentation"""
    def clean_name(name):
        """Remove outside commas from variables"""
        if name.startswith('"') and name.endswith('"'):
            return name[1:-1]
        else:
            return name

    doc = model.doc
    doc["Clean Name"] = doc["Real Name"].apply(clean_name)

    return doc


###############################################################################
#                 PREDEFINED CLI PARAMETERS                                   #
###############################################################################

@pytest.fixture()
def cli_input_long_names():

    cli_args = [
                "--final-time",
                "2006.0",
                "--time-step",
                "0.5",
                "--saveper",
                "5.0",
                "--scen",  # scenario file
                "scenario_parameters/scenario.xlsx",
                "--export",  # export results to pickle format
                "exported.pickle",
                "--silent",  # silent
                "--headless",  # headless
                "--fname",  # results file name
                "results.nc",
                "--externals",
                "externals.nc",
                "--plot",  # plot results at the end
                "var1=5",
                "var2=7.5",
                "var3=[[1, 2, 3], [4, 5, 6]]",
                "var4:5"
                ]
    return cli_args


@pytest.fixture()
def cli_input_short_names():

    cli_args = [
                "-F",
                "2006.0",
                "-T",
                "0.5",
                "-S",
                "5.0",
                "-c",  # scenario file
                "scenario_parameters/scenario.xlsx",
                "-x",  # export statefuls to file
                "exported.pickle",
                "-s",  # silent
                "-b",  # headless
                "-n",  # results file name
                "results.nc",
                "-e",  # path to external objects netCDF file
                "externals.nc",
                "-p",  # plot results at the end
                "var1=5",
                "var2=7.5",
                "var3=[[1, 2, 3], [4, 5, 6]]",
                "var4:5"
                ]

    return cli_args


# grouping configurations that do not raise
@pytest.fixture(params=["cli_input_long_names",
                        "cli_input_short_names"])
def cli_input_not_raises(request,
                         cli_input_long_names,
                         cli_input_short_names):
    return {"cli_input_long_names": cli_input_long_names,
            "cli_input_short_names": cli_input_short_names}[request.param]


###############################################################################
#           EXPECTED CONFIG AFTER CLI INPUT                                   #
###############################################################################

@pytest.fixture()
def expected_conf_cli_input_long_and_short(
    tmp_path, proj_folder, default_config):
    # this one should crash the update of the config class, cause the path
    # does not exist

    updated_conf = deepcopy(default_config)

    updated_conf.silent = True
    updated_conf.headless = True
    updated_conf.missing_values = "warning"  # not changed
    updated_conf.plot = True
    updated_conf.progress = True  # not configurable

    # model
    updated_conf.model.model_file = proj_folder.joinpath("wiliam/WILIAM.py")
    updated_conf.model.subscripts_file = proj_folder.joinpath(
        "wiliam/_subsctipts_WILIAM.json")
    updated_conf.model.scenario_file = proj_folder.joinpath(
        "scenario_parameters/scenario.xlsx")
    updated_conf.model.results_folder = tmp_path.joinpath("results")

    # model arguments
    updated_conf.model_arguments.initial_time = 2005.0
    updated_conf.model_arguments.time_step = .5
    updated_conf.model_arguments.final_time = 2006.0
    updated_conf.model_arguments.return_timestamp = 5.0
    updated_conf.model_arguments.update_params = {"var1": 5.0,
                                                  "var2": 7.5,
                                                  "var3": pd.Series(
                                                      index=[1, 2, 3],
                                                      data=[4, 5, 6])}
    updated_conf.model_arguments.update_initials = {"var4": 5.0}
    updated_conf.model_arguments.results_fname = "results.nc"
    updated_conf.model_arguments.export = tmp_path.joinpath(
        "exported.pickle").resolve()
    updated_conf.model_arguments.external_objects = tmp_path.joinpath(
        "externals.nc")

    return updated_conf
