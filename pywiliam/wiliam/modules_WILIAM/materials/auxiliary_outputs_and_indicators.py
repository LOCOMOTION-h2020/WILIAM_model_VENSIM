"""
Module materials.auxiliary_outputs_and_indicators
Translated using PySD version 3.10.0
"""


@component.add(
    name="Al_consumption_per_capita",
    units="Mt/(Year*person)",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"al_market_sales": 1, "world_population": 1},
)
def al_consumption_per_capita():
    """
    Aluminium consumption in kg/person/year.
    """
    return zidz(al_market_sales(), world_population() / 10**9)


@component.add(
    name="Al_reserves_to_production_ratio",
    units="Year",
    subscripts=["Al_ORE_GRADES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_al_known_reserves": 1, "al_market_sales": 1},
)
def al_reserves_to_production_ratio():
    """
    The Reserves-to-Production (R/P) Ratio measures the number of years of Al supplies left based on current annual consumption rates. Note that this can change through time through the discovery of new Al reserves, and increases in annual consumption.
    """
    return zidz(
        total_al_known_reserves()
        .loc[_subscript_dict["Al_ORE_GRADES_I"]]
        .rename({"ORE_GRADES_I": "Al_ORE_GRADES_I"}),
        al_market_sales(),
    )


@component.add(
    name="coal_consumption_per_capita",
    units="EJ/(Year*person)",
    subscripts=["COAL_TYPES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_coal_production_capacity_ej": 1, "world_population": 1},
)
def coal_consumption_per_capita():
    return zidz(total_coal_production_capacity_ej(), world_population())


@component.add(
    name="coal_reserves_to_production_ratio",
    units="Years",
    subscripts=["COAL_TYPES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_coal_reserves": 1, "total_coal_production_capacity_ej": 1},
)
def coal_reserves_to_production_ratio():
    """
    The Reserves-to-Production (R/P) Ratio measures the number of years of fuel supplies left based on current annual consumption rates. Note that this can change through time through the discovery of new fuel reserves, and increases in annual consumption.
    """
    return zidz(total_coal_reserves(), total_coal_production_capacity_ej())


@component.add(
    name="Cu_consumption_per_capita",
    units="Mt/(Year*person)",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"cu_market_sales": 1, "world_population": 1},
)
def cu_consumption_per_capita():
    """
    Copper consumption in kg/person/year.
    """
    return zidz(cu_market_sales(), world_population() / 10**9)


@component.add(
    name="Cu_reserves_to_production_ratio",
    units="Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_cu_known_reserves": 1, "cu_market_sales": 1},
)
def cu_reserves_to_production_ratio():
    """
    The Reserves-to-Production (R/P) Ratio measures the number of years of Cu supplies left based on current annual consumption rates. Note that this can change through time through the discovery of new Cu reserves, and increases in annual consumption.
    """
    return zidz(total_cu_known_reserves(), cu_market_sales())


@component.add(
    name="cumulated_materials_to_extract_for_the_PV_cells",
    units="Mt",
    subscripts=["REGIONS_9_I", "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I", "MATERIALS_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_cumulated_materials_to_extract_for_the_pv_cells": 1},
    other_deps={
        "_integ_cumulated_materials_to_extract_for_the_pv_cells": {
            "initial": {},
            "step": {"new_material_extract_for_the_pv_cells": 1},
        }
    },
)
def cumulated_materials_to_extract_for_the_pv_cells():
    """
    cumulated material demand of the cells of photovoltaic systems
    """
    return _integ_cumulated_materials_to_extract_for_the_pv_cells()


_integ_cumulated_materials_to_extract_for_the_pv_cells = Integ(
    lambda: new_material_extract_for_the_pv_cells(),
    lambda: xr.DataArray(
        0,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": _subscript_dict[
                "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"
            ],
            "MATERIALS_I": _subscript_dict["MATERIALS_I"],
        },
        ["REGIONS_9_I", "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I", "MATERIALS_I"],
    ),
    "_integ_cumulated_materials_to_extract_for_the_pv_cells",
)


@component.add(
    name="cumulated_materials_to_extract_for_the_PV_inverters_and_transformers",
    units="Mt",
    subscripts=["REGIONS_9_I", "MATERIALS_I", "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={
        "_integ_cumulated_materials_to_extract_for_the_pv_inverters_and_transformers": 1
    },
    other_deps={
        "_integ_cumulated_materials_to_extract_for_the_pv_inverters_and_transformers": {
            "initial": {},
            "step": {"new_material_extract_pv_inverters_and_transformers": 1},
        }
    },
)
def cumulated_materials_to_extract_for_the_pv_inverters_and_transformers():
    """
    cumulated material demand of the inverters and transformers of photovoltaic systems
    """
    return _integ_cumulated_materials_to_extract_for_the_pv_inverters_and_transformers()


_integ_cumulated_materials_to_extract_for_the_pv_inverters_and_transformers = Integ(
    lambda: new_material_extract_pv_inverters_and_transformers().expand_dims(
        {
            "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": _subscript_dict[
                "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"
            ]
        },
        2,
    ),
    lambda: xr.DataArray(
        0,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "MATERIALS_I": _subscript_dict["MATERIALS_I"],
            "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": _subscript_dict[
                "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"
            ],
        },
        ["REGIONS_9_I", "MATERIALS_I", "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"],
    ),
    "_integ_cumulated_materials_to_extract_for_the_pv_inverters_and_transformers",
)


@component.add(
    name="cumulated_materials_to_extract_for_the_PV_panel_frames",
    units="Mt",
    subscripts=["REGIONS_9_I", "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I", "MATERIALS_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_cumulated_materials_to_extract_for_the_pv_panel_frames": 1},
    other_deps={
        "_integ_cumulated_materials_to_extract_for_the_pv_panel_frames": {
            "initial": {},
            "step": {"new_material_extract_pv_panel_frames": 1},
        }
    },
)
def cumulated_materials_to_extract_for_the_pv_panel_frames():
    """
    cumulated material demand of the panels structures of photovoltaic systems
    """
    return _integ_cumulated_materials_to_extract_for_the_pv_panel_frames()


_integ_cumulated_materials_to_extract_for_the_pv_panel_frames = Integ(
    lambda: new_material_extract_pv_panel_frames(),
    lambda: xr.DataArray(
        0,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": _subscript_dict[
                "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"
            ],
            "MATERIALS_I": _subscript_dict["MATERIALS_I"],
        },
        ["REGIONS_9_I", "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I", "MATERIALS_I"],
    ),
    "_integ_cumulated_materials_to_extract_for_the_pv_panel_frames",
)


@component.add(
    name="cumulated_materials_to_extract_for_the_PV_panels_mounting_structures",
    units="Mt",
    subscripts=[
        "REGIONS_9_I",
        "MATERIALS_I",
        "PROTRA_PP_SOLAR_PV_I",
        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I",
    ],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={
        "_integ_cumulated_materials_to_extract_for_the_pv_panels_mounting_structures": 1
    },
    other_deps={
        "_integ_cumulated_materials_to_extract_for_the_pv_panels_mounting_structures": {
            "initial": {},
            "step": {"new_material_extract_pv_panels_mounting_structures": 1},
        }
    },
)
def cumulated_materials_to_extract_for_the_pv_panels_mounting_structures():
    """
    cumulated material demand of the mounting structures of photovoltaic systems
    """
    return _integ_cumulated_materials_to_extract_for_the_pv_panels_mounting_structures()


_integ_cumulated_materials_to_extract_for_the_pv_panels_mounting_structures = Integ(
    lambda: new_material_extract_pv_panels_mounting_structures(),
    lambda: xr.DataArray(
        0,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "MATERIALS_I": _subscript_dict["MATERIALS_I"],
            "PROTRA_PP_SOLAR_PV_I": _subscript_dict["PROTRA_PP_SOLAR_PV_I"],
            "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": _subscript_dict[
                "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"
            ],
        },
        [
            "REGIONS_9_I",
            "MATERIALS_I",
            "PROTRA_PP_SOLAR_PV_I",
            "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I",
        ],
    ),
    "_integ_cumulated_materials_to_extract_for_the_pv_panels_mounting_structures",
)


@component.add(
    name="cumulated_materials_to_extract_for_the_PV_wiring",
    units="Mt",
    subscripts=["REGIONS_9_I", "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I", "MATERIALS_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_cumulated_materials_to_extract_for_the_pv_wiring": 1},
    other_deps={
        "_integ_cumulated_materials_to_extract_for_the_pv_wiring": {
            "initial": {},
            "step": {"new_material_extract_pv_wiring": 1},
        }
    },
)
def cumulated_materials_to_extract_for_the_pv_wiring():
    """
    cumulated material demand of the wiring of photovoltaic systems
    """
    return _integ_cumulated_materials_to_extract_for_the_pv_wiring()


_integ_cumulated_materials_to_extract_for_the_pv_wiring = Integ(
    lambda: new_material_extract_pv_wiring(),
    lambda: xr.DataArray(
        0,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": _subscript_dict[
                "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"
            ],
            "MATERIALS_I": _subscript_dict["MATERIALS_I"],
        },
        ["REGIONS_9_I", "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I", "MATERIALS_I"],
    ),
    "_integ_cumulated_materials_to_extract_for_the_pv_wiring",
)


@component.add(
    name="Fe_consumption_per_capita",
    units="Mt/(Year*person)",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"fe_market_sales": 1, "world_population": 1},
)
def fe_consumption_per_capita():
    """
    Iron consumption in kg/person/year.
    """
    return zidz(fe_market_sales(), world_population() / 10**9)


@component.add(
    name="Fe_reserves_to_production_ratio",
    units="Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_fe_known_reserves": 1, "fe_market_sales": 1},
)
def fe_reserves_to_production_ratio():
    """
    The Reserves-to-Production (R/P) Ratio measures the number of years of Fe supplies left based on current annual consumption rates. Note that this can change through time through the discovery of new Fe reserves, and increases in annual consumption.
    """
    return zidz(total_fe_known_reserves(), fe_market_sales())


@component.add(
    name="gas_consumtion_per_capita",
    units="EJ/(Year*person)",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"current_gas_extraction": 1, "world_population": 1},
)
def gas_consumtion_per_capita():
    return zidz(current_gas_extraction(), world_population())


@component.add(
    name="gas_reserves_to_production_ratio",
    units="Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"gas_reserves": 1, "current_gas_extraction": 1},
)
def gas_reserves_to_production_ratio():
    """
    The Reserves-to-Production (R/P) Ratio measures the number of years of fuel supplies left based on current annual consumption rates. Note that this can change through time through the discovery of new fuel reserves, and increases in annual consumption.
    """
    return zidz(gas_reserves(), current_gas_extraction())


@component.add(
    name="new_material_extract_for_the_PV_cells",
    units="Mt/Year",
    subscripts=["REGIONS_9_I", "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "rc_rate_mineral": 2,
        "share_new_pv_subtechn_land": 1,
        "material_intensity_pv_cells": 2,
        "scrap_rate": 2,
        "share_new_pv_subtechn_urban": 1,
        "unit_conversion_mw_tw": 1,
        "unit_conversion_kg_mt": 1,
        "protra_capacity_expansion": 2,
    },
)
def new_material_extract_for_the_pv_cells():
    """
    annual material demand of the cells of photovoltaic systems
    """
    return if_then_else(
        time() < 2015,
        lambda: xr.DataArray(
            0,
            {
                "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": _subscript_dict[
                    "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"
                ],
                "MATERIALS_I": _subscript_dict["MATERIALS_I"],
            },
            ["REGIONS_9_I", "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I", "MATERIALS_I"],
        ),
        lambda: (
            share_new_pv_subtechn_land()
            * protra_capacity_expansion()
            .loc[:, "TO_elec", "PROTRA_PP_solar_open_space_PV"]
            .reset_coords(drop=True)
            * material_intensity_pv_cells().transpose(
                "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I", "MATERIALS_I"
            )
            * (1 - rc_rate_mineral())
            * (1 + scrap_rate())
            + share_new_pv_subtechn_urban()
            * protra_capacity_expansion()
            .loc[:, "TO_elec", "PROTRA_PP_solar_urban_PV"]
            .reset_coords(drop=True)
            * material_intensity_pv_cells().transpose(
                "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I", "MATERIALS_I"
            )
            * (1 - rc_rate_mineral())
            * (1 + scrap_rate())
        )
        * unit_conversion_mw_tw()
        / unit_conversion_kg_mt(),
    )


@component.add(
    name="new_material_extract_PV_inverters_and_transformers",
    units="Mt/Year",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "protra_capacity_expansion": 2,
        "rc_rate_mineral": 2,
        "scrap_rate": 2,
        "material_intensity_pv_inverter": 2,
        "material_intensity_pv_transformer_land": 1,
        "unit_conversion_mw_tw": 1,
        "unit_conversion_kg_mt": 1,
    },
)
def new_material_extract_pv_inverters_and_transformers():
    """
    annual material demand of the inverters and transformers of photovoltaic systems
    """
    return (
        if_then_else(
            time() < 2015,
            lambda: xr.DataArray(
                0,
                {
                    "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                    "MATERIALS_I": _subscript_dict["MATERIALS_I"],
                },
                ["REGIONS_9_I", "MATERIALS_I"],
            ),
            lambda: protra_capacity_expansion()
            .loc[:, "TO_elec", "PROTRA_PP_solar_open_space_PV"]
            .reset_coords(drop=True)
            * (
                material_intensity_pv_inverter()
                .loc[:, "PROTRA_PP_solar_open_space_PV"]
                .reset_coords(drop=True)
                + material_intensity_pv_transformer_land()
            )
            * (1 - rc_rate_mineral())
            * (1 + scrap_rate())
            + protra_capacity_expansion()
            .loc[:, "TO_elec", "PROTRA_PP_solar_urban_PV"]
            .reset_coords(drop=True)
            * material_intensity_pv_inverter()
            .loc[:, "PROTRA_PP_solar_urban_PV"]
            .reset_coords(drop=True)
            * (1 - rc_rate_mineral())
            * (1 + scrap_rate()),
        )
        * unit_conversion_mw_tw()
        / unit_conversion_kg_mt()
    )


@component.add(
    name="new_material_extract_PV_panel_frames",
    units="Mt/Year",
    subscripts=["REGIONS_9_I", "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "rc_rate_mineral": 2,
        "share_new_pv_subtechn_land": 1,
        "material_intensity_pv_panel_frame": 2,
        "scrap_rate": 2,
        "share_new_pv_subtechn_urban": 1,
        "unit_conversion_mw_tw": 1,
        "unit_conversion_kg_mt": 1,
        "protra_capacity_expansion": 2,
    },
)
def new_material_extract_pv_panel_frames():
    """
    annual material demand of the panels structures of photovoltaic systems
    """
    return if_then_else(
        time() < 2015,
        lambda: xr.DataArray(
            0,
            {
                "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": _subscript_dict[
                    "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"
                ],
                "MATERIALS_I": _subscript_dict["MATERIALS_I"],
            },
            ["REGIONS_9_I", "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I", "MATERIALS_I"],
        ),
        lambda: (
            share_new_pv_subtechn_land()
            * protra_capacity_expansion()
            .loc[:, "TO_elec", "PROTRA_PP_solar_open_space_PV"]
            .reset_coords(drop=True)
            * material_intensity_pv_panel_frame().transpose(
                "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I", "MATERIALS_I"
            )
            * (1 - rc_rate_mineral())
            * (1 + scrap_rate())
            + share_new_pv_subtechn_urban()
            * protra_capacity_expansion()
            .loc[:, "TO_elec", "PROTRA_PP_solar_urban_PV"]
            .reset_coords(drop=True)
            * material_intensity_pv_panel_frame().transpose(
                "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I", "MATERIALS_I"
            )
            * (1 - rc_rate_mineral())
            * (1 + scrap_rate())
        )
        * unit_conversion_mw_tw()
        / unit_conversion_kg_mt(),
    )


@component.add(
    name="new_material_extract_PV_panels_mounting_structures",
    units="Mt/Year",
    subscripts=[
        "REGIONS_9_I",
        "MATERIALS_I",
        "PROTRA_PP_SOLAR_PV_I",
        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "rc_rate_mineral": 1,
        "material_intensity_pv_panels_mounting_structures": 1,
        "share_new_pv_subtechn_land": 1,
        "scrap_rate": 1,
        "unit_conversion_kg_mt": 1,
        "unit_conversion_mw_tw": 1,
        "protra_capacity_expansion": 1,
    },
)
def new_material_extract_pv_panels_mounting_structures():
    """
    annual material demand of the mounting structures of photovoltaic systems
    """
    return if_then_else(
        time() < 2015,
        lambda: xr.DataArray(
            0,
            {
                "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": _subscript_dict[
                    "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"
                ],
                "PROTRA_PP_SOLAR_PV_I": _subscript_dict["PROTRA_PP_SOLAR_PV_I"],
                "MATERIALS_I": _subscript_dict["MATERIALS_I"],
            },
            [
                "REGIONS_9_I",
                "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I",
                "PROTRA_PP_SOLAR_PV_I",
                "MATERIALS_I",
            ],
        ),
        lambda: share_new_pv_subtechn_land()
        * protra_capacity_expansion()
        .loc[:, "TO_elec", _subscript_dict["PROTRA_PP_SOLAR_PV_I"]]
        .reset_coords(drop=True)
        .rename({"NRG_PROTRA_I": "PROTRA_PP_SOLAR_PV_I"})
        * material_intensity_pv_panels_mounting_structures().transpose(
            "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I",
            "PROTRA_PP_SOLAR_PV_I",
            "MATERIALS_I",
        )
        * (1 - rc_rate_mineral())
        * (1 + scrap_rate())
        * unit_conversion_mw_tw()
        / unit_conversion_kg_mt(),
    ).transpose(
        "REGIONS_9_I",
        "MATERIALS_I",
        "PROTRA_PP_SOLAR_PV_I",
        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I",
    )


@component.add(
    name="new_material_extract_PV_wiring",
    units="Mt/Year",
    subscripts=["REGIONS_9_I", "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "pv_wiring_land_total_intensity": 1,
        "rc_rate_mineral": 2,
        "share_new_pv_subtechn_land": 1,
        "pv_wiring_urban_total_intensity": 1,
        "scrap_rate": 2,
        "share_new_pv_subtechn_urban": 1,
        "unit_conversion_mw_tw": 1,
        "unit_conversion_kg_mt": 1,
        "protra_capacity_expansion": 2,
    },
)
def new_material_extract_pv_wiring():
    """
    annual material demand of the wiring of photovoltaic systems
    """
    return if_then_else(
        time() < 2015,
        lambda: xr.DataArray(
            0,
            {
                "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": _subscript_dict[
                    "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"
                ],
                "MATERIALS_I": _subscript_dict["MATERIALS_I"],
            },
            ["REGIONS_9_I", "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I", "MATERIALS_I"],
        ),
        lambda: (
            share_new_pv_subtechn_land()
            * protra_capacity_expansion()
            .loc[:, "TO_elec", "PROTRA_PP_solar_open_space_PV"]
            .reset_coords(drop=True)
            * pv_wiring_land_total_intensity().transpose(
                "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I", "MATERIALS_I"
            )
            * (1 - rc_rate_mineral())
            * (1 + scrap_rate())
            + share_new_pv_subtechn_urban()
            * protra_capacity_expansion()
            .loc[:, "TO_elec", "PROTRA_PP_solar_urban_PV"]
            .reset_coords(drop=True)
            * pv_wiring_urban_total_intensity().transpose(
                "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I", "MATERIALS_I"
            )
            * (1 - rc_rate_mineral())
            * (1 + scrap_rate())
        )
        * unit_conversion_mw_tw()
        / unit_conversion_kg_mt(),
    )


@component.add(
    name="Ni_consumption_per_capita",
    units="Mt/(Year*person)",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ni_market_sales": 1, "world_population": 1},
)
def ni_consumption_per_capita():
    """
    Nickel consumption in kg/person/year.
    """
    return zidz(ni_market_sales(), world_population() / 10**9)


@component.add(
    name="Ni_reserves_to_production_ratio",
    units="Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_ni_known_reserves": 1, "ni_market_sales": 1},
)
def ni_reserves_to_production_ratio():
    """
    The Reserves-to-Production (R/P) Ratio measures the number of years of Ni supplies left based on current annual consumption rates. Note that this can change through time through the discovery of new Ni reserves, and increases in annual consumption.
    """
    return zidz(total_ni_known_reserves(), ni_market_sales())


@component.add(
    name="oil_consumption_per_capita",
    units="bbl/(Year*person)",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"current_oil_extraction": 1, "world_population": 1},
)
def oil_consumption_per_capita():
    return zidz(current_oil_extraction(), world_population())


@component.add(
    name="oil_reserves_to_production_ratio",
    units="Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"oil_known_reserves": 1, "current_oil_extraction": 1},
)
def oil_reserves_to_production_ratio():
    """
    The Reserves-to-Production (R/P) Ratio measures the number of years of fuel supplies left based on current annual consumption rates. Note that this can change through time through the discovery of new fuel reserves, and increases in annual consumption.
    """
    return zidz(oil_known_reserves(), current_oil_extraction())


@component.add(
    name="reference_Ni",
    comp_type="Auxiliary",
    comp_subtype="with Lookup",
    depends_on={"time": 1},
)
def reference_ni():
    return np.interp(
        time(),
        [
            2010.0,
            2011.0,
            2012.0,
            2013.0,
            2014.0,
            2015.0,
            2016.0,
            2017.0,
            2018.0,
            2019.0,
            2020.0,
            2021.0,
        ],
        [
            1.465,
            1.607,
            1.668,
            1.785,
            1.87,
            1.89,
            2.002,
            2.14,
            2.313,
            2.443,
            2.441,
            2.851,
        ],
    )


@component.add(
    name="reference_Ni_value",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "world_population": 1, "reference_ni": 1},
)
def reference_ni_value():
    return if_then_else(
        time() >= 2010,
        lambda: reference_ni() / (world_population() / 10**9),
        lambda: 0,
    )


@component.add(
    name="relative_RURR_Al",
    units="1",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_initial_al_urr": 2, "al_cumulative_mining": 1},
)
def relative_rurr_al():
    """
    Remaining resources+reserves of aluminium as a share of the initial availability
    """
    return (total_initial_al_urr() - al_cumulative_mining()) / total_initial_al_urr()


@component.add(
    name="relative_RURR_coal",
    units="1",
    subscripts=["COAL_TYPES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"coal_urr": 2, "cumulative_coal_extracted": 1},
)
def relative_rurr_coal():
    """
    Remaining resources+reserves of coal as a share of the initial availability.
    """
    return (coal_urr() - cumulative_coal_extracted()) / coal_urr()


@component.add(
    name="relative_RURR_Cu",
    units="1",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_initial_cu_urr": 2, "cu_cumulative_mining": 1},
)
def relative_rurr_cu():
    """
    Remaining resources+reserves of copper as a share of the initial availability.
    """
    return (total_initial_cu_urr() - cu_cumulative_mining()) / total_initial_cu_urr()


@component.add(
    name="relative_RURR_Fe",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_initial_fe_urr": 2, "fe_cumulative_mining": 1},
)
def relative_rurr_fe():
    """
    Remaining resources+reserves of iron as a share of the initial availability
    """
    return (total_initial_fe_urr() - fe_cumulative_mining()) / total_initial_fe_urr()


@component.add(
    name="relative_RURR_gas",
    units="1",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"urr_natural_gas": 2, "cumulative_extracted_gas": 1},
)
def relative_rurr_gas():
    """
    Remaining resources of natural gas as a share of the initial availability.
    """
    return (urr_natural_gas() - cumulative_extracted_gas()) / urr_natural_gas()


@component.add(
    name="relative_RURR_materiales",
    units="DMNL",
    subscripts=["HYDROCARBONS_W_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "relative_rurr_total_coal": 1,
        "relative_rurr_oil": 1,
        "relative_rurr_gas": 1,
    },
)
def relative_rurr_materiales():
    """
    Remaining resources+reserves of materials as a share of the initial availability.
    """
    value = xr.DataArray(
        np.nan,
        {"HYDROCARBONS_W_I": _subscript_dict["HYDROCARBONS_W_I"]},
        ["HYDROCARBONS_W_I"],
    )
    value.loc[["Coal_W"]] = relative_rurr_total_coal()
    value.loc[["Oil_W"]] = relative_rurr_oil()
    value.loc[["Gas_W"]] = relative_rurr_gas()
    return value


@component.add(
    name="relative_RURR_Ni",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_initial_ni_urr": 2, "ni_cumulative_mining": 1},
)
def relative_rurr_ni():
    """
    Remaining resources+reserves of nickel as a share of the initial availability
    """
    return (total_initial_ni_urr() - ni_cumulative_mining()) / total_initial_ni_urr()


@component.add(
    name="relative_RURR_oil",
    units="1",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"oil_urr": 2, "cumulative_total_oil_extraction": 1},
)
def relative_rurr_oil():
    """
    Remaining resources+reserves of oil as a share of the initial availability.
    """
    return (oil_urr() - cumulative_total_oil_extraction()) / oil_urr()


@component.add(
    name="relative_RURR_total_coal",
    units="1",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"coal_urr": 2, "cumulative_coal_extracted": 1},
)
def relative_rurr_total_coal():
    """
    Remaining URR of total coal as a share of the initial availability.
    """
    return (
        sum(coal_urr().rename({"COAL_TYPES_I": "COAL_TYPES_I!"}), dim=["COAL_TYPES_I!"])
        - sum(
            cumulative_coal_extracted().rename({"COAL_TYPES_I": "COAL_TYPES_I!"}),
            dim=["COAL_TYPES_I!"],
        )
    ) / sum(coal_urr().rename({"COAL_TYPES_I": "COAL_TYPES_I!"}), dim=["COAL_TYPES_I!"])


@component.add(
    name="relative_RURR_uranium",
    units="1",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"initial_urr_uranium": 2, "cumulated_uranium_extraction": 1},
)
def relative_rurr_uranium():
    """
    Remaining resources+reserves of coal as a share of the initial availability.
    """
    return (
        initial_urr_uranium() - cumulated_uranium_extraction()
    ) / initial_urr_uranium()


@component.add(
    name="TOTAL_INITIAL_Al_URR",
    units="Mt",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"initial_al_hidden_resources": 1, "initial_al_known_reserves": 1},
)
def total_initial_al_urr():
    """
    initial availability of resources+reserves of aluminium
    """
    return sum(
        initial_al_hidden_resources().rename({"Al_ORE_GRADES_I": "Al_ORE_GRADES_I!"})
        + initial_al_known_reserves().rename({"Al_ORE_GRADES_I": "Al_ORE_GRADES_I!"}),
        dim=["Al_ORE_GRADES_I!"],
    )


@component.add(
    name="TOTAL_INITIAL_Fe_URR",
    units="Mt",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"initial_fe_hidden_resources": 1, "initial_fe_known_reserves": 1},
)
def total_initial_fe_urr():
    """
    initial availability of resources+reserves of Iron
    """
    return sum(
        initial_fe_hidden_resources().rename({"ORE_GRADES_I": "ORE_GRADES_I!"})
        + initial_fe_known_reserves().rename({"ORE_GRADES_I": "ORE_GRADES_I!"}),
        dim=["ORE_GRADES_I!"],
    )


@component.add(
    name="TOTAL_INITIAL_Ni_URR",
    units="Mt",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"initial_ni_hidden_resources": 1, "initial_ni_known_reserves": 1},
)
def total_initial_ni_urr():
    """
    initial availability of resources+reserves of Nickel
    """
    return sum(
        initial_ni_hidden_resources().rename({"ORE_GRADES_I": "ORE_GRADES_I!"})
        + initial_ni_known_reserves().rename({"ORE_GRADES_I": "ORE_GRADES_I!"}),
        dim=["ORE_GRADES_I!"],
    )


@component.add(
    name="uranium_consumption_per_capita",
    units="EJ/(Year*person)",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"uranium_extraction_rate": 1, "world_population": 1},
)
def uranium_consumption_per_capita():
    return zidz(uranium_extraction_rate(), world_population())


@component.add(
    name="uranium_RURR_to_production_ratio",
    units="Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"rurr_uranium": 1, "uranium_extraction_rate": 1},
)
def uranium_rurr_to_production_ratio():
    return zidz(rurr_uranium(), uranium_extraction_rate())
