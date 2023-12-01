"""
Module demography.feedbacks
Translated using PySD version 3.10.0
"""


@component.add(
    name="change_life_expectancy_at_birth",
    units="Years/Year",
    subscripts=["REGIONS_35_I", "SEX_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_x2dem_life_expectancy_at_birth": 1,
        "switch_demography": 1,
        "time": 2,
        "variation_historical_life_expectancy_at_birth": 2,
        "slope_ramp_life_expectancy_at_birth": 1,
        "last_historical_year_demography": 2,
        "endogenous_feedbacks_to_life_expectancy_at_birth": 1,
    },
)
def change_life_expectancy_at_birth():
    """
    Variation in the life expectancy at birth
    """
    return if_then_else(
        np.logical_or(
            switch_x2dem_life_expectancy_at_birth() == 0, switch_demography() == 0
        ),
        lambda: if_then_else(
            time() < last_historical_year_demography(),
            lambda: variation_historical_life_expectancy_at_birth(),
            lambda: slope_ramp_life_expectancy_at_birth(),
        ),
        lambda: if_then_else(
            time() < last_historical_year_demography(),
            lambda: variation_historical_life_expectancy_at_birth(),
            lambda: endogenous_feedbacks_to_life_expectancy_at_birth(),
        ),
    )


@component.add(
    name="COEFFICIENT_FEEDBACK_CO2_EMISSIONS_TO_LIFE_EXPECTANCY_AT_BIRTH",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_coefficient_feedback_co2_emissions_to_life_expectancy_at_birth"
    },
)
def coefficient_feedback_co2_emissions_to_life_expectancy_at_birth():
    """
    Coefficient of the feedback from annual CO2 emissions on health to life expectancy at birth. Source: (Majeed et all, 2020)
    """
    return (
        _ext_constant_coefficient_feedback_co2_emissions_to_life_expectancy_at_birth()
    )


_ext_constant_coefficient_feedback_co2_emissions_to_life_expectancy_at_birth = (
    ExtConstant(
        "model_parameters/demography/demography.xlsx",
        "DATA_LOADING",
        "COEFFICIENT_FEEDBACK_CO2_EMISSIONS_TO_LIFE_EXPECTANCY_AT_BIRTH",
        {},
        _root,
        {},
        "_ext_constant_coefficient_feedback_co2_emissions_to_life_expectancy_at_birth",
    )
)


@component.add(
    name="COEFFICIENT_FEEDBACK_EDUCATION_EXPENDITURE_TO_LIFE_EXPECTANCY_AT_BIRTH",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_coefficient_feedback_education_expenditure_to_life_expectancy_at_birth"
    },
)
def coefficient_feedback_education_expenditure_to_life_expectancy_at_birth():
    """
    Coefficient of the feedback from governemnt education to life expectancy at birth. Source: (Wigley and Akkoyunly-Wigley, 2006)
    """
    return (
        _ext_constant_coefficient_feedback_education_expenditure_to_life_expectancy_at_birth()
    )


_ext_constant_coefficient_feedback_education_expenditure_to_life_expectancy_at_birth = ExtConstant(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "COEFFICIENT_FEEDBACK_EDUCATION_EXPENDITURE_TO_LIFE_EXPECTANCY_AT_BIRTH",
    {},
    _root,
    {},
    "_ext_constant_coefficient_feedback_education_expenditure_to_life_expectancy_at_birth",
)


@component.add(
    name="COEFFICIENT_FEEDBACK_HEALTH_EXPENDITURE_TO_LIFE_EXPECTANCY_AT_BIRTH",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_coefficient_feedback_health_expenditure_to_life_expectancy_at_birth"
    },
)
def coefficient_feedback_health_expenditure_to_life_expectancy_at_birth():
    """
    Coefficient of the feedback from governemnt expenditure on health to life expectancy at birth. Source: (Rahman et al., 2022)
    """
    return (
        _ext_constant_coefficient_feedback_health_expenditure_to_life_expectancy_at_birth()
    )


_ext_constant_coefficient_feedback_health_expenditure_to_life_expectancy_at_birth = ExtConstant(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "COEFFICIENT_FEEDBACK_HEALTH_EXPENDITURE_TO_LIFE_EXPECTANCY_AT_BIRTH",
    {},
    _root,
    {},
    "_ext_constant_coefficient_feedback_health_expenditure_to_life_expectancy_at_birth",
)


@component.add(
    name="delayed_historical_life_expectancy_at_birth",
    units="Year",
    subscripts=["REGIONS_35_I", "SEX_I"],
    comp_type="Stateful",
    comp_subtype="Delay",
    depends_on={"_delay_delayed_historical_life_expectancy_at_birth": 1},
    other_deps={
        "_delay_delayed_historical_life_expectancy_at_birth": {
            "initial": {"historical_life_expectancy_at_birth": 1},
            "step": {"historical_life_expectancy_at_birth": 1},
        }
    },
)
def delayed_historical_life_expectancy_at_birth():
    """
    Delayed one year the historical life expectancy at birth
    """
    return _delay_delayed_historical_life_expectancy_at_birth()


_delay_delayed_historical_life_expectancy_at_birth = Delay(
    lambda: historical_life_expectancy_at_birth(),
    lambda: xr.DataArray(
        1,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "SEX_I": _subscript_dict["SEX_I"],
        },
        ["REGIONS_35_I", "SEX_I"],
    ),
    lambda: historical_life_expectancy_at_birth(),
    lambda: 1,
    time_step,
    "_delay_delayed_historical_life_expectancy_at_birth",
)


@component.add(
    name="endogenous_feedbacks_to_life_expectancy_at_birth",
    units="Years",
    subscripts=["REGIONS_35_I", "SEX_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "historical_life_expectancy_at_birth": 1,
        "coefficient_feedback_health_expenditure_to_life_expectancy_at_birth": 1,
        "coefficient_feedback_co2_emissions_to_life_expectancy_at_birth": 1,
        "annual_variation_regional_average_schooling_time": 1,
        "annual_variation_co2_emissions": 1,
        "coefficient_feedback_education_expenditure_to_life_expectancy_at_birth": 1,
        "annual_variation_government_expenditure": 1,
        "maximum_increase_life_expectancy_at_birth_by_health_expenditure": 1,
    },
)
def endogenous_feedbacks_to_life_expectancy_at_birth():
    """
    Additional (+) or penalty (-) in the life expectancy at birth indicator. Feedbacks to the demogrphy module
    """
    return historical_life_expectancy_at_birth() * (
        np.minimum(
            annual_variation_government_expenditure()
            .loc[:, "HEALTH_COFOG"]
            .reset_coords(drop=True)
            * coefficient_feedback_health_expenditure_to_life_expectancy_at_birth(),
            maximum_increase_life_expectancy_at_birth_by_health_expenditure(),
        )
        + annual_variation_regional_average_schooling_time()
        * coefficient_feedback_education_expenditure_to_life_expectancy_at_birth()
        + (
            annual_variation_co2_emissions()
            * coefficient_feedback_co2_emissions_to_life_expectancy_at_birth()
        )
    )


@component.add(
    name="final_value_life_expectancy_at_birth",
    units="Years/(Years*Years)",
    subscripts=["REGIONS_35_I", "SEX_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "objective_life_expectancy_at_birth_sp": 2,
        "life_expectancy_at_birth_minimums_sp": 1,
        "life_expectancy_at_birth_averages_sp": 1,
        "life_expectancy_at_birth_maximums_sp": 1,
    },
)
def final_value_life_expectancy_at_birth():
    """
    SSPs scenarios are not modelled for now. This variable makes 0 changes in life expectancy at birth as of 2020 (last year of historical data).
    """
    return if_then_else(
        (objective_life_expectancy_at_birth_sp() == 1).expand_dims(
            {"SEX_I": _subscript_dict["SEX_I"]}, 1
        ),
        lambda: life_expectancy_at_birth_minimums_sp(),
        lambda: if_then_else(
            (objective_life_expectancy_at_birth_sp() == 2).expand_dims(
                {"SEX_I": _subscript_dict["SEX_I"]}, 1
            ),
            lambda: life_expectancy_at_birth_averages_sp(),
            lambda: life_expectancy_at_birth_maximums_sp(),
        ),
    )


@component.add(
    name="LAST_HISTORICAL_YEAR_DEMOGRAPHY",
    units="Year",
    comp_type="Constant",
    comp_subtype="Normal",
)
def last_historical_year_demography():
    """
    Last year of the historical period, according to the demography data
    """
    return 2020


@component.add(
    name="life_expectancy_at_birth",
    units="Year",
    subscripts=["REGIONS_35_I", "SEX_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_life_expectancy_at_birth": 1},
    other_deps={
        "_integ_life_expectancy_at_birth": {
            "initial": {"historical_life_expectancy_at_birth": 1},
            "step": {"change_life_expectancy_at_birth": 1},
        }
    },
)
def life_expectancy_at_birth():
    """
    Life expectancy at birth of population
    """
    return _integ_life_expectancy_at_birth()


_integ_life_expectancy_at_birth = Integ(
    lambda: change_life_expectancy_at_birth(),
    lambda: historical_life_expectancy_at_birth(),
    "_integ_life_expectancy_at_birth",
)


@component.add(
    name="MAXIMUM_INCREASE_LIFE_EXPECTANCY_AT_BIRTH_BY_HEALTH_EXPENDITURE",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_maximum_increase_life_expectancy_at_birth_by_health_expenditure"
    },
)
def maximum_increase_life_expectancy_at_birth_by_health_expenditure():
    """
    Top limit to the increase of life expectancy at birth due to government expenditures on health. Source: (Aisa et al., 2014)
    """
    return (
        _ext_constant_maximum_increase_life_expectancy_at_birth_by_health_expenditure()
    )


_ext_constant_maximum_increase_life_expectancy_at_birth_by_health_expenditure = (
    ExtConstant(
        "model_parameters/demography/demography.xlsx",
        "DATA_LOADING",
        "MAXIMUM_INCREASE_LIFE_EXPECTANCY_AT_BIRTH_BY_HEALTH_EXPENDITURE",
        {},
        _root,
        {},
        "_ext_constant_maximum_increase_life_expectancy_at_birth_by_health_expenditure",
    )
)


@component.add(
    name="slope_ramp_life_expectancy_at_birth",
    units="Years",
    subscripts=["REGIONS_35_I", "SEX_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "final_value_life_expectancy_at_birth": 1,
        "historical_life_expectancy_at_birth": 1,
        "target_year_life_expectancy_at_birth_sp": 1,
        "last_historical_year_demography": 1,
    },
)
def slope_ramp_life_expectancy_at_birth():
    """
    Slope of the ramp to create the scenario for the life expectancy at birth
    """
    return (
        final_value_life_expectancy_at_birth() - historical_life_expectancy_at_birth()
    ) / (target_year_life_expectancy_at_birth_sp() - last_historical_year_demography())


@component.add(
    name="SWITCH_X2DEM_LIFE_EXPECTANCY_AT_BIRTH",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_x2dem_life_expectancy_at_birth"},
)
def switch_x2dem_life_expectancy_at_birth():
    """
    Switch to choose between (0) exogenous pathway and (1) endogenous feedbacks for life expectancy at birth with inputs from economy, energy and society modules.
    """
    return _ext_constant_switch_x2dem_life_expectancy_at_birth()


_ext_constant_switch_x2dem_life_expectancy_at_birth = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_X2DEM_LIFE_EXPECTANCY_AT_BIRTH",
    {},
    _root,
    {},
    "_ext_constant_switch_x2dem_life_expectancy_at_birth",
)


@component.add(
    name="variation_historical_life_expectancy_at_birth",
    units="Year",
    subscripts=["REGIONS_35_I", "SEX_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "historical_life_expectancy_at_birth": 1,
        "delayed_historical_life_expectancy_at_birth": 1,
    },
)
def variation_historical_life_expectancy_at_birth():
    """
    Variation in the historical life expectancy at birth
    """
    return (
        historical_life_expectancy_at_birth()
        - delayed_historical_life_expectancy_at_birth()
    )
