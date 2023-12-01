"""
Module energy.end_use.transport.ev.capacity_and_power
Translated using PySD version 3.10.0
"""


@component.add(
    name="CAPACITY_EV",
    units="kW*h/(cycle*vehicle)",
    subscripts=["TRANSPORT_POWER_TRAIN_I", "BATTERY_VEHICLES_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_capacity_ev"},
)
def capacity_ev():
    """
    Capacity storage of EV batteries by vehicle.
    """
    return _ext_constant_capacity_ev()


_ext_constant_capacity_ev = ExtConstant(
    "model_parameters/energy/energy-transport.xlsx",
    "electrified_transport",
    "VEHICLE_ELECTRIC_CAPACITY",
    {
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "BATTERY_VEHICLES_I": _subscript_dict["BATTERY_VEHICLES_I"],
    },
    _root,
    {
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "BATTERY_VEHICLES_I": _subscript_dict["BATTERY_VEHICLES_I"],
    },
    "_ext_constant_capacity_ev",
)


@component.add(
    name="discarded_transport_electrified_vehicle_batteries_capacity",
    units="TW*h/(Year*cycle)",
    subscripts=[
        "REGIONS_35_I",
        "EV_BATTERIES_I",
        "TRANSPORT_POWER_TRAIN_I",
        "BATTERY_VEHICLES_I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "transport_electrified_vehicle_batteries_capacity": 1,
        "lifetime_electrified_vehicle_batteries": 1,
    },
)
def discarded_transport_electrified_vehicle_batteries_capacity():
    """
    Electrical capacity discarded from the transport system by electrified vehicles by battery type
    """
    return np.maximum(
        0,
        zidz(
            transport_electrified_vehicle_batteries_capacity(),
            lifetime_electrified_vehicle_batteries(),
        ),
    )


@component.add(
    name="discarded_transport_electrified_vehicle_batteries_power",
    units="TW/Year",
    subscripts=[
        "REGIONS_35_I",
        "EV_BATTERIES_I",
        "TRANSPORT_POWER_TRAIN_I",
        "BATTERY_VEHICLES_I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "transport_electrified_vehicle_batteries_power": 1,
        "lifetime_electrified_vehicle_batteries": 1,
    },
)
def discarded_transport_electrified_vehicle_batteries_power():
    """
    Electrical power discarded from the transport system by electrified vehicles by battery type
    """
    return np.maximum(
        0,
        zidz(
            transport_electrified_vehicle_batteries_power(),
            lifetime_electrified_vehicle_batteries(),
        ),
    )


@component.add(
    name="electrified_vehicles_power_by_battery_type",
    units="TW",
    subscripts=["REGIONS_35_I", "EV_BATTERIES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"transport_electrified_vehicle_batteries_power": 1},
)
def electrified_vehicles_power_by_battery_type():
    """
    Total electrified vehicles (Ebike + EV + Hyb vehicle) power per type of battery.
    """
    return sum(
        transport_electrified_vehicle_batteries_power().rename(
            {
                "TRANSPORT_POWER_TRAIN_I": "TRANSPORT_POWER_TRAIN_I!",
                "BATTERY_VEHICLES_I": "BATTERY_VEHICLES_I!",
            }
        ),
        dim=["TRANSPORT_POWER_TRAIN_I!", "BATTERY_VEHICLES_I!"],
    )


@component.add(
    name="EV_batteries_capacity_required",
    units="TW*h/cycle",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "total_number_ev_vehicles": 1,
        "capacity_ev": 1,
        "unit_conversion_kwh_twh": 1,
    },
)
def ev_batteries_capacity_required():
    """
    Total battery capacity required for the Electric vehicles over the years
    """
    return (
        sum(
            total_number_ev_vehicles().rename(
                {
                    "TRANSPORT_POWER_TRAIN_I": "TRANSPORT_POWER_TRAIN_I!",
                    "BATTERY_VEHICLES_I": "BATTERY_VEHICLES_I!",
                }
            )
            * capacity_ev().rename(
                {
                    "TRANSPORT_POWER_TRAIN_I": "TRANSPORT_POWER_TRAIN_I!",
                    "BATTERY_VEHICLES_I": "BATTERY_VEHICLES_I!",
                }
            ),
            dim=["TRANSPORT_POWER_TRAIN_I!", "BATTERY_VEHICLES_I!"],
        )
        / unit_conversion_kwh_twh()
    )


@component.add(
    name="EV_batteries_power",
    units="TW",
    subscripts=["REGIONS_35_I", "EV_BATTERIES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"transport_electrified_vehicle_batteries_power": 1},
)
def ev_batteries_power():
    """
    Electric batteries from electric vehicles, expresed in terms of power available (TW)
    """
    return sum(
        transport_electrified_vehicle_batteries_power().rename(
            {
                "TRANSPORT_POWER_TRAIN_I": "TRANSPORT_POWER_TRAIN_I!",
                "BATTERY_VEHICLES_I": "BATTERY_VEHICLES_I!",
            }
        ),
        dim=["TRANSPORT_POWER_TRAIN_I!", "BATTERY_VEHICLES_I!"],
    )


@component.add(
    name="EV_batteries_power_SC",
    units="TW",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ev_batteries_power": 1, "smart_charging_share_ev_vehicles": 1},
)
def ev_batteries_power_sc():
    """
    EV batteries power for Smart Charging (ebike are assumed not to be available due to their small battery size).
    """
    return (
        sum(
            ev_batteries_power().rename({"EV_BATTERIES_I": "EV_BATTERIES_I!"}),
            dim=["EV_BATTERIES_I!"],
        )
        * smart_charging_share_ev_vehicles()
    )


@component.add(
    name="EV_batteries_power_V2G",
    units="TW",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ev_batteries_power": 1, "v2g_share_ev_vehicles": 1},
)
def ev_batteries_power_v2g():
    """
    EV batteries power for V2G (ebike are assumed not to be available due to their small battery size).
    """
    return (
        sum(
            ev_batteries_power().rename({"EV_BATTERIES_I": "EV_BATTERIES_I!"}),
            dim=["EV_BATTERIES_I!"],
        )
        * v2g_share_ev_vehicles()
    )


@component.add(
    name="EV_batteries_power_V2G_9R",
    units="TW",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ev_batteries_power_v2g": 2},
)
def ev_batteries_power_v2g_9r():
    value = xr.DataArray(
        np.nan, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
    )
    value.loc[["EU27"]] = sum(
        ev_batteries_power_v2g()
        .loc[_subscript_dict["REGIONS_EU27_I"]]
        .rename({"REGIONS_35_I": "REGIONS_EU27_I!"}),
        dim=["REGIONS_EU27_I!"],
    )
    value.loc[_subscript_dict["REGIONS_8_I"]] = (
        ev_batteries_power_v2g()
        .loc[_subscript_dict["REGIONS_8_I"]]
        .rename({"REGIONS_35_I": "REGIONS_8_I"})
        .values
    )
    return value


@component.add(
    name="EV_vehicles_batteries_power_required",
    units="TW",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "total_number_ev_vehicles": 1,
        "vehicle_electric_power": 1,
        "unit_conversion_tw_kw": 1,
        "batteries_per_ev_vehicle": 1,
    },
)
def ev_vehicles_batteries_power_required():
    """
    Total battery power required for the Electric vehicles over the years
    """
    return (
        sum(
            total_number_ev_vehicles().rename(
                {
                    "TRANSPORT_POWER_TRAIN_I": "TRANSPORT_POWER_TRAIN_I!",
                    "BATTERY_VEHICLES_I": "BATTERY_VEHICLES_I!",
                }
            )
            * vehicle_electric_power().rename(
                {
                    "TRANSPORT_POWER_TRAIN_I": "TRANSPORT_POWER_TRAIN_I!",
                    "BATTERY_VEHICLES_I": "BATTERY_VEHICLES_I!",
                }
            ),
            dim=["TRANSPORT_POWER_TRAIN_I!", "BATTERY_VEHICLES_I!"],
        )
        * unit_conversion_tw_kw()
        * batteries_per_ev_vehicle()
    )


@component.add(
    name="HEV_batteries_capacity_required",
    units="TW*h/cycle",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "total_number_electrified_vehicles": 1,
        "capacity_ev": 1,
        "unit_conversion_kwh_twh": 1,
    },
)
def hev_batteries_capacity_required():
    """
    Total battery capacity required for the hybrid vehicles over the years
    """
    return (
        sum(
            total_number_electrified_vehicles()
            .loc[:, :, _subscript_dict["BATTERY_VEHICLES_I"]]
            .rename(
                {
                    "TRANSPORT_POWER_TRAIN_I": "TRANSPORT_POWER_TRAIN_I!",
                    "TRANSPORT_MODE_I": "BATTERY_VEHICLES_I!",
                }
            )
            * capacity_ev().rename(
                {
                    "TRANSPORT_POWER_TRAIN_I": "TRANSPORT_POWER_TRAIN_I!",
                    "BATTERY_VEHICLES_I": "BATTERY_VEHICLES_I!",
                }
            ),
            dim=["TRANSPORT_POWER_TRAIN_I!", "BATTERY_VEHICLES_I!"],
        )
        / unit_conversion_kwh_twh()
    )


@component.add(
    name="HEV_vehicles_batteries_power_required",
    units="TW",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "total_number_electrified_vehicles": 1,
        "vehicle_electric_power": 1,
        "unit_conversion_tw_kw": 1,
        "batteries_per_ev_vehicle": 1,
    },
)
def hev_vehicles_batteries_power_required():
    """
    Total battery power required for the power vehicles over the years
    """
    return (
        sum(
            total_number_electrified_vehicles()
            .loc[:, :, _subscript_dict["BATTERY_VEHICLES_I"]]
            .rename(
                {
                    "TRANSPORT_POWER_TRAIN_I": "TRANSPORT_POWER_TRAIN_I!",
                    "TRANSPORT_MODE_I": "BATTERY_VEHICLES_I!",
                }
            )
            * vehicle_electric_power().rename(
                {
                    "TRANSPORT_POWER_TRAIN_I": "TRANSPORT_POWER_TRAIN_I!",
                    "BATTERY_VEHICLES_I": "BATTERY_VEHICLES_I!",
                }
            ),
            dim=["TRANSPORT_POWER_TRAIN_I!", "BATTERY_VEHICLES_I!"],
        )
        * unit_conversion_tw_kw()
        * batteries_per_ev_vehicle()
    )


@component.add(
    name="new_transport_electried_vehicle_batteries_capacity",
    units="TW*h/(Year*cycle)",
    subscripts=[
        "REGIONS_35_I",
        "EV_BATTERIES_I",
        "TRANSPORT_POWER_TRAIN_I",
        "BATTERY_VEHICLES_I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "capacity_ev": 1,
        "total_number_electrified_vehicles": 1,
        "unit_conversion_kwh_twh": 1,
        "one_year": 2,
        "transport_electrified_vehicle_batteries_capacity": 1,
        "discarded_transport_electrified_vehicle_batteries_capacity": 1,
        "share_of_new_ev_subtechn_batteries": 1,
    },
)
def new_transport_electried_vehicle_batteries_capacity():
    """
    Electric capacity fed into the transport system by hybrid commercial vehicles by battery type
    """
    return (
        (
            np.maximum(
                0,
                capacity_ev()
                * total_number_electrified_vehicles()
                .loc[:, :, _subscript_dict["BATTERY_VEHICLES_I"]]
                .rename({"TRANSPORT_MODE_I": "BATTERY_VEHICLES_I"})
                .transpose(
                    "TRANSPORT_POWER_TRAIN_I", "BATTERY_VEHICLES_I", "REGIONS_35_I"
                )
                / unit_conversion_kwh_twh()
                / one_year()
                - (
                    sum(
                        transport_electrified_vehicle_batteries_capacity().rename(
                            {"EV_BATTERIES_I": "EV_BATTERIES_I!"}
                        ),
                        dim=["EV_BATTERIES_I!"],
                    )
                    / one_year()
                ).transpose(
                    "TRANSPORT_POWER_TRAIN_I", "BATTERY_VEHICLES_I", "REGIONS_35_I"
                ),
            )
            + sum(
                discarded_transport_electrified_vehicle_batteries_capacity().rename(
                    {"EV_BATTERIES_I": "EV_BATTERIES_I!"}
                ),
                dim=["EV_BATTERIES_I!"],
            ).transpose("TRANSPORT_POWER_TRAIN_I", "BATTERY_VEHICLES_I", "REGIONS_35_I")
        )
        * share_of_new_ev_subtechn_batteries().transpose(
            "TRANSPORT_POWER_TRAIN_I",
            "BATTERY_VEHICLES_I",
            "REGIONS_35_I",
            "EV_BATTERIES_I",
        )
    ).transpose(
        "REGIONS_35_I",
        "EV_BATTERIES_I",
        "TRANSPORT_POWER_TRAIN_I",
        "BATTERY_VEHICLES_I",
    )


@component.add(
    name="new_transport_electrified_vehicle_batteries_power",
    units="TW/Year",
    subscripts=[
        "REGIONS_35_I",
        "EV_BATTERIES_I",
        "TRANSPORT_POWER_TRAIN_I",
        "BATTERY_VEHICLES_I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "vehicle_electric_power": 1,
        "total_number_electrified_vehicles": 1,
        "one_year": 2,
        "unit_conversion_tw_kw": 1,
        "batteries_per_ev_vehicle": 1,
        "transport_electrified_vehicle_batteries_power": 1,
        "discarded_transport_electrified_vehicle_batteries_power": 1,
        "share_of_new_ev_subtechn_batteries": 1,
    },
)
def new_transport_electrified_vehicle_batteries_power():
    """
    Electric power fed into the transport system by electrified vehicles by battery type
    """
    return (
        (
            np.maximum(
                0,
                vehicle_electric_power()
                * total_number_electrified_vehicles()
                .loc[:, :, _subscript_dict["BATTERY_VEHICLES_I"]]
                .rename({"TRANSPORT_MODE_I": "BATTERY_VEHICLES_I"})
                .transpose(
                    "TRANSPORT_POWER_TRAIN_I", "BATTERY_VEHICLES_I", "REGIONS_35_I"
                )
                / one_year()
                * unit_conversion_tw_kw()
                * batteries_per_ev_vehicle()
                - (
                    sum(
                        transport_electrified_vehicle_batteries_power().rename(
                            {"EV_BATTERIES_I": "EV_BATTERIES_I!"}
                        ),
                        dim=["EV_BATTERIES_I!"],
                    )
                    / one_year()
                ).transpose(
                    "TRANSPORT_POWER_TRAIN_I", "BATTERY_VEHICLES_I", "REGIONS_35_I"
                ),
            )
            + sum(
                discarded_transport_electrified_vehicle_batteries_power().rename(
                    {"EV_BATTERIES_I": "EV_BATTERIES_I!"}
                ),
                dim=["EV_BATTERIES_I!"],
            ).transpose("TRANSPORT_POWER_TRAIN_I", "BATTERY_VEHICLES_I", "REGIONS_35_I")
        )
        * share_of_new_ev_subtechn_batteries().transpose(
            "TRANSPORT_POWER_TRAIN_I",
            "BATTERY_VEHICLES_I",
            "REGIONS_35_I",
            "EV_BATTERIES_I",
        )
    ).transpose(
        "REGIONS_35_I",
        "EV_BATTERIES_I",
        "TRANSPORT_POWER_TRAIN_I",
        "BATTERY_VEHICLES_I",
    )


@component.add(
    name="power_discarded_batteries_9R",
    units="TW/Year",
    subscripts=["REGIONS_9_I", "EV_BATTERIES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"power_discarded_vehicle_batteries": 2},
)
def power_discarded_batteries_9r():
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "EV_BATTERIES_I": _subscript_dict["EV_BATTERIES_I"],
        },
        ["REGIONS_9_I", "EV_BATTERIES_I"],
    )
    value.loc[["EU27"], :] = (
        sum(
            power_discarded_vehicle_batteries()
            .loc[_subscript_dict["REGIONS_EU27_I"], :]
            .rename({"REGIONS_35_I": "REGIONS_EU27_I!"}),
            dim=["REGIONS_EU27_I!"],
        )
        .expand_dims({"REGIONS_36_I": ["EU27"]}, 0)
        .values
    )
    value.loc[_subscript_dict["REGIONS_8_I"], :] = (
        power_discarded_vehicle_batteries()
        .loc[_subscript_dict["REGIONS_8_I"], :]
        .rename({"REGIONS_35_I": "REGIONS_8_I"})
        .values
    )
    return value


@component.add(
    name="power_discarded_vehicle_batteries",
    units="TW/Year",
    subscripts=["REGIONS_35_I", "EV_BATTERIES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"discarded_transport_electrified_vehicle_batteries_power": 1},
)
def power_discarded_vehicle_batteries():
    """
    Capacity of discarded electric batteries.
    """
    return sum(
        discarded_transport_electrified_vehicle_batteries_power().rename(
            {
                "TRANSPORT_POWER_TRAIN_I": "TRANSPORT_POWER_TRAIN_I!",
                "BATTERY_VEHICLES_I": "BATTERY_VEHICLES_I!",
            }
        ),
        dim=["TRANSPORT_POWER_TRAIN_I!", "BATTERY_VEHICLES_I!"],
    )


@component.add(
    name="power_new_vehicle_batteries_35R",
    units="TW/Year",
    subscripts=["REGIONS_35_I", "EV_BATTERIES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"new_transport_electrified_vehicle_batteries_power": 3},
)
def power_new_vehicle_batteries_35r():
    """
    Capacity of new and replaced electric batteries.
    """
    return (
        sum(
            new_transport_electrified_vehicle_batteries_power().rename(
                {
                    "TRANSPORT_POWER_TRAIN_I": "TRANSPORT_POWER_TRAIN_I!",
                    "BATTERY_VEHICLES_I": "BATTERY_VEHICLES_I!",
                }
            ),
            dim=["TRANSPORT_POWER_TRAIN_I!", "BATTERY_VEHICLES_I!"],
        )
        + sum(
            new_transport_electrified_vehicle_batteries_power().rename(
                {
                    "TRANSPORT_POWER_TRAIN_I": "TRANSPORT_POWER_TRAIN_I!",
                    "BATTERY_VEHICLES_I": "BATTERY_VEHICLES_I!",
                }
            ),
            dim=["TRANSPORT_POWER_TRAIN_I!", "BATTERY_VEHICLES_I!"],
        )
        + sum(
            new_transport_electrified_vehicle_batteries_power().rename(
                {
                    "TRANSPORT_POWER_TRAIN_I": "TRANSPORT_POWER_TRAIN_I!",
                    "BATTERY_VEHICLES_I": "BATTERY_VEHICLES_I!",
                }
            ),
            dim=["TRANSPORT_POWER_TRAIN_I!", "BATTERY_VEHICLES_I!"],
        )
    )


@component.add(
    name="share_of_EV_batteries",
    units="DMNL",
    subscripts=["REGIONS_35_I", "EV_BATTERIES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_ev_vehicles_batteries_capacity": 2},
)
def share_of_ev_batteries():
    """
    Share of EV batteries in the EV vehicles.
    """
    return zidz(
        total_ev_vehicles_batteries_capacity(),
        sum(
            total_ev_vehicles_batteries_capacity().rename(
                {"EV_BATTERIES_I": "EV_BATTERIES_I!"}
            ),
            dim=["EV_BATTERIES_I!"],
        ).expand_dims({"EV_BATTERIES_I": _subscript_dict["EV_BATTERIES_I"]}, 1),
    )


@component.add(
    name="total_electrified_vehicles_batteries_power_required",
    units="TW",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "ev_vehicles_batteries_power_required": 1,
        "hev_vehicles_batteries_power_required": 1,
    },
)
def total_electrified_vehicles_batteries_power_required():
    """
    Total power required for electrified vehicles (EV + hybrid).
    """
    return (
        ev_vehicles_batteries_power_required() + hev_vehicles_batteries_power_required()
    )


@component.add(
    name="total_EV_vehicles_batteries_capacity",
    units="TW*h/cycle",
    subscripts=["REGIONS_35_I", "EV_BATTERIES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"transport_electrified_vehicle_batteries_capacity": 1},
)
def total_ev_vehicles_batteries_capacity():
    """
    Total capacity of EV batteries in the BEV vehicles.
    """
    return sum(
        transport_electrified_vehicle_batteries_capacity().rename(
            {
                "TRANSPORT_POWER_TRAIN_I": "TRANSPORT_POWER_TRAIN_I!",
                "BATTERY_VEHICLES_I": "BATTERY_VEHICLES_I!",
            }
        ),
        dim=["TRANSPORT_POWER_TRAIN_I!", "BATTERY_VEHICLES_I!"],
    )


@component.add(
    name="transport_electrified_vehicle_batteries_capacity",
    units="TW*h/cycle",
    subscripts=[
        "REGIONS_35_I",
        "EV_BATTERIES_I",
        "TRANSPORT_POWER_TRAIN_I",
        "BATTERY_VEHICLES_I",
    ],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_transport_electrified_vehicle_batteries_capacity": 1},
    other_deps={
        "_integ_transport_electrified_vehicle_batteries_capacity": {
            "initial": {},
            "step": {
                "new_transport_electried_vehicle_batteries_capacity": 1,
                "discarded_transport_electrified_vehicle_batteries_capacity": 1,
            },
        }
    },
)
def transport_electrified_vehicle_batteries_capacity():
    """
    Electric capacity in the transport system by electrified vehicles by battery type
    """
    return _integ_transport_electrified_vehicle_batteries_capacity()


_integ_transport_electrified_vehicle_batteries_capacity = Integ(
    lambda: new_transport_electried_vehicle_batteries_capacity()
    - discarded_transport_electrified_vehicle_batteries_capacity(),
    lambda: xr.DataArray(
        0,
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
    ),
    "_integ_transport_electrified_vehicle_batteries_capacity",
)


@component.add(
    name="transport_electrified_vehicle_batteries_power",
    units="TW",
    subscripts=[
        "REGIONS_35_I",
        "EV_BATTERIES_I",
        "TRANSPORT_POWER_TRAIN_I",
        "BATTERY_VEHICLES_I",
    ],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_transport_electrified_vehicle_batteries_power": 1},
    other_deps={
        "_integ_transport_electrified_vehicle_batteries_power": {
            "initial": {},
            "step": {
                "new_transport_electrified_vehicle_batteries_power": 1,
                "discarded_transport_electrified_vehicle_batteries_power": 1,
            },
        }
    },
)
def transport_electrified_vehicle_batteries_power():
    """
    Electric power in the transport system by electrified vehicles by battery type
    """
    return _integ_transport_electrified_vehicle_batteries_power()


_integ_transport_electrified_vehicle_batteries_power = Integ(
    lambda: new_transport_electrified_vehicle_batteries_power()
    - discarded_transport_electrified_vehicle_batteries_power(),
    lambda: xr.DataArray(
        0,
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
    ),
    "_integ_transport_electrified_vehicle_batteries_power",
)
