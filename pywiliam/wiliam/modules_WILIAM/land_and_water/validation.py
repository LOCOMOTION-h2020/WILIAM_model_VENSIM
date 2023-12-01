"""
Module land_and_water.validation
Translated using PySD version 3.10.0
"""


@component.add(
    name="EXO_SHARE_AREA_RICE_CROPLAND",
    units="km2",
    subscripts=["REGIONS_9_I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_exo_share_area_rice_cropland",
        "__lookup__": "_ext_lookup_exo_share_area_rice_cropland",
    },
)
def exo_share_area_rice_cropland(x, final_subs=None):
    """
    Exogenous data from simulation de share area rice cropland
    """
    return _ext_lookup_exo_share_area_rice_cropland(x, final_subs)


_ext_lookup_exo_share_area_rice_cropland = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "TIME_EXO_SIMULATION",
    "EXO_SHARE_AREA_RICE_CROPLAND",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_lookup_exo_share_area_rice_cropland",
)


@component.add(
    name="EXO_SHARE_OF_AGRICULTURE_IN_TRANSITION",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_exo_share_of_agriculture_in_transition",
        "__lookup__": "_ext_lookup_exo_share_of_agriculture_in_transition",
    },
)
def exo_share_of_agriculture_in_transition(x, final_subs=None):
    """
    exogenous data from simulation
    """
    return _ext_lookup_exo_share_of_agriculture_in_transition(x, final_subs)


_ext_lookup_exo_share_of_agriculture_in_transition = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "TIME_EXO_SIMULATION",
    "EXO_share_of_agriculture_in_transition",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_lookup_exo_share_of_agriculture_in_transition",
)


@component.add(
    name="EXO_SHARE_OF_INDUSTRIAL_AGRICULTURE",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_exo_share_of_industrial_agriculture",
        "__lookup__": "_ext_lookup_exo_share_of_industrial_agriculture",
    },
)
def exo_share_of_industrial_agriculture(x, final_subs=None):
    """
    exogenous data from simulation
    """
    return _ext_lookup_exo_share_of_industrial_agriculture(x, final_subs)


_ext_lookup_exo_share_of_industrial_agriculture = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "TIME_EXO_SIMULATION",
    "EXO_share_of_industrial_agriculture",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_lookup_exo_share_of_industrial_agriculture",
)


@component.add(
    name="EXO_SHARE_OF_LOW_INPUT_AGRICULTURE",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_exo_share_of_low_input_agriculture",
        "__lookup__": "_ext_lookup_exo_share_of_low_input_agriculture",
    },
)
def exo_share_of_low_input_agriculture(x, final_subs=None):
    """
    exogenous data from simulation
    """
    return _ext_lookup_exo_share_of_low_input_agriculture(x, final_subs)


_ext_lookup_exo_share_of_low_input_agriculture = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "TIME_EXO_SIMULATION",
    "EXO_share_of_low_input_agriculture",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_lookup_exo_share_of_low_input_agriculture",
)


@component.add(
    name="EXO_SHARE_OF_REGENERATIVE_AGRICULTURE",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_exo_share_of_regenerative_agriculture",
        "__lookup__": "_ext_lookup_exo_share_of_regenerative_agriculture",
    },
)
def exo_share_of_regenerative_agriculture(x, final_subs=None):
    """
    exogenous data from simulation
    """
    return _ext_lookup_exo_share_of_regenerative_agriculture(x, final_subs)


_ext_lookup_exo_share_of_regenerative_agriculture = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "TIME_EXO_SIMULATION",
    "EXO_share_of_regenerative_agriculture",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_lookup_exo_share_of_regenerative_agriculture",
)


@component.add(
    name="EXO_SHARE_OF_TRADITIONAL_AGRICULTURE",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_exo_share_of_traditional_agriculture",
        "__lookup__": "_ext_lookup_exo_share_of_traditional_agriculture",
    },
)
def exo_share_of_traditional_agriculture(x, final_subs=None):
    """
    exogenous data from simulation
    """
    return _ext_lookup_exo_share_of_traditional_agriculture(x, final_subs)


_ext_lookup_exo_share_of_traditional_agriculture = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "TIME_EXO_SIMULATION",
    "EXO_share_of_traditional_agriculture",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_lookup_exo_share_of_traditional_agriculture",
)
