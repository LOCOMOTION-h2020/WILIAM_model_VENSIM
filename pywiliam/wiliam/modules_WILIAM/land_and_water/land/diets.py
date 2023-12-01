"""
Module land_and_water.land.diets
Translated using PySD version 3.10.0
"""


@component.add(
    name="dairy_obtained_from_grasslands",
    units="t/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "initial_dairy_obtained_from_grasslands": 1,
        "land_use_area_by_region": 1,
        "initial_land_use_by_region": 1,
        "factor_of_grassland_production": 1,
    },
)
def dairy_obtained_from_grasslands():
    return (
        initial_dairy_obtained_from_grasslands()
        * zidz(
            land_use_area_by_region().loc[:, "GRASSLAND"].reset_coords(drop=True),
            initial_land_use_by_region().loc[:, "GRASSLAND"].reset_coords(drop=True),
        )
        * factor_of_grassland_production()
    )


@component.add(
    name="decrement_GDP_coefficient",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "poli_gdp_down": 1,
        "time": 1,
        "time_historical_data_land_module": 1,
        "gdp_down_coefficient": 1,
        "objective_gdp_down": 1,
    },
)
def decrement_gdp_coefficient():
    return if_then_else(
        np.logical_and(
            poli_gdp_down() == 1, time() > time_historical_data_land_module()
        ),
        lambda: -objective_gdp_down() * gdp_down_coefficient(),
        lambda: 0,
    )


@component.add(
    name="diet_according_to_food_shortage",
    units="kg/(person*Year)",
    subscripts=["REGIONS_9_I", "FOODS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "gdppc_per_share_of_available_food": 9,
        "diet_patterns_data_by_gdppc_for_eu": 1,
        "diet_patterns_data_by_gdppc_for_uk": 1,
        "diet_patterns_data_by_gdppc_for_china": 1,
        "diet_patterns_data_by_gdppc_for_easoc": 1,
        "diet_patterns_data_by_gdppc_for_india": 1,
        "diet_patterns_data_by_gdppc_for_latam": 1,
        "diet_patterns_data_by_gdppc_for_russia": 1,
        "diet_patterns_data_by_gdppc_for_usmca": 1,
        "diet_patterns_data_by_gdppc_for_lrow": 1,
    },
)
def diet_according_to_food_shortage():
    """
    diet patterns according to GDPpc desired_real_capital_stock[REGIONS_35_I,SECTORS_I]= SMOOTH( ZIDZ(output_real_expected[REGIONS_35_I,SECTORS_I],(CAPACITY_UTILIZATION_DES IRED[REGIONS_35_I,SECTORS_I]*capital_productivity[REGIONS_35_I,SECTORS_I])) ,3)
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "FOODS_I": _subscript_dict["FOODS_I"],
        },
        ["REGIONS_9_I", "FOODS_I"],
    )
    value.loc[["EU27"], :] = (
        diet_patterns_data_by_gdppc_for_eu(
            float(gdppc_per_share_of_available_food().loc["EU27"])
        )
        .expand_dims({"REGIONS_36_I": ["EU27"]}, 0)
        .values
    )
    value.loc[["UK"], :] = (
        diet_patterns_data_by_gdppc_for_uk(
            float(gdppc_per_share_of_available_food().loc["UK"])
        )
        .expand_dims({"REGIONS_35_I": ["UK"]}, 0)
        .values
    )
    value.loc[["CHINA"], :] = (
        diet_patterns_data_by_gdppc_for_china(
            float(gdppc_per_share_of_available_food().loc["CHINA"])
        )
        .expand_dims({"REGIONS_35_I": ["CHINA"]}, 0)
        .values
    )
    value.loc[["EASOC"], :] = (
        diet_patterns_data_by_gdppc_for_easoc(
            float(gdppc_per_share_of_available_food().loc["EASOC"])
        )
        .expand_dims({"REGIONS_35_I": ["EASOC"]}, 0)
        .values
    )
    value.loc[["INDIA"], :] = (
        diet_patterns_data_by_gdppc_for_india(
            float(gdppc_per_share_of_available_food().loc["INDIA"])
        )
        .expand_dims({"REGIONS_35_I": ["INDIA"]}, 0)
        .values
    )
    value.loc[["LATAM"], :] = (
        diet_patterns_data_by_gdppc_for_latam(
            float(gdppc_per_share_of_available_food().loc["LATAM"])
        )
        .expand_dims({"REGIONS_35_I": ["LATAM"]}, 0)
        .values
    )
    value.loc[["RUSSIA"], :] = (
        diet_patterns_data_by_gdppc_for_russia(
            float(gdppc_per_share_of_available_food().loc["RUSSIA"])
        )
        .expand_dims({"REGIONS_35_I": ["RUSSIA"]}, 0)
        .values
    )
    value.loc[["USMCA"], :] = (
        diet_patterns_data_by_gdppc_for_usmca(
            float(gdppc_per_share_of_available_food().loc["USMCA"])
        )
        .expand_dims({"REGIONS_35_I": ["USMCA"]}, 0)
        .values
    )
    value.loc[["LROW"], :] = (
        diet_patterns_data_by_gdppc_for_lrow(
            float(gdppc_per_share_of_available_food().loc["LROW"])
        )
        .expand_dims({"REGIONS_35_I": ["LROW"]}, 0)
        .values
    )
    return value


@component.add(
    name="diet_according_to_policies_sp",
    units="kg/(Year*people)",
    subscripts=["REGIONS_9_I", "FOODS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_model_explorer": 1,
        "model_explorer_diets": 1,
        "flexitariana_diet_patterns_of_policy_diets_sp": 1,
        "willett_diet_patterns_of_policy_diets_sp": 1,
        "plant_based_100_diet_pattern_of_policy_diets_sp": 1,
        "select_policy_diet_patterns_sp": 5,
        "plant_based_50_percent_diet_pattern_of_policy_diets_sp": 1,
        "baseline_diet_pattern_of_policy_diets_sp": 1,
    },
)
def diet_according_to_policies_sp():
    """
    Diet patterns according to the proposed policies
    """
    return if_then_else(
        switch_model_explorer() == 1,
        lambda: model_explorer_diets(),
        lambda: if_then_else(
            select_policy_diet_patterns_sp() == 0,
            lambda: flexitariana_diet_patterns_of_policy_diets_sp(),
            lambda: if_then_else(
                select_policy_diet_patterns_sp() == 1,
                lambda: willett_diet_patterns_of_policy_diets_sp(),
                lambda: if_then_else(
                    select_policy_diet_patterns_sp() == 2,
                    lambda: baseline_diet_pattern_of_policy_diets_sp(),
                    lambda: if_then_else(
                        select_policy_diet_patterns_sp() == 3,
                        lambda: plant_based_50_percent_diet_pattern_of_policy_diets_sp(),
                        lambda: if_then_else(
                            select_policy_diet_patterns_sp() == 4,
                            lambda: plant_based_100_diet_pattern_of_policy_diets_sp(),
                            lambda: xr.DataArray(
                                0,
                                {
                                    "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                                    "FOODS_I": _subscript_dict["FOODS_I"],
                                },
                                ["REGIONS_9_I", "FOODS_I"],
                            ),
                        ),
                    ),
                ),
            ),
        ),
    )


@component.add(
    name="diet_available",
    units="kg/(Year*person)",
    subscripts=["REGIONS_9_I", "FOODS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "time_historical_data_land_module": 1,
        "diet_demanded": 1,
        "efect_shortage_of_policy_diet": 1,
        "share_of_change_to_policy_diet": 2,
        "diet_according_to_food_shortage": 3,
        "switch_model_explorer": 2,
        "select_policy_diet_patterns_sp": 1,
        "diet_according_to_policies_sp": 1,
        "select_tipe_diets_me": 1,
    },
)
def diet_available():
    """
    Diet patterns of households according to food shortage and policies
    """
    return if_then_else(
        time() < time_historical_data_land_module(),
        lambda: diet_demanded(),
        lambda: if_then_else(
            np.logical_and(switch_model_explorer() == 1, select_tipe_diets_me() == 2),
            lambda: diet_according_to_food_shortage(),
            lambda: if_then_else(
                np.logical_and(
                    switch_model_explorer() == 0, select_policy_diet_patterns_sp() == 2
                ),
                lambda: diet_according_to_food_shortage(),
                lambda: diet_according_to_policies_sp()
                * share_of_change_to_policy_diet()
                * efect_shortage_of_policy_diet()
                + diet_according_to_food_shortage()
                * (1 - share_of_change_to_policy_diet()),
            ),
        ),
    )


@component.add(
    name="diet_demanded",
    units="kg/(Year*person)",
    subscripts=["REGIONS_9_I", "FOODS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_model_explorer": 2,
        "select_tipe_diets_me": 1,
        "diet_demanded_according_to_gdppc": 3,
        "select_policy_diet_patterns_sp": 1,
        "share_of_change_to_policy_diet": 2,
        "diet_according_to_policies_sp": 1,
    },
)
def diet_demanded():
    """
    Diet patterns of households according to GDPpc and policies
    """
    return if_then_else(
        np.logical_and(switch_model_explorer() == 1, select_tipe_diets_me() == 2),
        lambda: diet_demanded_according_to_gdppc(),
        lambda: if_then_else(
            np.logical_and(
                switch_model_explorer() == 0, select_policy_diet_patterns_sp() == 2
            ),
            lambda: diet_demanded_according_to_gdppc(),
            lambda: diet_according_to_policies_sp() * share_of_change_to_policy_diet()
            + diet_demanded_according_to_gdppc()
            * (1 - share_of_change_to_policy_diet()),
        ),
    )


@component.add(
    name="diet_demanded_according_to_GDPpc",
    units="kg/(person*Year)",
    subscripts=["REGIONS_9_I", "FOODS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "gdppc_9r_for_diets": 9,
        "diet_patterns_data_by_gdppc_for_eu": 1,
        "diet_patterns_data_by_gdppc_for_uk": 1,
        "diet_patterns_data_by_gdppc_for_china": 1,
        "diet_patterns_data_by_gdppc_for_easoc": 1,
        "diet_patterns_data_by_gdppc_for_india": 1,
        "diet_patterns_data_by_gdppc_for_latam": 1,
        "diet_patterns_data_by_gdppc_for_russia": 1,
        "diet_patterns_data_by_gdppc_for_usmca": 1,
        "diet_patterns_data_by_gdppc_for_lrow": 1,
    },
)
def diet_demanded_according_to_gdppc():
    """
    diet patterns according to GDPpc
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "FOODS_I": _subscript_dict["FOODS_I"],
        },
        ["REGIONS_9_I", "FOODS_I"],
    )
    value.loc[["EU27"], :] = (
        diet_patterns_data_by_gdppc_for_eu(float(gdppc_9r_for_diets().loc["EU27"]))
        .expand_dims({"REGIONS_36_I": ["EU27"]}, 0)
        .values
    )
    value.loc[["UK"], :] = (
        diet_patterns_data_by_gdppc_for_uk(float(gdppc_9r_for_diets().loc["UK"]))
        .expand_dims({"REGIONS_35_I": ["UK"]}, 0)
        .values
    )
    value.loc[["CHINA"], :] = (
        diet_patterns_data_by_gdppc_for_china(float(gdppc_9r_for_diets().loc["CHINA"]))
        .expand_dims({"REGIONS_35_I": ["CHINA"]}, 0)
        .values
    )
    value.loc[["EASOC"], :] = (
        diet_patterns_data_by_gdppc_for_easoc(float(gdppc_9r_for_diets().loc["EASOC"]))
        .expand_dims({"REGIONS_35_I": ["EASOC"]}, 0)
        .values
    )
    value.loc[["INDIA"], :] = (
        diet_patterns_data_by_gdppc_for_india(float(gdppc_9r_for_diets().loc["INDIA"]))
        .expand_dims({"REGIONS_35_I": ["INDIA"]}, 0)
        .values
    )
    value.loc[["LATAM"], :] = (
        diet_patterns_data_by_gdppc_for_latam(float(gdppc_9r_for_diets().loc["LATAM"]))
        .expand_dims({"REGIONS_35_I": ["LATAM"]}, 0)
        .values
    )
    value.loc[["RUSSIA"], :] = (
        diet_patterns_data_by_gdppc_for_russia(
            float(gdppc_9r_for_diets().loc["RUSSIA"])
        )
        .expand_dims({"REGIONS_35_I": ["RUSSIA"]}, 0)
        .values
    )
    value.loc[["USMCA"], :] = (
        diet_patterns_data_by_gdppc_for_usmca(float(gdppc_9r_for_diets().loc["USMCA"]))
        .expand_dims({"REGIONS_35_I": ["USMCA"]}, 0)
        .values
    )
    value.loc[["LROW"], :] = (
        diet_patterns_data_by_gdppc_for_lrow(float(gdppc_9r_for_diets().loc["LROW"]))
        .expand_dims({"REGIONS_35_I": ["LROW"]}, 0)
        .values
    )
    return value


@component.add(
    name="efect_shortage_of_policy_diet",
    units="DMNL",
    subscripts=["REGIONS_9_I", "FOODS_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={"share_of_available_crops_for_food": 33},
)
def efect_shortage_of_policy_diet():
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "FOODS_I": _subscript_dict["FOODS_I"],
        },
        ["REGIONS_9_I", "FOODS_I"],
    )
    value.loc[:, ["CEREALS_DIET"]] = (
        (
            (
                share_of_available_crops_for_food()
                .loc[:, "CORN"]
                .reset_coords(drop=True)
                + share_of_available_crops_for_food()
                .loc[:, "RICE"]
                .reset_coords(drop=True)
                + share_of_available_crops_for_food()
                .loc[:, "CEREALS_OTHER"]
                .reset_coords(drop=True)
            )
            / 3
        )
        .expand_dims({"FOODS_I": ["CEREALS_DIET"]}, 1)
        .values
    )
    value.loc[:, ["TUBERS_DIET"]] = (
        share_of_available_crops_for_food()
        .loc[:, "TUBERS"]
        .reset_coords(drop=True)
        .expand_dims({"FOODS_I": ["TUBERS_DIET"]}, 1)
        .values
    )
    value.loc[:, ["PULSES_LEGUMES_NUTS"]] = (
        share_of_available_crops_for_food()
        .loc[:, "PULSES_NUTS"]
        .reset_coords(drop=True)
        .expand_dims({"FOODS_I": ["PULSES_LEGUMES_NUTS"]}, 1)
        .values
    )
    value.loc[:, ["FRUITS_VEGETABLES_DIET"]] = (
        share_of_available_crops_for_food()
        .loc[:, "FRUITS_VEGETABLES"]
        .reset_coords(drop=True)
        .expand_dims({"FOODS_I": ["FRUITS_VEGETABLES_DIET"]}, 1)
        .values
    )
    value.loc[:, ["FATS_VEGETAL"]] = (
        share_of_available_crops_for_food()
        .loc[:, "OILCROPS"]
        .reset_coords(drop=True)
        .expand_dims({"FOODS_I": ["FATS_VEGETAL"]}, 1)
        .values
    )
    value.loc[:, ["FATS_ANIMAL"]] = (
        (
            (
                share_of_available_crops_for_food()
                .loc[:, "CORN"]
                .reset_coords(drop=True)
                + share_of_available_crops_for_food()
                .loc[:, "CEREALS_OTHER"]
                .reset_coords(drop=True)
                + share_of_available_crops_for_food()
                .loc[:, "PULSES_NUTS"]
                .reset_coords(drop=True)
                + share_of_available_crops_for_food()
                .loc[:, "SOY"]
                .reset_coords(drop=True)
                + share_of_available_crops_for_food()
                .loc[:, "OILCROPS"]
                .reset_coords(drop=True)
            )
            / 5
        )
        .expand_dims({"FOODS_I": ["FATS_ANIMAL"]}, 1)
        .values
    )
    value.loc[:, ["DAIRY"]] = (
        (
            (
                share_of_available_crops_for_food()
                .loc[:, "CORN"]
                .reset_coords(drop=True)
                + share_of_available_crops_for_food()
                .loc[:, "CEREALS_OTHER"]
                .reset_coords(drop=True)
                + share_of_available_crops_for_food()
                .loc[:, "PULSES_NUTS"]
                .reset_coords(drop=True)
                + share_of_available_crops_for_food()
                .loc[:, "SOY"]
                .reset_coords(drop=True)
                + share_of_available_crops_for_food()
                .loc[:, "OILCROPS"]
                .reset_coords(drop=True)
            )
            / 5
        )
        .expand_dims({"FOODS_I": ["DAIRY"]}, 1)
        .values
    )
    value.loc[:, ["EGGS"]] = (
        (
            (
                share_of_available_crops_for_food()
                .loc[:, "CORN"]
                .reset_coords(drop=True)
                + share_of_available_crops_for_food()
                .loc[:, "CEREALS_OTHER"]
                .reset_coords(drop=True)
                + share_of_available_crops_for_food()
                .loc[:, "PULSES_NUTS"]
                .reset_coords(drop=True)
                + share_of_available_crops_for_food()
                .loc[:, "SOY"]
                .reset_coords(drop=True)
                + share_of_available_crops_for_food()
                .loc[:, "OILCROPS"]
                .reset_coords(drop=True)
            )
            / 5
        )
        .expand_dims({"FOODS_I": ["EGGS"]}, 1)
        .values
    )
    value.loc[:, ["MEAT_RUMINANTS"]] = (
        (
            (
                share_of_available_crops_for_food()
                .loc[:, "CORN"]
                .reset_coords(drop=True)
                + share_of_available_crops_for_food()
                .loc[:, "CEREALS_OTHER"]
                .reset_coords(drop=True)
                + share_of_available_crops_for_food()
                .loc[:, "PULSES_NUTS"]
                .reset_coords(drop=True)
                + share_of_available_crops_for_food()
                .loc[:, "SOY"]
                .reset_coords(drop=True)
                + share_of_available_crops_for_food()
                .loc[:, "OILCROPS"]
                .reset_coords(drop=True)
            )
            / 5
        )
        .expand_dims({"FOODS_I": ["MEAT_RUMINANTS"]}, 1)
        .values
    )
    value.loc[:, ["MEAT_MONOGASTRIC"]] = (
        (
            (
                share_of_available_crops_for_food()
                .loc[:, "CORN"]
                .reset_coords(drop=True)
                + share_of_available_crops_for_food()
                .loc[:, "CEREALS_OTHER"]
                .reset_coords(drop=True)
                + share_of_available_crops_for_food()
                .loc[:, "PULSES_NUTS"]
                .reset_coords(drop=True)
                + share_of_available_crops_for_food()
                .loc[:, "SOY"]
                .reset_coords(drop=True)
                + share_of_available_crops_for_food()
                .loc[:, "OILCROPS"]
                .reset_coords(drop=True)
            )
            / 5
        )
        .expand_dims({"FOODS_I": ["MEAT_MONOGASTRIC"]}, 1)
        .values
    )
    value.loc[:, ["FISH"]] = 1
    value.loc[:, ["SUGARS"]] = (
        share_of_available_crops_for_food()
        .loc[:, "SUGAR_CROPS"]
        .reset_coords(drop=True)
        .expand_dims({"FOODS_I": ["SUGARS"]}, 1)
        .values
    )
    value.loc[:, ["BEVERAGES"]] = 1
    value.loc[:, ["STIMULANTS"]] = 1
    return value


@component.add(
    name="EXO_BIOFUELS_ALL_TRANSPORT",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_exo_biofuels_all_transport"},
)
def exo_biofuels_all_transport():
    return _ext_constant_exo_biofuels_all_transport()


_ext_constant_exo_biofuels_all_transport = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "exogenous_inputs",
    "EXO_BIOFUELS_FINAL*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_exo_biofuels_all_transport",
)


@component.add(
    name="EXO_BIOFUELS_INITIAL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_exo_biofuels_initial"},
)
def exo_biofuels_initial():
    return _ext_constant_exo_biofuels_initial()


_ext_constant_exo_biofuels_initial = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "exogenous_inputs",
    "EXO_BIOFUELS_INITIAL*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_exo_biofuels_initial",
)


@component.add(
    name="EXO_energy_demanded_biofuels",
    subscripts=["REGIONS_9_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_exo_energy_demanded_biofuels": 1},
    other_deps={
        "_integ_exo_energy_demanded_biofuels": {
            "initial": {},
            "step": {"increment_extra_biofuels": 1},
        }
    },
)
def exo_energy_demanded_biofuels():
    return _integ_exo_energy_demanded_biofuels()


_integ_exo_energy_demanded_biofuels = Integ(
    lambda: increment_extra_biofuels(),
    lambda: xr.DataArray(
        0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
    ),
    "_integ_exo_energy_demanded_biofuels",
)


@component.add(
    name="EXO_increment_demand_biomass",
    units="DMNL",
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_exo_increment_demand_biomass": 1},
    other_deps={
        "_integ_exo_increment_demand_biomass": {
            "initial": {},
            "step": {"increment_extra_biomass": 1},
        }
    },
)
def exo_increment_demand_biomass():
    """
    only for testing para el articulo metodologico, no usada
    """
    return _integ_exo_increment_demand_biomass()


_integ_exo_increment_demand_biomass = Integ(
    lambda: increment_extra_biomass(), lambda: 1, "_integ_exo_increment_demand_biomass"
)


@component.add(
    name="food_demanded_by_households_per_region",
    units="t/Year",
    subscripts=["REGIONS_9_I", "FOODS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "diet_demanded": 1,
        "population_9_regions_for_diets": 1,
        "unit_conversion_t_kg": 1,
    },
)
def food_demanded_by_households_per_region():
    """
    tonnes of food demanded by region
    """
    return diet_demanded() * population_9_regions_for_diets() * unit_conversion_t_kg()


@component.add(
    name="food_demanded_from_land_products",
    units="t/Year",
    subscripts=["REGIONS_9_I", "FOODS_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "food_demanded_by_households_per_region": 13,
        "dairy_obtained_from_grasslands": 1,
        "meat_obtained_from_grasslands": 1,
    },
)
def food_demanded_from_land_products():
    """
    diets of households by regions and without meat and dairy from grasslands and without fish
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "FOODS_I": _subscript_dict["FOODS_I"],
        },
        ["REGIONS_9_I", "FOODS_I"],
    )
    value.loc[:, ["CEREALS_DIET"]] = (
        food_demanded_by_households_per_region()
        .loc[:, "CEREALS_DIET"]
        .reset_coords(drop=True)
        .expand_dims({"FOODS_I": ["CEREALS_DIET"]}, 1)
        .values
    )
    value.loc[:, ["TUBERS_DIET"]] = (
        food_demanded_by_households_per_region()
        .loc[:, "TUBERS_DIET"]
        .reset_coords(drop=True)
        .expand_dims({"FOODS_I": ["TUBERS_DIET"]}, 1)
        .values
    )
    value.loc[:, ["PULSES_LEGUMES_NUTS"]] = (
        food_demanded_by_households_per_region()
        .loc[:, "PULSES_LEGUMES_NUTS"]
        .reset_coords(drop=True)
        .expand_dims({"FOODS_I": ["PULSES_LEGUMES_NUTS"]}, 1)
        .values
    )
    value.loc[:, ["FRUITS_VEGETABLES_DIET"]] = (
        food_demanded_by_households_per_region()
        .loc[:, "FRUITS_VEGETABLES_DIET"]
        .reset_coords(drop=True)
        .expand_dims({"FOODS_I": ["FRUITS_VEGETABLES_DIET"]}, 1)
        .values
    )
    value.loc[:, ["FATS_VEGETAL"]] = (
        food_demanded_by_households_per_region()
        .loc[:, "FATS_VEGETAL"]
        .reset_coords(drop=True)
        .expand_dims({"FOODS_I": ["FATS_VEGETAL"]}, 1)
        .values
    )
    value.loc[:, ["FATS_ANIMAL"]] = (
        food_demanded_by_households_per_region()
        .loc[:, "FATS_ANIMAL"]
        .reset_coords(drop=True)
        .expand_dims({"FOODS_I": ["FATS_ANIMAL"]}, 1)
        .values
    )
    value.loc[:, ["DAIRY"]] = (
        np.maximum(
            0,
            food_demanded_by_households_per_region()
            .loc[:, "DAIRY"]
            .reset_coords(drop=True)
            - dairy_obtained_from_grasslands(),
        )
        .expand_dims({"FOODS_I": ["DAIRY"]}, 1)
        .values
    )
    value.loc[:, ["EGGS"]] = (
        food_demanded_by_households_per_region()
        .loc[:, "EGGS"]
        .reset_coords(drop=True)
        .expand_dims({"FOODS_I": ["EGGS"]}, 1)
        .values
    )
    value.loc[:, ["MEAT_RUMINANTS"]] = (
        np.maximum(
            0,
            food_demanded_by_households_per_region()
            .loc[:, "MEAT_RUMINANTS"]
            .reset_coords(drop=True)
            - meat_obtained_from_grasslands(),
        )
        .expand_dims({"FOODS_I": ["MEAT_RUMINANTS"]}, 1)
        .values
    )
    value.loc[:, ["MEAT_MONOGASTRIC"]] = (
        food_demanded_by_households_per_region()
        .loc[:, "MEAT_MONOGASTRIC"]
        .reset_coords(drop=True)
        .expand_dims({"FOODS_I": ["MEAT_MONOGASTRIC"]}, 1)
        .values
    )
    value.loc[:, ["FISH"]] = 0
    value.loc[:, ["SUGARS"]] = (
        food_demanded_by_households_per_region()
        .loc[:, "SUGARS"]
        .reset_coords(drop=True)
        .expand_dims({"FOODS_I": ["SUGARS"]}, 1)
        .values
    )
    value.loc[:, ["BEVERAGES"]] = (
        food_demanded_by_households_per_region()
        .loc[:, "BEVERAGES"]
        .reset_coords(drop=True)
        .expand_dims({"FOODS_I": ["BEVERAGES"]}, 1)
        .values
    )
    value.loc[:, ["STIMULANTS"]] = (
        food_demanded_by_households_per_region()
        .loc[:, "STIMULANTS"]
        .reset_coords(drop=True)
        .expand_dims({"FOODS_I": ["STIMULANTS"]}, 1)
        .values
    )
    return value


@component.add(
    name="food_demanded_world",
    units="t/Year",
    subscripts=["FOODS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"food_demanded_by_households_per_region": 1},
)
def food_demanded_world():
    return sum(
        food_demanded_by_households_per_region().rename(
            {"REGIONS_9_I": "REGIONS_9_I!"}
        ),
        dim=["REGIONS_9_I!"],
    )


@component.add(
    name="GDP_down_coefficient",
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_gdp_down_coefficient": 1},
    other_deps={
        "_integ_gdp_down_coefficient": {
            "initial": {},
            "step": {"decrement_gdp_coefficient": 1},
        }
    },
)
def gdp_down_coefficient():
    return _integ_gdp_down_coefficient()


_integ_gdp_down_coefficient = Integ(
    lambda: decrement_gdp_coefficient(), lambda: 1, "_integ_gdp_down_coefficient"
)


@component.add(
    name="GDPpc_9R_for_diets",
    units="Mdollars_2015/(Year*person)",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_landwater": 1,
        "time": 1,
        "time_historical_data_land_module": 1,
        "imv_gdppc_9r_exogenous": 1,
        "gdppc_9r_real": 1,
    },
)
def gdppc_9r_for_diets():
    """
    GDPpc per share of availability of land products for food
    """
    return if_then_else(
        np.logical_or(
            switch_landwater() == 0, time() < time_historical_data_land_module()
        ),
        lambda: imv_gdppc_9r_exogenous(),
        lambda: gdppc_9r_real(),
    )


@component.add(
    name="GDPpc_per_share_of_available_food",
    units="Mdollars_2015/(Year*person)",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "gdppc_9r_for_diets": 1,
        "share_of_available_food": 1,
        "factor_of_food_availability": 1,
    },
)
def gdppc_per_share_of_available_food():
    return (
        gdppc_9r_for_diets() * share_of_available_food() * factor_of_food_availability()
    )


@component.add(
    name="imv_GDPpc_9R_exogenous",
    units="Mdollars_2015/(Year*person)",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "poli_gdp_down": 1,
        "time": 3,
        "imv_exogenous_gdppc_9r": 3,
        "gdp_down_coefficient": 1,
        "poli_constant_gdp": 1,
        "time_historical_data_land_module": 2,
    },
)
def imv_gdppc_9r_exogenous():
    """
    GDPpc real constant values with variation during time for 9 regions
    """
    return if_then_else(
        poli_gdp_down() == 1,
        lambda: imv_exogenous_gdppc_9r(time()) * gdp_down_coefficient(),
        lambda: if_then_else(
            np.logical_and(
                poli_constant_gdp() == 1, time() >= time_historical_data_land_module()
            ),
            lambda: imv_exogenous_gdppc_9r(time_historical_data_land_module()),
            lambda: imv_exogenous_gdppc_9r(time()),
        ),
    )


@component.add(
    name="increase_of_share_of_change_to_policy_diet",
    units="1/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_model_explorer": 1,
        "model_explorer_objective_diets": 1,
        "time": 2,
        "year_initial_diet_change_sp": 2,
        "year_final_diet_change_sp": 2,
        "objective_diet_change_sp": 1,
        "switch_diet_change_sp": 2,
    },
)
def increase_of_share_of_change_to_policy_diet():
    """
    The variation of share of change to policy diet
    """
    return if_then_else(
        switch_model_explorer() == 1,
        lambda: xr.DataArray(
            model_explorer_objective_diets(),
            {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
            ["REGIONS_9_I"],
        ),
        lambda: if_then_else(
            switch_diet_change_sp() == 0,
            lambda: xr.DataArray(
                0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
            ),
            lambda: if_then_else(
                np.logical_and(
                    switch_diet_change_sp() == 1,
                    np.logical_or(
                        time() < year_initial_diet_change_sp(),
                        time() > year_final_diet_change_sp(),
                    ),
                ),
                lambda: xr.DataArray(
                    0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
                ),
                lambda: objective_diet_change_sp()
                / (year_final_diet_change_sp() - year_initial_diet_change_sp()),
            ),
        ),
    )


@component.add(
    name="increment_extra_biofuels",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "poli_biofuels": 1,
        "exo_biofuels_all_transport": 1,
        "time_historical_data_land_module": 2,
        "exo_biofuels_initial": 1,
        "objective_biofuels": 1,
        "time": 1,
    },
)
def increment_extra_biofuels():
    """
    si vale 1 tomamos un valor exogeno de biofuels aumento lineal de la demanda hasta valor deseado
    """
    return if_then_else(
        poli_biofuels() == 1,
        lambda: if_then_else(
            time() < time_historical_data_land_module(),
            lambda: xr.DataArray(
                0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
            ),
            lambda: (
                exo_biofuels_all_transport() * objective_biofuels()
                - exo_biofuels_initial()
            )
            / (2050 - time_historical_data_land_module()),
        ),
        lambda: xr.DataArray(
            0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
        ),
    )


@component.add(
    name="increment_extra_biomass",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"poli_biomass": 1, "time": 1, "time_historical_data_land_module": 2},
)
def increment_extra_biomass():
    return if_then_else(
        poli_biomass() == 1,
        lambda: if_then_else(
            time() < time_historical_data_land_module(),
            lambda: 0,
            lambda: 1 / (2050 - time_historical_data_land_module()),
        ),
        lambda: 0,
    )


@component.add(
    name="land_products_demanded_for_food",
    units="t/Year",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "land_products_demanded_for_food_before_losses": 1,
        "loss_factor_of_land_products": 1,
    },
)
def land_products_demanded_for_food():
    return (
        land_products_demanded_for_food_before_losses() * loss_factor_of_land_products()
    )


@component.add(
    name="land_products_demanded_for_food_before_losses",
    units="t/Year",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "agrofood_transform_matrix": 14,
        "food_demanded_from_land_products": 14,
    },
)
def land_products_demanded_for_food_before_losses():
    """
    calculation of land products demanded for foor by using the Agrofood matrix
    """
    return (
        agrofood_transform_matrix().loc["CEREALS_DIET", :].reset_coords(drop=True)
        * food_demanded_from_land_products()
        .loc[:, "CEREALS_DIET"]
        .reset_coords(drop=True)
        + agrofood_transform_matrix().loc["TUBERS_DIET", :].reset_coords(drop=True)
        * food_demanded_from_land_products()
        .loc[:, "TUBERS_DIET"]
        .reset_coords(drop=True)
        + agrofood_transform_matrix()
        .loc["PULSES_LEGUMES_NUTS", :]
        .reset_coords(drop=True)
        * food_demanded_from_land_products()
        .loc[:, "PULSES_LEGUMES_NUTS"]
        .reset_coords(drop=True)
        + agrofood_transform_matrix()
        .loc["FRUITS_VEGETABLES_DIET", :]
        .reset_coords(drop=True)
        * food_demanded_from_land_products()
        .loc[:, "FRUITS_VEGETABLES_DIET"]
        .reset_coords(drop=True)
        + agrofood_transform_matrix().loc["FATS_VEGETAL", :].reset_coords(drop=True)
        * food_demanded_from_land_products()
        .loc[:, "FATS_VEGETAL"]
        .reset_coords(drop=True)
        + agrofood_transform_matrix().loc["FATS_ANIMAL", :].reset_coords(drop=True)
        * food_demanded_from_land_products()
        .loc[:, "FATS_ANIMAL"]
        .reset_coords(drop=True)
        + agrofood_transform_matrix().loc["DAIRY", :].reset_coords(drop=True)
        * food_demanded_from_land_products().loc[:, "DAIRY"].reset_coords(drop=True)
        + agrofood_transform_matrix().loc["EGGS", :].reset_coords(drop=True)
        * food_demanded_from_land_products().loc[:, "EGGS"].reset_coords(drop=True)
        + agrofood_transform_matrix().loc["MEAT_RUMINANTS", :].reset_coords(drop=True)
        * food_demanded_from_land_products()
        .loc[:, "MEAT_RUMINANTS"]
        .reset_coords(drop=True)
        + agrofood_transform_matrix().loc["MEAT_MONOGASTRIC", :].reset_coords(drop=True)
        * food_demanded_from_land_products()
        .loc[:, "MEAT_MONOGASTRIC"]
        .reset_coords(drop=True)
        + agrofood_transform_matrix().loc["FISH", :].reset_coords(drop=True)
        * food_demanded_from_land_products().loc[:, "FISH"].reset_coords(drop=True)
        + agrofood_transform_matrix().loc["SUGARS", :].reset_coords(drop=True)
        * food_demanded_from_land_products().loc[:, "SUGARS"].reset_coords(drop=True)
        + agrofood_transform_matrix().loc["BEVERAGES", :].reset_coords(drop=True)
        * food_demanded_from_land_products().loc[:, "BEVERAGES"].reset_coords(drop=True)
        + agrofood_transform_matrix().loc["STIMULANTS", :].reset_coords(drop=True)
        * food_demanded_from_land_products()
        .loc[:, "STIMULANTS"]
        .reset_coords(drop=True)
    ).transpose("REGIONS_9_I", "LAND_PRODUCTS_I")


@component.add(
    name="land_products_demanded_for_food_delayed",
    units="t/Year",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_land_products_demanded_for_food_delayed": 1},
    other_deps={
        "_delayfixed_land_products_demanded_for_food_delayed": {
            "initial": {"historical_land_products_production": 1},
            "step": {"land_products_demanded_for_food_before_losses": 1},
        }
    },
)
def land_products_demanded_for_food_delayed():
    return _delayfixed_land_products_demanded_for_food_delayed()


_delayfixed_land_products_demanded_for_food_delayed = DelayFixed(
    lambda: land_products_demanded_for_food_before_losses(),
    lambda: 1,
    lambda: historical_land_products_production(),
    time_step,
    "_delayfixed_land_products_demanded_for_food_delayed",
)


@component.add(
    name="land_products_demanded_for_food_world",
    units="t/Year",
    subscripts=["LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"land_products_demanded_for_food": 1},
)
def land_products_demanded_for_food_world():
    return sum(
        land_products_demanded_for_food().rename({"REGIONS_9_I": "REGIONS_9_I!"}),
        dim=["REGIONS_9_I!"],
    )


@component.add(
    name="meat_obtained_from_grasslands",
    units="t/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "initial_meat_obtained_from_grasslands": 1,
        "land_use_area_by_region": 1,
        "initial_land_use_by_region": 1,
        "factor_of_grassland_production": 1,
    },
)
def meat_obtained_from_grasslands():
    return (
        initial_meat_obtained_from_grasslands()
        * zidz(
            land_use_area_by_region().loc[:, "GRASSLAND"].reset_coords(drop=True),
            initial_land_use_by_region().loc[:, "GRASSLAND"].reset_coords(drop=True),
        )
        * factor_of_grassland_production()
    )


@component.add(name="OBJECTIVE_BIOFUELS", comp_type="Constant", comp_subtype="Normal")
def objective_biofuels():
    """
    TANTO POR CIENTO DEL consumo de 2019 de transprote que esta alimentado de petroleo que se pasa a biocombustibles en 2050
    """
    return 0.2


@component.add(name="OBJECTIVE_GDP_DOWN", comp_type="Constant", comp_subtype="Normal")
def objective_gdp_down():
    """
    no es el objetivo sino el coeficiente que hace bajar el GDP exponencialmente
    """
    return 0.1


@component.add(name="OBJECTIVE_YIELDS", comp_type="Constant", comp_subtype="Normal")
def objective_yields():
    return 0.3


@component.add(
    name="PLANT_BASED_50_PERCENT_DIET_PATTERN_OF_POLICY_DIETS_SP",
    units="kg/(Year*people)",
    subscripts=["REGIONS_9_I", "FOODS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_plant_based_50_percent_diet_pattern_of_policy_diets_sp"
    },
)
def plant_based_50_percent_diet_pattern_of_policy_diets_sp():
    """
    50% plant based policy diet
    """
    return _ext_constant_plant_based_50_percent_diet_pattern_of_policy_diets_sp()


_ext_constant_plant_based_50_percent_diet_pattern_of_policy_diets_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "PLANT_BASED_50_PERCENT_DIET_PATTERN_OF_POLICY_DIETS_SP",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "FOODS_I": _subscript_dict["FOODS_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "FOODS_I": _subscript_dict["FOODS_I"],
    },
    "_ext_constant_plant_based_50_percent_diet_pattern_of_policy_diets_sp",
)


@component.add(name="POLI_BIOFUELS", comp_type="Constant", comp_subtype="Normal")
def poli_biofuels():
    return 1


@component.add(name="POLI_BIOMASS", comp_type="Constant", comp_subtype="Normal")
def poli_biomass():
    """
    si vale 1 tomamos un aumento exogeno de la demanda de biomasa elegido linealmente hasta objtivo
    """
    return 0


@component.add(name="POLI_CONSTANT_GDP", comp_type="Constant", comp_subtype="Normal")
def poli_constant_gdp():
    """
    =0 no effect
    """
    return 0


@component.add(name="POLI_GDP_DOWN", comp_type="Constant", comp_subtype="Normal")
def poli_gdp_down():
    """
    =0 no effect
    """
    return 0


@component.add(name="POLI_YIELDS", comp_type="Constant", comp_subtype="Normal")
def poli_yields():
    """
    =0 no use, trial, SI ESTA A 1 ponemos los limites de rendimientos de industrial R+I desde aqui en lugar de desde el excel, usando el objective poli yields
    """
    return 0


@component.add(
    name="population_9_regions_for_diets",
    units="people",
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
def population_9_regions_for_diets():
    """
    Population constant values with variation during time for 9 regions
    """
    return if_then_else(
        switch_landwater() == 0,
        lambda: exogenous_population_9r(time()),
        lambda: population_9_regions(),
    )


@component.add(
    name="SELECT_POLICY_DIET_PATTERNS_SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_select_policy_diet_patterns_sp"},
)
def select_policy_diet_patterns_sp():
    """
    0: APPLICATION OF FLEXITARIANA_DIET_PATTERNS 1: APPLICATION OF WILLET_DIET_PATTERNS 2: APPLICATION OF BASELINE_DIET_PATTERNS 3: APPLICATION OF PLANT_BASED_50_DIET_PATTERNS 4: APPLICATION OF PLANT_BASED_100_DIET_PATTERN
    """
    return _ext_constant_select_policy_diet_patterns_sp()


_ext_constant_select_policy_diet_patterns_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_OF_DIET_PATTERNS_SELECTED",
    {},
    _root,
    {},
    "_ext_constant_select_policy_diet_patterns_sp",
)


@component.add(
    name="share_of_available_crops_for_food",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "mask_essential_foods": 1,
        "crops_available_for_food": 1,
        "land_products_demanded_for_food_delayed": 1,
    },
)
def share_of_available_crops_for_food():
    return if_then_else(
        (mask_essential_foods() == 1).expand_dims(
            {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, 1
        ),
        lambda: np.minimum(
            1,
            zidz(crops_available_for_food(), land_products_demanded_for_food_delayed()),
        ).transpose("LAND_PRODUCTS_I", "REGIONS_9_I"),
        lambda: xr.DataArray(
            0,
            {
                "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
                "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            },
            ["LAND_PRODUCTS_I", "REGIONS_9_I"],
        ),
    ).transpose("REGIONS_9_I", "LAND_PRODUCTS_I")


@component.add(
    name="share_of_available_food",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"share_of_available_crops_for_food": 1, "mask_essential_foods": 1},
)
def share_of_available_food():
    """
    >1 means food abundance, more that demanded
    """
    return sum(
        share_of_available_crops_for_food().rename(
            {"LAND_PRODUCTS_I": "LAND_PRODUCTS_I!"}
        ),
        dim=["LAND_PRODUCTS_I!"],
    ) / sum(
        mask_essential_foods().rename({"LAND_PRODUCTS_I": "LAND_PRODUCTS_I!"}),
        dim=["LAND_PRODUCTS_I!"],
    )


@component.add(
    name="share_of_change_to_policy_diet",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_share_of_change_to_policy_diet": 1},
    other_deps={
        "_integ_share_of_change_to_policy_diet": {
            "initial": {"share_of_change_to_policy_diet_initial_value_sp": 1},
            "step": {"increase_of_share_of_change_to_policy_diet": 1},
        }
    },
)
def share_of_change_to_policy_diet():
    """
    The share of change to policy diet
    """
    return _integ_share_of_change_to_policy_diet()


_integ_share_of_change_to_policy_diet = Integ(
    lambda: increase_of_share_of_change_to_policy_diet(),
    lambda: share_of_change_to_policy_diet_initial_value_sp(),
    "_integ_share_of_change_to_policy_diet",
)
