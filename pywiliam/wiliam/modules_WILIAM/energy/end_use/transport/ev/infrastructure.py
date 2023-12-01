"""
Module energy.end_use.transport.ev.infrastructure
Translated using PySD version 3.10.0
"""


@component.add(
    name="capacity_EV_chargers",
    units="TW",
    subscripts=["REGIONS_35_I", "EV_CHARGERS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "capacity_per_ev_charger": 1,
        "number_ev_chargers_by_type": 1,
        "unit_conversion_tw_kw": 1,
    },
)
def capacity_ev_chargers():
    """
    Total capacity in MW of the different types of EVchargers installed
    """
    return (
        capacity_per_ev_charger()
        * number_ev_chargers_by_type().transpose("EV_CHARGERS_I", "REGIONS_35_I")
        * unit_conversion_tw_kw()
    ).transpose("REGIONS_35_I", "EV_CHARGERS_I")


@component.add(
    name="length_grid_to_EV_chargers",
    units="km",
    subscripts=["REGIONS_35_I", "EV_CHARGERS_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_length_grid_to_ev_chargers": 1},
    other_deps={
        "_integ_length_grid_to_ev_chargers": {
            "initial": {"initial_length_electric_grid_to_connect_ev_chargers": 1},
            "step": {
                "new_length_grid_to_ev_chargers": 1,
                "wear_length_grid_to_ev_chargers": 1,
            },
        }
    },
)
def length_grid_to_ev_chargers():
    """
    Temporaly evolution of the km of electric grid to connect the EV chargers per type of EV charger
    """
    return _integ_length_grid_to_ev_chargers()


_integ_length_grid_to_ev_chargers = Integ(
    lambda: new_length_grid_to_ev_chargers() - wear_length_grid_to_ev_chargers(),
    lambda: initial_length_electric_grid_to_connect_ev_chargers().expand_dims(
        {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]}, 0
    ),
    "_integ_length_grid_to_ev_chargers",
)


@component.add(
    name="new_length_grid_to_EV_chargers",
    units="km/Year",
    subscripts=["REGIONS_35_I", "EV_CHARGERS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "length_electric_grid_to_connect_ev_chargers": 1,
        "number_ev_chargers_by_type": 1,
        "unit_conversion_km_m": 1,
        "length_grid_to_ev_chargers": 1,
        "one_year": 1,
    },
)
def new_length_grid_to_ev_chargers():
    """
    New km of the grids to connect the EV chargers per type of EV charger
    """
    return (
        (
            length_electric_grid_to_connect_ev_chargers()
            * number_ev_chargers_by_type().transpose("EV_CHARGERS_I", "REGIONS_35_I")
            * unit_conversion_km_m()
            - length_grid_to_ev_chargers().transpose("EV_CHARGERS_I", "REGIONS_35_I")
        )
        / one_year()
    ).transpose("REGIONS_35_I", "EV_CHARGERS_I")


@component.add(
    name="number_EV_chargers_by_type",
    units="chargers",
    subscripts=["REGIONS_35_I", "EV_CHARGERS_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_number_ev_chargers_by_type": 1},
    other_deps={
        "_integ_number_ev_chargers_by_type": {
            "initial": {"initial_number_ev_chargers_by_type": 1},
            "step": {"number_new_ev_chargers": 1, "number_wear_ev_chargers": 1},
        }
    },
)
def number_ev_chargers_by_type():
    """
    Temporal evolution of the number of different types EV chargers
    """
    return _integ_number_ev_chargers_by_type()


_integ_number_ev_chargers_by_type = Integ(
    lambda: number_new_ev_chargers() - number_wear_ev_chargers(),
    lambda: initial_number_ev_chargers_by_type().expand_dims(
        {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]}, 0
    ),
    "_integ_number_ev_chargers_by_type",
)


@component.add(
    name="number_new_EV_chargers",
    units="chargers/Year",
    subscripts=["REGIONS_35_I", "EV_CHARGERS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "number_chargers_per_type_of_vehicle": 1,
        "total_number_ev_vehicles": 1,
        "number_ev_chargers_by_type": 1,
        "one_year": 1,
    },
)
def number_new_ev_chargers():
    """
    New EV chargers to install
    """
    return (
        (
            sum(
                number_chargers_per_type_of_vehicle().rename(
                    {
                        "TRANSPORT_POWER_TRAIN_I": "TRANSPORT_POWER_TRAIN_I!",
                        "BATTERY_VEHICLES_I": "BATTERY_VEHICLES_I!",
                    }
                )
                * total_number_ev_vehicles()
                .rename(
                    {
                        "TRANSPORT_POWER_TRAIN_I": "TRANSPORT_POWER_TRAIN_I!",
                        "BATTERY_VEHICLES_I": "BATTERY_VEHICLES_I!",
                    }
                )
                .transpose(
                    "TRANSPORT_POWER_TRAIN_I!", "BATTERY_VEHICLES_I!", "REGIONS_35_I"
                ),
                dim=["TRANSPORT_POWER_TRAIN_I!", "BATTERY_VEHICLES_I!"],
            )
            - number_ev_chargers_by_type().transpose("EV_CHARGERS_I", "REGIONS_35_I")
        )
        / one_year()
    ).transpose("REGIONS_35_I", "EV_CHARGERS_I")


@component.add(
    name="number_wear_EV_chargers",
    units="chargers/Year",
    subscripts=["REGIONS_35_I", "EV_CHARGERS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"number_ev_chargers_by_type": 1, "lifetime_ev_chargers": 1},
)
def number_wear_ev_chargers():
    """
    Wear EV chargers to uninstall
    """
    return number_ev_chargers_by_type() / lifetime_ev_chargers()


@component.add(
    name="ratio_capacity_EV_batteries_vs_capacity_chargers",
    units="DMNL",
    subscripts=["REGIONS_35_I", "EV_BATTERIES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ev_batteries_power": 1, "total_capacity_ev_chargers": 1},
)
def ratio_capacity_ev_batteries_vs_capacity_chargers():
    """
    Ratio between battery and charger capacities
    """
    return zidz(
        ev_batteries_power(),
        total_capacity_ev_chargers().expand_dims(
            {"EV_BATTERIES_I": _subscript_dict["EV_BATTERIES_I"]}, 1
        ),
    )


@component.add(
    name="total_capacity_EV_chargers",
    units="TW",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"capacity_ev_chargers": 1},
)
def total_capacity_ev_chargers():
    """
    Total capacity in MW of EVchargers installed
    """
    return sum(
        capacity_ev_chargers().rename({"EV_CHARGERS_I": "EV_CHARGERS_I!"}),
        dim=["EV_CHARGERS_I!"],
    )


@component.add(
    name="total_length_grid_to_EV_chargers",
    units="km",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"length_grid_to_ev_chargers": 1},
)
def total_length_grid_to_ev_chargers():
    """
    Total km of electric grid to connect the EV chargers
    """
    return sum(
        length_grid_to_ev_chargers().rename({"EV_CHARGERS_I": "EV_CHARGERS_I!"}),
        dim=["EV_CHARGERS_I!"],
    )


@component.add(
    name="wear_length_grid_to_EV_chargers",
    units="km/Year",
    subscripts=["REGIONS_35_I", "EV_CHARGERS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "length_grid_to_ev_chargers": 1,
        "lifetime_electric_grid_to_connect_ev_chargers": 1,
    },
)
def wear_length_grid_to_ev_chargers():
    """
    Wear km of the grids to connect the EV chargers per type of EV charger
    """
    return (
        length_grid_to_ev_chargers() / lifetime_electric_grid_to_connect_ev_chargers()
    )
