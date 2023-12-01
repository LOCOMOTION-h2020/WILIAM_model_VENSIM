"""
Module economy.primary_inputs
Translated using PySD version 3.10.0
"""


@component.add(
    name="delayed_TS_net_operating_surplus_total",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_net_operating_surplus_total": 1},
    other_deps={
        "_delayfixed_delayed_ts_net_operating_surplus_total": {
            "initial": {"initial_delayed_net_operating_surplus": 1, "time_step": 1},
            "step": {
                "time": 1,
                "base_net_operating_surplus": 1,
                "net_operating_surplus": 1,
            },
        }
    },
)
def delayed_ts_net_operating_surplus_total():
    """
    Delayed total net operating surplus.
    """
    return _delayfixed_delayed_ts_net_operating_surplus_total()


_delayfixed_delayed_ts_net_operating_surplus_total = DelayFixed(
    lambda: if_then_else(
        time() <= 2015,
        lambda: base_net_operating_surplus(),
        lambda: sum(
            net_operating_surplus().rename(
                {"REGIONS_35_MAP_I": "REGIONS_35_I", "SECTORS_MAP_I": "SECTORS_I!"}
            ),
            dim=["SECTORS_I!"],
        ),
    ),
    lambda: time_step(),
    lambda: sum(
        initial_delayed_net_operating_surplus().rename({"SECTORS_I": "SECTORS_I!"}),
        dim=["SECTORS_I!"],
    ),
    time_step,
    "_delayfixed_delayed_ts_net_operating_surplus_total",
)


@component.add(
    name="gross_domestic_product_deflator",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "gross_domestic_product_nominal": 1,
        "gross_domestic_product_real_supply_side": 1,
    },
)
def gross_domestic_product_deflator():
    """
    Deflator of the gross domestic product
    """
    return zidz(
        gross_domestic_product_nominal(), gross_domestic_product_real_supply_side()
    )


@component.add(
    name="gross_domestic_product_nominal",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "gross_value_added": 1,
        "taxes_products_by_sector": 1,
        "taxes_products_final_demand": 1,
    },
)
def gross_domestic_product_nominal():
    """
    Gross domestic product in nominal terms.
    """
    return (
        sum(
            gross_value_added().rename(
                {"REGIONS_35_MAP_I": "REGIONS_35_I", "SECTORS_MAP_I": "SECTORS_I!"}
            ),
            dim=["SECTORS_I!"],
        )
        + sum(
            taxes_products_by_sector().rename(
                {"REGIONS_35_MAP_I": "REGIONS_35_I", "SECTORS_MAP_I": "SECTORS_I!"}
            ),
            dim=["SECTORS_I!"],
        )
        + sum(
            taxes_products_final_demand().rename(
                {
                    "REGIONS_35_MAP_I": "REGIONS_35_I",
                    "FINAL_DEMAND_I": "FINAL_DEMAND_I!",
                }
            ),
            dim=["FINAL_DEMAND_I!"],
        )
    )


@component.add(
    name="gross_domestic_product_real_demand_side",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "final_demand_dometic_in_basic_prices_real_by_component": 1,
        "final_demand_imports_in_basic_prices_real_by_component": 1,
        "total_exports_real_by_product": 1,
        "total_imports_real_by_product": 1,
        "taxes_products_final_demand_real": 1,
    },
)
def gross_domestic_product_real_demand_side():
    """
    Gross domrestic product in real terms from the demand side
    """
    return (
        sum(
            final_demand_dometic_in_basic_prices_real_by_component().rename(
                {"FINAL_DEMAND_I": "FINAL_DEMAND_I!"}
            ),
            dim=["FINAL_DEMAND_I!"],
        )
        + sum(
            final_demand_imports_in_basic_prices_real_by_component().rename(
                {"FINAL_DEMAND_I": "FINAL_DEMAND_I!"}
            ),
            dim=["FINAL_DEMAND_I!"],
        )
        + sum(
            total_exports_real_by_product().rename({"SECTORS_I": "SECTORS_I!"}),
            dim=["SECTORS_I!"],
        )
        - sum(
            total_imports_real_by_product().rename({"SECTORS_I": "SECTORS_I!"}),
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


@component.add(
    name="gross_domestic_product_real_supply_side",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "gross_value_added_real": 1,
        "taxes_products_by_sector_real": 1,
        "taxes_products_final_demand_real": 1,
    },
)
def gross_domestic_product_real_supply_side():
    """
    Gross domestic porduct in real terms calculated from the supply side
    """
    return (
        sum(
            gross_value_added_real().rename(
                {"REGIONS_35_MAP_I": "REGIONS_35_I", "SECTORS_MAP_I": "SECTORS_I!"}
            ),
            dim=["SECTORS_I!"],
        )
        + sum(
            taxes_products_by_sector_real().rename(
                {"REGIONS_35_MAP_I": "REGIONS_35_I", "SECTORS_MAP_I": "SECTORS_I!"}
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


@component.add(
    name="gross_value_added",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_MAP_I", "SECTORS_MAP_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_primary_inputs": 1,
        "net_value_added": 2,
        "base_consumption_fixed_capital": 1,
        "consumption_fixed_capital": 1,
    },
)
def gross_value_added():
    """
    Gross value added in nominal terms.
    """
    return if_then_else(
        switch_eco_primary_inputs() == 0,
        lambda: net_value_added().rename(
            {"REGIONS_35_I": "REGIONS_35_MAP_I", "SECTORS_I": "SECTORS_MAP_I"}
        )
        + base_consumption_fixed_capital().rename(
            {"REGIONS_35_I": "REGIONS_35_MAP_I", "SECTORS_I": "SECTORS_MAP_I"}
        ),
        lambda: net_value_added().rename(
            {"REGIONS_35_I": "REGIONS_35_MAP_I", "SECTORS_I": "SECTORS_MAP_I"}
        )
        + consumption_fixed_capital().rename(
            {"REGIONS_35_I": "REGIONS_35_MAP_I", "SECTORS_I": "SECTORS_MAP_I"}
        ),
    )


@component.add(
    name="gross_value_added_real",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_MAP_I", "SECTORS_MAP_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_primary_inputs": 1,
        "base_output_real": 1,
        "initial_intermediate_imports_and_exports_real": 1,
        "initial_intermediates_domestic_real": 1,
        "taxes_products_by_sector_real": 2,
        "intermediate_imports_and_exports_real": 1,
        "intermediates_domestic_real": 1,
        "output_real": 1,
    },
)
def gross_value_added_real():
    """
    Gross value added in real terms
    """
    return if_then_else(
        switch_eco_primary_inputs() == 0,
        lambda: base_output_real().rename(
            {"REGIONS_35_I": "REGIONS_35_MAP_I", "SECTORS_I": "SECTORS_MAP_I"}
        )
        - sum(
            initial_intermediates_domestic_real().rename(
                {"REGIONS_35_I": "REGIONS_35_MAP_I", "SECTORS_I": "SECTORS_I!"}
            ),
            dim=["SECTORS_I!"],
        )
        - sum(
            initial_intermediate_imports_and_exports_real().rename(
                {"REGIONS_35_I": "REGIONS_35_I!", "SECTORS_I": "SECTORS_I!"}
            ),
            dim=["REGIONS_35_I!", "SECTORS_I!"],
        )
        - taxes_products_by_sector_real(),
        lambda: output_real().rename(
            {"REGIONS_35_I": "REGIONS_35_MAP_I", "SECTORS_I": "SECTORS_MAP_I"}
        )
        - sum(
            intermediates_domestic_real().rename(
                {"REGIONS_35_I": "REGIONS_35_MAP_I", "SECTORS_I": "SECTORS_I!"}
            ),
            dim=["SECTORS_I!"],
        )
        - sum(
            intermediate_imports_and_exports_real().rename(
                {"REGIONS_35_I": "REGIONS_35_I!", "SECTORS_I": "SECTORS_I!"}
            ),
            dim=["REGIONS_35_I!", "SECTORS_I!"],
        )
        - taxes_products_by_sector_real(),
    )


@component.add(
    name="INITIAL_INTERMEDIATE_IMPORTS_AND_EXPORTS_REAL",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I", "REGIONS_35_MAP_I", "SECTORS_MAP_I"],
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_initial_intermediate_imports_and_exports_real": 1},
    other_deps={
        "_initial_initial_intermediate_imports_and_exports_real": {
            "initial": {"intermediate_imports_and_exports_real": 1},
            "step": {},
        }
    },
)
def initial_intermediate_imports_and_exports_real():
    return _initial_initial_intermediate_imports_and_exports_real()


_initial_initial_intermediate_imports_and_exports_real = Initial(
    lambda: intermediate_imports_and_exports_real(),
    "_initial_initial_intermediate_imports_and_exports_real",
)


@component.add(
    name="INITIAL_INTERMEDIATES_DOMESTIC_REAL",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I", "SECTORS_MAP_I"],
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_initial_intermediates_domestic_real": 1},
    other_deps={
        "_initial_initial_intermediates_domestic_real": {
            "initial": {"intermediates_domestic_real": 1},
            "step": {},
        }
    },
)
def initial_intermediates_domestic_real():
    """
    Initial value for variable intermediates_domestic_real
    """
    return _initial_initial_intermediates_domestic_real()


_initial_initial_intermediates_domestic_real = Initial(
    lambda: intermediates_domestic_real(),
    "_initial_initial_intermediates_domestic_real",
)


@component.add(
    name="INITIAL_TAXES_PRODUCTS_DOMESTIC",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I", "FINAL_DEMAND_I"],
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_initial_taxes_products_domestic": 1},
    other_deps={
        "_initial_initial_taxes_products_domestic": {
            "initial": {"taxes_products_domestic_final_demand_real": 1},
            "step": {},
        }
    },
)
def initial_taxes_products_domestic():
    return _initial_initial_taxes_products_domestic()


_initial_initial_taxes_products_domestic = Initial(
    lambda: taxes_products_domestic_final_demand_real(),
    "_initial_initial_taxes_products_domestic",
)


@component.add(
    name="INITIAL_TAXES_PRODUCTS_IMPORTS",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I", "REGIONS_35_MAP_I", "FINAL_DEMAND_I"],
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_initial_taxes_products_imports": 1},
    other_deps={
        "_initial_initial_taxes_products_imports": {
            "initial": {"taxes_products_imports_final_demand_real": 1},
            "step": {},
        }
    },
)
def initial_taxes_products_imports():
    return _initial_initial_taxes_products_imports()


_initial_initial_taxes_products_imports = Initial(
    lambda: taxes_products_imports_final_demand_real(),
    "_initial_initial_taxes_products_imports",
)


@component.add(
    name="net_domestic_product_real",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_primary_inputs": 1,
        "gross_domestic_product_real_supply_side": 2,
        "base_consumption_fixed_capital_real": 1,
        "consumption_fixed_capital_real": 1,
    },
)
def net_domestic_product_real():
    """
    Net domestic product in real terms. This is equivalent to GDP but removing the part of the investments associated with the replacement of capital due to depreciation and climate change damages.
    """
    return if_then_else(
        switch_eco_primary_inputs() == 0,
        lambda: gross_domestic_product_real_supply_side()
        - sum(
            base_consumption_fixed_capital_real().rename({"SECTORS_I": "SECTORS_I!"}),
            dim=["SECTORS_I!"],
        ),
        lambda: gross_domestic_product_real_supply_side()
        - sum(
            consumption_fixed_capital_real().rename({"SECTORS_I": "SECTORS_I!"}),
            dim=["SECTORS_I!"],
        ),
    )


@component.add(
    name="net_operating_surplus",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_MAP_I", "SECTORS_MAP_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "mark_up": 1,
        "output_real": 1,
        "price_output": 1,
        "price_transformation": 1,
    },
)
def net_operating_surplus():
    """
    Gross value added in nominal terms. IF_THEN_ELSE(SWITCH_PRIMARY_INPUTS=0, MARK_UP[REGIONS 35 MAP I,SECTORS MAP I]* ( SUM(BASE_INTERMEDIATES_DOMESTIC_REAL[REGIONS 35 MAP I,SECTORS I!,SECTORS MAP I]) +SUM(BASE_INTERMEDIATE_IMPORTS_AND_EXPORTS_REAL[REGIONS 35 I!,SECTORS I!,REGIONS 35 MAP I,SECTORS MAP I]) +BASE_TAXES_PRODUCTS_BY_SECTOR[REGIONS 35 MAP I,SECTORS MAP I] +BASE_TAXES_PRODUCTION[REGIONS 35 MAP I,SECTORS MAP I] +BASE_LABOUR_COMPENSATION[REGIONS 35 MAP I,SECTORS MAP I] +BASE_CONSUMPTION_FIXED_CAPITAL[REGIONS 35 MAP I,SECTORS MAP I]), MARK_UP[REGIONS 35 MAP I,SECTORS MAP I]* ( SUM(intermediates_domestic_real[REGIONS 35 MAP I,SECTORS I!,SECTORS MAP I]*price_output[REGIONS 35 MAP I,SECTORS MAP I] /PRICE_TRANSFORMATION) +SUM(intermediate_imports_and_exports_real[REGIONS 35 I!,SECTORS I!,REGIONS 35 MAP I,SECTORS MAP I]*price_output[REGIONS 35 MAP I ,SECTORS MAP I]/PRICE_TRANSFORMATION) +taxes_products_by_sector[REGIONS 35 MAP I,SECTORS MAP I] +taxes_production[REGIONS 35 MAP I,SECTORS MAP I] +labour_compensation[REGIONS 35 MAP I,SECTORS MAP I] +consumption_fixed_capital[REGIONS 35 MAP I,SECTORS MAP I] ) )
    """
    return (
        mark_up().rename(
            {"REGIONS_35_I": "REGIONS_35_MAP_I", "SECTORS_I": "SECTORS_MAP_I"}
        )
        * output_real().rename(
            {"REGIONS_35_I": "REGIONS_35_MAP_I", "SECTORS_I": "SECTORS_MAP_I"}
        )
        * price_output().rename(
            {"REGIONS_35_I": "REGIONS_35_MAP_I", "SECTORS_I": "SECTORS_MAP_I"}
        )
        / price_transformation()
    )


@component.add(
    name="net_operating_surplus_real",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "net_value_added_real": 1,
        "labour_compensation_real": 1,
        "taxes_production_real": 1,
    },
)
def net_operating_surplus_real():
    """
    Net operating surplus in real terms.
    """
    return net_value_added_real() - labour_compensation_real() - taxes_production_real()


@component.add(
    name="net_value_added",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_primary_inputs": 1,
        "net_operating_surplus": 2,
        "base_taxes_production": 1,
        "base_labour_compensation": 1,
        "taxes_production": 1,
        "labour_compensation": 1,
    },
)
def net_value_added():
    """
    Net value added in nominal terms.
    """
    return if_then_else(
        switch_eco_primary_inputs() == 0,
        lambda: net_operating_surplus().rename(
            {"REGIONS_35_MAP_I": "REGIONS_35_I", "SECTORS_MAP_I": "SECTORS_I"}
        )
        + base_labour_compensation()
        + base_taxes_production(),
        lambda: net_operating_surplus().rename(
            {"REGIONS_35_MAP_I": "REGIONS_35_I", "SECTORS_MAP_I": "SECTORS_I"}
        )
        + labour_compensation()
        + taxes_production(),
    )


@component.add(
    name="net_value_added_real",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_primary_inputs": 1,
        "gross_value_added_real": 2,
        "base_consumption_fixed_capital_real": 1,
        "consumption_fixed_capital_real": 1,
    },
)
def net_value_added_real():
    """
    Net value added in real terms.
    """
    return if_then_else(
        switch_eco_primary_inputs() == 0,
        lambda: gross_value_added_real().rename(
            {"REGIONS_35_MAP_I": "REGIONS_35_I", "SECTORS_MAP_I": "SECTORS_I"}
        )
        - base_consumption_fixed_capital_real(),
        lambda: gross_value_added_real().rename(
            {"REGIONS_35_MAP_I": "REGIONS_35_I", "SECTORS_MAP_I": "SECTORS_I"}
        )
        - consumption_fixed_capital_real(),
    )


@component.add(
    name="SWITCH_ECO_PRIMARY_INPUTS",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_eco_primary_inputs"},
)
def switch_eco_primary_inputs():
    """
    This switch can take two values: 0: the (sub)module runs isolated from the rest of WILIAM, replacing inter(sub)module variables with exogenous parameters. 1: the (sub)module runs integrated with the rest of WILIAM.
    """
    return _ext_constant_switch_eco_primary_inputs()


_ext_constant_switch_eco_primary_inputs = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_ECO_PRIMARY_INPUTS",
    {},
    _root,
    {},
    "_ext_constant_switch_eco_primary_inputs",
)


@component.add(
    name="taxes_production",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_primary_inputs": 1,
        "price_transformation": 2,
        "tax_rate_output": 2,
        "base_output_real": 1,
        "base_price_output": 1,
        "price_output": 1,
        "output_real": 1,
    },
)
def taxes_production():
    """
    Taxes on production in nominal terms.
    """
    return if_then_else(
        switch_eco_primary_inputs() == 0,
        lambda: tax_rate_output()
        * base_output_real()
        * zidz(base_price_output(), price_transformation()),
        lambda: tax_rate_output()
        * output_real()
        * zidz(price_output(), price_transformation()),
    )


@component.add(
    name="taxes_production_real",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "base_tax_rate_output": 1,
        "switch_eco_primary_inputs": 1,
        "base_output_real": 1,
        "output_real": 1,
    },
)
def taxes_production_real():
    """
    Net taxes on production in real terms.
    """
    return base_tax_rate_output() * if_then_else(
        switch_eco_primary_inputs() == 0,
        lambda: base_output_real(),
        lambda: output_real(),
    )


@component.add(
    name="taxes_products_by_sector",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_MAP_I", "SECTORS_MAP_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "taxes_products_domestic_by_sector": 1,
        "taxes_products_imports_by_sector": 1,
    },
)
def taxes_products_by_sector():
    """
    Net taxes on products by sector in nominal terms.
    """
    return taxes_products_domestic_by_sector().rename(
        {"REGIONS_35_I": "REGIONS_35_MAP_I", "SECTORS_I": "SECTORS_MAP_I"}
    ) + sum(
        taxes_products_imports_by_sector().rename(
            {"REGIONS_35_I": "REGIONS_35_I!", "SECTORS_I": "SECTORS_MAP_I"}
        ),
        dim=["REGIONS_35_I!"],
    )


@component.add(
    name="taxes_products_by_sector_real",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_MAP_I", "SECTORS_MAP_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "taxes_products_domestic_by_sector_real": 1,
        "taxes_products_imports_by_sector_real": 1,
    },
)
def taxes_products_by_sector_real():
    """
    Net taxes on products paid by sectors in real terms.
    """
    return taxes_products_domestic_by_sector_real().rename(
        {"REGIONS_35_I": "REGIONS_35_MAP_I", "SECTORS_I": "SECTORS_MAP_I"}
    ) + sum(
        taxes_products_imports_by_sector_real().rename(
            {"REGIONS_35_I": "REGIONS_35_I!", "SECTORS_I": "SECTORS_MAP_I"}
        ),
        dim=["REGIONS_35_I!"],
    )


@component.add(
    name="taxes_products_domestic_by_sector",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_primary_inputs": 1,
        "price_transformation": 2,
        "initial_intermediates_domestic_real": 1,
        "tax_rate_product_domestic_aggregated": 2,
        "base_price_output": 1,
        "intermediates_domestic_real": 1,
        "price_output": 1,
    },
)
def taxes_products_domestic_by_sector():
    """
    Net taxes on domestic products by sector in nominal terms.
    """
    return if_then_else(
        switch_eco_primary_inputs() == 0,
        lambda: sum(
            initial_intermediates_domestic_real().rename(
                {"SECTORS_I": "SECTORS_MAP_I!", "SECTORS_MAP_I": "SECTORS_I"}
            )
            * (
                base_price_output().rename({"SECTORS_I": "SECTORS_MAP_I!"})
                / price_transformation()
            ),
            dim=["SECTORS_MAP_I!"],
        )
        * tax_rate_product_domestic_aggregated(),
        lambda: sum(
            intermediates_domestic_real().rename(
                {"SECTORS_I": "SECTORS_MAP_I!", "SECTORS_MAP_I": "SECTORS_I"}
            )
            * (
                price_output().rename({"SECTORS_I": "SECTORS_MAP_I!"})
                / price_transformation()
            ),
            dim=["SECTORS_MAP_I!"],
        )
        * tax_rate_product_domestic_aggregated(),
    )


@component.add(
    name="taxes_products_domestic_by_sector_real",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_primary_inputs": 1,
        "base_tax_rate_products_domestic_aggregated": 2,
        "initial_intermediates_domestic_real": 1,
        "intermediates_domestic_real": 1,
    },
)
def taxes_products_domestic_by_sector_real():
    """
    Net taxes on domestic roducts paid by sectors in real terms.
    """
    return if_then_else(
        switch_eco_primary_inputs() == 0,
        lambda: sum(
            initial_intermediates_domestic_real().rename(
                {"SECTORS_I": "SECTORS_MAP_I!", "SECTORS_MAP_I": "SECTORS_I"}
            ),
            dim=["SECTORS_MAP_I!"],
        )
        * base_tax_rate_products_domestic_aggregated(),
        lambda: sum(
            intermediates_domestic_real().rename(
                {"SECTORS_I": "SECTORS_MAP_I!", "SECTORS_MAP_I": "SECTORS_I"}
            ),
            dim=["SECTORS_MAP_I!"],
        )
        * base_tax_rate_products_domestic_aggregated(),
    )


@component.add(
    name="taxes_products_final_demand",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_MAP_I", "FINAL_DEMAND_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_primary_inputs": 1,
        "initial_taxes_products_domestic": 1,
        "initial_taxes_products_imports": 1,
        "taxes_products_imports_final_demand": 1,
        "taxes_products_domestic_final_demand": 1,
    },
)
def taxes_products_final_demand():
    """
    Net taxes on final products in nominal terms.
    """
    return if_then_else(
        switch_eco_primary_inputs() == 0,
        lambda: sum(
            initial_taxes_products_domestic().rename(
                {"REGIONS_35_I": "REGIONS_35_MAP_I", "SECTORS_I": "SECTORS_I!"}
            ),
            dim=["SECTORS_I!"],
        )
        + sum(
            initial_taxes_products_imports().rename(
                {"REGIONS_35_I": "REGIONS_35_I!", "SECTORS_I": "SECTORS_I!"}
            ),
            dim=["REGIONS_35_I!", "SECTORS_I!"],
        ),
        lambda: sum(
            taxes_products_domestic_final_demand().rename(
                {"REGIONS_35_I": "REGIONS_35_MAP_I", "SECTORS_I": "SECTORS_I!"}
            ),
            dim=["SECTORS_I!"],
        )
        + sum(
            taxes_products_imports_final_demand().rename(
                {"REGIONS_35_I": "REGIONS_35_I!", "SECTORS_I": "SECTORS_I!"}
            ),
            dim=["REGIONS_35_I!", "SECTORS_I!"],
        ),
    )


@component.add(
    name="taxes_products_final_demand_real",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_MAP_I", "FINAL_DEMAND_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_primary_inputs": 1,
        "initial_taxes_products_domestic": 1,
        "initial_taxes_products_imports": 1,
        "taxes_products_domestic_final_demand_real": 1,
        "taxes_products_imports_final_demand_real": 1,
    },
)
def taxes_products_final_demand_real():
    return if_then_else(
        switch_eco_primary_inputs() == 0,
        lambda: sum(
            initial_taxes_products_domestic().rename(
                {"REGIONS_35_I": "REGIONS_35_MAP_I", "SECTORS_I": "SECTORS_I!"}
            ),
            dim=["SECTORS_I!"],
        )
        + sum(
            initial_taxes_products_imports().rename(
                {"REGIONS_35_I": "REGIONS_35_I!", "SECTORS_I": "SECTORS_I!"}
            ),
            dim=["REGIONS_35_I!", "SECTORS_I!"],
        ),
        lambda: sum(
            taxes_products_domestic_final_demand_real().rename(
                {"REGIONS_35_I": "REGIONS_35_MAP_I", "SECTORS_I": "SECTORS_I!"}
            ),
            dim=["SECTORS_I!"],
        )
        + sum(
            taxes_products_imports_final_demand_real().rename(
                {"REGIONS_35_I": "REGIONS_35_I!", "SECTORS_I": "SECTORS_I!"}
            ),
            dim=["REGIONS_35_I!", "SECTORS_I!"],
        ),
    )


@component.add(
    name="taxes_products_imports_by_sector",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_I", "REGIONS_35_MAP_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_primary_inputs": 1,
        "price_transformation": 2,
        "tax_rate_products_imports_aggregated": 2,
        "initial_intermediate_imports_and_exports_real": 1,
        "base_price_output": 1,
        "intermediate_imports_and_exports_real": 1,
        "price_output": 1,
    },
)
def taxes_products_imports_by_sector():
    """
    Net taxes on imported products by sector in nominal terms.
    """
    return if_then_else(
        switch_eco_primary_inputs() == 0,
        lambda: sum(
            initial_intermediate_imports_and_exports_real().rename(
                {"SECTORS_I": "SECTORS_MAP_I!", "SECTORS_MAP_I": "SECTORS_I"}
            )
            * (
                base_price_output().rename({"SECTORS_I": "SECTORS_MAP_I!"})
                / price_transformation()
            ),
            dim=["SECTORS_MAP_I!"],
        )
        * tax_rate_products_imports_aggregated(),
        lambda: sum(
            intermediate_imports_and_exports_real().rename(
                {"SECTORS_I": "SECTORS_MAP_I!", "SECTORS_MAP_I": "SECTORS_I"}
            )
            * (
                price_output().rename({"SECTORS_I": "SECTORS_MAP_I!"})
                / price_transformation()
            ),
            dim=["SECTORS_MAP_I!"],
        )
        * tax_rate_products_imports_aggregated(),
    )


@component.add(
    name="taxes_products_imports_by_sector_real",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I", "REGIONS_35_MAP_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_primary_inputs": 1,
        "base_tax_rate_products_imports_aggregated": 2,
        "initial_intermediate_imports_and_exports_real": 1,
        "intermediate_imports_and_exports_real": 1,
    },
)
def taxes_products_imports_by_sector_real():
    """
    Net taxes on imported roducts paid by sectors in real terms.
    """
    return if_then_else(
        switch_eco_primary_inputs() == 0,
        lambda: sum(
            initial_intermediate_imports_and_exports_real().rename(
                {"SECTORS_I": "SECTORS_MAP_I!", "SECTORS_MAP_I": "SECTORS_I"}
            ),
            dim=["SECTORS_MAP_I!"],
        )
        * base_tax_rate_products_imports_aggregated(),
        lambda: sum(
            intermediate_imports_and_exports_real().rename(
                {"SECTORS_I": "SECTORS_MAP_I!", "SECTORS_MAP_I": "SECTORS_I"}
            ),
            dim=["SECTORS_MAP_I!"],
        )
        * base_tax_rate_products_imports_aggregated(),
    )
