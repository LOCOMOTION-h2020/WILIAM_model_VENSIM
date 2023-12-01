"""
Module energy.end_use.transport.ev.cf_and_lifetime
Translated using PySD version 3.10.0
"""


@component.add(
    name="average_power_electrified_vehicle_used",
    units="w/batteries",
    subscripts=[
        "REGIONS_35_I",
        "EV_BATTERIES_I",
        "TRANSPORT_POWER_TRAIN_I",
        "BATTERY_VEHICLES_I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "energy_delivered_by_electrified_vehicles_battery": 1,
        "unit_conversion_j_mj": 1,
        "unit_conversion_j_wh": 1,
        "unit_conversion_hours_year": 1,
        "max_lifetime_ev_batteries": 1,
    },
)
def average_power_electrified_vehicle_used():
    """
    Average power delivered by the electrified vehicles battery over its lifetime
    """
    return (
        energy_delivered_by_electrified_vehicles_battery()
        * unit_conversion_j_mj()
        / unit_conversion_j_wh()
        / (max_lifetime_ev_batteries() * unit_conversion_hours_year())
    )


@component.add(
    name="average_power_EV_vehicle_used_for_transport",
    units="w/batteries",
    subscripts=["EV_BATTERIES_I", "TRANSPORT_POWER_TRAIN_I", "BATTERY_VEHICLES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "energy_delivered_by_ev_battery_for_transport": 1,
        "unit_conversion_j_mj": 1,
        "unit_conversion_j_wh": 1,
        "unit_conversion_hours_year": 1,
        "max_lifetime_ev_batteries": 1,
    },
)
def average_power_ev_vehicle_used_for_transport():
    """
    Average power delivered by the electric household vehicle battery over its lifetime only for transport
    """
    return (
        energy_delivered_by_ev_battery_for_transport()
        * unit_conversion_j_mj()
        / unit_conversion_j_wh()
        / (max_lifetime_ev_batteries() * unit_conversion_hours_year())
    ).transpose("EV_BATTERIES_I", "TRANSPORT_POWER_TRAIN_I", "BATTERY_VEHICLES_I")


@component.add(
    name="CF_electrified_vehicle",
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
        "average_power_electrified_vehicle_used": 1,
        "unit_conversion_w_kw": 1,
        "vehicle_electric_power": 1,
    },
)
def cf_electrified_vehicle():
    """
    capacity factor of a electrified vehicle battery
    """
    return zidz(
        zidz(average_power_electrified_vehicle_used(), unit_conversion_w_kw()),
        vehicle_electric_power()
        .expand_dims({"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]}, 0)
        .expand_dims({"EV_BATTERIES_I": _subscript_dict["EV_BATTERIES_I"]}, 1),
    )


@component.add(
    name="CF_EV_vehicle_for_transport",
    units="DMNL",
    subscripts=["EV_BATTERIES_I", "TRANSPORT_POWER_TRAIN_I", "BATTERY_VEHICLES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "average_power_ev_vehicle_used_for_transport": 1,
        "unit_conversion_w_kw": 1,
        "vehicle_electric_power": 1,
    },
)
def cf_ev_vehicle_for_transport():
    """
    capacity factor of a electric household vehicle battery only for transport
    """
    return zidz(
        zidz(average_power_ev_vehicle_used_for_transport(), unit_conversion_w_kw()),
        vehicle_electric_power().expand_dims(
            {"EV_BATTERIES_I": _subscript_dict["EV_BATTERIES_I"]}, 0
        ),
    )


@component.add(
    name="energy_delivered_by_electrified_vehicles_battery",
    units="MJ/batteries",
    subscripts=[
        "REGIONS_35_I",
        "EV_BATTERIES_I",
        "TRANSPORT_POWER_TRAIN_I",
        "BATTERY_VEHICLES_I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cycles_electrified_vehicles_for_mobility": 1,
        "cycles_for_elec_storage_and_supply_the_grid_of_ev_battery": 1,
        "battery_wear_factor": 1,
        "capacity_ev": 1,
        "batteries_per_ev_vehicle": 1,
        "unit_converison_wh_kwh": 1,
        "unit_conversion_j_wh": 1,
        "unit_conversion_j_mj": 1,
    },
)
def energy_delivered_by_electrified_vehicles_battery():
    """
    Energy delivered by the electrified vehicles battery over its lifetime
    """
    return (
        (
            cycles_electrified_vehicles_for_mobility()
            + cycles_for_elec_storage_and_supply_the_grid_of_ev_battery().transpose(
                "TRANSPORT_POWER_TRAIN_I",
                "BATTERY_VEHICLES_I",
                "REGIONS_35_I",
                "EV_BATTERIES_I",
            )
        )
        / (1 + battery_wear_factor())
        * capacity_ev()
        / batteries_per_ev_vehicle()
        * unit_converison_wh_kwh()
        * unit_conversion_j_wh()
        / unit_conversion_j_mj()
    ).transpose(
        "REGIONS_35_I",
        "EV_BATTERIES_I",
        "TRANSPORT_POWER_TRAIN_I",
        "BATTERY_VEHICLES_I",
    )


@component.add(
    name="energy_delivered_by_EV_battery_for_transport",
    units="MJ/batteries",
    subscripts=["TRANSPORT_POWER_TRAIN_I", "BATTERY_VEHICLES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cycles_electrified_vehicles_for_mobility": 1,
        "battery_wear_factor": 1,
        "capacity_ev": 1,
        "batteries_per_ev_vehicle": 1,
        "unit_converison_wh_kwh": 1,
        "unit_conversion_j_wh": 1,
        "unit_conversion_j_mj": 1,
    },
)
def energy_delivered_by_ev_battery_for_transport():
    """
    Energy delivered by the electric household vehicle battery over its lifetime only for transport
    """
    return (
        cycles_electrified_vehicles_for_mobility()
        / (1 + battery_wear_factor())
        * capacity_ev()
        / batteries_per_ev_vehicle()
        * unit_converison_wh_kwh()
        * unit_conversion_j_wh()
        / unit_conversion_j_mj()
    )


@component.add(
    name="lifetime_electrified_vehicle_batteries",
    units="Year",
    subscripts=[
        "REGIONS_35_I",
        "EV_BATTERIES_I",
        "TRANSPORT_POWER_TRAIN_I",
        "BATTERY_VEHICLES_I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "energy_delivered_by_electrified_vehicles_battery": 1,
        "unit_conversion_j_mj": 1,
        "unit_conversion_j_wh": 1,
        "unit_converison_wh_kwh": 1,
        "unit_conversion_hours_year": 1,
        "vehicle_electric_power": 1,
        "cf_electrified_vehicle": 1,
        "max_lifetime_ev_batteries": 1,
    },
)
def lifetime_electrified_vehicle_batteries():
    """
    Lifetime of electrified vehicle batteries. Minimum value between the lifetime of a battery given by its self-degradation (MAX_LIFETIME_EV_BATTERIES), and the maximum number of cycles due to its total use (both for mobility and as V2G option).
    """
    return np.minimum(
        zidz(
            zidz(
                zidz(
                    zidz(
                        energy_delivered_by_electrified_vehicles_battery()
                        * unit_conversion_j_mj(),
                        unit_conversion_j_wh(),
                    ),
                    unit_converison_wh_kwh(),
                ),
                unit_conversion_hours_year(),
            ),
            cf_electrified_vehicle() * vehicle_electric_power(),
        ),
        max_lifetime_ev_batteries(),
    )
