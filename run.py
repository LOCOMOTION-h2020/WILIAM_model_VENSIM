#!/usr/bin/env python
"""
This code allows parametrizing, launching and saving and plotting the
results of the pywiliam model.
"""
import warnings
import argparse

from pysd.py_backend.model import Model
import pysd

import plot_tool
from tools.config import Params
from tools.tools import (get_initial_user_input,
                         update_config_from_user_input,
                         run,
                         load_model,
                         initialize_model,
                         generate_output_path)


warnings.filterwarnings("ignore")

# check PySD version
if tuple(int(i) for i in pysd.__version__.split(".")[:2]) < (3, 8):
    raise RuntimeError(
        "\n\n"
        + "The current version of the wiliam model needs at least PySD 3.8"
        + " You are running:\n\tPySD "
        + pysd.__version__
        + "\nPlease update PySD library with your package manager, "
        + "via PyPy or conda-forge."
    )


def main(config: Params) -> None:
    """
    Main function for running the model

    Parameters
    ----------
    config: dict
        Configuration parameters.
    run_params: dict
        Simulation parameters.

    """

    # loading the model object
    model: Model = load_model(config)

    initialize_model(config, model)

    generate_output_path(config)

    # run the simulation and store results in netcdf_path
    run(config, model)

    # running the plot tool
    if config.plot:
        if not config.headless:
            plot_tool.main(config)
        else:
            print(
                '\nWe prevented the plot GUI from popping up, since'
                ' you are in headless mode. To prevent this message'
                ' from showing up again, please either remove the '
                '-p (or --plot) or -b (or --headless) from the simulation '
                'options.\n')


if __name__ == "__main__":

    # get command line parameters and update paths
    options: argparse.Namespace = get_initial_user_input()

    # read user input and update config
    config: Params = update_config_from_user_input(options)

    main(config)
