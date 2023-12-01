"""
Module intermodule_consistency.module_switches
Translated using PySD version 3.10.0
"""


@component.add(
    name="SWITCH_DEMOGRAPHY",
    units="1",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_demography"},
)
def switch_demography():
    """
    This switch can take two values: 0: the module runs isolated from the rest of WILIAM, replacing inter(sub)module variables with exogenous parameters. 1: the module runs integrated with the rest of WILIAM.
    """
    return _ext_constant_switch_demography()


_ext_constant_switch_demography = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_DEMOGRAPHY",
    {},
    _root,
    {},
    "_ext_constant_switch_demography",
)


@component.add(
    name="SWITCH_ECO2MAT_Fe_DEMAND",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_eco2mat_fe_demand"},
)
def switch_eco2mat_fe_demand():
    """
    Intermodule links SWITCH, it can take two values: 0: the link is broken, the intermodule variable is replaced by an exogenous parameter. 1: the link between modules is operational.
    """
    return _ext_constant_switch_eco2mat_fe_demand()


_ext_constant_switch_eco2mat_fe_demand = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_ECO2MAT_Fe_DEMAND",
    {},
    _root,
    {},
    "_ext_constant_switch_eco2mat_fe_demand",
)


@component.add(
    name="SWITCH_LANDWATER",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_landwater"},
)
def switch_landwater():
    """
    GET_DIRECT_CONSTANTS('scenario_parameters/switches.xlsx', 'SWITCHES', 'SWITCH_LANDWATER') If this parameter =1 the land use submodule works normally, integrated in the rest of WILIAM. If it is =0, land and water and climate modules work without interaction with the rest of the model. GET_DIRECT_CONSTANTS('scenario_parameters/switches.xlsx', 'SWITCHES', 'SWITCH_LANDWATER')
    """
    return _ext_constant_switch_landwater()


_ext_constant_switch_landwater = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_LANDWATER",
    {},
    _root,
    {},
    "_ext_constant_switch_landwater",
)


@component.add(
    name="SWITCH_LAW_EMISSIONS",
    units="1",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_law_emissions"},
)
def switch_law_emissions():
    """
    This switch can take two values: 0: the (sub)module runs isolated from the rest of WILIAM, replacing inter(sub)module variables with exogenous parameters. 1: the (sub)module runs integrated with the rest of WILIAM.
    """
    return _ext_constant_switch_law_emissions()


_ext_constant_switch_law_emissions = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_LAW_EMISSIONS",
    {},
    _root,
    {},
    "_ext_constant_switch_law_emissions",
)


@component.add(
    name="SWITCH_LAW_EMISSIONS_LAND_USE_PRODUCTIVE_AREA",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_switch_law_emissions_land_use_productive_area"
    },
)
def switch_law_emissions_land_use_productive_area():
    """
    Temporal switch- - 0: application of exogenous data - 1: all integrated (endogenous information)
    """
    return _ext_constant_switch_law_emissions_land_use_productive_area()


_ext_constant_switch_law_emissions_land_use_productive_area = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_LAW_EMISSIONS_LAND_USE_PRODUCTIVE_AREA",
    {},
    _root,
    {},
    "_ext_constant_switch_law_emissions_land_use_productive_area",
)


@component.add(
    name="SWITCH_LAW_EMISSIONS_MATRIX_OF_LAND_USE_CHANGES",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_switch_law_emissions_matrix_of_land_use_changes"
    },
)
def switch_law_emissions_matrix_of_land_use_changes():
    """
    Temporal switch- - 0: application of exogenous data - 1: all integrated (endogenous information)
    """
    return _ext_constant_switch_law_emissions_matrix_of_land_use_changes()


_ext_constant_switch_law_emissions_matrix_of_land_use_changes = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_LAW_EMISSIONS_MATRIX_OF_LAND_USE_CHANGES",
    {},
    _root,
    {},
    "_ext_constant_switch_law_emissions_matrix_of_land_use_changes",
)


@component.add(
    name="SWITCH_LAW_EMISSIONS_SHARE_MANAGEMENT_AGRICULTURE",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_switch_law_emissions_share_management_agriculture"
    },
)
def switch_law_emissions_share_management_agriculture():
    """
    Temporal switch- - 0: application of exogenous data - 1: all integrated (endogenous information)
    """
    return _ext_constant_switch_law_emissions_share_management_agriculture()


_ext_constant_switch_law_emissions_share_management_agriculture = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_LAW_EMISSIONS_SHARE_MANAGEMENT_AGRICULTURE",
    {},
    _root,
    {},
    "_ext_constant_switch_law_emissions_share_management_agriculture",
)


@component.add(
    name="SWITCH_MAT_EMBODIED_ENERGY_OF_MATERIAL_USE",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_switch_mat_embodied_energy_of_material_use"
    },
)
def switch_mat_embodied_energy_of_material_use():
    """
    0. Materials for alternative technologies available WITHOUT energy costs. 1: Materials for alternative technologies available with energy costs.
    """
    return _ext_constant_switch_mat_embodied_energy_of_material_use()


_ext_constant_switch_mat_embodied_energy_of_material_use = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_MAT_EMBODIED_ENERGY_OF_MATERIAL_USE",
    {},
    _root,
    {},
    "_ext_constant_switch_mat_embodied_energy_of_material_use",
)


@component.add(
    name="SWITCH_NRG2LAW_PV_LAND_OCCUPATION_RATIO",
    units="1",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_switch_nrg2law_pv_land_occupation_ratio"
    },
)
def switch_nrg2law_pv_land_occupation_ratio():
    return _ext_constant_switch_nrg2law_pv_land_occupation_ratio()


_ext_constant_switch_nrg2law_pv_land_occupation_ratio = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_NRG2LAW_PV_LAND_OCCUPATION_RATIO",
    {},
    _root,
    {},
    "_ext_constant_switch_nrg2law_pv_land_occupation_ratio",
)
