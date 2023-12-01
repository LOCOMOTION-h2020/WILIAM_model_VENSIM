"""
Module land_and_water.land.land_use_changes
Translated using PySD version 3.10.0
"""


@component.add(
    name="aux_land_uses_2015",
    units="km2",
    subscripts=["REGIONS_9_I", "LANDS_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_aux_land_uses_2015": 1},
    other_deps={
        "_delayfixed_aux_land_uses_2015": {
            "initial": {"time_step": 1},
            "step": {"land_uses_until_2015": 1},
        }
    },
)
def aux_land_uses_2015():
    """
    Auxiliary variable to estimate the land uses in the year 2015. The method is not mathematically exact, but the error tends to 0 when the TIME STEP decreases.
    """
    return _delayfixed_aux_land_uses_2015()


_delayfixed_aux_land_uses_2015 = DelayFixed(
    lambda: land_uses_until_2015(),
    lambda: time_step(),
    lambda: xr.DataArray(
        0,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "LANDS_I": _subscript_dict["LANDS_I"],
        },
        ["REGIONS_9_I", "LANDS_I"],
    ),
    time_step,
    "_delayfixed_aux_land_uses_2015",
)


@component.add(
    name="cropland_loss_due_to_sea_level_rise_by_region",
    units="km2",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_climate_change_damage": 1,
        "unit_conversion_km2_ha": 1,
        "effective_percent_of_land_change_per_meter_of_sea_level_rise": 1,
        "sea_level_rise_by_region": 1,
    },
)
def cropland_loss_due_to_sea_level_rise_by_region():
    """
    the percent of agricultural land lost for the sea level rise in each country i
    """
    return if_then_else(
        switch_climate_change_damage() == 0,
        lambda: xr.DataArray(
            0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
        ),
        lambda: sea_level_rise_by_region()
        * effective_percent_of_land_change_per_meter_of_sea_level_rise()
        * unit_conversion_km2_ha(),
    )


@component.add(
    name="factor_of_maximum_land_limit",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LANDS_I", "LANDS_MAP_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "matrix_of_accumulated_land_use_changes": 3,
        "matrix_of_maximum_land_changes": 3,
        "land_use_changes_demanded": 3,
        "land_use_area_by_region": 2,
        "swith_law_limits_land_by_source": 2,
        "initial_land_use_by_region_2015": 2,
        "maximum_land_uses_by_source": 2,
    },
)
def factor_of_maximum_land_limit():
    """
    factor of maximum land use changes by region
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "LANDS_I": _subscript_dict["LANDS_I"],
            "LANDS_MAP_I": _subscript_dict["LANDS_MAP_I"],
        },
        ["REGIONS_9_I", "LANDS_I", "LANDS_MAP_I"],
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, :, ["CROPLAND_RAINFED"]] = False
    except_subs.loc[:, :, ["FOREST_PLANTATIONS"]] = False
    value.values[except_subs.values] = if_then_else(
        np.logical_and(
            matrix_of_accumulated_land_use_changes()
            >= matrix_of_maximum_land_changes(),
            (land_use_changes_demanded().rename({"LANDS_I": "LANDS_MAP_I"}) > 0),
        ),
        lambda: xr.DataArray(
            0,
            {
                "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                "LANDS_I": _subscript_dict["LANDS_I"],
                "LANDS_MAP_I": _subscript_dict["LANDS_MAP_I"],
            },
            ["REGIONS_9_I", "LANDS_I", "LANDS_MAP_I"],
        ),
        lambda: xr.DataArray(
            1,
            {
                "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                "LANDS_I": _subscript_dict["LANDS_I"],
                "LANDS_MAP_I": _subscript_dict["LANDS_MAP_I"],
            },
            ["REGIONS_9_I", "LANDS_I", "LANDS_MAP_I"],
        ),
    ).values[except_subs.values]
    value.loc[:, :, ["CROPLAND_RAINFED"]] = (
        if_then_else(
            swith_law_limits_land_by_source() == 0,
            lambda: if_then_else(
                np.logical_and(
                    matrix_of_accumulated_land_use_changes()
                    .loc[:, :, "CROPLAND_RAINFED"]
                    .reset_coords(drop=True)
                    >= matrix_of_maximum_land_changes()
                    .loc[:, :, "CROPLAND_RAINFED"]
                    .reset_coords(drop=True),
                    (
                        land_use_changes_demanded()
                        .loc[:, "CROPLAND_RAINFED"]
                        .reset_coords(drop=True)
                        > 0
                    ),
                ),
                lambda: xr.DataArray(
                    0,
                    {
                        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                        "LANDS_I": _subscript_dict["LANDS_I"],
                    },
                    ["REGIONS_9_I", "LANDS_I"],
                ),
                lambda: xr.DataArray(
                    1,
                    {
                        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                        "LANDS_I": _subscript_dict["LANDS_I"],
                    },
                    ["REGIONS_9_I", "LANDS_I"],
                ),
            ),
            lambda: if_then_else(
                land_use_area_by_region()
                .loc[:, "CROPLAND_RAINFED"]
                .reset_coords(drop=True)
                >= maximum_land_uses_by_source()
                .loc[:, "CROPLAND_RAINFED"]
                .reset_coords(drop=True)
                * initial_land_use_by_region_2015()
                .loc[:, "CROPLAND_RAINFED"]
                .reset_coords(drop=True),
                lambda: xr.DataArray(
                    0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
                ),
                lambda: xr.DataArray(
                    1, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
                ),
            ).expand_dims({"LANDS_I": _subscript_dict["LANDS_I"]}, 1),
        )
        .expand_dims({"LANDS_MAP_I": ["CROPLAND_RAINFED"]}, 2)
        .values
    )
    value.loc[:, :, ["FOREST_PLANTATIONS"]] = (
        if_then_else(
            swith_law_limits_land_by_source() == 0,
            lambda: if_then_else(
                np.logical_and(
                    matrix_of_accumulated_land_use_changes()
                    .loc[:, :, "FOREST_PLANTATIONS"]
                    .reset_coords(drop=True)
                    >= matrix_of_maximum_land_changes()
                    .loc[:, :, "FOREST_PLANTATIONS"]
                    .reset_coords(drop=True),
                    (
                        land_use_changes_demanded()
                        .loc[:, "FOREST_PLANTATIONS"]
                        .reset_coords(drop=True)
                        > 0
                    ),
                ),
                lambda: xr.DataArray(
                    0,
                    {
                        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                        "LANDS_I": _subscript_dict["LANDS_I"],
                    },
                    ["REGIONS_9_I", "LANDS_I"],
                ),
                lambda: xr.DataArray(
                    1,
                    {
                        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                        "LANDS_I": _subscript_dict["LANDS_I"],
                    },
                    ["REGIONS_9_I", "LANDS_I"],
                ),
            ),
            lambda: if_then_else(
                land_use_area_by_region()
                .loc[:, "FOREST_PLANTATIONS"]
                .reset_coords(drop=True)
                >= maximum_land_uses_by_source()
                .loc[:, "FOREST_PLANTATIONS"]
                .reset_coords(drop=True)
                * initial_land_use_by_region_2015()
                .loc[:, "FOREST_PLANTATIONS"]
                .reset_coords(drop=True),
                lambda: xr.DataArray(
                    0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
                ),
                lambda: xr.DataArray(
                    1, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
                ),
            ).expand_dims({"LANDS_I": _subscript_dict["LANDS_I"]}, 1),
        )
        .expand_dims({"LANDS_FOREST_I": ["FOREST_PLANTATIONS"]}, 2)
        .values
    )
    return value


@component.add(
    name="factor_of_minimum_land_limit",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LANDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "land_use_area_by_region": 2,
        "minimum_land_uses_by_region": 1,
        "minimum_limit_land_use_by_policy": 1,
    },
)
def factor_of_minimum_land_limit():
    """
    factor of minimum use of land for each region
    """
    return if_then_else(
        np.logical_or(
            land_use_area_by_region() <= minimum_land_uses_by_region(),
            land_use_area_by_region() <= minimum_limit_land_use_by_policy(),
        ),
        lambda: xr.DataArray(
            0,
            {
                "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                "LANDS_I": _subscript_dict["LANDS_I"],
            },
            ["REGIONS_9_I", "LANDS_I"],
        ),
        lambda: xr.DataArray(
            1,
            {
                "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                "LANDS_I": _subscript_dict["LANDS_I"],
            },
            ["REGIONS_9_I", "LANDS_I"],
        ),
    )


@component.add(
    name="factor_of_solar_land_limit",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LANDS_I", "LANDS_MAP_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_policy_land_protection_from_solar_pv_sp": 1,
        "policy_land_protection_from_solar_pv_sp": 1,
    },
)
def factor_of_solar_land_limit():
    """
    =1 solar land can increase, =0 solar land cannot increase in that land use because that use is protected but only for solar PV instalation
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "LANDS_I": _subscript_dict["LANDS_I"],
            "LANDS_MAP_I": _subscript_dict["LANDS_MAP_I"],
        },
        ["REGIONS_9_I", "LANDS_I", "LANDS_MAP_I"],
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, :, ["SOLAR_LAND"]] = False
    value.values[except_subs.values] = 1
    value.loc[:, :, ["SOLAR_LAND"]] = (
        if_then_else(
            (switch_policy_land_protection_from_solar_pv_sp() == 0).expand_dims(
                {"LANDS_I": _subscript_dict["LANDS_I"]}, 1
            ),
            lambda: xr.DataArray(
                1,
                {
                    "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                    "LANDS_I": _subscript_dict["LANDS_I"],
                },
                ["REGIONS_9_I", "LANDS_I"],
            ),
            lambda: policy_land_protection_from_solar_pv_sp(),
        )
        .expand_dims({"LANDS_MAP_I": ["SOLAR_LAND"]}, 2)
        .values
    )
    return value


@component.add(
    name="global_loss_of_agricultural_land_by_sea_level_rise",
    units="km2",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"cropland_loss_due_to_sea_level_rise_by_region": 1},
)
def global_loss_of_agricultural_land_by_sea_level_rise():
    """
    the global loss of agricultural land by sea level rise for world
    """
    return sum(
        cropland_loss_due_to_sea_level_rise_by_region().rename(
            {"REGIONS_9_I": "REGIONS_9_I!"}
        ),
        dim=["REGIONS_9_I!"],
    )


@component.add(
    name="growth_land_uses_vs_2015",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LANDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "land_use_area_by_region": 1, "land_uses_until_2015": 1},
)
def growth_land_uses_vs_2015():
    """
    Growth in land uses with relation to the year 2015. Used to endogenize solar rooftop potential with urban land variation in the energy module.
    """
    return if_then_else(
        time() > 2015,
        lambda: zidz(land_use_area_by_region(), land_uses_until_2015()),
        lambda: xr.DataArray(
            1,
            {
                "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                "LANDS_I": _subscript_dict["LANDS_I"],
            },
            ["REGIONS_9_I", "LANDS_I"],
        ),
    )


@component.add(
    name="historical_land_use_by_region_t",
    units="km2/Year",
    subscripts=["REGIONS_9_I", "LANDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "historical_land_use_by_region": 1},
)
def historical_land_use_by_region_t():
    """
    Historical data of land use by region
    """
    return historical_land_use_by_region(time())


@component.add(
    name="land_protection_by_policy",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LANDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_land_production_policy": 1,
        "time": 2,
        "year_initial_land_protecion_policy": 1,
        "year_final_land_protection_policy": 1,
        "objective_land_protection_policy": 1,
    },
)
def land_protection_by_policy():
    """
    share of the initial land of each type in 2015 that is protected from changes to other uses
    """
    return if_then_else(
        np.logical_and(
            switch_land_production_policy() == 1,
            np.logical_and(
                time() > year_initial_land_protecion_policy(),
                time() < year_final_land_protection_policy(),
            ),
        ),
        lambda: objective_land_protection_policy(),
        lambda: xr.DataArray(
            0,
            {
                "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                "LANDS_I": _subscript_dict["LANDS_I"],
            },
            ["REGIONS_9_I", "LANDS_I"],
        ),
    )


@component.add(
    name="land_use_area_by_region",
    units="km2",
    subscripts=["REGIONS_9_I", "LANDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "land_use_area_productive_uses": 10,
        "snow_ice_and_waterbodies_area": 3,
        "wetland_area": 3,
        "share_of_shrubland": 2,
    },
)
def land_use_area_by_region():
    """
    land use area by region
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "LANDS_I": _subscript_dict["LANDS_I"],
        },
        ["REGIONS_9_I", "LANDS_I"],
    )
    value.loc[:, ["CROPLAND_RAINFED"]] = (
        land_use_area_productive_uses()
        .loc[:, "CROPLAND_RAINFED"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS_I": ["CROPLAND_RAINFED"]}, 1)
        .values
    )
    value.loc[:, ["CROPLAND_IRRIGATED"]] = (
        land_use_area_productive_uses()
        .loc[:, "CROPLAND_IRRIGATED"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS_I": ["CROPLAND_IRRIGATED"]}, 1)
        .values
    )
    value.loc[:, ["FOREST_MANAGED"]] = (
        land_use_area_productive_uses()
        .loc[:, "FOREST_MANAGED"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS_FOREST_I": ["FOREST_MANAGED"]}, 1)
        .values
    )
    value.loc[:, ["FOREST_PRIMARY"]] = (
        land_use_area_productive_uses()
        .loc[:, "FOREST_PRIMARY"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS_FOREST_I": ["FOREST_PRIMARY"]}, 1)
        .values
    )
    value.loc[:, ["FOREST_PLANTATIONS"]] = (
        land_use_area_productive_uses()
        .loc[:, "FOREST_PLANTATIONS"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS_FOREST_I": ["FOREST_PLANTATIONS"]}, 1)
        .values
    )
    value.loc[:, ["SHRUBLAND"]] = (
        (
            (
                land_use_area_productive_uses()
                .loc[:, "OTHER_LAND"]
                .reset_coords(drop=True)
                - wetland_area()
                - snow_ice_and_waterbodies_area()
            )
            * share_of_shrubland()
        )
        .expand_dims({"LANDS_I": ["SHRUBLAND"]}, 1)
        .values
    )
    value.loc[:, ["GRASSLAND"]] = (
        land_use_area_productive_uses()
        .loc[:, "GRASSLAND"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS_I": ["GRASSLAND"]}, 1)
        .values
    )
    value.loc[:, ["WETLAND"]] = (
        wetland_area().expand_dims({"LANDS_I": ["WETLAND"]}, 1).values
    )
    value.loc[:, ["URBAN_LAND"]] = (
        land_use_area_productive_uses()
        .loc[:, "URBAN_LAND"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS_I": ["URBAN_LAND"]}, 1)
        .values
    )
    value.loc[:, ["SOLAR_LAND"]] = (
        land_use_area_productive_uses()
        .loc[:, "SOLAR_LAND"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS_I": ["SOLAR_LAND"]}, 1)
        .values
    )
    value.loc[:, ["SNOW_ICE_WATERBODIES"]] = (
        snow_ice_and_waterbodies_area()
        .expand_dims({"LANDS_I": ["SNOW_ICE_WATERBODIES"]}, 1)
        .values
    )
    value.loc[:, ["OTHER_LAND"]] = (
        (
            (
                land_use_area_productive_uses()
                .loc[:, "OTHER_LAND"]
                .reset_coords(drop=True)
                - wetland_area()
                - snow_ice_and_waterbodies_area()
            )
            * (1 - share_of_shrubland())
        )
        .expand_dims({"LANDS_I": ["OTHER_LAND"]}, 1)
        .values
    )
    return value


@component.add(
    name="land_use_area_productive_uses",
    units="km2",
    subscripts=["REGIONS_9_I", "LANDS_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={
        "_integ_land_use_area_productive_uses": 1,
        "_integ_land_use_area_productive_uses_1": 1,
        "_integ_land_use_area_productive_uses_2": 1,
        "_integ_land_use_area_productive_uses_3": 1,
        "_integ_land_use_area_productive_uses_4": 1,
        "_integ_land_use_area_productive_uses_5": 1,
        "_integ_land_use_area_productive_uses_6": 1,
        "_integ_land_use_area_productive_uses_7": 1,
        "_integ_land_use_area_productive_uses_8": 1,
        "_integ_land_use_area_productive_uses_9": 1,
        "_integ_land_use_area_productive_uses_10": 1,
        "_integ_land_use_area_productive_uses_11": 1,
    },
    other_deps={
        "_integ_land_use_area_productive_uses": {
            "initial": {"initial_land_use_by_region": 1},
            "step": {"land_use_changes_productive_uses": 1},
        },
        "_integ_land_use_area_productive_uses_1": {
            "initial": {"initial_land_use_by_region": 1},
            "step": {"land_use_changes_productive_uses": 1},
        },
        "_integ_land_use_area_productive_uses_2": {
            "initial": {"initial_land_use_by_region": 1},
            "step": {"land_use_changes_productive_uses": 1},
        },
        "_integ_land_use_area_productive_uses_3": {
            "initial": {"initial_land_use_by_region": 1},
            "step": {"land_use_changes_productive_uses": 1},
        },
        "_integ_land_use_area_productive_uses_4": {
            "initial": {"initial_land_use_by_region": 1},
            "step": {"land_use_changes_productive_uses": 1},
        },
        "_integ_land_use_area_productive_uses_5": {
            "initial": {},
            "step": {"land_use_changes_productive_uses": 1},
        },
        "_integ_land_use_area_productive_uses_6": {
            "initial": {"initial_land_use_by_region": 1},
            "step": {"land_use_changes_productive_uses": 1},
        },
        "_integ_land_use_area_productive_uses_7": {
            "initial": {},
            "step": {"land_use_changes_productive_uses": 1},
        },
        "_integ_land_use_area_productive_uses_8": {
            "initial": {"initial_land_use_by_region": 1},
            "step": {"land_use_changes_productive_uses": 1},
        },
        "_integ_land_use_area_productive_uses_9": {
            "initial": {"initial_land_use_by_region": 1},
            "step": {"land_use_changes_productive_uses": 1},
        },
        "_integ_land_use_area_productive_uses_10": {
            "initial": {},
            "step": {"land_use_changes_productive_uses": 1},
        },
        "_integ_land_use_area_productive_uses_11": {
            "initial": {"initial_land_use_by_region": 4},
            "step": {"land_use_changes_productive_uses": 4},
        },
    },
)
def land_use_area_productive_uses():
    """
    stock of land uses area productive uses by region
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "LANDS_I": _subscript_dict["LANDS_I"],
        },
        ["REGIONS_9_I", "LANDS_I"],
    )
    value.loc[:, ["CROPLAND_RAINFED"]] = _integ_land_use_area_productive_uses().values
    value.loc[
        :, ["CROPLAND_IRRIGATED"]
    ] = _integ_land_use_area_productive_uses_1().values
    value.loc[:, ["FOREST_MANAGED"]] = _integ_land_use_area_productive_uses_2().values
    value.loc[:, ["FOREST_PRIMARY"]] = _integ_land_use_area_productive_uses_3().values
    value.loc[
        :, ["FOREST_PLANTATIONS"]
    ] = _integ_land_use_area_productive_uses_4().values
    value.loc[:, ["SHRUBLAND"]] = _integ_land_use_area_productive_uses_5().values
    value.loc[:, ["GRASSLAND"]] = _integ_land_use_area_productive_uses_6().values
    value.loc[:, ["WETLAND"]] = _integ_land_use_area_productive_uses_7().values
    value.loc[:, ["URBAN_LAND"]] = _integ_land_use_area_productive_uses_8().values
    value.loc[:, ["SOLAR_LAND"]] = _integ_land_use_area_productive_uses_9().values
    value.loc[
        :, ["SNOW_ICE_WATERBODIES"]
    ] = _integ_land_use_area_productive_uses_10().values
    value.loc[:, ["OTHER_LAND"]] = _integ_land_use_area_productive_uses_11().values
    return value


_integ_land_use_area_productive_uses = Integ(
    lambda: land_use_changes_productive_uses()
    .loc[:, "CROPLAND_RAINFED"]
    .reset_coords(drop=True)
    .expand_dims({"LANDS_I": ["CROPLAND_RAINFED"]}, 1),
    lambda: initial_land_use_by_region()
    .loc[:, "CROPLAND_RAINFED"]
    .reset_coords(drop=True)
    .expand_dims({"LANDS_I": ["CROPLAND_RAINFED"]}, 1),
    "_integ_land_use_area_productive_uses",
)

_integ_land_use_area_productive_uses_1 = Integ(
    lambda: land_use_changes_productive_uses()
    .loc[:, "CROPLAND_IRRIGATED"]
    .reset_coords(drop=True)
    .expand_dims({"LANDS_I": ["CROPLAND_IRRIGATED"]}, 1),
    lambda: initial_land_use_by_region()
    .loc[:, "CROPLAND_IRRIGATED"]
    .reset_coords(drop=True)
    .expand_dims({"LANDS_I": ["CROPLAND_IRRIGATED"]}, 1),
    "_integ_land_use_area_productive_uses_1",
)

_integ_land_use_area_productive_uses_2 = Integ(
    lambda: land_use_changes_productive_uses()
    .loc[:, "FOREST_MANAGED"]
    .reset_coords(drop=True)
    .expand_dims({"LANDS_FOREST_I": ["FOREST_MANAGED"]}, 1),
    lambda: initial_land_use_by_region()
    .loc[:, "FOREST_MANAGED"]
    .reset_coords(drop=True)
    .expand_dims({"LANDS_FOREST_I": ["FOREST_MANAGED"]}, 1),
    "_integ_land_use_area_productive_uses_2",
)

_integ_land_use_area_productive_uses_3 = Integ(
    lambda: land_use_changes_productive_uses()
    .loc[:, "FOREST_PRIMARY"]
    .reset_coords(drop=True)
    .expand_dims({"LANDS_FOREST_I": ["FOREST_PRIMARY"]}, 1),
    lambda: initial_land_use_by_region()
    .loc[:, "FOREST_PRIMARY"]
    .reset_coords(drop=True)
    .expand_dims({"LANDS_FOREST_I": ["FOREST_PRIMARY"]}, 1),
    "_integ_land_use_area_productive_uses_3",
)

_integ_land_use_area_productive_uses_4 = Integ(
    lambda: land_use_changes_productive_uses()
    .loc[:, "FOREST_PLANTATIONS"]
    .reset_coords(drop=True)
    .expand_dims({"LANDS_FOREST_I": ["FOREST_PLANTATIONS"]}, 1),
    lambda: initial_land_use_by_region()
    .loc[:, "FOREST_PLANTATIONS"]
    .reset_coords(drop=True)
    .expand_dims({"LANDS_FOREST_I": ["FOREST_PLANTATIONS"]}, 1),
    "_integ_land_use_area_productive_uses_4",
)

_integ_land_use_area_productive_uses_5 = Integ(
    lambda: land_use_changes_productive_uses()
    .loc[:, "SHRUBLAND"]
    .reset_coords(drop=True)
    .expand_dims({"LANDS_I": ["SHRUBLAND"]}, 1),
    lambda: xr.DataArray(
        0,
        {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"], "LANDS_I": ["SHRUBLAND"]},
        ["REGIONS_9_I", "LANDS_I"],
    ),
    "_integ_land_use_area_productive_uses_5",
)

_integ_land_use_area_productive_uses_6 = Integ(
    lambda: land_use_changes_productive_uses()
    .loc[:, "GRASSLAND"]
    .reset_coords(drop=True)
    .expand_dims({"LANDS_I": ["GRASSLAND"]}, 1),
    lambda: initial_land_use_by_region()
    .loc[:, "GRASSLAND"]
    .reset_coords(drop=True)
    .expand_dims({"LANDS_I": ["GRASSLAND"]}, 1),
    "_integ_land_use_area_productive_uses_6",
)

_integ_land_use_area_productive_uses_7 = Integ(
    lambda: land_use_changes_productive_uses()
    .loc[:, "WETLAND"]
    .reset_coords(drop=True)
    .expand_dims({"LANDS_I": ["WETLAND"]}, 1),
    lambda: xr.DataArray(
        0,
        {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"], "LANDS_I": ["WETLAND"]},
        ["REGIONS_9_I", "LANDS_I"],
    ),
    "_integ_land_use_area_productive_uses_7",
)

_integ_land_use_area_productive_uses_8 = Integ(
    lambda: land_use_changes_productive_uses()
    .loc[:, "URBAN_LAND"]
    .reset_coords(drop=True)
    .expand_dims({"LANDS_I": ["URBAN_LAND"]}, 1),
    lambda: initial_land_use_by_region()
    .loc[:, "URBAN_LAND"]
    .reset_coords(drop=True)
    .expand_dims({"LANDS_I": ["URBAN_LAND"]}, 1),
    "_integ_land_use_area_productive_uses_8",
)

_integ_land_use_area_productive_uses_9 = Integ(
    lambda: land_use_changes_productive_uses()
    .loc[:, "SOLAR_LAND"]
    .reset_coords(drop=True)
    .expand_dims({"LANDS_I": ["SOLAR_LAND"]}, 1),
    lambda: initial_land_use_by_region()
    .loc[:, "SOLAR_LAND"]
    .reset_coords(drop=True)
    .expand_dims({"LANDS_I": ["SOLAR_LAND"]}, 1),
    "_integ_land_use_area_productive_uses_9",
)

_integ_land_use_area_productive_uses_10 = Integ(
    lambda: land_use_changes_productive_uses()
    .loc[:, "SNOW_ICE_WATERBODIES"]
    .reset_coords(drop=True)
    .expand_dims({"LANDS_I": ["SNOW_ICE_WATERBODIES"]}, 1),
    lambda: xr.DataArray(
        0,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "LANDS_I": ["SNOW_ICE_WATERBODIES"],
        },
        ["REGIONS_9_I", "LANDS_I"],
    ),
    "_integ_land_use_area_productive_uses_10",
)

_integ_land_use_area_productive_uses_11 = Integ(
    lambda: (
        land_use_changes_productive_uses().loc[:, "OTHER_LAND"].reset_coords(drop=True)
        + land_use_changes_productive_uses()
        .loc[:, "SNOW_ICE_WATERBODIES"]
        .reset_coords(drop=True)
        + land_use_changes_productive_uses().loc[:, "WETLAND"].reset_coords(drop=True)
        + land_use_changes_productive_uses().loc[:, "SHRUBLAND"].reset_coords(drop=True)
    ).expand_dims({"LANDS_I": ["OTHER_LAND"]}, 1),
    lambda: (
        initial_land_use_by_region().loc[:, "OTHER_LAND"].reset_coords(drop=True)
        + initial_land_use_by_region()
        .loc[:, "SNOW_ICE_WATERBODIES"]
        .reset_coords(drop=True)
        + initial_land_use_by_region().loc[:, "WETLAND"].reset_coords(drop=True)
        + initial_land_use_by_region().loc[:, "SHRUBLAND"].reset_coords(drop=True)
    ).expand_dims({"LANDS_I": ["OTHER_LAND"]}, 1),
    "_integ_land_use_area_productive_uses_11",
)


@component.add(
    name="land_use_by_region_calibrated",
    units="km2",
    subscripts=["REGIONS_9_I", "LANDS_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={
        "_integ_land_use_by_region_calibrated": 1,
        "_integ_land_use_by_region_calibrated_1": 1,
        "_integ_land_use_by_region_calibrated_2": 1,
        "_integ_land_use_by_region_calibrated_3": 1,
        "_integ_land_use_by_region_calibrated_4": 1,
        "_integ_land_use_by_region_calibrated_5": 1,
        "_integ_land_use_by_region_calibrated_6": 1,
        "_integ_land_use_by_region_calibrated_7": 1,
        "_integ_land_use_by_region_calibrated_8": 1,
        "_integ_land_use_by_region_calibrated_9": 1,
        "_integ_land_use_by_region_calibrated_10": 1,
        "_integ_land_use_by_region_calibrated_11": 1,
    },
    other_deps={
        "_integ_land_use_by_region_calibrated": {
            "initial": {"initial_land_use_by_region": 1},
            "step": {"land_use_changes_by_region_calibrated": 1},
        },
        "_integ_land_use_by_region_calibrated_1": {
            "initial": {"initial_land_use_by_region": 1},
            "step": {"land_use_changes_by_region_calibrated": 1},
        },
        "_integ_land_use_by_region_calibrated_2": {
            "initial": {"initial_land_use_by_region": 1},
            "step": {"land_use_changes_by_region_calibrated": 1},
        },
        "_integ_land_use_by_region_calibrated_3": {
            "initial": {"initial_land_use_by_region": 1},
            "step": {"land_use_changes_by_region_calibrated": 1},
        },
        "_integ_land_use_by_region_calibrated_4": {
            "initial": {"initial_land_use_by_region": 1},
            "step": {"land_use_changes_by_region_calibrated": 1},
        },
        "_integ_land_use_by_region_calibrated_5": {
            "initial": {},
            "step": {"land_use_changes_by_region_calibrated": 1},
        },
        "_integ_land_use_by_region_calibrated_6": {
            "initial": {"initial_land_use_by_region": 1},
            "step": {"land_use_changes_by_region_calibrated": 1},
        },
        "_integ_land_use_by_region_calibrated_7": {
            "initial": {},
            "step": {"land_use_changes_by_region_calibrated": 1},
        },
        "_integ_land_use_by_region_calibrated_8": {
            "initial": {"initial_land_use_by_region": 1},
            "step": {"land_use_changes_by_region_calibrated": 1},
        },
        "_integ_land_use_by_region_calibrated_9": {
            "initial": {"initial_land_use_by_region": 1},
            "step": {"land_use_changes_by_region_calibrated": 1},
        },
        "_integ_land_use_by_region_calibrated_10": {
            "initial": {},
            "step": {"land_use_changes_by_region_calibrated": 1},
        },
        "_integ_land_use_by_region_calibrated_11": {
            "initial": {"initial_land_use_by_region": 4},
            "step": {"land_use_changes_by_region_calibrated": 4},
        },
    },
)
def land_use_by_region_calibrated():
    """
    stock of calibrated land use changes by region
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "LANDS_I": _subscript_dict["LANDS_I"],
        },
        ["REGIONS_9_I", "LANDS_I"],
    )
    value.loc[:, ["CROPLAND_RAINFED"]] = _integ_land_use_by_region_calibrated().values
    value.loc[
        :, ["CROPLAND_IRRIGATED"]
    ] = _integ_land_use_by_region_calibrated_1().values
    value.loc[:, ["FOREST_MANAGED"]] = _integ_land_use_by_region_calibrated_2().values
    value.loc[:, ["FOREST_PRIMARY"]] = _integ_land_use_by_region_calibrated_3().values
    value.loc[
        :, ["FOREST_PLANTATIONS"]
    ] = _integ_land_use_by_region_calibrated_4().values
    value.loc[:, ["SHRUBLAND"]] = _integ_land_use_by_region_calibrated_5().values
    value.loc[:, ["GRASSLAND"]] = _integ_land_use_by_region_calibrated_6().values
    value.loc[:, ["WETLAND"]] = _integ_land_use_by_region_calibrated_7().values
    value.loc[:, ["URBAN_LAND"]] = _integ_land_use_by_region_calibrated_8().values
    value.loc[:, ["SOLAR_LAND"]] = _integ_land_use_by_region_calibrated_9().values
    value.loc[
        :, ["SNOW_ICE_WATERBODIES"]
    ] = _integ_land_use_by_region_calibrated_10().values
    value.loc[:, ["OTHER_LAND"]] = _integ_land_use_by_region_calibrated_11().values
    return value


_integ_land_use_by_region_calibrated = Integ(
    lambda: land_use_changes_by_region_calibrated()
    .loc["CROPLAND_RAINFED", :]
    .reset_coords(drop=True)
    .expand_dims({"LANDS_I": ["CROPLAND_RAINFED"]}, 1),
    lambda: initial_land_use_by_region()
    .loc[:, "CROPLAND_RAINFED"]
    .reset_coords(drop=True)
    .expand_dims({"LANDS_I": ["CROPLAND_RAINFED"]}, 1),
    "_integ_land_use_by_region_calibrated",
)

_integ_land_use_by_region_calibrated_1 = Integ(
    lambda: land_use_changes_by_region_calibrated()
    .loc["CROPLAND_IRRIGATED", :]
    .reset_coords(drop=True)
    .expand_dims({"LANDS_I": ["CROPLAND_IRRIGATED"]}, 1),
    lambda: initial_land_use_by_region()
    .loc[:, "CROPLAND_IRRIGATED"]
    .reset_coords(drop=True)
    .expand_dims({"LANDS_I": ["CROPLAND_IRRIGATED"]}, 1),
    "_integ_land_use_by_region_calibrated_1",
)

_integ_land_use_by_region_calibrated_2 = Integ(
    lambda: land_use_changes_by_region_calibrated()
    .loc["FOREST_MANAGED", :]
    .reset_coords(drop=True)
    .expand_dims({"LANDS_FOREST_I": ["FOREST_MANAGED"]}, 1),
    lambda: initial_land_use_by_region()
    .loc[:, "FOREST_MANAGED"]
    .reset_coords(drop=True)
    .expand_dims({"LANDS_FOREST_I": ["FOREST_MANAGED"]}, 1),
    "_integ_land_use_by_region_calibrated_2",
)

_integ_land_use_by_region_calibrated_3 = Integ(
    lambda: land_use_changes_by_region_calibrated()
    .loc["FOREST_PRIMARY", :]
    .reset_coords(drop=True)
    .expand_dims({"LANDS_FOREST_I": ["FOREST_PRIMARY"]}, 1),
    lambda: initial_land_use_by_region()
    .loc[:, "FOREST_PRIMARY"]
    .reset_coords(drop=True)
    .expand_dims({"LANDS_FOREST_I": ["FOREST_PRIMARY"]}, 1),
    "_integ_land_use_by_region_calibrated_3",
)

_integ_land_use_by_region_calibrated_4 = Integ(
    lambda: land_use_changes_by_region_calibrated()
    .loc["FOREST_PLANTATIONS", :]
    .reset_coords(drop=True)
    .expand_dims({"LANDS_FOREST_I": ["FOREST_PLANTATIONS"]}, 1),
    lambda: initial_land_use_by_region()
    .loc[:, "FOREST_PLANTATIONS"]
    .reset_coords(drop=True)
    .expand_dims({"LANDS_FOREST_I": ["FOREST_PLANTATIONS"]}, 1),
    "_integ_land_use_by_region_calibrated_4",
)

_integ_land_use_by_region_calibrated_5 = Integ(
    lambda: land_use_changes_by_region_calibrated()
    .loc["SHRUBLAND", :]
    .reset_coords(drop=True)
    .expand_dims({"LANDS_I": ["SHRUBLAND"]}, 1),
    lambda: xr.DataArray(
        0,
        {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"], "LANDS_I": ["SHRUBLAND"]},
        ["REGIONS_9_I", "LANDS_I"],
    ),
    "_integ_land_use_by_region_calibrated_5",
)

_integ_land_use_by_region_calibrated_6 = Integ(
    lambda: land_use_changes_by_region_calibrated()
    .loc["GRASSLAND", :]
    .reset_coords(drop=True)
    .expand_dims({"LANDS_I": ["GRASSLAND"]}, 1),
    lambda: initial_land_use_by_region()
    .loc[:, "GRASSLAND"]
    .reset_coords(drop=True)
    .expand_dims({"LANDS_I": ["GRASSLAND"]}, 1),
    "_integ_land_use_by_region_calibrated_6",
)

_integ_land_use_by_region_calibrated_7 = Integ(
    lambda: land_use_changes_by_region_calibrated()
    .loc["WETLAND", :]
    .reset_coords(drop=True)
    .expand_dims({"LANDS_I": ["WETLAND"]}, 1),
    lambda: xr.DataArray(
        0,
        {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"], "LANDS_I": ["WETLAND"]},
        ["REGIONS_9_I", "LANDS_I"],
    ),
    "_integ_land_use_by_region_calibrated_7",
)

_integ_land_use_by_region_calibrated_8 = Integ(
    lambda: land_use_changes_by_region_calibrated()
    .loc["URBAN_LAND", :]
    .reset_coords(drop=True)
    .expand_dims({"LANDS_I": ["URBAN_LAND"]}, 1),
    lambda: initial_land_use_by_region()
    .loc[:, "URBAN_LAND"]
    .reset_coords(drop=True)
    .expand_dims({"LANDS_I": ["URBAN_LAND"]}, 1),
    "_integ_land_use_by_region_calibrated_8",
)

_integ_land_use_by_region_calibrated_9 = Integ(
    lambda: land_use_changes_by_region_calibrated()
    .loc["SOLAR_LAND", :]
    .reset_coords(drop=True)
    .expand_dims({"LANDS_I": ["SOLAR_LAND"]}, 1),
    lambda: initial_land_use_by_region()
    .loc[:, "SOLAR_LAND"]
    .reset_coords(drop=True)
    .expand_dims({"LANDS_I": ["SOLAR_LAND"]}, 1),
    "_integ_land_use_by_region_calibrated_9",
)

_integ_land_use_by_region_calibrated_10 = Integ(
    lambda: land_use_changes_by_region_calibrated()
    .loc["SNOW_ICE_WATERBODIES", :]
    .reset_coords(drop=True)
    .expand_dims({"LANDS_I": ["SNOW_ICE_WATERBODIES"]}, 1),
    lambda: xr.DataArray(
        0,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "LANDS_I": ["SNOW_ICE_WATERBODIES"],
        },
        ["REGIONS_9_I", "LANDS_I"],
    ),
    "_integ_land_use_by_region_calibrated_10",
)

_integ_land_use_by_region_calibrated_11 = Integ(
    lambda: (
        land_use_changes_by_region_calibrated()
        .loc["OTHER_LAND", :]
        .reset_coords(drop=True)
        + land_use_changes_by_region_calibrated()
        .loc["SNOW_ICE_WATERBODIES", :]
        .reset_coords(drop=True)
        + land_use_changes_by_region_calibrated()
        .loc["WETLAND", :]
        .reset_coords(drop=True)
        + land_use_changes_by_region_calibrated()
        .loc["SHRUBLAND", :]
        .reset_coords(drop=True)
    ).expand_dims({"LANDS_I": ["OTHER_LAND"]}, 1),
    lambda: (
        initial_land_use_by_region().loc[:, "OTHER_LAND"].reset_coords(drop=True)
        + initial_land_use_by_region()
        .loc[:, "SNOW_ICE_WATERBODIES"]
        .reset_coords(drop=True)
        + initial_land_use_by_region().loc[:, "WETLAND"].reset_coords(drop=True)
        + initial_land_use_by_region().loc[:, "SHRUBLAND"].reset_coords(drop=True)
    ).expand_dims({"LANDS_I": ["OTHER_LAND"]}, 1),
    "_integ_land_use_by_region_calibrated_11",
)


@component.add(
    name="land_use_changes_by_region_calibrated",
    units="km2/Year",
    subscripts=["LANDS_I", "REGIONS_9_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={"vector_of_land_use_changes": 13},
)
def land_use_changes_by_region_calibrated():
    """
    calibrated land use changes by region
    """
    value = xr.DataArray(
        np.nan,
        {
            "LANDS_I": _subscript_dict["LANDS_I"],
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        },
        ["LANDS_I", "REGIONS_9_I"],
    )
    value.loc[["CROPLAND_RAINFED"], :] = (
        vector_of_land_use_changes()
        .loc[:, "CROPLAND_RAINFED"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS_I": ["CROPLAND_RAINFED"]}, 0)
        .values
    )
    value.loc[["CROPLAND_IRRIGATED"], :] = (
        vector_of_land_use_changes()
        .loc[:, "CROPLAND_IRRIGATED"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS_I": ["CROPLAND_IRRIGATED"]}, 0)
        .values
    )
    value.loc[["FOREST_MANAGED"], :] = (
        vector_of_land_use_changes()
        .loc[:, "FOREST_MANAGED"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS_FOREST_I": ["FOREST_MANAGED"]}, 0)
        .values
    )
    value.loc[["FOREST_PRIMARY"], :] = (
        vector_of_land_use_changes()
        .loc[:, "FOREST_PRIMARY"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS_FOREST_I": ["FOREST_PRIMARY"]}, 0)
        .values
    )
    value.loc[["FOREST_PLANTATIONS"], :] = (
        vector_of_land_use_changes()
        .loc[:, "FOREST_PLANTATIONS"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS_FOREST_I": ["FOREST_PLANTATIONS"]}, 0)
        .values
    )
    value.loc[["SHRUBLAND"], :] = 0
    value.loc[["GRASSLAND"], :] = (
        vector_of_land_use_changes()
        .loc[:, "GRASSLAND"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS_I": ["GRASSLAND"]}, 0)
        .values
    )
    value.loc[["WETLAND"], :] = 0
    value.loc[["URBAN_LAND"], :] = (
        vector_of_land_use_changes()
        .loc[:, "URBAN_LAND"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS_I": ["URBAN_LAND"]}, 0)
        .values
    )
    value.loc[["SOLAR_LAND"], :] = (
        vector_of_land_use_changes()
        .loc[:, "SOLAR_LAND"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS_I": ["SOLAR_LAND"]}, 0)
        .values
    )
    value.loc[["SNOW_ICE_WATERBODIES"], :] = (
        vector_of_land_use_changes()
        .loc[:, "SNOW_ICE_WATERBODIES"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS_I": ["SNOW_ICE_WATERBODIES"]}, 0)
        .values
    )
    value.loc[["OTHER_LAND"], :] = (
        (
            vector_of_land_use_changes().loc[:, "OTHER_LAND"].reset_coords(drop=True)
            + vector_of_land_use_changes().loc[:, "SOLAR_LAND"].reset_coords(drop=True)
            + vector_of_land_use_changes().loc[:, "WETLAND"].reset_coords(drop=True)
            + vector_of_land_use_changes().loc[:, "SHRUBLAND"].reset_coords(drop=True)
        )
        .expand_dims({"LANDS_I": ["OTHER_LAND"]}, 0)
        .values
    )
    return value


@component.add(
    name="land_use_changes_productive_uses",
    units="km2/Year",
    subscripts=["REGIONS_9_I", "LANDS_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 21,
        "time_historical_data_land_module": 9,
        "historical_land_use_change_by_region": 12,
        "vector_of_land_use_changes": 12,
    },
)
def land_use_changes_productive_uses():
    """
    land use changes for productive uses by region
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "LANDS_I": _subscript_dict["LANDS_I"],
        },
        ["REGIONS_9_I", "LANDS_I"],
    )
    value.loc[:, ["CROPLAND_RAINFED"]] = (
        if_then_else(
            time() <= time_historical_data_land_module(),
            lambda: historical_land_use_change_by_region(time())
            .loc[:, "CROPLAND_RAINFED"]
            .reset_coords(drop=True),
            lambda: vector_of_land_use_changes()
            .loc[:, "CROPLAND_RAINFED"]
            .reset_coords(drop=True),
        )
        .expand_dims({"LANDS_I": ["CROPLAND_RAINFED"]}, 1)
        .values
    )
    value.loc[:, ["CROPLAND_IRRIGATED"]] = (
        if_then_else(
            time() <= time_historical_data_land_module(),
            lambda: historical_land_use_change_by_region(time())
            .loc[:, "CROPLAND_IRRIGATED"]
            .reset_coords(drop=True),
            lambda: vector_of_land_use_changes()
            .loc[:, "CROPLAND_IRRIGATED"]
            .reset_coords(drop=True),
        )
        .expand_dims({"LANDS_I": ["CROPLAND_IRRIGATED"]}, 1)
        .values
    )
    value.loc[:, ["FOREST_MANAGED"]] = (
        if_then_else(
            time() <= time_historical_data_land_module(),
            lambda: historical_land_use_change_by_region(time())
            .loc[:, "FOREST_MANAGED"]
            .reset_coords(drop=True),
            lambda: vector_of_land_use_changes()
            .loc[:, "FOREST_MANAGED"]
            .reset_coords(drop=True),
        )
        .expand_dims({"LANDS_FOREST_I": ["FOREST_MANAGED"]}, 1)
        .values
    )
    value.loc[:, ["FOREST_PRIMARY"]] = (
        if_then_else(
            time() <= time_historical_data_land_module(),
            lambda: historical_land_use_change_by_region(time())
            .loc[:, "FOREST_PRIMARY"]
            .reset_coords(drop=True),
            lambda: vector_of_land_use_changes()
            .loc[:, "FOREST_PRIMARY"]
            .reset_coords(drop=True),
        )
        .expand_dims({"LANDS_FOREST_I": ["FOREST_PRIMARY"]}, 1)
        .values
    )
    value.loc[:, ["FOREST_PLANTATIONS"]] = (
        if_then_else(
            time() <= time_historical_data_land_module(),
            lambda: historical_land_use_change_by_region(time())
            .loc[:, "FOREST_PLANTATIONS"]
            .reset_coords(drop=True),
            lambda: vector_of_land_use_changes()
            .loc[:, "FOREST_PLANTATIONS"]
            .reset_coords(drop=True),
        )
        .expand_dims({"LANDS_FOREST_I": ["FOREST_PLANTATIONS"]}, 1)
        .values
    )
    value.loc[:, ["SHRUBLAND"]] = 0
    value.loc[:, ["GRASSLAND"]] = (
        if_then_else(
            time() <= time_historical_data_land_module(),
            lambda: historical_land_use_change_by_region(time())
            .loc[:, "GRASSLAND"]
            .reset_coords(drop=True),
            lambda: vector_of_land_use_changes()
            .loc[:, "GRASSLAND"]
            .reset_coords(drop=True),
        )
        .expand_dims({"LANDS_I": ["GRASSLAND"]}, 1)
        .values
    )
    value.loc[:, ["WETLAND"]] = 0
    value.loc[:, ["URBAN_LAND"]] = (
        if_then_else(
            time() <= time_historical_data_land_module(),
            lambda: historical_land_use_change_by_region(time())
            .loc[:, "URBAN_LAND"]
            .reset_coords(drop=True),
            lambda: vector_of_land_use_changes()
            .loc[:, "URBAN_LAND"]
            .reset_coords(drop=True),
        )
        .expand_dims({"LANDS_I": ["URBAN_LAND"]}, 1)
        .values
    )
    value.loc[:, ["SOLAR_LAND"]] = (
        if_then_else(
            time() <= time_historical_data_land_module(),
            lambda: historical_land_use_change_by_region(time())
            .loc[:, "SOLAR_LAND"]
            .reset_coords(drop=True),
            lambda: vector_of_land_use_changes()
            .loc[:, "SOLAR_LAND"]
            .reset_coords(drop=True),
        )
        .expand_dims({"LANDS_I": ["SOLAR_LAND"]}, 1)
        .values
    )
    value.loc[:, ["SNOW_ICE_WATERBODIES"]] = 0
    value.loc[:, ["OTHER_LAND"]] = (
        (
            if_then_else(
                time() <= time_historical_data_land_module(),
                lambda: historical_land_use_change_by_region(time())
                .loc[:, "OTHER_LAND"]
                .reset_coords(drop=True)
                + historical_land_use_change_by_region(time())
                .loc[:, "SNOW_ICE_WATERBODIES"]
                .reset_coords(drop=True)
                + historical_land_use_change_by_region(time())
                .loc[:, "WETLAND"]
                .reset_coords(drop=True)
                + historical_land_use_change_by_region(time())
                .loc[:, "SHRUBLAND"]
                .reset_coords(drop=True),
                lambda: vector_of_land_use_changes()
                .loc[:, "OTHER_LAND"]
                .reset_coords(drop=True)
                + vector_of_land_use_changes()
                .loc[:, "SNOW_ICE_WATERBODIES"]
                .reset_coords(drop=True)
                + vector_of_land_use_changes()
                .loc[:, "WETLAND"]
                .reset_coords(drop=True),
            )
            + vector_of_land_use_changes().loc[:, "SHRUBLAND"].reset_coords(drop=True)
        )
        .expand_dims({"LANDS_I": ["OTHER_LAND"]}, 1)
        .values
    )
    return value


@component.add(
    name="land_uses_until_2015",
    units="km2",
    subscripts=["REGIONS_9_I", "LANDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "land_use_area_by_region": 1, "aux_land_uses_2015": 1},
)
def land_uses_until_2015():
    """
    Land uses fixed in the value of the year 2015 for the subsequent years of the simulation.
    """
    return if_then_else(
        time() < 2015, lambda: land_use_area_by_region(), lambda: aux_land_uses_2015()
    )


@component.add(
    name="LIMITS_TO_SOLAR_LAND_EXPANSION_EROI_MIN",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LANDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_eroi_min_potential_wind_solar_sp": 5,
        "limits_to_solar_land_expansion_eroi_min_0": 1,
        "limits_to_solar_land_expansion_eroi_min_10": 1,
        "limits_to_solar_land_expansion_eroi_min_5": 1,
        "limits_to_solar_land_expansion_eroi_min_2": 1,
        "limits_to_solar_land_expansion_eroi_min_3": 1,
        "limits_to_solar_land_expansion_eroi_min_8": 1,
    },
)
def limits_to_solar_land_expansion_eroi_min():
    """
    Share of are of each land use in 2015 that can be used for solar.
    """
    return if_then_else(
        select_eroi_min_potential_wind_solar_sp() == 0,
        lambda: limits_to_solar_land_expansion_eroi_min_0(),
        lambda: if_then_else(
            select_eroi_min_potential_wind_solar_sp() == 2,
            lambda: limits_to_solar_land_expansion_eroi_min_2(),
            lambda: if_then_else(
                select_eroi_min_potential_wind_solar_sp() == 3,
                lambda: limits_to_solar_land_expansion_eroi_min_3(),
                lambda: if_then_else(
                    select_eroi_min_potential_wind_solar_sp() == 5,
                    lambda: limits_to_solar_land_expansion_eroi_min_5(),
                    lambda: if_then_else(
                        select_eroi_min_potential_wind_solar_sp() == 8,
                        lambda: limits_to_solar_land_expansion_eroi_min_8(),
                        lambda: limits_to_solar_land_expansion_eroi_min_10(),
                    ),
                ),
            ),
        ),
    )


@component.add(
    name="matrix_of_accumulated_land_use_changes",
    units="km2",
    subscripts=["REGIONS_9_I", "LANDS_I", "LANDS_MAP_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_matrix_of_accumulated_land_use_changes": 1},
    other_deps={
        "_integ_matrix_of_accumulated_land_use_changes": {
            "initial": {},
            "step": {"matrix_of_acumulated_land_use_changes": 1},
        }
    },
)
def matrix_of_accumulated_land_use_changes():
    """
    stock of matrix of accumulated land use changes by region
    """
    return _integ_matrix_of_accumulated_land_use_changes()


_integ_matrix_of_accumulated_land_use_changes = Integ(
    lambda: matrix_of_acumulated_land_use_changes(),
    lambda: xr.DataArray(
        0,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "LANDS_I": _subscript_dict["LANDS_I"],
            "LANDS_MAP_I": _subscript_dict["LANDS_MAP_I"],
        },
        ["REGIONS_9_I", "LANDS_I", "LANDS_MAP_I"],
    ),
    "_integ_matrix_of_accumulated_land_use_changes",
)


@component.add(
    name="matrix_of_acumulated_land_use_changes",
    units="km2/Year",
    subscripts=["REGIONS_9_I", "LANDS_I", "LANDS_MAP_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_of_land_use_changes": 1},
)
def matrix_of_acumulated_land_use_changes():
    """
    matrix of acumulated land use changes by region
    """
    return matrix_of_land_use_changes()


@component.add(
    name="matrix_of_land_use_changes",
    units="km2/Year",
    subscripts=["REGIONS_9_I", "LANDS_I", "LANDS_MAP_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "factor_of_minimum_land_limit": 1,
        "factor_of_maximum_land_limit": 1,
        "factor_of_solar_land_limit": 1,
        "matrix_of_land_use_change_demands": 1,
    },
)
def matrix_of_land_use_changes():
    """
    from land use LANDS_I (down) to land use LANDS_MAP_I (right) multiplied by a factor that is 0 when the one that sends reaches its minimum limit and a factor that is 0 when the ose that sends reaches the limit of land suitable for that change *factor_of_maximum_land_use_by_region[LANDS_I,LANDS_I, REGIONS_9_I]*factor_of_minimum_land_use[REGIONS_9_I,LANDS_I]*0+ matrix_of_land_use_change_demand[LANDS_I,LANDS_MAP_I,REGIONS_9_I] matrix_of_land_use_change_demand_by_climatic_zones[LANDS_I,LANDS_MAP_I,CLIMATIC_ZONES _I]*factor_of_minimum_land_use[CLIMATIC_ZONES_I,LANDS_I]*factor_of_maximum_ land_use[LANDS_I,LANDS_MAP_I,CLIMATIC_ZONES_I ]*LAND_USE_CHANGE_SUITABILITY[LANDS_I,LANDS_MAP_I]
    """
    return (
        factor_of_minimum_land_limit()
        * factor_of_maximum_land_limit()
        * factor_of_solar_land_limit()
        * matrix_of_land_use_change_demands()
    )


@component.add(
    name="MATRIX_OF_MAXIMUM_LAND_CHANGES",
    units="km2",
    subscripts=["REGIONS_9_I", "LANDS_I", "LANDS_MAP_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "initial_land_use_by_region_2015": 2,
        "limits_to_land_use_changes_by_region": 1,
        "limits_to_solar_land_expansion_eroi_min": 1,
    },
)
def matrix_of_maximum_land_changes():
    """
    matrix of maximum land changes by region. FROM USE LANDS_I TO USE LANDS_MAP_I is the percent of use LANDS_I (related to the initial value) that can be converted to use LANDS_I
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "LANDS_I": _subscript_dict["LANDS_I"],
            "LANDS_MAP_I": _subscript_dict["LANDS_MAP_I"],
        },
        ["REGIONS_9_I", "LANDS_I", "LANDS_MAP_I"],
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, :, ["SOLAR_LAND"]] = False
    value.values[except_subs.values] = (
        initial_land_use_by_region_2015() * limits_to_land_use_changes_by_region()
    ).values[except_subs.values]
    value.loc[:, :, ["SOLAR_LAND"]] = (
        (initial_land_use_by_region_2015() * limits_to_solar_land_expansion_eroi_min())
        .expand_dims({"LANDS_MAP_I": ["SOLAR_LAND"]}, 2)
        .values
    )
    return value


@component.add(
    name="minimum_limit_land_use_by_policy",
    units="km2",
    subscripts=["REGIONS_9_I", "LANDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_model_explorer": 1,
        "model_explorer_land_protection": 1,
        "initial_land_use_by_region_2015": 2,
        "land_protection_by_policy": 1,
    },
)
def minimum_limit_land_use_by_policy():
    """
    Minimum limit of land use by policy for each region
    """
    return if_then_else(
        switch_model_explorer() == 1,
        lambda: model_explorer_land_protection() * initial_land_use_by_region_2015(),
        lambda: land_protection_by_policy() * initial_land_use_by_region_2015(),
    )


@component.add(
    name="objective_land_protection_policy",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LANDS_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "objective_cropland_protection_sp": 2,
        "objective_managed_forest_protection_sp": 1,
        "objective_primary_forest_protection_sp": 1,
        "objective_natural_land_protection_sp": 2,
        "objective_grassland_protection_sp": 1,
    },
)
def objective_land_protection_policy():
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "LANDS_I": _subscript_dict["LANDS_I"],
        },
        ["REGIONS_9_I", "LANDS_I"],
    )
    value.loc[:, ["CROPLAND_RAINFED"]] = (
        objective_cropland_protection_sp()
        .expand_dims({"LANDS_I": ["CROPLAND_RAINFED"]}, 1)
        .values
    )
    value.loc[:, ["CROPLAND_IRRIGATED"]] = (
        objective_cropland_protection_sp()
        .expand_dims({"LANDS_I": ["CROPLAND_IRRIGATED"]}, 1)
        .values
    )
    value.loc[:, ["FOREST_MANAGED"]] = (
        objective_managed_forest_protection_sp()
        .expand_dims({"LANDS_FOREST_I": ["FOREST_MANAGED"]}, 1)
        .values
    )
    value.loc[:, ["FOREST_PRIMARY"]] = (
        objective_primary_forest_protection_sp()
        .expand_dims({"LANDS_FOREST_I": ["FOREST_PRIMARY"]}, 1)
        .values
    )
    value.loc[:, ["FOREST_PLANTATIONS"]] = 0
    value.loc[:, ["SHRUBLAND"]] = (
        objective_natural_land_protection_sp()
        .expand_dims({"LANDS_I": ["SHRUBLAND"]}, 1)
        .values
    )
    value.loc[:, ["GRASSLAND"]] = (
        objective_grassland_protection_sp()
        .expand_dims({"LANDS_I": ["GRASSLAND"]}, 1)
        .values
    )
    value.loc[:, ["OTHER_LAND"]] = (
        objective_natural_land_protection_sp()
        .expand_dims({"LANDS_I": ["OTHER_LAND"]}, 1)
        .values
    )
    value.loc[:, ["WETLAND"]] = 0
    value.loc[:, ["URBAN_LAND"]] = 0
    value.loc[:, ["SOLAR_LAND"]] = 0
    value.loc[:, ["SNOW_ICE_WATERBODIES"]] = 0
    return value


@component.add(
    name="snow_ice_and_waterbodies_area",
    units="km2",
    subscripts=["REGIONS_9_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_snow_ice_and_waterbodies_area": 1},
    other_deps={
        "_integ_snow_ice_and_waterbodies_area": {
            "initial": {"initial_land_use_by_region": 1},
            "step": {"variation_of_snow_ice_and_waterbodies_area": 1},
        }
    },
)
def snow_ice_and_waterbodies_area():
    """
    stock of snow ice and waterbodies area by region
    """
    return _integ_snow_ice_and_waterbodies_area()


_integ_snow_ice_and_waterbodies_area = Integ(
    lambda: variation_of_snow_ice_and_waterbodies_area(),
    lambda: initial_land_use_by_region()
    .loc[:, "SNOW_ICE_WATERBODIES"]
    .reset_coords(drop=True),
    "_integ_snow_ice_and_waterbodies_area",
)


@component.add(
    name="switch_land_production_policy",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LANDS_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_cropland_protection_sp": 2,
        "switch_managed_forest_protection_sp": 1,
        "switch_primary_forest_protection_sp": 1,
        "switch_natural_land_protection_sp": 2,
        "switch_grassland_protection_sp": 1,
    },
)
def switch_land_production_policy():
    """
    0: deactivate policy the scenario parameter 1: Activate the scenario parameter
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "LANDS_I": _subscript_dict["LANDS_I"],
        },
        ["REGIONS_9_I", "LANDS_I"],
    )
    value.loc[:, ["CROPLAND_RAINFED"]] = (
        switch_cropland_protection_sp()
        .expand_dims({"LANDS_I": ["CROPLAND_RAINFED"]}, 1)
        .values
    )
    value.loc[:, ["CROPLAND_IRRIGATED"]] = (
        switch_cropland_protection_sp()
        .expand_dims({"LANDS_I": ["CROPLAND_IRRIGATED"]}, 1)
        .values
    )
    value.loc[:, ["FOREST_MANAGED"]] = (
        switch_managed_forest_protection_sp()
        .expand_dims({"LANDS_FOREST_I": ["FOREST_MANAGED"]}, 1)
        .values
    )
    value.loc[:, ["FOREST_PRIMARY"]] = (
        switch_primary_forest_protection_sp()
        .expand_dims({"LANDS_FOREST_I": ["FOREST_PRIMARY"]}, 1)
        .values
    )
    value.loc[:, ["FOREST_PLANTATIONS"]] = 0
    value.loc[:, ["SHRUBLAND"]] = (
        switch_natural_land_protection_sp()
        .expand_dims({"LANDS_I": ["SHRUBLAND"]}, 1)
        .values
    )
    value.loc[:, ["GRASSLAND"]] = (
        switch_grassland_protection_sp()
        .expand_dims({"LANDS_I": ["GRASSLAND"]}, 1)
        .values
    )
    value.loc[:, ["OTHER_LAND"]] = (
        switch_natural_land_protection_sp()
        .expand_dims({"LANDS_I": ["OTHER_LAND"]}, 1)
        .values
    )
    value.loc[:, ["WETLAND"]] = 0
    value.loc[:, ["URBAN_LAND"]] = 0
    value.loc[:, ["SOLAR_LAND"]] = 0
    value.loc[:, ["SNOW_ICE_WATERBODIES"]] = 0
    return value


@component.add(
    name="SWITH_LAW_LIMITS_LAND_BY_SOURCE",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_swith_law_limits_land_by_source"},
)
def swith_law_limits_land_by_source():
    """
    =1 The limits to expansion drive by the land type that gives the land =0 limites give by the land use that receives
    """
    return _ext_constant_swith_law_limits_land_by_source()


_ext_constant_swith_law_limits_land_by_source = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITH_LAW_LIMITS_LAND_BY_SOURCE",
    {},
    _root,
    {},
    "_ext_constant_swith_law_limits_land_by_source",
)


@component.add(
    name="variation_of_snow_ice_and_waterbodies_area",
    units="km2",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def variation_of_snow_ice_and_waterbodies_area():
    """
    variation of snow ice and waterbodies area by region
    """
    return xr.DataArray(
        0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
    )


@component.add(
    name="variation_of_wetland_area",
    units="km2",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def variation_of_wetland_area():
    """
    variation of wetland area by region
    """
    return xr.DataArray(
        0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
    )


@component.add(
    name="vector_of_land_use_changes",
    units="km2/Year",
    subscripts=["REGIONS_9_I", "LANDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cropland_loss_due_to_sea_level_rise_by_region": 1,
        "matrix_of_land_use_changes": 24,
    },
)
def vector_of_land_use_changes():
    """
    vector of land use changes by region
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "LANDS_I": _subscript_dict["LANDS_I"],
        },
        ["REGIONS_9_I", "LANDS_I"],
    )
    value.loc[:, ["CROPLAND_RAINFED"]] = (
        (
            cropland_loss_due_to_sea_level_rise_by_region()
            + sum(
                matrix_of_land_use_changes()
                .loc[:, :, "CROPLAND_RAINFED"]
                .reset_coords(drop=True)
                .rename({"LANDS_I": "LANDS_I!"}),
                dim=["LANDS_I!"],
            )
            - sum(
                matrix_of_land_use_changes()
                .loc[:, "CROPLAND_RAINFED", :]
                .reset_coords(drop=True)
                .rename({"LANDS_MAP_I": "LANDS_I!"}),
                dim=["LANDS_I!"],
            )
        )
        .expand_dims({"LANDS_I": ["CROPLAND_RAINFED"]}, 1)
        .values
    )
    value.loc[:, ["CROPLAND_IRRIGATED"]] = (
        (
            sum(
                matrix_of_land_use_changes()
                .loc[:, :, "CROPLAND_IRRIGATED"]
                .reset_coords(drop=True)
                .rename({"LANDS_I": "LANDS_I!"}),
                dim=["LANDS_I!"],
            )
            - sum(
                matrix_of_land_use_changes()
                .loc[:, "CROPLAND_IRRIGATED", :]
                .reset_coords(drop=True)
                .rename({"LANDS_MAP_I": "LANDS_I!"}),
                dim=["LANDS_I!"],
            )
        )
        .expand_dims({"LANDS_I": ["CROPLAND_IRRIGATED"]}, 1)
        .values
    )
    value.loc[:, ["FOREST_MANAGED"]] = (
        (
            sum(
                matrix_of_land_use_changes()
                .loc[:, :, "FOREST_MANAGED"]
                .reset_coords(drop=True)
                .rename({"LANDS_I": "LANDS_I!"}),
                dim=["LANDS_I!"],
            )
            - sum(
                matrix_of_land_use_changes()
                .loc[:, "FOREST_MANAGED", :]
                .reset_coords(drop=True)
                .rename({"LANDS_MAP_I": "LANDS_I!"}),
                dim=["LANDS_I!"],
            )
        )
        .expand_dims({"LANDS_FOREST_I": ["FOREST_MANAGED"]}, 1)
        .values
    )
    value.loc[:, ["FOREST_PRIMARY"]] = (
        (
            sum(
                matrix_of_land_use_changes()
                .loc[:, :, "FOREST_PRIMARY"]
                .reset_coords(drop=True)
                .rename({"LANDS_I": "LANDS_I!"}),
                dim=["LANDS_I!"],
            )
            - sum(
                matrix_of_land_use_changes()
                .loc[:, "FOREST_PRIMARY", :]
                .reset_coords(drop=True)
                .rename({"LANDS_MAP_I": "LANDS_I!"}),
                dim=["LANDS_I!"],
            )
        )
        .expand_dims({"LANDS_FOREST_I": ["FOREST_PRIMARY"]}, 1)
        .values
    )
    value.loc[:, ["FOREST_PLANTATIONS"]] = (
        (
            sum(
                matrix_of_land_use_changes()
                .loc[:, :, "FOREST_PLANTATIONS"]
                .reset_coords(drop=True)
                .rename({"LANDS_I": "LANDS_I!"}),
                dim=["LANDS_I!"],
            )
            - sum(
                matrix_of_land_use_changes()
                .loc[:, "FOREST_PLANTATIONS", :]
                .reset_coords(drop=True)
                .rename({"LANDS_MAP_I": "LANDS_I!"}),
                dim=["LANDS_I!"],
            )
        )
        .expand_dims({"LANDS_FOREST_I": ["FOREST_PLANTATIONS"]}, 1)
        .values
    )
    value.loc[:, ["SHRUBLAND"]] = (
        (
            sum(
                matrix_of_land_use_changes()
                .loc[:, :, "SHRUBLAND"]
                .reset_coords(drop=True)
                .rename({"LANDS_I": "LANDS_I!"}),
                dim=["LANDS_I!"],
            )
            - sum(
                matrix_of_land_use_changes()
                .loc[:, "SHRUBLAND", :]
                .reset_coords(drop=True)
                .rename({"LANDS_MAP_I": "LANDS_I!"}),
                dim=["LANDS_I!"],
            )
        )
        .expand_dims({"LANDS_I": ["SHRUBLAND"]}, 1)
        .values
    )
    value.loc[:, ["GRASSLAND"]] = (
        (
            sum(
                matrix_of_land_use_changes()
                .loc[:, :, "GRASSLAND"]
                .reset_coords(drop=True)
                .rename({"LANDS_I": "LANDS_I!"}),
                dim=["LANDS_I!"],
            )
            - sum(
                matrix_of_land_use_changes()
                .loc[:, "GRASSLAND", :]
                .reset_coords(drop=True)
                .rename({"LANDS_MAP_I": "LANDS_I!"}),
                dim=["LANDS_I!"],
            )
        )
        .expand_dims({"LANDS_I": ["GRASSLAND"]}, 1)
        .values
    )
    value.loc[:, ["WETLAND"]] = (
        (
            sum(
                matrix_of_land_use_changes()
                .loc[:, :, "WETLAND"]
                .reset_coords(drop=True)
                .rename({"LANDS_I": "LANDS_I!"}),
                dim=["LANDS_I!"],
            )
            - sum(
                matrix_of_land_use_changes()
                .loc[:, "WETLAND", :]
                .reset_coords(drop=True)
                .rename({"LANDS_MAP_I": "LANDS_I!"}),
                dim=["LANDS_I!"],
            )
        )
        .expand_dims({"LANDS_I": ["WETLAND"]}, 1)
        .values
    )
    value.loc[:, ["URBAN_LAND"]] = (
        (
            sum(
                matrix_of_land_use_changes()
                .loc[:, :, "URBAN_LAND"]
                .reset_coords(drop=True)
                .rename({"LANDS_I": "LANDS_I!"}),
                dim=["LANDS_I!"],
            )
            - sum(
                matrix_of_land_use_changes()
                .loc[:, "URBAN_LAND", :]
                .reset_coords(drop=True)
                .rename({"LANDS_MAP_I": "LANDS_I!"}),
                dim=["LANDS_I!"],
            )
        )
        .expand_dims({"LANDS_I": ["URBAN_LAND"]}, 1)
        .values
    )
    value.loc[:, ["SOLAR_LAND"]] = (
        (
            sum(
                matrix_of_land_use_changes()
                .loc[:, :, "SOLAR_LAND"]
                .reset_coords(drop=True)
                .rename({"LANDS_I": "LANDS_I!"}),
                dim=["LANDS_I!"],
            )
            - sum(
                matrix_of_land_use_changes()
                .loc[:, "SOLAR_LAND", :]
                .reset_coords(drop=True)
                .rename({"LANDS_MAP_I": "LANDS_I!"}),
                dim=["LANDS_I!"],
            )
        )
        .expand_dims({"LANDS_I": ["SOLAR_LAND"]}, 1)
        .values
    )
    value.loc[:, ["SNOW_ICE_WATERBODIES"]] = (
        (
            sum(
                matrix_of_land_use_changes()
                .loc[:, :, "SNOW_ICE_WATERBODIES"]
                .reset_coords(drop=True)
                .rename({"LANDS_I": "LANDS_I!"}),
                dim=["LANDS_I!"],
            )
            - sum(
                matrix_of_land_use_changes()
                .loc[:, "SNOW_ICE_WATERBODIES", :]
                .reset_coords(drop=True)
                .rename({"LANDS_MAP_I": "LANDS_I!"}),
                dim=["LANDS_I!"],
            )
        )
        .expand_dims({"LANDS_I": ["SNOW_ICE_WATERBODIES"]}, 1)
        .values
    )
    value.loc[:, ["OTHER_LAND"]] = (
        (
            sum(
                matrix_of_land_use_changes()
                .loc[:, :, "OTHER_LAND"]
                .reset_coords(drop=True)
                .rename({"LANDS_I": "LANDS_I!"}),
                dim=["LANDS_I!"],
            )
            - sum(
                matrix_of_land_use_changes()
                .loc[:, "OTHER_LAND", :]
                .reset_coords(drop=True)
                .rename({"LANDS_MAP_I": "LANDS_I!"}),
                dim=["LANDS_I!"],
            )
        )
        .expand_dims({"LANDS_I": ["OTHER_LAND"]}, 1)
        .values
    )
    return value


@component.add(
    name="wetland_area",
    units="km2",
    subscripts=["REGIONS_9_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_wetland_area": 1},
    other_deps={
        "_integ_wetland_area": {
            "initial": {"initial_land_use_by_region": 1},
            "step": {"variation_of_wetland_area": 1},
        }
    },
)
def wetland_area():
    """
    stock of wetland area by region
    """
    return _integ_wetland_area()


_integ_wetland_area = Integ(
    lambda: variation_of_wetland_area(),
    lambda: initial_land_use_by_region().loc[:, "WETLAND"].reset_coords(drop=True),
    "_integ_wetland_area",
)


@component.add(
    name="year_final_land_protection_policy",
    units="Year",
    subscripts=["REGIONS_9_I", "LANDS_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "year_final_cropland_protection_sp": 2,
        "year_final_managed_forest_protection_sp": 1,
        "year_final_primary_forest_protection_sp": 1,
        "year_final_natural_land_protection_sp": 2,
        "year_final_grassland_protection_sp": 1,
    },
)
def year_final_land_protection_policy():
    """
    final year of land protection policies
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "LANDS_I": _subscript_dict["LANDS_I"],
        },
        ["REGIONS_9_I", "LANDS_I"],
    )
    value.loc[:, ["CROPLAND_RAINFED"]] = (
        year_final_cropland_protection_sp()
        .expand_dims({"LANDS_I": ["CROPLAND_RAINFED"]}, 1)
        .values
    )
    value.loc[:, ["CROPLAND_IRRIGATED"]] = (
        year_final_cropland_protection_sp()
        .expand_dims({"LANDS_I": ["CROPLAND_IRRIGATED"]}, 1)
        .values
    )
    value.loc[:, ["FOREST_MANAGED"]] = (
        year_final_managed_forest_protection_sp()
        .expand_dims({"LANDS_FOREST_I": ["FOREST_MANAGED"]}, 1)
        .values
    )
    value.loc[:, ["FOREST_PRIMARY"]] = (
        year_final_primary_forest_protection_sp()
        .expand_dims({"LANDS_FOREST_I": ["FOREST_PRIMARY"]}, 1)
        .values
    )
    value.loc[:, ["FOREST_PLANTATIONS"]] = 0
    value.loc[:, ["SHRUBLAND"]] = (
        year_final_natural_land_protection_sp()
        .expand_dims({"LANDS_I": ["SHRUBLAND"]}, 1)
        .values
    )
    value.loc[:, ["GRASSLAND"]] = (
        year_final_grassland_protection_sp()
        .expand_dims({"LANDS_I": ["GRASSLAND"]}, 1)
        .values
    )
    value.loc[:, ["OTHER_LAND"]] = (
        year_final_natural_land_protection_sp()
        .expand_dims({"LANDS_I": ["OTHER_LAND"]}, 1)
        .values
    )
    value.loc[:, ["WETLAND"]] = 0
    value.loc[:, ["URBAN_LAND"]] = 0
    value.loc[:, ["SOLAR_LAND"]] = 0
    value.loc[:, ["SNOW_ICE_WATERBODIES"]] = 0
    return value


@component.add(
    name="year_initial_land_protecion_policy",
    units="Year",
    subscripts=["REGIONS_9_I", "LANDS_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "year_initial_cropland_protection_sp": 2,
        "year_initial_managed_forest_protection_sp": 1,
        "year_initial_primary_forest_protection_sp": 1,
        "year_initial_natural_land_protection_sp": 2,
        "year_initial_grassland_protection_sp": 1,
    },
)
def year_initial_land_protecion_policy():
    """
    initial year of land protection policies
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "LANDS_I": _subscript_dict["LANDS_I"],
        },
        ["REGIONS_9_I", "LANDS_I"],
    )
    value.loc[:, ["CROPLAND_RAINFED"]] = (
        year_initial_cropland_protection_sp()
        .expand_dims({"LANDS_I": ["CROPLAND_RAINFED"]}, 1)
        .values
    )
    value.loc[:, ["CROPLAND_IRRIGATED"]] = (
        year_initial_cropland_protection_sp()
        .expand_dims({"LANDS_I": ["CROPLAND_IRRIGATED"]}, 1)
        .values
    )
    value.loc[:, ["FOREST_MANAGED"]] = (
        year_initial_managed_forest_protection_sp()
        .expand_dims({"LANDS_FOREST_I": ["FOREST_MANAGED"]}, 1)
        .values
    )
    value.loc[:, ["FOREST_PRIMARY"]] = (
        year_initial_primary_forest_protection_sp()
        .expand_dims({"LANDS_FOREST_I": ["FOREST_PRIMARY"]}, 1)
        .values
    )
    value.loc[:, ["FOREST_PLANTATIONS"]] = 0
    value.loc[:, ["SHRUBLAND"]] = (
        year_initial_natural_land_protection_sp()
        .expand_dims({"LANDS_I": ["SHRUBLAND"]}, 1)
        .values
    )
    value.loc[:, ["GRASSLAND"]] = (
        year_initial_grassland_protection_sp()
        .expand_dims({"LANDS_I": ["GRASSLAND"]}, 1)
        .values
    )
    value.loc[:, ["OTHER_LAND"]] = (
        year_initial_natural_land_protection_sp()
        .expand_dims({"LANDS_I": ["OTHER_LAND"]}, 1)
        .values
    )
    value.loc[:, ["WETLAND"]] = 0
    value.loc[:, ["URBAN_LAND"]] = 0
    value.loc[:, ["SOLAR_LAND"]] = 0
    value.loc[:, ["SNOW_ICE_WATERBODIES"]] = 0
    return value
