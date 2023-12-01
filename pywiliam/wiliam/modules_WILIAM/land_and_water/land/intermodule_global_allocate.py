"""
Module land_and_water.land.intermodule_global_allocate
Translated using PySD version 3.10.0
"""


@component.add(
    name="availability_of_crops_for_energy",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"crops_available_for_energy": 1, "crops_demanded_for_energy": 1},
)
def availability_of_crops_for_energy():
    """
    If demand can be met, availability of crops for energy =1, if it is 0.2, for example, 20% of the demand cannot be met. supply includes international trade
    """
    return zidz(
        sum(
            crops_available_for_energy().rename(
                {"LAND_PRODUCTS_I": "LAND_PRODUCTS_I!"}
            ),
            dim=["LAND_PRODUCTS_I!"],
        ),
        sum(
            crops_demanded_for_energy().rename({"LAND_PRODUCTS_I": "LAND_PRODUCTS_I!"}),
            dim=["LAND_PRODUCTS_I!"],
        ),
    )


@component.add(
    name="availability_of_crops_for_food",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"crops_available_for_food": 1, "land_products_demanded_for_food": 1},
)
def availability_of_crops_for_food():
    """
    If demand can be met, availability of crops for food=1, if it is 0.2, for example, 20% of the demand cannot be met.
    """
    return zidz(
        sum(
            crops_available_for_food().rename({"LAND_PRODUCTS_I": "LAND_PRODUCTS_I!"}),
            dim=["LAND_PRODUCTS_I!"],
        ),
        sum(
            land_products_demanded_for_food().rename(
                {"LAND_PRODUCTS_I": "LAND_PRODUCTS_I!"}
            ),
            dim=["LAND_PRODUCTS_I!"],
        ),
    )


@component.add(
    name="availability_of_forestry_products_for_energy",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "forestry_products_available_for_energy": 1,
        "wood_demanded_for_energy_converted_to_tonnes": 1,
    },
)
def availability_of_forestry_products_for_energy():
    return zidz(
        forestry_products_available_for_energy(),
        wood_demanded_for_energy_converted_to_tonnes(),
    )


@component.add(
    name="availability_of_forestry_products_for_industry",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "forestry_products_available_for_industry": 1,
        "wood_demanded_for_industry": 2,
    },
)
def availability_of_forestry_products_for_industry():
    return zidz(
        forestry_products_available_for_industry() - wood_demanded_for_industry(),
        wood_demanded_for_industry(),
    )


@component.add(
    name="average_availability_of_crops_for_energy_world",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"availability_of_crops_for_energy": 1},
)
def average_availability_of_crops_for_energy_world():
    return sum(
        availability_of_crops_for_energy().rename({"REGIONS_9_I": "REGIONS_9_I!"}),
        dim=["REGIONS_9_I!"],
    ) / len(
        xr.DataArray(
            np.arange(28, len(_subscript_dict["REGIONS_9_I"]) + 28),
            {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
            ["REGIONS_9_I"],
        )
    )


@component.add(
    name="average_availability_of_crops_for_food_world",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"availability_of_crops_for_food": 1},
)
def average_availability_of_crops_for_food_world():
    return sum(
        availability_of_crops_for_food().rename({"REGIONS_9_I": "REGIONS_9_I!"}),
        dim=["REGIONS_9_I!"],
    ) / len(
        xr.DataArray(
            np.arange(28, len(_subscript_dict["REGIONS_9_I"]) + 28),
            {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
            ["REGIONS_9_I"],
        )
    )


@component.add(
    name="change_of_the_share_of_land_products_from_smallholders",
    units="1/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_land_products_global_pool_sp": 1,
        "time": 2,
        "year_initial_land_products_global_pool_sp": 2,
        "year_final_land_products_global_pool_sp": 2,
        "initial_share_of_production_from_smallholders": 1,
        "objective_land_products_global_pool_sp": 1,
    },
)
def change_of_the_share_of_land_products_from_smallholders():
    """
    change of the share of land products protected from global pool "market"
    """
    return if_then_else(
        np.logical_and(
            switch_land_products_global_pool_sp() == 1,
            np.logical_and(
                time() > year_initial_land_products_global_pool_sp(),
                time() < year_final_land_products_global_pool_sp(),
            ),
        ),
        lambda: zidz(
            objective_land_products_global_pool_sp()
            - initial_share_of_production_from_smallholders(),
            year_final_land_products_global_pool_sp()
            - year_initial_land_products_global_pool_sp(),
        ),
        lambda: xr.DataArray(
            0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
        ),
    )


@component.add(
    name="crops_available_for_energy",
    units="t/Year",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"crops_distributed_to_uses": 1},
)
def crops_available_for_energy():
    return (
        crops_distributed_to_uses()
        .loc[:, :, "LP_ENERGY_AGRICULTURAL"]
        .reset_coords(drop=True)
    )


@component.add(
    name="crops_available_for_food",
    units="t/Year",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"crops_distributed_to_uses": 1},
)
def crops_available_for_food():
    return crops_distributed_to_uses().loc[:, :, "LP_FOOD"].reset_coords(drop=True)


@component.add(
    name="crops_demanded_to_uses",
    units="t/Year",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I", "USES_LP_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={"land_products_demanded_for_food": 1, "crops_demanded_for_energy": 1},
)
def crops_demanded_to_uses():
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
            "USES_LP_I": _subscript_dict["USES_LP_I"],
        },
        ["REGIONS_9_I", "LAND_PRODUCTS_I", "USES_LP_I"],
    )
    value.loc[:, :, ["LP_FOOD"]] = (
        land_products_demanded_for_food()
        .expand_dims({"USES_LP_I": ["LP_FOOD"]}, 2)
        .values
    )
    value.loc[:, :, ["LP_INDUSTRY"]] = 0
    value.loc[:, :, ["LP_ENERGY_FORESTRY"]] = 0
    value.loc[:, :, ["LP_ENERGY_AGRICULTURAL"]] = (
        crops_demanded_for_energy()
        .expand_dims({"USES_LP_I": ["LP_ENERGY_AGRICULTURAL"]}, 2)
        .values
    )
    return value


@component.add(
    name="crops_distributed_to_uses",
    units="t/Year",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I", "USES_LP_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "crops_demanded_to_uses": 1,
        "priorities_of_crops_distribution_among_uses_sp": 1,
        "width_of_crops_distribution_among_uses_sp": 1,
        "land_products_available_to_each_region": 1,
    },
)
def crops_distributed_to_uses():
    return allocate_by_priority(
        crops_demanded_to_uses(),
        priorities_of_crops_distribution_among_uses_sp(),
        width_of_crops_distribution_among_uses_sp(),
        land_products_available_to_each_region(),
    )


@component.add(
    name="crops_distributed_to_uses_world",
    units="t/Year",
    subscripts=["LAND_PRODUCTS_I", "USES_LP_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"crops_distributed_to_uses": 1},
)
def crops_distributed_to_uses_world():
    return sum(
        crops_distributed_to_uses().rename({"REGIONS_9_I": "REGIONS_9_I!"}),
        dim=["REGIONS_9_I!"],
    )


@component.add(
    name="energy_available_for_crops_world",
    units="EJ/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"energy_available_from_crops": 1},
)
def energy_available_for_crops_world():
    return sum(
        energy_available_from_crops().rename({"REGIONS_9_I": "REGIONS_9_I!"}),
        dim=["REGIONS_9_I!"],
    )


@component.add(
    name="energy_available_from_crops",
    units="EJ/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "crops_available_for_energy": 1,
        "energy_to_land_products_conversion_factor": 1,
    },
)
def energy_available_from_crops():
    """
    Energy available in each region for biofuels coming from crops
    """
    return (
        sum(
            crops_available_for_energy().rename(
                {"LAND_PRODUCTS_I": "LAND_PRODUCTS_I!"}
            ),
            dim=["LAND_PRODUCTS_I!"],
        )
        * energy_to_land_products_conversion_factor()
    )


@component.add(
    name="energy_available_from_forestry_products",
    units="EJ/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "forestry_products_available_for_energy": 1,
        "energy_to_wood_conversion_factor": 1,
    },
)
def energy_available_from_forestry_products():
    return forestry_products_available_for_energy() * energy_to_wood_conversion_factor()


@component.add(
    name="forestry_products_available_for_energy",
    units="t/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"forestry_products_distributed_to_uses": 1},
)
def forestry_products_available_for_energy():
    return (
        forestry_products_distributed_to_uses()
        .loc[:, "LP_ENERGY_FORESTRY"]
        .reset_coords(drop=True)
    )


@component.add(
    name="forestry_products_available_for_industry",
    units="t/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"forestry_products_distributed_to_uses": 1},
)
def forestry_products_available_for_industry():
    return (
        forestry_products_distributed_to_uses()
        .loc[:, "LP_INDUSTRY"]
        .reset_coords(drop=True)
    )


@component.add(
    name="forestry_products_distributed_to_uses",
    units="t/Year",
    subscripts=["REGIONS_9_I", "USES_LP_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "wood_demanded_to_uses": 1,
        "priorities_of_forestry_products_distribution_among_uses_sp": 1,
        "width_of_forestry_products_distribution_among_uses_sp": 1,
        "land_products_available_to_each_region": 1,
    },
)
def forestry_products_distributed_to_uses():
    return allocate_by_priority(
        wood_demanded_to_uses(),
        priorities_of_forestry_products_distribution_among_uses_sp(),
        width_of_forestry_products_distribution_among_uses_sp(),
        land_products_available_to_each_region().loc[:, "WOOD"].reset_coords(drop=True),
    )


@component.add(
    name="land_products_available",
    units="t/Year",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={"land_products_available_from_croplands": 11, "roundwood_extracted": 1},
)
def land_products_available():
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
        },
        ["REGIONS_9_I", "LAND_PRODUCTS_I"],
    )
    value.loc[:, ["CORN"]] = (
        land_products_available_from_croplands()
        .loc[:, "CORN"]
        .reset_coords(drop=True)
        .expand_dims({"LAND_PRODUCTS_I": ["CORN"]}, 1)
        .values
    )
    value.loc[:, ["RICE"]] = (
        land_products_available_from_croplands()
        .loc[:, "RICE"]
        .reset_coords(drop=True)
        .expand_dims({"LAND_PRODUCTS_I": ["RICE"]}, 1)
        .values
    )
    value.loc[:, ["CEREALS_OTHER"]] = (
        land_products_available_from_croplands()
        .loc[:, "CEREALS_OTHER"]
        .reset_coords(drop=True)
        .expand_dims({"LAND_PRODUCTS_I": ["CEREALS_OTHER"]}, 1)
        .values
    )
    value.loc[:, ["TUBERS"]] = (
        land_products_available_from_croplands()
        .loc[:, "TUBERS"]
        .reset_coords(drop=True)
        .expand_dims({"LAND_PRODUCTS_I": ["TUBERS"]}, 1)
        .values
    )
    value.loc[:, ["SOY"]] = (
        land_products_available_from_croplands()
        .loc[:, "SOY"]
        .reset_coords(drop=True)
        .expand_dims({"LAND_PRODUCTS_I": ["SOY"]}, 1)
        .values
    )
    value.loc[:, ["PULSES_NUTS"]] = (
        land_products_available_from_croplands()
        .loc[:, "PULSES_NUTS"]
        .reset_coords(drop=True)
        .expand_dims({"LAND_PRODUCTS_I": ["PULSES_NUTS"]}, 1)
        .values
    )
    value.loc[:, ["OILCROPS"]] = (
        land_products_available_from_croplands()
        .loc[:, "OILCROPS"]
        .reset_coords(drop=True)
        .expand_dims({"LAND_PRODUCTS_I": ["OILCROPS"]}, 1)
        .values
    )
    value.loc[:, ["SUGAR_CROPS"]] = (
        land_products_available_from_croplands()
        .loc[:, "SUGAR_CROPS"]
        .reset_coords(drop=True)
        .expand_dims({"LAND_PRODUCTS_I": ["SUGAR_CROPS"]}, 1)
        .values
    )
    value.loc[:, ["FRUITS_VEGETABLES"]] = (
        land_products_available_from_croplands()
        .loc[:, "FRUITS_VEGETABLES"]
        .reset_coords(drop=True)
        .expand_dims({"LAND_PRODUCTS_I": ["FRUITS_VEGETABLES"]}, 1)
        .values
    )
    value.loc[:, ["BIOFUEL_2GCROP"]] = (
        land_products_available_from_croplands()
        .loc[:, "BIOFUEL_2GCROP"]
        .reset_coords(drop=True)
        .expand_dims({"LAND_PRODUCTS_I": ["BIOFUEL_2GCROP"]}, 1)
        .values
    )
    value.loc[:, ["OTHER_CROPS"]] = (
        land_products_available_from_croplands()
        .loc[:, "OTHER_CROPS"]
        .reset_coords(drop=True)
        .expand_dims({"LAND_PRODUCTS_I": ["OTHER_CROPS"]}, 1)
        .values
    )
    value.loc[:, ["WOOD"]] = (
        roundwood_extracted().expand_dims({"LAND_PRODUCTS_I": ["WOOD"]}, 1).values
    )
    value.loc[:, ["RESIDUES"]] = 0
    return value


@component.add(
    name="land_products_available_all_regions",
    units="t/Year",
    subscripts=["LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"land_products_available": 1},
)
def land_products_available_all_regions():
    return sum(
        land_products_available().rename({"REGIONS_9_I": "REGIONS_9_I!"}),
        dim=["REGIONS_9_I!"],
    )


@component.add(
    name="land_products_available_in_global_pool",
    units="t/Year",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "land_products_available": 1,
        "land_products_protected_from_global_pool": 1,
    },
)
def land_products_available_in_global_pool():
    return land_products_available() - land_products_protected_from_global_pool()


@component.add(
    name="land_products_available_in_global_pool_all_regions",
    units="t/Year",
    subscripts=["LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"land_products_available_in_global_pool": 1},
)
def land_products_available_in_global_pool_all_regions():
    """
    global land products available in global market
    """
    return sum(
        land_products_available_in_global_pool().rename(
            {"REGIONS_9_I": "REGIONS_9_I!"}
        ),
        dim=["REGIONS_9_I!"],
    )


@component.add(
    name="land_products_available_to_each_region",
    units="t/Year",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "land_products_distributed_from_pool": 1,
        "land_products_protected_from_global_pool": 1,
    },
)
def land_products_available_to_each_region():
    return (
        land_products_distributed_from_pool()
        + land_products_protected_from_global_pool().transpose(
            "LAND_PRODUCTS_I", "REGIONS_9_I"
        )
    ).transpose("REGIONS_9_I", "LAND_PRODUCTS_I")


@component.add(
    name="land_products_demanded_to_pool",
    units="t/Year",
    subscripts=["LAND_PRODUCTS_I", "REGIONS_9_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "land_products_demanded": 1,
        "land_products_protected_from_global_pool": 1,
    },
)
def land_products_demanded_to_pool():
    value = xr.DataArray(
        np.nan,
        {
            "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        },
        ["LAND_PRODUCTS_I", "REGIONS_9_I"],
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[["OTHER_CROPS"], :] = False
    value.values[except_subs.values] = (
        np.maximum(
            0, land_products_demanded() - land_products_protected_from_global_pool()
        )
        .transpose("LAND_PRODUCTS_I", "REGIONS_9_I")
        .values[except_subs.values]
    )
    value.loc[["OTHER_CROPS"], :] = 0
    return value


@component.add(
    name="land_products_distributed_from_pool",
    units="t/Year",
    subscripts=["LAND_PRODUCTS_I", "REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "land_products_demanded_to_pool": 1,
        "priorities_of_land_products_distribution_among_regions_sp": 1,
        "width_of_land_products_distribution_among_regions_sp": 1,
        "land_products_available_in_global_pool_all_regions": 1,
    },
)
def land_products_distributed_from_pool():
    """
    land products distributed to each region
    """
    return allocate_by_priority(
        land_products_demanded_to_pool(),
        priorities_of_land_products_distribution_among_regions_sp(),
        width_of_land_products_distribution_among_regions_sp(),
        land_products_available_in_global_pool_all_regions(),
    )


@component.add(
    name="land_products_protected_from_global_pool",
    units="t/Year",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "land_products_demanded": 2,
        "share_of_land_products_from_smallholders": 2,
        "land_products_available": 2,
    },
)
def land_products_protected_from_global_pool():
    return if_then_else(
        land_products_demanded()
        > land_products_available() * share_of_land_products_from_smallholders(),
        lambda: land_products_available() * share_of_land_products_from_smallholders(),
        lambda: land_products_demanded(),
    )


@component.add(
    name="share_of_land_products_from_smallholders",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_share_of_land_products_from_smallholders": 1},
    other_deps={
        "_integ_share_of_land_products_from_smallholders": {
            "initial": {"initial_share_of_production_from_smallholders": 1},
            "step": {"change_of_the_share_of_land_products_from_smallholders": 1},
        }
    },
)
def share_of_land_products_from_smallholders():
    """
    share of land products protected from global market
    """
    return _integ_share_of_land_products_from_smallholders()


_integ_share_of_land_products_from_smallholders = Integ(
    lambda: change_of_the_share_of_land_products_from_smallholders(),
    lambda: initial_share_of_production_from_smallholders(),
    "_integ_share_of_land_products_from_smallholders",
)


@component.add(
    name="shortage_of_forestry_products_for_energy",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"availability_of_forestry_products_for_energy": 2},
)
def shortage_of_forestry_products_for_energy():
    return if_then_else(
        availability_of_forestry_products_for_energy() > 0,
        lambda: xr.DataArray(
            0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
        ),
        lambda: availability_of_forestry_products_for_energy(),
    )


@component.add(
    name="wood_demanded_to_uses",
    units="t/Year",
    subscripts=["REGIONS_9_I", "USES_LP_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "wood_demanded_for_industry": 1,
        "wood_demanded_for_energy_converted_to_tonnes": 1,
    },
)
def wood_demanded_to_uses():
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "USES_LP_I": _subscript_dict["USES_LP_I"],
        },
        ["REGIONS_9_I", "USES_LP_I"],
    )
    value.loc[:, ["LP_FOOD"]] = 0
    value.loc[:, ["LP_INDUSTRY"]] = (
        wood_demanded_for_industry()
        .expand_dims({"USES_LP_I": ["LP_INDUSTRY"]}, 1)
        .values
    )
    value.loc[:, ["LP_ENERGY_FORESTRY"]] = (
        wood_demanded_for_energy_converted_to_tonnes()
        .expand_dims({"USES_LP_I": ["LP_ENERGY_FORESTRY"]}, 1)
        .values
    )
    value.loc[:, ["LP_ENERGY_AGRICULTURAL"]] = 0
    return value
