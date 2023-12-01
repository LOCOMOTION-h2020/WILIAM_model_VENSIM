import pathlib
from typing import Optional, List, Union
from dataclasses import dataclass
import json
import dacite
from dacite import Config
from . import PROJ_FOLDER


@dataclass
class ModelArguments:  # configurations to send to PySD
    """Holds the model arguments"""
    initial_time: float
    time_step: float
    final_time: float
    return_timestamp: float
    update_params: Optional[dict]  # dict of model pars to update at runtime
    update_initials: Union[dict, str]
    results_fname: Optional[str]  # name of the file
    results_fpath: Optional[pathlib.Path]  # Path to the file
    export: Optional[pathlib.Path]  # export to pickle file
    external_objects: Optional[Union[str, pathlib.Path]]


@dataclass
class Model:
    """Holds the main model parameters"""
    model_file: pathlib.Path
    subscripts_file: pathlib.Path  # TODO not used
    scenario_file: pathlib.Path
    results_folder: pathlib.Path


@dataclass
class Params:
    """Holds the main parameters for loading the model"""
    model_arguments: ModelArguments
    silent: bool
    headless: bool
    missing_values: str  # default is 'warning'
    plot: bool
    progress: bool  # default is True, not modifiable through CLI
    model: Model


def read_config() -> Params:
    """Read main configuration"""
    # default simulation parameters
    # None values are given in argparser.py

    config_path = PROJ_FOLDER / 'tools' / 'config.json'

    with config_path.open(encoding='utf-8') as params:
        pars = json.load(params)

    # loading general config
    config = dacite.from_dict(
        data_class=Params,
        data=pars,
        config=Config(type_hooks={pathlib.Path: PROJ_FOLDER.joinpath})
        )

    return config


def read_model_config(config: Params) -> None:
    """Read model configuration"""

    models_path = PROJ_FOLDER / 'tools' / 'outputs.json'

    with models_path.open(encoding='utf-8') as mod_pars:
        default_outputs = json.load(mod_pars)

    # adding the model configuration to the Params object
    config.model = dacite.from_dict(
        data_class=Model,
        data=default_outputs,
        config=Config(type_hooks={pathlib.Path: PROJ_FOLDER.joinpath})
    )
