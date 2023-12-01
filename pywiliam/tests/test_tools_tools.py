import pytest
from datetime import datetime
import pandas as pd
from pysd.py_backend.model import Model

import tools.tools as tools


def test_update_config_from_user_input_defaults(default_config):
    """Update config from user imput"""
    options = tools.get_initial_user_input([])
    assert tools.update_config_from_user_input(options) == default_config


def test_load_model(default_config):
    """Model is loaded correctly with default config"""
    model = tools.load_model(default_config)
    assert isinstance(model, Model)


def test_update_config_from_user_input_not_raising(
    cli_input_not_raises, expected_conf_cli_input_long_and_short):

    # if the parent results folder and the export pickle folder do not exist,
    # it will raise. Therefore they must exist.
    base_tmp_folder = expected_conf_cli_input_long_and_short. \
                    model_arguments.export.parent

    results_fpath = base_tmp_folder.joinpath(
        "results/" + cli_input_not_raises[13])

    pickle_fpath = base_tmp_folder.joinpath(cli_input_not_raises[9])

    externals_fpath = base_tmp_folder.joinpath(cli_input_not_raises[15])
    # creating results folder (hence the pickle folder too, but I leave it
    # there in case the config of the test ever changes)
    results_fpath.parent.mkdir(parents=True, exist_ok=True)
    pickle_fpath.parent.mkdir(parents=True, exist_ok=True)

    # creating externals file
    externals_fpath.touch(exist_ok=True)

    # mocking options passed by user
    options = tools.get_initial_user_input(cli_input_not_raises)

    # updating configs passed by the user
    result_config = tools.update_config_from_user_input(
        options, base_path=base_tmp_folder)

    # checking that the changes in the Params dataclass actually took place
    for attr in expected_conf_cli_input_long_and_short.__annotations__:
        if attr not in ["model_arguments", "model"]:
            assert getattr(expected_conf_cli_input_long_and_short, attr) == \
                getattr(result_config, attr)

    model_args_def = expected_conf_cli_input_long_and_short.model_arguments
    model_args_res = result_config.model_arguments

    for attr in model_args_def.__annotations__:
        if attr != "update_params":
            assert getattr(model_args_def, attr) == \
                        getattr(model_args_res, attr)

    for key, value in model_args_def.update_params.items():
        if isinstance(value, pd.Series):
            assert model_args_def.update_params[key].equals(
                model_args_res.update_params[key])
        else:
            assert model_args_def.update_params[key] == \
                model_args_res.update_params[key]


@pytest.mark.parametrize(
    "cli_arguments,error",
    [
      (["--export", "tests/test_data/" + "results.pickle"], ValueError),
      (["--externals", "missing_file.nc"], FileNotFoundError)
    ]
)
def test_update_config_from_user_input_raises(cli_arguments, error):
    with pytest.raises(error):
        options = tools.get_initial_user_input(
             cli_arguments)
        tools.update_config_from_user_input(options)


@pytest.mark.parametrize(
    "results_file",
    ["results_BAU_1995.0_1996.0_0.03125.nc", "results.nc"])
def test__rename_old_simulation_results_file_exists(default_config_tmp,
                                                    results_file):
    """Rename old simulations results"""
    file_path = default_config_tmp.model.results_folder.joinpath(
        results_file)
    folder = file_path.parent
    fname = file_path.stem
    extension = file_path.suffix

    # creating the file in the tmp_path to simulate it already exists
    file_path.touch()

    # storing the creation time of the file
    creation_time: str = datetime.fromtimestamp(
        file_path.stat().st_ctime).strftime("%Y%m%d__%H%M%S")

    tools._rename_old_simulation_results(file_path)

    new_file_path = folder.joinpath(fname + "_{}".format(creation_time) +
                                    extension)
    # the path in the config remains unchanged
    assert not file_path.is_file()
    assert new_file_path.is_file()


def test__rename_old_simulation_results_file_not_exists(default_config_tmp):
    """Do not rename old simulations results if no file with the same name
    exists"""
    original_path = default_config_tmp.model.results_folder.joinpath(
        "new_file.csv")

    tools._rename_old_simulation_results(original_path)

    # no file was written (renamed)
    assert not any(original_path.parent.iterdir())


@pytest.mark.parametrize(
    "fname,warns,expected_path",
    [("results.nc", False, "results.nc"),
     ("results.csv", True, "results.nc"),
     (None, False, "results_scenario_parameters_2005_2050_0.25.nc")
     ]
     )
def test_generate_output_path(default_config_tmp, fname, warns, expected_path):
    """
    Check that the results_fpath is set correctly, either if passed by the user
    or not.
    """
    # simulate user has passed a results file name
    default_config_tmp.model_arguments.results_fname = fname
    expected = default_config_tmp.model.results_folder.joinpath(expected_path)

    if warns:
        with pytest.warns():
            tools.generate_output_path(default_config_tmp)
    else:
        tools.generate_output_path(default_config_tmp)

    assert default_config_tmp.model_arguments.results_fpath == expected


@pytest.mark.skip(reason="Not implemented")
def test_initialize_model():
    assert False
