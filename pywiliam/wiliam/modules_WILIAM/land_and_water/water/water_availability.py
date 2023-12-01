"""
Module land_and_water.water.water_availability
Translated using PySD version 3.10.0
"""


@component.add(
    name="aux_ratio_precipitation_evapotranspiration_by_year",
    units="DMNL",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "precipitation_evapotranspiration_projections": 1,
        "initial_precipitation_evapotranspiration_by_region": 1,
    },
)
def aux_ratio_precipitation_evapotranspiration_by_year():
    return (
        precipitation_evapotranspiration_projections()
        / initial_precipitation_evapotranspiration_by_region()
    )


@component.add(
    name="initial_water_available_hm3",
    units="hm3",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"initial_total_renewable_water_by_region": 1},
)
def initial_water_available_hm3():
    return 1000 * initial_total_renewable_water_by_region()


@component.add(
    name="precipitation_evapotranspiration_projections",
    units="DMNL",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_landwater": 1,
        "first_factor_water_equation": 2,
        "second_factor_water_equation": 2,
        "global_temperature_change_2015": 1,
        "temperature_change": 1,
    },
)
def precipitation_evapotranspiration_projections():
    """
    Water availability values,from Distefano and Kelly (2017), for the end of the century (2080), for the 35 regions and 4 RCP scenarios.
    """
    return if_then_else(
        switch_landwater() == 0,
        lambda: first_factor_water_equation() * np.log(global_temperature_change_2015())
        + second_factor_water_equation(),
        lambda: first_factor_water_equation() * np.log(temperature_change())
        + second_factor_water_equation(),
    )


@component.add(
    name="ratio_precipitation_evapotranspiration_by_year",
    units="DMNL",
    subscripts=["REGIONS_36_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"aux_ratio_precipitation_evapotranspiration_by_year": 2},
)
def ratio_precipitation_evapotranspiration_by_year():
    value = xr.DataArray(
        np.nan, {"REGIONS_36_I": _subscript_dict["REGIONS_36_I"]}, ["REGIONS_36_I"]
    )
    value.loc[["EU27"]] = zidz(
        sum(
            aux_ratio_precipitation_evapotranspiration_by_year()
            .loc[_subscript_dict["REGIONS_EU27_I"]]
            .rename({"REGIONS_35_I": "REGIONS_EU27_I!"}),
            dim=["REGIONS_EU27_I!"],
        ),
        27,
    )
    value.loc[
        _subscript_dict["REGIONS_35_I"]
    ] = aux_ratio_precipitation_evapotranspiration_by_year().values
    return value


@component.add(
    name="water_available_by_region",
    units="hm3",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "initial_total_renewable_water_by_region": 1,
        "maximum_exploitation_water_coefficient": 1,
        "precipitation_evapotranspiration_projections": 1,
        "initial_precipitation_evapotranspiration_by_region": 1,
        "unit_conversion_km3_hm3": 1,
    },
)
def water_available_by_region():
    """
    Availability of water changing in time, for the 35 regions
    """
    return (
        initial_total_renewable_water_by_region()
        * maximum_exploitation_water_coefficient()
        * precipitation_evapotranspiration_projections()
        / initial_precipitation_evapotranspiration_by_region()
    ) / unit_conversion_km3_hm3()


@component.add(
    name="water_stress_9R",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"water_stress_9r_calculation": 2, "water_stress_average_eu27": 1},
)
def water_stress_9r():
    """
    water_stress_9R
    """
    return if_then_else(
        water_stress_9r_calculation() > 100,
        lambda: xr.DataArray(
            water_stress_average_eu27(),
            {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
            ["REGIONS_9_I"],
        ),
        lambda: water_stress_9r_calculation(),
    )


@component.add(
    name="water_stress_9R_calculation",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"water_stress_region_matrix": 1},
)
def water_stress_9r_calculation():
    return sum(
        water_stress_region_matrix().rename({"REGIONS_35_I": "REGIONS_35_I!"}),
        dim=["REGIONS_35_I!"],
    )


@component.add(
    name="water_stress_average_EU27",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"water_stress_by_region": 27},
)
def water_stress_average_eu27():
    return (
        float(water_stress_by_region().loc["AUSTRIA"])
        + float(water_stress_by_region().loc["BELGIUM"])
        + float(water_stress_by_region().loc["BULGARIA"])
        + float(water_stress_by_region().loc["CROATIA"])
        + float(water_stress_by_region().loc["CYPRUS"])
        + float(water_stress_by_region().loc["CZECH_REPUBLIC"])
        + float(water_stress_by_region().loc["DENMARK"])
        + float(water_stress_by_region().loc["ESTONIA"])
        + float(water_stress_by_region().loc["FINLAND"])
        + float(water_stress_by_region().loc["FRANCE"])
        + float(water_stress_by_region().loc["GERMANY"])
        + float(water_stress_by_region().loc["GREECE"])
        + float(water_stress_by_region().loc["HUNGARY"])
        + float(water_stress_by_region().loc["IRELAND"])
        + float(water_stress_by_region().loc["ITALY"])
        + float(water_stress_by_region().loc["LATVIA"])
        + float(water_stress_by_region().loc["LITHUANIA"])
        + float(water_stress_by_region().loc["LUXEMBOURG"])
        + float(water_stress_by_region().loc["MALTA"])
        + float(water_stress_by_region().loc["NETHERLANDS"])
        + float(water_stress_by_region().loc["POLAND"])
        + float(water_stress_by_region().loc["PORTUGAL"])
        + float(water_stress_by_region().loc["ROMANIA"])
        + float(water_stress_by_region().loc["SLOVAKIA"])
        + float(water_stress_by_region().loc["SLOVENIA"])
        + float(water_stress_by_region().loc["SPAIN"])
        + float(water_stress_by_region().loc["SWEDEN"])
    ) / 27


@component.add(
    name="water_stress_by_region",
    units="DMNL",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_demand_blue_water_by_region": 1, "water_available_by_region": 1},
)
def water_stress_by_region():
    """
    water_stress_by_region
    """
    return (total_demand_blue_water_by_region() / water_available_by_region()) * 100


@component.add(
    name="water_stress_region_matrix",
    units="DMNL",
    subscripts=["REGIONS_35_I", "REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"water_stress_by_region": 1, "matrix_country_region": 1},
)
def water_stress_region_matrix():
    return water_stress_by_region() * matrix_country_region()
