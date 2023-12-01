"""
Module energy.end_use.transport_passengers
Translated using PySD version 3.10.0
"""


@component.add(
    name="base_share_technologies_passanger_transport",
    subscripts=[
        "REGIONS_35_I",
        "TRANSPORT_POWER_TRAIN_I",
        "PASSENGERS_TRANSPORT_MODE_I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"objective_passenger_transport_demand_modal_share_sp": 2},
)
def base_share_technologies_passanger_transport():
    """
    Base shares of eahc technology over total light duty vehicles
    """
    return zidz(
        objective_passenger_transport_demand_modal_share_sp(),
        sum(
            objective_passenger_transport_demand_modal_share_sp().rename(
                {"TRANSPORT_POWER_TRAIN_I": "TRANSPORT_POWER_TRAIN_I!"}
            ),
            dim=["TRANSPORT_POWER_TRAIN_I!"],
        ).expand_dims(
            {"TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"]}, 1
        ),
    )


@component.add(
    name="battery_lifetime",
    units="Year",
    subscripts=[
        "REGIONS_35_I",
        "TRANSPORT_POWER_TRAIN_I",
        "BATTERY_VEHICLES_I",
        "HOUSEHOLDS_I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"max_cycles_batteries_ev": 1, "charge_cycles_per_year": 1},
)
def battery_lifetime():
    """
    Total battery life of a battery, it depends of the total battery cycles and the cycles performed by year.
    """
    return zidz(
        max_cycles_batteries_ev()
        .expand_dims({"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]}, 2)
        .expand_dims({"HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"]}, 3),
        charge_cycles_per_year().transpose(
            "TRANSPORT_POWER_TRAIN_I",
            "BATTERY_VEHICLES_I",
            "REGIONS_35_I",
            "HOUSEHOLDS_I",
        ),
    ).transpose(
        "REGIONS_35_I", "TRANSPORT_POWER_TRAIN_I", "BATTERY_VEHICLES_I", "HOUSEHOLDS_I"
    )


@component.add(
    name="BEV_and_PHEV_LDV_9R_sales",
    units="vehicles/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"new_passenger_private_vehicles": 4},
)
def bev_and_phev_ldv_9r_sales():
    value = xr.DataArray(
        np.nan, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
    )
    value.loc[_subscript_dict["REGIONS_8_I"]] = (
        sum(
            new_passenger_private_vehicles()
            .loc[_subscript_dict["REGIONS_8_I"], "BEV", "LDV", :]
            .reset_coords(drop=True)
            .rename({"REGIONS_35_I": "REGIONS_8_I", "HOUSEHOLDS_I": "HOUSEHOLDS_I!"}),
            dim=["HOUSEHOLDS_I!"],
        )
        + sum(
            new_passenger_private_vehicles()
            .loc[_subscript_dict["REGIONS_8_I"], "PHEV", "LDV", :]
            .reset_coords(drop=True)
            .rename({"REGIONS_35_I": "REGIONS_8_I", "HOUSEHOLDS_I": "HOUSEHOLDS_I!"}),
            dim=["HOUSEHOLDS_I!"],
        )
    ).values
    value.loc[["EU27"]] = sum(
        new_passenger_private_vehicles()
        .loc[_subscript_dict["REGIONS_EU27_I"], "BEV", "LDV", :]
        .reset_coords(drop=True)
        .rename({"REGIONS_35_I": "REGIONS_EU27_I!", "HOUSEHOLDS_I": "HOUSEHOLDS_I!"}),
        dim=["REGIONS_EU27_I!", "HOUSEHOLDS_I!"],
    ) + sum(
        new_passenger_private_vehicles()
        .loc[_subscript_dict["REGIONS_EU27_I"], "PHEV", "LDV", :]
        .reset_coords(drop=True)
        .rename({"REGIONS_35_I": "REGIONS_EU27_I!", "HOUSEHOLDS_I": "HOUSEHOLDS_I!"}),
        dim=["REGIONS_EU27_I!", "HOUSEHOLDS_I!"],
    )
    return value


@component.add(
    name="charge_cycles_per_year",
    units="cycle/Year",
    subscripts=[
        "REGIONS_35_I",
        "TRANSPORT_POWER_TRAIN_I",
        "BATTERY_VEHICLES_I",
        "HOUSEHOLDS_I",
    ],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={"desired_passenger_vehicle_distance": 3, "autonomy_ev_vehicles": 3},
)
def charge_cycles_per_year():
    """
    Number of cycles that a vehicle battery makes m in a year, it depends of the autonomy of the battery and the total annual mileage of the vehicle.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
            "BATTERY_VEHICLES_I": _subscript_dict["BATTERY_VEHICLES_I"],
            "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
        },
        [
            "REGIONS_35_I",
            "TRANSPORT_POWER_TRAIN_I",
            "BATTERY_VEHICLES_I",
            "HOUSEHOLDS_I",
        ],
    )
    value.loc[:, :, ["LDV"], :] = (
        zidz(
            desired_passenger_vehicle_distance()
            .loc[:, :, "LDV", :]
            .reset_coords(drop=True),
            autonomy_ev_vehicles()
            .loc[:, "LDV"]
            .reset_coords(drop=True)
            .expand_dims({"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]}, 0)
            .expand_dims({"HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"]}, 2),
        )
        .expand_dims({"BATTERY_VEHICLES_I": ["LDV"]}, 2)
        .values
    )
    value.loc[:, :, ["bus"], :] = (
        zidz(
            desired_passenger_vehicle_distance()
            .loc[:, :, "bus", :]
            .reset_coords(drop=True),
            autonomy_ev_vehicles()
            .loc[:, "bus"]
            .reset_coords(drop=True)
            .expand_dims({"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]}, 0)
            .expand_dims({"HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"]}, 2),
        )
        .expand_dims({"BATTERY_VEHICLES_I": ["bus"]}, 2)
        .values
    )
    value.loc[:, :, ["MOTORCYCLES_2W_3W"], :] = (
        zidz(
            desired_passenger_vehicle_distance()
            .loc[:, :, "MOTORCYCLES_2W_3W", :]
            .reset_coords(drop=True),
            autonomy_ev_vehicles()
            .loc[:, "MOTORCYCLES_2W_3W"]
            .reset_coords(drop=True)
            .expand_dims({"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]}, 0)
            .expand_dims({"HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"]}, 2),
        )
        .expand_dims({"BATTERY_VEHICLES_I": ["MOTORCYCLES_2W_3W"]}, 2)
        .values
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, :, ["LDV"], :] = False
    except_subs.loc[:, :, ["bus"], :] = False
    except_subs.loc[:, :, ["MOTORCYCLES_2W_3W"], :] = False
    value.values[except_subs.values] = 0
    return value


@component.add(
    name="CO2_passenger_transport_emissions_intensity",
    units="kg/km",
    subscripts=[
        "REGIONS_35_I",
        "TRANSPORT_POWER_TRAIN_I",
        "PASSENGERS_TRANSPORT_MODE_I",
        "GHG_ENERGY_USE_I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "co2_emissions_by_passenger_transport_mode_and_power_train_35r": 1,
        "private_passenger_transport_total_distance_traveled_by_transport_mode": 1,
    },
)
def co2_passenger_transport_emissions_intensity():
    """
    GHG emissions intensity in gGHG/km by POWER_TRAIn and TRANSPORT_MODE
    """
    return zidz(
        co2_emissions_by_passenger_transport_mode_and_power_train_35r()
        .loc[:, :, :, "CO2"]
        .reset_coords(drop=True),
        private_passenger_transport_total_distance_traveled_by_transport_mode(),
    ).expand_dims({"GHG_ENERGY_USE_I": ["CO2"]}, 3)


@component.add(
    name="CONSTANT_BEV_BUS",
    units="DMNL",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"base_share_technologies_passanger_transport": 2},
)
def constant_bev_bus():
    """
    Constant BEV BUS
    """
    return if_then_else(
        base_share_technologies_passanger_transport()
        .loc[:, "BEV", "bus"]
        .reset_coords(drop=True)
        == 0,
        lambda: xr.DataArray(
            0, {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]}, ["REGIONS_35_I"]
        ),
        lambda: np.log(
            base_share_technologies_passanger_transport()
            .loc[:, "BEV", "bus"]
            .reset_coords(drop=True)
        ),
    )


@component.add(
    name="CONSTANT_BEV_LDV",
    units="DMNL",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"base_share_technologies_passanger_transport": 2},
)
def constant_bev_ldv():
    """
    Constant BEV LDV
    """
    return if_then_else(
        base_share_technologies_passanger_transport()
        .loc[:, "BEV", "LDV"]
        .reset_coords(drop=True)
        == 0,
        lambda: xr.DataArray(
            0, {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]}, ["REGIONS_35_I"]
        ),
        lambda: np.log(
            base_share_technologies_passanger_transport()
            .loc[:, "BEV", "LDV"]
            .reset_coords(drop=True)
        ),
    )


@component.add(
    name="CONSTANT_MODAL_SPLIT_PUBLIC",
    units="DMNL",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"objective_passenger_transport_demand_modal_share_sp": 4},
)
def constant_modal_split_public():
    """
    Constant public transportation
    """
    return if_then_else(
        sum(
            objective_passenger_transport_demand_modal_share_sp()
            .loc[:, :, "bus"]
            .reset_coords(drop=True)
            .rename({"TRANSPORT_POWER_TRAIN_I": "TRANSPORT_POWER_TRAIN_I!"})
            + objective_passenger_transport_demand_modal_share_sp()
            .loc[:, :, "RAIL"]
            .reset_coords(drop=True)
            .rename({"TRANSPORT_POWER_TRAIN_I": "TRANSPORT_POWER_TRAIN_I!"}),
            dim=["TRANSPORT_POWER_TRAIN_I!"],
        )
        == 0,
        lambda: xr.DataArray(
            0, {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]}, ["REGIONS_35_I"]
        ),
        lambda: np.log(
            sum(
                objective_passenger_transport_demand_modal_share_sp()
                .loc[:, :, "bus"]
                .reset_coords(drop=True)
                .rename({"TRANSPORT_POWER_TRAIN_I": "TRANSPORT_POWER_TRAIN_I!"})
                + objective_passenger_transport_demand_modal_share_sp()
                .loc[:, :, "RAIL"]
                .reset_coords(drop=True)
                .rename({"TRANSPORT_POWER_TRAIN_I": "TRANSPORT_POWER_TRAIN_I!"}),
                dim=["TRANSPORT_POWER_TRAIN_I!"],
            )
        ),
    )


@component.add(
    name="DESIRED_PASSENGER_TRANSPORT_DEMAND",
    units="persons*km",
    subscripts=["REGIONS_35_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_desired_passenger_transport_demand"},
)
def desired_passenger_transport_demand():
    return _ext_constant_desired_passenger_transport_demand()


_ext_constant_desired_passenger_transport_demand = ExtConstant(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "TOTAL_TRANSPORT_DEMAND_BY_REGION*",
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    _root,
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    "_ext_constant_desired_passenger_transport_demand",
)


@component.add(
    name="desired_passenger_transport_demand_by_mode",
    units="persons*km",
    subscripts=[
        "REGIONS_35_I",
        "TRANSPORT_POWER_TRAIN_I",
        "PASSENGERS_TRANSPORT_MODE_I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "total_passenger_transport_demand_by_region": 1,
        "passenger_transport_modal_share": 1,
    },
)
def desired_passenger_transport_demand_by_mode():
    """
    Transport demand by region, power train and transport mode in pass*km. passengers_transport_demand_corrected_by_GDPpc[REGIONS 35 I]*PASSENGER_TRANSPORT_MODAL_SHARE[REGIONS 35 I,POWER TRAIN I ,PASSENGERS TRANSPORT MODE I]
    """
    return (
        total_passenger_transport_demand_by_region() * passenger_transport_modal_share()
    )


@component.add(
    name="desired_passenger_transport_demand_by_region",
    units="km*person",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"desired_transport_demand": 1},
)
def desired_passenger_transport_demand_by_region():
    return (
        sum(
            desired_transport_demand().rename({"HOUSEHOLDS_I": "HOUSEHOLDS_I!"}),
            dim=["HOUSEHOLDS_I!"],
        )
        / 1000000.0
    )


@component.add(
    name="desired_passenger_transport_demand_per_capita",
    units="km",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"desired_passenger_transport_demand": 1, "population_35_regions": 1},
)
def desired_passenger_transport_demand_per_capita():
    return zidz(desired_passenger_transport_demand(), population_35_regions())


@component.add(
    name="desired_passenger_vehicle_distance",
    units="km/(Year*vehicle)",
    subscripts=[
        "REGIONS_35_I",
        "TRANSPORT_POWER_TRAIN_I",
        "PASSENGERS_TRANSPORT_MODE_I",
        "HOUSEHOLDS_I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "desired_passengers_transport_demand_by_mode_and_type_of_households_modified": 2,
        "modified_load_factor_passenger_transport": 2,
        "private_passenger_vehicle_fleet": 1,
        "public_passenger_vehicle_fleet": 1,
    },
)
def desired_passenger_vehicle_distance():
    """
    Vehicle distance needed to acomply with the desired transport demand ZIDZ(desired_passengers_transport_demand_by_mode_and_type_of_households_mod ified[REGIONS_35_I,POWER_TRAIN_I,PUBLIC_TRANSPORT_I,HOUSEHOLDS_I],(Modified _load_factor_passenger_transport[REGIONS_35_I,POWER_TRAIN_I,PUBLIC_TRANSPOR T_I,HOUSEHOLDS_I]*public_passengers_vehicle_fleet[REGIONS_35_I,POWER_TRAIN_ I,PUBLIC_TRANSPORT_I,HOUSEHOLDS_I]))
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
            "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict[
                "PASSENGERS_TRANSPORT_MODE_I"
            ],
            "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
        },
        [
            "REGIONS_35_I",
            "TRANSPORT_POWER_TRAIN_I",
            "PASSENGERS_TRANSPORT_MODE_I",
            "HOUSEHOLDS_I",
        ],
    )
    value.loc[:, :, _subscript_dict["PRIVATE_TRANSPORT_I"], :] = zidz(
        desired_passengers_transport_demand_by_mode_and_type_of_households_modified()
        .loc[:, :, _subscript_dict["PRIVATE_TRANSPORT_I"], :]
        .rename({"PASSENGERS_TRANSPORT_MODE_I": "PRIVATE_TRANSPORT_I"}),
        modified_load_factor_passenger_transport()
        .loc[:, :, _subscript_dict["PRIVATE_TRANSPORT_I"], :]
        .rename({"PASSENGERS_TRANSPORT_MODE_I": "PRIVATE_TRANSPORT_I"})
        * private_passenger_vehicle_fleet(),
    ).values
    value.loc[:, :, _subscript_dict["PUBLIC_TRANSPORT_I"], :] = zidz(
        desired_passengers_transport_demand_by_mode_and_type_of_households_modified()
        .loc[:, :, _subscript_dict["PUBLIC_TRANSPORT_I"], :]
        .rename({"PASSENGERS_TRANSPORT_MODE_I": "PUBLIC_TRANSPORT_I"}),
        modified_load_factor_passenger_transport()
        .loc[:, :, _subscript_dict["PUBLIC_TRANSPORT_I"], :]
        .rename({"PASSENGERS_TRANSPORT_MODE_I": "PUBLIC_TRANSPORT_I"})
        * public_passenger_vehicle_fleet(),
    ).values
    return value


@component.add(
    name="desired_passengers_transport_demand_by_mode_and_type_of_households_modified",
    units="km*person",
    subscripts=[
        "REGIONS_35_I",
        "TRANSPORT_POWER_TRAIN_I",
        "PASSENGERS_TRANSPORT_MODE_I",
        "HOUSEHOLDS_I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "desired_passenger_transport_demand_by_mode": 1,
        "share_passenger_transport_demand_by_region_and_type_of_household": 1,
        "reduction_passenger_transport_demand": 1,
    },
)
def desired_passengers_transport_demand_by_mode_and_type_of_households_modified():
    """
    Transport demand by region, power train, transport mode and type of household modified by transport demand reduction policy, in pass*km.
    """
    return (
        desired_passenger_transport_demand_by_mode()
        * share_passenger_transport_demand_by_region_and_type_of_household()
        * reduction_passenger_transport_demand()
    )


@component.add(
    name="energy_consumption_private_passenger_transport_by_mode",
    units="EJ",
    subscripts=["REGIONS_35_I", "NRG_FE_I", "PRIVATE_TRANSPORT_I", "HOUSEHOLDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "energy_passenger_transport_consumption_by_fe_35r": 1,
        "unit_conversion_mj_ej": 1,
    },
)
def energy_consumption_private_passenger_transport_by_mode():
    """
    Energy passengers transport consumption by region, type of final energy, transport mode and type of household, in EJ. energy_consumption_private_transport_COICOP_physical_units[REGIONS_35_I, HOUSEHOLDS_I, HH_ELECTRICITY]= SUM(energy_consumption_private_transport_by_mode[REGIONS_35_I,FE_elec,PRIVA TE_TRANSPORT_I!,HOUSEHOLDS_I])
    """
    return (
        energy_passenger_transport_consumption_by_fe_35r()
        .loc[:, :, _subscript_dict["PRIVATE_TRANSPORT_I"], :]
        .rename({"PASSENGERS_TRANSPORT_MODE_I": "PRIVATE_TRANSPORT_I"})
        / unit_conversion_mj_ej()
    )


@component.add(
    name="energy_passenger_transport_consumption",
    units="MJ",
    subscripts=[
        "REGIONS_35_I",
        "TRANSPORT_POWER_TRAIN_I",
        "PASSENGERS_TRANSPORT_MODE_I",
        "HOUSEHOLDS_I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "passenger_transport_real_supply": 1,
        "mobility_passenger_transport_intensity": 1,
    },
)
def energy_passenger_transport_consumption():
    """
    Energy transport consumption by region, power train,transport mode and type of household in MJ.
    """
    return passenger_transport_real_supply() * mobility_passenger_transport_intensity()


@component.add(
    name="energy_passenger_transport_consumption_by_FE_35R",
    units="MJ",
    subscripts=[
        "REGIONS_35_I",
        "NRG_FE_I",
        "PASSENGERS_TRANSPORT_MODE_I",
        "HOUSEHOLDS_I",
    ],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={"energy_passenger_transport_consumption": 10, "share_elec_in_phev": 2},
)
def energy_passenger_transport_consumption_by_fe_35r():
    """
    Energy passengers transport consumption by region, type of final energy, transport mode and type of household, in MJ.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "NRG_FE_I": _subscript_dict["NRG_FE_I"],
            "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict[
                "PASSENGERS_TRANSPORT_MODE_I"
            ],
            "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
        },
        ["REGIONS_35_I", "NRG_FE_I", "PASSENGERS_TRANSPORT_MODE_I", "HOUSEHOLDS_I"],
    )
    value.loc[:, ["FE_elec"], :, :] = (
        (
            energy_passenger_transport_consumption()
            .loc[:, "EV", :, :]
            .reset_coords(drop=True)
            + energy_passenger_transport_consumption()
            .loc[:, "BEV", :, :]
            .reset_coords(drop=True)
            + energy_passenger_transport_consumption()
            .loc[:, "PHEV", :, :]
            .reset_coords(drop=True)
            * share_elec_in_phev()
        )
        .expand_dims({"FINAL_ENERGY_TRANSMISSION_I": ["FE_elec"]}, 1)
        .values
    )
    value.loc[:, ["FE_gas"], :, :] = (
        energy_passenger_transport_consumption()
        .loc[:, "ICE_gas", :, :]
        .reset_coords(drop=True)
        .expand_dims({"FINAL_ENERGY_TRANSMISSION_I": ["FE_gas"]}, 1)
        .values
    )
    value.loc[:, ["FE_hydrogen"], :, :] = (
        energy_passenger_transport_consumption()
        .loc[:, "FCEV", :, :]
        .reset_coords(drop=True)
        .expand_dims({"NRG_COMMODITIES_I": ["FE_hydrogen"]}, 1)
        .values
    )
    value.loc[:, ["FE_liquid"], :, :] = (
        (
            energy_passenger_transport_consumption()
            .loc[:, "ICE_gasoline", :, :]
            .reset_coords(drop=True)
            + energy_passenger_transport_consumption()
            .loc[:, "ICE_diesel", :, :]
            .reset_coords(drop=True)
            + energy_passenger_transport_consumption()
            .loc[:, "ICE_LPG", :, :]
            .reset_coords(drop=True)
            + energy_passenger_transport_consumption()
            .loc[:, "HEV", :, :]
            .reset_coords(drop=True)
            + energy_passenger_transport_consumption()
            .loc[:, "PHEV", :, :]
            .reset_coords(drop=True)
            * (1 - share_elec_in_phev())
        )
        .expand_dims({"NRG_COMMODITIES_I": ["FE_liquid"]}, 1)
        .values
    )
    value.loc[:, ["FE_heat"], :, :] = 0
    value.loc[:, ["FE_solid_bio"], :, :] = 0
    value.loc[:, ["FE_solid_fossil"], :, :] = 0
    return value


@component.add(
    name="energy_passengers_transport_consumption_new",
    units="MJ",
    subscripts=[
        "REGIONS_35_I",
        "TRANSPORT_POWER_TRAIN_I",
        "PASSENGERS_TRANSPORT_MODE_I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"energy_passenger_transport_consumption": 1},
)
def energy_passengers_transport_consumption_new():
    return sum(
        energy_passenger_transport_consumption().rename(
            {"HOUSEHOLDS_I": "HOUSEHOLDS_I!"}
        ),
        dim=["HOUSEHOLDS_I!"],
    )


@component.add(
    name="energy_private_transport_consumption_by_region_and_FE",
    units="TJ/Year",
    subscripts=["REGIONS_35_I", "NRG_FE_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "energy_passenger_transport_consumption_by_fe_35r": 1,
        "unit_conversion_j_mj": 1,
        "unit_conversion_j_tj": 1,
    },
)
def energy_private_transport_consumption_by_region_and_fe():
    """
    Energy private passengers transport consumption by region, and final energy, in TJ/year.
    """
    return (
        sum(
            energy_passenger_transport_consumption_by_fe_35r()
            .loc[:, :, _subscript_dict["PRIVATE_TRANSPORT_I"], :]
            .rename(
                {
                    "PASSENGERS_TRANSPORT_MODE_I": "PRIVATE_TRANSPORT_I!",
                    "HOUSEHOLDS_I": "HOUSEHOLDS_I!",
                }
            ),
            dim=["PRIVATE_TRANSPORT_I!", "HOUSEHOLDS_I!"],
        )
        * unit_conversion_j_mj()
        / unit_conversion_j_tj()
    )


@component.add(
    name="EXO_GDPpc_real",
    units="Mdollars_2015/(Year*person)",
    subscripts=["REGIONS_35_I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def exo_gdppc_real():
    return xr.DataArray(
        [
            0.0451118,
            0.0427141,
            0.00633706,
            0.0111552,
            0.0193577,
            0.0179868,
            0.0540681,
            0.0163542,
            0.0435244,
            0.0392724,
            0.0412518,
            0.0166724,
            0.011818,
            0.0662618,
            0.0308321,
            0.0119721,
            0.012299,
            0.123406,
            0.025844,
            0.0455362,
            0.0122944,
            0.018584,
            0.00833145,
            0.0161427,
            0.0210165,
            0.0269513,
            0.0543691,
            0.0472851,
            0.00846259,
            0.0138824,
            0.00176239,
            0.0100765,
            0.00936603,
            0.0476612,
            0.00462099,
        ],
        {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
        ["REGIONS_35_I"],
    )


@component.add(
    name="EXO_total_passenger_transport_demand",
    units="km*person",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"exo_total_transport_demand_by_region_and_type_of_hh": 1},
)
def exo_total_passenger_transport_demand():
    return sum(
        exo_total_transport_demand_by_region_and_type_of_hh().rename(
            {"REGIONS_35_I": "REGIONS_35_I!", "HOUSEHOLDS_I": "HOUSEHOLDS_I!"}
        ),
        dim=["REGIONS_35_I!", "HOUSEHOLDS_I!"],
    )


@component.add(
    name="FACTOR_PASSENGERS_PRIVATE_FLEET",
    units="1",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_factor_passengers_private_fleet"},
)
def factor_passengers_private_fleet():
    return _ext_constant_factor_passengers_private_fleet()


_ext_constant_factor_passengers_private_fleet = ExtConstant(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "FACTOR_PRIVATE_FLEET",
    {},
    _root,
    {},
    "_ext_constant_factor_passengers_private_fleet",
)


@component.add(
    name="FACTOR_PASSENGERS_PUBLIC_FLEET",
    units="1",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_factor_passengers_public_fleet"},
)
def factor_passengers_public_fleet():
    return _ext_constant_factor_passengers_public_fleet()


_ext_constant_factor_passengers_public_fleet = ExtConstant(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "FACTOR_PUBLIC_FLEET",
    {},
    _root,
    {},
    "_ext_constant_factor_passengers_public_fleet",
)


@component.add(
    name="global_BEV_and_PHEV_2W_sales",
    units="vehicles/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"new_passenger_private_vehicles": 2},
)
def global_bev_and_phev_2w_sales():
    return sum(
        new_passenger_private_vehicles()
        .loc[:, "BEV", "MOTORCYCLES_2W_3W", :]
        .reset_coords(drop=True)
        .rename({"REGIONS_35_I": "REGIONS_35_I!", "HOUSEHOLDS_I": "HOUSEHOLDS_I!"}),
        dim=["REGIONS_35_I!", "HOUSEHOLDS_I!"],
    ) + sum(
        new_passenger_private_vehicles()
        .loc[:, "PHEV", "MOTORCYCLES_2W_3W", :]
        .reset_coords(drop=True)
        .rename({"REGIONS_35_I": "REGIONS_35_I!", "HOUSEHOLDS_I": "HOUSEHOLDS_I!"}),
        dim=["REGIONS_35_I!", "HOUSEHOLDS_I!"],
    )


@component.add(
    name="global_BEV_and_PHEV_LDV_sales",
    units="vehicles/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"new_passenger_private_vehicles": 2},
)
def global_bev_and_phev_ldv_sales():
    return sum(
        new_passenger_private_vehicles()
        .loc[:, "BEV", "LDV", :]
        .reset_coords(drop=True)
        .rename({"REGIONS_35_I": "REGIONS_35_I!", "HOUSEHOLDS_I": "HOUSEHOLDS_I!"}),
        dim=["REGIONS_35_I!", "HOUSEHOLDS_I!"],
    ) + sum(
        new_passenger_private_vehicles()
        .loc[:, "PHEV", "LDV", :]
        .reset_coords(drop=True)
        .rename({"REGIONS_35_I": "REGIONS_35_I!", "HOUSEHOLDS_I": "HOUSEHOLDS_I!"}),
        dim=["REGIONS_35_I!", "HOUSEHOLDS_I!"],
    )


@component.add(
    name="INITIAL_LIFETIME_PASSENGERS_VEHICLES",
    units="Years",
    subscripts=["TRANSPORT_MODE_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_lifetime_passengers_vehicles"},
)
def initial_lifetime_passengers_vehicles():
    """
    Lifetime vehicles data for 2015 by transport mode vehicle, in years.
    """
    return _ext_constant_initial_lifetime_passengers_vehicles()


_ext_constant_initial_lifetime_passengers_vehicles = ExtConstant(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_LIFETIME_VEHICLES*",
    {"TRANSPORT_MODE_I": _subscript_dict["TRANSPORT_MODE_I"]},
    _root,
    {"TRANSPORT_MODE_I": _subscript_dict["TRANSPORT_MODE_I"]},
    "_ext_constant_initial_lifetime_passengers_vehicles",
)


@component.add(
    name="initial_passenger_private_fleet_1_type_HH",
    units="vehicles",
    subscripts=[
        "REGIONS_35_I",
        "TRANSPORT_POWER_TRAIN_I",
        "PRIVATE_TRANSPORT_I",
        "HOUSEHOLDS_I",
    ],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={"initial_passengers_private_fleet": 3},
)
def initial_passenger_private_fleet_1_type_hh():
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
            "PRIVATE_TRANSPORT_I": _subscript_dict["PRIVATE_TRANSPORT_I"],
            "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
        },
        [
            "REGIONS_35_I",
            "TRANSPORT_POWER_TRAIN_I",
            "PRIVATE_TRANSPORT_I",
            "HOUSEHOLDS_I",
        ],
    )
    value.loc[:, :, ["NMT"], ["REPRESENTATIVE_HOUSEHOLD"]] = (
        initial_passengers_private_fleet()
        .loc[:, :, "NMT"]
        .reset_coords(drop=True)
        .expand_dims({"PASSENGERS_TRANSPORT_MODE_I": ["NMT"]}, 2)
        .expand_dims({"HOUSEHOLDS_I": ["REPRESENTATIVE_HOUSEHOLD"]}, 3)
        .values
    )
    value.loc[:, :, ["LDV"], ["REPRESENTATIVE_HOUSEHOLD"]] = (
        initial_passengers_private_fleet()
        .loc[:, :, "LDV"]
        .reset_coords(drop=True)
        .expand_dims({"BATTERY_VEHICLES_I": ["LDV"]}, 2)
        .expand_dims({"HOUSEHOLDS_I": ["REPRESENTATIVE_HOUSEHOLD"]}, 3)
        .values
    )
    value.loc[:, :, ["MOTORCYCLES_2W_3W"], ["REPRESENTATIVE_HOUSEHOLD"]] = (
        initial_passengers_private_fleet()
        .loc[:, :, "MOTORCYCLES_2W_3W"]
        .reset_coords(drop=True)
        .expand_dims({"BATTERY_VEHICLES_I": ["MOTORCYCLES_2W_3W"]}, 2)
        .expand_dims({"HOUSEHOLDS_I": ["REPRESENTATIVE_HOUSEHOLD"]}, 3)
        .values
    )
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[:, :, ["NMT"], :] = True
    except_subs.loc[:, :, ["NMT"], ["REPRESENTATIVE_HOUSEHOLD"]] = False
    value.values[except_subs.values] = 0
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[:, :, ["LDV"], :] = True
    except_subs.loc[:, :, ["LDV"], ["REPRESENTATIVE_HOUSEHOLD"]] = False
    value.values[except_subs.values] = 0
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[:, :, ["MOTORCYCLES_2W_3W"], :] = True
    except_subs.loc[:, :, ["MOTORCYCLES_2W_3W"], ["REPRESENTATIVE_HOUSEHOLD"]] = False
    value.values[except_subs.values] = 0
    return value


@component.add(
    name="initial_passenger_private_fleet_by_type_of_HH",
    units="vehicle",
    subscripts=[
        "REGIONS_35_I",
        "TRANSPORT_POWER_TRAIN_I",
        "PRIVATE_TRANSPORT_I",
        "HOUSEHOLDS_I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "initial_passengers_private_fleet": 1,
        "initial_ldv_fleet": 1,
        "initial_2w_3w_fleet": 1,
    },
)
def initial_passenger_private_fleet_by_type_of_hh():
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
            "PRIVATE_TRANSPORT_I": _subscript_dict["PRIVATE_TRANSPORT_I"],
            "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
        },
        [
            "REGIONS_35_I",
            "TRANSPORT_POWER_TRAIN_I",
            "PRIVATE_TRANSPORT_I",
            "HOUSEHOLDS_I",
        ],
    )
    value.loc[:, :, ["NMT"], :] = (
        (
            initial_passengers_private_fleet().loc[:, :, "NMT"].reset_coords(drop=True)
            / 61
        )
        .expand_dims({"PASSENGERS_TRANSPORT_MODE_I": ["NMT"]}, 2)
        .expand_dims({"HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"]}, 3)
        .values
    )
    value.loc[:, :, ["LDV"], :] = (
        initial_ldv_fleet().expand_dims({"BATTERY_VEHICLES_I": ["LDV"]}, 2).values
    )
    value.loc[:, :, ["MOTORCYCLES_2W_3W"], :] = (
        initial_2w_3w_fleet()
        .expand_dims({"BATTERY_VEHICLES_I": ["MOTORCYCLES_2W_3W"]}, 2)
        .values
    )
    return value


@component.add(
    name="INITIAL_PASSENGER_PUBLIC_FLEET_BY_TYPE_OF_HH",
    units="vehicles",
    subscripts=[
        "REGIONS_35_I",
        "TRANSPORT_POWER_TRAIN_I",
        "PUBLIC_TRANSPORT_I",
        "HOUSEHOLDS_I",
    ],
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_initial_passenger_public_fleet_by_type_of_hh": 1},
    other_deps={
        "_initial_initial_passenger_public_fleet_by_type_of_hh": {
            "initial": {"passenger_fleet_demand": 1},
            "step": {},
        }
    },
)
def initial_passenger_public_fleet_by_type_of_hh():
    return _initial_initial_passenger_public_fleet_by_type_of_hh()


_initial_initial_passenger_public_fleet_by_type_of_hh = Initial(
    lambda: passenger_fleet_demand()
    .loc[:, :, _subscript_dict["PUBLIC_TRANSPORT_I"], :]
    .rename({"PASSENGERS_TRANSPORT_MODE_I": "PUBLIC_TRANSPORT_I"}),
    "_initial_initial_passenger_public_fleet_by_type_of_hh",
)


@component.add(
    name="initial_passenger_transport_demand_per_capita_by_GDPpc",
    units="Year*km*person/Mdollars_2015",
    subscripts=["REGIONS_35_I"],
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_initial_passenger_transport_demand_per_capita_by_gdppc": 1},
    other_deps={
        "_initial_initial_passenger_transport_demand_per_capita_by_gdppc": {
            "initial": {"passenger_transport_demand_per_capita_by_gdppc": 1},
            "step": {},
        }
    },
)
def initial_passenger_transport_demand_per_capita_by_gdppc():
    return _initial_initial_passenger_transport_demand_per_capita_by_gdppc()


_initial_initial_passenger_transport_demand_per_capita_by_gdppc = Initial(
    lambda: passenger_transport_demand_per_capita_by_gdppc(),
    "_initial_initial_passenger_transport_demand_per_capita_by_gdppc",
)


@component.add(
    name="initial_passenger_vehicle_fleet",
    units="vehicles",
    subscripts=[
        "REGIONS_35_I",
        "TRANSPORT_POWER_TRAIN_I",
        "PRIVATE_TRANSPORT_I",
        "HOUSEHOLDS_I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_hh_transport_disaggregated": 1,
        "initial_passenger_private_fleet_by_type_of_hh": 1,
        "initial_passenger_private_fleet_1_type_hh": 1,
    },
)
def initial_passenger_vehicle_fleet():
    return if_then_else(
        switch_hh_transport_disaggregated() == 1,
        lambda: initial_passenger_private_fleet_by_type_of_hh(),
        lambda: initial_passenger_private_fleet_1_type_hh(),
    )


@component.add(
    name="initial_public_passenger_vehicle_fleet",
    units="vehicles",
    subscripts=[
        "REGIONS_35_I",
        "TRANSPORT_POWER_TRAIN_I",
        "PUBLIC_TRANSPORT_I",
        "HOUSEHOLDS_I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_hh_transport_disaggregated": 1,
        "initial_passenger_public_fleet_by_type_of_hh": 1,
        "initial_public_passenger_vehicle_fleet_1_type_of_hh": 1,
    },
)
def initial_public_passenger_vehicle_fleet():
    return if_then_else(
        switch_hh_transport_disaggregated() == 1,
        lambda: initial_passenger_public_fleet_by_type_of_hh(),
        lambda: initial_public_passenger_vehicle_fleet_1_type_of_hh(),
    )


@component.add(
    name="initial_public_passenger_vehicle_fleet_1_type_of_HH",
    units="vehicles",
    subscripts=[
        "REGIONS_35_I",
        "TRANSPORT_POWER_TRAIN_I",
        "PUBLIC_TRANSPORT_I",
        "HOUSEHOLDS_I",
    ],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={"initial_passengers_public_fleet": 1},
)
def initial_public_passenger_vehicle_fleet_1_type_of_hh():
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
            "PUBLIC_TRANSPORT_I": _subscript_dict["PUBLIC_TRANSPORT_I"],
            "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
        },
        [
            "REGIONS_35_I",
            "TRANSPORT_POWER_TRAIN_I",
            "PUBLIC_TRANSPORT_I",
            "HOUSEHOLDS_I",
        ],
    )
    value.loc[:, :, :, ["REPRESENTATIVE_HOUSEHOLD"]] = (
        initial_passengers_public_fleet()
        .expand_dims({"HOUSEHOLDS_I": ["REPRESENTATIVE_HOUSEHOLD"]}, 3)
        .values
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, :, :, ["REPRESENTATIVE_HOUSEHOLD"]] = False
    value.values[except_subs.values] = 0
    return value


@component.add(
    name="lifetime_passenger_vehicles",
    units="Years",
    subscripts=[
        "REGIONS_35_I",
        "TRANSPORT_POWER_TRAIN_I",
        "PASSENGERS_TRANSPORT_MODE_I",
        "HOUSEHOLDS_I",
    ],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "mileage_vehicles": 10,
        "desired_passenger_vehicle_distance": 10,
        "max_lifetime_passenger_vehicles": 5,
        "initial_lifetime_passengers_vehicles": 1,
        "mod_passenger_vehicles_lifetime": 5,
        "battery_lifetime": 1,
        "lifetime_electrified_vehicle_batteries": 25,
    },
)
def lifetime_passenger_vehicles():
    """
    Lifetime vehicles data modified. --Eq-- MAX(MIN(ZIDZ(MILEAGE_VEHICLES[BEV,LDV],desired_passengers_vehicle_distance[REGIONS 35 I,BEV ,LDV,HOUSEHOLDS I] )*mod_passengers_lifetime[REGIONS 35 I,BEV,LDV], MIN(lifetime_electrified_vehicle_batteries[REGIONS 35 I,LMO,BEV,LDV], MIN(lifetime_electrified_vehicle_batteries[REGIONS 35 I,NMC622,BEV,LDV], MIN(lifetime_electrified_vehicle_batteries[REGIONS 35 I,NMC811,BEV,LDV], MIN(lifetime_electrified_vehicle_batteries[REGIONS 35 I,NCA,BEV,LDV], lifetime_electrified_vehicle_batteries[REGIONS 35 I,LFP,BEV,LDV]))))),1)
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
            "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict[
                "PASSENGERS_TRANSPORT_MODE_I"
            ],
            "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
        },
        [
            "REGIONS_35_I",
            "TRANSPORT_POWER_TRAIN_I",
            "PASSENGERS_TRANSPORT_MODE_I",
            "HOUSEHOLDS_I",
        ],
    )
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[:, :, _subscript_dict["PUBLIC_TRANSPORT_I"], :] = True
    except_subs.loc[:, :, ["bus"], :] = False
    value.values[except_subs.values] = (
        np.maximum(
            np.minimum(
                zidz(
                    mileage_vehicles()
                    .loc[:, _subscript_dict["PUBLIC_TRANSPORT_I"]]
                    .rename({"TRANSPORT_MODE_I": "PUBLIC_TRANSPORT_I"})
                    .expand_dims({"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]}, 2)
                    .expand_dims({"HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"]}, 3),
                    desired_passenger_vehicle_distance()
                    .loc[:, :, _subscript_dict["PUBLIC_TRANSPORT_I"], :]
                    .rename({"PASSENGERS_TRANSPORT_MODE_I": "PUBLIC_TRANSPORT_I"})
                    .transpose(
                        "TRANSPORT_POWER_TRAIN_I",
                        "PUBLIC_TRANSPORT_I",
                        "REGIONS_35_I",
                        "HOUSEHOLDS_I",
                    ),
                ),
                max_lifetime_passenger_vehicles()
                .loc[_subscript_dict["PUBLIC_TRANSPORT_I"]]
                .rename({"TRANSPORT_MODE_I": "PUBLIC_TRANSPORT_I"}),
            ),
            initial_lifetime_passengers_vehicles()
            .loc[_subscript_dict["PUBLIC_TRANSPORT_I"]]
            .rename({"TRANSPORT_MODE_I": "PUBLIC_TRANSPORT_I"}),
        )
        .transpose(
            "REGIONS_35_I",
            "TRANSPORT_POWER_TRAIN_I",
            "PUBLIC_TRANSPORT_I",
            "HOUSEHOLDS_I",
        )
        .values[except_subs.loc[:, :, _subscript_dict["PUBLIC_TRANSPORT_I"], :].values]
    )
    value.loc[:, :, ["NMT"], :] = 0
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[:, :, ["LDV"], :] = True
    except_subs.loc[:, ["BEV"], ["LDV"], :] = False
    except_subs.loc[:, ["PHEV"], ["LDV"], :] = False
    value.values[except_subs.values] = (
        np.minimum(
            np.maximum(
                1,
                zidz(
                    mileage_vehicles()
                    .loc[:, "LDV"]
                    .reset_coords(drop=True)
                    .expand_dims({"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]}, 1)
                    .expand_dims({"HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"]}, 2),
                    desired_passenger_vehicle_distance()
                    .loc[:, :, "LDV", :]
                    .reset_coords(drop=True)
                    .transpose(
                        "TRANSPORT_POWER_TRAIN_I", "REGIONS_35_I", "HOUSEHOLDS_I"
                    ),
                )
                * mod_passenger_vehicles_lifetime()
                .loc[:, :, "LDV"]
                .reset_coords(drop=True)
                .transpose("TRANSPORT_POWER_TRAIN_I", "REGIONS_35_I"),
            ),
            float(max_lifetime_passenger_vehicles().loc["LDV"]),
        )
        .transpose("REGIONS_35_I", "TRANSPORT_POWER_TRAIN_I", "HOUSEHOLDS_I")
        .expand_dims({"BATTERY_VEHICLES_I": ["LDV"]}, 2)
        .values[except_subs.loc[:, :, ["LDV"], :].values]
    )
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[:, :, ["bus"], :] = True
    except_subs.loc[:, ["BEV"], ["bus"], :] = False
    except_subs.loc[:, ["PHEV"], ["bus"], :] = False
    value.values[except_subs.values] = (
        np.minimum(
            np.maximum(
                1,
                zidz(
                    mileage_vehicles()
                    .loc[:, "bus"]
                    .reset_coords(drop=True)
                    .expand_dims({"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]}, 1)
                    .expand_dims({"HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"]}, 2),
                    desired_passenger_vehicle_distance()
                    .loc[:, :, "bus", :]
                    .reset_coords(drop=True)
                    .transpose(
                        "TRANSPORT_POWER_TRAIN_I", "REGIONS_35_I", "HOUSEHOLDS_I"
                    ),
                ),
            ),
            float(max_lifetime_passenger_vehicles().loc["bus"]),
        )
        .transpose("REGIONS_35_I", "TRANSPORT_POWER_TRAIN_I", "HOUSEHOLDS_I")
        .expand_dims({"BATTERY_VEHICLES_I": ["bus"]}, 2)
        .values[except_subs.loc[:, :, ["bus"], :].values]
    )
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[:, :, ["MOTORCYCLES_2W_3W"], :] = True
    except_subs.loc[:, ["BEV"], ["MOTORCYCLES_2W_3W"], :] = False
    except_subs.loc[:, ["PHEV"], ["MOTORCYCLES_2W_3W"], :] = False
    value.values[except_subs.values] = (
        np.minimum(
            np.maximum(
                1,
                zidz(
                    mileage_vehicles()
                    .loc[:, "MOTORCYCLES_2W_3W"]
                    .reset_coords(drop=True)
                    .expand_dims({"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]}, 1)
                    .expand_dims({"HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"]}, 2),
                    desired_passenger_vehicle_distance()
                    .loc[:, :, "MOTORCYCLES_2W_3W", :]
                    .reset_coords(drop=True)
                    .transpose(
                        "TRANSPORT_POWER_TRAIN_I", "REGIONS_35_I", "HOUSEHOLDS_I"
                    ),
                )
                * mod_passenger_vehicles_lifetime()
                .loc[:, :, "MOTORCYCLES_2W_3W"]
                .reset_coords(drop=True)
                .transpose("TRANSPORT_POWER_TRAIN_I", "REGIONS_35_I"),
            ),
            float(max_lifetime_passenger_vehicles().loc["MOTORCYCLES_2W_3W"]),
        )
        .transpose("REGIONS_35_I", "TRANSPORT_POWER_TRAIN_I", "HOUSEHOLDS_I")
        .expand_dims({"BATTERY_VEHICLES_I": ["MOTORCYCLES_2W_3W"]}, 2)
        .values[except_subs.loc[:, :, ["MOTORCYCLES_2W_3W"], :].values]
    )
    value.loc[:, ["BEV"], ["LDV"], :] = (
        np.minimum(
            np.minimum(
                battery_lifetime().loc[:, "BEV", "LDV", :].reset_coords(drop=True),
                zidz(
                    xr.DataArray(
                        float(mileage_vehicles().loc["BEV", "LDV"]),
                        {
                            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                            "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
                        },
                        ["REGIONS_35_I", "HOUSEHOLDS_I"],
                    ),
                    desired_passenger_vehicle_distance()
                    .loc[:, "BEV", "LDV", :]
                    .reset_coords(drop=True),
                ),
            ),
            float(max_lifetime_passenger_vehicles().loc["LDV"]),
        )
        .expand_dims({"TRANSPORT_POWER_TRAIN_I": ["BEV"]}, 1)
        .expand_dims({"BATTERY_VEHICLES_I": ["LDV"]}, 2)
        .values
    )
    value.loc[:, ["PHEV"], ["LDV"], :] = (
        np.maximum(
            np.minimum(
                zidz(
                    xr.DataArray(
                        float(mileage_vehicles().loc["PHEV", "LDV"]),
                        {
                            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                            "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
                        },
                        ["REGIONS_35_I", "HOUSEHOLDS_I"],
                    ),
                    desired_passenger_vehicle_distance()
                    .loc[:, "PHEV", "LDV", :]
                    .reset_coords(drop=True),
                )
                * mod_passenger_vehicles_lifetime()
                .loc[:, "PHEV", "LDV"]
                .reset_coords(drop=True),
                np.minimum(
                    lifetime_electrified_vehicle_batteries()
                    .loc[:, "LMO", "PHEV", "LDV"]
                    .reset_coords(drop=True),
                    np.minimum(
                        lifetime_electrified_vehicle_batteries()
                        .loc[:, "NMC622", "PHEV", "LDV"]
                        .reset_coords(drop=True),
                        np.minimum(
                            lifetime_electrified_vehicle_batteries()
                            .loc[:, "NMC811", "PHEV", "LDV"]
                            .reset_coords(drop=True),
                            np.minimum(
                                lifetime_electrified_vehicle_batteries()
                                .loc[:, "NCA", "PHEV", "LDV"]
                                .reset_coords(drop=True),
                                lifetime_electrified_vehicle_batteries()
                                .loc[:, "LFP", "PHEV", "LDV"]
                                .reset_coords(drop=True),
                            ),
                        ),
                    ),
                ),
            ),
            1,
        )
        .expand_dims({"TRANSPORT_POWER_TRAIN_I": ["PHEV"]}, 1)
        .expand_dims({"BATTERY_VEHICLES_I": ["LDV"]}, 2)
        .values
    )
    value.loc[:, ["BEV"], ["bus"], :] = (
        np.maximum(
            np.minimum(
                zidz(
                    xr.DataArray(
                        float(mileage_vehicles().loc["BEV", "bus"]),
                        {
                            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                            "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
                        },
                        ["REGIONS_35_I", "HOUSEHOLDS_I"],
                    ),
                    desired_passenger_vehicle_distance()
                    .loc[:, "BEV", "bus", :]
                    .reset_coords(drop=True),
                ),
                np.minimum(
                    lifetime_electrified_vehicle_batteries()
                    .loc[:, "LMO", "BEV", "bus"]
                    .reset_coords(drop=True),
                    np.minimum(
                        lifetime_electrified_vehicle_batteries()
                        .loc[:, "NMC622", "BEV", "bus"]
                        .reset_coords(drop=True),
                        np.minimum(
                            lifetime_electrified_vehicle_batteries()
                            .loc[:, "NMC811", "BEV", "bus"]
                            .reset_coords(drop=True),
                            np.minimum(
                                lifetime_electrified_vehicle_batteries()
                                .loc[:, "NCA", "BEV", "bus"]
                                .reset_coords(drop=True),
                                lifetime_electrified_vehicle_batteries()
                                .loc[:, "LFP", "BEV", "bus"]
                                .reset_coords(drop=True),
                            ),
                        ),
                    ),
                ),
            ),
            1,
        )
        .expand_dims({"TRANSPORT_POWER_TRAIN_I": ["BEV"]}, 1)
        .expand_dims({"BATTERY_VEHICLES_I": ["bus"]}, 2)
        .values
    )
    value.loc[:, ["PHEV"], ["bus"], :] = (
        np.maximum(
            np.minimum(
                zidz(
                    xr.DataArray(
                        float(mileage_vehicles().loc["PHEV", "bus"]),
                        {
                            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                            "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
                        },
                        ["REGIONS_35_I", "HOUSEHOLDS_I"],
                    ),
                    desired_passenger_vehicle_distance()
                    .loc[:, "PHEV", "bus", :]
                    .reset_coords(drop=True),
                ),
                np.minimum(
                    lifetime_electrified_vehicle_batteries()
                    .loc[:, "LMO", "PHEV", "bus"]
                    .reset_coords(drop=True),
                    np.minimum(
                        lifetime_electrified_vehicle_batteries()
                        .loc[:, "NMC622", "PHEV", "bus"]
                        .reset_coords(drop=True),
                        np.minimum(
                            lifetime_electrified_vehicle_batteries()
                            .loc[:, "NMC811", "PHEV", "bus"]
                            .reset_coords(drop=True),
                            np.minimum(
                                lifetime_electrified_vehicle_batteries()
                                .loc[:, "NCA", "PHEV", "bus"]
                                .reset_coords(drop=True),
                                lifetime_electrified_vehicle_batteries()
                                .loc[:, "LFP", "PHEV", "bus"]
                                .reset_coords(drop=True),
                            ),
                        ),
                    ),
                ),
            ),
            1,
        )
        .expand_dims({"TRANSPORT_POWER_TRAIN_I": ["PHEV"]}, 1)
        .expand_dims({"BATTERY_VEHICLES_I": ["bus"]}, 2)
        .values
    )
    value.loc[:, ["BEV"], ["MOTORCYCLES_2W_3W"], :] = (
        np.maximum(
            np.minimum(
                zidz(
                    xr.DataArray(
                        float(mileage_vehicles().loc["BEV", "MOTORCYCLES_2W_3W"]),
                        {
                            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                            "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
                        },
                        ["REGIONS_35_I", "HOUSEHOLDS_I"],
                    ),
                    desired_passenger_vehicle_distance()
                    .loc[:, "BEV", "MOTORCYCLES_2W_3W", :]
                    .reset_coords(drop=True),
                )
                * mod_passenger_vehicles_lifetime()
                .loc[:, "BEV", "MOTORCYCLES_2W_3W"]
                .reset_coords(drop=True),
                np.minimum(
                    lifetime_electrified_vehicle_batteries()
                    .loc[:, "LMO", "BEV", "MOTORCYCLES_2W_3W"]
                    .reset_coords(drop=True),
                    np.minimum(
                        lifetime_electrified_vehicle_batteries()
                        .loc[:, "NMC622", "BEV", "MOTORCYCLES_2W_3W"]
                        .reset_coords(drop=True),
                        np.minimum(
                            lifetime_electrified_vehicle_batteries()
                            .loc[:, "NMC811", "BEV", "MOTORCYCLES_2W_3W"]
                            .reset_coords(drop=True),
                            np.minimum(
                                lifetime_electrified_vehicle_batteries()
                                .loc[:, "NCA", "BEV", "MOTORCYCLES_2W_3W"]
                                .reset_coords(drop=True),
                                lifetime_electrified_vehicle_batteries()
                                .loc[:, "LFP", "BEV", "MOTORCYCLES_2W_3W"]
                                .reset_coords(drop=True),
                            ),
                        ),
                    ),
                ),
            ),
            1,
        )
        .expand_dims({"TRANSPORT_POWER_TRAIN_I": ["BEV"]}, 1)
        .expand_dims({"BATTERY_VEHICLES_I": ["MOTORCYCLES_2W_3W"]}, 2)
        .values
    )
    value.loc[:, ["PHEV"], ["MOTORCYCLES_2W_3W"], :] = (
        np.maximum(
            np.minimum(
                zidz(
                    xr.DataArray(
                        float(mileage_vehicles().loc["PHEV", "MOTORCYCLES_2W_3W"]),
                        {
                            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                            "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
                        },
                        ["REGIONS_35_I", "HOUSEHOLDS_I"],
                    ),
                    desired_passenger_vehicle_distance()
                    .loc[:, "PHEV", "MOTORCYCLES_2W_3W", :]
                    .reset_coords(drop=True),
                )
                * mod_passenger_vehicles_lifetime()
                .loc[:, "PHEV", "MOTORCYCLES_2W_3W"]
                .reset_coords(drop=True),
                np.minimum(
                    lifetime_electrified_vehicle_batteries()
                    .loc[:, "LMO", "PHEV", "MOTORCYCLES_2W_3W"]
                    .reset_coords(drop=True),
                    np.minimum(
                        lifetime_electrified_vehicle_batteries()
                        .loc[:, "NMC622", "PHEV", "MOTORCYCLES_2W_3W"]
                        .reset_coords(drop=True),
                        np.minimum(
                            lifetime_electrified_vehicle_batteries()
                            .loc[:, "NMC811", "PHEV", "MOTORCYCLES_2W_3W"]
                            .reset_coords(drop=True),
                            np.minimum(
                                lifetime_electrified_vehicle_batteries()
                                .loc[:, "NCA", "PHEV", "MOTORCYCLES_2W_3W"]
                                .reset_coords(drop=True),
                                lifetime_electrified_vehicle_batteries()
                                .loc[:, "LFP", "PHEV", "MOTORCYCLES_2W_3W"]
                                .reset_coords(drop=True),
                            ),
                        ),
                    ),
                ),
            ),
            1,
        )
        .expand_dims({"TRANSPORT_POWER_TRAIN_I": ["PHEV"]}, 1)
        .expand_dims({"BATTERY_VEHICLES_I": ["MOTORCYCLES_2W_3W"]}, 2)
        .values
    )
    return value


@component.add(
    name="load_factor_LDV",
    units="persons/vehicle",
    subscripts=["REGIONS_35_I", "TRANSPORT_POWER_TRAIN_I", "HOUSEHOLDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "passenger_transport_real_supply": 1,
        "private_passenger_vehicle_fleet": 1,
        "desired_passenger_vehicle_distance": 1,
    },
)
def load_factor_ldv():
    """
    Load factor of LDV vechiles by power train and type of household, in persons/vehicle.
    """
    return zidz(
        passenger_transport_real_supply().loc[:, :, "LDV", :].reset_coords(drop=True),
        desired_passenger_vehicle_distance().loc[:, :, "LDV", :].reset_coords(drop=True)
        * private_passenger_vehicle_fleet().loc[:, :, "LDV", :].reset_coords(drop=True),
    )


@component.add(
    name="load_factor_passenger_commercial_vehicles",
    units="persons/vehicle",
    subscripts=[
        "REGIONS_35_I",
        "TRANSPORT_POWER_TRAIN_I",
        "PUBLIC_TRANSPORT_I",
        "HOUSEHOLDS_I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "passenger_transport_real_supply": 1,
        "public_passenger_vehicle_fleet": 1,
        "desired_passenger_vehicle_distance": 1,
    },
)
def load_factor_passenger_commercial_vehicles():
    """
    Load factor of public vehicle transport by region, power train, public trasnport mode and type of household in persons/vehicle.
    """
    return zidz(
        passenger_transport_real_supply()
        .loc[:, :, _subscript_dict["PUBLIC_TRANSPORT_I"], :]
        .rename({"PASSENGERS_TRANSPORT_MODE_I": "PUBLIC_TRANSPORT_I"}),
        public_passenger_vehicle_fleet()
        * desired_passenger_vehicle_distance()
        .loc[:, :, _subscript_dict["PUBLIC_TRANSPORT_I"], :]
        .rename({"PASSENGERS_TRANSPORT_MODE_I": "PUBLIC_TRANSPORT_I"}),
    )


@component.add(
    name="MAX_LIFETIME_PASSENGER_VEHICLES",
    units="Years",
    subscripts=["TRANSPORT_MODE_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_max_lifetime_passenger_vehicles"},
)
def max_lifetime_passenger_vehicles():
    return _ext_constant_max_lifetime_passenger_vehicles()


_ext_constant_max_lifetime_passenger_vehicles = ExtConstant(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "MAX_LIFETIME_PASSENGER_VEHICLES*",
    {"TRANSPORT_MODE_I": _subscript_dict["TRANSPORT_MODE_I"]},
    _root,
    {"TRANSPORT_MODE_I": _subscript_dict["TRANSPORT_MODE_I"]},
    "_ext_constant_max_lifetime_passenger_vehicles",
)


@component.add(
    name="MAXIMUM_LOAD_FACTOR",
    units="persons/vehicle",
    subscripts=["PASSENGERS_TRANSPORT_MODE_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_maximum_load_factor"},
)
def maximum_load_factor():
    return _ext_constant_maximum_load_factor()


_ext_constant_maximum_load_factor = ExtConstant(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "MAX_LOAD_FACTOR*",
    {"PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"]},
    _root,
    {"PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"]},
    "_ext_constant_maximum_load_factor",
)


@component.add(
    name="mobility_passenger_transport_intensity",
    units="MJ/(person*km)",
    subscripts=[
        "REGIONS_35_I",
        "TRANSPORT_POWER_TRAIN_I",
        "PASSENGERS_TRANSPORT_MODE_I",
        "HOUSEHOLDS_I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "passenger_transport_fuel_consumption_efficiency": 1,
        "modified_load_factor_passenger_transport": 1,
    },
)
def mobility_passenger_transport_intensity():
    """
    Energy vehicle consumption modified by efficiency change and load factor policies by region, power train and transport mode in MJ/(person*km)
    """
    return zidz(
        passenger_transport_fuel_consumption_efficiency().expand_dims(
            {"HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"]}, 3
        ),
        modified_load_factor_passenger_transport(),
    )


@component.add(
    name="mod_passenger_vehicles_lifetime",
    units="1",
    subscripts=["REGIONS_35_I", "TRANSPORT_POWER_TRAIN_I", "PRIVATE_TRANSPORT_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"passenger_fleet_demand": 1, "private_passenger_vehicle_fleet": 1},
)
def mod_passenger_vehicles_lifetime():
    """
    Modifier of private vehicle lifetime in function of vehicle stock and demand of new vehciles. This variable endogenizes the behavioral change of the users in relation to the lifetime extension of the vehicles, it is designed to modify the lifetime in case the demand for cars is higher than the operational fleet in order not to increase so much the purchase of new vehicles in the short term.
    """
    return np.maximum(
        0.5,
        zidz(
            sum(
                passenger_fleet_demand()
                .loc[:, :, _subscript_dict["PRIVATE_TRANSPORT_I"], :]
                .rename(
                    {
                        "PASSENGERS_TRANSPORT_MODE_I": "PRIVATE_TRANSPORT_I",
                        "HOUSEHOLDS_I": "HOUSEHOLDS_I!",
                    }
                ),
                dim=["HOUSEHOLDS_I!"],
            ),
            sum(
                private_passenger_vehicle_fleet().rename(
                    {"HOUSEHOLDS_I": "HOUSEHOLDS_I!"}
                ),
                dim=["HOUSEHOLDS_I!"],
            ),
        ),
    )


@component.add(
    name="modal_split",
    subscripts=["REGIONS_35_I", "PASSENGERS_TRANSPORT_MODE_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"modal_split_exc_ldv_adjusted": 2},
)
def modal_split():
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict[
                "PASSENGERS_TRANSPORT_MODE_I"
            ],
        },
        ["REGIONS_35_I", "PASSENGERS_TRANSPORT_MODE_I"],
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, ["LDV"]] = False
    value.values[except_subs.values] = modal_split_exc_ldv_adjusted().values[
        except_subs.values
    ]
    value.loc[:, ["LDV"]] = (
        (
            1
            - sum(
                modal_split_exc_ldv_adjusted().rename(
                    {"PASSENGERS_TRANSPORT_MODE_I": "PASSENGERS_TRANSPORT_MODE_I!"}
                ),
                dim=["PASSENGERS_TRANSPORT_MODE_I!"],
            )
        )
        .expand_dims({"BATTERY_VEHICLES_I": ["LDV"]}, 1)
        .values
    )
    return value


@component.add(
    name="modal_split_bus",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"modal_split_public": 1, "sub_share_bus": 1},
)
def modal_split_bus():
    return modal_split_public() * sub_share_bus()


@component.add(
    name="modal_split_exc_LDV",
    subscripts=["REGIONS_35_I", "PASSENGERS_TRANSPORT_MODE_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "objective_passenger_transport_demand_modal_share_sp": 1,
        "modal_split_bus": 1,
        "modal_split_rail": 1,
    },
)
def modal_split_exc_ldv():
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict[
                "PASSENGERS_TRANSPORT_MODE_I"
            ],
        },
        ["REGIONS_35_I", "PASSENGERS_TRANSPORT_MODE_I"],
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, ["bus"]] = False
    except_subs.loc[:, ["RAIL"]] = False
    except_subs.loc[:, ["LDV"]] = False
    value.values[except_subs.values] = sum(
        objective_passenger_transport_demand_modal_share_sp().rename(
            {"TRANSPORT_POWER_TRAIN_I": "TRANSPORT_POWER_TRAIN_I!"}
        ),
        dim=["TRANSPORT_POWER_TRAIN_I!"],
    ).values[except_subs.values]
    value.loc[:, ["bus"]] = (
        modal_split_bus().expand_dims({"BATTERY_VEHICLES_I": ["bus"]}, 1).values
    )
    value.loc[:, ["RAIL"]] = (
        modal_split_rail().expand_dims({"FREIGHT_TRANSPORT_MODE_I": ["RAIL"]}, 1).values
    )
    value.loc[:, ["LDV"]] = 0
    return value


@component.add(
    name="modal_split_exc_LDV_adjusted",
    units="DMNL",
    subscripts=["REGIONS_35_I", "PASSENGERS_TRANSPORT_MODE_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"modal_split_exc_ldv": 4},
)
def modal_split_exc_ldv_adjusted():
    """
    Adjustmento of modal split when shares >1
    """
    return if_then_else(
        (
            sum(
                modal_split_exc_ldv().rename(
                    {"PASSENGERS_TRANSPORT_MODE_I": "PASSENGERS_TRANSPORT_MODE_I!"}
                ),
                dim=["PASSENGERS_TRANSPORT_MODE_I!"],
            )
            > 1
        ).expand_dims(
            {
                "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict[
                    "PASSENGERS_TRANSPORT_MODE_I"
                ]
            },
            1,
        ),
        lambda: zidz(
            modal_split_exc_ldv(),
            sum(
                modal_split_exc_ldv().rename(
                    {"PASSENGERS_TRANSPORT_MODE_I": "PASSENGERS_TRANSPORT_MODE_I!"}
                ),
                dim=["PASSENGERS_TRANSPORT_MODE_I!"],
            ).expand_dims(
                {
                    "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict[
                        "PASSENGERS_TRANSPORT_MODE_I"
                    ]
                },
                1,
            ),
        ),
        lambda: modal_split_exc_ldv(),
    )


@component.add(
    name="modal_split_public",
    units="DMNL",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "constant_modal_split_public": 1,
        "delayed_ts_price_output": 1,
        "sigma_public": 1,
        "base_price_output": 1,
        "time": 1,
        "trend_public": 1,
    },
)
def modal_split_public():
    """
    Share of pulbic transport calcualted as a funciton of the price of fuel and a trend
    """
    return np.exp(
        constant_modal_split_public()
        + sigma_public()
        * np.log(
            zidz(
                delayed_ts_price_output().loc[:, "REFINING"].reset_coords(drop=True),
                base_price_output().loc[:, "REFINING"].reset_coords(drop=True),
            )
        )
        + trend_public() * (time() - 2015)
    )


@component.add(
    name="modal_split_rail",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"modal_split_public": 1, "sub_share_rail": 1},
)
def modal_split_rail():
    return modal_split_public() * sub_share_rail()


@component.add(
    name="modified_load_factor_passenger_transport",
    units="persons/vehicle",
    subscripts=[
        "REGIONS_35_I",
        "TRANSPORT_POWER_TRAIN_I",
        "PASSENGERS_TRANSPORT_MODE_I",
        "HOUSEHOLDS_I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_load_factor_mod_sp": 2,
        "initial_load_factor_passengers_vehicles": 5,
        "objective_load_factor_mod_sp": 1,
        "year_initial_load_factor_mod_sp": 3,
        "maximum_load_factor": 1,
        "time": 2,
        "year_final_load_factor_mod_sp": 2,
    },
)
def modified_load_factor_passenger_transport():
    """
    Vehicle load factor modified with the behavioral change variable
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
            "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict[
                "PASSENGERS_TRANSPORT_MODE_I"
            ],
            "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
        },
        [
            "REGIONS_35_I",
            "TRANSPORT_POWER_TRAIN_I",
            "PASSENGERS_TRANSPORT_MODE_I",
            "HOUSEHOLDS_I",
        ],
    )
    value.loc[:, :, _subscript_dict["PRIVATE_TRANSPORT_I"], :] = (
        if_then_else(
            switch_load_factor_mod_sp() == 0,
            lambda: initial_load_factor_passengers_vehicles()
            .loc[:, :, _subscript_dict["PRIVATE_TRANSPORT_I"]]
            .rename({"PASSENGERS_TRANSPORT_MODE_I": "PRIVATE_TRANSPORT_I"}),
            lambda: if_then_else(
                np.logical_and(
                    switch_load_factor_mod_sp() == 1,
                    time() < year_initial_load_factor_mod_sp(),
                ),
                lambda: initial_load_factor_passengers_vehicles()
                .loc[:, :, _subscript_dict["PRIVATE_TRANSPORT_I"]]
                .rename({"PASSENGERS_TRANSPORT_MODE_I": "PRIVATE_TRANSPORT_I"}),
                lambda: np.minimum(
                    maximum_load_factor()
                    .loc[_subscript_dict["PRIVATE_TRANSPORT_I"]]
                    .rename({"PASSENGERS_TRANSPORT_MODE_I": "PRIVATE_TRANSPORT_I"}),
                    (
                        initial_load_factor_passengers_vehicles()
                        .loc[:, :, _subscript_dict["PRIVATE_TRANSPORT_I"]]
                        .rename({"PASSENGERS_TRANSPORT_MODE_I": "PRIVATE_TRANSPORT_I"})
                        + ramp(
                            __data["time"],
                            (
                                objective_load_factor_mod_sp()
                                - initial_load_factor_passengers_vehicles()
                                .loc[:, :, _subscript_dict["PRIVATE_TRANSPORT_I"]]
                                .rename(
                                    {
                                        "PASSENGERS_TRANSPORT_MODE_I": "PRIVATE_TRANSPORT_I"
                                    }
                                )
                                .transpose(
                                    "PRIVATE_TRANSPORT_I",
                                    "REGIONS_35_I",
                                    "TRANSPORT_POWER_TRAIN_I",
                                )
                            )
                            / (
                                year_final_load_factor_mod_sp()
                                - year_initial_load_factor_mod_sp()
                            ),
                            year_initial_load_factor_mod_sp(),
                            year_final_load_factor_mod_sp(),
                        ).transpose(
                            "REGIONS_35_I",
                            "TRANSPORT_POWER_TRAIN_I",
                            "PRIVATE_TRANSPORT_I",
                        )
                    ).transpose(
                        "PRIVATE_TRANSPORT_I", "REGIONS_35_I", "TRANSPORT_POWER_TRAIN_I"
                    ),
                ).transpose(
                    "REGIONS_35_I", "TRANSPORT_POWER_TRAIN_I", "PRIVATE_TRANSPORT_I"
                ),
            ),
        )
        .expand_dims({"HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"]}, 3)
        .values
    )
    value.loc[:, :, _subscript_dict["PUBLIC_TRANSPORT_I"], :] = (
        initial_load_factor_passengers_vehicles()
        .loc[:, :, _subscript_dict["PUBLIC_TRANSPORT_I"]]
        .rename({"PASSENGERS_TRANSPORT_MODE_I": "PUBLIC_TRANSPORT_I"})
        .expand_dims({"HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"]}, 3)
        .values
    )
    return value


@component.add(
    name="new_passenger_private_vehicles",
    units="vehicle/Year",
    subscripts=[
        "REGIONS_35_I",
        "TRANSPORT_POWER_TRAIN_I",
        "PRIVATE_TRANSPORT_I",
        "HOUSEHOLDS_I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "passenger_fleet_demand": 2,
        "private_passenger_vehicle_fleet": 2,
        "factor_passengers_private_fleet": 1,
    },
)
def new_passenger_private_vehicles():
    """
    New private vehicle flow by region, power train, private transport mode and type of household, in number of vehicles/year. MAX(0, MIN(MAXIMUM_BUDGET_FOR_VEHICLES[transport mode,type household]/PRICE_PER_VEHICLE[transport mode,type household], (Vehicle_fleet_demand[transport mode,type household]-vehicle_fleet[transport mode,type household])*FACTOR))
    """
    return if_then_else(
        passenger_fleet_demand()
        .loc[:, :, _subscript_dict["PRIVATE_TRANSPORT_I"], :]
        .rename({"PASSENGERS_TRANSPORT_MODE_I": "PRIVATE_TRANSPORT_I"})
        < private_passenger_vehicle_fleet(),
        lambda: xr.DataArray(
            0,
            {
                "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
                "PRIVATE_TRANSPORT_I": _subscript_dict["PRIVATE_TRANSPORT_I"],
                "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
            },
            [
                "REGIONS_35_I",
                "TRANSPORT_POWER_TRAIN_I",
                "PRIVATE_TRANSPORT_I",
                "HOUSEHOLDS_I",
            ],
        ),
        lambda: (
            passenger_fleet_demand()
            .loc[:, :, _subscript_dict["PRIVATE_TRANSPORT_I"], :]
            .rename({"PASSENGERS_TRANSPORT_MODE_I": "PRIVATE_TRANSPORT_I"})
            - private_passenger_vehicle_fleet()
        )
        * factor_passengers_private_fleet(),
    )


@component.add(
    name="new_passenger_public_vehicles",
    units="vehicle/Year",
    subscripts=[
        "REGIONS_35_I",
        "TRANSPORT_POWER_TRAIN_I",
        "PUBLIC_TRANSPORT_I",
        "HOUSEHOLDS_I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "passenger_fleet_demand": 2,
        "public_passenger_vehicle_fleet": 2,
        "factor_passengers_public_fleet": 1,
    },
)
def new_passenger_public_vehicles():
    """
    New public vehicle flow by region, power train, public transport mode and type of household, in number of vehicles/year.
    """
    return if_then_else(
        passenger_fleet_demand()
        .loc[:, :, _subscript_dict["PUBLIC_TRANSPORT_I"], :]
        .rename({"PASSENGERS_TRANSPORT_MODE_I": "PUBLIC_TRANSPORT_I"})
        < public_passenger_vehicle_fleet(),
        lambda: xr.DataArray(
            0,
            {
                "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
                "PUBLIC_TRANSPORT_I": _subscript_dict["PUBLIC_TRANSPORT_I"],
                "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
            },
            [
                "REGIONS_35_I",
                "TRANSPORT_POWER_TRAIN_I",
                "PUBLIC_TRANSPORT_I",
                "HOUSEHOLDS_I",
            ],
        ),
        lambda: (
            passenger_fleet_demand()
            .loc[:, :, _subscript_dict["PUBLIC_TRANSPORT_I"], :]
            .rename({"PASSENGERS_TRANSPORT_MODE_I": "PUBLIC_TRANSPORT_I"})
            - public_passenger_vehicle_fleet()
        )
        * factor_passengers_public_fleet(),
    )


@component.add(
    name="new_private_passenger_vehicles",
    units="vehicles/Year",
    subscripts=["REGIONS_35_I", "TRANSPORT_POWER_TRAIN_I", "PRIVATE_TRANSPORT_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"new_passenger_private_vehicles": 1},
)
def new_private_passenger_vehicles():
    return (
        new_passenger_private_vehicles()
        .loc[:, :, :, "REPRESENTATIVE_HOUSEHOLD"]
        .reset_coords(drop=True)
    )


@component.add(
    name="new_public_passenger_vehicles",
    units="vehicles/Year",
    subscripts=["REGIONS_35_I", "TRANSPORT_POWER_TRAIN_I", "PUBLIC_TRANSPORT_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"new_passenger_public_vehicles": 1},
)
def new_public_passenger_vehicles():
    return (
        new_passenger_public_vehicles()
        .loc[:, :, :, "REPRESENTATIVE_HOUSEHOLD"]
        .reset_coords(drop=True)
    )


@component.add(
    name="objective_passenger_transport_demand_modal_share",
    subscripts=[
        "REGIONS_35_I",
        "TRANSPORT_POWER_TRAIN_I",
        "PASSENGERS_TRANSPORT_MODE_I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_static_transport_demand": 1,
        "passanger_transport_demand_modal_share_endogenous": 1,
        "objective_passenger_transport_demand_modal_share_sp": 1,
    },
)
def objective_passenger_transport_demand_modal_share():
    """
    Objective passenger transport demand modal share modified by final fuel prices. If SWITCH STATIC TRANSPORT DEMAND=1 the passenger transport demand modal share comes is modified by the prices, if not the modal share comes from the modal share matrix.
    """
    return if_then_else(
        switch_static_transport_demand() == 1,
        lambda: passanger_transport_demand_modal_share_endogenous(),
        lambda: objective_passenger_transport_demand_modal_share_sp(),
    )


@component.add(
    name="passanger_transport_demand_modal_share_endogenous",
    subscripts=[
        "REGIONS_35_I",
        "TRANSPORT_POWER_TRAIN_I",
        "PASSENGERS_TRANSPORT_MODE_I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "objective_passenger_transport_demand_modal_share_sp": 1,
        "modal_split": 1,
        "share_technologies_passanger_transport": 1,
    },
)
def passanger_transport_demand_modal_share_endogenous():
    """
    Shares of passanger transport demand by technology and mode
    """
    return if_then_else(
        time() < 2015,
        lambda: objective_passenger_transport_demand_modal_share_sp(),
        lambda: share_technologies_passanger_transport() * modal_split(),
    )


@component.add(
    name="passenger_fleet_demand",
    units="vehicle",
    subscripts=[
        "REGIONS_35_I",
        "TRANSPORT_POWER_TRAIN_I",
        "PASSENGERS_TRANSPORT_MODE_I",
        "HOUSEHOLDS_I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "desired_passengers_transport_demand_by_mode_and_type_of_households_modified": 1,
        "initial_passengers_vehicle_distance": 1,
        "modified_load_factor_passenger_transport": 1,
    },
)
def passenger_fleet_demand():
    """
    Vehicle fleet demand by region, power train, transport mode and type of household in vehicles.
    """
    return zidz(
        desired_passengers_transport_demand_by_mode_and_type_of_households_modified(),
        modified_load_factor_passenger_transport()
        * initial_passengers_vehicle_distance(),
    )


@component.add(
    name="passenger_transport_demand_corrected_by_GDPpc",
    units="km*person",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_static_transport_demand": 1,
        "desired_passenger_transport_demand": 1,
        "initial_passenger_transport_demand_per_capita_by_gdppc": 1,
        "exo_gdppc_real": 1,
        "population_35_regions": 1,
    },
)
def passenger_transport_demand_corrected_by_gdppc():
    """
    total transport demand by region in pass*km. --- EXO_GDPpc_real[REGIONS 35 I]*initial_passengers_transport_demand_per_capita_by_GDPpc[REGIONS 35 I]*population_35_regions [REGIONS 35 I ]
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
        },
        ["REGIONS_35_I", "HOUSEHOLDS_I"],
    )
    value.loc[:, ["REPRESENTATIVE_HOUSEHOLD"]] = (
        if_then_else(
            switch_static_transport_demand() == 1,
            lambda: desired_passenger_transport_demand(),
            lambda: exo_gdppc_real()
            * initial_passenger_transport_demand_per_capita_by_gdppc()
            * population_35_regions(),
        )
        .expand_dims({"HOUSEHOLDS_I": ["REPRESENTATIVE_HOUSEHOLD"]}, 1)
        .values
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, ["REPRESENTATIVE_HOUSEHOLD"]] = False
    value.values[except_subs.values] = 0
    return value


@component.add(
    name="passenger_transport_demand_per_capita_by_GDPpc",
    units="Year*km*person/Mdollars_2015",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "desired_passenger_transport_demand_per_capita": 1,
        "exo_gdppc_real": 1,
    },
)
def passenger_transport_demand_per_capita_by_gdppc():
    """
    Total transport demand per capita by unit of GDPpc.
    """
    return zidz(desired_passenger_transport_demand_per_capita(), exo_gdppc_real())


@component.add(
    name="passenger_transport_demand_public_fleet",
    units="persons*km",
    subscripts=["REGIONS_35_I", "PUBLIC_TRANSPORT_I", "HOUSEHOLDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"passenger_transport_real_supply_by_mode": 1},
)
def passenger_transport_demand_public_fleet():
    """
    Public transport supply by region, public transport mode and type of household after all policy and endogenous modifications, in persons*km.
    """
    return (
        passenger_transport_real_supply_by_mode()
        .loc[:, _subscript_dict["PUBLIC_TRANSPORT_I"], :]
        .rename({"PASSENGERS_TRANSPORT_MODE_I": "PUBLIC_TRANSPORT_I"})
    )


@component.add(
    name="passenger_transport_fuel_consumption_efficiency",
    units="MJ/(km*vehicles)",
    subscripts=[
        "REGIONS_35_I",
        "TRANSPORT_POWER_TRAIN_I",
        "PASSENGERS_TRANSPORT_MODE_I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "final_energy_consumption_initial": 1,
        "passenger_transport_fuel_consumption_efficiency_change": 1,
    },
)
def passenger_transport_fuel_consumption_efficiency():
    """
    Energy vehicle consumption modified by efficiency change policy by region, power train and transport mode in MJ/(vehicle*km)
    """
    return (
        final_energy_consumption_initial()
        * passenger_transport_fuel_consumption_efficiency_change()
    )


@component.add(
    name="passenger_transport_fuel_consumption_efficiency_change",
    units="DMNL",
    subscripts=[
        "REGIONS_35_I",
        "TRANSPORT_POWER_TRAIN_I",
        "PASSENGERS_TRANSPORT_MODE_I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_fuel_consumption_efficiency_change_sp": 2,
        "time": 2,
        "objective_fuel_consumption_efficiency_change_sp": 1,
        "year_initial_fuel_consumption_efficiency_change_sp": 3,
        "year_final_fuel_consumption_efficiency_change_sp": 2,
    },
)
def passenger_transport_fuel_consumption_efficiency_change():
    """
    (RAMP((OBJECTIVE_FUEL_CONSUMPTION_EFFICIENCY_CHANGE_SP[POWER_TRAIN_I,PASSENGERS_TRANS PORT_MODE_I])/ (YEAR_FINAL_FUEL_CONSUMPTION_EFFICIENCY_CHANGE_SP-YEAR_INITIAL_FUEL_CONSUMP TION_EFFICIENCY_CHANGE_SP),YEAR_INITIAL_FUEL_CONSUMPTION_EFFICIENCY_CHANGE_ SP,YEAR_FINAL_FUEL_CONSUMPTION_EFFICIENCY_CHANGE_SP))
    """
    return if_then_else(
        switch_fuel_consumption_efficiency_change_sp() == 0,
        lambda: xr.DataArray(
            1,
            {
                "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
                "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict[
                    "PASSENGERS_TRANSPORT_MODE_I"
                ],
            },
            ["TRANSPORT_POWER_TRAIN_I", "PASSENGERS_TRANSPORT_MODE_I"],
        ),
        lambda: if_then_else(
            np.logical_and(
                switch_fuel_consumption_efficiency_change_sp() == 1,
                time() < year_initial_fuel_consumption_efficiency_change_sp(),
            ),
            lambda: xr.DataArray(
                1,
                {
                    "TRANSPORT_POWER_TRAIN_I": _subscript_dict[
                        "TRANSPORT_POWER_TRAIN_I"
                    ],
                    "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict[
                        "PASSENGERS_TRANSPORT_MODE_I"
                    ],
                },
                ["TRANSPORT_POWER_TRAIN_I", "PASSENGERS_TRANSPORT_MODE_I"],
            ),
            lambda: 1
            + ramp(
                __data["time"],
                (objective_fuel_consumption_efficiency_change_sp() - 1)
                / (
                    year_final_fuel_consumption_efficiency_change_sp()
                    - year_initial_fuel_consumption_efficiency_change_sp()
                ),
                year_initial_fuel_consumption_efficiency_change_sp(),
                year_final_fuel_consumption_efficiency_change_sp(),
            ),
        ),
    ).expand_dims({"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]}, 0)


@component.add(
    name="passenger_transport_modal_share",
    units="DMNL",
    subscripts=[
        "REGIONS_35_I",
        "TRANSPORT_POWER_TRAIN_I",
        "PASSENGERS_TRANSPORT_MODE_I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_model_explorer": 1,
        "model_explorer_passenger_transport_demand_modal_share": 1,
        "year_final_passenger_transport_share_sp": 2,
        "time": 2,
        "year_initial_passenger_transport_share_sp": 3,
        "initial_passenger_transport_demand_share": 4,
        "switch_passenger_transport_modal_share_sp": 2,
        "objective_passenger_transport_demand_modal_share": 1,
    },
)
def passenger_transport_modal_share():
    """
    Demand transport share by transport mode and power train.
    """
    return if_then_else(
        switch_model_explorer() == 1,
        lambda: model_explorer_passenger_transport_demand_modal_share(),
        lambda: if_then_else(
            switch_passenger_transport_modal_share_sp() == 0,
            lambda: initial_passenger_transport_demand_share(),
            lambda: if_then_else(
                np.logical_and(
                    switch_passenger_transport_modal_share_sp() == 1,
                    time() < year_initial_passenger_transport_share_sp(),
                ),
                lambda: initial_passenger_transport_demand_share(),
                lambda: initial_passenger_transport_demand_share()
                + ramp(
                    __data["time"],
                    (
                        objective_passenger_transport_demand_modal_share()
                        - initial_passenger_transport_demand_share()
                    )
                    / (
                        year_final_passenger_transport_share_sp()
                        - year_initial_passenger_transport_share_sp()
                    ),
                    year_initial_passenger_transport_share_sp(),
                    year_final_passenger_transport_share_sp(),
                ),
            ),
        ),
    )


@component.add(
    name="passenger_transport_real_supply",
    units="persons*km",
    subscripts=[
        "REGIONS_35_I",
        "TRANSPORT_POWER_TRAIN_I",
        "PASSENGERS_TRANSPORT_MODE_I",
        "HOUSEHOLDS_I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "desired_passenger_vehicle_distance": 2,
        "modified_load_factor_passenger_transport": 2,
        "private_passenger_vehicle_fleet": 1,
        "public_passenger_vehicle_fleet": 1,
    },
)
def passenger_transport_real_supply():
    """
    Transport supply by region, power train, transport mode and type of household after all policy and endogenous modifications, in persons*km.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
            "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict[
                "PASSENGERS_TRANSPORT_MODE_I"
            ],
            "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
        },
        [
            "REGIONS_35_I",
            "TRANSPORT_POWER_TRAIN_I",
            "PASSENGERS_TRANSPORT_MODE_I",
            "HOUSEHOLDS_I",
        ],
    )
    value.loc[:, :, _subscript_dict["PRIVATE_TRANSPORT_I"], :] = (
        desired_passenger_vehicle_distance()
        .loc[:, :, _subscript_dict["PRIVATE_TRANSPORT_I"], :]
        .rename({"PASSENGERS_TRANSPORT_MODE_I": "PRIVATE_TRANSPORT_I"})
        * modified_load_factor_passenger_transport()
        .loc[:, :, _subscript_dict["PRIVATE_TRANSPORT_I"], :]
        .rename({"PASSENGERS_TRANSPORT_MODE_I": "PRIVATE_TRANSPORT_I"})
        * private_passenger_vehicle_fleet()
    ).values
    value.loc[:, :, _subscript_dict["PUBLIC_TRANSPORT_I"], :] = (
        desired_passenger_vehicle_distance()
        .loc[:, :, _subscript_dict["PUBLIC_TRANSPORT_I"], :]
        .rename({"PASSENGERS_TRANSPORT_MODE_I": "PUBLIC_TRANSPORT_I"})
        * modified_load_factor_passenger_transport()
        .loc[:, :, _subscript_dict["PUBLIC_TRANSPORT_I"], :]
        .rename({"PASSENGERS_TRANSPORT_MODE_I": "PUBLIC_TRANSPORT_I"})
        * public_passenger_vehicle_fleet()
    ).values
    return value


@component.add(
    name="passenger_transport_real_supply_by_mode",
    units="persons*km",
    subscripts=["REGIONS_35_I", "PASSENGERS_TRANSPORT_MODE_I", "HOUSEHOLDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"passenger_transport_real_supply": 1},
)
def passenger_transport_real_supply_by_mode():
    """
    Transport supply by region, transport mode and type of household after all policy and endogenous modifications, in persons*km.
    """
    return sum(
        passenger_transport_real_supply().rename(
            {"TRANSPORT_POWER_TRAIN_I": "TRANSPORT_POWER_TRAIN_I!"}
        ),
        dim=["TRANSPORT_POWER_TRAIN_I!"],
    )


@component.add(
    name="passengers_by_transport_modes",
    units="person",
    subscripts=[
        "REGIONS_35_I",
        "TRANSPORT_POWER_TRAIN_I",
        "PASSENGERS_TRANSPORT_MODE_I",
        "HOUSEHOLDS_I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "modified_load_factor_passenger_transport": 1,
        "passenger_fleet_demand": 1,
    },
)
def passengers_by_transport_modes():
    return modified_load_factor_passenger_transport() * passenger_fleet_demand()


@component.add(
    name="private_passenger_transport_total_distance_traveled_by_transport_mode",
    units="km/Year",
    subscripts=[
        "REGIONS_35_I",
        "TRANSPORT_POWER_TRAIN_I",
        "PASSENGERS_TRANSPORT_MODE_I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "private_passenger_vehicle_fleet": 1,
        "desired_passenger_vehicle_distance": 2,
        "public_passenger_vehicle_fleet": 1,
    },
)
def private_passenger_transport_total_distance_traveled_by_transport_mode():
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
            "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict[
                "PASSENGERS_TRANSPORT_MODE_I"
            ],
        },
        ["REGIONS_35_I", "TRANSPORT_POWER_TRAIN_I", "PASSENGERS_TRANSPORT_MODE_I"],
    )
    value.loc[:, :, _subscript_dict["PRIVATE_TRANSPORT_I"]] = (
        sum(
            private_passenger_vehicle_fleet().rename({"HOUSEHOLDS_I": "HOUSEHOLDS_I!"}),
            dim=["HOUSEHOLDS_I!"],
        )
        * sum(
            desired_passenger_vehicle_distance()
            .loc[:, :, _subscript_dict["PRIVATE_TRANSPORT_I"], :]
            .rename(
                {
                    "PASSENGERS_TRANSPORT_MODE_I": "PRIVATE_TRANSPORT_I",
                    "HOUSEHOLDS_I": "HOUSEHOLDS_I!",
                }
            ),
            dim=["HOUSEHOLDS_I!"],
        )
    ).values
    value.loc[:, :, _subscript_dict["PUBLIC_TRANSPORT_I"]] = (
        sum(
            public_passenger_vehicle_fleet().rename({"HOUSEHOLDS_I": "HOUSEHOLDS_I!"}),
            dim=["HOUSEHOLDS_I!"],
        )
        * sum(
            desired_passenger_vehicle_distance()
            .loc[:, :, _subscript_dict["PUBLIC_TRANSPORT_I"], :]
            .rename(
                {
                    "PASSENGERS_TRANSPORT_MODE_I": "PUBLIC_TRANSPORT_I",
                    "HOUSEHOLDS_I": "HOUSEHOLDS_I!",
                }
            ),
            dim=["HOUSEHOLDS_I!"],
        )
    ).values
    return value


@component.add(
    name="private_passenger_vehicle_fleet",
    units="vehicle",
    subscripts=[
        "REGIONS_35_I",
        "TRANSPORT_POWER_TRAIN_I",
        "PRIVATE_TRANSPORT_I",
        "HOUSEHOLDS_I",
    ],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_private_passenger_vehicle_fleet": 1},
    other_deps={
        "_integ_private_passenger_vehicle_fleet": {
            "initial": {"initial_passenger_vehicle_fleet": 1},
            "step": {
                "new_passenger_private_vehicles": 1,
                "wear_passenger_private_vehicles": 1,
            },
        }
    },
)
def private_passenger_vehicle_fleet():
    """
    Private fleet stock by region, power train, private transport mode and type of household, in number of vehicles.
    """
    return _integ_private_passenger_vehicle_fleet()


_integ_private_passenger_vehicle_fleet = Integ(
    lambda: new_passenger_private_vehicles() - wear_passenger_private_vehicles(),
    lambda: initial_passenger_vehicle_fleet(),
    "_integ_private_passenger_vehicle_fleet",
)


@component.add(
    name="private_vehicle_ownership",
    units="vehicles/kpeople",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "private_passenger_vehicle_fleet": 1,
        "population_35_regions": 1,
        "unit_conversion_kpeople_people": 1,
    },
)
def private_vehicle_ownership():
    """
    Number of car ownership per 1000 persons.
    """
    return (
        sum(
            private_passenger_vehicle_fleet()
            .loc[:, :, "LDV", :]
            .reset_coords(drop=True)
            .rename(
                {
                    "TRANSPORT_POWER_TRAIN_I": "TRANSPORT_POWER_TRAIN_I!",
                    "HOUSEHOLDS_I": "HOUSEHOLDS_I!",
                }
            ),
            dim=["TRANSPORT_POWER_TRAIN_I!", "HOUSEHOLDS_I!"],
        )
        / population_35_regions()
        / unit_conversion_kpeople_people()
    )


@component.add(
    name="private_vehicle_ownership_9R",
    units="vehicles/kpeople",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "private_passenger_vehicle_fleet": 2,
        "population_9_regions": 2,
        "unit_conversion_kpeople_people": 2,
    },
)
def private_vehicle_ownership_9r():
    """
    private_vehicle_ownership_9R
    """
    value = xr.DataArray(
        np.nan, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
    )
    value.loc[_subscript_dict["REGIONS_8_I"]] = (
        zidz(
            sum(
                private_passenger_vehicle_fleet()
                .loc[_subscript_dict["REGIONS_8_I"], :, "LDV", :]
                .reset_coords(drop=True)
                .rename(
                    {
                        "REGIONS_35_I": "REGIONS_8_I",
                        "TRANSPORT_POWER_TRAIN_I": "TRANSPORT_POWER_TRAIN_I!",
                        "HOUSEHOLDS_I": "HOUSEHOLDS_I!",
                    }
                ),
                dim=["TRANSPORT_POWER_TRAIN_I!", "HOUSEHOLDS_I!"],
            ),
            population_9_regions()
            .loc[_subscript_dict["REGIONS_8_I"]]
            .rename({"REGIONS_9_I": "REGIONS_8_I"}),
        )
        / unit_conversion_kpeople_people()
    ).values
    value.loc[["EU27"]] = (
        zidz(
            sum(
                private_passenger_vehicle_fleet()
                .loc[_subscript_dict["REGIONS_EU27_I"], :, "LDV", :]
                .reset_coords(drop=True)
                .rename(
                    {
                        "REGIONS_35_I": "REGIONS_EU27_I!",
                        "TRANSPORT_POWER_TRAIN_I": "TRANSPORT_POWER_TRAIN_I!",
                        "HOUSEHOLDS_I": "HOUSEHOLDS_I!",
                    }
                ),
                dim=["REGIONS_EU27_I!", "TRANSPORT_POWER_TRAIN_I!", "HOUSEHOLDS_I!"],
            ),
            float(population_9_regions().loc["EU27"]),
        )
        / unit_conversion_kpeople_people()
    )
    return value


@component.add(
    name="public_passenger_vehicle_fleet",
    units="vehicle",
    subscripts=[
        "REGIONS_35_I",
        "TRANSPORT_POWER_TRAIN_I",
        "PUBLIC_TRANSPORT_I",
        "HOUSEHOLDS_I",
    ],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_public_passenger_vehicle_fleet": 1},
    other_deps={
        "_integ_public_passenger_vehicle_fleet": {
            "initial": {"initial_public_passenger_vehicle_fleet": 1},
            "step": {
                "new_passenger_public_vehicles": 1,
                "wear_passenger_public_vehicles": 1,
            },
        }
    },
)
def public_passenger_vehicle_fleet():
    """
    Public fleet stock by region, power train, public transport mode and type of household, in number of vehicles.
    """
    return _integ_public_passenger_vehicle_fleet()


_integ_public_passenger_vehicle_fleet = Integ(
    lambda: new_passenger_public_vehicles() - wear_passenger_public_vehicles(),
    lambda: initial_public_passenger_vehicle_fleet(),
    "_integ_public_passenger_vehicle_fleet",
)


@component.add(
    name="reduction_passenger_transport_demand",
    units="DMNL",
    subscripts=["TRANSPORT_POWER_TRAIN_I", "PASSENGERS_TRANSPORT_MODE_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_model_explorer": 1,
        "model_explorer_reduction_passenger_transport_demand": 1,
        "switch_reduction_passenger_transport_demand_sp": 2,
        "objective_reduction_passenger_transport_demand_sp": 1,
        "year_final_reduction_passenger_transport_demand_sp": 2,
        "time": 2,
        "year_initial_reduction_passenger_transport_demand_sp": 3,
    },
)
def reduction_passenger_transport_demand():
    """
    1+(RAMP((OBJECTIVE_REDUCTION_PASSENGER_TRANSPORT_DEMAND_SP[POWER TRAIN I,PASSENGERS TRANSPORT MODE I]-1)/ (YEAR_FINAL_REDUCTION_PASSENGER_TRANSPORT_DEMAND_SP-YEAR_INITIAL_REDUCTION_PASSENGER_ TRANSPORT_DEMAND_SP),YEAR_INITIAL_REDUCTION_PASSENGER_TRANSPORT_DEMAND_SP ,YEAR_FINAL_REDUCTION_PASSENGER_TRANSPORT_DEMAND_SP))
    """
    return if_then_else(
        switch_model_explorer() == 1,
        lambda: model_explorer_reduction_passenger_transport_demand(),
        lambda: if_then_else(
            switch_reduction_passenger_transport_demand_sp() == 0,
            lambda: xr.DataArray(
                1,
                {
                    "TRANSPORT_POWER_TRAIN_I": _subscript_dict[
                        "TRANSPORT_POWER_TRAIN_I"
                    ],
                    "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict[
                        "PASSENGERS_TRANSPORT_MODE_I"
                    ],
                },
                ["TRANSPORT_POWER_TRAIN_I", "PASSENGERS_TRANSPORT_MODE_I"],
            ),
            lambda: if_then_else(
                np.logical_and(
                    switch_reduction_passenger_transport_demand_sp() == 1,
                    time() < year_initial_reduction_passenger_transport_demand_sp(),
                ),
                lambda: xr.DataArray(
                    1,
                    {
                        "TRANSPORT_POWER_TRAIN_I": _subscript_dict[
                            "TRANSPORT_POWER_TRAIN_I"
                        ],
                        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict[
                            "PASSENGERS_TRANSPORT_MODE_I"
                        ],
                    },
                    ["TRANSPORT_POWER_TRAIN_I", "PASSENGERS_TRANSPORT_MODE_I"],
                ),
                lambda: 1
                + ramp(
                    __data["time"],
                    (objective_reduction_passenger_transport_demand_sp() - 1)
                    / (
                        year_final_reduction_passenger_transport_demand_sp()
                        - year_initial_reduction_passenger_transport_demand_sp()
                    ),
                    year_initial_reduction_passenger_transport_demand_sp(),
                    year_final_reduction_passenger_transport_demand_sp(),
                ),
            ),
        ),
    )


@component.add(
    name="share_BEV_BUS",
    units="DMNL",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "constant_bev_bus": 1,
        "delayed_ts_price_output": 2,
        "sigma_fuel_bus": 1,
        "base_price_output": 2,
        "sigma_elect_bus": 1,
        "time": 1,
        "trend_bev_bus": 1,
    },
)
def share_bev_bus():
    """
    Share of battery electric buses
    """
    return np.exp(
        constant_bev_bus()
        + sigma_fuel_bus()
        * np.log(
            zidz(
                delayed_ts_price_output().loc[:, "REFINING"].reset_coords(drop=True),
                base_price_output().loc[:, "REFINING"].reset_coords(drop=True),
            )
        )
        + sigma_elect_bus()
        * np.log(
            zidz(
                delayed_ts_price_output()
                .loc[:, "DISTRIBUTION_ELECTRICITY"]
                .reset_coords(drop=True),
                base_price_output()
                .loc[:, "DISTRIBUTION_ELECTRICITY"]
                .reset_coords(drop=True),
            )
        )
        + trend_bev_bus() * (time() - 2015)
    )


@component.add(
    name="share_BEV_LDV",
    units="DMNL",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "constant_bev_ldv": 1,
        "sigma_fuel_ldv": 1,
        "delayed_ts_price_output": 2,
        "base_price_output": 2,
        "sigma_elect_ldv": 1,
        "trend_bev_ldv": 1,
        "time": 1,
    },
)
def share_bev_ldv():
    """
    Share of battery electric light duty vehicles
    """
    return np.exp(
        constant_bev_ldv()
        + sigma_fuel_ldv()
        * np.log(
            zidz(
                delayed_ts_price_output().loc[:, "REFINING"].reset_coords(drop=True),
                base_price_output().loc[:, "REFINING"].reset_coords(drop=True),
            )
        )
        + sigma_elect_ldv()
        * np.log(
            zidz(
                delayed_ts_price_output()
                .loc[:, "DISTRIBUTION_ELECTRICITY"]
                .reset_coords(drop=True),
                base_price_output()
                .loc[:, "DISTRIBUTION_ELECTRICITY"]
                .reset_coords(drop=True),
            )
        )
        + trend_bev_ldv() * (time() - 2015)
    )


@component.add(
    name="share_passenger_transport_demand_by_region_and_type_of_household",
    units="1",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "total_passenger_transport_demand_by_region_and_type_of_household": 1,
        "total_passenger_transport_demand_by_region": 1,
    },
)
def share_passenger_transport_demand_by_region_and_type_of_household():
    return zidz(
        total_passenger_transport_demand_by_region_and_type_of_household(),
        total_passenger_transport_demand_by_region().expand_dims(
            {"HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"]}, 1
        ),
    )


@component.add(
    name="share_technologies_passanger_transport",
    subscripts=[
        "REGIONS_35_I",
        "TRANSPORT_POWER_TRAIN_I",
        "PASSENGERS_TRANSPORT_MODE_I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "share_technologies_passanger_transport_exc_fuel_adjusted": 5,
        "split_gasoline_diesel_passanger_transport": 4,
    },
)
def share_technologies_passanger_transport():
    """
    Shares technologies in passanger transport by mode
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
            "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict[
                "PASSENGERS_TRANSPORT_MODE_I"
            ],
        },
        ["REGIONS_35_I", "TRANSPORT_POWER_TRAIN_I", "PASSENGERS_TRANSPORT_MODE_I"],
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, ["ICE_gasoline"], ["LDV"]] = False
    except_subs.loc[:, ["ICE_diesel"], ["LDV"]] = False
    except_subs.loc[:, ["ICE_gasoline"], ["bus"]] = False
    except_subs.loc[:, ["ICE_diesel"], ["bus"]] = False
    value.values[
        except_subs.values
    ] = share_technologies_passanger_transport_exc_fuel_adjusted().values[
        except_subs.values
    ]
    value.loc[:, ["ICE_gasoline"], ["LDV"]] = (
        (
            split_gasoline_diesel_passanger_transport()
            .loc[:, "ICE_gasoline", "LDV"]
            .reset_coords(drop=True)
            * (
                1
                - sum(
                    share_technologies_passanger_transport_exc_fuel_adjusted()
                    .loc[:, :, "LDV"]
                    .reset_coords(drop=True)
                    .rename({"TRANSPORT_POWER_TRAIN_I": "TRANSPORT_POWER_TRAIN_I!"}),
                    dim=["TRANSPORT_POWER_TRAIN_I!"],
                )
            )
        )
        .expand_dims({"TRANSPORT_POWER_TRAIN_I": ["ICE_gasoline"]}, 1)
        .expand_dims({"BATTERY_VEHICLES_I": ["LDV"]}, 2)
        .values
    )
    value.loc[:, ["ICE_diesel"], ["LDV"]] = (
        (
            split_gasoline_diesel_passanger_transport()
            .loc[:, "ICE_diesel", "LDV"]
            .reset_coords(drop=True)
            * (
                1
                - sum(
                    share_technologies_passanger_transport_exc_fuel_adjusted()
                    .loc[:, :, "LDV"]
                    .reset_coords(drop=True)
                    .rename({"TRANSPORT_POWER_TRAIN_I": "TRANSPORT_POWER_TRAIN_I!"}),
                    dim=["TRANSPORT_POWER_TRAIN_I!"],
                )
            )
        )
        .expand_dims({"TRANSPORT_POWER_TRAIN_I": ["ICE_diesel"]}, 1)
        .expand_dims({"BATTERY_VEHICLES_I": ["LDV"]}, 2)
        .values
    )
    value.loc[:, ["ICE_gasoline"], ["bus"]] = (
        (
            split_gasoline_diesel_passanger_transport()
            .loc[:, "ICE_gasoline", "bus"]
            .reset_coords(drop=True)
            * (
                1
                - sum(
                    share_technologies_passanger_transport_exc_fuel_adjusted()
                    .loc[:, :, "bus"]
                    .reset_coords(drop=True)
                    .rename({"TRANSPORT_POWER_TRAIN_I": "TRANSPORT_POWER_TRAIN_I!"}),
                    dim=["TRANSPORT_POWER_TRAIN_I!"],
                )
            )
        )
        .expand_dims({"TRANSPORT_POWER_TRAIN_I": ["ICE_gasoline"]}, 1)
        .expand_dims({"BATTERY_VEHICLES_I": ["bus"]}, 2)
        .values
    )
    value.loc[:, ["ICE_diesel"], ["bus"]] = (
        (
            split_gasoline_diesel_passanger_transport()
            .loc[:, "ICE_diesel", "bus"]
            .reset_coords(drop=True)
            * (
                1
                - sum(
                    share_technologies_passanger_transport_exc_fuel_adjusted()
                    .loc[:, :, "bus"]
                    .reset_coords(drop=True)
                    .rename({"TRANSPORT_POWER_TRAIN_I": "TRANSPORT_POWER_TRAIN_I!"}),
                    dim=["TRANSPORT_POWER_TRAIN_I!"],
                )
            )
        )
        .expand_dims({"TRANSPORT_POWER_TRAIN_I": ["ICE_diesel"]}, 1)
        .expand_dims({"BATTERY_VEHICLES_I": ["bus"]}, 2)
        .values
    )
    return value


@component.add(
    name="share_technologies_passanger_transport_exc_fuel",
    subscripts=[
        "REGIONS_35_I",
        "TRANSPORT_POWER_TRAIN_I",
        "PASSENGERS_TRANSPORT_MODE_I",
    ],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "base_share_technologies_passanger_transport": 1,
        "share_bev_bus": 1,
        "share_bev_ldv": 1,
    },
)
def share_technologies_passanger_transport_exc_fuel():
    """
    Shares technologies in passanger transport by mode, exclunding gasoline and diesel
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
            "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict[
                "PASSENGERS_TRANSPORT_MODE_I"
            ],
        },
        ["REGIONS_35_I", "TRANSPORT_POWER_TRAIN_I", "PASSENGERS_TRANSPORT_MODE_I"],
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, ["BEV"], ["bus"]] = False
    except_subs.loc[:, ["BEV"], ["LDV"]] = False
    except_subs.loc[:, ["ICE_gasoline"], ["LDV"]] = False
    except_subs.loc[:, ["ICE_diesel"], ["LDV"]] = False
    except_subs.loc[:, ["ICE_gasoline"], ["bus"]] = False
    except_subs.loc[:, ["ICE_diesel"], ["bus"]] = False
    value.values[
        except_subs.values
    ] = base_share_technologies_passanger_transport().values[except_subs.values]
    value.loc[:, ["BEV"], ["bus"]] = (
        share_bev_bus()
        .expand_dims({"TRANSPORT_POWER_TRAIN_I": ["BEV"]}, 1)
        .expand_dims({"BATTERY_VEHICLES_I": ["bus"]}, 2)
        .values
    )
    value.loc[:, ["BEV"], ["LDV"]] = (
        share_bev_ldv()
        .expand_dims({"TRANSPORT_POWER_TRAIN_I": ["BEV"]}, 1)
        .expand_dims({"BATTERY_VEHICLES_I": ["LDV"]}, 2)
        .values
    )
    value.loc[:, ["ICE_gasoline"], ["LDV"]] = 0
    value.loc[:, ["ICE_diesel"], ["LDV"]] = 0
    value.loc[:, ["ICE_gasoline"], ["bus"]] = 0
    value.loc[:, ["ICE_diesel"], ["bus"]] = 0
    return value


@component.add(
    name="share_technologies_passanger_transport_exc_fuel_adjusted",
    subscripts=[
        "REGIONS_35_I",
        "TRANSPORT_POWER_TRAIN_I",
        "PASSENGERS_TRANSPORT_MODE_I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"share_technologies_passanger_transport_exc_fuel": 4},
)
def share_technologies_passanger_transport_exc_fuel_adjusted():
    """
    Shares technologies adjsuted when > 1
    """
    return if_then_else(
        (
            sum(
                share_technologies_passanger_transport_exc_fuel().rename(
                    {"TRANSPORT_POWER_TRAIN_I": "TRANSPORT_POWER_TRAIN_I!"}
                ),
                dim=["TRANSPORT_POWER_TRAIN_I!"],
            )
            > 1
        ).expand_dims(
            {"TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"]}, 2
        ),
        lambda: zidz(
            share_technologies_passanger_transport_exc_fuel(),
            sum(
                share_technologies_passanger_transport_exc_fuel().rename(
                    {"TRANSPORT_POWER_TRAIN_I": "TRANSPORT_POWER_TRAIN_I!"}
                ),
                dim=["TRANSPORT_POWER_TRAIN_I!"],
            ).expand_dims(
                {"TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"]},
                1,
            ),
        ).transpose(
            "REGIONS_35_I", "PASSENGERS_TRANSPORT_MODE_I", "TRANSPORT_POWER_TRAIN_I"
        ),
        lambda: share_technologies_passanger_transport_exc_fuel().transpose(
            "REGIONS_35_I", "PASSENGERS_TRANSPORT_MODE_I", "TRANSPORT_POWER_TRAIN_I"
        ),
    ).transpose(
        "REGIONS_35_I", "TRANSPORT_POWER_TRAIN_I", "PASSENGERS_TRANSPORT_MODE_I"
    )


@component.add(name="SIGMA_ELECT_BUS", comp_type="Constant", comp_subtype="Normal")
def sigma_elect_bus():
    """
    Signa electricity LDV
    """
    return -0.145


@component.add(name="SIGMA_ELECT_LDV", comp_type="Constant", comp_subtype="Normal")
def sigma_elect_ldv():
    """
    Signa electricity LDV
    """
    return -0.145


@component.add(name="SIGMA_FUEL_BUS", comp_type="Constant", comp_subtype="Normal")
def sigma_fuel_bus():
    """
    Sigma fuel LDV
    """
    return 0.499


@component.add(name="SIGMA_FUEL_LDV", comp_type="Constant", comp_subtype="Normal")
def sigma_fuel_ldv():
    """
    Sigma fuel LDV
    """
    return 0.499


@component.add(name="SIGMA_PUBLIC", comp_type="Constant", comp_subtype="Normal")
def sigma_public():
    return 0.5


@component.add(
    name="smooth_lifetime_passengers_vehicles",
    units="Year",
    subscripts=[
        "REGIONS_35_I",
        "TRANSPORT_POWER_TRAIN_I",
        "PASSENGERS_TRANSPORT_MODE_I",
        "HOUSEHOLDS_I",
    ],
    comp_type="Stateful",
    comp_subtype="Smooth",
    depends_on={"_smooth_smooth_lifetime_passengers_vehicles": 1},
    other_deps={
        "_smooth_smooth_lifetime_passengers_vehicles": {
            "initial": {"lifetime_passenger_vehicles": 1},
            "step": {"lifetime_passenger_vehicles": 1},
        }
    },
)
def smooth_lifetime_passengers_vehicles():
    return _smooth_smooth_lifetime_passengers_vehicles()


_smooth_smooth_lifetime_passengers_vehicles = Smooth(
    lambda: lifetime_passenger_vehicles(),
    lambda: xr.DataArray(
        1,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
            "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict[
                "PASSENGERS_TRANSPORT_MODE_I"
            ],
            "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
        },
        [
            "REGIONS_35_I",
            "TRANSPORT_POWER_TRAIN_I",
            "PASSENGERS_TRANSPORT_MODE_I",
            "HOUSEHOLDS_I",
        ],
    ),
    lambda: lifetime_passenger_vehicles(),
    lambda: 1,
    "_smooth_smooth_lifetime_passengers_vehicles",
)


@component.add(
    name="smooth_wear_passenger_private_vehicles_mod_factor",
    units="DMNL",
    subscripts=[
        "REGIONS_35_I",
        "TRANSPORT_POWER_TRAIN_I",
        "PRIVATE_TRANSPORT_I",
        "HOUSEHOLDS_I",
    ],
    comp_type="Stateful",
    comp_subtype="Smooth",
    depends_on={"_smooth_smooth_wear_passenger_private_vehicles_mod_factor": 1},
    other_deps={
        "_smooth_smooth_wear_passenger_private_vehicles_mod_factor": {
            "initial": {"wear_passenger_private_vehicles_mod_factor": 1},
            "step": {"wear_passenger_private_vehicles_mod_factor": 1},
        }
    },
)
def smooth_wear_passenger_private_vehicles_mod_factor():
    return _smooth_smooth_wear_passenger_private_vehicles_mod_factor()


_smooth_smooth_wear_passenger_private_vehicles_mod_factor = Smooth(
    lambda: wear_passenger_private_vehicles_mod_factor(),
    lambda: xr.DataArray(
        2,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
            "PRIVATE_TRANSPORT_I": _subscript_dict["PRIVATE_TRANSPORT_I"],
            "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
        },
        [
            "REGIONS_35_I",
            "TRANSPORT_POWER_TRAIN_I",
            "PRIVATE_TRANSPORT_I",
            "HOUSEHOLDS_I",
        ],
    ),
    lambda: wear_passenger_private_vehicles_mod_factor(),
    lambda: 1,
    "_smooth_smooth_wear_passenger_private_vehicles_mod_factor",
)


@component.add(
    name="smooth_wear_passenger_public_vehicles_mod_factor",
    subscripts=[
        "REGIONS_35_I",
        "TRANSPORT_POWER_TRAIN_I",
        "PUBLIC_TRANSPORT_I",
        "HOUSEHOLDS_I",
    ],
    comp_type="Stateful",
    comp_subtype="Smooth",
    depends_on={"_smooth_smooth_wear_passenger_public_vehicles_mod_factor": 1},
    other_deps={
        "_smooth_smooth_wear_passenger_public_vehicles_mod_factor": {
            "initial": {"wear_passenger_public_vehicles_mod_factor": 1},
            "step": {"wear_passenger_public_vehicles_mod_factor": 1},
        }
    },
)
def smooth_wear_passenger_public_vehicles_mod_factor():
    return _smooth_smooth_wear_passenger_public_vehicles_mod_factor()


_smooth_smooth_wear_passenger_public_vehicles_mod_factor = Smooth(
    lambda: wear_passenger_public_vehicles_mod_factor(),
    lambda: xr.DataArray(
        2,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
            "PUBLIC_TRANSPORT_I": _subscript_dict["PUBLIC_TRANSPORT_I"],
            "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
        },
        [
            "REGIONS_35_I",
            "TRANSPORT_POWER_TRAIN_I",
            "PUBLIC_TRANSPORT_I",
            "HOUSEHOLDS_I",
        ],
    ),
    lambda: wear_passenger_public_vehicles_mod_factor(),
    lambda: 1,
    "_smooth_smooth_wear_passenger_public_vehicles_mod_factor",
)


@component.add(
    name="split_gasoline_diesel_passanger_transport",
    subscripts=[
        "REGIONS_35_I",
        "TRANSPORT_POWER_TRAIN_I",
        "PASSENGERS_TRANSPORT_MODE_I",
    ],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={"base_share_technologies_passanger_transport": 6},
)
def split_gasoline_diesel_passanger_transport():
    """
    Split gasoline and diesel
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
            "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict[
                "PASSENGERS_TRANSPORT_MODE_I"
            ],
        },
        ["REGIONS_35_I", "TRANSPORT_POWER_TRAIN_I", "PASSENGERS_TRANSPORT_MODE_I"],
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, ["ICE_gasoline"], :] = False
    except_subs.loc[:, ["ICE_diesel"], :] = False
    value.values[except_subs.values] = 0
    value.loc[:, ["ICE_gasoline"], :] = (
        zidz(
            base_share_technologies_passanger_transport()
            .loc[:, "ICE_gasoline", :]
            .reset_coords(drop=True),
            base_share_technologies_passanger_transport()
            .loc[:, "ICE_gasoline", :]
            .reset_coords(drop=True)
            + base_share_technologies_passanger_transport()
            .loc[:, "ICE_diesel", :]
            .reset_coords(drop=True),
        )
        .expand_dims({"TRANSPORT_POWER_TRAIN_I": ["ICE_gasoline"]}, 1)
        .values
    )
    value.loc[:, ["ICE_diesel"], :] = (
        zidz(
            base_share_technologies_passanger_transport()
            .loc[:, "ICE_diesel", :]
            .reset_coords(drop=True),
            base_share_technologies_passanger_transport()
            .loc[:, "ICE_gasoline", :]
            .reset_coords(drop=True)
            + base_share_technologies_passanger_transport()
            .loc[:, "ICE_diesel", :]
            .reset_coords(drop=True),
        )
        .expand_dims({"TRANSPORT_POWER_TRAIN_I": ["ICE_diesel"]}, 1)
        .values
    )
    return value


@component.add(
    name="SUB_SHARE_BUS",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"objective_passenger_transport_demand_modal_share_sp": 3},
)
def sub_share_bus():
    return zidz(
        sum(
            objective_passenger_transport_demand_modal_share_sp()
            .loc[:, :, "bus"]
            .reset_coords(drop=True)
            .rename({"TRANSPORT_POWER_TRAIN_I": "TRANSPORT_POWER_TRAIN_I!"}),
            dim=["TRANSPORT_POWER_TRAIN_I!"],
        ),
        sum(
            objective_passenger_transport_demand_modal_share_sp()
            .loc[:, :, "RAIL"]
            .reset_coords(drop=True)
            .rename({"TRANSPORT_POWER_TRAIN_I": "TRANSPORT_POWER_TRAIN_I!"}),
            dim=["TRANSPORT_POWER_TRAIN_I!"],
        )
        + sum(
            objective_passenger_transport_demand_modal_share_sp()
            .loc[:, :, "bus"]
            .reset_coords(drop=True)
            .rename({"TRANSPORT_POWER_TRAIN_I": "TRANSPORT_POWER_TRAIN_I!"}),
            dim=["TRANSPORT_POWER_TRAIN_I!"],
        ),
    )


@component.add(
    name="SUB_SHARE_RAIL",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"objective_passenger_transport_demand_modal_share_sp": 3},
)
def sub_share_rail():
    """
    Share of rail over total bublic transportation
    """
    return zidz(
        sum(
            objective_passenger_transport_demand_modal_share_sp()
            .loc[:, :, "RAIL"]
            .reset_coords(drop=True)
            .rename({"TRANSPORT_POWER_TRAIN_I": "TRANSPORT_POWER_TRAIN_I!"}),
            dim=["TRANSPORT_POWER_TRAIN_I!"],
        ),
        sum(
            objective_passenger_transport_demand_modal_share_sp()
            .loc[:, :, "RAIL"]
            .reset_coords(drop=True)
            .rename({"TRANSPORT_POWER_TRAIN_I": "TRANSPORT_POWER_TRAIN_I!"}),
            dim=["TRANSPORT_POWER_TRAIN_I!"],
        )
        + sum(
            objective_passenger_transport_demand_modal_share_sp()
            .loc[:, :, "bus"]
            .reset_coords(drop=True)
            .rename({"TRANSPORT_POWER_TRAIN_I": "TRANSPORT_POWER_TRAIN_I!"}),
            dim=["TRANSPORT_POWER_TRAIN_I!"],
        ),
    )


@component.add(
    name="SWITCH_HH_TRANSPORT_DISAGGREGATED",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_hh_transport_disaggregated"},
)
def switch_hh_transport_disaggregated():
    """
    This switch can take two values: 0: the passenger transport module runs with 1 type of HH aggregated in REPRESENTATIVE HH subscript. 1: the passenger transport module runs disaggregated in 61 type of HH.
    """
    return _ext_constant_switch_hh_transport_disaggregated()


_ext_constant_switch_hh_transport_disaggregated = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_HH_TRANSPORT_DISAGGREGATED",
    {},
    _root,
    {},
    "_ext_constant_switch_hh_transport_disaggregated",
)


@component.add(
    name="SWITCH_STATIC_TRANSPORT_DEMAND",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_static_transport_demand"},
)
def switch_static_transport_demand():
    """
    =0 the model runs with passenger transport demand dinamically modified by the GDPpc and 1 type of HH =1 the model runs with static input passenger transport demand and 1 type of HH
    """
    return _ext_constant_switch_static_transport_demand()


_ext_constant_switch_static_transport_demand = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_STATIC_TRANSPORT_DEMAND",
    {},
    _root,
    {},
    "_ext_constant_switch_static_transport_demand",
)


@component.add(
    name="total_energy_consumption_passenger_transport",
    units="EJ",
    subscripts=["NRG_FE_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "energy_passenger_transport_consumption_by_fe_35r": 1,
        "unit_conversion_mj_ej": 1,
    },
)
def total_energy_consumption_passenger_transport():
    """
    Total energy passengers transport consumption by type of final energy in EJ.
    """
    return (
        sum(
            energy_passenger_transport_consumption_by_fe_35r().rename(
                {
                    "REGIONS_35_I": "REGIONS_35_I!",
                    "PASSENGERS_TRANSPORT_MODE_I": "PASSENGERS_TRANSPORT_MODE_I!",
                    "HOUSEHOLDS_I": "HOUSEHOLDS_I!",
                }
            ),
            dim=["REGIONS_35_I!", "PASSENGERS_TRANSPORT_MODE_I!", "HOUSEHOLDS_I!"],
        )
        / unit_conversion_mj_ej()
    )


@component.add(
    name="total_new_number_EV_vehicles",
    units="vehicles",
    subscripts=["REGIONS_35_I", "TRANSPORT_POWER_TRAIN_I", "BATTERY_VEHICLES_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "new_passenger_public_vehicles": 1,
        "new_passenger_private_vehicles": 2,
    },
)
def total_new_number_ev_vehicles():
    """
    New number of EV vehicles
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
            "BATTERY_VEHICLES_I": _subscript_dict["BATTERY_VEHICLES_I"],
        },
        ["REGIONS_35_I", "TRANSPORT_POWER_TRAIN_I", "BATTERY_VEHICLES_I"],
    )
    value.loc[:, ["BEV"], ["MDV"]] = 0
    value.loc[:, ["BEV"], ["bus"]] = (
        sum(
            new_passenger_public_vehicles()
            .loc[:, "BEV", "bus", :]
            .reset_coords(drop=True)
            .rename({"HOUSEHOLDS_I": "HOUSEHOLDS_I!"}),
            dim=["HOUSEHOLDS_I!"],
        )
        .expand_dims({"TRANSPORT_POWER_TRAIN_I": ["BEV"]}, 1)
        .expand_dims({"BATTERY_VEHICLES_I": ["bus"]}, 2)
        .values
    )
    value.loc[:, ["BEV"], ["LDV"]] = (
        sum(
            new_passenger_private_vehicles()
            .loc[:, "BEV", "LDV", :]
            .reset_coords(drop=True)
            .rename({"HOUSEHOLDS_I": "HOUSEHOLDS_I!"}),
            dim=["HOUSEHOLDS_I!"],
        )
        .expand_dims({"TRANSPORT_POWER_TRAIN_I": ["BEV"]}, 1)
        .expand_dims({"BATTERY_VEHICLES_I": ["LDV"]}, 2)
        .values
    )
    value.loc[:, ["BEV"], ["MOTORCYCLES_2W_3W"]] = (
        sum(
            new_passenger_private_vehicles()
            .loc[:, "BEV", "MOTORCYCLES_2W_3W", :]
            .reset_coords(drop=True)
            .rename({"HOUSEHOLDS_I": "HOUSEHOLDS_I!"}),
            dim=["HOUSEHOLDS_I!"],
        )
        .expand_dims({"TRANSPORT_POWER_TRAIN_I": ["BEV"]}, 1)
        .expand_dims({"BATTERY_VEHICLES_I": ["MOTORCYCLES_2W_3W"]}, 2)
        .values
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, ["BEV"], ["MDV"]] = False
    except_subs.loc[:, ["BEV"], ["bus"]] = False
    except_subs.loc[:, ["BEV"], ["LDV"]] = False
    except_subs.loc[:, ["BEV"], ["MOTORCYCLES_2W_3W"]] = False
    value.values[except_subs.values] = 0
    return value


@component.add(
    name="total_number_electrified_vehicles",
    units="vehicles",
    subscripts=["REGIONS_35_I", "TRANSPORT_POWER_TRAIN_I", "TRANSPORT_MODE_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "private_passenger_vehicle_fleet": 6,
        "public_passenger_vehicle_fleet": 3,
    },
)
def total_number_electrified_vehicles():
    """
    number_of_electrified_vehicles
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
            "TRANSPORT_MODE_I": _subscript_dict["TRANSPORT_MODE_I"],
        },
        ["REGIONS_35_I", "TRANSPORT_POWER_TRAIN_I", "TRANSPORT_MODE_I"],
    )
    value.loc[:, ["HEV"], ["LDV"]] = (
        sum(
            private_passenger_vehicle_fleet()
            .loc[:, "HEV", "LDV", :]
            .reset_coords(drop=True)
            .rename({"HOUSEHOLDS_I": "HOUSEHOLDS_I!"}),
            dim=["HOUSEHOLDS_I!"],
        )
        .expand_dims({"TRANSPORT_POWER_TRAIN_I": ["HEV"]}, 1)
        .expand_dims({"BATTERY_VEHICLES_I": ["LDV"]}, 2)
        .values
    )
    value.loc[:, ["HEV"], ["MOTORCYCLES_2W_3W"]] = (
        sum(
            private_passenger_vehicle_fleet()
            .loc[:, "HEV", "MOTORCYCLES_2W_3W", :]
            .reset_coords(drop=True)
            .rename({"HOUSEHOLDS_I": "HOUSEHOLDS_I!"}),
            dim=["HOUSEHOLDS_I!"],
        )
        .expand_dims({"TRANSPORT_POWER_TRAIN_I": ["HEV"]}, 1)
        .expand_dims({"BATTERY_VEHICLES_I": ["MOTORCYCLES_2W_3W"]}, 2)
        .values
    )
    value.loc[:, ["PHEV"], ["LDV"]] = (
        sum(
            private_passenger_vehicle_fleet()
            .loc[:, "PHEV", "LDV", :]
            .reset_coords(drop=True)
            .rename({"HOUSEHOLDS_I": "HOUSEHOLDS_I!"}),
            dim=["HOUSEHOLDS_I!"],
        )
        .expand_dims({"TRANSPORT_POWER_TRAIN_I": ["PHEV"]}, 1)
        .expand_dims({"BATTERY_VEHICLES_I": ["LDV"]}, 2)
        .values
    )
    value.loc[:, ["PHEV"], ["MOTORCYCLES_2W_3W"]] = (
        sum(
            private_passenger_vehicle_fleet()
            .loc[:, "HEV", "MOTORCYCLES_2W_3W", :]
            .reset_coords(drop=True)
            .rename({"HOUSEHOLDS_I": "HOUSEHOLDS_I!"}),
            dim=["HOUSEHOLDS_I!"],
        )
        .expand_dims({"TRANSPORT_POWER_TRAIN_I": ["PHEV"]}, 1)
        .expand_dims({"BATTERY_VEHICLES_I": ["MOTORCYCLES_2W_3W"]}, 2)
        .values
    )
    value.loc[:, ["BEV"], ["LDV"]] = (
        sum(
            private_passenger_vehicle_fleet()
            .loc[:, "BEV", "LDV", :]
            .reset_coords(drop=True)
            .rename({"HOUSEHOLDS_I": "HOUSEHOLDS_I!"}),
            dim=["HOUSEHOLDS_I!"],
        )
        .expand_dims({"TRANSPORT_POWER_TRAIN_I": ["BEV"]}, 1)
        .expand_dims({"BATTERY_VEHICLES_I": ["LDV"]}, 2)
        .values
    )
    value.loc[:, ["BEV"], ["MOTORCYCLES_2W_3W"]] = (
        sum(
            private_passenger_vehicle_fleet()
            .loc[:, "BEV", "MOTORCYCLES_2W_3W", :]
            .reset_coords(drop=True)
            .rename({"HOUSEHOLDS_I": "HOUSEHOLDS_I!"}),
            dim=["HOUSEHOLDS_I!"],
        )
        .expand_dims({"TRANSPORT_POWER_TRAIN_I": ["BEV"]}, 1)
        .expand_dims({"BATTERY_VEHICLES_I": ["MOTORCYCLES_2W_3W"]}, 2)
        .values
    )
    value.loc[:, ["HEV"], ["bus"]] = (
        sum(
            public_passenger_vehicle_fleet()
            .loc[:, "HEV", "bus", :]
            .reset_coords(drop=True)
            .rename({"HOUSEHOLDS_I": "HOUSEHOLDS_I!"}),
            dim=["HOUSEHOLDS_I!"],
        )
        .expand_dims({"TRANSPORT_POWER_TRAIN_I": ["HEV"]}, 1)
        .expand_dims({"BATTERY_VEHICLES_I": ["bus"]}, 2)
        .values
    )
    value.loc[:, ["PHEV"], ["bus"]] = (
        sum(
            public_passenger_vehicle_fleet()
            .loc[:, "PHEV", "bus", :]
            .reset_coords(drop=True)
            .rename({"HOUSEHOLDS_I": "HOUSEHOLDS_I!"}),
            dim=["HOUSEHOLDS_I!"],
        )
        .expand_dims({"TRANSPORT_POWER_TRAIN_I": ["PHEV"]}, 1)
        .expand_dims({"BATTERY_VEHICLES_I": ["bus"]}, 2)
        .values
    )
    value.loc[:, ["BEV"], ["bus"]] = (
        sum(
            public_passenger_vehicle_fleet()
            .loc[:, "BEV", "bus", :]
            .reset_coords(drop=True)
            .rename({"HOUSEHOLDS_I": "HOUSEHOLDS_I!"}),
            dim=["HOUSEHOLDS_I!"],
        )
        .expand_dims({"TRANSPORT_POWER_TRAIN_I": ["BEV"]}, 1)
        .expand_dims({"BATTERY_VEHICLES_I": ["bus"]}, 2)
        .values
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, ["HEV"], ["LDV"]] = False
    except_subs.loc[:, ["HEV"], ["MOTORCYCLES_2W_3W"]] = False
    except_subs.loc[:, ["PHEV"], ["LDV"]] = False
    except_subs.loc[:, ["PHEV"], ["MOTORCYCLES_2W_3W"]] = False
    except_subs.loc[:, ["BEV"], ["LDV"]] = False
    except_subs.loc[:, ["BEV"], ["MOTORCYCLES_2W_3W"]] = False
    except_subs.loc[:, ["HEV"], ["bus"]] = False
    except_subs.loc[:, ["PHEV"], ["bus"]] = False
    except_subs.loc[:, ["BEV"], ["bus"]] = False
    value.values[except_subs.values] = 0
    return value


@component.add(
    name="total_number_EV_vehicles",
    units="vehicles",
    subscripts=["REGIONS_35_I", "TRANSPORT_POWER_TRAIN_I", "BATTERY_VEHICLES_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "public_passenger_vehicle_fleet": 1,
        "private_passenger_vehicle_fleet": 2,
    },
)
def total_number_ev_vehicles():
    """
    number of EV vehicles
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
            "BATTERY_VEHICLES_I": _subscript_dict["BATTERY_VEHICLES_I"],
        },
        ["REGIONS_35_I", "TRANSPORT_POWER_TRAIN_I", "BATTERY_VEHICLES_I"],
    )
    value.loc[:, ["BEV"], ["MDV"]] = 0
    value.loc[:, ["BEV"], ["bus"]] = (
        sum(
            public_passenger_vehicle_fleet()
            .loc[:, "BEV", "bus", :]
            .reset_coords(drop=True)
            .rename({"HOUSEHOLDS_I": "HOUSEHOLDS_I!"}),
            dim=["HOUSEHOLDS_I!"],
        )
        .expand_dims({"TRANSPORT_POWER_TRAIN_I": ["BEV"]}, 1)
        .expand_dims({"BATTERY_VEHICLES_I": ["bus"]}, 2)
        .values
    )
    value.loc[:, ["BEV"], ["LDV"]] = (
        sum(
            private_passenger_vehicle_fleet()
            .loc[:, "BEV", "LDV", :]
            .reset_coords(drop=True)
            .rename({"HOUSEHOLDS_I": "HOUSEHOLDS_I!"}),
            dim=["HOUSEHOLDS_I!"],
        )
        .expand_dims({"TRANSPORT_POWER_TRAIN_I": ["BEV"]}, 1)
        .expand_dims({"BATTERY_VEHICLES_I": ["LDV"]}, 2)
        .values
    )
    value.loc[:, ["BEV"], ["MOTORCYCLES_2W_3W"]] = (
        sum(
            private_passenger_vehicle_fleet()
            .loc[:, "BEV", "MOTORCYCLES_2W_3W", :]
            .reset_coords(drop=True)
            .rename({"HOUSEHOLDS_I": "HOUSEHOLDS_I!"}),
            dim=["HOUSEHOLDS_I!"],
        )
        .expand_dims({"TRANSPORT_POWER_TRAIN_I": ["BEV"]}, 1)
        .expand_dims({"BATTERY_VEHICLES_I": ["MOTORCYCLES_2W_3W"]}, 2)
        .values
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, ["BEV"], ["MDV"]] = False
    except_subs.loc[:, ["BEV"], ["bus"]] = False
    except_subs.loc[:, ["BEV"], ["LDV"]] = False
    except_subs.loc[:, ["BEV"], ["MOTORCYCLES_2W_3W"]] = False
    value.values[except_subs.values] = 0
    return value


@component.add(
    name="total_passenger_transport_demand",
    units="km*person",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"passenger_transport_real_supply": 1},
)
def total_passenger_transport_demand():
    """
    Transport demand by region.
    """
    return sum(
        passenger_transport_real_supply().rename(
            {
                "TRANSPORT_POWER_TRAIN_I": "TRANSPORT_POWER_TRAIN_I!",
                "PASSENGERS_TRANSPORT_MODE_I": "PASSENGERS_TRANSPORT_MODE_I!",
                "HOUSEHOLDS_I": "HOUSEHOLDS_I!",
            }
        ),
        dim=[
            "TRANSPORT_POWER_TRAIN_I!",
            "PASSENGERS_TRANSPORT_MODE_I!",
            "HOUSEHOLDS_I!",
        ],
    )


@component.add(
    name="total_passenger_transport_demand_by_region",
    units="km*person",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_passenger_transport_demand_by_region_and_type_of_household": 1},
)
def total_passenger_transport_demand_by_region():
    return sum(
        total_passenger_transport_demand_by_region_and_type_of_household().rename(
            {"HOUSEHOLDS_I": "HOUSEHOLDS_I!"}
        ),
        dim=["HOUSEHOLDS_I!"],
    )


@component.add(
    name="total_passenger_transport_demand_by_region_and_type_of_household",
    units="km*person",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_hh_transport_disaggregated": 1,
        "passenger_transport_demand_corrected_by_gdppc": 1,
        "desired_transport_demand": 1,
        "exo_total_transport_demand_by_region_and_type_of_hh": 1,
        "switch_energy": 1,
    },
)
def total_passenger_transport_demand_by_region_and_type_of_household():
    """
    total transport demand comes from standalone part if SWITCH HH TRANSPORT DISAGREGATED=0, if SWITCH ENERGY=0 o SWITCH ECO HH TRANSPORT ENERGY BOTTOM UP=0 then transport demand comes from EXO transport demand variable in other case the transport demand comes from the economy transport demand variable.
    """
    return if_then_else(
        switch_hh_transport_disaggregated() == 0,
        lambda: passenger_transport_demand_corrected_by_gdppc(),
        lambda: if_then_else(
            switch_energy() == 0,
            lambda: exo_total_transport_demand_by_region_and_type_of_hh(),
            lambda: desired_transport_demand(),
        ),
    )


@component.add(
    name="total_passenger_transport_energy_consumption_by_region",
    units="MJ",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"energy_passenger_transport_consumption_by_fe_35r": 1},
)
def total_passenger_transport_energy_consumption_by_region():
    """
    Energy consumption by the passenger transport by region.
    """
    return sum(
        energy_passenger_transport_consumption_by_fe_35r().rename(
            {
                "NRG_FE_I": "NRG_FE_I!",
                "PASSENGERS_TRANSPORT_MODE_I": "PASSENGERS_TRANSPORT_MODE_I!",
                "HOUSEHOLDS_I": "HOUSEHOLDS_I!",
            }
        ),
        dim=["NRG_FE_I!", "PASSENGERS_TRANSPORT_MODE_I!", "HOUSEHOLDS_I!"],
    )


@component.add(
    name="total_passengers_transport_modes",
    units="person",
    subscripts=["REGIONS_35_I", "PASSENGERS_TRANSPORT_MODE_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"passengers_by_transport_modes": 1},
)
def total_passengers_transport_modes():
    return sum(
        passengers_by_transport_modes().rename(
            {
                "TRANSPORT_POWER_TRAIN_I": "TRANSPORT_POWER_TRAIN_I!",
                "HOUSEHOLDS_I": "HOUSEHOLDS_I!",
            }
        ),
        dim=["TRANSPORT_POWER_TRAIN_I!", "HOUSEHOLDS_I!"],
    )


@component.add(
    name="total_private_passenger_vehicle_fleet",
    units="vehicles",
    subscripts=["REGIONS_35_I", "TRANSPORT_POWER_TRAIN_I", "PRIVATE_TRANSPORT_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"private_passenger_vehicle_fleet": 1},
)
def total_private_passenger_vehicle_fleet():
    return (
        private_passenger_vehicle_fleet()
        .loc[:, :, :, "REPRESENTATIVE_HOUSEHOLD"]
        .reset_coords(drop=True)
    )


@component.add(
    name="total_public_passenger_vehicle_fleet",
    units="vehicles",
    subscripts=["REGIONS_35_I", "TRANSPORT_POWER_TRAIN_I", "PUBLIC_TRANSPORT_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"public_passenger_vehicle_fleet": 1},
)
def total_public_passenger_vehicle_fleet():
    return (
        public_passenger_vehicle_fleet()
        .loc[:, :, :, "REPRESENTATIVE_HOUSEHOLD"]
        .reset_coords(drop=True)
    )


@component.add(
    name="total_sum_passenger_transport_demand",
    units="km*person",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_passenger_transport_demand_by_region_and_type_of_household": 1},
)
def total_sum_passenger_transport_demand():
    return sum(
        total_passenger_transport_demand_by_region_and_type_of_household().rename(
            {"REGIONS_35_I": "REGIONS_35_I!", "HOUSEHOLDS_I": "HOUSEHOLDS_I!"}
        ),
        dim=["REGIONS_35_I!", "HOUSEHOLDS_I!"],
    )


@component.add(
    name="traffic_volume_per_capita",
    units="km",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_passenger_transport_demand": 1, "population_35_regions": 1},
)
def traffic_volume_per_capita():
    """
    Number of kilometers traveled per inhabitant per year.
    """
    return zidz(total_passenger_transport_demand(), population_35_regions())


@component.add(
    name="TREND_BEV_BUS", units="DMNL", comp_type="Constant", comp_subtype="Normal"
)
def trend_bev_bus():
    """
    Trend BEV LDV
    """
    return 0.16


@component.add(
    name="TREND_BEV_LDV", units="DMNL", comp_type="Constant", comp_subtype="Normal"
)
def trend_bev_ldv():
    """
    Trend BEV LDV
    """
    return 0.17


@component.add(name="TREND_PUBLIC", comp_type="Constant", comp_subtype="Normal")
def trend_public():
    return 0.01


@component.add(
    name="wear_passenger_private_vehicles",
    units="vehicle/Years",
    subscripts=[
        "REGIONS_35_I",
        "TRANSPORT_POWER_TRAIN_I",
        "PRIVATE_TRANSPORT_I",
        "HOUSEHOLDS_I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "private_passenger_vehicle_fleet": 1,
        "smooth_lifetime_passengers_vehicles": 1,
        "smooth_wear_passenger_private_vehicles_mod_factor": 1,
    },
)
def wear_passenger_private_vehicles():
    """
    Private vehicle scrapping flow in vehicles/year
    """
    return (
        zidz(
            private_passenger_vehicle_fleet(),
            smooth_lifetime_passengers_vehicles()
            .loc[:, :, _subscript_dict["PRIVATE_TRANSPORT_I"], :]
            .rename({"PASSENGERS_TRANSPORT_MODE_I": "PRIVATE_TRANSPORT_I"}),
        )
        * smooth_wear_passenger_private_vehicles_mod_factor()
    )


@component.add(
    name="wear_passenger_private_vehicles_mod_factor",
    units="1",
    subscripts=[
        "REGIONS_35_I",
        "TRANSPORT_POWER_TRAIN_I",
        "PRIVATE_TRANSPORT_I",
        "HOUSEHOLDS_I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"new_passenger_private_vehicles": 1, "time": 1},
)
def wear_passenger_private_vehicles_mod_factor():
    """
    Factor that modifies the wear passenger private vehicles when the flow of new vehicles goes to 0.
    """
    return if_then_else(
        np.logical_and(new_passenger_private_vehicles() == 0, time() > 2005),
        lambda: xr.DataArray(
            2,
            {
                "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
                "PRIVATE_TRANSPORT_I": _subscript_dict["PRIVATE_TRANSPORT_I"],
                "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
            },
            [
                "REGIONS_35_I",
                "TRANSPORT_POWER_TRAIN_I",
                "PRIVATE_TRANSPORT_I",
                "HOUSEHOLDS_I",
            ],
        ),
        lambda: xr.DataArray(
            1,
            {
                "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
                "PRIVATE_TRANSPORT_I": _subscript_dict["PRIVATE_TRANSPORT_I"],
                "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
            },
            [
                "REGIONS_35_I",
                "TRANSPORT_POWER_TRAIN_I",
                "PRIVATE_TRANSPORT_I",
                "HOUSEHOLDS_I",
            ],
        ),
    )


@component.add(
    name="wear_passenger_public_vehicles",
    units="vehicles/Year",
    subscripts=[
        "REGIONS_35_I",
        "TRANSPORT_POWER_TRAIN_I",
        "PUBLIC_TRANSPORT_I",
        "HOUSEHOLDS_I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "public_passenger_vehicle_fleet": 1,
        "smooth_lifetime_passengers_vehicles": 1,
        "smooth_wear_passenger_public_vehicles_mod_factor": 1,
    },
)
def wear_passenger_public_vehicles():
    """
    Public vehicle scrapping flow in vehicles/year.
    """
    return (
        zidz(
            public_passenger_vehicle_fleet(),
            smooth_lifetime_passengers_vehicles()
            .loc[:, :, _subscript_dict["PUBLIC_TRANSPORT_I"], :]
            .rename({"PASSENGERS_TRANSPORT_MODE_I": "PUBLIC_TRANSPORT_I"}),
        )
        * smooth_wear_passenger_public_vehicles_mod_factor()
    )


@component.add(
    name="wear_passenger_public_vehicles_mod_factor",
    units="1",
    subscripts=[
        "REGIONS_35_I",
        "TRANSPORT_POWER_TRAIN_I",
        "PUBLIC_TRANSPORT_I",
        "HOUSEHOLDS_I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"new_passenger_public_vehicles": 1, "time": 1},
)
def wear_passenger_public_vehicles_mod_factor():
    return if_then_else(
        np.logical_and(new_passenger_public_vehicles() == 0, time() > 2005),
        lambda: xr.DataArray(
            2,
            {
                "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
                "PUBLIC_TRANSPORT_I": _subscript_dict["PUBLIC_TRANSPORT_I"],
                "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
            },
            [
                "REGIONS_35_I",
                "TRANSPORT_POWER_TRAIN_I",
                "PUBLIC_TRANSPORT_I",
                "HOUSEHOLDS_I",
            ],
        ),
        lambda: xr.DataArray(
            1,
            {
                "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
                "PUBLIC_TRANSPORT_I": _subscript_dict["PUBLIC_TRANSPORT_I"],
                "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
            },
            [
                "REGIONS_35_I",
                "TRANSPORT_POWER_TRAIN_I",
                "PUBLIC_TRANSPORT_I",
                "HOUSEHOLDS_I",
            ],
        ),
    )


@component.add(
    name="world_total_passenger_transport_demand",
    units="km*person",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_passenger_transport_demand": 1},
)
def world_total_passenger_transport_demand():
    """
    Total world transport demand.
    """
    return sum(
        total_passenger_transport_demand().rename({"REGIONS_35_I": "REGIONS_35_I!"}),
        dim=["REGIONS_35_I!"],
    )
