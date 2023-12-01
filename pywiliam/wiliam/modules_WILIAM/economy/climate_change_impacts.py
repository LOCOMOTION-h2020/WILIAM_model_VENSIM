"""
Module economy.climate_change_impacts
Translated using PySD version 3.10.0
"""


@component.add(
    name="A_CAPITAL_STOCK_DAMAGE_FUNCTION",
    units="DMNL",
    subscripts=[
        "CLIMATE_HAZARDS_I",
        "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I",
        "REGIONS_35_I",
        "SECTORS_I",
    ],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_a_capital_stock_damage_function"},
)
def a_capital_stock_damage_function():
    """
    First parameter of the capital stock damage function. Calibrated by using data from Forzieri et al (2017). Data has been processed and extrapolations have been done for some regions and sectors.
    """
    return _ext_constant_a_capital_stock_damage_function()


_ext_constant_a_capital_stock_damage_function = ExtConstant(
    "model_parameters/economy/Climate_Change_Impacts_Economy.xlsx",
    "A_Damage_Function",
    "A_CAPITAL_STOCK_DAMAGE_FUNCTION_DROUGHT_MAXI",
    {
        "CLIMATE_HAZARDS_I": ["DROUGHT"],
        "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I": ["MAXI"],
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
    _root,
    {
        "CLIMATE_HAZARDS_I": _subscript_dict["CLIMATE_HAZARDS_I"],
        "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I": _subscript_dict[
            "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I"
        ],
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
    "_ext_constant_a_capital_stock_damage_function",
)

_ext_constant_a_capital_stock_damage_function.add(
    "model_parameters/economy/Climate_Change_Impacts_Economy.xlsx",
    "A_Damage_Function",
    "A_CAPITAL_STOCK_DAMAGE_FUNCTION_DROUGHT_MINI",
    {
        "CLIMATE_HAZARDS_I": ["DROUGHT"],
        "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I": ["MINI"],
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
)

_ext_constant_a_capital_stock_damage_function.add(
    "model_parameters/economy/Climate_Change_Impacts_Economy.xlsx",
    "A_Damage_Function",
    "A_CAPITAL_STOCK_DAMAGE_FUNCTION_DROUGHT_MEDIAN",
    {
        "CLIMATE_HAZARDS_I": ["DROUGHT"],
        "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I": ["MEDIAN"],
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
)

_ext_constant_a_capital_stock_damage_function.add(
    "model_parameters/economy/Climate_Change_Impacts_Economy.xlsx",
    "A_Damage_Function",
    "A_CAPITAL_STOCK_DAMAGE_FUNCTION_DROUGHT_AVERAGE",
    {
        "CLIMATE_HAZARDS_I": ["DROUGHT"],
        "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I": ["AVERAGE"],
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
)

_ext_constant_a_capital_stock_damage_function.add(
    "model_parameters/economy/Climate_Change_Impacts_Economy.xlsx",
    "A_Damage_Function",
    "A_CAPITAL_STOCK_DAMAGE_FUNCTION_FIRE_MAXI",
    {
        "CLIMATE_HAZARDS_I": ["FIRE"],
        "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I": ["MAXI"],
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
)

_ext_constant_a_capital_stock_damage_function.add(
    "model_parameters/economy/Climate_Change_Impacts_Economy.xlsx",
    "A_Damage_Function",
    "A_CAPITAL_STOCK_DAMAGE_FUNCTION_FIRE_MINI",
    {
        "CLIMATE_HAZARDS_I": ["FIRE"],
        "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I": ["MINI"],
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
)

_ext_constant_a_capital_stock_damage_function.add(
    "model_parameters/economy/Climate_Change_Impacts_Economy.xlsx",
    "A_Damage_Function",
    "A_CAPITAL_STOCK_DAMAGE_FUNCTION_FIRE_MEDIAN",
    {
        "CLIMATE_HAZARDS_I": ["FIRE"],
        "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I": ["MEDIAN"],
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
)

_ext_constant_a_capital_stock_damage_function.add(
    "model_parameters/economy/Climate_Change_Impacts_Economy.xlsx",
    "A_Damage_Function",
    "A_CAPITAL_STOCK_DAMAGE_FUNCTION_FIRE_AVERAGE",
    {
        "CLIMATE_HAZARDS_I": ["FIRE"],
        "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I": ["AVERAGE"],
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
)

_ext_constant_a_capital_stock_damage_function.add(
    "model_parameters/economy/Climate_Change_Impacts_Economy.xlsx",
    "A_Damage_Function",
    "A_CAPITAL_STOCK_DAMAGE_FUNCTION_HEATWAVES_MAXI",
    {
        "CLIMATE_HAZARDS_I": ["HEATWAVES"],
        "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I": ["MAXI"],
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
)

_ext_constant_a_capital_stock_damage_function.add(
    "model_parameters/economy/Climate_Change_Impacts_Economy.xlsx",
    "A_Damage_Function",
    "A_CAPITAL_STOCK_DAMAGE_FUNCTION_HEATWAVES_MINI",
    {
        "CLIMATE_HAZARDS_I": ["HEATWAVES"],
        "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I": ["MINI"],
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
)

_ext_constant_a_capital_stock_damage_function.add(
    "model_parameters/economy/Climate_Change_Impacts_Economy.xlsx",
    "A_Damage_Function",
    "A_CAPITAL_STOCK_DAMAGE_FUNCTION_HEATWAVES_MEDIAN",
    {
        "CLIMATE_HAZARDS_I": ["HEATWAVES"],
        "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I": ["MEDIAN"],
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
)

_ext_constant_a_capital_stock_damage_function.add(
    "model_parameters/economy/Climate_Change_Impacts_Economy.xlsx",
    "A_Damage_Function",
    "A_CAPITAL_STOCK_DAMAGE_FUNCTION_HEATWAVES_AVERAGE",
    {
        "CLIMATE_HAZARDS_I": ["HEATWAVES"],
        "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I": ["AVERAGE"],
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
)


@component.add(
    name="A_HEAT_STRESS_DAMAGE_FUNCTION",
    units="1/DegreesC",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_a_heat_stress_damage_function"},
)
def a_heat_stress_damage_function():
    """
    First parameter of the parabolic damage function. Calibrated by using data from Roson & Sartori (2015).
    """
    return _ext_constant_a_heat_stress_damage_function()


_ext_constant_a_heat_stress_damage_function = ExtConstant(
    "model_parameters/economy/Climate_Change_Impacts_Economy_2.xlsx",
    "Parameter_A_Heat_Stress",
    "A_HEAT_STRESS_DAMAGE_FUNCTION",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
    "_ext_constant_a_heat_stress_damage_function",
)


@component.add(
    name="A_VECTOR_BORNE_DISEASES_DAMAGE_FUNCTION",
    units="1/DegreesC",
    subscripts=["REGIONS_35_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_a_vector_borne_diseases_damage_function"
    },
)
def a_vector_borne_diseases_damage_function():
    """
    Parameter of the lineal vector borne diseases damage function. Estimated through using the data from Roson & Sartori (2015).
    """
    return _ext_constant_a_vector_borne_diseases_damage_function()


_ext_constant_a_vector_borne_diseases_damage_function = ExtConstant(
    "model_parameters/economy/Climate_Change_Impacts_Economy_2.xlsx",
    "Parameter_A_Vector_Borne_Dis",
    "A_VECTOR_BORNE_DISEASES_DAMAGE_FUNCTION*",
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    _root,
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    "_ext_constant_a_vector_borne_diseases_damage_function",
)


@component.add(
    name="auxiliar_for_climate_change_damage_rate_to_capital_stock_until_2015",
    units="DMNL",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={
        "_delayfixed_auxiliar_for_climate_change_damage_rate_to_capital_stock_until_2015": 1
    },
    other_deps={
        "_delayfixed_auxiliar_for_climate_change_damage_rate_to_capital_stock_until_2015": {
            "initial": {"time_step": 1},
            "step": {"climate_change_damage_rate_to_capital_stock_until_2015": 1},
        }
    },
)
def auxiliar_for_climate_change_damage_rate_to_capital_stock_until_2015():
    """
    Climate change damage rate of the stock of capital: auxiliar variable for calculating climate change damage as an incremental damage. The method is not mathematically exact, but the error tends to 0 when the TIME STEP decreases.
    """
    return (
        _delayfixed_auxiliar_for_climate_change_damage_rate_to_capital_stock_until_2015()
    )


_delayfixed_auxiliar_for_climate_change_damage_rate_to_capital_stock_until_2015 = DelayFixed(
    lambda: climate_change_damage_rate_to_capital_stock_until_2015(),
    lambda: time_step(),
    lambda: xr.DataArray(
        0,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "SECTORS_I": _subscript_dict["SECTORS_I"],
        },
        ["REGIONS_35_I", "SECTORS_I"],
    ),
    time_step,
    "_delayfixed_auxiliar_for_climate_change_damage_rate_to_capital_stock_until_2015",
)


@component.add(
    name="auxiliar_for_vector_borne_diseases_damage_function",
    subscripts=["REGIONS_35_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_auxiliar_for_vector_borne_diseases_damage_function": 1},
    other_deps={
        "_delayfixed_auxiliar_for_vector_borne_diseases_damage_function": {
            "initial": {"time_step": 1},
            "step": {"vector_borne_diseases_damage_function_until_2015": 1},
        }
    },
)
def auxiliar_for_vector_borne_diseases_damage_function():
    """
    Auxiliar variable aimed at calculating vector borne diseases incremental damage function
    """
    return _delayfixed_auxiliar_for_vector_borne_diseases_damage_function()


_delayfixed_auxiliar_for_vector_borne_diseases_damage_function = DelayFixed(
    lambda: vector_borne_diseases_damage_function_until_2015(),
    lambda: time_step(),
    lambda: xr.DataArray(
        0, {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]}, ["REGIONS_35_I"]
    ),
    time_step,
    "_delayfixed_auxiliar_for_vector_borne_diseases_damage_function",
)


@component.add(
    name="auxiliar_heat_stress_damage_function_until_2015",
    units="DMNL",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_auxiliar_heat_stress_damage_function_until_2015": 1},
    other_deps={
        "_delayfixed_auxiliar_heat_stress_damage_function_until_2015": {
            "initial": {"time_step": 1},
            "step": {"heat_stress_damage_function_until_2015": 1},
        }
    },
)
def auxiliar_heat_stress_damage_function_until_2015():
    """
    Auxiliar variable aimed at calculating heat stress incremental damage function. The method is not mathematically exact, but the error tends to 0 when the TIME STEP decreases.
    """
    return _delayfixed_auxiliar_heat_stress_damage_function_until_2015()


_delayfixed_auxiliar_heat_stress_damage_function_until_2015 = DelayFixed(
    lambda: heat_stress_damage_function_until_2015(),
    lambda: time_step(),
    lambda: xr.DataArray(
        0,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "SECTORS_I": _subscript_dict["SECTORS_I"],
        },
        ["REGIONS_35_I", "SECTORS_I"],
    ),
    time_step,
    "_delayfixed_auxiliar_heat_stress_damage_function_until_2015",
)


@component.add(
    name="auxiliar_variable_to_remove_extrapolations_of_droughts",
    units="DMNL",
    subscripts=[
        "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I",
        "REGIONS_35_I",
        "SECTORS_I",
    ],
    comp_type="Constant",
    comp_subtype="Normal",
)
def auxiliar_variable_to_remove_extrapolations_of_droughts():
    """
    This variable is used for doing some extrapolations related to sensitivity scenarios.
    """
    value = xr.DataArray(
        np.nan,
        {
            "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I": _subscript_dict[
                "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I"
            ],
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "SECTORS_I": _subscript_dict["SECTORS_I"],
        },
        ["CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I", "REGIONS_35_I", "SECTORS_I"],
    )
    value.loc[:, :, _subscript_dict["CLUSTER_AGRICULTURE_FISHING_FORESTRY"]] = 0
    value.loc[:, :, ["ELECTRICITY_OTHER"]] = 1
    value.loc[:, :, ["MANUFACTURE_CHEMICAL"]] = 1
    value.loc[:, :, _subscript_dict["CLUSTER_CONSTRUCTION_REAL_ESTATE"]] = 0
    value.loc[:, :, _subscript_dict["CLUSTER_EDUCATION_AND_HEALTH"]] = 1
    value.loc[:, :, ["DISTRIBUTION_ELECTRICITY"]] = 0
    value.loc[:, :, ["TRANSPORT_PIPELINE"]] = 0
    value.loc[:, :, ["ELECTRICITY_HYDRO"]] = 1
    value.loc[:, :, ["MANUFACTURE_METAL_PRODUCTS"]] = 1
    value.loc[:, :, _subscript_dict["CLUSTER_MINNING"]] = 1
    value.loc[:, :, ["ELECTRICITY_NUCLEAR"]] = 1
    value.loc[:, :, ["ELECTRICITY_OIL"]] = 1
    value.loc[:, :, _subscript_dict["CLUSTER_OTHER_ENERGY_ACTIVITIES"]] = 0
    value.loc[:, :, _subscript_dict["CLUSTER_OTHER_MANUFACTURES"]] = 0
    value.loc[:, :, _subscript_dict["CLUSTER_OTHER_SERVICE_SECTORS"]] = 0
    value.loc[:, :, ["PUBLIC_ADMINISTRATION"]] = 0
    value.loc[:, :, _subscript_dict["CLUSTER_QUARRYING"]] = 1
    value.loc[:, :, _subscript_dict["CLUSTER_REFINED_PRODUCTS_INDUSTRY"]] = 0
    value.loc[:, :, ["REFINING"]] = 1
    value.loc[:, :, _subscript_dict["CLUSTER_SOLAR_POWER_PLANTS"]] = 0
    value.loc[:, :, _subscript_dict["CLUSTER_TRANSPORT"]] = 0
    value.loc[:, :, ["WASTE_MANAGEMENT"]] = 1
    value.loc[:, :, ["ELECTRICITY_WIND"]] = 0
    value.loc[:, :, ["ELECTRICITY_COAL"]] = 1
    value.loc[:, :, ["ELECTRICITY_GAS"]] = 1
    value.loc[:, :, ["HYDROGEN_PRODUCTION"]] = 0
    value.loc[:, :, ["OTHER_SERVICES"]] = 1
    return value


@component.add(
    name="auxiliar_variable_to_remove_extrapolations_of_heatwaves",
    units="DMNL",
    subscripts=[
        "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I",
        "REGIONS_35_I",
        "SECTORS_I",
    ],
    comp_type="Constant",
    comp_subtype="Normal",
)
def auxiliar_variable_to_remove_extrapolations_of_heatwaves():
    """
    This variable is used for doing some extrapolations related to sensitivity scenarios.
    """
    value = xr.DataArray(
        np.nan,
        {
            "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I": _subscript_dict[
                "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I"
            ],
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "SECTORS_I": _subscript_dict["SECTORS_I"],
        },
        ["CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I", "REGIONS_35_I", "SECTORS_I"],
    )
    value.loc[:, :, _subscript_dict["CLUSTER_AGRICULTURE_FISHING_FORESTRY"]] = 0
    value.loc[:, :, ["ELECTRICITY_OTHER"]] = 1
    value.loc[:, :, ["MANUFACTURE_CHEMICAL"]] = 0
    value.loc[:, :, _subscript_dict["CLUSTER_CONSTRUCTION_REAL_ESTATE"]] = 0
    value.loc[:, :, _subscript_dict["CLUSTER_EDUCATION_AND_HEALTH"]] = 0
    value.loc[:, :, ["DISTRIBUTION_ELECTRICITY"]] = 0
    value.loc[:, :, ["TRANSPORT_PIPELINE"]] = 0
    value.loc[:, :, ["ELECTRICITY_HYDRO"]] = 0
    value.loc[:, :, ["MANUFACTURE_METAL_PRODUCTS"]] = 0
    value.loc[:, :, _subscript_dict["CLUSTER_MINNING"]] = 0
    value.loc[:, :, ["ELECTRICITY_NUCLEAR"]] = 1
    value.loc[:, :, ["ELECTRICITY_OIL"]] = 1
    value.loc[:, :, _subscript_dict["CLUSTER_OTHER_ENERGY_ACTIVITIES"]] = 0
    value.loc[:, :, _subscript_dict["CLUSTER_OTHER_MANUFACTURES"]] = 0
    value.loc[:, :, _subscript_dict["CLUSTER_OTHER_SERVICE_SECTORS"]] = 0
    value.loc[:, :, ["PUBLIC_ADMINISTRATION"]] = 0
    value.loc[:, :, _subscript_dict["CLUSTER_QUARRYING"]] = 0
    value.loc[:, :, _subscript_dict["CLUSTER_REFINED_PRODUCTS_INDUSTRY"]] = 0
    value.loc[:, :, ["REFINING"]] = 0
    value.loc[:, :, _subscript_dict["CLUSTER_SOLAR_POWER_PLANTS"]] = 0
    value.loc[:, :, _subscript_dict["CLUSTER_TRANSPORT"]] = 1
    value.loc[:, :, ["WASTE_MANAGEMENT"]] = 1
    value.loc[:, :, ["ELECTRICITY_WIND"]] = 0
    value.loc[:, :, ["ELECTRICITY_COAL"]] = 1
    value.loc[:, :, ["ELECTRICITY_GAS"]] = 1
    value.loc[:, :, ["HYDROGEN_PRODUCTION"]] = 0
    value.loc[:, :, ["OTHER_SERVICES"]] = 1
    return value


@component.add(
    name="auxiliar_variable_to_remove_extrapolations_of_wildfires",
    units="DMNL",
    subscripts=[
        "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I",
        "REGIONS_35_I",
        "SECTORS_I",
    ],
    comp_type="Constant",
    comp_subtype="Normal",
)
def auxiliar_variable_to_remove_extrapolations_of_wildfires():
    """
    This variable is used for doing some extrapolations related to sensitivity scenarios.
    """
    value = xr.DataArray(
        np.nan,
        {
            "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I": _subscript_dict[
                "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I"
            ],
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "SECTORS_I": _subscript_dict["SECTORS_I"],
        },
        ["CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I", "REGIONS_35_I", "SECTORS_I"],
    )
    value.loc[:, :, _subscript_dict["CLUSTER_AGRICULTURE_FISHING_FORESTRY"]] = 0
    value.loc[:, :, ["ELECTRICITY_OTHER"]] = 1
    value.loc[:, :, ["MANUFACTURE_CHEMICAL"]] = 0
    value.loc[:, :, _subscript_dict["CLUSTER_CONSTRUCTION_REAL_ESTATE"]] = 0
    value.loc[:, :, _subscript_dict["CLUSTER_EDUCATION_AND_HEALTH"]] = 1
    value.loc[:, :, ["DISTRIBUTION_ELECTRICITY"]] = 1
    value.loc[:, :, ["TRANSPORT_PIPELINE"]] = 1
    value.loc[:, :, ["ELECTRICITY_HYDRO"]] = 0
    value.loc[:, :, ["MANUFACTURE_METAL_PRODUCTS"]] = 0
    value.loc[:, :, _subscript_dict["CLUSTER_MINNING"]] = 0
    value.loc[:, :, ["ELECTRICITY_NUCLEAR"]] = 0
    value.loc[:, :, ["ELECTRICITY_OIL"]] = 0
    value.loc[:, :, _subscript_dict["CLUSTER_OTHER_ENERGY_ACTIVITIES"]] = 0
    value.loc[:, :, _subscript_dict["CLUSTER_OTHER_MANUFACTURES"]] = 0
    value.loc[:, :, _subscript_dict["CLUSTER_OTHER_SERVICE_SECTORS"]] = 0
    value.loc[:, :, ["PUBLIC_ADMINISTRATION"]] = 0
    value.loc[:, :, _subscript_dict["CLUSTER_QUARRYING"]] = 0
    value.loc[:, :, _subscript_dict["CLUSTER_REFINED_PRODUCTS_INDUSTRY"]] = 0
    value.loc[:, :, ["REFINING"]] = 0
    value.loc[:, :, _subscript_dict["CLUSTER_SOLAR_POWER_PLANTS"]] = 0
    value.loc[:, :, _subscript_dict["CLUSTER_TRANSPORT"]] = 0
    value.loc[:, :, ["WASTE_MANAGEMENT"]] = 1
    value.loc[:, :, ["ELECTRICITY_WIND"]] = 0
    value.loc[:, :, ["ELECTRICITY_COAL"]] = 0
    value.loc[:, :, ["ELECTRICITY_GAS"]] = 0
    value.loc[:, :, ["HYDROGEN_PRODUCTION"]] = 0
    value.loc[:, :, ["OTHER_SERVICES"]] = 1
    return value


@component.add(
    name="B_CAPITAL_STOCK_DAMAGE_FUNCTION",
    units="DMNL",
    subscripts=[
        "CLIMATE_HAZARDS_I",
        "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I",
        "REGIONS_35_I",
        "SECTORS_I",
    ],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_b_capital_stock_damage_function"},
)
def b_capital_stock_damage_function():
    """
    Second parameter of the capital stock damage function. Calibrated by using data from Forzieri et al (2017). Data has been processed and extrapolations have been done for some regions and sectors.
    """
    return _ext_constant_b_capital_stock_damage_function()


_ext_constant_b_capital_stock_damage_function = ExtConstant(
    "model_parameters/economy/Climate_Change_Impacts_Economy.xlsx",
    "B_Damage_Function",
    "B_CAPITAL_STOCK_DAMAGE_FUNCTION_DROUGHT_MAXI",
    {
        "CLIMATE_HAZARDS_I": ["DROUGHT"],
        "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I": ["MAXI"],
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
    _root,
    {
        "CLIMATE_HAZARDS_I": _subscript_dict["CLIMATE_HAZARDS_I"],
        "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I": _subscript_dict[
            "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I"
        ],
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
    "_ext_constant_b_capital_stock_damage_function",
)

_ext_constant_b_capital_stock_damage_function.add(
    "model_parameters/economy/Climate_Change_Impacts_Economy.xlsx",
    "B_Damage_Function",
    "B_CAPITAL_STOCK_DAMAGE_FUNCTION_DROUGHT_MINI",
    {
        "CLIMATE_HAZARDS_I": ["DROUGHT"],
        "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I": ["MINI"],
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
)

_ext_constant_b_capital_stock_damage_function.add(
    "model_parameters/economy/Climate_Change_Impacts_Economy.xlsx",
    "B_Damage_Function",
    "B_CAPITAL_STOCK_DAMAGE_FUNCTION_DROUGHT_MEDIAN",
    {
        "CLIMATE_HAZARDS_I": ["DROUGHT"],
        "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I": ["MEDIAN"],
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
)

_ext_constant_b_capital_stock_damage_function.add(
    "model_parameters/economy/Climate_Change_Impacts_Economy.xlsx",
    "B_Damage_Function",
    "B_CAPITAL_STOCK_DAMAGE_FUNCTION_DROUGHT_AVERAGE",
    {
        "CLIMATE_HAZARDS_I": ["DROUGHT"],
        "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I": ["AVERAGE"],
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
)

_ext_constant_b_capital_stock_damage_function.add(
    "model_parameters/economy/Climate_Change_Impacts_Economy.xlsx",
    "B_Damage_Function",
    "B_CAPITAL_STOCK_DAMAGE_FUNCTION_FIRE_MAXI",
    {
        "CLIMATE_HAZARDS_I": ["FIRE"],
        "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I": ["MAXI"],
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
)

_ext_constant_b_capital_stock_damage_function.add(
    "model_parameters/economy/Climate_Change_Impacts_Economy.xlsx",
    "B_Damage_Function",
    "B_CAPITAL_STOCK_DAMAGE_FUNCTION_FIRE_MINI",
    {
        "CLIMATE_HAZARDS_I": ["FIRE"],
        "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I": ["MINI"],
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
)

_ext_constant_b_capital_stock_damage_function.add(
    "model_parameters/economy/Climate_Change_Impacts_Economy.xlsx",
    "B_Damage_Function",
    "B_CAPITAL_STOCK_DAMAGE_FUNCTION_FIRE_MEDIAN",
    {
        "CLIMATE_HAZARDS_I": ["FIRE"],
        "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I": ["MEDIAN"],
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
)

_ext_constant_b_capital_stock_damage_function.add(
    "model_parameters/economy/Climate_Change_Impacts_Economy.xlsx",
    "B_Damage_Function",
    "B_CAPITAL_STOCK_DAMAGE_FUNCTION_FIRE_AVERAGE",
    {
        "CLIMATE_HAZARDS_I": ["FIRE"],
        "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I": ["AVERAGE"],
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
)

_ext_constant_b_capital_stock_damage_function.add(
    "model_parameters/economy/Climate_Change_Impacts_Economy.xlsx",
    "B_Damage_Function",
    "B_CAPITAL_STOCK_DAMAGE_FUNCTION_HEAT_MAXI",
    {
        "CLIMATE_HAZARDS_I": ["HEATWAVES"],
        "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I": ["MAXI"],
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
)

_ext_constant_b_capital_stock_damage_function.add(
    "model_parameters/economy/Climate_Change_Impacts_Economy.xlsx",
    "B_Damage_Function",
    "B_CAPITAL_STOCK_DAMAGE_FUNCTION_HEAT_MINI",
    {
        "CLIMATE_HAZARDS_I": ["HEATWAVES"],
        "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I": ["MINI"],
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
)

_ext_constant_b_capital_stock_damage_function.add(
    "model_parameters/economy/Climate_Change_Impacts_Economy.xlsx",
    "B_Damage_Function",
    "B_CAPITAL_STOCK_DAMAGE_FUNCTION_HEAT_MEDIAN",
    {
        "CLIMATE_HAZARDS_I": ["HEATWAVES"],
        "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I": ["MEDIAN"],
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
)

_ext_constant_b_capital_stock_damage_function.add(
    "model_parameters/economy/Climate_Change_Impacts_Economy.xlsx",
    "B_Damage_Function",
    "B_CAPITAL_STOCK_DAMAGE_FUNCTION_HEAT_AVERAGE",
    {
        "CLIMATE_HAZARDS_I": ["HEATWAVES"],
        "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I": ["AVERAGE"],
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
)


@component.add(
    name="B_HEAT_STRESS_DAMAGE_FUNCTION",
    units="1/DegreesC",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_b_heat_stress_damage_function"},
)
def b_heat_stress_damage_function():
    """
    Second parameter of the parabolic damage function. Calibrated by using data from Roson & Sartori (2015).
    """
    return _ext_constant_b_heat_stress_damage_function()


_ext_constant_b_heat_stress_damage_function = ExtConstant(
    "model_parameters/economy/Climate_Change_Impacts_Economy_2.xlsx",
    "Parameter_B_Heat_Stress",
    "B_HEAT_STRESS_DAMAGE_FUNCTION",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
    "_ext_constant_b_heat_stress_damage_function",
)


@component.add(
    name="C_CAPITAL_STOCK_DAMAGE_FUNCTION",
    units="DMNL",
    subscripts=[
        "CLIMATE_HAZARDS_I",
        "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I",
        "REGIONS_35_I",
        "SECTORS_I",
    ],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_c_capital_stock_damage_function"},
)
def c_capital_stock_damage_function():
    """
    Third parameter of the capital stock damage function. Calibrated by using data from Forzieri et al (2017). Data has been processed and extrapolations have been done for some regions and sectors.
    """
    return _ext_constant_c_capital_stock_damage_function()


_ext_constant_c_capital_stock_damage_function = ExtConstant(
    "model_parameters/economy/Climate_Change_Impacts_Economy.xlsx",
    "C_Damage_Function",
    "C_CAPITAL_STOCK_DAMAGE_FUNCTION_DROUGHT_MAXI",
    {
        "CLIMATE_HAZARDS_I": ["DROUGHT"],
        "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I": ["MAXI"],
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
    _root,
    {
        "CLIMATE_HAZARDS_I": _subscript_dict["CLIMATE_HAZARDS_I"],
        "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I": _subscript_dict[
            "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I"
        ],
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
    "_ext_constant_c_capital_stock_damage_function",
)

_ext_constant_c_capital_stock_damage_function.add(
    "model_parameters/economy/Climate_Change_Impacts_Economy.xlsx",
    "C_Damage_Function",
    "C_CAPITAL_STOCK_DAMAGE_FUNCTION_DROUGHT_MINI",
    {
        "CLIMATE_HAZARDS_I": ["DROUGHT"],
        "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I": ["MINI"],
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
)

_ext_constant_c_capital_stock_damage_function.add(
    "model_parameters/economy/Climate_Change_Impacts_Economy.xlsx",
    "C_Damage_Function",
    "C_CAPITAL_STOCK_DAMAGE_FUNCTION_DROUGHT_MEDIAN",
    {
        "CLIMATE_HAZARDS_I": ["DROUGHT"],
        "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I": ["MEDIAN"],
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
)

_ext_constant_c_capital_stock_damage_function.add(
    "model_parameters/economy/Climate_Change_Impacts_Economy.xlsx",
    "C_Damage_Function",
    "C_CAPITAL_STOCK_DAMAGE_FUNCTION_DROUGHT_AVERAGE",
    {
        "CLIMATE_HAZARDS_I": ["DROUGHT"],
        "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I": ["AVERAGE"],
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
)

_ext_constant_c_capital_stock_damage_function.add(
    "model_parameters/economy/Climate_Change_Impacts_Economy.xlsx",
    "C_Damage_Function",
    "C_CAPITAL_STOCK_DAMAGE_FUNCTION_FIRE_MAXI",
    {
        "CLIMATE_HAZARDS_I": ["FIRE"],
        "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I": ["MAXI"],
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
)

_ext_constant_c_capital_stock_damage_function.add(
    "model_parameters/economy/Climate_Change_Impacts_Economy.xlsx",
    "C_Damage_Function",
    "C_CAPITAL_STOCK_DAMAGE_FUNCTION_FIRE_MINI",
    {
        "CLIMATE_HAZARDS_I": ["FIRE"],
        "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I": ["MINI"],
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
)

_ext_constant_c_capital_stock_damage_function.add(
    "model_parameters/economy/Climate_Change_Impacts_Economy.xlsx",
    "C_Damage_Function",
    "C_CAPITAL_STOCK_DAMAGE_FUNCTION_FIRE_MEDIAN",
    {
        "CLIMATE_HAZARDS_I": ["FIRE"],
        "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I": ["MEDIAN"],
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
)

_ext_constant_c_capital_stock_damage_function.add(
    "model_parameters/economy/Climate_Change_Impacts_Economy.xlsx",
    "C_Damage_Function",
    "C_CAPITAL_STOCK_DAMAGE_FUNCTION_FIRE_AVERAGE",
    {
        "CLIMATE_HAZARDS_I": ["FIRE"],
        "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I": ["AVERAGE"],
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
)

_ext_constant_c_capital_stock_damage_function.add(
    "model_parameters/economy/Climate_Change_Impacts_Economy.xlsx",
    "C_Damage_Function",
    "C_CAPITAL_STOCK_DAMAGE_FUNCTION_HEAT_MAXI",
    {
        "CLIMATE_HAZARDS_I": ["HEATWAVES"],
        "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I": ["MAXI"],
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
)

_ext_constant_c_capital_stock_damage_function.add(
    "model_parameters/economy/Climate_Change_Impacts_Economy.xlsx",
    "C_Damage_Function",
    "C_CAPITAL_STOCK_DAMAGE_FUNCTION_HEAT_MINI",
    {
        "CLIMATE_HAZARDS_I": ["HEATWAVES"],
        "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I": ["MINI"],
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
)

_ext_constant_c_capital_stock_damage_function.add(
    "model_parameters/economy/Climate_Change_Impacts_Economy.xlsx",
    "C_Damage_Function",
    "C_CAPITAL_STOCK_DAMAGE_FUNCTION_HEAT_MEDIAN",
    {
        "CLIMATE_HAZARDS_I": ["HEATWAVES"],
        "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I": ["MEDIAN"],
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
)

_ext_constant_c_capital_stock_damage_function.add(
    "model_parameters/economy/Climate_Change_Impacts_Economy.xlsx",
    "C_Damage_Function",
    "C_CAPITAL_STOCK_DAMAGE_FUNCTION_HEAT_AVERAGE",
    {
        "CLIMATE_HAZARDS_I": ["HEATWAVES"],
        "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I": ["AVERAGE"],
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
)


@component.add(
    name="C_HEAT_STRESS_DAMAGE_FUNCTION",
    units="DMNL",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_c_heat_stress_damage_function"},
)
def c_heat_stress_damage_function():
    """
    Third parameter of the parabolic damage function. Calibrated by using data from Roson & Sartori (2015).
    """
    return _ext_constant_c_heat_stress_damage_function()


_ext_constant_c_heat_stress_damage_function = ExtConstant(
    "model_parameters/economy/Climate_Change_Impacts_Economy_2.xlsx",
    "Parameter_C_Heat_Stress",
    "C_HEAT_STRESS_DAMAGE_FUNCTION",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
    "_ext_constant_c_heat_stress_damage_function",
)


@component.add(
    name="capital_stock_damage_function",
    units="DMNL",
    subscripts=[
        "CLIMATE_HAZARDS_I",
        "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I",
        "REGIONS_35_I",
        "SECTORS_I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_economy": 1,
        "c_capital_stock_damage_function": 2,
        "b_capital_stock_damage_function": 8,
        "temperature_change_2015": 5,
        "correspondence_matrix_damage_function": 14,
        "a_capital_stock_damage_function": 10,
        "temperature_change_in_35regions": 5,
    },
)
def capital_stock_damage_function():
    """
    Damage function that measures the yearly capital stock losses. It is a multi-dimmensional matrix with different values per climate hazard, climate change uncertainty scenario, region and sector. For these combinations, there exist 6 types of functional forms.
    """
    return if_then_else(
        switch_economy() == 0,
        lambda: if_then_else(
            correspondence_matrix_damage_function() == 0,
            lambda: a_capital_stock_damage_function() * (temperature_change_2015() ** 2)
            + b_capital_stock_damage_function() * temperature_change_2015()
            + c_capital_stock_damage_function(),
            lambda: if_then_else(
                correspondence_matrix_damage_function() == 1,
                lambda: 1
                / (
                    1
                    + a_capital_stock_damage_function()
                    * np.exp(
                        -b_capital_stock_damage_function() * temperature_change_2015()
                    )
                ),
                lambda: if_then_else(
                    correspondence_matrix_damage_function() == 2,
                    lambda: a_capital_stock_damage_function()
                    * temperature_change_2015()
                    + b_capital_stock_damage_function(),
                    lambda: if_then_else(
                        correspondence_matrix_damage_function() == 3,
                        lambda: a_capital_stock_damage_function(),
                        lambda: if_then_else(
                            correspondence_matrix_damage_function() == 4,
                            lambda: a_capital_stock_damage_function()
                            * (
                                temperature_change_2015()
                                ** b_capital_stock_damage_function().transpose(
                                    "REGIONS_35_I",
                                    "CLIMATE_HAZARDS_I",
                                    "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I",
                                    "SECTORS_I",
                                )
                            ).transpose(
                                "CLIMATE_HAZARDS_I",
                                "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I",
                                "REGIONS_35_I",
                                "SECTORS_I",
                            ),
                            lambda: if_then_else(
                                correspondence_matrix_damage_function() == 5,
                                lambda: xr.DataArray(
                                    0,
                                    {
                                        "CLIMATE_HAZARDS_I": _subscript_dict[
                                            "CLIMATE_HAZARDS_I"
                                        ],
                                        "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I": _subscript_dict[
                                            "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I"
                                        ],
                                        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                                        "SECTORS_I": _subscript_dict["SECTORS_I"],
                                    },
                                    [
                                        "CLIMATE_HAZARDS_I",
                                        "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I",
                                        "REGIONS_35_I",
                                        "SECTORS_I",
                                    ],
                                ),
                                lambda: if_then_else(
                                    correspondence_matrix_damage_function() == 6,
                                    lambda: xr.DataArray(
                                        0,
                                        {
                                            "CLIMATE_HAZARDS_I": _subscript_dict[
                                                "CLIMATE_HAZARDS_I"
                                            ],
                                            "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I": _subscript_dict[
                                                "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I"
                                            ],
                                            "REGIONS_35_I": _subscript_dict[
                                                "REGIONS_35_I"
                                            ],
                                            "SECTORS_I": _subscript_dict["SECTORS_I"],
                                        },
                                        [
                                            "CLIMATE_HAZARDS_I",
                                            "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I",
                                            "REGIONS_35_I",
                                            "SECTORS_I",
                                        ],
                                    ),
                                    lambda: xr.DataArray(
                                        0,
                                        {
                                            "CLIMATE_HAZARDS_I": _subscript_dict[
                                                "CLIMATE_HAZARDS_I"
                                            ],
                                            "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I": _subscript_dict[
                                                "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I"
                                            ],
                                            "REGIONS_35_I": _subscript_dict[
                                                "REGIONS_35_I"
                                            ],
                                            "SECTORS_I": _subscript_dict["SECTORS_I"],
                                        },
                                        [
                                            "CLIMATE_HAZARDS_I",
                                            "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I",
                                            "REGIONS_35_I",
                                            "SECTORS_I",
                                        ],
                                    ),
                                ),
                            ),
                        ),
                    ),
                ),
            ),
        ),
        lambda: if_then_else(
            correspondence_matrix_damage_function() == 0,
            lambda: a_capital_stock_damage_function()
            * (temperature_change_in_35regions() ** 2)
            + b_capital_stock_damage_function() * temperature_change_in_35regions()
            + c_capital_stock_damage_function(),
            lambda: if_then_else(
                correspondence_matrix_damage_function() == 1,
                lambda: 1
                / (
                    1
                    + a_capital_stock_damage_function()
                    * np.exp(
                        -b_capital_stock_damage_function()
                        * temperature_change_in_35regions()
                    )
                ),
                lambda: if_then_else(
                    correspondence_matrix_damage_function() == 2,
                    lambda: a_capital_stock_damage_function()
                    * temperature_change_in_35regions()
                    + b_capital_stock_damage_function(),
                    lambda: if_then_else(
                        correspondence_matrix_damage_function() == 3,
                        lambda: a_capital_stock_damage_function(),
                        lambda: if_then_else(
                            correspondence_matrix_damage_function() == 4,
                            lambda: a_capital_stock_damage_function()
                            * (
                                temperature_change_in_35regions()
                                ** b_capital_stock_damage_function().transpose(
                                    "REGIONS_35_I",
                                    "CLIMATE_HAZARDS_I",
                                    "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I",
                                    "SECTORS_I",
                                )
                            ).transpose(
                                "CLIMATE_HAZARDS_I",
                                "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I",
                                "REGIONS_35_I",
                                "SECTORS_I",
                            ),
                            lambda: if_then_else(
                                correspondence_matrix_damage_function() == 5,
                                lambda: xr.DataArray(
                                    0,
                                    {
                                        "CLIMATE_HAZARDS_I": _subscript_dict[
                                            "CLIMATE_HAZARDS_I"
                                        ],
                                        "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I": _subscript_dict[
                                            "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I"
                                        ],
                                        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                                        "SECTORS_I": _subscript_dict["SECTORS_I"],
                                    },
                                    [
                                        "CLIMATE_HAZARDS_I",
                                        "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I",
                                        "REGIONS_35_I",
                                        "SECTORS_I",
                                    ],
                                ),
                                lambda: if_then_else(
                                    correspondence_matrix_damage_function() == 6,
                                    lambda: xr.DataArray(
                                        0,
                                        {
                                            "CLIMATE_HAZARDS_I": _subscript_dict[
                                                "CLIMATE_HAZARDS_I"
                                            ],
                                            "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I": _subscript_dict[
                                                "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I"
                                            ],
                                            "REGIONS_35_I": _subscript_dict[
                                                "REGIONS_35_I"
                                            ],
                                            "SECTORS_I": _subscript_dict["SECTORS_I"],
                                        },
                                        [
                                            "CLIMATE_HAZARDS_I",
                                            "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I",
                                            "REGIONS_35_I",
                                            "SECTORS_I",
                                        ],
                                    ),
                                    lambda: xr.DataArray(
                                        0,
                                        {
                                            "CLIMATE_HAZARDS_I": _subscript_dict[
                                                "CLIMATE_HAZARDS_I"
                                            ],
                                            "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I": _subscript_dict[
                                                "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I"
                                            ],
                                            "REGIONS_35_I": _subscript_dict[
                                                "REGIONS_35_I"
                                            ],
                                            "SECTORS_I": _subscript_dict["SECTORS_I"],
                                        },
                                        [
                                            "CLIMATE_HAZARDS_I",
                                            "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I",
                                            "REGIONS_35_I",
                                            "SECTORS_I",
                                        ],
                                    ),
                                ),
                            ),
                        ),
                    ),
                ),
            ),
        ),
    )


@component.add(
    name="capital_stock_damage_function_drought",
    units="DMNL",
    subscripts=[
        "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I",
        "REGIONS_35_I",
        "SECTORS_I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_climate_change_impacts_remove_extrapolations_sp": 1,
        "auxiliar_variable_to_remove_extrapolations_of_droughts": 1,
        "capital_stock_damage_function": 4,
    },
)
def capital_stock_damage_function_drought():
    """
    Damage function that measures the yearly capital stock losses due to droughts.
    """
    return if_then_else(
        select_climate_change_impacts_remove_extrapolations_sp() == 0,
        lambda: if_then_else(
            capital_stock_damage_function()
            .loc["DROUGHT", :, :, :]
            .reset_coords(drop=True)
            > 1,
            lambda: xr.DataArray(
                1,
                {
                    "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I": _subscript_dict[
                        "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I"
                    ],
                    "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                    "SECTORS_I": _subscript_dict["SECTORS_I"],
                },
                [
                    "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I",
                    "REGIONS_35_I",
                    "SECTORS_I",
                ],
            ),
            lambda: capital_stock_damage_function()
            .loc["DROUGHT", :, :, :]
            .reset_coords(drop=True),
        )
        * auxiliar_variable_to_remove_extrapolations_of_droughts(),
        lambda: if_then_else(
            capital_stock_damage_function()
            .loc["DROUGHT", :, :, :]
            .reset_coords(drop=True)
            > 1,
            lambda: xr.DataArray(
                1,
                {
                    "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I": _subscript_dict[
                        "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I"
                    ],
                    "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                    "SECTORS_I": _subscript_dict["SECTORS_I"],
                },
                [
                    "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I",
                    "REGIONS_35_I",
                    "SECTORS_I",
                ],
            ),
            lambda: capital_stock_damage_function()
            .loc["DROUGHT", :, :, :]
            .reset_coords(drop=True),
        ),
    )


@component.add(
    name="capital_stock_damage_function_heat",
    units="DMNL",
    subscripts=[
        "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I",
        "REGIONS_35_I",
        "SECTORS_I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_climate_change_impacts_remove_extrapolations_sp": 1,
        "capital_stock_damage_function": 4,
        "auxiliar_variable_to_remove_extrapolations_of_heatwaves": 1,
    },
)
def capital_stock_damage_function_heat():
    """
    Damage function that measures the yearly capital stock losses due to heatwaves.
    """
    return if_then_else(
        select_climate_change_impacts_remove_extrapolations_sp() == 0,
        lambda: if_then_else(
            capital_stock_damage_function()
            .loc["HEATWAVES", :, :, :]
            .reset_coords(drop=True)
            > 1,
            lambda: xr.DataArray(
                1,
                {
                    "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I": _subscript_dict[
                        "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I"
                    ],
                    "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                    "SECTORS_I": _subscript_dict["SECTORS_I"],
                },
                [
                    "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I",
                    "REGIONS_35_I",
                    "SECTORS_I",
                ],
            ),
            lambda: capital_stock_damage_function()
            .loc["HEATWAVES", :, :, :]
            .reset_coords(drop=True),
        )
        * auxiliar_variable_to_remove_extrapolations_of_heatwaves(),
        lambda: if_then_else(
            capital_stock_damage_function()
            .loc["HEATWAVES", :, :, :]
            .reset_coords(drop=True)
            > 1,
            lambda: xr.DataArray(
                1,
                {
                    "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I": _subscript_dict[
                        "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I"
                    ],
                    "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                    "SECTORS_I": _subscript_dict["SECTORS_I"],
                },
                [
                    "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I",
                    "REGIONS_35_I",
                    "SECTORS_I",
                ],
            ),
            lambda: capital_stock_damage_function()
            .loc["HEATWAVES", :, :, :]
            .reset_coords(drop=True),
        ),
    )


@component.add(
    name="capital_stock_damage_function_wildfire",
    units="DMNL",
    subscripts=[
        "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I",
        "REGIONS_35_I",
        "SECTORS_I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_climate_change_impacts_remove_extrapolations_sp": 1,
        "capital_stock_damage_function": 4,
        "auxiliar_variable_to_remove_extrapolations_of_wildfires": 1,
    },
)
def capital_stock_damage_function_wildfire():
    """
    Damage function that measures the yearly capital stock losses due to wildfires.
    """
    return if_then_else(
        select_climate_change_impacts_remove_extrapolations_sp() == 0,
        lambda: if_then_else(
            capital_stock_damage_function().loc["FIRE", :, :, :].reset_coords(drop=True)
            > 1,
            lambda: xr.DataArray(
                1,
                {
                    "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I": _subscript_dict[
                        "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I"
                    ],
                    "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                    "SECTORS_I": _subscript_dict["SECTORS_I"],
                },
                [
                    "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I",
                    "REGIONS_35_I",
                    "SECTORS_I",
                ],
            ),
            lambda: capital_stock_damage_function()
            .loc["FIRE", :, :, :]
            .reset_coords(drop=True),
        )
        * auxiliar_variable_to_remove_extrapolations_of_wildfires(),
        lambda: if_then_else(
            capital_stock_damage_function().loc["FIRE", :, :, :].reset_coords(drop=True)
            > 1,
            lambda: xr.DataArray(
                1,
                {
                    "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I": _subscript_dict[
                        "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I"
                    ],
                    "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                    "SECTORS_I": _subscript_dict["SECTORS_I"],
                },
                [
                    "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I",
                    "REGIONS_35_I",
                    "SECTORS_I",
                ],
            ),
            lambda: capital_stock_damage_function()
            .loc["FIRE", :, :, :]
            .reset_coords(drop=True),
        ),
    )


@component.add(
    name="capital_stock_damage_rate_for_all_the_uncertainty_scenarios",
    units="DMNL",
    subscripts=[
        "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I",
        "REGIONS_35_I",
        "SECTORS_I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_climate_hazards_sp": 4,
        "total_hazards_capital_stock_damage_function": 1,
        "capital_stock_damage_function_heat": 1,
        "capital_stock_damage_function_drought": 1,
        "capital_stock_damage_function_wildfire": 1,
    },
)
def capital_stock_damage_rate_for_all_the_uncertainty_scenarios():
    """
    Damage function that measures the yearly capital stock losses once selected a hazard combination and an uncertainty scenario in the 'SELECT' respective options.
    """
    return if_then_else(
        select_climate_hazards_sp() == 0,
        lambda: total_hazards_capital_stock_damage_function(),
        lambda: if_then_else(
            select_climate_hazards_sp() == 1,
            lambda: capital_stock_damage_function_heat(),
            lambda: if_then_else(
                select_climate_hazards_sp() == 2,
                lambda: capital_stock_damage_function_wildfire(),
                lambda: if_then_else(
                    select_climate_hazards_sp() == 3,
                    lambda: capital_stock_damage_function_drought(),
                    lambda: xr.DataArray(
                        0,
                        {
                            "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I": _subscript_dict[
                                "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I"
                            ],
                            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                            "SECTORS_I": _subscript_dict["SECTORS_I"],
                        },
                        [
                            "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I",
                            "REGIONS_35_I",
                            "SECTORS_I",
                        ],
                    ),
                ),
            ),
        ),
    )


@component.add(
    name="climate_change_damage_rate_to_capital_stock",
    units="DMNL",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_climate_change_impact_uncertainty_scenario_sp": 4,
        "capital_stock_damage_rate_for_all_the_uncertainty_scenarios": 4,
    },
)
def climate_change_damage_rate_to_capital_stock():
    """
    Climate change damage rate of the stock of capital
    """
    return np.maximum(
        0,
        np.minimum(
            1,
            if_then_else(
                select_climate_change_impact_uncertainty_scenario_sp() == 0,
                lambda: capital_stock_damage_rate_for_all_the_uncertainty_scenarios()
                .loc["MAXI", :, :]
                .reset_coords(drop=True),
                lambda: if_then_else(
                    select_climate_change_impact_uncertainty_scenario_sp() == 1,
                    lambda: capital_stock_damage_rate_for_all_the_uncertainty_scenarios()
                    .loc["MINI", :, :]
                    .reset_coords(drop=True),
                    lambda: if_then_else(
                        select_climate_change_impact_uncertainty_scenario_sp() == 2,
                        lambda: capital_stock_damage_rate_for_all_the_uncertainty_scenarios()
                        .loc["MEDIAN", :, :]
                        .reset_coords(drop=True),
                        lambda: if_then_else(
                            select_climate_change_impact_uncertainty_scenario_sp() == 3,
                            lambda: capital_stock_damage_rate_for_all_the_uncertainty_scenarios()
                            .loc["AVERAGE", :, :]
                            .reset_coords(drop=True),
                            lambda: xr.DataArray(
                                0,
                                {
                                    "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                                    "SECTORS_I": _subscript_dict["SECTORS_I"],
                                },
                                ["REGIONS_35_I", "SECTORS_I"],
                            ),
                        ),
                    ),
                ),
            ),
        ),
    )


@component.add(
    name="climate_change_damage_rate_to_capital_stock_delayed",
    units="DMNL",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_climate_change_damage_rate_to_capital_stock_delayed": 1},
    other_deps={
        "_delayfixed_climate_change_damage_rate_to_capital_stock_delayed": {
            "initial": {"time_step": 1},
            "step": {"climate_change_damage_rate_to_capital_stock": 1},
        }
    },
)
def climate_change_damage_rate_to_capital_stock_delayed():
    """
    Climate change damage rate of the stock of capital delayed one time step
    """
    return _delayfixed_climate_change_damage_rate_to_capital_stock_delayed()


_delayfixed_climate_change_damage_rate_to_capital_stock_delayed = DelayFixed(
    lambda: climate_change_damage_rate_to_capital_stock(),
    lambda: time_step(),
    lambda: xr.DataArray(
        0,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "SECTORS_I": _subscript_dict["SECTORS_I"],
        },
        ["REGIONS_35_I", "SECTORS_I"],
    ),
    time_step,
    "_delayfixed_climate_change_damage_rate_to_capital_stock_delayed",
)


@component.add(
    name="climate_change_damage_rate_to_capital_stock_until_2015",
    units="DMNL",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "auxiliar_for_climate_change_damage_rate_to_capital_stock_until_2015": 1,
        "climate_change_damage_rate_to_capital_stock": 1,
    },
)
def climate_change_damage_rate_to_capital_stock_until_2015():
    """
    Climate change damage rate of the stock of capital: values until the year 2015
    """
    return if_then_else(
        time() > 2015,
        lambda: auxiliar_for_climate_change_damage_rate_to_capital_stock_until_2015(),
        lambda: climate_change_damage_rate_to_capital_stock(),
    )


@component.add(
    name="climate_change_incremental_damage_rate_to_capital_stock",
    units="DMNL",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "climate_change_damage_rate_to_capital_stock_until_2015": 1,
        "climate_change_damage_rate_to_capital_stock": 1,
        "ratio_to_update_df": 1,
    },
)
def climate_change_incremental_damage_rate_to_capital_stock():
    """
    Climate change damage rate to capital stock adjusted to be 0 in 2015, since we assume that historical data already accounts for the implicit damage.
    """
    return (
        if_then_else(
            time() < 2015,
            lambda: xr.DataArray(
                0,
                {
                    "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                    "SECTORS_I": _subscript_dict["SECTORS_I"],
                },
                ["REGIONS_35_I", "SECTORS_I"],
            ),
            lambda: climate_change_damage_rate_to_capital_stock()
            - climate_change_damage_rate_to_capital_stock_until_2015(),
        )
        * ratio_to_update_df()
    )


@component.add(
    name="GLOBAL_TEMPERATURE_CHANGE_2015",
    units="DegreesC",
    comp_type="Constant",
    comp_subtype="Normal",
)
def global_temperature_change_2015():
    """
    Exogenous global temperature increase in 2015
    """
    return 0.999


@component.add(
    name="heat_stress_damage_function",
    units="DMNL",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_economy": 1,
        "global_temperature_change_2015": 2,
        "a_heat_stress_damage_function": 2,
        "c_heat_stress_damage_function": 2,
        "b_heat_stress_damage_function": 2,
        "temperature_change": 2,
    },
)
def heat_stress_damage_function():
    """
    Damage function that measures heat stress impacts on labour productivity.
    """
    return if_then_else(
        switch_economy() == 0,
        lambda: a_heat_stress_damage_function() * global_temperature_change_2015() ** 2
        + b_heat_stress_damage_function() * global_temperature_change_2015()
        + c_heat_stress_damage_function(),
        lambda: a_heat_stress_damage_function() * temperature_change() ** 2
        + b_heat_stress_damage_function() * temperature_change()
        + c_heat_stress_damage_function(),
    )


@component.add(
    name="heat_stress_damage_function_until_2015",
    units="DMNL",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "auxiliar_heat_stress_damage_function_until_2015": 1,
        "heat_stress_damage_function": 1,
    },
)
def heat_stress_damage_function_until_2015():
    """
    Heat stress damage function (values until 2015, after constant)
    """
    return if_then_else(
        time() > 2015,
        lambda: auxiliar_heat_stress_damage_function_until_2015(),
        lambda: heat_stress_damage_function(),
    )


@component.add(
    name="heat_stress_incremental_damage_function",
    units="DMNL",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "heat_stress_damage_function_until_2015": 1,
        "heat_stress_damage_function": 1,
    },
)
def heat_stress_incremental_damage_function():
    """
    Heat stress damage rate to labour productivity adjusted to be 0 in 2015, since we assume that historical data already accounts for the implicit damage.
    """
    return if_then_else(
        time() < 2015,
        lambda: xr.DataArray(
            0,
            {
                "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                "SECTORS_I": _subscript_dict["SECTORS_I"],
            },
            ["REGIONS_35_I", "SECTORS_I"],
        ),
        lambda: heat_stress_damage_function()
        - heat_stress_damage_function_until_2015(),
    )


@component.add(
    name="INITIAL_CAPITAL_STOCK_OUTDATED",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_capital_stock_outdated"},
)
def initial_capital_stock_outdated():
    return _ext_constant_initial_capital_stock_outdated()


_ext_constant_initial_capital_stock_outdated = ExtConstant(
    "model_parameters/economy/CS_2015_outdated.xlsx",
    "CS_2015_outdated",
    "B3",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
    "_ext_constant_initial_capital_stock_outdated",
)


@component.add(
    name="ratio_to_update_DF",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"initial_capital_stock_outdated": 1, "initial_capital_stock": 1},
)
def ratio_to_update_df():
    return zidz(initial_capital_stock_outdated(), initial_capital_stock())


@component.add(
    name="SELECT_CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIO_SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_select_climate_change_impact_uncertainty_scenario_sp"
    },
)
def select_climate_change_impact_uncertainty_scenario_sp():
    """
    This 'select' has the following position: 0: maximum damages (the statistic measure 'maximum' is used to calibrate the damage function) 1: minimum damages (the statistic measure 'minimum' is used to calibrate the damage function) 2: median damages (the statistic measure 'median' is used to calibrate the damage function) 3: average damages (the statistic measure 'mean' is used to calibrate the damage function)
    """
    return _ext_constant_select_climate_change_impact_uncertainty_scenario_sp()


_ext_constant_select_climate_change_impact_uncertainty_scenario_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "SELECT_CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIO_SP",
    {},
    _root,
    {},
    "_ext_constant_select_climate_change_impact_uncertainty_scenario_sp",
)


@component.add(
    name="SELECT_CLIMATE_CHANGE_IMPACTS_REMOVE_EXTRAPOLATIONS_SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_select_climate_change_impacts_remove_extrapolations_sp"
    },
)
def select_climate_change_impacts_remove_extrapolations_sp():
    """
    TEST SELECT: 0: Damage of extrapolated clusters are multiplied by 0 (EXTRAPOLATIONS OFF) 1: no sectors are multiplied by 0 (EXTRAPOLATIONS ON)
    """
    return _ext_constant_select_climate_change_impacts_remove_extrapolations_sp()


_ext_constant_select_climate_change_impacts_remove_extrapolations_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "SELECT_CLIMATE_CHANGE_IMPACTS_REMOVE_EXTRAPOLATIONS_SP",
    {},
    _root,
    {},
    "_ext_constant_select_climate_change_impacts_remove_extrapolations_sp",
)


@component.add(
    name="SELECT_CLIMATE_HAZARDS_SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_select_climate_hazards_sp"},
)
def select_climate_hazards_sp():
    """
    This 'select' has the following options: 0: damage function represent impacts from all the hazards 1: damage function represent impacts from heatwaves 2: damage function represent impacts from wildfires 3: damage function represent impacts from droughts
    """
    return _ext_constant_select_climate_hazards_sp()


_ext_constant_select_climate_hazards_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "SELECT_CLIMATE_HAZARDS_SP",
    {},
    _root,
    {},
    "_ext_constant_select_climate_hazards_sp",
)


@component.add(
    name="SWITCH_CLIMATE_CHANGE_DAMAGE",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_climate_change_damage"},
)
def switch_climate_change_damage():
    """
    Transversal module SWITCH which can take two values: 0: no climate change damages in all the model 1: climate change damages allowed in all the model
    """
    return _ext_constant_switch_climate_change_damage()


_ext_constant_switch_climate_change_damage = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_CLIMATE_CHANGE_DAMAGE",
    {},
    _root,
    {},
    "_ext_constant_switch_climate_change_damage",
)


@component.add(
    name="SWITCH_ECO_CLIMATE_CHANGE_DAMAGE_CAPITAL",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_switch_eco_climate_change_damage_capital"
    },
)
def switch_eco_climate_change_damage_capital():
    """
    This switch can take two values: 0: capital stock damages are not activated 1: capital stock damages are activated
    """
    return _ext_constant_switch_eco_climate_change_damage_capital()


_ext_constant_switch_eco_climate_change_damage_capital = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_ECO_CLIMATE_CHANGE_DAMAGE_CAPITAL",
    {},
    _root,
    {},
    "_ext_constant_switch_eco_climate_change_damage_capital",
)


@component.add(
    name="SWITCH_ECO_CLIMATE_CHANGE_DAMAGE_LABOUR_PRODUCTIVITY",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_switch_eco_climate_change_damage_labour_productivity"
    },
)
def switch_eco_climate_change_damage_labour_productivity():
    """
    This switch can take two values: 0: labour productivity damages are not activated 1: labour productivity damages are activated
    """
    return _ext_constant_switch_eco_climate_change_damage_labour_productivity()


_ext_constant_switch_eco_climate_change_damage_labour_productivity = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_ECO_CLIMATE_CHANGE_DAMAGE_LABOUR_PRODUCTIVITY",
    {},
    _root,
    {},
    "_ext_constant_switch_eco_climate_change_damage_labour_productivity",
)


@component.add(
    name="TEMPERATURE_CHANGE_2015",
    units="DegreesC",
    subscripts=["REGIONS_35_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_temperature_change_2015"},
)
def temperature_change_2015():
    """
    Exogenous Value of the Temperature in 2015. It is uploaded in case we want to modularize this sub-module.
    """
    return _ext_constant_temperature_change_2015()


_ext_constant_temperature_change_2015 = ExtConstant(
    "model_parameters/economy/Climate_Change_Impacts_Economy.xlsx",
    "TEMPERATURE_CHANGE_2015",
    "TEMPERATURE_CHANGE_2015",
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    _root,
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    "_ext_constant_temperature_change_2015",
)


@component.add(
    name="total_hazards_capital_stock_damage_function",
    units="DMNL",
    subscripts=[
        "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I",
        "REGIONS_35_I",
        "SECTORS_I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "capital_stock_damage_function_drought": 2,
        "capital_stock_damage_function_heat": 2,
        "capital_stock_damage_function_wildfire": 2,
    },
)
def total_hazards_capital_stock_damage_function():
    """
    IF_THEN_ELSE(SUM(capital stock damage function[CLIMATE HAZARDS I!,CLIMATE CHANGE IMPACT UNCERTAINTY SCENARIOS I,REGIONS 35 I ,SECTORS I])>1, 1, SUM(capital stock damage function[CLIMATE HAZARDS I!,CLIMATE CHANGE IMPACT UNCERTAINTY SCENARIOS I,REGIONS 35 I ,SECTORS I]))
    """
    return if_then_else(
        capital_stock_damage_function_drought()
        + capital_stock_damage_function_heat()
        + capital_stock_damage_function_wildfire()
        > 1,
        lambda: xr.DataArray(
            1,
            {
                "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I": _subscript_dict[
                    "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I"
                ],
                "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                "SECTORS_I": _subscript_dict["SECTORS_I"],
            },
            [
                "CLIMATE_CHANGE_IMPACT_UNCERTAINTY_SCENARIOS_I",
                "REGIONS_35_I",
                "SECTORS_I",
            ],
        ),
        lambda: capital_stock_damage_function_drought()
        + capital_stock_damage_function_heat()
        + capital_stock_damage_function_wildfire(),
    )


@component.add(
    name="vector_borne_diseases_damage_function",
    units="DMNL",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "a_vector_borne_diseases_damage_function": 1,
        "global_temperature_change_2015": 1,
        "temperature_change": 1,
        "switch_economy": 1,
    },
)
def vector_borne_diseases_damage_function():
    """
    Damage function that measures vector borne diseases impacts on labour productivity.
    """
    return a_vector_borne_diseases_damage_function() * if_then_else(
        switch_economy() == 0,
        lambda: global_temperature_change_2015(),
        lambda: temperature_change(),
    )


@component.add(
    name="vector_borne_diseases_damage_function_delayed",
    units="DMNL",
    subscripts=["REGIONS_35_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_vector_borne_diseases_damage_function_delayed": 1},
    other_deps={
        "_delayfixed_vector_borne_diseases_damage_function_delayed": {
            "initial": {"time_step": 1},
            "step": {"vector_borne_diseases_damage_function": 1},
        }
    },
)
def vector_borne_diseases_damage_function_delayed():
    """
    Vector borne diseases damage function delayed one time step
    """
    return _delayfixed_vector_borne_diseases_damage_function_delayed()


_delayfixed_vector_borne_diseases_damage_function_delayed = DelayFixed(
    lambda: vector_borne_diseases_damage_function(),
    lambda: time_step(),
    lambda: xr.DataArray(
        0, {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]}, ["REGIONS_35_I"]
    ),
    time_step,
    "_delayfixed_vector_borne_diseases_damage_function_delayed",
)


@component.add(
    name="vector_borne_diseases_damage_function_until_2015",
    units="DMNL",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "vector_borne_diseases_damage_function_delayed": 1,
        "auxiliar_for_vector_borne_diseases_damage_function": 1,
    },
)
def vector_borne_diseases_damage_function_until_2015():
    """
    Vector borne diseases damage function (values until 2015, after constant)
    """
    return if_then_else(
        time() < 2015,
        lambda: vector_borne_diseases_damage_function_delayed(),
        lambda: auxiliar_for_vector_borne_diseases_damage_function(),
    )


@component.add(
    name="vector_borne_diseases_incremental_damage_function",
    units="DMNL",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "vector_borne_diseases_damage_function_until_2015": 1,
        "vector_borne_diseases_damage_function": 1,
    },
)
def vector_borne_diseases_incremental_damage_function():
    """
    Vector borne diseases damage function adjusted to be 0 in 2015, since we assume that historical data already accounts for the implicit damage.
    """
    return if_then_else(
        time() < 2015,
        lambda: xr.DataArray(
            0, {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]}, ["REGIONS_35_I"]
        ),
        lambda: vector_borne_diseases_damage_function()
        - vector_borne_diseases_damage_function_until_2015(),
    )
