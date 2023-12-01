"""
Module land_and_water.land.crop_yields
Translated using PySD version 3.10.0
"""


@component.add(
    name="aux_effect_CC_on_yields",
    subscripts=["REGIONS_9_I", "CLIMATIC_ZONES_I", "LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "matrix_of_cc_yields_zone_region": 1,
        "factor_of_cc_effect_per_zone_and_crop": 1,
    },
)
def aux_effect_cc_on_yields():
    return matrix_of_cc_yields_zone_region() * factor_of_cc_effect_per_zone_and_crop()


@component.add(
    name="aux_trends_of_yield_change_R_and_I",
    units="t/(km2*Year)",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "time_historical_data_land_module": 1,
        "trends_of_yield_change_r_and_i": 2,
    },
)
def aux_trends_of_yield_change_r_and_i():
    """
    This variable is to avoid that yields decrease after the historical perior. Some crops like tubers in some regions show a trend that goes down but the historical data is not clear to show that this is a real decrease, we leave it constant.
    """
    return if_then_else(
        time() <= time_historical_data_land_module(),
        lambda: trends_of_yield_change_r_and_i(),
        lambda: np.maximum(0, trends_of_yield_change_r_and_i()),
    )


@component.add(
    name="average_effect_of_management_on_crops",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"effect_of_management_on_crops": 1},
)
def average_effect_of_management_on_crops():
    return sum(
        effect_of_management_on_crops().rename({"LAND_PRODUCTS_I": "LAND_PRODUCTS_I!"}),
        dim=["LAND_PRODUCTS_I!"],
    ) / (
        len(
            xr.DataArray(
                np.arange(1, len(_subscript_dict["LAND_PRODUCTS_I"]) + 1),
                {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"]},
                ["LAND_PRODUCTS_I"],
            )
        )
        - 3
    )


@component.add(
    name="average_share_of_agriculture_in_transition",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"share_of_agriculture_in_transition": 1},
)
def average_share_of_agriculture_in_transition():
    return sum(
        share_of_agriculture_in_transition().rename(
            {"LAND_PRODUCTS_I": "LAND_PRODUCTS_I!"}
        ),
        dim=["LAND_PRODUCTS_I!"],
    ) / (
        len(
            xr.DataArray(
                np.arange(1, len(_subscript_dict["LAND_PRODUCTS_I"]) + 1),
                {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"]},
                ["LAND_PRODUCTS_I"],
            )
        )
        - 3
    )


@component.add(
    name="average_share_of_industrial_agriculture",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"share_of_industrial_agriculture": 1},
)
def average_share_of_industrial_agriculture():
    return sum(
        share_of_industrial_agriculture().rename(
            {"LAND_PRODUCTS_I": "LAND_PRODUCTS_I!"}
        ),
        dim=["LAND_PRODUCTS_I!"],
    ) / (
        len(
            xr.DataArray(
                np.arange(1, len(_subscript_dict["LAND_PRODUCTS_I"]) + 1),
                {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"]},
                ["LAND_PRODUCTS_I"],
            )
        )
        - 3
    )


@component.add(
    name="average_share_of_low_input_agriculture",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"share_of_low_input_agriculture": 1},
)
def average_share_of_low_input_agriculture():
    return sum(
        share_of_low_input_agriculture().rename(
            {"LAND_PRODUCTS_I": "LAND_PRODUCTS_I!"}
        ),
        dim=["LAND_PRODUCTS_I!"],
    ) / (
        len(
            xr.DataArray(
                np.arange(1, len(_subscript_dict["LAND_PRODUCTS_I"]) + 1),
                {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"]},
                ["LAND_PRODUCTS_I"],
            )
        )
        - 3
    )


@component.add(
    name="average_share_of_regenerative_agriculture",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"share_of_regenerative_agriculture": 1},
)
def average_share_of_regenerative_agriculture():
    return sum(
        share_of_regenerative_agriculture().rename(
            {"LAND_PRODUCTS_I": "LAND_PRODUCTS_I!"}
        ),
        dim=["LAND_PRODUCTS_I!"],
    ) / (
        len(
            xr.DataArray(
                np.arange(1, len(_subscript_dict["LAND_PRODUCTS_I"]) + 1),
                {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"]},
                ["LAND_PRODUCTS_I"],
            )
        )
        - 3
    )


@component.add(
    name="average_share_of_traditional_agriculture",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"share_of_traditional_agriculture": 1},
)
def average_share_of_traditional_agriculture():
    return sum(
        share_of_traditional_agriculture().rename(
            {"LAND_PRODUCTS_I": "LAND_PRODUCTS_I!"}
        ),
        dim=["LAND_PRODUCTS_I!"],
    ) / (
        len(
            xr.DataArray(
                np.arange(1, len(_subscript_dict["LAND_PRODUCTS_I"]) + 1),
                {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"]},
                ["LAND_PRODUCTS_I"],
            )
        )
        - 3
    )


@component.add(
    name="average_yields_world",
    units="t/(km2*Year)",
    subscripts=["LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"yields_of_crops_all_managements": 1},
)
def average_yields_world():
    return (
        sum(
            yields_of_crops_all_managements().rename({"REGIONS_9_I": "REGIONS_9_I!"}),
            dim=["REGIONS_9_I!"],
        )
        / 9
    )


@component.add(
    name="change_to_regenerative_agriculture_sp",
    units="DMNL/Year",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_model_explorer": 1,
        "model_explorer_change_to_regenerative_agriculture": 1,
        "year_final_regenerative_agriculture_sp": 2,
        "objective_regenerative_agriculture_sp": 1,
        "switch_regenerative_agriculture_sp": 1,
        "year_initial_regenerative_agriculture_sp": 2,
        "time": 2,
        "initial_share_of_regenerative_agriculture": 1,
    },
)
def change_to_regenerative_agriculture_sp():
    return if_then_else(
        switch_model_explorer() == 1,
        lambda: model_explorer_change_to_regenerative_agriculture(),
        lambda: if_then_else(
            np.logical_and(
                switch_regenerative_agriculture_sp() == 1,
                np.logical_and(
                    time() > year_initial_regenerative_agriculture_sp(),
                    time() < year_final_regenerative_agriculture_sp(),
                ),
            ).expand_dims({"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"]}, 1),
            lambda: (
                objective_regenerative_agriculture_sp()
                - initial_share_of_regenerative_agriculture()
            )
            / (
                year_final_regenerative_agriculture_sp()
                - year_initial_regenerative_agriculture_sp()
            ),
            lambda: xr.DataArray(
                0,
                {
                    "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                    "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
                },
                ["REGIONS_9_I", "LAND_PRODUCTS_I"],
            ),
        ),
    )


@component.add(
    name="check_correction_factor_irrigation",
    subscripts=["LAND_PRODUCTS_I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def check_correction_factor_irrigation():
    return xr.DataArray(
        1, {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"]}, ["LAND_PRODUCTS_I"]
    )


@component.add(
    name="effect_of_climate_change_on_yields",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "number_elements_zones": 1,
        "switch_cli2law_cc_effects": 1,
        "aux_effect_cc_on_yields": 1,
    },
)
def effect_of_climate_change_on_yields():
    """
    effect of climate change on yields, only calculated for cereals, rice, corn and soy
    """
    return if_then_else(
        np.logical_or(number_elements_zones() == 0, switch_cli2law_cc_effects() == 0),
        lambda: xr.DataArray(
            1,
            {
                "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
            },
            ["REGIONS_9_I", "LAND_PRODUCTS_I"],
        ),
        lambda: sum(
            aux_effect_cc_on_yields().rename({"CLIMATIC_ZONES_I": "CLIMATIC_ZONES_I!"}),
            dim=["CLIMATIC_ZONES_I!"],
        ),
    )


@component.add(
    name="effect_of_irrigation_of_yields_corrected",
    subscripts=["LAND_PRODUCTS_I", "REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "check_correction_factor_irrigation": 1,
        "effect_of_irrigation_on_yields": 1,
    },
)
def effect_of_irrigation_of_yields_corrected():
    return (
        check_correction_factor_irrigation()
        * effect_of_irrigation_on_yields().transpose("LAND_PRODUCTS_I", "REGIONS_9_I")
    )


@component.add(
    name="effect_of_management_on_crops",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "share_of_industrial_agriculture": 1,
        "share_of_traditional_agriculture": 1,
        "effect_of_low_input_agriculture": 1,
        "share_of_agriculture_in_transition": 1,
        "share_of_low_input_agriculture": 1,
        "effect_of_regenerative_agriculture": 1,
        "share_of_regenerative_agriculture": 1,
    },
)
def effect_of_management_on_crops():
    """
    we assume that all irrigated is high input, effect of tradition removed
    """
    return (
        share_of_industrial_agriculture()
        + (
            share_of_agriculture_in_transition()
            + share_of_low_input_agriculture()
            + share_of_traditional_agriculture()
        )
        * effect_of_low_input_agriculture()
        + share_of_regenerative_agriculture() * effect_of_regenerative_agriculture()
    )


@component.add(
    name="EFFECT_OF_TRADITIONAL_AGRICULTURE",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"effect_of_low_input_agriculture": 1},
)
def effect_of_traditional_agriculture():
    return effect_of_low_input_agriculture()


@component.add(
    name="factor_of_CC_effect_per_zone_and_crop",
    subscripts=["REGIONS_9_I", "CLIMATIC_ZONES_I", "LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "factor_alfa_1_effects_of_cc_on_yields": 2,
        "initial_co2_concentration": 2,
        "factor_b_1_effects_of_cc_on_yields": 1,
        "atmospheric_concentrations_co2": 2,
        "initial_temperature_by_region_and_climate": 2,
        "temperature_change_by_region_and_climate": 2,
        "factor_alfa_2_effects_of_cc_on_yields": 1,
        "switch_cli2law_cc_fertilization": 1,
        "factor_b_2_effects_of_cc_on_yields": 1,
    },
)
def factor_of_cc_effect_per_zone_and_crop():
    """
    if =-1 data is not provided and the effect of CC on this items not calculated
    """
    return if_then_else(
        (factor_alfa_1_effects_of_cc_on_yields() == 0).expand_dims(
            {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, 2
        ),
        lambda: xr.DataArray(
            -1,
            {
                "CLIMATIC_ZONES_I": _subscript_dict["CLIMATIC_ZONES_I"],
                "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
                "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            },
            ["CLIMATIC_ZONES_I", "LAND_PRODUCTS_I", "REGIONS_9_I"],
        ),
        lambda: 1
        + factor_alfa_1_effects_of_cc_on_yields()
        * (
            temperature_change_by_region_and_climate()
            - initial_temperature_by_region_and_climate().transpose(
                "CLIMATIC_ZONES_I", "REGIONS_9_I"
            )
        )
        + factor_alfa_2_effects_of_cc_on_yields()
        * (
            (
                temperature_change_by_region_and_climate()
                - initial_temperature_by_region_and_climate().transpose(
                    "CLIMATIC_ZONES_I", "REGIONS_9_I"
                )
            )
            ** 2
        )
        + (
            factor_b_1_effects_of_cc_on_yields()
            * switch_cli2law_cc_fertilization()
            * zidz(
                xr.DataArray(
                    atmospheric_concentrations_co2() - initial_co2_concentration(),
                    {
                        "CLIMATIC_ZONES_I": _subscript_dict["CLIMATIC_ZONES_I"],
                        "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
                    },
                    ["CLIMATIC_ZONES_I", "LAND_PRODUCTS_I"],
                ),
                (atmospheric_concentrations_co2() - initial_co2_concentration())
                + factor_b_2_effects_of_cc_on_yields(),
            )
        ),
    ).transpose("REGIONS_9_I", "CLIMATIC_ZONES_I", "LAND_PRODUCTS_I")


@component.add(
    name="fertilizers_demanded",
    units="t",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "chemical_fertilizers_per_cropland_area": 1,
        "average_share_of_industrial_agriculture": 1,
        "land_use_area_by_region": 2,
    },
)
def fertilizers_demanded():
    """
    Fertilizers demanded depending of the type of cropland management (share of industrial agriculture) **NOTES-TODO: potential improvement: demand of fertilizers or fertilizers quantity applied based on type of crop management be better quantified (include more data about management--> excel noelia_marga calibrate "industrial area vs tradictional and agricological?) We could use this information to calibrate Nitrogen demand.
    """
    return (
        chemical_fertilizers_per_cropland_area()
        * average_share_of_industrial_agriculture()
        * (
            land_use_area_by_region().loc[:, "CROPLAND_RAINFED"].reset_coords(drop=True)
            + land_use_area_by_region()
            .loc[:, "CROPLAND_IRRIGATED"]
            .reset_coords(drop=True)
        )
    )


@component.add(
    name="from_industrial_to_low_input_agriculture",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_effect_oil_and_gas_on_agriculture_sp": 1,
        "time": 2,
        "year_initial_effect_of_oil_and_gas_on_agriculture_sp": 2,
        "year_final_effect_of_oil_and_gas_on_agriculture_sp": 2,
        "share_of_industrial_agriculture": 2,
        "objective_effect_of_oil_and_gas_on_agriculture_sp": 1,
        "initial_share_of_industrial_agriculture_r_and_i": 1,
    },
)
def from_industrial_to_low_input_agriculture():
    """
    EL OBJETIVO EXPRESADO COMO EL PORCENTAJE DE LA INDUSTRIAL EN EL AÑO INICIAL QUE YA NO ES VIABLE Y PASA A LOW INPUT OBJETIVO DEBE ESTAR ENTRE 0 Y 1
    """
    return if_then_else(
        np.logical_and(
            (switch_effect_oil_and_gas_on_agriculture_sp() == 1),
            np.logical_and(
                (time() > year_initial_effect_of_oil_and_gas_on_agriculture_sp()),
                np.logical_and(
                    (time() < year_final_effect_of_oil_and_gas_on_agriculture_sp()),
                    np.logical_and(
                        share_of_industrial_agriculture() > 0,
                        share_of_industrial_agriculture() < 1,
                    ),
                ),
            ),
        ),
        lambda: zidz(
            objective_effect_of_oil_and_gas_on_agriculture_sp()
            * initial_share_of_industrial_agriculture_r_and_i(),
            (
                year_final_effect_of_oil_and_gas_on_agriculture_sp()
                - year_initial_effect_of_oil_and_gas_on_agriculture_sp()
            ).expand_dims({"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"]}, 1),
        ),
        lambda: xr.DataArray(
            0,
            {
                "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
            },
            ["REGIONS_9_I", "LAND_PRODUCTS_I"],
        ),
    )


@component.add(
    name="from_industrial_to_regenerative_agriculture",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "change_to_regenerative_agriculture_sp": 1,
        "share_of_traditional_agriculture": 1,
        "share_of_industrial_agriculture": 2,
        "share_of_low_input_agriculture": 1,
    },
)
def from_industrial_to_regenerative_agriculture():
    return change_to_regenerative_agriculture_sp() * (
        share_of_industrial_agriculture()
        / (
            share_of_industrial_agriculture()
            + share_of_low_input_agriculture()
            + share_of_traditional_agriculture()
        )
    )


@component.add(
    name="from_low_input_to_regenerative_agriculture",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "change_to_regenerative_agriculture_sp": 1,
        "share_of_traditional_agriculture": 1,
        "share_of_industrial_agriculture": 1,
        "share_of_low_input_agriculture": 2,
    },
)
def from_low_input_to_regenerative_agriculture():
    return change_to_regenerative_agriculture_sp() * (
        share_of_low_input_agriculture()
        / (
            share_of_industrial_agriculture()
            + share_of_low_input_agriculture()
            + share_of_traditional_agriculture()
        )
    )


@component.add(
    name="from_traditional_to_industrial_agriculture_sp",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_industrial_agriculture_sp": 1,
        "time": 2,
        "year_initial_industrial_agriculture_sp": 2,
        "year_final_industrial_agriculture_sp": 2,
        "share_of_traditional_agriculture": 1,
        "objective_industrial_agriculture_sp": 1,
        "initial_share_of_traditional_agriculture": 1,
    },
)
def from_traditional_to_industrial_agriculture_sp():
    """
    IF_THEN_ELSE( SWITCH_INDUSTRIAL_AGRICULTURE_SP[REGIONS_9_I]=1 :AND:Time>YEAR_INITIAL_INDUSTRIAL_AGRICULTURE_SP[REGIONS_9_I] :AND:Time<YEAR_FINAL_INDUSTRIAL_AGRICULTURE_SP[REGIONS_9_I] :AND:share_of_traditional_agriculture[REGIONS_9_I] >=0 , (MAX(OBJECTIVE_INDUSTRIAL_AGRICULTURE_SP[REGIONS_9_I]-INITIAL_SHARE_OF_TRAD ITIONAL_AGRICULTURE[REGIONS_9_I],0))/(YEAR_FINAL_INDUSTRIAL_AGRICULTURE_SP[ REGIONS_9_I] -YEAR_INITIAL_INDUSTRIAL_AGRICULTURE_SP[REGIONS_9_I]) , 0 )
    """
    return if_then_else(
        np.logical_and(
            (switch_industrial_agriculture_sp() == 1),
            np.logical_and(
                (time() > year_initial_industrial_agriculture_sp()),
                np.logical_and(
                    (time() < year_final_industrial_agriculture_sp()),
                    share_of_traditional_agriculture() >= 0,
                ),
            ),
        ),
        lambda: np.maximum(
            objective_industrial_agriculture_sp()
            - initial_share_of_traditional_agriculture(),
            0,
        )
        / (
            year_final_industrial_agriculture_sp()
            - year_initial_industrial_agriculture_sp()
        ),
        lambda: xr.DataArray(
            0,
            {
                "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
            },
            ["REGIONS_9_I", "LAND_PRODUCTS_I"],
        ),
    )


@component.add(
    name="from_traditional_to_regenerative_agriculture",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "change_to_regenerative_agriculture_sp": 1,
        "share_of_traditional_agriculture": 2,
        "share_of_industrial_agriculture": 1,
        "share_of_low_input_agriculture": 1,
    },
)
def from_traditional_to_regenerative_agriculture():
    return change_to_regenerative_agriculture_sp() * (
        share_of_traditional_agriculture()
        / (
            share_of_industrial_agriculture()
            + share_of_low_input_agriculture()
            + share_of_traditional_agriculture()
        )
    )


@component.add(
    name="from_transition_to_regenerative_agriculture",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "share_of_agriculture_in_transition": 1,
        "time_of_transition_to_regenerative_agriculture": 1,
    },
)
def from_transition_to_regenerative_agriculture():
    return share_of_agriculture_in_transition() * (
        1 / time_of_transition_to_regenerative_agriculture()
    )


@component.add(
    name="historical_yields_of_crops_all_managements",
    units="t/(km2*Year)",
    subscripts=["LAND_PRODUCTS_I", "REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 2,
        "historical_crops_production_fao": 1,
        "historical_area_of_crops_all_management": 1,
    },
)
def historical_yields_of_crops_all_managements():
    return zidz(
        historical_crops_production_fao(time()),
        historical_area_of_crops_all_management(time()),
    )


@component.add(
    name="increase_of_yields_all_managements_trends",
    units="t/(km2*Year*Year)",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"trends_of_yield_change_r_and_i": 1},
)
def increase_of_yields_all_managements_trends():
    return trends_of_yield_change_r_and_i()


@component.add(
    name="increase_of_yields_industrial_R_and_I",
    units="t/(km2*Year*Year)",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "poli_yields": 1,
        "yields_industrial_crops_r_and_i": 2,
        "maximum_yields_r_and_i_industrial": 1,
        "aux_trends_of_yield_change_r_and_i": 2,
        "objective_yields": 1,
        "yields_all_management_2019": 1,
    },
)
def increase_of_yields_industrial_r_and_i():
    return if_then_else(
        poli_yields() == 0,
        lambda: if_then_else(
            yields_industrial_crops_r_and_i() < maximum_yields_r_and_i_industrial(),
            lambda: aux_trends_of_yield_change_r_and_i(),
            lambda: xr.DataArray(
                0,
                {
                    "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                    "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
                },
                ["REGIONS_9_I", "LAND_PRODUCTS_I"],
            ),
        ),
        lambda: if_then_else(
            yields_industrial_crops_r_and_i()
            < yields_all_management_2019() * (1 + objective_yields()),
            lambda: aux_trends_of_yield_change_r_and_i(),
            lambda: xr.DataArray(
                0,
                {
                    "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                    "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
                },
                ["REGIONS_9_I", "LAND_PRODUCTS_I"],
            ),
        ),
    )


@component.add(
    name="increase_of_yields_rainfed_industrial",
    units="t/(km2*Year*Year)",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "yields_rainfed_industrial": 1,
        "maximum_yields_rainfed_industrial": 1,
        "trends_of_industrial_rainfed_yields": 1,
    },
)
def increase_of_yields_rainfed_industrial():
    return if_then_else(
        yields_rainfed_industrial() < maximum_yields_rainfed_industrial(),
        lambda: trends_of_industrial_rainfed_yields(),
        lambda: xr.DataArray(
            0,
            {
                "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
            },
            ["REGIONS_9_I", "LAND_PRODUCTS_I"],
        ),
    )


@component.add(
    name="INITIAL_SHARE_OF_INDUSTRIAL_AGRICULTURE_R_AND_I",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "initial_share_of_low_input_agriculture": 1,
        "initial_share_of_regenerative_agriculture": 1,
        "initial_share_of_traditional_agriculture": 1,
    },
)
def initial_share_of_industrial_agriculture_r_and_i():
    return np.maximum(
        0,
        1
        - initial_share_of_low_input_agriculture()
        - initial_share_of_regenerative_agriculture()
        - initial_share_of_traditional_agriculture(),
    )


@component.add(
    name="INITIAL_YIELDS_OF_INDUSTRIAL_R_AND_I_CROPS",
    units="t/(km2*Year)",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "initial_yields_all_managements": 1,
        "effect_of_low_input_agriculture": 1,
        "initial_share_of_traditional_agriculture": 1,
        "initial_share_of_regenerative_agriculture": 1,
        "effect_of_regenerative_agriculture": 1,
        "initial_share_of_industrial_agriculture_r_and_i": 1,
    },
)
def initial_yields_of_industrial_r_and_i_crops():
    return initial_yields_all_managements() / (
        initial_share_of_industrial_agriculture_r_and_i()
        + initial_share_of_traditional_agriculture() * effect_of_low_input_agriculture()
        + initial_share_of_regenerative_agriculture()
        * effect_of_regenerative_agriculture()
    )


@component.add(
    name="initial_yields_of_industrial_rainfed_crops",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "initial_yields_all_managements": 1,
        "initial_share_of_irrigation": 1,
        "effect_of_low_input_agriculture": 1,
        "initial_share_of_traditional_agriculture": 1,
        "initial_time": 1,
        "effect_of_irrigation_of_yields_corrected": 1,
        "initial_share_of_regenerative_agriculture": 1,
        "effect_of_regenerative_agriculture": 1,
        "initial_share_of_industrial_agriculture_r_and_i": 1,
    },
)
def initial_yields_of_industrial_rainfed_crops():
    return initial_yields_all_managements() / (
        initial_share_of_industrial_agriculture_r_and_i()
        + (
            initial_share_of_irrigation(initial_time())
            * effect_of_irrigation_of_yields_corrected()
        ).transpose("REGIONS_9_I", "LAND_PRODUCTS_I")
        + initial_share_of_traditional_agriculture() * effect_of_low_input_agriculture()
        + initial_share_of_regenerative_agriculture()
        * effect_of_regenerative_agriculture()
    )


@component.add(
    name="land_products_available_all_managements_trends",
    units="t/Year",
    subscripts=["LAND_PRODUCTS_I", "REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "historical_area_of_crops_all_managements": 1,
        "yields_crops_all_mangements_trends": 1,
    },
)
def land_products_available_all_managements_trends():
    return (
        historical_area_of_crops_all_managements()
        * yields_crops_all_mangements_trends().transpose(
            "LAND_PRODUCTS_I", "REGIONS_9_I"
        )
    )


@component.add(
    name="number_elements_zones",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"zone_non_zero": 1},
)
def number_elements_zones():
    """
    number of elements of the matrix regions zones that have valid elements
    """
    return sum(
        zone_non_zero().rename({"CLIMATIC_ZONES_I": "CLIMATIC_ZONES_I!"}),
        dim=["CLIMATIC_ZONES_I!"],
    )


@component.add(
    name="percent_increase_of_yields_all_managements",
    units="DMNL",
    subscripts=["LAND_PRODUCTS_I", "REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "increase_of_yields_all_managements_trends": 1,
        "yields_crops_all_mangements_trends": 1,
    },
)
def percent_increase_of_yields_all_managements():
    return zidz(
        increase_of_yields_all_managements_trends(),
        yields_crops_all_mangements_trends(),
    ).transpose("LAND_PRODUCTS_I", "REGIONS_9_I")


@component.add(
    name="share_of_agriculture_in_transition",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_share_of_agriculture_in_transition": 1},
    other_deps={
        "_integ_share_of_agriculture_in_transition": {
            "initial": {},
            "step": {
                "from_industrial_to_regenerative_agriculture": 1,
                "from_low_input_to_regenerative_agriculture": 1,
                "from_traditional_to_regenerative_agriculture": 1,
                "from_transition_to_regenerative_agriculture": 1,
            },
        }
    },
)
def share_of_agriculture_in_transition():
    return _integ_share_of_agriculture_in_transition()


_integ_share_of_agriculture_in_transition = Integ(
    lambda: from_industrial_to_regenerative_agriculture()
    + from_low_input_to_regenerative_agriculture()
    + from_traditional_to_regenerative_agriculture()
    - from_transition_to_regenerative_agriculture(),
    lambda: xr.DataArray(
        0,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
        },
        ["REGIONS_9_I", "LAND_PRODUCTS_I"],
    ),
    "_integ_share_of_agriculture_in_transition",
)


@component.add(
    name="share_of_industrial_agriculture",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_share_of_industrial_agriculture": 1},
    other_deps={
        "_integ_share_of_industrial_agriculture": {
            "initial": {"initial_share_of_industrial_agriculture_r_and_i": 1},
            "step": {
                "from_traditional_to_industrial_agriculture_sp": 1,
                "from_industrial_to_regenerative_agriculture": 1,
                "from_industrial_to_low_input_agriculture": 1,
            },
        }
    },
)
def share_of_industrial_agriculture():
    return _integ_share_of_industrial_agriculture()


_integ_share_of_industrial_agriculture = Integ(
    lambda: from_traditional_to_industrial_agriculture_sp()
    - from_industrial_to_regenerative_agriculture()
    - from_industrial_to_low_input_agriculture(),
    lambda: initial_share_of_industrial_agriculture_r_and_i(),
    "_integ_share_of_industrial_agriculture",
)


@component.add(
    name="share_of_low_input_agriculture",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_share_of_low_input_agriculture": 1},
    other_deps={
        "_integ_share_of_low_input_agriculture": {
            "initial": {"initial_share_of_low_input_agriculture": 1},
            "step": {
                "from_industrial_to_low_input_agriculture": 1,
                "from_low_input_to_regenerative_agriculture": 1,
            },
        }
    },
)
def share_of_low_input_agriculture():
    return _integ_share_of_low_input_agriculture()


_integ_share_of_low_input_agriculture = Integ(
    lambda: from_industrial_to_low_input_agriculture()
    - from_low_input_to_regenerative_agriculture(),
    lambda: initial_share_of_low_input_agriculture(),
    "_integ_share_of_low_input_agriculture",
)


@component.add(
    name="share_of_regenerative_agriculture",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_share_of_regenerative_agriculture": 1},
    other_deps={
        "_integ_share_of_regenerative_agriculture": {
            "initial": {"initial_share_of_regenerative_agriculture": 1},
            "step": {"from_transition_to_regenerative_agriculture": 1},
        }
    },
)
def share_of_regenerative_agriculture():
    return _integ_share_of_regenerative_agriculture()


_integ_share_of_regenerative_agriculture = Integ(
    lambda: from_transition_to_regenerative_agriculture(),
    lambda: initial_share_of_regenerative_agriculture(),
    "_integ_share_of_regenerative_agriculture",
)


@component.add(
    name="share_of_traditional_agriculture",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_share_of_traditional_agriculture": 1},
    other_deps={
        "_integ_share_of_traditional_agriculture": {
            "initial": {"initial_share_of_traditional_agriculture": 1},
            "step": {
                "from_traditional_to_industrial_agriculture_sp": 1,
                "from_traditional_to_regenerative_agriculture": 1,
            },
        }
    },
)
def share_of_traditional_agriculture():
    return _integ_share_of_traditional_agriculture()


_integ_share_of_traditional_agriculture = Integ(
    lambda: -from_traditional_to_industrial_agriculture_sp()
    - from_traditional_to_regenerative_agriculture(),
    lambda: initial_share_of_traditional_agriculture(),
    "_integ_share_of_traditional_agriculture",
)


@component.add(
    name="sum_of_all_agriculture_share",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "share_of_agriculture_in_transition": 1,
        "share_of_industrial_agriculture": 1,
        "share_of_low_input_agriculture": 1,
        "share_of_regenerative_agriculture": 1,
        "share_of_traditional_agriculture": 1,
    },
)
def sum_of_all_agriculture_share():
    return (
        share_of_agriculture_in_transition()
        + share_of_industrial_agriculture()
        + share_of_low_input_agriculture()
        + share_of_regenerative_agriculture()
        + share_of_traditional_agriculture()
    )


@component.add(
    name="SWITCH_CLI2LAW_CC_EFFECTS",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_cli2law_cc_effects"},
)
def switch_cli2law_cc_effects():
    """
    if =0 not activated the effect of climate change on crop yields, 1= activated
    """
    return _ext_constant_switch_cli2law_cc_effects()


_ext_constant_switch_cli2law_cc_effects = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_CLI2LAW_CC_EFFECTS",
    {},
    _root,
    {},
    "_ext_constant_switch_cli2law_cc_effects",
)


@component.add(
    name="SWITCH_CLI2LAW_CC_FERTILIZATION",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_cli2law_cc_fertilization"},
)
def switch_cli2law_cc_fertilization():
    """
    =1 C fertilization activated, 0= no activated, it gives strage results when activated. It needs SWITCH_CLI2LAW_CC_EFFECTS=1 too.
    """
    return _ext_constant_switch_cli2law_cc_fertilization()


_ext_constant_switch_cli2law_cc_fertilization = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_CLI2LAW_CC_FERTILIZATION",
    {},
    _root,
    {},
    "_ext_constant_switch_cli2law_cc_fertilization",
)


@component.add(
    name="trends_of_industrial_rainfed_yields",
    units="t/(km2*Year*Year)",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "trends_of_yield_change_r_and_i": 1,
        "initial_share_of_irrigation": 1,
        "effect_of_low_input_agriculture": 1,
        "initial_share_of_traditional_agriculture": 1,
        "initial_time": 1,
        "effect_of_irrigation_of_yields_corrected": 1,
        "initial_share_of_regenerative_agriculture": 1,
        "effect_of_regenerative_agriculture": 1,
        "initial_share_of_industrial_agriculture_r_and_i": 1,
    },
)
def trends_of_industrial_rainfed_yields():
    return trends_of_yield_change_r_and_i() / (
        initial_share_of_industrial_agriculture_r_and_i()
        + (
            initial_share_of_irrigation(initial_time())
            * effect_of_irrigation_of_yields_corrected()
        ).transpose("REGIONS_9_I", "LAND_PRODUCTS_I")
        + initial_share_of_traditional_agriculture() * effect_of_low_input_agriculture()
        + initial_share_of_regenerative_agriculture()
        * effect_of_regenerative_agriculture()
    )


@component.add(
    name="yields_crops_all_mangements_trends",
    units="t/(km2*Year)",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_yields_crops_all_mangements_trends": 1},
    other_deps={
        "_integ_yields_crops_all_mangements_trends": {
            "initial": {"initial_time": 1, "historical_yields_fao": 1},
            "step": {"increase_of_yields_all_managements_trends": 1},
        }
    },
)
def yields_crops_all_mangements_trends():
    return _integ_yields_crops_all_mangements_trends()


_integ_yields_crops_all_mangements_trends = Integ(
    lambda: increase_of_yields_all_managements_trends(),
    lambda: historical_yields_fao(initial_time()).transpose(
        "REGIONS_9_I", "LAND_PRODUCTS_I"
    ),
    "_integ_yields_crops_all_mangements_trends",
)


@component.add(
    name="yields_FAO",
    units="t/(km2*Year)",
    subscripts=["LAND_PRODUCTS_I", "REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "historical_yields_fao": 1},
)
def yields_fao():
    return historical_yields_fao(time())


@component.add(
    name="yields_industrial_crops_R_and_I",
    units="t/(km2*Year)",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_yields_industrial_crops_r_and_i": 1},
    other_deps={
        "_integ_yields_industrial_crops_r_and_i": {
            "initial": {"initial_yields_of_industrial_r_and_i_crops": 1},
            "step": {"increase_of_yields_industrial_r_and_i": 1},
        }
    },
)
def yields_industrial_crops_r_and_i():
    return _integ_yields_industrial_crops_r_and_i()


_integ_yields_industrial_crops_r_and_i = Integ(
    lambda: increase_of_yields_industrial_r_and_i(),
    lambda: initial_yields_of_industrial_r_and_i_crops(),
    "_integ_yields_industrial_crops_r_and_i",
)


@component.add(
    name="yields_of_crops_all_managements",
    units="t/(km2*Year)",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "time_historical_data_land_module": 1,
        "yields_fao": 1,
        "effect_of_management_on_crops": 1,
        "yields_industrial_crops_r_and_i": 1,
        "effect_of_climate_change_on_yields": 1,
    },
)
def yields_of_crops_all_managements():
    return if_then_else(
        time() < time_historical_data_land_module(),
        lambda: yields_fao(),
        lambda: (
            yields_industrial_crops_r_and_i()
            * effect_of_management_on_crops()
            * effect_of_climate_change_on_yields()
        ).transpose("LAND_PRODUCTS_I", "REGIONS_9_I"),
    ).transpose("REGIONS_9_I", "LAND_PRODUCTS_I")


@component.add(
    name="yields_of_irrigated_crops",
    units="t/(km2*Year)",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "yields_rainfed_industrial": 1,
        "effect_of_irrigation_of_yields_corrected": 1,
        "effect_of_management_on_crops": 1,
    },
)
def yields_of_irrigated_crops():
    """
    yields of irrigated crops
    """
    return (
        yields_rainfed_industrial()
        * effect_of_irrigation_of_yields_corrected().transpose(
            "REGIONS_9_I", "LAND_PRODUCTS_I"
        )
        * effect_of_management_on_crops()
    )


@component.add(
    name="yields_of_rainfed_crops",
    units="t/(km2*Year)",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"yields_rainfed_industrial": 1, "effect_of_management_on_crops": 1},
)
def yields_of_rainfed_crops():
    """
    yields of rainfed crops
    """
    return yields_rainfed_industrial() * effect_of_management_on_crops()


@component.add(
    name="yields_rainfed_industrial",
    units="t/(km2*Year)",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_yields_rainfed_industrial": 1},
    other_deps={
        "_integ_yields_rainfed_industrial": {
            "initial": {"initial_yields_of_industrial_rainfed_crops": 1},
            "step": {"increase_of_yields_rainfed_industrial": 1},
        }
    },
)
def yields_rainfed_industrial():
    return _integ_yields_rainfed_industrial()


_integ_yields_rainfed_industrial = Integ(
    lambda: increase_of_yields_rainfed_industrial(),
    lambda: initial_yields_of_industrial_rainfed_crops(),
    "_integ_yields_rainfed_industrial",
)


@component.add(
    name="zone_non_zero",
    subscripts=["REGIONS_9_I", "CLIMATIC_ZONES_I", "LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_of_cc_yields_zone_region": 1},
)
def zone_non_zero():
    """
    Is used to cound the number of climatic zones with value non 0
    """
    return if_then_else(
        matrix_of_cc_yields_zone_region() == 0,
        lambda: xr.DataArray(
            0,
            {
                "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                "CLIMATIC_ZONES_I": _subscript_dict["CLIMATIC_ZONES_I"],
                "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
            },
            ["REGIONS_9_I", "CLIMATIC_ZONES_I", "LAND_PRODUCTS_I"],
        ),
        lambda: xr.DataArray(
            1,
            {
                "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                "CLIMATIC_ZONES_I": _subscript_dict["CLIMATIC_ZONES_I"],
                "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
            },
            ["REGIONS_9_I", "CLIMATIC_ZONES_I", "LAND_PRODUCTS_I"],
        ),
    )
