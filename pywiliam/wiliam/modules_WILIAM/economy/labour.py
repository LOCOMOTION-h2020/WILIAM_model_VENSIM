"""
Module economy.labour
Translated using PySD version 3.10.0
"""


@component.add(
    name="annual_growth_labour_productivity",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 3,
        "aux_growth_labour_productivity": 1,
        "annual_labour_productivity_variation": 1,
    },
)
def annual_growth_labour_productivity():
    return if_then_else(
        time() < 2015,
        lambda: xr.DataArray(
            0,
            {
                "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                "SECTORS_I": _subscript_dict["SECTORS_I"],
            },
            ["REGIONS_35_I", "SECTORS_I"],
        ),
        lambda: if_then_else(
            time() == integer(time()),
            lambda: annual_labour_productivity_variation(),
            lambda: aux_growth_labour_productivity(),
        ),
    )


@component.add(
    name="annual_labour_productivity",
    units="Mdollars_2015/Mhour",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 2, "labour_productivity": 1, "aux_labour_productivity": 1},
)
def annual_labour_productivity():
    return if_then_else(
        time() == integer(time()),
        lambda: labour_productivity(),
        lambda: aux_labour_productivity(),
    )


@component.add(
    name="annual_labour_productivity_variation",
    units="DMNL/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_calibration_labour_productivity": 1,
        "calibrated_labour_productivity_growth": 1,
        "initial_year_labour_productivity_variation_sp": 1,
        "select_labour_productivity_variation_sp": 1,
        "labour_productivity_variation_sp": 1,
        "labour_productivity_variation_default": 2,
        "time": 1,
    },
)
def annual_labour_productivity_variation():
    """
    Labour productivity variation. IF THEN ELSE(SWITCH CALIBRATION LABOUR PRODUCTIVITY=1,calibrated labour productivity growth[REGIONS 35 I,SECTORS I], IF THEN ELSE(Time<INITIAL YEAR LABOUR PRODUCTIVITY VARIATION SP,LABOUR PRODUCTIVITY VARIATION DEFAULT[REGIONS 35 I], IF THEN ELSE(SELECT LABOUR PRODUCTIVITY VARIATION SP=0, LABOUR PRODUCTIVITY VARIATION DEFAULT[REGIONS 35 I], LABOUR PRODUCTIVITY VARIATION SP[REGIONS 35 I,SECTORS I] )) )
    """
    return if_then_else(
        switch_calibration_labour_productivity() == 1,
        lambda: calibrated_labour_productivity_growth(),
        lambda: if_then_else(
            time() < initial_year_labour_productivity_variation_sp(),
            lambda: labour_productivity_variation_default().expand_dims(
                {"SECTORS_I": _subscript_dict["SECTORS_I"]}, 1
            ),
            lambda: if_then_else(
                select_labour_productivity_variation_sp() == 0,
                lambda: labour_productivity_variation_default().expand_dims(
                    {"SECTORS_I": _subscript_dict["SECTORS_I"]}, 1
                ),
                lambda: labour_productivity_variation_sp(),
            ),
        ),
    )


@component.add(
    name="annual_wage_hour_variation",
    units="dollars/Hour",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_exogenous_wage_variation": 1,
        "exogeonus_annual_wage_hour_variation": 1,
        "gamma_wage_hour": 1,
        "constant_wage": 1,
        "non_accelerating_wage_inflation_rate_of_unemployment": 2,
        "delayed_ts_labour_productivity": 2,
        "alpha_wage_hour": 1,
        "delayed_2_consumer_price_index": 1,
        "delayed_consumer_price_index": 2,
        "labour_productivity": 1,
        "unemployment_rate": 2,
        "epsilon_wage_hour": 1,
    },
)
def annual_wage_hour_variation():
    """
    Wage per hour annual growth EXP( CONSTANT WAGE[REGIONS 35 I,SECTORS I] +IF THEN ELSE( unemployment rate[REGIONS 35 I]/NON ACCELERATING WAGE INFLATION RATE OF UNEMPLOYMENT[REGIONS 35 I]<=0, 0 , ALPHA WAGE HOUR[SECTORS I ]*LN(unemployment rate[REGIONS 35 I]/NON ACCELERATING WAGE INFLATION RATE OF UNEMPLOYMENT[REGIONS 35 I])) +IF THEN ELSE( delayed labour productivity[REGIONS 35 I,SECTORS I]<=0, 0, EPSILON WAGE HOUR[SECTORS I]*LN(delayed labour productivity [REGIONS 35 I,SECTORS I])) +IF THEN ELSE( delayed consumer price index[REGIONS 35 I]<=0, 0 , GAMMA WAGE HOUR[SECTORS I]*LN(delayed consumer price index [REGIONS 35 I]/100)) )
    """
    return if_then_else(
        switch_exogenous_wage_variation() == 1,
        lambda: xr.DataArray(
            exogeonus_annual_wage_hour_variation(),
            {
                "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                "SECTORS_I": _subscript_dict["SECTORS_I"],
            },
            ["REGIONS_35_I", "SECTORS_I"],
        ),
        lambda: np.exp(
            constant_wage()
            + if_then_else(
                (
                    unemployment_rate()
                    / non_accelerating_wage_inflation_rate_of_unemployment()
                    <= 0
                ).expand_dims({"SECTORS_I": _subscript_dict["SECTORS_I"]}, 1),
                lambda: xr.DataArray(
                    0,
                    {
                        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                        "SECTORS_I": _subscript_dict["SECTORS_I"],
                    },
                    ["REGIONS_35_I", "SECTORS_I"],
                ),
                lambda: (
                    alpha_wage_hour()
                    * np.log(
                        unemployment_rate()
                        / non_accelerating_wage_inflation_rate_of_unemployment()
                    )
                ).transpose("REGIONS_35_I", "SECTORS_I"),
            )
            + if_then_else(
                delayed_ts_labour_productivity() <= 0,
                lambda: xr.DataArray(
                    0,
                    {
                        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                        "SECTORS_I": _subscript_dict["SECTORS_I"],
                    },
                    ["REGIONS_35_I", "SECTORS_I"],
                ),
                lambda: (
                    epsilon_wage_hour()
                    * np.log(
                        zidz(labour_productivity(), delayed_ts_labour_productivity())
                    ).transpose("SECTORS_I", "REGIONS_35_I")
                ).transpose("REGIONS_35_I", "SECTORS_I"),
            )
            + if_then_else(
                (delayed_consumer_price_index() <= 0).expand_dims(
                    {"SECTORS_I": _subscript_dict["SECTORS_I"]}, 1
                ),
                lambda: xr.DataArray(
                    0,
                    {
                        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                        "SECTORS_I": _subscript_dict["SECTORS_I"],
                    },
                    ["REGIONS_35_I", "SECTORS_I"],
                ),
                lambda: (
                    gamma_wage_hour()
                    * np.log(
                        delayed_consumer_price_index()
                        / delayed_2_consumer_price_index()
                    )
                ).transpose("REGIONS_35_I", "SECTORS_I"),
            )
        ),
    )


@component.add(
    name="aux_growth_labour_productivity",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_aux_growth_labour_productivity": 1},
    other_deps={
        "_delayfixed_aux_growth_labour_productivity": {
            "initial": {"time_step": 1},
            "step": {"annual_growth_labour_productivity": 1},
        }
    },
)
def aux_growth_labour_productivity():
    return _delayfixed_aux_growth_labour_productivity()


_delayfixed_aux_growth_labour_productivity = DelayFixed(
    lambda: annual_growth_labour_productivity(),
    lambda: time_step(),
    lambda: xr.DataArray(
        0,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "SECTORS_I": _subscript_dict["SECTORS_I"],
        },
        ["REGIONS_35_I", "SECTORS_I"],
    ),
    time_step,
    "_delayfixed_aux_growth_labour_productivity",
)


@component.add(
    name="aux_labour_productivity",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_aux_labour_productivity": 1},
    other_deps={
        "_delayfixed_aux_labour_productivity": {
            "initial": {"time_step": 1},
            "step": {"annual_labour_productivity": 1},
        }
    },
)
def aux_labour_productivity():
    return _delayfixed_aux_labour_productivity()


_delayfixed_aux_labour_productivity = DelayFixed(
    lambda: annual_labour_productivity(),
    lambda: time_step(),
    lambda: xr.DataArray(
        0,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "SECTORS_I": _subscript_dict["SECTORS_I"],
        },
        ["REGIONS_35_I", "SECTORS_I"],
    ),
    time_step,
    "_delayfixed_aux_labour_productivity",
)


@component.add(
    name="BASE_WORKING_AGE_POPULATION",
    units="kpeople",
    subscripts=["REGIONS_35_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_base_working_age_population"},
)
def base_working_age_population():
    """
    Working age population: persons aged 15 years and older.
    """
    return _ext_constant_base_working_age_population()


_ext_constant_base_working_age_population = ExtConstant(
    "model_parameters/economy/Primary_Inputs_BASE.xlsx",
    "BASE_Working_age_pop",
    "A5",
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    _root,
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    "_ext_constant_base_working_age_population",
)


@component.add(
    name="calibrated_labour_productivity_growth",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "labour_productivity_variation_historic": 1,
        "delayed_ts_labour_productivity": 1,
        "desired_labour_productivity": 1,
    },
)
def calibrated_labour_productivity_growth():
    """
    IF THEN ELSE(Time<=2015,LABOUR PRODUCTIVITY VARIATION HISTORIC[REGIONS 35 I,SECTORS I],ZIDZ(desired labour productivity [REGIONS 35 I,SECTORS I],delayed labour productivity[REGIONS 35 I ,SECTORS I])-1)
    """
    return if_then_else(
        time() <= 2015,
        lambda: labour_productivity_variation_historic(),
        lambda: zidz(desired_labour_productivity(), delayed_ts_labour_productivity())
        - 1,
    )


@component.add(
    name="climate_change_impact_in_labour_productivity",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_activation_labour_productivity_adaptation": 1,
        "unemployment_rate": 1,
        "heat_stress_incremental_damage_function": 1,
        "switch_climate_change_damage": 1,
        "labour_productivity": 1,
        "switch_eco_climate_change_damage_labour_productivity": 1,
        "vector_borne_diseases_incremental_damage_function": 1,
    },
)
def climate_change_impact_in_labour_productivity():
    """
    Climate change impact in labour productuvuty
    """
    return if_then_else(
        np.logical_and(
            switch_activation_labour_productivity_adaptation() == 1,
            unemployment_rate() < 0.035,
        ).expand_dims({"SECTORS_I": _subscript_dict["SECTORS_I"]}, 1),
        lambda: xr.DataArray(
            0,
            {
                "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                "SECTORS_I": _subscript_dict["SECTORS_I"],
            },
            ["REGIONS_35_I", "SECTORS_I"],
        ),
        lambda: if_then_else(
            np.logical_or(
                switch_climate_change_damage() == 0,
                switch_eco_climate_change_damage_labour_productivity() == 0,
            ),
            lambda: xr.DataArray(
                0,
                {
                    "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                    "SECTORS_I": _subscript_dict["SECTORS_I"],
                },
                ["REGIONS_35_I", "SECTORS_I"],
            ),
            lambda: labour_productivity()
            * (
                heat_stress_incremental_damage_function()
                + vector_borne_diseases_incremental_damage_function()
            ),
        ),
    )


@component.add(
    name="delayed_2_consumer_price_index",
    units="DMNL",
    subscripts=["REGIONS_35_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_2_consumer_price_index": 1},
    other_deps={
        "_delayfixed_delayed_2_consumer_price_index": {
            "initial": {"initial_delayed_2_consumer_price_index": 1},
            "step": {
                "time": 1,
                "initial_delayed_2_consumer_price_index": 1,
                "consumer_price_index": 1,
            },
        }
    },
)
def delayed_2_consumer_price_index():
    """
    Delayed Consumer price index.
    """
    return _delayfixed_delayed_2_consumer_price_index()


_delayfixed_delayed_2_consumer_price_index = DelayFixed(
    lambda: if_then_else(
        time() <= 2015,
        lambda: initial_delayed_2_consumer_price_index(),
        lambda: consumer_price_index(),
    ),
    lambda: 2,
    lambda: initial_delayed_2_consumer_price_index(),
    time_step,
    "_delayfixed_delayed_2_consumer_price_index",
)


@component.add(
    name="delayed_consumer_price_index",
    units="DMNL",
    subscripts=["REGIONS_35_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_consumer_price_index": 1},
    other_deps={
        "_delayfixed_delayed_consumer_price_index": {
            "initial": {"initial_delayed_consumer_price_index": 1},
            "step": {
                "time": 1,
                "initial_delayed_consumer_price_index": 1,
                "consumer_price_index": 1,
            },
        }
    },
)
def delayed_consumer_price_index():
    """
    Delayed Consumer price index.
    """
    return _delayfixed_delayed_consumer_price_index()


_delayfixed_delayed_consumer_price_index = DelayFixed(
    lambda: if_then_else(
        time() <= 2015,
        lambda: initial_delayed_consumer_price_index(),
        lambda: consumer_price_index(),
    ),
    lambda: 1,
    lambda: initial_delayed_consumer_price_index(),
    time_step,
    "_delayfixed_delayed_consumer_price_index",
)


@component.add(
    name="delayed_TS_desired_unemployment_rate",
    subscripts=["REGIONS_35_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_desired_unemployment_rate": 1},
    other_deps={
        "_delayfixed_delayed_ts_desired_unemployment_rate": {
            "initial": {"initial_delayed_unemployment_rate": 1, "time_step": 1},
            "step": {"desired_unemployment_rate": 1},
        }
    },
)
def delayed_ts_desired_unemployment_rate():
    """
    IF THEN ELSE(Time<=2015, INITIAL DELAYED UNEMPLOYMENT RATE[REGIONS 35 I] ,desired unemployment rate[REGIONS 35 I]), TIME STEP, INITIAL DELAYED UNEMPLOYMENT RATE[REGIONS 35 I]
    """
    return _delayfixed_delayed_ts_desired_unemployment_rate()


_delayfixed_delayed_ts_desired_unemployment_rate = DelayFixed(
    lambda: desired_unemployment_rate(),
    lambda: time_step(),
    lambda: initial_delayed_unemployment_rate(),
    time_step,
    "_delayfixed_delayed_ts_desired_unemployment_rate",
)


@component.add(
    name="delayed_TS_hours_per_worker",
    units="Mhours/(kpeople*Year)",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_hours_per_worker": 1},
    other_deps={
        "_delayfixed_delayed_ts_hours_per_worker": {
            "initial": {"hours_per_worker": 1, "time_step": 1},
            "step": {"hours_per_worker": 1},
        }
    },
)
def delayed_ts_hours_per_worker():
    return _delayfixed_delayed_ts_hours_per_worker()


_delayfixed_delayed_ts_hours_per_worker = DelayFixed(
    lambda: hours_per_worker(),
    lambda: time_step(),
    lambda: hours_per_worker(),
    time_step,
    "_delayfixed_delayed_ts_hours_per_worker",
)


@component.add(
    name="delayed_TS_hours_worked",
    units="Mhours/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_hours_worked": 1},
    other_deps={
        "_delayfixed_delayed_ts_hours_worked": {
            "initial": {"initial_delayed_hours_worked": 1, "time_step": 1},
            "step": {"time": 1, "initial_delayed_hours_worked": 1, "hours_worked": 1},
        }
    },
)
def delayed_ts_hours_worked():
    """
    Delayed hours worked.
    """
    return _delayfixed_delayed_ts_hours_worked()


_delayfixed_delayed_ts_hours_worked = DelayFixed(
    lambda: if_then_else(
        time() <= 2015, lambda: initial_delayed_hours_worked(), lambda: hours_worked()
    ),
    lambda: time_step(),
    lambda: initial_delayed_hours_worked(),
    time_step,
    "_delayfixed_delayed_ts_hours_worked",
)


@component.add(
    name="delayed_TS_labour_compensation_total",
    subscripts=["REGIONS_35_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_labour_compensation_total": 1},
    other_deps={
        "_delayfixed_delayed_ts_labour_compensation_total": {
            "initial": {"base_labour_compensation": 1, "time_step": 1},
            "step": {
                "time": 1,
                "base_labour_compensation": 1,
                "labour_compensation_total": 1,
            },
        }
    },
)
def delayed_ts_labour_compensation_total():
    """
    Delayed labour compensation total
    """
    return _delayfixed_delayed_ts_labour_compensation_total()


_delayfixed_delayed_ts_labour_compensation_total = DelayFixed(
    lambda: if_then_else(
        time() <= 2015,
        lambda: sum(
            base_labour_compensation().rename({"SECTORS_I": "SECTORS_I!"}),
            dim=["SECTORS_I!"],
        ),
        lambda: labour_compensation_total(),
    ),
    lambda: time_step(),
    lambda: sum(
        base_labour_compensation().rename({"SECTORS_I": "SECTORS_I!"}),
        dim=["SECTORS_I!"],
    ),
    time_step,
    "_delayfixed_delayed_ts_labour_compensation_total",
)


@component.add(
    name="delayed_TS_labour_productivity",
    units="Mdollars_2015/Mhour",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_labour_productivity": 1},
    other_deps={
        "_delayfixed_delayed_ts_labour_productivity": {
            "initial": {"initial_delayed_labour_productivity": 1, "time_step": 1},
            "step": {
                "time": 1,
                "initial_delayed_labour_productivity": 1,
                "labour_productivity": 1,
            },
        }
    },
)
def delayed_ts_labour_productivity():
    """
    Delayed labour productivity.
    """
    return _delayfixed_delayed_ts_labour_productivity()


_delayfixed_delayed_ts_labour_productivity = DelayFixed(
    lambda: if_then_else(
        time() <= 2015,
        lambda: initial_delayed_labour_productivity(),
        lambda: labour_productivity(),
    ),
    lambda: time_step(),
    lambda: initial_delayed_labour_productivity(),
    time_step,
    "_delayfixed_delayed_ts_labour_productivity",
)


@component.add(
    name="delayed_TS_unemployment_rate",
    units="DMNL",
    subscripts=["REGIONS_35_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_unemployment_rate": 1},
    other_deps={
        "_delayfixed_delayed_ts_unemployment_rate": {
            "initial": {"initial_delayed_unemployment_rate": 1, "time_step": 1},
            "step": {
                "time": 1,
                "initial_delayed_unemployment_rate": 1,
                "unemployment_rate": 1,
            },
        }
    },
)
def delayed_ts_unemployment_rate():
    """
    Delayed unemployment rate.
    """
    return _delayfixed_delayed_ts_unemployment_rate()


_delayfixed_delayed_ts_unemployment_rate = DelayFixed(
    lambda: if_then_else(
        time() <= 2015,
        lambda: initial_delayed_unemployment_rate(),
        lambda: unemployment_rate(),
    ),
    lambda: time_step(),
    lambda: initial_delayed_unemployment_rate(),
    time_step,
    "_delayfixed_delayed_ts_unemployment_rate",
)


@component.add(
    name="delayed_TS_wage_hour",
    units="dollars/Hour",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_wage_hour": 1},
    other_deps={
        "_delayfixed_delayed_ts_wage_hour": {
            "initial": {"initial_delayed_wage_hour": 1, "time_step": 1},
            "step": {"time": 1, "initial_delayed_wage_hour": 1, "wage_hour": 1},
        }
    },
)
def delayed_ts_wage_hour():
    """
    Delayed wage per hour.
    """
    return _delayfixed_delayed_ts_wage_hour()


_delayfixed_delayed_ts_wage_hour = DelayFixed(
    lambda: if_then_else(
        time() <= 2016, lambda: initial_delayed_wage_hour(), lambda: wage_hour()
    ),
    lambda: time_step(),
    lambda: initial_delayed_wage_hour(),
    time_step,
    "_delayfixed_delayed_ts_wage_hour",
)


@component.add(
    name="delayed_TS_wage_hour_total",
    units="dollars/Hour",
    subscripts=["REGIONS_35_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_wage_hour_total": 1},
    other_deps={
        "_delayfixed_delayed_ts_wage_hour_total": {
            "initial": {"initial_delayed_wage_hour_total": 1, "time_step": 1},
            "step": {
                "time": 1,
                "initial_delayed_wage_hour_total": 1,
                "wage_hour_total": 1,
            },
        }
    },
)
def delayed_ts_wage_hour_total():
    """
    Delayed weighted average wage per hour.
    """
    return _delayfixed_delayed_ts_wage_hour_total()


_delayfixed_delayed_ts_wage_hour_total = DelayFixed(
    lambda: if_then_else(
        time() <= 2015,
        lambda: initial_delayed_wage_hour_total(),
        lambda: wage_hour_total(),
    ),
    lambda: time_step(),
    lambda: initial_delayed_wage_hour_total(),
    time_step,
    "_delayfixed_delayed_ts_wage_hour_total",
)


@component.add(
    name="delayed_TS_working_age_population",
    units="kpeople",
    subscripts=["REGIONS_35_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_working_age_population": 1},
    other_deps={
        "_delayfixed_delayed_ts_working_age_population": {
            "initial": {"time_step": 1},
            "step": {"working_age_population": 1},
        }
    },
)
def delayed_ts_working_age_population():
    return _delayfixed_delayed_ts_working_age_population()


_delayfixed_delayed_ts_working_age_population = DelayFixed(
    lambda: working_age_population(),
    lambda: time_step(),
    lambda: xr.DataArray(
        0, {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]}, ["REGIONS_35_I"]
    ),
    time_step,
    "_delayfixed_delayed_ts_working_age_population",
)


@component.add(
    name="desired_labour_productivity",
    units="Mdollars_2015/Mhour",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"delayed_ts_labour_productivity": 1, "employment_gap": 1},
)
def desired_labour_productivity():
    """
    delayed labour productivity[REGIONS 35 I,SECTORS I]*employment gap[REGIONS 35 I]
    """
    return delayed_ts_labour_productivity() * employment_gap()


@component.add(
    name="desired_unemployment_rate",
    units="DMNL",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "initial_delayed_unemployment_rate": 1,
        "time_step": 1,
        "delayed_ts_desired_unemployment_rate": 1,
        "desired_unemployment_rate_growth": 1,
    },
)
def desired_unemployment_rate():
    return if_then_else(
        time() <= 2015,
        lambda: initial_delayed_unemployment_rate(),
        lambda: delayed_ts_desired_unemployment_rate()
        * (1 + desired_unemployment_rate_growth() * time_step()),
    )


@component.add(
    name="desired_unemployment_rate_growth",
    units="DMNL/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "long_term_unemployment_rate": 1,
        "initial_delayed_unemployment_rate": 1,
    },
)
def desired_unemployment_rate_growth():
    return (
        zidz(long_term_unemployment_rate(), initial_delayed_unemployment_rate())
        ** (1 / 35)
        - 1
    )


@component.add(
    name="employment_by_sector",
    units="kpeople",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"hours_worked": 1, "hours_per_worker": 1},
)
def employment_by_sector():
    """
    Employment.
    """
    return zidz(hours_worked(), hours_per_worker())


@component.add(
    name="employment_desired",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"desired_unemployment_rate": 1, "labour_force": 1},
)
def employment_desired():
    return (1 - desired_unemployment_rate()) * labour_force()


@component.add(
    name="employment_gap",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"employment_total": 1, "employment_desired": 1},
)
def employment_gap():
    return zidz(employment_total(), employment_desired())


@component.add(
    name="employment_total",
    units="kpeople",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"employment_by_sector": 1},
)
def employment_total():
    """
    Total employment.
    """
    return sum(
        employment_by_sector().rename({"SECTORS_I": "SECTORS_I!"}), dim=["SECTORS_I!"]
    )


@component.add(
    name="EXOGEONUS_ANNUAL_WAGE_HOUR_VARIATION",
    units="DMNL/Year",
    comp_type="Constant",
    comp_subtype="Normal",
)
def exogeonus_annual_wage_hour_variation():
    """
    Exogenous wage variation
    """
    return 0.04


@component.add(
    name="hours_per_worker",
    units="Mhours/(kpeople*Year)",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "maximum_hours_per_worker": 1,
        "hours_per_worker_historic": 2,
        "working_time_variation_sp": 1,
        "initial_year_working_time_variation_sp": 2,
        "model_explorer_working_time_variation": 1,
        "switch_model_explorer": 1,
        "time": 2,
    },
)
def hours_per_worker():
    """
    Hours per worker.
    """
    return np.maximum(
        0,
        np.minimum(
            maximum_hours_per_worker(),
            if_then_else(
                time() < initial_year_working_time_variation_sp(),
                lambda: hours_per_worker_historic(),
                lambda: if_then_else(
                    switch_model_explorer() == 1,
                    lambda: model_explorer_working_time_variation(),
                    lambda: hours_per_worker_historic()
                    * (1 + working_time_variation_sp())
                    ** (time() - initial_year_working_time_variation_sp()),
                ),
            ),
        ),
    )


@component.add(
    name="hours_per_worker_variation_rate",
    units="DMNL/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"hours_per_worker": 1, "delayed_ts_hours_per_worker": 2},
)
def hours_per_worker_variation_rate():
    return zidz(
        hours_per_worker() - delayed_ts_hours_per_worker(),
        delayed_ts_hours_per_worker(),
    )


@component.add(
    name="hours_worked",
    units="Mhours/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_labour": 1,
        "base_output_real": 1,
        "labour_productivity": 2,
        "output_real": 1,
    },
)
def hours_worked():
    """
    Hours worked.
    """
    return if_then_else(
        switch_eco_labour() == 0,
        lambda: zidz(base_output_real(), labour_productivity()),
        lambda: zidz(output_real(), labour_productivity()),
    )


@component.add(
    name="INITIAL_DELAYED_2_CONSUMER_PRICE_INDEX",
    subscripts=["REGIONS_35_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_delayed_2_consumer_price_index"},
)
def initial_delayed_2_consumer_price_index():
    """
    Delayed consumer price index, 2 periods
    """
    return _ext_constant_initial_delayed_2_consumer_price_index()


_ext_constant_initial_delayed_2_consumer_price_index = ExtConstant(
    "model_parameters/economy/Primary_Inputs_LAGGED_t1.xlsx",
    "Consumer_Price_Index_t2",
    "INITIAL_DELAYED_2_CONSUMER_PRICE_INDEX",
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    _root,
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    "_ext_constant_initial_delayed_2_consumer_price_index",
)


@component.add(
    name="INITIAL_YEAR_LABOUR_PRODUCTIVITY_VARIATION_SP",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_initial_year_labour_productivity_variation_sp"
    },
)
def initial_year_labour_productivity_variation_sp():
    return _ext_constant_initial_year_labour_productivity_variation_sp()


_ext_constant_initial_year_labour_productivity_variation_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "INITIAL_YEAR_LABOUR_PRODUCTIVITY_VARIATION_SP",
    {},
    _root,
    {},
    "_ext_constant_initial_year_labour_productivity_variation_sp",
)


@component.add(
    name="INITIAL_YEAR_WORKING_TIME_VARIATION_SP",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_year_working_time_variation_sp"},
)
def initial_year_working_time_variation_sp():
    return _ext_constant_initial_year_working_time_variation_sp()


_ext_constant_initial_year_working_time_variation_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "INITIAL_YEAR_WORKING_TIME_VARIATION_SP",
    {},
    _root,
    {},
    "_ext_constant_initial_year_working_time_variation_sp",
)


@component.add(
    name="labour_compensation",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"hours_worked": 1, "wage_hour": 1},
)
def labour_compensation():
    """
    Labour compensation in nominal terms.
    """
    return hours_worked() * wage_hour()


@component.add(
    name="labour_compensation_real",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"base_wage_hour": 1, "hours_worked": 1},
)
def labour_compensation_real():
    """
    Labour compensation in real terms.
    """
    return base_wage_hour() * hours_worked()


@component.add(
    name="labour_compensation_total",
    units="Mdollars",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"labour_compensation": 1},
)
def labour_compensation_total():
    """
    Total labour compensation
    """
    return sum(
        labour_compensation().rename({"SECTORS_I": "SECTORS_I!"}), dim=["SECTORS_I!"]
    )


@component.add(
    name="labour_force",
    units="kpeople",
    subscripts=["REGIONS_35_I"],
    comp_type="Stateful",
    comp_subtype="Smooth",
    depends_on={
        "time": 1,
        "switch_eco_participation_rate": 1,
        "initial_participation_rate": 1,
        "working_age_population": 1,
        "_smooth_labour_force": 1,
    },
    other_deps={
        "_smooth_labour_force": {
            "initial": {"participation_rate": 1, "working_age_population": 1},
            "step": {"participation_rate": 1, "working_age_population": 1},
        }
    },
)
def labour_force():
    """
    Labour force.
    """
    return if_then_else(
        np.logical_or(time() <= 2015, switch_eco_participation_rate() == 0),
        lambda: initial_participation_rate() * working_age_population(),
        lambda: _smooth_labour_force(),
    )


_smooth_labour_force = Smooth(
    lambda: participation_rate() * working_age_population(),
    lambda: xr.DataArray(
        8, {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]}, ["REGIONS_35_I"]
    ),
    lambda: participation_rate() * working_age_population(),
    lambda: 1,
    "_smooth_labour_force",
)


@component.add(
    name="labour_force_millions",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"labour_force": 1},
)
def labour_force_millions():
    return labour_force() / 1000000.0


@component.add(
    name="labour_force_variation_rate",
    units="DMNL/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"labour_force": 1, "labour_ts_force_delayed": 2},
)
def labour_force_variation_rate():
    return zidz(labour_force() - labour_ts_force_delayed(), labour_ts_force_delayed())


@component.add(
    name="labour_productivity",
    units="Mdollars_2015/Mhour",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_labour_productivity": 1},
    other_deps={
        "_integ_labour_productivity": {
            "initial": {"base_labour_productivity": 1},
            "step": {
                "labour_productivity_variation": 1,
                "climate_change_impact_in_labour_productivity": 1,
            },
        }
    },
)
def labour_productivity():
    """
    Labour productivity
    """
    return _integ_labour_productivity()


_integ_labour_productivity = Integ(
    lambda: labour_productivity_variation()
    - climate_change_impact_in_labour_productivity(),
    lambda: base_labour_productivity(),
    "_integ_labour_productivity",
)


@component.add(
    name="labour_productivity_variation",
    units="Mdollars_2015/(Mhour*Year)",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "switch_activation_labour_productivity_adaptation": 1,
        "labour_productivity_variation_adaptation": 1,
        "annual_labour_productivity": 2,
        "round_annual_growth_labour_productivity": 2,
        "unemployment_rate": 1,
    },
)
def labour_productivity_variation():
    """
    Vartion labour productivity IF_THEN_ELSE(Time<=2015, 0, IF_THEN_ELSE(unemployment_rate[REGIONS_35_I]>0.035 :OR: SWITCH_ACTIVATION_LABOUR_PRODUCTIVITY_ADAPTATION=0, annual_growth_labour_productivity[REGIONS_35_I,SECTORS_I]*labour_productivity[REGIONS _35_I,SECTORS_I], (MAX(0,annual_growth_labour_productivity[REGIONS_35_I,SECTORS_I])+labour_productivity _variation_adaptation[REGIONS_35_I ,SECTORS_I])*labour_productivity[REGIONS_35_I,SECTORS_I]))
    """
    return if_then_else(
        time() <= 2015,
        lambda: xr.DataArray(
            0,
            {
                "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                "SECTORS_I": _subscript_dict["SECTORS_I"],
            },
            ["REGIONS_35_I", "SECTORS_I"],
        ),
        lambda: if_then_else(
            np.logical_or(
                unemployment_rate() > 0.035,
                switch_activation_labour_productivity_adaptation() == 0,
            ).expand_dims({"SECTORS_I": _subscript_dict["SECTORS_I"]}, 1),
            lambda: round_annual_growth_labour_productivity()
            * annual_labour_productivity(),
            lambda: (
                np.maximum(0, round_annual_growth_labour_productivity())
                + labour_productivity_variation_adaptation()
            )
            * annual_labour_productivity(),
        ),
    )


@component.add(
    name="labour_productivity_variation_adaptation",
    units="DMNL/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"sum_variation_rates": 1},
)
def labour_productivity_variation_adaptation():
    return np.maximum(0, sum_variation_rates())


@component.add(
    name="LABOUR_PRODUCTIVITY_VARIATION_DEFAULT",
    units="DMNL/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_labour_productivity_variation_default",
        "__data__": "_ext_data_labour_productivity_variation_default",
        "time": 1,
    },
)
def labour_productivity_variation_default():
    """
    Default scenario for labour productivity growth
    """
    return _ext_data_labour_productivity_variation_default(time())


_ext_data_labour_productivity_variation_default = ExtData(
    "model_parameters/economy/Primary_Inputs_EXO_1.xlsx",
    "EXO_Lab_productivity_growth_def",
    "TIME_LAB_PROD",
    "LABOUR_PRODUCTIVITY_VARIATION_DEFAULT",
    None,
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    _root,
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    "_ext_data_labour_productivity_variation_default",
)


@component.add(
    name="LABOUR_PRODUCTIVITY_VARIATION_SP",
    units="1/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_labour_productivity_variation_sp"},
)
def labour_productivity_variation_sp():
    return _ext_constant_labour_productivity_variation_sp()


_ext_constant_labour_productivity_variation_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "LABOUR_PRODUCTIVITY_VARIATION_SP",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
    "_ext_constant_labour_productivity_variation_sp",
)


@component.add(
    name="labour_TS_force_delayed",
    units="kpeople",
    subscripts=["REGIONS_35_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_labour_ts_force_delayed": 1},
    other_deps={
        "_delayfixed_labour_ts_force_delayed": {
            "initial": {"labour_force": 1, "time_step": 1},
            "step": {"labour_force": 1},
        }
    },
)
def labour_ts_force_delayed():
    return _delayfixed_labour_ts_force_delayed()


_delayfixed_labour_ts_force_delayed = DelayFixed(
    lambda: labour_force(),
    lambda: time_step(),
    lambda: labour_force(),
    time_step,
    "_delayfixed_labour_ts_force_delayed",
)


@component.add(
    name="LONG_TERM_UNEMPLOYMENT_RATE",
    units="DMNL",
    subscripts=["REGIONS_35_I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def long_term_unemployment_rate():
    return xr.DataArray(
        0.065, {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]}, ["REGIONS_35_I"]
    )


@component.add(
    name="MAXIMUM_HOURS_PER_WORKER",
    units="Mhours/kpeople",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"unit_conversion_hours_year": 1},
)
def maximum_hours_per_worker():
    """
    Setting the maximum working time at 24-8=16 hours/day.
    """
    return (24 - 8 / 24) * unit_conversion_hours_year() / 1000


@component.add(
    name="output_real_1000",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"output_real": 1},
)
def output_real_1000():
    return output_real() / 1000


@component.add(
    name="participation_rate",
    units="DMNL",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "constant_participation_rate": 1,
        "beta_participation_rate": 1,
        "delayed_ts_unemployment_rate": 1,
        "delayed_ts_consumer_price_index": 1,
        "epsilon_participation_rate": 1,
        "delayed_ts_wage_hour_total": 1,
        "price_transformation": 1,
    },
)
def participation_rate():
    """
    Particpation rate: share of active population in the labour market (i.e., labour force divided by working-age population)
    """
    return np.exp(
        constant_participation_rate()
        + beta_participation_rate() * np.log(1 - delayed_ts_unemployment_rate())
        + epsilon_participation_rate()
        * np.log(
            zidz(
                delayed_ts_wage_hour_total(),
                delayed_ts_consumer_price_index() / price_transformation(),
            )
        )
    )


@component.add(
    name="round_annual_growth_labour_productivity",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"annual_growth_labour_productivity": 1},
)
def round_annual_growth_labour_productivity():
    return integer(annual_growth_labour_productivity() * 1000) / 1000


@component.add(
    name="SELECT_LABOUR_PRODUCTIVITY_VARIATION_SP",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_select_labour_productivity_variation_sp"
    },
)
def select_labour_productivity_variation_sp():
    """
    0= LABOUR_PRODUCTIVITY_VARIATION_DEFAULT 1= LABOUR_PRODUCTIVITY_VARIATION_SP[
    """
    return _ext_constant_select_labour_productivity_variation_sp()


_ext_constant_select_labour_productivity_variation_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "SELECT_LABOUR_PRODUCTIVITY_VARIATION_SP",
    {},
    _root,
    {},
    "_ext_constant_select_labour_productivity_variation_sp",
)


@component.add(
    name="sum_variation_rates",
    units="DMNL/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "output_real_growth": 1,
        "hours_per_worker_variation_rate": 1,
        "labour_force_variation_rate": 1,
    },
)
def sum_variation_rates():
    return (
        output_real_growth()
        - hours_per_worker_variation_rate()
        - labour_force_variation_rate()
    )


@component.add(
    name="SWITCH_ACTIVATION_LABOUR_PRODUCTIVITY_ADAPTATION",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_switch_activation_labour_productivity_adaptation"
    },
)
def switch_activation_labour_productivity_adaptation():
    return _ext_constant_switch_activation_labour_productivity_adaptation()


_ext_constant_switch_activation_labour_productivity_adaptation = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_ACTIVATION_LABOUR_PRODUCTIVITY_ADAPTATION",
    {},
    _root,
    {},
    "_ext_constant_switch_activation_labour_productivity_adaptation",
)


@component.add(
    name="SWITCH_CALIBRATION_LABOUR_PRODUCTIVITY",
    comp_type="Constant",
    comp_subtype="Normal",
)
def switch_calibration_labour_productivity():
    """
    Switch on to calibrate the growth path ofo the labour porductivirty to be consitent with the long-term non-accelerating wage inflation rate of unemployment (structural unemployment rate): unemployment rate that doest not change wages 0: Calibration off 1: calibration on
    """
    return 0


@component.add(
    name="SWITCH_DEM2ECO_WORKING_AGE_POPULATION",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_dem2eco_working_age_population"},
)
def switch_dem2eco_working_age_population():
    """
    Intermodule links SWITCH, it can take two values: 0: the link is broken, the intermodule variable is replaced by an exogenous parameter. 1: the link between modules is operational.
    """
    return _ext_constant_switch_dem2eco_working_age_population()


_ext_constant_switch_dem2eco_working_age_population = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_DEM2ECO_WORKING_AGE_POPULATION",
    {},
    _root,
    {},
    "_ext_constant_switch_dem2eco_working_age_population",
)


@component.add(
    name="SWITCH_ECO_LABOUR",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_eco_labour"},
)
def switch_eco_labour():
    """
    This switch can take two values: 0: the (sub)module runs isolated from the rest of WILIAM, replacing inter(sub)module variables with exogenous parameters. 1: the (sub)module runs integrated with the rest of WILIAM.
    """
    return _ext_constant_switch_eco_labour()


_ext_constant_switch_eco_labour = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_ECO_LABOUR",
    {},
    _root,
    {},
    "_ext_constant_switch_eco_labour",
)


@component.add(
    name="SWITCH_ECO_PARTICIPATION_RATE",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_eco_participation_rate"},
)
def switch_eco_participation_rate():
    """
    1: dynamic endogenous participation rate 0: exogenous participation rate
    """
    return _ext_constant_switch_eco_participation_rate()


_ext_constant_switch_eco_participation_rate = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_ECO_PARTICIPATION_RATE",
    {},
    _root,
    {},
    "_ext_constant_switch_eco_participation_rate",
)


@component.add(
    name="SWITCH_ECONOMY",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_economy"},
)
def switch_economy():
    """
    This switch can take two values: 0: the module runs isolated from the rest of WILIAM, replacing inter(sub)module variables with exogenous parameters. 1: the module runs integrated with the rest of WILIAM.
    """
    return _ext_constant_switch_economy()


_ext_constant_switch_economy = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_ECONOMY",
    {},
    _root,
    {},
    "_ext_constant_switch_economy",
)


@component.add(
    name="SWITCH_EXOGENOUS_WAGE_VARIATION",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_exogenous_wage_variation"},
)
def switch_exogenous_wage_variation():
    """
    SWITCH to activate an exogeous wage variation 1: ON 0: OFF
    """
    return _ext_constant_switch_exogenous_wage_variation()


_ext_constant_switch_exogenous_wage_variation = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_EXOGENOUS_WAGE_VARIATION",
    {},
    _root,
    {},
    "_ext_constant_switch_exogenous_wage_variation",
)


@component.add(
    name="total_population_over_15_millions",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_population_over_15": 1},
)
def total_population_over_15_millions():
    return total_population_over_15() / 1000000.0


@component.add(
    name="unemployment_rate",
    units="DMNL",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"employment_total": 1, "labour_force": 1},
)
def unemployment_rate():
    """
    Unemployment rate.
    """
    return np.maximum(1 - zidz(employment_total(), labour_force()), 0)


@component.add(
    name="wage_hour",
    units="dollars/Hour",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"wage_hour_stock": 1},
)
def wage_hour():
    """
    Wage per hour corrected for downward rigidity IF_THEN_ELSE(wage_hour_stock[REGIONS_35_I,SECTORS_I]>delayed_wage_hour[REGIONS_35_I,S ECTORS_I],wage_hour_stock[REGIONS_35_I ,SECTORS_I],delayed_wage_hour[REGIONS_35_I,SECTORS_I])
    """
    return wage_hour_stock()


@component.add(
    name="wage_hour_stock",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_wage_hour_stock": 1},
    other_deps={
        "_integ_wage_hour_stock": {
            "initial": {"base_wage_hour": 1},
            "step": {"time": 1, "wage_hour_variation": 1},
        }
    },
)
def wage_hour_stock():
    return _integ_wage_hour_stock()


_integ_wage_hour_stock = Integ(
    lambda: if_then_else(
        time() <= 2015,
        lambda: xr.DataArray(
            0,
            {
                "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                "SECTORS_I": _subscript_dict["SECTORS_I"],
            },
            ["REGIONS_35_I", "SECTORS_I"],
        ),
        lambda: wage_hour_variation(),
    ),
    lambda: base_wage_hour(),
    "_integ_wage_hour_stock",
)


@component.add(
    name="wage_hour_total",
    units="dollars/Hour",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"labour_compensation": 1, "hours_worked": 1},
)
def wage_hour_total():
    """
    Weighted averaga wage per hour
    """
    return zidz(
        sum(
            labour_compensation().rename({"SECTORS_I": "SECTORS_I!"}),
            dim=["SECTORS_I!"],
        ),
        sum(hours_worked().rename({"SECTORS_I": "SECTORS_I!"}), dim=["SECTORS_I!"]),
    )


@component.add(
    name="wage_hour_variation",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"wage_hour_stock": 1, "annual_wage_hour_variation": 1},
)
def wage_hour_variation():
    return wage_hour_stock() * annual_wage_hour_variation()


@component.add(
    name="working_age_population",
    units="kpeople",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "switch_economy": 1,
        "switch_eco_labour": 1,
        "switch_dem2eco_working_age_population": 1,
        "base_working_age_population": 1,
        "total_population_over_15": 1,
        "unit_conversion_kpeople_people": 1,
    },
)
def working_age_population():
    """
    Working age population defined as 15 years old and older.
    """
    return if_then_else(
        np.logical_or(
            time() <= 2015,
            np.logical_or(
                switch_economy() == 0,
                np.logical_or(
                    switch_eco_labour() == 0,
                    switch_dem2eco_working_age_population() == 0,
                ),
            ),
        ),
        lambda: base_working_age_population(),
        lambda: total_population_over_15() * unit_conversion_kpeople_people(),
    )


@component.add(
    name="WORKING_TIME_VARIATION_SP",
    units="1/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_working_time_variation_sp"},
)
def working_time_variation_sp():
    return _ext_constant_working_time_variation_sp()


_ext_constant_working_time_variation_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "WORKING_TIME_VARIATION_SP",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
    "_ext_constant_working_time_variation_sp",
)
