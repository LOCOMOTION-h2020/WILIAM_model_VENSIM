"""
Module finance.exogenous_inputs
Translated using PySD version 3.10.0
"""


@component.add(
    name="INITIAL_HOUSEHOLDS_ASSETS_INTEREST_RATE",
    units="DMNL",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_initial_households_assets_interest_rate"
    },
)
def initial_households_assets_interest_rate():
    """
    Households liabilities interest rate in 2015.
    """
    return _ext_constant_initial_households_assets_interest_rate()


_ext_constant_initial_households_assets_interest_rate = ExtConstant(
    "model_parameters/finance/finance.xlsx",
    "assets_yield",
    "HOUSEHOLDS_ASSETS_YIELD",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
    "_ext_constant_initial_households_assets_interest_rate",
)


@component.add(
    name="INITIAL_HOUSEHOLDS_CAPITAL_STOCK",
    units="$",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_households_capital_stock"},
)
def initial_households_capital_stock():
    """
    Initial households capital stock.
    """
    return _ext_constant_initial_households_capital_stock()


_ext_constant_initial_households_capital_stock = ExtConstant(
    "model_parameters/finance/finance.xlsx",
    "non_financial_assets",
    "INITIAL_HOUSEHOLDS_CAPITAL_STOCK_MP",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
    "_ext_constant_initial_households_capital_stock",
)


@component.add(
    name="INITIAL_HOUSEHOLDS_FINANCIAL_ASSETS",
    units="$",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_households_financial_assets"},
)
def initial_households_financial_assets():
    """
    Initial total households financial assets.
    """
    return _ext_constant_initial_households_financial_assets()


_ext_constant_initial_households_financial_assets = ExtConstant(
    "model_parameters/finance/finance.xlsx",
    "financial_assets",
    "IMV_BASE_HOUSEHOLD_ASSETS",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
    "_ext_constant_initial_households_financial_assets",
)


@component.add(
    name="INITIAL_HOUSEHOLDS_FINANCIAL_LIABILITIES",
    units="$",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_initial_households_financial_liabilities"
    },
)
def initial_households_financial_liabilities():
    """
    Initial total households financial liabilities.
    """
    return _ext_constant_initial_households_financial_liabilities()


_ext_constant_initial_households_financial_liabilities = ExtConstant(
    "model_parameters/finance/finance.xlsx",
    "financial_liabilities",
    "IMV_BASE_HOUSEHOLDS_LIABILITIES",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
    "_ext_constant_initial_households_financial_liabilities",
)


@component.add(
    name="INITIAL_HOUSEHOLDS_LIABILITIES_INTEREST_RATE",
    units="DMNL",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_initial_households_liabilities_interest_rate"
    },
)
def initial_households_liabilities_interest_rate():
    """
    Households liabilities interest rate in 2015.
    """
    return _ext_constant_initial_households_liabilities_interest_rate()


_ext_constant_initial_households_liabilities_interest_rate = ExtConstant(
    "model_parameters/finance/finance.xlsx",
    "liabilites_yield",
    "HOUSEHOLDS_LIABILITIES_YIELD",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
    "_ext_constant_initial_households_liabilities_interest_rate",
)


@component.add(
    name="MAXIMUM_YEARS_TO_REPAY_A_LOAN_SP",
    units="Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_maximum_years_to_repay_a_loan_sp"},
)
def maximum_years_to_repay_a_loan_sp():
    """
    Maximum years to repay a loan.
    """
    return _ext_constant_maximum_years_to_repay_a_loan_sp()


_ext_constant_maximum_years_to_repay_a_loan_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "finance",
    "MAXIMUM_YEARS_TO_REPAY_A_LOAN_SP*",
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    _root,
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    "_ext_constant_maximum_years_to_repay_a_loan_sp",
)


@component.add(
    name="MINIMUM_HOUSEHOLDS_INTEREST_RATE",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_minimum_households_interest_rate"},
)
def minimum_households_interest_rate():
    """
    Minimum interest ratio that households will have on both their assets and their liabilities.
    """
    return _ext_constant_minimum_households_interest_rate()


_ext_constant_minimum_households_interest_rate = ExtConstant(
    "model_parameters/finance/finance.xlsx",
    "ratios",
    "MINIMUM_HOUSEHOLDS_INTEREST_RATE_MP",
    {},
    _root,
    {},
    "_ext_constant_minimum_households_interest_rate",
)


@component.add(
    name="RATIO_OF_MAXIMUM_ANUAL_LOAN_PAYMENT_OVER_DISPOSABLE_INCOME_SP",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_ratio_of_maximum_anual_loan_payment_over_disposable_income_sp"
    },
)
def ratio_of_maximum_anual_loan_payment_over_disposable_income_sp():
    """
    Ratio of maximum anual loan payment over disposable income.
    """
    return _ext_constant_ratio_of_maximum_anual_loan_payment_over_disposable_income_sp()


_ext_constant_ratio_of_maximum_anual_loan_payment_over_disposable_income_sp = (
    ExtConstant(
        "scenario_parameters/scenario_parameters.xlsx",
        "finance",
        "RATIO_OF_MAXIMUM_ANUAL_LOAN_PAYMENT_OVER_DISPOSABLE_INCOME_SP",
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
        },
        _root,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
        },
        "_ext_constant_ratio_of_maximum_anual_loan_payment_over_disposable_income_sp",
    )
)
