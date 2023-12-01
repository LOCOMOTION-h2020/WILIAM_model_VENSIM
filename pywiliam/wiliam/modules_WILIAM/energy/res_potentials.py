"""
Module energy.res_potentials
Translated using PySD version 3.10.0
"""


@component.add(
    name="actual_rooftop_use_solar_technologies",
    units="EJ/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_capacity_stock": 1,
        "protra_max_full_load_hours_after_constraints": 1,
        "share_capacity_stock_protra_pp_solar_pv_by_subtechnology": 1,
        "efficiences_pv_technology_panels": 2,
        "unit_conversion_tw_per_ej_per_year": 1,
    },
)
def actual_rooftop_use_solar_technologies():
    """
    Actual rooftop use calculated taking into account the actual share of solar PV subtechnologies.
    """
    return (
        protra_capacity_stock()
        .loc[:, "TO_elec", "PROTRA_PP_solar_urban_PV"]
        .reset_coords(drop=True)
        * protra_max_full_load_hours_after_constraints()
        .loc[:, "PROTRA_PP_solar_urban_PV"]
        .reset_coords(drop=True)
        * sum(
            (
                float(efficiences_pv_technology_panels().loc["C_Si_mono"])
                / efficiences_pv_technology_panels().rename(
                    {
                        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!"
                    }
                )
            )
            * share_capacity_stock_protra_pp_solar_pv_by_subtechnology()
            .loc[:, "PROTRA_PP_solar_urban_PV", :]
            .reset_coords(drop=True)
            .rename(
                {
                    "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!"
                }
            )
            .transpose("PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!", "REGIONS_9_I"),
            dim=["PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!"],
        )
        * unit_conversion_tw_per_ej_per_year()
    )


@component.add(
    name="EXOGENOUS_PROTRA_RES_POTENTIALS_SP",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "PROTRA_RES_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_exogenous_protra_res_potentials_sp"},
)
def exogenous_protra_res_potentials_sp():
    """
    scenario parameter for policy parameters
    """
    return _ext_constant_exogenous_protra_res_potentials_sp()


_ext_constant_exogenous_protra_res_potentials_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "EXOGENOUS_PROTRA_RES_POTENTIALS_SP*",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PROTRA_RES_I": _subscript_dict["PROTRA_RES_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PROTRA_RES_I": _subscript_dict["PROTRA_RES_I"],
    },
    "_ext_constant_exogenous_protra_res_potentials_sp",
)


@component.add(
    name="POTENTIAL_WIND_OFFSHORE_FIXED",
    units="EJ/Year",
    subscripts=["REGIONS_36_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_eroi_min_potential_wind_solar_sp": 8,
        "potential_wind_offshore_fixed_by_eroi_min": 8,
    },
)
def potential_wind_offshore_fixed():
    """
    Potential wind offshore fixed selected by the user depending on the EROI miniumun theshold.
    """
    return if_then_else(
        select_eroi_min_potential_wind_solar_sp() == 0,
        lambda: potential_wind_offshore_fixed_by_eroi_min()
        .loc[:, "EROI_MIN_0"]
        .reset_coords(drop=True),
        lambda: if_then_else(
            select_eroi_min_potential_wind_solar_sp() == 2,
            lambda: potential_wind_offshore_fixed_by_eroi_min()
            .loc[:, "EROI_MIN_2_1"]
            .reset_coords(drop=True),
            lambda: if_then_else(
                select_eroi_min_potential_wind_solar_sp() == 3,
                lambda: potential_wind_offshore_fixed_by_eroi_min()
                .loc[:, "EROI_MIN_3_1"]
                .reset_coords(drop=True),
                lambda: if_then_else(
                    select_eroi_min_potential_wind_solar_sp() == 5,
                    lambda: potential_wind_offshore_fixed_by_eroi_min()
                    .loc[:, "EROI_MIN_5_1"]
                    .reset_coords(drop=True),
                    lambda: if_then_else(
                        select_eroi_min_potential_wind_solar_sp() == 8,
                        lambda: potential_wind_offshore_fixed_by_eroi_min()
                        .loc[:, "EROI_MIN_8_1"]
                        .reset_coords(drop=True),
                        lambda: if_then_else(
                            select_eroi_min_potential_wind_solar_sp() == 10,
                            lambda: potential_wind_offshore_fixed_by_eroi_min()
                            .loc[:, "EROI_MIN_10_1"]
                            .reset_coords(drop=True),
                            lambda: if_then_else(
                                select_eroi_min_potential_wind_solar_sp() == 10,
                                lambda: potential_wind_offshore_fixed_by_eroi_min()
                                .loc[:, "EROI_MIN_12_1"]
                                .reset_coords(drop=True),
                                lambda: if_then_else(
                                    select_eroi_min_potential_wind_solar_sp() == 10,
                                    lambda: potential_wind_offshore_fixed_by_eroi_min()
                                    .loc[:, "EROI_MIN_15_1"]
                                    .reset_coords(drop=True),
                                    lambda: xr.DataArray(
                                        np.nan,
                                        {
                                            "REGIONS_36_I": _subscript_dict[
                                                "REGIONS_36_I"
                                            ]
                                        },
                                        ["REGIONS_36_I"],
                                    ),
                                ),
                            ),
                        ),
                    ),
                ),
            ),
        ),
    )


@component.add(
    name="POTENTIAL_WIND_OFFSHORE_FIXED_BY_EROI_MIN",
    units="EJ/Year",
    subscripts=["REGIONS_36_I", "EROI_MIN_POTENTIAL_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_potential_wind_offshore_fixed_by_eroi_min"
    },
)
def potential_wind_offshore_fixed_by_eroi_min():
    """
    Potential wind offshore fixed by region and EROI minimum threshold.
    """
    return _ext_constant_potential_wind_offshore_fixed_by_eroi_min()


_ext_constant_potential_wind_offshore_fixed_by_eroi_min = ExtConstant(
    "model_parameters/energy/energy-potentials.xlsx",
    "PROTRA",
    "POTENTIAL_WIND_OFFSHORE_FIXED_BY_EROI_MIN",
    {
        "REGIONS_36_I": _subscript_dict["REGIONS_36_I"],
        "EROI_MIN_POTENTIAL_I": _subscript_dict["EROI_MIN_POTENTIAL_I"],
    },
    _root,
    {
        "REGIONS_36_I": _subscript_dict["REGIONS_36_I"],
        "EROI_MIN_POTENTIAL_I": _subscript_dict["EROI_MIN_POTENTIAL_I"],
    },
    "_ext_constant_potential_wind_offshore_fixed_by_eroi_min",
)


@component.add(
    name="POTENTIAL_WIND_OFFSHORE_FLOATING",
    units="EJ/Year",
    subscripts=["REGIONS_36_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_eroi_min_potential_wind_solar_sp": 8,
        "potential_wind_offshore_floating_by_eroi_min": 8,
    },
)
def potential_wind_offshore_floating():
    """
    Potential wind offshore floating selected by the user depending on the EROI miniumun theshold.
    """
    return if_then_else(
        select_eroi_min_potential_wind_solar_sp() == 0,
        lambda: potential_wind_offshore_floating_by_eroi_min()
        .loc[:, "EROI_MIN_0"]
        .reset_coords(drop=True),
        lambda: if_then_else(
            select_eroi_min_potential_wind_solar_sp() == 2,
            lambda: potential_wind_offshore_floating_by_eroi_min()
            .loc[:, "EROI_MIN_2_1"]
            .reset_coords(drop=True),
            lambda: if_then_else(
                select_eroi_min_potential_wind_solar_sp() == 3,
                lambda: potential_wind_offshore_floating_by_eroi_min()
                .loc[:, "EROI_MIN_3_1"]
                .reset_coords(drop=True),
                lambda: if_then_else(
                    select_eroi_min_potential_wind_solar_sp() == 5,
                    lambda: potential_wind_offshore_floating_by_eroi_min()
                    .loc[:, "EROI_MIN_5_1"]
                    .reset_coords(drop=True),
                    lambda: if_then_else(
                        select_eroi_min_potential_wind_solar_sp() == 8,
                        lambda: potential_wind_offshore_floating_by_eroi_min()
                        .loc[:, "EROI_MIN_8_1"]
                        .reset_coords(drop=True),
                        lambda: if_then_else(
                            select_eroi_min_potential_wind_solar_sp() == 10,
                            lambda: potential_wind_offshore_floating_by_eroi_min()
                            .loc[:, "EROI_MIN_10_1"]
                            .reset_coords(drop=True),
                            lambda: if_then_else(
                                select_eroi_min_potential_wind_solar_sp() == 10,
                                lambda: potential_wind_offshore_floating_by_eroi_min()
                                .loc[:, "EROI_MIN_12_1"]
                                .reset_coords(drop=True),
                                lambda: if_then_else(
                                    select_eroi_min_potential_wind_solar_sp() == 10,
                                    lambda: potential_wind_offshore_floating_by_eroi_min()
                                    .loc[:, "EROI_MIN_15_1"]
                                    .reset_coords(drop=True),
                                    lambda: xr.DataArray(
                                        np.nan,
                                        {
                                            "REGIONS_36_I": _subscript_dict[
                                                "REGIONS_36_I"
                                            ]
                                        },
                                        ["REGIONS_36_I"],
                                    ),
                                ),
                            ),
                        ),
                    ),
                ),
            ),
        ),
    )


@component.add(
    name="POTENTIAL_WIND_OFFSHORE_FLOATING_BY_EROI_MIN",
    units="EJ/Year",
    subscripts=["REGIONS_36_I", "EROI_MIN_POTENTIAL_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_potential_wind_offshore_floating_by_eroi_min"
    },
)
def potential_wind_offshore_floating_by_eroi_min():
    """
    Potential wind offshore floating by region and EROI minimum threshold.
    """
    return _ext_constant_potential_wind_offshore_floating_by_eroi_min()


_ext_constant_potential_wind_offshore_floating_by_eroi_min = ExtConstant(
    "model_parameters/energy/energy-potentials.xlsx",
    "PROTRA",
    "POTENTIAL_WIND_OFFSHORE_FLOATING_BY_EROI_MIN",
    {
        "REGIONS_36_I": _subscript_dict["REGIONS_36_I"],
        "EROI_MIN_POTENTIAL_I": _subscript_dict["EROI_MIN_POTENTIAL_I"],
    },
    _root,
    {
        "REGIONS_36_I": _subscript_dict["REGIONS_36_I"],
        "EROI_MIN_POTENTIAL_I": _subscript_dict["EROI_MIN_POTENTIAL_I"],
    },
    "_ext_constant_potential_wind_offshore_floating_by_eroi_min",
)


@component.add(
    name="POTENTIAL_WIND_ONSHORE",
    units="EJ/Year",
    subscripts=["REGIONS_36_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_eroi_min_potential_wind_solar_sp": 8,
        "potential_wind_onshore_by_eroi_min": 8,
    },
)
def potential_wind_onshore():
    """
    Potential wind onshore selected by the user depending on the EROI miniumun theshold.
    """
    return if_then_else(
        select_eroi_min_potential_wind_solar_sp() == 0,
        lambda: potential_wind_onshore_by_eroi_min()
        .loc[:, "EROI_MIN_0"]
        .reset_coords(drop=True),
        lambda: if_then_else(
            select_eroi_min_potential_wind_solar_sp() == 2,
            lambda: potential_wind_onshore_by_eroi_min()
            .loc[:, "EROI_MIN_2_1"]
            .reset_coords(drop=True),
            lambda: if_then_else(
                select_eroi_min_potential_wind_solar_sp() == 3,
                lambda: potential_wind_onshore_by_eroi_min()
                .loc[:, "EROI_MIN_3_1"]
                .reset_coords(drop=True),
                lambda: if_then_else(
                    select_eroi_min_potential_wind_solar_sp() == 5,
                    lambda: potential_wind_onshore_by_eroi_min()
                    .loc[:, "EROI_MIN_5_1"]
                    .reset_coords(drop=True),
                    lambda: if_then_else(
                        select_eroi_min_potential_wind_solar_sp() == 8,
                        lambda: potential_wind_onshore_by_eroi_min()
                        .loc[:, "EROI_MIN_8_1"]
                        .reset_coords(drop=True),
                        lambda: if_then_else(
                            select_eroi_min_potential_wind_solar_sp() == 10,
                            lambda: potential_wind_onshore_by_eroi_min()
                            .loc[:, "EROI_MIN_10_1"]
                            .reset_coords(drop=True),
                            lambda: if_then_else(
                                select_eroi_min_potential_wind_solar_sp() == 10,
                                lambda: potential_wind_onshore_by_eroi_min()
                                .loc[:, "EROI_MIN_12_1"]
                                .reset_coords(drop=True),
                                lambda: if_then_else(
                                    select_eroi_min_potential_wind_solar_sp() == 10,
                                    lambda: potential_wind_onshore_by_eroi_min()
                                    .loc[:, "EROI_MIN_15_1"]
                                    .reset_coords(drop=True),
                                    lambda: xr.DataArray(
                                        np.nan,
                                        {
                                            "REGIONS_36_I": _subscript_dict[
                                                "REGIONS_36_I"
                                            ]
                                        },
                                        ["REGIONS_36_I"],
                                    ),
                                ),
                            ),
                        ),
                    ),
                ),
            ),
        ),
    )


@component.add(
    name="POTENTIAL_WIND_ONSHORE_BY_EROI_MIN",
    units="EJ/Year",
    subscripts=["REGIONS_36_I", "EROI_MIN_POTENTIAL_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_potential_wind_onshore_by_eroi_min"},
)
def potential_wind_onshore_by_eroi_min():
    """
    Potential wind onshore by region and EROI minimum threshold.
    """
    return _ext_constant_potential_wind_onshore_by_eroi_min()


_ext_constant_potential_wind_onshore_by_eroi_min = ExtConstant(
    "model_parameters/energy/energy-potentials.xlsx",
    "PROTRA",
    "POTENTIAL_WIND_ONSHORE_BY_EROI_MIN",
    {
        "REGIONS_36_I": _subscript_dict["REGIONS_36_I"],
        "EROI_MIN_POTENTIAL_I": _subscript_dict["EROI_MIN_POTENTIAL_I"],
    },
    _root,
    {
        "REGIONS_36_I": _subscript_dict["REGIONS_36_I"],
        "EROI_MIN_POTENTIAL_I": _subscript_dict["EROI_MIN_POTENTIAL_I"],
    },
    "_ext_constant_potential_wind_onshore_by_eroi_min",
)


@component.add(
    name="remaining_exogenous_potential_solar_PV_open_space",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_COMMODITIES_I", "NRG_PRO_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_protra_res_potentials_sp": 2,
        "unlimited_protra_res_parameter": 1,
        "unit_conversion_tw_per_ej_per_year": 1,
        "exogenous_protra_res_potentials_sp": 1,
        "switch_law2nrg_solarland": 1,
        "protra_max_full_load_hours": 1,
        "protra_capacity_stock": 1,
        "switch_energy": 1,
    },
)
def remaining_exogenous_potential_solar_pv_open_space():
    """
    Remaining exogenous potential solar PV open space after discounting the already capacity in place with the real operation CF. Solar PV availability coming from land-use enters the energy-capacity module directly through 'shortage_of_solar_land'. If SELECT_PROTRA_RES_POTENTIALS_SP=2 :OR: SWITCH_ENERGY=1 :OR: SWITCH_LAW2NRG_SOLARLAND=1 then the value is not taken in the allocate so '0' is writen ad hoc.
    """
    return (
        if_then_else(
            select_protra_res_potentials_sp() == 0,
            lambda: xr.DataArray(
                unlimited_protra_res_parameter(),
                {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
                ["REGIONS_9_I"],
            ),
            lambda: if_then_else(
                np.logical_or(
                    select_protra_res_potentials_sp() == 1,
                    np.logical_or(
                        switch_energy() == 0, switch_law2nrg_solarland() == 0
                    ),
                ),
                lambda: exogenous_protra_res_potentials_sp()
                .loc[:, "PROTRA_PP_solar_open_space_PV"]
                .reset_coords(drop=True)
                - protra_capacity_stock()
                .loc[:, "TO_elec", "PROTRA_PP_solar_open_space_PV"]
                .reset_coords(drop=True)
                * protra_max_full_load_hours()
                .loc[:, "PROTRA_PP_solar_open_space_PV"]
                .reset_coords(drop=True)
                * unit_conversion_tw_per_ej_per_year(),
                lambda: xr.DataArray(
                    0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
                ),
            ),
        )
        .expand_dims({"NRG_COMMODITIES_I": ["TO_elec"]}, 1)
        .expand_dims({"NRG_PRO_I": ["PROTRA_PP_solar_open_space_PV"]}, 2)
    )


@component.add(
    name="remaining_potential_PROTRA_RES_CHP_HP",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_COMMODITIES_I", "PROTRA_RES_CHP_HP_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_protra_res_potentials_sp": 1,
        "unlimited_protra_res_parameter": 1,
        "exogenous_protra_res_potentials_sp": 1,
        "protra_capacity_stock": 1,
        "protra_max_full_load_hours": 1,
        "unit_conversion_tw_per_ej_per_year": 1,
    },
)
def remaining_potential_protra_res_chp_hp():
    """
    Remaining potential of RES for heat generation (including CHPs) in EJ/year.
    """
    return if_then_else(
        select_protra_res_potentials_sp() == 0,
        lambda: xr.DataArray(
            unlimited_protra_res_parameter(),
            {
                "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                "PROTRA_RES_CHP_HP_I": _subscript_dict["PROTRA_RES_CHP_HP_I"],
            },
            ["REGIONS_9_I", "PROTRA_RES_CHP_HP_I"],
        ),
        lambda: exogenous_protra_res_potentials_sp()
        .loc[:, _subscript_dict["PROTRA_RES_CHP_HP_I"]]
        .rename({"PROTRA_RES_I": "PROTRA_RES_CHP_HP_I"})
        - protra_capacity_stock()
        .loc[:, "TO_heat", _subscript_dict["PROTRA_RES_CHP_HP_I"]]
        .reset_coords(drop=True)
        .rename({"NRG_PROTRA_I": "PROTRA_RES_CHP_HP_I"})
        * protra_max_full_load_hours()
        .loc[:, _subscript_dict["PROTRA_RES_CHP_HP_I"]]
        .rename({"NRG_PROTRA_I": "PROTRA_RES_CHP_HP_I"})
        * unit_conversion_tw_per_ej_per_year(),
    ).expand_dims({"NRG_COMMODITIES_I": ["TO_heat"]}, 1)


@component.add(
    name="remaining_potential_PROTRA_RES_PP",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_COMMODITIES_I", "PROTRA_RES_PP_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "remaining_potential_wind": 1,
        "remaining_exogenous_potential_solar_pv_open_space": 1,
        "exogenous_protra_res_potentials_sp": 2,
        "protra_capacity_stock": 2,
        "protra_max_full_load_hours": 2,
        "unit_conversion_tw_per_ej_per_year": 2,
        "remaining_solar_pv_rooftop_potential": 1,
        "select_availability_unmature_energy_technologies_sp": 2,
    },
)
def remaining_potential_protra_res_pp():
    """
    Remaining potential of RES for electricity generation in EJ/year. For solar PV it is the exogenous potential.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "NRG_COMMODITIES_I": _subscript_dict["NRG_COMMODITIES_I"],
            "PROTRA_RES_PP_I": _subscript_dict["PROTRA_RES_PP_I"],
        },
        ["REGIONS_9_I", "NRG_COMMODITIES_I", "PROTRA_RES_PP_I"],
    )
    value.loc[:, ["TO_elec"], _subscript_dict["PROTRA_WIND_I"]] = (
        remaining_potential_wind()
        .loc[:, "TO_elec", :]
        .reset_coords(drop=True)
        .expand_dims({"NRG_COMMODITIES_I": ["TO_elec"]}, 1)
        .values
    )
    value.loc[:, ["TO_elec"], ["PROTRA_PP_solar_open_space_PV"]] = (
        remaining_exogenous_potential_solar_pv_open_space()
        .loc[:, "TO_elec", "PROTRA_PP_solar_open_space_PV"]
        .reset_coords(drop=True)
        .expand_dims({"NRG_COMMODITIES_I": ["TO_elec"]}, 1)
        .expand_dims({"NRG_PRO_I": ["PROTRA_PP_solar_open_space_PV"]}, 2)
        .values
    )
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[:, ["TO_elec"], :] = True
    except_subs.loc[:, ["TO_elec"], ["PROTRA_PP_solar_open_space_PV"]] = False
    except_subs.loc[:, ["TO_elec"], _subscript_dict["PROTRA_WIND_I"]] = False
    except_subs.loc[:, ["TO_elec"], ["PROTRA_PP_solar_urban_PV"]] = False
    except_subs.loc[:, ["TO_elec"], ["PROTRA_PP_oceanic"]] = False
    value.values[except_subs.values] = (
        (
            exogenous_protra_res_potentials_sp()
            .loc[:, _subscript_dict["PROTRA_RES_PP_I"]]
            .rename({"PROTRA_RES_I": "PROTRA_RES_PP_I"})
            - protra_capacity_stock()
            .loc[:, "TO_elec", _subscript_dict["PROTRA_RES_PP_I"]]
            .reset_coords(drop=True)
            .rename({"NRG_PROTRA_I": "PROTRA_RES_PP_I"})
            * protra_max_full_load_hours()
            .loc[:, _subscript_dict["PROTRA_RES_PP_I"]]
            .rename({"NRG_PROTRA_I": "PROTRA_RES_PP_I"})
            * unit_conversion_tw_per_ej_per_year()
        )
        .expand_dims({"NRG_COMMODITIES_I": ["TO_elec"]}, 1)
        .values[except_subs.loc[:, ["TO_elec"], :].values]
    )
    value.loc[:, ["TO_elec"], ["PROTRA_PP_solar_urban_PV"]] = (
        remaining_solar_pv_rooftop_potential()
        .expand_dims({"NRG_COMMODITIES_I": ["TO_elec"]}, 1)
        .expand_dims({"NRG_PRO_I": ["PROTRA_PP_solar_urban_PV"]}, 2)
        .values
    )
    value.loc[:, ["TO_elec"], ["PROTRA_PP_oceanic"]] = (
        if_then_else(
            np.logical_or(
                select_availability_unmature_energy_technologies_sp() == 1,
                select_availability_unmature_energy_technologies_sp() == 5,
            ),
            lambda: exogenous_protra_res_potentials_sp()
            .loc[:, "PROTRA_PP_oceanic"]
            .reset_coords(drop=True)
            - protra_capacity_stock()
            .loc[:, "TO_elec", "PROTRA_PP_oceanic"]
            .reset_coords(drop=True)
            * protra_max_full_load_hours()
            .loc[:, "PROTRA_PP_oceanic"]
            .reset_coords(drop=True)
            * unit_conversion_tw_per_ej_per_year(),
            lambda: xr.DataArray(
                0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
            ),
        )
        .expand_dims({"NRG_COMMODITIES_I": ["TO_elec"]}, 1)
        .expand_dims({"NRG_PRO_I": ["PROTRA_PP_oceanic"]}, 2)
        .values
    )
    return value


@component.add(
    name="remaining_potential_wind",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_COMMODITIES_I", "PROTRA_WIND_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_protra_res_potentials_sp": 4,
        "unlimited_protra_res_parameter": 2,
        "unit_conversion_tw_per_ej_per_year": 5,
        "exogenous_protra_res_potentials_sp": 2,
        "protra_max_full_load_hours": 5,
        "potential_wind_onshore": 1,
        "protra_capacity_stock": 5,
        "potential_wind_offshore_fixed": 2,
        "potential_wind_offshore_floating": 1,
        "select_availability_unmature_energy_technologies_sp": 2,
    },
)
def remaining_potential_wind():
    """
    Remaining wind potential ( onshore and offshore (fixed + floating) ) after discounting the already capacity in place with the real operation CF.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "NRG_COMMODITIES_I": _subscript_dict["NRG_COMMODITIES_I"],
            "PROTRA_WIND_I": _subscript_dict["PROTRA_WIND_I"],
        },
        ["REGIONS_9_I", "NRG_COMMODITIES_I", "PROTRA_WIND_I"],
    )
    value.loc[:, ["TO_elec"], ["PROTRA_PP_wind_onshore"]] = (
        if_then_else(
            select_protra_res_potentials_sp() == 0,
            lambda: xr.DataArray(
                unlimited_protra_res_parameter(),
                {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
                ["REGIONS_9_I"],
            ),
            lambda: if_then_else(
                select_protra_res_potentials_sp() == 1,
                lambda: exogenous_protra_res_potentials_sp()
                .loc[:, "PROTRA_PP_wind_onshore"]
                .reset_coords(drop=True)
                - protra_capacity_stock()
                .loc[:, "TO_elec", "PROTRA_PP_wind_onshore"]
                .reset_coords(drop=True)
                * protra_max_full_load_hours()
                .loc[:, "PROTRA_PP_wind_onshore"]
                .reset_coords(drop=True)
                * unit_conversion_tw_per_ej_per_year(),
                lambda: potential_wind_onshore()
                .loc[_subscript_dict["REGIONS_9_I"]]
                .rename({"REGIONS_36_I": "REGIONS_9_I"})
                - protra_capacity_stock()
                .loc[:, "TO_elec", "PROTRA_PP_wind_onshore"]
                .reset_coords(drop=True)
                * protra_max_full_load_hours()
                .loc[:, "PROTRA_PP_wind_onshore"]
                .reset_coords(drop=True)
                * unit_conversion_tw_per_ej_per_year(),
            ),
        )
        .expand_dims({"NRG_COMMODITIES_I": ["TO_elec"]}, 1)
        .expand_dims({"NRG_PRO_I": ["PROTRA_PP_wind_onshore"]}, 2)
        .values
    )
    value.loc[:, ["TO_elec"], ["PROTRA_PP_wind_offshore"]] = (
        if_then_else(
            select_protra_res_potentials_sp() == 0,
            lambda: xr.DataArray(
                unlimited_protra_res_parameter(),
                {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
                ["REGIONS_9_I"],
            ),
            lambda: if_then_else(
                select_protra_res_potentials_sp() == 1,
                lambda: exogenous_protra_res_potentials_sp()
                .loc[:, "PROTRA_PP_wind_offshore"]
                .reset_coords(drop=True)
                - protra_capacity_stock()
                .loc[:, "TO_elec", "PROTRA_PP_wind_offshore"]
                .reset_coords(drop=True)
                * protra_max_full_load_hours()
                .loc[:, "PROTRA_PP_wind_offshore"]
                .reset_coords(drop=True)
                * unit_conversion_tw_per_ej_per_year(),
                lambda: if_then_else(
                    np.logical_or(
                        select_availability_unmature_energy_technologies_sp() == 1,
                        select_availability_unmature_energy_technologies_sp() == 3,
                    ),
                    lambda: (
                        potential_wind_offshore_fixed()
                        .loc[_subscript_dict["REGIONS_9_I"]]
                        .rename({"REGIONS_36_I": "REGIONS_9_I"})
                        + potential_wind_offshore_floating()
                        .loc[_subscript_dict["REGIONS_9_I"]]
                        .rename({"REGIONS_36_I": "REGIONS_9_I"})
                    )
                    - protra_capacity_stock()
                    .loc[:, "TO_elec", "PROTRA_PP_wind_offshore"]
                    .reset_coords(drop=True)
                    * protra_max_full_load_hours()
                    .loc[:, "PROTRA_PP_wind_offshore"]
                    .reset_coords(drop=True)
                    * unit_conversion_tw_per_ej_per_year(),
                    lambda: potential_wind_offshore_fixed()
                    .loc[_subscript_dict["REGIONS_9_I"]]
                    .rename({"REGIONS_36_I": "REGIONS_9_I"})
                    - protra_capacity_stock()
                    .loc[:, "TO_elec", "PROTRA_PP_wind_offshore"]
                    .reset_coords(drop=True)
                    * protra_max_full_load_hours()
                    .loc[:, "PROTRA_PP_wind_offshore"]
                    .reset_coords(drop=True)
                    * unit_conversion_tw_per_ej_per_year(),
                ),
            ),
        )
        .expand_dims({"NRG_COMMODITIES_I": ["TO_elec"]}, 1)
        .expand_dims({"NRG_PRO_I": ["PROTRA_PP_wind_offshore"]}, 2)
        .values
    )
    return value


@component.add(
    name="remaining_solar_PV_rooftop_potential",
    units="EJ/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_protra_res_potentials_sp": 1,
        "unlimited_protra_res_parameter": 1,
        "actual_rooftop_use_solar_technologies": 1,
        "solar_pv_rooftop_potential_c_si_mono": 1,
    },
)
def remaining_solar_pv_rooftop_potential():
    """
    Remaining solar PV rooftop potential recalculated taking into account the actual share of solar PV subtechnologies.
    """
    return if_then_else(
        select_protra_res_potentials_sp() == 0,
        lambda: xr.DataArray(
            unlimited_protra_res_parameter(),
            {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
            ["REGIONS_9_I"],
        ),
        lambda: solar_pv_rooftop_potential_c_si_mono()
        - actual_rooftop_use_solar_technologies(),
    )


@component.add(
    name="remaining_solar_thermal_rooftop_potential",
    units="EJ/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_protra_res_potentials_sp": 1,
        "unlimited_protra_res_parameter": 1,
        "actual_rooftop_use_solar_technologies": 1,
        "solar_thermal_rooftop_potential": 1,
    },
)
def remaining_solar_thermal_rooftop_potential():
    """
    Remaining solar thermal rooftop potential.
    """
    return if_then_else(
        select_protra_res_potentials_sp() == 0,
        lambda: xr.DataArray(
            unlimited_protra_res_parameter(),
            {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
            ["REGIONS_9_I"],
        ),
        lambda: solar_thermal_rooftop_potential()
        - actual_rooftop_use_solar_technologies(),
    )


@component.add(
    name="SELECT_AVAILABILITY_UNMATURE_ENERGY_TECHNOLOGIES_SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_select_availability_unmature_energy_technologies_sp"
    },
)
def select_availability_unmature_energy_technologies_sp():
    """
    Hypothesis to select the availability at large commercial scale in the future of today unmature/unproven energy technologies (H2, CCS, wind offshore floating, marine). It is possible to select individually which technology might be available, as well as none and all.
    """
    return _ext_constant_select_availability_unmature_energy_technologies_sp()


_ext_constant_select_availability_unmature_energy_technologies_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "SELECT_AVAILABILITY_UNMATURE_ENERGY_TECHNOLOGIES_SP",
    {},
    _root,
    {},
    "_ext_constant_select_availability_unmature_energy_technologies_sp",
)


@component.add(
    name="SELECT_PROTRA_RES_POTENTIALS_SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_select_protra_res_potentials_sp"},
)
def select_protra_res_potentials_sp():
    """
    =0: Unlimited RES potentials =1: Exogenous potentials (set here as scenario parameter hypothesis). =2: Endogenous for solar PV & CSP (depending on selected EROImin and link with land-use) and wind onshore & offshore (depending on selected EROImin) -see below PROTRA_RES_I marked in yellow-, exogenous for the remaining technologies
    """
    return _ext_constant_select_protra_res_potentials_sp()


_ext_constant_select_protra_res_potentials_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "SELECT_PROTRA_RES_POTENTIALS_SP",
    {},
    _root,
    {},
    "_ext_constant_select_protra_res_potentials_sp",
)


@component.add(
    name="SELECT_ROOFTOP_USE_SOLAR_TECHNOLOGIES_SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_select_rooftop_use_solar_technologies_sp"
    },
)
def select_rooftop_use_solar_technologies_sp():
    """
    User select option for the use of rooftop of solar PV vs thermal.
    """
    return _ext_constant_select_rooftop_use_solar_technologies_sp()


_ext_constant_select_rooftop_use_solar_technologies_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "SELECT_ROOFTOP_USE_SOLAR_TECHNOLOGIES_SP",
    {},
    _root,
    {},
    "_ext_constant_select_rooftop_use_solar_technologies_sp",
)


@component.add(
    name="SOLAR_PV_ROOFTOP_POTENTIAL_C_Si_MONO",
    units="EJ/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_rooftop_use_solar_technologies_sp": 5,
        "efficiences_pv_technology_panels": 6,
        "solar_pv_rooftop_potential_c_si_mono_0pv_100th_sp": 1,
        "solar_pv_rooftop_potential_c_si_mono_50pv_50th_sp": 1,
        "solar_pv_rooftop_potential_c_si_mono_100pv_0th_sp": 1,
        "solar_pv_rooftop_potential_c_si_mono_user_defined_sp": 1,
        "solar_pv_rooftop_potential_c_si_mono_25pv_75th_sp": 1,
        "solar_pv_rooftop_potential_c_si_mono_75pv_25th_sp": 1,
        "growth_land_uses_vs_2015": 1,
        "switch_energy": 1,
        "unit_conversion_pj_ej": 1,
    },
)
def solar_pv_rooftop_potential_c_si_mono():
    """
    Solar PV rooftop potential Si-monocrystaline assuming a fixed share of roofs dedicated to solar PV and thermal. Including linear variation with urban land surface.
    """
    return (
        if_then_else(
            select_rooftop_use_solar_technologies_sp() == 0,
            lambda: solar_pv_rooftop_potential_c_si_mono_0pv_100th_sp(
                float(efficiences_pv_technology_panels().loc["C_Si_mono"])
            )
            .loc[_subscript_dict["REGIONS_9_I"]]
            .rename({"REGIONS_36_I": "REGIONS_9_I"}),
            lambda: if_then_else(
                select_rooftop_use_solar_technologies_sp() == 1,
                lambda: solar_pv_rooftop_potential_c_si_mono_25pv_75th_sp(
                    float(efficiences_pv_technology_panels().loc["C_Si_mono"])
                )
                .loc[_subscript_dict["REGIONS_9_I"]]
                .rename({"REGIONS_36_I": "REGIONS_9_I"}),
                lambda: if_then_else(
                    select_rooftop_use_solar_technologies_sp() == 2,
                    lambda: solar_pv_rooftop_potential_c_si_mono_50pv_50th_sp(
                        float(efficiences_pv_technology_panels().loc["C_Si_mono"])
                    )
                    .loc[_subscript_dict["REGIONS_9_I"]]
                    .rename({"REGIONS_36_I": "REGIONS_9_I"}),
                    lambda: if_then_else(
                        select_rooftop_use_solar_technologies_sp() == 3,
                        lambda: solar_pv_rooftop_potential_c_si_mono_75pv_25th_sp(
                            float(efficiences_pv_technology_panels().loc["C_Si_mono"])
                        )
                        .loc[_subscript_dict["REGIONS_9_I"]]
                        .rename({"REGIONS_36_I": "REGIONS_9_I"}),
                        lambda: if_then_else(
                            select_rooftop_use_solar_technologies_sp() == 4,
                            lambda: solar_pv_rooftop_potential_c_si_mono_100pv_0th_sp(
                                float(
                                    efficiences_pv_technology_panels().loc["C_Si_mono"]
                                )
                            )
                            .loc[_subscript_dict["REGIONS_9_I"]]
                            .rename({"REGIONS_36_I": "REGIONS_9_I"}),
                            lambda: solar_pv_rooftop_potential_c_si_mono_user_defined_sp(
                                float(
                                    efficiences_pv_technology_panels().loc["C_Si_mono"]
                                )
                            )
                            .loc[_subscript_dict["REGIONS_9_I"]]
                            .rename({"REGIONS_36_I": "REGIONS_9_I"}),
                        ),
                    ),
                ),
            ),
        )
        * if_then_else(
            switch_energy() == 0,
            lambda: xr.DataArray(
                1, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
            ),
            lambda: growth_land_uses_vs_2015()
            .loc[:, "URBAN_LAND"]
            .reset_coords(drop=True),
        )
        / unit_conversion_pj_ej()
    )


@component.add(
    name="SOLAR_PV_ROOFTOP_POTENTIAL_C_Si_MONO_0PV_100TH_SP",
    units="PJ/Year",
    subscripts=["REGIONS_36_I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_solar_pv_rooftop_potential_c_si_mono_0pv_100th_sp",
        "__lookup__": "_ext_lookup_solar_pv_rooftop_potential_c_si_mono_0pv_100th_sp",
    },
)
def solar_pv_rooftop_potential_c_si_mono_0pv_100th_sp(x, final_subs=None):
    """
    Solar PV rooftop potential Si-monocrystaline assuming a 0% share of rooftop for PV (vs solar thermal rooftop).
    """
    return _ext_lookup_solar_pv_rooftop_potential_c_si_mono_0pv_100th_sp(x, final_subs)


_ext_lookup_solar_pv_rooftop_potential_c_si_mono_0pv_100th_sp = ExtLookup(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-data",
    "PV_PANEL_EFFICIENCY_C_Si_Mono",
    "SOLAR_PV_ROOFTOP_POTENTIAL_C_Si_Mono_0PV_100TH_SP",
    {"REGIONS_36_I": _subscript_dict["REGIONS_36_I"]},
    _root,
    {"REGIONS_36_I": _subscript_dict["REGIONS_36_I"]},
    "_ext_lookup_solar_pv_rooftop_potential_c_si_mono_0pv_100th_sp",
)


@component.add(
    name="SOLAR_PV_ROOFTOP_POTENTIAL_C_Si_MONO_100PV_0TH_SP",
    units="PJ/Year",
    subscripts=["REGIONS_36_I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_solar_pv_rooftop_potential_c_si_mono_100pv_0th_sp",
        "__lookup__": "_ext_lookup_solar_pv_rooftop_potential_c_si_mono_100pv_0th_sp",
    },
)
def solar_pv_rooftop_potential_c_si_mono_100pv_0th_sp(x, final_subs=None):
    """
    Solar PV rooftop potential Si-monocrystaline assuming a 100% share of rooftop for PV (vs solar thermal rooftop).
    """
    return _ext_lookup_solar_pv_rooftop_potential_c_si_mono_100pv_0th_sp(x, final_subs)


_ext_lookup_solar_pv_rooftop_potential_c_si_mono_100pv_0th_sp = ExtLookup(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-data",
    "PV_PANEL_EFFICIENCY_C_Si_Mono",
    "SOLAR_PV_ROOFTOP_POTENTIAL_C_Si_Mono_100PV_0TH_SP",
    {"REGIONS_36_I": _subscript_dict["REGIONS_36_I"]},
    _root,
    {"REGIONS_36_I": _subscript_dict["REGIONS_36_I"]},
    "_ext_lookup_solar_pv_rooftop_potential_c_si_mono_100pv_0th_sp",
)


@component.add(
    name="SOLAR_PV_ROOFTOP_POTENTIAL_C_Si_MONO_25PV_75TH_SP",
    units="PJ/Year",
    subscripts=["REGIONS_36_I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_solar_pv_rooftop_potential_c_si_mono_25pv_75th_sp",
        "__lookup__": "_ext_lookup_solar_pv_rooftop_potential_c_si_mono_25pv_75th_sp",
    },
)
def solar_pv_rooftop_potential_c_si_mono_25pv_75th_sp(x, final_subs=None):
    """
    Solar PV rooftop potential Si-monocrystaline assuming a 25% share of rooftop for PV (vs solar thermal rooftop).
    """
    return _ext_lookup_solar_pv_rooftop_potential_c_si_mono_25pv_75th_sp(x, final_subs)


_ext_lookup_solar_pv_rooftop_potential_c_si_mono_25pv_75th_sp = ExtLookup(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-data",
    "PV_PANEL_EFFICIENCY_C_Si_Mono",
    "SOLAR_PV_ROOFTOP_POTENTIAL_C_Si_Mono_25PV_75TH_SP",
    {"REGIONS_36_I": _subscript_dict["REGIONS_36_I"]},
    _root,
    {"REGIONS_36_I": _subscript_dict["REGIONS_36_I"]},
    "_ext_lookup_solar_pv_rooftop_potential_c_si_mono_25pv_75th_sp",
)


@component.add(
    name="SOLAR_PV_ROOFTOP_POTENTIAL_C_Si_MONO_50PV_50TH_SP",
    units="PJ/Year",
    subscripts=["REGIONS_36_I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_solar_pv_rooftop_potential_c_si_mono_50pv_50th_sp",
        "__lookup__": "_ext_lookup_solar_pv_rooftop_potential_c_si_mono_50pv_50th_sp",
    },
)
def solar_pv_rooftop_potential_c_si_mono_50pv_50th_sp(x, final_subs=None):
    """
    Solar PV rooftop potential Si-monocrystaline assuming a 50% share of rooftop for PV (vs solar thermal rooftop).
    """
    return _ext_lookup_solar_pv_rooftop_potential_c_si_mono_50pv_50th_sp(x, final_subs)


_ext_lookup_solar_pv_rooftop_potential_c_si_mono_50pv_50th_sp = ExtLookup(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-data",
    "PV_PANEL_EFFICIENCY_C_Si_Mono",
    "SOLAR_PV_ROOFTOP_POTENTIAL_C_Si_Mono_50PV_50TH_SP",
    {"REGIONS_36_I": _subscript_dict["REGIONS_36_I"]},
    _root,
    {"REGIONS_36_I": _subscript_dict["REGIONS_36_I"]},
    "_ext_lookup_solar_pv_rooftop_potential_c_si_mono_50pv_50th_sp",
)


@component.add(
    name="SOLAR_PV_ROOFTOP_POTENTIAL_C_Si_MONO_75PV_25TH_SP",
    units="PJ/Year",
    subscripts=["REGIONS_36_I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_solar_pv_rooftop_potential_c_si_mono_75pv_25th_sp",
        "__lookup__": "_ext_lookup_solar_pv_rooftop_potential_c_si_mono_75pv_25th_sp",
    },
)
def solar_pv_rooftop_potential_c_si_mono_75pv_25th_sp(x, final_subs=None):
    """
    Solar PV rooftop potential Si-monocrystaline assuming a 75% share of rooftop for PV (vs solar thermal rooftop).
    """
    return _ext_lookup_solar_pv_rooftop_potential_c_si_mono_75pv_25th_sp(x, final_subs)


_ext_lookup_solar_pv_rooftop_potential_c_si_mono_75pv_25th_sp = ExtLookup(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-data",
    "PV_PANEL_EFFICIENCY_C_Si_Mono",
    "SOLAR_PV_ROOFTOP_POTENTIAL_C_Si_Mono_75PV_25TH_SP",
    {"REGIONS_36_I": _subscript_dict["REGIONS_36_I"]},
    _root,
    {"REGIONS_36_I": _subscript_dict["REGIONS_36_I"]},
    "_ext_lookup_solar_pv_rooftop_potential_c_si_mono_75pv_25th_sp",
)


@component.add(
    name="SOLAR_PV_ROOFTOP_POTENTIAL_C_Si_MONO_USER_DEFINED_SP",
    units="PJ/Year",
    subscripts=["REGIONS_36_I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_solar_pv_rooftop_potential_c_si_mono_user_defined_sp",
        "__lookup__": "_ext_lookup_solar_pv_rooftop_potential_c_si_mono_user_defined_sp",
    },
)
def solar_pv_rooftop_potential_c_si_mono_user_defined_sp(x, final_subs=None):
    """
    Solar PV rooftop potential Si-monocrystaline assuming a share of rooftop for PV (vs solar thermal rooftop) defined by the user.
    """
    return _ext_lookup_solar_pv_rooftop_potential_c_si_mono_user_defined_sp(
        x, final_subs
    )


_ext_lookup_solar_pv_rooftop_potential_c_si_mono_user_defined_sp = ExtLookup(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "PV_PANEL_EFFICIENCY_C_Si_Mono_USER_DEFINED",
    "SOLAR_PV_ROOFTOP_POTENTIAL_C_Si_Mono_USER_DEFINED_SP",
    {"REGIONS_36_I": _subscript_dict["REGIONS_36_I"]},
    _root,
    {"REGIONS_36_I": _subscript_dict["REGIONS_36_I"]},
    "_ext_lookup_solar_pv_rooftop_potential_c_si_mono_user_defined_sp",
)


@component.add(
    name="SOLAR_THERMAL_ROOFTOP_POTENTIAL",
    units="EJ/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_rooftop_use_solar_technologies_sp": 5,
        "solar_thermal_rooftop_potential_0pv_100th_sp": 1,
        "solar_thermal_rooftop_potential_user_defined_sp": 1,
        "solar_thermal_rooftop_potential_75pv_25th_sp": 1,
        "solar_thermal_rooftop_potential_100pv_0th_sp": 1,
        "solar_thermal_rooftop_potential_50pv_50th_sp": 1,
        "solar_thermal_rooftop_potential_25pv_75th_sp": 1,
        "growth_land_uses_vs_2015": 1,
        "switch_energy": 1,
        "unit_conversion_pj_ej": 1,
    },
)
def solar_thermal_rooftop_potential():
    """
    Solar thermal rooftop potential assuming a fixed share of roofs dedicated to solar PV and thermal. For current urban land.Including linear variation with urban land surface.
    """
    return (
        if_then_else(
            select_rooftop_use_solar_technologies_sp() == 0,
            lambda: solar_thermal_rooftop_potential_0pv_100th_sp()
            .loc[_subscript_dict["REGIONS_9_I"]]
            .rename({"REGIONS_36_I": "REGIONS_9_I"}),
            lambda: if_then_else(
                select_rooftop_use_solar_technologies_sp() == 1,
                lambda: solar_thermal_rooftop_potential_25pv_75th_sp()
                .loc[_subscript_dict["REGIONS_9_I"]]
                .rename({"REGIONS_36_I": "REGIONS_9_I"}),
                lambda: if_then_else(
                    select_rooftop_use_solar_technologies_sp() == 2,
                    lambda: solar_thermal_rooftop_potential_50pv_50th_sp()
                    .loc[_subscript_dict["REGIONS_9_I"]]
                    .rename({"REGIONS_36_I": "REGIONS_9_I"}),
                    lambda: if_then_else(
                        select_rooftop_use_solar_technologies_sp() == 3,
                        lambda: solar_thermal_rooftop_potential_75pv_25th_sp()
                        .loc[_subscript_dict["REGIONS_9_I"]]
                        .rename({"REGIONS_36_I": "REGIONS_9_I"}),
                        lambda: if_then_else(
                            select_rooftop_use_solar_technologies_sp() == 4,
                            lambda: solar_thermal_rooftop_potential_100pv_0th_sp()
                            .loc[_subscript_dict["REGIONS_9_I"]]
                            .rename({"REGIONS_36_I": "REGIONS_9_I"}),
                            lambda: solar_thermal_rooftop_potential_user_defined_sp()
                            .loc[_subscript_dict["REGIONS_9_I"]]
                            .rename({"REGIONS_36_I": "REGIONS_9_I"}),
                        ),
                    ),
                ),
            ),
        )
        * if_then_else(
            switch_energy() == 0,
            lambda: xr.DataArray(
                1, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
            ),
            lambda: growth_land_uses_vs_2015()
            .loc[:, "URBAN_LAND"]
            .reset_coords(drop=True),
        )
        / unit_conversion_pj_ej()
    )


@component.add(
    name="SOLAR_THERMAL_ROOFTOP_POTENTIAL_0PV_100TH_SP",
    units="PJ/Year",
    subscripts=["REGIONS_36_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_solar_thermal_rooftop_potential_0pv_100th_sp"
    },
)
def solar_thermal_rooftop_potential_0pv_100th_sp():
    """
    Solar thermal rooftop potential 0% share of rooftop for PV (vs solar thermal rooftop).
    """
    return _ext_constant_solar_thermal_rooftop_potential_0pv_100th_sp()


_ext_constant_solar_thermal_rooftop_potential_0pv_100th_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-data",
    "SOLAR_THERMAL_ROOFTOP_POTENTIAL_0PV_100TH_SP*",
    {"REGIONS_36_I": _subscript_dict["REGIONS_36_I"]},
    _root,
    {"REGIONS_36_I": _subscript_dict["REGIONS_36_I"]},
    "_ext_constant_solar_thermal_rooftop_potential_0pv_100th_sp",
)


@component.add(
    name="SOLAR_THERMAL_ROOFTOP_POTENTIAL_100PV_0TH_SP",
    units="PJ/Year",
    subscripts=["REGIONS_36_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_solar_thermal_rooftop_potential_100pv_0th_sp"
    },
)
def solar_thermal_rooftop_potential_100pv_0th_sp():
    """
    Solar thermal rooftop potential 100% share of rooftop for PV (vs solar thermal rooftop).
    """
    return _ext_constant_solar_thermal_rooftop_potential_100pv_0th_sp()


_ext_constant_solar_thermal_rooftop_potential_100pv_0th_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-data",
    "SOLAR_THERMAL_ROOFTOP_POTENTIAL_100PV_0TH_SP*",
    {"REGIONS_36_I": _subscript_dict["REGIONS_36_I"]},
    _root,
    {"REGIONS_36_I": _subscript_dict["REGIONS_36_I"]},
    "_ext_constant_solar_thermal_rooftop_potential_100pv_0th_sp",
)


@component.add(
    name="SOLAR_THERMAL_ROOFTOP_POTENTIAL_25PV_75TH_SP",
    units="PJ/Year",
    subscripts=["REGIONS_36_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_solar_thermal_rooftop_potential_25pv_75th_sp"
    },
)
def solar_thermal_rooftop_potential_25pv_75th_sp():
    """
    Solar thermal rooftop potential 25% share of rooftop for PV (vs solar thermal rooftop).
    """
    return _ext_constant_solar_thermal_rooftop_potential_25pv_75th_sp()


_ext_constant_solar_thermal_rooftop_potential_25pv_75th_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-data",
    "SOLAR_THERMAL_ROOFTOP_POTENTIAL_25PV_75TH_SP*",
    {"REGIONS_36_I": _subscript_dict["REGIONS_36_I"]},
    _root,
    {"REGIONS_36_I": _subscript_dict["REGIONS_36_I"]},
    "_ext_constant_solar_thermal_rooftop_potential_25pv_75th_sp",
)


@component.add(
    name="SOLAR_THERMAL_ROOFTOP_POTENTIAL_50PV_50TH_SP",
    units="PJ/Year",
    subscripts=["REGIONS_36_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_solar_thermal_rooftop_potential_50pv_50th_sp"
    },
)
def solar_thermal_rooftop_potential_50pv_50th_sp():
    """
    Solar thermal rooftop potential 50% share of rooftop for PV (vs solar thermal rooftop).
    """
    return _ext_constant_solar_thermal_rooftop_potential_50pv_50th_sp()


_ext_constant_solar_thermal_rooftop_potential_50pv_50th_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-data",
    "SOLAR_THERMAL_ROOFTOP_POTENTIAL_50PV_50TH_SP*",
    {"REGIONS_36_I": _subscript_dict["REGIONS_36_I"]},
    _root,
    {"REGIONS_36_I": _subscript_dict["REGIONS_36_I"]},
    "_ext_constant_solar_thermal_rooftop_potential_50pv_50th_sp",
)


@component.add(
    name="SOLAR_THERMAL_ROOFTOP_POTENTIAL_75PV_25TH_SP",
    units="PJ/Year",
    subscripts=["REGIONS_36_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_solar_thermal_rooftop_potential_75pv_25th_sp"
    },
)
def solar_thermal_rooftop_potential_75pv_25th_sp():
    """
    Solar thermal rooftop potential 75% share of rooftop for PV (vs solar thermal rooftop).
    """
    return _ext_constant_solar_thermal_rooftop_potential_75pv_25th_sp()


_ext_constant_solar_thermal_rooftop_potential_75pv_25th_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-data",
    "SOLAR_THERMAL_ROOFTOP_POTENTIAL_75PV_25TH_SP*",
    {"REGIONS_36_I": _subscript_dict["REGIONS_36_I"]},
    _root,
    {"REGIONS_36_I": _subscript_dict["REGIONS_36_I"]},
    "_ext_constant_solar_thermal_rooftop_potential_75pv_25th_sp",
)


@component.add(
    name="SOLAR_THERMAL_ROOFTOP_POTENTIAL_USER_DEFINED_SP",
    units="PJ/Year",
    subscripts=["REGIONS_36_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_solar_thermal_rooftop_potential_user_defined_sp"
    },
)
def solar_thermal_rooftop_potential_user_defined_sp():
    """
    Solar thermal rooftop potential share of rooftop for PV (vs solar thermal rooftop) defined by the user.
    """
    return _ext_constant_solar_thermal_rooftop_potential_user_defined_sp()


_ext_constant_solar_thermal_rooftop_potential_user_defined_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "SOLAR_THERMAL_ROOFTOP_POTENTIAL_USER_DEFINED_SP*",
    {"REGIONS_36_I": _subscript_dict["REGIONS_36_I"]},
    _root,
    {"REGIONS_36_I": _subscript_dict["REGIONS_36_I"]},
    "_ext_constant_solar_thermal_rooftop_potential_user_defined_sp",
)


@component.add(
    name="SWITCH_NRG_LIMITED_RES_POTENTIALS",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_nrg_limited_res_potentials"},
)
def switch_nrg_limited_res_potentials():
    """
    Can take two values: 1: limited RES potentials (either exogenous or endogenously) 0: unlimited RES potentials (although the annual growth rate can still be limited following energy module parametrization)
    """
    return _ext_constant_switch_nrg_limited_res_potentials()


_ext_constant_switch_nrg_limited_res_potentials = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_NRG_LIMITED_RES_POTENTIALS",
    {},
    _root,
    {},
    "_ext_constant_switch_nrg_limited_res_potentials",
)


@component.add(
    name="UNLIMITED_PROTRA_RES_PARAMETER",
    units="EJ/Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_unlimited_protra_res_parameter"},
)
def unlimited_protra_res_parameter():
    """
    This parameter represents a extremely high potential which is used in the model in order to represent that PROTRA RES are in practical unlimited.
    """
    return _ext_constant_unlimited_protra_res_parameter()


_ext_constant_unlimited_protra_res_parameter = ExtConstant(
    "model_parameters/energy/energy-potentials.xlsx",
    "PROTRA",
    "UNLIMITED_PROTRA_RES_PARAMETER",
    {},
    _root,
    {},
    "_ext_constant_unlimited_protra_res_parameter",
)
