"""
Module land_and_water.urban_land
Translated using PySD version 3.10.0
"""


@component.add(
    name="change_of_urban_land_density",
    units="m2/person/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 3,
        "time_historical_data_land_module": 1,
        "change_of_urban_land_density_trends": 2,
        "year_final_urban_land_density_sp": 2,
        "objective_urban_land_density_sp": 1,
        "year_initial_urban_land_density_sp": 2,
        "urban_land_density_trends": 1,
        "switch_urban_land_density_sp": 1,
    },
)
def change_of_urban_land_density():
    """
    IF_THEN_ELSE( Time<TIME_HISTORICAL_DATA_LAND_MODULE, change_of_urban_land_density_trends[REGIONS_9_I], IF_THEN_ELSE( SWITCH_URBAN_LAND_DENSITY_SP[REGIONS_9_I]=1:AND:Time>YEAR_INITIAL_URBAN_LAN D_DENSITY_SP :AND:Time<YEAR_FINAL_URBAN_LAND_DENSITY_SP ,(OBJECTIVE_URBAN_LAND_DENSITY_SP[REGIONS_9_I]-urban_land_density_trends[REGIONS_9_I] )/(YEAR_FINAL_URBAN_LAND_DENSITY_SP-YEAR_INITIAL_URBAN_LAND_DENSITY_SP ) , change_of_urban_land_density_trends[REGIONS_9_I] ) )
    """
    return if_then_else(
        time() < time_historical_data_land_module(),
        lambda: change_of_urban_land_density_trends(),
        lambda: if_then_else(
            np.logical_and(
                switch_urban_land_density_sp() == 1,
                np.logical_and(
                    time() > year_initial_urban_land_density_sp(),
                    time() < year_final_urban_land_density_sp(),
                ),
            ),
            lambda: (objective_urban_land_density_sp() - urban_land_density_trends())
            / (
                year_final_urban_land_density_sp()
                - year_initial_urban_land_density_sp()
            ),
            lambda: change_of_urban_land_density_trends(),
        ),
    )


@component.add(
    name="change_of_urban_land_density_trends",
    units="m2/person",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"urban_land_density_trends": 1, "delayed_urban_land_density": 1},
)
def change_of_urban_land_density_trends():
    """
    historical_change_of_urban_land_density
    """
    return urban_land_density_trends() - delayed_urban_land_density()


@component.add(
    name="delayed_urban_land_density",
    units="m2/person",
    subscripts=["REGIONS_9_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_urban_land_density": 1},
    other_deps={
        "_delayfixed_delayed_urban_land_density": {
            "initial": {"initial_urban_land_density": 1},
            "step": {"urban_land_density_trends": 1},
        }
    },
)
def delayed_urban_land_density():
    """
    delayed_urban_land_density
    """
    return _delayfixed_delayed_urban_land_density()


_delayfixed_delayed_urban_land_density = DelayFixed(
    lambda: urban_land_density_trends(),
    lambda: 1,
    lambda: initial_urban_land_density(),
    time_step,
    "_delayfixed_delayed_urban_land_density",
)


@component.add(
    name="historical_data_of_population_with_time",
    units="person",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_landwater": 1,
        "time": 1,
        "exogenous_population_9r": 1,
        "population_9_regions": 1,
    },
)
def historical_data_of_population_with_time():
    """
    Population historical data with variation (LOOKUPS)
    """
    return if_then_else(
        switch_landwater() == 0,
        lambda: exogenous_population_9r(time()),
        lambda: population_9_regions(),
    )


@component.add(
    name="historical_data_of_urban_land_with_time",
    units="km2",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "historical_land_use_by_region": 1},
)
def historical_data_of_urban_land_with_time():
    """
    Urban land historical data with variation (LOOKUPS)
    """
    return (
        historical_land_use_by_region(time())
        .loc[:, "URBAN_LAND"]
        .reset_coords(drop=True)
    )


@component.add(
    name="initial_urban_land_density",
    units="m2/(Year*person)",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_landwater": 1,
        "historical_land_use_by_region": 2,
        "exogenous_population_9r": 1,
        "initial_time": 3,
        "unit_conversion_m2_km2": 2,
        "population_9_regions": 1,
    },
)
def initial_urban_land_density():
    """
    initial_urban_land_density
    """
    return if_then_else(
        switch_landwater() == 0,
        lambda: zidz(
            unit_conversion_m2_km2()
            * historical_land_use_by_region(initial_time())
            .loc[:, "URBAN_LAND"]
            .reset_coords(drop=True),
            exogenous_population_9r(initial_time()),
        ),
        lambda: zidz(
            unit_conversion_m2_km2()
            * historical_land_use_by_region(initial_time())
            .loc[:, "URBAN_LAND"]
            .reset_coords(drop=True),
            population_9_regions(),
        ),
    )


@component.add(
    name="urban_land_density",
    units="m2/person",
    subscripts=["REGIONS_9_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_urban_land_density": 1},
    other_deps={
        "_integ_urban_land_density": {
            "initial": {"initial_urban_land_density": 1},
            "step": {"change_of_urban_land_density": 1},
        }
    },
)
def urban_land_density():
    """
    the urban land density by region
    """
    return _integ_urban_land_density()


_integ_urban_land_density = Integ(
    lambda: change_of_urban_land_density(),
    lambda: initial_urban_land_density(),
    "_integ_urban_land_density",
)


@component.add(
    name="urban_land_density_trends",
    units="m2/person",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "historical_data_of_urban_land_with_time": 1,
        "unit_conversion_m2_km2": 1,
        "historical_data_of_population_with_time": 1,
    },
)
def urban_land_density_trends():
    """
    Urban land density historical data by region
    """
    return (
        historical_data_of_urban_land_with_time() * unit_conversion_m2_km2()
    ) / historical_data_of_population_with_time()
