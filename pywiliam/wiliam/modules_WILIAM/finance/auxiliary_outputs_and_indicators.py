"""
Module finance.auxiliary_outputs_and_indicators
Translated using PySD version 3.10.0
"""


@component.add(
    name="INITIAL_HOUSEHOLDS_CAPITAL_STOCK_PER_HOUSEHOLD",
    units="$",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_initial_households_capital_stock_per_household": 1},
    other_deps={
        "_initial_initial_households_capital_stock_per_household": {
            "initial": {"households_capital_stock": 1},
            "step": {},
        }
    },
)
def initial_households_capital_stock_per_household():
    return _initial_initial_households_capital_stock_per_household()


_initial_initial_households_capital_stock_per_household = Initial(
    lambda: households_capital_stock(),
    "_initial_initial_households_capital_stock_per_household",
)


@component.add(
    name="INITIAL_HOUSEHOLDS_FINANCIAL_ASSETS_PER_HOUSEHOLD",
    units="$",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_initial_households_financial_assets_per_household": 1},
    other_deps={
        "_initial_initial_households_financial_assets_per_household": {
            "initial": {"households_financial_assets": 1},
            "step": {},
        }
    },
)
def initial_households_financial_assets_per_household():
    return _initial_initial_households_financial_assets_per_household()


_initial_initial_households_financial_assets_per_household = Initial(
    lambda: households_financial_assets(),
    "_initial_initial_households_financial_assets_per_household",
)


@component.add(
    name="INITIAL_HOUSEHOLDS_FINANCIAL_LIABILITIES_PER_HOUSEHOLD",
    units="$",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_initial_households_financial_liabilities_per_household": 1},
    other_deps={
        "_initial_initial_households_financial_liabilities_per_household": {
            "initial": {"households_financial_liabilities": 1},
            "step": {},
        }
    },
)
def initial_households_financial_liabilities_per_household():
    return _initial_initial_households_financial_liabilities_per_household()


_initial_initial_households_financial_liabilities_per_household = Initial(
    lambda: households_financial_liabilities(),
    "_initial_initial_households_financial_liabilities_per_household",
)


@component.add(
    name="INITIAL_HOUSEHOLDS_PROPERTY_INCOME_PAID",
    units="$/Year",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_initial_households_property_income_paid"
    },
)
def initial_households_property_income_paid():
    return _ext_constant_initial_households_property_income_paid()


_ext_constant_initial_households_property_income_paid = ExtConstant(
    "model_parameters/economy/Consumption_ENDOGENOUS.xlsx",
    "HH_Property_income_paid",
    "INITIAL_HOUSEHOLDS_PROPERTY_INCOME_PAID",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
    "_ext_constant_initial_households_property_income_paid",
)
