"""
Module materials.materials_requirements.rest_economy_med
Translated using PySD version 3.10.0
"""


@component.add(
    name="cum_materials_demand_RoE_from_2015",
    units="Mt",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_cum_materials_demand_roe_from_2015": 1},
    other_deps={
        "_integ_cum_materials_demand_roe_from_2015": {
            "initial": {},
            "step": {"materials_demand_by_roe_from_2015": 1},
        }
    },
)
def cum_materials_demand_roe_from_2015():
    return _integ_cum_materials_demand_roe_from_2015()


_integ_cum_materials_demand_roe_from_2015 = Integ(
    lambda: materials_demand_by_roe_from_2015(),
    lambda: xr.DataArray(
        0,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "MATERIALS_I": _subscript_dict["MATERIALS_I"],
        },
        ["REGIONS_9_I", "MATERIALS_I"],
    ),
    "_integ_cum_materials_demand_roe_from_2015",
)


@component.add(
    name="cum_materials_to_extract_RoE_from_2015",
    units="Mt",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_cum_materials_to_extract_roe_from_2015": 1},
    other_deps={
        "_integ_cum_materials_to_extract_roe_from_2015": {
            "initial": {},
            "step": {"materials_to_extract_roe_from_2015": 1},
        }
    },
)
def cum_materials_to_extract_roe_from_2015():
    """
    Cumulative materials to be mined for the rest of the economy from 2015.
    """
    return _integ_cum_materials_to_extract_roe_from_2015()


_integ_cum_materials_to_extract_roe_from_2015 = Integ(
    lambda: materials_to_extract_roe_from_2015(),
    lambda: xr.DataArray(
        0,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "MATERIALS_I": _subscript_dict["MATERIALS_I"],
        },
        ["REGIONS_9_I", "MATERIALS_I"],
    ),
    "_integ_cum_materials_to_extract_roe_from_2015",
)


@component.add(
    name="cum_materials_to_extract_RoE_from_initial_year",
    units="Mt",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_cum_materials_to_extract_roe_from_initial_year": 1},
    other_deps={
        "_integ_cum_materials_to_extract_roe_from_initial_year": {
            "initial": {},
            "step": {"materials_to_extract_roe": 1},
        }
    },
)
def cum_materials_to_extract_roe_from_initial_year():
    """
    Cumulative materials to be mined for the rest of the economy.
    """
    return _integ_cum_materials_to_extract_roe_from_initial_year()


_integ_cum_materials_to_extract_roe_from_initial_year = Integ(
    lambda: materials_to_extract_roe(),
    lambda: xr.DataArray(
        0,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "MATERIALS_I": _subscript_dict["MATERIALS_I"],
        },
        ["REGIONS_9_I", "MATERIALS_I"],
    ),
    "_integ_cum_materials_to_extract_roe_from_initial_year",
)


@component.add(
    name="Demand_projection_materials_RoE",
    units="Mt",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_demand_projection_materials_roe": 1},
    other_deps={
        "_integ_demand_projection_materials_roe": {
            "initial": {
                "initial_mineral_consumption_roe": 1,
                "matrix_unit_prefixes": 1,
            },
            "step": {"variation_demand_materials_roe": 1},
        }
    },
)
def demand_projection_materials_roe():
    """
    Projection of the demand of minerals by the rest of the economy.
    """
    return _integ_demand_projection_materials_roe()


_integ_demand_projection_materials_roe = Integ(
    lambda: variation_demand_materials_roe(),
    lambda: initial_mineral_consumption_roe()
    * float(matrix_unit_prefixes().loc["BASE_UNIT", "mega"]),
    "_integ_demand_projection_materials_roe",
)


@component.add(
    name="Historical_variation_materials_consumption_RoE",
    units="tonnes",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 2,
        "historical_consumption_materials_roe": 2,
        "number_of_regions": 1,
    },
)
def historical_variation_materials_consumption_roe():
    """
    Historical variation (yearly) in the consumption of minerals by the rest of the economy.
    """
    return (
        (
            historical_consumption_materials_roe(time() + 1)
            - historical_consumption_materials_roe(time())
        )
        / number_of_regions()
    ).expand_dims({"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, 0)


@component.add(
    name="Materials_demand_by_RoE_from_2015",
    units="Mt",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "demand_projection_materials_roe": 1},
)
def materials_demand_by_roe_from_2015():
    """
    Materials demand by the rest of the economy from 2015
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
        lambda: demand_projection_materials_roe(),
    )


@component.add(
    name="Materials_extraction_demand_RoE",
    units="Mt",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "demand_projection_materials_roe": 1,
        "eol_recycling_rates_minerals_rest": 1,
    },
)
def materials_extraction_demand_roe():
    """
    Minerals extraction demand projection of the rest of the economy accounting for the dynamic evolution of recycling rates.
    """
    return demand_projection_materials_roe() * (1 - eol_recycling_rates_minerals_rest())


@component.add(
    name="Materials_to_extract_RoE",
    units="Mt/Year",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"materials_extraction_demand_roe": 1},
)
def materials_to_extract_roe():
    """
    Annual materials to be mined for the rest of the economy.
    """
    return materials_extraction_demand_roe()


@component.add(
    name="Materials_to_extract_RoE_from_2015",
    units="Mt/Year",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "materials_to_extract_roe": 1},
)
def materials_to_extract_roe_from_2015():
    """
    Annual materials to be mined for the ithe rest of the economy from 2015.
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
        lambda: materials_to_extract_roe(),
    )


@component.add(
    name="Total_recycled_materials_RoE",
    units="Mt",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "demand_projection_materials_roe": 1,
        "materials_extraction_demand_roe": 1,
    },
)
def total_recycled_materials_roe():
    """
    Total recycled materials rest of the economy.
    """
    return demand_projection_materials_roe() - materials_extraction_demand_roe()


@component.add(
    name="variation_demand_materials_RoE",
    units="Mt",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "historical_variation_materials_consumption_roe": 1,
        "demand_projection_materials_roe": 1,
        "annual_gdp_real_9r_growth": 1,
        "a_demand_projection_materials_roe": 1,
        "matrix_unit_prefixes": 1,
    },
)
def variation_demand_materials_roe():
    """
    Variation of demand of minerals by the rest of the economy.
    """
    return if_then_else(
        time() < 2015,
        lambda: historical_variation_materials_consumption_roe(),
        lambda: if_then_else(
            demand_projection_materials_roe() > 0.01,
            lambda: (
                a_demand_projection_materials_roe() * annual_gdp_real_9r_growth()
            ).transpose("REGIONS_9_I", "MATERIALS_I"),
            lambda: xr.DataArray(
                0,
                {
                    "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                    "MATERIALS_I": _subscript_dict["MATERIALS_I"],
                },
                ["REGIONS_9_I", "MATERIALS_I"],
            ),
        ),
    ) * float(matrix_unit_prefixes().loc["BASE_UNIT", "mega"])
