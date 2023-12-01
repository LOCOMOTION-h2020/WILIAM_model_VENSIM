"""
Module economy.firms.production
Translated using PySD version 3.10.0
"""


@component.add(
    name="change_economy_electricity_output",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "SECTORS_ELECTRICITY_PRODUCTION_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "economy_energy_transformation_output_aggregated": 1,
        "delayed_ts_economy_energy_physical_output": 1,
    },
)
def change_economy_electricity_output():
    return economy_energy_transformation_output_aggregated().loc[
        :, _subscript_dict["SECTORS_ELECTRICITY_PRODUCTION_I"]
    ].rename(
        {"SECTORS_TRANSFORMATION_ENERGY_I": "SECTORS_ELECTRICITY_PRODUCTION_I"}
    ) - delayed_ts_economy_energy_physical_output().loc[
        :, _subscript_dict["SECTORS_ELECTRICITY_PRODUCTION_I"]
    ].rename(
        {"SECTORS_TRANSFORMATION_ENERGY_I": "SECTORS_ELECTRICITY_PRODUCTION_I"}
    )


@component.add(
    name="change_technical_coefficients",
    units="DMNL/Year",
    subscripts=["REGIONS_36_I", "SECTORS_I", "SECTORS_MAP_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 2,
        "switch_economy": 2,
        "energy_intensities_growth_economic_module_classification": 1,
        "select_nrg2eco_a_matrix_energy_intensities": 1,
        "test_exo_energy_intensities_growth_cu_sector": 1,
        "switch_mat2eco_a_matrix_cu_intensity": 1,
    },
)
def change_technical_coefficients():
    """
    Change in technical coefficients.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_36_I": _subscript_dict["REGIONS_36_I"],
            "SECTORS_I": _subscript_dict["SECTORS_I"],
            "SECTORS_MAP_I": _subscript_dict["SECTORS_MAP_I"],
        },
        ["REGIONS_36_I", "SECTORS_I", "SECTORS_MAP_I"],
    )
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[_subscript_dict["REGIONS_35_I"], :, :] = True
    except_subs.loc[
        _subscript_dict["REGIONS_35_I"], _subscript_dict["SECTORS_FINAL_ENERGY_I"], :
    ] = False
    except_subs.loc[
        _subscript_dict["REGIONS_35_I"], ["MINING_AND_MANUFACTURING_COPPER"], :
    ] = False
    value.values[except_subs.values] = 0
    value.loc[
        _subscript_dict["REGIONS_35_I"], _subscript_dict["SECTORS_FINAL_ENERGY_I"], :
    ] = if_then_else(
        time() <= 2015,
        lambda: xr.DataArray(
            0,
            {
                "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                "SECTORS_FINAL_ENERGY_I": _subscript_dict["SECTORS_FINAL_ENERGY_I"],
                "SECTORS_MAP_I": _subscript_dict["SECTORS_MAP_I"],
            },
            ["REGIONS_35_I", "SECTORS_FINAL_ENERGY_I", "SECTORS_MAP_I"],
        ),
        lambda: if_then_else(
            np.logical_or(
                switch_economy() == 0, select_nrg2eco_a_matrix_energy_intensities() == 0
            ),
            lambda: xr.DataArray(
                0,
                {
                    "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                    "SECTORS_FINAL_ENERGY_I": _subscript_dict["SECTORS_FINAL_ENERGY_I"],
                    "SECTORS_MAP_I": _subscript_dict["SECTORS_MAP_I"],
                },
                ["REGIONS_35_I", "SECTORS_FINAL_ENERGY_I", "SECTORS_MAP_I"],
            ),
            lambda: energy_intensities_growth_economic_module_classification().rename(
                {"SECTORS_I": "SECTORS_MAP_I"}
            ),
        ),
    ).values
    value.loc[:, ["MINING_AND_MANUFACTURING_COPPER"], :] = if_then_else(
        time() <= 2015,
        lambda: 0,
        lambda: if_then_else(
            np.logical_or(
                switch_economy() == 0, switch_mat2eco_a_matrix_cu_intensity() == 0
            ),
            lambda: 0,
            lambda: test_exo_energy_intensities_growth_cu_sector(),
        ),
    )
    return value


@component.add(
    name="delayed_TS_economy_energy_physical_output",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "SECTORS_TRANSFORMATION_ENERGY_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_economy_energy_physical_output": 1},
    other_deps={
        "_delayfixed_delayed_ts_economy_energy_physical_output": {
            "initial": {
                "initial_economy_energy_transformation_output": 1,
                "time_step": 1,
            },
            "step": {"economy_energy_transformation_output_aggregated": 1},
        }
    },
)
def delayed_ts_economy_energy_physical_output():
    return _delayfixed_delayed_ts_economy_energy_physical_output()


_delayfixed_delayed_ts_economy_energy_physical_output = DelayFixed(
    lambda: economy_energy_transformation_output_aggregated(),
    lambda: time_step(),
    lambda: initial_economy_energy_transformation_output(),
    time_step,
    "_delayfixed_delayed_ts_economy_energy_physical_output",
)


@component.add(
    name="delayed_TS_output_real",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_output_real": 1},
    other_deps={
        "_delayfixed_delayed_ts_output_real": {
            "initial": {"base_output_real": 1, "time_step": 1},
            "step": {"time": 1, "base_output_real": 1, "output_real": 1},
        }
    },
)
def delayed_ts_output_real():
    """
    Delayed production in basic prices and real terms. IF THEN ELSE(Time<=2015,BASE OUTPUT REAL[REGIONS 35 I,SECTORS I],output real[REGIONS 35 I,SECTORS I]), 1 , BASE OUTPUT REAL [REGIONS 35 I,SECTORS I]
    """
    return _delayfixed_delayed_ts_output_real()


_delayfixed_delayed_ts_output_real = DelayFixed(
    lambda: if_then_else(
        time() <= 2015, lambda: base_output_real(), lambda: output_real()
    ),
    lambda: time_step(),
    lambda: base_output_real(),
    time_step,
    "_delayfixed_delayed_ts_output_real",
)


@component.add(
    name="delayed_TS_technical_coefficients_total",
    units="DMNL",
    subscripts=["REGIONS_35_I", "SECTORS_I", "SECTORS_MAP_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_technical_coefficients_total": 1},
    other_deps={
        "_delayfixed_delayed_ts_technical_coefficients_total": {
            "initial": {
                "initial_delayed_technical_coefficients_total": 1,
                "time_step": 1,
            },
            "step": {
                "time": 1,
                "initial_delayed_technical_coefficients_total": 1,
                "technical_coefficients_total": 1,
            },
        }
    },
)
def delayed_ts_technical_coefficients_total():
    """
    Delayed technical coeffcients: total
    """
    return _delayfixed_delayed_ts_technical_coefficients_total()


_delayfixed_delayed_ts_technical_coefficients_total = DelayFixed(
    lambda: if_then_else(
        time() <= 2015,
        lambda: initial_delayed_technical_coefficients_total(),
        lambda: technical_coefficients_total(),
    ),
    lambda: time_step(),
    lambda: initial_delayed_technical_coefficients_total(),
    time_step,
    "_delayfixed_delayed_ts_technical_coefficients_total",
)


@component.add(
    name="delayed_TS_total_intermediate_exports_real",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_total_intermediate_exports_real": 1},
    other_deps={
        "_delayfixed_delayed_ts_total_intermediate_exports_real": {
            "initial": {
                "sum_initial_total_intermediate_exports_real": 1,
                "time_step": 1,
            },
            "step": {
                "time": 1,
                "sum_initial_total_intermediate_exports_real": 1,
                "total_intermediate_exports_real": 1,
            },
        }
    },
)
def delayed_ts_total_intermediate_exports_real():
    """
    Delayed total intermediate exports.
    """
    return _delayfixed_delayed_ts_total_intermediate_exports_real()


_delayfixed_delayed_ts_total_intermediate_exports_real = DelayFixed(
    lambda: if_then_else(
        time() <= 2015,
        lambda: sum_initial_total_intermediate_exports_real(),
        lambda: total_intermediate_exports_real(),
    ),
    lambda: time_step(),
    lambda: sum_initial_total_intermediate_exports_real(),
    time_step,
    "_delayfixed_delayed_ts_total_intermediate_exports_real",
)


@component.add(
    name="delayed_TS_variation_energy_intensity_by_sector_and_FE",
    subscripts=["REGIONS_35_I", "SECTORS_I", "NRG_FE_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={
        "_delayfixed_delayed_ts_variation_energy_intensity_by_sector_and_fe": 1
    },
    other_deps={
        "_delayfixed_delayed_ts_variation_energy_intensity_by_sector_and_fe": {
            "initial": {"time_step": 1},
            "step": {"variation_energy_intensity_by_sector_and_fe": 1},
        }
    },
)
def delayed_ts_variation_energy_intensity_by_sector_and_fe():
    return _delayfixed_delayed_ts_variation_energy_intensity_by_sector_and_fe()


_delayfixed_delayed_ts_variation_energy_intensity_by_sector_and_fe = DelayFixed(
    lambda: variation_energy_intensity_by_sector_and_fe(),
    lambda: time_step(),
    lambda: xr.DataArray(
        0,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "SECTORS_I": _subscript_dict["SECTORS_I"],
            "NRG_FE_I": _subscript_dict["NRG_FE_I"],
        },
        ["REGIONS_35_I", "SECTORS_I", "NRG_FE_I"],
    ),
    time_step,
    "_delayfixed_delayed_ts_variation_energy_intensity_by_sector_and_fe",
)


@component.add(
    name="economy_electricity_physical_output_delayed_EU27",
    units="EJ/Year",
    subscripts=["REGIONS_EU27_I", "SECTORS_ELECTRICITY_PRODUCTION_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "delayed_ts_economy_energy_physical_output": 1,
        "share_eu27_sectors_transformation": 1,
    },
)
def economy_electricity_physical_output_delayed_eu27():
    return (
        delayed_ts_economy_energy_physical_output()
        .loc["EU27", _subscript_dict["SECTORS_ELECTRICITY_PRODUCTION_I"]]
        .reset_coords(drop=True)
        .rename({"SECTORS_TRANSFORMATION_ENERGY_I": "SECTORS_ELECTRICITY_PRODUCTION_I"})
        * share_eu27_sectors_transformation()
        .loc[:, _subscript_dict["SECTORS_ELECTRICITY_PRODUCTION_I"]]
        .rename({"SECTORS_TRANSFORMATION_ENERGY_I": "SECTORS_ELECTRICITY_PRODUCTION_I"})
        .transpose("SECTORS_ELECTRICITY_PRODUCTION_I", "REGIONS_EU27_I")
    ).transpose("REGIONS_EU27_I", "SECTORS_ELECTRICITY_PRODUCTION_I")


@component.add(
    name="economy_electricity_physical_output_EU27",
    units="EJ/Year",
    subscripts=["REGIONS_EU27_I", "SECTORS_ELECTRICITY_PRODUCTION_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "economy_electricity_physical_output_delayed_eu27": 1,
        "negative_change_electricity_output_eu27": 1,
        "positive_change_electricity_output_eu27": 1,
    },
)
def economy_electricity_physical_output_eu27():
    return (
        economy_electricity_physical_output_delayed_eu27()
        + negative_change_electricity_output_eu27()
        + positive_change_electricity_output_eu27()
    )


@component.add(
    name="economy_energy_transformation_matrix_input_aggregated_35R",
    subscripts=[
        "REGIONS_35_I",
        "SECTORS_TRANSFORMATION_ENERGY_I",
        "SECTORS_TRANSFORMATION_ENERGY_MAP_I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "economy_energy_transformation_matrix_input_aggregated": 2,
        "share_eu27_sectors_transformation": 1,
    },
)
def economy_energy_transformation_matrix_input_aggregated_35r():
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "SECTORS_TRANSFORMATION_ENERGY_I": _subscript_dict[
                "SECTORS_TRANSFORMATION_ENERGY_I"
            ],
            "SECTORS_TRANSFORMATION_ENERGY_MAP_I": _subscript_dict[
                "SECTORS_TRANSFORMATION_ENERGY_MAP_I"
            ],
        },
        [
            "REGIONS_35_I",
            "SECTORS_TRANSFORMATION_ENERGY_I",
            "SECTORS_TRANSFORMATION_ENERGY_MAP_I",
        ],
    )
    value.loc[_subscript_dict["REGIONS_8_I"], :, :] = (
        economy_energy_transformation_matrix_input_aggregated()
        .loc[_subscript_dict["REGIONS_8_I"], :, :]
        .rename({"REGIONS_9_I": "REGIONS_8_I"})
        .values
    )
    value.loc[_subscript_dict["REGIONS_EU27_I"], :, :] = (
        (
            economy_energy_transformation_matrix_input_aggregated()
            .loc["EU27", :, :]
            .reset_coords(drop=True)
            * share_eu27_sectors_transformation().transpose(
                "SECTORS_TRANSFORMATION_ENERGY_I", "REGIONS_EU27_I"
            )
        )
        .transpose(
            "REGIONS_EU27_I",
            "SECTORS_TRANSFORMATION_ENERGY_I",
            "SECTORS_TRANSFORMATION_ENERGY_MAP_I",
        )
        .values
    )
    return value


@component.add(
    name="electricity_gap_EU27",
    units="EJ/Year",
    subscripts=["REGIONS_EU27_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "final_energy_demand_by_fe_35r": 2,
        "unit_conversion_tj_ej": 2,
        "remaining_economy_energy_electricity_output_delayed_eu27": 2,
    },
)
def electricity_gap_eu27():
    return if_then_else(
        final_energy_demand_by_fe_35r()
        .loc[_subscript_dict["REGIONS_EU27_I"], "FE_elec"]
        .reset_coords(drop=True)
        .rename({"REGIONS_35_I": "REGIONS_EU27_I"})
        / unit_conversion_tj_ej()
        - sum(
            remaining_economy_energy_electricity_output_delayed_eu27().rename(
                {
                    "SECTORS_ELECTRICITY_PRODUCTION_I": "SECTORS_ELECTRICITY_PRODUCTION_I!"
                }
            ),
            dim=["SECTORS_ELECTRICITY_PRODUCTION_I!"],
        )
        > 0,
        lambda: final_energy_demand_by_fe_35r()
        .loc[_subscript_dict["REGIONS_EU27_I"], "FE_elec"]
        .reset_coords(drop=True)
        .rename({"REGIONS_35_I": "REGIONS_EU27_I"})
        / unit_conversion_tj_ej()
        - sum(
            remaining_economy_energy_electricity_output_delayed_eu27().rename(
                {
                    "SECTORS_ELECTRICITY_PRODUCTION_I": "SECTORS_ELECTRICITY_PRODUCTION_I!"
                }
            ),
            dim=["SECTORS_ELECTRICITY_PRODUCTION_I!"],
        ),
        lambda: xr.DataArray(
            0, {"REGIONS_EU27_I": _subscript_dict["REGIONS_EU27_I"]}, ["REGIONS_EU27_I"]
        ),
    )


@component.add(
    name="energy_intensities_growth_economic_module_classification",
    units="DMNL/Year",
    subscripts=["REGIONS_35_I", "SECTORS_FINAL_ENERGY_I", "SECTORS_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={"energy_intensity_growth": 6},
)
def energy_intensities_growth_economic_module_classification():
    """
    Change in energy intensities. COKE, SOLID BIOMASS are missing.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "SECTORS_FINAL_ENERGY_I": _subscript_dict["SECTORS_FINAL_ENERGY_I"],
            "SECTORS_I": _subscript_dict["SECTORS_I"],
        },
        ["REGIONS_35_I", "SECTORS_FINAL_ENERGY_I", "SECTORS_I"],
    )
    value.loc[:, ["REFINING"], :] = (
        energy_intensity_growth()
        .loc[:, :, "FE_liquid"]
        .reset_coords(drop=True)
        .expand_dims({"CLUSTER_REFINERY": _subscript_dict["CLUSTER_REFINERY"]}, 1)
        .values
    )
    value.loc[:, ["MINING_COAL"], :] = (
        energy_intensity_growth()
        .loc[:, :, "FE_solid_fossil"]
        .reset_coords(drop=True)
        .expand_dims({"CLUSTER_MINNING": ["MINING_COAL"]}, 1)
        .values
    )
    value.loc[:, ["COKE"], :] = 0
    value.loc[:, ["DISTRIBUTION_ELECTRICITY"], :] = (
        energy_intensity_growth()
        .loc[:, :, "FE_elec"]
        .reset_coords(drop=True)
        .expand_dims(
            {
                "CLUSTER_ELECTRICITY_TRANSPORT": _subscript_dict[
                    "CLUSTER_ELECTRICITY_TRANSPORT"
                ]
            },
            1,
        )
        .values
    )
    value.loc[:, ["DISTRIBUTION_GAS"], :] = (
        energy_intensity_growth()
        .loc[:, :, "FE_gas"]
        .reset_coords(drop=True)
        .expand_dims({"CLUSTER_OTHER_ENERGY_ACTIVITIES": ["DISTRIBUTION_GAS"]}, 1)
        .values
    )
    value.loc[:, ["STEAM_HOT_WATER"], :] = (
        energy_intensity_growth()
        .loc[:, :, "FE_heat"]
        .reset_coords(drop=True)
        .expand_dims({"CLUSTER_OTHER_ENERGY_ACTIVITIES": ["STEAM_HOT_WATER"]}, 1)
        .values
    )
    value.loc[:, ["HYDROGEN_PRODUCTION"], :] = (
        energy_intensity_growth()
        .loc[:, :, "FE_hydrogen"]
        .reset_coords(drop=True)
        .expand_dims({"CLUSTER_HYDROGEN": _subscript_dict["CLUSTER_HYDROGEN"]}, 1)
        .values
    )
    return value


@component.add(
    name="energy_intensity_growth",
    subscripts=["REGIONS_35_I", "SECTORS_I", "NRG_FE_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_nrg2eco_a_matrix_energy_intensities": 2,
        "baseline_energy_intensities_growth": 1,
        "delayed_ts_variation_energy_intensity_by_sector_and_fe": 1,
    },
)
def energy_intensity_growth():
    return if_then_else(
        select_nrg2eco_a_matrix_energy_intensities() == 0,
        lambda: xr.DataArray(
            0,
            {
                "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                "SECTORS_I": _subscript_dict["SECTORS_I"],
                "NRG_FE_I": _subscript_dict["NRG_FE_I"],
            },
            ["REGIONS_35_I", "SECTORS_I", "NRG_FE_I"],
        ),
        lambda: if_then_else(
            select_nrg2eco_a_matrix_energy_intensities() == 1,
            lambda: baseline_energy_intensities_growth(),
            lambda: delayed_ts_variation_energy_intensity_by_sector_and_fe(),
        ),
    )


@component.add(
    name="final_exports_real",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"final_demand_imports_in_basic_prices_real": 1},
)
def final_exports_real():
    """
    Final exports in basic prices and real terms. Esta es la única variable que cambia desde la simulación Trade_11 y que puede estar causando las pequeñas diferencias con el output, intermediates, etc. La anterior no lo sabemos porque no hay datos para la simulación Trade_11.
    """
    return sum(
        final_demand_imports_in_basic_prices_real().rename(
            {
                "REGIONS_35_MAP_I": "REGIONS_35_MAP_I!",
                "FINAL_DEMAND_I": "FINAL_DEMAND_I!",
            }
        ),
        dim=["REGIONS_35_MAP_I!", "FINAL_DEMAND_I!"],
    )


@component.add(
    name="identity_minus_technical_coefficients_domestic",
    units="DMNL",
    subscripts=["REGIONS_35_I", "SECTORS_I", "SECTORS_MAP_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"identity_matrix": 1, "technical_coefficients_domestic": 1},
)
def identity_minus_technical_coefficients_domestic():
    """
    Identity matrix minus matrix of technical coeffcients.
    """
    return (
        identity_matrix()
        - technical_coefficients_domestic().transpose(
            "SECTORS_I", "SECTORS_MAP_I", "REGIONS_35_I"
        )
    ).transpose("REGIONS_35_I", "SECTORS_I", "SECTORS_MAP_I")


@component.add(
    name="INITIAL_economy_energy_transformation_output",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "SECTORS_TRANSFORMATION_ENERGY_I"],
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_initial_economy_energy_transformation_output": 1},
    other_deps={
        "_initial_initial_economy_energy_transformation_output": {
            "initial": {"economy_energy_transformation_output_aggregated": 1},
            "step": {},
        }
    },
)
def initial_economy_energy_transformation_output():
    return _initial_initial_economy_energy_transformation_output()


_initial_initial_economy_energy_transformation_output = Initial(
    lambda: economy_energy_transformation_output_aggregated(),
    "_initial_initial_economy_energy_transformation_output",
)


@component.add(
    name="intermediate_imports_and_exports_real",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I", "REGIONS_35_MAP_I", "SECTORS_MAP_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"technical_coefficients_import": 1, "output_real": 1},
)
def intermediate_imports_and_exports_real():
    """
    Total intermediate exports and imports in real terms.
    """
    return technical_coefficients_import().rename(
        {"REGIONS_35_MAP_I": "REGIONS_35_I", "REGIONS_35_I": "REGIONS_35_MAP_I"}
    ) * output_real().rename(
        {"REGIONS_35_I": "REGIONS_35_MAP_I", "SECTORS_I": "SECTORS_MAP_I"}
    )


@component.add(
    name="intermediates_domestic_real",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I", "SECTORS_MAP_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"output_real": 1, "technical_coefficients_domestic": 1},
)
def intermediates_domestic_real():
    """
    Demand of domestic intermediate goods in basic prices and real terms.
    """
    return (
        output_real().rename({"SECTORS_I": "SECTORS_MAP_I"})
        * technical_coefficients_domestic().transpose(
            "REGIONS_35_I", "SECTORS_MAP_I", "SECTORS_I"
        )
    ).transpose("REGIONS_35_I", "SECTORS_I", "SECTORS_MAP_I")


@component.add(
    name="intermediates_total_real",
    units="Mdollars_2015",
    subscripts=["REGIONS_35_I", "SECTORS_I", "SECTORS_MAP_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"technical_coefficients_total": 1, "output_real": 1},
)
def intermediates_total_real():
    """
    Total demand intermediates
    """
    return technical_coefficients_total() * output_real().rename(
        {"SECTORS_I": "SECTORS_MAP_I"}
    )


@component.add(
    name="leontief_inverse",
    units="DMNL",
    subscripts=["REGIONS_35_I", "SECTORS_I", "SECTORS_MAP_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "identity_minus_technical_coefficients_domestic": 1,
        "year_compute_leontief_inverse": 1,
    },
)
def leontief_inverse():
    """
    Leontief invert matrix.
    """
    return invert_matrix(identity_minus_technical_coefficients_domestic())


@component.add(
    name="negative_change_electricity_output",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "SECTORS_ELECTRICITY_PRODUCTION_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"change_economy_electricity_output": 2},
)
def negative_change_electricity_output():
    return if_then_else(
        change_economy_electricity_output() < 0,
        lambda: change_economy_electricity_output(),
        lambda: xr.DataArray(
            0,
            {
                "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                "SECTORS_ELECTRICITY_PRODUCTION_I": _subscript_dict[
                    "SECTORS_ELECTRICITY_PRODUCTION_I"
                ],
            },
            ["REGIONS_9_I", "SECTORS_ELECTRICITY_PRODUCTION_I"],
        ),
    )


@component.add(
    name="negative_change_electricity_output_EU27",
    units="EJ/Year",
    subscripts=["REGIONS_EU27_I", "SECTORS_ELECTRICITY_PRODUCTION_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "share_eu27_sectors_transformation": 1,
        "negative_change_electricity_output": 1,
    },
)
def negative_change_electricity_output_eu27():
    return share_eu27_sectors_transformation().loc[
        :, _subscript_dict["SECTORS_ELECTRICITY_PRODUCTION_I"]
    ].rename(
        {"SECTORS_TRANSFORMATION_ENERGY_I": "SECTORS_ELECTRICITY_PRODUCTION_I"}
    ) * negative_change_electricity_output().loc[
        "EU27", :
    ].reset_coords(
        drop=True
    )


@component.add(
    name="output_real",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"leontief_inverse": 1, "total_demand_domestic_produced_goods_real": 1},
)
def output_real():
    """
    Total production by sector in basic prices and real terms.
    """
    return sum(
        leontief_inverse().rename({"SECTORS_MAP_I": "SECTORS_MAP_I!"})
        * total_demand_domestic_produced_goods_real().rename(
            {"SECTORS_I": "SECTORS_MAP_I!"}
        ),
        dim=["SECTORS_MAP_I!"],
    )


@component.add(
    name="output_real_growth",
    units="DMNL/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"output_real": 1, "delayed_ts_output_real": 2},
)
def output_real_growth():
    """
    Output real growth rate.
    """
    return zidz(output_real() - delayed_ts_output_real(), delayed_ts_output_real())


@component.add(
    name="positive_change_electricity_output",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "SECTORS_ELECTRICITY_PRODUCTION_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"change_economy_electricity_output": 2},
)
def positive_change_electricity_output():
    return if_then_else(
        change_economy_electricity_output() > 0,
        lambda: change_economy_electricity_output(),
        lambda: xr.DataArray(
            0,
            {
                "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                "SECTORS_ELECTRICITY_PRODUCTION_I": _subscript_dict[
                    "SECTORS_ELECTRICITY_PRODUCTION_I"
                ],
            },
            ["REGIONS_9_I", "SECTORS_ELECTRICITY_PRODUCTION_I"],
        ),
    )


@component.add(
    name="positive_change_electricity_output_EU27",
    units="EJ/Year",
    subscripts=["REGIONS_EU27_I", "SECTORS_ELECTRICITY_PRODUCTION_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "share_electricity_gap_eu27": 1,
        "positive_change_electricity_output": 1,
    },
)
def positive_change_electricity_output_eu27():
    return share_electricity_gap_eu27() * positive_change_electricity_output().loc[
        "EU27", :
    ].reset_coords(drop=True)


@component.add(
    name="remaining_economy_energy_electricity_output_delayed_EU27",
    units="EJ/Year",
    subscripts=["REGIONS_EU27_I", "SECTORS_ELECTRICITY_PRODUCTION_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "economy_electricity_physical_output_delayed_eu27": 1,
        "negative_change_electricity_output_eu27": 1,
    },
)
def remaining_economy_energy_electricity_output_delayed_eu27():
    return (
        economy_electricity_physical_output_delayed_eu27()
        + negative_change_electricity_output_eu27()
    )


@component.add(
    name="SELECT_NRG2ECO_A_MATRIX_ENERGY_INTENSITIES",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="Normal",
)
def select_nrg2eco_a_matrix_energy_intensities():
    """
    This select can take three values: 0: Final Energy input coefficient remains constants 1: Final Energy input coefficient linked to Energy Intensities exogenous 2: Final Energy input coefficient linked to Energy Intensities endogenous
    """
    return 0


@component.add(
    name="share_electricity_gap_EU27",
    units="DMNL",
    subscripts=["REGIONS_EU27_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"electricity_gap_eu27": 2},
)
def share_electricity_gap_eu27():
    return zidz(
        electricity_gap_eu27(),
        sum(
            electricity_gap_eu27().rename({"REGIONS_EU27_I": "REGIONS_EU27_MAP_I!"}),
            dim=["REGIONS_EU27_MAP_I!"],
        ),
    )


@component.add(
    name="Share_EU27_sectors_transformation",
    units="1",
    subscripts=["REGIONS_EU27_I", "SECTORS_TRANSFORMATION_ENERGY_I"],
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_share_eu27_sectors_transformation": 1},
    other_deps={
        "_initial_share_eu27_sectors_transformation": {
            "initial": {"output_real": 2},
            "step": {},
        }
    },
)
def share_eu27_sectors_transformation():
    return _initial_share_eu27_sectors_transformation()


_initial_share_eu27_sectors_transformation = Initial(
    lambda: zidz(
        output_real()
        .loc[
            _subscript_dict["REGIONS_EU27_I"],
            _subscript_dict["SECTORS_TRANSFORMATION_ENERGY_I"],
        ]
        .rename(
            {
                "REGIONS_35_I": "REGIONS_EU27_I",
                "SECTORS_I": "SECTORS_TRANSFORMATION_ENERGY_I",
            }
        ),
        sum(
            output_real()
            .loc[
                _subscript_dict["REGIONS_EU27_I"],
                _subscript_dict["SECTORS_TRANSFORMATION_ENERGY_I"],
            ]
            .rename(
                {
                    "REGIONS_35_I": "REGIONS_EU27_I!",
                    "SECTORS_I": "SECTORS_TRANSFORMATION_ENERGY_I",
                }
            ),
            dim=["REGIONS_EU27_I!"],
        ).expand_dims({"REGIONS_EU27_I": _subscript_dict["REGIONS_EU27_I"]}, 0),
    ),
    "_initial_share_eu27_sectors_transformation",
)


@component.add(
    name="SUM_INITIAL_TOTAL_INTERMEDIATE_EXPORTS_REAL",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_sum_initial_total_intermediate_exports_real"
    },
)
def sum_initial_total_intermediate_exports_real():
    return _ext_constant_sum_initial_total_intermediate_exports_real()


_ext_constant_sum_initial_total_intermediate_exports_real = ExtConstant(
    "model_parameters/economy/Production_ENDOGENOUS.xlsx",
    "Sum_initial_total_intermediate_",
    "SUM_INITIAL_TOTAL_INTERMEDIATE_EXPORTS_REAL",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
    "_ext_constant_sum_initial_total_intermediate_exports_real",
)


@component.add(
    name="SWITCH_MAT2ECO_A_MATRIX_Cu_INTENSITY",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="Normal",
)
def switch_mat2eco_a_matrix_cu_intensity():
    """
    This switch can take two values: 0: Copper input coefficient remains constants 1: Copper input coefficient growths for the chosen sectors
    """
    return 0


@component.add(
    name="technical_coefficients_domestic",
    units="DMNL",
    subscripts=["REGIONS_35_I", "SECTORS_I", "SECTORS_MAP_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "technical_coefficients_total": 1,
        "switch_eco_trade": 1,
        "import_shares_intermediates_constrained": 1,
        "base_import_shares_intermediates": 1,
    },
)
def technical_coefficients_domestic():
    """
    Technical coeffcients: domenstic. Domestic inputs required to proudce one unit of output (in real terms). IF_THEN_ELSE(SWITCH_A_MATRIX_Cu_INTENSITY=1,A_MATRIX_TOTAL_TEST[REGIONS_35_I,SECTORS_ I,SECTORS_MAP_I],IF_THEN_ELSE(SWITCH_A_MATRIX_ENERGY_INTENSITIES=1, A_MATRIX_TOTAL_TEST[REGIONS_35_I,SECTORS_I,SECTORS_MAP_I],A_MATRIX_TOTAL[RE GIONS_35_I,SECTORS_I,SECTORS_MAP_I])*(1-(IF_THEN_ELSE(SWITCH_PRODUCTION=0,B ASE_IMPORT_SHARES_INTERMEDIATES [REGIONS_35_I,SECTORS_I,SECTORS_MAP_I],import_shares_intermediates_constrai ned[REGIONS_35_I,SECTORS_I,SECTORS_MAP_I]))))
    """
    return technical_coefficients_total() * (
        1
        - if_then_else(
            switch_eco_trade() == 0,
            lambda: base_import_shares_intermediates(),
            lambda: import_shares_intermediates_constrained(),
        )
    )


@component.add(
    name="technical_coefficients_import",
    units="DMNL",
    subscripts=["REGIONS_35_MAP_I", "SECTORS_I", "REGIONS_35_I", "SECTORS_MAP_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_trade": 1,
        "base_import_shares_intermediates": 1,
        "import_shares_intermediates_constrained": 1,
        "import_shares_origin_intermediates": 1,
        "technical_coefficients_total": 1,
    },
)
def technical_coefficients_import():
    """
    Technical coefficients: imports. Imported inputs required to proudce one unit of output (in real terms).
    """
    return (
        if_then_else(
            switch_eco_trade() == 0,
            lambda: base_import_shares_intermediates(),
            lambda: import_shares_intermediates_constrained(),
        )
        * (
            technical_coefficients_total()
            * import_shares_origin_intermediates().transpose(
                "REGIONS_35_I", "SECTORS_I", "SECTORS_MAP_I", "REGIONS_35_MAP_I"
            )
        )
    ).transpose("REGIONS_35_MAP_I", "SECTORS_I", "REGIONS_35_I", "SECTORS_MAP_I")


@component.add(
    name="technical_coefficients_total",
    units="DMNL",
    subscripts=["REGIONS_35_I", "SECTORS_I", "SECTORS_MAP_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "delayed_ts_technical_coefficients_total": 1,
        "change_technical_coefficients": 1,
    },
)
def technical_coefficients_total():
    """
    Technical coeffcients: total
    """
    return delayed_ts_technical_coefficients_total() * (
        1
        + change_technical_coefficients()
        .loc[_subscript_dict["REGIONS_35_I"], :, :]
        .rename({"REGIONS_36_I": "REGIONS_35_I"})
    )


@component.add(
    name="TEST_EXO_energy_intensities_growth_Cu_sector",
    comp_type="Constant",
    comp_subtype="Normal",
)
def test_exo_energy_intensities_growth_cu_sector():
    return 0.0473


@component.add(
    name="total_demand_domestic_produced_goods_real",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "total_final_demand_domestic_produced_goods_basic_prices_real": 1,
        "delayed_ts_total_intermediate_exports_real": 1,
    },
)
def total_demand_domestic_produced_goods_real():
    """
    Total demand including exports of intermediate goods
    """
    return (
        total_final_demand_domestic_produced_goods_basic_prices_real()
        + delayed_ts_total_intermediate_exports_real()
    )


@component.add(
    name="total_final_demand_domestic_produced_goods_basic_prices_real",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "final_demand_domestic_in_basic_prices_real": 1,
        "final_exports_real": 1,
    },
)
def total_final_demand_domestic_produced_goods_basic_prices_real():
    """
    Total final demand of domestic produced goods in basic prices and real terms.
    """
    return (
        sum(
            final_demand_domestic_in_basic_prices_real().rename(
                {"FINAL_DEMAND_I": "FINAL_DEMAND_I!"}
            ),
            dim=["FINAL_DEMAND_I!"],
        )
        + final_exports_real()
    )


@component.add(
    name="total_intermediate_exports_real",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"intermediate_imports_and_exports_real": 1},
)
def total_intermediate_exports_real():
    """
    Total intermediate exports in real terms.
    """
    return sum(
        intermediate_imports_and_exports_real().rename(
            {"REGIONS_35_MAP_I": "REGIONS_35_MAP_I!", "SECTORS_MAP_I": "SECTORS_MAP_I!"}
        ),
        dim=["REGIONS_35_MAP_I!", "SECTORS_MAP_I!"],
    )


@component.add(
    name="total_intermediate_imports_real",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_MAP_I", "SECTORS_MAP_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"intermediate_imports_and_exports_real": 1},
)
def total_intermediate_imports_real():
    """
    Total intrmediate imports in real terms
    """
    return sum(
        intermediate_imports_and_exports_real().rename(
            {"REGIONS_35_I": "REGIONS_35_I!", "SECTORS_I": "SECTORS_I!"}
        ),
        dim=["REGIONS_35_I!", "SECTORS_I!"],
    )


@component.add(
    name="year_compute_leontief_inverse",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 2},
)
def year_compute_leontief_inverse():
    return if_then_else(time() == integer(time()), lambda: 62, lambda: 0)
