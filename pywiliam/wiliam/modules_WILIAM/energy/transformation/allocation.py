"""
Module energy.transformation.allocation
Translated using PySD version 3.10.0
"""


@component.add(
    name="aggregated_TO_production_by_commodity",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_TO_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"protra_to_allocated": 1},
)
def aggregated_to_production_by_commodity():
    """
    Output from PROTRA (after allocation) aggregated
    """
    return sum(
        protra_to_allocated().rename({"NRG_PROTRA_I": "NRG_PROTRA_I!"}),
        dim=["NRG_PROTRA_I!"],
    )


@component.add(
    name="ALLOCATION_TOLERANCE_RANGE",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="Normal",
)
def allocation_tolerance_range():
    """
    This value determines the upper and lower priorities starting from the marginal value and therefore takes into account technologies which are near to the marginal level.
    """
    return 0.15


@component.add(
    name="biomass_price_function",
    comp_type="Auxiliary",
    comp_subtype="with Lookup",
    depends_on={"pe_forestry_demand_delayed": 1},
)
def biomass_price_function():
    """
    Price-cost curve from Rogner et al 2012
    !EJ/yr
    !$/GJ
    """
    return np.interp(
        pe_forestry_demand_delayed(),
        [
            2.60035,
            4.41968,
            6.23928,
            7.31991,
            7.33025,
            7.82069,
            9.75033,
            11.5697,
            13.389,
            15.2083,
            17.0277,
            18.847,
            20.6664,
            22.4857,
            24.305,
            26.1244,
            27.9437,
            29.7631,
            31.5824,
            33.4017,
            35.2211,
            37.0404,
            38.8597,
            40.6791,
            42.4984,
            44.3178,
            46.1378,
            46.4779,
            46.7293,
            46.7397,
            46.7502,
            46.7607,
            46.7711,
            47.2618,
            49.1917,
            51.011,
            52.8303,
            54.6497,
            56.469,
            58.2884,
            60.1077,
            61.9279,
            62.2683,
            62.5197,
            62.5302,
            62.5406,
            62.5511,
            62.5615,
            63.052,
            64.9816,
            66.8009,
            68.6203,
            70.4396,
            72.259,
            74.0783,
            75.8976,
            77.717,
            79.5363,
            81.1076,
        ],
        [
            1.04792,
            1.04676,
            1.05221,
            1.19357,
            1.45751,
            1.91401,
            2.0142,
            2.01304,
            2.01187,
            2.01071,
            2.00955,
            2.00839,
            2.00723,
            2.00607,
            2.0049,
            2.00374,
            2.00258,
            2.00142,
            2.00026,
            1.99909,
            1.99793,
            1.99677,
            1.99561,
            1.99445,
            1.99329,
            1.99212,
            2.00861,
            2.24559,
            2.33038,
            2.59736,
            2.86433,
            3.13131,
            3.39828,
            3.85999,
            3.96711,
            3.96595,
            3.96478,
            3.96362,
            3.96246,
            3.9613,
            3.96014,
            3.98104,
            4.22574,
            4.31053,
            4.5775,
            4.84448,
            5.11146,
            5.37843,
            5.83494,
            5.93512,
            5.93396,
            5.9328,
            5.93164,
            5.93048,
            5.92931,
            5.92815,
            5.92699,
            5.92583,
            5.92482,
        ],
    )


@component.add(
    name="Biomass_price_global_Mdollars_per_EJ",
    units="Mdollars/EJ",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "biomass_price_function": 1,
        "unit_conversion_gj_ej": 1,
        "unit_conversion_dollars_mdollars": 1,
    },
)
def biomass_price_global_mdollars_per_ej():
    return (
        biomass_price_function()
        * unit_conversion_gj_ej()
        / unit_conversion_dollars_mdollars()
    )


@component.add(
    name="CF_PROTRA",
    units="DMNL",
    subscripts=["REGIONS_9_I", "NRG_TO_I", "NRG_PROTRA_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_to_allocated": 1,
        "unit_conversion_hours_year": 1,
        "protra_capacity_stock": 1,
        "unit_conversion_tw_per_ej_per_year": 1,
    },
)
def cf_protra():
    """
    Capacity factor of energy transformation processes.
    """
    return zidz(
        protra_to_allocated(),
        protra_capacity_stock()
        * unit_conversion_hours_year()
        * unit_conversion_tw_per_ej_per_year(),
    )


@component.add(
    name="CF_PROTRA_FULL_LOAD_HOURS",
    units="1",
    subscripts=["REGIONS_9_I", "NRG_PROTRA_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"protra_max_full_load_hours": 1, "unit_conversion_hours_year": 1},
)
def cf_protra_full_load_hours():
    """
    Initial Capacity factor of energy transformation processes.
    """
    return protra_max_full_load_hours() / unit_conversion_hours_year()


@component.add(
    name="CF_PROTRA_full_load_hours_after_constraints",
    units="1",
    subscripts=["REGIONS_9_I", "NRG_PROTRA_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_max_full_load_hours_after_constraints": 1,
        "unit_conversion_hours_year": 1,
    },
)
def cf_protra_full_load_hours_after_constraints():
    """
    Actual capacity factor of energy transformation processes.
    """
    return protra_max_full_load_hours_after_constraints() / unit_conversion_hours_year()


@component.add(
    name="check_elec_allocation",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "max_to_from_existing_stock_by_protra_pp": 1,
        "remaining_to_to_be_allocated": 1,
        "protra_elec_allocation": 1,
    },
)
def check_elec_allocation():
    return np.minimum(
        sum(
            max_to_from_existing_stock_by_protra_pp()
            .loc[:, "TO_elec", :]
            .reset_coords(drop=True)
            .rename({"NRG_PRO_I": "NRG_PRO_I!"}),
            dim=["NRG_PRO_I!"],
        ),
        remaining_to_to_be_allocated().loc[:, "TO_elec"].reset_coords(drop=True),
    ) - sum(
        protra_elec_allocation()
        .loc[:, "TO_elec", :]
        .reset_coords(drop=True)
        .rename({"NRG_PRO_I": "NRG_PRO_I!"}),
        dim=["NRG_PRO_I!"],
    )


@component.add(
    name="check_PROTRA_heat_allocation",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "max_to_from_existing_stock_by_protra_hp_and_chp": 1,
        "to_by_commodity": 1,
        "protra_heat_allocation": 1,
    },
)
def check_protra_heat_allocation():
    return np.minimum(
        sum(
            max_to_from_existing_stock_by_protra_hp_and_chp()
            .loc[:, "TO_heat", :]
            .reset_coords(drop=True)
            .rename({"NRG_PRO_I": "NRG_PRO_I!"}),
            dim=["NRG_PRO_I!"],
        ),
        to_by_commodity().loc[:, "TO_heat"].reset_coords(drop=True),
    ) - sum(
        protra_heat_allocation()
        .loc[:, "TO_heat", :]
        .reset_coords(drop=True)
        .rename({"NRG_PRO_I": "NRG_PRO_I!"}),
        dim=["NRG_PRO_I!"],
    )


@component.add(
    name="CHP_HEAT_POWER_RATIO_9R",
    subscripts=["REGIONS_9_I", "PROTRA_CHP_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_chp_heat_power_ratio_9r"},
)
def chp_heat_power_ratio_9r():
    """
    Heat to power ratio of CHPs; value < 1: more elec than heat value > 1: more heat than elec
    """
    return _ext_constant_chp_heat_power_ratio_9r()


_ext_constant_chp_heat_power_ratio_9r = ExtConstant(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "CHP-heat-to-power-ratio",
    "CHP_HEAT_POWER_RATIO_9R",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PROTRA_CHP_I": _subscript_dict["PROTRA_CHP_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PROTRA_CHP_I": _subscript_dict["PROTRA_CHP_I"],
    },
    "_ext_constant_chp_heat_power_ratio_9r",
)


@component.add(
    name="CHP_production",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_COMMODITIES_I", "PROTRA_CHP_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_heat_allocation": 2,
        "max_to_from_existing_stock_by_protra": 1,
        "chp_heat_power_ratio_9r": 1,
    },
)
def chp_production():
    """
    Production of TO_heat and TO_elec from CHPs based on heat allocation
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "NRG_COMMODITIES_I": _subscript_dict["NRG_COMMODITIES_I"],
            "PROTRA_CHP_I": _subscript_dict["PROTRA_CHP_I"],
        },
        ["REGIONS_9_I", "NRG_COMMODITIES_I", "PROTRA_CHP_I"],
    )
    value.loc[:, ["TO_heat"], :] = (
        protra_heat_allocation()
        .loc[:, "TO_heat", _subscript_dict["PROTRA_CHP_I"]]
        .reset_coords(drop=True)
        .rename({"NRG_PRO_I": "PROTRA_CHP_I"})
        .expand_dims({"NRG_COMMODITIES_I": ["TO_heat"]}, 1)
        .values
    )
    value.loc[:, ["TO_elec"], :] = (
        if_then_else(
            max_to_from_existing_stock_by_protra()
            .loc[:, "TO_heat", _subscript_dict["PROTRA_CHP_I"]]
            .reset_coords(drop=True)
            .rename({"NRG_PRO_I": "PROTRA_CHP_I"})
            == 0,
            lambda: xr.DataArray(
                0,
                {
                    "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                    "PROTRA_CHP_I": _subscript_dict["PROTRA_CHP_I"],
                },
                ["REGIONS_9_I", "PROTRA_CHP_I"],
            ),
            lambda: protra_heat_allocation()
            .loc[:, "TO_heat", _subscript_dict["PROTRA_CHP_I"]]
            .reset_coords(drop=True)
            .rename({"NRG_PRO_I": "PROTRA_CHP_I"})
            / chp_heat_power_ratio_9r(),
        )
        .expand_dims({"NRG_COMMODITIES_I": ["TO_elec"]}, 1)
        .values
    )
    return value


@component.add(
    name="CO2_emission_factor_by_PROTRA",
    units="kg/TJ",
    subscripts=["NRG_PROTRA_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={"co2_emission_factors_pe": 22},
)
def co2_emission_factor_by_protra():
    """
    regions not strictly required here, in emission intensities values are the same for all regions. Oter PROTRA equations pending.
    """
    value = xr.DataArray(
        np.nan, {"NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"]}, ["NRG_PROTRA_I"]
    )
    value.loc[["PROTRA_CHP_gas_fuels"]] = float(
        co2_emission_factors_pe().loc["PE_natural_gas"]
    )
    value.loc[["PROTRA_CHP_gas_fuels_CCS"]] = (
        float(co2_emission_factors_pe().loc["PE_natural_gas"]) * 0
    )
    value.loc[["PROTRA_CHP_geothermal_DEACTIVATED"]] = 0
    value.loc[["PROTRA_CHP_liquid_fuels"]] = float(
        co2_emission_factors_pe().loc["PE_oil"]
    )
    value.loc[["PROTRA_CHP_liquid_fuels_CCS"]] = (
        float(co2_emission_factors_pe().loc["PE_oil"]) * 0
    )
    value.loc[["PROTRA_CHP_solid_fossil"]] = float(
        co2_emission_factors_pe().loc["PE_coal"]
    )
    value.loc[["PROTRA_CHP_solid_fossil_CCS"]] = (
        float(co2_emission_factors_pe().loc["PE_coal"]) * 0
    )
    value.loc[["PROTRA_CHP_waste"]] = float(co2_emission_factors_pe().loc["PE_waste"])
    value.loc[["PROTRA_CHP_solid_bio"]] = float(
        co2_emission_factors_pe().loc["PE_forestry_products"]
    )
    value.loc[["PROTRA_CHP_solid_bio_CCS"]] = (
        float(co2_emission_factors_pe().loc["PE_forestry_products"]) * 0
    )
    value.loc[["PROTRA_HP_gas_fuels"]] = float(
        co2_emission_factors_pe().loc["PE_natural_gas"]
    )
    value.loc[["PROTRA_HP_solid_bio"]] = float(
        co2_emission_factors_pe().loc["PE_forestry_products"]
    )
    value.loc[["PROTRA_HP_geothermal"]] = 0
    value.loc[["PROTRA_HP_liquid_fuels"]] = float(
        co2_emission_factors_pe().loc["PE_oil"]
    )
    value.loc[["PROTRA_HP_solar_DEACTIVATED"]] = 0
    value.loc[["PROTRA_HP_solid_fossil"]] = float(
        co2_emission_factors_pe().loc["PE_coal"]
    )
    value.loc[["PROTRA_HP_waste"]] = float(co2_emission_factors_pe().loc["PE_waste"])
    value.loc[["PROTRA_PP_solid_bio"]] = float(
        co2_emission_factors_pe().loc["PE_forestry_products"]
    )
    value.loc[["PROTRA_PP_solid_bio_CCS"]] = (
        float(co2_emission_factors_pe().loc["PE_forestry_products"]) * 0
    )
    value.loc[["PROTRA_PP_gas_fuels"]] = float(
        co2_emission_factors_pe().loc["PE_natural_gas"]
    )
    value.loc[["PROTRA_PP_gas_fuels_CCS"]] = (
        float(co2_emission_factors_pe().loc["PE_natural_gas"]) * 0
    )
    value.loc[["PROTRA_PP_geothermal"]] = 0
    value.loc[["PROTRA_PP_hydropower_dammed"]] = 0
    value.loc[["PROTRA_PP_hydropower_run_of_river"]] = 0
    value.loc[["PROTRA_PP_liquid_fuels"]] = float(
        co2_emission_factors_pe().loc["PE_oil"]
    )
    value.loc[["PROTRA_PP_liquid_fuels_CCS"]] = (
        float(co2_emission_factors_pe().loc["PE_oil"]) * 0
    )
    value.loc[["PROTRA_PP_nuclear"]] = 0
    value.loc[["PROTRA_PP_oceanic"]] = 0
    value.loc[["PROTRA_PP_solar_CSP"]] = 0
    value.loc[["PROTRA_PP_solar_open_space_PV"]] = 0
    value.loc[["PROTRA_PP_solar_urban_PV"]] = 0
    value.loc[["PROTRA_PP_solid_fossil"]] = 0
    value.loc[["PROTRA_PP_solid_fossil_CCS"]] = 0 * 0
    value.loc[["PROTRA_PP_waste"]] = float(co2_emission_factors_pe().loc["PE_waste"])
    value.loc[["PROTRA_PP_waste_CCS"]] = (
        float(co2_emission_factors_pe().loc["PE_waste"]) * 0
    )
    value.loc[["PROTRA_PP_wind_offshore"]] = 0
    value.loc[["PROTRA_PP_wind_onshore"]] = 0
    value.loc[["PROTRA_blending_gas_fuels"]] = 0
    value.loc[["PROTRA_blending_liquid_fuels"]] = 0
    value.loc[["PROTRA_no_process_TI_hydrogen"]] = 0
    value.loc[["PROTRA_no_process_TI_solid_bio"]] = 0
    value.loc[["PROTRA_no_process_TI_solid_fossil"]] = 0
    return value


@component.add(
    name="CO2_emission_factor_by_PROTRA_MT_per_EJ",
    units="Mt/EJ",
    subscripts=["NRG_PROTRA_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "co2_emission_factor_by_protra": 1,
        "unit_conversion_tj_ej": 1,
        "unit_conversion_kg_mt": 1,
    },
)
def co2_emission_factor_by_protra_mt_per_ej():
    return (
        co2_emission_factor_by_protra()
        * unit_conversion_tj_ej()
        / unit_conversion_kg_mt()
    )


@component.add(
    name="Coal_price_Mdollars_per_EJ",
    units="Mdollars/EJ",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "switch_energy": 1,
        "coal_price_historical_t": 1,
        "estimated_coal_price": 1,
        "mixed_coal_conversion_factor_mt_to_ej": 1,
    },
)
def coal_price_mdollars_per_ej():
    return if_then_else(
        np.logical_or(time() < 2015, switch_energy() == 0),
        lambda: coal_price_historical_t() * 44.4,
        lambda: estimated_coal_price() * mixed_coal_conversion_factor_mt_to_ej(),
    )


@component.add(
    name="CONVERSION_FACTOR_Mt_to_EJ",
    subscripts=["COAL_TYPES_I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def conversion_factor_mt_to_ej():
    """
    Conversion factor Mt to EJ of hard coal and brown coal based on the Source: Global Energy Assessment-Toward a Sustainable Future (Rogner et al., 2012)
    """
    value = xr.DataArray(
        np.nan, {"COAL_TYPES_I": _subscript_dict["COAL_TYPES_I"]}, ["COAL_TYPES_I"]
    )
    value.loc[["HARD_COAL"]] = 40.51
    value.loc[["BROWN_COAL"]] = 103.3
    return value


@component.add(
    name="delayed_TS_PROTRA_capacity_stock",
    units="TW",
    subscripts=["REGIONS_9_I", "NRG_TO_I", "NRG_PROTRA_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_protra_capacity_stock": 1},
    other_deps={
        "_delayfixed_delayed_ts_protra_capacity_stock": {
            "initial": {"initial_protra_capacity_stock": 1, "time_step": 1},
            "step": {"protra_capacity_stock": 1},
        }
    },
)
def delayed_ts_protra_capacity_stock():
    """
    Delay to break simulataneous equations in the feedback demand nuclear -> demand uranium -> uranium availability -> demand nuclear.
    """
    return _delayfixed_delayed_ts_protra_capacity_stock()


_delayfixed_delayed_ts_protra_capacity_stock = DelayFixed(
    lambda: protra_capacity_stock(),
    lambda: time_step(),
    lambda: initial_protra_capacity_stock()
    .loc[_subscript_dict["REGIONS_9_I"], :, :]
    .rename({"REGIONS_36_I": "REGIONS_9_I"}),
    time_step,
    "_delayfixed_delayed_ts_protra_capacity_stock",
)


@component.add(
    name="fuel_price_by_PROTRA_9R",
    units="Mdollars/EJ",
    subscripts=["REGIONS_9_I", "NRG_PROTRA_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"fuel_price_by_protra_world": 1},
)
def fuel_price_by_protra_9r():
    return fuel_price_by_protra_world().expand_dims(
        {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, 0
    )


@component.add(
    name="fuel_price_by_PROTRA_9R_adjusted",
    units="Mdollars/EJ",
    subscripts=["REGIONS_9_I", "NRG_PROTRA_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "fuel_price_by_protra_9r": 11,
        "availability_of_forestry_products_for_energy": 5,
        "switch_nrg_limited_res_potentials": 5,
        "switch_energy": 5,
    },
)
def fuel_price_by_protra_9r_adjusted():
    """
    taken into account regionalised biomass availability from land use model
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
        },
        ["REGIONS_9_I", "NRG_PROTRA_I"],
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, ["PROTRA_CHP_solid_bio"]] = False
    except_subs.loc[:, ["PROTRA_CHP_solid_bio_CCS"]] = False
    except_subs.loc[:, ["PROTRA_HP_solid_bio"]] = False
    except_subs.loc[:, ["PROTRA_PP_solid_bio"]] = False
    except_subs.loc[:, ["PROTRA_PP_solid_bio_CCS"]] = False
    value.values[except_subs.values] = fuel_price_by_protra_9r().values[
        except_subs.values
    ]
    value.loc[:, ["PROTRA_CHP_solid_bio_CCS"]] = (
        if_then_else(
            np.logical_or(
                switch_energy() == 0, switch_nrg_limited_res_potentials() == 0
            ),
            lambda: fuel_price_by_protra_9r()
            .loc[:, "PROTRA_CHP_solid_bio_CCS"]
            .reset_coords(drop=True),
            lambda: xidz(
                fuel_price_by_protra_9r()
                .loc[:, "PROTRA_CHP_solid_bio_CCS"]
                .reset_coords(drop=True),
                availability_of_forestry_products_for_energy(),
                1000,
            ),
        )
        .expand_dims({"NRG_PRO_I": ["PROTRA_CHP_solid_bio_CCS"]}, 1)
        .values
    )
    value.loc[:, ["PROTRA_HP_solid_bio"]] = (
        if_then_else(
            np.logical_or(
                switch_energy() == 0, switch_nrg_limited_res_potentials() == 0
            ),
            lambda: fuel_price_by_protra_9r()
            .loc[:, "PROTRA_HP_solid_bio"]
            .reset_coords(drop=True),
            lambda: xidz(
                fuel_price_by_protra_9r()
                .loc[:, "PROTRA_HP_solid_bio"]
                .reset_coords(drop=True),
                availability_of_forestry_products_for_energy(),
                1000,
            ),
        )
        .expand_dims({"NRG_PRO_I": ["PROTRA_HP_solid_bio"]}, 1)
        .values
    )
    value.loc[:, ["PROTRA_PP_solid_bio"]] = (
        if_then_else(
            np.logical_or(
                switch_energy() == 0, switch_nrg_limited_res_potentials() == 0
            ),
            lambda: fuel_price_by_protra_9r()
            .loc[:, "PROTRA_PP_solid_bio"]
            .reset_coords(drop=True),
            lambda: xidz(
                fuel_price_by_protra_9r()
                .loc[:, "PROTRA_PP_solid_bio"]
                .reset_coords(drop=True),
                availability_of_forestry_products_for_energy(),
                1000,
            ),
        )
        .expand_dims({"NRG_PRO_I": ["PROTRA_PP_solid_bio"]}, 1)
        .values
    )
    value.loc[:, ["PROTRA_PP_solid_bio_CCS"]] = (
        if_then_else(
            np.logical_or(
                switch_energy() == 0, switch_nrg_limited_res_potentials() == 0
            ),
            lambda: fuel_price_by_protra_9r()
            .loc[:, "PROTRA_PP_solid_bio_CCS"]
            .reset_coords(drop=True),
            lambda: xidz(
                fuel_price_by_protra_9r()
                .loc[:, "PROTRA_PP_solid_bio_CCS"]
                .reset_coords(drop=True),
                availability_of_forestry_products_for_energy(),
                1000,
            ),
        )
        .expand_dims({"NRG_PRO_I": ["PROTRA_PP_solid_bio_CCS"]}, 1)
        .values
    )
    value.loc[:, ["PROTRA_CHP_solid_bio"]] = (
        if_then_else(
            np.logical_or(
                switch_energy() == 0, switch_nrg_limited_res_potentials() == 0
            ),
            lambda: fuel_price_by_protra_9r()
            .loc[:, "PROTRA_CHP_solid_bio"]
            .reset_coords(drop=True),
            lambda: xidz(
                fuel_price_by_protra_9r()
                .loc[:, "PROTRA_CHP_solid_bio"]
                .reset_coords(drop=True),
                availability_of_forestry_products_for_energy(),
                1000,
            ),
        )
        .expand_dims({"NRG_PRO_I": ["PROTRA_CHP_solid_bio"]}, 1)
        .values
    )
    return value


@component.add(
    name="fuel_price_by_PROTRA_world",
    units="Mdollars/EJ",
    subscripts=["NRG_PROTRA_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "gas_price_mdollars_per_ej": 5,
        "oil_price_mdollars_per_ej": 5,
        "coal_price_mdollars_per_ej": 3,
        "biomass_price_global_mdollars_per_ej": 5,
        "nuclear_price_mdollars_per_ej_fictional": 1,
    },
)
def fuel_price_by_protra_world():
    value = xr.DataArray(
        np.nan, {"NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"]}, ["NRG_PROTRA_I"]
    )
    value.loc[["PROTRA_CHP_gas_fuels"]] = gas_price_mdollars_per_ej()
    value.loc[["PROTRA_CHP_gas_fuels_CCS"]] = gas_price_mdollars_per_ej()
    value.loc[["PROTRA_CHP_geothermal_DEACTIVATED"]] = 0
    value.loc[["PROTRA_CHP_liquid_fuels"]] = oil_price_mdollars_per_ej()
    value.loc[["PROTRA_CHP_liquid_fuels_CCS"]] = oil_price_mdollars_per_ej()
    value.loc[["PROTRA_CHP_solid_fossil"]] = coal_price_mdollars_per_ej()
    value.loc[["PROTRA_CHP_solid_fossil_CCS"]] = coal_price_mdollars_per_ej()
    value.loc[["PROTRA_CHP_waste"]] = 0
    value.loc[["PROTRA_CHP_solid_bio"]] = biomass_price_global_mdollars_per_ej()
    value.loc[["PROTRA_CHP_solid_bio_CCS"]] = biomass_price_global_mdollars_per_ej()
    value.loc[["PROTRA_HP_gas_fuels"]] = gas_price_mdollars_per_ej()
    value.loc[["PROTRA_HP_solid_bio"]] = biomass_price_global_mdollars_per_ej()
    value.loc[["PROTRA_HP_geothermal"]] = 0
    value.loc[["PROTRA_HP_liquid_fuels"]] = oil_price_mdollars_per_ej()
    value.loc[["PROTRA_HP_solar_DEACTIVATED"]] = 0
    value.loc[["PROTRA_HP_solid_fossil"]] = coal_price_mdollars_per_ej()
    value.loc[["PROTRA_HP_waste"]] = 0
    value.loc[["PROTRA_PP_solid_bio"]] = biomass_price_global_mdollars_per_ej()
    value.loc[["PROTRA_PP_solid_bio_CCS"]] = biomass_price_global_mdollars_per_ej()
    value.loc[["PROTRA_PP_gas_fuels"]] = gas_price_mdollars_per_ej()
    value.loc[["PROTRA_PP_gas_fuels_CCS"]] = gas_price_mdollars_per_ej()
    value.loc[["PROTRA_PP_geothermal"]] = 0
    value.loc[["PROTRA_PP_hydropower_dammed"]] = 0
    value.loc[["PROTRA_PP_hydropower_run_of_river"]] = 0
    value.loc[["PROTRA_PP_liquid_fuels"]] = oil_price_mdollars_per_ej()
    value.loc[["PROTRA_PP_liquid_fuels_CCS"]] = oil_price_mdollars_per_ej()
    value.loc[["PROTRA_PP_nuclear"]] = nuclear_price_mdollars_per_ej_fictional()
    value.loc[["PROTRA_PP_oceanic"]] = 0
    value.loc[["PROTRA_PP_solar_CSP"]] = 0
    value.loc[["PROTRA_PP_solar_open_space_PV"]] = 0
    value.loc[["PROTRA_PP_solar_urban_PV"]] = 0
    value.loc[["PROTRA_PP_solid_fossil"]] = 0
    value.loc[["PROTRA_PP_solid_fossil_CCS"]] = 0
    value.loc[["PROTRA_PP_waste"]] = 0
    value.loc[["PROTRA_PP_waste_CCS"]] = 0
    value.loc[["PROTRA_PP_wind_offshore"]] = 0
    value.loc[["PROTRA_PP_wind_onshore"]] = 0
    value.loc[["PROTRA_blending_gas_fuels"]] = 0
    value.loc[["PROTRA_blending_liquid_fuels"]] = 0
    value.loc[["PROTRA_no_process_TI_hydrogen"]] = 0
    value.loc[["PROTRA_no_process_TI_solid_bio"]] = 0
    value.loc[["PROTRA_no_process_TI_solid_fossil"]] = 0
    return value


@component.add(
    name="Gas_price_Mdollars_per_EJ",
    units="Mdollars/EJ",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "switch_energy": 1,
        "unit_conversion_dollars_mdollars": 2,
        "unit_conversion_mmbtu_ej": 2,
        "gas_price_historical": 1,
        "estimated_gas_price": 1,
    },
)
def gas_price_mdollars_per_ej():
    return if_then_else(
        np.logical_or(time() < 2015, switch_energy() == 0),
        lambda: gas_price_historical()
        * unit_conversion_mmbtu_ej()
        / unit_conversion_dollars_mdollars(),
        lambda: estimated_gas_price()
        * unit_conversion_mmbtu_ej()
        / unit_conversion_dollars_mdollars(),
    )


@component.add(
    name="INTIAL_OPEX_by_PROTRA_and_region",
    units="MD/EJ",
    subscripts=["REGIONS_9_I", "NRG_PROTRA_I"],
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_intial_opex_by_protra_and_region": 1},
    other_deps={
        "_initial_intial_opex_by_protra_and_region": {"initial": {}, "step": {}}
    },
)
def intial_opex_by_protra_and_region():
    return _initial_intial_opex_by_protra_and_region()


_initial_intial_opex_by_protra_and_region = Initial(
    lambda: xr.DataArray(
        1,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
        },
        ["REGIONS_9_I", "NRG_PROTRA_I"],
    ),
    "_initial_intial_opex_by_protra_and_region",
)


@component.add(
    name="max_OPEX_signal",
    units="MD/EJ",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"opex_by_protra_and_region_delayed_ts": 1},
)
def max_opex_signal():
    return vmax(
        opex_by_protra_and_region_delayed_ts().rename(
            {"NRG_PROTRA_I": "NRG_PROTRA_I!"}
        ),
        dim=["NRG_PROTRA_I!"],
    )


@component.add(
    name="max_TO_from_existing_stock_by_PROTRA",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_TO_I", "NRG_PRO_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_capacity_stock": 1,
        "protra_max_full_load_hours_after_constraints": 1,
        "unit_conversion_tw_per_ej_per_year": 1,
    },
)
def max_to_from_existing_stock_by_protra():
    """
    maximum possible TO production volumes that could be produced from the existing transformation capacity (=powerplant, heatplant and CHP) stock
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "NRG_TO_I": _subscript_dict["NRG_TO_I"],
            "NRG_PRO_I": _subscript_dict["NRG_PRO_I"],
        },
        ["REGIONS_9_I", "NRG_TO_I", "NRG_PRO_I"],
    )
    value.loc[:, :, _subscript_dict["NRG_PROTRA_I"]] = np.maximum(
        0,
        protra_capacity_stock()
        * protra_max_full_load_hours_after_constraints()
        * unit_conversion_tw_per_ej_per_year(),
    ).values
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, :, _subscript_dict["NRG_PROTRA_I"]] = False
    value.values[except_subs.values] = 0
    return value


@component.add(
    name="max_TO_from_existing_stock_by_PROTRA_HP_and_CHP",
    subscripts=["REGIONS_9_I", "NRG_COMMODITIES_I", "NRG_PRO_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={"max_to_from_existing_stock_by_protra": 1},
)
def max_to_from_existing_stock_by_protra_hp_and_chp():
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "NRG_COMMODITIES_I": _subscript_dict["NRG_COMMODITIES_I"],
            "NRG_PRO_I": _subscript_dict["NRG_PRO_I"],
        },
        ["REGIONS_9_I", "NRG_COMMODITIES_I", "NRG_PRO_I"],
    )
    value.loc[:, ["TO_heat"], _subscript_dict["PROTRA_CHP_HP_I"]] = (
        max_to_from_existing_stock_by_protra()
        .loc[:, "TO_heat", _subscript_dict["PROTRA_CHP_HP_I"]]
        .reset_coords(drop=True)
        .rename({"NRG_PRO_I": "PROTRA_CHP_HP_I"})
        .expand_dims({"NRG_COMMODITIES_I": ["TO_heat"]}, 1)
        .values
    )
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[:, ["TO_heat"], :] = True
    except_subs.loc[:, ["TO_heat"], _subscript_dict["PROTRA_CHP_HP_I"]] = False
    value.values[except_subs.values] = 0
    return value


@component.add(
    name="max_TO_from_existing_stock_by_PROTRA_PP",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_COMMODITIES_I", "NRG_PRO_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={"max_to_from_existing_stock_by_protra": 1},
)
def max_to_from_existing_stock_by_protra_pp():
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "NRG_COMMODITIES_I": _subscript_dict["NRG_COMMODITIES_I"],
            "NRG_PRO_I": _subscript_dict["NRG_PRO_I"],
        },
        ["REGIONS_9_I", "NRG_COMMODITIES_I", "NRG_PRO_I"],
    )
    value.loc[:, ["TO_elec"], _subscript_dict["PROTRA_PP_I"]] = (
        max_to_from_existing_stock_by_protra()
        .loc[:, "TO_elec", _subscript_dict["PROTRA_PP_I"]]
        .reset_coords(drop=True)
        .rename({"NRG_PRO_I": "PROTRA_PP_I"})
        .expand_dims({"NRG_COMMODITIES_I": ["TO_elec"]}, 1)
        .values
    )
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[:, ["TO_elec"], :] = True
    except_subs.loc[:, ["TO_elec"], _subscript_dict["PROTRA_PP_I"]] = False
    value.values[except_subs.values] = 0
    return value


@component.add(
    name="min_OPEX_signal",
    units="MD/EJ",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"opex_by_protra_and_region_delayed_ts": 1},
)
def min_opex_signal():
    return vmin(
        opex_by_protra_and_region_delayed_ts().rename(
            {"NRG_PROTRA_I": "NRG_PROTRA_I!"}
        ),
        dim=["NRG_PROTRA_I!"],
    )


@component.add(
    name="mixed_coal_conversion_factor_Mt_to_EJ",
    units="Mt/EJ",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"extraction_of_coal": 6, "conversion_factor_mt_to_ej": 2},
)
def mixed_coal_conversion_factor_mt_to_ej():
    """
    mixed conversion factor (accounting for hard coal / brown coal share)
    """
    return float(extraction_of_coal().loc["HARD_COAL"]) / (
        float(extraction_of_coal().loc["HARD_COAL"])
        + float(extraction_of_coal().loc["BROWN_COAL"])
    ) * float(conversion_factor_mt_to_ej().loc["HARD_COAL"]) + float(
        extraction_of_coal().loc["BROWN_COAL"]
    ) / (
        float(extraction_of_coal().loc["HARD_COAL"])
        + float(extraction_of_coal().loc["BROWN_COAL"])
    ) * float(
        conversion_factor_mt_to_ej().loc["BROWN_COAL"]
    )


@component.add(
    name="nuclear_implicit_subsidy",
    units="Mdollars/EJ",
    comp_type="Constant",
    comp_subtype="Normal",
)
def nuclear_implicit_subsidy():
    return -2000


@component.add(
    name="Nuclear_price_Mdollars_per_EJ_fictional",
    units="Mdollars/EJ",
    comp_type="Constant",
    comp_subtype="Normal",
)
def nuclear_price_mdollars_per_ej_fictional():
    return 500


@component.add(
    name="Oil_price_Mdollars_per_EJ",
    units="Mdollars/EJ",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "switch_energy": 1,
        "oil_price_historical_bbl": 1,
        "oil_bbl_per_ej": 2,
        "estimated_oil_price": 1,
    },
)
def oil_price_mdollars_per_ej():
    return if_then_else(
        np.logical_or(time() < 2015, switch_energy() == 0),
        lambda: oil_price_historical_bbl() * oil_bbl_per_ej() / 10**6,
        lambda: estimated_oil_price() * oil_bbl_per_ej() / 10**6,
    )


@component.add(
    name="OPEX_by_PROTRA_and_region",
    units="Mdollars/EJ",
    subscripts=["REGIONS_9_I", "NRG_PROTRA_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_fuel_utilization_ratio": 1,
        "co2_price_sp": 1,
        "fuel_price_by_protra_9r_adjusted": 1,
        "co2_emission_factor_by_protra_mt_per_ej": 1,
    },
)
def opex_by_protra_and_region():
    """
    OPEX taking into account efficiency, fuelprice, CO2-cost and O&M cost (to be implemented)
    """
    return (
        1
        / protra_fuel_utilization_ratio()
        .loc[_subscript_dict["REGIONS_9_I"], :]
        .rename({"REGIONS_36_I": "REGIONS_9_I"})
        * (
            fuel_price_by_protra_9r_adjusted()
            + (
                co2_emission_factor_by_protra_mt_per_ej()
                * co2_price_sp()
                .loc[_subscript_dict["REGIONS_9_I"]]
                .rename({"REGIONS_36_I": "REGIONS_9_I"})
            ).transpose("REGIONS_9_I", "NRG_PROTRA_I")
        )
    )


@component.add(
    name="OPEX_by_PROTRA_and_region_delayed_TS",
    units="MD/EJ",
    subscripts=["REGIONS_9_I", "NRG_PROTRA_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_opex_by_protra_and_region_delayed_ts": 1},
    other_deps={
        "_delayfixed_opex_by_protra_and_region_delayed_ts": {
            "initial": {"intial_opex_by_protra_and_region": 1, "time_step": 1},
            "step": {"opex_by_protra_and_region": 1},
        }
    },
)
def opex_by_protra_and_region_delayed_ts():
    return _delayfixed_opex_by_protra_and_region_delayed_ts()


_delayfixed_opex_by_protra_and_region_delayed_ts = DelayFixed(
    lambda: opex_by_protra_and_region(),
    lambda: time_step(),
    lambda: intial_opex_by_protra_and_region(),
    time_step,
    "_delayfixed_opex_by_protra_and_region_delayed_ts",
)


@component.add(
    name="PE_forestry_demand_delayed",
    units="EJ/Year",
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_pe_forestry_demand_delayed": 1},
    other_deps={
        "_delayfixed_pe_forestry_demand_delayed": {
            "initial": {"time_step": 1},
            "step": {"world_pe_by_commodity": 1},
        }
    },
)
def pe_forestry_demand_delayed():
    return _delayfixed_pe_forestry_demand_delayed()


_delayfixed_pe_forestry_demand_delayed = DelayFixed(
    lambda: float(world_pe_by_commodity().loc["PE_forestry_products"]),
    lambda: time_step(),
    lambda: 1,
    time_step,
    "_delayfixed_pe_forestry_demand_delayed",
)


@component.add(
    name="PROTRA_actual_full_load_hours",
    units="h/Year",
    subscripts=["REGIONS_9_I", "PROTRA_PP_CHP_HP_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"protra_to_allocated_in_twh": 2, "protra_capacity_stock": 2},
)
def protra_actual_full_load_hours():
    """
    PROTRA_TO_allocated_in_TWh[REGIONS_9_I,TO_elec,NRG_PROTRA_I]/ PROTRA_capacity_stock[REGIONS_9_I,TO_elec,NRG_PROTRA_I]/ UNIT_CONVERSION_HOURS_YEAR PROTRA_TO_allocated_in_TWh[REGIONS_9_I,TO_heat,NRG_PROTRA_I]/PROTRA_capacit y_stock[REGIONS_9_I,TO_heat,NRG_PROTRA_I]
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "PROTRA_PP_CHP_HP_I": _subscript_dict["PROTRA_PP_CHP_HP_I"],
        },
        ["REGIONS_9_I", "PROTRA_PP_CHP_HP_I"],
    )
    value.loc[:, _subscript_dict["PROTRA_CHP_PP_I"]] = zidz(
        protra_to_allocated_in_twh()
        .loc[:, "TO_elec", _subscript_dict["PROTRA_CHP_PP_I"]]
        .reset_coords(drop=True)
        .rename({"NRG_PROTRA_I": "PROTRA_CHP_PP_I"}),
        protra_capacity_stock()
        .loc[:, "TO_elec", _subscript_dict["PROTRA_CHP_PP_I"]]
        .reset_coords(drop=True)
        .rename({"NRG_PROTRA_I": "PROTRA_CHP_PP_I"}),
    ).values
    value.loc[:, _subscript_dict["PROTRA_HP_I"]] = zidz(
        protra_to_allocated_in_twh()
        .loc[:, "TO_heat", _subscript_dict["PROTRA_HP_I"]]
        .reset_coords(drop=True)
        .rename({"NRG_PROTRA_I": "PROTRA_HP_I"}),
        protra_capacity_stock()
        .loc[:, "TO_heat", _subscript_dict["PROTRA_HP_I"]]
        .reset_coords(drop=True)
        .rename({"NRG_PROTRA_I": "PROTRA_HP_I"}),
    ).values
    return value


@component.add(
    name="PROTRA_capacity_utilization_rate",
    units="1",
    subscripts=["REGIONS_9_I", "NRG_PROTRA_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_actual_full_load_hours": 1,
        "protra_max_full_load_hours_after_constraints": 1,
    },
)
def protra_capacity_utilization_rate():
    """
    Rate of utilization of existing PROTRA capacities after allocation.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
        },
        ["REGIONS_9_I", "NRG_PROTRA_I"],
    )
    value.loc[:, _subscript_dict["PROTRA_PP_CHP_HP_I"]] = zidz(
        protra_actual_full_load_hours(),
        protra_max_full_load_hours_after_constraints()
        .loc[:, _subscript_dict["PROTRA_PP_CHP_HP_I"]]
        .rename({"NRG_PROTRA_I": "PROTRA_PP_CHP_HP_I"}),
    ).values
    value.loc[:, _subscript_dict["PROTRA_NP_I"]] = 1
    return value


@component.add(
    name="PROTRA_elec_allocation",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_COMMODITIES_I", "NRG_PRO_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "max_to_from_existing_stock_by_protra_pp": 1,
        "protra_utilization_applied_priorities": 1,
        "remaining_to_to_be_allocated": 1,
    },
)
def protra_elec_allocation():
    """
    allocation of TO_elec to different Powerplant technologies (elec production from CHP has already been allocated in the previous step)
    """
    return allocate_available(
        max_to_from_existing_stock_by_protra_pp()
        .loc[:, "TO_elec", :]
        .reset_coords(drop=True),
        protra_utilization_applied_priorities(),
        remaining_to_to_be_allocated().loc[:, "TO_elec"].reset_coords(drop=True),
    ).expand_dims({"NRG_COMMODITIES_I": ["TO_elec"]}, 1)


@component.add(
    name="PROTRA_heat_allocation",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_COMMODITIES_I", "NRG_PRO_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "max_to_from_existing_stock_by_protra_hp_and_chp": 1,
        "protra_utilization_applied_priorities": 1,
        "to_by_commodity": 1,
    },
)
def protra_heat_allocation():
    """
    Allocation of (district-)heat demand to available genration technologies (PROTRA). (note: CHPs that treated as heat-demand driven: If they produce heat in the first allocation step, they will recieve highest priority in the second allocation for electricity).
    """
    return allocate_available(
        max_to_from_existing_stock_by_protra_hp_and_chp()
        .loc[:, "TO_heat", :]
        .reset_coords(drop=True),
        protra_utilization_applied_priorities(),
        to_by_commodity().loc[:, "TO_heat"].reset_coords(drop=True),
    ).expand_dims({"NRG_COMMODITIES_I": ["TO_heat"]}, 1)


@component.add(
    name="protra_max_full_load_hours_after_constraints",
    units="h/Year",
    subscripts=["REGIONS_9_I", "NRG_PROTRA_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_mat2nrg_uranium_availability": 1,
        "switch_energy": 3,
        "protra_max_full_load_hours": 5,
        "protra_max_full_load_hours_after_constraints_nuclear": 1,
        "protra_max_full_load_hours_curtailed": 1,
        "ratio_precipitation_evapotranspiration_by_year": 2,
        "switch_env2nrg_hydropower_production": 2,
    },
)
def protra_max_full_load_hours_after_constraints():
    """
    Full load hours of plants taking into account biophysical limitations (uranium availability, RES variability, percipitation-changes impact on hydropower production etc.)
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
        },
        ["REGIONS_9_I", "NRG_PROTRA_I"],
    )
    value.loc[:, ["PROTRA_PP_nuclear"]] = (
        if_then_else(
            np.logical_and(
                switch_mat2nrg_uranium_availability() == 0, switch_energy() == 0
            ),
            lambda: protra_max_full_load_hours()
            .loc[:, "PROTRA_PP_nuclear"]
            .reset_coords(drop=True),
            lambda: protra_max_full_load_hours_after_constraints_nuclear(),
        )
        .expand_dims({"NRG_PRO_I": ["PROTRA_PP_nuclear"]}, 1)
        .values
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, ["PROTRA_PP_nuclear"]] = False
    except_subs.loc[:, ["PROTRA_PP_hydropower_run_of_river"]] = False
    except_subs.loc[:, ["PROTRA_PP_hydropower_dammed"]] = False
    value.values[except_subs.values] = protra_max_full_load_hours_curtailed().values[
        except_subs.values
    ]
    value.loc[:, ["PROTRA_PP_hydropower_run_of_river"]] = (
        if_then_else(
            np.logical_or(
                switch_env2nrg_hydropower_production() == 0, switch_energy() == 0
            ),
            lambda: protra_max_full_load_hours()
            .loc[:, "PROTRA_PP_hydropower_run_of_river"]
            .reset_coords(drop=True),
            lambda: protra_max_full_load_hours()
            .loc[:, "PROTRA_PP_hydropower_run_of_river"]
            .reset_coords(drop=True)
            * ratio_precipitation_evapotranspiration_by_year()
            .loc[_subscript_dict["REGIONS_9_I"]]
            .rename({"REGIONS_36_I": "REGIONS_9_I"}),
        )
        .expand_dims({"NRG_PRO_I": ["PROTRA_PP_hydropower_run_of_river"]}, 1)
        .values
    )
    value.loc[:, ["PROTRA_PP_hydropower_dammed"]] = (
        if_then_else(
            np.logical_or(
                switch_env2nrg_hydropower_production() == 0, switch_energy() == 0
            ),
            lambda: protra_max_full_load_hours()
            .loc[:, "PROTRA_PP_hydropower_dammed"]
            .reset_coords(drop=True),
            lambda: protra_max_full_load_hours()
            .loc[:, "PROTRA_PP_hydropower_dammed"]
            .reset_coords(drop=True)
            * ratio_precipitation_evapotranspiration_by_year()
            .loc[_subscript_dict["REGIONS_9_I"]]
            .rename({"REGIONS_36_I": "REGIONS_9_I"}),
        )
        .expand_dims({"NRG_PRO_I": ["PROTRA_PP_hydropower_dammed"]}, 1)
        .values
    )
    return value


@component.add(
    name="protra_max_full_load_hours_after_constraints_nuclear",
    units="h/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "delayed_ts_uranium_extraction_rate": 1,
        "delayed_ts_protra_capacity_stock": 3,
        "protra_fuel_utilization_ratio": 1,
        "unit_conversion_tw_per_ej_per_year": 1,
    },
)
def protra_max_full_load_hours_after_constraints_nuclear():
    """
    For nuclear: maximum load hours from nuclear power plants given uranium extraction rate constraints; the eventual scarcity among regions is split proportionally to the nuclear capacity stock.
    """
    return zidz(
        delayed_ts_uranium_extraction_rate()
        * zidz(
            delayed_ts_protra_capacity_stock()
            .loc[:, "TO_elec", "PROTRA_PP_nuclear"]
            .reset_coords(drop=True),
            sum(
                delayed_ts_protra_capacity_stock()
                .loc[:, "TO_elec", "PROTRA_PP_nuclear"]
                .reset_coords(drop=True)
                .rename({"REGIONS_9_I": "REGIONS_9_I!"}),
                dim=["REGIONS_9_I!"],
            ),
        )
        * protra_fuel_utilization_ratio()
        .loc[_subscript_dict["REGIONS_9_I"], "PROTRA_PP_nuclear"]
        .reset_coords(drop=True)
        .rename({"REGIONS_36_I": "REGIONS_9_I"}),
        delayed_ts_protra_capacity_stock()
        .loc[:, "TO_elec", "PROTRA_PP_nuclear"]
        .reset_coords(drop=True)
        * unit_conversion_tw_per_ej_per_year(),
    )


@component.add(
    name="protra_max_full_load_hours_curtailed",
    units="h/Year",
    subscripts=["REGIONS_9_I", "NRG_PROTRA_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_nrg_variability_effects": 1,
        "protra_max_full_load_hours": 2,
        "variation_cf_curtailed_protra": 3,
    },
)
def protra_max_full_load_hours_curtailed():
    """
    Maximum full load hours taking into account curtailement due to energy variability (CEEP in EnergyPLAN).
    """
    return if_then_else(
        switch_nrg_variability_effects() == 1,
        lambda: protra_max_full_load_hours()
        * (
            1
            - if_then_else(
                variation_cf_curtailed_protra()
                .loc[:, "TO_elec", :]
                .reset_coords(drop=True)
                < 0,
                lambda: xr.DataArray(
                    0,
                    {
                        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                        "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
                    },
                    ["REGIONS_9_I", "NRG_PROTRA_I"],
                ),
                lambda: if_then_else(
                    variation_cf_curtailed_protra()
                    .loc[:, "TO_elec", :]
                    .reset_coords(drop=True)
                    > 1,
                    lambda: xr.DataArray(
                        1,
                        {
                            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                            "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
                        },
                        ["REGIONS_9_I", "NRG_PROTRA_I"],
                    ),
                    lambda: variation_cf_curtailed_protra()
                    .loc[:, "TO_elec", :]
                    .reset_coords(drop=True),
                ),
            )
        ),
        lambda: protra_max_full_load_hours(),
    )


@component.add(
    name="PROTRA_other_TO_allocations",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_TO_I", "PROTRA_NP_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={"remaining_to_to_be_allocated": 5},
)
def protra_other_to_allocations():
    """
    allocation of blending and No-Process processes (mainly for accounting processes)
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "NRG_TO_I": _subscript_dict["NRG_TO_I"],
            "PROTRA_NP_I": _subscript_dict["PROTRA_NP_I"],
        },
        ["REGIONS_9_I", "NRG_TO_I", "PROTRA_NP_I"],
    )
    value.loc[:, ["TO_gas"], ["PROTRA_blending_gas_fuels"]] = (
        remaining_to_to_be_allocated()
        .loc[:, "TO_gas"]
        .reset_coords(drop=True)
        .expand_dims({"NRG_COMMODITIES_I": ["TO_gas"]}, 1)
        .expand_dims({"NRG_PRO_I": ["PROTRA_blending_gas_fuels"]}, 2)
        .values
    )
    value.loc[:, ["TO_liquid"], ["PROTRA_blending_liquid_fuels"]] = (
        remaining_to_to_be_allocated()
        .loc[:, "TO_liquid"]
        .reset_coords(drop=True)
        .expand_dims({"NRG_COMMODITIES_I": ["TO_liquid"]}, 1)
        .expand_dims({"NRG_PRO_I": ["PROTRA_blending_liquid_fuels"]}, 2)
        .values
    )
    value.loc[:, ["TO_hydrogen"], ["PROTRA_no_process_TI_hydrogen"]] = (
        remaining_to_to_be_allocated()
        .loc[:, "TO_hydrogen"]
        .reset_coords(drop=True)
        .expand_dims({"NRG_COMMODITIES_I": ["TO_hydrogen"]}, 1)
        .expand_dims({"NRG_PRO_I": ["PROTRA_no_process_TI_hydrogen"]}, 2)
        .values
    )
    value.loc[:, ["TO_solid_bio"], ["PROTRA_no_process_TI_solid_bio"]] = (
        remaining_to_to_be_allocated()
        .loc[:, "TO_solid_bio"]
        .reset_coords(drop=True)
        .expand_dims({"NRG_COMMODITIES_I": ["TO_solid_bio"]}, 1)
        .expand_dims({"NRG_PRO_I": ["PROTRA_no_process_TI_solid_bio"]}, 2)
        .values
    )
    value.loc[:, ["TO_solid_fossil"], ["PROTRA_no_process_TI_solid_fossil"]] = (
        remaining_to_to_be_allocated()
        .loc[:, "TO_solid_fossil"]
        .reset_coords(drop=True)
        .expand_dims({"NRG_COMMODITIES_I": ["TO_solid_fossil"]}, 1)
        .expand_dims({"NRG_PRO_I": ["PROTRA_no_process_TI_solid_fossil"]}, 2)
        .values
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[
        :, ["TO_solid_fossil"], ["PROTRA_no_process_TI_solid_fossil"]
    ] = False
    except_subs.loc[:, ["TO_solid_bio"], ["PROTRA_no_process_TI_solid_bio"]] = False
    except_subs.loc[:, ["TO_hydrogen"], ["PROTRA_no_process_TI_hydrogen"]] = False
    except_subs.loc[:, ["TO_gas"], ["PROTRA_blending_gas_fuels"]] = False
    except_subs.loc[:, ["TO_liquid"], ["PROTRA_blending_liquid_fuels"]] = False
    value.values[except_subs.values] = 0
    return value


@component.add(
    name="PROTRA_TO_allocated",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_TO_I", "NRG_PROTRA_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "chp_production": 2,
        "protra_heat_allocation": 1,
        "protra_elec_allocation": 1,
        "protra_other_to_allocations": 1,
    },
)
def protra_to_allocated():
    """
    TO allocated to PROTRA technologies. Set together from stepwise-allocation approach (first heat, than elec)
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "NRG_TO_I": _subscript_dict["NRG_TO_I"],
            "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
        },
        ["REGIONS_9_I", "NRG_TO_I", "NRG_PROTRA_I"],
    )
    value.loc[:, ["TO_heat"], _subscript_dict["PROTRA_CHP_I"]] = (
        chp_production()
        .loc[:, "TO_heat", :]
        .reset_coords(drop=True)
        .expand_dims({"NRG_COMMODITIES_I": ["TO_heat"]}, 1)
        .values
    )
    value.loc[:, ["TO_elec"], _subscript_dict["PROTRA_CHP_I"]] = (
        chp_production()
        .loc[:, "TO_elec", :]
        .reset_coords(drop=True)
        .expand_dims({"NRG_COMMODITIES_I": ["TO_elec"]}, 1)
        .values
    )
    value.loc[:, ["TO_heat"], _subscript_dict["PROTRA_HP_I"]] = (
        protra_heat_allocation()
        .loc[:, "TO_heat", _subscript_dict["PROTRA_HP_I"]]
        .reset_coords(drop=True)
        .rename({"NRG_PRO_I": "PROTRA_HP_I"})
        .expand_dims({"NRG_COMMODITIES_I": ["TO_heat"]}, 1)
        .values
    )
    value.loc[:, ["TO_elec"], _subscript_dict["PROTRA_PP_I"]] = (
        protra_elec_allocation()
        .loc[:, "TO_elec", _subscript_dict["PROTRA_PP_I"]]
        .reset_coords(drop=True)
        .rename({"NRG_PRO_I": "PROTRA_PP_I"})
        .expand_dims({"NRG_COMMODITIES_I": ["TO_elec"]}, 1)
        .values
    )
    value.loc[
        :, :, _subscript_dict["PROTRA_NP_I"]
    ] = protra_other_to_allocations().values
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[:, :, _subscript_dict["PROTRA_CHP_I"]] = True
    except_subs.loc[:, ["TO_elec"], _subscript_dict["PROTRA_CHP_I"]] = False
    except_subs.loc[:, ["TO_heat"], _subscript_dict["PROTRA_CHP_I"]] = False
    value.values[except_subs.values] = 0
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[:, :, _subscript_dict["PROTRA_HP_I"]] = True
    except_subs.loc[:, ["TO_heat"], _subscript_dict["PROTRA_HP_I"]] = False
    value.values[except_subs.values] = 0
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[:, :, _subscript_dict["PROTRA_PP_I"]] = True
    except_subs.loc[:, ["TO_elec"], _subscript_dict["PROTRA_PP_I"]] = False
    value.values[except_subs.values] = 0
    return value


@component.add(
    name="PROTRA_utilization_applied_priorities",
    units="DMNL",
    subscripts=["REGIONS_9_I", "NRG_PRO_I", "pprofile"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "pwidth_protra_utilization_allocation_policy_priorities_sp": 1,
        "protra_utilization_priorities_endogenous": 1,
        "protra_utilization_allocation_priorities_sp": 1,
        "protra_utilization_priorities_policyweight_sp": 2,
    },
)
def protra_utilization_applied_priorities():
    """
    Applied allocation priorities for PROTRA energy transformation technology utilization, based on a mix of exogenous (policy) and endogeneous (OPEX, currently NOT ACTIVE) signals.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "NRG_PRO_I": _subscript_dict["NRG_PRO_I"],
            "pprofile": _subscript_dict["pprofile"],
        },
        ["REGIONS_9_I", "NRG_PRO_I", "pprofile"],
    )
    value.loc[:, :, ["ptype"]] = 3
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[:, :, ["ppriority"]] = True
    except_subs.loc[:, _subscript_dict["NRG_PROTRA_I"], ["ppriority"]] = False
    value.values[except_subs.values] = 0
    value.loc[
        :, :, ["pwidth"]
    ] = pwidth_protra_utilization_allocation_policy_priorities_sp()
    value.loc[:, :, ["pextra"]] = 0
    value.loc[:, _subscript_dict["NRG_PROTRA_I"], ["ppriority"]] = (
        (
            protra_utilization_allocation_priorities_sp()
            * protra_utilization_priorities_policyweight_sp()
            + protra_utilization_priorities_endogenous()
            * (1 - protra_utilization_priorities_policyweight_sp())
        )
        .expand_dims({"pprofile": ["ppriority"]}, 2)
        .values
    )
    return value


@component.add(
    name="PROTRA_utilization_priorities_endogenous",
    units="DMNL",
    subscripts=["REGIONS_9_I", "NRG_PROTRA_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "opex_by_protra_and_region_delayed_ts": 1,
        "min_opex_signal": 2,
        "max_opex_signal": 1,
    },
)
def protra_utilization_priorities_endogenous():
    """
    Endogeneous allocation priorities for technology utilization allocation, based on transformation efficiency, Fuel prices and CO2 prics (so far no O&M cost element included)
    """
    return 1 - zidz(
        opex_by_protra_and_region_delayed_ts() - min_opex_signal(),
        (max_opex_signal() - min_opex_signal()).expand_dims(
            {"NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"]}, 1
        ),
    )


@component.add(
    name="PWIDTH_PROTRA_UTILIZATION_ALLOCATION_POLICY_PRIORITIES_SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_pwidth_protra_utilization_allocation_policy_priorities_sp"
    },
)
def pwidth_protra_utilization_allocation_policy_priorities_sp():
    """
    One of the parameters of the Vensim ALLOCATE_AVAILABLE function used to specify the curves to be used for supply and demand. Note that the priorities and widths specified should all be of the same order of magnitude. For example, it does not make sense to have one priority be 20 and another 2e6 if width is 100.
    """
    return _ext_constant_pwidth_protra_utilization_allocation_policy_priorities_sp()


_ext_constant_pwidth_protra_utilization_allocation_policy_priorities_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "PWIDTH_PROTRA_UTILIZATION_ALLOCATION_POLICY_PRIORITIES_SP",
    {},
    _root,
    {},
    "_ext_constant_pwidth_protra_utilization_allocation_policy_priorities_sp",
)


@component.add(
    name="Remaining_TO_to_be_allocated",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_TO_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"to_by_commodity": 7, "chp_production": 2},
)
def remaining_to_to_be_allocated():
    """
    TO demand lesser the heat and elec produced from CHPs
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "NRG_TO_I": _subscript_dict["NRG_TO_I"],
        },
        ["REGIONS_9_I", "NRG_TO_I"],
    )
    value.loc[:, ["TO_elec"]] = (
        np.maximum(
            to_by_commodity().loc[:, "TO_elec"].reset_coords(drop=True)
            - sum(
                chp_production()
                .loc[:, "TO_elec", :]
                .reset_coords(drop=True)
                .rename({"PROTRA_CHP_I": "PROTRA_CHP_I!"}),
                dim=["PROTRA_CHP_I!"],
            ),
            0,
        )
        .expand_dims({"NRG_COMMODITIES_I": ["TO_elec"]}, 1)
        .values
    )
    value.loc[:, ["TO_gas"]] = (
        np.maximum(0, to_by_commodity().loc[:, "TO_gas"].reset_coords(drop=True))
        .expand_dims({"NRG_COMMODITIES_I": ["TO_gas"]}, 1)
        .values
    )
    value.loc[:, ["TO_heat"]] = (
        np.maximum(
            0,
            to_by_commodity().loc[:, "TO_heat"].reset_coords(drop=True)
            - sum(
                chp_production()
                .loc[:, "TO_heat", :]
                .reset_coords(drop=True)
                .rename({"PROTRA_CHP_I": "PROTRA_CHP_I!"}),
                dim=["PROTRA_CHP_I!"],
            ),
        )
        .expand_dims({"NRG_COMMODITIES_I": ["TO_heat"]}, 1)
        .values
    )
    value.loc[:, ["TO_hydrogen"]] = (
        np.maximum(0, to_by_commodity().loc[:, "TO_hydrogen"].reset_coords(drop=True))
        .expand_dims({"NRG_COMMODITIES_I": ["TO_hydrogen"]}, 1)
        .values
    )
    value.loc[:, ["TO_liquid"]] = (
        np.maximum(0, to_by_commodity().loc[:, "TO_liquid"].reset_coords(drop=True))
        .expand_dims({"NRG_COMMODITIES_I": ["TO_liquid"]}, 1)
        .values
    )
    value.loc[:, ["TO_solid_bio"]] = (
        np.maximum(0, to_by_commodity().loc[:, "TO_solid_bio"].reset_coords(drop=True))
        .expand_dims({"NRG_COMMODITIES_I": ["TO_solid_bio"]}, 1)
        .values
    )
    value.loc[:, ["TO_solid_fossil"]] = (
        np.maximum(
            0, to_by_commodity().loc[:, "TO_solid_fossil"].reset_coords(drop=True)
        )
        .expand_dims({"NRG_COMMODITIES_I": ["TO_solid_fossil"]}, 1)
        .values
    )
    return value


@component.add(
    name="SWITCH_ENV2NRG_HYDROPOWER_PRODUCTION",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_env2nrg_hydropower_production"},
)
def switch_env2nrg_hydropower_production():
    return _ext_constant_switch_env2nrg_hydropower_production()


_ext_constant_switch_env2nrg_hydropower_production = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_ENV2NRG_HYDROPOWER_PRODUCTION",
    {},
    _root,
    {},
    "_ext_constant_switch_env2nrg_hydropower_production",
)


@component.add(
    name="SWITCH_NRG_VARIABILITY_EFFECTS",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_nrg_variability_effects"},
)
def switch_nrg_variability_effects():
    """
    This switch can take two values: 0: the energy module does not see the effects variability in the generation of energy (RES would appear as fully dispatachable). 1: the energy module sees the effects of variability in utilization, capacity expansion, etc.
    """
    return _ext_constant_switch_nrg_variability_effects()


_ext_constant_switch_nrg_variability_effects = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_NRG_VARIABILITY_EFFECTS",
    {},
    _root,
    {},
    "_ext_constant_switch_nrg_variability_effects",
)


@component.add(
    name="TO_deficit",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_TO_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"to_by_commodity": 1, "aggregated_to_production_by_commodity": 1},
)
def to_deficit():
    """
    Variable to detect if there is transformation output (FE) scarcity by region and TO type.
    """
    return to_by_commodity() - aggregated_to_production_by_commodity()


@component.add(
    name="TO_deficit_relative",
    units="1",
    subscripts=["REGIONS_9_I", "NRG_TO_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"to_by_commodity": 1, "aggregated_to_production_by_commodity": 1},
)
def to_deficit_relative():
    """
    Variable to detect if there is transformation output (FE) scarcity by region and TO type.
    """
    return -1 + zidz(to_by_commodity(), aggregated_to_production_by_commodity())
