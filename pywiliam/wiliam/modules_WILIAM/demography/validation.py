"""
Module demography.validation
Translated using PySD version 3.10.0
"""


@component.add(
    name="check_errors_households_composition",
    units="1",
    subscripts=["REGIONS_EU27_I", "HOUSEHOLDS_DEMOGRAPHY_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "number_households_by_type_eu27": 1,
        "economic_aggregation_households": 2,
    },
)
def check_errors_households_composition():
    """
    Relative errors in households composition in 2015.
    """
    return xidz(
        number_households_by_type_eu27()
        - economic_aggregation_households()
        .loc[_subscript_dict["REGIONS_EU27_I"], :]
        .rename({"REGIONS_35_I": "REGIONS_EU27_I"}),
        economic_aggregation_households()
        .loc[_subscript_dict["REGIONS_EU27_I"], :]
        .rename({"REGIONS_35_I": "REGIONS_EU27_I"}),
        0,
    )


@component.add(
    name="check_number_EU_households_with_children_under_15",
    units="households",
    subscripts=["REGIONS_EU27_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"number_households_by_type_eu27": 6},
)
def check_number_eu_households_with_children_under_15():
    """
    Number of european households with children
    """
    return (
        number_households_by_type_eu27()
        .loc[:, "DENSE_SINGLEWCHILDREN"]
        .reset_coords(drop=True)
        + number_households_by_type_eu27()
        .loc[:, "DENSE_COUPLEWCHILDREN"]
        .reset_coords(drop=True)
        + number_households_by_type_eu27()
        .loc[:, "DENSE_OTHERWCHILDREN"]
        .reset_coords(drop=True)
        + number_households_by_type_eu27()
        .loc[:, "SPARSE_SINGLEWCHILDREN"]
        .reset_coords(drop=True)
        + number_households_by_type_eu27()
        .loc[:, "SPARSE_COUPLEWCHILDREN"]
        .reset_coords(drop=True)
        + number_households_by_type_eu27()
        .loc[:, "SPARSE_OTHERWCHILDREN"]
        .reset_coords(drop=True)
    )


@component.add(
    name="check_population",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"historic_population_35_regions": 2, "population_35_regions": 1},
)
def check_population():
    return (
        historic_population_35_regions() - population_35_regions()
    ) / historic_population_35_regions()


@component.add(
    name="economic_aggregation_households",
    units="households",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_DEMOGRAPHY_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"number_of_households_by_income_and_type": 60},
)
def economic_aggregation_households():
    """
    Aggregation of economic households to meet the demographic categories of households composition
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "HOUSEHOLDS_DEMOGRAPHY_I": _subscript_dict["HOUSEHOLDS_DEMOGRAPHY_I"],
        },
        ["REGIONS_35_I", "HOUSEHOLDS_DEMOGRAPHY_I"],
    )
    value.loc[:, ["DENSE_SINGLE"]] = (
        (
            number_of_households_by_income_and_type()
            .loc[:, "INCOME1_DENSE_SINGLE"]
            .reset_coords(drop=True)
            + number_of_households_by_income_and_type()
            .loc[:, "INCOME2_DENSE_SINGLE"]
            .reset_coords(drop=True)
            + number_of_households_by_income_and_type()
            .loc[:, "INCOME3_DENSE_SINGLE"]
            .reset_coords(drop=True)
            + number_of_households_by_income_and_type()
            .loc[:, "INCOME4_DENSE_SINGLE"]
            .reset_coords(drop=True)
            + number_of_households_by_income_and_type()
            .loc[:, "INCOME5_DENSE_SINGLE"]
            .reset_coords(drop=True)
        )
        .expand_dims({"HOUSEHOLDS_DEMOGRAPHY_I": ["DENSE_SINGLE"]}, 1)
        .values
    )
    value.loc[:, ["DENSE_SINGLEWCHILDREN"]] = (
        (
            number_of_households_by_income_and_type()
            .loc[:, "INCOME1_DENSE_SINGLEWCHILDREN"]
            .reset_coords(drop=True)
            + number_of_households_by_income_and_type()
            .loc[:, "INCOME2_DENSE_SINGLEWCHILDREN"]
            .reset_coords(drop=True)
            + number_of_households_by_income_and_type()
            .loc[:, "INCOME3_DENSE_SINGLEWCHILDREN"]
            .reset_coords(drop=True)
            + number_of_households_by_income_and_type()
            .loc[:, "INCOME4_DENSE_SINGLEWCHILDREN"]
            .reset_coords(drop=True)
            + number_of_households_by_income_and_type()
            .loc[:, "INCOME5_DENSE_SINGLEWCHILDREN"]
            .reset_coords(drop=True)
        )
        .expand_dims({"HOUSEHOLDS_DEMOGRAPHY_I": ["DENSE_SINGLEWCHILDREN"]}, 1)
        .values
    )
    value.loc[:, ["DENSE_COUPLE"]] = (
        (
            number_of_households_by_income_and_type()
            .loc[:, "INCOME1_DENSE_COUPLE"]
            .reset_coords(drop=True)
            + number_of_households_by_income_and_type()
            .loc[:, "INCOME2_DENSE_COUPLE"]
            .reset_coords(drop=True)
            + number_of_households_by_income_and_type()
            .loc[:, "INCOME3_DENSE_COUPLE"]
            .reset_coords(drop=True)
            + number_of_households_by_income_and_type()
            .loc[:, "INCOME4_DENSE_COUPLE"]
            .reset_coords(drop=True)
            + number_of_households_by_income_and_type()
            .loc[:, "INCOME5_DENSE_COUPLE"]
            .reset_coords(drop=True)
        )
        .expand_dims({"HOUSEHOLDS_DEMOGRAPHY_I": ["DENSE_COUPLE"]}, 1)
        .values
    )
    value.loc[:, ["DENSE_COUPLEWCHILDREN"]] = (
        (
            number_of_households_by_income_and_type()
            .loc[:, "INCOME1_DENSE_COUPLEWCHILDREN"]
            .reset_coords(drop=True)
            + number_of_households_by_income_and_type()
            .loc[:, "INCOME2_DENSE_COUPLEWCHILDREN"]
            .reset_coords(drop=True)
            + number_of_households_by_income_and_type()
            .loc[:, "INCOME3_DENSE_COUPLEWCHILDREN"]
            .reset_coords(drop=True)
            + number_of_households_by_income_and_type()
            .loc[:, "INCOME4_DENSE_COUPLEWCHILDREN"]
            .reset_coords(drop=True)
            + number_of_households_by_income_and_type()
            .loc[:, "INCOME5_DENSE_COUPLEWCHILDREN"]
            .reset_coords(drop=True)
        )
        .expand_dims({"HOUSEHOLDS_DEMOGRAPHY_I": ["DENSE_COUPLEWCHILDREN"]}, 1)
        .values
    )
    value.loc[:, ["DENSE_OTHER"]] = (
        (
            number_of_households_by_income_and_type()
            .loc[:, "INCOME1_DENSE_OTHER"]
            .reset_coords(drop=True)
            + number_of_households_by_income_and_type()
            .loc[:, "INCOME2_DENSE_OTHER"]
            .reset_coords(drop=True)
            + number_of_households_by_income_and_type()
            .loc[:, "INCOME3_DENSE_OTHER"]
            .reset_coords(drop=True)
            + number_of_households_by_income_and_type()
            .loc[:, "INCOME4_DENSE_OTHER"]
            .reset_coords(drop=True)
            + number_of_households_by_income_and_type()
            .loc[:, "INCOME5_DENSE_OTHER"]
            .reset_coords(drop=True)
        )
        .expand_dims({"HOUSEHOLDS_DEMOGRAPHY_I": ["DENSE_OTHER"]}, 1)
        .values
    )
    value.loc[:, ["DENSE_OTHERWCHILDREN"]] = (
        (
            number_of_households_by_income_and_type()
            .loc[:, "INCOME1_DENSE_OTHERWCHILDREN"]
            .reset_coords(drop=True)
            + number_of_households_by_income_and_type()
            .loc[:, "INCOME2_DENSE_OTHERWCHILDREN"]
            .reset_coords(drop=True)
            + number_of_households_by_income_and_type()
            .loc[:, "INCOME3_DENSE_OTHERWCHILDREN"]
            .reset_coords(drop=True)
            + number_of_households_by_income_and_type()
            .loc[:, "INCOME4_DENSE_OTHERWCHILDREN"]
            .reset_coords(drop=True)
            + number_of_households_by_income_and_type()
            .loc[:, "INCOME5_DENSE_OTHERWCHILDREN"]
            .reset_coords(drop=True)
        )
        .expand_dims({"HOUSEHOLDS_DEMOGRAPHY_I": ["DENSE_OTHERWCHILDREN"]}, 1)
        .values
    )
    value.loc[:, ["SPARSE_SINGLE"]] = (
        (
            number_of_households_by_income_and_type()
            .loc[:, "INCOME1_SPARSE_SINGLE"]
            .reset_coords(drop=True)
            + number_of_households_by_income_and_type()
            .loc[:, "INCOME2_SPARSE_SINGLE"]
            .reset_coords(drop=True)
            + number_of_households_by_income_and_type()
            .loc[:, "INCOME3_SPARSE_SINGLE"]
            .reset_coords(drop=True)
            + number_of_households_by_income_and_type()
            .loc[:, "INCOME4_SPARSE_SINGLE"]
            .reset_coords(drop=True)
            + number_of_households_by_income_and_type()
            .loc[:, "INCOME5_SPARSE_SINGLE"]
            .reset_coords(drop=True)
        )
        .expand_dims({"HOUSEHOLDS_DEMOGRAPHY_I": ["SPARSE_SINGLE"]}, 1)
        .values
    )
    value.loc[:, ["SPARSE_SINGLEWCHILDREN"]] = (
        (
            number_of_households_by_income_and_type()
            .loc[:, "INCOME1_SPARSE_SINGLEWCHILDREN"]
            .reset_coords(drop=True)
            + number_of_households_by_income_and_type()
            .loc[:, "INCOME2_SPARSE_SINGLEWCHILDREN"]
            .reset_coords(drop=True)
            + number_of_households_by_income_and_type()
            .loc[:, "INCOME3_SPARSE_SINGLEWCHILDREN"]
            .reset_coords(drop=True)
            + number_of_households_by_income_and_type()
            .loc[:, "INCOME4_SPARSE_SINGLEWCHILDREN"]
            .reset_coords(drop=True)
            + number_of_households_by_income_and_type()
            .loc[:, "INCOME5_SPARSE_SINGLEWCHILDREN"]
            .reset_coords(drop=True)
        )
        .expand_dims({"HOUSEHOLDS_DEMOGRAPHY_I": ["SPARSE_SINGLEWCHILDREN"]}, 1)
        .values
    )
    value.loc[:, ["SPARSE_COUPLE"]] = (
        (
            number_of_households_by_income_and_type()
            .loc[:, "INCOME1_SPARSE_COUPLE"]
            .reset_coords(drop=True)
            + number_of_households_by_income_and_type()
            .loc[:, "INCOME2_SPARSE_COUPLE"]
            .reset_coords(drop=True)
            + number_of_households_by_income_and_type()
            .loc[:, "INCOME3_SPARSE_COUPLE"]
            .reset_coords(drop=True)
            + number_of_households_by_income_and_type()
            .loc[:, "INCOME4_SPARSE_COUPLE"]
            .reset_coords(drop=True)
            + number_of_households_by_income_and_type()
            .loc[:, "INCOME5_SPARSE_COUPLE"]
            .reset_coords(drop=True)
        )
        .expand_dims({"HOUSEHOLDS_DEMOGRAPHY_I": ["SPARSE_COUPLE"]}, 1)
        .values
    )
    value.loc[:, ["SPARSE_COUPLEWCHILDREN"]] = (
        (
            number_of_households_by_income_and_type()
            .loc[:, "INCOME1_SPARSE_COUPLEWCHILDREN"]
            .reset_coords(drop=True)
            + number_of_households_by_income_and_type()
            .loc[:, "INCOME2_SPARSE_COUPLEWCHILDREN"]
            .reset_coords(drop=True)
            + number_of_households_by_income_and_type()
            .loc[:, "INCOME3_SPARSE_COUPLEWCHILDREN"]
            .reset_coords(drop=True)
            + number_of_households_by_income_and_type()
            .loc[:, "INCOME4_SPARSE_COUPLEWCHILDREN"]
            .reset_coords(drop=True)
            + number_of_households_by_income_and_type()
            .loc[:, "INCOME5_SPARSE_COUPLEWCHILDREN"]
            .reset_coords(drop=True)
        )
        .expand_dims({"HOUSEHOLDS_DEMOGRAPHY_I": ["SPARSE_COUPLEWCHILDREN"]}, 1)
        .values
    )
    value.loc[:, ["SPARSE_OTHER"]] = (
        (
            number_of_households_by_income_and_type()
            .loc[:, "INCOME1_SPARSE_OTHER"]
            .reset_coords(drop=True)
            + number_of_households_by_income_and_type()
            .loc[:, "INCOME2_SPARSE_OTHER"]
            .reset_coords(drop=True)
            + number_of_households_by_income_and_type()
            .loc[:, "INCOME3_SPARSE_OTHER"]
            .reset_coords(drop=True)
            + number_of_households_by_income_and_type()
            .loc[:, "INCOME4_SPARSE_OTHER"]
            .reset_coords(drop=True)
            + number_of_households_by_income_and_type()
            .loc[:, "INCOME5_SPARSE_OTHER"]
            .reset_coords(drop=True)
        )
        .expand_dims({"HOUSEHOLDS_DEMOGRAPHY_I": ["SPARSE_OTHER"]}, 1)
        .values
    )
    value.loc[:, ["SPARSE_OTHERWCHILDREN"]] = (
        (
            number_of_households_by_income_and_type()
            .loc[:, "INCOME1_SPARSE_OTHERWCHILDREN"]
            .reset_coords(drop=True)
            + number_of_households_by_income_and_type()
            .loc[:, "INCOME2_SPARSE_OTHERWCHILDREN"]
            .reset_coords(drop=True)
            + number_of_households_by_income_and_type()
            .loc[:, "INCOME3_SPARSE_OTHERWCHILDREN"]
            .reset_coords(drop=True)
            + number_of_households_by_income_and_type()
            .loc[:, "INCOME4_SPARSE_OTHERWCHILDREN"]
            .reset_coords(drop=True)
            + number_of_households_by_income_and_type()
            .loc[:, "INCOME5_SPARSE_OTHERWCHILDREN"]
            .reset_coords(drop=True)
        )
        .expand_dims({"HOUSEHOLDS_DEMOGRAPHY_I": ["SPARSE_OTHERWCHILDREN"]}, 1)
        .values
    )
    return value


@component.add(
    name="Historic_population_35_regions",
    units="people",
    subscripts=["REGIONS_35_I"],
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_historic_population_35_regions",
        "__data__": "_ext_data_historic_population_35_regions",
        "time": 1,
    },
)
def historic_population_35_regions():
    """
    Historic population by region
    """
    return _ext_data_historic_population_35_regions(time())


_ext_data_historic_population_35_regions = ExtData(
    "model_parameters/demography/demography.xlsx",
    "Calibration",
    "HISTORICAL_TIME_POPULATION",
    "HISTORICAL_POPULATION",
    "interpolate",
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    _root,
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    "_ext_data_historic_population_35_regions",
)
