"""
Module energy.eroi.protra
Translated using PySD version 3.10.0
"""


@component.add(
    name="check_dynFEnUst_intensity_new_PROTRA",
    units="EJ/TW",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"dynfenust_intensity_new_protra": 1},
)
def check_dynfenust_intensity_new_protra():
    return sum(
        dynfenust_intensity_new_protra().rename(
            {
                "REGIONS_9_I": "REGIONS_9_I!",
                "NRG_TO_I": "NRG_TO_I!",
                "NRG_PROTRA_I": "NRG_PROTRA_I!",
            }
        ),
        dim=["REGIONS_9_I!", "NRG_TO_I!", "NRG_PROTRA_I!"],
    )


@component.add(
    name="check_dynFEnUst_new_grids",
    units="EJ/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"dynfenust_new_grids": 1},
)
def check_dynfenust_new_grids():
    return sum(
        dynfenust_new_grids().rename(
            {
                "REGIONS_9_I": "REGIONS_9_I!",
                "NRG_TO_I": "NRG_TO_I!",
                "NRG_PROTRA_I": "NRG_PROTRA_I!",
            }
        ),
        dim=["REGIONS_9_I!", "NRG_TO_I!", "NRG_PROTRA_I!"],
    )


@component.add(
    name="check_dynFEnUst_new_PROTRA",
    units="EJ/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"dynfenust_new_protra": 1},
)
def check_dynfenust_new_protra():
    return sum(
        dynfenust_new_protra().rename(
            {
                "REGIONS_9_I": "REGIONS_9_I!",
                "NRG_TO_I": "NRG_TO_I!",
                "NRG_PROTRA_I": "NRG_PROTRA_I!",
            }
        ),
        dim=["REGIONS_9_I!", "NRG_TO_I!", "NRG_PROTRA_I!"],
    )


@component.add(
    name="check_dynFEnUst_OM_PROTRA",
    units="EJ/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"dynfenust_om_protra": 1},
)
def check_dynfenust_om_protra():
    return sum(
        dynfenust_om_protra().rename(
            {
                "REGIONS_9_I": "REGIONS_9_I!",
                "NRG_TO_I": "NRG_TO_I!",
                "NRG_PROTRA_I": "NRG_PROTRA_I!",
            }
        ),
        dim=["REGIONS_9_I!", "NRG_TO_I!", "NRG_PROTRA_I!"],
    )


@component.add(
    name="check_required_embodied_FE_per_material_for_new_PROTRA",
    units="EJ/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"required_embodied_fe_per_material_for_new_protra": 1},
)
def check_required_embodied_fe_per_material_for_new_protra():
    return sum(
        required_embodied_fe_per_material_for_new_protra().rename(
            {
                "REGIONS_9_I": "REGIONS_9_I!",
                "NRG_PROTRA_I": "NRG_PROTRA_I!",
                "MATERIALS_I": "MATERIALS_I!",
            }
        ),
        dim=["REGIONS_9_I!", "NRG_PROTRA_I!", "MATERIALS_I!"],
    )


@component.add(
    name="Clean_water_for_OM_required_for_PROTRA",
    units="Mt",
    subscripts=["REGIONS_9_I", "NRG_TO_I", "NRG_PROTRA_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_capacity_stock": 1,
        "clean_water_intensity_csp_om": 1,
        "matrix_unit_prefixes": 2,
    },
)
def clean_water_for_om_required_for_protra():
    """
    Annual water required for the operation and maintenance of the capacity of PROTRA in operation.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "NRG_TO_I": _subscript_dict["NRG_TO_I"],
            "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
        },
        ["REGIONS_9_I", "NRG_TO_I", "NRG_PROTRA_I"],
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, :, ["PROTRA_PP_solar_CSP"]] = False
    value.values[except_subs.values] = 0
    value.loc[:, :, ["PROTRA_PP_solar_CSP"]] = (
        (
            protra_capacity_stock()
            .loc[:, :, "PROTRA_PP_solar_CSP"]
            .reset_coords(drop=True)
            * clean_water_intensity_csp_om()
            * float(matrix_unit_prefixes().loc["tera", "mega"])
            / float(matrix_unit_prefixes().loc["giga", "BASE_UNIT"])
        )
        .expand_dims({"NRG_PRO_I": ["PROTRA_PP_solar_CSP"]}, 2)
        .values
    )
    return value


@component.add(
    name="Distilled_water_for_OM_required_for_PROTRA",
    units="Mt",
    subscripts=["REGIONS_9_I", "NRG_TO_I", "NRG_PROTRA_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_capacity_stock": 2,
        "distilled_water_intensity_csp_om": 1,
        "matrix_unit_prefixes": 4,
        "distilled_water_intensity_pv_om": 1,
    },
)
def distilled_water_for_om_required_for_protra():
    """
    Annual water required for the operation and maintenance of the capacity of PROTRA.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "NRG_TO_I": _subscript_dict["NRG_TO_I"],
            "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
        },
        ["REGIONS_9_I", "NRG_TO_I", "NRG_PROTRA_I"],
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, :, ["PROTRA_PP_solar_CSP"]] = False
    except_subs.loc[:, :, ["PROTRA_PP_solar_open_space_PV"]] = False
    value.values[except_subs.values] = 0
    value.loc[:, :, ["PROTRA_PP_solar_CSP"]] = (
        (
            protra_capacity_stock()
            .loc[:, :, "PROTRA_PP_solar_CSP"]
            .reset_coords(drop=True)
            * distilled_water_intensity_csp_om()
            * float(matrix_unit_prefixes().loc["tera", "mega"])
            / float(matrix_unit_prefixes().loc["giga", "BASE_UNIT"])
        )
        .expand_dims({"NRG_PRO_I": ["PROTRA_PP_solar_CSP"]}, 2)
        .values
    )
    value.loc[:, :, ["PROTRA_PP_solar_open_space_PV"]] = (
        (
            protra_capacity_stock()
            .loc[:, :, "PROTRA_PP_solar_open_space_PV"]
            .reset_coords(drop=True)
            * distilled_water_intensity_pv_om()
            * float(matrix_unit_prefixes().loc["tera", "mega"])
            / float(matrix_unit_prefixes().loc["giga", "BASE_UNIT"])
        )
        .expand_dims({"NRG_PRO_I": ["PROTRA_PP_solar_open_space_PV"]}, 2)
        .values
    )
    return value


@component.add(
    name="dynEROIst_PROTRA",
    units="DMNL",
    subscripts=["REGIONS_9_I", "NRG_TO_I", "NRG_PROTRA_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_to_allocated": 9,
        "fenust_protra_eroi_exogenous": 4,
        "dynfenust_protra": 5,
    },
)
def dyneroist_protra():
    """
    Dynamic evolution of EROIst over time per PROTRA. For some technologies the EROI is computed fully endogenously and dynamically, while for other the EROIst has been set exogenously, but still it is affected by some dynamic factors (e.g., real CF).
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "NRG_TO_I": _subscript_dict["NRG_TO_I"],
            "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
        },
        ["REGIONS_9_I", "NRG_TO_I", "NRG_PROTRA_I"],
    )
    value.loc[:, :, ["PROTRA_PP_hydropower_dammed"]] = (
        zidz(
            protra_to_allocated()
            .loc[:, :, "PROTRA_PP_hydropower_dammed"]
            .reset_coords(drop=True),
            fenust_protra_eroi_exogenous()
            .loc[:, :, "PROTRA_PP_hydropower_dammed"]
            .reset_coords(drop=True),
        )
        .expand_dims({"NRG_PRO_I": ["PROTRA_PP_hydropower_dammed"]}, 2)
        .values
    )
    value.loc[:, :, ["PROTRA_PP_geothermal"]] = (
        zidz(
            protra_to_allocated()
            .loc[:, :, "PROTRA_PP_geothermal"]
            .reset_coords(drop=True),
            fenust_protra_eroi_exogenous()
            .loc[:, :, "PROTRA_PP_geothermal"]
            .reset_coords(drop=True),
        )
        .expand_dims({"NRG_PRO_I": ["PROTRA_PP_geothermal"]}, 2)
        .values
    )
    value.loc[:, :, ["PROTRA_PP_solid_bio"]] = (
        zidz(
            protra_to_allocated()
            .loc[:, :, "PROTRA_PP_solid_bio"]
            .reset_coords(drop=True),
            fenust_protra_eroi_exogenous()
            .loc[:, :, "PROTRA_PP_solid_bio"]
            .reset_coords(drop=True),
        )
        .expand_dims({"NRG_PRO_I": ["PROTRA_PP_solid_bio"]}, 2)
        .values
    )
    value.loc[:, :, ["PROTRA_PP_oceanic"]] = (
        zidz(
            protra_to_allocated()
            .loc[:, :, "PROTRA_PP_oceanic"]
            .reset_coords(drop=True),
            fenust_protra_eroi_exogenous()
            .loc[:, :, "PROTRA_PP_oceanic"]
            .reset_coords(drop=True),
        )
        .expand_dims({"NRG_PRO_I": ["PROTRA_PP_oceanic"]}, 2)
        .values
    )
    value.loc[:, :, ["PROTRA_PP_wind_onshore"]] = (
        zidz(
            protra_to_allocated()
            .loc[:, :, "PROTRA_PP_wind_onshore"]
            .reset_coords(drop=True),
            dynfenust_protra()
            .loc[:, :, "PROTRA_PP_wind_onshore"]
            .reset_coords(drop=True),
        )
        .expand_dims({"NRG_PRO_I": ["PROTRA_PP_wind_onshore"]}, 2)
        .values
    )
    value.loc[:, :, ["PROTRA_PP_wind_offshore"]] = (
        zidz(
            protra_to_allocated()
            .loc[:, :, "PROTRA_PP_wind_offshore"]
            .reset_coords(drop=True),
            dynfenust_protra()
            .loc[:, :, "PROTRA_PP_wind_offshore"]
            .reset_coords(drop=True),
        )
        .expand_dims({"NRG_PRO_I": ["PROTRA_PP_wind_offshore"]}, 2)
        .values
    )
    value.loc[:, :, ["PROTRA_PP_solar_open_space_PV"]] = (
        zidz(
            protra_to_allocated()
            .loc[:, :, "PROTRA_PP_solar_open_space_PV"]
            .reset_coords(drop=True),
            dynfenust_protra()
            .loc[:, :, "PROTRA_PP_solar_open_space_PV"]
            .reset_coords(drop=True),
        )
        .expand_dims({"NRG_PRO_I": ["PROTRA_PP_solar_open_space_PV"]}, 2)
        .values
    )
    value.loc[:, :, ["PROTRA_PP_solar_urban_PV"]] = (
        zidz(
            protra_to_allocated()
            .loc[:, :, "PROTRA_PP_solar_urban_PV"]
            .reset_coords(drop=True),
            dynfenust_protra()
            .loc[:, :, "PROTRA_PP_solar_urban_PV"]
            .reset_coords(drop=True),
        )
        .expand_dims({"NRG_PRO_I": ["PROTRA_PP_solar_urban_PV"]}, 2)
        .values
    )
    value.loc[:, :, ["PROTRA_PP_solar_CSP"]] = (
        zidz(
            protra_to_allocated()
            .loc[:, :, "PROTRA_PP_solar_CSP"]
            .reset_coords(drop=True),
            dynfenust_protra().loc[:, :, "PROTRA_PP_solar_CSP"].reset_coords(drop=True),
        )
        .expand_dims({"NRG_PRO_I": ["PROTRA_PP_solar_CSP"]}, 2)
        .values
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, :, ["PROTRA_PP_solar_CSP"]] = False
    except_subs.loc[:, :, ["PROTRA_PP_solar_urban_PV"]] = False
    except_subs.loc[:, :, ["PROTRA_PP_solar_open_space_PV"]] = False
    except_subs.loc[:, :, ["PROTRA_PP_wind_offshore"]] = False
    except_subs.loc[:, :, ["PROTRA_PP_wind_onshore"]] = False
    except_subs.loc[:, :, ["PROTRA_PP_oceanic"]] = False
    except_subs.loc[:, :, ["PROTRA_PP_solid_bio"]] = False
    except_subs.loc[:, :, ["PROTRA_PP_geothermal"]] = False
    except_subs.loc[:, :, ["PROTRA_PP_hydropower_dammed"]] = False
    value.values[except_subs.values] = 0
    return value


@component.add(
    name="dynFEnU_decom_PROTRA",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_TO_I", "NRG_PROTRA_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "share_energy_requirements_for_decomm_protra": 1,
        "dynfenust_intensity_new_protra": 1,
        "protra_capacity_decommissioning": 1,
    },
)
def dynfenu_decom_protra():
    """
    Dynamic energy used (in final terms) required to decommission PROTRA capacity which have ended their lifetime.
    """
    return (
        share_energy_requirements_for_decomm_protra()
        * dynfenust_intensity_new_protra().transpose(
            "NRG_PROTRA_I", "REGIONS_9_I", "NRG_TO_I"
        )
        * protra_capacity_decommissioning().transpose(
            "NRG_PROTRA_I", "REGIONS_9_I", "NRG_TO_I"
        )
    ).transpose("REGIONS_9_I", "NRG_TO_I", "NRG_PROTRA_I")


@component.add(
    name="dynFEnU_water_OM_PROTRA",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_TO_I", "NRG_PROTRA_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "clean_water_for_om_required_for_protra": 1,
        "embodied_fe_intensity_clean_water": 1,
        "distilled_water_for_om_required_for_protra": 1,
        "embodied_fe_intensity_distilled_water": 1,
        "matrix_unit_prefixes": 2,
    },
)
def dynfenu_water_om_protra():
    """
    Dynamic energy use (in final terms) for water for O&M of VRES per technology.
    """
    return (
        (
            clean_water_for_om_required_for_protra()
            * embodied_fe_intensity_clean_water()
            + distilled_water_for_om_required_for_protra()
            * embodied_fe_intensity_distilled_water()
        )
        * float(matrix_unit_prefixes().loc["giga", "BASE_UNIT"])
        / float(matrix_unit_prefixes().loc["exa", "mega"])
    )


@component.add(
    name="dynFEnUst_intensity_new_grids",
    units="EJ/TW",
    subscripts=["REGIONS_9_I", "NRG_TO_I", "NRG_PROTRA_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "required_embodied_fe_materials_for_new_grids": 1,
        "protra_capacity_expansion": 1,
    },
)
def dynfenust_intensity_new_grids():
    """
    Energy use (in final energy terms) per new installed capacity (TW) for overgrids by PROTRA. Dynamic variable affected by recycling policies.
    """
    return zidz(
        required_embodied_fe_materials_for_new_grids().expand_dims(
            {"NRG_TO_I": _subscript_dict["NRG_TO_I"]}, 2
        ),
        protra_capacity_expansion().transpose(
            "REGIONS_9_I", "NRG_PROTRA_I", "NRG_TO_I"
        ),
    ).transpose("REGIONS_9_I", "NRG_TO_I", "NRG_PROTRA_I")


@component.add(
    name="dynFEnUst_intensity_new_PROTRA",
    units="EJ/TW",
    subscripts=["REGIONS_9_I", "NRG_TO_I", "NRG_PROTRA_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "manufacturing_energy_intensity_protra": 1,
        "transport_materials_energy_intensity_protra": 1,
        "required_embodied_fe_materials_for_new_protra": 1,
        "protra_capacity_expansion": 1,
    },
)
def dynfenust_intensity_new_protra():
    """
    Energy use (in final energy terms) per new installed capacity (TW) for new PROTRA. Dynamic variable affected by recycling policies.
    """
    return (
        manufacturing_energy_intensity_protra()
        + transport_materials_energy_intensity_protra()
        + zidz(
            required_embodied_fe_materials_for_new_protra().expand_dims(
                {"NRG_TO_I": _subscript_dict["NRG_TO_I"]}, 2
            ),
            protra_capacity_expansion().transpose(
                "REGIONS_9_I", "NRG_PROTRA_I", "NRG_TO_I"
            ),
        ).transpose("REGIONS_9_I", "NRG_TO_I", "NRG_PROTRA_I")
    )


@component.add(
    name="dynFEnUst_intensity_OM_PROTRA",
    units="EJ/(Year*TW)",
    subscripts=["REGIONS_9_I", "NRG_TO_I", "NRG_PROTRA_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "required_embodied_fe_materials_for_om_protra": 1,
        "protra_capacity_stock": 1,
    },
)
def dynfenust_intensity_om_protra():
    """
    Energy use (in final energy terms) per new installed capacity (TW) for O&M BY PROTRA. Dynamic variable affected by recycling policies.
    """
    return zidz(
        required_embodied_fe_materials_for_om_protra().expand_dims(
            {"NRG_TO_I": _subscript_dict["NRG_TO_I"]}, 2
        ),
        protra_capacity_stock().transpose("REGIONS_9_I", "NRG_PROTRA_I", "NRG_TO_I"),
    ).transpose("REGIONS_9_I", "NRG_TO_I", "NRG_PROTRA_I")


@component.add(
    name="dynFEnUst_new_grids",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_TO_I", "NRG_PROTRA_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"dynfenust_intensity_new_grids": 1, "protra_capacity_expansion": 1},
)
def dynfenust_new_grids():
    """
    Dynamic energy used (in final terms) for the construction of new grids related to new PROTRA. Dynamic variable affected by recycling policies.
    """
    return dynfenust_intensity_new_grids() * protra_capacity_expansion()


@component.add(
    name="dynFEnUst_new_PROTRA",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_TO_I", "NRG_PROTRA_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"dynfenust_intensity_new_protra": 1, "protra_capacity_expansion": 1},
)
def dynfenust_new_protra():
    """
    Dynamic energy used (in final terms) for the construction of new PROTRA capacity. Dynamic variable affected by recycling policies.
    """
    return dynfenust_intensity_new_protra() * protra_capacity_expansion()


@component.add(
    name="dynFEnUst_OM_PROTRA",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_TO_I", "NRG_PROTRA_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "dynfenust_intensity_om_protra": 1,
        "protra_capacity_stock": 1,
        "dynfenu_water_om_protra": 1,
    },
)
def dynfenust_om_protra():
    """
    Dynamic energy used (in final terms) for the operation and maintenance of PROTRA capacity stock. Dynamic variable affected by recycling policies.
    """
    return (
        dynfenust_intensity_om_protra() * protra_capacity_stock()
        + dynfenu_water_om_protra()
    )


@component.add(
    name="dynFEnUst_PROTRA",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_TO_I", "NRG_PROTRA_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "dynfenust_new_protra": 1,
        "dynfenust_new_grids": 1,
        "dynfenu_decom_protra": 1,
        "dynfenust_om_protra": 1,
        "share_self_electricity_consumption_protra": 1,
        "protra_to_allocated": 1,
    },
)
def dynfenust_protra():
    """
    Dynamic final energy use invested (equivalent to the denominator of the EROIst for PROTRA per technology).
    """
    return (
        dynfenust_new_protra()
        + dynfenust_new_grids()
        + dynfenu_decom_protra()
        + dynfenust_om_protra()
        + protra_to_allocated() * share_self_electricity_consumption_protra()
    )


@component.add(
    name="Embodied_FE_intensity_clean_water",
    units="MJ/kg",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "embodied_pe_intensity_clean_water": 1,
        "final_to_primary_energy_by_region_until_2015": 1,
    },
)
def embodied_fe_intensity_clean_water():
    """
    Embodied final energy intensity for clean water consumption in PROTRA plants.
    """
    return (
        embodied_pe_intensity_clean_water()
        * final_to_primary_energy_by_region_until_2015()
    )


@component.add(
    name="Embodied_FE_intensity_distilled_water",
    units="MJ/kg",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "embodied_pe_intensity_distilled_water": 1,
        "final_to_primary_energy_by_region_until_2015": 1,
    },
)
def embodied_fe_intensity_distilled_water():
    """
    Embodied final energy intensity for distilled water consumption in PROTRA plants.
    """
    return (
        embodied_pe_intensity_distilled_water()
        * final_to_primary_energy_by_region_until_2015()
    )


@component.add(
    name="EPTB_dynamic",
    units="Year",
    subscripts=["REGIONS_9_I", "NRG_TO_I", "NRG_PROTRA_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"protra_lifetime": 1, "dyneroist_protra": 1},
)
def eptb_dynamic():
    """
    Energy payback time per RES for electricity generation.
    """
    return zidz(
        protra_lifetime().expand_dims({"NRG_TO_I": _subscript_dict["NRG_TO_I"]}, 2),
        dyneroist_protra().transpose("REGIONS_9_I", "NRG_PROTRA_I", "NRG_TO_I"),
    ).transpose("REGIONS_9_I", "NRG_TO_I", "NRG_PROTRA_I")


@component.add(
    name="EROIfinal_PROTRA",
    units="DMNL",
    subscripts=["REGIONS_9_I", "NRG_TO_I", "NRG_PROTRA_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "to_over_lifetime_protra": 2,
        "share_total_transmission_loss": 2,
        "share_self_electricity_consumption_protra": 1,
        "fenust_protra": 1,
        "fe_intensity_current_grids_om": 1,
        "unit_conversion_mw_tw": 1,
        "unit_conversion_mj_ej": 1,
        "protra_capacity_expansion": 1,
    },
)
def eroifinal_protra():
    """
    EROI final (over the full lifetime of the infrastructure) per RES technology for generating electricity.
    """
    return zidz(
        to_over_lifetime_protra() * (1 - share_total_transmission_loss()),
        fenust_protra()
        + (
            share_total_transmission_loss().loc[:, "TO_elec"].reset_coords(drop=True)
            * share_self_electricity_consumption_protra()
            * to_over_lifetime_protra().transpose(
                "REGIONS_9_I", "NRG_PROTRA_I", "NRG_TO_I"
            )
        ).transpose("REGIONS_9_I", "NRG_TO_I", "NRG_PROTRA_I")
        + fe_intensity_current_grids_om()
        * protra_capacity_expansion()
        * unit_conversion_mw_tw()
        / unit_conversion_mj_ej(),
    )


@component.add(
    name="EROIst_PROTRA",
    units="DMNL",
    subscripts=["REGIONS_9_I", "NRG_TO_I", "NRG_PROTRA_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"to_over_lifetime_protra": 1, "fenust_protra": 1},
)
def eroist_protra():
    """
    EROIst (over the full lifetime of the infrastructure) by PROTRA.
    """
    return zidz(to_over_lifetime_protra(), fenust_protra())


@component.add(
    name="EXOGENOUS_EROIst_PROTRA",
    units="DMNL",
    subscripts=["NRG_PROTRA_I"],
    comp_type="Data, Constant",
    comp_subtype="External, Normal",
    depends_on={
        "__external__": "_ext_data_exogenous_eroist_protra",
        "__data__": "_ext_data_exogenous_eroist_protra",
        "time": 1,
    },
)
def exogenous_eroist_protra():
    """
    Exogenous EROIst levels for those PROTRA for which we do not have computed the EROI endogenous and dynamically in the model.
    """
    value = xr.DataArray(
        np.nan, {"NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"]}, ["NRG_PROTRA_I"]
    )
    def_subs = xr.zeros_like(value, dtype=bool)
    def_subs.loc[["PROTRA_PP_hydropower_dammed"]] = True
    value.values[def_subs.values] = _ext_data_exogenous_eroist_protra(time()).values[
        def_subs.values
    ]
    def_subs = xr.zeros_like(value, dtype=bool)
    def_subs.loc[["PROTRA_PP_geothermal"]] = True
    def_subs.loc[["PROTRA_PP_solid_bio"]] = True
    def_subs.loc[["PROTRA_PP_oceanic"]] = True
    value.values[def_subs.values] = _ext_constant_exogenous_eroist_protra().values[
        def_subs.values
    ]
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[["PROTRA_PP_hydropower_dammed"]] = False
    except_subs.loc[["PROTRA_PP_geothermal"]] = False
    except_subs.loc[["PROTRA_PP_solid_bio"]] = False
    except_subs.loc[["PROTRA_PP_oceanic"]] = False
    value.values[except_subs.values] = 0
    return value


_ext_data_exogenous_eroist_protra = ExtData(
    "model_parameters/energy/energy.xlsm",
    "World",
    "time_RES_nuclear_index",
    "EROIst_initial_Hydro",
    "interpolate",
    {"NRG_PROTRA_I": ["PROTRA_PP_hydropower_dammed"]},
    _root,
    {"NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"]},
    "_ext_data_exogenous_eroist_protra",
)

_ext_constant_exogenous_eroist_protra = ExtConstant(
    "model_parameters/energy/energy.xlsm",
    "World",
    "EROIst_geot_elec",
    {"NRG_PROTRA_I": ["PROTRA_PP_geothermal"]},
    _root,
    {"NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"]},
    "_ext_constant_exogenous_eroist_protra",
)

_ext_constant_exogenous_eroist_protra.add(
    "model_parameters/energy/energy.xlsm",
    "World",
    "EROIst_solid_bioE_elec",
    {"NRG_PROTRA_I": ["PROTRA_PP_solid_bio"]},
)

_ext_constant_exogenous_eroist_protra.add(
    "model_parameters/energy/energy.xlsm",
    "World",
    "EROIst_oceanic",
    {"NRG_PROTRA_I": ["PROTRA_PP_oceanic"]},
)


@component.add(
    name="FEnU_water_OM_PTOTRA",
    units="EJ",
    subscripts=["REGIONS_9_I", "NRG_TO_I", "NRG_PROTRA_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_capacity_expansion": 1,
        "clean_water_for_om_required_for_protra": 1,
        "distilled_water_for_om_required_for_protra": 1,
        "embodied_fe_intensity_distilled_water": 1,
        "embodied_fe_intensity_clean_water": 1,
        "protra_lifetime": 1,
        "matrix_unit_prefixes": 4,
    },
)
def fenu_water_om_ptotra():
    """
    Energy use (in final terms) for water for PROTRA over all the lifetime of the infrastructure.
    """
    return (
        protra_capacity_expansion()
        * (
            clean_water_for_om_required_for_protra()
            * embodied_fe_intensity_clean_water()
            + distilled_water_for_om_required_for_protra()
            * embodied_fe_intensity_distilled_water()
        )
        * protra_lifetime()
        * (
            float(matrix_unit_prefixes().loc["tera", "mega"])
            / float(matrix_unit_prefixes().loc["giga", "BASE_UNIT"])
        )
        * (
            float(matrix_unit_prefixes().loc["giga", "BASE_UNIT"])
            / float(matrix_unit_prefixes().loc["exa", "mega"])
        )
    )


@component.add(
    name="FEnUst_intensity_PROTRA_EROI_exogenous",
    units="EJ/TW",
    subscripts=["REGIONS_9_I", "NRG_PROTRA_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cf_protra_full_load_hours": 1,
        "protra_lifetime": 1,
        "unit_conversion_wh_we": 1,
        "unit_conversion_j_wh": 1,
        "matrix_unit_prefixes": 1,
        "exogenous_eroist_protra": 1,
    },
)
def fenust_intensity_protra_eroi_exogenous():
    """
    Energy use (in final energy terms) per new installed capacity (TW) over lifetime for PROTRA for which we assume an exogenous EROIst value. We assume the same lifetime for PHS than for hydro.
    """
    return zidz(
        cf_protra_full_load_hours()
        * protra_lifetime()
        * (
            unit_conversion_j_wh()
            * unit_conversion_wh_we()
            / float(matrix_unit_prefixes().loc["exa", "tera"])
        ),
        exogenous_eroist_protra().expand_dims(
            {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, 0
        ),
    )


@component.add(
    name="FEnUst_OM_PROTRA_dynEROI",
    units="EJ",
    subscripts=["REGIONS_9_I", "NRG_TO_I", "NRG_PROTRA_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_capacity_expansion": 1,
        "dynfenust_intensity_om_protra": 1,
        "fenu_water_om_ptotra": 1,
        "protra_lifetime": 1,
    },
)
def fenust_om_protra_dyneroi():
    """
    Energy use over the lifetime for operation and maintenance of VRES for electricity generation (value W for dispatchable RES).
    """
    return (
        protra_capacity_expansion() * dynfenust_intensity_om_protra()
        + fenu_water_om_ptotra()
    ) * protra_lifetime()


@component.add(
    name="FEnUst_PROTRA",
    units="EJ",
    subscripts=["REGIONS_9_I", "NRG_TO_I", "NRG_PROTRA_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"fenust_protra_eroi_exogenous": 1, "fenust_protra_dyneroi": 5},
)
def fenust_protra():
    """
    Final energy investments over lifetime PROTRA technologies.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "NRG_TO_I": _subscript_dict["NRG_TO_I"],
            "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
        },
        ["REGIONS_9_I", "NRG_TO_I", "NRG_PROTRA_I"],
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, :, ["PROTRA_PP_solar_CSP"]] = False
    except_subs.loc[:, :, ["PROTRA_PP_solar_open_space_PV"]] = False
    except_subs.loc[:, :, ["PROTRA_PP_solar_urban_PV"]] = False
    except_subs.loc[:, :, ["PROTRA_PP_wind_onshore"]] = False
    except_subs.loc[:, :, ["PROTRA_PP_wind_offshore"]] = False
    value.values[except_subs.values] = fenust_protra_eroi_exogenous().values[
        except_subs.values
    ]
    value.loc[:, :, ["PROTRA_PP_solar_CSP"]] = (
        fenust_protra_dyneroi()
        .loc[:, :, "PROTRA_PP_solar_CSP"]
        .reset_coords(drop=True)
        .expand_dims({"NRG_PRO_I": ["PROTRA_PP_solar_CSP"]}, 2)
        .values
    )
    value.loc[:, :, ["PROTRA_PP_solar_open_space_PV"]] = (
        fenust_protra_dyneroi()
        .loc[:, :, "PROTRA_PP_solar_open_space_PV"]
        .reset_coords(drop=True)
        .expand_dims({"NRG_PRO_I": ["PROTRA_PP_solar_open_space_PV"]}, 2)
        .values
    )
    value.loc[:, :, ["PROTRA_PP_solar_urban_PV"]] = (
        fenust_protra_dyneroi()
        .loc[:, :, "PROTRA_PP_solar_urban_PV"]
        .reset_coords(drop=True)
        .expand_dims({"NRG_PRO_I": ["PROTRA_PP_solar_urban_PV"]}, 2)
        .values
    )
    value.loc[:, :, ["PROTRA_PP_wind_onshore"]] = (
        fenust_protra_dyneroi()
        .loc[:, :, "PROTRA_PP_wind_onshore"]
        .reset_coords(drop=True)
        .expand_dims({"NRG_PRO_I": ["PROTRA_PP_wind_onshore"]}, 2)
        .values
    )
    value.loc[:, :, ["PROTRA_PP_wind_offshore"]] = (
        fenust_protra_dyneroi()
        .loc[:, :, "PROTRA_PP_wind_offshore"]
        .reset_coords(drop=True)
        .expand_dims({"NRG_PRO_I": ["PROTRA_PP_wind_offshore"]}, 2)
        .values
    )
    return value


@component.add(
    name="FEnUst_PROTRA_dynEROI",
    units="EJ",
    subscripts=["REGIONS_9_I", "NRG_TO_I", "NRG_PROTRA_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "dynfenust_new_protra": 1,
        "share_energy_requirements_for_decomm_protra": 1,
        "fenust_om_protra_dyneroi": 1,
        "to_over_lifetime_protra": 1,
        "share_self_electricity_consumption_protra": 1,
    },
)
def fenust_protra_dyneroi():
    """
    Energy use (in final terms) invested over lifetime per PROTRA (including installation of new capacity and O&M).
    """
    return (
        dynfenust_new_protra() * (1 + share_energy_requirements_for_decomm_protra())
        + fenust_om_protra_dyneroi()
        + to_over_lifetime_protra() * share_self_electricity_consumption_protra()
    )


@component.add(
    name="FEnUst_PROTRA_EROI_exogenous",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_TO_I", "NRG_PROTRA_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "fenust_intensity_protra_eroi_exogenous": 1,
        "protra_capacity_expansion": 1,
    },
)
def fenust_protra_eroi_exogenous():
    """
    Final energy use invested over lifetime for those PROTRA for which the EROI is set exogenously.
    """
    return (
        fenust_intensity_protra_eroi_exogenous()
        * protra_capacity_expansion().transpose(
            "REGIONS_9_I", "NRG_PROTRA_I", "NRG_TO_I"
        )
    ).transpose("REGIONS_9_I", "NRG_TO_I", "NRG_PROTRA_I")


@component.add(
    name="manufacturing_energy_intensity_for_PV_panels",
    units="EJ/TW",
    subscripts=[
        "REGIONS_9_I",
        "NRG_TO_I",
        "PROTRA_PP_SOLAR_PV_I",
        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "fe_intensity_manufacturing_pv_panels": 2,
        "share_new_pv_subtechn_land": 1,
        "unit_conversion_mw_tw": 2,
        "unit_conversion_mj_ej": 2,
        "share_new_pv_subtechn_urban": 1,
    },
)
def manufacturing_energy_intensity_for_pv_panels():
    """
    Energy spent for the manufacturing of PV panels
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "NRG_TO_I": _subscript_dict["NRG_TO_I"],
            "PROTRA_PP_SOLAR_PV_I": _subscript_dict["PROTRA_PP_SOLAR_PV_I"],
            "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": _subscript_dict[
                "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"
            ],
        },
        [
            "REGIONS_9_I",
            "NRG_TO_I",
            "PROTRA_PP_SOLAR_PV_I",
            "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I",
        ],
    )
    value.loc[:, :, ["PROTRA_PP_solar_open_space_PV"], :] = (
        (
            sum(
                fe_intensity_manufacturing_pv_panels().rename(
                    {
                        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!"
                    }
                )
                * share_new_pv_subtechn_land().rename(
                    {
                        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!"
                    }
                ),
                dim=["PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!"],
            )
            * unit_conversion_mw_tw()
            / unit_conversion_mj_ej()
        )
        .expand_dims({"NRG_TO_I": _subscript_dict["NRG_TO_I"]}, 1)
        .expand_dims({"NRG_PRO_I": ["PROTRA_PP_solar_open_space_PV"]}, 2)
        .expand_dims(
            {
                "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": _subscript_dict[
                    "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"
                ]
            },
            3,
        )
        .values
    )
    value.loc[:, :, ["PROTRA_PP_solar_urban_PV"], :] = (
        (
            sum(
                fe_intensity_manufacturing_pv_panels().rename(
                    {
                        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!"
                    }
                )
                * share_new_pv_subtechn_urban().rename(
                    {
                        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!"
                    }
                ),
                dim=["PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!"],
            )
            * unit_conversion_mw_tw()
            / unit_conversion_mj_ej()
        )
        .expand_dims({"NRG_TO_I": _subscript_dict["NRG_TO_I"]}, 1)
        .expand_dims({"NRG_PRO_I": ["PROTRA_PP_solar_urban_PV"]}, 2)
        .expand_dims(
            {
                "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": _subscript_dict[
                    "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"
                ]
            },
            3,
        )
        .values
    )
    return value


@component.add(
    name="manufacturing_energy_intensity_PROTRA",
    units="EJ/TW",
    subscripts=["REGIONS_9_I", "NRG_TO_I", "NRG_PROTRA_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={"manufacturing_energy_intensity_for_pv_panels": 1},
)
def manufacturing_energy_intensity_protra():
    """
    Manufacturing energy intensity (FE) for all PROTRA.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "NRG_TO_I": _subscript_dict["NRG_TO_I"],
            "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
        },
        ["REGIONS_9_I", "NRG_TO_I", "NRG_PROTRA_I"],
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, :, _subscript_dict["PROTRA_PP_SOLAR_PV_I"]] = False
    value.values[except_subs.values] = 0
    value.loc[:, :, _subscript_dict["PROTRA_PP_SOLAR_PV_I"]] = sum(
        manufacturing_energy_intensity_for_pv_panels().rename(
            {
                "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!"
            }
        ),
        dim=["PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!"],
    ).values
    return value


@component.add(
    name="required_embodied_FE_materials_for_new_grids",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_PROTRA_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"required_embodied_fe_per_material_for_new_grids": 1},
)
def required_embodied_fe_materials_for_new_grids():
    """
    Required embodied final energy of total material consumption for overgrids.
    """
    return sum(
        required_embodied_fe_per_material_for_new_grids().rename(
            {"MATERIALS_I": "MATERIALS_I!"}
        ),
        dim=["MATERIALS_I!"],
    )


@component.add(
    name="required_embodied_FE_materials_for_new_PROTRA",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_PROTRA_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"required_embodied_fe_per_material_for_new_protra": 1},
)
def required_embodied_fe_materials_for_new_protra():
    """
    Required embodied final energy of total material consumption for new PROTRA
    """
    return sum(
        required_embodied_fe_per_material_for_new_protra().rename(
            {"MATERIALS_I": "MATERIALS_I!"}
        ),
        dim=["MATERIALS_I!"],
    )


@component.add(
    name="required_embodied_FE_materials_for_OM_PROTRA",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_PROTRA_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"required_embodied_fe_per_material_for_om_new_protra": 1},
)
def required_embodied_fe_materials_for_om_protra():
    """
    Required embodied final energy of total material consumption for O&M of PROTRA.
    """
    return sum(
        required_embodied_fe_per_material_for_om_new_protra().rename(
            {"MATERIALS_I": "MATERIALS_I!"}
        ),
        dim=["MATERIALS_I!"],
    )


@component.add(
    name="required_embodied_FE_materials_for_PROTRA",
    units="EJ/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "required_embodied_fe_materials_for_new_protra": 1,
        "required_embodied_fe_materials_for_om_protra": 1,
    },
)
def required_embodied_fe_materials_for_protra():
    """
    Required embodied final energy of total material consumption for PROTRA.
    """
    return sum(
        required_embodied_fe_materials_for_new_protra().rename(
            {"NRG_PROTRA_I": "NRG_PROTRA_I!"}
        ),
        dim=["NRG_PROTRA_I!"],
    ) + sum(
        required_embodied_fe_materials_for_om_protra().rename(
            {"NRG_PROTRA_I": "NRG_PROTRA_I!"}
        ),
        dim=["NRG_PROTRA_I!"],
    )


@component.add(
    name="required_embodied_FE_per_material_for_new_grids",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_PROTRA_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_energy": 2,
        "unit_conversion_mj_ej": 2,
        "unit_conversion_kg_mt": 2,
        "materials_required_for_new_grids_by_protra": 2,
        "embodied_fe_intensity_materials": 2,
    },
)
def required_embodied_fe_per_material_for_new_grids():
    """
    Required embodied final energy of material consumption for overgrids.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
            "MATERIALS_I": _subscript_dict["MATERIALS_I"],
        },
        ["REGIONS_9_I", "NRG_PROTRA_I", "MATERIALS_I"],
    )
    value.loc[_subscript_dict["REGIONS_8_I"], :, :] = if_then_else(
        switch_energy() == 0,
        lambda: xr.DataArray(
            0,
            {
                "REGIONS_8_I": _subscript_dict["REGIONS_8_I"],
                "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
                "MATERIALS_I": _subscript_dict["MATERIALS_I"],
            },
            ["REGIONS_8_I", "NRG_PROTRA_I", "MATERIALS_I"],
        ),
        lambda: materials_required_for_new_grids_by_protra()
        .loc[_subscript_dict["REGIONS_8_I"], :, :]
        .rename({"REGIONS_9_I": "REGIONS_8_I"})
        * embodied_fe_intensity_materials()
        .loc[_subscript_dict["REGIONS_8_I"], :]
        .rename({"REGIONS_9_I": "REGIONS_8_I"})
        * (unit_conversion_kg_mt() / unit_conversion_mj_ej()),
    ).values
    value.loc[["EU27"], :, :] = (
        if_then_else(
            switch_energy() == 0,
            lambda: xr.DataArray(
                0,
                {
                    "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
                    "MATERIALS_I": _subscript_dict["MATERIALS_I"],
                },
                ["NRG_PROTRA_I", "MATERIALS_I"],
            ),
            lambda: materials_required_for_new_grids_by_protra()
            .loc["EU27", :, :]
            .reset_coords(drop=True)
            * embodied_fe_intensity_materials().loc["EU27", :].reset_coords(drop=True)
            * (unit_conversion_kg_mt() / unit_conversion_mj_ej()),
        )
        .expand_dims({"REGIONS_36_I": ["EU27"]}, 0)
        .values
    )
    return value


@component.add(
    name="required_embodied_FE_per_material_for_new_PROTRA",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_PROTRA_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_energy": 6,
        "unit_conversion_mj_ej": 6,
        "unit_conversion_kg_mt": 6,
        "embodied_fe_intensity_materials": 6,
        "materials_required_for_new_protra": 6,
        "scrap_rate": 8,
        "machining_rate_pv": 4,
    },
)
def required_embodied_fe_per_material_for_new_protra():
    """
    Required embodied final energy of material consumption for new PROTRA.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
            "MATERIALS_I": _subscript_dict["MATERIALS_I"],
        },
        ["REGIONS_9_I", "NRG_PROTRA_I", "MATERIALS_I"],
    )
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[_subscript_dict["REGIONS_8_I"], :, :] = True
    except_subs.loc[
        _subscript_dict["REGIONS_8_I"], ["PROTRA_PP_solar_open_space_PV"], :
    ] = False
    except_subs.loc[
        _subscript_dict["REGIONS_8_I"], ["PROTRA_PP_solar_urban_PV"], :
    ] = False
    value.values[except_subs.values] = if_then_else(
        switch_energy() == 0,
        lambda: xr.DataArray(
            0,
            {
                "REGIONS_8_I": _subscript_dict["REGIONS_8_I"],
                "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
                "MATERIALS_I": _subscript_dict["MATERIALS_I"],
            },
            ["REGIONS_8_I", "NRG_PROTRA_I", "MATERIALS_I"],
        ),
        lambda: materials_required_for_new_protra()
        .loc[_subscript_dict["REGIONS_8_I"], :, :]
        .rename({"REGIONS_9_I": "REGIONS_8_I"})
        * embodied_fe_intensity_materials()
        .loc[_subscript_dict["REGIONS_8_I"], :]
        .rename({"REGIONS_9_I": "REGIONS_8_I"})
        * (unit_conversion_kg_mt() / unit_conversion_mj_ej()),
    ).values[except_subs.loc[_subscript_dict["REGIONS_8_I"], :, :].values]
    value.loc[_subscript_dict["REGIONS_8_I"], ["PROTRA_PP_solar_open_space_PV"], :] = (
        if_then_else(
            switch_energy() == 0,
            lambda: xr.DataArray(
                0,
                {
                    "REGIONS_8_I": _subscript_dict["REGIONS_8_I"],
                    "MATERIALS_I": _subscript_dict["MATERIALS_I"],
                },
                ["REGIONS_8_I", "MATERIALS_I"],
            ),
            lambda: materials_required_for_new_protra()
            .loc[_subscript_dict["REGIONS_8_I"], "PROTRA_PP_solar_open_space_PV", :]
            .reset_coords(drop=True)
            .rename({"REGIONS_9_I": "REGIONS_8_I"})
            * embodied_fe_intensity_materials()
            .loc[_subscript_dict["REGIONS_8_I"], :]
            .rename({"REGIONS_9_I": "REGIONS_8_I"})
            * (unit_conversion_kg_mt() / unit_conversion_mj_ej())
            / ((1 + scrap_rate()) * (1 + machining_rate_pv() + scrap_rate())),
        )
        .expand_dims({"NRG_PRO_I": ["PROTRA_PP_solar_open_space_PV"]}, 1)
        .values
    )
    value.loc[_subscript_dict["REGIONS_8_I"], ["PROTRA_PP_solar_urban_PV"], :] = (
        if_then_else(
            switch_energy() == 0,
            lambda: xr.DataArray(
                0,
                {
                    "REGIONS_8_I": _subscript_dict["REGIONS_8_I"],
                    "MATERIALS_I": _subscript_dict["MATERIALS_I"],
                },
                ["REGIONS_8_I", "MATERIALS_I"],
            ),
            lambda: materials_required_for_new_protra()
            .loc[_subscript_dict["REGIONS_8_I"], "PROTRA_PP_solar_urban_PV", :]
            .reset_coords(drop=True)
            .rename({"REGIONS_9_I": "REGIONS_8_I"})
            * embodied_fe_intensity_materials()
            .loc[_subscript_dict["REGIONS_8_I"], :]
            .rename({"REGIONS_9_I": "REGIONS_8_I"})
            * (unit_conversion_kg_mt() / unit_conversion_mj_ej())
            / ((1 + scrap_rate()) * (1 + machining_rate_pv() + scrap_rate())),
        )
        .expand_dims({"NRG_PRO_I": ["PROTRA_PP_solar_urban_PV"]}, 1)
        .values
    )
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[["EU27"], :, :] = True
    except_subs.loc[["EU27"], ["PROTRA_PP_solar_open_space_PV"], :] = False
    except_subs.loc[["EU27"], ["PROTRA_PP_solar_urban_PV"], :] = False
    value.values[except_subs.values] = (
        if_then_else(
            switch_energy() == 0,
            lambda: xr.DataArray(
                0,
                {
                    "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
                    "MATERIALS_I": _subscript_dict["MATERIALS_I"],
                },
                ["NRG_PROTRA_I", "MATERIALS_I"],
            ),
            lambda: materials_required_for_new_protra()
            .loc["EU27", :, :]
            .reset_coords(drop=True)
            * embodied_fe_intensity_materials().loc["EU27", :].reset_coords(drop=True)
            * (unit_conversion_kg_mt() / unit_conversion_mj_ej()),
        )
        .expand_dims({"REGIONS_36_I": ["EU27"]}, 0)
        .values[except_subs.loc[["EU27"], :, :].values]
    )
    value.loc[["EU27"], ["PROTRA_PP_solar_open_space_PV"], :] = (
        if_then_else(
            switch_energy() == 0,
            lambda: xr.DataArray(
                0, {"MATERIALS_I": _subscript_dict["MATERIALS_I"]}, ["MATERIALS_I"]
            ),
            lambda: materials_required_for_new_protra()
            .loc["EU27", "PROTRA_PP_solar_open_space_PV", :]
            .reset_coords(drop=True)
            * embodied_fe_intensity_materials().loc["EU27", :].reset_coords(drop=True)
            * (unit_conversion_kg_mt() / unit_conversion_mj_ej())
            / ((1 + scrap_rate()) * (1 + machining_rate_pv() + scrap_rate())),
        )
        .expand_dims({"REGIONS_36_I": ["EU27"]}, 0)
        .expand_dims({"NRG_PRO_I": ["PROTRA_PP_solar_open_space_PV"]}, 1)
        .values
    )
    value.loc[["EU27"], ["PROTRA_PP_solar_urban_PV"], :] = (
        if_then_else(
            switch_energy() == 0,
            lambda: xr.DataArray(
                0, {"MATERIALS_I": _subscript_dict["MATERIALS_I"]}, ["MATERIALS_I"]
            ),
            lambda: materials_required_for_new_protra()
            .loc["EU27", "PROTRA_PP_solar_urban_PV", :]
            .reset_coords(drop=True)
            * embodied_fe_intensity_materials().loc["EU27", :].reset_coords(drop=True)
            * (unit_conversion_kg_mt() / unit_conversion_mj_ej())
            / ((1 + scrap_rate()) * (1 + machining_rate_pv() + scrap_rate())),
        )
        .expand_dims({"REGIONS_36_I": ["EU27"]}, 0)
        .expand_dims({"NRG_PRO_I": ["PROTRA_PP_solar_urban_PV"]}, 1)
        .values
    )
    return value


@component.add(
    name="required_embodied_FE_per_material_for_OM_new_PROTRA",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_PROTRA_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_energy": 2,
        "unit_conversion_mj_ej": 2,
        "unit_conversion_kg_mt": 2,
        "materials_required_for_om_protra": 2,
        "embodied_fe_intensity_materials": 2,
    },
)
def required_embodied_fe_per_material_for_om_new_protra():
    """
    Required embodied final energy of material consumption for O&M new RES elec.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
            "MATERIALS_I": _subscript_dict["MATERIALS_I"],
        },
        ["REGIONS_9_I", "NRG_PROTRA_I", "MATERIALS_I"],
    )
    value.loc[_subscript_dict["REGIONS_8_I"], :, :] = if_then_else(
        switch_energy() == 0,
        lambda: xr.DataArray(
            0,
            {
                "REGIONS_8_I": _subscript_dict["REGIONS_8_I"],
                "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
                "MATERIALS_I": _subscript_dict["MATERIALS_I"],
            },
            ["REGIONS_8_I", "NRG_PROTRA_I", "MATERIALS_I"],
        ),
        lambda: materials_required_for_om_protra()
        .loc[_subscript_dict["REGIONS_8_I"], :, :]
        .rename({"REGIONS_9_I": "REGIONS_8_I"})
        * embodied_fe_intensity_materials()
        .loc[_subscript_dict["REGIONS_8_I"], :]
        .rename({"REGIONS_9_I": "REGIONS_8_I"})
        * (unit_conversion_kg_mt() / unit_conversion_mj_ej()),
    ).values
    value.loc[["EU27"], :, :] = (
        if_then_else(
            switch_energy() == 0,
            lambda: xr.DataArray(
                0,
                {
                    "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
                    "MATERIALS_I": _subscript_dict["MATERIALS_I"],
                },
                ["NRG_PROTRA_I", "MATERIALS_I"],
            ),
            lambda: materials_required_for_om_protra()
            .loc["EU27", :, :]
            .reset_coords(drop=True)
            * embodied_fe_intensity_materials().loc["EU27", :].reset_coords(drop=True)
            * (unit_conversion_kg_mt() / unit_conversion_mj_ej()),
        )
        .expand_dims({"REGIONS_36_I": ["EU27"]}, 0)
        .values
    )
    return value


@component.add(
    name="share_FEnU_overgrids_over_total_FEnU_PROTRA",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"dynfenust_new_grids": 1, "total_dynfenu_protra": 1},
)
def share_fenu_overgrids_over_total_fenu_protra():
    """
    Share new rids over total FEnU RES for PROTRA.
    """
    return zidz(
        sum(
            dynfenust_new_grids().rename(
                {"NRG_TO_I": "NRG_TO_I!", "NRG_PROTRA_I": "NRG_PROTRA_I!"}
            ),
            dim=["NRG_TO_I!", "NRG_PROTRA_I!"],
        ),
        total_dynfenu_protra(),
    )


@component.add(
    name="TO_over_lifetime_PROTRA",
    units="EJ",
    subscripts=["REGIONS_9_I", "NRG_TO_I", "NRG_PROTRA_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cf_protra": 1,
        "protra_capacity_expansion": 1,
        "unit_conversion_wh_we": 1,
        "protra_lifetime": 1,
        "matrix_unit_prefixes": 1,
        "unit_conversion_j_wh": 1,
    },
)
def to_over_lifetime_protra():
    """
    Total electricity output expected to be generated over the full operation of the infrastructure of the new PROTRA capacity installed, assuming current performance factors.
    """
    return (
        cf_protra()
        * protra_capacity_expansion()
        * (1 / (1 / unit_conversion_wh_we()))
        * protra_lifetime()
        * (unit_conversion_j_wh() / float(matrix_unit_prefixes().loc["exa", "tera"]))
    )


@component.add(
    name="Total_blue_water_for_OM_required_by_PROTRA",
    units="Mt",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "clean_water_for_om_required_for_protra": 1,
        "distilled_water_for_om_required_for_protra": 1,
    },
)
def total_blue_water_for_om_required_by_protra():
    """
    Total blue water requirements for PROTRA.
    """
    return sum(
        clean_water_for_om_required_for_protra().rename(
            {"NRG_TO_I": "NRG_TO_I!", "NRG_PROTRA_I": "NRG_PROTRA_I!"}
        ),
        dim=["NRG_TO_I!", "NRG_PROTRA_I!"],
    ) + sum(
        distilled_water_for_om_required_for_protra().rename(
            {"NRG_TO_I": "NRG_TO_I!", "NRG_PROTRA_I": "NRG_PROTRA_I!"}
        ),
        dim=["NRG_TO_I!", "NRG_PROTRA_I!"],
    )


@component.add(
    name="Total_dynFEnU_PROTRA",
    units="EJ/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"dynfenust_protra": 1},
)
def total_dynfenu_protra():
    """
    Dynamic final energy use invested for all PROTRA.
    """
    return sum(
        dynfenust_protra().rename(
            {"NRG_TO_I": "NRG_TO_I!", "NRG_PROTRA_I": "NRG_PROTRA_I!"}
        ),
        dim=["NRG_TO_I!", "NRG_PROTRA_I!"],
    )


@component.add(
    name="Total_FEnUst_PROTRA_EROI_exogenous",
    units="EJ/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"fenust_protra_eroi_exogenous": 1},
)
def total_fenust_protra_eroi_exogenous():
    """
    Final energy use invested over lifetime for those PROTRA for which the EROI is set exogenously.
    """
    return sum(
        fenust_protra_eroi_exogenous().rename(
            {"NRG_TO_I": "NRG_TO_I!", "NRG_PROTRA_I": "NRG_PROTRA_I!"}
        ),
        dim=["NRG_TO_I!", "NRG_PROTRA_I!"],
    )


@component.add(
    name="transport_materials_energy_intensity_PROTRA",
    units="EJ/TW",
    subscripts=["NRG_TO_I", "NRG_PROTRA_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "transport_materials_fe_intensity_pv_technologies": 1,
        "unit_conversion_mw_tw": 1,
        "unit_conversion_mj_ej": 1,
    },
)
def transport_materials_energy_intensity_protra():
    """
    Energy for transporting materials for all PROTRA (round-trip).
    """
    value = xr.DataArray(
        np.nan,
        {
            "NRG_TO_I": _subscript_dict["NRG_TO_I"],
            "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
        },
        ["NRG_TO_I", "NRG_PROTRA_I"],
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[["TO_elec"], _subscript_dict["PROTRA_PP_SOLAR_PV_I"]] = False
    value.values[except_subs.values] = 0
    value.loc[["TO_elec"], _subscript_dict["PROTRA_PP_SOLAR_PV_I"]] = (
        (
            2
            * sum(
                transport_materials_fe_intensity_pv_technologies().rename(
                    {
                        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!"
                    }
                ),
                dim=["PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!"],
            )
            * unit_conversion_mw_tw()
            / unit_conversion_mj_ej()
        )
        .expand_dims({"NRG_COMMODITIES_I": ["TO_elec"]}, 0)
        .values
    )
    return value
