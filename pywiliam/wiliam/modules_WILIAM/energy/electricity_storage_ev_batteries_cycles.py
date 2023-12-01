"""
Module energy.electricity_storage_ev_batteries_cycles
Translated using PySD version 3.10.0
"""


@component.add(
    name="capacity_charge_vehicles_with_SC",
    units="TW*h/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cf_ev_vehicle_for_transport": 4,
        "transport_electrified_vehicle_batteries_power": 4,
        "unit_conversion_hours_year": 4,
        "smart_charging_share_ev_vehicles": 1,
    },
)
def capacity_charge_vehicles_with_sc():
    """
    Energy to recharge smart charging vehicles in a year
    """
    return (
        sum(
            cf_ev_vehicle_for_transport()
            .loc[:, "BEV", "LDV"]
            .reset_coords(drop=True)
            .rename({"EV_BATTERIES_I": "EV_BATTERIES_I!"})
            * transport_electrified_vehicle_batteries_power()
            .loc[:, :, "BEV", "LDV"]
            .reset_coords(drop=True)
            .rename({"EV_BATTERIES_I": "EV_BATTERIES_I!"})
            .transpose("EV_BATTERIES_I!", "REGIONS_35_I")
            * unit_conversion_hours_year(),
            dim=["EV_BATTERIES_I!"],
        )
        + sum(
            cf_ev_vehicle_for_transport()
            .loc[:, "BEV", "MOTORCYCLES_2W_3W"]
            .reset_coords(drop=True)
            .rename({"EV_BATTERIES_I": "EV_BATTERIES_I!"})
            * transport_electrified_vehicle_batteries_power()
            .loc[:, :, "BEV", "MOTORCYCLES_2W_3W"]
            .reset_coords(drop=True)
            .rename({"EV_BATTERIES_I": "EV_BATTERIES_I!"})
            .transpose("EV_BATTERIES_I!", "REGIONS_35_I")
            * unit_conversion_hours_year(),
            dim=["EV_BATTERIES_I!"],
        )
        + sum(
            cf_ev_vehicle_for_transport()
            .loc[:, "BEV", "MDV"]
            .reset_coords(drop=True)
            .rename({"EV_BATTERIES_I": "EV_BATTERIES_I!"})
            * transport_electrified_vehicle_batteries_power()
            .loc[:, :, "BEV", "MDV"]
            .reset_coords(drop=True)
            .rename({"EV_BATTERIES_I": "EV_BATTERIES_I!"})
            .transpose("EV_BATTERIES_I!", "REGIONS_35_I")
            * unit_conversion_hours_year(),
            dim=["EV_BATTERIES_I!"],
        )
        + sum(
            cf_ev_vehicle_for_transport()
            .loc[:, "BEV", "bus"]
            .reset_coords(drop=True)
            .rename({"EV_BATTERIES_I": "EV_BATTERIES_I!"})
            * transport_electrified_vehicle_batteries_power()
            .loc[:, :, "BEV", "bus"]
            .reset_coords(drop=True)
            .rename({"EV_BATTERIES_I": "EV_BATTERIES_I!"})
            .transpose("EV_BATTERIES_I!", "REGIONS_35_I")
            * unit_conversion_hours_year(),
            dim=["EV_BATTERIES_I!"],
        )
    ) * smart_charging_share_ev_vehicles()


@component.add(
    name="capacity_charge_vehicles_without_SC",
    units="TW*h/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cf_ev_vehicle_for_transport": 4,
        "transport_electrified_vehicle_batteries_power": 4,
        "unit_conversion_hours_year": 4,
        "smart_charging_share_ev_vehicles": 1,
    },
)
def capacity_charge_vehicles_without_sc():
    """
    Energy to recharge normal vehicles
    """
    return (
        sum(
            cf_ev_vehicle_for_transport()
            .loc[:, "BEV", "LDV"]
            .reset_coords(drop=True)
            .rename({"EV_BATTERIES_I": "EV_BATTERIES_I!"})
            * transport_electrified_vehicle_batteries_power()
            .loc[:, :, "BEV", "LDV"]
            .reset_coords(drop=True)
            .rename({"EV_BATTERIES_I": "EV_BATTERIES_I!"})
            .transpose("EV_BATTERIES_I!", "REGIONS_35_I")
            * unit_conversion_hours_year(),
            dim=["EV_BATTERIES_I!"],
        )
        + sum(
            cf_ev_vehicle_for_transport()
            .loc[:, "BEV", "MOTORCYCLES_2W_3W"]
            .reset_coords(drop=True)
            .rename({"EV_BATTERIES_I": "EV_BATTERIES_I!"})
            * transport_electrified_vehicle_batteries_power()
            .loc[:, :, "BEV", "MOTORCYCLES_2W_3W"]
            .reset_coords(drop=True)
            .rename({"EV_BATTERIES_I": "EV_BATTERIES_I!"})
            .transpose("EV_BATTERIES_I!", "REGIONS_35_I")
            * unit_conversion_hours_year(),
            dim=["EV_BATTERIES_I!"],
        )
        + sum(
            cf_ev_vehicle_for_transport()
            .loc[:, "BEV", "MDV"]
            .reset_coords(drop=True)
            .rename({"EV_BATTERIES_I": "EV_BATTERIES_I!"})
            * transport_electrified_vehicle_batteries_power()
            .loc[:, :, "BEV", "MDV"]
            .reset_coords(drop=True)
            .rename({"EV_BATTERIES_I": "EV_BATTERIES_I!"})
            .transpose("EV_BATTERIES_I!", "REGIONS_35_I")
            * unit_conversion_hours_year(),
            dim=["EV_BATTERIES_I!"],
        )
        + sum(
            cf_ev_vehicle_for_transport()
            .loc[:, "BEV", "bus"]
            .reset_coords(drop=True)
            .rename({"EV_BATTERIES_I": "EV_BATTERIES_I!"})
            * transport_electrified_vehicle_batteries_power()
            .loc[:, :, "BEV", "bus"]
            .reset_coords(drop=True)
            .rename({"EV_BATTERIES_I": "EV_BATTERIES_I!"})
            .transpose("EV_BATTERIES_I!", "REGIONS_35_I")
            * unit_conversion_hours_year(),
            dim=["EV_BATTERIES_I!"],
        )
    ) * (1 - smart_charging_share_ev_vehicles())


@component.add(
    name="CF_max_EV_vehicle_battery_for_elec_storage",
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
        "cycles_max_for_elec_storage_ev_vehicles": 1,
        "cycles_electrified_vehicles_for_mobility": 1,
        "cf_ev_vehicle_for_transport": 1,
        "v2g_share_ev_vehicles": 1,
    },
)
def cf_max_ev_vehicle_battery_for_elec_storage():
    """
    CF max of EV Household vehicle battery for electricity storage
    """
    return (
        zidz(
            cycles_max_for_elec_storage_ev_vehicles(),
            cycles_electrified_vehicles_for_mobility(),
        )
        * cf_ev_vehicle_for_transport().transpose(
            "TRANSPORT_POWER_TRAIN_I", "BATTERY_VEHICLES_I", "EV_BATTERIES_I"
        )
        * v2g_share_ev_vehicles()
    ).transpose(
        "REGIONS_35_I",
        "EV_BATTERIES_I",
        "TRANSPORT_POWER_TRAIN_I",
        "BATTERY_VEHICLES_I",
    )


@component.add(
    name="cycles_electrified_vehicles_for_mobility",
    units="cycle",
    subscripts=["TRANSPORT_POWER_TRAIN_I", "BATTERY_VEHICLES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "mileage_vehicles": 2,
        "autonomy_ev_vehicles": 2,
        "battery_wear_factor": 1,
    },
)
def cycles_electrified_vehicles_for_mobility():
    return zidz(
        mileage_vehicles()
        .loc[:, _subscript_dict["BATTERY_VEHICLES_I"]]
        .rename({"TRANSPORT_MODE_I": "BATTERY_VEHICLES_I"}),
        autonomy_ev_vehicles(),
    ) + battery_wear_factor() * zidz(
        mileage_vehicles()
        .loc[:, _subscript_dict["BATTERY_VEHICLES_I"]]
        .rename({"TRANSPORT_MODE_I": "BATTERY_VEHICLES_I"}),
        autonomy_ev_vehicles(),
    )


@component.add(
    name="cycles_for_elec_storage_and_supply_the_grid_of_EV_battery",
    units="cycles",
    subscripts=[
        "REGIONS_35_I",
        "EV_BATTERIES_I",
        "TRANSPORT_POWER_TRAIN_I",
        "BATTERY_VEHICLES_I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cf_v2g_storage": 1,
        "cf_ev_vehicle_for_transport": 1,
        "cycles_electrified_vehicles_for_mobility": 1,
    },
)
def cycles_for_elec_storage_and_supply_the_grid_of_ev_battery():
    """
    cycles used for storage and feed electrical energy for the system
    """
    return (
        zidz(
            cf_v2g_storage()
            .expand_dims({"EV_BATTERIES_I": _subscript_dict["EV_BATTERIES_I"]}, 1)
            .expand_dims(
                {"TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"]},
                2,
            )
            .expand_dims(
                {"BATTERY_VEHICLES_I": _subscript_dict["BATTERY_VEHICLES_I"]}, 3
            ),
            cf_ev_vehicle_for_transport().expand_dims(
                {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]}, 0
            ),
        )
        * cycles_electrified_vehicles_for_mobility()
    )


@component.add(
    name="cycles_max_for_elec_storage_EV_vehicles",
    units="cycles",
    subscripts=["TRANSPORT_POWER_TRAIN_I", "BATTERY_VEHICLES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "max_cycles_batteries_ev": 1,
        "cycles_electrified_vehicles_for_mobility": 1,
    },
)
def cycles_max_for_elec_storage_ev_vehicles():
    """
    cycles max of EV Household vehicle battery for electricity storage
    """
    return np.maximum(
        0, max_cycles_batteries_ev() - cycles_electrified_vehicles_for_mobility()
    )


@component.add(
    name="MAX_capacity_for_elec_storage_of_the_EV_batteries_in_one_day",
    units="TW*h/cycle",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "transport_electrified_vehicle_batteries_capacity": 1,
        "v2g_share_ev_vehicles": 1,
    },
)
def max_capacity_for_elec_storage_of_the_ev_batteries_in_one_day():
    """
    max capacity in a day given by EV batteries for electricity storage
    """
    return (
        sum(
            transport_electrified_vehicle_batteries_capacity().rename(
                {
                    "EV_BATTERIES_I": "EV_BATTERIES_I!",
                    "TRANSPORT_POWER_TRAIN_I": "TRANSPORT_POWER_TRAIN_I!",
                    "BATTERY_VEHICLES_I": "BATTERY_VEHICLES_I!",
                }
            ),
            dim=["EV_BATTERIES_I!", "TRANSPORT_POWER_TRAIN_I!", "BATTERY_VEHICLES_I!"],
        )
        * v2g_share_ev_vehicles()
    )


@component.add(
    name="MAX_capacity_for_elec_storage_of_the_EV_vehicles",
    units="TW*h/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cf_max_ev_vehicle_battery_for_elec_storage": 1,
        "transport_electrified_vehicle_batteries_power": 1,
        "unit_conversion_hours_year": 1,
    },
)
def max_capacity_for_elec_storage_of_the_ev_vehicles():
    """
    max capacity in a year given by EV batteries for electricity storage
    """
    return (
        sum(
            cf_max_ev_vehicle_battery_for_elec_storage().rename(
                {
                    "EV_BATTERIES_I": "EV_BATTERIES_I!",
                    "TRANSPORT_POWER_TRAIN_I": "TRANSPORT_POWER_TRAIN_I!",
                    "BATTERY_VEHICLES_I": "BATTERY_VEHICLES_I!",
                }
            )
            * transport_electrified_vehicle_batteries_power().rename(
                {
                    "EV_BATTERIES_I": "EV_BATTERIES_I!",
                    "TRANSPORT_POWER_TRAIN_I": "TRANSPORT_POWER_TRAIN_I!",
                    "BATTERY_VEHICLES_I": "BATTERY_VEHICLES_I!",
                }
            ),
            dim=["EV_BATTERIES_I!", "TRANSPORT_POWER_TRAIN_I!", "BATTERY_VEHICLES_I!"],
        )
        * unit_conversion_hours_year()
    )


@component.add(
    name="MAX_CYCLES_BATTERIES_EV",
    units="cycle",
    subscripts=["TRANSPORT_POWER_TRAIN_I", "BATTERY_VEHICLES_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_max_cycles_batteries_ev"},
)
def max_cycles_batteries_ev():
    """
    Max cycles for a EV Battery
    """
    return _ext_constant_max_cycles_batteries_ev()


_ext_constant_max_cycles_batteries_ev = ExtConstant(
    "model_parameters/energy/energy-transport.xlsx",
    "electrified_transport",
    "MAX_CYCLES_EV_VEHICLES",
    {
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "BATTERY_VEHICLES_I": _subscript_dict["BATTERY_VEHICLES_I"],
    },
    _root,
    {
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "BATTERY_VEHICLES_I": _subscript_dict["BATTERY_VEHICLES_I"],
    },
    "_ext_constant_max_cycles_batteries_ev",
)


@component.add(
    name="MAX_power_for_elec_storage_of_the_EV_vehicles",
    units="TW",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cf_max_ev_vehicle_battery_for_elec_storage": 1,
        "transport_electrified_vehicle_batteries_power": 1,
    },
)
def max_power_for_elec_storage_of_the_ev_vehicles():
    """
    max power given by EV batteries for electricity storage
    """
    return sum(
        cf_max_ev_vehicle_battery_for_elec_storage().rename(
            {
                "EV_BATTERIES_I": "EV_BATTERIES_I!",
                "TRANSPORT_POWER_TRAIN_I": "TRANSPORT_POWER_TRAIN_I!",
                "BATTERY_VEHICLES_I": "BATTERY_VEHICLES_I!",
            }
        )
        * transport_electrified_vehicle_batteries_power().rename(
            {
                "EV_BATTERIES_I": "EV_BATTERIES_I!",
                "TRANSPORT_POWER_TRAIN_I": "TRANSPORT_POWER_TRAIN_I!",
                "BATTERY_VEHICLES_I": "BATTERY_VEHICLES_I!",
            }
        ),
        dim=["EV_BATTERIES_I!", "TRANSPORT_POWER_TRAIN_I!", "BATTERY_VEHICLES_I!"],
    )


@component.add(
    name="power_charge_vehicles_with_SC",
    units="TW",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cf_ev_vehicle_for_transport": 4,
        "transport_electrified_vehicle_batteries_power": 4,
        "smart_charging_share_ev_vehicles": 1,
    },
)
def power_charge_vehicles_with_sc():
    """
    Power to recharge smart charging vehicles in a year
    """
    return (
        sum(
            cf_ev_vehicle_for_transport()
            .loc[:, "BEV", "LDV"]
            .reset_coords(drop=True)
            .rename({"EV_BATTERIES_I": "EV_BATTERIES_I!"})
            * transport_electrified_vehicle_batteries_power()
            .loc[:, :, "BEV", "LDV"]
            .reset_coords(drop=True)
            .rename({"EV_BATTERIES_I": "EV_BATTERIES_I!"})
            .transpose("EV_BATTERIES_I!", "REGIONS_35_I"),
            dim=["EV_BATTERIES_I!"],
        )
        + sum(
            cf_ev_vehicle_for_transport()
            .loc[:, "BEV", "MOTORCYCLES_2W_3W"]
            .reset_coords(drop=True)
            .rename({"EV_BATTERIES_I": "EV_BATTERIES_I!"})
            * transport_electrified_vehicle_batteries_power()
            .loc[:, :, "BEV", "MOTORCYCLES_2W_3W"]
            .reset_coords(drop=True)
            .rename({"EV_BATTERIES_I": "EV_BATTERIES_I!"})
            .transpose("EV_BATTERIES_I!", "REGIONS_35_I"),
            dim=["EV_BATTERIES_I!"],
        )
        + sum(
            cf_ev_vehicle_for_transport()
            .loc[:, "BEV", "MDV"]
            .reset_coords(drop=True)
            .rename({"EV_BATTERIES_I": "EV_BATTERIES_I!"})
            * transport_electrified_vehicle_batteries_power()
            .loc[:, :, "BEV", "MDV"]
            .reset_coords(drop=True)
            .rename({"EV_BATTERIES_I": "EV_BATTERIES_I!"})
            .transpose("EV_BATTERIES_I!", "REGIONS_35_I"),
            dim=["EV_BATTERIES_I!"],
        )
        + sum(
            cf_ev_vehicle_for_transport()
            .loc[:, "BEV", "bus"]
            .reset_coords(drop=True)
            .rename({"EV_BATTERIES_I": "EV_BATTERIES_I!"})
            * transport_electrified_vehicle_batteries_power()
            .loc[:, :, "BEV", "bus"]
            .reset_coords(drop=True)
            .rename({"EV_BATTERIES_I": "EV_BATTERIES_I!"})
            .transpose("EV_BATTERIES_I!", "REGIONS_35_I"),
            dim=["EV_BATTERIES_I!"],
        )
    ) * smart_charging_share_ev_vehicles()


@component.add(
    name="power_charge_vehicles_without_SC",
    units="TW",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cf_ev_vehicle_for_transport": 4,
        "transport_electrified_vehicle_batteries_power": 4,
        "smart_charging_share_ev_vehicles": 1,
    },
)
def power_charge_vehicles_without_sc():
    """
    Power to recharge smart charging vehicles in a year
    """
    return (
        sum(
            cf_ev_vehicle_for_transport()
            .loc[:, "BEV", "LDV"]
            .reset_coords(drop=True)
            .rename({"EV_BATTERIES_I": "EV_BATTERIES_I!"})
            * transport_electrified_vehicle_batteries_power()
            .loc[:, :, "BEV", "LDV"]
            .reset_coords(drop=True)
            .rename({"EV_BATTERIES_I": "EV_BATTERIES_I!"})
            .transpose("EV_BATTERIES_I!", "REGIONS_35_I"),
            dim=["EV_BATTERIES_I!"],
        )
        + sum(
            cf_ev_vehicle_for_transport()
            .loc[:, "BEV", "MOTORCYCLES_2W_3W"]
            .reset_coords(drop=True)
            .rename({"EV_BATTERIES_I": "EV_BATTERIES_I!"})
            * transport_electrified_vehicle_batteries_power()
            .loc[:, :, "BEV", "MOTORCYCLES_2W_3W"]
            .reset_coords(drop=True)
            .rename({"EV_BATTERIES_I": "EV_BATTERIES_I!"})
            .transpose("EV_BATTERIES_I!", "REGIONS_35_I"),
            dim=["EV_BATTERIES_I!"],
        )
        + sum(
            cf_ev_vehicle_for_transport()
            .loc[:, "BEV", "MDV"]
            .reset_coords(drop=True)
            .rename({"EV_BATTERIES_I": "EV_BATTERIES_I!"})
            * transport_electrified_vehicle_batteries_power()
            .loc[:, :, "BEV", "MDV"]
            .reset_coords(drop=True)
            .rename({"EV_BATTERIES_I": "EV_BATTERIES_I!"})
            .transpose("EV_BATTERIES_I!", "REGIONS_35_I"),
            dim=["EV_BATTERIES_I!"],
        )
        + sum(
            cf_ev_vehicle_for_transport()
            .loc[:, "BEV", "bus"]
            .reset_coords(drop=True)
            .rename({"EV_BATTERIES_I": "EV_BATTERIES_I!"})
            * transport_electrified_vehicle_batteries_power()
            .loc[:, :, "BEV", "bus"]
            .reset_coords(drop=True)
            .rename({"EV_BATTERIES_I": "EV_BATTERIES_I!"})
            .transpose("EV_BATTERIES_I!", "REGIONS_35_I"),
            dim=["EV_BATTERIES_I!"],
        )
    ) * (1 - smart_charging_share_ev_vehicles())


@component.add(
    name="smart_charging_share_EV_vehicles",
    units="DMNL",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "v2g_share_ev_vehicles": 1,
        "objective_sc_sp": 2,
        "initial_sc_sp": 4,
        "year_final_sc_sp": 2,
        "time": 4,
        "year_initial_sc_sp": 3,
        "switch_sc_sp": 1,
    },
)
def smart_charging_share_ev_vehicles():
    """
    Smart charging factor.This factor indicates the percentage of EV vehicles that can be charged when there is excess power in the grid. Priority is given to V2G since together they cannot represent > 100%.
    """
    return (
        np.minimum(
            1 - v2g_share_ev_vehicles(),
            if_then_else(
                time() < 2015,
                lambda: initial_sc_sp(),
                lambda: if_then_else(
                    time() < year_initial_sc_sp(),
                    lambda: initial_sc_sp(),
                    lambda: if_then_else(
                        time() < year_final_sc_sp(),
                        lambda: initial_sc_sp()
                        + (objective_sc_sp() - initial_sc_sp())
                        * (time() - year_initial_sc_sp())
                        / (year_final_sc_sp() - year_initial_sc_sp()),
                        lambda: objective_sc_sp(),
                    ),
                ),
            ),
        )
        * switch_sc_sp()
    )


@component.add(
    name="SWITCH_SC_SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_sc_sp"},
)
def switch_sc_sp():
    """
    1: activate scenario parameter 0: deactivate scenario parameter
    """
    return _ext_constant_switch_sc_sp()


_ext_constant_switch_sc_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "SWITCH_SC_SP",
    {},
    _root,
    {},
    "_ext_constant_switch_sc_sp",
)


@component.add(
    name="SWITCH_V2G_SP",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_v2g_sp"},
)
def switch_v2g_sp():
    """
    1: activate scenario parameter 0: deactivate scenario parameter
    """
    return _ext_constant_switch_v2g_sp()


_ext_constant_switch_v2g_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "SWITCH_V2G_SP",
    {},
    _root,
    {},
    "_ext_constant_switch_v2g_sp",
)


@component.add(
    name="V2G_share_EV_vehicles",
    units="DMNL",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 4,
        "initial_v2g_sp": 4,
        "objective_v2g_sp": 2,
        "year_final_v2g_sp": 2,
        "year_initial_v2g_sp": 3,
        "switch_v2g_sp": 1,
    },
)
def v2g_share_ev_vehicles():
    """
    Vehicle to grid factor. This factor indicates the share of EV vehicles that can transfer electrical energy from their batteries to the grid.
    """
    return xr.DataArray(
        if_then_else(
            time() < 2015,
            lambda: initial_v2g_sp(),
            lambda: if_then_else(
                time() < year_initial_v2g_sp(),
                lambda: initial_v2g_sp(),
                lambda: if_then_else(
                    time() < year_final_v2g_sp(),
                    lambda: initial_v2g_sp()
                    + (objective_v2g_sp() - initial_v2g_sp())
                    * (time() - year_initial_v2g_sp())
                    / (year_final_v2g_sp() - year_initial_v2g_sp()),
                    lambda: objective_v2g_sp(),
                ),
            ),
        )
        * switch_v2g_sp(),
        {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
        ["REGIONS_35_I"],
    )
