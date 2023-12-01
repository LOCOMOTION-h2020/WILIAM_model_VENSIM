"""
Module climate.waste_emissions
Translated using PySD version 3.10.0
"""


@component.add(
    name="CH4_waste_emissions_9R",
    units="Mt/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "ch4_waste_emissions_by_gdp": 1,
        "unit_conversion_kt_gt": 1,
        "unit_conversion_mt_gt": 1,
    },
)
def ch4_waste_emissions_9r():
    """
    CH4_waste_emissions_9R
    """
    return (
        ch4_waste_emissions_by_gdp() / unit_conversion_kt_gt()
    ) * unit_conversion_mt_gt()


@component.add(
    name="CH4_waste_emissions_by_GDP",
    units="Kt/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ch4_waste_emissions_intensity": 1, "gdp_real_9r": 1},
)
def ch4_waste_emissions_by_gdp():
    """
    CH4_waste_emissions_by_GDP
    """
    return ch4_waste_emissions_intensity() * gdp_real_9r()


@component.add(
    name="CH4_WASTE_EMISSIONS_HISTORICAL_DATA",
    units="Kt/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_ch4_waste_emissions_historical_data"},
)
def ch4_waste_emissions_historical_data():
    """
    CH4_WASTE_EMISSIONS_HISTORICAL_DATA
    """
    return _ext_constant_ch4_waste_emissions_historical_data()


_ext_constant_ch4_waste_emissions_historical_data = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "CH4_WASTE_EMISSIONS_HISTORICAL_DATA*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_ch4_waste_emissions_historical_data",
)


@component.add(
    name="CH4_waste_emissions_intensity",
    units="Kt/Mdollars_2015",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ch4_waste_emissions_historical_data": 1, "gdp_real_9r_until_2015": 1},
)
def ch4_waste_emissions_intensity():
    """
    CH4_waste_emissions_intensity
    """
    return ch4_waste_emissions_historical_data() / gdp_real_9r_until_2015()


@component.add(
    name="CO2_waste_emissions_35R",
    units="Gt/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"co2_waste_emissions_by_gdp_35_r": 1, "unit_conversion_kt_gt": 1},
)
def co2_waste_emissions_35r():
    """
    CO2_waste_emissions_35R
    """
    return co2_waste_emissions_by_gdp_35_r() / unit_conversion_kt_gt()


@component.add(
    name="CO2_waste_emissions_9R",
    units="Gt/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"co2_waste_emissions_by_gdp": 1, "unit_conversion_kt_gt": 1},
)
def co2_waste_emissions_9r():
    """
    CO2_waste_emissions_9R
    """
    return co2_waste_emissions_by_gdp() / unit_conversion_kt_gt()


@component.add(
    name="CO2_waste_emissions_by_GDP",
    units="Kt/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"co2_waste_emissions_intensity": 1, "gdp_real_9r": 1},
)
def co2_waste_emissions_by_gdp():
    """
    CO2_waste_emissions_by_GDP
    """
    return co2_waste_emissions_intensity() * gdp_real_9r()


@component.add(
    name="CO2_waste_emissions_by_GDP_35_R",
    units="Kt/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "co2_waste_emissions_intensity_35r": 1,
        "gross_domestic_product_real_supply_side": 1,
    },
)
def co2_waste_emissions_by_gdp_35_r():
    """
    CO2_waste_emissions_by_GDP_35_R
    """
    return (
        co2_waste_emissions_intensity_35r() * gross_domestic_product_real_supply_side()
    )


@component.add(
    name="CO2_waste_emissions_by_sector",
    units="Gt/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={"co2_waste_emissions_35r": 1},
)
def co2_waste_emissions_by_sector():
    """
    CO2_waste_emissions_by_sector
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "SECTORS_I": _subscript_dict["SECTORS_I"],
        },
        ["REGIONS_35_I", "SECTORS_I"],
    )
    value.loc[:, ["WASTE_MANAGEMENT"]] = (
        co2_waste_emissions_35r()
        .expand_dims(
            {"CLUSTER_WATER_AND_WASTE": _subscript_dict["CLUSTER_WATER_AND_WASTE"]}, 1
        )
        .values
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, ["WASTE_MANAGEMENT"]] = False
    value.values[except_subs.values] = 0
    return value


@component.add(
    name="CO2_WASTE_EMISSIONS_HISTORICAL_DATA_35R",
    units="Kt/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_co2_waste_emissions_historical_data_35r"
    },
)
def co2_waste_emissions_historical_data_35r():
    """
    CO2_WASTE_EMISSIONS_HISTORICAL_DATA_35R
    """
    return _ext_constant_co2_waste_emissions_historical_data_35r()


_ext_constant_co2_waste_emissions_historical_data_35r = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "CO2_WASTE_EMISSIONS_HISTORICAL_DATA_35R*",
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    _root,
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    "_ext_constant_co2_waste_emissions_historical_data_35r",
)


@component.add(
    name="CO2_WASTE_EMISSIONS_HISTORICAL_DATA_9R",
    units="Kt/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_co2_waste_emissions_historical_data_9r"},
)
def co2_waste_emissions_historical_data_9r():
    """
    CO2_WASTE_EMISSIONS_HISTORICAL_DATA
    """
    return _ext_constant_co2_waste_emissions_historical_data_9r()


_ext_constant_co2_waste_emissions_historical_data_9r = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "CO2_WASTE_EMISSIONS_HISTORICAL_DATA*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_co2_waste_emissions_historical_data_9r",
)


@component.add(
    name="CO2_waste_emissions_intensity",
    units="Kt/Mdollars_2015",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "co2_waste_emissions_historical_data_9r": 1,
        "gdp_real_9r_until_2015": 1,
    },
)
def co2_waste_emissions_intensity():
    """
    CO2_waste_emissions_intensity
    """
    return co2_waste_emissions_historical_data_9r() / gdp_real_9r_until_2015()


@component.add(
    name="CO2_waste_emissions_intensity_35R",
    units="Kt/Mdollars_2015",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "co2_waste_emissions_historical_data_35r": 1,
        "gdp_real_35r_until_2015": 1,
    },
)
def co2_waste_emissions_intensity_35r():
    """
    CO2_waste_emissions_intensity_35R
    """
    return co2_waste_emissions_historical_data_35r() / gdp_real_35r_until_2015()


@component.add(
    name="GHG_waste_emissions_9R",
    units="Gt/Year",
    subscripts=["REGIONS_9_I", "GHG_ENERGY_USE_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "co2_waste_emissions_9r": 1,
        "unit_conversion_mt_gt": 2,
        "ch4_waste_emissions_9r": 1,
        "n2o_waste_emissions_9r": 1,
    },
)
def ghg_waste_emissions_9r():
    """
    GHG_waste_emissions_9R
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "GHG_ENERGY_USE_I": _subscript_dict["GHG_ENERGY_USE_I"],
        },
        ["REGIONS_9_I", "GHG_ENERGY_USE_I"],
    )
    value.loc[:, ["CO2"]] = (
        co2_waste_emissions_9r().expand_dims({"GHG_ENERGY_USE_I": ["CO2"]}, 1).values
    )
    value.loc[:, ["CH4"]] = (
        (ch4_waste_emissions_9r() * unit_conversion_mt_gt())
        .expand_dims({"GHG_ENERGY_USE_I": ["CH4"]}, 1)
        .values
    )
    value.loc[:, ["N2O"]] = (
        (n2o_waste_emissions_9r() * unit_conversion_mt_gt())
        .expand_dims({"GHG_ENERGY_USE_I": ["N2O"]}, 1)
        .values
    )
    return value


@component.add(
    name="N2O_waste_emissions_9R",
    units="Mt/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "n2o_waste_emissions_by_gdp": 1,
        "unit_conversion_kt_gt": 1,
        "unit_conversion_mt_gt": 1,
    },
)
def n2o_waste_emissions_9r():
    """
    N2O_waste_emissions_9R
    """
    return (
        n2o_waste_emissions_by_gdp() / unit_conversion_kt_gt()
    ) * unit_conversion_mt_gt()


@component.add(
    name="N2O_waste_emissions_by_GDP",
    units="Kt/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"n2o_waste_emissions_intensity": 1, "gdp_real_9r": 1},
)
def n2o_waste_emissions_by_gdp():
    """
    N2O_waste_emissions_by_GDP
    """
    return n2o_waste_emissions_intensity() * gdp_real_9r()


@component.add(
    name="N2O_WASTE_EMISSIONS_HISTORICAL_DATA",
    units="Kt/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_n2o_waste_emissions_historical_data"},
)
def n2o_waste_emissions_historical_data():
    """
    N2O_WASTE_EMISSIONS_HISTORICAL_DATA
    """
    return _ext_constant_n2o_waste_emissions_historical_data()


_ext_constant_n2o_waste_emissions_historical_data = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "N2O_WASTE_EMISSIONS_HISTORICAL_DATA*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_n2o_waste_emissions_historical_data",
)


@component.add(
    name="N2O_waste_emissions_intensity",
    units="Kt/Mdollars_2015",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"n2o_waste_emissions_historical_data": 1, "gdp_real_9r_until_2015": 1},
)
def n2o_waste_emissions_intensity():
    """
    N2O_waste_emissions_intensity
    """
    return n2o_waste_emissions_historical_data() / gdp_real_9r_until_2015()


@component.add(
    name="total_GHG_waste_emissions",
    units="Gt/Year",
    subscripts=["GHG_ENERGY_USE_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ghg_waste_emissions_9r": 1},
)
def total_ghg_waste_emissions():
    """
    total_GHG_waste_emissions
    """
    return sum(
        ghg_waste_emissions_9r().rename({"REGIONS_9_I": "REGIONS_9_I!"}),
        dim=["REGIONS_9_I!"],
    )
