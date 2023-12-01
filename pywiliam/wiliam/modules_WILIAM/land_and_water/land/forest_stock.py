"""
Module land_and_water.land.forest_stock
Translated using PySD version 3.10.0
"""


@component.add(
    name="annual_growth_rate_of_forest_stocks",
    units="DMNL/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "annual_growth_rate_of_forest_stocks_coefficient_0": 1,
        "annual_growth_rate_of_forest_stocks_coefficient_1": 1,
        "proportion_of_plantations_in_the_total_forest_area": 1,
        "forest_volume_stock_per_unit_area": 1,
        "maximum_forest_stock_per_area": 1,
    },
)
def annual_growth_rate_of_forest_stocks():
    """
    annual growth rate of forest stocks
    """
    return (
        annual_growth_rate_of_forest_stocks_coefficient_0()
        + annual_growth_rate_of_forest_stocks_coefficient_1()
        * proportion_of_plantations_in_the_total_forest_area()
    ) * (1 - zidz(forest_volume_stock_per_unit_area(), maximum_forest_stock_per_area()))


@component.add(
    name="change_of_all_forests_stock",
    units="m3/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "forests_stock_all_forests": 1,
        "historical_forest_volume_stock_all_forests": 1,
        "initial_time": 1,
        "forest_volume_stock_changes": 1,
    },
)
def change_of_all_forests_stock():
    """
    increase of forest volume stock
    """
    return if_then_else(
        forests_stock_all_forests()
        <= 0.08 * historical_forest_volume_stock_all_forests(initial_time()),
        lambda: xr.DataArray(
            0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
        ),
        lambda: forest_volume_stock_changes(),
    )


@component.add(
    name="forest_area_lost_total",
    units="km2/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"land_use_changes_productive_uses": 6},
)
def forest_area_lost_total():
    """
    forest area lost total, >0 means forest are is lost
    """
    return -if_then_else(
        land_use_changes_productive_uses()
        .loc[:, "FOREST_MANAGED"]
        .reset_coords(drop=True)
        + land_use_changes_productive_uses()
        .loc[:, "FOREST_PRIMARY"]
        .reset_coords(drop=True)
        + land_use_changes_productive_uses()
        .loc[:, "FOREST_PLANTATIONS"]
        .reset_coords(drop=True)
        < 0,
        lambda: land_use_changes_productive_uses()
        .loc[:, "FOREST_MANAGED"]
        .reset_coords(drop=True)
        + land_use_changes_productive_uses()
        .loc[:, "FOREST_PRIMARY"]
        .reset_coords(drop=True)
        + land_use_changes_productive_uses()
        .loc[:, "FOREST_PLANTATIONS"]
        .reset_coords(drop=True),
        lambda: xr.DataArray(
            0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
        ),
    )


@component.add(
    name="forest_planetary_boundary_volume",
    units="m3/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"forest_stock_growth": 1, "outturn_of_wood_extraction": 1},
)
def forest_planetary_boundary_volume():
    """
    forestry planetary boundary
    """
    return forest_stock_growth() * outturn_of_wood_extraction()


@component.add(
    name="forest_planetary_boundary_weight",
    units="t/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"forest_planetary_boundary_volume": 1, "wood_density_by_region": 1},
)
def forest_planetary_boundary_weight():
    return forest_planetary_boundary_volume() * wood_density_by_region()


@component.add(
    name="forest_stock_growth",
    units="m3/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "forests_stock_all_forests": 1,
        "annual_growth_rate_of_forest_stocks": 1,
    },
)
def forest_stock_growth():
    """
    forest stock increment
    """
    return forests_stock_all_forests() * annual_growth_rate_of_forest_stocks()


@component.add(
    name="forest_stock_lost_for_deforestation",
    units="m3/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"forest_volume_stock_per_unit_area": 1, "forest_area_lost_total": 1},
)
def forest_stock_lost_for_deforestation():
    return forest_volume_stock_per_unit_area() * forest_area_lost_total()


@component.add(
    name="forest_volume_stock_changes",
    units="m3/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 2,
        "time_historical_data_land_module": 1,
        "historical_forest_volume_stock_change_all_forests": 1,
        "roundwood_volumme_extracted_from_forest_m_and_p": 1,
        "forest_stock_growth": 1,
        "forest_stock_lost_for_deforestation": 1,
    },
)
def forest_volume_stock_changes():
    """
    forest volume stock changes.
    """
    return if_then_else(
        time() <= time_historical_data_land_module(),
        lambda: historical_forest_volume_stock_change_all_forests(time()),
        lambda: forest_stock_growth()
        - roundwood_volumme_extracted_from_forest_m_and_p()
        - forest_stock_lost_for_deforestation(),
    )


@component.add(
    name="forest_volume_stock_per_unit_area",
    units="m3/km2",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"forests_stock_all_forests": 1, "total_forest_area": 1},
)
def forest_volume_stock_per_unit_area():
    """
    forest volume stock per unit area
    """
    return forests_stock_all_forests() / total_forest_area()


@component.add(
    name="forestry_sustainability_index_by_region",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "roundwood_volumme_extracted_from_forest_m_and_p": 1,
        "forest_volume_stock_per_unit_area": 1,
        "forest_area_lost_total": 1,
        "forest_planetary_boundary_volume": 1,
    },
)
def forestry_sustainability_index_by_region():
    """
    forestry sustainability index by region
    """
    return zidz(
        roundwood_volumme_extracted_from_forest_m_and_p()
        + forest_volume_stock_per_unit_area() * np.abs(forest_area_lost_total()),
        forest_planetary_boundary_volume(),
    )


@component.add(
    name="forests_stock_all_forests",
    units="m3",
    subscripts=["REGIONS_9_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_forests_stock_all_forests": 1},
    other_deps={
        "_integ_forests_stock_all_forests": {
            "initial": {
                "initial_time": 1,
                "historical_forest_volume_stock_all_forests": 1,
            },
            "step": {"change_of_all_forests_stock": 1},
        }
    },
)
def forests_stock_all_forests():
    """
    forest volume stock
    """
    return _integ_forests_stock_all_forests()


_integ_forests_stock_all_forests = Integ(
    lambda: change_of_all_forests_stock(),
    lambda: historical_forest_volume_stock_all_forests(initial_time()),
    "_integ_forests_stock_all_forests",
)


@component.add(
    name="forests_stock_all_forests_global",
    units="m3",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"forests_stock_all_forests": 1},
)
def forests_stock_all_forests_global():
    """
    forests_stock_all_forests_global
    """
    return sum(
        forests_stock_all_forests().rename({"REGIONS_9_I": "REGIONS_9_I!"}),
        dim=["REGIONS_9_I!"],
    )


@component.add(
    name="historical_stock_all_forests",
    units="m3",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "historical_forest_volume_stock_all_forests": 1},
)
def historical_stock_all_forests():
    return historical_forest_volume_stock_all_forests(time())


@component.add(
    name="maximum_forest_stock_all_forests",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"maximum_forest_stock_per_area": 1, "total_forest_area": 1},
)
def maximum_forest_stock_all_forests():
    return maximum_forest_stock_per_area() * total_forest_area()


@component.add(
    name="proportion_of_plantations_in_the_total_forest_area",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"land_use_area_by_region": 1, "total_forest_area": 1},
)
def proportion_of_plantations_in_the_total_forest_area():
    """
    proportion of plantations in the total forest area
    """
    return (
        land_use_area_by_region().loc[:, "FOREST_PLANTATIONS"].reset_coords(drop=True)
        / total_forest_area()
    )


@component.add(
    name="share_of_overexploitation_all_forests",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "global_roundwood_demand_distributed_to_regions": 1,
        "forest_planetary_boundary_weight": 1,
    },
)
def share_of_overexploitation_all_forests():
    return zidz(
        global_roundwood_demand_distributed_to_regions(),
        forest_planetary_boundary_weight(),
    )


@component.add(
    name="total_forest_area",
    units="km2",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"land_use_area_by_region": 3},
)
def total_forest_area():
    """
    total forest area
    """
    return (
        land_use_area_by_region().loc[:, "FOREST_MANAGED"].reset_coords(drop=True)
        + land_use_area_by_region().loc[:, "FOREST_PLANTATIONS"].reset_coords(drop=True)
        + land_use_area_by_region().loc[:, "FOREST_PRIMARY"].reset_coords(drop=True)
    )
