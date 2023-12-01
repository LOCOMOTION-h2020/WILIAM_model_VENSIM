"""
Module materials.fossil_fuels
Translated using PySD version 3.10.0
"""


@component.add(
    name="actual_spare_capacity",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"oil_demand": 1, "oil_max_extraction_capacity": 1},
)
def actual_spare_capacity():
    """
    Actual Oil spare capacity based on the supply and the demand.
    """
    return np.maximum(1 - oil_demand() / oil_max_extraction_capacity(), 0)


@component.add(
    name="actual_spare_capacity_gas",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"gas_demand_1": 1, "gas_max_extraction_capacity": 1},
)
def actual_spare_capacity_gas():
    """
    Spare capacity of natural gas. Difference between the demand and the the extraction capacity of natural gas
    """
    return np.maximum(1 - gas_demand_1() / gas_max_extraction_capacity(), 0)


@component.add(
    name="AVERAGE_COAL_MINING_CAPACITY",
    units="Mt/mines/Year",
    subscripts=["COAL_TYPES_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_average_coal_mining_capacity"},
)
def average_coal_mining_capacity():
    """
    Average Production capacity, HARD COAL and BROWN coal mines based on the data of Operating mines in 2022 and their production output.Simplification made by the Authors since the mining capacity varies strongly across mines.Assignt and average prodcution capacity per mine per year over the total number of mines. Source: “Global Coal Mine Tracker, Global Energy Monitor, July 2022 release.” HARD COAL 2.43618 BROWN COAL 5.21164
    """
    return _ext_constant_average_coal_mining_capacity()


_ext_constant_average_coal_mining_capacity = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Hydrocarbons",
    "AVERAGE_COAL_MINING_CAPACITY*",
    {"COAL_TYPES_I": _subscript_dict["COAL_TYPES_I"]},
    _root,
    {"COAL_TYPES_I": _subscript_dict["COAL_TYPES_I"]},
    "_ext_constant_average_coal_mining_capacity",
)


@component.add(
    name="BROWN_COAL_RESOURCE_ESTIMATION_HIGH_SP",
    units="EJ",
    subscripts=["COAL_TYPES_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_brown_coal_resource_estimation_high_sp"},
)
def brown_coal_resource_estimation_high_sp():
    return _ext_constant_brown_coal_resource_estimation_high_sp()


_ext_constant_brown_coal_resource_estimation_high_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "materials",
    "BROWN_COAL_RESOURCE_ESTIMATION_HIGH_SP",
    {"COAL_TYPES_I": ["BROWN_COAL"]},
    _root,
    {"COAL_TYPES_I": _subscript_dict["COAL_TYPES_I"]},
    "_ext_constant_brown_coal_resource_estimation_high_sp",
)


@component.add(
    name="BROWN_COAL_RESOURCE_ESTIMATION_LOW_SP",
    units="EJ",
    subscripts=["COAL_TYPES_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_brown_coal_resource_estimation_low_sp"},
)
def brown_coal_resource_estimation_low_sp():
    return _ext_constant_brown_coal_resource_estimation_low_sp()


_ext_constant_brown_coal_resource_estimation_low_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "materials",
    "BROWN_COAL_RESOURCE_ESTIMATION_LOW_SP",
    {"COAL_TYPES_I": ["BROWN_COAL"]},
    _root,
    {"COAL_TYPES_I": _subscript_dict["COAL_TYPES_I"]},
    "_ext_constant_brown_coal_resource_estimation_low_sp",
)


@component.add(
    name="BROWN_COAL_RESOURCE_ESTIMATION_MED_SP",
    units="EJ",
    subscripts=["COAL_TYPES_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_brown_coal_resource_estimation_med_sp"},
)
def brown_coal_resource_estimation_med_sp():
    return _ext_constant_brown_coal_resource_estimation_med_sp()


_ext_constant_brown_coal_resource_estimation_med_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "materials",
    "BROWN_COAL_RESOURCE_ESTIMATION_MED_SP",
    {"COAL_TYPES_I": ["BROWN_COAL"]},
    _root,
    {"COAL_TYPES_I": _subscript_dict["COAL_TYPES_I"]},
    "_ext_constant_brown_coal_resource_estimation_med_sp",
)


@component.add(name="Coal_base_price_2015", comp_type="Constant", comp_subtype="Normal")
def coal_base_price_2015():
    return 75.1643


@component.add(
    name="coal_demand_2",
    units="EJ/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "switch_nrg2mat_coal_demand": 1,
        "switch_materials": 1,
        "historical_coal_demand_two": 1,
        "world_pe_coal_ej": 1,
    },
)
def coal_demand_2():
    """
    Coal demand before 2015 historical values from 2015 onwards it takes the values from the WILIAM energy module.
    """
    return if_then_else(
        np.logical_or(
            time() < 2015,
            np.logical_or(switch_nrg2mat_coal_demand() == 0, switch_materials() == 0),
        ),
        lambda: historical_coal_demand_two(),
        lambda: world_pe_coal_ej(),
    )


@component.add(
    name="coal_extraction_in_Mt",
    units="Mt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"extraction_of_coal": 2, "unit_conversion_mt_ej": 2},
)
def coal_extraction_in_mt():
    """
    Total coal in extracted in Mt
    """
    return float(extraction_of_coal().loc["HARD_COAL"]) * float(
        unit_conversion_mt_ej().loc["HARD_COAL"]
    ) + float(extraction_of_coal().loc["BROWN_COAL"]) * float(
        unit_conversion_mt_ej().loc["BROWN_COAL"]
    )


@component.add(
    name="coal_gap_between_total_available_and_demand",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "coal_demand_2": 1,
        "total_coal_available": 1,
        "coefficient_max_coal_price": 1,
    },
)
def coal_gap_between_total_available_and_demand():
    """
    Coal spare capacity and a set maximium. Intermediate step for the Coal price calculation. Calculation is based on a LN function which describes the relation between Coal demand per year and Coal available without the spare capacity. (1-Q/Q available)
    """
    return np.maximum(
        1 - coal_demand_2() / total_coal_available(), coefficient_max_coal_price()
    )


@component.add(
    name="COAL_MINE_DEPLETION_RATE", comp_type="Constant", comp_subtype="Normal"
)
def coal_mine_depletion_rate():
    return 0


@component.add(
    name="COAL_MINES_INVESTMENT_CAP",
    units="DMNL/Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_coal_mines_investment_cap"},
)
def coal_mines_investment_cap():
    """
    Maximum Investment in Coal mines possible from one year to another. Estimation made by the authors in the moment modeled with 12%. or value of 0.12
    """
    return _ext_constant_coal_mines_investment_cap()


_ext_constant_coal_mines_investment_cap = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Hydrocarbons",
    "COAL_MINES_INVESTMENT_CAP",
    {},
    _root,
    {},
    "_ext_constant_coal_mines_investment_cap",
)


@component.add(
    name="Coal_price_economy_adjusted",
    subscripts=["HYDROCARBONS_W_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "coal_price_index_economy": 1},
)
def coal_price_economy_adjusted():
    return xr.DataArray(
        if_then_else(
            time() < 2015,
            lambda: 100,
            lambda: float(coal_price_index_economy().loc["Coal_W"]),
        ),
        {"HYDROCARBONS_W_I": _subscript_dict["HYDROCARBONS_W_I"]},
        ["HYDROCARBONS_W_I"],
    )


@component.add(
    name='"COAL_PRICE_HISTORICAL_$/t"',
    units="$/t",
    comp_type="Auxiliary",
    comp_subtype="with Lookup",
    depends_on={"time": 1},
)
def coal_price_historical_t():
    """
    Average Coal price of for each year based on the Source: acessed 10.10.2022 - https://tradingeconomics.com/commodity/coal
    """
    return np.interp(
        time(),
        [
            2008.0,
            2009.0,
            2010.0,
            2011.0,
            2012.0,
            2013.0,
            2014.0,
            2015.0,
            2016.0,
            2017.0,
            2018.0,
            2019.0,
            2020.0,
            2021.0,
            2022.0,
        ],
        [
            69.24,
            87.5347,
            108.668,
            108.645,
            95.8592,
            82.5651,
            70.4646,
            63.697,
            71.0204,
            88.1589,
            96.8592,
            88.0457,
            74.4235,
            111.191,
            253.97,
        ],
    )


@component.add(
    name="Coal_price_index_economy",
    subscripts=["HYDROCARBONS_W_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_mat2eco_coal_price": 1,
        "estimated_coal_price_with_tax": 1,
        "coal_base_price_2015": 1,
        "price_transformation": 1,
    },
)
def coal_price_index_economy():
    return xr.DataArray(
        if_then_else(
            switch_mat2eco_coal_price() == 0,
            lambda: 100,
            lambda: (
                float(estimated_coal_price_with_tax().loc["Coal_W"])
                / coal_base_price_2015()
            )
            * price_transformation(),
        ),
        {"HYDROCARBONS_W_I": _subscript_dict["HYDROCARBONS_W_I"]},
        ["HYDROCARBONS_W_I"],
    )


@component.add(
    name="coal_prospecting",
    units="EJ/Year",
    subscripts=["COAL_TYPES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"coal_resources": 2, "coal_prospecting_rate": 2},
)
def coal_prospecting():
    """
    Hard and Brown Coal discovered and moved from resources to the reserves.
    """
    value = xr.DataArray(
        np.nan, {"COAL_TYPES_I": _subscript_dict["COAL_TYPES_I"]}, ["COAL_TYPES_I"]
    )
    value.loc[["HARD_COAL"]] = (
        float(coal_resources().loc["HARD_COAL"]) * coal_prospecting_rate()
    )
    value.loc[["BROWN_COAL"]] = (
        float(coal_resources().loc["BROWN_COAL"]) * coal_prospecting_rate()
    )
    return value


@component.add(
    name="COAL_PROSPECTING_RATE",
    units="1/Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_coal_prospecting_rate"},
)
def coal_prospecting_rate():
    """
    Prospecting rate calibrated to match historical data based on work done in the WORLD 7 model. Estimated by the Authors.
    """
    return _ext_constant_coal_prospecting_rate()


_ext_constant_coal_prospecting_rate = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Hydrocarbons",
    "COAL_PROSPECTING_RATE",
    {},
    _root,
    {},
    "_ext_constant_coal_prospecting_rate",
)


@component.add(
    name="coal_reserves",
    units="EJ",
    subscripts=["COAL_TYPES_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_coal_reserves": 1, "_integ_coal_reserves_1": 1},
    other_deps={
        "_integ_coal_reserves": {
            "initial": {"initial_coal_reserves": 1},
            "step": {"coal_prospecting": 1, "extraction_of_coal": 1},
        },
        "_integ_coal_reserves_1": {
            "initial": {"initial_coal_reserves": 1},
            "step": {"coal_prospecting": 1, "extraction_of_coal": 1},
        },
    },
)
def coal_reserves():
    """
    Hard and Brown Coal in the reserves stock. Initial values based on: Global Energy Assessment-Toward a Sustainable Future (Rogner et al., 2012)
    """
    value = xr.DataArray(
        np.nan, {"COAL_TYPES_I": _subscript_dict["COAL_TYPES_I"]}, ["COAL_TYPES_I"]
    )
    value.loc[["HARD_COAL"]] = _integ_coal_reserves().values
    value.loc[["BROWN_COAL"]] = _integ_coal_reserves_1().values
    return value


_integ_coal_reserves = Integ(
    lambda: xr.DataArray(
        float(coal_prospecting().loc["HARD_COAL"])
        - float(extraction_of_coal().loc["HARD_COAL"]),
        {"COAL_TYPES_I": ["HARD_COAL"]},
        ["COAL_TYPES_I"],
    ),
    lambda: xr.DataArray(
        float(initial_coal_reserves().loc["HARD_COAL"]),
        {"COAL_TYPES_I": ["HARD_COAL"]},
        ["COAL_TYPES_I"],
    ),
    "_integ_coal_reserves",
)

_integ_coal_reserves_1 = Integ(
    lambda: xr.DataArray(
        float(coal_prospecting().loc["BROWN_COAL"])
        - float(extraction_of_coal().loc["BROWN_COAL"]),
        {"COAL_TYPES_I": ["BROWN_COAL"]},
        ["COAL_TYPES_I"],
    ),
    lambda: xr.DataArray(
        float(initial_coal_reserves().loc["BROWN_COAL"]),
        {"COAL_TYPES_I": ["BROWN_COAL"]},
        ["COAL_TYPES_I"],
    ),
    "_integ_coal_reserves_1",
)


@component.add(
    name="coal_resources",
    units="EJ",
    subscripts=["COAL_TYPES_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_coal_resources": 1, "_integ_coal_resources_1": 1},
    other_deps={
        "_integ_coal_resources": {
            "initial": {"initial_coal_resources": 1, "potential_recovery_factor": 1},
            "step": {"coal_prospecting": 1},
        },
        "_integ_coal_resources_1": {
            "initial": {"initial_coal_resources": 1, "potential_recovery_factor": 1},
            "step": {"coal_prospecting": 1},
        },
    },
)
def coal_resources():
    """
    Initial amount of HARD and BROWN COAL in EJ available as resources according to Source: Global Energy Assessment-Toward a Sustainable Future (Rogner et al., 2012)
    """
    value = xr.DataArray(
        np.nan, {"COAL_TYPES_I": _subscript_dict["COAL_TYPES_I"]}, ["COAL_TYPES_I"]
    )
    value.loc[["HARD_COAL"]] = _integ_coal_resources().values
    value.loc[["BROWN_COAL"]] = _integ_coal_resources_1().values
    return value


_integ_coal_resources = Integ(
    lambda: xr.DataArray(
        -float(coal_prospecting().loc["HARD_COAL"]),
        {"COAL_TYPES_I": ["HARD_COAL"]},
        ["COAL_TYPES_I"],
    ),
    lambda: xr.DataArray(
        float(initial_coal_resources().loc["HARD_COAL"]) * potential_recovery_factor(),
        {"COAL_TYPES_I": ["HARD_COAL"]},
        ["COAL_TYPES_I"],
    ),
    "_integ_coal_resources",
)

_integ_coal_resources_1 = Integ(
    lambda: xr.DataArray(
        -float(coal_prospecting().loc["BROWN_COAL"]),
        {"COAL_TYPES_I": ["BROWN_COAL"]},
        ["COAL_TYPES_I"],
    ),
    lambda: xr.DataArray(
        float(initial_coal_resources().loc["BROWN_COAL"]) * potential_recovery_factor(),
        {"COAL_TYPES_I": ["BROWN_COAL"]},
        ["COAL_TYPES_I"],
    ),
    "_integ_coal_resources_1",
)


@component.add(
    name="COAL_URR",
    units="EJ",
    subscripts=["COAL_TYPES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "initial_coal_resources": 1,
        "initial_coal_reserves": 1,
        "initial_coal_cumulatively_extracted_2005": 1,
    },
)
def coal_urr():
    """
    initial availability of resources+reserves of Coal
    """
    return (
        initial_coal_resources()
        + initial_coal_reserves()
        + initial_coal_cumulatively_extracted_2005()
    )


@component.add(
    name="COEFFICIENT_ESTIMATED_OIL_PRICE",
    units="DMNL",
    subscripts=["LINEAR_LOG_FIT_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_coefficient_estimated_oil_price"},
)
def coefficient_estimated_oil_price():
    """
    Parameter of the LN function for calculating the price in $/bbl. The Parameters are derived from fitting the historical data of the oil based on econometric estimation.
    """
    return _ext_constant_coefficient_estimated_oil_price()


_ext_constant_coefficient_estimated_oil_price = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Hydrocarbons",
    "COEFFICIENTS_ESTIMATED_OIL_PRICE*",
    {"LINEAR_LOG_FIT_I": _subscript_dict["LINEAR_LOG_FIT_I"]},
    _root,
    {"LINEAR_LOG_FIT_I": _subscript_dict["LINEAR_LOG_FIT_I"]},
    "_ext_constant_coefficient_estimated_oil_price",
)


@component.add(
    name="COEFFICIENT_GAS_INVESTMENT",
    units="DMNL",
    subscripts=["LINEAR_LOG_FIT_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_coefficient_gas_investment"},
)
def coefficient_gas_investment():
    """
    Parameters are chosen to fit the historical observation of extraction activity and Gas prices. COEFFICIENT GAS INVESTMENT A LINEAR LOG FIT= 6.492 B LINEAR LOG FIT= 0.0066
    """
    return _ext_constant_coefficient_gas_investment()


_ext_constant_coefficient_gas_investment = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Hydrocarbons",
    "COEFFICIENT_GAS_INVESTMENT*",
    {"LINEAR_LOG_FIT_I": _subscript_dict["LINEAR_LOG_FIT_I"]},
    _root,
    {"LINEAR_LOG_FIT_I": _subscript_dict["LINEAR_LOG_FIT_I"]},
    "_ext_constant_coefficient_gas_investment",
)


@component.add(
    name="COEFFICIENT_MAX_COAL_PRICE",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_coefficient_max_coal_price"},
)
def coefficient_max_coal_price():
    """
    Maximum paramenter to limit the coal price function.
    """
    return _ext_constant_coefficient_max_coal_price()


_ext_constant_coefficient_max_coal_price = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Hydrocarbons",
    "COEFFICIENT_MAX_COAL_PRICE",
    {},
    _root,
    {},
    "_ext_constant_coefficient_max_coal_price",
)


@component.add(
    name="COEFFICIENT_MAXIMUM_OIL_PRICE",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_coefficient_maximum_oil_price"},
)
def coefficient_maximum_oil_price():
    """
    A set maximum for the oil price, technical solution to limit the price in cases of scarcity.When not used the price can climb to very high values that might be unreasonable.
    """
    return _ext_constant_coefficient_maximum_oil_price()


_ext_constant_coefficient_maximum_oil_price = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Hydrocarbons",
    "COEFFICIENT_MAXIMUM_OIL_PRICE",
    {},
    _root,
    {},
    "_ext_constant_coefficient_maximum_oil_price",
)


@component.add(
    name="COEFFICIENTS_COAL_MINE_INVESTMENT",
    units="DMNL",
    subscripts=["LINEAR_LOG_FIT_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_coefficients_coal_mine_investment"},
)
def coefficients_coal_mine_investment():
    """
    Estimated Parameters-estimation based on calibration of the price function against the historical price. A LINEAR LOG FIT = -64.2104 B LINEAR LOG FIT = 2.03759
    """
    return _ext_constant_coefficients_coal_mine_investment()


_ext_constant_coefficients_coal_mine_investment = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Hydrocarbons",
    "COEFFICIENTS_COAL_MINE_INVESTMENT*",
    {"LINEAR_LOG_FIT_I": _subscript_dict["LINEAR_LOG_FIT_I"]},
    _root,
    {"LINEAR_LOG_FIT_I": _subscript_dict["LINEAR_LOG_FIT_I"]},
    "_ext_constant_coefficients_coal_mine_investment",
)


@component.add(
    name="COEFFICIENTS_ESTIMATED_PRICE",
    units="DMNL",
    subscripts=["EXP_CURVE_FIT_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_coefficients_estimated_price"},
)
def coefficients_estimated_price():
    """
    Estimated Parameters-estimation based on calibration of the price function against the historical price. A EXP CURVE 3.55372 B EXP CURVE 0.282675 C EXP CURVE 0
    """
    return _ext_constant_coefficients_estimated_price()


_ext_constant_coefficients_estimated_price = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Hydrocarbons",
    "COEFFICIENTS_ESTIMATED_PRICE*",
    {"EXP_CURVE_FIT_I": _subscript_dict["EXP_CURVE_FIT_I"]},
    _root,
    {"EXP_CURVE_FIT_I": _subscript_dict["EXP_CURVE_FIT_I"]},
    "_ext_constant_coefficients_estimated_price",
)


@component.add(
    name="COEFFICIENTS_ESTIMATED_PRICE_GAS",
    units="DMNL",
    subscripts=["EXP_CURVE_FIT_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_coefficients_estimated_price_gas"},
)
def coefficients_estimated_price_gas():
    """
    Parameter of the LN function for calculating the price in $/Btu. The Parameters are derived from fitting the historical data of the Gas. A EXP CURVE -1.326 B EXP CURVE -0.0319 C EXP CURVE 0.814
    """
    return _ext_constant_coefficients_estimated_price_gas()


_ext_constant_coefficients_estimated_price_gas = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Hydrocarbons",
    "COEFFIECIENTS_ESTIMATED_PRICE_GAS*",
    {"EXP_CURVE_FIT_I": _subscript_dict["EXP_CURVE_FIT_I"]},
    _root,
    {"EXP_CURVE_FIT_I": _subscript_dict["EXP_CURVE_FIT_I"]},
    "_ext_constant_coefficients_estimated_price_gas",
)


@component.add(
    name="COEFFICIENTS_WELL_INVESTMENT",
    units="DMNL",
    subscripts=["LINEAR_LOG_FIT_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_coefficients_well_investment"},
)
def coefficients_well_investment():
    """
    Parameters are chosen to fit the historical observation of drilling activity and oil prices. A=50958.6 B= 328.36 Assumption made by the Authors of this model. The underlying idea of this assumption is that even when there is a high demand and price increase for Oil, there is a limitation to which extant the demand and price translates into infrastructure investment due to capacity limitations. Source the Authors based their assumption on: Used a liniar function that describes the relation of the oil price to wells drilled in that year. Based on Historical Oil prices and drilling activities. Parameters of that function are derived by matching historical data and economentric estimations. https://www.rystadenergy.com/newsevents/news/newsletters/OfsArchive/ofs-november-2018 / https://www.drillingcontractor.org/670000-wells-to-be-drilled-through-2020-28709 https://www.rystadenergy.com/energy-themes/supply-chain/wells/well-cube/ https://www.eia.gov/dnav/pet/hist/LeafHandler.ashx?n=pet&s=rwtc&f=a
    """
    return _ext_constant_coefficients_well_investment()


_ext_constant_coefficients_well_investment = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Hydrocarbons",
    "COEFFICIENTS_WELL_INVESTMENT*",
    {"LINEAR_LOG_FIT_I": _subscript_dict["LINEAR_LOG_FIT_I"]},
    _root,
    {"LINEAR_LOG_FIT_I": _subscript_dict["LINEAR_LOG_FIT_I"]},
    "_ext_constant_coefficients_well_investment",
)


@component.add(
    name="COEFFIECIENTS_OPEC_SPARE_CAP",
    subscripts=["EXP_CURVE_FIT_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_coeffiecients_opec_spare_cap"},
)
def coeffiecients_opec_spare_cap():
    """
    Parameter chosen to match the historical data of the opec spare capacity.Parameters derived by econometric estimations. A =-1.97698 B = 0.0292976 C = 53.0393
    """
    return _ext_constant_coeffiecients_opec_spare_cap()


_ext_constant_coeffiecients_opec_spare_cap = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Hydrocarbons",
    "COEFFICIENTS_OPEC_SPARE_CAP*",
    {"EXP_CURVE_FIT_I": _subscript_dict["EXP_CURVE_FIT_I"]},
    _root,
    {"EXP_CURVE_FIT_I": _subscript_dict["EXP_CURVE_FIT_I"]},
    "_ext_constant_coeffiecients_opec_spare_cap",
)


@component.add(
    name="cumulative_coal_extracted",
    units="EJ",
    subscripts=["COAL_TYPES_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={
        "_integ_cumulative_coal_extracted": 1,
        "_integ_cumulative_coal_extracted_1": 1,
    },
    other_deps={
        "_integ_cumulative_coal_extracted": {
            "initial": {"initial_coal_cumulatively_extracted_2005": 1},
            "step": {"total_coal_mined": 1},
        },
        "_integ_cumulative_coal_extracted_1": {
            "initial": {"initial_coal_cumulatively_extracted_2005": 1},
            "step": {"total_coal_mined": 1},
        },
    },
)
def cumulative_coal_extracted():
    """
    Extracted Coal from 1978 onwards. Source: Global Energy Assessment-Toward a Sustainable Future (Rogner et al., 2012)
    """
    value = xr.DataArray(
        np.nan, {"COAL_TYPES_I": _subscript_dict["COAL_TYPES_I"]}, ["COAL_TYPES_I"]
    )
    value.loc[["HARD_COAL"]] = _integ_cumulative_coal_extracted().values
    value.loc[["BROWN_COAL"]] = _integ_cumulative_coal_extracted_1().values
    return value


_integ_cumulative_coal_extracted = Integ(
    lambda: xr.DataArray(
        float(total_coal_mined().loc["HARD_COAL"]),
        {"COAL_TYPES_I": ["HARD_COAL"]},
        ["COAL_TYPES_I"],
    ),
    lambda: xr.DataArray(
        float(initial_coal_cumulatively_extracted_2005().loc["HARD_COAL"]),
        {"COAL_TYPES_I": ["HARD_COAL"]},
        ["COAL_TYPES_I"],
    ),
    "_integ_cumulative_coal_extracted",
)

_integ_cumulative_coal_extracted_1 = Integ(
    lambda: xr.DataArray(
        float(total_coal_mined().loc["BROWN_COAL"]),
        {"COAL_TYPES_I": ["BROWN_COAL"]},
        ["COAL_TYPES_I"],
    ),
    lambda: xr.DataArray(
        float(initial_coal_cumulatively_extracted_2005().loc["BROWN_COAL"]),
        {"COAL_TYPES_I": ["BROWN_COAL"]},
        ["COAL_TYPES_I"],
    ),
    "_integ_cumulative_coal_extracted_1",
)


@component.add(
    name="cumulative_extracted_gas",
    units="EJ",
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_cumulative_extracted_gas": 1},
    other_deps={
        "_integ_cumulative_extracted_gas": {
            "initial": {"initial_total_gas_extracted": 1},
            "step": {"total_gas_extracted": 1},
        }
    },
)
def cumulative_extracted_gas():
    """
    Gas that has already been extracted until 2005- Source: BGR (2017) Bundesanstalt für Geowissenschaften und Rohstoffe (BGR), 2017. Energy Study: Data and Developments Concerning German and Global Energy Supplies - extraction from 2005 to 2017 data taken from BP Stat review. 2022 Report.
    """
    return _integ_cumulative_extracted_gas()


_integ_cumulative_extracted_gas = Integ(
    lambda: total_gas_extracted(),
    lambda: initial_total_gas_extracted(),
    "_integ_cumulative_extracted_gas",
)


@component.add(
    name="cumulative_total_oil_extraction",
    units="bbl",
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_cumulative_total_oil_extraction": 1},
    other_deps={
        "_integ_cumulative_total_oil_extraction": {
            "initial": {"initial_oil_cumulatively_extracted_2005": 1},
            "step": {"total_oil_extracted": 1},
        }
    },
)
def cumulative_total_oil_extraction():
    """
    According to the Source the cumulative amount of oil already extracted and used until the year 2005 According to estimates based on - SOURCE, conventional and unconventional oil resources are available for discovery.Recalculated into bbl. Source: Meta-analysis of non-renewable energy resource estimates Author:MichaelDale https://doi.org/10.1016/j.enpol.2011.12.039 Projection of world fossil fuels by country Author: S.H.Mohr https://doi.org/10.1016/j.fuel.2014.10.030 There should be a separation between conventional and unconventional Oil in a later approach.
    """
    return _integ_cumulative_total_oil_extraction()


_integ_cumulative_total_oil_extraction = Integ(
    lambda: total_oil_extracted(),
    lambda: initial_oil_cumulatively_extracted_2005(),
    "_integ_cumulative_total_oil_extraction",
)


@component.add(
    name="current_Gas_extraction",
    units="EJ/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"gas_max_extraction_capacity": 1, "actual_spare_capacity_gas": 1},
)
def current_gas_extraction():
    """
    The current Gas extraction is a function of the number of Gas extraction capacity taking the spare capacity into account.
    """
    return gas_max_extraction_capacity() * (1 - actual_spare_capacity_gas())


@component.add(
    name="current_Oil_extraction",
    units="bbl/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "number_of_oil_wells": 1,
        "oil_per_oil_well": 1,
        "actual_spare_capacity": 1,
    },
)
def current_oil_extraction():
    """
    The current Oil extraction is a function of the number of Oil wells and production of oil per well taking the spare capacity into account.
    """
    return number_of_oil_wells() * oil_per_oil_well() * (1 - actual_spare_capacity())


@component.add(
    name="delayed_estimated_Oil_price",
    units="$/bbl",
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_estimated_oil_price": 1},
    other_deps={
        "_delayfixed_delayed_estimated_oil_price": {
            "initial": {"time_step": 1},
            "step": {"estimated_oil_price": 1},
        }
    },
)
def delayed_estimated_oil_price():
    """
    Delayed estimated price.
    """
    return _delayfixed_delayed_estimated_oil_price()


_delayfixed_delayed_estimated_oil_price = DelayFixed(
    lambda: estimated_oil_price(),
    lambda: time_step(),
    lambda: 100,
    time_step,
    "_delayfixed_delayed_estimated_oil_price",
)


@component.add(
    name="delayed_first_estimated_Oil_price",
    units="$/bbl",
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_first_estimated_oil_price": 1},
    other_deps={
        "_delayfixed_delayed_first_estimated_oil_price": {
            "initial": {"time_step": 1},
            "step": {"first_estimated_oil_price": 1},
        }
    },
)
def delayed_first_estimated_oil_price():
    """
    Delayed first estimated oil price. Used to calculate the variation between timesteps and to avoid simultonous calculations.
    """
    return _delayfixed_delayed_first_estimated_oil_price()


_delayfixed_delayed_first_estimated_oil_price = DelayFixed(
    lambda: first_estimated_oil_price(),
    lambda: time_step(),
    lambda: 100,
    time_step,
    "_delayfixed_delayed_first_estimated_oil_price",
)


@component.add(
    name="delayed_TS_coal_price_economy_adjusted",
    units="DMNL",
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_coal_price_economy_adjusted": 1},
    other_deps={
        "_delayfixed_delayed_ts_coal_price_economy_adjusted": {
            "initial": {"time_step": 1},
            "step": {"coal_price_economy_adjusted": 1},
        }
    },
)
def delayed_ts_coal_price_economy_adjusted():
    """
    Delayed coal price economy adjusted.
    """
    return _delayfixed_delayed_ts_coal_price_economy_adjusted()


_delayfixed_delayed_ts_coal_price_economy_adjusted = DelayFixed(
    lambda: float(coal_price_economy_adjusted().loc["Coal_W"]),
    lambda: time_step(),
    lambda: 100,
    time_step,
    "_delayfixed_delayed_ts_coal_price_economy_adjusted",
)


@component.add(
    name="delayed_TS_gas_price_economy_adjusted",
    units="DMNL",
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_gas_price_economy_adjusted": 1},
    other_deps={
        "_delayfixed_delayed_ts_gas_price_economy_adjusted": {
            "initial": {"time_step": 1},
            "step": {"gas_price_econmy_adjusted_1": 1},
        }
    },
)
def delayed_ts_gas_price_economy_adjusted():
    """
    Delayed natural gas (fossil) price economy adjusted. Delay is used to prevent simultanious equations.
    """
    return _delayfixed_delayed_ts_gas_price_economy_adjusted()


_delayfixed_delayed_ts_gas_price_economy_adjusted = DelayFixed(
    lambda: gas_price_econmy_adjusted_1(),
    lambda: time_step(),
    lambda: 100,
    time_step,
    "_delayfixed_delayed_ts_gas_price_economy_adjusted",
)


@component.add(
    name="delayed_TS_oil_price_economy_adjusted",
    units="DMNL",
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_oil_price_economy_adjusted": 1},
    other_deps={
        "_delayfixed_delayed_ts_oil_price_economy_adjusted": {
            "initial": {"time_step": 1},
            "step": {"oil_price_economy_adjusted": 1},
        }
    },
)
def delayed_ts_oil_price_economy_adjusted():
    """
    Delayed oil price economy adjusted. Delay is used to prevent simultanious equations.
    """
    return _delayfixed_delayed_ts_oil_price_economy_adjusted()


_delayfixed_delayed_ts_oil_price_economy_adjusted = DelayFixed(
    lambda: oil_price_economy_adjusted(),
    lambda: time_step(),
    lambda: 100,
    time_step,
    "_delayfixed_delayed_ts_oil_price_economy_adjusted",
)


@component.add(
    name="DEPLETION_FACTOR_AFTER_PEAK",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_depletion_factor_after_peak"},
)
def depletion_factor_after_peak():
    """
    Assumption made by the authors that wells are depletiing faster when the half of URR is reached. It is a simplification because in the real world the productivity per well would decrease if the well production peak is reached.The authors of the model assume that the lifetime of a well is shorter when half of URR is reached, which basically means that a well has a shorter operating time and needs to be replaced faster. value is 9.5
    """
    return _ext_constant_depletion_factor_after_peak()


_ext_constant_depletion_factor_after_peak = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Hydrocarbons",
    "DEPLETION_FACTOR_AFTER_PEAK",
    {},
    _root,
    {},
    "_ext_constant_depletion_factor_after_peak",
)


@component.add(
    name="DEPLETION_FACTOR_AFTER_PEAK_COAL", comp_type="Constant", comp_subtype="Normal"
)
def depletion_factor_after_peak_coal():
    return 0


@component.add(
    name="depletion_of_coal_mines",
    units="mines/Year",
    subscripts=["COAL_TYPES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "number_of_operating_coal_mines": 2,
        "increase_in_depletion_after_peak_coal": 2,
    },
)
def depletion_of_coal_mines():
    """
    Number of mines that are decomissioned per year.
    """
    value = xr.DataArray(
        np.nan, {"COAL_TYPES_I": _subscript_dict["COAL_TYPES_I"]}, ["COAL_TYPES_I"]
    )
    value.loc[["HARD_COAL"]] = float(
        number_of_operating_coal_mines().loc["HARD_COAL"]
    ) * float(increase_in_depletion_after_peak_coal().loc["HARD_COAL"])
    value.loc[["BROWN_COAL"]] = float(
        number_of_operating_coal_mines().loc["BROWN_COAL"]
    ) * float(increase_in_depletion_after_peak_coal().loc["BROWN_COAL"])
    return value


@component.add(
    name="depletion_of_extraction_capacity",
    units="EJ/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"extraction_capacity_of_gas": 1, "increase_in_depletion_gas": 1},
)
def depletion_of_extraction_capacity():
    """
    Amount ofextraction capacity (wells) that is are going out of service per year.
    """
    return extraction_capacity_of_gas() * increase_in_depletion_gas()


@component.add(
    name="depletion_of_oil_wells",
    units="wells/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"number_of_oil_wells": 1, "oil_well_depletion_rate": 1},
)
def depletion_of_oil_wells():
    """
    Number of wells that is are going out of service per year.
    """
    return number_of_oil_wells() * oil_well_depletion_rate()


@component.add(
    name="desired_desired_gas_extraction_capacity",
    units="EJ/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "estimated_gas_price": 2,
        "minimum_gas_price_for_investment": 1,
        "coefficient_gas_investment": 2,
    },
)
def desired_desired_gas_extraction_capacity():
    """
    Assumption made by the Authors of this model. The underlying idea of this assumption is that even when there is a high demand and price increase for Gas, there is a limitation to which extant the demand and price translates into infrastructure investment due to capacity limitations. Based on the work for the Oil model: Source the Authors based their assumption on: Used a liniar function that describes the relation of the oil price to wells drilled in that year. Based on Historical Oil prices and drilling activities. adapted to fit the gas model. The Aussumption is that minimal price of gas is nessesary to invest into gas extraction capacity. If the price is above the minimum price than investment is done in gas extraction capacity. The higher the price the higher the investment in extraction capacity, what follow is a higher extraction capacity. https://www.rystadenergy.com/newsevents/news/newsletters/OfsArchive/ofs-november-2018 / https://www.drillingcontractor.org/670000-wells-to-be-drilled-through-2020-28709 https://www.rystadenergy.com/energy-themes/supply-chain/wells/well-cube/ https://www.eia.gov/dnav/pet/hist/LeafHandler.ashx?n=pet&s=rwtc&f=a
    """
    return if_then_else(
        estimated_gas_price() <= minimum_gas_price_for_investment(),
        lambda: 0,
        lambda: float(coefficient_gas_investment().loc["A_LINEAR_LOG_FIT"])
        + float(coefficient_gas_investment().loc["B_LINEAR_LOG_FIT"])
        * estimated_gas_price(),
    )


@component.add(
    name="desired_new_coal_mines",
    units="mines/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"coefficients_coal_mine_investment": 2, "estimated_coal_price": 1},
)
def desired_new_coal_mines():
    """
    Funktion calculates the number of desired mines based on the price of coal.
    """
    return (
        float(coefficients_coal_mine_investment().loc["A_LINEAR_LOG_FIT"])
        + float(coefficients_coal_mine_investment().loc["B_LINEAR_LOG_FIT"])
        * estimated_coal_price()
    )


@component.add(
    name="desired_Oil_wells",
    units="wells/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "estimated_oil_price": 2,
        "minimum_oil_price_for_investment": 1,
        "coefficients_well_investment": 2,
    },
)
def desired_oil_wells():
    """
    Assumption made by the Authors of this model. The underlying idea of this assumption is that even when there is a high demand and price increase for Oil, there is a limitation to which extant the demand and price translates into infrastructure investment due to capacity limitations. Source the Authors based their assumption on: Used a liniar function that describes the relation of the oil price to wells drilled in that year. Based on Historical Oil prices and drilling activities. Parameters of that function are derived by matching historical data and economentric estimations. https://www.rystadenergy.com/newsevents/news/newsletters/OfsArchive/ofs-november-2018 / https://www.drillingcontractor.org/670000-wells-to-be-drilled-through-2020-28709 https://www.rystadenergy.com/energy-themes/supply-chain/wells/well-cube/ https://www.eia.gov/dnav/pet/hist/LeafHandler.ashx?n=pet&s=rwtc&f=a
    """
    return if_then_else(
        estimated_oil_price() <= minimum_oil_price_for_investment(),
        lambda: 0,
        lambda: float(coefficients_well_investment().loc["A_LINEAR_LOG_FIT"])
        + float(coefficients_well_investment().loc["B_LINEAR_LOG_FIT"])
        * estimated_oil_price(),
    )


@component.add(
    name="estimated_coal_price",
    units="$/t",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"coefficients_estimated_price": 2, "ln_of_the_coal_spare_cap": 1},
)
def estimated_coal_price():
    """
    Function to calculate the coal price based on the tension between supply and demand.Parameters for the function derived by matching the historical price data.
    """
    return np.exp(
        float(coefficients_estimated_price().loc["A_EXP_CURVE"])
        + float(coefficients_estimated_price().loc["B_EXP_CURVE"])
        * ln_of_the_coal_spare_cap()
    )


@component.add(
    name="estimated_coal_price_with_tax",
    units="$/t",
    subscripts=["HYDROCARBONS_W_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "initial_year_tax_rate_on_extraction_of_resources_sp": 1,
        "switch_tax_rate_on_extraction_of_resources_sp": 1,
        "estimated_coal_price": 3,
        "tax_rate_on_extraction_of_resources_sp": 1,
    },
)
def estimated_coal_price_with_tax():
    return xr.DataArray(
        if_then_else(
            np.logical_and(
                time() >= initial_year_tax_rate_on_extraction_of_resources_sp(),
                switch_tax_rate_on_extraction_of_resources_sp(),
            ),
            lambda: estimated_coal_price()
            + estimated_coal_price()
            * float(tax_rate_on_extraction_of_resources_sp().loc["Coal_W"]),
            lambda: estimated_coal_price(),
        ),
        {"HYDROCARBONS_W_I": _subscript_dict["HYDROCARBONS_W_I"]},
        ["HYDROCARBONS_W_I"],
    )


@component.add(
    name="estimated_Gas_price",
    units="$/million_Btu",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "coefficients_estimated_price_gas": 3,
        "gas_extraction_capacity_excluding_spare_capacity": 1,
        "estimated_oil_price": 1,
    },
)
def estimated_gas_price():
    """
    Gas price calculation based on spare capacity, Gas demand and Gas available and Oil price. LN function is calculating the price in $/Btu. The Parameters are derived from fitting the historical data of the Gas price development. Intermediate step for the Gas price calculation. Calculation is based on a LN function which describes the relation between Gas demand per year and Gas available without the spare capacity. The function covers the relation of the Gas price, the oil price and the behaviour of the Opec countries which try to control the oil and gas price.
    """
    return np.exp(
        float(coefficients_estimated_price_gas().loc["A_EXP_CURVE"])
        + float(coefficients_estimated_price_gas().loc["B_EXP_CURVE"])
        * np.log(1 / gas_extraction_capacity_excluding_spare_capacity())
        + float(coefficients_estimated_price_gas().loc["C_EXP_CURVE"])
        * np.log(estimated_oil_price())
    )


@component.add(
    name="estimated_gas_price_with_tax",
    units="$/million_Btu",
    subscripts=["HYDROCARBONS_W_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "initial_year_tax_rate_on_extraction_of_resources_sp": 1,
        "switch_tax_rate_on_extraction_of_resources_sp": 1,
        "estimated_gas_price": 3,
        "tax_rate_on_extraction_of_resources_sp": 1,
    },
)
def estimated_gas_price_with_tax():
    """
    Either the estimated Gas price is used or the estimated gas price plus a resource tax.Depending if the policy is activated or not.
    """
    return xr.DataArray(
        if_then_else(
            np.logical_and(
                time() >= initial_year_tax_rate_on_extraction_of_resources_sp(),
                switch_tax_rate_on_extraction_of_resources_sp(),
            ),
            lambda: estimated_gas_price()
            * float(tax_rate_on_extraction_of_resources_sp().loc["Gas_W"])
            + estimated_gas_price(),
            lambda: estimated_gas_price(),
        ),
        {"HYDROCARBONS_W_I": _subscript_dict["HYDROCARBONS_W_I"]},
        ["HYDROCARBONS_W_I"],
    )


@component.add(
    name="estimated_Oil_price",
    units="$/bbl",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "first_estimated_oil_price": 2,
        "switch_oil_price_growth_limit": 1,
        "delayed_estimated_oil_price": 1,
        "estimated_oil_price_variation": 1,
    },
)
def estimated_oil_price():
    """
    Oil price calculation based on historic data of opec spare cap, oil demand and oil available. LN function is calculating the price in $/bbl. The Parameters are derived from fitting the historical data of the oil price development, parameters derived from econometric estimations. The time step variation is limited to avoid extreme oscialtions.
    """
    return if_then_else(
        time() <= 2015,
        lambda: first_estimated_oil_price(),
        lambda: if_then_else(
            switch_oil_price_growth_limit() == 1,
            lambda: delayed_estimated_oil_price()
            * (1 + estimated_oil_price_variation()),
            lambda: first_estimated_oil_price(),
        ),
    )


@component.add(
    name="estimated_Oil_price_variation",
    units="DMML",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "delayed_first_estimated_oil_price": 4,
        "max_oil_price_for_limit": 1,
        "oil_price_growth_limit": 4,
        "first_estimated_oil_price": 3,
    },
)
def estimated_oil_price_variation():
    """
    Variation of oil price by time step. This is limited to a certain thershold in orther to avoid very high oscilations.
    """
    return if_then_else(
        delayed_first_estimated_oil_price() > max_oil_price_for_limit(),
        lambda: oil_price_growth_limit(),
        lambda: if_then_else(
            zidz(first_estimated_oil_price(), delayed_first_estimated_oil_price()) - 1
            < oil_price_growth_limit(),
            lambda: np.maximum(
                zidz(first_estimated_oil_price(), delayed_first_estimated_oil_price())
                - 1,
                -oil_price_growth_limit(),
            ),
            lambda: np.minimum(
                zidz(first_estimated_oil_price(), delayed_first_estimated_oil_price())
                - 1,
                oil_price_growth_limit(),
            ),
        ),
    )


@component.add(
    name="estimated_oil_price_with_tax",
    units="$/bbl",
    subscripts=["HYDROCARBONS_W_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "initial_year_tax_rate_on_extraction_of_resources_sp": 1,
        "switch_tax_rate_on_extraction_of_resources_sp": 1,
        "estimated_oil_price": 3,
        "tax_rate_on_extraction_of_resources_sp": 1,
    },
)
def estimated_oil_price_with_tax():
    """
    The price calculated by the model with an added resource tax for extraction.
    """
    return xr.DataArray(
        if_then_else(
            np.logical_and(
                time() >= initial_year_tax_rate_on_extraction_of_resources_sp(),
                switch_tax_rate_on_extraction_of_resources_sp() == 1,
            ),
            lambda: estimated_oil_price()
            + estimated_oil_price()
            * float(tax_rate_on_extraction_of_resources_sp().loc["Oil_W"]),
            lambda: estimated_oil_price(),
        ),
        {"HYDROCARBONS_W_I": _subscript_dict["HYDROCARBONS_W_I"]},
        ["HYDROCARBONS_W_I"],
    )


@component.add(
    name="estimated_price_with_tax_metals",
    units="$/t",
    subscripts=["METALS_W_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 4,
        "initial_year_tax_rate_on_extraction_of_resources_sp": 4,
        "switch_tax_rate_on_extraction_of_resources_sp": 4,
        "cu_price_economy": 3,
        "tax_rate_on_extraction_of_resources_sp": 4,
        "al_price_economy": 3,
        "fe_price_economy": 3,
        "ni_price_economy": 3,
    },
)
def estimated_price_with_tax_metals():
    """
    Estimated price plus an additional resource tax rate.
    """
    value = xr.DataArray(
        np.nan, {"METALS_W_I": _subscript_dict["METALS_W_I"]}, ["METALS_W_I"]
    )
    value.loc[["Cu_W"]] = if_then_else(
        np.logical_and(
            time() >= initial_year_tax_rate_on_extraction_of_resources_sp(),
            switch_tax_rate_on_extraction_of_resources_sp() == 1,
        ),
        lambda: cu_price_economy()
        + cu_price_economy()
        * float(tax_rate_on_extraction_of_resources_sp().loc["Cu_W"]),
        lambda: cu_price_economy(),
    )
    value.loc[["Al_W"]] = if_then_else(
        np.logical_and(
            time() >= initial_year_tax_rate_on_extraction_of_resources_sp(),
            switch_tax_rate_on_extraction_of_resources_sp() == 1,
        ),
        lambda: al_price_economy()
        + al_price_economy()
        * float(tax_rate_on_extraction_of_resources_sp().loc["Al_W"]),
        lambda: al_price_economy(),
    )
    value.loc[["Fe_W"]] = if_then_else(
        np.logical_and(
            time() >= initial_year_tax_rate_on_extraction_of_resources_sp(),
            switch_tax_rate_on_extraction_of_resources_sp() == 1,
        ),
        lambda: fe_price_economy()
        + fe_price_economy()
        * float(tax_rate_on_extraction_of_resources_sp().loc["Fe_W"]),
        lambda: fe_price_economy(),
    )
    value.loc[["Ni_W"]] = if_then_else(
        np.logical_and(
            time() >= initial_year_tax_rate_on_extraction_of_resources_sp(),
            switch_tax_rate_on_extraction_of_resources_sp() == 1,
        ),
        lambda: ni_price_economy()
        + ni_price_economy()
        * float(tax_rate_on_extraction_of_resources_sp().loc["Ni_W"]),
        lambda: ni_price_economy(),
    )
    return value


@component.add(
    name="extraction_capacity_of_Gas",
    units="EJ",
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_extraction_capacity_of_gas": 1},
    other_deps={
        "_integ_extraction_capacity_of_gas": {
            "initial": {"initial_extraction_capacity": 1},
            "step": {
                "investment_in_gas_extraction_capacity": 1,
                "depletion_of_extraction_capacity": 1,
            },
        }
    },
)
def extraction_capacity_of_gas():
    """
    Current extraction capacity of natural gas.
    """
    return _integ_extraction_capacity_of_gas()


_integ_extraction_capacity_of_gas = Integ(
    lambda: investment_in_gas_extraction_capacity()
    - depletion_of_extraction_capacity(),
    lambda: initial_extraction_capacity(),
    "_integ_extraction_capacity_of_gas",
)


@component.add(
    name="extraction_of_coal",
    units="EJ/Year",
    subscripts=["COAL_TYPES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_coal_production_capacity_ej": 2},
)
def extraction_of_coal():
    """
    Mining of HARD and BROWN coal in EJ per Year
    """
    value = xr.DataArray(
        np.nan, {"COAL_TYPES_I": _subscript_dict["COAL_TYPES_I"]}, ["COAL_TYPES_I"]
    )
    value.loc[["HARD_COAL"]] = float(
        total_coal_production_capacity_ej().loc["HARD_COAL"]
    )
    value.loc[["BROWN_COAL"]] = float(
        total_coal_production_capacity_ej().loc["BROWN_COAL"]
    )
    return value


@component.add(
    name="extraction_of_gas",
    units="EJ/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"current_gas_extraction": 1},
)
def extraction_of_gas():
    """
    Gas flow that is currently extracted.
    """
    return current_gas_extraction()


@component.add(
    name="extraction_of_Oil",
    units="bbl/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"current_oil_extraction": 1},
)
def extraction_of_oil():
    """
    Oil that is currently extracted per year, based on the average production per well and the number of active wells.
    """
    return current_oil_extraction()


@component.add(
    name="first_estimated_Oil_price",
    units="$/bbl",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "coefficient_estimated_oil_price": 2,
        "oil_extraction_spare_capacity_excluding_opec": 1,
    },
)
def first_estimated_oil_price():
    """
    Oil price calculation based on historic data of opec spare cap, oil demand and oil available. LN function is calculating the price in $/bbl. The Parameters are derived from fitting the historical data of the oil price development and econometric estimations.
    """
    return np.exp(
        float(coefficient_estimated_oil_price().loc["A_LINEAR_LOG_FIT"])
        + float(coefficient_estimated_oil_price().loc["B_LINEAR_LOG_FIT"])
        * np.log(1 / oil_extraction_spare_capacity_excluding_opec())
    )


@component.add(
    name="Gas_base_price_2015",
    units="$/million_Btu",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_gas_base_price_2015"},
)
def gas_base_price_2015():
    """
    Gas price of the year 2015 in $/million Btu. Price taken from BP Statistical Review of World Energy June 2022. Average over the regions. value in the year 2016 = 6.24 $/million Btu
    """
    return _ext_constant_gas_base_price_2015()


_ext_constant_gas_base_price_2015 = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Hydrocarbons",
    "GAS_BASE_PRICE_2015",
    {},
    _root,
    {},
    "_ext_constant_gas_base_price_2015",
)


@component.add(
    name="Gas_demand_1",
    units="EJ/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "switch_nrg2mat_gas_demand": 1,
        "switch_materials": 1,
        "historical_gas_demand": 1,
        "world_pe_gas_ej": 1,
    },
)
def gas_demand_1():
    """
    Gas demand in EJ/year. Either taken from historical data or coming from the interlinked module. Connection between the Economy,Energy and materials.
    """
    return if_then_else(
        np.logical_or(
            time() < 2015,
            np.logical_or(switch_nrg2mat_gas_demand() == 0, switch_materials() == 0),
        ),
        lambda: historical_gas_demand(),
        lambda: world_pe_gas_ej(),
    )


@component.add(
    name="Gas_extraction_capacity_excluding_spare_capacity",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"gas_demand_1": 1, "gas_extraction_without_spare_cap": 1},
)
def gas_extraction_capacity_excluding_spare_capacity():
    """
    Intermediate step for the Gas price calculation. Calculation is based on a LN function which describes the relation between Gas demand per year and Gas available without the spare capacity. The function covers the relation of the Gas price, the oil price and the behaviour of the Opec countries which try to control the oil and gas price.
    """
    return np.maximum(1 - gas_demand_1() / gas_extraction_without_spare_cap(), 0.0005)


@component.add(
    name="Gas_extraction_without_spare_cap",
    units="EJ",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"gas_max_extraction_capacity": 1, "actual_spare_capacity_gas": 1},
)
def gas_extraction_without_spare_cap():
    """
    Gas extraction without the actual spare capcity.
    """
    return gas_max_extraction_capacity() - actual_spare_capacity_gas()


@component.add(
    name="GAS_INVESTMENT_CAP",
    units="1/Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_gas_investment_cap"},
)
def gas_investment_cap():
    """
    Maximun growth rate of active wells. This rate was chosen on the bases of the historical maximum growth in drilling activity in drilling of Oil wells. The authors adapted this value for the Gas extraction capacity. Value = 0.064
    """
    return _ext_constant_gas_investment_cap()


_ext_constant_gas_investment_cap = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Hydrocarbons",
    "GAS_INVESTMENT_CAP",
    {},
    _root,
    {},
    "_ext_constant_gas_investment_cap",
)


@component.add(
    name="Gas_max_extraction_capacity",
    units="EJ",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"extraction_capacity_of_gas": 1},
)
def gas_max_extraction_capacity():
    """
    Maximium Gas extraction capacity per year
    """
    return extraction_capacity_of_gas()


@component.add(
    name="Gas_price_econmy_adjusted_1",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "gas_price_index_economy_0": 1},
)
def gas_price_econmy_adjusted_1():
    """
    Gas price for the years 2005 to 2015 is set to 100 as a starting value-nominal price in the economy module. After 2015- Gas price index economy. The reason for this is that the materials module is starting in 2005, and is simulating with an historical demand until 2015. The economy module starts to simulate in the year 2015. The material module reports fixed values from 2005 to 2015 to the economy module, at 2015 dynamic values are involved in the economy module.
    """
    return if_then_else(
        time() < 2015,
        lambda: 100,
        lambda: float(gas_price_index_economy_0().loc["Gas_W"]),
    )


@component.add(
    name="GAS_PRICE_HISTORICAL",
    units="$/million_Btu",
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_gas_price_historical",
        "__data__": "_ext_data_gas_price_historical",
        "time": 1,
    },
)
def gas_price_historical():
    """
    Historical Gas price avergae over the different price region. Taken from BP Stat. Review. 2022.
    """
    return _ext_data_gas_price_historical(time())


_ext_data_gas_price_historical = ExtData(
    "model_parameters/materials/materials.xlsx",
    "Hydrocarbons",
    "TIME_SERIES_HYDRO",
    "GAS_PRICE_HISTORICAL",
    None,
    {},
    _root,
    {},
    "_ext_data_gas_price_historical",
)


@component.add(
    name="Gas_price_index_economy_0",
    units="DMNL",
    subscripts=["HYDROCARBONS_W_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_mat2eco_gas_price": 1,
        "percent_price_transformation": 1,
        "estimated_gas_price_with_tax": 1,
        "gas_base_price_2015": 1,
    },
)
def gas_price_index_economy_0():
    """
    Calculation of the estimated Gas price based on the price of estimated Gas price divided by the base price for the starting year of the economy module (2015) the result should be in the first year (2015) = 1 and then multiplied with hundered. This is the nominal price signal used in the economy module. With changes of the estimated Gas price variable which will be depending on the supply and demand situation changes in the nominal price will occour Price Index that gets delivered to the econimic model. IF THEN ELSE and the switch are used to try different things. (estimated Gas price/Gas base price 2015)*PERCENT PRICE TRANSFORMATION
    """
    return xr.DataArray(
        if_then_else(
            switch_mat2eco_gas_price() == 0,
            lambda: 100,
            lambda: (
                float(estimated_gas_price_with_tax().loc["Gas_W"])
                / gas_base_price_2015()
            )
            * percent_price_transformation(),
        ),
        {"HYDROCARBONS_W_I": _subscript_dict["HYDROCARBONS_W_I"]},
        ["HYDROCARBONS_W_I"],
    )


@component.add(
    name="GAS_price_jump_look_up",
    comp_type="Auxiliary",
    comp_subtype="with Lookup",
    depends_on={"time": 1},
)
def gas_price_jump_look_up():
    """
    GAs look up table for testing the loop between economy and materials.
    """
    return np.interp(
        time(),
        [
            2005,
            2006,
            2007,
            2008,
            2009,
            2010,
            2011,
            2012,
            2013,
            2014,
            2015,
            2016,
            2017,
            2018,
            2019,
            2020,
            2021,
            2022,
            2023,
            2024,
            2025,
            2026,
            2027,
            2028,
            2029,
            2030,
            2031,
            2032,
            2033,
            2034,
            2035,
        ],
        [
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            120,
            150,
            200,
            220,
            250,
            270,
            300,
            320,
            350,
            370,
        ],
    )


@component.add(
    name="GAS_price_jump_look_up_0",
    comp_type="Auxiliary",
    comp_subtype="with Lookup",
    depends_on={"time": 1},
)
def gas_price_jump_look_up_0():
    """
    GAs look up table for testing the loop between economy and materials.
    """
    return np.interp(
        time(),
        [
            2005,
            2006,
            2007,
            2008,
            2009,
            2010,
            2011,
            2012,
            2013,
            2014,
            2015,
            2016,
            2017,
            2018,
            2019,
            2020,
            2021,
            2022,
            2023,
            2024,
            2025,
            2026,
            2027,
            2028,
            2029,
            2030,
            2031,
            2032,
            2033,
            2034,
            2035,
        ],
        [
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
        ],
    )


@component.add(
    name="gas_prospecting",
    units="EJ/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"gas_resources": 1, "gas_search_rate": 1},
)
def gas_prospecting():
    """
    Gas prospecting is the reclassification of resources that get moved to the reserves. The become econocimally viable, accesible to extract.
    """
    return gas_resources() * gas_search_rate()


@component.add(
    name="gas_reserves",
    units="EJ",
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_gas_reserves": 1},
    other_deps={
        "_integ_gas_reserves": {
            "initial": {"initial_gas_reserves": 1},
            "step": {"gas_prospecting": 1, "extraction_of_gas": 1},
        }
    },
)
def gas_reserves():
    """
    Gas reserves according to the following: Source: Bundesanstalt für Geowissenschaften und Rohstoffe (BGR), 2017. Energy Study: Data and Developments Concerning German and Global Energy Supplies Wang, J., & Bentley, Y. (2020). Modelling world natural gas production. Energy Reports, 6, 1363–1372. https://doi.org/10.1016/j.egyr.2020.05.018
    """
    return _integ_gas_reserves()


_integ_gas_reserves = Integ(
    lambda: gas_prospecting() - extraction_of_gas(),
    lambda: initial_gas_reserves(),
    "_integ_gas_reserves",
)


@component.add(
    name="GAS_RESOURCE_ESTIMATION_HIGH_SP",
    units="EJ",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_gas_resource_estimation_high_sp"},
)
def gas_resource_estimation_high_sp():
    """
    High gas resources estimation
    """
    return _ext_constant_gas_resource_estimation_high_sp()


_ext_constant_gas_resource_estimation_high_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "materials",
    "GAS_RESOURCE_ESTIMATION_HIGH_SP",
    {},
    _root,
    {},
    "_ext_constant_gas_resource_estimation_high_sp",
)


@component.add(
    name="GAS_RESOURCE_ESTIMATION_LOW_SP",
    units="EJ",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_gas_resource_estimation_low_sp"},
)
def gas_resource_estimation_low_sp():
    """
    Low gas resources estimation
    """
    return _ext_constant_gas_resource_estimation_low_sp()


_ext_constant_gas_resource_estimation_low_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "materials",
    "GAS_RESOURCE_ESTIMATION_LOW_SP",
    {},
    _root,
    {},
    "_ext_constant_gas_resource_estimation_low_sp",
)


@component.add(
    name="GAS_RESOURCE_ESTIMATION_MED_SP",
    units="EJ",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_gas_resource_estimation_med_sp"},
)
def gas_resource_estimation_med_sp():
    """
    Medium gas resources estimation
    """
    return _ext_constant_gas_resource_estimation_med_sp()


_ext_constant_gas_resource_estimation_med_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "materials",
    "GAS_RESOURCE_ESTIMATION_MED_SP",
    {},
    _root,
    {},
    "_ext_constant_gas_resource_estimation_med_sp",
)


@component.add(
    name="GAS_RESOURCE_ESTIMATION_USER_DEFINED_SP",
    units="EJ",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_gas_resource_estimation_user_defined_sp"
    },
)
def gas_resource_estimation_user_defined_sp():
    """
    User defined gas resources estimation
    """
    return _ext_constant_gas_resource_estimation_user_defined_sp()


_ext_constant_gas_resource_estimation_user_defined_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "materials",
    "GAS_User_defines",
    {},
    _root,
    {},
    "_ext_constant_gas_resource_estimation_user_defined_sp",
)


@component.add(
    name="gas_resources",
    units="EJ",
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_gas_resources": 1},
    other_deps={
        "_integ_gas_resources": {
            "initial": {"initial_gas_resource": 1},
            "step": {"gas_prospecting": 1},
        }
    },
)
def gas_resources():
    """
    Remaining gas resources. According to estimates based on - SOURCE: Source: Bundesanstalt für Geowissenschaften und Rohstoffe (BGR), 2017. Energy Study: Data and Developments Concerning German and Global Energy Supplies Wang, J., & Bentley, Y. (2020). Modelling world natural gas production. Energy Reports, 6, 1363–1372. https://doi.org/10.1016/j.egyr.2020.05.018, conventional and unconventional oil resources are available for discovery.Recalculated into bbl. Source: Meta-analysis of non-renewable energy resource estimates Author:MichaelDale https://doi.org/10.1016/j.enpol.2011.12.039 Projection of world fossil fuels by country Author: S.H.Mohr https://doi.org/10.1016/j.fuel.2014.10.030 There should be a separation between conventional and unconventional Gas in a later approach.
    """
    return _integ_gas_resources()


_integ_gas_resources = Integ(
    lambda: -gas_prospecting(), lambda: initial_gas_resource(), "_integ_gas_resources"
)


@component.add(
    name="GAS_SEARCH_RATE",
    units="1/Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_gas_search_rate"},
)
def gas_search_rate():
    """
    This is the rate of prospecting. Authors assumptions based on the WOLRD 7 model and calibration to historical data.
    """
    return _ext_constant_gas_search_rate()


_ext_constant_gas_search_rate = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Hydrocarbons",
    "GAS_SEARCH_RATE",
    {},
    _root,
    {},
    "_ext_constant_gas_search_rate",
)


@component.add(
    name="HARD_COAL_RESOURCE_ESTIMATION_HIGH_SP",
    units="EJ",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_hard_coal_resource_estimation_high_sp"},
)
def hard_coal_resource_estimation_high_sp():
    return _ext_constant_hard_coal_resource_estimation_high_sp()


_ext_constant_hard_coal_resource_estimation_high_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "materials",
    "HARD_COAL_RESOURCE_ESTIMATION_HIGH_SP",
    {},
    _root,
    {},
    "_ext_constant_hard_coal_resource_estimation_high_sp",
)


@component.add(
    name="HARD_COAL_RESOURCE_ESTIMATION_LOW_SP",
    units="EJ",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_hard_coal_resource_estimation_low_sp"},
)
def hard_coal_resource_estimation_low_sp():
    return _ext_constant_hard_coal_resource_estimation_low_sp()


_ext_constant_hard_coal_resource_estimation_low_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "materials",
    "HARD_COAL_RESOURCE_ESTIMATION_LOW_SP",
    {},
    _root,
    {},
    "_ext_constant_hard_coal_resource_estimation_low_sp",
)


@component.add(
    name="HARD_COAL_RESOURCE_ESTIMATION_MED_SP",
    units="EJ",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_hard_coal_resource_estimation_med_sp"},
)
def hard_coal_resource_estimation_med_sp():
    return _ext_constant_hard_coal_resource_estimation_med_sp()


_ext_constant_hard_coal_resource_estimation_med_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "materials",
    "HARD_COAL_RESOURCE_ESTIMATION_MED_SP",
    {},
    _root,
    {},
    "_ext_constant_hard_coal_resource_estimation_med_sp",
)


@component.add(
    name="HISTORICAL_COAL_DEMAND_TWO",
    units="EJ/Year",
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_historical_coal_demand_two",
        "__data__": "_ext_data_historical_coal_demand_two",
        "time": 1,
    },
)
def historical_coal_demand_two():
    """
    Historical demand for coal based on Source: Source: IEA. All Rights Reserved This data is subject to the IEA's terms and conditions: https://www.iea.org/t_c/termsandconditions/Units: in EJ/year
    """
    return _ext_data_historical_coal_demand_two(time())


_ext_data_historical_coal_demand_two = ExtData(
    "model_parameters/materials/materials.xlsx",
    "Hydrocarbons",
    "TIME_SERIES_HYDRO",
    "HISTORICAL_COAL_DEMAND_TWO",
    "interpolate",
    {},
    _root,
    {},
    "_ext_data_historical_coal_demand_two",
)


@component.add(
    name="HISTORICAL_CONSUMPTION_COAL_PER_YEAR",
    comp_type="Auxiliary",
    comp_subtype="with Lookup",
    depends_on={"time": 1},
)
def historical_consumption_coal_per_year():
    """
    Historical demand of coal based on the SOURCE: acessed 10.09.2022 - https://www.iea.org/data-and-statistics/charts/world-coal-consumption-1978- 2020
    """
    return np.interp(
        time(),
        [
            1978.0,
            1979.0,
            1980.0,
            1981.0,
            1982.0,
            1983.0,
            1984.0,
            1985.0,
            1986.0,
            1987.0,
            1988.0,
            1989.0,
            1990.0,
            1991.0,
            1992.0,
            1993.0,
            1994.0,
            1995.0,
            1996.0,
            1997.0,
            1998.0,
            1999.0,
            2000.0,
            2001.0,
            2002.0,
            2003.0,
            2004.0,
            2005.0,
            2006.0,
            2007.0,
            2008.0,
            2009.0,
            2010.0,
            2011.0,
            2012.0,
            2013.0,
            2014.0,
            2015.0,
            2016.0,
            2017.0,
            2018.0,
            2019.0,
            2020.0,
        ],
        [
            70.16,
            72.943,
            74.404,
            74.878,
            76.341,
            77.703,
            80.627,
            83.539,
            84.439,
            87.689,
            90.282,
            90.161,
            92.199,
            89.963,
            88.314,
            88.763,
            89.547,
            92.151,
            93.508,
            92.774,
            92.582,
            92.923,
            96.53,
            98.145,
            101.426,
            109.347,
            117.982,
            125.039,
            132.524,
            139.679,
            141.269,
            141.096,
            152.534,
            160.072,
            160.852,
            163.643,
            165.207,
            160.657,
            155.437,
            158.116,
            162.228,
            162.209,
            157.164,
        ],
    )


@component.add(
    name="HISTORICAL_GAS_DEMAND",
    units="EJ/Year",
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_historical_gas_demand",
        "__data__": "_ext_data_historical_gas_demand",
        "time": 1,
    },
)
def historical_gas_demand():
    """
    Consumption data for global gas cosumption from 1970 until 2021 taken from BP statistic report 2022
    """
    return _ext_data_historical_gas_demand(time())


_ext_data_historical_gas_demand = ExtData(
    "model_parameters/materials/materials.xlsx",
    "Hydrocarbons",
    "TIME_SERIES_HYDRO",
    "HISTORICAL_GAS_DEMAND",
    None,
    {},
    _root,
    {},
    "_ext_data_historical_gas_demand",
)


@component.add(
    name="HISTORICAL_OIL_DEMAND",
    units="bbl/Year",
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_historical_oil_demand",
        "__data__": "_ext_data_historical_oil_demand",
        "time": 1,
    },
)
def historical_oil_demand():
    """
    Historical Oil demand in bbl per year Source: bp-stats-review-2021 calulated from daily to yearly
    """
    return _ext_data_historical_oil_demand(time())


_ext_data_historical_oil_demand = ExtData(
    "model_parameters/materials/materials.xlsx",
    "Hydrocarbons",
    "TIME_SERIES_HYDRO",
    "HISTORICAL_OIL_DEMAND",
    "interpolate",
    {},
    _root,
    {},
    "_ext_data_historical_oil_demand",
)


@component.add(
    name="HISTORICAL_TARGET_PRICE",
    units="$/bbl",
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_historical_target_price",
        "__data__": "_ext_data_historical_target_price",
        "time": 1,
    },
)
def historical_target_price():
    """
    Estimation made based on OPEC spare capacity and price development in market.Values derived by fitting the model results with the historical data. Different than Inaki's excel! NEEDS an UPDATE! Target Price derived from the excels Table we developed in Bilboa, based on the the attempt to fit the opec spare capacity and the oil price.
    """
    return _ext_data_historical_target_price(time())


_ext_data_historical_target_price = ExtData(
    "model_parameters/materials/materials.xlsx",
    "Hydrocarbons",
    "TIME_SERIES_HYDRO",
    "HISTORICAL_TARGET_PRICE",
    None,
    {},
    _root,
    {},
    "_ext_data_historical_target_price",
)


@component.add(
    name="increase_in_depletion_after_peak_coal",
    units="1/Year",
    subscripts=["COAL_TYPES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"urr_coal_int": 4, "cumulative_coal_extracted": 4},
)
def increase_in_depletion_after_peak_coal():
    """
    Switch in mining depletion, increase when total cummulative Is larger than the URR-> the depletion of mines will be higher.
    """
    value = xr.DataArray(
        np.nan, {"COAL_TYPES_I": _subscript_dict["COAL_TYPES_I"]}, ["COAL_TYPES_I"]
    )
    value.loc[["HARD_COAL"]] = if_then_else(
        float(urr_coal_int().loc["HARD_COAL"]) / 2
        <= float(cumulative_coal_extracted().loc["HARD_COAL"]),
        lambda: (
            float(cumulative_coal_extracted().loc["HARD_COAL"])
            / float(urr_coal_int().loc["HARD_COAL"])
        )
        / 3,
        lambda: 0.03,
    )
    value.loc[["BROWN_COAL"]] = if_then_else(
        float(urr_coal_int().loc["BROWN_COAL"]) / 2
        <= float(cumulative_coal_extracted().loc["BROWN_COAL"]),
        lambda: (
            float(cumulative_coal_extracted().loc["BROWN_COAL"])
            / float(urr_coal_int().loc["BROWN_COAL"])
        )
        / 3,
        lambda: 0.03,
    )
    return value


@component.add(
    name="increase_in_depletion_gas",
    units="1/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"urr_natural_gas": 2, "cumulative_extracted_gas": 2},
)
def increase_in_depletion_gas():
    """
    Assumption made by the authors that wells are depletiing faster when the half of URR is reached. Its a simplification because in the real world the productivity per well would decrease if the well production peak is reached.
    """
    return if_then_else(
        urr_natural_gas() / 2 <= cumulative_extracted_gas(),
        lambda: (cumulative_extracted_gas() / urr_natural_gas()) / 9.5,
        lambda: 0.032,
    )


@component.add(
    name="INITIAL_COAL_CUMULATIVELY_EXTRACTED_2005",
    units="EJ",
    subscripts=["COAL_TYPES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"initial_total_coal_extracted": 2, "share_of_coal_type": 2},
)
def initial_coal_cumulatively_extracted_2005():
    """
    The INITIAL value for the Coal that is already extracted until the Year 2004. which is known to exist in current explored deposits -Initial HARD and BROWN COAL resources in EJ according to the Source: Global Energy Assessment-Toward a Sustainable Future (Rogner et al., 2012) Calculated backwards with the data from: https://www.iea.org/data-and-statistics/charts/world-coal-consumption-1978- 2020 2656.88
    """
    value = xr.DataArray(
        np.nan, {"COAL_TYPES_I": _subscript_dict["COAL_TYPES_I"]}, ["COAL_TYPES_I"]
    )
    value.loc[["HARD_COAL"]] = initial_total_coal_extracted() * float(
        share_of_coal_type().loc["HARD_COAL"]
    )
    value.loc[["BROWN_COAL"]] = initial_total_coal_extracted() * float(
        share_of_coal_type().loc["BROWN_COAL"]
    )
    return value


@component.add(
    name="INITIAL_COAL_HIDDEN_2005",
    units="EJ",
    subscripts=["COAL_TYPES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"initial_coal_resources": 2, "potential_recovery_factor": 2},
)
def initial_coal_hidden_2005():
    """
    INITIAL value for the remaining Coal which still needs to be discovered- and recovery factor- Source: Global Energy Assessment-Toward a Sustainable Future (Rogner et al., 2012) Calculated backwards with the data from: https://www.iea.org/data-and-statistics/charts/world-coal-consumption-1978- 2020
    """
    value = xr.DataArray(
        np.nan, {"COAL_TYPES_I": _subscript_dict["COAL_TYPES_I"]}, ["COAL_TYPES_I"]
    )
    value.loc[["HARD_COAL"]] = (
        float(initial_coal_resources().loc["HARD_COAL"]) * potential_recovery_factor()
    )
    value.loc[["BROWN_COAL"]] = (
        float(initial_coal_resources().loc["BROWN_COAL"]) * potential_recovery_factor()
    )
    return value


@component.add(
    name="INITIAL_COAL_RESERVES",
    units="EJ",
    subscripts=["COAL_TYPES_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_coal_reserves"},
)
def initial_coal_reserves():
    """
    'Reserves’ refer to endowments estimated to be economically extractable at the time of determination. In WILIAM resources do not include reserves. Initial HARD and BROWN COAL reserves in EJ according to the Source: Global Energy Assessment-Toward a Sustainable Future (Rogner et al., 2012) HARD COAL 18246 BROWN COAL 2775
    """
    return _ext_constant_initial_coal_reserves()


_ext_constant_initial_coal_reserves = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "materials",
    "INITIAL_COAL_RESERVES_2005_SP",
    {"COAL_TYPES_I": _subscript_dict["COAL_TYPES_I"]},
    _root,
    {"COAL_TYPES_I": _subscript_dict["COAL_TYPES_I"]},
    "_ext_constant_initial_coal_reserves",
)


@component.add(
    name="INITIAL_COAL_RESOURCES",
    units="EJ",
    subscripts=["COAL_TYPES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_hard_coal_resource_estimation_sp": 3,
        "hard_coal_resource_estimation_low_sp": 1,
        "hard_coal_resource_estimation_high_sp": 1,
        "hard_coal_resource_estimation_med_sp": 1,
        "brown_coal_resource_estimation_med_sp": 1,
        "select_brown_coal_resource_estimation_sp": 3,
        "brown_coal_resource_estimation_low_sp": 1,
        "brown_coal_resource_estimation_high_sp": 1,
    },
)
def initial_coal_resources():
    """
    'Resources' refer to the amount of energy resources (proven or geologically possible), which cannot currently be exploited for technical and/or economic reasons but may be exploitable in the future. Depending on the definition it may include or not reserves, which refer to the fraction of the resource base estimated to be economically extractable at the time of determination. In WILIAM resources do not include reserves.
    """
    value = xr.DataArray(
        np.nan, {"COAL_TYPES_I": _subscript_dict["COAL_TYPES_I"]}, ["COAL_TYPES_I"]
    )
    value.loc[["HARD_COAL"]] = if_then_else(
        select_hard_coal_resource_estimation_sp() == 0,
        lambda: hard_coal_resource_estimation_low_sp(),
        lambda: if_then_else(
            select_hard_coal_resource_estimation_sp() == 1,
            lambda: hard_coal_resource_estimation_med_sp(),
            lambda: if_then_else(
                select_hard_coal_resource_estimation_sp() == 2,
                lambda: hard_coal_resource_estimation_high_sp(),
                lambda: 0,
            ),
        ),
    )
    value.loc[["BROWN_COAL"]] = if_then_else(
        select_brown_coal_resource_estimation_sp() == 0,
        lambda: float(brown_coal_resource_estimation_low_sp().loc["BROWN_COAL"]),
        lambda: if_then_else(
            select_brown_coal_resource_estimation_sp() == 1,
            lambda: float(brown_coal_resource_estimation_med_sp().loc["BROWN_COAL"]),
            lambda: if_then_else(
                select_brown_coal_resource_estimation_sp() == 2,
                lambda: float(
                    brown_coal_resource_estimation_high_sp().loc["BROWN_COAL"]
                ),
                lambda: 0,
            ),
        ),
    )
    return value


@component.add(
    name="INITIAL_EXTRACTION_CAPACITY",
    units="EJ",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_extraction_capacity"},
)
def initial_extraction_capacity():
    """
    99.28 EJ Natural Gas production in the year 2005- Source data is the BP report from the year 2022 report New 98,77 BP consumption 2005 * 1,07 assumption of the Authors of 7 % spare capacity = 103.43
    """
    return _ext_constant_initial_extraction_capacity()


_ext_constant_initial_extraction_capacity = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Hydrocarbons",
    "INITIAL_EXTRACTION_CAPACITY",
    {},
    _root,
    {},
    "_ext_constant_initial_extraction_capacity",
)


@component.add(
    name="INITIAL_GAS_RESERVES",
    units="EJ",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_gas_reserves"},
)
def initial_gas_reserves():
    """
    'Reserves’ refer to endowments estimated to be economically extractable at the time of determination. In WILIAM resources do not include reserves. New 7012 EJ of conventional gas and 261,91 EJ for unconventional gas total of 7273,96 EJ status of 2017 need to be back calibrated + 1404,623499 = 8678.58 Source: Bundesanstalt für Geowissenschaften und Rohstoffe (BGR), 2017. Energy Study: Data and Developments Concerning German and Global Energy Supplies Wang, J., & Bentley, Y. (2020). Modelling world natural gas production. Energy Reports, 6, 1363–1372. https://doi.org/10.1016/j.egyr.2020.05.018
    """
    return _ext_constant_initial_gas_reserves()


_ext_constant_initial_gas_reserves = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "materials",
    "INITIAL_GAS_RESERVES_2005_SP",
    {},
    _root,
    {},
    "_ext_constant_initial_gas_reserves",
)


@component.add(
    name="INITIAL_GAS_RESOURCE",
    units="bbl",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_gas_resource_estimation_sp": 3,
        "gas_resource_estimation_low_sp": 1,
        "gas_resource_estimation_med_sp": 1,
        "gas_resource_estimation_high_sp": 1,
        "gas_resource_estimation_user_defined_sp": 1,
    },
)
def initial_gas_resource():
    """
    'Resources refer to the amount of energy resources (proven or geologically possible), which cannot currently be exploited for technical and/or economic reasons but may be exploitable in the future. Depending on the definition it may include or not reserves, which refer to the fraction of the resource base estimated to be economically extractable at the time of determination. In WILIAM resources do not include reserves. The model user can modify the amount of gas resources that are remaining and are potentially recoverable. There is high uncertainty with regards to resource estimation. Due to this circumstances we allow the user to explore different scenarios with low, medium and high estimates found in the literature plus one additional option where the user can define.
    """
    return if_then_else(
        select_gas_resource_estimation_sp() == 0,
        lambda: gas_resource_estimation_low_sp(),
        lambda: if_then_else(
            select_gas_resource_estimation_sp() == 1,
            lambda: gas_resource_estimation_med_sp(),
            lambda: if_then_else(
                select_gas_resource_estimation_sp() == 2,
                lambda: gas_resource_estimation_high_sp(),
                lambda: gas_resource_estimation_user_defined_sp(),
            ),
        ),
    )


@component.add(
    name="INITIAL_NUMBER_OF_OPERATING_COAL_MINES_2008",
    units="mines",
    subscripts=["COAL_TYPES_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_initial_number_of_operating_coal_mines_2008"
    },
)
def initial_number_of_operating_coal_mines_2008():
    """
    Estimated amount of operating mines, by calibration to historical data. Calculation is based on the nummber of mines in the year 2022 and the amount of mined coal. Than calculated backwards to match the historical data. From the source: “Global Coal Mine Tracker, Global Energy Monitor, July 2022 release.” HARD COAL 1941.98 BROWN COAL 160
    """
    return _ext_constant_initial_number_of_operating_coal_mines_2008()


_ext_constant_initial_number_of_operating_coal_mines_2008 = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Hydrocarbons",
    "INITIAL_NUMBER_OF_OPERATING_COAL_MINES_2008*",
    {"COAL_TYPES_I": _subscript_dict["COAL_TYPES_I"]},
    _root,
    {"COAL_TYPES_I": _subscript_dict["COAL_TYPES_I"]},
    "_ext_constant_initial_number_of_operating_coal_mines_2008",
)


@component.add(
    name="INITIAL_NUMBER_OF_WELLS",
    units="wells",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_number_of_wells"},
)
def initial_number_of_wells():
    """
    Inital number of wells is based on the data of Rystad Energy Data at 2005: website accesd last on:28.07.2022 https://www.rystadenergy.com/energy-themes/supply-chain/wells/well-cube/ 1.56e+06
    """
    return _ext_constant_initial_number_of_wells()


_ext_constant_initial_number_of_wells = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Hydrocarbons",
    "INITIAL_NUMBER_OF_WELLS",
    {},
    _root,
    {},
    "_ext_constant_initial_number_of_wells",
)


@component.add(
    name="INITIAL_OIL_CUMULATIVELY_EXTRACTED_2005",
    units="bbl",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_initial_oil_cumulatively_extracted_2005"
    },
)
def initial_oil_cumulatively_extracted_2005():
    """
    The INITIAL value for the Oil that is already extracted until the Year 2005. which is known to exist in current explored deposits - Source:
    """
    return _ext_constant_initial_oil_cumulatively_extracted_2005()


_ext_constant_initial_oil_cumulatively_extracted_2005 = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Hydrocarbons",
    "INITIAL_OIL_CUMULATIVELY_EXTRACTED_2005",
    {},
    _root,
    {},
    "_ext_constant_initial_oil_cumulatively_extracted_2005",
)


@component.add(
    name="INITIAL_OIL_PRODUCTION_PER_YEAR",
    units="bbl/Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_oil_production_per_year"},
)
def initial_oil_production_per_year():
    """
    oil per well new max cap first year 5,71 Bt*Oe/ per year/1,821 million wells (2020) values got recalculated to bbl 4,1 Bt*Oe(2005)/ 1,56 million wells values got recalculated to bbl An assumption made by the authors to simplify the complex issues of Wells with different productivity. The authors assume that each well has the same productivity- from a global perspective. In reality, there is a small amount of highly productive wells and a large amount of less productive wells. Sources: bbl: 2.9892e+10
    """
    return _ext_constant_initial_oil_production_per_year()


_ext_constant_initial_oil_production_per_year = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Hydrocarbons",
    "INITIAL_OIL_PRODUCTION_PER_YEAR",
    {},
    _root,
    {},
    "_ext_constant_initial_oil_production_per_year",
)


@component.add(
    name="INITIAL_OIL_RESERVES_2005",
    units="bbl",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_oil_reserves_2005"},
)
def initial_oil_reserves_2005():
    """
    'Reserves’ refer to endowments estimated to be economically extractable at the time of determination. In WILIAM resources do not include reserves. BGR Energy Study 2020.-> 1.79429E+12 bbl recalculated to 2005 = 2.26998E+12 bbl
    """
    return _ext_constant_initial_oil_reserves_2005()


_ext_constant_initial_oil_reserves_2005 = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "materials",
    "INITIAL_OIL_RESERVES_2005_SP",
    {},
    _root,
    {},
    "_ext_constant_initial_oil_reserves_2005",
)


@component.add(
    name="INITIAL_OIL_RESOURCES",
    units="bbl",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_model_explorer": 1,
        "model_explorer_oil_resource": 1,
        "oil_resource_estimation_user_defined_sp": 1,
        "oil_resource_estimation_low_sp": 1,
        "oil_resource_estimation_med_sp": 1,
        "select_oil_resource_estimation_sp": 3,
        "oil_resource_estimation_high_sp": 1,
    },
)
def initial_oil_resources():
    """
    'Resources refer to the amount of energy resources (proven or geologically possible), which cannot currently be exploited for technical and/or economic reasons but may be exploitable in the future. Depending on the definition it may include or not reserves, which refer to the fraction of the resource base estimated to be economically extractable at the time of determination. In WILIAM resources do not include reserves. The model user can modify the amount of crude oil resources that are remaining and are potentially recoverable. Unconventional oil and conventional oil are added up. There is high uncertainty with regards to resource estimation. Due to this circumstances we allow the user to explore different scenarios with low, medium and high estimates found in the literature plus one additional option where the user can define.
    """
    return if_then_else(
        switch_model_explorer() == 1,
        lambda: model_explorer_oil_resource(),
        lambda: if_then_else(
            select_oil_resource_estimation_sp() == 0,
            lambda: oil_resource_estimation_low_sp(),
            lambda: if_then_else(
                select_oil_resource_estimation_sp() == 1,
                lambda: oil_resource_estimation_med_sp(),
                lambda: if_then_else(
                    select_oil_resource_estimation_sp() == 2,
                    lambda: oil_resource_estimation_high_sp(),
                    lambda: oil_resource_estimation_user_defined_sp(),
                ),
            ),
        ),
    )


@component.add(
    name="INITIAL_SPARE_CAPACITY",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_spare_capacity"},
)
def initial_spare_capacity():
    """
    The model was calibrated without the consideration of an Initial spare capacity, the authors of the model assume an Initial spare capacity of 0.003.
    """
    return _ext_constant_initial_spare_capacity()


_ext_constant_initial_spare_capacity = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Hydrocarbons",
    "INITIAL_SPARE_CAPACITY",
    {},
    _root,
    {},
    "_ext_constant_initial_spare_capacity",
)


@component.add(
    name="INITIAL_TOTAL_COAL_EXTRACTED",
    units="EJ",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_total_coal_extracted"},
)
def initial_total_coal_extracted():
    """
    Cummulative amount of extracted Coal until 2005 based on the Source: Global Energy Assessment-Toward a Sustainable Future (Rogner et al., 2012) calculated backwards with extraction data from BP Stat. review. 2022 report. INITIAL TOTAL COAL EXTRACTED = 2656.88 EJ
    """
    return _ext_constant_initial_total_coal_extracted()


_ext_constant_initial_total_coal_extracted = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Hydrocarbons",
    "INITIAL_TOTAL_COAL_EXTRACTED",
    {},
    _root,
    {},
    "_ext_constant_initial_total_coal_extracted",
)


@component.add(
    name="INITIAL_TOTAL_GAS_EXTRACTED",
    units="EJ",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_total_gas_extracted"},
)
def initial_total_gas_extracted():
    """
    (BGR 2017) Bundesanstalt für Geowissenschaften und Rohstoffe (BGR), 2017. Energy Study: Data and Developments Concerning German and Global Energy Supplies Cumulative Production of 116,9 (Tcm) * 28,317 conversion factor of Tcm to EJ = 3310,2573 for the year 2017 New value = 4325 it is for 2017 has to back calibrated When back calculated to 2005 cumulative production is 2920,38 EJ
    """
    return _ext_constant_initial_total_gas_extracted()


_ext_constant_initial_total_gas_extracted = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Hydrocarbons",
    "INITIAL_TOTAL_GAS_EXTRACTED",
    {},
    _root,
    {},
    "_ext_constant_initial_total_gas_extracted",
)


@component.add(
    name="INITIAL_YEAR_TAX_RATE_ON_EXTRACTION_OF_RESOURCES_SP",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_initial_year_tax_rate_on_extraction_of_resources_sp"
    },
)
def initial_year_tax_rate_on_extraction_of_resources_sp():
    """
    Start year for the policy of the resource Tax on extraction. Can be modified by the user in the scenario_parameter excel sheet. Standart setting is set to 2025. So the policy is switched off. INITIAL_YEAR_TAX_RATE_ON_EXTRACTION_OF_RESOURCES_LOW = 2025 INITIAL_YEAR_TAX_RATE_ON_EXTRACTION_OF_RESOURCES_MEDIUM = 2025 INITIAL_YEAR_TAX_RATE_ON_EXTRACTION_OF_RESOURCES_HIGH = 2025 INITIAL_YEAR_TAX_RATE_ON_EXTRACTION_OF_RESOURCES_OTHER = 2025
    """
    return _ext_constant_initial_year_tax_rate_on_extraction_of_resources_sp()


_ext_constant_initial_year_tax_rate_on_extraction_of_resources_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "materials",
    "INITIAL_YEAR_TAX_RATE_ON_EXTRACTION_OF_RESOURCES_MEDIUM",
    {},
    _root,
    {},
    "_ext_constant_initial_year_tax_rate_on_extraction_of_resources_sp",
)


@component.add(
    name="investment_in_coal_mines",
    units="mines/Year",
    subscripts=["COAL_TYPES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "reserves_in_operating_coal_mines": 2,
        "coal_reserves": 2,
        "seperation_of_mining_types": 2,
    },
)
def investment_in_coal_mines():
    """
    Investment into coal mines separated in HARD and BROWN coal. The invements in mines will only take place if the coal reserves are still larger than the coal reserves already accessed by the mines. There will no mines be opened when the available coal reserves are to small independent of the current price of coal.
    """
    value = xr.DataArray(
        np.nan, {"COAL_TYPES_I": _subscript_dict["COAL_TYPES_I"]}, ["COAL_TYPES_I"]
    )
    value.loc[["HARD_COAL"]] = if_then_else(
        float(reserves_in_operating_coal_mines().loc["HARD_COAL"])
        < float(coal_reserves().loc["HARD_COAL"]),
        lambda: float(seperation_of_mining_types().loc["HARD_COAL"]),
        lambda: 0,
    )
    value.loc[["BROWN_COAL"]] = if_then_else(
        float(reserves_in_operating_coal_mines().loc["BROWN_COAL"])
        < float(coal_reserves().loc["BROWN_COAL"]),
        lambda: float(seperation_of_mining_types().loc["BROWN_COAL"]),
        lambda: 0,
    )
    return value


@component.add(
    name="investment_in_Gas_extraction_capacity",
    units="EJ/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "desired_desired_gas_extraction_capacity": 2,
        "max_invest_in_gas_extraction_capacity": 2,
    },
)
def investment_in_gas_extraction_capacity():
    """
    Investment in gas extraction capacity. In cases where the price is demanding for a capacity increase the capacity increase will be build. In the case the desired gas extraction capacity is higher than the maximium capacity increase per year , the maximum capacity increase gets build.
    """
    return if_then_else(
        desired_desired_gas_extraction_capacity()
        > max_invest_in_gas_extraction_capacity(),
        lambda: max_invest_in_gas_extraction_capacity(),
        lambda: np.maximum(desired_desired_gas_extraction_capacity(), 0),
    )


@component.add(
    name="investment_in_oil_wells",
    units="wells/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"desired_oil_wells": 2, "max_invest_in_oil_wells": 2},
)
def investment_in_oil_wells():
    """
    New oil wells entering into operation each year.
    """
    return if_then_else(
        desired_oil_wells() > max_invest_in_oil_wells(),
        lambda: max_invest_in_oil_wells(),
        lambda: np.maximum(desired_oil_wells(), 0),
    )


@component.add(
    name="Laherrere_2018_estimate_per_year",
    units="bbl/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"oil_laherrere_2018_modified": 1, "unit_conversion_days_year": 1},
)
def laherrere_2018_estimate_per_year():
    return oil_laherrere_2018_modified() * unit_conversion_days_year() * 10**6


@component.add(
    name="Laherrere_CURVE_2018_total_oil",
    units="Mbbl/Year",
    comp_type="Auxiliary",
    comp_subtype="with Lookup",
    depends_on={"time": 1},
)
def laherrere_curve_2018_total_oil():
    """
    Laherrrere total Oil prediction 2018
    """
    return np.interp(
        time(),
        [
            1900.0,
            1901.0,
            1902.0,
            1903.0,
            1904.0,
            1905.0,
            1906.0,
            1907.0,
            1908.0,
            1909.0,
            1910.0,
            1911.0,
            1912.0,
            1913.0,
            1914.0,
            1915.0,
            1916.0,
            1917.0,
            1918.0,
            1919.0,
            1920.0,
            1921.0,
            1922.0,
            1923.0,
            1924.0,
            1925.0,
            1926.0,
            1927.0,
            1928.0,
            1929.0,
            1930.0,
            1931.0,
            1932.0,
            1933.0,
            1934.0,
            1935.0,
            1936.0,
            1937.0,
            1938.0,
            1939.0,
            1940.0,
            1941.0,
            1942.0,
            1943.0,
            1944.0,
            1945.0,
            1946.0,
            1947.0,
            1948.0,
            1949.0,
            1950.0,
            1951.0,
            1952.0,
            1953.0,
            1954.0,
            1955.0,
            1956.0,
            1957.0,
            1958.0,
            1959.0,
            1960.0,
            1961.0,
            1962.0,
            1963.0,
            1964.0,
            1965.0,
            1966.0,
            1967.0,
            1968.0,
            1969.0,
            1970.0,
            1971.0,
            1972.0,
            1973.0,
            1974.0,
            1975.0,
            1976.0,
            1977.0,
            1978.0,
            1979.0,
            1980.0,
            1981.0,
            1982.0,
            1983.0,
            1984.0,
            1985.0,
            1986.0,
            1987.0,
            1988.0,
            1989.0,
            1990.0,
            1991.0,
            1992.0,
            1993.0,
            1994.0,
            1995.0,
            1996.0,
            1997.0,
            1998.0,
            1999.0,
            2000.0,
            2001.0,
            2002.0,
            2003.0,
            2004.0,
            2005.0,
            2006.0,
            2007.0,
            2008.0,
            2009.0,
            2010.0,
            2011.0,
            2012.0,
            2013.0,
            2014.0,
            2015.0,
            2016.0,
            2017.0,
            2018.0,
            2019.0,
            2020.0,
            2021.0,
            2022.0,
            2023.0,
            2024.0,
            2025.0,
            2026.0,
            2027.0,
            2028.0,
            2029.0,
            2030.0,
            2031.0,
            2032.0,
            2033.0,
            2034.0,
            2035.0,
            2036.0,
            2037.0,
            2038.0,
            2039.0,
            2040.0,
            2041.0,
            2042.0,
            2043.0,
            2044.0,
            2045.0,
            2046.0,
            2047.0,
            2048.0,
            2049.0,
            2050.0,
            2051.0,
            2052.0,
            2053.0,
            2054.0,
            2055.0,
            2056.0,
            2057.0,
            2058.0,
            2059.0,
            2060.0,
            2065.0,
            2070.0,
            2075.0,
            2080.0,
            2085.0,
            2090.0,
            2095.0,
            2100.0,
            2110.0,
            2120.0,
            2130.0,
            2140.0,
            2150.0,
            2160.0,
            2170.0,
            2180.0,
            2190.0,
            2200.0,
            2210.0,
            2220.0,
            2230.0,
            2240.0,
            2250.0,
            2260.0,
            2270.0,
            2280.0,
            2290.0,
            2300.0,
        ],
        [
            4.58630e-01,
            4.98082e-01,
            5.33973e-01,
            5.97260e-01,
            5.89315e-01,
            5.84384e-01,
            7.23836e-01,
            7.82466e-01,
            8.18356e-01,
            8.98082e-01,
            9.43562e-01,
            9.65479e-01,
            1.05562e00,
            1.11644e00,
            1.18356e00,
            1.25342e00,
            1.37781e00,
            1.37945e00,
            1.52301e00,
            1.88740e00,
            2.09863e00,
            2.35315e00,
            2.78274e00,
            2.77890e00,
            2.92575e00,
            3.00493e00,
            3.46027e00,
            3.63014e00,
            4.07123e00,
            3.86301e00,
            3.76164e00,
            3.58904e00,
            3.95069e00,
            4.16986e00,
            4.53151e00,
            4.90959e00,
            5.58630e00,
            5.44658e00,
            5.71507e00,
            5.89041e00,
            6.08493e00,
            5.73425e00,
            6.18356e00,
            7.10411e00,
            7.10959e00,
            7.52055e00,
            8.27945e00,
            9.40548e00,
            9.32603e00,
            1.04192e01,
            1.17342e01,
            1.23808e01,
            1.31452e01,
            1.37479e01,
            1.54137e01,
            1.67808e01,
            1.76411e01,
            1.81041e01,
            1.95452e01,
            2.09900e01,
            2.24500e01,
            2.43500e01,
            2.61300e01,
            2.81800e01,
            3.03300e01,
            3.29600e01,
            3.53920e01,
            3.80173e01,
            4.17441e01,
            4.59148e01,
            4.85515e01,
            5.11805e01,
            5.85173e01,
            5.85573e01,
            5.56660e01,
            6.02576e01,
            6.27470e01,
            6.32919e01,
            6.60250e01,
            6.31050e01,
            5.98193e01,
            5.72086e01,
            5.70237e01,
            5.85522e01,
            5.80795e01,
            6.07417e01,
            6.12429e01,
            6.35206e01,
            6.46770e01,
            6.54993e01,
            6.53297e01,
            6.53544e01,
            6.56566e01,
            6.69907e01,
            6.84883e01,
            7.00562e01,
            7.22407e01,
            7.37345e01,
            7.28863e01,
            7.55231e01,
            7.55868e01,
            7.49908e01,
            7.76156e01,
            8.13569e01,
            8.33354e01,
            8.32224e01,
            8.32323e01,
            8.43869e01,
            8.37993e01,
            8.60108e01,
            8.65260e01,
            8.85181e01,
            8.88690e01,
            9.08142e01,
            9.08869e01,
            9.14937e01,
            9.20961e01,
            9.25056e01,
            9.28150e01,
            9.30250e01,
            9.31368e01,
            9.31520e01,
            9.30729e01,
            9.29025e01,
            9.26440e01,
            9.23012e01,
            9.18782e01,
            9.13796e01,
            9.08101e01,
            9.01747e01,
            8.94788e01,
            8.87275e01,
            8.79261e01,
            8.70801e01,
            8.61945e01,
            8.52744e01,
            8.43247e01,
            8.33498e01,
            8.23540e01,
            8.13413e01,
            8.03150e01,
            7.92784e01,
            7.82340e01,
            7.71842e01,
            7.61307e01,
            7.50750e01,
            7.40181e01,
            7.29607e01,
            7.19030e01,
            7.08453e01,
            6.97872e01,
            6.87284e01,
            6.76684e01,
            6.66066e01,
            6.55424e01,
            6.44752e01,
            6.34044e01,
            6.23297e01,
            6.12506e01,
            6.01671e01,
            5.90792e01,
            5.35890e01,
            4.81032e01,
            4.27978e01,
            3.78490e01,
            3.33728e01,
            2.94044e01,
            2.59144e01,
            2.28379e01,
            1.76460e01,
            1.34056e01,
            9.93386e00,
            7.16904e00,
            5.05322e00,
            3.49529e00,
            2.38390e00,
            1.60973e00,
            1.07957e00,
            7.20747e-01,
            4.79787e-01,
            3.18806e-01,
            2.11611e-01,
            1.40376e-01,
            9.30948e-02,
            6.17328e-02,
            4.09371e-02,
            2.71491e-02,
            1.80073e-02,
            1.19453e-02,
        ],
    )


@component.add(
    name="Laherrere_TEST",
    units="bbl/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"laherrere_curve_2018_total_oil": 1, "unit_conversion_days_year": 1},
)
def laherrere_test():
    return laherrere_curve_2018_total_oil() * unit_conversion_days_year() * 10**6


@component.add(
    name="LN_of_the_coal_spare_cap",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"coal_gap_between_total_available_and_demand": 1},
)
def ln_of_the_coal_spare_cap():
    """
    LN of the coal spare cap. Intermediate step for the Coal price calculation. Calculation is based on a LN function which describes the relation between Coal demand per year and Coal available without the spare capacity. "Coal ln (1-Q/Q available)"
    """
    return np.log(1 / coal_gap_between_total_available_and_demand())


@component.add(
    name="max_invest_in_Gas_extraction_capacity",
    units="EJ/Year",
    comp_type="Stateful",
    comp_subtype="Delay",
    depends_on={
        "_delay_max_invest_in_gas_extraction_capacity": 1,
        "gas_investment_cap": 1,
    },
    other_deps={
        "_delay_max_invest_in_gas_extraction_capacity": {
            "initial": {"extraction_capacity_of_gas": 1},
            "step": {"extraction_capacity_of_gas": 1},
        }
    },
)
def max_invest_in_gas_extraction_capacity():
    """
    Function that limits the investment in Gas extraction capacity. Limits the possibility to growth in an unrealisting propartion when the price is increasing.
    """
    return _delay_max_invest_in_gas_extraction_capacity() * gas_investment_cap()


_delay_max_invest_in_gas_extraction_capacity = Delay(
    lambda: extraction_capacity_of_gas(),
    lambda: 1,
    lambda: extraction_capacity_of_gas(),
    lambda: 1,
    time_step,
    "_delay_max_invest_in_gas_extraction_capacity",
)


@component.add(
    name="max_invest_in_Oil_wells",
    units="wells/Year",
    comp_type="Stateful",
    comp_subtype="Delay",
    depends_on={"_delay_max_invest_in_oil_wells": 1, "oil_well_investment_cap": 1},
    other_deps={
        "_delay_max_invest_in_oil_wells": {
            "initial": {"number_of_oil_wells": 1},
            "step": {"number_of_oil_wells": 1},
        }
    },
)
def max_invest_in_oil_wells():
    """
    Function that limits the investment in Oil wells. Limits the possibility to growth in an unrealisting propartion when the price is increasing. Function included to represent the limits in capacity expension from one year to the next.
    """
    return _delay_max_invest_in_oil_wells() * oil_well_investment_cap()


_delay_max_invest_in_oil_wells = Delay(
    lambda: number_of_oil_wells(),
    lambda: 1,
    lambda: number_of_oil_wells(),
    lambda: 1,
    time_step,
    "_delay_max_invest_in_oil_wells",
)


@component.add(
    name="max_investment_in_Coal_mines",
    units="mines/Year",
    comp_type="Stateful",
    comp_subtype="Delay",
    depends_on={
        "_delay_max_investment_in_coal_mines": 1,
        "coal_mines_investment_cap": 1,
    },
    other_deps={
        "_delay_max_investment_in_coal_mines": {
            "initial": {"number_of_operating_coal_mines": 2},
            "step": {"number_of_operating_coal_mines": 2},
        }
    },
)
def max_investment_in_coal_mines():
    """
    Function that determines the maximum of mines put into operation based the the excisting operating coal mines of the previous year and the maximium increase in mines.
    """
    return _delay_max_investment_in_coal_mines() * coal_mines_investment_cap()


_delay_max_investment_in_coal_mines = Delay(
    lambda: float(number_of_operating_coal_mines().loc["HARD_COAL"])
    + float(number_of_operating_coal_mines().loc["BROWN_COAL"]),
    lambda: 1,
    lambda: float(number_of_operating_coal_mines().loc["HARD_COAL"])
    + float(number_of_operating_coal_mines().loc["BROWN_COAL"]),
    lambda: 1,
    time_step,
    "_delay_max_investment_in_coal_mines",
)


@component.add(
    name="MAX_OIL_PRICE_FOR_LIMIT",
    units="$/bbl",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_max_oil_price_for_limit"},
)
def max_oil_price_for_limit():
    """
    Maximum of the Oil price, before the oil price growth limit is kicking in.
    """
    return _ext_constant_max_oil_price_for_limit()


_ext_constant_max_oil_price_for_limit = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Hydrocarbons",
    "MAX_OIL_PRICE_FOR_LIMIT",
    {},
    _root,
    {},
    "_ext_constant_max_oil_price_for_limit",
)


@component.add(
    name="MINIMUM_GAS_PRICE_FOR_INVESTMENT",
    units="$/million_Btu",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_minimum_gas_price_for_investment"},
)
def minimum_gas_price_for_investment():
    """
    ssumption made by the Authors of this model. The underlying idea of this assumption is that even when there is a high demand and price increase for Gas, there is a limitation to which extant the demand and price translates into infrastructure investment due to capacity limitations. No investment in gas infrastructe under a gas price of 3.5 $/ million Btu Based on the work for the Oil model: Source the Authors based their assumption on: Used a liniar function that describes the relation of the oil price to wells drilled in that year. Based on Historical Oil prices and drilling activities. adapted to fit the gas model. The Aussumption is that minimal price of gas is nessesary to invest into gas extraction capacity. If the price is above the minimum price than investment is done in gas extraction capacity. The higher the price the higher the investment in extraction capacity, what follow is a higher extraction capacity. https://www.rystadenergy.com/newsevents/news/newsletters/OfsArchive/ofs-november-2018 / https://www.drillingcontractor.org/670000-wells-to-be-drilled-through-2020-28709 https://www.rystadenergy.com/energy-themes/supply-chain/wells/well-cube/ https://www.eia.gov/dnav/pet/hist/LeafHandler.ashx?n=pet&s=rwtc&f=a
    """
    return _ext_constant_minimum_gas_price_for_investment()


_ext_constant_minimum_gas_price_for_investment = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Hydrocarbons",
    "MINIMUM_GAS_PRICE_FOR_INVESTMENT",
    {},
    _root,
    {},
    "_ext_constant_minimum_gas_price_for_investment",
)


@component.add(
    name="MINIMUM_OIL_PRICE_FOR_INVESTMENT",
    units="$/bbl",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_minimum_oil_price_for_investment"},
)
def minimum_oil_price_for_investment():
    """
    The minimum oil price for investment in 26 $/bbl and is based on the supply cost curve for oil from different grades according to the source: https://www.ajot.com/news/article/rystad-energy-ranks-the-cheapest-sources-of-supply- in-the-oil-industry Original source: Rystad Energy Ucube The choosen minimum reflects the breakeven point for extracting and producing the easiest accesible oil sources.
    """
    return _ext_constant_minimum_oil_price_for_investment()


_ext_constant_minimum_oil_price_for_investment = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Hydrocarbons",
    "MINIMUM_OIL_PRICE_FOR_INVESTMENT",
    {},
    _root,
    {},
    "_ext_constant_minimum_oil_price_for_investment",
)


@component.add(
    name="number_of_Oil_wells",
    units="wells",
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_number_of_oil_wells": 1},
    other_deps={
        "_integ_number_of_oil_wells": {
            "initial": {"initial_number_of_wells": 1},
            "step": {"investment_in_oil_wells": 1, "depletion_of_oil_wells": 1},
        }
    },
)
def number_of_oil_wells():
    """
    number of active wells on the global scale.
    """
    return _integ_number_of_oil_wells()


_integ_number_of_oil_wells = Integ(
    lambda: investment_in_oil_wells() - depletion_of_oil_wells(),
    lambda: initial_number_of_wells(),
    "_integ_number_of_oil_wells",
)


@component.add(
    name="Number_of_operating_coal_mines",
    units="mines",
    subscripts=["COAL_TYPES_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={
        "_integ_number_of_operating_coal_mines": 1,
        "_integ_number_of_operating_coal_mines_1": 1,
    },
    other_deps={
        "_integ_number_of_operating_coal_mines": {
            "initial": {"initial_number_of_operating_coal_mines_2008": 1},
            "step": {"investment_in_coal_mines": 1, "depletion_of_coal_mines": 1},
        },
        "_integ_number_of_operating_coal_mines_1": {
            "initial": {"initial_number_of_operating_coal_mines_2008": 1},
            "step": {"investment_in_coal_mines": 1, "depletion_of_coal_mines": 1},
        },
    },
)
def number_of_operating_coal_mines():
    """
    Number of operating mines.
    """
    value = xr.DataArray(
        np.nan, {"COAL_TYPES_I": _subscript_dict["COAL_TYPES_I"]}, ["COAL_TYPES_I"]
    )
    value.loc[["HARD_COAL"]] = _integ_number_of_operating_coal_mines().values
    value.loc[["BROWN_COAL"]] = _integ_number_of_operating_coal_mines_1().values
    return value


_integ_number_of_operating_coal_mines = Integ(
    lambda: xr.DataArray(
        float(investment_in_coal_mines().loc["HARD_COAL"])
        - float(depletion_of_coal_mines().loc["HARD_COAL"]),
        {"COAL_TYPES_I": ["HARD_COAL"]},
        ["COAL_TYPES_I"],
    ),
    lambda: xr.DataArray(
        float(initial_number_of_operating_coal_mines_2008().loc["HARD_COAL"]),
        {"COAL_TYPES_I": ["HARD_COAL"]},
        ["COAL_TYPES_I"],
    ),
    "_integ_number_of_operating_coal_mines",
)

_integ_number_of_operating_coal_mines_1 = Integ(
    lambda: xr.DataArray(
        float(investment_in_coal_mines().loc["BROWN_COAL"])
        - float(depletion_of_coal_mines().loc["BROWN_COAL"]),
        {"COAL_TYPES_I": ["BROWN_COAL"]},
        ["COAL_TYPES_I"],
    ),
    lambda: xr.DataArray(
        float(initial_number_of_operating_coal_mines_2008().loc["BROWN_COAL"]),
        {"COAL_TYPES_I": ["BROWN_COAL"]},
        ["COAL_TYPES_I"],
    ),
    "_integ_number_of_operating_coal_mines_1",
)


@component.add(
    name="Oil_available_daily_without_OPEC_spare_cap",
    units="bbl/day",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"oil_max_daily": 1, "opec_spare_cap": 1},
)
def oil_available_daily_without_opec_spare_cap():
    """
    The amount of oil available per day, minus the OPEC spare capacity.
    """
    return oil_max_daily() - opec_spare_cap()


@component.add(
    name="Oil_base_price_2006",
    units="$/bbl",
    comp_type="Constant",
    comp_subtype="Normal",
)
def oil_base_price_2006():
    """
    Oil price of the year 2006, obtained from the model. done for the purpose of price calibration for the economic model. 107.244
    """
    return 57.0584


@component.add(
    name="oil_bbl_per_EJ",
    units="bbl/EJ",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_oil_bbl_per_ej"},
)
def oil_bbl_per_ej():
    """
    Conversion factor from EJ to bbl Source: https://www.eia.gov/energyexplained/units-and-calculators/energy-conversion -calculators.php
    """
    return _ext_constant_oil_bbl_per_ej()


_ext_constant_oil_bbl_per_ej = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Hydrocarbons",
    "oil_bbl_per_EJ",
    {},
    _root,
    {},
    "_ext_constant_oil_bbl_per_ej",
)


@component.add(
    name="oil_demand",
    units="bbl/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "switch_nrg2mat_oil_demand": 1,
        "switch_materials": 1,
        "historical_oil_demand": 1,
        "world_pe_oil_bbl": 1,
    },
)
def oil_demand():
    """
    Oil demand in bbl/year. Before 2015 HISTORICAL DEMAND after 2015 demand coming from the WIlIAM enrgy module.
    """
    return if_then_else(
        np.logical_or(
            time() < 2015,
            np.logical_or(switch_nrg2mat_oil_demand() == 0, switch_materials() == 0),
        ),
        lambda: historical_oil_demand(),
        lambda: world_pe_oil_bbl(),
    )


@component.add(
    name="Oil_demand_per_day",
    units="bbl/days",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"oil_demand": 1, "unit_conversion_days_year": 1},
)
def oil_demand_per_day():
    """
    Oil demand in bbl per day.
    """
    return oil_demand() / unit_conversion_days_year()


@component.add(
    name="Oil_extraction_spare_capacity_excluding_OPEC",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "initial_spare_capacity": 1,
        "oil_demand_per_day": 1,
        "coefficient_maximum_oil_price": 1,
        "oil_available_daily_without_opec_spare_cap": 1,
    },
)
def oil_extraction_spare_capacity_excluding_opec():
    """
    Intermediate step for the Oil price calculation. Calculation is based on a LN function which describes the relation between Oil demand per day and Oil available without the opec spare capacity. The function covers the relation of the Oil price and the behaviour of the Opec countries which try to control the oil price.
    """
    return if_then_else(
        time() == 2005,
        lambda: initial_spare_capacity(),
        lambda: np.maximum(
            1 - oil_demand_per_day() / oil_available_daily_without_opec_spare_cap(),
            coefficient_maximum_oil_price(),
        ),
    )


@component.add(
    name="oil_hidden_resources",
    units="bbl",
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_oil_hidden_resources": 1},
    other_deps={
        "_integ_oil_hidden_resources": {
            "initial": {"initial_oil_resources": 1},
            "step": {"oil_resources_to_known_reserves": 1},
        }
    },
)
def oil_hidden_resources():
    """
    The model user can modify the amount of crude oil resources that are remaining and are potentially recoverable. Unconventional oil and conventional oil are added up. There is high uncertainty with regards to resource estimation. Due to this circumstances we allow the user to explore different scenarios with low, medium and high estimates found in the literature plus one additional option where the user can define. (Remaining oil resources. According to estimates based on - SOURCE, conventional and unconventional oil resources are available for discovery.Recalculated into bbl. Source: Meta-analysis of non-renewable energy resource estimates Author:MichaelDale https://doi.org/10.1016/j.enpol.2011.12.039 Projection of world fossil fuels by country Author: S.H.Mohr https://doi.org/10.1016/j.fuel.2014.10.030 There should be a separation between conventional and unconventional Oil in a later approach.)
    """
    return _integ_oil_hidden_resources()


_integ_oil_hidden_resources = Integ(
    lambda: -oil_resources_to_known_reserves(),
    lambda: initial_oil_resources(),
    "_integ_oil_hidden_resources",
)


@component.add(
    name="oil_known_reserves",
    units="bbl",
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_oil_known_reserves": 1},
    other_deps={
        "_integ_oil_known_reserves": {
            "initial": {"initial_oil_reserves_2005": 1},
            "step": {"oil_resources_to_known_reserves": 1, "extraction_of_oil": 1},
        }
    },
)
def oil_known_reserves():
    """
    BGR Energy Study 2020.-> 1.79429E+12 bbl recalculated to 2005 = 2.26998E+12 bbl According to estimates based on , conventional and unconventional oil reserves that are known from current explorations, that are available for extraction. According to estimates based on - SOURCE, conventional and unconventional oil resources are available for discovery.Recalculated into bbl. Source: Meta-analysis of non-renewable energy resource estimates Author:MichaelDale https://doi.org/10.1016/j.enpol.2011.12.039 Projection of world fossil fuels by country Author: S.H.Mohr https://doi.org/10.1016/j.fuel.2014.10.030 There should be a separation between conventional and unconventional Oil in a later approach.
    """
    return _integ_oil_known_reserves()


_integ_oil_known_reserves = Integ(
    lambda: oil_resources_to_known_reserves() - extraction_of_oil(),
    lambda: initial_oil_reserves_2005(),
    "_integ_oil_known_reserves",
)


@component.add(
    name="OIL_Laherrere_2018_modified",
    comp_type="Auxiliary",
    comp_subtype="with Lookup",
    depends_on={"time": 1},
)
def oil_laherrere_2018_modified():
    """
    Data taken from Laherrère, J., Hall, C.A.S., 2018.
    """
    return np.interp(
        time(),
        [
            1900.0,
            1901.0,
            1902.0,
            1903.0,
            1904.0,
            1905.0,
            1906.0,
            1907.0,
            1908.0,
            1909.0,
            1910.0,
            1911.0,
            1912.0,
            1913.0,
            1914.0,
            1915.0,
            1916.0,
            1917.0,
            1918.0,
            1919.0,
            1920.0,
            1921.0,
            1922.0,
            1923.0,
            1924.0,
            1925.0,
            1926.0,
            1927.0,
            1928.0,
            1929.0,
            1930.0,
            1931.0,
            1932.0,
            1933.0,
            1934.0,
            1935.0,
            1936.0,
            1937.0,
            1938.0,
            1939.0,
            1940.0,
            1941.0,
            1942.0,
            1943.0,
            1944.0,
            1945.0,
            1946.0,
            1947.0,
            1948.0,
            1949.0,
            1950.0,
            1951.0,
            1952.0,
            1953.0,
            1954.0,
            1955.0,
            1956.0,
            1957.0,
            1958.0,
            1959.0,
            1960.0,
            1961.0,
            1962.0,
            1963.0,
            1964.0,
            1965.0,
            1966.0,
            1967.0,
            1968.0,
            1969.0,
            1970.0,
            1971.0,
            1972.0,
            1973.0,
            1974.0,
            1975.0,
            1976.0,
            1977.0,
            1978.0,
            1979.0,
            1980.0,
            1981.0,
            1982.0,
            1983.0,
            1984.0,
            1985.0,
            1986.0,
            1987.0,
            1988.0,
            1989.0,
            1990.0,
            1991.0,
            1992.0,
            1993.0,
            1994.0,
            1995.0,
            1996.0,
            1997.0,
            1998.0,
            1999.0,
            2000.0,
            2001.0,
            2002.0,
            2003.0,
            2004.0,
            2005.0,
            2006.0,
            2007.0,
            2008.0,
            2009.0,
            2010.0,
            2011.0,
            2012.0,
            2013.0,
            2014.0,
            2015.0,
            2016.0,
            2017.0,
            2018.0,
            2019.0,
            2020.0,
            2021.0,
        ],
        [
            0.45863,
            0.498082,
            0.533973,
            0.59726,
            0.589315,
            0.584384,
            0.723836,
            0.782466,
            0.818356,
            0.898082,
            0.943562,
            0.965479,
            1.05562,
            1.11644,
            1.18356,
            1.25342,
            1.37781,
            1.37945,
            1.52301,
            1.8874,
            2.09863,
            2.35315,
            2.78274,
            2.7789,
            2.92575,
            3.00493,
            3.46027,
            3.63014,
            4.07123,
            3.86301,
            3.76164,
            3.58904,
            3.95069,
            4.16986,
            4.53151,
            4.90959,
            5.5863,
            5.44658,
            5.71507,
            5.89041,
            6.08493,
            5.73425,
            6.18356,
            7.10411,
            7.10959,
            7.52055,
            8.27945,
            9.40548,
            9.32603,
            10.4192,
            11.7342,
            12.3808,
            13.1452,
            13.7479,
            15.4137,
            16.7808,
            17.6411,
            18.1041,
            19.5452,
            20.99,
            22.45,
            24.35,
            26.13,
            28.18,
            30.33,
            32.96,
            35.392,
            38.0173,
            41.7441,
            45.9148,
            48.5515,
            51.1805,
            58.5173,
            58.5573,
            55.666,
            60.2576,
            62.747,
            63.2919,
            66.025,
            63.105,
            59.8193,
            57.2086,
            57.0237,
            58.5522,
            58.0795,
            60.7417,
            61.2429,
            63.5206,
            64.677,
            65.4993,
            65.3297,
            65.3544,
            65.6566,
            66.9907,
            68.4883,
            70.0562,
            72.2407,
            73.7345,
            72.8863,
            75.5231,
            75.5868,
            74.9908,
            77.6156,
            81.3569,
            83.3354,
            83.2224,
            83.2323,
            84.3869,
            83.7993,
            86.0108,
            86.526,
            88.5181,
            88.869,
            90.8142,
            90.8869,
            91.4937,
            92.0961,
            92.5056,
            92.815,
            93.025,
            93.1368,
            93.152,
        ],
    )


@component.add(
    name="Oil_max_daily",
    units="bbl/days",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"oil_max_extraction_capacity": 1, "unit_conversion_days_year": 1},
)
def oil_max_daily():
    """
    Maximun Oil extraction per day.
    """
    return oil_max_extraction_capacity() / unit_conversion_days_year()


@component.add(
    name="Oil_max_extraction_capacity",
    units="bbl/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"oil_per_oil_well": 1, "number_of_oil_wells": 1},
)
def oil_max_extraction_capacity():
    """
    Maximium Oil extraction capacity in bbl per year.
    """
    return oil_per_oil_well() * number_of_oil_wells()


@component.add(
    name="oil_per_oil_well",
    units="bbl/(Year*wells)",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"initial_oil_production_per_year": 1, "initial_number_of_wells": 1},
)
def oil_per_oil_well():
    """
    oil per well max cap first year 5,71 Bt*Oe/ per year/1,821 million wells (2020) values got recalculated to bbl 4,1 Bt*Oe(2005)/ 1,56 million wells values got recalculated to bbl An assumption made by the authors to simplify the complex issues of Wells with different productivity. The authors assume that each well has the same productivity- from a global perspective. In reality, there is a small amount of highly productive wells and a large amount of less productive wells. Sources:
    """
    return initial_oil_production_per_year() / initial_number_of_wells()


@component.add(
    name="Oil_price_economy_adjusted",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "oil_price_index_economy": 1},
)
def oil_price_economy_adjusted():
    """
    Control to keep the economic price index constant and 100 for the years 2005 and 2006 while the stocks fill up the the model stablizes.
    """
    return if_then_else(
        time() < 2015,
        lambda: 100,
        lambda: float(oil_price_index_economy().loc["Oil_W"]),
    )


@component.add(
    name="OIL_PRICE_GROWTH_LIMIT",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_oil_price_growth_limit"},
)
def oil_price_growth_limit():
    """
    Limit to the time step variation in oil price. Value of 0.2.
    """
    return _ext_constant_oil_price_growth_limit()


_ext_constant_oil_price_growth_limit = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Hydrocarbons",
    "OIL_PRICE_GROWTH_LIMIT",
    {},
    _root,
    {},
    "_ext_constant_oil_price_growth_limit",
)


@component.add(
    name='"OIL_PRICE_HISTORICAL_$/bbl"',
    units="$/bbl",
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_oil_price_historical_bbl",
        "__data__": "_ext_data_oil_price_historical_bbl",
        "time": 1,
    },
)
def oil_price_historical_bbl():
    """
    Historical Oil price in dollars per bbl. Source:U.S. Energy Information Administration, 2022. https://www.eia.gov/dnav/pet/pet_pri_spt_s1_m.htm
    """
    return _ext_data_oil_price_historical_bbl(time())


_ext_data_oil_price_historical_bbl = ExtData(
    "model_parameters/materials/materials.xlsx",
    "Hydrocarbons",
    "TIME_SERIES_HYDRO",
    "OIL_PRICE_HISTORICAL",
    None,
    {},
    _root,
    {},
    "_ext_data_oil_price_historical_bbl",
)


@component.add(
    name="Oil_price_index_economy",
    units="DMNL",
    subscripts=["HYDROCARBONS_W_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_mat2eco_oil_price": 1,
        "oil_price_jump_look_up": 1,
        "estimated_oil_price_with_tax": 1,
        "oil_base_price_2006": 1,
        "price_transformation": 1,
    },
)
def oil_price_index_economy():
    """
    Price Index that gets delivered to the econimic model. IF THEN ELSE function and the switch are used to switch between indigenous price calculation and a look up function. (estimated oil price with tax [Oil W]/Oil base price 2006)*PRICE TRANSFORMATION)
    """
    return xr.DataArray(
        if_then_else(
            switch_mat2eco_oil_price() == 0,
            lambda: oil_price_jump_look_up(),
            lambda: (
                float(estimated_oil_price_with_tax().loc["Oil_W"])
                / oil_base_price_2006()
            )
            * price_transformation(),
        ),
        {"HYDROCARBONS_W_I": _subscript_dict["HYDROCARBONS_W_I"]},
        ["HYDROCARBONS_W_I"],
    )


@component.add(
    name="Oil_price_jump_look_up",
    comp_type="Auxiliary",
    comp_subtype="with Lookup",
    depends_on={"time": 1},
)
def oil_price_jump_look_up():
    """
    Oil look up table for thesting the loop between economy and materials.
    """
    return np.interp(
        time(),
        [
            2005.0,
            2006.0,
            2007.0,
            2008.0,
            2009.0,
            2010.0,
            2011.0,
            2012.0,
            2013.0,
            2014.0,
            2015.0,
            2016.0,
            2018.0,
            2019.0,
            2020.0,
            2021.0,
            2022.0,
            2023.0,
            2032.21,
        ],
        [
            100.0,
            100.0,
            100.0,
            100.0,
            100.0,
            100.0,
            100.0,
            100.0,
            100.0,
            100.0,
            100.0,
            100.0,
            100.0,
            100.0,
            100.0,
            100.0,
            100.0,
            100.0,
            100.0,
        ],
    )


@component.add(
    name="OIL_RESOURCE_ESTIMATION_HIGH_SP",
    units="bbl",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_oil_resource_estimation_high_sp"},
)
def oil_resource_estimation_high_sp():
    """
    High oil resources estimation
    """
    return _ext_constant_oil_resource_estimation_high_sp()


_ext_constant_oil_resource_estimation_high_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "materials",
    "OIL_RESOURCE_ESTIMATION_HIGH_SP",
    {},
    _root,
    {},
    "_ext_constant_oil_resource_estimation_high_sp",
)


@component.add(
    name="OIL_RESOURCE_ESTIMATION_LOW_SP",
    units="bbl",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_oil_resource_estimation_low_sp"},
)
def oil_resource_estimation_low_sp():
    """
    Low oil resources estimation
    """
    return _ext_constant_oil_resource_estimation_low_sp()


_ext_constant_oil_resource_estimation_low_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "materials",
    "OIL_RESOURCE_ESTIMATION_LOW_SP",
    {},
    _root,
    {},
    "_ext_constant_oil_resource_estimation_low_sp",
)


@component.add(
    name="OIL_RESOURCE_ESTIMATION_MED_SP",
    units="bbl",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_oil_resource_estimation_med_sp"},
)
def oil_resource_estimation_med_sp():
    """
    Medium oil resources estimation
    """
    return _ext_constant_oil_resource_estimation_med_sp()


_ext_constant_oil_resource_estimation_med_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "materials",
    "OIL_RESOURCE_ESTIMATION_MED_SP",
    {},
    _root,
    {},
    "_ext_constant_oil_resource_estimation_med_sp",
)


@component.add(
    name="OIL_RESOURCE_ESTIMATION_USER_DEFINED_SP",
    units="bbl",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_oil_resource_estimation_user_defined_sp"
    },
)
def oil_resource_estimation_user_defined_sp():
    """
    User defined oil resources estimation
    """
    return _ext_constant_oil_resource_estimation_user_defined_sp()


_ext_constant_oil_resource_estimation_user_defined_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "materials",
    "OIL_User_defines",
    {},
    _root,
    {},
    "_ext_constant_oil_resource_estimation_user_defined_sp",
)


@component.add(
    name="Oil_resources_to_known_reserves",
    units="bbl/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"oil_hidden_resources": 1, "oil_search_rate": 1},
)
def oil_resources_to_known_reserves():
    """
    Oil that is prospected and moving from resources to reserves.
    """
    return oil_hidden_resources() * oil_search_rate()


@component.add(
    name="OIL_SEARCH_RATE",
    units="1/Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_oil_search_rate"},
)
def oil_search_rate():
    """
    This is the discovery rate that puts the discovery peak in 1965, the year the data indicates as the peak according to Campbell. Based on the World 7 Parameter-from the World 7 Fossil Fuel model.
    """
    return _ext_constant_oil_search_rate()


_ext_constant_oil_search_rate = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Hydrocarbons",
    "OIL_SEARCH_RATE",
    {},
    _root,
    {},
    "_ext_constant_oil_search_rate",
)


@component.add(
    name="OIL_URR",
    units="bbl",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "initial_oil_resources": 1,
        "initial_oil_reserves_2005": 1,
        "initial_oil_cumulatively_extracted_2005": 1,
    },
)
def oil_urr():
    """
    initial availability of resources+reserves of Oil
    """
    return (
        initial_oil_resources()
        + initial_oil_reserves_2005()
        + initial_oil_cumulatively_extracted_2005()
    )


@component.add(
    name="oil_well_depletion_rate",
    units="1/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "urr_oil": 2,
        "cumulative_total_oil_extraction": 2,
        "depletion_factor_after_peak": 1,
        "oil_well_depletion_rate_before_peak": 1,
    },
)
def oil_well_depletion_rate():
    """
    Oil well depletion rate, as an annual share of the existing number of oil wells. Assumption made by the authors that wells are depleting faster when the half of URR is reached. Its a simplification because in the real world the productivity per well would decrease if the well production peak is reached. Here the assumption is that more wells will go out of production, because they have a shorter life-time, in the moment half of the global URR is reached.
    """
    return if_then_else(
        urr_oil() / 2 <= cumulative_total_oil_extraction(),
        lambda: (cumulative_total_oil_extraction() / urr_oil())
        / depletion_factor_after_peak(),
        lambda: oil_well_depletion_rate_before_peak(),
    )


@component.add(
    name="OIL_WELL_DEPLETION_RATE_BEFORE_PEAK",
    units="1/Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_oil_well_depletion_rate_before_peak"},
)
def oil_well_depletion_rate_before_peak():
    """
    Parameter based on the observation that well lifetimes mentioned in the literature reach from 20 to 40 years. The parameter choosed here was derived by matching the model result with historical data. Assumption made by the authors that wells are depletiing faster when the half of URR is reached. Its a simplification because in the real world the productivity per well would decrease if the well production peak is reached. Value is 0.032
    """
    return _ext_constant_oil_well_depletion_rate_before_peak()


_ext_constant_oil_well_depletion_rate_before_peak = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Hydrocarbons",
    "OIL_WELL_DEPLETION_RATE",
    {},
    _root,
    {},
    "_ext_constant_oil_well_depletion_rate_before_peak",
)


@component.add(
    name="Oil_WELL_INVESTMENT_CAP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_oil_well_investment_cap"},
)
def oil_well_investment_cap():
    """
    Maximun growth rate of active wells. This rate was chosen on the bases of the historical maximum growth in drilling activity. Source: https://www.rystadenergy.com/newsevents/news/newsletters/OfsArchive/ofs-november-2018 / https://www.drillingcontractor.org/670000-wells-to-be-drilled-through-2020-28709 https://www.rystadenergy.com/energy-themes/supply-chain/wells/well-cube/ https://www.eia.gov/dnav/pet/hist/LeafHandler.ashx?n=pet&s=rwtc&f=a
    """
    return _ext_constant_oil_well_investment_cap()


_ext_constant_oil_well_investment_cap = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Hydrocarbons",
    "Oil_WELL_INVESTMENT_CAP",
    {},
    _root,
    {},
    "_ext_constant_oil_well_investment_cap",
)


@component.add(
    name="OPEC_spare_cap",
    units="bbl/day",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_opec_scenario_fossil_fuel_paper_sp": 1,
        "set_opec_spare_capacity_sp": 1,
        "oil_max_daily": 4,
        "set_opec_spare_capacity_before_and_after_scenario_sp": 2,
        "coeffiecients_opec_spare_cap": 12,
        "select_opec_target_price": 6,
        "delayed_estimated_oil_price": 2,
        "time": 5,
        "oil_demand_per_day": 4,
    },
)
def opec_spare_cap():
    """
    Calculation that determines the OPEC SPARE capacity based on the COEFFICIENTS, Oil demand per, Oil max and the desired OPEC target price. Coeffiecients are choosen by fitting the historical OPEC SPARE capacity and econometric estimations. Equations old: IF THEN ELSE(delayed estimated Oil price > SELECT OPEC TARGET PRICE,0, IF THEN ELSE ((+COEFFIECIENTS OPEC SPARE CAP[A EXP CURVE] + COEFFIECIENTS OPEC SPARE CAP[B EXP CURVE] * SELECT OPEC TARGET PRICE +COEFFIECIENTS OPEC SPARE CAP[C EXP CURVE]*(1 - Oil demand per day / Oil max daily)) * 1e+06<=0, 0 , MIN((+COEFFIECIENTS OPEC SPARE CAP[A EXP CURVE] + COEFFIECIENTS OPEC SPARE CAP[B EXP CURVE] * SELECT OPEC TARGET PRICE + COEFFIECIENTS OPEC SPARE CAP[C EXP CURVE] * (1-Oil demand per day/Oil max daily)) * 1e+06, 7e+06 )) )
    """
    return if_then_else(
        switch_opec_scenario_fossil_fuel_paper_sp() == 1,
        lambda: if_then_else(
            np.logical_and(time() >= 2017, time() < 2025),
            lambda: set_opec_spare_capacity_before_and_after_scenario_sp(),
            lambda: if_then_else(
                np.logical_and(time() >= 2025, time() <= 2030),
                lambda: set_opec_spare_capacity_sp(),
                lambda: if_then_else(
                    time() > 2030,
                    lambda: set_opec_spare_capacity_before_and_after_scenario_sp(),
                    lambda: if_then_else(
                        delayed_estimated_oil_price() > select_opec_target_price(),
                        lambda: 0,
                        lambda: if_then_else(
                            (
                                float(coeffiecients_opec_spare_cap().loc["A_EXP_CURVE"])
                                + float(
                                    coeffiecients_opec_spare_cap().loc["B_EXP_CURVE"]
                                )
                                * select_opec_target_price()
                                + float(
                                    coeffiecients_opec_spare_cap().loc["C_EXP_CURVE"]
                                )
                                * (1 - oil_demand_per_day() / oil_max_daily())
                            )
                            * 1000000.0
                            <= 0,
                            lambda: 0,
                            lambda: np.minimum(
                                (
                                    float(
                                        coeffiecients_opec_spare_cap().loc[
                                            "A_EXP_CURVE"
                                        ]
                                    )
                                    + float(
                                        coeffiecients_opec_spare_cap().loc[
                                            "B_EXP_CURVE"
                                        ]
                                    )
                                    * select_opec_target_price()
                                    + float(
                                        coeffiecients_opec_spare_cap().loc[
                                            "C_EXP_CURVE"
                                        ]
                                    )
                                    * (1 - oil_demand_per_day() / oil_max_daily())
                                )
                                * 1000000.0,
                                7000000.0,
                            ),
                        ),
                    ),
                ),
            ),
        ),
        lambda: if_then_else(
            delayed_estimated_oil_price() > select_opec_target_price(),
            lambda: 0,
            lambda: if_then_else(
                (
                    float(coeffiecients_opec_spare_cap().loc["A_EXP_CURVE"])
                    + float(coeffiecients_opec_spare_cap().loc["B_EXP_CURVE"])
                    * select_opec_target_price()
                    + float(coeffiecients_opec_spare_cap().loc["C_EXP_CURVE"])
                    * (1 - oil_demand_per_day() / oil_max_daily())
                )
                * 1000000.0
                <= 0,
                lambda: 0,
                lambda: np.minimum(
                    (
                        float(coeffiecients_opec_spare_cap().loc["A_EXP_CURVE"])
                        + float(coeffiecients_opec_spare_cap().loc["B_EXP_CURVE"])
                        * select_opec_target_price()
                        + float(coeffiecients_opec_spare_cap().loc["C_EXP_CURVE"])
                        * (1 - oil_demand_per_day() / oil_max_daily())
                    )
                    * 1000000.0,
                    7000000.0,
                ),
            ),
        ),
    )


@component.add(
    name="OPEC_TARGET_PRICE_JUMP",
    comp_type="Auxiliary",
    comp_subtype="with Lookup",
    depends_on={"time": 1},
)
def opec_target_price_jump():
    """
    Test variable.
    """
    return np.interp(
        time(),
        [2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016],
        [100, 100, 100, 200, 300, 200, 100, 100, 100, 100, 100, 100],
    )


@component.add(
    name="OPEC_TARGET_PRICE_LOW_MED_HIGH_OTHER_SP",
    units="$/bbl",
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_opec_target_price_low_med_high_other_sp",
        "__data__": "_ext_data_opec_target_price_low_med_high_other_sp",
        "time": 1,
    },
)
def opec_target_price_low_med_high_other_sp():
    """
    The EIA predicts that by 2025 Brent crude oil's nominal price will rise to $67/b (in 2021 dollars). By 2030, world demand is seen driving Brent prices to $79/b. By 2040, prices are projected to be $84/b. By then, the cheap oil sources will have been exhausted, making it more expensive to extract oil. By 2050, oil prices could be $90/b. Source https://www.thebalancemoney.com/oil-price-forecast-3306219 accessed at : 07.02.2023 at 09:46 Brent Crude The Organization of Petroleum Exporting Countries (OPEC) uses Brent Crude as its pricing benchmark. OPEC comprises 14 oil-producing countries and is largely responsible for setting oil prices. Brent Crude is waterborne, which makes it cheaper to transport than WTI, which is extracted from landlocked areas of the US.Jan 8, 2023 Source: https://corporatefinanceinstitute.com/resources/commodities/north-sea-brent-crude/#: :text=The%20Organization%20of%20Petroleum%20Exporting,landlocked%20areas%20 of%20the%20US. accessed at : 07.02.2023 at 09:46 The User has the choice to modify the forecast with the Variable OPEC TARGET PRICE SAME AS EIA OIL FORECAST MED in the Scenario Sheet by loading differen data sets. The standard is OPEC_TAGRET_PRICE_MED. Options: OPEC_TARGET_PRICE_LOW OPEC_TAGRET_PRICE_MED OPEC_TARGET_PRICE_HIGH OPEC_TARGET_PRICE_OTHER
    """
    return _ext_data_opec_target_price_low_med_high_other_sp(time())


_ext_data_opec_target_price_low_med_high_other_sp = ExtData(
    "scenario_parameters/scenario_parameters.xlsx",
    "materials",
    "TIME_SERIES",
    "OPEC_TARGET_PRICE_MED",
    "interpolate",
    {},
    _root,
    {},
    "_ext_data_opec_target_price_low_med_high_other_sp",
)


@component.add(
    name="POTENTIAL_RECOVERY_FACTOR",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_potential_recovery_factor"},
)
def potential_recovery_factor():
    """
    Potential recovery factor according to Source: Global Energy Assessment-Toward a Sustainable Future (Rogner et al., 2012) value : 0.2
    """
    return _ext_constant_potential_recovery_factor()


_ext_constant_potential_recovery_factor = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Hydrocarbons",
    "POTENTIAL_RECOVERY_FACTOR",
    {},
    _root,
    {},
    "_ext_constant_potential_recovery_factor",
)


@component.add(
    name="reserves_in_operating_coal_mines",
    units="EJ",
    subscripts=["COAL_TYPES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "total_coal_production_capacity_ej": 2,
        "increase_in_depletion_after_peak_coal": 2,
    },
)
def reserves_in_operating_coal_mines():
    """
    Calculates the reserves in operinting coal mines. Used for the invesment in mines function. Only if there is enough reserves left investment in mines will take place.
    """
    value = xr.DataArray(
        np.nan, {"COAL_TYPES_I": _subscript_dict["COAL_TYPES_I"]}, ["COAL_TYPES_I"]
    )
    value.loc[["HARD_COAL"]] = float(
        total_coal_production_capacity_ej().loc["HARD_COAL"]
    ) * (1 / float(increase_in_depletion_after_peak_coal().loc["HARD_COAL"]))
    value.loc[["BROWN_COAL"]] = float(
        total_coal_production_capacity_ej().loc["BROWN_COAL"]
    ) * (1 / float(increase_in_depletion_after_peak_coal().loc["BROWN_COAL"]))
    return value


@component.add(
    name="SELECT_BROWN_COAL_RESOURCE_ESTIMATION_SP",
    units="DMML",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_select_brown_coal_resource_estimation_sp"
    },
)
def select_brown_coal_resource_estimation_sp():
    return _ext_constant_select_brown_coal_resource_estimation_sp()


_ext_constant_select_brown_coal_resource_estimation_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "materials",
    "SELECT_BROWN_COAL_RESOURCE_ESTIMATION_SP",
    {},
    _root,
    {},
    "_ext_constant_select_brown_coal_resource_estimation_sp",
)


@component.add(
    name="SELECT_GAS_RESOURCE_ESTIMATION_SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_select_gas_resource_estimation_sp"},
)
def select_gas_resource_estimation_sp():
    """
    The model user can modify the amount of gas resources that are remaining and are potentially recoverable. Options: 0: Low 1: medium 2: High 3: user defined
    """
    return _ext_constant_select_gas_resource_estimation_sp()


_ext_constant_select_gas_resource_estimation_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "materials",
    "SELECT_GAS_RESPOURCE_ESTIMATION_SP",
    {},
    _root,
    {},
    "_ext_constant_select_gas_resource_estimation_sp",
)


@component.add(
    name="SELECT_HARD_COAL_RESOURCE_ESTIMATION_SP",
    units="DMML",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_select_hard_coal_resource_estimation_sp"
    },
)
def select_hard_coal_resource_estimation_sp():
    return _ext_constant_select_hard_coal_resource_estimation_sp()


_ext_constant_select_hard_coal_resource_estimation_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "materials",
    "SELECT_HARD_COAL_RESOURCE_ESTIMATION_SP",
    {},
    _root,
    {},
    "_ext_constant_select_hard_coal_resource_estimation_sp",
)


@component.add(
    name="SELECT_OIL_RESOURCE_ESTIMATION_SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_select_oil_resource_estimation_sp"},
)
def select_oil_resource_estimation_sp():
    """
    The model user can modify the amount of crude oil resources that are remaining and are potentially recoverable. Unconventional oil and conventional oil are added up. There is high uncertainty with regards to resource estimation. Due to this circumstances we allow the user to explore different scenarios with low, medium and high estimates found in the literature plus one additional option where the user can define. Options: 0: Low 1: medium 2: High 3: user defined
    """
    return _ext_constant_select_oil_resource_estimation_sp()


_ext_constant_select_oil_resource_estimation_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "materials",
    "SELECT_OIL_RESPOURCE_ESTIMATION_SP",
    {},
    _root,
    {},
    "_ext_constant_select_oil_resource_estimation_sp",
)


@component.add(
    name="SELECT_OPEC_TARGET_PRICE",
    units="$/bbl",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "opec_target_price_low_med_high_other_sp": 1,
        "historical_target_price": 1,
    },
)
def select_opec_target_price():
    """
    Switch introduced to switch between the OPEC SPARE CAP price with is estimated on historical observations and the target price past 2020. After 2020 the Opec target price is a policy variable. We need to decide how we increase the target price past 2020. IF THEN ELSE(Time>2020, TARGET PRICE 2020*(1+0.001)^(Time-2020), HISTORICAL TARGET PRICE)
    """
    return if_then_else(
        time() > 2020,
        lambda: opec_target_price_low_med_high_other_sp(),
        lambda: historical_target_price(),
    )


@component.add(
    name="seperation_of_mining_types",
    units="mines/Year",
    subscripts=["COAL_TYPES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "desired_new_coal_mines": 4,
        "max_investment_in_coal_mines": 4,
        "share_of_coal_type": 4,
    },
)
def seperation_of_mining_types():
    """
    Variables determines if the invesment into new mines will be according to the price or if it will be based on the maximum of capacity increase if the desired mines are higher than the maxium possible increase of one year to another. The equation is splid into the different mine types HARD and BROWN COAL
    """
    value = xr.DataArray(
        np.nan, {"COAL_TYPES_I": _subscript_dict["COAL_TYPES_I"]}, ["COAL_TYPES_I"]
    )
    value.loc[["HARD_COAL"]] = if_then_else(
        desired_new_coal_mines() > max_investment_in_coal_mines(),
        lambda: max_investment_in_coal_mines()
        * float(share_of_coal_type().loc["HARD_COAL"]),
        lambda: np.maximum(
            desired_new_coal_mines() * float(share_of_coal_type().loc["HARD_COAL"]), 0
        ),
    )
    value.loc[["BROWN_COAL"]] = if_then_else(
        desired_new_coal_mines() > max_investment_in_coal_mines(),
        lambda: max_investment_in_coal_mines()
        * float(share_of_coal_type().loc["BROWN_COAL"]),
        lambda: np.maximum(
            desired_new_coal_mines() * float(share_of_coal_type().loc["BROWN_COAL"]), 0
        ),
    )
    return value


@component.add(
    name="SET_OPEC_SPARE_CAPACITY_BEFORE_AND_AFTER_SCENARIO_SP",
    units="bbl/day",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_set_opec_spare_capacity_before_and_after_scenario_sp"
    },
)
def set_opec_spare_capacity_before_and_after_scenario_sp():
    """
    User can modify the amount of the OPEC spare capacity in bbl/day. Between 2017 to 2025 and from 2030 onwards. Used for scenarios to test the impact of the OPEC countries and thier effect on the oil price.
    """
    return _ext_constant_set_opec_spare_capacity_before_and_after_scenario_sp()


_ext_constant_set_opec_spare_capacity_before_and_after_scenario_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "materials",
    "SET_OPEC_SPARE_CAPACITY_BEFORE_AND_AFTER_SCENARIO_SP",
    {},
    _root,
    {},
    "_ext_constant_set_opec_spare_capacity_before_and_after_scenario_sp",
)


@component.add(
    name="SET_OPEC_SPARE_CAPACITY_SP",
    units="bbl/day",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_set_opec_spare_capacity_sp"},
)
def set_opec_spare_capacity_sp():
    """
    User can modify the amount of the OPEC spare capacity in bbl/day. Used for scenarios to test the impact of the OPEC countries and thier effect on the oil price. The spare capacity that is from 2025 to 2030.
    """
    return _ext_constant_set_opec_spare_capacity_sp()


_ext_constant_set_opec_spare_capacity_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "materials",
    "SET_OPEC_SPARE_CAPACITY_SP",
    {},
    _root,
    {},
    "_ext_constant_set_opec_spare_capacity_sp",
)


@component.add(
    name="SHARE_OF_COAL_TYPE",
    units="DMNL",
    subscripts=["COAL_TYPES_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_share_of_coal_type"},
)
def share_of_coal_type():
    """
    HARD and BROWN coal share calculated based on the source: Global Energy Assessment-Toward a Sustainable Future (Rogner et al., 2012) HARD COAL = 0.934 BROWN COAL = 0.065
    """
    return _ext_constant_share_of_coal_type()


_ext_constant_share_of_coal_type = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Hydrocarbons",
    "SHARE_OF_COAL_TYPES*",
    {"COAL_TYPES_I": _subscript_dict["COAL_TYPES_I"]},
    _root,
    {"COAL_TYPES_I": _subscript_dict["COAL_TYPES_I"]},
    "_ext_constant_share_of_coal_type",
)


@component.add(
    name="sum_of_new_coal_mines_per_year",
    units="mines/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"investment_in_coal_mines": 2},
)
def sum_of_new_coal_mines_per_year():
    """
    Sum of mines constructed per year.
    """
    return float(investment_in_coal_mines().loc["HARD_COAL"]) + float(
        investment_in_coal_mines().loc["BROWN_COAL"]
    )


@component.add(
    name="SWITCH_MAT2ECO_COAL_PRICE",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_mat2eco_coal_price"},
)
def switch_mat2eco_coal_price():
    """
    Intermodule links SWITCH, it can take two values: 0: the link is broken, the intermodule variable is replaced by an exogenous parameter. 1: the link between modules is operational.
    """
    return _ext_constant_switch_mat2eco_coal_price()


_ext_constant_switch_mat2eco_coal_price = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_MAT2ECO_COAL_PRICE",
    {},
    _root,
    {},
    "_ext_constant_switch_mat2eco_coal_price",
)


@component.add(
    name="SWITCH_MAT2ECO_GAS_PRICE",
    units="1",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_mat2eco_gas_price"},
)
def switch_mat2eco_gas_price():
    """
    Intermodule links SWITCH, it can take two values: 0: the link is broken, the intermodule variable is replaced by an exogenous parameter. 1: the link between modules is operational.
    """
    return _ext_constant_switch_mat2eco_gas_price()


_ext_constant_switch_mat2eco_gas_price = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_MAT2ECO_GAS_PRICE",
    {},
    _root,
    {},
    "_ext_constant_switch_mat2eco_gas_price",
)


@component.add(
    name="SWITCH_MAT2ECO_OIL_PRICE",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_mat2eco_oil_price"},
)
def switch_mat2eco_oil_price():
    """
    Intermodule links SWITCH, it can take two values: 0: the link is broken, the intermodule variable is replaced by an exogenous parameter. 1: the link between modules is operational.
    """
    return _ext_constant_switch_mat2eco_oil_price()


_ext_constant_switch_mat2eco_oil_price = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_MAT2ECO_OIL_PRICE",
    {},
    _root,
    {},
    "_ext_constant_switch_mat2eco_oil_price",
)


@component.add(
    name="SWITCH_NRG2MAT_COAL_DEMAND",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_nrg2mat_coal_demand"},
)
def switch_nrg2mat_coal_demand():
    """
    Intermodule links SWITCH, it can take two values: 0: the link is broken, the intermodule variable is replaced by an exogenous parameter. 1: the link between modules is operational.
    """
    return _ext_constant_switch_nrg2mat_coal_demand()


_ext_constant_switch_nrg2mat_coal_demand = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_NRG2MAT_COAL_DEMAND",
    {},
    _root,
    {},
    "_ext_constant_switch_nrg2mat_coal_demand",
)


@component.add(
    name="SWITCH_NRG2MAT_GAS_DEMAND",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_nrg2mat_gas_demand"},
)
def switch_nrg2mat_gas_demand():
    """
    Intermodule links SWITCH, it can take two values: 0: the link is broken, the intermodule variable is replaced by an exogenous parameter. 1: the link between modules is operational.
    """
    return _ext_constant_switch_nrg2mat_gas_demand()


_ext_constant_switch_nrg2mat_gas_demand = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_NRG2MAT_GAS_DEMAND",
    {},
    _root,
    {},
    "_ext_constant_switch_nrg2mat_gas_demand",
)


@component.add(
    name="SWITCH_NRG2MAT_OIL_DEMAND",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_nrg2mat_oil_demand"},
)
def switch_nrg2mat_oil_demand():
    """
    Intermodule links SWITCH, it can take two values: 0: the link is broken, the intermodule variable is replaced by an exogenous parameter. 1: the link between modules is operational.
    """
    return _ext_constant_switch_nrg2mat_oil_demand()


_ext_constant_switch_nrg2mat_oil_demand = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_NRG2MAT_OIL_DEMAND",
    {},
    _root,
    {},
    "_ext_constant_switch_nrg2mat_oil_demand",
)


@component.add(
    name="SWITCH_OIL_PRICE_GROWTH_LIMIT", comp_type="Constant", comp_subtype="Normal"
)
def switch_oil_price_growth_limit():
    """
    Switch for constrain the time step variation in oil price 0: OFF: the price is taken directly form the first estiamtion 1: ON: the variation in th price is limited
    """
    return 1


@component.add(
    name="SWITCH_OPEC_SCENARIO_FOSSIL_FUEL_PAPER_SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_switch_opec_scenario_fossil_fuel_paper_sp"
    },
)
def switch_opec_scenario_fossil_fuel_paper_sp():
    """
    Switch for the OPEC scenario used in the FOSSIL FUEL paper. If the switch = 1 OPEC spare capacity is set to 3mbbl/day between 2017 to 2025. Than modified to either 0 mbbl/day or 6 mbbl/day. After 2030 the spare capacity is set to 3 mbbl/day. When the Switch= 0 Opec spare capacity is determined by the OPEC target price.
    """
    return _ext_constant_switch_opec_scenario_fossil_fuel_paper_sp()


_ext_constant_switch_opec_scenario_fossil_fuel_paper_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "materials",
    "SWITCH_OPEC_SCENARIO_FOSSIL_FUEL_PAPER_SP",
    {},
    _root,
    {},
    "_ext_constant_switch_opec_scenario_fossil_fuel_paper_sp",
)


@component.add(
    name="SWITCH_TAX_RATE_ON_EXTRACTION_OF_RESOURCES_SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_switch_tax_rate_on_extraction_of_resources_sp"
    },
)
def switch_tax_rate_on_extraction_of_resources_sp():
    """
    SWITCH for the policy "Tax rate on extraction of resources" it can take two values: 0: The policy is switched off 1: The policy in effect is switched on
    """
    return _ext_constant_switch_tax_rate_on_extraction_of_resources_sp()


_ext_constant_switch_tax_rate_on_extraction_of_resources_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "materials",
    "SWITCH_TAX_RATE_ON_EXTRACTION_OF_RESOURCES_SP",
    {},
    _root,
    {},
    "_ext_constant_switch_tax_rate_on_extraction_of_resources_sp",
)


@component.add(
    name="TARGET_PRICE_2020", units="$/bbl", comp_type="Constant", comp_subtype="Normal"
)
def target_price_2020():
    """
    Target price of 2020.In the moment constant. In a future version it will be a Dynamic value.
    """
    return 65


@component.add(
    name="TAX_RATE_ON_EXTRACTION_OF_RESOURCES_SP",
    subscripts=["MATERIALS_W_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_tax_rate_on_extraction_of_resources_sp"},
)
def tax_rate_on_extraction_of_resources_sp():
    """
    TAX_RATE_ON_EXTRACTION_LOW TAX_RATE_ON_EXTRACTION_MEDIUM TAX_RATE_ON_EXTRACTION_HIGH TAX_RATE_ON_EXTRACTION_OTHER
    """
    return _ext_constant_tax_rate_on_extraction_of_resources_sp()


_ext_constant_tax_rate_on_extraction_of_resources_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "materials",
    "TAX_RATE_ON_EXTRACTION_MEDIUM",
    {"MATERIALS_W_I": _subscript_dict["MATERIALS_W_I"]},
    _root,
    {"MATERIALS_W_I": _subscript_dict["MATERIALS_W_I"]},
    "_ext_constant_tax_rate_on_extraction_of_resources_sp",
)


@component.add(
    name="tax_revenue_from_hydrocarbons",
    units="Mdollars/Year",
    subscripts=["HYDROCARBONS_W_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "extraction_of_oil": 1,
        "estimated_oil_price_with_tax": 1,
        "estimated_oil_price": 1,
        "unit_conversion_dollars_mdollars": 2,
        "unit_conversion_mmbtu_ej": 1,
        "total_gas_extracted": 1,
        "estimated_gas_price_with_tax": 1,
        "estimated_gas_price": 1,
        "estimated_coal_price_with_tax": 1,
        "estimated_coal_price": 1,
        "coal_extraction_in_mt": 1,
        "unit_conversion_mdollarmt_dollart": 1,
    },
)
def tax_revenue_from_hydrocarbons():
    """
    Tax Revenue from hydrocarbon Tax. The tax revenue is collected by the countries that are extracting these materials. It is a policy variable. The idea is with increasing prices for resource extraction by imposing a tax the demand for the taxed resources will decrease
    """
    value = xr.DataArray(
        np.nan,
        {"HYDROCARBONS_W_I": _subscript_dict["HYDROCARBONS_W_I"]},
        ["HYDROCARBONS_W_I"],
    )
    value.loc[["Oil_W"]] = (
        extraction_of_oil()
        * (float(estimated_oil_price_with_tax().loc["Oil_W"]) - estimated_oil_price())
    ) / unit_conversion_dollars_mdollars()
    value.loc[["Gas_W"]] = (
        unit_conversion_mmbtu_ej()
        * total_gas_extracted()
        * (float(estimated_gas_price_with_tax().loc["Gas_W"]) - estimated_gas_price())
        / unit_conversion_dollars_mdollars()
    )
    value.loc[["Coal_W"]] = (
        unit_conversion_mdollarmt_dollart()
        * coal_extraction_in_mt()
        * (
            float(estimated_coal_price_with_tax().loc["Coal_W"])
            - estimated_coal_price()
        )
    )
    return value


@component.add(
    name="tax_revenue_from_metals",
    units="Mdollars/Year",
    subscripts=["METALS_W_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "unit_conversion_mdollarmt_dollart": 4,
        "cu_market_sales": 1,
        "estimated_price_with_tax_metals": 4,
        "cu_price_economy": 1,
        "al_market_sales": 1,
        "al_price_economy": 1,
        "fe_price_economy": 1,
        "fe_market_sales": 1,
        "ni_price_economy": 1,
        "ni_market_sales": 1,
    },
)
def tax_revenue_from_metals():
    """
    Tax Revenue from metals/ resources Tax. The tax revenue is collected by the countries that are extracting these materials. It is a policy variable. The idea is with increasing prices for resource extraction by imposing a tax the demand for the taxed resources will decrease
    """
    value = xr.DataArray(
        np.nan, {"METALS_W_I": _subscript_dict["METALS_W_I"]}, ["METALS_W_I"]
    )
    value.loc[["Cu_W"]] = (
        unit_conversion_mdollarmt_dollart()
        * cu_market_sales()
        * (float(estimated_price_with_tax_metals().loc["Cu_W"]) - cu_price_economy())
    )
    value.loc[["Al_W"]] = (
        unit_conversion_mdollarmt_dollart()
        * al_market_sales()
        * (float(estimated_price_with_tax_metals().loc["Al_W"]) - al_price_economy())
    )
    value.loc[["Fe_W"]] = (
        unit_conversion_mdollarmt_dollart()
        * fe_market_sales()
        * (float(estimated_price_with_tax_metals().loc["Fe_W"]) - fe_price_economy())
    )
    value.loc[["Ni_W"]] = (
        unit_conversion_mdollarmt_dollart()
        * ni_market_sales()
        * (float(estimated_price_with_tax_metals().loc["Ni_W"]) - ni_price_economy())
    )
    return value


@component.add(
    name="taxes_on_resources",
    units="Mdollars/Year",
    subscripts=["MATERIALS_W_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"tax_revenue_from_hydrocarbons": 3, "tax_revenue_from_metals": 4},
)
def taxes_on_resources():
    """
    Tax Revenue from Resource Tax. The tax revenue is collected by the countries that are extracting these materials. It is a policy variable. The idea is with increasing prices for resource extraction by imposing a tax the demand for the taxed resources will decrease.
    """
    value = xr.DataArray(
        np.nan, {"MATERIALS_W_I": _subscript_dict["MATERIALS_W_I"]}, ["MATERIALS_W_I"]
    )
    value.loc[["Oil_W"]] = float(tax_revenue_from_hydrocarbons().loc["Oil_W"])
    value.loc[["Gas_W"]] = float(tax_revenue_from_hydrocarbons().loc["Gas_W"])
    value.loc[["Coal_W"]] = float(tax_revenue_from_hydrocarbons().loc["Coal_W"])
    value.loc[["Cu_W"]] = float(tax_revenue_from_metals().loc["Cu_W"])
    value.loc[["Al_W"]] = float(tax_revenue_from_metals().loc["Al_W"])
    value.loc[["Fe_W"]] = float(tax_revenue_from_metals().loc["Fe_W"])
    value.loc[["Ni_W"]] = float(tax_revenue_from_metals().loc["Ni_W"])
    return value


@component.add(
    name="total_coal_available",
    units="EJ/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_coal_production_capacity_ej": 2},
)
def total_coal_available():
    """
    Total amount of coal that could potaintially be mined per year in EJ.
    """
    return float(total_coal_production_capacity_ej().loc["HARD_COAL"]) + float(
        total_coal_production_capacity_ej().loc["BROWN_COAL"]
    )


@component.add(
    name="total_coal_mined",
    units="EJ/Year",
    subscripts=["COAL_TYPES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"extraction_of_coal": 2},
)
def total_coal_mined():
    """
    Sum of HARD and BROWN COAL mined per Year in EJ per Year
    """
    value = xr.DataArray(
        np.nan, {"COAL_TYPES_I": _subscript_dict["COAL_TYPES_I"]}, ["COAL_TYPES_I"]
    )
    value.loc[["HARD_COAL"]] = float(extraction_of_coal().loc["HARD_COAL"])
    value.loc[["BROWN_COAL"]] = float(extraction_of_coal().loc["BROWN_COAL"])
    return value


@component.add(
    name="total_coal_production_capacity",
    units="Mt/Year",
    subscripts=["COAL_TYPES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"number_of_operating_coal_mines": 2, "average_coal_mining_capacity": 2},
)
def total_coal_production_capacity():
    """
    Total mining capacity of HARD COAL AND BRWON COAL in Mt per year.
    """
    value = xr.DataArray(
        np.nan, {"COAL_TYPES_I": _subscript_dict["COAL_TYPES_I"]}, ["COAL_TYPES_I"]
    )
    value.loc[["HARD_COAL"]] = float(
        number_of_operating_coal_mines().loc["HARD_COAL"]
    ) * float(average_coal_mining_capacity().loc["HARD_COAL"])
    value.loc[["BROWN_COAL"]] = float(
        number_of_operating_coal_mines().loc["BROWN_COAL"]
    ) * float(average_coal_mining_capacity().loc["BROWN_COAL"])
    return value


@component.add(
    name="total_coal_production_capacity_EJ",
    units="EJ/Year",
    subscripts=["COAL_TYPES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_coal_production_capacity": 2, "unit_conversion_mt_ej": 2},
)
def total_coal_production_capacity_ej():
    """
    Total Production capacity in EJ/year separated into HARD COAL and BROWN COAL
    """
    value = xr.DataArray(
        np.nan, {"COAL_TYPES_I": _subscript_dict["COAL_TYPES_I"]}, ["COAL_TYPES_I"]
    )
    value.loc[["HARD_COAL"]] = float(
        total_coal_production_capacity().loc["HARD_COAL"]
    ) / float(unit_conversion_mt_ej().loc["HARD_COAL"])
    value.loc[["BROWN_COAL"]] = float(
        total_coal_production_capacity().loc["BROWN_COAL"]
    ) / float(unit_conversion_mt_ej().loc["BROWN_COAL"])
    return value


@component.add(
    name="total_coal_remaining_resources",
    units="EJ",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"coal_resources": 1},
)
def total_coal_remaining_resources():
    """
    Remaining coal resources. Sum of coal in resources. Hard and Brown coal.
    """
    return sum(
        coal_resources().rename({"COAL_TYPES_I": "COAL_TYPES_I!"}),
        dim=["COAL_TYPES_I!"],
    )


@component.add(
    name="total_coal_reserves",
    units="EJ",
    subscripts=["COAL_TYPES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"coal_reserves": 1},
)
def total_coal_reserves():
    """
    Sum of coal in reserves. Hard and Brown coal.
    """
    return xr.DataArray(
        sum(
            coal_reserves().rename({"COAL_TYPES_I": "COAL_TYPES_I!"}),
            dim=["COAL_TYPES_I!"],
        ),
        {"COAL_TYPES_I": _subscript_dict["COAL_TYPES_I"]},
        ["COAL_TYPES_I"],
    )


@component.add(
    name="total_gas_extracted",
    units="EJ/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"extraction_of_gas": 1},
)
def total_gas_extracted():
    """
    Flow to track the stock of cummulative gas extraction
    """
    return extraction_of_gas()


@component.add(
    name="total_oil_extracted",
    units="bbl/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"extraction_of_oil": 1},
)
def total_oil_extracted():
    """
    Flow to track the stock of cummulative oil extraction.
    """
    return extraction_of_oil()


@component.add(
    name="total_production_capacity_of_coal",
    units="EJ/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_coal_production_capacity_ej": 2},
)
def total_production_capacity_of_coal():
    """
    Total production capacity of Hard coal and brown coal together in EJ/year.
    """
    return float(total_coal_production_capacity_ej().loc["HARD_COAL"]) + float(
        total_coal_production_capacity_ej().loc["BROWN_COAL"]
    )


@component.add(
    name="UNIT_CONVERSION_dollars_$",
    units="dollars/$",
    comp_type="Constant",
    comp_subtype="Normal",
)
def unit_conversion_dollars_():
    """
    Unit conversion
    """
    return 1


@component.add(
    name="UNIT_CONVERSION_MdollarMt_dollart",
    units="(Mdollars/Mt)/($/t)",
    comp_type="Constant",
    comp_subtype="Normal",
)
def unit_conversion_mdollarmt_dollart():
    """
    Unit conversion-
    """
    return 1


@component.add(
    name="UNIT_CONVERSION_MMBTU_EJ",
    units="million_Btu/EJ",
    comp_type="Constant",
    comp_subtype="Normal",
)
def unit_conversion_mmbtu_ej():
    """
    Unit Conversion from EJ to MMBTU
    """
    return 9.48 * 10**8


@component.add(
    name="UNIT_CONVERSION_Mt_EJ",
    units="Mt/EJ",
    subscripts=["COAL_TYPES_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_unit_conversion_mt_ej"},
)
def unit_conversion_mt_ej():
    """
    Conversion factor Mt to EJ of hard coal and brown coal based on the Source: Global Energy Assessment-Toward a Sustainable Future (Rogner et al., 2012) Conversion factor is calculated by looking and the reported extraction volume in Mt and the reported values of extracted coal in EJ.
    """
    return _ext_constant_unit_conversion_mt_ej()


_ext_constant_unit_conversion_mt_ej = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Hydrocarbons",
    "UNIT_CONVERSION_Mt_EJ*",
    {"COAL_TYPES_I": _subscript_dict["COAL_TYPES_I"]},
    _root,
    {"COAL_TYPES_I": _subscript_dict["COAL_TYPES_I"]},
    "_ext_constant_unit_conversion_mt_ej",
)


@component.add(
    name="URR_COAL_INT",
    units="EJ",
    subscripts=["COAL_TYPES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "initial_coal_cumulatively_extracted_2005": 2,
        "initial_coal_reserves": 2,
        "initial_coal_hidden_2005": 2,
    },
)
def urr_coal_int():
    value = xr.DataArray(
        np.nan, {"COAL_TYPES_I": _subscript_dict["COAL_TYPES_I"]}, ["COAL_TYPES_I"]
    )
    value.loc[["HARD_COAL"]] = (
        float(initial_coal_cumulatively_extracted_2005().loc["HARD_COAL"])
        + float(initial_coal_reserves().loc["HARD_COAL"])
        + float(initial_coal_hidden_2005().loc["HARD_COAL"])
    )
    value.loc[["BROWN_COAL"]] = (
        float(initial_coal_hidden_2005().loc["BROWN_COAL"])
        + float(initial_coal_reserves().loc["BROWN_COAL"])
        + float(initial_coal_cumulatively_extracted_2005().loc["BROWN_COAL"])
    )
    return value


@component.add(
    name="URR_NATURAL_GAS",
    units="EJ",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "initial_total_gas_extracted": 1,
        "initial_gas_resource": 1,
        "initial_gas_reserves": 1,
    },
)
def urr_natural_gas():
    """
    According to estimates based on - SOURCE: Bundesanstalt für Geowissenschaften und Rohstoffe (BGR), 2017. Energy Study: Data and Developments Concerning German and Global Energy Supplies , conventional and unconventional Gas resources are available for discovery.Recalculated into EJ. Source: BGR 2017-Bundesanstalt für Geowissenschaften und Rohstoffe (BGR), 2017. Energy Study: Data and Developments Concerning German and Global Energy Supplies BP stat. review report 2022 There should be a separation between conventional and unconventional Gas in a later approach.
    """
    return (
        initial_total_gas_extracted() + initial_gas_resource() + initial_gas_reserves()
    )


@component.add(
    name="URR_Oil",
    units="bbl",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "initial_oil_cumulatively_extracted_2005": 1,
        "initial_oil_reserves_2005": 1,
        "initial_oil_resources": 1,
    },
)
def urr_oil():
    """
    THe URR is deepending on the users choice of estimated oil resources the reserves and the cumulatively extracted. According to estimates based on - SOURCE, conventional and unconventional oil resources are available for discovery.Recalculated into bbl. Source: Meta-analysis of non-renewable energy resource estimates Author:MichaelDale https://doi.org/10.1016/j.enpol.2011.12.039 Projection of world fossil fuels by country Author: S.H.Mohr https://doi.org/10.1016/j.fuel.2014.10.030 There should be a separation between conventional and unconventional Oil in a later approach.
    """
    return (
        initial_oil_cumulatively_extracted_2005()
        + initial_oil_reserves_2005()
        + initial_oil_resources()
    )


@component.add(
    name="world_PE_coal_EJ",
    units="EJ/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"world_pe_by_commodity": 1},
)
def world_pe_coal_ej():
    """
    Global (primary energy) demand of Coal. Coming from the energy transformation view. Link between materials, energy and economy.
    """
    return float(world_pe_by_commodity().loc["PE_coal"])


@component.add(
    name="world_PE_gas_EJ",
    units="EJ/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"world_pe_by_commodity": 1},
)
def world_pe_gas_ej():
    """
    Global (primary energy) demand of natural gas. Coming from the energy transformation view. Link between materials, energy and economy.
    """
    return float(world_pe_by_commodity().loc["PE_natural_gas"])


@component.add(
    name="world_PE_oil_bbl",
    units="bbl/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"world_pe_by_commodity": 1, "oil_bbl_per_ej": 1},
)
def world_pe_oil_bbl():
    """
    Oil demand from the Energy model converted into bbl/year- Global (primary energy) demand of Oil. Coming from the energy transformation view. Link between materials, energy and economy.
    """
    return float(world_pe_by_commodity().loc["PE_oil"]) * oil_bbl_per_ej()
