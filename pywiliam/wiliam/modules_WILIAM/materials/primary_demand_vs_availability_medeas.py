"""
Module materials.primary_demand_vs_availability_medeas
Translated using PySD version 3.10.0
"""


@component.add(
    name="cum_materials_to_extract_BU_from_2015",
    units="Mt",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cum_total_materials_to_extract_for_electrified_transport_from_2015_9r": 1,
        "cumulated_extracted_materials_all_protras_from_2015": 1,
        "cumulated_materials_extracted_for_all_prosup_from_2015": 1,
    },
)
def cum_materials_to_extract_bu_from_2015():
    """
    Cumulative materials demand through bottom-up (BU) estimation from the year 2015.
    """
    return (
        cum_total_materials_to_extract_for_electrified_transport_from_2015_9r()
        + cumulated_extracted_materials_all_protras_from_2015()
        + cumulated_materials_extracted_for_all_prosup_from_2015()
    )


@component.add(
    name="indicator_materials_reserves_availability",
    units="DMNL",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"share_tot_cum_dem_vs_reserves_materials": 1},
)
def indicator_materials_reserves_availability():
    """
    =1 while the cumulative demand is lower than the estimated reserves, and =0 when the cumulative demand surpasses the estimated reserves.
    """
    return if_then_else(
        share_tot_cum_dem_vs_reserves_materials() < 1,
        lambda: xr.DataArray(
            1,
            {
                "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                "MATERIALS_I": _subscript_dict["MATERIALS_I"],
            },
            ["REGIONS_9_I", "MATERIALS_I"],
        ),
        lambda: xr.DataArray(
            0,
            {
                "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                "MATERIALS_I": _subscript_dict["MATERIALS_I"],
            },
            ["REGIONS_9_I", "MATERIALS_I"],
        ),
    )


@component.add(
    name="indicator_materials_resources_availability",
    units="DMNL",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"share_tot_cum_dem_vs_resources_materials": 1},
)
def indicator_materials_resources_availability():
    """
    =1 while the cumulative demand is lower than the estimated resources, and =0 when the cumulative demand surpasses the estimated resources.
    """
    return if_then_else(
        share_tot_cum_dem_vs_resources_materials() < 1,
        lambda: xr.DataArray(
            1,
            {
                "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                "MATERIALS_I": _subscript_dict["MATERIALS_I"],
            },
            ["REGIONS_9_I", "MATERIALS_I"],
        ),
        lambda: xr.DataArray(
            0,
            {
                "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                "MATERIALS_I": _subscript_dict["MATERIALS_I"],
            },
            ["REGIONS_9_I", "MATERIALS_I"],
        ),
    )


@component.add(
    name="risk_indicator_mineral_availability",
    units="DMNL",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "indicator_materials_resources_availability": 2,
        "indicator_materials_reserves_availability": 1,
    },
)
def risk_indicator_mineral_availability():
    """
    Risk indicator: - if cumulated primary demand > resources: 1 (high risk) - if cumulated primary demand > reserves but <:resources: 0.5 (medium risk) - if cumulated primary demand < reserves: 0 (no risk detected)
    """
    return if_then_else(
        indicator_materials_resources_availability() == 0,
        lambda: xr.DataArray(
            1,
            {
                "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                "MATERIALS_I": _subscript_dict["MATERIALS_I"],
            },
            ["REGIONS_9_I", "MATERIALS_I"],
        ),
        lambda: if_then_else(
            np.logical_and(
                indicator_materials_reserves_availability() == 0,
                indicator_materials_resources_availability() == 1,
            ),
            lambda: xr.DataArray(
                0.5,
                {
                    "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                    "MATERIALS_I": _subscript_dict["MATERIALS_I"],
                },
                ["REGIONS_9_I", "MATERIALS_I"],
            ),
            lambda: xr.DataArray(
                0,
                {
                    "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                    "MATERIALS_I": _subscript_dict["MATERIALS_I"],
                },
                ["REGIONS_9_I", "MATERIALS_I"],
            ),
        ),
    )


@component.add(
    name="share_cum_dem_materials_to_extract_BU_vs_total",
    units="DMNL",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cum_materials_to_extract_bu_from_2015": 1,
        "total_cumulative_demand_materials_to_extract_from_2015": 1,
    },
)
def share_cum_dem_materials_to_extract_bu_vs_total():
    """
    Yearly share of cumulative demand of materials to extract from bottom-up (BU) vs. total.
    """
    return zidz(
        cum_materials_to_extract_bu_from_2015(),
        total_cumulative_demand_materials_to_extract_from_2015(),
    )


@component.add(
    name="share_materials_cum_demand_to_extract_vs_reserves_BU",
    units="DMNL",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cum_materials_to_extract_bu_from_2015": 1,
        "global_mineral_reserves": 1,
    },
)
def share_materials_cum_demand_to_extract_vs_reserves_bu():
    """
    Share of materials cumulative demand to extract in mines from bottom-up (BU) vs reserves of each material.
    """
    return zidz(
        cum_materials_to_extract_bu_from_2015(),
        global_mineral_reserves().expand_dims(
            {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, 0
        ),
    )


@component.add(
    name="share_materials_cum_demand_to_extract_vs_resources_BU",
    units="DMNL",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cum_materials_to_extract_bu_from_2015": 1,
        "global_mineral_resources": 1,
    },
)
def share_materials_cum_demand_to_extract_vs_resources_bu():
    """
    Share of materials cumulative demand to extract in mines from bottom-up (BU) vs resources of each material.
    """
    return zidz(
        cum_materials_to_extract_bu_from_2015(),
        global_mineral_resources().expand_dims(
            {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, 0
        ),
    )


@component.add(
    name="share_minerals_consumption_alt_techn_vs_total_economy",
    units="DMNL",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_materials_required_bu": 2, "demand_projection_materials_roe": 1},
)
def share_minerals_consumption_alt_techn_vs_total_economy():
    """
    Share of minerals consumptions of the alternative technologies with relation to the total.
    """
    return zidz(
        total_materials_required_bu(),
        demand_projection_materials_roe() + total_materials_required_bu(),
    )


@component.add(
    name="share_RoE_cumulative_demand_to_extract_vs_reserves_materials",
    units="DMNL",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cum_materials_to_extract_roe_from_2015": 1,
        "global_mineral_reserves": 1,
    },
)
def share_roe_cumulative_demand_to_extract_vs_reserves_materials():
    """
    Yearly share of cumulative demand of the rest of the economy to be extracted in mines of materials vs. reserves.
    """
    return zidz(
        cum_materials_to_extract_roe_from_2015(),
        global_mineral_reserves().expand_dims(
            {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, 0
        ),
    )


@component.add(
    name="share_RoE_cumulative_demand_to_extract_vs_resources_materials",
    units="DMNL",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cum_materials_to_extract_roe_from_2015": 1,
        "global_mineral_resources": 1,
    },
)
def share_roe_cumulative_demand_to_extract_vs_resources_materials():
    """
    Yearly share of cumulative demand of the rest of the economy to be extracted in mines of materials vs. resources.
    """
    return zidz(
        cum_materials_to_extract_roe_from_2015(),
        global_mineral_resources().expand_dims(
            {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, 0
        ),
    )


@component.add(
    name="share_tot_cum_dem_vs_reserves_materials",
    units="DMNL",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "total_cumulative_demand_materials_to_extract_from_2015": 1,
        "global_mineral_reserves": 1,
    },
)
def share_tot_cum_dem_vs_reserves_materials():
    """
    Yearly share of total cumulative demand of materials vs. reserves.
    """
    return zidz(
        total_cumulative_demand_materials_to_extract_from_2015(),
        global_mineral_reserves().expand_dims(
            {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, 0
        ),
    )


@component.add(
    name="share_tot_cum_dem_vs_resources_materials",
    units="DMNL",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "total_cumulative_demand_materials_to_extract_from_2015": 1,
        "global_mineral_resources": 1,
    },
)
def share_tot_cum_dem_vs_resources_materials():
    """
    Yearly share of total cumulative demand of materials vs. resources.
    """
    return zidz(
        total_cumulative_demand_materials_to_extract_from_2015(),
        global_mineral_resources().expand_dims(
            {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, 0
        ),
    )


@component.add(
    name="total_cumulative_demand_materials_to_extract_from_2015",
    units="Mt",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cum_materials_to_extract_bu_from_2015": 1,
        "cum_materials_to_extract_roe_from_2015": 1,
    },
)
def total_cumulative_demand_materials_to_extract_from_2015():
    """
    Total cumulative demand materials to extract in mines.
    """
    return (
        cum_materials_to_extract_bu_from_2015()
        + cum_materials_to_extract_roe_from_2015()
    )


@component.add(
    name="Total_flow_materials_to_extract",
    units="Mt/Year",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"materials_to_extract_roe": 1, "total_materials_to_extract_bu": 1},
)
def total_flow_materials_to_extract():
    """
    Total flow of materials to extract from mines over time, i.e., the addition of the demand estimated through top-down and bottom-up methods.
    """
    return materials_to_extract_roe() + total_materials_to_extract_bu()


@component.add(
    name="Total_materials_required",
    units="Mt",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"demand_projection_materials_roe": 1, "total_materials_required_bu": 1},
)
def total_materials_required():
    """
    Total demand of minerals, i.e., the addition of the demand estimated through top-down and bottom-up methods.
    """
    return demand_projection_materials_roe() + total_materials_required_bu()


@component.add(
    name="Total_materials_required_BU",
    units="Mt/Year",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "materials_required_for_electric_transport_9r": 1,
        "materials_required_for_protra": 1,
        "materials_required_for_new_grids_by_protra": 1,
    },
)
def total_materials_required_bu():
    """
    Total materials required estimated through the bottom-up (BU) method.
    """
    return (
        materials_required_for_electric_transport_9r()
        + sum(
            materials_required_for_protra().rename({"NRG_PROTRA_I": "NRG_PROTRA_I!"}),
            dim=["NRG_PROTRA_I!"],
        )
        + sum(
            materials_required_for_new_grids_by_protra().rename(
                {"NRG_PROTRA_I": "NRG_PROTRA_I!"}
            ),
            dim=["NRG_PROTRA_I!"],
        )
    )


@component.add(
    name="total_materials_to_extract_BU",
    units="Mt/Year",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "materials_extracted_for_prosup": 1,
        "materials_extracted_for_protra": 1,
        "total_materials_to_extract_for_electric_transport_9r": 1,
    },
)
def total_materials_to_extract_bu():
    """
    Total materials to extract through bottom-up (BU) estimation.
    """
    return (
        materials_extracted_for_prosup()
        + sum(
            materials_extracted_for_protra().rename({"NRG_PROTRA_I": "NRG_PROTRA_I!"}),
            dim=["NRG_PROTRA_I!"],
        )
        + total_materials_to_extract_for_electric_transport_9r()
    )
