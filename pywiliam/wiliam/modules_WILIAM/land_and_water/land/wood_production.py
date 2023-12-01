"""
Module land_and_water.land.wood_production
Translated using PySD version 3.10.0
"""


@component.add(
    name="annual_growth_rate_of_forest_M_and_P",
    units="DMNL/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "annual_growth_rate_of_forest_stocks_coefficient_0": 1,
        "proportion_of_plantations_in_forest_m_and_p": 1,
        "annual_growth_rate_of_forest_stocks_coefficient_1": 1,
        "volume_stock_per_area_forest_m_and_p": 1,
        "maximum_forest_stock_per_area": 1,
    },
)
def annual_growth_rate_of_forest_m_and_p():
    """
    annual growth rate of forest stocks,
    """
    return (
        annual_growth_rate_of_forest_stocks_coefficient_0()
        + annual_growth_rate_of_forest_stocks_coefficient_1()
        * proportion_of_plantations_in_forest_m_and_p()
    ) * (
        1
        - zidz(volume_stock_per_area_forest_m_and_p(), maximum_forest_stock_per_area())
    )


@component.add(
    name="area_forest_M_and_P",
    units="km2",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"land_use_area_by_region": 5},
)
def area_forest_m_and_p():
    """
    total forest area
    """
    value = xr.DataArray(
        np.nan, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[["INDIA"]] = False
    value.values[except_subs.values] = (
        land_use_area_by_region().loc[:, "FOREST_MANAGED"].reset_coords(drop=True)
        + land_use_area_by_region().loc[:, "FOREST_PLANTATIONS"].reset_coords(drop=True)
    ).values[except_subs.values]
    value.loc[["INDIA"]] = (
        float(land_use_area_by_region().loc["INDIA", "FOREST_MANAGED"])
        + float(land_use_area_by_region().loc["INDIA", "FOREST_PRIMARY"])
        + float(land_use_area_by_region().loc["INDIA", "FOREST_PLANTATIONS"])
    )
    return value


@component.add(
    name="area_lost_of_forest_M_and_P",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"land_use_changes_productive_uses": 10},
)
def area_lost_of_forest_m_and_p():
    value = xr.DataArray(
        np.nan, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[["INDIA"]] = False
    value.values[except_subs.values] = (
        -if_then_else(
            land_use_changes_productive_uses()
            .loc[:, "FOREST_MANAGED"]
            .reset_coords(drop=True)
            + land_use_changes_productive_uses()
            .loc[:, "FOREST_PLANTATIONS"]
            .reset_coords(drop=True)
            < 0,
            lambda: land_use_changes_productive_uses()
            .loc[:, "FOREST_MANAGED"]
            .reset_coords(drop=True)
            + land_use_changes_productive_uses()
            .loc[:, "FOREST_PLANTATIONS"]
            .reset_coords(drop=True),
            lambda: xr.DataArray(
                0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
            ),
        )
    ).values[except_subs.values]
    value.loc[["INDIA"]] = -if_then_else(
        float(land_use_changes_productive_uses().loc["INDIA", "FOREST_MANAGED"])
        + float(land_use_changes_productive_uses().loc["INDIA", "FOREST_PRIMARY"])
        + float(land_use_changes_productive_uses().loc["INDIA", "FOREST_PLANTATIONS"])
        < 0,
        lambda: float(land_use_changes_productive_uses().loc["INDIA", "FOREST_MANAGED"])
        + float(land_use_changes_productive_uses().loc["INDIA", "FOREST_PRIMARY"])
        + float(land_use_changes_productive_uses().loc["INDIA", "FOREST_PLANTATIONS"]),
        lambda: 0,
    )
    return value


@component.add(
    name="change_of_stock_forest_M_and_P",
    units="m3/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "stock_of_managed_forest_and_plantations": 1,
        "initial_volume_stock_of_forest_m_and_p": 1,
        "volume_stock_changes_forest_m_and_p": 1,
    },
)
def change_of_stock_forest_m_and_p():
    """
    increase of forest volume stock. If the stock of forest is less than 1% of initial valur, extraction stops to avoid negative stock.
    """
    return if_then_else(
        stock_of_managed_forest_and_plantations()
        > 0.055 * initial_volume_stock_of_forest_m_and_p(),
        lambda: volume_stock_changes_forest_m_and_p(),
        lambda: xr.DataArray(
            0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
        ),
    )


@component.add(
    name="global_availability_of_biomass",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "roundwood_available_world": 1,
        "roundwood_demanded_world": 1,
        "historical_roundwood_harvested": 1,
        "initial_time": 1,
    },
)
def global_availability_of_biomass():
    """
    difference between demanded and available biomass (=0 meand no shortage) This should be always zero since there are no restrictions set to wood extraction, until all the forests are cut!
    """
    return zidz(
        roundwood_available_world() - roundwood_demanded_world(),
        sum(
            historical_roundwood_harvested(initial_time()).rename(
                {"REGIONS_9_I": "REGIONS_9_I!"}
            ),
            dim=["REGIONS_9_I!"],
        ),
    )


@component.add(
    name="global_roundwood_demand_distributed_as_trends",
    units="t/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "share_of_roundwood_extraction_by_region": 1,
        "roundwood_demanded_world": 1,
    },
)
def global_roundwood_demand_distributed_as_trends():
    """
    Demand of roundwood to producing regions acording to present shares of distribution (global market of wood)
    """
    return share_of_roundwood_extraction_by_region() * roundwood_demanded_world()


@component.add(
    name="global_roundwood_demand_distributed_to_regions",
    units="t/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "global_roundwood_demand_distributed_as_trends": 1,
        "share_of_self_suficiency_of_forestry_products": 2,
        "global_roundwood_demand_self_suficiency": 1,
    },
)
def global_roundwood_demand_distributed_to_regions():
    """
    Demand of roundwood distributed to regions is a compbination of the one destributed as present and the one by policy of self suficiency.Share of self suficiency =1 --> all regions produce their wood
    """
    return (
        global_roundwood_demand_distributed_as_trends()
        * (1 - share_of_self_suficiency_of_forestry_products())
        + global_roundwood_demand_self_suficiency()
        * share_of_self_suficiency_of_forestry_products()
    )


@component.add(
    name="global_roundwood_demand_self_suficiency",
    units="t/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"roundwood_demanded_for_energy_and_industry": 1},
)
def global_roundwood_demand_self_suficiency():
    """
    In 100% self suficiency each regions produces the wood that demands
    """
    return roundwood_demanded_for_energy_and_industry()


@component.add(
    name="historical_roundwood_extracted_world",
    units="t/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"historical_wood_extracted": 1},
)
def historical_roundwood_extracted_world():
    return sum(
        historical_wood_extracted().rename({"REGIONS_9_I": "REGIONS_9_I!"}),
        dim=["REGIONS_9_I!"],
    )


@component.add(
    name="historical_stock_F_and_P",
    units="m3",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "historical_volume_stock_of_forest_m_and_p": 1},
)
def historical_stock_f_and_p():
    return historical_volume_stock_of_forest_m_and_p(time())


@component.add(
    name="historical_wood_extracted",
    units="t/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 2, "historical_roundwood_harvested": 2},
)
def historical_wood_extracted():
    value = xr.DataArray(
        np.nan, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[["INDIA"]] = False
    value.values[except_subs.values] = historical_roundwood_harvested(time()).values[
        except_subs.values
    ]
    value.loc[["INDIA"]] = float(historical_roundwood_harvested(time()).loc["INDIA"])
    return value


@component.add(
    name="increase_of_self_suficiency_forestry",
    units="DMNL/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_model_explorer": 1,
        "model_explorer_forestry_self_sufficiency": 1,
        "year_final_forestry_self_sufficiency_sp": 2,
        "year_initial_forestry_self_sufficiency_sp": 2,
        "objective_forestry_self_sufficiency_sp": 1,
        "time": 2,
        "switch_forestry_self_sufficiency_sp": 1,
    },
)
def increase_of_self_suficiency_forestry():
    """
    Increase of the self suficiency of regions in wood production, =1 means that each region produces its wood demanded
    """
    return if_then_else(
        switch_model_explorer() == 1,
        lambda: model_explorer_forestry_self_sufficiency(),
        lambda: if_then_else(
            np.logical_and(
                switch_forestry_self_sufficiency_sp() == 1,
                np.logical_and(
                    time() > year_initial_forestry_self_sufficiency_sp(),
                    time() < year_final_forestry_self_sufficiency_sp(),
                ),
            ),
            lambda: objective_forestry_self_sufficiency_sp()
            / (
                year_final_forestry_self_sufficiency_sp()
                - year_initial_forestry_self_sufficiency_sp()
            ),
            lambda: xr.DataArray(
                0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
            ),
        ),
    )


@component.add(
    name="loss_of_forest_stock_M_and_P",
    units="m3/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"change_of_stock_forest_m_and_p": 1},
)
def loss_of_forest_stock_m_and_p():
    """
    If stock is loss this is positive,
    """
    return -change_of_stock_forest_m_and_p()


@component.add(
    name="maximum_stock_forest_M_and_P",
    units="m3",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"area_forest_m_and_p": 1, "maximum_forest_stock_per_area": 1},
)
def maximum_stock_forest_m_and_p():
    return area_forest_m_and_p() * maximum_forest_stock_per_area()


@component.add(
    name="proportion_of_plantations_in_forest_M_and_P",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"land_use_area_by_region": 1, "area_forest_m_and_p": 1},
)
def proportion_of_plantations_in_forest_m_and_p():
    """
    proportion of plantations in the total forest area
    """
    return (
        land_use_area_by_region().loc[:, "FOREST_PLANTATIONS"].reset_coords(drop=True)
        / area_forest_m_and_p()
    )


@component.add(
    name="roundwood_available_world",
    units="t/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"roundwood_demanded_world": 1},
)
def roundwood_available_world():
    """
    Available wood equals demand, no limits to wood extraction set
    """
    return roundwood_demanded_world()


@component.add(
    name="roundwood_extracted",
    units="t/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "time_historical_data_land_module": 1,
        "historical_wood_extracted": 1,
        "global_roundwood_demand_distributed_to_regions": 1,
        "stock_of_managed_forest_and_plantations": 1,
        "initial_volume_stock_of_forest_m_and_p": 1,
    },
)
def roundwood_extracted():
    """
    All the roundwood that is demanded is extracted, no limits to extraction (as long as there is forest area)
    """
    return if_then_else(
        time() <= time_historical_data_land_module(),
        lambda: historical_wood_extracted(),
        lambda: if_then_else(
            stock_of_managed_forest_and_plantations()
            > 0.01 * initial_volume_stock_of_forest_m_and_p(),
            lambda: global_roundwood_demand_distributed_to_regions(),
            lambda: xr.DataArray(
                0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
            ),
        ),
    )


@component.add(
    name="roundwood_from_deforestation",
    units="t/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"roundwood_volumme_from_deforestation": 1, "wood_density_by_region": 1},
)
def roundwood_from_deforestation():
    """
    This is not added to the wood available to meet demand
    """
    return roundwood_volumme_from_deforestation() * wood_density_by_region()


@component.add(
    name="roundwood_volumme_extracted_from_forest_M_and_P",
    units="m3/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "roundwood_extracted": 1,
        "wood_density_by_region": 1,
        "outturn_of_wood_extraction": 1,
    },
)
def roundwood_volumme_extracted_from_forest_m_and_p():
    """
    roundwood harvested
    """
    return roundwood_extracted() / (
        wood_density_by_region() * outturn_of_wood_extraction()
    )


@component.add(
    name="roundwood_volumme_from_deforestation",
    units="m3/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_roundwood_volumme_from_deforestation": 1},
    other_deps={
        "_delayfixed_roundwood_volumme_from_deforestation": {
            "initial": {},
            "step": {
                "volume_stock_loss_for_deforestation_m_and_p": 1,
                "outturn_of_wood_extraction": 1,
            },
        }
    },
)
def roundwood_volumme_from_deforestation():
    return _delayfixed_roundwood_volumme_from_deforestation()


_delayfixed_roundwood_volumme_from_deforestation = DelayFixed(
    lambda: volume_stock_loss_for_deforestation_m_and_p()
    * outturn_of_wood_extraction(),
    lambda: 1,
    lambda: xr.DataArray(
        0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
    ),
    time_step,
    "_delayfixed_roundwood_volumme_from_deforestation",
)


@component.add(
    name="share_of_forest_stock_loss",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "loss_of_forest_stock_m_and_p": 1,
        "stock_of_managed_forest_and_plantations": 1,
    },
)
def share_of_forest_stock_loss():
    """
    Indicator of forest sustainability. It shows the percent of forest stock loss per year, >0 means loss of forest
    """
    return zidz(
        np.maximum(0, loss_of_forest_stock_m_and_p()),
        stock_of_managed_forest_and_plantations(),
    )


@component.add(
    name="share_of_self_suficiency_of_forestry_products",
    subscripts=["REGIONS_9_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_share_of_self_suficiency_of_forestry_products": 1},
    other_deps={
        "_integ_share_of_self_suficiency_of_forestry_products": {
            "initial": {},
            "step": {"increase_of_self_suficiency_forestry": 1},
        }
    },
)
def share_of_self_suficiency_of_forestry_products():
    return _integ_share_of_self_suficiency_of_forestry_products()


_integ_share_of_self_suficiency_of_forestry_products = Integ(
    lambda: increase_of_self_suficiency_forestry(),
    lambda: xr.DataArray(
        0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
    ),
    "_integ_share_of_self_suficiency_of_forestry_products",
)


@component.add(
    name="stock_growth_forest_M_and_P",
    units="m3/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "stock_of_managed_forest_and_plantations": 1,
        "annual_growth_rate_of_forest_m_and_p": 1,
    },
)
def stock_growth_forest_m_and_p():
    """
    forest stock increment
    """
    return (
        stock_of_managed_forest_and_plantations()
        * annual_growth_rate_of_forest_m_and_p()
    )


@component.add(
    name="stock_of_managed_forest_and_plantations",
    units="m3",
    subscripts=["REGIONS_9_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_stock_of_managed_forest_and_plantations": 1},
    other_deps={
        "_integ_stock_of_managed_forest_and_plantations": {
            "initial": {
                "initial_time": 1,
                "historical_volume_stock_of_forest_m_and_p": 1,
            },
            "step": {"change_of_stock_forest_m_and_p": 1},
        }
    },
)
def stock_of_managed_forest_and_plantations():
    """
    forest volume stock
    """
    return _integ_stock_of_managed_forest_and_plantations()


_integ_stock_of_managed_forest_and_plantations = Integ(
    lambda: change_of_stock_forest_m_and_p(),
    lambda: historical_volume_stock_of_forest_m_and_p(initial_time()),
    "_integ_stock_of_managed_forest_and_plantations",
)


@component.add(
    name="volume_stock_changes_forest_M_and_P",
    units="m3/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 2,
        "time_historical_data_land_module": 1,
        "historical_volume_stock_change_forest_m_and_p": 1,
        "roundwood_volumme_extracted_from_forest_m_and_p": 1,
        "stock_growth_forest_m_and_p": 1,
        "volume_stock_loss_for_deforestation_m_and_p": 1,
    },
)
def volume_stock_changes_forest_m_and_p():
    """
    forest volume stock changes....
    """
    return if_then_else(
        time() <= time_historical_data_land_module(),
        lambda: historical_volume_stock_change_forest_m_and_p(time()),
        lambda: stock_growth_forest_m_and_p()
        - roundwood_volumme_extracted_from_forest_m_and_p()
        - volume_stock_loss_for_deforestation_m_and_p(),
    )


@component.add(
    name="volume_stock_loss_for_deforestation_M_and_P",
    units="m3/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "area_lost_of_forest_m_and_p": 1,
        "volume_stock_per_area_forest_m_and_p": 1,
    },
)
def volume_stock_loss_for_deforestation_m_and_p():
    return area_lost_of_forest_m_and_p() * volume_stock_per_area_forest_m_and_p()


@component.add(
    name="volume_stock_per_area_forest_M_and_P",
    units="m3/km2",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"stock_of_managed_forest_and_plantations": 1, "area_forest_m_and_p": 1},
)
def volume_stock_per_area_forest_m_and_p():
    """
    forest volume stock per unit area
    """
    return zidz(stock_of_managed_forest_and_plantations(), area_forest_m_and_p())
