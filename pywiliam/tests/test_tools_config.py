import pytest


def test_default_config(proj_folder, default_config):
    """test default configuration values"""
    config = default_config

    assert not config.silent
    assert not config.headless
    assert config.missing_values == "warning"
    assert not config.plot
    assert config.progress

    # model
    assert config.model.model_file.is_file()
    assert config.model.subscripts_file.is_file()
    assert config.model.scenario_file.name == "scenario_parameters.xlsx"
    assert config.model.results_folder == proj_folder.joinpath("results")

    # model arguments
    assert config.model_arguments.initial_time == 2005.0
    assert config.model_arguments.time_step == .25
    assert config.model_arguments.final_time == 2050.0
    assert config.model_arguments.return_timestamp == 1.0
    assert config.model_arguments.update_params is None
    assert config.model_arguments.update_initials == {}
    assert config.model_arguments.results_fname is None
    assert config.model_arguments.export is None
    assert config.model_arguments.external_objects is None
