"""
Module intermodule_consistency.exogenous_inputs
Translated using PySD version 3.10.0
"""


@component.add(
    name="ENERGY_SCARCITY_FORGETTING_TIME_HH_SP",
    units="Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"energy_scarcity_forgetting_time_hh_sp_w": 1},
)
def energy_scarcity_forgetting_time_hh_sp():
    """
    Time in years that households take to forget the percepticon of scarcity.
    """
    return xr.DataArray(
        energy_scarcity_forgetting_time_hh_sp_w(),
        {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
        ["REGIONS_9_I"],
    )


@component.add(
    name="ENERGY_SCARCITY_FORGETTING_TIME_HH_SP_W",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_energy_scarcity_forgetting_time_hh_sp_w"
    },
)
def energy_scarcity_forgetting_time_hh_sp_w():
    """
    Time in years that households take to forget the percepticon of scarcity.
    """
    return _ext_constant_energy_scarcity_forgetting_time_hh_sp_w()


_ext_constant_energy_scarcity_forgetting_time_hh_sp_w = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "intermodule_consistency",
    "Energy_scarcity_forgetting_factor_Households",
    {},
    _root,
    {},
    "_ext_constant_energy_scarcity_forgetting_time_hh_sp_w",
)


@component.add(
    name="ENERGY_SCARCITY_FORGETTING_TIME_SP",
    units="Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"energy_scarcity_forgetting_time_sp_w": 1},
)
def energy_scarcity_forgetting_time_sp():
    """
    Time in years that society takes to forget the percepticon of scarcity for economic sectors.
    """
    return xr.DataArray(
        energy_scarcity_forgetting_time_sp_w(),
        {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
        ["REGIONS_9_I"],
    )


@component.add(
    name="ENERGY_SCARCITY_FORGETTING_TIME_SP_W",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_energy_scarcity_forgetting_time_sp_w"},
)
def energy_scarcity_forgetting_time_sp_w():
    """
    Time in years that society takes to forget the percepticon of scarcity for economic sectors.
    """
    return _ext_constant_energy_scarcity_forgetting_time_sp_w()


_ext_constant_energy_scarcity_forgetting_time_sp_w = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "intermodule_consistency",
    "Energy_scarcity_forgetting_factor_sectors",
    {},
    _root,
    {},
    "_ext_constant_energy_scarcity_forgetting_time_sp_w",
)


@component.add(
    name="sensitivity_to_scarcity_option",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"sensitivity_to_scarcity_option_w": 1},
)
def sensitivity_to_scarcity_option():
    """
    Option defined by user about the sensitivity of economic sectors to energy scarcity: 1-Low 2-Medium 3-High
    """
    return xr.DataArray(
        sensitivity_to_scarcity_option_w(),
        {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
        ["REGIONS_9_I"],
    )


@component.add(
    name="sensitivity_to_scarcity_option_H",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"sensitivity_to_scarcity_option_h_w": 1},
)
def sensitivity_to_scarcity_option_h():
    """
    Option defined by user about the sensitivity of households to the energy scarcity: 1-Low 2-Medium 3-High
    """
    return xr.DataArray(
        sensitivity_to_scarcity_option_h_w(),
        {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
        ["REGIONS_9_I"],
    )


@component.add(
    name="sensitivity_to_scarcity_option_H_W",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_sensitivity_to_scarcity_option_h_w"},
)
def sensitivity_to_scarcity_option_h_w():
    """
    Option defined by user about the sensitivity of households to the energy scarcity: 1-Low 2-Medium 3-High
    """
    return _ext_constant_sensitivity_to_scarcity_option_h_w()


_ext_constant_sensitivity_to_scarcity_option_h_w = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "intermodule_consistency",
    "Sensitivity_to_scarcity_Households",
    {},
    _root,
    {},
    "_ext_constant_sensitivity_to_scarcity_option_h_w",
)


@component.add(
    name="sensitivity_to_scarcity_option_W",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_sensitivity_to_scarcity_option_w"},
)
def sensitivity_to_scarcity_option_w():
    """
    Option defined by user about the sensitivity of economic sectors to energy scarcity: 1-Low 2-Medium 3-High
    """
    return _ext_constant_sensitivity_to_scarcity_option_w()


_ext_constant_sensitivity_to_scarcity_option_w = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "intermodule_consistency",
    "Sensitivity_to_scarcity_economic_sectors",
    {},
    _root,
    {},
    "_ext_constant_sensitivity_to_scarcity_option_w",
)


@component.add(
    name="SWITCH_SCARCITY_FEEDBACK_FINAL_FUEL_REPLACEMENT_SP",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"switch_scarcity_feedback_final_fuel_replacement_sp_w": 1},
)
def switch_scarcity_feedback_final_fuel_replacement_sp():
    """
    Switch to (de)activate the scarcity feedback fuel replacement.
    """
    return xr.DataArray(
        switch_scarcity_feedback_final_fuel_replacement_sp_w(),
        {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
        ["REGIONS_9_I"],
    )


@component.add(
    name="SWITCH_SCARCITY_FEEDBACK_FINAL_FUEL_REPLACEMENT_SP_W",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_switch_scarcity_feedback_final_fuel_replacement_sp_w"
    },
)
def switch_scarcity_feedback_final_fuel_replacement_sp_w():
    """
    Switch to (de)activate the scarcity feedback fuel replacement.
    """
    return _ext_constant_switch_scarcity_feedback_final_fuel_replacement_sp_w()


_ext_constant_switch_scarcity_feedback_final_fuel_replacement_sp_w = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "intermodule_consistency",
    "Activate_scarcity_feedback_final_fuel_replacement_1_Y_0_N",
    {},
    _root,
    {},
    "_ext_constant_switch_scarcity_feedback_final_fuel_replacement_sp_w",
)
