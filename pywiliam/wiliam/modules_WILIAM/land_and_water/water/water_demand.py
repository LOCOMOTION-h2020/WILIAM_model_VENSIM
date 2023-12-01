"""
Module land_and_water.water.water_demand
Translated using PySD version 3.10.0
"""


@component.add(
    name="blue_water_available_for_agriculture",
    units="hm3",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "blue_water_used_for_households": 2,
        "blue_water_used_by_industries": 2,
        "water_available_by_region": 2,
        "blue_water_demand_for_agriculture_by_gdp": 2,
    },
)
def blue_water_available_for_agriculture():
    """
    The rest of the water goes to agriculture (but we do not gime more than demanded)
    """
    return if_then_else(
        blue_water_used_for_households() + blue_water_used_by_industries()
        >= water_available_by_region(),
        lambda: xr.DataArray(
            0, {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]}, ["REGIONS_35_I"]
        ),
        lambda: np.minimum(
            water_available_by_region()
            - blue_water_used_by_industries()
            - blue_water_used_for_households(),
            blue_water_demand_for_agriculture_by_gdp()
            .loc[:, "CROPS"]
            .reset_coords(drop=True)
            + blue_water_demand_for_agriculture_by_gdp()
            .loc[:, "ANIMALS"]
            .reset_coords(drop=True),
        ),
    )


@component.add(
    name="blue_water_demand_by_industries",
    units="hm3",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "total_demand_blue_water_by_region": 1,
        "blue_water_demand_for_agriculture_by_gdp": 2,
        "blue_water_demand_from_households": 1,
    },
)
def blue_water_demand_by_industries():
    """
    Total amount of the blue and green water, for the industrial sectors, for the 35 regions. REVER!!!!
    """
    return (
        total_demand_blue_water_by_region()
        - blue_water_demand_for_agriculture_by_gdp()
        .loc[:, "CROPS"]
        .reset_coords(drop=True)
        - blue_water_demand_for_agriculture_by_gdp()
        .loc[:, "ANIMALS"]
        .reset_coords(drop=True)
        - blue_water_demand_from_households()
    )


@component.add(
    name="blue_water_demand_by_sector",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "time_historical_data_land_module": 1,
        "blue_water_demand_trends": 2,
        "factor_of_economic_output_for_water": 1,
    },
)
def blue_water_demand_by_sector():
    return if_then_else(
        time() <= time_historical_data_land_module(),
        lambda: blue_water_demand_trends(),
        lambda: blue_water_demand_trends() * factor_of_economic_output_for_water(),
    )


@component.add(
    name="blue_water_demand_for_agriculture_by_GDP",
    units="hm3",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "blue_water_demand_by_sector": 2,
        "ratio_precipitation_evapotranspiration_by_year": 2,
    },
)
def blue_water_demand_for_agriculture_by_gdp():
    """
    Total amount of the blue water, only for the agricultural sectors (Crops, Animals, Forestry and Fishing), for the 35 regions.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "SECTORS_I": _subscript_dict["SECTORS_I"],
        },
        ["REGIONS_35_I", "SECTORS_I"],
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, ["CROPS"]] = False
    except_subs.loc[:, ["ANIMALS"]] = False
    value.values[except_subs.values] = 0
    value.loc[:, ["CROPS"]] = (
        zidz(
            blue_water_demand_by_sector().loc[:, "CROPS"].reset_coords(drop=True),
            ratio_precipitation_evapotranspiration_by_year()
            .loc[_subscript_dict["REGIONS_35_I"]]
            .rename({"REGIONS_36_I": "REGIONS_35_I"}),
        )
        .expand_dims({"CLUSTER_AGRICULTURE_FISHING_FORESTRY": ["CROPS"]}, 1)
        .values
    )
    value.loc[:, ["ANIMALS"]] = (
        zidz(
            blue_water_demand_by_sector().loc[:, "ANIMALS"].reset_coords(drop=True),
            ratio_precipitation_evapotranspiration_by_year()
            .loc[_subscript_dict["REGIONS_35_I"]]
            .rename({"REGIONS_36_I": "REGIONS_35_I"}),
        )
        .expand_dims({"CLUSTER_AGRICULTURE_FISHING_FORESTRY": ["ANIMALS"]}, 1)
        .values
    )
    return value


@component.add(
    name="blue_water_demand_from_households",
    units="hm3",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"water_population_factor_2005": 1, "population_35r_for_water": 1},
)
def blue_water_demand_from_households():
    """
    Blue water values for the households, per capita, for the 35 regions, changing in time.
    """
    return water_population_factor_2005() * population_35r_for_water()


@component.add(
    name="blue_water_demand_trends",
    units="hm3",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_blue_water_demand_trends": 1},
    other_deps={
        "_integ_blue_water_demand_trends": {
            "initial": {"initial_blue_water_region_sect": 1},
            "step": {"historical_blue_water_growth_trends": 1},
        }
    },
)
def blue_water_demand_trends():
    """
    Blue water intensity values, for the 35 regions and 62 sectors, changing in time.
    """
    return _integ_blue_water_demand_trends()


_integ_blue_water_demand_trends = Integ(
    lambda: historical_blue_water_growth_trends(),
    lambda: initial_blue_water_region_sect(),
    "_integ_blue_water_demand_trends",
)


@component.add(
    name="blue_water_used_by_industries",
    units="hm3",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "blue_water_demand_for_agriculture_by_gdp": 2,
        "blue_water_demand_by_industries": 2,
        "blue_water_used_for_households": 2,
        "water_available_by_region": 2,
    },
)
def blue_water_used_by_industries():
    return if_then_else(
        blue_water_demand_for_agriculture_by_gdp()
        .loc[:, "CROPS"]
        .reset_coords(drop=True)
        + blue_water_demand_for_agriculture_by_gdp()
        .loc[:, "ANIMALS"]
        .reset_coords(drop=True)
        + blue_water_demand_by_industries()
        < water_available_by_region() - blue_water_used_for_households(),
        lambda: blue_water_demand_by_industries(),
        lambda: water_available_by_region() - blue_water_used_for_households(),
    )


@component.add(
    name="blue_water_used_for_households",
    units="hm3",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"water_available_by_region": 2, "blue_water_demand_from_households": 2},
)
def blue_water_used_for_households():
    """
    priority to households demand in the distribution of water
    """
    return if_then_else(
        water_available_by_region() >= blue_water_demand_from_households(),
        lambda: blue_water_demand_from_households(),
        lambda: water_available_by_region(),
    )


@component.add(
    name="effective_blue_water_demanded_for_agriculture",
    units="hm3",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"blue_water_demand_for_agriculture_by_gdp": 2, "water_efficiency": 1},
)
def effective_blue_water_demanded_for_agriculture():
    return zidz(
        blue_water_demand_for_agriculture_by_gdp()
        .loc[:, "CROPS"]
        .reset_coords(drop=True)
        + blue_water_demand_for_agriculture_by_gdp()
        .loc[:, "ANIMALS"]
        .reset_coords(drop=True),
        water_efficiency(),
    )


@component.add(
    name="factor_of_economic_output_for_water",
    units="DMNL",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_landwater": 1,
        "gdp_for_water": 1,
        "gdp_real_35r_until_2019": 1,
        "gdp_by_oekstra_for_water": 1,
        "gdp_oekstra_2019": 1,
    },
)
def factor_of_economic_output_for_water():
    """
    Factor con compensate the estimations of water demand done with the paper by Oekstra et al. with scenarions of growing economic output
    """
    return if_then_else(
        switch_landwater() == 0,
        lambda: xr.DataArray(
            1, {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]}, ["REGIONS_35_I"]
        ),
        lambda: zidz(gdp_for_water(), gdp_by_oekstra_for_water())
        * zidz(gdp_oekstra_2019(), gdp_real_35r_until_2019()),
    )


@component.add(
    name="GDP_by_Oekstra_for_water",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_gdp_by_oekstra_for_water": 1},
    other_deps={
        "_integ_gdp_by_oekstra_for_water": {
            "initial": {"gdp_oekstra_initial": 1},
            "step": {"gdp_oekstra_growth": 1},
        }
    },
)
def gdp_by_oekstra_for_water():
    return _integ_gdp_by_oekstra_for_water()


_integ_gdp_by_oekstra_for_water = Integ(
    lambda: gdp_oekstra_growth(),
    lambda: gdp_oekstra_initial(),
    "_integ_gdp_by_oekstra_for_water",
)


@component.add(
    name="GDP_for_water",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"gross_domestic_product_real_demand_side": 1},
)
def gdp_for_water():
    return gross_domestic_product_real_demand_side()


@component.add(
    name="GDP_oekstra_growth",
    units="Mdollars_2015/Year/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"gdp_variation_by_oekstra": 1},
)
def gdp_oekstra_growth():
    return gdp_variation_by_oekstra()


@component.add(
    name="green_water_region_sector",
    units="hm3",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_green_water_region_sector": 1},
    other_deps={
        "_integ_green_water_region_sector": {
            "initial": {"initial_green_water_region_sect": 1},
            "step": {"historical_green_water_of_sectors_by_region": 1},
        }
    },
)
def green_water_region_sector():
    """
    Green water intensity values, for the 35 regions and 62 sectors, changing in time.
    """
    return _integ_green_water_region_sector()


_integ_green_water_region_sector = Integ(
    lambda: historical_green_water_of_sectors_by_region(),
    lambda: initial_green_water_region_sect(),
    "_integ_green_water_region_sector",
)


@component.add(
    name="historical_blue_water_growth_trends",
    units="hm3",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 2,
        "initial_blue_water_region_sect": 1,
        "variation_linear_blue_water_region_sect": 1,
    },
)
def historical_blue_water_growth_trends():
    """
    Variation of water demand by type, sector and year.
    """
    return if_then_else(
        time() > 2005,
        lambda: if_then_else(
            time() < 2050,
            lambda: variation_linear_blue_water_region_sect()
            * initial_blue_water_region_sect(),
            lambda: xr.DataArray(
                0,
                {
                    "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                    "SECTORS_I": _subscript_dict["SECTORS_I"],
                },
                ["REGIONS_35_I", "SECTORS_I"],
            ),
        ),
        lambda: xr.DataArray(
            0,
            {
                "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                "SECTORS_I": _subscript_dict["SECTORS_I"],
            },
            ["REGIONS_35_I", "SECTORS_I"],
        ),
    )


@component.add(
    name="historical_green_water_of_sectors_by_region",
    units="hm3",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 2,
        "variation_linear_green_water_region_sect": 1,
        "initial_green_water_region_sect": 1,
    },
)
def historical_green_water_of_sectors_by_region():
    """
    Variation of green water demand by type, sector and year.
    """
    return if_then_else(
        time() > 2005,
        lambda: if_then_else(
            time() < 2050,
            lambda: variation_linear_green_water_region_sect()
            * initial_green_water_region_sect(),
            lambda: xr.DataArray(
                0,
                {
                    "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                    "SECTORS_I": _subscript_dict["SECTORS_I"],
                },
                ["REGIONS_35_I", "SECTORS_I"],
            ),
        ),
        lambda: xr.DataArray(
            0,
            {
                "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                "SECTORS_I": _subscript_dict["SECTORS_I"],
            },
            ["REGIONS_35_I", "SECTORS_I"],
        ),
    )


@component.add(
    name="increase_water_efficiency",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_water_efficiency_sp": 2,
        "objective_water_efficiency_sp": 1,
        "time": 2,
        "year_final_water_efficiency_sp": 2,
        "year_initial_water_efficiency_sp": 2,
    },
)
def increase_water_efficiency():
    return if_then_else(
        switch_water_efficiency_sp() == 0,
        lambda: 0,
        lambda: if_then_else(
            np.logical_and(
                switch_water_efficiency_sp() == 1,
                np.logical_or(
                    time() < year_initial_water_efficiency_sp(),
                    time() > year_final_water_efficiency_sp(),
                ),
            ),
            lambda: 0,
            lambda: objective_water_efficiency_sp()
            / (year_final_water_efficiency_sp() - year_initial_water_efficiency_sp()),
        ),
    )


@component.add(
    name="INITIAL_BLUE_WATER_REGION_SECT",
    units="hm3",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_blue_water_region_sect"},
)
def initial_blue_water_region_sect():
    """
    Load the initial (2005) values of the Blue Water demand, for the 35 Regions and 62 Sectors.
    """
    return _ext_constant_initial_blue_water_region_sect()


_ext_constant_initial_blue_water_region_sect = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Water",
    "Blue2005",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
    "_ext_constant_initial_blue_water_region_sect",
)


@component.add(
    name="initial_blue_water_use_all_sectors",
    units="hm3",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"initial_blue_water_region_sect": 1},
)
def initial_blue_water_use_all_sectors():
    return sum(
        initial_blue_water_region_sect().rename({"SECTORS_I": "SECTORS_I!"}),
        dim=["SECTORS_I!"],
    )


@component.add(
    name="initial_share_water_per_sector",
    units="DMNL",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "initial_blue_water_region_sect": 1,
        "initial_blue_water_use_all_sectors": 1,
    },
)
def initial_share_water_per_sector():
    return zidz(
        initial_blue_water_region_sect(),
        initial_blue_water_use_all_sectors().expand_dims(
            {"SECTORS_I": _subscript_dict["SECTORS_I"]}, 1
        ),
    )


@component.add(
    name="initial_water_per_sector_FAO",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "initial_time": 1,
        "historical_water_use_fao": 1,
        "initial_share_water_per_sector": 1,
    },
)
def initial_water_per_sector_fao():
    """
    HISTORICAL_WATER_USE_FAO[REGIONS 35 I](INITIAL_TIME)*INITIAL SHARE WATER PER SECTOR[REGIONS 35 I,SECTORS I]
    """
    return historical_water_use_fao(initial_time()) * initial_share_water_per_sector()


@component.add(
    name="intensity_green_water_region_sector",
    units="hm3/Mdollars",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_landwater": 1,
        "green_water_region_sector": 2,
        "base_output_real": 2,
        "output_real": 2,
    },
)
def intensity_green_water_region_sector():
    """
    Total amount of water demand from the Blue and Green Water, for the 35 regions and sectors. IF_THEN_ELSE (SWITCH_LANDWATER = 0 , (intensity_blue_water_region_sector[REGIONS 35 I,SECTORS I]+intensity_green_water_region_sector[REGIONS 35 I,SECTORS I] )*BASE OUTPUT REAL[REGIONS 35 I,SECTORS I], (intensity_blue_water_region_sector[REGIONS 35 I,SECTORS I]+intensity_green_water_region_sector[REGIONS 35 I,SECTORS I] )*output real[REGIONS 35 I,SECTORS I] )
    """
    return if_then_else(
        switch_landwater() == 0,
        lambda: xr.DataArray(
            1,
            {
                "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                "SECTORS_I": _subscript_dict["SECTORS_I"],
            },
            ["REGIONS_35_I", "SECTORS_I"],
        ),
        lambda: if_then_else(
            base_output_real() > 0,
            lambda: green_water_region_sector() / base_output_real(),
            lambda: if_then_else(
                output_real() > 0,
                lambda: green_water_region_sector() / output_real(),
                lambda: xr.DataArray(
                    1,
                    {
                        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                        "SECTORS_I": _subscript_dict["SECTORS_I"],
                    },
                    ["REGIONS_35_I", "SECTORS_I"],
                ),
            ),
        ),
    )


@component.add(
    name="irrigated_land_changes_due_water_availability",
    units="km2",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "land_use_area_by_region": 1,
        "water_agric_9r_variation_in_percentage": 1,
    },
)
def irrigated_land_changes_due_water_availability():
    """
    Varia na mesma proporção que o water availability for agriculture
    """
    return (
        land_use_area_by_region().loc[:, "CROPLAND_IRRIGATED"].reset_coords(drop=True)
        * water_agric_9r_variation_in_percentage()
    )


@component.add(
    name="population_35R_for_water",
    units="person",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_landwater": 1,
        "population_35_regions": 1,
        "time": 1,
        "exo_population_35r": 1,
    },
)
def population_35r_for_water():
    return if_then_else(
        switch_landwater() == 1,
        lambda: population_35_regions(),
        lambda: exo_population_35r(time()),
    )


@component.add(
    name="ratio_of_water_available_for_agriculture",
    units="DMNL",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "water_available_by_region": 1,
        "blue_water_used_for_households": 1,
        "blue_water_used_by_industries": 1,
        "blue_water_demand_for_agriculture_by_gdp": 2,
    },
)
def ratio_of_water_available_for_agriculture():
    """
    Ratio of water available for agriculture indicates if there is water available for agriculture after other uses (households and industries), including the future projections of water demand and climate.
    """
    return zidz(
        water_available_by_region()
        - blue_water_used_for_households()
        - blue_water_used_by_industries(),
        blue_water_demand_for_agriculture_by_gdp()
        .loc[:, "CROPS"]
        .reset_coords(drop=True)
        + blue_water_demand_for_agriculture_by_gdp()
        .loc[:, "ANIMALS"]
        .reset_coords(drop=True),
    )


@component.add(
    name="total_blue_water_demand_9R",
    units="hm3",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"water_demand_region_matrix": 1},
)
def total_blue_water_demand_9r():
    """
    Total water demand for the 9 LOCOMOTION regions.
    """
    return sum(
        water_demand_region_matrix().rename({"REGIONS_35_I": "REGIONS_35_I!"}),
        dim=["REGIONS_35_I!"],
    )


@component.add(
    name="total_demand_blue_water_by_region",
    units="hm3",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "blue_water_demand_by_sector": 1,
        "blue_water_demand_from_households": 1,
    },
)
def total_demand_blue_water_by_region():
    """
    total_demand_blue_water_by_region
    """
    return (
        sum(
            blue_water_demand_by_sector().rename({"SECTORS_I": "SECTORS_I!"}),
            dim=["SECTORS_I!"],
        )
        + blue_water_demand_from_households()
    )


@component.add(
    name="total_use_water_by_area_0_0", comp_type="Constant", comp_subtype="Normal"
)
def total_use_water_by_area_0_0():
    return 1


@component.add(
    name="water_agric_9R_variation_in_percentage",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "water_available_for_agriculture_9r": 1,
        "water_available_for_agriculture_9r_delayed": 1,
    },
)
def water_agric_9r_variation_in_percentage():
    return zidz(
        water_available_for_agriculture_9r(),
        water_available_for_agriculture_9r_delayed(),
    )


@component.add(
    name="water_available_for_agriculture_9R",
    units="hm3",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"water_available_for_agriculture_matrix": 1},
)
def water_available_for_agriculture_9r():
    return sum(
        water_available_for_agriculture_matrix().rename(
            {"REGIONS_35_I": "REGIONS_35_I!"}
        ),
        dim=["REGIONS_35_I!"],
    )


@component.add(
    name="water_available_for_agriculture_9R_delayed",
    units="hm3",
    subscripts=["REGIONS_9_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_water_available_for_agriculture_9r_delayed": 1},
    other_deps={
        "_delayfixed_water_available_for_agriculture_9r_delayed": {
            "initial": {"water_available_for_agriculture_9r": 1},
            "step": {"water_available_for_agriculture_9r": 1},
        }
    },
)
def water_available_for_agriculture_9r_delayed():
    return _delayfixed_water_available_for_agriculture_9r_delayed()


_delayfixed_water_available_for_agriculture_9r_delayed = DelayFixed(
    lambda: water_available_for_agriculture_9r(),
    lambda: 1,
    lambda: water_available_for_agriculture_9r(),
    time_step,
    "_delayfixed_water_available_for_agriculture_9r_delayed",
)


@component.add(
    name="water_available_for_agriculture_matrix",
    units="hm3",
    subscripts=["REGIONS_35_I", "REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"blue_water_available_for_agriculture": 1, "matrix_country_region": 1},
)
def water_available_for_agriculture_matrix():
    return blue_water_available_for_agriculture() * matrix_country_region()


@component.add(
    name="water_demand_region_matrix",
    units="hm3",
    subscripts=["REGIONS_35_I", "REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_demand_blue_water_by_region": 1, "matrix_country_region": 1},
)
def water_demand_region_matrix():
    """
    Matrix to compute the total values for each 9 LOCOMOTION regions.
    """
    return total_demand_blue_water_by_region() * matrix_country_region()


@component.add(
    name="water_efficiency",
    units="DMNL",
    subscripts=["REGIONS_35_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_water_efficiency": 1},
    other_deps={
        "_integ_water_efficiency": {
            "initial": {"initial_water_efficiency": 1},
            "step": {"increase_water_efficiency": 1},
        }
    },
)
def water_efficiency():
    return _integ_water_efficiency()


_integ_water_efficiency = Integ(
    lambda: xr.DataArray(
        increase_water_efficiency(),
        {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
        ["REGIONS_35_I"],
    ),
    lambda: initial_water_efficiency(),
    "_integ_water_efficiency",
)


@component.add(
    name="Water_population_factor_2005",
    units="hm3/Mperson",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"initial_blue_water_region_households": 1, "population_2005": 1},
)
def water_population_factor_2005():
    """
    Function to compute the amount of the water consumed by person. It is needed for the link with the population in the future.
    """
    return initial_blue_water_region_households() / sum(
        population_2005()
        .loc[:, :, _subscript_dict["AGE_CHAIN_I"]]
        .rename({"SEX_I": "SEX_I!", "AGE_COHORTS_I": "AGE_CHAIN_I!"}),
        dim=["SEX_I!", "AGE_CHAIN_I!"],
    )
