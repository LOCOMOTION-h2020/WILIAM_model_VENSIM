"""
Module energy.capacities.investment_cost
Translated using PySD version 3.10.0
"""


@component.add(
    name="CAPACITY_INVESTMENT_COST_PRO_FLEXOPT_HIGH_DEVELOPMENT",
    units="Mdollars_2015/MW",
    subscripts=["PRO_FLEXOPT_I"],
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_capacity_investment_cost_pro_flexopt_high_development",
        "__data__": "_ext_data_capacity_investment_cost_pro_flexopt_high_development",
        "time": 1,
    },
)
def capacity_investment_cost_pro_flexopt_high_development():
    """
    Assumption of higher development (lower costs) future capacity costs for PRO FLEXOPT with relation to the medium-reference scenario.
    """
    return _ext_data_capacity_investment_cost_pro_flexopt_high_development(time())


_ext_data_capacity_investment_cost_pro_flexopt_high_development = ExtData(
    "model_parameters/energy/energy-capacity_investment_cost.xlsx",
    "PRO_FLEXOPT",
    "time_PRO_FLEXOPT",
    "CAPACITY_INVESTMENT_COST_PRO_FLEXOPT_HIGH",
    "interpolate",
    {"PRO_FLEXOPT_I": _subscript_dict["PRO_FLEXOPT_I"]},
    _root,
    {"PRO_FLEXOPT_I": _subscript_dict["PRO_FLEXOPT_I"]},
    "_ext_data_capacity_investment_cost_pro_flexopt_high_development",
)


@component.add(
    name="CAPACITY_INVESTMENT_COST_PRO_FLEXOPT_LOW_DEVELOPMENT",
    units="Mdollars_2015/MW",
    subscripts=["PRO_FLEXOPT_I"],
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_capacity_investment_cost_pro_flexopt_low_development",
        "__data__": "_ext_data_capacity_investment_cost_pro_flexopt_low_development",
        "time": 1,
    },
)
def capacity_investment_cost_pro_flexopt_low_development():
    """
    Assumption of lower development (higher costs) future capacity costs for PRO FLEXOPT with relation to the medium-reference scenario.
    """
    return _ext_data_capacity_investment_cost_pro_flexopt_low_development(time())


_ext_data_capacity_investment_cost_pro_flexopt_low_development = ExtData(
    "model_parameters/energy/energy-capacity_investment_cost.xlsx",
    "PRO_FLEXOPT",
    "time_PRO_FLEXOPT",
    "CAPACITY_INVESTMENT_COST_PRO_FLEXOPT_LOW",
    "interpolate",
    {"PRO_FLEXOPT_I": _subscript_dict["PRO_FLEXOPT_I"]},
    _root,
    {"PRO_FLEXOPT_I": _subscript_dict["PRO_FLEXOPT_I"]},
    "_ext_data_capacity_investment_cost_pro_flexopt_low_development",
)


@component.add(
    name="CAPACITY_INVESTMENT_COST_PRO_FLEXOPT_MEDIUM_DEVELOPMENT",
    units="Mdollars_2015/MW",
    subscripts=["PRO_FLEXOPT_I"],
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_capacity_investment_cost_pro_flexopt_medium_development",
        "__data__": "_ext_data_capacity_investment_cost_pro_flexopt_medium_development",
        "time": 1,
    },
)
def capacity_investment_cost_pro_flexopt_medium_development():
    """
    Assumption of medium future capacity costs for PRO FLEXOPT with relation to the medium-reference scenario.
    """
    return _ext_data_capacity_investment_cost_pro_flexopt_medium_development(time())


_ext_data_capacity_investment_cost_pro_flexopt_medium_development = ExtData(
    "model_parameters/energy/energy-capacity_investment_cost.xlsx",
    "PRO_FLEXOPT",
    "time_PRO_FLEXOPT",
    "CAPACITY_INVESTMENT_COST_PRO_FLEXOPT_MEDIUM",
    "interpolate",
    {"PRO_FLEXOPT_I": _subscript_dict["PRO_FLEXOPT_I"]},
    _root,
    {"PRO_FLEXOPT_I": _subscript_dict["PRO_FLEXOPT_I"]},
    "_ext_data_capacity_investment_cost_pro_flexopt_medium_development",
)


@component.add(
    name="CAPACITY_INVESTMENT_COST_PRO_FLEXOPT_USER_DEFINED_SP",
    units="Mdollars_2015/MW",
    subscripts=["PRO_FLEXOPT_I"],
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_capacity_investment_cost_pro_flexopt_user_defined_sp",
        "__data__": "_ext_data_capacity_investment_cost_pro_flexopt_user_defined_sp",
        "time": 1,
    },
)
def capacity_investment_cost_pro_flexopt_user_defined_sp():
    """
    Assumption from model user for future capacity costs for PROFLEX.
    """
    return _ext_data_capacity_investment_cost_pro_flexopt_user_defined_sp(time())


_ext_data_capacity_investment_cost_pro_flexopt_user_defined_sp = ExtData(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "time",
    "CAPACITY_INVESTMENT_COST_PRO_FLEXOPT_USER_DEFINED_SP",
    "interpolate",
    {"PRO_FLEXOPT_I": _subscript_dict["PRO_FLEXOPT_I"]},
    _root,
    {"PRO_FLEXOPT_I": _subscript_dict["PRO_FLEXOPT_I"]},
    "_ext_data_capacity_investment_cost_pro_flexopt_user_defined_sp",
)


@component.add(
    name="CAPACITY_INVESTMENT_COST_PROFLEX_DEVELOPMENT",
    units="Mdollars_2015/MW",
    subscripts=["PRO_FLEXOPT_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_capacity_investment_cost_development_sp": 4,
        "pro_flexopt_capacity_investment_cost_2015": 1,
        "capacity_investment_cost_pro_flexopt_medium_development": 1,
        "capacity_investment_cost_pro_flexopt_high_development": 1,
        "capacity_investment_cost_pro_flexopt_user_defined_sp": 1,
        "capacity_investment_cost_pro_flexopt_low_development": 1,
    },
)
def capacity_investment_cost_proflex_development():
    """
    Investment cost depending on assumption of their exogenous future evolution.
    """
    return if_then_else(
        select_capacity_investment_cost_development_sp() == 0,
        lambda: pro_flexopt_capacity_investment_cost_2015(),
        lambda: if_then_else(
            select_capacity_investment_cost_development_sp() == 1,
            lambda: capacity_investment_cost_pro_flexopt_low_development(),
            lambda: if_then_else(
                select_capacity_investment_cost_development_sp() == 2,
                lambda: capacity_investment_cost_pro_flexopt_medium_development(),
                lambda: if_then_else(
                    select_capacity_investment_cost_development_sp() == 3,
                    lambda: capacity_investment_cost_pro_flexopt_high_development(),
                    lambda: capacity_investment_cost_pro_flexopt_user_defined_sp(),
                ),
            ),
        ),
    )


@component.add(
    name="CAPACITY_INVESTMENT_COST_PROTRA_DEVELOPMENT",
    units="Mdollars_2015/MW",
    subscripts=["PROTRA_PP_CHP_HP_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_capacity_investment_cost_development_sp": 4,
        "protra_capacity_investment_cost_2015": 1,
        "capacity_investment_cost_protra_user_defined_sp": 1,
        "capacity_investment_cost_protra_high_development": 1,
        "capacity_investment_cost_protra_medium_development": 1,
        "capacity_investment_cost_protra_low_development": 1,
    },
)
def capacity_investment_cost_protra_development():
    """
    Investment cost depending on assumption of their exogenous future evolution.
    """
    return if_then_else(
        select_capacity_investment_cost_development_sp() == 0,
        lambda: protra_capacity_investment_cost_2015(),
        lambda: if_then_else(
            select_capacity_investment_cost_development_sp() == 1,
            lambda: capacity_investment_cost_protra_low_development(),
            lambda: if_then_else(
                select_capacity_investment_cost_development_sp() == 2,
                lambda: capacity_investment_cost_protra_medium_development(),
                lambda: if_then_else(
                    select_capacity_investment_cost_development_sp() == 3,
                    lambda: capacity_investment_cost_protra_high_development(),
                    lambda: capacity_investment_cost_protra_user_defined_sp(),
                ),
            ),
        ),
    )


@component.add(
    name="CAPACITY_INVESTMENT_COST_PROTRA_HIGH_DEVELOPMENT",
    units="Mdollars_2015/MW",
    subscripts=["PROTRA_PP_CHP_HP_I"],
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_capacity_investment_cost_protra_high_development",
        "__data__": "_ext_data_capacity_investment_cost_protra_high_development",
        "time": 1,
    },
)
def capacity_investment_cost_protra_high_development():
    """
    Assumption of higher development (reduced costs) future capacity costs for PROTRA with relation to the medium-reference scenario.
    """
    return _ext_data_capacity_investment_cost_protra_high_development(time())


_ext_data_capacity_investment_cost_protra_high_development = ExtData(
    "model_parameters/energy/energy-capacity_investment_cost.xlsx",
    "PROTRA",
    "time",
    "CAPACITY_INVESTMENT_COST_PROTRA_CHP_HP_PP_HIGH_DEVELOPMENT",
    "interpolate",
    {"PROTRA_PP_CHP_HP_I": _subscript_dict["PROTRA_PP_CHP_HP_I"]},
    _root,
    {"PROTRA_PP_CHP_HP_I": _subscript_dict["PROTRA_PP_CHP_HP_I"]},
    "_ext_data_capacity_investment_cost_protra_high_development",
)


@component.add(
    name="CAPACITY_INVESTMENT_COST_PROTRA_LOW_DEVELOPMENT",
    units="Mdollars_2015/MW",
    subscripts=["PROTRA_PP_CHP_HP_I"],
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_capacity_investment_cost_protra_low_development",
        "__data__": "_ext_data_capacity_investment_cost_protra_low_development",
        "time": 1,
    },
)
def capacity_investment_cost_protra_low_development():
    """
    Assumption of lower development (higher costs) future capacity costs for PROTRA with relation to the medium-reference scenario.
    """
    return _ext_data_capacity_investment_cost_protra_low_development(time())


_ext_data_capacity_investment_cost_protra_low_development = ExtData(
    "model_parameters/energy/energy-capacity_investment_cost.xlsx",
    "PROTRA",
    "time",
    "CAPACITY_INVESTMENT_COST_PROTRA_CHP_HP_PP_LOW_DEVELOPMENT",
    "interpolate",
    {"PROTRA_PP_CHP_HP_I": _subscript_dict["PROTRA_PP_CHP_HP_I"]},
    _root,
    {"PROTRA_PP_CHP_HP_I": _subscript_dict["PROTRA_PP_CHP_HP_I"]},
    "_ext_data_capacity_investment_cost_protra_low_development",
)


@component.add(
    name="CAPACITY_INVESTMENT_COST_PROTRA_MEDIUM_DEVELOPMENT",
    units="Mdollars_2015/MW",
    subscripts=["PROTRA_PP_CHP_HP_I"],
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_capacity_investment_cost_protra_medium_development",
        "__data__": "_ext_data_capacity_investment_cost_protra_medium_development",
        "time": 1,
    },
)
def capacity_investment_cost_protra_medium_development():
    return _ext_data_capacity_investment_cost_protra_medium_development(time())


_ext_data_capacity_investment_cost_protra_medium_development = ExtData(
    "model_parameters/energy/energy-capacity_investment_cost.xlsx",
    "PROTRA",
    "time",
    "CAPACITY_INVESTMENT_COST_PROTRA_CHP_HP_PP_MEDIUM_DEVELOPMENT",
    "interpolate",
    {"PROTRA_PP_CHP_HP_I": _subscript_dict["PROTRA_PP_CHP_HP_I"]},
    _root,
    {"PROTRA_PP_CHP_HP_I": _subscript_dict["PROTRA_PP_CHP_HP_I"]},
    "_ext_data_capacity_investment_cost_protra_medium_development",
)


@component.add(
    name="CAPACITY_INVESTMENT_COST_PROTRA_USER_DEFINED_SP",
    units="Mdollars_2015/MW",
    subscripts=["PROTRA_PP_CHP_HP_I"],
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_capacity_investment_cost_protra_user_defined_sp",
        "__data__": "_ext_data_capacity_investment_cost_protra_user_defined_sp",
        "time": 1,
    },
)
def capacity_investment_cost_protra_user_defined_sp():
    """
    Assumption from model user for future capacity costs for PROTRA.
    """
    return _ext_data_capacity_investment_cost_protra_user_defined_sp(time())


_ext_data_capacity_investment_cost_protra_user_defined_sp = ExtData(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "time",
    "CAPACITY_INVESTMENT_COST_PROTRA_CHP_HP_PP_USER_DEFINED",
    "interpolate",
    {"PROTRA_PP_CHP_HP_I": _subscript_dict["PROTRA_PP_CHP_HP_I"]},
    _root,
    {"PROTRA_PP_CHP_HP_I": _subscript_dict["PROTRA_PP_CHP_HP_I"]},
    "_ext_data_capacity_investment_cost_protra_user_defined_sp",
)


@component.add(
    name="capital_decommissioning_by_PROTRA",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I", "PROTRA_PP_CHP_HP_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_capacity_decommissioning_35r": 1,
        "unit_conversion_mw_tw": 1,
        "dynamic_capacity_investment_cost_protra_development": 1,
    },
)
def capital_decommissioning_by_protra():
    """
    Investment costs by PROTRA, calculated as the new capacity addition times the unitary cost ($/MW) in real terms.
    """
    return (
        sum(
            protra_capacity_decommissioning_35r()
            .loc[:, :, _subscript_dict["PROTRA_PP_CHP_HP_I"]]
            .rename({"NRG_TO_I": "NRG_TO_I!", "NRG_PROTRA_I": "PROTRA_PP_CHP_HP_I"}),
            dim=["NRG_TO_I!"],
        )
        * unit_conversion_mw_tw()
        * dynamic_capacity_investment_cost_protra_development()
    )


@component.add(
    name="capital_decommissioning_PROTRA_sectors",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I", "SECTORS_ENERGY_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "capital_decommissioning_by_protra": 1,
        "correspondence_matrix_protra_sectors": 1,
    },
)
def capital_decommissioning_protra_sectors():
    """
    Capita stock of PROTRA using projection of investments costs up to 2050, by economic sector (SECTORS_ENERGY_I is a subrange of the vector SECTORS_I).
    """
    return sum(
        capital_decommissioning_by_protra().rename(
            {"PROTRA_PP_CHP_HP_I": "PROTRA_PP_CHP_HP_I!"}
        )
        * correspondence_matrix_protra_sectors().rename(
            {"PROTRA_PP_CHP_HP_I": "PROTRA_PP_CHP_HP_I!"}
        ),
        dim=["PROTRA_PP_CHP_HP_I!"],
    )


@component.add(
    name="capital_depreciation_total_PROTRA",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"capital_depreciation": 15},
)
def capital_depreciation_total_protra():
    return (
        capital_depreciation().loc[:, "COKE"].reset_coords(drop=True) * 0
        + capital_depreciation().loc[:, "REFINING"].reset_coords(drop=True) * 0
        + capital_depreciation().loc[:, "HYDROGEN_PRODUCTION"].reset_coords(drop=True)
        * 0
        + capital_depreciation().loc[:, "ELECTRICITY_COAL"].reset_coords(drop=True)
        + capital_depreciation().loc[:, "ELECTRICITY_GAS"].reset_coords(drop=True)
        + capital_depreciation().loc[:, "ELECTRICITY_NUCLEAR"].reset_coords(drop=True)
        + capital_depreciation().loc[:, "ELECTRICITY_HYDRO"].reset_coords(drop=True)
        + capital_depreciation().loc[:, "ELECTRICITY_WIND"].reset_coords(drop=True)
        + capital_depreciation().loc[:, "ELECTRICITY_OIL"].reset_coords(drop=True)
        + capital_depreciation().loc[:, "ELECTRICITY_SOLAR_PV"].reset_coords(drop=True)
        + capital_depreciation()
        .loc[:, "ELECTRICITY_SOLAR_THERMAL"]
        .reset_coords(drop=True)
        + capital_depreciation().loc[:, "ELECTRICITY_OTHER"].reset_coords(drop=True)
        + capital_depreciation()
        .loc[:, "DISTRIBUTION_ELECTRICITY"]
        .reset_coords(drop=True)
        * 0
        + capital_depreciation().loc[:, "DISTRIBUTION_GAS"].reset_coords(drop=True) * 0
        + capital_depreciation().loc[:, "STEAM_HOT_WATER"].reset_coords(drop=True)
    )


@component.add(
    name="capital_stock_by_PROTRA",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I", "PROTRA_PP_CHP_HP_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_capacity_stock_35r": 1,
        "unit_conversion_mw_tw": 1,
        "dynamic_capacity_investment_cost_protra_development": 1,
    },
)
def capital_stock_by_protra():
    """
    Investment costs by PROTRA, calculated as the new capacity addition times the unitary cost ($/MW) in real terms.
    """
    return (
        sum(
            protra_capacity_stock_35r()
            .loc[:, :, _subscript_dict["PROTRA_PP_CHP_HP_I"]]
            .rename({"NRG_TO_I": "NRG_TO_I!", "NRG_PROTRA_I": "PROTRA_PP_CHP_HP_I"}),
            dim=["NRG_TO_I!"],
        )
        * unit_conversion_mw_tw()
        * dynamic_capacity_investment_cost_protra_development()
    )


@component.add(
    name="capital_stock_PROTRA_sectors",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I", "SECTORS_ENERGY_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "capital_stock_by_protra": 1,
        "correspondence_matrix_protra_sectors": 1,
    },
)
def capital_stock_protra_sectors():
    """
    Capita stock of PROTRA using projection of investments costs up to 2050, by economic sector (SECTORS_ENERGY_I is a subrange of the vector SECTORS_I).
    """
    return sum(
        capital_stock_by_protra().rename({"PROTRA_PP_CHP_HP_I": "PROTRA_PP_CHP_HP_I!"})
        * correspondence_matrix_protra_sectors().rename(
            {"PROTRA_PP_CHP_HP_I": "PROTRA_PP_CHP_HP_I!"}
        ),
        dim=["PROTRA_PP_CHP_HP_I!"],
    )


@component.add(
    name="CORRESPONDENCE_MATRIX_PROFLEX_SECTORS",
    units="DMNL",
    subscripts=["PRO_FLEXOPT_I", "SECTORS_ENERGY_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_correspondence_matrix_proflex_sectors"},
)
def correspondence_matrix_proflex_sectors():
    """
    Correspondence matrix to assign technologies of flexibility management to economic sectors.
    """
    return _ext_constant_correspondence_matrix_proflex_sectors()


_ext_constant_correspondence_matrix_proflex_sectors = ExtConstant(
    "model_parameters/economy/correspondence_matrixes.xlsx",
    "economy_energy",
    "CORRESPONDENCE_MATRIX_FLEXOPT_SECTORS",
    {
        "PRO_FLEXOPT_I": _subscript_dict["PRO_FLEXOPT_I"],
        "SECTORS_ENERGY_I": _subscript_dict["SECTORS_ENERGY_I"],
    },
    _root,
    {
        "PRO_FLEXOPT_I": _subscript_dict["PRO_FLEXOPT_I"],
        "SECTORS_ENERGY_I": _subscript_dict["SECTORS_ENERGY_I"],
    },
    "_ext_constant_correspondence_matrix_proflex_sectors",
)


@component.add(
    name="CORRESPONDENCE_MATRIX_PROTRA_SECTORS",
    units="DMNL",
    subscripts=["PROTRA_PP_CHP_HP_I", "SECTORS_ENERGY_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_correspondence_matrix_protra_sectors"},
)
def correspondence_matrix_protra_sectors():
    """
    Correspondence matrix to assign PROTRA to economic sectors.
    """
    return _ext_constant_correspondence_matrix_protra_sectors()


_ext_constant_correspondence_matrix_protra_sectors = ExtConstant(
    "model_parameters/economy/correspondence_matrixes.xlsx",
    "economy_energy",
    "CORRESPONDENCE_PROTRA_SECTORS",
    {
        "PROTRA_PP_CHP_HP_I": _subscript_dict["PROTRA_PP_CHP_HP_I"],
        "SECTORS_ENERGY_I": _subscript_dict["SECTORS_ENERGY_I"],
    },
    _root,
    {
        "PROTRA_PP_CHP_HP_I": _subscript_dict["PROTRA_PP_CHP_HP_I"],
        "SECTORS_ENERGY_I": _subscript_dict["SECTORS_ENERGY_I"],
    },
    "_ext_constant_correspondence_matrix_protra_sectors",
)


@component.add(
    name="CORRESPONDENCE_MATRIX_SECTORS_PROFLEX",
    units="DMNL",
    subscripts=["SECTORS_ENERGY_I", "PRO_FLEXOPT_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"correspondence_matrix_proflex_sectors": 15},
)
def correspondence_matrix_sectors_proflex():
    """
    Correspondence matrix to assign economic sectors to PROFLEX. Transpose 'CORRESPONDENCE_MATRIX_PROFLEX_SECTORS'.
    """
    value = xr.DataArray(
        np.nan,
        {
            "SECTORS_ENERGY_I": _subscript_dict["SECTORS_ENERGY_I"],
            "PRO_FLEXOPT_I": _subscript_dict["PRO_FLEXOPT_I"],
        },
        ["SECTORS_ENERGY_I", "PRO_FLEXOPT_I"],
    )
    value.loc[["COKE"], :] = (
        correspondence_matrix_proflex_sectors()
        .loc[:, "COKE"]
        .reset_coords(drop=True)
        .expand_dims({"CLUSTER_REFINED_PRODUCTS_INDUSTRY": ["COKE"]}, 0)
        .values
    )
    value.loc[["REFINING"], :] = (
        correspondence_matrix_proflex_sectors()
        .loc[:, "REFINING"]
        .reset_coords(drop=True)
        .expand_dims({"CLUSTER_REFINERY": _subscript_dict["CLUSTER_REFINERY"]}, 0)
        .values
    )
    value.loc[["HYDROGEN_PRODUCTION"], :] = (
        correspondence_matrix_proflex_sectors()
        .loc[:, "HYDROGEN_PRODUCTION"]
        .reset_coords(drop=True)
        .expand_dims({"CLUSTER_HYDROGEN": _subscript_dict["CLUSTER_HYDROGEN"]}, 0)
        .values
    )
    value.loc[["ELECTRICITY_COAL"], :] = (
        correspondence_matrix_proflex_sectors()
        .loc[:, "ELECTRICITY_COAL"]
        .reset_coords(drop=True)
        .expand_dims(
            {"CLUSTER_COAL_POWER_PLANTS": _subscript_dict["CLUSTER_COAL_POWER_PLANTS"]},
            0,
        )
        .values
    )
    value.loc[["ELECTRICITY_GAS"], :] = (
        correspondence_matrix_proflex_sectors()
        .loc[:, "ELECTRICITY_GAS"]
        .reset_coords(drop=True)
        .expand_dims(
            {"CLUSTER_GAS_POWER_PLANTS": _subscript_dict["CLUSTER_GAS_POWER_PLANTS"]}, 0
        )
        .values
    )
    value.loc[["ELECTRICITY_NUCLEAR"], :] = (
        correspondence_matrix_proflex_sectors()
        .loc[:, "ELECTRICITY_NUCLEAR"]
        .reset_coords(drop=True)
        .expand_dims(
            {
                "CLUSTER_NUCLEAR_POWER_PLANTS": _subscript_dict[
                    "CLUSTER_NUCLEAR_POWER_PLANTS"
                ]
            },
            0,
        )
        .values
    )
    value.loc[["ELECTRICITY_HYDRO"], :] = (
        correspondence_matrix_proflex_sectors()
        .loc[:, "ELECTRICITY_HYDRO"]
        .reset_coords(drop=True)
        .expand_dims(
            {
                "CLUSTER_HYDRO_POWER_PLANTS": _subscript_dict[
                    "CLUSTER_HYDRO_POWER_PLANTS"
                ]
            },
            0,
        )
        .values
    )
    value.loc[["ELECTRICITY_WIND"], :] = (
        correspondence_matrix_proflex_sectors()
        .loc[:, "ELECTRICITY_WIND"]
        .reset_coords(drop=True)
        .expand_dims(
            {"CLUSTER_WIND_POWER_PLANTS": _subscript_dict["CLUSTER_WIND_POWER_PLANTS"]},
            0,
        )
        .values
    )
    value.loc[["ELECTRICITY_OIL"], :] = (
        correspondence_matrix_proflex_sectors()
        .loc[:, "ELECTRICITY_OIL"]
        .reset_coords(drop=True)
        .expand_dims(
            {"CLUSTER_OIL_POWER_PLANTS": _subscript_dict["CLUSTER_OIL_POWER_PLANTS"]}, 0
        )
        .values
    )
    value.loc[["ELECTRICITY_SOLAR_PV"], :] = (
        correspondence_matrix_proflex_sectors()
        .loc[:, "ELECTRICITY_SOLAR_PV"]
        .reset_coords(drop=True)
        .expand_dims({"CLUSTER_SOLAR_POWER_PLANTS": ["ELECTRICITY_SOLAR_PV"]}, 0)
        .values
    )
    value.loc[["ELECTRICITY_SOLAR_THERMAL"], :] = (
        correspondence_matrix_proflex_sectors()
        .loc[:, "ELECTRICITY_SOLAR_THERMAL"]
        .reset_coords(drop=True)
        .expand_dims({"CLUSTER_SOLAR_POWER_PLANTS": ["ELECTRICITY_SOLAR_THERMAL"]}, 0)
        .values
    )
    value.loc[["ELECTRICITY_OTHER"], :] = (
        correspondence_matrix_proflex_sectors()
        .loc[:, "ELECTRICITY_OTHER"]
        .reset_coords(drop=True)
        .expand_dims(
            {
                "CLUSTER_BIOMASS_POWER_PLANTS": _subscript_dict[
                    "CLUSTER_BIOMASS_POWER_PLANTS"
                ]
            },
            0,
        )
        .values
    )
    value.loc[["DISTRIBUTION_ELECTRICITY"], :] = (
        correspondence_matrix_proflex_sectors()
        .loc[:, "DISTRIBUTION_ELECTRICITY"]
        .reset_coords(drop=True)
        .expand_dims(
            {
                "CLUSTER_ELECTRICITY_TRANSPORT": _subscript_dict[
                    "CLUSTER_ELECTRICITY_TRANSPORT"
                ]
            },
            0,
        )
        .values
    )
    value.loc[["DISTRIBUTION_GAS"], :] = (
        correspondence_matrix_proflex_sectors()
        .loc[:, "DISTRIBUTION_GAS"]
        .reset_coords(drop=True)
        .expand_dims({"CLUSTER_OTHER_ENERGY_ACTIVITIES": ["DISTRIBUTION_GAS"]}, 0)
        .values
    )
    value.loc[["STEAM_HOT_WATER"], :] = (
        correspondence_matrix_proflex_sectors()
        .loc[:, "STEAM_HOT_WATER"]
        .reset_coords(drop=True)
        .expand_dims({"CLUSTER_OTHER_ENERGY_ACTIVITIES": ["STEAM_HOT_WATER"]}, 0)
        .values
    )
    return value


@component.add(
    name="CORRESPONDENCE_MATRIX_SECTORS_PROTRA",
    units="DMNL",
    subscripts=["SECTORS_ENERGY_I", "PROTRA_PP_CHP_HP_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"correspondence_matrix_protra_sectors": 15},
)
def correspondence_matrix_sectors_protra():
    """
    Correspondence matrix to assign economic sectors to PROTRA. Transpose 'CORRESPONDENCE_MATRIX_PROTRA_SECTORS'.
    """
    value = xr.DataArray(
        np.nan,
        {
            "SECTORS_ENERGY_I": _subscript_dict["SECTORS_ENERGY_I"],
            "PROTRA_PP_CHP_HP_I": _subscript_dict["PROTRA_PP_CHP_HP_I"],
        },
        ["SECTORS_ENERGY_I", "PROTRA_PP_CHP_HP_I"],
    )
    value.loc[["COKE"], :] = (
        correspondence_matrix_protra_sectors()
        .loc[:, "COKE"]
        .reset_coords(drop=True)
        .expand_dims({"CLUSTER_REFINED_PRODUCTS_INDUSTRY": ["COKE"]}, 0)
        .values
    )
    value.loc[["REFINING"], :] = (
        correspondence_matrix_protra_sectors()
        .loc[:, "REFINING"]
        .reset_coords(drop=True)
        .expand_dims({"CLUSTER_REFINERY": _subscript_dict["CLUSTER_REFINERY"]}, 0)
        .values
    )
    value.loc[["HYDROGEN_PRODUCTION"], :] = (
        correspondence_matrix_protra_sectors()
        .loc[:, "HYDROGEN_PRODUCTION"]
        .reset_coords(drop=True)
        .expand_dims({"CLUSTER_HYDROGEN": _subscript_dict["CLUSTER_HYDROGEN"]}, 0)
        .values
    )
    value.loc[["ELECTRICITY_COAL"], :] = (
        correspondence_matrix_protra_sectors()
        .loc[:, "ELECTRICITY_COAL"]
        .reset_coords(drop=True)
        .expand_dims(
            {"CLUSTER_COAL_POWER_PLANTS": _subscript_dict["CLUSTER_COAL_POWER_PLANTS"]},
            0,
        )
        .values
    )
    value.loc[["ELECTRICITY_GAS"], :] = (
        correspondence_matrix_protra_sectors()
        .loc[:, "ELECTRICITY_GAS"]
        .reset_coords(drop=True)
        .expand_dims(
            {"CLUSTER_GAS_POWER_PLANTS": _subscript_dict["CLUSTER_GAS_POWER_PLANTS"]}, 0
        )
        .values
    )
    value.loc[["ELECTRICITY_NUCLEAR"], :] = (
        correspondence_matrix_protra_sectors()
        .loc[:, "ELECTRICITY_NUCLEAR"]
        .reset_coords(drop=True)
        .expand_dims(
            {
                "CLUSTER_NUCLEAR_POWER_PLANTS": _subscript_dict[
                    "CLUSTER_NUCLEAR_POWER_PLANTS"
                ]
            },
            0,
        )
        .values
    )
    value.loc[["ELECTRICITY_HYDRO"], :] = (
        correspondence_matrix_protra_sectors()
        .loc[:, "ELECTRICITY_HYDRO"]
        .reset_coords(drop=True)
        .expand_dims(
            {
                "CLUSTER_HYDRO_POWER_PLANTS": _subscript_dict[
                    "CLUSTER_HYDRO_POWER_PLANTS"
                ]
            },
            0,
        )
        .values
    )
    value.loc[["ELECTRICITY_WIND"], :] = (
        correspondence_matrix_protra_sectors()
        .loc[:, "ELECTRICITY_WIND"]
        .reset_coords(drop=True)
        .expand_dims(
            {"CLUSTER_WIND_POWER_PLANTS": _subscript_dict["CLUSTER_WIND_POWER_PLANTS"]},
            0,
        )
        .values
    )
    value.loc[["ELECTRICITY_OIL"], :] = (
        correspondence_matrix_protra_sectors()
        .loc[:, "ELECTRICITY_OIL"]
        .reset_coords(drop=True)
        .expand_dims(
            {"CLUSTER_OIL_POWER_PLANTS": _subscript_dict["CLUSTER_OIL_POWER_PLANTS"]}, 0
        )
        .values
    )
    value.loc[["ELECTRICITY_SOLAR_PV"], :] = (
        correspondence_matrix_protra_sectors()
        .loc[:, "ELECTRICITY_SOLAR_PV"]
        .reset_coords(drop=True)
        .expand_dims({"CLUSTER_SOLAR_POWER_PLANTS": ["ELECTRICITY_SOLAR_PV"]}, 0)
        .values
    )
    value.loc[["ELECTRICITY_SOLAR_THERMAL"], :] = (
        correspondence_matrix_protra_sectors()
        .loc[:, "ELECTRICITY_SOLAR_THERMAL"]
        .reset_coords(drop=True)
        .expand_dims({"CLUSTER_SOLAR_POWER_PLANTS": ["ELECTRICITY_SOLAR_THERMAL"]}, 0)
        .values
    )
    value.loc[["ELECTRICITY_OTHER"], :] = (
        correspondence_matrix_protra_sectors()
        .loc[:, "ELECTRICITY_OTHER"]
        .reset_coords(drop=True)
        .expand_dims(
            {
                "CLUSTER_BIOMASS_POWER_PLANTS": _subscript_dict[
                    "CLUSTER_BIOMASS_POWER_PLANTS"
                ]
            },
            0,
        )
        .values
    )
    value.loc[["DISTRIBUTION_ELECTRICITY"], :] = (
        correspondence_matrix_protra_sectors()
        .loc[:, "DISTRIBUTION_ELECTRICITY"]
        .reset_coords(drop=True)
        .expand_dims(
            {
                "CLUSTER_ELECTRICITY_TRANSPORT": _subscript_dict[
                    "CLUSTER_ELECTRICITY_TRANSPORT"
                ]
            },
            0,
        )
        .values
    )
    value.loc[["DISTRIBUTION_GAS"], :] = (
        correspondence_matrix_protra_sectors()
        .loc[:, "DISTRIBUTION_GAS"]
        .reset_coords(drop=True)
        .expand_dims({"CLUSTER_OTHER_ENERGY_ACTIVITIES": ["DISTRIBUTION_GAS"]}, 0)
        .values
    )
    value.loc[["STEAM_HOT_WATER"], :] = (
        correspondence_matrix_protra_sectors()
        .loc[:, "STEAM_HOT_WATER"]
        .reset_coords(drop=True)
        .expand_dims({"CLUSTER_OTHER_ENERGY_ACTIVITIES": ["STEAM_HOT_WATER"]}, 0)
        .values
    )
    return value


@component.add(
    name="delayed_TS_GFCF_PROTRA_sectors_35R",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I", "SECTORS_ENERGY_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_gfcf_protra_sectors_35r": 1},
    other_deps={
        "_delayfixed_delayed_ts_gfcf_protra_sectors_35r": {
            "initial": {"time_step": 1},
            "step": {"investment_cost_protra_sectors_35r": 1},
        }
    },
)
def delayed_ts_gfcf_protra_sectors_35r():
    """
    DELAY to avoid feedback problems.
    """
    return _delayfixed_delayed_ts_gfcf_protra_sectors_35r()


_delayfixed_delayed_ts_gfcf_protra_sectors_35r = DelayFixed(
    lambda: investment_cost_protra_sectors_35r(),
    lambda: time_step(),
    lambda: xr.DataArray(
        0,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "SECTORS_ENERGY_I": _subscript_dict["SECTORS_ENERGY_I"],
        },
        ["REGIONS_35_I", "SECTORS_ENERGY_I"],
    ),
    time_step,
    "_delayfixed_delayed_ts_gfcf_protra_sectors_35r",
)


@component.add(
    name="diff_NFCF_energy_PROTRA",
    units="1",
    subscripts=["REGIONS_35_I", "SECTORS_ENERGY_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "investment_cost_protra_sectors_35r": 1,
        "gross_fixed_capital_formation_real": 1,
        "capital_depreciation": 1,
    },
)
def diff_nfcf_energy_protra():
    """
    Net Fixed Capital Formation
    """
    return -1 + zidz(
        investment_cost_protra_sectors_35r(),
        gross_fixed_capital_formation_real()
        .loc[:, _subscript_dict["SECTORS_ENERGY_I"]]
        .rename({"SECTORS_I": "SECTORS_ENERGY_I"})
        - capital_depreciation()
        .loc[:, _subscript_dict["SECTORS_ENERGY_I"]]
        .rename({"SECTORS_I": "SECTORS_ENERGY_I"}),
    )


@component.add(
    name="diff_NFCF_total_PROTRA",
    units="1",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "total_protra_investment_cost_35r": 1,
        "gfcf_real_total_protra": 1,
        "capital_depreciation_total_protra": 1,
    },
)
def diff_nfcf_total_protra():
    return -1 + zidz(
        total_protra_investment_cost_35r(),
        gfcf_real_total_protra() - capital_depreciation_total_protra(),
    )


@component.add(
    name="dynamic_capacity_investment_cost_PROFLEX_development",
    units="Mdollars_2015/MW",
    subscripts=["REGIONS_9_I", "PRO_FLEXOPT_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_energy": 2,
        "capacity_investment_cost_proflex_development": 4,
        "correspondence_matrix_sectors_proflex": 2,
        "price_gfcf": 2,
    },
)
def dynamic_capacity_investment_cost_proflex_development():
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "PRO_FLEXOPT_I": _subscript_dict["PRO_FLEXOPT_I"],
        },
        ["REGIONS_9_I", "PRO_FLEXOPT_I"],
    )
    value.loc[_subscript_dict["REGIONS_8_I"], :] = (
        if_then_else(
            switch_energy() == 0,
            lambda: capacity_investment_cost_proflex_development().expand_dims(
                {"REGIONS_8_I": _subscript_dict["REGIONS_8_I"]}, 1
            ),
            lambda: capacity_investment_cost_proflex_development()
            * sum(
                price_gfcf()
                .loc[
                    _subscript_dict["REGIONS_8_I"], _subscript_dict["SECTORS_ENERGY_I"]
                ]
                .rename(
                    {
                        "REGIONS_35_I": "REGIONS_8_I",
                        "SECTORS_MAP_I": "SECTORS_ENERGY_I!",
                    }
                )
                * correspondence_matrix_sectors_proflex().rename(
                    {"SECTORS_ENERGY_I": "SECTORS_ENERGY_I!"}
                )
                / 100,
                dim=["SECTORS_ENERGY_I!"],
            ).transpose("PRO_FLEXOPT_I", "REGIONS_8_I"),
        )
        .transpose("REGIONS_8_I", "PRO_FLEXOPT_I")
        .values
    )
    value.loc[["EU27"], :] = (
        if_then_else(
            switch_energy() == 0,
            lambda: capacity_investment_cost_proflex_development(),
            lambda: capacity_investment_cost_proflex_development()
            * sum(
                price_gfcf()
                .loc["GERMANY", _subscript_dict["SECTORS_ENERGY_I"]]
                .reset_coords(drop=True)
                .rename({"SECTORS_MAP_I": "SECTORS_ENERGY_I!"})
                * correspondence_matrix_sectors_proflex().rename(
                    {"SECTORS_ENERGY_I": "SECTORS_ENERGY_I!"}
                )
                / 100,
                dim=["SECTORS_ENERGY_I!"],
            ),
        )
        .expand_dims({"REGIONS_36_I": ["EU27"]}, 0)
        .values
    )
    return value


@component.add(
    name="dynamic_capacity_investment_cost_PROTRA_development",
    units="Mdollars_2015/MW",
    subscripts=["REGIONS_35_I", "PROTRA_PP_CHP_HP_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_energy": 1,
        "capacity_investment_cost_protra_development": 2,
        "price_gfcf": 1,
        "correspondence_matrix_sectors_protra": 1,
    },
)
def dynamic_capacity_investment_cost_protra_development():
    """
    Capacity investment cost dynamized by the price of investments (price_GFCF) from economy module. Can be compared with the exogenous values in 'CAPACITY INVESTMENT COST PROTRA DEVELOPMENT'.
    """
    return if_then_else(
        switch_energy() == 0,
        lambda: capacity_investment_cost_protra_development().expand_dims(
            {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]}, 1
        ),
        lambda: capacity_investment_cost_protra_development()
        * sum(
            price_gfcf()
            .loc[:, _subscript_dict["SECTORS_ENERGY_I"]]
            .rename({"SECTORS_MAP_I": "SECTORS_ENERGY_I!"})
            * correspondence_matrix_sectors_protra().rename(
                {"SECTORS_ENERGY_I": "SECTORS_ENERGY_I!"}
            )
            / 100,
            dim=["SECTORS_ENERGY_I!"],
        ).transpose("PROTRA_PP_CHP_HP_I", "REGIONS_35_I"),
    ).transpose("REGIONS_35_I", "PROTRA_PP_CHP_HP_I")


@component.add(
    name="dynamic_capacity_investment_cost_PROTRA_development_36R",
    units="Mdollars_2015/MW",
    subscripts=["REGIONS_36_I", "PROTRA_PP_CHP_HP_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "dynamic_capacity_investment_cost_protra_development": 1,
        "dynamic_capacity_investment_cost_protra_development_eu27": 1,
    },
)
def dynamic_capacity_investment_cost_protra_development_36r():
    """
    Capacity investment cost dynamized by the price of investments (price_GFCF) from economy module for 36 regions. Can be compared with the exogenous values in 'CAPACITY INVESTMENT COST PROTRA DEVELOPMENT'.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_36_I": _subscript_dict["REGIONS_36_I"],
            "PROTRA_PP_CHP_HP_I": _subscript_dict["PROTRA_PP_CHP_HP_I"],
        },
        ["REGIONS_36_I", "PROTRA_PP_CHP_HP_I"],
    )
    value.loc[
        _subscript_dict["REGIONS_35_I"], :
    ] = dynamic_capacity_investment_cost_protra_development().values
    value.loc[["EU27"], :] = (
        dynamic_capacity_investment_cost_protra_development_eu27()
        .loc["EU27", :]
        .reset_coords(drop=True)
        .expand_dims({"REGIONS_36_I": ["EU27"]}, 0)
        .values
    )
    return value


@component.add(
    name="dynamic_capacity_investment_cost_PROTRA_development_EU27",
    units="Mdollars_2015/MW",
    subscripts=["REGIONS_36_I", "PROTRA_PP_CHP_HP_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"dynamic_capacity_investment_cost_protra_development": 1},
)
def dynamic_capacity_investment_cost_protra_development_eu27():
    """
    Dynamic capacity investment cost downscaled for the 27 EU countries.
    """
    return (
        sum(
            dynamic_capacity_investment_cost_protra_development()
            .loc[_subscript_dict["REGIONS_EU27_I"], :]
            .rename({"REGIONS_35_I": "REGIONS_EU27_I!"}),
            dim=["REGIONS_EU27_I!"],
        )
        / 27
    ).expand_dims({"REGIONS_36_I": ["EU27"]}, 0)


@component.add(
    name="GFCF_real_total_PROTRA",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"gross_fixed_capital_formation_real": 15},
)
def gfcf_real_total_protra():
    """
    Excluding from the comparison those energy investments not computed bottom-up.
    """
    return (
        gross_fixed_capital_formation_real().loc[:, "COKE"].reset_coords(drop=True) * 0
        + gross_fixed_capital_formation_real()
        .loc[:, "REFINING"]
        .reset_coords(drop=True)
        * 0
        + gross_fixed_capital_formation_real()
        .loc[:, "HYDROGEN_PRODUCTION"]
        .reset_coords(drop=True)
        * 0
        + gross_fixed_capital_formation_real()
        .loc[:, "ELECTRICITY_COAL"]
        .reset_coords(drop=True)
        + gross_fixed_capital_formation_real()
        .loc[:, "ELECTRICITY_GAS"]
        .reset_coords(drop=True)
        + gross_fixed_capital_formation_real()
        .loc[:, "ELECTRICITY_NUCLEAR"]
        .reset_coords(drop=True)
        + gross_fixed_capital_formation_real()
        .loc[:, "ELECTRICITY_HYDRO"]
        .reset_coords(drop=True)
        + gross_fixed_capital_formation_real()
        .loc[:, "ELECTRICITY_WIND"]
        .reset_coords(drop=True)
        + gross_fixed_capital_formation_real()
        .loc[:, "ELECTRICITY_OIL"]
        .reset_coords(drop=True)
        + gross_fixed_capital_formation_real()
        .loc[:, "ELECTRICITY_SOLAR_PV"]
        .reset_coords(drop=True)
        + gross_fixed_capital_formation_real()
        .loc[:, "ELECTRICITY_SOLAR_THERMAL"]
        .reset_coords(drop=True)
        + gross_fixed_capital_formation_real()
        .loc[:, "ELECTRICITY_OTHER"]
        .reset_coords(drop=True)
        + gross_fixed_capital_formation_real()
        .loc[:, "DISTRIBUTION_ELECTRICITY"]
        .reset_coords(drop=True)
        * 0
        + gross_fixed_capital_formation_real()
        .loc[:, "DISTRIBUTION_GAS"]
        .reset_coords(drop=True)
        * 0
        + gross_fixed_capital_formation_real()
        .loc[:, "STEAM_HOT_WATER"]
        .reset_coords(drop=True)
    )


@component.add(
    name="investment_cost_PROFLEX",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_9_I", "PRO_FLEXOPT_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "proflex_capacity_expansion": 1,
        "unit_conversion_mw_tw": 1,
        "dynamic_capacity_investment_cost_proflex_development": 1,
    },
)
def investment_cost_proflex():
    """
    Investment costs by FLEXOPT, calculated as the new capacity addition times the unitary cost ($/MW) in real terms.
    """
    return (
        proflex_capacity_expansion()
        * unit_conversion_mw_tw()
        * dynamic_capacity_investment_cost_proflex_development()
    )


@component.add(
    name="investment_cost_PROFLEX_sectors",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_9_I", "SECTORS_ENERGY_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "investment_cost_proflex": 1,
        "correspondence_matrix_proflex_sectors": 1,
    },
)
def investment_cost_proflex_sectors():
    """
    Investments costs FLEXOPT using projection of investments costs up to 2050, by economic sector (SECTORS_ENERGY_I is a subrange of the vector SECTORS_I).
    """
    return sum(
        investment_cost_proflex().rename({"PRO_FLEXOPT_I": "PRO_FLEXOPT_I!"})
        * correspondence_matrix_proflex_sectors().rename(
            {"PRO_FLEXOPT_I": "PRO_FLEXOPT_I!"}
        ),
        dim=["PRO_FLEXOPT_I!"],
    )


@component.add(
    name="investment_cost_PROTRA_35R",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I", "PROTRA_PP_CHP_HP_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_capacity_expansion_35r": 1,
        "unit_conversion_mw_tw": 1,
        "dynamic_capacity_investment_cost_protra_development": 1,
    },
)
def investment_cost_protra_35r():
    """
    Investment costs by PROTRA, calculated as the new capacity addition times the unitary cost ($/MW) in real terms.
    """
    return (
        sum(
            protra_capacity_expansion_35r()
            .loc[:, :, _subscript_dict["PROTRA_PP_CHP_HP_I"]]
            .rename({"NRG_TO_I": "NRG_TO_I!", "NRG_PROTRA_I": "PROTRA_PP_CHP_HP_I"}),
            dim=["NRG_TO_I!"],
        )
        * unit_conversion_mw_tw()
        * dynamic_capacity_investment_cost_protra_development()
    )


@component.add(
    name="investment_cost_PROTRA_sectors_35R",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I", "SECTORS_ENERGY_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "investment_cost_protra_35r": 1,
        "correspondence_matrix_protra_sectors": 1,
    },
)
def investment_cost_protra_sectors_35r():
    """
    Investments costs PROTRA using projection of investments costs up to 2050, by economic sector (SECTORS_ENERGY_I is a subrange of the vector SECTORS_I).
    """
    return sum(
        investment_cost_protra_35r().rename(
            {"PROTRA_PP_CHP_HP_I": "PROTRA_PP_CHP_HP_I!"}
        )
        * correspondence_matrix_protra_sectors().rename(
            {"PROTRA_PP_CHP_HP_I": "PROTRA_PP_CHP_HP_I!"}
        ),
        dim=["PROTRA_PP_CHP_HP_I!"],
    )


@component.add(
    name="investment_cost_PROTRA_sectors_9R",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_9_I", "SECTORS_ENERGY_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "investment_cost_protra_sectors_35r": 1,
        "investment_cost_protra_sectors_eu27": 1,
    },
)
def investment_cost_protra_sectors_9r():
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "SECTORS_ENERGY_I": _subscript_dict["SECTORS_ENERGY_I"],
        },
        ["REGIONS_9_I", "SECTORS_ENERGY_I"],
    )
    value.loc[_subscript_dict["REGIONS_8_I"], :] = (
        investment_cost_protra_sectors_35r()
        .loc[_subscript_dict["REGIONS_8_I"], :]
        .rename({"REGIONS_35_I": "REGIONS_8_I"})
        .values
    )
    value.loc[["EU27"], :] = (
        investment_cost_protra_sectors_eu27()
        .loc["EU27", :]
        .reset_coords(drop=True)
        .expand_dims({"REGIONS_36_I": ["EU27"]}, 0)
        .values
    )
    return value


@component.add(
    name="investment_cost_PROTRA_sectors_EU27",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_36_I", "SECTORS_ENERGY_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"investment_cost_protra_sectors_35r": 1},
)
def investment_cost_protra_sectors_eu27():
    return sum(
        investment_cost_protra_sectors_35r()
        .loc[_subscript_dict["REGIONS_EU27_I"], :]
        .rename({"REGIONS_35_I": "REGIONS_EU27_I!"}),
        dim=["REGIONS_EU27_I!"],
    ).expand_dims({"REGIONS_36_I": ["EU27"]}, 0)


@component.add(
    name="investment_cost_stationary_electrolysers",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "stationary_electrolyzers_capacity_expansion": 1,
        "unit_conversion_mw_tw": 1,
        "dynamic_capacity_investment_cost_proflex_development": 1,
    },
)
def investment_cost_stationary_electrolysers():
    """
    Investment costs if stationary electrolysers, assuming same cost than flexible electrolysers.
    """
    return (
        stationary_electrolyzers_capacity_expansion()
        * unit_conversion_mw_tw()
        * dynamic_capacity_investment_cost_proflex_development()
        .loc[:, "PROSUP_elec_2_hydrogen"]
        .reset_coords(drop=True)
    )


@component.add(
    name="investment_cost_stationary_electrolysers_sectors",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_9_I", "CLUSTER_HYDROGEN"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"investment_cost_stationary_electrolysers": 1},
)
def investment_cost_stationary_electrolysers_sectors():
    return investment_cost_stationary_electrolysers().expand_dims(
        {"CLUSTER_HYDROGEN": _subscript_dict["CLUSTER_HYDROGEN"]}, 1
    )


@component.add(
    name="PRO_FLEXOPT_CAPACITY_INVESTMENT_COST_2015",
    units="Mdollars_2015/MW",
    subscripts=["PRO_FLEXOPT_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_pro_flexopt_capacity_investment_cost_2015"
    },
)
def pro_flexopt_capacity_investment_cost_2015():
    """
    Since the cost of electrolyzers does not have a defined value (it is defined in a range) MIN, MEDIUM and HIGH INVESTMENT COST do not coincide in 2015; the value corresponding to CAPACITY_INVESTMENT_COST_PRO_FLEXOPT_MEDIUM for PRO_FLEXOPT elec 2 hydrogen will be taken.
    """
    return _ext_constant_pro_flexopt_capacity_investment_cost_2015()


_ext_constant_pro_flexopt_capacity_investment_cost_2015 = ExtConstant(
    "model_parameters/energy/energy-capacity_investment_cost.xlsx",
    "PRO_FLEXOPT",
    "CAPACITY_INVESTMENT_COST_PRO_FLEXOPT_2015*",
    {"PRO_FLEXOPT_I": _subscript_dict["PRO_FLEXOPT_I"]},
    _root,
    {"PRO_FLEXOPT_I": _subscript_dict["PRO_FLEXOPT_I"]},
    "_ext_constant_pro_flexopt_capacity_investment_cost_2015",
)


@component.add(
    name="PROTRA_CAPACITY_INVESTMENT_COST_2015",
    units="Mdollars_2015/MW",
    subscripts=["PROTRA_PP_CHP_HP_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_protra_capacity_investment_cost_2015"},
)
def protra_capacity_investment_cost_2015():
    return _ext_constant_protra_capacity_investment_cost_2015()


_ext_constant_protra_capacity_investment_cost_2015 = ExtConstant(
    "model_parameters/energy/energy-capacity_investment_cost.xlsx",
    "PROTRA",
    "CAPACITY_INVESTMENT_COST_PROTRA_CHP_HP_PP_2015*",
    {"PROTRA_PP_CHP_HP_I": _subscript_dict["PROTRA_PP_CHP_HP_I"]},
    _root,
    {"PROTRA_PP_CHP_HP_I": _subscript_dict["PROTRA_PP_CHP_HP_I"]},
    "_ext_constant_protra_capacity_investment_cost_2015",
)


@component.add(
    name="ratio_investment_cost_energy_vs_total_GFCF",
    units="1",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_protra_investment_cost_35r": 1, "total_gfcf": 1},
)
def ratio_investment_cost_energy_vs_total_gfcf():
    """
    Ratio for checking how much of the GFCF comes from the energy sector.
    """
    return zidz(total_protra_investment_cost_35r(), total_gfcf())


@component.add(
    name="SELECT_CAPACITY_INVESTMENT_COST_DEVELOPMENT_SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_select_capacity_investment_cost_development_sp"
    },
)
def select_capacity_investment_cost_development_sp():
    """
    0: constant 2015 values 1: low cost improvement development 2: medium cost improvement development 3: high cost improvement development 4: user-defined
    """
    return _ext_constant_select_capacity_investment_cost_development_sp()


_ext_constant_select_capacity_investment_cost_development_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "SELECT_CAPACITY_INVESTMENT_COST_DEVELOPMENT_SP",
    {},
    _root,
    {},
    "_ext_constant_select_capacity_investment_cost_development_sp",
)


@component.add(
    name="total_energy_capacities_investment_cost",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "investment_cost_stationary_electrolysers_sectors": 1,
        "total_proflex_investment_cost": 1,
        "investment_cost_protra_sectors_9r": 1,
    },
)
def total_energy_capacities_investment_cost():
    """
    Total investment cost of new energy capacities for PROTRAs, electrolysers for H2 and synthetic fuels, and PROFLEX.
    """
    return (
        investment_cost_stationary_electrolysers_sectors()
        .loc[:, "HYDROGEN_PRODUCTION"]
        .reset_coords(drop=True)
        + total_proflex_investment_cost()
        + sum(
            investment_cost_protra_sectors_9r().rename(
                {"SECTORS_ENERGY_I": "SECTORS_ENERGY_I!"}
            ),
            dim=["SECTORS_ENERGY_I!"],
        )
    )


@component.add(
    name="total_GFCF",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"gross_fixed_capital_formation_real": 1},
)
def total_gfcf():
    return sum(
        gross_fixed_capital_formation_real().rename({"SECTORS_I": "SECTORS_I!"}),
        dim=["SECTORS_I!"],
    )


@component.add(
    name="total_PROFLEX_investment_cost",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"investment_cost_proflex_sectors": 1},
)
def total_proflex_investment_cost():
    return sum(
        investment_cost_proflex_sectors().rename(
            {"SECTORS_ENERGY_I": "SECTORS_ENERGY_I!"}
        ),
        dim=["SECTORS_ENERGY_I!"],
    )


@component.add(
    name="total_PROTRA_investment_cost_35R",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"investment_cost_protra_sectors_35r": 1},
)
def total_protra_investment_cost_35r():
    return sum(
        investment_cost_protra_sectors_35r().rename(
            {"SECTORS_ENERGY_I": "SECTORS_ENERGY_I!"}
        ),
        dim=["SECTORS_ENERGY_I!"],
    )
