"""
Module economy.auxiliary_outputs_and_indicators
Translated using PySD version 3.10.0
"""


@component.add(
    name="annual_variation_government_expenditure",
    units="DMNL",
    subscripts=["REGIONS_35_I", "COFOG_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "government_expenditure_by_cofog": 1,
        "delayed_government_expenditure_by_cofog": 2,
    },
)
def annual_variation_government_expenditure():
    """
    Percent of the annual variation in the government expenditure
    """
    return (
        (government_expenditure_by_cofog() - delayed_government_expenditure_by_cofog())
        / delayed_government_expenditure_by_cofog()
        * 100
    )


@component.add(
    name="aux_GDP_real_35R_until_2019",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_aux_gdp_real_35r_until_2019": 1},
    other_deps={
        "_delayfixed_aux_gdp_real_35r_until_2019": {
            "initial": {"time_step": 1},
            "step": {"gdp_real_35r_until_2019": 1},
        }
    },
)
def aux_gdp_real_35r_until_2019():
    return _delayfixed_aux_gdp_real_35r_until_2019()


_delayfixed_aux_gdp_real_35r_until_2019 = DelayFixed(
    lambda: gdp_real_35r_until_2019(),
    lambda: time_step(),
    lambda: xr.DataArray(
        0, {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]}, ["REGIONS_35_I"]
    ),
    time_step,
    "_delayfixed_aux_gdp_real_35r_until_2019",
)


@component.add(
    name="delayed_government_expenditure_by_COFOG",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_I", "COFOG_I"],
    comp_type="Stateful",
    comp_subtype="Delay",
    depends_on={"_delay_delayed_government_expenditure_by_cofog": 1},
    other_deps={
        "_delay_delayed_government_expenditure_by_cofog": {
            "initial": {"government_expenditure_by_cofog": 1},
            "step": {"government_expenditure_by_cofog": 1},
        }
    },
)
def delayed_government_expenditure_by_cofog():
    """
    Delay of one year to calculate the difference
    """
    return _delay_delayed_government_expenditure_by_cofog()


_delay_delayed_government_expenditure_by_cofog = Delay(
    lambda: government_expenditure_by_cofog(),
    lambda: xr.DataArray(
        1,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "COFOG_I": _subscript_dict["COFOG_I"],
        },
        ["REGIONS_35_I", "COFOG_I"],
    ),
    lambda: government_expenditure_by_cofog(),
    lambda: 1,
    time_step,
    "_delay_delayed_government_expenditure_by_cofog",
)


@component.add(
    name="GDP_real_35R_until_2019",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "aux_gdp_real_35r_until_2019": 1,
        "gross_domestic_product_real_demand_side": 1,
    },
)
def gdp_real_35r_until_2019():
    return if_then_else(
        time() > 2019,
        lambda: aux_gdp_real_35r_until_2019(),
        lambda: gross_domestic_product_real_demand_side(),
    )


@component.add(
    name="government_expenditure_by_COFOG",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_I", "COFOG_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "government_consumption_by_cofog": 1,
        "government_investment_by_cofog": 1,
    },
)
def government_expenditure_by_cofog():
    """
    Government expenditure by category (COFOG classification: Classification of the Functions of the Government).
    """
    return government_consumption_by_cofog() + government_investment_by_cofog()


@component.add(
    name="INITIAL_GROSS_SAVINGS",
    units="$/Year",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_initial_gross_savings": 1},
    other_deps={
        "_initial_initial_gross_savings": {
            "initial": {"households_gross_savings": 1},
            "step": {},
        }
    },
)
def initial_gross_savings():
    return _initial_initial_gross_savings()


_initial_initial_gross_savings = Initial(
    lambda: households_gross_savings(), "_initial_initial_gross_savings"
)
