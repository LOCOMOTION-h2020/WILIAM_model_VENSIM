"""
Module materials.requirements.electric_transport
Translated using PySD version 3.10.0
"""


@component.add(
    name="additional_Cu_in_the_rest_of_EV_wrt_to_ICE",
    units="Mt/Year",
    subscripts=["REGIONS_35_I", "MATERIALS_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_materials": 1,
        "total_new_number_ev_vehicles": 1,
        "unit_conversion_kg_mt": 1,
        "additional_cu_inland_ev_in_relation_to_ice": 1,
    },
)
def additional_cu_in_the_rest_of_ev_wrt_to_ice():
    """
    Total materials requirements of additional Cu in the rest of the electric vehicle respect to ICE vehicles.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "MATERIALS_I": _subscript_dict["MATERIALS_I"],
        },
        ["REGIONS_35_I", "MATERIALS_I"],
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, ["Copper"]] = False
    value.values[except_subs.values] = 0
    value.loc[:, ["Copper"]] = (
        if_then_else(
            switch_materials() == 0,
            lambda: xr.DataArray(
                0, {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]}, ["REGIONS_35_I"]
            ),
            lambda: sum(
                total_new_number_ev_vehicles().rename(
                    {
                        "TRANSPORT_POWER_TRAIN_I": "TRANSPORT_POWER_TRAIN_I!",
                        "BATTERY_VEHICLES_I": "BATTERY_VEHICLES_I!",
                    }
                )
                * additional_cu_inland_ev_in_relation_to_ice().rename(
                    {
                        "TRANSPORT_POWER_TRAIN_I": "TRANSPORT_POWER_TRAIN_I!",
                        "BATTERY_VEHICLES_I": "BATTERY_VEHICLES_I!",
                    }
                ),
                dim=["TRANSPORT_POWER_TRAIN_I!", "BATTERY_VEHICLES_I!"],
            )
            / unit_conversion_kg_mt(),
        )
        .expand_dims({"EV_BATTERIES_MATERIALS_I": ["Copper"]}, 1)
        .values
    )
    return value


@component.add(
    name="cement_required_for_new_EV_chargers_and_grids",
    units="Mt/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "materials_required_for_new_ev_chargers": 1,
        "materials_required_for_new_ev_chargers_grids": 1,
    },
)
def cement_required_for_new_ev_chargers_and_grids():
    """
    weight of cement required for the infrastructure of electric vehicles
    """
    return materials_required_for_new_ev_chargers().loc[:, "Cement"].reset_coords(
        drop=True
    ) + materials_required_for_new_ev_chargers_grids().loc[:, "Cement"].reset_coords(
        drop=True
    )


@component.add(
    name="Cu_extract_for_new_EV",
    units="Mt/Year",
    subscripts=["REGIONS_35_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "additional_cu_in_the_rest_of_ev_wrt_to_ice": 2,
        "rc_rate_mineral_35r": 2,
        "cumulated_additional_cu_in_the_rest_of_electric_vehicles_respect_to_ice": 2,
    },
)
def cu_extract_for_new_ev():
    """
    Total extracted additional Cu of electrified vehicles. additional_Cu_in_the_rest_of_EV_wrt_to_ICE[REGIONS 35 I,MATERIALS I]*(1-RC_rate_mineral_35R[REGIONS 35 I,MATERIALS I])
    """
    return if_then_else(
        -additional_cu_in_the_rest_of_ev_wrt_to_ice() * (1 - rc_rate_mineral_35r())
        > cumulated_additional_cu_in_the_rest_of_electric_vehicles_respect_to_ice(),
        lambda: -cumulated_additional_cu_in_the_rest_of_electric_vehicles_respect_to_ice(),
        lambda: additional_cu_in_the_rest_of_ev_wrt_to_ice()
        * (1 - rc_rate_mineral_35r()),
    )


@component.add(
    name="cum_total_materials_to_extract_for_electrified_transport_from_2015_9R",
    units="Mt",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cumulated_total_materials_to_extract_for_electrified_transport_from_2015": 2
    },
)
def cum_total_materials_to_extract_for_electrified_transport_from_2015_9r():
    value = xr.DataArray(
        np.nan, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
    )
    value.loc[["EU27"]] = sum(
        cumulated_total_materials_to_extract_for_electrified_transport_from_2015()
        .loc[_subscript_dict["REGIONS_EU27_I"], :]
        .rename({"REGIONS_35_I": "REGIONS_EU27_I!", "MATERIALS_I": "MATERIALS_I!"}),
        dim=["REGIONS_EU27_I!", "MATERIALS_I!"],
    )
    value.loc[_subscript_dict["REGIONS_8_I"]] = sum(
        cumulated_total_materials_to_extract_for_electrified_transport_from_2015()
        .loc[_subscript_dict["REGIONS_8_I"], :]
        .rename({"REGIONS_35_I": "REGIONS_8_I", "MATERIALS_I": "MATERIALS_I!"}),
        dim=["MATERIALS_I!"],
    ).values
    return value


@component.add(
    name="cumulated_additional_Cu_in_the_rest_of_electric_vehicles_respect_to_ICE",
    units="Mt",
    subscripts=["REGIONS_35_I", "MATERIALS_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={
        "_integ_cumulated_additional_cu_in_the_rest_of_electric_vehicles_respect_to_ice": 1
    },
    other_deps={
        "_integ_cumulated_additional_cu_in_the_rest_of_electric_vehicles_respect_to_ice": {
            "initial": {},
            "step": {"cu_extract_for_new_ev": 1},
        }
    },
)
def cumulated_additional_cu_in_the_rest_of_electric_vehicles_respect_to_ice():
    """
    Cumulated extracted additional Cu of electrified vehicles.
    """
    return (
        _integ_cumulated_additional_cu_in_the_rest_of_electric_vehicles_respect_to_ice()
    )


_integ_cumulated_additional_cu_in_the_rest_of_electric_vehicles_respect_to_ice = Integ(
    lambda: cu_extract_for_new_ev(),
    lambda: xr.DataArray(
        0,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "MATERIALS_I": _subscript_dict["MATERIALS_I"],
        },
        ["REGIONS_35_I", "MATERIALS_I"],
    ),
    "_integ_cumulated_additional_cu_in_the_rest_of_electric_vehicles_respect_to_ice",
)


@component.add(
    name="cumulated_materials_extract_for_railway_catenaries",
    units="Mt",
    subscripts=["REGIONS_35_I", "MATERIALS_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_cumulated_materials_extract_for_railway_catenaries": 1},
    other_deps={
        "_integ_cumulated_materials_extract_for_railway_catenaries": {
            "initial": {},
            "step": {"materials_extract_for_new_railway_catenaries": 1},
        }
    },
)
def cumulated_materials_extract_for_railway_catenaries():
    """
    Cumulated extracted material to install the electrified railway .
    """
    return _integ_cumulated_materials_extract_for_railway_catenaries()


_integ_cumulated_materials_extract_for_railway_catenaries = Integ(
    lambda: materials_extract_for_new_railway_catenaries(),
    lambda: xr.DataArray(
        0,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "MATERIALS_I": _subscript_dict["MATERIALS_I"],
        },
        ["REGIONS_35_I", "MATERIALS_I"],
    ),
    "_integ_cumulated_materials_extract_for_railway_catenaries",
)


@component.add(
    name="cumulated_materials_req_chargers_and_additional_Cu_and_grids_to_chargers_and_catenary",
    units="Mt",
    subscripts=["REGIONS_35_I", "MATERIALS_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={
        "_integ_cumulated_materials_req_chargers_and_additional_cu_and_grids_to_chargers_and_catenary": 1
    },
    other_deps={
        "_integ_cumulated_materials_req_chargers_and_additional_cu_and_grids_to_chargers_and_catenary": {
            "initial": {},
            "step": {
                "materials_req_new_chargers_and_additional_cu_and_grids_to_chargers_and_catenary": 1
            },
        }
    },
)
def cumulated_materials_req_chargers_and_additional_cu_and_grids_to_chargers_and_catenary():
    """
    Cumulated required materials to install Ev chargers, grids, catenaries and the additional Cu of electrified vehicles.
    """
    return (
        _integ_cumulated_materials_req_chargers_and_additional_cu_and_grids_to_chargers_and_catenary()
    )


_integ_cumulated_materials_req_chargers_and_additional_cu_and_grids_to_chargers_and_catenary = Integ(
    lambda: materials_req_new_chargers_and_additional_cu_and_grids_to_chargers_and_catenary(),
    lambda: xr.DataArray(
        0,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "MATERIALS_I": _subscript_dict["MATERIALS_I"],
        },
        ["REGIONS_35_I", "MATERIALS_I"],
    ),
    "_integ_cumulated_materials_req_chargers_and_additional_cu_and_grids_to_chargers_and_catenary",
)


@component.add(
    name="cumulated_materials_req_chargers_and_additional_Cu_and_grids_to_chargers_from_2015",
    units="Mt",
    subscripts=["REGIONS_35_I", "MATERIALS_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={
        "_integ_cumulated_materials_req_chargers_and_additional_cu_and_grids_to_chargers_from_2015": 1
    },
    other_deps={
        "_integ_cumulated_materials_req_chargers_and_additional_cu_and_grids_to_chargers_from_2015": {
            "initial": {},
            "step": {
                "materials_req_new_chargers_and_additional_cu_and_grids_to_chargers_from_2015": 1
            },
        }
    },
)
def cumulated_materials_req_chargers_and_additional_cu_and_grids_to_chargers_from_2015():
    """
    Cumulated required materials to install Ev chargers, grids and the additional Cu of electrified vehicles.
    """
    return (
        _integ_cumulated_materials_req_chargers_and_additional_cu_and_grids_to_chargers_from_2015()
    )


_integ_cumulated_materials_req_chargers_and_additional_cu_and_grids_to_chargers_from_2015 = Integ(
    lambda: materials_req_new_chargers_and_additional_cu_and_grids_to_chargers_from_2015(),
    lambda: xr.DataArray(
        0,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "MATERIALS_I": _subscript_dict["MATERIALS_I"],
        },
        ["REGIONS_35_I", "MATERIALS_I"],
    ),
    "_integ_cumulated_materials_req_chargers_and_additional_cu_and_grids_to_chargers_from_2015",
)


@component.add(
    name="cumulated_materials_req_EV_batteries_from_2015",
    units="Mt",
    subscripts=["REGIONS_35_I", "MATERIALS_I", "EV_BATTERIES_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_cumulated_materials_req_ev_batteries_from_2015": 1},
    other_deps={
        "_integ_cumulated_materials_req_ev_batteries_from_2015": {
            "initial": {},
            "step": {"materials_req_for_ev_batteries_from_2015": 1},
        }
    },
)
def cumulated_materials_req_ev_batteries_from_2015():
    """
    Accumulated mineral requirements of EV batteries since 2015
    """
    return _integ_cumulated_materials_req_ev_batteries_from_2015()


_integ_cumulated_materials_req_ev_batteries_from_2015 = Integ(
    lambda: materials_req_for_ev_batteries_from_2015(),
    lambda: xr.DataArray(
        0,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "MATERIALS_I": _subscript_dict["MATERIALS_I"],
            "EV_BATTERIES_I": _subscript_dict["EV_BATTERIES_I"],
        },
        ["REGIONS_35_I", "MATERIALS_I", "EV_BATTERIES_I"],
    ),
    "_integ_cumulated_materials_req_ev_batteries_from_2015",
)


@component.add(
    name="cumulated_materials_requirements_for_EV_batteries_from_initial_year",
    units="Mt",
    subscripts=["REGIONS_35_I", "MATERIALS_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={
        "_integ_cumulated_materials_requirements_for_ev_batteries_from_initial_year": 1
    },
    other_deps={
        "_integ_cumulated_materials_requirements_for_ev_batteries_from_initial_year": {
            "initial": {},
            "step": {"materials_required_for_new_ev_batteries": 1},
        }
    },
)
def cumulated_materials_requirements_for_ev_batteries_from_initial_year():
    """
    Total cumulative materials requirements for EV batteries.
    """
    return _integ_cumulated_materials_requirements_for_ev_batteries_from_initial_year()


_integ_cumulated_materials_requirements_for_ev_batteries_from_initial_year = Integ(
    lambda: sum(
        materials_required_for_new_ev_batteries().rename(
            {"EV_BATTERIES_I": "EV_BATTERIES_I!"}
        ),
        dim=["EV_BATTERIES_I!"],
    ),
    lambda: xr.DataArray(
        0,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "MATERIALS_I": _subscript_dict["MATERIALS_I"],
        },
        ["REGIONS_35_I", "MATERIALS_I"],
    ),
    "_integ_cumulated_materials_requirements_for_ev_batteries_from_initial_year",
)


@component.add(
    name="cumulated_materials_to_extract_for_chargers_and_additional_Cu_and_grids_to_chargers_and_catenary",
    units="Mt",
    subscripts=["REGIONS_35_I", "MATERIALS_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={
        "_integ_cumulated_materials_to_extract_for_chargers_and_additional_cu_and_grids_to_chargers_and_catenary": 1
    },
    other_deps={
        "_integ_cumulated_materials_to_extract_for_chargers_and_additional_cu_and_grids_to_chargers_and_catenary": {
            "initial": {},
            "step": {
                "materials_to_extract_for_new_chargers_and_additional_cu_and_grids_to_chargers_and_catenary": 1
            },
        }
    },
)
def cumulated_materials_to_extract_for_chargers_and_additional_cu_and_grids_to_chargers_and_catenary():
    """
    Cumulated extracted materials to install Ev chargers, grids, catenaries and the additional Cu of electrified vehicles.
    """
    return (
        _integ_cumulated_materials_to_extract_for_chargers_and_additional_cu_and_grids_to_chargers_and_catenary()
    )


_integ_cumulated_materials_to_extract_for_chargers_and_additional_cu_and_grids_to_chargers_and_catenary = Integ(
    lambda: materials_to_extract_for_new_chargers_and_additional_cu_and_grids_to_chargers_and_catenary(),
    lambda: xr.DataArray(
        0,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "MATERIALS_I": _subscript_dict["MATERIALS_I"],
        },
        ["REGIONS_35_I", "MATERIALS_I"],
    ),
    "_integ_cumulated_materials_to_extract_for_chargers_and_additional_cu_and_grids_to_chargers_and_catenary",
)


@component.add(
    name="cumulated_materials_to_extract_for_chargers_and_additional_Cu_and_grids_to_chargers_and_catenary_from_2015",
    units="Mt",
    subscripts=["REGIONS_35_I", "MATERIALS_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={
        "_integ_cumulated_materials_to_extract_for_chargers_and_additional_cu_and_grids_to_chargers_and_catenary_from_2015": 1
    },
    other_deps={
        "_integ_cumulated_materials_to_extract_for_chargers_and_additional_cu_and_grids_to_chargers_and_catenary_from_2015": {
            "initial": {},
            "step": {
                "materials_to_extract_for_new_chargers_and_additional_cu_and_grids_to_chargers_and_catenary_from_2015": 1
            },
        }
    },
)
def cumulated_materials_to_extract_for_chargers_and_additional_cu_and_grids_to_chargers_and_catenary_from_2015():
    """
    Cumulated extracted materials to install Ev chargers, grids, catenaries and the additional Cu of electrified vehicles from 2015.
    """
    return (
        _integ_cumulated_materials_to_extract_for_chargers_and_additional_cu_and_grids_to_chargers_and_catenary_from_2015()
    )


_integ_cumulated_materials_to_extract_for_chargers_and_additional_cu_and_grids_to_chargers_and_catenary_from_2015 = Integ(
    lambda: materials_to_extract_for_new_chargers_and_additional_cu_and_grids_to_chargers_and_catenary_from_2015(),
    lambda: xr.DataArray(
        0,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "MATERIALS_I": _subscript_dict["MATERIALS_I"],
        },
        ["REGIONS_35_I", "MATERIALS_I"],
    ),
    "_integ_cumulated_materials_to_extract_for_chargers_and_additional_cu_and_grids_to_chargers_and_catenary_from_2015",
)


@component.add(
    name="cumulated_materials_to_extract_for_EV_batteries_from_2015",
    units="Mt",
    subscripts=["REGIONS_35_I", "MATERIALS_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_cumulated_materials_to_extract_for_ev_batteries_from_2015": 1},
    other_deps={
        "_integ_cumulated_materials_to_extract_for_ev_batteries_from_2015": {
            "initial": {},
            "step": {"total_materials_to_extract_for_new_ev_batteries_from_2015": 1},
        }
    },
)
def cumulated_materials_to_extract_for_ev_batteries_from_2015():
    """
    Cumulative materials to be mined for EV batteries.
    """
    return _integ_cumulated_materials_to_extract_for_ev_batteries_from_2015()


_integ_cumulated_materials_to_extract_for_ev_batteries_from_2015 = Integ(
    lambda: sum(
        total_materials_to_extract_for_new_ev_batteries_from_2015().rename(
            {"EV_BATTERIES_I": "EV_BATTERIES_I!"}
        ),
        dim=["EV_BATTERIES_I!"],
    ),
    lambda: xr.DataArray(
        0,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "MATERIALS_I": _subscript_dict["MATERIALS_I"],
        },
        ["REGIONS_35_I", "MATERIALS_I"],
    ),
    "_integ_cumulated_materials_to_extract_for_ev_batteries_from_2015",
)


@component.add(
    name="cumulated_materials_to_extract_for_EV_batteries_from_initial_year",
    units="Mt",
    subscripts=["REGIONS_35_I", "MATERIALS_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={
        "_integ_cumulated_materials_to_extract_for_ev_batteries_from_initial_year": 1
    },
    other_deps={
        "_integ_cumulated_materials_to_extract_for_ev_batteries_from_initial_year": {
            "initial": {},
            "step": {"total_materials_to_extract_for_new_ev_batteries": 1},
        }
    },
)
def cumulated_materials_to_extract_for_ev_batteries_from_initial_year():
    """
    Cumulative materials to be mined for EV batteries.
    """
    return _integ_cumulated_materials_to_extract_for_ev_batteries_from_initial_year()


_integ_cumulated_materials_to_extract_for_ev_batteries_from_initial_year = Integ(
    lambda: sum(
        total_materials_to_extract_for_new_ev_batteries().rename(
            {"EV_BATTERIES_I": "EV_BATTERIES_I!"}
        ),
        dim=["EV_BATTERIES_I!"],
    ),
    lambda: xr.DataArray(
        0,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "MATERIALS_I": _subscript_dict["MATERIALS_I"],
        },
        ["REGIONS_35_I", "MATERIALS_I"],
    ),
    "_integ_cumulated_materials_to_extract_for_ev_batteries_from_initial_year",
)


@component.add(
    name="cumulated_total_materials_to_extract_for_electrified_transport_from_2015",
    units="Mt",
    subscripts=["REGIONS_35_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cumulated_materials_to_extract_for_ev_batteries_from_2015": 1,
        "cumulated_materials_to_extract_for_chargers_and_additional_cu_and_grids_to_chargers_and_catenary_from_2015": 1,
    },
)
def cumulated_total_materials_to_extract_for_electrified_transport_from_2015():
    """
    Total cumulated materials required for electrify the transport from 2015
    """
    return (
        cumulated_materials_to_extract_for_ev_batteries_from_2015()
        + cumulated_materials_to_extract_for_chargers_and_additional_cu_and_grids_to_chargers_and_catenary_from_2015()
    )


@component.add(
    name="demand_Cu_of_the_vehicles_vs_reserves",
    units="DMNL",
    subscripts=["REGIONS_35_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cumulated_additional_cu_in_the_rest_of_electric_vehicles_respect_to_ice": 1,
        "global_mineral_reserves": 1,
    },
)
def demand_cu_of_the_vehicles_vs_reserves():
    """
    Cumulated of Cu extracted for Electric vehicles (without the battery) in relation to reserves
    """
    return zidz(
        cumulated_additional_cu_in_the_rest_of_electric_vehicles_respect_to_ice(),
        global_mineral_reserves().expand_dims(
            {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]}, 0
        ),
    )


@component.add(
    name="demand_Cu_of_the_vehicles_vs_resources",
    units="DMNL",
    subscripts=["REGIONS_35_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cumulated_additional_cu_in_the_rest_of_electric_vehicles_respect_to_ice": 1,
        "global_mineral_resources": 1,
    },
)
def demand_cu_of_the_vehicles_vs_resources():
    """
    Cumulated of Cu extracted for Electric vehicles (without the battery) in relation to resources
    """
    return zidz(
        cumulated_additional_cu_in_the_rest_of_electric_vehicles_respect_to_ice(),
        global_mineral_resources().expand_dims(
            {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]}, 0
        ),
    )


@component.add(
    name="demand_of_the_chargers_and_grids_vs_reserves",
    units="DMNL",
    subscripts=["REGIONS_35_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "global_mineral_reserves": 2,
        "cumulated_materials_to_extract_for_chargers_and_additional_cu_and_grids_to_chargers_and_catenary": 1,
        "cumulated_materials_extract_for_railway_catenaries": 1,
        "cumulated_additional_cu_in_the_rest_of_electric_vehicles_respect_to_ice": 1,
    },
)
def demand_of_the_chargers_and_grids_vs_reserves():
    """
    Cumulated of mineral extracted for chargers and grids of EV vehicles in relation to reserves
    """
    return if_then_else(
        (global_mineral_reserves() <= 0).expand_dims(
            {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]}, 1
        ),
        lambda: xr.DataArray(
            0,
            {
                "MATERIALS_I": _subscript_dict["MATERIALS_I"],
                "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            },
            ["MATERIALS_I", "REGIONS_35_I"],
        ),
        lambda: (
            (
                cumulated_materials_to_extract_for_chargers_and_additional_cu_and_grids_to_chargers_and_catenary()
                - cumulated_materials_extract_for_railway_catenaries()
                - cumulated_additional_cu_in_the_rest_of_electric_vehicles_respect_to_ice()
            )
            / global_mineral_reserves()
        ).transpose("MATERIALS_I", "REGIONS_35_I"),
    ).transpose("REGIONS_35_I", "MATERIALS_I")


@component.add(
    name="demand_of_the_chargers_and_grids_vs_resources",
    units="DMNL",
    subscripts=["REGIONS_35_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "global_mineral_resources": 2,
        "cumulated_materials_to_extract_for_chargers_and_additional_cu_and_grids_to_chargers_and_catenary": 1,
        "cumulated_materials_extract_for_railway_catenaries": 1,
        "cumulated_additional_cu_in_the_rest_of_electric_vehicles_respect_to_ice": 1,
    },
)
def demand_of_the_chargers_and_grids_vs_resources():
    """
    Cumulated of mineral extracted for chargers and grids of EV vehicles in relation to resources
    """
    return if_then_else(
        (global_mineral_resources() <= 0).expand_dims(
            {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]}, 1
        ),
        lambda: xr.DataArray(
            0,
            {
                "MATERIALS_I": _subscript_dict["MATERIALS_I"],
                "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            },
            ["MATERIALS_I", "REGIONS_35_I"],
        ),
        lambda: (
            (
                cumulated_materials_to_extract_for_chargers_and_additional_cu_and_grids_to_chargers_and_catenary()
                - cumulated_materials_extract_for_railway_catenaries()
                - cumulated_additional_cu_in_the_rest_of_electric_vehicles_respect_to_ice()
            )
            / global_mineral_resources()
        ).transpose("MATERIALS_I", "REGIONS_35_I"),
    ).transpose("REGIONS_35_I", "MATERIALS_I")


@component.add(
    name="demand_of_the_EV_batteries_vs_reserves",
    units="DMNL",
    subscripts=["REGIONS_35_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cumulated_materials_to_extract_for_ev_batteries_from_initial_year": 1,
        "global_mineral_reserves": 1,
    },
)
def demand_of_the_ev_batteries_vs_reserves():
    """
    Cumulated of mineral extracted for EV batteries in relation to reserves
    """
    return zidz(
        cumulated_materials_to_extract_for_ev_batteries_from_initial_year(),
        global_mineral_reserves().expand_dims(
            {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]}, 0
        ),
    )


@component.add(
    name="demand_of_the_EV_batteries_vs_resources",
    units="DMNL",
    subscripts=["REGIONS_35_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cumulated_materials_to_extract_for_ev_batteries_from_initial_year": 1,
        "global_mineral_resources": 1,
    },
)
def demand_of_the_ev_batteries_vs_resources():
    """
    Cumulated of mineral extracted for EV batteries in relation to resources
    """
    return zidz(
        cumulated_materials_to_extract_for_ev_batteries_from_initial_year(),
        global_mineral_resources().expand_dims(
            {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]}, 0
        ),
    )


@component.add(
    name="demand_of_the_railroad_vs_reserves",
    units="DMNL",
    subscripts=["REGIONS_35_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cumulated_materials_extract_for_railway_catenaries": 1,
        "global_mineral_reserves": 1,
    },
)
def demand_of_the_railroad_vs_reserves():
    """
    Cumulated of mineral extracted for railroads in relation to reserves
    """
    return zidz(
        cumulated_materials_extract_for_railway_catenaries(),
        global_mineral_reserves().expand_dims(
            {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]}, 0
        ),
    )


@component.add(
    name="demand_of_the_railroad_vs_resources",
    units="DMNL",
    subscripts=["REGIONS_35_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cumulated_materials_extract_for_railway_catenaries": 1,
        "global_mineral_resources": 1,
    },
)
def demand_of_the_railroad_vs_resources():
    """
    Cumulated of mineral extracted for railroads in relation to resources
    """
    return zidz(
        cumulated_materials_extract_for_railway_catenaries(),
        global_mineral_resources().expand_dims(
            {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]}, 0
        ),
    )


@component.add(
    name="MATERIAL_INTENSITY_EV_CHARGERS",
    units="kg/charger",
    subscripts=["MATERIALS_I", "EV_CHARGERS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "material_intensity_ev_home_charger": 2,
        "scrap_rate": 3,
        "material_intensity_ev_normal_charger": 2,
        "material_intensity_ev_quick_charger": 2,
    },
)
def material_intensity_ev_chargers():
    """
    Materials requirements of all types of EV charger .
    """
    value = xr.DataArray(
        np.nan,
        {
            "MATERIALS_I": _subscript_dict["MATERIALS_I"],
            "EV_CHARGERS_I": _subscript_dict["EV_CHARGERS_I"],
        },
        ["MATERIALS_I", "EV_CHARGERS_I"],
    )
    value.loc[:, ["home"]] = (
        (
            material_intensity_ev_home_charger()
            + scrap_rate() * material_intensity_ev_home_charger()
        )
        .expand_dims({"EV_CHARGERS_I": ["home"]}, 1)
        .values
    )
    value.loc[:, ["normal"]] = (
        (
            material_intensity_ev_normal_charger()
            + scrap_rate() * material_intensity_ev_normal_charger()
        )
        .expand_dims({"EV_CHARGERS_I": ["normal"]}, 1)
        .values
    )
    value.loc[:, ["quick"]] = (
        (
            material_intensity_ev_quick_charger()
            + scrap_rate() * material_intensity_ev_quick_charger()
        )
        .expand_dims({"EV_CHARGERS_I": ["quick"]}, 1)
        .values
    )
    return value


@component.add(
    name="MATERIAL_INTENSITY_GRIDS_EV_CHARGERS",
    units="kg/m",
    subscripts=["MATERIALS_I", "EV_CHARGERS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "material_intensity_ev_grid_to_charger_low_voltage": 2,
        "scrap_rate": 4,
        "material_intensity_ev_grid_to_charger_lowmedium_voltage": 2,
        "material_intensity_ev_grid_to_charger_medium_voltage": 2,
        "material_intensity_ev_grid_to_charger_high_voltage": 2,
    },
)
def material_intensity_grids_ev_chargers():
    """
    Materials requirements of all types of EV charger grid.
    """
    value = xr.DataArray(
        np.nan,
        {
            "MATERIALS_I": _subscript_dict["MATERIALS_I"],
            "EV_CHARGERS_I": _subscript_dict["EV_CHARGERS_I"],
        },
        ["MATERIALS_I", "EV_CHARGERS_I"],
    )
    value.loc[:, ["home"]] = (
        (
            material_intensity_ev_grid_to_charger_low_voltage()
            + scrap_rate() * material_intensity_ev_grid_to_charger_low_voltage()
        )
        .expand_dims({"EV_CHARGERS_I": ["home"]}, 1)
        .values
    )
    value.loc[:, ["normal"]] = (
        (
            material_intensity_ev_grid_to_charger_lowmedium_voltage()
            + scrap_rate() * material_intensity_ev_grid_to_charger_lowmedium_voltage()
        )
        .expand_dims({"EV_CHARGERS_I": ["normal"]}, 1)
        .values
    )
    value.loc[:, ["quick"]] = (
        (
            material_intensity_ev_grid_to_charger_medium_voltage()
            + scrap_rate() * material_intensity_ev_grid_to_charger_medium_voltage()
            + material_intensity_ev_grid_to_charger_high_voltage()
            + scrap_rate() * material_intensity_ev_grid_to_charger_high_voltage()
        )
        .expand_dims({"EV_CHARGERS_I": ["quick"]}, 1)
        .values
    )
    return value


@component.add(
    name="materials_extract_for_new_railway_catenaries",
    units="Mt/Year",
    subscripts=["REGIONS_35_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "materials_required_for_new_railway_catenaries": 2,
        "rc_rate_mineral_35r": 2,
        "cumulated_materials_extract_for_railway_catenaries": 2,
    },
)
def materials_extract_for_new_railway_catenaries():
    """
    Total extracted material to install the electrified railway .
    """
    return if_then_else(
        -materials_required_for_new_railway_catenaries() * (1 - rc_rate_mineral_35r())
        > cumulated_materials_extract_for_railway_catenaries(),
        lambda: cumulated_materials_extract_for_railway_catenaries(),
        lambda: materials_required_for_new_railway_catenaries()
        * (1 - rc_rate_mineral_35r()),
    )


@component.add(
    name="MATERIALS_PER_NEW_CAPACITY_INSTALLED_EV_BATTERIES",
    units="kg/MW",
    subscripts=["MATERIALS_I", "EV_BATTERIES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "materials_per_new_capacity_installed_ev_batteries_lmo": 1,
        "materials_per_new_capacity_installed_ev_batteries_nmc622": 1,
        "materials_per_new_capacity_installed_ev_batteries_nmc811": 1,
        "materials_per_new_capacity_installed_ev_batteries_nca": 1,
        "materials_per_new_capacity_installed_ev_batteries_lfp": 1,
    },
)
def materials_per_new_capacity_installed_ev_batteries():
    """
    10% of the mine's ore cost has been added to the manufactured product (scrap).
    """
    value = xr.DataArray(
        np.nan,
        {
            "MATERIALS_I": _subscript_dict["MATERIALS_I"],
            "EV_BATTERIES_I": _subscript_dict["EV_BATTERIES_I"],
        },
        ["MATERIALS_I", "EV_BATTERIES_I"],
    )
    value.loc[:, ["LMO"]] = (
        materials_per_new_capacity_installed_ev_batteries_lmo()
        .expand_dims({"EV_BATTERIES_I": ["LMO"]}, 1)
        .values
    )
    value.loc[:, ["NMC622"]] = (
        materials_per_new_capacity_installed_ev_batteries_nmc622()
        .expand_dims({"EV_BATTERIES_I": ["NMC622"]}, 1)
        .values
    )
    value.loc[:, ["NMC811"]] = (
        materials_per_new_capacity_installed_ev_batteries_nmc811()
        .expand_dims({"EV_BATTERIES_I": ["NMC811"]}, 1)
        .values
    )
    value.loc[:, ["NCA"]] = (
        materials_per_new_capacity_installed_ev_batteries_nca()
        .expand_dims({"EV_BATTERIES_I": ["NCA"]}, 1)
        .values
    )
    value.loc[:, ["LFP"]] = (
        materials_per_new_capacity_installed_ev_batteries_lfp()
        .expand_dims({"EV_BATTERIES_I": ["LFP"]}, 1)
        .values
    )
    return value


@component.add(
    name="materials_req_chargers_and_additional_Cu_and_grids_to_chargers_and_catenary_9R",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "materials_req_new_chargers_and_additional_cu_and_grids_to_chargers_and_catenary": 2
    },
)
def materials_req_chargers_and_additional_cu_and_grids_to_chargers_and_catenary_9r():
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "MATERIALS_I": _subscript_dict["MATERIALS_I"],
        },
        ["REGIONS_9_I", "MATERIALS_I"],
    )
    value.loc[["EU27"], :] = (
        sum(
            materials_req_new_chargers_and_additional_cu_and_grids_to_chargers_and_catenary()
            .loc[_subscript_dict["REGIONS_EU27_I"], :]
            .rename({"REGIONS_35_I": "REGIONS_EU27_I!"}),
            dim=["REGIONS_EU27_I!"],
        )
        .expand_dims({"REGIONS_36_I": ["EU27"]}, 0)
        .values
    )
    value.loc[_subscript_dict["REGIONS_8_I"], :] = (
        materials_req_new_chargers_and_additional_cu_and_grids_to_chargers_and_catenary()
        .loc[_subscript_dict["REGIONS_8_I"], :]
        .rename({"REGIONS_35_I": "REGIONS_8_I"})
        .values
    )
    return value


@component.add(
    name="materials_req_for_EV_batteries_from_2015",
    units="Mt/Year",
    subscripts=["REGIONS_35_I", "MATERIALS_I", "EV_BATTERIES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "materials_required_for_new_ev_batteries": 1},
)
def materials_req_for_ev_batteries_from_2015():
    """
    Materials requirements for EV batteries from 2015
    """
    return if_then_else(
        time() < 2015,
        lambda: xr.DataArray(
            0,
            {
                "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                "MATERIALS_I": _subscript_dict["MATERIALS_I"],
                "EV_BATTERIES_I": _subscript_dict["EV_BATTERIES_I"],
            },
            ["REGIONS_35_I", "MATERIALS_I", "EV_BATTERIES_I"],
        ),
        lambda: materials_required_for_new_ev_batteries(),
    )


@component.add(
    name="materials_req_new_chargers_and_additional_Cu_and_grids_to_chargers_and_catenary",
    units="Mt/Year",
    subscripts=["REGIONS_35_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "additional_cu_in_the_rest_of_ev_wrt_to_ice": 2,
        "materials_required_for_new_ev_chargers": 2,
        "materials_required_for_new_ev_chargers_grids": 2,
        "materials_required_for_new_railway_catenaries": 2,
        "cumulated_materials_req_chargers_and_additional_cu_and_grids_to_chargers_and_catenary": 2,
    },
)
def materials_req_new_chargers_and_additional_cu_and_grids_to_chargers_and_catenary():
    """
    Required materials to install Ev chargers, grids, catenaries and the additional Cu of electrified vehicles.
    """
    return if_then_else(
        -(
            additional_cu_in_the_rest_of_ev_wrt_to_ice()
            + materials_required_for_new_ev_chargers()
            + materials_required_for_new_ev_chargers_grids()
            + materials_required_for_new_railway_catenaries()
        )
        > cumulated_materials_req_chargers_and_additional_cu_and_grids_to_chargers_and_catenary(),
        lambda: -cumulated_materials_req_chargers_and_additional_cu_and_grids_to_chargers_and_catenary(),
        lambda: additional_cu_in_the_rest_of_ev_wrt_to_ice()
        + materials_required_for_new_ev_chargers()
        + materials_required_for_new_ev_chargers_grids()
        + materials_required_for_new_railway_catenaries(),
    )


@component.add(
    name="materials_req_new_chargers_and_additional_Cu_and_grids_to_chargers_from_2015",
    units="Mt/Year",
    subscripts=["REGIONS_35_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "additional_cu_in_the_rest_of_ev_wrt_to_ice": 1,
        "materials_required_for_new_ev_chargers_grids": 1,
        "materials_required_for_new_ev_chargers": 1,
    },
)
def materials_req_new_chargers_and_additional_cu_and_grids_to_chargers_from_2015():
    """
    Required materials to install Ev chargers, grids and the additional Cu of electrified vehicles.
    """
    return if_then_else(
        time() < 2015,
        lambda: xr.DataArray(
            0,
            {
                "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                "MATERIALS_I": _subscript_dict["MATERIALS_I"],
            },
            ["REGIONS_35_I", "MATERIALS_I"],
        ),
        lambda: additional_cu_in_the_rest_of_ev_wrt_to_ice()
        + materials_required_for_new_ev_chargers_grids()
        + materials_required_for_new_ev_chargers(),
    )


@component.add(
    name="materials_required_for_electric_transport_9R",
    units="Mt/Year",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "materials_required_for_ev_batteries_9r": 1,
        "materials_req_chargers_and_additional_cu_and_grids_to_chargers_and_catenary_9r": 1,
    },
)
def materials_required_for_electric_transport_9r():
    return (
        sum(
            materials_required_for_ev_batteries_9r().rename(
                {"EV_BATTERIES_I": "EV_BATTERIES_I!"}
            ),
            dim=["EV_BATTERIES_I!"],
        )
        + materials_req_chargers_and_additional_cu_and_grids_to_chargers_and_catenary_9r()
    )


@component.add(
    name="materials_required_for_EV_batteries_9R",
    units="Mt/Year",
    subscripts=["REGIONS_9_I", "MATERIALS_I", "EV_BATTERIES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"materials_required_for_new_ev_batteries": 2},
)
def materials_required_for_ev_batteries_9r():
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "MATERIALS_I": _subscript_dict["MATERIALS_I"],
            "EV_BATTERIES_I": _subscript_dict["EV_BATTERIES_I"],
        },
        ["REGIONS_9_I", "MATERIALS_I", "EV_BATTERIES_I"],
    )
    value.loc[["EU27"], :, :] = (
        sum(
            materials_required_for_new_ev_batteries()
            .loc[_subscript_dict["REGIONS_EU27_I"], :, :]
            .rename({"REGIONS_35_I": "REGIONS_EU27_I!"}),
            dim=["REGIONS_EU27_I!"],
        )
        .expand_dims({"REGIONS_36_I": ["EU27"]}, 0)
        .values
    )
    value.loc[_subscript_dict["REGIONS_8_I"], :, :] = (
        materials_required_for_new_ev_batteries()
        .loc[_subscript_dict["REGIONS_8_I"], :, :]
        .rename({"REGIONS_35_I": "REGIONS_8_I"})
        .values
    )
    return value


@component.add(
    name="materials_required_for_new_electric_transport",
    units="Mt",
    subscripts=["REGIONS_35_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "materials_required_for_new_ev_batteries": 1,
        "materials_req_new_chargers_and_additional_cu_and_grids_to_chargers_and_catenary": 1,
    },
)
def materials_required_for_new_electric_transport():
    """
    Total required materials for electrify the transport (including EV batteries and chargers, additional Cu and grids to chargers and railway catenary).
    """
    return (
        sum(
            materials_required_for_new_ev_batteries().rename(
                {"EV_BATTERIES_I": "EV_BATTERIES_I!"}
            ),
            dim=["EV_BATTERIES_I!"],
        )
        + materials_req_new_chargers_and_additional_cu_and_grids_to_chargers_and_catenary()
    )


@component.add(
    name="materials_required_for_new_EV_batteries",
    units="Mt/Year",
    subscripts=["REGIONS_35_I", "MATERIALS_I", "EV_BATTERIES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "power_new_vehicle_batteries_35r": 1,
        "materials_per_new_capacity_installed_ev_batteries": 1,
        "scrap_rate": 1,
        "unit_conversion_mw_tw": 1,
        "unit_conversion_kg_mt": 1,
    },
)
def materials_required_for_new_ev_batteries():
    """
    Annual materials required for the fabrication of EV batteries.
    """
    return (
        power_new_vehicle_batteries_35r()
        * materials_per_new_capacity_installed_ev_batteries().transpose(
            "EV_BATTERIES_I", "MATERIALS_I"
        )
        * (1 + scrap_rate())
        * unit_conversion_mw_tw()
        / unit_conversion_kg_mt()
    ).transpose("REGIONS_35_I", "MATERIALS_I", "EV_BATTERIES_I")


@component.add(
    name="materials_required_for_new_EV_chargers",
    units="Mt/Year",
    subscripts=["REGIONS_35_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_materials": 1,
        "material_intensity_ev_chargers": 1,
        "unit_conversion_kg_mt": 1,
        "number_new_ev_chargers": 1,
    },
)
def materials_required_for_new_ev_chargers():
    """
    Materials required for the construction of the EV chargers
    """
    return if_then_else(
        switch_materials() == 0,
        lambda: xr.DataArray(
            0,
            {
                "MATERIALS_I": _subscript_dict["MATERIALS_I"],
                "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            },
            ["MATERIALS_I", "REGIONS_35_I"],
        ),
        lambda: sum(
            material_intensity_ev_chargers().rename({"EV_CHARGERS_I": "EV_CHARGERS_I!"})
            * number_new_ev_chargers()
            .rename({"EV_CHARGERS_I": "EV_CHARGERS_I!"})
            .transpose("EV_CHARGERS_I!", "REGIONS_35_I"),
            dim=["EV_CHARGERS_I!"],
        )
        / unit_conversion_kg_mt(),
    ).transpose("REGIONS_35_I", "MATERIALS_I")


@component.add(
    name="materials_required_for_new_EV_chargers_grids",
    units="Mt/Year",
    subscripts=["REGIONS_35_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_materials": 1,
        "unit_conversion_km_m": 1,
        "material_intensity_grids_ev_chargers": 1,
        "unit_conversion_kg_mt": 1,
        "new_length_grid_to_ev_chargers": 1,
    },
)
def materials_required_for_new_ev_chargers_grids():
    """
    Total materials requirements of EV charger grid.
    """
    return if_then_else(
        switch_materials() == 0,
        lambda: xr.DataArray(
            0,
            {
                "MATERIALS_I": _subscript_dict["MATERIALS_I"],
                "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            },
            ["MATERIALS_I", "REGIONS_35_I"],
        ),
        lambda: sum(
            material_intensity_grids_ev_chargers().rename(
                {"EV_CHARGERS_I": "EV_CHARGERS_I!"}
            )
            * new_length_grid_to_ev_chargers()
            .rename({"EV_CHARGERS_I": "EV_CHARGERS_I!"})
            .transpose("EV_CHARGERS_I!", "REGIONS_35_I"),
            dim=["EV_CHARGERS_I!"],
        )
        / unit_conversion_kg_mt()
        / unit_conversion_km_m(),
    ).transpose("REGIONS_35_I", "MATERIALS_I")


@component.add(
    name="materials_required_for_new_railway_catenaries",
    units="Mt/Year",
    subscripts=["REGIONS_35_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_materials": 1,
        "unit_conversion_km_m": 2,
        "scrap_rate": 1,
        "unit_conversion_kg_mt": 2,
        "new_railway_catenary": 2,
        "material_intensity_catenary_railway": 2,
    },
)
def materials_required_for_new_railway_catenaries():
    """
    Total materials requirements of electrified railway .
    """
    return if_then_else(
        switch_materials() == 0,
        lambda: xr.DataArray(
            0,
            {
                "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                "MATERIALS_I": _subscript_dict["MATERIALS_I"],
            },
            ["REGIONS_35_I", "MATERIALS_I"],
        ),
        lambda: new_railway_catenary()
        * material_intensity_catenary_railway()
        / unit_conversion_kg_mt()
        / unit_conversion_km_m()
        + scrap_rate()
        * (
            new_railway_catenary()
            * material_intensity_catenary_railway()
            / unit_conversion_kg_mt()
            / unit_conversion_km_m()
        ),
    )


@component.add(
    name="materials_to_extract_for_new_chargers_and_additional_Cu_and_grids_to_chargers_and_catenary",
    units="Mt/Year",
    subscripts=["REGIONS_35_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "materials_req_new_chargers_and_additional_cu_and_grids_to_chargers_and_catenary": 1,
        "rc_rate_mineral_35r": 1,
    },
)
def materials_to_extract_for_new_chargers_and_additional_cu_and_grids_to_chargers_and_catenary():
    """
    Extracted materials to install Ev chargers, grids, catenaries and the additional Cu of electrified vehicles.
    """
    return materials_req_new_chargers_and_additional_cu_and_grids_to_chargers_and_catenary() * (
        1 - rc_rate_mineral_35r()
    )


@component.add(
    name="materials_to_extract_for_new_chargers_and_additional_Cu_and_grids_to_chargers_and_catenary_from_2015",
    units="Mt/Year",
    subscripts=["REGIONS_35_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "materials_to_extract_for_new_chargers_and_additional_cu_and_grids_to_chargers_and_catenary": 1,
    },
)
def materials_to_extract_for_new_chargers_and_additional_cu_and_grids_to_chargers_and_catenary_from_2015():
    """
    Materials extracted to install Ev chargers, grids, catenaries and the additional Cu of electrified vehicles from 2015.
    """
    return if_then_else(
        time() < 2015,
        lambda: xr.DataArray(
            0,
            {
                "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                "MATERIALS_I": _subscript_dict["MATERIALS_I"],
            },
            ["REGIONS_35_I", "MATERIALS_I"],
        ),
        lambda: materials_to_extract_for_new_chargers_and_additional_cu_and_grids_to_chargers_and_catenary(),
    )


@component.add(
    name="mineral_of_decom_batteries",
    units="Mt/Year",
    subscripts=["REGIONS_35_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_materials": 1,
        "unit_conversion_kg_mt": 1,
        "materials_per_new_capacity_installed_ev_batteries": 1,
        "unit_conversion_mw_tw": 1,
        "power_discarded_vehicle_batteries": 1,
    },
)
def mineral_of_decom_batteries():
    """
    Total annual materials of decom EV batteries.
    """
    return if_then_else(
        switch_materials() == 0,
        lambda: xr.DataArray(
            0,
            {
                "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                "MATERIALS_I": _subscript_dict["MATERIALS_I"],
            },
            ["REGIONS_35_I", "MATERIALS_I"],
        ),
        lambda: sum(
            power_discarded_vehicle_batteries().rename(
                {"EV_BATTERIES_I": "EV_BATTERIES_I!"}
            )
            * materials_per_new_capacity_installed_ev_batteries()
            .rename({"EV_BATTERIES_I": "EV_BATTERIES_I!"})
            .transpose("EV_BATTERIES_I!", "MATERIALS_I"),
            dim=["EV_BATTERIES_I!"],
        )
        * unit_conversion_mw_tw()
        / unit_conversion_kg_mt(),
    )


@component.add(
    name="mineral_of_decom_batteries_9R",
    units="Mt/Year",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"mineral_of_decom_batteries": 2},
)
def mineral_of_decom_batteries_9r():
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "MATERIALS_I": _subscript_dict["MATERIALS_I"],
        },
        ["REGIONS_9_I", "MATERIALS_I"],
    )
    value.loc[["EU27"], :] = (
        sum(
            mineral_of_decom_batteries()
            .loc[_subscript_dict["REGIONS_EU27_I"], :]
            .rename({"REGIONS_35_I": "REGIONS_EU27_I!"}),
            dim=["REGIONS_EU27_I!"],
        )
        .expand_dims({"REGIONS_36_I": ["EU27"]}, 0)
        .values
    )
    value.loc[_subscript_dict["REGIONS_8_I"], :] = (
        mineral_of_decom_batteries()
        .loc[_subscript_dict["REGIONS_8_I"], :]
        .rename({"REGIONS_35_I": "REGIONS_8_I"})
        .values
    )
    return value


@component.add(
    name="mineral_Stock_EV_batteries",
    units="Mt",
    subscripts=["REGIONS_35_I", "MATERIALS_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_mineral_stock_ev_batteries": 1},
    other_deps={
        "_integ_mineral_stock_ev_batteries": {
            "initial": {},
            "step": {
                "minerals_supply_for_new_electric_batteries": 1,
                "mineral_of_decom_batteries": 1,
            },
        }
    },
)
def mineral_stock_ev_batteries():
    """
    Minerals stock of EV batteries
    """
    return _integ_mineral_stock_ev_batteries()


_integ_mineral_stock_ev_batteries = Integ(
    lambda: minerals_supply_for_new_electric_batteries() - mineral_of_decom_batteries(),
    lambda: xr.DataArray(
        0,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "MATERIALS_I": _subscript_dict["MATERIALS_I"],
        },
        ["REGIONS_35_I", "MATERIALS_I"],
    ),
    "_integ_mineral_stock_ev_batteries",
)


@component.add(
    name="minerals_supply_for_new_electric_batteries",
    units="Mt/Year",
    subscripts=["REGIONS_35_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"materials_required_for_new_ev_batteries": 1},
)
def minerals_supply_for_new_electric_batteries():
    """
    Total annual materials requirements for EV batteries.
    """
    return sum(
        materials_required_for_new_ev_batteries().rename(
            {"EV_BATTERIES_I": "EV_BATTERIES_I!"}
        ),
        dim=["EV_BATTERIES_I!"],
    )


@component.add(
    name="RC_rate_mineral_35R",
    subscripts=["REGIONS_35_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"rc_rate_mineral": 2},
)
def rc_rate_mineral_35r():
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "MATERIALS_I": _subscript_dict["MATERIALS_I"],
        },
        ["REGIONS_35_I", "MATERIALS_I"],
    )
    value.loc[_subscript_dict["REGIONS_8_I"], :] = (
        rc_rate_mineral()
        .loc[_subscript_dict["REGIONS_8_I"], :]
        .rename({"REGIONS_9_I": "REGIONS_8_I"})
        .values
    )
    value.loc[_subscript_dict["REGIONS_EU27_I"], :] = (
        rc_rate_mineral()
        .loc["EU27", :]
        .reset_coords(drop=True)
        .expand_dims({"REGIONS_EU27_I": _subscript_dict["REGIONS_EU27_I"]}, 0)
        .values
    )
    return value


@component.add(
    name="RELATIVE_DEMAND_OF_MINERAL_BY_EV_BATTERY",
    units="DMNL",
    subscripts=["MATERIALS_I", "EV_BATTERIES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "materials_per_new_capacity_installed_ev_batteries_lmo": 6,
        "materials_per_new_capacity_installed_ev_batteries_nca": 6,
        "materials_per_new_capacity_installed_ev_batteries_lfp": 6,
        "materials_per_new_capacity_installed_ev_batteries_nmc622": 6,
        "materials_per_new_capacity_installed_ev_batteries_nmc811": 6,
    },
)
def relative_demand_of_mineral_by_ev_battery():
    """
    relative demand of mineral by battery; demand of mineral i by battery l /demand of mineral i by all the batteries
    """
    value = xr.DataArray(
        np.nan,
        {
            "MATERIALS_I": _subscript_dict["MATERIALS_I"],
            "EV_BATTERIES_I": _subscript_dict["EV_BATTERIES_I"],
        },
        ["MATERIALS_I", "EV_BATTERIES_I"],
    )
    value.loc[:, ["LMO"]] = (
        zidz(
            materials_per_new_capacity_installed_ev_batteries_lmo(),
            materials_per_new_capacity_installed_ev_batteries_lmo()
            + materials_per_new_capacity_installed_ev_batteries_nmc622()
            + materials_per_new_capacity_installed_ev_batteries_nmc811()
            + materials_per_new_capacity_installed_ev_batteries_nca()
            + materials_per_new_capacity_installed_ev_batteries_lfp(),
        )
        .expand_dims({"EV_BATTERIES_I": ["LMO"]}, 1)
        .values
    )
    value.loc[:, ["NMC622"]] = (
        zidz(
            materials_per_new_capacity_installed_ev_batteries_nmc622(),
            materials_per_new_capacity_installed_ev_batteries_lmo()
            + materials_per_new_capacity_installed_ev_batteries_nmc622()
            + materials_per_new_capacity_installed_ev_batteries_nmc811()
            + materials_per_new_capacity_installed_ev_batteries_nca()
            + materials_per_new_capacity_installed_ev_batteries_lfp(),
        )
        .expand_dims({"EV_BATTERIES_I": ["NMC622"]}, 1)
        .values
    )
    value.loc[:, ["NMC811"]] = (
        zidz(
            materials_per_new_capacity_installed_ev_batteries_nmc811(),
            materials_per_new_capacity_installed_ev_batteries_lmo()
            + materials_per_new_capacity_installed_ev_batteries_nmc622()
            + materials_per_new_capacity_installed_ev_batteries_nmc811()
            + materials_per_new_capacity_installed_ev_batteries_nca()
            + materials_per_new_capacity_installed_ev_batteries_lfp(),
        )
        .expand_dims({"EV_BATTERIES_I": ["NMC811"]}, 1)
        .values
    )
    value.loc[:, ["NCA"]] = (
        zidz(
            materials_per_new_capacity_installed_ev_batteries_nca(),
            materials_per_new_capacity_installed_ev_batteries_lmo()
            + materials_per_new_capacity_installed_ev_batteries_nmc622()
            + materials_per_new_capacity_installed_ev_batteries_nmc811()
            + materials_per_new_capacity_installed_ev_batteries_nca()
            + materials_per_new_capacity_installed_ev_batteries_lfp(),
        )
        .expand_dims({"EV_BATTERIES_I": ["NCA"]}, 1)
        .values
    )
    value.loc[:, ["LFP"]] = (
        zidz(
            materials_per_new_capacity_installed_ev_batteries_lfp(),
            materials_per_new_capacity_installed_ev_batteries_lmo()
            + materials_per_new_capacity_installed_ev_batteries_nmc622()
            + materials_per_new_capacity_installed_ev_batteries_nmc811()
            + materials_per_new_capacity_installed_ev_batteries_nca()
            + materials_per_new_capacity_installed_ev_batteries_lfp(),
        )
        .expand_dims({"EV_BATTERIES_I": ["LFP"]}, 1)
        .values
    )
    return value


@component.add(
    name="total_materials_required_for_new_EV_chargers_and_grids",
    units="Mt/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "materials_required_for_new_ev_chargers": 1,
        "materials_required_for_new_ev_chargers_grids": 1,
    },
)
def total_materials_required_for_new_ev_chargers_and_grids():
    """
    weight of materials required for the infrastructure of EV
    """
    return sum(
        materials_required_for_new_ev_chargers().rename(
            {"MATERIALS_I": "MATERIALS_I!"}
        ),
        dim=["MATERIALS_I!"],
    ) + sum(
        materials_required_for_new_ev_chargers_grids().rename(
            {"MATERIALS_I": "MATERIALS_I!"}
        ),
        dim=["MATERIALS_I!"],
    )


@component.add(
    name="total_materials_required_for_new_EV_chargers_and_grids_without_cement",
    units="Mt/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "materials_required_for_new_ev_chargers": 2,
        "materials_required_for_new_ev_chargers_grids": 2,
    },
)
def total_materials_required_for_new_ev_chargers_and_grids_without_cement():
    """
    weight of materials required for the infrastructure of electric vehicles without taking account cement
    """
    return (
        sum(
            materials_required_for_new_ev_chargers().rename(
                {"MATERIALS_I": "MATERIALS_I!"}
            ),
            dim=["MATERIALS_I!"],
        )
        + sum(
            materials_required_for_new_ev_chargers_grids().rename(
                {"MATERIALS_I": "MATERIALS_I!"}
            ),
            dim=["MATERIALS_I!"],
        )
        - materials_required_for_new_ev_chargers()
        .loc[:, "Cement"]
        .reset_coords(drop=True)
        - materials_required_for_new_ev_chargers_grids()
        .loc[:, "Cement"]
        .reset_coords(drop=True)
    )


@component.add(
    name="total_materials_to_extract_for_electric_transport",
    units="Mt/Year",
    subscripts=["REGIONS_35_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "total_materials_to_extract_for_new_ev_batteries": 1,
        "materials_to_extract_for_new_chargers_and_additional_cu_and_grids_to_chargers_and_catenary": 1,
    },
)
def total_materials_to_extract_for_electric_transport():
    """
    Total extracted materials to electrify the transport (including EV batteries and chargers, additional Cu and grids to chargers and railway catenary)
    """
    return (
        sum(
            total_materials_to_extract_for_new_ev_batteries().rename(
                {"EV_BATTERIES_I": "EV_BATTERIES_I!"}
            ),
            dim=["EV_BATTERIES_I!"],
        )
        + materials_to_extract_for_new_chargers_and_additional_cu_and_grids_to_chargers_and_catenary()
    )


@component.add(
    name="total_materials_to_extract_for_electric_transport_9R",
    units="Mt/Year",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_materials_to_extract_for_electric_transport": 2},
)
def total_materials_to_extract_for_electric_transport_9r():
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "MATERIALS_I": _subscript_dict["MATERIALS_I"],
        },
        ["REGIONS_9_I", "MATERIALS_I"],
    )
    value.loc[["EU27"], :] = (
        sum(
            total_materials_to_extract_for_electric_transport()
            .loc[_subscript_dict["REGIONS_EU27_I"], :]
            .rename({"REGIONS_35_I": "REGIONS_EU27_I!"}),
            dim=["REGIONS_EU27_I!"],
        )
        .expand_dims({"REGIONS_36_I": ["EU27"]}, 0)
        .values
    )
    value.loc[_subscript_dict["REGIONS_8_I"], :] = (
        total_materials_to_extract_for_electric_transport()
        .loc[_subscript_dict["REGIONS_8_I"], :]
        .rename({"REGIONS_35_I": "REGIONS_8_I"})
        .values
    )
    return value


@component.add(
    name="total_materials_to_extract_for_new_EV_batteries",
    units="Mt/Year",
    subscripts=["REGIONS_35_I", "MATERIALS_I", "EV_BATTERIES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"materials_required_for_new_ev_batteries": 1, "rc_rate_mineral_35r": 1},
)
def total_materials_to_extract_for_new_ev_batteries():
    """
    Annual materials to be mined for the construction of EV batteries.
    """
    return materials_required_for_new_ev_batteries() * (1 - rc_rate_mineral_35r())


@component.add(
    name="total_materials_to_extract_for_new_EV_batteries_from_2015",
    units="Mt/Year",
    subscripts=["REGIONS_35_I", "MATERIALS_I", "EV_BATTERIES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "total_materials_to_extract_for_new_ev_batteries": 1},
)
def total_materials_to_extract_for_new_ev_batteries_from_2015():
    """
    Annual materials to be mined for EV batteries from 2015.
    """
    return if_then_else(
        time() < 2015,
        lambda: xr.DataArray(
            0,
            {
                "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                "MATERIALS_I": _subscript_dict["MATERIALS_I"],
                "EV_BATTERIES_I": _subscript_dict["EV_BATTERIES_I"],
            },
            ["REGIONS_35_I", "MATERIALS_I", "EV_BATTERIES_I"],
        ),
        lambda: total_materials_to_extract_for_new_ev_batteries(),
    )


@component.add(
    name="total_recycled_materials_for_chargers_and_additional_Cu_and_grids_to_chargers_and_catenary",
    units="Mt/Year",
    subscripts=["REGIONS_35_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "materials_req_new_chargers_and_additional_cu_and_grids_to_chargers_and_catenary": 1,
        "materials_to_extract_for_new_chargers_and_additional_cu_and_grids_to_chargers_and_catenary": 1,
    },
)
def total_recycled_materials_for_chargers_and_additional_cu_and_grids_to_chargers_and_catenary():
    """
    Recycled materials to install Ev chargers, grids, catenaries and the additional Cu of electrified vehicles.
    """
    return (
        materials_req_new_chargers_and_additional_cu_and_grids_to_chargers_and_catenary()
        - materials_to_extract_for_new_chargers_and_additional_cu_and_grids_to_chargers_and_catenary()
    )


@component.add(
    name="total_recycled_materials_for_new_EV_batteries",
    units="Mt/Year",
    subscripts=["REGIONS_35_I", "MATERIALS_I", "EV_BATTERIES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "materials_required_for_new_ev_batteries": 1,
        "total_materials_to_extract_for_new_ev_batteries": 1,
    },
)
def total_recycled_materials_for_new_ev_batteries():
    """
    Total recycled materials for EV batteries.
    """
    return (
        materials_required_for_new_ev_batteries()
        - total_materials_to_extract_for_new_ev_batteries()
    )
