"""
Module land_and_water.land.ghg_emissions_agriculture
Translated using PySD version 3.10.0
"""


@component.add(
    name="ANIMALS_DISTRIBUTION_REGIONS",
    units="number_animals",
    subscripts=["REGIONS_9_I", "ANIMALS_TYPES_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_animals_distribution_regions"},
)
def animals_distribution_regions():
    """
    Distribution of number of "world" animals among the 9 regions. Excel file: animals_stock_byregion_2
    """
    return _ext_constant_animals_distribution_regions()


_ext_constant_animals_distribution_regions = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "ANIMALS_DISTRIBUTION_REGIONS",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "ANIMALS_TYPES_I": _subscript_dict["ANIMALS_TYPES_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "ANIMALS_TYPES_I": _subscript_dict["ANIMALS_TYPES_I"],
    },
    "_ext_constant_animals_distribution_regions",
)


@component.add(
    name="animals_producing",
    units="number_animals",
    subscripts=["ANIMALS_TYPES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "production_from_animals": 10,
        "dairy_milk_cattle_distribution": 1,
        "yield_of_cattle_milk": 1,
        "meat_ruminant_cattle_distribution": 1,
        "yield_of_meat_cattle": 1,
        "yield_of_buffalo_milk": 1,
        "yield_of_meat_buffalo": 1,
        "dairy_milk_buffalo_distribution": 1,
        "meat_ruminant_buffalo_distribution": 1,
        "dairy_milk_goats_distribution": 1,
        "yield_of_goats_milk": 1,
        "yield_of_meat_goat": 1,
        "meat_ruminant_goat_distribution": 1,
        "meat_ruminant_sheep_distribution": 1,
        "yield_of_sheep_milk": 1,
        "yield_of_meat_sheep": 1,
        "dairy_milk_sheep_distribution": 1,
        "yield_of_meat_chickens": 1,
        "meat_monogastric_chickens_distribution": 1,
        "meat_monogastric_swine_distribution": 1,
        "yield_of_meat_pig": 1,
    },
)
def animals_producing():
    """
    Number of animals producting from main CH4 and N2O emmiters (Cattle, buffalo, sheep, chickens, goat, and swine) **NOTES:todo: ideallly livestock yiekld should change in time (now it is an average of past years)
    """
    value = xr.DataArray(
        np.nan,
        {"ANIMALS_TYPES_I": _subscript_dict["ANIMALS_TYPES_I"]},
        ["ANIMALS_TYPES_I"],
    )
    value.loc[["DAIRY_CATTLE"]] = (
        float(production_from_animals().loc["DAIRY"])
        * dairy_milk_cattle_distribution()
        * (1 / yield_of_cattle_milk())
    )
    value.loc[["OTHER_CATTLE"]] = (
        float(production_from_animals().loc["MEAT_RUMINANTS"])
        * meat_ruminant_cattle_distribution()
        * (1 / yield_of_meat_cattle())
    )
    value.loc[["BUFFALO"]] = float(
        production_from_animals().loc["DAIRY"]
    ) * dairy_milk_buffalo_distribution() * (1 / yield_of_buffalo_milk()) + float(
        production_from_animals().loc["MEAT_RUMINANTS"]
    ) * meat_ruminant_buffalo_distribution() * (
        1 / yield_of_meat_buffalo()
    )
    value.loc[["GOAT"]] = float(
        production_from_animals().loc["DAIRY"]
    ) * dairy_milk_goats_distribution() * (1 / yield_of_goats_milk()) + float(
        production_from_animals().loc["MEAT_RUMINANTS"]
    ) * meat_ruminant_goat_distribution() * (
        1 / yield_of_meat_goat()
    )
    value.loc[["SHEEP"]] = float(
        production_from_animals().loc["DAIRY"]
    ) * dairy_milk_sheep_distribution() * (1 / yield_of_sheep_milk()) + float(
        production_from_animals().loc["MEAT_RUMINANTS"]
    ) * meat_ruminant_sheep_distribution() * (
        1 / yield_of_meat_sheep()
    )
    value.loc[["CHICKENS"]] = (
        float(production_from_animals().loc["MEAT_MONOGASTRIC"])
        * meat_monogastric_chickens_distribution()
        * (1 / yield_of_meat_chickens())
    )
    value.loc[["SWINE"]] = (
        float(production_from_animals().loc["MEAT_MONOGASTRIC"])
        * meat_monogastric_swine_distribution()
        * (1 / yield_of_meat_pig())
    )
    return value


@component.add(
    name="area_of_irrigated_rice",
    units="km2",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_law_emissions_irrigated_crop_area": 1,
        "switch_law_emissions": 1,
        "exo_area_irrigated_rice_t": 1,
        "area_of_irrigated_crops": 1,
    },
)
def area_of_irrigated_rice():
    """
    Area of rice with water regime irrigated
    """
    return if_then_else(
        np.logical_or(
            switch_law_emissions_irrigated_crop_area() == 0, switch_law_emissions() == 0
        ),
        lambda: exo_area_irrigated_rice_t(),
        lambda: area_of_irrigated_crops().loc[:, "RICE"].reset_coords(drop=True),
    )


@component.add(
    name="area_of_rainfed_rice",
    units="km2",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_law_emissions_irrigated_crop_area": 1,
        "switch_law_emissions": 1,
        "exo_area_rainfed_rice_t": 1,
        "area_of_rainfed_crops": 1,
    },
)
def area_of_rainfed_rice():
    """
    Area of rice with water regime rainfed
    """
    return if_then_else(
        np.logical_or(
            switch_law_emissions_irrigated_crop_area() == 0, switch_law_emissions() == 0
        ),
        lambda: exo_area_rainfed_rice_t(),
        lambda: area_of_rainfed_crops().loc[:, "RICE"].reset_coords(drop=True),
    )


@component.add(
    name="area_of_rice",
    units="km2",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"area_of_rainfed_rice": 1, "area_of_irrigated_rice": 1},
)
def area_of_rice():
    """
    Area of rice total
    """
    return area_of_rainfed_rice() + area_of_irrigated_rice()


@component.add(
    name="area_of_rice_world",
    units="km2",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"area_of_rice": 1},
)
def area_of_rice_world():
    """
    Area of rice total world
    """
    return sum(
        area_of_rice().rename({"REGIONS_9_I": "REGIONS_9_I!"}), dim=["REGIONS_9_I!"]
    )


@component.add(
    name="BUFFALO_EMISSION_SECOND_FACTOR_METHANE_MANURE_MANAGEMENT",
    units="kg/(number_animals*Year)",
    subscripts=["REGIONS_9_I", "MANURE_MANAGEMENT_SYSTEM_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_livestock_manure_management_sp": 1,
        "time": 2,
        "year_initial_manure_management_system_sp": 1,
        "year_final_manure_management_system_sp": 1,
        "objetive_buffalo_manure_system_sp": 1,
        "methane_conversion_factor_by_system": 2,
        "buffalo_manure_system": 1,
    },
)
def buffalo_emission_second_factor_methane_manure_management():
    """
    IPCC 2006 Guidelines (Tier 1) (Eggleston, Buendia, Miwa, Ngara, & Tanabe, 2006) tABLES 10.14 TO 10.16 Adapted to WILIAM regions. Not used the ones of "goat", sheep and chkens, as this factor is to be applied to the rest in which policies about manure system can be applied. If the policies about manure management are activited then the estimation are based on the new manure system defined by the policy. If not, the values by defaul (manure management systems according to each region of WILIAM) are considered. This is based in 2006 IPCC guidelines , but adaptated to WILIAM regions
    """
    return if_then_else(
        np.logical_and(
            switch_livestock_manure_management_sp() == 1,
            np.logical_and(
                time() > year_initial_manure_management_system_sp(),
                time() <= year_final_manure_management_system_sp(),
            ),
        ).expand_dims(
            {
                "MANURE_MANAGEMENT_SYSTEM_I": _subscript_dict[
                    "MANURE_MANAGEMENT_SYSTEM_I"
                ]
            },
            1,
        ),
        lambda: methane_conversion_factor_by_system()
        * objetive_buffalo_manure_system_sp(),
        lambda: methane_conversion_factor_by_system() * buffalo_manure_system(),
    )


@component.add(
    name="BUFFALO_MANURE_SYSTEM",
    units="DMNL",
    subscripts=["REGIONS_9_I", "MANURE_MANAGEMENT_SYSTEM_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_buffalo_manure_system"},
)
def buffalo_manure_system():
    """
    % MS by default. The "less emissions" options are: solid storage, dry lot, range/paddock, daily spread and Pit storage <1month From IPCC 2006 Chapter livestock, adapted to WILIAM regions % of the types manure systems by type of animal , for the calculation of methane emissions due to manure management . These are the ones currently applied in WILIAM regions obtained in IPCC 2006 adapted to WILIAM
    """
    return _ext_constant_buffalo_manure_system()


_ext_constant_buffalo_manure_system = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "BUFFALO_MANURE_SYSTEM",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "MANURE_MANAGEMENT_SYSTEM_I": _subscript_dict["MANURE_MANAGEMENT_SYSTEM_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "MANURE_MANAGEMENT_SYSTEM_I": _subscript_dict["MANURE_MANAGEMENT_SYSTEM_I"],
    },
    "_ext_constant_buffalo_manure_system",
)


@component.add(
    name="CH4_emissions_agriculture",
    units="Mt/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ch4_emissions_livestock": 1, "ch4_emissions_rice": 1},
)
def ch4_emissions_agriculture():
    """
    Total CH4 emissions from agricultur BY region. Important note: the emissions calculated in this variable from agriculture are ONLY those related to "Enteric fermentation", "Manure management", "Rice cultivation" , and "Synthetic Fertilizers. The rest of agriculture emissions are not included in this variable such as crop residues, burning of crop residues, manure left on pasture, manure applied to soils, or energy use in agriculture.
    """
    return ch4_emissions_livestock() + ch4_emissions_rice()


@component.add(
    name="CH4_emissions_enteric_fermentation",
    units="Mt/Year",
    subscripts=["REGIONS_9_I", "ANIMALS_TYPES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "factor_emissions_enteric_fermentation": 1,
        "number_animals_by_region": 1,
        "unit_conversion_t_kg": 1,
        "unit_conversion_mt_t": 1,
    },
)
def ch4_emissions_enteric_fermentation():
    """
    Equation for CH4 emissiones based on activity data (animals) and factor emissions (from IPCC)
    """
    return (
        factor_emissions_enteric_fermentation()
        * number_animals_by_region()
        * (unit_conversion_mt_t() * unit_conversion_t_kg())
    )


@component.add(
    name="CH4_emissions_enteric_fermentation_by_region",
    units="MtCH4/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "ch4_emissions_enteric_fermentation": 1,
        "share_rest_ch4_enteric_fermentation_emissions": 1,
    },
)
def ch4_emissions_enteric_fermentation_by_region():
    """
    Equation for CH4 emissions based on activity data (animals) and factor emissions (from IPCC),
    """
    return sum(
        ch4_emissions_enteric_fermentation().rename(
            {"ANIMALS_TYPES_I": "ANIMALS_TYPES_I!"}
        ),
        dim=["ANIMALS_TYPES_I!"],
    ) * (1 + share_rest_ch4_enteric_fermentation_emissions())


@component.add(
    name="CH4_emissions_enteric_fermentation_byanimal",
    units="Mt/Year",
    subscripts=["ANIMALS_TYPES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ch4_emissions_enteric_fermentation": 1},
)
def ch4_emissions_enteric_fermentation_byanimal():
    """
    ch4 emissions from enteric fermentation by type of animal at world scale
    """
    return sum(
        ch4_emissions_enteric_fermentation().rename({"REGIONS_9_I": "REGIONS_9_I!"}),
        dim=["REGIONS_9_I!"],
    )


@component.add(
    name="CH4_emissions_enteric_fermentation_total",
    units="Mt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ch4_emissions_enteric_fermentation_by_region": 1},
)
def ch4_emissions_enteric_fermentation_total():
    """
    ch4 emissions from enteric fermentation at world scale
    """
    return sum(
        ch4_emissions_enteric_fermentation_by_region().rename(
            {"REGIONS_9_I": "REGIONS_9_I!"}
        ),
        dim=["REGIONS_9_I!"],
    )


@component.add(
    name="CH4_emissions_livestock",
    units="MtCH4/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "ch4_emissions_enteric_fermentation_by_region": 1,
        "ch4_emissions_manure_management_by_region": 1,
    },
)
def ch4_emissions_livestock():
    """
    CH4 livestock emissions due to manure management.
    """
    return (
        ch4_emissions_enteric_fermentation_by_region()
        + ch4_emissions_manure_management_by_region()
    )


@component.add(
    name="CH4_emissions_manure_management",
    units="MtCH4/Year",
    subscripts=["REGIONS_9_I", "ANIMALS_TYPES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "number_animals_by_region": 1,
        "emission_factor_methane_manure_management_calculated": 1,
        "unit_conversion_t_kg": 1,
        "unit_conversion_mt_t": 1,
    },
)
def ch4_emissions_manure_management():
    """
    Equation for CH4 emissions based on activity data (animals) and factor emissions (from IPCC),
    """
    return (
        number_animals_by_region()
        * emission_factor_methane_manure_management_calculated()
        * unit_conversion_t_kg()
        * unit_conversion_mt_t()
    )


@component.add(
    name="CH4_emissions_manure_management_by_region",
    units="MtCH4/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "ch4_emissions_manure_management": 1,
        "share_rest_ch4_manure_management_emissions": 1,
    },
)
def ch4_emissions_manure_management_by_region():
    """
    Equation for CH4 emissions based on activity data (animals) and factor emissions (from IPCC),
    """
    return sum(
        ch4_emissions_manure_management().rename(
            {"ANIMALS_TYPES_I": "ANIMALS_TYPES_I!"}
        ),
        dim=["ANIMALS_TYPES_I!"],
    ) * (1 + share_rest_ch4_manure_management_emissions())


@component.add(
    name="CH4_emissions_manure_management_byanimal",
    units="MtCH4/Year",
    subscripts=["ANIMALS_TYPES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ch4_emissions_manure_management": 1},
)
def ch4_emissions_manure_management_byanimal():
    """
    Equation for CH4 emissions based on activity data (animals) and factor emissions (from IPCC),-->***STILL to be checked the subscripts (depending on LEO data and exogenous input)
    """
    return sum(
        ch4_emissions_manure_management().rename({"REGIONS_9_I": "REGIONS_9_I!"}),
        dim=["REGIONS_9_I!"],
    )


@component.add(
    name="CH4_emissions_manure_management_total",
    units="MtCH4/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ch4_emissions_manure_management_by_region": 1},
)
def ch4_emissions_manure_management_total():
    """
    Equation for CH4 emissions based on activity data (animals) and factor emissions (from IPCC),
    """
    return sum(
        ch4_emissions_manure_management_by_region().rename(
            {"REGIONS_9_I": "REGIONS_9_I!"}
        ),
        dim=["REGIONS_9_I!"],
    )


@component.add(
    name="CH4_emissions_rice",
    units="Mt/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "area_of_irrigated_rice": 1,
        "scaling_factor_organic_amendment": 2,
        "unit_conversion_km2_ha": 2,
        "unit_conversion_mt_t": 2,
        "scaling_factor_water_regime_rice_irrigated": 1,
        "cultivation_period_rice": 2,
        "factor_emissions_baseline_rice": 2,
        "unit_conversion_t_kg": 2,
        "scaling_factor_water_regime_preseason": 2,
        "share_upland_rice_by_region": 1,
        "area_of_rainfed_rice": 1,
        "scaling_factor_water_regime_rice_rainfed": 1,
    },
)
def ch4_emissions_rice():
    """
    CH4 emissions in paddy fields. Based on IPCC 2006 default values (Tier 1, Chapter 5). Upland has a scaling factor of 0 --> Notes for calibration (future): 1º--> ajustar con los datos de 1997 de upland (especialmente para la region de INDIA, LATAM, USMCA, y LROW)--> no todo es Rainfed (e esos casos las emisiones son 0 porque el factor de water-regime es 0) --- emissions are ajusted well (at the moment) when the Scaling factor of water regime for rainfed is 0 (considering instead of rainfed, as "upland", i., fields are never flooded for a significant period of time), but this could be related with the percentages of rainfed and irrigated area (check this with Marga, including the meaning of "rice" in "rainfed"). ---Also these emissions are better adjusted considering a scaling factor "for water regimes before the cultivation period" of ( this correspondes to "non flooded preseason". ---In case nothing works, the EFs would be adjusted to historical information as some important details are missed in this "aggreagated" activity coming from land uses....
    """
    return area_of_irrigated_rice() * (
        (factor_emissions_baseline_rice() * cultivation_period_rice())
        * scaling_factor_water_regime_rice_irrigated()
        * scaling_factor_water_regime_preseason()
        * scaling_factor_organic_amendment()
        * unit_conversion_t_kg()
        * unit_conversion_mt_t()
        * (1 / unit_conversion_km2_ha())
    ) + area_of_rainfed_rice() * (
        (factor_emissions_baseline_rice() * cultivation_period_rice())
        * scaling_factor_water_regime_rice_rainfed()
        * (1 - share_upland_rice_by_region())
        * scaling_factor_organic_amendment()
        * unit_conversion_t_kg()
        * scaling_factor_water_regime_preseason()
        * unit_conversion_mt_t()
        * (1 / unit_conversion_km2_ha())
    )


@component.add(
    name="CH4_emissions_rice_world",
    units="MtCH4/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ch4_emissions_rice": 1},
)
def ch4_emissions_rice_world():
    """
    historic rice emissions WORLD
    """
    return sum(
        ch4_emissions_rice().rename({"REGIONS_9_I": "REGIONS_9_I!"}),
        dim=["REGIONS_9_I!"],
    )


@component.add(
    name="CO2_EMISSIONS_CROP_ORGANIC_EXOGENOUS",
    units="ha",
    comp_type="Constant",
    comp_subtype="Normal",
)
def co2_emissions_crop_organic_exogenous():
    """
    POTENTIALY TO BE ELIMINATED: Exogenous Historic data of CO2 emissions of organic soils (depending of the area of organic soil that it is cropland) -->from now exogenous, as we cannot determine in any module this OLD COMMENTS:Noelia Comment: maybe this two in red could be removed, if we cannot determine well the "percentag_organic_soils_" which should be "variable", and in principle, it is not going to be calculated in any View Factor activity was the area of cropland in organic soil multiplied by the emission factor--> IPCC 2006 Guidlines Table 5.6 default values by climate (warm, tropical, boreal...)
    """
    return 0


@component.add(
    name="CO2_EMISSIONS_GRASSLAND_ORGANIC_EXOGENOUS",
    units="ha",
    comp_type="Constant",
    comp_subtype="Normal",
)
def co2_emissions_grassland_organic_exogenous():
    """
    POTENTIALY TO BE ELIMINATED:Exogenous Historic data of CO2 emissions of organic soils (depending of the area of organic soil that it is GRASSland) -->from now exogenous, as we cannot determine in any module this OLD COMMENTS:Noelia Comment: maybe this two in red could be removed, if we cannot determine well the "percentag_organic_soils_" which should be "variable", and in principle, it is not going to be calculated in any View
    """
    return 0


@component.add(
    name="CULTIVATION_PERIOD_RICE",
    units="days/Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_cultivation_period_rice"},
)
def cultivation_period_rice():
    """
    cultivation period! (120 days?)--> https://www.fao.org/3/s2022e/s2022e02.htm (total grown period:Rice 90-150) (average value)
    """
    return _ext_constant_cultivation_period_rice()


_ext_constant_cultivation_period_rice = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "CULTIVATION_PERIOD_RICE",
    {},
    _root,
    {},
    "_ext_constant_cultivation_period_rice",
)


@component.add(
    name="DAIRY_CATLLE_EMISSION_SECOND_FACTOR_METHANE_MANURE_MANAGEMENT",
    units="kg/(number_animals*Year)",
    subscripts=["REGIONS_9_I", "MANURE_MANAGEMENT_SYSTEM_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_livestock_manure_management_sp": 1,
        "time": 2,
        "year_initial_manure_management_system_sp": 1,
        "year_final_manure_management_system_sp": 1,
        "objetive_dairy_cattle_manure_system_sp": 1,
        "methane_conversion_factor_by_system": 2,
        "dairy_cattle_manure_system": 1,
    },
)
def dairy_catlle_emission_second_factor_methane_manure_management():
    """
    IPCC 2006 Guidelines (Tier 1) (Eggleston, Buendia, Miwa, Ngara, & Tanabe, 2006) tABLES 10.14 TO 10.16 Adapted to WILIAM regions. Not used the ones of "goat", sheep and chkens, as this factor is to be applied to the rest in which policies about manure system can be applied. If the policies about manure management are activited then the estimation are based on the new manure system defined by the policy. If not, the values by defaul (manure management systems according to each region of WILIAM) are considered. This is based in 2006 IPCC guidelines , but adaptated to WILIAM regions
    """
    return if_then_else(
        np.logical_and(
            switch_livestock_manure_management_sp() == 1,
            np.logical_and(
                time() > year_initial_manure_management_system_sp(),
                time() <= year_final_manure_management_system_sp(),
            ),
        ).expand_dims(
            {
                "MANURE_MANAGEMENT_SYSTEM_I": _subscript_dict[
                    "MANURE_MANAGEMENT_SYSTEM_I"
                ]
            },
            1,
        ),
        lambda: methane_conversion_factor_by_system()
        * objetive_dairy_cattle_manure_system_sp(),
        lambda: methane_conversion_factor_by_system() * dairy_cattle_manure_system(),
    )


@component.add(
    name="DAIRY_CATTLE_MANURE_SYSTEM",
    units="DMNL",
    subscripts=["REGIONS_9_I", "MANURE_MANAGEMENT_SYSTEM_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_dairy_cattle_manure_system"},
)
def dairy_cattle_manure_system():
    """
    % MS by default. The "less emissions" options are: solid storage, dry lot, range/paddock, daily spread and Pit storage <1month From IPCC 2006 Chapter livestock, adapted to WILIAM regions % of the types manure systems by type of animal , for the calculation of methane emissions due to manure management . These are the ones currently applied in WILIAM regions obtained in IPCC 2006 adapted to WILIAM
    """
    return _ext_constant_dairy_cattle_manure_system()


_ext_constant_dairy_cattle_manure_system = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "DAIRY_CATTLE_MANURE_SYSTEM",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "MANURE_MANAGEMENT_SYSTEM_I": _subscript_dict["MANURE_MANAGEMENT_SYSTEM_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "MANURE_MANAGEMENT_SYSTEM_I": _subscript_dict["MANURE_MANAGEMENT_SYSTEM_I"],
    },
    "_ext_constant_dairy_cattle_manure_system",
)


@component.add(
    name="DAIRY_MILK_BUFFALO_DISTRIBUTION",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_dairy_milk_buffalo_distribution"},
)
def dairy_milk_buffalo_distribution():
    """
    SHARE PRODUCTION ANIMALS (share of production that corresponds to an specific type of animal) Excel file: "Animals_number_prodcution_WORLD_clean"
    """
    return _ext_constant_dairy_milk_buffalo_distribution()


_ext_constant_dairy_milk_buffalo_distribution = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "DAIRY_MILK_BUFFALO_DISTRIBUTION",
    {},
    _root,
    {},
    "_ext_constant_dairy_milk_buffalo_distribution",
)


@component.add(
    name="DAIRY_MILK_CATTLE_DISTRIBUTION",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_dairy_milk_cattle_distribution"},
)
def dairy_milk_cattle_distribution():
    """
    SHARE PRODUCTION ANIMALS (share of production that corresponds to an specific type of animal) Excel file: "Animals_number_prodcution_WORLD_clean"
    """
    return _ext_constant_dairy_milk_cattle_distribution()


_ext_constant_dairy_milk_cattle_distribution = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "DAIRY_MILK_CATTLE_DISTRIBUTION",
    {},
    _root,
    {},
    "_ext_constant_dairy_milk_cattle_distribution",
)


@component.add(
    name="DAIRY_MILK_GOATS_DISTRIBUTION",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_dairy_milk_goats_distribution"},
)
def dairy_milk_goats_distribution():
    """
    SHARE PRODUCTION ANIMALS (share of production that corresponds to an specific type of animal) Excel file: "Animals_number_prodcution_WORLD_clean"
    """
    return _ext_constant_dairy_milk_goats_distribution()


_ext_constant_dairy_milk_goats_distribution = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "DAIRY_MILK_GOATS_DISTRIBUTION",
    {},
    _root,
    {},
    "_ext_constant_dairy_milk_goats_distribution",
)


@component.add(
    name="DAIRY_MILK_SHEEP_DISTRIBUTION",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_dairy_milk_sheep_distribution"},
)
def dairy_milk_sheep_distribution():
    """
    SHARE PRODUCTION ANIMALS (share of production that corresponds to an specific type of animal) Excel file: "Animals_number_prodcution_WORLD_clean"
    """
    return _ext_constant_dairy_milk_sheep_distribution()


_ext_constant_dairy_milk_sheep_distribution = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "DAIRY_MILK_SHEEP_DISTRIBUTION",
    {},
    _root,
    {},
    "_ext_constant_dairy_milk_sheep_distribution",
)


@component.add(
    name="EMISSION_FACTOR_METHANE_MANURE_MANAGEMENT_BY_DEFAULT",
    units="kg/(number_animals*Year)",
    subscripts=["REGIONS_9_I", "ANIMALS_TYPES_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_emission_factor_methane_manure_management_by_default"
    },
)
def emission_factor_methane_manure_management_by_default():
    """
    IPCC 2006 Guidelines (Tier 1) (Eggleston, Buendia, Miwa, Ngara, & Tanabe, 2006) tABLES 10.14 TO 10.16 Adapted to WILIAM regions. Only used the ones of "goat", sheep and chkens, the rest are obtained by manure system to be able to apply another policies or manure management systems
    """
    return _ext_constant_emission_factor_methane_manure_management_by_default()


_ext_constant_emission_factor_methane_manure_management_by_default = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "EMISSION_FACTOR_METHANE_MANURE_MANAGEMENT_BY_DEFAULT",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "ANIMALS_TYPES_I": _subscript_dict["ANIMALS_TYPES_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "ANIMALS_TYPES_I": _subscript_dict["ANIMALS_TYPES_I"],
    },
    "_ext_constant_emission_factor_methane_manure_management_by_default",
)


@component.add(
    name="EMISSION_FACTOR_METHANE_MANURE_MANAGEMENT_CALCULATED",
    units="kg/(number_animals*Year)",
    subscripts=["REGIONS_9_I", "ANIMALS_TYPES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_model_explorer": 4,
        "emission_first_factor_methane_manure_management": 8,
        "model_explorer_manure_management_system": 4,
        "dairy_catlle_emission_second_factor_methane_manure_management": 1,
        "other_catlle_emission_second_factor_methane_manure_management": 1,
        "buffalo_emission_second_factor_methane_manure_management": 1,
        "emission_factor_methane_manure_management_by_default": 3,
        "swine_emission_second_factor_methane_manure_management": 1,
    },
)
def emission_factor_methane_manure_management_calculated():
    """
    IPCC 2006 Guidelines (Tier 1) (Eggleston, Buendia, Miwa, Ngara, & Tanabe, 2006) tABLES 10.14 TO 10.16 Adapted to WILIAM regions. Only used the ones of "goat", sheep and chkens, the rest are obtained by manure system to be able to apply another policies or manure management systems
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "ANIMALS_TYPES_I": _subscript_dict["ANIMALS_TYPES_I"],
        },
        ["REGIONS_9_I", "ANIMALS_TYPES_I"],
    )
    value.loc[:, ["DAIRY_CATTLE"]] = (
        if_then_else(
            switch_model_explorer() == 1,
            lambda: emission_first_factor_methane_manure_management()
            .loc[:, "DAIRY_CATTLE"]
            .reset_coords(drop=True)
            * sum(
                model_explorer_manure_management_system()
                .loc["DAIRY_CATTLE", :, :]
                .reset_coords(drop=True)
                .rename({"MANURE_MANAGEMENT_SYSTEM_I": "MANURE_MANAGEMENT_SYSTEM_I!"}),
                dim=["MANURE_MANAGEMENT_SYSTEM_I!"],
            ),
            lambda: emission_first_factor_methane_manure_management()
            .loc[:, "DAIRY_CATTLE"]
            .reset_coords(drop=True)
            * sum(
                dairy_catlle_emission_second_factor_methane_manure_management().rename(
                    {"MANURE_MANAGEMENT_SYSTEM_I": "MANURE_MANAGEMENT_SYSTEM_I!"}
                ),
                dim=["MANURE_MANAGEMENT_SYSTEM_I!"],
            ),
        )
        .expand_dims({"ANIMALS_TYPES_I": ["DAIRY_CATTLE"]}, 1)
        .values
    )
    value.loc[:, ["OTHER_CATTLE"]] = (
        if_then_else(
            switch_model_explorer() == 1,
            lambda: emission_first_factor_methane_manure_management()
            .loc[:, "OTHER_CATTLE"]
            .reset_coords(drop=True)
            * sum(
                model_explorer_manure_management_system()
                .loc["OTHER_CATTLE", :, :]
                .reset_coords(drop=True)
                .rename({"MANURE_MANAGEMENT_SYSTEM_I": "MANURE_MANAGEMENT_SYSTEM_I!"}),
                dim=["MANURE_MANAGEMENT_SYSTEM_I!"],
            ),
            lambda: emission_first_factor_methane_manure_management()
            .loc[:, "OTHER_CATTLE"]
            .reset_coords(drop=True)
            * sum(
                other_catlle_emission_second_factor_methane_manure_management().rename(
                    {"MANURE_MANAGEMENT_SYSTEM_I": "MANURE_MANAGEMENT_SYSTEM_I!"}
                ),
                dim=["MANURE_MANAGEMENT_SYSTEM_I!"],
            ),
        )
        .expand_dims({"ANIMALS_TYPES_I": ["OTHER_CATTLE"]}, 1)
        .values
    )
    value.loc[:, ["BUFFALO"]] = (
        if_then_else(
            switch_model_explorer() == 1,
            lambda: emission_first_factor_methane_manure_management()
            .loc[:, "BUFFALO"]
            .reset_coords(drop=True)
            * sum(
                model_explorer_manure_management_system()
                .loc["BUFFALO", :, :]
                .reset_coords(drop=True)
                .rename({"MANURE_MANAGEMENT_SYSTEM_I": "MANURE_MANAGEMENT_SYSTEM_I!"}),
                dim=["MANURE_MANAGEMENT_SYSTEM_I!"],
            ),
            lambda: emission_first_factor_methane_manure_management()
            .loc[:, "BUFFALO"]
            .reset_coords(drop=True)
            * sum(
                buffalo_emission_second_factor_methane_manure_management().rename(
                    {"MANURE_MANAGEMENT_SYSTEM_I": "MANURE_MANAGEMENT_SYSTEM_I!"}
                ),
                dim=["MANURE_MANAGEMENT_SYSTEM_I!"],
            ),
        )
        .expand_dims({"ANIMALS_TYPES_I": ["BUFFALO"]}, 1)
        .values
    )
    value.loc[:, ["GOAT"]] = (
        emission_factor_methane_manure_management_by_default()
        .loc[:, "GOAT"]
        .reset_coords(drop=True)
        .expand_dims({"ANIMALS_TYPES_I": ["GOAT"]}, 1)
        .values
    )
    value.loc[:, ["SHEEP"]] = (
        emission_factor_methane_manure_management_by_default()
        .loc[:, "SHEEP"]
        .reset_coords(drop=True)
        .expand_dims({"ANIMALS_TYPES_I": ["SHEEP"]}, 1)
        .values
    )
    value.loc[:, ["CHICKENS"]] = (
        emission_factor_methane_manure_management_by_default()
        .loc[:, "CHICKENS"]
        .reset_coords(drop=True)
        .expand_dims({"ANIMALS_TYPES_I": ["CHICKENS"]}, 1)
        .values
    )
    value.loc[:, ["SWINE"]] = (
        if_then_else(
            switch_model_explorer() == 1,
            lambda: emission_first_factor_methane_manure_management()
            .loc[:, "SWINE"]
            .reset_coords(drop=True)
            * sum(
                model_explorer_manure_management_system()
                .loc["SWINE", :, :]
                .reset_coords(drop=True)
                .rename({"MANURE_MANAGEMENT_SYSTEM_I": "MANURE_MANAGEMENT_SYSTEM_I!"}),
                dim=["MANURE_MANAGEMENT_SYSTEM_I!"],
            ),
            lambda: emission_first_factor_methane_manure_management()
            .loc[:, "SWINE"]
            .reset_coords(drop=True)
            * sum(
                swine_emission_second_factor_methane_manure_management().rename(
                    {"MANURE_MANAGEMENT_SYSTEM_I": "MANURE_MANAGEMENT_SYSTEM_I!"}
                ),
                dim=["MANURE_MANAGEMENT_SYSTEM_I!"],
            ),
        )
        .expand_dims({"ANIMALS_TYPES_I": ["SWINE"]}, 1)
        .values
    )
    return value


@component.add(
    name="EMISSION_FIRST_FACTOR_METHANE_MANURE_MANAGEMENT",
    units="kg/(number_animals*Year)",
    subscripts=["REGIONS_9_I", "ANIMALS_TYPES_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_emission_first_factor_methane_manure_management"
    },
)
def emission_first_factor_methane_manure_management():
    """
    IPCC 2006 Guidelines (Tier 1) (Eggleston, Buendia, Miwa, Ngara, & Tanabe, 2006) tABLES 10.14 TO 10.16 Adapted to WILIAM regions. Not used the ones of "goat", sheep and chkens, as this factor is to applied to the rest in which policies about manure system can be applied
    """
    return _ext_constant_emission_first_factor_methane_manure_management()


_ext_constant_emission_first_factor_methane_manure_management = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "EMISSION_FIRST_FACTOR_METHANE_MANURE_MANAGEMENT",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "ANIMALS_TYPES_I": _subscript_dict["ANIMALS_TYPES_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "ANIMALS_TYPES_I": _subscript_dict["ANIMALS_TYPES_I"],
    },
    "_ext_constant_emission_first_factor_methane_manure_management",
)


@component.add(
    name="EXO_AREA_IRRIGATED_RICE",
    units="km2",
    subscripts=["REGIONS_9_I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_exo_area_irrigated_rice",
        "__lookup__": "_ext_lookup_exo_area_irrigated_rice",
    },
)
def exo_area_irrigated_rice(x, final_subs=None):
    """
    irrigated crops area by region (exogenous data from simulation)
    """
    return _ext_lookup_exo_area_irrigated_rice(x, final_subs)


_ext_lookup_exo_area_irrigated_rice = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "TIME_EXO_SIMULATION",
    "EXO_AREA_IRRIGATED_RICE",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_lookup_exo_area_irrigated_rice",
)


@component.add(
    name="exo_area_irrigated_rice_t",
    units="km2",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "exo_area_irrigated_rice": 1},
)
def exo_area_irrigated_rice_t():
    """
    exogenous information from siulation
    """
    return exo_area_irrigated_rice(time())


@component.add(
    name="EXO_AREA_RAINFED_RICE",
    units="km2",
    subscripts=["REGIONS_9_I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_exo_area_rainfed_rice",
        "__lookup__": "_ext_lookup_exo_area_rainfed_rice",
    },
)
def exo_area_rainfed_rice(x, final_subs=None):
    """
    rainfed crops area by region
    """
    return _ext_lookup_exo_area_rainfed_rice(x, final_subs)


_ext_lookup_exo_area_rainfed_rice = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "TIME_EXO_SIMULATION",
    "EXO_AREA_RAINFED_RICE",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_lookup_exo_area_rainfed_rice",
)


@component.add(
    name="exo_area_rainfed_rice_t",
    units="km2",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "exo_area_rainfed_rice": 1},
)
def exo_area_rainfed_rice_t():
    """
    exogenous information from siulation
    """
    return exo_area_rainfed_rice(time())


@component.add(
    name="EXO_DIET_AVAILABLE",
    units="t/Year",
    subscripts=["REGIONS_9_I", "FOODS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"food_available_by_households_per_region": 1},
)
def exo_diet_available():
    """
    Switch made withouth data historic.. just directly from data from simultion...
    """
    return food_available_by_households_per_region()


@component.add(
    name="EXO_FERTILIZERS_DEMANDED",
    units="tonnes",
    subscripts=["REGIONS_9_I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_exo_fertilizers_demanded",
        "__lookup__": "_ext_lookup_exo_fertilizers_demanded",
    },
)
def exo_fertilizers_demanded(x, final_subs=None):
    """
    DATA from FAO about synthetic fertilizers demanded Historic data from 2005 to 2020 , then constant
    """
    return _ext_lookup_exo_fertilizers_demanded(x, final_subs)


_ext_lookup_exo_fertilizers_demanded = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "TIME_EXO_SIMULATION",
    "EXO_FERTILIZERS_DEMANDED",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_lookup_exo_fertilizers_demanded",
)


@component.add(
    name="exo_fertilizers_demanded_t",
    units="ton/Years",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "exo_fertilizers_demanded": 1},
)
def exo_fertilizers_demanded_t():
    """
    exogenous information from historic data from FAO
    """
    return exo_fertilizers_demanded(time())


@component.add(
    name="EXOGENOUS_CH4_ENTERIC_FERMENTATION_EMISSIONS",
    units="t/Year",
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_exogenous_ch4_enteric_fermentation_emissions",
        "__lookup__": "_ext_lookup_exogenous_ch4_enteric_fermentation_emissions",
    },
)
def exogenous_ch4_enteric_fermentation_emissions(x, final_subs=None):
    """
    Historic data of EMISSIONS from enteric fermentation from FAO https://www.fao.org/faostat/en/#data/GR/metadata
    """
    return _ext_lookup_exogenous_ch4_enteric_fermentation_emissions(x, final_subs)


_ext_lookup_exogenous_ch4_enteric_fermentation_emissions = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "TIME_HISTORIC_DATA",
    "EXOGENOUS_ENTERIC_FERMENTATION_EMISSIONS",
    {},
    _root,
    {},
    "_ext_lookup_exogenous_ch4_enteric_fermentation_emissions",
)


@component.add(
    name="EXOGENOUS_CH4_ENTERIC_FERMENTATION_EMISSIONS_t",
    units="t/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "exogenous_ch4_enteric_fermentation_emissions": 1},
)
def exogenous_ch4_enteric_fermentation_emissions_t():
    """
    HISTORIC Enteric emissions from FAO until 2020, then constant for the future
    """
    return exogenous_ch4_enteric_fermentation_emissions(time())


@component.add(
    name="FACTOR_EMISSION_N_APPLICATION",
    units="kg_N2ON/kgN",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_factor_emission_n_application"},
)
def factor_emission_n_application():
    """
    IPCC 2006 (Tier 1, Chapter 11, Table 11.1) default values for direct emissions N2O emitted from the various synthetic and organic N applications to soils, including crop residue and mineralisation of soil organic carbon in mineral soils due to land-use change or management "Conversion of N2O-N emissions to N2O emissions for reporting purposes is performed by using the following equation: N2O = N2O-N * 44/28 1 kg N2O-N = 1 kg de N= (44/28)*1 kg N2O (factor from kg of N to kg of N2O) (N2O= 44 g/mol and N=28 g/mol, and 1N2Omol=1N mol)
    """
    return _ext_constant_factor_emission_n_application()


_ext_constant_factor_emission_n_application = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "EF_N2O_direct_fertilizers",
    {},
    _root,
    {},
    "_ext_constant_factor_emission_n_application",
)


@component.add(
    name="FACTOR_EMISSION_N_APPLICATION_INDIRECT",
    units="kg_N2ON/kgvolatilised",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_factor_emission_n_application_indirect"},
)
def factor_emission_n_application_indirect():
    """
    IPCC 2006 (Tier 1, table 11.3)emission factor for N2O emissions from atmospheric deposition of N on soils and water surfaces
    """
    return _ext_constant_factor_emission_n_application_indirect()


_ext_constant_factor_emission_n_application_indirect = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "EF_N2O_indirect_fertilizers",
    {},
    _root,
    {},
    "_ext_constant_factor_emission_n_application_indirect",
)


@component.add(
    name="FACTOR_EMISSIONS_BASELINE_RICE",
    units="kgCH4/(ha*Year)",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_factor_emissions_baseline_rice"},
)
def factor_emissions_baseline_rice():
    """
    1,3 kgCH4/(ha*day)--> cultivation period! (120 days?) "FACTOR_EMISSIONS_BASELINE_RICE" Baseline emission factor: the IPCC default for EFc is 1.30 kg CH4 ha-1 day-1 (with error range of 0.80 - 2.20, Table 5.11), estimated by a statistical analysis of available field measurement data (Yan et al., 2005,
    """
    return _ext_constant_factor_emissions_baseline_rice()


_ext_constant_factor_emissions_baseline_rice = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "FACTOR_EMISSIONS_BASELINE_RICE",
    {},
    _root,
    {},
    "_ext_constant_factor_emissions_baseline_rice",
)


@component.add(
    name="FACTOR_EMISSIONS_ENTERIC_FERMENTATION",
    units="kg/(number_animals*Year)",
    subscripts=["REGIONS_9_I", "ANIMALS_TYPES_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_factor_emissions_enteric_fermentation"},
)
def factor_emissions_enteric_fermentation():
    """
    IPCC 2006 Guidelines (Tier 1) (Eggleston, Buendia, Miwa, Ngara, & Tanabe, 2006), Chapter 10 of Volume 4. Tables 10.10 and 10.11 Adapted to WILIAM regions
    """
    return _ext_constant_factor_emissions_enteric_fermentation()


_ext_constant_factor_emissions_enteric_fermentation = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "EMISSION_FACTOR_ENTERIC_FERMENTATION",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "ANIMALS_TYPES_I": _subscript_dict["ANIMALS_TYPES_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "ANIMALS_TYPES_I": _subscript_dict["ANIMALS_TYPES_I"],
    },
    "_ext_constant_factor_emissions_enteric_fermentation",
)


@component.add(
    name="food_available_by_households_per_region",
    units="t/Year",
    subscripts=["REGIONS_9_I", "FOODS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "diet_available": 1,
        "population_9_regions_for_diets": 1,
        "unit_conversion_t_kg": 1,
    },
)
def food_available_by_households_per_region():
    """
    tonnes of food available by region
    """
    return diet_available() * population_9_regions_for_diets() * unit_conversion_t_kg()


@component.add(
    name="food_consumption_region",
    units="t/Year",
    subscripts=["REGIONS_9_I", "FOODS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_law_emissions_diet_available": 1,
        "switch_law_emissions": 1,
        "exo_diet_available": 1,
        "food_available_by_households_per_region": 1,
    },
)
def food_consumption_region():
    """
    Food consumed by region
    """
    return if_then_else(
        np.logical_or(
            switch_law_emissions_diet_available() == 0, switch_law_emissions() == 0
        ),
        lambda: exo_diet_available(),
        lambda: food_available_by_households_per_region(),
    )


@component.add(
    name="food_consumption_world",
    units="t/Year",
    subscripts=["FOODS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"food_consumption_region": 1},
)
def food_consumption_world():
    return sum(
        food_consumption_region().rename({"REGIONS_9_I": "REGIONS_9_I!"}),
        dim=["REGIONS_9_I!"],
    )


@component.add(
    name="MEAT_MONOGASTRIC_CHICKENS_DISTRIBUTION",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_meat_monogastric_chickens_distribution"},
)
def meat_monogastric_chickens_distribution():
    """
    SHARE PRODUCTION ANIMALS (share of production that corresponds to an specific type of animal) Excel file: "Animals_number_prodcution_WORLD_clean"
    """
    return _ext_constant_meat_monogastric_chickens_distribution()


_ext_constant_meat_monogastric_chickens_distribution = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "MEAT_MONOGASTRIC_CHICKENS_DISTRIBUTION",
    {},
    _root,
    {},
    "_ext_constant_meat_monogastric_chickens_distribution",
)


@component.add(
    name="MEAT_MONOGASTRIC_SWINE_DISTRIBUTION",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_meat_monogastric_swine_distribution"},
)
def meat_monogastric_swine_distribution():
    """
    SHARE PRODUCTION ANIMALS (share of production that corresponds to an specific type of animal) Excel file: "Animals_number_prodcution_WORLD_clean"
    """
    return _ext_constant_meat_monogastric_swine_distribution()


_ext_constant_meat_monogastric_swine_distribution = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "MEAT_MONOGASTRIC_SWINE_DISTRIBUTION",
    {},
    _root,
    {},
    "_ext_constant_meat_monogastric_swine_distribution",
)


@component.add(
    name="MEAT_RUMINANT_BUFFALO_DISTRIBUTION",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_meat_ruminant_buffalo_distribution"},
)
def meat_ruminant_buffalo_distribution():
    """
    SHARE PRODUCTION ANIMALS (share of production that corresponds to an specific type of animal) Excel file: "Animals_number_prodcution_WORLD_clean"
    """
    return _ext_constant_meat_ruminant_buffalo_distribution()


_ext_constant_meat_ruminant_buffalo_distribution = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "MEAT_RUMINANT_BUFFALO_DISTRIBUTION",
    {},
    _root,
    {},
    "_ext_constant_meat_ruminant_buffalo_distribution",
)


@component.add(
    name="MEAT_RUMINANT_CATTLE_DISTRIBUTION",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_meat_ruminant_cattle_distribution"},
)
def meat_ruminant_cattle_distribution():
    """
    SHARE PRODUCTION ANIMALS (share of production that corresponds to an specific type of animal) Excel file: "Animals_number_prodcution_WORLD_clean"
    """
    return _ext_constant_meat_ruminant_cattle_distribution()


_ext_constant_meat_ruminant_cattle_distribution = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "MEAT_RUMINANT_CATTLE_DISTRIBUTION",
    {},
    _root,
    {},
    "_ext_constant_meat_ruminant_cattle_distribution",
)


@component.add(
    name="MEAT_RUMINANT_GOAT_DISTRIBUTION",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_meat_ruminant_goat_distribution"},
)
def meat_ruminant_goat_distribution():
    """
    SHARE PRODUCTION ANIMALS (share of production that corresponds to an specific type of animal) Excel file: "Animals_number_prodcution_WORLD_clean"
    """
    return _ext_constant_meat_ruminant_goat_distribution()


_ext_constant_meat_ruminant_goat_distribution = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "MEAT_RUMINANT_GOAT_DISTRIBUTION",
    {},
    _root,
    {},
    "_ext_constant_meat_ruminant_goat_distribution",
)


@component.add(
    name="MEAT_RUMINANT_SHEEP_DISTRIBUTION",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_meat_ruminant_sheep_distribution"},
)
def meat_ruminant_sheep_distribution():
    """
    SHARE PRODUCTION ANIMALS (share of production that corresponds to an specific type of animal) Excel file: "Animals_number_prodcution_WORLD_clean"
    """
    return _ext_constant_meat_ruminant_sheep_distribution()


_ext_constant_meat_ruminant_sheep_distribution = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "MEAT_RUMINANT_SHEEP_DISTRIBUTION",
    {},
    _root,
    {},
    "_ext_constant_meat_ruminant_sheep_distribution",
)


@component.add(
    name="METHANE_CONVERSION_FACTOR_BY_SYSTEM",
    units="DMNL",
    subscripts=["REGIONS_9_I", "MANURE_MANAGEMENT_SYSTEM_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_methane_conversion_factor_by_system"},
)
def methane_conversion_factor_by_system():
    """
    methane conversion factors for each manure management system S by WILIAM region. From IPCC 2006 Chapter livestock, adapted to WILIAM regions
    """
    return _ext_constant_methane_conversion_factor_by_system()


_ext_constant_methane_conversion_factor_by_system = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "METHANE_CONVERSION_FACTOR_BY_SYSTEM",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "MANURE_MANAGEMENT_SYSTEM_I": _subscript_dict["MANURE_MANAGEMENT_SYSTEM_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "MANURE_MANAGEMENT_SYSTEM_I": _subscript_dict["MANURE_MANAGEMENT_SYSTEM_I"],
    },
    "_ext_constant_methane_conversion_factor_by_system",
)


@component.add(
    name="N2O_emissions_agriculture",
    units="Mt/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"n2o_emissions_fertilizers": 1, "n2o_emissions_livestock": 1},
)
def n2o_emissions_agriculture():
    """
    Total N2O emissions from agriculture. Important note: the emissions calculated in this variable from agriculture are ONLY those related to "Enteric fermentation", "Manure management", "Rice cultivation" , and "Synthetic Fertilizers. The rest of agriculture emissions are not included in this variable such as crop residues, burning of crop residues, manure left on pasture, manure applied to soils, or energy use in agriculture.
    """
    return n2o_emissions_fertilizers() + n2o_emissions_livestock()


@component.add(
    name="N2O_emissions_fertilizers",
    units="Mt_N2O/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "n_application": 2,
        "factor_emission_n_application": 1,
        "n_fraction_volatilises": 1,
        "factor_emission_n_application_indirect": 1,
        "unit_conversion_n2on_n2o": 1,
        "unit_conversion_t_kg": 1,
        "unit_conversion_t_mt": 1,
    },
)
def n2o_emissions_fertilizers():
    """
    Direct and indirect emissions from synthetic fertilizers (N applied by farmers)
    """
    return (
        (
            n_application() * factor_emission_n_application()
            + n_application()
            * n_fraction_volatilises()
            * factor_emission_n_application_indirect()
        )
        * unit_conversion_n2on_n2o()
        * unit_conversion_t_kg()
        * (1 / unit_conversion_t_mt())
    )


@component.add(
    name="N2O_emissions_livestock",
    units="Mton_N/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"n2o_emissions_manure_management": 1},
)
def n2o_emissions_livestock():
    """
    N2O livestock emissions due to manure management.
    """
    return n2o_emissions_manure_management()


@component.add(
    name="N2O_emissions_manure_management",
    units="Mton_N/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "ch4_emissions_manure_management_by_region": 1,
        "share_rest_n2o_manure_management_emissions": 1,
    },
)
def n2o_emissions_manure_management():
    """
    Total N20 emissions due to manure management
    """
    return (
        ch4_emissions_manure_management_by_region()
        * share_rest_n2o_manure_management_emissions()
    )


@component.add(
    name="N_application",
    units="kgN/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_law_emissions_fertilizers_demanded": 1,
        "switch_law_emissions": 1,
        "exo_fertilizers_demanded_t": 1,
        "unit_conversion_t_kg": 2,
        "fertilizers_demanded": 1,
    },
)
def n_application():
    """
    Exogenous information from FAO or Fertilizers demanded by cropland area (based on type of managemednt applied).
    """
    return if_then_else(
        np.logical_or(
            switch_law_emissions_fertilizers_demanded() == 0,
            switch_law_emissions() == 0,
        ),
        lambda: exo_fertilizers_demanded_t() * 1 / unit_conversion_t_kg(),
        lambda: fertilizers_demanded() * 1 / unit_conversion_t_kg(),
    )


@component.add(
    name="N_FRACTION_VOLATILISES",
    units="kgvolatilised/kgN",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_n_fraction_volatilises"},
)
def n_fraction_volatilises():
    """
    IPCC 2006 (Tier 1, table 11.3)fraction of synthetic fertiliser N that volatilises as NH3 and NOx, kg N volatilised (kg of N applied)-1
    """
    return _ext_constant_n_fraction_volatilises()


_ext_constant_n_fraction_volatilises = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "Fraction_volatilises",
    {},
    _root,
    {},
    "_ext_constant_n_fraction_volatilises",
)


@component.add(
    name="number_animals",
    units="number_animals",
    subscripts=["ANIMALS_TYPES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"animals_producing": 1, "ratio_animals_producing": 1},
)
def number_animals():
    """
    total number of animals for calculating emissions
    """
    return animals_producing() * (1 / ratio_animals_producing())


@component.add(
    name="number_animals_by_region",
    units="number_animals",
    subscripts=["REGIONS_9_I", "ANIMALS_TYPES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"animals_distribution_regions": 1, "number_animals": 1},
)
def number_animals_by_region():
    """
    total number of animals by type and by region
    """
    return animals_distribution_regions() * number_animals()


@component.add(
    name="NUMBER_ANIMALS_HISTORIC",
    units="number_animals",
    subscripts=["ANIMALS_TYPES_I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_number_animals_historic",
        "__lookup__": "_ext_lookup_number_animals_historic",
    },
)
def number_animals_historic(x, final_subs=None):
    """
    Historic data of number of animals (stock) from FAO https://www.fao.org/faostat/en/#data/GR/metadata
    """
    return _ext_lookup_number_animals_historic(x, final_subs)


_ext_lookup_number_animals_historic = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "TIME_HISTORIC_DATA",
    "NUMBER_ANIMALS_HISTORIC",
    {"ANIMALS_TYPES_I": _subscript_dict["ANIMALS_TYPES_I"]},
    _root,
    {"ANIMALS_TYPES_I": _subscript_dict["ANIMALS_TYPES_I"]},
    "_ext_lookup_number_animals_historic",
)


@component.add(
    name="NUMBER_ANIMALS_HISTORIC_t",
    units="number_animals",
    subscripts=["ANIMALS_TYPES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "number_animals_historic": 1},
)
def number_animals_historic_t():
    """
    historic number animals
    """
    return number_animals_historic(time())


@component.add(
    name="OBJETIVE_BUFFALO_MANURE_SYSTEM_SP",
    units="DMNL",
    subscripts=["REGIONS_9_I", "MANURE_MANAGEMENT_SYSTEM_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_objetive_buffalo_manure_system_sp"},
)
def objetive_buffalo_manure_system_sp():
    """
    GET_DIRECT_CONSTANTS( 'scenario_parameters/scenario_parameters.xlsx' , 'land_and_water' , 'POLICY_OBJETIVE_BUFFALO_MANURE_SYSTEM_SP' ) % MS by default. The "less emissions" options are: solid storage, dry lot, range/paddock, daily spread and Pit storage <1month From IPCC 2006 Chapter livestock, adapted to WILIAM regions % of the types manure systems by type of animal , for the calculation of methane emissions due to manure management . These are the ones currently applied in WILIAM regions obtained in IPCC 2006 adapted to WILIAM
    """
    return _ext_constant_objetive_buffalo_manure_system_sp()


_ext_constant_objetive_buffalo_manure_system_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_OBJETIVE_BUFFALO_MANURE_SYSTEM_SP",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "MANURE_MANAGEMENT_SYSTEM_I": _subscript_dict["MANURE_MANAGEMENT_SYSTEM_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "MANURE_MANAGEMENT_SYSTEM_I": _subscript_dict["MANURE_MANAGEMENT_SYSTEM_I"],
    },
    "_ext_constant_objetive_buffalo_manure_system_sp",
)


@component.add(
    name="OBJETIVE_DAIRY_CATTLE_MANURE_SYSTEM_SP",
    units="DMNL",
    subscripts=["REGIONS_9_I", "MANURE_MANAGEMENT_SYSTEM_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_objetive_dairy_cattle_manure_system_sp"},
)
def objetive_dairy_cattle_manure_system_sp():
    """
    % MS by default. The "less emissions" options are: solid storage, dry lot, range/paddock, daily spread and Pit storage <1month From IPCC 2006 Chapter livestock, adapted to WILIAM regions % of the types manure systems by type of animal , for the calculation of methane emissions due to manure management . These are the ones currently applied in WILIAM regions obtained in IPCC 2006 adapted to WILIAM
    """
    return _ext_constant_objetive_dairy_cattle_manure_system_sp()


_ext_constant_objetive_dairy_cattle_manure_system_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_OBJETIVE_DAIRY_CATTLE_MANURE_SYSTEM_SP",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "MANURE_MANAGEMENT_SYSTEM_I": _subscript_dict["MANURE_MANAGEMENT_SYSTEM_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "MANURE_MANAGEMENT_SYSTEM_I": _subscript_dict["MANURE_MANAGEMENT_SYSTEM_I"],
    },
    "_ext_constant_objetive_dairy_cattle_manure_system_sp",
)


@component.add(
    name="OBJETIVE_OTHER_CATTLE_MANURE_SYSTEM_SP",
    units="DMNL",
    subscripts=["REGIONS_9_I", "MANURE_MANAGEMENT_SYSTEM_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_objetive_other_cattle_manure_system_sp"},
)
def objetive_other_cattle_manure_system_sp():
    """
    % MS by default. The "less emissions" options are: solid storage, dry lot, range/paddock, daily spread and Pit storage <1month From IPCC 2006 Chapter livestock, adapted to WILIAM regions % of the types manure systems by type of animal , for the calculation of methane emissions due to manure management . These are the ones currently applied in WILIAM regions obtained in IPCC 2006 adapted to WILIAM
    """
    return _ext_constant_objetive_other_cattle_manure_system_sp()


_ext_constant_objetive_other_cattle_manure_system_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_OBJETIVE_OTHER_CATTLE_MANURE_SYSTEM_SP",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "MANURE_MANAGEMENT_SYSTEM_I": _subscript_dict["MANURE_MANAGEMENT_SYSTEM_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "MANURE_MANAGEMENT_SYSTEM_I": _subscript_dict["MANURE_MANAGEMENT_SYSTEM_I"],
    },
    "_ext_constant_objetive_other_cattle_manure_system_sp",
)


@component.add(
    name="OBJETIVE_SWINE_MANURE_SYSTEM_SP",
    units="DMNL",
    subscripts=["REGIONS_9_I", "MANURE_MANAGEMENT_SYSTEM_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_objetive_swine_manure_system_sp"},
)
def objetive_swine_manure_system_sp():
    """
    % MS by default. The "less emissions" options are: solid storage, dry lot, range/paddock, daily spread and Pit storage <1month From IPCC 2006 Chapter livestock, adapted to WILIAM regions % of the types manure systems by type of animal , for the calculation of methane emissions due to manure management . These are the ones currently applied in WILIAM regions obtained in IPCC 2006 adapted to WILIAM
    """
    return _ext_constant_objetive_swine_manure_system_sp()


_ext_constant_objetive_swine_manure_system_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_OBJETIVE_SWINE_MANURE_SYSTEM_SP",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "MANURE_MANAGEMENT_SYSTEM_I": _subscript_dict["MANURE_MANAGEMENT_SYSTEM_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "MANURE_MANAGEMENT_SYSTEM_I": _subscript_dict["MANURE_MANAGEMENT_SYSTEM_I"],
    },
    "_ext_constant_objetive_swine_manure_system_sp",
)


@component.add(
    name="OTHER_CATLLE_EMISSION_SECOND_FACTOR_METHANE_MANURE_MANAGEMENT",
    units="kg/(number_animals*Year)",
    subscripts=["REGIONS_9_I", "MANURE_MANAGEMENT_SYSTEM_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_livestock_manure_management_sp": 1,
        "time": 2,
        "year_initial_manure_management_system_sp": 1,
        "year_final_manure_management_system_sp": 1,
        "objetive_other_cattle_manure_system_sp": 1,
        "methane_conversion_factor_by_system": 2,
        "other_cattle_manure_system": 1,
    },
)
def other_catlle_emission_second_factor_methane_manure_management():
    """
    IPCC 2006 Guidelines (Tier 1) (Eggleston, Buendia, Miwa, Ngara, & Tanabe, 2006) tABLES 10.14 TO 10.16 Adapted to WILIAM regions. Not used the ones of "goat", sheep and chkens, as this factor is to applied to the rest in which policies about manure system can be applied
    """
    return if_then_else(
        np.logical_and(
            switch_livestock_manure_management_sp() == 1,
            np.logical_and(
                time() > year_initial_manure_management_system_sp(),
                time() <= year_final_manure_management_system_sp(),
            ),
        ).expand_dims(
            {
                "MANURE_MANAGEMENT_SYSTEM_I": _subscript_dict[
                    "MANURE_MANAGEMENT_SYSTEM_I"
                ]
            },
            1,
        ),
        lambda: methane_conversion_factor_by_system()
        * objetive_other_cattle_manure_system_sp(),
        lambda: methane_conversion_factor_by_system() * other_cattle_manure_system(),
    )


@component.add(
    name="OTHER_CATTLE_MANURE_SYSTEM",
    units="DMNL",
    subscripts=["REGIONS_9_I", "MANURE_MANAGEMENT_SYSTEM_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_other_cattle_manure_system"},
)
def other_cattle_manure_system():
    """
    % MS by default. The "less emissions" options are: solid storage, dry lot, range/paddock, daily spread and Pit storage <1month From IPCC 2006 Chapter livestock, adapted to WILIAM regions % of the types manure systems by type of animal , for the calculation of methane emissions due to manure management . These are the ones currently applied in WILIAM regions obtained in IPCC 2006 adapted to WILIAM
    """
    return _ext_constant_other_cattle_manure_system()


_ext_constant_other_cattle_manure_system = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "OTHER_CATTLE_MANURE_SYSTEM",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "MANURE_MANAGEMENT_SYSTEM_I": _subscript_dict["MANURE_MANAGEMENT_SYSTEM_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "MANURE_MANAGEMENT_SYSTEM_I": _subscript_dict["MANURE_MANAGEMENT_SYSTEM_I"],
    },
    "_ext_constant_other_cattle_manure_system",
)


@component.add(
    name="production_from_animals",
    units="t/Year",
    subscripts=["FOODS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"food_consumption_world": 1, "ratio_consumption_production": 1},
)
def production_from_animals():
    """
    Livestock primary production Products (Dairy, eggs, meat ruminants, MEAT MONOGASTRIC) form main CH4 and N2O emmiters (Cattle, buffalo, sheep, chickens, goat, and swine)
    """
    return zidz(food_consumption_world(), ratio_consumption_production())


@component.add(
    name="RATIO_ANIMALS_PRODUCING",
    units="DMNL",
    subscripts=["ANIMALS_TYPES_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_ratio_animals_producing"},
)
def ratio_animals_producing():
    """
    Ratio between animals producing and total livestock (total number of animals alive [animals producing/total stock] The last ones are the number of animals emitting gases. Excel file: "animals_number_production_WORLD"
    """
    return _ext_constant_ratio_animals_producing()


_ext_constant_ratio_animals_producing = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "RATIO_ANIMALS_PRODUCING*",
    {"ANIMALS_TYPES_I": _subscript_dict["ANIMALS_TYPES_I"]},
    _root,
    {"ANIMALS_TYPES_I": _subscript_dict["ANIMALS_TYPES_I"]},
    "_ext_constant_ratio_animals_producing",
)


@component.add(
    name="RATIO_CONSUMPTION_PRODUCTION",
    units="DMNL",
    subscripts=["FOODS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_ratio_consumption_production"},
)
def ratio_consumption_production():
    """
    To take into account losses (data processed from FAO)
    """
    return _ext_constant_ratio_consumption_production()


_ext_constant_ratio_consumption_production = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "RATIO_CONSUMPTION_PRODUCTION*",
    {"FOODS_I": _subscript_dict["FOODS_I"]},
    _root,
    {"FOODS_I": _subscript_dict["FOODS_I"]},
    "_ext_constant_ratio_consumption_production",
)


@component.add(
    name="REST_ENTERIC_FERMENTATION_EMISSIONS",
    units="t/Year",
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_rest_enteric_fermentation_emissions",
        "__lookup__": "_ext_lookup_rest_enteric_fermentation_emissions",
    },
)
def rest_enteric_fermentation_emissions(x, final_subs=None):
    """
    Historic data of number of animals (stock) from FAO https://www.fao.org/faostat/en/#data/GR/metadata
    """
    return _ext_lookup_rest_enteric_fermentation_emissions(x, final_subs)


_ext_lookup_rest_enteric_fermentation_emissions = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "TIME_HISTORIC_DATA",
    "REST_ENTERIC_FERMENTATION_EMISSIONS",
    {},
    _root,
    {},
    "_ext_lookup_rest_enteric_fermentation_emissions",
)


@component.add(
    name="REST_ENTERIC_FERMENTATION_EMISSIONS_t",
    units="t/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "rest_enteric_fermentation_emissions": 1},
)
def rest_enteric_fermentation_emissions_t():
    """
    Enteric emissions from the rest of animals (historic emissions + assumption of constant since 2020
    """
    return rest_enteric_fermentation_emissions(time())


@component.add(
    name="RICE_AREA_HISTORIC",
    units="ha",
    subscripts=["REGIONS_9_I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_rice_area_historic",
        "__lookup__": "_ext_lookup_rice_area_historic",
    },
)
def rice_area_historic(x, final_subs=None):
    """
    Historic data of area harvested of paddy rice from FAO https://www.fao.org/faostat/en/#data/GR/metadata
    """
    return _ext_lookup_rice_area_historic(x, final_subs)


_ext_lookup_rice_area_historic = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "TIME_HISTORIC_DATA",
    "RICE_AREA_HISTORIC",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_lookup_rice_area_historic",
)


@component.add(
    name="RICE_AREA_HISTORIC_KM2",
    units="km2",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"rice_area_historic_t": 1, "unit_conversion_km2_ha": 1},
)
def rice_area_historic_km2():
    """
    Historic data of area harvested of paddy rice from FAO https://www.fao.org/faostat/en/#data/GR/metadata in km2
    """
    return rice_area_historic_t() * unit_conversion_km2_ha()


@component.add(
    name="RICE_AREA_HISTORIC_KM2_world",
    units="km2",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"rice_area_historic_km2": 1},
)
def rice_area_historic_km2_world():
    """
    Historic data of area harvested of paddy rice from FAO https://www.fao.org/faostat/en/#data/GR/metadata in km2 world
    """
    return sum(
        rice_area_historic_km2().rename({"REGIONS_9_I": "REGIONS_9_I!"}),
        dim=["REGIONS_9_I!"],
    )


@component.add(
    name="RICE_AREA_HISTORIC_t",
    units="km2",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "rice_area_historic": 1},
)
def rice_area_historic_t():
    """
    historic rice area
    """
    return rice_area_historic(time())


@component.add(
    name="RICE_EMISSIONS_CH4_HISTORIC",
    units="MtCH4/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_rice_emissions_ch4_historic",
        "__lookup__": "_ext_lookup_rice_emissions_ch4_historic",
    },
)
def rice_emissions_ch4_historic(x, final_subs=None):
    """
    Historic data of methane emissions from Rice Cultivation (CH4) from FAO https://www.fao.org/faostat/en/#data/GR/metadata
    """
    return _ext_lookup_rice_emissions_ch4_historic(x, final_subs)


_ext_lookup_rice_emissions_ch4_historic = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "TIME_HISTORIC_DATA",
    "RICE_EMISSIONS_HISTORIC",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_lookup_rice_emissions_ch4_historic",
)


@component.add(
    name="rice_emissions_CH4_historic_t",
    units="MtCH4/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "rice_emissions_ch4_historic": 1},
)
def rice_emissions_ch4_historic_t():
    """
    historic rice emissions
    """
    return rice_emissions_ch4_historic(time())


@component.add(
    name="rice_emissions_CH4_historic_t_world",
    units="km2",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"rice_emissions_ch4_historic_t": 1},
)
def rice_emissions_ch4_historic_t_world():
    """
    historic rice emissions WORLD
    """
    return sum(
        rice_emissions_ch4_historic_t().rename({"REGIONS_9_I": "REGIONS_9_I!"}),
        dim=["REGIONS_9_I!"],
    )


@component.add(
    name="SCALING_FACTOR_ORGANIC_AMENDMENT",
    units="Dnml",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_scaling_factor_organic_amendment"},
)
def scaling_factor_organic_amendment():
    """
    Default value of 2 for all countries (metadata from FAO) (although a bit old).Corresponding
    """
    return _ext_constant_scaling_factor_organic_amendment()


_ext_constant_scaling_factor_organic_amendment = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "SCALING_FACTOR_ORGANIC_AMENDMENT",
    {},
    _root,
    {},
    "_ext_constant_scaling_factor_organic_amendment",
)


@component.add(
    name="SCALING_FACTOR_WATER_REGIME_PRESEASON",
    units="Dnml",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_scaling_factor_water_regime_preseason"},
)
def scaling_factor_water_regime_preseason():
    """
    scaling factor to account for the differences in water regime in the pre-season before the cultivation period (from Table 5.13) ipcc 2006 Tier 1). --> No more information: The aggregated case (1.22 refers to a situation when activity data are only available for rice ecosystem types, but not for flooding patterns
    """
    return _ext_constant_scaling_factor_water_regime_preseason()


_ext_constant_scaling_factor_water_regime_preseason = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "SCALING_FACTOR_WATER_REGIME_PRESEASON",
    {},
    _root,
    {},
    "_ext_constant_scaling_factor_water_regime_preseason",
)


@component.add(
    name="SCALING_FACTOR_WATER_REGIME_RICE_IRRIGATED",
    units="Dnml",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_scaling_factor_water_regime_rice_irrigated"
    },
)
def scaling_factor_water_regime_rice_irrigated():
    """
    water regime during the cultivation period default scaling factors and error ranges reflecting different water regimes. (tABLE 5.12, ipcc 2006 Tier 1). ( DURING THE CULTIVATION PERIOD RELATIVE TO CONTINUOUSLY FLOODED FIELDS )
    """
    return _ext_constant_scaling_factor_water_regime_rice_irrigated()


_ext_constant_scaling_factor_water_regime_rice_irrigated = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "SCALING_FACTOR_WATER_REGIME_RICE_IRRIGATED",
    {},
    _root,
    {},
    "_ext_constant_scaling_factor_water_regime_rice_irrigated",
)


@component.add(
    name="SCALING_FACTOR_WATER_REGIME_RICE_RAINFED",
    units="Dnml",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_scaling_factor_water_regime_rice_rainfed"
    },
)
def scaling_factor_water_regime_rice_rainfed():
    """
    water regime during the cultivation period default scaling factors and error ranges reflecting different water regimes. (tABLE 5.12, ipcc 2006 Tier 1). ( DURING THE CULTIVATION PERIOD RELATIVE TO CONTINUOUSLY FLOODED FIELDS )
    """
    return _ext_constant_scaling_factor_water_regime_rice_rainfed()


_ext_constant_scaling_factor_water_regime_rice_rainfed = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "SCALING_FACTOR_WATER_REGIME_RICE_RAINFED",
    {},
    _root,
    {},
    "_ext_constant_scaling_factor_water_regime_rice_rainfed",
)


@component.add(
    name="share_area_of_irrigated_rice",
    units="km2",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"area_of_irrigated_rice": 2, "area_of_rainfed_rice": 1},
)
def share_area_of_irrigated_rice():
    """
    Share of the Area of rice with water regime irrigated with respect to the total rice area
    """
    return zidz(
        area_of_irrigated_rice(), area_of_rainfed_rice() + area_of_irrigated_rice()
    )


@component.add(
    name="SHARE_REST_CH4_ENTERIC_FERMENTATION_EMISSIONS",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_share_rest_ch4_enteric_fermentation_emissions"
    },
)
def share_rest_ch4_enteric_fermentation_emissions():
    return _ext_constant_share_rest_ch4_enteric_fermentation_emissions()


_ext_constant_share_rest_ch4_enteric_fermentation_emissions = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "SHARE_REST_CH4_ENTERIC_FERMENTATION_EMISSIONS",
    {},
    _root,
    {},
    "_ext_constant_share_rest_ch4_enteric_fermentation_emissions",
)


@component.add(
    name="SHARE_REST_CH4_MANURE_MANAGEMENT_EMISSIONS",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_share_rest_ch4_manure_management_emissions"
    },
)
def share_rest_ch4_manure_management_emissions():
    return _ext_constant_share_rest_ch4_manure_management_emissions()


_ext_constant_share_rest_ch4_manure_management_emissions = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "SHARE_REST_CH4_MANURE_MANAGEMENT_EMISSIONS",
    {},
    _root,
    {},
    "_ext_constant_share_rest_ch4_manure_management_emissions",
)


@component.add(
    name="SHARE_REST_N2O_MANURE_MANAGEMENT_EMISSIONS",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_share_rest_n2o_manure_management_emissions"
    },
)
def share_rest_n2o_manure_management_emissions():
    return _ext_constant_share_rest_n2o_manure_management_emissions()


_ext_constant_share_rest_n2o_manure_management_emissions = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "SHARE_REST_N2O_MANURE_MANAGEMENT_EMISSIONS",
    {},
    _root,
    {},
    "_ext_constant_share_rest_n2o_manure_management_emissions",
)


@component.add(
    name="SHARE_UPLAND_RICE_BY_REGION",
    units="Dnml",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_share_upland_rice_by_region"},
)
def share_upland_rice_by_region():
    """
    Share of upland rice with respect to the total "rainfed" area
    """
    return _ext_constant_share_upland_rice_by_region()


_ext_constant_share_upland_rice_by_region = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "SHARE_UPLAND_RICE_BY_REGION*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_share_upland_rice_by_region",
)


@component.add(
    name="SWINE_EMISSION_SECOND_FACTOR_METHANE_MANURE_MANAGEMENT",
    units="kg/(number_animals*Year)",
    subscripts=["REGIONS_9_I", "MANURE_MANAGEMENT_SYSTEM_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_livestock_manure_management_sp": 1,
        "time": 2,
        "year_initial_manure_management_system_sp": 1,
        "year_final_manure_management_system_sp": 1,
        "objetive_swine_manure_system_sp": 1,
        "methane_conversion_factor_by_system": 2,
        "swine_manure_system": 1,
    },
)
def swine_emission_second_factor_methane_manure_management():
    """
    IPCC 2006 Guidelines (Tier 1) (Eggleston, Buendia, Miwa, Ngara, & Tanabe, 2006) tABLES 10.14 TO 10.16 Adapted to WILIAM regions. Not used the ones of "goat", sheep and chkens, as this factor is to be applied to the rest in which policies about manure system can be applied. If the policies about manure management are activited then the estimation are based on the new manure system defined by the policy. If not, the values by defaul (manure management systems according to each region of WILIAM) are considered. This is based in 2006 IPCC guidelines , but adaptated to WILIAM regions
    """
    return if_then_else(
        np.logical_and(
            switch_livestock_manure_management_sp() == 1,
            np.logical_and(
                time() > year_initial_manure_management_system_sp(),
                time() <= year_final_manure_management_system_sp(),
            ),
        ).expand_dims(
            {
                "MANURE_MANAGEMENT_SYSTEM_I": _subscript_dict[
                    "MANURE_MANAGEMENT_SYSTEM_I"
                ]
            },
            1,
        ),
        lambda: methane_conversion_factor_by_system()
        * objetive_swine_manure_system_sp(),
        lambda: methane_conversion_factor_by_system() * swine_manure_system(),
    )


@component.add(
    name="SWINE_MANURE_SYSTEM",
    units="DMNL",
    subscripts=["REGIONS_9_I", "MANURE_MANAGEMENT_SYSTEM_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_swine_manure_system"},
)
def swine_manure_system():
    """
    % MS by default. The "less emissions" options are: solid storage, dry lot, range/paddock, daily spread and Pit storage <1month From IPCC 2006 Chapter livestock, adapted to WILIAM regions % of the types manure systems by type of animal , for the calculation of methane emissions due to manure management . These are the ones currently applied in WILIAM regions obtained in IPCC 2006 adapted to WILIAM
    """
    return _ext_constant_swine_manure_system()


_ext_constant_swine_manure_system = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "SWINE_CATTLE_MANURE_SYSTEM",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "MANURE_MANAGEMENT_SYSTEM_I": _subscript_dict["MANURE_MANAGEMENT_SYSTEM_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "MANURE_MANAGEMENT_SYSTEM_I": _subscript_dict["MANURE_MANAGEMENT_SYSTEM_I"],
    },
    "_ext_constant_swine_manure_system",
)


@component.add(
    name="SWITCH_LAW_EMISSIONS_DIET_AVAILABLE",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_law_emissions_diet_available"},
)
def switch_law_emissions_diet_available():
    """
    Temporal switch- - 0: application of exogenous data - 1: all integrated (endogenous information)
    """
    return _ext_constant_switch_law_emissions_diet_available()


_ext_constant_switch_law_emissions_diet_available = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_LAW_EMISSIONS_DIET_AVAILABLE",
    {},
    _root,
    {},
    "_ext_constant_switch_law_emissions_diet_available",
)


@component.add(
    name="SWITCH_LAW_EMISSIONS_FERTILIZERS_DEMANDED",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_switch_law_emissions_fertilizers_demanded"
    },
)
def switch_law_emissions_fertilizers_demanded():
    """
    Temporal switch- - 0: application of exogenous data - 1: all integrated (endogenous information)
    """
    return _ext_constant_switch_law_emissions_fertilizers_demanded()


_ext_constant_switch_law_emissions_fertilizers_demanded = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_LAW_EMISSIONS_FERTILIZERS_DEMANDED",
    {},
    _root,
    {},
    "_ext_constant_switch_law_emissions_fertilizers_demanded",
)


@component.add(
    name="SWITCH_LAW_EMISSIONS_IRRIGATED_CROP_AREA",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_switch_law_emissions_irrigated_crop_area"
    },
)
def switch_law_emissions_irrigated_crop_area():
    """
    Temporal switch- - 0: application of exogenous data - 1: all integrated (endogenous information)
    """
    return _ext_constant_switch_law_emissions_irrigated_crop_area()


_ext_constant_switch_law_emissions_irrigated_crop_area = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_LAW_EMISSIONS_IRRIGATED_CROP_AREA",
    {},
    _root,
    {},
    "_ext_constant_switch_law_emissions_irrigated_crop_area",
)


@component.add(
    name="SWITCH_LIVESTOCK_MANURE_MANAGEMENT_SP",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_livestock_manure_management_sp"},
)
def switch_livestock_manure_management_sp():
    """
    0. No new policies. Keep trends (values by default from IPCC 2006 Tables 10.14 to 10.16). 1. Policies based on the new the porcentage of manure management handled as an specific systems. The "less emissions" options are: solid storage, dry lot, range/paddock, daily spread and Pit storage <1month
    """
    return _ext_constant_switch_livestock_manure_management_sp()


_ext_constant_switch_livestock_manure_management_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "SWITCH_MANURE_MANAGEMENT_SYSTEM_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_switch_livestock_manure_management_sp",
)


@component.add(
    name="YEAR_FINAL_MANURE_MANAGEMENT_SYSTEM_SP",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_year_final_manure_management_system_sp"},
)
def year_final_manure_management_system_sp():
    return _ext_constant_year_final_manure_management_system_sp()


_ext_constant_year_final_manure_management_system_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "YEAR_FINAL_MANURE_MANAGEMENT_SYSTEM_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_year_final_manure_management_system_sp",
)


@component.add(
    name="YEAR_INITIAL_MANURE_MANAGEMENT_SYSTEM_SP",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_year_initial_manure_management_system_sp"
    },
)
def year_initial_manure_management_system_sp():
    return _ext_constant_year_initial_manure_management_system_sp()


_ext_constant_year_initial_manure_management_system_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "YEAR_INITIAL_MANURE_MANAGEMENT_SYSTEM_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_year_initial_manure_management_system_sp",
)


@component.add(
    name="YIELD_OF_BUFFALO_MILK",
    units="t/number_animals",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_yield_of_buffalo_milk"},
)
def yield_of_buffalo_milk():
    """
    Yields of livestock animals. Based on data from FAO (at WORLD level Excel file: "Animals_number_prodcution_WORLD_clean"
    """
    return _ext_constant_yield_of_buffalo_milk()


_ext_constant_yield_of_buffalo_milk = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "YIELD_OF_BUFFALO_MILK",
    {},
    _root,
    {},
    "_ext_constant_yield_of_buffalo_milk",
)


@component.add(
    name="YIELD_OF_CATTLE_MILK",
    units="t/number_animals",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_yield_of_cattle_milk"},
)
def yield_of_cattle_milk():
    """
    Yields of livestock animals. Based on data from FAO (at WORLD level Excel file: "Animals_number_prodcution_WORLD_clean"
    """
    return _ext_constant_yield_of_cattle_milk()


_ext_constant_yield_of_cattle_milk = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "YIELD_OF_CATTLE_MILK",
    {},
    _root,
    {},
    "_ext_constant_yield_of_cattle_milk",
)


@component.add(
    name="YIELD_OF_GOATS_MILK",
    units="t/number_animals",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_yield_of_goats_milk"},
)
def yield_of_goats_milk():
    """
    Yields of livestock animals. Based on data from FAO (at WORLD level Excel file: "Animals_number_prodcution_WORLD_clean"
    """
    return _ext_constant_yield_of_goats_milk()


_ext_constant_yield_of_goats_milk = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "YIELD_OF_GOATS_MILK",
    {},
    _root,
    {},
    "_ext_constant_yield_of_goats_milk",
)


@component.add(
    name="YIELD_OF_HEN_EGGS",
    units="t/number_animals",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_yield_of_hen_eggs"},
)
def yield_of_hen_eggs():
    """
    Yields of livestock animals. Based on data from FAO (at WORLD level Excel file: "Animals_number_prodcution_WORLD_clean"
    """
    return _ext_constant_yield_of_hen_eggs()


_ext_constant_yield_of_hen_eggs = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "YIELD_OF_HEN_EGGS",
    {},
    _root,
    {},
    "_ext_constant_yield_of_hen_eggs",
)


@component.add(
    name="YIELD_OF_MEAT_BUFFALO",
    units="t/number_animals",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_yield_of_meat_buffalo"},
)
def yield_of_meat_buffalo():
    """
    Yields of livestock animals. Based on data from FAO (at WORLD level Excel file: "Animals_number_prodcution_WORLD_clean"
    """
    return _ext_constant_yield_of_meat_buffalo()


_ext_constant_yield_of_meat_buffalo = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "YIELD_OF_MEAT_BUFFALO",
    {},
    _root,
    {},
    "_ext_constant_yield_of_meat_buffalo",
)


@component.add(
    name="YIELD_OF_MEAT_CATTLE",
    units="t/number_animals",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_yield_of_meat_cattle"},
)
def yield_of_meat_cattle():
    """
    Yields of livestock animals. Based on data from FAO (at WORLD level Excel file: "Animals_number_prodcution_WORLD_clean"
    """
    return _ext_constant_yield_of_meat_cattle()


_ext_constant_yield_of_meat_cattle = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "YIELD_OF_MEAT_CATTLE",
    {},
    _root,
    {},
    "_ext_constant_yield_of_meat_cattle",
)


@component.add(
    name="YIELD_OF_MEAT_CHICKENS",
    units="t/number_animals",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_yield_of_meat_chickens"},
)
def yield_of_meat_chickens():
    """
    Yields of livestock animals. Based on data from FAO (at WORLD level Excel file: "Animals_number_prodcution_WORLD_clean"
    """
    return _ext_constant_yield_of_meat_chickens()


_ext_constant_yield_of_meat_chickens = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "YIELD_OF_MEAT_CHICKENS",
    {},
    _root,
    {},
    "_ext_constant_yield_of_meat_chickens",
)


@component.add(
    name="YIELD_OF_MEAT_GOAT",
    units="t/number_animals",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_yield_of_meat_goat"},
)
def yield_of_meat_goat():
    """
    Yields of livestock animals. Based on data from FAO (at WORLD level Excel file: "Animals_number_prodcution_WORLD_clean"
    """
    return _ext_constant_yield_of_meat_goat()


_ext_constant_yield_of_meat_goat = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "YIELD_OF_MEAT_GOAT",
    {},
    _root,
    {},
    "_ext_constant_yield_of_meat_goat",
)


@component.add(
    name="YIELD_OF_MEAT_PIG",
    units="t/number_animals",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_yield_of_meat_pig"},
)
def yield_of_meat_pig():
    """
    Yields of livestock animals. Based on data from FAO (at WORLD level Excel file: "Animals_number_prodcution_WORLD_clean"
    """
    return _ext_constant_yield_of_meat_pig()


_ext_constant_yield_of_meat_pig = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "YIELD_OF_MEAT_PIG",
    {},
    _root,
    {},
    "_ext_constant_yield_of_meat_pig",
)


@component.add(
    name="YIELD_OF_MEAT_SHEEP",
    units="t/number_animals",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_yield_of_meat_sheep"},
)
def yield_of_meat_sheep():
    """
    Yields of livestock animals. Based on data from FAO (at WORLD level Excel file: "Animals_number_prodcution_WORLD_clean"
    """
    return _ext_constant_yield_of_meat_sheep()


_ext_constant_yield_of_meat_sheep = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "YIELD_OF_MEAT_SHEEP",
    {},
    _root,
    {},
    "_ext_constant_yield_of_meat_sheep",
)


@component.add(
    name="YIELD_OF_SHEEP_MILK",
    units="t/number_animals",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_yield_of_sheep_milk"},
)
def yield_of_sheep_milk():
    """
    Yields of livestock animals. Based on data from FAO (at WORLD level Excel file: "Animals_number_prodcution_WORLD_clean"
    """
    return _ext_constant_yield_of_sheep_milk()


_ext_constant_yield_of_sheep_milk = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "YIELD_OF_SHEEP_MILK",
    {},
    _root,
    {},
    "_ext_constant_yield_of_sheep_milk",
)
