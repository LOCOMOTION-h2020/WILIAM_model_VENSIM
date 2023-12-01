"""
Module energy.end_use.households_buildings
Translated using PySD version 3.10.0
"""


@component.add(
    name="ALPHA_PARAMETER_CONSTRUCTION",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_alpha_parameter_construction"},
)
def alpha_parameter_construction():
    return _ext_constant_alpha_parameter_construction()


_ext_constant_alpha_parameter_construction = ExtConstant(
    "model_parameters/energy/energy-end_use-buildings.xlsx",
    "Other_building_parameters",
    "ALPHA_PARAMETER_CONSTRUCTION",
    {},
    _root,
    {},
    "_ext_constant_alpha_parameter_construction",
)


@component.add(
    name="AREA_BY_DWELLING_TYPE",
    subscripts=["REGIONS_35_I", "BUILDING_TYPE_I"],
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_area_by_dwelling_type",
        "__data__": "_ext_data_area_by_dwelling_type",
        "time": 1,
    },
)
def area_by_dwelling_type():
    """
    Dwelling area per household type.
    """
    return _ext_data_area_by_dwelling_type(time())


_ext_data_area_by_dwelling_type = ExtData(
    "model_parameters/energy/energy-end_use-buildings.xlsx",
    "Area_by_type",
    "TIME_SERIES",
    "AREA_SINGLE_FAMILY",
    None,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "BUILDING_TYPE_I": ["SINGLE_FAMILY"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "BUILDING_TYPE_I": _subscript_dict["BUILDING_TYPE_I"],
    },
    "_ext_data_area_by_dwelling_type",
)

_ext_data_area_by_dwelling_type.add(
    "model_parameters/energy/energy-end_use-buildings.xlsx",
    "Area_by_type",
    "TIME_SERIES",
    "AREA_MULTI_FAMILY",
    None,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "BUILDING_TYPE_I": ["MULTI_FAMILY"],
    },
)


@component.add(
    name="AREA_PER_DWELLING",
    subscripts=["REGIONS_35_I"],
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_area_per_dwelling",
        "__data__": "_ext_data_area_per_dwelling",
        "time": 1,
    },
)
def area_per_dwelling():
    """
    Area
    """
    return _ext_data_area_per_dwelling(time())


_ext_data_area_per_dwelling = ExtData(
    "model_parameters/energy/energy-end_use-buildings.xlsx",
    "Area_per_dwelling",
    "TIME_SERIES",
    "AREA_PER_DWELLING",
    None,
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    _root,
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    "_ext_data_area_per_dwelling",
)


@component.add(
    name="C_WEIBULL_PARAMETER",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_c_weibull_parameter"},
)
def c_weibull_parameter():
    return _ext_constant_c_weibull_parameter()


_ext_constant_c_weibull_parameter = ExtConstant(
    "model_parameters/energy/energy-end_use-buildings.xlsx",
    "Other_building_parameters",
    "C_WEIBULL_PARAMETER",
    {},
    _root,
    {},
    "_ext_constant_c_weibull_parameter",
)


@component.add(
    name="cummulative_renovated_dwellings",
    subscripts=[
        "REGIONS_35_I",
        "BUILDING_AGE_I",
        "BUILDING_LOCATION_I",
        "BUILDING_TYPE_I",
        "RENOVATION_LEVEL_I",
    ],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_cummulative_renovated_dwellings": 1},
    other_deps={
        "_integ_cummulative_renovated_dwellings": {
            "initial": {},
            "step": {"input_cummulative_renovated_dwelling_s": 1},
        }
    },
)
def cummulative_renovated_dwellings():
    return _integ_cummulative_renovated_dwellings()


_integ_cummulative_renovated_dwellings = Integ(
    lambda: input_cummulative_renovated_dwelling_s(),
    lambda: xr.DataArray(
        0,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "BUILDING_AGE_I": _subscript_dict["BUILDING_AGE_I"],
            "BUILDING_LOCATION_I": _subscript_dict["BUILDING_LOCATION_I"],
            "BUILDING_TYPE_I": _subscript_dict["BUILDING_TYPE_I"],
            "RENOVATION_LEVEL_I": _subscript_dict["RENOVATION_LEVEL_I"],
        },
        [
            "REGIONS_35_I",
            "BUILDING_AGE_I",
            "BUILDING_LOCATION_I",
            "BUILDING_TYPE_I",
            "RENOVATION_LEVEL_I",
        ],
    ),
    "_integ_cummulative_renovated_dwellings",
)


@component.add(
    name="demolition_rate",
    units="DMNL/per_year",
    subscripts=["REGIONS_35_I", "BUILDING_AGE_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_demolition_rate"},
)
def demolition_rate():
    """
    Share of demolished buildings.
    """
    return _ext_constant_demolition_rate()


_ext_constant_demolition_rate = ExtConstant(
    "model_parameters/energy/energy-end_use-buildings.xlsx",
    "Dem_rate",
    "DEMOLITION_RATES",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "BUILDING_AGE_I": _subscript_dict["BUILDING_AGE_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "BUILDING_AGE_I": _subscript_dict["BUILDING_AGE_I"],
    },
    "_ext_constant_demolition_rate",
)


@component.add(
    name="dwelling_demolition",
    subscripts=[
        "REGIONS_35_I",
        "BUILDING_AGE_I",
        "BUILDING_LOCATION_I",
        "BUILDING_TYPE_I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "demolition_rate": 1, "new_dwelling_stocks": 1},
)
def dwelling_demolition():
    return if_then_else(
        time() < 2016,
        lambda: xr.DataArray(
            0,
            {
                "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                "BUILDING_AGE_I": _subscript_dict["BUILDING_AGE_I"],
                "BUILDING_LOCATION_I": _subscript_dict["BUILDING_LOCATION_I"],
                "BUILDING_TYPE_I": _subscript_dict["BUILDING_TYPE_I"],
            },
            [
                "REGIONS_35_I",
                "BUILDING_AGE_I",
                "BUILDING_LOCATION_I",
                "BUILDING_TYPE_I",
            ],
        ),
        lambda: demolition_rate() * new_dwelling_stocks(),
    )


@component.add(
    name="dwelling_stocks_sum",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"new_dwelling_stocks": 1},
)
def dwelling_stocks_sum():
    return sum(
        new_dwelling_stocks().rename(
            {
                "BUILDING_AGE_I": "BUILDING_AGE_I!",
                "BUILDING_LOCATION_I": "BUILDING_LOCATION_I!",
                "BUILDING_TYPE_I": "BUILDING_TYPE_I!",
            }
        ),
        dim=["BUILDING_AGE_I!", "BUILDING_LOCATION_I!", "BUILDING_TYPE_I!"],
    )


@component.add(
    name="dwellings_renovated_by_type_age", comp_type="Constant", comp_subtype="Normal"
)
def dwellings_renovated_by_type_age():
    return 0


@component.add(
    name="final_energy_consumption_dwellings",
    comp_type="Constant",
    comp_subtype="Normal",
)
def final_energy_consumption_dwellings():
    return 0


@component.add(
    name="IMPROVEMENT_LEVELS_FROM_RENOVATION",
    units="DMNL",
    subscripts=["RENOVATION_LEVEL_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_improvement_levels_from_renovation"},
)
def improvement_levels_from_renovation():
    return _ext_constant_improvement_levels_from_renovation()


_ext_constant_improvement_levels_from_renovation = ExtConstant(
    "model_parameters/energy/energy-end_use-buildings.xlsx",
    "Other_building_parameters",
    "IMPROVEMENT_SHARES*",
    {"RENOVATION_LEVEL_I": _subscript_dict["RENOVATION_LEVEL_I"]},
    _root,
    {"RENOVATION_LEVEL_I": _subscript_dict["RENOVATION_LEVEL_I"]},
    "_ext_constant_improvement_levels_from_renovation",
)


@component.add(
    name="IMV_COMFORT",
    units="DMNL",
    subscripts=["REGIONS_35_I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def imv_comfort():
    """
    Comfort level- will be coming from other part in the model.
    """
    return xr.DataArray(
        1, {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]}, ["REGIONS_35_I"]
    )


@component.add(
    name="INITIAL_DWELLING_STOCK",
    units="dwellings_in_Thousands",
    subscripts=["REGIONS_35_I"],
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_initial_dwelling_stock",
        "__data__": "_ext_data_initial_dwelling_stock",
        "time": 1,
    },
)
def initial_dwelling_stock():
    """
    Intial dwellings number in thousands.
    """
    return _ext_data_initial_dwelling_stock(time())


_ext_data_initial_dwelling_stock = ExtData(
    "model_parameters/energy/energy-end_use-buildings.xlsx",
    "Stock",
    "TIME_SERIES",
    "INITIAL_DWELLING_STOCK",
    "interpolate",
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    _root,
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    "_ext_data_initial_dwelling_stock",
)


@component.add(
    name="INITIAL_DWELLING_STOCK_BY_TYPE_AGE_LOC",
    units="dwellings_in_Thousands",
    subscripts=[
        "REGIONS_35_I",
        "BUILDING_AGE_I",
        "BUILDING_LOCATION_I",
        "BUILDING_TYPE_I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "initial_dwelling_stock": 1,
        "initial_share_age_con": 1,
        "initial_share_loc": 1,
        "initial_share_types": 1,
    },
)
def initial_dwelling_stock_by_type_age_loc():
    """
    Break down of dwelling stock by type age and location.
    """
    return (
        initial_dwelling_stock()
        * initial_share_age_con()
        * initial_share_loc()
        * initial_share_types()
    )


@component.add(
    name="initial_dwellings_getting_demolished",
    units="thousands_dwellings",
    subscripts=[
        "REGIONS_35_I",
        "BUILDING_AGE_I",
        "BUILDING_LOCATION_I",
        "BUILDING_TYPE_I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "intial_dewellings_by_type_age_loc": 1,
        "demolition_rate": 1,
    },
)
def initial_dwellings_getting_demolished():
    """
    REGIONS 35 I ,BUILDING AGE I,BUILDING LOCATION I ,BUILDING TYPE I] )
    """
    return if_then_else(
        time() < 2016,
        lambda: xr.DataArray(
            0,
            {
                "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                "BUILDING_AGE_I": _subscript_dict["BUILDING_AGE_I"],
                "BUILDING_LOCATION_I": _subscript_dict["BUILDING_LOCATION_I"],
                "BUILDING_TYPE_I": _subscript_dict["BUILDING_TYPE_I"],
            },
            [
                "REGIONS_35_I",
                "BUILDING_AGE_I",
                "BUILDING_LOCATION_I",
                "BUILDING_TYPE_I",
            ],
        ),
        lambda: demolition_rate() * intial_dewellings_by_type_age_loc(),
    )


@component.add(
    name="INITIAL_SHARE_AGE_CON",
    units="DMNL",
    subscripts=["REGIONS_35_I", "BUILDING_AGE_I"],
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_initial_share_age_con",
        "__data__": "_ext_data_initial_share_age_con",
        "time": 1,
    },
)
def initial_share_age_con():
    """
    share of dwellings in different age groups.
    """
    return _ext_data_initial_share_age_con(time())


_ext_data_initial_share_age_con = ExtData(
    "model_parameters/energy/energy-end_use-buildings.xlsx",
    "Shares_age",
    "TIME_SERIES",
    "BEFORE_45",
    "interpolate",
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"], "BUILDING_AGE_I": ["BEFORE_45"]},
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "BUILDING_AGE_I": _subscript_dict["BUILDING_AGE_I"],
    },
    "_ext_data_initial_share_age_con",
)

_ext_data_initial_share_age_con.add(
    "model_parameters/energy/energy-end_use-buildings.xlsx",
    "Shares_age",
    "TIME_SERIES",
    "FROM_45_69",
    "interpolate",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "BUILDING_AGE_I": ["FROM_45_TO_69"],
    },
)

_ext_data_initial_share_age_con.add(
    "model_parameters/energy/energy-end_use-buildings.xlsx",
    "Shares_age",
    "TIME_SERIES",
    "FROM_70_79",
    "interpolate",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "BUILDING_AGE_I": ["FROM_70_TO_79"],
    },
)

_ext_data_initial_share_age_con.add(
    "model_parameters/energy/energy-end_use-buildings.xlsx",
    "Shares_age",
    "TIME_SERIES",
    "FROM_80_89",
    "interpolate",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "BUILDING_AGE_I": ["FROM_80_TO_89"],
    },
)

_ext_data_initial_share_age_con.add(
    "model_parameters/energy/energy-end_use-buildings.xlsx",
    "Shares_age",
    "TIME_SERIES",
    "FROM_90_99",
    "interpolate",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "BUILDING_AGE_I": ["FROM_90_TO_99"],
    },
)

_ext_data_initial_share_age_con.add(
    "model_parameters/energy/energy-end_use-buildings.xlsx",
    "Shares_age",
    "TIME_SERIES",
    "FROM_00_10",
    "interpolate",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "BUILDING_AGE_I": ["FROM_00_TO_10"],
    },
)

_ext_data_initial_share_age_con.add(
    "model_parameters/energy/energy-end_use-buildings.xlsx",
    "Shares_age",
    "TIME_SERIES",
    "AFTER_10",
    "interpolate",
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"], "BUILDING_AGE_I": ["AFTER_10"]},
)


@component.add(
    name="INITIAL_SHARE_LOC",
    units="DMNL",
    subscripts=["REGIONS_35_I", "BUILDING_LOCATION_I"],
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_initial_share_loc",
        "__data__": "_ext_data_initial_share_loc",
        "time": 1,
    },
)
def initial_share_loc():
    """
    Shareof dwellings by location. Urban or Rural.
    """
    return _ext_data_initial_share_loc(time())


_ext_data_initial_share_loc = ExtData(
    "model_parameters/energy/energy-end_use-buildings.xlsx",
    "Shares_loc",
    "TIME_SERIES",
    "BUILDING_SHARES_LOCATION_URBAN",
    "interpolate",
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"], "BUILDING_LOCATION_I": ["urban"]},
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "BUILDING_LOCATION_I": _subscript_dict["BUILDING_LOCATION_I"],
    },
    "_ext_data_initial_share_loc",
)

_ext_data_initial_share_loc.add(
    "model_parameters/energy/energy-end_use-buildings.xlsx",
    "Shares_loc",
    "TIME_SERIES",
    "BUILDING_SHARES_LOCATION_RURAL",
    "interpolate",
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"], "BUILDING_LOCATION_I": ["rural"]},
)


@component.add(
    name="INITIAL_SHARE_TYPES",
    units="DMNL",
    subscripts=["REGIONS_35_I", "BUILDING_TYPE_I"],
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_initial_share_types",
        "__data__": "_ext_data_initial_share_types",
        "time": 1,
    },
)
def initial_share_types():
    """
    Seperation of share by single and multi family.
    """
    return _ext_data_initial_share_types(time())


_ext_data_initial_share_types = ExtData(
    "model_parameters/energy/energy-end_use-buildings.xlsx",
    "Shares_type",
    "TIME_SERIES",
    "BUILDING_SHARES_SINGLE_FAMILY",
    "interpolate",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "BUILDING_TYPE_I": ["SINGLE_FAMILY"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "BUILDING_TYPE_I": _subscript_dict["BUILDING_TYPE_I"],
    },
    "_ext_data_initial_share_types",
)

_ext_data_initial_share_types.add(
    "model_parameters/energy/energy-end_use-buildings.xlsx",
    "Shares_type",
    "TIME_SERIES",
    "BUILDING_SHARES_MULTI_FAMILY",
    "interpolate",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "BUILDING_TYPE_I": ["MULTI_FAMILY"],
    },
)


@component.add(
    name="input_cummulative_renovated_dwelling_s",
    units="thousands_dwellings/Year",
    subscripts=[
        "REGIONS_35_I",
        "BUILDING_AGE_I",
        "BUILDING_LOCATION_I",
        "BUILDING_TYPE_I",
        "RENOVATION_LEVEL_I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "number_buildings_renovated_by_hh_type_age_loc": 4,
        "share_of_renovation_level_by_different_hh": 4,
    },
)
def input_cummulative_renovated_dwelling_s():
    """
    Renovated per year dwellings by region,age, location and type.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "BUILDING_AGE_I": _subscript_dict["BUILDING_AGE_I"],
            "BUILDING_LOCATION_I": _subscript_dict["BUILDING_LOCATION_I"],
            "BUILDING_TYPE_I": _subscript_dict["BUILDING_TYPE_I"],
            "RENOVATION_LEVEL_I": _subscript_dict["RENOVATION_LEVEL_I"],
        },
        [
            "REGIONS_35_I",
            "BUILDING_AGE_I",
            "BUILDING_LOCATION_I",
            "BUILDING_TYPE_I",
            "RENOVATION_LEVEL_I",
        ],
    )
    value.loc[:, :, :, :, ["RENOVATION_LEVEL_NONE"]] = (
        (
            number_buildings_renovated_by_hh_type_age_loc()
            * float(
                share_of_renovation_level_by_different_hh().loc["RENOVATION_LEVEL_NONE"]
            )
        )
        .expand_dims({"RENOVATION_LEVEL_I": ["RENOVATION_LEVEL_NONE"]}, 4)
        .values
    )
    value.loc[:, :, :, :, ["RENOVATION_LEVEL_LOW"]] = (
        (
            number_buildings_renovated_by_hh_type_age_loc()
            * float(
                share_of_renovation_level_by_different_hh().loc["RENOVATION_LEVEL_LOW"]
            )
        )
        .expand_dims({"RENOVATION_LEVEL_I": ["RENOVATION_LEVEL_LOW"]}, 4)
        .values
    )
    value.loc[:, :, :, :, ["RENOVATION_LEVEL_MEDIUM"]] = (
        (
            number_buildings_renovated_by_hh_type_age_loc()
            * float(
                share_of_renovation_level_by_different_hh().loc[
                    "RENOVATION_LEVEL_MEDIUM"
                ]
            )
        )
        .expand_dims({"RENOVATION_LEVEL_I": ["RENOVATION_LEVEL_MEDIUM"]}, 4)
        .values
    )
    value.loc[:, :, :, :, ["RENOVATION_LEVEL_HIGH"]] = (
        (
            number_buildings_renovated_by_hh_type_age_loc()
            * float(
                share_of_renovation_level_by_different_hh().loc["RENOVATION_LEVEL_HIGH"]
            )
        )
        .expand_dims({"RENOVATION_LEVEL_I": ["RENOVATION_LEVEL_HIGH"]}, 4)
        .values
    )
    return value


@component.add(
    name="INTIAL_DEWELLINGS_BY_TYPE_AGE_LOC",
    units="thousands_dwellings",
    subscripts=[
        "REGIONS_35_I",
        "BUILDING_AGE_I",
        "BUILDING_LOCATION_I",
        "BUILDING_TYPE_I",
    ],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_intial_dewellings_by_type_age_loc": 1},
    other_deps={
        "_integ_intial_dewellings_by_type_age_loc": {
            "initial": {"initial_dwelling_stock_by_type_age_loc": 1},
            "step": {
                "number_buildings_renovated_by_hh_type_age_loc": 1,
                "initial_dwellings_getting_demolished": 1,
            },
        }
    },
)
def intial_dewellings_by_type_age_loc():
    """
    -initial dwellings getting demolished[REGIONS 35 I, BUILDING AGE I]-number buildings renovated by HH TYPE AGE LOC[REGIONS 35 I]
    """
    return _integ_intial_dewellings_by_type_age_loc()


_integ_intial_dewellings_by_type_age_loc = Integ(
    lambda: -number_buildings_renovated_by_hh_type_age_loc()
    - initial_dwellings_getting_demolished(),
    lambda: initial_dwelling_stock_by_type_age_loc(),
    "_integ_intial_dewellings_by_type_age_loc",
)


@component.add(
    name="K_WEIBULL_PARAMETER",
    units="Dnml",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_k_weibull_parameter"},
)
def k_weibull_parameter():
    return _ext_constant_k_weibull_parameter()


_ext_constant_k_weibull_parameter = ExtConstant(
    "model_parameters/energy/energy-end_use-buildings.xlsx",
    "Other_building_parameters",
    "K_WEIBULL_PARAMETER",
    {},
    _root,
    {},
    "_ext_constant_k_weibull_parameter",
)


@component.add(
    name="new_dwelling_stocks",
    units="thousands_dwellings",
    subscripts=[
        "REGIONS_35_I",
        "BUILDING_AGE_I",
        "BUILDING_LOCATION_I",
        "BUILDING_TYPE_I",
    ],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_new_dwelling_stocks": 1},
    other_deps={
        "_integ_new_dwelling_stocks": {
            "initial": {},
            "step": {"new_dwellings_input": 1, "dwelling_demolition": 1},
        }
    },
)
def new_dwelling_stocks():
    """
    Number of dwellings by age, type, urban or rural.IF THEN ELSE ( Time>=2015, INITIAL DWELLING STOCK BY TYPE AGE LOC[REGIONS 35 I,BUILDING AGE I,BUILDING LOCATION I,BUILDING TYPE I]+new dwellings input[REGIONS 35 I,BUILDING TYPE I]-dwelling demolition[REGIONS 35 I,BUILDING AGE I,BUILDING LOCATION I,BUILDING TYPE I], 0) INITIAL DWELLING STOCK BY TYPE AGE LOC[REGIONS 35 I,BUILDING AGE I,BUILDING LOCATION I,BUILDING TYPE I]
    """
    return _integ_new_dwelling_stocks()


_integ_new_dwelling_stocks = Integ(
    lambda: (
        new_dwellings_input()
        - dwelling_demolition().transpose(
            "REGIONS_35_I", "BUILDING_TYPE_I", "BUILDING_AGE_I", "BUILDING_LOCATION_I"
        )
    ).transpose(
        "REGIONS_35_I", "BUILDING_AGE_I", "BUILDING_LOCATION_I", "BUILDING_TYPE_I"
    ),
    lambda: xr.DataArray(
        0,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "BUILDING_AGE_I": _subscript_dict["BUILDING_AGE_I"],
            "BUILDING_LOCATION_I": _subscript_dict["BUILDING_LOCATION_I"],
            "BUILDING_TYPE_I": _subscript_dict["BUILDING_TYPE_I"],
        },
        ["REGIONS_35_I", "BUILDING_AGE_I", "BUILDING_LOCATION_I", "BUILDING_TYPE_I"],
    ),
    "_integ_new_dwelling_stocks",
)


@component.add(
    name="new_dwellings",
    units="thousand_dwellings/Year",
    subscripts=["REGIONS_35_I", "BUILDING_TYPE_I"],
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_new_dwellings",
        "__data__": "_ext_data_new_dwellings",
        "time": 1,
    },
)
def new_dwellings():
    """
    New dwellings being constructed.
    """
    return _ext_data_new_dwellings(time())


_ext_data_new_dwellings = ExtData(
    "model_parameters/energy/energy-end_use-buildings.xlsx",
    "New_buildings",
    "TIME_SERIES",
    "NEW_BUILDINGS_SINGLE_FAMILY",
    "interpolate",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "BUILDING_TYPE_I": ["SINGLE_FAMILY"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "BUILDING_TYPE_I": _subscript_dict["BUILDING_TYPE_I"],
    },
    "_ext_data_new_dwellings",
)

_ext_data_new_dwellings.add(
    "model_parameters/energy/energy-end_use-buildings.xlsx",
    "New_buildings",
    "TIME_SERIES",
    "NEW_BUILDINGS_MULTI_FAMILY",
    "interpolate",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "BUILDING_TYPE_I": ["MULTI_FAMILY"],
    },
)


@component.add(
    name="new_dwellings_input",
    subscripts=["REGIONS_35_I", "BUILDING_TYPE_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "new_dwellings": 1},
)
def new_dwellings_input():
    """
    New dwellings getting build.
    """
    return if_then_else(
        time() < 2016,
        lambda: xr.DataArray(
            0,
            {
                "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                "BUILDING_TYPE_I": _subscript_dict["BUILDING_TYPE_I"],
            },
            ["REGIONS_35_I", "BUILDING_TYPE_I"],
        ),
        lambda: new_dwellings(),
    )


@component.add(
    name="number_buildings_renovated_by_HH_building_age",
    comp_type="Constant",
    comp_subtype="Normal",
)
def number_buildings_renovated_by_hh_building_age():
    return 0


@component.add(
    name="number_buildings_renovated_by_HH_TYPE_AGE_LOC",
    units="thousands_dwellings/Year",
    subscripts=[
        "REGIONS_35_I",
        "BUILDING_AGE_I",
        "BUILDING_LOCATION_I",
        "BUILDING_TYPE_I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "intial_dewellings_by_type_age_loc": 1,
        "renovation_rate": 1,
    },
)
def number_buildings_renovated_by_hh_type_age_loc():
    """
    THe renovation ofbuilding is starting after the year 2015.
    """
    return if_then_else(
        time() < 2016,
        lambda: xr.DataArray(
            0,
            {
                "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                "BUILDING_AGE_I": _subscript_dict["BUILDING_AGE_I"],
                "BUILDING_LOCATION_I": _subscript_dict["BUILDING_LOCATION_I"],
                "BUILDING_TYPE_I": _subscript_dict["BUILDING_TYPE_I"],
            },
            [
                "REGIONS_35_I",
                "BUILDING_AGE_I",
                "BUILDING_LOCATION_I",
                "BUILDING_TYPE_I",
            ],
        ),
        lambda: intial_dewellings_by_type_age_loc() * renovation_rate(),
    )


@component.add(
    name="renovation_rate",
    units="1/Year",
    subscripts=["REGIONS_35_I", "BUILDING_AGE_I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def renovation_rate():
    """
    Assumption made by the Authors of the model that the renovation rate for EU is between 1% and 2 %. Set here to 2%.
    """
    return xr.DataArray(
        0.02,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "BUILDING_AGE_I": _subscript_dict["BUILDING_AGE_I"],
        },
        ["REGIONS_35_I", "BUILDING_AGE_I"],
    )


@component.add(name="SHARE_FEC", comp_type="Constant", comp_subtype="Normal")
def share_fec():
    return 0


@component.add(
    name="SHARE_OF_DWELLINGS_WITH_COOLING",
    subscripts=["REGIONS_35_I", "BUILDING_TYPE_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_share_of_dwellings_with_cooling"},
)
def share_of_dwellings_with_cooling():
    """
    Shares of households with cooling.
    """
    return _ext_constant_share_of_dwellings_with_cooling()


_ext_constant_share_of_dwellings_with_cooling = ExtConstant(
    "model_parameters/energy/energy-end_use-buildings.xlsx",
    "Shares_cooling",
    "SHARES_COOLING",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "BUILDING_TYPE_I": _subscript_dict["BUILDING_TYPE_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "BUILDING_TYPE_I": _subscript_dict["BUILDING_TYPE_I"],
    },
    "_ext_constant_share_of_dwellings_with_cooling",
)


@component.add(
    name="share_of_renovation_level_by_different_HH",
    units="DMNL",
    subscripts=["RENOVATION_LEVEL_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_share_of_renovation_level_by_different_hh"
    },
)
def share_of_renovation_level_by_different_hh():
    """
    Different levels of renovation.
    """
    return _ext_constant_share_of_renovation_level_by_different_hh()


_ext_constant_share_of_renovation_level_by_different_hh = ExtConstant(
    "model_parameters/energy/energy-end_use-buildings.xlsx",
    "Other_building_parameters",
    "RENOVATION_INTENSITY_SHARES*",
    {"RENOVATION_LEVEL_I": _subscript_dict["RENOVATION_LEVEL_I"]},
    _root,
    {"RENOVATION_LEVEL_I": _subscript_dict["RENOVATION_LEVEL_I"]},
    "_ext_constant_share_of_renovation_level_by_different_hh",
)


@component.add(
    name="Sum_Buildings",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"initial_dwelling_stock_by_type_age_loc": 1},
)
def sum_buildings():
    return sum(
        initial_dwelling_stock_by_type_age_loc().rename(
            {
                "BUILDING_AGE_I": "BUILDING_AGE_I!",
                "BUILDING_LOCATION_I": "BUILDING_LOCATION_I!",
                "BUILDING_TYPE_I": "BUILDING_TYPE_I!",
            }
        ),
        dim=["BUILDING_AGE_I!", "BUILDING_LOCATION_I!", "BUILDING_TYPE_I!"],
    )


@component.add(
    name="total_useful_energy_dwellings",
    subscripts=[
        "REGIONS_35_I",
        "BUILDING_AGE_I",
        "BUILDING_LOCATION_I",
        "BUILDING_TYPE_I",
    ],
    comp_type="Constant",
    comp_subtype="Normal",
)
def total_useful_energy_dwellings():
    """
    useful energy by dwelling type age loc non renovated[REGIONS 35 I,BUILDING AGE I,BUILDING LOCATION I,BUILDING TYPE I]+useful energy by new dwelling type [REGIONS 35 I,BUILDING AGE I,BUILDING LOCATION I,BUILDING TYPE I]
    """
    return xr.DataArray(
        0,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "BUILDING_AGE_I": _subscript_dict["BUILDING_AGE_I"],
            "BUILDING_LOCATION_I": _subscript_dict["BUILDING_LOCATION_I"],
            "BUILDING_TYPE_I": _subscript_dict["BUILDING_TYPE_I"],
        },
        ["REGIONS_35_I", "BUILDING_AGE_I", "BUILDING_LOCATION_I", "BUILDING_TYPE_I"],
    )


@component.add(
    name="U_VALUE_BY_AGE",
    units="DMNL",
    subscripts=["REGIONS_35_I", "BUILDING_AGE_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_u_value_by_age"},
)
def u_value_by_age():
    """
    U-value of buildings by different age.
    """
    return _ext_constant_u_value_by_age()


_ext_constant_u_value_by_age = ExtConstant(
    "model_parameters/energy/energy-end_use-buildings.xlsx",
    "U_value",
    "U_VALUE",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "BUILDING_AGE_I": _subscript_dict["BUILDING_AGE_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "BUILDING_AGE_I": _subscript_dict["BUILDING_AGE_I"],
    },
    "_ext_constant_u_value_by_age",
)


@component.add(
    name="UNIT_CONVERSION_kWh_TJ",
    units="kWh/TJ",
    comp_type="Constant",
    comp_subtype="Normal",
)
def unit_conversion_kwh_tj():
    """
    Unit converter - Kilowatthours to Terajoule
    """
    return 3.6e-06


@component.add(
    name="USEFUL_ENERGY_BUILDING_EXISTING_UNTIL_2015",
    units="khw/m2",
    comp_type="Data",
    comp_subtype="Normal",
)
def useful_energy_building_existing_until_2015():
    """
    0GET DIRECT DATA('model_parameters/energy/energy-end_use-buildings.xlsx', 'Useful_energy_SH' , 'BUILDING_AGE_BAND' , 'USEFUL_ENERGY_SPACE_HEATING_MULTI_FAMILY' )
    """
    return 0


@component.add(
    name="useful_energy_by_dwelling_type_age_loc_non_renovated",
    subscripts=[
        "REGIONS_35_I",
        "BUILDING_AGE_I",
        "BUILDING_LOCATION_I",
        "BUILDING_TYPE_I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "area_by_dwelling_type": 1,
        "intial_dewellings_by_type_age_loc": 1,
        "unit_conversion_kwh_tj": 1,
    },
)
def useful_energy_by_dwelling_type_age_loc_non_renovated():
    """
    INTIAL DEWELLINGS BY TYPE AGE LOC[REGIONS 35 I,BUILDING AGE I,BUILDING LOCATION I,BUILDING TYPE I]*AREA BY DWELLING TYPE [REGIONS 35 I,BUILDING TYPE I]*USEFUL ENERGY EXISTING DWELLINGS BY TYPE WATER HEATING[REGIONS 35 I,BUILDING TYPE I,WATER HEATING ]*UNIT CONVERSION kWh TJ/1000
    """
    return (
        area_by_dwelling_type()
        * intial_dewellings_by_type_age_loc().transpose(
            "REGIONS_35_I", "BUILDING_TYPE_I", "BUILDING_AGE_I", "BUILDING_LOCATION_I"
        )
        * unit_conversion_kwh_tj()
    ).transpose(
        "REGIONS_35_I", "BUILDING_AGE_I", "BUILDING_LOCATION_I", "BUILDING_TYPE_I"
    )


@component.add(
    name="useful_energy_by_new_dwelling_type",
    subscripts=[
        "REGIONS_35_I",
        "BUILDING_AGE_I",
        "BUILDING_LOCATION_I",
        "BUILDING_TYPE_I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "area_by_dwelling_type": 1,
        "new_dwelling_stocks": 1,
        "useful_energy_new": 1,
        "unit_conversion_kwh_tj": 1,
    },
)
def useful_energy_by_new_dwelling_type():
    return (
        area_by_dwelling_type()
        * new_dwelling_stocks().transpose(
            "REGIONS_35_I", "BUILDING_TYPE_I", "BUILDING_AGE_I", "BUILDING_LOCATION_I"
        )
        * useful_energy_new()
        * unit_conversion_kwh_tj()
        / 1000
    ).transpose(
        "REGIONS_35_I", "BUILDING_AGE_I", "BUILDING_LOCATION_I", "BUILDING_TYPE_I"
    )


@component.add(
    name="useful_energy_by_renovated_dwellings_type_age",
    subscripts=[
        "REGIONS_35_I",
        "BUILDING_AGE_I",
        "BUILDING_LOCATION_I",
        "BUILDING_TYPE_I",
        "RENOVATION_LEVEL_I",
    ],
    comp_type="Constant",
    comp_subtype="Normal",
)
def useful_energy_by_renovated_dwellings_type_age():
    """
    cummulative renovated dwellings[REGIONS 35 I,BUILDING AGE I,BUILDING LOCATION I,BUILDING TYPE I, RENOVATION LEVEL I]*AREA BY DWELLING TYPE [ REGIONS 35 I,BUILDING TYPE I]*((1-IMPROVEMENT LEVELS FROM RENOVATION[RENOVATION LEVEL I])*USEFUL ENERGY BUILDING EXISTING UNTIL 2015) *UNIT CONVERSION kWh TJ/1000 cummulative renovated dwellings[REGIONS 35 I,BUILDING AGE I,BUILDING LOCATION I,BUILDING TYPE I, RENOVATION LEVEL I]*AREA BY DWELLING TYPE [ REGIONS 35 I,BUILDING TYPE I]*((1-IMPROVEMENT LEVELS FROM RENOVATION[RENOVATION LEVEL I])*USEFUL ENERGY BUILDING EXISTING UNTIL 2015 ) *UNIT CONVERSION kWh TJ/1000
    """
    return xr.DataArray(
        0,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "BUILDING_AGE_I": _subscript_dict["BUILDING_AGE_I"],
            "BUILDING_LOCATION_I": _subscript_dict["BUILDING_LOCATION_I"],
            "BUILDING_TYPE_I": _subscript_dict["BUILDING_TYPE_I"],
            "RENOVATION_LEVEL_I": _subscript_dict["RENOVATION_LEVEL_I"],
        },
        [
            "REGIONS_35_I",
            "BUILDING_AGE_I",
            "BUILDING_LOCATION_I",
            "BUILDING_TYPE_I",
            "RENOVATION_LEVEL_I",
        ],
    )


@component.add(
    name="USEFUL_ENERGY_EXISTING_DWELLINGS_BY_AGE_AND_TYPE_SPACE_COOLING",
    subscripts=[
        "BUILDING_TYPE_I",
        "BUILDING_FEC_USES_I",
        "REGIONS_35_I",
        "BUILDING_AGE_I",
    ],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_useful_energy_existing_dwellings_by_age_and_type_space_cooling"
    },
)
def useful_energy_existing_dwellings_by_age_and_type_space_cooling():
    return (
        _ext_constant_useful_energy_existing_dwellings_by_age_and_type_space_cooling()
    )


_ext_constant_useful_energy_existing_dwellings_by_age_and_type_space_cooling = (
    ExtConstant(
        "model_parameters/energy/energy-end_use-buildings.xlsx",
        "Useful_energy_SC",
        "USEFUL_ENERGY_MULTI_FAMILY_SPACE_COOLING",
        {
            "BUILDING_TYPE_I": ["MULTI_FAMILY"],
            "BUILDING_FEC_USES_I": ["SPACE_COOLING"],
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "BUILDING_AGE_I": _subscript_dict["BUILDING_AGE_I"],
        },
        _root,
        {
            "BUILDING_TYPE_I": _subscript_dict["BUILDING_TYPE_I"],
            "BUILDING_FEC_USES_I": _subscript_dict["BUILDING_FEC_USES_I"],
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "BUILDING_AGE_I": _subscript_dict["BUILDING_AGE_I"],
        },
        "_ext_constant_useful_energy_existing_dwellings_by_age_and_type_space_cooling",
    )
)

_ext_constant_useful_energy_existing_dwellings_by_age_and_type_space_cooling.add(
    "model_parameters/energy/energy-end_use-buildings.xlsx",
    "Useful_energy_SC",
    "USEFUL_ENERGY_SINGLE_FAMILY_SPACE_COOLING",
    {
        "BUILDING_TYPE_I": ["SINGLE_FAMILY"],
        "BUILDING_FEC_USES_I": ["SPACE_COOLING"],
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "BUILDING_AGE_I": _subscript_dict["BUILDING_AGE_I"],
    },
)


@component.add(
    name="USEFUL_ENERGY_EXISTING_DWELLINGS_BY_AGE_AND_TYPE_SPACE_HEATING",
    subscripts=[
        "BUILDING_TYPE_I",
        "BUILDING_FEC_USES_I",
        "REGIONS_35_I",
        "BUILDING_AGE_I",
    ],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_useful_energy_existing_dwellings_by_age_and_type_space_heating"
    },
)
def useful_energy_existing_dwellings_by_age_and_type_space_heating():
    return (
        _ext_constant_useful_energy_existing_dwellings_by_age_and_type_space_heating()
    )


_ext_constant_useful_energy_existing_dwellings_by_age_and_type_space_heating = (
    ExtConstant(
        "model_parameters/energy/energy-end_use-buildings.xlsx",
        "Useful_energy_SH",
        "USEFUL_ENERGY_SPACE_HEATING_MULTI_FAMILY",
        {
            "BUILDING_TYPE_I": ["MULTI_FAMILY"],
            "BUILDING_FEC_USES_I": ["SPACE_HEATING"],
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "BUILDING_AGE_I": _subscript_dict["BUILDING_AGE_I"],
        },
        _root,
        {
            "BUILDING_TYPE_I": _subscript_dict["BUILDING_TYPE_I"],
            "BUILDING_FEC_USES_I": _subscript_dict["BUILDING_FEC_USES_I"],
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "BUILDING_AGE_I": _subscript_dict["BUILDING_AGE_I"],
        },
        "_ext_constant_useful_energy_existing_dwellings_by_age_and_type_space_heating",
    )
)

_ext_constant_useful_energy_existing_dwellings_by_age_and_type_space_heating.add(
    "model_parameters/energy/energy-end_use-buildings.xlsx",
    "Useful_energy_SH",
    "USEFUL_ENERGY_SPACE_HEATING_SINGLE_FAMILY",
    {
        "BUILDING_TYPE_I": ["SINGLE_FAMILY"],
        "BUILDING_FEC_USES_I": ["SPACE_HEATING"],
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "BUILDING_AGE_I": _subscript_dict["BUILDING_AGE_I"],
    },
)


@component.add(
    name="USEFUL_ENERGY_EXISTING_DWELLINGS_BY_TYPE_WATER_HEATING",
    subscripts=["REGIONS_35_I", "BUILDING_TYPE_I", "BUILDING_FEC_USES_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_useful_energy_existing_dwellings_by_type_water_heating"
    },
)
def useful_energy_existing_dwellings_by_type_water_heating():
    return _ext_constant_useful_energy_existing_dwellings_by_type_water_heating()


_ext_constant_useful_energy_existing_dwellings_by_type_water_heating = ExtConstant(
    "model_parameters/energy/energy-end_use-buildings.xlsx",
    "Useful_energy_WH",
    "USEFUL_ENERGY_WATER_HEATING",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "BUILDING_TYPE_I": _subscript_dict["BUILDING_TYPE_I"],
        "BUILDING_FEC_USES_I": ["WATER_HEATING"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "BUILDING_TYPE_I": _subscript_dict["BUILDING_TYPE_I"],
        "BUILDING_FEC_USES_I": _subscript_dict["BUILDING_FEC_USES_I"],
    },
    "_ext_constant_useful_energy_existing_dwellings_by_type_water_heating",
)


@component.add(
    name="USEFUL_ENERGY_NEW",
    units="kWh/m2",
    comp_type="Constant",
    comp_subtype="Normal",
)
def useful_energy_new():
    return 0


@component.add(
    name="useful_energy_not_renovated_water_heating",
    subscripts=[
        "REGIONS_35_I",
        "BUILDING_AGE_I",
        "BUILDING_LOCATION_I",
        "BUILDING_TYPE_I",
        "BUILDING_FEC_USES_I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "intial_dewellings_by_type_age_loc": 1,
        "useful_energy_existing_dwellings_by_type_water_heating": 1,
        "area_by_dwelling_type": 1,
        "unit_conversion_kwh_tj": 1,
    },
)
def useful_energy_not_renovated_water_heating():
    return (
        intial_dewellings_by_type_age_loc()
        * useful_energy_existing_dwellings_by_type_water_heating()
        .loc[:, :, "WATER_HEATING"]
        .reset_coords(drop=True)
        * area_by_dwelling_type()
        * unit_conversion_kwh_tj()
    ).expand_dims({"BUILDING_FEC_USES_I": ["WATER_HEATING"]}, 4)
