"""
Module demography.exogenous_inputs
Translated using PySD version 3.10.0
"""


@component.add(
    name="A_EXPONENTIAL_LEAB_TO_MR",
    units="DMNL",
    subscripts=["SEX_I", "AGE_COHORTS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_a_exponential_leab_to_mr"},
)
def a_exponential_leab_to_mr():
    """
    Parameter A of the equation that related the life expectancy at birth and the mortality rates (MR = A * exp(B * LEAB)
    """
    return _ext_constant_a_exponential_leab_to_mr()


_ext_constant_a_exponential_leab_to_mr = ExtConstant(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "A_EXPONENTIAL_LEAB_TO_MR*",
    {
        "SEX_I": _subscript_dict["SEX_I"],
        "AGE_COHORTS_I": _subscript_dict["AGE_COHORTS_I"],
    },
    _root,
    {
        "SEX_I": _subscript_dict["SEX_I"],
        "AGE_COHORTS_I": _subscript_dict["AGE_COHORTS_I"],
    },
    "_ext_constant_a_exponential_leab_to_mr",
)


@component.add(
    name="A_RURAL_REGRESSION",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_a_rural_regression"},
)
def a_rural_regression():
    """
    First parameter (a) of the linear regression model (y = a * x + b) to estimate the percentage of population in rural areas.
    """
    return _ext_constant_a_rural_regression()


_ext_constant_a_rural_regression = ExtConstant(
    "model_parameters/demography/demography.xlsx",
    "World",
    "a_rural_regression",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_a_rural_regression",
)


@component.add(
    name="AVERAGE_PEOPLE_PER_HOUSEHOLD_NON_EU_REGIONS_TIMESERIES_TARGET_SP",
    units="people/household",
    subscripts=["REGIONS_8_I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_average_people_per_household_non_eu_regions_timeseries_target_sp",
        "__lookup__": "_ext_lookup_average_people_per_household_non_eu_regions_timeseries_target_sp",
    },
)
def average_people_per_household_non_eu_regions_timeseries_target_sp(
    x, final_subs=None
):
    """
    Scenario parameter setting the number of people per household for the non EU regions through timeseries 2015-2100.
    """
    return _ext_lookup_average_people_per_household_non_eu_regions_timeseries_target_sp(
        x, final_subs
    )


_ext_lookup_average_people_per_household_non_eu_regions_timeseries_target_sp = (
    ExtLookup(
        "scenario_parameters/scenario_parameters.xlsx",
        "demography",
        "time_index_2015_2100",
        "AVERAGE_PEOPLE_PER_HOUSEHOLD_NON_EU_REGIONS_TIMESERIES_TARGET_SP",
        {"REGIONS_8_I": _subscript_dict["REGIONS_8_I"]},
        _root,
        {"REGIONS_8_I": _subscript_dict["REGIONS_8_I"]},
        "_ext_lookup_average_people_per_household_non_eu_regions_timeseries_target_sp",
    )
)


@component.add(
    name="B_EXPONENTIAL_LEAB_TO_MR",
    units="DMNL",
    subscripts=["SEX_I", "AGE_COHORTS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_b_exponential_leab_to_mr"},
)
def b_exponential_leab_to_mr():
    """
    Parameter B of the equation that related the life expectancy at birth and the mortality rates (MR = A * exp(B * LEAB)
    """
    return _ext_constant_b_exponential_leab_to_mr()


_ext_constant_b_exponential_leab_to_mr = ExtConstant(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "B_EXPONENTIAL_LEAB_TO_MR*",
    {
        "SEX_I": _subscript_dict["SEX_I"],
        "AGE_COHORTS_I": _subscript_dict["AGE_COHORTS_I"],
    },
    _root,
    {
        "SEX_I": _subscript_dict["SEX_I"],
        "AGE_COHORTS_I": _subscript_dict["AGE_COHORTS_I"],
    },
    "_ext_constant_b_exponential_leab_to_mr",
)


@component.add(
    name="B_RURAL_REGRESSION",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_b_rural_regression"},
)
def b_rural_regression():
    """
    Second parameter (b) of the linear regression model (y = a * x + b) to estimate the percentage of population in rural areas.
    """
    return _ext_constant_b_rural_regression()


_ext_constant_b_rural_regression = ExtConstant(
    "model_parameters/demography/demography.xlsx",
    "World",
    "b_rural_regression",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_b_rural_regression",
)


@component.add(
    name="BASE_NUMBER_OF_HOUSEHOLDS",
    units="DMNL/Year",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_base_number_of_households"},
)
def base_number_of_households():
    """
    Base number of households
    """
    return _ext_constant_base_number_of_households()


_ext_constant_base_number_of_households = ExtConstant(
    "model_parameters/economy/Consumption_BASE.xlsx",
    "BASE_Number_households",
    "IMV_BASE_NUMBER_OF_HOUSEHOLDS",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
    "_ext_constant_base_number_of_households",
)


@component.add(
    name="CAL_POPULATION",
    units="people",
    subscripts=["REGIONS_35_I"],
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_cal_population",
        "__data__": "_ext_data_cal_population",
        "time": 1,
    },
)
def cal_population():
    """
    Variable for calibration porpuses regional population by year
    """
    return _ext_data_cal_population(time())


_ext_data_cal_population = ExtData(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "HISTORICAL_TIME_POP_CAL",
    "CAL_POPULATION",
    None,
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    _root,
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    "_ext_data_cal_population",
)


@component.add(
    name="HISTORIC_EMIGRATIONS_RATE",
    units="DMNL",
    subscripts=["REGIONS_35_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_historic_emigrations_rate"},
)
def historic_emigrations_rate():
    """
    Share of population that emigrates per region
    """
    return _ext_constant_historic_emigrations_rate()


_ext_constant_historic_emigrations_rate = ExtConstant(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "HISTORIC_EMIGRATIONS_RATE",
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    _root,
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    "_ext_constant_historic_emigrations_rate",
)


@component.add(
    name="HISTORICAL_FERTILITY_RATES_2005_2010",
    units="people/(kpeople*Year)",
    subscripts=["REGIONS_35_I", "SEX_I", "FERTILITY_AGES_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_historical_fertility_rates_2005_2010"},
)
def historical_fertility_rates_2005_2010():
    """
    Exogenous data of the historical fertility rates in the period 2005-2010.
    """
    return _ext_constant_historical_fertility_rates_2005_2010()


_ext_constant_historical_fertility_rates_2005_2010 = ExtConstant(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "HISTORICAL_FERTILITY_RATES_2005_2010",
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
    "_ext_constant_historical_fertility_rates_2005_2010",
)


@component.add(
    name="HISTORICAL_FERTILITY_RATES_2010_2015",
    units="people/(kpeople*Year)",
    subscripts=["REGIONS_35_I", "SEX_I", "FERTILITY_AGES_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_historical_fertility_rates_2010_2015"},
)
def historical_fertility_rates_2010_2015():
    """
    Exogenous data of the historical fertility rates in the period 2010-2015.
    """
    return _ext_constant_historical_fertility_rates_2010_2015()


_ext_constant_historical_fertility_rates_2010_2015 = ExtConstant(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "HISTORICAL_FERTILITY_RATES_2010_2015",
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
    "_ext_constant_historical_fertility_rates_2010_2015",
)


@component.add(
    name="HISTORICAL_FERTILITY_RATES_2015_2020",
    units="people/(kpeople*Year)",
    subscripts=["REGIONS_35_I", "SEX_I", "FERTILITY_AGES_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_historical_fertility_rates_2015_2020"},
)
def historical_fertility_rates_2015_2020():
    """
    Exogenous data of the historical fertility rates in the period 2015-2020.
    """
    return _ext_constant_historical_fertility_rates_2015_2020()


_ext_constant_historical_fertility_rates_2015_2020 = ExtConstant(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "HISTORICAL_FERTILITY_RATES_2015_2020",
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
    "_ext_constant_historical_fertility_rates_2015_2020",
)


@component.add(
    name="HISTORICAL_GENDER_BIRTH_RATIO_2005_2010",
    units="DMNL",
    subscripts=["REGIONS_35_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_historical_gender_birth_ratio_2005_2010"
    },
)
def historical_gender_birth_ratio_2005_2010():
    """
    Exogenous data of the historical gender rate in birth in the period 2005-2010.
    """
    return _ext_constant_historical_gender_birth_ratio_2005_2010()


_ext_constant_historical_gender_birth_ratio_2005_2010 = ExtConstant(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "HISTORICAL_GENDER_BIRTH_RATIO_2005_2010",
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    _root,
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    "_ext_constant_historical_gender_birth_ratio_2005_2010",
)


@component.add(
    name="HISTORICAL_GENDER_BIRTH_RATIO_2010_2015",
    units="DMNL",
    subscripts=["REGIONS_35_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_historical_gender_birth_ratio_2010_2015"
    },
)
def historical_gender_birth_ratio_2010_2015():
    """
    Exogenous data of the historical gender rate in birth in the period 2010-2015.
    """
    return _ext_constant_historical_gender_birth_ratio_2010_2015()


_ext_constant_historical_gender_birth_ratio_2010_2015 = ExtConstant(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "HISTORICAL_GENDER_BIRTH_RATIO_2010_2015",
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    _root,
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    "_ext_constant_historical_gender_birth_ratio_2010_2015",
)


@component.add(
    name="HISTORICAL_GENDER_BIRTH_RATIO_2015_2020",
    units="DMNL",
    subscripts=["REGIONS_35_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_historical_gender_birth_ratio_2015_2020"
    },
)
def historical_gender_birth_ratio_2015_2020():
    """
    Exogenous data of the historical gender rate in birth in the period 2015-2020.
    """
    return _ext_constant_historical_gender_birth_ratio_2015_2020()


_ext_constant_historical_gender_birth_ratio_2015_2020 = ExtConstant(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "HISTORICAL_GENDER_BIRTH_RATIO_2015_2020",
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    _root,
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    "_ext_constant_historical_gender_birth_ratio_2015_2020",
)


@component.add(
    name="HISTORICAL_LIFE_EXPECTANCY_AT_BIRTH",
    units="Years",
    subscripts=["REGIONS_35_I", "SEX_I"],
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_historical_life_expectancy_at_birth",
        "__data__": "_ext_data_historical_life_expectancy_at_birth",
        "time": 1,
    },
)
def historical_life_expectancy_at_birth():
    """
    Historical life expectancy at birth for regions and gender.
    """
    return _ext_data_historical_life_expectancy_at_birth(time())


_ext_data_historical_life_expectancy_at_birth = ExtData(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "historical_time",
    "historical_life_expectancy_at_birth_AUSTRIA",
    "interpolate",
    {"REGIONS_35_I": ["AUSTRIA"], "SEX_I": _subscript_dict["SEX_I"]},
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SEX_I": _subscript_dict["SEX_I"],
    },
    "_ext_data_historical_life_expectancy_at_birth",
)

_ext_data_historical_life_expectancy_at_birth.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "historical_time",
    "historical_life_expectancy_at_birth_BELGIUM",
    "interpolate",
    {"REGIONS_35_I": ["BELGIUM"], "SEX_I": _subscript_dict["SEX_I"]},
)

_ext_data_historical_life_expectancy_at_birth.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "historical_time",
    "historical_life_expectancy_at_birth_BULGARIA",
    "interpolate",
    {"REGIONS_35_I": ["BULGARIA"], "SEX_I": _subscript_dict["SEX_I"]},
)

_ext_data_historical_life_expectancy_at_birth.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "historical_time",
    "historical_life_expectancy_at_birth_CROATIA",
    "interpolate",
    {"REGIONS_35_I": ["CROATIA"], "SEX_I": _subscript_dict["SEX_I"]},
)

_ext_data_historical_life_expectancy_at_birth.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "historical_time",
    "historical_life_expectancy_at_birth_CYPRUS",
    "interpolate",
    {"REGIONS_35_I": ["CYPRUS"], "SEX_I": _subscript_dict["SEX_I"]},
)

_ext_data_historical_life_expectancy_at_birth.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "historical_time",
    "historical_life_expectancy_at_birth_CZECH_REPUBLIC",
    "interpolate",
    {"REGIONS_35_I": ["CZECH_REPUBLIC"], "SEX_I": _subscript_dict["SEX_I"]},
)

_ext_data_historical_life_expectancy_at_birth.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "historical_time",
    "historical_life_expectancy_at_birth_DENMARK",
    "interpolate",
    {"REGIONS_35_I": ["DENMARK"], "SEX_I": _subscript_dict["SEX_I"]},
)

_ext_data_historical_life_expectancy_at_birth.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "historical_time",
    "historical_life_expectancy_at_birth_ESTONIA",
    "interpolate",
    {"REGIONS_35_I": ["ESTONIA"], "SEX_I": _subscript_dict["SEX_I"]},
)

_ext_data_historical_life_expectancy_at_birth.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "historical_time",
    "historical_life_expectancy_at_birth_FINLAND",
    "interpolate",
    {"REGIONS_35_I": ["FINLAND"], "SEX_I": _subscript_dict["SEX_I"]},
)

_ext_data_historical_life_expectancy_at_birth.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "historical_time",
    "historical_life_expectancy_at_birth_FRANCE",
    "interpolate",
    {"REGIONS_35_I": ["FRANCE"], "SEX_I": _subscript_dict["SEX_I"]},
)

_ext_data_historical_life_expectancy_at_birth.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "historical_time",
    "historical_life_expectancy_at_birth_GERMANY",
    "interpolate",
    {"REGIONS_35_I": ["GERMANY"], "SEX_I": _subscript_dict["SEX_I"]},
)

_ext_data_historical_life_expectancy_at_birth.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "historical_time",
    "historical_life_expectancy_at_birth_GREECE",
    "interpolate",
    {"REGIONS_35_I": ["GREECE"], "SEX_I": _subscript_dict["SEX_I"]},
)

_ext_data_historical_life_expectancy_at_birth.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "historical_time",
    "historical_life_expectancy_at_birth_HUNGARY",
    "interpolate",
    {"REGIONS_35_I": ["HUNGARY"], "SEX_I": _subscript_dict["SEX_I"]},
)

_ext_data_historical_life_expectancy_at_birth.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "historical_time",
    "historical_life_expectancy_at_birth_IRELAND",
    "interpolate",
    {"REGIONS_35_I": ["IRELAND"], "SEX_I": _subscript_dict["SEX_I"]},
)

_ext_data_historical_life_expectancy_at_birth.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "historical_time",
    "historical_life_expectancy_at_birth_ITALY",
    "interpolate",
    {"REGIONS_35_I": ["ITALY"], "SEX_I": _subscript_dict["SEX_I"]},
)

_ext_data_historical_life_expectancy_at_birth.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "historical_time",
    "historical_life_expectancy_at_birth_LATVIA",
    "interpolate",
    {"REGIONS_35_I": ["LATVIA"], "SEX_I": _subscript_dict["SEX_I"]},
)

_ext_data_historical_life_expectancy_at_birth.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "historical_time",
    "historical_life_expectancy_at_birth_LITHUANIA",
    "interpolate",
    {"REGIONS_35_I": ["LITHUANIA"], "SEX_I": _subscript_dict["SEX_I"]},
)

_ext_data_historical_life_expectancy_at_birth.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "historical_time",
    "historical_life_expectancy_at_birth_LUXEMBOURG",
    "interpolate",
    {"REGIONS_35_I": ["LUXEMBOURG"], "SEX_I": _subscript_dict["SEX_I"]},
)

_ext_data_historical_life_expectancy_at_birth.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "historical_time",
    "historical_life_expectancy_at_birth_MALTA",
    "interpolate",
    {"REGIONS_35_I": ["MALTA"], "SEX_I": _subscript_dict["SEX_I"]},
)

_ext_data_historical_life_expectancy_at_birth.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "historical_time",
    "historical_life_expectancy_at_birth_NETHERLANDS",
    "interpolate",
    {"REGIONS_35_I": ["NETHERLANDS"], "SEX_I": _subscript_dict["SEX_I"]},
)

_ext_data_historical_life_expectancy_at_birth.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "historical_time",
    "historical_life_expectancy_at_birth_POLAND",
    "interpolate",
    {"REGIONS_35_I": ["POLAND"], "SEX_I": _subscript_dict["SEX_I"]},
)

_ext_data_historical_life_expectancy_at_birth.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "historical_time",
    "historical_life_expectancy_at_birth_PORTUGAL",
    "interpolate",
    {"REGIONS_35_I": ["PORTUGAL"], "SEX_I": _subscript_dict["SEX_I"]},
)

_ext_data_historical_life_expectancy_at_birth.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "historical_time",
    "historical_life_expectancy_at_birth_ROMANIA",
    "interpolate",
    {"REGIONS_35_I": ["ROMANIA"], "SEX_I": _subscript_dict["SEX_I"]},
)

_ext_data_historical_life_expectancy_at_birth.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "historical_time",
    "historical_life_expectancy_at_birth_SLOVAKIA",
    "interpolate",
    {"REGIONS_35_I": ["SLOVAKIA"], "SEX_I": _subscript_dict["SEX_I"]},
)

_ext_data_historical_life_expectancy_at_birth.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "historical_time",
    "historical_life_expectancy_at_birth_SLOVENIA",
    "interpolate",
    {"REGIONS_35_I": ["SLOVENIA"], "SEX_I": _subscript_dict["SEX_I"]},
)

_ext_data_historical_life_expectancy_at_birth.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "historical_time",
    "historical_life_expectancy_at_birth_SPAIN",
    "interpolate",
    {"REGIONS_35_I": ["SPAIN"], "SEX_I": _subscript_dict["SEX_I"]},
)

_ext_data_historical_life_expectancy_at_birth.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "historical_time",
    "historical_life_expectancy_at_birth_SWEDEN",
    "interpolate",
    {"REGIONS_35_I": ["SWEDEN"], "SEX_I": _subscript_dict["SEX_I"]},
)

_ext_data_historical_life_expectancy_at_birth.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "historical_time",
    "historical_life_expectancy_at_birth_UK",
    "interpolate",
    {"REGIONS_35_I": ["UK"], "SEX_I": _subscript_dict["SEX_I"]},
)

_ext_data_historical_life_expectancy_at_birth.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "historical_time",
    "historical_life_expectancy_at_birth_CHINA",
    "interpolate",
    {"REGIONS_35_I": ["CHINA"], "SEX_I": _subscript_dict["SEX_I"]},
)

_ext_data_historical_life_expectancy_at_birth.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "historical_time",
    "historical_life_expectancy_at_birth_EASOC",
    "interpolate",
    {"REGIONS_35_I": ["EASOC"], "SEX_I": _subscript_dict["SEX_I"]},
)

_ext_data_historical_life_expectancy_at_birth.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "historical_time",
    "historical_life_expectancy_at_birth_INDIA",
    "interpolate",
    {"REGIONS_35_I": ["INDIA"], "SEX_I": _subscript_dict["SEX_I"]},
)

_ext_data_historical_life_expectancy_at_birth.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "historical_time",
    "historical_life_expectancy_at_birth_LATAM",
    "interpolate",
    {"REGIONS_35_I": ["LATAM"], "SEX_I": _subscript_dict["SEX_I"]},
)

_ext_data_historical_life_expectancy_at_birth.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "historical_time",
    "historical_life_expectancy_at_birth_RUSSIA",
    "interpolate",
    {"REGIONS_35_I": ["RUSSIA"], "SEX_I": _subscript_dict["SEX_I"]},
)

_ext_data_historical_life_expectancy_at_birth.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "historical_time",
    "historical_life_expectancy_at_birth_USMCA",
    "interpolate",
    {"REGIONS_35_I": ["USMCA"], "SEX_I": _subscript_dict["SEX_I"]},
)

_ext_data_historical_life_expectancy_at_birth.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "historical_time",
    "historical_life_expectancy_at_birth_LROW",
    "interpolate",
    {"REGIONS_35_I": ["LROW"], "SEX_I": _subscript_dict["SEX_I"]},
)


@component.add(
    name="historical_population_regions_lt",
    units="people",
    subscripts=["REGIONS_9_I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_historical_population_regions_lt",
        "__lookup__": "_ext_lookup_historical_population_regions_lt",
    },
)
def historical_population_regions_lt(x, final_subs=None):
    """
    Historical population in regions.
    """
    return _ext_lookup_historical_population_regions_lt(x, final_subs)


_ext_lookup_historical_population_regions_lt = ExtLookup(
    "model_parameters/demography/demography.xlsx",
    "World",
    "time_historicalPop",
    "HistPopLT",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_lookup_historical_population_regions_lt",
)


@component.add(
    name="INITIAL_RATIO_EU_HOUSEHOLDS_PER_100_PEOPLE",
    units="households/person",
    subscripts=["REGIONS_EU27_I", "HOUSEHOLDS_DEMOGRAPHY_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_initial_ratio_eu_households_per_100_people"
    },
)
def initial_ratio_eu_households_per_100_people():
    """
    Initial ratio of households per 100 people
    """
    return _ext_constant_initial_ratio_eu_households_per_100_people()


_ext_constant_initial_ratio_eu_households_per_100_people = ExtConstant(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "INITIAL_RATIO_EU_HOUSEHOLDS_PER_100_PEOPLE*",
    {
        "REGIONS_EU27_I": _subscript_dict["REGIONS_EU27_I"],
        "HOUSEHOLDS_DEMOGRAPHY_I": _subscript_dict["HOUSEHOLDS_DEMOGRAPHY_I"],
    },
    _root,
    {
        "REGIONS_EU27_I": _subscript_dict["REGIONS_EU27_I"],
        "HOUSEHOLDS_DEMOGRAPHY_I": _subscript_dict["HOUSEHOLDS_DEMOGRAPHY_I"],
    },
    "_ext_constant_initial_ratio_eu_households_per_100_people",
)


@component.add(
    name="LIFE_EXPECTANCY_AT_BIRTH_AVERAGES_SP",
    units="Years/(Years*Years)",
    subscripts=["REGIONS_35_I", "SEX_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_life_expectancy_at_birth_averages_sp"},
)
def life_expectancy_at_birth_averages_sp():
    """
    Selection of the values for the high life expectancy at birth (historical average)
    """
    return _ext_constant_life_expectancy_at_birth_averages_sp()


_ext_constant_life_expectancy_at_birth_averages_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "demography_data",
    "LEAB_AVERAGES_SP",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SEX_I": _subscript_dict["SEX_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SEX_I": _subscript_dict["SEX_I"],
    },
    "_ext_constant_life_expectancy_at_birth_averages_sp",
)


@component.add(
    name="LIFE_EXPECTANCY_AT_BIRTH_MAXIMUMS_SP",
    units="Years/(Years*Years)",
    subscripts=["REGIONS_35_I", "SEX_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_life_expectancy_at_birth_maximums_sp"},
)
def life_expectancy_at_birth_maximums_sp():
    """
    Selection of the values for the high life expectancy at birth (historical maximum)
    """
    return _ext_constant_life_expectancy_at_birth_maximums_sp()


_ext_constant_life_expectancy_at_birth_maximums_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "demography_data",
    "LEAB_MAXIMUMS_SP",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SEX_I": _subscript_dict["SEX_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SEX_I": _subscript_dict["SEX_I"],
    },
    "_ext_constant_life_expectancy_at_birth_maximums_sp",
)


@component.add(
    name="LIFE_EXPECTANCY_AT_BIRTH_MINIMUMS_SP",
    units="Years/(Years*Years)",
    subscripts=["REGIONS_35_I", "SEX_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_life_expectancy_at_birth_minimums_sp"},
)
def life_expectancy_at_birth_minimums_sp():
    """
    Selection of the values for the high life expectancy at birth (historical minimum)
    """
    return _ext_constant_life_expectancy_at_birth_minimums_sp()


_ext_constant_life_expectancy_at_birth_minimums_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "demography_data",
    "LEAB_MINIMUMS_SP",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SEX_I": _subscript_dict["SEX_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SEX_I": _subscript_dict["SEX_I"],
    },
    "_ext_constant_life_expectancy_at_birth_minimums_sp",
)


@component.add(
    name="MAX_VARIATION_EU_HOUSEHOLDS_PER_100_PEOPLE",
    units="households/(person*Year)",
    subscripts=["REGIONS_EU27_I", "HOUSEHOLDS_DEMOGRAPHY_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_max_variation_eu_households_per_100_people"
    },
)
def max_variation_eu_households_per_100_people():
    """
    Maximum annual variations in the ratio of households per 100 people.
    """
    return _ext_constant_max_variation_eu_households_per_100_people()


_ext_constant_max_variation_eu_households_per_100_people = ExtConstant(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "MAX_SLOPE_RATIO_HOUSEHOLDS*",
    {
        "REGIONS_EU27_I": _subscript_dict["REGIONS_EU27_I"],
        "HOUSEHOLDS_DEMOGRAPHY_I": _subscript_dict["HOUSEHOLDS_DEMOGRAPHY_I"],
    },
    _root,
    {
        "REGIONS_EU27_I": _subscript_dict["REGIONS_EU27_I"],
        "HOUSEHOLDS_DEMOGRAPHY_I": _subscript_dict["HOUSEHOLDS_DEMOGRAPHY_I"],
    },
    "_ext_constant_max_variation_eu_households_per_100_people",
)


@component.add(
    name="MAXIMUM_LIFE_EXPECTANCY_AT_BIRTH",
    units="Years",
    subscripts=["SEX_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_maximum_life_expectancy_at_birth"},
)
def maximum_life_expectancy_at_birth():
    """
    Maximum of the life expectancy at birth to human beings.
    """
    return _ext_constant_maximum_life_expectancy_at_birth()


_ext_constant_maximum_life_expectancy_at_birth = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "demography_data",
    "MAX_LIFE_EXPECTANCY_AT_BIRTH",
    {"SEX_I": _subscript_dict["SEX_I"]},
    _root,
    {"SEX_I": _subscript_dict["SEX_I"]},
    "_ext_constant_maximum_life_expectancy_at_birth",
)


@component.add(
    name="MEAN_VARIATION_EU_HOUSEHOLDS_PER_100_PEOPLE",
    units="households/(person*Year)",
    subscripts=["REGIONS_EU27_I", "HOUSEHOLDS_DEMOGRAPHY_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_mean_variation_eu_households_per_100_people"
    },
)
def mean_variation_eu_households_per_100_people():
    """
    Average annual variations in the ratio of households per 100 people
    """
    return _ext_constant_mean_variation_eu_households_per_100_people()


_ext_constant_mean_variation_eu_households_per_100_people = ExtConstant(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "MEAN_SLOPE_RATIO_HOUSEHOLDS*",
    {
        "REGIONS_EU27_I": _subscript_dict["REGIONS_EU27_I"],
        "HOUSEHOLDS_DEMOGRAPHY_I": _subscript_dict["HOUSEHOLDS_DEMOGRAPHY_I"],
    },
    _root,
    {
        "REGIONS_EU27_I": _subscript_dict["REGIONS_EU27_I"],
        "HOUSEHOLDS_DEMOGRAPHY_I": _subscript_dict["HOUSEHOLDS_DEMOGRAPHY_I"],
    },
    "_ext_constant_mean_variation_eu_households_per_100_people",
)


@component.add(
    name="MIN_HISTORICAL_MORTALITY_RATE",
    units="people/(Year*kpeople)",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_min_historical_mortality_rate"},
)
def min_historical_mortality_rate():
    """
    Minimum historical mortality rate to constraint the modelling of deaths.
    """
    return _ext_constant_min_historical_mortality_rate()


_ext_constant_min_historical_mortality_rate = ExtConstant(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "MIN_HISTORICAL_MORTALITY_RATE",
    {},
    _root,
    {},
    "_ext_constant_min_historical_mortality_rate",
)


@component.add(
    name="MIN_VARIATION_EU_HOUSEHOLDS_PER_100_PEOPLE",
    units="households/(person*Year)",
    subscripts=["REGIONS_EU27_I", "HOUSEHOLDS_DEMOGRAPHY_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_min_variation_eu_households_per_100_people"
    },
)
def min_variation_eu_households_per_100_people():
    """
    Minimum annual variations in the ratio of households per 100 people
    """
    return _ext_constant_min_variation_eu_households_per_100_people()


_ext_constant_min_variation_eu_households_per_100_people = ExtConstant(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "MIN_SLOPE_RATIO_HOUSEHOLDS*",
    {
        "REGIONS_EU27_I": _subscript_dict["REGIONS_EU27_I"],
        "HOUSEHOLDS_DEMOGRAPHY_I": _subscript_dict["HOUSEHOLDS_DEMOGRAPHY_I"],
    },
    _root,
    {
        "REGIONS_EU27_I": _subscript_dict["REGIONS_EU27_I"],
        "HOUSEHOLDS_DEMOGRAPHY_I": _subscript_dict["HOUSEHOLDS_DEMOGRAPHY_I"],
    },
    "_ext_constant_min_variation_eu_households_per_100_people",
)


@component.add(
    name="MINIMUM_POPULATION_RURAL",
    units="percent",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_minimum_population_rural"},
)
def minimum_population_rural():
    """
    Minimum value of population in rural areas.
    """
    return _ext_constant_minimum_population_rural()


_ext_constant_minimum_population_rural = ExtConstant(
    "model_parameters/demography/demography.xlsx",
    "World",
    "minimum_rural_regression",
    {},
    _root,
    {},
    "_ext_constant_minimum_population_rural",
)


@component.add(
    name="OBJECTIVE_FERTILITY_RATES_SP",
    units="DMNL",
    subscripts=["REGIONS_35_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_objective_fertility_rates_sp"},
)
def objective_fertility_rates_sp():
    """
    Selection of the qualitative scenario (minimum, average, maximum) for the fertility rates
    """
    return _ext_constant_objective_fertility_rates_sp()


_ext_constant_objective_fertility_rates_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "demography",
    "OBJECTIVE_FERTILITY_RATES_SP*",
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    _root,
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    "_ext_constant_objective_fertility_rates_sp",
)


@component.add(
    name="OBJECTIVE_LIFE_EXPECTANCY_AT_BIRTH_SP",
    units="DMNL",
    subscripts=["REGIONS_35_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_objective_life_expectancy_at_birth_sp"},
)
def objective_life_expectancy_at_birth_sp():
    """
    Selection of the qualitative scenario (high, medium, low) for the life expectancy at birth
    """
    return _ext_constant_objective_life_expectancy_at_birth_sp()


_ext_constant_objective_life_expectancy_at_birth_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "demography",
    "OBJECTIVE_LEAB_SP*",
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    _root,
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    "_ext_constant_objective_life_expectancy_at_birth_sp",
)


@component.add(
    name="PERCENTAGE_EMIGRATIONS_SP",
    subscripts=["REGIONS_35_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_percentage_emigrations_sp"},
)
def percentage_emigrations_sp():
    return _ext_constant_percentage_emigrations_sp()


_ext_constant_percentage_emigrations_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "demography",
    "PERCENTAGE_EMIGRATIONS_SP*",
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    _root,
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    "_ext_constant_percentage_emigrations_sp",
)


@component.add(
    name="POPULATION_2004",
    units="people",
    subscripts=["REGIONS_35_I", "SEX_I", "AGE_COHORTS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_population_2004"},
)
def population_2004():
    """
    Snapshot of the population in the year before the simulation (2004) to do the delays of the population.
    """
    return _ext_constant_population_2004()


_ext_constant_population_2004 = ExtConstant(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "POP_FEMALE_2004",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SEX_I": ["FEMALE"],
        "AGE_COHORTS_I": _subscript_dict["AGE_COHORTS_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SEX_I": _subscript_dict["SEX_I"],
        "AGE_COHORTS_I": _subscript_dict["AGE_COHORTS_I"],
    },
    "_ext_constant_population_2004",
)

_ext_constant_population_2004.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "POP_MALE_2004",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SEX_I": ["MALE"],
        "AGE_COHORTS_I": _subscript_dict["AGE_COHORTS_I"],
    },
)


@component.add(
    name="POPULATION_2005",
    units="people",
    subscripts=["REGIONS_35_I", "SEX_I", "AGE_COHORTS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_population_2005"},
)
def population_2005():
    """
    Snapshot of the population in the first year of simulation (2005) to initialize the stock of population.
    """
    return _ext_constant_population_2005()


_ext_constant_population_2005 = ExtConstant(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "POP_FEMALE_2005",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SEX_I": ["FEMALE"],
        "AGE_COHORTS_I": _subscript_dict["AGE_COHORTS_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SEX_I": _subscript_dict["SEX_I"],
        "AGE_COHORTS_I": _subscript_dict["AGE_COHORTS_I"],
    },
    "_ext_constant_population_2005",
)

_ext_constant_population_2005.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "POP_MALE_2005",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SEX_I": ["MALE"],
        "AGE_COHORTS_I": _subscript_dict["AGE_COHORTS_I"],
    },
)


@component.add(
    name="SCENARIO_FERTILITY_RATE_AVERAGE_SP",
    units="people/(kpeople*Year)",
    subscripts=["REGIONS_35_I", "SEX_I", "FERTILITY_AGES_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_scenario_fertility_rate_average_sp"},
)
def scenario_fertility_rate_average_sp():
    """
    Selection of the values for the medium fertility rates (historical average)
    """
    return _ext_constant_scenario_fertility_rate_average_sp()


_ext_constant_scenario_fertility_rate_average_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "demography_data",
    "SCEN_FERTILITY_AVERAGE",
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
    "_ext_constant_scenario_fertility_rate_average_sp",
)


@component.add(
    name="SCENARIO_FERTILITY_RATE_MAXIMUM_SP",
    units="people/(kpeople*Year)",
    subscripts=["REGIONS_35_I", "SEX_I", "FERTILITY_AGES_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_scenario_fertility_rate_maximum_sp"},
)
def scenario_fertility_rate_maximum_sp():
    """
    Selection of the values for the high fertility rates (historical maximum)
    """
    return _ext_constant_scenario_fertility_rate_maximum_sp()


_ext_constant_scenario_fertility_rate_maximum_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "demography_data",
    "SCEN_FERTILITY_MAXIMUM",
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
    "_ext_constant_scenario_fertility_rate_maximum_sp",
)


@component.add(
    name="SCENARIO_FERTILITY_RATE_MINIMUM_SP",
    units="people/(kpeople*Year)",
    subscripts=["REGIONS_35_I", "SEX_I", "FERTILITY_AGES_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_scenario_fertility_rate_minimum_sp"},
)
def scenario_fertility_rate_minimum_sp():
    """
    Selection of the values for the low fertility rates (historical minimum)
    """
    return _ext_constant_scenario_fertility_rate_minimum_sp()


_ext_constant_scenario_fertility_rate_minimum_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "demography_data",
    "SCEN_FERTILITY_MINIMUM",
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
    "_ext_constant_scenario_fertility_rate_minimum_sp",
)


@component.add(
    name="SELECT_SLOPE_EVOLUTION_OF_EU27_HOUSEHOLDS_COMPOSITION_SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_select_slope_evolution_of_eu27_households_composition_sp"
    },
)
def select_slope_evolution_of_eu27_households_composition_sp():
    """
    Value for the switch scenario for households composition for EU27 countries. 4 options for the evolution of the ratio of households per 100 people over time available from the statistical analysis of past data: 0: Constant 2015 values 1: Mean values for future trend 2: Minimum values for future trend 3: Maximum values for future trend
    """
    return _ext_constant_select_slope_evolution_of_eu27_households_composition_sp()


_ext_constant_select_slope_evolution_of_eu27_households_composition_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "demography",
    "SLOPE_EU_HOUSEHOLDS_SP",
    {},
    _root,
    {},
    "_ext_constant_select_slope_evolution_of_eu27_households_composition_sp",
)


@component.add(
    name="SHARES_EMIGRATION_SP",
    units="DMNL",
    subscripts=["REGIONS_35_I", "REGIONS_35_MAP_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_shares_emigration_sp"},
)
def shares_emigration_sp():
    """
    Shares to distribute each regional emigration into the rest of regions
    """
    return _ext_constant_shares_emigration_sp()


_ext_constant_shares_emigration_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "demography_data",
    "SHARES_MIGRATION_SP",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "REGIONS_35_MAP_I": _subscript_dict["REGIONS_35_MAP_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "REGIONS_35_MAP_I": _subscript_dict["REGIONS_35_MAP_I"],
    },
    "_ext_constant_shares_emigration_sp",
)


@component.add(
    name="START_YEAR_MIGRATIONS_SP",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_start_year_migrations_sp"},
)
def start_year_migrations_sp():
    return _ext_constant_start_year_migrations_sp()


_ext_constant_start_year_migrations_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "demography",
    "START_YEAR_MIGRATIONS_SP",
    {},
    _root,
    {},
    "_ext_constant_start_year_migrations_sp",
)


@component.add(
    name="TARGET_YEAR_FERTILITY_RATES_SP",
    units="Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_target_year_fertility_rates_sp"},
)
def target_year_fertility_rates_sp():
    """
    Final year of policy/scenario of fertility rates
    """
    return _ext_constant_target_year_fertility_rates_sp()


_ext_constant_target_year_fertility_rates_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "demography",
    "YEAR_FINAL_FERTILITY_RATES_SP*",
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    _root,
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    "_ext_constant_target_year_fertility_rates_sp",
)


@component.add(
    name="TARGET_YEAR_LIFE_EXPECTANCY_AT_BIRTH_SP",
    units="DMNL",
    subscripts=["REGIONS_35_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_target_year_life_expectancy_at_birth_sp"
    },
)
def target_year_life_expectancy_at_birth_sp():
    """
    Final year of policy/scenario of life expectancy at birth
    """
    return _ext_constant_target_year_life_expectancy_at_birth_sp()


_ext_constant_target_year_life_expectancy_at_birth_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "demography",
    "LEAB_YEAR_FINAL_LEAB_SP*",
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    _root,
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    "_ext_constant_target_year_life_expectancy_at_birth_sp",
)
