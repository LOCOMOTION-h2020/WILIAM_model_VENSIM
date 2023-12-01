"""
Module land_and_water.auxiliary_outputs_and_indicators
Translated using PySD version 3.10.0
"""


@component.add(
    name="accumulated_sea_level_rise_loss",
    subscripts=["REGIONS_9_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_accumulated_sea_level_rise_loss": 1},
    other_deps={
        "_integ_accumulated_sea_level_rise_loss": {
            "initial": {},
            "step": {"increment_sea_level_rise_loss": 1},
        }
    },
)
def accumulated_sea_level_rise_loss():
    return _integ_accumulated_sea_level_rise_loss()


_integ_accumulated_sea_level_rise_loss = Integ(
    lambda: increment_sea_level_rise_loss(),
    lambda: xr.DataArray(
        0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
    ),
    "_integ_accumulated_sea_level_rise_loss",
)


@component.add(
    name="check_summ_all_lands",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "land_use_area_productive_uses": 1,
        "accumulated_sea_level_rise_loss": 1,
        "historical_land_use_by_region": 2,
        "initial_time": 2,
    },
)
def check_summ_all_lands():
    return zidz(
        sum(
            land_use_area_productive_uses().rename({"LANDS_I": "LANDS_I!"}),
            dim=["LANDS_I!"],
        )
        - accumulated_sea_level_rise_loss()
        - sum(
            historical_land_use_by_region(initial_time()).rename(
                {"LANDS_I": "LANDS_I!"}
            ),
            dim=["LANDS_I!"],
        ),
        sum(
            historical_land_use_by_region(initial_time()).rename(
                {"LANDS_I": "LANDS_I!"}
            ),
            dim=["LANDS_I!"],
        ),
    )


@component.add(
    name="combined_indicator_calories_proteins_fats",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "indicator_of_calories_available": 1,
        "indicator_of_fats_available": 1,
        "indicator_of_proteins_available": 1,
    },
)
def combined_indicator_calories_proteins_fats():
    """
    combined_indicator_calories_proteins_fats
    """
    return (
        indicator_of_calories_available()
        + indicator_of_fats_available()
        + indicator_of_proteins_available()
    ) / 3


@component.add(
    name="combined_indicator_calories_proteins_fats_demanded",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "indicator_of_calories_demanded": 1,
        "indicator_of_fats_demanded": 1,
        "indicator_of_proteins_demanded": 1,
    },
)
def combined_indicator_calories_proteins_fats_demanded():
    return (
        indicator_of_calories_demanded()
        + indicator_of_fats_demanded()
        + indicator_of_proteins_demanded()
    ) / 3


@component.add(
    name="demand_for_food",
    units="t/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"land_products_demanded_for_food_before_losses": 1},
)
def demand_for_food():
    """
    Calculation of total demanded for food.
    """
    return sum(
        land_products_demanded_for_food_before_losses().rename(
            {"REGIONS_9_I": "REGIONS_9_I!", "LAND_PRODUCTS_I": "LAND_PRODUCTS_I!"}
        ),
        dim=["REGIONS_9_I!", "LAND_PRODUCTS_I!"],
    )


@component.add(
    name="diet_available_converted_to_kcal_calories",
    units="kcal/(Year*person)",
    subscripts=["REGIONS_9_I", "FOODS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"diet_available": 1, "macronutrient_translation_matrix": 1},
)
def diet_available_converted_to_kcal_calories():
    """
    diet according to GDPpc with kcal (calories)
    """
    return diet_available() * macronutrient_translation_matrix().loc[
        "CALORIES", :
    ].reset_coords(drop=True)


@component.add(
    name="diet_available_converted_to_kcal_calories_world",
    units="kcal/(Year*person)",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"diet_available_converted_to_kcal_calories": 1},
)
def diet_available_converted_to_kcal_calories_world():
    """
    global diet quantity according to GDPpc with kcal (calories) by region
    """
    return sum(
        diet_available_converted_to_kcal_calories().rename({"FOODS_I": "FOODS_I!"}),
        dim=["FOODS_I!"],
    )


@component.add(
    name="diet_available_converted_to_kg_carbohydrates",
    units="kg/(Year*person)",
    subscripts=["REGIONS_9_I", "FOODS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"diet_available": 1, "macronutrient_translation_matrix": 1},
)
def diet_available_converted_to_kg_carbohydrates():
    """
    diet according to GDPpc with kg (carbohydrates)
    """
    return diet_available() * macronutrient_translation_matrix().loc[
        "CARBOHYDRATES", :
    ].reset_coords(drop=True)


@component.add(
    name="diet_available_converted_to_kg_carbohydrates_world",
    units="kg/(Year*person)",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"diet_available_converted_to_kg_carbohydrates": 1},
)
def diet_available_converted_to_kg_carbohydrates_world():
    """
    global diet quantity according to GDPpc with kg (carbohydrates) by region
    """
    return sum(
        diet_available_converted_to_kg_carbohydrates().rename({"FOODS_I": "FOODS_I!"}),
        dim=["FOODS_I!"],
    )


@component.add(
    name="diet_available_converted_to_kg_fats",
    units="kg/(Year*person)",
    subscripts=["REGIONS_9_I", "FOODS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"diet_available": 1, "macronutrient_translation_matrix": 1},
)
def diet_available_converted_to_kg_fats():
    """
    diet according to GDPpc with kg (fats)
    """
    return diet_available() * macronutrient_translation_matrix().loc[
        "FATS", :
    ].reset_coords(drop=True)


@component.add(
    name="diet_available_converted_to_kg_fats_world",
    units="kg/(Year*person)",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"diet_available_converted_to_kg_fats": 1},
)
def diet_available_converted_to_kg_fats_world():
    """
    global diet quantity according to GDPpc with kg (fats) by region
    """
    return sum(
        diet_available_converted_to_kg_fats().rename({"FOODS_I": "FOODS_I!"}),
        dim=["FOODS_I!"],
    )


@component.add(
    name="diet_available_converted_to_kg_proteins",
    units="kg/(Year*person)",
    subscripts=["REGIONS_9_I", "FOODS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"diet_available": 1, "macronutrient_translation_matrix": 1},
)
def diet_available_converted_to_kg_proteins():
    """
    diet according to GDPpc with kg (proteins)
    """
    return diet_available() * macronutrient_translation_matrix().loc[
        "PROTEINS", :
    ].reset_coords(drop=True)


@component.add(
    name="diet_available_converted_to_kg_proteins_world",
    units="kg/(Year*person)",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"diet_available_converted_to_kg_proteins": 1},
)
def diet_available_converted_to_kg_proteins_world():
    """
    global diet quantity according to GDPpc with kg (proteins) by region
    """
    return sum(
        diet_available_converted_to_kg_proteins().rename({"FOODS_I": "FOODS_I!"}),
        dim=["FOODS_I!"],
    )


@component.add(
    name="diet_demanded_converted_to_kcal_calories",
    units="kcal/(Year*person)",
    subscripts=["REGIONS_9_I", "FOODS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"diet_demanded": 1, "macronutrient_translation_matrix": 1},
)
def diet_demanded_converted_to_kcal_calories():
    """
    diet according to GDPpc with kcal (calories)
    """
    return diet_demanded() * macronutrient_translation_matrix().loc[
        "CALORIES", :
    ].reset_coords(drop=True)


@component.add(
    name="diet_demanded_converted_to_kcal_calories_wold",
    units="kcal/(Year*person)",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"diet_demanded_converted_to_kcal_calories": 1},
)
def diet_demanded_converted_to_kcal_calories_wold():
    """
    global diet quantity according to GDPpc with kcal (calories) by region
    """
    return sum(
        diet_demanded_converted_to_kcal_calories().rename({"FOODS_I": "FOODS_I!"}),
        dim=["FOODS_I!"],
    )


@component.add(
    name="diet_demanded_converted_to_kg_carbohydrates",
    units="kg/(Year*person)",
    subscripts=["REGIONS_9_I", "FOODS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"diet_demanded": 1, "macronutrient_translation_matrix": 1},
)
def diet_demanded_converted_to_kg_carbohydrates():
    """
    diet according to GDPpc with kg (carbohydrates)
    """
    return diet_demanded() * macronutrient_translation_matrix().loc[
        "CARBOHYDRATES", :
    ].reset_coords(drop=True)


@component.add(
    name="diet_demanded_converted_to_kg_carbohydrates_world",
    units="kg/(Year*person)",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"diet_demanded_converted_to_kg_carbohydrates": 1},
)
def diet_demanded_converted_to_kg_carbohydrates_world():
    """
    global diet quantity according to GDPpc with kg (carbohydrates) by region
    """
    return sum(
        diet_demanded_converted_to_kg_carbohydrates().rename({"FOODS_I": "FOODS_I!"}),
        dim=["FOODS_I!"],
    )


@component.add(
    name="diet_demanded_converted_to_kg_fats",
    units="kg/(Year*person)",
    subscripts=["REGIONS_9_I", "FOODS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"diet_demanded": 1, "macronutrient_translation_matrix": 1},
)
def diet_demanded_converted_to_kg_fats():
    """
    diet according to GDPpc with kg (fats)
    """
    return diet_demanded() * macronutrient_translation_matrix().loc[
        "FATS", :
    ].reset_coords(drop=True)


@component.add(
    name="diet_demanded_converted_to_kg_fats_world",
    units="kg/(Year*person)",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"diet_demanded_converted_to_kg_fats": 1},
)
def diet_demanded_converted_to_kg_fats_world():
    """
    global diet quantity according to GDPpc with kg (fats) by region
    """
    return sum(
        diet_demanded_converted_to_kg_fats().rename({"FOODS_I": "FOODS_I!"}),
        dim=["FOODS_I!"],
    )


@component.add(
    name="diet_demanded_converted_to_kg_proteins",
    units="kg/(Year*person)",
    subscripts=["REGIONS_9_I", "FOODS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"diet_demanded": 1, "macronutrient_translation_matrix": 1},
)
def diet_demanded_converted_to_kg_proteins():
    """
    diet according to GDPpc with kg (proteins)
    """
    return diet_demanded() * macronutrient_translation_matrix().loc[
        "PROTEINS", :
    ].reset_coords(drop=True)


@component.add(
    name="diet_demanded_converted_to_kg_proteins_world",
    units="kg/(Year*person)",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"diet_demanded_converted_to_kg_proteins": 1},
)
def diet_demanded_converted_to_kg_proteins_world():
    """
    global diet quantity according to GDPpc with kg (proteins) by region
    """
    return sum(
        diet_demanded_converted_to_kg_proteins().rename({"FOODS_I": "FOODS_I!"}),
        dim=["FOODS_I!"],
    )


@component.add(
    name="increment_sea_level_rise_loss",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "time_historical_data_land_module": 1,
        "cropland_loss_due_to_sea_level_rise_by_region": 1,
    },
)
def increment_sea_level_rise_loss():
    return if_then_else(
        time() < time_historical_data_land_module(),
        lambda: xr.DataArray(
            0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
        ),
        lambda: cropland_loss_due_to_sea_level_rise_by_region(),
    )


@component.add(
    name="indicator_of_calories_available",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "diet_available_converted_to_kcal_calories_world": 1,
        "maximum_intake_for_healthy_diets_1": 1,
        "minimum_intake_for_healthy_diets_1": 1,
    },
)
def indicator_of_calories_available():
    """
    share compared to healthy diet if indicator <0 , shortage indicadot >0 excess
    """
    return zidz(
        diet_available_converted_to_kcal_calories_world()
        - maximum_intake_for_healthy_diets_1()
        .loc[:, "CALORIES"]
        .reset_coords(drop=True),
        minimum_intake_for_healthy_diets_1().loc[:, "CALORIES"].reset_coords(drop=True),
    )


@component.add(
    name="indicator_of_calories_demanded",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "diet_demanded_converted_to_kcal_calories_wold": 1,
        "maximum_intake_for_healthy_diets_1": 1,
        "minimum_intake_for_healthy_diets_1": 1,
    },
)
def indicator_of_calories_demanded():
    """
    share of calories compared to healthy diet if indicator <0 , shortage of calories indicadot >0 excess of calories
    """
    return zidz(
        diet_demanded_converted_to_kcal_calories_wold()
        - maximum_intake_for_healthy_diets_1()
        .loc[:, "CALORIES"]
        .reset_coords(drop=True),
        minimum_intake_for_healthy_diets_1().loc[:, "CALORIES"].reset_coords(drop=True),
    )


@component.add(
    name="indicator_of_carbohydrates_available",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "diet_available_converted_to_kg_carbohydrates_world": 1,
        "maximum_intake_for_healthy_diets_1": 1,
        "minimum_intake_for_healthy_diets_1": 1,
    },
)
def indicator_of_carbohydrates_available():
    """
    share compared to healthy diet if indicator <0 , shortage indicadot >0 excess
    """
    return zidz(
        diet_available_converted_to_kg_carbohydrates_world()
        - maximum_intake_for_healthy_diets_1()
        .loc[:, "CARBOHYDRATES"]
        .reset_coords(drop=True),
        minimum_intake_for_healthy_diets_1()
        .loc[:, "CARBOHYDRATES"]
        .reset_coords(drop=True),
    )


@component.add(
    name="indicator_of_carbohydrates_demanded",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "diet_demanded_converted_to_kg_carbohydrates_world": 1,
        "maximum_intake_for_healthy_diets_1": 1,
        "minimum_intake_for_healthy_diets_1": 1,
    },
)
def indicator_of_carbohydrates_demanded():
    """
    share compared to healthy diet if indicator <0 , shortage indicadot >0 excess
    """
    return zidz(
        diet_demanded_converted_to_kg_carbohydrates_world()
        - maximum_intake_for_healthy_diets_1()
        .loc[:, "CARBOHYDRATES"]
        .reset_coords(drop=True),
        minimum_intake_for_healthy_diets_1()
        .loc[:, "CARBOHYDRATES"]
        .reset_coords(drop=True),
    )


@component.add(
    name="indicator_of_fats_available",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "diet_available_converted_to_kg_fats_world": 1,
        "maximum_intake_for_healthy_diets_1": 1,
        "minimum_intake_for_healthy_diets_1": 1,
    },
)
def indicator_of_fats_available():
    """
    share compared to healthy diet if indicator <0 , shortage indicadot >0 excess
    """
    return zidz(
        diet_available_converted_to_kg_fats_world()
        - maximum_intake_for_healthy_diets_1().loc[:, "FATS"].reset_coords(drop=True),
        minimum_intake_for_healthy_diets_1().loc[:, "FATS"].reset_coords(drop=True),
    )


@component.add(
    name="indicator_of_fats_demanded",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "diet_demanded_converted_to_kg_fats_world": 1,
        "maximum_intake_for_healthy_diets_1": 1,
        "minimum_intake_for_healthy_diets_1": 1,
    },
)
def indicator_of_fats_demanded():
    """
    share of fats compared to healthy diet if indicator <0 , shortage of fats indicadot >0 excess of fats
    """
    return zidz(
        diet_demanded_converted_to_kg_fats_world()
        - maximum_intake_for_healthy_diets_1().loc[:, "FATS"].reset_coords(drop=True),
        minimum_intake_for_healthy_diets_1().loc[:, "FATS"].reset_coords(drop=True),
    )


@component.add(
    name="indicator_of_proteins_available",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "diet_available_converted_to_kg_proteins_world": 1,
        "maximum_intake_for_healthy_diets_1": 1,
        "minimum_intake_for_healthy_diets_1": 1,
    },
)
def indicator_of_proteins_available():
    """
    share compared to healthy diet if indicator <0 , shortage indicadot >0 excess
    """
    return zidz(
        diet_available_converted_to_kg_proteins_world()
        - maximum_intake_for_healthy_diets_1()
        .loc[:, "PROTEINS"]
        .reset_coords(drop=True),
        minimum_intake_for_healthy_diets_1().loc[:, "PROTEINS"].reset_coords(drop=True),
    )


@component.add(
    name="indicator_of_proteins_demanded",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "diet_demanded_converted_to_kg_proteins_world": 1,
        "maximum_intake_for_healthy_diets_1": 1,
        "minimum_intake_for_healthy_diets_1": 1,
    },
)
def indicator_of_proteins_demanded():
    """
    share of proteins compared to healthy diet if indicator <0 ,proteins shortage indicadot >0 excess of proteins
    """
    return zidz(
        diet_demanded_converted_to_kg_proteins_world()
        - maximum_intake_for_healthy_diets_1()
        .loc[:, "PROTEINS"]
        .reset_coords(drop=True),
        minimum_intake_for_healthy_diets_1().loc[:, "PROTEINS"].reset_coords(drop=True),
    )


@component.add(
    name="land_use_area_1R",
    units="km2",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"land_use_area_by_region": 1},
)
def land_use_area_1r():
    """
    Total land use area.
    """
    return sum(
        land_use_area_by_region().rename(
            {"REGIONS_9_I": "REGIONS_9_I!", "LANDS_I": "LANDS_I!"}
        ),
        dim=["REGIONS_9_I!", "LANDS_I!"],
    )


@component.add(
    name="MACRONUTRIENT_TRANSLATION_MATRIX",
    units="DMNL",
    subscripts=["MACRONUTRIENT_FACTORS_I", "FOODS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_macronutrient_translation_matrix"},
)
def macronutrient_translation_matrix():
    """
    this matrix allows to convert from kg (diets) to kcal (calories), kg (proteins), kg (fats) or kg (carbohydrates)
    """
    return _ext_constant_macronutrient_translation_matrix()


_ext_constant_macronutrient_translation_matrix = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Diet",
    "MACRONUTRIENT_TRANSLATION_MATRIX",
    {
        "MACRONUTRIENT_FACTORS_I": _subscript_dict["MACRONUTRIENT_FACTORS_I"],
        "FOODS_I": _subscript_dict["FOODS_I"],
    },
    _root,
    {
        "MACRONUTRIENT_FACTORS_I": _subscript_dict["MACRONUTRIENT_FACTORS_I"],
        "FOODS_I": _subscript_dict["FOODS_I"],
    },
    "_ext_constant_macronutrient_translation_matrix",
)


@component.add(
    name="MAXIMUM_INTAKE_FOR_HEALTHY_DIETS_1",
    units="kcal/(Year*person)",
    subscripts=["REGIONS_9_I", "MACRONUTRIENT_FACTORS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_maximum_intake_for_healthy_diets_1"},
)
def maximum_intake_for_healthy_diets_1():
    """
    the maximum intake for helthy diets with macronutrient factors
    """
    return _ext_constant_maximum_intake_for_healthy_diets_1()


_ext_constant_maximum_intake_for_healthy_diets_1 = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Diet",
    "MAXIMUM_INTAKE_FOR_HEALTHY_DIETS_1",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "MACRONUTRIENT_FACTORS_I": _subscript_dict["MACRONUTRIENT_FACTORS_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "MACRONUTRIENT_FACTORS_I": _subscript_dict["MACRONUTRIENT_FACTORS_I"],
    },
    "_ext_constant_maximum_intake_for_healthy_diets_1",
)


@component.add(
    name="MINIMUM_INTAKE_FOR_HEALTHY_DIETS_1",
    units="kcal/(Year*person)",
    subscripts=["REGIONS_9_I", "MACRONUTRIENT_FACTORS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_minimum_intake_for_healthy_diets_1"},
)
def minimum_intake_for_healthy_diets_1():
    """
    the minimum intake for helthy diets with macronutrient factors
    """
    return _ext_constant_minimum_intake_for_healthy_diets_1()


_ext_constant_minimum_intake_for_healthy_diets_1 = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Diet",
    "MINIMUM_INTAKE_FOR_HEALTHY_DIETS_1",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "MACRONUTRIENT_FACTORS_I": _subscript_dict["MACRONUTRIENT_FACTORS_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "MACRONUTRIENT_FACTORS_I": _subscript_dict["MACRONUTRIENT_FACTORS_I"],
    },
    "_ext_constant_minimum_intake_for_healthy_diets_1",
)


@component.add(
    name="water_stress_1R",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"water_stress_by_region": 2},
)
def water_stress_1r():
    """
    Total water strees.
    """
    return zidz(
        zidz(
            sum(
                water_stress_by_region()
                .loc[_subscript_dict["REGIONS_EU27_I"]]
                .rename({"REGIONS_35_I": "REGIONS_EU27_I!"}),
                dim=["REGIONS_EU27_I!"],
            ),
            27,
        )
        + zidz(
            sum(
                water_stress_by_region()
                .loc[_subscript_dict["REGIONS_8_I"]]
                .rename({"REGIONS_35_I": "REGIONS_8_I!"}),
                dim=["REGIONS_8_I!"],
            ),
            8,
        ),
        2,
    )
