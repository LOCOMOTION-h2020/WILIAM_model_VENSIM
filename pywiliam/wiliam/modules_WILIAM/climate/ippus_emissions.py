"""
Module climate.ippus_emissions
Translated using PySD version 3.10.0
"""


@component.add(
    name="aux_GDP_real_35R_until_2015",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_aux_gdp_real_35r_until_2015": 1},
    other_deps={
        "_delayfixed_aux_gdp_real_35r_until_2015": {
            "initial": {"time_step": 1},
            "step": {"gdp_real_35r_until_2015": 1},
        }
    },
)
def aux_gdp_real_35r_until_2015():
    """
    Auxiliary variable to estimate the GDPpc in the year 2015. The method is not mathematically exact, but the error tends to 0 when the TIME STEP decreases.
    """
    return _delayfixed_aux_gdp_real_35r_until_2015()


_delayfixed_aux_gdp_real_35r_until_2015 = DelayFixed(
    lambda: gdp_real_35r_until_2015(),
    lambda: time_step(),
    lambda: xr.DataArray(
        0, {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]}, ["REGIONS_35_I"]
    ),
    time_step,
    "_delayfixed_aux_gdp_real_35r_until_2015",
)


@component.add(
    name="aux_GDP_real_9R_until_2015",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_aux_gdp_real_9r_until_2015": 1},
    other_deps={
        "_delayfixed_aux_gdp_real_9r_until_2015": {
            "initial": {"time_step": 1},
            "step": {"gdp_real_9r_until_2015": 1},
        }
    },
)
def aux_gdp_real_9r_until_2015():
    """
    Auxiliary variable to estimate the GDPpc in the year 2015. The method is not mathematically exact, but the error tends to 0 when the TIME STEP decreases.
    """
    return _delayfixed_aux_gdp_real_9r_until_2015()


_delayfixed_aux_gdp_real_9r_until_2015 = DelayFixed(
    lambda: gdp_real_9r_until_2015(),
    lambda: time_step(),
    lambda: xr.DataArray(
        0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
    ),
    time_step,
    "_delayfixed_aux_gdp_real_9r_until_2015",
)


@component.add(
    name="CH4_chemical_industry_emissions_by_GDP",
    units="Kt/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "ch4_chemical_industry_emissions_intensity": 1,
        "gross_domestic_product_real_supply_side": 1,
    },
)
def ch4_chemical_industry_emissions_by_gdp():
    """
    The calculation of CH4 chemical industry emissions by using the GDP trends.
    """
    return (
        ch4_chemical_industry_emissions_intensity()
        * gross_domestic_product_real_supply_side()
    )


@component.add(
    name="CH4_CHEMICAL_INDUSTRY_EMISSIONS_HISTORICAL_DATA",
    units="Kt/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_ch4_chemical_industry_emissions_historical_data"
    },
)
def ch4_chemical_industry_emissions_historical_data():
    """
    Historical data of CH4 emissions of chemical industry for 35 regions, EDGAR DATABASE
    """
    return _ext_constant_ch4_chemical_industry_emissions_historical_data()


_ext_constant_ch4_chemical_industry_emissions_historical_data = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "CH4_CHEMICAL_INDUSTRY_EMISSIONS_HISTORICAL_DATA*",
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    _root,
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    "_ext_constant_ch4_chemical_industry_emissions_historical_data",
)


@component.add(
    name="CH4_chemical_industry_emissions_intensity",
    units="Kt/Mdollars_2015",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "ch4_chemical_industry_emissions_historical_data": 1,
        "gdp_real_35r_until_2015": 1,
    },
)
def ch4_chemical_industry_emissions_intensity():
    """
    the calculation of CH4 chemical industry emissions intensity for the year 2015.
    """
    return ch4_chemical_industry_emissions_historical_data() / gdp_real_35r_until_2015()


@component.add(
    name="CH4_IPPUs_emissions_9R",
    units="Gt/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ch4_ipuus_emissions_35r": 2},
)
def ch4_ippus_emissions_9r():
    """
    CH4_IPPUs_emissions_9R
    """
    value = xr.DataArray(
        np.nan, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
    )
    value.loc[_subscript_dict["REGIONS_8_I"]] = (
        ch4_ipuus_emissions_35r()
        .loc[_subscript_dict["REGIONS_8_I"]]
        .rename({"REGIONS_35_I": "REGIONS_8_I"})
        .values
    )
    value.loc[["EU27"]] = sum(
        ch4_ipuus_emissions_35r()
        .loc[_subscript_dict["REGIONS_EU27_I"]]
        .rename({"REGIONS_35_I": "REGIONS_EU27_I!"}),
        dim=["REGIONS_EU27_I!"],
    )
    return value


@component.add(
    name="CH4_IPPUs_emissions_by_sectors",
    units="Gt/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "ch4_chemical_industry_emissions_by_gdp": 1,
        "unit_conversion_kt_gt": 2,
        "ch4_metal_industry_emissions_by_gdp": 1,
    },
)
def ch4_ippus_emissions_by_sectors():
    """
    CH4 IPPUs emissions by region and sector
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "SECTORS_I": _subscript_dict["SECTORS_I"],
        },
        ["REGIONS_35_I", "SECTORS_I"],
    )
    value.loc[:, ["MANUFACTURE_CHEMICAL"]] = (
        (ch4_chemical_industry_emissions_by_gdp() / unit_conversion_kt_gt())
        .expand_dims({"CLUSTER_CHEMICALS": _subscript_dict["CLUSTER_CHEMICALS"]}, 1)
        .values
    )
    value.loc[:, ["MINING_AND_MANUFACTURING_IRON"]] = (
        (ch4_metal_industry_emissions_by_gdp() / unit_conversion_kt_gt())
        .expand_dims({"CLUSTER_MINNING": ["MINING_AND_MANUFACTURING_IRON"]}, 1)
        .values
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, ["MANUFACTURE_CHEMICAL"]] = False
    except_subs.loc[:, ["MINING_AND_MANUFACTURING_IRON"]] = False
    value.values[except_subs.values] = 0
    return value


@component.add(
    name="CH4_IPUUs_emissions_35R",
    units="Gt/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "ch4_chemical_industry_emissions_by_gdp": 1,
        "ch4_metal_industry_emissions_by_gdp": 1,
        "unit_conversion_kt_gt": 1,
    },
)
def ch4_ipuus_emissions_35r():
    """
    CH4 IPPUs emissions by region
    """
    return (
        ch4_chemical_industry_emissions_by_gdp() + ch4_metal_industry_emissions_by_gdp()
    ) / unit_conversion_kt_gt()


@component.add(
    name="CH4_metal_industry_emissions_by_GDP",
    units="Kt/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "ch4_metal_industry_emissions_intensity": 1,
        "gross_domestic_product_real_supply_side": 1,
    },
)
def ch4_metal_industry_emissions_by_gdp():
    """
    The calculation of CH4 metal industry emissions by using the GDP trends.
    """
    return (
        ch4_metal_industry_emissions_intensity()
        * gross_domestic_product_real_supply_side()
    )


@component.add(
    name="CH4_METAL_INDUSTRY_EMISSIONS_HISTORICAL_DATA",
    units="Kt/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_ch4_metal_industry_emissions_historical_data"
    },
)
def ch4_metal_industry_emissions_historical_data():
    """
    Historical data of CO2 emissions of metal industry for 35 regions, EDGAR DATABASE
    """
    return _ext_constant_ch4_metal_industry_emissions_historical_data()


_ext_constant_ch4_metal_industry_emissions_historical_data = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "CH4_METAL_INDUSTRY_EMISSIONS_HISTORICAL_DATA*",
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    _root,
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    "_ext_constant_ch4_metal_industry_emissions_historical_data",
)


@component.add(
    name="CH4_metal_industry_emissions_intensity",
    units="Kt/Mdollars_2015",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "ch4_metal_industry_emissions_historical_data": 1,
        "gdp_real_35r_until_2015": 1,
    },
)
def ch4_metal_industry_emissions_intensity():
    """
    the calculation of CH4 metal industry emissions intensity for the year 2015.
    """
    return ch4_metal_industry_emissions_historical_data() / gdp_real_35r_until_2015()


@component.add(
    name="CO2_cement_production_emissions_by_GDP",
    units="Kt/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "co2_cement_production_emissions_intensity": 1,
        "gross_domestic_product_real_supply_side": 1,
    },
)
def co2_cement_production_emissions_by_gdp():
    """
    The calculation of CO2 cement production emissions by using the GDP trends.
    """
    return (
        co2_cement_production_emissions_intensity()
        * gross_domestic_product_real_supply_side()
    )


@component.add(
    name="CO2_CEMENT_PRODUCTION_EMISSIONS_HISTORICAL_DATA",
    units="Kt/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_co2_cement_production_emissions_historical_data"
    },
)
def co2_cement_production_emissions_historical_data():
    """
    Historical data of CO2 emissions of cement production for 35 regions. EDGAR DATABASE
    """
    return _ext_constant_co2_cement_production_emissions_historical_data()


_ext_constant_co2_cement_production_emissions_historical_data = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "CO2_EMISSIONS_CEMENT_PRODUCTION_HISTORICAL_DATA*",
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    _root,
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    "_ext_constant_co2_cement_production_emissions_historical_data",
)


@component.add(
    name="CO2_cement_production_emissions_intensity",
    units="Kt/Mdollars_2015",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "co2_cement_production_emissions_historical_data": 1,
        "gdp_real_35r_until_2015": 1,
    },
)
def co2_cement_production_emissions_intensity():
    """
    the calculation of CO2 cement production emissions intensity for the year 2015.
    """
    return co2_cement_production_emissions_historical_data() / gdp_real_35r_until_2015()


@component.add(
    name="CO2_chemical_industry_emissions_by_GDP",
    units="Kt/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "co2_chemical_industry_emissions_intensity": 1,
        "gross_domestic_product_real_supply_side": 1,
    },
)
def co2_chemical_industry_emissions_by_gdp():
    """
    The calculation of CO2 chemical industry emissions by using the GDP trends.
    """
    return (
        co2_chemical_industry_emissions_intensity()
        * gross_domestic_product_real_supply_side()
    )


@component.add(
    name="CO2_CHEMICAL_INDUSTRY_EMISSIONS_HISTORICAL_DATA",
    units="Kt/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_co2_chemical_industry_emissions_historical_data"
    },
)
def co2_chemical_industry_emissions_historical_data():
    """
    Historical data of CO2 emissions of chemical industry for 35 regions. EDGAR DATABASE
    """
    return _ext_constant_co2_chemical_industry_emissions_historical_data()


_ext_constant_co2_chemical_industry_emissions_historical_data = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "CO2_CHEMICAL_INDUSTRY_EMISSIONS_HISTORICAL_DATA*",
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    _root,
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    "_ext_constant_co2_chemical_industry_emissions_historical_data",
)


@component.add(
    name="CO2_chemical_industry_emissions_intensity",
    units="Kt/Mdollars_2015",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "co2_chemical_industry_emissions_historical_data": 1,
        "gdp_real_35r_until_2015": 1,
    },
)
def co2_chemical_industry_emissions_intensity():
    """
    the calculation of CO2 chemical industry emissions intensity for the year 2015.
    """
    return co2_chemical_industry_emissions_historical_data() / gdp_real_35r_until_2015()


@component.add(
    name="CO2_glass_production_emissions_by_GDP",
    units="Kt/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "co2_glass_production_emissions_intensity": 1,
        "gross_domestic_product_real_supply_side": 1,
    },
)
def co2_glass_production_emissions_by_gdp():
    """
    CO2_glass_production_emissions_by_GDP
    """
    return (
        co2_glass_production_emissions_intensity()
        * gross_domestic_product_real_supply_side()
    )


@component.add(
    name="CO2_GLASS_PRODUCTION_EMISSIONS_HISTORICAL_DATA",
    units="Kt/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_co2_glass_production_emissions_historical_data"
    },
)
def co2_glass_production_emissions_historical_data():
    """
    Historical data of CO2 emissions of glass production for 35 regions. EDGAR DATABASE
    """
    return _ext_constant_co2_glass_production_emissions_historical_data()


_ext_constant_co2_glass_production_emissions_historical_data = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "CO2_GLASS_PRODUCTION_EMISSIONS_HISTORICAL_DATA*",
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    _root,
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    "_ext_constant_co2_glass_production_emissions_historical_data",
)


@component.add(
    name="CO2_glass_production_emissions_intensity",
    units="Kt/Mdollars_2015",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "co2_glass_production_emissions_historical_data": 1,
        "gdp_real_35r_until_2015": 1,
    },
)
def co2_glass_production_emissions_intensity():
    """
    CO2_glass_production_emissions_intensity
    """
    return co2_glass_production_emissions_historical_data() / gdp_real_35r_until_2015()


@component.add(
    name="CO2_IPPUs_emissions_9R",
    units="Gt/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"co2_ipuus_emissions_35r": 2},
)
def co2_ippus_emissions_9r():
    """
    CO2_IPPUs_emissions_9R
    """
    value = xr.DataArray(
        np.nan, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
    )
    value.loc[_subscript_dict["REGIONS_8_I"]] = (
        co2_ipuus_emissions_35r()
        .loc[_subscript_dict["REGIONS_8_I"]]
        .rename({"REGIONS_35_I": "REGIONS_8_I"})
        .values
    )
    value.loc[["EU27"]] = sum(
        co2_ipuus_emissions_35r()
        .loc[_subscript_dict["REGIONS_EU27_I"]]
        .rename({"REGIONS_35_I": "REGIONS_EU27_I!"}),
        dim=["REGIONS_EU27_I!"],
    )
    return value


@component.add(
    name="CO2_IPPUs_emissions_by_sectors",
    units="Gt/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "co2_cement_production_emissions_by_gdp": 1,
        "co2_lime_production_emissions_by_gdp": 1,
        "unit_conversion_kt_gt": 4,
        "co2_chemical_industry_emissions_by_gdp": 1,
        "co2_non_energy_products_from_fuels_and_solvent_use_emissions_by_gdp": 1,
        "co2_other_process_uses_of_carbonates_emissions_by_gdp": 1,
        "co2_metal_industry_emissions_by_gdp": 1,
        "co2_glass_production_emissions_by_gdp": 1,
    },
)
def co2_ippus_emissions_by_sectors():
    """
    CO2 IPPUs emissions by region and sector
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "SECTORS_I": _subscript_dict["SECTORS_I"],
        },
        ["REGIONS_35_I", "SECTORS_I"],
    )
    value.loc[:, ["MANUFACTURE_OTHER_NON_METAL"]] = (
        (
            (
                co2_cement_production_emissions_by_gdp()
                + co2_lime_production_emissions_by_gdp()
            )
            / unit_conversion_kt_gt()
        )
        .expand_dims({"CLUSTER_MINNING": ["MANUFACTURE_OTHER_NON_METAL"]}, 1)
        .values
    )
    value.loc[:, ["MANUFACTURE_CHEMICAL"]] = (
        (
            (
                co2_chemical_industry_emissions_by_gdp()
                + co2_non_energy_products_from_fuels_and_solvent_use_emissions_by_gdp()
                + co2_other_process_uses_of_carbonates_emissions_by_gdp()
            )
            / unit_conversion_kt_gt()
        )
        .expand_dims({"CLUSTER_CHEMICALS": _subscript_dict["CLUSTER_CHEMICALS"]}, 1)
        .values
    )
    value.loc[:, ["MINING_AND_MANUFACTURING_IRON"]] = (
        (co2_metal_industry_emissions_by_gdp() / unit_conversion_kt_gt())
        .expand_dims({"CLUSTER_MINNING": ["MINING_AND_MANUFACTURING_IRON"]}, 1)
        .values
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, ["MANUFACTURE_OTHER_NON_METAL"]] = False
    except_subs.loc[:, ["MANUFACTURE_CHEMICAL"]] = False
    except_subs.loc[:, ["MINING_AND_MANUFACTURING_IRON"]] = False
    except_subs.loc[:, ["MANUFACTURE_OTHER"]] = False
    value.values[except_subs.values] = 0
    value.loc[:, ["MANUFACTURE_OTHER"]] = (
        (co2_glass_production_emissions_by_gdp() / unit_conversion_kt_gt())
        .expand_dims({"CLUSTER_OTHER_MANUFACTURES": ["MANUFACTURE_OTHER"]}, 1)
        .values
    )
    return value


@component.add(
    name="CO2_IPPUs_emissions_global",
    units="Gt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"co2_ipuus_emissions_35r": 1},
)
def co2_ippus_emissions_global():
    """
    Global estimation of CO2 IPPUs emissions
    """
    return sum(
        co2_ipuus_emissions_35r().rename({"REGIONS_35_I": "REGIONS_35_I!"}),
        dim=["REGIONS_35_I!"],
    )


@component.add(
    name="CO2_IPUUs_emissions_35R",
    units="Gt/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "co2_cement_production_emissions_by_gdp": 1,
        "co2_chemical_industry_emissions_by_gdp": 1,
        "co2_lime_production_emissions_by_gdp": 1,
        "co2_metal_industry_emissions_by_gdp": 1,
        "co2_non_energy_products_from_fuels_and_solvent_use_emissions_by_gdp": 1,
        "co2_other_process_uses_of_carbonates_emissions_by_gdp": 1,
        "co2_glass_production_emissions_by_gdp": 1,
        "unit_conversion_kt_gt": 1,
    },
)
def co2_ipuus_emissions_35r():
    """
    CO2 IPPUs emissions by region
    """
    return (
        co2_cement_production_emissions_by_gdp()
        + co2_chemical_industry_emissions_by_gdp()
        + co2_lime_production_emissions_by_gdp()
        + co2_metal_industry_emissions_by_gdp()
        + co2_non_energy_products_from_fuels_and_solvent_use_emissions_by_gdp()
        + co2_other_process_uses_of_carbonates_emissions_by_gdp()
        + co2_glass_production_emissions_by_gdp()
    ) / unit_conversion_kt_gt()


@component.add(
    name="CO2_lime_production_emissions_by_GDP",
    units="Kt/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "co2_lime_production_emissions_intensity": 1,
        "gross_domestic_product_real_supply_side": 1,
    },
)
def co2_lime_production_emissions_by_gdp():
    """
    The calculation of CO2 lime production emissions by using the GDP trends.
    """
    return (
        co2_lime_production_emissions_intensity()
        * gross_domestic_product_real_supply_side()
    )


@component.add(
    name="CO2_LIME_PRODUCTION_EMISSIONS_HISTORICAL_DATA",
    units="Kt/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_co2_lime_production_emissions_historical_data"
    },
)
def co2_lime_production_emissions_historical_data():
    """
    Historical data of CO2 emissions of lime production for 35 regions, EDGAR DATABASE
    """
    return _ext_constant_co2_lime_production_emissions_historical_data()


_ext_constant_co2_lime_production_emissions_historical_data = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "CO2_LIME_PRODUCTION_EMISSIONS_HISTORICAL_DATA*",
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    _root,
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    "_ext_constant_co2_lime_production_emissions_historical_data",
)


@component.add(
    name="CO2_lime_production_emissions_intensity",
    units="Kt/Mdollars_2015",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "co2_lime_production_emissions_historical_data": 1,
        "gdp_real_35r_until_2015": 1,
    },
)
def co2_lime_production_emissions_intensity():
    """
    the calculation of CO2 lime production emissions intensity for the year 2015.
    """
    return co2_lime_production_emissions_historical_data() / gdp_real_35r_until_2015()


@component.add(
    name="CO2_metal_industry_emissions_by_GDP",
    units="Kt/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "co2_metal_industry_emissions_intensity": 1,
        "gross_domestic_product_real_supply_side": 1,
    },
)
def co2_metal_industry_emissions_by_gdp():
    """
    The calculation of CO2 metal industry emissions by using the GDP trends.
    """
    return (
        co2_metal_industry_emissions_intensity()
        * gross_domestic_product_real_supply_side()
    )


@component.add(
    name="CO2_METAL_INDUSTRY_EMISSIONS_HISTORICAL_DATA",
    units="Kt/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_co2_metal_industry_emissions_historical_data"
    },
)
def co2_metal_industry_emissions_historical_data():
    """
    Historical data of CO2 emissions of metal industry for 35 regions, EDGAR DATABASE
    """
    return _ext_constant_co2_metal_industry_emissions_historical_data()


_ext_constant_co2_metal_industry_emissions_historical_data = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "CO2_METAL_PRODUCTION_EMISSIONS_HISTORICAL_DATA*",
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    _root,
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    "_ext_constant_co2_metal_industry_emissions_historical_data",
)


@component.add(
    name="CO2_metal_industry_emissions_intensity",
    units="Kt/Mdollars_2015",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "co2_metal_industry_emissions_historical_data": 1,
        "gdp_real_35r_until_2015": 1,
    },
)
def co2_metal_industry_emissions_intensity():
    """
    the calculation of CO2 meal industry emissions intensity for the year 2015.
    """
    return co2_metal_industry_emissions_historical_data() / gdp_real_35r_until_2015()


@component.add(
    name="CO2_non_energy_products_from_fuels_and_solvent_use_emissions_by_GDP",
    units="Kt/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "co2_non_energy_products_from_fuels_and_solvent_use_emissions_intensity": 1,
        "gross_domestic_product_real_supply_side": 1,
    },
)
def co2_non_energy_products_from_fuels_and_solvent_use_emissions_by_gdp():
    """
    The calculation of CO2 non energy products from fuels and solvent use emissions by using the GDP trends.
    """
    return (
        co2_non_energy_products_from_fuels_and_solvent_use_emissions_intensity()
        * gross_domestic_product_real_supply_side()
    )


@component.add(
    name="CO2_NON_ENERGY_PRODUCTS_FROM_FUELS_AND_SOLVENT_USE_EMISSIONS_HISTORICAL_DATA",
    units="Kt/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_co2_non_energy_products_from_fuels_and_solvent_use_emissions_historical_data"
    },
)
def co2_non_energy_products_from_fuels_and_solvent_use_emissions_historical_data():
    """
    Historical data of CO2 emissions of no energy products from fuels and solvent use for 35 regions, EDGAR DATABASE
    """
    return (
        _ext_constant_co2_non_energy_products_from_fuels_and_solvent_use_emissions_historical_data()
    )


_ext_constant_co2_non_energy_products_from_fuels_and_solvent_use_emissions_historical_data = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "CO2_NON_ENERGY_PRODUCTS_FROM_FUELS_AND_SOLVENT_USE_EMISSIONS_HISTORICAL_DATA*",
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    _root,
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    "_ext_constant_co2_non_energy_products_from_fuels_and_solvent_use_emissions_historical_data",
)


@component.add(
    name="CO2_non_energy_products_from_fuels_and_solvent_use_emissions_intensity",
    units="Kt/Mdollars_2015",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "co2_non_energy_products_from_fuels_and_solvent_use_emissions_historical_data": 1,
        "gdp_real_35r_until_2015": 1,
    },
)
def co2_non_energy_products_from_fuels_and_solvent_use_emissions_intensity():
    """
    the calculation of CO2 non energy products from fuels and solvent use emissions intensity for the year 2015.
    """
    return (
        co2_non_energy_products_from_fuels_and_solvent_use_emissions_historical_data()
        / gdp_real_35r_until_2015()
    )


@component.add(
    name="CO2_other_process_uses_of_carbonates_emissions_by_GDP",
    units="Kt/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "co2_other_process_uses_of_carbonates_emissions_intensity": 1,
        "gross_domestic_product_real_supply_side": 1,
    },
)
def co2_other_process_uses_of_carbonates_emissions_by_gdp():
    """
    The calculation of CO2 other process uses of carbonates emissions by using the GDP trends.
    """
    return (
        co2_other_process_uses_of_carbonates_emissions_intensity()
        * gross_domestic_product_real_supply_side()
    )


@component.add(
    name="CO2_OTHER_PROCESS_USES_OF_CARBONATES_EMISSIONS_HISTORICAL_DATA",
    units="Kt/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_co2_other_process_uses_of_carbonates_emissions_historical_data"
    },
)
def co2_other_process_uses_of_carbonates_emissions_historical_data():
    """
    Historical data of CO2 emissions of other process uses of carbonates for 35 regions, EDGAR DATABASE
    """
    return (
        _ext_constant_co2_other_process_uses_of_carbonates_emissions_historical_data()
    )


_ext_constant_co2_other_process_uses_of_carbonates_emissions_historical_data = (
    ExtConstant(
        "model_parameters/climate/climate.xlsx",
        "World",
        "CO2_OTHER_PROCESS_USES_OF_CARBONATES_EMISSIONS_HISTORICAL_DATA*",
        {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
        _root,
        {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
        "_ext_constant_co2_other_process_uses_of_carbonates_emissions_historical_data",
    )
)


@component.add(
    name="CO2_other_process_uses_of_carbonates_emissions_intensity",
    units="Kt/Mdollars_2015",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "co2_other_process_uses_of_carbonates_emissions_historical_data": 1,
        "gdp_real_35r_until_2015": 1,
    },
)
def co2_other_process_uses_of_carbonates_emissions_intensity():
    """
    the calculation of CO2 other process uses of carbonates emissions intensity for the year 2015.
    """
    return (
        co2_other_process_uses_of_carbonates_emissions_historical_data()
        / gdp_real_35r_until_2015()
    )


@component.add(
    name="GDP_real_35R_until_2015",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "aux_gdp_real_35r_until_2015": 1,
        "gross_domestic_product_real_supply_side": 1,
    },
)
def gdp_real_35r_until_2015():
    """
    GDPpc until the year 2015.
    """
    return if_then_else(
        time() > 2015,
        lambda: aux_gdp_real_35r_until_2015(),
        lambda: gross_domestic_product_real_supply_side(),
    )


@component.add(
    name="GDP_real_9R_until_2015",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "aux_gdp_real_9r_until_2015": 1, "gdp_real_9r": 1},
)
def gdp_real_9r_until_2015():
    """
    GDPpc until the year 2015.
    """
    return if_then_else(
        time() > 2015, lambda: aux_gdp_real_9r_until_2015(), lambda: gdp_real_9r()
    )


@component.add(
    name="GHG_IPPUs_emissions_9R",
    units="Gt/Year",
    subscripts=["REGIONS_9_I", "GHG_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "co2_ippus_emissions_9r": 1,
        "ch4_ippus_emissions_9r": 1,
        "n2o_ippus_emissions_9r": 1,
        "rest_of_ghg_ippus_emissions_9r": 1,
    },
)
def ghg_ippus_emissions_9r():
    """
    GHG_IPPUs_emissions_9R
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "GHG_I": _subscript_dict["GHG_I"],
        },
        ["REGIONS_9_I", "GHG_I"],
    )
    value.loc[:, ["CO2"]] = (
        co2_ippus_emissions_9r().expand_dims({"GHG_ENERGY_USE_I": ["CO2"]}, 1).values
    )
    value.loc[:, ["CH4"]] = (
        ch4_ippus_emissions_9r().expand_dims({"GHG_ENERGY_USE_I": ["CH4"]}, 1).values
    )
    value.loc[:, ["N2O"]] = (
        n2o_ippus_emissions_9r().expand_dims({"GHG_ENERGY_USE_I": ["N2O"]}, 1).values
    )
    value.loc[
        :, _subscript_dict["GHG_REST_I"]
    ] = rest_of_ghg_ippus_emissions_9r().values
    return value


@component.add(
    name="N2O_chemical_industry_emissions_by_GDP",
    units="Kt/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "n2o_chemical_industry_emissions_intensity": 1,
        "gross_domestic_product_real_supply_side": 1,
    },
)
def n2o_chemical_industry_emissions_by_gdp():
    """
    The calculation of N2O chemical industry emissions by using the GDP trends.
    """
    return (
        n2o_chemical_industry_emissions_intensity()
        * gross_domestic_product_real_supply_side()
    )


@component.add(
    name="N2O_CHEMICAL_INDUSTRY_EMISSIONS_HISTORICAL_DATA",
    units="Kt/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_n2o_chemical_industry_emissions_historical_data"
    },
)
def n2o_chemical_industry_emissions_historical_data():
    """
    Historical data of N2O emissions of chemical industry for 35 regions, EDGAR DATABASE
    """
    return _ext_constant_n2o_chemical_industry_emissions_historical_data()


_ext_constant_n2o_chemical_industry_emissions_historical_data = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "N2O_CHEMICAL_INDUSTRY_EMISSIONS_HISTORICAL_DATA*",
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    _root,
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    "_ext_constant_n2o_chemical_industry_emissions_historical_data",
)


@component.add(
    name="N2O_chemical_industry_emissions_intensity",
    units="Kt/Mdollars_2015",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "n2o_chemical_industry_emissions_historical_data": 1,
        "gdp_real_35r_until_2015": 1,
    },
)
def n2o_chemical_industry_emissions_intensity():
    return n2o_chemical_industry_emissions_historical_data() / gdp_real_35r_until_2015()


@component.add(
    name="N2O_IPPUs_emissions_9R",
    units="Gt/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"n2o_ipuus_emissions_35r": 2},
)
def n2o_ippus_emissions_9r():
    """
    N2O_IPPUs_emissions_9R
    """
    value = xr.DataArray(
        np.nan, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
    )
    value.loc[_subscript_dict["REGIONS_8_I"]] = (
        n2o_ipuus_emissions_35r()
        .loc[_subscript_dict["REGIONS_8_I"]]
        .rename({"REGIONS_35_I": "REGIONS_8_I"})
        .values
    )
    value.loc[["EU27"]] = sum(
        n2o_ipuus_emissions_35r()
        .loc[_subscript_dict["REGIONS_EU27_I"]]
        .rename({"REGIONS_35_I": "REGIONS_EU27_I!"}),
        dim=["REGIONS_EU27_I!"],
    )
    return value


@component.add(
    name="N2O_IPPUs_emissions_by_sectors",
    units="Gt/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "n2o_chemical_industry_emissions_by_gdp": 1,
        "n2o_other_product_manufacture_and_use_emissions_by_gdp": 1,
        "unit_conversion_kt_gt": 1,
    },
)
def n2o_ippus_emissions_by_sectors():
    """
    N2O IPPUs emissions by region and sector
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "SECTORS_I": _subscript_dict["SECTORS_I"],
        },
        ["REGIONS_35_I", "SECTORS_I"],
    )
    value.loc[:, ["MANUFACTURE_CHEMICAL"]] = (
        (
            (
                n2o_chemical_industry_emissions_by_gdp()
                + n2o_other_product_manufacture_and_use_emissions_by_gdp()
            )
            / unit_conversion_kt_gt()
        )
        .expand_dims({"CLUSTER_CHEMICALS": _subscript_dict["CLUSTER_CHEMICALS"]}, 1)
        .values
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, ["MANUFACTURE_CHEMICAL"]] = False
    value.values[except_subs.values] = 0
    return value


@component.add(
    name="N2O_IPUUs_emissions_35R",
    units="Gt/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "n2o_chemical_industry_emissions_by_gdp": 1,
        "n2o_other_product_manufacture_and_use_emissions_by_gdp": 1,
        "unit_conversion_kt_gt": 1,
    },
)
def n2o_ipuus_emissions_35r():
    """
    N2O IPPUs emissions by region
    """
    return (
        n2o_chemical_industry_emissions_by_gdp()
        + n2o_other_product_manufacture_and_use_emissions_by_gdp()
    ) / unit_conversion_kt_gt()


@component.add(
    name="N2O_other_product_manufacture_and_use_emissions_by_GDP",
    units="Kt/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "n2o_other_product_manufacture_and_use_emissions_intensity": 1,
        "gross_domestic_product_real_supply_side": 1,
    },
)
def n2o_other_product_manufacture_and_use_emissions_by_gdp():
    """
    The calculation of N2O other product manufacture and use emissions by using the GDP trends.
    """
    return (
        n2o_other_product_manufacture_and_use_emissions_intensity()
        * gross_domestic_product_real_supply_side()
    )


@component.add(
    name="N2O_OTHER_PRODUCT_MANUFACTURE_AND_USE_EMISSIONS_HISTORICAL_DATA",
    units="Kt/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_n2o_other_product_manufacture_and_use_emissions_historical_data"
    },
)
def n2o_other_product_manufacture_and_use_emissions_historical_data():
    """
    Historical data of N2O emissions of other product manufacture and use for 35 regions, EDGAR DATABASE
    """
    return (
        _ext_constant_n2o_other_product_manufacture_and_use_emissions_historical_data()
    )


_ext_constant_n2o_other_product_manufacture_and_use_emissions_historical_data = (
    ExtConstant(
        "model_parameters/climate/climate.xlsx",
        "World",
        "N2O_OTHER_PRODUCT_MANUFACTURE_AND_USE_EMISSIONS_HISTORICAL_DATA*",
        {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
        _root,
        {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
        "_ext_constant_n2o_other_product_manufacture_and_use_emissions_historical_data",
    )
)


@component.add(
    name="N2O_other_product_manufacture_and_use_emissions_intensity",
    units="Kt/Mdollars_2015",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "n2o_other_product_manufacture_and_use_emissions_historical_data": 1,
        "gdp_real_35r_until_2015": 1,
    },
)
def n2o_other_product_manufacture_and_use_emissions_intensity():
    return (
        n2o_other_product_manufacture_and_use_emissions_historical_data()
        / gdp_real_35r_until_2015()
    )


@component.add(
    name="rest_of_GHG_IPPUs_emissions_9R",
    units="Gt/Year",
    subscripts=["REGIONS_9_I", "GHG_REST_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"rest_of_ghg_ippus_emissions_by_gdp": 1, "unit_conversion_t_gt": 1},
)
def rest_of_ghg_ippus_emissions_9r():
    """
    rest_of_GHG_IPPUs_emissions_9R
    """
    return rest_of_ghg_ippus_emissions_by_gdp() / unit_conversion_t_gt()


@component.add(
    name="rest_of_GHG_IPPUs_emissions_by_GDP",
    units="t/Year",
    subscripts=["REGIONS_9_I", "GHG_REST_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"rest_of_ghg_ippus_emissions_intensity": 1, "gdp_real_9r": 1},
)
def rest_of_ghg_ippus_emissions_by_gdp():
    """
    rest_of_GHG_IPPUs_emissions_by_GDP
    """
    return rest_of_ghg_ippus_emissions_intensity() * gdp_real_9r()


@component.add(
    name="rest_of_GHG_IPPUs_emissions_conversion",
    units="t/Year",
    subscripts=["REGIONS_9_I", "GHG_REST_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "rest_of_ghg_ippus_emissions_historical_data": 1,
        "gwp_20_year": 1,
        "select_gwp_time_frame_sp": 1,
        "gwp_100_year": 1,
        "unit_conversion_tco2eq_gtco2eq": 1,
    },
)
def rest_of_ghg_ippus_emissions_conversion():
    """
    rest_of_GHG_IPPUs_emissions_conversion
    """
    return (
        rest_of_ghg_ippus_emissions_historical_data()
        / if_then_else(
            select_gwp_time_frame_sp() == 1,
            lambda: float(gwp_20_year().loc["CO2"]),
            lambda: float(gwp_100_year().loc["CO2"]),
        )
        * unit_conversion_tco2eq_gtco2eq()
    )


@component.add(
    name="REST_OF_GHG_IPPUS_EMISSIONS_HISTORICAL_DATA",
    units="GtCO2eq/Year",
    subscripts=["REGIONS_9_I", "GHG_REST_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_rest_of_ghg_ippus_emissions_historical_data"
    },
)
def rest_of_ghg_ippus_emissions_historical_data():
    """
    REST_OF_GHG_IPPUS_EMISSIONS_HISTORICAL_DATA
    """
    return _ext_constant_rest_of_ghg_ippus_emissions_historical_data()


_ext_constant_rest_of_ghg_ippus_emissions_historical_data = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "GHG_REST_IPPUS_HISTORICAL_DATA",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "GHG_REST_I": _subscript_dict["GHG_REST_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "GHG_REST_I": _subscript_dict["GHG_REST_I"],
    },
    "_ext_constant_rest_of_ghg_ippus_emissions_historical_data",
)


@component.add(
    name="rest_of_GHG_IPPUs_emissions_intensity",
    units="t/Mdollars_2015",
    subscripts=["REGIONS_9_I", "GHG_REST_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "rest_of_ghg_ippus_emissions_conversion": 1,
        "gdp_real_9r_until_2015": 1,
    },
)
def rest_of_ghg_ippus_emissions_intensity():
    """
    rest_of_GHG_IPPUs_emissions_intensity
    """
    return rest_of_ghg_ippus_emissions_conversion() / gdp_real_9r_until_2015()


@component.add(
    name="total_GHG_IPPUs_emission",
    units="Gt/Year",
    subscripts=["GHG_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ghg_ippus_emissions_9r": 1},
)
def total_ghg_ippus_emission():
    """
    total_GHG_IPPUs_emission_9R
    """
    return sum(
        ghg_ippus_emissions_9r().rename({"REGIONS_9_I": "REGIONS_9_I!"}),
        dim=["REGIONS_9_I!"],
    )
