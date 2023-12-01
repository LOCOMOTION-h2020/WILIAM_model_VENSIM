"""
Module energy.electrolyzers_h2_production
Translated using PySD version 3.10.0
"""


@component.add(
    name="allocation_pure_hydrogen_by_process",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "PROSUP_H2_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "h2_production_from_stationary_electrolyzers_by_prosup_h2": 1,
        "h2_production_from_flexible_electrolysers": 1,
        "share_hydrogen_commodity_by_process": 1,
    },
)
def allocation_pure_hydrogen_by_process():
    """
    Distribution of pure hydrogen (commodity) to different processes.
    """
    return (
        h2_production_from_stationary_electrolyzers_by_prosup_h2()
        + h2_production_from_flexible_electrolysers()
    ) * share_hydrogen_commodity_by_process()


@component.add(
    name="CF_electrolysers_CEEP",
    units="1",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "hydrogen_ceep_scaled": 1,
        "unit_conversion_hours_year": 1,
        "flexible_electrolysers_capacity_stock": 1,
    },
)
def cf_electrolysers_ceep():
    """
    CF of electrolysers used as flexibility option in regresions, CEEP (critical excess of electricity production in EnergyPLAN). EnergyPLAN works with 8784 hours in the (leap) year
    """
    return zidz(
        hydrogen_ceep_scaled(),
        flexible_electrolysers_capacity_stock() * (unit_conversion_hours_year() + 24),
    )


@component.add(
    name="CF_EXOGENOUS_FLEXIBLE_ELECTROLYSERS",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_cf_exogenous_flexible_electrolysers"},
)
def cf_exogenous_flexible_electrolysers():
    """
    Exogenous capacity factor flexible electrolysers. A very low value similar to those of PHS currently is set as first approximation.
    """
    return _ext_constant_cf_exogenous_flexible_electrolysers()


_ext_constant_cf_exogenous_flexible_electrolysers = ExtConstant(
    "model_parameters/energy/energy-hydrogen.xlsx",
    "hydrogen_supply",
    "CF_FLEXIBLE_ELECTROLYSERS",
    {},
    _root,
    {},
    "_ext_constant_cf_exogenous_flexible_electrolysers",
)


@component.add(
    name="CF_flexible_electrolysers",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_proflex_cf_endogenous": 1,
        "cf_electrolysers_ceep": 1,
        "cf_exogenous_flexible_electrolysers": 1,
    },
)
def cf_flexible_electrolysers():
    return if_then_else(
        switch_proflex_cf_endogenous() == 1,
        lambda: cf_electrolysers_ceep(),
        lambda: xr.DataArray(
            cf_exogenous_flexible_electrolysers(),
            {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
            ["REGIONS_9_I"],
        ),
    )


@component.add(
    name="CF_STATIONARY_ELECTROLYZERS",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_cf_stationary_electrolyzers"},
)
def cf_stationary_electrolyzers():
    return _ext_constant_cf_stationary_electrolyzers()


_ext_constant_cf_stationary_electrolyzers = ExtConstant(
    "model_parameters/energy/energy-hydrogen.xlsx",
    "hydrogen_supply",
    "CF_STATIONARY_ELECTROLYZERS",
    {},
    _root,
    {},
    "_ext_constant_cf_stationary_electrolyzers",
)


@component.add(
    name="CORRESPONDENCE_MATRIX_TO_INPUT_OUTPUT_PROSUP_H2_PER_COMMODITY",
    units="DMNL",
    subscripts=["PROSUP_H2_I", "NRG_TO_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_correspondence_matrix_to_input_output_prosup_h2_per_commodity"
    },
)
def correspondence_matrix_to_input_output_prosup_h2_per_commodity():
    """
    Correspondence matrix (0s, 1s and -1s) relating TO inputs and outputs for each PROSUP. Note: negative values for output values fo the process (because the it reduces the amount of TO that needs to be coveres by other processes), positive values for process-inputs (mostly electricity - because it increases the amount of electricity needed to run these flexibility processes).
    """
    return _ext_constant_correspondence_matrix_to_input_output_prosup_h2_per_commodity()


_ext_constant_correspondence_matrix_to_input_output_prosup_h2_per_commodity = (
    ExtConstant(
        "model_parameters/energy/energy.xlsm",
        "Common",
        "CORRESPONDENCE_MATRIX_TO_INPUT_OUTPUT_PROSUP_H2_PER_COMMODITY",
        {
            "PROSUP_H2_I": _subscript_dict["PROSUP_H2_I"],
            "NRG_TO_I": _subscript_dict["NRG_TO_I"],
        },
        _root,
        {
            "PROSUP_H2_I": _subscript_dict["PROSUP_H2_I"],
            "NRG_TO_I": _subscript_dict["NRG_TO_I"],
        },
        "_ext_constant_correspondence_matrix_to_input_output_prosup_h2_per_commodity",
    )
)


@component.add(
    name="EFFICIENCY_GAS_STORAGE",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_efficiency_gas_storage"},
)
def efficiency_gas_storage():
    """
    This parameter represents the efficiency associated with the methane storage process; compression of methane for storage and losses due to self-discharge and standby (mainly caused by leaks).
    """
    return _ext_constant_efficiency_gas_storage()


_ext_constant_efficiency_gas_storage = ExtConstant(
    "model_parameters/energy/energy-storage.xlsx",
    "Dedicated_capacities",
    "EFFICIENCY_GAS_STORAGE",
    {},
    _root,
    {},
    "_ext_constant_efficiency_gas_storage",
)


@component.add(
    name="EFFICIENCY_METHANIZATION",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_efficiency_methanization"},
)
def efficiency_methanization():
    """
    Methane production, i.e. production of synthetic methane, takes place through the hydrogenation of carbon dioxide (Sabatier process), according to the following formula: CO_2+4H_2?CH_4+2H_2_O This parameter represents the amont of hydrogen energy required to produce synthetic methane (MJ methane produced per MJ hydrogen, in LHV basis).
    """
    return _ext_constant_efficiency_methanization()


_ext_constant_efficiency_methanization = ExtConstant(
    "model_parameters/energy/energy-hydrogen.xlsx",
    "hydrogen_supply",
    "EFFICIENCY_METHANIZATION",
    {},
    _root,
    {},
    "_ext_constant_efficiency_methanization",
)


@component.add(
    name="EFFICIENCY_METHANOL_SYNTHESIS",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_efficiency_methanol_synthesis"},
)
def efficiency_methanol_synthesis():
    """
    This parameter represents the hydrogen energy required to produce methanol (MJ methanol produced per MJ hydrogen, in LHV basis).
    """
    return _ext_constant_efficiency_methanol_synthesis()


_ext_constant_efficiency_methanol_synthesis = ExtConstant(
    "model_parameters/energy/energy-hydrogen.xlsx",
    "hydrogen_supply",
    "EFFICIENCY_METHANOL_SYNTHESIS",
    {},
    _root,
    {},
    "_ext_constant_efficiency_methanol_synthesis",
)


@component.add(
    name="EFFICIENCY_STATIONARY_ELECTROLYZER",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_efficiency_stationary_electrolyzer"},
)
def efficiency_stationary_electrolyzer():
    """
    This variable gives an account of the efficiency of converting electrical energy into hydrogen for an electrolyzer (LHV basis), considering the auxiliary elements (pumps, heat exchangers, etc.) i.e. the efficiency of the system. Commercially available electrolyzer technologies include the alkaline electrolyzer (AEL) (mature technology) and the polymer exchange electrolyzer (PEM) (developing technology) and allow the production of hydrogen with a purity very close to 100 %.
    """
    return _ext_constant_efficiency_stationary_electrolyzer()


_ext_constant_efficiency_stationary_electrolyzer = ExtConstant(
    "model_parameters/energy/energy-hydrogen.xlsx",
    "hydrogen_supply",
    "EFFICIENCY_ELECTROLYZER",
    {},
    _root,
    {},
    "_ext_constant_efficiency_stationary_electrolyzer",
)


@component.add(
    name="flexible_electrolysers_capacity_decommissioning",
    units="TW/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "flexible_electrolysers_capacity_stock": 1,
        "lifetime_electrolyzers": 1,
    },
)
def flexible_electrolysers_capacity_decommissioning():
    """
    Decommission of flexible electrolysers
    """
    return flexible_electrolysers_capacity_stock() / lifetime_electrolyzers()


@component.add(
    name="flexible_electrolysers_capacity_expansion",
    units="TW/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_nrg_proflex_capacity_expansion_endogenous": 1,
        "flexible_electrolysers_capacity_decommissioning": 1,
        "prosup_flexopt_elec_capacity_expansion": 1,
        "one_year": 1,
        "objective_flexible_electrolizers_expansion_sp": 1,
        "year_final_flexible_electrolizers_expansion_sp_0": 2,
        "time": 1,
        "switch_policy_flexible_electrolyzers_expansion_sp_0": 1,
        "initial_year_flexible_electrolizers_expansion_sp_0": 2,
    },
)
def flexible_electrolysers_capacity_expansion():
    """
    New capacity of flexible electrolysers
    """
    return if_then_else(
        switch_nrg_proflex_capacity_expansion_endogenous() == 1,
        lambda: prosup_flexopt_elec_capacity_expansion()
        .loc[:, "PROSUP_elec_2_hydrogen"]
        .reset_coords(drop=True)
        + flexible_electrolysers_capacity_decommissioning(),
        lambda: if_then_else(
            switch_policy_flexible_electrolyzers_expansion_sp_0() == 1,
            lambda: ramp(
                __data["time"],
                objective_flexible_electrolizers_expansion_sp()
                / (
                    year_final_flexible_electrolizers_expansion_sp_0()
                    - initial_year_flexible_electrolizers_expansion_sp_0()
                ),
                initial_year_flexible_electrolizers_expansion_sp_0(),
                year_final_flexible_electrolizers_expansion_sp_0(),
            )
            / one_year(),
            lambda: xr.DataArray(
                0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
            ),
        ),
    )


@component.add(
    name="flexible_electrolysers_capacity_stock",
    units="TW",
    subscripts=["REGIONS_9_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_flexible_electrolysers_capacity_stock": 1},
    other_deps={
        "_integ_flexible_electrolysers_capacity_stock": {
            "initial": {},
            "step": {
                "flexible_electrolysers_capacity_expansion": 1,
                "flexible_electrolysers_capacity_decommissioning": 1,
            },
        }
    },
)
def flexible_electrolysers_capacity_stock():
    """
    Capacity of flexible electrolysers installed in the region
    """
    return _integ_flexible_electrolysers_capacity_stock()


_integ_flexible_electrolysers_capacity_stock = Integ(
    lambda: flexible_electrolysers_capacity_expansion()
    - flexible_electrolysers_capacity_decommissioning(),
    lambda: xr.DataArray(
        0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
    ),
    "_integ_flexible_electrolysers_capacity_stock",
)


@component.add(
    name="H2_maximum_production_via_stationary_electrolyzer",
    units="EJ/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "stationary_electrolyzer_capacity_stock": 1,
        "cf_stationary_electrolyzers": 1,
        "efficiency_stationary_electrolyzer": 1,
        "unit_conversion_hours_year": 1,
        "unit_conversion_tw_per_ej_per_year": 1,
    },
)
def h2_maximum_production_via_stationary_electrolyzer():
    """
    Maximum amount of hydrogen that can be produced with stationary electrolyzers
    """
    return (
        stationary_electrolyzer_capacity_stock()
        * cf_stationary_electrolyzers()
        * efficiency_stationary_electrolyzer()
        * unit_conversion_hours_year()
        * unit_conversion_tw_per_ej_per_year()
    )


@component.add(
    name="H2_production_from_flexible_electrolysers",
    units="EJ/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "flexible_electrolysers_capacity_stock": 1,
        "cf_flexible_electrolysers": 1,
        "unit_conversion_hours_year": 1,
        "efficiency_stationary_electrolyzer": 1,
        "unit_conversion_w_tw": 1,
        "unit_conversion_j_wh": 1,
        "unit_conversion_j_ej": 1,
    },
)
def h2_production_from_flexible_electrolysers():
    return (
        flexible_electrolysers_capacity_stock()
        * cf_flexible_electrolysers()
        * unit_conversion_hours_year()
        * efficiency_stationary_electrolyzer()
        * unit_conversion_w_tw()
        * unit_conversion_j_wh()
        / unit_conversion_j_ej()
    )


@component.add(
    name="H2_production_from_stationary_electrolyzers_by_PROSUP_H2",
    units="EJ/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "stationary_electrolyzer_capacity_stock": 1,
        "cf_stationary_electrolyzers": 1,
        "unit_conversion_hours_year": 1,
        "efficiency_stationary_electrolyzer": 1,
        "unit_conversion_w_tw": 1,
        "unit_conversion_j_wh": 1,
        "unit_conversion_j_ej": 1,
    },
)
def h2_production_from_stationary_electrolyzers_by_prosup_h2():
    """
    Hydrogen produced by electrolysers ([PROSUP elec 2 hydrogen]).
    """
    return (
        stationary_electrolyzer_capacity_stock()
        * cf_stationary_electrolyzers()
        * unit_conversion_hours_year()
        * efficiency_stationary_electrolyzer()
        * unit_conversion_w_tw()
        * unit_conversion_j_wh()
        / unit_conversion_j_ej()
    )


@component.add(
    name="hydrogen_required_to_satisfy_H2_demand",
    units="EJ/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "total_fe_including_net_trade": 3,
        "switch_hydrogen_industrial_demand": 1,
        "share_fe_liquid_substituted_by_h2_synthetic_liquid": 1,
        "efficiency_methanol_synthesis": 1,
        "efficiency_methanization": 1,
        "share_fe_gas_substituted_by_h2_synthetic_gas": 1,
        "h2_production_from_flexible_electrolysers": 1,
        "h2_production_from_stationary_electrolyzers_by_prosup_h2": 1,
    },
)
def hydrogen_required_to_satisfy_h2_demand():
    """
    Quantity of hydrogen demanded that is not supplied via stationary electrolysis. Note that hydrogen produced from "flexible_electrolysers_capacity_stock" is deducted from the required amount for satisfaction of TO demand.
    """
    return (
        total_fe_including_net_trade().loc[:, "FE_hydrogen"].reset_coords(drop=True)
        * switch_hydrogen_industrial_demand()
        + share_fe_liquid_substituted_by_h2_synthetic_liquid()
        * total_fe_including_net_trade().loc[:, "FE_liquid"].reset_coords(drop=True)
        / efficiency_methanol_synthesis()
        + share_fe_gas_substituted_by_h2_synthetic_gas()
        * total_fe_including_net_trade().loc[:, "FE_gas"].reset_coords(drop=True)
        / efficiency_methanization()
        - h2_production_from_flexible_electrolysers()
        - h2_production_from_stationary_electrolyzers_by_prosup_h2()
    )


@component.add(
    name="INITIAL_STATIONARY_ELECTROLYZER_CAPACITY_STOCK",
    units="TW",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_initial_stationary_electrolyzer_capacity_stock"
    },
)
def initial_stationary_electrolyzer_capacity_stock():
    """
    Capacity stock in the initial year of the simulation.
    """
    return _ext_constant_initial_stationary_electrolyzer_capacity_stock()


_ext_constant_initial_stationary_electrolyzer_capacity_stock = ExtConstant(
    "model_parameters/energy/energy-hydrogen.xlsx",
    "hydrogen_supply",
    "INITIAL_ELECTROLYZER_CAPACITY_STOCK*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_initial_stationary_electrolyzer_capacity_stock",
)


@component.add(
    name="INITIAL_YEAR_FLEXIBLE_ELECTROLIZERS_EXPANSION_SP_0",
    units="Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_initial_year_flexible_electrolizers_expansion_sp_0"
    },
)
def initial_year_flexible_electrolizers_expansion_sp_0():
    """
    Initial year of the policy scenario for flexible electrolyzers.
    """
    return _ext_constant_initial_year_flexible_electrolizers_expansion_sp_0()


_ext_constant_initial_year_flexible_electrolizers_expansion_sp_0 = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "INITIAL_YEAR_FLEXIBLE_ELECTROLIZERS_EXPANSION_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_initial_year_flexible_electrolizers_expansion_sp_0",
)


@component.add(
    name="INITIAL_YEAR_SHARE_FE_LIQUID_AND_GAS_SUBSTITUTED_BY_H2_SYNFUELS_SP",
    units="Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_initial_year_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp"
    },
)
def initial_year_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp():
    """
    Year from which the policies to replace liquids and gases with H2-based synthetic fuels begin
    """
    return (
        _ext_constant_initial_year_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp()
    )


_ext_constant_initial_year_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "INITIAL_YEAR_PERCENTAGE_FE_LIQUID_AND_GAS_SUBSTITUTED_BY_H2_LIQUIDS_AND_GASES_BASED_FUEL_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_initial_year_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp",
)


@component.add(
    name="LIFETIME_ELECTROLYZERS",
    units="Years",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_lifetime_electrolyzers"},
)
def lifetime_electrolyzers():
    """
    Lifetime of electrolyzers.
    """
    return _ext_constant_lifetime_electrolyzers()


_ext_constant_lifetime_electrolyzers = ExtConstant(
    "model_parameters/energy/energy-hydrogen.xlsx",
    "hydrogen_supply",
    "LIFETIME_ELECTROLYZERS",
    {},
    _root,
    {},
    "_ext_constant_lifetime_electrolyzers",
)


@component.add(
    name="maximum_installed_capacity_electrolysers",
    units="TW/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "h2_total_demand_lhv_basis": 1,
        "unit_conversion_tj_ej": 1,
        "unit_conversion_hours_year": 1,
        "unit_conversion_tw_per_ej_per_year": 1,
        "time_step": 1,
        "factor_backup_power_system": 1,
    },
)
def maximum_installed_capacity_electrolysers():
    """
    Assumption: 100% of the hydrogen demand may be electrified.
    """
    return (
        h2_total_demand_lhv_basis()
        / unit_conversion_tj_ej()
        / unit_conversion_hours_year()
        / unit_conversion_tw_per_ej_per_year()
        / time_step()
        * factor_backup_power_system()
    )


@component.add(
    name="OBJECTIVE_FLEXIBLE_ELECTROLIZERS_EXPANSION_SP",
    units="TW",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_objective_flexible_electrolizers_expansion_sp"
    },
)
def objective_flexible_electrolizers_expansion_sp():
    """
    Final installed capacity of the policy scenario for flexible electrolyzers.
    """
    return _ext_constant_objective_flexible_electrolizers_expansion_sp()


_ext_constant_objective_flexible_electrolizers_expansion_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "OBJECTIVE_FLEXIBLE_ELECTROLIZERS_EXPANSION_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_objective_flexible_electrolizers_expansion_sp",
)


@component.add(
    name="OBJECTIVE_SHARE_FE_GAS_SUBSTITUTED_BY_H2_SYNTHETIC_GAS_SP",
    units="DMML",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_objective_share_fe_gas_substituted_by_h2_synthetic_gas_sp"
    },
)
def objective_share_fe_gas_substituted_by_h2_synthetic_gas_sp():
    """
    Share of FE gas demand substituted by H2 synthetic gas
    """
    return _ext_constant_objective_share_fe_gas_substituted_by_h2_synthetic_gas_sp()


_ext_constant_objective_share_fe_gas_substituted_by_h2_synthetic_gas_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "OBJECTIVE_PERCENTAGE_FE_GAS_SUBSTITUTED_BY_H2_GASES_BASED_FUEL_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_objective_share_fe_gas_substituted_by_h2_synthetic_gas_sp",
)


@component.add(
    name="OBJECTIVE_SHARE_FE_LIQUID_SUBSTITUTED_BY_H2_SYNTHETIC_LIQUID_SP",
    units="DMML",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_objective_share_fe_liquid_substituted_by_h2_synthetic_liquid_sp"
    },
)
def objective_share_fe_liquid_substituted_by_h2_synthetic_liquid_sp():
    return (
        _ext_constant_objective_share_fe_liquid_substituted_by_h2_synthetic_liquid_sp()
    )


_ext_constant_objective_share_fe_liquid_substituted_by_h2_synthetic_liquid_sp = (
    ExtConstant(
        "scenario_parameters/scenario_parameters.xlsx",
        "energy",
        "OBJECTIVE_PERCENTAGE_FE_LIQUID_SUBSTITUTED_BY_H2_LIQUIDS_BASED_FUEL_SP*",
        {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
        _root,
        {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
        "_ext_constant_objective_share_fe_liquid_substituted_by_h2_synthetic_liquid_sp",
    )
)


@component.add(
    name="share_FE_gas_substituted_by_H2_synthetic_gas",
    units="DMML",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_policy_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp": 1,
        "time": 3,
        "objective_share_fe_gas_substituted_by_h2_synthetic_gas_sp": 3,
        "initial_year_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp": 4,
        "year_final_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp": 3,
    },
)
def share_fe_gas_substituted_by_h2_synthetic_gas():
    return if_then_else(
        switch_policy_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp() == 0,
        lambda: xr.DataArray(
            0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
        ),
        lambda: if_then_else(
            time()
            < initial_year_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp(),
            lambda: xr.DataArray(
                0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
            ),
            lambda: if_then_else(
                time()
                > year_final_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp(),
                lambda: objective_share_fe_gas_substituted_by_h2_synthetic_gas_sp(),
                lambda: -objective_share_fe_gas_substituted_by_h2_synthetic_gas_sp()
                * initial_year_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp()
                / (
                    year_final_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp()
                    - initial_year_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp()
                )
                + time()
                * zidz(
                    objective_share_fe_gas_substituted_by_h2_synthetic_gas_sp(),
                    year_final_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp()
                    - initial_year_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp(),
                ),
            ),
        ),
    )


@component.add(
    name="share_FE_liquid_substituted_by_H2_synthetic_liquid",
    units="DMML",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_model_explorer": 1,
        "model_explorer_percentage_fe_liquid_substituted_by_h2_synthetic_liquid": 1,
        "year_final_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp": 3,
        "switch_policy_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp": 1,
        "objective_share_fe_liquid_substituted_by_h2_synthetic_liquid_sp": 3,
        "initial_year_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp": 4,
        "time": 3,
    },
)
def share_fe_liquid_substituted_by_h2_synthetic_liquid():
    """
    Share of FE liquid demand substituted by H2 synthetic liquids
    """
    return if_then_else(
        switch_model_explorer() == 1,
        lambda: model_explorer_percentage_fe_liquid_substituted_by_h2_synthetic_liquid(),
        lambda: if_then_else(
            switch_policy_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp() == 0,
            lambda: xr.DataArray(
                0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
            ),
            lambda: if_then_else(
                time()
                < initial_year_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp(),
                lambda: xr.DataArray(
                    0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
                ),
                lambda: if_then_else(
                    time()
                    > year_final_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp(),
                    lambda: objective_share_fe_liquid_substituted_by_h2_synthetic_liquid_sp(),
                    lambda: -objective_share_fe_liquid_substituted_by_h2_synthetic_liquid_sp()
                    * initial_year_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp()
                    / (
                        year_final_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp()
                        - initial_year_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp()
                    )
                    + time()
                    * zidz(
                        objective_share_fe_liquid_substituted_by_h2_synthetic_liquid_sp(),
                        year_final_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp()
                        - initial_year_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp(),
                    ),
                ),
            ),
        ),
    )


@component.add(
    name="share_hydrogen_commodity_by_process",
    units="DMNL",
    subscripts=["REGIONS_9_I", "PROSUP_H2_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "total_fe_including_net_trade": 12,
        "share_fe_liquid_substituted_by_h2_synthetic_liquid": 4,
        "efficiency_methanization": 4,
        "share_fe_gas_substituted_by_h2_synthetic_gas": 4,
        "efficiency_methanol_synthesis": 4,
    },
)
def share_hydrogen_commodity_by_process():
    """
    Share of pure hydrogen (commodity) to different processes.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "PROSUP_H2_I": _subscript_dict["PROSUP_H2_I"],
        },
        ["REGIONS_9_I", "PROSUP_H2_I"],
    )
    value.loc[:, ["PROSUP_elec_2_hydrogen"]] = (
        zidz(
            total_fe_including_net_trade()
            .loc[:, "FE_hydrogen"]
            .reset_coords(drop=True),
            total_fe_including_net_trade().loc[:, "FE_hydrogen"].reset_coords(drop=True)
            + share_fe_liquid_substituted_by_h2_synthetic_liquid()
            * total_fe_including_net_trade().loc[:, "FE_liquid"].reset_coords(drop=True)
            / efficiency_methanol_synthesis()
            + share_fe_gas_substituted_by_h2_synthetic_gas()
            * total_fe_including_net_trade().loc[:, "FE_gas"].reset_coords(drop=True)
            / efficiency_methanization(),
        )
        .expand_dims({"NRG_PRO_I": ["PROSUP_elec_2_hydrogen"]}, 1)
        .values
    )
    value.loc[:, ["PROSUP_hydrogen_2_liquid"]] = (
        zidz(
            share_fe_liquid_substituted_by_h2_synthetic_liquid()
            * total_fe_including_net_trade().loc[:, "FE_liquid"].reset_coords(drop=True)
            / efficiency_methanol_synthesis(),
            total_fe_including_net_trade().loc[:, "FE_hydrogen"].reset_coords(drop=True)
            + share_fe_liquid_substituted_by_h2_synthetic_liquid()
            * total_fe_including_net_trade().loc[:, "FE_liquid"].reset_coords(drop=True)
            / efficiency_methanol_synthesis()
            + share_fe_gas_substituted_by_h2_synthetic_gas()
            * total_fe_including_net_trade().loc[:, "FE_gas"].reset_coords(drop=True)
            / efficiency_methanization(),
        )
        .expand_dims({"NRG_PRO_I": ["PROSUP_hydrogen_2_liquid"]}, 1)
        .values
    )
    value.loc[:, ["PROSUP_hydrogen_2_gas"]] = (
        zidz(
            share_fe_gas_substituted_by_h2_synthetic_gas()
            * total_fe_including_net_trade().loc[:, "FE_gas"].reset_coords(drop=True)
            / efficiency_methanization(),
            total_fe_including_net_trade().loc[:, "FE_hydrogen"].reset_coords(drop=True)
            + share_fe_liquid_substituted_by_h2_synthetic_liquid()
            * total_fe_including_net_trade().loc[:, "FE_liquid"].reset_coords(drop=True)
            / efficiency_methanol_synthesis()
            + share_fe_gas_substituted_by_h2_synthetic_gas()
            * total_fe_including_net_trade().loc[:, "FE_gas"].reset_coords(drop=True)
            / efficiency_methanization(),
        )
        .expand_dims({"NRG_PRO_I": ["PROSUP_hydrogen_2_gas"]}, 1)
        .values
    )
    return value


@component.add(
    name="stationary_electrolyzer_capacity_stock",
    units="TW",
    subscripts=["REGIONS_9_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_stationary_electrolyzer_capacity_stock": 1},
    other_deps={
        "_integ_stationary_electrolyzer_capacity_stock": {
            "initial": {"initial_stationary_electrolyzer_capacity_stock": 1},
            "step": {
                "stationary_electrolyzers_capacity_expansion": 1,
                "stationary_electrolyzers_capacity_decommissioning": 1,
            },
        }
    },
)
def stationary_electrolyzer_capacity_stock():
    """
    Operational capacity stock of electrolyzers.
    """
    return _integ_stationary_electrolyzer_capacity_stock()


_integ_stationary_electrolyzer_capacity_stock = Integ(
    lambda: stationary_electrolyzers_capacity_expansion()
    - stationary_electrolyzers_capacity_decommissioning(),
    lambda: initial_stationary_electrolyzer_capacity_stock(),
    "_integ_stationary_electrolyzer_capacity_stock",
)


@component.add(
    name="stationary_electrolyzers_capacity_decommissioning",
    units="TW/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "stationary_electrolyzer_capacity_stock": 1,
        "lifetime_electrolyzers": 1,
    },
)
def stationary_electrolyzers_capacity_decommissioning():
    """
    Decommissioning of electrolyzers capacity stock due to reaching the end of their lifetime.
    """
    return stationary_electrolyzer_capacity_stock() / lifetime_electrolyzers()


@component.add(
    name="stationary_electrolyzers_capacity_expansion",
    units="TW/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_availability_unmature_energy_technologies_sp": 2,
        "stationary_electrolyzers_capacity_expansion_required": 1,
    },
)
def stationary_electrolyzers_capacity_expansion():
    """
    New installed capacities of electrolyzers.
    """
    return if_then_else(
        np.logical_or(
            select_availability_unmature_energy_technologies_sp() == 1,
            select_availability_unmature_energy_technologies_sp() == 2,
        ),
        lambda: stationary_electrolyzers_capacity_expansion_required(),
        lambda: xr.DataArray(
            0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
        ),
    )


@component.add(
    name="stationary_electrolyzers_capacity_expansion_required",
    units="TW/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "hydrogen_required_to_satisfy_h2_demand": 1,
        "cf_stationary_electrolyzers": 1,
        "efficiency_stationary_electrolyzer": 1,
        "unit_conversion_hours_year": 1,
        "unit_conversion_tw_per_ej_per_year": 1,
        "one_year": 1,
    },
)
def stationary_electrolyzers_capacity_expansion_required():
    """
    Electrolyzers capacity expansion required annualy which would make it possible to cover the demand for hydrogen with stationary eletctrolyzers
    """
    return (
        hydrogen_required_to_satisfy_h2_demand()
        / cf_stationary_electrolyzers()
        / efficiency_stationary_electrolyzer()
        / unit_conversion_hours_year()
        / unit_conversion_tw_per_ej_per_year()
        / one_year()
    )


@component.add(
    name="SWITCH_NRG_PROFLEX_CAPACITY_EXPANSION_ENDOGENOUS",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_switch_nrg_proflex_capacity_expansion_endogenous"
    },
)
def switch_nrg_proflex_capacity_expansion_endogenous():
    """
    0: exogenous capacity expansion of PROFLEX based on scenario parameters inputs 1: endogenous capacity expansion of PROFLEX driven by the allocation of curtailement
    """
    return _ext_constant_switch_nrg_proflex_capacity_expansion_endogenous()


_ext_constant_switch_nrg_proflex_capacity_expansion_endogenous = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_NRG_PROFLEX_CAPACITY_EXPANSION_ENDOGENOUS",
    {},
    _root,
    {},
    "_ext_constant_switch_nrg_proflex_capacity_expansion_endogenous",
)


@component.add(
    name="SWITCH_POLICY_FLEXIBLE_ELECTROLYZERS_EXPANSION_SP_0",
    units="Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_switch_policy_flexible_electrolyzers_expansion_sp_0"
    },
)
def switch_policy_flexible_electrolyzers_expansion_sp_0():
    """
    Switch to activate and deactivate policy by country.
    """
    return _ext_constant_switch_policy_flexible_electrolyzers_expansion_sp_0()


_ext_constant_switch_policy_flexible_electrolyzers_expansion_sp_0 = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "SWITCH_POLICY_FLEXIBLE_ELECTROLYZERS_EXPANSION_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_switch_policy_flexible_electrolyzers_expansion_sp_0",
)


@component.add(
    name="SWITCH_POLICY_SHARE_FE_LIQUID_AND_GAS_SUBSTITUTED_BY_H2_SYNFUELS_SP",
    units="DMML",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_switch_policy_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp"
    },
)
def switch_policy_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp():
    """
    Switch to activate and deactivate policy by country.
    """
    return (
        _ext_constant_switch_policy_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp()
    )


_ext_constant_switch_policy_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "SWITCH_POLICY_PERCENTAGE_FE_LIQUID_AND_GAS_SUBSTITUTED_BY_H2_LIQUIDS_AND_GASES_BASED_FUEL_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_switch_policy_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp",
)


@component.add(
    name="TO_commodities_H2",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_TO_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "to_elec_consumption_stationary_electrolyzers_by_prosup_h2": 1,
        "to_h2_gases_based_fuel": 1,
        "to_pure_hydrogen": 1,
        "to_h2_liquids_based_fuel": 1,
    },
)
def to_commodities_h2():
    """
    Adjustment for the energy balance in the energy transformation chain. Positive to increment the commodidty and negative to substract what is already produced.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "NRG_TO_I": _subscript_dict["NRG_TO_I"],
        },
        ["REGIONS_9_I", "NRG_TO_I"],
    )
    value.loc[:, ["TO_elec"]] = (
        to_elec_consumption_stationary_electrolyzers_by_prosup_h2()
        .expand_dims({"NRG_COMMODITIES_I": ["TO_elec"]}, 1)
        .values
    )
    value.loc[:, ["TO_gas"]] = (
        (-to_h2_gases_based_fuel())
        .expand_dims({"NRG_COMMODITIES_I": ["TO_gas"]}, 1)
        .values
    )
    value.loc[:, ["TO_heat"]] = 0
    value.loc[:, ["TO_hydrogen"]] = (
        (-to_pure_hydrogen())
        .expand_dims({"NRG_COMMODITIES_I": ["TO_hydrogen"]}, 1)
        .values
    )
    value.loc[:, ["TO_liquid"]] = (
        (-to_h2_liquids_based_fuel())
        .expand_dims({"NRG_COMMODITIES_I": ["TO_liquid"]}, 1)
        .values
    )
    value.loc[:, ["TO_solid_bio"]] = 0
    value.loc[:, ["TO_solid_fossil"]] = 0
    return value


@component.add(
    name="TO_elec_consumption_stationary_electrolyzers_by_PROSUP_H2",
    units="EJ/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "stationary_electrolyzer_capacity_stock": 1,
        "cf_stationary_electrolyzers": 1,
        "unit_conversion_hours_year": 1,
        "unit_conversion_w_tw": 1,
        "unit_conversion_j_wh": 1,
        "unit_conversion_j_ej": 1,
    },
)
def to_elec_consumption_stationary_electrolyzers_by_prosup_h2():
    """
    Consumption of electricity by electrolyzers to produce H2 and H2-derived fuels ([PROSUP_elec_2_hydrogen]).
    """
    return (
        stationary_electrolyzer_capacity_stock()
        * cf_stationary_electrolyzers()
        * unit_conversion_hours_year()
        * unit_conversion_w_tw()
        * unit_conversion_j_wh()
        / unit_conversion_j_ej()
    )


@component.add(
    name="TO_H2_gases_based_fuel",
    units="EJ/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "allocation_pure_hydrogen_by_process": 1,
        "efficiency_methanization": 1,
    },
)
def to_h2_gases_based_fuel():
    """
    Gas produced in methanization plants (commodity based on hydrogen)
    """
    return (
        allocation_pure_hydrogen_by_process()
        .loc[:, "PROSUP_hydrogen_2_gas"]
        .reset_coords(drop=True)
        * efficiency_methanization()
    )


@component.add(
    name="To_H2_liquids_based_fuel",
    units="EJ/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "allocation_pure_hydrogen_by_process": 1,
        "efficiency_methanol_synthesis": 1,
    },
)
def to_h2_liquids_based_fuel():
    """
    Liquid produced in methanol synthesis process (commodity based on hydrogen)
    """
    return (
        allocation_pure_hydrogen_by_process()
        .loc[:, "PROSUP_hydrogen_2_liquid"]
        .reset_coords(drop=True)
        * efficiency_methanol_synthesis()
    )


@component.add(
    name="TO_PROSUP_H2_per_commodity",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "PROSUP_H2_I", "NRG_TO_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "to_elec_consumption_stationary_electrolyzers_by_prosup_h2": 1,
        "correspondence_matrix_to_input_output_prosup_h2_per_commodity": 4,
        "h2_production_from_stationary_electrolyzers_by_prosup_h2": 1,
    },
)
def to_prosup_h2_per_commodity():
    """
    Note: negative values for output values fo the process (because the it reduces the amount of TO that needs to be coveres by other processes), positive values for process-inputs (mostly electricity - because it increases the amount of electricity needed to run these flexibility processes).
    """
    return to_elec_consumption_stationary_electrolyzers_by_prosup_h2() * if_then_else(
        correspondence_matrix_to_input_output_prosup_h2_per_commodity() > 0,
        lambda: correspondence_matrix_to_input_output_prosup_h2_per_commodity(),
        lambda: xr.DataArray(
            0,
            {
                "PROSUP_H2_I": _subscript_dict["PROSUP_H2_I"],
                "NRG_TO_I": _subscript_dict["NRG_TO_I"],
            },
            ["PROSUP_H2_I", "NRG_TO_I"],
        ),
    ) + h2_production_from_stationary_electrolyzers_by_prosup_h2() * if_then_else(
        correspondence_matrix_to_input_output_prosup_h2_per_commodity() > 0,
        lambda: xr.DataArray(
            0,
            {
                "PROSUP_H2_I": _subscript_dict["PROSUP_H2_I"],
                "NRG_TO_I": _subscript_dict["NRG_TO_I"],
            },
            ["PROSUP_H2_I", "NRG_TO_I"],
        ),
        lambda: correspondence_matrix_to_input_output_prosup_h2_per_commodity(),
    )


@component.add(
    name="TO_pure_hydrogen",
    units="EJ/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"allocation_pure_hydrogen_by_process": 1},
)
def to_pure_hydrogen():
    """
    Pure hydrogen usage in the economy. Actually, PROSUP_elec_2_hydrogen should be here substituted by other processes using pure hydrogen.
    """
    return (
        allocation_pure_hydrogen_by_process()
        .loc[:, "PROSUP_elec_2_hydrogen"]
        .reset_coords(drop=True)
    )


@component.add(
    name="YEAR_FINAL_FLEXIBLE_ELECTROLIZERS_EXPANSION_SP_0",
    units="Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_year_final_flexible_electrolizers_expansion_sp_0"
    },
)
def year_final_flexible_electrolizers_expansion_sp_0():
    """
    Final year of the policy scenario for flexible electrolyzers.
    """
    return _ext_constant_year_final_flexible_electrolizers_expansion_sp_0()


_ext_constant_year_final_flexible_electrolizers_expansion_sp_0 = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "YEAR_FINAL_FLEXIBLE_ELECTROLIZERS_EXPANSION_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_year_final_flexible_electrolizers_expansion_sp_0",
)


@component.add(
    name="YEAR_FINAL_SHARE_FE_LIQUID_AND_GAS_SUBSTITUTED_BY_H2_SYNFUELS_SP",
    units="Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_year_final_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp"
    },
)
def year_final_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp():
    """
    Target year of policies to replace liquids and gases with H2-based synthetic fuels
    """
    return (
        _ext_constant_year_final_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp()
    )


_ext_constant_year_final_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "YEAR_FINAL_PERCENTAGE_FE_LIQUID_AND_GAS_SUBSTITUTED_BY_H2_LIQUIDS_AND_GASES_BASED_FUEL_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_year_final_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp",
)
