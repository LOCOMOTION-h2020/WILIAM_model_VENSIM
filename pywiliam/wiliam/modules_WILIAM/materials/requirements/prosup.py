"""
Module materials.requirements.prosup
Translated using PySD version 3.10.0
"""


@component.add(
    name="cumulated_materials_extracted_for_all_PROSUP_from_2015",
    units="Mt",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"cumulated_materials_extracted_for_prosup_from_2015": 1},
)
def cumulated_materials_extracted_for_all_prosup_from_2015():
    """
    Cumulatd materials to extrac for all PROSUP technologies from 2015.
    """
    return cumulated_materials_extracted_for_prosup_from_2015()


@component.add(
    name="cumulated_materials_extracted_for_PROSUP_from_2015",
    units="Mt",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_cumulated_materials_extracted_for_prosup_from_2015": 1},
    other_deps={
        "_integ_cumulated_materials_extracted_for_prosup_from_2015": {
            "initial": {},
            "step": {"materials_extracted_for_prosup_from_2015": 1},
        }
    },
)
def cumulated_materials_extracted_for_prosup_from_2015():
    """
    Cumulative materials to be mined for PROSUP technologies.
    """
    return _integ_cumulated_materials_extracted_for_prosup_from_2015()


_integ_cumulated_materials_extracted_for_prosup_from_2015 = Integ(
    lambda: materials_extracted_for_prosup_from_2015(),
    lambda: xr.DataArray(
        0,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "MATERIALS_I": _subscript_dict["MATERIALS_I"],
        },
        ["REGIONS_9_I", "MATERIALS_I"],
    ),
    "_integ_cumulated_materials_extracted_for_prosup_from_2015",
)


@component.add(
    name="cumulated_materials_extracted_for_PROSUP_from_initial_year",
    units="Mt",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_cumulated_materials_extracted_for_prosup_from_initial_year": 1},
    other_deps={
        "_integ_cumulated_materials_extracted_for_prosup_from_initial_year": {
            "initial": {},
            "step": {"materials_extracted_for_prosup": 1},
        }
    },
)
def cumulated_materials_extracted_for_prosup_from_initial_year():
    """
    Cumulative materials to be mined for PROSUP.
    """
    return _integ_cumulated_materials_extracted_for_prosup_from_initial_year()


_integ_cumulated_materials_extracted_for_prosup_from_initial_year = Integ(
    lambda: materials_extracted_for_prosup(),
    lambda: xr.DataArray(
        0,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "MATERIALS_I": _subscript_dict["MATERIALS_I"],
        },
        ["REGIONS_9_I", "MATERIALS_I"],
    ),
    "_integ_cumulated_materials_extracted_for_prosup_from_initial_year",
)


@component.add(
    name="cumulated_materials_requirements_for_PROSUP_from_initial_year",
    units="Mt",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={
        "_integ_cumulated_materials_requirements_for_prosup_from_initial_year": 1
    },
    other_deps={
        "_integ_cumulated_materials_requirements_for_prosup_from_initial_year": {
            "initial": {},
            "step": {"materials_required_for_prosup": 1},
        }
    },
)
def cumulated_materials_requirements_for_prosup_from_initial_year():
    """
    Total cumulative materials requirements for PROSUP technologies.
    """
    return _integ_cumulated_materials_requirements_for_prosup_from_initial_year()


_integ_cumulated_materials_requirements_for_prosup_from_initial_year = Integ(
    lambda: materials_required_for_prosup(),
    lambda: xr.DataArray(
        0,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "MATERIALS_I": _subscript_dict["MATERIALS_I"],
        },
        ["REGIONS_9_I", "MATERIALS_I"],
    ),
    "_integ_cumulated_materials_requirements_for_prosup_from_initial_year",
)


@component.add(
    name="MATERIAL_INTENSITY_NEW_CAPACITY_OVERGRIDS",
    units="kg/MW",
    subscripts=["MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "material_intensity_new_capacity_overgrid_high_power": 1,
        "material_intensity_new_capacity_hvdcs": 1,
        "switch_endogenous_account_materials_for_overgrids": 1,
    },
)
def material_intensity_new_capacity_overgrids():
    """
    Materials for overgrids (high power & HVDC) per new RES elc variable capacity.
    """
    return (
        material_intensity_new_capacity_overgrid_high_power()
        + material_intensity_new_capacity_hvdcs()
    ) * switch_endogenous_account_materials_for_overgrids()


@component.add(
    name="Materials_extracted_for_PROSUP",
    units="Mt/Year",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "materials_required_for_prosup": 1,
        "eol_recycling_rates_minerals_alt_techn": 1,
    },
)
def materials_extracted_for_prosup():
    """
    Annual materials to be mined for PROSUP.
    """
    return materials_required_for_prosup() * (
        1 - eol_recycling_rates_minerals_alt_techn()
    )


@component.add(
    name="Materials_extracted_for_PROSUP_from_2015",
    units="Mt/Year",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "materials_extracted_for_prosup": 1},
)
def materials_extracted_for_prosup_from_2015():
    """
    Annual materials to be mined for PROSUP from 2015.
    """
    return if_then_else(
        time() < 2015,
        lambda: xr.DataArray(
            0,
            {
                "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                "MATERIALS_I": _subscript_dict["MATERIALS_I"],
            },
            ["REGIONS_9_I", "MATERIALS_I"],
        ),
        lambda: materials_extracted_for_prosup(),
    )


@component.add(
    name="materials_required_for_new_grids_by_PROTRA",
    units="Mt/Year",
    subscripts=["REGIONS_9_I", "NRG_PROTRA_I", "MATERIALS_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_materials": 5,
        "material_intensity_new_capacity_overgrids": 10,
        "unit_conversion_kg_mt": 10,
        "initial_protra_capacity_expansion": 5,
        "unit_conversion_mw_tw": 10,
        "protra_capacity_expansion": 5,
    },
)
def materials_required_for_new_grids_by_protra():
    """
    Annual materials required for the installation of new grids.
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
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, ["PROTRA_PP_solar_CSP"], :] = False
    except_subs.loc[:, ["PROTRA_PP_solar_open_space_PV"], :] = False
    except_subs.loc[:, ["PROTRA_PP_solar_urban_PV"], :] = False
    except_subs.loc[:, ["PROTRA_PP_wind_offshore"], :] = False
    except_subs.loc[:, ["PROTRA_PP_wind_onshore"], :] = False
    value.values[except_subs.values] = 0
    value.loc[:, ["PROTRA_PP_solar_CSP"], :] = (
        if_then_else(
            switch_materials() == 0,
            lambda: sum(
                initial_protra_capacity_expansion()
                .loc[:, :, "PROTRA_PP_solar_CSP"]
                .reset_coords(drop=True)
                .rename({"NRG_TO_I": "NRG_TO_I!"}),
                dim=["NRG_TO_I!"],
            )
            * material_intensity_new_capacity_overgrids()
            * unit_conversion_mw_tw()
            / unit_conversion_kg_mt(),
            lambda: sum(
                protra_capacity_expansion()
                .loc[:, :, "PROTRA_PP_solar_CSP"]
                .reset_coords(drop=True)
                .rename({"NRG_TO_I": "NRG_TO_I!"}),
                dim=["NRG_TO_I!"],
            )
            * material_intensity_new_capacity_overgrids()
            * unit_conversion_mw_tw()
            / unit_conversion_kg_mt(),
        )
        .expand_dims({"NRG_PRO_I": ["PROTRA_PP_solar_CSP"]}, 1)
        .values
    )
    value.loc[:, ["PROTRA_PP_solar_open_space_PV"], :] = (
        if_then_else(
            switch_materials() == 0,
            lambda: sum(
                initial_protra_capacity_expansion()
                .loc[:, :, "PROTRA_PP_solar_open_space_PV"]
                .reset_coords(drop=True)
                .rename({"NRG_TO_I": "NRG_TO_I!"}),
                dim=["NRG_TO_I!"],
            )
            * material_intensity_new_capacity_overgrids()
            * unit_conversion_mw_tw()
            / unit_conversion_kg_mt(),
            lambda: sum(
                protra_capacity_expansion()
                .loc[:, :, "PROTRA_PP_solar_open_space_PV"]
                .reset_coords(drop=True)
                .rename({"NRG_TO_I": "NRG_TO_I!"}),
                dim=["NRG_TO_I!"],
            )
            * material_intensity_new_capacity_overgrids()
            * unit_conversion_mw_tw()
            / unit_conversion_kg_mt(),
        )
        .expand_dims({"NRG_PRO_I": ["PROTRA_PP_solar_open_space_PV"]}, 1)
        .values
    )
    value.loc[:, ["PROTRA_PP_solar_urban_PV"], :] = (
        if_then_else(
            switch_materials() == 0,
            lambda: sum(
                initial_protra_capacity_expansion()
                .loc[:, :, "PROTRA_PP_solar_urban_PV"]
                .reset_coords(drop=True)
                .rename({"NRG_TO_I": "NRG_TO_I!"}),
                dim=["NRG_TO_I!"],
            )
            * material_intensity_new_capacity_overgrids()
            * unit_conversion_mw_tw()
            / unit_conversion_kg_mt(),
            lambda: sum(
                protra_capacity_expansion()
                .loc[:, :, "PROTRA_PP_solar_urban_PV"]
                .reset_coords(drop=True)
                .rename({"NRG_TO_I": "NRG_TO_I!"}),
                dim=["NRG_TO_I!"],
            )
            * material_intensity_new_capacity_overgrids()
            * unit_conversion_mw_tw()
            / unit_conversion_kg_mt(),
        )
        .expand_dims({"NRG_PRO_I": ["PROTRA_PP_solar_urban_PV"]}, 1)
        .values
    )
    value.loc[:, ["PROTRA_PP_wind_offshore"], :] = (
        if_then_else(
            switch_materials() == 0,
            lambda: sum(
                initial_protra_capacity_expansion()
                .loc[:, :, "PROTRA_PP_wind_offshore"]
                .reset_coords(drop=True)
                .rename({"NRG_TO_I": "NRG_TO_I!"}),
                dim=["NRG_TO_I!"],
            )
            * material_intensity_new_capacity_overgrids()
            * unit_conversion_mw_tw()
            / unit_conversion_kg_mt(),
            lambda: sum(
                protra_capacity_expansion()
                .loc[:, :, "PROTRA_PP_wind_offshore"]
                .reset_coords(drop=True)
                .rename({"NRG_TO_I": "NRG_TO_I!"}),
                dim=["NRG_TO_I!"],
            )
            * material_intensity_new_capacity_overgrids()
            * unit_conversion_mw_tw()
            / unit_conversion_kg_mt(),
        )
        .expand_dims({"NRG_PRO_I": ["PROTRA_PP_wind_offshore"]}, 1)
        .values
    )
    value.loc[:, ["PROTRA_PP_wind_onshore"], :] = (
        if_then_else(
            switch_materials() == 0,
            lambda: sum(
                initial_protra_capacity_expansion()
                .loc[:, :, "PROTRA_PP_wind_onshore"]
                .reset_coords(drop=True)
                .rename({"NRG_TO_I": "NRG_TO_I!"}),
                dim=["NRG_TO_I!"],
            )
            * material_intensity_new_capacity_overgrids()
            * unit_conversion_mw_tw()
            / unit_conversion_kg_mt(),
            lambda: sum(
                protra_capacity_expansion()
                .loc[:, :, "PROTRA_PP_wind_onshore"]
                .reset_coords(drop=True)
                .rename({"NRG_TO_I": "NRG_TO_I!"}),
                dim=["NRG_TO_I!"],
            )
            * material_intensity_new_capacity_overgrids()
            * unit_conversion_mw_tw()
            / unit_conversion_kg_mt(),
        )
        .expand_dims({"NRG_PRO_I": ["PROTRA_PP_wind_onshore"]}, 1)
        .values
    )
    return value


@component.add(
    name="materials_required_for_PROSTO",
    units="Mt/Year",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_materials": 1,
        "initial_prosto_dedicated_capacity_expansion": 1,
        "unit_conversion_kg_mt": 2,
        "materials_per_new_capacity_installed_ev_batteries_lfp": 2,
        "unit_conversion_mw_tw": 2,
        "prosto_dedicated_capacity_expansion": 1,
    },
)
def materials_required_for_prosto():
    return if_then_else(
        switch_materials() == 0,
        lambda: initial_prosto_dedicated_capacity_expansion()
        .loc[:, "PROSTO_STATIONARY_BATTERIES"]
        .reset_coords(drop=True)
        * materials_per_new_capacity_installed_ev_batteries_lfp()
        * unit_conversion_mw_tw()
        / unit_conversion_kg_mt(),
        lambda: prosto_dedicated_capacity_expansion()
        .loc[:, "PROSTO_STATIONARY_BATTERIES"]
        .reset_coords(drop=True)
        * materials_per_new_capacity_installed_ev_batteries_lfp()
        * unit_conversion_mw_tw()
        / unit_conversion_kg_mt(),
    )


@component.add(
    name="materials_required_for_PROSUP",
    units="Mt/Year",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "materials_required_for_new_grids_by_protra": 1,
        "materials_required_for_prosto": 1,
    },
)
def materials_required_for_prosup():
    """
    Annual materials requirements for the construction of new PROSUP. We assume dedicated stationary batteries are all LFP.
    """
    return (
        sum(
            materials_required_for_new_grids_by_protra().rename(
                {"NRG_PROTRA_I": "NRG_PROTRA_I!"}
            ),
            dim=["NRG_PROTRA_I!"],
        )
        + materials_required_for_prosto()
    )


@component.add(
    name="SWITCH_endogenous_account_materials_for_overgrids",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"switch_computation_static_eroi": 1, "switch_mat_overgrids": 1},
)
def switch_endogenous_account_materials_for_overgrids():
    """
    When estimating the static EROIst, overgrids are not considered. To disable only the option of materials for overgrids, the user has to modify the last number in the IF THEN ELSE(x, x, x) function of this variable: 1. Include materials for overgrids in the CED of RES elec var 0: NOT include materials for overgrids in the CED of RES elec var
    """
    return if_then_else(
        switch_computation_static_eroi() == 1, lambda: 0, lambda: switch_mat_overgrids()
    )


@component.add(
    name="SWITCH_MAT_OVERGRIDS",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_mat_overgrids"},
)
def switch_mat_overgrids():
    """
    This switch can take two values: 0: not accounting for additional materials for overgrids. 1: accounting for additional materials for overgrids.
    """
    return _ext_constant_switch_mat_overgrids()


_ext_constant_switch_mat_overgrids = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_MAT_OVERGRIDS",
    {},
    _root,
    {},
    "_ext_constant_switch_mat_overgrids",
)


@component.add(
    name="Total_recycled_materials_for_PROSUP",
    units="Mt",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "materials_required_for_prosup": 1,
        "materials_extracted_for_prosup": 1,
    },
)
def total_recycled_materials_for_prosup():
    """
    Total recycled materials for PROSUP.
    """
    return materials_required_for_prosup() - materials_extracted_for_prosup()
