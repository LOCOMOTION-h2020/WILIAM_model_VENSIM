"""
Module materials.requirements.protra
Translated using PySD version 3.10.0
"""


@component.add(
    name="cum_materials_requirements_for_PROTRA_from_initial_year",
    units="Mt",
    subscripts=["REGIONS_9_I", "NRG_PROTRA_I", "MATERIALS_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_cum_materials_requirements_for_protra_from_initial_year": 1},
    other_deps={
        "_integ_cum_materials_requirements_for_protra_from_initial_year": {
            "initial": {},
            "step": {"materials_required_for_protra": 1},
        }
    },
)
def cum_materials_requirements_for_protra_from_initial_year():
    """
    Total cumulative materials requirements for the installation and O&M by PROTRA technology.
    """
    return _integ_cum_materials_requirements_for_protra_from_initial_year()


_integ_cum_materials_requirements_for_protra_from_initial_year = Integ(
    lambda: materials_required_for_protra(),
    lambda: xr.DataArray(
        0,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
            "MATERIALS_I": _subscript_dict["MATERIALS_I"],
        },
        ["REGIONS_9_I", "NRG_PROTRA_I", "MATERIALS_I"],
    ),
    "_integ_cum_materials_requirements_for_protra_from_initial_year",
)


@component.add(
    name="cum_materials_to_extract_for_PROTRA_from_initial_year",
    units="Mt",
    subscripts=["REGIONS_9_I", "NRG_PROTRA_I", "MATERIALS_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_cum_materials_to_extract_for_protra_from_initial_year": 1},
    other_deps={
        "_integ_cum_materials_to_extract_for_protra_from_initial_year": {
            "initial": {},
            "step": {"materials_extracted_for_protra": 1},
        }
    },
)
def cum_materials_to_extract_for_protra_from_initial_year():
    """
    Cumulative materials to be mined for the installation and O&M of PROTRA.
    """
    return _integ_cum_materials_to_extract_for_protra_from_initial_year()


_integ_cum_materials_to_extract_for_protra_from_initial_year = Integ(
    lambda: materials_extracted_for_protra(),
    lambda: xr.DataArray(
        0,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
            "MATERIALS_I": _subscript_dict["MATERIALS_I"],
        },
        ["REGIONS_9_I", "NRG_PROTRA_I", "MATERIALS_I"],
    ),
    "_integ_cum_materials_to_extract_for_protra_from_initial_year",
)


@component.add(
    name="cum_materials_xtracted_for_PROTRA_from_2015",
    units="Mt",
    subscripts=["REGIONS_9_I", "NRG_PROTRA_I", "MATERIALS_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_cum_materials_xtracted_for_protra_from_2015": 1},
    other_deps={
        "_integ_cum_materials_xtracted_for_protra_from_2015": {
            "initial": {},
            "step": {"materials_extracted_for_protra_from_2015": 1},
        }
    },
)
def cum_materials_xtracted_for_protra_from_2015():
    """
    Cumulative materials to be mined for the installation and O&M by PROTRA technology.
    """
    return _integ_cum_materials_xtracted_for_protra_from_2015()


_integ_cum_materials_xtracted_for_protra_from_2015 = Integ(
    lambda: materials_extracted_for_protra_from_2015(),
    lambda: xr.DataArray(
        0,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
            "MATERIALS_I": _subscript_dict["MATERIALS_I"],
        },
        ["REGIONS_9_I", "NRG_PROTRA_I", "MATERIALS_I"],
    ),
    "_integ_cum_materials_xtracted_for_protra_from_2015",
)


@component.add(
    name="cumulated_extracted_materials_all_PROTRAs_from_2015",
    units="Mt",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"cum_materials_xtracted_for_protra_from_2015": 1},
)
def cumulated_extracted_materials_all_protras_from_2015():
    """
    Cumulatd materials to extrac for all PROTRA technologies from 2015.
    """
    return sum(
        cum_materials_xtracted_for_protra_from_2015().rename(
            {"NRG_PROTRA_I": "NRG_PROTRA_I!"}
        ),
        dim=["NRG_PROTRA_I!"],
    )


@component.add(
    name="material_intensities_for_new_PROTRA",
    units="kg/MW",
    subscripts=["REGIONS_9_I", "NRG_PROTRA_I", "MATERIALS_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "material_intensity_new_capacity_csp_regional": 1,
        "material_intensity_weighted_average_new_pv": 1,
        "material_intensity_new_capacity_wind_offshore_regional": 1,
        "material_intensity_new_capacity_wind_onshore_regional": 1,
    },
)
def material_intensities_for_new_protra():
    """
    Material intensities for new capacities of transformation.
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
    except_subs.loc[:, _subscript_dict["PROTRA_PP_SOLAR_PV_I"], :] = False
    except_subs.loc[:, ["PROTRA_PP_wind_offshore"], :] = False
    except_subs.loc[:, ["PROTRA_PP_wind_onshore"], :] = False
    value.values[except_subs.values] = 0
    value.loc[:, ["PROTRA_PP_solar_CSP"], :] = (
        material_intensity_new_capacity_csp_regional()
        .expand_dims({"NRG_PRO_I": ["PROTRA_PP_solar_CSP"]}, 1)
        .values
    )
    value.loc[:, _subscript_dict["PROTRA_PP_SOLAR_PV_I"], :] = (
        material_intensity_weighted_average_new_pv()
        .transpose("REGIONS_9_I", "PROTRA_PP_SOLAR_PV_I", "MATERIALS_I")
        .values
    )
    value.loc[:, ["PROTRA_PP_wind_offshore"], :] = (
        material_intensity_new_capacity_wind_offshore_regional()
        .expand_dims({"NRG_PRO_I": ["PROTRA_PP_wind_offshore"]}, 1)
        .values
    )
    value.loc[:, ["PROTRA_PP_wind_onshore"], :] = (
        material_intensity_new_capacity_wind_onshore_regional()
        .expand_dims({"NRG_PRO_I": ["PROTRA_PP_wind_onshore"]}, 1)
        .values
    )
    return value


@component.add(
    name="material_intensities_OM_PROTRA",
    units="kg/(MW*Year)",
    subscripts=["REGIONS_9_I", "NRG_PROTRA_I", "MATERIALS_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "material_intensity_om_csp_regional": 1,
        "material_intensity_weigthed_average_om_pv": 1,
        "material_intensity_om_wind_offshore_regional": 1,
        "material_intensity_om_wind_onshore_regional": 1,
    },
)
def material_intensities_om_protra():
    """
    Material intensities for the operation & maintenance of process transformation capacities in operation.
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
    except_subs.loc[:, _subscript_dict["PROTRA_PP_SOLAR_PV_I"], :] = False
    except_subs.loc[:, ["PROTRA_PP_wind_offshore"], :] = False
    except_subs.loc[:, ["PROTRA_PP_wind_onshore"], :] = False
    value.values[except_subs.values] = 0
    value.loc[:, ["PROTRA_PP_solar_CSP"], :] = (
        material_intensity_om_csp_regional()
        .expand_dims({"NRG_PRO_I": ["PROTRA_PP_solar_CSP"]}, 1)
        .values
    )
    value.loc[:, _subscript_dict["PROTRA_PP_SOLAR_PV_I"], :] = (
        material_intensity_weigthed_average_om_pv()
        .transpose("REGIONS_9_I", "PROTRA_PP_SOLAR_PV_I", "MATERIALS_I")
        .values
    )
    value.loc[:, ["PROTRA_PP_wind_offshore"], :] = (
        material_intensity_om_wind_offshore_regional()
        .expand_dims({"NRG_PRO_I": ["PROTRA_PP_wind_offshore"]}, 1)
        .values
    )
    value.loc[:, ["PROTRA_PP_wind_onshore"], :] = (
        material_intensity_om_wind_onshore_regional()
        .expand_dims({"NRG_PRO_I": ["PROTRA_PP_wind_onshore"]}, 1)
        .values
    )
    return value


@component.add(
    name="MATERIAL_INTENSITY_NEW_CAPACITY_CSP_REGIONAL",
    units="kg/MW",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"material_intensity_new_capacity_csp": 1},
)
def material_intensity_new_capacity_csp_regional():
    return material_intensity_new_capacity_csp().expand_dims(
        {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, 0
    )


@component.add(
    name="MATERIAL_INTENSITY_NEW_CAPACITY_WIND_OFFSHORE_REGIONAL",
    units="kg/MW",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"material_intensity_new_capacity_wind_offshore": 1},
)
def material_intensity_new_capacity_wind_offshore_regional():
    return material_intensity_new_capacity_wind_offshore().expand_dims(
        {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, 0
    )


@component.add(
    name="MATERIAL_INTENSITY_NEW_CAPACITY_WIND_ONSHORE_REGIONAL",
    units="kg/MW",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"material_intensity_new_capacity_wind_onshore": 1},
)
def material_intensity_new_capacity_wind_onshore_regional():
    return material_intensity_new_capacity_wind_onshore().expand_dims(
        {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, 0
    )


@component.add(
    name="MATERIAL_INTENSITY_OM_CSP_REGIONAL",
    units="kg/(MW*Year)",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"material_intensity_om_csp": 1},
)
def material_intensity_om_csp_regional():
    return material_intensity_om_csp().expand_dims(
        {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, 0
    )


@component.add(
    name="MATERIAL_INTENSITY_OM_WIND_OFFSHORE_REGIONAL",
    units="kg/(MW*Year)",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"material_intensity_om_wind_offshore": 1},
)
def material_intensity_om_wind_offshore_regional():
    return material_intensity_om_wind_offshore().expand_dims(
        {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, 0
    )


@component.add(
    name="MATERIAL_INTENSITY_OM_WIND_ONSHORE_REGIONAL",
    units="kg/(MW*Year)",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"material_intensity_om_wind_onshore": 1},
)
def material_intensity_om_wind_onshore_regional():
    return material_intensity_om_wind_onshore().expand_dims(
        {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, 0
    )


@component.add(
    name="material_intensity_weighted_average_new_PV",
    units="kg/MW",
    subscripts=["REGIONS_9_I", "MATERIALS_I", "PROTRA_PP_SOLAR_PV_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_materials": 2,
        "scrap_rate": 4,
        "initial_share_new_pv_subtechn_land": 1,
        "total_material_intensity_pv_by_technology": 4,
        "share_new_pv_subtechn_land": 1,
        "initial_share_new_pv_subtechn_urban": 1,
        "share_new_pv_subtechn_urban": 1,
    },
)
def material_intensity_weighted_average_new_pv():
    """
    Total material intensity of new PV instalations as a weighted average of the different subtechnologies.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "MATERIALS_I": _subscript_dict["MATERIALS_I"],
            "PROTRA_PP_SOLAR_PV_I": _subscript_dict["PROTRA_PP_SOLAR_PV_I"],
        },
        ["REGIONS_9_I", "MATERIALS_I", "PROTRA_PP_SOLAR_PV_I"],
    )
    value.loc[:, :, ["PROTRA_PP_solar_open_space_PV"]] = (
        if_then_else(
            switch_materials() == 0,
            lambda: sum(
                initial_share_new_pv_subtechn_land().rename(
                    {
                        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!"
                    }
                )
                * total_material_intensity_pv_by_technology()
                .loc[:, "PROTRA_PP_solar_open_space_PV", :]
                .reset_coords(drop=True)
                .rename(
                    {
                        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!"
                    }
                )
                .transpose("PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!", "MATERIALS_I"),
                dim=["PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!"],
            )
            * (1 + scrap_rate()),
            lambda: sum(
                share_new_pv_subtechn_land().rename(
                    {
                        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!"
                    }
                )
                * total_material_intensity_pv_by_technology()
                .loc[:, "PROTRA_PP_solar_open_space_PV", :]
                .reset_coords(drop=True)
                .rename(
                    {
                        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!"
                    }
                )
                .transpose("PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!", "MATERIALS_I"),
                dim=["PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!"],
            )
            * (1 + scrap_rate()),
        )
        .expand_dims({"NRG_PRO_I": ["PROTRA_PP_solar_open_space_PV"]}, 2)
        .values
    )
    value.loc[:, :, ["PROTRA_PP_solar_urban_PV"]] = (
        if_then_else(
            switch_materials() == 0,
            lambda: sum(
                initial_share_new_pv_subtechn_urban().rename(
                    {
                        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!"
                    }
                )
                * total_material_intensity_pv_by_technology()
                .loc[:, "PROTRA_PP_solar_urban_PV", :]
                .reset_coords(drop=True)
                .rename(
                    {
                        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!"
                    }
                )
                .transpose("PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!", "MATERIALS_I"),
                dim=["PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!"],
            )
            * (1 + scrap_rate()),
            lambda: sum(
                share_new_pv_subtechn_urban().rename(
                    {
                        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!"
                    }
                )
                * total_material_intensity_pv_by_technology()
                .loc[:, "PROTRA_PP_solar_urban_PV", :]
                .reset_coords(drop=True)
                .rename(
                    {
                        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!"
                    }
                )
                .transpose("PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!", "MATERIALS_I"),
                dim=["PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!"],
            )
            * (1 + scrap_rate()),
        )
        .expand_dims({"NRG_PRO_I": ["PROTRA_PP_solar_urban_PV"]}, 2)
        .values
    )
    return value


@component.add(
    name="material_intensity_weigthed_average_OM_PV",
    units="kg/(MW*Year)",
    subscripts=["REGIONS_9_I", "MATERIALS_I", "PROTRA_PP_SOLAR_PV_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_materials": 1,
        "material_intensity_om_pv_by_technology": 2,
        "initial_share_pv_capacity_by_subtechnology": 1,
        "share_pv_capacity_by_subtechnology": 1,
    },
)
def material_intensity_weigthed_average_om_pv():
    """
    Total OM material intensity of PV instalations stock as a weighted average of the different subtechnologies.
    """
    return if_then_else(
        switch_materials() == 0,
        lambda: sum(
            initial_share_pv_capacity_by_subtechnology().rename(
                {
                    "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!"
                }
            )
            * material_intensity_om_pv_by_technology()
            .rename(
                {
                    "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!"
                }
            )
            .transpose(
                "PROTRA_PP_SOLAR_PV_I",
                "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!",
                "MATERIALS_I",
            ),
            dim=["PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!"],
        ),
        lambda: sum(
            share_pv_capacity_by_subtechnology().rename(
                {
                    "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!"
                }
            )
            * material_intensity_om_pv_by_technology()
            .rename(
                {
                    "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!"
                }
            )
            .transpose(
                "PROTRA_PP_SOLAR_PV_I",
                "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!",
                "MATERIALS_I",
            ),
            dim=["PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!"],
        ),
    ).transpose("REGIONS_9_I", "MATERIALS_I", "PROTRA_PP_SOLAR_PV_I")


@component.add(
    name="Materials_extracted_for_PROTRA",
    units="Mt/Year",
    subscripts=["REGIONS_9_I", "NRG_PROTRA_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "materials_required_for_protra": 1,
        "eol_recycling_rates_minerals_alt_techn": 1,
    },
)
def materials_extracted_for_protra():
    """
    Annual materials to be mined for the construction and O&M by PROTRA technology..
    """
    return materials_required_for_protra() * (
        1 - eol_recycling_rates_minerals_alt_techn()
    )


@component.add(
    name="Materials_extracted_for_PROTRA_from_2015",
    units="Mt/Year",
    subscripts=["REGIONS_9_I", "NRG_PROTRA_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "materials_extracted_for_protra": 1},
)
def materials_extracted_for_protra_from_2015():
    """
    Annual materials to be mined for the installation and O&M by PROTRA technology from 2015.
    """
    return if_then_else(
        time() < 2015,
        lambda: xr.DataArray(
            0,
            {
                "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
                "MATERIALS_I": _subscript_dict["MATERIALS_I"],
            },
            ["REGIONS_9_I", "NRG_PROTRA_I", "MATERIALS_I"],
        ),
        lambda: materials_extracted_for_protra(),
    )


@component.add(
    name="materials_required_for_new_PROTRA",
    units="Mt/Year",
    subscripts=["REGIONS_9_I", "NRG_PROTRA_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_materials": 1,
        "initial_protra_capacity_expansion": 1,
        "protra_capacity_expansion": 1,
        "material_intensities_for_new_protra": 1,
        "unit_conversion_mw_tw": 1,
        "unit_conversion_kg_mt": 1,
    },
)
def materials_required_for_new_protra():
    """
    Annual materials required for the installation of new capacity by PROTRA technology.
    """
    return (
        if_then_else(
            switch_materials() == 0,
            lambda: sum(
                initial_protra_capacity_expansion().rename({"NRG_TO_I": "NRG_TO_I!"}),
                dim=["NRG_TO_I!"],
            ),
            lambda: sum(
                protra_capacity_expansion().rename({"NRG_TO_I": "NRG_TO_I!"}),
                dim=["NRG_TO_I!"],
            ),
        )
        * material_intensities_for_new_protra()
        * unit_conversion_mw_tw()
        / unit_conversion_kg_mt()
    )


@component.add(
    name="Materials_required_for_OM_PROTRA",
    units="Mt/Year",
    subscripts=["REGIONS_9_I", "NRG_PROTRA_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_materials": 1,
        "material_intensities_om_protra": 2,
        "initial_protra_capacity_stock": 1,
        "unit_conversion_kg_mt": 2,
        "unit_conversion_mw_tw": 2,
        "protra_capacity_stock": 1,
    },
)
def materials_required_for_om_protra():
    """
    Annual materials required for the operation and maintenance of the capacity of PROTRA in operation by technology.
    """
    return if_then_else(
        switch_materials() == 0,
        lambda: sum(
            initial_protra_capacity_stock()
            .loc[_subscript_dict["REGIONS_9_I"], :, :]
            .rename({"REGIONS_36_I": "REGIONS_9_I", "NRG_TO_I": "NRG_TO_I!"}),
            dim=["NRG_TO_I!"],
        )
        * material_intensities_om_protra()
        * unit_conversion_mw_tw()
        / unit_conversion_kg_mt(),
        lambda: sum(
            protra_capacity_stock().rename({"NRG_TO_I": "NRG_TO_I!"}), dim=["NRG_TO_I!"]
        )
        * material_intensities_om_protra()
        * unit_conversion_mw_tw()
        / unit_conversion_kg_mt(),
    )


@component.add(
    name="Materials_required_for_PROTRA",
    units="Mt/Year",
    subscripts=["REGIONS_9_I", "NRG_PROTRA_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "materials_required_for_new_protra": 1,
        "materials_required_for_om_protra": 1,
    },
)
def materials_required_for_protra():
    """
    Annual materials requirements for the construction and O&M of PROTRA.
    """
    return materials_required_for_new_protra() + materials_required_for_om_protra()


@component.add(
    name="Total_recycled_materials_for_PROTRA",
    units="Mt",
    subscripts=["REGIONS_9_I", "NRG_PROTRA_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "materials_required_for_protra": 1,
        "materials_extracted_for_protra": 1,
    },
)
def total_recycled_materials_for_protra():
    """
    Total recycled materials for PROTRA.
    """
    return materials_required_for_protra() - materials_extracted_for_protra()
