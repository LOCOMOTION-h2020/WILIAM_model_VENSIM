"""
Module economy.households_consumption
Translated using PySD version 3.10.0
"""


@component.add(
    name="adjustment_factor_households_consumption_to_avoid_negative_assets",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "delayed_ts_households_net_lending": 1,
        "delayed_ts_households_financial_assets": 1,
        "initial_households_financial_assets_per_household": 1,
        "delayed_ts_households_disposable_income": 1,
        "delayed_ts_total_households_consumption_coicop": 1,
    },
)
def adjustment_factor_households_consumption_to_avoid_negative_assets():
    """
    Correction factor of consumption to avoid negative fiancnial assets. When financial assets are lower than 0.5 initial assets we downscale the consumption to be equal to disposable income
    """
    return if_then_else(
        np.logical_and(
            time() > 2015,
            np.logical_and(
                delayed_ts_households_net_lending() < 0,
                delayed_ts_households_financial_assets()
                < 0.5 * initial_households_financial_assets_per_household(),
            ),
        ),
        lambda: zidz(
            delayed_ts_households_disposable_income(),
            delayed_ts_total_households_consumption_coicop(),
        ),
        lambda: xr.DataArray(
            1,
            {
                "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
            },
            ["REGIONS_35_I", "HOUSEHOLDS_I"],
        ),
    )


@component.add(
    name="adjustment_factor_labour_compensation",
    units="DMNL",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "delayed_ts_labour_compensation_total": 1,
        "labour_compensation_non_adjusted": 1,
    },
)
def adjustment_factor_labour_compensation():
    """
    Adjustment factor for labour compensation
    """
    return zidz(
        delayed_ts_labour_compensation_total(), labour_compensation_non_adjusted()
    )


@component.add(
    name="adjustment_factor_net_operating_surplus",
    units="DMNL",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "delayed_ts_net_operating_surplus_total": 1,
        "tax_income_corporations": 1,
        "net_operationg_surplus_non_adjusted": 1,
    },
)
def adjustment_factor_net_operating_surplus():
    return zidz(
        delayed_ts_net_operating_surplus_total() - tax_income_corporations(),
        net_operationg_surplus_non_adjusted(),
    )


@component.add(
    name="adjustment_factor_social_benefits",
    units="DMNL",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"social_benefits": 1, "social_benefits_non_adjusted": 1},
)
def adjustment_factor_social_benefits():
    """
    Adjustment factor for social benefits
    """
    return zidz(social_benefits(), social_benefits_non_adjusted())


@component.add(
    name="BASE_CONSUMPTION_COICOP",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I", "COICOP_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_base_consumption_coicop"},
)
def base_consumption_coicop():
    return _ext_constant_base_consumption_coicop()


_ext_constant_base_consumption_coicop = ExtConstant(
    "model_parameters/economy/Consumption_ENDOGENOUS.xlsx",
    "Consumption_COICOP",
    "BASE_CONSUMPTION_COICOP",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "COICOP_I": _subscript_dict["COICOP_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "COICOP_I": _subscript_dict["COICOP_I"],
    },
    "_ext_constant_base_consumption_coicop",
)


@component.add(
    name="BASE_HOUSEHOLDS_WEALTH_TAX",
    units="$/Year",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_base_households_wealth_tax"},
)
def base_households_wealth_tax():
    """
    Households wealth taxes by household type
    """
    return _ext_constant_base_households_wealth_tax()


_ext_constant_base_households_wealth_tax = ExtConstant(
    "model_parameters/economy/Consumption_ENDOGENOUS.xlsx",
    "HH_wealth_tax",
    "BASE_HOUSEHOLDS_WEALTH_TAX",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
    "_ext_constant_base_households_wealth_tax",
)


@component.add(
    name="BETA_TRANSPORT",
    units="DMNL",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_beta_transport"},
)
def beta_transport():
    """
    Beta parameter of transport demand equation
    """
    return _ext_constant_beta_transport()


_ext_constant_beta_transport = ExtConstant(
    "model_parameters/economy/Consumption_ECONOMETRIC.xlsx",
    "Beta_hh_transport_1",
    "BETA_HH_TRANSPORT",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
    "_ext_constant_beta_transport",
)


@component.add(
    name="check_households_consumption_transport_and_buildings_energy",
    units="$/Year",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"households_consumption_transport_and_buildings_energy": 1},
)
def check_households_consumption_transport_and_buildings_energy():
    return sum(
        households_consumption_transport_and_buildings_energy().rename(
            {"COICOP_TRANSP_ENERGY_I": "COICOP_TRANSP_ENERGY_I!"}
        ),
        dim=["COICOP_TRANSP_ENERGY_I!"],
    )


@component.add(
    name="CONSTANT_AIR",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_constant_air"},
)
def constant_air():
    return _ext_constant_constant_air()


_ext_constant_constant_air = ExtConstant(
    "model_parameters/economy/Consumption_ECONOMETRIC.xlsx",
    "Const_Air",
    "CONST_AIR",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
    "_ext_constant_constant_air",
)


@component.add(
    name="CONSTANT_ELECTRICITY",
    units="DMNL",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_constant_electricity"},
)
def constant_electricity():
    return _ext_constant_constant_electricity()


_ext_constant_constant_electricity = ExtConstant(
    "model_parameters/economy/Consumption_ECONOMETRIC.xlsx",
    "Const_Electricity",
    "CONST_ELECTRICITY",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
    "_ext_constant_constant_electricity",
)


@component.add(
    name="CONSTANT_FUEL_TRANSP",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_constant_fuel_transp"},
)
def constant_fuel_transp():
    return _ext_constant_constant_fuel_transp()


_ext_constant_constant_fuel_transp = ExtConstant(
    "model_parameters/economy/Consumption_ECONOMETRIC.xlsx",
    "Const_Fuel_transp",
    "CONST_FUEL_TRANSP",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
    "_ext_constant_constant_fuel_transp",
)


@component.add(
    name="CONSTANT_GAS",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_constant_gas"},
)
def constant_gas():
    return _ext_constant_constant_gas()


_ext_constant_constant_gas = ExtConstant(
    "model_parameters/economy/Consumption_ECONOMETRIC.xlsx",
    "Const_Gas",
    "CONST_GAS",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
    "_ext_constant_constant_gas",
)


@component.add(
    name="CONSTANT_HEAT",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_constant_heat"},
)
def constant_heat():
    return _ext_constant_constant_heat()


_ext_constant_constant_heat = ExtConstant(
    "model_parameters/economy/Consumption_ECONOMETRIC.xlsx",
    "Const_Heat",
    "CONST_HEAT",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
    "_ext_constant_constant_heat",
)


@component.add(
    name="CONSTANT_LIQUIDS",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_constant_liquids"},
)
def constant_liquids():
    return _ext_constant_constant_liquids()


_ext_constant_constant_liquids = ExtConstant(
    "model_parameters/economy/Consumption_ECONOMETRIC.xlsx",
    "Const_Liquids",
    "CONST_LIQUIDS",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
    "_ext_constant_constant_liquids",
)


@component.add(
    name="CONSTANT_RAIL",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_constant_rail"},
)
def constant_rail():
    return _ext_constant_constant_rail()


_ext_constant_constant_rail = ExtConstant(
    "model_parameters/economy/Consumption_ECONOMETRIC.xlsx",
    "Const_Rail",
    "CONST_RAIL",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
    "_ext_constant_constant_rail",
)


@component.add(
    name="CONSTANT_ROAD",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_constant_road"},
)
def constant_road():
    return _ext_constant_constant_road()


_ext_constant_constant_road = ExtConstant(
    "model_parameters/economy/Consumption_ECONOMETRIC.xlsx",
    "Const_Road",
    "CONST_ROAD",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
    "_ext_constant_constant_road",
)


@component.add(
    name="CONSTANT_SEA",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_constant_sea"},
)
def constant_sea():
    return _ext_constant_constant_sea()


_ext_constant_constant_sea = ExtConstant(
    "model_parameters/economy/Consumption_ECONOMETRIC.xlsx",
    "Const_Sea",
    "CONST_SEA",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
    "_ext_constant_constant_sea",
)


@component.add(
    name="CONSTANT_SOLID",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_constant_solid"},
)
def constant_solid():
    return _ext_constant_constant_solid()


_ext_constant_constant_solid = ExtConstant(
    "model_parameters/economy/Consumption_ECONOMETRIC.xlsx",
    "Const_Solid",
    "CONST_SOLID",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
    "_ext_constant_constant_solid",
)


@component.add(
    name="CONSTANT_TRANSPORT",
    units="DMNL",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_constant_transport"},
)
def constant_transport():
    """
    Constant parameter of transport demand equation
    """
    return _ext_constant_constant_transport()


_ext_constant_constant_transport = ExtConstant(
    "model_parameters/economy/Consumption_ECONOMETRIC.xlsx",
    "Constant_hh_transport",
    "CONSTANT_HH_TRANSPORT",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
    "_ext_constant_constant_transport",
)


@component.add(
    name="CONSTANT_TRANSPORT_ENERGY",
    units="DMNL",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I", "COICOP_TRANSP_ENERGY_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "constant_electricity": 1,
        "constant_air": 1,
        "constant_fuel_transp": 1,
        "constant_gas": 1,
        "constant_heat": 1,
        "constant_liquids": 1,
        "constant_rail": 1,
        "constant_road": 1,
        "constant_sea": 1,
        "constant_solid": 1,
    },
)
def constant_transport_energy():
    """
    Constant econometric euqations for households demand of energy and transportation
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
            "COICOP_TRANSP_ENERGY_I": _subscript_dict["COICOP_TRANSP_ENERGY_I"],
        },
        ["REGIONS_35_I", "HOUSEHOLDS_I", "COICOP_TRANSP_ENERGY_I"],
    )
    value.loc[:, :, ["HH_ELECTRICITY"]] = (
        constant_electricity()
        .expand_dims({"COICOP_ENERGY_BUILDINGS_I": ["HH_ELECTRICITY"]}, 2)
        .values
    )
    value.loc[:, :, ["HH_AIR"]] = (
        constant_air().expand_dims({"COICOP_I": ["HH_AIR"]}, 2).values
    )
    value.loc[:, :, ["HH_FUEL_TRANSPORT"]] = (
        constant_fuel_transp()
        .expand_dims({"COICOP_ENERGY_I": ["HH_FUEL_TRANSPORT"]}, 2)
        .values
    )
    value.loc[:, :, ["HH_GAS"]] = (
        constant_gas().expand_dims({"COICOP_ENERGY_BUILDINGS_I": ["HH_GAS"]}, 2).values
    )
    value.loc[:, :, ["HH_HEAT"]] = (
        constant_heat()
        .expand_dims({"COICOP_ENERGY_BUILDINGS_I": ["HH_HEAT"]}, 2)
        .values
    )
    value.loc[:, :, ["HH_LIQUID_FUELS"]] = (
        constant_liquids()
        .expand_dims({"COICOP_ENERGY_BUILDINGS_I": ["HH_LIQUID_FUELS"]}, 2)
        .values
    )
    value.loc[:, :, ["HH_RAILWAY"]] = (
        constant_rail().expand_dims({"COICOP_I": ["HH_RAILWAY"]}, 2).values
    )
    value.loc[:, :, ["HH_ROAD"]] = (
        constant_road().expand_dims({"COICOP_I": ["HH_ROAD"]}, 2).values
    )
    value.loc[:, :, ["HH_MARITIME"]] = (
        constant_sea().expand_dims({"COICOP_I": ["HH_MARITIME"]}, 2).values
    )
    value.loc[:, :, ["HH_SOLID_FUELS"]] = (
        constant_solid()
        .expand_dims({"COICOP_ENERGY_BUILDINGS_I": ["HH_SOLID_FUELS"]}, 2)
        .values
    )
    return value


@component.add(
    name="consumer_price_index",
    units="DMNL",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"price_coicop": 1, "consumption_coicop": 2},
)
def consumer_price_index():
    """
    Consumer price index.
    """
    return zidz(
        sum(
            price_coicop().rename({"COICOP_I": "COICOP_I!"})
            * consumption_coicop().rename({"COICOP_I": "COICOP_I!"}),
            dim=["COICOP_I!"],
        ),
        sum(
            consumption_coicop().rename({"COICOP_I": "COICOP_MAP_I!"}),
            dim=["COICOP_MAP_I!"],
        ),
    )


@component.add(
    name="consumption_COICOP",
    units="Mdollars",
    subscripts=["REGIONS_35_I", "COICOP_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "unit_conversion_dollars_mdollars": 2,
        "households_consumption_coicop": 2,
        "base_number_of_households": 1,
        "number_of_households_by_income_and_type": 1,
    },
)
def consumption_coicop():
    """
    Consumption by category (COICOP classification)
    """
    return if_then_else(
        time() <= 2015,
        lambda: sum(
            households_consumption_coicop().rename({"HOUSEHOLDS_I": "HOUSEHOLDS_I!"})
            * base_number_of_households().rename({"HOUSEHOLDS_I": "HOUSEHOLDS_I!"})
            / unit_conversion_dollars_mdollars(),
            dim=["HOUSEHOLDS_I!"],
        ),
        lambda: sum(
            households_consumption_coicop().rename({"HOUSEHOLDS_I": "HOUSEHOLDS_I!"})
            * number_of_households_by_income_and_type().rename(
                {"HOUSEHOLDS_I": "HOUSEHOLDS_I!"}
            )
            / unit_conversion_dollars_mdollars(),
            dim=["HOUSEHOLDS_I!"],
        ),
    )


@component.add(
    name="consumption_COICOP_real",
    units="Mdollars_2015",
    subscripts=["REGIONS_35_I", "COICOP_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"consumption_coicop": 1, "price_transformation": 1, "price_coicop": 1},
)
def consumption_coicop_real():
    """
    ZIDZ(consumption_COICOP[REGIONS_35_I,COICOP_I]* BASE_PRICE_COICOP[REGIONS_35_I,COICOP_I],price_COICOP[REGIONS_35_I,COICOP_I ])
    """
    return zidz(consumption_coicop() * price_transformation(), price_coicop())


@component.add(
    name="delayed_number_of_households",
    units="DMNL/Year",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_number_of_households": 1},
    other_deps={
        "_delayfixed_delayed_number_of_households": {
            "initial": {"base_number_of_households": 1, "time_step": 1},
            "step": {"number_of_households_by_income_and_type": 1},
        }
    },
)
def delayed_number_of_households():
    """
    Delayed number of housholds
    """
    return _delayfixed_delayed_number_of_households()


_delayfixed_delayed_number_of_households = DelayFixed(
    lambda: number_of_households_by_income_and_type(),
    lambda: time_step(),
    lambda: base_number_of_households(),
    time_step,
    "_delayfixed_delayed_number_of_households",
)


@component.add(
    name="delayed_TS_consumer_price_index",
    units="DMNL",
    subscripts=["REGIONS_35_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_consumer_price_index": 1},
    other_deps={
        "_delayfixed_delayed_ts_consumer_price_index": {
            "initial": {"initial_delayed_consumer_price_index": 1, "time_step": 1},
            "step": {"consumer_price_index": 1},
        }
    },
)
def delayed_ts_consumer_price_index():
    """
    Delayed (time step) consumer price index.
    """
    return _delayfixed_delayed_ts_consumer_price_index()


_delayfixed_delayed_ts_consumer_price_index = DelayFixed(
    lambda: consumer_price_index(),
    lambda: time_step(),
    lambda: initial_delayed_consumer_price_index(),
    time_step,
    "_delayfixed_delayed_ts_consumer_price_index",
)


@component.add(
    name="delayed_TS_households_consumption_COICOP",
    units="$/Year",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I", "COICOP_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_households_consumption_coicop": 1},
    other_deps={
        "_delayfixed_delayed_ts_households_consumption_coicop": {
            "initial": {"initial_households_consumption_coicop": 1, "time_step": 1},
            "step": {"households_consumption_coicop": 1},
        }
    },
)
def delayed_ts_households_consumption_coicop():
    """
    Delayes housholds consumption in COICOP classification
    """
    return _delayfixed_delayed_ts_households_consumption_coicop()


_delayfixed_delayed_ts_households_consumption_coicop = DelayFixed(
    lambda: households_consumption_coicop(),
    lambda: time_step(),
    lambda: initial_households_consumption_coicop(),
    time_step,
    "_delayfixed_delayed_ts_households_consumption_coicop",
)


@component.add(
    name="delayed_TS_households_disposable_income",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_households_disposable_income": 1},
    other_deps={
        "_delayfixed_delayed_ts_households_disposable_income": {
            "initial": {"initial_households_disposable_income": 1, "time_step": 1},
            "step": {"households_disposable_income": 1},
        }
    },
)
def delayed_ts_households_disposable_income():
    """
    Delayed disposable income
    """
    return _delayfixed_delayed_ts_households_disposable_income()


_delayfixed_delayed_ts_households_disposable_income = DelayFixed(
    lambda: households_disposable_income(),
    lambda: time_step(),
    lambda: initial_households_disposable_income(),
    time_step,
    "_delayfixed_delayed_ts_households_disposable_income",
)


@component.add(
    name="delayed_TS_households_net_wealth_by_type_of_household",
    units="$/Year",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_households_net_wealth_by_type_of_household": 1},
    other_deps={
        "_delayfixed_delayed_ts_households_net_wealth_by_type_of_household": {
            "initial": {
                "households_net_wealth_by_type_of_household": 1,
                "time_step": 1,
            },
            "step": {"time": 1, "households_net_wealth_by_type_of_household": 2},
        }
    },
)
def delayed_ts_households_net_wealth_by_type_of_household():
    """
    Delayed households net wealth by household type
    """
    return _delayfixed_delayed_ts_households_net_wealth_by_type_of_household()


_delayfixed_delayed_ts_households_net_wealth_by_type_of_household = DelayFixed(
    lambda: if_then_else(
        time() <= 2015,
        lambda: households_net_wealth_by_type_of_household(),
        lambda: households_net_wealth_by_type_of_household(),
    ),
    lambda: time_step(),
    lambda: households_net_wealth_by_type_of_household(),
    time_step,
    "_delayfixed_delayed_ts_households_net_wealth_by_type_of_household",
)


@component.add(
    name="delayed_TS_households_share_quaids",
    units="DMNL",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I", "QUAIDS_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_households_share_quaids": 1},
    other_deps={
        "_delayfixed_delayed_ts_households_share_quaids": {
            "initial": {"initial_delayed_households_share_quaids": 1, "time_step": 1},
            "step": {
                "time": 1,
                "initial_delayed_households_share_quaids": 1,
                "households_share_quaids": 1,
            },
        }
    },
)
def delayed_ts_households_share_quaids():
    """
    Delayed households share quaids.
    """
    return _delayfixed_delayed_ts_households_share_quaids()


_delayfixed_delayed_ts_households_share_quaids = DelayFixed(
    lambda: if_then_else(
        time() <= 2015,
        lambda: initial_delayed_households_share_quaids(),
        lambda: households_share_quaids(),
    ),
    lambda: time_step(),
    lambda: initial_delayed_households_share_quaids(),
    time_step,
    "_delayfixed_delayed_ts_households_share_quaids",
)


@component.add(
    name="delayed_TS_labour_compensation_per_household",
    units="$/Year",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_labour_compensation_per_household": 1},
    other_deps={
        "_delayfixed_delayed_ts_labour_compensation_per_household": {
            "initial": {"initial_households_labour_compensation": 1, "time_step": 1},
            "step": {
                "time": 1,
                "initial_households_labour_compensation": 1,
                "households_gross_labour_income": 1,
            },
        }
    },
)
def delayed_ts_labour_compensation_per_household():
    """
    Delayed labour compensation
    """
    return _delayfixed_delayed_ts_labour_compensation_per_household()


_delayfixed_delayed_ts_labour_compensation_per_household = DelayFixed(
    lambda: if_then_else(
        time() <= 2015,
        lambda: initial_households_labour_compensation(),
        lambda: households_gross_labour_income(),
    ),
    lambda: time_step(),
    lambda: initial_households_labour_compensation(),
    time_step,
    "_delayfixed_delayed_ts_labour_compensation_per_household",
)


@component.add(
    name="delayed_TS_net_operating_surplus_per_hh",
    units="$/Year",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_net_operating_surplus_per_hh": 1},
    other_deps={
        "_delayfixed_delayed_ts_net_operating_surplus_per_hh": {
            "initial": {"initial_households_net_operating_surplus": 1, "time_step": 1},
            "step": {
                "time": 1,
                "initial_households_net_operating_surplus": 1,
                "households_net_operating_surplus": 1,
            },
        }
    },
)
def delayed_ts_net_operating_surplus_per_hh():
    """
    Delayed
    """
    return _delayfixed_delayed_ts_net_operating_surplus_per_hh()


_delayfixed_delayed_ts_net_operating_surplus_per_hh = DelayFixed(
    lambda: if_then_else(
        time() <= 2015,
        lambda: initial_households_net_operating_surplus(),
        lambda: households_net_operating_surplus(),
    ),
    lambda: time_step(),
    lambda: initial_households_net_operating_surplus(),
    time_step,
    "_delayfixed_delayed_ts_net_operating_surplus_per_hh",
)


@component.add(
    name="delayed_TS_shares_consumption_non_durables",
    units="DMNL",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I", "COICOP_NON_DURABLES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"delayed_ts_households_consumption_coicop": 2},
)
def delayed_ts_shares_consumption_non_durables():
    """
    Delayesd shares of non durable consumption
    """
    return zidz(
        delayed_ts_households_consumption_coicop()
        .loc[:, :, _subscript_dict["COICOP_NON_DURABLES_I"]]
        .rename({"COICOP_I": "COICOP_NON_DURABLES_I"}),
        sum(
            delayed_ts_households_consumption_coicop()
            .loc[:, :, _subscript_dict["COICOP_NON_DURABLES_MAP_I"]]
            .rename({"COICOP_I": "COICOP_NON_DURABLES_MAP_I!"}),
            dim=["COICOP_NON_DURABLES_MAP_I!"],
        ).expand_dims(
            {"COICOP_NON_DURABLES_I": _subscript_dict["COICOP_NON_DURABLES_I"]}, 2
        ),
    )


@component.add(
    name="delayed_TS_shares_consumption_transportation",
    units="DMNL",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I", "COICOP_TRANSPORT_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"delayed_ts_households_consumption_coicop": 2},
)
def delayed_ts_shares_consumption_transportation():
    """
    Delayed shares of consumption of transportation
    """
    return zidz(
        delayed_ts_households_consumption_coicop()
        .loc[:, :, _subscript_dict["COICOP_TRANSPORT_I"]]
        .rename({"COICOP_I": "COICOP_TRANSPORT_I"}),
        sum(
            delayed_ts_households_consumption_coicop()
            .loc[:, :, _subscript_dict["COICOP_TRANSPORT_I"]]
            .rename({"COICOP_I": "COICOP_TRANSPORT_I!"}),
            dim=["COICOP_TRANSPORT_I!"],
        ).expand_dims({"COICOP_TRANSPORT_I": _subscript_dict["COICOP_TRANSPORT_I"]}, 2),
    )


@component.add(
    name="delayed_TS_social_benefits_per_household",
    units="$/Year",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_social_benefits_per_household": 1},
    other_deps={
        "_delayfixed_delayed_ts_social_benefits_per_household": {
            "initial": {"initial_households_social_benefits": 1, "time_step": 1},
            "step": {
                "time": 1,
                "initial_households_social_benefits": 1,
                "households_social_benefits": 1,
            },
        }
    },
)
def delayed_ts_social_benefits_per_household():
    """
    Delayed social benefits per household
    """
    return _delayfixed_delayed_ts_social_benefits_per_household()


_delayfixed_delayed_ts_social_benefits_per_household = DelayFixed(
    lambda: if_then_else(
        time() <= 2015,
        lambda: initial_households_social_benefits(),
        lambda: households_social_benefits(),
    ),
    lambda: time_step(),
    lambda: initial_households_social_benefits(),
    time_step,
    "_delayfixed_delayed_ts_social_benefits_per_household",
)


@component.add(
    name="delayed_TS_taxable_income",
    units="$/Year",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_taxable_income": 1},
    other_deps={
        "_delayfixed_delayed_ts_taxable_income": {
            "initial": {"taxable_income": 1, "time_step": 1},
            "step": {"time": 1, "taxable_income": 2},
        }
    },
)
def delayed_ts_taxable_income():
    """
    Delayed taxable income.
    """
    return _delayfixed_delayed_ts_taxable_income()


_delayfixed_delayed_ts_taxable_income = DelayFixed(
    lambda: if_then_else(
        time() <= 2015, lambda: taxable_income(), lambda: taxable_income()
    ),
    lambda: time_step(),
    lambda: taxable_income(),
    time_step,
    "_delayfixed_delayed_ts_taxable_income",
)


@component.add(
    name="delayed_TS_total_households_consumption_COICOP",
    units="$/Year",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_total_households_consumption_coicop": 1},
    other_deps={
        "_delayfixed_delayed_ts_total_households_consumption_coicop": {
            "initial": {"time_step": 1},
            "step": {"total_households_consumption_coicop": 1},
        }
    },
)
def delayed_ts_total_households_consumption_coicop():
    """
    Delayes housholds consumption in COICOP classification
    """
    return _delayfixed_delayed_ts_total_households_consumption_coicop()


_delayfixed_delayed_ts_total_households_consumption_coicop = DelayFixed(
    lambda: total_households_consumption_coicop(),
    lambda: time_step(),
    lambda: xr.DataArray(
        0,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
        },
        ["REGIONS_35_I", "HOUSEHOLDS_I"],
    ),
    time_step,
    "_delayfixed_delayed_ts_total_households_consumption_coicop",
)


@component.add(
    name="desired_transport_demand",
    units="km*person",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "transport_demand_by_household_type": 1,
        "number_of_households_by_income_and_type": 1,
    },
)
def desired_transport_demand():
    """
    Desired transport demand
    """
    return (
        transport_demand_by_household_type() * number_of_households_by_income_and_type()
    )


@component.add(
    name="disposable_income",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "households_disposable_income": 1,
        "number_of_households_by_income_and_type": 1,
        "unit_conversion_dollars_mdollars": 1,
    },
)
def disposable_income():
    return sum(
        households_disposable_income().rename({"HOUSEHOLDS_I": "HOUSEHOLDS_I!"})
        * number_of_households_by_income_and_type().rename(
            {"HOUSEHOLDS_I": "HOUSEHOLDS_I!"}
        )
        / unit_conversion_dollars_mdollars(),
        dim=["HOUSEHOLDS_I!"],
    )


@component.add(
    name="disposable_income_real",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "households_disposable_income_real": 1,
        "number_of_households_by_income_and_type": 1,
        "unit_conversion_dollars_mdollars": 1,
    },
)
def disposable_income_real():
    """
    Disposable income real
    """
    return sum(
        households_disposable_income_real().rename({"HOUSEHOLDS_I": "HOUSEHOLDS_I!"})
        * number_of_households_by_income_and_type().rename(
            {"HOUSEHOLDS_I": "HOUSEHOLDS_I!"}
        )
        / unit_conversion_dollars_mdollars(),
        dim=["HOUSEHOLDS_I!"],
    )


@component.add(
    name="energy_consumption_buildings_and_transport_top_down",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I", "COICOP_ENERGY_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"consumption_coicop_real": 1},
)
def energy_consumption_buildings_and_transport_top_down():
    """
    Energy consumption in buldings and private transportaion calculated top-down in the economic model
    """
    return (
        consumption_coicop_real()
        .loc[:, _subscript_dict["COICOP_ENERGY_I"]]
        .rename({"COICOP_I": "COICOP_ENERGY_I"})
    )


@component.add(
    name="energy_consumption_private_transport_COICOP_physical_units",
    units="EJ/Year",
    subscripts=["REGIONS_36_I", "HOUSEHOLDS_I", "COICOP_ENERGY_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={"energy_consumption_private_passenger_transport_by_mode": 6},
)
def energy_consumption_private_transport_coicop_physical_units():
    """
    Energy consumption for private trasnport in COICOP classsification, physical units
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_36_I": _subscript_dict["REGIONS_36_I"],
            "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
            "COICOP_ENERGY_I": _subscript_dict["COICOP_ENERGY_I"],
        },
        ["REGIONS_36_I", "HOUSEHOLDS_I", "COICOP_ENERGY_I"],
    )
    value.loc[_subscript_dict["REGIONS_35_I"], :, ["HH_GAS"]] = (
        sum(
            energy_consumption_private_passenger_transport_by_mode()
            .loc[:, "FE_gas", :, :]
            .reset_coords(drop=True)
            .rename({"PRIVATE_TRANSPORT_I": "PRIVATE_TRANSPORT_I!"}),
            dim=["PRIVATE_TRANSPORT_I!"],
        )
        .expand_dims({"COICOP_ENERGY_BUILDINGS_I": ["HH_GAS"]}, 2)
        .values
    )
    value.loc[_subscript_dict["REGIONS_35_I"], :, ["HH_HEAT"]] = (
        sum(
            energy_consumption_private_passenger_transport_by_mode()
            .loc[:, "FE_heat", :, :]
            .reset_coords(drop=True)
            .rename({"PRIVATE_TRANSPORT_I": "PRIVATE_TRANSPORT_I!"}),
            dim=["PRIVATE_TRANSPORT_I!"],
        )
        .expand_dims({"COICOP_ENERGY_BUILDINGS_I": ["HH_HEAT"]}, 2)
        .values
    )
    value.loc[_subscript_dict["REGIONS_35_I"], :, ["HH_SOLID_FUELS"]] = (
        (
            sum(
                energy_consumption_private_passenger_transport_by_mode()
                .loc[:, "FE_solid_bio", :, :]
                .reset_coords(drop=True)
                .rename({"PRIVATE_TRANSPORT_I": "PRIVATE_TRANSPORT_I!"}),
                dim=["PRIVATE_TRANSPORT_I!"],
            )
            + sum(
                energy_consumption_private_passenger_transport_by_mode()
                .loc[:, "FE_solid_fossil", :, :]
                .reset_coords(drop=True)
                .rename({"PRIVATE_TRANSPORT_I": "PRIVATE_TRANSPORT_I!"}),
                dim=["PRIVATE_TRANSPORT_I!"],
            )
        )
        .expand_dims({"COICOP_ENERGY_BUILDINGS_I": ["HH_SOLID_FUELS"]}, 2)
        .values
    )
    value.loc[_subscript_dict["REGIONS_35_I"], :, ["HH_FUEL_TRANSPORT"]] = (
        sum(
            energy_consumption_private_passenger_transport_by_mode()
            .loc[:, "FE_liquid", :, :]
            .reset_coords(drop=True)
            .rename({"PRIVATE_TRANSPORT_I": "PRIVATE_TRANSPORT_I!"}),
            dim=["PRIVATE_TRANSPORT_I!"],
        )
        .expand_dims({"COICOP_ENERGY_I": ["HH_FUEL_TRANSPORT"]}, 2)
        .values
    )
    value.loc[:, :, ["HH_LIQUID_FUELS"]] = 0
    value.loc[_subscript_dict["REGIONS_35_I"], :, ["HH_ELECTRICITY"]] = (
        sum(
            energy_consumption_private_passenger_transport_by_mode()
            .loc[:, "FE_elec", :, :]
            .reset_coords(drop=True)
            .rename({"PRIVATE_TRANSPORT_I": "PRIVATE_TRANSPORT_I!"}),
            dim=["PRIVATE_TRANSPORT_I!"],
        )
        .expand_dims({"COICOP_ENERGY_BUILDINGS_I": ["HH_ELECTRICITY"]}, 2)
        .values
    )
    return value


@component.add(
    name="EPSILON_TRANSPORT",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_epsilon_transport"},
)
def epsilon_transport():
    """
    Epsilon parameter of transport demand equation
    """
    return _ext_constant_epsilon_transport()


_ext_constant_epsilon_transport = ExtConstant(
    "model_parameters/economy/Consumption_ECONOMETRIC.xlsx",
    "Beta_hh_transport_2",
    "EPSILON_HH_TRANSPORT",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
    "_ext_constant_epsilon_transport",
)


@component.add(
    name="FINAL_ENERGY_CONSUMPTION_HOUSEHOLDS_COICOP",
    units="TJ/Year",
    subscripts=["REGIONS_35_I", "COICOP_ENERGY_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "base_final_energy_consumption_households_by_fe_buildings": 6,
        "base_final_energy_consumption_households_by_fe_transport": 1,
    },
)
def final_energy_consumption_households_coicop():
    """
    Housholds final energy consumption (in physical units) by COICOP categoty
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "COICOP_ENERGY_I": _subscript_dict["COICOP_ENERGY_I"],
        },
        ["REGIONS_35_I", "COICOP_ENERGY_I"],
    )
    value.loc[:, ["HH_ELECTRICITY"]] = (
        base_final_energy_consumption_households_by_fe_buildings()
        .loc[:, "FE_elec"]
        .reset_coords(drop=True)
        .expand_dims({"COICOP_ENERGY_BUILDINGS_I": ["HH_ELECTRICITY"]}, 1)
        .values
    )
    value.loc[:, ["HH_GAS"]] = (
        base_final_energy_consumption_households_by_fe_buildings()
        .loc[:, "FE_gas"]
        .reset_coords(drop=True)
        .expand_dims({"COICOP_ENERGY_BUILDINGS_I": ["HH_GAS"]}, 1)
        .values
    )
    value.loc[:, ["HH_HEAT"]] = (
        base_final_energy_consumption_households_by_fe_buildings()
        .loc[:, "FE_heat"]
        .reset_coords(drop=True)
        .expand_dims({"COICOP_ENERGY_BUILDINGS_I": ["HH_HEAT"]}, 1)
        .values
    )
    value.loc[:, ["HH_LIQUID_FUELS"]] = (
        base_final_energy_consumption_households_by_fe_buildings()
        .loc[:, "FE_liquid"]
        .reset_coords(drop=True)
        .expand_dims({"COICOP_ENERGY_BUILDINGS_I": ["HH_LIQUID_FUELS"]}, 1)
        .values
    )
    value.loc[:, ["HH_SOLID_FUELS"]] = (
        (
            base_final_energy_consumption_households_by_fe_buildings()
            .loc[:, "FE_solid_fossil"]
            .reset_coords(drop=True)
            + base_final_energy_consumption_households_by_fe_buildings()
            .loc[:, "FE_solid_bio"]
            .reset_coords(drop=True)
        )
        .expand_dims({"COICOP_ENERGY_BUILDINGS_I": ["HH_SOLID_FUELS"]}, 1)
        .values
    )
    value.loc[:, ["HH_FUEL_TRANSPORT"]] = (
        sum(
            base_final_energy_consumption_households_by_fe_transport().rename(
                {"NRG_FE_I": "NRG_FE_I!"}
            ),
            dim=["NRG_FE_I!"],
        )
        .expand_dims({"COICOP_ENERGY_I": ["HH_FUEL_TRANSPORT"]}, 1)
        .values
    )
    return value


@component.add(
    name="households_consumer_price_index",
    units="$/Year",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"households_consumption_shares": 1, "price_coicop": 1},
)
def households_consumer_price_index():
    """
    Households consumer price index
    """
    return sum(
        households_consumption_shares().rename({"COICOP_I": "COICOP_I!"})
        * price_coicop().rename({"COICOP_I": "COICOP_I!"}),
        dim=["COICOP_I!"],
    )


@component.add(
    name="households_consumption_COICOP",
    units="$/Year",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I", "COICOP_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "smooth_adjustment_factor_households_consumption_to_avoid_negative_assets": 1,
        "households_consumption_coicop_non_adjusted_negative_assets": 1,
        "households_consumption_shares": 1,
        "households_disposable_income": 1,
    },
)
def households_consumption_coicop():
    """
    Househodls consumption by category (durables and non-durables energy and transport) and by household type
    """
    return if_then_else(
        (
            smooth_adjustment_factor_households_consumption_to_avoid_negative_assets()
            >= 1
        ).expand_dims({"COICOP_I": _subscript_dict["COICOP_I"]}, 2),
        lambda: households_consumption_coicop_non_adjusted_negative_assets(),
        lambda: households_consumption_shares() * households_disposable_income(),
    )


@component.add(
    name="households_consumption_COICOP_non_adjusted_negative_assets",
    units="$/Year",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I", "COICOP_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "households_consumption_propensity_durables": 1,
        "households_disposable_income": 1,
        "households_consumption_transport_and_buildings_energy": 1,
        "households_consumption_coicop_quaids": 1,
    },
)
def households_consumption_coicop_non_adjusted_negative_assets():
    """
    Househodls consumption by category (durables and non-durables energy and transport) and by household type
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
            "COICOP_I": _subscript_dict["COICOP_I"],
        },
        ["REGIONS_35_I", "HOUSEHOLDS_I", "COICOP_I"],
    )
    value.loc[:, :, _subscript_dict["COICOP_DURABLES_I"]] = (
        households_consumption_propensity_durables() * households_disposable_income()
    ).values
    value.loc[
        :, :, _subscript_dict["COICOP_TRANSP_ENERGY_I"]
    ] = households_consumption_transport_and_buildings_energy().values
    value.loc[
        :, :, _subscript_dict["QUAIDS_I"]
    ] = households_consumption_coicop_quaids().values
    return value


@component.add(
    name="households_consumption_COICOP_quaids",
    units="$/Year",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I", "QUAIDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "households_share_quaids": 1,
        "households_consumption_non_durable_non_energy": 1,
    },
)
def households_consumption_coicop_quaids():
    """
    Households consumption non durable non energy by category and by household type.
    """
    return households_share_quaids() * households_consumption_non_durable_non_energy()


@component.add(
    name="households_consumption_energy_buildings_bottom_up",
    units="$/Year",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I", "COICOP_ENERGY_BUILDINGS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"initial_households_consumption_coicop": 1},
)
def households_consumption_energy_buildings_bottom_up():
    """
    Households energgy consumption in buildings by household type
    """
    return (
        initial_households_consumption_coicop()
        .loc[:, :, _subscript_dict["COICOP_ENERGY_BUILDINGS_I"]]
        .rename({"COICOP_I": "COICOP_ENERGY_BUILDINGS_I"})
    )


@component.add(
    name="households_consumption_energy_buildings_top_down",
    units="$/Year",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I", "COICOP_ENERGY_BUILDINGS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"households_consumption_transport_energy_top_down_adjusted": 1},
)
def households_consumption_energy_buildings_top_down():
    """
    Households energy consumption in buildings to down
    """
    return (
        households_consumption_transport_energy_top_down_adjusted()
        .loc[:, :, _subscript_dict["COICOP_ENERGY_BUILDINGS_I"]]
        .rename({"COICOP_TRANSP_ENERGY_I": "COICOP_ENERGY_BUILDINGS_I"})
    )


@component.add(
    name="households_consumption_energy_transport_bottom_up",
    units="$/Year",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I", "COICOP_TRANSP_ENERGY_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "households_energy_transport_consumption_coicop": 1,
        "implicit_price_energy_households_coicop": 1,
        "price_coicop": 1,
        "price_transformation": 1,
        "unit_conversion_dollars_mdollars": 1,
    },
)
def households_consumption_energy_transport_bottom_up():
    """
    Households electricity consumption for transportation
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
            "COICOP_TRANSP_ENERGY_I": _subscript_dict["COICOP_TRANSP_ENERGY_I"],
        },
        ["REGIONS_35_I", "HOUSEHOLDS_I", "COICOP_TRANSP_ENERGY_I"],
    )
    value.loc[:, :, _subscript_dict["COICOP_ENERGY_I"]] = (
        households_energy_transport_consumption_coicop()
        * implicit_price_energy_households_coicop()
        * (
            price_coicop()
            .loc[:, _subscript_dict["COICOP_ENERGY_I"]]
            .rename({"COICOP_I": "COICOP_ENERGY_I"})
            / price_transformation()
        )
        * unit_conversion_dollars_mdollars()
    ).values
    value.loc[:, :, _subscript_dict["COICOP_TRANSPORT_EXC_FUEL_I"]] = 0
    return value


@component.add(
    name="households_consumption_non_durable_non_energy",
    units="$/Year",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "households_consumption_non_durables": 2,
        "households_consumption_transport_and_buildings_energy": 2,
    },
)
def households_consumption_non_durable_non_energy():
    """
    Households total consumption non durable non energy by household type.
    """
    return if_then_else(
        households_consumption_non_durables()
        - sum(
            households_consumption_transport_and_buildings_energy().rename(
                {"COICOP_TRANSP_ENERGY_I": "COICOP_TRANSP_ENERGY_I!"}
            ),
            dim=["COICOP_TRANSP_ENERGY_I!"],
        )
        < 0,
        lambda: xr.DataArray(
            0,
            {
                "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
            },
            ["REGIONS_35_I", "HOUSEHOLDS_I"],
        ),
        lambda: households_consumption_non_durables()
        - sum(
            households_consumption_transport_and_buildings_energy().rename(
                {"COICOP_TRANSP_ENERGY_I": "COICOP_TRANSP_ENERGY_I!"}
            ),
            dim=["COICOP_TRANSP_ENERGY_I!"],
        ),
    )


@component.add(
    name="households_consumption_non_durables",
    units="$/Year",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "households_consumption_propensity_non_durables": 1,
        "households_disposable_income": 1,
    },
)
def households_consumption_non_durables():
    """
    Households consumption of non durable goods
    """
    return (
        households_consumption_propensity_non_durables()
        * households_disposable_income()
    )


@component.add(
    name="households_consumption_propensity_durables",
    units="DMNL",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I", "COICOP_DURABLES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_economy": 3,
        "switch_fin2eco": 3,
        "price_transformation": 6,
        "households_consumer_price_index": 12,
        "epsilon_housing": 2,
        "initial_households_financial_liabilities_per_household": 6,
        "initial_households_financial_assets_per_household": 18,
        "beta_housing": 2,
        "constant_parameter_housing": 2,
        "households_disposable_income": 12,
        "initial_households_capital_stock_per_household": 18,
        "households_financial_liabilities": 6,
        "households_financial_assets": 18,
        "households_capital_stock": 18,
        "epsilon_appliances": 2,
        "beta_appliances": 2,
        "constant_parameter_appliances": 2,
        "constant_parameter_vehicles": 2,
        "epsilon_vehicles": 2,
        "beta_vehicles": 2,
    },
)
def households_consumption_propensity_durables():
    """
    Households consumption propensity non durable goods EXP(CONSTANT_PARAMETER_APPLIANCES[REGIONS 35 I,HOUSEHOLDS I]+BETA_APPLIANCES[REGIONS 35 I,HOUSEHOLDS I ]*LN(ABS(households_disposable_income[REGIONS 35 I,HOUSEHOLDS I]+1e-07) )+EPSILON_APPLIANCES[REGIONS 35 I,HOUSEHOLDS I] *LN(ABS(ZIDZ((households_financial_assets[REGIONS 35 I,HOUSEHOLDS I]+households_capital_stock[REGIONS 35 I ,HOUSEHOLDS I]),(households_financial_assets[REGIONS 35 I,HOUSEHOLDS I]+households_capital_stock [REGIONS 35 I,HOUSEHOLDS I]+households_financial_liabilities[REGIONS 35 I,HOUSEHOLDS I]))*(households_financial_assets [REGIONS 35 I,HOUSEHOLDS I]+households_capital_stock[REGIONS 35 I,HOUSEHOLDS I])+1e-07)))
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
            "COICOP_DURABLES_I": _subscript_dict["COICOP_DURABLES_I"],
        },
        ["REGIONS_35_I", "HOUSEHOLDS_I", "COICOP_DURABLES_I"],
    )
    value.loc[:, :, ["HH_HOUSING"]] = (
        if_then_else(
            np.logical_or(switch_economy() == 0, switch_fin2eco() == 0),
            lambda: np.exp(
                constant_parameter_housing()
                + if_then_else(
                    np.logical_or(
                        households_disposable_income() <= 0,
                        households_consumer_price_index() <= 0,
                    ),
                    lambda: xr.DataArray(
                        0,
                        {
                            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                            "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
                        },
                        ["REGIONS_35_I", "HOUSEHOLDS_I"],
                    ),
                    lambda: beta_housing()
                    * np.log(
                        households_disposable_income()
                        / (households_consumer_price_index() / price_transformation())
                    ),
                )
                + if_then_else(
                    zidz(
                        initial_households_financial_assets_per_household()
                        + initial_households_capital_stock_per_household(),
                        initial_households_financial_assets_per_household()
                        + initial_households_capital_stock_per_household()
                        + initial_households_financial_liabilities_per_household(),
                    )
                    * (
                        initial_households_financial_assets_per_household()
                        + initial_households_capital_stock_per_household()
                    )
                    <= 0,
                    lambda: xr.DataArray(
                        0,
                        {
                            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                            "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
                        },
                        ["REGIONS_35_I", "HOUSEHOLDS_I"],
                    ),
                    lambda: epsilon_housing()
                    * np.log(
                        zidz(
                            initial_households_financial_assets_per_household()
                            + initial_households_capital_stock_per_household(),
                            initial_households_financial_assets_per_household()
                            + initial_households_capital_stock_per_household()
                            + initial_households_financial_liabilities_per_household(),
                        )
                        * (
                            initial_households_financial_assets_per_household()
                            + initial_households_capital_stock_per_household()
                        )
                    ),
                )
            ),
            lambda: np.exp(
                constant_parameter_housing()
                + if_then_else(
                    np.logical_or(
                        households_disposable_income() <= 0,
                        households_consumer_price_index() <= 0,
                    ),
                    lambda: xr.DataArray(
                        0,
                        {
                            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                            "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
                        },
                        ["REGIONS_35_I", "HOUSEHOLDS_I"],
                    ),
                    lambda: beta_housing()
                    * np.log(
                        households_disposable_income()
                        / (households_consumer_price_index() / price_transformation())
                    ),
                )
                + if_then_else(
                    zidz(
                        households_financial_assets() + households_capital_stock(),
                        households_financial_assets()
                        + households_capital_stock()
                        + households_financial_liabilities(),
                    )
                    * (households_financial_assets() + households_capital_stock())
                    <= 0,
                    lambda: xr.DataArray(
                        0,
                        {
                            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                            "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
                        },
                        ["REGIONS_35_I", "HOUSEHOLDS_I"],
                    ),
                    lambda: epsilon_housing()
                    * np.log(
                        zidz(
                            households_financial_assets() + households_capital_stock(),
                            households_financial_assets()
                            + households_capital_stock()
                            + households_financial_liabilities(),
                        )
                        * (households_financial_assets() + households_capital_stock())
                    ),
                )
            ),
        )
        .expand_dims({"COICOP_DURABLES_I": ["HH_HOUSING"]}, 2)
        .values
    )
    value.loc[:, :, ["HH_APPLIANCES"]] = (
        if_then_else(
            np.logical_or(switch_economy() == 0, switch_fin2eco() == 0),
            lambda: np.exp(
                constant_parameter_appliances()
                + if_then_else(
                    np.logical_or(
                        households_disposable_income() <= 0,
                        households_consumer_price_index() <= 0,
                    ),
                    lambda: xr.DataArray(
                        0,
                        {
                            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                            "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
                        },
                        ["REGIONS_35_I", "HOUSEHOLDS_I"],
                    ),
                    lambda: beta_appliances()
                    * np.log(
                        households_disposable_income()
                        / (households_consumer_price_index() / price_transformation())
                    ),
                )
                + if_then_else(
                    zidz(
                        initial_households_financial_assets_per_household()
                        + initial_households_capital_stock_per_household(),
                        initial_households_financial_assets_per_household()
                        + initial_households_capital_stock_per_household()
                        + initial_households_financial_liabilities_per_household(),
                    )
                    * (
                        initial_households_financial_assets_per_household()
                        + initial_households_capital_stock_per_household()
                    )
                    <= 0,
                    lambda: xr.DataArray(
                        0,
                        {
                            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                            "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
                        },
                        ["REGIONS_35_I", "HOUSEHOLDS_I"],
                    ),
                    lambda: epsilon_appliances()
                    * np.log(
                        zidz(
                            initial_households_financial_assets_per_household()
                            + initial_households_capital_stock_per_household(),
                            initial_households_financial_assets_per_household()
                            + initial_households_capital_stock_per_household()
                            + initial_households_financial_liabilities_per_household(),
                        )
                        * (
                            initial_households_financial_assets_per_household()
                            + initial_households_capital_stock_per_household()
                        )
                    ),
                )
            ),
            lambda: np.exp(
                constant_parameter_appliances()
                + if_then_else(
                    np.logical_or(
                        households_disposable_income() <= 0,
                        households_consumer_price_index() <= 0,
                    ),
                    lambda: xr.DataArray(
                        0,
                        {
                            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                            "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
                        },
                        ["REGIONS_35_I", "HOUSEHOLDS_I"],
                    ),
                    lambda: beta_appliances()
                    * np.log(
                        households_disposable_income()
                        / (households_consumer_price_index() / price_transformation())
                    ),
                )
                + if_then_else(
                    zidz(
                        households_financial_assets() + households_capital_stock(),
                        households_financial_assets()
                        + households_capital_stock()
                        + households_financial_liabilities(),
                    )
                    * (households_financial_assets() + households_capital_stock())
                    <= 0,
                    lambda: xr.DataArray(
                        0,
                        {
                            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                            "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
                        },
                        ["REGIONS_35_I", "HOUSEHOLDS_I"],
                    ),
                    lambda: epsilon_appliances()
                    * np.log(
                        zidz(
                            households_financial_assets() + households_capital_stock(),
                            households_financial_assets()
                            + households_capital_stock()
                            + households_financial_liabilities(),
                        )
                        * (households_financial_assets() + households_capital_stock())
                    ),
                )
            ),
        )
        .expand_dims({"COICOP_DURABLES_I": ["HH_APPLIANCES"]}, 2)
        .values
    )
    value.loc[:, :, ["HH_VEHICLES"]] = (
        if_then_else(
            np.logical_or(switch_economy() == 0, switch_fin2eco() == 0),
            lambda: np.exp(
                constant_parameter_vehicles()
                + if_then_else(
                    np.logical_or(
                        households_disposable_income() <= 0,
                        households_consumer_price_index() <= 0,
                    ),
                    lambda: xr.DataArray(
                        0,
                        {
                            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                            "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
                        },
                        ["REGIONS_35_I", "HOUSEHOLDS_I"],
                    ),
                    lambda: beta_vehicles()
                    * np.log(
                        households_disposable_income()
                        / (households_consumer_price_index() / price_transformation())
                    ),
                )
                + if_then_else(
                    zidz(
                        initial_households_financial_assets_per_household()
                        + initial_households_capital_stock_per_household(),
                        initial_households_financial_assets_per_household()
                        + initial_households_capital_stock_per_household()
                        + initial_households_financial_liabilities_per_household(),
                    )
                    * (
                        initial_households_financial_assets_per_household()
                        + initial_households_capital_stock_per_household()
                    )
                    <= 0,
                    lambda: xr.DataArray(
                        0,
                        {
                            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                            "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
                        },
                        ["REGIONS_35_I", "HOUSEHOLDS_I"],
                    ),
                    lambda: epsilon_vehicles()
                    * np.log(
                        zidz(
                            initial_households_financial_assets_per_household()
                            + initial_households_capital_stock_per_household(),
                            initial_households_financial_assets_per_household()
                            + initial_households_capital_stock_per_household()
                            + initial_households_financial_liabilities_per_household(),
                        )
                        * (
                            initial_households_financial_assets_per_household()
                            + initial_households_capital_stock_per_household()
                        )
                    ),
                )
            ),
            lambda: np.exp(
                constant_parameter_vehicles()
                + if_then_else(
                    np.logical_or(
                        households_disposable_income() <= 0,
                        households_consumer_price_index() <= 0,
                    ),
                    lambda: xr.DataArray(
                        0,
                        {
                            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                            "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
                        },
                        ["REGIONS_35_I", "HOUSEHOLDS_I"],
                    ),
                    lambda: beta_vehicles()
                    * np.log(
                        households_disposable_income()
                        / (households_consumer_price_index() / price_transformation())
                    ),
                )
                + if_then_else(
                    zidz(
                        households_financial_assets() + households_capital_stock(),
                        households_financial_assets()
                        + households_capital_stock()
                        + households_financial_liabilities(),
                    )
                    * (households_financial_assets() + households_capital_stock())
                    <= 0,
                    lambda: xr.DataArray(
                        0,
                        {
                            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                            "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
                        },
                        ["REGIONS_35_I", "HOUSEHOLDS_I"],
                    ),
                    lambda: epsilon_vehicles()
                    * np.log(
                        zidz(
                            households_financial_assets() + households_capital_stock(),
                            households_financial_assets()
                            + households_capital_stock()
                            + households_financial_liabilities(),
                        )
                        * (households_financial_assets() + households_capital_stock())
                    ),
                )
            ),
        )
        .expand_dims({"COICOP_DURABLES_I": ["HH_VEHICLES"]}, 2)
        .values
    )
    return value


@component.add(
    name="households_consumption_propensity_non_durables",
    units="DMNL",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_economy": 1,
        "switch_fin2eco": 1,
        "price_transformation": 2,
        "constant_parameter_non_durables": 2,
        "households_consumer_price_index": 4,
        "epsilon_non_durables": 2,
        "initial_households_financial_liabilities_per_household": 2,
        "initial_households_financial_assets_per_household": 6,
        "households_disposable_income": 4,
        "initial_households_capital_stock_per_household": 6,
        "beta_non_durables": 2,
        "households_financial_liabilities": 2,
        "households_financial_assets": 6,
        "households_capital_stock": 6,
    },
)
def households_consumption_propensity_non_durables():
    """
    Households consumption propensity for non durable goods IF_THEN_ELSE(SWITCH_ECONOMY=0,EXP( CONSTANT_PARAMETER_NON_DURABLES[REGIONS 35 I,HOUSEHOLDS I] +IF_THEN_ELSE(households_disposable_income[REGIONS 35 I,HOUSEHOLDS I]<=0 :OR: households_consumer_price_index[REGIONS 35 I ,HOUSEHOLDS I]<=0,0, BETA_NON_DURABLES[REGIONS 35 I,HOUSEHOLDS I]*LN(households_disposable_income[REGIONS 35 I,HOUSEHOLDS I]/(households_consumer_price_index [REGIONS 35 I,HOUSEHOLDS I]/PRICE_TRANSFORMATION) )) +IF_THEN_ELSE( (ZIDZ(initial_households_financial_assets_per_household[REGIONS 35 I,HOUSEHOLDS I]+initial_households_capital_stock_per_household[REGIONS 35 I,HOUSEHOLDS I]),(initial_households_financial_assets_per_household[REGIONS 35 I,HOUSEHOLDS I]+initial_households_capital_stock_per_household[REGIONS 35 I,HOUSEHOLDS I]+initial_households_financial_liabilities_per_household[REGIONS 35 I,HOUSEHOLDS I])))*(initial_households_financial_assets_per_household[REGIONS 35 I,HOUSEHOLDS I]+initial_households_capital_stock_per_household[REGIONS 35 I,HOUSEHOLDS I])<=0,0, EPSILON_NON_DURABLES[REGIONS 35 I,HOUSEHOLDS I] *LN((ZIDZ(initial_households_financial_assets_per_household[REGIONS 35 I,HOUSEHOLDS I]+initial_households_capital_stock_per_household[REGIONS 35 I,HOUSEHOLDS I]),(initial_households_financial_assets_per_household[REGIONS 35 I,HOUSEHOLDS I]+initial_households_capital_stock_per_household[REGIONS 35 I,HOUSEHOLDS I]+initial_households_financial_liabilities_per_household[REGIONS 35 I,HOUSEHOLDS I])))*(initial_households_financial_assets_per_household[REGIONS 35 I,HOUSEHOLDS I]+initial_households_capital_stock_per_household[REGIONS 35 I,HOUSEHOLDS I]))), EXP(CONSTANT_PARAMETER_NON_DURABLES[REGIONS 35 I,HOUSEHOLDS I] +IF_THEN_ELSE(households_disposable_income[REGIONS 35 I,HOUSEHOLDS I]<=0 :OR: households_consumer_price_index[REGIONS 35 I ,HOUSEHOLDS I]<=0,0, BETA_NON_DURABLES[REGIONS 35 I,HOUSEHOLDS I]*LN(households_disposable_income[REGIONS 35 I,HOUSEHOLDS I]/(households_consumer_price_index [REGIONS 35 I,HOUSEHOLDS I]/PRICE_TRANSFORMATION) )) +IF_THEN_ELSE( (ZIDZ(initial_households_financial_assets_per_household[REGIONS 35 I,HOUSEHOLDS I]+initial_households_capital_stock_per_household[REGIONS 35 I,HOUSEHOLDS I]),(initial_households_financial_assets_per_household[REGIONS 35 I,HOUSEHOLDS I]+initial_households_capital_stock_per_household[REGIONS 35 I,HOUSEHOLDS I]+initial_households_financial_liabilities_per_household[REGIONS 35 I,HOUSEHOLDS I])))*(initial_households_financial_assets_per_household[REGIONS 35 I,HOUSEHOLDS I]+initial_households_capital_stock_per_household[REGIONS 35 I,HOUSEHOLDS I])<=0,0, EPSILON_NON_DURABLES[REGIONS 35 I,HOUSEHOLDS I] *LN((ZIDZ(initial_households_financial_assets_per_household[REGIONS 35 I,HOUSEHOLDS I]+initial_households_capital_stock_per_household[REGIONS 35 I,HOUSEHOLDS I]),(initial_households_financial_assets_per_household[REGIONS 35 I,HOUSEHOLDS I]+initial_households_capital_stock_per_household[REGIONS 35 I,HOUSEHOLDS I]+initial_households_financial_liabilities_per_household[REGIONS 35 I,HOUSEHOLDS I])))*(initial_households_financial_assets_per_household[REGIONS 35 I,HOUSEHOLDS I]+initial_households_capital_stock_per_household[REGIONS 35 I,HOUSEHOLDS I])))))
    """
    return if_then_else(
        np.logical_or(switch_economy() == 0, switch_fin2eco() == 0),
        lambda: np.exp(
            constant_parameter_non_durables()
            + if_then_else(
                np.logical_or(
                    households_disposable_income() <= 0,
                    households_consumer_price_index() <= 0,
                ),
                lambda: xr.DataArray(
                    0,
                    {
                        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
                    },
                    ["REGIONS_35_I", "HOUSEHOLDS_I"],
                ),
                lambda: beta_non_durables()
                * np.log(
                    households_disposable_income()
                    / (households_consumer_price_index() / price_transformation())
                ),
            )
            + if_then_else(
                zidz(
                    initial_households_financial_assets_per_household()
                    + initial_households_capital_stock_per_household(),
                    initial_households_financial_assets_per_household()
                    + initial_households_capital_stock_per_household()
                    + initial_households_financial_liabilities_per_household(),
                )
                * (
                    initial_households_financial_assets_per_household()
                    + initial_households_capital_stock_per_household()
                )
                <= 0,
                lambda: xr.DataArray(
                    0,
                    {
                        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
                    },
                    ["REGIONS_35_I", "HOUSEHOLDS_I"],
                ),
                lambda: epsilon_non_durables()
                * np.log(
                    zidz(
                        initial_households_financial_assets_per_household()
                        + initial_households_capital_stock_per_household(),
                        initial_households_financial_assets_per_household()
                        + initial_households_capital_stock_per_household()
                        + initial_households_financial_liabilities_per_household(),
                    )
                    * (
                        initial_households_financial_assets_per_household()
                        + initial_households_capital_stock_per_household()
                    )
                ),
            )
        ),
        lambda: np.exp(
            constant_parameter_non_durables()
            + if_then_else(
                np.logical_or(
                    households_disposable_income() <= 0,
                    households_consumer_price_index() <= 0,
                ),
                lambda: xr.DataArray(
                    0,
                    {
                        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
                    },
                    ["REGIONS_35_I", "HOUSEHOLDS_I"],
                ),
                lambda: beta_non_durables()
                * np.log(
                    households_disposable_income()
                    / (households_consumer_price_index() / price_transformation())
                ),
            )
            + if_then_else(
                zidz(
                    households_financial_assets() + households_capital_stock(),
                    households_financial_assets()
                    + households_capital_stock()
                    + households_financial_liabilities(),
                )
                * (households_financial_assets() + households_capital_stock())
                <= 0,
                lambda: xr.DataArray(
                    0,
                    {
                        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
                    },
                    ["REGIONS_35_I", "HOUSEHOLDS_I"],
                ),
                lambda: epsilon_non_durables()
                * np.log(
                    zidz(
                        households_financial_assets() + households_capital_stock(),
                        households_financial_assets()
                        + households_capital_stock()
                        + households_financial_liabilities(),
                    )
                    * (households_financial_assets() + households_capital_stock())
                ),
            )
        ),
    )


@component.add(
    name="households_consumption_public_transport_bottom_up",
    units="$/Year",
    subscripts=["REGIONS_36_I", "HOUSEHOLDS_I", "COICOP_TRANSP_ENERGY_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "public_households_transport_demand_coicop": 1,
        "implicit_price_public_transport_households": 1,
        "price_coicop": 1,
        "price_transformation": 1,
    },
)
def households_consumption_public_transport_bottom_up():
    """
    Households consumption of public transport calculated bottom-up
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_36_I": _subscript_dict["REGIONS_36_I"],
            "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
            "COICOP_TRANSP_ENERGY_I": _subscript_dict["COICOP_TRANSP_ENERGY_I"],
        },
        ["REGIONS_36_I", "HOUSEHOLDS_I", "COICOP_TRANSP_ENERGY_I"],
    )
    value.loc[
        _subscript_dict["REGIONS_35_I"],
        :,
        _subscript_dict["COICOP_TRANSPORT_EXC_FUEL_I"],
    ] = (
        public_households_transport_demand_coicop()
        * implicit_price_public_transport_households()
        * (
            price_coicop()
            .loc[:, _subscript_dict["COICOP_TRANSPORT_EXC_FUEL_I"]]
            .rename({"COICOP_I": "COICOP_TRANSPORT_EXC_FUEL_I"})
            / price_transformation()
        )
    ).values
    value.loc[:, :, _subscript_dict["COICOP_ENERGY_I"]] = 0
    return value


@component.add(
    name="households_consumption_purchaser_prices",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"consumption_structure_coicop": 1, "consumption_coicop": 1},
)
def households_consumption_purchaser_prices():
    """
    Households consumption in purchaser prices and nominal terms.
    """
    return sum(
        consumption_structure_coicop().rename({"COICOP_I": "COICOP_I!"})
        * consumption_coicop().rename({"COICOP_I": "COICOP_I!"}),
        dim=["COICOP_I!"],
    )


@component.add(
    name="households_consumption_shares",
    units="DMNL",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I", "COICOP_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"delayed_ts_households_consumption_coicop": 2},
)
def households_consumption_shares():
    """
    Households consumption shares
    """
    return zidz(
        delayed_ts_households_consumption_coicop(),
        sum(
            delayed_ts_households_consumption_coicop().rename(
                {"COICOP_I": "COICOP_MAP_I!"}
            ),
            dim=["COICOP_MAP_I!"],
        ).expand_dims({"COICOP_I": _subscript_dict["COICOP_I"]}, 2),
    )


@component.add(
    name="households_consumption_transport_and_buildings_energy",
    units="$/Year",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I", "COICOP_TRANSP_ENERGY_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_hh_buildings_energy_bottom_up": 1,
        "switch_economy": 4,
        "time": 4,
        "households_consumption_energy_buildings_top_down": 1,
        "households_consumption_energy_buildings_bottom_up": 1,
        "switch_eco_hh_transport_energy_bottom_up": 3,
        "households_consumption_transport_bottom_up": 4,
        "households_consumption_transport_top_down": 2,
    },
)
def households_consumption_transport_and_buildings_energy():
    """
    Households consumption of energy: buildings and transport (passengers). *---------------------------------- equation buildings => includes electricidy and gas consumption for transportaion IF_THEN_ELSE(SWITCH_ENERGY_BUILDINGS_BOTTOM_UP=0,households_consumption_energy_buildi ngs_top_down[REGIONS_35_I,HOUSEHOLDS_I ,COICOP_ENERGY_BUILDINGS_I],households_consumption_energy_buildings_bottom_up [REGIONS_35_I,HOUSEHOLDS_I,COICOP_ENERGY_BUILDINGS_I]) +IF_THEN_ELSE(SWITCH_TRANSPORT_HH_BOTTOM_UP=0,0,households_consumption_transport_bott om_up[REGIONS_35_I,HOUSEHOLDS_I,COICOP_ENERGY_BUILDINGS_I ]) *--------------------------------- eqaution transport IF_THEN_ELSE(SWITCH_TRANSPORT_HH_BOTTOM_UP=0,households_consumption_transport_top_dow n[REGIONS_35_I,HOUSEHOLDS_I,COICOP_TRANSPORT_I],households_consumption_tran sport_bottom_up[REGIONS_35_I,HOUSEHOLDS_I,COICOP_TRANSPORT_I]) *------------------------------------ Except fpor martiime transportaion. Wehn bottom up is equal to zero we take top down estiamtion
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
            "COICOP_TRANSP_ENERGY_I": _subscript_dict["COICOP_TRANSP_ENERGY_I"],
        },
        ["REGIONS_35_I", "HOUSEHOLDS_I", "COICOP_TRANSP_ENERGY_I"],
    )
    value.loc[:, :, _subscript_dict["COICOP_ENERGY_BUILDINGS_I"]] = (
        if_then_else(
            np.logical_or(
                switch_eco_hh_buildings_energy_bottom_up() == 0,
                np.logical_or(switch_economy() == 0, time() <= 2015),
            ),
            lambda: households_consumption_energy_buildings_top_down(),
            lambda: households_consumption_energy_buildings_bottom_up(),
        )
        + if_then_else(
            np.logical_or(
                switch_eco_hh_transport_energy_bottom_up() == 0,
                np.logical_or(switch_economy() == 0, time() <= 2015),
            ),
            lambda: xr.DataArray(
                0,
                {
                    "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                    "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
                    "COICOP_ENERGY_BUILDINGS_I": _subscript_dict[
                        "COICOP_ENERGY_BUILDINGS_I"
                    ],
                },
                ["REGIONS_35_I", "HOUSEHOLDS_I", "COICOP_ENERGY_BUILDINGS_I"],
            ),
            lambda: households_consumption_transport_bottom_up()
            .loc[:, :, _subscript_dict["COICOP_ENERGY_BUILDINGS_I"]]
            .rename({"COICOP_TRANSP_ENERGY_I": "COICOP_ENERGY_BUILDINGS_I"}),
        )
    ).values
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[:, :, _subscript_dict["COICOP_TRANSPORT_I"]] = True
    except_subs.loc[:, :, ["HH_MARITIME"]] = False
    value.values[except_subs.values] = if_then_else(
        np.logical_or(
            switch_eco_hh_transport_energy_bottom_up() == 0,
            np.logical_or(switch_economy() == 0, time() <= 2015),
        ),
        lambda: households_consumption_transport_top_down(),
        lambda: households_consumption_transport_bottom_up()
        .loc[:, :, _subscript_dict["COICOP_TRANSPORT_I"]]
        .rename({"COICOP_TRANSP_ENERGY_I": "COICOP_TRANSPORT_I"}),
    ).values[except_subs.loc[:, :, _subscript_dict["COICOP_TRANSPORT_I"]].values]
    value.loc[:, :, ["HH_MARITIME"]] = (
        if_then_else(
            np.logical_or(
                switch_eco_hh_transport_energy_bottom_up() == 0,
                np.logical_or(
                    switch_economy() == 0,
                    np.logical_or(
                        time() <= 2015,
                        households_consumption_transport_bottom_up()
                        .loc[:, :, "HH_MARITIME"]
                        .reset_coords(drop=True)
                        == 0,
                    ),
                ),
            ),
            lambda: households_consumption_transport_top_down()
            .loc[:, :, "HH_MARITIME"]
            .reset_coords(drop=True),
            lambda: households_consumption_transport_bottom_up()
            .loc[:, :, "HH_MARITIME"]
            .reset_coords(drop=True),
        )
        .expand_dims({"COICOP_I": ["HH_MARITIME"]}, 2)
        .values
    )
    return value


@component.add(
    name="households_consumption_transport_bottom_up",
    units="$/Year",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I", "COICOP_TRANSP_ENERGY_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "households_consumption_energy_transport_bottom_up": 1,
        "households_consumption_public_transport_bottom_up": 1,
    },
)
def households_consumption_transport_bottom_up():
    """
    housholds consumption of transportaion (public and fuel) by household type
    """
    return (
        households_consumption_energy_transport_bottom_up()
        + households_consumption_public_transport_bottom_up()
        .loc[_subscript_dict["REGIONS_35_I"], :, :]
        .rename({"REGIONS_36_I": "REGIONS_35_I"})
    )


@component.add(
    name="households_consumption_transport_energy_top_down",
    units="$/Year",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I", "COICOP_TRANSP_ENERGY_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "households_disposable_income": 2,
        "price_coicop": 2,
        "price_transformation": 2,
        "constant_transport_energy": 1,
        "transport_and_energy_elasticities": 2,
    },
)
def households_consumption_transport_energy_top_down():
    return if_then_else(
        np.logical_or(
            (households_disposable_income() == 0),
            (
                zidz(
                    price_coicop()
                    .loc[:, _subscript_dict["COICOP_TRANSP_ENERGY_I"]]
                    .rename({"COICOP_I": "COICOP_TRANSP_ENERGY_I"}),
                    price_transformation(),
                )
                == 0
            ),
        ),
        lambda: xr.DataArray(
            0,
            {
                "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
                "COICOP_TRANSP_ENERGY_I": _subscript_dict["COICOP_TRANSP_ENERGY_I"],
            },
            ["REGIONS_35_I", "HOUSEHOLDS_I", "COICOP_TRANSP_ENERGY_I"],
        ),
        lambda: np.exp(
            constant_transport_energy()
            + (
                transport_and_energy_elasticities()
                .loc[:, "INCOME_ELASTICITY"]
                .reset_coords(drop=True)
                * np.log(households_disposable_income())
            ).transpose("REGIONS_35_I", "HOUSEHOLDS_I", "COICOP_TRANSP_ENERGY_I")
            + (
                transport_and_energy_elasticities()
                .loc[:, "PRICE_ELASTICITY"]
                .reset_coords(drop=True)
                * np.log(
                    zidz(
                        price_coicop()
                        .loc[:, _subscript_dict["COICOP_TRANSP_ENERGY_I"]]
                        .rename({"COICOP_I": "COICOP_TRANSP_ENERGY_I"}),
                        price_transformation(),
                    )
                ).transpose("COICOP_TRANSP_ENERGY_I", "REGIONS_35_I")
            ).transpose("REGIONS_35_I", "COICOP_TRANSP_ENERGY_I")
        ),
    )


@component.add(
    name="households_consumption_transport_energy_top_down_adjusted",
    units="$/Year",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I", "COICOP_TRANSP_ENERGY_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "households_consumption_transport_energy_top_down": 2,
        "households_consumption_transport_energy_top_down_adjustment_factor": 1,
    },
)
def households_consumption_transport_energy_top_down_adjusted():
    """
    households_consumption_transport_energy_top_down[REGIONS_35_I,HOUSEHOLDS_I, COICOP_TRANSP_ENERGY_I]*households_consumption_transport_energy_top_down_ad justment_factor[REGIONS_35_I,HOUSEHOLDS_I]
    """
    return if_then_else(
        time() <= 2015,
        lambda: households_consumption_transport_energy_top_down(),
        lambda: households_consumption_transport_energy_top_down()
        * households_consumption_transport_energy_top_down_adjustment_factor(),
    )


@component.add(
    name="households_consumption_transport_energy_top_down_adjustment_factor",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Stateful",
    comp_subtype="Smooth",
    depends_on={
        "_smooth_households_consumption_transport_energy_top_down_adjustment_factor": 1
    },
    other_deps={
        "_smooth_households_consumption_transport_energy_top_down_adjustment_factor": {
            "initial": {
                "switch_limit_consumption_energy_over_total_non_durables_sp": 1,
                "ratio_household_consumpion_transport_energy_to_total_non_durables": 2,
                "limit_consumption_energy_over_total_non_durables_sp": 2,
            },
            "step": {
                "switch_limit_consumption_energy_over_total_non_durables_sp": 1,
                "ratio_household_consumpion_transport_energy_to_total_non_durables": 2,
                "limit_consumption_energy_over_total_non_durables_sp": 2,
            },
        }
    },
)
def households_consumption_transport_energy_top_down_adjustment_factor():
    """
    Adjustment factor for consumption of energy and transportation. Total consumption of energy and transportation is restricted to be lower than x% of total consumption of non durables.
    """
    return _smooth_households_consumption_transport_energy_top_down_adjustment_factor()


_smooth_households_consumption_transport_energy_top_down_adjustment_factor = Smooth(
    lambda: if_then_else(
        np.logical_and(
            switch_limit_consumption_energy_over_total_non_durables_sp() == 1,
            ratio_household_consumpion_transport_energy_to_total_non_durables()
            > limit_consumption_energy_over_total_non_durables_sp(),
        ),
        lambda: zidz(
            xr.DataArray(
                limit_consumption_energy_over_total_non_durables_sp(),
                {
                    "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                    "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
                },
                ["REGIONS_35_I", "HOUSEHOLDS_I"],
            ),
            ratio_household_consumpion_transport_energy_to_total_non_durables(),
        ),
        lambda: xr.DataArray(
            1,
            {
                "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
            },
            ["REGIONS_35_I", "HOUSEHOLDS_I"],
        ),
    ),
    lambda: xr.DataArray(
        2,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
        },
        ["REGIONS_35_I", "HOUSEHOLDS_I"],
    ),
    lambda: if_then_else(
        np.logical_and(
            switch_limit_consumption_energy_over_total_non_durables_sp() == 1,
            ratio_household_consumpion_transport_energy_to_total_non_durables()
            > limit_consumption_energy_over_total_non_durables_sp(),
        ),
        lambda: zidz(
            xr.DataArray(
                limit_consumption_energy_over_total_non_durables_sp(),
                {
                    "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                    "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
                },
                ["REGIONS_35_I", "HOUSEHOLDS_I"],
            ),
            ratio_household_consumpion_transport_energy_to_total_non_durables(),
        ),
        lambda: xr.DataArray(
            1,
            {
                "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
            },
            ["REGIONS_35_I", "HOUSEHOLDS_I"],
        ),
    ),
    lambda: 1,
    "_smooth_households_consumption_transport_energy_top_down_adjustment_factor",
)


@component.add(
    name="households_consumption_transport_top_down",
    units="$/Year",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I", "COICOP_TRANSPORT_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_lockdown_effect_on_transport_sp": 1,
        "time": 1,
        "lockdown_shock_reduction_demand_transport_sp": 1,
        "households_consumption_transport_energy_top_down_adjusted": 2,
    },
)
def households_consumption_transport_top_down():
    """
    Households transport consumption top down
    """
    return if_then_else(
        np.logical_and(switch_lockdown_effect_on_transport_sp() == 1, time() == 2030),
        lambda: (1 - lockdown_shock_reduction_demand_transport_sp())
        * households_consumption_transport_energy_top_down_adjusted()
        .loc[:, :, _subscript_dict["COICOP_TRANSPORT_I"]]
        .rename({"COICOP_TRANSP_ENERGY_I": "COICOP_TRANSPORT_I"}),
        lambda: households_consumption_transport_energy_top_down_adjusted()
        .loc[:, :, _subscript_dict["COICOP_TRANSPORT_I"]]
        .rename({"COICOP_TRANSP_ENERGY_I": "COICOP_TRANSPORT_I"}),
    )


@component.add(
    name="households_disposable_income",
    units="$/Year",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_economy": 1,
        "switch_fin2eco": 1,
        "time": 1,
        "base_households_wealth_tax": 1,
        "initial_households_property_income_received": 1,
        "households_other_transfers_received": 2,
        "households_net_labour_income": 2,
        "households_other_transfers_paid": 2,
        "household_basic_income": 2,
        "households_income_tax": 2,
        "households_social_benefits": 2,
        "initial_households_property_income_paid": 1,
        "households_net_operating_surplus": 2,
        "households_property_income_paid": 1,
        "households_wealth_tax": 1,
        "households_property_income_received": 1,
    },
)
def households_disposable_income():
    """
    Households disposable income by household type.
    """
    return if_then_else(
        np.logical_or(
            switch_economy() == 0, np.logical_or(switch_fin2eco() == 0, time() <= 2015)
        ),
        lambda: households_net_labour_income()
        + initial_households_property_income_received()
        + households_net_operating_surplus()
        - initial_households_property_income_paid()
        + households_social_benefits()
        + households_other_transfers_received()
        - households_other_transfers_paid()
        - households_income_tax()
        - base_households_wealth_tax()
        + household_basic_income(),
        lambda: np.maximum(
            0,
            households_net_labour_income()
            + households_property_income_received()
            + households_net_operating_surplus()
            - households_property_income_paid()
            + households_social_benefits()
            + households_other_transfers_received()
            - households_other_transfers_paid()
            - households_income_tax()
            - households_wealth_tax()
            + household_basic_income(),
        ),
    )


@component.add(
    name="households_disposable_income_real",
    units="dollars_2015/Year",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "households_disposable_income": 1,
        "price_transformation": 1,
        "households_consumer_price_index": 1,
    },
)
def households_disposable_income_real():
    """
    Households disposable income in real terms
    """
    return zidz(
        households_disposable_income(),
        households_consumer_price_index() / price_transformation(),
    )


@component.add(
    name="households_energy_transport_consumption_COICOP",
    units="TJ/Year",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I", "COICOP_ENERGY_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "energy_consumption_private_transport_coicop_physical_units": 1,
        "number_of_households_by_income_and_type": 1,
        "unit_conversion_tj_ej": 1,
    },
)
def households_energy_transport_consumption_coicop():
    """
    Household energy consumption for transportation by housholed type in physicla untis
    """
    return (
        zidz(
            energy_consumption_private_transport_coicop_physical_units()
            .loc[_subscript_dict["REGIONS_35_I"], :, :]
            .rename({"REGIONS_36_I": "REGIONS_35_I"}),
            number_of_households_by_income_and_type().expand_dims(
                {"COICOP_ENERGY_I": _subscript_dict["COICOP_ENERGY_I"]}, 2
            ),
        )
        * unit_conversion_tj_ej()
    )


@component.add(
    name="households_gross_labour_income",
    units="$/Year",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_households": 1,
        "time": 1,
        "initial_households_labour_compensation": 1,
        "delayed_ts_labour_compensation_per_household": 1,
        "adjustment_factor_labour_compensation": 1,
    },
)
def households_gross_labour_income():
    """
    Gross labour income by household type
    """
    return if_then_else(
        np.logical_or(switch_eco_households() == 0, time() <= 2015),
        lambda: initial_households_labour_compensation(),
        lambda: adjustment_factor_labour_compensation()
        * delayed_ts_labour_compensation_per_household(),
    )


@component.add(
    name="households_gross_savings",
    units="$/Year",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "households_disposable_income": 1,
        "total_households_consumption_coicop": 1,
    },
)
def households_gross_savings():
    """
    Net amount that households have available to purchase financial assets. If it is negative, they will have to liquidate assets or acquire liabilities.
    """
    return households_disposable_income() - total_households_consumption_coicop()


@component.add(
    name="households_income_tax",
    units="$/Year",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"income_tax_rate": 1, "delayed_ts_taxable_income": 1},
)
def households_income_tax():
    """
    Households income tax by household type
    """
    return income_tax_rate() * delayed_ts_taxable_income()


@component.add(
    name="households_net_labour_income",
    units="$/Year",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"households_gross_labour_income": 1, "households_social_security": 1},
)
def households_net_labour_income():
    """
    Households net labour income by household type.
    """
    return households_gross_labour_income() - households_social_security()


@component.add(
    name="households_net_operating_surplus",
    units="$/Year",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_households": 1,
        "time": 1,
        "initial_households_net_operating_surplus": 1,
        "adjustment_factor_net_operating_surplus": 1,
        "delayed_ts_net_operating_surplus_per_hh": 1,
    },
)
def households_net_operating_surplus():
    """
    Households net operating surplus by household type
    """
    return if_then_else(
        np.logical_or(switch_eco_households() == 0, time() <= 2015),
        lambda: initial_households_net_operating_surplus(),
        lambda: adjustment_factor_net_operating_surplus()
        * delayed_ts_net_operating_surplus_per_hh(),
    )


@component.add(
    name="households_net_wealth_by_type_of_household",
    units="$",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_economy": 1,
        "switch_fin2eco": 1,
        "initial_households_financial_assets_per_household": 1,
        "initial_households_financial_liabilities_per_household": 1,
        "initial_households_capital_stock_per_household": 1,
        "households_financial_liabilities": 1,
        "households_financial_assets": 1,
        "households_capital_stock": 1,
    },
)
def households_net_wealth_by_type_of_household():
    """
    Households net wealth by type of households.
    """
    return if_then_else(
        np.logical_or(switch_economy() == 0, switch_fin2eco() == 0),
        lambda: initial_households_capital_stock_per_household()
        + initial_households_financial_assets_per_household()
        - initial_households_financial_liabilities_per_household(),
        lambda: households_capital_stock()
        + households_financial_assets()
        - households_financial_liabilities(),
    )


@component.add(
    name="households_other_transfers_paid",
    units="$/Year",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_households_other_transfers_paid"},
)
def households_other_transfers_paid():
    """
    Households other transfers paid by household type
    """
    return _ext_constant_households_other_transfers_paid()


_ext_constant_households_other_transfers_paid = ExtConstant(
    "model_parameters/economy/Consumption_ENDOGENOUS.xlsx",
    "HH_Other_transfers_paid",
    "OTHER_TRANSFERS_PAID",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
    "_ext_constant_households_other_transfers_paid",
)


@component.add(
    name="households_other_transfers_received",
    units="$/Year",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_households_other_transfers_received"},
)
def households_other_transfers_received():
    """
    Households other transfers received by household type
    """
    return _ext_constant_households_other_transfers_received()


_ext_constant_households_other_transfers_received = ExtConstant(
    "model_parameters/economy/Consumption_ENDOGENOUS.xlsx",
    "HH_Other_transfers_rec",
    "OTHER_TRANSFERS_RECEIVED",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
    "_ext_constant_households_other_transfers_received",
)


@component.add(
    name="households_share_quaids",
    units="DMNL",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I", "QUAIDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"households_share_quaids_non_adjusted": 2},
)
def households_share_quaids():
    """
    Households non-durable consumption shares (QUAIDS model)
    """
    return zidz(
        households_share_quaids_non_adjusted(),
        sum(
            households_share_quaids_non_adjusted().rename(
                {"QUAIDS_I": "QUAIDS_MAP_I!"}
            ),
            dim=["QUAIDS_MAP_I!"],
        ).expand_dims({"QUAIDS_I": _subscript_dict["QUAIDS_I"]}, 2),
    )


@component.add(
    name="households_share_quaids_non_adjusted",
    units="DMNL",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I", "QUAIDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "constant_quaids": 2,
        "price_coicop": 4,
        "price_transformation": 8,
        "beta_quaids": 2,
        "households_consumption_non_durable_non_energy": 8,
        "price_quaids_1": 8,
        "epsilon_quaids": 2,
        "alpha_quaids": 2,
        "price_quaids_2": 4,
    },
)
def households_share_quaids_non_adjusted():
    """
    Households share of non-durables consumption. MAX( 0.02 , IF_THEN_ELSE( CONSTANT_QUAIDS[REGIONS_35_I,HOUSEHOLDS_I,QUAIDS_I] +SUM(BETA_QUAIDS[REGIONS_35_I,HOUSEHOLDS_I,QUAIDS_I,QUAIDS_MAP_I!] *LN(price_QUAIDS_category[REGIONS_35_I,HOUSEHOLDS_I,QUAIDS_MAP_I!]/PRICE_TRANSFORMATI ON +1e-07)) +IF_THEN_ELSE(price_QUAIDS_1[REGIONS_35_I,HOUSEHOLDS_I] <= 0 , 0 , EPSILON_QUAIDS[REGIONS_35_I,HOUSEHOLDS_I,QUAIDS_I] *LN(households_consumption_non_durable_non_energy[REGIONS_35_I,HOUSEHOLDS_I]/price_QU AIDS_1[REGIONS_35_I,HOUSEHOLDS_I]/PRICE_TRANSFORMATION+1e-07) ) +IF_THEN_ELSE( price_QUAIDS_2[REGIONS_35_I,HOUSEHOLDS_I] = 0, 0 , IF_THEN_ELSE(price_QUAIDS_1[REGIONS_35_I,HOUSEHOLDS_I] = 0, 0, (ALPHA_QUAIDS[REGIONS_35_I,HOUSEHOLDS_I,QUAIDS_I]/price_QUAIDS_2[REGIONS_35_I,HOUSEHO LDS_I]/PRICE_TRANSFORMATION) *(LN(households_consumption_non_durable_non_energy[REGIONS_35_I,HOUSEHOLDS_ I]/price_QUAIDS_1[REGIONS_35_I,HOUSEHOLDS_I]/PRICE_TRANSFORMATION+1e-07))^2 )) <=0 , 0 , CONSTANT_QUAIDS[REGIONS_35_I,HOUSEHOLDS_I,QUAIDS_I] +SUM(BETA_QUAIDS[REGIONS_35_I,HOUSEHOLDS_I,QUAIDS_I,QUAIDS_MAP_I!] *LN(price_QUAIDS_category[REGIONS_35_I,HOUSEHOLDS_I,QUAIDS_MAP_I!]/PRICE_TRANSFORMATI ON +1e-07)) +IF_THEN_ELSE(price_QUAIDS_1[REGIONS_35_I,HOUSEHOLDS_I] <= 0 , 0 , EPSILON_QUAIDS[REGIONS_35_I,HOUSEHOLDS_I,QUAIDS_I] *LN(households_consumption_non_durable_non_energy[REGIONS_35_I,HOUSEHOLDS_I]/price_QU AIDS_1[REGIONS_35_I,HOUSEHOLDS_I]/PRICE_TRANSFORMATION+1e-07) ) +IF_THEN_ELSE( price_QUAIDS_2[REGIONS_35_I,HOUSEHOLDS_I] = 0, 0 , IF_THEN_ELSE(price_QUAIDS_1[REGIONS_35_I,HOUSEHOLDS_I] = 0, 0, (ALPHA_QUAIDS[REGIONS_35_I,HOUSEHOLDS_I,QUAIDS_I]/price_QUAIDS_2[REGIONS_35_I,HOUSEHO LDS_I]/PRICE_TRANSFORMATION) *(LN(households_consumption_non_durable_non_energy[REGIONS_35_I,HOUSEHOLDS_ I]/price_QUAIDS_1[REGIONS_35_I,HOUSEHOLDS_I]/PRICE_TRANSFORMATION+1e-07))^2 )) ) )
    """
    return np.maximum(
        0.02,
        if_then_else(
            constant_quaids()
            + if_then_else(
                (
                    price_coicop()
                    .loc[:, _subscript_dict["QUAIDS_I"]]
                    .rename({"COICOP_I": "QUAIDS_I"})
                    <= 0
                ).expand_dims({"HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"]}, 2),
                lambda: xr.DataArray(
                    0,
                    {
                        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                        "QUAIDS_I": _subscript_dict["QUAIDS_I"],
                        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
                    },
                    ["REGIONS_35_I", "QUAIDS_I", "HOUSEHOLDS_I"],
                ),
                lambda: sum(
                    beta_quaids().rename({"QUAIDS_MAP_I": "QUAIDS_MAP_I!"})
                    * np.log(
                        price_coicop()
                        .loc[:, _subscript_dict["QUAIDS_MAP_I"]]
                        .rename({"COICOP_I": "QUAIDS_MAP_I!"})
                        / price_transformation()
                    ),
                    dim=["QUAIDS_MAP_I!"],
                ).transpose("REGIONS_35_I", "QUAIDS_I", "HOUSEHOLDS_I"),
            ).transpose("REGIONS_35_I", "HOUSEHOLDS_I", "QUAIDS_I")
            + if_then_else(
                np.logical_or(
                    price_quaids_1() <= 0,
                    households_consumption_non_durable_non_energy() <= 0,
                ).expand_dims({"QUAIDS_I": _subscript_dict["QUAIDS_I"]}, 2),
                lambda: xr.DataArray(
                    0,
                    {
                        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
                        "QUAIDS_I": _subscript_dict["QUAIDS_I"],
                    },
                    ["REGIONS_35_I", "HOUSEHOLDS_I", "QUAIDS_I"],
                ),
                lambda: epsilon_quaids()
                * np.log(
                    households_consumption_non_durable_non_energy()
                    / (price_quaids_1() / price_transformation())
                ),
            )
            + if_then_else(
                np.logical_or(
                    price_quaids_2() <= 0,
                    np.logical_or(
                        price_quaids_1() <= 0,
                        households_consumption_non_durable_non_energy() <= 0,
                    ),
                ).expand_dims({"QUAIDS_I": _subscript_dict["QUAIDS_I"]}, 2),
                lambda: xr.DataArray(
                    0,
                    {
                        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
                        "QUAIDS_I": _subscript_dict["QUAIDS_I"],
                    },
                    ["REGIONS_35_I", "HOUSEHOLDS_I", "QUAIDS_I"],
                ),
                lambda: (alpha_quaids() / (price_quaids_2() / price_transformation()))
                * (
                    np.log(
                        households_consumption_non_durable_non_energy()
                        / (price_quaids_1() / price_transformation())
                    )
                    ** 2
                ),
            )
            <= 0,
            lambda: xr.DataArray(
                0,
                {
                    "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                    "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
                    "QUAIDS_I": _subscript_dict["QUAIDS_I"],
                },
                ["REGIONS_35_I", "HOUSEHOLDS_I", "QUAIDS_I"],
            ),
            lambda: constant_quaids()
            + if_then_else(
                (
                    price_coicop()
                    .loc[:, _subscript_dict["QUAIDS_I"]]
                    .rename({"COICOP_I": "QUAIDS_I"})
                    <= 0
                ).expand_dims({"HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"]}, 2),
                lambda: xr.DataArray(
                    0,
                    {
                        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                        "QUAIDS_I": _subscript_dict["QUAIDS_I"],
                        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
                    },
                    ["REGIONS_35_I", "QUAIDS_I", "HOUSEHOLDS_I"],
                ),
                lambda: sum(
                    beta_quaids().rename({"QUAIDS_MAP_I": "QUAIDS_MAP_I!"})
                    * np.log(
                        price_coicop()
                        .loc[:, _subscript_dict["QUAIDS_MAP_I"]]
                        .rename({"COICOP_I": "QUAIDS_MAP_I!"})
                        / price_transformation()
                    ),
                    dim=["QUAIDS_MAP_I!"],
                ).transpose("REGIONS_35_I", "QUAIDS_I", "HOUSEHOLDS_I"),
            ).transpose("REGIONS_35_I", "HOUSEHOLDS_I", "QUAIDS_I")
            + if_then_else(
                np.logical_or(
                    price_quaids_1() <= 0,
                    households_consumption_non_durable_non_energy() <= 0,
                ).expand_dims({"QUAIDS_I": _subscript_dict["QUAIDS_I"]}, 2),
                lambda: xr.DataArray(
                    0,
                    {
                        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
                        "QUAIDS_I": _subscript_dict["QUAIDS_I"],
                    },
                    ["REGIONS_35_I", "HOUSEHOLDS_I", "QUAIDS_I"],
                ),
                lambda: epsilon_quaids()
                * np.log(
                    households_consumption_non_durable_non_energy()
                    / (price_quaids_1() / price_transformation())
                ),
            )
            + if_then_else(
                np.logical_or(
                    price_quaids_2() <= 0,
                    np.logical_or(
                        price_quaids_1() <= 0,
                        households_consumption_non_durable_non_energy() <= 0,
                    ),
                ).expand_dims({"QUAIDS_I": _subscript_dict["QUAIDS_I"]}, 2),
                lambda: xr.DataArray(
                    0,
                    {
                        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
                        "QUAIDS_I": _subscript_dict["QUAIDS_I"],
                    },
                    ["REGIONS_35_I", "HOUSEHOLDS_I", "QUAIDS_I"],
                ),
                lambda: (alpha_quaids() / (price_quaids_2() / price_transformation()))
                * (
                    np.log(
                        households_consumption_non_durable_non_energy()
                        / (price_quaids_1() / price_transformation())
                    )
                    ** 2
                ),
            ),
        ),
    )


@component.add(
    name="households_shares_by_income",
    units="DMNL/Year",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "delayed_number_of_households": 2,
        "summation_matrix_hh_shares_by_income_group": 1,
    },
)
def households_shares_by_income():
    """
    Households shares by income in each 12 socio-demographic groups (rural/unrab * 6 type)
    """
    return zidz(
        delayed_number_of_households(),
        sum(
            delayed_number_of_households().rename({"HOUSEHOLDS_I": "HOUSEHOLDS_MAP_I!"})
            * summation_matrix_hh_shares_by_income_group()
            .rename({"HOUSEHOLDS_MAP_I": "HOUSEHOLDS_MAP_I!"})
            .transpose("HOUSEHOLDS_MAP_I!", "HOUSEHOLDS_I"),
            dim=["HOUSEHOLDS_MAP_I!"],
        ),
    )


@component.add(
    name="households_social_benefits",
    units="$/Year",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_households": 1,
        "time": 1,
        "initial_households_social_benefits": 1,
        "adjustment_factor_social_benefits": 1,
        "delayed_ts_social_benefits_per_household": 1,
    },
)
def households_social_benefits():
    """
    Households social benefits by household type. Hay algunas diferencias entre social benefits y BASE_SOCIAL_BENEFITS
    """
    return if_then_else(
        np.logical_or(switch_eco_households() == 0, time() <= 2015),
        lambda: initial_households_social_benefits(),
        lambda: adjustment_factor_social_benefits()
        * delayed_ts_social_benefits_per_household(),
    )


@component.add(
    name="households_social_security",
    units="$/Year",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"rate_social_security_sp": 1, "households_gross_labour_income": 1},
)
def households_social_security():
    """
    Social security contributions by household type
    """
    return rate_social_security_sp() * households_gross_labour_income()


@component.add(
    name="households_wealth_tax",
    units="$/Year",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "delayed_ts_households_net_wealth_by_type_of_household": 1,
        "wealth_tax_rate": 1,
        "households_taxes_on_assets_to_finance_basic_income": 1,
    },
)
def households_wealth_tax():
    """
    Households wealth taxes by household type
    """
    return (
        delayed_ts_households_net_wealth_by_type_of_household() * wealth_tax_rate()
        + households_taxes_on_assets_to_finance_basic_income()
    )


@component.add(
    name="IMPLICIT_PRICE_ENERGY_HOUSEHOLDS_COICOP",
    units="Mdollars_2015/TJ",
    subscripts=["REGIONS_35_I", "COICOP_ENERGY_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "base_consumption_coicop": 1,
        "final_energy_consumption_households_coicop": 1,
    },
)
def implicit_price_energy_households_coicop():
    """
    Implicit prices of energy consumed by housholds by
    """
    return zidz(
        base_consumption_coicop()
        .loc[:, _subscript_dict["COICOP_ENERGY_I"]]
        .rename({"COICOP_I": "COICOP_ENERGY_I"}),
        final_energy_consumption_households_coicop(),
    )


@component.add(
    name="IMPLICIT_PRICE_PUBLIC_TRANSPORT_HOUSEHOLDS",
    units="Mdollars_2015/(pkm*person)",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I", "COICOP_TRANSPORT_EXC_FUEL_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "initial_households_consumption_coicop": 1,
        "initial_public_transport_demand_coicop": 1,
    },
)
def implicit_price_public_transport_households():
    """
    Implicit prices for households consumption of public transporta
    """
    return zidz(
        initial_households_consumption_coicop()
        .loc[:, :, _subscript_dict["COICOP_TRANSPORT_EXC_FUEL_I"]]
        .rename({"COICOP_I": "COICOP_TRANSPORT_EXC_FUEL_I"}),
        initial_public_transport_demand_coicop(),
    )


@component.add(
    name="IMV_final_energy_consumption_buildings_and_transport_top_down_COICOP",
    units="TJ/Year",
    subscripts=["REGIONS_35_I", "COICOP_ENERGY_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "energy_consumption_buildings_and_transport_top_down": 1,
        "implicit_price_energy_households_coicop": 1,
    },
)
def imv_final_energy_consumption_buildings_and_transport_top_down_coicop():
    """
    Households final energy consumption in physical untis calcaulted top-down in COICOP classification
    """
    return zidz(
        energy_consumption_buildings_and_transport_top_down(),
        implicit_price_energy_households_coicop(),
    )


@component.add(
    name="INITIAL_HOUSEHOLDS_DISPOSABLE_INCOME",
    units="$/Year",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_initial_households_disposable_income": 1},
    other_deps={
        "_initial_initial_households_disposable_income": {
            "initial": {"households_disposable_income": 1},
            "step": {},
        }
    },
)
def initial_households_disposable_income():
    """
    Initial households disposable income.
    """
    return _initial_initial_households_disposable_income()


_initial_initial_households_disposable_income = Initial(
    lambda: households_disposable_income(),
    "_initial_initial_households_disposable_income",
)


@component.add(
    name="INITIAL_HOUSEHOLDS_LABOUR_COMPENSATION",
    units="$/Year",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "base_number_of_households": 1,
        "base_labour_compensation": 1,
        "base_labour_compensation_share": 1,
        "unit_conversion_dollars_mdollars": 1,
    },
)
def initial_households_labour_compensation():
    """
    Inital household labour compensation
    """
    return (
        zidz(
            xr.DataArray(
                1,
                {
                    "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                    "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
                },
                ["REGIONS_35_I", "HOUSEHOLDS_I"],
            ),
            base_number_of_households(),
        )
        * sum(
            base_labour_compensation().rename({"SECTORS_I": "SECTORS_I!"}),
            dim=["SECTORS_I!"],
        )
        * base_labour_compensation_share()
        * unit_conversion_dollars_mdollars()
    )


@component.add(
    name="INITIAL_HOUSEHOLDS_NET_OPERATING_SURPLUS",
    units="$/Year",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "base_number_of_households": 1,
        "base_operating_surplus_share": 1,
        "base_net_operating_surplus": 1,
        "base_tax_income_corporations": 1,
        "unit_conversion_dollars_mdollars": 1,
    },
)
def initial_households_net_operating_surplus():
    """
    Initial households net operating surplus
    """
    return (
        zidz(
            xr.DataArray(
                1,
                {
                    "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                    "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
                },
                ["REGIONS_35_I", "HOUSEHOLDS_I"],
            ),
            base_number_of_households(),
        )
        * base_operating_surplus_share()
        * (base_net_operating_surplus() - base_tax_income_corporations())
        * unit_conversion_dollars_mdollars()
    )


@component.add(
    name="INITIAL_HOUSEHOLDS_PROPERTY_INCOME_RECEIVED",
    units="$/Year",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_initial_households_property_income_received"
    },
)
def initial_households_property_income_received():
    return _ext_constant_initial_households_property_income_received()


_ext_constant_initial_households_property_income_received = ExtConstant(
    "model_parameters/economy/Consumption_ENDOGENOUS.xlsx",
    "HH_Property_income_rec",
    "INITIAL_HOUSEHOLDS_PROPERTY_INCOME_RECEIVED",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
    "_ext_constant_initial_households_property_income_received",
)


@component.add(
    name="INITIAL_HOUSEHOLDS_SOCIAL_BENEFITS",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "base_number_of_households": 1,
        "base_share_social_benefits": 1,
        "base_social_benefits": 1,
        "unit_conversion_dollars_mdollars": 1,
    },
)
def initial_households_social_benefits():
    """
    Inital households social benefits
    """
    return (
        zidz(
            xr.DataArray(
                1,
                {
                    "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                    "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
                },
                ["REGIONS_35_I", "HOUSEHOLDS_I"],
            ),
            base_number_of_households(),
        )
        * base_share_social_benefits()
        * base_social_benefits()
        * unit_conversion_dollars_mdollars()
    )


@component.add(
    name="INITIAL_PUBLIC_TRANSPORT_DEMAND_COICOP",
    units="km*person",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I", "COICOP_TRANSPORT_EXC_FUEL_I"],
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_initial_public_transport_demand_coicop": 1},
    other_deps={
        "_initial_initial_public_transport_demand_coicop": {
            "initial": {"public_households_transport_demand_coicop": 1},
            "step": {},
        }
    },
)
def initial_public_transport_demand_coicop():
    """
    Inital public transport demand
    """
    return _initial_initial_public_transport_demand_coicop()


_initial_initial_public_transport_demand_coicop = Initial(
    lambda: public_households_transport_demand_coicop(),
    "_initial_initial_public_transport_demand_coicop",
)


@component.add(
    name="labour_compensation_non_adjusted",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "delayed_ts_labour_compensation_per_household": 2,
        "unit_conversion_dollars_mdollars": 2,
        "base_number_of_households": 1,
        "number_of_households_by_income_and_type": 1,
    },
)
def labour_compensation_non_adjusted():
    """
    Labour compensation non adjusted
    """
    return if_then_else(
        time() <= 2015,
        lambda: sum(
            delayed_ts_labour_compensation_per_household().rename(
                {"HOUSEHOLDS_I": "HOUSEHOLDS_I!"}
            )
            * base_number_of_households().rename({"HOUSEHOLDS_I": "HOUSEHOLDS_I!"}),
            dim=["HOUSEHOLDS_I!"],
        )
        / unit_conversion_dollars_mdollars(),
        lambda: sum(
            delayed_ts_labour_compensation_per_household().rename(
                {"HOUSEHOLDS_I": "HOUSEHOLDS_I!"}
            )
            * number_of_households_by_income_and_type().rename(
                {"HOUSEHOLDS_I": "HOUSEHOLDS_I!"}
            ),
            dim=["HOUSEHOLDS_I!"],
        )
        / unit_conversion_dollars_mdollars(),
    )


@component.add(
    name="LIMIT_CONSUMPTION_ENERGY_OVER_TOTAL_NON_DURABLES_SP",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_limit_consumption_energy_over_total_non_durables_sp"
    },
)
def limit_consumption_energy_over_total_non_durables_sp():
    """
    Limit to the consumption of energy over total consumption of non durables.
    """
    return _ext_constant_limit_consumption_energy_over_total_non_durables_sp()


_ext_constant_limit_consumption_energy_over_total_non_durables_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "LIMIT_CONSUMPTION_ENERGY_OVER_TOTAL_NON_DURABLES",
    {},
    _root,
    {},
    "_ext_constant_limit_consumption_energy_over_total_non_durables_sp",
)


@component.add(
    name="LOCKDOWN_SHOCK_REDUCTION_DEMAND_TRANSPORT_SP",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_lockdown_shock_reduction_demand_transport_sp"
    },
)
def lockdown_shock_reduction_demand_transport_sp():
    """
    Effect of Lockdown on private passenger transport.
    """
    return _ext_constant_lockdown_shock_reduction_demand_transport_sp()


_ext_constant_lockdown_shock_reduction_demand_transport_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "LOCKDOWN_SHOCK_REDUCTION_DEMAND_TRANSPORT",
    {},
    _root,
    {},
    "_ext_constant_lockdown_shock_reduction_demand_transport_sp",
)


@component.add(
    name="net_operationg_surplus_non_adjusted",
    units="$/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "unit_conversion_dollars_mdollars": 2,
        "base_number_of_households": 1,
        "delayed_ts_net_operating_surplus_per_hh": 2,
        "number_of_households_by_income_and_type": 1,
    },
)
def net_operationg_surplus_non_adjusted():
    return if_then_else(
        time() <= 2015,
        lambda: sum(
            delayed_ts_net_operating_surplus_per_hh().rename(
                {"HOUSEHOLDS_I": "HOUSEHOLDS_I!"}
            )
            * base_number_of_households().rename({"HOUSEHOLDS_I": "HOUSEHOLDS_I!"}),
            dim=["HOUSEHOLDS_I!"],
        )
        / unit_conversion_dollars_mdollars(),
        lambda: sum(
            delayed_ts_net_operating_surplus_per_hh().rename(
                {"HOUSEHOLDS_I": "HOUSEHOLDS_I!"}
            )
            * number_of_households_by_income_and_type().rename(
                {"HOUSEHOLDS_I": "HOUSEHOLDS_I!"}
            ),
            dim=["HOUSEHOLDS_I!"],
        )
        / unit_conversion_dollars_mdollars(),
    )


@component.add(
    name="number_of_households_by_income_and_type",
    units="DMNL/Year",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "base_number_of_households": 9,
        "switch_dem2eco_number_households": 8,
        "switch_eco_households": 8,
        "number_households_by_type_eu27": 7,
        "households_correspondance_16_to_60": 1,
        "households_shares_by_income": 8,
        "switch_economy": 8,
        "number_households_noneu": 1,
    },
)
def number_of_households_by_income_and_type():
    """
    number of housholds by income group and type
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
        },
        ["REGIONS_35_I", "HOUSEHOLDS_I"],
    )
    value.loc[_subscript_dict["REGIONS_DISAGGREGATED_HH_I"], :] = if_then_else(
        time() <= 2015,
        lambda: base_number_of_households()
        .loc[_subscript_dict["REGIONS_DISAGGREGATED_HH_I"], :]
        .rename({"REGIONS_35_I": "REGIONS_DISAGGREGATED_HH_I"}),
        lambda: if_then_else(
            np.logical_or(
                switch_economy() == 0,
                np.logical_or(
                    switch_eco_households() == 0,
                    switch_dem2eco_number_households() == 0,
                ),
            ),
            lambda: base_number_of_households()
            .loc[_subscript_dict["REGIONS_DISAGGREGATED_HH_I"], :]
            .rename({"REGIONS_35_I": "REGIONS_DISAGGREGATED_HH_I"}),
            lambda: sum(
                number_households_by_type_eu27()
                .loc[_subscript_dict["REGIONS_DISAGGREGATED_HH_I"], :]
                .rename(
                    {
                        "REGIONS_EU27_I": "REGIONS_DISAGGREGATED_HH_I",
                        "HOUSEHOLDS_DEMOGRAPHY_I": "HOUSEHOLDS_DEMOGRAPHY_I!",
                    }
                )
                * households_correspondance_16_to_60()
                .rename({"HOUSEHOLDS_DEMOGRAPHY_I": "HOUSEHOLDS_DEMOGRAPHY_I!"})
                .transpose("HOUSEHOLDS_DEMOGRAPHY_I!", "HOUSEHOLDS_I"),
                dim=["HOUSEHOLDS_DEMOGRAPHY_I!"],
            )
            * households_shares_by_income()
            .loc[_subscript_dict["REGIONS_DISAGGREGATED_HH_I"], :]
            .rename({"REGIONS_35_I": "REGIONS_DISAGGREGATED_HH_I"}),
        ),
    ).values
    value.loc[_subscript_dict["REGIONS_8_I"], :] = if_then_else(
        np.logical_or(
            switch_economy() == 0,
            np.logical_or(
                switch_eco_households() == 0, switch_dem2eco_number_households() == 0
            ),
        ),
        lambda: base_number_of_households()
        .loc[_subscript_dict["REGIONS_8_I"], :]
        .rename({"REGIONS_35_I": "REGIONS_8_I"}),
        lambda: number_households_noneu()
        * households_shares_by_income()
        .loc[_subscript_dict["REGIONS_8_I"], :]
        .rename({"REGIONS_35_I": "REGIONS_8_I"}),
    ).values
    value.loc[["AUSTRIA"], :] = (
        if_then_else(
            np.logical_or(
                switch_economy() == 0,
                np.logical_or(
                    switch_dem2eco_number_households() == 0,
                    switch_eco_households() == 0,
                ),
            ),
            lambda: base_number_of_households()
            .loc["AUSTRIA", :]
            .reset_coords(drop=True),
            lambda: sum(
                number_households_by_type_eu27()
                .loc["AUSTRIA", :]
                .reset_coords(drop=True)
                .rename({"HOUSEHOLDS_DEMOGRAPHY_I": "HOUSEHOLDS_DEMOGRAPHY_I!"}),
                dim=["HOUSEHOLDS_DEMOGRAPHY_I!"],
            )
            * households_shares_by_income().loc["AUSTRIA", :].reset_coords(drop=True),
        )
        .expand_dims({"REGIONS_35_I": ["AUSTRIA"]}, 0)
        .values
    )
    value.loc[["ITALY"], :] = (
        if_then_else(
            np.logical_or(
                switch_economy() == 0,
                np.logical_or(
                    switch_dem2eco_number_households() == 0,
                    switch_eco_households() == 0,
                ),
            ),
            lambda: base_number_of_households().loc["ITALY", :].reset_coords(drop=True),
            lambda: sum(
                number_households_by_type_eu27()
                .loc["ITALY", :]
                .reset_coords(drop=True)
                .rename({"HOUSEHOLDS_DEMOGRAPHY_I": "HOUSEHOLDS_DEMOGRAPHY_I!"}),
                dim=["HOUSEHOLDS_DEMOGRAPHY_I!"],
            )
            * households_shares_by_income().loc["ITALY", :].reset_coords(drop=True),
        )
        .expand_dims({"REGIONS_35_I": ["ITALY"]}, 0)
        .values
    )
    value.loc[["MALTA"], :] = (
        if_then_else(
            np.logical_or(
                switch_economy() == 0,
                np.logical_or(
                    switch_dem2eco_number_households() == 0,
                    switch_eco_households() == 0,
                ),
            ),
            lambda: base_number_of_households().loc["MALTA", :].reset_coords(drop=True),
            lambda: sum(
                number_households_by_type_eu27()
                .loc["MALTA", :]
                .reset_coords(drop=True)
                .rename({"HOUSEHOLDS_DEMOGRAPHY_I": "HOUSEHOLDS_DEMOGRAPHY_I!"}),
                dim=["HOUSEHOLDS_DEMOGRAPHY_I!"],
            )
            * households_shares_by_income().loc["MALTA", :].reset_coords(drop=True),
        )
        .expand_dims({"REGIONS_35_I": ["MALTA"]}, 0)
        .values
    )
    value.loc[["NETHERLANDS"], :] = (
        if_then_else(
            np.logical_or(
                switch_economy() == 0,
                np.logical_or(
                    switch_dem2eco_number_households() == 0,
                    switch_eco_households() == 0,
                ),
            ),
            lambda: base_number_of_households()
            .loc["NETHERLANDS", :]
            .reset_coords(drop=True),
            lambda: sum(
                number_households_by_type_eu27()
                .loc["NETHERLANDS", :]
                .reset_coords(drop=True)
                .rename({"HOUSEHOLDS_DEMOGRAPHY_I": "HOUSEHOLDS_DEMOGRAPHY_I!"}),
                dim=["HOUSEHOLDS_DEMOGRAPHY_I!"],
            )
            * households_shares_by_income()
            .loc["NETHERLANDS", :]
            .reset_coords(drop=True),
        )
        .expand_dims({"REGIONS_35_I": ["NETHERLANDS"]}, 0)
        .values
    )
    value.loc[["ROMANIA"], :] = (
        if_then_else(
            np.logical_or(
                switch_economy() == 0,
                np.logical_or(
                    switch_dem2eco_number_households() == 0,
                    switch_eco_households() == 0,
                ),
            ),
            lambda: base_number_of_households()
            .loc["ROMANIA", :]
            .reset_coords(drop=True),
            lambda: sum(
                number_households_by_type_eu27()
                .loc["ROMANIA", :]
                .reset_coords(drop=True)
                .rename({"HOUSEHOLDS_DEMOGRAPHY_I": "HOUSEHOLDS_DEMOGRAPHY_I!"}),
                dim=["HOUSEHOLDS_DEMOGRAPHY_I!"],
            )
            * households_shares_by_income().loc["ROMANIA", :].reset_coords(drop=True),
        )
        .expand_dims({"REGIONS_35_I": ["ROMANIA"]}, 0)
        .values
    )
    value.loc[["SLOVENIA"], :] = (
        if_then_else(
            np.logical_or(
                switch_economy() == 0,
                np.logical_or(
                    switch_dem2eco_number_households() == 0,
                    switch_eco_households() == 0,
                ),
            ),
            lambda: base_number_of_households()
            .loc["SLOVENIA", :]
            .reset_coords(drop=True),
            lambda: sum(
                number_households_by_type_eu27()
                .loc["SLOVENIA", :]
                .reset_coords(drop=True)
                .rename({"HOUSEHOLDS_DEMOGRAPHY_I": "HOUSEHOLDS_DEMOGRAPHY_I!"}),
                dim=["HOUSEHOLDS_DEMOGRAPHY_I!"],
            )
            * households_shares_by_income().loc["SLOVENIA", :].reset_coords(drop=True),
        )
        .expand_dims({"REGIONS_35_I": ["SLOVENIA"]}, 0)
        .values
    )
    return value


@component.add(
    name="price_non_durables",
    units="DMNL",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"delayed_ts_shares_consumption_non_durables": 1, "price_coicop": 1},
)
def price_non_durables():
    """
    Aggregated price of non durables by household
    """
    return sum(
        delayed_ts_shares_consumption_non_durables().rename(
            {"COICOP_NON_DURABLES_I": "COICOP_NON_DURABLES_I!"}
        )
        * price_coicop()
        .loc[:, _subscript_dict["COICOP_NON_DURABLES_I"]]
        .rename({"COICOP_I": "COICOP_NON_DURABLES_I!"}),
        dim=["COICOP_NON_DURABLES_I!"],
    )


@component.add(
    name="price_QUAIDS_1",
    units="DMNL",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "delayed_ts_households_share_quaids": 2,
        "price_coicop": 2,
        "price_transformation": 4,
    },
)
def price_quaids_1():
    """
    Price 1 of the QUAIDS model. IF_THEN_ELSE(SUM(delayed_households_share_quaids[REGIONS_35_I,HOUSEHOLDS_I, QUAIDS_I!]*(LN(ZIDZ(price_QUAIDS_category[REGIONS_35_I,HOUSEHOLDS_I,QUAIDS_ I!],PRICE_TRANSFORMATION))))*PRICE_TRANSFORMATION<=0,0,SUM(delayed_househol ds_share_quaids[REGIONS_35_I,HOUSEHOLDS_I,QUAIDS_I!]*(LN(ZIDZ(price_QUAIDS_ category[REGIONS_35_I,HOUSEHOLDS_I,QUAIDS_I!],PRICE_TRANSFORMATION))))*PRIC E_TRANSFORMATION)SFORMATION))))*PRICE_TRANSFORMATION)
    """
    return if_then_else(
        sum(
            delayed_ts_households_share_quaids().rename({"QUAIDS_I": "QUAIDS_I!"})
            * (
                np.log(
                    zidz(
                        price_coicop()
                        .loc[:, _subscript_dict["QUAIDS_I"]]
                        .rename({"COICOP_I": "QUAIDS_I!"}),
                        price_transformation(),
                    )
                )
                + 1
            ),
            dim=["QUAIDS_I!"],
        )
        * price_transformation()
        <= 0,
        lambda: xr.DataArray(
            0,
            {
                "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
            },
            ["REGIONS_35_I", "HOUSEHOLDS_I"],
        ),
        lambda: sum(
            delayed_ts_households_share_quaids().rename({"QUAIDS_I": "QUAIDS_I!"})
            * (
                np.log(
                    zidz(
                        price_coicop()
                        .loc[:, _subscript_dict["QUAIDS_I"]]
                        .rename({"COICOP_I": "QUAIDS_I!"}),
                        price_transformation(),
                    )
                )
                + 1
            ),
            dim=["QUAIDS_I!"],
        )
        * price_transformation(),
    )


@component.add(
    name="price_QUAIDS_2",
    units="DMNL",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "delayed_ts_households_share_quaids": 1,
        "epsilon_quaids": 1,
        "price_transformation": 1,
    },
)
def price_quaids_2():
    """
    Price 2 of the QUAIDS model. PROD((delayed_households_share_quaids[REGIONS_35_I,HOUSEHOLDS_I,QUAIDS_I!]+1e-07)^EPS ILON_QUAIDS[REGIONS_35_I,HOUSEHOLDS_I ,QUAIDS_I!] )*PRICE_TRANSFORMATION
    """
    return (
        prod(
            (
                delayed_ts_households_share_quaids().rename({"QUAIDS_I": "QUAIDS_I!"})
                + 1e-07
            )
            ** epsilon_quaids().rename({"QUAIDS_I": "QUAIDS_I!"}),
            dim=["QUAIDS_I!"],
        )
        * price_transformation()
    )


@component.add(
    name="price_transport",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"delayed_ts_shares_consumption_transportation": 1, "price_coicop": 1},
)
def price_transport():
    """
    Aggregated price of transportation by households type
    """
    return sum(
        delayed_ts_shares_consumption_transportation().rename(
            {"COICOP_TRANSPORT_I": "COICOP_TRANSPORT_I!"}
        )
        * price_coicop()
        .loc[:, _subscript_dict["COICOP_TRANSPORT_I"]]
        .rename({"COICOP_I": "COICOP_TRANSPORT_I!"}),
        dim=["COICOP_TRANSPORT_I!"],
    )


@component.add(
    name="public_households_transport_demand_COICOP",
    units="km*person",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I", "COICOP_TRANSPORT_EXC_FUEL_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "public_transport_demand_coicop_physical_units": 1,
        "number_of_households_by_income_and_type": 1,
    },
)
def public_households_transport_demand_coicop():
    """
    Housholds consumption of public transport by houshold type in physical units
    """
    return zidz(
        public_transport_demand_coicop_physical_units(),
        number_of_households_by_income_and_type().expand_dims(
            {
                "COICOP_TRANSPORT_EXC_FUEL_I": _subscript_dict[
                    "COICOP_TRANSPORT_EXC_FUEL_I"
                ]
            },
            2,
        ),
    )


@component.add(
    name="public_transport_demand_COICOP_physical_units",
    units="km*person",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I", "COICOP_TRANSPORT_EXC_FUEL_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"passenger_transport_demand_public_fleet": 6},
)
def public_transport_demand_coicop_physical_units():
    """
    Transport demand in COICOP classification, physilca units
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
            "COICOP_TRANSPORT_EXC_FUEL_I": _subscript_dict[
                "COICOP_TRANSPORT_EXC_FUEL_I"
            ],
        },
        ["REGIONS_35_I", "HOUSEHOLDS_I", "COICOP_TRANSPORT_EXC_FUEL_I"],
    )
    value.loc[:, :, ["HH_ROAD"]] = (
        passenger_transport_demand_public_fleet()
        .loc[:, "bus", :]
        .reset_coords(drop=True)
        .expand_dims({"COICOP_I": ["HH_ROAD"]}, 2)
        .values
    )
    value.loc[:, :, ["HH_RAILWAY"]] = (
        passenger_transport_demand_public_fleet()
        .loc[:, "RAIL", :]
        .reset_coords(drop=True)
        .expand_dims({"COICOP_I": ["HH_RAILWAY"]}, 2)
        .values
    )
    value.loc[:, :, ["HH_MARITIME"]] = (
        passenger_transport_demand_public_fleet()
        .loc[:, "MARINE", :]
        .reset_coords(drop=True)
        .expand_dims({"COICOP_I": ["HH_MARITIME"]}, 2)
        .values
    )
    value.loc[:, :, ["HH_AIR"]] = (
        (
            passenger_transport_demand_public_fleet()
            .loc[:, "AIR_DOMESTIC", :]
            .reset_coords(drop=True)
            + passenger_transport_demand_public_fleet()
            .loc[:, "AIR_INTRA_EU", :]
            .reset_coords(drop=True)
            + passenger_transport_demand_public_fleet()
            .loc[:, "AIR_INTERNATIONAL", :]
            .reset_coords(drop=True)
        )
        .expand_dims({"COICOP_I": ["HH_AIR"]}, 2)
        .values
    )
    return value


@component.add(
    name="ratio_household_consumpion_transport_energy_to_total_non_durables",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "total_households_consumption_transport_energy_top_down": 1,
        "households_consumption_non_durables": 1,
    },
)
def ratio_household_consumpion_transport_energy_to_total_non_durables():
    """
    Ratio total household consumption of energy and transrpot to total consumption of non durables
    """
    return zidz(
        total_households_consumption_transport_energy_top_down(),
        households_consumption_non_durables(),
    )


@component.add(
    name="SHARE_ENERGY_CONSUMPTION_SOLID_BIO_VS_SOLID_FOSSIL",
    subscripts=["REGIONS_35_I"],
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_share_energy_consumption_solid_bio_vs_solid_fossil": 1},
    other_deps={
        "_initial_share_energy_consumption_solid_bio_vs_solid_fossil": {
            "initial": {"base_final_energy_consumption_households_by_fe_buildings": 3},
            "step": {},
        }
    },
)
def share_energy_consumption_solid_bio_vs_solid_fossil():
    return _initial_share_energy_consumption_solid_bio_vs_solid_fossil()


_initial_share_energy_consumption_solid_bio_vs_solid_fossil = Initial(
    lambda: base_final_energy_consumption_households_by_fe_buildings()
    .loc[:, "FE_solid_bio"]
    .reset_coords(drop=True)
    / (
        base_final_energy_consumption_households_by_fe_buildings()
        .loc[:, "FE_solid_bio"]
        .reset_coords(drop=True)
        + base_final_energy_consumption_households_by_fe_buildings()
        .loc[:, "FE_solid_fossil"]
        .reset_coords(drop=True)
    ),
    "_initial_share_energy_consumption_solid_bio_vs_solid_fossil",
)


@component.add(
    name="smooth_adjustment_factor_households_consumption_to_avoid_negative_assets",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Stateful",
    comp_subtype="Smooth",
    depends_on={
        "_smooth_smooth_adjustment_factor_households_consumption_to_avoid_negative_assets": 1
    },
    other_deps={
        "_smooth_smooth_adjustment_factor_households_consumption_to_avoid_negative_assets": {
            "initial": {
                "adjustment_factor_households_consumption_to_avoid_negative_assets": 1
            },
            "step": {
                "adjustment_factor_households_consumption_to_avoid_negative_assets": 1
            },
        }
    },
)
def smooth_adjustment_factor_households_consumption_to_avoid_negative_assets():
    """
    Correction factor of consumption to avoid negative fiancnial assets. When net lending is negative and in absoulte figures is twice the volume of assets we downscale the consumption to be equal to dispoable income
    """
    return (
        _smooth_smooth_adjustment_factor_households_consumption_to_avoid_negative_assets()
    )


_smooth_smooth_adjustment_factor_households_consumption_to_avoid_negative_assets = Smooth(
    lambda: adjustment_factor_households_consumption_to_avoid_negative_assets(),
    lambda: xr.DataArray(
        2,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
        },
        ["REGIONS_35_I", "HOUSEHOLDS_I"],
    ),
    lambda: adjustment_factor_households_consumption_to_avoid_negative_assets(),
    lambda: 1,
    "_smooth_smooth_adjustment_factor_households_consumption_to_avoid_negative_assets",
)


@component.add(
    name="social_benefits_non_adjusted",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "unit_conversion_dollars_mdollars": 2,
        "base_number_of_households": 1,
        "delayed_ts_social_benefits_per_household": 2,
        "number_of_households_by_income_and_type": 1,
    },
)
def social_benefits_non_adjusted():
    return if_then_else(
        time() <= 2015,
        lambda: sum(
            delayed_ts_social_benefits_per_household().rename(
                {"HOUSEHOLDS_I": "HOUSEHOLDS_I!"}
            )
            * base_number_of_households().rename({"HOUSEHOLDS_I": "HOUSEHOLDS_I!"}),
            dim=["HOUSEHOLDS_I!"],
        )
        / unit_conversion_dollars_mdollars(),
        lambda: sum(
            delayed_ts_social_benefits_per_household().rename(
                {"HOUSEHOLDS_I": "HOUSEHOLDS_I!"}
            )
            * number_of_households_by_income_and_type().rename(
                {"HOUSEHOLDS_I": "HOUSEHOLDS_I!"}
            ),
            dim=["HOUSEHOLDS_I!"],
        )
        / unit_conversion_dollars_mdollars(),
    )


@component.add(
    name="SWITCH_DEM2ECO_NUMBER_HOUSEHOLDS",
    units="1",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_dem2eco_number_households"},
)
def switch_dem2eco_number_households():
    """
    Intermodule links SWITCH, it can take two values: 0: the link is broken, the intermodule variable is replaced by an exogenous parameter. 1: the link between modules is operational.
    """
    return _ext_constant_switch_dem2eco_number_households()


_ext_constant_switch_dem2eco_number_households = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_DEM2ECO_NUMBER_HOUSEHOLDS",
    {},
    _root,
    {},
    "_ext_constant_switch_dem2eco_number_households",
)


@component.add(
    name="SWITCH_ECO_HH_BUILDINGS_ENERGY_BOTTOM_UP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_switch_eco_hh_buildings_energy_bottom_up"
    },
)
def switch_eco_hh_buildings_energy_bottom_up():
    """
    Dmnl
    """
    return _ext_constant_switch_eco_hh_buildings_energy_bottom_up()


_ext_constant_switch_eco_hh_buildings_energy_bottom_up = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_ECO_HH_BUILDINGS_ENERGY_BOTTOM_UP",
    {},
    _root,
    {},
    "_ext_constant_switch_eco_hh_buildings_energy_bottom_up",
)


@component.add(
    name="SWITCH_ECO_HH_TRANSPORT_ENERGY_BOTTOM_UP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_switch_eco_hh_transport_energy_bottom_up"
    },
)
def switch_eco_hh_transport_energy_bottom_up():
    return _ext_constant_switch_eco_hh_transport_energy_bottom_up()


_ext_constant_switch_eco_hh_transport_energy_bottom_up = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_ECO_HH_TRANSPORT_ENERGY_BOTTOM_UP",
    {},
    _root,
    {},
    "_ext_constant_switch_eco_hh_transport_energy_bottom_up",
)


@component.add(
    name="SWITCH_ECO_HOUSEHOLDS",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_eco_households"},
)
def switch_eco_households():
    """
    This switch can take two values: 0: the module runs isolated from the rest of WILIAM, replacing inter(sub)module variables with exogenous parameters. 1: the module runs integrated with the rest of WILIAM.
    """
    return _ext_constant_switch_eco_households()


_ext_constant_switch_eco_households = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_ECO_HOUSEHOLDS",
    {},
    _root,
    {},
    "_ext_constant_switch_eco_households",
)


@component.add(
    name="SWITCH_FIN2ECO",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_fin2eco"},
)
def switch_fin2eco():
    return _ext_constant_switch_fin2eco()


_ext_constant_switch_fin2eco = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_FINAN2ECO",
    {},
    _root,
    {},
    "_ext_constant_switch_fin2eco",
)


@component.add(
    name="SWITCH_LIMIT_CONSUMPTION_ENERGY_OVER_TOTAL_NON_DURABLES_SP",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_switch_limit_consumption_energy_over_total_non_durables_sp"
    },
)
def switch_limit_consumption_energy_over_total_non_durables_sp():
    """
    Switch for limiting the consumption of energy of non durables. Switch at= 0 -> no limit Switch at= 1 -> imposed limit
    """
    return _ext_constant_switch_limit_consumption_energy_over_total_non_durables_sp()


_ext_constant_switch_limit_consumption_energy_over_total_non_durables_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "SWITCH_LIMIT_CONSUMPTION_ENERGY_OVER_TOTAL_NON_DURABLES_SP",
    {},
    _root,
    {},
    "_ext_constant_switch_limit_consumption_energy_over_total_non_durables_sp",
)


@component.add(
    name="SWITCH_LOCKDOWN_EFFECT_ON_TRANSPORT_SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_lockdown_effect_on_transport_sp"},
)
def switch_lockdown_effect_on_transport_sp():
    """
    Switch for COVID shock on passernger Transport. If switch is zero no shock on passengers transport. If the Switch is is set to one than a reduction of passenger transport in the year 2030.
    """
    return _ext_constant_switch_lockdown_effect_on_transport_sp()


_ext_constant_switch_lockdown_effect_on_transport_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "SWITCH_LOCKDOWN_EFFECT_ON_TRANSPORT_SP",
    {},
    _root,
    {},
    "_ext_constant_switch_lockdown_effect_on_transport_sp",
)


@component.add(
    name="taxable_income",
    units="$/Year",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_economy": 1,
        "switch_fin2eco": 1,
        "initial_households_property_income_received": 1,
        "households_other_transfers_received": 2,
        "households_net_labour_income": 2,
        "households_social_security": 2,
        "households_social_benefits": 2,
        "households_net_operating_surplus": 2,
        "households_property_income_received": 1,
    },
)
def taxable_income():
    """
    Households taxable income by household type
    """
    return if_then_else(
        np.logical_or(switch_economy() == 0, switch_fin2eco() == 0),
        lambda: households_net_labour_income()
        + households_social_security()
        + households_net_operating_surplus()
        + initial_households_property_income_received()
        + households_social_benefits()
        + households_other_transfers_received(),
        lambda: households_net_labour_income()
        + households_social_security()
        + households_net_operating_surplus()
        + households_property_income_received()
        + households_social_benefits()
        + households_other_transfers_received(),
    )


@component.add(
    name="total_households_consumption_COICOP",
    units="$/Year",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"households_consumption_coicop": 1},
)
def total_households_consumption_coicop():
    """
    Sum of all consumption COICOP.
    """
    return sum(
        households_consumption_coicop().rename({"COICOP_I": "COICOP_I!"}),
        dim=["COICOP_I!"],
    )


@component.add(
    name="total_households_consumption_transport_energy_top_down",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"households_consumption_transport_energy_top_down": 1},
)
def total_households_consumption_transport_energy_top_down():
    """
    Total households consumption in transportation and energy
    """
    return sum(
        households_consumption_transport_energy_top_down().rename(
            {"COICOP_TRANSP_ENERGY_I": "COICOP_TRANSP_ENERGY_I!"}
        ),
        dim=["COICOP_TRANSP_ENERGY_I!"],
    )


@component.add(
    name="TRANSPORT_AND_ENERGY_ELASTICITIES",
    subscripts=["COICOP_TRANSP_ENERGY_I", "ELASTICITIES_TRANSPORT_ENERGY_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_transport_and_energy_elasticities"},
)
def transport_and_energy_elasticities():
    return _ext_constant_transport_and_energy_elasticities()


_ext_constant_transport_and_energy_elasticities = ExtConstant(
    "model_parameters/economy/Consumption_ECONOMETRIC.xlsx",
    "Elasticities",
    "ELASTICITIES",
    {
        "COICOP_TRANSP_ENERGY_I": _subscript_dict["COICOP_TRANSP_ENERGY_I"],
        "ELASTICITIES_TRANSPORT_ENERGY_I": _subscript_dict[
            "ELASTICITIES_TRANSPORT_ENERGY_I"
        ],
    },
    _root,
    {
        "COICOP_TRANSP_ENERGY_I": _subscript_dict["COICOP_TRANSP_ENERGY_I"],
        "ELASTICITIES_TRANSPORT_ENERGY_I": _subscript_dict[
            "ELASTICITIES_TRANSPORT_ENERGY_I"
        ],
    },
    "_ext_constant_transport_and_energy_elasticities",
)


@component.add(
    name="transport_demand_by_household_type",
    units="km*person",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "constant_transport": 1,
        "households_consumption_non_durables": 2,
        "price_transformation": 2,
        "price_non_durables": 2,
        "beta_transport": 1,
        "price_transport": 2,
        "epsilon_transport": 1,
    },
)
def transport_demand_by_household_type():
    """
    Household transport demand
    """
    return np.exp(
        constant_transport()
        + if_then_else(
            np.logical_or(
                households_consumption_non_durables() <= 0, price_non_durables() <= 0
            ),
            lambda: xr.DataArray(
                0,
                {
                    "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                    "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
                },
                ["REGIONS_35_I", "HOUSEHOLDS_I"],
            ),
            lambda: beta_transport()
            * np.log(
                households_consumption_non_durables()
                / (price_non_durables() / price_transformation())
            ),
        )
        + if_then_else(
            price_transport() <= 0,
            lambda: xr.DataArray(
                0,
                {
                    "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                    "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
                },
                ["REGIONS_35_I", "HOUSEHOLDS_I"],
            ),
            lambda: epsilon_transport()
            * np.log(price_transport() / price_transformation()),
        )
    )
