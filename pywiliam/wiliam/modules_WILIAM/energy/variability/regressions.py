"""
Module energy.variability.regressions
Translated using PySD version 3.10.0
"""


@component.add(
    name="CF_PHS_storage",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def cf_phs_storage():
    """
    capacity factor of pumped hydro storage - constant for now might change with new regression approach
    """
    return xr.DataArray(
        0.1, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
    )


@component.add(
    name="CF_PROSTO",
    units="DMNL",
    subscripts=["REGIONS_9_I", "NRG_PROSTO_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cf_v2g_storage_9r": 1,
        "cf_phs_storage": 1,
        "cf_stationary_batteries": 1,
    },
)
def cf_prosto():
    """
    Capacity factor of utility-scale storage facilities.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "NRG_PROSTO_I": _subscript_dict["NRG_PROSTO_I"],
        },
        ["REGIONS_9_I", "NRG_PROSTO_I"],
    )
    value.loc[:, ["PROSTO_V2G"]] = (
        cf_v2g_storage_9r().expand_dims({"NRG_PRO_I": ["PROSTO_V2G"]}, 1).values
    )
    value.loc[:, ["PROSTO_PHS"]] = (
        cf_phs_storage().expand_dims({"NRG_PRO_I": ["PROSTO_PHS"]}, 1).values
    )
    value.loc[:, ["PROSTO_STATIONARY_BATTERIES"]] = (
        cf_stationary_batteries()
        .expand_dims({"NRG_PRO_I": ["PROSTO_STATIONARY_BATTERIES"]}, 1)
        .values
    )
    return value


@component.add(
    name="CF_stationary_batteries",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def cf_stationary_batteries():
    """
    capacity factor of staitonary batteries - constant for now
    """
    return xr.DataArray(
        0.1, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
    )


@component.add(
    name="CF_V2G_storage",
    units="DMNL",
    subscripts=["REGIONS_35_I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def cf_v2g_storage():
    """
    Capacity factor of V2G, defined as output from storage (after the charger) divided by the power of V2G.
    """
    return xr.DataArray(
        0.01, {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]}, ["REGIONS_35_I"]
    )


@component.add(
    name="CF_V2G_storage_9R",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"cf_v2g_storage": 2},
)
def cf_v2g_storage_9r():
    value = xr.DataArray(
        np.nan, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
    )
    value.loc[_subscript_dict["REGIONS_8_I"]] = (
        cf_v2g_storage()
        .loc[_subscript_dict["REGIONS_8_I"]]
        .rename({"REGIONS_35_I": "REGIONS_8_I"})
        .values
    )
    value.loc[["EU27"]] = sum(
        cf_v2g_storage()
        .loc[_subscript_dict["REGIONS_EU27_I"]]
        .rename({"REGIONS_35_I": "REGIONS_EU27_I!"}),
        dim=["REGIONS_EU27_I!"],
    ) / len(
        xr.DataArray(
            np.arange(1, len(_subscript_dict["REGIONS_EU27_I"]) + 1),
            {"REGIONS_EU27_I": _subscript_dict["REGIONS_EU27_I"]},
            ["REGIONS_EU27_I"],
        )
    )
    return value


@component.add(
    name="check_ranges",
    units="DMNL",
    subscripts=["REGIONS_9_I", "BASIC_PREDICTORS_NGR_VARIABILITY_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "predictors_all": 2,
        "minimum_predictors_variability_regression": 1,
        "maximum_predictors_variability_regression": 1,
    },
)
def check_ranges():
    """
    Check if predictors are within the range (0) or not (1)
    """
    return if_then_else(
        np.logical_or(
            predictors_all()
            .loc[:, _subscript_dict["BASIC_PREDICTORS_NGR_VARIABILITY_I"]]
            .rename(
                {"PREDICTORS_NGR_VARIABILITY_I": "BASIC_PREDICTORS_NGR_VARIABILITY_I"}
            )
            < minimum_predictors_variability_regression(),
            predictors_all()
            .loc[:, _subscript_dict["BASIC_PREDICTORS_NGR_VARIABILITY_I"]]
            .rename(
                {"PREDICTORS_NGR_VARIABILITY_I": "BASIC_PREDICTORS_NGR_VARIABILITY_I"}
            )
            > maximum_predictors_variability_regression(),
        ),
        lambda: xr.DataArray(
            1,
            {
                "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                "BASIC_PREDICTORS_NGR_VARIABILITY_I": _subscript_dict[
                    "BASIC_PREDICTORS_NGR_VARIABILITY_I"
                ],
            },
            ["REGIONS_9_I", "BASIC_PREDICTORS_NGR_VARIABILITY_I"],
        ),
        lambda: xr.DataArray(
            0,
            {
                "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                "BASIC_PREDICTORS_NGR_VARIABILITY_I": _subscript_dict[
                    "BASIC_PREDICTORS_NGR_VARIABILITY_I"
                ],
            },
            ["REGIONS_9_I", "BASIC_PREDICTORS_NGR_VARIABILITY_I"],
        ),
    )


@component.add(
    name="checking_linear_regression_models_energy_variability",
    units="DMNL",
    subscripts=["REGIONS_9_I", "OUTPUTS_NGR_VARIABILITY_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "energy_variability_linear_regression_intercept": 3,
        "individual_linear_regression_terms_energy_variability": 3,
    },
)
def checking_linear_regression_models_energy_variability():
    """
    Calculation of the regression model (independent term + sum(Coefficients * predictors)) to consider the variability of renewable energy. For linear functions, it is assumed a range to be between [0, 1], in order to avoid errors.
    """
    return if_then_else(
        energy_variability_linear_regression_intercept()
        + sum(
            individual_linear_regression_terms_energy_variability().rename(
                {"PREDICTORS_NGR_VARIABILITY_I": "PREDICTORS_NGR_VARIABILITY_I!"}
            ),
            dim=["PREDICTORS_NGR_VARIABILITY_I!"],
        ).transpose("OUTPUTS_NGR_VARIABILITY_I", "REGIONS_9_I")
        > 1,
        lambda: xr.DataArray(
            1,
            {
                "OUTPUTS_NGR_VARIABILITY_I": _subscript_dict[
                    "OUTPUTS_NGR_VARIABILITY_I"
                ],
                "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            },
            ["OUTPUTS_NGR_VARIABILITY_I", "REGIONS_9_I"],
        ),
        lambda: if_then_else(
            energy_variability_linear_regression_intercept()
            + sum(
                individual_linear_regression_terms_energy_variability().rename(
                    {"PREDICTORS_NGR_VARIABILITY_I": "PREDICTORS_NGR_VARIABILITY_I!"}
                ),
                dim=["PREDICTORS_NGR_VARIABILITY_I!"],
            ).transpose("OUTPUTS_NGR_VARIABILITY_I", "REGIONS_9_I")
            < 0,
            lambda: xr.DataArray(
                0,
                {
                    "OUTPUTS_NGR_VARIABILITY_I": _subscript_dict[
                        "OUTPUTS_NGR_VARIABILITY_I"
                    ],
                    "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                },
                ["OUTPUTS_NGR_VARIABILITY_I", "REGIONS_9_I"],
            ),
            lambda: energy_variability_linear_regression_intercept()
            + sum(
                individual_linear_regression_terms_energy_variability().rename(
                    {"PREDICTORS_NGR_VARIABILITY_I": "PREDICTORS_NGR_VARIABILITY_I!"}
                ),
                dim=["PREDICTORS_NGR_VARIABILITY_I!"],
            ).transpose("OUTPUTS_NGR_VARIABILITY_I", "REGIONS_9_I"),
        ),
    ).transpose("REGIONS_9_I", "OUTPUTS_NGR_VARIABILITY_I")


@component.add(
    name="checking_logistic_regression_models_energy_variability",
    units="DMNL",
    subscripts=["REGIONS_9_I", "OUTPUTS_NGR_VARIABILITY_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "energy_variability_logistic_regression_intercept": 3,
        "individual_logistic_regression_terms_energy_variability": 3,
    },
)
def checking_logistic_regression_models_energy_variability():
    """
    Calculation of the regression model (independent term + sum(Coefficients * predictors)) to consider the variability of renewable energy. For logistic functions, it is assumed a range to be between [-10, 10], in order to avoid errors.
    """
    return if_then_else(
        energy_variability_logistic_regression_intercept()
        + sum(
            individual_logistic_regression_terms_energy_variability().rename(
                {"PREDICTORS_NGR_VARIABILITY_I": "PREDICTORS_NGR_VARIABILITY_I!"}
            ),
            dim=["PREDICTORS_NGR_VARIABILITY_I!"],
        ).transpose("OUTPUTS_NGR_VARIABILITY_I", "REGIONS_9_I")
        > 10,
        lambda: xr.DataArray(
            10,
            {
                "OUTPUTS_NGR_VARIABILITY_I": _subscript_dict[
                    "OUTPUTS_NGR_VARIABILITY_I"
                ],
                "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            },
            ["OUTPUTS_NGR_VARIABILITY_I", "REGIONS_9_I"],
        ),
        lambda: if_then_else(
            energy_variability_logistic_regression_intercept()
            + sum(
                individual_logistic_regression_terms_energy_variability().rename(
                    {"PREDICTORS_NGR_VARIABILITY_I": "PREDICTORS_NGR_VARIABILITY_I!"}
                ),
                dim=["PREDICTORS_NGR_VARIABILITY_I!"],
            ).transpose("OUTPUTS_NGR_VARIABILITY_I", "REGIONS_9_I")
            < -10,
            lambda: xr.DataArray(
                -10,
                {
                    "OUTPUTS_NGR_VARIABILITY_I": _subscript_dict[
                        "OUTPUTS_NGR_VARIABILITY_I"
                    ],
                    "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                },
                ["OUTPUTS_NGR_VARIABILITY_I", "REGIONS_9_I"],
            ),
            lambda: energy_variability_logistic_regression_intercept()
            + sum(
                individual_logistic_regression_terms_energy_variability().rename(
                    {"PREDICTORS_NGR_VARIABILITY_I": "PREDICTORS_NGR_VARIABILITY_I!"}
                ),
                dim=["PREDICTORS_NGR_VARIABILITY_I!"],
            ).transpose("OUTPUTS_NGR_VARIABILITY_I", "REGIONS_9_I"),
        ),
    ).transpose("REGIONS_9_I", "OUTPUTS_NGR_VARIABILITY_I")


@component.add(
    name="critical_min_hourly_PP2_regression",
    units="MW",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "predictor_6_chp": 10,
        "predictor_9_electric_vehicle_demand": 10,
        "predictor_11_hydrogen_fe_demand": 10,
        "predictor_7_heat_pumps": 6,
        "predictor_13_flexible_demand": 2,
        "predictor_1_protra_pp_solar": 4,
        "predictor_2_protra_pp_wind": 6,
        "predictor_3_capacity_zero_ghg_semiflex": 10,
    },
)
def critical_min_hourly_pp2_regression():
    """
    Minimumm capacity of diapatchable power plants in one hour over the year. Output in regressions with EnergyPLAN. This variable is de-normalized in the next step. R-squared (adjusted) = 0.9370
    """
    return if_then_else(
        0
        - 0.254786 * predictor_6_chp()
        - 0.00462968 * (predictor_6_chp() * predictor_9_electric_vehicle_demand())
        - 0.0048092 * (predictor_6_chp() * predictor_11_hydrogen_fe_demand())
        + 230.984 * predictor_9_electric_vehicle_demand()
        - 0.102376
        * (predictor_9_electric_vehicle_demand() * predictor_11_hydrogen_fe_demand())
        + 0.00251505
        * (predictor_7_heat_pumps() * predictor_9_electric_vehicle_demand())
        - 0.000986303 * (predictor_7_heat_pumps() * predictor_11_hydrogen_fe_demand())
        + 199.737 * predictor_11_hydrogen_fe_demand()
        - 0.000100768 * (predictor_1_protra_pp_solar() * predictor_13_flexible_demand())
        - 9.08352e-07 * (predictor_1_protra_pp_solar() * predictor_2_protra_pp_wind())
        - 0.0463001 * predictor_2_protra_pp_wind()
        + 5.7223e-07 * (predictor_2_protra_pp_wind() * predictor_6_chp())
        - 0.276016 * predictor_3_capacity_zero_ghg_semiflex()
        + 1.91542e-05 * (predictor_3_capacity_zero_ghg_semiflex() * predictor_6_chp())
        - 0.00428106
        * (
            predictor_3_capacity_zero_ghg_semiflex()
            * predictor_9_electric_vehicle_demand()
        )
        + 8.51984e-06
        * (predictor_3_capacity_zero_ghg_semiflex() * predictor_7_heat_pumps())
        - 0.00572539
        * (predictor_3_capacity_zero_ghg_semiflex() * predictor_11_hydrogen_fe_demand())
        < 0,
        lambda: xr.DataArray(
            0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
        ),
        lambda: 0
        - 0.254786 * predictor_6_chp()
        - 0.00462968 * (predictor_6_chp() * predictor_9_electric_vehicle_demand())
        - 0.0048092 * (predictor_6_chp() * predictor_11_hydrogen_fe_demand())
        + 230.984 * predictor_9_electric_vehicle_demand()
        - 0.102376
        * (predictor_9_electric_vehicle_demand() * predictor_11_hydrogen_fe_demand())
        + 0.00251505
        * (predictor_7_heat_pumps() * predictor_9_electric_vehicle_demand())
        - 0.000986303 * (predictor_7_heat_pumps() * predictor_11_hydrogen_fe_demand())
        + 199.737 * predictor_11_hydrogen_fe_demand()
        - 0.000100768 * (predictor_1_protra_pp_solar() * predictor_13_flexible_demand())
        - 9.08352e-07 * (predictor_1_protra_pp_solar() * predictor_2_protra_pp_wind())
        - 0.0463001 * predictor_2_protra_pp_wind()
        + 5.7223e-07 * (predictor_2_protra_pp_wind() * predictor_6_chp())
        - 0.276016 * predictor_3_capacity_zero_ghg_semiflex()
        + 1.91542e-05 * (predictor_3_capacity_zero_ghg_semiflex() * predictor_6_chp())
        - 0.00428106
        * (
            predictor_3_capacity_zero_ghg_semiflex()
            * predictor_9_electric_vehicle_demand()
        )
        + 8.51984e-06
        * (predictor_3_capacity_zero_ghg_semiflex() * predictor_7_heat_pumps())
        - 0.00572539
        * (
            predictor_3_capacity_zero_ghg_semiflex() * predictor_11_hydrogen_fe_demand()
        ),
    )


@component.add(
    name="critical_min_hourly_PP2_regressionExcelTerms",
    units="MW",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "predictor_6_chp": 10,
        "predictor_9_electric_vehicle_demand": 10,
        "predictor_11_hydrogen_fe_demand": 10,
        "predictor_7_heat_pumps": 6,
        "predictor_13_flexible_demand": 2,
        "predictor_1_protra_pp_solar": 4,
        "predictor_2_protra_pp_wind": 6,
        "predictor_3_capacity_zero_ghg_semiflex": 10,
    },
)
def critical_min_hourly_pp2_regressionexcelterms():
    """
    Minimumm capacity of diapatchable power plants in one hour over the year. Output in regressions with EnergyPLAN. This variable is de-normalized in the next step. R-squared (adjusted) = 0.9370
    """
    return if_then_else(
        9183.77
        - 0.5561 * predictor_6_chp()
        - 0.00244843 * (predictor_6_chp() * predictor_9_electric_vehicle_demand())
        - 0.00144543 * (predictor_6_chp() * predictor_11_hydrogen_fe_demand())
        + 151.539 * predictor_9_electric_vehicle_demand()
        + 0.466833
        * (predictor_9_electric_vehicle_demand() * predictor_11_hydrogen_fe_demand())
        + 0.00239256
        * (predictor_7_heat_pumps() * predictor_9_electric_vehicle_demand())
        + 0.000857741 * (predictor_7_heat_pumps() * predictor_11_hydrogen_fe_demand())
        + 65.1181 * predictor_11_hydrogen_fe_demand()
        - 0.000345652 * (predictor_1_protra_pp_solar() * predictor_13_flexible_demand())
        - 4.18398e-07 * (predictor_1_protra_pp_solar() * predictor_2_protra_pp_wind())
        - 0.0713645 * predictor_2_protra_pp_wind()
        + 1.35694e-06 * (predictor_2_protra_pp_wind() * predictor_6_chp())
        - 0.497365 * predictor_3_capacity_zero_ghg_semiflex()
        + 1.94319e-05 * (predictor_3_capacity_zero_ghg_semiflex() * predictor_6_chp())
        - 0.00202634
        * (
            predictor_3_capacity_zero_ghg_semiflex()
            * predictor_9_electric_vehicle_demand()
        )
        + 1.89793e-06
        * (predictor_3_capacity_zero_ghg_semiflex() * predictor_7_heat_pumps())
        - 0.00241295
        * (predictor_3_capacity_zero_ghg_semiflex() * predictor_11_hydrogen_fe_demand())
        < 0,
        lambda: xr.DataArray(
            0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
        ),
        lambda: 9183.77
        - 0.5561 * predictor_6_chp()
        - 0.00244843 * (predictor_6_chp() * predictor_9_electric_vehicle_demand())
        - 0.00144543 * (predictor_6_chp() * predictor_11_hydrogen_fe_demand())
        + 151.539 * predictor_9_electric_vehicle_demand()
        + 0.466833
        * (predictor_9_electric_vehicle_demand() * predictor_11_hydrogen_fe_demand())
        + 0.00239256
        * (predictor_7_heat_pumps() * predictor_9_electric_vehicle_demand())
        + 0.000857741 * (predictor_7_heat_pumps() * predictor_11_hydrogen_fe_demand())
        + 65.1181 * predictor_11_hydrogen_fe_demand()
        - 0.000345652 * (predictor_1_protra_pp_solar() * predictor_13_flexible_demand())
        - 4.18398e-07 * (predictor_1_protra_pp_solar() * predictor_2_protra_pp_wind())
        - 0.0713645 * predictor_2_protra_pp_wind()
        + 1.35694e-06 * (predictor_2_protra_pp_wind() * predictor_6_chp())
        - 0.497365 * predictor_3_capacity_zero_ghg_semiflex()
        + 1.94319e-05 * (predictor_3_capacity_zero_ghg_semiflex() * predictor_6_chp())
        - 0.00202634
        * (
            predictor_3_capacity_zero_ghg_semiflex()
            * predictor_9_electric_vehicle_demand()
        )
        + 1.89793e-06
        * (predictor_3_capacity_zero_ghg_semiflex() * predictor_7_heat_pumps())
        - 0.00241295
        * (
            predictor_3_capacity_zero_ghg_semiflex() * predictor_11_hydrogen_fe_demand()
        ),
    )


@component.add(
    name="critical_min_PP2_regression_ExcelTerms_scaled",
    units="MW",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "critical_min_hourly_pp2_regressionexcelterms": 1,
        "hourly_average_power_elec_demand": 1,
        "hourly_average_power_elec_demand_energyplan": 1,
    },
)
def critical_min_pp2_regression_excelterms_scaled():
    """
    Mininum dispatchable capacity (PP2 in EnergyPLAN) in one hour over the year. Output of the regression scaled from the normalized system to the regional one
    """
    return (
        critical_min_hourly_pp2_regressionexcelterms()
        * hourly_average_power_elec_demand()
        / hourly_average_power_elec_demand_energyplan()
    )


@component.add(
    name="EXOGENOUS_PREDICTORS_ENERGY_VARIABILITY_REGRESSIONS",
    units="DMNL",
    subscripts=["BASIC_PREDICTORS_NGR_VARIABILITY_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_exogenous_predictors_energy_variability_regressions"
    },
)
def exogenous_predictors_energy_variability_regressions():
    """
    INPUTS_ENERGY_VARIABILITY_REGRESSION
    """
    return _ext_constant_exogenous_predictors_energy_variability_regressions()


_ext_constant_exogenous_predictors_energy_variability_regressions = ExtConstant(
    "model_parameters/energy/energy.xlsm",
    "Common",
    "INPUTS_ENERGY_VARIABILITY_REGRESSION",
    {
        "BASIC_PREDICTORS_NGR_VARIABILITY_I": _subscript_dict[
            "BASIC_PREDICTORS_NGR_VARIABILITY_I"
        ]
    },
    _root,
    {
        "BASIC_PREDICTORS_NGR_VARIABILITY_I": _subscript_dict[
            "BASIC_PREDICTORS_NGR_VARIABILITY_I"
        ]
    },
    "_ext_constant_exogenous_predictors_energy_variability_regressions",
)


@component.add(
    name="hourly_average_power_elec_demand",
    units="MW*TWh/(TW*h)",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "legacy_elec_demand": 1,
        "unit_conversion_mw_tw": 1,
        "unit_conversion_hours_year": 1,
    },
)
def hourly_average_power_elec_demand():
    """
    1 year = 8760 hours
    """
    return legacy_elec_demand() * unit_conversion_mw_tw() / unit_conversion_hours_year()


@component.add(
    name="HOURLY_AVERAGE_POWER_ELEC_DEMAND_EnergyPLAN",
    units="MW*TWh/(TW*h)",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "legacy_elec_demand_energyplan": 1,
        "unit_conversion_mw_tw": 1,
        "unit_conversion_hours_year": 1,
    },
)
def hourly_average_power_elec_demand_energyplan():
    return (
        legacy_elec_demand_energyplan()
        * unit_conversion_mw_tw()
        / unit_conversion_hours_year()
    )


@component.add(
    name="hydrogen_CEEP_regression",
    units="TWh",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "predictor_9_electric_vehicle_demand": 10,
        "predictor_11_hydrogen_fe_demand": 8,
        "predictor_12_hydrogen_supply": 8,
        "predictor_5_heat_demand": 2,
        "predictor_1_protra_pp_solar": 8,
        "predictor_3_capacity_zero_ghg_semiflex": 12,
        "predictor_2_protra_pp_wind": 4,
        "predictor_6_chp": 2,
    },
)
def hydrogen_ceep_regression():
    """
    Hydrogen generated with overproduction (CEEP, critical excess of electricity produciton). Output in regressions with EnergyPLAN. This variable is de-normalized in the next step.
    """
    return if_then_else(
        -0.0920676
        - 0.000102589
        * (predictor_9_electric_vehicle_demand() * predictor_11_hydrogen_fe_demand())
        + 1.2852e-07
        * (predictor_9_electric_vehicle_demand() * predictor_12_hydrogen_supply())
        + 4.16058e-08 * (predictor_5_heat_demand() * predictor_12_hydrogen_supply())
        - 0.995615 * predictor_11_hydrogen_fe_demand()
        + 7.83684e-08
        * (predictor_1_protra_pp_solar() * predictor_9_electric_vehicle_demand())
        + 1.25655e-07
        * (predictor_1_protra_pp_solar() * predictor_11_hydrogen_fe_demand())
        - 1.28976e-09 * (predictor_1_protra_pp_solar() * predictor_12_hydrogen_supply())
        - 1.01834e-09
        * (predictor_1_protra_pp_solar() * predictor_3_capacity_zero_ghg_semiflex())
        + 1.32526e-07
        * (predictor_2_protra_pp_wind() * predictor_9_electric_vehicle_demand())
        - 1.85899e-09
        * (predictor_2_protra_pp_wind() * predictor_3_capacity_zero_ghg_semiflex())
        - 3.02653e-10 * (predictor_3_capacity_zero_ghg_semiflex() * predictor_6_chp())
        + 3.66111e-07
        * (
            predictor_3_capacity_zero_ghg_semiflex()
            * predictor_9_electric_vehicle_demand()
        )
        + 4.86997e-07
        * (predictor_3_capacity_zero_ghg_semiflex() * predictor_11_hydrogen_fe_demand())
        - 2.2032e-09
        * (predictor_3_capacity_zero_ghg_semiflex() * predictor_12_hydrogen_supply())
        > 0,
        lambda: xr.DataArray(
            0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
        ),
        lambda: -0.0920676
        - 0.000102589
        * (predictor_9_electric_vehicle_demand() * predictor_11_hydrogen_fe_demand())
        + 1.2852e-07
        * (predictor_9_electric_vehicle_demand() * predictor_12_hydrogen_supply())
        + 4.16058e-08 * (predictor_5_heat_demand() * predictor_12_hydrogen_supply())
        - 0.995615 * predictor_11_hydrogen_fe_demand()
        + 7.83684e-08
        * (predictor_1_protra_pp_solar() * predictor_9_electric_vehicle_demand())
        + 1.25655e-07
        * (predictor_1_protra_pp_solar() * predictor_11_hydrogen_fe_demand())
        - 1.28976e-09 * (predictor_1_protra_pp_solar() * predictor_12_hydrogen_supply())
        - 1.01834e-09
        * (predictor_1_protra_pp_solar() * predictor_3_capacity_zero_ghg_semiflex())
        + 1.32526e-07
        * (predictor_2_protra_pp_wind() * predictor_9_electric_vehicle_demand())
        - 1.85899e-09
        * (predictor_2_protra_pp_wind() * predictor_3_capacity_zero_ghg_semiflex())
        - 3.02653e-10 * (predictor_3_capacity_zero_ghg_semiflex() * predictor_6_chp())
        + 3.66111e-07
        * (
            predictor_3_capacity_zero_ghg_semiflex()
            * predictor_9_electric_vehicle_demand()
        )
        + 4.86997e-07
        * (predictor_3_capacity_zero_ghg_semiflex() * predictor_11_hydrogen_fe_demand())
        - 2.2032e-09
        * (predictor_3_capacity_zero_ghg_semiflex() * predictor_12_hydrogen_supply()),
    )


@component.add(
    name="hydrogen_CEEP_scaled",
    units="TW*h/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "hydrogen_ceep_regression": 1,
        "legacy_elec_demand": 1,
        "legacy_elec_demand_energyplan": 1,
    },
)
def hydrogen_ceep_scaled():
    """
    Hydrogen generated with overproduction (CEEP, critical excess of electricity produciton). Output of the regression scaled from the normalized system to the regional one
    """
    return (
        hydrogen_ceep_regression()
        * legacy_elec_demand()
        / legacy_elec_demand_energyplan()
    )


@component.add(
    name="individual_linear_regression_terms_energy_variability",
    units="DMNL",
    subscripts=[
        "REGIONS_9_I",
        "OUTPUTS_NGR_VARIABILITY_I",
        "PREDICTORS_NGR_VARIABILITY_I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "predictors_all": 1,
        "energy_variability_linear_regression_coefficients": 1,
    },
)
def individual_linear_regression_terms_energy_variability():
    """
    Calculation of individual terms in the multiple linear regression models to consider the variability of renewable energy
    """
    return (
        predictors_all()
        * energy_variability_linear_regression_coefficients().transpose(
            "PREDICTORS_NGR_VARIABILITY_I", "OUTPUTS_NGR_VARIABILITY_I"
        )
    ).transpose(
        "REGIONS_9_I", "OUTPUTS_NGR_VARIABILITY_I", "PREDICTORS_NGR_VARIABILITY_I"
    )


@component.add(
    name="individual_logistic_regression_terms_energy_variability",
    units="DMNL",
    subscripts=[
        "REGIONS_9_I",
        "OUTPUTS_NGR_VARIABILITY_I",
        "PREDICTORS_NGR_VARIABILITY_I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "predictors_all": 1,
        "energy_variability_logistic_regression_coefficients": 1,
    },
)
def individual_logistic_regression_terms_energy_variability():
    """
    Calculation of individual terms in the regression models to consider the variability of renewable energy
    """
    return (
        predictors_all()
        * energy_variability_logistic_regression_coefficients().transpose(
            "PREDICTORS_NGR_VARIABILITY_I", "OUTPUTS_NGR_VARIABILITY_I"
        )
    ).transpose(
        "REGIONS_9_I", "OUTPUTS_NGR_VARIABILITY_I", "PREDICTORS_NGR_VARIABILITY_I"
    )


@component.add(
    name="input_PROSUP_storage_heat",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "predictor_5_heat_demand": 6,
        "predictor_6_chp": 7,
        "predictor_7_heat_pumps": 9,
        "predictor_11_hydrogen_fe_demand": 7,
        "predictor_13_flexible_demand": 6,
        "predictor_1_protra_pp_solar": 8,
        "predictor_2_protra_pp_wind": 7,
        "predictor_3_capacity_zero_ghg_semiflex": 8,
        "predictor_8_electric_boilers": 3,
    },
)
def input_prosup_storage_heat():
    """
    Share of heat storage (input energy). Output in regressions with EnergyPLAN. R-squared (adjusted) = 0.6504
    """
    return (
        0
        - 0.0216202 * predictor_5_heat_demand()
        + 1.52356e-05 * predictor_6_chp()
        - 8.22302e-05 * predictor_7_heat_pumps()
        - 0.0662637 * predictor_11_hydrogen_fe_demand()
        - 0.0251686 * predictor_13_flexible_demand()
        - 9.88699e-10 * (predictor_1_protra_pp_solar() * predictor_2_protra_pp_wind())
        - 4.18854e-09
        * (predictor_1_protra_pp_solar() * predictor_3_capacity_zero_ghg_semiflex())
        + 2.35257e-07 * (predictor_1_protra_pp_solar() * predictor_5_heat_demand())
        - 1.09407e-09 * (predictor_1_protra_pp_solar() * predictor_6_chp())
        + 1.93404e-09 * (predictor_1_protra_pp_solar() * predictor_7_heat_pumps())
        + 3.60838e-10 * (predictor_1_protra_pp_solar() * predictor_8_electric_boilers())
        + 7.7119e-07
        * (predictor_1_protra_pp_solar() * predictor_11_hydrogen_fe_demand())
        + 2.03313e-07 * (predictor_1_protra_pp_solar() * predictor_13_flexible_demand())
        - 1.65318e-09
        * (predictor_2_protra_pp_wind() * predictor_3_capacity_zero_ghg_semiflex())
        + 1.8917e-07 * (predictor_2_protra_pp_wind() * predictor_5_heat_demand())
        - 4.77233e-10 * (predictor_2_protra_pp_wind() * predictor_6_chp())
        + 9.15942e-10 * (predictor_2_protra_pp_wind() * predictor_7_heat_pumps())
        + 2.00706e-07
        * (predictor_2_protra_pp_wind() * predictor_11_hydrogen_fe_demand())
        + 2.84238e-07 * (predictor_2_protra_pp_wind() * predictor_13_flexible_demand())
        + 5.36215e-07
        * (predictor_3_capacity_zero_ghg_semiflex() * predictor_5_heat_demand())
        - 1.87762e-09 * (predictor_3_capacity_zero_ghg_semiflex() * predictor_6_chp())
        + 6.60958e-10
        * (predictor_3_capacity_zero_ghg_semiflex() * predictor_7_heat_pumps())
        + 6.53454e-10
        * (predictor_3_capacity_zero_ghg_semiflex() * predictor_8_electric_boilers())
        + 2.14058e-06
        * (predictor_3_capacity_zero_ghg_semiflex() * predictor_11_hydrogen_fe_demand())
        + 3.7937e-07
        * (predictor_3_capacity_zero_ghg_semiflex() * predictor_13_flexible_demand())
        + 1.7724e-07 * (predictor_5_heat_demand() * predictor_7_heat_pumps())
        - 3.22375e-05 * (predictor_5_heat_demand() * predictor_11_hydrogen_fe_demand())
        + 7.92447e-10 * (predictor_6_chp() * predictor_7_heat_pumps())
        + 7.59909e-07 * (predictor_6_chp() * predictor_11_hydrogen_fe_demand())
        + 6.41093e-07 * (predictor_6_chp() * predictor_13_flexible_demand())
        - 1.00534e-09 * (predictor_7_heat_pumps() * predictor_8_electric_boilers())
        + 2.42188e-07 * (predictor_7_heat_pumps() * predictor_11_hydrogen_fe_demand())
        - 5.89929e-07 * (predictor_7_heat_pumps() * predictor_13_flexible_demand())
    )


@component.add(
    name="input_PROSUP_storage_heat_bounded",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"input_prosup_storage_heat": 3},
)
def input_prosup_storage_heat_bounded():
    """
    Output considering bounds. Values must be between 0 and 1
    """
    return if_then_else(
        input_prosup_storage_heat() < 0,
        lambda: xr.DataArray(
            0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
        ),
        lambda: if_then_else(
            input_prosup_storage_heat() > 1,
            lambda: xr.DataArray(
                1, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
            ),
            lambda: input_prosup_storage_heat(),
        ),
    )


@component.add(
    name="legacy_elec_demand",
    units="TWh/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_nrg_variability": 1,
        "legacy_elec_demand_energyplan": 1,
        "fe_excluding_trade": 1,
        "unit_conversion_twh_ej": 1,
    },
)
def legacy_elec_demand():
    """
    Reference of legacy demand for the regression models for the renewable variability management
    """
    return if_then_else(
        switch_nrg_variability() == 0,
        lambda: xr.DataArray(
            legacy_elec_demand_energyplan(),
            {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
            ["REGIONS_9_I"],
        ),
        lambda: fe_excluding_trade().loc[:, "FE_elec"].reset_coords(drop=True)
        * unit_conversion_twh_ej(),
    )


@component.add(
    name="LEGACY_ELEC_DEMAND_EnergyPLAN",
    units="TWh/Year",
    comp_type="Constant",
    comp_subtype="Normal",
)
def legacy_elec_demand_energyplan():
    """
    Base value of the EnergyPLAN experimental design
    """
    return 100


@component.add(
    name="max_electrolyser_capacity_used_regression",
    units="MW",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "predictor_6_chp": 2,
        "predictor_12_hydrogen_supply": 14,
        "predictor_7_heat_pumps": 4,
        "predictor_5_heat_demand": 4,
        "predictor_11_hydrogen_fe_demand": 12,
        "predictor_13_flexible_demand": 6,
        "predictor_1_protra_pp_solar": 10,
        "predictor_2_protra_pp_wind": 8,
        "predictor_3_capacity_zero_ghg_semiflex": 10,
    },
)
def max_electrolyser_capacity_used_regression():
    """
    Maximum capacity of electrolysers used in the year. Output in regressions with EnergyPLAN. This variable is de-normalized in the next step.
    """
    return if_then_else(
        -129.558
        + 2.11025e-06 * (predictor_6_chp() * predictor_12_hydrogen_supply())
        - 4.16636e-05 * (predictor_5_heat_demand() * predictor_7_heat_pumps())
        + 4.53068e-06 * (predictor_5_heat_demand() * predictor_12_hydrogen_supply())
        + 130.212 * predictor_11_hydrogen_fe_demand()
        + 0.0484495
        * (predictor_11_hydrogen_fe_demand() * predictor_13_flexible_demand())
        - 0.00642155
        * (predictor_11_hydrogen_fe_demand() * predictor_12_hydrogen_supply())
        - 0.000236685
        * (predictor_12_hydrogen_supply() * predictor_13_flexible_demand())
        - 0.000231999 * (predictor_1_protra_pp_solar() * predictor_13_flexible_demand())
        - 0.000152961
        * (predictor_1_protra_pp_solar() * predictor_11_hydrogen_fe_demand())
        + 1.22617e-05 * (predictor_1_protra_pp_solar() * predictor_12_hydrogen_supply())
        + 5.50283e-07 * (predictor_1_protra_pp_solar() * predictor_2_protra_pp_wind())
        - 2.22068e-06
        * (predictor_1_protra_pp_solar() * predictor_3_capacity_zero_ghg_semiflex())
        - 0.000490584
        * (predictor_2_protra_pp_wind() * predictor_11_hydrogen_fe_demand())
        + 1.27121e-05 * (predictor_2_protra_pp_wind() * predictor_12_hydrogen_supply())
        - 2.01016e-06
        * (predictor_2_protra_pp_wind() * predictor_3_capacity_zero_ghg_semiflex())
        + 8.14855e-07
        * (predictor_3_capacity_zero_ghg_semiflex() * predictor_7_heat_pumps())
        + 3.37564e-05
        * (predictor_3_capacity_zero_ghg_semiflex() * predictor_11_hydrogen_fe_demand())
        + 2.09385e-05
        * (predictor_3_capacity_zero_ghg_semiflex() * predictor_12_hydrogen_supply())
        < 0,
        lambda: xr.DataArray(
            0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
        ),
        lambda: -129.558
        + 2.11025e-06 * (predictor_6_chp() * predictor_12_hydrogen_supply())
        - 4.16636e-05 * (predictor_5_heat_demand() * predictor_7_heat_pumps())
        + 4.53068e-06 * (predictor_5_heat_demand() * predictor_12_hydrogen_supply())
        + 130.212 * predictor_11_hydrogen_fe_demand()
        + 0.0484495
        * (predictor_11_hydrogen_fe_demand() * predictor_13_flexible_demand())
        - 0.00642155
        * (predictor_11_hydrogen_fe_demand() * predictor_12_hydrogen_supply())
        - 0.000236685
        * (predictor_12_hydrogen_supply() * predictor_13_flexible_demand())
        - 0.000231999 * (predictor_1_protra_pp_solar() * predictor_13_flexible_demand())
        - 0.000152961
        * (predictor_1_protra_pp_solar() * predictor_11_hydrogen_fe_demand())
        + 1.22617e-05 * (predictor_1_protra_pp_solar() * predictor_12_hydrogen_supply())
        + 5.50283e-07 * (predictor_1_protra_pp_solar() * predictor_2_protra_pp_wind())
        - 2.22068e-06
        * (predictor_1_protra_pp_solar() * predictor_3_capacity_zero_ghg_semiflex())
        - 0.000490584
        * (predictor_2_protra_pp_wind() * predictor_11_hydrogen_fe_demand())
        + 1.27121e-05 * (predictor_2_protra_pp_wind() * predictor_12_hydrogen_supply())
        - 2.01016e-06
        * (predictor_2_protra_pp_wind() * predictor_3_capacity_zero_ghg_semiflex())
        + 8.14855e-07
        * (predictor_3_capacity_zero_ghg_semiflex() * predictor_7_heat_pumps())
        + 3.37564e-05
        * (predictor_3_capacity_zero_ghg_semiflex() * predictor_11_hydrogen_fe_demand())
        + 2.09385e-05
        * (predictor_3_capacity_zero_ghg_semiflex() * predictor_12_hydrogen_supply()),
    )


@component.add(
    name="max_electrolyser_capacity_used_scaled",
    units="MW",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "max_electrolyser_capacity_used_regression": 1,
        "hourly_average_power_elec_demand": 1,
        "hourly_average_power_elec_demand_energyplan": 1,
    },
)
def max_electrolyser_capacity_used_scaled():
    """
    Maximum capacity of electrolysers used in the year. Output of the regression scaled from the normalized system to the regional one
    """
    return (
        max_electrolyser_capacity_used_regression()
        * hourly_average_power_elec_demand()
        / hourly_average_power_elec_demand_energyplan()
    )


@component.add(
    name="max_hourly_electricity_demand_regression",
    units="MW",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "predictor_5_heat_demand": 2,
        "predictor_12_hydrogen_supply": 10,
        "predictor_11_hydrogen_fe_demand": 8,
        "predictor_13_flexible_demand": 2,
        "predictor_1_protra_pp_solar": 2,
        "predictor_3_capacity_zero_ghg_semiflex": 14,
        "predictor_2_protra_pp_wind": 6,
        "predictor_9_electric_vehicle_demand": 2,
        "predictor_7_heat_pumps": 2,
    },
)
def max_hourly_electricity_demand_regression():
    """
    Maximum demand load in one hour over the year. Output in regressions with EnergyPLAN. This variable is de-normalized in the next step. R-squared (adjusted) = 0.7643
    """
    return if_then_else(
        -547700
        - 0.074059 * (predictor_5_heat_demand() * predictor_12_hydrogen_supply())
        + 13939 * predictor_11_hydrogen_fe_demand()
        - 0.585981
        * (predictor_11_hydrogen_fe_demand() * predictor_12_hydrogen_supply())
        - 0.0912308 * (predictor_12_hydrogen_supply() * predictor_13_flexible_demand())
        + 0.00187158
        * (predictor_1_protra_pp_solar() * predictor_3_capacity_zero_ghg_semiflex())
        - 0.344829 * (predictor_2_protra_pp_wind() * predictor_11_hydrogen_fe_demand())
        + 0.00180859 * (predictor_2_protra_pp_wind() * predictor_12_hydrogen_supply())
        + 0.00281171
        * (predictor_2_protra_pp_wind() * predictor_3_capacity_zero_ghg_semiflex())
        + 58.6547 * predictor_3_capacity_zero_ghg_semiflex()
        - 0.351289
        * (
            predictor_3_capacity_zero_ghg_semiflex()
            * predictor_9_electric_vehicle_demand()
        )
        + 0.000262875
        * (predictor_3_capacity_zero_ghg_semiflex() * predictor_7_heat_pumps())
        - 1.78477
        * (predictor_3_capacity_zero_ghg_semiflex() * predictor_11_hydrogen_fe_demand())
        + 0.00852054
        * (predictor_3_capacity_zero_ghg_semiflex() * predictor_12_hydrogen_supply())
        < 0,
        lambda: xr.DataArray(
            0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
        ),
        lambda: -547700
        - 0.074059 * (predictor_5_heat_demand() * predictor_12_hydrogen_supply())
        + 13939 * predictor_11_hydrogen_fe_demand()
        - 0.585981
        * (predictor_11_hydrogen_fe_demand() * predictor_12_hydrogen_supply())
        - 0.0912308 * (predictor_12_hydrogen_supply() * predictor_13_flexible_demand())
        + 0.00187158
        * (predictor_1_protra_pp_solar() * predictor_3_capacity_zero_ghg_semiflex())
        - 0.344829 * (predictor_2_protra_pp_wind() * predictor_11_hydrogen_fe_demand())
        + 0.00180859 * (predictor_2_protra_pp_wind() * predictor_12_hydrogen_supply())
        + 0.00281171
        * (predictor_2_protra_pp_wind() * predictor_3_capacity_zero_ghg_semiflex())
        + 58.6547 * predictor_3_capacity_zero_ghg_semiflex()
        - 0.351289
        * (
            predictor_3_capacity_zero_ghg_semiflex()
            * predictor_9_electric_vehicle_demand()
        )
        + 0.000262875
        * (predictor_3_capacity_zero_ghg_semiflex() * predictor_7_heat_pumps())
        - 1.78477
        * (predictor_3_capacity_zero_ghg_semiflex() * predictor_11_hydrogen_fe_demand())
        + 0.00852054
        * (predictor_3_capacity_zero_ghg_semiflex() * predictor_12_hydrogen_supply()),
    )


@component.add(
    name="max_hourly_electricity_demand_scaled",
    units="MW",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "max_hourly_electricity_demand_regression": 1,
        "hourly_average_power_elec_demand": 1,
        "hourly_average_power_elec_demand_energyplan": 1,
    },
)
def max_hourly_electricity_demand_scaled():
    """
    Maximum demand load in one hour over the year. Output of the regression scaled from the normalized system to the regional one
    """
    return (
        max_hourly_electricity_demand_regression()
        * hourly_average_power_elec_demand()
        / hourly_average_power_elec_demand_energyplan()
    )


@component.add(
    name="outputs_linear_regression",
    units="DMNL",
    subscripts=["REGIONS_9_I", "OUTPUTS_NGR_VARIABILITY_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"checking_linear_regression_models_energy_variability": 1},
)
def outputs_linear_regression():
    """
    Outputs of the linear regression models taking into account variable renewable energies
    """
    return checking_linear_regression_models_energy_variability()


@component.add(
    name="outputs_logistic_regression",
    units="Dnml",
    subscripts=["REGIONS_9_I", "OUTPUTS_NGR_VARIABILITY_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"checking_logistic_regression_models_energy_variability": 1},
)
def outputs_logistic_regression():
    """
    Outputs of the logistic regression models taking into account variable renewable energies
    """
    return 1 / (1 + np.exp(-checking_logistic_regression_models_energy_variability()))


@component.add(
    name="predictor_10_v2g",
    units="MW",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_nrg_variability": 1,
        "exogenous_predictors_energy_variability_regressions": 1,
        "ev_batteries_power_v2g_9r": 1,
        "unit_conversion_mw_tw": 1,
        "hourly_average_power_elec_demand_energyplan": 1,
        "hourly_average_power_elec_demand": 1,
    },
)
def predictor_10_v2g():
    """
    Value of the cluster. The input is re-scaled according to the design of the experiment
    """
    return if_then_else(
        switch_nrg_variability() == 0,
        lambda: xr.DataArray(
            float(
                exogenous_predictors_energy_variability_regressions().loc[
                    "PREDICTOR_V2G"
                ]
            ),
            {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
            ["REGIONS_9_I"],
        ),
        lambda: ev_batteries_power_v2g_9r()
        * unit_conversion_mw_tw()
        * hourly_average_power_elec_demand_energyplan()
        / hourly_average_power_elec_demand(),
    )


@component.add(
    name="predictor_11_hydrogen_FE_demand",
    units="TWh/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_nrg_variability": 1,
        "exogenous_predictors_energy_variability_regressions": 1,
        "fe_excluding_trade": 1,
        "legacy_elec_demand_energyplan": 1,
        "unit_conversion_twh_ej": 1,
        "legacy_elec_demand": 1,
    },
)
def predictor_11_hydrogen_fe_demand():
    """
    Value of the cluster. The input is re-scaled according to the design of the experiment
    """
    return if_then_else(
        switch_nrg_variability() == 0,
        lambda: xr.DataArray(
            float(
                exogenous_predictors_energy_variability_regressions().loc[
                    "PREDICTOR_HYDROGEN_DEMAND"
                ]
            ),
            {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
            ["REGIONS_9_I"],
        ),
        lambda: fe_excluding_trade().loc[:, "FE_hydrogen"].reset_coords(drop=True)
        * unit_conversion_twh_ej()
        * legacy_elec_demand_energyplan()
        / legacy_elec_demand(),
    )


@component.add(
    name="predictor_12_hydrogen_supply",
    units="MW",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_nrg_variability": 1,
        "exogenous_predictors_energy_variability_regressions": 1,
        "flexible_electrolysers_capacity_stock": 1,
        "hourly_average_power_elec_demand": 1,
        "hourly_average_power_elec_demand_energyplan": 1,
        "unit_conversion_mw_tw": 1,
    },
)
def predictor_12_hydrogen_supply():
    """
    Value of the cluster. The input is re-scaled according to the design of the experiment
    """
    return if_then_else(
        switch_nrg_variability() == 0,
        lambda: xr.DataArray(
            float(
                exogenous_predictors_energy_variability_regressions().loc[
                    "PREDICTOR_HYDROGEN_SUPPLY"
                ]
            ),
            {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
            ["REGIONS_9_I"],
        ),
        lambda: flexible_electrolysers_capacity_stock()
        * unit_conversion_mw_tw()
        * hourly_average_power_elec_demand_energyplan()
        / hourly_average_power_elec_demand(),
    )


@component.add(
    name="predictor_13_flexible_demand",
    units="TWh/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_nrg_variability": 1,
        "exogenous_predictors_energy_variability_regressions": 1,
        "year_final_flex_elec_demand_sp": 3,
        "initial_year_flex_elec_demand_sp": 3,
        "switch_flex_elec_demand_sp": 3,
        "time": 3,
        "objective_flex_elec_demand_sp": 2,
    },
)
def predictor_13_flexible_demand():
    """
    Value of the cluster. The input is re-scaled according to the design of the experiment
    """
    return if_then_else(
        switch_nrg_variability() == 0,
        lambda: xr.DataArray(
            float(
                exogenous_predictors_energy_variability_regressions().loc[
                    "PREDICTOR_FLEX_DEMAND"
                ]
            ),
            {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
            ["REGIONS_9_I"],
        ),
        lambda: if_then_else(
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
        ),
    )


@component.add(
    name="predictor_1_PROTRA_PP_solar",
    units="MW",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_nrg_variability": 1,
        "exogenous_predictors_energy_variability_regressions": 1,
        "protra_capacity_stock": 2,
        "hourly_average_power_elec_demand": 1,
        "hourly_average_power_elec_demand_energyplan": 1,
        "unit_conversion_mw_tw": 1,
    },
)
def predictor_1_protra_pp_solar():
    """
    Value of the cluster. The input is re-scaled according to the design of the experiment
    """
    return if_then_else(
        switch_nrg_variability() == 0,
        lambda: xr.DataArray(
            float(
                exogenous_predictors_energy_variability_regressions().loc[
                    "PREDICTOR_SOLAR"
                ]
            ),
            {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
            ["REGIONS_9_I"],
        ),
        lambda: (
            protra_capacity_stock()
            .loc[:, "TO_elec", "PROTRA_PP_solar_CSP"]
            .reset_coords(drop=True)
            + protra_capacity_stock()
            .loc[:, "TO_elec", "PROTRA_PP_solar_open_space_PV"]
            .reset_coords(drop=True)
        )
        * unit_conversion_mw_tw()
        * hourly_average_power_elec_demand_energyplan()
        / hourly_average_power_elec_demand(),
    )


@component.add(
    name="predictor_2_PROTRA_PP_wind",
    units="MW",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_nrg_variability": 1,
        "exogenous_predictors_energy_variability_regressions": 1,
        "protra_capacity_stock": 2,
        "hourly_average_power_elec_demand": 1,
        "hourly_average_power_elec_demand_energyplan": 1,
        "unit_conversion_mw_tw": 1,
    },
)
def predictor_2_protra_pp_wind():
    """
    Value of the cluster. The input is re-scaled according to the design of the experiment
    """
    return if_then_else(
        switch_nrg_variability() == 0,
        lambda: xr.DataArray(
            float(
                exogenous_predictors_energy_variability_regressions().loc[
                    "PREDICTOR_WIND"
                ]
            ),
            {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
            ["REGIONS_9_I"],
        ),
        lambda: (
            protra_capacity_stock()
            .loc[:, "TO_elec", "PROTRA_PP_wind_offshore"]
            .reset_coords(drop=True)
            + protra_capacity_stock()
            .loc[:, "TO_elec", "PROTRA_PP_wind_onshore"]
            .reset_coords(drop=True)
        )
        * unit_conversion_mw_tw()
        * hourly_average_power_elec_demand_energyplan()
        / hourly_average_power_elec_demand(),
    )


@component.add(
    name="predictor_3_capacity_zero_ghg_semiflex",
    units="MW",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_nrg_variability": 1,
        "exogenous_predictors_energy_variability_regressions": 1,
        "protra_capacity_stock": 4,
        "hourly_average_power_elec_demand": 1,
        "hourly_average_power_elec_demand_energyplan": 1,
        "unit_conversion_mw_tw": 1,
    },
)
def predictor_3_capacity_zero_ghg_semiflex():
    """
    Value of the cluster. The input is re-scaled according to the design of the experiment
    """
    return if_then_else(
        switch_nrg_variability() == 0,
        lambda: xr.DataArray(
            float(
                exogenous_predictors_energy_variability_regressions().loc[
                    "PREDICTOR_ZERO_GHG_SEMIFLEX"
                ]
            ),
            {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
            ["REGIONS_9_I"],
        ),
        lambda: (
            protra_capacity_stock()
            .loc[:, "TO_elec", "PROTRA_PP_nuclear"]
            .reset_coords(drop=True)
            + protra_capacity_stock()
            .loc[:, "TO_elec", "PROTRA_PP_geothermal"]
            .reset_coords(drop=True)
            + protra_capacity_stock()
            .loc[:, "TO_elec", "PROTRA_PP_hydropower_run_of_river"]
            .reset_coords(drop=True)
            + protra_capacity_stock()
            .loc[:, "TO_elec", "PROTRA_PP_hydropower_dammed"]
            .reset_coords(drop=True)
        )
        * unit_conversion_mw_tw()
        * hourly_average_power_elec_demand_energyplan()
        / hourly_average_power_elec_demand(),
    )


@component.add(
    name="predictor_4_stationary_storage",
    units="MW",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_nrg_variability": 1,
        "exogenous_predictors_energy_variability_regressions": 1,
        "ev_batteries_power_sc": 2,
        "hourly_average_power_elec_demand": 2,
        "prosto_capacity_stock": 2,
        "unit_conversion_mw_tw": 2,
        "hourly_average_power_elec_demand_energyplan": 2,
        "ev_batteries_power_v2g": 2,
    },
)
def predictor_4_stationary_storage():
    """
    Value of the cluster. The input is re-scaled according to the design of the experiment
    """
    value = xr.DataArray(
        np.nan, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
    )
    value.loc[["EU27"]] = if_then_else(
        switch_nrg_variability() == 0,
        lambda: float(
            exogenous_predictors_energy_variability_regressions().loc[
                "PREDICTOR_STATIONARY_STORAGE"
            ]
        ),
        lambda: (
            sum(
                ev_batteries_power_v2g()
                .loc[_subscript_dict["REGIONS_EU27_I"]]
                .rename({"REGIONS_35_I": "REGIONS_EU27_I!"}),
                dim=["REGIONS_EU27_I!"],
            )
            + sum(
                ev_batteries_power_sc()
                .loc[_subscript_dict["REGIONS_EU27_I"]]
                .rename({"REGIONS_35_I": "REGIONS_EU27_I!"}),
                dim=["REGIONS_EU27_I!"],
            )
            + sum(
                prosto_capacity_stock()
                .loc["EU27", _subscript_dict["PROSTO_ELEC_DEDICATED_I"]]
                .reset_coords(drop=True)
                .rename({"NRG_PROSTO_I": "PROSTO_ELEC_DEDICATED_I!"}),
                dim=["PROSTO_ELEC_DEDICATED_I!"],
            )
        )
        * unit_conversion_mw_tw()
        * hourly_average_power_elec_demand_energyplan()
        / float(hourly_average_power_elec_demand().loc["EU27"]),
    )
    value.loc[_subscript_dict["REGIONS_8_I"]] = (
        ev_batteries_power_v2g()
        .loc[_subscript_dict["REGIONS_8_I"]]
        .rename({"REGIONS_35_I": "REGIONS_8_I"})
        + ev_batteries_power_sc()
        .loc[_subscript_dict["REGIONS_8_I"]]
        .rename({"REGIONS_35_I": "REGIONS_8_I"})
        + sum(
            prosto_capacity_stock()
            .loc[
                _subscript_dict["REGIONS_8_I"],
                _subscript_dict["PROSTO_ELEC_DEDICATED_I"],
            ]
            .rename(
                {
                    "REGIONS_9_I": "REGIONS_8_I",
                    "NRG_PROSTO_I": "PROSTO_ELEC_DEDICATED_I!",
                }
            ),
            dim=["PROSTO_ELEC_DEDICATED_I!"],
        )
        * unit_conversion_mw_tw()
        * hourly_average_power_elec_demand_energyplan()
        / hourly_average_power_elec_demand()
        .loc[_subscript_dict["REGIONS_8_I"]]
        .rename({"REGIONS_9_I": "REGIONS_8_I"})
    ).values
    return value


@component.add(
    name="predictor_5_heat_demand",
    units="TWh/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_nrg_variability": 1,
        "exogenous_predictors_energy_variability_regressions": 1,
        "fe_excluding_trade": 1,
        "legacy_elec_demand_energyplan": 1,
        "unit_conversion_twh_ej": 1,
        "legacy_elec_demand": 1,
    },
)
def predictor_5_heat_demand():
    """
    Value of the cluster. The input is re-scaled according to the design of the experiment
    """
    return if_then_else(
        switch_nrg_variability() == 0,
        lambda: xr.DataArray(
            float(
                exogenous_predictors_energy_variability_regressions().loc[
                    "PREDICTOR_HEAT_DEMAND"
                ]
            ),
            {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
            ["REGIONS_9_I"],
        ),
        lambda: fe_excluding_trade().loc[:, "FE_heat"].reset_coords(drop=True)
        * unit_conversion_twh_ej()
        * legacy_elec_demand_energyplan()
        / legacy_elec_demand(),
    )


@component.add(
    name="predictor_6_chp",
    units="MW",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_nrg_variability": 1,
        "exogenous_predictors_energy_variability_regressions": 1,
        "protra_capacity_stock": 10,
        "hourly_average_power_elec_demand": 1,
        "hourly_average_power_elec_demand_energyplan": 1,
        "unit_conversion_mw_tw": 1,
    },
)
def predictor_6_chp():
    """
    Value of the cluster. The input is re-scaled according to the design of the experiment
    """
    return if_then_else(
        switch_nrg_variability() == 0,
        lambda: xr.DataArray(
            float(
                exogenous_predictors_energy_variability_regressions().loc[
                    "PREDICTOR_CHP"
                ]
            ),
            {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
            ["REGIONS_9_I"],
        ),
        lambda: (
            protra_capacity_stock()
            .loc[:, "TO_elec", "PROTRA_CHP_gas_fuels"]
            .reset_coords(drop=True)
            + protra_capacity_stock()
            .loc[:, "TO_elec", "PROTRA_CHP_gas_fuels_CCS"]
            .reset_coords(drop=True)
            + protra_capacity_stock()
            .loc[:, "TO_elec", "PROTRA_CHP_geothermal_DEACTIVATED"]
            .reset_coords(drop=True)
            + protra_capacity_stock()
            .loc[:, "TO_elec", "PROTRA_CHP_liquid_fuels"]
            .reset_coords(drop=True)
            + protra_capacity_stock()
            .loc[:, "TO_elec", "PROTRA_CHP_liquid_fuels_CCS"]
            .reset_coords(drop=True)
            + protra_capacity_stock()
            .loc[:, "TO_elec", "PROTRA_CHP_solid_fossil"]
            .reset_coords(drop=True)
            + protra_capacity_stock()
            .loc[:, "TO_elec", "PROTRA_CHP_solid_fossil_CCS"]
            .reset_coords(drop=True)
            + protra_capacity_stock()
            .loc[:, "TO_elec", "PROTRA_CHP_waste"]
            .reset_coords(drop=True)
            + protra_capacity_stock()
            .loc[:, "TO_elec", "PROTRA_CHP_solid_bio"]
            .reset_coords(drop=True)
            + protra_capacity_stock()
            .loc[:, "TO_elec", "PROTRA_CHP_solid_bio_CCS"]
            .reset_coords(drop=True)
        )
        * unit_conversion_mw_tw()
        * hourly_average_power_elec_demand_energyplan()
        / hourly_average_power_elec_demand(),
    )


@component.add(
    name="predictor_7_heat_pumps",
    units="MW",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_nrg_variability": 1,
        "exogenous_predictors_energy_variability_regressions": 1,
        "hourly_average_power_elec_demand_energyplan": 1,
        "hourly_average_power_elec_demand": 1,
        "prosup_p2h_capacity_stock": 1,
        "unit_conversion_mw_tw": 1,
        "switch_test_nrg_activate_p2h_regressions": 1,
    },
)
def predictor_7_heat_pumps():
    """
    Value of the cluster. The input is re-scaled according to the design of the experiment
    """
    return (
        if_then_else(
            switch_nrg_variability() == 0,
            lambda: xr.DataArray(
                float(
                    exogenous_predictors_energy_variability_regressions().loc[
                        "PREDICTOR_HEAT_PUMPS"
                    ]
                ),
                {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
                ["REGIONS_9_I"],
            ),
            lambda: prosup_p2h_capacity_stock()
            .loc[:, "PROSUP_P2H_heat_pump"]
            .reset_coords(drop=True)
            * unit_conversion_mw_tw()
            * hourly_average_power_elec_demand_energyplan()
            / hourly_average_power_elec_demand(),
        )
        * switch_test_nrg_activate_p2h_regressions()
    )


@component.add(
    name="predictor_8_electric_boilers",
    units="MW",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_nrg_variability": 1,
        "exogenous_predictors_energy_variability_regressions": 1,
        "hourly_average_power_elec_demand_energyplan": 1,
        "hourly_average_power_elec_demand": 1,
        "prosup_p2h_capacity_stock": 1,
        "unit_conversion_mw_tw": 1,
        "switch_test_nrg_activate_p2h_regressions": 1,
    },
)
def predictor_8_electric_boilers():
    """
    Value of the cluster. The input is re-scaled according to the design of the experiment
    """
    return (
        if_then_else(
            switch_nrg_variability() == 0,
            lambda: xr.DataArray(
                float(
                    exogenous_predictors_energy_variability_regressions().loc[
                        "PREDICTOR_ELEC_BOILERS"
                    ]
                ),
                {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
                ["REGIONS_9_I"],
            ),
            lambda: prosup_p2h_capacity_stock()
            .loc[:, "PROSUP_P2H_electric_boiler"]
            .reset_coords(drop=True)
            * unit_conversion_mw_tw()
            * hourly_average_power_elec_demand_energyplan()
            / hourly_average_power_elec_demand(),
        )
        * switch_test_nrg_activate_p2h_regressions()
    )


@component.add(
    name="predictor_9_electric_vehicle_demand",
    units="TWh",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_nrg_variability": 1,
        "exogenous_predictors_energy_variability_regressions": 1,
        "legacy_elec_demand": 9,
        "unit_conversion_twh_ej": 9,
        "energy_passenger_transport_consumption_by_fe_35r": 9,
        "legacy_elec_demand_energyplan": 9,
        "unit_conversion_mj_ej": 9,
    },
)
def predictor_9_electric_vehicle_demand():
    """
    Value of the cluster. The input is re-scaled according to the design of the experiment
    """
    value = xr.DataArray(
        np.nan, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
    )
    value.loc[["EU27"]] = if_then_else(
        switch_nrg_variability() == 0,
        lambda: float(
            exogenous_predictors_energy_variability_regressions().loc[
                "PREDICTOR_EV_DEMAND"
            ]
        ),
        lambda: sum(
            energy_passenger_transport_consumption_by_fe_35r()
            .loc[_subscript_dict["REGIONS_EU27_I"], "FE_elec", :, :]
            .reset_coords(drop=True)
            .rename(
                {
                    "REGIONS_35_I": "REGIONS_EU27_I!",
                    "PASSENGERS_TRANSPORT_MODE_I": "PASSENGERS_TRANSPORT_MODE_I!",
                    "HOUSEHOLDS_I": "HOUSEHOLDS_I!",
                }
            ),
            dim=["REGIONS_EU27_I!", "PASSENGERS_TRANSPORT_MODE_I!", "HOUSEHOLDS_I!"],
        )
        / unit_conversion_mj_ej()
        * unit_conversion_twh_ej()
        * legacy_elec_demand_energyplan()
        / float(legacy_elec_demand().loc["EU27"]),
    )
    value.loc[["UK"]] = (
        sum(
            energy_passenger_transport_consumption_by_fe_35r()
            .loc["UK", "FE_elec", :, :]
            .reset_coords(drop=True)
            .rename(
                {
                    "PASSENGERS_TRANSPORT_MODE_I": "PASSENGERS_TRANSPORT_MODE_I!",
                    "HOUSEHOLDS_I": "HOUSEHOLDS_I!",
                }
            ),
            dim=["PASSENGERS_TRANSPORT_MODE_I!", "HOUSEHOLDS_I!"],
        )
        / unit_conversion_mj_ej()
        * unit_conversion_twh_ej()
        * legacy_elec_demand_energyplan()
        / float(legacy_elec_demand().loc["UK"])
    )
    value.loc[["CHINA"]] = (
        sum(
            energy_passenger_transport_consumption_by_fe_35r()
            .loc["CHINA", "FE_elec", :, :]
            .reset_coords(drop=True)
            .rename(
                {
                    "PASSENGERS_TRANSPORT_MODE_I": "PASSENGERS_TRANSPORT_MODE_I!",
                    "HOUSEHOLDS_I": "HOUSEHOLDS_I!",
                }
            ),
            dim=["PASSENGERS_TRANSPORT_MODE_I!", "HOUSEHOLDS_I!"],
        )
        / unit_conversion_mj_ej()
        * unit_conversion_twh_ej()
        * legacy_elec_demand_energyplan()
        / float(legacy_elec_demand().loc["CHINA"])
    )
    value.loc[["EASOC"]] = (
        sum(
            energy_passenger_transport_consumption_by_fe_35r()
            .loc["EASOC", "FE_elec", :, :]
            .reset_coords(drop=True)
            .rename(
                {
                    "PASSENGERS_TRANSPORT_MODE_I": "PASSENGERS_TRANSPORT_MODE_I!",
                    "HOUSEHOLDS_I": "HOUSEHOLDS_I!",
                }
            ),
            dim=["PASSENGERS_TRANSPORT_MODE_I!", "HOUSEHOLDS_I!"],
        )
        / unit_conversion_mj_ej()
        * unit_conversion_twh_ej()
        * legacy_elec_demand_energyplan()
        / float(legacy_elec_demand().loc["EASOC"])
    )
    value.loc[["INDIA"]] = (
        sum(
            energy_passenger_transport_consumption_by_fe_35r()
            .loc["INDIA", "FE_elec", :, :]
            .reset_coords(drop=True)
            .rename(
                {
                    "PASSENGERS_TRANSPORT_MODE_I": "PASSENGERS_TRANSPORT_MODE_I!",
                    "HOUSEHOLDS_I": "HOUSEHOLDS_I!",
                }
            ),
            dim=["PASSENGERS_TRANSPORT_MODE_I!", "HOUSEHOLDS_I!"],
        )
        / unit_conversion_mj_ej()
        * unit_conversion_twh_ej()
        * legacy_elec_demand_energyplan()
        / float(legacy_elec_demand().loc["INDIA"])
    )
    value.loc[["LATAM"]] = (
        sum(
            energy_passenger_transport_consumption_by_fe_35r()
            .loc["LATAM", "FE_elec", :, :]
            .reset_coords(drop=True)
            .rename(
                {
                    "PASSENGERS_TRANSPORT_MODE_I": "PASSENGERS_TRANSPORT_MODE_I!",
                    "HOUSEHOLDS_I": "HOUSEHOLDS_I!",
                }
            ),
            dim=["PASSENGERS_TRANSPORT_MODE_I!", "HOUSEHOLDS_I!"],
        )
        / unit_conversion_mj_ej()
        * unit_conversion_twh_ej()
        * legacy_elec_demand_energyplan()
        / float(legacy_elec_demand().loc["LATAM"])
    )
    value.loc[["RUSSIA"]] = (
        sum(
            energy_passenger_transport_consumption_by_fe_35r()
            .loc["RUSSIA", "FE_elec", :, :]
            .reset_coords(drop=True)
            .rename(
                {
                    "PASSENGERS_TRANSPORT_MODE_I": "PASSENGERS_TRANSPORT_MODE_I!",
                    "HOUSEHOLDS_I": "HOUSEHOLDS_I!",
                }
            ),
            dim=["PASSENGERS_TRANSPORT_MODE_I!", "HOUSEHOLDS_I!"],
        )
        / unit_conversion_mj_ej()
        * unit_conversion_twh_ej()
        * legacy_elec_demand_energyplan()
        / float(legacy_elec_demand().loc["RUSSIA"])
    )
    value.loc[["USMCA"]] = (
        sum(
            energy_passenger_transport_consumption_by_fe_35r()
            .loc["USMCA", "FE_elec", :, :]
            .reset_coords(drop=True)
            .rename(
                {
                    "PASSENGERS_TRANSPORT_MODE_I": "PASSENGERS_TRANSPORT_MODE_I!",
                    "HOUSEHOLDS_I": "HOUSEHOLDS_I!",
                }
            ),
            dim=["PASSENGERS_TRANSPORT_MODE_I!", "HOUSEHOLDS_I!"],
        )
        / unit_conversion_mj_ej()
        * unit_conversion_twh_ej()
        * legacy_elec_demand_energyplan()
        / float(legacy_elec_demand().loc["USMCA"])
    )
    value.loc[["LROW"]] = (
        sum(
            energy_passenger_transport_consumption_by_fe_35r()
            .loc["LROW", "FE_elec", :, :]
            .reset_coords(drop=True)
            .rename(
                {
                    "PASSENGERS_TRANSPORT_MODE_I": "PASSENGERS_TRANSPORT_MODE_I!",
                    "HOUSEHOLDS_I": "HOUSEHOLDS_I!",
                }
            ),
            dim=["PASSENGERS_TRANSPORT_MODE_I!", "HOUSEHOLDS_I!"],
        )
        / unit_conversion_mj_ej()
        * unit_conversion_twh_ej()
        * legacy_elec_demand_energyplan()
        / float(legacy_elec_demand().loc["LROW"])
    )
    return value


@component.add(
    name="predictors_all",
    units="DMNL",
    subscripts=["REGIONS_9_I", "PREDICTORS_NGR_VARIABILITY_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "predictor_6_chp": 15,
        "predictor_8_electric_boilers": 15,
        "predictor_9_electric_vehicle_demand": 15,
        "predictor_13_flexible_demand": 15,
        "predictor_7_heat_pumps": 15,
        "predictor_11_hydrogen_fe_demand": 15,
        "predictor_12_hydrogen_supply": 15,
        "predictor_10_v2g": 15,
        "predictor_5_heat_demand": 15,
        "predictor_1_protra_pp_solar": 15,
        "predictor_4_stationary_storage": 15,
        "predictor_2_protra_pp_wind": 15,
        "predictor_3_capacity_zero_ghg_semiflex": 15,
    },
)
def predictors_all():
    """
    Inputs of the regression analysis in the energy variability submodule
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "PREDICTORS_NGR_VARIABILITY_I": _subscript_dict[
                "PREDICTORS_NGR_VARIABILITY_I"
            ],
        },
        ["REGIONS_9_I", "PREDICTORS_NGR_VARIABILITY_I"],
    )
    value.loc[:, ["PREDICTOR_CHP"]] = (
        predictor_6_chp()
        .expand_dims({"BASIC_PREDICTORS_NGR_VARIABILITY_I": ["PREDICTOR_CHP"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR_CHPoELEC_BOILERS"]] = (
        (predictor_6_chp() * predictor_8_electric_boilers())
        .expand_dims({"NRG_VARIABILITY_I": ["PREDICTOR_CHPoELEC_BOILERS"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR_CHPoEV_DEMAND"]] = (
        (predictor_6_chp() * predictor_9_electric_vehicle_demand())
        .expand_dims({"NRG_VARIABILITY_I": ["PREDICTOR_CHPoEV_DEMAND"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR_CHPoFLEX_DEMAND"]] = (
        (predictor_6_chp() * predictor_13_flexible_demand())
        .expand_dims({"NRG_VARIABILITY_I": ["PREDICTOR_CHPoFLEX_DEMAND"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR_CHPoHEAT_PUMPS"]] = (
        (predictor_6_chp() * predictor_7_heat_pumps())
        .expand_dims({"NRG_VARIABILITY_I": ["PREDICTOR_CHPoHEAT_PUMPS"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR_CHPoHYDROGEN_DEMAND"]] = (
        (predictor_6_chp() * predictor_11_hydrogen_fe_demand())
        .expand_dims({"NRG_VARIABILITY_I": ["PREDICTOR_CHPoHYDROGEN_DEMAND"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR_CHPoHYDROGEN_SUPPLY"]] = (
        (predictor_6_chp() * predictor_12_hydrogen_supply())
        .expand_dims({"NRG_VARIABILITY_I": ["PREDICTOR_CHPoHYDROGEN_SUPPLY"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR_CHPoV2G"]] = (
        (predictor_6_chp() * predictor_10_v2g())
        .expand_dims({"NRG_VARIABILITY_I": ["PREDICTOR_CHPoV2G"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR_ELEC_BOILERS"]] = (
        predictor_8_electric_boilers()
        .expand_dims(
            {"BASIC_PREDICTORS_NGR_VARIABILITY_I": ["PREDICTOR_ELEC_BOILERS"]}, 1
        )
        .values
    )
    value.loc[:, ["PREDICTOR_ELEC_BOILERSoEV_DEMAND"]] = (
        (predictor_8_electric_boilers() * predictor_9_electric_vehicle_demand())
        .expand_dims({"NRG_VARIABILITY_I": ["PREDICTOR_ELEC_BOILERSoEV_DEMAND"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR_ELEC_BOILERSoFLEX_DEMAND"]] = (
        (predictor_8_electric_boilers() * predictor_13_flexible_demand())
        .expand_dims({"NRG_VARIABILITY_I": ["PREDICTOR_ELEC_BOILERSoFLEX_DEMAND"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR_ELEC_BOILERSoHYDROGEN_DEMAND"]] = (
        (predictor_8_electric_boilers() * predictor_11_hydrogen_fe_demand())
        .expand_dims(
            {"NRG_VARIABILITY_I": ["PREDICTOR_ELEC_BOILERSoHYDROGEN_DEMAND"]}, 1
        )
        .values
    )
    value.loc[:, ["PREDICTOR_ELEC_BOILERSoHYDROGEN_SUPPLY"]] = (
        (predictor_8_electric_boilers() * predictor_12_hydrogen_supply())
        .expand_dims(
            {"NRG_VARIABILITY_I": ["PREDICTOR_ELEC_BOILERSoHYDROGEN_SUPPLY"]}, 1
        )
        .values
    )
    value.loc[:, ["PREDICTOR_ELEC_BOILERSoV2G"]] = (
        (predictor_8_electric_boilers() * predictor_10_v2g())
        .expand_dims({"NRG_VARIABILITY_I": ["PREDICTOR_ELEC_BOILERSoV2G"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR_EV_DEMAND"]] = (
        predictor_9_electric_vehicle_demand()
        .expand_dims({"BASIC_PREDICTORS_NGR_VARIABILITY_I": ["PREDICTOR_EV_DEMAND"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR_EV_DEMANDoFLEX_DEMAND"]] = (
        (predictor_9_electric_vehicle_demand() * predictor_13_flexible_demand())
        .expand_dims({"NRG_VARIABILITY_I": ["PREDICTOR_EV_DEMANDoFLEX_DEMAND"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR_EV_DEMANDoHYDROGEN_DEMAND"]] = (
        (predictor_9_electric_vehicle_demand() * predictor_11_hydrogen_fe_demand())
        .expand_dims({"NRG_VARIABILITY_I": ["PREDICTOR_EV_DEMANDoHYDROGEN_DEMAND"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR_EV_DEMANDoHYDROGEN_SUPPLY"]] = (
        (predictor_9_electric_vehicle_demand() * predictor_12_hydrogen_supply())
        .expand_dims({"NRG_VARIABILITY_I": ["PREDICTOR_EV_DEMANDoHYDROGEN_SUPPLY"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR_EV_DEMANDoV2G"]] = (
        (predictor_9_electric_vehicle_demand() * predictor_10_v2g())
        .expand_dims({"NRG_VARIABILITY_I": ["PREDICTOR_EV_DEMANDoV2G"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR_FLEX_DEMAND"]] = (
        predictor_13_flexible_demand()
        .expand_dims(
            {"BASIC_PREDICTORS_NGR_VARIABILITY_I": ["PREDICTOR_FLEX_DEMAND"]}, 1
        )
        .values
    )
    value.loc[:, ["PREDICTOR_HEAT_DEMAND"]] = (
        predictor_5_heat_demand()
        .expand_dims(
            {"BASIC_PREDICTORS_NGR_VARIABILITY_I": ["PREDICTOR_HEAT_DEMAND"]}, 1
        )
        .values
    )
    value.loc[:, ["PREDICTOR_HEAT_DEMANDoCHP"]] = (
        (predictor_5_heat_demand() * predictor_6_chp())
        .expand_dims({"NRG_VARIABILITY_I": ["PREDICTOR_HEAT_DEMANDoCHP"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR_HEAT_DEMANDoELEC_BOILERS"]] = (
        (predictor_5_heat_demand() * predictor_8_electric_boilers())
        .expand_dims({"NRG_VARIABILITY_I": ["PREDICTOR_HEAT_DEMANDoELEC_BOILERS"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR_HEAT_DEMANDoEV_DEMAND"]] = (
        (predictor_5_heat_demand() * predictor_9_electric_vehicle_demand())
        .expand_dims({"NRG_VARIABILITY_I": ["PREDICTOR_HEAT_DEMANDoEV_DEMAND"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR_HEAT_DEMANDoFLEX_DEMAND"]] = (
        (predictor_5_heat_demand() * predictor_13_flexible_demand())
        .expand_dims({"NRG_VARIABILITY_I": ["PREDICTOR_HEAT_DEMANDoFLEX_DEMAND"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR_HEAT_DEMANDoHEAT_PUMPS"]] = (
        (predictor_5_heat_demand() * predictor_7_heat_pumps())
        .expand_dims({"NRG_VARIABILITY_I": ["PREDICTOR_HEAT_DEMANDoHEAT_PUMPS"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR_HEAT_DEMANDoHYDROGEN_DEMAND"]] = (
        (predictor_5_heat_demand() * predictor_11_hydrogen_fe_demand())
        .expand_dims(
            {"NRG_VARIABILITY_I": ["PREDICTOR_HEAT_DEMANDoHYDROGEN_DEMAND"]}, 1
        )
        .values
    )
    value.loc[:, ["PREDICTOR_HEAT_DEMANDoHYDROGEN_SUPPLY"]] = (
        (predictor_5_heat_demand() * predictor_12_hydrogen_supply())
        .expand_dims(
            {"NRG_VARIABILITY_I": ["PREDICTOR_HEAT_DEMANDoHYDROGEN_SUPPLY"]}, 1
        )
        .values
    )
    value.loc[:, ["PREDICTOR_HEAT_DEMANDoV2G"]] = (
        (predictor_5_heat_demand() * predictor_10_v2g())
        .expand_dims({"NRG_VARIABILITY_I": ["PREDICTOR_HEAT_DEMANDoV2G"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR_HEAT_PUMPS"]] = (
        predictor_7_heat_pumps()
        .expand_dims(
            {"BASIC_PREDICTORS_NGR_VARIABILITY_I": ["PREDICTOR_HEAT_PUMPS"]}, 1
        )
        .values
    )
    value.loc[:, ["PREDICTOR_HEAT_PUMPSoELEC_BOILERS"]] = (
        (predictor_7_heat_pumps() * predictor_8_electric_boilers())
        .expand_dims({"NRG_VARIABILITY_I": ["PREDICTOR_HEAT_PUMPSoELEC_BOILERS"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR_HEAT_PUMPSoEV_DEMAND"]] = (
        (predictor_7_heat_pumps() * predictor_9_electric_vehicle_demand())
        .expand_dims({"NRG_VARIABILITY_I": ["PREDICTOR_HEAT_PUMPSoEV_DEMAND"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR_HEAT_PUMPSoFLEX_DEMAND"]] = (
        (predictor_7_heat_pumps() * predictor_13_flexible_demand())
        .expand_dims({"NRG_VARIABILITY_I": ["PREDICTOR_HEAT_PUMPSoFLEX_DEMAND"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR_HEAT_PUMPSoHYDROGEN_DEMAND"]] = (
        (predictor_7_heat_pumps() * predictor_11_hydrogen_fe_demand())
        .expand_dims({"NRG_VARIABILITY_I": ["PREDICTOR_HEAT_PUMPSoHYDROGEN_DEMAND"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR_HEAT_PUMPSoHYDROGEN_SUPPLY"]] = (
        (predictor_7_heat_pumps() * predictor_12_hydrogen_supply())
        .expand_dims({"NRG_VARIABILITY_I": ["PREDICTOR_HEAT_PUMPSoHYDROGEN_SUPPLY"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR_HEAT_PUMPSoV2G"]] = (
        (predictor_7_heat_pumps() * predictor_10_v2g())
        .expand_dims({"NRG_VARIABILITY_I": ["PREDICTOR_HEAT_PUMPSoV2G"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR_HYDROGEN_DEMAND"]] = (
        predictor_11_hydrogen_fe_demand()
        .expand_dims(
            {"BASIC_PREDICTORS_NGR_VARIABILITY_I": ["PREDICTOR_HYDROGEN_DEMAND"]}, 1
        )
        .values
    )
    value.loc[:, ["PREDICTOR_HYDROGEN_DEMANDoFLEX_DEMAND"]] = (
        (predictor_11_hydrogen_fe_demand() * predictor_13_flexible_demand())
        .expand_dims(
            {"NRG_VARIABILITY_I": ["PREDICTOR_HYDROGEN_DEMANDoFLEX_DEMAND"]}, 1
        )
        .values
    )
    value.loc[:, ["PREDICTOR_HYDROGEN_DEMANDoHYDROGEN_SUPPLY"]] = (
        (predictor_11_hydrogen_fe_demand() * predictor_12_hydrogen_supply())
        .expand_dims(
            {"NRG_VARIABILITY_I": ["PREDICTOR_HYDROGEN_DEMANDoHYDROGEN_SUPPLY"]}, 1
        )
        .values
    )
    value.loc[:, ["PREDICTOR_HYDROGEN_SUPPLY"]] = (
        predictor_12_hydrogen_supply()
        .expand_dims(
            {"BASIC_PREDICTORS_NGR_VARIABILITY_I": ["PREDICTOR_HYDROGEN_SUPPLY"]}, 1
        )
        .values
    )
    value.loc[:, ["PREDICTOR_HYDROGEN_SUPPLYoFLEX_DEMAND"]] = (
        (predictor_12_hydrogen_supply() * predictor_13_flexible_demand())
        .expand_dims(
            {"NRG_VARIABILITY_I": ["PREDICTOR_HYDROGEN_SUPPLYoFLEX_DEMAND"]}, 1
        )
        .values
    )
    value.loc[:, ["PREDICTOR_SOLAR"]] = (
        predictor_1_protra_pp_solar()
        .expand_dims({"BASIC_PREDICTORS_NGR_VARIABILITY_I": ["PREDICTOR_SOLAR"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR_SOLARoCHP"]] = (
        (predictor_1_protra_pp_solar() * predictor_6_chp())
        .expand_dims({"NRG_VARIABILITY_I": ["PREDICTOR_SOLARoCHP"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR_SOLARoELEC_BOILERS"]] = (
        (predictor_1_protra_pp_solar() * predictor_8_electric_boilers())
        .expand_dims({"NRG_VARIABILITY_I": ["PREDICTOR_SOLARoELEC_BOILERS"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR_SOLARoEV_DEMAND"]] = (
        (predictor_1_protra_pp_solar() * predictor_9_electric_vehicle_demand())
        .expand_dims({"NRG_VARIABILITY_I": ["PREDICTOR_SOLARoEV_DEMAND"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR_SOLARoFLEX_DEMAND"]] = (
        (predictor_1_protra_pp_solar() * predictor_13_flexible_demand())
        .expand_dims({"NRG_VARIABILITY_I": ["PREDICTOR_SOLARoFLEX_DEMAND"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR_SOLARoHEAT_DEMAND"]] = (
        (predictor_1_protra_pp_solar() * predictor_5_heat_demand())
        .expand_dims({"NRG_VARIABILITY_I": ["PREDICTOR_SOLARoHEAT_DEMAND"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR_SOLARoHEAT_PUMPS"]] = (
        (predictor_1_protra_pp_solar() * predictor_7_heat_pumps())
        .expand_dims({"NRG_VARIABILITY_I": ["PREDICTOR_SOLARoHEAT_PUMPS"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR_SOLARoHYDROGEN_DEMAND"]] = (
        (predictor_1_protra_pp_solar() * predictor_11_hydrogen_fe_demand())
        .expand_dims({"NRG_VARIABILITY_I": ["PREDICTOR_SOLARoHYDROGEN_DEMAND"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR_SOLARoHYDROGEN_SUPPLY"]] = (
        (predictor_1_protra_pp_solar() * predictor_12_hydrogen_supply())
        .expand_dims({"NRG_VARIABILITY_I": ["PREDICTOR_SOLARoHYDROGEN_SUPPLY"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR_SOLARoSTATIONARY_STORAGE"]] = (
        (predictor_1_protra_pp_solar() * predictor_4_stationary_storage())
        .expand_dims({"NRG_VARIABILITY_I": ["PREDICTOR_SOLARoSTATIONARY_STORAGE"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR_SOLARoV2G"]] = (
        (predictor_1_protra_pp_solar() * predictor_10_v2g())
        .expand_dims({"NRG_VARIABILITY_I": ["PREDICTOR_SOLARoV2G"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR_SOLARoWIND"]] = (
        (predictor_1_protra_pp_solar() * predictor_2_protra_pp_wind())
        .expand_dims({"NRG_VARIABILITY_I": ["PREDICTOR_SOLARoWIND"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR_SOLARoZERO_GHG_SEMIFLEX"]] = (
        (predictor_1_protra_pp_solar() * predictor_3_capacity_zero_ghg_semiflex())
        .expand_dims({"NRG_VARIABILITY_I": ["PREDICTOR_SOLARoZERO_GHG_SEMIFLEX"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR_STATIONARY_STORAGE"]] = (
        predictor_4_stationary_storage()
        .expand_dims(
            {"BASIC_PREDICTORS_NGR_VARIABILITY_I": ["PREDICTOR_STATIONARY_STORAGE"]}, 1
        )
        .values
    )
    value.loc[:, ["PREDICTOR_STATIONARY_STORAGEoCHP"]] = (
        (predictor_4_stationary_storage() * predictor_6_chp())
        .expand_dims({"NRG_VARIABILITY_I": ["PREDICTOR_STATIONARY_STORAGEoCHP"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR_STATIONARY_STORAGEoELEC_BOILERS"]] = (
        (predictor_4_stationary_storage() * predictor_8_electric_boilers())
        .expand_dims(
            {"NRG_VARIABILITY_I": ["PREDICTOR_STATIONARY_STORAGEoELEC_BOILERS"]}, 1
        )
        .values
    )
    value.loc[:, ["PREDICTOR_STATIONARY_STORAGEoEV_DEMAND"]] = (
        (predictor_4_stationary_storage() * predictor_9_electric_vehicle_demand())
        .expand_dims(
            {"NRG_VARIABILITY_I": ["PREDICTOR_STATIONARY_STORAGEoEV_DEMAND"]}, 1
        )
        .values
    )
    value.loc[:, ["PREDICTOR_STATIONARY_STORAGEoFLEX_DEMAND"]] = (
        (predictor_4_stationary_storage() * predictor_13_flexible_demand())
        .expand_dims(
            {"NRG_VARIABILITY_I": ["PREDICTOR_STATIONARY_STORAGEoFLEX_DEMAND"]}, 1
        )
        .values
    )
    value.loc[:, ["PREDICTOR_STATIONARY_STORAGEoHEAT_DEMAND"]] = (
        (predictor_4_stationary_storage() * predictor_5_heat_demand())
        .expand_dims(
            {"NRG_VARIABILITY_I": ["PREDICTOR_STATIONARY_STORAGEoHEAT_DEMAND"]}, 1
        )
        .values
    )
    value.loc[:, ["PREDICTOR_STATIONARY_STORAGEoHEAT_PUMPS"]] = (
        (predictor_4_stationary_storage() * predictor_7_heat_pumps())
        .expand_dims(
            {"NRG_VARIABILITY_I": ["PREDICTOR_STATIONARY_STORAGEoHEAT_PUMPS"]}, 1
        )
        .values
    )
    value.loc[:, ["PREDICTOR_STATIONARY_STORAGEoHYDROGEN_DEMAND"]] = (
        (predictor_4_stationary_storage() * predictor_11_hydrogen_fe_demand())
        .expand_dims(
            {"NRG_VARIABILITY_I": ["PREDICTOR_STATIONARY_STORAGEoHYDROGEN_DEMAND"]}, 1
        )
        .values
    )
    value.loc[:, ["PREDICTOR_STATIONARY_STORAGEoHYDROGEN_SUPPLY"]] = (
        (predictor_4_stationary_storage() * predictor_12_hydrogen_supply())
        .expand_dims(
            {"NRG_VARIABILITY_I": ["PREDICTOR_STATIONARY_STORAGEoHYDROGEN_SUPPLY"]}, 1
        )
        .values
    )
    value.loc[:, ["PREDICTOR_STATIONARY_STORAGEoV2G"]] = (
        (predictor_4_stationary_storage() * predictor_10_v2g())
        .expand_dims({"NRG_VARIABILITY_I": ["PREDICTOR_STATIONARY_STORAGEoV2G"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR_V2G"]] = (
        predictor_10_v2g()
        .expand_dims({"BASIC_PREDICTORS_NGR_VARIABILITY_I": ["PREDICTOR_V2G"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR_V2GoFLEX_DEMAND"]] = (
        (predictor_10_v2g() * predictor_13_flexible_demand())
        .expand_dims({"NRG_VARIABILITY_I": ["PREDICTOR_V2GoFLEX_DEMAND"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR_V2GoHYDROGEN_DEMAND"]] = (
        (predictor_10_v2g() * predictor_11_hydrogen_fe_demand())
        .expand_dims({"NRG_VARIABILITY_I": ["PREDICTOR_V2GoHYDROGEN_DEMAND"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR_V2GoHYDROGEN_SUPPLY"]] = (
        (predictor_10_v2g() * predictor_12_hydrogen_supply())
        .expand_dims({"NRG_VARIABILITY_I": ["PREDICTOR_V2GoHYDROGEN_SUPPLY"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR_WIND"]] = (
        predictor_2_protra_pp_wind()
        .expand_dims({"BASIC_PREDICTORS_NGR_VARIABILITY_I": ["PREDICTOR_WIND"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR_WINDoCHP"]] = (
        (predictor_2_protra_pp_wind() * predictor_6_chp())
        .expand_dims({"NRG_VARIABILITY_I": ["PREDICTOR_WINDoCHP"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR_WINDoELEC_BOILERS"]] = (
        (predictor_2_protra_pp_wind() * predictor_8_electric_boilers())
        .expand_dims({"NRG_VARIABILITY_I": ["PREDICTOR_WINDoELEC_BOILERS"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR_WINDoEV_DEMAND"]] = (
        (predictor_2_protra_pp_wind() * predictor_9_electric_vehicle_demand())
        .expand_dims({"NRG_VARIABILITY_I": ["PREDICTOR_WINDoEV_DEMAND"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR_WINDoFLEX_DEMAND"]] = (
        (predictor_2_protra_pp_wind() * predictor_13_flexible_demand())
        .expand_dims({"NRG_VARIABILITY_I": ["PREDICTOR_WINDoFLEX_DEMAND"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR_WINDoHEAT_DEMAND"]] = (
        (predictor_2_protra_pp_wind() * predictor_5_heat_demand())
        .expand_dims({"NRG_VARIABILITY_I": ["PREDICTOR_WINDoHEAT_DEMAND"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR_WINDoHEAT_PUMPS"]] = (
        (predictor_2_protra_pp_wind() * predictor_7_heat_pumps())
        .expand_dims({"NRG_VARIABILITY_I": ["PREDICTOR_WINDoHEAT_PUMPS"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR_WINDoHYDROGEN_DEMAND"]] = (
        (predictor_2_protra_pp_wind() * predictor_11_hydrogen_fe_demand())
        .expand_dims({"NRG_VARIABILITY_I": ["PREDICTOR_WINDoHYDROGEN_DEMAND"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR_WINDoHYDROGEN_SUPPLY"]] = (
        (predictor_2_protra_pp_wind() * predictor_12_hydrogen_supply())
        .expand_dims({"NRG_VARIABILITY_I": ["PREDICTOR_WINDoHYDROGEN_SUPPLY"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR_WINDoSTATIONARY_STORAGE"]] = (
        (predictor_2_protra_pp_wind() * predictor_4_stationary_storage())
        .expand_dims({"NRG_VARIABILITY_I": ["PREDICTOR_WINDoSTATIONARY_STORAGE"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR_WINDoV2G"]] = (
        (predictor_2_protra_pp_wind() * predictor_10_v2g())
        .expand_dims({"NRG_VARIABILITY_I": ["PREDICTOR_WINDoV2G"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR_WINDoZERO_GHG_SEMIFLEX"]] = (
        (predictor_2_protra_pp_wind() * predictor_3_capacity_zero_ghg_semiflex())
        .expand_dims({"NRG_VARIABILITY_I": ["PREDICTOR_WINDoZERO_GHG_SEMIFLEX"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR_ZERO_GHG_SEMIFLEX"]] = (
        predictor_3_capacity_zero_ghg_semiflex()
        .expand_dims(
            {"BASIC_PREDICTORS_NGR_VARIABILITY_I": ["PREDICTOR_ZERO_GHG_SEMIFLEX"]}, 1
        )
        .values
    )
    value.loc[:, ["PREDICTOR_ZERO_GHG_SEMIFLEXoCHP"]] = (
        (predictor_3_capacity_zero_ghg_semiflex() * predictor_6_chp())
        .expand_dims({"NRG_VARIABILITY_I": ["PREDICTOR_ZERO_GHG_SEMIFLEXoCHP"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR_ZERO_GHG_SEMIFLEXoELEC_BOILERS"]] = (
        (predictor_3_capacity_zero_ghg_semiflex() * predictor_8_electric_boilers())
        .expand_dims(
            {"NRG_VARIABILITY_I": ["PREDICTOR_ZERO_GHG_SEMIFLEXoELEC_BOILERS"]}, 1
        )
        .values
    )
    value.loc[:, ["PREDICTOR_ZERO_GHG_SEMIFLEXoEV_DEMAND"]] = (
        (
            predictor_3_capacity_zero_ghg_semiflex()
            * predictor_9_electric_vehicle_demand()
        )
        .expand_dims(
            {"NRG_VARIABILITY_I": ["PREDICTOR_ZERO_GHG_SEMIFLEXoEV_DEMAND"]}, 1
        )
        .values
    )
    value.loc[:, ["PREDICTOR_ZERO_GHG_SEMIFLEXoFLEX_DEMAND"]] = (
        (predictor_3_capacity_zero_ghg_semiflex() * predictor_13_flexible_demand())
        .expand_dims(
            {"NRG_VARIABILITY_I": ["PREDICTOR_ZERO_GHG_SEMIFLEXoFLEX_DEMAND"]}, 1
        )
        .values
    )
    value.loc[:, ["PREDICTOR_ZERO_GHG_SEMIFLEXoHEAT_DEMAND"]] = (
        (predictor_3_capacity_zero_ghg_semiflex() * predictor_5_heat_demand())
        .expand_dims(
            {"NRG_VARIABILITY_I": ["PREDICTOR_ZERO_GHG_SEMIFLEXoHEAT_DEMAND"]}, 1
        )
        .values
    )
    value.loc[:, ["PREDICTOR_ZERO_GHG_SEMIFLEXoHEAT_PUMPS"]] = (
        (predictor_3_capacity_zero_ghg_semiflex() * predictor_7_heat_pumps())
        .expand_dims(
            {"NRG_VARIABILITY_I": ["PREDICTOR_ZERO_GHG_SEMIFLEXoHEAT_PUMPS"]}, 1
        )
        .values
    )
    value.loc[:, ["PREDICTOR_ZERO_GHG_SEMIFLEXoHYDROGEN_DEMAND"]] = (
        (predictor_3_capacity_zero_ghg_semiflex() * predictor_11_hydrogen_fe_demand())
        .expand_dims(
            {"NRG_VARIABILITY_I": ["PREDICTOR_ZERO_GHG_SEMIFLEXoHYDROGEN_DEMAND"]}, 1
        )
        .values
    )
    value.loc[:, ["PREDICTOR_ZERO_GHG_SEMIFLEXoHYDROGEN_SUPPLY"]] = (
        (predictor_3_capacity_zero_ghg_semiflex() * predictor_12_hydrogen_supply())
        .expand_dims(
            {"NRG_VARIABILITY_I": ["PREDICTOR_ZERO_GHG_SEMIFLEXoHYDROGEN_SUPPLY"]}, 1
        )
        .values
    )
    value.loc[:, ["PREDICTOR_ZERO_GHG_SEMIFLEXoSTATIONARY_STORAGE"]] = (
        (predictor_3_capacity_zero_ghg_semiflex() * predictor_4_stationary_storage())
        .expand_dims(
            {"NRG_VARIABILITY_I": ["PREDICTOR_ZERO_GHG_SEMIFLEXoSTATIONARY_STORAGE"]}, 1
        )
        .values
    )
    value.loc[:, ["PREDICTOR_ZERO_GHG_SEMIFLEXoV2G"]] = (
        (predictor_3_capacity_zero_ghg_semiflex() * predictor_10_v2g())
        .expand_dims({"NRG_VARIABILITY_I": ["PREDICTOR_ZERO_GHG_SEMIFLEXoV2G"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR_SOLARoSOLAR"]] = (
        (predictor_1_protra_pp_solar() * predictor_1_protra_pp_solar())
        .expand_dims({"NRG_VARIABILITY_I": ["PREDICTOR_SOLARoSOLAR"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR_WINDoWIND"]] = (
        (predictor_2_protra_pp_wind() * predictor_2_protra_pp_wind())
        .expand_dims({"NRG_VARIABILITY_I": ["PREDICTOR_WINDoWIND"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR_ZERO_GHG_SEMIFLEXoZERO_GHG_SEMIFLEX"]] = (
        (
            predictor_3_capacity_zero_ghg_semiflex()
            * predictor_3_capacity_zero_ghg_semiflex()
        )
        .expand_dims(
            {"NRG_VARIABILITY_I": ["PREDICTOR_ZERO_GHG_SEMIFLEXoZERO_GHG_SEMIFLEX"]}, 1
        )
        .values
    )
    value.loc[:, ["PREDICTOR_STATIONARY_STORAGEoSTATIONARY_STORAGE"]] = (
        (predictor_4_stationary_storage() * predictor_4_stationary_storage())
        .expand_dims(
            {"NRG_VARIABILITY_I": ["PREDICTOR_STATIONARY_STORAGEoSTATIONARY_STORAGE"]},
            1,
        )
        .values
    )
    value.loc[:, ["PREDICTOR_HEAT_DEMANDoHEAT_DEMAND"]] = (
        (predictor_5_heat_demand() * predictor_5_heat_demand())
        .expand_dims({"NRG_VARIABILITY_I": ["PREDICTOR_HEAT_DEMANDoHEAT_DEMAND"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR_CHPoCHP"]] = (
        (predictor_6_chp() * predictor_6_chp())
        .expand_dims({"NRG_VARIABILITY_I": ["PREDICTOR_CHPoCHP"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR_HEAT_PUMPSoHEAT_PUMPS"]] = (
        (predictor_7_heat_pumps() * predictor_7_heat_pumps())
        .expand_dims({"NRG_VARIABILITY_I": ["PREDICTOR_HEAT_PUMPSoHEAT_PUMPS"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR_ELEC_BOILERSoELEC_BOILERS"]] = (
        (predictor_8_electric_boilers() * predictor_8_electric_boilers())
        .expand_dims({"NRG_VARIABILITY_I": ["PREDICTOR_ELEC_BOILERSoELEC_BOILERS"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR_EV_DEMANDoEV_DEMAND"]] = (
        (predictor_9_electric_vehicle_demand() * predictor_9_electric_vehicle_demand())
        .expand_dims({"NRG_VARIABILITY_I": ["PREDICTOR_EV_DEMANDoEV_DEMAND"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR_V2GoV2G"]] = (
        (predictor_10_v2g() * predictor_10_v2g())
        .expand_dims({"NRG_VARIABILITY_I": ["PREDICTOR_V2GoV2G"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR_HYDROGEN_DEMANDoHYDROGEN_DEMAND"]] = (
        (predictor_11_hydrogen_fe_demand() * predictor_11_hydrogen_fe_demand())
        .expand_dims(
            {"NRG_VARIABILITY_I": ["PREDICTOR_HYDROGEN_DEMANDoHYDROGEN_DEMAND"]}, 1
        )
        .values
    )
    value.loc[:, ["PREDICTOR_HYDROGEN_SUPPLYoHYDROGEN_SUPPLY"]] = (
        (predictor_12_hydrogen_supply() * predictor_12_hydrogen_supply())
        .expand_dims(
            {"NRG_VARIABILITY_I": ["PREDICTOR_HYDROGEN_SUPPLYoHYDROGEN_SUPPLY"]}, 1
        )
        .values
    )
    value.loc[:, ["PREDICTOR_FLEX_DEMANDoFLEX_DEMAND"]] = (
        (predictor_13_flexible_demand() * predictor_13_flexible_demand())
        .expand_dims({"NRG_VARIABILITY_I": ["PREDICTOR_FLEX_DEMANDoFLEX_DEMAND"]}, 1)
        .values
    )
    return value


@component.add(
    name="PROSUP_P2H_electric_boiler_heat_generation_regression",
    units="TWh",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "predictor_8_electric_boilers": 8,
        "predictor_11_hydrogen_fe_demand": 12,
        "predictor_7_heat_pumps": 10,
        "predictor_1_protra_pp_solar": 4,
        "predictor_3_capacity_zero_ghg_semiflex": 16,
        "predictor_2_protra_pp_wind": 8,
        "predictor_13_flexible_demand": 2,
        "predictor_5_heat_demand": 2,
    },
)
def prosup_p2h_electric_boiler_heat_generation_regression():
    """
    Heat generation by electric boilers. Output in regressions with EnergyPLAN. This variable is de-normalized in the next step.
    """
    return if_then_else(
        -0.289619
        - 2.4388e-06
        * (predictor_8_electric_boilers() * predictor_11_hydrogen_fe_demand())
        + 0.000180101 * predictor_7_heat_pumps()
        - 1.57226e-08 * (predictor_7_heat_pumps() * predictor_8_electric_boilers())
        + 1.18251e-05 * (predictor_7_heat_pumps() * predictor_11_hydrogen_fe_demand())
        - 0.0710187 * predictor_11_hydrogen_fe_demand()
        - 1.19822e-06
        * (predictor_1_protra_pp_solar() * predictor_11_hydrogen_fe_demand())
        + 1.22396e-08
        * (predictor_1_protra_pp_solar() * predictor_3_capacity_zero_ghg_semiflex())
        + 1.04038e-08 * (predictor_2_protra_pp_wind() * predictor_8_electric_boilers())
        - 2.28912e-08 * (predictor_2_protra_pp_wind() * predictor_7_heat_pumps())
        - 7.55627e-07
        * (predictor_2_protra_pp_wind() * predictor_11_hydrogen_fe_demand())
        + 3.49514e-08
        * (predictor_2_protra_pp_wind() * predictor_3_capacity_zero_ghg_semiflex())
        + 0.000428146 * predictor_3_capacity_zero_ghg_semiflex()
        + 2.2767e-08
        * (predictor_3_capacity_zero_ghg_semiflex() * predictor_8_electric_boilers())
        + 5.52266e-07
        * (predictor_3_capacity_zero_ghg_semiflex() * predictor_13_flexible_demand())
        + 4.93622e-07
        * (predictor_3_capacity_zero_ghg_semiflex() * predictor_5_heat_demand())
        - 7.5073e-08
        * (predictor_3_capacity_zero_ghg_semiflex() * predictor_7_heat_pumps())
        - 6.74654e-06
        * (predictor_3_capacity_zero_ghg_semiflex() * predictor_11_hydrogen_fe_demand())
        < 0,
        lambda: xr.DataArray(
            0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
        ),
        lambda: -0.289619
        - 2.4388e-06
        * (predictor_8_electric_boilers() * predictor_11_hydrogen_fe_demand())
        + 0.000180101 * predictor_7_heat_pumps()
        - 1.57226e-08 * (predictor_7_heat_pumps() * predictor_8_electric_boilers())
        + 1.18251e-05 * (predictor_7_heat_pumps() * predictor_11_hydrogen_fe_demand())
        - 0.0710187 * predictor_11_hydrogen_fe_demand()
        - 1.19822e-06
        * (predictor_1_protra_pp_solar() * predictor_11_hydrogen_fe_demand())
        + 1.22396e-08
        * (predictor_1_protra_pp_solar() * predictor_3_capacity_zero_ghg_semiflex())
        + 1.04038e-08 * (predictor_2_protra_pp_wind() * predictor_8_electric_boilers())
        - 2.28912e-08 * (predictor_2_protra_pp_wind() * predictor_7_heat_pumps())
        - 7.55627e-07
        * (predictor_2_protra_pp_wind() * predictor_11_hydrogen_fe_demand())
        + 3.49514e-08
        * (predictor_2_protra_pp_wind() * predictor_3_capacity_zero_ghg_semiflex())
        + 0.000428146 * predictor_3_capacity_zero_ghg_semiflex()
        + 2.2767e-08
        * (predictor_3_capacity_zero_ghg_semiflex() * predictor_8_electric_boilers())
        + 5.52266e-07
        * (predictor_3_capacity_zero_ghg_semiflex() * predictor_13_flexible_demand())
        + 4.93622e-07
        * (predictor_3_capacity_zero_ghg_semiflex() * predictor_5_heat_demand())
        - 7.5073e-08
        * (predictor_3_capacity_zero_ghg_semiflex() * predictor_7_heat_pumps())
        - 6.74654e-06
        * (
            predictor_3_capacity_zero_ghg_semiflex() * predictor_11_hydrogen_fe_demand()
        ),
    )


@component.add(
    name="PROSUP_P2H_electric_boiler_heat_generation_scaled",
    units="TWh",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "prosup_p2h_capacity_stock": 1,
        "prosup_p2h_electric_boiler_heat_generation_regression": 1,
        "legacy_elec_demand": 1,
        "legacy_elec_demand_energyplan": 1,
    },
)
def prosup_p2h_electric_boiler_heat_generation_scaled():
    """
    Heat generation by electric boilers. Output of the regression scaled from the normalized system to the regional one
    """
    return if_then_else(
        prosup_p2h_capacity_stock()
        .loc[:, "PROSUP_P2H_electric_boiler"]
        .reset_coords(drop=True)
        <= 0,
        lambda: xr.DataArray(
            0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
        ),
        lambda: prosup_p2h_electric_boiler_heat_generation_regression()
        * legacy_elec_demand()
        / legacy_elec_demand_energyplan(),
    )


@component.add(
    name="PROSUP_P2H_heat_pump_heat_generation_scaled",
    units="EJ/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "prosup_p2h_capacity_stock": 1,
        "fe_excluding_trade": 1,
        "prosup_p2h_heat_pump_heat_share_regression": 1,
    },
)
def prosup_p2h_heat_pump_heat_generation_scaled():
    """
    Generation of heat by heat pumps
    """
    return if_then_else(
        prosup_p2h_capacity_stock()
        .loc[:, "PROSUP_P2H_heat_pump"]
        .reset_coords(drop=True)
        <= 0,
        lambda: xr.DataArray(
            0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
        ),
        lambda: fe_excluding_trade().loc[:, "FE_heat"].reset_coords(drop=True)
        * prosup_p2h_heat_pump_heat_share_regression(),
    )


@component.add(
    name="PROSUP_P2H_heat_pump_heat_share_regression",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "predictor_6_chp": 18,
        "predictor_7_heat_pumps": 18,
        "predictor_11_hydrogen_fe_demand": 15,
        "predictor_5_heat_demand": 12,
        "predictor_1_protra_pp_solar": 3,
        "predictor_2_protra_pp_wind": 9,
        "predictor_3_capacity_zero_ghg_semiflex": 15,
        "predictor_13_flexible_demand": 3,
    },
)
def prosup_p2h_heat_pump_heat_share_regression():
    """
    Generaition of heat by heat pumps(share of the heat demand). Output in regressions with EnergyPLAN. R-squared (adjusted) = 0.9071
    """
    return if_then_else(
        0
        + 2.6107e-05 * predictor_6_chp()
        + 3.53785e-09 * (predictor_6_chp() * predictor_7_heat_pumps())
        + 7.17404e-07 * (predictor_6_chp() * predictor_11_hydrogen_fe_demand())
        - 0.00408913 * predictor_5_heat_demand()
        + 3.8269e-08 * (predictor_5_heat_demand() * predictor_6_chp())
        - 1.37004e-07 * (predictor_5_heat_demand() * predictor_7_heat_pumps())
        + 4.15105e-05 * (predictor_5_heat_demand() * predictor_11_hydrogen_fe_demand())
        - 6.84634e-07 * (predictor_7_heat_pumps() * predictor_11_hydrogen_fe_demand())
        - 0.0353161 * predictor_11_hydrogen_fe_demand()
        + 5.78904e-10 * (predictor_1_protra_pp_solar() * predictor_7_heat_pumps())
        + 1.45937e-05 * predictor_2_protra_pp_wind()
        - 7.40645e-10 * (predictor_2_protra_pp_wind() * predictor_6_chp())
        + 1.64839e-09 * (predictor_2_protra_pp_wind() * predictor_7_heat_pumps())
        + 3.32574e-05 * predictor_3_capacity_zero_ghg_semiflex()
        - 4.10826e-09 * (predictor_3_capacity_zero_ghg_semiflex() * predictor_6_chp())
        + 4.79075e-08
        * (predictor_3_capacity_zero_ghg_semiflex() * predictor_13_flexible_demand())
        + 5.15414e-09
        * (predictor_3_capacity_zero_ghg_semiflex() * predictor_7_heat_pumps())
        + 9.41246e-07
        * (predictor_3_capacity_zero_ghg_semiflex() * predictor_11_hydrogen_fe_demand())
        < 0,
        lambda: xr.DataArray(
            0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
        ),
        lambda: if_then_else(
            0
            + 2.6107e-05 * predictor_6_chp()
            + 3.53785e-09 * (predictor_6_chp() * predictor_7_heat_pumps())
            + 7.17404e-07 * (predictor_6_chp() * predictor_11_hydrogen_fe_demand())
            - 0.00408913 * predictor_5_heat_demand()
            + 3.8269e-08 * (predictor_5_heat_demand() * predictor_6_chp())
            - 1.37004e-07 * (predictor_5_heat_demand() * predictor_7_heat_pumps())
            + 4.15105e-05
            * (predictor_5_heat_demand() * predictor_11_hydrogen_fe_demand())
            - 6.84634e-07
            * (predictor_7_heat_pumps() * predictor_11_hydrogen_fe_demand())
            - 0.0353161 * predictor_11_hydrogen_fe_demand()
            + 5.78904e-10 * (predictor_1_protra_pp_solar() * predictor_7_heat_pumps())
            + 1.45937e-05 * predictor_2_protra_pp_wind()
            - 7.40645e-10 * (predictor_2_protra_pp_wind() * predictor_6_chp())
            + 1.64839e-09 * (predictor_2_protra_pp_wind() * predictor_7_heat_pumps())
            + 3.32574e-05 * predictor_3_capacity_zero_ghg_semiflex()
            - 4.10826e-09
            * (predictor_3_capacity_zero_ghg_semiflex() * predictor_6_chp())
            + 4.79075e-08
            * (
                predictor_3_capacity_zero_ghg_semiflex()
                * predictor_13_flexible_demand()
            )
            + 5.15414e-09
            * (predictor_3_capacity_zero_ghg_semiflex() * predictor_7_heat_pumps())
            + 9.41246e-07
            * (
                predictor_3_capacity_zero_ghg_semiflex()
                * predictor_11_hydrogen_fe_demand()
            )
            > 1,
            lambda: xr.DataArray(
                1, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
            ),
            lambda: 0
            + 2.6107e-05 * predictor_6_chp()
            + 3.53785e-09 * (predictor_6_chp() * predictor_7_heat_pumps())
            + 7.17404e-07 * (predictor_6_chp() * predictor_11_hydrogen_fe_demand())
            - 0.00408913 * predictor_5_heat_demand()
            + 3.8269e-08 * (predictor_5_heat_demand() * predictor_6_chp())
            - 1.37004e-07 * (predictor_5_heat_demand() * predictor_7_heat_pumps())
            + 4.15105e-05
            * (predictor_5_heat_demand() * predictor_11_hydrogen_fe_demand())
            - 6.84634e-07
            * (predictor_7_heat_pumps() * predictor_11_hydrogen_fe_demand())
            - 0.0353161 * predictor_11_hydrogen_fe_demand()
            + 5.78904e-10 * (predictor_1_protra_pp_solar() * predictor_7_heat_pumps())
            + 1.45937e-05 * predictor_2_protra_pp_wind()
            - 7.40645e-10 * (predictor_2_protra_pp_wind() * predictor_6_chp())
            + 1.64839e-09 * (predictor_2_protra_pp_wind() * predictor_7_heat_pumps())
            + 3.32574e-05 * predictor_3_capacity_zero_ghg_semiflex()
            - 4.10826e-09
            * (predictor_3_capacity_zero_ghg_semiflex() * predictor_6_chp())
            + 4.79075e-08
            * (
                predictor_3_capacity_zero_ghg_semiflex()
                * predictor_13_flexible_demand()
            )
            + 5.15414e-09
            * (predictor_3_capacity_zero_ghg_semiflex() * predictor_7_heat_pumps())
            + 9.41246e-07
            * (
                predictor_3_capacity_zero_ghg_semiflex()
                * predictor_11_hydrogen_fe_demand()
            ),
        ),
    )


@component.add(
    name="PROSUP_storage_heat_losses_regression",
    units="EJ/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "fe_excluding_trade": 1,
        "share_storage_heat_losses": 1,
        "input_prosup_storage_heat_bounded": 1,
    },
)
def prosup_storage_heat_losses_regression():
    """
    Storage heat losses
    """
    return fe_excluding_trade().loc[:, "FE_heat"].reset_coords(drop=True) * (
        input_prosup_storage_heat_bounded() * share_storage_heat_losses()
    )


@component.add(
    name="SELECT_NRG_VARIABILITY_TYPE_REGRESSION",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_select_nrg_variability_type_regression"},
)
def select_nrg_variability_type_regression():
    """
    Selection of the type of regresssion to consider the variability of renewable energy sources 0: multiple linear regression models 1: multiple logistic regression models
    """
    return _ext_constant_select_nrg_variability_type_regression()


_ext_constant_select_nrg_variability_type_regression = ExtConstant(
    "model_parameters/energy/intermittency_coefficients.xlsx",
    "SELECT_regression_method",
    "SELECT_NRG_VARIABILITY_TYPE_REGRESSION",
    {},
    _root,
    {},
    "_ext_constant_select_nrg_variability_type_regression",
)


@component.add(
    name="share_storage_heat_losses",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="Normal",
)
def share_storage_heat_losses():
    """
    Share of losses in heat storage, based on the input to the facilities. This value needs to be justified.
    """
    return 0.1


@component.add(
    name="SWITCH_NRG_VARIABILITY",
    units="DMNL/per_year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_nrg_variability"},
)
def switch_nrg_variability():
    """
    This switch can take two values: 0: the energy variability equations are activated and the (sub)module runs integrated with the rest of WILIAM. 1: the (sub)module imports exogenous constants, i.e., WILIAM does not see the energy variability in the generation of energy (RES would appear as fully dispatachable).
    """
    return _ext_constant_switch_nrg_variability()


_ext_constant_switch_nrg_variability = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_NRG_VARIABILITY",
    {},
    _root,
    {},
    "_ext_constant_switch_nrg_variability",
)


@component.add(
    name="SWITCH_TEST_NRG_ACTIVATE_P2H_REGRESSIONS",
    units="DMML",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_switch_test_nrg_activate_p2h_regressions"
    },
)
def switch_test_nrg_activate_p2h_regressions():
    """
    0: P2H technologies are not considered in the energy variability submodule. 1: P2H technologies are considered in the energy variability submodule.
    """
    return _ext_constant_switch_test_nrg_activate_p2h_regressions()


_ext_constant_switch_test_nrg_activate_p2h_regressions = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_TEST_NRG_ACTIVATE_P2H_REGRESSIONS",
    {},
    _root,
    {},
    "_ext_constant_switch_test_nrg_activate_p2h_regressions",
)


@component.add(
    name="variation_CF_curtailed_PROTRA",
    units="DMNL",
    subscripts=["REGIONS_9_I", "NRG_COMMODITIES_I", "NRG_PROTRA_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_nrg_variability_type_regression": 3,
        "outputs_linear_regression": 3,
        "outputs_logistic_regression": 3,
    },
)
def variation_cf_curtailed_protra():
    """
    Variation from the maximum capacity factor of PROTRA technologies. This indicator hence ranges 0-1 (0 means CF=0% and 1 means CF= maximum possible CF without curtailment).
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "NRG_COMMODITIES_I": _subscript_dict["NRG_COMMODITIES_I"],
            "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
        },
        ["REGIONS_9_I", "NRG_COMMODITIES_I", "NRG_PROTRA_I"],
    )
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[:, ["TO_elec"], :] = True
    except_subs.loc[:, ["TO_elec"], _subscript_dict["PROTRA_WIND_I"]] = False
    except_subs.loc[:, ["TO_elec"], ["PROTRA_PP_solar_CSP"]] = False
    except_subs.loc[:, ["TO_elec"], ["PROTRA_PP_solar_open_space_PV"]] = False
    value.values[except_subs.values] = 0
    value.loc[:, ["TO_elec"], _subscript_dict["PROTRA_WIND_I"]] = (
        if_then_else(
            select_nrg_variability_type_regression() == 0,
            lambda: outputs_linear_regression()
            .loc[:, "OUTPUT_WIND_CF_DECLINE"]
            .reset_coords(drop=True),
            lambda: outputs_logistic_regression()
            .loc[:, "OUTPUT_WIND_CF_DECLINE"]
            .reset_coords(drop=True),
        )
        .expand_dims({"NRG_COMMODITIES_I": ["TO_elec"]}, 1)
        .expand_dims({"PROTRA_WIND_I": _subscript_dict["PROTRA_WIND_I"]}, 2)
        .values
    )
    value.loc[:, ["TO_elec"], ["PROTRA_PP_solar_CSP"]] = (
        if_then_else(
            select_nrg_variability_type_regression() == 0,
            lambda: outputs_linear_regression()
            .loc[:, "OUTPUT_SOLAR_CF_DECLINE"]
            .reset_coords(drop=True),
            lambda: outputs_logistic_regression()
            .loc[:, "OUTPUT_SOLAR_CF_DECLINE"]
            .reset_coords(drop=True),
        )
        .expand_dims({"NRG_COMMODITIES_I": ["TO_elec"]}, 1)
        .expand_dims({"NRG_PRO_I": ["PROTRA_PP_solar_CSP"]}, 2)
        .values
    )
    value.loc[:, ["TO_elec"], ["PROTRA_PP_solar_open_space_PV"]] = (
        if_then_else(
            select_nrg_variability_type_regression() == 0,
            lambda: outputs_linear_regression()
            .loc[:, "OUTPUT_SOLAR_CF_DECLINE"]
            .reset_coords(drop=True),
            lambda: outputs_logistic_regression()
            .loc[:, "OUTPUT_SOLAR_CF_DECLINE"]
            .reset_coords(drop=True),
        )
        .expand_dims({"NRG_COMMODITIES_I": ["TO_elec"]}, 1)
        .expand_dims({"NRG_PRO_I": ["PROTRA_PP_solar_open_space_PV"]}, 2)
        .values
    )
    return value
