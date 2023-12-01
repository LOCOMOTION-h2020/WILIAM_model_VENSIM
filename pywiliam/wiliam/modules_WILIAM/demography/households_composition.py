"""
Module demography.households_composition
Translated using PySD version 3.10.0
"""


@component.add(
    name="average_people_per_household_nonEU_regions",
    units="person/household",
    subscripts=["REGIONS_8_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_average_people_per_household_noneu_regions": 1},
    other_deps={
        "_integ_average_people_per_household_noneu_regions": {
            "initial": {"initial_2015_average_people_per_household_noneu_regions": 1},
            "step": {"variation_average_people_per_household_noneu_regions": 1},
        }
    },
)
def average_people_per_household_noneu_regions():
    """
    Average people per household for non EU regions.
    """
    return _integ_average_people_per_household_noneu_regions()


_integ_average_people_per_household_noneu_regions = Integ(
    lambda: variation_average_people_per_household_noneu_regions(),
    lambda: initial_2015_average_people_per_household_noneu_regions(),
    "_integ_average_people_per_household_noneu_regions",
)


@component.add(
    name="EU_households_per_100_people",
    units="households/person",
    subscripts=["REGIONS_EU27_I", "HOUSEHOLDS_DEMOGRAPHY_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_eu_households_per_100_people": 1},
    other_deps={
        "_integ_eu_households_per_100_people": {
            "initial": {"initial_ratio_eu_households_per_100_people": 1},
            "step": {"variation_eu_households_per_100_people": 1},
        }
    },
)
def eu_households_per_100_people():
    """
    Dynamic ratio of European households per capita. Households per 100 people
    """
    return _integ_eu_households_per_100_people()


_integ_eu_households_per_100_people = Integ(
    lambda: variation_eu_households_per_100_people(),
    lambda: initial_ratio_eu_households_per_100_people(),
    "_integ_eu_households_per_100_people",
)


@component.add(
    name="INITIAL_2015_AVERAGE_PEOPLE_PER_HOUSEHOLD_NONEU_REGIONS",
    units="people/household",
    subscripts=["REGIONS_8_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"population_2015_regions_8": 1, "base_number_of_households": 1},
)
def initial_2015_average_people_per_household_noneu_regions():
    """
    Average people per household in the year 2015 for non EU regions.
    """
    return population_2015_regions_8() / sum(
        base_number_of_households()
        .loc[_subscript_dict["REGIONS_8_I"], :]
        .rename({"REGIONS_35_I": "REGIONS_8_I", "HOUSEHOLDS_I": "HOUSEHOLDS_I!"}),
        dim=["HOUSEHOLDS_I!"],
    )


@component.add(
    name="number_households_by_type_EU27",
    units="households",
    subscripts=["REGIONS_EU27_I", "HOUSEHOLDS_DEMOGRAPHY_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"eu_households_per_100_people": 1, "population_35_regions": 1},
)
def number_households_by_type_eu27():
    """
    Extrapolation of the number of households based on the regional population. The value "100" is used to translate from ratios (originally in households per 100 people) into households.
    """
    return np.maximum(
        eu_households_per_100_people()
        * (
            population_35_regions()
            .loc[_subscript_dict["REGIONS_EU27_I"]]
            .rename({"REGIONS_35_I": "REGIONS_EU27_I"})
            / 100
        ),
        1,
    )


@component.add(
    name="number_households_nonEU",
    units="households",
    subscripts=["REGIONS_8_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "population_35_regions": 1,
        "average_people_per_household_noneu_regions": 1,
    },
)
def number_households_noneu():
    return (
        population_35_regions()
        .loc[_subscript_dict["REGIONS_8_I"]]
        .rename({"REGIONS_35_I": "REGIONS_8_I"})
        / average_people_per_household_noneu_regions()
    )


@component.add(
    name="percentage_population_rural_areas",
    units="percent",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "a_rural_regression": 2,
        "time": 2,
        "b_rural_regression": 2,
        "minimum_population_rural": 2,
    },
)
def percentage_population_rural_areas():
    """
    Linear regression model (y = a * x + b) to estimate the percentage of population in rural areas. A minimum percentage was included as constant to avoid unreal numbers.
    """
    return if_then_else(
        a_rural_regression() * time() + b_rural_regression()
        < minimum_population_rural(),
        lambda: xr.DataArray(
            minimum_population_rural(),
            {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
            ["REGIONS_9_I"],
        ),
        lambda: a_rural_regression() * time() + b_rural_regression(),
    )


@component.add(
    name="POPULATION_2015_REGIONS_8",
    units="people",
    subscripts=["REGIONS_8_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_population_2015_regions_8"},
)
def population_2015_regions_8():
    """
    Population in the year 2015 for the non EU regions.
    """
    return _ext_constant_population_2015_regions_8()


_ext_constant_population_2015_regions_8 = ExtConstant(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "POPULATION_2015_REGIONS_8*",
    {"REGIONS_8_I": _subscript_dict["REGIONS_8_I"]},
    _root,
    {"REGIONS_8_I": _subscript_dict["REGIONS_8_I"]},
    "_ext_constant_population_2015_regions_8",
)


@component.add(
    name="SELECT_VARIATION_OF_AVERAGE_PEOPLE_PER_HOUSEHOLD_IN_NON_EU_REGIONS_SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_select_variation_of_average_people_per_household_in_non_eu_regions_sp"
    },
)
def select_variation_of_average_people_per_household_in_non_eu_regions_sp():
    """
    Select scenario parameter for seting the average people per household in the non EU regions.
    """
    return (
        _ext_constant_select_variation_of_average_people_per_household_in_non_eu_regions_sp()
    )


_ext_constant_select_variation_of_average_people_per_household_in_non_eu_regions_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "demography",
    "SELECT_VARIATION_OF_AVERAGE_PEOPLE_PER_HOUSEHOLD_IN_NON_EU_REGIONS_SP",
    {},
    _root,
    {},
    "_ext_constant_select_variation_of_average_people_per_household_in_non_eu_regions_sp",
)


@component.add(
    name="variation_average_people_per_household_nonEU_regions",
    units="people/(household*Year)",
    subscripts=["REGIONS_8_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 3,
        "average_people_per_household_non_eu_regions_timeseries_target_sp": 2,
        "select_variation_of_average_people_per_household_in_non_eu_regions_sp": 2,
    },
)
def variation_average_people_per_household_noneu_regions():
    """
    Variation over time of average number of people per household for non EU regions.
    """
    return if_then_else(
        time() < 2015,
        lambda: xr.DataArray(
            0, {"REGIONS_8_I": _subscript_dict["REGIONS_8_I"]}, ["REGIONS_8_I"]
        ),
        lambda: if_then_else(
            select_variation_of_average_people_per_household_in_non_eu_regions_sp()
            == 0,
            lambda: xr.DataArray(
                0, {"REGIONS_8_I": _subscript_dict["REGIONS_8_I"]}, ["REGIONS_8_I"]
            ),
            lambda: if_then_else(
                select_variation_of_average_people_per_household_in_non_eu_regions_sp()
                == 1,
                lambda: average_people_per_household_non_eu_regions_timeseries_target_sp(
                    time() + 1
                )
                - average_people_per_household_non_eu_regions_timeseries_target_sp(
                    time()
                ),
                lambda: xr.DataArray(
                    0, {"REGIONS_8_I": _subscript_dict["REGIONS_8_I"]}, ["REGIONS_8_I"]
                ),
            ),
        ),
    )


@component.add(
    name="variation_EU_households_per_100_people",
    units="households/(person*Year)",
    subscripts=["REGIONS_EU27_I", "HOUSEHOLDS_DEMOGRAPHY_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_slope_evolution_of_eu27_households_composition_sp": 3,
        "mean_variation_eu_households_per_100_people": 1,
        "min_variation_eu_households_per_100_people": 1,
        "max_variation_eu_households_per_100_people": 1,
        "eu_households_per_100_people": 1,
    },
)
def variation_eu_households_per_100_people():
    """
    Slope in the ratio of households composition. Units: households per 100 people
    """
    return np.maximum(
        if_then_else(
            select_slope_evolution_of_eu27_households_composition_sp() == 1,
            lambda: mean_variation_eu_households_per_100_people(),
            lambda: if_then_else(
                select_slope_evolution_of_eu27_households_composition_sp() == 2,
                lambda: min_variation_eu_households_per_100_people(),
                lambda: if_then_else(
                    select_slope_evolution_of_eu27_households_composition_sp() == 3,
                    lambda: max_variation_eu_households_per_100_people(),
                    lambda: xr.DataArray(
                        0,
                        {
                            "REGIONS_EU27_I": _subscript_dict["REGIONS_EU27_I"],
                            "HOUSEHOLDS_DEMOGRAPHY_I": _subscript_dict[
                                "HOUSEHOLDS_DEMOGRAPHY_I"
                            ],
                        },
                        ["REGIONS_EU27_I", "HOUSEHOLDS_DEMOGRAPHY_I"],
                    ),
                ),
            ),
        ),
        -eu_households_per_100_people(),
    )
