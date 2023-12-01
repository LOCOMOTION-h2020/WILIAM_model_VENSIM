"""
Module materials.requirements.pv_subtechn
Translated using PySD version 3.10.0
"""


@component.add(
    name="length_per_MW_building_wiring",
    units="m",
    subscripts=["PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_materials": 1,
        "length_per_mw_building_wiring_baseline": 2,
        "power_pv_panel_baseline": 1,
        "power_per_panel_by_pv_technology": 1,
    },
)
def length_per_mw_building_wiring():
    """
    Length per MW of PV rooftop building installation
    """
    return if_then_else(
        switch_materials() == 0,
        lambda: length_per_mw_building_wiring_baseline(),
        lambda: length_per_mw_building_wiring_baseline()
        * (power_pv_panel_baseline() / power_per_panel_by_pv_technology()),
    )


@component.add(
    name="length_per_MW_house_wiring",
    units="m",
    subscripts=["PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_materials": 1,
        "length_per_mw_house_wiring_baseline": 2,
        "power_pv_panel_baseline": 1,
        "power_per_panel_by_pv_technology": 1,
    },
)
def length_per_mw_house_wiring():
    """
    Length per MW of PV rooftop house installation
    """
    return if_then_else(
        switch_materials() == 0,
        lambda: length_per_mw_house_wiring_baseline(),
        lambda: length_per_mw_house_wiring_baseline()
        * (power_pv_panel_baseline() / power_per_panel_by_pv_technology()),
    )


@component.add(
    name="length_per_MW_inverter_to_transformer",
    units="m",
    subscripts=["PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_materials": 1,
        "length_per_mw_inverter_to_transformer_baseline": 2,
        "power_pv_panel_baseline": 1,
        "power_per_panel_by_pv_technology": 1,
    },
)
def length_per_mw_inverter_to_transformer():
    """
    length per MW of ground PV installation from the inverter to the transformer
    """
    return if_then_else(
        switch_materials() == 0,
        lambda: length_per_mw_inverter_to_transformer_baseline(),
        lambda: length_per_mw_inverter_to_transformer_baseline()
        * (power_pv_panel_baseline() / power_per_panel_by_pv_technology()),
    )


@component.add(
    name="length_per_MW_panel_to_inverter",
    units="m",
    subscripts=["PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_materials": 1,
        "length_per_mw_panel_to_inverter_baseline": 2,
        "power_pv_panel_baseline": 1,
        "power_per_panel_by_pv_technology": 1,
    },
)
def length_per_mw_panel_to_inverter():
    """
    length per MW of PV ground installation from the panel to the inverter
    """
    return if_then_else(
        switch_materials() == 0,
        lambda: length_per_mw_panel_to_inverter_baseline(),
        lambda: length_per_mw_panel_to_inverter_baseline()
        * (power_pv_panel_baseline() / power_per_panel_by_pv_technology()),
    )


@component.add(
    name="material_intensity_OM_PV_by_technology",
    units="kg/(Year*MW)",
    subscripts=[
        "MATERIALS_I",
        "PROTRA_PP_SOLAR_PV_I",
        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "material_intensity_pv_cells": 2,
        "material_intensity_pv_panel_frame": 2,
        "material_intensity_ratio_om_pv_panels": 2,
        "material_intensity_pv_inverter": 2,
        "protra_lifetime": 4,
        "inverter_pv_lifetime": 4,
    },
)
def material_intensity_om_pv_by_technology():
    """
    Materials requirements per MW for O&M of solar technology per type of panel
    """
    value = xr.DataArray(
        np.nan,
        {
            "MATERIALS_I": _subscript_dict["MATERIALS_I"],
            "PROTRA_PP_SOLAR_PV_I": _subscript_dict["PROTRA_PP_SOLAR_PV_I"],
            "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": _subscript_dict[
                "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"
            ],
        },
        ["MATERIALS_I", "PROTRA_PP_SOLAR_PV_I", "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"],
    )
    value.loc[:, ["PROTRA_PP_solar_open_space_PV"], :] = (
        (
            (
                (material_intensity_pv_cells() + material_intensity_pv_panel_frame())
                * material_intensity_ratio_om_pv_panels()
                + (
                    material_intensity_pv_inverter()
                    .loc[:, "PROTRA_PP_solar_open_space_PV"]
                    .reset_coords(drop=True)
                    * (
                        float(
                            protra_lifetime().loc[
                                "EU27", "PROTRA_PP_solar_open_space_PV"
                            ]
                        )
                        - inverter_pv_lifetime()
                    )
                    / inverter_pv_lifetime()
                )
            )
            / float(protra_lifetime().loc["EU27", "PROTRA_PP_solar_open_space_PV"])
        )
        .expand_dims({"NRG_PRO_I": ["PROTRA_PP_solar_open_space_PV"]}, 1)
        .values
    )
    value.loc[:, ["PROTRA_PP_solar_urban_PV"], :] = (
        (
            (
                (material_intensity_pv_cells() + material_intensity_pv_panel_frame())
                * material_intensity_ratio_om_pv_panels()
                + (
                    material_intensity_pv_inverter()
                    .loc[:, "PROTRA_PP_solar_urban_PV"]
                    .reset_coords(drop=True)
                    * (
                        float(protra_lifetime().loc["EU27", "PROTRA_PP_solar_urban_PV"])
                        - inverter_pv_lifetime()
                    )
                    / inverter_pv_lifetime()
                )
            )
            / float(protra_lifetime().loc["EU27", "PROTRA_PP_solar_urban_PV"])
        )
        .expand_dims({"NRG_PRO_I": ["PROTRA_PP_solar_urban_PV"]}, 1)
        .values
    )
    return value


@component.add(
    name="material_intensity_PV_cells",
    units="kg/MW",
    subscripts=["MATERIALS_I", "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_material_intensity_pv_cells": 1},
    other_deps={
        "_integ_material_intensity_pv_cells": {
            "initial": {"initial_material_intensity_pv_cells": 1},
            "step": {"reduction_rate_material_intensity_pv_cells": 1},
        }
    },
)
def material_intensity_pv_cells():
    """
    Materials requirements per MW of new solar cells of PV taking account the technology evolution
    """
    return _integ_material_intensity_pv_cells()


_integ_material_intensity_pv_cells = Integ(
    lambda: -reduction_rate_material_intensity_pv_cells(),
    lambda: initial_material_intensity_pv_cells(),
    "_integ_material_intensity_pv_cells",
)


@component.add(
    name="material_intensity_PV_panel_frame",
    units="kg/MW",
    subscripts=["MATERIALS_I", "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_materials": 1,
        "material_intensity_pv_subtechnology_panel_frame": 2,
        "initial_area_pv_panel_per_power": 1,
        "area_pv_panel_per_power": 1,
    },
)
def material_intensity_pv_panel_frame():
    """
    Materials requirements per MW and type of cell of new panel structures of solar PV technology.
    """
    return if_then_else(
        switch_materials() == 0,
        lambda: material_intensity_pv_subtechnology_panel_frame()
        * initial_area_pv_panel_per_power(),
        lambda: material_intensity_pv_subtechnology_panel_frame()
        * area_pv_panel_per_power(),
    )


@component.add(
    name="material_intensity_PV_panels_mounting_structures",
    units="kg/MW",
    subscripts=[
        "MATERIALS_I",
        "PROTRA_PP_SOLAR_PV_I",
        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_materials": 1,
        "material_requirements_pv_mounting_structures_baseline": 2,
        "initial_area_pv_panel_per_power": 1,
        "area_pv_panel_per_power": 1,
    },
)
def material_intensity_pv_panels_mounting_structures():
    """
    Materials requirements per MW and type of cell of new mounting structures of solar PV technology.
    """
    return if_then_else(
        switch_materials() == 0,
        lambda: material_requirements_pv_mounting_structures_baseline()
        * initial_area_pv_panel_per_power(),
        lambda: material_requirements_pv_mounting_structures_baseline()
        * area_pv_panel_per_power(),
    )


@component.add(
    name="PV_wiring_land_total_intensity",
    units="kg/MW",
    subscripts=["MATERIALS_I", "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "length_per_mw_inverter_to_transformer": 1,
        "material_requirements_pv_wiring_land_inverter_to_transformer": 1,
        "material_requirements_pv_wiring_land_panel_to_inverter": 1,
        "length_per_mw_panel_to_inverter": 1,
    },
)
def pv_wiring_land_total_intensity():
    """
    Mineral requirements per MW for the wiring of a photovoltaic ground system
    """
    return (
        length_per_mw_inverter_to_transformer()
        * material_requirements_pv_wiring_land_inverter_to_transformer()
        + length_per_mw_panel_to_inverter()
        * material_requirements_pv_wiring_land_panel_to_inverter()
    ).transpose("MATERIALS_I", "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I")


@component.add(
    name="PV_wiring_urban_total_intensity",
    units="kg/MW",
    subscripts=["MATERIALS_I", "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "material_requirements_pv_wiring_building": 1,
        "length_per_mw_building_wiring": 1,
        "share_pv_installations_single_family_vs_total_households_buildings_sp": 2,
        "length_per_mw_house_wiring": 1,
        "material_requirements_pv_wiring_house": 1,
    },
)
def pv_wiring_urban_total_intensity():
    """
    Mineral requirements per MW for the wiring of a photovoltaic rooftop system
    """
    return (
        material_requirements_pv_wiring_building()
        * length_per_mw_building_wiring()
        * (1 - share_pv_installations_single_family_vs_total_households_buildings_sp())
        + material_requirements_pv_wiring_house()
        * length_per_mw_house_wiring()
        * share_pv_installations_single_family_vs_total_households_buildings_sp()
    )


@component.add(
    name="reduction_rate_material_intensity_PV_cells",
    units="kg/(Year*MW)",
    subscripts=["MATERIALS_I", "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 3,
        "initial_year_reduction_material_intensity_pv_sp": 3,
        "reduction_rate_material_intensity_pv_rest_of_materials_sp": 1,
        "material_intensity_pv_cells": 3,
        "reduction_rate_material_intensity_c_si_pv_sn_sp": 1,
        "reduction_rate_material_intensity_c_si_pv_si_sp": 1,
    },
)
def reduction_rate_material_intensity_pv_cells():
    """
    Reduction rate for material intensities of PV cells. Only improvements for the panels are considered.
    """
    value = xr.DataArray(
        np.nan,
        {
            "MATERIALS_I": _subscript_dict["MATERIALS_I"],
            "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": _subscript_dict[
                "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"
            ],
        },
        ["MATERIALS_I", "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"],
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[["Tin"], :] = False
    except_subs.loc[["Silicon_sand"], :] = False
    value.values[except_subs.values] = if_then_else(
        time() < initial_year_reduction_material_intensity_pv_sp(),
        lambda: xr.DataArray(
            0,
            {
                "MATERIALS_I": _subscript_dict["MATERIALS_I"],
                "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": _subscript_dict[
                    "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"
                ],
            },
            ["MATERIALS_I", "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"],
        ),
        lambda: reduction_rate_material_intensity_pv_rest_of_materials_sp()
        * material_intensity_pv_cells(),
    ).values[except_subs.values]
    value.loc[["Tin"], :] = (
        if_then_else(
            time() < initial_year_reduction_material_intensity_pv_sp(),
            lambda: xr.DataArray(
                0,
                {
                    "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": _subscript_dict[
                        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"
                    ]
                },
                ["PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"],
            ),
            lambda: reduction_rate_material_intensity_c_si_pv_sn_sp()
            * material_intensity_pv_cells().loc["Tin", :].reset_coords(drop=True),
        )
        .expand_dims({"MATERIALS_I": ["Tin"]}, 0)
        .values
    )
    value.loc[["Silicon_sand"], :] = (
        if_then_else(
            time() < initial_year_reduction_material_intensity_pv_sp(),
            lambda: xr.DataArray(
                0,
                {
                    "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": _subscript_dict[
                        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"
                    ]
                },
                ["PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"],
            ),
            lambda: reduction_rate_material_intensity_c_si_pv_si_sp()
            * material_intensity_pv_cells()
            .loc["Silicon_sand", :]
            .reset_coords(drop=True),
        )
        .expand_dims({"MATERIALS_I": ["Silicon_sand"]}, 0)
        .values
    )
    return value


@component.add(
    name="relative_demand_of_material_i_by_PV_panel",
    units="DMNL",
    subscripts=[
        "MATERIALS_I",
        "PROTRA_PP_SOLAR_PV_I",
        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_material_intensity_pv_by_technology": 2},
)
def relative_demand_of_material_i_by_pv_panel():
    """
    Relative demand of mineral by PV panel; demand of mineral i by panel l /demand of mineral i by all the panels.
    """
    return zidz(
        total_material_intensity_pv_by_technology(),
        sum(
            total_material_intensity_pv_by_technology().rename(
                {
                    "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!"
                }
            ),
            dim=["PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!"],
        ).expand_dims(
            {
                "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": _subscript_dict[
                    "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"
                ]
            },
            2,
        ),
    )


@component.add(
    name="SHARE_PV_INSTALLATIONS_SINGLE_FAMILY_VS_TOTAL_HOUSEHOLDS_BUILDINGS_SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_share_pv_installations_single_family_vs_total_households_buildings_sp"
    },
)
def share_pv_installations_single_family_vs_total_households_buildings_sp():
    """
    Ratio of PV installations in individual houses as a share of total buildings (individual houses + flats + etc.). Due to uncertainty a 0.5/1 is chosen by default.
    """
    return (
        _ext_constant_share_pv_installations_single_family_vs_total_households_buildings_sp()
    )


_ext_constant_share_pv_installations_single_family_vs_total_households_buildings_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "SHARE_PV_INSTALLATIONS_SINGLE_FAMILY_VS_TOTAL_HOUSEHOLDS_BUILDINGS_SP",
    {},
    _root,
    {},
    "_ext_constant_share_pv_installations_single_family_vs_total_households_buildings_sp",
)


@component.add(
    name="total_material_intensity_PV_by_technology",
    units="kg/MW",
    subscripts=[
        "MATERIALS_I",
        "PROTRA_PP_SOLAR_PV_I",
        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "material_aux_intensity_pv_land": 1,
        "material_intensity_pv_cells": 2,
        "material_intensity_pv_inverter": 2,
        "material_intensity_pv_panels_mounting_structures": 2,
        "material_intensity_pv_panel_frame": 2,
        "material_intensity_pv_transformer_land": 1,
        "pv_wiring_land_total_intensity": 1,
        "pv_wiring_urban_total_intensity": 1,
    },
)
def total_material_intensity_pv_by_technology():
    """
    Total mineral requirements per MW of a photovoltaic system per type of panel and per type of location (urban vs open-space).
    """
    value = xr.DataArray(
        np.nan,
        {
            "MATERIALS_I": _subscript_dict["MATERIALS_I"],
            "PROTRA_PP_SOLAR_PV_I": _subscript_dict["PROTRA_PP_SOLAR_PV_I"],
            "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": _subscript_dict[
                "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"
            ],
        },
        ["MATERIALS_I", "PROTRA_PP_SOLAR_PV_I", "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"],
    )
    value.loc[:, ["PROTRA_PP_solar_open_space_PV"], :] = (
        (
            material_aux_intensity_pv_land()
            + material_intensity_pv_cells()
            + material_intensity_pv_inverter()
            .loc[:, "PROTRA_PP_solar_open_space_PV"]
            .reset_coords(drop=True)
            + material_intensity_pv_panels_mounting_structures()
            .loc[:, "PROTRA_PP_solar_open_space_PV", :]
            .reset_coords(drop=True)
            + material_intensity_pv_panel_frame()
            + material_intensity_pv_transformer_land()
            + pv_wiring_land_total_intensity()
        )
        .expand_dims({"NRG_PRO_I": ["PROTRA_PP_solar_open_space_PV"]}, 1)
        .values
    )
    value.loc[:, ["PROTRA_PP_solar_urban_PV"], :] = (
        (
            material_intensity_pv_cells()
            + material_intensity_pv_inverter()
            .loc[:, "PROTRA_PP_solar_urban_PV"]
            .reset_coords(drop=True)
            + material_intensity_pv_panels_mounting_structures()
            .loc[:, "PROTRA_PP_solar_urban_PV", :]
            .reset_coords(drop=True)
            + material_intensity_pv_panel_frame()
            + pv_wiring_urban_total_intensity()
        )
        .expand_dims({"NRG_PRO_I": ["PROTRA_PP_solar_urban_PV"]}, 1)
        .values
    )
    return value
