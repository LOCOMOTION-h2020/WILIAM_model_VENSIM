"""
Module land_and_water.land.demand_of_land_products
Translated using PySD version 3.10.0
"""


@component.add(
    name="crops_demanded_for_energy",
    units="t/Year",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "crops_demanded_for_energy_converted_to_tonnes": 1,
        "land_products_used_for_energy_percentages": 1,
    },
)
def crops_demanded_for_energy():
    """
    all the land products demanded and used for energy
    """
    return (
        crops_demanded_for_energy_converted_to_tonnes()
        * land_products_used_for_energy_percentages()
    )


@component.add(
    name="crops_demanded_for_energy_converted_to_tonnes",
    units="t/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "energy_demanded_from_agriculture_products": 1,
        "energy_to_land_products_conversion_factor": 1,
    },
)
def crops_demanded_for_energy_converted_to_tonnes():
    """
    agriculture products demanded for energy with tonnes unit
    """
    return (
        energy_demanded_from_agriculture_products()
        / energy_to_land_products_conversion_factor()
    )


@component.add(
    name="crops_demanded_for_energy_world",
    units="t/Year",
    subscripts=["LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"crops_demanded_for_energy": 1},
)
def crops_demanded_for_energy_world():
    """
    global quantity of land products used for energy
    """
    return sum(
        crops_demanded_for_energy().rename({"REGIONS_9_I": "REGIONS_9_I!"}),
        dim=["REGIONS_9_I!"],
    )


@component.add(
    name="energy_demanded_from_agriculture_products",
    units="EJ/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_landwater": 1,
        "pe_by_commodity_dem": 1,
        "imv_pe_by_commodity_agriculture_products_constant_with_variation": 1,
    },
)
def energy_demanded_from_agriculture_products():
    """
    agriculture products demanded for energy
    """
    return if_then_else(
        switch_landwater() == 1,
        lambda: pe_by_commodity_dem()
        .loc[:, "PE_agriculture_products"]
        .reset_coords(drop=True),
        lambda: imv_pe_by_commodity_agriculture_products_constant_with_variation(),
    )


@component.add(
    name="energy_demanded_from_forestry_products",
    units="EJ/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_landwater": 1,
        "pe_by_commodity": 1,
        "imv_pe_by_commodity_forestry_products_constant_with_variation": 1,
    },
)
def energy_demanded_from_forestry_products():
    return if_then_else(
        switch_landwater() == 1,
        lambda: pe_by_commodity()
        .loc[:, "PE_forestry_products"]
        .reset_coords(drop=True),
        lambda: imv_pe_by_commodity_forestry_products_constant_with_variation(),
    )


@component.add(
    name="exogenous_output_real_9R_construction_sector",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "exo_output_real_for_construction_sector": 1},
)
def exogenous_output_real_9r_construction_sector():
    return exo_output_real_for_construction_sector(time())


@component.add(
    name="exogenous_output_real_9R_forrestry_sector",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "exo_output_real_for_forestry_sector": 1},
)
def exogenous_output_real_9r_forrestry_sector():
    """
    Output real for forestry sector constant values with variation during time for 9 regions
    """
    return exo_output_real_for_forestry_sector(time())


@component.add(
    name="exogenous_output_real_9R_manufacture_wood_sector",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "exo_output_real_for_manufacture_wood_sector": 1},
)
def exogenous_output_real_9r_manufacture_wood_sector():
    return exo_output_real_for_manufacture_wood_sector(time())


@component.add(
    name="imv_PE_by_commodity_agriculture_products_constant_with_variation",
    units="EJ/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 2,
        "time_historical_data_land_module": 1,
        "imv_pe_by_commodity_agriculture_products_constant": 1,
        "exo_biofuels_initial": 1,
        "exo_energy_demanded_biofuels": 1,
    },
)
def imv_pe_by_commodity_agriculture_products_constant_with_variation():
    """
    PE by commidity agriculture products constant values with variation during time for 9 regions
    """
    return if_then_else(
        time() < time_historical_data_land_module(),
        lambda: imv_pe_by_commodity_agriculture_products_constant(time()),
        lambda: exo_biofuels_initial() + exo_energy_demanded_biofuels(),
    )


@component.add(
    name="imv_PE_by_commodity_forestry_products_constant_with_variation",
    units="EJ/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "imv_pe_by_commodity_forestry_products": 1},
)
def imv_pe_by_commodity_forestry_products_constant_with_variation():
    """
    PE by commidity forestry products constant values with variation during time for 9 regions
    """
    return imv_pe_by_commodity_forestry_products(time())


@component.add(
    name="land_products_demanded",
    units="t/Year",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "land_products_demanded_before_losses": 1,
        "loss_factor_of_land_products": 1,
    },
)
def land_products_demanded():
    """
    land_products_demanded
    """
    return land_products_demanded_before_losses() * loss_factor_of_land_products()


@component.add(
    name="land_products_demanded_before_losses",
    units="t/Year",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "crops_demanded_for_energy": 11,
        "land_products_demanded_for_food_before_losses": 10,
        "percent_of_land_products_for_other_uses": 10,
        "wood_demanded_for_energy_converted_to_tonnes": 1,
        "roundwood_demanded_for_industry": 1,
        "residues_of_forests_demanded_for_industry": 1,
    },
)
def land_products_demanded_before_losses():
    """
    land products demanded for food, energy, and industry by region and each type of land product
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
        },
        ["REGIONS_9_I", "LAND_PRODUCTS_I"],
    )
    value.loc[:, ["CORN"]] = (
        (
            (
                crops_demanded_for_energy().loc[:, "CORN"].reset_coords(drop=True)
                + land_products_demanded_for_food_before_losses()
                .loc[:, "CORN"]
                .reset_coords(drop=True)
            )
            * (1 + (1 - float(percent_of_land_products_for_other_uses().loc["CORN"])))
        )
        .expand_dims({"LAND_PRODUCTS_I": ["CORN"]}, 1)
        .values
    )
    value.loc[:, ["RICE"]] = (
        (
            (
                crops_demanded_for_energy().loc[:, "RICE"].reset_coords(drop=True)
                + land_products_demanded_for_food_before_losses()
                .loc[:, "RICE"]
                .reset_coords(drop=True)
            )
            * (1 + (1 - float(percent_of_land_products_for_other_uses().loc["CORN"])))
        )
        .expand_dims({"LAND_PRODUCTS_I": ["RICE"]}, 1)
        .values
    )
    value.loc[:, ["CEREALS_OTHER"]] = (
        (
            (
                crops_demanded_for_energy()
                .loc[:, "CEREALS_OTHER"]
                .reset_coords(drop=True)
                + land_products_demanded_for_food_before_losses()
                .loc[:, "CEREALS_OTHER"]
                .reset_coords(drop=True)
            )
            * (1 + (1 - float(percent_of_land_products_for_other_uses().loc["CORN"])))
        )
        .expand_dims({"LAND_PRODUCTS_I": ["CEREALS_OTHER"]}, 1)
        .values
    )
    value.loc[:, ["TUBERS"]] = (
        (
            (
                crops_demanded_for_energy().loc[:, "TUBERS"].reset_coords(drop=True)
                + land_products_demanded_for_food_before_losses()
                .loc[:, "TUBERS"]
                .reset_coords(drop=True)
            )
            * (1 + (1 - float(percent_of_land_products_for_other_uses().loc["CORN"])))
        )
        .expand_dims({"LAND_PRODUCTS_I": ["TUBERS"]}, 1)
        .values
    )
    value.loc[:, ["SOY"]] = (
        (
            (
                crops_demanded_for_energy().loc[:, "SOY"].reset_coords(drop=True)
                + land_products_demanded_for_food_before_losses()
                .loc[:, "SOY"]
                .reset_coords(drop=True)
            )
            * (1 + (1 - float(percent_of_land_products_for_other_uses().loc["CORN"])))
        )
        .expand_dims({"LAND_PRODUCTS_I": ["SOY"]}, 1)
        .values
    )
    value.loc[:, ["PULSES_NUTS"]] = (
        (
            (
                crops_demanded_for_energy()
                .loc[:, "PULSES_NUTS"]
                .reset_coords(drop=True)
                + land_products_demanded_for_food_before_losses()
                .loc[:, "PULSES_NUTS"]
                .reset_coords(drop=True)
            )
            * (1 + (1 - float(percent_of_land_products_for_other_uses().loc["CORN"])))
        )
        .expand_dims({"LAND_PRODUCTS_I": ["PULSES_NUTS"]}, 1)
        .values
    )
    value.loc[:, ["OILCROPS"]] = (
        (
            (
                crops_demanded_for_energy().loc[:, "OILCROPS"].reset_coords(drop=True)
                + land_products_demanded_for_food_before_losses()
                .loc[:, "OILCROPS"]
                .reset_coords(drop=True)
            )
            * (1 + (1 - float(percent_of_land_products_for_other_uses().loc["CORN"])))
        )
        .expand_dims({"LAND_PRODUCTS_I": ["OILCROPS"]}, 1)
        .values
    )
    value.loc[:, ["SUGAR_CROPS"]] = (
        (
            (
                crops_demanded_for_energy()
                .loc[:, "SUGAR_CROPS"]
                .reset_coords(drop=True)
                + land_products_demanded_for_food_before_losses()
                .loc[:, "SUGAR_CROPS"]
                .reset_coords(drop=True)
            )
            * (1 + (1 - float(percent_of_land_products_for_other_uses().loc["CORN"])))
        )
        .expand_dims({"LAND_PRODUCTS_I": ["SUGAR_CROPS"]}, 1)
        .values
    )
    value.loc[:, ["FRUITS_VEGETABLES"]] = (
        (
            (
                crops_demanded_for_energy()
                .loc[:, "FRUITS_VEGETABLES"]
                .reset_coords(drop=True)
                + land_products_demanded_for_food_before_losses()
                .loc[:, "FRUITS_VEGETABLES"]
                .reset_coords(drop=True)
            )
            * (1 + (1 - float(percent_of_land_products_for_other_uses().loc["CORN"])))
        )
        .expand_dims({"LAND_PRODUCTS_I": ["FRUITS_VEGETABLES"]}, 1)
        .values
    )
    value.loc[:, ["BIOFUEL_2GCROP"]] = (
        crops_demanded_for_energy()
        .loc[:, "BIOFUEL_2GCROP"]
        .reset_coords(drop=True)
        .expand_dims({"LAND_PRODUCTS_I": ["BIOFUEL_2GCROP"]}, 1)
        .values
    )
    value.loc[:, ["OTHER_CROPS"]] = (
        (
            (
                crops_demanded_for_energy()
                .loc[:, "OTHER_CROPS"]
                .reset_coords(drop=True)
                + land_products_demanded_for_food_before_losses()
                .loc[:, "OTHER_CROPS"]
                .reset_coords(drop=True)
            )
            * (1 + (1 - float(percent_of_land_products_for_other_uses().loc["CORN"])))
        )
        .expand_dims({"LAND_PRODUCTS_I": ["OTHER_CROPS"]}, 1)
        .values
    )
    value.loc[:, ["WOOD"]] = (
        (
            roundwood_demanded_for_industry()
            + wood_demanded_for_energy_converted_to_tonnes()
        )
        .expand_dims({"LAND_PRODUCTS_I": ["WOOD"]}, 1)
        .values
    )
    value.loc[:, ["RESIDUES"]] = (
        residues_of_forests_demanded_for_industry()
        .expand_dims({"LAND_PRODUCTS_I": ["RESIDUES"]}, 1)
        .values
    )
    return value


@component.add(
    name="land_products_demanded_world",
    units="t/Year",
    subscripts=["LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"land_products_demanded": 1},
)
def land_products_demanded_world():
    """
    land products demanded for food and energy for all regions
    """
    return sum(
        land_products_demanded().rename({"REGIONS_9_I": "REGIONS_9_I!"}),
        dim=["REGIONS_9_I!"],
    )


@component.add(
    name="land_products_demanded_world_before_losses",
    units="t/Year",
    subscripts=["LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"land_products_demanded_before_losses": 1},
)
def land_products_demanded_world_before_losses():
    return sum(
        land_products_demanded_before_losses().rename({"REGIONS_9_I": "REGIONS_9_I!"}),
        dim=["REGIONS_9_I!"],
    )


@component.add(
    name="output_real_9R_for_forestry_sector",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_landwater": 1,
        "output_real_9r": 1,
        "exogenous_output_real_9r_forrestry_sector": 1,
    },
)
def output_real_9r_for_forestry_sector():
    """
    Output real for forestry sector by region
    """
    return if_then_else(
        switch_landwater() == 1,
        lambda: output_real_9r().loc[:, "FORESTRY"].reset_coords(drop=True),
        lambda: exogenous_output_real_9r_forrestry_sector(),
    )


@component.add(
    name="output_real_of_wood_manufacturing_and_construction_sectors",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_landwater": 1,
        "output_real_9r": 2,
        "exogenous_output_real_9r_manufacture_wood_sector": 1,
        "exogenous_output_real_9r_construction_sector": 1,
    },
)
def output_real_of_wood_manufacturing_and_construction_sectors():
    """
    Output real for construction and wood manufacturing, the main sectors that demand industrial wood
    """
    return if_then_else(
        switch_landwater() == 1,
        lambda: output_real_9r().loc[:, "MANUFACTURE_WOOD"].reset_coords(drop=True)
        + output_real_9r().loc[:, "CONSTRUCTION"].reset_coords(drop=True),
        lambda: exogenous_output_real_9r_manufacture_wood_sector()
        + exogenous_output_real_9r_construction_sector(),
    )


@component.add(
    name="residues_of_forests_demanded_for_industry",
    units="t/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "output_real_9r_for_forestry_sector": 1,
        "intensities_of_residues_for_industry": 1,
    },
)
def residues_of_forests_demanded_for_industry():
    """
    The global quantity of wood waste demanded for industry by region
    """
    return output_real_9r_for_forestry_sector() * intensities_of_residues_for_industry()


@component.add(
    name="roundwood_demanded_for_energy_and_industry",
    units="t/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "wood_demanded_for_energy_converted_to_tonnes": 1,
        "wood_demanded_for_industry": 1,
    },
)
def roundwood_demanded_for_energy_and_industry():
    """
    wood demanded for energy and industry
    """
    return wood_demanded_for_energy_converted_to_tonnes() + wood_demanded_for_industry()


@component.add(
    name="roundwood_demanded_for_industry",
    units="t/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "output_real_of_wood_manufacturing_and_construction_sectors": 1,
        "intensities_of_wood_for_industry": 1,
    },
)
def roundwood_demanded_for_industry():
    """
    The global quantity of wood demanded for industry by region
    """
    return (
        output_real_of_wood_manufacturing_and_construction_sectors()
        * intensities_of_wood_for_industry()
    )


@component.add(
    name="roundwood_demanded_world",
    units="t/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"roundwood_demanded_for_energy_and_industry": 1},
)
def roundwood_demanded_world():
    """
    global quantity of wood demanded for all regions
    """
    return sum(
        roundwood_demanded_for_energy_and_industry().rename(
            {"REGIONS_9_I": "REGIONS_9_I!"}
        ),
        dim=["REGIONS_9_I!"],
    )


@component.add(
    name="wood_demanded_for_energy_converted_to_tonnes",
    units="t/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "exo_increment_demand_biomass": 1,
        "energy_demanded_from_forestry_products": 1,
        "energy_to_wood_conversion_factor": 1,
    },
)
def wood_demanded_for_energy_converted_to_tonnes():
    """
    forestry products demanded for energy with tonnes unit
    """
    return (
        exo_increment_demand_biomass()
        * energy_demanded_from_forestry_products()
        / energy_to_wood_conversion_factor()
    )


@component.add(
    name="wood_demanded_for_energy_world",
    units="t/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"wood_demanded_for_energy_converted_to_tonnes": 1},
)
def wood_demanded_for_energy_world():
    """
    wood demanded for energy for all regions
    """
    return sum(
        wood_demanded_for_energy_converted_to_tonnes().rename(
            {"REGIONS_9_I": "REGIONS_9_I!"}
        ),
        dim=["REGIONS_9_I!"],
    )


@component.add(
    name="wood_demanded_for_industry",
    units="t/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "residues_of_forests_demanded_for_industry": 1,
        "roundwood_demanded_for_industry": 1,
    },
)
def wood_demanded_for_industry():
    """
    global quantity of wood demand for industry
    """
    return (
        residues_of_forests_demanded_for_industry() + roundwood_demanded_for_industry()
    )


@component.add(
    name="wood_demanded_for_industry_world",
    units="t/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"wood_demanded_for_industry": 1},
)
def wood_demanded_for_industry_world():
    """
    wood demanded for industry for all regions
    """
    return sum(
        wood_demanded_for_industry().rename({"REGIONS_9_I": "REGIONS_9_I!"}),
        dim=["REGIONS_9_I!"],
    )
