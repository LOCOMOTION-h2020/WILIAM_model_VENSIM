"""
Module economy.purchaser_to_basic_prices
Translated using PySD version 3.10.0
"""


@component.add(
    name="delayed_TS_final_demand_total_in_purchaser_prices",
    subscripts=["REGIONS_35_I", "SECTORS_I", "FINAL_DEMAND_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_final_demand_total_in_purchaser_prices": 1},
    other_deps={
        "_delayfixed_delayed_ts_final_demand_total_in_purchaser_prices": {
            "initial": {
                "base_final_demand_at_purchaser_prices_total": 1,
                "time_step": 1,
            },
            "step": {
                "time": 1,
                "base_final_demand_at_purchaser_prices_total": 1,
                "final_demand_total_in_purchaser_prices": 1,
            },
        }
    },
)
def delayed_ts_final_demand_total_in_purchaser_prices():
    return _delayfixed_delayed_ts_final_demand_total_in_purchaser_prices()


_delayfixed_delayed_ts_final_demand_total_in_purchaser_prices = DelayFixed(
    lambda: if_then_else(
        time() <= 2015,
        lambda: base_final_demand_at_purchaser_prices_total(),
        lambda: final_demand_total_in_purchaser_prices(),
    ),
    lambda: time_step(),
    lambda: base_final_demand_at_purchaser_prices_total(),
    time_step,
    "_delayfixed_delayed_ts_final_demand_total_in_purchaser_prices",
)


@component.add(
    name="delayed_TS_gross_domestic_product_growth",
    subscripts=["REGIONS_35_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_gross_domestic_product_growth": 1},
    other_deps={
        "_delayfixed_delayed_ts_gross_domestic_product_growth": {
            "initial": {"time_step": 1},
            "step": {"gross_domestic_product_growth_ts": 1},
        }
    },
)
def delayed_ts_gross_domestic_product_growth():
    return _delayfixed_delayed_ts_gross_domestic_product_growth()


_delayfixed_delayed_ts_gross_domestic_product_growth = DelayFixed(
    lambda: gross_domestic_product_growth_ts(),
    lambda: time_step(),
    lambda: xr.DataArray(
        0.02, {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]}, ["REGIONS_35_I"]
    ),
    time_step,
    "_delayfixed_delayed_ts_gross_domestic_product_growth",
)


@component.add(
    name="delayed_TS_gross_domestic_product_nominal",
    subscripts=["REGIONS_35_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_gross_domestic_product_nominal": 1},
    other_deps={
        "_delayfixed_delayed_ts_gross_domestic_product_nominal": {
            "initial": {"initial_delayed_gdp": 1, "time_step": 1},
            "step": {
                "time": 1,
                "initial_delayed_gdp": 1,
                "gross_domestic_product_nominal": 1,
            },
        }
    },
)
def delayed_ts_gross_domestic_product_nominal():
    """
    Delayed time stpe gross domestic porduct nominal
    """
    return _delayfixed_delayed_ts_gross_domestic_product_nominal()


_delayfixed_delayed_ts_gross_domestic_product_nominal = DelayFixed(
    lambda: if_then_else(
        time() <= 2014,
        lambda: initial_delayed_gdp(),
        lambda: gross_domestic_product_nominal(),
    ),
    lambda: time_step(),
    lambda: initial_delayed_gdp(),
    time_step,
    "_delayfixed_delayed_ts_gross_domestic_product_nominal",
)


@component.add(
    name="final_demand_domestic_basic_prices",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I", "FINAL_DEMAND_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "final_demand_domestic_in_purchaser_prices": 1,
        "taxes_products_domestic_final_demand": 1,
        "margins_paid_domestic": 1,
        "margins_received_domestic": 1,
    },
)
def final_demand_domestic_basic_prices():
    """
    Final demand domestic in basic prices and nominal terms.
    """
    return (
        final_demand_domestic_in_purchaser_prices()
        - taxes_products_domestic_final_demand()
        - margins_paid_domestic()
        + margins_received_domestic()
    )


@component.add(
    name="final_demand_domestic_in_basic_prices_real",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I", "FINAL_DEMAND_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_trade": 1,
        "price_transformation": 2,
        "final_demand_domestic_basic_prices": 2,
        "base_price_output": 1,
        "price_output": 1,
    },
)
def final_demand_domestic_in_basic_prices_real():
    """
    Final demand domestic products in basic prices and real terms.
    """
    return if_then_else(
        switch_eco_trade() == 0,
        lambda: final_demand_domestic_basic_prices()
        * zidz(
            xr.DataArray(
                price_transformation(),
                {
                    "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                    "SECTORS_I": _subscript_dict["SECTORS_I"],
                },
                ["REGIONS_35_I", "SECTORS_I"],
            ),
            base_price_output(),
        ),
        lambda: final_demand_domestic_basic_prices()
        * zidz(
            xr.DataArray(
                price_transformation(),
                {
                    "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                    "SECTORS_I": _subscript_dict["SECTORS_I"],
                },
                ["REGIONS_35_I", "SECTORS_I"],
            ),
            price_output(),
        ),
    )


@component.add(
    name="final_demand_domestic_in_purchaser_prices",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I", "FINAL_DEMAND_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_trade": 1,
        "base_import_shares_final_demand": 1,
        "final_demand_total_in_purchaser_prices": 2,
        "import_shares_final_demand_constrained": 1,
    },
)
def final_demand_domestic_in_purchaser_prices():
    """
    Final demand domestic in purchaser prices and nominal terms.
    """
    return if_then_else(
        switch_eco_trade() == 0,
        lambda: final_demand_total_in_purchaser_prices()
        * (1 - base_import_shares_final_demand()),
        lambda: final_demand_total_in_purchaser_prices()
        * (1 - import_shares_final_demand_constrained()),
    )


@component.add(
    name="final_demand_dometic_in_basic_prices_real_by_component",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I", "FINAL_DEMAND_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"final_demand_domestic_in_basic_prices_real": 1},
)
def final_demand_dometic_in_basic_prices_real_by_component():
    """
    Total final demand real in basic prices
    """
    return sum(
        final_demand_domestic_in_basic_prices_real().rename(
            {"SECTORS_I": "SECTORS_I!"}
        ),
        dim=["SECTORS_I!"],
    )


@component.add(
    name="final_demand_imports_basic_prices",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I", "REGIONS_35_MAP_I", "FINAL_DEMAND_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "final_demand_imports_by_origin_in_purchaser_prices": 1,
        "margins_paid_imports": 1,
        "taxes_products_imports_final_demand": 1,
        "margins_received_imports": 1,
    },
)
def final_demand_imports_basic_prices():
    """
    Final demand imports in basic prices and nominal terms.
    """
    return (
        final_demand_imports_by_origin_in_purchaser_prices().rename(
            {"REGIONS_35_MAP_I": "REGIONS_35_I", "REGIONS_35_I": "REGIONS_35_MAP_I"}
        )
        - margins_paid_imports()
        - taxes_products_imports_final_demand()
        + margins_received_imports()
    )


@component.add(
    name="final_demand_imports_by_origin_in_purchaser_prices",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_MAP_I", "SECTORS_I", "REGIONS_35_I", "FINAL_DEMAND_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_trade": 1,
        "base_import_shares_origin_final_demand": 1,
        "final_demand_imports_in_purchaser_prices": 2,
        "import_shares_origin_final_demand": 1,
    },
)
def final_demand_imports_by_origin_in_purchaser_prices():
    """
    Final demand imports by origin in purchaser prices and nominal terms.
    """
    return if_then_else(
        switch_eco_trade() == 0,
        lambda: final_demand_imports_in_purchaser_prices()
        * base_import_shares_origin_final_demand().transpose(
            "REGIONS_35_I", "SECTORS_I", "FINAL_DEMAND_I", "REGIONS_35_MAP_I"
        ),
        lambda: final_demand_imports_in_purchaser_prices()
        * import_shares_origin_final_demand().transpose(
            "REGIONS_35_I", "SECTORS_I", "FINAL_DEMAND_I", "REGIONS_35_MAP_I"
        ),
    ).transpose("REGIONS_35_MAP_I", "SECTORS_I", "REGIONS_35_I", "FINAL_DEMAND_I")


@component.add(
    name="final_demand_imports_in_basic_prices_real",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I", "REGIONS_35_MAP_I", "FINAL_DEMAND_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_trade": 1,
        "price_transformation": 2,
        "final_demand_imports_basic_prices": 2,
        "base_price_output": 1,
        "price_output": 1,
    },
)
def final_demand_imports_in_basic_prices_real():
    """
    Final demand imported products in basic prices and real terms.
    """
    return if_then_else(
        switch_eco_trade() == 0,
        lambda: final_demand_imports_basic_prices()
        * zidz(
            xr.DataArray(
                price_transformation(),
                {
                    "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                    "SECTORS_I": _subscript_dict["SECTORS_I"],
                },
                ["REGIONS_35_I", "SECTORS_I"],
            ),
            base_price_output(),
        ),
        lambda: final_demand_imports_basic_prices()
        * zidz(
            xr.DataArray(
                price_transformation(),
                {
                    "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                    "SECTORS_I": _subscript_dict["SECTORS_I"],
                },
                ["REGIONS_35_I", "SECTORS_I"],
            ),
            price_output(),
        ),
    )


@component.add(
    name="final_demand_imports_in_basic_prices_real_by_component",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I", "FINAL_DEMAND_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"final_demand_imports_in_basic_prices_real": 1},
)
def final_demand_imports_in_basic_prices_real_by_component():
    """
    Total final demand real in basic prices
    """
    return sum(
        final_demand_imports_in_basic_prices_real().rename(
            {
                "REGIONS_35_I": "REGIONS_35_MAP_I!",
                "SECTORS_I": "SECTORS_I!",
                "REGIONS_35_MAP_I": "REGIONS_35_I",
            }
        ),
        dim=["REGIONS_35_MAP_I!", "SECTORS_I!"],
    )


@component.add(
    name="final_demand_imports_in_purchaser_prices",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I", "FINAL_DEMAND_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_trade": 1,
        "base_import_shares_final_demand": 1,
        "final_demand_total_in_purchaser_prices": 2,
        "import_shares_final_demand_constrained": 1,
    },
)
def final_demand_imports_in_purchaser_prices():
    """
    Final demand imports in purchaser prices and nominal terms.
    """
    return if_then_else(
        switch_eco_trade() == 0,
        lambda: final_demand_total_in_purchaser_prices()
        * base_import_shares_final_demand(),
        lambda: final_demand_total_in_purchaser_prices()
        * import_shares_final_demand_constrained(),
    )


@component.add(
    name="final_demand_total_in_basic_prices_real",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I", "FINAL_DEMAND_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "final_demand_dometic_in_basic_prices_real_by_component": 1,
        "final_demand_imports_in_basic_prices_real_by_component": 1,
    },
)
def final_demand_total_in_basic_prices_real():
    """
    Total final demand real in basic prices
    """
    return (
        final_demand_dometic_in_basic_prices_real_by_component()
        + final_demand_imports_in_basic_prices_real_by_component()
    )


@component.add(
    name="final_demand_total_in_purchaser_prices",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I", "FINAL_DEMAND_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "base_final_demand_at_purchaser_prices_total": 2,
        "delayed_ts_gross_domestic_product_growth": 1,
        "delayed_ts_final_demand_total_in_purchaser_prices": 1,
        "switch_eco_government": 1,
        "base_government_consumption_at_purchaser_prices": 1,
        "government_consumption_purchaser_prices": 1,
        "switch_eco_investment": 1,
        "base_gross_fixed_capital_formation_by_good_at_purchaser_prices": 1,
        "gross_fixed_capital_formation_by_good": 1,
        "households_consumption_purchaser_prices": 1,
        "switch_eco_households": 1,
    },
)
def final_demand_total_in_purchaser_prices():
    """
    CONSUMPTION_W, NON_PROFIT_W, GOVERNMENT_W, GROSS_FIXED_CAPITAL_FORMATION_W, INVENTORY_W, ABROAD_W IF_THEN_ELSE(Time<=2015,BASE_FINAL_DEMAND_AT_PURCHASER_PRICES_TOTAL[REGIONS_35_I,SECT ORS_I,FINAL_DEMAND_EXCEPT_CONSUMPTION_INVESTMENT_GOVERNMENT_I ],BASE_FINAL_DEMAND_AT_PURCHASER_PRICES_TOTAL[REGIONS_35_I,SECTORS_I,FINAL_ DEMAND_EXCEPT_CONSUMPTION_INVESTMENT_GOVERNMENT_I])
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "SECTORS_I": _subscript_dict["SECTORS_I"],
            "FINAL_DEMAND_I": _subscript_dict["FINAL_DEMAND_I"],
        },
        ["REGIONS_35_I", "SECTORS_I", "FINAL_DEMAND_I"],
    )
    value.loc[
        :, :, _subscript_dict["FINAL_DEMAND_EXCEPT_CONSUMPTION_INVESTMENT_GOVERNMENT_I"]
    ] = if_then_else(
        time() <= 2015,
        lambda: base_final_demand_at_purchaser_prices_total()
        .loc[
            :,
            :,
            _subscript_dict["FINAL_DEMAND_EXCEPT_CONSUMPTION_INVESTMENT_GOVERNMENT_I"],
        ]
        .rename(
            {
                "FINAL_DEMAND_I": "FINAL_DEMAND_EXCEPT_CONSUMPTION_INVESTMENT_GOVERNMENT_I"
            }
        ),
        lambda: (1 + delayed_ts_gross_domestic_product_growth())
        * delayed_ts_final_demand_total_in_purchaser_prices()
        .loc[
            :,
            :,
            _subscript_dict["FINAL_DEMAND_EXCEPT_CONSUMPTION_INVESTMENT_GOVERNMENT_I"],
        ]
        .rename(
            {
                "FINAL_DEMAND_I": "FINAL_DEMAND_EXCEPT_CONSUMPTION_INVESTMENT_GOVERNMENT_I"
            }
        ),
    ).values
    value.loc[:, :, ["GOVERNMENT_W"]] = (
        if_then_else(
            switch_eco_government() == 0,
            lambda: base_government_consumption_at_purchaser_prices(),
            lambda: government_consumption_purchaser_prices(),
        )
        .expand_dims(
            {"FINAL_DEMAND_CONSUMPTION_INVESTMENT_GOVERNMENT_I": ["GOVERNMENT_W"]}, 2
        )
        .values
    )
    value.loc[:, :, ["GROSS_FIXED_CAPITAL_FORMATION_W"]] = (
        if_then_else(
            switch_eco_investment() == 0,
            lambda: base_gross_fixed_capital_formation_by_good_at_purchaser_prices(),
            lambda: gross_fixed_capital_formation_by_good(),
        )
        .expand_dims(
            {
                "FINAL_DEMAND_CONSUMPTION_INVESTMENT_GOVERNMENT_I": [
                    "GROSS_FIXED_CAPITAL_FORMATION_W"
                ]
            },
            2,
        )
        .values
    )
    value.loc[:, :, ["CONSUMPTION_W"]] = (
        if_then_else(
            switch_eco_households() == 0,
            lambda: base_final_demand_at_purchaser_prices_total()
            .loc[:, :, "CONSUMPTION_W"]
            .reset_coords(drop=True),
            lambda: households_consumption_purchaser_prices(),
        )
        .expand_dims(
            {"FINAL_DEMAND_CONSUMPTION_INVESTMENT_GOVERNMENT_I": ["CONSUMPTION_W"]}, 2
        )
        .values
    )
    return value


@component.add(
    name="gross_domestic_product_growth_TS",
    units="DMNL",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "gross_domestic_product_nominal": 1,
        "delayed_ts_gross_domestic_product_nominal": 1,
    },
)
def gross_domestic_product_growth_ts():
    """
    Gros domestic product growth by Time Step
    """
    return (
        zidz(
            gross_domestic_product_nominal(),
            delayed_ts_gross_domestic_product_nominal(),
        )
        - 1
    )


@component.add(
    name="margins_paid_domestic",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I", "FINAL_DEMAND_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "final_demand_domestic_in_purchaser_prices": 1,
        "taxes_products_domestic_final_demand": 1,
        "trade_and_transportation_margins_paid_for_domestic_products_for_final_demand": 1,
    },
)
def margins_paid_domestic():
    """
    Margins paid domestic in nominal terms.
    """
    return (
        final_demand_domestic_in_purchaser_prices()
        - taxes_products_domestic_final_demand()
    ) * (
        1
        - zidz(
            xr.DataArray(
                1,
                {
                    "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                    "SECTORS_I": _subscript_dict["SECTORS_I"],
                    "FINAL_DEMAND_I": _subscript_dict["FINAL_DEMAND_I"],
                },
                ["REGIONS_35_I", "SECTORS_I", "FINAL_DEMAND_I"],
            ),
            1
            + trade_and_transportation_margins_paid_for_domestic_products_for_final_demand(),
        )
    )


@component.add(
    name="margins_paid_imports",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I", "REGIONS_35_MAP_I", "FINAL_DEMAND_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "final_demand_imports_by_origin_in_purchaser_prices": 1,
        "taxes_products_imports_final_demand": 1,
        "trade_and_transportation_margins_paid_for_imported_products_for_final_demand": 1,
    },
)
def margins_paid_imports():
    """
    Margins paid imports in nominal terms.
    """
    return (
        final_demand_imports_by_origin_in_purchaser_prices().rename(
            {"REGIONS_35_MAP_I": "REGIONS_35_I", "REGIONS_35_I": "REGIONS_35_MAP_I"}
        )
        - taxes_products_imports_final_demand()
    ) * (
        1
        - zidz(
            xr.DataArray(
                1,
                {
                    "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                    "SECTORS_I": _subscript_dict["SECTORS_I"],
                    "REGIONS_35_MAP_I": _subscript_dict["REGIONS_35_MAP_I"],
                    "FINAL_DEMAND_I": _subscript_dict["FINAL_DEMAND_I"],
                },
                ["REGIONS_35_I", "SECTORS_I", "REGIONS_35_MAP_I", "FINAL_DEMAND_I"],
            ),
            1
            + trade_and_transportation_margins_paid_for_imported_products_for_final_demand().rename(
                {"REGIONS_35_MAP_I": "REGIONS_35_I", "REGIONS_35_I": "REGIONS_35_MAP_I"}
            ),
        )
    )


@component.add(
    name="margins_received_domestic",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I", "FINAL_DEMAND_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "margins_paid_domestic": 1,
        "trade_and_transportation_margins_received_for_domestic_products_for_final_demand": 1,
    },
)
def margins_received_domestic():
    """
    Margins recived domestic in nominal terms.
    """
    return (
        sum(
            margins_paid_domestic().rename({"SECTORS_I": "SECTORS_I!"}),
            dim=["SECTORS_I!"],
        )
        * trade_and_transportation_margins_received_for_domestic_products_for_final_demand().transpose(
            "REGIONS_35_I", "FINAL_DEMAND_I", "SECTORS_I"
        )
    ).transpose("REGIONS_35_I", "SECTORS_I", "FINAL_DEMAND_I")


@component.add(
    name="margins_received_imports",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I", "REGIONS_35_MAP_I", "FINAL_DEMAND_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "margins_paid_imports": 1,
        "trade_and_transportation_margins_received_for_imported_products_for_final_demand": 1,
    },
)
def margins_received_imports():
    """
    Margins recived imports in nominal terms.
    """
    return (
        sum(
            margins_paid_imports().rename({"SECTORS_I": "SECTORS_I!"}),
            dim=["SECTORS_I!"],
        )
        * trade_and_transportation_margins_received_for_imported_products_for_final_demand()
        .rename(
            {"REGIONS_35_MAP_I": "REGIONS_35_I", "REGIONS_35_I": "REGIONS_35_MAP_I"}
        )
        .transpose("REGIONS_35_I", "REGIONS_35_MAP_I", "FINAL_DEMAND_I", "SECTORS_I")
    ).transpose("REGIONS_35_I", "SECTORS_I", "REGIONS_35_MAP_I", "FINAL_DEMAND_I")


@component.add(
    name="SWITCH_ECO_TRADE",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_eco_trade"},
)
def switch_eco_trade():
    """
    This switch can take two values: 0: Trade shares remain constant 1: Trade shares linked to trade module
    """
    return _ext_constant_switch_eco_trade()


_ext_constant_switch_eco_trade = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_ECO_TRADE",
    {},
    _root,
    {},
    "_ext_constant_switch_eco_trade",
)


@component.add(
    name="taxes_products_domestic_final_demand",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I", "FINAL_DEMAND_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "final_demand_domestic_in_purchaser_prices": 1,
        "tax_rate_products_domestic_for_final_demand": 1,
    },
)
def taxes_products_domestic_final_demand():
    """
    Net taxes on domestic final products in nominal terms.
    """
    return final_demand_domestic_in_purchaser_prices() * (
        1
        - zidz(
            xr.DataArray(
                1,
                {
                    "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                    "SECTORS_I": _subscript_dict["SECTORS_I"],
                    "FINAL_DEMAND_I": _subscript_dict["FINAL_DEMAND_I"],
                },
                ["REGIONS_35_I", "SECTORS_I", "FINAL_DEMAND_I"],
            ),
            1 + tax_rate_products_domestic_for_final_demand(),
        )
    )


@component.add(
    name="taxes_products_domestic_final_demand_real",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I", "FINAL_DEMAND_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "final_demand_domestic_in_basic_prices_real": 2,
        "trade_and_transportation_margins_paid_for_domestic_products_for_final_demand": 2,
        "trade_and_transportation_margins_received_for_domestic_products_for_final_demand": 1,
        "base_tax_rate_products_domestic_for_final_demand": 1,
    },
)
def taxes_products_domestic_final_demand_real():
    """
    Taxes on domestic final products in real terms
    """
    return (
        final_demand_domestic_in_basic_prices_real()
        * (
            1
            + trade_and_transportation_margins_paid_for_domestic_products_for_final_demand()
        )
        - (
            sum(
                final_demand_domestic_in_basic_prices_real().rename(
                    {"SECTORS_I": "SECTORS_MAP_I!"}
                )
                * trade_and_transportation_margins_paid_for_domestic_products_for_final_demand().rename(
                    {"SECTORS_I": "SECTORS_MAP_I!"}
                ),
                dim=["SECTORS_MAP_I!"],
            )
            * trade_and_transportation_margins_received_for_domestic_products_for_final_demand().transpose(
                "REGIONS_35_I", "FINAL_DEMAND_I", "SECTORS_I"
            )
        ).transpose("REGIONS_35_I", "SECTORS_I", "FINAL_DEMAND_I")
    ) * base_tax_rate_products_domestic_for_final_demand()


@component.add(
    name="taxes_products_imports_final_demand",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I", "REGIONS_35_MAP_I", "FINAL_DEMAND_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "final_demand_imports_by_origin_in_purchaser_prices": 1,
        "tax_rate_products_imports_for_final_demand": 1,
    },
)
def taxes_products_imports_final_demand():
    """
    Net taxes on imported final products in nominal terms.
    """
    return final_demand_imports_by_origin_in_purchaser_prices().rename(
        {"REGIONS_35_MAP_I": "REGIONS_35_I", "REGIONS_35_I": "REGIONS_35_MAP_I"}
    ) * (
        1
        - zidz(
            xr.DataArray(
                1,
                {
                    "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                    "SECTORS_I": _subscript_dict["SECTORS_I"],
                    "REGIONS_35_MAP_I": _subscript_dict["REGIONS_35_MAP_I"],
                    "FINAL_DEMAND_I": _subscript_dict["FINAL_DEMAND_I"],
                },
                ["REGIONS_35_I", "SECTORS_I", "REGIONS_35_MAP_I", "FINAL_DEMAND_I"],
            ),
            1 + tax_rate_products_imports_for_final_demand(),
        )
    )


@component.add(
    name="taxes_products_imports_final_demand_real",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I", "REGIONS_35_MAP_I", "FINAL_DEMAND_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "final_demand_imports_in_basic_prices_real": 2,
        "trade_and_transportation_margins_paid_for_imported_products_for_final_demand": 2,
        "trade_and_transportation_margins_received_for_imported_products_for_final_demand": 1,
        "tax_rate_products_imports_for_final_demand": 1,
    },
)
def taxes_products_imports_final_demand_real():
    """
    Taxes on imported final products in real terms
    """
    return (
        final_demand_imports_in_basic_prices_real()
        * (
            1
            + trade_and_transportation_margins_paid_for_imported_products_for_final_demand().rename(
                {"REGIONS_35_MAP_I": "REGIONS_35_I", "REGIONS_35_I": "REGIONS_35_MAP_I"}
            )
        )
        - (
            sum(
                final_demand_imports_in_basic_prices_real().rename(
                    {"SECTORS_I": "SECTORS_I!"}
                )
                * trade_and_transportation_margins_paid_for_imported_products_for_final_demand().rename(
                    {
                        "REGIONS_35_MAP_I": "REGIONS_35_I",
                        "SECTORS_I": "SECTORS_I!",
                        "REGIONS_35_I": "REGIONS_35_MAP_I",
                    }
                ),
                dim=["SECTORS_I!"],
            )
            * trade_and_transportation_margins_received_for_imported_products_for_final_demand()
            .rename(
                {"REGIONS_35_MAP_I": "REGIONS_35_I", "REGIONS_35_I": "REGIONS_35_MAP_I"}
            )
            .transpose(
                "REGIONS_35_I", "REGIONS_35_MAP_I", "FINAL_DEMAND_I", "SECTORS_I"
            )
        ).transpose("REGIONS_35_I", "SECTORS_I", "REGIONS_35_MAP_I", "FINAL_DEMAND_I")
    ) * tax_rate_products_imports_for_final_demand()
