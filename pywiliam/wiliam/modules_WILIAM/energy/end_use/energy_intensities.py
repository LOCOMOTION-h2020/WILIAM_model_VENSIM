"""
Module energy.end_use.energy_intensities
Translated using PySD version 3.10.0
"""


@component.add(
    name="adjustment_factor_estimate_final_energy_substitution_component_2015",
    units="DMNL",
    subscripts=["REGIONS_35_I", "SECTORS_NON_ENERGY_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"estimate_final_energy_substitution_component_2015": 1},
)
def adjustment_factor_estimate_final_energy_substitution_component_2015():
    """
    Auxiliary variable used in the method to disaggregate in 2015 the two components of the final energy intensity: energy efficiency and final energy substitution. Sum of the first estimation of the final energy substitution by sector and final energy in 2015 to normalize this variable.
    """
    return sum(
        estimate_final_energy_substitution_component_2015().rename(
            {"NRG_FE_I": "NRG_FE_I!"}
        ),
        dim=["NRG_FE_I!"],
    )


@component.add(
    name="availability_of_forestry_products_for_energy_35R",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"availability_of_forestry_products_for_energy": 2},
)
def availability_of_forestry_products_for_energy_35r():
    value = xr.DataArray(
        np.nan, {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]}, ["REGIONS_35_I"]
    )
    value.loc[_subscript_dict["REGIONS_EU27_I"]] = float(
        availability_of_forestry_products_for_energy().loc["EU27"]
    )
    value.loc[_subscript_dict["REGIONS_8_I"]] = (
        availability_of_forestry_products_for_energy()
        .loc[_subscript_dict["REGIONS_8_I"]]
        .rename({"REGIONS_9_I": "REGIONS_8_I"})
        .values
    )
    return value


@component.add(
    name="base_implicit_price_FE",
    subscripts=["REGIONS_35_I", "SECTORS_NON_ENERGY_I", "NRG_FE_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "intermediates_total_real": 6,
        "final_energy_demand_by_sector_and_fe": 6,
    },
)
def base_implicit_price_fe():
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "SECTORS_NON_ENERGY_I": _subscript_dict["SECTORS_NON_ENERGY_I"],
            "NRG_FE_I": _subscript_dict["NRG_FE_I"],
        },
        ["REGIONS_35_I", "SECTORS_NON_ENERGY_I", "NRG_FE_I"],
    )
    value.loc[:, :, ["FE_elec"]] = (
        zidz(
            intermediates_total_real()
            .loc[:, "DISTRIBUTION_ELECTRICITY", _subscript_dict["SECTORS_NON_ENERGY_I"]]
            .reset_coords(drop=True)
            .rename({"SECTORS_MAP_I": "SECTORS_NON_ENERGY_I"}),
            final_energy_demand_by_sector_and_fe()
            .loc[:, :, "FE_elec"]
            .reset_coords(drop=True),
        )
        .expand_dims({"FINAL_ENERGY_TRANSMISSION_I": ["FE_elec"]}, 2)
        .values
    )
    value.loc[:, :, ["FE_gas"]] = (
        zidz(
            intermediates_total_real()
            .loc[:, "DISTRIBUTION_GAS", _subscript_dict["SECTORS_NON_ENERGY_I"]]
            .reset_coords(drop=True)
            .rename({"SECTORS_MAP_I": "SECTORS_NON_ENERGY_I"}),
            final_energy_demand_by_sector_and_fe()
            .loc[:, :, "FE_gas"]
            .reset_coords(drop=True),
        )
        .expand_dims({"FINAL_ENERGY_TRANSMISSION_I": ["FE_gas"]}, 2)
        .values
    )
    value.loc[:, :, ["FE_hydrogen"]] = (
        zidz(
            intermediates_total_real()
            .loc[:, "HYDROGEN_PRODUCTION", _subscript_dict["SECTORS_NON_ENERGY_I"]]
            .reset_coords(drop=True)
            .rename({"SECTORS_MAP_I": "SECTORS_NON_ENERGY_I"}),
            final_energy_demand_by_sector_and_fe()
            .loc[:, :, "FE_hydrogen"]
            .reset_coords(drop=True),
        )
        .expand_dims({"NRG_COMMODITIES_I": ["FE_hydrogen"]}, 2)
        .values
    )
    value.loc[:, :, ["FE_liquid"]] = (
        zidz(
            intermediates_total_real()
            .loc[:, "REFINING", _subscript_dict["SECTORS_NON_ENERGY_I"]]
            .reset_coords(drop=True)
            .rename({"SECTORS_MAP_I": "SECTORS_NON_ENERGY_I"}),
            final_energy_demand_by_sector_and_fe()
            .loc[:, :, "FE_liquid"]
            .reset_coords(drop=True),
        )
        .expand_dims({"NRG_COMMODITIES_I": ["FE_liquid"]}, 2)
        .values
    )
    value.loc[:, :, ["FE_solid_fossil"]] = (
        zidz(
            intermediates_total_real()
            .loc[:, "MINING_COAL", _subscript_dict["SECTORS_NON_ENERGY_I"]]
            .reset_coords(drop=True)
            .rename({"SECTORS_MAP_I": "SECTORS_NON_ENERGY_I"}),
            final_energy_demand_by_sector_and_fe()
            .loc[:, :, "FE_solid_fossil"]
            .reset_coords(drop=True),
        )
        .expand_dims({"NRG_COMMODITIES_I": ["FE_solid_fossil"]}, 2)
        .values
    )
    value.loc[:, :, ["FE_heat"]] = (
        zidz(
            intermediates_total_real()
            .loc[:, "STEAM_HOT_WATER", _subscript_dict["SECTORS_NON_ENERGY_I"]]
            .reset_coords(drop=True)
            .rename({"SECTORS_MAP_I": "SECTORS_NON_ENERGY_I"}),
            final_energy_demand_by_sector_and_fe()
            .loc[:, :, "FE_heat"]
            .reset_coords(drop=True),
        )
        .expand_dims({"FINAL_ENERGY_TRANSMISSION_I": ["FE_heat"]}, 2)
        .values
    )
    value.loc[:, :, ["FE_solid_bio"]] = 0
    return value


@component.add(
    name="delayed_final_energy_substitution_component",
    subscripts=["REGIONS_35_I", "SECTORS_NON_ENERGY_I", "NRG_FE_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_final_energy_substitution_component": 1},
    other_deps={
        "_delayfixed_delayed_final_energy_substitution_component": {
            "initial": {"final_energy_substitution_component_2015": 1, "time_step": 1},
            "step": {"final_energy_substitution_component": 1},
        }
    },
)
def delayed_final_energy_substitution_component():
    return _delayfixed_delayed_final_energy_substitution_component()


_delayfixed_delayed_final_energy_substitution_component = DelayFixed(
    lambda: final_energy_substitution_component(),
    lambda: time_step(),
    lambda: final_energy_substitution_component_2015(),
    time_step,
    "_delayfixed_delayed_final_energy_substitution_component",
)


@component.add(
    name="elec_by_sector_FE_and_output",
    units="TJ/million$",
    subscripts=["REGIONS_35_I", "SECTORS_NON_ENERGY_I", "FINAL_ENERGY_TRANSMISSION_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "share_final_energy_demand_by_sector_and_fe": 1,
        "total_final_energy_intensities_by_sector": 1,
    },
)
def elec_by_sector_fe_and_output():
    """
    Auxiliary variable used in the method to disaggregate in 2015 the two components of the final energy intensity: energy efficiency and final energy substitution. Electricy intensity by sector assuming the shame shares that in energy demand.
    """
    return (
        share_final_energy_demand_by_sector_and_fe()
        .loc[:, :, "FE_elec"]
        .reset_coords(drop=True)
        * total_final_energy_intensities_by_sector()
    ).expand_dims({"FINAL_ENERGY_TRANSMISSION_I": ["FE_elec"]}, 2)


@component.add(
    name="energy_efficiency_annual_improvement",
    units="1/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_model_explorer": 1,
        "model_explorer_energy_efficiency_anual_improvement": 1,
        "time": 1,
        "historical_energy_efficiency_annual_improvement": 1,
        "energy_efficiency_annual_improvement_sp": 1,
        "start_year_energy_efficiency_annual_improvement_sp": 1,
    },
)
def energy_efficiency_annual_improvement():
    """
    Energy efficiency annual improvement by sector and final energy as a function of the historical trends and exogenous policies.
    """
    return if_then_else(
        switch_model_explorer() == 1,
        lambda: model_explorer_energy_efficiency_anual_improvement(),
        lambda: if_then_else(
            time() < start_year_energy_efficiency_annual_improvement_sp(),
            lambda: historical_energy_efficiency_annual_improvement(),
            lambda: energy_efficiency_annual_improvement_sp(),
        ),
    )


@component.add(
    name="ENERGY_EFFICIENCY_ANNUAL_IMPROVEMENT_SP",
    units="1/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_energy_efficiency_annual_improvement_sp"
    },
)
def energy_efficiency_annual_improvement_sp():
    """
    Energy effiency annual improvement policy
    """
    return _ext_constant_energy_efficiency_annual_improvement_sp()


_ext_constant_energy_efficiency_annual_improvement_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "ENERGY_EFFICIENCY_ANNUAL_IMPROVEMENT_SP*",
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    _root,
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    "_ext_constant_energy_efficiency_annual_improvement_sp",
)


@component.add(
    name="energy_efficiency_component",
    units="TJ/million$",
    subscripts=["REGIONS_35_I", "SECTORS_NON_ENERGY_I", "NRG_FE_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_energy_efficiency_component": 1},
    other_deps={
        "_integ_energy_efficiency_component": {
            "initial": {"energy_efficiengy_component_2015": 3},
            "step": {"variation_energy_efficiency_component": 1},
        }
    },
)
def energy_efficiency_component():
    """
    Energy efficiency by sector and final energy estimated with a top-down approach
    """
    return _integ_energy_efficiency_component()


_integ_energy_efficiency_component = Integ(
    lambda: variation_energy_efficiency_component(),
    lambda: if_then_else(
        energy_efficiengy_component_2015() == 0,
        lambda: energy_efficiengy_component_2015()
        .loc[:, :, "FE_elec"]
        .reset_coords(drop=True)
        .expand_dims({"NRG_FE_I": _subscript_dict["NRG_FE_I"]}, 2),
        lambda: energy_efficiengy_component_2015(),
    ),
    "_integ_energy_efficiency_component",
)


@component.add(
    name="energy_efficiengy_component_2015",
    units="TJ/million$",
    subscripts=["REGIONS_35_I", "SECTORS_NON_ENERGY_I", "NRG_FE_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "final_energy_intensities_by_sector_and_fe": 1,
        "estimate_final_energy_demand_by_sector_fe_and_output_2015": 1,
        "adjustment_factor_estimate_final_energy_substitution_component_2015": 1,
    },
)
def energy_efficiengy_component_2015():
    """
    Auxiliary variable used in the method to disaggregate in 2015 the two components of the final energy intensity: energy efficiency and final energy substitution. Estimation of the energy efficiency by sector and final energy in 2015
    """
    return if_then_else(
        final_energy_intensities_by_sector_and_fe() <= 0,
        lambda: xr.DataArray(
            0,
            {
                "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                "SECTORS_NON_ENERGY_I": _subscript_dict["SECTORS_NON_ENERGY_I"],
                "NRG_FE_I": _subscript_dict["NRG_FE_I"],
            },
            ["REGIONS_35_I", "SECTORS_NON_ENERGY_I", "NRG_FE_I"],
        ),
        lambda: estimate_final_energy_demand_by_sector_fe_and_output_2015()
        * adjustment_factor_estimate_final_energy_substitution_component_2015(),
    )


@component.add(
    name="estimate_final_energy_demand_by_sector_FE_and_output_2015",
    units="TJ/million$",
    subscripts=["REGIONS_35_I", "SECTORS_NON_ENERGY_I", "NRG_FE_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"elec_by_sector_fe_and_output": 1, "relative_energy_intensity_2015": 1},
)
def estimate_final_energy_demand_by_sector_fe_and_output_2015():
    """
    Auxiliary variable used in the method to disaggregate in 2015 the two components of the final energy intensity: energy efficiency and final energy substitution. Estimation of the final energy demand by sector and final energy in 2015 used to disaggregate the two components.
    """
    return elec_by_sector_fe_and_output().loc[:, :, "FE_elec"].reset_coords(
        drop=True
    ) * relative_energy_intensity_2015().loc[
        _subscript_dict["SECTORS_NON_ENERGY_I"], :
    ].rename(
        {"SECTORS_I": "SECTORS_NON_ENERGY_I"}
    )


@component.add(
    name="estimate_final_energy_substitution_component_2015",
    units="DMNL",
    subscripts=["REGIONS_35_I", "SECTORS_NON_ENERGY_I", "NRG_FE_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "final_energy_intensities_by_sector_and_fe": 1,
        "estimate_final_energy_demand_by_sector_fe_and_output_2015": 1,
    },
)
def estimate_final_energy_substitution_component_2015():
    """
    Auxiliary variable used in the method to disaggregate in 2015 the two components of the final energy intensity: energy efficiency and final energy substitution. First estimation of the final energy substitution by sector and final energy in 2015 (non-normalized).
    """
    return zidz(
        final_energy_intensities_by_sector_and_fe(),
        estimate_final_energy_demand_by_sector_fe_and_output_2015(),
    )


@component.add(
    name="final_energy_demand_by_FE_35R",
    units="TJ/Year",
    subscripts=["REGIONS_35_I", "NRG_FE_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "final_energy_demand_by_sector_and_fe": 1,
        "households_final_energy_demand_by_fe": 1,
    },
)
def final_energy_demand_by_fe_35r():
    """
    Final energy demand by final energy 35 regions
    """
    return (
        sum(
            final_energy_demand_by_sector_and_fe().rename(
                {"SECTORS_NON_ENERGY_I": "SECTORS_NON_ENERGY_I!"}
            ),
            dim=["SECTORS_NON_ENERGY_I!"],
        )
        + households_final_energy_demand_by_fe()
    )


@component.add(
    name="final_energy_demand_by_FE_9R",
    units="TJ/Year",
    subscripts=["REGIONS_9_I", "NRG_FE_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "final_energy_demand_by_fe_eu27": 1,
        "final_energy_demand_by_fe_35r": 1,
    },
)
def final_energy_demand_by_fe_9r():
    """
    Final energy demand by final energy 9 regions (not including non-energy uses).
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "NRG_FE_I": _subscript_dict["NRG_FE_I"],
        },
        ["REGIONS_9_I", "NRG_FE_I"],
    )
    value.loc[["EU27"], :] = (
        final_energy_demand_by_fe_eu27()
        .expand_dims({"REGIONS_36_I": ["EU27"]}, 0)
        .values
    )
    value.loc[_subscript_dict["REGIONS_8_I"], :] = (
        final_energy_demand_by_fe_35r()
        .loc[_subscript_dict["REGIONS_8_I"], :]
        .rename({"REGIONS_35_I": "REGIONS_8_I"})
        .values
    )
    return value


@component.add(
    name="final_energy_demand_by_FE_EU27",
    units="TJ/Year",
    subscripts=["NRG_FE_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"final_energy_demand_by_fe_35r": 1},
)
def final_energy_demand_by_fe_eu27():
    """
    Final energy demand by final energy EU27
    """
    return sum(
        final_energy_demand_by_fe_35r()
        .loc[_subscript_dict["REGIONS_EU27_I"], :]
        .rename({"REGIONS_35_I": "REGIONS_EU27_I!"}),
        dim=["REGIONS_EU27_I!"],
    )


@component.add(
    name="final_energy_demand_by_sector_and_FE",
    units="TJ/Year",
    subscripts=["REGIONS_35_I", "SECTORS_NON_ENERGY_I", "NRG_FE_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_energy": 1,
        "final_energy_intensities_by_sector_and_fe": 3,
        "base_output_real": 2,
        "switch_eco2nrg_output_real": 1,
        "output_real": 1,
    },
)
def final_energy_demand_by_sector_and_fe():
    """
    Final energy demand by sector and final energy estimated with a top-down approach
    """
    return if_then_else(
        switch_energy() == 0,
        lambda: final_energy_intensities_by_sector_and_fe()
        * base_output_real()
        .loc[:, _subscript_dict["SECTORS_NON_ENERGY_I"]]
        .rename({"SECTORS_I": "SECTORS_NON_ENERGY_I"}),
        lambda: if_then_else(
            switch_eco2nrg_output_real() == 0,
            lambda: final_energy_intensities_by_sector_and_fe()
            * base_output_real()
            .loc[:, _subscript_dict["SECTORS_NON_ENERGY_I"]]
            .rename({"SECTORS_I": "SECTORS_NON_ENERGY_I"}),
            lambda: final_energy_intensities_by_sector_and_fe()
            * output_real()
            .loc[:, _subscript_dict["SECTORS_NON_ENERGY_I"]]
            .rename({"SECTORS_I": "SECTORS_NON_ENERGY_I"}),
        ),
    )


@component.add(
    name="final_energy_intensities_by_sector_and_FE",
    units="TJ/million$",
    subscripts=["REGIONS_35_I", "SECTORS_NON_ENERGY_I", "NRG_FE_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_final_energy_intensities_by_sector_and_fe": 1},
    other_deps={
        "_integ_final_energy_intensities_by_sector_and_fe": {
            "initial": {"historical_energy_intensities_top_down_by_sector_and_fe": 1},
            "step": {"variation_energy_intensity_by_sector_and_fe": 1},
        }
    },
)
def final_energy_intensities_by_sector_and_fe():
    """
    Final energy intensities by sector and final energy estimated with a top-down approach
    """
    return _integ_final_energy_intensities_by_sector_and_fe()


_integ_final_energy_intensities_by_sector_and_fe = Integ(
    lambda: variation_energy_intensity_by_sector_and_fe()
    .loc[:, _subscript_dict["SECTORS_NON_ENERGY_I"], :]
    .rename({"SECTORS_I": "SECTORS_NON_ENERGY_I"}),
    lambda: historical_energy_intensities_top_down_by_sector_and_fe()
    .loc[:, _subscript_dict["SECTORS_NON_ENERGY_I"], :]
    .rename({"SECTORS_I": "SECTORS_NON_ENERGY_I"}),
    "_integ_final_energy_intensities_by_sector_and_fe",
)


@component.add(
    name="final_energy_substituion_annual_variation",
    units="1/Year",
    subscripts=["REGIONS_35_I", "SECTORS_NON_ENERGY_I", "NRG_FE_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 7,
        "trend_of_final_energy_substituion_annual_variation": 8,
        "price_final_energy": 9,
        "availability_of_forestry_products_for_energy_35r": 1,
        "switch_law2nrg_available_forestry_for_energy": 1,
        "switch_energy": 1,
    },
)
def final_energy_substituion_annual_variation():
    """
    Estimated final energy annunal substitution by sector and final energy as a function of the historical trends, the final energy prioces and exogenous policies. (not normalized)
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "SECTORS_NON_ENERGY_I": _subscript_dict["SECTORS_NON_ENERGY_I"],
            "NRG_FE_I": _subscript_dict["NRG_FE_I"],
        },
        ["REGIONS_35_I", "SECTORS_NON_ENERGY_I", "NRG_FE_I"],
    )
    value.loc[:, :, ["FE_elec"]] = (
        if_then_else(
            time() < 2015,
            lambda: xr.DataArray(
                0, {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]}, ["REGIONS_35_I"]
            ),
            lambda: trend_of_final_energy_substituion_annual_variation()
            .loc[:, "FE_elec"]
            .reset_coords(drop=True),
        )
        .expand_dims(
            {"SECTORS_NON_ENERGY_I": _subscript_dict["SECTORS_NON_ENERGY_I"]}, 1
        )
        .expand_dims({"FINAL_ENERGY_TRANSMISSION_I": ["FE_elec"]}, 2)
        .values
    )
    value.loc[:, :, ["FE_gas"]] = (
        if_then_else(
            time() < 2015,
            lambda: xr.DataArray(
                0, {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]}, ["REGIONS_35_I"]
            ),
            lambda: trend_of_final_energy_substituion_annual_variation()
            .loc[:, "FE_gas"]
            .reset_coords(drop=True)
            + np.minimum(
                0,
                price_final_energy().loc[:, "FE_elec"].reset_coords(drop=True)
                - price_final_energy().loc[:, "FE_gas"].reset_coords(drop=True),
            )
            / price_final_energy().loc[:, "FE_elec"].reset_coords(drop=True),
        )
        .expand_dims(
            {"SECTORS_NON_ENERGY_I": _subscript_dict["SECTORS_NON_ENERGY_I"]}, 1
        )
        .expand_dims({"FINAL_ENERGY_TRANSMISSION_I": ["FE_gas"]}, 2)
        .values
    )
    value.loc[:, :, ["FE_heat"]] = (
        if_then_else(
            time() < 2015,
            lambda: xr.DataArray(
                0, {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]}, ["REGIONS_35_I"]
            ),
            lambda: trend_of_final_energy_substituion_annual_variation()
            .loc[:, "FE_heat"]
            .reset_coords(drop=True),
        )
        .expand_dims(
            {"SECTORS_NON_ENERGY_I": _subscript_dict["SECTORS_NON_ENERGY_I"]}, 1
        )
        .expand_dims({"FINAL_ENERGY_TRANSMISSION_I": ["FE_heat"]}, 2)
        .values
    )
    value.loc[:, :, ["FE_hydrogen"]] = (
        if_then_else(
            time() < 2015,
            lambda: xr.DataArray(
                0, {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]}, ["REGIONS_35_I"]
            ),
            lambda: trend_of_final_energy_substituion_annual_variation()
            .loc[:, "FE_hydrogen"]
            .reset_coords(drop=True),
        )
        .expand_dims(
            {"SECTORS_NON_ENERGY_I": _subscript_dict["SECTORS_NON_ENERGY_I"]}, 1
        )
        .expand_dims({"NRG_COMMODITIES_I": ["FE_hydrogen"]}, 2)
        .values
    )
    value.loc[:, :, ["FE_liquid"]] = (
        if_then_else(
            time() < 2015,
            lambda: xr.DataArray(
                0, {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]}, ["REGIONS_35_I"]
            ),
            lambda: trend_of_final_energy_substituion_annual_variation()
            .loc[:, "FE_liquid"]
            .reset_coords(drop=True)
            + np.minimum(
                0,
                price_final_energy().loc[:, "FE_elec"].reset_coords(drop=True)
                - price_final_energy().loc[:, "FE_liquid"].reset_coords(drop=True),
            )
            / price_final_energy().loc[:, "FE_elec"].reset_coords(drop=True),
        )
        .expand_dims(
            {"SECTORS_NON_ENERGY_I": _subscript_dict["SECTORS_NON_ENERGY_I"]}, 1
        )
        .expand_dims({"NRG_COMMODITIES_I": ["FE_liquid"]}, 2)
        .values
    )
    value.loc[:, :, ["FE_solid_bio"]] = (
        if_then_else(
            time() < 2015,
            lambda: xr.DataArray(
                0, {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]}, ["REGIONS_35_I"]
            ),
            lambda: if_then_else(
                np.logical_or(
                    switch_energy() == 0,
                    switch_law2nrg_available_forestry_for_energy() == 0,
                ),
                lambda: trend_of_final_energy_substituion_annual_variation()
                .loc[:, "FE_solid_bio"]
                .reset_coords(drop=True),
                lambda: trend_of_final_energy_substituion_annual_variation()
                .loc[:, "FE_solid_bio"]
                .reset_coords(drop=True)
                + (availability_of_forestry_products_for_energy_35r() - 1),
            ),
        )
        .expand_dims(
            {"SECTORS_NON_ENERGY_I": _subscript_dict["SECTORS_NON_ENERGY_I"]}, 1
        )
        .expand_dims({"NRG_COMMODITIES_I": ["FE_solid_bio"]}, 2)
        .values
    )
    value.loc[:, :, ["FE_solid_fossil"]] = (
        if_then_else(
            time() < 2015,
            lambda: xr.DataArray(
                0, {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]}, ["REGIONS_35_I"]
            ),
            lambda: trend_of_final_energy_substituion_annual_variation()
            .loc[:, "FE_solid_fossil"]
            .reset_coords(drop=True)
            + np.minimum(
                0,
                price_final_energy().loc[:, "FE_elec"].reset_coords(drop=True)
                - price_final_energy()
                .loc[:, "FE_solid_fossil"]
                .reset_coords(drop=True),
            )
            / price_final_energy().loc[:, "FE_elec"].reset_coords(drop=True),
        )
        .expand_dims(
            {"SECTORS_NON_ENERGY_I": _subscript_dict["SECTORS_NON_ENERGY_I"]}, 1
        )
        .expand_dims({"NRG_COMMODITIES_I": ["FE_solid_fossil"]}, 2)
        .values
    )
    return value


@component.add(
    name="final_energy_substitution_component",
    units="DMNL",
    subscripts=["REGIONS_35_I", "SECTORS_NON_ENERGY_I", "NRG_FE_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_final_energy_substitution_component": 1},
    other_deps={
        "_integ_final_energy_substitution_component": {
            "initial": {"final_energy_substitution_component_2015": 1},
            "step": {"variation_final_energy_substitution_component": 1},
        }
    },
)
def final_energy_substitution_component():
    """
    Final energy substitution by sector and final energy estimated with a top-down approach
    """
    return _integ_final_energy_substitution_component()


_integ_final_energy_substitution_component = Integ(
    lambda: variation_final_energy_substitution_component(),
    lambda: final_energy_substitution_component_2015(),
    "_integ_final_energy_substitution_component",
)


@component.add(
    name="final_energy_substitution_component_2015",
    units="DMNL",
    subscripts=["REGIONS_35_I", "SECTORS_NON_ENERGY_I", "NRG_FE_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "estimate_final_energy_substitution_component_2015": 1,
        "adjustment_factor_estimate_final_energy_substitution_component_2015": 1,
    },
)
def final_energy_substitution_component_2015():
    """
    Auxiliary variable used in the method to disaggregate in 2015 the two components of the final energy intensity: energy efficiency and final energy substitution. Estimation of the final energy substitution by sector and final energy in 2015
    """
    return zidz(
        estimate_final_energy_substitution_component_2015(),
        adjustment_factor_estimate_final_energy_substitution_component_2015().expand_dims(
            {"NRG_FE_I": _subscript_dict["NRG_FE_I"]}, 2
        ),
    )


@component.add(
    name="final_energy_substitution_component_aux",
    units="DMNL",
    subscripts=["REGIONS_35_I", "SECTORS_NON_ENERGY_I", "NRG_FE_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "delayed_final_energy_substitution_component": 2,
        "time_step": 1,
        "final_energy_substituion_annual_variation": 1,
    },
)
def final_energy_substitution_component_aux():
    """
    Auxiliarity variable to normalize the final energy annual substitution by sector and final energy
    """
    return (
        delayed_final_energy_substitution_component()
        + final_energy_substituion_annual_variation()
        * delayed_final_energy_substitution_component()
        * time_step()
    )


@component.add(
    name="FINAL_ENERGY_SUBSTITUTION_SP",
    units="1/Year",
    subscripts=["REGIONS_35_I", "NRG_FE_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_final_energy_substitution_sp"},
)
def final_energy_substitution_sp():
    """
    Final energy substitution policy
    """
    return _ext_constant_final_energy_substitution_sp()


_ext_constant_final_energy_substitution_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "FINAL_ENERGY_SUBSTITUTION_SP",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
    "_ext_constant_final_energy_substitution_sp",
)


@component.add(
    name="HISTORICAL_ENERGY_EFFICIENCY_ANNUAL_IMPROVEMENT",
    units="1/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_historical_energy_efficiency_annual_improvement"
    },
)
def historical_energy_efficiency_annual_improvement():
    """
    Historical energy effiency annual variation form IEA balances 2000-2015 (no difference between sectors).
    """
    return _ext_constant_historical_energy_efficiency_annual_improvement()


_ext_constant_historical_energy_efficiency_annual_improvement = ExtConstant(
    "model_parameters/energy/energy-end_use.xlsx",
    "Hist_energy_intensity_variation",
    "HISTORIC_ENERGY_EFFICIENCY_IMPROVEMENT*",
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    _root,
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    "_ext_constant_historical_energy_efficiency_annual_improvement",
)


@component.add(
    name="HISTORICAL_FINAL_ENERGY_SUBSTITUTION",
    units="1/Year",
    subscripts=["REGIONS_35_I", "NRG_FE_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_historical_final_energy_substitution"},
)
def historical_final_energy_substitution():
    """
    Historical final energy annual substitution form IEA balances 2000-2015 (no difference between sectors).
    """
    return _ext_constant_historical_final_energy_substitution()


_ext_constant_historical_final_energy_substitution = ExtConstant(
    "model_parameters/energy/energy-end_use.xlsx",
    "Hist_energy_intensity_variation",
    "HISTORIC_FINAL_ENERGY_SUBSTITUTION",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
    "_ext_constant_historical_final_energy_substitution",
)


@component.add(
    name="households_final_energy_demand_by_FE",
    units="TJ/Year",
    subscripts=["REGIONS_35_I", "NRG_FE_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_hh_transport_energy_bottom_up": 4,
        "imv_final_energy_consumption_buildings_and_transport_top_down_coicop": 10,
        "energy_private_transport_consumption_by_region_and_fe": 4,
        "share_energy_consumption_solid_bio_vs_solid_fossil": 2,
    },
)
def households_final_energy_demand_by_fe():
    """
    Households final energy demand by final energy
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "NRG_FE_I": _subscript_dict["NRG_FE_I"],
        },
        ["REGIONS_35_I", "NRG_FE_I"],
    )
    value.loc[:, ["FE_elec"]] = (
        if_then_else(
            switch_eco_hh_transport_energy_bottom_up() == 0,
            lambda: imv_final_energy_consumption_buildings_and_transport_top_down_coicop()
            .loc[:, "HH_ELECTRICITY"]
            .reset_coords(drop=True),
            lambda: imv_final_energy_consumption_buildings_and_transport_top_down_coicop()
            .loc[:, "HH_ELECTRICITY"]
            .reset_coords(drop=True)
            + energy_private_transport_consumption_by_region_and_fe()
            .loc[:, "FE_elec"]
            .reset_coords(drop=True),
        )
        .expand_dims({"FINAL_ENERGY_TRANSMISSION_I": ["FE_elec"]}, 1)
        .values
    )
    value.loc[:, ["FE_gas"]] = (
        if_then_else(
            switch_eco_hh_transport_energy_bottom_up() == 0,
            lambda: imv_final_energy_consumption_buildings_and_transport_top_down_coicop()
            .loc[:, "HH_GAS"]
            .reset_coords(drop=True),
            lambda: imv_final_energy_consumption_buildings_and_transport_top_down_coicop()
            .loc[:, "HH_GAS"]
            .reset_coords(drop=True)
            + energy_private_transport_consumption_by_region_and_fe()
            .loc[:, "FE_gas"]
            .reset_coords(drop=True),
        )
        .expand_dims({"FINAL_ENERGY_TRANSMISSION_I": ["FE_gas"]}, 1)
        .values
    )
    value.loc[:, ["FE_heat"]] = (
        imv_final_energy_consumption_buildings_and_transport_top_down_coicop()
        .loc[:, "HH_HEAT"]
        .reset_coords(drop=True)
        .expand_dims({"FINAL_ENERGY_TRANSMISSION_I": ["FE_heat"]}, 1)
        .values
    )
    value.loc[:, ["FE_hydrogen"]] = (
        if_then_else(
            switch_eco_hh_transport_energy_bottom_up() == 0,
            lambda: xr.DataArray(
                0, {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]}, ["REGIONS_35_I"]
            ),
            lambda: energy_private_transport_consumption_by_region_and_fe()
            .loc[:, "FE_hydrogen"]
            .reset_coords(drop=True),
        )
        .expand_dims({"NRG_COMMODITIES_I": ["FE_hydrogen"]}, 1)
        .values
    )
    value.loc[:, ["FE_liquid"]] = (
        if_then_else(
            switch_eco_hh_transport_energy_bottom_up() == 0,
            lambda: imv_final_energy_consumption_buildings_and_transport_top_down_coicop()
            .loc[:, "HH_LIQUID_FUELS"]
            .reset_coords(drop=True)
            + imv_final_energy_consumption_buildings_and_transport_top_down_coicop()
            .loc[:, "HH_FUEL_TRANSPORT"]
            .reset_coords(drop=True),
            lambda: imv_final_energy_consumption_buildings_and_transport_top_down_coicop()
            .loc[:, "HH_LIQUID_FUELS"]
            .reset_coords(drop=True)
            + energy_private_transport_consumption_by_region_and_fe()
            .loc[:, "FE_liquid"]
            .reset_coords(drop=True),
        )
        .expand_dims({"NRG_COMMODITIES_I": ["FE_liquid"]}, 1)
        .values
    )
    value.loc[:, ["FE_solid_bio"]] = (
        (
            imv_final_energy_consumption_buildings_and_transport_top_down_coicop()
            .loc[:, "HH_SOLID_FUELS"]
            .reset_coords(drop=True)
            * share_energy_consumption_solid_bio_vs_solid_fossil()
        )
        .expand_dims({"NRG_COMMODITIES_I": ["FE_solid_bio"]}, 1)
        .values
    )
    value.loc[:, ["FE_solid_fossil"]] = (
        (
            imv_final_energy_consumption_buildings_and_transport_top_down_coicop()
            .loc[:, "HH_SOLID_FUELS"]
            .reset_coords(drop=True)
            * (1 - share_energy_consumption_solid_bio_vs_solid_fossil())
        )
        .expand_dims({"NRG_COMMODITIES_I": ["FE_solid_fossil"]}, 1)
        .values
    )
    return value


@component.add(
    name="IMV_HISTORIC_HOUSEHOLDS_FINAL_ENERGY",
    subscripts=["REGIONS_35_I", "NRG_FE_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_imv_historic_households_final_energy"},
)
def imv_historic_households_final_energy():
    return _ext_constant_imv_historic_households_final_energy()


_ext_constant_imv_historic_households_final_energy = ExtConstant(
    "model_parameters/energy/energy-end_use.xlsx",
    "Households_final_energy",
    "HISTORIC_HOUSEHOLDS_FINAL_ENERGY",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
    "_ext_constant_imv_historic_households_final_energy",
)


@component.add(
    name="IMV_PRICE_ELEC", units="DMNL", comp_type="Constant", comp_subtype="Normal"
)
def imv_price_elec():
    """
    Exogenous value of electricity price
    """
    return 100


@component.add(
    name="IMV_PRICE_GAS", units="DMNL", comp_type="Constant", comp_subtype="Normal"
)
def imv_price_gas():
    """
    Exogenous value of gas price
    """
    return 100


@component.add(
    name="IMV_PRICE_HEAT", units="dollars", comp_type="Constant", comp_subtype="Normal"
)
def imv_price_heat():
    """
    Exogenous value of heat price
    """
    return 100


@component.add(
    name="IMV_PRICE_HYDROGEN",
    units="dollars",
    comp_type="Constant",
    comp_subtype="Normal",
)
def imv_price_hydrogen():
    """
    Exogenous value of hydrogen price
    """
    return 100


@component.add(
    name="IMV_PRICE_LIQUID", units="DMNL", comp_type="Constant", comp_subtype="Normal"
)
def imv_price_liquid():
    """
    Exogenous value of liquid price
    """
    return 100


@component.add(
    name="IMV_PRICE_SOLID_BIO",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="Normal",
)
def imv_price_solid_bio():
    """
    Exogenous value of solid bio price
    """
    return 100


@component.add(
    name="IMV_PRICE_SOLID_FOSSIL",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="Normal",
)
def imv_price_solid_fossil():
    """
    Exogenous value of solid fossil price
    """
    return 100


@component.add(
    name="MINIMUM_ENERGY_EFFICIENCY_VERSUS_INITIAL",
    units="TJ/million$",
    subscripts=["REGIONS_35_I", "SECTORS_NON_ENERGY_I", "NRG_FE_I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def minimum_energy_efficiency_versus_initial():
    """
    Minimum value that the energy efficiency for each economic sector could reach, obviously always above zero. This minimum value is very difficult to estimate, but based on historical values it has been considered that it can reach 30% of the value of 2009. (Capellán-Pérez et al., 2014)
    """
    return xr.DataArray(
        0.3,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "SECTORS_NON_ENERGY_I": _subscript_dict["SECTORS_NON_ENERGY_I"],
            "NRG_FE_I": _subscript_dict["NRG_FE_I"],
        },
        ["REGIONS_35_I", "SECTORS_NON_ENERGY_I", "NRG_FE_I"],
    )


@component.add(
    name="price_final_energy",
    units="DMNL",
    subscripts=["REGIONS_35_I", "NRG_FE_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_energy": 7,
        "imv_price_elec": 2,
        "switch_eco2nrg_price_output": 7,
        "price_output": 6,
        "imv_price_gas": 2,
        "imv_price_heat": 2,
        "imv_price_hydrogen": 2,
        "imv_price_liquid": 2,
        "imv_price_solid_bio": 3,
        "imv_price_solid_fossil": 2,
    },
)
def price_final_energy():
    """
    Price by final energy obtaining for the price output corresponding sector: FE_elec: DISTRIBUTION_ELECTRICITY FE_gas: DISTRIBUTION_GAS FE_heat: STEAM_HOT_WATER FE_hydrogen: HYDROGEN_PRODUCTION FE_liquid: RFINING FE_solid_bio FE_solid_fossil:MINING_COAL
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "NRG_FE_I": _subscript_dict["NRG_FE_I"],
        },
        ["REGIONS_35_I", "NRG_FE_I"],
    )
    value.loc[:, ["FE_elec"]] = (
        if_then_else(
            switch_energy() == 0,
            lambda: xr.DataArray(
                imv_price_elec(),
                {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
                ["REGIONS_35_I"],
            ),
            lambda: if_then_else(
                switch_eco2nrg_price_output() == 0,
                lambda: xr.DataArray(
                    imv_price_elec(),
                    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
                    ["REGIONS_35_I"],
                ),
                lambda: price_output()
                .loc[:, "DISTRIBUTION_ELECTRICITY"]
                .reset_coords(drop=True),
            ),
        )
        .expand_dims({"FINAL_ENERGY_TRANSMISSION_I": ["FE_elec"]}, 1)
        .values
    )
    value.loc[:, ["FE_gas"]] = (
        if_then_else(
            switch_energy() == 0,
            lambda: xr.DataArray(
                imv_price_gas(),
                {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
                ["REGIONS_35_I"],
            ),
            lambda: if_then_else(
                switch_eco2nrg_price_output() == 0,
                lambda: xr.DataArray(
                    imv_price_gas(),
                    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
                    ["REGIONS_35_I"],
                ),
                lambda: price_output()
                .loc[:, "DISTRIBUTION_GAS"]
                .reset_coords(drop=True),
            ),
        )
        .expand_dims({"FINAL_ENERGY_TRANSMISSION_I": ["FE_gas"]}, 1)
        .values
    )
    value.loc[:, ["FE_heat"]] = (
        if_then_else(
            switch_energy() == 0,
            lambda: xr.DataArray(
                imv_price_heat(),
                {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
                ["REGIONS_35_I"],
            ),
            lambda: if_then_else(
                switch_eco2nrg_price_output() == 0,
                lambda: xr.DataArray(
                    imv_price_heat(),
                    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
                    ["REGIONS_35_I"],
                ),
                lambda: price_output()
                .loc[:, "STEAM_HOT_WATER"]
                .reset_coords(drop=True),
            ),
        )
        .expand_dims({"FINAL_ENERGY_TRANSMISSION_I": ["FE_heat"]}, 1)
        .values
    )
    value.loc[:, ["FE_hydrogen"]] = (
        if_then_else(
            switch_energy() == 0,
            lambda: xr.DataArray(
                imv_price_hydrogen(),
                {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
                ["REGIONS_35_I"],
            ),
            lambda: if_then_else(
                switch_eco2nrg_price_output() == 0,
                lambda: xr.DataArray(
                    imv_price_hydrogen(),
                    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
                    ["REGIONS_35_I"],
                ),
                lambda: price_output()
                .loc[:, "HYDROGEN_PRODUCTION"]
                .reset_coords(drop=True),
            ),
        )
        .expand_dims({"NRG_COMMODITIES_I": ["FE_hydrogen"]}, 1)
        .values
    )
    value.loc[:, ["FE_liquid"]] = (
        if_then_else(
            switch_energy() == 0,
            lambda: xr.DataArray(
                imv_price_liquid(),
                {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
                ["REGIONS_35_I"],
            ),
            lambda: if_then_else(
                switch_eco2nrg_price_output() == 0,
                lambda: xr.DataArray(
                    imv_price_liquid(),
                    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
                    ["REGIONS_35_I"],
                ),
                lambda: price_output().loc[:, "REFINING"].reset_coords(drop=True),
            ),
        )
        .expand_dims({"NRG_COMMODITIES_I": ["FE_liquid"]}, 1)
        .values
    )
    value.loc[:, ["FE_solid_bio"]] = if_then_else(
        switch_energy() == 0,
        lambda: imv_price_solid_bio(),
        lambda: if_then_else(
            switch_eco2nrg_price_output() == 0,
            lambda: imv_price_solid_bio(),
            lambda: imv_price_solid_bio(),
        ),
    )
    value.loc[:, ["FE_solid_fossil"]] = (
        if_then_else(
            switch_energy() == 0,
            lambda: xr.DataArray(
                imv_price_solid_fossil(),
                {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
                ["REGIONS_35_I"],
            ),
            lambda: if_then_else(
                switch_eco2nrg_price_output() == 0,
                lambda: xr.DataArray(
                    imv_price_solid_fossil(),
                    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
                    ["REGIONS_35_I"],
                ),
                lambda: price_output().loc[:, "MINING_COAL"].reset_coords(drop=True),
            ),
        )
        .expand_dims({"NRG_COMMODITIES_I": ["FE_solid_fossil"]}, 1)
        .values
    )
    return value


@component.add(
    name="RELATIVE_ENERGY_INTENSITY_2015",
    units="DMNL",
    subscripts=["SECTORS_I", "NRG_FE_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_relative_energy_intensity_2015"},
)
def relative_energy_intensity_2015():
    """
    Exogenous variable that estimates the final energy intensity ratio beetween the different final energies. These data are the key to the disaggregation in 2015 between the two components of the final energy intensity: energy efficiency and final energy substitution. The data are provisional and should be updated in the next WILIAM version.
    """
    return _ext_constant_relative_energy_intensity_2015()


_ext_constant_relative_energy_intensity_2015 = ExtConstant(
    "model_parameters/energy/energy-end_use.xlsx",
    "Relative_energy_intensity_2015",
    "RELATIVE_ENERGY_INTENSITY_2015",
    {
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
    _root,
    {
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
    "_ext_constant_relative_energy_intensity_2015",
)


@component.add(
    name="SELECT_FINAL_ENERGY_SUBSTITUTION_SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_select_final_energy_substitution_sp"},
)
def select_final_energy_substitution_sp():
    """
    Select final energy substitution policy option: 0: No final energy substitution 1: Final energy substitution follows historical trends* 2: Final energy substitution defined by user: FINAL ENERGY SUBSTITUTION* *The evolution of the final energy substitution is not only exogenous defiened by those variables, it also depends endogenously on the final energy prices
    """
    return _ext_constant_select_final_energy_substitution_sp()


_ext_constant_select_final_energy_substitution_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "SELECT_FINAL_ENERGY_SUBSTITUTION_SP",
    {},
    _root,
    {},
    "_ext_constant_select_final_energy_substitution_sp",
)


@component.add(
    name="share_final_energy_demand_by_sector_and_FE",
    units="DMNL",
    subscripts=["REGIONS_35_I", "SECTORS_NON_ENERGY_I", "NRG_FE_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "final_energy_demand_by_sector_and_fe": 1,
        "total_final_energy_demand_by_sector": 1,
    },
)
def share_final_energy_demand_by_sector_and_fe():
    """
    Share of each final enegy demand in the total final energy demand by sector
    """
    return zidz(
        final_energy_demand_by_sector_and_fe(),
        total_final_energy_demand_by_sector().expand_dims(
            {"NRG_FE_I": _subscript_dict["NRG_FE_I"]}, 2
        ),
    )


@component.add(
    name="START_YEAR_ENERGY_EFFICIENCY_ANNUAL_IMPROVEMENT_SP",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_start_year_energy_efficiency_annual_improvement_sp"
    },
)
def start_year_energy_efficiency_annual_improvement_sp():
    """
    Start year energy effiency annual improvement policy
    """
    return _ext_constant_start_year_energy_efficiency_annual_improvement_sp()


_ext_constant_start_year_energy_efficiency_annual_improvement_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "START_YEAR_ENERGY_EFFICIENCY_ANNUAL_IMPROVEMENT_SP",
    {},
    _root,
    {},
    "_ext_constant_start_year_energy_efficiency_annual_improvement_sp",
)


@component.add(
    name="START_YEAR_FINAL_ENERGY_SUBSTITUTION_SP",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_start_year_final_energy_substitution_sp"
    },
)
def start_year_final_energy_substitution_sp():
    """
    Start year final energy subsitution policy
    """
    return _ext_constant_start_year_final_energy_substitution_sp()


_ext_constant_start_year_final_energy_substitution_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "START_YEAR_FINAL_ENERGY_SUBSTITUTION_SP",
    {},
    _root,
    {},
    "_ext_constant_start_year_final_energy_substitution_sp",
)


@component.add(
    name="SWITCH_ECO2NRG_OUTPUT_REAL",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_eco2nrg_output_real"},
)
def switch_eco2nrg_output_real():
    """
    This switch can take two values: 0: the (sub)module runs isolated from the rest of WILIAM, replacing inter(sub)module variables with exogenous parameters. 1: the (sub)module runs integrated with the rest of WILIAM
    """
    return _ext_constant_switch_eco2nrg_output_real()


_ext_constant_switch_eco2nrg_output_real = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_ECO2NRG_OUTPUT_REAL",
    {},
    _root,
    {},
    "_ext_constant_switch_eco2nrg_output_real",
)


@component.add(
    name="SWITCH_ECO2NRG_PRICE_OUTPUT",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_eco2nrg_price_output"},
)
def switch_eco2nrg_price_output():
    return _ext_constant_switch_eco2nrg_price_output()


_ext_constant_switch_eco2nrg_price_output = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_ECO2NRG_PRICE_OUTPUT",
    {},
    _root,
    {},
    "_ext_constant_switch_eco2nrg_price_output",
)


@component.add(
    name="SWITCH_ENERGY",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_energy"},
)
def switch_energy():
    """
    This switch can take two values: 0: the module runs isolated from the rest of WILIAM, replacing inter(sub)module variables with exogenous parameters. 1: the module runs integrated with the rest of WILIAM.
    """
    return _ext_constant_switch_energy()


_ext_constant_switch_energy = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_ENERGY",
    {},
    _root,
    {},
    "_ext_constant_switch_energy",
)


@component.add(
    name="SWITCH_LAW2NRG_AVAILABLE_FORESTRY_FOR_ENERGY",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_switch_law2nrg_available_forestry_for_energy"
    },
)
def switch_law2nrg_available_forestry_for_energy():
    return _ext_constant_switch_law2nrg_available_forestry_for_energy()


_ext_constant_switch_law2nrg_available_forestry_for_energy = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_LAW2NRG_AVAILABLE_FORESTRY_FOR_ENERGY",
    {},
    _root,
    {},
    "_ext_constant_switch_law2nrg_available_forestry_for_energy",
)


@component.add(
    name="total_energy_transport_consumption",
    units="TJ/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"households_final_energy_demand_by_fe": 1},
)
def total_energy_transport_consumption():
    return sum(
        households_final_energy_demand_by_fe().rename(
            {"REGIONS_35_I": "REGIONS_35_I!", "NRG_FE_I": "NRG_FE_I!"}
        ),
        dim=["REGIONS_35_I!", "NRG_FE_I!"],
    )


@component.add(
    name="total_FES",
    units="DMNL",
    subscripts=["REGIONS_35_I", "SECTORS_NON_ENERGY_I", "NRG_FE_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"final_energy_substitution_component": 1},
)
def total_fes():
    """
    Total final energy substitution by sector and final energy estimated with a top-down approach
    """
    return sum(
        final_energy_substitution_component().rename({"NRG_FE_I": "NRG_FE_I!"}),
        dim=["NRG_FE_I!"],
    ).expand_dims({"NRG_FE_I": _subscript_dict["NRG_FE_I"]}, 2)


@component.add(
    name="total_final_energy_demand_by_sector",
    units="TJ/Year",
    subscripts=["REGIONS_35_I", "SECTORS_NON_ENERGY_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"final_energy_demand_by_sector_and_fe": 1},
)
def total_final_energy_demand_by_sector():
    """
    Final energy demand by sector estimated with a top-down approach
    """
    return sum(
        final_energy_demand_by_sector_and_fe().rename({"NRG_FE_I": "NRG_FE_I!"}),
        dim=["NRG_FE_I!"],
    )


@component.add(
    name="total_final_energy_intensities_by_sector",
    units="TJ/million$",
    subscripts=["REGIONS_35_I", "SECTORS_NON_ENERGY_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"final_energy_intensities_by_sector_and_fe": 1},
)
def total_final_energy_intensities_by_sector():
    """
    Final energy intensities by sector estimated with a top-down approach
    """
    return sum(
        final_energy_intensities_by_sector_and_fe().rename({"NRG_FE_I": "NRG_FE_I!"}),
        dim=["NRG_FE_I!"],
    )


@component.add(
    name="trend_of_final_energy_substituion_annual_variation",
    units="1/Year",
    subscripts=["REGIONS_35_I", "NRG_FE_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 2,
        "select_final_energy_substitution_sp": 2,
        "historical_final_energy_substitution": 2,
        "final_energy_substitution_sp": 1,
        "start_year_final_energy_substitution_sp": 1,
    },
)
def trend_of_final_energy_substituion_annual_variation():
    """
    Estimated final energy annunal substitution by final energy as a function of the exogenous policies
    """
    return if_then_else(
        time() < 2015,
        lambda: xr.DataArray(
            0,
            {
                "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                "NRG_FE_I": _subscript_dict["NRG_FE_I"],
            },
            ["REGIONS_35_I", "NRG_FE_I"],
        ),
        lambda: if_then_else(
            select_final_energy_substitution_sp() == 0,
            lambda: xr.DataArray(
                0,
                {
                    "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                    "NRG_FE_I": _subscript_dict["NRG_FE_I"],
                },
                ["REGIONS_35_I", "NRG_FE_I"],
            ),
            lambda: if_then_else(
                select_final_energy_substitution_sp() == 1,
                lambda: historical_final_energy_substitution(),
                lambda: if_then_else(
                    time() < start_year_final_energy_substitution_sp(),
                    lambda: historical_final_energy_substitution(),
                    lambda: final_energy_substitution_sp(),
                ),
            ),
        ),
    )


@component.add(
    name="variation_energy_efficiency_component",
    units="TJ/million$/Year",
    subscripts=["REGIONS_35_I", "SECTORS_NON_ENERGY_I", "NRG_FE_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "energy_efficiency_annual_improvement": 3,
        "energy_efficiengy_component_2015": 2,
        "minimum_energy_efficiency_versus_initial": 1,
        "energy_efficiency_component": 1,
    },
)
def variation_energy_efficiency_component():
    """
    Variation of the energy efficiency by sector and final energy as a function of the historical trends and exogenous policies.
    """
    return if_then_else(
        time() < 2015,
        lambda: xr.DataArray(
            0,
            {
                "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                "SECTORS_NON_ENERGY_I": _subscript_dict["SECTORS_NON_ENERGY_I"],
                "NRG_FE_I": _subscript_dict["NRG_FE_I"],
            },
            ["REGIONS_35_I", "SECTORS_NON_ENERGY_I", "NRG_FE_I"],
        ),
        lambda: if_then_else(
            (energy_efficiency_annual_improvement() < 0)
            .expand_dims(
                {"SECTORS_NON_ENERGY_I": _subscript_dict["SECTORS_NON_ENERGY_I"]}, 1
            )
            .expand_dims({"NRG_FE_I": _subscript_dict["NRG_FE_I"]}, 2),
            lambda: energy_efficiency_annual_improvement()
            * (
                energy_efficiency_component()
                - minimum_energy_efficiency_versus_initial()
                * energy_efficiengy_component_2015()
            ),
            lambda: energy_efficiency_annual_improvement()
            * energy_efficiengy_component_2015(),
        ),
    )


@component.add(
    name="variation_energy_intensity_by_sector_and_FE",
    units="TJ/million$/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I", "NRG_FE_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "final_energy_substitution_component": 1,
        "variation_energy_efficiency_component": 1,
        "variation_final_energy_substitution_component": 1,
        "energy_efficiency_component": 1,
    },
)
def variation_energy_intensity_by_sector_and_fe():
    """
    Variation of the final energy intensities by sector and final energy as a function of the energy efficiencies and the final energy substitution.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "SECTORS_I": _subscript_dict["SECTORS_I"],
            "NRG_FE_I": _subscript_dict["NRG_FE_I"],
        },
        ["REGIONS_35_I", "SECTORS_I", "NRG_FE_I"],
    )
    value.loc[:, _subscript_dict["SECTORS_NON_ENERGY_I"], :] = (
        final_energy_substitution_component() * variation_energy_efficiency_component()
        + energy_efficiency_component()
        * variation_final_energy_substitution_component()
    ).values
    value.loc[:, _subscript_dict["SECTORS_ENERGY_I"], :] = 0
    return value


@component.add(
    name="variation_final_energy_substitution_component",
    units="1/Year",
    subscripts=["REGIONS_35_I", "SECTORS_NON_ENERGY_I", "NRG_FE_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "final_energy_substitution_component_aux": 2,
        "final_energy_substitution_component": 1,
    },
)
def variation_final_energy_substitution_component():
    """
    Variation of the final energy substitution by sector and final energy as a function of the historical trends, the final energy prioces and exogenous policies.
    """
    return (
        zidz(
            final_energy_substitution_component_aux(),
            sum(
                final_energy_substitution_component_aux().rename(
                    {"NRG_FE_I": "NRG_FE_I!"}
                ),
                dim=["NRG_FE_I!"],
            ).expand_dims({"NRG_FE_I": _subscript_dict["NRG_FE_I"]}, 2),
        )
        - final_energy_substitution_component()
    )
