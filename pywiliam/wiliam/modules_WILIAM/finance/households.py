"""
Module finance.households
Translated using PySD version 3.10.0
"""


@component.add(
    name="AUX_BASIC_INCOME_TAX_PAYERS_SP",
    subscripts=["HOUSEHOLDS_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={"basic_income_tax_payers_sp": 1},
)
def aux_basic_income_tax_payers_sp():
    value = xr.DataArray(
        np.nan, {"HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"]}, ["HOUSEHOLDS_I"]
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[_subscript_dict["HOUSEHOLDS_EU27_I"]] = False
    except_subs.loc[["REPRESENTATIVE_HOUSEHOLD"]] = False
    value.values[except_subs.values] = 0
    value.loc[
        _subscript_dict["HOUSEHOLDS_EU27_I"]
    ] = basic_income_tax_payers_sp().values
    value.loc[["REPRESENTATIVE_HOUSEHOLD"]] = 0
    return value


@component.add(
    name="average_households_real_net_wealth_9R",
    units="dollars_2015",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "households_net_wealth": 1,
        "consumer_price_index": 1,
        "average_households_real_net_wealth_eu27": 1,
    },
)
def average_households_real_net_wealth_9r():
    """
    average_households_real_net_wealth_9R
    """
    value = xr.DataArray(
        np.nan, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
    )
    value.loc[_subscript_dict["REGIONS_8_I"]] = sum(
        households_net_wealth()
        .loc[_subscript_dict["REGIONS_8_I"], :]
        .rename({"REGIONS_35_I": "REGIONS_8_I", "HOUSEHOLDS_I": "HOUSEHOLDS_I!"})
        * zidz(
            xr.DataArray(
                100, {"REGIONS_8_I": _subscript_dict["REGIONS_8_I"]}, ["REGIONS_8_I"]
            ),
            consumer_price_index()
            .loc[_subscript_dict["REGIONS_8_I"]]
            .rename({"REGIONS_35_I": "REGIONS_8_I"}),
        ),
        dim=["HOUSEHOLDS_I!"],
    ).values
    value.loc[["EU27"]] = average_households_real_net_wealth_eu27()
    return value


@component.add(
    name="average_households_real_net_wealth_EU27",
    units="$_2015",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "households_net_wealth": 2,
        "base_number_of_households": 1,
        "consumer_price_index": 2,
        "number_of_households_by_income_and_type": 3,
    },
)
def average_households_real_net_wealth_eu27():
    """
    ZIDZ(SUM(households_net_wealth[REGIONS_EU27_I!,HOUSEHOLDS_I!]*ZIDZ(100,consumer_price _index[REGIONS_EU27_I!])*number_of_households_by_income_and_type[REGIONS_EU 27_I!,HOUSEHOLDS_I !]),SUM(number_of_households_by_income_and_type[REGIONS_EU27_I!,HOUSEHOLDS_ I!]))
    """
    return if_then_else(
        time() < 2015,
        lambda: zidz(
            sum(
                households_net_wealth()
                .loc[_subscript_dict["REGIONS_EU27_I"], :]
                .rename(
                    {"REGIONS_35_I": "REGIONS_EU27_I!", "HOUSEHOLDS_I": "HOUSEHOLDS_I!"}
                )
                * zidz(
                    xr.DataArray(
                        100,
                        {
                            "REGIONS_EU27_I!": [
                                "AUSTRIA",
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
                                "ITALY",
                                "LATVIA",
                                "LITHUANIA",
                                "LUXEMBOURG",
                                "MALTA",
                                "NETHERLANDS",
                                "POLAND",
                                "PORTUGAL",
                                "ROMANIA",
                                "SLOVAKIA",
                                "SLOVENIA",
                                "SPAIN",
                                "SWEDEN",
                            ]
                        },
                        ["REGIONS_EU27_I!"],
                    ),
                    consumer_price_index()
                    .loc[_subscript_dict["REGIONS_EU27_I"]]
                    .rename({"REGIONS_35_I": "REGIONS_EU27_I!"}),
                )
                * number_of_households_by_income_and_type()
                .loc[_subscript_dict["REGIONS_EU27_I"], :]
                .rename(
                    {"REGIONS_35_I": "REGIONS_EU27_I!", "HOUSEHOLDS_I": "HOUSEHOLDS_I!"}
                ),
                dim=["REGIONS_EU27_I!", "HOUSEHOLDS_I!"],
            ),
            sum(
                base_number_of_households()
                .loc[_subscript_dict["REGIONS_EU27_I"], :]
                .rename(
                    {"REGIONS_35_I": "REGIONS_EU27_I!", "HOUSEHOLDS_I": "HOUSEHOLDS_I!"}
                ),
                dim=["REGIONS_EU27_I!", "HOUSEHOLDS_I!"],
            ),
        ),
        lambda: zidz(
            sum(
                households_net_wealth()
                .loc[_subscript_dict["REGIONS_EU27_I"], :]
                .rename(
                    {"REGIONS_35_I": "REGIONS_EU27_I!", "HOUSEHOLDS_I": "HOUSEHOLDS_I!"}
                )
                * zidz(
                    xr.DataArray(
                        100,
                        {
                            "REGIONS_EU27_I!": [
                                "AUSTRIA",
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
                                "ITALY",
                                "LATVIA",
                                "LITHUANIA",
                                "LUXEMBOURG",
                                "MALTA",
                                "NETHERLANDS",
                                "POLAND",
                                "PORTUGAL",
                                "ROMANIA",
                                "SLOVAKIA",
                                "SLOVENIA",
                                "SPAIN",
                                "SWEDEN",
                            ]
                        },
                        ["REGIONS_EU27_I!"],
                    ),
                    consumer_price_index()
                    .loc[_subscript_dict["REGIONS_EU27_I"]]
                    .rename({"REGIONS_35_I": "REGIONS_EU27_I!"}),
                )
                * number_of_households_by_income_and_type()
                .loc[_subscript_dict["REGIONS_EU27_I"], :]
                .rename(
                    {"REGIONS_35_I": "REGIONS_EU27_I!", "HOUSEHOLDS_I": "HOUSEHOLDS_I!"}
                ),
                dim=["REGIONS_EU27_I!", "HOUSEHOLDS_I!"],
            ),
            sum(
                number_of_households_by_income_and_type()
                .loc[_subscript_dict["REGIONS_EU27_I"], :]
                .rename(
                    {"REGIONS_35_I": "REGIONS_EU27_I!", "HOUSEHOLDS_I": "HOUSEHOLDS_I!"}
                ),
                dim=["REGIONS_EU27_I!", "HOUSEHOLDS_I!"],
            ),
        ),
    )


@component.add(
    name="BASIC_INCOME_TAX_PAYERS_SP",
    subscripts=["HOUSEHOLDS_EU27_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_basic_income_tax_payers_sp"},
)
def basic_income_tax_payers_sp():
    """
    Vector of ones for selecting those households paying taxed to finance basic income
    """
    return _ext_constant_basic_income_tax_payers_sp()


_ext_constant_basic_income_tax_payers_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "BASIC_INCOME_TAX_PAYERS_SP*",
    {"HOUSEHOLDS_EU27_I": _subscript_dict["HOUSEHOLDS_EU27_I"]},
    _root,
    {"HOUSEHOLDS_EU27_I": _subscript_dict["HOUSEHOLDS_EU27_I"]},
    "_ext_constant_basic_income_tax_payers_sp",
)


@component.add(
    name="decrease_in_households_capital_stock_due_to_depreciation",
    units="$/Year",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"depreciation_rate": 1, "households_capital_stock": 1},
)
def decrease_in_households_capital_stock_due_to_depreciation():
    """
    Decrease in households capital stock due to depreciation.
    """
    return (
        depreciation_rate().loc[:, "REAL_ESTATE"].reset_coords(drop=True)
        * households_capital_stock()
    )


@component.add(
    name="delayed_households_taxes_on_assets_to_finance_basic_income",
    units="$",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={
        "_delayfixed_delayed_households_taxes_on_assets_to_finance_basic_income": 1
    },
    other_deps={
        "_delayfixed_delayed_households_taxes_on_assets_to_finance_basic_income": {
            "initial": {"time_step": 1},
            "step": {"households_taxes_on_assets_to_finance_basic_income": 1},
        }
    },
)
def delayed_households_taxes_on_assets_to_finance_basic_income():
    """
    Delayed taxes on financial assets to finance basic income paid by each household
    """
    return _delayfixed_delayed_households_taxes_on_assets_to_finance_basic_income()


_delayfixed_delayed_households_taxes_on_assets_to_finance_basic_income = DelayFixed(
    lambda: households_taxes_on_assets_to_finance_basic_income(),
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
    "_delayfixed_delayed_households_taxes_on_assets_to_finance_basic_income",
)


@component.add(
    name="delayed_TS_households_financial_assets",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_households_financial_assets": 1},
    other_deps={
        "_delayfixed_delayed_ts_households_financial_assets": {
            "initial": {"initial_households_financial_assets": 1, "time_step": 1},
            "step": {"households_financial_assets": 1},
        }
    },
)
def delayed_ts_households_financial_assets():
    return _delayfixed_delayed_ts_households_financial_assets()


_delayfixed_delayed_ts_households_financial_assets = DelayFixed(
    lambda: households_financial_assets(),
    lambda: time_step(),
    lambda: initial_households_financial_assets(),
    time_step,
    "_delayfixed_delayed_ts_households_financial_assets",
)


@component.add(
    name="delayed_TS_households_net_lending",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_households_net_lending": 1},
    other_deps={
        "_delayfixed_delayed_ts_households_net_lending": {
            "initial": {"time_step": 1},
            "step": {"households_net_lending": 1},
        }
    },
)
def delayed_ts_households_net_lending():
    return _delayfixed_delayed_ts_households_net_lending()


_delayfixed_delayed_ts_households_net_lending = DelayFixed(
    lambda: households_net_lending(),
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
    "_delayfixed_delayed_ts_households_net_lending",
)


@component.add(
    name="households_capital_stock",
    units="$",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_households_capital_stock": 1},
    other_deps={
        "_integ_households_capital_stock": {
            "initial": {
                "initial_households_capital_stock": 1,
                "base_number_of_households": 1,
            },
            "step": {
                "time": 1,
                "decrease_in_households_capital_stock_due_to_depreciation": 1,
                "increase_in_households_capital_stock_due_to_investments": 1,
                "variation_in_households_capital_stock_due_to_revalorizations": 1,
            },
        }
    },
)
def households_capital_stock():
    """
    Households capital stock, mainly housing.
    """
    return _integ_households_capital_stock()


_integ_households_capital_stock = Integ(
    lambda: if_then_else(
        time() < 2015,
        lambda: xr.DataArray(
            0,
            {
                "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
            },
            ["REGIONS_35_I", "HOUSEHOLDS_I"],
        ),
        lambda: increase_in_households_capital_stock_due_to_investments()
        + variation_in_households_capital_stock_due_to_revalorizations()
        - decrease_in_households_capital_stock_due_to_depreciation(),
    ),
    lambda: zidz(initial_households_capital_stock(), base_number_of_households()),
    "_integ_households_capital_stock",
)


@component.add(
    name="households_financial_assets",
    units="$",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_households_financial_assets": 1},
    other_deps={
        "_integ_households_financial_assets": {
            "initial": {
                "initial_households_financial_assets": 1,
                "base_number_of_households": 1,
            },
            "step": {
                "time": 1,
                "variation_in_households_financial_assets_due_to_net_lending": 1,
            },
        }
    },
)
def households_financial_assets():
    """
    Total households financial assets.
    """
    return _integ_households_financial_assets()


_integ_households_financial_assets = Integ(
    lambda: if_then_else(
        time() < 2015,
        lambda: xr.DataArray(
            0,
            {
                "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
            },
            ["REGIONS_35_I", "HOUSEHOLDS_I"],
        ),
        lambda: variation_in_households_financial_assets_due_to_net_lending(),
    ),
    lambda: zidz(initial_households_financial_assets(), base_number_of_households()),
    "_integ_households_financial_assets",
)


@component.add(
    name="households_financial_liabilities",
    units="$",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_households_financial_liabilities": 1},
    other_deps={
        "_integ_households_financial_liabilities": {
            "initial": {
                "initial_households_financial_liabilities": 1,
                "base_number_of_households": 1,
            },
            "step": {"time": 1, "variation_in_households_financial_liabilities": 1},
        }
    },
)
def households_financial_liabilities():
    """
    Total households financial liabilities.
    """
    return _integ_households_financial_liabilities()


_integ_households_financial_liabilities = Integ(
    lambda: if_then_else(
        time() < 2015,
        lambda: xr.DataArray(
            0,
            {
                "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
            },
            ["REGIONS_35_I", "HOUSEHOLDS_I"],
        ),
        lambda: variation_in_households_financial_liabilities(),
    ),
    lambda: zidz(
        initial_households_financial_liabilities(), base_number_of_households()
    ),
    "_integ_households_financial_liabilities",
)


@component.add(
    name="households_net_lending",
    units="$/Year",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_finance": 1,
        "increase_in_households_capital_stock_due_to_investments": 2,
        "initial_gross_savings": 1,
        "households_gross_savings": 1,
    },
)
def households_net_lending():
    """
    Amount of money that households can use to buy financial assets or cancel their liabilities.
    """
    return if_then_else(
        switch_finance() == 0,
        lambda: initial_gross_savings()
        - increase_in_households_capital_stock_due_to_investments(),
        lambda: households_gross_savings()
        - increase_in_households_capital_stock_due_to_investments(),
    )


@component.add(
    name="households_net_wealth",
    units="$",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "households_capital_stock": 1,
        "households_financial_assets": 1,
        "households_financial_liabilities": 1,
    },
)
def households_net_wealth():
    """
    Total assets minus total liabilities of households.
    """
    return (
        households_capital_stock()
        + households_financial_assets()
        - households_financial_liabilities()
    )


@component.add(
    name="households_property_income_paid",
    units="$/Year",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "households_financial_liabilities": 1,
        "interest_rate_for_households_liabilities": 1,
    },
)
def households_property_income_paid():
    """
    Households property income paid by household type.
    """
    return (
        households_financial_liabilities() * interest_rate_for_households_liabilities()
    )


@component.add(
    name="households_property_income_received",
    units="$/Year",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "households_financial_assets": 1,
        "households_capital_stock": 1,
        "interest_rate_for_households_assets": 1,
    },
)
def households_property_income_received():
    """
    Households property income received by household type.
    """
    return (
        households_financial_assets() + households_capital_stock()
    ) * interest_rate_for_households_assets()


@component.add(
    name="households_taxes_on_assets_to_finance_basic_income",
    units="$",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "taxes_on_assets_to_finance_basic_income_by_household_group": 1,
        "unit_conversion_dollars_mdollars": 1,
        "number_of_households_by_income_and_type": 1,
    },
)
def households_taxes_on_assets_to_finance_basic_income():
    """
    Taxes on financial assets to finance basic income paid by each household
    """
    return zidz(
        taxes_on_assets_to_finance_basic_income_by_household_group()
        * unit_conversion_dollars_mdollars(),
        number_of_households_by_income_and_type(),
    )


@component.add(
    name="implicit_tax_rate_to_finance_basic_income",
    units="DMNL",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "households_taxes_on_assets_to_finance_basic_income": 1,
        "households_financial_assets": 1,
    },
)
def implicit_tax_rate_to_finance_basic_income():
    return zidz(
        households_taxes_on_assets_to_finance_basic_income(),
        households_financial_assets(),
    )


@component.add(
    name="increase_in_households_capital_stock_due_to_investments",
    units="$/Year",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "price_transformation": 2,
        "unit_conversion_dollars_mdollars": 2,
        "households_financial_assets": 4,
        "price_gfcf": 2,
        "gross_fixed_capital_formation_real": 2,
        "base_number_of_households": 3,
        "number_of_households_by_income_and_type": 3,
    },
)
def increase_in_households_capital_stock_due_to_investments():
    """
    Household investments to increase their capital stock, mainly housing. The initial values are used to maintain certain ratios throughout the simulation.
    """
    return if_then_else(
        time() < 2015,
        lambda: zidz(
            gross_fixed_capital_formation_real()
            .loc[:, "REAL_ESTATE"]
            .reset_coords(drop=True)
            * price_gfcf().loc[:, "REAL_ESTATE"].reset_coords(drop=True)
            / price_transformation()
            * unit_conversion_dollars_mdollars()
            * zidz(
                households_financial_assets() * base_number_of_households(),
                sum(
                    households_financial_assets().rename(
                        {"HOUSEHOLDS_I": "HOUSEHOLDS_I!"}
                    )
                    * base_number_of_households().rename(
                        {"HOUSEHOLDS_I": "HOUSEHOLDS_I!"}
                    ),
                    dim=["HOUSEHOLDS_I!"],
                ).expand_dims({"HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"]}, 1),
            ),
            base_number_of_households(),
        ),
        lambda: zidz(
            gross_fixed_capital_formation_real()
            .loc[:, "REAL_ESTATE"]
            .reset_coords(drop=True)
            * price_gfcf().loc[:, "REAL_ESTATE"].reset_coords(drop=True)
            / price_transformation()
            * unit_conversion_dollars_mdollars()
            * zidz(
                households_financial_assets()
                * number_of_households_by_income_and_type(),
                sum(
                    households_financial_assets().rename(
                        {"HOUSEHOLDS_I": "HOUSEHOLDS_I!"}
                    )
                    * number_of_households_by_income_and_type().rename(
                        {"HOUSEHOLDS_I": "HOUSEHOLDS_I!"}
                    ),
                    dim=["HOUSEHOLDS_I!"],
                ).expand_dims({"HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"]}, 1),
            ),
            number_of_households_by_income_and_type(),
        ),
    )


@component.add(
    name="interest_rate_for_households_assets",
    units="DMNL",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "debt_interest_rate": 1,
        "mark_up_for_households_assets": 1,
        "minimum_households_interest_rate": 1,
    },
)
def interest_rate_for_households_assets():
    """
    Interest rate for households assets.
    """
    return np.maximum(
        debt_interest_rate() + mark_up_for_households_assets(),
        minimum_households_interest_rate(),
    )


@component.add(
    name="interest_rate_for_households_liabilities",
    units="DMNL",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "debt_interest_rate": 1,
        "mark_up_for_households_liabilities": 1,
        "minimum_households_interest_rate": 1,
    },
)
def interest_rate_for_households_liabilities():
    """
    Interest rate for households liabilities.
    """
    return np.maximum(
        debt_interest_rate() + mark_up_for_households_liabilities(),
        minimum_households_interest_rate(),
    )


@component.add(
    name="mark_up_for_households_assets",
    units="DMNL",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "initial_households_assets_interest_rate": 1,
        "debt_interest_rate_historic": 1,
    },
)
def mark_up_for_households_assets():
    """
    Increase in the interest rate on household assets with respect to the base interest rate.
    """
    return initial_households_assets_interest_rate() - debt_interest_rate_historic()


@component.add(
    name="mark_up_for_households_liabilities",
    units="DMNL",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "initial_households_liabilities_interest_rate": 1,
        "debt_interest_rate_historic": 1,
    },
)
def mark_up_for_households_liabilities():
    """
    Increase in the interest rate on household liabilities with respect to the base interest rate.
    """
    return (
        initial_households_liabilities_interest_rate() - debt_interest_rate_historic()
    )


@component.add(
    name="Maximum_annual_loan_payment",
    units="$/Year",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "households_disposable_income": 1,
        "ratio_of_maximum_anual_loan_payment_over_disposable_income_sp": 1,
    },
)
def maximum_annual_loan_payment():
    """
    Maximum annual loan payment.
    """
    return (
        households_disposable_income()
        * ratio_of_maximum_anual_loan_payment_over_disposable_income_sp()
    )


@component.add(
    name="Maximum_financing_obtainable",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "maximum_annual_loan_payment": 1,
        "maximum_years_to_repay_a_loan_sp": 2,
        "interest_rate_for_households_liabilities": 3,
    },
)
def maximum_financing_obtainable():
    """
    Maximum financing obtainable.
    """
    return zidz(
        maximum_annual_loan_payment()
        * (
            (1 + interest_rate_for_households_liabilities())
            ** maximum_years_to_repay_a_loan_sp()
            - 1
        ),
        (1 + interest_rate_for_households_liabilities())
        ** maximum_years_to_repay_a_loan_sp()
        * interest_rate_for_households_liabilities(),
    )


@component.add(
    name="ratio_liabilties_to_disposable_income",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "initial_households_financial_liabilities_per_household": 1,
        "initial_households_disposable_income": 1,
    },
)
def ratio_liabilties_to_disposable_income():
    return zidz(
        initial_households_financial_liabilities_per_household(),
        initial_households_disposable_income(),
    )


@component.add(
    name="SELECT_POLICY_FINANCE_BASIC_INCOME_SP",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_select_policy_finance_basic_income_sp"},
)
def select_policy_finance_basic_income_sp():
    """
    SWITHC 0: Tax on wealth to finance basic income 1: Tax on CO2 to finance basic income
    """
    return _ext_constant_select_policy_finance_basic_income_sp()


_ext_constant_select_policy_finance_basic_income_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "SELECT_POLICY_FINANCE_BASIC_INCOME_SP*",
    {},
    _root,
    {},
    "_ext_constant_select_policy_finance_basic_income_sp",
)


@component.add(
    name="share_of_total_financial_assets_households_paying_taxes_finance_basic_income",
    units="DMNL",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "total_financial_assets_by_houshold_group": 1,
        "aux_basic_income_tax_payers_sp": 1,
        "total_financial_assets_households_paying_taxes_finance_basic_income": 1,
    },
)
def share_of_total_financial_assets_households_paying_taxes_finance_basic_income():
    """
    Share of the total finacial assets in a country owned by each household
    """
    return zidz(
        total_financial_assets_by_houshold_group() * aux_basic_income_tax_payers_sp(),
        total_financial_assets_households_paying_taxes_finance_basic_income().expand_dims(
            {"HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"]}, 1
        ),
    )


@component.add(
    name="SWITCH_FINANCE",
    units="1",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_finance"},
)
def switch_finance():
    """
    This switch can take two values: 0: the module runs isolated from the rest of WILIAM, replacing inter(sub)module variables with exogenous parameters. 1: the module runs integrated with the rest of WILIAM.
    """
    return _ext_constant_switch_finance()


_ext_constant_switch_finance = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_FINANCE",
    {},
    _root,
    {},
    "_ext_constant_switch_finance",
)


@component.add(
    name="taxes_on_assets_to_finance_basic_income",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"government_basic_income_expenditure": 1},
)
def taxes_on_assets_to_finance_basic_income():
    """
    Taxes on financial assets to fiance basic income
    """
    return government_basic_income_expenditure()


@component.add(
    name="taxes_on_assets_to_finance_basic_income_by_household_group",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_policy_finance_basic_income_sp": 1,
        "share_of_total_financial_assets_households_paying_taxes_finance_basic_income": 1,
        "taxes_on_assets_to_finance_basic_income": 1,
    },
)
def taxes_on_assets_to_finance_basic_income_by_household_group():
    """
    Taxes on financial assets to finance basic income paid by each household group
    """
    return if_then_else(
        select_policy_finance_basic_income_sp() == 0,
        lambda: taxes_on_assets_to_finance_basic_income()
        * share_of_total_financial_assets_households_paying_taxes_finance_basic_income(),
        lambda: xr.DataArray(
            0,
            {
                "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
            },
            ["REGIONS_35_I", "HOUSEHOLDS_I"],
        ),
    )


@component.add(
    name="total_financial_assets_by_houshold_group",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "households_financial_assets": 1,
        "number_of_households_by_income_and_type": 1,
        "unit_conversion_dollars_mdollars": 1,
    },
)
def total_financial_assets_by_houshold_group():
    """
    Total finacial assets by type of household
    """
    return (
        households_financial_assets()
        * number_of_households_by_income_and_type()
        / unit_conversion_dollars_mdollars()
    )


@component.add(
    name="total_financial_assets_households_paying_taxes_finance_basic_income",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "total_financial_assets_by_houshold_group": 1,
        "aux_basic_income_tax_payers_sp": 1,
    },
)
def total_financial_assets_households_paying_taxes_finance_basic_income():
    """
    Total finacial assets
    """
    return sum(
        total_financial_assets_by_houshold_group().rename(
            {"HOUSEHOLDS_I": "HOUSEHOLDS_I!"}
        )
        * aux_basic_income_tax_payers_sp().rename({"HOUSEHOLDS_I": "HOUSEHOLDS_I!"}),
        dim=["HOUSEHOLDS_I!"],
    )


@component.add(
    name="variation_in_households_capital_stock_due_to_revalorizations",
    units="$/Year",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_finance": 1,
        "delayed_ts_price_gfcf": 1,
        "price_gfcf": 1,
        "households_capital_stock": 1,
    },
)
def variation_in_households_capital_stock_due_to_revalorizations():
    """
    Variation in households capital stock due to revalorizations.
    """
    return if_then_else(
        switch_finance() == 0,
        lambda: xr.DataArray(
            0,
            {
                "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
            },
            ["REGIONS_35_I", "HOUSEHOLDS_I"],
        ),
        lambda: np.minimum(
            zidz(
                price_gfcf().loc[:, "REAL_ESTATE"].reset_coords(drop=True),
                delayed_ts_price_gfcf().loc[:, "REAL_ESTATE"].reset_coords(drop=True),
            )
            - 1,
            0.05,
        )
        * households_capital_stock(),
    )


@component.add(
    name="variation_in_households_financial_assets_due_to_net_lending",
    units="$/Year",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "households_net_lending": 3,
        "variation_in_households_financial_liabilities": 3,
        "households_financial_assets": 1,
    },
)
def variation_in_households_financial_assets_due_to_net_lending():
    """
    Variation in households financial assets due to net lending IF_THEN_ELSE(households_net_lending[REGIONS_35_I,HOUSEHOLDS_I]<0 :AND: ABS(households_net_lending[REGIONS_35_I,HOUSEHOLDS_I])>households_financial _assets[REGIONS_35_I,HOUSEHOLDS_I],-households_financial_assets[REGIONS_35_ I,HOUSEHOLDS_I],households_net_lending[REGIONS_35_I,HOUSEHOLDS_I])
    """
    return if_then_else(
        np.logical_and(
            households_net_lending() + variation_in_households_financial_liabilities()
            < 0,
            np.abs(
                households_net_lending()
                + variation_in_households_financial_liabilities()
            )
            > households_financial_assets(),
        ),
        lambda: xr.DataArray(
            0,
            {
                "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
            },
            ["REGIONS_35_I", "HOUSEHOLDS_I"],
        ),
        lambda: households_net_lending()
        + variation_in_households_financial_liabilities(),
    )


@component.add(
    name="variation_in_households_financial_liabilities",
    units="$/Year",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "ratio_liabilties_to_disposable_income": 3,
        "households_net_lending": 3,
        "households_financial_assets": 1,
        "delayed_ts_households_disposable_income": 3,
        "households_financial_liabilities": 3,
    },
)
def variation_in_households_financial_liabilities():
    """
    Variation in households financial liabilities. IF_THEN_ELSE(Time < 2015, 0, IF_THEN_ELSE(households_net_lending[REGIONS_35_I,HOUSEHOLDS_I]< 0 :AND: ABS(households_net_lending[REGIONS_35_I,HOUSEHOLDS_I ])>households_financial_assets[REGIONS_35_I,HOUSEHOLDS_I],-households_net_lending[REG IONS_35_I,HOUSEHOLDS_I], ratio_liabilities_to_assets[REGIONS_35_I,HOUSEHOLDS_I]*(households_capital_stock[REGI ONS_35_I ,HOUSEHOLDS_I]+households_financial_assets[REGIONS_35_I,HOUSEHOLDS_I])-households_fin ancial_liabilities[REGIONS_35_I,HOUSEHOLDS_I ]) )
    """
    return if_then_else(
        time() < 2015,
        lambda: xr.DataArray(
            0,
            {
                "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
            },
            ["REGIONS_35_I", "HOUSEHOLDS_I"],
        ),
        lambda: if_then_else(
            np.logical_and(
                households_net_lending()
                + ratio_liabilties_to_disposable_income()
                * delayed_ts_households_disposable_income()
                - households_financial_liabilities()
                < 0,
                np.abs(
                    households_net_lending()
                    + ratio_liabilties_to_disposable_income()
                    * delayed_ts_households_disposable_income()
                    - households_financial_liabilities()
                )
                > households_financial_assets(),
            ),
            lambda: -households_net_lending(),
            lambda: ratio_liabilties_to_disposable_income()
            * delayed_ts_households_disposable_income()
            - households_financial_liabilities(),
        ),
    )
