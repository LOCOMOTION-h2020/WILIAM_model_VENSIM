"""
Module land_and_water.land.ghg_emissions_luc
Translated using PySD version 3.10.0
"""


@component.add(
    name="area_of_managed_and_primary_forest",
    units="ha",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_law_emissions_land_use_productive_area": 1,
        "switch_law_emissions": 1,
        "exo_land_use_area_productive_uses_t": 1,
        "land_use_area_productive_uses": 2,
    },
)
def area_of_managed_and_primary_forest():
    """
    Area of managed and primary forest by region
    """
    return if_then_else(
        np.logical_or(
            switch_law_emissions_land_use_productive_area() == 0,
            switch_law_emissions() == 0,
        ),
        lambda: exo_land_use_area_productive_uses_t()
        .loc[:, "FOREST_PRIMARY"]
        .reset_coords(drop=True),
        lambda: land_use_area_productive_uses()
        .loc[:, "FOREST_MANAGED"]
        .reset_coords(drop=True)
        + land_use_area_productive_uses()
        .loc[:, "FOREST_PRIMARY"]
        .reset_coords(drop=True),
    )


@component.add(
    name="C_check_emissions_LUC_cropland_management",
    units="t/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "c_landuse1_to_landuse2_emissions": 1,
        "c_checksoil_emissions_cropland_management_delayed": 1,
        "unit_conversion_t_gt": 1,
    },
)
def c_check_emissions_luc_cropland_management():
    """
    Sum by region ***To be programmed: include the exception of emissions due to afforestation (land use2 = forest)that will come from "forest vensim view". This emissions are instataneous (except the carbon uptake by afforestation: from forest vensim view, and the carbon uptake from cropland to grassland (this last still to be programmed--> default time of 20 years which corresponds to a delay time of 5 years )
    """
    return (
        c_landuse1_to_landuse2_emissions()
        + c_checksoil_emissions_cropland_management_delayed()
    ) / unit_conversion_t_gt()


@component.add(
    name="C_checksoil_emissions_cropland_management_delayed",
    units="t/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"soil_emissions_cropland_management_delayed": 1},
)
def c_checksoil_emissions_cropland_management_delayed():
    """
    SUM of soil emission
    """
    return sum(
        soil_emissions_cropland_management_delayed().rename(
            {"REGIONS_9_I": "REGIONS_9_I!"}
        ),
        dim=["REGIONS_9_I!"],
    )


@component.add(
    name="C_landuse1_to_landuse2_emissions",
    units="t/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"c_landuse1_to_landuse2_emissions_region": 1},
)
def c_landuse1_to_landuse2_emissions():
    """
    Sum by region ***To be programmed: include the exception of emissions due to afforestation (land use2 = forest)that will come from "forest vensim view". This emissions are instataneous (except the carbon uptake by afforestation: from forest vensim view, and the carbon uptake from cropland to grassland (this last still to be programmed--> default time of 20 years which corresponds to a delay time of 5 years )
    """
    return sum(
        c_landuse1_to_landuse2_emissions_region().rename(
            {"REGIONS_9_I": "REGIONS_9_I!"}
        ),
        dim=["REGIONS_9_I!"],
    )


@component.add(
    name="C_landuse1_to_landuse2_emissions_region",
    units="t/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "vegetation_emissions_landuse1_to_landuse2_byregion": 1,
        "soil_emissions_landuse1_to_landuse2_byregion": 1,
    },
)
def c_landuse1_to_landuse2_emissions_region():
    """
    Sum by region ***To be linked with forest module: include the exception of emissions due to afforestation (land use2 = forest)that will come from "forest vensim view". ***To be included some delays: This emissions are instataneous (except the carbon uptake by afforestation: from forest vensim view, and the carbon uptake from cropland to grassland (this last still to be programmed--> default time of 20 years which corresponds to a delay time of 5 years )
    """
    return (
        vegetation_emissions_landuse1_to_landuse2_byregion()
        + soil_emissions_landuse1_to_landuse2_byregion()
    )


@component.add(
    name="carbon_density_cropland_region",
    units="tC/ha",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "soil_carbon_density_cropland_region": 1,
        "share_area_rainfed_cropland": 2,
        "vegetation_carbon_density_data_by_land_use": 2,
    },
)
def carbon_density_cropland_region():
    """
    Carbon density of cropland for each region ** From now the carbon density by type of crop is deactivated,and average value for all region are applied (soil carbon density default values) TO BE CHANGED.
    """
    return (
        soil_carbon_density_cropland_region()
        + vegetation_carbon_density_data_by_land_use()
        .loc[:, "CROPLAND_RAINFED"]
        .reset_coords(drop=True)
        * share_area_rainfed_cropland()
        + vegetation_carbon_density_data_by_land_use()
        .loc[:, "CROPLAND_IRRIGATED"]
        .reset_coords(drop=True)
        * (1 - share_area_rainfed_cropland())
    )


@component.add(
    name="carbon_density_grassland_climate_zone",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "soil_carbon_density_grassland_region": 1,
        "vegetation_carbon_density_grassland_region": 1,
    },
)
def carbon_density_grassland_climate_zone():
    """
    Carbon density of grassland for each region
    """
    return (
        soil_carbon_density_grassland_region()
        + vegetation_carbon_density_grassland_region()
    )


@component.add(
    name="carbon_stock_in_managed_and_primary_forests",
    comp_type="Constant",
    comp_subtype="Normal",
)
def carbon_stock_in_managed_and_primary_forests():
    """
    **TODO: calculate forest carbon density based on the forest module.
    """
    return 0


@component.add(
    name="cropland_total_area_by_region",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_law_emissions_land_use_productive_area": 1,
        "switch_law_emissions": 1,
        "exo_land_use_area_productive_uses_t": 2,
        "land_use_area_productive_uses": 2,
    },
)
def cropland_total_area_by_region():
    """
    area of cropland (by region)
    """
    return if_then_else(
        np.logical_or(
            switch_law_emissions_land_use_productive_area() == 0,
            switch_law_emissions() == 0,
        ),
        lambda: exo_land_use_area_productive_uses_t()
        .loc[:, "CROPLAND_RAINFED"]
        .reset_coords(drop=True)
        + exo_land_use_area_productive_uses_t()
        .loc[:, "CROPLAND_IRRIGATED"]
        .reset_coords(drop=True),
        lambda: land_use_area_productive_uses()
        .loc[:, "CROPLAND_RAINFED"]
        .reset_coords(drop=True)
        + land_use_area_productive_uses()
        .loc[:, "CROPLAND_IRRIGATED"]
        .reset_coords(drop=True),
    )


@component.add(
    name="delayed_soil_carbon_stock_cropland_region",
    units="tC/ha",
    subscripts=["REGIONS_9_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_soil_carbon_stock_cropland_region": 1},
    other_deps={
        "_delayfixed_delayed_soil_carbon_stock_cropland_region": {
            "initial": {"soil_carbon_density_cropland_region": 1},
            "step": {"soil_carbon_density_cropland_region": 1},
        }
    },
)
def delayed_soil_carbon_stock_cropland_region():
    """
    soil carbon stock density in cropland the previous year NOTES: *check as the time step is 0,25 and the time delayed is 1 year (the effects seem to be just "smooth" the maximum)
    """
    return _delayfixed_delayed_soil_carbon_stock_cropland_region()


_delayfixed_delayed_soil_carbon_stock_cropland_region = DelayFixed(
    lambda: soil_carbon_density_cropland_region(),
    lambda: 1,
    lambda: soil_carbon_density_cropland_region(),
    time_step,
    "_delayfixed_delayed_soil_carbon_stock_cropland_region",
)


@component.add(
    name="delayed_soil_carbon_stock_grassland_climate_zone",
    units="tC/ha",
    subscripts=["REGIONS_9_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_soil_carbon_stock_grassland_climate_zone": 1},
    other_deps={
        "_delayfixed_delayed_soil_carbon_stock_grassland_climate_zone": {
            "initial": {"soil_carbon_density_grassland_region": 1},
            "step": {"soil_carbon_density_grassland_region": 1},
        }
    },
)
def delayed_soil_carbon_stock_grassland_climate_zone():
    return _delayfixed_delayed_soil_carbon_stock_grassland_climate_zone()


_delayfixed_delayed_soil_carbon_stock_grassland_climate_zone = DelayFixed(
    lambda: soil_carbon_density_grassland_region(),
    lambda: 1,
    lambda: soil_carbon_density_grassland_region(),
    time_step,
    "_delayfixed_delayed_soil_carbon_stock_grassland_climate_zone",
)


@component.add(
    name="exo_land_use_area_productive_uses_t",
    units="km2",
    subscripts=["REGIONS_9_I", "LANDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "exo_land_use_area_productive_uses": 1},
)
def exo_land_use_area_productive_uses_t():
    """
    exogenous information from siulation
    """
    return exo_land_use_area_productive_uses(time())


@component.add(
    name="exo_pv_land_occupation_ratio_t",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "exo_pv_land_occupation_ratio": 1},
)
def exo_pv_land_occupation_ratio_t():
    """
    exogenous information from siulation
    """
    return exo_pv_land_occupation_ratio(time())


@component.add(
    name="exo_share_area_rice_cropland_t",
    units="km2",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "exo_share_area_rice_cropland": 1},
)
def exo_share_area_rice_cropland_t():
    """
    exogenous information from siulation
    """
    return exo_share_area_rice_cropland(time())


@component.add(
    name="exo_share_of_agriculture_in_transition_t",
    units="km2",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "exo_share_of_agriculture_in_transition": 1},
)
def exo_share_of_agriculture_in_transition_t():
    """
    exogenous information from siulation
    """
    return exo_share_of_agriculture_in_transition(time())


@component.add(
    name="exo_share_of_industrial_agriculture_t",
    units="km2",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "exo_share_of_industrial_agriculture": 1},
)
def exo_share_of_industrial_agriculture_t():
    """
    exogenous information from siulation
    """
    return exo_share_of_industrial_agriculture(time())


@component.add(
    name="exo_share_of_low_input_agriculture_t",
    units="km2",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "exo_share_of_low_input_agriculture": 1},
)
def exo_share_of_low_input_agriculture_t():
    """
    exogenous information from siulation
    """
    return exo_share_of_low_input_agriculture(time())


@component.add(
    name="exo_share_of_regenerative_agriculture_t",
    units="km2",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "exo_share_of_regenerative_agriculture": 1},
)
def exo_share_of_regenerative_agriculture_t():
    """
    exogenous information from siulation
    """
    return exo_share_of_regenerative_agriculture(time())


@component.add(
    name="exo_share_of_traditional_agriculture_t",
    units="km2",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "exo_share_of_traditional_agriculture": 1},
)
def exo_share_of_traditional_agriculture_t():
    """
    exogenous information from siulation
    """
    return exo_share_of_traditional_agriculture(time())


@component.add(
    name="factor_emission_soil_landuse_to_landuse2",
    units="tC/ha",
    subscripts=["LANDS_I", "LANDS_MAP_I", "REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"soil_carbon_density_data_by_land_use": 18},
)
def factor_emission_soil_landuse_to_landuse2():
    """
    Carbon stock change factors in each position of the matrix: (Equation applied: soil_carbondensity_landuse2 - soil_carbondensity_landuse1) from land use LANDS_I (down) to land use LANDS_MAP_I (right) If factor emission is positive this means that the change of land use emits (e.g. from forest land to cropland). If factor emissions is negative(carbon stock change positive) means that this es "carbon uptake) -------------------------------------- to modify-equation **TODO:include also here the variability of landuse1 to landuse2 being landuse2= solarland (the final carbon density depends on the previous land use, i.e., on landuse1)
    """
    value = xr.DataArray(
        np.nan,
        {
            "LANDS_I": _subscript_dict["LANDS_I"],
            "LANDS_MAP_I": _subscript_dict["LANDS_MAP_I"],
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        },
        ["LANDS_I", "LANDS_MAP_I", "REGIONS_9_I"],
    )
    value.loc[:, :, ["EU27"]] = (
        (
            soil_carbon_density_data_by_land_use()
            .loc["EU27", :]
            .reset_coords(drop=True)
            - soil_carbon_density_data_by_land_use()
            .loc["EU27", :]
            .reset_coords(drop=True)
            .rename({"LANDS_I": "LANDS_MAP_I"})
        )
        .expand_dims({"REGIONS_36_I": ["EU27"]}, 2)
        .values
    )
    value.loc[:, :, ["UK"]] = (
        (
            soil_carbon_density_data_by_land_use().loc["UK", :].reset_coords(drop=True)
            - soil_carbon_density_data_by_land_use()
            .loc["UK", :]
            .reset_coords(drop=True)
            .rename({"LANDS_I": "LANDS_MAP_I"})
        )
        .expand_dims({"REGIONS_35_I": ["UK"]}, 2)
        .values
    )
    value.loc[:, :, ["CHINA"]] = (
        (
            soil_carbon_density_data_by_land_use()
            .loc["CHINA", :]
            .reset_coords(drop=True)
            - soil_carbon_density_data_by_land_use()
            .loc["CHINA", :]
            .reset_coords(drop=True)
            .rename({"LANDS_I": "LANDS_MAP_I"})
        )
        .expand_dims({"REGIONS_35_I": ["CHINA"]}, 2)
        .values
    )
    value.loc[:, :, ["EASOC"]] = (
        (
            soil_carbon_density_data_by_land_use()
            .loc["EASOC", :]
            .reset_coords(drop=True)
            - soil_carbon_density_data_by_land_use()
            .loc["EASOC", :]
            .reset_coords(drop=True)
            .rename({"LANDS_I": "LANDS_MAP_I"})
        )
        .expand_dims({"REGIONS_35_I": ["EASOC"]}, 2)
        .values
    )
    value.loc[:, :, ["INDIA"]] = (
        (
            soil_carbon_density_data_by_land_use()
            .loc["INDIA", :]
            .reset_coords(drop=True)
            - soil_carbon_density_data_by_land_use()
            .loc["INDIA", :]
            .reset_coords(drop=True)
            .rename({"LANDS_I": "LANDS_MAP_I"})
        )
        .expand_dims({"REGIONS_35_I": ["INDIA"]}, 2)
        .values
    )
    value.loc[:, :, ["LATAM"]] = (
        (
            soil_carbon_density_data_by_land_use()
            .loc["LATAM", :]
            .reset_coords(drop=True)
            - soil_carbon_density_data_by_land_use()
            .loc["LATAM", :]
            .reset_coords(drop=True)
            .rename({"LANDS_I": "LANDS_MAP_I"})
        )
        .expand_dims({"REGIONS_35_I": ["LATAM"]}, 2)
        .values
    )
    value.loc[:, :, ["RUSSIA"]] = (
        (
            soil_carbon_density_data_by_land_use()
            .loc["RUSSIA", :]
            .reset_coords(drop=True)
            - soil_carbon_density_data_by_land_use()
            .loc["RUSSIA", :]
            .reset_coords(drop=True)
            .rename({"LANDS_I": "LANDS_MAP_I"})
        )
        .expand_dims({"REGIONS_35_I": ["RUSSIA"]}, 2)
        .values
    )
    value.loc[:, :, ["USMCA"]] = (
        (
            soil_carbon_density_data_by_land_use()
            .loc["USMCA", :]
            .reset_coords(drop=True)
            - soil_carbon_density_data_by_land_use()
            .loc["USMCA", :]
            .reset_coords(drop=True)
            .rename({"LANDS_I": "LANDS_MAP_I"})
        )
        .expand_dims({"REGIONS_35_I": ["USMCA"]}, 2)
        .values
    )
    value.loc[:, :, ["LROW"]] = (
        (
            soil_carbon_density_data_by_land_use()
            .loc["LROW", :]
            .reset_coords(drop=True)
            - soil_carbon_density_data_by_land_use()
            .loc["LROW", :]
            .reset_coords(drop=True)
            .rename({"LANDS_I": "LANDS_MAP_I"})
        )
        .expand_dims({"REGIONS_35_I": ["LROW"]}, 2)
        .values
    )
    return value


@component.add(
    name="factor_emission_vegetation_landuse_to_landuse2",
    units="tC/ha",
    subscripts=["LANDS_I", "LANDS_MAP_I", "REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"vegetation_carbon_density_data_by_land_use": 18},
)
def factor_emission_vegetation_landuse_to_landuse2():
    """
    Carbon stock change factors in each position of the matrix: (Equation applied: vegetation_carbondensity_landuse1 - vegetation_carbondensity_landuse2) from land use LANDS_I (down) to land use LANDS_MAP_I (right) If factor emission is positive this means that the change of land use emits (e.g. from forest land to cropland). If factor emissions is negative (carbon stock change positive) means that this es "carbon uptake) -------------------------------------- to modify-equation - To include also here the variability of landuse1 to landuse2 being landuse2= solarland (the final carbon density depends on the previous land use, i.e., on landuse1)
    """
    value = xr.DataArray(
        np.nan,
        {
            "LANDS_I": _subscript_dict["LANDS_I"],
            "LANDS_MAP_I": _subscript_dict["LANDS_MAP_I"],
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        },
        ["LANDS_I", "LANDS_MAP_I", "REGIONS_9_I"],
    )
    value.loc[:, :, ["EU27"]] = (
        (
            vegetation_carbon_density_data_by_land_use()
            .loc["EU27", :]
            .reset_coords(drop=True)
            - vegetation_carbon_density_data_by_land_use()
            .loc["EU27", :]
            .reset_coords(drop=True)
            .rename({"LANDS_I": "LANDS_MAP_I"})
        )
        .expand_dims({"REGIONS_36_I": ["EU27"]}, 2)
        .values
    )
    value.loc[:, :, ["UK"]] = (
        (
            vegetation_carbon_density_data_by_land_use()
            .loc["UK", :]
            .reset_coords(drop=True)
            - vegetation_carbon_density_data_by_land_use()
            .loc["UK", :]
            .reset_coords(drop=True)
            .rename({"LANDS_I": "LANDS_MAP_I"})
        )
        .expand_dims({"REGIONS_35_I": ["UK"]}, 2)
        .values
    )
    value.loc[:, :, ["CHINA"]] = (
        (
            vegetation_carbon_density_data_by_land_use()
            .loc["CHINA", :]
            .reset_coords(drop=True)
            - vegetation_carbon_density_data_by_land_use()
            .loc["CHINA", :]
            .reset_coords(drop=True)
            .rename({"LANDS_I": "LANDS_MAP_I"})
        )
        .expand_dims({"REGIONS_35_I": ["CHINA"]}, 2)
        .values
    )
    value.loc[:, :, ["EASOC"]] = (
        (
            vegetation_carbon_density_data_by_land_use()
            .loc["EASOC", :]
            .reset_coords(drop=True)
            - vegetation_carbon_density_data_by_land_use()
            .loc["EASOC", :]
            .reset_coords(drop=True)
            .rename({"LANDS_I": "LANDS_MAP_I"})
        )
        .expand_dims({"REGIONS_35_I": ["EASOC"]}, 2)
        .values
    )
    value.loc[:, :, ["INDIA"]] = (
        (
            vegetation_carbon_density_data_by_land_use()
            .loc["INDIA", :]
            .reset_coords(drop=True)
            - vegetation_carbon_density_data_by_land_use()
            .loc["INDIA", :]
            .reset_coords(drop=True)
            .rename({"LANDS_I": "LANDS_MAP_I"})
        )
        .expand_dims({"REGIONS_35_I": ["INDIA"]}, 2)
        .values
    )
    value.loc[:, :, ["LATAM"]] = (
        (
            vegetation_carbon_density_data_by_land_use()
            .loc["LATAM", :]
            .reset_coords(drop=True)
            - vegetation_carbon_density_data_by_land_use()
            .loc["LATAM", :]
            .reset_coords(drop=True)
            .rename({"LANDS_I": "LANDS_MAP_I"})
        )
        .expand_dims({"REGIONS_35_I": ["LATAM"]}, 2)
        .values
    )
    value.loc[:, :, ["RUSSIA"]] = (
        (
            vegetation_carbon_density_data_by_land_use()
            .loc["RUSSIA", :]
            .reset_coords(drop=True)
            - vegetation_carbon_density_data_by_land_use()
            .loc["RUSSIA", :]
            .reset_coords(drop=True)
            .rename({"LANDS_I": "LANDS_MAP_I"})
        )
        .expand_dims({"REGIONS_35_I": ["RUSSIA"]}, 2)
        .values
    )
    value.loc[:, :, ["USMCA"]] = (
        (
            vegetation_carbon_density_data_by_land_use()
            .loc["USMCA", :]
            .reset_coords(drop=True)
            - vegetation_carbon_density_data_by_land_use()
            .loc["USMCA", :]
            .reset_coords(drop=True)
            .rename({"LANDS_I": "LANDS_MAP_I"})
        )
        .expand_dims({"REGIONS_35_I": ["USMCA"]}, 2)
        .values
    )
    value.loc[:, :, ["LROW"]] = (
        (
            vegetation_carbon_density_data_by_land_use()
            .loc["LROW", :]
            .reset_coords(drop=True)
            - vegetation_carbon_density_data_by_land_use()
            .loc["LROW", :]
            .reset_coords(drop=True)
            .rename({"LANDS_I": "LANDS_MAP_I"})
        )
        .expand_dims({"REGIONS_35_I": ["LROW"]}, 2)
        .values
    )
    return value


@component.add(
    name="final_management_stock_change_factor_region_cropland",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "management_stock_change_factor_cropland": 1,
        "land_use_system_stock_change_factor_cropland": 1,
    },
)
def final_management_stock_change_factor_region_cropland():
    """
    Mutiplication of the relative stock change factors. Cstock= Cref *(FLU* FMG* FL)
    """
    return (
        management_stock_change_factor_cropland()
        * land_use_system_stock_change_factor_cropland()
    )


@component.add(
    name="grassland_area_by_region",
    units="km2",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_law_emissions_land_use_productive_area": 1,
        "switch_law_emissions": 1,
        "exo_land_use_area_productive_uses_t": 1,
        "land_use_area_productive_uses": 1,
    },
)
def grassland_area_by_region():
    """
    area of grassland (by region)
    """
    return if_then_else(
        np.logical_or(
            switch_law_emissions_land_use_productive_area() == 0,
            switch_law_emissions() == 0,
        ),
        lambda: exo_land_use_area_productive_uses_t()
        .loc[:, "GRASSLAND"]
        .reset_coords(drop=True),
        lambda: land_use_area_productive_uses()
        .loc[:, "GRASSLAND"]
        .reset_coords(drop=True),
    )


@component.add(
    name="IMV_matrix_land_use_changes",
    units="km2",
    subscripts=["REGIONS_9_I", "LANDS_I", "LANDS_MAP_I"],
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_imv_matrix_land_use_changes": 1},
    other_deps={
        "_initial_imv_matrix_land_use_changes": {
            "initial": {"matrix_of_land_use_changes": 1},
            "step": {},
        }
    },
)
def imv_matrix_land_use_changes():
    """
    Exogenous information from simulation (constant the first value in 2005) of land use changes
    """
    return _initial_imv_matrix_land_use_changes()


_initial_imv_matrix_land_use_changes = Initial(
    lambda: matrix_of_land_use_changes(), "_initial_imv_matrix_land_use_changes"
)


@component.add(
    name="input_stock_change_factor_cropland",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_law_emissions_share_management_agriculture": 1,
        "switch_law_emissions": 1,
        "exo_share_of_agriculture_in_transition_t": 1,
        "exo_share_of_traditional_agriculture_t": 1,
        "factor_input_low_crops": 6,
        "factor_input_high_without_manure_crops": 2,
        "exo_share_of_industrial_agriculture_t": 1,
        "factor_input_medium_crops": 2,
        "exo_share_of_low_input_agriculture_t": 1,
        "exo_share_of_regenerative_agriculture_t": 1,
        "average_share_of_agriculture_in_transition": 1,
        "average_share_of_traditional_agriculture": 1,
        "average_share_of_regenerative_agriculture": 1,
        "average_share_of_industrial_agriculture": 1,
        "average_share_of_low_input_agriculture": 1,
    },
)
def input_stock_change_factor_cropland():
    """
    IPCC 2006 Guidelines (Tier 1) (Eggleston, Buendia, Miwa, Ngara, & Tanabe, 2006) Table 5.5. Assumptions: - Industrial = Keep present trends/default: Medium input (Plevin et al 2014) - Traditional (subsistence) = Low input - Low input = Low input - Transition =Low input - Regenerative = High without manure (inputs) Based on IPCC Table 5.5 (soil stock change factor for different management activities on cropland). 0. Medium input. No new policies. Keep present trends/default assumption (Plevin et al 2014).All crop residues are returned to the field. If residues are removed then supplemental organic matter (e.g., manure)is added. Also requires mineral fertilization or N-fixing crop in rotation. 1. Low input. Low residue return: due to removal of residues (via collection or burning), frequent bare-fallowing, production of crops yielding low residues, no mineral fertilization or N-fixing crops. 2. High with-out manure. Greater crop residue inputs over medium C input cropping systems due to additional practices, such as production of high residue yielding crops or use of green manures, cover crops, but without manure applied. 3. High with manure. Higher C input over medium C input cropping systems due to an additional practice of regular addition of animal manure.
    """
    return if_then_else(
        np.logical_or(
            switch_law_emissions_share_management_agriculture() == 0,
            switch_law_emissions() == 0,
        ),
        lambda: exo_share_of_traditional_agriculture_t() * factor_input_low_crops()
        + exo_share_of_industrial_agriculture_t() * factor_input_medium_crops()
        + exo_share_of_low_input_agriculture_t() * factor_input_low_crops()
        + exo_share_of_agriculture_in_transition_t() * factor_input_low_crops()
        + exo_share_of_regenerative_agriculture_t()
        * factor_input_high_without_manure_crops(),
        lambda: average_share_of_traditional_agriculture() * factor_input_low_crops()
        + average_share_of_industrial_agriculture() * factor_input_medium_crops()
        + average_share_of_low_input_agriculture() * factor_input_low_crops()
        + average_share_of_agriculture_in_transition() * factor_input_low_crops()
        + average_share_of_regenerative_agriculture()
        * factor_input_high_without_manure_crops(),
    )


@component.add(
    name="land_use_system_stock_change_factor_cropland",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "share_area_rice_cropland": 2,
        "factor_landuse_paddy_rice": 1,
        "factor_landuse_set_asside_crop": 1,
        "share_area_fallow_cropland_sp": 2,
        "factor_landuse_longterm_cultivated_crop": 1,
    },
)
def land_use_system_stock_change_factor_cropland():
    """
    IPCC 2006 Guidelines (Tier 1) (Eggleston, Buendia, Miwa, Ngara, & Tanabe, 2006) Table 5.5. 4 types of land use systems: 1. Long-term cultivated 2.Paddy rice 3. Perenial/tree crops (assumption: 0%) 4. Temporary set asside (fallow) Factors from Table 5.5. IPCC in the excel file (parameters) **notes TODO: Perenial/tree crop have different factors. It has been applied by default factor of "lont-term cultivated" for cropland. It is not precis (percentage of perenial and tree crop should be applied)
    """
    return (
        share_area_rice_cropland() * factor_landuse_paddy_rice()
        + share_area_fallow_cropland_sp() * factor_landuse_set_asside_crop()
        + (1 - share_area_fallow_cropland_sp() - share_area_rice_cropland())
        * factor_landuse_longterm_cultivated_crop()
    )


@component.add(
    name="managed_grassland_area_by_region",
    units="km2",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"grassland_area_by_region": 1},
)
def managed_grassland_area_by_region():
    """
    **TODO: define percentage of area of grassland managed before calculating emissisons area of managed grassland (by region)
    """
    return grassland_area_by_region() * 0


@component.add(
    name="management_regime_stock_change_factor_cropland",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_law_emissions_share_management_agriculture": 1,
        "switch_law_emissions": 1,
        "exo_share_of_agriculture_in_transition_t": 1,
        "exo_share_of_traditional_agriculture_t": 1,
        "exo_share_of_industrial_agriculture_t": 1,
        "factor_management_full_tillage_crops": 6,
        "factor_management_reduce_tillage_crops": 6,
        "exo_share_of_low_input_agriculture_t": 1,
        "factor_management_notill_tillage_crops": 2,
        "exo_share_of_regenerative_agriculture_t": 1,
        "average_share_of_agriculture_in_transition": 1,
        "average_share_of_traditional_agriculture": 1,
        "average_share_of_regenerative_agriculture": 1,
        "average_share_of_industrial_agriculture": 1,
        "average_share_of_low_input_agriculture": 1,
    },
)
def management_regime_stock_change_factor_cropland():
    """
    IPCC 2006 Guidelines (Tier 1) (Eggleston, Buendia, Miwa, Ngara, & Tanabe, 2006) Table 5.5.(soil stock change factor for different management activities on cropland). Assumptions: - Traditional: Average full tillage and reduce - Industrial: Full tillage - Low input: Fulll tillage - Agri in transition: Reduced tillage - Regenerative/agroecology: Average Reduced and No till 3 OPTIONS: 1. Full tillage. No new policies. Keep present trends/default assumption. (Plevin et al 2014). ((Substantial soil disturbance with full inversion and/or frequent (within year) tillage operation) 2. Reduced tillage. Primary and/or secondary tillage but with reduced soil disturbance. 3. No-till. Direct seeding without primary tillage, with only minimal soil disturbance in the seeding zone.
    """
    return if_then_else(
        np.logical_or(
            switch_law_emissions_share_management_agriculture() == 0,
            switch_law_emissions() == 0,
        ),
        lambda: exo_share_of_traditional_agriculture_t()
        * (
            factor_management_full_tillage_crops()
            + factor_management_reduce_tillage_crops()
        )
        / 2
        + exo_share_of_industrial_agriculture_t()
        * factor_management_full_tillage_crops()
        + exo_share_of_low_input_agriculture_t()
        * factor_management_full_tillage_crops()
        + exo_share_of_agriculture_in_transition_t()
        * factor_management_reduce_tillage_crops()
        + exo_share_of_regenerative_agriculture_t()
        * (
            factor_management_reduce_tillage_crops()
            + factor_management_notill_tillage_crops()
        )
        / 2,
        lambda: average_share_of_traditional_agriculture()
        * (
            factor_management_full_tillage_crops()
            + factor_management_reduce_tillage_crops()
        )
        / 2
        + average_share_of_industrial_agriculture()
        * factor_management_full_tillage_crops()
        + average_share_of_low_input_agriculture()
        * factor_management_full_tillage_crops()
        + average_share_of_agriculture_in_transition()
        * factor_management_reduce_tillage_crops()
        + average_share_of_regenerative_agriculture()
        * (
            factor_management_reduce_tillage_crops()
            + factor_management_notill_tillage_crops()
        )
        / 2,
    )


@component.add(
    name="management_stock_change_factor_cropland",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "input_stock_change_factor_cropland": 1,
        "management_regime_stock_change_factor_cropland": 1,
    },
)
def management_stock_change_factor_cropland():
    """
    FMG*FI (management and input practices)
    """
    return (
        input_stock_change_factor_cropland()
        * management_regime_stock_change_factor_cropland()
    )


@component.add(
    name="management_stock_change_factor_grassland",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_selection_management_grassland_sp": 4,
        "factor_management_nominally_managed_grassland": 1,
        "factor_management_improved_medium_grassland": 1,
        "factor_management_severely_degraded_grassland": 1,
        "factor_management_improved_high_grassland": 1,
        "factor_management_moderately_degraded_grassland": 1,
    },
)
def management_stock_change_factor_grassland():
    """
    IPCC 2006 Guidelines (Tier 1) (Eggleston, Buendia, Miwa, Ngara, & Tanabe, 2006) Table 6.2. Based on IPCC Table 6.2 (soil stock change factor for different management activities on grassland). 0. Nominally managed (non-degraded). No new policies. Keep present trends/default assumption (Plevin et al. 2014). Sustainably managed grassland, but without significant management improvements. 1. Moderately degraded grassland. Overgrazed or moderately degraded grassland, with somewhat reduced productivity and receiving no management inputs. 2. Severely degraded. Implies major long-term loss of productivity and vegetation cover, due to severe mechanical damage to the vegetation and/or severe soil erosion. 3. Improved grassland medium inputs. Sustainably managed with moderate grazing pressure and that receive at least one improvement (e.g., fertilization, species improvement, irrigation). No additional management inputs have been used. 4. Improved grassland high inputs. Sustainably managed with moderate grazing pressure and that receive at least one improvement (e.g., fertilization, species improvement, irrigation). One or more additional management inputs/improvements have been used (beyond that is required to be classified as improved grassland)
    """
    return if_then_else(
        select_selection_management_grassland_sp() == 0,
        lambda: factor_management_nominally_managed_grassland(),
        lambda: if_then_else(
            select_selection_management_grassland_sp() == 1,
            lambda: factor_management_moderately_degraded_grassland(),
            lambda: if_then_else(
                select_selection_management_grassland_sp() == 2,
                lambda: factor_management_severely_degraded_grassland(),
                lambda: if_then_else(
                    select_selection_management_grassland_sp() == 3,
                    lambda: factor_management_improved_medium_grassland(),
                    lambda: factor_management_improved_high_grassland(),
                ),
            ),
        ),
    )


@component.add(
    name="Past_trends_C_land_use_change_emissions_W",
    units="Gt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "past_trends_global_co2_land_use_change_emissions": 1,
        "unit_conversion_c_co2": 1,
    },
)
def past_trends_c_land_use_change_emissions_w():
    """
    [DICE-2013R] Land-use change emissions. Cte at 2010 level for the period 1990-2100 as first approximation.
    """
    return past_trends_global_co2_land_use_change_emissions() * unit_conversion_c_co2()


@component.add(
    name="SHARE_AREA_FALLOW_CROPLAND_SP",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def share_area_fallow_cropland_sp():
    """
    **TODO: now it is assumed as cero, but pending a better value Total area of cropland temporary set aside by climate zone. (Included by the user? Add one by default (keep trends??--> trends for EU seem to be being lower/ctes) (at least for EU FAO data this is not totally cte, neither the total area neither the share of fallow (relative to cropland).
    """
    return xr.DataArray(
        0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
    )


@component.add(
    name="share_area_rainfed_cropland",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_law_emissions_land_use_productive_area": 1,
        "switch_law_emissions": 1,
        "exo_land_use_area_productive_uses_t": 3,
        "land_use_area_productive_uses": 3,
    },
)
def share_area_rainfed_cropland():
    """
    Share of RAINFED cropland with respect to the total area of cropland by region
    """
    return if_then_else(
        np.logical_or(
            switch_law_emissions_land_use_productive_area() == 0,
            switch_law_emissions() == 0,
        ),
        lambda: zidz(
            exo_land_use_area_productive_uses_t()
            .loc[:, "CROPLAND_RAINFED"]
            .reset_coords(drop=True),
            exo_land_use_area_productive_uses_t()
            .loc[:, "CROPLAND_RAINFED"]
            .reset_coords(drop=True)
            + exo_land_use_area_productive_uses_t()
            .loc[:, "CROPLAND_IRRIGATED"]
            .reset_coords(drop=True),
        ),
        lambda: zidz(
            land_use_area_productive_uses()
            .loc[:, "CROPLAND_RAINFED"]
            .reset_coords(drop=True),
            land_use_area_productive_uses()
            .loc[:, "CROPLAND_RAINFED"]
            .reset_coords(drop=True)
            + land_use_area_productive_uses()
            .loc[:, "CROPLAND_IRRIGATED"]
            .reset_coords(drop=True),
        ),
    )


@component.add(
    name="share_area_rice_cropland",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_law_emissions_irrigated_crop_area": 1,
        "area_of_irrigated_crops": 2,
        "area_of_rainfed_crops": 2,
        "exo_share_area_rice_cropland_t": 1,
    },
)
def share_area_rice_cropland():
    """
    Total area of rice of the total cropland area for each region
    """
    return if_then_else(
        switch_law_emissions_irrigated_crop_area() == 1,
        lambda: zidz(
            area_of_irrigated_crops().loc[:, "RICE"].reset_coords(drop=True)
            + area_of_rainfed_crops().loc[:, "RICE"].reset_coords(drop=True),
            sum(
                area_of_irrigated_crops().rename(
                    {"LAND_PRODUCTS_I": "LAND_PRODUCTS_I!"}
                ),
                dim=["LAND_PRODUCTS_I!"],
            )
            + sum(
                area_of_rainfed_crops().rename({"LAND_PRODUCTS_I": "LAND_PRODUCTS_I!"}),
                dim=["LAND_PRODUCTS_I!"],
            ),
        ),
        lambda: exo_share_area_rice_cropland_t(),
    )


@component.add(
    name="soil_carbon_density_cropland_region",
    units="tC/ha",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "soil_carbon_density_data_by_land_use": 2,
        "share_area_rainfed_cropland": 2,
        "final_management_stock_change_factor_region_cropland": 1,
        "management_stock_change_factor_default_cropland": 1,
    },
)
def soil_carbon_density_cropland_region():
    """
    Soil carbon stock cropland by climate zone (after anagement factors being applied). Soil database (regionally average C stocks) corresponds to Cbef (default values) assuming full tillage (FMG), Input is medium (FI) and long-term cultivated (FLU). Cstock-after= Cref *(FLUaf* FMGaf* FLaft)= Cbef* (FLUaft* FMGaft*FLaft)/ (FLUbef* FMGbef*FLbef)
    """
    return (
        (
            soil_carbon_density_data_by_land_use()
            .loc[:, "CROPLAND_RAINFED"]
            .reset_coords(drop=True)
            * share_area_rainfed_cropland()
            + soil_carbon_density_data_by_land_use()
            .loc[:, "CROPLAND_IRRIGATED"]
            .reset_coords(drop=True)
            * (1 - share_area_rainfed_cropland())
        )
        * final_management_stock_change_factor_region_cropland()
        / management_stock_change_factor_default_cropland()
    )


@component.add(
    name="soil_carbon_density_forestland_region",
    units="tC/ha",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"soil_carbon_density_data_by_land_use": 1},
)
def soil_carbon_density_forestland_region():
    """
    Same default carbon stock data for the three type of forests (managed/primary/plantations)
    """
    return (
        soil_carbon_density_data_by_land_use()
        .loc[:, "FOREST_MANAGED"]
        .reset_coords(drop=True)
    )


@component.add(
    name="soil_carbon_density_grassland_region",
    units="tC/ha",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "soil_carbon_density_data_by_land_use": 1,
        "management_stock_change_factor_grassland": 1,
        "management_stock_change_factor_default_grassland": 1,
    },
)
def soil_carbon_density_grassland_region():
    """
    Soil carbon stock grassland by REGION (after anagement factors being applied)
    """
    return (
        soil_carbon_density_data_by_land_use()
        .loc[:, "GRASSLAND"]
        .reset_coords(drop=True)
        * management_stock_change_factor_grassland()
        / management_stock_change_factor_default_grassland()
    )


@component.add(
    name="soil_carbon_density_otherland_region",
    units="tC/ha",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"soil_carbon_density_data_by_land_use": 1},
)
def soil_carbon_density_otherland_region():
    return (
        soil_carbon_density_data_by_land_use()
        .loc[:, "OTHER_LAND"]
        .reset_coords(drop=True)
    )


@component.add(
    name="soil_carbon_density_shrubland_region",
    units="tC/ha",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"soil_carbon_density_data_by_land_use": 1},
)
def soil_carbon_density_shrubland_region():
    """
    soil_carbon_density_shrubland_region
    """
    return (
        soil_carbon_density_data_by_land_use()
        .loc[:, "SHRUBLAND"]
        .reset_coords(drop=True)
    )


@component.add(
    name="soil_carbon_density_solarland_fromlanduse1",
    units="tC/ha",
    subscripts=["LANDS_I", "REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_nrg2law_pv_land_occupation_ratio": 1,
        "switch_landwater": 1,
        "select_selection_management_solarland_sp": 6,
        "exo_pv_land_occupation_ratio_t": 6,
        "pv_land_occupation_ratio": 6,
    },
)
def soil_carbon_density_solarland_fromlanduse1():
    """
    Soil carbon density in solar land depending on the previous land use (land use 1)
    """
    return if_then_else(
        np.logical_or(
            switch_nrg2law_pv_land_occupation_ratio() == 0, switch_landwater() == 0
        ),
        lambda: if_then_else(
            select_selection_management_solarland_sp() == 0,
            lambda: 0 * (1 - exo_pv_land_occupation_ratio_t())
            + 0 * exo_pv_land_occupation_ratio_t(),
            lambda: if_then_else(
                select_selection_management_solarland_sp() == 1,
                lambda: 0 * (1 - exo_pv_land_occupation_ratio_t())
                + 0 * exo_pv_land_occupation_ratio_t(),
                lambda: if_then_else(
                    select_selection_management_solarland_sp() == 2,
                    lambda: 0 * (1 - exo_pv_land_occupation_ratio_t())
                    + 0 * exo_pv_land_occupation_ratio_t(),
                    lambda: xr.DataArray(
                        0,
                        {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
                        ["REGIONS_9_I"],
                    ),
                ),
            ),
        ),
        lambda: if_then_else(
            select_selection_management_solarland_sp() == 0,
            lambda: 0
            * (
                1
                - pv_land_occupation_ratio()
                .loc[_subscript_dict["REGIONS_9_I"]]
                .rename({"REGIONS_36_I": "REGIONS_9_I"})
            )
            + 0
            * pv_land_occupation_ratio()
            .loc[_subscript_dict["REGIONS_9_I"]]
            .rename({"REGIONS_36_I": "REGIONS_9_I"}),
            lambda: if_then_else(
                select_selection_management_solarland_sp() == 1,
                lambda: 0
                * (
                    1
                    - pv_land_occupation_ratio()
                    .loc[_subscript_dict["REGIONS_9_I"]]
                    .rename({"REGIONS_36_I": "REGIONS_9_I"})
                )
                + 0
                * pv_land_occupation_ratio()
                .loc[_subscript_dict["REGIONS_9_I"]]
                .rename({"REGIONS_36_I": "REGIONS_9_I"}),
                lambda: if_then_else(
                    select_selection_management_solarland_sp() == 2,
                    lambda: 0
                    * (
                        1
                        - pv_land_occupation_ratio()
                        .loc[_subscript_dict["REGIONS_9_I"]]
                        .rename({"REGIONS_36_I": "REGIONS_9_I"})
                    )
                    + 0
                    * pv_land_occupation_ratio()
                    .loc[_subscript_dict["REGIONS_9_I"]]
                    .rename({"REGIONS_36_I": "REGIONS_9_I"}),
                    lambda: xr.DataArray(
                        0,
                        {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
                        ["REGIONS_9_I"],
                    ),
                ),
            ),
        ),
    ).expand_dims({"LANDS_I": _subscript_dict["LANDS_I"]}, 0)


@component.add(
    name="soil_carbon_density_urbanland_region",
    units="tC/ha",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"soil_carbon_density_data_by_land_use": 1},
)
def soil_carbon_density_urbanland_region():
    return (
        soil_carbon_density_data_by_land_use()
        .loc[:, "URBAN_LAND"]
        .reset_coords(drop=True)
    )


@component.add(
    name="soil_carbon_density_wetland_region",
    units="tC/ha",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"soil_carbon_density_data_by_land_use": 1},
)
def soil_carbon_density_wetland_region():
    """
    **Not calculated (put just a zero).
    """
    return (
        soil_carbon_density_data_by_land_use().loc[:, "WETLAND"].reset_coords(drop=True)
    )


@component.add(
    name="soil_carbon_stock_change_crops_region",
    units="tC/ha*Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "soil_carbon_density_cropland_region": 1,
        "delayed_soil_carbon_stock_cropland_region": 1,
    },
)
def soil_carbon_stock_change_crops_region():
    return (
        soil_carbon_density_cropland_region()
        - delayed_soil_carbon_stock_cropland_region()
    )


@component.add(
    name="soil_carbon_stock_change_grassland_region",
    units="tC/ha",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "soil_carbon_density_grassland_region": 1,
        "delayed_soil_carbon_stock_grassland_climate_zone": 1,
    },
)
def soil_carbon_stock_change_grassland_region():
    return (
        soil_carbon_density_grassland_region()
        - delayed_soil_carbon_stock_grassland_climate_zone()
    )


@component.add(
    name="soil_emissions_cropland_management",
    units="tC/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cropland_total_area_by_region": 1,
        "soil_carbon_stock_change_crops_region": 1,
        "unit_conversion_km2_ha": 1,
    },
)
def soil_emissions_cropland_management():
    """
    Change of stock in soil in cropland due to change of practices in cropland
    """
    return (
        cropland_total_area_by_region()
        * soil_carbon_stock_change_crops_region()
        * (1 / unit_conversion_km2_ha())
    )


@component.add(
    name="soil_emissions_cropland_management_delayed",
    units="tC/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Stateful",
    comp_subtype="Delay",
    depends_on={"_delay_soil_emissions_cropland_management_delayed": 1},
    other_deps={
        "_delay_soil_emissions_cropland_management_delayed": {
            "initial": {
                "soil_emissions_cropland_management": 1,
                "delay_time_soil_emissions_management": 1,
            },
            "step": {
                "soil_emissions_cropland_management": 1,
                "delay_time_soil_emissions_management": 1,
            },
        }
    },
)
def soil_emissions_cropland_management_delayed():
    """
    Delay of the change in carbon in soil (natural process that it is not inmediate) . Application of a first order delay in line with the equation: C_((t))=(C_0+a [1-e^(-bx)])
    """
    return _delay_soil_emissions_cropland_management_delayed()


_delay_soil_emissions_cropland_management_delayed = Delay(
    lambda: soil_emissions_cropland_management(),
    lambda: xr.DataArray(
        delay_time_soil_emissions_management(),
        {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
        ["REGIONS_9_I"],
    ),
    lambda: soil_emissions_cropland_management(),
    lambda: 1,
    time_step,
    "_delay_soil_emissions_cropland_management_delayed",
)


@component.add(
    name="soil_emissions_grassland_management",
    units="tC/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "managed_grassland_area_by_region": 1,
        "soil_carbon_stock_change_grassland_region": 1,
        "unit_conversion_km2_ha": 1,
    },
)
def soil_emissions_grassland_management():
    return (
        managed_grassland_area_by_region()
        * soil_carbon_stock_change_grassland_region()
        * (1 / unit_conversion_km2_ha())
    )


@component.add(
    name="soil_emissions_grassland_management_delayed",
    units="tC/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Stateful",
    comp_subtype="Delay",
    depends_on={"_delay_soil_emissions_grassland_management_delayed": 1},
    other_deps={
        "_delay_soil_emissions_grassland_management_delayed": {
            "initial": {
                "soil_emissions_grassland_management": 1,
                "delay_time_soil_emissions_management": 1,
            },
            "step": {
                "soil_emissions_grassland_management": 1,
                "delay_time_soil_emissions_management": 1,
            },
        }
    },
)
def soil_emissions_grassland_management_delayed():
    return _delay_soil_emissions_grassland_management_delayed()


_delay_soil_emissions_grassland_management_delayed = Delay(
    lambda: soil_emissions_grassland_management(),
    lambda: xr.DataArray(
        delay_time_soil_emissions_management(),
        {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
        ["REGIONS_9_I"],
    ),
    lambda: soil_emissions_grassland_management(),
    lambda: 1,
    time_step,
    "_delay_soil_emissions_grassland_management_delayed",
)


@component.add(
    name="soil_emissions_landuse1_to_landuse2",
    units="tC/Year",
    subscripts=["LANDS_I", "LANDS_MAP_I", "REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_law_emissions_matrix_of_land_use_changes": 1,
        "switch_law_emissions": 1,
        "imv_matrix_land_use_changes": 1,
        "unit_conversion_km2_ha": 2,
        "factor_emission_soil_landuse_to_landuse2": 2,
        "matrix_of_land_use_changes": 1,
    },
)
def soil_emissions_landuse1_to_landuse2():
    """
    ***To be programmed. old: factorss emission soil landuse to landuse2[LANDS I,LANDS MAP I]*(matrix of land use changes by climatic zones[LANDS I,LANDS MAP I ,TROPICAL]+matrix of land use changes by climatic zones[LANDS I,LANDS MAP I,WARM]+matrix of land use changes by climatic zones [LANDS I,LANDS MAP I,ARID HOT]+matrix of land use changes by climatic zones[LANDS I,LANDS MAP I,ARID COLD]+matrix of land use changes by climatic zones [LANDS I,LANDS MAP I,TEMPERATE]+matrix of land use changes by climatic zones[LANDS I,LANDS MAP I,WINTER SNOW]+matrix of land use changes by climatic zones [LANDS I,LANDS MAP I,POLAR])
    """
    return if_then_else(
        np.logical_or(
            switch_law_emissions_matrix_of_land_use_changes() == 0,
            switch_law_emissions() == 0,
        ),
        lambda: imv_matrix_land_use_changes()
        * factor_emission_soil_landuse_to_landuse2().transpose(
            "REGIONS_9_I", "LANDS_I", "LANDS_MAP_I"
        )
        * (1 / unit_conversion_km2_ha()),
        lambda: matrix_of_land_use_changes()
        * factor_emission_soil_landuse_to_landuse2().transpose(
            "REGIONS_9_I", "LANDS_I", "LANDS_MAP_I"
        )
        * (1 / unit_conversion_km2_ha()),
    ).transpose("LANDS_I", "LANDS_MAP_I", "REGIONS_9_I")


@component.add(
    name="soil_emissions_landuse1_to_landuse2_byregion",
    units="tC/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"soil_emissions_landuse1_to_landuse2_delayed": 1},
)
def soil_emissions_landuse1_to_landuse2_byregion():
    """
    Sum by region ***To be programmed:
    """
    return sum(
        soil_emissions_landuse1_to_landuse2_delayed().rename(
            {"LANDS_I": "LANDS_I!", "LANDS_MAP_I": "LANDS_MAP_I!"}
        ),
        dim=["LANDS_I!", "LANDS_MAP_I!"],
    )


@component.add(
    name="soil_emissions_landuse1_to_landuse2_delayed",
    subscripts=["LANDS_I", "LANDS_MAP_I", "REGIONS_9_I"],
    comp_type="Stateful",
    comp_subtype="Delay",
    depends_on={"_delay_soil_emissions_landuse1_to_landuse2_delayed": 1},
    other_deps={
        "_delay_soil_emissions_landuse1_to_landuse2_delayed": {
            "initial": {
                "soil_emissions_landuse1_to_landuse2": 1,
                "delay_time_landuse_to_landuse2_soil": 1,
            },
            "step": {
                "soil_emissions_landuse1_to_landuse2": 1,
                "delay_time_landuse_to_landuse2_soil": 1,
            },
        }
    },
)
def soil_emissions_landuse1_to_landuse2_delayed():
    return _delay_soil_emissions_landuse1_to_landuse2_delayed()


_delay_soil_emissions_landuse1_to_landuse2_delayed = Delay(
    lambda: soil_emissions_landuse1_to_landuse2(),
    lambda: xr.DataArray(
        delay_time_landuse_to_landuse2_soil(),
        {
            "LANDS_I": _subscript_dict["LANDS_I"],
            "LANDS_MAP_I": _subscript_dict["LANDS_MAP_I"],
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        },
        ["LANDS_I", "LANDS_MAP_I", "REGIONS_9_I"],
    ),
    lambda: soil_emissions_landuse1_to_landuse2(),
    lambda: 1,
    time_step,
    "_delay_soil_emissions_landuse1_to_landuse2_delayed",
)


@component.add(
    name="vegetation_carbon_density_grassland_region",
    units="tC/ha",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"vegetation_carbon_density_data_by_land_use": 1},
)
def vegetation_carbon_density_grassland_region():
    """
    Vegetation carbon density for each region for grassland
    """
    return (
        vegetation_carbon_density_data_by_land_use()
        .loc[:, "GRASSLAND"]
        .reset_coords(drop=True)
    )


@component.add(
    name="vegetation_carbon_density_managed_and_primary_forestland_region",
    units="tC/ha",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "carbon_stock_in_managed_and_primary_forests": 1,
        "area_of_managed_and_primary_forest": 1,
    },
)
def vegetation_carbon_density_managed_and_primary_forestland_region():
    """
    Vegetation carbon density for each climate zone for managed and primary forest land
    """
    return zidz(
        xr.DataArray(
            carbon_stock_in_managed_and_primary_forests(),
            {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
            ["REGIONS_9_I"],
        ),
        area_of_managed_and_primary_forest(),
    )


@component.add(
    name="vegetation_carbon_density_otherland_region",
    units="tC/ha",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"vegetation_carbon_density_data_by_land_use": 1},
)
def vegetation_carbon_density_otherland_region():
    """
    Vegetation carbon density for each region for shrubland
    """
    return (
        vegetation_carbon_density_data_by_land_use()
        .loc[:, "OTHER_LAND"]
        .reset_coords(drop=True)
    )


@component.add(
    name="vegetation_carbon_density_plantations_forestland_region",
    units="tC/ha",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"vegetation_carbon_density_data_by_land_use": 1},
)
def vegetation_carbon_density_plantations_forestland_region():
    """
    Same default carbon stock data for the three type of forests (managed/primary/plantations)
    """
    return (
        vegetation_carbon_density_data_by_land_use()
        .loc[:, "FOREST_MANAGED"]
        .reset_coords(drop=True)
    )


@component.add(
    name="vegetation_carbon_density_shrubland_region",
    units="tC/ha",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"vegetation_carbon_density_data_by_land_use": 1},
)
def vegetation_carbon_density_shrubland_region():
    """
    Vegetation carbon density for each region for shrubland
    """
    return (
        vegetation_carbon_density_data_by_land_use()
        .loc[:, "SHRUBLAND"]
        .reset_coords(drop=True)
    )


@component.add(
    name="vegetation_carbon_density_solarland_fromlanduse1",
    units="tC/ha",
    subscripts=["LANDS_I", "REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_nrg2law_pv_land_occupation_ratio": 1,
        "switch_landwater": 1,
        "select_selection_management_solarland_sp": 6,
        "exo_pv_land_occupation_ratio_t": 6,
        "pv_land_occupation_ratio": 6,
    },
)
def vegetation_carbon_density_solarland_fromlanduse1():
    """
    Vegetation carbon density for each climate zone for ssolar land depending on the previous land use (landuse1) ** to be completed with the values from Dirk et al 2021
    """
    return if_then_else(
        np.logical_or(
            switch_nrg2law_pv_land_occupation_ratio() == 0, switch_landwater() == 0
        ),
        lambda: if_then_else(
            select_selection_management_solarland_sp() == 0,
            lambda: 0 * (1 - exo_pv_land_occupation_ratio_t())
            + 0 * exo_pv_land_occupation_ratio_t(),
            lambda: if_then_else(
                select_selection_management_solarland_sp() == 1,
                lambda: 0 * (1 - exo_pv_land_occupation_ratio_t())
                + 0 * exo_pv_land_occupation_ratio_t(),
                lambda: if_then_else(
                    select_selection_management_solarland_sp() == 2,
                    lambda: 0 * (1 - exo_pv_land_occupation_ratio_t())
                    + 0 * exo_pv_land_occupation_ratio_t(),
                    lambda: xr.DataArray(
                        0,
                        {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
                        ["REGIONS_9_I"],
                    ),
                ),
            ),
        ),
        lambda: if_then_else(
            select_selection_management_solarland_sp() == 0,
            lambda: 0
            * (
                1
                - pv_land_occupation_ratio()
                .loc[_subscript_dict["REGIONS_9_I"]]
                .rename({"REGIONS_36_I": "REGIONS_9_I"})
            )
            + 0
            * pv_land_occupation_ratio()
            .loc[_subscript_dict["REGIONS_9_I"]]
            .rename({"REGIONS_36_I": "REGIONS_9_I"}),
            lambda: if_then_else(
                select_selection_management_solarland_sp() == 1,
                lambda: 0
                * (
                    1
                    - pv_land_occupation_ratio()
                    .loc[_subscript_dict["REGIONS_9_I"]]
                    .rename({"REGIONS_36_I": "REGIONS_9_I"})
                )
                + 0
                * pv_land_occupation_ratio()
                .loc[_subscript_dict["REGIONS_9_I"]]
                .rename({"REGIONS_36_I": "REGIONS_9_I"}),
                lambda: if_then_else(
                    select_selection_management_solarland_sp() == 2,
                    lambda: 0
                    * (
                        1
                        - pv_land_occupation_ratio()
                        .loc[_subscript_dict["REGIONS_9_I"]]
                        .rename({"REGIONS_36_I": "REGIONS_9_I"})
                    )
                    + 0
                    * pv_land_occupation_ratio()
                    .loc[_subscript_dict["REGIONS_9_I"]]
                    .rename({"REGIONS_36_I": "REGIONS_9_I"}),
                    lambda: xr.DataArray(
                        0,
                        {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
                        ["REGIONS_9_I"],
                    ),
                ),
            ),
        ),
    ).expand_dims({"LANDS_I": _subscript_dict["LANDS_I"]}, 0)


@component.add(
    name="vegetation_carbon_density_urbanland_region",
    units="tC/ha",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"vegetation_carbon_density_data_by_land_use": 1},
)
def vegetation_carbon_density_urbanland_region():
    """
    Vegetation carbon density for each region for urbanland
    """
    return (
        vegetation_carbon_density_data_by_land_use()
        .loc[:, "URBAN_LAND"]
        .reset_coords(drop=True)
    )


@component.add(
    name="vegetation_carbon_density_wetland_region",
    units="tC/ha",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"vegetation_carbon_density_data_by_land_use": 1},
)
def vegetation_carbon_density_wetland_region():
    """
    Vegetation carbon density for region for wetland. **Not calculated (put just a zero).
    """
    return (
        vegetation_carbon_density_data_by_land_use()
        .loc[:, "WETLAND"]
        .reset_coords(drop=True)
    )


@component.add(
    name="vegetation_emissions_landuse1_to_landuse2",
    units="tC/Year",
    subscripts=["LANDS_I", "LANDS_MAP_I", "REGIONS_9_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_law_emissions_matrix_of_land_use_changes": 1,
        "switch_law_emissions": 1,
        "imv_matrix_land_use_changes": 1,
        "factor_emission_vegetation_landuse_to_landuse2": 2,
        "unit_conversion_km2_ha": 2,
        "matrix_of_land_use_changes": 1,
    },
)
def vegetation_emissions_landuse1_to_landuse2():
    """
    ***To be programmed: include the exception of emissions due to afforestation (land use2 = forest)that will come from "forest vensim view". This emissions are instataneous (except the carbon uptake by afforestation: from forest vensim view, and the carbon uptake from cropland to grassland (this last still to be programmed--> default time of 20 years which corresponds to a delay time of 5 years ) old: factor_emission_vegetation_landuse_to_landuse2[LANDS I,LANDS I,REGIONS 9 I]*(matrix of land use changes by climatic zones [LANDS I ,LANDS MAP I,TROPICAL]+matrix of land use changes by climatic zones[LANDS I,LANDS MAP I,WARM]+matrix of land use changes by climatic zones [LANDS I,LANDS MAP I,ARID HOT]+matrix of land use changes by climatic zones[LANDS I,LANDS MAP I,ARID COLD]+matrix of land use changes by climatic zones [LANDS I,LANDS MAP I,TEMPERATE]+matrix of land use changes by climatic zones[LANDS I,LANDS MAP I,WINTER SNOW]+matrix of land use changes by climatic zones [LANDS I,LANDS MAP I,POLAR])
    """
    value = xr.DataArray(
        np.nan,
        {
            "LANDS_I": _subscript_dict["LANDS_I"],
            "LANDS_MAP_I": _subscript_dict["LANDS_MAP_I"],
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        },
        ["LANDS_I", "LANDS_MAP_I", "REGIONS_9_I"],
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[
        _subscript_dict["LANDS_NON_FOREST_I"], ["FOREST_MANAGED"], :
    ] = False
    except_subs.loc[
        _subscript_dict["LANDS_NON_FOREST_I"], ["FOREST_PLANTATIONS"], :
    ] = False
    except_subs.loc[
        ["FOREST_MANAGED"], _subscript_dict["LANDS_NON_FOREST_I"], :
    ] = False
    except_subs.loc[
        ["FOREST_PLANTATIONS"], _subscript_dict["LANDS_NON_FOREST_I"], :
    ] = False
    value.values[except_subs.values] = (
        if_then_else(
            np.logical_or(
                switch_law_emissions_matrix_of_land_use_changes() == 0,
                switch_law_emissions() == 0,
            ),
            lambda: imv_matrix_land_use_changes()
            * factor_emission_vegetation_landuse_to_landuse2().transpose(
                "REGIONS_9_I", "LANDS_I", "LANDS_MAP_I"
            )
            * (1 / unit_conversion_km2_ha()),
            lambda: matrix_of_land_use_changes()
            * factor_emission_vegetation_landuse_to_landuse2().transpose(
                "REGIONS_9_I", "LANDS_I", "LANDS_MAP_I"
            )
            * (1 / unit_conversion_km2_ha()),
        )
        .transpose("LANDS_I", "LANDS_MAP_I", "REGIONS_9_I")
        .values[except_subs.values]
    )
    value.loc[_subscript_dict["LANDS_NON_FOREST_I"], ["FOREST_MANAGED"], :] = 0
    value.loc[_subscript_dict["LANDS_NON_FOREST_I"], ["FOREST_PLANTATIONS"], :] = 0
    value.loc[["FOREST_MANAGED"], _subscript_dict["LANDS_NON_FOREST_I"], :] = 0
    value.loc[["FOREST_PLANTATIONS"], _subscript_dict["LANDS_NON_FOREST_I"], :] = 0
    return value


@component.add(
    name="vegetation_emissions_landuse1_to_landuse2_byregion",
    units="tC/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "vegetation_emissions_landuse1_to_landuse2": 1,
        "forest_carbon_dioxide_total_flow_by_region": 1,
    },
)
def vegetation_emissions_landuse1_to_landuse2_byregion():
    """
    Sum by region **TODO: TO review the dynamics (those that are not delayed?)/ Vegetation: check notes (from cropland to grassland for example) AND alos check how the exception of emissions due to afforestation it is included (land use2 = forest)that will come from "forest vensim view". This emissions are instataneous (except the carbon uptake by afforestation: from forest vensim view, and the carbon uptake from cropland to grassland (this last is not yet included--> default time of 20 years which corresponds to a delay time of 5 years )
    """
    return (
        sum(
            vegetation_emissions_landuse1_to_landuse2().rename(
                {"LANDS_I": "LANDS_I!", "LANDS_MAP_I": "LANDS_MAP_I!"}
            ),
            dim=["LANDS_I!", "LANDS_MAP_I!"],
        )
        - forest_carbon_dioxide_total_flow_by_region()
    )
