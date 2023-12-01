"""
Module energy.eroi.ev_batteries_esoi
Translated using PySD version 3.10.0
"""


@component.add(
    name="dyn_PEnU_batteries_electrified_vehicle",
    units="MJ/battery",
    subscripts=[
        "REGIONS_35_I",
        "EV_BATTERIES_I",
        "TRANSPORT_POWER_TRAIN_I",
        "BATTERY_VEHICLES_I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "embodied_pe_intensity_materials_36r": 1,
        "machining_rate_ev_batteries": 1,
        "materials_per_new_capacity_installed_ev_batteries": 1,
        "scrap_rate": 1,
        "vehicle_electric_power": 1,
        "unit_conversion_kw_mw": 1,
    },
)
def dyn_penu_batteries_electrified_vehicle():
    """
    Energy intensity (primary) of the construction of Electrified Vehicles batteries PER BATTERY.
    """
    return (
        sum(
            embodied_pe_intensity_materials_36r()
            .loc[_subscript_dict["REGIONS_35_I"], :]
            .rename({"REGIONS_36_I": "REGIONS_35_I", "MATERIALS_I": "MATERIALS_I!"})
            * machining_rate_ev_batteries()
            * materials_per_new_capacity_installed_ev_batteries().rename(
                {"MATERIALS_I": "MATERIALS_I!"}
            ),
            dim=["MATERIALS_I!"],
        )
        * (1 + scrap_rate())
        * vehicle_electric_power()
        / unit_conversion_kw_mw()
    )


@component.add(
    name="dynFEnUst_EV_batteries",
    units="EJ/Year",
    subscripts=["REGIONS_35_I", "EV_BATTERIES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_fei_elec_storage0": 1,
        "power_new_vehicle_batteries_35r": 1,
        "share_energy_requirements_for_decom_ev_batteries": 1,
        "power_discarded_vehicle_batteries": 1,
        "dynfenust_intensity_ev_batteries": 2,
    },
)
def dynfenust_ev_batteries():
    """
    Dynamic final energy invested for EV batteries.
    """
    return if_then_else(
        switch_fei_elec_storage0() == 1,
        lambda: xr.DataArray(
            0,
            {
                "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                "EV_BATTERIES_I": _subscript_dict["EV_BATTERIES_I"],
            },
            ["REGIONS_35_I", "EV_BATTERIES_I"],
        ),
        lambda: dynfenust_intensity_ev_batteries() * power_new_vehicle_batteries_35r()
        + power_discarded_vehicle_batteries()
        * dynfenust_intensity_ev_batteries()
        * share_energy_requirements_for_decom_ev_batteries(),
    )


@component.add(
    name="dynFEnUst_EV_batteries_9R",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "EV_BATTERIES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"dynfenust_ev_batteries": 2},
)
def dynfenust_ev_batteries_9r():
    """
    Dynamic final energy invested for EV batteries for 9 regions.
    """
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
            dynfenust_ev_batteries()
            .loc[_subscript_dict["REGIONS_EU27_I"], :]
            .rename({"REGIONS_35_I": "REGIONS_EU27_I!"}),
            dim=["REGIONS_EU27_I!"],
        )
        .expand_dims({"REGIONS_36_I": ["EU27"]}, 0)
        .values
    )
    value.loc[_subscript_dict["REGIONS_8_I"], :] = (
        dynfenust_ev_batteries()
        .loc[_subscript_dict["REGIONS_8_I"], :]
        .rename({"REGIONS_35_I": "REGIONS_8_I"})
        .values
    )
    return value


@component.add(
    name="dynFEnUst_intensity_EV_batteries",
    units="EJ/TW",
    subscripts=["REGIONS_35_I", "EV_BATTERIES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "dynpenust_intensity_ev_batteries": 2,
        "final_to_primary_energy_by_region_until_2015": 2,
    },
)
def dynfenust_intensity_ev_batteries():
    """
    Energy use (in final energy terms) per new installed capacity (TW) over lifetime for EV batteries. Dynamic variable affected by recycling policies.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "EV_BATTERIES_I": _subscript_dict["EV_BATTERIES_I"],
        },
        ["REGIONS_35_I", "EV_BATTERIES_I"],
    )
    value.loc[_subscript_dict["REGIONS_8_I"], :] = (
        dynpenust_intensity_ev_batteries()
        .loc[_subscript_dict["REGIONS_8_I"], :]
        .rename({"REGIONS_35_I": "REGIONS_8_I"})
        * final_to_primary_energy_by_region_until_2015()
        .loc[_subscript_dict["REGIONS_8_I"]]
        .rename({"REGIONS_9_I": "REGIONS_8_I"})
    ).values
    value.loc[_subscript_dict["REGIONS_EU27_I"], :] = (
        dynpenust_intensity_ev_batteries()
        .loc[_subscript_dict["REGIONS_EU27_I"], :]
        .rename({"REGIONS_35_I": "REGIONS_EU27_I"})
        * float(final_to_primary_energy_by_region_until_2015().loc["EU27"])
    ).values
    return value


@component.add(
    name="dynPEnUst_intensity_EV_batteries",
    units="EJ/TW",
    subscripts=["REGIONS_35_I", "EV_BATTERIES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "required_embodied_pe_materials_for_ev_batteries": 1,
        "power_new_vehicle_batteries_35r": 1,
    },
)
def dynpenust_intensity_ev_batteries():
    """
    Energy use (in primary energy terms) per new installed capacity (TW) over lifetime for EV batteries. Dynamic variable affected by recycling policies.
    """
    return zidz(
        required_embodied_pe_materials_for_ev_batteries(),
        power_new_vehicle_batteries_35r(),
    )


@component.add(
    name="EnU_of_charger_and_grids",
    units="MJ/MW",
    subscripts=["REGIONS_35_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "embodied_pe_intensity_materials_36r": 1,
        "machining_rate_ev_batteries": 1,
        "materials_required_for_new_ev_chargers": 1,
        "materials_required_for_new_ev_chargers_grids": 1,
        "unit_conversion_kg_mt": 1,
        "power_new_vehicle_batteries_35r": 1,
        "unit_conversion_mw_tw": 1,
    },
)
def enu_of_charger_and_grids():
    """
    EnU per material of the chargers and grids for the EV batteries
    """
    return zidz(
        embodied_pe_intensity_materials_36r()
        .loc[_subscript_dict["REGIONS_35_I"], :]
        .rename({"REGIONS_36_I": "REGIONS_35_I"})
        * machining_rate_ev_batteries()
        * (
            materials_required_for_new_ev_chargers()
            + materials_required_for_new_ev_chargers_grids()
        )
        * unit_conversion_kg_mt(),
        (
            sum(
                power_new_vehicle_batteries_35r().rename(
                    {"EV_BATTERIES_I": "EV_BATTERIES_I!"}
                ),
                dim=["EV_BATTERIES_I!"],
            )
            * unit_conversion_mw_tw()
        ).expand_dims({"MATERIALS_I": _subscript_dict["MATERIALS_I"]}, 1),
    )


@component.add(
    name="EnU_total_of_charger_and_grids",
    units="MJ/MW",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"enu_of_charger_and_grids": 1},
)
def enu_total_of_charger_and_grids():
    """
    EnU of the chargers and grids for the EV batteries
    """
    return sum(
        enu_of_charger_and_grids().rename({"MATERIALS_I": "MATERIALS_I!"}),
        dim=["MATERIALS_I!"],
    )


@component.add(
    name="ESOI_final_electrified_vehicle",
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
        "energy_delivered_by_electrified_vehicles_battery": 2,
        "ol_ev_batteries": 2,
        "eabe": 1,
        "vehicle_electric_power": 2,
        "ev_charge_losses_share": 2,
        "dyn_penu_batteries_electrified_vehicle": 1,
        "transport_total_ev_vehicles_technology_energy": 1,
        "enu_total_of_charger_and_grids": 1,
        "unit_conversion_kw_mw": 2,
        "share_energy_requirements_for_decom_ev_batteries": 1,
    },
)
def esoi_final_electrified_vehicle():
    """
    Dynamic ESOI final over lifetime of electrified vehicle battery
    """
    return zidz(
        energy_delivered_by_electrified_vehicles_battery()
        * (1 - ol_ev_batteries())
        * (1 - eabe()),
        dyn_penu_batteries_electrified_vehicle()
        * (1 + share_energy_requirements_for_decom_ev_batteries())
        + transport_total_ev_vehicles_technology_energy()
        * vehicle_electric_power()
        / unit_conversion_kw_mw()
        + (
            enu_total_of_charger_and_grids()
            * vehicle_electric_power()
            / unit_conversion_kw_mw()
        )
        + energy_delivered_by_electrified_vehicles_battery()
        * (1 - ol_ev_batteries())
        * (ev_charge_losses_share() / 1 - ev_charge_losses_share()),
    )


@component.add(
    name="ESOI_st_electrified_vehicle",
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
        "energy_delivered_by_electrified_vehicles_battery": 1,
        "ol_ev_batteries": 1,
        "vehicle_electric_power": 1,
        "dyn_penu_batteries_electrified_vehicle": 1,
        "transport_batteries_materials_energy": 1,
        "unit_conversion_kw_mw": 1,
        "share_energy_requirements_for_decom_ev_batteries": 1,
    },
)
def esoi_st_electrified_vehicle():
    """
    Dynamic ESOIst over lifetime of electrified vehicle battery
    """
    return zidz(
        energy_delivered_by_electrified_vehicles_battery() * (1 - ol_ev_batteries()),
        dyn_penu_batteries_electrified_vehicle()
        * (1 + share_energy_requirements_for_decom_ev_batteries())
        + transport_batteries_materials_energy()
        * vehicle_electric_power()
        / unit_conversion_kw_mw(),
    )


@component.add(
    name="required_embodied_PE_materials_for_EV_batteries",
    units="EJ",
    subscripts=["REGIONS_35_I", "EV_BATTERIES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"required_embodied_pe_per_material_for_ev_batteries": 1},
)
def required_embodied_pe_materials_for_ev_batteries():
    """
    Required embodied primary energy of total material consumption for EV batteries.
    """
    return sum(
        required_embodied_pe_per_material_for_ev_batteries().rename(
            {"MATERIALS_I": "MATERIALS_I!"}
        ),
        dim=["MATERIALS_I!"],
    )


@component.add(
    name="required_embodied_PE_materials_for_EV_batteries_9R",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "EV_BATTERIES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"required_embodied_pe_materials_for_ev_batteries": 2},
)
def required_embodied_pe_materials_for_ev_batteries_9r():
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
            required_embodied_pe_materials_for_ev_batteries()
            .loc[_subscript_dict["REGIONS_EU27_I"], :]
            .rename({"REGIONS_35_I": "REGIONS_EU27_I!"}),
            dim=["REGIONS_EU27_I!"],
        )
        .expand_dims({"REGIONS_36_I": ["EU27"]}, 0)
        .values
    )
    value.loc[_subscript_dict["REGIONS_8_I"], :] = (
        required_embodied_pe_materials_for_ev_batteries()
        .loc[_subscript_dict["REGIONS_8_I"], :]
        .rename({"REGIONS_35_I": "REGIONS_8_I"})
        .values
    )
    return value


@component.add(
    name="required_embodied_PE_per_material_for_EV_batteries",
    units="EJ",
    subscripts=["REGIONS_35_I", "MATERIALS_I", "EV_BATTERIES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "materials_required_for_new_ev_batteries": 1,
        "embodied_pe_intensity_materials_36r": 1,
        "unit_conversion_mj_ej": 1,
        "unit_conversion_kg_mt": 1,
    },
)
def required_embodied_pe_per_material_for_ev_batteries():
    """
    Required embodied primary energy of material consumption for EV batteries.
    """
    return (
        materials_required_for_new_ev_batteries()
        * embodied_pe_intensity_materials_36r()
        .loc[_subscript_dict["REGIONS_35_I"], :]
        .rename({"REGIONS_36_I": "REGIONS_35_I"})
        * (unit_conversion_kg_mt() / unit_conversion_mj_ej())
    )


@component.add(
    name="total_dynFEnUst_EV_batteries_9R",
    units="EJ",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"dynfenust_ev_batteries_9r": 1},
)
def total_dynfenust_ev_batteries_9r():
    """
    Total dynamic final energy use for EV batteries by country.
    """
    return sum(
        dynfenust_ev_batteries_9r().rename({"EV_BATTERIES_I": "EV_BATTERIES_I!"}),
        dim=["EV_BATTERIES_I!"],
    )


@component.add(
    name="Total_EV_batteries_ESOI",
    units="DMNL",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"esoi_st_electrified_vehicle": 1, "power_new_vehicle_batteries_35r": 2},
)
def total_ev_batteries_esoi():
    return zidz(
        sum(
            esoi_st_electrified_vehicle()
            .loc[:, :, "EV", "LDV"]
            .reset_coords(drop=True)
            .rename({"EV_BATTERIES_I": "EV_BATTERIES_I!"})
            * power_new_vehicle_batteries_35r().rename(
                {"EV_BATTERIES_I": "EV_BATTERIES_I!"}
            ),
            dim=["EV_BATTERIES_I!"],
        ),
        sum(
            power_new_vehicle_batteries_35r().rename(
                {"EV_BATTERIES_I": "EV_BATTERIES_I!"}
            ),
            dim=["EV_BATTERIES_I!"],
        ),
    )


@component.add(
    name="transport_batteries_materials_energy",
    units="MJ/MW",
    subscripts=["REGIONS_35_I", "EV_BATTERIES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "materials_required_for_new_ev_batteries": 2,
        "unit_conversion_kg_mt": 2,
        "power_new_vehicle_batteries_35r": 2,
        "matrix_unit_prefixes": 2,
    },
)
def transport_batteries_materials_energy():
    """
    Energy used to transport battery materials using the methodology of De Castro et al.
    """
    return (
        1.19
        * zidz(
            sum(
                materials_required_for_new_ev_batteries().rename(
                    {"MATERIALS_I": "MATERIALS_I!"}
                )
                * unit_conversion_kg_mt(),
                dim=["MATERIALS_I!"],
            ),
            power_new_vehicle_batteries_35r() * 1000000.0,
        )
        * 500
        * 3.5
        + 1.09
        * zidz(
            sum(
                materials_required_for_new_ev_batteries().rename(
                    {"MATERIALS_I": "MATERIALS_I!"}
                )
                * unit_conversion_kg_mt(),
                dim=["MATERIALS_I!"],
            ),
            power_new_vehicle_batteries_35r()
            * float(matrix_unit_prefixes().loc["tera", "mega"]),
        )
        * 10000
        * 0.2
        + 1.19 * 0 * 3.5 * 250
    ) / float(matrix_unit_prefixes().loc["mega", "kilo"])


@component.add(
    name="transport_total_EV_vehicles_technology_energy",
    units="MJ/MW",
    subscripts=["REGIONS_35_I", "EV_BATTERIES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "materials_required_for_new_ev_batteries": 2,
        "unit_conversion_kg_mt": 3,
        "power_new_vehicle_batteries_35r": 5,
        "matrix_unit_prefixes": 7,
        "total_materials_required_for_new_ev_chargers_and_grids_without_cement": 2,
        "cement_required_for_new_ev_chargers_and_grids": 1,
    },
)
def transport_total_ev_vehicles_technology_energy():
    """
    Energy used to transport battery and infrastructure materials using the methodology of De Castro et al.
    """
    return (
        1.19
        * (
            zidz(
                sum(
                    materials_required_for_new_ev_batteries().rename(
                        {"MATERIALS_I": "MATERIALS_I!"}
                    ),
                    dim=["MATERIALS_I!"],
                )
                * unit_conversion_kg_mt(),
                power_new_vehicle_batteries_35r()
                * float(matrix_unit_prefixes().loc["tera", "mega"]),
            )
            + zidz(
                total_materials_required_for_new_ev_chargers_and_grids_without_cement()
                * float(matrix_unit_prefixes().loc["tera", "mega"]),
                sum(
                    power_new_vehicle_batteries_35r().rename(
                        {"EV_BATTERIES_I": "EV_BATTERIES_I!"}
                    ),
                    dim=["EV_BATTERIES_I!"],
                )
                * float(matrix_unit_prefixes().loc["tera", "mega"]),
            )
        )
        * 500
        * 3.5
        + 1.09
        * (
            zidz(
                sum(
                    materials_required_for_new_ev_batteries().rename(
                        {"MATERIALS_I": "MATERIALS_I!"}
                    ),
                    dim=["MATERIALS_I!"],
                )
                * unit_conversion_kg_mt(),
                power_new_vehicle_batteries_35r()
                * float(matrix_unit_prefixes().loc["tera", "mega"]),
            )
            + zidz(
                total_materials_required_for_new_ev_chargers_and_grids_without_cement()
                * unit_conversion_kg_mt(),
                sum(
                    power_new_vehicle_batteries_35r().rename(
                        {"EV_BATTERIES_I": "EV_BATTERIES_I!"}
                    ),
                    dim=["EV_BATTERIES_I!"],
                )
                * float(matrix_unit_prefixes().loc["tera", "mega"]),
            )
        )
        * 10000
        * 0.2
        + (
            1.19
            * zidz(
                cement_required_for_new_ev_chargers_and_grids(),
                sum(
                    power_new_vehicle_batteries_35r().rename(
                        {"EV_BATTERIES_I": "EV_BATTERIES_I!"}
                    )
                    * float(matrix_unit_prefixes().loc["tera", "mega"]),
                    dim=["EV_BATTERIES_I!"],
                ),
            )
            * 3.5
            * 250
        )
    ) / float(matrix_unit_prefixes().loc["mega", "kilo"])
