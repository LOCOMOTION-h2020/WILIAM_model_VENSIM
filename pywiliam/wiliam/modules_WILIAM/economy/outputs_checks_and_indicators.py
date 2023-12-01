"""
Module economy.outputs_checks_and_indicators
Translated using PySD version 3.10.0
"""


@component.add(
    name="annual_GDP_growth_rate_real",
    units="1/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "one_year": 1,
        "gross_domestic_product_real_supply_side": 1,
        "delayed_gdp_real": 1,
    },
)
def annual_gdp_growth_rate_real():
    """
    Annual GDP growth rate.
    """
    return if_then_else(
        time() < 2015,
        lambda: xr.DataArray(
            0, {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]}, ["REGIONS_35_I"]
        ),
        lambda: (
            zidz(gross_domestic_product_real_supply_side(), delayed_gdp_real()) - 1
        )
        / one_year(),
    )


@component.add(
    name="annual_GDP_real_9R_growth",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"gdp_real_9r": 1, "delayed_gdp_real_9r": 1},
)
def annual_gdp_real_9r_growth():
    return gdp_real_9r() - delayed_gdp_real_9r()


@component.add(
    name="annual_GDPpc_growth_rate_real",
    units="1/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "delayed_gdppc_real": 1, "one_year": 1, "gdppc_real": 1},
)
def annual_gdppc_growth_rate_real():
    """
    Annual GDPpc growth rate.
    """
    return if_then_else(
        time() < 2015,
        lambda: xr.DataArray(
            0, {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]}, ["REGIONS_35_I"]
        ),
        lambda: (zidz(gdppc_real(), delayed_gdppc_real()) - 1) / one_year(),
    )


@component.add(
    name="annual_GDPpc_growth_rate_real_1R",
    units="DMNL/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"annual_gdppc_growth_rate_real": 2},
)
def annual_gdppc_growth_rate_real_1r():
    """
    Annual GDPpc growth rate.
    """
    return zidz(
        zidz(
            sum(
                annual_gdppc_growth_rate_real()
                .loc[_subscript_dict["REGIONS_EU27_I"]]
                .rename({"REGIONS_35_I": "REGIONS_EU27_I!"}),
                dim=["REGIONS_EU27_I!"],
            ),
            27,
        )
        + zidz(
            sum(
                annual_gdppc_growth_rate_real()
                .loc[_subscript_dict["REGIONS_8_I"]]
                .rename({"REGIONS_35_I": "REGIONS_8_I!"}),
                dim=["REGIONS_8_I!"],
            ),
            8,
        ),
        2,
    )


@component.add(
    name="annual_output_growth_rate",
    units="1/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"output_real": 1, "delayed_ts_output_real": 1, "one_year": 1},
)
def annual_output_growth_rate():
    """
    Annual output per sector and region growth rate.
    """
    return (-1 + zidz(output_real(), delayed_ts_output_real())) / one_year()


@component.add(
    name="aux_GFCF_2015",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I", "SECTORS_ENERGY_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_aux_gfcf_2015": 1},
    other_deps={
        "_delayfixed_aux_gfcf_2015": {
            "initial": {"time_step": 1},
            "step": {"gfcf_until_2015": 1},
        }
    },
)
def aux_gfcf_2015():
    """
    Auxiliary variable to estimate the GFCF in the year 2015.
    """
    return _delayfixed_aux_gfcf_2015()


_delayfixed_aux_gfcf_2015 = DelayFixed(
    lambda: gfcf_until_2015(),
    lambda: time_step(),
    lambda: xr.DataArray(
        0,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "SECTORS_ENERGY_I": _subscript_dict["SECTORS_ENERGY_I"],
        },
        ["REGIONS_35_I", "SECTORS_ENERGY_I"],
    ),
    time_step,
    "_delayfixed_aux_gfcf_2015",
)


@component.add(
    name="consumption_fixed_capital_real_1S",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"consumption_fixed_capital_real": 1},
)
def consumption_fixed_capital_real_1s():
    return sum(
        consumption_fixed_capital_real().rename({"SECTORS_I": "SECTORS_I!"}),
        dim=["SECTORS_I!"],
    )


@component.add(
    name="delayed_GDP_real",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_gdp_real": 1},
    other_deps={
        "_delayfixed_delayed_gdp_real": {
            "initial": {},
            "step": {"gross_domestic_product_real_supply_side": 1},
        }
    },
)
def delayed_gdp_real():
    """
    GDP projection delayed 1 year.
    """
    return _delayfixed_delayed_gdp_real()


_delayfixed_delayed_gdp_real = DelayFixed(
    lambda: gross_domestic_product_real_supply_side(),
    lambda: 1,
    lambda: xr.DataArray(
        0, {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]}, ["REGIONS_35_I"]
    ),
    time_step,
    "_delayfixed_delayed_gdp_real",
)


@component.add(
    name="delayed_GDP_real_9R",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_gdp_real_9r": 1},
    other_deps={
        "_delayfixed_delayed_gdp_real_9r": {
            "initial": {"gdp_real_9r": 1},
            "step": {"gdp_real_9r": 1},
        }
    },
)
def delayed_gdp_real_9r():
    return _delayfixed_delayed_gdp_real_9r()


_delayfixed_delayed_gdp_real_9r = DelayFixed(
    lambda: gdp_real_9r(),
    lambda: 1,
    lambda: gdp_real_9r(),
    time_step,
    "_delayfixed_delayed_gdp_real_9r",
)


@component.add(
    name="delayed_GDPpc_real",
    units="Mdollars_2015/(Year*person)",
    subscripts=["REGIONS_35_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_gdppc_real": 1},
    other_deps={
        "_delayfixed_delayed_gdppc_real": {"initial": {}, "step": {"gdppc_real": 1}}
    },
)
def delayed_gdppc_real():
    """
    GDPpc projection delayed 1 year.
    """
    return _delayfixed_delayed_gdppc_real()


_delayfixed_delayed_gdppc_real = DelayFixed(
    lambda: gdppc_real(),
    lambda: 1,
    lambda: xr.DataArray(
        0, {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]}, ["REGIONS_35_I"]
    ),
    time_step,
    "_delayfixed_delayed_gdppc_real",
)


@component.add(
    name="disposable_income_per_capita_real",
    units="dollars_2015/(Year*person)",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"disposable_income_real": 1, "population_35_regions": 1},
)
def disposable_income_per_capita_real():
    """
    Disposable income per capita in real terms
    """
    return zidz(disposable_income_real(), population_35_regions())


@component.add(
    name="disposable_income_per_capita_real_9R",
    units="dollars_2015/(Year*person)",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "disposable_income_per_capita_real": 1,
        "disposable_income_per_capita_real_eu27": 1,
    },
)
def disposable_income_per_capita_real_9r():
    """
    disposable_income_per_capita_real_9R
    """
    value = xr.DataArray(
        np.nan, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
    )
    value.loc[_subscript_dict["REGIONS_8_I"]] = (
        disposable_income_per_capita_real()
        .loc[_subscript_dict["REGIONS_8_I"]]
        .rename({"REGIONS_35_I": "REGIONS_8_I"})
        .values
    )
    value.loc[["EU27"]] = disposable_income_per_capita_real_eu27()
    return value


@component.add(
    name="disposable_income_per_capita_real_EU27",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"disposable_income_real": 1, "population_35_regions": 1},
)
def disposable_income_per_capita_real_eu27():
    return sum(
        disposable_income_real()
        .loc[_subscript_dict["REGIONS_EU27_I"]]
        .rename({"REGIONS_35_I": "REGIONS_EU27_I!"}),
        dim=["REGIONS_EU27_I!"],
    ) / sum(
        population_35_regions()
        .loc[_subscript_dict["REGIONS_EU27_I"]]
        .rename({"REGIONS_35_I": "REGIONS_EU27_I!"}),
        dim=["REGIONS_EU27_I!"],
    )


@component.add(
    name="disposable_income_real_1R",
    units="Mdollars_2015/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"disposable_income_real": 1},
)
def disposable_income_real_1r():
    return sum(
        disposable_income_real().rename({"REGIONS_35_I": "REGIONS_35_I!"}),
        dim=["REGIONS_35_I!"],
    )


@component.add(
    name="economy_dashboard",
    subscripts=["REGIONS_35_I", "DASHBOARD_ECONOMY_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "gross_domestic_product_real_supply_side": 4,
        "gross_value_added_real": 5,
        "taxes_products_final_demand_real": 5,
        "taxes_products_by_sector_real": 1,
        "final_demand_imports_in_basic_prices_real_by_component": 4,
        "final_demand_dometic_in_basic_prices_real_by_component": 4,
        "total_imports_real_by_product": 2,
        "total_exports_real_by_product": 2,
        "employment_total": 1,
        "labour_force": 1,
        "unemployment_rate": 1,
        "government_revenue": 1,
        "gross_domestic_product_deflator": 6,
        "government_expenditure": 1,
        "government_budget_balance": 2,
        "government_debt": 2,
        "disposable_income_real": 3,
        "consumption_coicop_real": 2,
        "unit_conversion_dollars_mdollars": 2,
        "population_35_regions": 2,
        "consumer_price_index": 1,
        "disposable_income": 2,
        "consumption_coicop": 2,
    },
)
def economy_dashboard():
    """
    Dashboard of the economy. Monetary values in Million USD 2015 prices. per capita vaules in USD 2015. Employment in number of people.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "DASHBOARD_ECONOMY_I": _subscript_dict["DASHBOARD_ECONOMY_I"],
        },
        ["REGIONS_35_I", "DASHBOARD_ECONOMY_I"],
    )
    value.loc[:, ["DB_GDP"]] = (
        (gross_domestic_product_real_supply_side() / 1000)
        .expand_dims({"DASHBOARD_ECONOMY_I": ["DB_GDP"]}, 1)
        .values
    )
    value.loc[:, ["DB_GVA_AGRICULTURE"]] = (
        (
            sum(
                gross_value_added_real()
                .loc[:, _subscript_dict["SECTORS_AGRICULTURE_I"]]
                .rename(
                    {
                        "REGIONS_35_MAP_I": "REGIONS_35_I",
                        "SECTORS_MAP_I": "SECTORS_AGRICULTURE_I!",
                    }
                ),
                dim=["SECTORS_AGRICULTURE_I!"],
            )
            / 1000
        )
        .expand_dims({"DASHBOARD_ECONOMY_I": ["DB_GVA_AGRICULTURE"]}, 1)
        .values
    )
    value.loc[:, ["DB_GVA_EXTRACTION"]] = (
        (
            sum(
                gross_value_added_real()
                .loc[:, _subscript_dict["SECTORS_EXTRACTION_I"]]
                .rename(
                    {
                        "REGIONS_35_MAP_I": "REGIONS_35_I",
                        "SECTORS_MAP_I": "SECTORS_EXTRACTION_I!",
                    }
                ),
                dim=["SECTORS_EXTRACTION_I!"],
            )
            / 1000
        )
        .expand_dims({"DASHBOARD_ECONOMY_I": ["DB_GVA_EXTRACTION"]}, 1)
        .values
    )
    value.loc[:, ["DB_GVA_ENERGY"]] = (
        (
            sum(
                gross_value_added_real()
                .loc[:, _subscript_dict["SECTORS_ENERGY_I"]]
                .rename(
                    {
                        "REGIONS_35_MAP_I": "REGIONS_35_I",
                        "SECTORS_MAP_I": "SECTORS_ENERGY_I!",
                    }
                ),
                dim=["SECTORS_ENERGY_I!"],
            )
            / 1000
        )
        .expand_dims({"DASHBOARD_ECONOMY_I": ["DB_GVA_ENERGY"]}, 1)
        .values
    )
    value.loc[:, ["DB_GVA_INDUSTRY"]] = (
        (
            sum(
                gross_value_added_real()
                .loc[:, _subscript_dict["SECTORS_INDUSTRY_I"]]
                .rename(
                    {
                        "REGIONS_35_MAP_I": "REGIONS_35_I",
                        "SECTORS_MAP_I": "SECTORS_INDUSTRY_I!",
                    }
                ),
                dim=["SECTORS_INDUSTRY_I!"],
            )
            / 1000
        )
        .expand_dims({"DASHBOARD_ECONOMY_I": ["DB_GVA_INDUSTRY"]}, 1)
        .values
    )
    value.loc[:, ["DB_GVA_SERVICES"]] = (
        (
            sum(
                gross_value_added_real()
                .loc[:, _subscript_dict["SECTORS_SERVICES_I"]]
                .rename(
                    {
                        "REGIONS_35_MAP_I": "REGIONS_35_I",
                        "SECTORS_MAP_I": "SECTORS_SERVICES_I!",
                    }
                ),
                dim=["SECTORS_SERVICES_I!"],
            )
            / 1000
        )
        .expand_dims({"DASHBOARD_ECONOMY_I": ["DB_GVA_SERVICES"]}, 1)
        .values
    )
    value.loc[:, ["DB_GVA_TAXES_PRODUCTS_TOTAL"]] = (
        (
            (
                sum(
                    taxes_products_by_sector_real().rename(
                        {
                            "REGIONS_35_MAP_I": "REGIONS_35_I",
                            "SECTORS_MAP_I": "SECTORS_I!",
                        }
                    ),
                    dim=["SECTORS_I!"],
                )
                + sum(
                    taxes_products_final_demand_real().rename(
                        {
                            "REGIONS_35_MAP_I": "REGIONS_35_I",
                            "FINAL_DEMAND_I": "FINAL_DEMAND_I!",
                        }
                    ),
                    dim=["FINAL_DEMAND_I!"],
                )
            )
            / 1000
        )
        .expand_dims({"DASHBOARD_ECONOMY_I": ["DB_GVA_TAXES_PRODUCTS_TOTAL"]}, 1)
        .values
    )
    value.loc[:, ["DB_HH_CONSUMPTION"]] = (
        (
            final_demand_dometic_in_basic_prices_real_by_component()
            .loc[:, "CONSUMPTION_W"]
            .reset_coords(drop=True)
            / 1000
            + final_demand_imports_in_basic_prices_real_by_component()
            .loc[:, "CONSUMPTION_W"]
            .reset_coords(drop=True)
            / 1000
            + taxes_products_final_demand_real()
            .loc[:, "CONSUMPTION_W"]
            .reset_coords(drop=True)
            .rename({"REGIONS_35_MAP_I": "REGIONS_35_I"})
            / 1000
        )
        .expand_dims({"DASHBOARD_ECONOMY_I": ["DB_HH_CONSUMPTION"]}, 1)
        .values
    )
    value.loc[:, ["DB_GOV_CONSUMPTION"]] = (
        (
            final_demand_dometic_in_basic_prices_real_by_component()
            .loc[:, "GOVERNMENT_W"]
            .reset_coords(drop=True)
            / 1000
            + final_demand_imports_in_basic_prices_real_by_component()
            .loc[:, "GOVERNMENT_W"]
            .reset_coords(drop=True)
            / 1000
            + taxes_products_final_demand_real()
            .loc[:, "GOVERNMENT_W"]
            .reset_coords(drop=True)
            .rename({"REGIONS_35_MAP_I": "REGIONS_35_I"})
            / 1000
        )
        .expand_dims({"DASHBOARD_ECONOMY_I": ["DB_GOV_CONSUMPTION"]}, 1)
        .values
    )
    value.loc[:, ["DB_GROSS_FIXED_CAPITAL_FORMATION"]] = (
        (
            final_demand_dometic_in_basic_prices_real_by_component()
            .loc[:, "GROSS_FIXED_CAPITAL_FORMATION_W"]
            .reset_coords(drop=True)
            / 1000
            + final_demand_imports_in_basic_prices_real_by_component()
            .loc[:, "GROSS_FIXED_CAPITAL_FORMATION_W"]
            .reset_coords(drop=True)
            / 1000
            + taxes_products_final_demand_real()
            .loc[:, "GROSS_FIXED_CAPITAL_FORMATION_W"]
            .reset_coords(drop=True)
            .rename({"REGIONS_35_MAP_I": "REGIONS_35_I"})
            / 1000
        )
        .expand_dims({"DASHBOARD_ECONOMY_I": ["DB_GROSS_FIXED_CAPITAL_FORMATION"]}, 1)
        .values
    )
    value.loc[:, ["DB_OTHER_FINAL_DEMAND"]] = (
        (
            sum(
                final_demand_dometic_in_basic_prices_real_by_component()
                .loc[
                    :,
                    _subscript_dict[
                        "FINAL_DEMAND_EXCEPT_CONSUMPTION_INVESTMENT_GOVERNMENT_I"
                    ],
                ]
                .rename(
                    {
                        "FINAL_DEMAND_I": "FINAL_DEMAND_EXCEPT_CONSUMPTION_INVESTMENT_GOVERNMENT_I!"
                    }
                ),
                dim=["FINAL_DEMAND_EXCEPT_CONSUMPTION_INVESTMENT_GOVERNMENT_I!"],
            )
            / 1000
            + sum(
                final_demand_imports_in_basic_prices_real_by_component()
                .loc[
                    :,
                    _subscript_dict[
                        "FINAL_DEMAND_EXCEPT_CONSUMPTION_INVESTMENT_GOVERNMENT_I"
                    ],
                ]
                .rename(
                    {
                        "FINAL_DEMAND_I": "FINAL_DEMAND_EXCEPT_CONSUMPTION_INVESTMENT_GOVERNMENT_I!"
                    }
                ),
                dim=["FINAL_DEMAND_EXCEPT_CONSUMPTION_INVESTMENT_GOVERNMENT_I!"],
            )
            / 1000
            + sum(
                taxes_products_final_demand_real()
                .loc[
                    :,
                    _subscript_dict[
                        "FINAL_DEMAND_EXCEPT_CONSUMPTION_INVESTMENT_GOVERNMENT_I"
                    ],
                ]
                .rename(
                    {
                        "REGIONS_35_MAP_I": "REGIONS_35_I",
                        "FINAL_DEMAND_I": "FINAL_DEMAND_EXCEPT_CONSUMPTION_INVESTMENT_GOVERNMENT_I!",
                    }
                ),
                dim=["FINAL_DEMAND_EXCEPT_CONSUMPTION_INVESTMENT_GOVERNMENT_I!"],
            )
            / 1000
        )
        .expand_dims({"DASHBOARD_ECONOMY_I": ["DB_OTHER_FINAL_DEMAND"]}, 1)
        .values
    )
    value.loc[:, ["DB_TRADE_BALANCE"]] = (
        (
            sum(
                total_exports_real_by_product().rename({"SECTORS_I": "SECTORS_I!"}),
                dim=["SECTORS_I!"],
            )
            / 1000
            - sum(
                total_imports_real_by_product().rename({"SECTORS_I": "SECTORS_I!"}),
                dim=["SECTORS_I!"],
            )
            / 1000
        )
        .expand_dims({"DASHBOARD_ECONOMY_I": ["DB_TRADE_BALANCE"]}, 1)
        .values
    )
    value.loc[:, ["DB_EXPORTS"]] = (
        (
            sum(
                total_exports_real_by_product().rename({"SECTORS_I": "SECTORS_I!"}),
                dim=["SECTORS_I!"],
            )
            / 1000
        )
        .expand_dims({"DASHBOARD_ECONOMY_I": ["DB_EXPORTS"]}, 1)
        .values
    )
    value.loc[:, ["DB_IMPORTS"]] = (
        (
            sum(
                total_imports_real_by_product().rename({"SECTORS_I": "SECTORS_I!"}),
                dim=["SECTORS_I!"],
            )
            / 1000
        )
        .expand_dims({"DASHBOARD_ECONOMY_I": ["DB_IMPORTS"]}, 1)
        .values
    )
    value.loc[:, ["DB_EMPLOYMENT"]] = (
        (employment_total() / 1000)
        .expand_dims({"DASHBOARD_ECONOMY_I": ["DB_EMPLOYMENT"]}, 1)
        .values
    )
    value.loc[:, ["DB_LABOUR_FORCE"]] = (
        (labour_force() / 1000)
        .expand_dims({"DASHBOARD_ECONOMY_I": ["DB_LABOUR_FORCE"]}, 1)
        .values
    )
    value.loc[:, ["DB_UNEMPLOYMENT_RATE"]] = (
        unemployment_rate()
        .expand_dims({"DASHBOARD_ECONOMY_I": ["DB_UNEMPLOYMENT_RATE"]}, 1)
        .values
    )
    value.loc[:, ["DB_GOV_REVENUE"]] = (
        (zidz(government_revenue(), gross_domestic_product_deflator()) / 1000)
        .expand_dims({"DASHBOARD_ECONOMY_I": ["DB_GOV_REVENUE"]}, 1)
        .values
    )
    value.loc[:, ["DB_GOV_EXPENDITURE"]] = (
        (zidz(government_expenditure(), gross_domestic_product_deflator()) / 1000)
        .expand_dims({"DASHBOARD_ECONOMY_I": ["DB_GOV_EXPENDITURE"]}, 1)
        .values
    )
    value.loc[:, ["DB_GOV_BALANCE"]] = (
        (zidz(government_budget_balance(), gross_domestic_product_deflator()) / 1000)
        .expand_dims({"DASHBOARD_ECONOMY_I": ["DB_GOV_BALANCE"]}, 1)
        .values
    )
    value.loc[:, ["DB_GOV_BALANCE_TO_GDP"]] = (
        zidz(
            zidz(government_budget_balance(), gross_domestic_product_deflator()),
            gross_domestic_product_real_supply_side(),
        )
        .expand_dims({"DASHBOARD_ECONOMY_I": ["DB_GOV_BALANCE_TO_GDP"]}, 1)
        .values
    )
    value.loc[:, ["DB_GOV_DEBT"]] = (
        (zidz(government_debt(), gross_domestic_product_deflator()) / 1000)
        .expand_dims({"DASHBOARD_ECONOMY_I": ["DB_GOV_DEBT"]}, 1)
        .values
    )
    value.loc[:, ["DB_GOV_DEBT_TO_GDP"]] = (
        zidz(
            zidz(government_debt(), gross_domestic_product_deflator()),
            gross_domestic_product_real_supply_side(),
        )
        .expand_dims({"DASHBOARD_ECONOMY_I": ["DB_GOV_DEBT_TO_GDP"]}, 1)
        .values
    )
    value.loc[:, ["DB_HH_DISPOSABLE_INCOME"]] = (
        (disposable_income_real() / 1000)
        .expand_dims({"DASHBOARD_ECONOMY_I": ["DB_HH_DISPOSABLE_INCOME"]}, 1)
        .values
    )
    value.loc[:, ["DB_HH_CONSUMPTION_COICOP"]] = (
        (
            sum(
                consumption_coicop_real().rename({"COICOP_I": "COICOP_I!"}),
                dim=["COICOP_I!"],
            )
            / 1000
        )
        .expand_dims({"DASHBOARD_ECONOMY_I": ["DB_HH_CONSUMPTION_COICOP"]}, 1)
        .values
    )
    value.loc[:, ["DB_HH_SAVINGS"]] = (
        (
            disposable_income_real() / 1000
            - sum(
                consumption_coicop_real().rename({"COICOP_I": "COICOP_I!"}),
                dim=["COICOP_I!"],
            )
            / 1000
        )
        .expand_dims({"DASHBOARD_ECONOMY_I": ["DB_HH_SAVINGS"]}, 1)
        .values
    )
    value.loc[:, ["DB_GDP_PER_CAPITA"]] = (
        (
            zidz(gross_domestic_product_real_supply_side(), population_35_regions())
            * unit_conversion_dollars_mdollars()
        )
        .expand_dims({"DASHBOARD_ECONOMY_I": ["DB_GDP_PER_CAPITA"]}, 1)
        .values
    )
    value.loc[:, ["DB_DISPOSABLE_INCOME_PER_CAPITA"]] = (
        (
            zidz(disposable_income_real(), population_35_regions())
            * unit_conversion_dollars_mdollars()
        )
        .expand_dims({"DASHBOARD_ECONOMY_I": ["DB_DISPOSABLE_INCOME_PER_CAPITA"]}, 1)
        .values
    )
    value.loc[:, ["DB_CONSUMER_PRICE_INDEX"]] = (
        consumer_price_index()
        .expand_dims({"DASHBOARD_ECONOMY_I": ["DB_CONSUMER_PRICE_INDEX"]}, 1)
        .values
    )
    value.loc[:, ["DB_HH_DISPOSABLE_INCOME_NOMINAL"]] = (
        (disposable_income() / 1000)
        .expand_dims({"DASHBOARD_ECONOMY_I": ["DB_HH_DISPOSABLE_INCOME_NOMINAL"]}, 1)
        .values
    )
    value.loc[:, ["DB_HH_CONSUMPTION_COICOP_NOMINAL"]] = (
        (
            sum(
                consumption_coicop().rename({"COICOP_I": "COICOP_I!"}),
                dim=["COICOP_I!"],
            )
            / 1000
        )
        .expand_dims({"DASHBOARD_ECONOMY_I": ["DB_HH_CONSUMPTION_COICOP_NOMINAL"]}, 1)
        .values
    )
    value.loc[:, ["DB_HH_SAVINGS_NOMINAL"]] = (
        (
            disposable_income() / 1000
            - sum(
                consumption_coicop().rename({"COICOP_I": "COICOP_I!"}),
                dim=["COICOP_I!"],
            )
            / 1000
        )
        .expand_dims({"DASHBOARD_ECONOMY_I": ["DB_HH_SAVINGS_NOMINAL"]}, 1)
        .values
    )
    return value


@component.add(
    name="final_demand_domestic_in_basic_prices_real_1S",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I", "FINAL_DEMAND_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"final_demand_domestic_in_basic_prices_real": 1},
)
def final_demand_domestic_in_basic_prices_real_1s():
    return sum(
        final_demand_domestic_in_basic_prices_real().rename(
            {"SECTORS_I": "SECTORS_I!"}
        ),
        dim=["SECTORS_I!"],
    )


@component.add(
    name="final_exports_real_1S",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"final_exports_real": 1},
)
def final_exports_real_1s():
    return sum(
        final_exports_real().rename({"SECTORS_I": "SECTORS_I!"}), dim=["SECTORS_I!"]
    )


@component.add(
    name="GDP_real_1R",
    units="Mdollars_2015/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"gdp_real_9r": 1},
)
def gdp_real_1r():
    return sum(
        gdp_real_9r().rename({"REGIONS_9_I": "REGIONS_9_I!"}), dim=["REGIONS_9_I!"]
    )


@component.add(
    name="GDP_real_9R",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"gross_domestic_product_real_supply_side": 1, "gdp_real_eu27": 1},
)
def gdp_real_9r():
    value = xr.DataArray(
        np.nan, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
    )
    value.loc[_subscript_dict["REGIONS_8_I"]] = (
        gross_domestic_product_real_supply_side()
        .loc[_subscript_dict["REGIONS_8_I"]]
        .rename({"REGIONS_35_I": "REGIONS_8_I"})
        .values
    )
    value.loc[["EU27"]] = gdp_real_eu27()
    return value


@component.add(
    name="GDP_real_EU27",
    units="Mdollars_2015/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"gross_domestic_product_real_supply_side": 1},
)
def gdp_real_eu27():
    return sum(
        gross_domestic_product_real_supply_side()
        .loc[_subscript_dict["REGIONS_EU27_I"]]
        .rename({"REGIONS_35_I": "REGIONS_EU27_I!"}),
        dim=["REGIONS_EU27_I!"],
    )


@component.add(
    name="GDP_real_index",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "gross_domestic_product_real_supply_side": 1,
        "base_gross_domestic_product": 1,
    },
)
def gdp_real_index():
    """
    GDP real index (2015=100)
    """
    return (
        zidz(gross_domestic_product_real_supply_side(), base_gross_domestic_product())
        * 100
    )


@component.add(
    name="GDPpc_9R_real",
    units="Mdollars_2015/(Year*person)",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"gdp_real_9r": 1, "population_9_regions": 1},
)
def gdppc_9r_real():
    """
    GDPpc_9R_real
    """
    return zidz(gdp_real_9r(), population_9_regions())


@component.add(
    name="GDPpc_real",
    units="Mdollars_2015/(Year*person)",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "gross_domestic_product_real_supply_side": 1,
        "population_35_regions": 1,
    },
)
def gdppc_real():
    return zidz(gross_domestic_product_real_supply_side(), population_35_regions())


@component.add(
    name="GFCF_until_2015",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I", "SECTORS_ENERGY_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "aux_gfcf_2015": 1, "gross_fixed_capital_formation_real": 1},
)
def gfcf_until_2015():
    """
    GFCF until the year 2015.
    """
    return if_then_else(
        time() > 2015,
        lambda: aux_gfcf_2015(),
        lambda: gross_fixed_capital_formation_real()
        .loc[:, _subscript_dict["SECTORS_ENERGY_I"]]
        .rename({"SECTORS_I": "SECTORS_ENERGY_I"}),
    )


@component.add(
    name="government_debt_to_GDP_ratio_9R",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "government_debt_to_gdp_ratio_eu27": 1,
        "government_debt_to_gdp_ratio": 1,
    },
)
def government_debt_to_gdp_ratio_9r():
    """
    government_debt_to_GDP_ratio_9R
    """
    value = xr.DataArray(
        np.nan, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
    )
    value.loc[["EU27"]] = government_debt_to_gdp_ratio_eu27()
    value.loc[_subscript_dict["REGIONS_8_I"]] = (
        government_debt_to_gdp_ratio()
        .loc[_subscript_dict["REGIONS_8_I"]]
        .rename({"REGIONS_35_I": "REGIONS_8_I"})
        .values
    )
    return value


@component.add(
    name="government_debt_to_GDP_ratio_EU27",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"government_debt": 1, "gross_domestic_product_nominal": 1},
)
def government_debt_to_gdp_ratio_eu27():
    return zidz(
        sum(
            government_debt()
            .loc[_subscript_dict["REGIONS_EU27_I"]]
            .rename({"REGIONS_35_I": "REGIONS_EU27_I!"}),
            dim=["REGIONS_EU27_I!"],
        ),
        sum(
            gross_domestic_product_nominal()
            .loc[_subscript_dict["REGIONS_EU27_I"]]
            .rename({"REGIONS_35_I": "REGIONS_EU27_I!"}),
            dim=["REGIONS_EU27_I!"],
        ),
    )


@component.add(
    name="government_expenditure_1R",
    units="Mdollars/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"government_expenditure": 1},
)
def government_expenditure_1r():
    """
    Total government expenditure.
    """
    return sum(
        government_expenditure().rename({"REGIONS_35_I": "REGIONS_35_I!"}),
        dim=["REGIONS_35_I!"],
    )


@component.add(
    name="labour_compensation_1R_5S",
    units="Mdollars/Year",
    subscripts=["SECTORS_GROUPED_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"labour_compensation_9r_5s": 1},
)
def labour_compensation_1r_5s():
    return sum(
        labour_compensation_9r_5s().rename({"REGIONS_9_I": "REGIONS_9_I!"}),
        dim=["REGIONS_9_I!"],
    )


@component.add(
    name="labour_compensation_35R_5S",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_I", "SECTORS_GROUPED_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "labour_compensation": 1,
        "correspondence_matrix_sector_to_grouped_sectors": 1,
    },
)
def labour_compensation_35r_5s():
    return sum(
        labour_compensation().rename({"SECTORS_I": "SECTORS_I!"})
        * correspondence_matrix_sector_to_grouped_sectors().rename(
            {"SECTORS_I": "SECTORS_I!"}
        ),
        dim=["SECTORS_I!"],
    )


@component.add(
    name="labour_compensation_9R_1S",
    units="Mdollars/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"labour_compensation_9r_5s": 1},
)
def labour_compensation_9r_1s():
    return sum(
        labour_compensation_9r_5s().rename({"SECTORS_GROUPED_I": "SECTORS_GROUPED_I!"}),
        dim=["SECTORS_GROUPED_I!"],
    )


@component.add(
    name="labour_compensation_9R_5S",
    units="Mdollars/Year",
    subscripts=["REGIONS_9_I", "SECTORS_GROUPED_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "labour_compensation_35r_5s": 1,
        "correspondence_matrix_sector_to_grouped_sectors": 1,
        "labour_compensation_eu27": 1,
    },
)
def labour_compensation_9r_5s():
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "SECTORS_GROUPED_I": _subscript_dict["SECTORS_GROUPED_I"],
        },
        ["REGIONS_9_I", "SECTORS_GROUPED_I"],
    )
    value.loc[_subscript_dict["REGIONS_8_I"], :] = (
        labour_compensation_35r_5s()
        .loc[_subscript_dict["REGIONS_8_I"], :]
        .rename({"REGIONS_35_I": "REGIONS_8_I"})
        .values
    )
    value.loc[["EU27"], :] = (
        sum(
            labour_compensation_eu27().rename({"SECTORS_I": "SECTORS_I!"})
            * correspondence_matrix_sector_to_grouped_sectors().rename(
                {"SECTORS_I": "SECTORS_I!"}
            ),
            dim=["SECTORS_I!"],
        )
        .expand_dims({"REGIONS_36_I": ["EU27"]}, 0)
        .values
    )
    return value


@component.add(
    name="labour_compensation_EU27",
    units="Mdollars/Year",
    subscripts=["SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"labour_compensation": 1},
)
def labour_compensation_eu27():
    return sum(
        labour_compensation()
        .loc[_subscript_dict["REGIONS_EU27_I"], :]
        .rename({"REGIONS_35_I": "REGIONS_EU27_I!"}),
        dim=["REGIONS_EU27_I!"],
    )


@component.add(
    name="net_operating_surplus_real_1S",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"net_operating_surplus_real": 1},
)
def net_operating_surplus_real_1s():
    return sum(
        net_operating_surplus_real().rename({"SECTORS_I": "SECTORS_I!"}),
        dim=["SECTORS_I!"],
    )


@component.add(
    name="output_real_9R",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_9_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"output_real": 1, "output_real_eu27": 1},
)
def output_real_9r():
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "SECTORS_I": _subscript_dict["SECTORS_I"],
        },
        ["REGIONS_9_I", "SECTORS_I"],
    )
    value.loc[_subscript_dict["REGIONS_8_I"], :] = (
        output_real()
        .loc[_subscript_dict["REGIONS_8_I"], :]
        .rename({"REGIONS_35_I": "REGIONS_8_I"})
        .values
    )
    value.loc[["EU27"], :] = (
        output_real_eu27().expand_dims({"REGIONS_36_I": ["EU27"]}, 0).values
    )
    return value


@component.add(
    name="output_real_EU27",
    units="Mdollars_2015/Year",
    subscripts=["SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"output_real": 1},
)
def output_real_eu27():
    return sum(
        output_real()
        .loc[_subscript_dict["REGIONS_EU27_I"], :]
        .rename({"REGIONS_35_I": "REGIONS_EU27_I!"}),
        dim=["REGIONS_EU27_I!"],
    )


@component.add(
    name="real_capital_stock_1R_1S",
    units="Mdollars_2015",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"real_capital_stock_9r_1s": 1},
)
def real_capital_stock_1r_1s():
    return sum(
        real_capital_stock_9r_1s().rename({"REGIONS_9_I": "REGIONS_9_I!"}),
        dim=["REGIONS_9_I!"],
    )


@component.add(
    name="real_capital_stock_35R_5S",
    units="Mdollars_2015",
    subscripts=["REGIONS_36_I", "SECTORS_GROUPED_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "real_capital_stock": 1,
        "correspondence_matrix_sector_to_grouped_sectors": 2,
        "real_capital_stock_eu27": 1,
    },
)
def real_capital_stock_35r_5s():
    """
    Variable for interface purposes.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_36_I": _subscript_dict["REGIONS_36_I"],
            "SECTORS_GROUPED_I": _subscript_dict["SECTORS_GROUPED_I"],
        },
        ["REGIONS_36_I", "SECTORS_GROUPED_I"],
    )
    value.loc[_subscript_dict["REGIONS_35_I"], :] = sum(
        real_capital_stock().rename({"SECTORS_I": "SECTORS_I!"})
        * correspondence_matrix_sector_to_grouped_sectors().rename(
            {"SECTORS_I": "SECTORS_I!"}
        ),
        dim=["SECTORS_I!"],
    ).values
    value.loc[["EU27"], :] = (
        sum(
            real_capital_stock_eu27().rename({"SECTORS_I": "SECTORS_I!"})
            * correspondence_matrix_sector_to_grouped_sectors().rename(
                {"SECTORS_I": "SECTORS_I!"}
            ),
            dim=["SECTORS_I!"],
        )
        .expand_dims({"REGIONS_36_I": ["EU27"]}, 0)
        .values
    )
    return value


@component.add(
    name="real_capital_stock_9R_1S",
    units="Mdollars_2015",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"real_capital_stock_9r_5s": 1},
)
def real_capital_stock_9r_1s():
    return sum(
        real_capital_stock_9r_5s().rename({"SECTORS_GROUPED_I": "SECTORS_GROUPED_I!"}),
        dim=["SECTORS_GROUPED_I!"],
    )


@component.add(
    name="real_capital_stock_9R_5S",
    units="Mdollars_2015",
    subscripts=["REGIONS_9_I", "SECTORS_GROUPED_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "real_capital_stock_35r_5s": 1,
        "correspondence_matrix_sector_to_grouped_sectors": 1,
        "real_capital_stock_eu27": 1,
    },
)
def real_capital_stock_9r_5s():
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "SECTORS_GROUPED_I": _subscript_dict["SECTORS_GROUPED_I"],
        },
        ["REGIONS_9_I", "SECTORS_GROUPED_I"],
    )
    value.loc[_subscript_dict["REGIONS_8_I"], :] = (
        real_capital_stock_35r_5s()
        .loc[_subscript_dict["REGIONS_8_I"], :]
        .rename({"REGIONS_36_I": "REGIONS_8_I"})
        .values
    )
    value.loc[["EU27"], :] = (
        sum(
            real_capital_stock_eu27().rename({"SECTORS_I": "SECTORS_I!"})
            * correspondence_matrix_sector_to_grouped_sectors().rename(
                {"SECTORS_I": "SECTORS_I!"}
            ),
            dim=["SECTORS_I!"],
        )
        .expand_dims({"REGIONS_36_I": ["EU27"]}, 0)
        .values
    )
    return value


@component.add(
    name="real_capital_stock_EU27",
    units="Mdollars_2015",
    subscripts=["SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"real_capital_stock": 1},
)
def real_capital_stock_eu27():
    """
    Intermediate variable for interface purposes.
    """
    return sum(
        real_capital_stock()
        .loc[_subscript_dict["REGIONS_EU27_I"], :]
        .rename({"REGIONS_35_I": "REGIONS_EU27_I!"}),
        dim=["REGIONS_EU27_I!"],
    )


@component.add(
    name="SHARE_GFCF_REAL_2015",
    units="1",
    subscripts=["REGIONS_35_I", "SECTORS_ENERGY_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"gfcf_until_2015": 2},
)
def share_gfcf_real_2015():
    return zidz(
        gfcf_until_2015(),
        sum(
            gfcf_until_2015().rename({"SECTORS_ENERGY_I": "SECTORS_ENERGY_I!"}),
            dim=["SECTORS_ENERGY_I!"],
        ).expand_dims({"SECTORS_ENERGY_I": _subscript_dict["SECTORS_ENERGY_I"]}, 1),
    )


@component.add(
    name="share_output_real_EU27",
    units="1",
    subscripts=["REGIONS_EU27_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"output_real": 2},
)
def share_output_real_eu27():
    return zidz(
        output_real()
        .loc[_subscript_dict["REGIONS_EU27_I"], :]
        .rename({"REGIONS_35_I": "REGIONS_EU27_I"}),
        sum(
            output_real()
            .loc[_subscript_dict["REGIONS_EU27_I"], :]
            .rename({"REGIONS_35_I": "REGIONS_EU27_I!"}),
            dim=["REGIONS_EU27_I!"],
        ).expand_dims({"REGIONS_EU27_I": _subscript_dict["REGIONS_EU27_I"]}, 0),
    )


@component.add(
    name="unemployement_rate_9R",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"unemployment_rate": 1, "unemployement_rate_eu27": 1},
)
def unemployement_rate_9r():
    """
    unemployement_rate_9R
    """
    value = xr.DataArray(
        np.nan, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
    )
    value.loc[_subscript_dict["REGIONS_8_I"]] = (
        unemployment_rate()
        .loc[_subscript_dict["REGIONS_8_I"]]
        .rename({"REGIONS_35_I": "REGIONS_8_I"})
        .values
    )
    value.loc[["EU27"]] = unemployement_rate_eu27()
    return value


@component.add(
    name="unemployement_rate_EU27",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"employment_total": 1, "labour_force": 1},
)
def unemployement_rate_eu27():
    return 1 - zidz(
        sum(
            employment_total()
            .loc[_subscript_dict["REGIONS_EU27_I"]]
            .rename({"REGIONS_35_I": "REGIONS_EU27_I!"}),
            dim=["REGIONS_EU27_I!"],
        ),
        sum(
            labour_force()
            .loc[_subscript_dict["REGIONS_EU27_I"]]
            .rename({"REGIONS_35_I": "REGIONS_EU27_I!"}),
            dim=["REGIONS_EU27_I!"],
        ),
    )


@component.add(
    name="unemployment_rate_1R",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"unemployment_rate": 2},
)
def unemployment_rate_1r():
    """
    Unemployment rate.
    """
    return zidz(
        zidz(
            sum(
                unemployment_rate()
                .loc[_subscript_dict["REGIONS_EU27_I"]]
                .rename({"REGIONS_35_I": "REGIONS_EU27_I!"}),
                dim=["REGIONS_EU27_I!"],
            ),
            27,
        )
        + zidz(
            sum(
                unemployment_rate()
                .loc[_subscript_dict["REGIONS_8_I"]]
                .rename({"REGIONS_35_I": "REGIONS_8_I!"}),
                dim=["REGIONS_8_I!"],
            ),
            8,
        ),
        2,
    )
