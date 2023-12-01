"""
Module land_and_water.land.diets_nutrition
Translated using PySD version 3.10.0
"""


@component.add(
    name="daily_nutritional_intake",
    units="DMNL",
    subscripts=["REGIONS_9_I", "NUTRITION_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"daily_nutritional_intake_by_food": 1},
)
def daily_nutritional_intake():
    """
    Daily nutritional intake by region and nutrion factor
    """
    return sum(
        daily_nutritional_intake_by_food().rename({"FOODS_I": "FOODS_I!"}),
        dim=["FOODS_I!"],
    )


@component.add(
    name="daily_nutritional_intake_by_food",
    units="DMNL",
    subscripts=["REGIONS_9_I", "NUTRITION_I", "FOODS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"diet_after_food_losses": 1, "food_composition_table": 1},
)
def daily_nutritional_intake_by_food():
    """
    Nutritional intake by category of nutritional assessment. Units are different across categories (1000/365/100) --> 1000 g per kg; 365 days per year; 100 g of reference in food composition table
    """
    return (
        diet_after_food_losses() * (1000 / 365 / 100) * food_composition_table()
    ).transpose("REGIONS_9_I", "NUTRITION_I", "FOODS_I")


@component.add(
    name="diet_after_food_losses",
    units="kg/(Year*person)",
    subscripts=["REGIONS_9_I", "FOODS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"diet_demanded": 3, "food_loss_parameters": 8},
)
def diet_after_food_losses():
    """
    diet data after food losses
    """
    return (
        diet_demanded()
        * food_loss_parameters().loc[:, :, "cf"].reset_coords(drop=True)
        * (1 - food_loss_parameters().loc[:, :, "wp_cns"].reset_coords(drop=True) / 100)
        + diet_demanded()
        * food_loss_parameters().loc[:, :, "pct_fresh"].reset_coords(drop=True)
        / 100
        * food_loss_parameters().loc[:, :, "cf_fresh"].reset_coords(drop=True)
        * (1 - food_loss_parameters().loc[:, :, "wp_cns"].reset_coords(drop=True) / 100)
        + diet_demanded()
        * food_loss_parameters().loc[:, :, "pct_prcd"].reset_coords(drop=True)
        / 100
        * food_loss_parameters().loc[:, :, "cf_prcd"].reset_coords(drop=True)
        * (
            1
            - food_loss_parameters().loc[:, :, "wp_cnsprcd"].reset_coords(drop=True)
            / 100
        )
    )


@component.add(
    name="indicator_of_daily_nutritional_intake",
    units="DMNL",
    subscripts=["REGIONS_9_I", "NUTRITION_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "daily_nutritional_intake": 1,
        "maximum_intake_for_healthy_diets": 1,
        "minimum_intake_for_healthy_diets": 1,
    },
)
def indicator_of_daily_nutritional_intake():
    """
    indicator of daily nutritional intake by region and by nutrition type
    """
    return zidz(
        daily_nutritional_intake() - maximum_intake_for_healthy_diets(),
        minimum_intake_for_healthy_diets(),
    )
