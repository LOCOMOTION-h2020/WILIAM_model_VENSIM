"""
Module land_and_water.exogenous_inputs
Translated using PySD version 3.10.0
"""


@component.add(
    name="AGROFOOD_TRANSFORM_MATRIX",
    units="DMNL",
    subscripts=["FOODS_I", "LAND_PRODUCTS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_agrofood_transform_matrix"},
)
def agrofood_transform_matrix():
    """
    Agrofood matrix to convert diet patterns to land products
    """
    return _ext_constant_agrofood_transform_matrix()


_ext_constant_agrofood_transform_matrix = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Diet",
    "AGROFOOD_TRANSFORM_MATRIX",
    {
        "FOODS_I": _subscript_dict["FOODS_I"],
        "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
    },
    _root,
    {
        "FOODS_I": _subscript_dict["FOODS_I"],
        "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
    },
    "_ext_constant_agrofood_transform_matrix",
)


@component.add(
    name="ANNUAL_GROWTH_RATE_OF_FOREST_STOCKS_COEFFICIENT_0",
    units="DMNL/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_annual_growth_rate_of_forest_stocks_coefficient_0"
    },
)
def annual_growth_rate_of_forest_stocks_coefficient_0():
    """
    annual growth rate of forest stocks coefficient 0 GET_DIRECT_CONSTANTS('model_parameters/land_and_water/land_and_water.xlsx', 'forest' , 'ANNUAL_GROWTH_RATE_OF_FOREST_STOCKS_COEFFICIENT_0*' )
    """
    return _ext_constant_annual_growth_rate_of_forest_stocks_coefficient_0()


_ext_constant_annual_growth_rate_of_forest_stocks_coefficient_0 = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "forest",
    "ANNUAL_GROWTH_RATE_OF_FOREST_STOCKS_COEFFICIENT_0*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_annual_growth_rate_of_forest_stocks_coefficient_0",
)


@component.add(
    name="ANNUAL_GROWTH_RATE_OF_FOREST_STOCKS_COEFFICIENT_1",
    units="DMNL/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_annual_growth_rate_of_forest_stocks_coefficient_1"
    },
)
def annual_growth_rate_of_forest_stocks_coefficient_1():
    """
    annual growth rate of forest stocks coefficient 1 GET_DIRECT_CONSTANTS('model_parameters/land_and_water/land_and_water.xlsx', 'forest' , 'ANNUAL_GROWTH_RATE_OF_FOREST_STOCKS_COEFFICIENT_1*' )
    """
    return _ext_constant_annual_growth_rate_of_forest_stocks_coefficient_1()


_ext_constant_annual_growth_rate_of_forest_stocks_coefficient_1 = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "forest",
    "ANNUAL_GROWTH_RATE_OF_FOREST_STOCKS_COEFFICIENT_1*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_annual_growth_rate_of_forest_stocks_coefficient_1",
)


@component.add(
    name="ANNUAL_GROWTH_RATE_OF_FOREST_STOCKS_COEFFICIENT_2",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def annual_growth_rate_of_forest_stocks_coefficient_2():
    """
    annual growth rate of forest stocks coefficient 2 GET_DIRECT_CONSTANTS('model_parameters/land_and_water/land_and_water.xlsx', 'forest' , 'ANNUAL_GROWTH_RATE_OF_FOREST_STOCKS_COEFFICIENT_2*' )
    """
    return xr.DataArray(
        -0.38252, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
    )


@component.add(
    name="BASELINE_DIET_PATTERN_OF_POLICY_DIETS_SP",
    units="kg/(Year*people)",
    subscripts=["REGIONS_9_I", "FOODS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_baseline_diet_pattern_of_policy_diets_sp"
    },
)
def baseline_diet_pattern_of_policy_diets_sp():
    """
    Baseline policy diet
    """
    return _ext_constant_baseline_diet_pattern_of_policy_diets_sp()


_ext_constant_baseline_diet_pattern_of_policy_diets_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "BASELINE_DIET_PATTERN_OF_POLICY_DIETS_SP",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "FOODS_I": _subscript_dict["FOODS_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "FOODS_I": _subscript_dict["FOODS_I"],
    },
    "_ext_constant_baseline_diet_pattern_of_policy_diets_sp",
)


@component.add(
    name="CARBON_FRACTION_OF_DRY_MATTER_FOREST",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_carbon_fraction_of_dry_matter_forest"},
)
def carbon_fraction_of_dry_matter_forest():
    """
    carbon fraction of dry matter forest
    """
    return _ext_constant_carbon_fraction_of_dry_matter_forest()


_ext_constant_carbon_fraction_of_dry_matter_forest = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "forest",
    "CARBON_FRACTION_OF_DRY_MATTER_FOREST*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_carbon_fraction_of_dry_matter_forest",
)


@component.add(
    name="CHECK_EXOGENOUS_LAND_USE_DEMANDS",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LANDS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_check_exogenous_land_use_demands"},
)
def check_exogenous_land_use_demands():
    return _ext_constant_check_exogenous_land_use_demands()


_ext_constant_check_exogenous_land_use_demands = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "EXOGENOUS_LAND_USE_DEMANDS",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": _subscript_dict["LANDS_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": _subscript_dict["LANDS_I"],
    },
    "_ext_constant_check_exogenous_land_use_demands",
)


@component.add(
    name="CHEMICAL_FERTILIZERS_PER_CROPLAND_AREA",
    units="t/km2",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_chemical_fertilizers_per_cropland_area"},
)
def chemical_fertilizers_per_cropland_area():
    return _ext_constant_chemical_fertilizers_per_cropland_area()


_ext_constant_chemical_fertilizers_per_cropland_area = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "CHEMICAL_FERTILIZERS_PER_CROPLAND_AREA",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_chemical_fertilizers_per_cropland_area",
)


@component.add(
    name="CONTROL_PARAMETER_OF_LAND_USE_CHANGES",
    units="DMNL",
    subscripts=["LANDS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_control_parameter_of_land_use_changes"},
)
def control_parameter_of_land_use_changes():
    """
    Constant of the proprotional control of the feedback loop of land changes drive by shortage. It is multiplied by the initial value of land uses in order to be proportional to the land area of each region and to the PRIORITIES OF LAND USE CHANGE to speed up those uses with highest priority.
    """
    return _ext_constant_control_parameter_of_land_use_changes()


_ext_constant_control_parameter_of_land_use_changes = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "CONTROL_PARAMETER_OF_LAND_USE_CHANGES",
    {"LANDS_I": _subscript_dict["LANDS_I"]},
    _root,
    {"LANDS_I": _subscript_dict["LANDS_I"]},
    "_ext_constant_control_parameter_of_land_use_changes",
)


@component.add(
    name="DELAY_TIME_LANDUSE_TO_LANDUSE2_SOIL",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_delay_time_landuse_to_landuse2_soil"},
)
def delay_time_landuse_to_landuse2_soil():
    """
    Time period to reach equilibrium of the soil carbon stock when grassland is changed to cropland. Source: IPPC Guidelines 2006 A value of 20 for the time period of equilibrimm corresponds to a delay time (for the delay function) of 5 years.If the value is of 0 the emissions are produced instantaenosly (inmediate)--> time period of equilibrium of 1 year
    """
    return _ext_constant_delay_time_landuse_to_landuse2_soil()


_ext_constant_delay_time_landuse_to_landuse2_soil = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "DELAY_TIME_LANDUSE_TO_LANDUSE2_SOIL",
    {},
    _root,
    {},
    "_ext_constant_delay_time_landuse_to_landuse2_soil",
)


@component.add(
    name="DELAY_TIME_SOIL_EMISSIONS_MANAGEMENT",
    units="Years",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_delay_time_soil_emissions_management"},
)
def delay_time_soil_emissions_management():
    """
    Time to reach equilibrium of soil carbon stock equal to 20 years (by default, provided by IPCC 2006 guidelines this is the time dependence of the stock change factors). This corresponds to a constant time/delay time (first order) of 20/4 = 5 years.
    """
    return _ext_constant_delay_time_soil_emissions_management()


_ext_constant_delay_time_soil_emissions_management = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "DELAY_TIME_SOIL_EMISSIONS_MANAGEMENT",
    {},
    _root,
    {},
    "_ext_constant_delay_time_soil_emissions_management",
)


@component.add(
    name="DIET_PATTERNS_DATA_BY_GDPpc_FOR_CHINA",
    units="kg/(Year*people)",
    subscripts=["FOODS_I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_diet_patterns_data_by_gdppc_for_china",
        "__lookup__": "_ext_lookup_diet_patterns_data_by_gdppc_for_china",
    },
)
def diet_patterns_data_by_gdppc_for_china(x, final_subs=None):
    return _ext_lookup_diet_patterns_data_by_gdppc_for_china(x, final_subs)


_ext_lookup_diet_patterns_data_by_gdppc_for_china = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Diet",
    "GDPpc_CHINA",
    "DIET_PATTERNS_CHINA",
    {"FOODS_I": _subscript_dict["FOODS_I"]},
    _root,
    {"FOODS_I": _subscript_dict["FOODS_I"]},
    "_ext_lookup_diet_patterns_data_by_gdppc_for_china",
)


@component.add(
    name="DIET_PATTERNS_DATA_BY_GDPpc_FOR_EASOC",
    units="kg/(Year*people)",
    subscripts=["FOODS_I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_diet_patterns_data_by_gdppc_for_easoc",
        "__lookup__": "_ext_lookup_diet_patterns_data_by_gdppc_for_easoc",
    },
)
def diet_patterns_data_by_gdppc_for_easoc(x, final_subs=None):
    return _ext_lookup_diet_patterns_data_by_gdppc_for_easoc(x, final_subs)


_ext_lookup_diet_patterns_data_by_gdppc_for_easoc = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Diet",
    "GDPpc_EASOC",
    "DIET_PATTERNS_EASOC",
    {"FOODS_I": _subscript_dict["FOODS_I"]},
    _root,
    {"FOODS_I": _subscript_dict["FOODS_I"]},
    "_ext_lookup_diet_patterns_data_by_gdppc_for_easoc",
)


@component.add(
    name="DIET_PATTERNS_DATA_BY_GDPpc_FOR_EU",
    units="kg/(Year*people)",
    subscripts=["FOODS_I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_diet_patterns_data_by_gdppc_for_eu",
        "__lookup__": "_ext_lookup_diet_patterns_data_by_gdppc_for_eu",
    },
)
def diet_patterns_data_by_gdppc_for_eu(x, final_subs=None):
    return _ext_lookup_diet_patterns_data_by_gdppc_for_eu(x, final_subs)


_ext_lookup_diet_patterns_data_by_gdppc_for_eu = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Diet",
    "GDPpc_EU",
    "DIET_PATTERNS_EU",
    {"FOODS_I": _subscript_dict["FOODS_I"]},
    _root,
    {"FOODS_I": _subscript_dict["FOODS_I"]},
    "_ext_lookup_diet_patterns_data_by_gdppc_for_eu",
)


@component.add(
    name="DIET_PATTERNS_DATA_BY_GDPpc_FOR_INDIA",
    units="kg/(Year*people)",
    subscripts=["FOODS_I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_diet_patterns_data_by_gdppc_for_india",
        "__lookup__": "_ext_lookup_diet_patterns_data_by_gdppc_for_india",
    },
)
def diet_patterns_data_by_gdppc_for_india(x, final_subs=None):
    return _ext_lookup_diet_patterns_data_by_gdppc_for_india(x, final_subs)


_ext_lookup_diet_patterns_data_by_gdppc_for_india = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Diet",
    "GDPpc_INDIA",
    "DIET_PATTERNS_INDIA",
    {"FOODS_I": _subscript_dict["FOODS_I"]},
    _root,
    {"FOODS_I": _subscript_dict["FOODS_I"]},
    "_ext_lookup_diet_patterns_data_by_gdppc_for_india",
)


@component.add(
    name="DIET_PATTERNS_DATA_BY_GDPpc_FOR_LATAM",
    units="kg/(Year*people)",
    subscripts=["FOODS_I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_diet_patterns_data_by_gdppc_for_latam",
        "__lookup__": "_ext_lookup_diet_patterns_data_by_gdppc_for_latam",
    },
)
def diet_patterns_data_by_gdppc_for_latam(x, final_subs=None):
    return _ext_lookup_diet_patterns_data_by_gdppc_for_latam(x, final_subs)


_ext_lookup_diet_patterns_data_by_gdppc_for_latam = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Diet",
    "GDPpc_LATAM",
    "DIET_PATTERNS_LATAM",
    {"FOODS_I": _subscript_dict["FOODS_I"]},
    _root,
    {"FOODS_I": _subscript_dict["FOODS_I"]},
    "_ext_lookup_diet_patterns_data_by_gdppc_for_latam",
)


@component.add(
    name="DIET_PATTERNS_DATA_BY_GDPpc_FOR_LROW",
    units="kg/(Year*people)",
    subscripts=["FOODS_I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_diet_patterns_data_by_gdppc_for_lrow",
        "__lookup__": "_ext_lookup_diet_patterns_data_by_gdppc_for_lrow",
    },
)
def diet_patterns_data_by_gdppc_for_lrow(x, final_subs=None):
    return _ext_lookup_diet_patterns_data_by_gdppc_for_lrow(x, final_subs)


_ext_lookup_diet_patterns_data_by_gdppc_for_lrow = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Diet",
    "GDPpc_LROW",
    "DIET_PATTERNS_LROW",
    {"FOODS_I": _subscript_dict["FOODS_I"]},
    _root,
    {"FOODS_I": _subscript_dict["FOODS_I"]},
    "_ext_lookup_diet_patterns_data_by_gdppc_for_lrow",
)


@component.add(
    name="DIET_PATTERNS_DATA_BY_GDPpc_FOR_RUSSIA",
    units="kg/(Year*people)",
    subscripts=["FOODS_I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_diet_patterns_data_by_gdppc_for_russia",
        "__lookup__": "_ext_lookup_diet_patterns_data_by_gdppc_for_russia",
    },
)
def diet_patterns_data_by_gdppc_for_russia(x, final_subs=None):
    return _ext_lookup_diet_patterns_data_by_gdppc_for_russia(x, final_subs)


_ext_lookup_diet_patterns_data_by_gdppc_for_russia = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Diet",
    "GDPpc_RUSSIA",
    "DIET_PATTERNS_RUSSIA",
    {"FOODS_I": _subscript_dict["FOODS_I"]},
    _root,
    {"FOODS_I": _subscript_dict["FOODS_I"]},
    "_ext_lookup_diet_patterns_data_by_gdppc_for_russia",
)


@component.add(
    name="DIET_PATTERNS_DATA_BY_GDPpc_FOR_UK",
    units="kg/(Year*people)",
    subscripts=["FOODS_I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_diet_patterns_data_by_gdppc_for_uk",
        "__lookup__": "_ext_lookup_diet_patterns_data_by_gdppc_for_uk",
    },
)
def diet_patterns_data_by_gdppc_for_uk(x, final_subs=None):
    return _ext_lookup_diet_patterns_data_by_gdppc_for_uk(x, final_subs)


_ext_lookup_diet_patterns_data_by_gdppc_for_uk = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Diet",
    "GDPpc_UK",
    "DIET_PATTERNS_UK",
    {"FOODS_I": _subscript_dict["FOODS_I"]},
    _root,
    {"FOODS_I": _subscript_dict["FOODS_I"]},
    "_ext_lookup_diet_patterns_data_by_gdppc_for_uk",
)


@component.add(
    name="DIET_PATTERNS_DATA_BY_GDPpc_FOR_USMCA",
    units="kg/(Year*people)",
    subscripts=["FOODS_I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_diet_patterns_data_by_gdppc_for_usmca",
        "__lookup__": "_ext_lookup_diet_patterns_data_by_gdppc_for_usmca",
    },
)
def diet_patterns_data_by_gdppc_for_usmca(x, final_subs=None):
    return _ext_lookup_diet_patterns_data_by_gdppc_for_usmca(x, final_subs)


_ext_lookup_diet_patterns_data_by_gdppc_for_usmca = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Diet",
    "GDPpc_USMCA",
    "DIET_PATTERNS_USMCA",
    {"FOODS_I": _subscript_dict["FOODS_I"]},
    _root,
    {"FOODS_I": _subscript_dict["FOODS_I"]},
    "_ext_lookup_diet_patterns_data_by_gdppc_for_usmca",
)


@component.add(
    name="EFFECT_OF_IRRIGATION_ON_YIELDS",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_effect_of_irrigation_on_yields"},
)
def effect_of_irrigation_on_yields():
    return _ext_constant_effect_of_irrigation_on_yields()


_ext_constant_effect_of_irrigation_on_yields = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "EFFECT_OF_IRRIGATION_ON_YIELDS",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
    },
    "_ext_constant_effect_of_irrigation_on_yields",
)


@component.add(
    name="EFFECT_OF_LOW_INPUT_AGRICULTURE",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_effect_of_low_input_agriculture"},
)
def effect_of_low_input_agriculture():
    """
    coparacion entre el rendimiento promedio de la agricultura tradicional y la industrial, tradicional low input /industrial high input <1
    """
    return _ext_constant_effect_of_low_input_agriculture()


_ext_constant_effect_of_low_input_agriculture = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "EFFECT_OF_LOW_INPUT_ON_YIELDS",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
    },
    "_ext_constant_effect_of_low_input_agriculture",
)


@component.add(
    name="EFFECT_OF_REGENERATIVE_AGRICULTURE",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_effect_of_regenerative_agriculture"},
)
def effect_of_regenerative_agriculture():
    return _ext_constant_effect_of_regenerative_agriculture()


_ext_constant_effect_of_regenerative_agriculture = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "EFFECT_OF_REGENERATIVE_ON_YIELDS",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
    },
    "_ext_constant_effect_of_regenerative_agriculture",
)


@component.add(
    name="EFFECTIVE_PERCENT_OF_LAND_CHANGE_PER_METER_OF_SEA_LEVEL_RISE",
    units="ha/m",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_effective_percent_of_land_change_per_meter_of_sea_level_rise"
    },
)
def effective_percent_of_land_change_per_meter_of_sea_level_rise():
    """
    the effective percent of land change per meter of sea level rise
    """
    return _ext_constant_effective_percent_of_land_change_per_meter_of_sea_level_rise()


_ext_constant_effective_percent_of_land_change_per_meter_of_sea_level_rise = (
    ExtConstant(
        "model_parameters/land_and_water/land_and_water.xlsx",
        "land_uses",
        "LOST_CROPLAND*",
        {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
        _root,
        {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
        "_ext_constant_effective_percent_of_land_change_per_meter_of_sea_level_rise",
    )
)


@component.add(
    name="ENERGY_TO_LAND_PRODUCTS_CONVERSION_FACTOR",
    units="EJ/t",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_energy_to_land_products_conversion_factor"
    },
)
def energy_to_land_products_conversion_factor():
    """
    conversion factor (from EJ to tonnes )
    """
    return _ext_constant_energy_to_land_products_conversion_factor()


_ext_constant_energy_to_land_products_conversion_factor = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Diet",
    "ENERGY_TO_LAND_PRODUCTS_CONVERSION_FACTOR",
    {},
    _root,
    {},
    "_ext_constant_energy_to_land_products_conversion_factor",
)


@component.add(
    name="ENERGY_TO_WOOD_CONVERSION_FACTOR",
    units="EJ/t",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_energy_to_wood_conversion_factor"},
)
def energy_to_wood_conversion_factor():
    """
    conversion factor (from TJ to tonnes or from tonnes to TJ)
    """
    return _ext_constant_energy_to_wood_conversion_factor()


_ext_constant_energy_to_wood_conversion_factor = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Diet",
    "ENERGY_TO_WOOD_CONVERSION_FACTOR*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_energy_to_wood_conversion_factor",
)


@component.add(
    name="EXO_LAND_FOR_SOLAR_DEMANDED",
    units="km2",
    subscripts=["REGIONS_9_I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_exo_land_for_solar_demanded",
        "__lookup__": "_ext_lookup_exo_land_for_solar_demanded",
    },
)
def exo_land_for_solar_demanded(x, final_subs=None):
    return _ext_lookup_exo_land_for_solar_demanded(x, final_subs)


_ext_lookup_exo_land_for_solar_demanded = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "exogenous_inputs",
    "TIME_EXOGENOUS_POPULATION",
    "EXOGENOUS_LAND_FOR_SOLAR_DEMANDED",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_lookup_exo_land_for_solar_demanded",
)


@component.add(
    name="EXO_LAND_USE_AREA_PRODUCTIVE_USES",
    units="km2",
    subscripts=["REGIONS_9_I", "LANDS_I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_exo_land_use_area_productive_uses",
        "__lookup__": "_ext_lookup_exo_land_use_area_productive_uses",
    },
)
def exo_land_use_area_productive_uses(x, final_subs=None):
    """
    Exogenous information from simulation- stock of land uses area productive uses by region
    """
    return _ext_lookup_exo_land_use_area_productive_uses(x, final_subs)


_ext_lookup_exo_land_use_area_productive_uses = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "TIME_EXO_SIMULATION",
    "EXO_land_use_area_productive_uses_EU27",
    {"REGIONS_9_I": ["EU27"], "LANDS_I": _subscript_dict["LANDS_I"]},
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": _subscript_dict["LANDS_I"],
    },
    "_ext_lookup_exo_land_use_area_productive_uses",
)

_ext_lookup_exo_land_use_area_productive_uses.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "TIME_EXO_SIMULATION",
    "EXO_land_use_area_productive_uses_UK",
    {"REGIONS_9_I": ["UK"], "LANDS_I": _subscript_dict["LANDS_I"]},
)

_ext_lookup_exo_land_use_area_productive_uses.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "TIME_EXO_SIMULATION",
    "EXO_land_use_area_productive_uses_CHINA",
    {"REGIONS_9_I": ["CHINA"], "LANDS_I": _subscript_dict["LANDS_I"]},
)

_ext_lookup_exo_land_use_area_productive_uses.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "TIME_EXO_SIMULATION",
    "EXO_land_use_area_productive_uses_EASOC",
    {"REGIONS_9_I": ["EASOC"], "LANDS_I": _subscript_dict["LANDS_I"]},
)

_ext_lookup_exo_land_use_area_productive_uses.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "TIME_EXO_SIMULATION",
    "EXO_land_use_area_productive_uses_INDIA",
    {"REGIONS_9_I": ["INDIA"], "LANDS_I": _subscript_dict["LANDS_I"]},
)

_ext_lookup_exo_land_use_area_productive_uses.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "TIME_EXO_SIMULATION",
    "EXO_land_use_area_productive_uses_LATAM",
    {"REGIONS_9_I": ["LATAM"], "LANDS_I": _subscript_dict["LANDS_I"]},
)

_ext_lookup_exo_land_use_area_productive_uses.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "TIME_EXO_SIMULATION",
    "EXO_land_use_area_productive_uses_RUSSIA",
    {"REGIONS_9_I": ["RUSSIA"], "LANDS_I": _subscript_dict["LANDS_I"]},
)

_ext_lookup_exo_land_use_area_productive_uses.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "TIME_EXO_SIMULATION",
    "EXO_land_use_area_productive_uses_USMCA",
    {"REGIONS_9_I": ["USMCA"], "LANDS_I": _subscript_dict["LANDS_I"]},
)

_ext_lookup_exo_land_use_area_productive_uses.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "TIME_EXO_SIMULATION",
    "EXO_land_use_area_productive_uses_LROW",
    {"REGIONS_9_I": ["LROW"], "LANDS_I": _subscript_dict["LANDS_I"]},
)


@component.add(
    name="EXO_OUTPUT_REAL_FOR_CONSTRUCTION_SECTOR",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_exo_output_real_for_construction_sector",
        "__lookup__": "_ext_lookup_exo_output_real_for_construction_sector",
    },
)
def exo_output_real_for_construction_sector(x, final_subs=None):
    return _ext_lookup_exo_output_real_for_construction_sector(x, final_subs)


_ext_lookup_exo_output_real_for_construction_sector = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "exogenous_inputs",
    "TIME_EXOGENOUS_POPULATION",
    "OUTPUT_CONSTRUCTION",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_lookup_exo_output_real_for_construction_sector",
)


@component.add(
    name="EXO_OUTPUT_REAL_FOR_FORESTRY_SECTOR",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_exo_output_real_for_forestry_sector",
        "__lookup__": "_ext_lookup_exo_output_real_for_forestry_sector",
    },
)
def exo_output_real_for_forestry_sector(x, final_subs=None):
    """
    Output real for forestry sector constant values for 9 regions
    """
    return _ext_lookup_exo_output_real_for_forestry_sector(x, final_subs)


_ext_lookup_exo_output_real_for_forestry_sector = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "exogenous_inputs",
    "TIME_EXOGENOUS_POPULATION",
    "EXOGENOUS_OUTPUT_REAL_FORESTRY",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_lookup_exo_output_real_for_forestry_sector",
)


@component.add(
    name="EXO_OUTPUT_REAL_FOR_MANUFACTURE_WOOD_SECTOR",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_exo_output_real_for_manufacture_wood_sector",
        "__lookup__": "_ext_lookup_exo_output_real_for_manufacture_wood_sector",
    },
)
def exo_output_real_for_manufacture_wood_sector(x, final_subs=None):
    return _ext_lookup_exo_output_real_for_manufacture_wood_sector(x, final_subs)


_ext_lookup_exo_output_real_for_manufacture_wood_sector = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "exogenous_inputs",
    "TIME_EXOGENOUS_POPULATION",
    "OUTPUT_MANU_WOOD",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_lookup_exo_output_real_for_manufacture_wood_sector",
)


@component.add(
    name="EXO_POPULATION_35R",
    units="people",
    subscripts=["REGIONS_35_I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_exo_population_35r",
        "__lookup__": "_ext_lookup_exo_population_35r",
    },
)
def exo_population_35r(x, final_subs=None):
    return _ext_lookup_exo_population_35r(x, final_subs)


_ext_lookup_exo_population_35r = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "exogenous_inputs",
    "TIME_EXOGENOUS_POPULATION",
    "EXOGENOUS_POPULATION_35R",
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    _root,
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    "_ext_lookup_exo_population_35r",
)


@component.add(
    name="EXO_PV_LAND_OCCUPATION_RATIO",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_exo_pv_land_occupation_ratio",
        "__lookup__": "_ext_lookup_exo_pv_land_occupation_ratio",
    },
)
def exo_pv_land_occupation_ratio(x, final_subs=None):
    """
    Exogenous information from simulation- stock of PV land occupation ratio
    """
    return _ext_lookup_exo_pv_land_occupation_ratio(x, final_subs)


_ext_lookup_exo_pv_land_occupation_ratio = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "TIME_EXO_SIMULATION",
    "EXO_PV_LAND_OCCUPATION_RATIO",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_lookup_exo_pv_land_occupation_ratio",
)


@component.add(
    name="EXOGENOUS_POPULATION_9R",
    units="people",
    subscripts=["REGIONS_9_I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_exogenous_population_9r",
        "__lookup__": "_ext_lookup_exogenous_population_9r",
    },
)
def exogenous_population_9r(x, final_subs=None):
    """
    population historical data by rehion
    """
    return _ext_lookup_exogenous_population_9r(x, final_subs)


_ext_lookup_exogenous_population_9r = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "exogenous_inputs",
    "TIME_EXOGENOUS_POPULATION",
    "EXOGENOUS_POPULATION_9R",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_lookup_exogenous_population_9r",
)


@component.add(
    name="FACTOR_ALFA_1_EFFECTS_OF_CC_ON_YIELDS",
    subscripts=["CLIMATIC_ZONES_I", "LAND_PRODUCTS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_factor_alfa_1_effects_of_cc_on_yields"},
)
def factor_alfa_1_effects_of_cc_on_yields():
    return _ext_constant_factor_alfa_1_effects_of_cc_on_yields()


_ext_constant_factor_alfa_1_effects_of_cc_on_yields = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "FACTOR_ALFA_1_EFFECTS_OF_CC_ON_YIELDS",
    {
        "CLIMATIC_ZONES_I": _subscript_dict["CLIMATIC_ZONES_I"],
        "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
    },
    _root,
    {
        "CLIMATIC_ZONES_I": _subscript_dict["CLIMATIC_ZONES_I"],
        "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
    },
    "_ext_constant_factor_alfa_1_effects_of_cc_on_yields",
)


@component.add(
    name="FACTOR_ALFA_2_EFFECTS_OF_CC_ON_YIELDS",
    subscripts=["CLIMATIC_ZONES_I", "LAND_PRODUCTS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_factor_alfa_2_effects_of_cc_on_yields"},
)
def factor_alfa_2_effects_of_cc_on_yields():
    return _ext_constant_factor_alfa_2_effects_of_cc_on_yields()


_ext_constant_factor_alfa_2_effects_of_cc_on_yields = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "FACTOR_ALFA_2_EFFECTS_OF_CC_ON_YIELDS",
    {
        "CLIMATIC_ZONES_I": _subscript_dict["CLIMATIC_ZONES_I"],
        "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
    },
    _root,
    {
        "CLIMATIC_ZONES_I": _subscript_dict["CLIMATIC_ZONES_I"],
        "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
    },
    "_ext_constant_factor_alfa_2_effects_of_cc_on_yields",
)


@component.add(
    name="FACTOR_B_1_EFFECTS_OF_CC_ON_YIELDS",
    subscripts=["CLIMATIC_ZONES_I", "LAND_PRODUCTS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_factor_b_1_effects_of_cc_on_yields"},
)
def factor_b_1_effects_of_cc_on_yields():
    return _ext_constant_factor_b_1_effects_of_cc_on_yields()


_ext_constant_factor_b_1_effects_of_cc_on_yields = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "FACTOR_B_1_EFFECTS_OF_CC_ON_YIELDS",
    {
        "CLIMATIC_ZONES_I": _subscript_dict["CLIMATIC_ZONES_I"],
        "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
    },
    _root,
    {
        "CLIMATIC_ZONES_I": _subscript_dict["CLIMATIC_ZONES_I"],
        "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
    },
    "_ext_constant_factor_b_1_effects_of_cc_on_yields",
)


@component.add(
    name="FACTOR_B_2_EFFECTS_OF_CC_ON_YIELDS",
    subscripts=["CLIMATIC_ZONES_I", "LAND_PRODUCTS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_factor_b_2_effects_of_cc_on_yields"},
)
def factor_b_2_effects_of_cc_on_yields():
    return _ext_constant_factor_b_2_effects_of_cc_on_yields()


_ext_constant_factor_b_2_effects_of_cc_on_yields = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "FACTOR_B_2_EFFECTS_OF_CC_ON_YIELDS",
    {
        "CLIMATIC_ZONES_I": _subscript_dict["CLIMATIC_ZONES_I"],
        "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
    },
    _root,
    {
        "CLIMATIC_ZONES_I": _subscript_dict["CLIMATIC_ZONES_I"],
        "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
    },
    "_ext_constant_factor_b_2_effects_of_cc_on_yields",
)


@component.add(
    name="FACTOR_INPUT_HIGH_WITH_MANURE_CROPS",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_factor_input_high_with_manure_crops"},
)
def factor_input_high_with_manure_crops():
    """
    Stock change factor input (FI) High with manure
    """
    return _ext_constant_factor_input_high_with_manure_crops()


_ext_constant_factor_input_high_with_manure_crops = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "FACTOR_INPUT_HIGHWMANURE_CROPS",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_factor_input_high_with_manure_crops",
)


@component.add(
    name="FACTOR_INPUT_HIGH_WITHOUT_MANURE_CROPS",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_factor_input_high_without_manure_crops"},
)
def factor_input_high_without_manure_crops():
    """
    Stock change factor input (FI) High with-out manure
    """
    return _ext_constant_factor_input_high_without_manure_crops()


_ext_constant_factor_input_high_without_manure_crops = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "FACTOR_INPUT_HIGHWOUTMANURE_CROPS",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_factor_input_high_without_manure_crops",
)


@component.add(
    name="FACTOR_INPUT_LOW_CROPS",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_factor_input_low_crops"},
)
def factor_input_low_crops():
    """
    Stock change factor input (FI) low
    """
    return _ext_constant_factor_input_low_crops()


_ext_constant_factor_input_low_crops = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "FACTOR_INPUT_LOW_CROPS",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_factor_input_low_crops",
)


@component.add(
    name="FACTOR_INPUT_MEDIUM_CROPS",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_factor_input_medium_crops"},
)
def factor_input_medium_crops():
    """
    Stock change factor input (FI) medium
    """
    return _ext_constant_factor_input_medium_crops()


_ext_constant_factor_input_medium_crops = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "FACTOR_INPUT_MEDIUM_CROPS",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_factor_input_medium_crops",
)


@component.add(
    name="FACTOR_LANDUSE_LONGTERM_CULTIVATED_CROP",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_factor_landuse_longterm_cultivated_crop"
    },
)
def factor_landuse_longterm_cultivated_crop():
    """
    Stock change factor land use (FLU) Long-term cultivated
    """
    return _ext_constant_factor_landuse_longterm_cultivated_crop()


_ext_constant_factor_landuse_longterm_cultivated_crop = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "FACTOR_LANDUSE_LONGTERMCULT",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_factor_landuse_longterm_cultivated_crop",
)


@component.add(
    name="FACTOR_LANDUSE_PADDY_RICE",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_factor_landuse_paddy_rice"},
)
def factor_landuse_paddy_rice():
    """
    Stock change factor land use (FLU) paddy rice
    """
    return _ext_constant_factor_landuse_paddy_rice()


_ext_constant_factor_landuse_paddy_rice = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "FACTOR_LANDUSE_PADDY_RICE",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_factor_landuse_paddy_rice",
)


@component.add(
    name="FACTOR_LANDUSE_PERENNIAL_TREE_CROP",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_factor_landuse_perennial_tree_crop"},
)
def factor_landuse_perennial_tree_crop():
    """
    Stock change factor land use (FLU) Perennial/tree crop
    """
    return _ext_constant_factor_landuse_perennial_tree_crop()


_ext_constant_factor_landuse_perennial_tree_crop = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "FACTOR_LANDUSE_PERENIAL_TREECROP",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_factor_landuse_perennial_tree_crop",
)


@component.add(
    name="FACTOR_LANDUSE_SET_ASSIDE_CROP",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_factor_landuse_set_asside_crop"},
)
def factor_landuse_set_asside_crop():
    """
    Stock change factor land use (FLU) SET ASSIDE
    """
    return _ext_constant_factor_landuse_set_asside_crop()


_ext_constant_factor_landuse_set_asside_crop = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "FACTOR_LANDUSE_SET_ASSIDE",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_factor_landuse_set_asside_crop",
)


@component.add(
    name="FACTOR_MANAGEMENT_FULL_TILLAGE_CROPS",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_factor_management_full_tillage_crops"},
)
def factor_management_full_tillage_crops():
    """
    Stock change factor management (FMG) full tillage
    """
    return _ext_constant_factor_management_full_tillage_crops()


_ext_constant_factor_management_full_tillage_crops = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "FACTOR_MANAGEMENT_FULL_TILLAGE_CROPS",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_factor_management_full_tillage_crops",
)


@component.add(
    name="FACTOR_MANAGEMENT_IMPROVED_HIGH_GRASSLAND",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_factor_management_improved_high_grassland"
    },
)
def factor_management_improved_high_grassland():
    """
    Stock change factor management IMPROVED_HIGH_ inputs grassland
    """
    return _ext_constant_factor_management_improved_high_grassland()


_ext_constant_factor_management_improved_high_grassland = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "FACTOR_MANAGEMENT_IMPROVED_HIGH_GRASSLAND*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_factor_management_improved_high_grassland",
)


@component.add(
    name="FACTOR_MANAGEMENT_IMPROVED_MEDIUM_GRASSLAND",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_factor_management_improved_medium_grassland"
    },
)
def factor_management_improved_medium_grassland():
    """
    Stock change factor management MPROVED with MEDIUM inputs grassland
    """
    return _ext_constant_factor_management_improved_medium_grassland()


_ext_constant_factor_management_improved_medium_grassland = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "FACTOR_MANAGEMENT_IMPROVED_MEDIUM_GRASSLAND*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_factor_management_improved_medium_grassland",
)


@component.add(
    name="FACTOR_MANAGEMENT_MODERATELY_DEGRADED_GRASSLAND",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_factor_management_moderately_degraded_grassland"
    },
)
def factor_management_moderately_degraded_grassland():
    """
    Stock change factor management MODERATELY_DEGRADED grassland
    """
    return _ext_constant_factor_management_moderately_degraded_grassland()


_ext_constant_factor_management_moderately_degraded_grassland = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "FACTOR_MANAGEMENT_MODERATELY_DEGRADED_GRASSLAND*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_factor_management_moderately_degraded_grassland",
)


@component.add(
    name="FACTOR_MANAGEMENT_NOMINALLY_MANAGED_GRASSLAND",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_factor_management_nominally_managed_grassland"
    },
)
def factor_management_nominally_managed_grassland():
    """
    Stock change factor management nominally managed grassland
    """
    return _ext_constant_factor_management_nominally_managed_grassland()


_ext_constant_factor_management_nominally_managed_grassland = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "FACTOR_MANAGEMENT_NOMINALLY_MANAGED_GRASSLAND*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_factor_management_nominally_managed_grassland",
)


@component.add(
    name="FACTOR_MANAGEMENT_NOTILL_TILLAGE_CROPS",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_factor_management_notill_tillage_crops"},
)
def factor_management_notill_tillage_crops():
    """
    Stock change factor management (FMG) no till
    """
    return _ext_constant_factor_management_notill_tillage_crops()


_ext_constant_factor_management_notill_tillage_crops = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "FACTOR_MANAGEMENT_NO_TILL_CROPS",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_factor_management_notill_tillage_crops",
)


@component.add(
    name="FACTOR_MANAGEMENT_REDUCE_TILLAGE_CROPS",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_factor_management_reduce_tillage_crops"},
)
def factor_management_reduce_tillage_crops():
    """
    Stock change factor management (FMG) reduced tillage
    """
    return _ext_constant_factor_management_reduce_tillage_crops()


_ext_constant_factor_management_reduce_tillage_crops = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "FACTOR_MANAGEMENT_REDUCED_TILLAGE_CROPS",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_factor_management_reduce_tillage_crops",
)


@component.add(
    name="FACTOR_MANAGEMENT_SEVERELY_DEGRADED_GRASSLAND",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_factor_management_severely_degraded_grassland"
    },
)
def factor_management_severely_degraded_grassland():
    """
    Stock change factor management SEVERELY_DEGRADED grassland
    """
    return _ext_constant_factor_management_severely_degraded_grassland()


_ext_constant_factor_management_severely_degraded_grassland = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "FACTOR_MANAGEMENT_SEVERELY_DEGRADED_GRASSLAND*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_factor_management_severely_degraded_grassland",
)


@component.add(
    name="FACTOR_OF_CARBON_CAPTURE_OF_GRASSLANDS",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def factor_of_carbon_capture_of_grasslands():
    return xr.DataArray(
        0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
    )


@component.add(
    name="FACTOR_OF_CARBON_CAPTURE_OF_REGENERATIVE_GRASSLANDS",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def factor_of_carbon_capture_of_regenerative_grasslands():
    return xr.DataArray(
        0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
    )


@component.add(
    name="FACTOR_OF_FOOD_AVAILABILITY",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="Normal",
)
def factor_of_food_availability():
    return 1


@component.add(
    name="FACTOR_OF_GAIN_OF_REGENERATIVE_GRAZING",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_factor_of_gain_of_regenerative_grazing"},
)
def factor_of_gain_of_regenerative_grazing():
    return _ext_constant_factor_of_gain_of_regenerative_grazing()


_ext_constant_factor_of_gain_of_regenerative_grazing = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "GAIN_OF_REGENERATIVE_GRAZING",
    {},
    _root,
    {},
    "_ext_constant_factor_of_gain_of_regenerative_grazing",
)


@component.add(
    name="FEEDBACK_PARAMETER_CROPS_KI", comp_type="Constant", comp_subtype="Normal"
)
def feedback_parameter_crops_ki():
    return 0.006


@component.add(
    name="FEEDBACK_PARAMETER_CROPS_KP", comp_type="Constant", comp_subtype="Normal"
)
def feedback_parameter_crops_kp():
    return 0.03


@component.add(
    name="FIRST_FACTOR_WATER_EQUATION",
    units="DMNL",
    subscripts=["REGIONS_35_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_first_factor_water_equation"},
)
def first_factor_water_equation():
    return _ext_constant_first_factor_water_equation()


_ext_constant_first_factor_water_equation = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Water",
    "WA_Projections_Eq_Factor_1*",
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    _root,
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    "_ext_constant_first_factor_water_equation",
)


@component.add(
    name="FLEXITARIANA_DIET_PATTERNS_OF_POLICY_DIETS_SP",
    units="kg/(Year*people)",
    subscripts=["REGIONS_9_I", "FOODS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_flexitariana_diet_patterns_of_policy_diets_sp"
    },
)
def flexitariana_diet_patterns_of_policy_diets_sp():
    """
    Flexitariana policy diet
    """
    return _ext_constant_flexitariana_diet_patterns_of_policy_diets_sp()


_ext_constant_flexitariana_diet_patterns_of_policy_diets_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "FLEXITARIANA_DIET_PATTERN_OF_POLICY_DIETS_SP",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "FOODS_I": _subscript_dict["FOODS_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "FOODS_I": _subscript_dict["FOODS_I"],
    },
    "_ext_constant_flexitariana_diet_patterns_of_policy_diets_sp",
)


@component.add(
    name="FOOD_COMPOSITION_TABLE",
    units="DMNL",
    subscripts=["FOODS_I", "NUTRITION_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_food_composition_table"},
)
def food_composition_table():
    """
    Matrix to translate from food products to nutrtition categories by 100 grams of intake
    """
    return _ext_constant_food_composition_table()


_ext_constant_food_composition_table = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Nutrition",
    "FOOD_COMPOSITION_TABLE",
    {
        "FOODS_I": _subscript_dict["FOODS_I"],
        "NUTRITION_I": _subscript_dict["NUTRITION_I"],
    },
    _root,
    {
        "FOODS_I": _subscript_dict["FOODS_I"],
        "NUTRITION_I": _subscript_dict["NUTRITION_I"],
    },
    "_ext_constant_food_composition_table",
)


@component.add(
    name="FOOD_LOSS_PARAMETERS",
    units="DMNL",
    subscripts=["REGIONS_9_I", "FOODS_I", "FOOD_LOSSES_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_food_loss_parameters"},
)
def food_loss_parameters():
    """
    food loss parameters
    """
    return _ext_constant_food_loss_parameters()


_ext_constant_food_loss_parameters = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Nutrition",
    "FOOD_LOSS_PARAMETERS_EU27",
    {
        "REGIONS_9_I": ["EU27"],
        "FOODS_I": _subscript_dict["FOODS_I"],
        "FOOD_LOSSES_I": _subscript_dict["FOOD_LOSSES_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "FOODS_I": _subscript_dict["FOODS_I"],
        "FOOD_LOSSES_I": _subscript_dict["FOOD_LOSSES_I"],
    },
    "_ext_constant_food_loss_parameters",
)

_ext_constant_food_loss_parameters.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Nutrition",
    "FOOD_LOSS_PARAMETERS_UK",
    {
        "REGIONS_9_I": ["UK"],
        "FOODS_I": _subscript_dict["FOODS_I"],
        "FOOD_LOSSES_I": _subscript_dict["FOOD_LOSSES_I"],
    },
)

_ext_constant_food_loss_parameters.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Nutrition",
    "FOOD_LOSS_PARAMETERS_CHINA",
    {
        "REGIONS_9_I": ["CHINA"],
        "FOODS_I": _subscript_dict["FOODS_I"],
        "FOOD_LOSSES_I": _subscript_dict["FOOD_LOSSES_I"],
    },
)

_ext_constant_food_loss_parameters.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Nutrition",
    "FOOD_LOSS_PARAMETERS_EASOC",
    {
        "REGIONS_9_I": ["EASOC"],
        "FOODS_I": _subscript_dict["FOODS_I"],
        "FOOD_LOSSES_I": _subscript_dict["FOOD_LOSSES_I"],
    },
)

_ext_constant_food_loss_parameters.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Nutrition",
    "FOOD_LOSS_PARAMETERS_INDIA",
    {
        "REGIONS_9_I": ["INDIA"],
        "FOODS_I": _subscript_dict["FOODS_I"],
        "FOOD_LOSSES_I": _subscript_dict["FOOD_LOSSES_I"],
    },
)

_ext_constant_food_loss_parameters.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Nutrition",
    "FOOD_LOSS_PARAMETERS_LATAM",
    {
        "REGIONS_9_I": ["LATAM"],
        "FOODS_I": _subscript_dict["FOODS_I"],
        "FOOD_LOSSES_I": _subscript_dict["FOOD_LOSSES_I"],
    },
)

_ext_constant_food_loss_parameters.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Nutrition",
    "FOOD_LOSS_PARAMETERS_RUSSIA",
    {
        "REGIONS_9_I": ["RUSSIA"],
        "FOODS_I": _subscript_dict["FOODS_I"],
        "FOOD_LOSSES_I": _subscript_dict["FOOD_LOSSES_I"],
    },
)

_ext_constant_food_loss_parameters.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Nutrition",
    "FOOD_LOSS_PARAMETERS_USMCA",
    {
        "REGIONS_9_I": ["USMCA"],
        "FOODS_I": _subscript_dict["FOODS_I"],
        "FOOD_LOSSES_I": _subscript_dict["FOOD_LOSSES_I"],
    },
)

_ext_constant_food_loss_parameters.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Nutrition",
    "FOOD_LOSS_PARAMETERS_LROW",
    {
        "REGIONS_9_I": ["LROW"],
        "FOODS_I": _subscript_dict["FOODS_I"],
        "FOOD_LOSSES_I": _subscript_dict["FOOD_LOSSES_I"],
    },
)


@component.add(
    name="GDP_OEKSTRA_2019",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_gdp_oekstra_2019"},
)
def gdp_oekstra_2019():
    return _ext_constant_gdp_oekstra_2019()


_ext_constant_gdp_oekstra_2019 = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Water",
    "GDP_BY_OEKSTRA_2019*",
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    _root,
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    "_ext_constant_gdp_oekstra_2019",
)


@component.add(
    name="GDP_OEKSTRA_INITIAL",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_gdp_oekstra_initial"},
)
def gdp_oekstra_initial():
    return _ext_constant_gdp_oekstra_initial()


_ext_constant_gdp_oekstra_initial = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Water",
    "GDPw_B2*",
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    _root,
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    "_ext_constant_gdp_oekstra_initial",
)


@component.add(
    name="GDP_VARIATION_BY_OEKSTRA",
    subscripts=["REGIONS_35_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_gdp_variation_by_oekstra"},
)
def gdp_variation_by_oekstra():
    """
    Put here the output of each sector and region by Oekstra estimations
    """
    return _ext_constant_gdp_variation_by_oekstra()


_ext_constant_gdp_variation_by_oekstra = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Water",
    "GDPw_var_B2*",
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    _root,
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    "_ext_constant_gdp_variation_by_oekstra",
)


@component.add(
    name="HISTORICAL_AFFORESTATION_BY_REGION",
    units="km2/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_historical_afforestation_by_region",
        "__lookup__": "_ext_lookup_historical_afforestation_by_region",
    },
)
def historical_afforestation_by_region(x, final_subs=None):
    """
    Historical data of land uses change to afforestation by region
    """
    return _ext_lookup_historical_afforestation_by_region(x, final_subs)


_ext_lookup_historical_afforestation_by_region = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "TIME_LAND_USE",
    "HISTORICAL_AFFORESTATION_BY_REGION",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_lookup_historical_afforestation_by_region",
)


@component.add(
    name="HISTORICAL_AREA_OF_CROPS_ALL_MANAGEMENT",
    units="km2",
    subscripts=["LAND_PRODUCTS_I", "REGIONS_9_I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_historical_area_of_crops_all_management",
        "__lookup__": "_ext_lookup_historical_area_of_crops_all_management",
    },
)
def historical_area_of_crops_all_management(x, final_subs=None):
    """
    FAO data only per region mixing irrigated and rainfed
    """
    return _ext_lookup_historical_area_of_crops_all_management(x, final_subs)


_ext_lookup_historical_area_of_crops_all_management = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_AREA_OF_CROPS_EU27",
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"], "REGIONS_9_I": ["EU27"]},
    _root,
    {
        "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
    },
    "_ext_lookup_historical_area_of_crops_all_management",
)

_ext_lookup_historical_area_of_crops_all_management.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_AREA_OF_CROPS_UK",
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"], "REGIONS_9_I": ["UK"]},
)

_ext_lookup_historical_area_of_crops_all_management.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_AREA_OF_CROPS_CHINA",
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"], "REGIONS_9_I": ["CHINA"]},
)

_ext_lookup_historical_area_of_crops_all_management.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_AREA_OF_CROPS_EASOC",
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"], "REGIONS_9_I": ["EASOC"]},
)

_ext_lookup_historical_area_of_crops_all_management.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_AREA_OF_CROPS_INDIA",
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"], "REGIONS_9_I": ["INDIA"]},
)

_ext_lookup_historical_area_of_crops_all_management.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_AREA_OF_CROPS_LATAM",
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"], "REGIONS_9_I": ["LATAM"]},
)

_ext_lookup_historical_area_of_crops_all_management.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_AREA_OF_CROPS_RUSSIA",
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"], "REGIONS_9_I": ["RUSSIA"]},
)

_ext_lookup_historical_area_of_crops_all_management.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_AREA_OF_CROPS_USMCA",
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"], "REGIONS_9_I": ["USMCA"]},
)

_ext_lookup_historical_area_of_crops_all_management.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_AREA_OF_CROPS_LROW",
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"], "REGIONS_9_I": ["LROW"]},
)


@component.add(
    name="HISTORICAL_AVERAGE_FOREST_STOCK_LOSS",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_historical_average_forest_stock_loss"},
)
def historical_average_forest_stock_loss():
    """
    Average share of forest stock loss during historical period
    """
    return _ext_constant_historical_average_forest_stock_loss()


_ext_constant_historical_average_forest_stock_loss = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "forest",
    "HISTORICAL_FOREST_STOCK_LOSS*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_historical_average_forest_stock_loss",
)


@component.add(
    name="HISTORICAL_CROPS_PRODUCTION_FAO",
    units="t/Year",
    subscripts=["LAND_PRODUCTS_I", "REGIONS_9_I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_historical_crops_production_fao",
        "__lookup__": "_ext_lookup_historical_crops_production_fao",
    },
)
def historical_crops_production_fao(x, final_subs=None):
    """
    FAO data only per region mixing irrigated and rainfed
    """
    return _ext_lookup_historical_crops_production_fao(x, final_subs)


_ext_lookup_historical_crops_production_fao = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_CROPS_FAO_EU27",
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"], "REGIONS_9_I": ["EU27"]},
    _root,
    {
        "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
    },
    "_ext_lookup_historical_crops_production_fao",
)

_ext_lookup_historical_crops_production_fao.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_CROPS_FAO_UK",
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"], "REGIONS_9_I": ["UK"]},
)

_ext_lookup_historical_crops_production_fao.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_CROPS_FAO_CHINA",
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"], "REGIONS_9_I": ["CHINA"]},
)

_ext_lookup_historical_crops_production_fao.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_CROPS_FAO_EASOC",
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"], "REGIONS_9_I": ["EASOC"]},
)

_ext_lookup_historical_crops_production_fao.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_CROPS_FAO_INDIA",
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"], "REGIONS_9_I": ["INDIA"]},
)

_ext_lookup_historical_crops_production_fao.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_CROPS_FAO_LATAM",
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"], "REGIONS_9_I": ["LATAM"]},
)

_ext_lookup_historical_crops_production_fao.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_CROPS_FAO_RUSSIA",
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"], "REGIONS_9_I": ["RUSSIA"]},
)

_ext_lookup_historical_crops_production_fao.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_CROPS_FAO_USMCA",
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"], "REGIONS_9_I": ["USMCA"]},
)

_ext_lookup_historical_crops_production_fao.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_CROPS_FAO_LROW",
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"], "REGIONS_9_I": ["LROW"]},
)


@component.add(
    name="HISTORICAL_FOREST_VOLUME_STOCK_ALL_FORESTS",
    units="m3",
    subscripts=["REGIONS_9_I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_historical_forest_volume_stock_all_forests",
        "__lookup__": "_ext_lookup_historical_forest_volume_stock_all_forests",
    },
)
def historical_forest_volume_stock_all_forests(x, final_subs=None):
    """
    historical forest volume stock change by region
    """
    return _ext_lookup_historical_forest_volume_stock_all_forests(x, final_subs)


_ext_lookup_historical_forest_volume_stock_all_forests = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "forest",
    "TIME_FORESTS",
    "HISTORICAL_FOREST_VOLUME_STOCK_ALL_FORESTS",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_lookup_historical_forest_volume_stock_all_forests",
)


@component.add(
    name="HISTORICAL_FOREST_VOLUME_STOCK_CHANGE_ALL_FORESTS",
    units="m3/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_historical_forest_volume_stock_change_all_forests",
        "__lookup__": "_ext_lookup_historical_forest_volume_stock_change_all_forests",
    },
)
def historical_forest_volume_stock_change_all_forests(x, final_subs=None):
    """
    historical forest volume stock change by region
    """
    return _ext_lookup_historical_forest_volume_stock_change_all_forests(x, final_subs)


_ext_lookup_historical_forest_volume_stock_change_all_forests = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "forest",
    "TIME_FORESTS",
    "HISTORICAL_FOREST_VOLUME_STOCK_CHANGE_ALL_FORESTS",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_lookup_historical_forest_volume_stock_change_all_forests",
)


@component.add(
    name="HISTORICAL_LAND_PRODUCTS_PRODUCTION",
    units="t/Year",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_historical_land_products_production",
        "__data__": "_ext_data_historical_land_products_production",
        "time": 1,
    },
)
def historical_land_products_production():
    """
    land products production (FAO data)
    """
    return _ext_data_historical_land_products_production(time())


_ext_data_historical_land_products_production = ExtData(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "diet",
    "TIME_LP",
    "CORN",
    None,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"], "LAND_PRODUCTS_I": ["CORN"]},
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
    },
    "_ext_data_historical_land_products_production",
)

_ext_data_historical_land_products_production.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "diet",
    "TIME_LP",
    "RICE",
    None,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"], "LAND_PRODUCTS_I": ["RICE"]},
)

_ext_data_historical_land_products_production.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "diet",
    "TIME_LP",
    "CEREALS",
    None,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LAND_PRODUCTS_I": ["CEREALS_OTHER"],
    },
)

_ext_data_historical_land_products_production.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "diet",
    "TIME_LP",
    "TUBERS",
    None,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"], "LAND_PRODUCTS_I": ["TUBERS"]},
)

_ext_data_historical_land_products_production.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "diet",
    "TIME_LP",
    "SOY",
    None,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"], "LAND_PRODUCTS_I": ["SOY"]},
)

_ext_data_historical_land_products_production.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "diet",
    "TIME_LP",
    "PULSES_NUTS",
    None,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"], "LAND_PRODUCTS_I": ["PULSES_NUTS"]},
)

_ext_data_historical_land_products_production.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "diet",
    "TIME_LP",
    "OILCROPS",
    None,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"], "LAND_PRODUCTS_I": ["OILCROPS"]},
)

_ext_data_historical_land_products_production.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "diet",
    "TIME_LP",
    "SUGARS",
    None,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"], "LAND_PRODUCTS_I": ["SUGAR_CROPS"]},
)

_ext_data_historical_land_products_production.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "diet",
    "TIME_LP",
    "VEGETABLES_FRUITS",
    None,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LAND_PRODUCTS_I": ["FRUITS_VEGETABLES"],
    },
)

_ext_data_historical_land_products_production.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "diet",
    "TIME_LP",
    "BIOFUEL",
    None,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LAND_PRODUCTS_I": ["BIOFUEL_2GCROP"],
    },
)

_ext_data_historical_land_products_production.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "diet",
    "TIME_LP",
    "OTHER_CROPS",
    None,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"], "LAND_PRODUCTS_I": ["OTHER_CROPS"]},
)

_ext_data_historical_land_products_production.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "diet",
    "TIME_LP",
    "WOOD",
    None,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"], "LAND_PRODUCTS_I": ["WOOD"]},
)

_ext_data_historical_land_products_production.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "diet",
    "TIME_LP",
    "RESIDUES",
    None,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"], "LAND_PRODUCTS_I": ["RESIDUES"]},
)


@component.add(
    name="HISTORICAL_LAND_USE_BY_REGION",
    units="km2/Year",
    subscripts=["REGIONS_9_I", "LANDS_I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_historical_land_use_by_region",
        "__lookup__": "_ext_lookup_historical_land_use_by_region",
    },
)
def historical_land_use_by_region(x, final_subs=None):
    """
    HISTORICAL_LAND_USE_BY_REGION
    """
    return _ext_lookup_historical_land_use_by_region(x, final_subs)


_ext_lookup_historical_land_use_by_region = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "TIME_LAND_USE",
    "HISTORICAL_CROPLAND_RAINFED_BY_REGION",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"], "LANDS_I": ["CROPLAND_RAINFED"]},
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": _subscript_dict["LANDS_I"],
    },
    "_ext_lookup_historical_land_use_by_region",
)

_ext_lookup_historical_land_use_by_region.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "TIME_LAND_USE",
    "HISTORICAL_CROPLAND_IRRIGATED_BY_REGION",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"], "LANDS_I": ["CROPLAND_IRRIGATED"]},
)

_ext_lookup_historical_land_use_by_region.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "TIME_LAND_USE",
    "HISTORICAL_FOREST_MANAGED_BY_REGION",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"], "LANDS_I": ["FOREST_MANAGED"]},
)

_ext_lookup_historical_land_use_by_region.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "TIME_LAND_USE",
    "HISTORICAL_FOREST_PRIMARY_BY_REGION",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"], "LANDS_I": ["FOREST_PRIMARY"]},
)

_ext_lookup_historical_land_use_by_region.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "TIME_LAND_USE",
    "HISTORICAL_FOREST_PLANTATIONS_BY_REGION",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"], "LANDS_I": ["FOREST_PLANTATIONS"]},
)

_ext_lookup_historical_land_use_by_region.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "TIME_LAND_USE",
    "HISTORICAL_SHRUBLAND_BY_REGION",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"], "LANDS_I": ["SHRUBLAND"]},
)

_ext_lookup_historical_land_use_by_region.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "TIME_LAND_USE",
    "HISTORICAL_GRASSLAND_BY_REGION",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"], "LANDS_I": ["GRASSLAND"]},
)

_ext_lookup_historical_land_use_by_region.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "TIME_LAND_USE",
    "HISTORICAL_WETLAND_BY_REGION",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"], "LANDS_I": ["WETLAND"]},
)

_ext_lookup_historical_land_use_by_region.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "TIME_LAND_USE",
    "HISTORICAL_URBAN_LAND_BY_REGION",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"], "LANDS_I": ["URBAN_LAND"]},
)

_ext_lookup_historical_land_use_by_region.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "TIME_LAND_USE",
    "HISTORICAL_SOLAR_LAND_BY_REGION",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"], "LANDS_I": ["SOLAR_LAND"]},
)

_ext_lookup_historical_land_use_by_region.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "TIME_LAND_USE",
    "HISTORICAL_SNOW_ICE_WATERBODIES_BY_REGION",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": ["SNOW_ICE_WATERBODIES"],
    },
)

_ext_lookup_historical_land_use_by_region.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "TIME_LAND_USE",
    "HISTORICAL_OTHER_LAND_BY_REGION",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"], "LANDS_I": ["OTHER_LAND"]},
)


@component.add(
    name="HISTORICAL_LAND_USE_CHANGE_BY_REGION",
    units="km2/Year",
    subscripts=["REGIONS_9_I", "LANDS_I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_historical_land_use_change_by_region",
        "__lookup__": "_ext_lookup_historical_land_use_change_by_region",
    },
)
def historical_land_use_change_by_region(x, final_subs=None):
    return _ext_lookup_historical_land_use_change_by_region(x, final_subs)


_ext_lookup_historical_land_use_change_by_region = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "TIME_LAND_USE",
    "HISTORICAL_CROPLAND_RAINFED_VARIATION_BY_REGION",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"], "LANDS_I": ["CROPLAND_RAINFED"]},
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": _subscript_dict["LANDS_I"],
    },
    "_ext_lookup_historical_land_use_change_by_region",
)

_ext_lookup_historical_land_use_change_by_region.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "TIME_LAND_USE",
    "HISTORICAL_CROPLAND_IRRIGATED_VARIATION_BY_REGION",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"], "LANDS_I": ["CROPLAND_IRRIGATED"]},
)

_ext_lookup_historical_land_use_change_by_region.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "TIME_LAND_USE",
    "HISTORICAL_FOREST_MANAGED_VARIATION_BY_REGION",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"], "LANDS_I": ["FOREST_MANAGED"]},
)

_ext_lookup_historical_land_use_change_by_region.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "TIME_LAND_USE",
    "HISTORICAL_FOREST_PRIMARY_VARIATION_BY_REGION",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"], "LANDS_I": ["FOREST_PRIMARY"]},
)

_ext_lookup_historical_land_use_change_by_region.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "TIME_LAND_USE",
    "HISTORICAL_FOREST_PLANTATIONS_VARIATION_BY_REGION",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"], "LANDS_I": ["FOREST_PLANTATIONS"]},
)

_ext_lookup_historical_land_use_change_by_region.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "TIME_LAND_USE",
    "HISTORICAL_SHRUBLAND_VARIATION_BY_REGION",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"], "LANDS_I": ["SHRUBLAND"]},
)

_ext_lookup_historical_land_use_change_by_region.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "TIME_LAND_USE",
    "HISTORICAL_GRASSLAND_VARIATION_BY_REGION",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"], "LANDS_I": ["GRASSLAND"]},
)

_ext_lookup_historical_land_use_change_by_region.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "TIME_LAND_USE",
    "HISTORICAL_WETLAND_VARIATION_BY_REGION",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"], "LANDS_I": ["WETLAND"]},
)

_ext_lookup_historical_land_use_change_by_region.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "TIME_LAND_USE",
    "HISTORICAL_URBAN_LAND_VARIATION_BY_REGION",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"], "LANDS_I": ["URBAN_LAND"]},
)

_ext_lookup_historical_land_use_change_by_region.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "TIME_LAND_USE",
    "HISTORICAL_SOLAR_LAND_VARIATION_BY_REGION",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"], "LANDS_I": ["SOLAR_LAND"]},
)

_ext_lookup_historical_land_use_change_by_region.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "TIME_LAND_USE",
    "HISTORICAL_SNOW_ICE_WATERBODIES_VARIATION_BY_REGION",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": ["SNOW_ICE_WATERBODIES"],
    },
)

_ext_lookup_historical_land_use_change_by_region.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "TIME_LAND_USE",
    "HISTORICAL_OTHER_LAND_VARIATION_BY_REGION",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"], "LANDS_I": ["OTHER_LAND"]},
)


@component.add(
    name="HISTORICAL_ROUNDWOOD_HARVESTED",
    units="t/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_historical_roundwood_harvested",
        "__lookup__": "_ext_lookup_historical_roundwood_harvested",
    },
)
def historical_roundwood_harvested(x, final_subs=None):
    """
    historical roundwood harvested
    """
    return _ext_lookup_historical_roundwood_harvested(x, final_subs)


_ext_lookup_historical_roundwood_harvested = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "forest",
    "ROUNDWOOD_TIME",
    "HISTORICAL_ROUNDWOOD_HARVESTED",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_lookup_historical_roundwood_harvested",
)


@component.add(
    name="HISTORICAL_SHARE_OF_LAND_USE_CHANGES_FROM_OTHERS",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LANDS_I", "LANDS_MAP_I"],
    comp_type="Constant",
    comp_subtype="External, Normal",
    depends_on={
        "__external__": "_ext_constant_historical_share_of_land_use_changes_from_others"
    },
)
def historical_share_of_land_use_changes_from_others():
    """
    SHARES (LANDS_I,LANDS_MAP_I)=demand of use LANDS_MAP_I taken from LANDS_I
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "LANDS_I": _subscript_dict["LANDS_I"],
            "LANDS_MAP_I": _subscript_dict["LANDS_MAP_I"],
        },
        ["REGIONS_9_I", "LANDS_I", "LANDS_MAP_I"],
    )
    def_subs = xr.zeros_like(value, dtype=bool)
    def_subs.loc[:, :, ["CROPLAND_RAINFED"]] = True
    def_subs.loc[:, :, ["CROPLAND_IRRIGATED"]] = True
    def_subs.loc[:, :, ["FOREST_MANAGED"]] = True
    def_subs.loc[:, :, ["FOREST_PLANTATIONS"]] = True
    def_subs.loc[:, :, ["GRASSLAND"]] = True
    def_subs.loc[:, :, ["URBAN_LAND"]] = True
    def_subs.loc[:, :, ["SOLAR_LAND"]] = True
    value.values[
        def_subs.values
    ] = _ext_constant_historical_share_of_land_use_changes_from_others().values[
        def_subs.values
    ]
    value.loc[:, :, ["FOREST_PRIMARY"]] = 0
    value.loc[:, :, ["SHRUBLAND"]] = 0
    value.loc[:, :, ["WETLAND"]] = 0
    value.loc[:, :, ["SNOW_ICE_WATERBODIES"]] = 0
    value.loc[:, :, ["OTHER_LAND"]] = 0
    return value


_ext_constant_historical_share_of_land_use_changes_from_others = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "HISTORICAL_SHARE_OF_CROPLAND_RAINFED_FROM_OTHERS_BY_REGION",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": _subscript_dict["LANDS_I"],
        "LANDS_MAP_I": ["CROPLAND_RAINFED"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": _subscript_dict["LANDS_I"],
        "LANDS_MAP_I": _subscript_dict["LANDS_MAP_I"],
    },
    "_ext_constant_historical_share_of_land_use_changes_from_others",
)

_ext_constant_historical_share_of_land_use_changes_from_others.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "INITIAL_SHARE_OF_CROPLAND_IRRIGATED_FROM_OTHERS_BY_REGION",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": _subscript_dict["LANDS_I"],
        "LANDS_MAP_I": ["CROPLAND_IRRIGATED"],
    },
)

_ext_constant_historical_share_of_land_use_changes_from_others.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "INITIAL_SHARE_OF_AFFORESTATION_FROM_OTHERS_BY_REGION",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": _subscript_dict["LANDS_I"],
        "LANDS_MAP_I": ["FOREST_MANAGED"],
    },
)

_ext_constant_historical_share_of_land_use_changes_from_others.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "INITIAL_SHARE_OF_FOREST_PLANTATIONS_FROM_OTHERS_BY_REGION",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": _subscript_dict["LANDS_I"],
        "LANDS_MAP_I": ["FOREST_PLANTATIONS"],
    },
)

_ext_constant_historical_share_of_land_use_changes_from_others.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "HISTORICAL_SHARE_OF_GRASSLAND_FROM_OTHERS_BY_REGION",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": _subscript_dict["LANDS_I"],
        "LANDS_MAP_I": ["GRASSLAND"],
    },
)

_ext_constant_historical_share_of_land_use_changes_from_others.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "INITIAL_SHARE_OF_URBAN_LAND_FROM_OTHERS_BY_REGION",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": _subscript_dict["LANDS_I"],
        "LANDS_MAP_I": ["URBAN_LAND"],
    },
)

_ext_constant_historical_share_of_land_use_changes_from_others.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "INITIAL_SHARE_OF_SOLAR_LAND_FROM_OTHERS_BY_REGION",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": _subscript_dict["LANDS_I"],
        "LANDS_MAP_I": ["SOLAR_LAND"],
    },
)


@component.add(
    name="HISTORICAL_SHARES_OF_CROPS_ALL_MANAGEMENT",
    units="DMNL",
    subscripts=["LAND_PRODUCTS_I", "REGIONS_9_I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_historical_shares_of_crops_all_management",
        "__lookup__": "_ext_lookup_historical_shares_of_crops_all_management",
    },
)
def historical_shares_of_crops_all_management(x, final_subs=None):
    """
    FAO data only per region mixing irrigated and rainfed
    """
    return _ext_lookup_historical_shares_of_crops_all_management(x, final_subs)


_ext_lookup_historical_shares_of_crops_all_management = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_SHARES_ALL_MANAGEMENT_EU27",
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"], "REGIONS_9_I": ["EU27"]},
    _root,
    {
        "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
    },
    "_ext_lookup_historical_shares_of_crops_all_management",
)

_ext_lookup_historical_shares_of_crops_all_management.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_SHARES_ALL_MANAGEMENT_UK",
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"], "REGIONS_9_I": ["UK"]},
)

_ext_lookup_historical_shares_of_crops_all_management.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_SHARES_ALL_MANAGEMENT_CHINA",
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"], "REGIONS_9_I": ["CHINA"]},
)

_ext_lookup_historical_shares_of_crops_all_management.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_SHARES_ALL_MANAGEMENT_EASOC",
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"], "REGIONS_9_I": ["EASOC"]},
)

_ext_lookup_historical_shares_of_crops_all_management.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_SHARES_ALL_MANAGEMENT_INDIA",
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"], "REGIONS_9_I": ["INDIA"]},
)

_ext_lookup_historical_shares_of_crops_all_management.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_SHARES_ALL_MANAGEMENT_LATAM",
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"], "REGIONS_9_I": ["LATAM"]},
)

_ext_lookup_historical_shares_of_crops_all_management.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_SHARES_ALL_MANAGEMENT_RUSSIA",
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"], "REGIONS_9_I": ["RUSSIA"]},
)

_ext_lookup_historical_shares_of_crops_all_management.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_SHARES_ALL_MANAGEMENT_USMCA",
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"], "REGIONS_9_I": ["USMCA"]},
)

_ext_lookup_historical_shares_of_crops_all_management.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_SHARES_ALL_MANAGEMENT_LROW",
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"], "REGIONS_9_I": ["LROW"]},
)


@component.add(
    name="HISTORICAL_SHARES_OF_RAINFED_CROPS_EU",
    subscripts=["LAND_PRODUCTS_I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_historical_shares_of_rainfed_crops_eu",
        "__lookup__": "_ext_lookup_historical_shares_of_rainfed_crops_eu",
    },
)
def historical_shares_of_rainfed_crops_eu(x, final_subs=None):
    """
    GET_DIRECT_LOOKUPS('model_parameters/land_and_water/land_and_water_parameters.xlsx', 'croplands' , 'TIME_CROPLANDS', 'HISTORICAL_VARIATION_OF_RAINFED_CROP_SHARES_UK') GET_DIRECT_LOOKUPS('model_parameters/land_and_water/land_and_water_paramete rs.xlsx', 'croplands' , 'TIME_CROPLANDS', 'HISTORICAL_VARIATION_OF_RAINFED_CROP_SHARES_CHINA')
    """
    return _ext_lookup_historical_shares_of_rainfed_crops_eu(x, final_subs)


_ext_lookup_historical_shares_of_rainfed_crops_eu = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_RAINFED_CROP_SHARES_EU27",
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"]},
    _root,
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"]},
    "_ext_lookup_historical_shares_of_rainfed_crops_eu",
)


@component.add(
    name="HISTORICAL_SOLAR_LAND_BY_REGION",
    subscripts=["REGIONS_9_I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_historical_solar_land_by_region",
        "__lookup__": "_ext_lookup_historical_solar_land_by_region",
    },
)
def historical_solar_land_by_region(x, final_subs=None):
    return _ext_lookup_historical_solar_land_by_region(x, final_subs)


_ext_lookup_historical_solar_land_by_region = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "TIME_LAND_USE",
    "HISTORICAL_SOLAR_LAND_BY_REGION",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_lookup_historical_solar_land_by_region",
)


@component.add(
    name="HISTORICAL_TRENDS_OF_LAND_USE_DEMAND",
    units="km2/Year",
    subscripts=["REGIONS_9_I", "LANDS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_historical_trends_of_land_use_demand"},
)
def historical_trends_of_land_use_demand():
    """
    GET_DIRECT_CONSTANTS('model_parameters/land_and_water/land_and_water.xlsx', 'land_uses' , 'TREND_CROPLAND_RAINFED_BY_REGION') GET_DIRECT_CONSTANTS('model_parameters/land_and_water/land_and_water.xlsx', 'land_uses' , 'TREND_CROPLAND_IRRIGATED_BY_REGION' ) GET_DIRECT_CONSTANTS('model_parameters/land_and_water/land_and_water.xlsx', 'land_uses' , 'TREND_AFFORESTATION_BY_REGION' ) GET_DIRECT_CONSTANTS('model_parameters/land_and_water/land_and_water.xlsx', 'land_uses' ,'TREND_FOREST_PLANTATIONS_BY_REGION') GET_DIRECT_CONSTANTS('model_parameters/land_and_water/land_and_water.xlsx', 'land_uses' , 'TREND_GRASSLAND_BY_REGION' ) GET_DIRECT_CONSTANTS('model_parameters/land_and_water/land_and_water.xlsx', 'land_uses' , 'TREND_URBAN_LAND_BY_REGION' ) GET_DIRECT_CONSTANTS('model_parameters/land_and_water/land_and_water_parame ters.xlsx', 'land_uses' , 'TREND_SOLAR_LAND_BY_REGION' )
    """
    return _ext_constant_historical_trends_of_land_use_demand()


_ext_constant_historical_trends_of_land_use_demand = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "HISTORICAL_TRENDS_OF_LAND_USE_CHANGE_BY_REGION",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": _subscript_dict["LANDS_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": _subscript_dict["LANDS_I"],
    },
    "_ext_constant_historical_trends_of_land_use_demand",
)


@component.add(
    name="HISTORICAL_URBAN_LAND_BY_REGION",
    subscripts=["REGIONS_9_I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_historical_urban_land_by_region",
        "__lookup__": "_ext_lookup_historical_urban_land_by_region",
    },
)
def historical_urban_land_by_region(x, final_subs=None):
    return _ext_lookup_historical_urban_land_by_region(x, final_subs)


_ext_lookup_historical_urban_land_by_region = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "TIME_LAND_USE",
    "HISTORICAL_URBAN_LAND_BY_REGION",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_lookup_historical_urban_land_by_region",
)


@component.add(
    name="HISTORICAL_VARIATION_OF_SHARES_OF_IRRIGATED_CROPS",
    subscripts=["LAND_PRODUCTS_I", "REGIONS_9_I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_historical_variation_of_shares_of_irrigated_crops",
        "__lookup__": "_ext_lookup_historical_variation_of_shares_of_irrigated_crops",
    },
)
def historical_variation_of_shares_of_irrigated_crops(x, final_subs=None):
    return _ext_lookup_historical_variation_of_shares_of_irrigated_crops(x, final_subs)


_ext_lookup_historical_variation_of_shares_of_irrigated_crops = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_VARIATION_OF_IRRIGATED_CROP_SHARES_EU27",
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"], "REGIONS_9_I": ["EU27"]},
    _root,
    {
        "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
    },
    "_ext_lookup_historical_variation_of_shares_of_irrigated_crops",
)

_ext_lookup_historical_variation_of_shares_of_irrigated_crops.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_VARIATION_OF_IRRIGATED_CROP_SHARES_UK",
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"], "REGIONS_9_I": ["UK"]},
)

_ext_lookup_historical_variation_of_shares_of_irrigated_crops.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_VARIATION_OF_IRRIGATED_CROP_SHARES_CHINA",
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"], "REGIONS_9_I": ["CHINA"]},
)

_ext_lookup_historical_variation_of_shares_of_irrigated_crops.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_VARIATION_OF_IRRIGATED_CROP_SHARES_EASOC",
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"], "REGIONS_9_I": ["EASOC"]},
)

_ext_lookup_historical_variation_of_shares_of_irrigated_crops.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_VARIATION_OF_IRRIGATED_CROP_SHARES_INDIA",
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"], "REGIONS_9_I": ["INDIA"]},
)

_ext_lookup_historical_variation_of_shares_of_irrigated_crops.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_VARIATION_OF_IRRIGATED_CROP_SHARES_LATAM",
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"], "REGIONS_9_I": ["LATAM"]},
)

_ext_lookup_historical_variation_of_shares_of_irrigated_crops.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_VARIATION_OF_IRRIGATED_CROP_SHARES_RUSSIA",
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"], "REGIONS_9_I": ["RUSSIA"]},
)

_ext_lookup_historical_variation_of_shares_of_irrigated_crops.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_VARIATION_OF_IRRIGATED_CROP_SHARES_USMCA",
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"], "REGIONS_9_I": ["USMCA"]},
)

_ext_lookup_historical_variation_of_shares_of_irrigated_crops.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_VARIATION_OF_IRRIGATED_CROP_SHARES_LROW",
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"], "REGIONS_9_I": ["LROW"]},
)


@component.add(
    name="HISTORICAL_VARIATION_OF_SHARES_OF_RAINFED_CROPS",
    subscripts=["LAND_PRODUCTS_I", "REGIONS_9_I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_historical_variation_of_shares_of_rainfed_crops",
        "__lookup__": "_ext_lookup_historical_variation_of_shares_of_rainfed_crops",
    },
)
def historical_variation_of_shares_of_rainfed_crops(x, final_subs=None):
    return _ext_lookup_historical_variation_of_shares_of_rainfed_crops(x, final_subs)


_ext_lookup_historical_variation_of_shares_of_rainfed_crops = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_VARIATION_OF_RAINFED_CROP_SHARES_EU27",
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"], "REGIONS_9_I": ["EU27"]},
    _root,
    {
        "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
    },
    "_ext_lookup_historical_variation_of_shares_of_rainfed_crops",
)

_ext_lookup_historical_variation_of_shares_of_rainfed_crops.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_VARIATION_OF_RAINFED_CROP_SHARES_UK",
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"], "REGIONS_9_I": ["UK"]},
)

_ext_lookup_historical_variation_of_shares_of_rainfed_crops.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_VARIATION_OF_RAINFED_CROP_SHARES_CHINA",
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"], "REGIONS_9_I": ["CHINA"]},
)

_ext_lookup_historical_variation_of_shares_of_rainfed_crops.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_VARIATION_OF_RAINFED_CROP_SHARES_EASOC",
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"], "REGIONS_9_I": ["EASOC"]},
)

_ext_lookup_historical_variation_of_shares_of_rainfed_crops.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_VARIATION_OF_RAINFED_CROP_SHARES_INDIA",
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"], "REGIONS_9_I": ["INDIA"]},
)

_ext_lookup_historical_variation_of_shares_of_rainfed_crops.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_VARIATION_OF_RAINFED_CROP_SHARES_LATAM",
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"], "REGIONS_9_I": ["LATAM"]},
)

_ext_lookup_historical_variation_of_shares_of_rainfed_crops.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_VARIATION_OF_RAINFED_CROP_SHARES_RUSSIA",
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"], "REGIONS_9_I": ["RUSSIA"]},
)

_ext_lookup_historical_variation_of_shares_of_rainfed_crops.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_VARIATION_OF_RAINFED_CROP_SHARES_USMCA",
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"], "REGIONS_9_I": ["USMCA"]},
)

_ext_lookup_historical_variation_of_shares_of_rainfed_crops.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_VARIATION_OF_RAINFED_CROP_SHARES_LROW",
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"], "REGIONS_9_I": ["LROW"]},
)


@component.add(
    name="HISTORICAL_VOLUME_STOCK_CHANGE_FOREST_M_AND_P",
    units="m3/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_historical_volume_stock_change_forest_m_and_p",
        "__lookup__": "_ext_lookup_historical_volume_stock_change_forest_m_and_p",
    },
)
def historical_volume_stock_change_forest_m_and_p(x, final_subs=None):
    """
    historical forest volume stock change by region
    """
    return _ext_lookup_historical_volume_stock_change_forest_m_and_p(x, final_subs)


_ext_lookup_historical_volume_stock_change_forest_m_and_p = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "forest",
    "TIME_FORESTS",
    "HISTORICAL_CHANGE_OF_STOCK_MANAGED_FORESTS",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_lookup_historical_volume_stock_change_forest_m_and_p",
)


@component.add(
    name="HISTORICAL_VOLUME_STOCK_OF_FOREST_M_AND_P",
    units="m3",
    subscripts=["REGIONS_9_I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_historical_volume_stock_of_forest_m_and_p",
        "__lookup__": "_ext_lookup_historical_volume_stock_of_forest_m_and_p",
    },
)
def historical_volume_stock_of_forest_m_and_p(x, final_subs=None):
    """
    historical forest volume stock change by region
    """
    return _ext_lookup_historical_volume_stock_of_forest_m_and_p(x, final_subs)


_ext_lookup_historical_volume_stock_of_forest_m_and_p = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "forest",
    "TIME_FORESTS",
    "HISTORICAL_STOCK_OF_MANAGED_FORESTS",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_lookup_historical_volume_stock_of_forest_m_and_p",
)


@component.add(
    name="HISTORICAL_WATER_AVAILABLE_35R",
    units="hm3",
    subscripts=["REGIONS_35_I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_historical_water_available_35r",
        "__lookup__": "_ext_lookup_historical_water_available_35r",
    },
)
def historical_water_available_35r(x, final_subs=None):
    return _ext_lookup_historical_water_available_35r(x, final_subs)


_ext_lookup_historical_water_available_35r = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "water",
    "TIME_WATER",
    "HISTORICAL_WATER_AVAILABLE_35R",
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    _root,
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    "_ext_lookup_historical_water_available_35r",
)


@component.add(
    name="HISTORICAL_WATER_USE_FAO",
    units="hm3",
    subscripts=["REGIONS_35_I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_historical_water_use_fao",
        "__lookup__": "_ext_lookup_historical_water_use_fao",
    },
)
def historical_water_use_fao(x, final_subs=None):
    """
    historical WATER use from FAO accounts
    """
    return _ext_lookup_historical_water_use_fao(x, final_subs)


_ext_lookup_historical_water_use_fao = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "water",
    "TIME_WATER_USE",
    "HISTORICAL_BLUE_WATER_USE",
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    _root,
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    "_ext_lookup_historical_water_use_fao",
)


@component.add(
    name="HISTORICAL_YIELDS_FAO",
    units="t/(km2*Year)",
    subscripts=["LAND_PRODUCTS_I", "REGIONS_9_I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_historical_yields_fao",
        "__lookup__": "_ext_lookup_historical_yields_fao",
    },
)
def historical_yields_fao(x, final_subs=None):
    """
    FAO data only per region mixing irrigated and rainfed
    """
    return _ext_lookup_historical_yields_fao(x, final_subs)


_ext_lookup_historical_yields_fao = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_YIELDS_FAO_EU27",
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"], "REGIONS_9_I": ["EU27"]},
    _root,
    {
        "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
    },
    "_ext_lookup_historical_yields_fao",
)

_ext_lookup_historical_yields_fao.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_YIELDS_FAO_UK",
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"], "REGIONS_9_I": ["UK"]},
)

_ext_lookup_historical_yields_fao.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_YIELDS_FAO_CHINA",
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"], "REGIONS_9_I": ["CHINA"]},
)

_ext_lookup_historical_yields_fao.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_YIELDS_FAO_EASOC",
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"], "REGIONS_9_I": ["EASOC"]},
)

_ext_lookup_historical_yields_fao.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_YIELDS_FAO_INDIA",
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"], "REGIONS_9_I": ["INDIA"]},
)

_ext_lookup_historical_yields_fao.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_YIELDS_FAO_LATAM",
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"], "REGIONS_9_I": ["LATAM"]},
)

_ext_lookup_historical_yields_fao.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_YIELDS_FAO_RUSSIA",
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"], "REGIONS_9_I": ["RUSSIA"]},
)

_ext_lookup_historical_yields_fao.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_YIELDS_FAO_USMCA",
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"], "REGIONS_9_I": ["USMCA"]},
)

_ext_lookup_historical_yields_fao.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_YIELDS_FAO_LROW",
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"], "REGIONS_9_I": ["LROW"]},
)


@component.add(
    name="IMV_EXOGENOUS_GDPpc_9R",
    units="Mdollars_2015/(Year*person)",
    subscripts=["REGIONS_9_I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_imv_exogenous_gdppc_9r",
        "__lookup__": "_ext_lookup_imv_exogenous_gdppc_9r",
    },
)
def imv_exogenous_gdppc_9r(x, final_subs=None):
    """
    GDPpc real constant values for 9 regions
    """
    return _ext_lookup_imv_exogenous_gdppc_9r(x, final_subs)


_ext_lookup_imv_exogenous_gdppc_9r = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "exogenous_inputs",
    "TIME_GDPPC",
    "EXOGENOUS_GDPPC_CONSTANT",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_lookup_imv_exogenous_gdppc_9r",
)


@component.add(
    name="IMV_EXOGENOUS_POPULATION_VARIATION",
    units="people/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_imv_exogenous_population_variation",
        "__lookup__": "_ext_lookup_imv_exogenous_population_variation",
    },
)
def imv_exogenous_population_variation(x, final_subs=None):
    """
    to be removed when integrating with Demography module
    """
    return _ext_lookup_imv_exogenous_population_variation(x, final_subs)


_ext_lookup_imv_exogenous_population_variation = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "exogenous_inputs",
    "TIME_EXOGENOUS_POPULATION",
    "EXOGENOUS_VARIATION_OF_POPULATION_9R",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_lookup_imv_exogenous_population_variation",
)


@component.add(
    name="IMV_PE_BY_COMMODITY_AGRICULTURE_PRODUCTS_CONSTANT",
    units="EJ/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_imv_pe_by_commodity_agriculture_products_constant",
        "__lookup__": "_ext_lookup_imv_pe_by_commodity_agriculture_products_constant",
    },
)
def imv_pe_by_commodity_agriculture_products_constant(x, final_subs=None):
    """
    PE by commodity agriculture products constant values for 9 regions
    """
    return _ext_lookup_imv_pe_by_commodity_agriculture_products_constant(x, final_subs)


_ext_lookup_imv_pe_by_commodity_agriculture_products_constant = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "exogenous_inputs",
    "TIME_EXOGENOUS_POPULATION",
    "EXOGENOUS_PE_BY_COMMODITY_AGRICULTURE",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_lookup_imv_pe_by_commodity_agriculture_products_constant",
)


@component.add(
    name="IMV_PE_BY_COMMODITY_FORESTRY_PRODUCTS",
    units="EJ/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_imv_pe_by_commodity_forestry_products",
        "__lookup__": "_ext_lookup_imv_pe_by_commodity_forestry_products",
    },
)
def imv_pe_by_commodity_forestry_products(x, final_subs=None):
    """
    PE by commodity forestry products constant values for 9 regions
    """
    return _ext_lookup_imv_pe_by_commodity_forestry_products(x, final_subs)


_ext_lookup_imv_pe_by_commodity_forestry_products = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "exogenous_inputs",
    "TIME_EXOGENOUS_POPULATION",
    "EXOGENOUS_PE_BY_COMMODITY_FORESTRY",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_lookup_imv_pe_by_commodity_forestry_products",
)


@component.add(
    name="INITIAL_BLUE_WATER_REGION_HOUSEHOLDS",
    units="hm3",
    subscripts=["REGIONS_35_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_blue_water_region_households"},
)
def initial_blue_water_region_households():
    """
    Load the initial (2005) values of the Blue Water for the Households, for the 35 Regions, per capita.
    """
    return _ext_constant_initial_blue_water_region_households()


_ext_constant_initial_blue_water_region_households = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Water",
    "Blue2005h*",
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    _root,
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    "_ext_constant_initial_blue_water_region_households",
)


@component.add(
    name="INITIAL_CO2_CONCENTRATION",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_co2_concentration"},
)
def initial_co2_concentration():
    return _ext_constant_initial_co2_concentration()


_ext_constant_initial_co2_concentration = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "INITIAL_CO2_CONCENTRATION",
    {},
    _root,
    {},
    "_ext_constant_initial_co2_concentration",
)


@component.add(
    name="INITIAL_DAIRY_OBTAINED_FROM_GRASSLANDS",
    units="t/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_dairy_obtained_from_grasslands"},
)
def initial_dairy_obtained_from_grasslands():
    """
    dairy quantity produced by grasslands
    """
    return _ext_constant_initial_dairy_obtained_from_grasslands()


_ext_constant_initial_dairy_obtained_from_grasslands = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Diet",
    "DAIRY_GRASSLANDS*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_initial_dairy_obtained_from_grasslands",
)


@component.add(
    name="INITIAL_FOREST_ABOVE_GROUND_BIOMASS_STOCK",
    units="t",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_initial_forest_above_ground_biomass_stock"
    },
)
def initial_forest_above_ground_biomass_stock():
    """
    Initial forest above ground biomass stock
    """
    return _ext_constant_initial_forest_above_ground_biomass_stock()


_ext_constant_initial_forest_above_ground_biomass_stock = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "forest",
    "INITIAL_FOREST_ABOVE_GROUND_BIOMASS_STOCK*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_initial_forest_above_ground_biomass_stock",
)


@component.add(
    name="INITIAL_FOREST_BELOW_GROUND_BIOMASS_STOCK",
    units="t",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_initial_forest_below_ground_biomass_stock"
    },
)
def initial_forest_below_ground_biomass_stock():
    """
    initial forest below ground biomass stock
    """
    return _ext_constant_initial_forest_below_ground_biomass_stock()


_ext_constant_initial_forest_below_ground_biomass_stock = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "forest",
    "INITIAL_FOREST_BELOW_GROUND_BIOMASS_STOCK*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_initial_forest_below_ground_biomass_stock",
)


@component.add(
    name="INITIAL_FOREST_CARBON_IN_ABOVE_GROUND_BIOMASS_STOCK",
    units="t",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_initial_forest_carbon_in_above_ground_biomass_stock"
    },
)
def initial_forest_carbon_in_above_ground_biomass_stock():
    """
    Initial forest carbon in above ground biomass stock
    """
    return _ext_constant_initial_forest_carbon_in_above_ground_biomass_stock()


_ext_constant_initial_forest_carbon_in_above_ground_biomass_stock = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "forest",
    "INITIAL_FOREST_CARBON_IN_ABOVE_GROUND_BIOMASS_STOCK*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_initial_forest_carbon_in_above_ground_biomass_stock",
)


@component.add(
    name="INITIAL_FOREST_CARBON_IN_BELOW_GROUND_BIOMASS_STOCK",
    units="t",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_initial_forest_carbon_in_below_ground_biomass_stock"
    },
)
def initial_forest_carbon_in_below_ground_biomass_stock():
    """
    initial forest carbon in below ground biomass stock
    """
    return _ext_constant_initial_forest_carbon_in_below_ground_biomass_stock()


_ext_constant_initial_forest_carbon_in_below_ground_biomass_stock = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "forest",
    "INITIAL_FOREST_CARBON_IN_BELOW_GROUND_BIOMASS_STOCK*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_initial_forest_carbon_in_below_ground_biomass_stock",
)


@component.add(
    name="INITIAL_GREEN_WATER_REGION_SECT",
    units="hm3",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_green_water_region_sect"},
)
def initial_green_water_region_sect():
    """
    Load the initial (2005) values of the Green Water, for the 35 Regions and 62 Sectors.
    """
    return _ext_constant_initial_green_water_region_sect()


_ext_constant_initial_green_water_region_sect = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Water",
    "Green2005",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
    "_ext_constant_initial_green_water_region_sect",
)


@component.add(
    name="INITIAL_LAND_USE_BY_REGION",
    units="km2",
    subscripts=["REGIONS_9_I", "LANDS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_land_use_by_region"},
)
def initial_land_use_by_region():
    return _ext_constant_initial_land_use_by_region()


_ext_constant_initial_land_use_by_region = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "INITIAL_LAND_BY_REGION_2005*",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": _subscript_dict["LANDS_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": _subscript_dict["LANDS_I"],
    },
    "_ext_constant_initial_land_use_by_region",
)


@component.add(
    name="INITIAL_LAND_USE_BY_REGION_2015",
    units="km2",
    subscripts=["REGIONS_9_I", "LANDS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_land_use_by_region_2015"},
)
def initial_land_use_by_region_2015():
    return _ext_constant_initial_land_use_by_region_2015()


_ext_constant_initial_land_use_by_region_2015 = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "INITIAL_LAND_BY_REGION_2015*",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": _subscript_dict["LANDS_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": _subscript_dict["LANDS_I"],
    },
    "_ext_constant_initial_land_use_by_region_2015",
)


@component.add(
    name="INITIAL_MEAT_OBTAINED_FROM_GRASSLANDS",
    units="t/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_meat_obtained_from_grasslands"},
)
def initial_meat_obtained_from_grasslands():
    """
    meat quantity produced by grasslands
    """
    return _ext_constant_initial_meat_obtained_from_grasslands()


_ext_constant_initial_meat_obtained_from_grasslands = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Diet",
    "MEAT_GRASSLANDS*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_initial_meat_obtained_from_grasslands",
)


@component.add(
    name="INITIAL_PRECIPITATION_EVAPOTRANSPIRATION_BY_REGION",
    units="DMNL",
    subscripts=["REGIONS_35_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_initial_precipitation_evapotranspiration_by_region"
    },
)
def initial_precipitation_evapotranspiration_by_region():
    """
    GET_DIRECT_CONSTANTS( 'water', 'WaPPET' , 'B2' ) initial water availability from FAO
    """
    return _ext_constant_initial_precipitation_evapotranspiration_by_region()


_ext_constant_initial_precipitation_evapotranspiration_by_region = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Water",
    "PE_presente*",
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    _root,
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    "_ext_constant_initial_precipitation_evapotranspiration_by_region",
)


@component.add(
    name="INITIAL_SHARE_OF_IRRIGATION",
    subscripts=["LAND_PRODUCTS_I", "REGIONS_9_I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_initial_share_of_irrigation",
        "__lookup__": "_ext_lookup_initial_share_of_irrigation",
    },
)
def initial_share_of_irrigation(x, final_subs=None):
    return _ext_lookup_initial_share_of_irrigation(x, final_subs)


_ext_lookup_initial_share_of_irrigation = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "SHARE_OF_IRRIGATION_EU27",
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"], "REGIONS_9_I": ["EU27"]},
    _root,
    {
        "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
    },
    "_ext_lookup_initial_share_of_irrigation",
)

_ext_lookup_initial_share_of_irrigation.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "SHARE_OF_IRRIGATION_UK",
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"], "REGIONS_9_I": ["UK"]},
)

_ext_lookup_initial_share_of_irrigation.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "SHARE_OF_IRRIGATION_CHINA",
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"], "REGIONS_9_I": ["CHINA"]},
)

_ext_lookup_initial_share_of_irrigation.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "SHARE_OF_IRRIGATION_EASOC",
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"], "REGIONS_9_I": ["EASOC"]},
)

_ext_lookup_initial_share_of_irrigation.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "SHARE_OF_IRRIGATION_INDIA",
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"], "REGIONS_9_I": ["INDIA"]},
)

_ext_lookup_initial_share_of_irrigation.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "SHARE_OF_IRRIGATION_LATAM",
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"], "REGIONS_9_I": ["LATAM"]},
)

_ext_lookup_initial_share_of_irrigation.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "SHARE_OF_IRRIGATION_RUSSIA",
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"], "REGIONS_9_I": ["RUSSIA"]},
)

_ext_lookup_initial_share_of_irrigation.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "SHARE_OF_IRRIGATION_USMCA",
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"], "REGIONS_9_I": ["USMCA"]},
)

_ext_lookup_initial_share_of_irrigation.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "SHARE_OF_IRRIGATION_LROW",
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"], "REGIONS_9_I": ["LROW"]},
)


@component.add(
    name="INITIAL_SHARE_OF_LAND_USE_CHANGES_FROM_OTHERS_DOWN",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LANDS_I", "LANDS_MAP_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="External, Normal",
    depends_on={
        "__external__": "_ext_constant_initial_share_of_land_use_changes_from_others_down",
        "initial_share_of_land_use_changes_from_others_up": 8,
    },
)
def initial_share_of_land_use_changes_from_others_down():
    """
    SHARES (LANDS_I,LANDS_MAP_I)=demand of use LANDS_MAP_I taken from LANDS_I now is set equal to the shares when the demands go up, EXCEPT FOR FOREST AND CROPLAND IRRIGATED
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "LANDS_I": _subscript_dict["LANDS_I"],
            "LANDS_MAP_I": _subscript_dict["LANDS_MAP_I"],
        },
        ["REGIONS_9_I", "LANDS_I", "LANDS_MAP_I"],
    )
    def_subs = xr.zeros_like(value, dtype=bool)
    def_subs.loc[:, :, ["CROPLAND_RAINFED"]] = True
    def_subs.loc[:, :, ["FOREST_MANAGED"]] = True
    def_subs.loc[:, :, ["FOREST_PRIMARY"]] = True
    def_subs.loc[:, :, ["SOLAR_LAND"]] = True
    value.values[
        def_subs.values
    ] = _ext_constant_initial_share_of_land_use_changes_from_others_down().values[
        def_subs.values
    ]
    value.loc[:, :, ["CROPLAND_IRRIGATED"]] = (
        initial_share_of_land_use_changes_from_others_up()
        .loc[:, :, "CROPLAND_IRRIGATED"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS_MAP_I": ["CROPLAND_IRRIGATED"]}, 2)
        .values
    )
    value.loc[:, :, ["FOREST_PLANTATIONS"]] = (
        initial_share_of_land_use_changes_from_others_up()
        .loc[:, :, "FOREST_PLANTATIONS"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS_FOREST_I": ["FOREST_PLANTATIONS"]}, 2)
        .values
    )
    value.loc[:, :, ["SHRUBLAND"]] = (
        initial_share_of_land_use_changes_from_others_up()
        .loc[:, :, "SHRUBLAND"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS_MAP_I": ["SHRUBLAND"]}, 2)
        .values
    )
    value.loc[:, :, ["GRASSLAND"]] = (
        initial_share_of_land_use_changes_from_others_up()
        .loc[:, :, "GRASSLAND"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS_MAP_I": ["GRASSLAND"]}, 2)
        .values
    )
    value.loc[:, :, ["WETLAND"]] = (
        initial_share_of_land_use_changes_from_others_up()
        .loc[:, :, "WETLAND"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS_MAP_I": ["WETLAND"]}, 2)
        .values
    )
    value.loc[:, :, ["URBAN_LAND"]] = (
        initial_share_of_land_use_changes_from_others_up()
        .loc[:, :, "URBAN_LAND"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS_MAP_I": ["URBAN_LAND"]}, 2)
        .values
    )
    value.loc[:, :, ["SNOW_ICE_WATERBODIES"]] = (
        initial_share_of_land_use_changes_from_others_up()
        .loc[:, :, "SNOW_ICE_WATERBODIES"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS_MAP_I": ["SNOW_ICE_WATERBODIES"]}, 2)
        .values
    )
    value.loc[:, :, ["OTHER_LAND"]] = (
        initial_share_of_land_use_changes_from_others_up()
        .loc[:, :, "OTHER_LAND"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS_MAP_I": ["OTHER_LAND"]}, 2)
        .values
    )
    return value


_ext_constant_initial_share_of_land_use_changes_from_others_down = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "INITIAL_SHARE_OF_CROPLAND_RAINFED_FROM_OTHERS_DOWN",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": _subscript_dict["LANDS_I"],
        "LANDS_MAP_I": ["CROPLAND_RAINFED"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": _subscript_dict["LANDS_I"],
        "LANDS_MAP_I": _subscript_dict["LANDS_MAP_I"],
    },
    "_ext_constant_initial_share_of_land_use_changes_from_others_down",
)

_ext_constant_initial_share_of_land_use_changes_from_others_down.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "INITIAL_SHARE_OF_AFFORESTATION_FROM_OTHERS_DOWN",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": _subscript_dict["LANDS_I"],
        "LANDS_MAP_I": ["FOREST_MANAGED"],
    },
)

_ext_constant_initial_share_of_land_use_changes_from_others_down.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "INITIAL_SHARE_OF_AFFORESTATION_FROM_OTHERS_DOWN",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": _subscript_dict["LANDS_I"],
        "LANDS_MAP_I": ["FOREST_PRIMARY"],
    },
)

_ext_constant_initial_share_of_land_use_changes_from_others_down.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "INITIAL_SHARE_OF_SOLAR_LAND_FROM_OTHERS_DOWN",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": _subscript_dict["LANDS_I"],
        "LANDS_MAP_I": ["SOLAR_LAND"],
    },
)


@component.add(
    name="INITIAL_SHARE_OF_LAND_USE_CHANGES_FROM_OTHERS_UP",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LANDS_I", "LANDS_MAP_I"],
    comp_type="Constant",
    comp_subtype="External, Normal",
    depends_on={
        "__external__": "_ext_constant_initial_share_of_land_use_changes_from_others_up"
    },
)
def initial_share_of_land_use_changes_from_others_up():
    """
    SHARES (LANDS_I,LANDS_MAP_I)=demand of use LANDS_MAP_I taken from LANDS_I
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "LANDS_I": _subscript_dict["LANDS_I"],
            "LANDS_MAP_I": _subscript_dict["LANDS_MAP_I"],
        },
        ["REGIONS_9_I", "LANDS_I", "LANDS_MAP_I"],
    )
    def_subs = xr.zeros_like(value, dtype=bool)
    def_subs.loc[:, :, ["CROPLAND_RAINFED"]] = True
    def_subs.loc[:, :, ["CROPLAND_IRRIGATED"]] = True
    def_subs.loc[:, :, ["FOREST_MANAGED"]] = True
    def_subs.loc[:, :, ["FOREST_PLANTATIONS"]] = True
    def_subs.loc[:, :, ["GRASSLAND"]] = True
    def_subs.loc[:, :, ["URBAN_LAND"]] = True
    def_subs.loc[:, :, ["SOLAR_LAND"]] = True
    value.values[
        def_subs.values
    ] = _ext_constant_initial_share_of_land_use_changes_from_others_up().values[
        def_subs.values
    ]
    value.loc[:, :, ["FOREST_PRIMARY"]] = 0
    value.loc[:, :, ["SHRUBLAND"]] = 0
    value.loc[:, :, ["WETLAND"]] = 0
    value.loc[:, :, ["SNOW_ICE_WATERBODIES"]] = 0
    value.loc[:, :, ["OTHER_LAND"]] = 0
    return value


_ext_constant_initial_share_of_land_use_changes_from_others_up = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "INITIAL_SHARE_OF_CROPLAND_RAINFED_FROM_OTHERS_BY_REGION",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": _subscript_dict["LANDS_I"],
        "LANDS_MAP_I": ["CROPLAND_RAINFED"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": _subscript_dict["LANDS_I"],
        "LANDS_MAP_I": _subscript_dict["LANDS_MAP_I"],
    },
    "_ext_constant_initial_share_of_land_use_changes_from_others_up",
)

_ext_constant_initial_share_of_land_use_changes_from_others_up.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "INITIAL_SHARE_OF_CROPLAND_IRRIGATED_FROM_OTHERS_BY_REGION",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": _subscript_dict["LANDS_I"],
        "LANDS_MAP_I": ["CROPLAND_IRRIGATED"],
    },
)

_ext_constant_initial_share_of_land_use_changes_from_others_up.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "INITIAL_SHARE_OF_AFFORESTATION_FROM_OTHERS_BY_REGION",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": _subscript_dict["LANDS_I"],
        "LANDS_MAP_I": ["FOREST_MANAGED"],
    },
)

_ext_constant_initial_share_of_land_use_changes_from_others_up.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "INITIAL_SHARE_OF_FOREST_PLANTATIONS_FROM_OTHERS_BY_REGION",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": _subscript_dict["LANDS_I"],
        "LANDS_MAP_I": ["FOREST_PLANTATIONS"],
    },
)

_ext_constant_initial_share_of_land_use_changes_from_others_up.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "INITIAL_SHARE_OF_GRASSLAND_FROM_OTHERS_BY_REGION",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": _subscript_dict["LANDS_I"],
        "LANDS_MAP_I": ["GRASSLAND"],
    },
)

_ext_constant_initial_share_of_land_use_changes_from_others_up.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "INITIAL_SHARE_OF_URBAN_LAND_FROM_OTHERS_BY_REGION",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": _subscript_dict["LANDS_I"],
        "LANDS_MAP_I": ["URBAN_LAND"],
    },
)

_ext_constant_initial_share_of_land_use_changes_from_others_up.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "INITIAL_SHARE_OF_SOLAR_LAND_FROM_OTHERS_BY_REGION",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": _subscript_dict["LANDS_I"],
        "LANDS_MAP_I": ["SOLAR_LAND"],
    },
)


@component.add(
    name="INITIAL_SHARE_OF_LOW_INPUT_AGRICULTURE",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def initial_share_of_low_input_agriculture():
    return xr.DataArray(
        0,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
        },
        ["REGIONS_9_I", "LAND_PRODUCTS_I"],
    )


@component.add(
    name="INITIAL_SHARE_OF_PRODUCTION_FROM_SMALLHOLDERS",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_initial_share_of_production_from_smallholders"
    },
)
def initial_share_of_production_from_smallholders():
    """
    INICIAL PERCENTAGES OF FOOD PRODUCTION FROM SMALLHOLDERS
    """
    return _ext_constant_initial_share_of_production_from_smallholders()


_ext_constant_initial_share_of_production_from_smallholders = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "intermodule_global_allocate",
    "INITIAL_PERCENTAGES_OF_PRODUCTION_SMALLHOLDERS*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_initial_share_of_production_from_smallholders",
)


@component.add(
    name="INITIAL_SHARE_OF_REGENERATIVE_AGRICULTURE",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_initial_share_of_regenerative_agriculture"
    },
)
def initial_share_of_regenerative_agriculture():
    """
    INITIAL_SHARE_OF_REGENERATIVE_AGRICULTURE
    """
    return _ext_constant_initial_share_of_regenerative_agriculture()


_ext_constant_initial_share_of_regenerative_agriculture = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "INITIAL_SHARE_OF_REGENERATIVE_AGRICULTURE",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
    },
    "_ext_constant_initial_share_of_regenerative_agriculture",
)


@component.add(
    name="INITIAL_SHARE_OF_TRADITIONAL_AGRICULTURE",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_initial_share_of_traditional_agriculture"
    },
)
def initial_share_of_traditional_agriculture():
    return _ext_constant_initial_share_of_traditional_agriculture()


_ext_constant_initial_share_of_traditional_agriculture = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "INITIAL_SHARE_OF_TRADITIONAL_AGRICULTURE",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
    },
    "_ext_constant_initial_share_of_traditional_agriculture",
)


@component.add(
    name="INITIAL_SHARE_OF_URBAN_AND_SOLAR_FROM_OTHER_LANDS_BY_REGION",
    units="DMNL",
    subscripts=["REGIONS_36_I", "LANDS_I", "LANDS_MAP_I"],
    comp_type="Constant",
    comp_subtype="External, Normal",
    depends_on={
        "__external__": "_ext_constant_initial_share_of_urban_and_solar_from_other_lands_by_region"
    },
)
def initial_share_of_urban_and_solar_from_other_lands_by_region():
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_36_I": _subscript_dict["REGIONS_36_I"],
            "LANDS_I": _subscript_dict["LANDS_I"],
            "LANDS_MAP_I": _subscript_dict["LANDS_MAP_I"],
        },
        ["REGIONS_36_I", "LANDS_I", "LANDS_MAP_I"],
    )
    def_subs = xr.zeros_like(value, dtype=bool)
    def_subs.loc[
        ["EU27", "UK", "CHINA", "EASOC", "INDIA", "LATAM", "RUSSIA", "USMCA", "LROW"],
        :,
        ["URBAN_LAND"],
    ] = True
    def_subs.loc[
        ["EU27", "UK", "CHINA", "EASOC", "INDIA", "LATAM", "RUSSIA", "USMCA", "LROW"],
        :,
        ["SOLAR_LAND"],
    ] = True
    value.values[
        def_subs.values
    ] = _ext_constant_initial_share_of_urban_and_solar_from_other_lands_by_region().values[
        def_subs.values
    ]
    value.loc[_subscript_dict["REGIONS_9_I"], :, ["CROPLAND_RAINFED"]] = 1
    value.loc[_subscript_dict["REGIONS_9_I"], :, ["CROPLAND_IRRIGATED"]] = 1
    value.loc[_subscript_dict["REGIONS_9_I"], :, ["FOREST_MANAGED"]] = 1
    value.loc[_subscript_dict["REGIONS_9_I"], :, ["FOREST_PRIMARY"]] = 1
    value.loc[_subscript_dict["REGIONS_9_I"], :, ["FOREST_PLANTATIONS"]] = 1
    value.loc[_subscript_dict["REGIONS_9_I"], :, ["SHRUBLAND"]] = 1
    value.loc[_subscript_dict["REGIONS_9_I"], :, ["WETLAND"]] = 1
    value.loc[_subscript_dict["REGIONS_9_I"], :, ["SNOW_ICE_WATERBODIES"]] = 1
    value.loc[_subscript_dict["REGIONS_9_I"], :, ["OTHER_LAND"]] = 1
    value.loc[:, :, ["GRASSLAND"]] = 1
    return value


_ext_constant_initial_share_of_urban_and_solar_from_other_lands_by_region = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "INITIAL_SHARE_OF_URBAN_LAND_FROM_OTHERS_BY_REGION",
    {
        "REGIONS_36_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": _subscript_dict["LANDS_I"],
        "LANDS_MAP_I": ["URBAN_LAND"],
    },
    _root,
    {
        "REGIONS_36_I": _subscript_dict["REGIONS_36_I"],
        "LANDS_I": _subscript_dict["LANDS_I"],
        "LANDS_MAP_I": _subscript_dict["LANDS_MAP_I"],
    },
    "_ext_constant_initial_share_of_urban_and_solar_from_other_lands_by_region",
)

_ext_constant_initial_share_of_urban_and_solar_from_other_lands_by_region.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "INITIAL_SHARE_OF_SOLAR_LAND_FROM_OTHERS_BY_REGION",
    {
        "REGIONS_36_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": _subscript_dict["LANDS_I"],
        "LANDS_MAP_I": ["SOLAR_LAND"],
    },
)


@component.add(
    name="INITIAL_SHARES_OF_CROPS_ALL_MANAGEMENTS",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_initial_shares_of_crops_all_managements"
    },
)
def initial_shares_of_crops_all_managements():
    return _ext_constant_initial_shares_of_crops_all_managements()


_ext_constant_initial_shares_of_crops_all_managements = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "INITIAL_SHARES_OF_CROPS",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
    },
    "_ext_constant_initial_shares_of_crops_all_managements",
)


@component.add(
    name="INITIAL_SHARES_OF_IRRIGATED_CROPS",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_shares_of_irrigated_crops"},
)
def initial_shares_of_irrigated_crops():
    return _ext_constant_initial_shares_of_irrigated_crops()


_ext_constant_initial_shares_of_irrigated_crops = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "INITIAL_SHARES_OF_IRRIGATED_CROPS",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
    },
    "_ext_constant_initial_shares_of_irrigated_crops",
)


@component.add(
    name="INITIAL_SHARES_OF_RAINFED_CROPS",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_shares_of_rainfed_crops"},
)
def initial_shares_of_rainfed_crops():
    return _ext_constant_initial_shares_of_rainfed_crops()


_ext_constant_initial_shares_of_rainfed_crops = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "INITIAL_SHARES_OF_RAINFED_CROPS",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
    },
    "_ext_constant_initial_shares_of_rainfed_crops",
)


@component.add(
    name="INITIAL_TEMPERATURE_BY_REGION_AND_CLIMATE",
    subscripts=["REGIONS_9_I", "CLIMATIC_ZONES_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_initial_temperature_by_region_and_climate"
    },
)
def initial_temperature_by_region_and_climate():
    return _ext_constant_initial_temperature_by_region_and_climate()


_ext_constant_initial_temperature_by_region_and_climate = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "INITIAL_TEMPERATURE_BY_REGION_AND_CLIMATE",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "CLIMATIC_ZONES_I": _subscript_dict["CLIMATIC_ZONES_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "CLIMATIC_ZONES_I": _subscript_dict["CLIMATIC_ZONES_I"],
    },
    "_ext_constant_initial_temperature_by_region_and_climate",
)


@component.add(
    name="INITIAL_TOTAL_RENEWABLE_WATER_BY_REGION",
    units="km3",
    subscripts=["REGIONS_35_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_initial_total_renewable_water_by_region"
    },
)
def initial_total_renewable_water_by_region():
    """
    GET_DIRECT_CONSTANTS('water','WaPPET' , 'C2' )
    """
    return _ext_constant_initial_total_renewable_water_by_region()


_ext_constant_initial_total_renewable_water_by_region = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Water",
    "dams*",
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    _root,
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    "_ext_constant_initial_total_renewable_water_by_region",
)


@component.add(
    name="INITIAL_VALUE_OF_LAND_PRODUCTS_DEMANDED_FOR_FOOD",
    units="t/Year",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_initial_value_of_land_products_demanded_for_food"
    },
)
def initial_value_of_land_products_demanded_for_food():
    """
    INITIAL DELAY FOR LAND PRODUCTS DEMANDED FOR FOOD
    """
    return _ext_constant_initial_value_of_land_products_demanded_for_food()


_ext_constant_initial_value_of_land_products_demanded_for_food = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Diet",
    "INITIAL_DELAY",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
    },
    "_ext_constant_initial_value_of_land_products_demanded_for_food",
)


@component.add(
    name="INITIAL_VOLUME_STOCK_OF_FOREST_M_AND_P",
    units="m3",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_volume_stock_of_forest_m_and_p"},
)
def initial_volume_stock_of_forest_m_and_p():
    """
    INITIAL_VALUE_OF_MANAGED_STOCK
    """
    return _ext_constant_initial_volume_stock_of_forest_m_and_p()


_ext_constant_initial_volume_stock_of_forest_m_and_p = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "forest",
    "INITIAL_VALUE_OF_MANAGED_STOCK*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_initial_volume_stock_of_forest_m_and_p",
)


@component.add(
    name="INITIAL_WATER_EFFICIENCY",
    subscripts=["REGIONS_35_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_water_efficiency"},
)
def initial_water_efficiency():
    return _ext_constant_initial_water_efficiency()


_ext_constant_initial_water_efficiency = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Water",
    "INITIAL_WATER_EFFICIENCY*",
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    _root,
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    "_ext_constant_initial_water_efficiency",
)


@component.add(
    name="INITIAL_YIELDS_ALL_MANAGEMENTS",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_yields_all_managements"},
)
def initial_yields_all_managements():
    return _ext_constant_initial_yields_all_managements()


_ext_constant_initial_yields_all_managements = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "INITIAL_YIELDS_ALL_MANAGEMENTS",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
    },
    "_ext_constant_initial_yields_all_managements",
)


@component.add(
    name="INTENSITIES_OF_RESIDUES_FOR_INDUSTRY",
    units="t/Mdollars_2015",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_intensities_of_residues_for_industry"},
)
def intensities_of_residues_for_industry():
    """
    Calculated intensities for residues wood demanded for industry
    """
    return _ext_constant_intensities_of_residues_for_industry()


_ext_constant_intensities_of_residues_for_industry = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Diet",
    "INTENSITIES_OF_RESIDUES_FOR_INDUSTRY*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_intensities_of_residues_for_industry",
)


@component.add(
    name="INTENSITIES_OF_WOOD_FOR_INDUSTRY",
    units="t/Mdollars_2015",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_intensities_of_wood_for_industry"},
)
def intensities_of_wood_for_industry():
    """
    Calculated intensities for wood demanded for industry
    """
    return _ext_constant_intensities_of_wood_for_industry()


_ext_constant_intensities_of_wood_for_industry = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Diet",
    "INTENSITIES_OF_WOOD_FOR_INDUSTRY*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_intensities_of_wood_for_industry",
)


@component.add(
    name="KI_SOLAR_FEEDBACK", units="DMNL", comp_type="Constant", comp_subtype="Normal"
)
def ki_solar_feedback():
    return 0.03


@component.add(
    name="KP_SOLAR_FEEDBACK", units="DMNL", comp_type="Constant", comp_subtype="Normal"
)
def kp_solar_feedback():
    return 2


@component.add(
    name="LAND_AREA_ADJUST_COEFFICIENT",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_land_area_adjust_coefficient"},
)
def land_area_adjust_coefficient():
    return _ext_constant_land_area_adjust_coefficient()


_ext_constant_land_area_adjust_coefficient = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "LAND_AREA_ADJUST_COEFFICIENT*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_land_area_adjust_coefficient",
)


@component.add(
    name="LAND_PRODUCTS_HISTORICAL_CONSUMPTION",
    units="t/Year",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Data",
    comp_subtype="External, Normal",
    depends_on={
        "__external__": "_ext_data_land_products_historical_consumption",
        "__data__": "_ext_data_land_products_historical_consumption",
        "time": 1,
    },
)
def land_products_historical_consumption():
    """
    land products consumption historical, net consumption production + imports - exports
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
        },
        ["REGIONS_9_I", "LAND_PRODUCTS_I"],
    )
    def_subs = xr.zeros_like(value, dtype=bool)
    def_subs.loc[:, ["CORN"]] = True
    def_subs.loc[:, ["RICE"]] = True
    def_subs.loc[:, ["CEREALS_OTHER"]] = True
    def_subs.loc[:, ["TUBERS"]] = True
    def_subs.loc[:, ["SOY"]] = True
    def_subs.loc[:, ["PULSES_NUTS"]] = True
    def_subs.loc[:, ["OILCROPS"]] = True
    def_subs.loc[:, ["SUGAR_CROPS"]] = True
    def_subs.loc[:, ["FRUITS_VEGETABLES"]] = True
    def_subs.loc[:, ["OTHER_CROPS"]] = True
    value.values[def_subs.values] = _ext_data_land_products_historical_consumption(
        time()
    ).values[def_subs.values]
    value.loc[:, ["BIOFUEL_2GCROP"]] = 0
    value.loc[:, ["WOOD"]] = 0
    value.loc[:, ["RESIDUES"]] = 0
    return value


_ext_data_land_products_historical_consumption = ExtData(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "intermodule_global_allocate",
    "TIME_INTERMODULE",
    "HISTORICAL_CONSUMPTION_CORN",
    "interpolate",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"], "LAND_PRODUCTS_I": ["CORN"]},
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
    },
    "_ext_data_land_products_historical_consumption",
)

_ext_data_land_products_historical_consumption.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "intermodule_global_allocate",
    "TIME_INTERMODULE",
    "HISTORICAL_CONSUMPTION_RICE",
    "interpolate",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"], "LAND_PRODUCTS_I": ["RICE"]},
)

_ext_data_land_products_historical_consumption.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "intermodule_global_allocate",
    "TIME_INTERMODULE",
    "HISTORICAL_CONSUMPTION_CEREALS_OTHER",
    "interpolate",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LAND_PRODUCTS_I": ["CEREALS_OTHER"],
    },
)

_ext_data_land_products_historical_consumption.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "intermodule_global_allocate",
    "TIME_INTERMODULE",
    "HISTORICAL_CONSUMPTION_TUBERS",
    "interpolate",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"], "LAND_PRODUCTS_I": ["TUBERS"]},
)

_ext_data_land_products_historical_consumption.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "intermodule_global_allocate",
    "TIME_INTERMODULE",
    "HISTORICAL_CONSUMPTION_SOY",
    "interpolate",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"], "LAND_PRODUCTS_I": ["SOY"]},
)

_ext_data_land_products_historical_consumption.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "intermodule_global_allocate",
    "TIME_INTERMODULE",
    "HISTORICAL_CONSUMPTION_PULSES_NUTS",
    "interpolate",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"], "LAND_PRODUCTS_I": ["PULSES_NUTS"]},
)

_ext_data_land_products_historical_consumption.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "intermodule_global_allocate",
    "TIME_INTERMODULE",
    "HISTORICAL_CONSUMPTION_OILCROPS",
    "interpolate",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"], "LAND_PRODUCTS_I": ["OILCROPS"]},
)

_ext_data_land_products_historical_consumption.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "intermodule_global_allocate",
    "TIME_INTERMODULE",
    "HISTORICAL_CONSUMPTION_SUGAR_CROPS",
    "interpolate",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"], "LAND_PRODUCTS_I": ["SUGAR_CROPS"]},
)

_ext_data_land_products_historical_consumption.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "intermodule_global_allocate",
    "TIME_INTERMODULE",
    "HISTORICAL_CONSUMPTION_FRUITS_VEGETABLES",
    "interpolate",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LAND_PRODUCTS_I": ["FRUITS_VEGETABLES"],
    },
)

_ext_data_land_products_historical_consumption.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "intermodule_global_allocate",
    "TIME_INTERMODULE",
    "HISTORICAL_CONSUMPTION_OTHER_CROPS",
    "interpolate",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"], "LAND_PRODUCTS_I": ["OTHER_CROPS"]},
)


@component.add(
    name="LAND_PRODUCTS_USED_FOR_ENERGY_PERCENTAGES",
    units="DMNL",
    subscripts=["LAND_PRODUCTS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_land_products_used_for_energy_percentages"
    },
)
def land_products_used_for_energy_percentages():
    """
    percentage of each land product used for energy
    """
    return _ext_constant_land_products_used_for_energy_percentages()


_ext_constant_land_products_used_for_energy_percentages = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Diet",
    "LAND_PRODUCTS_USED_FOR_ENERGY_PERCENTAGES*",
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"]},
    _root,
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"]},
    "_ext_constant_land_products_used_for_energy_percentages",
)


@component.add(
    name="LIMITS_TO_LAND_USE_CHANGES_BY_REGION",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LANDS_I", "LANDS_MAP_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_limits_to_land_use_changes_by_region"},
)
def limits_to_land_use_changes_by_region():
    """
    maximum land use change allowed from use LANDS_I to use LANDS_I_MAP in percent of the initial land of the use that gives (LANDS_I)
    """
    return _ext_constant_limits_to_land_use_changes_by_region()


_ext_constant_limits_to_land_use_changes_by_region = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "LIMITS_TO_LAND_USE_CHANGES_EU27",
    {
        "REGIONS_9_I": ["EU27"],
        "LANDS_I": _subscript_dict["LANDS_I"],
        "LANDS_MAP_I": _subscript_dict["LANDS_MAP_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": _subscript_dict["LANDS_I"],
        "LANDS_MAP_I": _subscript_dict["LANDS_MAP_I"],
    },
    "_ext_constant_limits_to_land_use_changes_by_region",
)

_ext_constant_limits_to_land_use_changes_by_region.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "LIMITS_TO_LAND_USE_CHANGES_UK",
    {
        "REGIONS_9_I": ["UK"],
        "LANDS_I": _subscript_dict["LANDS_I"],
        "LANDS_MAP_I": _subscript_dict["LANDS_MAP_I"],
    },
)

_ext_constant_limits_to_land_use_changes_by_region.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "LIMITS_TO_LAND_USE_CHANGES_CHINA",
    {
        "REGIONS_9_I": ["CHINA"],
        "LANDS_I": _subscript_dict["LANDS_I"],
        "LANDS_MAP_I": _subscript_dict["LANDS_MAP_I"],
    },
)

_ext_constant_limits_to_land_use_changes_by_region.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "LIMITS_TO_LAND_USE_CHANGES_EASOC",
    {
        "REGIONS_9_I": ["EASOC"],
        "LANDS_I": _subscript_dict["LANDS_I"],
        "LANDS_MAP_I": _subscript_dict["LANDS_MAP_I"],
    },
)

_ext_constant_limits_to_land_use_changes_by_region.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "LIMITS_TO_LAND_USE_CHANGES_INDIA",
    {
        "REGIONS_9_I": ["INDIA"],
        "LANDS_I": _subscript_dict["LANDS_I"],
        "LANDS_MAP_I": _subscript_dict["LANDS_MAP_I"],
    },
)

_ext_constant_limits_to_land_use_changes_by_region.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "LIMITS_TO_LAND_USE_CHANGES_LATAM",
    {
        "REGIONS_9_I": ["LATAM"],
        "LANDS_I": _subscript_dict["LANDS_I"],
        "LANDS_MAP_I": _subscript_dict["LANDS_MAP_I"],
    },
)

_ext_constant_limits_to_land_use_changes_by_region.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "LIMITS_TO_LAND_USE_CHANGES_RUSSIA",
    {
        "REGIONS_9_I": ["RUSSIA"],
        "LANDS_I": _subscript_dict["LANDS_I"],
        "LANDS_MAP_I": _subscript_dict["LANDS_MAP_I"],
    },
)

_ext_constant_limits_to_land_use_changes_by_region.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "LIMITS_TO_LAND_USE_CHANGES_USMCA",
    {
        "REGIONS_9_I": ["USMCA"],
        "LANDS_I": _subscript_dict["LANDS_I"],
        "LANDS_MAP_I": _subscript_dict["LANDS_MAP_I"],
    },
)

_ext_constant_limits_to_land_use_changes_by_region.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "LIMITS_TO_LAND_USE_CHANGES_LROW",
    {
        "REGIONS_9_I": ["LROW"],
        "LANDS_I": _subscript_dict["LANDS_I"],
        "LANDS_MAP_I": _subscript_dict["LANDS_MAP_I"],
    },
)


@component.add(
    name="LIMITS_TO_SOLAR_LAND_EXPANSION_EROI_MIN_0",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LANDS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_limits_to_solar_land_expansion_eroi_min_0"
    },
)
def limits_to_solar_land_expansion_eroi_min_0():
    """
    Share of are of each land use in 2015 that can be used for solar.
    """
    return _ext_constant_limits_to_solar_land_expansion_eroi_min_0()


_ext_constant_limits_to_solar_land_expansion_eroi_min_0 = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "LIMITS_TO_SOLAR_LAND_EXPANSION_EROI_MIN_0",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": _subscript_dict["LANDS_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": _subscript_dict["LANDS_I"],
    },
    "_ext_constant_limits_to_solar_land_expansion_eroi_min_0",
)


@component.add(
    name="LIMITS_TO_SOLAR_LAND_EXPANSION_EROI_MIN_10",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LANDS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_limits_to_solar_land_expansion_eroi_min_10"
    },
)
def limits_to_solar_land_expansion_eroi_min_10():
    """
    Share of are of each land use in 2015 that can be used for solar.
    """
    return _ext_constant_limits_to_solar_land_expansion_eroi_min_10()


_ext_constant_limits_to_solar_land_expansion_eroi_min_10 = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "LIMITS_TO_SOLAR_LAND_EXPANSION_EROI_MIN_10",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": _subscript_dict["LANDS_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": _subscript_dict["LANDS_I"],
    },
    "_ext_constant_limits_to_solar_land_expansion_eroi_min_10",
)


@component.add(
    name="LIMITS_TO_SOLAR_LAND_EXPANSION_EROI_MIN_2",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LANDS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_limits_to_solar_land_expansion_eroi_min_2"
    },
)
def limits_to_solar_land_expansion_eroi_min_2():
    """
    Share of are of each land use in 2015 that can be used for solar.
    """
    return _ext_constant_limits_to_solar_land_expansion_eroi_min_2()


_ext_constant_limits_to_solar_land_expansion_eroi_min_2 = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "LIMITS_TO_SOLAR_LAND_EXPANSION_EROI_MIN_2",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": _subscript_dict["LANDS_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": _subscript_dict["LANDS_I"],
    },
    "_ext_constant_limits_to_solar_land_expansion_eroi_min_2",
)


@component.add(
    name="LIMITS_TO_SOLAR_LAND_EXPANSION_EROI_MIN_3",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LANDS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_limits_to_solar_land_expansion_eroi_min_3"
    },
)
def limits_to_solar_land_expansion_eroi_min_3():
    """
    Share of are of each land use in 2015 that can be used for solar.
    """
    return _ext_constant_limits_to_solar_land_expansion_eroi_min_3()


_ext_constant_limits_to_solar_land_expansion_eroi_min_3 = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "LIMITS_TO_SOLAR_LAND_EXPANSION_EROI_MIN_3",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": _subscript_dict["LANDS_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": _subscript_dict["LANDS_I"],
    },
    "_ext_constant_limits_to_solar_land_expansion_eroi_min_3",
)


@component.add(
    name="LIMITS_TO_SOLAR_LAND_EXPANSION_EROI_MIN_5",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LANDS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_limits_to_solar_land_expansion_eroi_min_5"
    },
)
def limits_to_solar_land_expansion_eroi_min_5():
    """
    Share of are of each land use in 2015 that can be used for solar.
    """
    return _ext_constant_limits_to_solar_land_expansion_eroi_min_5()


_ext_constant_limits_to_solar_land_expansion_eroi_min_5 = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "LIMITS_TO_SOLAR_LAND_EXPANSION_EROI_MIN_5",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": _subscript_dict["LANDS_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": _subscript_dict["LANDS_I"],
    },
    "_ext_constant_limits_to_solar_land_expansion_eroi_min_5",
)


@component.add(
    name="LIMITS_TO_SOLAR_LAND_EXPANSION_EROI_MIN_8",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LANDS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_limits_to_solar_land_expansion_eroi_min_8"
    },
)
def limits_to_solar_land_expansion_eroi_min_8():
    """
    Share of are of each land use in 2015 that can be used for solar.
    """
    return _ext_constant_limits_to_solar_land_expansion_eroi_min_8()


_ext_constant_limits_to_solar_land_expansion_eroi_min_8 = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "LIMITS_TO_SOLAR_LAND_EXPANSION_EROI_MIN_8",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": _subscript_dict["LANDS_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": _subscript_dict["LANDS_I"],
    },
    "_ext_constant_limits_to_solar_land_expansion_eroi_min_8",
)


@component.add(
    name="LOSS_FACTOR_OF_LAND_PRODUCTS",
    units="DMNL",
    subscripts=["LAND_PRODUCTS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_loss_factor_of_land_products"},
)
def loss_factor_of_land_products():
    return _ext_constant_loss_factor_of_land_products()


_ext_constant_loss_factor_of_land_products = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "intermodule_global_allocate",
    "LOSS_FACTOR_LAND_PRODUCTS*",
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"]},
    _root,
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"]},
    "_ext_constant_loss_factor_of_land_products",
)


@component.add(
    name="MANAGEMENT_STOCK_CHANGE_FACTOR_DEFAULT_CROPLAND",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_management_stock_change_factor_default_cropland"
    },
)
def management_stock_change_factor_default_cropland():
    """
    Factors for "Cbefore". Soil database (regionally average C stocks) corresponds to Cbef (default values) assuming full tillage (FMG), Input is medium (FI) and long-term cultivated (FLU).
    """
    return _ext_constant_management_stock_change_factor_default_cropland()


_ext_constant_management_stock_change_factor_default_cropland = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "DEFAULT_MANAGEMENT_STOCK_FACTOR_CROPS*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_management_stock_change_factor_default_cropland",
)


@component.add(
    name="MANAGEMENT_STOCK_CHANGE_FACTOR_DEFAULT_GRASSLAND",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_management_stock_change_factor_default_grassland"
    },
)
def management_stock_change_factor_default_grassland():
    """
    Factors for "Cbefore". Soil database (regionally average C stocks) corresponds to Cbef (default values) For grasslands (Plevin et al 2014) ,assume a value of 1 for all three: LU (following the IPCC recommendation for all grassland); MG, assuming the land is nominally managed (non-degraded); and I, assuming medium inputs .
    """
    return _ext_constant_management_stock_change_factor_default_grassland()


_ext_constant_management_stock_change_factor_default_grassland = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "DEFAULT_MANAGEMENT_STOCK_FACTOR_GRASSLANDS*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_management_stock_change_factor_default_grassland",
)


@component.add(
    name="MASK_CROPS",
    units="DMNL",
    subscripts=["LAND_PRODUCTS_I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def mask_crops():
    """
    =1 if land product is a crop , 0 for wood and residues and for other crops because its demand is not given by the diets module
    """
    return xr.DataArray(
        [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0],
        {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"]},
        ["LAND_PRODUCTS_I"],
    )


@component.add(
    name="MASK_ESSENTIAL_FOODS",
    units="DMNL",
    subscripts=["LAND_PRODUCTS_I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def mask_essential_foods():
    return xr.DataArray(
        [1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0],
        {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"]},
        ["LAND_PRODUCTS_I"],
    )


@component.add(
    name="MATRIX_COUNTRY_REGION",
    subscripts=["REGIONS_35_I", "REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_matrix_country_region"},
)
def matrix_country_region():
    """
    GET_DIRECT_CONSTANTS( 'model_parameters/constants.xlsx', 'constants', 'D76' )
    """
    return _ext_constant_matrix_country_region()


_ext_constant_matrix_country_region = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Water",
    "water_matrix",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
    },
    "_ext_constant_matrix_country_region",
)


@component.add(
    name="MATRIX_OF_CC_YIELDS_ZONE_REGION",
    units="DMNL",
    subscripts=["REGIONS_9_I", "CLIMATIC_ZONES_I", "LAND_PRODUCTS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_matrix_of_cc_yields_zone_region"},
)
def matrix_of_cc_yields_zone_region():
    return _ext_constant_matrix_of_cc_yields_zone_region()


_ext_constant_matrix_of_cc_yields_zone_region = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "MATRIX_OF_CC_YIELDS_ZONE_REGION_EU27",
    {
        "REGIONS_9_I": ["EU27"],
        "CLIMATIC_ZONES_I": _subscript_dict["CLIMATIC_ZONES_I"],
        "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "CLIMATIC_ZONES_I": _subscript_dict["CLIMATIC_ZONES_I"],
        "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
    },
    "_ext_constant_matrix_of_cc_yields_zone_region",
)

_ext_constant_matrix_of_cc_yields_zone_region.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "MATRIX_OF_CC_YIELDS_ZONE_REGION_UK",
    {
        "REGIONS_9_I": ["UK"],
        "CLIMATIC_ZONES_I": _subscript_dict["CLIMATIC_ZONES_I"],
        "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
    },
)

_ext_constant_matrix_of_cc_yields_zone_region.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "MATRIX_OF_CC_YIELDS_ZONE_REGION_CHINA",
    {
        "REGIONS_9_I": ["CHINA"],
        "CLIMATIC_ZONES_I": _subscript_dict["CLIMATIC_ZONES_I"],
        "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
    },
)

_ext_constant_matrix_of_cc_yields_zone_region.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "MATRIX_OF_CC_YIELDS_ZONE_REGION_EASOC",
    {
        "REGIONS_9_I": ["EASOC"],
        "CLIMATIC_ZONES_I": _subscript_dict["CLIMATIC_ZONES_I"],
        "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
    },
)

_ext_constant_matrix_of_cc_yields_zone_region.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "MATRIX_OF_CC_YIELDS_ZONE_REGION_INDIA",
    {
        "REGIONS_9_I": ["INDIA"],
        "CLIMATIC_ZONES_I": _subscript_dict["CLIMATIC_ZONES_I"],
        "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
    },
)

_ext_constant_matrix_of_cc_yields_zone_region.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "MATRIX_OF_CC_YIELDS_ZONE_REGION_LATAM",
    {
        "REGIONS_9_I": ["LATAM"],
        "CLIMATIC_ZONES_I": _subscript_dict["CLIMATIC_ZONES_I"],
        "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
    },
)

_ext_constant_matrix_of_cc_yields_zone_region.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "MATRIX_OF_CC_YIELDS_ZONE_REGION_RUSSIA",
    {
        "REGIONS_9_I": ["RUSSIA"],
        "CLIMATIC_ZONES_I": _subscript_dict["CLIMATIC_ZONES_I"],
        "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
    },
)

_ext_constant_matrix_of_cc_yields_zone_region.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "MATRIX_OF_CC_YIELDS_ZONE_REGION_USMCA",
    {
        "REGIONS_9_I": ["USMCA"],
        "CLIMATIC_ZONES_I": _subscript_dict["CLIMATIC_ZONES_I"],
        "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
    },
)

_ext_constant_matrix_of_cc_yields_zone_region.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "MATRIX_OF_CC_YIELDS_ZONE_REGION_LROW",
    {
        "REGIONS_9_I": ["LROW"],
        "CLIMATIC_ZONES_I": _subscript_dict["CLIMATIC_ZONES_I"],
        "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
    },
)


@component.add(
    name="MAXIMUM_ANNUAL_LAND_USE_CHANGE",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_maximum_annual_land_use_change"},
)
def maximum_annual_land_use_change():
    return _ext_constant_maximum_annual_land_use_change()


_ext_constant_maximum_annual_land_use_change = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "MAXIMUM_ANNUAL_LAND_USE_CHANGE",
    {},
    _root,
    {},
    "_ext_constant_maximum_annual_land_use_change",
)


@component.add(
    name="MAXIMUM_CROP_SHARES",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_maximum_crop_shares"},
)
def maximum_crop_shares():
    return _ext_constant_maximum_crop_shares()


_ext_constant_maximum_crop_shares = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "MAXIMUM_SHARES_OF_CROPS",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
    },
    "_ext_constant_maximum_crop_shares",
)


@component.add(
    name="MAXIMUM_EXPLOITATION_WATER_COEFFICIENT",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="Normal",
)
def maximum_exploitation_water_coefficient():
    """
    max exploitable to preserve envirn systems (from Amandine) Could change with policies, we can put in the excel: scenario_parameters, add in water explotation. 0.3 and 0.2.
    """
    return 0.4


@component.add(
    name="MAXIMUM_FOREST_STOCK_PER_AREA",
    units="m3/km2",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_maximum_forest_stock_per_area"},
)
def maximum_forest_stock_per_area():
    return _ext_constant_maximum_forest_stock_per_area()


_ext_constant_maximum_forest_stock_per_area = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "forest",
    "MAXIMUM_FOREST_STOCK_PER_AREA*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_maximum_forest_stock_per_area",
)


@component.add(
    name="MAXIMUM_INTAKE_FOR_HEALTHY_DIETS",
    units="DMNL",
    subscripts=["REGIONS_9_I", "NUTRITION_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_maximum_intake_for_healthy_diets"},
)
def maximum_intake_for_healthy_diets():
    """
    MAXIMUM_INTAKE_FOR_HEALTHY_DIETS
    """
    return _ext_constant_maximum_intake_for_healthy_diets()


_ext_constant_maximum_intake_for_healthy_diets = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Diet",
    "MAXIMUM_INTAKE_FOR_HEALTHY_DIETS",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "NUTRITION_I": _subscript_dict["NUTRITION_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "NUTRITION_I": _subscript_dict["NUTRITION_I"],
    },
    "_ext_constant_maximum_intake_for_healthy_diets",
)


@component.add(
    name="MAXIMUM_IRRIGATED_CROPS_SHARES",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_maximum_irrigated_crops_shares"},
)
def maximum_irrigated_crops_shares():
    return _ext_constant_maximum_irrigated_crops_shares()


_ext_constant_maximum_irrigated_crops_shares = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "MAXIMUM_SHARES_OF_IRRIGATED_CROPS",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
    },
    "_ext_constant_maximum_irrigated_crops_shares",
)


@component.add(
    name="MAXIMUM_LAND_USES_BY_SOURCE",
    subscripts=["REGIONS_9_I", "LANDS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_maximum_land_uses_by_source"},
)
def maximum_land_uses_by_source():
    return _ext_constant_maximum_land_uses_by_source()


_ext_constant_maximum_land_uses_by_source = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "MAXIMUM_INCREASE_OF_LAND_SOURCE",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": _subscript_dict["LANDS_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": _subscript_dict["LANDS_I"],
    },
    "_ext_constant_maximum_land_uses_by_source",
)


@component.add(
    name="MAXIMUM_RAINFED_CROPS_SHARES",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_maximum_rainfed_crops_shares"},
)
def maximum_rainfed_crops_shares():
    return _ext_constant_maximum_rainfed_crops_shares()


_ext_constant_maximum_rainfed_crops_shares = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "MAXIMUM_SHARES_OF_RAINFED_CROPS",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
    },
    "_ext_constant_maximum_rainfed_crops_shares",
)


@component.add(
    name="MAXIMUM_YIELDS_R_AND_I_INDUSTRIAL",
    units="t/(km2*Year)",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_maximum_yields_r_and_i_industrial"},
)
def maximum_yields_r_and_i_industrial():
    return _ext_constant_maximum_yields_r_and_i_industrial()


_ext_constant_maximum_yields_r_and_i_industrial = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "MAXIMUM_YIELDS_R_AND_I",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
    },
    "_ext_constant_maximum_yields_r_and_i_industrial",
)


@component.add(
    name="MAXIMUM_YIELDS_RAINFED_INDUSTRIAL",
    units="t/(km2*Year)",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_maximum_yields_rainfed_industrial"},
)
def maximum_yields_rainfed_industrial():
    """
    test
    """
    return _ext_constant_maximum_yields_rainfed_industrial()


_ext_constant_maximum_yields_rainfed_industrial = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "MAXIMUM_YIELDS_RAINFED_INDUSTRIAL",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
    },
    "_ext_constant_maximum_yields_rainfed_industrial",
)


@component.add(
    name="MINIMUM_INTAKE_FOR_HEALTHY_DIETS",
    units="DMNL",
    subscripts=["REGIONS_9_I", "NUTRITION_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_minimum_intake_for_healthy_diets"},
)
def minimum_intake_for_healthy_diets():
    """
    MINIMUM_INTAKE_FOR_HEALTHY_DIETS
    """
    return _ext_constant_minimum_intake_for_healthy_diets()


_ext_constant_minimum_intake_for_healthy_diets = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Diet",
    "MINIMUM_INTAKE_FOR_HEALTHY_DIETS",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "NUTRITION_I": _subscript_dict["NUTRITION_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "NUTRITION_I": _subscript_dict["NUTRITION_I"],
    },
    "_ext_constant_minimum_intake_for_healthy_diets",
)


@component.add(
    name="MINIMUM_LAND_USES_BY_REGION",
    units="km2",
    subscripts=["REGIONS_9_I", "LANDS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_minimum_land_uses_by_region"},
)
def minimum_land_uses_by_region():
    """
    Minimum limit of land use for each region
    """
    return _ext_constant_minimum_land_uses_by_region()


_ext_constant_minimum_land_uses_by_region = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "MINIMUM_LAND_USES_BY_REGION",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": _subscript_dict["LANDS_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": _subscript_dict["LANDS_I"],
    },
    "_ext_constant_minimum_land_uses_by_region",
)


@component.add(
    name="OBJECTIVE_AFFORESTATION_SP",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_objective_afforestation_sp"},
)
def objective_afforestation_sp():
    """
    -Policy of increase of managed forest. -This is an increase of the hihg biodiversity forest (not the increase of tree plantations) -The OBJECTIVE area of forest is achieved in the FINAL TIME with a lineal evolution. -OBJECTIVE of this policy is expressed as a % of the historical value of the area of forest of 2015 (0=0%, means that there is no increse of forest; 1=100%, means that the area reforested equals forest area in 2015). -This policy competes with the rest of land uses, therefore, the forest area objective might not be achiven in the final year due to land use changes from forest to other uses.
    """
    return _ext_constant_objective_afforestation_sp()


_ext_constant_objective_afforestation_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_OBJECTIVE_AFFORESTATION_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_objective_afforestation_sp",
)


@component.add(
    name="OBJECTIVE_CROPLAND_PROTECTION_SP",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_objective_cropland_protection_sp"},
)
def objective_cropland_protection_sp():
    """
    -If this policy is applied, the cropland (Sum of irrigated and rainfed cropland) is protected and its area does not go down the value given in OBJECTIVE. -The protection starts in INITIAL YEAR and ends in FINAL YEAR. -If cropland area in INITIAL YEAR is lower than OBJECTIVE*cropland area in 2015 (TIME HISTORICAL DATA LAND MODULE), the area in INITIAL YEAR is maintained. -OBJECTIVE of policy is expressed as a share of the initial area of cropland in 2015 (from 0 to 1; =1 means that an area equal to the cropland we had in 2015 is protected, =0 means that there are no limits to cropland loss).
    """
    return _ext_constant_objective_cropland_protection_sp()


_ext_constant_objective_cropland_protection_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_OBJECTIVE_CROPLAND_PROTECTION_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_objective_cropland_protection_sp",
)


@component.add(
    name="OBJECTIVE_DIET_CHANGE_SP",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_objective_diet_change_sp"},
)
def objective_diet_change_sp():
    """
    -If this policy is applied, the population starts a cultural-driven change of diet to the policy diets that starts in INITIAL YEAR and ends in FINAL YEAR. -OBJECTIVE of this policy is expressed as a share of the population that has adopted the policy diet in FINAL YEAR. -OBJECTIVE varies between 0 and 1 (0= means that there no dietary change, 1= means that all the population adopts the policy diet).
    """
    return _ext_constant_objective_diet_change_sp()


_ext_constant_objective_diet_change_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "OBJECTIVE_DIET_CHANGE_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_objective_diet_change_sp",
)


@component.add(
    name="OBJECTIVE_EFFECT_OF_OIL_AND_GAS_ON_AGRICULTURE_SP",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_objective_effect_of_oil_and_gas_on_agriculture_sp"
    },
)
def objective_effect_of_oil_and_gas_on_agriculture_sp():
    """
    EL OBJETIVO EXPRESADO COMO EL PORCENTAJE DE LA INDUSTRIAL EN EL AÑO INICIAL QUE YA NO ES VIABLE Y PASA A LOW INPUT OBJETIVO DEBE ESTAR ENTRE 0 Y 1-
    """
    return _ext_constant_objective_effect_of_oil_and_gas_on_agriculture_sp()


_ext_constant_objective_effect_of_oil_and_gas_on_agriculture_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "OBJECTIVE_EFFECT_OIL_AND_GAS_ON_AGRICULTURE_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_objective_effect_of_oil_and_gas_on_agriculture_sp",
)


@component.add(
    name="OBJECTIVE_FOREST_PLANTATIONS_SP",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_objective_forest_plantations_sp"},
)
def objective_forest_plantations_sp():
    """
    -This is an increase of tree plantations. -The OBJECTIVE area of forest is achieved in the FINAL TIME with a lineal evolution. -OBJECTIVE of this policy is expressed as a % of the historical value of the area of PLANTATIONS of 2015 (0=0%, means that there is no increse of plantations; 1=100%, means that the area planted equals plantations area in 2015). -This policy competes with the rest of land uses, therefore, the area objective might not be achiven in the final year due to land use changes to other uses.
    """
    return _ext_constant_objective_forest_plantations_sp()


_ext_constant_objective_forest_plantations_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "OBJECTIVE_FOREST_PLANTATIONS*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_objective_forest_plantations_sp",
)


@component.add(
    name="OBJECTIVE_FORESTRY_SELF_SUFFICIENCY_SP",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_objective_forestry_self_sufficiency_sp"},
)
def objective_forestry_self_sufficiency_sp():
    """
    forest overexplotation policy objective 0 means that only sustainable extraction is allowed, >0 means that a percent of stock loss is allowed, for example, objective=0.01 means that 1% os the stock of the forest can be loss per year
    """
    return _ext_constant_objective_forestry_self_sufficiency_sp()


_ext_constant_objective_forestry_self_sufficiency_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "OBJECTIVE_FORESTRY_SELF_SUFFICIENCY_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_objective_forestry_self_sufficiency_sp",
)


@component.add(
    name="OBJECTIVE_GRASSLAND_PROTECTION_SP",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_objective_grassland_protection_sp"},
)
def objective_grassland_protection_sp():
    """
    -If this policy is applied, the grassland is protected and its area does not go down the value given in OBJECTIVE. -The protection starts in INITIAL YEAR and ends in FINAL YEAR. -If grassland area in INITIAL YEAR is lower than OBJECTIVE*grassland area in 2015 (TIME HISTORICAL DATA LAND MODULE), the area in INITIAL YEAR is maintained. -OBJECTIVE of policy is expressed as a share of the initial area of grassland in 2015 (from 0 to 1; =1 means that an area equal to the grassland we had in 2015 is protected, =0 means that there are no limits to grassland loss).
    """
    return _ext_constant_objective_grassland_protection_sp()


_ext_constant_objective_grassland_protection_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_OBJECTIVE_GRASSLAND_PROTECTION_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_objective_grassland_protection_sp",
)


@component.add(
    name="OBJECTIVE_INDUSTRIAL_AGRICULTURE_SP",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_objective_industrial_agriculture_sp"},
)
def objective_industrial_agriculture_sp():
    """
    policy objective
    """
    return _ext_constant_objective_industrial_agriculture_sp()


_ext_constant_objective_industrial_agriculture_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_OBJECTIVE_INDUSTRIAL_AGRICULTURE_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_objective_industrial_agriculture_sp",
)


@component.add(
    name="OBJECTIVE_LAND_PRODUCTS_GLOBAL_POOL_SP",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_objective_land_products_global_pool_sp"},
)
def objective_land_products_global_pool_sp():
    """
    -Policy of protection of land products from global trade.
    """
    return _ext_constant_objective_land_products_global_pool_sp()


_ext_constant_objective_land_products_global_pool_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "OBJECTIVE_LAND_PRODUCTS_GLOBAL_POOL_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_objective_land_products_global_pool_sp",
)


@component.add(
    name="OBJECTIVE_MANAGED_FOREST_PROTECTION_SP",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_objective_managed_forest_protection_sp"},
)
def objective_managed_forest_protection_sp():
    """
    -If this policy is applied, the managed forest is protected and its area does not go down the value given in OBJECTIVE. -The protection starts in INITIAL YEAR and ends in FINAL YEAR. -If managed forest area in INITIAL YEAR is lower than OBJECTIVE*forest area in 2015 (TIME HISTORICAL DATA LAND MODULE), the area in INITIAL YEAR is maintained. -OBJECTIVE of policy is expressed as a share of the initial area of managed forest in 2015 (from 0 to 1; =1 means that an area equal to the managed forest we had in 2015 is protected, =0 means that there are no limits to deforestation).
    """
    return _ext_constant_objective_managed_forest_protection_sp()


_ext_constant_objective_managed_forest_protection_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_OBJECTIVE_MANAGED_FOREST_PROTECTION_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_objective_managed_forest_protection_sp",
)


@component.add(
    name="OBJECTIVE_NATURAL_LAND_PROTECTION_SP",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_objective_natural_land_protection_sp"},
)
def objective_natural_land_protection_sp():
    """
    -If this policy is applied, the natural land is protected and its area does not go down the value given in OBJECTIVE. -The protection starts in INITIAL YEAR and ends in FINAL YEAR. -If natural land area in INITIAL YEAR is lower than OBJECTIVE*natural land area in 2015 (TIME HISTORICAL DATA LAND MODULE), the area in INITIAL YEAR is maintained. -OBJECTIVE of policy is expressed as a share of the initial area of natural land in 2015 (from 0 to 1; =1 means that an area equal to the land natural we had in 2015 is protected, =0 means that there are no limits to natural land loss).
    """
    return _ext_constant_objective_natural_land_protection_sp()


_ext_constant_objective_natural_land_protection_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_OBJECTIVE_NATURAL_LAND_PROTECTION_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_objective_natural_land_protection_sp",
)


@component.add(
    name="OBJECTIVE_PRIMARY_FOREST_PROTECTION_SP",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_objective_primary_forest_protection_sp"},
)
def objective_primary_forest_protection_sp():
    """
    -If this policy is applied, the primary forest is protected and its area does not go down the value given in OBJECTIVE. -The protection starts in INITIAL YEAR and ends in FINAL YEAR. -If primary forest area in INITIAL YEAR is lower than OBJECTIVE*forest area in 2015 (TIME HISTORICAL DATA LAND MODULE), the area in INITIAL YEAR is maintained. -OBJECTIVE of policy is expressed as a share of the initial area of primary forest in 2015 (from 0 to 1; =1 means that an area equal to the primary forest we had in 2015 is protected, =0 means that there are no limits to deforestation).
    """
    return _ext_constant_objective_primary_forest_protection_sp()


_ext_constant_objective_primary_forest_protection_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_OBJECTIVE_PRIMARY_FOREST_PROTECTION_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_objective_primary_forest_protection_sp",
)


@component.add(
    name="OBJECTIVE_REGENERATIVE_AGRICULTURE_SP",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_objective_regenerative_agriculture_sp"},
)
def objective_regenerative_agriculture_sp():
    """
    policy objective
    """
    return _ext_constant_objective_regenerative_agriculture_sp()


_ext_constant_objective_regenerative_agriculture_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_OBJECTIVE_REGENERATIVE_AGRICULTURE_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_objective_regenerative_agriculture_sp",
)


@component.add(
    name="OBJECTIVE_SOIL_MANAGEMENT_IN_GRASSLANDS_SP",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_objective_soil_management_in_grasslands_sp"
    },
)
def objective_soil_management_in_grasslands_sp():
    """
    soil management in grasslands policy objective
    """
    return _ext_constant_objective_soil_management_in_grasslands_sp()


_ext_constant_objective_soil_management_in_grasslands_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "OBJECTIVE_SOIL_MANAGEMENT_IN_GRASSLANDS_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_objective_soil_management_in_grasslands_sp",
)


@component.add(
    name="OBJECTIVE_SOLAR_LAND_FROM_OTHERS_SP",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LANDS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_objective_solar_land_from_others_sp"},
)
def objective_solar_land_from_others_sp():
    """
    solar land from others objective
    """
    return _ext_constant_objective_solar_land_from_others_sp()


_ext_constant_objective_solar_land_from_others_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "OBJECTIVE_SOLAR_LAND_FROM_OTHERS",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": _subscript_dict["LANDS_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": _subscript_dict["LANDS_I"],
    },
    "_ext_constant_objective_solar_land_from_others_sp",
)


@component.add(
    name="OBJECTIVE_URBAN_LAND_DENSITY_SP",
    units="m2/person",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_objective_urban_land_density_sp"},
)
def objective_urban_land_density_sp():
    """
    Policy objective to set urban land density in final year of policy.
    """
    return _ext_constant_objective_urban_land_density_sp()


_ext_constant_objective_urban_land_density_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "OBJECTIVE_URBAN_LAND_DENSITY_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_objective_urban_land_density_sp",
)


@component.add(
    name="OBJECTIVE_WATER_EFFICIENCY_SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_objective_water_efficiency_sp"},
)
def objective_water_efficiency_sp():
    """
    OBJECTIVE_WATER_EFFICIENCY_SP
    """
    return _ext_constant_objective_water_efficiency_sp()


_ext_constant_objective_water_efficiency_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "OBJECTIVE_WATER_EFFICIENCY_SP*",
    {},
    _root,
    {},
    "_ext_constant_objective_water_efficiency_sp",
)


@component.add(
    name="OUTTURN_OF_WOOD_EXTRACTION",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_outturn_of_wood_extraction"},
)
def outturn_of_wood_extraction():
    return _ext_constant_outturn_of_wood_extraction()


_ext_constant_outturn_of_wood_extraction = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "forest",
    "OUTTURN_OF_WOOD_EXTRACTION*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_outturn_of_wood_extraction",
)


@component.add(
    name="PAST_TRENDS_GLOBAL_CO2_LAND_USE_CHANGE_EMISSIONS",
    units="GtCO2/Year",
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_past_trends_global_co2_land_use_change_emissions",
        "__data__": "_ext_data_past_trends_global_co2_land_use_change_emissions",
        "time": 1,
    },
)
def past_trends_global_co2_land_use_change_emissions():
    """
    [DICE-2013R] Land-use change emissions. Cte at 2010 level for the period 1990-2100 as first approximation. Also aligned with Houghton Et al 2017--> Global and regional fluxes of carbon from land use and land cover change 1850–2015 (total cumulative = 145,5 / (2015-1850)= 0.88 GtC/año (in DICE = 0,9 GtC/año)
    """
    return _ext_data_past_trends_global_co2_land_use_change_emissions(time())


_ext_data_past_trends_global_co2_land_use_change_emissions = ExtData(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "TIME_OTHER_GHG_EMISSIONS",
    "LAND_USE_CHANGE_EMISSIONS",
    "interpolate",
    {},
    _root,
    {},
    "_ext_data_past_trends_global_co2_land_use_change_emissions",
)


@component.add(
    name="PERCENT_OF_LAND_PRODUCTS_FOR_OTHER_USES",
    units="DMNL",
    subscripts=["LAND_PRODUCTS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_percent_of_land_products_for_other_uses"
    },
)
def percent_of_land_products_for_other_uses():
    """
    Percentages of food + feed + energy - other uses
    """
    return _ext_constant_percent_of_land_products_for_other_uses()


_ext_constant_percent_of_land_products_for_other_uses = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Diet",
    "LAND_PRODUCTS_DISTRIBUTION_PERCENTAGES*",
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"]},
    _root,
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"]},
    "_ext_constant_percent_of_land_products_for_other_uses",
)


@component.add(
    name="PLANT_BASED_100_DIET_PATTERN_OF_POLICY_DIETS_SP",
    units="kg/(Year*people)",
    subscripts=["REGIONS_9_I", "FOODS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_plant_based_100_diet_pattern_of_policy_diets_sp"
    },
)
def plant_based_100_diet_pattern_of_policy_diets_sp():
    """
    100% plant based policy diet
    """
    return _ext_constant_plant_based_100_diet_pattern_of_policy_diets_sp()


_ext_constant_plant_based_100_diet_pattern_of_policy_diets_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "PLANT_BASED_100_DIET_PATTERN_OF_POLICY_DIETS_SP",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "FOODS_I": _subscript_dict["FOODS_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "FOODS_I": _subscript_dict["FOODS_I"],
    },
    "_ext_constant_plant_based_100_diet_pattern_of_policy_diets_sp",
)


@component.add(
    name="POLICIES_OF_LAND_USE_CHANGE_FROM_OTHERS_AT_REGIONAL_LEVEL",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="Normal",
)
def policies_of_land_use_change_from_others_at_regional_level():
    """
    EQUATION NOT SET esto seria par ahacer que la demanda de tierras de solar y de urban no se tomase de un tipo de tierras sino de otras,cambios poco a poco en os hsares
    """
    return 0


@component.add(
    name="POLICY_LAND_PROTECTION_FROM_SOLAR_PV_SP",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LANDS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_policy_land_protection_from_solar_pv_sp"
    },
)
def policy_land_protection_from_solar_pv_sp():
    """
    Policies of land protected from solar PV deployment. if =1 the policy allows to deploy solar PV in that land use type if =0 the policy protect that type of land use to be occupied for solar PV
    """
    return _ext_constant_policy_land_protection_from_solar_pv_sp()


_ext_constant_policy_land_protection_from_solar_pv_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_LAND_PROTECTION_FROM_SOLAR_PV_SP",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": _subscript_dict["LANDS_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": _subscript_dict["LANDS_I"],
    },
    "_ext_constant_policy_land_protection_from_solar_pv_sp",
)


@component.add(
    name="POLICY_MAXIMUM_SHARE_SOLAR_URBAN_SP",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_policy_maximum_share_solar_urban_sp"},
)
def policy_maximum_share_solar_urban_sp():
    """
    Policy defining the maximum value for the share of urban and solar, --> land use solar/ land use urban Potential changes: not dynamic, better the urban in 2005?? - To put this value considering the relation to cropland (example: solar land/cropland compared to urban_land/cropland).
    """
    return _ext_constant_policy_maximum_share_solar_urban_sp()


_ext_constant_policy_maximum_share_solar_urban_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_MAXIMUM_SHARE_SOLAR_URBAN_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_policy_maximum_share_solar_urban_sp",
)


@component.add(
    name="PREINDUSTRIAL_C",
    units="Gt",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_preindustrial_c"},
)
def preindustrial_c():
    """
    Preindustrial C content of atmosphere.
    """
    return _ext_constant_preindustrial_c()


_ext_constant_preindustrial_c = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "preindustrial_C",
    {},
    _root,
    {},
    "_ext_constant_preindustrial_c",
)


@component.add(
    name="PRIORITIES_OF_CROPS_DISTRIBUTION_AMONG_USES_SP",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I", "USES_LP_I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def priorities_of_crops_distribution_among_uses_sp():
    """
    PRIORITIES_OF_CROPS_DISTRIBUTION_AMONG_USES
    """
    return xr.DataArray(
        1,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
            "USES_LP_I": _subscript_dict["USES_LP_I"],
        },
        ["REGIONS_9_I", "LAND_PRODUCTS_I", "USES_LP_I"],
    )


@component.add(
    name="PRIORITIES_OF_FORESTRY_PRODUCTS_DISTRIBUTION_AMONG_USES_SP",
    units="DMNL",
    subscripts=["REGIONS_9_I", "USES_LP_I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def priorities_of_forestry_products_distribution_among_uses_sp():
    """
    PRIORITIES_OF_FORESTRY_PRODUCTS_DISTRIBUTION_AMONG_USES
    """
    return xr.DataArray(
        1,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "USES_LP_I": _subscript_dict["USES_LP_I"],
        },
        ["REGIONS_9_I", "USES_LP_I"],
    )


@component.add(
    name="PRIORITIES_OF_LAND_PRODUCTS_DISTRIBUTION_AMONG_REGIONS_SP",
    units="DMNL",
    subscripts=["LAND_PRODUCTS_I", "REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_priorities_of_land_products_distribution_among_regions_sp"
    },
)
def priorities_of_land_products_distribution_among_regions_sp():
    """
    PRIORITIES_OF_LAND_PRODUCTS_DISTRIBUTION_AMONG_REGIONS_
    """
    return _ext_constant_priorities_of_land_products_distribution_among_regions_sp()


_ext_constant_priorities_of_land_products_distribution_among_regions_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "PRIORITIES_OF_LAND_PRODUCTS_DISTRIBUTION_REGIONS*",
    {
        "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
    },
    _root,
    {
        "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
    },
    "_ext_constant_priorities_of_land_products_distribution_among_regions_sp",
)


@component.add(
    name="PRIORITIES_OF_LAND_USE_CHANGE_SP",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LANDS_I"],
    comp_type="Constant",
    comp_subtype="External, Normal",
    depends_on={"__external__": "_ext_constant_priorities_of_land_use_change_sp"},
)
def priorities_of_land_use_change_sp():
    """
    propoerties of land use change policy
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "LANDS_I": _subscript_dict["LANDS_I"],
        },
        ["REGIONS_9_I", "LANDS_I"],
    )
    def_subs = xr.zeros_like(value, dtype=bool)
    def_subs.loc[:, ["CROPLAND_RAINFED"]] = True
    def_subs.loc[:, ["FOREST_MANAGED"]] = True
    def_subs.loc[:, ["FOREST_PLANTATIONS"]] = True
    def_subs.loc[:, ["SOLAR_LAND"]] = True
    value.values[
        def_subs.values
    ] = _ext_constant_priorities_of_land_use_change_sp().values[def_subs.values]
    value.loc[:, ["CROPLAND_IRRIGATED"]] = 0
    value.loc[:, ["FOREST_PRIMARY"]] = 0
    value.loc[:, ["SHRUBLAND"]] = 0
    value.loc[:, ["GRASSLAND"]] = 0
    value.loc[:, ["WETLAND"]] = 0
    value.loc[:, ["URBAN_LAND"]] = 0
    value.loc[:, ["SNOW_ICE_WATERBODIES"]] = 0
    value.loc[:, ["OTHER_LAND"]] = 0
    return value


_ext_constant_priorities_of_land_use_change_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "PRIORITIES_OF_LAND_USE_CROPLAND_RAINFED*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"], "LANDS_I": ["CROPLAND_RAINFED"]},
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": _subscript_dict["LANDS_I"],
    },
    "_ext_constant_priorities_of_land_use_change_sp",
)

_ext_constant_priorities_of_land_use_change_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "PRIORITIES_OF_LAND_USE_FOREST_MANAGED*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"], "LANDS_I": ["FOREST_MANAGED"]},
)

_ext_constant_priorities_of_land_use_change_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "PRIORITIES_OF_LAND_USE_FOREST_PLANTATIONS*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"], "LANDS_I": ["FOREST_PLANTATIONS"]},
)

_ext_constant_priorities_of_land_use_change_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "PRIORITIES_OF_LAND_USE_SOLAR_LAND*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"], "LANDS_I": ["SOLAR_LAND"]},
)


@component.add(
    name="ROOT_TO_SHOOT_RATIO_FOREST",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_root_to_shoot_ratio_forest"},
)
def root_to_shoot_ratio_forest():
    """
    root to shoot ratio forest
    """
    return _ext_constant_root_to_shoot_ratio_forest()


_ext_constant_root_to_shoot_ratio_forest = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "forest",
    "ROOT_TO_SHOOT_RATIO_FOREST*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_root_to_shoot_ratio_forest",
)


@component.add(
    name="SATURATION_TIME_OF_REGENERATIVE_GRASSLANDS",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def saturation_time_of_regenerative_grasslands():
    return xr.DataArray(
        50, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
    )


@component.add(
    name="SEA_LEVEL_RISE_PARAMETER_ALPHA",
    units="m/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_sea_level_rise_parameter_alpha"},
)
def sea_level_rise_parameter_alpha():
    """
    parameter alpha is part of the "Roson and Sartori 2016b" equation that assumes a positive relationship between sea level rise and the increase in global mean surface temperature. 〖SLR〗_i=(α+β∆t-V_i )(T-2000)
    """
    return _ext_constant_sea_level_rise_parameter_alpha()


_ext_constant_sea_level_rise_parameter_alpha = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "ALPHA_CONSTANT*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_sea_level_rise_parameter_alpha",
)


@component.add(
    name="SEA_LEVEL_RISE_PARAMETER_BETA",
    units="m/(Year*DegreesC)",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_sea_level_rise_parameter_beta"},
)
def sea_level_rise_parameter_beta():
    """
    parameter beta is part of the "Roson and Sartori 2016b" equation that assumes a positive relationship between sea level rise and the increase in global mean surface temperature. 〖SLR〗_i=(α+β∆t-V_i )(T-2000)
    """
    return _ext_constant_sea_level_rise_parameter_beta()


_ext_constant_sea_level_rise_parameter_beta = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "BETA_CONSTANT*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_sea_level_rise_parameter_beta",
)


@component.add(
    name="SECOND_FACTOR_WATER_EQUATION",
    units="DMNL",
    subscripts=["REGIONS_35_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_second_factor_water_equation"},
)
def second_factor_water_equation():
    return _ext_constant_second_factor_water_equation()


_ext_constant_second_factor_water_equation = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Water",
    "WA_Projections_Eq_Factor_2*",
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    _root,
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    "_ext_constant_second_factor_water_equation",
)


@component.add(
    name="SELECT_EROI_MIN_POTENTIAL_WIND_SOLAR_SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_select_eroi_min_potential_wind_solar_sp"
    },
)
def select_eroi_min_potential_wind_solar_sp():
    """
    Threshold of EROImin selected by the user for the solar and wind potential.
    """
    return _ext_constant_select_eroi_min_potential_wind_solar_sp()


_ext_constant_select_eroi_min_potential_wind_solar_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "SELECT_EROI_MIN_POTENTIAL_WIND_SOLAR_SP",
    {},
    _root,
    {},
    "_ext_constant_select_eroi_min_potential_wind_solar_sp",
)


@component.add(
    name="SELECT_SELECTION_MANAGEMENT_GRASSLAND_SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_select_selection_management_grassland_sp"
    },
)
def select_selection_management_grassland_sp():
    """
    Based on IPCC Table 6.2 (soil stock change factor for different management activities on grassland). 0. Nominally managed (non-degraded). No new policies. Keep present trends/default assumption (Plevin et al. 2014). Sustainably managed grassland, but without significant management improvements. 1. Moderately degraded grassland. Overgrazed or moderately degraded grassland, with somewhat reduced productivity and receiving no management inputs. 2. Severely degraded. Implies major long-term loss of productivity and vegetation cover, due to severe mechanical damage to the vegetation and/or severe soil erosion. 3. Improved grassland medium inputs. Sustainably managed with moderate grazing pressure and that receive at least one improvement (e.g., fertilization, species improvement, irrigation). No additional management inputs have been used. 4. Improved grassland high inputs. Sustainably managed with moderate grazing pressure and that receive at least one improvement (e.g., fertilization, species improvement, irrigation). One or more additional management inputs/improvements have been used (beyond that is required to be classified as improved grassland)
    """
    return _ext_constant_select_selection_management_grassland_sp()


_ext_constant_select_selection_management_grassland_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_OF_GRASSLAND_MANAGEMENT_SELECTED",
    {},
    _root,
    {},
    "_ext_constant_select_selection_management_grassland_sp",
)


@component.add(
    name="SELECT_SELECTION_MANAGEMENT_SOLARLAND_SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_select_selection_management_solarland_sp"
    },
)
def select_selection_management_solarland_sp():
    """
    Based on article from Dirk (Suplementary information: Table S8), Capellán et al 2021 https://www.nature.com/articles/s41598-021-82042-5#author-information 0. Permanently clearing land vegetation 1. Maintain /restore previous vegetation (up to 30 cm) 2. Seeding and management as pastures GET_DIRECT_CONSTANTS('scenario_parameters/scenario_parameters.xlsx', 'land_and_water', 'XXXXX')
    """
    return _ext_constant_select_selection_management_solarland_sp()


_ext_constant_select_selection_management_solarland_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_OF_SOLARLAND_MANAGEMENT_SELECTED",
    {},
    _root,
    {},
    "_ext_constant_select_selection_management_solarland_sp",
)


@component.add(
    name="SHARE_OF_CHANGE_TO_POLICY_DIET_INITIAL_VALUE_SP",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_share_of_change_to_policy_diet_initial_value_sp"
    },
)
def share_of_change_to_policy_diet_initial_value_sp():
    """
    initial value of share of change to policy diet and must be 0.
    """
    return _ext_constant_share_of_change_to_policy_diet_initial_value_sp()


_ext_constant_share_of_change_to_policy_diet_initial_value_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "SHARE_OF_CHANGE_TO_POLICY_DIET_INICIAL_VALUE_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_share_of_change_to_policy_diet_initial_value_sp",
)


@component.add(
    name="SHARE_OF_RESIDUALS_FROM_CROPS",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_share_of_residuals_from_crops"},
)
def share_of_residuals_from_crops():
    return _ext_constant_share_of_residuals_from_crops()


_ext_constant_share_of_residuals_from_crops = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "SHARE_OF_RESIDUALS_FROM_CROPS*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_share_of_residuals_from_crops",
)


@component.add(
    name="SHARE_OF_ROUNDWOOD_EXTRACTION_BY_REGION",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_share_of_roundwood_extraction_by_region"
    },
)
def share_of_roundwood_extraction_by_region():
    return _ext_constant_share_of_roundwood_extraction_by_region()


_ext_constant_share_of_roundwood_extraction_by_region = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "forest",
    "SHARE_OF_WOOD_EXTRACTION_BY_REGION*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_share_of_roundwood_extraction_by_region",
)


@component.add(
    name="SHARE_OF_SHRUBLAND",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_share_of_shrubland"},
)
def share_of_shrubland():
    """
    Share of shrubland by region
    """
    return _ext_constant_share_of_shrubland()


_ext_constant_share_of_shrubland = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "SHARE_OF_SHRUBLAND*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_share_of_shrubland",
)


@component.add(
    name="SOIL_CARBON_DENSITY_DATA_BY_LAND_USE",
    units="tC/ha",
    subscripts=["REGIONS_9_I", "LANDS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_soil_carbon_density_data_by_land_use"},
)
def soil_carbon_density_data_by_land_use():
    """
    SOC before: Soil carbon stock density data (soil carbon database) before conversion, and based also in assumptions for "land use factors" (current trends). Source: Assumed carbon stock in GCAM land use module. Van de Ven et al. 2021,.The potential land requirements and related land use change emissions of solar energy Notes: Vegetation in cropland, wetland and snow-ice-waterbodies data should be reviewed and improved. In the case of waterbodies soil carbon stock, and wetland carbon data, the numbers should be corrected in the future. For this version their area is cte so this information is not used.
    """
    return _ext_constant_soil_carbon_density_data_by_land_use()


_ext_constant_soil_carbon_density_data_by_land_use = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "SOIL_CARBON_DATA_REGIONSXLAND",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": _subscript_dict["LANDS_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": _subscript_dict["LANDS_I"],
    },
    "_ext_constant_soil_carbon_density_data_by_land_use",
)


@component.add(
    name="SWITCH_AFFORESTATION_SP",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_afforestation_sp"},
)
def switch_afforestation_sp():
    """
    0: deactivate policy the scenario parameter 1: Activate the scenario parameter
    """
    return _ext_constant_switch_afforestation_sp()


_ext_constant_switch_afforestation_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_SWITCH_AFFORESTATION_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_switch_afforestation_sp",
)


@component.add(
    name="SWITCH_CROPLAND_PROTECTION_SP",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_cropland_protection_sp"},
)
def switch_cropland_protection_sp():
    """
    0: deactivate policy the scenario parameter 1: Activate the scenario parameter
    """
    return _ext_constant_switch_cropland_protection_sp()


_ext_constant_switch_cropland_protection_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_SWITCH_CROPLAND_PROTECTION_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_switch_cropland_protection_sp",
)


@component.add(
    name="SWITCH_DIET_CHANGE_SP",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_diet_change_sp"},
)
def switch_diet_change_sp():
    """
    0: deactivate policy the scenario parameter 1: Activate the scenario parameter
    """
    return _ext_constant_switch_diet_change_sp()


_ext_constant_switch_diet_change_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "SWITCH_DIET_CHANGE_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_switch_diet_change_sp",
)


@component.add(
    name="SWITCH_EFFECT_OIL_AND_GAS_ON_AGRICULTURE_SP",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_switch_effect_oil_and_gas_on_agriculture_sp"
    },
)
def switch_effect_oil_and_gas_on_agriculture_sp():
    """
    0: deactivate policy the scenario parameter 1: Activate the scenario parameter
    """
    return _ext_constant_switch_effect_oil_and_gas_on_agriculture_sp()


_ext_constant_switch_effect_oil_and_gas_on_agriculture_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "SWITCH_EFFECT_OIL_AND_GAS_ON_AGRICULTURE_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_switch_effect_oil_and_gas_on_agriculture_sp",
)


@component.add(
    name="SWITCH_FOREST_PLANTATIONS_SP",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_forest_plantations_sp"},
)
def switch_forest_plantations_sp():
    """
    0: deactivate policy the scenario parameter , increase of plantations land driven only by trends 1: Activate the scenario parameter
    """
    return _ext_constant_switch_forest_plantations_sp()


_ext_constant_switch_forest_plantations_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_SWITCH_FOREST_PLANTATIONS_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_switch_forest_plantations_sp",
)


@component.add(
    name="SWITCH_FORESTRY_SELF_SUFFICIENCY_SP",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_forestry_self_sufficiency_sp"},
)
def switch_forestry_self_sufficiency_sp():
    """
    IF =1 the policy of forest suficiency starts, regions increase the share of self consumption of wood
    """
    return _ext_constant_switch_forestry_self_sufficiency_sp()


_ext_constant_switch_forestry_self_sufficiency_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "SWITCH_FORESTRY_SELF_SUFFICIENCY_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_switch_forestry_self_sufficiency_sp",
)


@component.add(
    name="SWITCH_GRASSLAND_PROTECTION_SP",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_grassland_protection_sp"},
)
def switch_grassland_protection_sp():
    """
    0: deactivate policy the scenario parameter 1: Activate the scenario parameter
    """
    return _ext_constant_switch_grassland_protection_sp()


_ext_constant_switch_grassland_protection_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_SWITCH_GRASSLAND_PROTECTION_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_switch_grassland_protection_sp",
)


@component.add(
    name="SWITCH_INDUSTRIAL_AGRICULTURE_SP",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_industrial_agriculture_sp"},
)
def switch_industrial_agriculture_sp():
    """
    policy on or off
    """
    return _ext_constant_switch_industrial_agriculture_sp()


_ext_constant_switch_industrial_agriculture_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_SWITCH_INDUSTRIAL_AGRICULTURE_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_switch_industrial_agriculture_sp",
)


@component.add(
    name="SWITCH_LAND_PRODUCTS_GLOBAL_POOL_SP",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_land_products_global_pool_sp"},
)
def switch_land_products_global_pool_sp():
    """
    0: deactivate policy the scenario parameter 1: Activate the scenario parameter
    """
    return _ext_constant_switch_land_products_global_pool_sp()


_ext_constant_switch_land_products_global_pool_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "SWITCH_LAND_PRODUCTS_GLOBAL_POOL_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_switch_land_products_global_pool_sp",
)


@component.add(
    name="SWITCH_MANAGED_FOREST_PROTECTION_SP",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_managed_forest_protection_sp"},
)
def switch_managed_forest_protection_sp():
    """
    0: deactivate policy the scenario parameter 1: Activate the scenario parameter
    """
    return _ext_constant_switch_managed_forest_protection_sp()


_ext_constant_switch_managed_forest_protection_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_SWITCH_MANAGED_FOREST_PROTECTION_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_switch_managed_forest_protection_sp",
)


@component.add(
    name="SWITCH_NATURAL_LAND_PROTECTION_SP",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_natural_land_protection_sp"},
)
def switch_natural_land_protection_sp():
    """
    0: deactivate policy the scenario parameter 1: Activate the scenario parameter
    """
    return _ext_constant_switch_natural_land_protection_sp()


_ext_constant_switch_natural_land_protection_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_YEAR_INITIAL_NATURAL_LAND_PROTECTION_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_switch_natural_land_protection_sp",
)


@component.add(
    name="SWITCH_POLICY_LAND_PROTECTION_FROM_SOLAR_PV_SP",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_switch_policy_land_protection_from_solar_pv_sp"
    },
)
def switch_policy_land_protection_from_solar_pv_sp():
    """
    0: deactivate policy the scenario parameter 1: Activate the scenario parameter
    """
    return _ext_constant_switch_policy_land_protection_from_solar_pv_sp()


_ext_constant_switch_policy_land_protection_from_solar_pv_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "SWITCH_POLICY_LAND_PROTECTION_FROM_SOLAR_PV_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_switch_policy_land_protection_from_solar_pv_sp",
)


@component.add(
    name="SWITCH_POLICY_MAXIMUM_SHARE_SOLAR_URBAN_SP",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_switch_policy_maximum_share_solar_urban_sp"
    },
)
def switch_policy_maximum_share_solar_urban_sp():
    """
    0: deactivate policy the scenario parameter 1: Activate the scenario parameter
    """
    return _ext_constant_switch_policy_maximum_share_solar_urban_sp()


_ext_constant_switch_policy_maximum_share_solar_urban_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "SWITCH_SOLAR_LAND_FROM_OTHERS*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_switch_policy_maximum_share_solar_urban_sp",
)


@component.add(
    name="SWITCH_PRIMARY_FOREST_PROTECTION_SP",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_primary_forest_protection_sp"},
)
def switch_primary_forest_protection_sp():
    """
    0: deactivate policy the scenario parameter 1: Activate the scenario parameter
    """
    return _ext_constant_switch_primary_forest_protection_sp()


_ext_constant_switch_primary_forest_protection_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_SWITCH_PRIMARY_FOREST_PROTECTION_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_switch_primary_forest_protection_sp",
)


@component.add(
    name="SWITCH_REGENERATIVE_AGRICULTURE_SP",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_regenerative_agriculture_sp"},
)
def switch_regenerative_agriculture_sp():
    """
    policy on or off
    """
    return _ext_constant_switch_regenerative_agriculture_sp()


_ext_constant_switch_regenerative_agriculture_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_SWITCH_REGENERATIVE_AGRICULTURE_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_switch_regenerative_agriculture_sp",
)


@component.add(
    name="SWITCH_SOIL_MANAGEMENT_IN_GRASSLANDS_SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="Normal",
)
def switch_soil_management_in_grasslands_sp():
    """
    IF switch_between_wiliam_and_constant_outreal=1---> soil management in grasslands policy is applied IF switch_between_wiliam_and_constant_outreal=0---> soil management in grasslands policy is not applied
    """
    return 0


@component.add(
    name="SWITCH_SOLAR_LAND_FROM_OTHERS_SP",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_solar_land_from_others_sp"},
)
def switch_solar_land_from_others_sp():
    """
    0: deactivate policy the scenario parameter 1: Activate the scenario parameter
    """
    return _ext_constant_switch_solar_land_from_others_sp()


_ext_constant_switch_solar_land_from_others_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "SWITCH_SOLAR_LAND_FROM_OTHERS*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_switch_solar_land_from_others_sp",
)


@component.add(
    name="SWITCH_URBAN_LAND_DENSITY_SP",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_urban_land_density_sp"},
)
def switch_urban_land_density_sp():
    """
    IF switch_between_wiliam_and_constant_outreal=1---> urban land density policy is applied IF switch_between_wiliam_and_constant_outreal=0---> urban land density policy is not applied
    """
    return _ext_constant_switch_urban_land_density_sp()


_ext_constant_switch_urban_land_density_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "SWITCH_URBAN_LAND_DENSITY_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_switch_urban_land_density_sp",
)


@component.add(
    name="SWITCH_WATER_EFFICIENCY_SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="Normal",
)
def switch_water_efficiency_sp():
    """
    IF switch_between_wiliam_and_constant_outreal=1---> water efficiency policy is applied IF switch_between_wiliam_and_constant_outreal=0---> water efficiency policy is not applied
    """
    return 1


@component.add(
    name="TIME_HISTORICAL_DATA_LAND_MODULE",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_time_historical_data_land_module"},
)
def time_historical_data_land_module():
    """
    time of hostorical data
    """
    return _ext_constant_time_historical_data_land_module()


_ext_constant_time_historical_data_land_module = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "TIME_HISTORICAL_DATA_LAND_MODULE",
    {},
    _root,
    {},
    "_ext_constant_time_historical_data_land_module",
)


@component.add(
    name="TIME_OF_TRANSITION_TO_REGENERATIVE_AGRICULTURE",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_time_of_transition_to_regenerative_agriculture"
    },
)
def time_of_transition_to_regenerative_agriculture():
    return _ext_constant_time_of_transition_to_regenerative_agriculture()


_ext_constant_time_of_transition_to_regenerative_agriculture = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_OF_TRANSITION_TO_REGENERATIVE_AGRICULTURE*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_time_of_transition_to_regenerative_agriculture",
)


@component.add(
    name="TRANSFORMATION_MATRICES_REGIONS_TO_ZONES",
    subscripts=["REGIONS_9_I", "CLIMATIC_ZONES_I", "LANDS_I"],
    comp_type="Constant",
    comp_subtype="External, Normal",
    depends_on={
        "__external__": "_ext_constant_transformation_matrices_regions_to_zones"
    },
)
def transformation_matrices_regions_to_zones():
    """
    GET_DIRECT_CONSTANTS('model_parameters/land_and_water/land_and_water_parame ters.xlsx', 'transformation_matrices' , 'MATRIX_REGIONS_TO_ZONES_SNOW_ICE_WATERBODIES_9_R' )
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "CLIMATIC_ZONES_I": _subscript_dict["CLIMATIC_ZONES_I"],
            "LANDS_I": _subscript_dict["LANDS_I"],
        },
        ["REGIONS_9_I", "CLIMATIC_ZONES_I", "LANDS_I"],
    )
    def_subs = xr.zeros_like(value, dtype=bool)
    def_subs.loc[:, :, ["CROPLAND_RAINFED"]] = True
    def_subs.loc[:, :, ["CROPLAND_IRRIGATED"]] = True
    def_subs.loc[:, :, ["FOREST_MANAGED"]] = True
    def_subs.loc[:, :, ["FOREST_PRIMARY"]] = True
    def_subs.loc[:, :, ["FOREST_PLANTATIONS"]] = True
    def_subs.loc[:, :, ["SHRUBLAND"]] = True
    def_subs.loc[:, :, ["WETLAND"]] = True
    def_subs.loc[:, :, ["URBAN_LAND"]] = True
    def_subs.loc[:, :, ["SOLAR_LAND"]] = True
    def_subs.loc[:, :, ["OTHER_LAND"]] = True
    def_subs.loc[:, :, ["GRASSLAND"]] = True
    value.values[
        def_subs.values
    ] = _ext_constant_transformation_matrices_regions_to_zones().values[def_subs.values]
    value.loc[:, :, ["SNOW_ICE_WATERBODIES"]] = 0
    return value


_ext_constant_transformation_matrices_regions_to_zones = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "transformation_matrices",
    "MATRIX_REGIONS_TO_ZONES_CROPLAND_RAINFED_9_R",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "CLIMATIC_ZONES_I": _subscript_dict["CLIMATIC_ZONES_I"],
        "LANDS_I": ["CROPLAND_RAINFED"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "CLIMATIC_ZONES_I": _subscript_dict["CLIMATIC_ZONES_I"],
        "LANDS_I": _subscript_dict["LANDS_I"],
    },
    "_ext_constant_transformation_matrices_regions_to_zones",
)

_ext_constant_transformation_matrices_regions_to_zones.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "transformation_matrices",
    "MATRIX_REGIONS_TO_ZONES_CROPLAND_IRRIGATED_9_R",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "CLIMATIC_ZONES_I": _subscript_dict["CLIMATIC_ZONES_I"],
        "LANDS_I": ["CROPLAND_IRRIGATED"],
    },
)

_ext_constant_transformation_matrices_regions_to_zones.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "transformation_matrices",
    "MATRIX_REGIONS_TO_ZONES_FOREST_MANAGED_9_R",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "CLIMATIC_ZONES_I": _subscript_dict["CLIMATIC_ZONES_I"],
        "LANDS_I": ["FOREST_MANAGED"],
    },
)

_ext_constant_transformation_matrices_regions_to_zones.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "transformation_matrices",
    "MATRIX_REGIONS_TO_ZONES_FOREST_PRIMARY_9_R",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "CLIMATIC_ZONES_I": _subscript_dict["CLIMATIC_ZONES_I"],
        "LANDS_I": ["FOREST_PRIMARY"],
    },
)

_ext_constant_transformation_matrices_regions_to_zones.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "transformation_matrices",
    "MATRIX_REGIONS_TO_ZONES_FOREST_PLANTATIONS_9_R",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "CLIMATIC_ZONES_I": _subscript_dict["CLIMATIC_ZONES_I"],
        "LANDS_I": ["FOREST_PLANTATIONS"],
    },
)

_ext_constant_transformation_matrices_regions_to_zones.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "transformation_matrices",
    "MATRIX_REGIONS_TO_ZONES_SHRUBLAND_9_R",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "CLIMATIC_ZONES_I": _subscript_dict["CLIMATIC_ZONES_I"],
        "LANDS_I": ["SHRUBLAND"],
    },
)

_ext_constant_transformation_matrices_regions_to_zones.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "transformation_matrices",
    "MATRIX_REGIONS_TO_ZONES_WETLAND_9_R",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "CLIMATIC_ZONES_I": _subscript_dict["CLIMATIC_ZONES_I"],
        "LANDS_I": ["WETLAND"],
    },
)

_ext_constant_transformation_matrices_regions_to_zones.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "transformation_matrices",
    "MATRIX_REGIONS_TO_ZONES_URBAN_LAND_9_R",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "CLIMATIC_ZONES_I": _subscript_dict["CLIMATIC_ZONES_I"],
        "LANDS_I": ["URBAN_LAND"],
    },
)

_ext_constant_transformation_matrices_regions_to_zones.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "transformation_matrices",
    "MATRIX_REGIONS_TO_ZONES_SOLAR_LAND_9_R",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "CLIMATIC_ZONES_I": _subscript_dict["CLIMATIC_ZONES_I"],
        "LANDS_I": ["SOLAR_LAND"],
    },
)

_ext_constant_transformation_matrices_regions_to_zones.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "transformation_matrices",
    "MATRIX_REGIONS_TO_ZONES_OTHER_LAND_9_R",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "CLIMATIC_ZONES_I": _subscript_dict["CLIMATIC_ZONES_I"],
        "LANDS_I": ["OTHER_LAND"],
    },
)

_ext_constant_transformation_matrices_regions_to_zones.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "transformation_matrices",
    "MATRIX_REGIONS_TO_ZONES_GRASSLAND_9_R",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "CLIMATIC_ZONES_I": _subscript_dict["CLIMATIC_ZONES_I"],
        "LANDS_I": ["GRASSLAND"],
    },
)


@component.add(
    name="TRANSFORMATION_MATRICES_ZONES_TO_REGIONS",
    subscripts=["CLIMATIC_ZONES_I", "REGIONS_9_I", "LANDS_I"],
    comp_type="Constant",
    comp_subtype="External, Normal",
    depends_on={
        "__external__": "_ext_constant_transformation_matrices_zones_to_regions"
    },
)
def transformation_matrices_zones_to_regions():
    """
    GET_DIRECT_CONSTANTS('model_parameters/land_and_water/land_and_water_parame ters.xlsx', 'transformation_matrices' , 'MATRIX_REGIONS_TO_ZONES_SNOW_ICE_WATERBODIES_9_R' )
    """
    value = xr.DataArray(
        np.nan,
        {
            "CLIMATIC_ZONES_I": _subscript_dict["CLIMATIC_ZONES_I"],
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "LANDS_I": _subscript_dict["LANDS_I"],
        },
        ["CLIMATIC_ZONES_I", "REGIONS_9_I", "LANDS_I"],
    )
    def_subs = xr.zeros_like(value, dtype=bool)
    def_subs.loc[:, :, ["CROPLAND_RAINFED"]] = True
    def_subs.loc[:, :, ["CROPLAND_IRRIGATED"]] = True
    def_subs.loc[:, :, ["FOREST_MANAGED"]] = True
    def_subs.loc[:, :, ["FOREST_PRIMARY"]] = True
    def_subs.loc[:, :, ["FOREST_PLANTATIONS"]] = True
    def_subs.loc[:, :, ["SHRUBLAND"]] = True
    def_subs.loc[:, :, ["WETLAND"]] = True
    def_subs.loc[:, :, ["URBAN_LAND"]] = True
    def_subs.loc[:, :, ["SOLAR_LAND"]] = True
    def_subs.loc[:, :, ["OTHER_LAND"]] = True
    value.values[
        def_subs.values
    ] = _ext_constant_transformation_matrices_zones_to_regions().values[def_subs.values]
    value.loc[:, :, ["SNOW_ICE_WATERBODIES"]] = 0
    return value


_ext_constant_transformation_matrices_zones_to_regions = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "transformation_matrices",
    "MATRIX_ZONES_TO_REGIONS_CROPLAND_RAINFED_8_Z",
    {
        "CLIMATIC_ZONES_I": _subscript_dict["CLIMATIC_ZONES_I"],
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": ["CROPLAND_RAINFED"],
    },
    _root,
    {
        "CLIMATIC_ZONES_I": _subscript_dict["CLIMATIC_ZONES_I"],
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": _subscript_dict["LANDS_I"],
    },
    "_ext_constant_transformation_matrices_zones_to_regions",
)

_ext_constant_transformation_matrices_zones_to_regions.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "transformation_matrices",
    "MATRIX_ZONES_TO_REGIONS_CROPLAND_IRRIGATED_8_Z",
    {
        "CLIMATIC_ZONES_I": _subscript_dict["CLIMATIC_ZONES_I"],
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": ["CROPLAND_IRRIGATED"],
    },
)

_ext_constant_transformation_matrices_zones_to_regions.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "transformation_matrices",
    "MATRIX_ZONES_TO_REGIONS_FOREST_MANAGED_8_Z",
    {
        "CLIMATIC_ZONES_I": _subscript_dict["CLIMATIC_ZONES_I"],
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": ["FOREST_MANAGED"],
    },
)

_ext_constant_transformation_matrices_zones_to_regions.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "transformation_matrices",
    "MATRIX_ZONES_TO_REGIONS_FOREST_PRIMARY_8_Z",
    {
        "CLIMATIC_ZONES_I": _subscript_dict["CLIMATIC_ZONES_I"],
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": ["FOREST_PRIMARY"],
    },
)

_ext_constant_transformation_matrices_zones_to_regions.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "transformation_matrices",
    "MATRIX_ZONES_TO_REGIONS_FOREST_PLANTATIONS_8_Z",
    {
        "CLIMATIC_ZONES_I": _subscript_dict["CLIMATIC_ZONES_I"],
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": ["FOREST_PLANTATIONS"],
    },
)

_ext_constant_transformation_matrices_zones_to_regions.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "transformation_matrices",
    "MATRIX_ZONES_TO_REGIONS_SHRUBLAND_8_Z",
    {
        "CLIMATIC_ZONES_I": _subscript_dict["CLIMATIC_ZONES_I"],
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": ["SHRUBLAND"],
    },
)

_ext_constant_transformation_matrices_zones_to_regions.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "transformation_matrices",
    "MATRIX_ZONES_TO_REGIONS_WETLAND_8_Z",
    {
        "CLIMATIC_ZONES_I": _subscript_dict["CLIMATIC_ZONES_I"],
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": ["WETLAND"],
    },
)

_ext_constant_transformation_matrices_zones_to_regions.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "transformation_matrices",
    "MATRIX_ZONES_TO_REGIONS_URBAN_LAND_8_Z",
    {
        "CLIMATIC_ZONES_I": _subscript_dict["CLIMATIC_ZONES_I"],
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": ["URBAN_LAND"],
    },
)

_ext_constant_transformation_matrices_zones_to_regions.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "transformation_matrices",
    "MATRIX_ZONES_TO_REGIONS_SOLAR_LAND_8_Z",
    {
        "CLIMATIC_ZONES_I": _subscript_dict["CLIMATIC_ZONES_I"],
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": ["SOLAR_LAND"],
    },
)

_ext_constant_transformation_matrices_zones_to_regions.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "transformation_matrices",
    "MATRIX_ZONES_TO_REGIONS_OTHER_LAND_8_Z",
    {
        "CLIMATIC_ZONES_I": _subscript_dict["CLIMATIC_ZONES_I"],
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": ["OTHER_LAND"],
    },
)


@component.add(
    name="TRENDS_OF_LAND_USE_DEMAND",
    units="km2/Year",
    subscripts=["REGIONS_9_I", "LANDS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_trends_of_land_use_demand"},
)
def trends_of_land_use_demand():
    """
    GET_DIRECT_CONSTANTS('model_parameters/land_and_water/land_and_water.xlsx', 'land_uses' , 'TREND_CROPLAND_RAINFED_BY_REGION') GET_DIRECT_CONSTANTS('model_parameters/land_and_water/land_and_water.xlsx', 'land_uses' , 'TREND_CROPLAND_IRRIGATED_BY_REGION' ) GET_DIRECT_CONSTANTS('model_parameters/land_and_water/land_and_water.xlsx', 'land_uses' , 'TREND_AFFORESTATION_BY_REGION' ) GET_DIRECT_CONSTANTS('model_parameters/land_and_water/land_and_water.xlsx', 'land_uses' ,'TREND_FOREST_PLANTATIONS_BY_REGION') GET_DIRECT_CONSTANTS('model_parameters/land_and_water/land_and_water.xlsx', 'land_uses' , 'TREND_GRASSLAND_BY_REGION' ) GET_DIRECT_CONSTANTS('model_parameters/land_and_water/land_and_water.xlsx', 'land_uses' , 'TREND_URBAN_LAND_BY_REGION' ) GET_DIRECT_CONSTANTS('model_parameters/land_and_water/land_and_water_parame ters.xlsx', 'land_uses' , 'TREND_SOLAR_LAND_BY_REGION' )
    """
    return _ext_constant_trends_of_land_use_demand()


_ext_constant_trends_of_land_use_demand = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "TRENDS_OF_LAND_USE_DEMAND_BY_REGION",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": _subscript_dict["LANDS_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": _subscript_dict["LANDS_I"],
    },
    "_ext_constant_trends_of_land_use_demand",
)


@component.add(
    name="TRENDS_OF_YIELD_CHANGE_R_AND_I",
    units="t/(km2*Year*Year)",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_trends_of_yield_change_r_and_i"},
)
def trends_of_yield_change_r_and_i():
    return _ext_constant_trends_of_yield_change_r_and_i()


_ext_constant_trends_of_yield_change_r_and_i = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TRENDS_OF_YIELD_CHANGE_R_AND_I",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
    },
    "_ext_constant_trends_of_yield_change_r_and_i",
)


@component.add(
    name="VARIATION_LINEAR_BLUE_WATER_REGION_SECT",
    units="hm3",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_variation_linear_blue_water_region_sect"
    },
)
def variation_linear_blue_water_region_sect():
    """
    Load the variation of the Blue Water values, for the 35 Regions and 62 Sectors. Data from Ercin and Hoekstra (2014): Water footprint scenarios for 2050: A global analysis.Table 7, Scenario S4.
    """
    return _ext_constant_variation_linear_blue_water_region_sect()


_ext_constant_variation_linear_blue_water_region_sect = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Water",
    "dBlue",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
    "_ext_constant_variation_linear_blue_water_region_sect",
)


@component.add(
    name="VARIATION_LINEAR_GREEN_WATER_REGION_SECT",
    units="hm3",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_variation_linear_green_water_region_sect"
    },
)
def variation_linear_green_water_region_sect():
    """
    Load the variation of the Green Water values, for the 35 Regions and 62 Sectors. Data from Ercin and Hoekstra (2014): Water footprint scenarios for 2050: A global analysis.Table 7, Scenario S4.
    """
    return _ext_constant_variation_linear_green_water_region_sect()


_ext_constant_variation_linear_green_water_region_sect = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Water",
    "dGreen",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
    "_ext_constant_variation_linear_green_water_region_sect",
)


@component.add(
    name="VEGETATION_CARBON_DENSITY_DATA_BY_LAND_USE",
    units="tC/ha",
    subscripts=["REGIONS_9_I", "LANDS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_vegetation_carbon_density_data_by_land_use"
    },
)
def vegetation_carbon_density_data_by_land_use():
    """
    Vegetation carbon stock data (vegetation carbon database) SOC before: Soil carbon stock density data (soil carbon database) before conversion, and based also in assumptions for "land use factors" (current trends). Source: Assumed carbon stock in GCAM land use module. Van de Ven et al. 2021,.The potential land requirements and related land use change emissions of solar energy Notes: Vegetation in cropland, wetland and snow-ice-waterbodies data should be reviewed and improved. In the case of waterbodies soil carbon stock, and wetland carbon data, the numbers should be corrected in the future. For this version their area is cte so this information is not used.
    """
    return _ext_constant_vegetation_carbon_density_data_by_land_use()


_ext_constant_vegetation_carbon_density_data_by_land_use = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "VEGETATION_CARBON_DATA_REGIONSXLAND",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": _subscript_dict["LANDS_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": _subscript_dict["LANDS_I"],
    },
    "_ext_constant_vegetation_carbon_density_data_by_land_use",
)


@component.add(
    name="VERTICAL_LAND_MOVEMENT",
    units="m/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_vertical_land_movement"},
)
def vertical_land_movement():
    """
    the vertical land movement is a generic term used to describe several processes affecting the elevation at a given location (tectonic movements, subsidence, ground water extraction) that cause the land to move up or down.
    """
    return _ext_constant_vertical_land_movement()


_ext_constant_vertical_land_movement = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "VI_CONSTANT*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_vertical_land_movement",
)


@component.add(
    name="WBS_PLUS_BIOMASS_EXANSION_FACTOR_FOREST",
    units="t/m3",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_wbs_plus_biomass_exansion_factor_forest"
    },
)
def wbs_plus_biomass_exansion_factor_forest():
    """
    wbs plus biomass exansion factor forest
    """
    return _ext_constant_wbs_plus_biomass_exansion_factor_forest()


_ext_constant_wbs_plus_biomass_exansion_factor_forest = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "forest",
    "WBS_PLUS_BIOMASS_EXANSION_FACTOR_FOREST*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_wbs_plus_biomass_exansion_factor_forest",
)


@component.add(
    name="WIDTH_OF_CROPS_DISTRIBUTION_AMONG_USES_SP",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def width_of_crops_distribution_among_uses_sp():
    """
    WIDTH_OF_CROPS_DISTRIBUTION_AMONG_USES
    """
    return xr.DataArray(
        1,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
        },
        ["REGIONS_9_I", "LAND_PRODUCTS_I"],
    )


@component.add(
    name="WIDTH_OF_FORESTRY_PRODUCTS_DISTRIBUTION_AMONG_USES_SP",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def width_of_forestry_products_distribution_among_uses_sp():
    """
    WIDTH_OF_FORESTRY_PRODUCTS_DISTRIBUTION_AMONG_USES
    """
    return xr.DataArray(
        1, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
    )


@component.add(
    name="WIDTH_OF_LAND_PRODUCTS_DISTRIBUTION_AMONG_REGIONS_SP",
    units="DMNL",
    subscripts=["LAND_PRODUCTS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_width_of_land_products_distribution_among_regions_sp"
    },
)
def width_of_land_products_distribution_among_regions_sp():
    """
    WIDTH_OF_LAND_PRODUCTS_DISTRIBUTION_AMONG_REGIONS
    """
    return _ext_constant_width_of_land_products_distribution_among_regions_sp()


_ext_constant_width_of_land_products_distribution_among_regions_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "WIDTH_OF_LAND_PRODUCTS_DISTRIBUTION_AMONG_REGIONS",
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"]},
    _root,
    {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"]},
    "_ext_constant_width_of_land_products_distribution_among_regions_sp",
)


@component.add(
    name="WILLETT_DIET_PATTERNS_OF_POLICY_DIETS_SP",
    units="kg/(Year*people)",
    subscripts=["REGIONS_9_I", "FOODS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_willett_diet_patterns_of_policy_diets_sp"
    },
)
def willett_diet_patterns_of_policy_diets_sp():
    """
    Willett policy diet
    """
    return _ext_constant_willett_diet_patterns_of_policy_diets_sp()


_ext_constant_willett_diet_patterns_of_policy_diets_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "WILLET_DIET_PATTERN_OF_POLICY_DIETS_SP",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "FOODS_I": _subscript_dict["FOODS_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "FOODS_I": _subscript_dict["FOODS_I"],
    },
    "_ext_constant_willett_diet_patterns_of_policy_diets_sp",
)


@component.add(
    name="WOOD_DENSITY_BY_REGION",
    units="t/m3",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_wood_density_by_region"},
)
def wood_density_by_region():
    """
    wood density by region
    """
    return _ext_constant_wood_density_by_region()


_ext_constant_wood_density_by_region = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "forest",
    "WOOD_DENSITY_BY_REGION*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_wood_density_by_region",
)


@component.add(
    name="WOOD_FUEL_PRODUCTION",
    units="t/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_wood_fuel_production",
        "__data__": "_ext_data_wood_fuel_production",
        "time": 1,
    },
)
def wood_fuel_production():
    """
    wood fuel production for energy by region
    """
    return _ext_data_wood_fuel_production(time())


_ext_data_wood_fuel_production = ExtData(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "diet",
    "TIME_WOOD",
    "WOOD_FUEL",
    "interpolate",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_data_wood_fuel_production",
)


@component.add(
    name="YEAR_FINAL_AFFORESTATION_SP",
    units="Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_year_final_afforestation_sp"},
)
def year_final_afforestation_sp():
    """
    Scenario parameter final year
    """
    return _ext_constant_year_final_afforestation_sp()


_ext_constant_year_final_afforestation_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_YEAR_FINAL_AFFORESTATION_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_year_final_afforestation_sp",
)


@component.add(
    name="YEAR_FINAL_CROPLAND_PROTECTION_SP",
    units="Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_year_final_cropland_protection_sp"},
)
def year_final_cropland_protection_sp():
    """
    Scenario parameter final year
    """
    return _ext_constant_year_final_cropland_protection_sp()


_ext_constant_year_final_cropland_protection_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_YEAR_FINAL_CROPLAND_PROTECTION_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_year_final_cropland_protection_sp",
)


@component.add(
    name="YEAR_FINAL_DIET_CHANGE_SP",
    units="Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_year_final_diet_change_sp"},
)
def year_final_diet_change_sp():
    """
    Scenario parameter final year
    """
    return _ext_constant_year_final_diet_change_sp()


_ext_constant_year_final_diet_change_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "YEAR_FINAL_DIET_CHANGE_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_year_final_diet_change_sp",
)


@component.add(
    name="YEAR_FINAL_EFFECT_OF_OIL_AND_GAS_ON_AGRICULTURE_SP",
    units="Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_year_final_effect_of_oil_and_gas_on_agriculture_sp"
    },
)
def year_final_effect_of_oil_and_gas_on_agriculture_sp():
    """
    Scenario parameter final year
    """
    return _ext_constant_year_final_effect_of_oil_and_gas_on_agriculture_sp()


_ext_constant_year_final_effect_of_oil_and_gas_on_agriculture_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "YEAR_FINAL_EFFECT_OIL_AND_GAS_ON_AGRICULTURE_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_year_final_effect_of_oil_and_gas_on_agriculture_sp",
)


@component.add(
    name="YEAR_FINAL_FOREST_PLANTATIONS_SP",
    units="Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_year_final_forest_plantations_sp"},
)
def year_final_forest_plantations_sp():
    """
    Scenario parameter final year
    """
    return _ext_constant_year_final_forest_plantations_sp()


_ext_constant_year_final_forest_plantations_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "YEAR_FINAL_FOREST_PLANTATIONS*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_year_final_forest_plantations_sp",
)


@component.add(
    name="YEAR_FINAL_FORESTRY_SELF_SUFFICIENCY_SP",
    units="Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_year_final_forestry_self_sufficiency_sp"
    },
)
def year_final_forestry_self_sufficiency_sp():
    """
    FORESTRY_SELF_SUFFICIENCY policy final year
    """
    return _ext_constant_year_final_forestry_self_sufficiency_sp()


_ext_constant_year_final_forestry_self_sufficiency_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "YEAR_FINAL_FORESTRY_SELF_SUFFICIENCY_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_year_final_forestry_self_sufficiency_sp",
)


@component.add(
    name="YEAR_FINAL_GRASSLAND_PROTECTION_SP",
    units="Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_year_final_grassland_protection_sp"},
)
def year_final_grassland_protection_sp():
    """
    Scenario parameter final year
    """
    return _ext_constant_year_final_grassland_protection_sp()


_ext_constant_year_final_grassland_protection_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_YEAR_FINAL_GRASSLAND_PROTECTION_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_year_final_grassland_protection_sp",
)


@component.add(
    name="YEAR_FINAL_INDUSTRIAL_AGRICULTURE_SP",
    units="Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_year_final_industrial_agriculture_sp"},
)
def year_final_industrial_agriculture_sp():
    """
    policy final year
    """
    return _ext_constant_year_final_industrial_agriculture_sp()


_ext_constant_year_final_industrial_agriculture_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_YEAR_FINAL_INDUSTRIAL_AGRICULTURE_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_year_final_industrial_agriculture_sp",
)


@component.add(
    name="YEAR_FINAL_LAND_PRODUCTS_GLOBAL_POOL_SP",
    units="Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_year_final_land_products_global_pool_sp"
    },
)
def year_final_land_products_global_pool_sp():
    """
    Scenario parameter final year
    """
    return _ext_constant_year_final_land_products_global_pool_sp()


_ext_constant_year_final_land_products_global_pool_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "YEAR_FINAL_LAND_PRODUCTS_GLOBAL_POOL_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_year_final_land_products_global_pool_sp",
)


@component.add(
    name="YEAR_FINAL_MANAGED_FOREST_PROTECTION_SP",
    units="Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_year_final_managed_forest_protection_sp"
    },
)
def year_final_managed_forest_protection_sp():
    """
    Scenario parameter final year
    """
    return _ext_constant_year_final_managed_forest_protection_sp()


_ext_constant_year_final_managed_forest_protection_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_YEAR_FINAL_MANAGED_FOREST_PROTECTION_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_year_final_managed_forest_protection_sp",
)


@component.add(
    name="YEAR_FINAL_NATURAL_LAND_PROTECTION_SP",
    units="Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_year_final_natural_land_protection_sp"},
)
def year_final_natural_land_protection_sp():
    """
    Scenario parameter final year
    """
    return _ext_constant_year_final_natural_land_protection_sp()


_ext_constant_year_final_natural_land_protection_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_YEAR_FINAL_NATURAL_LAND_PROTECTION_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_year_final_natural_land_protection_sp",
)


@component.add(
    name="YEAR_FINAL_PRIMARY_FOREST_PROTECTION_SP",
    units="Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_year_final_primary_forest_protection_sp"
    },
)
def year_final_primary_forest_protection_sp():
    """
    Scenario parameter final year
    """
    return _ext_constant_year_final_primary_forest_protection_sp()


_ext_constant_year_final_primary_forest_protection_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_YEAR_FINAL_PRIMARY_FOREST_PROTECTION_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_year_final_primary_forest_protection_sp",
)


@component.add(
    name="YEAR_FINAL_REGENERATIVE_AGRICULTURE_SP",
    units="Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_year_final_regenerative_agriculture_sp"},
)
def year_final_regenerative_agriculture_sp():
    """
    policy final year
    """
    return _ext_constant_year_final_regenerative_agriculture_sp()


_ext_constant_year_final_regenerative_agriculture_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_YEAR_FINAL_REGENERATIVE_AGRICULTURE_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_year_final_regenerative_agriculture_sp",
)


@component.add(
    name="YEAR_FINAL_SOIL_MANAGEMENT_IN_GRASSLANDS_SP",
    units="Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_year_final_soil_management_in_grasslands_sp"
    },
)
def year_final_soil_management_in_grasslands_sp():
    """
    soil management in grasslands policy final year
    """
    return _ext_constant_year_final_soil_management_in_grasslands_sp()


_ext_constant_year_final_soil_management_in_grasslands_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "YEAR_FINAL_SOIL_MANAGEMENT_GRASSLANDS_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_year_final_soil_management_in_grasslands_sp",
)


@component.add(
    name="YEAR_FINAL_SOLAR_LAND_FROM_OTHERS_SP",
    units="Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_year_final_solar_land_from_others_sp"},
)
def year_final_solar_land_from_others_sp():
    """
    Scenario parameter final year
    """
    return _ext_constant_year_final_solar_land_from_others_sp()


_ext_constant_year_final_solar_land_from_others_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "YEAR_FINAL_SOLAR_LAND_FROM_OTHERS*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_year_final_solar_land_from_others_sp",
)


@component.add(
    name="YEAR_FINAL_URBAN_LAND_DENSITY_SP",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_year_final_urban_land_density_sp"},
)
def year_final_urban_land_density_sp():
    """
    urban land density policy final year
    """
    return _ext_constant_year_final_urban_land_density_sp()


_ext_constant_year_final_urban_land_density_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "YEAR_FINAL_URBAN_LAND_DENSITY_SP",
    {},
    _root,
    {},
    "_ext_constant_year_final_urban_land_density_sp",
)


@component.add(
    name="YEAR_FINAL_WATER_EFFICIENCY_SP",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_year_final_water_efficiency_sp"},
)
def year_final_water_efficiency_sp():
    """
    YEAR_FINAL_WATER_EFFICIENCY_SP
    """
    return _ext_constant_year_final_water_efficiency_sp()


_ext_constant_year_final_water_efficiency_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "YEAR_FINAL_WATER_EFFICIENCY_SP*",
    {},
    _root,
    {},
    "_ext_constant_year_final_water_efficiency_sp",
)


@component.add(
    name="YEAR_INITIAL_AFFORESTATION_SP",
    units="Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_year_initial_afforestation_sp"},
)
def year_initial_afforestation_sp():
    """
    Scenario parameter intial year
    """
    return _ext_constant_year_initial_afforestation_sp()


_ext_constant_year_initial_afforestation_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_YEAR_INITIAL_AFFORESTATION_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_year_initial_afforestation_sp",
)


@component.add(
    name="YEAR_INITIAL_CROPLAND_PROTECTION_SP",
    units="Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_year_initial_cropland_protection_sp"},
)
def year_initial_cropland_protection_sp():
    """
    Scenario parameter intial year
    """
    return _ext_constant_year_initial_cropland_protection_sp()


_ext_constant_year_initial_cropland_protection_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_YEAR_INITIAL_CROPLAND_PROTECTION_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_year_initial_cropland_protection_sp",
)


@component.add(
    name="YEAR_INITIAL_DIET_CHANGE_SP",
    units="Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_year_initial_diet_change_sp"},
)
def year_initial_diet_change_sp():
    """
    Scenario parameter intial year
    """
    return _ext_constant_year_initial_diet_change_sp()


_ext_constant_year_initial_diet_change_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "YEAR_INITIAL_DIET_CHANGE_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_year_initial_diet_change_sp",
)


@component.add(
    name="YEAR_INITIAL_EFFECT_OF_OIL_AND_GAS_ON_AGRICULTURE_SP",
    units="Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_year_initial_effect_of_oil_and_gas_on_agriculture_sp"
    },
)
def year_initial_effect_of_oil_and_gas_on_agriculture_sp():
    """
    Scenario parameter intial year
    """
    return _ext_constant_year_initial_effect_of_oil_and_gas_on_agriculture_sp()


_ext_constant_year_initial_effect_of_oil_and_gas_on_agriculture_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "YEAR_INITIAL_EFFECT_OIL_AND_GAS_ON_AGRICULTURE_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_year_initial_effect_of_oil_and_gas_on_agriculture_sp",
)


@component.add(
    name="YEAR_INITIAL_FOREST_PLANTATIONS_SP",
    units="Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_year_initial_forest_plantations_sp"},
)
def year_initial_forest_plantations_sp():
    """
    Scenario parameter intial year
    """
    return _ext_constant_year_initial_forest_plantations_sp()


_ext_constant_year_initial_forest_plantations_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "YEAR_INITIAL_FOREST_PLANTATIONS*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_year_initial_forest_plantations_sp",
)


@component.add(
    name="YEAR_INITIAL_FORESTRY_SELF_SUFFICIENCY_SP",
    units="Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_year_initial_forestry_self_sufficiency_sp"
    },
)
def year_initial_forestry_self_sufficiency_sp():
    """
    FORESTRY_SELF_SUFFICIENCY policy initial year
    """
    return _ext_constant_year_initial_forestry_self_sufficiency_sp()


_ext_constant_year_initial_forestry_self_sufficiency_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "YEAR_INITIAL_FORESTRY_SELF_SUFFICIENCY_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_year_initial_forestry_self_sufficiency_sp",
)


@component.add(
    name="YEAR_INITIAL_GRASSLAND_PROTECTION_SP",
    units="Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_year_initial_grassland_protection_sp"},
)
def year_initial_grassland_protection_sp():
    """
    Scenario parameter intial year
    """
    return _ext_constant_year_initial_grassland_protection_sp()


_ext_constant_year_initial_grassland_protection_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_YEAR_INITIAL_GRASSLAND_PROTECTION_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_year_initial_grassland_protection_sp",
)


@component.add(
    name="YEAR_INITIAL_INDUSTRIAL_AGRICULTURE_SP",
    units="Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_year_initial_industrial_agriculture_sp"},
)
def year_initial_industrial_agriculture_sp():
    """
    policy intial year
    """
    return _ext_constant_year_initial_industrial_agriculture_sp()


_ext_constant_year_initial_industrial_agriculture_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_YEAR_INITIAL_INDUSTRIAL_AGRICULTURE_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_year_initial_industrial_agriculture_sp",
)


@component.add(
    name="YEAR_INITIAL_LAND_PRODUCTS_GLOBAL_POOL_SP",
    units="Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_year_initial_land_products_global_pool_sp"
    },
)
def year_initial_land_products_global_pool_sp():
    """
    Scenario parameter intial year
    """
    return _ext_constant_year_initial_land_products_global_pool_sp()


_ext_constant_year_initial_land_products_global_pool_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "YEAR_INITIAL_LAND_PRODUCTS_GLOBAL_POOL_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_year_initial_land_products_global_pool_sp",
)


@component.add(
    name="YEAR_INITIAL_MANAGED_FOREST_PROTECTION_SP",
    units="Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_year_initial_managed_forest_protection_sp"
    },
)
def year_initial_managed_forest_protection_sp():
    """
    Scenario parameter intial year
    """
    return _ext_constant_year_initial_managed_forest_protection_sp()


_ext_constant_year_initial_managed_forest_protection_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_YEAR_INITIAL_MANAGED_FOREST_PROTECTION_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_year_initial_managed_forest_protection_sp",
)


@component.add(
    name="YEAR_INITIAL_NATURAL_LAND_PROTECTION_SP",
    units="Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_year_initial_natural_land_protection_sp"
    },
)
def year_initial_natural_land_protection_sp():
    """
    Scenario parameter intial year
    """
    return _ext_constant_year_initial_natural_land_protection_sp()


_ext_constant_year_initial_natural_land_protection_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_YEAR_INITIAL_NATURAL_LAND_PROTECTION_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_year_initial_natural_land_protection_sp",
)


@component.add(
    name="YEAR_INITIAL_PRIMARY_FOREST_PROTECTION_SP",
    units="Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_year_initial_primary_forest_protection_sp"
    },
)
def year_initial_primary_forest_protection_sp():
    """
    Scenario parameter intial year
    """
    return _ext_constant_year_initial_primary_forest_protection_sp()


_ext_constant_year_initial_primary_forest_protection_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_YEAR_INITIAL_PRIMARY_FOREST_PROTECTION_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_year_initial_primary_forest_protection_sp",
)


@component.add(
    name="YEAR_INITIAL_REGENERATIVE_AGRICULTURE_SP",
    units="Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_year_initial_regenerative_agriculture_sp"
    },
)
def year_initial_regenerative_agriculture_sp():
    """
    policy initial year
    """
    return _ext_constant_year_initial_regenerative_agriculture_sp()


_ext_constant_year_initial_regenerative_agriculture_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_YEAR_INITIAL_REGENERATIVE_AGRICULTURE_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_year_initial_regenerative_agriculture_sp",
)


@component.add(
    name="YEAR_INITIAL_SOIL_MANAGEMENT_IN_GRASSLANDS_SP",
    units="Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_year_initial_soil_management_in_grasslands_sp"
    },
)
def year_initial_soil_management_in_grasslands_sp():
    """
    soil management in grasslands policy initial year
    """
    return _ext_constant_year_initial_soil_management_in_grasslands_sp()


_ext_constant_year_initial_soil_management_in_grasslands_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "YEAR_INITIAL_SOIL_MANAGEMENT_GRASSLANDS_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_year_initial_soil_management_in_grasslands_sp",
)


@component.add(
    name="YEAR_INITIAL_SOLAR_LAND_FROM_OTHERS_SP",
    units="Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_year_initial_solar_land_from_others_sp"},
)
def year_initial_solar_land_from_others_sp():
    """
    Scenario parameter intial year
    """
    return _ext_constant_year_initial_solar_land_from_others_sp()


_ext_constant_year_initial_solar_land_from_others_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "YEAR_INITIAL_SOLAR_LAND_FROM_OTHERS*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_year_initial_solar_land_from_others_sp",
)


@component.add(
    name="YEAR_INITIAL_URBAN_LAND_DENSITY_SP",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_year_initial_urban_land_density_sp"},
)
def year_initial_urban_land_density_sp():
    """
    urban land density policy initial year
    """
    return _ext_constant_year_initial_urban_land_density_sp()


_ext_constant_year_initial_urban_land_density_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "YEAR_INITIAL_URBAN_LAND_DENSITY_SP",
    {},
    _root,
    {},
    "_ext_constant_year_initial_urban_land_density_sp",
)


@component.add(
    name="YEAR_INITIAL_WATER_EFFICIENCY_SP",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_year_initial_water_efficiency_sp"},
)
def year_initial_water_efficiency_sp():
    """
    YEAR_INITIAL_WATER_EFFICIENCY_SP
    """
    return _ext_constant_year_initial_water_efficiency_sp()


_ext_constant_year_initial_water_efficiency_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "YEAR_INITIAL_WATER_EFFICIENCY_SP*",
    {},
    _root,
    {},
    "_ext_constant_year_initial_water_efficiency_sp",
)


@component.add(
    name="YIELDS_ALL_MANAGEMENT_2019",
    units="t/(km2*Year)",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_yields_all_management_2019"},
)
def yields_all_management_2019():
    return _ext_constant_yields_all_management_2019()


_ext_constant_yields_all_management_2019 = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "YIELDS_ALL_MANAGEMENTS_2019",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
    },
    "_ext_constant_yields_all_management_2019",
)
