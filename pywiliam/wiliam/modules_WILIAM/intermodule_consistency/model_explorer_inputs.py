"""
Module intermodule_consistency.model_explorer_inputs
Translated using PySD version 3.10.0
"""


@component.add(
    name="FINAL_YEAR_MODEL_EXPLORER",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_final_year_model_explorer"},
)
def final_year_model_explorer():
    """
    FINAL_YEAR_MODEL_EXPLORER
    """
    return _ext_constant_final_year_model_explorer()


_ext_constant_final_year_model_explorer = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "inputs_model_explorer",
    "FINAL_YEAR_MODEL_EXPLORER",
    {},
    _root,
    {},
    "_ext_constant_final_year_model_explorer",
)


@component.add(
    name="FINAL_YEAR_WORKING_TIME",
    units="Year",
    comp_type="Constant",
    comp_subtype="Normal",
)
def final_year_working_time():
    """
    FINAL_YEAR_WORKING_TIME
    """
    return 2030


@component.add(
    name="INITIAL_YEAR_MODEL_EXPLORER",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_year_model_explorer"},
)
def initial_year_model_explorer():
    """
    INITIAL_YEAR_MODEL_EXPLORER
    """
    return _ext_constant_initial_year_model_explorer()


_ext_constant_initial_year_model_explorer = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "inputs_model_explorer",
    "INITIAL_YEAR_MODEL_EXPLORER",
    {},
    _root,
    {},
    "_ext_constant_initial_year_model_explorer",
)


@component.add(
    name="model_explorer_change_to_regenerative_agriculture",
    units="DMNL/Year",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_change_to_regenerative_agriculture_me": 3,
        "time": 6,
        "scenario_select_change_to_regenerative_agriculture_option_1_me": 1,
        "final_year_model_explorer": 5,
        "initial_year_model_explorer": 5,
        "initial_share_of_regenerative_agriculture": 2,
        "scenario_select_change_to_regenerative_agriculture_option_2_me": 1,
        "scenario_select_change_to_regenerative_agriculture_option_3_me": 1,
    },
)
def model_explorer_change_to_regenerative_agriculture():
    """
    Policy Change to Regenerative Agriculture for model explorer.
    """
    return if_then_else(
        select_change_to_regenerative_agriculture_me() == 1,
        lambda: if_then_else(
            np.logical_and(
                time() > initial_year_model_explorer(),
                time() < final_year_model_explorer(),
            ),
            lambda: scenario_select_change_to_regenerative_agriculture_option_1_me(),
            lambda: xr.DataArray(
                0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
            ),
        ).expand_dims({"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"]}, 1),
        lambda: if_then_else(
            select_change_to_regenerative_agriculture_me() == 2,
            lambda: if_then_else(
                np.logical_and(
                    time() > initial_year_model_explorer(),
                    time() < final_year_model_explorer(),
                ),
                lambda: (
                    scenario_select_change_to_regenerative_agriculture_option_2_me()
                    - initial_share_of_regenerative_agriculture()
                )
                / (final_year_model_explorer() - initial_year_model_explorer()),
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
                select_change_to_regenerative_agriculture_me() == 3,
                lambda: if_then_else(
                    np.logical_and(
                        time() > initial_year_model_explorer(),
                        time() < final_year_model_explorer(),
                    ),
                    lambda: (
                        scenario_select_change_to_regenerative_agriculture_option_3_me()
                        - initial_share_of_regenerative_agriculture()
                    )
                    / (final_year_model_explorer() - initial_year_model_explorer()),
                    lambda: xr.DataArray(
                        0,
                        {
                            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                            "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
                        },
                        ["REGIONS_9_I", "LAND_PRODUCTS_I"],
                    ),
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
        ),
    )


@component.add(
    name="model_explorer_climate_sensitivity",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "scenario_climate_sensitivity_option_2_me": 2,
        "scenario_climate_sensitivity_option_1_me": 1,
        "select_climate_sensitivity_me": 3,
        "scenario_climate_sensitivity_option_3_me": 1,
    },
)
def model_explorer_climate_sensitivity():
    """
    Hypothesis climate sensitivity for model explorer.
    """
    return if_then_else(
        time() < 2015,
        lambda: scenario_climate_sensitivity_option_2_me(),
        lambda: if_then_else(
            select_climate_sensitivity_me() == 1,
            lambda: scenario_climate_sensitivity_option_1_me(),
            lambda: if_then_else(
                select_climate_sensitivity_me() == 2,
                lambda: scenario_climate_sensitivity_option_2_me(),
                lambda: if_then_else(
                    select_climate_sensitivity_me() == 3,
                    lambda: scenario_climate_sensitivity_option_3_me(),
                    lambda: 0,
                ),
            ),
        ),
    )


@component.add(
    name="model_explorer_debt_interest_rate_target",
    units="DMNL/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_debt_interest_rate_target_me": 3,
        "time": 3,
        "scenario_debt_interest_rate_target_option_1_me": 1,
        "initial_year_model_explorer": 3,
        "debt_interest_rate_historic": 6,
        "scenario_debt_interest_rate_target_option_2_me": 1,
        "scenario_debt_interest_rate_target_option_3_me": 1,
    },
)
def model_explorer_debt_interest_rate_target():
    """
    Policy debt interest rate target for model explorer.
    """
    return if_then_else(
        select_debt_interest_rate_target_me() == 1,
        lambda: if_then_else(
            time() < initial_year_model_explorer(),
            lambda: debt_interest_rate_historic(),
            lambda: scenario_debt_interest_rate_target_option_1_me()
            + debt_interest_rate_historic(),
        ),
        lambda: if_then_else(
            select_debt_interest_rate_target_me() == 2,
            lambda: if_then_else(
                time() < initial_year_model_explorer(),
                lambda: debt_interest_rate_historic(),
                lambda: scenario_debt_interest_rate_target_option_2_me()
                + debt_interest_rate_historic(),
            ),
            lambda: if_then_else(
                select_debt_interest_rate_target_me() == 3,
                lambda: if_then_else(
                    time() < initial_year_model_explorer(),
                    lambda: debt_interest_rate_historic(),
                    lambda: scenario_debt_interest_rate_target_option_3_me()
                    + debt_interest_rate_historic(),
                ),
                lambda: xr.DataArray(
                    0,
                    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
                    ["REGIONS_35_I"],
                ),
            ),
        ),
    )


@component.add(
    name="model_explorer_diets",
    units="kg/(Year*person)",
    subscripts=["REGIONS_9_I", "FOODS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_tipe_diets_me": 3,
        "scenario_flexitariana_option_1_me": 1,
        "scenario_plant_based_100_option_3_me": 1,
        "scenario_baseline_option_2_me": 1,
    },
)
def model_explorer_diets():
    """
    Policy diets for model explorer.
    """
    return if_then_else(
        select_tipe_diets_me() == 1,
        lambda: scenario_flexitariana_option_1_me(),
        lambda: if_then_else(
            select_tipe_diets_me() == 2,
            lambda: scenario_baseline_option_2_me(),
            lambda: if_then_else(
                select_tipe_diets_me() == 3,
                lambda: scenario_plant_based_100_option_3_me(),
                lambda: xr.DataArray(
                    0,
                    {
                        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                        "FOODS_I": _subscript_dict["FOODS_I"],
                    },
                    ["REGIONS_9_I", "FOODS_I"],
                ),
            ),
        ),
    )


@component.add(
    name="model_explorer_energy_efficiency_anual_improvement",
    units="1/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "initial_year_model_explorer": 1,
        "historical_energy_efficiency_annual_improvement": 1,
        "scenario_energy_efficiency_option_1_me": 1,
        "select_energy_efficiency_annual_improvement_me": 3,
        "scenario_energy_efficiency_option_3_me": 1,
        "scenario_energy_efficiency_option_2_me": 1,
    },
)
def model_explorer_energy_efficiency_anual_improvement():
    """
    Policy government deficit of surplus for model explorer.
    """
    return if_then_else(
        time() < initial_year_model_explorer(),
        lambda: historical_energy_efficiency_annual_improvement(),
        lambda: if_then_else(
            select_energy_efficiency_annual_improvement_me() == 1,
            lambda: scenario_energy_efficiency_option_1_me(),
            lambda: if_then_else(
                select_energy_efficiency_annual_improvement_me() == 2,
                lambda: scenario_energy_efficiency_option_2_me(),
                lambda: if_then_else(
                    select_energy_efficiency_annual_improvement_me() == 3,
                    lambda: scenario_energy_efficiency_option_3_me(),
                    lambda: xr.DataArray(
                        1,
                        {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
                        ["REGIONS_35_I"],
                    ),
                ),
            ),
        ),
    )


@component.add(
    name="model_explorer_fertility_rates",
    units="people/(kpeople*Year)",
    subscripts=["REGIONS_35_I", "SEX_I", "FERTILITY_AGES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_fertility_rates_me": 3,
        "historical_fertility_rates_2015_2020": 3,
        "final_year_model_explorer": 3,
        "scenario_fertility_rates_option_1_me": 1,
        "scenario_fertility_rates_option_3_me": 1,
        "scenario_fertility_rates_option_2_me": 1,
    },
)
def model_explorer_fertility_rates():
    """
    Policy fertility rates for model explorer.
    """
    return if_then_else(
        select_fertility_rates_me() == 1,
        lambda: (
            scenario_fertility_rates_option_1_me()
            .loc[:, "FEMALE", :]
            .reset_coords(drop=True)
            - historical_fertility_rates_2015_2020()
            .loc[:, "FEMALE", :]
            .reset_coords(drop=True)
        )
        / (final_year_model_explorer() - 2020),
        lambda: if_then_else(
            select_fertility_rates_me() == 2,
            lambda: (
                scenario_fertility_rates_option_2_me()
                .loc[:, "FEMALE", :]
                .reset_coords(drop=True)
                - historical_fertility_rates_2015_2020()
                .loc[:, "FEMALE", :]
                .reset_coords(drop=True)
            )
            / (final_year_model_explorer() - 2020),
            lambda: if_then_else(
                select_fertility_rates_me() == 3,
                lambda: (
                    scenario_fertility_rates_option_3_me()
                    .loc[:, "FEMALE", :]
                    .reset_coords(drop=True)
                    - historical_fertility_rates_2015_2020()
                    .loc[:, "FEMALE", :]
                    .reset_coords(drop=True)
                )
                / (final_year_model_explorer() - 2020),
                lambda: xr.DataArray(
                    0,
                    {
                        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                        "FERTILITY_AGES_I": _subscript_dict["FERTILITY_AGES_I"],
                    },
                    ["REGIONS_35_I", "FERTILITY_AGES_I"],
                ),
            ),
        ),
    ).expand_dims({"SEX_I": ["FEMALE"]}, 1)


@component.add(
    name="model_explorer_final_gender_parity_index",
    units="1/Year",
    subscripts=["REGIONS_35_I", "EDUCATIONAL_LEVEL_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_final_gender_parity_index_me": 6,
        "scenario_final_gender_parity_index_option_1_me": 2,
        "initial_gender_parity_index": 6,
        "time": 12,
        "final_year_model_explorer": 12,
        "initial_year_model_explorer": 12,
        "scenario_final_gender_parity_index_option_2_me": 2,
        "scenario_final_gender_parity_index_option_3_me": 2,
    },
)
def model_explorer_final_gender_parity_index():
    """
    Policy gender parity in education for model explorer.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "EDUCATIONAL_LEVEL_I": _subscript_dict["EDUCATIONAL_LEVEL_I"],
        },
        ["REGIONS_35_I", "EDUCATIONAL_LEVEL_I"],
    )
    value.loc[:, ["HIGH_EDUCATION"]] = (
        if_then_else(
            select_final_gender_parity_index_me() == 1,
            lambda: if_then_else(
                time() < initial_year_model_explorer(),
                lambda: xr.DataArray(
                    0,
                    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
                    ["REGIONS_35_I"],
                ),
                lambda: if_then_else(
                    time() < final_year_model_explorer(),
                    lambda: zidz(
                        scenario_final_gender_parity_index_option_1_me()
                        .loc[:, "HIGH_EDUCATION"]
                        .reset_coords(drop=True)
                        - initial_gender_parity_index()
                        .loc[:, "HIGH_EDUCATION"]
                        .reset_coords(drop=True),
                        final_year_model_explorer() - initial_year_model_explorer(),
                    ),
                    lambda: xr.DataArray(
                        0,
                        {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
                        ["REGIONS_35_I"],
                    ),
                ),
            ),
            lambda: if_then_else(
                select_final_gender_parity_index_me() == 2,
                lambda: if_then_else(
                    time() < initial_year_model_explorer(),
                    lambda: xr.DataArray(
                        0,
                        {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
                        ["REGIONS_35_I"],
                    ),
                    lambda: if_then_else(
                        time() < final_year_model_explorer(),
                        lambda: zidz(
                            scenario_final_gender_parity_index_option_2_me()
                            .loc[:, "HIGH_EDUCATION"]
                            .reset_coords(drop=True)
                            - initial_gender_parity_index()
                            .loc[:, "HIGH_EDUCATION"]
                            .reset_coords(drop=True),
                            final_year_model_explorer() - initial_year_model_explorer(),
                        ),
                        lambda: xr.DataArray(
                            0,
                            {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
                            ["REGIONS_35_I"],
                        ),
                    ),
                ),
                lambda: if_then_else(
                    select_final_gender_parity_index_me() == 3,
                    lambda: if_then_else(
                        time() < initial_year_model_explorer(),
                        lambda: xr.DataArray(
                            0,
                            {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
                            ["REGIONS_35_I"],
                        ),
                        lambda: if_then_else(
                            time() < final_year_model_explorer(),
                            lambda: zidz(
                                scenario_final_gender_parity_index_option_3_me()
                                .loc[:, "HIGH_EDUCATION"]
                                .reset_coords(drop=True)
                                - initial_gender_parity_index()
                                .loc[:, "HIGH_EDUCATION"]
                                .reset_coords(drop=True),
                                final_year_model_explorer()
                                - initial_year_model_explorer(),
                            ),
                            lambda: xr.DataArray(
                                0,
                                {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
                                ["REGIONS_35_I"],
                            ),
                        ),
                    ),
                    lambda: xr.DataArray(
                        0,
                        {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
                        ["REGIONS_35_I"],
                    ),
                ),
            ),
        )
        .expand_dims({"EDUCATIONAL_LEVEL_I": ["HIGH_EDUCATION"]}, 1)
        .values
    )
    value.loc[:, ["MEDIUM_EDUCATION"]] = (
        if_then_else(
            select_final_gender_parity_index_me() == 1,
            lambda: if_then_else(
                time() < initial_year_model_explorer(),
                lambda: xr.DataArray(
                    0,
                    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
                    ["REGIONS_35_I"],
                ),
                lambda: if_then_else(
                    time() < final_year_model_explorer(),
                    lambda: zidz(
                        scenario_final_gender_parity_index_option_1_me()
                        .loc[:, "MEDIUM_EDUCATION"]
                        .reset_coords(drop=True)
                        - initial_gender_parity_index()
                        .loc[:, "MEDIUM_EDUCATION"]
                        .reset_coords(drop=True),
                        final_year_model_explorer() - initial_year_model_explorer(),
                    ),
                    lambda: xr.DataArray(
                        0,
                        {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
                        ["REGIONS_35_I"],
                    ),
                ),
            ),
            lambda: if_then_else(
                select_final_gender_parity_index_me() == 2,
                lambda: if_then_else(
                    time() < initial_year_model_explorer(),
                    lambda: xr.DataArray(
                        0,
                        {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
                        ["REGIONS_35_I"],
                    ),
                    lambda: if_then_else(
                        time() < final_year_model_explorer(),
                        lambda: zidz(
                            scenario_final_gender_parity_index_option_2_me()
                            .loc[:, "MEDIUM_EDUCATION"]
                            .reset_coords(drop=True)
                            - initial_gender_parity_index()
                            .loc[:, "MEDIUM_EDUCATION"]
                            .reset_coords(drop=True),
                            final_year_model_explorer() - initial_year_model_explorer(),
                        ),
                        lambda: xr.DataArray(
                            0,
                            {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
                            ["REGIONS_35_I"],
                        ),
                    ),
                ),
                lambda: if_then_else(
                    select_final_gender_parity_index_me() == 3,
                    lambda: if_then_else(
                        time() < initial_year_model_explorer(),
                        lambda: xr.DataArray(
                            0,
                            {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
                            ["REGIONS_35_I"],
                        ),
                        lambda: if_then_else(
                            time() < final_year_model_explorer(),
                            lambda: zidz(
                                scenario_final_gender_parity_index_option_3_me()
                                .loc[:, "MEDIUM_EDUCATION"]
                                .reset_coords(drop=True)
                                - initial_gender_parity_index()
                                .loc[:, "MEDIUM_EDUCATION"]
                                .reset_coords(drop=True),
                                final_year_model_explorer()
                                - initial_year_model_explorer(),
                            ),
                            lambda: xr.DataArray(
                                0,
                                {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
                                ["REGIONS_35_I"],
                            ),
                        ),
                    ),
                    lambda: xr.DataArray(
                        0,
                        {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
                        ["REGIONS_35_I"],
                    ),
                ),
            ),
        )
        .expand_dims({"EDUCATIONAL_LEVEL_I": ["MEDIUM_EDUCATION"]}, 1)
        .values
    )
    return value


@component.add(
    name="model_explorer_forestry_self_sufficiency",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_forestry_self_sufficiency": 3,
        "time": 6,
        "initial_year_model_explorer": 6,
        "final_year_model_explorer": 6,
        "scenario_forestry_self_sufficiency_option_1_me": 1,
        "scenario_forestry_self_sufficiency_option_2_me": 1,
        "scenario_forestry_self_sufficiency_option_3_me": 1,
    },
)
def model_explorer_forestry_self_sufficiency():
    """
    Policy Forestry self sufficiency policy for model explorer.
    """
    return if_then_else(
        np.logical_and(
            select_forestry_self_sufficiency() == 1,
            np.logical_and(
                time() > initial_year_model_explorer(),
                time() <= final_year_model_explorer(),
            ),
        ),
        lambda: scenario_forestry_self_sufficiency_option_1_me()
        / (final_year_model_explorer() - initial_year_model_explorer()),
        lambda: if_then_else(
            np.logical_and(
                select_forestry_self_sufficiency() == 2,
                np.logical_and(
                    time() > initial_year_model_explorer(),
                    time() <= final_year_model_explorer(),
                ),
            ),
            lambda: scenario_forestry_self_sufficiency_option_2_me()
            / (final_year_model_explorer() - initial_year_model_explorer()),
            lambda: if_then_else(
                np.logical_and(
                    select_forestry_self_sufficiency() == 3,
                    np.logical_and(
                        time() > initial_year_model_explorer(),
                        time() <= final_year_model_explorer(),
                    ),
                ),
                lambda: scenario_forestry_self_sufficiency_option_3_me()
                / (final_year_model_explorer() - initial_year_model_explorer()),
                lambda: xr.DataArray(
                    0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
                ),
            ),
        ),
    )


@component.add(
    name="model_explorer_government_to_GDP_objetive",
    units="1/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "initial_year_model_explorer": 1,
        "scenario_goverment_option_2_me": 1,
        "scenario_goverment_option_1_me": 1,
        "scenario_goverment_option_3_me": 1,
        "select_government_budget_balance_to_gdp_objective_target_me": 3,
    },
)
def model_explorer_government_to_gdp_objetive():
    """
    Policy government deficit of surplus for model explorer.
    """
    return if_then_else(
        time() < initial_year_model_explorer(),
        lambda: xr.DataArray(
            0, {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]}, ["REGIONS_35_I"]
        ),
        lambda: if_then_else(
            select_government_budget_balance_to_gdp_objective_target_me() == 1,
            lambda: scenario_goverment_option_1_me(),
            lambda: if_then_else(
                select_government_budget_balance_to_gdp_objective_target_me() == 2,
                lambda: scenario_goverment_option_2_me(),
                lambda: if_then_else(
                    select_government_budget_balance_to_gdp_objective_target_me() == 3,
                    lambda: scenario_goverment_option_3_me(),
                    lambda: xr.DataArray(
                        0,
                        {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
                        ["REGIONS_35_I"],
                    ),
                ),
            ),
        ),
    )


@component.add(
    name="model_explorer_land_protection",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LANDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_land_protection_by_policy_me": 3,
        "time": 6,
        "initial_year_model_explorer": 3,
        "final_year_model_explorer": 3,
        "scenario_land_protection_by_policy_option_1_me": 1,
        "scenario_land_protection_by_policy_option_3_me": 1,
        "scenario_land_protection_by_policy_option_2_me": 1,
    },
)
def model_explorer_land_protection():
    """
    Policy Protection of Primary Forest Policy for model explorer.
    """
    return if_then_else(
        np.logical_and(
            select_land_protection_by_policy_me() == 1,
            np.logical_and(
                time() > initial_year_model_explorer(),
                time() < final_year_model_explorer(),
            ),
        ),
        lambda: scenario_land_protection_by_policy_option_1_me(),
        lambda: if_then_else(
            np.logical_and(
                select_land_protection_by_policy_me() == 2,
                np.logical_and(
                    time() > initial_year_model_explorer(),
                    time() < final_year_model_explorer(),
                ),
            ),
            lambda: scenario_land_protection_by_policy_option_2_me(),
            lambda: if_then_else(
                np.logical_and(
                    select_land_protection_by_policy_me() == 3,
                    np.logical_and(
                        time() > initial_year_model_explorer(),
                        time() < final_year_model_explorer(),
                    ),
                ),
                lambda: scenario_land_protection_by_policy_option_3_me(),
                lambda: xr.DataArray(
                    0,
                    {
                        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                        "LANDS_I": _subscript_dict["LANDS_I"],
                    },
                    ["REGIONS_9_I", "LANDS_I"],
                ),
            ),
        ),
    )


@component.add(
    name="model_explorer_manure_management_system",
    units="kg/(number_animals*Year)",
    subscripts=["ANIMALS_TYPES_I", "REGIONS_9_I", "MANURE_MANAGEMENT_SYSTEM_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_manure_management_system_me": 12,
        "dairy_cattle_manure_system": 3,
        "methane_conversion_factor_by_system": 24,
        "time": 24,
        "scenario_manure_management_system_option_1_me": 4,
        "final_year_model_explorer": 12,
        "initial_year_model_explorer": 12,
        "scenario_manure_management_system_option_3_me": 4,
        "scenario_manure_management_system_option_2_me": 4,
        "other_cattle_manure_system": 3,
        "buffalo_manure_system": 3,
        "swine_manure_system": 3,
    },
)
def model_explorer_manure_management_system():
    """
    Policy manure management system policy for model explorer.
    """
    value = xr.DataArray(
        np.nan,
        {
            "ANIMALS_TYPES_I": _subscript_dict["ANIMALS_TYPES_I"],
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "MANURE_MANAGEMENT_SYSTEM_I": _subscript_dict["MANURE_MANAGEMENT_SYSTEM_I"],
        },
        ["ANIMALS_TYPES_I", "REGIONS_9_I", "MANURE_MANAGEMENT_SYSTEM_I"],
    )
    value.loc[["DAIRY_CATTLE"], :, :] = (
        if_then_else(
            select_manure_management_system_me() == 1,
            lambda: if_then_else(
                np.logical_and(
                    time() > initial_year_model_explorer(),
                    time() <= final_year_model_explorer(),
                ),
                lambda: methane_conversion_factor_by_system()
                * scenario_manure_management_system_option_1_me()
                .loc["DAIRY_CATTLE", :, :]
                .reset_coords(drop=True),
                lambda: methane_conversion_factor_by_system()
                * dairy_cattle_manure_system(),
            ),
            lambda: if_then_else(
                select_manure_management_system_me() == 2,
                lambda: if_then_else(
                    np.logical_and(
                        time() > initial_year_model_explorer(),
                        time() <= final_year_model_explorer(),
                    ),
                    lambda: methane_conversion_factor_by_system()
                    * scenario_manure_management_system_option_2_me()
                    .loc["DAIRY_CATTLE", :, :]
                    .reset_coords(drop=True),
                    lambda: methane_conversion_factor_by_system()
                    * dairy_cattle_manure_system(),
                ),
                lambda: if_then_else(
                    select_manure_management_system_me() == 3,
                    lambda: if_then_else(
                        np.logical_and(
                            time() > initial_year_model_explorer(),
                            time() <= final_year_model_explorer(),
                        ),
                        lambda: methane_conversion_factor_by_system()
                        * scenario_manure_management_system_option_3_me()
                        .loc["DAIRY_CATTLE", :, :]
                        .reset_coords(drop=True),
                        lambda: methane_conversion_factor_by_system()
                        * dairy_cattle_manure_system(),
                    ),
                    lambda: xr.DataArray(
                        0,
                        {
                            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                            "MANURE_MANAGEMENT_SYSTEM_I": _subscript_dict[
                                "MANURE_MANAGEMENT_SYSTEM_I"
                            ],
                        },
                        ["REGIONS_9_I", "MANURE_MANAGEMENT_SYSTEM_I"],
                    ),
                ),
            ),
        )
        .expand_dims({"ANIMALS_TYPES_I": ["DAIRY_CATTLE"]}, 0)
        .values
    )
    value.loc[["OTHER_CATTLE"], :, :] = (
        if_then_else(
            select_manure_management_system_me() == 1,
            lambda: if_then_else(
                np.logical_and(
                    time() > initial_year_model_explorer(),
                    time() <= final_year_model_explorer(),
                ),
                lambda: methane_conversion_factor_by_system()
                * scenario_manure_management_system_option_1_me()
                .loc["OTHER_CATTLE", :, :]
                .reset_coords(drop=True),
                lambda: methane_conversion_factor_by_system()
                * other_cattle_manure_system(),
            ),
            lambda: if_then_else(
                select_manure_management_system_me() == 2,
                lambda: if_then_else(
                    np.logical_and(
                        time() > initial_year_model_explorer(),
                        time() <= final_year_model_explorer(),
                    ),
                    lambda: methane_conversion_factor_by_system()
                    * scenario_manure_management_system_option_2_me()
                    .loc["OTHER_CATTLE", :, :]
                    .reset_coords(drop=True),
                    lambda: methane_conversion_factor_by_system()
                    * other_cattle_manure_system(),
                ),
                lambda: if_then_else(
                    select_manure_management_system_me() == 3,
                    lambda: if_then_else(
                        np.logical_and(
                            time() > initial_year_model_explorer(),
                            time() <= final_year_model_explorer(),
                        ),
                        lambda: methane_conversion_factor_by_system()
                        * scenario_manure_management_system_option_3_me()
                        .loc["OTHER_CATTLE", :, :]
                        .reset_coords(drop=True),
                        lambda: methane_conversion_factor_by_system()
                        * other_cattle_manure_system(),
                    ),
                    lambda: xr.DataArray(
                        0,
                        {
                            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                            "MANURE_MANAGEMENT_SYSTEM_I": _subscript_dict[
                                "MANURE_MANAGEMENT_SYSTEM_I"
                            ],
                        },
                        ["REGIONS_9_I", "MANURE_MANAGEMENT_SYSTEM_I"],
                    ),
                ),
            ),
        )
        .expand_dims({"ANIMALS_TYPES_I": ["OTHER_CATTLE"]}, 0)
        .values
    )
    value.loc[["BUFFALO"], :, :] = (
        if_then_else(
            select_manure_management_system_me() == 1,
            lambda: if_then_else(
                np.logical_and(
                    time() > initial_year_model_explorer(),
                    time() <= final_year_model_explorer(),
                ),
                lambda: methane_conversion_factor_by_system()
                * scenario_manure_management_system_option_1_me()
                .loc["BUFFALO", :, :]
                .reset_coords(drop=True),
                lambda: methane_conversion_factor_by_system() * buffalo_manure_system(),
            ),
            lambda: if_then_else(
                select_manure_management_system_me() == 2,
                lambda: if_then_else(
                    np.logical_and(
                        time() > initial_year_model_explorer(),
                        time() <= final_year_model_explorer(),
                    ),
                    lambda: methane_conversion_factor_by_system()
                    * scenario_manure_management_system_option_2_me()
                    .loc["BUFFALO", :, :]
                    .reset_coords(drop=True),
                    lambda: methane_conversion_factor_by_system()
                    * buffalo_manure_system(),
                ),
                lambda: if_then_else(
                    select_manure_management_system_me() == 3,
                    lambda: if_then_else(
                        np.logical_and(
                            time() > initial_year_model_explorer(),
                            time() <= final_year_model_explorer(),
                        ),
                        lambda: methane_conversion_factor_by_system()
                        * scenario_manure_management_system_option_3_me()
                        .loc["BUFFALO", :, :]
                        .reset_coords(drop=True),
                        lambda: methane_conversion_factor_by_system()
                        * buffalo_manure_system(),
                    ),
                    lambda: xr.DataArray(
                        0,
                        {
                            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                            "MANURE_MANAGEMENT_SYSTEM_I": _subscript_dict[
                                "MANURE_MANAGEMENT_SYSTEM_I"
                            ],
                        },
                        ["REGIONS_9_I", "MANURE_MANAGEMENT_SYSTEM_I"],
                    ),
                ),
            ),
        )
        .expand_dims({"ANIMALS_TYPES_I": ["BUFFALO"]}, 0)
        .values
    )
    value.loc[["SWINE"], :, :] = (
        if_then_else(
            select_manure_management_system_me() == 1,
            lambda: if_then_else(
                np.logical_and(
                    time() > initial_year_model_explorer(),
                    time() <= final_year_model_explorer(),
                ),
                lambda: methane_conversion_factor_by_system()
                * scenario_manure_management_system_option_1_me()
                .loc["SWINE", :, :]
                .reset_coords(drop=True),
                lambda: methane_conversion_factor_by_system() * swine_manure_system(),
            ),
            lambda: if_then_else(
                select_manure_management_system_me() == 2,
                lambda: if_then_else(
                    np.logical_and(
                        time() > initial_year_model_explorer(),
                        time() <= final_year_model_explorer(),
                    ),
                    lambda: methane_conversion_factor_by_system()
                    * scenario_manure_management_system_option_2_me()
                    .loc["SWINE", :, :]
                    .reset_coords(drop=True),
                    lambda: methane_conversion_factor_by_system()
                    * swine_manure_system(),
                ),
                lambda: if_then_else(
                    select_manure_management_system_me() == 3,
                    lambda: if_then_else(
                        np.logical_and(
                            time() > initial_year_model_explorer(),
                            time() <= final_year_model_explorer(),
                        ),
                        lambda: methane_conversion_factor_by_system()
                        * scenario_manure_management_system_option_3_me()
                        .loc["SWINE", :, :]
                        .reset_coords(drop=True),
                        lambda: methane_conversion_factor_by_system()
                        * swine_manure_system(),
                    ),
                    lambda: xr.DataArray(
                        0,
                        {
                            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                            "MANURE_MANAGEMENT_SYSTEM_I": _subscript_dict[
                                "MANURE_MANAGEMENT_SYSTEM_I"
                            ],
                        },
                        ["REGIONS_9_I", "MANURE_MANAGEMENT_SYSTEM_I"],
                    ),
                ),
            ),
        )
        .expand_dims({"ANIMALS_TYPES_I": ["SWINE"]}, 0)
        .values
    )
    return value


@component.add(
    name="model_explorer_objective_diets",
    units="1/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 2,
        "initial_year_model_explorer": 2,
        "final_year_model_explorer": 2,
        "scenario_share_diets_me": 1,
    },
)
def model_explorer_objective_diets():
    """
    Policy diets for model explorer.
    """
    return if_then_else(
        np.logical_or(
            time() < initial_year_model_explorer(), time() > final_year_model_explorer()
        ),
        lambda: 0,
        lambda: scenario_share_diets_me()
        / (final_year_model_explorer() - initial_year_model_explorer()),
    )


@component.add(
    name="model_explorer_oil_resource",
    units="bbl",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_oil_resource_me": 3,
        "scenario_oil_resource_option_1_me": 1,
        "scenario_oil_resource_option_2_me": 1,
        "scenario_oil_resource_option_3_me": 1,
    },
)
def model_explorer_oil_resource():
    """
    Selection of different resource estimation in the model explorer.
    """
    return if_then_else(
        select_oil_resource_me() == 1,
        lambda: scenario_oil_resource_option_1_me(),
        lambda: if_then_else(
            select_oil_resource_me() == 2,
            lambda: scenario_oil_resource_option_2_me(),
            lambda: if_then_else(
                select_oil_resource_me() == 3,
                lambda: scenario_oil_resource_option_3_me(),
                lambda: 1,
            ),
        ),
    )


@component.add(
    name="model_explorer_passenger_transport_demand_modal_share",
    units="DMNL",
    subscripts=[
        "REGIONS_35_I",
        "TRANSPORT_POWER_TRAIN_I",
        "PASSENGERS_TRANSPORT_MODE_I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 4,
        "initial_year_model_explorer": 7,
        "initial_passenger_transport_demand_share": 7,
        "select_passenger_transport_demand_modal_share_me": 3,
        "scenario_passenger_transport_demand_modal_share_option_3_me": 1,
        "scenario_passenger_transport_demand_modal_share_option_2_me": 1,
        "scenario_passenger_transport_demand_modal_share_option_1_me": 1,
        "final_year_model_explorer": 6,
    },
)
def model_explorer_passenger_transport_demand_modal_share():
    """
    Policy government deficit of surplus for model explorer.
    """
    return if_then_else(
        time() < initial_year_model_explorer(),
        lambda: initial_passenger_transport_demand_share(),
        lambda: if_then_else(
            select_passenger_transport_demand_modal_share_me() == 1,
            lambda: initial_passenger_transport_demand_share()
            + ramp(
                __data["time"],
                (
                    scenario_passenger_transport_demand_modal_share_option_1_me()
                    - initial_passenger_transport_demand_share()
                )
                / (final_year_model_explorer() - initial_year_model_explorer()),
                initial_year_model_explorer(),
                final_year_model_explorer(),
            ),
            lambda: if_then_else(
                select_passenger_transport_demand_modal_share_me() == 2,
                lambda: initial_passenger_transport_demand_share()
                + ramp(
                    __data["time"],
                    (
                        scenario_passenger_transport_demand_modal_share_option_2_me()
                        - initial_passenger_transport_demand_share()
                    )
                    / (final_year_model_explorer() - initial_year_model_explorer()),
                    initial_year_model_explorer(),
                    final_year_model_explorer(),
                ),
                lambda: if_then_else(
                    select_passenger_transport_demand_modal_share_me() == 3,
                    lambda: initial_passenger_transport_demand_share()
                    + ramp(
                        __data["time"],
                        (
                            scenario_passenger_transport_demand_modal_share_option_3_me()
                            - initial_passenger_transport_demand_share()
                        )
                        / (final_year_model_explorer() - initial_year_model_explorer()),
                        initial_year_model_explorer(),
                        final_year_model_explorer(),
                    ),
                    lambda: xr.DataArray(
                        1,
                        {
                            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                            "TRANSPORT_POWER_TRAIN_I": _subscript_dict[
                                "TRANSPORT_POWER_TRAIN_I"
                            ],
                            "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict[
                                "PASSENGERS_TRANSPORT_MODE_I"
                            ],
                        },
                        [
                            "REGIONS_35_I",
                            "TRANSPORT_POWER_TRAIN_I",
                            "PASSENGERS_TRANSPORT_MODE_I",
                        ],
                    ),
                ),
            ),
        ),
    )


@component.add(
    name="model_explorer_percentage_FE_liquid_substituted_by_H2_synthetic_liquid",
    units="DMML",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_percentage_fe_liquid_substituted_by_h2_synthetic_liquid_me": 3,
        "scenario_objective_percentage_fe_liquid_substituted_by_h2_synthetic_liquid_option_1_me": 1,
        "scenario_objective_percentage_fe_liquid_substituted_by_h2_synthetic_liquid_option_3_me": 3,
        "scenario_objective_percentage_fe_liquid_substituted_by_h2_synthetic_liquid_option_2_me": 3,
        "time": 6,
        "final_year_model_explorer": 6,
        "initial_year_model_explorer": 8,
    },
)
def model_explorer_percentage_fe_liquid_substituted_by_h2_synthetic_liquid():
    """
    Policy share of FE gas substituted by H2 gases based fuel for model explorer.
    """
    return if_then_else(
        select_percentage_fe_liquid_substituted_by_h2_synthetic_liquid_me() == 1,
        lambda: scenario_objective_percentage_fe_liquid_substituted_by_h2_synthetic_liquid_option_1_me(),
        lambda: if_then_else(
            select_percentage_fe_liquid_substituted_by_h2_synthetic_liquid_me() == 2,
            lambda: if_then_else(
                time() < initial_year_model_explorer(),
                lambda: xr.DataArray(
                    0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
                ),
                lambda: if_then_else(
                    time() < final_year_model_explorer(),
                    lambda: -scenario_objective_percentage_fe_liquid_substituted_by_h2_synthetic_liquid_option_2_me()
                    * initial_year_model_explorer()
                    / (final_year_model_explorer() - initial_year_model_explorer())
                    + time()
                    * zidz(
                        scenario_objective_percentage_fe_liquid_substituted_by_h2_synthetic_liquid_option_2_me(),
                        final_year_model_explorer() - initial_year_model_explorer(),
                    ),
                    lambda: scenario_objective_percentage_fe_liquid_substituted_by_h2_synthetic_liquid_option_2_me(),
                ),
            ),
            lambda: if_then_else(
                select_percentage_fe_liquid_substituted_by_h2_synthetic_liquid_me()
                == 3,
                lambda: if_then_else(
                    time() < initial_year_model_explorer(),
                    lambda: xr.DataArray(
                        0,
                        {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
                        ["REGIONS_9_I"],
                    ),
                    lambda: if_then_else(
                        time() < final_year_model_explorer(),
                        lambda: -scenario_objective_percentage_fe_liquid_substituted_by_h2_synthetic_liquid_option_3_me()
                        * initial_year_model_explorer()
                        / (final_year_model_explorer() - initial_year_model_explorer())
                        + time()
                        * zidz(
                            scenario_objective_percentage_fe_liquid_substituted_by_h2_synthetic_liquid_option_3_me(),
                            final_year_model_explorer() - initial_year_model_explorer(),
                        ),
                        lambda: scenario_objective_percentage_fe_liquid_substituted_by_h2_synthetic_liquid_option_3_me(),
                    ),
                ),
                lambda: xr.DataArray(
                    0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
                ),
            ),
        ),
    )


@component.add(
    name="model_explorer_protra_capacity_expansion",
    units="DMNL",
    subscripts=["REGIONS_9_I", "NRG_PROTRA_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_protra_capacity_expansion_priorities_vector_me": 3,
        "scenario_protra_expansion_option_1_me": 1,
        "scenario_protra_expansion_option_3_me": 1,
        "scenario_protra_expansion_option_2_me": 1,
    },
)
def model_explorer_protra_capacity_expansion():
    """
    Policy government deficit of surplus for model explorer.
    """
    return if_then_else(
        select_protra_capacity_expansion_priorities_vector_me() == 1,
        lambda: scenario_protra_expansion_option_1_me(),
        lambda: if_then_else(
            select_protra_capacity_expansion_priorities_vector_me() == 2,
            lambda: scenario_protra_expansion_option_2_me(),
            lambda: if_then_else(
                select_protra_capacity_expansion_priorities_vector_me() == 3,
                lambda: scenario_protra_expansion_option_3_me(),
                lambda: xr.DataArray(
                    1,
                    {
                        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                        "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
                    },
                    ["REGIONS_9_I", "NRG_PROTRA_I"],
                ),
            ),
        ),
    )


@component.add(
    name="model_explorer_RCP_GHG_emissions",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"select_rcp_ghg_emissions_me": 1},
)
def model_explorer_rcp_ghg_emissions():
    """
    Hypothesis RCP for setting the GHG emissions of those gases not being modelled endogenously for model explorer.
    """
    return select_rcp_ghg_emissions_me()


@component.add(
    name="model_explorer_reduction_passenger_transport_demand",
    units="DMNL",
    subscripts=["TRANSPORT_POWER_TRAIN_I", "PASSENGERS_TRANSPORT_MODE_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 4,
        "initial_year_model_explorer": 7,
        "scenario_passenger_transport_demand_option_3_me": 1,
        "select_reduction_passenger_transport_demand_me": 3,
        "scenario_passenger_transport_demand_option_1_me": 1,
        "scenario_passenger_transport_demand_option_2_me": 1,
        "final_year_model_explorer": 6,
    },
)
def model_explorer_reduction_passenger_transport_demand():
    """
    Policy government deficit of surplus for model explorer.
    """
    return if_then_else(
        time() < initial_year_model_explorer(),
        lambda: xr.DataArray(
            1,
            {
                "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
                "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict[
                    "PASSENGERS_TRANSPORT_MODE_I"
                ],
            },
            ["TRANSPORT_POWER_TRAIN_I", "PASSENGERS_TRANSPORT_MODE_I"],
        ),
        lambda: if_then_else(
            select_reduction_passenger_transport_demand_me() == 1,
            lambda: 1
            + ramp(
                __data["time"],
                (scenario_passenger_transport_demand_option_1_me() - 1)
                / (final_year_model_explorer() - initial_year_model_explorer()),
                initial_year_model_explorer(),
                final_year_model_explorer(),
            ),
            lambda: if_then_else(
                select_reduction_passenger_transport_demand_me() == 2,
                lambda: 1
                + ramp(
                    __data["time"],
                    (scenario_passenger_transport_demand_option_2_me() - 1)
                    / (final_year_model_explorer() - initial_year_model_explorer()),
                    initial_year_model_explorer(),
                    final_year_model_explorer(),
                ),
                lambda: if_then_else(
                    select_reduction_passenger_transport_demand_me() == 3,
                    lambda: 1
                    + ramp(
                        __data["time"],
                        (scenario_passenger_transport_demand_option_3_me() - 1)
                        / (final_year_model_explorer() - initial_year_model_explorer()),
                        initial_year_model_explorer(),
                        final_year_model_explorer(),
                    ),
                    lambda: xr.DataArray(
                        1,
                        {
                            "TRANSPORT_POWER_TRAIN_I": _subscript_dict[
                                "TRANSPORT_POWER_TRAIN_I"
                            ],
                            "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict[
                                "PASSENGERS_TRANSPORT_MODE_I"
                            ],
                        },
                        ["TRANSPORT_POWER_TRAIN_I", "PASSENGERS_TRANSPORT_MODE_I"],
                    ),
                ),
            ),
        ),
    )


@component.add(
    name="model_explorer_target_share_bioenergy_in_fossil_liquids_and_gases",
    units="1/Year",
    subscripts=["REGIONS_9_I", "NRG_PRO_I", "NRG_COMMODITIES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_target_share_bioenergy_in_fossil_liquids_and_gases_me": 12,
        "scenario_target_share_bioenergy_in_fossil_liquids_and_gases_option_1_me": 4,
        "scenario_target_share_bioenergy_in_fossil_liquids_and_gases_option_3_me": 4,
        "scenario_target_share_bioenergy_in_fossil_liquids_and_gases_option_2_me": 4,
        "time": 16,
        "protra_input_shares_empiric": 8,
        "final_year_model_explorer": 16,
        "initial_year_model_explorer": 16,
    },
)
def model_explorer_target_share_bioenergy_in_fossil_liquids_and_gases():
    """
    Policy share of bioenergy fossil liquids and gases for model explorer.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "NRG_PRO_I": _subscript_dict["NRG_PRO_I"],
            "NRG_COMMODITIES_I": _subscript_dict["NRG_COMMODITIES_I"],
        },
        ["REGIONS_9_I", "NRG_PRO_I", "NRG_COMMODITIES_I"],
    )
    value.loc[:, _subscript_dict["PROTRA_TI_GAS_I"], ["TI_gas_bio"]] = (
        if_then_else(
            select_target_share_bioenergy_in_fossil_liquids_and_gases_me() == 1,
            lambda: scenario_target_share_bioenergy_in_fossil_liquids_and_gases_option_1_me().expand_dims(
                {"PROTRA_TI_GAS_I": _subscript_dict["PROTRA_TI_GAS_I"]}, 1
            ),
            lambda: if_then_else(
                select_target_share_bioenergy_in_fossil_liquids_and_gases_me() == 2,
                lambda: if_then_else(
                    time() < initial_year_model_explorer(),
                    lambda: xr.DataArray(
                        0,
                        {
                            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                            "PROTRA_TI_GAS_I": _subscript_dict["PROTRA_TI_GAS_I"],
                        },
                        ["REGIONS_9_I", "PROTRA_TI_GAS_I"],
                    ),
                    lambda: if_then_else(
                        time() < final_year_model_explorer(),
                        lambda: zidz(
                            scenario_target_share_bioenergy_in_fossil_liquids_and_gases_option_2_me()
                            - protra_input_shares_empiric()
                            .loc[:, _subscript_dict["PROTRA_TI_GAS_I"], "TI_gas_bio"]
                            .reset_coords(drop=True)
                            .rename({"NRG_PROTRA_I": "PROTRA_TI_GAS_I"}),
                            final_year_model_explorer() - initial_year_model_explorer(),
                        ),
                        lambda: xr.DataArray(
                            0,
                            {
                                "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                                "PROTRA_TI_GAS_I": _subscript_dict["PROTRA_TI_GAS_I"],
                            },
                            ["REGIONS_9_I", "PROTRA_TI_GAS_I"],
                        ),
                    ),
                ),
                lambda: if_then_else(
                    select_target_share_bioenergy_in_fossil_liquids_and_gases_me() == 3,
                    lambda: if_then_else(
                        time() < initial_year_model_explorer(),
                        lambda: xr.DataArray(
                            0,
                            {
                                "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                                "PROTRA_TI_GAS_I": _subscript_dict["PROTRA_TI_GAS_I"],
                            },
                            ["REGIONS_9_I", "PROTRA_TI_GAS_I"],
                        ),
                        lambda: if_then_else(
                            time() < final_year_model_explorer(),
                            lambda: zidz(
                                scenario_target_share_bioenergy_in_fossil_liquids_and_gases_option_3_me()
                                - protra_input_shares_empiric()
                                .loc[
                                    :, _subscript_dict["PROTRA_TI_GAS_I"], "TI_gas_bio"
                                ]
                                .reset_coords(drop=True)
                                .rename({"NRG_PROTRA_I": "PROTRA_TI_GAS_I"}),
                                final_year_model_explorer()
                                - initial_year_model_explorer(),
                            ),
                            lambda: xr.DataArray(
                                0,
                                {
                                    "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                                    "PROTRA_TI_GAS_I": _subscript_dict[
                                        "PROTRA_TI_GAS_I"
                                    ],
                                },
                                ["REGIONS_9_I", "PROTRA_TI_GAS_I"],
                            ),
                        ),
                    ),
                    lambda: xr.DataArray(
                        0,
                        {
                            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                            "PROTRA_TI_GAS_I": _subscript_dict["PROTRA_TI_GAS_I"],
                        },
                        ["REGIONS_9_I", "PROTRA_TI_GAS_I"],
                    ),
                ),
            ),
        )
        .expand_dims({"NRG_COMMODITIES_I": ["TI_gas_bio"]}, 2)
        .values
    )
    value.loc[:, _subscript_dict["PROTRA_TI_GAS_I"], ["TI_gas_fossil"]] = (
        if_then_else(
            select_target_share_bioenergy_in_fossil_liquids_and_gases_me() == 1,
            lambda: scenario_target_share_bioenergy_in_fossil_liquids_and_gases_option_1_me().expand_dims(
                {"PROTRA_TI_GAS_I": _subscript_dict["PROTRA_TI_GAS_I"]}, 1
            ),
            lambda: if_then_else(
                select_target_share_bioenergy_in_fossil_liquids_and_gases_me() == 2,
                lambda: if_then_else(
                    time() < initial_year_model_explorer(),
                    lambda: xr.DataArray(
                        0,
                        {
                            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                            "PROTRA_TI_GAS_I": _subscript_dict["PROTRA_TI_GAS_I"],
                        },
                        ["REGIONS_9_I", "PROTRA_TI_GAS_I"],
                    ),
                    lambda: if_then_else(
                        time() < final_year_model_explorer(),
                        lambda: zidz(
                            (
                                1
                                - scenario_target_share_bioenergy_in_fossil_liquids_and_gases_option_2_me()
                            )
                            - protra_input_shares_empiric()
                            .loc[:, _subscript_dict["PROTRA_TI_GAS_I"], "TI_gas_fossil"]
                            .reset_coords(drop=True)
                            .rename({"NRG_PROTRA_I": "PROTRA_TI_GAS_I"}),
                            final_year_model_explorer() - initial_year_model_explorer(),
                        ),
                        lambda: xr.DataArray(
                            0,
                            {
                                "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                                "PROTRA_TI_GAS_I": _subscript_dict["PROTRA_TI_GAS_I"],
                            },
                            ["REGIONS_9_I", "PROTRA_TI_GAS_I"],
                        ),
                    ),
                ),
                lambda: if_then_else(
                    select_target_share_bioenergy_in_fossil_liquids_and_gases_me() == 3,
                    lambda: if_then_else(
                        time() < initial_year_model_explorer(),
                        lambda: xr.DataArray(
                            0,
                            {
                                "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                                "PROTRA_TI_GAS_I": _subscript_dict["PROTRA_TI_GAS_I"],
                            },
                            ["REGIONS_9_I", "PROTRA_TI_GAS_I"],
                        ),
                        lambda: if_then_else(
                            time() < final_year_model_explorer(),
                            lambda: zidz(
                                (
                                    1
                                    - scenario_target_share_bioenergy_in_fossil_liquids_and_gases_option_3_me()
                                )
                                - protra_input_shares_empiric()
                                .loc[
                                    :,
                                    _subscript_dict["PROTRA_TI_GAS_I"],
                                    "TI_gas_fossil",
                                ]
                                .reset_coords(drop=True)
                                .rename({"NRG_PROTRA_I": "PROTRA_TI_GAS_I"}),
                                final_year_model_explorer()
                                - initial_year_model_explorer(),
                            ),
                            lambda: xr.DataArray(
                                0,
                                {
                                    "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                                    "PROTRA_TI_GAS_I": _subscript_dict[
                                        "PROTRA_TI_GAS_I"
                                    ],
                                },
                                ["REGIONS_9_I", "PROTRA_TI_GAS_I"],
                            ),
                        ),
                    ),
                    lambda: xr.DataArray(
                        0,
                        {
                            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                            "PROTRA_TI_GAS_I": _subscript_dict["PROTRA_TI_GAS_I"],
                        },
                        ["REGIONS_9_I", "PROTRA_TI_GAS_I"],
                    ),
                ),
            ),
        )
        .expand_dims({"NRG_COMMODITIES_I": ["TI_gas_fossil"]}, 2)
        .values
    )
    value.loc[:, _subscript_dict["PROTRA_TI_LIQUIDS_I"], ["TI_liquid_bio"]] = (
        if_then_else(
            select_target_share_bioenergy_in_fossil_liquids_and_gases_me() == 1,
            lambda: scenario_target_share_bioenergy_in_fossil_liquids_and_gases_option_1_me().expand_dims(
                {"PROTRA_TI_LIQUIDS_I": _subscript_dict["PROTRA_TI_LIQUIDS_I"]}, 1
            ),
            lambda: if_then_else(
                select_target_share_bioenergy_in_fossil_liquids_and_gases_me() == 2,
                lambda: if_then_else(
                    time() < initial_year_model_explorer(),
                    lambda: xr.DataArray(
                        0,
                        {
                            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                            "PROTRA_TI_LIQUIDS_I": _subscript_dict[
                                "PROTRA_TI_LIQUIDS_I"
                            ],
                        },
                        ["REGIONS_9_I", "PROTRA_TI_LIQUIDS_I"],
                    ),
                    lambda: if_then_else(
                        time() < final_year_model_explorer(),
                        lambda: zidz(
                            scenario_target_share_bioenergy_in_fossil_liquids_and_gases_option_2_me()
                            - protra_input_shares_empiric()
                            .loc[
                                :,
                                _subscript_dict["PROTRA_TI_LIQUIDS_I"],
                                "TI_liquid_bio",
                            ]
                            .reset_coords(drop=True)
                            .rename({"NRG_PROTRA_I": "PROTRA_TI_LIQUIDS_I"}),
                            final_year_model_explorer() - initial_year_model_explorer(),
                        ),
                        lambda: xr.DataArray(
                            0,
                            {
                                "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                                "PROTRA_TI_LIQUIDS_I": _subscript_dict[
                                    "PROTRA_TI_LIQUIDS_I"
                                ],
                            },
                            ["REGIONS_9_I", "PROTRA_TI_LIQUIDS_I"],
                        ),
                    ),
                ),
                lambda: if_then_else(
                    select_target_share_bioenergy_in_fossil_liquids_and_gases_me() == 3,
                    lambda: if_then_else(
                        time() < initial_year_model_explorer(),
                        lambda: xr.DataArray(
                            0,
                            {
                                "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                                "PROTRA_TI_LIQUIDS_I": _subscript_dict[
                                    "PROTRA_TI_LIQUIDS_I"
                                ],
                            },
                            ["REGIONS_9_I", "PROTRA_TI_LIQUIDS_I"],
                        ),
                        lambda: if_then_else(
                            time() < final_year_model_explorer(),
                            lambda: zidz(
                                scenario_target_share_bioenergy_in_fossil_liquids_and_gases_option_3_me()
                                - protra_input_shares_empiric()
                                .loc[
                                    :,
                                    _subscript_dict["PROTRA_TI_LIQUIDS_I"],
                                    "TI_liquid_bio",
                                ]
                                .reset_coords(drop=True)
                                .rename({"NRG_PROTRA_I": "PROTRA_TI_LIQUIDS_I"}),
                                final_year_model_explorer()
                                - initial_year_model_explorer(),
                            ),
                            lambda: xr.DataArray(
                                0,
                                {
                                    "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                                    "PROTRA_TI_LIQUIDS_I": _subscript_dict[
                                        "PROTRA_TI_LIQUIDS_I"
                                    ],
                                },
                                ["REGIONS_9_I", "PROTRA_TI_LIQUIDS_I"],
                            ),
                        ),
                    ),
                    lambda: xr.DataArray(
                        0,
                        {
                            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                            "PROTRA_TI_LIQUIDS_I": _subscript_dict[
                                "PROTRA_TI_LIQUIDS_I"
                            ],
                        },
                        ["REGIONS_9_I", "PROTRA_TI_LIQUIDS_I"],
                    ),
                ),
            ),
        )
        .expand_dims({"NRG_COMMODITIES_I": ["TI_liquid_bio"]}, 2)
        .values
    )
    value.loc[:, _subscript_dict["PROTRA_TI_LIQUIDS_I"], ["TI_liquid_fossil"]] = (
        if_then_else(
            select_target_share_bioenergy_in_fossil_liquids_and_gases_me() == 1,
            lambda: scenario_target_share_bioenergy_in_fossil_liquids_and_gases_option_1_me().expand_dims(
                {"PROTRA_TI_LIQUIDS_I": _subscript_dict["PROTRA_TI_LIQUIDS_I"]}, 1
            ),
            lambda: if_then_else(
                select_target_share_bioenergy_in_fossil_liquids_and_gases_me() == 2,
                lambda: if_then_else(
                    time() < initial_year_model_explorer(),
                    lambda: xr.DataArray(
                        0,
                        {
                            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                            "PROTRA_TI_LIQUIDS_I": _subscript_dict[
                                "PROTRA_TI_LIQUIDS_I"
                            ],
                        },
                        ["REGIONS_9_I", "PROTRA_TI_LIQUIDS_I"],
                    ),
                    lambda: if_then_else(
                        time() < final_year_model_explorer(),
                        lambda: zidz(
                            (
                                1
                                - scenario_target_share_bioenergy_in_fossil_liquids_and_gases_option_2_me()
                            )
                            - protra_input_shares_empiric()
                            .loc[
                                :,
                                _subscript_dict["PROTRA_TI_LIQUIDS_I"],
                                "TI_liquid_fossil",
                            ]
                            .reset_coords(drop=True)
                            .rename({"NRG_PROTRA_I": "PROTRA_TI_LIQUIDS_I"}),
                            final_year_model_explorer() - initial_year_model_explorer(),
                        ),
                        lambda: xr.DataArray(
                            0,
                            {
                                "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                                "PROTRA_TI_LIQUIDS_I": _subscript_dict[
                                    "PROTRA_TI_LIQUIDS_I"
                                ],
                            },
                            ["REGIONS_9_I", "PROTRA_TI_LIQUIDS_I"],
                        ),
                    ),
                ),
                lambda: if_then_else(
                    select_target_share_bioenergy_in_fossil_liquids_and_gases_me() == 3,
                    lambda: if_then_else(
                        time() < initial_year_model_explorer(),
                        lambda: xr.DataArray(
                            0,
                            {
                                "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                                "PROTRA_TI_LIQUIDS_I": _subscript_dict[
                                    "PROTRA_TI_LIQUIDS_I"
                                ],
                            },
                            ["REGIONS_9_I", "PROTRA_TI_LIQUIDS_I"],
                        ),
                        lambda: if_then_else(
                            time() < final_year_model_explorer(),
                            lambda: zidz(
                                (
                                    1
                                    - scenario_target_share_bioenergy_in_fossil_liquids_and_gases_option_3_me()
                                )
                                - protra_input_shares_empiric()
                                .loc[
                                    :,
                                    _subscript_dict["PROTRA_TI_LIQUIDS_I"],
                                    "TI_liquid_fossil",
                                ]
                                .reset_coords(drop=True)
                                .rename({"NRG_PROTRA_I": "PROTRA_TI_LIQUIDS_I"}),
                                final_year_model_explorer()
                                - initial_year_model_explorer(),
                            ),
                            lambda: xr.DataArray(
                                0,
                                {
                                    "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                                    "PROTRA_TI_LIQUIDS_I": _subscript_dict[
                                        "PROTRA_TI_LIQUIDS_I"
                                    ],
                                },
                                ["REGIONS_9_I", "PROTRA_TI_LIQUIDS_I"],
                            ),
                        ),
                    ),
                    lambda: xr.DataArray(
                        0,
                        {
                            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                            "PROTRA_TI_LIQUIDS_I": _subscript_dict[
                                "PROTRA_TI_LIQUIDS_I"
                            ],
                        },
                        ["REGIONS_9_I", "PROTRA_TI_LIQUIDS_I"],
                    ),
                ),
            ),
        )
        .expand_dims({"NRG_COMMODITIES_I": ["TI_liquid_fossil"]}, 2)
        .values
    )
    return value


@component.add(
    name="model_explorer_uranium_maximum_supply_curve",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_uranium_maximum_supply_curve_me": 3,
        "scenario_uranium_maximum_supply_curve_option_1_me": 1,
        "scenario_uranium_maximum_supply_curve_option_2_me": 1,
        "scenario_uranium_maximum_supply_curve_option_3_me": 1,
    },
)
def model_explorer_uranium_maximum_supply_curve():
    return if_then_else(
        select_uranium_maximum_supply_curve_me() == 1,
        lambda: scenario_uranium_maximum_supply_curve_option_1_me(),
        lambda: if_then_else(
            select_uranium_maximum_supply_curve_me() == 2,
            lambda: scenario_uranium_maximum_supply_curve_option_2_me(),
            lambda: if_then_else(
                select_uranium_maximum_supply_curve_me() == 3,
                lambda: scenario_uranium_maximum_supply_curve_option_3_me(),
                lambda: 0,
            ),
        ),
    )


@component.add(
    name="model_explorer_working_time_variation",
    units="DMNL",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 4,
        "initial_year_model_explorer": 7,
        "hours_per_worker_historic": 7,
        "scenario_working_time_option_2_me": 1,
        "select_working_time_variation_me": 3,
        "final_year_working_time": 6,
        "scenario_working_time_option_1_me": 1,
        "scenario_working_time_option_3_me": 1,
    },
)
def model_explorer_working_time_variation():
    """
    Policy working time variation for model explorer.
    """
    return if_then_else(
        time() < initial_year_model_explorer(),
        lambda: hours_per_worker_historic(),
        lambda: if_then_else(
            select_working_time_variation_me() == 1,
            lambda: hours_per_worker_historic()
            + ramp(
                __data["time"],
                (scenario_working_time_option_1_me() * hours_per_worker_historic())
                / (final_year_working_time() - initial_year_model_explorer()),
                initial_year_model_explorer(),
                final_year_working_time(),
            ),
            lambda: if_then_else(
                select_working_time_variation_me() == 2,
                lambda: hours_per_worker_historic()
                + ramp(
                    __data["time"],
                    (scenario_working_time_option_2_me() * hours_per_worker_historic())
                    / (final_year_working_time() - initial_year_model_explorer()),
                    initial_year_model_explorer(),
                    final_year_working_time(),
                ),
                lambda: if_then_else(
                    select_working_time_variation_me() == 3,
                    lambda: hours_per_worker_historic()
                    + ramp(
                        __data["time"],
                        (
                            scenario_working_time_option_3_me()
                            * hours_per_worker_historic()
                        )
                        / (final_year_working_time() - initial_year_model_explorer()),
                        initial_year_model_explorer(),
                        final_year_working_time(),
                    ),
                    lambda: xr.DataArray(
                        0,
                        {
                            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                            "SECTORS_I": _subscript_dict["SECTORS_I"],
                        },
                        ["REGIONS_35_I", "SECTORS_I"],
                    ),
                ),
            ),
        ),
    )


@component.add(
    name="SCENARIO_BASELINE_OPTION_2_ME",
    units="kg/(Year*people)",
    subscripts=["REGIONS_9_I", "FOODS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_scenario_baseline_option_2_me"},
)
def scenario_baseline_option_2_me():
    """
    SCENARIO_BASELINE_OPTION_2_ME
    """
    return _ext_constant_scenario_baseline_option_2_me()


_ext_constant_scenario_baseline_option_2_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_BASELINE_OPTION_2_ME",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "FOODS_I": _subscript_dict["FOODS_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "FOODS_I": _subscript_dict["FOODS_I"],
    },
    "_ext_constant_scenario_baseline_option_2_me",
)


@component.add(
    name="SCENARIO_CLIMATE_SENSITIVITY_OPTION_1_ME",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_scenario_climate_sensitivity_option_1_me"
    },
)
def scenario_climate_sensitivity_option_1_me():
    """
    SCENARIO_CLIMATE_SENSITIVITY_OPTION_1_ME
    """
    return _ext_constant_scenario_climate_sensitivity_option_1_me()


_ext_constant_scenario_climate_sensitivity_option_1_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_CLIMATE_SENSITIVITY_OPTION_1_ME",
    {},
    _root,
    {},
    "_ext_constant_scenario_climate_sensitivity_option_1_me",
)


@component.add(
    name="SCENARIO_CLIMATE_SENSITIVITY_OPTION_2_ME",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_scenario_climate_sensitivity_option_2_me"
    },
)
def scenario_climate_sensitivity_option_2_me():
    """
    SCENARIO_CLIMATE_SENSITIVITY_OPTION_2_ME
    """
    return _ext_constant_scenario_climate_sensitivity_option_2_me()


_ext_constant_scenario_climate_sensitivity_option_2_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_CLIMATE_SENSITIVITY_OPTION_2_ME",
    {},
    _root,
    {},
    "_ext_constant_scenario_climate_sensitivity_option_2_me",
)


@component.add(
    name="SCENARIO_CLIMATE_SENSITIVITY_OPTION_3_ME",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_scenario_climate_sensitivity_option_3_me"
    },
)
def scenario_climate_sensitivity_option_3_me():
    """
    SCENARIO_CLIMATE_SENSITIVITY_OPTION_3_ME
    """
    return _ext_constant_scenario_climate_sensitivity_option_3_me()


_ext_constant_scenario_climate_sensitivity_option_3_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_CLIMATE_SENSITIVITY_OPTION_3_ME",
    {},
    _root,
    {},
    "_ext_constant_scenario_climate_sensitivity_option_3_me",
)


@component.add(
    name="SCENARIO_DEBT_INTEREST_RATE_TARGET_OPTION_1_ME",
    units="DMNL",
    subscripts=["REGIONS_35_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_scenario_debt_interest_rate_target_option_1_me"
    },
)
def scenario_debt_interest_rate_target_option_1_me():
    """
    SCENARIO_DEBT_INTEREST_RATE_TARGET_OPTION_1_ME
    """
    return _ext_constant_scenario_debt_interest_rate_target_option_1_me()


_ext_constant_scenario_debt_interest_rate_target_option_1_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_DEBT_INTEREST_RATE_TARGET_OPTION_1_ME*",
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    _root,
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    "_ext_constant_scenario_debt_interest_rate_target_option_1_me",
)


@component.add(
    name="SCENARIO_DEBT_INTEREST_RATE_TARGET_OPTION_2_ME",
    units="DMNL",
    subscripts=["REGIONS_35_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_scenario_debt_interest_rate_target_option_2_me"
    },
)
def scenario_debt_interest_rate_target_option_2_me():
    """
    SCENARIO_DEBT_INTEREST_RATE_TARGET_OPTION_2_ME
    """
    return _ext_constant_scenario_debt_interest_rate_target_option_2_me()


_ext_constant_scenario_debt_interest_rate_target_option_2_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_DEBT_INTEREST_RATE_TARGET_OPTION_2_ME*",
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    _root,
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    "_ext_constant_scenario_debt_interest_rate_target_option_2_me",
)


@component.add(
    name="SCENARIO_DEBT_INTEREST_RATE_TARGET_OPTION_3_ME",
    units="DMNL",
    subscripts=["REGIONS_35_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_scenario_debt_interest_rate_target_option_3_me"
    },
)
def scenario_debt_interest_rate_target_option_3_me():
    """
    SCENARIO_DEBT_INTEREST_RATE_TARGET_OPTION_3_ME
    """
    return _ext_constant_scenario_debt_interest_rate_target_option_3_me()


_ext_constant_scenario_debt_interest_rate_target_option_3_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_DEBT_INTEREST_RATE_TARGET_OPTION_3_ME*",
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    _root,
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    "_ext_constant_scenario_debt_interest_rate_target_option_3_me",
)


@component.add(
    name="SCENARIO_ENERGY_EFFICIENCY_OPTION_1_ME",
    units="1/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_scenario_energy_efficiency_option_1_me"},
)
def scenario_energy_efficiency_option_1_me():
    """
    SCENARIO_ENERGY_EFFICIENCY_OPTION_1_ME
    """
    return _ext_constant_scenario_energy_efficiency_option_1_me()


_ext_constant_scenario_energy_efficiency_option_1_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_ENERGY_EFFICIENCY_OPTION_1_ME*",
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    _root,
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    "_ext_constant_scenario_energy_efficiency_option_1_me",
)


@component.add(
    name="SCENARIO_ENERGY_EFFICIENCY_OPTION_2_ME",
    units="1/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_scenario_energy_efficiency_option_2_me"},
)
def scenario_energy_efficiency_option_2_me():
    """
    SCENARIO_ENERGY_EFFICIENCY_OPTION_2_ME
    """
    return _ext_constant_scenario_energy_efficiency_option_2_me()


_ext_constant_scenario_energy_efficiency_option_2_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_ENERGY_EFFICIENCY_OPTION_2_ME*",
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    _root,
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    "_ext_constant_scenario_energy_efficiency_option_2_me",
)


@component.add(
    name="SCENARIO_ENERGY_EFFICIENCY_OPTION_3_ME",
    units="1/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_scenario_energy_efficiency_option_3_me"},
)
def scenario_energy_efficiency_option_3_me():
    """
    SCENARIO_ENERGY_EFFICIENCY_OPTION_3_ME
    """
    return _ext_constant_scenario_energy_efficiency_option_3_me()


_ext_constant_scenario_energy_efficiency_option_3_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_ENERGY_EFFICIENCY_OPTION_3_ME*",
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    _root,
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    "_ext_constant_scenario_energy_efficiency_option_3_me",
)


@component.add(
    name="SCENARIO_FERTILITY_RATES_OPTION_1_ME",
    units="people/(kpeople*Year)",
    subscripts=["REGIONS_35_I", "SEX_I", "FERTILITY_AGES_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_scenario_fertility_rates_option_1_me"},
)
def scenario_fertility_rates_option_1_me():
    """
    SCENARIO_FERTILITY_RATES_OPTION_1_ME
    """
    return _ext_constant_scenario_fertility_rates_option_1_me()


_ext_constant_scenario_fertility_rates_option_1_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_FERTILITY_RATES_OPTION_1_ME",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SEX_I": ["FEMALE"],
        "FERTILITY_AGES_I": _subscript_dict["FERTILITY_AGES_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SEX_I": _subscript_dict["SEX_I"],
        "FERTILITY_AGES_I": _subscript_dict["FERTILITY_AGES_I"],
    },
    "_ext_constant_scenario_fertility_rates_option_1_me",
)


@component.add(
    name="SCENARIO_FERTILITY_RATES_OPTION_2_ME",
    units="people/(kpeople*Year)",
    subscripts=["REGIONS_35_I", "SEX_I", "FERTILITY_AGES_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_scenario_fertility_rates_option_2_me"},
)
def scenario_fertility_rates_option_2_me():
    """
    SCENARIO_FERTILITY_RATES_OPTION_2_ME
    """
    return _ext_constant_scenario_fertility_rates_option_2_me()


_ext_constant_scenario_fertility_rates_option_2_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_FERTILITY_RATES_OPTION_2_ME",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SEX_I": ["FEMALE"],
        "FERTILITY_AGES_I": _subscript_dict["FERTILITY_AGES_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SEX_I": _subscript_dict["SEX_I"],
        "FERTILITY_AGES_I": _subscript_dict["FERTILITY_AGES_I"],
    },
    "_ext_constant_scenario_fertility_rates_option_2_me",
)


@component.add(
    name="SCENARIO_FERTILITY_RATES_OPTION_3_ME",
    units="people/(kpeople*Year)",
    subscripts=["REGIONS_35_I", "SEX_I", "FERTILITY_AGES_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_scenario_fertility_rates_option_3_me"},
)
def scenario_fertility_rates_option_3_me():
    """
    SCENARIO_FERTILITY_RATES_OPTION_3_ME
    """
    return _ext_constant_scenario_fertility_rates_option_3_me()


_ext_constant_scenario_fertility_rates_option_3_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_FERTILITY_RATES_OPTION_3_ME",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SEX_I": ["FEMALE"],
        "FERTILITY_AGES_I": _subscript_dict["FERTILITY_AGES_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SEX_I": _subscript_dict["SEX_I"],
        "FERTILITY_AGES_I": _subscript_dict["FERTILITY_AGES_I"],
    },
    "_ext_constant_scenario_fertility_rates_option_3_me",
)


@component.add(
    name="SCENARIO_FINAL_GENDER_PARITY_INDEX_OPTION_1_ME",
    units="DMNL",
    subscripts=["REGIONS_35_I", "EDUCATIONAL_LEVEL_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_scenario_final_gender_parity_index_option_1_me"
    },
)
def scenario_final_gender_parity_index_option_1_me():
    """
    SCENARIO_FINAL_GENDER_PARITY_INDEX_OPTION_1_ME
    """
    return _ext_constant_scenario_final_gender_parity_index_option_1_me()


_ext_constant_scenario_final_gender_parity_index_option_1_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_FINAL_GENDER_PARITY_INDEX_HIGH_OPTION_1_ME*",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "EDUCATIONAL_LEVEL_I": ["HIGH_EDUCATION"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "EDUCATIONAL_LEVEL_I": _subscript_dict["EDUCATIONAL_LEVEL_I"],
    },
    "_ext_constant_scenario_final_gender_parity_index_option_1_me",
)

_ext_constant_scenario_final_gender_parity_index_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_FINAL_GENDER_PARITY_INDEX_MEDIUM_OPTION_1_ME*",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "EDUCATIONAL_LEVEL_I": ["MEDIUM_EDUCATION"],
    },
)


@component.add(
    name="SCENARIO_FINAL_GENDER_PARITY_INDEX_OPTION_2_ME",
    units="DMNL",
    subscripts=["REGIONS_35_I", "EDUCATIONAL_LEVEL_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_scenario_final_gender_parity_index_option_2_me"
    },
)
def scenario_final_gender_parity_index_option_2_me():
    """
    SCENARIO_FINAL_GENDER_PARITY_INDEX_OPTION_2_ME
    """
    return _ext_constant_scenario_final_gender_parity_index_option_2_me()


_ext_constant_scenario_final_gender_parity_index_option_2_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_FINAL_GENDER_PARITY_INDEX_HIGH_OPTION_2_ME*",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "EDUCATIONAL_LEVEL_I": ["HIGH_EDUCATION"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "EDUCATIONAL_LEVEL_I": _subscript_dict["EDUCATIONAL_LEVEL_I"],
    },
    "_ext_constant_scenario_final_gender_parity_index_option_2_me",
)

_ext_constant_scenario_final_gender_parity_index_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_FINAL_GENDER_PARITY_INDEX_MEDIUM_OPTION_2_ME*",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "EDUCATIONAL_LEVEL_I": ["MEDIUM_EDUCATION"],
    },
)


@component.add(
    name="SCENARIO_FINAL_GENDER_PARITY_INDEX_OPTION_3_ME",
    units="DMNL",
    subscripts=["REGIONS_35_I", "EDUCATIONAL_LEVEL_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_scenario_final_gender_parity_index_option_3_me"
    },
)
def scenario_final_gender_parity_index_option_3_me():
    """
    SCENARIO_FINAL_GENDER_PARITY_INDEX_OPTION_3_ME
    """
    return _ext_constant_scenario_final_gender_parity_index_option_3_me()


_ext_constant_scenario_final_gender_parity_index_option_3_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_FINAL_GENDER_PARITY_INDEX_HIGH_OPTION_3_ME*",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "EDUCATIONAL_LEVEL_I": ["HIGH_EDUCATION"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "EDUCATIONAL_LEVEL_I": _subscript_dict["EDUCATIONAL_LEVEL_I"],
    },
    "_ext_constant_scenario_final_gender_parity_index_option_3_me",
)

_ext_constant_scenario_final_gender_parity_index_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_FINAL_GENDER_PARITY_INDEX_MEDIUM_OPTION_3_ME*",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "EDUCATIONAL_LEVEL_I": ["MEDIUM_EDUCATION"],
    },
)


@component.add(
    name="SCENARIO_FLEXITARIANA_OPTION_1_ME",
    units="kg/(Year*people)",
    subscripts=["REGIONS_9_I", "FOODS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_scenario_flexitariana_option_1_me"},
)
def scenario_flexitariana_option_1_me():
    """
    SCENARIO_FLEXITARIANA_OPTION_1_ME
    """
    return _ext_constant_scenario_flexitariana_option_1_me()


_ext_constant_scenario_flexitariana_option_1_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_FLEXITARIANA_OPTION_1_ME",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "FOODS_I": _subscript_dict["FOODS_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "FOODS_I": _subscript_dict["FOODS_I"],
    },
    "_ext_constant_scenario_flexitariana_option_1_me",
)


@component.add(
    name="SCENARIO_FORESTRY_SELF_SUFFICIENCY_OPTION_1_ME",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_scenario_forestry_self_sufficiency_option_1_me"
    },
)
def scenario_forestry_self_sufficiency_option_1_me():
    """
    SCENARIO_FOREST_OVEREXPLOITATION_OPTION_1_ME
    """
    return _ext_constant_scenario_forestry_self_sufficiency_option_1_me()


_ext_constant_scenario_forestry_self_sufficiency_option_1_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_FOREST_OVEREXPLOITATION_OPTION_1_ME*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_scenario_forestry_self_sufficiency_option_1_me",
)


@component.add(
    name="SCENARIO_FORESTRY_SELF_SUFFICIENCY_OPTION_2_ME",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_scenario_forestry_self_sufficiency_option_2_me"
    },
)
def scenario_forestry_self_sufficiency_option_2_me():
    """
    SCENARIO_FOREST_OVEREXPLOITATION_OPTION_2_ME
    """
    return _ext_constant_scenario_forestry_self_sufficiency_option_2_me()


_ext_constant_scenario_forestry_self_sufficiency_option_2_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_FOREST_OVEREXPLOITATION_OPTION_2_ME*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_scenario_forestry_self_sufficiency_option_2_me",
)


@component.add(
    name="SCENARIO_FORESTRY_SELF_SUFFICIENCY_OPTION_3_ME",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_scenario_forestry_self_sufficiency_option_3_me"
    },
)
def scenario_forestry_self_sufficiency_option_3_me():
    """
    SCENARIO_FOREST_OVEREXPLOITATION_OPTION_3_ME
    """
    return _ext_constant_scenario_forestry_self_sufficiency_option_3_me()


_ext_constant_scenario_forestry_self_sufficiency_option_3_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_FOREST_OVEREXPLOITATION_OPTION_3_ME*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_scenario_forestry_self_sufficiency_option_3_me",
)


@component.add(
    name="SCENARIO_GOVERMENT_OPTION_1_ME",
    units="1/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_scenario_goverment_option_1_me"},
)
def scenario_goverment_option_1_me():
    """
    SCENARIO_GOVERMENT_OPTION_1_ME
    """
    return _ext_constant_scenario_goverment_option_1_me()


_ext_constant_scenario_goverment_option_1_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_GOVERMENT_OPTION_1_ME*",
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    _root,
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    "_ext_constant_scenario_goverment_option_1_me",
)


@component.add(
    name="SCENARIO_GOVERMENT_OPTION_2_ME",
    units="1/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_scenario_goverment_option_2_me"},
)
def scenario_goverment_option_2_me():
    """
    SCENARIO_GOVERMENT_OPTION_2_ME
    """
    return _ext_constant_scenario_goverment_option_2_me()


_ext_constant_scenario_goverment_option_2_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_GOVERMENT_OPTION_2_ME*",
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    _root,
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    "_ext_constant_scenario_goverment_option_2_me",
)


@component.add(
    name="SCENARIO_GOVERMENT_OPTION_3_ME",
    units="1/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_scenario_goverment_option_3_me"},
)
def scenario_goverment_option_3_me():
    """
    SCENARIO_GOVERMENT_OPTION_3_ME
    """
    return _ext_constant_scenario_goverment_option_3_me()


_ext_constant_scenario_goverment_option_3_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_GOVERMENT_OPTION_3_ME*",
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    _root,
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    "_ext_constant_scenario_goverment_option_3_me",
)


@component.add(
    name="SCENARIO_LAND_PROTECTION_BY_POLICY_OPTION_1_ME",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LANDS_I"],
    comp_type="Constant",
    comp_subtype="External, Normal",
    depends_on={
        "__external__": "_ext_constant_scenario_land_protection_by_policy_option_1_me"
    },
)
def scenario_land_protection_by_policy_option_1_me():
    """
    SCENARIO_LAND_PROTECTION_BY_POLICY_OPTION_1_ME
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "LANDS_I": _subscript_dict["LANDS_I"],
        },
        ["REGIONS_9_I", "LANDS_I"],
    )
    def_subs = xr.zeros_like(value, dtype=bool)
    def_subs.loc[:, ["CROPLAND_RAINFED"]] = True
    def_subs.loc[:, ["CROPLAND_IRRIGATED"]] = True
    def_subs.loc[:, ["FOREST_MANAGED"]] = True
    def_subs.loc[:, ["FOREST_PRIMARY"]] = True
    value.values[
        def_subs.values
    ] = _ext_constant_scenario_land_protection_by_policy_option_1_me().values[
        def_subs.values
    ]
    value.loc[:, ["FOREST_PLANTATIONS"]] = 0
    value.loc[:, ["SHRUBLAND"]] = 0
    value.loc[:, ["GRASSLAND"]] = 0
    value.loc[:, ["OTHER_LAND"]] = 0
    value.loc[:, ["WETLAND"]] = 0
    value.loc[:, ["URBAN_LAND"]] = 0
    value.loc[:, ["SOLAR_LAND"]] = 0
    value.loc[:, ["SNOW_ICE_WATERBODIES"]] = 0
    return value


_ext_constant_scenario_land_protection_by_policy_option_1_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OPTION_1_POLICY_OBJECTIVE_CROPLAND_PROTECTION_ME*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"], "LANDS_I": ["CROPLAND_RAINFED"]},
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": _subscript_dict["LANDS_I"],
    },
    "_ext_constant_scenario_land_protection_by_policy_option_1_me",
)

_ext_constant_scenario_land_protection_by_policy_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OPTION_1_POLICY_OBJECTIVE_CROPLAND_PROTECTION_ME*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"], "LANDS_I": ["CROPLAND_IRRIGATED"]},
)

_ext_constant_scenario_land_protection_by_policy_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OPTION_1_POLICY_OBJECTIVE_MANAGED_FOREST_PROTECTION_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"], "LANDS_I": ["FOREST_MANAGED"]},
)

_ext_constant_scenario_land_protection_by_policy_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OPTION_1_POLICY_OBJECTIVE_PRIMARY_FOREST_PROTECTION_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"], "LANDS_I": ["FOREST_PRIMARY"]},
)


@component.add(
    name="SCENARIO_LAND_PROTECTION_BY_POLICY_OPTION_2_ME",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LANDS_I"],
    comp_type="Constant",
    comp_subtype="External, Normal",
    depends_on={
        "__external__": "_ext_constant_scenario_land_protection_by_policy_option_2_me"
    },
)
def scenario_land_protection_by_policy_option_2_me():
    """
    SCENARIO_LAND_PROTECTION_BY_POLICY_OPTION_2_ME
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "LANDS_I": _subscript_dict["LANDS_I"],
        },
        ["REGIONS_9_I", "LANDS_I"],
    )
    def_subs = xr.zeros_like(value, dtype=bool)
    def_subs.loc[:, ["CROPLAND_RAINFED"]] = True
    def_subs.loc[:, ["CROPLAND_IRRIGATED"]] = True
    def_subs.loc[:, ["FOREST_MANAGED"]] = True
    def_subs.loc[:, ["FOREST_PRIMARY"]] = True
    value.values[
        def_subs.values
    ] = _ext_constant_scenario_land_protection_by_policy_option_2_me().values[
        def_subs.values
    ]
    value.loc[:, ["FOREST_PLANTATIONS"]] = 0
    value.loc[:, ["SHRUBLAND"]] = 0
    value.loc[:, ["GRASSLAND"]] = 0
    value.loc[:, ["OTHER_LAND"]] = 0
    value.loc[:, ["WETLAND"]] = 0
    value.loc[:, ["URBAN_LAND"]] = 0
    value.loc[:, ["SOLAR_LAND"]] = 0
    value.loc[:, ["SNOW_ICE_WATERBODIES"]] = 0
    return value


_ext_constant_scenario_land_protection_by_policy_option_2_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OPTION_2_POLICY_OBJECTIVE_CROPLAND_PROTECTION_ME*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"], "LANDS_I": ["CROPLAND_RAINFED"]},
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": _subscript_dict["LANDS_I"],
    },
    "_ext_constant_scenario_land_protection_by_policy_option_2_me",
)

_ext_constant_scenario_land_protection_by_policy_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OPTION_2_POLICY_OBJECTIVE_CROPLAND_PROTECTION_ME*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"], "LANDS_I": ["CROPLAND_IRRIGATED"]},
)

_ext_constant_scenario_land_protection_by_policy_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OPTION_2_POLICY_OBJECTIVE_MANAGED_FOREST_PROTECTION_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"], "LANDS_I": ["FOREST_MANAGED"]},
)

_ext_constant_scenario_land_protection_by_policy_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OPTION_2_POLICY_OBJECTIVE_PRIMARY_FOREST_PROTECTION_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"], "LANDS_I": ["FOREST_PRIMARY"]},
)


@component.add(
    name="SCENARIO_LAND_PROTECTION_BY_POLICY_OPTION_3_ME",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LANDS_I"],
    comp_type="Constant",
    comp_subtype="External, Normal",
    depends_on={
        "__external__": "_ext_constant_scenario_land_protection_by_policy_option_3_me"
    },
)
def scenario_land_protection_by_policy_option_3_me():
    """
    SCENARIO_LAND_PROTECTION_BY_POLICY_OPTION_3_ME
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "LANDS_I": _subscript_dict["LANDS_I"],
        },
        ["REGIONS_9_I", "LANDS_I"],
    )
    def_subs = xr.zeros_like(value, dtype=bool)
    def_subs.loc[:, ["CROPLAND_RAINFED"]] = True
    def_subs.loc[:, ["CROPLAND_IRRIGATED"]] = True
    def_subs.loc[:, ["FOREST_MANAGED"]] = True
    def_subs.loc[:, ["FOREST_PRIMARY"]] = True
    value.values[
        def_subs.values
    ] = _ext_constant_scenario_land_protection_by_policy_option_3_me().values[
        def_subs.values
    ]
    value.loc[:, ["FOREST_PLANTATIONS"]] = 0
    value.loc[:, ["SHRUBLAND"]] = 0
    value.loc[:, ["GRASSLAND"]] = 0
    value.loc[:, ["OTHER_LAND"]] = 0
    value.loc[:, ["WETLAND"]] = 0
    value.loc[:, ["URBAN_LAND"]] = 0
    value.loc[:, ["SOLAR_LAND"]] = 0
    value.loc[:, ["SNOW_ICE_WATERBODIES"]] = 0
    return value


_ext_constant_scenario_land_protection_by_policy_option_3_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OPTION_3_POLICY_OBJECTIVE_CROPLAND_PROTECTION_ME*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"], "LANDS_I": ["CROPLAND_RAINFED"]},
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "LANDS_I": _subscript_dict["LANDS_I"],
    },
    "_ext_constant_scenario_land_protection_by_policy_option_3_me",
)

_ext_constant_scenario_land_protection_by_policy_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OPTION_3_POLICY_OBJECTIVE_CROPLAND_PROTECTION_ME*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"], "LANDS_I": ["CROPLAND_IRRIGATED"]},
)

_ext_constant_scenario_land_protection_by_policy_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OPTION_3_POLICY_OBJECTIVE_MANAGED_FOREST_PROTECTION_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"], "LANDS_I": ["FOREST_MANAGED"]},
)

_ext_constant_scenario_land_protection_by_policy_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OPTION_3_POLICY_OBJECTIVE_PRIMARY_FOREST_PROTECTION_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"], "LANDS_I": ["FOREST_PRIMARY"]},
)


@component.add(
    name="SCENARIO_MANURE_MANAGEMENT_SYSTEM_OPTION_1_ME",
    units="DMNL",
    subscripts=["ANIMALS_TYPES_I", "REGIONS_9_I", "MANURE_MANAGEMENT_SYSTEM_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_scenario_manure_management_system_option_1_me"
    },
)
def scenario_manure_management_system_option_1_me():
    """
    SCENARIO_MANURE_MANAGEMENT_SYSTEM_OPTION_1_ME
    """
    return _ext_constant_scenario_manure_management_system_option_1_me()


_ext_constant_scenario_manure_management_system_option_1_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_DAIRY_CATTLE_MANURE_MANAGEMENT_SYSTEMS_OPTION_1_ME",
    {
        "ANIMALS_TYPES_I": ["DAIRY_CATTLE"],
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "MANURE_MANAGEMENT_SYSTEM_I": _subscript_dict["MANURE_MANAGEMENT_SYSTEM_I"],
    },
    _root,
    {
        "ANIMALS_TYPES_I": _subscript_dict["ANIMALS_TYPES_I"],
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "MANURE_MANAGEMENT_SYSTEM_I": _subscript_dict["MANURE_MANAGEMENT_SYSTEM_I"],
    },
    "_ext_constant_scenario_manure_management_system_option_1_me",
)

_ext_constant_scenario_manure_management_system_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_OTHER_CATTLE_MANURE_MANAGEMENT_SYSTEM_OPTION_1_ME",
    {
        "ANIMALS_TYPES_I": ["OTHER_CATTLE"],
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "MANURE_MANAGEMENT_SYSTEM_I": _subscript_dict["MANURE_MANAGEMENT_SYSTEM_I"],
    },
)

_ext_constant_scenario_manure_management_system_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_BUFFALO_MANURE_MANAGEMENT_SYSTEM_OPTION_1_ME",
    {
        "ANIMALS_TYPES_I": ["BUFFALO"],
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "MANURE_MANAGEMENT_SYSTEM_I": _subscript_dict["MANURE_MANAGEMENT_SYSTEM_I"],
    },
)

_ext_constant_scenario_manure_management_system_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_SWINE_MANURE_MANAGEMENT_SYSTEM_OPTION_1_ME",
    {
        "ANIMALS_TYPES_I": ["SWINE"],
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "MANURE_MANAGEMENT_SYSTEM_I": _subscript_dict["MANURE_MANAGEMENT_SYSTEM_I"],
    },
)


@component.add(
    name="SCENARIO_MANURE_MANAGEMENT_SYSTEM_OPTION_2_ME",
    units="DMNL",
    subscripts=["ANIMALS_TYPES_I", "REGIONS_9_I", "MANURE_MANAGEMENT_SYSTEM_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_scenario_manure_management_system_option_2_me"
    },
)
def scenario_manure_management_system_option_2_me():
    """
    SCENARIO_MANURE_MANAGEMENT_SYSTEM_OPTION_2_ME
    """
    return _ext_constant_scenario_manure_management_system_option_2_me()


_ext_constant_scenario_manure_management_system_option_2_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_DAIRY_CATTLE_MANURE_MANAGEMENT_SYSTEM_OPTION_2_ME",
    {
        "ANIMALS_TYPES_I": ["DAIRY_CATTLE"],
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "MANURE_MANAGEMENT_SYSTEM_I": _subscript_dict["MANURE_MANAGEMENT_SYSTEM_I"],
    },
    _root,
    {
        "ANIMALS_TYPES_I": _subscript_dict["ANIMALS_TYPES_I"],
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "MANURE_MANAGEMENT_SYSTEM_I": _subscript_dict["MANURE_MANAGEMENT_SYSTEM_I"],
    },
    "_ext_constant_scenario_manure_management_system_option_2_me",
)

_ext_constant_scenario_manure_management_system_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_OTHER_CATTLE_MANURE_MANAGEMENT_SYSTEM_OPTION_2_ME",
    {
        "ANIMALS_TYPES_I": ["OTHER_CATTLE"],
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "MANURE_MANAGEMENT_SYSTEM_I": _subscript_dict["MANURE_MANAGEMENT_SYSTEM_I"],
    },
)

_ext_constant_scenario_manure_management_system_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_BUFFALO_MANURE_MANAGEMENT_SYSTEM_OPTION_2_ME",
    {
        "ANIMALS_TYPES_I": ["BUFFALO"],
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "MANURE_MANAGEMENT_SYSTEM_I": _subscript_dict["MANURE_MANAGEMENT_SYSTEM_I"],
    },
)

_ext_constant_scenario_manure_management_system_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_SWINE_MANURE_MANAGEMENT_SYSTEM_OPTION_2_ME",
    {
        "ANIMALS_TYPES_I": ["SWINE"],
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "MANURE_MANAGEMENT_SYSTEM_I": _subscript_dict["MANURE_MANAGEMENT_SYSTEM_I"],
    },
)


@component.add(
    name="SCENARIO_MANURE_MANAGEMENT_SYSTEM_OPTION_3_ME",
    units="DMNL",
    subscripts=["ANIMALS_TYPES_I", "REGIONS_9_I", "MANURE_MANAGEMENT_SYSTEM_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_scenario_manure_management_system_option_3_me"
    },
)
def scenario_manure_management_system_option_3_me():
    """
    SCENARIO_MANURE_MANAGEMENT_SYSTEM_OPTION_3_ME
    """
    return _ext_constant_scenario_manure_management_system_option_3_me()


_ext_constant_scenario_manure_management_system_option_3_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_DAIRY_CATTLE_MANURE_MANAGEMENT_SYSTEM_OPTION_3_ME",
    {
        "ANIMALS_TYPES_I": ["DAIRY_CATTLE"],
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "MANURE_MANAGEMENT_SYSTEM_I": _subscript_dict["MANURE_MANAGEMENT_SYSTEM_I"],
    },
    _root,
    {
        "ANIMALS_TYPES_I": _subscript_dict["ANIMALS_TYPES_I"],
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "MANURE_MANAGEMENT_SYSTEM_I": _subscript_dict["MANURE_MANAGEMENT_SYSTEM_I"],
    },
    "_ext_constant_scenario_manure_management_system_option_3_me",
)

_ext_constant_scenario_manure_management_system_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_OTHER_CATTLE_MANURE_MANAGEMENT_SYSTEM_OPTION_3_ME",
    {
        "ANIMALS_TYPES_I": ["OTHER_CATTLE"],
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "MANURE_MANAGEMENT_SYSTEM_I": _subscript_dict["MANURE_MANAGEMENT_SYSTEM_I"],
    },
)

_ext_constant_scenario_manure_management_system_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_BUFFALO_MANURE_MANAGEMENT_SYSTEM_OPTION_3_ME",
    {
        "ANIMALS_TYPES_I": ["BUFFALO"],
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "MANURE_MANAGEMENT_SYSTEM_I": _subscript_dict["MANURE_MANAGEMENT_SYSTEM_I"],
    },
)

_ext_constant_scenario_manure_management_system_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_SWINE_MANURE_MANAGEMENT_SYSTEM_OPTION_3_ME",
    {
        "ANIMALS_TYPES_I": ["SWINE"],
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "MANURE_MANAGEMENT_SYSTEM_I": _subscript_dict["MANURE_MANAGEMENT_SYSTEM_I"],
    },
)


@component.add(
    name="SCENARIO_OBJECTIVE_PERCENTAGE_FE_LIQUID_SUBSTITUTED_BY_H2_SYNTHETIC_LIQUID_OPTION_1_ME",
    units="DMML",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_scenario_objective_percentage_fe_liquid_substituted_by_h2_synthetic_liquid_option_1_me"
    },
)
def scenario_objective_percentage_fe_liquid_substituted_by_h2_synthetic_liquid_option_1_me():
    """
    SCENARIO_OBJECTIVE_PERCENTAGE_FE_LIQUID_SUBSTITUTED_BY_H2_SYNTHETIC_LIQUID_ OPTION_1_ME
    """
    return (
        _ext_constant_scenario_objective_percentage_fe_liquid_substituted_by_h2_synthetic_liquid_option_1_me()
    )


_ext_constant_scenario_objective_percentage_fe_liquid_substituted_by_h2_synthetic_liquid_option_1_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_OBJECTIVE_PERCENTAGE_FE_LIQUID_SUBSTITUTED_BY_H2_SYNTHETIC_LIQUID_OPTION_1_ME*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_scenario_objective_percentage_fe_liquid_substituted_by_h2_synthetic_liquid_option_1_me",
)


@component.add(
    name="SCENARIO_OBJECTIVE_PERCENTAGE_FE_LIQUID_SUBSTITUTED_BY_H2_SYNTHETIC_LIQUID_OPTION_2_ME",
    units="DMML",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_scenario_objective_percentage_fe_liquid_substituted_by_h2_synthetic_liquid_option_2_me"
    },
)
def scenario_objective_percentage_fe_liquid_substituted_by_h2_synthetic_liquid_option_2_me():
    """
    SCENARIO_OBJECTIVE_PERCENTAGE_FE_LIQUID_SUBSTITUTED_BY_H2_SYNTHETIC_LIQUID_ OPTION_2_ME
    """
    return (
        _ext_constant_scenario_objective_percentage_fe_liquid_substituted_by_h2_synthetic_liquid_option_2_me()
    )


_ext_constant_scenario_objective_percentage_fe_liquid_substituted_by_h2_synthetic_liquid_option_2_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_OBJECTIVE_PERCENTAGE_FE_LIQUID_SUBSTITUTED_BY_H2_SYNTHETIC_LIQUID_OPTION_2_ME*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_scenario_objective_percentage_fe_liquid_substituted_by_h2_synthetic_liquid_option_2_me",
)


@component.add(
    name="SCENARIO_OBJECTIVE_PERCENTAGE_FE_LIQUID_SUBSTITUTED_BY_H2_SYNTHETIC_LIQUID_OPTION_3_ME",
    units="DMML",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_scenario_objective_percentage_fe_liquid_substituted_by_h2_synthetic_liquid_option_3_me"
    },
)
def scenario_objective_percentage_fe_liquid_substituted_by_h2_synthetic_liquid_option_3_me():
    """
    SCENARIO_OBJECTIVE_PERCENTAGE_FE_LIQUID_SUBSTITUTED_BY_H2_SYNTHETIC_LIQUID_ OPTION_3_ME
    """
    return (
        _ext_constant_scenario_objective_percentage_fe_liquid_substituted_by_h2_synthetic_liquid_option_3_me()
    )


_ext_constant_scenario_objective_percentage_fe_liquid_substituted_by_h2_synthetic_liquid_option_3_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_OBJECTIVE_PERCENTAGE_FE_LIQUID_SUBSTITUTED_BY_H2_SYNTHETIC_LIQUID_OPTION_3_ME*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_scenario_objective_percentage_fe_liquid_substituted_by_h2_synthetic_liquid_option_3_me",
)


@component.add(
    name="SCENARIO_OIL_RESOURCE_OPTION_1_ME",
    units="bbl",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_scenario_oil_resource_option_1_me"},
)
def scenario_oil_resource_option_1_me():
    """
    SCENARIO_OIL_RESOURCE_OPTION_1_ME
    """
    return _ext_constant_scenario_oil_resource_option_1_me()


_ext_constant_scenario_oil_resource_option_1_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_OIL_RESOURCE_OPTION_1_ME",
    {},
    _root,
    {},
    "_ext_constant_scenario_oil_resource_option_1_me",
)


@component.add(
    name="SCENARIO_OIL_RESOURCE_OPTION_2_ME",
    units="bbl",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_scenario_oil_resource_option_2_me"},
)
def scenario_oil_resource_option_2_me():
    """
    SCENARIO_OIL_RESOURCE_OPTION_2_ME
    """
    return _ext_constant_scenario_oil_resource_option_2_me()


_ext_constant_scenario_oil_resource_option_2_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_OIL_RESOURCE_OPTION_2_ME",
    {},
    _root,
    {},
    "_ext_constant_scenario_oil_resource_option_2_me",
)


@component.add(
    name="SCENARIO_OIL_RESOURCE_OPTION_3_ME",
    units="bbl",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_scenario_oil_resource_option_3_me"},
)
def scenario_oil_resource_option_3_me():
    """
    SCENARIO_OIL_RESOURCE_OPTION_3_ME
    """
    return _ext_constant_scenario_oil_resource_option_3_me()


_ext_constant_scenario_oil_resource_option_3_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_OIL_RESOURCE_OPTION_3_ME",
    {},
    _root,
    {},
    "_ext_constant_scenario_oil_resource_option_3_me",
)


@component.add(
    name="SCENARIO_PASSENGER_TRANSPORT_DEMAND_MODAL_SHARE_OPTION_1_ME",
    units="DMNL",
    subscripts=[
        "REGIONS_35_I",
        "TRANSPORT_POWER_TRAIN_I",
        "PASSENGERS_TRANSPORT_MODE_I",
    ],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me"
    },
)
def scenario_passenger_transport_demand_modal_share_option_1_me():
    """
    SCENARIO_PASSENGER_TRANSPORT_DEMAND_MODAL_SHARE_OPTION_1_ME
    """
    return _ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me()


_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_AUSTRIA_OPTION_1_ME",
    {
        "REGIONS_35_I": ["AUSTRIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
    "_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me",
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_BELGIUM_OPTION_1_ME",
    {
        "REGIONS_35_I": ["BELGIUM"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_BULGARIA_OPTION_1_ME",
    {
        "REGIONS_35_I": ["BULGARIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_CROATIA_OPTION_1_ME",
    {
        "REGIONS_35_I": ["CROATIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_CYPRUS_OPTION_1_ME",
    {
        "REGIONS_35_I": ["CYPRUS"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_CZECH_REPUBILC_OPTION_1_ME",
    {
        "REGIONS_35_I": ["CZECH_REPUBLIC"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_DENMARK_OPTION_1_ME",
    {
        "REGIONS_35_I": ["DENMARK"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_ESTONIA_OPTION_1_ME",
    {
        "REGIONS_35_I": ["ESTONIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_FINLAND_OPTION_1_ME",
    {
        "REGIONS_35_I": ["FINLAND"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_FRANCE_OPTION_1_ME",
    {
        "REGIONS_35_I": ["FRANCE"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_GERMANY_OPTION_1_ME",
    {
        "REGIONS_35_I": ["GERMANY"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_GREECE_OPTION_1_ME",
    {
        "REGIONS_35_I": ["GREECE"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_HUNGARY_OPTION_1_ME",
    {
        "REGIONS_35_I": ["HUNGARY"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_IRELAND_OPTION_1_ME",
    {
        "REGIONS_35_I": ["IRELAND"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_ITALY_OPTION_1_ME",
    {
        "REGIONS_35_I": ["ITALY"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_LATVIA_OPTION_1_ME",
    {
        "REGIONS_35_I": ["LATVIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_LITHUANIA_OPTION_1_ME",
    {
        "REGIONS_35_I": ["LITHUANIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_LUXEMBOURG_OPTION_1_ME",
    {
        "REGIONS_35_I": ["LUXEMBOURG"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_MALTA_OPTION_1_ME",
    {
        "REGIONS_35_I": ["MALTA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_NEHTERLANDS_OPTION_1_ME",
    {
        "REGIONS_35_I": ["NETHERLANDS"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_POLAND_OPTION_1_ME",
    {
        "REGIONS_35_I": ["POLAND"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_PORTUGAL_OPTION_1_ME",
    {
        "REGIONS_35_I": ["PORTUGAL"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_ROMANIA_OPTION_1_ME",
    {
        "REGIONS_35_I": ["ROMANIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_SLOVAKIA_OPTION_1_ME",
    {
        "REGIONS_35_I": ["SLOVAKIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_SLOVENIA_OPTION_1_ME",
    {
        "REGIONS_35_I": ["SLOVENIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_SPAIN_OPTION_1_ME",
    {
        "REGIONS_35_I": ["SPAIN"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_SWEDEN_OPTION_1_ME",
    {
        "REGIONS_35_I": ["SWEDEN"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_UK_OPTION_1_ME",
    {
        "REGIONS_35_I": ["UK"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_CHINA_OPTION_1_ME",
    {
        "REGIONS_35_I": ["CHINA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_EASOC_OPTION_1_ME",
    {
        "REGIONS_35_I": ["EASOC"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_INDIA_OPTION_1_ME",
    {
        "REGIONS_35_I": ["INDIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_LATAM_OPTION_1_ME",
    {
        "REGIONS_35_I": ["LATAM"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_RUSSIA_OPTION_1_ME",
    {
        "REGIONS_35_I": ["RUSSIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_USMCA_OPTION_1_ME",
    {
        "REGIONS_35_I": ["USMCA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_LROW_OPTION_1_ME",
    {
        "REGIONS_35_I": ["LROW"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)


@component.add(
    name="SCENARIO_PASSENGER_TRANSPORT_DEMAND_MODAL_SHARE_OPTION_2_ME",
    units="DMNL",
    subscripts=[
        "REGIONS_35_I",
        "TRANSPORT_POWER_TRAIN_I",
        "PASSENGERS_TRANSPORT_MODE_I",
    ],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me"
    },
)
def scenario_passenger_transport_demand_modal_share_option_2_me():
    """
    SCENARIO_PASSENGER_TRANSPORT_DEMAND_MODAL_SHARE_OPTION_2_ME
    """
    return _ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me()


_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_AUSTRIA_OPTION_2_ME",
    {
        "REGIONS_35_I": ["AUSTRIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
    "_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me",
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_BELGIUM_OPTION_2_ME",
    {
        "REGIONS_35_I": ["BELGIUM"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_BULGARIA_OPTION_2_ME",
    {
        "REGIONS_35_I": ["BULGARIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_CROATIA_OPTION_2_ME",
    {
        "REGIONS_35_I": ["CROATIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_CYPRUS_OPTION_2_ME",
    {
        "REGIONS_35_I": ["CYPRUS"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_CZECH_REPUBLIC_OPTION_2_ME",
    {
        "REGIONS_35_I": ["CZECH_REPUBLIC"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_DENMARK_OPTION_2_ME",
    {
        "REGIONS_35_I": ["DENMARK"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_ESTONIA_OPTION_2_ME",
    {
        "REGIONS_35_I": ["ESTONIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_FINLAND_OPTION_2_ME",
    {
        "REGIONS_35_I": ["FINLAND"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_FRANCE_OPTION_2_ME",
    {
        "REGIONS_35_I": ["FRANCE"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_GERMANY_OPTION_2_ME",
    {
        "REGIONS_35_I": ["GERMANY"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_GREECE_OPTION_2_ME",
    {
        "REGIONS_35_I": ["GREECE"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_HUNGARY_OPTION_2_ME",
    {
        "REGIONS_35_I": ["HUNGARY"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_IRELAND_OPTION_2_ME",
    {
        "REGIONS_35_I": ["IRELAND"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_ITALY_OPTION_2_ME",
    {
        "REGIONS_35_I": ["ITALY"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_LATVIA_OPTION_2_ME",
    {
        "REGIONS_35_I": ["LATVIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_LITHUANIA_OPTION_2_ME",
    {
        "REGIONS_35_I": ["LITHUANIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_LUXEMBOURG_OPTION_2_ME",
    {
        "REGIONS_35_I": ["LUXEMBOURG"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_MALTA_OPTION_2_ME",
    {
        "REGIONS_35_I": ["MALTA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_NETHERLANDS_OPTION_2_ME",
    {
        "REGIONS_35_I": ["NETHERLANDS"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_POLAND_OPTION_2_ME",
    {
        "REGIONS_35_I": ["POLAND"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_PORTUGAL_OPTION_2_ME",
    {
        "REGIONS_35_I": ["PORTUGAL"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_ROMANIA_OPTION_2_ME",
    {
        "REGIONS_35_I": ["ROMANIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_SLOVAKIA_OPTION_2_ME",
    {
        "REGIONS_35_I": ["SLOVAKIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_SLOVENIA_OPTION_2_ME",
    {
        "REGIONS_35_I": ["SLOVENIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_SPAIN_OPTION_2_ME",
    {
        "REGIONS_35_I": ["SPAIN"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_SWEDEN_OPTION_2_ME",
    {
        "REGIONS_35_I": ["SWEDEN"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_UK_OPTION_2_ME",
    {
        "REGIONS_35_I": ["UK"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_CHINA_OPTION_2_ME",
    {
        "REGIONS_35_I": ["CHINA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_EASOC_OPTION_2_ME",
    {
        "REGIONS_35_I": ["EASOC"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_INDIA_OPTION_2_ME",
    {
        "REGIONS_35_I": ["INDIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_LATAM_OPTION_2_ME",
    {
        "REGIONS_35_I": ["LATAM"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_RUSSIA_OPTION_2_ME",
    {
        "REGIONS_35_I": ["RUSSIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_USMCA_OPTION_2_ME",
    {
        "REGIONS_35_I": ["USMCA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_LROW_OPTION_2_ME",
    {
        "REGIONS_35_I": ["LROW"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)


@component.add(
    name="SCENARIO_PASSENGER_TRANSPORT_DEMAND_MODAL_SHARE_OPTION_3_ME",
    units="DMNL",
    subscripts=[
        "REGIONS_35_I",
        "TRANSPORT_POWER_TRAIN_I",
        "PASSENGERS_TRANSPORT_MODE_I",
    ],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me"
    },
)
def scenario_passenger_transport_demand_modal_share_option_3_me():
    """
    SCENARIO_PASSENGER_TRANSPORT_DEMAND_MODAL_SHARE_OPTION_3_ME
    """
    return _ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me()


_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_AUSTRIA_OPTION_3_ME",
    {
        "REGIONS_35_I": ["AUSTRIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
    "_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me",
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_BELGIUM_OPTION_3_ME",
    {
        "REGIONS_35_I": ["BELGIUM"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_BULGARIA_OPTION_3_ME",
    {
        "REGIONS_35_I": ["BULGARIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_CROATIA_OPTION_3_ME",
    {
        "REGIONS_35_I": ["CROATIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_CYPRUS_OPTION_3_ME",
    {
        "REGIONS_35_I": ["CYPRUS"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_CZECH_REPUBLIC_OPTION_3_ME",
    {
        "REGIONS_35_I": ["CZECH_REPUBLIC"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_DENMARK_OPTION_3_ME",
    {
        "REGIONS_35_I": ["DENMARK"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_ESTONIA_OPTION_3_ME",
    {
        "REGIONS_35_I": ["ESTONIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_FINLAND_OPTION_3_ME",
    {
        "REGIONS_35_I": ["FINLAND"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_FRANCE_OPTION_3_ME",
    {
        "REGIONS_35_I": ["FRANCE"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_GERMANY_OPTION_3_ME",
    {
        "REGIONS_35_I": ["GERMANY"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_GREECE_OPTION_3_ME",
    {
        "REGIONS_35_I": ["GREECE"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_HUNGARY_OPTION_3_ME",
    {
        "REGIONS_35_I": ["HUNGARY"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_IRELAND_OPTION_3_ME",
    {
        "REGIONS_35_I": ["IRELAND"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_ITALY_OPTION_3_ME",
    {
        "REGIONS_35_I": ["ITALY"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_LATVIA_OPTION_3_ME",
    {
        "REGIONS_35_I": ["LATVIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_LITHUANIA_OPTION_3_ME",
    {
        "REGIONS_35_I": ["LITHUANIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_LUXEMBOURG_OPTION_3_ME",
    {
        "REGIONS_35_I": ["LUXEMBOURG"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_MALTA_OPTION_3_ME",
    {
        "REGIONS_35_I": ["MALTA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_NETHERLANDS_OPTION_3_ME",
    {
        "REGIONS_35_I": ["NETHERLANDS"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_POLAND_OPTION_3_ME",
    {
        "REGIONS_35_I": ["POLAND"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_PORTUGAL_OPTION_3_ME",
    {
        "REGIONS_35_I": ["PORTUGAL"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_ROMANIA_OPTION_3_ME",
    {
        "REGIONS_35_I": ["ROMANIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_SLOVAKIA_OPTION_3_ME",
    {
        "REGIONS_35_I": ["SLOVAKIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_SLOVENIA_OPTION_3_ME",
    {
        "REGIONS_35_I": ["SLOVENIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_SPAIN_OPTION_3_ME",
    {
        "REGIONS_35_I": ["SPAIN"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_SWEDEN_OPTION_3_ME",
    {
        "REGIONS_35_I": ["SWEDEN"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_UK_OPTION_3_ME",
    {
        "REGIONS_35_I": ["UK"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_CHINA_OPTION_3_ME",
    {
        "REGIONS_35_I": ["CHINA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_EASOC_OPTION_3_ME",
    {
        "REGIONS_35_I": ["EASOC"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_INDIA_OPTION_3_ME",
    {
        "REGIONS_35_I": ["INDIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_LATAM_OPTION_3_ME",
    {
        "REGIONS_35_I": ["LATAM"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_RUSSIA_OPTION_3_ME",
    {
        "REGIONS_35_I": ["RUSSIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_USMCA_OPTION_3_ME",
    {
        "REGIONS_35_I": ["USMCA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_LROW_OPTION_3_ME",
    {
        "REGIONS_35_I": ["LROW"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)


@component.add(
    name="SCENARIO_PASSENGER_TRANSPORT_DEMAND_OPTION_1_ME",
    units="DMNL",
    subscripts=["TRANSPORT_POWER_TRAIN_I", "PASSENGERS_TRANSPORT_MODE_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_scenario_passenger_transport_demand_option_1_me"
    },
)
def scenario_passenger_transport_demand_option_1_me():
    """
    SCENARIO_PASSENGER_TRANSPORT_DEMAND_OPTION_1_ME
    """
    return _ext_constant_scenario_passenger_transport_demand_option_1_me()


_ext_constant_scenario_passenger_transport_demand_option_1_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_PASSENGER_TRANSPORT_DEMAND_OPTION_1_ME",
    {
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
    _root,
    {
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
    "_ext_constant_scenario_passenger_transport_demand_option_1_me",
)


@component.add(
    name="SCENARIO_PASSENGER_TRANSPORT_DEMAND_OPTION_2_ME",
    units="DMNL",
    subscripts=["TRANSPORT_POWER_TRAIN_I", "PASSENGERS_TRANSPORT_MODE_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_scenario_passenger_transport_demand_option_2_me"
    },
)
def scenario_passenger_transport_demand_option_2_me():
    """
    SCENARIO_PASSENGER_TRANSPORT_DEMAND_OPTION_2_ME
    """
    return _ext_constant_scenario_passenger_transport_demand_option_2_me()


_ext_constant_scenario_passenger_transport_demand_option_2_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_PASSENGER_TRANSPORT_DEMAND_OPTION_2_ME",
    {
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
    _root,
    {
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
    "_ext_constant_scenario_passenger_transport_demand_option_2_me",
)


@component.add(
    name="SCENARIO_PASSENGER_TRANSPORT_DEMAND_OPTION_3_ME",
    units="DMNL",
    subscripts=["TRANSPORT_POWER_TRAIN_I", "PASSENGERS_TRANSPORT_MODE_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_scenario_passenger_transport_demand_option_3_me"
    },
)
def scenario_passenger_transport_demand_option_3_me():
    """
    SCENARIO_PASSENGER_TRANSPORT_DEMAND_OPTION_3_ME
    """
    return _ext_constant_scenario_passenger_transport_demand_option_3_me()


_ext_constant_scenario_passenger_transport_demand_option_3_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_PASSENGER_TRANSPORT_DEMAND_OPTION_3_ME",
    {
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
    _root,
    {
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
    "_ext_constant_scenario_passenger_transport_demand_option_3_me",
)


@component.add(
    name="SCENARIO_PLANT_BASED_100_OPTION_3_ME",
    units="kg/(Year*people)",
    subscripts=["REGIONS_9_I", "FOODS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_scenario_plant_based_100_option_3_me"},
)
def scenario_plant_based_100_option_3_me():
    """
    SCENARIO_PLANT_BASED_100_OPTION_3_ME
    """
    return _ext_constant_scenario_plant_based_100_option_3_me()


_ext_constant_scenario_plant_based_100_option_3_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_PLANT_BASED_100_OPTION_3_ME",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "FOODS_I": _subscript_dict["FOODS_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "FOODS_I": _subscript_dict["FOODS_I"],
    },
    "_ext_constant_scenario_plant_based_100_option_3_me",
)


@component.add(
    name="SCENARIO_PROTRA_EXPANSION_OPTION_1_ME",
    units="DMNL",
    subscripts=["REGIONS_9_I", "NRG_PROTRA_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_scenario_protra_expansion_option_1_me"},
)
def scenario_protra_expansion_option_1_me():
    """
    SCENARIO_PROTRA_EXPANSION_OPTION_1_ME
    """
    return _ext_constant_scenario_protra_expansion_option_1_me()


_ext_constant_scenario_protra_expansion_option_1_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_PROTRA_EXPANSION_OPTION_1_ME*",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
    },
    "_ext_constant_scenario_protra_expansion_option_1_me",
)


@component.add(
    name="SCENARIO_PROTRA_EXPANSION_OPTION_2_ME",
    units="DMNL",
    subscripts=["REGIONS_9_I", "NRG_PROTRA_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_scenario_protra_expansion_option_2_me"},
)
def scenario_protra_expansion_option_2_me():
    """
    SCENARIO_PROTRA_EXPANSION_OPTION_2_ME
    """
    return _ext_constant_scenario_protra_expansion_option_2_me()


_ext_constant_scenario_protra_expansion_option_2_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_PROTRA_EXPANSION_OPTION_2_ME*",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
    },
    "_ext_constant_scenario_protra_expansion_option_2_me",
)


@component.add(
    name="SCENARIO_PROTRA_EXPANSION_OPTION_3_ME",
    units="DMNL",
    subscripts=["REGIONS_9_I", "NRG_PROTRA_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_scenario_protra_expansion_option_3_me"},
)
def scenario_protra_expansion_option_3_me():
    """
    SCENARIO_PROTRA_EXPANSION_OPTION_3_ME
    """
    return _ext_constant_scenario_protra_expansion_option_3_me()


_ext_constant_scenario_protra_expansion_option_3_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_PROTRA_EXPANSION_OPTION_3_ME*",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
    },
    "_ext_constant_scenario_protra_expansion_option_3_me",
)


@component.add(
    name="SCENARIO_SELECT_CHANGE_TO_REGENERATIVE_AGRICULTURE_OPTION_1_ME",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_scenario_select_change_to_regenerative_agriculture_option_1_me"
    },
)
def scenario_select_change_to_regenerative_agriculture_option_1_me():
    """
    SCENARIO_SELECT_CHANGE_TO_REGENERATIVE_AGRICULTURE_OPTION_1_ME
    """
    return (
        _ext_constant_scenario_select_change_to_regenerative_agriculture_option_1_me()
    )


_ext_constant_scenario_select_change_to_regenerative_agriculture_option_1_me = (
    ExtConstant(
        "scenario_parameters/scenario_parameters.xlsx",
        "data_model_explorer",
        "SCENARIO_SELECT_CHANGE_TO_REGENERATIVE_AGRICULTURE_OPTION_1_ME*",
        {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
        _root,
        {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
        "_ext_constant_scenario_select_change_to_regenerative_agriculture_option_1_me",
    )
)


@component.add(
    name="SCENARIO_SELECT_CHANGE_TO_REGENERATIVE_AGRICULTURE_OPTION_2_ME",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_scenario_select_change_to_regenerative_agriculture_option_2_me"
    },
)
def scenario_select_change_to_regenerative_agriculture_option_2_me():
    """
    SCENARIO_SELECT_CHANGE_TO_REGENERATIVE_AGRICULTURE_OPTION_2_ME
    """
    return (
        _ext_constant_scenario_select_change_to_regenerative_agriculture_option_2_me()
    )


_ext_constant_scenario_select_change_to_regenerative_agriculture_option_2_me = (
    ExtConstant(
        "scenario_parameters/scenario_parameters.xlsx",
        "data_model_explorer",
        "SCENARIO_SELECT_CHANGE_TO_REGENERATIVE_AGRICULTURE_OPTION_2_ME*",
        {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
        _root,
        {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
        "_ext_constant_scenario_select_change_to_regenerative_agriculture_option_2_me",
    )
)


@component.add(
    name="SCENARIO_SELECT_CHANGE_TO_REGENERATIVE_AGRICULTURE_OPTION_3_ME",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_scenario_select_change_to_regenerative_agriculture_option_3_me"
    },
)
def scenario_select_change_to_regenerative_agriculture_option_3_me():
    """
    SCENARIO_SELECT_CHANGE_TO_REGENERATIVE_AGRICULTURE_OPTION_3_ME
    """
    return (
        _ext_constant_scenario_select_change_to_regenerative_agriculture_option_3_me()
    )


_ext_constant_scenario_select_change_to_regenerative_agriculture_option_3_me = (
    ExtConstant(
        "scenario_parameters/scenario_parameters.xlsx",
        "data_model_explorer",
        "SCENARIO_SELECT_CHANGE_TO_REGENERATIVE_AGRICULTURE_OPTION_3_ME*",
        {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
        _root,
        {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
        "_ext_constant_scenario_select_change_to_regenerative_agriculture_option_3_me",
    )
)


@component.add(
    name="SCENARIO_SHARE_DIETS_ME",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_scenario_share_diets_me"},
)
def scenario_share_diets_me():
    """
    Percent of population
    """
    return _ext_constant_scenario_share_diets_me()


_ext_constant_scenario_share_diets_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_SHARE_DIETS_ME",
    {},
    _root,
    {},
    "_ext_constant_scenario_share_diets_me",
)


@component.add(
    name="SCENARIO_TARGET_SHARE_BIOENERGY_IN_FOSSIL_LIQUIDS_AND_GASES_OPTION_1_ME",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_scenario_target_share_bioenergy_in_fossil_liquids_and_gases_option_1_me"
    },
)
def scenario_target_share_bioenergy_in_fossil_liquids_and_gases_option_1_me():
    """
    SCENARIO_TARGET_SHARE_BIOENERGY_IN_FOSSIL_LIQUIDS_AND_GASES_OPTION_1_ME
    """
    return (
        _ext_constant_scenario_target_share_bioenergy_in_fossil_liquids_and_gases_option_1_me()
    )


_ext_constant_scenario_target_share_bioenergy_in_fossil_liquids_and_gases_option_1_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_TARGET_SHARE_BIOENERGY_IN_FOSSIL_LIQUIDS_AND_GASES_OPTION_1_ME*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_scenario_target_share_bioenergy_in_fossil_liquids_and_gases_option_1_me",
)


@component.add(
    name="SCENARIO_TARGET_SHARE_BIOENERGY_IN_FOSSIL_LIQUIDS_AND_GASES_OPTION_2_ME",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_scenario_target_share_bioenergy_in_fossil_liquids_and_gases_option_2_me"
    },
)
def scenario_target_share_bioenergy_in_fossil_liquids_and_gases_option_2_me():
    """
    SCENARIO_TARGET_SHARE_BIOENERGY_IN_FOSSIL_LIQUIDS_AND_GASES_OPTION_2_ME
    """
    return (
        _ext_constant_scenario_target_share_bioenergy_in_fossil_liquids_and_gases_option_2_me()
    )


_ext_constant_scenario_target_share_bioenergy_in_fossil_liquids_and_gases_option_2_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_TARGET_SHARE_BIOENERGY_IN_FOSSIL_LIQUIDS_AND_GASES_OPTION_2_ME*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_scenario_target_share_bioenergy_in_fossil_liquids_and_gases_option_2_me",
)


@component.add(
    name="SCENARIO_TARGET_SHARE_BIOENERGY_IN_FOSSIL_LIQUIDS_AND_GASES_OPTION_3_ME",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_scenario_target_share_bioenergy_in_fossil_liquids_and_gases_option_3_me"
    },
)
def scenario_target_share_bioenergy_in_fossil_liquids_and_gases_option_3_me():
    """
    SCENARIO_TARGET_SHARE_BIOENERGY_IN_FOSSIL_LIQUIDS_AND_GASES_OPTION_3_ME
    """
    return (
        _ext_constant_scenario_target_share_bioenergy_in_fossil_liquids_and_gases_option_3_me()
    )


_ext_constant_scenario_target_share_bioenergy_in_fossil_liquids_and_gases_option_3_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_TARGET_SHARE_BIOENERGY_IN_FOSSIL_LIQUIDS_AND_GASES_OPTION_3_ME*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_scenario_target_share_bioenergy_in_fossil_liquids_and_gases_option_3_me",
)


@component.add(
    name="SCENARIO_URANIUM_MAXIMUM_SUPPLY_CURVE_OPTION_1_ME",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_scenario_uranium_maximum_supply_curve_option_1_me"
    },
)
def scenario_uranium_maximum_supply_curve_option_1_me():
    return _ext_constant_scenario_uranium_maximum_supply_curve_option_1_me()


_ext_constant_scenario_uranium_maximum_supply_curve_option_1_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_URANIUM_MAXIMUM_SUPPLY_CURVE_OPTION_1_ME",
    {},
    _root,
    {},
    "_ext_constant_scenario_uranium_maximum_supply_curve_option_1_me",
)


@component.add(
    name="SCENARIO_URANIUM_MAXIMUM_SUPPLY_CURVE_OPTION_2_ME",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_scenario_uranium_maximum_supply_curve_option_2_me"
    },
)
def scenario_uranium_maximum_supply_curve_option_2_me():
    return _ext_constant_scenario_uranium_maximum_supply_curve_option_2_me()


_ext_constant_scenario_uranium_maximum_supply_curve_option_2_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_URANIUM_MAXIMUM_SUPPLY_CURVE_OPTION_2_ME",
    {},
    _root,
    {},
    "_ext_constant_scenario_uranium_maximum_supply_curve_option_2_me",
)


@component.add(
    name="SCENARIO_URANIUM_MAXIMUM_SUPPLY_CURVE_OPTION_3_ME",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_scenario_uranium_maximum_supply_curve_option_3_me"
    },
)
def scenario_uranium_maximum_supply_curve_option_3_me():
    return _ext_constant_scenario_uranium_maximum_supply_curve_option_3_me()


_ext_constant_scenario_uranium_maximum_supply_curve_option_3_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_URANIUM_MAXIMUM_SUPPLY_CURVE_OPTION_3_ME",
    {},
    _root,
    {},
    "_ext_constant_scenario_uranium_maximum_supply_curve_option_3_me",
)


@component.add(
    name="SCENARIO_WORKING_TIME_OPTION_1_ME",
    units="1/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_scenario_working_time_option_1_me"},
)
def scenario_working_time_option_1_me():
    """
    SCENARIO_WORKING_TIME_OPTION_1_ME
    """
    return _ext_constant_scenario_working_time_option_1_me()


_ext_constant_scenario_working_time_option_1_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_WORKING_TIME_OPTION_1_ME",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
    "_ext_constant_scenario_working_time_option_1_me",
)


@component.add(
    name="SCENARIO_WORKING_TIME_OPTION_2_ME",
    units="1/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_scenario_working_time_option_2_me"},
)
def scenario_working_time_option_2_me():
    """
    SCENARIO_WORKING_TIME_OPTION_2_ME
    """
    return _ext_constant_scenario_working_time_option_2_me()


_ext_constant_scenario_working_time_option_2_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_WORKING_TIME_OPTION_2_ME",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
    "_ext_constant_scenario_working_time_option_2_me",
)


@component.add(
    name="SCENARIO_WORKING_TIME_OPTION_3_ME",
    units="1/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_scenario_working_time_option_3_me"},
)
def scenario_working_time_option_3_me():
    """
    SCENARIO_WORKING_TIME_OPTION_3_ME
    """
    return _ext_constant_scenario_working_time_option_3_me()


_ext_constant_scenario_working_time_option_3_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_WORKING_TIME_OPTION_3_ME",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
    "_ext_constant_scenario_working_time_option_3_me",
)


@component.add(
    name="SELECT_CHANGE_TO_REGENERATIVE_AGRICULTURE_ME",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_select_change_to_regenerative_agriculture_me"
    },
)
def select_change_to_regenerative_agriculture_me():
    """
    1: No policy 2: Medium level of policy implementation 3: High level of policy implementation
    """
    return _ext_constant_select_change_to_regenerative_agriculture_me()


_ext_constant_select_change_to_regenerative_agriculture_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "inputs_model_explorer",
    "SELECT_CHANGE_TO_REGENERATIVE_AGRICULTURE_ME",
    {},
    _root,
    {},
    "_ext_constant_select_change_to_regenerative_agriculture_me",
)


@component.add(
    name="SELECT_CLIMATE_SENSITIVITY_ME",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_select_climate_sensitivity_me"},
)
def select_climate_sensitivity_me():
    """
    1: Application of 2.5 as climate sensitivity value 2: Application of 3 as climate sensitivity value 3: Application of 4 as climate sensitivity value
    """
    return _ext_constant_select_climate_sensitivity_me()


_ext_constant_select_climate_sensitivity_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "inputs_model_explorer",
    "SELECT_CLIMATE_SENSITIVITY_ME",
    {},
    _root,
    {},
    "_ext_constant_select_climate_sensitivity_me",
)


@component.add(
    name="SELECT_DEBT_INTEREST_RATE_TARGET_ME",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_select_debt_interest_rate_target_me"},
)
def select_debt_interest_rate_target_me():
    """
    1: Less than current debt interest rate 2: Current debt interest rate 3: More than current debt interest rate
    """
    return _ext_constant_select_debt_interest_rate_target_me()


_ext_constant_select_debt_interest_rate_target_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "inputs_model_explorer",
    "SELECT_DEBT_INTEREST_RATE_TARGET_ME",
    {},
    _root,
    {},
    "_ext_constant_select_debt_interest_rate_target_me",
)


@component.add(
    name="SELECT_ENERGY_EFFICIENCY_ANNUAL_IMPROVEMENT_ME",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_select_energy_efficiency_annual_improvement_me"
    },
)
def select_energy_efficiency_annual_improvement_me():
    """
    1: Less than current energy efficiency improvement 2: Current trends energy efficiency improvement 3: More than current energy efficiency improvement
    """
    return _ext_constant_select_energy_efficiency_annual_improvement_me()


_ext_constant_select_energy_efficiency_annual_improvement_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "inputs_model_explorer",
    "SELECT_ENERGY_EFFICIENCY_ANNUAL_IMPROVEMENT_ME",
    {},
    _root,
    {},
    "_ext_constant_select_energy_efficiency_annual_improvement_me",
)


@component.add(
    name="SELECT_FERTILITY_RATES_ME",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_select_fertility_rates_me"},
)
def select_fertility_rates_me():
    """
    1: LOW FERTILITY RATES 2: MEDIUM FERTILITY RATES 3: HIGH FERTILITY RATES
    """
    return _ext_constant_select_fertility_rates_me()


_ext_constant_select_fertility_rates_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "inputs_model_explorer",
    "SELECT_FERTILITY_RATES_ME",
    {},
    _root,
    {},
    "_ext_constant_select_fertility_rates_me",
)


@component.add(
    name="SELECT_FINAL_GENDER_PARITY_INDEX_ME",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_select_final_gender_parity_index_me"},
)
def select_final_gender_parity_index_me():
    """
    1: No policy (current trends) 2: Medium level of policy implementation 3: Total gender parity in education
    """
    return _ext_constant_select_final_gender_parity_index_me()


_ext_constant_select_final_gender_parity_index_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "inputs_model_explorer",
    "SELECT_FINAL_GENDER_PARITY_INDEX_ME",
    {},
    _root,
    {},
    "_ext_constant_select_final_gender_parity_index_me",
)


@component.add(
    name="SELECT_FORESTRY_SELF_SUFFICIENCY",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_select_forestry_self_sufficiency"},
)
def select_forestry_self_sufficiency():
    """
    1: Forestry explotation for other regions allowed 2: Only 50% of explotation for other regions allowed 3: Self-Suficient forestrexplotation
    """
    return _ext_constant_select_forestry_self_sufficiency()


_ext_constant_select_forestry_self_sufficiency = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "inputs_model_explorer",
    "SELECT_FORESTRY_SELF_SUFFICIENCY",
    {},
    _root,
    {},
    "_ext_constant_select_forestry_self_sufficiency",
)


@component.add(
    name="SELECT_GOVERNMENT_BUDGET_BALANCE_TO_GDP_OBJECTIVE_TARGET_ME",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_select_government_budget_balance_to_gdp_objective_target_me"
    },
)
def select_government_budget_balance_to_gdp_objective_target_me():
    """
    1: Less than current GDP objetive 2: Current GDP objetive 3: More than current GDP objetive
    """
    return _ext_constant_select_government_budget_balance_to_gdp_objective_target_me()


_ext_constant_select_government_budget_balance_to_gdp_objective_target_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "inputs_model_explorer",
    "SELECT_GOVERNMENT_BUDGET_BALANCE_TO_GDP_OBJECTIVE_TARGET_ME",
    {},
    _root,
    {},
    "_ext_constant_select_government_budget_balance_to_gdp_objective_target_me",
)


@component.add(
    name="SELECT_LAND_PROTECTION_BY_POLICY_ME",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_select_land_protection_by_policy_me"},
)
def select_land_protection_by_policy_me():
    """
    1: No policy 2: Medium level of policy implementation 3: High level of policy implementation
    """
    return _ext_constant_select_land_protection_by_policy_me()


_ext_constant_select_land_protection_by_policy_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "inputs_model_explorer",
    "SELECT_LAND_PROTECTION_BY_POLICY_ME",
    {},
    _root,
    {},
    "_ext_constant_select_land_protection_by_policy_me",
)


@component.add(
    name="SELECT_MANURE_MANAGEMENT_SYSTEM_ME",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_select_manure_management_system_me"},
)
def select_manure_management_system_me():
    """
    1: No policy 2: Medium level of policy implementation 3: High level of policy implementation
    """
    return _ext_constant_select_manure_management_system_me()


_ext_constant_select_manure_management_system_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "inputs_model_explorer",
    "SELECT_MANURE_MANAGEMENT_SYSTEM_ME",
    {},
    _root,
    {},
    "_ext_constant_select_manure_management_system_me",
)


@component.add(
    name="SELECT_OIL_RESOURCE_ME",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_select_oil_resource_me"},
)
def select_oil_resource_me():
    """
    1: Low level of oil resources 2: Medium level of oil resources 3: High level of oil resources
    """
    return _ext_constant_select_oil_resource_me()


_ext_constant_select_oil_resource_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "inputs_model_explorer",
    "SELECT_OIL_RESOURCE_ME",
    {},
    _root,
    {},
    "_ext_constant_select_oil_resource_me",
)


@component.add(
    name="SELECT_PASSENGER_TRANSPORT_DEMAND_MODAL_SHARE_ME",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_select_passenger_transport_demand_modal_share_me"
    },
)
def select_passenger_transport_demand_modal_share_me():
    """
    1: No policy 2: Medium level of policy implementation 3: High level of policy implementation
    """
    return _ext_constant_select_passenger_transport_demand_modal_share_me()


_ext_constant_select_passenger_transport_demand_modal_share_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "inputs_model_explorer",
    "SELECT_PASSENGER_TRANSPORT_DEMAND_MODAL_SHARE_ME",
    {},
    _root,
    {},
    "_ext_constant_select_passenger_transport_demand_modal_share_me",
)


@component.add(
    name="SELECT_PERCENTAGE_FE_LIQUID_SUBSTITUTED_BY_H2_SYNTHETIC_LIQUID_ME",
    units="DMML",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_select_percentage_fe_liquid_substituted_by_h2_synthetic_liquid_me"
    },
)
def select_percentage_fe_liquid_substituted_by_h2_synthetic_liquid_me():
    """
    1: LOW LEVEL OF POLICY IMPLEMENTATION 2: MEEDIUM LEVEL OF POLICY IMPLEMENTATION 3: HIGH LEVEL OF POLICY IMPLEMENTATION
    """
    return (
        _ext_constant_select_percentage_fe_liquid_substituted_by_h2_synthetic_liquid_me()
    )


_ext_constant_select_percentage_fe_liquid_substituted_by_h2_synthetic_liquid_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "inputs_model_explorer",
    "SELECT_PERCENTAGE_FE_LIQUID_SUBSTITUTED_BY_H2_SYNTHETIC_LIQUID_ME",
    {},
    _root,
    {},
    "_ext_constant_select_percentage_fe_liquid_substituted_by_h2_synthetic_liquid_me",
)


@component.add(
    name="SELECT_PROTRA_CAPACITY_EXPANSION_PRIORITIES_VECTOR_ME",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_select_protra_capacity_expansion_priorities_vector_me"
    },
)
def select_protra_capacity_expansion_priorities_vector_me():
    """
    1: Back to fossil and uranium energies 2: Current trends 3: Rapid implementaion of renewable energies
    """
    return _ext_constant_select_protra_capacity_expansion_priorities_vector_me()


_ext_constant_select_protra_capacity_expansion_priorities_vector_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "inputs_model_explorer",
    "SELECT_PROTRA_CAPACITY_EXPANSION_PRIORITIES_VECTOR_ME",
    {},
    _root,
    {},
    "_ext_constant_select_protra_capacity_expansion_priorities_vector_me",
)


@component.add(
    name="SELECT_RCP_GHG_EMISSIONS_ME",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_select_rcp_ghg_emissions_me"},
)
def select_rcp_ghg_emissions_me():
    """
    1: APPLICATION OF RCP 2.6 2: APPLICATION OF RCP 4.5 3: APPLICATION OF RCP 6 4: APPLICATION OF RCP 8.5
    """
    return _ext_constant_select_rcp_ghg_emissions_me()


_ext_constant_select_rcp_ghg_emissions_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "inputs_model_explorer",
    "SELECT_RCP_GHG_EMISSIONS_ME",
    {},
    _root,
    {},
    "_ext_constant_select_rcp_ghg_emissions_me",
)


@component.add(
    name="SELECT_REDUCTION_PASSENGER_TRANSPORT_DEMAND_ME",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_select_reduction_passenger_transport_demand_me"
    },
)
def select_reduction_passenger_transport_demand_me():
    """
    1: No policy 2: Medium level of policy implementation 3: High level of policy implementation
    """
    return _ext_constant_select_reduction_passenger_transport_demand_me()


_ext_constant_select_reduction_passenger_transport_demand_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "inputs_model_explorer",
    "SELECT_REDUCTION_PASSENGER_TRANSPORT_DEMAND_ME",
    {},
    _root,
    {},
    "_ext_constant_select_reduction_passenger_transport_demand_me",
)


@component.add(
    name="SELECT_TARGET_SHARE_BIOENERGY_IN_FOSSIL_LIQUIDS_AND_GASES_ME",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_select_target_share_bioenergy_in_fossil_liquids_and_gases_me"
    },
)
def select_target_share_bioenergy_in_fossil_liquids_and_gases_me():
    """
    1: No policy 2: Medium level of policy implementation 3: High level of policy implementation
    """
    return _ext_constant_select_target_share_bioenergy_in_fossil_liquids_and_gases_me()


_ext_constant_select_target_share_bioenergy_in_fossil_liquids_and_gases_me = (
    ExtConstant(
        "scenario_parameters/scenario_parameters.xlsx",
        "inputs_model_explorer",
        "SELECT_TARGET_SHARE_BIOENERGY_IN_FOSSIL_LIQUIDS_AND_GASES_ME",
        {},
        _root,
        {},
        "_ext_constant_select_target_share_bioenergy_in_fossil_liquids_and_gases_me",
    )
)


@component.add(
    name="SELECT_TIPE_DIETS_ME",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_select_tipe_diets_me"},
)
def select_tipe_diets_me():
    """
    1: 30% of population with flexitarian diet 2: Baseline diet patterns 3: 30% of population with 100% plant based diet
    """
    return _ext_constant_select_tipe_diets_me()


_ext_constant_select_tipe_diets_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "inputs_model_explorer",
    "SELECT_SHARE_OF_CHANGE_TO_POLICY_DIET_ME",
    {},
    _root,
    {},
    "_ext_constant_select_tipe_diets_me",
)


@component.add(
    name="SELECT_URANIUM_MAXIMUM_SUPPLY_CURVE_ME",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_select_uranium_maximum_supply_curve_me"},
)
def select_uranium_maximum_supply_curve_me():
    """
    1: Unlimited uranium supply 2: Medium level uranium resources 3: High level uranium resources
    """
    return _ext_constant_select_uranium_maximum_supply_curve_me()


_ext_constant_select_uranium_maximum_supply_curve_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "inputs_model_explorer",
    "SELECT_URANIUM_MAXIMUM_SUPPLY_CURVE_ME",
    {},
    _root,
    {},
    "_ext_constant_select_uranium_maximum_supply_curve_me",
)


@component.add(
    name="SELECT_WORKING_TIME_VARIATION_ME",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_select_working_time_variation_me"},
)
def select_working_time_variation_me():
    """
    1: Less than current working time 2: Current working time 3: More than current working time
    """
    return _ext_constant_select_working_time_variation_me()


_ext_constant_select_working_time_variation_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "inputs_model_explorer",
    "SELECT_WORKING_TIME_VARIATION_ME",
    {},
    _root,
    {},
    "_ext_constant_select_working_time_variation_me",
)


@component.add(
    name="SWITCH_MODEL_EXPLORER",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_model_explorer"},
)
def switch_model_explorer():
    """
    Switch for the model explorer. OFF=0 ON=1
    """
    return _ext_constant_switch_model_explorer()


_ext_constant_switch_model_explorer = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "inputs_model_explorer",
    "SWITCH_MODEL_EXPLORER",
    {},
    _root,
    {},
    "_ext_constant_switch_model_explorer",
)
