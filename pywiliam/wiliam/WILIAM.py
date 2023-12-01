"""
Python model 'WILIAM.py'
Translated using PySD
"""

from pathlib import Path
import numpy as np
import xarray as xr

from pysd.py_backend.functions import (
    sum,
    vmax,
    prod,
    zidz,
    integer,
    vector_reorder,
    vector_select,
    ramp,
    vmin,
    modulo,
    get_time_value,
    vector_sort_order,
    xidz,
    step,
    if_then_else,
    active_initial,
    invert_matrix,
)
from pysd.py_backend.statefuls import (
    SampleIfTrue,
    Smooth,
    Delay,
    DelayFixed,
    Initial,
    Integ,
)
from pysd.py_backend.external import ExtLookup, ExtData, ExtConstant
from pysd.py_backend.utils import load_model_data, load_modules
from pysd.py_backend.allocation import allocate_available, allocate_by_priority
from pysd import Component

__pysd_version__ = "3.10.0"

__data = {"scope": None, "time": lambda: 0}

_root = Path(__file__).parent

_subscript_dict, _modules = load_model_data(_root, "WILIAM")

component = Component()

#######################################################################
#                          CONTROL VARIABLES                          #
#######################################################################

_control_vars = {
    "initial_time": lambda: 2005,
    "final_time": lambda: 2050,
    "time_step": lambda: 0.25,
    "saveper": lambda: 1,
}


def _init_outer_references(data):
    for key in data:
        __data[key] = data[key]


@component.add(name="Time")
def time():
    """
    Current time of the model.
    """
    return __data["time"]()


@component.add(
    name="FINAL_TIME", units="Year", comp_type="Constant", comp_subtype="Normal"
)
def final_time():
    """
    The final time for the simulation.
    """
    return __data["time"].final_time()


@component.add(
    name="INITIAL_TIME", units="Year", comp_type="Constant", comp_subtype="Normal"
)
def initial_time():
    """
    Initial time for the simulation of WILIAM. DO NOT MODIFY!!
    """
    return __data["time"].initial_time()


@component.add(
    name="SAVEPER",
    units="Year",
    limits=(0.0, np.nan),
    comp_type="Constant",
    comp_subtype="Normal",
)
def saveper():
    """
    The frequency with which output is stored.
    """
    return __data["time"].saveper()


@component.add(
    name="TIME_STEP",
    units="Year",
    limits=(0.0, np.nan),
    comp_type="Constant",
    comp_subtype="Normal",
)
def time_step():
    """
    The time step for the simulation.Used to delay the price signal, to prevent simultanous calculations.
    """
    return __data["time"].time_step()


#######################################################################
#                           MODEL VARIABLES                           #
#######################################################################

# load modules from modules_WILIAM directory
exec(load_modules("modules_WILIAM", _modules, _root, []))
