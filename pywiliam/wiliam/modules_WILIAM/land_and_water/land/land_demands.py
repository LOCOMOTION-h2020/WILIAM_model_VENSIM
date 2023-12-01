"""
Module land_and_water.land.land_demands
Translated using PySD version 3.10.0
"""


@component.add(
    name="accumulated_error_in_solar_land",
    units="km2",
    subscripts=["REGIONS_9_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_accumulated_error_in_solar_land": 1},
    other_deps={
        "_integ_accumulated_error_in_solar_land": {
            "initial": {},
            "step": {"error_solar_land": 1},
        }
    },
)
def accumulated_error_in_solar_land():
    return _integ_accumulated_error_in_solar_land()


_integ_accumulated_error_in_solar_land = Integ(
    lambda: error_solar_land(),
    lambda: xr.DataArray(
        0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
    ),
    "_integ_accumulated_error_in_solar_land",
)


@component.add(
    name="afforestation_due_to_policies",
    units="km2/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_afforestation_sp": 1,
        "time": 2,
        "year_initial_afforestation_sp": 2,
        "year_final_afforestation_sp": 2,
        "objective_afforestation_sp": 1,
        "initial_land_use_by_region": 1,
    },
)
def afforestation_due_to_policies():
    return if_then_else(
        np.logical_and(
            switch_afforestation_sp() == 1,
            np.logical_and(
                time() > year_initial_afforestation_sp(),
                time() < year_final_afforestation_sp(),
            ),
        ),
        lambda: (
            objective_afforestation_sp()
            * initial_land_use_by_region()
            .loc[:, "FOREST_MANAGED"]
            .reset_coords(drop=True)
        )
        / (year_final_afforestation_sp() - year_initial_afforestation_sp()),
        lambda: xr.DataArray(
            0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
        ),
    )


@component.add(
    name="changes_of_share_of_solar_land",
    units="1/Year",
    subscripts=["REGIONS_9_I", "LANDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 2,
        "year_initial_solar_land_from_others_sp": 2,
        "year_final_solar_land_from_others_sp": 2,
        "objective_solar_land_from_others_sp": 1,
        "initial_share_of_land_use_changes_from_others_up": 1,
    },
)
def changes_of_share_of_solar_land():
    return if_then_else(
        np.logical_and(
            time() > year_initial_solar_land_from_others_sp(),
            time() < year_final_solar_land_from_others_sp(),
        ).expand_dims({"LANDS_I": _subscript_dict["LANDS_I"]}, 1),
        lambda: zidz(
            objective_solar_land_from_others_sp()
            - initial_share_of_land_use_changes_from_others_up()
            .loc[:, :, "SOLAR_LAND"]
            .reset_coords(drop=True),
            (
                year_final_solar_land_from_others_sp()
                - year_initial_solar_land_from_others_sp()
            ).expand_dims({"LANDS_I": _subscript_dict["LANDS_I"]}, 1),
        ),
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
    name="error_solar_land",
    units="km2",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "time_historical_data_land_module": 1,
        "land_use_area_by_region": 1,
        "land_for_solar_demanded": 1,
    },
)
def error_solar_land():
    return if_then_else(
        time() < time_historical_data_land_module(),
        lambda: xr.DataArray(
            0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
        ),
        lambda: land_for_solar_demanded()
        - land_use_area_by_region().loc[:, "SOLAR_LAND"].reset_coords(drop=True),
    )


@component.add(
    name="forest_plantations_growth_due_to_policies",
    units="km2/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_forest_plantations_sp": 1,
        "time": 2,
        "year_initial_forest_plantations_sp": 2,
        "year_final_forest_plantations_sp": 2,
        "initial_land_use_by_region": 1,
        "objective_forest_plantations_sp": 1,
    },
)
def forest_plantations_growth_due_to_policies():
    """
    Growth of forest plantations driven by policies, it is added to the trends.
    """
    return if_then_else(
        np.logical_and(
            switch_forest_plantations_sp() == 1,
            np.logical_and(
                time() > year_initial_forest_plantations_sp(),
                time() < year_final_forest_plantations_sp(),
            ),
        ),
        lambda: (
            objective_forest_plantations_sp()
            * initial_land_use_by_region()
            .loc[:, "FOREST_PLANTATIONS"]
            .reset_coords(drop=True)
        )
        / (year_final_forest_plantations_sp() - year_initial_forest_plantations_sp()),
        lambda: xr.DataArray(
            0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
        ),
    )


@component.add(
    name="imv_population_variation_exogenous",
    units="people/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_landwater": 9,
        "deaths": 9,
        "births": 9,
        "time": 9,
        "imv_exogenous_population_variation": 9,
    },
)
def imv_population_variation_exogenous():
    """
    Variation of population by region (9 regions)
    """
    value = xr.DataArray(
        np.nan, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
    )
    value.loc[["EU27"]] = if_then_else(
        switch_landwater() == 1,
        lambda: sum(
            births()
            .loc[_subscript_dict["REGIONS_EU27_I"], :, "c0c4"]
            .reset_coords(drop=True)
            .rename({"REGIONS_35_I": "REGIONS_EU27_I!", "SEX_I": "SEX_I!"}),
            dim=["REGIONS_EU27_I!", "SEX_I!"],
        )
        - sum(
            deaths()
            .loc[_subscript_dict["REGIONS_EU27_I"], :, :]
            .rename(
                {
                    "REGIONS_35_I": "REGIONS_EU27_I!",
                    "SEX_I": "SEX_I!",
                    "AGE_COHORTS_I": "AGE_COHORTS_I!",
                }
            ),
            dim=["REGIONS_EU27_I!", "SEX_I!", "AGE_COHORTS_I!"],
        ),
        lambda: float(imv_exogenous_population_variation(time()).loc["EU27"]),
    )
    value.loc[["UK"]] = if_then_else(
        switch_landwater() == 1,
        lambda: sum(
            births()
            .loc["UK", :, "c0c4"]
            .reset_coords(drop=True)
            .rename({"SEX_I": "SEX_I!"}),
            dim=["SEX_I!"],
        )
        - sum(
            deaths()
            .loc["UK", :, :]
            .reset_coords(drop=True)
            .rename({"SEX_I": "SEX_I!", "AGE_COHORTS_I": "AGE_COHORTS_I!"}),
            dim=["SEX_I!", "AGE_COHORTS_I!"],
        ),
        lambda: float(imv_exogenous_population_variation(time()).loc["UK"]),
    )
    value.loc[["CHINA"]] = if_then_else(
        switch_landwater() == 1,
        lambda: sum(
            births()
            .loc["CHINA", :, "c0c4"]
            .reset_coords(drop=True)
            .rename({"SEX_I": "SEX_I!"}),
            dim=["SEX_I!"],
        )
        - sum(
            deaths()
            .loc["CHINA", :, :]
            .reset_coords(drop=True)
            .rename({"SEX_I": "SEX_I!", "AGE_COHORTS_I": "AGE_COHORTS_I!"}),
            dim=["SEX_I!", "AGE_COHORTS_I!"],
        ),
        lambda: float(imv_exogenous_population_variation(time()).loc["CHINA"]),
    )
    value.loc[["EASOC"]] = if_then_else(
        switch_landwater() == 1,
        lambda: sum(
            births()
            .loc["EASOC", :, "c0c4"]
            .reset_coords(drop=True)
            .rename({"SEX_I": "SEX_I!"}),
            dim=["SEX_I!"],
        )
        - sum(
            deaths()
            .loc["EASOC", :, :]
            .reset_coords(drop=True)
            .rename({"SEX_I": "SEX_I!", "AGE_COHORTS_I": "AGE_COHORTS_I!"}),
            dim=["SEX_I!", "AGE_COHORTS_I!"],
        ),
        lambda: float(imv_exogenous_population_variation(time()).loc["EASOC"]),
    )
    value.loc[["INDIA"]] = if_then_else(
        switch_landwater() == 1,
        lambda: sum(
            births()
            .loc["INDIA", :, "c0c4"]
            .reset_coords(drop=True)
            .rename({"SEX_I": "SEX_I!"}),
            dim=["SEX_I!"],
        )
        - sum(
            deaths()
            .loc["INDIA", :, :]
            .reset_coords(drop=True)
            .rename({"SEX_I": "SEX_I!", "AGE_COHORTS_I": "AGE_COHORTS_I!"}),
            dim=["SEX_I!", "AGE_COHORTS_I!"],
        ),
        lambda: float(imv_exogenous_population_variation(time()).loc["INDIA"]),
    )
    value.loc[["LATAM"]] = if_then_else(
        switch_landwater() == 1,
        lambda: sum(
            births()
            .loc["LATAM", :, "c0c4"]
            .reset_coords(drop=True)
            .rename({"SEX_I": "SEX_I!"}),
            dim=["SEX_I!"],
        )
        - sum(
            deaths()
            .loc["LATAM", :, :]
            .reset_coords(drop=True)
            .rename({"SEX_I": "SEX_I!", "AGE_COHORTS_I": "AGE_COHORTS_I!"}),
            dim=["SEX_I!", "AGE_COHORTS_I!"],
        ),
        lambda: float(imv_exogenous_population_variation(time()).loc["LATAM"]),
    )
    value.loc[["RUSSIA"]] = if_then_else(
        switch_landwater() == 1,
        lambda: sum(
            births()
            .loc["RUSSIA", :, "c0c4"]
            .reset_coords(drop=True)
            .rename({"SEX_I": "SEX_I!"}),
            dim=["SEX_I!"],
        )
        - sum(
            deaths()
            .loc["RUSSIA", :, :]
            .reset_coords(drop=True)
            .rename({"SEX_I": "SEX_I!", "AGE_COHORTS_I": "AGE_COHORTS_I!"}),
            dim=["SEX_I!", "AGE_COHORTS_I!"],
        ),
        lambda: float(imv_exogenous_population_variation(time()).loc["RUSSIA"]),
    )
    value.loc[["USMCA"]] = if_then_else(
        switch_landwater() == 1,
        lambda: sum(
            births()
            .loc["USMCA", :, "c0c4"]
            .reset_coords(drop=True)
            .rename({"SEX_I": "SEX_I!"}),
            dim=["SEX_I!"],
        )
        - sum(
            deaths()
            .loc["USMCA", :, :]
            .reset_coords(drop=True)
            .rename({"SEX_I": "SEX_I!", "AGE_COHORTS_I": "AGE_COHORTS_I!"}),
            dim=["SEX_I!", "AGE_COHORTS_I!"],
        ),
        lambda: float(imv_exogenous_population_variation(time()).loc["USMCA"]),
    )
    value.loc[["LROW"]] = if_then_else(
        switch_landwater() == 1,
        lambda: sum(
            births()
            .loc["LROW", :, "c0c4"]
            .reset_coords(drop=True)
            .rename({"SEX_I": "SEX_I!"}),
            dim=["SEX_I!"],
        )
        - sum(
            deaths()
            .loc["LROW", :, :]
            .reset_coords(drop=True)
            .rename({"SEX_I": "SEX_I!", "AGE_COHORTS_I": "AGE_COHORTS_I!"}),
            dim=["SEX_I!", "AGE_COHORTS_I!"],
        ),
        lambda: float(imv_exogenous_population_variation(time()).loc["LROW"]),
    )
    return value


@component.add(
    name="increment_of_cropland_and_solar_limited",
    units="km2",
    subscripts=["REGIONS_9_I", "LANDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "initial_land_use_by_region": 1,
        "maximum_annual_land_use_change": 1,
        "increment_of_croplands_and_solar_demanded": 4,
    },
)
def increment_of_cropland_and_solar_limited():
    """
    The same increment but saturated at the maximum change per year observed historically
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "LANDS_I": _subscript_dict["LANDS_I"],
        },
        ["REGIONS_9_I", "LANDS_I"],
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, ["SOLAR_LAND"]] = False
    value.values[except_subs.values] = (
        np.minimum(
            initial_land_use_by_region() * maximum_annual_land_use_change(),
            np.abs(increment_of_croplands_and_solar_demanded()),
        )
        * zidz(
            increment_of_croplands_and_solar_demanded(),
            np.abs(increment_of_croplands_and_solar_demanded()),
        )
    ).values[except_subs.values]
    value.loc[:, ["SOLAR_LAND"]] = (
        increment_of_croplands_and_solar_demanded()
        .loc[:, "SOLAR_LAND"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS_I": ["SOLAR_LAND"]}, 1)
        .values
    )
    return value


@component.add(
    name="increment_of_croplands_and_solar_demanded",
    units="km2",
    subscripts=["REGIONS_9_I", "LANDS_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "global_availability_of_crops": 2,
        "priorities_of_land_use_change_sp": 2,
        "initial_land_use_by_region": 2,
        "control_parameter_of_land_use_changes": 2,
        "accumulated_error_in_solar_land": 1,
        "kp_solar_feedback": 1,
        "ki_solar_feedback": 1,
        "error_solar_land": 1,
    },
)
def increment_of_croplands_and_solar_demanded():
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
            -global_availability_of_crops()
            * (
                1
                + priorities_of_land_use_change_sp()
                .loc[:, "CROPLAND_RAINFED"]
                .reset_coords(drop=True)
            )
            * initial_land_use_by_region()
            .loc[:, "CROPLAND_RAINFED"]
            .reset_coords(drop=True)
            * float(control_parameter_of_land_use_changes().loc["CROPLAND_RAINFED"])
        )
        .expand_dims({"LANDS_I": ["CROPLAND_RAINFED"]}, 1)
        .values
    )
    value.loc[:, ["CROPLAND_IRRIGATED"]] = (
        (
            0
            * (
                -global_availability_of_crops()
                * priorities_of_land_use_change_sp()
                .loc[:, "CROPLAND_IRRIGATED"]
                .reset_coords(drop=True)
                * initial_land_use_by_region()
                .loc[:, "CROPLAND_IRRIGATED"]
                .reset_coords(drop=True)
                * float(
                    control_parameter_of_land_use_changes().loc["CROPLAND_IRRIGATED"]
                )
            )
        )
        .expand_dims({"LANDS_I": ["CROPLAND_IRRIGATED"]}, 1)
        .values
    )
    value.loc[:, ["FOREST_MANAGED"]] = 0
    value.loc[:, ["FOREST_PRIMARY"]] = 0
    value.loc[:, ["FOREST_PLANTATIONS"]] = 0
    value.loc[:, ["SHRUBLAND"]] = 0
    value.loc[:, ["GRASSLAND"]] = 0
    value.loc[:, ["WETLAND"]] = 0
    value.loc[:, ["URBAN_LAND"]] = 0
    value.loc[:, ["SOLAR_LAND"]] = (
        (
            (
                error_solar_land()
                + accumulated_error_in_solar_land() * ki_solar_feedback()
            )
            * kp_solar_feedback()
        )
        .expand_dims({"LANDS_I": ["SOLAR_LAND"]}, 1)
        .values
    )
    value.loc[:, ["SNOW_ICE_WATERBODIES"]] = 0
    value.loc[:, ["OTHER_LAND"]] = 0
    return value


@component.add(
    name="increment_of_urban_land_demanded",
    units="km2/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Stateful",
    comp_subtype="Smooth",
    depends_on={
        "_smooth_increment_of_urban_land_demanded": 1,
        "urban_land_density": 1,
        "unit_conversion_m2_km2": 1,
    },
    other_deps={
        "_smooth_increment_of_urban_land_demanded": {
            "initial": {"imv_population_variation_exogenous": 1},
            "step": {"imv_population_variation_exogenous": 1},
        }
    },
)
def increment_of_urban_land_demanded():
    return np.maximum(
        0,
        _smooth_increment_of_urban_land_demanded()
        * urban_land_density()
        / unit_conversion_m2_km2(),
    )


_smooth_increment_of_urban_land_demanded = Smooth(
    lambda: imv_population_variation_exogenous(),
    lambda: xr.DataArray(
        10, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
    ),
    lambda: imv_population_variation_exogenous(),
    lambda: 1,
    "_smooth_increment_of_urban_land_demanded",
)


@component.add(
    name="land_for_solar_demanded",
    units="km2",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 2,
        "time_historical_data_land_module": 1,
        "switch_landwater": 1,
        "land_use_by_protra": 1,
        "exo_land_for_solar_demanded": 1,
    },
)
def land_for_solar_demanded():
    return if_then_else(
        time() < time_historical_data_land_module(),
        lambda: xr.DataArray(
            0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
        ),
        lambda: if_then_else(
            switch_landwater() == 1,
            lambda: land_use_by_protra()
            .loc[:, "TO_elec", "PROTRA_PP_solar_open_space_PV"]
            .reset_coords(drop=True),
            lambda: exo_land_for_solar_demanded(time()),
        ),
    )


@component.add(
    name="land_use_changes_demanded",
    units="km2/Year",
    subscripts=["REGIONS_9_I", "LANDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "time_historical_data_land_module": 1,
        "trends_of_land_use_changes": 1,
        "check_exogenous_land_use_demands": 1,
        "switch_law_exogenous_land_use_demands": 2,
        "land_use_changes_demanded_before_exogenous": 1,
    },
)
def land_use_changes_demanded():
    return if_then_else(
        time() < time_historical_data_land_module(),
        lambda: trends_of_land_use_changes(),
        lambda: switch_law_exogenous_land_use_demands()
        * land_use_changes_demanded_before_exogenous()
        + (1 - switch_law_exogenous_land_use_demands())
        * check_exogenous_land_use_demands(),
    )


@component.add(
    name="land_use_changes_demanded_before_exogenous",
    units="km2/Year",
    subscripts=["REGIONS_9_I", "LANDS_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "trends_of_land_use_changes": 6,
        "land_use_changes_driven_by_demands": 6,
    },
)
def land_use_changes_demanded_before_exogenous():
    """
    IF_THEN_ELSE( irrigated_land_loss_due_to_water_stress[REGIONS_9_I]>0, -irrigated_land_loss_due_to_water_stress[REGIONS_9_I], trends_of_land_use_changes[REGIONS_9_I,CROPLAND_IRRIGATED])
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
            trends_of_land_use_changes()
            .loc[:, "CROPLAND_RAINFED"]
            .reset_coords(drop=True)
            + land_use_changes_driven_by_demands()
            .loc[:, "CROPLAND_RAINFED"]
            .reset_coords(drop=True)
        )
        .expand_dims({"LANDS_I": ["CROPLAND_RAINFED"]}, 1)
        .values
    )
    value.loc[:, ["CROPLAND_IRRIGATED"]] = (
        trends_of_land_use_changes()
        .loc[:, "CROPLAND_IRRIGATED"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS_I": ["CROPLAND_IRRIGATED"]}, 1)
        .values
    )
    value.loc[:, ["FOREST_MANAGED"]] = (
        (
            trends_of_land_use_changes()
            .loc[:, "FOREST_MANAGED"]
            .reset_coords(drop=True)
            + land_use_changes_driven_by_demands()
            .loc[:, "FOREST_MANAGED"]
            .reset_coords(drop=True)
        )
        .expand_dims({"LANDS_FOREST_I": ["FOREST_MANAGED"]}, 1)
        .values
    )
    value.loc[:, ["FOREST_PRIMARY"]] = (
        (
            trends_of_land_use_changes()
            .loc[:, "FOREST_PRIMARY"]
            .reset_coords(drop=True)
            + land_use_changes_driven_by_demands()
            .loc[:, "FOREST_PRIMARY"]
            .reset_coords(drop=True)
        )
        .expand_dims({"LANDS_FOREST_I": ["FOREST_PRIMARY"]}, 1)
        .values
    )
    value.loc[:, ["FOREST_PLANTATIONS"]] = (
        (
            trends_of_land_use_changes()
            .loc[:, "FOREST_PLANTATIONS"]
            .reset_coords(drop=True)
            + land_use_changes_driven_by_demands()
            .loc[:, "FOREST_PLANTATIONS"]
            .reset_coords(drop=True)
        )
        .expand_dims({"LANDS_FOREST_I": ["FOREST_PLANTATIONS"]}, 1)
        .values
    )
    value.loc[:, ["SHRUBLAND"]] = 0
    value.loc[:, ["GRASSLAND"]] = (
        trends_of_land_use_changes()
        .loc[:, "GRASSLAND"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS_I": ["GRASSLAND"]}, 1)
        .values
    )
    value.loc[:, ["WETLAND"]] = 0
    value.loc[:, ["URBAN_LAND"]] = (
        land_use_changes_driven_by_demands()
        .loc[:, "URBAN_LAND"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS_I": ["URBAN_LAND"]}, 1)
        .values
    )
    value.loc[:, ["SOLAR_LAND"]] = (
        land_use_changes_driven_by_demands()
        .loc[:, "SOLAR_LAND"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS_I": ["SOLAR_LAND"]}, 1)
        .values
    )
    value.loc[:, ["SNOW_ICE_WATERBODIES"]] = 0
    value.loc[:, ["OTHER_LAND"]] = 0
    return value


@component.add(
    name="land_use_changes_driven_by_demands",
    units="km2/Year",
    subscripts=["REGIONS_9_I", "LANDS_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 6,
        "time_historical_data_land_module": 6,
        "increment_of_cropland_and_solar_limited": 3,
        "afforestation_due_to_policies": 1,
        "forest_plantations_growth_due_to_policies": 1,
        "increment_of_urban_land_demanded": 1,
    },
)
def land_use_changes_driven_by_demands():
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
            time() < time_historical_data_land_module(),
            lambda: xr.DataArray(
                0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
            ),
            lambda: increment_of_cropland_and_solar_limited()
            .loc[:, "CROPLAND_RAINFED"]
            .reset_coords(drop=True),
        )
        .expand_dims({"LANDS_I": ["CROPLAND_RAINFED"]}, 1)
        .values
    )
    value.loc[:, ["CROPLAND_IRRIGATED"]] = (
        if_then_else(
            time() <= time_historical_data_land_module(),
            lambda: xr.DataArray(
                0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
            ),
            lambda: increment_of_cropland_and_solar_limited()
            .loc[:, "CROPLAND_IRRIGATED"]
            .reset_coords(drop=True),
        )
        .expand_dims({"LANDS_I": ["CROPLAND_IRRIGATED"]}, 1)
        .values
    )
    value.loc[:, ["FOREST_MANAGED"]] = (
        if_then_else(
            time() <= time_historical_data_land_module(),
            lambda: xr.DataArray(
                0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
            ),
            lambda: afforestation_due_to_policies(),
        )
        .expand_dims({"LANDS_FOREST_I": ["FOREST_MANAGED"]}, 1)
        .values
    )
    value.loc[:, ["FOREST_PRIMARY"]] = 0
    value.loc[:, ["FOREST_PLANTATIONS"]] = (
        if_then_else(
            time() <= time_historical_data_land_module(),
            lambda: xr.DataArray(
                0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
            ),
            lambda: forest_plantations_growth_due_to_policies(),
        )
        .expand_dims({"LANDS_FOREST_I": ["FOREST_PLANTATIONS"]}, 1)
        .values
    )
    value.loc[:, ["SHRUBLAND"]] = 0
    value.loc[:, ["GRASSLAND"]] = 0
    value.loc[:, ["WETLAND"]] = 0
    value.loc[:, ["URBAN_LAND"]] = (
        if_then_else(
            time() <= time_historical_data_land_module(),
            lambda: xr.DataArray(
                0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
            ),
            lambda: increment_of_urban_land_demanded(),
        )
        .expand_dims({"LANDS_I": ["URBAN_LAND"]}, 1)
        .values
    )
    value.loc[:, ["SOLAR_LAND"]] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: xr.DataArray(
                0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
            ),
            lambda: increment_of_cropland_and_solar_limited()
            .loc[:, "SOLAR_LAND"]
            .reset_coords(drop=True),
        )
        .expand_dims({"LANDS_I": ["SOLAR_LAND"]}, 1)
        .values
    )
    value.loc[:, ["SNOW_ICE_WATERBODIES"]] = 0
    value.loc[:, ["OTHER_LAND"]] = 0
    return value


@component.add(
    name="matrix_of_land_use_change_demands",
    units="km2/Year",
    subscripts=["REGIONS_9_I", "LANDS_I", "LANDS_MAP_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "land_use_changes_demanded": 12,
        "share_of_land_use_change_from_others": 12,
    },
)
def matrix_of_land_use_change_demands():
    """
    from land use LANDS_I (down, first index) to land use LANDS_MAP_I (right, second index) WE take from land use LANDS_I the demand of LANDS_MAP_I * the % of the demand of LANDS_MAP_I from LANDS_I
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
    value.loc[:, :, ["CROPLAND_RAINFED"]] = (
        (
            land_use_changes_demanded()
            .loc[:, "CROPLAND_RAINFED"]
            .reset_coords(drop=True)
            * share_of_land_use_change_from_others()
            .loc[:, :, "CROPLAND_RAINFED"]
            .reset_coords(drop=True)
        )
        .expand_dims({"LANDS_MAP_I": ["CROPLAND_RAINFED"]}, 2)
        .values
    )
    value.loc[:, :, ["CROPLAND_IRRIGATED"]] = (
        (
            land_use_changes_demanded()
            .loc[:, "CROPLAND_IRRIGATED"]
            .reset_coords(drop=True)
            * share_of_land_use_change_from_others()
            .loc[:, :, "CROPLAND_IRRIGATED"]
            .reset_coords(drop=True)
        )
        .expand_dims({"LANDS_MAP_I": ["CROPLAND_IRRIGATED"]}, 2)
        .values
    )
    value.loc[:, :, ["FOREST_MANAGED"]] = (
        (
            land_use_changes_demanded().loc[:, "FOREST_MANAGED"].reset_coords(drop=True)
            * share_of_land_use_change_from_others()
            .loc[:, :, "FOREST_MANAGED"]
            .reset_coords(drop=True)
        )
        .expand_dims({"LANDS_FOREST_I": ["FOREST_MANAGED"]}, 2)
        .values
    )
    value.loc[:, :, ["FOREST_PRIMARY"]] = (
        (
            land_use_changes_demanded().loc[:, "FOREST_PRIMARY"].reset_coords(drop=True)
            * share_of_land_use_change_from_others()
            .loc[:, :, "FOREST_PRIMARY"]
            .reset_coords(drop=True)
        )
        .expand_dims({"LANDS_FOREST_I": ["FOREST_PRIMARY"]}, 2)
        .values
    )
    value.loc[:, :, ["FOREST_PLANTATIONS"]] = (
        (
            land_use_changes_demanded()
            .loc[:, "FOREST_PLANTATIONS"]
            .reset_coords(drop=True)
            * share_of_land_use_change_from_others()
            .loc[:, :, "FOREST_PLANTATIONS"]
            .reset_coords(drop=True)
        )
        .expand_dims({"LANDS_FOREST_I": ["FOREST_PLANTATIONS"]}, 2)
        .values
    )
    value.loc[:, :, ["SHRUBLAND"]] = (
        (
            land_use_changes_demanded().loc[:, "SHRUBLAND"].reset_coords(drop=True)
            * share_of_land_use_change_from_others()
            .loc[:, :, "SHRUBLAND"]
            .reset_coords(drop=True)
        )
        .expand_dims({"LANDS_MAP_I": ["SHRUBLAND"]}, 2)
        .values
    )
    value.loc[:, :, ["GRASSLAND"]] = (
        (
            land_use_changes_demanded().loc[:, "GRASSLAND"].reset_coords(drop=True)
            * share_of_land_use_change_from_others()
            .loc[:, :, "GRASSLAND"]
            .reset_coords(drop=True)
        )
        .expand_dims({"LANDS_MAP_I": ["GRASSLAND"]}, 2)
        .values
    )
    value.loc[:, :, ["WETLAND"]] = (
        (
            land_use_changes_demanded().loc[:, "WETLAND"].reset_coords(drop=True)
            * share_of_land_use_change_from_others()
            .loc[:, :, "WETLAND"]
            .reset_coords(drop=True)
        )
        .expand_dims({"LANDS_MAP_I": ["WETLAND"]}, 2)
        .values
    )
    value.loc[:, :, ["URBAN_LAND"]] = (
        (
            land_use_changes_demanded().loc[:, "URBAN_LAND"].reset_coords(drop=True)
            * share_of_land_use_change_from_others()
            .loc[:, :, "URBAN_LAND"]
            .reset_coords(drop=True)
        )
        .expand_dims({"LANDS_MAP_I": ["URBAN_LAND"]}, 2)
        .values
    )
    value.loc[:, :, ["SOLAR_LAND"]] = (
        (
            land_use_changes_demanded().loc[:, "SOLAR_LAND"].reset_coords(drop=True)
            * share_of_land_use_change_from_others()
            .loc[:, :, "SOLAR_LAND"]
            .reset_coords(drop=True)
        )
        .expand_dims({"LANDS_MAP_I": ["SOLAR_LAND"]}, 2)
        .values
    )
    value.loc[:, :, ["SNOW_ICE_WATERBODIES"]] = (
        (
            land_use_changes_demanded()
            .loc[:, "SNOW_ICE_WATERBODIES"]
            .reset_coords(drop=True)
            * share_of_land_use_change_from_others()
            .loc[:, :, "SNOW_ICE_WATERBODIES"]
            .reset_coords(drop=True)
        )
        .expand_dims({"LANDS_MAP_I": ["SNOW_ICE_WATERBODIES"]}, 2)
        .values
    )
    value.loc[:, :, ["OTHER_LAND"]] = (
        (
            land_use_changes_demanded().loc[:, "OTHER_LAND"].reset_coords(drop=True)
            * share_of_land_use_change_from_others()
            .loc[:, :, "OTHER_LAND"]
            .reset_coords(drop=True)
        )
        .expand_dims({"LANDS_MAP_I": ["OTHER_LAND"]}, 2)
        .values
    )
    return value


@component.add(
    name="share_of_land_use_change_from_others",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LANDS_I", "LANDS_MAP_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 9,
        "time_historical_data_land_module": 9,
        "historical_share_of_land_use_changes_from_others": 9,
        "land_use_changes_demanded": 9,
        "share_of_land_use_changes_from_others_up": 9,
        "initial_share_of_land_use_changes_from_others_down": 9,
    },
)
def share_of_land_use_change_from_others():
    """
    SHARES (LANDS_I,LANDS_MAP_I)=demand of use LANDS_MAP_I taken from LANDS_I
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
    value.loc[["EU27"], :, :] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_share_of_land_use_changes_from_others()
            .loc["EU27", :, :]
            .reset_coords(drop=True),
            lambda: if_then_else(
                (
                    land_use_changes_demanded()
                    .loc["EU27", :]
                    .reset_coords(drop=True)
                    .rename({"LANDS_I": "LANDS_MAP_I"})
                    > 0
                ).expand_dims({"LANDS_I": _subscript_dict["LANDS_I"]}, 1),
                lambda: share_of_land_use_changes_from_others_up()
                .loc["EU27", :, :]
                .reset_coords(drop=True)
                .transpose("LANDS_MAP_I", "LANDS_I"),
                lambda: initial_share_of_land_use_changes_from_others_down()
                .loc["EU27", :, :]
                .reset_coords(drop=True)
                .transpose("LANDS_MAP_I", "LANDS_I"),
            ).transpose("LANDS_I", "LANDS_MAP_I"),
        )
        .expand_dims({"REGIONS_36_I": ["EU27"]}, 0)
        .values
    )
    value.loc[["UK"], :, :] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_share_of_land_use_changes_from_others()
            .loc["UK", :, :]
            .reset_coords(drop=True),
            lambda: if_then_else(
                (
                    land_use_changes_demanded()
                    .loc["UK", :]
                    .reset_coords(drop=True)
                    .rename({"LANDS_I": "LANDS_MAP_I"})
                    > 0
                ).expand_dims({"LANDS_I": _subscript_dict["LANDS_I"]}, 1),
                lambda: share_of_land_use_changes_from_others_up()
                .loc["UK", :, :]
                .reset_coords(drop=True)
                .transpose("LANDS_MAP_I", "LANDS_I"),
                lambda: initial_share_of_land_use_changes_from_others_down()
                .loc["UK", :, :]
                .reset_coords(drop=True)
                .transpose("LANDS_MAP_I", "LANDS_I"),
            ).transpose("LANDS_I", "LANDS_MAP_I"),
        )
        .expand_dims({"REGIONS_35_I": ["UK"]}, 0)
        .values
    )
    value.loc[["CHINA"], :, :] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_share_of_land_use_changes_from_others()
            .loc["CHINA", :, :]
            .reset_coords(drop=True),
            lambda: if_then_else(
                (
                    land_use_changes_demanded()
                    .loc["CHINA", :]
                    .reset_coords(drop=True)
                    .rename({"LANDS_I": "LANDS_MAP_I"})
                    > 0
                ).expand_dims({"LANDS_I": _subscript_dict["LANDS_I"]}, 1),
                lambda: share_of_land_use_changes_from_others_up()
                .loc["CHINA", :, :]
                .reset_coords(drop=True)
                .transpose("LANDS_MAP_I", "LANDS_I"),
                lambda: initial_share_of_land_use_changes_from_others_down()
                .loc["CHINA", :, :]
                .reset_coords(drop=True)
                .transpose("LANDS_MAP_I", "LANDS_I"),
            ).transpose("LANDS_I", "LANDS_MAP_I"),
        )
        .expand_dims({"REGIONS_35_I": ["CHINA"]}, 0)
        .values
    )
    value.loc[["EASOC"], :, :] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_share_of_land_use_changes_from_others()
            .loc["EASOC", :, :]
            .reset_coords(drop=True),
            lambda: if_then_else(
                (
                    land_use_changes_demanded()
                    .loc["EASOC", :]
                    .reset_coords(drop=True)
                    .rename({"LANDS_I": "LANDS_MAP_I"})
                    > 0
                ).expand_dims({"LANDS_I": _subscript_dict["LANDS_I"]}, 1),
                lambda: share_of_land_use_changes_from_others_up()
                .loc["EASOC", :, :]
                .reset_coords(drop=True)
                .transpose("LANDS_MAP_I", "LANDS_I"),
                lambda: initial_share_of_land_use_changes_from_others_down()
                .loc["EASOC", :, :]
                .reset_coords(drop=True)
                .transpose("LANDS_MAP_I", "LANDS_I"),
            ).transpose("LANDS_I", "LANDS_MAP_I"),
        )
        .expand_dims({"REGIONS_35_I": ["EASOC"]}, 0)
        .values
    )
    value.loc[["INDIA"], :, :] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_share_of_land_use_changes_from_others()
            .loc["INDIA", :, :]
            .reset_coords(drop=True),
            lambda: if_then_else(
                (
                    land_use_changes_demanded()
                    .loc["INDIA", :]
                    .reset_coords(drop=True)
                    .rename({"LANDS_I": "LANDS_MAP_I"})
                    > 0
                ).expand_dims({"LANDS_I": _subscript_dict["LANDS_I"]}, 1),
                lambda: share_of_land_use_changes_from_others_up()
                .loc["INDIA", :, :]
                .reset_coords(drop=True)
                .transpose("LANDS_MAP_I", "LANDS_I"),
                lambda: initial_share_of_land_use_changes_from_others_down()
                .loc["INDIA", :, :]
                .reset_coords(drop=True)
                .transpose("LANDS_MAP_I", "LANDS_I"),
            ).transpose("LANDS_I", "LANDS_MAP_I"),
        )
        .expand_dims({"REGIONS_35_I": ["INDIA"]}, 0)
        .values
    )
    value.loc[["LATAM"], :, :] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_share_of_land_use_changes_from_others()
            .loc["LATAM", :, :]
            .reset_coords(drop=True),
            lambda: if_then_else(
                (
                    land_use_changes_demanded()
                    .loc["LATAM", :]
                    .reset_coords(drop=True)
                    .rename({"LANDS_I": "LANDS_MAP_I"})
                    > 0
                ).expand_dims({"LANDS_I": _subscript_dict["LANDS_I"]}, 1),
                lambda: share_of_land_use_changes_from_others_up()
                .loc["LATAM", :, :]
                .reset_coords(drop=True)
                .transpose("LANDS_MAP_I", "LANDS_I"),
                lambda: initial_share_of_land_use_changes_from_others_down()
                .loc["LATAM", :, :]
                .reset_coords(drop=True)
                .transpose("LANDS_MAP_I", "LANDS_I"),
            ).transpose("LANDS_I", "LANDS_MAP_I"),
        )
        .expand_dims({"REGIONS_35_I": ["LATAM"]}, 0)
        .values
    )
    value.loc[["RUSSIA"], :, :] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_share_of_land_use_changes_from_others()
            .loc["RUSSIA", :, :]
            .reset_coords(drop=True),
            lambda: if_then_else(
                (
                    land_use_changes_demanded()
                    .loc["RUSSIA", :]
                    .reset_coords(drop=True)
                    .rename({"LANDS_I": "LANDS_MAP_I"})
                    > 0
                ).expand_dims({"LANDS_I": _subscript_dict["LANDS_I"]}, 1),
                lambda: share_of_land_use_changes_from_others_up()
                .loc["RUSSIA", :, :]
                .reset_coords(drop=True)
                .transpose("LANDS_MAP_I", "LANDS_I"),
                lambda: initial_share_of_land_use_changes_from_others_down()
                .loc["RUSSIA", :, :]
                .reset_coords(drop=True)
                .transpose("LANDS_MAP_I", "LANDS_I"),
            ).transpose("LANDS_I", "LANDS_MAP_I"),
        )
        .expand_dims({"REGIONS_35_I": ["RUSSIA"]}, 0)
        .values
    )
    value.loc[["USMCA"], :, :] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_share_of_land_use_changes_from_others()
            .loc["USMCA", :, :]
            .reset_coords(drop=True),
            lambda: if_then_else(
                (
                    land_use_changes_demanded()
                    .loc["USMCA", :]
                    .reset_coords(drop=True)
                    .rename({"LANDS_I": "LANDS_MAP_I"})
                    > 0
                ).expand_dims({"LANDS_I": _subscript_dict["LANDS_I"]}, 1),
                lambda: share_of_land_use_changes_from_others_up()
                .loc["USMCA", :, :]
                .reset_coords(drop=True)
                .transpose("LANDS_MAP_I", "LANDS_I"),
                lambda: initial_share_of_land_use_changes_from_others_down()
                .loc["USMCA", :, :]
                .reset_coords(drop=True)
                .transpose("LANDS_MAP_I", "LANDS_I"),
            ).transpose("LANDS_I", "LANDS_MAP_I"),
        )
        .expand_dims({"REGIONS_35_I": ["USMCA"]}, 0)
        .values
    )
    value.loc[["LROW"], :, :] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_share_of_land_use_changes_from_others()
            .loc["LROW", :, :]
            .reset_coords(drop=True),
            lambda: if_then_else(
                (
                    land_use_changes_demanded()
                    .loc["LROW", :]
                    .reset_coords(drop=True)
                    .rename({"LANDS_I": "LANDS_MAP_I"})
                    > 0
                ).expand_dims({"LANDS_I": _subscript_dict["LANDS_I"]}, 1),
                lambda: share_of_land_use_changes_from_others_up()
                .loc["LROW", :, :]
                .reset_coords(drop=True)
                .transpose("LANDS_MAP_I", "LANDS_I"),
                lambda: initial_share_of_land_use_changes_from_others_down()
                .loc["LROW", :, :]
                .reset_coords(drop=True)
                .transpose("LANDS_MAP_I", "LANDS_I"),
            ).transpose("LANDS_I", "LANDS_MAP_I"),
        )
        .expand_dims({"REGIONS_35_I": ["LROW"]}, 0)
        .values
    )
    return value


@component.add(
    name="share_of_land_use_changes_from_others_up",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LANDS_I", "LANDS_MAP_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "initial_share_of_land_use_changes_from_others_up": 12,
        "share_of_solar_land_from_others": 1,
        "switch_solar_land_from_others_sp": 1,
    },
)
def share_of_land_use_changes_from_others_up():
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "LANDS_I": _subscript_dict["LANDS_I"],
            "LANDS_MAP_I": _subscript_dict["LANDS_MAP_I"],
        },
        ["REGIONS_9_I", "LANDS_I", "LANDS_MAP_I"],
    )
    value.loc[:, :, ["CROPLAND_RAINFED"]] = (
        initial_share_of_land_use_changes_from_others_up()
        .loc[:, :, "CROPLAND_RAINFED"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS_MAP_I": ["CROPLAND_RAINFED"]}, 2)
        .values
    )
    value.loc[:, :, ["CROPLAND_IRRIGATED"]] = (
        initial_share_of_land_use_changes_from_others_up()
        .loc[:, :, "CROPLAND_IRRIGATED"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS_MAP_I": ["CROPLAND_IRRIGATED"]}, 2)
        .values
    )
    value.loc[:, :, ["FOREST_MANAGED"]] = (
        initial_share_of_land_use_changes_from_others_up()
        .loc[:, :, "FOREST_MANAGED"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS_FOREST_I": ["FOREST_MANAGED"]}, 2)
        .values
    )
    value.loc[:, :, ["FOREST_PRIMARY"]] = (
        initial_share_of_land_use_changes_from_others_up()
        .loc[:, :, "FOREST_PRIMARY"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS_FOREST_I": ["FOREST_PRIMARY"]}, 2)
        .values
    )
    value.loc[:, :, ["FOREST_PLANTATIONS"]] = (
        initial_share_of_land_use_changes_from_others_up()
        .loc[:, :, "FOREST_PLANTATIONS"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS_FOREST_I": ["FOREST_PLANTATIONS"]}, 2)
        .values
    )
    value.loc[:, :, ["SHRUBLAND"]] = (
        initial_share_of_land_use_changes_from_others_up()
        .loc[:, :, "SHRUBLAND"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS_MAP_I": ["SHRUBLAND"]}, 2)
        .values
    )
    value.loc[:, :, ["GRASSLAND"]] = (
        initial_share_of_land_use_changes_from_others_up()
        .loc[:, :, "GRASSLAND"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS_MAP_I": ["GRASSLAND"]}, 2)
        .values
    )
    value.loc[:, :, ["WETLAND"]] = (
        initial_share_of_land_use_changes_from_others_up()
        .loc[:, :, "WETLAND"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS_MAP_I": ["WETLAND"]}, 2)
        .values
    )
    value.loc[:, :, ["URBAN_LAND"]] = (
        initial_share_of_land_use_changes_from_others_up()
        .loc[:, :, "URBAN_LAND"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS_MAP_I": ["URBAN_LAND"]}, 2)
        .values
    )
    value.loc[:, :, ["SOLAR_LAND"]] = (
        if_then_else(
            (switch_solar_land_from_others_sp() == 1).expand_dims(
                {"LANDS_I": _subscript_dict["LANDS_I"]}, 1
            ),
            lambda: share_of_solar_land_from_others(),
            lambda: initial_share_of_land_use_changes_from_others_up()
            .loc[:, :, "SOLAR_LAND"]
            .reset_coords(drop=True),
        )
        .expand_dims({"LANDS_MAP_I": ["SOLAR_LAND"]}, 2)
        .values
    )
    value.loc[:, :, ["SNOW_ICE_WATERBODIES"]] = (
        initial_share_of_land_use_changes_from_others_up()
        .loc[:, :, "SNOW_ICE_WATERBODIES"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS_MAP_I": ["SNOW_ICE_WATERBODIES"]}, 2)
        .values
    )
    value.loc[:, :, ["OTHER_LAND"]] = (
        initial_share_of_land_use_changes_from_others_up()
        .loc[:, :, "OTHER_LAND"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS_MAP_I": ["OTHER_LAND"]}, 2)
        .values
    )
    return value


@component.add(
    name="share_of_solar_land_from_others",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LANDS_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_share_of_solar_land_from_others": 1},
    other_deps={
        "_integ_share_of_solar_land_from_others": {
            "initial": {"historical_share_of_land_use_changes_from_others": 1},
            "step": {"changes_of_share_of_solar_land": 1},
        }
    },
)
def share_of_solar_land_from_others():
    return _integ_share_of_solar_land_from_others()


_integ_share_of_solar_land_from_others = Integ(
    lambda: changes_of_share_of_solar_land(),
    lambda: historical_share_of_land_use_changes_from_others()
    .loc[:, :, "SOLAR_LAND"]
    .reset_coords(drop=True),
    "_integ_share_of_solar_land_from_others",
)


@component.add(
    name="share_solar_urban",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"land_use_area_by_region": 2},
)
def share_solar_urban():
    """
    share of the area of solar land with respect to the area of urban land
    """
    return zidz(
        land_use_area_by_region().loc[:, "SOLAR_LAND"].reset_coords(drop=True),
        land_use_area_by_region().loc[:, "URBAN_LAND"].reset_coords(drop=True),
    )


@component.add(
    name="stress_signal_solar_land",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_policy_maximum_share_solar_urban_sp": 1,
        "policy_maximum_share_solar_urban_sp": 6,
        "share_solar_urban": 4,
    },
)
def stress_signal_solar_land():
    """
    Variable sending signal of stress of land for solar . If=1 no stress, from 0,5 to 1 the stress grows linearly, If =0 maximum stress
    """
    return if_then_else(
        switch_policy_maximum_share_solar_urban_sp() == 0,
        lambda: xr.DataArray(
            1, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
        ),
        lambda: if_then_else(
            share_solar_urban() < policy_maximum_share_solar_urban_sp() * 0.8,
            lambda: xr.DataArray(
                1, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
            ),
            lambda: if_then_else(
                np.logical_and(
                    share_solar_urban() >= policy_maximum_share_solar_urban_sp() * 0.8,
                    share_solar_urban() < policy_maximum_share_solar_urban_sp(),
                ),
                lambda: 1
                - (
                    1
                    / (
                        policy_maximum_share_solar_urban_sp()
                        - policy_maximum_share_solar_urban_sp() * 0.8
                    )
                )
                * (share_solar_urban() - policy_maximum_share_solar_urban_sp() * 0.8),
                lambda: xr.DataArray(
                    0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
                ),
            ),
        ),
    )


@component.add(
    name="SWITCH_LAW_EXOGENOUS_LAND_USE_DEMANDS",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_law_exogenous_land_use_demands"},
)
def switch_law_exogenous_land_use_demands():
    """
    If this parameter =1 the land use submodule works normally, If it is =0, exogenous land demands are taken.
    """
    return _ext_constant_switch_law_exogenous_land_use_demands()


_ext_constant_switch_law_exogenous_land_use_demands = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_LAW_EXOGENOUS_LAND_USE_DEMANDS",
    {},
    _root,
    {},
    "_ext_constant_switch_law_exogenous_land_use_demands",
)


@component.add(
    name="trends_of_land_use_changes",
    units="km2/Year",
    subscripts=["REGIONS_9_I", "LANDS_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 8,
        "time_historical_data_land_module": 8,
        "historical_trends_of_land_use_demand": 8,
        "trends_of_land_use_demand": 8,
    },
)
def trends_of_land_use_changes():
    """
    land use changes demanded by trends calculated usign historcal data
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
            lambda: historical_trends_of_land_use_demand()
            .loc[:, "CROPLAND_RAINFED"]
            .reset_coords(drop=True),
            lambda: trends_of_land_use_demand()
            .loc[:, "CROPLAND_RAINFED"]
            .reset_coords(drop=True),
        )
        .expand_dims({"LANDS_I": ["CROPLAND_RAINFED"]}, 1)
        .values
    )
    value.loc[:, ["CROPLAND_IRRIGATED"]] = (
        if_then_else(
            time() <= time_historical_data_land_module(),
            lambda: historical_trends_of_land_use_demand()
            .loc[:, "CROPLAND_IRRIGATED"]
            .reset_coords(drop=True),
            lambda: trends_of_land_use_demand()
            .loc[:, "CROPLAND_IRRIGATED"]
            .reset_coords(drop=True),
        )
        .expand_dims({"LANDS_I": ["CROPLAND_IRRIGATED"]}, 1)
        .values
    )
    value.loc[:, ["FOREST_MANAGED"]] = (
        if_then_else(
            time() <= time_historical_data_land_module(),
            lambda: historical_trends_of_land_use_demand()
            .loc[:, "FOREST_MANAGED"]
            .reset_coords(drop=True),
            lambda: trends_of_land_use_demand()
            .loc[:, "FOREST_MANAGED"]
            .reset_coords(drop=True),
        )
        .expand_dims({"LANDS_FOREST_I": ["FOREST_MANAGED"]}, 1)
        .values
    )
    value.loc[:, ["FOREST_PRIMARY"]] = 0
    value.loc[:, ["FOREST_PLANTATIONS"]] = (
        if_then_else(
            time() <= time_historical_data_land_module(),
            lambda: historical_trends_of_land_use_demand()
            .loc[:, "FOREST_PLANTATIONS"]
            .reset_coords(drop=True),
            lambda: trends_of_land_use_demand()
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
            lambda: historical_trends_of_land_use_demand()
            .loc[:, "GRASSLAND"]
            .reset_coords(drop=True),
            lambda: trends_of_land_use_demand()
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
            lambda: historical_trends_of_land_use_demand()
            .loc[:, "URBAN_LAND"]
            .reset_coords(drop=True),
            lambda: trends_of_land_use_demand()
            .loc[:, "URBAN_LAND"]
            .reset_coords(drop=True),
        )
        .expand_dims({"LANDS_I": ["URBAN_LAND"]}, 1)
        .values
    )
    value.loc[:, ["SOLAR_LAND"]] = (
        if_then_else(
            time() <= time_historical_data_land_module(),
            lambda: historical_trends_of_land_use_demand()
            .loc[:, "SOLAR_LAND"]
            .reset_coords(drop=True),
            lambda: trends_of_land_use_demand()
            .loc[:, "SOLAR_LAND"]
            .reset_coords(drop=True),
        )
        .expand_dims({"LANDS_I": ["SOLAR_LAND"]}, 1)
        .values
    )
    value.loc[:, ["SNOW_ICE_WATERBODIES"]] = 0
    value.loc[:, ["OTHER_LAND"]] = (
        if_then_else(
            time() <= time_historical_data_land_module(),
            lambda: historical_trends_of_land_use_demand()
            .loc[:, "OTHER_LAND"]
            .reset_coords(drop=True),
            lambda: trends_of_land_use_demand()
            .loc[:, "OTHER_LAND"]
            .reset_coords(drop=True),
        )
        .expand_dims({"LANDS_I": ["OTHER_LAND"]}, 1)
        .values
    )
    return value
