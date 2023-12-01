"""
Module economy.prices
Translated using PySD version 3.10.0
"""


@component.add(
    name="BASE_PRICE_MATERIALS_AND_PRIVATE_HOUSEHOLDS",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="Normal",
)
def base_price_materials_and_private_households():
    return 100


@component.add(
    name="CO2_cost_by_region_and_sector",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "output_real_9r": 2,
        "co2_price_sp": 2,
        "switch_economy": 2,
        "initial_ghg_emissions_per_unit_of_sector_output": 2,
        "switch_eco_prices": 2,
        "ghg_emissions_per_unit_of_sector_output": 2,
        "unit_conversion_dollars_mdollars": 2,
        "share_output_real_eu27": 1,
    },
)
def co2_cost_by_region_and_sector():
    """
    Total cost by region and sector of the policy of puting a price to CO2.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "SECTORS_I": _subscript_dict["SECTORS_I"],
        },
        ["REGIONS_35_I", "SECTORS_I"],
    )
    value.loc[_subscript_dict["REGIONS_8_I"], :] = (
        output_real_9r()
        .loc[_subscript_dict["REGIONS_8_I"], :]
        .rename({"REGIONS_9_I": "REGIONS_8_I"})
        * co2_price_sp()
        .loc[_subscript_dict["REGIONS_8_I"]]
        .rename({"REGIONS_36_I": "REGIONS_8_I"})
        * if_then_else(
            np.logical_or(switch_economy() == 0, switch_eco_prices() == 0),
            lambda: initial_ghg_emissions_per_unit_of_sector_output()
            .loc[_subscript_dict["REGIONS_8_I"], :, "CO2"]
            .reset_coords(drop=True)
            .rename({"REGIONS_9_I": "REGIONS_8_I"}),
            lambda: ghg_emissions_per_unit_of_sector_output()
            .loc[_subscript_dict["REGIONS_8_I"], :, "CO2"]
            .reset_coords(drop=True)
            .rename({"REGIONS_9_I": "REGIONS_8_I"}),
        )
        / unit_conversion_dollars_mdollars()
    ).values
    value.loc[_subscript_dict["REGIONS_EU27_I"], :] = (
        (
            output_real_9r().loc["EU27", :].reset_coords(drop=True)
            * co2_price_sp()
            .loc[_subscript_dict["REGIONS_EU27_I"]]
            .rename({"REGIONS_36_I": "REGIONS_EU27_I"})
            * share_output_real_eu27().transpose("SECTORS_I", "REGIONS_EU27_I")
            * if_then_else(
                np.logical_or(switch_economy() == 0, switch_eco_prices() == 0),
                lambda: initial_ghg_emissions_per_unit_of_sector_output()
                .loc["EU27", :, "CO2"]
                .reset_coords(drop=True),
                lambda: ghg_emissions_per_unit_of_sector_output()
                .loc["EU27", :, "CO2"]
                .reset_coords(drop=True),
            )
            / unit_conversion_dollars_mdollars()
        )
        .transpose("REGIONS_EU27_I", "SECTORS_I")
        .values
    )
    return value


@component.add(
    name="CO2_emissions_per_unit_of_sector_output_35R",
    units="t/Mdollars_2015",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ghg_emissions_per_unit_of_sector_output": 2},
)
def co2_emissions_per_unit_of_sector_output_35r():
    """
    CO2 emissions per unit of sector output by WILIAM region. Given that the energy module works for 9 regions, we assume the same CO2 emissions per unit of sector output for all EU member states.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "SECTORS_I": _subscript_dict["SECTORS_I"],
        },
        ["REGIONS_35_I", "SECTORS_I"],
    )
    value.loc[_subscript_dict["REGIONS_8_I"], :] = (
        ghg_emissions_per_unit_of_sector_output()
        .loc[_subscript_dict["REGIONS_8_I"], :, "CO2"]
        .reset_coords(drop=True)
        .rename({"REGIONS_9_I": "REGIONS_8_I"})
        .values
    )
    value.loc[_subscript_dict["REGIONS_EU27_I"], :] = (
        ghg_emissions_per_unit_of_sector_output()
        .loc["EU27", :, "CO2"]
        .reset_coords(drop=True)
        .expand_dims({"REGIONS_EU27_I": _subscript_dict["REGIONS_EU27_I"]}, 0)
        .values
    )
    return value


@component.add(
    name="CO2_PRICE_SP",
    units="$/t",
    subscripts=["REGIONS_36_I"],
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_co2_price_sp",
        "__data__": "_ext_data_co2_price_sp",
        "time": 1,
    },
)
def co2_price_sp():
    """
    Policy target CO2 price by region over time.
    """
    return _ext_data_co2_price_sp(time())


_ext_data_co2_price_sp = ExtData(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "time_index_2100",
    "CO2_PRICE_SP",
    "interpolate",
    {"REGIONS_36_I": _subscript_dict["REGIONS_36_I"]},
    _root,
    {"REGIONS_36_I": _subscript_dict["REGIONS_36_I"]},
    "_ext_data_co2_price_sp",
)


@component.add(
    name="DELAYED_non_metals_price_economy_adjusted",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="Normal",
)
def delayed_non_metals_price_economy_adjusted():
    """
    Delayed non metals price economy adjusted.
    """
    return 100


@component.add(
    name="DELAYED_other_gas_price_economy_adjusted",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="Normal",
)
def delayed_other_gas_price_economy_adjusted():
    """
    Delayed other gas price economy adjusted.
    """
    return 100


@component.add(
    name="DELAYED_other_metals_price_economy_adjusted",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="Normal",
)
def delayed_other_metals_price_economy_adjusted():
    """
    Delayed other metals price economy adjusted.
    """
    return 100


@component.add(
    name="DELAYED_Pb_Zn_Tn_price_economy_adjusted",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="Normal",
)
def delayed_pb_zn_tn_price_economy_adjusted():
    """
    Delayed lead, zinc and tin price economy adjusted.
    """
    return 100


@component.add(
    name="DELAYED_precious_metals_price_economy_adjusted",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="Normal",
)
def delayed_precious_metals_price_economy_adjusted():
    """
    Delayed precious metals price economy adjusted.
    """
    return 100


@component.add(
    name="delayed_TS_price_GFCF",
    units="DMNL",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_price_gfcf": 1},
    other_deps={
        "_delayfixed_delayed_ts_price_gfcf": {
            "initial": {"initial_price_gfcf": 1, "time_step": 1},
            "step": {"time": 1, "initial_price_gfcf": 1, "price_gfcf": 1},
        }
    },
)
def delayed_ts_price_gfcf():
    """
    Delayed price of investment goods.
    """
    return _delayfixed_delayed_ts_price_gfcf()


_delayfixed_delayed_ts_price_gfcf = DelayFixed(
    lambda: if_then_else(
        time() <= 2015,
        lambda: initial_price_gfcf(),
        lambda: price_gfcf().rename({"SECTORS_MAP_I": "SECTORS_I"}),
    ),
    lambda: time_step(),
    lambda: initial_price_gfcf(),
    time_step,
    "_delayfixed_delayed_ts_price_gfcf",
)


@component.add(
    name="delayed_TS_price_materials_and_private_households",
    units="DMNL",
    subscripts=["REGIONS_35_I", "SECTORS_EXTRACTION_PH_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_economy": 13,
        "base_price_materials_and_private_households": 14,
        "delayed_ts_coal_price_economy_adjusted": 1,
        "delayed_ts_oil_price_economy_adjusted": 1,
        "delayed_ts_gas_price_economy_adjusted": 1,
        "delayed_other_gas_price_economy_adjusted": 1,
        "delayed_uranium_price_economy_adjusted": 1,
        "delayed_ts_fe_price_economy_adjusted": 1,
        "delayed_ts_cu_price_economy_adjusted": 1,
        "delayed_ts_ni_price_economy_adjusted": 1,
        "delayed_ts_al_price_economy_adjusted": 1,
        "delayed_precious_metals_price_economy_adjusted": 1,
        "delayed_pb_zn_tn_price_economy_adjusted": 1,
        "delayed_other_metals_price_economy_adjusted": 1,
        "delayed_non_metals_price_economy_adjusted": 1,
    },
)
def delayed_ts_price_materials_and_private_households():
    """
    Delayed price of all materials calculated in materials model and fixed price of private households with employed persons (Sector 95 in NACE classification).
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "SECTORS_EXTRACTION_PH_I": _subscript_dict["SECTORS_EXTRACTION_PH_I"],
        },
        ["REGIONS_35_I", "SECTORS_EXTRACTION_PH_I"],
    )
    value.loc[:, ["MINING_COAL"]] = if_then_else(
        switch_economy() == 0,
        lambda: base_price_materials_and_private_households(),
        lambda: delayed_ts_coal_price_economy_adjusted(),
    )
    value.loc[:, ["EXTRACTION_OIL"]] = if_then_else(
        switch_economy() == 0,
        lambda: base_price_materials_and_private_households(),
        lambda: delayed_ts_oil_price_economy_adjusted(),
    )
    value.loc[:, ["EXTRACTION_GAS"]] = if_then_else(
        switch_economy() == 0,
        lambda: base_price_materials_and_private_households(),
        lambda: delayed_ts_gas_price_economy_adjusted(),
    )
    value.loc[:, ["EXTRACTION_OTHER_GAS"]] = if_then_else(
        switch_economy() == 0,
        lambda: base_price_materials_and_private_households(),
        lambda: delayed_other_gas_price_economy_adjusted(),
    )
    value.loc[:, ["MINING_AND_MANUFACTURING_URANIUM_THORIUM"]] = if_then_else(
        switch_economy() == 0,
        lambda: base_price_materials_and_private_households(),
        lambda: delayed_uranium_price_economy_adjusted(),
    )
    value.loc[:, ["MINING_AND_MANUFACTURING_IRON"]] = if_then_else(
        switch_economy() == 0,
        lambda: base_price_materials_and_private_households(),
        lambda: delayed_ts_fe_price_economy_adjusted(),
    )
    value.loc[:, ["MINING_AND_MANUFACTURING_COPPER"]] = if_then_else(
        switch_economy() == 0,
        lambda: base_price_materials_and_private_households(),
        lambda: delayed_ts_cu_price_economy_adjusted(),
    )
    value.loc[:, ["MINING_AND_MANUFACTURING_NICKEL"]] = if_then_else(
        switch_economy() == 0,
        lambda: base_price_materials_and_private_households(),
        lambda: delayed_ts_ni_price_economy_adjusted(),
    )
    value.loc[:, ["MINING_AND_MANUFACTURING_ALUMINIUM"]] = if_then_else(
        switch_economy() == 0,
        lambda: base_price_materials_and_private_households(),
        lambda: delayed_ts_al_price_economy_adjusted(),
    )
    value.loc[:, ["MINING_AND_MANUFACTURING_PRECIOUS_METALS"]] = if_then_else(
        switch_economy() == 0,
        lambda: base_price_materials_and_private_households(),
        lambda: delayed_precious_metals_price_economy_adjusted(),
    )
    value.loc[:, ["MINING_AND_MANUFACTURING_LEAD_ZINC_TIN"]] = if_then_else(
        switch_economy() == 0,
        lambda: base_price_materials_and_private_households(),
        lambda: delayed_pb_zn_tn_price_economy_adjusted(),
    )
    value.loc[:, ["MINING_AND_MANUFACTURING_OTHER_METALS"]] = if_then_else(
        switch_economy() == 0,
        lambda: base_price_materials_and_private_households(),
        lambda: delayed_other_metals_price_economy_adjusted(),
    )
    value.loc[:, ["MINING_NON_METALS"]] = if_then_else(
        switch_economy() == 0,
        lambda: base_price_materials_and_private_households(),
        lambda: delayed_non_metals_price_economy_adjusted(),
    )
    value.loc[:, ["PRIVATE_HOUSEHOLDS"]] = base_price_materials_and_private_households()
    return value


@component.add(
    name="delayed_TS_price_output",
    units="DMNL",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_price_output": 1},
    other_deps={
        "_delayfixed_delayed_ts_price_output": {
            "initial": {"initial_price_of_output": 1, "time_step": 1},
            "step": {"time": 1, "initial_price_of_output": 1, "price_output": 1},
        }
    },
)
def delayed_ts_price_output():
    """
    Delayed output price.
    """
    return _delayfixed_delayed_ts_price_output()


_delayfixed_delayed_ts_price_output = DelayFixed(
    lambda: if_then_else(
        time() <= 2015, lambda: initial_price_of_output(), lambda: price_output()
    ),
    lambda: time_step(),
    lambda: initial_price_of_output(),
    time_step,
    "_delayfixed_delayed_ts_price_output",
)


@component.add(
    name="delayed_TS_price_ratio_households",
    units="DMNL",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_price_ratio_households": 1},
    other_deps={
        "_delayfixed_delayed_ts_price_ratio_households": {
            "initial": {"initial_delayed_price_ratio_households": 1, "time_step": 1},
            "step": {
                "time": 1,
                "initial_delayed_price_ratio_households": 1,
                "price_ratio_households": 1,
            },
        }
    },
)
def delayed_ts_price_ratio_households():
    """
    Delayed price ratio between domestic and foreign products for households.
    """
    return _delayfixed_delayed_ts_price_ratio_households()


_delayfixed_delayed_ts_price_ratio_households = DelayFixed(
    lambda: if_then_else(
        time() <= 2015,
        lambda: initial_delayed_price_ratio_households(),
        lambda: np.maximum(0, price_ratio_households()),
    ),
    lambda: time_step(),
    lambda: initial_delayed_price_ratio_households(),
    time_step,
    "_delayfixed_delayed_ts_price_ratio_households",
)


@component.add(
    name="delayed_TS_price_ratio_sectors",
    units="DMNL",
    subscripts=["REGIONS_35_I", "SECTORS_I", "SECTORS_MAP_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_price_ratio_sectors": 1},
    other_deps={
        "_delayfixed_delayed_ts_price_ratio_sectors": {
            "initial": {"initial_delayed_price_ratio_intermediates": 1, "time_step": 1},
            "step": {
                "time": 1,
                "initial_delayed_price_ratio_intermediates": 1,
                "price_ratio_sectors": 1,
            },
        }
    },
)
def delayed_ts_price_ratio_sectors():
    """
    Delayed price ratio between domestic and foreign products for intermdiates.
    """
    return _delayfixed_delayed_ts_price_ratio_sectors()


_delayfixed_delayed_ts_price_ratio_sectors = DelayFixed(
    lambda: if_then_else(
        time() <= 2015,
        lambda: initial_delayed_price_ratio_intermediates(),
        lambda: price_ratio_sectors(),
    ),
    lambda: time_step(),
    lambda: initial_delayed_price_ratio_intermediates(),
    time_step,
    "_delayfixed_delayed_ts_price_ratio_sectors",
)


@component.add(
    name="DELAYED_uranium_price_economy_adjusted",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="Normal",
)
def delayed_uranium_price_economy_adjusted():
    """
    Delayed price of uranium.
    """
    return 100


@component.add(
    name="initial_delayed_estimated_oil_price",
    comp_type="Constant",
    comp_subtype="Normal",
)
def initial_delayed_estimated_oil_price():
    """
    Initial delayed estimated oil price.
    """
    return 81.1898


@component.add(
    name="INITIAL_GHG_emissions_per_unit_of_sector_output",
    units="t/Mdollars_2015",
    subscripts=["REGIONS_9_I", "SECTORS_I", "GHG_I"],
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_initial_ghg_emissions_per_unit_of_sector_output": 1},
    other_deps={
        "_initial_initial_ghg_emissions_per_unit_of_sector_output": {
            "initial": {"ghg_emissions_per_unit_of_sector_output": 1},
            "step": {},
        }
    },
)
def initial_ghg_emissions_per_unit_of_sector_output():
    return _initial_initial_ghg_emissions_per_unit_of_sector_output()


_initial_initial_ghg_emissions_per_unit_of_sector_output = Initial(
    lambda: ghg_emissions_per_unit_of_sector_output(),
    "_initial_initial_ghg_emissions_per_unit_of_sector_output",
)


@component.add(
    name="initial_price_with_mark_up",
    units="DMNL",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_initial_price_with_mark_up": 1},
    other_deps={
        "_initial_initial_price_with_mark_up": {
            "initial": {"price_domestic": 1, "price_import": 1},
            "step": {},
        }
    },
)
def initial_price_with_mark_up():
    """
    Initial price with mark-up.
    """
    return _initial_initial_price_with_mark_up()


_initial_initial_price_with_mark_up = Initial(
    lambda: price_domestic() + price_import(), "_initial_initial_price_with_mark_up"
)


@component.add(
    name="initial_primary_inputs_coefficients",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_initial_primary_inputs_coefficients": 1},
    other_deps={
        "_initial_initial_primary_inputs_coefficients": {
            "initial": {"primary_inputs_coefficients": 1},
            "step": {},
        }
    },
)
def initial_primary_inputs_coefficients():
    return _initial_initial_primary_inputs_coefficients()


_initial_initial_primary_inputs_coefficients = Initial(
    lambda: primary_inputs_coefficients(),
    "_initial_initial_primary_inputs_coefficients",
)


@component.add(
    name="intermediate_imports_multipliers",
    units="DMNL",
    subscripts=["REGIONS_35_MAP_I", "SECTORS_MAP_I", "REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"technical_coefficients_import": 1, "leontief_inverse": 1},
)
def intermediate_imports_multipliers():
    """
    Intermdiate imports multiplier. Imports required (directly and indirectly) to satisfy on unit of final demand.
    """
    return sum(
        technical_coefficients_import().rename(
            {"SECTORS_I": "SECTORS_MAP_I", "SECTORS_MAP_I": "SECTORS_MAP_MAP_I!"}
        )
        * leontief_inverse().rename(
            {"SECTORS_I": "SECTORS_MAP_MAP_I!", "SECTORS_MAP_I": "SECTORS_I"}
        ),
        dim=["SECTORS_MAP_MAP_I!"],
    )


@component.add(
    name="PERCENT_PRICE_TRANSFORMATION",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="Normal",
)
def percent_price_transformation():
    """
    This variable is used just for normalizing prices that are basis 100.
    """
    return 100


@component.add(
    name="price_COICOP",
    units="DMNL",
    subscripts=["REGIONS_35_I", "COICOP_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_households": 1,
        "price_transformation": 4,
        "trade_and_transportation_margins_paid_for_imported_products_for_final_demand": 2,
        "base_import_shares_origin_final_demand": 2,
        "trade_and_transportation_margins_paid_for_domestic_products_for_final_demand": 2,
        "tax_rate_products_imports_for_final_demand": 2,
        "base_price_output": 2,
        "tax_rate_products_domestic_for_final_demand": 2,
        "base_import_shares_final_demand": 2,
        "consumption_structure_coicop": 4,
        "base_price_coicop": 4,
        "import_shares_final_demand_constrained": 2,
        "price_output": 2,
    },
)
def price_coicop():
    """
    Price by consumption category (COICOP classification) CHECK THIS FORMULA
    """
    return if_then_else(
        switch_eco_households() == 0,
        lambda: (
            sum(
                consumption_structure_coicop().rename({"SECTORS_I": "SECTORS_I!"})
                * (
                    base_price_output().rename({"SECTORS_I": "SECTORS_I!"})
                    * (
                        1
                        - base_import_shares_final_demand()
                        .loc[:, :, "CONSUMPTION_W"]
                        .reset_coords(drop=True)
                        .rename({"SECTORS_I": "SECTORS_I!"})
                    )
                    * (
                        1
                        + trade_and_transportation_margins_paid_for_domestic_products_for_final_demand()
                        .loc[:, :, "CONSUMPTION_W"]
                        .reset_coords(drop=True)
                        .rename({"SECTORS_I": "SECTORS_I!"})
                    )
                    * (
                        1
                        + tax_rate_products_domestic_for_final_demand()
                        .loc[:, :, "CONSUMPTION_W"]
                        .reset_coords(drop=True)
                        .rename({"SECTORS_I": "SECTORS_I!"})
                    )
                ),
                dim=["SECTORS_I!"],
            )
            / base_price_coicop()
        )
        * price_transformation()
        + (
            sum(
                consumption_structure_coicop().rename({"SECTORS_I": "SECTORS_I!"})
                * (
                    base_price_output().rename(
                        {"REGIONS_35_I": "REGIONS_35_MAP_I!", "SECTORS_I": "SECTORS_I!"}
                    )
                    * base_import_shares_final_demand()
                    .loc[:, :, "CONSUMPTION_W"]
                    .reset_coords(drop=True)
                    .rename({"SECTORS_I": "SECTORS_I!"})
                    .transpose("SECTORS_I!", "REGIONS_35_I")
                    * base_import_shares_origin_final_demand()
                    .loc[:, :, :, "CONSUMPTION_W"]
                    .reset_coords(drop=True)
                    .rename(
                        {
                            "REGIONS_35_MAP_I": "REGIONS_35_MAP_I!",
                            "SECTORS_I": "SECTORS_I!",
                        }
                    )
                    * (
                        1
                        + trade_and_transportation_margins_paid_for_imported_products_for_final_demand()
                        .loc[:, :, :, "CONSUMPTION_W"]
                        .reset_coords(drop=True)
                        .rename(
                            {
                                "REGIONS_35_MAP_I": "REGIONS_35_MAP_I!",
                                "SECTORS_I": "SECTORS_I!",
                            }
                        )
                    )
                    * (
                        1
                        + tax_rate_products_imports_for_final_demand()
                        .loc[:, :, :, "CONSUMPTION_W"]
                        .reset_coords(drop=True)
                        .rename(
                            {
                                "REGIONS_35_I": "REGIONS_35_MAP_I!",
                                "SECTORS_I": "SECTORS_I!",
                                "REGIONS_35_MAP_I": "REGIONS_35_I",
                            }
                        )
                    )
                ).transpose("REGIONS_35_I", "SECTORS_I!", "REGIONS_35_MAP_I!"),
                dim=["SECTORS_I!", "REGIONS_35_MAP_I!"],
            )
            / base_price_coicop()
        )
        * price_transformation(),
        lambda: (
            sum(
                consumption_structure_coicop().rename({"SECTORS_I": "SECTORS_I!"})
                * (
                    price_output().rename({"SECTORS_I": "SECTORS_I!"})
                    * (
                        1
                        - import_shares_final_demand_constrained()
                        .loc[:, :, "CONSUMPTION_W"]
                        .reset_coords(drop=True)
                        .rename({"SECTORS_I": "SECTORS_I!"})
                    )
                    * (
                        1
                        + trade_and_transportation_margins_paid_for_domestic_products_for_final_demand()
                        .loc[:, :, "CONSUMPTION_W"]
                        .reset_coords(drop=True)
                        .rename({"SECTORS_I": "SECTORS_I!"})
                    )
                    * (
                        1
                        + tax_rate_products_domestic_for_final_demand()
                        .loc[:, :, "CONSUMPTION_W"]
                        .reset_coords(drop=True)
                        .rename({"SECTORS_I": "SECTORS_I!"})
                    )
                ),
                dim=["SECTORS_I!"],
            )
            / base_price_coicop()
        )
        * price_transformation()
        + (
            sum(
                consumption_structure_coicop().rename({"SECTORS_I": "SECTORS_I!"})
                * (
                    price_output().rename(
                        {"REGIONS_35_I": "REGIONS_35_MAP_I!", "SECTORS_I": "SECTORS_I!"}
                    )
                    * import_shares_final_demand_constrained()
                    .loc[:, :, "CONSUMPTION_W"]
                    .reset_coords(drop=True)
                    .rename({"SECTORS_I": "SECTORS_I!"})
                    .transpose("SECTORS_I!", "REGIONS_35_I")
                    * base_import_shares_origin_final_demand()
                    .loc[:, :, :, "CONSUMPTION_W"]
                    .reset_coords(drop=True)
                    .rename(
                        {
                            "REGIONS_35_MAP_I": "REGIONS_35_MAP_I!",
                            "SECTORS_I": "SECTORS_I!",
                        }
                    )
                    * (
                        1
                        + trade_and_transportation_margins_paid_for_imported_products_for_final_demand()
                        .loc[:, :, :, "CONSUMPTION_W"]
                        .reset_coords(drop=True)
                        .rename(
                            {
                                "REGIONS_35_MAP_I": "REGIONS_35_MAP_I!",
                                "SECTORS_I": "SECTORS_I!",
                            }
                        )
                    )
                    * (
                        1
                        + tax_rate_products_imports_for_final_demand()
                        .loc[:, :, :, "CONSUMPTION_W"]
                        .reset_coords(drop=True)
                        .rename(
                            {
                                "REGIONS_35_I": "REGIONS_35_MAP_I!",
                                "SECTORS_I": "SECTORS_I!",
                                "REGIONS_35_MAP_I": "REGIONS_35_I",
                            }
                        )
                    )
                ).transpose("REGIONS_35_I", "SECTORS_I!", "REGIONS_35_MAP_I!"),
                dim=["SECTORS_I!", "REGIONS_35_MAP_I!"],
            )
            / base_price_coicop()
        )
        * price_transformation(),
    )


@component.add(
    name="price_domestic",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "primary_inputs_coefficients_with_changes_in_material_prices": 1,
        "leontief_inverse": 1,
    },
)
def price_domestic():
    """
    Domestic price witouht mark-up.
    """
    return sum(
        primary_inputs_coefficients_with_changes_in_material_prices().rename(
            {"SECTORS_I": "SECTORS_MAP_I!"}
        )
        * leontief_inverse().rename(
            {"SECTORS_I": "SECTORS_MAP_I!", "SECTORS_MAP_I": "SECTORS_I"}
        ),
        dim=["SECTORS_MAP_I!"],
    )


@component.add(
    name="price_domestic_purchaser_prices_households",
    units="DMNL",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "price_output": 1,
        "price_transformation": 1,
        "trade_and_transportation_margins_paid_for_domestic_products_for_final_demand": 1,
        "tax_rate_products_domestic_for_final_demand": 1,
    },
)
def price_domestic_purchaser_prices_households():
    """
    Domestic prices in purchasers prices.
    """
    return (
        price_output()
        / price_transformation()
        * (
            1
            + trade_and_transportation_margins_paid_for_domestic_products_for_final_demand()
            .loc[:, :, "CONSUMPTION_W"]
            .reset_coords(drop=True)
        )
        * (
            1
            + tax_rate_products_domestic_for_final_demand()
            .loc[:, :, "CONSUMPTION_W"]
            .reset_coords(drop=True)
        )
    )


@component.add(
    name="price_domestic_purchaser_prices_sectors",
    units="DMNL",
    subscripts=["REGIONS_35_I", "SECTORS_I", "SECTORS_MAP_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "price_output": 1,
        "price_transformation": 1,
        "trade_and_transportation_margins_paid_for_domestic_products_by_sectors": 1,
        "tax_rate_products_domestic_by_sectors": 1,
    },
)
def price_domestic_purchaser_prices_sectors():
    """
    Domestic prices in purchasers prices. CHECK: ESTOS REQUIEREN OTRA VEZ LAS MATRICES GRANDES TRADE...
    """
    return (
        zidz(price_output(), price_transformation())
        * (1 + trade_and_transportation_margins_paid_for_domestic_products_by_sectors())
        * (1 + tax_rate_products_domestic_by_sectors())
    )


@component.add(
    name="price_GFCF",
    units="DMNL",
    subscripts=["REGIONS_35_I", "SECTORS_MAP_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "gross_fixed_capital_formation_structure": 2,
        "price_transformation": 6,
        "trade_and_transportation_margins_paid_for_domestic_products_for_final_demand": 1,
        "import_shares_final_demand_constrained": 2,
        "tax_rate_products_domestic_for_final_demand": 1,
        "price_output": 2,
        "base2015_price_gfcf": 2,
        "tax_rate_products_imports_for_final_demand": 1,
        "trade_and_transportation_margins_paid_for_imported_products_for_final_demand": 1,
        "import_shares_origin_final_demand": 1,
    },
)
def price_gfcf():
    """
    Price of investment goods No está metido el SWITCH***
    """
    return (
        sum(
            gross_fixed_capital_formation_structure().rename(
                {"SECTORS_I": "SECTORS_I!"}
            )
            * (
                (
                    price_output().rename({"SECTORS_I": "SECTORS_I!"})
                    / price_transformation()
                )
                * (
                    1
                    - import_shares_final_demand_constrained()
                    .loc[:, :, "GROSS_FIXED_CAPITAL_FORMATION_W"]
                    .reset_coords(drop=True)
                    .rename({"SECTORS_I": "SECTORS_I!"})
                )
                * (
                    1
                    + trade_and_transportation_margins_paid_for_domestic_products_for_final_demand()
                    .loc[:, :, "GROSS_FIXED_CAPITAL_FORMATION_W"]
                    .reset_coords(drop=True)
                    .rename({"SECTORS_I": "SECTORS_I!"})
                )
                * (
                    1
                    + tax_rate_products_domestic_for_final_demand()
                    .loc[:, :, "GROSS_FIXED_CAPITAL_FORMATION_W"]
                    .reset_coords(drop=True)
                    .rename({"SECTORS_I": "SECTORS_I!"})
                )
            ),
            dim=["SECTORS_I!"],
        )
        * zidz(
            xr.DataArray(
                price_transformation(),
                {
                    "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                    "SECTORS_MAP_I": _subscript_dict["SECTORS_MAP_I"],
                },
                ["REGIONS_35_I", "SECTORS_MAP_I"],
            ),
            base2015_price_gfcf().rename({"SECTORS_I": "SECTORS_MAP_I"}),
        )
        * price_transformation()
        + sum(
            gross_fixed_capital_formation_structure().rename(
                {"SECTORS_I": "SECTORS_I!"}
            )
            * (
                (
                    price_output().rename(
                        {"REGIONS_35_I": "REGIONS_35_MAP_I!", "SECTORS_I": "SECTORS_I!"}
                    )
                    / price_transformation()
                )
                * import_shares_final_demand_constrained()
                .loc[:, :, "GROSS_FIXED_CAPITAL_FORMATION_W"]
                .reset_coords(drop=True)
                .rename({"SECTORS_I": "SECTORS_I!"})
                .transpose("SECTORS_I!", "REGIONS_35_I")
                * import_shares_origin_final_demand()
                .loc[:, :, :, "GROSS_FIXED_CAPITAL_FORMATION_W"]
                .reset_coords(drop=True)
                .rename(
                    {"REGIONS_35_MAP_I": "REGIONS_35_MAP_I!", "SECTORS_I": "SECTORS_I!"}
                )
                * (
                    1
                    + trade_and_transportation_margins_paid_for_imported_products_for_final_demand()
                    .loc[:, :, :, "GROSS_FIXED_CAPITAL_FORMATION_W"]
                    .reset_coords(drop=True)
                    .rename(
                        {
                            "REGIONS_35_MAP_I": "REGIONS_35_MAP_I!",
                            "SECTORS_I": "SECTORS_I!",
                        }
                    )
                )
                * (
                    1
                    + tax_rate_products_imports_for_final_demand()
                    .loc[:, :, :, "GROSS_FIXED_CAPITAL_FORMATION_W"]
                    .reset_coords(drop=True)
                    .rename(
                        {
                            "REGIONS_35_I": "REGIONS_35_MAP_I!",
                            "SECTORS_I": "SECTORS_I!",
                            "REGIONS_35_MAP_I": "REGIONS_35_I",
                        }
                    )
                )
            ).transpose("REGIONS_35_I", "SECTORS_I!", "REGIONS_35_MAP_I!"),
            dim=["SECTORS_I!", "REGIONS_35_MAP_I!"],
        )
        * zidz(
            xr.DataArray(
                price_transformation(),
                {
                    "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                    "SECTORS_MAP_I": _subscript_dict["SECTORS_MAP_I"],
                },
                ["REGIONS_35_I", "SECTORS_MAP_I"],
            ),
            base2015_price_gfcf().rename({"SECTORS_I": "SECTORS_MAP_I"}),
        )
        * price_transformation()
    )


@component.add(
    name="price_import",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "primary_inputs_coefficients_with_changes_in_material_prices": 1,
        "intermediate_imports_multipliers": 1,
    },
)
def price_import():
    return sum(
        primary_inputs_coefficients_with_changes_in_material_prices().rename(
            {"REGIONS_35_I": "REGIONS_35_MAP_I!", "SECTORS_I": "SECTORS_MAP_I!"}
        )
        * intermediate_imports_multipliers().rename(
            {"REGIONS_35_MAP_I": "REGIONS_35_MAP_I!", "SECTORS_MAP_I": "SECTORS_MAP_I!"}
        ),
        dim=["REGIONS_35_MAP_I!", "SECTORS_MAP_I!"],
    )


@component.add(
    name="price_import_purchaser_prices_households",
    units="DMNL",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "price_output": 1,
        "price_transformation": 1,
        "import_shares_origin_final_demand": 1,
        "trade_and_transportation_margins_paid_for_imported_products_for_final_demand": 1,
        "tax_rate_products_imports_for_final_demand": 1,
    },
)
def price_import_purchaser_prices_households():
    """
    Import prices in purchasers prices.
    """
    return sum(
        price_output().rename({"REGIONS_35_I": "REGIONS_35_MAP_I!"})
        / price_transformation()
        * import_shares_origin_final_demand()
        .loc[:, :, :, "CONSUMPTION_W"]
        .reset_coords(drop=True)
        .rename({"REGIONS_35_MAP_I": "REGIONS_35_MAP_I!"})
        * (
            1
            + trade_and_transportation_margins_paid_for_imported_products_for_final_demand()
            .loc[:, :, :, "CONSUMPTION_W"]
            .reset_coords(drop=True)
            .rename({"REGIONS_35_MAP_I": "REGIONS_35_MAP_I!"})
        )
        * (
            1
            + tax_rate_products_imports_for_final_demand()
            .loc[:, :, :, "CONSUMPTION_W"]
            .reset_coords(drop=True)
            .rename(
                {
                    "REGIONS_35_I": "REGIONS_35_MAP_I!",
                    "REGIONS_35_MAP_I": "REGIONS_35_I",
                }
            )
        ),
        dim=["REGIONS_35_MAP_I!"],
    ).transpose("REGIONS_35_I", "SECTORS_I")


@component.add(
    name="price_import_purchaser_prices_sectors",
    units="DMNL",
    subscripts=["REGIONS_35_I", "SECTORS_I", "SECTORS_MAP_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "price_output": 1,
        "price_transformation": 1,
        "import_shares_origin_intermediates": 1,
        "trade_and_transportation_margins_paid_for_imported_products_by_sectors": 1,
        "tax_rate_products_imports_by_sectors": 1,
    },
)
def price_import_purchaser_prices_sectors():
    """
    Import prices in purchasers prices. CHECK: ESTOS REQUIEREN OTRA VEZ LAS MATRICES GRANDES TRADE...
    """
    return sum(
        price_output().rename({"REGIONS_35_I": "REGIONS_35_MAP_I!"})
        / price_transformation()
        * import_shares_origin_intermediates().rename(
            {"REGIONS_35_MAP_I": "REGIONS_35_MAP_I!"}
        )
        * (
            1
            + trade_and_transportation_margins_paid_for_imported_products_by_sectors().rename(
                {
                    "REGIONS_35_I": "REGIONS_35_MAP_I!",
                    "REGIONS_35_MAP_I": "REGIONS_35_I",
                }
            )
        )
        * (
            1
            + tax_rate_products_imports_by_sectors().rename(
                {
                    "REGIONS_35_I": "REGIONS_35_MAP_I!",
                    "REGIONS_35_MAP_I": "REGIONS_35_I",
                }
            )
        ),
        dim=["REGIONS_35_MAP_I!"],
    ).transpose("REGIONS_35_I", "SECTORS_I", "SECTORS_MAP_I")


@component.add(
    name="price_output",
    units="DMNL",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "initial_price_with_mark_up": 1,
        "price_transformation": 1,
        "price_domestic": 1,
        "price_import": 1,
        "delayed_ts_price_materials_and_private_households": 1,
        "base_price_materials_and_private_households": 1,
    },
)
def price_output():
    """
    Output price by sector CHECK: Falta hacer endógeno Trade y Climate Change Damage????? IMPORT ORIGIN SHARES INTERMEDIATES
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "SECTORS_I": _subscript_dict["SECTORS_I"],
        },
        ["REGIONS_35_I", "SECTORS_I"],
    )
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[:, _subscript_dict["SECTORS_NON_EXTRACTION_NON_PH_I"]] = True
    except_subs.loc[:, _subscript_dict["SECTORS_EXTRACTION_PH_I"]] = False
    except_subs.loc[:, ["PRIVATE_HOUSEHOLDS"]] = False
    value.values[except_subs.values] = if_then_else(
        time() == 2005,
        lambda: xr.DataArray(
            100,
            {
                "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                "SECTORS_NON_EXTRACTION_NON_PH_I": _subscript_dict[
                    "SECTORS_NON_EXTRACTION_NON_PH_I"
                ],
            },
            ["REGIONS_35_I", "SECTORS_NON_EXTRACTION_NON_PH_I"],
        ),
        lambda: zidz(
            price_domestic()
            .loc[:, _subscript_dict["SECTORS_NON_EXTRACTION_NON_PH_I"]]
            .rename({"SECTORS_I": "SECTORS_NON_EXTRACTION_NON_PH_I"})
            + price_import()
            .loc[:, _subscript_dict["SECTORS_NON_EXTRACTION_NON_PH_I"]]
            .rename({"SECTORS_I": "SECTORS_NON_EXTRACTION_NON_PH_I"}),
            initial_price_with_mark_up()
            .loc[:, _subscript_dict["SECTORS_NON_EXTRACTION_NON_PH_I"]]
            .rename({"SECTORS_I": "SECTORS_NON_EXTRACTION_NON_PH_I"}),
        )
        * price_transformation(),
    ).values[
        except_subs.loc[:, _subscript_dict["SECTORS_NON_EXTRACTION_NON_PH_I"]].values
    ]
    value.loc[:, _subscript_dict["SECTORS_EXTRACTION_I"]] = (
        delayed_ts_price_materials_and_private_households()
        .loc[:, _subscript_dict["SECTORS_EXTRACTION_I"]]
        .rename({"SECTORS_EXTRACTION_PH_I": "SECTORS_EXTRACTION_I"})
        .values
    )
    value.loc[:, ["PRIVATE_HOUSEHOLDS"]] = base_price_materials_and_private_households()
    return value


@component.add(
    name="price_ratio_households",
    units="DMNL",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "price_domestic_purchaser_prices_households": 1,
        "base2015_price_ratio_households": 1,
        "price_import_purchaser_prices_households": 1,
    },
)
def price_ratio_households():
    """
    Price ratio between domestic and foreign products for households.
    """
    return zidz(
        price_domestic_purchaser_prices_households(),
        price_import_purchaser_prices_households() * base2015_price_ratio_households(),
    )


@component.add(
    name="price_ratio_sectors",
    units="DMNL",
    subscripts=["REGIONS_35_I", "SECTORS_I", "SECTORS_MAP_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "price_domestic_purchaser_prices_sectors": 1,
        "price_import_purchaser_prices_sectors": 1,
        "base2015_price_ratio_sectors": 1,
    },
)
def price_ratio_sectors():
    """
    Price ratio between domestic and foreign products for intermdiates.
    """
    return zidz(
        price_domestic_purchaser_prices_sectors(),
        price_import_purchaser_prices_sectors() * base2015_price_ratio_sectors(),
    )


@component.add(
    name="primary_inputs_coefficients",
    units="DMNL",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_prices": 1,
        "delayed_ts_price_gfcf": 2,
        "price_transformation": 12,
        "tax_rate_products_imports_aggregated": 2,
        "mark_up": 4,
        "delayed_ts_price_output": 8,
        "base_wage_hour": 3,
        "base_capital_productivity": 1,
        "tax_rate_output": 2,
        "depreciation_rate": 2,
        "technical_coefficients_import": 2,
        "tax_rate_product_domestic_aggregated": 2,
        "base_labour_productivity": 1,
        "technical_coefficients_domestic": 2,
        "climate_change_incremental_damage_rate_to_capital_stock": 1,
        "capital_productivity": 1,
        "wage_hour": 1,
        "select_climate_change_impacts_sensitivity_sp": 1,
        "switch_climate_change_damage": 1,
        "labour_productivity": 1,
        "climate_change_incremental_damage_rate_to_capital_stock_extrapolations_included": 1,
        "switch_eco_climate_change_damage_capital": 1,
    },
)
def primary_inputs_coefficients():
    """
    Primary input coeffcients IF_THEN_ELSE(SWITCH_PRICES=0,( delayed_price_GFCF[REGIONS_35_I,SECTORS_I]/PRICE_TRANSFORMATION*(DEPRECIATION_RATE[RE GIONS_35_I,SECTORS_I] +NO_CLIMATE_CHANGE_DAMAGE_RATE_TO_CAPITAL_STOCK[REGIONS_35_I,SECTORS_I])*(ZIDZ(1,BASE _CAPITAL_PRODUCTIVITY[REGIONS_35_I ,SECTORS_I])) +(ZIDZ(BASE_WAGE_HOUR[REGIONS_35_I,SECTORS_I],(BASE_WAGE_HOUR[REGIONS_35_I,SECTORS_I] *BASE_LABOUR_PRODUCTIVITY[REGIONS_35_I , SECTORS_I])) +SUM(delayed_price_output[REGIONS_35_I,SECTORS_MAP_I!]/PRICE_TRANSFORMATION*technical _coefficients_domestic [REGIONS_35_I,SECTORS_MAP_I!,SECTORS_I])*TAX_RATE_PRODUCT_DOMESTIC_AGGREGATED[REGIONS _35_I,SECTORS_I] +SUM(delayed_price_output[REGIONS_35_MAP_I!,SECTORS_MAP_I!]/PRICE_TRANSFORMATION*tech nical_coefficients_import [REGIONS_35_MAP_I!,SECTORS_MAP_I!,REGIONS_35_I,SECTORS_I]*TAX_RATE_PRODUCTS_IMPORTS_A GGREGATED[REGIONS_35_MAP_I!,REGIONS_35_I ,SECTORS_I]) +delayed_price_output[REGIONS_35_I,SECTORS_I]/PRICE_TRANSFORMATION*TAX_RATE_OUTPUT[RE GIONS_35_I,SECTORS_I] + IF_THEN_ELSE(EXO_MARK_UP_NOS_TO_Q[REGIONS_35_I,SECTORS_I]<0,0,delayed_price_output[RE GIONS_35_I,SECTORS_I]/PRICE_TRANSFORMATION*EXO_MARK_UP_NOS_TO_Q[REGIONS_35_ I,SECTORS_I] )))*PRICE_TRANSFORMATION , (delayed_price_GFCF[REGIONS_35_I,SECTORS_I]/PRICE_TRANSFORMATION*(DEPRECIATION_RATE[R EGIONS_35_I,SECTORS_I] +IF_THEN_ELSE(ENDOGENOUS_SWITCH_CLIMATE_CHANGE_DAMAGE_CAPITAL=0,NO_CLIMATE_CHANGE_DAM AGE_RATE_TO_CAPITAL_STOCK[REGIONS_35_I ,SECTORS_I],climate_change_incremental_damage_rate_to_capital_stock[REGIONS_35_I,SECT ORS_I]))*(ZIDZ(1,capital_productivity [REGIONS_35_I,SECTORS_I ])) +(ZIDZ(wage_hour_downwards_rigidity[REGIONS_35_I,SECTORS_I],(BASE_WAGE_HOUR[REGIONS_3 5_I,SECTORS_I]*labour_productivity [REGIONS_35_I, SECTORS_I ])) +SUM(delayed_price_output[REGIONS_35_I,SECTORS_MAP_I!]/PRICE_TRANSFORMATION*technical _coefficients_domestic [REGIONS_35_I,SECTORS_MAP_I!,SECTORS_I])*TAX_RATE_PRODUCT_DOMESTIC_AGGREGATED[REGIONS _35_I,SECTORS_I] +SUM(delayed_price_output[REGIONS_35_MAP_I!,SECTORS_MAP_I!]/PRICE_TRANSFORMATION*tech nical_coefficients_import [REGIONS_35_MAP_I!,SECTORS_MAP_I!,REGIONS_35_I,SECTORS_I]*TAX_RATE_PRODUCTS_IMPORTS_A GGREGATED[REGIONS_35_MAP_I!,REGIONS_35_I ,SECTORS_I]) +delayed_price_output[REGIONS_35_I,SECTORS_I]/PRICE_TRANSFORMATION*TAX_RATE_OUTPUT[RE GIONS_35_I,SECTORS_I] +IF_THEN_ELSE(EXO_MARK_UP_NOS_TO_Q[REGIONS_35_I,SECTORS_I]<0,0, delayed_price_output[REGIONS_35_I,SECTORS_I]/PRICE_TRANSFORMATION*EXO_MARK_ UP_NOS_TO_Q[REGIONS_35_I,SECTORS_I] )))*PRICE_TRANSFORMATION)
    """
    return if_then_else(
        switch_eco_prices() == 0,
        lambda: (
            delayed_ts_price_gfcf()
            / price_transformation()
            * depreciation_rate()
            * zidz(
                xr.DataArray(
                    1,
                    {
                        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                        "SECTORS_I": _subscript_dict["SECTORS_I"],
                    },
                    ["REGIONS_35_I", "SECTORS_I"],
                ),
                base_capital_productivity(),
            )
            + (
                zidz(base_wage_hour(), base_wage_hour() * base_labour_productivity())
                + sum(
                    delayed_ts_price_output().rename({"SECTORS_I": "SECTORS_MAP_I!"})
                    / price_transformation()
                    * technical_coefficients_domestic().rename(
                        {"SECTORS_I": "SECTORS_MAP_I!", "SECTORS_MAP_I": "SECTORS_I"}
                    ),
                    dim=["SECTORS_MAP_I!"],
                )
                * tax_rate_product_domestic_aggregated()
                + sum(
                    delayed_ts_price_output().rename(
                        {
                            "REGIONS_35_I": "REGIONS_35_MAP_I!",
                            "SECTORS_I": "SECTORS_MAP_I!",
                        }
                    )
                    / price_transformation()
                    * technical_coefficients_import().rename(
                        {
                            "REGIONS_35_MAP_I": "REGIONS_35_MAP_I!",
                            "SECTORS_I": "SECTORS_MAP_I!",
                            "SECTORS_MAP_I": "SECTORS_I",
                        }
                    )
                    * tax_rate_products_imports_aggregated().rename(
                        {
                            "REGIONS_35_I": "REGIONS_35_MAP_I!",
                            "REGIONS_35_MAP_I": "REGIONS_35_I",
                        }
                    ),
                    dim=["REGIONS_35_MAP_I!", "SECTORS_MAP_I!"],
                )
                + delayed_ts_price_output() / price_transformation() * tax_rate_output()
                + if_then_else(
                    mark_up() < 0,
                    lambda: xr.DataArray(
                        0,
                        {
                            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                            "SECTORS_I": _subscript_dict["SECTORS_I"],
                        },
                        ["REGIONS_35_I", "SECTORS_I"],
                    ),
                    lambda: delayed_ts_price_output()
                    / price_transformation()
                    * mark_up(),
                )
            )
        )
        * price_transformation(),
        lambda: (
            delayed_ts_price_gfcf()
            / price_transformation()
            * (
                depreciation_rate()
                + if_then_else(
                    np.logical_or(
                        switch_climate_change_damage() == 0,
                        switch_eco_climate_change_damage_capital() == 0,
                    ),
                    lambda: xr.DataArray(
                        0,
                        {
                            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                            "SECTORS_I": _subscript_dict["SECTORS_I"],
                        },
                        ["REGIONS_35_I", "SECTORS_I"],
                    ),
                    lambda: if_then_else(
                        select_climate_change_impacts_sensitivity_sp() == 0,
                        lambda: climate_change_incremental_damage_rate_to_capital_stock(),
                        lambda: climate_change_incremental_damage_rate_to_capital_stock_extrapolations_included(),
                    ),
                )
            )
            * zidz(
                xr.DataArray(
                    1,
                    {
                        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                        "SECTORS_I": _subscript_dict["SECTORS_I"],
                    },
                    ["REGIONS_35_I", "SECTORS_I"],
                ),
                capital_productivity(),
            )
            + (
                zidz(wage_hour(), base_wage_hour() * labour_productivity())
                + sum(
                    delayed_ts_price_output().rename({"SECTORS_I": "SECTORS_MAP_I!"})
                    / price_transformation()
                    * technical_coefficients_domestic().rename(
                        {"SECTORS_I": "SECTORS_MAP_I!", "SECTORS_MAP_I": "SECTORS_I"}
                    ),
                    dim=["SECTORS_MAP_I!"],
                )
                * tax_rate_product_domestic_aggregated()
                + sum(
                    delayed_ts_price_output().rename(
                        {
                            "REGIONS_35_I": "REGIONS_35_MAP_I!",
                            "SECTORS_I": "SECTORS_MAP_I!",
                        }
                    )
                    / price_transformation()
                    * technical_coefficients_import().rename(
                        {
                            "REGIONS_35_MAP_I": "REGIONS_35_MAP_I!",
                            "SECTORS_I": "SECTORS_MAP_I!",
                            "SECTORS_MAP_I": "SECTORS_I",
                        }
                    )
                    * tax_rate_products_imports_aggregated().rename(
                        {
                            "REGIONS_35_I": "REGIONS_35_MAP_I!",
                            "REGIONS_35_MAP_I": "REGIONS_35_I",
                        }
                    ),
                    dim=["REGIONS_35_MAP_I!", "SECTORS_MAP_I!"],
                )
                + delayed_ts_price_output() / price_transformation() * tax_rate_output()
                + if_then_else(
                    mark_up() < 0,
                    lambda: xr.DataArray(
                        0,
                        {
                            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                            "SECTORS_I": _subscript_dict["SECTORS_I"],
                        },
                        ["REGIONS_35_I", "SECTORS_I"],
                    ),
                    lambda: delayed_ts_price_output()
                    / price_transformation()
                    * mark_up(),
                )
            )
        )
        * price_transformation(),
    )


@component.add(
    name="primary_inputs_coefficients_with_changes_in_material_prices",
    units="DMNL",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "primary_inputs_coefficients": 2,
        "percent_price_transformation": 1,
        "time": 1,
        "delayed_ts_price_materials_and_private_households": 1,
        "initial_primary_inputs_coefficients": 1,
    },
)
def primary_inputs_coefficients_with_changes_in_material_prices():
    """
    Primary input coefficients recalculated taking into account changes in the material prices.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "SECTORS_I": _subscript_dict["SECTORS_I"],
        },
        ["REGIONS_35_I", "SECTORS_I"],
    )
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[:, _subscript_dict["SECTORS_NON_EXTRACTION_I"]] = True
    except_subs.loc[:, _subscript_dict["SECTORS_EXTRACTION_I"]] = False
    value.values[except_subs.values] = (
        primary_inputs_coefficients()
        .loc[:, _subscript_dict["SECTORS_NON_EXTRACTION_I"]]
        .rename({"SECTORS_I": "SECTORS_NON_EXTRACTION_I"})
        .values[except_subs.loc[:, _subscript_dict["SECTORS_NON_EXTRACTION_I"]].values]
    )
    value.loc[:, _subscript_dict["SECTORS_EXTRACTION_I"]] = if_then_else(
        time() >= 2015,
        lambda: initial_primary_inputs_coefficients()
        .loc[:, _subscript_dict["SECTORS_EXTRACTION_I"]]
        .rename({"SECTORS_I": "SECTORS_EXTRACTION_I"})
        * delayed_ts_price_materials_and_private_households()
        .loc[:, _subscript_dict["SECTORS_EXTRACTION_I"]]
        .rename({"SECTORS_EXTRACTION_PH_I": "SECTORS_EXTRACTION_I"})
        / percent_price_transformation(),
        lambda: primary_inputs_coefficients()
        .loc[:, _subscript_dict["SECTORS_EXTRACTION_I"]]
        .rename({"SECTORS_I": "SECTORS_EXTRACTION_I"}),
    ).values
    return value


@component.add(
    name="SWITCH_ECO_PRICES",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_eco_prices"},
)
def switch_eco_prices():
    """
    This switch can take two values: 0: the (sub)module runs isolated from the rest of WILIAM, replacing inter(sub)module variables with exogenous parameters. 1: the (sub)module runs integrated with the rest of WILIAM.
    """
    return _ext_constant_switch_eco_prices()


_ext_constant_switch_eco_prices = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_ECO_PRICES",
    {},
    _root,
    {},
    "_ext_constant_switch_eco_prices",
)
