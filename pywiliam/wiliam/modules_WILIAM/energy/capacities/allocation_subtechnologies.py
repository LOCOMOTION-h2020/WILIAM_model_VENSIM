"""
Module energy.capacities.allocation_subtechnologies
Translated using PySD version 3.10.0
"""


@component.add(
    name="DELAY_indicator_PV_panel_mineral_abundance",
    units="DMNL",
    subscripts=["PROTRA_PP_SOLAR_PV_I", "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delay_indicator_pv_panel_mineral_abundance": 1},
    other_deps={
        "_delayfixed_delay_indicator_pv_panel_mineral_abundance": {
            "initial": {},
            "step": {"indicator_pv_panel_mineral_abundance": 1},
        }
    },
)
def delay_indicator_pv_panel_mineral_abundance():
    """
    DELAY for avoid feedback problems with the Share of PV panels.
    """
    return _delayfixed_delay_indicator_pv_panel_mineral_abundance()


_delayfixed_delay_indicator_pv_panel_mineral_abundance = DelayFixed(
    lambda: indicator_pv_panel_mineral_abundance(),
    lambda: 1,
    lambda: xr.DataArray(
        1,
        {
            "PROTRA_PP_SOLAR_PV_I": _subscript_dict["PROTRA_PP_SOLAR_PV_I"],
            "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": _subscript_dict[
                "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"
            ],
        },
        ["PROTRA_PP_SOLAR_PV_I", "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"],
    ),
    time_step,
    "_delayfixed_delay_indicator_pv_panel_mineral_abundance",
)


@component.add(
    name="DELAY_PV_EROI_selection",
    units="DMNL",
    subscripts=[
        "REGIONS_9_I",
        "PROTRA_PP_SOLAR_PV_I",
        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I",
    ],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delay_pv_eroi_selection": 1},
    other_deps={
        "_delayfixed_delay_pv_eroi_selection": {
            "initial": {},
            "step": {"eroi_pv_selection": 1},
        }
    },
)
def delay_pv_eroi_selection():
    """
    DELAY for avoid feedback problems with EROI of PV panels
    """
    return _delayfixed_delay_pv_eroi_selection()


_delayfixed_delay_pv_eroi_selection = DelayFixed(
    lambda: eroi_pv_selection(),
    lambda: 1,
    lambda: xr.DataArray(
        3,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "PROTRA_PP_SOLAR_PV_I": _subscript_dict["PROTRA_PP_SOLAR_PV_I"],
            "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": _subscript_dict[
                "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"
            ],
        },
        ["REGIONS_9_I", "PROTRA_PP_SOLAR_PV_I", "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"],
    ),
    time_step,
    "_delayfixed_delay_pv_eroi_selection",
)


@component.add(
    name="delayed_ESOI_st_electrified_vehicle",
    units="DMNL",
    subscripts=[
        "REGIONS_35_I",
        "EV_BATTERIES_I",
        "TRANSPORT_POWER_TRAIN_I",
        "BATTERY_VEHICLES_I",
    ],
    comp_type="Constant, Stateful",
    comp_subtype="DelayFixed, Normal",
    depends_on={
        "_delayfixed_delayed_esoi_st_electrified_vehicle": 1,
        "_delayfixed_delayed_esoi_st_electrified_vehicle_1": 1,
    },
    other_deps={
        "_delayfixed_delayed_esoi_st_electrified_vehicle": {
            "initial": {},
            "step": {"esoi_st_electrified_vehicle": 1},
        },
        "_delayfixed_delayed_esoi_st_electrified_vehicle_1": {
            "initial": {},
            "step": {"esoi_st_electrified_vehicle": 1},
        },
    },
)
def delayed_esoi_st_electrified_vehicle():
    """
    DELAY for avoid feedback problems with the Dynamic ESOI of EV batteries
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "EV_BATTERIES_I": _subscript_dict["EV_BATTERIES_I"],
            "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
            "BATTERY_VEHICLES_I": _subscript_dict["BATTERY_VEHICLES_I"],
        },
        [
            "REGIONS_35_I",
            "EV_BATTERIES_I",
            "TRANSPORT_POWER_TRAIN_I",
            "BATTERY_VEHICLES_I",
        ],
    )
    value.loc[
        :, :, ["BEV"], :
    ] = _delayfixed_delayed_esoi_st_electrified_vehicle().values
    value.loc[
        :, :, ["PHEV"], :
    ] = _delayfixed_delayed_esoi_st_electrified_vehicle_1().values
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, :, ["BEV"], :] = False
    except_subs.loc[:, :, ["PHEV"], :] = False
    value.values[except_subs.values] = 0
    return value


_delayfixed_delayed_esoi_st_electrified_vehicle = DelayFixed(
    lambda: esoi_st_electrified_vehicle()
    .loc[:, :, "BEV", :]
    .reset_coords(drop=True)
    .expand_dims({"TRANSPORT_POWER_TRAIN_I": ["BEV"]}, 2),
    lambda: 1,
    lambda: xr.DataArray(
        3,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "EV_BATTERIES_I": _subscript_dict["EV_BATTERIES_I"],
            "TRANSPORT_POWER_TRAIN_I": ["BEV"],
            "BATTERY_VEHICLES_I": _subscript_dict["BATTERY_VEHICLES_I"],
        },
        [
            "REGIONS_35_I",
            "EV_BATTERIES_I",
            "TRANSPORT_POWER_TRAIN_I",
            "BATTERY_VEHICLES_I",
        ],
    ),
    time_step,
    "_delayfixed_delayed_esoi_st_electrified_vehicle",
)

_delayfixed_delayed_esoi_st_electrified_vehicle_1 = DelayFixed(
    lambda: esoi_st_electrified_vehicle()
    .loc[:, :, "PHEV", :]
    .reset_coords(drop=True)
    .expand_dims({"TRANSPORT_POWER_TRAIN_I": ["PHEV"]}, 2),
    lambda: 1,
    lambda: xr.DataArray(
        3,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "EV_BATTERIES_I": _subscript_dict["EV_BATTERIES_I"],
            "TRANSPORT_POWER_TRAIN_I": ["PHEV"],
            "BATTERY_VEHICLES_I": _subscript_dict["BATTERY_VEHICLES_I"],
        },
        [
            "REGIONS_35_I",
            "EV_BATTERIES_I",
            "TRANSPORT_POWER_TRAIN_I",
            "BATTERY_VEHICLES_I",
        ],
    ),
    time_step,
    "_delayfixed_delayed_esoi_st_electrified_vehicle_1",
)


@component.add(
    name="EROI_PV_selection",
    units="DMNL",
    subscripts=[
        "REGIONS_9_I",
        "PROTRA_PP_SOLAR_PV_I",
        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_eroi_boundary_for_pv_share_allocation": 1,
        "eroifinal_pv_technologies": 1,
        "eroist_pv_technologies": 1,
    },
)
def eroi_pv_selection():
    """
    EROI selection to use in the share PV technologies function
    """
    return if_then_else(
        select_eroi_boundary_for_pv_share_allocation() == 1,
        lambda: eroifinal_pv_technologies(),
        lambda: eroist_pv_technologies(),
    )


@component.add(
    name="indicator_of_battery_abundance",
    units="DMNL",
    subscripts=["EV_BATTERIES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"indicator_of_battery_scarcity": 2},
)
def indicator_of_battery_abundance():
    """
    indicator of battery abundance, the share of new EV Batteries needs a abundance indicator, therefore, we mathematically transform the scarcity indicator into an abundance indicator.
    """
    return (1 - indicator_of_battery_scarcity()) / (
        5
        - sum(
            indicator_of_battery_scarcity().rename(
                {"EV_BATTERIES_I": "EV_BATTERIES_I!"}
            ),
            dim=["EV_BATTERIES_I!"],
        )
    )


@component.add(
    name="indicator_of_battery_scarcity",
    units="DMNL",
    subscripts=["EV_BATTERIES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_energy": 1,
        "indicator_of_mineral_scarcity": 2,
        "relative_demand_of_mineral_by_ev_battery": 1,
    },
)
def indicator_of_battery_scarcity():
    """
    indicator of battery scarcity: factor that varies its value from 0 (not very scarce) to 1 (very scarce) depending on the remaining resources and reserves of each mineral present in the battery.
    """
    return if_then_else(
        switch_energy() == 0,
        lambda: xr.DataArray(
            0, {"EV_BATTERIES_I": _subscript_dict["EV_BATTERIES_I"]}, ["EV_BATTERIES_I"]
        ),
        lambda: zidz(
            sum(
                indicator_of_mineral_scarcity()
                .loc[_subscript_dict["EV_BATTERIES_MATERIALS_I"]]
                .rename({"MATERIALS_I": "EV_BATTERIES_MATERIALS_I!"})
                * relative_demand_of_mineral_by_ev_battery()
                .loc[_subscript_dict["EV_BATTERIES_MATERIALS_I"], :]
                .rename({"MATERIALS_I": "EV_BATTERIES_MATERIALS_I!"}),
                dim=["EV_BATTERIES_MATERIALS_I!"],
            ),
            sum(
                indicator_of_mineral_scarcity()
                .loc[_subscript_dict["EV_BATTERIES_MATERIALS_I"]]
                .rename({"MATERIALS_I": "EV_BATTERIES_MATERIALS_I!"}),
                dim=["EV_BATTERIES_MATERIALS_I!"],
            ),
        ),
    )


@component.add(
    name="indicator_PV_panel_mineral_abundance",
    units="DMNL",
    subscripts=["PROTRA_PP_SOLAR_PV_I", "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"indicator_pv_panel_mineral_scarcity": 2},
)
def indicator_pv_panel_mineral_abundance():
    """
    indicator of PV panel material abundance, the share of PV panel needs a abundance indicator, therefore, we mathematically transform the scarcity indicator into an abundance indicator.
    """
    return (1 - indicator_pv_panel_mineral_scarcity()) / (
        4
        - sum(
            indicator_pv_panel_mineral_scarcity().rename(
                {
                    "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!"
                }
            ),
            dim=["PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!"],
        )
    )


@component.add(
    name="indicator_PV_panel_mineral_scarcity",
    units="DMNL",
    subscripts=["PROTRA_PP_SOLAR_PV_I", "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_energy": 1,
        "indicator_of_mineral_scarcity": 2,
        "relative_demand_of_material_i_by_pv_panel": 1,
    },
)
def indicator_pv_panel_mineral_scarcity():
    """
    indicator of PV panel material scarcity: factor that varies its value from 0 (not very scarce) to 1 (very scarce) depending on the remaining resources and reserves of each mineral present in the panel.
    """
    return if_then_else(
        switch_energy() == 0,
        lambda: xr.DataArray(
            0,
            {
                "PROTRA_PP_SOLAR_PV_I": _subscript_dict["PROTRA_PP_SOLAR_PV_I"],
                "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": _subscript_dict[
                    "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"
                ],
            },
            ["PROTRA_PP_SOLAR_PV_I", "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"],
        ),
        lambda: zidz(
            sum(
                indicator_of_mineral_scarcity()
                .loc[_subscript_dict["PV_MATERIALS"]]
                .rename({"MATERIALS_I": "PV_MATERIALS!"})
                * relative_demand_of_material_i_by_pv_panel()
                .loc[_subscript_dict["PV_MATERIALS"], :, :]
                .rename({"MATERIALS_I": "PV_MATERIALS!"}),
                dim=["PV_MATERIALS!"],
            ),
            sum(
                indicator_of_mineral_scarcity()
                .loc[_subscript_dict["PV_MATERIALS"]]
                .rename({"MATERIALS_I": "PV_MATERIALS!"}),
                dim=["PV_MATERIALS!"],
            ),
        ),
    )


@component.add(
    name="INITIAL_SHARE_WEIGHTS_PV_TECHNOLOGIES",
    units="DMNL",
    subscripts=["PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_share_weights_pv_technologies"},
)
def initial_share_weights_pv_technologies():
    """
    initial share weights, from the logit model functions
    """
    return _ext_constant_initial_share_weights_pv_technologies()


_ext_constant_initial_share_weights_pv_technologies = ExtConstant(
    "model_parameters/energy/energy.xlsm",
    "allocation_new_capacity_subtech",
    "INITIAL_SHARE_WEIGHTS_PV_TECHNOLOGIES*",
    {
        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": _subscript_dict[
            "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"
        ]
    },
    _root,
    {
        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": _subscript_dict[
            "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"
        ]
    },
    "_ext_constant_initial_share_weights_pv_technologies",
)


@component.add(
    name="SELECT_EROI_BOUNDARY_FOR_PV_SHARE_ALLOCATION",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_select_eroi_boundary_for_pv_share_allocation"
    },
)
def select_eroi_boundary_for_pv_share_allocation():
    """
    SELECT to chose which EROI boundary level to be used to compute the allocation of PV subtechnologies: 1:EROIfinal 0:EROIst
    """
    return _ext_constant_select_eroi_boundary_for_pv_share_allocation()


_ext_constant_select_eroi_boundary_for_pv_share_allocation = ExtConstant(
    "model_parameters/energy/energy.xlsm",
    "allocation_new_capacity_subtech",
    "SELECT_EROI_BOUNDARY",
    {},
    _root,
    {},
    "_ext_constant_select_eroi_boundary_for_pv_share_allocation",
)


@component.add(
    name="SELECT_LOGIT_MODEL_PV_SUBTECH_ALLOCATION",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_select_logit_model_pv_subtech_allocation"
    },
)
def select_logit_model_pv_subtech_allocation():
    """
    1: modified logit model 0: logit model
    """
    return _ext_constant_select_logit_model_pv_subtech_allocation()


_ext_constant_select_logit_model_pv_subtech_allocation = ExtConstant(
    "model_parameters/energy/energy.xlsm",
    "allocation_new_capacity_subtech",
    "SELECT_LOGIT_MODEL_PV_SUBTECH_ALLOCATION",
    {},
    _root,
    {},
    "_ext_constant_select_logit_model_pv_subtech_allocation",
)


@component.add(
    name="share_new_PV_subtechn_land",
    units="DMNL",
    subscripts=["REGIONS_9_I", "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 2,
        "select_logit_model_pv_subtech_allocation": 1,
        "share_pv_subtechnologies_before_2020": 1,
        "logit_model_coefficient_or_exponent": 4,
        "delay_pv_eroi_selection": 4,
        "delay_indicator_pv_panel_mineral_abundance": 4,
        "initial_share_weights_pv_technologies": 4,
    },
)
def share_new_pv_subtechn_land():
    """
    Share of PV subtechnologies for PV on land.
    """
    return if_then_else(
        time() < 2012,
        lambda: xr.DataArray(
            0,
            {
                "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": _subscript_dict[
                    "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"
                ],
                "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            },
            ["PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I", "REGIONS_9_I"],
        ),
        lambda: if_then_else(
            time() < 2021,
            lambda: share_pv_subtechnologies_before_2020().expand_dims(
                {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, 1
            ),
            lambda: if_then_else(
                select_logit_model_pv_subtech_allocation() == 1,
                lambda: initial_share_weights_pv_technologies()
                * zidz(
                    (
                        delay_pv_eroi_selection()
                        .loc[:, "PROTRA_PP_solar_open_space_PV", :]
                        .reset_coords(drop=True)
                        * delay_indicator_pv_panel_mineral_abundance()
                        .loc["PROTRA_PP_solar_open_space_PV", :]
                        .reset_coords(drop=True)
                    )
                    ** logit_model_coefficient_or_exponent(),
                    sum(
                        initial_share_weights_pv_technologies().rename(
                            {
                                "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!"
                            }
                        )
                        * (
                            (
                                delay_pv_eroi_selection()
                                .loc[:, "PROTRA_PP_solar_open_space_PV", :]
                                .reset_coords(drop=True)
                                .rename(
                                    {
                                        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!"
                                    }
                                )
                                * delay_indicator_pv_panel_mineral_abundance()
                                .loc["PROTRA_PP_solar_open_space_PV", :]
                                .reset_coords(drop=True)
                                .rename(
                                    {
                                        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!"
                                    }
                                )
                            )
                            ** logit_model_coefficient_or_exponent()
                        ).transpose(
                            "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!", "REGIONS_9_I"
                        ),
                        dim=["PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!"],
                    ).expand_dims(
                        {
                            "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": _subscript_dict[
                                "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"
                            ]
                        },
                        1,
                    ),
                ).transpose("PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I", "REGIONS_9_I"),
                lambda: initial_share_weights_pv_technologies()
                * zidz(
                    np.exp(
                        (
                            delay_pv_eroi_selection()
                            .loc[:, "PROTRA_PP_solar_open_space_PV", :]
                            .reset_coords(drop=True)
                            * delay_indicator_pv_panel_mineral_abundance()
                            .loc["PROTRA_PP_solar_open_space_PV", :]
                            .reset_coords(drop=True)
                        )
                        * logit_model_coefficient_or_exponent()
                    ),
                    sum(
                        initial_share_weights_pv_technologies().rename(
                            {
                                "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!"
                            }
                        )
                        * np.exp(
                            (
                                delay_pv_eroi_selection()
                                .loc[:, "PROTRA_PP_solar_open_space_PV", :]
                                .reset_coords(drop=True)
                                .rename(
                                    {
                                        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!"
                                    }
                                )
                                * delay_indicator_pv_panel_mineral_abundance()
                                .loc["PROTRA_PP_solar_open_space_PV", :]
                                .reset_coords(drop=True)
                                .rename(
                                    {
                                        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!"
                                    }
                                )
                            )
                            * logit_model_coefficient_or_exponent()
                        ).transpose(
                            "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!", "REGIONS_9_I"
                        ),
                        dim=["PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!"],
                    ).expand_dims(
                        {
                            "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": _subscript_dict[
                                "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"
                            ]
                        },
                        1,
                    ),
                ).transpose("PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I", "REGIONS_9_I"),
            ),
        ),
    ).transpose("REGIONS_9_I", "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I")


@component.add(
    name="share_new_PV_subtechn_urban",
    units="DMNL",
    subscripts=["REGIONS_9_I", "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 2,
        "select_logit_model_pv_subtech_allocation": 1,
        "share_pv_subtechnologies_before_2020": 1,
        "logit_model_coefficient_or_exponent": 4,
        "delay_pv_eroi_selection": 4,
        "delay_indicator_pv_panel_mineral_abundance": 4,
        "initial_share_weights_pv_technologies": 4,
    },
)
def share_new_pv_subtechn_urban():
    """
    Share of PV subtechnologies for urban PV.
    """
    return if_then_else(
        time() < 2012,
        lambda: xr.DataArray(
            0,
            {
                "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": _subscript_dict[
                    "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"
                ],
                "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            },
            ["PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I", "REGIONS_9_I"],
        ),
        lambda: if_then_else(
            time() < 2021,
            lambda: share_pv_subtechnologies_before_2020().expand_dims(
                {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, 1
            ),
            lambda: if_then_else(
                select_logit_model_pv_subtech_allocation() == 1,
                lambda: initial_share_weights_pv_technologies()
                * zidz(
                    (
                        delay_pv_eroi_selection()
                        .loc[:, "PROTRA_PP_solar_urban_PV", :]
                        .reset_coords(drop=True)
                        * delay_indicator_pv_panel_mineral_abundance()
                        .loc["PROTRA_PP_solar_urban_PV", :]
                        .reset_coords(drop=True)
                    )
                    ** logit_model_coefficient_or_exponent(),
                    sum(
                        initial_share_weights_pv_technologies().rename(
                            {
                                "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!"
                            }
                        )
                        * (
                            (
                                delay_pv_eroi_selection()
                                .loc[:, "PROTRA_PP_solar_urban_PV", :]
                                .reset_coords(drop=True)
                                .rename(
                                    {
                                        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!"
                                    }
                                )
                                * delay_indicator_pv_panel_mineral_abundance()
                                .loc["PROTRA_PP_solar_urban_PV", :]
                                .reset_coords(drop=True)
                                .rename(
                                    {
                                        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!"
                                    }
                                )
                            )
                            ** logit_model_coefficient_or_exponent()
                        ).transpose(
                            "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!", "REGIONS_9_I"
                        ),
                        dim=["PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!"],
                    ).expand_dims(
                        {
                            "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": _subscript_dict[
                                "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"
                            ]
                        },
                        1,
                    ),
                ).transpose("PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I", "REGIONS_9_I"),
                lambda: initial_share_weights_pv_technologies()
                * zidz(
                    np.exp(
                        (
                            delay_pv_eroi_selection()
                            .loc[:, "PROTRA_PP_solar_urban_PV", :]
                            .reset_coords(drop=True)
                            * delay_indicator_pv_panel_mineral_abundance()
                            .loc["PROTRA_PP_solar_urban_PV", :]
                            .reset_coords(drop=True)
                        )
                        * logit_model_coefficient_or_exponent()
                    ),
                    sum(
                        initial_share_weights_pv_technologies().rename(
                            {
                                "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!"
                            }
                        )
                        * np.exp(
                            (
                                delay_pv_eroi_selection()
                                .loc[:, "PROTRA_PP_solar_urban_PV", :]
                                .reset_coords(drop=True)
                                .rename(
                                    {
                                        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!"
                                    }
                                )
                                * delay_indicator_pv_panel_mineral_abundance()
                                .loc["PROTRA_PP_solar_urban_PV", :]
                                .reset_coords(drop=True)
                                .rename(
                                    {
                                        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!"
                                    }
                                )
                            )
                            * logit_model_coefficient_or_exponent()
                        ).transpose(
                            "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!", "REGIONS_9_I"
                        ),
                        dim=["PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!"],
                    ).expand_dims(
                        {
                            "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": _subscript_dict[
                                "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"
                            ]
                        },
                        1,
                    ),
                ).transpose("PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I", "REGIONS_9_I"),
            ),
        ),
    ).transpose("REGIONS_9_I", "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I")


@component.add(
    name="share_of_new_EV_subtechn_batteries",
    units="DMNL",
    subscripts=[
        "REGIONS_35_I",
        "EV_BATTERIES_I",
        "TRANSPORT_POWER_TRAIN_I",
        "BATTERY_VEHICLES_I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "share_ev_batteries_before_2015": 1,
        "delayed_esoi_st_electrified_vehicle": 4,
        "logit_model_coefficient_or_exponent": 4,
        "select_logit_model_ev_batteries_subtech_allocation": 1,
        "initial_share_weights_evs_batteries": 4,
        "indicator_of_battery_abundance": 4,
    },
)
def share_of_new_ev_subtechn_batteries():
    """
    Share of new EV batteries. Equation of logit and modified logit model from J. F. Clarke y J. A. Edmonds 1993.
    """
    return if_then_else(
        time() < 2015,
        lambda: share_ev_batteries_before_2015()
        .expand_dims(
            {"TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"]}, 2
        )
        .expand_dims({"BATTERY_VEHICLES_I": _subscript_dict["BATTERY_VEHICLES_I"]}, 3),
        lambda: if_then_else(
            select_logit_model_ev_batteries_subtech_allocation() == 1,
            lambda: initial_share_weights_evs_batteries()
            * zidz(
                (
                    delayed_esoi_st_electrified_vehicle()
                    * indicator_of_battery_abundance()
                )
                ** logit_model_coefficient_or_exponent(),
                sum(
                    initial_share_weights_evs_batteries().rename(
                        {"EV_BATTERIES_I": "EV_BATTERIES_I!"}
                    )
                    * (
                        (
                            delayed_esoi_st_electrified_vehicle().rename(
                                {"EV_BATTERIES_I": "EV_BATTERIES_I!"}
                            )
                            * indicator_of_battery_abundance().rename(
                                {"EV_BATTERIES_I": "EV_BATTERIES_I!"}
                            )
                        )
                        ** logit_model_coefficient_or_exponent()
                    ).transpose(
                        "EV_BATTERIES_I!",
                        "REGIONS_35_I",
                        "TRANSPORT_POWER_TRAIN_I",
                        "BATTERY_VEHICLES_I",
                    ),
                    dim=["EV_BATTERIES_I!"],
                ).expand_dims({"EV_BATTERIES_I": _subscript_dict["EV_BATTERIES_I"]}, 1),
            ).transpose(
                "EV_BATTERIES_I",
                "REGIONS_35_I",
                "TRANSPORT_POWER_TRAIN_I",
                "BATTERY_VEHICLES_I",
            ),
            lambda: initial_share_weights_evs_batteries()
            * zidz(
                np.exp(
                    (
                        delayed_esoi_st_electrified_vehicle()
                        * indicator_of_battery_abundance()
                    )
                    * logit_model_coefficient_or_exponent()
                ),
                sum(
                    initial_share_weights_evs_batteries().rename(
                        {"EV_BATTERIES_I": "EV_BATTERIES_I!"}
                    )
                    * np.exp(
                        (
                            delayed_esoi_st_electrified_vehicle().rename(
                                {"EV_BATTERIES_I": "EV_BATTERIES_I!"}
                            )
                            * indicator_of_battery_abundance().rename(
                                {"EV_BATTERIES_I": "EV_BATTERIES_I!"}
                            )
                        )
                        * logit_model_coefficient_or_exponent()
                    ).transpose(
                        "EV_BATTERIES_I!",
                        "REGIONS_35_I",
                        "TRANSPORT_POWER_TRAIN_I",
                        "BATTERY_VEHICLES_I",
                    ),
                    dim=["EV_BATTERIES_I!"],
                ).expand_dims({"EV_BATTERIES_I": _subscript_dict["EV_BATTERIES_I"]}, 1),
            ).transpose(
                "EV_BATTERIES_I",
                "REGIONS_35_I",
                "TRANSPORT_POWER_TRAIN_I",
                "BATTERY_VEHICLES_I",
            ),
        ).transpose(
            "REGIONS_35_I",
            "EV_BATTERIES_I",
            "TRANSPORT_POWER_TRAIN_I",
            "BATTERY_VEHICLES_I",
        ),
    )
