"""
Module constants.exogenous_inputs
Translated using PySD version 3.10.0
"""


@component.add(
    name="BILLONperson_PER_MILLONperson_units",
    units="Billon_persons/Million_persons",
    comp_type="Constant",
    comp_subtype="Normal",
)
def billonperson_per_millonperson_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="dollars_per_Mdollar",
    units="dollars/Mdollars",
    comp_type="Constant",
    comp_subtype="Normal",
)
def dollars_per_mdollar():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="g_per_Mt_units", units="g/Mt", comp_type="Constant", comp_subtype="Normal"
)
def g_per_mt_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="g_per_t_units", units="g/t", comp_type="Constant", comp_subtype="Normal"
)
def g_per_t_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="GHG_VOLUME_TO_MASS_CONVERSION_FACTOR",
    units="Mt/m3",
    subscripts=["GHG_ENERGY_USE_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_ghg_volume_to_mass_conversion_factor"},
)
def ghg_volume_to_mass_conversion_factor():
    return _ext_constant_ghg_volume_to_mass_conversion_factor()


_ext_constant_ghg_volume_to_mass_conversion_factor = ExtConstant(
    "model_parameters/energy/energy-emission_factors.xlsx",
    "EF_MINING",
    "GHG_VOLUME_TO_MASS_CONVERSION_FACTOR*",
    {"GHG_ENERGY_USE_I": _subscript_dict["GHG_ENERGY_USE_I"]},
    _root,
    {"GHG_ENERGY_USE_I": _subscript_dict["GHG_ENERGY_USE_I"]},
    "_ext_constant_ghg_volume_to_mass_conversion_factor",
)


@component.add(
    name="GJ_per_EJ_units", units="GJ/EJ", comp_type="Constant", comp_subtype="Normal"
)
def gj_per_ej_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="GW_per_TW_units", units="GW/TW", comp_type="Constant", comp_subtype="Normal"
)
def gw_per_tw_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="ha_per_Mha_units", units="ha/MHa", comp_type="Constant", comp_subtype="Normal"
)
def ha_per_mha_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="INITIAL_SIMULATION_YEAR",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_simulation_year"},
)
def initial_simulation_year():
    """
    Initial simulation year.
    """
    return _ext_constant_initial_simulation_year()


_ext_constant_initial_simulation_year = ExtConstant(
    "model_parameters/constants.xlsx",
    "constants",
    "INITIAL_SIMULATION_YEAR",
    {},
    _root,
    {},
    "_ext_constant_initial_simulation_year",
)


@component.add(
    name="J_per_EJ_units", units="J/EJ", comp_type="Constant", comp_subtype="Normal"
)
def j_per_ej_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="J_per_MJ_units", units="J/MJ", comp_type="Constant", comp_subtype="Normal"
)
def j_per_mj_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="J_per_TJ_units", units="TJ/J", comp_type="Constant", comp_subtype="Normal"
)
def j_per_tj_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="kg_per_Mt_units", units="kg/Mt", comp_type="Constant", comp_subtype="Normal"
)
def kg_per_mt_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="km2_per_ha_units", units="km2/ha", comp_type="Constant", comp_subtype="Normal"
)
def km2_per_ha_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="km3_per_hm3_units",
    units="km3/hm3",
    comp_type="Constant",
    comp_subtype="Normal",
)
def km3_per_hm3_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="km_per_m_units", units="km/m", comp_type="Constant", comp_subtype="Normal"
)
def km_per_m_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="kpeople_per_people_units",
    units="kpeople/people",
    comp_type="Constant",
    comp_subtype="Normal",
)
def kpeople_per_people_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="kt_per_Gt_units", units="Kt/Gt", comp_type="Constant", comp_subtype="Normal"
)
def kt_per_gt_units():
    return 1


@component.add(
    name="kW_per_MW_units", units="kW/MW", comp_type="Constant", comp_subtype="Normal"
)
def kw_per_mw_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="kWh_per_TWh_units",
    units="kWh/TWh",
    comp_type="Constant",
    comp_subtype="Normal",
)
def kwh_per_twh_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="m2_per_km2_units", units="m2/km2", comp_type="Constant", comp_subtype="Normal"
)
def m2_per_km2_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="m_per_mm_units", units="m/mm", comp_type="Constant", comp_subtype="Normal"
)
def m_per_mm_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="MATRIX_UNIT_PREFIXES",
    units="DMNL",
    subscripts=["UNIT_PREFIXES_I", "UNIT_PREFIXES1_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_matrix_unit_prefixes"},
)
def matrix_unit_prefixes():
    """
    Conversion from Matrix unit prefixes[tera,BASE UNIT] (1 T$ = 1e12 $).
    """
    return _ext_constant_matrix_unit_prefixes()


_ext_constant_matrix_unit_prefixes = ExtConstant(
    "model_parameters/constants.xlsx",
    "Constants",
    "MATRIX_UNIT_PREFIXES",
    {
        "UNIT_PREFIXES_I": _subscript_dict["UNIT_PREFIXES_I"],
        "UNIT_PREFIXES1_I": _subscript_dict["UNIT_PREFIXES1_I"],
    },
    _root,
    {
        "UNIT_PREFIXES_I": _subscript_dict["UNIT_PREFIXES_I"],
        "UNIT_PREFIXES1_I": _subscript_dict["UNIT_PREFIXES1_I"],
    },
    "_ext_constant_matrix_unit_prefixes",
)


@component.add(
    name="MJ_per_EJ_units", units="MJ/EJ", comp_type="Constant", comp_subtype="Normal"
)
def mj_per_ej_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="Mm3_per_m3_units", units="Mm3/m3", comp_type="Constant", comp_subtype="Normal"
)
def mm3_per_m3_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="Mt_per_Bt_units", units="Mt/Bt", comp_type="Constant", comp_subtype="Normal"
)
def mt_per_bt_units():
    return 1


@component.add(
    name="Mt_per_Gt_units", units="Mt/Gt", comp_type="Constant", comp_subtype="Normal"
)
def mt_per_gt_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="Mt_per_kt_units", units="Mt/Kt", comp_type="Constant", comp_subtype="Normal"
)
def mt_per_kt_units():
    return 1


@component.add(
    name="Mvehicles_per_vehicles_units",
    units="Mvehicles/vehicles",
    comp_type="Constant",
    comp_subtype="Normal",
)
def mvehicles_per_vehicles_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="MW_1_YEAR_TO_MJ",
    units="MJ/(Year*MW)",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_mw_1_year_to_mj"},
)
def mw_1_year_to_mj():
    """
    Conversion factor MW in 1 year to MJ.
    """
    return _ext_constant_mw_1_year_to_mj()


_ext_constant_mw_1_year_to_mj = ExtConstant(
    "model_parameters/constants.xlsx",
    "Constants",
    "MW_in_1_year_to_MJ",
    {},
    _root,
    {},
    "_ext_constant_mw_1_year_to_mj",
)


@component.add(
    name="MW_per_TW_units", units="MW/TW", comp_type="Constant", comp_subtype="Normal"
)
def mw_per_tw_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="NUMBER_OF_REGIONS",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_number_of_regions"},
)
def number_of_regions():
    """
    **DO NOT MODIFY THIS PARAMETER** Auxiliary variable to prorate world data to 9 regions weighting equally each one (World/9). Each module should take care of adapting the inputs received from other modules so they are correctly calibrated with historical data. As versions of the model are progressively built, all the variables which are provided by other modules should come endogenously regionalized.
    """
    return _ext_constant_number_of_regions()


_ext_constant_number_of_regions = ExtConstant(
    "model_parameters/constants.xlsx",
    "constants",
    "NUMBER_OF_REGIONS",
    {},
    _root,
    {},
    "_ext_constant_number_of_regions",
)


@component.add(
    name="ONE_YEAR", units="Year", comp_type="Constant", comp_subtype="Normal"
)
def one_year():
    return 1


@component.add(
    name="PE_ENERGY_DENSITY_MJ_kg",
    units="MJ/kg",
    subscripts=["NRG_PE_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_pe_energy_density_mj_kg"},
)
def pe_energy_density_mj_kg():
    """
    Energy density of primary energy sources (commodities). This indicator assumes constant quantities of energy per kilogram of mass.
    """
    return _ext_constant_pe_energy_density_mj_kg()


_ext_constant_pe_energy_density_mj_kg = ExtConstant(
    "model_parameters/constants.xlsx",
    "constants",
    "PE_ENERGY_DENSITY_MJ_kg*",
    {"NRG_PE_I": _subscript_dict["NRG_PE_I"]},
    _root,
    {"NRG_PE_I": _subscript_dict["NRG_PE_I"]},
    "_ext_constant_pe_energy_density_mj_kg",
)


@component.add(
    name="PJ_per_EJ_units", units="PJ/EJ", comp_type="Constant", comp_subtype="Normal"
)
def pj_per_ej_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="RADIANS_PER_ARCDEGREE",
    units="radians/arcdegree",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_radians_per_arcdegree"},
)
def radians_per_arcdegree():
    """
    x PI/180°.
    """
    return _ext_constant_radians_per_arcdegree()


_ext_constant_radians_per_arcdegree = ExtConstant(
    "model_parameters/constants.xlsx",
    "constants",
    "RADIANS_PER_ARCDEGREE",
    {},
    _root,
    {},
    "_ext_constant_radians_per_arcdegree",
)


@component.add(
    name="SPECIFIC_HEAT_CAPACITY_WATER",
    units="J/kg/DegreesC",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_specific_heat_capacity_water"},
)
def specific_heat_capacity_water():
    """
    Specific heat of water, i.e., amount of heat in Joules per kg water required to raise the temperature by one degree Celsius.
    """
    return _ext_constant_specific_heat_capacity_water()


_ext_constant_specific_heat_capacity_water = ExtConstant(
    "model_parameters/constants.xlsx",
    "constants",
    "SPECIFIC_HEAT_CAPACITY_WATER",
    {},
    _root,
    {},
    "_ext_constant_specific_heat_capacity_water",
)


@component.add(
    name="t_per_Gt_units", units="t/Gt", comp_type="Constant", comp_subtype="Normal"
)
def t_per_gt_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="t_per_kg_units", units="t/kg", comp_type="Constant", comp_subtype="Normal"
)
def t_per_kg_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="t_per_kt_units", units="t/Kt", comp_type="Constant", comp_subtype="Normal"
)
def t_per_kt_units():
    return 1


@component.add(
    name="t_per_Mt_units", units="t/Mt", comp_type="Constant", comp_subtype="Normal"
)
def t_per_mt_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="tCO2eq_per_GtCO2eq_units",
    units="tCO2eq/GtCO2eq",
    comp_type="Constant",
    comp_subtype="Normal",
)
def tco2eq_per_gtco2eq_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="TJ_per_EJ_units", units="TJ/EJ", comp_type="Constant", comp_subtype="Normal"
)
def tj_per_ej_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="TJ_per_MJ_units", units="TJ/MJ", comp_type="Constant", comp_subtype="Normal"
)
def tj_per_mj_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="TW_per_kW_units", units="TW/kW", comp_type="Constant", comp_subtype="Normal"
)
def tw_per_kw_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="TWh_per_EJ_units", units="TWh/EJ", comp_type="Constant", comp_subtype="Normal"
)
def twh_per_ej_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="UNIT_CONVERISON_Wh_kWh",
    units="w*h/(kW*h)",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "wh_per_kwh_units": 1},
)
def unit_converison_wh_kwh():
    """
    Unit conversion Wh per kWh.
    """
    return float(matrix_unit_prefixes().loc["kilo", "BASE_UNIT"]) * wh_per_kwh_units()


@component.add(
    name="UNIT_CONVERSION_C_CO2",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_unit_conversion_c_co2"},
)
def unit_conversion_c_co2():
    """
    1 g of CO2 contains 3/11 of carbon.
    """
    return _ext_constant_unit_conversion_c_co2()


_ext_constant_unit_conversion_c_co2 = ExtConstant(
    "model_parameters/constants.xlsx",
    "constants",
    "UNIT_CONVERSION_C_CO2",
    {},
    _root,
    {},
    "_ext_constant_unit_conversion_c_co2",
)


@component.add(
    name="UNIT_CONVERSION_CH4_C",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_unit_conversion_ch4_c"},
)
def unit_conversion_ch4_c():
    """
    Molar mass ratio of CH4 to C, 16/12
    """
    return _ext_constant_unit_conversion_ch4_c()


_ext_constant_unit_conversion_ch4_c = ExtConstant(
    "model_parameters/constants.xlsx",
    "constants",
    "UNIT_CONVERSION_CH4_C",
    {},
    _root,
    {},
    "_ext_constant_unit_conversion_ch4_c",
)


@component.add(
    name="UNIT_CONVERSION_DAYS_YEAR",
    units="days/Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_unit_conversion_days_year"},
)
def unit_conversion_days_year():
    """
    Constant: 365 days in a year.
    """
    return _ext_constant_unit_conversion_days_year()


_ext_constant_unit_conversion_days_year = ExtConstant(
    "model_parameters/constants.xlsx",
    "constants",
    "UNIT_CONVERSION_DAYS_YEAR",
    {},
    _root,
    {},
    "_ext_constant_unit_conversion_days_year",
)


@component.add(
    name="UNIT_CONVERSION_dollars_Mdollars",
    units="dollars/Mdollars",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "dollars_per_mdollar": 1},
)
def unit_conversion_dollars_mdollars():
    """
    Unit conversion dollars per Mdollar.
    """
    return (
        float(matrix_unit_prefixes().loc["mega", "BASE_UNIT"]) * dollars_per_mdollar()
    )


@component.add(
    name="UNIT_CONVERSION_g_Mt",
    units="g/Mt",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "g_per_mt_units": 1},
)
def unit_conversion_g_mt():
    """
    Unit conversion g per Mt.
    """
    return float(matrix_unit_prefixes().loc["tera", "BASE_UNIT"]) * g_per_mt_units()


@component.add(
    name="UNIT_CONVERSION_g_t",
    units="g/t",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "g_per_t_units": 1},
)
def unit_conversion_g_t():
    """
    Unit conversion g per t
    """
    return float(matrix_unit_prefixes().loc["mega", "BASE_UNIT"]) * g_per_t_units()


@component.add(
    name="UNIT_CONVERSION_GJ_EJ",
    units="GJ/EJ",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "gj_per_ej_units": 1},
)
def unit_conversion_gj_ej():
    """
    Unit conversion GJ per EJ.
    """
    return float(matrix_unit_prefixes().loc["exa", "giga"]) * gj_per_ej_units()


@component.add(
    name="UNIT_CONVERSION_GtC_ppm",
    units="Gt/ppm",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_unit_conversion_gtc_ppm"},
)
def unit_conversion_gtc_ppm():
    """
    Conversion from ppm to GtC (1 ppm by volume of atmosphere CO2 = 2.13 Gt C (Uses atmospheric mass (Ma) = 5.137 × 10^18 kg)) CDIAC: http://cdiac.ornl.gov/pns/convert.html
    """
    return _ext_constant_unit_conversion_gtc_ppm()


_ext_constant_unit_conversion_gtc_ppm = ExtConstant(
    "model_parameters/constants.xlsx",
    "constants",
    "UNIT_CONVERSION_GtC_ppm",
    {},
    _root,
    {},
    "_ext_constant_unit_conversion_gtc_ppm",
)


@component.add(
    name="UNIT_CONVERSION_GW_TW",
    units="GW/TW",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "gw_per_tw_units": 1},
)
def unit_conversion_gw_tw():
    """
    Unit conversion GW per TW.
    """
    return float(matrix_unit_prefixes().loc["tera", "giga"]) * gw_per_tw_units()


@component.add(
    name="UNIT_CONVERSION_ha_Mha",
    units="ha/MHa",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "ha_per_mha_units": 1},
)
def unit_conversion_ha_mha():
    """
    Unit conversion ha per MHa.
    """
    return float(matrix_unit_prefixes().loc["mega", "BASE_UNIT"]) * ha_per_mha_units()


@component.add(
    name="UNIT_CONVERSION_HOURS_YEAR",
    units="h/Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_unit_conversion_hours_year"},
)
def unit_conversion_hours_year():
    """
    Constant: 8760 hours in a year.
    """
    return _ext_constant_unit_conversion_hours_year()


_ext_constant_unit_conversion_hours_year = ExtConstant(
    "model_parameters/constants.xlsx",
    "constants",
    "UNIT_CONVERSION_HOURS_YEAR",
    {},
    _root,
    {},
    "_ext_constant_unit_conversion_hours_year",
)


@component.add(
    name="UNIT_CONVERSION_J_boe",
    units="J/boe",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_unit_conversion_j_boe"},
)
def unit_conversion_j_boe():
    """
    Constant: 5711869031,31802 jules in a barrel of oil equivalent.
    """
    return _ext_constant_unit_conversion_j_boe()


_ext_constant_unit_conversion_j_boe = ExtConstant(
    "model_parameters/constants.xlsx",
    "Constants",
    "UNIT_CONVERSION_J_boe",
    {},
    _root,
    {},
    "_ext_constant_unit_conversion_j_boe",
)


@component.add(
    name="UNIT_CONVERSION_J_EJ",
    units="J/EJ",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "j_per_ej_units": 1},
)
def unit_conversion_j_ej():
    """
    Unit conversion J per EJ.
    """
    return float(matrix_unit_prefixes().loc["exa", "BASE_UNIT"]) * j_per_ej_units()


@component.add(
    name="UNIT_CONVERSION_J_MJ",
    units="J/MJ",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "j_per_mj_units": 1},
)
def unit_conversion_j_mj():
    """
    Unit conversion J per MJ.
    """
    return float(matrix_unit_prefixes().loc["mega", "BASE_UNIT"]) * j_per_mj_units()


@component.add(
    name="UNIT_CONVERSION_J_TJ",
    units="TJ/J",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "j_per_tj_units": 1},
)
def unit_conversion_j_tj():
    """
    Unit conversion J per TJ
    """
    return float(matrix_unit_prefixes().loc["tera", "BASE_UNIT"]) * j_per_tj_units()


@component.add(
    name="UNIT_CONVERSION_J_toe",
    units="J/toe",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_unit_conversion_j_toe"},
)
def unit_conversion_j_toe():
    """
    Constant: 41867999999,5611 jules in a tonne of oil equivalent.
    """
    return _ext_constant_unit_conversion_j_toe()


_ext_constant_unit_conversion_j_toe = ExtConstant(
    "model_parameters/constants.xlsx",
    "Constants",
    "UNIT_CONVERSION_J_toe",
    {},
    _root,
    {},
    "_ext_constant_unit_conversion_j_toe",
)


@component.add(
    name="UNIT_CONVERSION_J_Wh",
    units="J/(w*h)",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_unit_conversion_j_wh"},
)
def unit_conversion_j_wh():
    """
    Constant: 3600 joules per watt hour.
    """
    return _ext_constant_unit_conversion_j_wh()


_ext_constant_unit_conversion_j_wh = ExtConstant(
    "model_parameters/constants.xlsx",
    "Constants",
    "UNIT_CONVERSION_J_Wh",
    {},
    _root,
    {},
    "_ext_constant_unit_conversion_j_wh",
)


@component.add(
    name="UNIT_CONVERSION_kg_Mt",
    units="kg/Mt",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "kg_per_mt_units": 1},
)
def unit_conversion_kg_mt():
    """
    Unit conversion kg per Mt
    """
    return float(matrix_unit_prefixes().loc["tera", "kilo"]) * kg_per_mt_units()


@component.add(
    name="UNIT_CONVERSION_km2_ha",
    units="km2/ha",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "km2_per_ha_units": 1},
)
def unit_conversion_km2_ha():
    """
    Unit conversion ha per km2
    """
    return float(matrix_unit_prefixes().loc["centi", "BASE_UNIT"]) * km2_per_ha_units()


@component.add(
    name="UNIT_CONVERSION_km3_hm3",
    units="km3/hm3",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "km3_per_hm3_units": 1},
)
def unit_conversion_km3_hm3():
    """
    Unit conversion km3 per hm3.
    """
    return float(matrix_unit_prefixes().loc["hecto", "kilo"]) ** 3 * km3_per_hm3_units()


@component.add(
    name="UNIT_CONVERSION_km_m",
    units="km/m",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "km_per_m_units": 1},
)
def unit_conversion_km_m():
    """
    Unit conversion km per m.
    """
    return float(matrix_unit_prefixes().loc["BASE_UNIT", "kilo"]) * km_per_m_units()


@component.add(
    name="UNIT_CONVERSION_KPEOPLE_PEOPLE",
    units="kpeople/people",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "kpeople_per_people_units": 1},
)
def unit_conversion_kpeople_people():
    """
    Conversion unit for demography to fertility (births/1000people) and mortality rates (deaths/1000people)
    """
    return (
        float(matrix_unit_prefixes().loc["BASE_UNIT", "kilo"])
        * kpeople_per_people_units()
    )


@component.add(
    name="UNIT_CONVERSION_kt_Gt",
    units="Kt/Gt",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "kt_per_gt_units": 1},
)
def unit_conversion_kt_gt():
    return float(matrix_unit_prefixes().loc["mega", "BASE_UNIT"]) * kt_per_gt_units()


@component.add(
    name="UNIT_CONVERSION_kt_URANIUM_EJ",
    units="Kt/EJ",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_unit_conversion_kt_uranium_ej"},
)
def unit_conversion_kt_uranium_ej():
    """
    Unit conversion (1 EJ thermal = 2.3866). See EWG (2006).
    """
    return _ext_constant_unit_conversion_kt_uranium_ej()


_ext_constant_unit_conversion_kt_uranium_ej = ExtConstant(
    "model_parameters/constants.xlsx",
    "Constants",
    "UNIT_CONVERSION_kt_URANIUM_EJ",
    {},
    _root,
    {},
    "_ext_constant_unit_conversion_kt_uranium_ej",
)


@component.add(
    name="UNIT_CONVERSION_kW_MW",
    units="kW/MW",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "kw_per_mw_units": 1},
)
def unit_conversion_kw_mw():
    """
    Unit conversion kW per MW.
    """
    return float(matrix_unit_prefixes().loc["mega", "kilo"]) * kw_per_mw_units()


@component.add(
    name="UNIT_CONVERSION_kWh_TWh",
    units="kW*h/(TW*h)",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "kwh_per_twh_units": 1},
)
def unit_conversion_kwh_twh():
    """
    Unit conversion kWh per TWh.
    """
    return float(matrix_unit_prefixes().loc["tera", "kilo"]) * kwh_per_twh_units()


@component.add(
    name="UNIT_CONVERSION_m2_km2",
    units="m2/km2",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "m2_per_km2_units": 1},
)
def unit_conversion_m2_km2():
    """
    Unit conversion m2 per km2.
    """
    return (
        float(matrix_unit_prefixes().loc["kilo", "BASE_UNIT"]) ** 2 * m2_per_km2_units()
    )


@component.add(
    name="UNIT_CONVERSION_m_mm",
    units="m/mm",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "m_per_mm_units": 1},
)
def unit_conversion_m_mm():
    return float(matrix_unit_prefixes().loc["BASE_UNIT", "kilo"]) * m_per_mm_units()


@component.add(
    name="UNIT_CONVERSION_MILLION_BILLION",
    units="Million_persons/Billon_persons",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "billonperson_per_millonperson_units": 1},
)
def unit_conversion_million_billion():
    """
    Converting from billion people to billion people.
    """
    return (
        float(matrix_unit_prefixes().loc["kilo", "BASE_UNIT"])
        * billonperson_per_millonperson_units()
    )


@component.add(
    name="UNIT_CONVERSION_MJ_EJ",
    units="MJ/EJ",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "mj_per_ej_units": 1},
)
def unit_conversion_mj_ej():
    """
    Unit conversion MJ per EJ
    """
    return float(matrix_unit_prefixes().loc["exa", "mega"]) * mj_per_ej_units()


@component.add(
    name="UNIT_CONVERSION_Mm3_m3",
    units="Mm3/m3",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "mm3_per_m3_units": 1},
)
def unit_conversion_mm3_m3():
    """
    Unit conversion Mm3 per m3.
    """
    return float(matrix_unit_prefixes().loc["BASE_UNIT", "mega"]) * mm3_per_m3_units()


@component.add(
    name="UNIT_CONVERSION_Mt_Bt",
    units="Mt/Bt",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "mt_per_bt_units": 1},
)
def unit_conversion_mt_bt():
    return float(matrix_unit_prefixes().loc["kilo", "BASE_UNIT"]) * mt_per_bt_units()


@component.add(
    name="UNIT_CONVERSION_Mt_Gt",
    units="Mt/Gt",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "mt_per_gt_units": 1},
)
def unit_conversion_mt_gt():
    """
    Unit conversion Mt per Gt
    """
    return float(matrix_unit_prefixes().loc["giga", "mega"]) * mt_per_gt_units()


@component.add(
    name="UNIT_CONVERSION_Mt_kt",
    units="Mt/Kt",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "mt_per_kt_units": 1},
)
def unit_conversion_mt_kt():
    """
    Unit conversion Mt per kt.
    """
    return float(matrix_unit_prefixes().loc["kilo", "mega"]) * mt_per_kt_units()


@component.add(
    name="UNIT_CONVERSION_Mt_t",
    units="Mt/t",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"unit_conversion_t_mt": 1},
)
def unit_conversion_mt_t():
    """
    ton to mega ton
    """
    return 1 / unit_conversion_t_mt()


@component.add(
    name="UNIT_CONVERSION_Mvehicles_vehicles",
    units="Mvehicles/vehicles",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "mvehicles_per_vehicles_units": 1},
)
def unit_conversion_mvehicles_vehicles():
    """
    Unit conversion Mvehicles per vehicles
    """
    return (
        float(matrix_unit_prefixes().loc["BASE_UNIT", "mega"])
        * mvehicles_per_vehicles_units()
    )


@component.add(
    name="UNIT_CONVERSION_MW_TW",
    units="MW/TW",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "mw_per_tw_units": 1},
)
def unit_conversion_mw_tw():
    """
    Unit conversion MW per TW.
    """
    return float(matrix_unit_prefixes().loc["tera", "mega"]) * mw_per_tw_units()


@component.add(
    name="UNIT_CONVERSION_N2ON_N2O",
    units="N2O/N2ON",
    comp_type="Constant",
    comp_subtype="Normal",
)
def unit_conversion_n2on_n2o():
    """
    N2O-N_TO_N2O N2O = N2O-N ? 44/28 (IPCC)
    """
    return 44 / 28


@component.add(
    name="UNIT_CONVERSION_PERCENT_SHARE",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_unit_conversion_percent_share"},
)
def unit_conversion_percent_share():
    """
    Conversion of percent to share.
    """
    return _ext_constant_unit_conversion_percent_share()


_ext_constant_unit_conversion_percent_share = ExtConstant(
    "model_parameters/constants.xlsx",
    "Constants",
    "UNIT_CONVERSION_PERCENT_SHARE",
    {},
    _root,
    {},
    "_ext_constant_unit_conversion_percent_share",
)


@component.add(
    name="UNIT_CONVERSION_PJ_EJ",
    units="PJ/EJ",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "pj_per_ej_units": 1},
)
def unit_conversion_pj_ej():
    """
    Unit conversion PJ per EJ.
    """
    return float(matrix_unit_prefixes().loc["exa", "peta"]) * pj_per_ej_units()


@component.add(
    name="UNIT_CONVERSION_ppt_MOL",
    units="ppt/mol",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_unit_conversion_ppt_mol"},
)
def unit_conversion_ppt_mol():
    """
    Parts per trillion per mol.
    """
    return _ext_constant_unit_conversion_ppt_mol()


_ext_constant_unit_conversion_ppt_mol = ExtConstant(
    "model_parameters/constants.xlsx",
    "Constants",
    "UNIT_CONVERSION_ppt_MOL",
    {},
    _root,
    {},
    "_ext_constant_unit_conversion_ppt_mol",
)


@component.add(
    name="UNIT_CONVERSION_ppt_ppb",
    units="ppt/ppb",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_unit_conversion_ppt_ppb"},
)
def unit_conversion_ppt_ppb():
    """
    Parts-per-trillion per parts-per-billion.
    """
    return _ext_constant_unit_conversion_ppt_ppb()


_ext_constant_unit_conversion_ppt_ppb = ExtConstant(
    "model_parameters/constants.xlsx",
    "Constants",
    "UNIT_CONVERSION_ppt_ppb",
    {},
    _root,
    {},
    "_ext_constant_unit_conversion_ppt_ppb",
)


@component.add(
    name="UNIT_CONVERSION_SECONDS_DAY",
    units="s/day",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_unit_conversion_seconds_day"},
)
def unit_conversion_seconds_day():
    """
    Constant: 86400 seconds in a day.
    """
    return _ext_constant_unit_conversion_seconds_day()


_ext_constant_unit_conversion_seconds_day = ExtConstant(
    "model_parameters/constants.xlsx",
    "constants",
    "UNIT_CONVERSION_SECONDS_DAY",
    {},
    _root,
    {},
    "_ext_constant_unit_conversion_seconds_day",
)


@component.add(
    name="UNIT_CONVERSION_SECONDS_HOUR",
    units="s/Hours",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_unit_conversion_seconds_hour"},
)
def unit_conversion_seconds_hour():
    """
    Constant: 3600 seconds in a hour.
    """
    return _ext_constant_unit_conversion_seconds_hour()


_ext_constant_unit_conversion_seconds_hour = ExtConstant(
    "model_parameters/constants.xlsx",
    "constants",
    "UNIT_CONVERSION_SECONDS_HOUR",
    {},
    _root,
    {},
    "_ext_constant_unit_conversion_seconds_hour",
)


@component.add(
    name="UNIT_CONVERSION_t_Gt",
    units="t/Gt",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "t_per_gt_units": 1},
)
def unit_conversion_t_gt():
    """
    Unit conversion t per Gt
    """
    return float(matrix_unit_prefixes().loc["giga", "BASE_UNIT"]) * t_per_gt_units()


@component.add(
    name="UNIT_CONVERSION_t_kg",
    units="t/kg",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "t_per_kg_units": 1},
)
def unit_conversion_t_kg():
    """
    Unit conversion t per kg.
    """
    return float(matrix_unit_prefixes().loc["kilo", "mega"]) * t_per_kg_units()


@component.add(
    name="UNIT_CONVERSION_t_kt",
    units="t/Kt",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "t_per_kt_units": 1},
)
def unit_conversion_t_kt():
    return float(matrix_unit_prefixes().loc["kilo", "BASE_UNIT"]) * t_per_kt_units()


@component.add(
    name="UNIT_CONVERSION_t_Mt",
    units="t/Mt",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "t_per_mt_units": 1},
)
def unit_conversion_t_mt():
    return float(matrix_unit_prefixes().loc["mega", "BASE_UNIT"]) * t_per_mt_units()


@component.add(
    name="UNIT_CONVERSION_tCO2eq_GtCO2eq",
    units="tCO2eq/GtCO2eq",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "tco2eq_per_gtco2eq_units": 1},
)
def unit_conversion_tco2eq_gtco2eq():
    """
    Unit conversion tCO2eq per GtCO2eq.
    """
    return (
        float(matrix_unit_prefixes().loc["giga", "BASE_UNIT"])
        * tco2eq_per_gtco2eq_units()
    )


@component.add(
    name="UNIT_CONVERSION_TJ_EJ",
    units="TJ/EJ",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "tj_per_ej_units": 1},
)
def unit_conversion_tj_ej():
    """
    Unit conversion TJ per EJ.
    """
    return float(matrix_unit_prefixes().loc["exa", "tera"]) * tj_per_ej_units()


@component.add(
    name="UNIT_CONVERSION_TJ_MJ",
    units="TJ/MJ",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "tj_per_mj_units": 1},
)
def unit_conversion_tj_mj():
    """
    Unit conversion TJ per MJ.
    """
    return float(matrix_unit_prefixes().loc["mega", "tera"]) * tj_per_mj_units()


@component.add(
    name="UNIT_CONVERSION_toe_m3",
    units="toe/m3",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_unit_conversion_toe_m3"},
)
def unit_conversion_toe_m3():
    return _ext_constant_unit_conversion_toe_m3()


_ext_constant_unit_conversion_toe_m3 = ExtConstant(
    "model_parameters/constants.xlsx",
    "Constants",
    "UNIT_CONVERSION_toe_m3",
    {},
    _root,
    {},
    "_ext_constant_unit_conversion_toe_m3",
)


@component.add(
    name="UNIT_CONVERSION_TW_kW",
    units="TW/kW",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "tw_per_kw_units": 1},
)
def unit_conversion_tw_kw():
    """
    Unit conversion TW per kW.
    """
    return float(matrix_unit_prefixes().loc["kilo", "tera"]) * tw_per_kw_units()


@component.add(
    name="UNIT_CONVERSION_TW_PER_EJ_PER_YEAR",
    units="EJ/(TW*h)",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "unit_conversion_j_wh": 1,
        "unit_conversion_w_tw": 1,
        "unit_conversion_j_ej": 1,
    },
)
def unit_conversion_tw_per_ej_per_year():
    return unit_conversion_j_wh() * unit_conversion_w_tw() / unit_conversion_j_ej()


@component.add(
    name="UNIT_CONVERSION_TWh_EJ",
    units="TWh/EJ",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"twh_per_ej_units": 1, "matrix_unit_prefixes": 1},
)
def unit_conversion_twh_ej():
    """
    1 EJ = 1 EJ * (10^6 TJ) * (second/second) = 10^6 TW * s * (1 hour / 3600 seconds) = TWh
    """
    return twh_per_ej_units() * float(matrix_unit_prefixes().loc["exa", "tera"]) / 3600


@component.add(
    name="UNIT_CONVERSION_W_J_s",
    units="w/(J/s)",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_unit_conversion_w_j_s"},
)
def unit_conversion_w_j_s():
    """
    Constant: 1 watt in a jules/second.
    """
    return _ext_constant_unit_conversion_w_j_s()


_ext_constant_unit_conversion_w_j_s = ExtConstant(
    "model_parameters/constants.xlsx",
    "constants",
    "UNIT_CONVERSION_W_J_s",
    {},
    _root,
    {},
    "_ext_constant_unit_conversion_w_j_s",
)


@component.add(
    name="UNIT_CONVERSION_W_kW",
    units="w/kW",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "w_per_kw_units": 1},
)
def unit_conversion_w_kw():
    """
    Unit conversion W per kW.
    """
    return float(matrix_unit_prefixes().loc["kilo", "BASE_UNIT"]) * w_per_kw_units()


@component.add(
    name="UNIT_CONVERSION_W_MW",
    units="w/MW",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "w_per_mw_units": 1},
)
def unit_conversion_w_mw():
    """
    Unit conversion W per MW.
    """
    return float(matrix_unit_prefixes().loc["mega", "BASE_UNIT"]) * w_per_mw_units()


@component.add(
    name="UNIT_CONVERSION_W_TW",
    units="w/TW",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "w_per_tw_units": 1},
)
def unit_conversion_w_tw():
    """
    Unit conversion W per TW.
    """
    return float(matrix_unit_prefixes().loc["tera", "BASE_UNIT"]) * w_per_tw_units()


@component.add(
    name="UNIT_CONVERSION_Wh_We",
    units="Wh/We",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_unit_conversion_wh_we"},
)
def unit_conversion_wh_we():
    """
    Constant: 8760 watt hour in a electric watt.
    """
    return _ext_constant_unit_conversion_wh_we()


_ext_constant_unit_conversion_wh_we = ExtConstant(
    "model_parameters/constants.xlsx",
    "Constants",
    "UNIT_CONVERSION_Wh_We",
    {},
    _root,
    {},
    "_ext_constant_unit_conversion_wh_we",
)


@component.add(
    name="W_per_kW_units", units="w/kW", comp_type="Constant", comp_subtype="Normal"
)
def w_per_kw_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="W_per_MW_units", units="w/TW", comp_type="Constant", comp_subtype="Normal"
)
def w_per_mw_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="W_per_TW_units", units="w/TW", comp_type="Constant", comp_subtype="Normal"
)
def w_per_tw_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="WATER_DENSITY",
    units="kg/(m*m*m)",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_water_density"},
)
def water_density():
    """
    Density of water, i.e., mass per volume of water.
    """
    return _ext_constant_water_density()


_ext_constant_water_density = ExtConstant(
    "model_parameters/constants.xlsx",
    "constants",
    "WATER_DENSITY",
    {},
    _root,
    {},
    "_ext_constant_water_density",
)


@component.add(
    name="Wh_per_kWh_units", units="Wh/kWh", comp_type="Constant", comp_subtype="Normal"
)
def wh_per_kwh_units():
    """
    Units for unit conversion.
    """
    return 1
