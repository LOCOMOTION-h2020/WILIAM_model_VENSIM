"""
Module energy.utility_scale_storage.losses
Translated using PySD version 3.10.0
"""


@component.add(
    name="CHARGING_LOSSES_SHARE_BY_PROSTO_ELEC",
    units="DMNL",
    subscripts=["NRG_PROSTO_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "charging_losses_share_by_prosto_elec_dedicated": 1,
        "ev_charge_losses_share": 1,
    },
)
def charging_losses_share_by_prosto_elec():
    """
    Charging losses by storage utility-scale facility.
    """
    value = xr.DataArray(
        np.nan, {"NRG_PROSTO_I": _subscript_dict["NRG_PROSTO_I"]}, ["NRG_PROSTO_I"]
    )
    value.loc[
        _subscript_dict["PROSTO_ELEC_DEDICATED_I"]
    ] = charging_losses_share_by_prosto_elec_dedicated().values
    value.loc[["PROSTO_V2G"]] = ev_charge_losses_share()
    return value


@component.add(
    name="CHARGING_LOSSES_SHARE_BY_PROSTO_ELEC_DEDICATED",
    units="DMNL",
    subscripts=["PROSTO_ELEC_DEDICATED_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_charging_losses_share_by_prosto_elec_dedicated"
    },
)
def charging_losses_share_by_prosto_elec_dedicated():
    """
    Relative charging losses by storage utility-scale facility.
    """
    return _ext_constant_charging_losses_share_by_prosto_elec_dedicated()


_ext_constant_charging_losses_share_by_prosto_elec_dedicated = ExtConstant(
    "model_parameters/energy/energy-storage.xlsx",
    "Dedicated_capacities",
    "CHARGING_LOSSES_SHARE_BY_PROSTO_ELEC_DEDICATED*",
    {"PROSTO_ELEC_DEDICATED_I": _subscript_dict["PROSTO_ELEC_DEDICATED_I"]},
    _root,
    {"PROSTO_ELEC_DEDICATED_I": _subscript_dict["PROSTO_ELEC_DEDICATED_I"]},
    "_ext_constant_charging_losses_share_by_prosto_elec_dedicated",
)


@component.add(
    name="DISCHARGE_LOSSES_SHARE_BY_PROSTO_ELEC_DEDICATED",
    units="DMNL",
    subscripts=["PROSTO_ELEC_DEDICATED_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_discharge_losses_share_by_prosto_elec_dedicated"
    },
)
def discharge_losses_share_by_prosto_elec_dedicated():
    """
    Relative discharging losses by storage utility-scale facility.
    """
    return _ext_constant_discharge_losses_share_by_prosto_elec_dedicated()


_ext_constant_discharge_losses_share_by_prosto_elec_dedicated = ExtConstant(
    "model_parameters/energy/energy-storage.xlsx",
    "Dedicated_capacities",
    "DISCHARGE_LOSSES_SHARE_BY_PROSTO_ELEC_DEDICATED*",
    {"PROSTO_ELEC_DEDICATED_I": _subscript_dict["PROSTO_ELEC_DEDICATED_I"]},
    _root,
    {"PROSTO_ELEC_DEDICATED_I": _subscript_dict["PROSTO_ELEC_DEDICATED_I"]},
    "_ext_constant_discharge_losses_share_by_prosto_elec_dedicated",
)


@component.add(
    name="DISCHARGING_LOSSES_SHARE_BY_PROSTO_ELEC",
    units="DMNL",
    subscripts=["NRG_PROSTO_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "discharge_losses_share_by_prosto_elec_dedicated": 1,
        "ev_discharge_losses_share": 1,
    },
)
def discharging_losses_share_by_prosto_elec():
    """
    Discharging losses by storage utility-scale facility.
    """
    value = xr.DataArray(
        np.nan, {"NRG_PROSTO_I": _subscript_dict["NRG_PROSTO_I"]}, ["NRG_PROSTO_I"]
    )
    value.loc[
        _subscript_dict["PROSTO_ELEC_DEDICATED_I"]
    ] = discharge_losses_share_by_prosto_elec_dedicated().values
    value.loc[["PROSTO_V2G"]] = ev_discharge_losses_share()
    return value


@component.add(
    name="elec_transmission_losses_by_PROSTO",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "PROSTO_ELEC_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "stored_energy_input_by_prosto": 1,
        "prosup_transmission_loss_shares": 1,
    },
)
def elec_transmission_losses_by_prosto():
    """
    Roundtrip storage losses and additional transmission losses by PROcess STOrage.
    """
    return stored_energy_input_by_prosto() * prosup_transmission_loss_shares().loc[
        :, "PROSUP_transmission_losses_elec"
    ].reset_coords(drop=True)


@component.add(
    name="PROSTO_capacity_stock",
    units="TW",
    subscripts=["REGIONS_9_I", "NRG_PROSTO_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"prosto_dedicated_capacity_stock": 1, "ev_batteries_power_v2g_9r": 1},
)
def prosto_capacity_stock():
    """
    Capacity stock by PROcess STOrage.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "NRG_PROSTO_I": _subscript_dict["NRG_PROSTO_I"],
        },
        ["REGIONS_9_I", "NRG_PROSTO_I"],
    )
    value.loc[
        :, _subscript_dict["PROSTO_ELEC_DEDICATED_I"]
    ] = prosto_dedicated_capacity_stock().values
    value.loc[:, ["PROSTO_V2G"]] = (
        ev_batteries_power_v2g_9r().expand_dims({"NRG_PRO_I": ["PROSTO_V2G"]}, 1).values
    )
    return value


@component.add(
    name="roundtrip_and_transmission_losses_by_PROSTO",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "PROSTO_ELEC_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "stored_energy_losses_roundtrip_by_prosto": 1,
        "elec_transmission_losses_by_prosto": 1,
    },
)
def roundtrip_and_transmission_losses_by_prosto():
    """
    Roundtrip storage losses and additional transmission losses by PROcess STOrage.
    """
    return (
        stored_energy_losses_roundtrip_by_prosto()
        + elec_transmission_losses_by_prosto()
    )


@component.add(
    name="stored_energy_input_by_PROSTO",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "PROSTO_ELEC_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "stored_energy_output_by_prosto": 1,
        "stored_energy_losses_roundtrip_by_prosto": 1,
    },
)
def stored_energy_input_by_prosto():
    """
    Total energy entering the storage device.
    """
    return stored_energy_output_by_prosto() + stored_energy_losses_roundtrip_by_prosto()


@component.add(
    name="stored_energy_losses_roundtrip_by_PROSTO",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "PROSTO_ELEC_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "stored_energy_output_by_prosto": 2,
        "charging_losses_share_by_prosto_elec": 1,
        "discharging_losses_share_by_prosto_elec": 1,
    },
)
def stored_energy_losses_roundtrip_by_prosto():
    """
    Energy losses associated to storage by PROcess STOrage.
    """
    return (
        stored_energy_output_by_prosto()
        / (
            (
                1
                - charging_losses_share_by_prosto_elec().rename(
                    {"NRG_PROSTO_I": "PROSTO_ELEC_I"}
                )
            )
            * (
                1
                - discharging_losses_share_by_prosto_elec().rename(
                    {"NRG_PROSTO_I": "PROSTO_ELEC_I"}
                )
            )
        )
        - stored_energy_output_by_prosto()
    )


@component.add(
    name="stored_energy_output_by_PROSTO",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "PROSTO_ELEC_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cf_prosto": 1,
        "prosto_capacity_stock": 1,
        "unit_conversion_hours_year": 1,
        "unit_conversion_tw_per_ej_per_year": 1,
    },
)
def stored_energy_output_by_prosto():
    """
    Total energy exiting the storage device.
    """
    return (
        cf_prosto().rename({"NRG_PROSTO_I": "PROSTO_ELEC_I"})
        * prosto_capacity_stock().rename({"NRG_PROSTO_I": "PROSTO_ELEC_I"})
        * unit_conversion_hours_year()
        * unit_conversion_tw_per_ej_per_year()
    )


@component.add(
    name="total_PROSTO_losses_elec",
    units="EJ/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"roundtrip_and_transmission_losses_by_prosto": 1},
)
def total_prosto_losses_elec():
    """
    Storage losses including roundtrip storage and additional transmission losses.
    """
    return sum(
        roundtrip_and_transmission_losses_by_prosto().rename(
            {"PROSTO_ELEC_I": "NRG_PROSTO_I!"}
        ),
        dim=["NRG_PROSTO_I!"],
    )
