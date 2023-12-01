"""
Module economy.government
Translated using PySD version 3.10.0
"""


@component.add(
    name="aux_delayed_TS_average_disposable_income_inital_year_basic_income",
    subscripts=["REGIONS_35_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={
        "_delayfixed_aux_delayed_ts_average_disposable_income_inital_year_basic_income": 1
    },
    other_deps={
        "_delayfixed_aux_delayed_ts_average_disposable_income_inital_year_basic_income": {
            "initial": {"time_step": 1},
            "step": {
                "delayed_ts_average_disposable_income_inital_year_basic_income": 1
            },
        }
    },
)
def aux_delayed_ts_average_disposable_income_inital_year_basic_income():
    return (
        _delayfixed_aux_delayed_ts_average_disposable_income_inital_year_basic_income()
    )


_delayfixed_aux_delayed_ts_average_disposable_income_inital_year_basic_income = (
    DelayFixed(
        lambda: delayed_ts_average_disposable_income_inital_year_basic_income(),
        lambda: time_step(),
        lambda: xr.DataArray(
            0, {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]}, ["REGIONS_35_I"]
        ),
        time_step,
        "_delayfixed_aux_delayed_ts_average_disposable_income_inital_year_basic_income",
    )
)


@component.add(
    name="auxiliar_government_debt_statistical_difference",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "government_debt_statistical_difference": 1},
)
def auxiliar_government_debt_statistical_difference():
    """
    Statistical difference to make the change in government debt coherent with national accounts in the initial year. IF_THEN_ELSE (Time=2015,GOVERNMENT_DEBT_STATISTICAL_DIFFERENCE[REGIONS_35_I],0)
    """
    return if_then_else(
        time() == 2005,
        lambda: government_debt_statistical_difference(),
        lambda: xr.DataArray(
            0, {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]}, ["REGIONS_35_I"]
        ),
    )


@component.add(
    name="average_disposable_income",
    units="$/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "households_disposable_income": 1,
        "number_of_households_by_income_and_type": 2,
    },
)
def average_disposable_income():
    """
    Average disposable income per household
    """
    return zidz(
        sum(
            households_disposable_income().rename({"HOUSEHOLDS_I": "HOUSEHOLDS_I!"})
            * number_of_households_by_income_and_type().rename(
                {"HOUSEHOLDS_I": "HOUSEHOLDS_I!"}
            ),
            dim=["HOUSEHOLDS_I!"],
        ),
        sum(
            number_of_households_by_income_and_type().rename(
                {"HOUSEHOLDS_I": "HOUSEHOLDS_I!"}
            ),
            dim=["HOUSEHOLDS_I!"],
        ),
    )


@component.add(
    name="base_delayed_GDP",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"base_gross_domestic_product": 1},
)
def base_delayed_gdp():
    """
    Delayed Gross Domestic Product (GDP). ZIDZ( BASE GDP[REGIONS 35 I] , 1+INITIAL_DELAYED_GDP_GROWTH[REGIONS 35 I])
    """
    return base_gross_domestic_product() / (1 + 0.0005)


@component.add(
    name="change_in_government_debt",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "government_budget_balance": 1,
        "government_debt_adjustment": 1,
        "auxiliar_government_debt_statistical_difference": 1,
        "base_government_assets_net_adquisition": 1,
    },
)
def change_in_government_debt():
    """
    Change in the stock gross of debt.
    """
    return (
        -government_budget_balance()
        + government_debt_adjustment()
        + auxiliar_government_debt_statistical_difference()
        + base_government_assets_net_adquisition()
    )


@component.add(
    name="debt_interest",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"delayed_ts_government_debt": 1, "debt_interest_rate": 1},
)
def debt_interest():
    """
    Interests paid by the government to the owners of public debt.
    """
    return delayed_ts_government_debt() * debt_interest_rate()


@component.add(
    name="debt_interest_rate",
    units="DMNL/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_model_explorer": 1,
        "model_explorer_debt_interest_rate_target": 1,
        "time": 1,
        "initial_year_debt_interest_rate_target_sp": 1,
        "debt_interest_rate_historic": 2,
        "debt_interest_rate_target_sp": 1,
    },
)
def debt_interest_rate():
    """
    Debt interest rate.
    """
    return if_then_else(
        switch_model_explorer() == 1,
        lambda: model_explorer_debt_interest_rate_target(),
        lambda: if_then_else(
            time() < initial_year_debt_interest_rate_target_sp(),
            lambda: debt_interest_rate_historic(),
            lambda: debt_interest_rate_target_sp() + debt_interest_rate_historic(),
        ),
    )


@component.add(
    name="DEBT_INTEREST_RATE_TARGET_SP",
    units="DMNL/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_debt_interest_rate_target_sp"},
)
def debt_interest_rate_target_sp():
    """
    Debt interest rate target.
    """
    return _ext_constant_debt_interest_rate_target_sp()


_ext_constant_debt_interest_rate_target_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "DEBT_INTEREST_RATE_TARGET_SP*",
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    _root,
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    "_ext_constant_debt_interest_rate_target_sp",
)


@component.add(
    name="delayed_gdp_growth",
    units="DMNL/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_gdp_growth": 1},
    other_deps={
        "_delayfixed_delayed_gdp_growth": {
            "initial": {"base_initial_delayed_gdp_growth": 1},
            "step": {
                "time": 1,
                "base_initial_delayed_gdp_growth": 1,
                "gross_domestic_product_growth": 1,
            },
        }
    },
)
def delayed_gdp_growth():
    """
    Delayed GDP growth
    """
    return _delayfixed_delayed_gdp_growth()


_delayfixed_delayed_gdp_growth = DelayFixed(
    lambda: if_then_else(
        time() <= 2016,
        lambda: base_initial_delayed_gdp_growth(),
        lambda: gross_domestic_product_growth(),
    ),
    lambda: 1,
    lambda: base_initial_delayed_gdp_growth(),
    time_step,
    "_delayfixed_delayed_gdp_growth",
)


@component.add(
    name="delayed_government_revenue_to_GDP",
    units="DMNL",
    subscripts=["REGIONS_35_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_government_revenue_to_gdp": 1},
    other_deps={
        "_delayfixed_delayed_government_revenue_to_gdp": {
            "initial": {"initial_delayed_government_revenue_to_gdp": 1},
            "step": {
                "time": 1,
                "initial_delayed_government_revenue_to_gdp": 1,
                "government_revenue_to_gdp": 1,
            },
        }
    },
)
def delayed_government_revenue_to_gdp():
    """
    Delayed government revenue to GDP. *Initial value should be the delay. But this is how it is programmed in GAMS...
    """
    return _delayfixed_delayed_government_revenue_to_gdp()


_delayfixed_delayed_government_revenue_to_gdp = DelayFixed(
    lambda: if_then_else(
        time() <= 2015,
        lambda: initial_delayed_government_revenue_to_gdp(),
        lambda: government_revenue_to_gdp(),
    ),
    lambda: 1,
    lambda: initial_delayed_government_revenue_to_gdp(),
    time_step,
    "_delayfixed_delayed_government_revenue_to_gdp",
)


@component.add(
    name="delayed_gross_domestic_product",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_gross_domestic_product": 1},
    other_deps={
        "_delayfixed_delayed_gross_domestic_product": {
            "initial": {"initial_delayed_gdp": 1},
            "step": {
                "time": 1,
                "initial_delayed_gdp": 1,
                "gross_domestic_product_nominal": 1,
            },
        }
    },
)
def delayed_gross_domestic_product():
    """
    Delayed GDP
    """
    return _delayfixed_delayed_gross_domestic_product()


_delayfixed_delayed_gross_domestic_product = DelayFixed(
    lambda: if_then_else(
        time() <= 2014,
        lambda: initial_delayed_gdp(),
        lambda: gross_domestic_product_nominal(),
    ),
    lambda: 1,
    lambda: initial_delayed_gdp(),
    time_step,
    "_delayfixed_delayed_gross_domestic_product",
)


@component.add(
    name="delayed_TS_average_disposable_income",
    units="$/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_average_disposable_income": 1},
    other_deps={
        "_delayfixed_delayed_ts_average_disposable_income": {
            "initial": {"time_step": 1},
            "step": {"average_disposable_income": 1},
        }
    },
)
def delayed_ts_average_disposable_income():
    """
    Delayed average disposable income
    """
    return _delayfixed_delayed_ts_average_disposable_income()


_delayfixed_delayed_ts_average_disposable_income = DelayFixed(
    lambda: average_disposable_income(),
    lambda: time_step(),
    lambda: xr.DataArray(
        0, {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]}, ["REGIONS_35_I"]
    ),
    time_step,
    "_delayfixed_delayed_ts_average_disposable_income",
)


@component.add(
    name="delayed_TS_average_disposable_income_inital_year_basic_income",
    units="$/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_basic_income_sp": 1,
        "time": 1,
        "initial_year_basic_income_sp": 1,
        "aux_delayed_ts_average_disposable_income_inital_year_basic_income": 1,
        "delayed_ts_average_disposable_income": 1,
    },
)
def delayed_ts_average_disposable_income_inital_year_basic_income():
    value = xr.DataArray(
        np.nan, {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]}, ["REGIONS_35_I"]
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[_subscript_dict["REGIONS_NON_DISAGGREGATED_HH_I"]] = False
    except_subs.loc[_subscript_dict["REGIONS_DISAGGREGATED_HH_I"]] = False
    value.values[except_subs.values] = 0
    value.loc[_subscript_dict["REGIONS_DISAGGREGATED_HH_I"]] = if_then_else(
        np.logical_and(
            switch_basic_income_sp()
            .loc[_subscript_dict["REGIONS_DISAGGREGATED_HH_I"]]
            .rename({"REGIONS_35_I": "REGIONS_DISAGGREGATED_HH_I"})
            == 1,
            time() >= initial_year_basic_income_sp(),
        ),
        lambda: aux_delayed_ts_average_disposable_income_inital_year_basic_income()
        .loc[_subscript_dict["REGIONS_DISAGGREGATED_HH_I"]]
        .rename({"REGIONS_35_I": "REGIONS_DISAGGREGATED_HH_I"}),
        lambda: delayed_ts_average_disposable_income()
        .loc[_subscript_dict["REGIONS_DISAGGREGATED_HH_I"]]
        .rename({"REGIONS_35_I": "REGIONS_DISAGGREGATED_HH_I"}),
    ).values
    value.loc[_subscript_dict["REGIONS_NON_DISAGGREGATED_HH_I"]] = 0
    return value


@component.add(
    name="delayed_TS_government_debt",
    units="Mdollars",
    subscripts=["REGIONS_35_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_government_debt": 1},
    other_deps={
        "_delayfixed_delayed_ts_government_debt": {
            "initial": {"initial_delayed_government_debt": 1, "time_step": 1},
            "step": {
                "time": 1,
                "initial_delayed_government_debt": 1,
                "government_debt": 1,
            },
        }
    },
)
def delayed_ts_government_debt():
    """
    Delayed government debt.
    """
    return _delayfixed_delayed_ts_government_debt()


_delayfixed_delayed_ts_government_debt = DelayFixed(
    lambda: if_then_else(
        time() <= 2015,
        lambda: initial_delayed_government_debt(),
        lambda: government_debt(),
    ),
    lambda: time_step(),
    lambda: initial_delayed_government_debt(),
    time_step,
    "_delayfixed_delayed_ts_government_debt",
)


@component.add(
    name="delayed_TS_gross_value_added",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_gross_value_added": 1},
    other_deps={
        "_delayfixed_delayed_ts_gross_value_added": {
            "initial": {"base_gross_value_added": 1, "time_step": 1},
            "step": {"time": 1, "base_gross_value_added": 1, "gross_value_added": 1},
        }
    },
)
def delayed_ts_gross_value_added():
    """
    Delayed gross value added in current prices.
    """
    return _delayfixed_delayed_ts_gross_value_added()


_delayfixed_delayed_ts_gross_value_added = DelayFixed(
    lambda: if_then_else(
        time() <= 2015,
        lambda: base_gross_value_added(),
        lambda: gross_value_added().rename(
            {"REGIONS_35_MAP_I": "REGIONS_35_I", "SECTORS_MAP_I": "SECTORS_I"}
        ),
    ),
    lambda: time_step(),
    lambda: base_gross_value_added(),
    time_step,
    "_delayfixed_delayed_ts_gross_value_added",
)


@component.add(
    name="delayed_TS_taxes_on_resources",
    units="Mdollars/Year",
    subscripts=["MATERIALS_W_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_taxes_on_resources": 1},
    other_deps={
        "_delayfixed_delayed_ts_taxes_on_resources": {
            "initial": {"taxes_on_resources": 1, "time_step": 1},
            "step": {"taxes_on_resources": 1},
        }
    },
)
def delayed_ts_taxes_on_resources():
    """
    Delayed to avoid simoultanious equations. Tax Revenue from metals/ resources Tax. The tax revenue is collected by the countries that are extracting these materials. It is a policy variable. The idea is with increasing prices for resource extraction by imposing a tax the demand for the taxed resources will decrease
    """
    return _delayfixed_delayed_ts_taxes_on_resources()


_delayfixed_delayed_ts_taxes_on_resources = DelayFixed(
    lambda: taxes_on_resources(),
    lambda: time_step(),
    lambda: taxes_on_resources(),
    time_step,
    "_delayfixed_delayed_ts_taxes_on_resources",
)


@component.add(
    name="delayed_TS_taxes_production",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_taxes_production": 1},
    other_deps={
        "_delayfixed_delayed_ts_taxes_production": {
            "initial": {"base_taxes_production": 1, "time_step": 1},
            "step": {"time": 1, "base_taxes_production": 1, "taxes_production": 1},
        }
    },
)
def delayed_ts_taxes_production():
    """
    Delayed taxes on production.
    """
    return _delayfixed_delayed_ts_taxes_production()


_delayfixed_delayed_ts_taxes_production = DelayFixed(
    lambda: if_then_else(
        time() <= 2015, lambda: base_taxes_production(), lambda: taxes_production()
    ),
    lambda: time_step(),
    lambda: base_taxes_production(),
    time_step,
    "_delayfixed_delayed_ts_taxes_production",
)


@component.add(
    name="delayed_TS_taxes_products_by_sector",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_taxes_products_by_sector": 1},
    other_deps={
        "_delayfixed_delayed_ts_taxes_products_by_sector": {
            "initial": {"base_taxes_products_by_sector": 1, "time_step": 1},
            "step": {
                "time": 1,
                "base_taxes_products_by_sector": 1,
                "taxes_products_by_sector": 1,
            },
        }
    },
)
def delayed_ts_taxes_products_by_sector():
    """
    Delayed taxes on products by sector.
    """
    return _delayfixed_delayed_ts_taxes_products_by_sector()


_delayfixed_delayed_ts_taxes_products_by_sector = DelayFixed(
    lambda: if_then_else(
        time() <= 2015,
        lambda: base_taxes_products_by_sector(),
        lambda: taxes_products_by_sector().rename(
            {"REGIONS_35_MAP_I": "REGIONS_35_I", "SECTORS_MAP_I": "SECTORS_I"}
        ),
    ),
    lambda: time_step(),
    lambda: base_taxes_products_by_sector(),
    time_step,
    "_delayfixed_delayed_ts_taxes_products_by_sector",
)


@component.add(
    name="delayed_TS_taxes_products_final_demand",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_I", "FINAL_DEMAND_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_taxes_products_final_demand": 1},
    other_deps={
        "_delayfixed_delayed_ts_taxes_products_final_demand": {
            "initial": {"base_taxes_products_final_demand": 1, "time_step": 1},
            "step": {
                "time": 1,
                "base_taxes_products_final_demand": 1,
                "taxes_products_final_demand": 1,
            },
        }
    },
)
def delayed_ts_taxes_products_final_demand():
    """
    Delayed taxes products final demand.
    """
    return _delayfixed_delayed_ts_taxes_products_final_demand()


_delayfixed_delayed_ts_taxes_products_final_demand = DelayFixed(
    lambda: if_then_else(
        time() <= 2015,
        lambda: base_taxes_products_final_demand(),
        lambda: taxes_products_final_demand().rename(
            {"REGIONS_35_MAP_I": "REGIONS_35_I"}
        ),
    ),
    lambda: time_step(),
    lambda: base_taxes_products_final_demand(),
    time_step,
    "_delayfixed_delayed_ts_taxes_products_final_demand",
)


@component.add(
    name="GDP_objective_government_budget",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_government": 1,
        "base_initial_delayed_gdp_growth": 1,
        "base_delayed_gdp": 1,
        "delayed_gross_domestic_product": 1,
        "delayed_gdp_growth": 1,
    },
)
def gdp_objective_government_budget():
    """
    Expected GDP by the government.
    """
    return if_then_else(
        switch_eco_government() == 0,
        lambda: base_delayed_gdp() * (1 + base_initial_delayed_gdp_growth()),
        lambda: delayed_gross_domestic_product() * (1 + delayed_gdp_growth()),
    )


@component.add(
    name="government_basic_income_expenditure",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "household_basic_income": 1,
        "number_of_households_by_income_and_type": 1,
        "unit_conversion_dollars_mdollars": 1,
    },
)
def government_basic_income_expenditure():
    """
    Government basic income expenditure
    """
    return (
        sum(
            household_basic_income().rename({"HOUSEHOLDS_I": "HOUSEHOLDS_I!"})
            * number_of_households_by_income_and_type().rename(
                {"HOUSEHOLDS_I": "HOUSEHOLDS_I!"}
            ),
            dim=["HOUSEHOLDS_I!"],
        )
        / unit_conversion_dollars_mdollars()
    )


@component.add(
    name="government_budget_balance",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"government_revenue": 1, "government_expenditure": 1},
)
def government_budget_balance():
    """
    Government deficit or surplus (difference between revenue and expenditure).
    """
    return government_revenue() - government_expenditure()


@component.add(
    name="government_budget_balance_objective",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "government_budget_balance_to_gdp_objective_target": 1,
        "gdp_objective_government_budget": 1,
    },
)
def government_budget_balance_objective():
    """
    Government deficit or surplus expected by the government.
    """
    return (
        government_budget_balance_to_gdp_objective_target()
        * gdp_objective_government_budget()
    )


@component.add(
    name="government_budget_balance_to_GDP",
    units="DMNL",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"government_budget_balance": 1, "gross_domestic_product_nominal": 1},
)
def government_budget_balance_to_gdp():
    """
    Government budget balance to GDP
    """
    return zidz(government_budget_balance(), gross_domestic_product_nominal())


@component.add(
    name="government_budget_balance_to_GDP_objective_target",
    units="DMNL/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "government_budget_balance_to_gdp_objective_historic": 1,
        "switch_model_explorer": 1,
        "model_explorer_government_to_gdp_objetive": 1,
        "government_budget_balance_to_gdp_objective_target_sp": 2,
    },
)
def government_budget_balance_to_gdp_objective_target():
    """
    Government deficit or surplus to GDP objetive target.
    """
    return if_then_else(
        time() <= 2015,
        lambda: government_budget_balance_to_gdp_objective_historic(),
        lambda: if_then_else(
            switch_model_explorer() == 1,
            lambda: model_explorer_government_to_gdp_objetive()
            + government_budget_balance_to_gdp_objective_target_sp(),
            lambda: government_budget_balance_to_gdp_objective_target_sp(),
        ),
    )


@component.add(
    name="GOVERNMENT_BUDGET_BALANCE_TO_GDP_OBJECTIVE_TARGET_SP",
    units="DMNL/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_government_budget_balance_to_gdp_objective_target_sp",
        "__data__": "_ext_data_government_budget_balance_to_gdp_objective_target_sp",
        "time": 1,
    },
)
def government_budget_balance_to_gdp_objective_target_sp():
    """
    Goverment deficit or surplus to GDP objetive target.
    """
    return _ext_data_government_budget_balance_to_gdp_objective_target_sp(time())


_ext_data_government_budget_balance_to_gdp_objective_target_sp = ExtData(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "TIME_GOV_BALANCE",
    "GOVERNMENT_BUDGET_BALANCE_TO_GDP_OBJECTIVE_TARGET_SP",
    "interpolate",
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    _root,
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    "_ext_data_government_budget_balance_to_gdp_objective_target_sp",
)


@component.add(
    name="government_consumption",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "government_expenditure_objective_rest": 1,
        "share_government_expenditure_consumption_sp": 1,
    },
)
def government_consumption():
    """
    Total government consumption of goods and services.
    """
    return (
        government_expenditure_objective_rest()
        * share_government_expenditure_consumption_sp()
    )


@component.add(
    name="government_consumption_by_COFOG",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_I", "COFOG_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"government_consumption": 1, "structure_cofog_consumption_sp": 1},
)
def government_consumption_by_cofog():
    """
    Government consumption by category (COFOG classification: Classification of the Functions of the Government).
    """
    return government_consumption() * structure_cofog_consumption_sp()


@component.add(
    name="government_consumption_COFOG_adjusted",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_I", "COFOG_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "statistical_difference_government_consumption": 1,
        "government_consumption_by_cofog": 1,
    },
)
def government_consumption_cofog_adjusted():
    """
    Government consumption by category (COFOG) adjusted.
    """
    return (
        statistical_difference_government_consumption()
        * government_consumption_by_cofog()
    )


@component.add(
    name="government_consumption_purchaser_prices",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "bridge_government_consumption": 1,
        "government_consumption_cofog_adjusted": 1,
    },
)
def government_consumption_purchaser_prices():
    """
    Government consumption in purchaser prices and nominal terms.
    """
    return sum(
        bridge_government_consumption().rename({"COFOG_I": "COFOG_I!"})
        * government_consumption_cofog_adjusted().rename({"COFOG_I": "COFOG_I!"}),
        dim=["COFOG_I!"],
    )


@component.add(
    name="government_debt",
    units="Mdollars",
    subscripts=["REGIONS_35_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_government_debt": 1},
    other_deps={
        "_integ_government_debt": {
            "initial": {"initial_government_debt": 1},
            "step": {"time": 1, "change_in_government_debt": 1},
        }
    },
)
def government_debt():
    """
    Total government debt (accumulated deficit or surplus + some adjustments). * Check problems with the initial value
    """
    return _integ_government_debt()


_integ_government_debt = Integ(
    lambda: if_then_else(
        time() <= 2015,
        lambda: xr.DataArray(
            0, {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]}, ["REGIONS_35_I"]
        ),
        lambda: change_in_government_debt(),
    ),
    lambda: initial_government_debt(),
    "_integ_government_debt",
)


@component.add(
    name="government_debt_to_GDP_ratio",
    units="DMNL",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"government_debt": 1, "gross_domestic_product_nominal": 1},
)
def government_debt_to_gdp_ratio():
    """
    Ratio government debt to GDP
    """
    return zidz(government_debt(), gross_domestic_product_nominal())


@component.add(
    name="government_expenditure",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "government_consumption": 1,
        "debt_interest": 1,
        "government_investment": 1,
        "government_other_expenditures": 1,
        "government_transferences": 1,
        "social_benefits": 1,
        "government_basic_income_expenditure": 1,
    },
)
def government_expenditure():
    """
    Total government expenditure.
    """
    return (
        government_consumption()
        + debt_interest()
        + government_investment()
        + government_other_expenditures()
        + government_transferences()
        + social_benefits()
        + government_basic_income_expenditure()
    )


@component.add(
    name="government_expenditure_objective",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "government_revenue_objective": 1,
        "government_budget_balance_objective": 1,
    },
)
def government_expenditure_objective():
    """
    Government expenditure expected/desired by the government.
    """
    return government_revenue_objective() - government_budget_balance_objective()


@component.add(
    name="government_expenditure_objective_rest",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "government_expenditure_objective": 1,
        "debt_interest": 1,
        "public_gfcf_to_replace_climate_damage": 1,
    },
)
def government_expenditure_objective_rest():
    """
    Government expenditure desired adjusted taking into account some specific expenditures.
    """
    return (
        government_expenditure_objective()
        - debt_interest()
        - public_gfcf_to_replace_climate_damage()
    )


@component.add(
    name="government_investment",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "government_expenditure_objective_rest": 1,
        "share_government_expenditure_investment_sp": 1,
        "public_gfcf_to_replace_climate_damage": 1,
    },
)
def government_investment():
    """
    Government purchase of investment goods.
    """
    return (
        government_expenditure_objective_rest()
        * share_government_expenditure_investment_sp()
        + public_gfcf_to_replace_climate_damage()
    )


@component.add(
    name="government_investment_by_COFOG",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_I", "COFOG_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"government_investment": 1, "structure_cofog_investment_sp": 1},
)
def government_investment_by_cofog():
    """
    Government investment by category (COFOG classification: Classification of the Functions of the Government).
    """
    return government_investment() * structure_cofog_investment_sp()


@component.add(
    name="government_other_expenditures",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "government_expenditure_objective_rest": 1,
        "structure_government_expenditure_other_expenditures_sp": 1,
    },
)
def government_other_expenditures():
    """
    Other kind of public transferences.
    """
    return (
        government_expenditure_objective_rest()
        * structure_government_expenditure_other_expenditures_sp()
    )


@component.add(
    name="government_other_revenue",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_government": 1,
        "base_gross_value_added": 1,
        "rate_government_other_revenue_to_value_added_sp": 2,
        "delayed_ts_gross_value_added": 1,
    },
)
def government_other_revenue():
    """
    Other government revenue.
    """
    return if_then_else(
        switch_eco_government() == 0,
        lambda: rate_government_other_revenue_to_value_added_sp()
        * sum(
            base_gross_value_added().rename({"SECTORS_I": "SECTORS_I!"}),
            dim=["SECTORS_I!"],
        ),
        lambda: rate_government_other_revenue_to_value_added_sp()
        * sum(
            delayed_ts_gross_value_added().rename({"SECTORS_I": "SECTORS_I!"}),
            dim=["SECTORS_I!"],
        ),
    )


@component.add(
    name="government_property_income",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_government": 1,
        "base_gross_value_added": 1,
        "rate_government_property_income_to_value_added_sp": 2,
        "delayed_ts_gross_value_added": 1,
    },
)
def government_property_income():
    """
    Government revenue received from property income.
    """
    return if_then_else(
        switch_eco_government() == 0,
        lambda: sum(
            base_gross_value_added().rename({"SECTORS_I": "SECTORS_I!"}),
            dim=["SECTORS_I!"],
        )
        * rate_government_property_income_to_value_added_sp(),
        lambda: sum(
            delayed_ts_gross_value_added().rename({"SECTORS_I": "SECTORS_I!"}),
            dim=["SECTORS_I!"],
        )
        * rate_government_property_income_to_value_added_sp(),
    )


@component.add(
    name="government_revenue",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "government_other_revenue": 1,
        "government_property_income": 1,
        "social_security": 1,
        "taxes_on_income_and_wealth": 1,
        "net_taxes_on_production": 1,
        "net_taxes_on_products": 1,
        "taxes_on_resources_r35": 1,
    },
)
def government_revenue():
    """
    Total government revenue.
    """
    return (
        government_other_revenue()
        + government_property_income()
        + social_security()
        + taxes_on_income_and_wealth()
        + net_taxes_on_production()
        + net_taxes_on_products()
        + sum(
            taxes_on_resources_r35().rename({"MATERIALS_W_I": "MATERIALS_W_I!"}),
            dim=["MATERIALS_W_I!"],
        )
    )


@component.add(
    name="government_revenue_objective",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "delayed_government_revenue_to_gdp": 1,
        "gdp_objective_government_budget": 1,
    },
)
def government_revenue_objective():
    """
    Government revenue expected by the government.
    """
    return delayed_government_revenue_to_gdp() * gdp_objective_government_budget()


@component.add(
    name="government_revenue_to_GDP",
    units="DMNL",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "government_revenue": 1,
        "government_basic_income_expenditure": 1,
        "base_gross_domestic_product": 1,
        "gross_domestic_product_nominal": 1,
        "switch_eco_government": 1,
    },
)
def government_revenue_to_gdp():
    """
    Ratio government revenue to GDP.
    """
    return zidz(
        government_revenue() - government_basic_income_expenditure(),
        if_then_else(
            switch_eco_government() == 0,
            lambda: base_gross_domestic_product(),
            lambda: gross_domestic_product_nominal(),
        ),
    )


@component.add(
    name="government_transferences",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "government_expenditure_objective_rest": 1,
        "share_government_expenditure_transferences_sp": 1,
    },
)
def government_transferences():
    """
    Government expenditures for tranferences (such as income distribution, etc.)
    """
    return (
        government_expenditure_objective_rest()
        * share_government_expenditure_transferences_sp()
    )


@component.add(
    name="gross_domestic_product_growth",
    units="DMNL/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "gross_domestic_product_nominal": 1,
        "delayed_gross_domestic_product": 2,
    },
)
def gross_domestic_product_growth():
    """
    GDP growth in current prices
    """
    return (
        gross_domestic_product_nominal() - delayed_gross_domestic_product()
    ) / delayed_gross_domestic_product()


@component.add(
    name="household_basic_income",
    units="$/Year",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_basic_income_sp": 1,
        "time": 1,
        "initial_year_basic_income_sp": 1,
        "ratio_basic_income_to_average_disposable_income_sp": 1,
        "delayed_ts_average_disposable_income": 1,
    },
)
def household_basic_income():
    """
    IF THEN ELSE(Time>YEAR ACTIVATE BASIC INCOME SP,delayed TS average disposable income[REGIONS 35 I]*SHARE AVERAGE DISPOSABLE INCOME BASIC INCOME SP ,0)*ACTIVATE BASIC INCOME SP
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
        },
        ["REGIONS_35_I", "HOUSEHOLDS_I"],
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[_subscript_dict["REGIONS_NON_DISAGGREGATED_HH_I"], :] = False
    except_subs.loc[
        _subscript_dict["REGIONS_DISAGGREGATED_HH_I"], ["REPRESENTATIVE_HOUSEHOLD"]
    ] = False
    except_subs.loc[
        _subscript_dict["REGIONS_DISAGGREGATED_HH_I"],
        _subscript_dict["HOUSEHOLDS_EU27_I"],
    ] = False
    value.values[except_subs.values] = 0
    value.loc[_subscript_dict["REGIONS_NON_DISAGGREGATED_HH_I"], :] = 0
    value.loc[
        _subscript_dict["REGIONS_DISAGGREGATED_HH_I"], ["REPRESENTATIVE_HOUSEHOLD"]
    ] = 0
    value.loc[
        _subscript_dict["REGIONS_DISAGGREGATED_HH_I"],
        _subscript_dict["HOUSEHOLDS_EU27_I"],
    ] = (
        if_then_else(
            np.logical_and(
                switch_basic_income_sp()
                .loc[_subscript_dict["REGIONS_DISAGGREGATED_HH_I"]]
                .rename({"REGIONS_35_I": "REGIONS_DISAGGREGATED_HH_I"})
                == 1,
                time() > initial_year_basic_income_sp(),
            ),
            lambda: delayed_ts_average_disposable_income()
            .loc[_subscript_dict["REGIONS_DISAGGREGATED_HH_I"]]
            .rename({"REGIONS_35_I": "REGIONS_DISAGGREGATED_HH_I"})
            * ratio_basic_income_to_average_disposable_income_sp(),
            lambda: xr.DataArray(
                0,
                {
                    "REGIONS_DISAGGREGATED_HH_I": _subscript_dict[
                        "REGIONS_DISAGGREGATED_HH_I"
                    ]
                },
                ["REGIONS_DISAGGREGATED_HH_I"],
            ),
        )
        .expand_dims({"HOUSEHOLDS_EU27_I": _subscript_dict["HOUSEHOLDS_EU27_I"]}, 1)
        .values
    )
    return value


@component.add(
    name="implicit_tax_income_corportations_to_finance_basic_income",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "tax_income_corportations_to_finance_basic_income": 1,
        "delayed_ts_net_operating_surplus_total": 1,
    },
)
def implicit_tax_income_corportations_to_finance_basic_income():
    return zidz(
        tax_income_corportations_to_finance_basic_income(),
        delayed_ts_net_operating_surplus_total(),
    )


@component.add(
    name="INITIAL_YEAR_BASIC_INCOME_SP",
    units="DMNL",
    subscripts=["REGIONS_DISAGGREGATED_HH_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_year_basic_income_sp"},
)
def initial_year_basic_income_sp():
    return _ext_constant_initial_year_basic_income_sp()


_ext_constant_initial_year_basic_income_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "INITIAL_YEAR_BASIC_INCOME_SP*",
    {"REGIONS_DISAGGREGATED_HH_I": _subscript_dict["REGIONS_DISAGGREGATED_HH_I"]},
    _root,
    {"REGIONS_DISAGGREGATED_HH_I": _subscript_dict["REGIONS_DISAGGREGATED_HH_I"]},
    "_ext_constant_initial_year_basic_income_sp",
)


@component.add(
    name="INITIAL_YEAR_DEBT_INTEREST_RATE_TARGET_SP",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_initial_year_debt_interest_rate_target_sp"
    },
)
def initial_year_debt_interest_rate_target_sp():
    """
    Initial year debt interest rate target.
    """
    return _ext_constant_initial_year_debt_interest_rate_target_sp()


_ext_constant_initial_year_debt_interest_rate_target_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "INITIAL_YEAR_DEBT_INTEREST_RATE_TARGET_SP",
    {},
    _root,
    {},
    "_ext_constant_initial_year_debt_interest_rate_target_sp",
)


@component.add(
    name="net_taxes_on_production",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_government": 1,
        "statistical_difference_net_taxes_production": 2,
        "base_taxes_production": 1,
        "delayed_ts_taxes_production": 1,
    },
)
def net_taxes_on_production():
    """
    Net taxes on production.
    """
    return if_then_else(
        switch_eco_government() == 0,
        lambda: sum(
            base_taxes_production().rename({"SECTORS_I": "SECTORS_I!"}),
            dim=["SECTORS_I!"],
        )
        + statistical_difference_net_taxes_production(),
        lambda: sum(
            delayed_ts_taxes_production().rename({"SECTORS_I": "SECTORS_I!"}),
            dim=["SECTORS_I!"],
        )
        + statistical_difference_net_taxes_production(),
    )


@component.add(
    name="net_taxes_on_products",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"statistical_difference_net_taxes_products": 1, "taxes_products": 1},
)
def net_taxes_on_products():
    """
    Net taxed on products.
    """
    return statistical_difference_net_taxes_products() + taxes_products()


@component.add(
    name="RATIO_BASIC_INCOME_TO_AVERAGE_DISPOSABLE_INCOME_SP",
    units="DMNL",
    subscripts=["REGIONS_DISAGGREGATED_HH_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_ratio_basic_income_to_average_disposable_income_sp"
    },
)
def ratio_basic_income_to_average_disposable_income_sp():
    """
    Ratio of basic income to average disposable income
    """
    return _ext_constant_ratio_basic_income_to_average_disposable_income_sp()


_ext_constant_ratio_basic_income_to_average_disposable_income_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "RATIO_BASIC_INCOME_TO_AVERAGE_DISPOSABLE_INCOME_SP*",
    {"REGIONS_DISAGGREGATED_HH_I": _subscript_dict["REGIONS_DISAGGREGATED_HH_I"]},
    _root,
    {"REGIONS_DISAGGREGATED_HH_I": _subscript_dict["REGIONS_DISAGGREGATED_HH_I"]},
    "_ext_constant_ratio_basic_income_to_average_disposable_income_sp",
)


@component.add(
    name="social_benefits",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "government_expenditure_objective_rest": 1,
        "share_government_expenditure_social_benefits_sp": 1,
    },
)
def social_benefits():
    """
    Social benefits paid by the government (such as pensions and payments for umemployed people). *CHECK: This part is going to change when the model is integrated (see D9.2). it will be calculated taking into account variables that come from the sociodemographic and household module.
    """
    return (
        government_expenditure_objective_rest()
        * share_government_expenditure_social_benefits_sp()
    )


@component.add(
    name="social_security",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_government": 1,
        "rate_social_security_sp": 1,
        "base_labour_compensation": 1,
        "unit_conversion_dollars_mdollars": 1,
        "households_social_security": 1,
        "number_of_households_by_income_and_type": 1,
    },
)
def social_security():
    """
    Social security contributions.
    """
    return if_then_else(
        switch_eco_government() == 0,
        lambda: rate_social_security_sp()
        * sum(
            base_labour_compensation().rename({"SECTORS_I": "SECTORS_I!"}),
            dim=["SECTORS_I!"],
        ),
        lambda: sum(
            households_social_security().rename({"HOUSEHOLDS_I": "HOUSEHOLDS_I!"})
            * number_of_households_by_income_and_type().rename(
                {"HOUSEHOLDS_I": "HOUSEHOLDS_I!"}
            )
            / unit_conversion_dollars_mdollars(),
            dim=["HOUSEHOLDS_I!"],
        ),
    )


@component.add(
    name="SWITCH_BASIC_INCOME_SP",
    subscripts=["REGIONS_35_I"],
    comp_type="Constant",
    comp_subtype="External, Normal",
    depends_on={"__external__": "_ext_constant_switch_basic_income_sp"},
)
def switch_basic_income_sp():
    value = xr.DataArray(
        np.nan, {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]}, ["REGIONS_35_I"]
    )
    def_subs = xr.zeros_like(value, dtype=bool)
    def_subs.loc[
        [
            "BELGIUM",
            "BULGARIA",
            "CROATIA",
            "CYPRUS",
            "CZECH_REPUBLIC",
            "DENMARK",
            "ESTONIA",
            "FINLAND",
            "FRANCE",
            "GERMANY",
            "GREECE",
            "HUNGARY",
            "IRELAND",
            "LATVIA",
            "LITHUANIA",
            "LUXEMBOURG",
            "POLAND",
            "PORTUGAL",
            "SLOVAKIA",
            "SPAIN",
            "SWEDEN",
        ]
    ] = True
    value.values[def_subs.values] = _ext_constant_switch_basic_income_sp().values[
        def_subs.values
    ]
    value.loc[_subscript_dict["REGIONS_NON_DISAGGREGATED_HH_I"]] = 0
    return value


_ext_constant_switch_basic_income_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "SWITCH_BASIC_INCOME_SP*",
    {"REGIONS_35_I": _subscript_dict["REGIONS_DISAGGREGATED_HH_I"]},
    _root,
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    "_ext_constant_switch_basic_income_sp",
)


@component.add(
    name="SWITCH_ECO_GOVERNMENT",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_eco_government"},
)
def switch_eco_government():
    """
    This switch can take two values: 0: the (sub)module runs isolated from the rest of WILIAM, replacing inter(sub)module variables with exogenous parameters. 1: the (sub)module runs integrated with the rest of WILIAM.
    """
    return _ext_constant_switch_eco_government()


_ext_constant_switch_eco_government = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_ECO_GOVERNMENT",
    {},
    _root,
    {},
    "_ext_constant_switch_eco_government",
)


@component.add(
    name="tax_income_corporations",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_government": 1,
        "initial_delayed_net_operating_surplus": 1,
        "tax_rate_on_profits": 3,
        "tax_income_corportations_to_finance_basic_income": 1,
        "delayed_ts_net_operating_surplus_total": 2,
        "select_policy_finance_basic_income_sp": 1,
    },
)
def tax_income_corporations():
    """
    Total taxes on corporations profits.
    """
    return if_then_else(
        switch_eco_government() == 0,
        lambda: sum(
            initial_delayed_net_operating_surplus().rename({"SECTORS_I": "SECTORS_I!"}),
            dim=["SECTORS_I!"],
        )
        * tax_rate_on_profits(),
        lambda: if_then_else(
            select_policy_finance_basic_income_sp() == 1,
            lambda: delayed_ts_net_operating_surplus_total() * tax_rate_on_profits()
            + tax_income_corportations_to_finance_basic_income(),
            lambda: delayed_ts_net_operating_surplus_total() * tax_rate_on_profits(),
        ),
    )


@component.add(
    name="tax_income_corportations_to_finance_basic_income",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"government_basic_income_expenditure": 1},
)
def tax_income_corportations_to_finance_basic_income():
    return government_basic_income_expenditure()


@component.add(
    name="taxes_on_income",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_government": 1,
        "base_taxes_on_income_hh": 1,
        "unit_conversion_dollars_mdollars": 1,
        "households_income_tax": 1,
        "number_of_households_by_income_and_type": 1,
    },
)
def taxes_on_income():
    """
    Total of taxes on income.
    """
    return if_then_else(
        switch_eco_government() == 0,
        lambda: base_taxes_on_income_hh(),
        lambda: sum(
            households_income_tax().rename({"HOUSEHOLDS_I": "HOUSEHOLDS_I!"})
            * number_of_households_by_income_and_type().rename(
                {"HOUSEHOLDS_I": "HOUSEHOLDS_I!"}
            ),
            dim=["HOUSEHOLDS_I!"],
        )
        / unit_conversion_dollars_mdollars(),
    )


@component.add(
    name="taxes_on_income_and_wealth",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "tax_income_corporations": 1,
        "taxes_on_income": 1,
        "taxes_on_wealth": 1,
    },
)
def taxes_on_income_and_wealth():
    """
    Total of taxes on income and wealth.
    """
    return tax_income_corporations() + taxes_on_income() + taxes_on_wealth()


@component.add(
    name="taxes_on_resources_R35",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_I", "MATERIALS_W_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"delayed_ts_taxes_on_resources": 7, "delayed_ts_output_real": 14},
)
def taxes_on_resources_r35():
    """
    Split into the different regions according to the share of production in the base year. Tax Revenue from metals/ resources Tax. The tax revenue is collected by the countries that are extracting these materials. It is a policy variable. The idea is with increasing prices for resource extraction by imposing a tax the demand for the taxed resources will decrease
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "MATERIALS_W_I": _subscript_dict["MATERIALS_W_I"],
        },
        ["REGIONS_35_I", "MATERIALS_W_I"],
    )
    value.loc[:, ["Oil_W"]] = (
        (
            float(delayed_ts_taxes_on_resources().loc["Oil_W"])
            * delayed_ts_output_real().loc[:, "EXTRACTION_OIL"].reset_coords(drop=True)
            / sum(
                delayed_ts_output_real()
                .loc[:, "EXTRACTION_OIL"]
                .reset_coords(drop=True)
                .rename({"REGIONS_35_I": "REGIONS_35_I!"}),
                dim=["REGIONS_35_I!"],
            )
        )
        .expand_dims({"HYDROCARBONS_W_I": ["Oil_W"]}, 1)
        .values
    )
    value.loc[:, ["Gas_W"]] = (
        (
            float(delayed_ts_taxes_on_resources().loc["Gas_W"])
            * delayed_ts_output_real().loc[:, "EXTRACTION_GAS"].reset_coords(drop=True)
            / sum(
                delayed_ts_output_real()
                .loc[:, "EXTRACTION_GAS"]
                .reset_coords(drop=True)
                .rename({"REGIONS_35_I": "REGIONS_35_I!"}),
                dim=["REGIONS_35_I!"],
            )
        )
        .expand_dims({"HYDROCARBONS_W_I": ["Gas_W"]}, 1)
        .values
    )
    value.loc[:, ["Coal_W"]] = (
        (
            float(delayed_ts_taxes_on_resources().loc["Coal_W"])
            * delayed_ts_output_real().loc[:, "MINING_COAL"].reset_coords(drop=True)
            / sum(
                delayed_ts_output_real()
                .loc[:, "MINING_COAL"]
                .reset_coords(drop=True)
                .rename({"REGIONS_35_I": "REGIONS_35_I!"}),
                dim=["REGIONS_35_I!"],
            )
        )
        .expand_dims({"HYDROCARBONS_W_I": ["Coal_W"]}, 1)
        .values
    )
    value.loc[:, ["Cu_W"]] = (
        (
            float(delayed_ts_taxes_on_resources().loc["Cu_W"])
            * delayed_ts_output_real()
            .loc[:, "MINING_AND_MANUFACTURING_COPPER"]
            .reset_coords(drop=True)
            / sum(
                delayed_ts_output_real()
                .loc[:, "MINING_AND_MANUFACTURING_COPPER"]
                .reset_coords(drop=True)
                .rename({"REGIONS_35_I": "REGIONS_35_I!"}),
                dim=["REGIONS_35_I!"],
            )
        )
        .expand_dims({"MATERIALS_W_I": ["Cu_W"]}, 1)
        .values
    )
    value.loc[:, ["Al_W"]] = (
        (
            float(delayed_ts_taxes_on_resources().loc["Al_W"])
            * delayed_ts_output_real()
            .loc[:, "MINING_AND_MANUFACTURING_ALUMINIUM"]
            .reset_coords(drop=True)
            / sum(
                delayed_ts_output_real()
                .loc[:, "MINING_AND_MANUFACTURING_ALUMINIUM"]
                .reset_coords(drop=True)
                .rename({"REGIONS_35_I": "REGIONS_35_I!"}),
                dim=["REGIONS_35_I!"],
            )
        )
        .expand_dims({"MATERIALS_W_I": ["Al_W"]}, 1)
        .values
    )
    value.loc[:, ["Fe_W"]] = (
        (
            float(delayed_ts_taxes_on_resources().loc["Fe_W"])
            * delayed_ts_output_real()
            .loc[:, "MINING_AND_MANUFACTURING_IRON"]
            .reset_coords(drop=True)
            / sum(
                delayed_ts_output_real()
                .loc[:, "MINING_AND_MANUFACTURING_IRON"]
                .reset_coords(drop=True)
                .rename({"REGIONS_35_I": "REGIONS_35_I!"}),
                dim=["REGIONS_35_I!"],
            )
        )
        .expand_dims({"MATERIALS_W_I": ["Fe_W"]}, 1)
        .values
    )
    value.loc[:, ["Ni_W"]] = (
        (
            float(delayed_ts_taxes_on_resources().loc["Ni_W"])
            * delayed_ts_output_real()
            .loc[:, "MINING_AND_MANUFACTURING_NICKEL"]
            .reset_coords(drop=True)
            / sum(
                delayed_ts_output_real()
                .loc[:, "MINING_AND_MANUFACTURING_NICKEL"]
                .reset_coords(drop=True)
                .rename({"REGIONS_35_I": "REGIONS_35_I!"}),
                dim=["REGIONS_35_I!"],
            )
        )
        .expand_dims({"MATERIALS_W_I": ["Ni_W"]}, 1)
        .values
    )
    return value


@component.add(
    name="taxes_on_wealth",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_government": 1,
        "base_taxes_on_wealth": 1,
        "unit_conversion_dollars_mdollars": 1,
        "households_wealth_tax": 1,
        "number_of_households_by_income_and_type": 1,
    },
)
def taxes_on_wealth():
    """
    Total of taxes on wealth. SUM(delayed_wealth[REGIONS_35_I,HOUSEHOLDS_EU27_I!]*TAX_RATE_ON_WEALTH[REGI ONS_35_I,HOUSEHOLDS_EU27_I!])
    """
    return if_then_else(
        switch_eco_government() == 0,
        lambda: base_taxes_on_wealth(),
        lambda: sum(
            households_wealth_tax().rename({"HOUSEHOLDS_I": "HOUSEHOLDS_I!"})
            * number_of_households_by_income_and_type().rename(
                {"HOUSEHOLDS_I": "HOUSEHOLDS_I!"}
            ),
            dim=["HOUSEHOLDS_I!"],
        )
        / unit_conversion_dollars_mdollars(),
    )


@component.add(
    name="taxes_products",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_government": 1,
        "base_taxes_products_by_sector": 1,
        "base_taxes_products_final_demand": 1,
        "delayed_ts_taxes_products_by_sector": 1,
        "delayed_ts_taxes_products_final_demand": 1,
    },
)
def taxes_products():
    """
    Taxes on products.
    """
    return if_then_else(
        switch_eco_government() == 0,
        lambda: sum(
            base_taxes_products_final_demand().rename(
                {"FINAL_DEMAND_I": "FINAL_DEMAND_I!"}
            ),
            dim=["FINAL_DEMAND_I!"],
        )
        + sum(
            base_taxes_products_by_sector().rename({"SECTORS_I": "SECTORS_I!"}),
            dim=["SECTORS_I!"],
        ),
        lambda: sum(
            delayed_ts_taxes_products_final_demand().rename(
                {"FINAL_DEMAND_I": "FINAL_DEMAND_I!"}
            ),
            dim=["FINAL_DEMAND_I!"],
        )
        + sum(
            delayed_ts_taxes_products_by_sector().rename({"SECTORS_I": "SECTORS_I!"}),
            dim=["SECTORS_I!"],
        ),
    )
