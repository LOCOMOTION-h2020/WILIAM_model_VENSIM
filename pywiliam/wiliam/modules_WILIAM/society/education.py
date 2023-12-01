"""
Module society.education
Translated using PySD version 3.10.0
"""


@component.add(
    name="accumulated_public_expenditure_on_education_per_capita",
    units="Mdollars_2015/people",
    subscripts=["REGIONS_35_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_accumulated_public_expenditure_on_education_per_capita": 1},
    other_deps={
        "_integ_accumulated_public_expenditure_on_education_per_capita": {
            "initial": {
                "initial_accumulated_public_expenditure_on_education_per_capita": 1
            },
            "step": {
                "public_expenditure_on_education_per_capita": 1,
                "output_of_accumulated_expenditure_on_education_per_capita": 1,
            },
        }
    },
)
def accumulated_public_expenditure_on_education_per_capita():
    """
    Cumulative public education is taken as input to calculate the percentages of new students at each level of education.
    """
    return _integ_accumulated_public_expenditure_on_education_per_capita()


_integ_accumulated_public_expenditure_on_education_per_capita = Integ(
    lambda: public_expenditure_on_education_per_capita()
    - output_of_accumulated_expenditure_on_education_per_capita(),
    lambda: initial_accumulated_public_expenditure_on_education_per_capita(),
    "_integ_accumulated_public_expenditure_on_education_per_capita",
)


@component.add(
    name="decrease_in_workforce_per_eduacational_level",
    units="people/Year",
    subscripts=["REGIONS_35_I", "EDUCATIONAL_LEVEL_I", "SEX_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "deaths": 1,
        "population_by_cohorts_each_five_years": 1,
        "percentage_of_workforce_in_each_educational_level": 1,
    },
)
def decrease_in_workforce_per_eduacational_level():
    """
    The assumption is made that workers who die or retire are divided according to the same level of education in the country. (SUM(deaths[REGIONS_35_I,SEX_I,AGE_EDUCATION_I!])+decrease_in_workforce[REGIONS_35_I, SEX_I])*percentage_of_workforce_in_each_educational_level[REGIONS_35_I,EDUC ATIONAL_LEVEL_I ,SEX_I]/100
    """
    return (
        (
            sum(
                deaths()
                .loc[:, :, _subscript_dict["AGE_EDUCATION_I"]]
                .rename({"AGE_COHORTS_I": "AGE_EDUCATION_I!"}),
                dim=["AGE_EDUCATION_I!"],
            )
            + population_by_cohorts_each_five_years()
            .loc[:, :, "c60c64"]
            .reset_coords(drop=True)
            / 5
        )
        * percentage_of_workforce_in_each_educational_level().transpose(
            "REGIONS_35_I", "SEX_I", "EDUCATIONAL_LEVEL_I"
        )
        / 100
    ).transpose("REGIONS_35_I", "EDUCATIONAL_LEVEL_I", "SEX_I")


@component.add(
    name="Delayed_15_public_expenditure_on_education_per_capita",
    units="Mdollars_2015/(people*Year)",
    subscripts=["REGIONS_35_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_15_public_expenditure_on_education_per_capita": 1},
    other_deps={
        "_delayfixed_delayed_15_public_expenditure_on_education_per_capita": {
            "initial": {"public_expenditure_on_education_per_capita": 1},
            "step": {"public_expenditure_on_education_per_capita": 1},
        }
    },
)
def delayed_15_public_expenditure_on_education_per_capita():
    """
    The accumulated 15 years is an approximation of a person's years of education.
    """
    return _delayfixed_delayed_15_public_expenditure_on_education_per_capita()


_delayfixed_delayed_15_public_expenditure_on_education_per_capita = DelayFixed(
    lambda: public_expenditure_on_education_per_capita(),
    lambda: 15,
    lambda: public_expenditure_on_education_per_capita(),
    time_step,
    "_delayfixed_delayed_15_public_expenditure_on_education_per_capita",
)


@component.add(
    name="gender_parity_index",
    units="DMNL",
    subscripts=["REGIONS_35_I", "EDUCATIONAL_LEVEL_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_gender_parity_index": 1, "_integ_gender_parity_index_1": 1},
    other_deps={
        "_integ_gender_parity_index": {
            "initial": {"initial_gender_parity_index": 1},
            "step": {"variation_in_gender_parity_index": 1},
        },
        "_integ_gender_parity_index_1": {
            "initial": {"initial_gender_parity_index": 1},
            "step": {"variation_in_gender_parity_index": 1},
        },
    },
)
def gender_parity_index():
    """
    Socio-economic index designed to calculate the relative access of men and women to education. This index is released by UNESCO. In its simplest form, it is calculated as the quotient of the number of females by the number of males enrolled in a given stage of education (primary, secondary, etc.). A GPI equal to one signifies equality between males and females. A GPI less than one is an indication that gender parity favors males while a GPI greater than one indicates gender parity that favors females. The closer a GPI is to one, the closer a country is to achieving equality of access between males and females.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "EDUCATIONAL_LEVEL_I": _subscript_dict["EDUCATIONAL_LEVEL_I"],
        },
        ["REGIONS_35_I", "EDUCATIONAL_LEVEL_I"],
    )
    value.loc[:, ["HIGH_EDUCATION"]] = _integ_gender_parity_index().values
    value.loc[:, ["MEDIUM_EDUCATION"]] = _integ_gender_parity_index_1().values
    return value


_integ_gender_parity_index = Integ(
    lambda: variation_in_gender_parity_index()
    .loc[:, "HIGH_EDUCATION"]
    .reset_coords(drop=True)
    .expand_dims({"EDUCATIONAL_LEVEL_I": ["HIGH_EDUCATION"]}, 1),
    lambda: initial_gender_parity_index()
    .loc[:, "HIGH_EDUCATION"]
    .reset_coords(drop=True)
    .expand_dims({"EDUCATIONAL_LEVEL_I": ["HIGH_EDUCATION"]}, 1),
    "_integ_gender_parity_index",
)

_integ_gender_parity_index_1 = Integ(
    lambda: variation_in_gender_parity_index()
    .loc[:, "MEDIUM_EDUCATION"]
    .reset_coords(drop=True)
    .expand_dims({"EDUCATIONAL_LEVEL_I": ["MEDIUM_EDUCATION"]}, 1),
    lambda: initial_gender_parity_index()
    .loc[:, "MEDIUM_EDUCATION"]
    .reset_coords(drop=True)
    .expand_dims({"EDUCATIONAL_LEVEL_I": ["MEDIUM_EDUCATION"]}, 1),
    "_integ_gender_parity_index_1",
)


@component.add(
    name="increase_in_workforce",
    units="people/Year",
    subscripts=["REGIONS_35_I", "SEX_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"population_by_cohorts_each_five_years": 1},
)
def increase_in_workforce():
    """
    People who enter the labor market when leaving the age range between 20-24 years
    """
    return (
        population_by_cohorts_each_five_years()
        .loc[:, :, "c20c24"]
        .reset_coords(drop=True)
        / 5
    )


@component.add(
    name="increase_in_workforce_per_educational_level",
    units="people/Year",
    subscripts=["REGIONS_35_I", "EDUCATIONAL_LEVEL_I", "SEX_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "increase_in_workforce": 1,
        "percentage_of_new_workforce_in_each_educational_level": 1,
    },
)
def increase_in_workforce_per_educational_level():
    """
    Increase in the number of people entering the labour market after 25 years of age
    """
    return (
        increase_in_workforce()
        * percentage_of_new_workforce_in_each_educational_level().transpose(
            "REGIONS_35_I", "SEX_I", "EDUCATIONAL_LEVEL_I"
        )
        / 100
    ).transpose("REGIONS_35_I", "EDUCATIONAL_LEVEL_I", "SEX_I")


@component.add(
    name="initial_workforce",
    units="people",
    subscripts=["REGIONS_35_I", "SEX_I"],
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_initial_workforce": 1},
    other_deps={
        "_initial_initial_workforce": {
            "initial": {"population_by_cohorts_each_five_years": 1},
            "step": {},
        }
    },
)
def initial_workforce():
    """
    Initial workforce in the labour market
    """
    return _initial_initial_workforce()


_initial_initial_workforce = Initial(
    lambda: sum(
        population_by_cohorts_each_five_years()
        .loc[:, :, _subscript_dict["AGE_EDUCATION_I"]]
        .rename({"AGE_COHORTS_I": "AGE_EDUCATION_I!"}),
        dim=["AGE_EDUCATION_I!"],
    ),
    "_initial_initial_workforce",
)


@component.add(
    name="MAXIMUM_PERCENTAGE_OF_EDUCATION_LEVEL",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_maximum_percentage_of_education_level"},
)
def maximum_percentage_of_education_level():
    return _ext_constant_maximum_percentage_of_education_level()


_ext_constant_maximum_percentage_of_education_level = ExtConstant(
    "model_parameters/society/society.xlsx",
    "education",
    "MAXIMUM_PERCENTAGE_OF_EDUCATION_LEVEL_MP",
    {},
    _root,
    {},
    "_ext_constant_maximum_percentage_of_education_level",
)


@component.add(
    name="MINIMUM_PERCENTAGE_OF_HIGH_EDUCATION_LEVEL",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_minimum_percentage_of_high_education_level"
    },
)
def minimum_percentage_of_high_education_level():
    return _ext_constant_minimum_percentage_of_high_education_level()


_ext_constant_minimum_percentage_of_high_education_level = ExtConstant(
    "model_parameters/society/society.xlsx",
    "education",
    "MINIMUM_PERCENTAGE_OF_HIGH_EDUCATION_LEVEL_MP",
    {},
    _root,
    {},
    "_ext_constant_minimum_percentage_of_high_education_level",
)


@component.add(
    name="MINIMUM_PERCENTAGE_OF_MEDIUM_EDUCATION_LEVEL",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_minimum_percentage_of_medium_education_level"
    },
)
def minimum_percentage_of_medium_education_level():
    return _ext_constant_minimum_percentage_of_medium_education_level()


_ext_constant_minimum_percentage_of_medium_education_level = ExtConstant(
    "model_parameters/society/society.xlsx",
    "education",
    "MINIMUM_PERCENTAGE_OF_MEDIUM_EDUCATION_LEVEL_MP",
    {},
    _root,
    {},
    "_ext_constant_minimum_percentage_of_medium_education_level",
)


@component.add(
    name="net_immigration",
    subscripts=["REGIONS_35_I", "SEX_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"net_migrations": 1},
)
def net_immigration():
    return sum(
        net_migrations()
        .loc[:, :, _subscript_dict["AGE_EDUCATION_I"]]
        .rename({"AGE_COHORTS_I": "AGE_EDUCATION_I!"}),
        dim=["AGE_EDUCATION_I!"],
    )


@component.add(
    name="output_of_accumulated_expenditure_on_education_per_capita",
    units="Mdollars_2015/(people*Year)",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "accumulated_public_expenditure_on_education_per_capita": 1,
        "delayed_15_public_expenditure_on_education_per_capita": 1,
    },
)
def output_of_accumulated_expenditure_on_education_per_capita():
    """
    In the first years a part of the stock is taken instead of the expenditure of 15 years ago because it is not available in the historical data for all regions.
    """
    return if_then_else(
        time() < 2030,
        lambda: accumulated_public_expenditure_on_education_per_capita() / 15,
        lambda: delayed_15_public_expenditure_on_education_per_capita(),
    )


@component.add(
    name="percentage_of_new_workforce_in_each_educational_level",
    units="DMNL",
    subscripts=["REGIONS_35_I", "EDUCATIONAL_LEVEL_I", "SEX_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "maximum_percentage_of_education_level": 20,
        "minimum_percentage_of_high_education_level": 12,
        "beta_0_educational_level": 20,
        "accumulated_public_expenditure_on_education_per_capita": 20,
        "gender_parity_index": 30,
        "beta_1_educational_level": 20,
        "minimum_percentage_of_medium_education_level": 8,
    },
)
def percentage_of_new_workforce_in_each_educational_level():
    """
    The percentages change as the level of education increases or decreases until reaching certain maximums or minimums. The maximums and minimums are taken by giving a certain margin to the maximum and minimum percentages observed in the historical data.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "EDUCATIONAL_LEVEL_I": _subscript_dict["EDUCATIONAL_LEVEL_I"],
            "SEX_I": _subscript_dict["SEX_I"],
        },
        ["REGIONS_35_I", "EDUCATIONAL_LEVEL_I", "SEX_I"],
    )
    value.loc[:, ["HIGH_EDUCATION"], ["FEMALE"]] = (
        np.minimum(
            maximum_percentage_of_education_level(),
            np.maximum(
                minimum_percentage_of_high_education_level(),
                2
                * zidz(
                    beta_0_educational_level()
                    .loc[:, "HIGH_EDUCATION"]
                    .reset_coords(drop=True)
                    + beta_1_educational_level()
                    .loc[:, "HIGH_EDUCATION"]
                    .reset_coords(drop=True)
                    * accumulated_public_expenditure_on_education_per_capita(),
                    1
                    + 1
                    / gender_parity_index()
                    .loc[:, "HIGH_EDUCATION"]
                    .reset_coords(drop=True),
                ),
            ),
        )
        .expand_dims({"EDUCATIONAL_LEVEL_I": ["HIGH_EDUCATION"]}, 1)
        .expand_dims({"SEX_I": ["FEMALE"]}, 2)
        .values
    )
    value.loc[:, ["HIGH_EDUCATION"], ["MALE"]] = (
        np.minimum(
            maximum_percentage_of_education_level(),
            np.maximum(
                minimum_percentage_of_high_education_level(),
                2
                * zidz(
                    beta_0_educational_level()
                    .loc[:, "HIGH_EDUCATION"]
                    .reset_coords(drop=True)
                    + beta_1_educational_level()
                    .loc[:, "HIGH_EDUCATION"]
                    .reset_coords(drop=True)
                    * accumulated_public_expenditure_on_education_per_capita(),
                    1
                    + 1
                    / gender_parity_index()
                    .loc[:, "HIGH_EDUCATION"]
                    .reset_coords(drop=True),
                )
                / gender_parity_index()
                .loc[:, "HIGH_EDUCATION"]
                .reset_coords(drop=True),
            ),
        )
        .expand_dims({"EDUCATIONAL_LEVEL_I": ["HIGH_EDUCATION"]}, 1)
        .expand_dims({"SEX_I": ["MALE"]}, 2)
        .values
    )
    value.loc[:, ["MEDIUM_EDUCATION"], ["FEMALE"]] = (
        if_then_else(
            np.minimum(
                maximum_percentage_of_education_level(),
                np.maximum(
                    minimum_percentage_of_high_education_level(),
                    2
                    * zidz(
                        beta_0_educational_level()
                        .loc[:, "HIGH_EDUCATION"]
                        .reset_coords(drop=True)
                        + beta_1_educational_level()
                        .loc[:, "HIGH_EDUCATION"]
                        .reset_coords(drop=True)
                        * accumulated_public_expenditure_on_education_per_capita(),
                        1
                        + 1
                        / gender_parity_index()
                        .loc[:, "HIGH_EDUCATION"]
                        .reset_coords(drop=True),
                    ),
                ),
            )
            + np.minimum(
                maximum_percentage_of_education_level(),
                np.maximum(
                    minimum_percentage_of_medium_education_level(),
                    2
                    * zidz(
                        beta_0_educational_level()
                        .loc[:, "MEDIUM_EDUCATION"]
                        .reset_coords(drop=True)
                        + beta_1_educational_level()
                        .loc[:, "MEDIUM_EDUCATION"]
                        .reset_coords(drop=True)
                        * accumulated_public_expenditure_on_education_per_capita(),
                        1
                        + 1
                        / gender_parity_index()
                        .loc[:, "MEDIUM_EDUCATION"]
                        .reset_coords(drop=True),
                    ),
                ),
            )
            > 95,
            lambda: 95
            - np.minimum(
                maximum_percentage_of_education_level(),
                np.maximum(
                    minimum_percentage_of_high_education_level(),
                    2
                    * zidz(
                        beta_0_educational_level()
                        .loc[:, "HIGH_EDUCATION"]
                        .reset_coords(drop=True)
                        + beta_1_educational_level()
                        .loc[:, "HIGH_EDUCATION"]
                        .reset_coords(drop=True)
                        * accumulated_public_expenditure_on_education_per_capita(),
                        1
                        + 1
                        / gender_parity_index()
                        .loc[:, "HIGH_EDUCATION"]
                        .reset_coords(drop=True),
                    ),
                ),
            ),
            lambda: np.minimum(
                maximum_percentage_of_education_level(),
                np.maximum(
                    minimum_percentage_of_medium_education_level(),
                    2
                    * zidz(
                        beta_0_educational_level()
                        .loc[:, "MEDIUM_EDUCATION"]
                        .reset_coords(drop=True)
                        + beta_1_educational_level()
                        .loc[:, "MEDIUM_EDUCATION"]
                        .reset_coords(drop=True)
                        * accumulated_public_expenditure_on_education_per_capita(),
                        1
                        + 1
                        / gender_parity_index()
                        .loc[:, "MEDIUM_EDUCATION"]
                        .reset_coords(drop=True),
                    ),
                ),
            ),
        )
        .expand_dims({"EDUCATIONAL_LEVEL_I": ["MEDIUM_EDUCATION"]}, 1)
        .expand_dims({"SEX_I": ["FEMALE"]}, 2)
        .values
    )
    value.loc[:, ["MEDIUM_EDUCATION"], ["MALE"]] = (
        if_then_else(
            np.minimum(
                maximum_percentage_of_education_level(),
                np.maximum(
                    minimum_percentage_of_high_education_level(),
                    2
                    * zidz(
                        beta_0_educational_level()
                        .loc[:, "HIGH_EDUCATION"]
                        .reset_coords(drop=True)
                        + beta_1_educational_level()
                        .loc[:, "HIGH_EDUCATION"]
                        .reset_coords(drop=True)
                        * accumulated_public_expenditure_on_education_per_capita(),
                        1
                        + 1
                        / gender_parity_index()
                        .loc[:, "HIGH_EDUCATION"]
                        .reset_coords(drop=True),
                    )
                    / gender_parity_index()
                    .loc[:, "HIGH_EDUCATION"]
                    .reset_coords(drop=True),
                ),
            )
            + np.minimum(
                maximum_percentage_of_education_level(),
                np.maximum(
                    minimum_percentage_of_medium_education_level(),
                    2
                    * zidz(
                        beta_0_educational_level()
                        .loc[:, "MEDIUM_EDUCATION"]
                        .reset_coords(drop=True)
                        + beta_1_educational_level()
                        .loc[:, "MEDIUM_EDUCATION"]
                        .reset_coords(drop=True)
                        * accumulated_public_expenditure_on_education_per_capita(),
                        1
                        + 1
                        / gender_parity_index()
                        .loc[:, "MEDIUM_EDUCATION"]
                        .reset_coords(drop=True),
                    )
                    / gender_parity_index()
                    .loc[:, "MEDIUM_EDUCATION"]
                    .reset_coords(drop=True),
                ),
            )
            > 95,
            lambda: 95
            - np.minimum(
                maximum_percentage_of_education_level(),
                np.maximum(
                    minimum_percentage_of_high_education_level(),
                    2
                    * zidz(
                        beta_0_educational_level()
                        .loc[:, "HIGH_EDUCATION"]
                        .reset_coords(drop=True)
                        + beta_1_educational_level()
                        .loc[:, "HIGH_EDUCATION"]
                        .reset_coords(drop=True)
                        * accumulated_public_expenditure_on_education_per_capita(),
                        1
                        + 1
                        / gender_parity_index()
                        .loc[:, "HIGH_EDUCATION"]
                        .reset_coords(drop=True),
                    )
                    / gender_parity_index()
                    .loc[:, "HIGH_EDUCATION"]
                    .reset_coords(drop=True),
                ),
            ),
            lambda: np.minimum(
                maximum_percentage_of_education_level(),
                np.maximum(
                    minimum_percentage_of_medium_education_level(),
                    2
                    * zidz(
                        beta_0_educational_level()
                        .loc[:, "MEDIUM_EDUCATION"]
                        .reset_coords(drop=True)
                        + beta_1_educational_level()
                        .loc[:, "MEDIUM_EDUCATION"]
                        .reset_coords(drop=True)
                        * accumulated_public_expenditure_on_education_per_capita(),
                        1
                        + 1
                        / gender_parity_index()
                        .loc[:, "MEDIUM_EDUCATION"]
                        .reset_coords(drop=True),
                    )
                    / gender_parity_index()
                    .loc[:, "MEDIUM_EDUCATION"]
                    .reset_coords(drop=True),
                ),
            ),
        )
        .expand_dims({"EDUCATIONAL_LEVEL_I": ["MEDIUM_EDUCATION"]}, 1)
        .expand_dims({"SEX_I": ["MALE"]}, 2)
        .values
    )
    value.loc[:, ["LOW_EDUCATION"], ["FEMALE"]] = (
        (
            100
            - np.minimum(
                maximum_percentage_of_education_level(),
                np.maximum(
                    minimum_percentage_of_high_education_level(),
                    2
                    * zidz(
                        beta_0_educational_level()
                        .loc[:, "HIGH_EDUCATION"]
                        .reset_coords(drop=True)
                        + beta_1_educational_level()
                        .loc[:, "HIGH_EDUCATION"]
                        .reset_coords(drop=True)
                        * accumulated_public_expenditure_on_education_per_capita(),
                        1
                        + 1
                        / gender_parity_index()
                        .loc[:, "HIGH_EDUCATION"]
                        .reset_coords(drop=True),
                    ),
                ),
            )
            - if_then_else(
                np.minimum(
                    maximum_percentage_of_education_level(),
                    np.maximum(
                        minimum_percentage_of_high_education_level(),
                        2
                        * zidz(
                            beta_0_educational_level()
                            .loc[:, "HIGH_EDUCATION"]
                            .reset_coords(drop=True)
                            + beta_1_educational_level()
                            .loc[:, "HIGH_EDUCATION"]
                            .reset_coords(drop=True)
                            * accumulated_public_expenditure_on_education_per_capita(),
                            1
                            + 1
                            / gender_parity_index()
                            .loc[:, "HIGH_EDUCATION"]
                            .reset_coords(drop=True),
                        ),
                    ),
                )
                + np.minimum(
                    maximum_percentage_of_education_level(),
                    np.maximum(
                        minimum_percentage_of_medium_education_level(),
                        2
                        * zidz(
                            beta_0_educational_level()
                            .loc[:, "MEDIUM_EDUCATION"]
                            .reset_coords(drop=True)
                            + beta_1_educational_level()
                            .loc[:, "MEDIUM_EDUCATION"]
                            .reset_coords(drop=True)
                            * accumulated_public_expenditure_on_education_per_capita(),
                            1
                            + 1
                            / gender_parity_index()
                            .loc[:, "MEDIUM_EDUCATION"]
                            .reset_coords(drop=True),
                        ),
                    ),
                )
                > 95,
                lambda: 95
                - np.minimum(
                    maximum_percentage_of_education_level(),
                    np.maximum(
                        minimum_percentage_of_high_education_level(),
                        2
                        * zidz(
                            beta_0_educational_level()
                            .loc[:, "HIGH_EDUCATION"]
                            .reset_coords(drop=True)
                            + beta_1_educational_level()
                            .loc[:, "HIGH_EDUCATION"]
                            .reset_coords(drop=True)
                            * accumulated_public_expenditure_on_education_per_capita(),
                            1
                            + 1
                            / gender_parity_index()
                            .loc[:, "HIGH_EDUCATION"]
                            .reset_coords(drop=True),
                        ),
                    ),
                ),
                lambda: np.minimum(
                    maximum_percentage_of_education_level(),
                    np.maximum(
                        minimum_percentage_of_medium_education_level(),
                        2
                        * zidz(
                            beta_0_educational_level()
                            .loc[:, "MEDIUM_EDUCATION"]
                            .reset_coords(drop=True)
                            + beta_1_educational_level()
                            .loc[:, "MEDIUM_EDUCATION"]
                            .reset_coords(drop=True)
                            * accumulated_public_expenditure_on_education_per_capita(),
                            1
                            + 1
                            / gender_parity_index()
                            .loc[:, "MEDIUM_EDUCATION"]
                            .reset_coords(drop=True),
                        ),
                    ),
                ),
            )
        )
        .expand_dims({"EDUCATIONAL_LEVEL_I": ["LOW_EDUCATION"]}, 1)
        .expand_dims({"SEX_I": ["FEMALE"]}, 2)
        .values
    )
    value.loc[:, ["LOW_EDUCATION"], ["MALE"]] = (
        (
            100
            - np.minimum(
                maximum_percentage_of_education_level(),
                np.maximum(
                    minimum_percentage_of_high_education_level(),
                    2
                    * zidz(
                        beta_0_educational_level()
                        .loc[:, "HIGH_EDUCATION"]
                        .reset_coords(drop=True)
                        + beta_1_educational_level()
                        .loc[:, "HIGH_EDUCATION"]
                        .reset_coords(drop=True)
                        * accumulated_public_expenditure_on_education_per_capita(),
                        1
                        + 1
                        / gender_parity_index()
                        .loc[:, "HIGH_EDUCATION"]
                        .reset_coords(drop=True),
                    )
                    / gender_parity_index()
                    .loc[:, "HIGH_EDUCATION"]
                    .reset_coords(drop=True),
                ),
            )
            - if_then_else(
                np.minimum(
                    maximum_percentage_of_education_level(),
                    np.maximum(
                        minimum_percentage_of_high_education_level(),
                        2
                        * zidz(
                            beta_0_educational_level()
                            .loc[:, "HIGH_EDUCATION"]
                            .reset_coords(drop=True)
                            + beta_1_educational_level()
                            .loc[:, "HIGH_EDUCATION"]
                            .reset_coords(drop=True)
                            * accumulated_public_expenditure_on_education_per_capita(),
                            1
                            + 1
                            / gender_parity_index()
                            .loc[:, "HIGH_EDUCATION"]
                            .reset_coords(drop=True),
                        )
                        / gender_parity_index()
                        .loc[:, "HIGH_EDUCATION"]
                        .reset_coords(drop=True),
                    ),
                )
                + np.minimum(
                    maximum_percentage_of_education_level(),
                    np.maximum(
                        minimum_percentage_of_medium_education_level(),
                        2
                        * zidz(
                            beta_0_educational_level()
                            .loc[:, "MEDIUM_EDUCATION"]
                            .reset_coords(drop=True)
                            + beta_1_educational_level()
                            .loc[:, "MEDIUM_EDUCATION"]
                            .reset_coords(drop=True)
                            * accumulated_public_expenditure_on_education_per_capita(),
                            1
                            + 1
                            / gender_parity_index()
                            .loc[:, "MEDIUM_EDUCATION"]
                            .reset_coords(drop=True),
                        )
                        / gender_parity_index()
                        .loc[:, "MEDIUM_EDUCATION"]
                        .reset_coords(drop=True),
                    ),
                )
                > 95,
                lambda: 95
                - np.minimum(
                    maximum_percentage_of_education_level(),
                    np.maximum(
                        minimum_percentage_of_high_education_level(),
                        2
                        * zidz(
                            beta_0_educational_level()
                            .loc[:, "HIGH_EDUCATION"]
                            .reset_coords(drop=True)
                            + beta_1_educational_level()
                            .loc[:, "HIGH_EDUCATION"]
                            .reset_coords(drop=True)
                            * accumulated_public_expenditure_on_education_per_capita(),
                            1
                            + 1
                            / gender_parity_index()
                            .loc[:, "HIGH_EDUCATION"]
                            .reset_coords(drop=True),
                        )
                        / gender_parity_index()
                        .loc[:, "HIGH_EDUCATION"]
                        .reset_coords(drop=True),
                    ),
                ),
                lambda: np.minimum(
                    maximum_percentage_of_education_level(),
                    np.maximum(
                        minimum_percentage_of_medium_education_level(),
                        2
                        * zidz(
                            beta_0_educational_level()
                            .loc[:, "MEDIUM_EDUCATION"]
                            .reset_coords(drop=True)
                            + beta_1_educational_level()
                            .loc[:, "MEDIUM_EDUCATION"]
                            .reset_coords(drop=True)
                            * accumulated_public_expenditure_on_education_per_capita(),
                            1
                            + 1
                            / gender_parity_index()
                            .loc[:, "MEDIUM_EDUCATION"]
                            .reset_coords(drop=True),
                        )
                        / gender_parity_index()
                        .loc[:, "MEDIUM_EDUCATION"]
                        .reset_coords(drop=True),
                    ),
                ),
            )
        )
        .expand_dims({"EDUCATIONAL_LEVEL_I": ["LOW_EDUCATION"]}, 1)
        .expand_dims({"SEX_I": ["MALE"]}, 2)
        .values
    )
    return value


@component.add(
    name="percentage_of_workforce_in_each_educational_level",
    units="DMNL",
    subscripts=["REGIONS_35_I", "EDUCATIONAL_LEVEL_I", "SEX_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"workforce_per_educational_level": 6},
)
def percentage_of_workforce_in_each_educational_level():
    """
    Percentage of workforce by educational attainment level
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "EDUCATIONAL_LEVEL_I": _subscript_dict["EDUCATIONAL_LEVEL_I"],
            "SEX_I": _subscript_dict["SEX_I"],
        },
        ["REGIONS_35_I", "EDUCATIONAL_LEVEL_I", "SEX_I"],
    )
    value.loc[:, ["HIGH_EDUCATION"], :] = (
        (
            zidz(
                workforce_per_educational_level()
                .loc[:, "HIGH_EDUCATION", :]
                .reset_coords(drop=True),
                sum(
                    workforce_per_educational_level().rename(
                        {"EDUCATIONAL_LEVEL_I": "EDUCATIONAL_LEVEL_I!"}
                    ),
                    dim=["EDUCATIONAL_LEVEL_I!"],
                ),
            )
            * 100
        )
        .expand_dims({"EDUCATIONAL_LEVEL_I": ["HIGH_EDUCATION"]}, 1)
        .values
    )
    value.loc[:, ["MEDIUM_EDUCATION"], :] = (
        (
            zidz(
                workforce_per_educational_level()
                .loc[:, "MEDIUM_EDUCATION", :]
                .reset_coords(drop=True),
                sum(
                    workforce_per_educational_level().rename(
                        {"EDUCATIONAL_LEVEL_I": "EDUCATIONAL_LEVEL_I!"}
                    ),
                    dim=["EDUCATIONAL_LEVEL_I!"],
                ),
            )
            * 100
        )
        .expand_dims({"EDUCATIONAL_LEVEL_I": ["MEDIUM_EDUCATION"]}, 1)
        .values
    )
    value.loc[:, ["LOW_EDUCATION"], :] = (
        (
            zidz(
                workforce_per_educational_level()
                .loc[:, "LOW_EDUCATION", :]
                .reset_coords(drop=True),
                sum(
                    workforce_per_educational_level().rename(
                        {"EDUCATIONAL_LEVEL_I": "EDUCATIONAL_LEVEL_I!"}
                    ),
                    dim=["EDUCATIONAL_LEVEL_I!"],
                ),
            )
            * 100
        )
        .expand_dims({"EDUCATIONAL_LEVEL_I": ["LOW_EDUCATION"]}, 1)
        .values
    )
    return value


@component.add(
    name="public_expenditure_on_education_per_capita",
    units="Mdollars_2015/(people*Year)",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "government_consumption_purchaser_prices": 1,
        "price_output": 1,
        "population_35_regions": 1,
        "matrix_unit_prefixes": 1,
    },
)
def public_expenditure_on_education_per_capita():
    """
    Public spending on education is taken instead of total spending (public and private) because the availability of historical data for the former is greater. The historical data have been necessary to calculate the parameters of the function of percentages of new workers by level of education.
    """
    return zidz(
        government_consumption_purchaser_prices()
        .loc[:, "EDUCATION"]
        .reset_coords(drop=True)
        * 100
        / price_output().loc[:, "EDUCATION"].reset_coords(drop=True),
        population_35_regions(),
    ) * float(matrix_unit_prefixes().loc["mega", "BASE_UNIT"])


@component.add(
    name="regional_average_schooling_time",
    units="Years",
    subscripts=["REGIONS_35_I", "SEX_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "workforce_per_educational_level": 4,
        "years_of_education_corresponding_to_each_level_for_means_years_of_schooling_mp": 3,
    },
)
def regional_average_schooling_time():
    """
    Average schooling time for the whole educational system
    """
    return (
        workforce_per_educational_level()
        .loc[:, "LOW_EDUCATION", :]
        .reset_coords(drop=True)
        * float(
            years_of_education_corresponding_to_each_level_for_means_years_of_schooling_mp().loc[
                "LOW_EDUCATION"
            ]
        )
        + workforce_per_educational_level()
        .loc[:, "MEDIUM_EDUCATION", :]
        .reset_coords(drop=True)
        * float(
            years_of_education_corresponding_to_each_level_for_means_years_of_schooling_mp().loc[
                "MEDIUM_EDUCATION"
            ]
        )
        + workforce_per_educational_level()
        .loc[:, "HIGH_EDUCATION", :]
        .reset_coords(drop=True)
        * float(
            years_of_education_corresponding_to_each_level_for_means_years_of_schooling_mp().loc[
                "HIGH_EDUCATION"
            ]
        )
    ) / sum(
        workforce_per_educational_level().rename(
            {"EDUCATIONAL_LEVEL_I": "EDUCATIONAL_LEVEL_I!"}
        ),
        dim=["EDUCATIONAL_LEVEL_I!"],
    )


@component.add(
    name="SWITCH_SOCIETY",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_society"},
)
def switch_society():
    """
    This switch can take two values: 0: the (sub)module runs isolated from the rest of WILIAM, replacing inter(sub)module variables with exogenous parameters. 1: the (sub)module runs integrated with the rest of WILIAM.
    """
    return _ext_constant_switch_society()


_ext_constant_switch_society = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_SOCIETY",
    {},
    _root,
    {},
    "_ext_constant_switch_society",
)


@component.add(
    name="variation_in_gender_parity_index",
    units="1/Year",
    subscripts=["REGIONS_35_I", "EDUCATIONAL_LEVEL_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_model_explorer": 2,
        "model_explorer_final_gender_parity_index": 2,
        "initial_gender_parity_index": 2,
        "switch_policy_gender_parity_index_sp": 2,
        "final_gender_parity_index_sp": 2,
        "year_initial_gender_parity_index_sp": 4,
        "year_final_gender_parity_index_sp": 4,
        "time": 4,
    },
)
def variation_in_gender_parity_index():
    """
    A value below one indicates differences in favour of boys, while a value close to one indicates that parity has been more or less achieved
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
            switch_model_explorer() == 1,
            lambda: model_explorer_final_gender_parity_index()
            .loc[:, "HIGH_EDUCATION"]
            .reset_coords(drop=True),
            lambda: if_then_else(
                switch_policy_gender_parity_index_sp() == 0,
                lambda: xr.DataArray(
                    0,
                    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
                    ["REGIONS_35_I"],
                ),
                lambda: if_then_else(
                    time() < year_initial_gender_parity_index_sp(),
                    lambda: xr.DataArray(
                        0,
                        {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
                        ["REGIONS_35_I"],
                    ),
                    lambda: if_then_else(
                        time() < year_final_gender_parity_index_sp(),
                        lambda: zidz(
                            final_gender_parity_index_sp()
                            .loc[:, "HIGH_EDUCATION"]
                            .reset_coords(drop=True)
                            - initial_gender_parity_index()
                            .loc[:, "HIGH_EDUCATION"]
                            .reset_coords(drop=True),
                            year_final_gender_parity_index_sp()
                            - year_initial_gender_parity_index_sp(),
                        ),
                        lambda: xr.DataArray(
                            0,
                            {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
                            ["REGIONS_35_I"],
                        ),
                    ),
                ),
            ),
        )
        .expand_dims({"EDUCATIONAL_LEVEL_I": ["HIGH_EDUCATION"]}, 1)
        .values
    )
    value.loc[:, ["MEDIUM_EDUCATION"]] = (
        if_then_else(
            switch_model_explorer() == 1,
            lambda: model_explorer_final_gender_parity_index()
            .loc[:, "MEDIUM_EDUCATION"]
            .reset_coords(drop=True),
            lambda: if_then_else(
                switch_policy_gender_parity_index_sp() == 0,
                lambda: xr.DataArray(
                    0,
                    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
                    ["REGIONS_35_I"],
                ),
                lambda: if_then_else(
                    time() < year_initial_gender_parity_index_sp(),
                    lambda: xr.DataArray(
                        0,
                        {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
                        ["REGIONS_35_I"],
                    ),
                    lambda: if_then_else(
                        time() < year_final_gender_parity_index_sp(),
                        lambda: zidz(
                            final_gender_parity_index_sp()
                            .loc[:, "MEDIUM_EDUCATION"]
                            .reset_coords(drop=True)
                            - initial_gender_parity_index()
                            .loc[:, "MEDIUM_EDUCATION"]
                            .reset_coords(drop=True),
                            year_final_gender_parity_index_sp()
                            - year_initial_gender_parity_index_sp(),
                        ),
                        lambda: xr.DataArray(
                            0,
                            {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
                            ["REGIONS_35_I"],
                        ),
                    ),
                ),
            ),
        )
        .expand_dims({"EDUCATIONAL_LEVEL_I": ["MEDIUM_EDUCATION"]}, 1)
        .values
    )
    return value


@component.add(
    name="variation_in_workforce_per_educational_level_by_migrations",
    units="people/Year",
    subscripts=["REGIONS_35_I", "EDUCATIONAL_LEVEL_I", "SEX_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "net_immigration": 1,
        "percentage_of_workforce_in_each_educational_level": 1,
    },
)
def variation_in_workforce_per_educational_level_by_migrations():
    """
    The assumption is made that migrants are divided according to the same educational level in the country. SUM(net_immigration[REGIONS_35_I,AGE_EDUCATION_I!,SEX_I])*percentage_of_workforce_in_ each_educational_level[REGIONS_35_I,EDUCATIONAL_LEVEL_I ,SEX_I]/100
    """
    return (
        net_immigration()
        * percentage_of_workforce_in_each_educational_level().transpose(
            "REGIONS_35_I", "SEX_I", "EDUCATIONAL_LEVEL_I"
        )
        / 100
    ).transpose("REGIONS_35_I", "EDUCATIONAL_LEVEL_I", "SEX_I")


@component.add(
    name="workforce_per_educational_level",
    units="people",
    subscripts=["REGIONS_35_I", "EDUCATIONAL_LEVEL_I", "SEX_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_workforce_per_educational_level": 1},
    other_deps={
        "_integ_workforce_per_educational_level": {
            "initial": {
                "initial_share_of_workforce_in_each_educational_level": 1,
                "initial_workforce": 1,
            },
            "step": {
                "increase_in_workforce_per_educational_level": 1,
                "decrease_in_workforce_per_eduacational_level": 1,
                "variation_in_workforce_per_educational_level_by_migrations": 1,
            },
        }
    },
)
def workforce_per_educational_level():
    """
    The labor force has as an inflow the people who pass a certain age and as an outflow the people of working age who die and those who reach retirement age. The migration flow can be positive or negative.
    """
    return _integ_workforce_per_educational_level()


_integ_workforce_per_educational_level = Integ(
    lambda: increase_in_workforce_per_educational_level()
    - decrease_in_workforce_per_eduacational_level()
    + variation_in_workforce_per_educational_level_by_migrations(),
    lambda: initial_share_of_workforce_in_each_educational_level()
    * initial_workforce(),
    "_integ_workforce_per_educational_level",
)
