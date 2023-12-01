"""
Module society.exogenous_inputs
Translated using PySD version 3.10.0
"""


@component.add(
    name="BETA_0_EDUCATIONAL_LEVEL",
    units="DMNL",
    subscripts=["REGIONS_35_I", "EDUCATIONAL_LEVEL_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_beta_0_educational_level"},
)
def beta_0_educational_level():
    """
    BETAS are for calculating the percentage of new workers at educational level (25-34 years)
    """
    return _ext_constant_beta_0_educational_level()


_ext_constant_beta_0_educational_level = ExtConstant(
    "model_parameters/society/society.xlsx",
    "education",
    "BETA_1_EDUCATIONAL_LEVEL_HIGH_MP*",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "EDUCATIONAL_LEVEL_I": ["HIGH_EDUCATION"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "EDUCATIONAL_LEVEL_I": _subscript_dict["EDUCATIONAL_LEVEL_I"],
    },
    "_ext_constant_beta_0_educational_level",
)

_ext_constant_beta_0_educational_level.add(
    "model_parameters/society/society.xlsx",
    "education",
    "BETA_1_EDUCATIONAL_LEVEL_MEDIUM_MP*",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "EDUCATIONAL_LEVEL_I": ["MEDIUM_EDUCATION"],
    },
)


@component.add(
    name="BETA_1_EDUCATIONAL_LEVEL",
    units="(Year*person)/Mdollars_2015",
    subscripts=["REGIONS_35_I", "EDUCATIONAL_LEVEL_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_beta_1_educational_level"},
)
def beta_1_educational_level():
    """
    BETAS are for calculating the percentage of new workers at educational level (25-34 years)
    """
    return _ext_constant_beta_1_educational_level()


_ext_constant_beta_1_educational_level = ExtConstant(
    "model_parameters/society/society.xlsx",
    "education",
    "BETA_2_EDUCATIONAL_LEVEL_HIGH_MP*",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "EDUCATIONAL_LEVEL_I": ["HIGH_EDUCATION"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "EDUCATIONAL_LEVEL_I": _subscript_dict["EDUCATIONAL_LEVEL_I"],
    },
    "_ext_constant_beta_1_educational_level",
)

_ext_constant_beta_1_educational_level.add(
    "model_parameters/society/society.xlsx",
    "education",
    "BETA_2_EDUCATIONAL_LEVEL_MEDIUM_MP*",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "EDUCATIONAL_LEVEL_I": ["MEDIUM_EDUCATION"],
    },
)


@component.add(
    name="CONVERSION_TO_PURCHASING_PARITY_POWER_MP",
    units="Mdollars_2017PPP/Mdollars_2015",
    subscripts=["REGIONS_35_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_conversion_to_purchasing_parity_power_mp"
    },
)
def conversion_to_purchasing_parity_power_mp():
    return _ext_constant_conversion_to_purchasing_parity_power_mp()


_ext_constant_conversion_to_purchasing_parity_power_mp = ExtConstant(
    "model_parameters/society/society.xlsx",
    "developement_human_index",
    "CONVERSION_TO_PURCHASING_PARITY_POWER_MP*",
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    _root,
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    "_ext_constant_conversion_to_purchasing_parity_power_mp",
)


@component.add(
    name="FINAL_GENDER_PARITY_INDEX_SP",
    units="DMNL",
    subscripts=["REGIONS_35_I", "EDUCATIONAL_LEVEL_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_final_gender_parity_index_sp"},
)
def final_gender_parity_index_sp():
    """
    Target value by region in the final year of the gender parity index.
    """
    return _ext_constant_final_gender_parity_index_sp()


_ext_constant_final_gender_parity_index_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "society",
    "FINAL_GENDER_PARITY_INDEX_HIGH_SP*",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "EDUCATIONAL_LEVEL_I": ["HIGH_EDUCATION"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "EDUCATIONAL_LEVEL_I": _subscript_dict["EDUCATIONAL_LEVEL_I"],
    },
    "_ext_constant_final_gender_parity_index_sp",
)

_ext_constant_final_gender_parity_index_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "society",
    "FINAL_GENDER_PARITY_INDEX_MEDIUM_SP*",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "EDUCATIONAL_LEVEL_I": ["MEDIUM_EDUCATION"],
    },
)


@component.add(
    name="High_range_FEC_good_standard_of_living",
    units="GJ/(Year*people)",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_high_range_fec_good_standard_of_living"},
)
def high_range_fec_good_standard_of_living():
    """
    40 GJ/yr per capita: high range FEC good standard of living (Lamb & Steinberger (2017), i.e. above 70 years life expectancy, full access to water, sanitation, electricity and other basic infrastructures.
    """
    return _ext_constant_high_range_fec_good_standard_of_living()


_ext_constant_high_range_fec_good_standard_of_living = ExtConstant(
    "model_parameters/society/society.xlsx",
    "World",
    "High_range_FEC_good_standard_of_living",
    {},
    _root,
    {},
    "_ext_constant_high_range_fec_good_standard_of_living",
)


@component.add(
    name="INITIAL_ACCUMULATED_PUBLIC_EXPENDITURE_ON_EDUCATION_PER_CAPITA",
    units="Mdollars/people",
    subscripts=["REGIONS_35_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_initial_accumulated_public_expenditure_on_education_per_capita"
    },
)
def initial_accumulated_public_expenditure_on_education_per_capita():
    return (
        _ext_constant_initial_accumulated_public_expenditure_on_education_per_capita()
    )


_ext_constant_initial_accumulated_public_expenditure_on_education_per_capita = (
    ExtConstant(
        "model_parameters/society/society.xlsx",
        "education",
        "INITIAL_ACCUMULATED_PUBLIC_EXPENDITURE_ON_EDUCATION_PER_CAPITA_MP*",
        {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
        _root,
        {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
        "_ext_constant_initial_accumulated_public_expenditure_on_education_per_capita",
    )
)


@component.add(
    name="INITIAL_GENDER_PARITY_INDEX",
    units="DMNL",
    subscripts=["REGIONS_35_I", "EDUCATIONAL_LEVEL_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_gender_parity_index"},
)
def initial_gender_parity_index():
    """
    2015 is subtracted as it is the initial simulation time.
    """
    return _ext_constant_initial_gender_parity_index()


_ext_constant_initial_gender_parity_index = ExtConstant(
    "model_parameters/society/society.xlsx",
    "education",
    "GENDER_PARITY_INDEX_HIGH_MP*",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "EDUCATIONAL_LEVEL_I": ["HIGH_EDUCATION"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "EDUCATIONAL_LEVEL_I": _subscript_dict["EDUCATIONAL_LEVEL_I"],
    },
    "_ext_constant_initial_gender_parity_index",
)

_ext_constant_initial_gender_parity_index.add(
    "model_parameters/society/society.xlsx",
    "education",
    "GENDER_PARITY_INDEX_MEDIUM_MP*",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "EDUCATIONAL_LEVEL_I": ["MEDIUM_EDUCATION"],
    },
)


@component.add(
    name="INITIAL_SHARE_OF_WORKFORCE_IN_EACH_EDUCATIONAL_LEVEL",
    units="DMNL",
    subscripts=["REGIONS_35_I", "EDUCATIONAL_LEVEL_I", "SEX_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_initial_share_of_workforce_in_each_educational_level"
    },
)
def initial_share_of_workforce_in_each_educational_level():
    return _ext_constant_initial_share_of_workforce_in_each_educational_level()


_ext_constant_initial_share_of_workforce_in_each_educational_level = ExtConstant(
    "model_parameters/society/society.xlsx",
    "education",
    "INITIAL_PROPORTION_OF_WORKFORCE_IN_EACH_EDUCATIONAL_LEVEL_FEMALE_MP",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "EDUCATIONAL_LEVEL_I": _subscript_dict["EDUCATIONAL_LEVEL_I"],
        "SEX_I": ["FEMALE"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "EDUCATIONAL_LEVEL_I": _subscript_dict["EDUCATIONAL_LEVEL_I"],
        "SEX_I": _subscript_dict["SEX_I"],
    },
    "_ext_constant_initial_share_of_workforce_in_each_educational_level",
)

_ext_constant_initial_share_of_workforce_in_each_educational_level.add(
    "model_parameters/society/society.xlsx",
    "education",
    "INITIAL_PROPORTION_OF_WORKFORCE_IN_EACH_EDUCATIONAL_LEVEL_MALE_MP",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "EDUCATIONAL_LEVEL_I": _subscript_dict["EDUCATIONAL_LEVEL_I"],
        "SEX_I": ["MALE"],
    },
)


@component.add(
    name="Low_range_FEC_good_standard_of_living",
    units="GJ/(Year*people)",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_low_range_fec_good_standard_of_living"},
)
def low_range_fec_good_standard_of_living():
    """
    30 GJ/yr per capita: low range FEC good standard of living (Lamb & Steinberger (2017), i.e. above 70 years life expectancy, full access to water, sanitation, electricity and other basic infrastructures.
    """
    return _ext_constant_low_range_fec_good_standard_of_living()


_ext_constant_low_range_fec_good_standard_of_living = ExtConstant(
    "model_parameters/society/society.xlsx",
    "World",
    "Low_range_FEC_good_standard_of_living",
    {},
    _root,
    {},
    "_ext_constant_low_range_fec_good_standard_of_living",
)


@component.add(
    name="minimum_EROI_Brandt_2017",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_minimum_eroi_brandt_2017"},
)
def minimum_eroi_brandt_2017():
    """
    "At levels of net energy return ? 5 J/J, the fraction of productive outputs free to use in discretionary purposes declines rapidly, resulting in the emergence of an effective "minimum EROI" below which prosperity is burdened by excessive direct and indirect requirements of the energy sector." Source: Brandt (2017).
    """
    return _ext_constant_minimum_eroi_brandt_2017()


_ext_constant_minimum_eroi_brandt_2017 = ExtConstant(
    "model_parameters/society/society.xlsx",
    "World",
    "Brandt_2017",
    {},
    _root,
    {},
    "_ext_constant_minimum_eroi_brandt_2017",
)


@component.add(
    name="minimum_EROI_Hall_et_al_2009",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_minimum_eroi_hall_et_al_2009"},
)
def minimum_eroi_hall_et_al_2009():
    """
    Minimum EROI.
    """
    return _ext_constant_minimum_eroi_hall_et_al_2009()


_ext_constant_minimum_eroi_hall_et_al_2009 = ExtConstant(
    "model_parameters/society/society.xlsx",
    "World",
    "Hall_et_al_2009",
    {},
    _root,
    {},
    "_ext_constant_minimum_eroi_hall_et_al_2009",
)


@component.add(
    name="SWITCH_POLICY_GENDER_PARITY_INDEX_SP",
    units="DMNL",
    subscripts=["REGIONS_35_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_policy_gender_parity_index_sp"},
)
def switch_policy_gender_parity_index_sp():
    """
    Target value by region in the final year of the gender parity index.
    """
    return _ext_constant_switch_policy_gender_parity_index_sp()


_ext_constant_switch_policy_gender_parity_index_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "society",
    "SWITCH_GENDER_PARITY_INDEX_SP*",
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    _root,
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    "_ext_constant_switch_policy_gender_parity_index_sp",
)


@component.add(
    name="Threshold_FEC_'high_development'",
    units="GJ/(Year*people)",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_threshold_fec_high_development"},
)
def threshold_fec_high_development():
    """
    75 GJ/yr per capita. Minimum final energy consumption threshold approximating a "high development" standard of living (Arto et al. (2016)), i.e. HDI>0.8.
    """
    return _ext_constant_threshold_fec_high_development()


_ext_constant_threshold_fec_high_development = ExtConstant(
    "model_parameters/society/society.xlsx",
    "World",
    "Threshold_FEC_high_development",
    {},
    _root,
    {},
    "_ext_constant_threshold_fec_high_development",
)


@component.add(
    name="TPEDpc_acceptable_standard_living",
    units="GJ/people",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_tpedpc_acceptable_standard_living"},
)
def tpedpc_acceptable_standard_living():
    """
    Approximative energy use value to fulfill the aceptable standard of living (in terms of total primary energy use): 40 GJ/person. Source: (Goldemberg, 2011; Rao et al, 2014, WBGU,2003) cited in Arto et al., (2016).
    """
    return _ext_constant_tpedpc_acceptable_standard_living()


_ext_constant_tpedpc_acceptable_standard_living = ExtConstant(
    "model_parameters/society/society.xlsx",
    "World",
    "TPEDpc_acceptable_standard_living",
    {},
    _root,
    {},
    "_ext_constant_tpedpc_acceptable_standard_living",
)


@component.add(
    name="TPEFpc_threshold_high_development",
    units="GJ/people",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_tpefpc_threshold_high_development"},
)
def tpefpc_threshold_high_development():
    """
    Energy use threshold (in terms of total primary energy footprint) found by Arto et al., (2016) to reach high development (HDI>0.8).
    """
    return _ext_constant_tpefpc_threshold_high_development()


_ext_constant_tpefpc_threshold_high_development = ExtConstant(
    "model_parameters/society/society.xlsx",
    "World",
    "TPEFpc_threshold_high_development",
    {},
    _root,
    {},
    "_ext_constant_tpefpc_threshold_high_development",
)


@component.add(
    name="YEAR_FINAL_GENDER_PARITY_INDEX_SP",
    units="Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_year_final_gender_parity_index_sp"},
)
def year_final_gender_parity_index_sp():
    return _ext_constant_year_final_gender_parity_index_sp()


_ext_constant_year_final_gender_parity_index_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "society",
    "YEAR_FINAL_GENDER_PARITY_INDEX_SP*",
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    _root,
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    "_ext_constant_year_final_gender_parity_index_sp",
)


@component.add(
    name="YEAR_INITIAL_GENDER_PARITY_INDEX_SP",
    units="Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_year_initial_gender_parity_index_sp"},
)
def year_initial_gender_parity_index_sp():
    return _ext_constant_year_initial_gender_parity_index_sp()


_ext_constant_year_initial_gender_parity_index_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "society",
    "YEAR_INITIAL_GENDER_PARITY_INDEX_SP*",
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    _root,
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    "_ext_constant_year_initial_gender_parity_index_sp",
)


@component.add(
    name="YEARS_OF_EDUCATION_CORRESPONDING_TO_EACH_LEVEL_FOR_MEANS_YEARS_OF_SCHOOLING_MP",
    units="Years",
    subscripts=["EDUCATIONAL_LEVEL_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_years_of_education_corresponding_to_each_level_for_means_years_of_schooling_mp"
    },
)
def years_of_education_corresponding_to_each_level_for_means_years_of_schooling_mp():
    return (
        _ext_constant_years_of_education_corresponding_to_each_level_for_means_years_of_schooling_mp()
    )


_ext_constant_years_of_education_corresponding_to_each_level_for_means_years_of_schooling_mp = ExtConstant(
    "model_parameters/society/society.xlsx",
    "developement_human_index",
    "YEARS_OF_EDUCATION_CORRESPONDING_TO_EACH_LEVEL_FOR_MEANS_YEARS_OF_SCHOOLING_MP",
    {"EDUCATIONAL_LEVEL_I": _subscript_dict["EDUCATIONAL_LEVEL_I"]},
    _root,
    {"EDUCATIONAL_LEVEL_I": _subscript_dict["EDUCATIONAL_LEVEL_I"]},
    "_ext_constant_years_of_education_corresponding_to_each_level_for_means_years_of_schooling_mp",
)


@component.add(
    name="YEARS_OF_EDUCATION_CORRESPONDING_TO_EACH_LEVEL_FOR_SCHOOLING_LIFE_EXPECTANCY_MP",
    units="Years",
    subscripts=["EDUCATIONAL_LEVEL_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_years_of_education_corresponding_to_each_level_for_schooling_life_expectancy_mp"
    },
)
def years_of_education_corresponding_to_each_level_for_schooling_life_expectancy_mp():
    return (
        _ext_constant_years_of_education_corresponding_to_each_level_for_schooling_life_expectancy_mp()
    )


_ext_constant_years_of_education_corresponding_to_each_level_for_schooling_life_expectancy_mp = ExtConstant(
    "model_parameters/society/society.xlsx",
    "developement_human_index",
    "YEARS_OF_EDUCATION_CORRESPONDING_TO_EACH_LEVEL_FOR_SCHOOLING_LIFE_EXPECTANCY_MP",
    {"EDUCATIONAL_LEVEL_I": _subscript_dict["EDUCATIONAL_LEVEL_I"]},
    _root,
    {"EDUCATIONAL_LEVEL_I": _subscript_dict["EDUCATIONAL_LEVEL_I"]},
    "_ext_constant_years_of_education_corresponding_to_each_level_for_schooling_life_expectancy_mp",
)
