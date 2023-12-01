"""
Module energy_variability.proflex_allocation
Translated using PySD version 3.10.0
"""


@component.add(
    name="CF_PROSUP_FLEXOPT",
    units="DMNL",
    subscripts=["REGIONS_9_I", "NRG_PRO_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cf_prosup_elec2heat": 1,
        "cf_flexible_electrolysers": 1,
        "cf_v2g_storage_9r": 1,
        "cf_prosto": 1,
    },
)
def cf_prosup_flexopt():
    """
    CF of flexibility options.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "NRG_PRO_I": _subscript_dict["NRG_PRO_I"],
        },
        ["REGIONS_9_I", "NRG_PRO_I"],
    )
    value.loc[:, _subscript_dict["PROSUP_P2H_I"]] = (
        cf_prosup_elec2heat()
        .expand_dims({"PROSUP_P2H_I": _subscript_dict["PROSUP_P2H_I"]}, 1)
        .values
    )
    value.loc[:, ["PROSUP_elec_2_hydrogen"]] = (
        cf_flexible_electrolysers()
        .expand_dims({"NRG_PRO_I": ["PROSUP_elec_2_hydrogen"]}, 1)
        .values
    )
    value.loc[:, ["PROSTO_V2G"]] = (
        cf_v2g_storage_9r().expand_dims({"NRG_PRO_I": ["PROSTO_V2G"]}, 1).values
    )
    value.loc[:, _subscript_dict["PROSTO_ELEC_DEDICATED_I"]] = (
        cf_prosto()
        .loc[:, _subscript_dict["PROSTO_ELEC_DEDICATED_I"]]
        .rename({"NRG_PROSTO_I": "PROSTO_ELEC_DEDICATED_I"})
        .values
    )
    value.loc[:, ["PROSUP_DSM"]] = 1
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, _subscript_dict["PRO_FLEXOPT_I"]] = False
    value.values[except_subs.values] = 0
    return value


@component.add(
    name="curtailement_TO_elec_power_system",
    units="TW*h/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_capacity_stock": 4,
        "protra_max_full_load_hours_curtailed": 4,
        "protra_max_full_load_hours": 4,
    },
)
def curtailement_to_elec_power_system():
    """
    Energy curtailed by year.
    """
    return (
        protra_capacity_stock()
        .loc[:, "TO_elec", "PROTRA_PP_wind_offshore"]
        .reset_coords(drop=True)
        * (
            protra_max_full_load_hours()
            .loc[:, "PROTRA_PP_wind_offshore"]
            .reset_coords(drop=True)
            - protra_max_full_load_hours_curtailed()
            .loc[:, "PROTRA_PP_wind_offshore"]
            .reset_coords(drop=True)
        )
        + protra_capacity_stock()
        .loc[:, "TO_elec", "PROTRA_PP_wind_onshore"]
        .reset_coords(drop=True)
        * (
            protra_max_full_load_hours()
            .loc[:, "PROTRA_PP_wind_onshore"]
            .reset_coords(drop=True)
            - protra_max_full_load_hours_curtailed()
            .loc[:, "PROTRA_PP_wind_onshore"]
            .reset_coords(drop=True)
        )
        + protra_capacity_stock()
        .loc[:, "TO_elec", "PROTRA_PP_solar_CSP"]
        .reset_coords(drop=True)
        * (
            protra_max_full_load_hours()
            .loc[:, "PROTRA_PP_solar_CSP"]
            .reset_coords(drop=True)
            - protra_max_full_load_hours_curtailed()
            .loc[:, "PROTRA_PP_solar_CSP"]
            .reset_coords(drop=True)
        )
        + protra_capacity_stock()
        .loc[:, "TO_elec", "PROTRA_PP_solar_open_space_PV"]
        .reset_coords(drop=True)
        * (
            protra_max_full_load_hours()
            .loc[:, "PROTRA_PP_solar_open_space_PV"]
            .reset_coords(drop=True)
            - protra_max_full_load_hours_curtailed()
            .loc[:, "PROTRA_PP_solar_open_space_PV"]
            .reset_coords(drop=True)
        )
    )


@component.add(
    name="delayed_PROFLEX_DSM_capacity",
    units="Year*TWh/h",
    subscripts=["REGIONS_9_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_proflex_dsm_capacity": 1},
    other_deps={
        "_delayfixed_delayed_proflex_dsm_capacity": {
            "initial": {},
            "step": {"proflex_dsm_capacity": 1},
        }
    },
)
def delayed_proflex_dsm_capacity():
    """
    Delayed 1 year demand-side management (DSM) capacity.
    """
    return _delayfixed_delayed_proflex_dsm_capacity()


_delayfixed_delayed_proflex_dsm_capacity = DelayFixed(
    lambda: proflex_dsm_capacity(),
    lambda: 1,
    lambda: xr.DataArray(
        0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
    ),
    time_step,
    "_delayfixed_delayed_proflex_dsm_capacity",
)


@component.add(
    name="INITIAL_YEAR_FLEX_ELEC_DEMAND_SP",
    units="Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_year_flex_elec_demand_sp"},
)
def initial_year_flex_elec_demand_sp():
    """
    Initial year of the policy scenario for flexible electricity demand
    """
    return _ext_constant_initial_year_flex_elec_demand_sp()


_ext_constant_initial_year_flex_elec_demand_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "INITIAL_YEAR_FLEX_ELEC_DEMAND_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_initial_year_flex_elec_demand_sp",
)


@component.add(
    name="MINIMUM_PROFLEX_CAPACITY_EXPANSION_SP",
    units="TW/Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_minimum_proflex_capacity_expansion_sp"},
)
def minimum_proflex_capacity_expansion_sp():
    """
    Minimum potential of new expansion capacity for flexibility options
    """
    return _ext_constant_minimum_proflex_capacity_expansion_sp()


_ext_constant_minimum_proflex_capacity_expansion_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "MINIMUM_PROFLEX_CAPACITY_EXPANSION_SP",
    {},
    _root,
    {},
    "_ext_constant_minimum_proflex_capacity_expansion_sp",
)


@component.add(
    name="OBJECTIVE_FLEX_ELEC_DEMAND_SP",
    units="TWh",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_objective_flex_elec_demand_sp"},
)
def objective_flex_elec_demand_sp():
    """
    Objective value of the policy scenario for flexible electricity demand
    """
    return _ext_constant_objective_flex_elec_demand_sp()


_ext_constant_objective_flex_elec_demand_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "OBJECTIVE_FLEX_ELEC_DEMAND_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_objective_flex_elec_demand_sp",
)


@component.add(
    name="PROFLEX_capacity_expansion",
    units="TW/Year",
    subscripts=["REGIONS_9_I", "PRO_FLEXOPT_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "prosup_p2h_capacity_expansion": 1,
        "flexible_electrolysers_capacity_expansion": 1,
        "ev_batteries_power_v2g_9r": 1,
        "prosto_dedicated_capacity_expansion": 1,
        "proflex_dsm_capacity": 1,
        "delayed_proflex_dsm_capacity": 1,
    },
)
def proflex_capacity_expansion():
    """
    Annual capacity expansion of options to manage variability. For all processes using hydrogen from electrolyzers (e.g., synthetic fuels) only the cost for producing electrolyzers is included,
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "PRO_FLEXOPT_I": _subscript_dict["PRO_FLEXOPT_I"],
        },
        ["REGIONS_9_I", "PRO_FLEXOPT_I"],
    )
    value.loc[
        :, _subscript_dict["PROSUP_P2H_I"]
    ] = prosup_p2h_capacity_expansion().values
    value.loc[:, ["PROSUP_elec_2_hydrogen"]] = (
        flexible_electrolysers_capacity_expansion()
        .expand_dims({"NRG_PRO_I": ["PROSUP_elec_2_hydrogen"]}, 1)
        .values
    )
    value.loc[:, ["PROSTO_V2G"]] = (
        ev_batteries_power_v2g_9r().expand_dims({"NRG_PRO_I": ["PROSTO_V2G"]}, 1).values
    )
    value.loc[
        :, _subscript_dict["PROSTO_ELEC_DEDICATED_I"]
    ] = prosto_dedicated_capacity_expansion().values
    value.loc[:, ["PROSUP_DSM"]] = (
        np.maximum(0, proflex_dsm_capacity() - delayed_proflex_dsm_capacity())
        .expand_dims({"NRG_PRO_I": ["PROSUP_DSM"]}, 1)
        .values
    )
    return value


@component.add(
    name="PROFLEX_DSM_capacity",
    units="Year*TWh/h",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_flex_elec_demand_sp": 3,
        "time": 3,
        "objective_flex_elec_demand_sp": 2,
        "initial_year_flex_elec_demand_sp": 3,
        "year_final_flex_elec_demand_sp": 3,
        "unit_conversion_hours_year": 1,
    },
)
def proflex_dsm_capacity():
    """
    Average hourly load for demand side management. Proxy of "installed capacity" of demand side management.
    """
    return (
        if_then_else(
            switch_flex_elec_demand_sp() == 0,
            lambda: xr.DataArray(
                0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
            ),
            lambda: if_then_else(
                np.logical_and(
                    switch_flex_elec_demand_sp() == 1,
                    time() < initial_year_flex_elec_demand_sp(),
                ),
                lambda: xr.DataArray(
                    0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
                ),
                lambda: if_then_else(
                    np.logical_and(
                        switch_flex_elec_demand_sp() == 1,
                        time() > year_final_flex_elec_demand_sp(),
                    ),
                    lambda: objective_flex_elec_demand_sp(),
                    lambda: ramp(
                        __data["time"],
                        objective_flex_elec_demand_sp()
                        / (
                            year_final_flex_elec_demand_sp()
                            - initial_year_flex_elec_demand_sp()
                        ),
                        initial_year_flex_elec_demand_sp(),
                        year_final_flex_elec_demand_sp(),
                    ),
                ),
            ),
        )
        / unit_conversion_hours_year()
    )


@component.add(
    name="PROFLEX_potential_capacity_expansion",
    units="TW/Year",
    subscripts=["REGIONS_9_I", "NRG_COMMODITIES_I", "NRG_PRO_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "maximum_capacity_expansion_p2h": 1,
        "prosup_p2h_capacity_decomissioning": 1,
        "select_availability_unmature_energy_technologies_sp": 2,
        "ratio_maximum_proflex_expansion_sp": 3,
        "flexible_electrolysers_capacity_stock": 1,
        "flexible_electrolysers_capacity_decommissioning": 1,
        "minimum_proflex_capacity_expansion_sp": 1,
        "maximum_prosto_dedicated": 2,
        "prosto_dedicated_capacity_stock": 2,
        "prosto_dedicated_capacity_decomissioning": 2,
    },
)
def proflex_potential_capacity_expansion():
    """
    Installed capacities of flexibility options. V2G is zero because it is already endogenous. P2H is based on the final heat demand. The last equation (DSM) is zero because this is an exogenous policy assumption. In order to not duplicate, electrolysers are only assigned to PROSUP_elec_2_hydrogen.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "NRG_COMMODITIES_I": _subscript_dict["NRG_COMMODITIES_I"],
            "NRG_PRO_I": _subscript_dict["NRG_PRO_I"],
        },
        ["REGIONS_9_I", "NRG_COMMODITIES_I", "NRG_PRO_I"],
    )
    value.loc[:, ["TO_elec"], _subscript_dict["PROSUP_P2H_I"]] = (
        np.maximum(
            maximum_capacity_expansion_p2h() - prosup_p2h_capacity_decomissioning(), 0
        )
        .expand_dims({"NRG_COMMODITIES_I": ["TO_elec"]}, 1)
        .values
    )
    value.loc[:, ["TO_elec"], ["PROSUP_elec_2_hydrogen"]] = (
        if_then_else(
            np.logical_or(
                select_availability_unmature_energy_technologies_sp() == 1,
                select_availability_unmature_energy_technologies_sp() == 2,
            ),
            lambda: np.maximum(
                np.maximum(
                    flexible_electrolysers_capacity_stock()
                    * ratio_maximum_proflex_expansion_sp()
                    - flexible_electrolysers_capacity_decommissioning(),
                    minimum_proflex_capacity_expansion_sp(),
                ),
                0,
            ),
            lambda: xr.DataArray(
                0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
            ),
        )
        .expand_dims({"NRG_COMMODITIES_I": ["TO_elec"]}, 1)
        .expand_dims({"NRG_PRO_I": ["PROSUP_elec_2_hydrogen"]}, 2)
        .values
    )
    value.loc[:, ["TO_elec"], ["PROSTO_V2G"]] = 0
    value.loc[:, ["TO_elec"], ["PROSTO_PHS"]] = (
        np.maximum(
            (
                maximum_prosto_dedicated().loc[:, "PROSTO_PHS"].reset_coords(drop=True)
                - prosto_dedicated_capacity_stock()
                .loc[:, "PROSTO_PHS"]
                .reset_coords(drop=True)
            )
            * ratio_maximum_proflex_expansion_sp()
            - prosto_dedicated_capacity_decomissioning()
            .loc[:, "PROSTO_PHS"]
            .reset_coords(drop=True),
            0,
        )
        .expand_dims({"NRG_COMMODITIES_I": ["TO_elec"]}, 1)
        .expand_dims({"NRG_PRO_I": ["PROSTO_PHS"]}, 2)
        .values
    )
    value.loc[:, ["TO_elec"], ["PROSTO_STATIONARY_BATTERIES"]] = (
        np.maximum(
            (
                maximum_prosto_dedicated()
                .loc[:, "PROSTO_STATIONARY_BATTERIES"]
                .reset_coords(drop=True)
                - prosto_dedicated_capacity_stock()
                .loc[:, "PROSTO_STATIONARY_BATTERIES"]
                .reset_coords(drop=True)
            )
            * ratio_maximum_proflex_expansion_sp()
            - prosto_dedicated_capacity_decomissioning()
            .loc[:, "PROSTO_STATIONARY_BATTERIES"]
            .reset_coords(drop=True),
            0,
        )
        .expand_dims({"NRG_COMMODITIES_I": ["TO_elec"]}, 1)
        .expand_dims({"NRG_PRO_I": ["PROSTO_STATIONARY_BATTERIES"]}, 2)
        .values
    )
    value.loc[:, ["TO_elec"], ["PROSUP_DSM"]] = 0
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, ["TO_elec"], _subscript_dict["PRO_FLEXOPT_I"]] = False
    value.values[except_subs.values] = 0
    return value


@component.add(
    name="PROSUP_CAPACITY_EXPANSION_ALLOCATION_POLICY_PWIDTH_SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_prosup_capacity_expansion_allocation_policy_pwidth_sp"
    },
)
def prosup_capacity_expansion_allocation_policy_pwidth_sp():
    """
    Width for the allocation functions of flexibility options
    """
    return _ext_constant_prosup_capacity_expansion_allocation_policy_pwidth_sp()


_ext_constant_prosup_capacity_expansion_allocation_policy_pwidth_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "PROSUP_CAPACITY_EXPANSION_ALLOCATION_POLICY_PWIDTH_SP",
    {},
    _root,
    {},
    "_ext_constant_prosup_capacity_expansion_allocation_policy_pwidth_sp",
)


@component.add(
    name="PROSUP_FLEXOPT_CAPACITY_EXPANSION_POLICY_PRIORITIES_SP",
    units="Dnml",
    subscripts=["REGIONS_9_I", "PRO_FLEXOPT_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_prosup_flexopt_capacity_expansion_policy_priorities_sp"
    },
)
def prosup_flexopt_capacity_expansion_policy_priorities_sp():
    """
    Priorities to allocate new capacity requirements into the existing flexibility options
    """
    return _ext_constant_prosup_flexopt_capacity_expansion_policy_priorities_sp()


_ext_constant_prosup_flexopt_capacity_expansion_policy_priorities_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "PROSUP_FLEXOPT_CAPACITY_EXPANSION_POLICY_PRIORITIES_SP*",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PRO_FLEXOPT_I": _subscript_dict["PRO_FLEXOPT_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PRO_FLEXOPT_I": _subscript_dict["PRO_FLEXOPT_I"],
    },
    "_ext_constant_prosup_flexopt_capacity_expansion_policy_priorities_sp",
)


@component.add(
    name="PROSUP_FLEXOPT_elec_capacity_expansion",
    units="TW/Year",
    subscripts=["REGIONS_9_I", "PRO_FLEXOPT_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "prosup_flexopt_elec_curtailment_allocation": 1,
        "cf_prosup_flexopt": 1,
    },
)
def prosup_flexopt_elec_capacity_expansion():
    """
    Allocate of the capacity expansion for power flexibility options taking into account the CF.
    """
    return zidz(
        prosup_flexopt_elec_curtailment_allocation()
        .loc[:, "TO_elec", _subscript_dict["PRO_FLEXOPT_I"]]
        .reset_coords(drop=True)
        .rename({"NRG_PRO_I": "PRO_FLEXOPT_I"}),
        cf_prosup_flexopt()
        .loc[:, _subscript_dict["PRO_FLEXOPT_I"]]
        .rename({"NRG_PRO_I": "PRO_FLEXOPT_I"}),
    )


@component.add(
    name="PROSUP_FLEXOPT_elec_curtailment_allocation",
    units="TW/Year",
    subscripts=["REGIONS_9_I", "NRG_TO_I", "NRG_PRO_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "proflex_potential_capacity_expansion": 1,
        "prosup_flexopt_priority_vector": 1,
        "required_capacity_expansion_flexibility_options": 1,
    },
)
def prosup_flexopt_elec_curtailment_allocation():
    """
    Allocate of the capacity expansion (as it would work 100% CF) for power flexibility options
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "NRG_TO_I": _subscript_dict["NRG_TO_I"],
            "NRG_PRO_I": _subscript_dict["NRG_PRO_I"],
        },
        ["REGIONS_9_I", "NRG_TO_I", "NRG_PRO_I"],
    )
    value.loc[:, ["TO_elec"], :] = (
        allocate_available(
            proflex_potential_capacity_expansion()
            .loc[:, "TO_elec", :]
            .reset_coords(drop=True),
            prosup_flexopt_priority_vector(),
            required_capacity_expansion_flexibility_options()
            .loc[:, "TO_elec"]
            .reset_coords(drop=True),
        )
        .expand_dims({"NRG_COMMODITIES_I": ["TO_elec"]}, 1)
        .values
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, ["TO_elec"], :] = False
    value.values[except_subs.values] = 0
    return value


@component.add(
    name="PROSUP_FLEXOPT_priority_vector",
    subscripts=["REGIONS_9_I", "NRG_PRO_I", "pprofile"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "prosup_flexopt_capacity_expansion_policy_priorities_sp": 1,
        "prosup_capacity_expansion_allocation_policy_pwidth_sp": 1,
    },
)
def prosup_flexopt_priority_vector():
    """
    Vector of parameters for the allocate of capacity expansion of flexibility options
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "NRG_PRO_I": _subscript_dict["NRG_PRO_I"],
            "pprofile": _subscript_dict["pprofile"],
        },
        ["REGIONS_9_I", "NRG_PRO_I", "pprofile"],
    )
    value.loc[:, :, ["ptype"]] = 3
    value.loc[:, _subscript_dict["PRO_FLEXOPT_I"], ["ppriority"]] = (
        prosup_flexopt_capacity_expansion_policy_priorities_sp()
        .expand_dims({"pprofile": ["ppriority"]}, 2)
        .values
    )
    value.loc[
        :, :, ["pwidth"]
    ] = prosup_capacity_expansion_allocation_policy_pwidth_sp()
    value.loc[:, :, ["pextra"]] = 0
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[:, :, ["ppriority"]] = True
    except_subs.loc[:, _subscript_dict["PRO_FLEXOPT_I"], ["ppriority"]] = False
    value.values[except_subs.values] = 0
    return value


@component.add(
    name="RATIO_MAXIMUM_PROFLEX_EXPANSION_SP",
    units="1/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_ratio_maximum_proflex_expansion_sp"},
)
def ratio_maximum_proflex_expansion_sp():
    """
    Maximum ratio of the installed capacity of flexibility options that can be installed in the year
    """
    return _ext_constant_ratio_maximum_proflex_expansion_sp()


_ext_constant_ratio_maximum_proflex_expansion_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "RATIO_MAXIMUM_PROFLEX_EXPANSION_SP",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_ratio_maximum_proflex_expansion_sp",
)


@component.add(
    name="required_capacity_expansion_flexibility_options",
    units="TW/Year",
    subscripts=["REGIONS_9_I", "NRG_COMMODITIES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "curtailement_to_elec_power_system": 1,
        "unit_conversion_hours_year": 1,
        "one_year": 1,
    },
)
def required_capacity_expansion_flexibility_options():
    """
    Equivalent capacity to the curtailed energy per year. This is the trigger variable to expand the installed capacities of flexible power plants. EnergyPLAN --> equivalent to the CEEP before strategy decisions. MAX(SUM(PROTRA_capacity_stock[REGIONS_9_I,TO_elec,NRG_PROTRA_I!] * UNIT_CONVERSION_TW_PER_EJ_PER_YEAR * (protra_max_full_load_hours_curtailed[REGIONS_9_I,NRG_PROTRA_I!] - protra_max_full_load_hours_after_constraints[REGIONS_9_I ,NRG_PROTRA_I!]) ) * UNIT_CONVERSION_TWh_EJ / UNIT_CONVERSION_HOURS_YEAR, 0)
    """
    return (
        curtailement_to_elec_power_system() / unit_conversion_hours_year() / one_year()
    ).expand_dims({"NRG_COMMODITIES_I": ["TO_elec"]}, 1)


@component.add(
    name="share_curtailment_TO_elec",
    units="1",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "curtailement_to_elec_power_system": 1,
        "unit_conversion_twh_ej": 1,
        "to_by_commodity": 1,
    },
)
def share_curtailment_to_elec():
    """
    Share of curtailed electricity by region with relation to the total production.
    """
    return zidz(
        curtailement_to_elec_power_system(),
        to_by_commodity().loc[:, "TO_elec"].reset_coords(drop=True)
        * unit_conversion_twh_ej(),
    )


@component.add(
    name="SWITCH_FLEX_ELEC_DEMAND_SP",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_flex_elec_demand_sp"},
)
def switch_flex_elec_demand_sp():
    """
    Switch of the policy for the policy of flexible electricity demand
    """
    return _ext_constant_switch_flex_elec_demand_sp()


_ext_constant_switch_flex_elec_demand_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "SWITCH_FLEX_ELEC_DEMAND_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_switch_flex_elec_demand_sp",
)


@component.add(
    name="YEAR_FINAL_FLEX_ELEC_DEMAND_SP",
    units="Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_year_final_flex_elec_demand_sp"},
)
def year_final_flex_elec_demand_sp():
    """
    Final year of the policy scenario for flexible electricity demand
    """
    return _ext_constant_year_final_flex_elec_demand_sp()


_ext_constant_year_final_flex_elec_demand_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "YEAR_FINAL_FLEX_ELEC_DEMAND_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_year_final_flex_elec_demand_sp",
)
