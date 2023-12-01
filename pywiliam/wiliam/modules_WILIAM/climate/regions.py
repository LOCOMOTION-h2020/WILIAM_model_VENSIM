"""
Module climate.regions
Translated using PySD version 3.10.0
"""


@component.add(
    name="CLIMATE_ZONES_PERC_BY_REGION",
    units="percent",
    subscripts=["CLIMATIC_ZONES_I", "REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_climate_zones_perc_by_region"},
)
def climate_zones_perc_by_region():
    """
    Percentage (%) of climate zones in each LOCOMOTION region.
    """
    return _ext_constant_climate_zones_perc_by_region()


_ext_constant_climate_zones_perc_by_region = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "climate_percentages",
    {
        "CLIMATIC_ZONES_I": _subscript_dict["CLIMATIC_ZONES_I"],
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
    },
    _root,
    {
        "CLIMATIC_ZONES_I": _subscript_dict["CLIMATIC_ZONES_I"],
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
    },
    "_ext_constant_climate_zones_perc_by_region",
)


@component.add(
    name="SLOPE_VALUE_RoE",
    units="DegreesC/DegreesC",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_slope_value_roe"},
)
def slope_value_roe():
    """
    Slope (b) from linear regression results for local average temperature as a function of global mean surface temperature, in the Rest of the World (RoE); non-Locomotion regions, i.e., oceans, seas and Antarctica
    """
    return _ext_constant_slope_value_roe()


_ext_constant_slope_value_roe = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "slopeRoE",
    {},
    _root,
    {},
    "_ext_constant_slope_value_roe",
)


@component.add(
    name="SLOPE_VALUES_BY_35REGIONS",
    units="DegreesC/DegreesC",
    subscripts=["REGIONS_35_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_slope_values_by_35regions"},
)
def slope_values_by_35regions():
    """
    Slope (b) from linear regression results per countries and WILIAM regions (35 in total) for local average temperature as a function of global mean surface temperature
    """
    return _ext_constant_slope_values_by_35regions()


_ext_constant_slope_values_by_35regions = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "climate_35slopes",
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    _root,
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    "_ext_constant_slope_values_by_35regions",
)


@component.add(
    name="SLOPE_VALUES_BY_CLIMATE_AND_REGIONS",
    units="DegreesC/DegreesC",
    subscripts=["CLIMATIC_ZONES_I", "REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_slope_values_by_climate_and_regions"},
)
def slope_values_by_climate_and_regions():
    """
    Slope (b) from linear regression results per climate zones and WILIAM regions for local average temperature as a function of global mean surface temperature
    """
    return _ext_constant_slope_values_by_climate_and_regions()


_ext_constant_slope_values_by_climate_and_regions = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "climate_slopes",
    {
        "CLIMATIC_ZONES_I": _subscript_dict["CLIMATIC_ZONES_I"],
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
    },
    _root,
    {
        "CLIMATIC_ZONES_I": _subscript_dict["CLIMATIC_ZONES_I"],
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
    },
    "_ext_constant_slope_values_by_climate_and_regions",
)


@component.add(
    name="temperature_change_by_region_and_climate",
    units="DegreesC",
    subscripts=["CLIMATIC_ZONES_I", "REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"slope_values_by_climate_and_regions": 1, "temperature_change": 1},
)
def temperature_change_by_region_and_climate():
    """
    Change in temperature depend by region and climate.
    """
    return slope_values_by_climate_and_regions() * temperature_change()


@component.add(
    name="temperature_change_in9regions",
    units="DegreesC",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "weighted_temperature_change_by_region_and_climate": 2,
        "temperature_change_amoc_weakening": 1,
    },
)
def temperature_change_in9regions():
    """
    Temperature change for the 9 LOCOMOTION Regions. Computed using the climate values for each region.
    """
    return if_then_else(
        time() > 2080,
        lambda: sum(
            weighted_temperature_change_by_region_and_climate().rename(
                {"CLIMATIC_ZONES_I": "CLIMATIC_ZONES_I!"}
            ),
            dim=["CLIMATIC_ZONES_I!"],
        )
        + temperature_change_amoc_weakening(),
        lambda: sum(
            weighted_temperature_change_by_region_and_climate().rename(
                {"CLIMATIC_ZONES_I": "CLIMATIC_ZONES_I!"}
            ),
            dim=["CLIMATIC_ZONES_I!"],
        ),
    )


@component.add(
    name="temperature_change_in_35regions",
    units="DegreesC",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"slope_values_by_35regions": 1, "temperature_change": 1},
)
def temperature_change_in_35regions():
    """
    Temperature change in the 35 regions of LOCOMOTION (without climatic zones, only political regions)
    """
    return slope_values_by_35regions() * temperature_change()


@component.add(
    name="temperature_change_RoE",
    units="DegreesC",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"slope_value_roe": 1, "temperature_change": 1},
)
def temperature_change_roe():
    """
    Temperature Change in the Rest of the World (RoE); non-Locomotion regions, i.e., oceans, seas and Antarctica
    """
    return slope_value_roe() * temperature_change()


@component.add(
    name="weighted_temperature_change_by_region_and_climate",
    units="DegreesC",
    subscripts=["CLIMATIC_ZONES_I", "REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "temperature_change_by_region_and_climate": 1,
        "climate_zones_perc_by_region": 1,
    },
)
def weighted_temperature_change_by_region_and_climate():
    """
    Climate temperature values vs climate zones,in percentage (divide by 100 to correct values of percentage). Returns a matrix with the values by Region and by climate in each region
    """
    return (
        temperature_change_by_region_and_climate()
        * climate_zones_perc_by_region()
        / 100
    )
