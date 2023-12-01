"""
Module climate.exogenous_inputs
Translated using PySD version 3.10.0
"""


@component.add(
    name="ARAGONITE_SATURATION_CONSTANT_1",
    units="1/(pH*pH)",
    comp_type="Constant",
    comp_subtype="Normal",
)
def aragonite_saturation_constant_1():
    """
    Aragonite saturation constant = 3.8731
    """
    return 3.8731


@component.add(
    name="ARAGONITE_SATURATION_CONSTANT_2",
    units="1/pH",
    comp_type="Constant",
    comp_subtype="Normal",
)
def aragonite_saturation_constant_2():
    """
    Aragnite saturation constant = 57.3718
    """
    return 57.3718


@component.add(
    name="BIOSTIMULATION_COEFF_INDEX",
    units="DMNL",
    limits=(0.6, 1.7),
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_biostimulation_coeff_index"},
)
def biostimulation_coeff_index():
    """
    Index of coefficient for response of primary production to carbon concentration, as multiplying factor of the mean value.
    """
    return _ext_constant_biostimulation_coeff_index()


_ext_constant_biostimulation_coeff_index = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "Biostim_coeff_index",
    {},
    _root,
    {},
    "_ext_constant_biostimulation_coeff_index",
)


@component.add(
    name="BIOSTIMULATION_COEFF_MEAN",
    units="DMNL",
    limits=(0.3, 0.7),
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_biostimulation_coeff_mean"},
)
def biostimulation_coeff_mean():
    """
    Mean coefficient for response of primary production to CO2 concentration. Reflects the increase in NPP with doubling the CO2 level. Goudriaan and Ketner, 1984; Rotmans, 1990
    """
    return _ext_constant_biostimulation_coeff_mean()


_ext_constant_biostimulation_coeff_mean = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "Biostim_coeff_mean",
    {},
    _root,
    {},
    "_ext_constant_biostimulation_coeff_mean",
)


@component.add(
    name="BUFF_C_COEFF",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_buff_c_coeff"},
)
def buff_c_coeff():
    """
    Coefficient of CO2 concentration influence on buffer factor.
    """
    return _ext_constant_buff_c_coeff()


_ext_constant_buff_c_coeff = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "Buff_C_Coeff",
    {},
    _root,
    {},
    "_ext_constant_buff_c_coeff",
)


@component.add(
    name="CARBON_BUDGET",
    units="GtonsC",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_carbon_budget"},
)
def carbon_budget():
    """
    Carbon budget, the amount of carbon dioxide emissions we can emit while still having a likely chance of limiting global temperature rise to 2 degrees Celsius above pre-industrial levels (IPCC 2014).
    """
    return _ext_constant_carbon_budget()


_ext_constant_carbon_budget = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "carbon_budget",
    {},
    _root,
    {},
    "_ext_constant_carbon_budget",
)


@component.add(
    name="CF4_MOLAR_MASS",
    units="g/mol",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_cf4_molar_mass"},
)
def cf4_molar_mass():
    """
    Molar mass of CF4.
    """
    return _ext_constant_cf4_molar_mass()


_ext_constant_cf4_molar_mass = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "CF4_molar_mass",
    {},
    _root,
    {},
    "_ext_constant_cf4_molar_mass",
)


@component.add(
    name="CH4_GENERATION_RATE_FROM_BIOMASS",
    units="1/Year",
    limits=(0.0, 0.00014),
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_ch4_generation_rate_from_biomass"},
)
def ch4_generation_rate_from_biomass():
    """
    The rate of the natural flux of methane from C in biomass. The sum of the flux of methane from C in humus and the flux of methane from C in biomass yields the natural emissions of methane.
    """
    return _ext_constant_ch4_generation_rate_from_biomass()


_ext_constant_ch4_generation_rate_from_biomass = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "CH4_Generation_Rate_from_Biomass",
    {},
    _root,
    {},
    "_ext_constant_ch4_generation_rate_from_biomass",
)


@component.add(
    name="CH4_GENERATION_RATE_FROM_HUMUS",
    units="1/Year",
    limits=(0.0, 0.00016),
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_ch4_generation_rate_from_humus"},
)
def ch4_generation_rate_from_humus():
    """
    The rate of the natural flux of methane from C in humus. The sum of the flux of methane from C in humus and the flux of methane from C in biomass yields the natural emissions of methane.
    """
    return _ext_constant_ch4_generation_rate_from_humus()


_ext_constant_ch4_generation_rate_from_humus = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "CH4_Generation_Rate_from_Humus",
    {},
    _root,
    {},
    "_ext_constant_ch4_generation_rate_from_humus",
)


@component.add(
    name="CH4_MOLAR_MASS",
    units="g/mol",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_ch4_molar_mass"},
)
def ch4_molar_mass():
    """
    Molar mass of CH4.
    """
    return _ext_constant_ch4_molar_mass()


_ext_constant_ch4_molar_mass = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "CH4_molar_mass",
    {},
    _root,
    {},
    "_ext_constant_ch4_molar_mass",
)


@component.add(
    name="CH4_N20_INTER_EXP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_ch4_n20_inter_exp"},
)
def ch4_n20_inter_exp():
    """
    First exponent of CH4 N2O interaction. AR5 WG1 Chapter 8 Anthropogenic and Natural Radiative Forcing. Table 8.SM.1 Supplementary for Table 8.3: RF formulae for CO2, CH4 and N2O.
    """
    return _ext_constant_ch4_n20_inter_exp()


_ext_constant_ch4_n20_inter_exp = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "CH4_N20_inter_exp",
    {},
    _root,
    {},
    "_ext_constant_ch4_n20_inter_exp",
)


@component.add(
    name="CH4_N20_INTER_EXP_2",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_ch4_n20_inter_exp_2"},
)
def ch4_n20_inter_exp_2():
    """
    Second exponent of CH4 N2O interaction. AR5 WG1 Chapter 8 Anthropogenic and Natural Radiative Forcing. Table 8.SM.1 Supplementary for Table 8.3: RF formulae for CO2, CH4 and N2O.
    """
    return _ext_constant_ch4_n20_inter_exp_2()


_ext_constant_ch4_n20_inter_exp_2 = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "CH4_N20_inter_exp_2",
    {},
    _root,
    {},
    "_ext_constant_ch4_n20_inter_exp_2",
)


@component.add(
    name="CH4_N2O_INTER_COEF_2",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_ch4_n2o_inter_coef_2"},
)
def ch4_n2o_inter_coef_2():
    """
    Coefficient of CH4 N2O interaction. AR5 WG1 Chapter 8 Anthropogenic and Natural Radiative Forcing. Table 8.SM.1 Supplementary for Table 8.3: RF formulae for CO2, CH4 and N2O.
    """
    return _ext_constant_ch4_n2o_inter_coef_2()


_ext_constant_ch4_n2o_inter_coef_2 = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "CH4_N2O_inter_coef_2",
    {},
    _root,
    {},
    "_ext_constant_ch4_n2o_inter_coef_2",
)


@component.add(
    name="CH4_N2O_INTER_COEF_3",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_ch4_n2o_inter_coef_3"},
)
def ch4_n2o_inter_coef_3():
    """
    Coefficient of CH4 N2O interaction. AR5 WG1 Chapter 8 Anthropogenic and Natural Radiative Forcing. Table 8.SM.1 Supplementary for Table 8.3: RF formulae for CO2, CH4 and N2O.
    """
    return _ext_constant_ch4_n2o_inter_coef_3()


_ext_constant_ch4_n2o_inter_coef_3 = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "CH4_N2O_inter_coef_3",
    {},
    _root,
    {},
    "_ext_constant_ch4_n2o_inter_coef_3",
)


@component.add(
    name="CH4_N2O_INTERACTION_COEFFIENT",
    units="w/(m*m)",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_ch4_n2o_interaction_coeffient"},
)
def ch4_n2o_interaction_coeffient():
    """
    Coefficient of CH4 N2O interaction. AR5 WG1 Chapter 8 Anthropogenic and Natural Radiative Forcing. Table 8.SM.1 Supplementary for Table 8.3: RF formulae for CO2, CH4 and N2O.
    """
    return _ext_constant_ch4_n2o_interaction_coeffient()


_ext_constant_ch4_n2o_interaction_coeffient = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "CH4_N2O_interaction_coeffient",
    {},
    _root,
    {},
    "_ext_constant_ch4_n2o_interaction_coeffient",
)


@component.add(
    name="CH4_N2O_UNIT_ADJ",
    units="1/ppb",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_ch4_n2o_unit_adj"},
)
def ch4_n2o_unit_adj():
    """
    Normalizes units to avoid dimensioned variable in exponent
    """
    return _ext_constant_ch4_n2o_unit_adj()


_ext_constant_ch4_n2o_unit_adj = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "CH4_N2O_unit_adj",
    {},
    _root,
    {},
    "_ext_constant_ch4_n2o_unit_adj",
)


@component.add(
    name="CH4_RADIATIVE_EFFICIENCY_COEFFICIENT",
    units="w/(m*m)",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_ch4_radiative_efficiency_coefficient"},
)
def ch4_radiative_efficiency_coefficient():
    """
    AR5 WG1 Chapter 8 Anthropogenic and Natural Radiative Forcing. Table 8.SM.1 Supplementary for Table 8.3: RF formulae for CO2, CH4 and N2O.
    """
    return _ext_constant_ch4_radiative_efficiency_coefficient()


_ext_constant_ch4_radiative_efficiency_coefficient = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "CH4_radiative_efficiency_coefficient",
    {},
    _root,
    {},
    "_ext_constant_ch4_radiative_efficiency_coefficient",
)


@component.add(
    name="CH4_REFERENCE_CONC",
    units="ppb",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_ch4_reference_conc"},
)
def ch4_reference_conc():
    """
    WG1AR5_Chapter08_FINAL.pdf. https://www.ipcc.ch/pdf/assessment-report/ar5/wg1/WG1AR5_Chapter08_FINAL.pd f 722 ± 25 ppb
    """
    return _ext_constant_ch4_reference_conc()


_ext_constant_ch4_reference_conc = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "CH4_reference_conc",
    {},
    _root,
    {},
    "_ext_constant_ch4_reference_conc",
)


@component.add(
    name="CH4_TOTAL_ANTHRO_REST_OF_EMISSIONS_RCP",
    units="Mt/Year",
    subscripts=["REGIONS_9_I", "RCP_Scenario"],
    comp_type="Data",
    comp_subtype="Normal",
    depends_on={"global_ch4_anthro_emissions_rcp": 4, "number_of_regions": 4},
)
def ch4_total_anthro_rest_of_emissions_rcp():
    """
    "Representative Concentration Pathways" (RCPs, see http://tntcat.iiasa.ac.at:8787/RcpDb/dsd?Action=htmlpage&page=compare) data, TODO: except "Power Plants, Energy Conversion, Extraction, and Distribution" and "agriculture: animals, rice, soil"
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "RCP_Scenario": _subscript_dict["RCP_Scenario"],
        },
        ["REGIONS_9_I", "RCP_Scenario"],
    )
    value.loc[:, ["RCP26"]] = (
        float(global_ch4_anthro_emissions_rcp().loc["RCP26"]) / number_of_regions()
    )
    value.loc[:, ["RCP45"]] = (
        float(global_ch4_anthro_emissions_rcp().loc["RCP45"]) / number_of_regions()
    )
    value.loc[:, ["RCP60"]] = (
        float(global_ch4_anthro_emissions_rcp().loc["RCP60"]) / number_of_regions()
    )
    value.loc[:, ["RCP85"]] = (
        float(global_ch4_anthro_emissions_rcp().loc["RCP85"]) / number_of_regions()
    )
    return value


@component.add(
    name="CLIMATE_SENSITIVITY_SP",
    units="DegreesC",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_climate_sensitivity_sp"},
)
def climate_sensitivity_sp():
    """
    Equilibrium Climate Sensitivity hypothesis. It is the amount of global warming over hundreds of years after a doubling of the atmospheric CO2 concentration. There is a high uncertainty about this parameter. [Fiddaman] Equilibrium temperature change in response to a 2xCO2 equivalent change in radiative forcing. /2.908 /. [DICE-2013R] t2xco2 Equilibrium temp impact (ºC per doubling CO2) /2.9 /
    """
    return _ext_constant_climate_sensitivity_sp()


_ext_constant_climate_sensitivity_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "climate",
    "Climate_Sensitivity",
    {},
    _root,
    {},
    "_ext_constant_climate_sensitivity_sp",
)


@component.add(
    name="CO2_MAUNA_LOA",
    units="ppm",
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_co2_mauna_loa",
        "__data__": "_ext_data_co2_mauna_loa",
        "time": 1,
    },
)
def co2_mauna_loa():
    """
    Mauna Loa CO2 annual mean data. (https://www.esrl.noaa.gov/gmd/ccgg/trends/data.html)
    """
    return _ext_data_co2_mauna_loa(time())


_ext_data_co2_mauna_loa = ExtData(
    "model_parameters/climate/climate.xlsx",
    "World",
    "time_index_ppm",
    "ppm",
    "interpolate",
    {},
    _root,
    {},
    "_ext_data_co2_mauna_loa",
)


@component.add(
    name="CO2_RAD_FORCE_COEFFICIENT",
    units="w/(m*m)",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_co2_rad_force_coefficient"},
)
def co2_rad_force_coefficient():
    """
    Coefficient of Radiative Forcing from CO2 From IPCC
    """
    return _ext_constant_co2_rad_force_coefficient()


_ext_constant_co2_rad_force_coefficient = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "CO2_Rad_Force_C_ROADS",
    {},
    _root,
    {},
    "_ext_constant_co2_rad_force_coefficient",
)


@component.add(
    name="CUMULATIVE_CO2_EMISSIONS_TO_2005",
    units="Gt",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"cumulative_co2_emissions_to_2005_w": 1, "number_of_regions": 1},
)
def cumulative_co2_emissions_to_2005():
    """
    Cumulative CO2 emissions 1751-1995 due to fossil fuel combustion, cement production and land-use changes.
    """
    return xr.DataArray(
        cumulative_co2_emissions_to_2005_w() / number_of_regions(),
        {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
        ["REGIONS_9_I"],
    )


@component.add(
    name="CUMULATIVE_CO2_EMISSIONS_TO_2005_W",
    units="GtonsCO2",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_cumulative_co2_emissions_to_2005_w"},
)
def cumulative_co2_emissions_to_2005_w():
    """
    Cumulative CO2 emissions 1751-2005 due to fossil fuel combustion, cement production and land-use changes.
    """
    return _ext_constant_cumulative_co2_emissions_to_2005_w()


_ext_constant_cumulative_co2_emissions_to_2005_w = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "Cumulative_CO2_emissions_1751_2005",
    {},
    _root,
    {},
    "_ext_constant_cumulative_co2_emissions_to_2005_w",
)


@component.add(
    name="ECDF_ECS_AR5_lt",
    units="DegreesC",
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_ecdf_ecs_ar5_lt",
        "__lookup__": "_ext_lookup_ecdf_ecs_ar5_lt",
    },
)
def ecdf_ecs_ar5_lt(x, final_subs=None):
    """
    Empirical cumulative distribution function (ECDF) of the Equilibrium Climate Sensitivity (ECS) as estimated by Rogelj et al (2014) and used in the IPCC AR5 WGIII for the standardization of the climate outputs of the IAMs.
    """
    return _ext_lookup_ecdf_ecs_ar5_lt(x, final_subs)


_ext_lookup_ecdf_ecs_ar5_lt = ExtLookup(
    "model_parameters/climate/climate.xlsx",
    "World",
    "ECDF_ECS_AR5",
    "temp_AR5",
    {},
    _root,
    {},
    "_ext_lookup_ecdf_ecs_ar5_lt",
)


@component.add(
    name="EDDY_DIFF_COEFF_INDEX",
    units="DMNL",
    limits=(0.85, 1.15),
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_eddy_diff_coeff_index"},
)
def eddy_diff_coeff_index():
    """
    Index of coefficient for rate at which carbon is mixed in the ocean due to eddy motion, where 1 is equivalent to the expected value (defaulted to 4400 meter*meter/year).
    """
    return _ext_constant_eddy_diff_coeff_index()


_ext_constant_eddy_diff_coeff_index = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "Eddy_diff_coeff_index",
    {},
    _root,
    {},
    "_ext_constant_eddy_diff_coeff_index",
)


@component.add(
    name="EDDY_DIFF_MEAN",
    units="m*m/Year",
    limits=(2000.0, 8000.0),
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_eddy_diff_mean"},
)
def eddy_diff_mean():
    """
    Rate of vertical transport and mixing in the ocean due to eddy diffusion motion.
    """
    return _ext_constant_eddy_diff_mean()


_ext_constant_eddy_diff_mean = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "Eddy_diff_mean",
    {},
    _root,
    {},
    "_ext_constant_eddy_diff_mean",
)


@component.add(
    name="GISS_NASA_TEMPERATURE",
    units="DegreesC",
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_giss_nasa_temperature",
        "__data__": "_ext_data_giss_nasa_temperature",
        "time": 1,
    },
)
def giss_nasa_temperature():
    """
    GISS NASA Temperature.https://data.giss.nasa.gov/gistemp/graphs/
    """
    return _ext_data_giss_nasa_temperature(time())


_ext_data_giss_nasa_temperature = ExtData(
    "model_parameters/climate/climate.xlsx",
    "World",
    "time_index_temp_NASA",
    "temp_NASA",
    "interpolate",
    {},
    _root,
    {},
    "_ext_data_giss_nasa_temperature",
)


@component.add(
    name="GLOBAL_CH4_ANTHRO_EMISSIONS_RCP",
    units="Mt/Year",
    subscripts=["RCP_SCENARIO_I"],
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_global_ch4_anthro_emissions_rcp",
        "__data__": "_ext_data_global_ch4_anthro_emissions_rcp",
        "time": 1,
    },
)
def global_ch4_anthro_emissions_rcp():
    """
    "Representative Concentration Pathways" (RCPs, see http://tntcat.iiasa.ac.at:8787/RcpDb/dsd?Action=htmlpage&page=compare)
    """
    return _ext_data_global_ch4_anthro_emissions_rcp(time())


_ext_data_global_ch4_anthro_emissions_rcp = ExtData(
    "model_parameters/climate/climate.xlsx",
    "World",
    "TIME_INDEX",
    "CH4_emissions",
    "interpolate",
    {"RCP_SCENARIO_I": _subscript_dict["RCP_SCENARIO_I"]},
    _root,
    {"RCP_SCENARIO_I": _subscript_dict["RCP_SCENARIO_I"]},
    "_ext_data_global_ch4_anthro_emissions_rcp",
)


@component.add(
    name="GLOBAL_HFC_EMISSIONS_RCP_2_6",
    units="t/Year",
    subscripts=["HFC_TYPE_I"],
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_global_hfc_emissions_rcp_2_6",
        "__data__": "_ext_data_global_hfc_emissions_rcp_2_6",
        "time": 1,
    },
)
def global_hfc_emissions_rcp_2_6():
    """
    Historic data + projections "Representative Concentration Pathways" (RCPs, see http://tntcat.iiasa.ac.at:8787/RcpDb/dsd?Action=htmlpage&page=compare)
    """
    return _ext_data_global_hfc_emissions_rcp_2_6(time())


_ext_data_global_hfc_emissions_rcp_2_6 = ExtData(
    "model_parameters/climate/climate.xlsx",
    "World",
    "time_index_RCP",
    "HFCs_RCP_2_6",
    "interpolate",
    {"HFC_TYPE_I": _subscript_dict["HFC_TYPE_I"]},
    _root,
    {"HFC_TYPE_I": _subscript_dict["HFC_TYPE_I"]},
    "_ext_data_global_hfc_emissions_rcp_2_6",
)


@component.add(
    name="GLOBAL_HFC_EMISSIONS_RCP_4_5",
    units="t/Year",
    subscripts=["HFC_TYPE_I"],
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_global_hfc_emissions_rcp_4_5",
        "__data__": "_ext_data_global_hfc_emissions_rcp_4_5",
        "time": 1,
    },
)
def global_hfc_emissions_rcp_4_5():
    """
    Historic data + projections "Representative Concentration Pathways" (RCPs, see http://tntcat.iiasa.ac.at:8787/RcpDb/dsd?Action=htmlpage&page=compare)
    """
    return _ext_data_global_hfc_emissions_rcp_4_5(time())


_ext_data_global_hfc_emissions_rcp_4_5 = ExtData(
    "model_parameters/climate/climate.xlsx",
    "World",
    "time_index_RCP",
    "HFCs_RCP_4_5",
    "interpolate",
    {"HFC_TYPE_I": _subscript_dict["HFC_TYPE_I"]},
    _root,
    {"HFC_TYPE_I": _subscript_dict["HFC_TYPE_I"]},
    "_ext_data_global_hfc_emissions_rcp_4_5",
)


@component.add(
    name="GLOBAL_HFC_EMISSIONS_RCP_6_0",
    units="t/Year",
    subscripts=["HFC_TYPE_I"],
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_global_hfc_emissions_rcp_6_0",
        "__data__": "_ext_data_global_hfc_emissions_rcp_6_0",
        "time": 1,
    },
)
def global_hfc_emissions_rcp_6_0():
    """
    Historic data + projections "Representative Concentration Pathways" (RCPs, see http://tntcat.iiasa.ac.at:8787/RcpDb/dsd?Action=htmlpage&page=compare)
    """
    return _ext_data_global_hfc_emissions_rcp_6_0(time())


_ext_data_global_hfc_emissions_rcp_6_0 = ExtData(
    "model_parameters/climate/climate.xlsx",
    "World",
    "time_index_RCP",
    "HFCs_RCP_6",
    "interpolate",
    {"HFC_TYPE_I": _subscript_dict["HFC_TYPE_I"]},
    _root,
    {"HFC_TYPE_I": _subscript_dict["HFC_TYPE_I"]},
    "_ext_data_global_hfc_emissions_rcp_6_0",
)


@component.add(
    name="GLOBAL_HFC_EMISSIONS_RCP_8_5",
    units="t/Year",
    subscripts=["HFC_TYPE_I"],
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_global_hfc_emissions_rcp_8_5",
        "__data__": "_ext_data_global_hfc_emissions_rcp_8_5",
        "time": 1,
    },
)
def global_hfc_emissions_rcp_8_5():
    """
    Historic data + projections "Representative Concentration Pathways" (RCPs, see http://tntcat.iiasa.ac.at:8787/RcpDb/dsd?Action=htmlpage&page=compare)
    """
    return _ext_data_global_hfc_emissions_rcp_8_5(time())


_ext_data_global_hfc_emissions_rcp_8_5 = ExtData(
    "model_parameters/climate/climate.xlsx",
    "World",
    "time_index_RCP",
    "HFCs_RCP_8_5",
    "interpolate",
    {"HFC_TYPE_I": _subscript_dict["HFC_TYPE_I"]},
    _root,
    {"HFC_TYPE_I": _subscript_dict["HFC_TYPE_I"]},
    "_ext_data_global_hfc_emissions_rcp_8_5",
)


@component.add(
    name="GLOBAL_N2O_ANTHRO_EMISSIONS_RCP",
    units="Mt/Year",
    subscripts=["RCP_SCENARIO_I"],
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_global_n2o_anthro_emissions_rcp",
        "__data__": "_ext_data_global_n2o_anthro_emissions_rcp",
        "time": 1,
    },
)
def global_n2o_anthro_emissions_rcp():
    """
    Historic data + projections "Representative Concentration Pathways" (RCPs, see http://tntcat.iiasa.ac.at:8787/RcpDb/dsd?Action=htmlpage&page=compare)
    """
    return _ext_data_global_n2o_anthro_emissions_rcp(time())


_ext_data_global_n2o_anthro_emissions_rcp = ExtData(
    "model_parameters/climate/climate.xlsx",
    "World",
    "TIME_INDEX",
    "N2O_emissions",
    "interpolate",
    {"RCP_SCENARIO_I": _subscript_dict["RCP_SCENARIO_I"]},
    _root,
    {"RCP_SCENARIO_I": _subscript_dict["RCP_SCENARIO_I"]},
    "_ext_data_global_n2o_anthro_emissions_rcp",
)


@component.add(
    name="GLOBAL_PFC_EMISSIONS_RCP",
    units="t/Year",
    subscripts=["RCP_SCENARIO_I"],
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_global_pfc_emissions_rcp",
        "__data__": "_ext_data_global_pfc_emissions_rcp",
        "time": 1,
    },
)
def global_pfc_emissions_rcp():
    """
    Historic data + projections "Representative Concentration Pathways" (RCPs, see http://tntcat.iiasa.ac.at:8787/RcpDb/dsd?Action=htmlpage&page=compare)
    """
    return _ext_data_global_pfc_emissions_rcp(time())


_ext_data_global_pfc_emissions_rcp = ExtData(
    "model_parameters/climate/climate.xlsx",
    "World",
    "time_index_RCP",
    "PFCs_emissions",
    "interpolate",
    {"RCP_SCENARIO_I": _subscript_dict["RCP_SCENARIO_I"]},
    _root,
    {"RCP_SCENARIO_I": _subscript_dict["RCP_SCENARIO_I"]},
    "_ext_data_global_pfc_emissions_rcp",
)


@component.add(
    name="GLOBAL_SF6_EMISSIONS_RCP",
    units="t/Year",
    subscripts=["RCP_SCENARIO_I"],
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_global_sf6_emissions_rcp",
        "__data__": "_ext_data_global_sf6_emissions_rcp",
        "time": 1,
    },
)
def global_sf6_emissions_rcp():
    """
    Historic data + projections "Representative Concentration Pathways" (RCPs, see http://tntcat.iiasa.ac.at:8787/RcpDb/dsd?Action=htmlpage&page=compare)
    """
    return _ext_data_global_sf6_emissions_rcp(time())


_ext_data_global_sf6_emissions_rcp = ExtData(
    "model_parameters/climate/climate.xlsx",
    "World",
    "time_index_RCP",
    "SF6_emissions",
    "interpolate",
    {"RCP_SCENARIO_I": _subscript_dict["RCP_SCENARIO_I"]},
    _root,
    {"RCP_SCENARIO_I": _subscript_dict["RCP_SCENARIO_I"]},
    "_ext_data_global_sf6_emissions_rcp",
)


@component.add(
    name="GLOBAL_SURFACE_AREA",
    units="m*m",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_global_surface_area"},
)
def global_surface_area():
    """
    Global surface area.
    """
    return _ext_constant_global_surface_area()


_ext_constant_global_surface_area = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "area",
    {},
    _root,
    {},
    "_ext_constant_global_surface_area",
)


@component.add(
    name="GWP_100_YEAR",
    units="tCO2eq/t",
    subscripts=["GHG_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_gwp_100_year"},
)
def gwp_100_year():
    """
    Warming caused by any greenhouse gas in 100 years as a multiple of the warming caused by the same mass of carbon dioxide (CO2). GWP is 1 for CO2.
    """
    return _ext_constant_gwp_100_year()


_ext_constant_gwp_100_year = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "GWP_100*",
    {"GHG_I": _subscript_dict["GHG_I"]},
    _root,
    {"GHG_I": _subscript_dict["GHG_I"]},
    "_ext_constant_gwp_100_year",
)


@component.add(
    name="GWP_20_YEAR",
    units="tCO2eq/t",
    subscripts=["GHG_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_gwp_20_year"},
)
def gwp_20_year():
    """
    Warming caused by any greenhouse gas in 20 years as a multiple of the warming caused by the same mass of carbon dioxide (CO2). GWP is 1 for CO2.
    """
    return _ext_constant_gwp_20_year()


_ext_constant_gwp_20_year = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "GWP_20*",
    {"GHG_I": _subscript_dict["GHG_I"]},
    _root,
    {"GHG_I": _subscript_dict["GHG_I"]},
    "_ext_constant_gwp_20_year",
)


@component.add(
    name="HADCRUT4_TEMPERATURE",
    units="DegreesC",
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_hadcrut4_temperature",
        "__data__": "_ext_data_hadcrut4_temperature",
        "time": 1,
    },
)
def hadcrut4_temperature():
    """
    HadCRUT4 Temperature Data https://www.metoffice.gov.uk/hadobs/hadcrut4/data/current/download.html
    """
    return _ext_data_hadcrut4_temperature(time())


_ext_data_hadcrut4_temperature = ExtData(
    "model_parameters/climate/climate.xlsx",
    "World",
    "time_index_temp_HadCRUT4",
    "temp_HadCRUT4",
    "interpolate",
    {},
    _root,
    {},
    "_ext_data_hadcrut4_temperature",
)


@component.add(
    name="HEAT_DIFFUSION_COVAR",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_heat_diffusion_covar"},
)
def heat_diffusion_covar():
    """
    Fraction of heat transfer that depends on eddy diffusion.
    """
    return _ext_constant_heat_diffusion_covar()


_ext_constant_heat_diffusion_covar = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "Heat_Diffusion_Covar",
    {},
    _root,
    {},
    "_ext_constant_heat_diffusion_covar",
)


@component.add(
    name="HEAT_TRANSFER_RATE",
    units="w/(m*m)/DegreesC",
    limits=(0.0, 2.0),
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_heat_transfer_rate"},
)
def heat_transfer_rate():
    """
    Heat transfer rate.
    """
    return _ext_constant_heat_transfer_rate()


_ext_constant_heat_transfer_rate = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "Heat_Transfer_Rate",
    {},
    _root,
    {},
    "_ext_constant_heat_transfer_rate",
)


@component.add(
    name="HFC_MOLAR_MASS",
    units="g/mol",
    subscripts=["HFC_TYPE_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_hfc_molar_mass"},
)
def hfc_molar_mass():
    """
    http://www.qc.ec.gc.ca/dpe/publication/enjeux_ges/hfc134a_a.html
    """
    return _ext_constant_hfc_molar_mass()


_ext_constant_hfc_molar_mass = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "HFC_molar_mass*",
    {"HFC_TYPE_I": _subscript_dict["HFC_TYPE_I"]},
    _root,
    {"HFC_TYPE_I": _subscript_dict["HFC_TYPE_I"]},
    "_ext_constant_hfc_molar_mass",
)


@component.add(
    name="HFC_RADIATIVE_EFFICIENCY",
    units="w/(ppb*m*m)",
    subscripts=["HFC_TYPE_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_hfc_radiative_efficiency"},
)
def hfc_radiative_efficiency():
    """
    From AR5 WG1 Chapter 8. Table 8.A.1. Lifetimes, Radiative Efficiencies and Metric Values
    """
    return _ext_constant_hfc_radiative_efficiency()


_ext_constant_hfc_radiative_efficiency = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "HFC_radiative_efficiency*",
    {"HFC_TYPE_I": _subscript_dict["HFC_TYPE_I"]},
    _root,
    {"HFC_TYPE_I": _subscript_dict["HFC_TYPE_I"]},
    "_ext_constant_hfc_radiative_efficiency",
)


@component.add(
    name="HISTORIC_SEA_LEVEL_RISE",
    units="mm",
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_historic_sea_level_rise",
        "__data__": "_ext_data_historic_sea_level_rise",
        "time": 1,
    },
)
def historic_sea_level_rise():
    """
    Historic data of sea-level rise,
    """
    return _ext_data_historic_sea_level_rise(time())


_ext_data_historic_sea_level_rise = ExtData(
    "model_parameters/climate/climate.xlsx",
    "World",
    "time_SLR",
    "SLR",
    "interpolate",
    {},
    _root,
    {},
    "_ext_data_historic_sea_level_rise",
)


@component.add(
    name="HUMIFICATION_FRACTION",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_humification_fraction"},
)
def humification_fraction():
    """
    Fraction of carbon outflow from biomass that enters humus stock.
    """
    return _ext_constant_humification_fraction()


_ext_constant_humification_fraction = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "Humification_Fraction",
    {},
    _root,
    {},
    "_ext_constant_humification_fraction",
)


@component.add(
    name="HUMUS_RES_TIME",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_humus_res_time"},
)
def humus_res_time():
    """
    Average carbon residence time in humus.
    """
    return _ext_constant_humus_res_time()


_ext_constant_humus_res_time = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "Humus_Res_Time",
    {},
    _root,
    {},
    "_ext_constant_humus_res_time",
)


@component.add(
    name="INIT_ATMOS_UOCEAN_TEMP",
    units="DegreesC",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_init_atmos_uocean_temp"},
)
def init_atmos_uocean_temp():
    """
    Global Annual Temperature Anomaly (Land + Ocean) in 1990 from NASA GISS Surface Temperature (GISTEMP): +0.43 ºC. 5-year average: +0.36 ºC. Average 1880-1889 = -0,225. Preindustrial reference: W,36 + W,225 = W,585 http://cdiac.ornl.gov/ftp/trends/temp/hansen/gl_land_ocean.txt
    """
    return _ext_constant_init_atmos_uocean_temp()


_ext_constant_init_atmos_uocean_temp = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "init_Atmos_UOcean_Temp",
    {},
    _root,
    {},
    "_ext_constant_init_atmos_uocean_temp",
)


@component.add(
    name="INIT_C_IN_BIOMASS",
    units="Gt",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_init_c_in_biomass"},
)
def init_c_in_biomass():
    """
    Initial carbon in biomass.
    """
    return _ext_constant_init_c_in_biomass()


_ext_constant_init_c_in_biomass = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "Init_C_in_Biomass",
    {},
    _root,
    {},
    "_ext_constant_init_c_in_biomass",
)


@component.add(
    name="INIT_C_IN_DEEP_OCEAN_PER_METER",
    units="Gt/m",
    subscripts=["LAYERS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_init_c_in_deep_ocean_per_meter"},
)
def init_c_in_deep_ocean_per_meter():
    """
    Initial carbon concentration in deep ocean layers.
    """
    return _ext_constant_init_c_in_deep_ocean_per_meter()


_ext_constant_init_c_in_deep_ocean_per_meter = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "Init_C_in_Deep_Ocean_per_meter*",
    {"LAYERS_I": _subscript_dict["LAYERS_I"]},
    _root,
    {"LAYERS_I": _subscript_dict["LAYERS_I"]},
    "_ext_constant_init_c_in_deep_ocean_per_meter",
)


@component.add(
    name="INIT_C_IN_HUMUS",
    units="Gt",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_init_c_in_humus"},
)
def init_c_in_humus():
    """
    Inital carbon in humus.
    """
    return _ext_constant_init_c_in_humus()


_ext_constant_init_c_in_humus = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "Init_C_in_Humus",
    {},
    _root,
    {},
    "_ext_constant_init_c_in_humus",
)


@component.add(
    name="INIT_C_IN_MIXED_OCEAN_PER_METER",
    units="Gt/m",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_init_c_in_mixed_ocean_per_meter"},
)
def init_c_in_mixed_ocean_per_meter():
    """
    Initial carbon in mixed ocean layer.
    """
    return _ext_constant_init_c_in_mixed_ocean_per_meter()


_ext_constant_init_c_in_mixed_ocean_per_meter = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "Init_C_in_Mixed_Ocean_per_meter",
    {},
    _root,
    {},
    "_ext_constant_init_c_in_mixed_ocean_per_meter",
)


@component.add(
    name="INIT_CO2_IN_ATMOSPHERE_PPM",
    units="ppm",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_init_co2_in_atmosphere_ppm"},
)
def init_co2_in_atmosphere_ppm():
    """
    Initial CO2 in atmosphere. Historical Mauna Loa CO2 Record: Average between 1st and last month of 1990 was: (353.74+355.12)/2=354.43 ppm Historical Mauna Loa CO2 Record: Average between 1st and last month of 1995 was: (359.92+360.68)/2= 360.3 ppm ftp://ftp.cmdl.noaa.gov/products/trends/co2/co2_mm_mlo.txt [DICE-1994] Initial Greenhouse Gases in Atmosphere 1965 [M(t)] (tC equivalent). [Cowles, pg. 21] /6.77e+011 / [DICE-2013R] mat0: Initial concentration in atmosphere 2010 (GtC) /830.4 /
    """
    return _ext_constant_init_co2_in_atmosphere_ppm()


_ext_constant_init_co2_in_atmosphere_ppm = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "init_CO2_in_Atmos_ppm",
    {},
    _root,
    {},
    "_ext_constant_init_co2_in_atmosphere_ppm",
)


@component.add(
    name="INIT_DEEP_OCEAN_TEMP",
    units="DegreesC",
    subscripts=["LAYERS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_init_deep_ocean_temp"},
)
def init_deep_ocean_temp():
    """
    C-ROADS simulation
    """
    return _ext_constant_init_deep_ocean_temp()


_ext_constant_init_deep_ocean_temp = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "Init_Deep_Ocean_Temp*",
    {"LAYERS_I": _subscript_dict["LAYERS_I"]},
    _root,
    {"LAYERS_I": _subscript_dict["LAYERS_I"]},
    "_ext_constant_init_deep_ocean_temp",
)


@component.add(
    name="INIT_NPP",
    units="GtonsC/Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_init_npp"},
)
def init_npp():
    """
    Initial net primary production. Adapted from Goudriaan, 1984.
    """
    return _ext_constant_init_npp()


_ext_constant_init_npp = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "Init_NPP",
    {},
    _root,
    {},
    "_ext_constant_init_npp",
)


@component.add(
    name="INIT_PFC_IN_ATM_CON",
    units="ppt",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_init_pfc_in_atm_con"},
)
def init_pfc_in_atm_con():
    """
    Historical data. NASA. GISS. https://data.giss.nasa.gov/modelforce/ghgases/
    """
    return _ext_constant_init_pfc_in_atm_con()


_ext_constant_init_pfc_in_atm_con = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "Init_PFC_in_Atm",
    {},
    _root,
    {},
    "_ext_constant_init_pfc_in_atm_con",
)


@component.add(
    name="INITAL_HFC_CON",
    units="ppt",
    subscripts=["HFC_TYPE_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_inital_hfc_con"},
)
def inital_hfc_con():
    """
    Historical data. NASA. GISS. https://data.giss.nasa.gov/modelforce/ghgases/
    """
    return _ext_constant_inital_hfc_con()


_ext_constant_inital_hfc_con = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "Initial_HFC_con*",
    {"HFC_TYPE_I": _subscript_dict["HFC_TYPE_I"]},
    _root,
    {"HFC_TYPE_I": _subscript_dict["HFC_TYPE_I"]},
    "_ext_constant_inital_hfc_con",
)


@component.add(
    name="INITIAL_CH4_CONC",
    units="ppb",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_ch4_conc"},
)
def initial_ch4_conc():
    """
    Historical data. NASA. GISS. https://data.giss.nasa.gov/modelforce/ghgases/
    """
    return _ext_constant_initial_ch4_conc()


_ext_constant_initial_ch4_conc = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "Initial_CH4_conc",
    {},
    _root,
    {},
    "_ext_constant_initial_ch4_conc",
)


@component.add(
    name="INITIAL_N2O_CONC",
    units="ppb",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_n2o_conc"},
)
def initial_n2o_conc():
    """
    Historical data. NASA. GISS. https://data.giss.nasa.gov/modelforce/ghgases/
    """
    return _ext_constant_initial_n2o_conc()


_ext_constant_initial_n2o_conc = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "Initial_N2O_conc",
    {},
    _root,
    {},
    "_ext_constant_initial_n2o_conc",
)


@component.add(
    name="INITIAL_SEA_LEVEL_RISE_IN_2005",
    units="mm",
    limits=(-400.0, 400.0),
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_sea_level_rise_in_2005"},
)
def initial_sea_level_rise_in_2005():
    """
    Estimated SLR in 1995.
    """
    return _ext_constant_initial_sea_level_rise_in_2005()


_ext_constant_initial_sea_level_rise_in_2005 = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "initial_sea_level_rise_in_2005",
    {},
    _root,
    {},
    "_ext_constant_initial_sea_level_rise_in_2005",
)


@component.add(
    name="INITIAL_SF6_CON",
    units="ppt",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_sf6_con"},
)
def initial_sf6_con():
    """
    Historical data. NASA. GISS. https://data.giss.nasa.gov/modelforce/ghgases/
    """
    return _ext_constant_initial_sf6_con()


_ext_constant_initial_sf6_con = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "Initial_SF6_con",
    {},
    _root,
    {},
    "_ext_constant_initial_sf6_con",
)


@component.add(
    name="LAND_AREA_FRACTION",
    units="fraction",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_land_area_fraction"},
)
def land_area_fraction():
    """
    Fraction of global surface area that is land.
    """
    return _ext_constant_land_area_fraction()


_ext_constant_land_area_fraction = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "land_area_fraction",
    {},
    _root,
    {},
    "_ext_constant_land_area_fraction",
)


@component.add(
    name="LAND_THICKNESS",
    units="m",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_land_thickness"},
)
def land_thickness():
    """
    Effective land area heat capacity, expressed as equivalent water layer thickness.
    """
    return _ext_constant_land_thickness()


_ext_constant_land_thickness = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "land_thickness",
    {},
    _root,
    {},
    "_ext_constant_land_thickness",
)


@component.add(
    name="LAST_HISTORICAL_RF_YEAR",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_last_historical_rf_year"},
)
def last_historical_rf_year():
    """
    2010
    """
    return _ext_constant_last_historical_rf_year()


_ext_constant_last_historical_rf_year = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "Last_historical_RF_year",
    {},
    _root,
    {},
    "_ext_constant_last_historical_rf_year",
)


@component.add(
    name="LAYER_DEPTH",
    units="m",
    subscripts=["LAYERS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_layer_depth"},
)
def layer_depth():
    """
    Deep ocean layer thicknesses.
    """
    return _ext_constant_layer_depth()


_ext_constant_layer_depth = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "Layer_Depth_Layers*",
    {"LAYERS_I": _subscript_dict["LAYERS_I"]},
    _root,
    {"LAYERS_I": _subscript_dict["LAYERS_I"]},
    "_ext_constant_layer_depth",
)


@component.add(
    name="MINERAL_AEROSOLS_AND_LAND_RF",
    units="w/(m*m)",
    limits=(-1.0, 1.0),
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_mineral_aerosols_and_land_rf"},
)
def mineral_aerosols_and_land_rf():
    """
    Qaermn (minerals), Qland. Updated to reflect AR5. (-0.3)
    """
    return _ext_constant_mineral_aerosols_and_land_rf()


_ext_constant_mineral_aerosols_and_land_rf = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "Mineral_aerosols_and_land_RF",
    {},
    _root,
    {},
    "_ext_constant_mineral_aerosols_and_land_rf",
)


@component.add(
    name="MIXED_DEPTH",
    units="m",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_mixed_depth"},
)
def mixed_depth():
    """
    Mixed ocean layer depth.
    """
    return _ext_constant_mixed_depth()


_ext_constant_mixed_depth = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "Mixed_Depth",
    {},
    _root,
    {},
    "_ext_constant_mixed_depth",
)


@component.add(
    name="MIXING_TIME",
    units="Year",
    limits=(0.25, 10.0),
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_mixing_time"},
)
def mixing_time():
    """
    Atmosphere - mixed ocean layer mixing time.
    """
    return _ext_constant_mixing_time()


_ext_constant_mixing_time = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "Mixing_Time",
    {},
    _root,
    {},
    "_ext_constant_mixing_time",
)


@component.add(
    name="MP_RF_TOTAL",
    units="w/(m*m)",
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_mp_rf_total",
        "__data__": "_ext_data_mp_rf_total",
        "time": 1,
    },
)
def mp_rf_total():
    """
    Radiative forcing due to Montreal Protocol gases, based on the concentration of each gas multiplied by its radiative forcing coefficient. CROADS. JS Daniel, GJM Velders et al. (2007) Scientific Assessment of Ozone Depletion: 2006. Chapter 8. Halocarbon Scenarios, Ozone Depletion Potentials, and Global Warming Potentials. Table 8-5. Mixing ratios (ppt) of the ODSs considered in scenario A1.
    """
    return _ext_data_mp_rf_total(time())


_ext_data_mp_rf_total = ExtData(
    "model_parameters/climate/climate.xlsx",
    "World",
    "time_MP_RF_Total",
    "MP_RF_Total",
    "interpolate",
    {},
    _root,
    {},
    "_ext_data_mp_rf_total",
)


@component.add(
    name="N2O_N_MOLAR_MASS",
    units="g/mol",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_n2o_n_molar_mass"},
)
def n2o_n_molar_mass():
    """
    Molar mass of N2O.
    """
    return _ext_constant_n2o_n_molar_mass()


_ext_constant_n2o_n_molar_mass = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "N2O_N_molar_mass",
    {},
    _root,
    {},
    "_ext_constant_n2o_n_molar_mass",
)


@component.add(
    name="N2O_RADIATIVE_EFFICIENCY_COEFFICIENT",
    units="w/(m*m)",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_n2o_radiative_efficiency_coefficient"},
)
def n2o_radiative_efficiency_coefficient():
    """
    AR5 WG1 Chapter 8 Anthropogenic and Natural Radiative Forcing. Table 8.SM.1 Supplementary for Table 8.3: RF formulae for CO2, CH4 and N2O.
    """
    return _ext_constant_n2o_radiative_efficiency_coefficient()


_ext_constant_n2o_radiative_efficiency_coefficient = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "N2O_radiative_efficiency_coefficient",
    {},
    _root,
    {},
    "_ext_constant_n2o_radiative_efficiency_coefficient",
)


@component.add(
    name="N2O_REFERENCE_CONC",
    units="ppb",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_n2o_reference_conc"},
)
def n2o_reference_conc():
    """
    WG1AR5_Chapter08_FINAL.pdf. https://www.ipcc.ch/pdf/assessment-report/ar5/wg1/WG1AR5_Chapter08_FINAL.pd f
    """
    return _ext_constant_n2o_reference_conc()


_ext_constant_n2o_reference_conc = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "N2O_reference_conc",
    {},
    _root,
    {},
    "_ext_constant_n2o_reference_conc",
)


@component.add(
    name="N2O_TOTAL_ANTHRO_REST_OF_EMISSIONS_RCP",
    units="Mt/Year",
    subscripts=["REGIONS_9_I", "RCP_Scenario"],
    comp_type="Data",
    comp_subtype="Normal",
    depends_on={"global_n2o_anthro_emissions_rcp": 4, "number_of_regions": 4},
)
def n2o_total_anthro_rest_of_emissions_rcp():
    """
    Historic data + projections "Representative Concentration Pathways" (RCPs, see http://tntcat.iiasa.ac.at:8787/RcpDb/dsd?Action=htmlpage&page=compare)data, TODO:except "agriculture: fertilizers, animals, soil".
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "RCP_Scenario": _subscript_dict["RCP_Scenario"],
        },
        ["REGIONS_9_I", "RCP_Scenario"],
    )
    value.loc[:, ["RCP26"]] = (
        float(global_n2o_anthro_emissions_rcp().loc["RCP26"]) / number_of_regions()
    )
    value.loc[:, ["RCP45"]] = (
        float(global_n2o_anthro_emissions_rcp().loc["RCP45"]) / number_of_regions()
    )
    value.loc[:, ["RCP60"]] = (
        float(global_n2o_anthro_emissions_rcp().loc["RCP60"]) / number_of_regions()
    )
    value.loc[:, ["RCP85"]] = (
        float(global_n2o_anthro_emissions_rcp().loc["RCP85"]) / number_of_regions()
    )
    return value


@component.add(
    name="NATURAL_N2O_EMISSIONS",
    units="Mt/Year",
    limits=(0.0, 20.0),
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_natural_n2o_emissions"},
)
def natural_n2o_emissions():
    """
    AR5 WG1 Chapter 6 Table 6.9
    """
    return _ext_constant_natural_n2o_emissions()


_ext_constant_natural_n2o_emissions = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "Natural_N2O_emissions",
    {},
    _root,
    {},
    "_ext_constant_natural_n2o_emissions",
)


@component.add(
    name='"1975_1995_temp_change_lt"',
    units="DegreesC",
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_nvs_1975_1995_temp_change_lt",
        "__lookup__": "_ext_lookup_nvs_1975_1995_temp_change_lt",
    },
)
def nvs_1975_1995_temp_change_lt(x, final_subs=None):
    """
    Historic Temperature change from GISS NASA from year 1975 to 1995.
    """
    return _ext_lookup_nvs_1975_1995_temp_change_lt(x, final_subs)


_ext_lookup_nvs_1975_1995_temp_change_lt = ExtLookup(
    "model_parameters/climate/climate.xlsx",
    "World",
    "time_index_1975_1995_temp",
    "temp_1975_1995",
    {},
    _root,
    {},
    "_ext_lookup_nvs_1975_1995_temp_change_lt",
)


@component.add(
    name="OTHER_FORCINGS_HISTORY",
    units="w/(m*m)",
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_other_forcings_history",
        "__data__": "_ext_data_other_forcings_history",
        "time": 1,
    },
)
def other_forcings_history():
    """
    GISS other forcings 1850-2010.
    """
    return _ext_data_other_forcings_history(time())


_ext_data_other_forcings_history = ExtData(
    "model_parameters/climate/climate.xlsx",
    "World",
    "time_other_forcings_historic",
    "Other_forcings",
    "interpolate",
    {},
    _root,
    {},
    "_ext_data_other_forcings_history",
)


@component.add(
    name="OTHER_FORCINGS_RCP_SCENARIO",
    units="w/(m*m)",
    subscripts=["RCP_SCENARIO_I"],
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_other_forcings_rcp_scenario",
        "__data__": "_ext_data_other_forcings_rcp_scenario",
        "time": 1,
    },
)
def other_forcings_rcp_scenario():
    """
    RCPs starting in 2010.
    """
    return _ext_data_other_forcings_rcp_scenario(time())


_ext_data_other_forcings_rcp_scenario = ExtData(
    "model_parameters/climate/climate.xlsx",
    "World",
    "time_other_forcings_RCP",
    "other_forcings_RCP",
    None,
    {"RCP_SCENARIO_I": _subscript_dict["RCP_SCENARIO_I"]},
    _root,
    {"RCP_SCENARIO_I": _subscript_dict["RCP_SCENARIO_I"]},
    "_ext_data_other_forcings_rcp_scenario",
)


@component.add(
    name="PFC_RADIATIVE_EFFICIENCY",
    units="w/(ppb*m*m)",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_pfc_radiative_efficiency"},
)
def pfc_radiative_efficiency():
    """
    Radiative efficiency of CF4. From AR5 WG1 Chapter 8. Table 8.A.1. Lifetimes, Radiative Efficiencies and Metric Values
    """
    return _ext_constant_pfc_radiative_efficiency()


_ext_constant_pfc_radiative_efficiency = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "PFC_radiative_efficiency",
    {},
    _root,
    {},
    "_ext_constant_pfc_radiative_efficiency",
)


@component.add(
    name="PH_CONSTANT_1",
    units="pH",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_ph_constant_1"},
)
def ph_constant_1():
    """
    Bernie, D., J. Lowe, T. Tyrrell, and O. Legge (2010), Influence of mitigation policy on ocean acidification, Geophys. Res. Lett., 37, L15704, doi:10.1029/2010GL043181.
    """
    return _ext_constant_ph_constant_1()


_ext_constant_ph_constant_1 = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "pH_constant_1",
    {},
    _root,
    {},
    "_ext_constant_ph_constant_1",
)


@component.add(
    name="PH_CONSTANT_2",
    units="pH/ppm",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_ph_constant_2"},
)
def ph_constant_2():
    """
    Bernie, D., J. Lowe, T. Tyrrell, and O. Legge (2010), Influence of mitigation policy on ocean acidification, Geophys. Res. Lett., 37, L15704, doi:10.1029/2010GL043181.
    """
    return _ext_constant_ph_constant_2()


_ext_constant_ph_constant_2 = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "pH_constant_2",
    {},
    _root,
    {},
    "_ext_constant_ph_constant_2",
)


@component.add(
    name="PH_CONSTANT_3",
    units="pH/(ppm*ppm)",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_ph_constant_3"},
)
def ph_constant_3():
    """
    Bernie, D., J. Lowe, T. Tyrrell, and O. Legge (2010), Influence of mitigation policy on ocean acidification, Geophys. Res. Lett., 37, L15704, doi:10.1029/2010GL043181.
    """
    return _ext_constant_ph_constant_3()


_ext_constant_ph_constant_3 = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "pH_constant_3",
    {},
    _root,
    {},
    "_ext_constant_ph_constant_3",
)


@component.add(
    name="PH_CONSTANT_4",
    units="pH/(ppm*ppm*ppm)",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_ph_constant_4"},
)
def ph_constant_4():
    """
    Bernie, D., J. Lowe, T. Tyrrell, and O. Legge (2010), Influence of mitigation policy on ocean acidification, Geophys. Res. Lett., 37, L15704, doi:10.1029/2010GL043181.
    """
    return _ext_constant_ph_constant_4()


_ext_constant_ph_constant_4 = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "pH_constant_4",
    {},
    _root,
    {},
    "_ext_constant_ph_constant_4",
)


@component.add(
    name="PPM_TO_CALCULATE_OCEANIC_PH_THRESHOLD",
    units="ppm",
    comp_type="Constant",
    comp_subtype="Normal",
)
def ppm_to_calculate_oceanic_ph_threshold():
    """
    Parts per billion to calculate oceanic pH threshold
    """
    return 480


@component.add(
    name="PRE_INDUSTRIAL_PPM_CO2",
    units="ppm",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_pre_industrial_ppm_co2"},
)
def pre_industrial_ppm_co2():
    """
    Pre-industrial CO2 concentrations (275 ppm).
    """
    return _ext_constant_pre_industrial_ppm_co2()


_ext_constant_pre_industrial_ppm_co2 = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "pre_industrial_value_ppm",
    {},
    _root,
    {},
    "_ext_constant_pre_industrial_ppm_co2",
)


@component.add(
    name="PREIND_OCEAN_C_PER_METER",
    units="Gt/m",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_preind_ocean_c_per_meter"},
)
def preind_ocean_c_per_meter():
    """
    Corresponds with 767.8 GtC in a 75m layer.
    """
    return _ext_constant_preind_ocean_c_per_meter()


_ext_constant_preind_ocean_c_per_meter = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "Preind_Ocean_C_per_meter",
    {},
    _root,
    {},
    "_ext_constant_preind_ocean_c_per_meter",
)


@component.add(
    name="PREINDUSTRIAL_CH4",
    units="MtonsCH4",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_preindustrial_ch4"},
)
def preindustrial_ch4():
    """
    Law Dome ice core
    """
    return _ext_constant_preindustrial_ch4()


_ext_constant_preindustrial_ch4 = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "Preindustrial_CH4",
    {},
    _root,
    {},
    "_ext_constant_preindustrial_ch4",
)


@component.add(
    name="PREINDUSTRIAL_HFC_CONC",
    units="ppt",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_preindustrial_hfc_conc"},
)
def preindustrial_hfc_conc():
    """
    Preindustrial HFC in atmosphere concentration.
    """
    return _ext_constant_preindustrial_hfc_conc()


_ext_constant_preindustrial_hfc_conc = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "Preindustrial_HFC_conc",
    {},
    _root,
    {},
    "_ext_constant_preindustrial_hfc_conc",
)


@component.add(
    name="PREINDUSTRIAL_PFC_CONC",
    units="ppt",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_preindustrial_pfc_conc"},
)
def preindustrial_pfc_conc():
    """
    Preindustrial PFC in atmosphere concentration.
    """
    return _ext_constant_preindustrial_pfc_conc()


_ext_constant_preindustrial_pfc_conc = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "Preindustrial_PFC_conc",
    {},
    _root,
    {},
    "_ext_constant_preindustrial_pfc_conc",
)


@component.add(
    name="PREINDUSTRIAL_SF6_CONC",
    units="ppt",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_preindustrial_sf6_conc"},
)
def preindustrial_sf6_conc():
    """
    Preindustrial SF6 in atmosphere concentration.
    """
    return _ext_constant_preindustrial_sf6_conc()


_ext_constant_preindustrial_sf6_conc = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "Preindustrial_SF6_conc",
    {},
    _root,
    {},
    "_ext_constant_preindustrial_sf6_conc",
)


@component.add(
    name="PROB_AMAZ_TP_2010_2200_C1",
    units="1/Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_prob_amaz_tp_2010_2200_c1"},
)
def prob_amaz_tp_2010_2200_c1():
    """
    AMAZ probability 2010-2200. Source: Kriegler, E., Hall, J.W., Held, H., Dawson, R., Schellnhuber, H.J., 2009. Imprecise probability assessment of tipping points in the climate system. PNAS 106, 5041–5046. https://doi.org/10.1073/pnas.0809117106
    """
    return _ext_constant_prob_amaz_tp_2010_2200_c1()


_ext_constant_prob_amaz_tp_2010_2200_c1 = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "AMAZ",
    {},
    _root,
    {},
    "_ext_constant_prob_amaz_tp_2010_2200_c1",
)


@component.add(
    name="PROB_AMOC_WEAKENING_TP_2010_2100_C1",
    units="1/Year",
    comp_type="Constant",
    comp_subtype="Normal",
)
def prob_amoc_weakening_tp_2010_2100_c1():
    """
    AMOC partial collapse probability until 2100. Source: Castellana, D., Baars, S., Wubs, F. W. and Dijkstra H. A., 2019. Transition Probabilities of Noise-induced Transitions of the Atlantic Ocean Circulation. Sci Rep 9, 20284 (2019). https://doi.org/10.1038/s41598-019-56435-6
    """
    return 0.15


@component.add(
    name="PROB_DAIS_TP_2010_2200_C1",
    units="1/Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_prob_dais_tp_2010_2200_c1"},
)
def prob_dais_tp_2010_2200_c1():
    """
    DAIS probability 2010-2200. Source: Kriegler, E., Hall, J.W., Held, H., Dawson, R., Schellnhuber, H.J., 2009. Imprecise probability assessment of tipping points in the climate system. PNAS 106, 5041–5046. https://doi.org/10.1073/pnas.0809117106
    """
    return _ext_constant_prob_dais_tp_2010_2200_c1()


_ext_constant_prob_dais_tp_2010_2200_c1 = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "DAIS",
    {},
    _root,
    {},
    "_ext_constant_prob_dais_tp_2010_2200_c1",
)


@component.add(
    name="PROB_MGIS_TP_2010_2200_C1",
    units="1/Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_prob_mgis_tp_2010_2200_c1"},
)
def prob_mgis_tp_2010_2200_c1():
    """
    MGIS probability 2010-2200. Source: Kriegler, E., Hall, J.W., Held, H., Dawson, R., Schellnhuber, H.J., 2009. Imprecise probability assessment of tipping points in the climate system. PNAS 106, 5041–5046. https://doi.org/10.1073/pnas.0809117106
    """
    return _ext_constant_prob_mgis_tp_2010_2200_c1()


_ext_constant_prob_mgis_tp_2010_2200_c1 = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "MGIS",
    {},
    _root,
    {},
    "_ext_constant_prob_mgis_tp_2010_2200_c1",
)


@component.add(
    name="PROB_NINO_TP_2010_2200_C1",
    units="1/Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_prob_nino_tp_2010_2200_c1"},
)
def prob_nino_tp_2010_2200_c1():
    """
    NIÑO probability 2010-2200. Source: Kriegler, E., Hall, J.W., Held, H., Dawson, R., Schellnhuber, H.J., 2009. Imprecise probability assessment of tipping points in the climate system. PNAS 106, 5041–5046. https://doi.org/10.1073/pnas.0809117106
    """
    return _ext_constant_prob_nino_tp_2010_2200_c1()


_ext_constant_prob_nino_tp_2010_2200_c1 = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "NIÑO",
    {},
    _root,
    {},
    "_ext_constant_prob_nino_tp_2010_2200_c1",
)


@component.add(
    name="REF_BUFFER_FACTOR",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_ref_buffer_factor"},
)
def ref_buffer_factor():
    """
    Normal buffer factor.
    """
    return _ext_constant_ref_buffer_factor()


_ext_constant_ref_buffer_factor = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "Ref_Buffer_Factor",
    {},
    _root,
    {},
    "_ext_constant_ref_buffer_factor",
)


@component.add(
    name="REFERENCE_CH4_TIME_CONSTANT",
    units="Year",
    limits=(8.0, 10.0),
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_reference_ch4_time_constant"},
)
def reference_ch4_time_constant():
    """
    Calculated from AR5 WG1 Chapter 6
    """
    return _ext_constant_reference_ch4_time_constant()


_ext_constant_reference_ch4_time_constant = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "Reference_CH4_time_constant",
    {},
    _root,
    {},
    "_ext_constant_reference_ch4_time_constant",
)


@component.add(
    name="REFERENCE_SENSITIVITY_OF_C_FROM_PERMAFROST_AND_CLATHRATE_TO_TEMPERATURE",
    units="Gt/(Year*DegreesC)",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_reference_sensitivity_of_c_from_permafrost_and_clathrate_to_temperature"
    },
)
def reference_sensitivity_of_c_from_permafrost_and_clathrate_to_temperature():
    """
    The reference emissions of carbon from melting permafrost and outgassing from clathrates per degree C of warming above the threshold.
    """
    return (
        _ext_constant_reference_sensitivity_of_c_from_permafrost_and_clathrate_to_temperature()
    )


_ext_constant_reference_sensitivity_of_c_from_permafrost_and_clathrate_to_temperature = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "Reference_Sensitivity_of_C_from_Permafrost_and_Clathrate_to_Temperature",
    {},
    _root,
    {},
    "_ext_constant_reference_sensitivity_of_c_from_permafrost_and_clathrate_to_temperature",
)


@component.add(
    name="REFERENCE_SENSITIVITY_OF_CH4_FROM_PERMAFROST_AND_CLATHRATE_TO_TEMPERATURE",
    units="Mt/(Year*DegreesC)",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_reference_sensitivity_of_ch4_from_permafrost_and_clathrate_to_temperature"
    },
)
def reference_sensitivity_of_ch4_from_permafrost_and_clathrate_to_temperature():
    """
    The reference emissions of methane from melting permafrost and outgassing from clathrates per degree C of warming above the threshold.
    """
    return (
        _ext_constant_reference_sensitivity_of_ch4_from_permafrost_and_clathrate_to_temperature()
    )


_ext_constant_reference_sensitivity_of_ch4_from_permafrost_and_clathrate_to_temperature = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "Reference_Sensitivity_of_CH4_from_Permafrost_and_Clathrate_to_Temperature",
    {},
    _root,
    {},
    "_ext_constant_reference_sensitivity_of_ch4_from_permafrost_and_clathrate_to_temperature",
)


@component.add(
    name="REFERENCE_TEMPERATURE",
    units="DegreesC",
    limits=(-2.0, 2.0),
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_reference_temperature"},
)
def reference_temperature():
    """
    From V&R (2009) supplement, table S1.
    """
    return _ext_constant_reference_temperature()


_ext_constant_reference_temperature = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "Reference_Temperature",
    {},
    _root,
    {},
    "_ext_constant_reference_temperature",
)


@component.add(
    name="REFERENCE_TEMPERATURE_CHANGE_FOR_EFFECT_OF_WARMING_ON_CH4_FROM_RESPIRATION",
    units="DegreesC",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_reference_temperature_change_for_effect_of_warming_on_ch4_from_respiration"
    },
)
def reference_temperature_change_for_effect_of_warming_on_ch4_from_respiration():
    """
    Temperature change at which the C as CH4 release from humus doubles for the Sensitivity of Methane Emissions to Temperature=1.
    """
    return (
        _ext_constant_reference_temperature_change_for_effect_of_warming_on_ch4_from_respiration()
    )


_ext_constant_reference_temperature_change_for_effect_of_warming_on_ch4_from_respiration = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "Reference_Temperature_Change_for_Effect_of_Warming_on_CH4_from_Respiration",
    {},
    _root,
    {},
    "_ext_constant_reference_temperature_change_for_effect_of_warming_on_ch4_from_respiration",
)


@component.add(
    name="RESIDENTIAL_TIME_OF_BIOMASS",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_residential_time_of_biomass"},
)
def residential_time_of_biomass():
    """
    Average residence time of carbon in biomass.
    """
    return _ext_constant_residential_time_of_biomass()


_ext_constant_residential_time_of_biomass = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "Biomass_Res_Time",
    {},
    _root,
    {},
    "_ext_constant_residential_time_of_biomass",
)


@component.add(
    name="SAMPLE_FOR_MONTE_CARLO_ECS",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="Normal",
)
def sample_for_monte_carlo_ecs():
    """
    By default the value "0.5", which corresponds to the median of the distribution (P50). This is the variable to use as probabilistic input to run Monte Carlo simulations.
    """
    return 0.5


@component.add(
    name="SEA_LEVEL_SENSITIVITY_FROM_ICE_SHEET_MELTING",
    units="DMNL",
    limits=(0.0, 1.0),
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_sea_level_sensitivity_from_ice_sheet_melting"
    },
)
def sea_level_sensitivity_from_ice_sheet_melting():
    """
    User specified parameter to capture change in rate of sea level rise above or below the value of 3.4 mm/year/degree C estimated by Rahmstorf from data 1880-2000. Positive values capture accelerated SLR from rates of ice sheet melt higher than those reflected in the data Rahmstorf used. Negative values would capture lower rates of melting. Does not affect the historic period; impact only from 2000 on. A value of 1 yields a doubling of the Rahmstorf rate constant.
    """
    return _ext_constant_sea_level_sensitivity_from_ice_sheet_melting()


_ext_constant_sea_level_sensitivity_from_ice_sheet_melting = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "Sea_Level_Sensitivity_from_Ice_Sheet_Melting",
    {},
    _root,
    {},
    "_ext_constant_sea_level_sensitivity_from_ice_sheet_melting",
)


@component.add(
    name="SELECT_GWP_TIME_FRAME_SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_select_gwp_time_frame_sp"},
)
def select_gwp_time_frame_sp():
    """
    Choose Global Warming Potential (GWP) time frame: 1: 20 years 2: 100 years Greenhouse gases (GHGs) warm the Earth by absorbing energy and slowing the rate at which the energy escapes to space; they act like a blanket insulating the Earth. Different GHGs can have different effects on the Earth's warming. Two key ways in which these gases differ from each other are their ability to absorb energy (their "radiative efficiency"), and how long they stay in the atmosphere (also known as their "lifetime"). The GWP was developed to allow comparisons of the global warming impacts of different gases. Specifically, it is a measure of how much energy the emissions of 1 ton of a gas will absorb over a given period of time, relative to the emissions of 1 ton of carbon dioxide (CO2). The larger the GWP, the more that a given gas warms the Earth compared to CO2 over that time period. The time period usually used for GWPs is 100 years, but it may be argued that a shorter time- frame could be used to assess the shorter-term effects of some gases such as CH4 which has a much higher short-term warming effect than CO2 (e.g., Howarth, R.W., Santoro, R., Ingraffea, A., 2011. Methane and the greenhouse-gas footprint of natural gas from shale formations. Climatic Change 106, 679–690. https://doi.org/10.1007/s10584-011-0061-5).
    """
    return _ext_constant_select_gwp_time_frame_sp()


_ext_constant_select_gwp_time_frame_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "climate",
    "GWP_time_frame",
    {},
    _root,
    {},
    "_ext_constant_select_gwp_time_frame_sp",
)


@component.add(
    name="SELECT_RCP_FOR_EXOGENOUS_GHG_EMISSIONS_SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_select_rcp_for_exogenous_ghg_emissions_sp"
    },
)
def select_rcp_for_exogenous_ghg_emissions_sp():
    """
    Choose RCP (Representative Concentration Pathway) from IPCC: 1. RCP 2.6 2. RCP 4.5 3. RCP 6.0 4. RCP 8.5 Each RCP represents a level of radiative forcing (W/m2) by 2100. Four pathways were used for climate modeling and research for the IPCC fifth Assessment Report (AR5) in 2014. The pathways describe different climate futures, all of which are considered possible depending on the volume of greenhouse gases (GHG) emitted in the years to come. This hypothesis is used in WILIAM to drive the evolution of some dimensions which have not been fully endogenized (e.g., some GHG, water availability, etc.).
    """
    return _ext_constant_select_rcp_for_exogenous_ghg_emissions_sp()


_ext_constant_select_rcp_for_exogenous_ghg_emissions_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "climate",
    "Exogenous_other_GHG_emissions_selection_of_RCP",
    {},
    _root,
    {},
    "_ext_constant_select_rcp_for_exogenous_ghg_emissions_sp",
)


@component.add(
    name="SELECTION_ECS_INPUT_METHOD",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_selection_ecs_input_method"},
)
def selection_ecs_input_method():
    """
    Parameter to select different input method for the Equilibrium Climate Sensitivity: 0: exogenous from inputs.xlsx (for each scenario) 1: ECDF from AR5 Rogelj et al 2014
    """
    return _ext_constant_selection_ecs_input_method()


_ext_constant_selection_ecs_input_method = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "selection_ECS_input_method",
    {},
    _root,
    {},
    "_ext_constant_selection_ecs_input_method",
)


@component.add(
    name="SENSITIVITY_OF_C_UPTAKE_TO_TEMPERATURE",
    units="DMNL",
    limits=(0.0, 2.5),
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_sensitivity_of_c_uptake_to_temperature"},
)
def sensitivity_of_c_uptake_to_temperature():
    """
    Strength of the feedback effect of temperature on uptake of C by land and oceans. W means no temperature-carbon uptake feedback and default of 1 yields the average value found in Friedlingstein et al., 2006. Climate-Carbon Cycle Feedback Analysis: ResuMCS from the C4MIP Model Intercomparison. Journal of Climate. p3337-3353.
    """
    return _ext_constant_sensitivity_of_c_uptake_to_temperature()


_ext_constant_sensitivity_of_c_uptake_to_temperature = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "Sensitivity_of_C_Uptake_to_Temperature",
    {},
    _root,
    {},
    "_ext_constant_sensitivity_of_c_uptake_to_temperature",
)


@component.add(
    name="SENSITIVITY_OF_METHANE_EMISSIONS_TO_PERMAFROST_AND_CLATHRATE",
    units="DMNL",
    limits=(0.0, 1.0),
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_sensitivity_of_methane_emissions_to_permafrost_and_clathrate"
    },
)
def sensitivity_of_methane_emissions_to_permafrost_and_clathrate():
    """
    0 = no feedback 1 = base feedback
    """
    return _ext_constant_sensitivity_of_methane_emissions_to_permafrost_and_clathrate()


_ext_constant_sensitivity_of_methane_emissions_to_permafrost_and_clathrate = (
    ExtConstant(
        "model_parameters/climate/climate.xlsx",
        "World",
        "Sensitivity_of_Methane_Emissions_to_Temperature",
        {},
        _root,
        {},
        "_ext_constant_sensitivity_of_methane_emissions_to_permafrost_and_clathrate",
    )
)


@component.add(
    name="SENSITIVITY_OF_METHANE_EMISSIONS_TO_TEMPERATURE",
    units="DMNL",
    limits=(0.0, 2.5),
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_sensitivity_of_methane_emissions_to_temperature"
    },
)
def sensitivity_of_methane_emissions_to_temperature():
    """
    Allows users to control the strength of the feedback effect of temperature on release of C as CH4 from humus. Default of W means no temperature feedback and 1 is mean feedback.
    """
    return _ext_constant_sensitivity_of_methane_emissions_to_temperature()


_ext_constant_sensitivity_of_methane_emissions_to_temperature = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "Sensitivity_of_Methane_Emissions_to_Temperature",
    {},
    _root,
    {},
    "_ext_constant_sensitivity_of_methane_emissions_to_temperature",
)


@component.add(
    name="SENSITIVITY_OF_PCO2_DIC_TO_TEMPERATURE_MEAN",
    units="1/DegreesC",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_sensitivity_of_pco2_dic_to_temperature_mean"
    },
)
def sensitivity_of_pco2_dic_to_temperature_mean():
    """
    Sensitivity of equilibrium concentration of dissolved inorganic carbon to temperature. Calibrated to be consistent with Friedlingstein et al., 2006. Climate-Carbon Cycle Feedback Analysis: ResuMCS from the C4MIP Model Intercomparison. Journal of Climate. p3337-3353. Default Sensitivity of C Uptake to Temperature of 1 corresponds to mean value from the 11 models tested.
    """
    return _ext_constant_sensitivity_of_pco2_dic_to_temperature_mean()


_ext_constant_sensitivity_of_pco2_dic_to_temperature_mean = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "Sensitivity_of_pCO2_DIC_to_Temperature_Mean",
    {},
    _root,
    {},
    "_ext_constant_sensitivity_of_pco2_dic_to_temperature_mean",
)


@component.add(
    name="SENSITIVITY_OF_SEA_LEVEL_RISE_TO_TEMPERATURE",
    units="mm/(Year*DegreesC)",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_sensitivity_of_sea_level_rise_to_temperature"
    },
)
def sensitivity_of_sea_level_rise_to_temperature():
    """
    Sensitivity of sea level rise to temperature anomaly. From V&R (2009) supplement, table S1. Rahmstorf (2007) uses 3.4
    """
    return _ext_constant_sensitivity_of_sea_level_rise_to_temperature()


_ext_constant_sensitivity_of_sea_level_rise_to_temperature = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "Sensitivity_of_Sea_Level_Rise_to_Temperature",
    {},
    _root,
    {},
    "_ext_constant_sensitivity_of_sea_level_rise_to_temperature",
)


@component.add(
    name="SENSITIVITY_OF_SLR_RATE_TO_TEMP_RATE",
    units="mm/DegreesC",
    limits=(-100.0, 100.0),
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_sensitivity_of_slr_rate_to_temp_rate"},
)
def sensitivity_of_slr_rate_to_temp_rate():
    """
    Slope of instantaneous temperature change - sea level change relationship (Vermeer & Rahmstorf, 2009) From V&R (2009) supplement, table S1. Rahmstorf (2007) uses W (i.e. term is missing)
    """
    return _ext_constant_sensitivity_of_slr_rate_to_temp_rate()


_ext_constant_sensitivity_of_slr_rate_to_temp_rate = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "Sensitivity_of_SLR_rate_to_temp_rate",
    {},
    _root,
    {},
    "_ext_constant_sensitivity_of_slr_rate_to_temp_rate",
)


@component.add(
    name="SF6_MOLAR_MASS",
    units="g/mol",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_sf6_molar_mass"},
)
def sf6_molar_mass():
    """
    Molar mass of SF6.
    """
    return _ext_constant_sf6_molar_mass()


_ext_constant_sf6_molar_mass = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "SF6_molar_mass",
    {},
    _root,
    {},
    "_ext_constant_sf6_molar_mass",
)


@component.add(
    name="SF6_RADIATIVE_EFFICIENCY",
    units="w/(ppb*m*m)",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_sf6_radiative_efficiency"},
)
def sf6_radiative_efficiency():
    """
    From AR5 WG1 Chapter 8. Table 8.A.1. Lifetimes, Radiative Efficiencies and Metric Values
    """
    return _ext_constant_sf6_radiative_efficiency()


_ext_constant_sf6_radiative_efficiency = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "SF6_radiative_efficiency",
    {},
    _root,
    {},
    "_ext_constant_sf6_radiative_efficiency",
)


@component.add(
    name="SLR_ICE_SHEET_MELTING_YEAR",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_slr_ice_sheet_melting_year"},
)
def slr_ice_sheet_melting_year():
    """
    Sea Level Rise sheet melting year
    """
    return _ext_constant_slr_ice_sheet_melting_year()


_ext_constant_slr_ice_sheet_melting_year = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "SLR_ice_sheet_melting_year",
    {},
    _root,
    {},
    "_ext_constant_slr_ice_sheet_melting_year",
)


@component.add(
    name="STRATOSPHERIC_CH4_PATH_SHARE",
    units="DMNL",
    limits=(0.0, 1.0),
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_stratospheric_ch4_path_share"},
)
def stratospheric_ch4_path_share():
    """
    Calculated from AR5 WG1 Chapter 6
    """
    return _ext_constant_stratospheric_ch4_path_share()


_ext_constant_stratospheric_ch4_path_share = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "Stratospheric_CH4_path_share",
    {},
    _root,
    {},
    "_ext_constant_stratospheric_ch4_path_share",
)


@component.add(
    name="STRENGTH_OF_TEMP_EFFECT_ON_LAND_C_FLUX_MEAN",
    units="1/DegreesC",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_strength_of_temp_effect_on_land_c_flux_mean"
    },
)
def strength_of_temp_effect_on_land_c_flux_mean():
    """
    Average effect of temperature on flux of carbon to land. Calibrated to be consistent with Friedlingstein et al., 2006. Climate-Carbon Cycle Feedback Analysis: ResuMCS from the C4MIP Model Intercomparison. Journal of Climate. p3337-3353. Default Sensitivity of C Uptake to Temperature of 1 corresponds to mean value from the 11 models tested.
    """
    return _ext_constant_strength_of_temp_effect_on_land_c_flux_mean()


_ext_constant_strength_of_temp_effect_on_land_c_flux_mean = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "Strength_of_temp_effect_on_land_C_flux_mean",
    {},
    _root,
    {},
    "_ext_constant_strength_of_temp_effect_on_land_c_flux_mean",
)


@component.add(
    name="TEMP_ADJUSTMENT_FOR_SLR",
    units="DegreesC",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_temp_adjustment_for_slr"},
)
def temp_adjustment_for_slr():
    """
    Adjustment to global surface temperature that is relative to pre-industrial levels from the average of the 1951-1980 data that Vermeer and Rahmstorf (2009) used based on GISTEMP. See V&R 2009 supplement.
    """
    return _ext_constant_temp_adjustment_for_slr()


_ext_constant_temp_adjustment_for_slr = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "Temp_adjustment_for_SLR",
    {},
    _root,
    {},
    "_ext_constant_temp_adjustment_for_slr",
)


@component.add(
    name="TEMPERATURE_CHANGE_IN_1995",
    units="DegreesC",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_temperature_change_in_1995"},
)
def temperature_change_in_1995():
    """
    Temperature change in 1995 (GISS NASA).
    """
    return _ext_constant_temperature_change_in_1995()


_ext_constant_temperature_change_in_1995 = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "temp_1995",
    {},
    _root,
    {},
    "_ext_constant_temperature_change_in_1995",
)


@component.add(
    name="TEMPERATURE_THRESHOLD_FOR_METHANE_EMISSIONS_FROM_PERMAFROST_AND_CLATHRATE",
    units="DegreesC",
    limits=(0.0, 4.0),
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_temperature_threshold_for_methane_emissions_from_permafrost_and_clathrate"
    },
)
def temperature_threshold_for_methane_emissions_from_permafrost_and_clathrate():
    """
    The threshold rise in global mean surface temperature above preindustrial levels that triggers the release of methane from permafrost and clathrates. Below this threshold, emissions from these sources are assumed to be zero. Above the threshold, emissions are assumed to rise linearly with temperature.
    """
    return (
        _ext_constant_temperature_threshold_for_methane_emissions_from_permafrost_and_clathrate()
    )


_ext_constant_temperature_threshold_for_methane_emissions_from_permafrost_and_clathrate = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "Temperature_Threshold_for_Methane_Emissions_from_Permafrost_and_Clathrate",
    {},
    _root,
    {},
    "_ext_constant_temperature_threshold_for_methane_emissions_from_permafrost_and_clathrate",
)


@component.add(
    name="TIME_CONST_FOR_HFC",
    units="Years",
    subscripts=["HFC_TYPE_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_time_const_for_hfc"},
)
def time_const_for_hfc():
    """
    From AR5 WG1 Chapter 8. Table 8.A.1. Lifetimes, Radiative Efficiencies and Metric Values
    """
    return _ext_constant_time_const_for_hfc()


_ext_constant_time_const_for_hfc = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "Time_Const_for_HFC*",
    {"HFC_TYPE_I": _subscript_dict["HFC_TYPE_I"]},
    _root,
    {"HFC_TYPE_I": _subscript_dict["HFC_TYPE_I"]},
    "_ext_constant_time_const_for_hfc",
)


@component.add(
    name="TIME_CONST_FOR_N2O",
    units="Years",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_time_const_for_n2o"},
)
def time_const_for_n2o():
    """
    Value of CH4 and N2O time constants reported in AR5 WG1 Chapter 8 Table 8.A.1 noted to be for calculation of GWP, not for cycle. Value of 117 years determined through optimization.
    """
    return _ext_constant_time_const_for_n2o()


_ext_constant_time_const_for_n2o = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "Time_Const_for_N2O",
    {},
    _root,
    {},
    "_ext_constant_time_const_for_n2o",
)


@component.add(
    name="TIME_CONST_FOR_PFC",
    units="Years",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_time_const_for_pfc"},
)
def time_const_for_pfc():
    """
    based on CF4 From AR5 WG1 Chapter 8. Table 8.A.1. Lifetimes, Radiative Efficiencies and Metric Values
    """
    return _ext_constant_time_const_for_pfc()


_ext_constant_time_const_for_pfc = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "Time_Const_for_PFC",
    {},
    _root,
    {},
    "_ext_constant_time_const_for_pfc",
)


@component.add(
    name="TIME_CONST_FOR_SF6",
    units="Years",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_time_const_for_sf6"},
)
def time_const_for_sf6():
    """
    From AR5 WG1 Chapter 8. Table 8.A.1. Lifetimes, Radiative Efficiencies and Metric Values
    """
    return _ext_constant_time_const_for_sf6()


_ext_constant_time_const_for_sf6 = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "Time_Const_for_SF6",
    {},
    _root,
    {},
    "_ext_constant_time_const_for_sf6",
)


@component.add(
    name="TIME_TO_COMMIT_RF",
    units="Year",
    limits=(1900.0, 2200.0),
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_time_to_commit_rf"},
)
def time_to_commit_rf():
    """
    Time after which forcing is frozen for a test of committed warming.
    """
    return _ext_constant_time_to_commit_rf()


_ext_constant_time_to_commit_rf = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "Time_to_Commit_RF",
    {},
    _root,
    {},
    "_ext_constant_time_to_commit_rf",
)


@component.add(
    name="TOTAL_GHG_EMISSIONS_INCLUDING_LAND_USE_CHANGE_AND_FORESTRY",
    units="GtonsCO2e/Year",
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_total_ghg_emissions_including_land_use_change_and_forestry",
        "__data__": "_ext_data_total_ghg_emissions_including_land_use_change_and_forestry",
        "time": 1,
    },
)
def total_ghg_emissions_including_land_use_change_and_forestry():
    """
    Total GHG Emissions Including Land-Use Change and Forestry (CDIAC).
    """
    return _ext_data_total_ghg_emissions_including_land_use_change_and_forestry(time())


_ext_data_total_ghg_emissions_including_land_use_change_and_forestry = ExtData(
    "model_parameters/energy/energy.xlsm",
    "World",
    "time_index",
    "Total_GHG_Emissions_Including_Land_Use_Change_and_Forestry",
    "interpolate",
    {},
    _root,
    {},
    "_ext_data_total_ghg_emissions_including_land_use_change_and_forestry",
)


@component.add(
    name="TROPOSPHERIC_CH4_PATH_SHARE",
    units="DMNL",
    limits=(0.0, 1.0),
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_tropospheric_ch4_path_share"},
)
def tropospheric_ch4_path_share():
    """
    Calculated from AR5 WG1 Chapter 6
    """
    return _ext_constant_tropospheric_ch4_path_share()


_ext_constant_tropospheric_ch4_path_share = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "Tropospheric_CH4_path_share",
    {},
    _root,
    {},
    "_ext_constant_tropospheric_ch4_path_share",
)
