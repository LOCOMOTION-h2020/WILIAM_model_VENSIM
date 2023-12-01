"""
Module materials.ni
Translated using PySD version 3.10.0
"""


@component.add(
    name="AMOUNT_OF_Ni_IN_WEIGHT_OF_ROCK",
    units="DMNL",
    subscripts=["ORE_GRADES_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_amount_of_ni_in_weight_of_rock"},
)
def amount_of_ni_in_weight_of_rock():
    """
    Definition of the nickel weight content in % for each ore grade: Rich=12, High grade=2%, low grade=0,6%, ultralow=0,2%, trace=0,05% and the last class is zero 0.00%. Follows a generic scheme and is checked against fit with data. Data come from Mudd (2010) and associated publications.
    """
    return _ext_constant_amount_of_ni_in_weight_of_rock()


_ext_constant_amount_of_ni_in_weight_of_rock = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Nickel",
    "AMOUNT_OF_Ni_IN_WEIGHT_OF_ROCK*",
    {"ORE_GRADES_I": _subscript_dict["ORE_GRADES_I"]},
    _root,
    {"ORE_GRADES_I": _subscript_dict["ORE_GRADES_I"]},
    "_ext_constant_amount_of_ni_in_weight_of_rock",
)


@component.add(
    name="avoid_zero_division",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="Normal",
)
def avoid_zero_division():
    return 0.0001


@component.add(
    name="COEFFICIENT_Cu_INVERTED_COST_CURVE",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_coefficient_cu_inverted_cost_curve"},
)
def coefficient_cu_inverted_cost_curve():
    """
    Olafsdottir, A.H., and Sverdrup, H., 2020, System dynamics modelling of mining, supply, recycling, stocks-in-use and market price for nickel. Mining, Metallurgy & Exploration. 1-22. 10.1007/s42461-020-00370-
    """
    return _ext_constant_coefficient_cu_inverted_cost_curve()


_ext_constant_coefficient_cu_inverted_cost_curve = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Nickel",
    "COEFFICIENT_Cu_INVERTED_COST_CURVE",
    {},
    _root,
    {},
    "_ext_constant_coefficient_cu_inverted_cost_curve",
)


@component.add(
    name="COEFFICIENTS_GLOBAL_Ni_OTHER_DEMAND",
    units="DMNL",
    subscripts=["S_CURVE_FIT_ABC_I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def coefficients_global_ni_other_demand():
    """
    a=8,169001e-01 b=3,951132e-04 c=4,781710e+03
    """
    value = xr.DataArray(
        np.nan,
        {"S_CURVE_FIT_ABC_I": _subscript_dict["S_CURVE_FIT_ABC_I"]},
        ["S_CURVE_FIT_ABC_I"],
    )
    value.loc[["A_S_CURVE"]] = 4
    value.loc[["B_S_CURVE"]] = 0.000295113
    value.loc[["C_S_CURVE"]] = 11500
    return value


@component.add(
    name="COEFFICIENTS_HIGH_TECH_Ni_DEMAND",
    units="1/Years",
    comp_type="Constant",
    comp_subtype="Normal",
)
def coefficients_high_tech_ni_demand():
    """
    This is the fraction of the total nickel production we assume is used for aircraft turbines, superalloys, specialty tools, rechargeable accumulators and electronics.
    """
    return 0.025


@component.add(
    name="COEFFICIENTS_Ni_CHANGE_GRADE_TWO",
    subscripts=["ORE_GRADES_I", "S_CURVE_FIT_ABC_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_coefficients_ni_change_grade_two"},
)
def coefficients_ni_change_grade_two():
    return _ext_constant_coefficients_ni_change_grade_two()


_ext_constant_coefficients_ni_change_grade_two = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Nickel",
    "COEFFICIENTS_Ni_CHANGE_GRADE",
    {
        "ORE_GRADES_I": _subscript_dict["ORE_GRADES_I"],
        "S_CURVE_FIT_ABC_I": _subscript_dict["S_CURVE_FIT_ABC_I"],
    },
    _root,
    {
        "ORE_GRADES_I": _subscript_dict["ORE_GRADES_I"],
        "S_CURVE_FIT_ABC_I": _subscript_dict["S_CURVE_FIT_ABC_I"],
    },
    "_ext_constant_coefficients_ni_change_grade_two",
)


@component.add(
    name="COEFFICIENTS_Ni_ENERGY_USE",
    units="MJ/kg",
    subscripts=["ORE_GRADES_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_coefficients_ni_energy_use"},
)
def coefficients_ni_energy_use():
    """
    Our own estimates of water use per grade extraction, based on a large literature survey. See the separate report for documentation of setting the value and where the information came from. Sverdrup and Olafsdottir 2021: Assessing the global energy and water use from of metals, materials and fossil fuels extraction and production. Internal report for LOCOMOTION WP7. 44pp
    """
    return _ext_constant_coefficients_ni_energy_use()


_ext_constant_coefficients_ni_energy_use = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Nickel",
    "COEFFICIENTS_Ni_ENERGY_USE*",
    {"ORE_GRADES_I": _subscript_dict["ORE_GRADES_I"]},
    _root,
    {"ORE_GRADES_I": _subscript_dict["ORE_GRADES_I"]},
    "_ext_constant_coefficients_ni_energy_use",
)


@component.add(
    name="COEFFICIENTS_Ni_GRADE_COST",
    units="M$/Mt",
    subscripts=["ORE_GRADES_I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def coefficients_ni_grade_cost():
    """
    The numbers come from gathering this kind of information on the internet: https://seekingalpha.com/article/4246690-top-5-nickel-producers-and-smaller -producers-to-consider
    """
    value = xr.DataArray(
        np.nan, {"ORE_GRADES_I": _subscript_dict["ORE_GRADES_I"]}, ["ORE_GRADES_I"]
    )
    value.loc[["RICH_GRADE"]] = 4000
    value.loc[["HIGH_GRADE"]] = 7000
    value.loc[["LOW_GRADE"]] = 15000
    value.loc[["ULTRALOW_GRADE"]] = 28000
    value.loc[["TRACE_GRADE"]] = 40000
    value.loc[["OCEANS_GRADE"]] = 0
    return value


@component.add(
    name="COEFFICIENTS_Ni_MINING_EFFICIENCY_CURVE",
    units="DMNL",
    subscripts=["S_CURVE_FIT_ABC_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_coefficients_ni_mining_efficiency_curve"
    },
)
def coefficients_ni_mining_efficiency_curve():
    """
    a= 1,579237e+00 b= 4,809316e-02 c=1,922562e+03 Similar to the curve used for copper mining. Copper and nickel mining have many technical similarities and assuming the same progress of technology is reasonable.
    """
    return _ext_constant_coefficients_ni_mining_efficiency_curve()


_ext_constant_coefficients_ni_mining_efficiency_curve = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Nickel",
    "COEFFICIENTS_Ni_MINING_EFFICIENCY_CURVE*",
    {"S_CURVE_FIT_ABC_I": _subscript_dict["S_CURVE_FIT_ABC_I"]},
    _root,
    {"S_CURVE_FIT_ABC_I": _subscript_dict["S_CURVE_FIT_ABC_I"]},
    "_ext_constant_coefficients_ni_mining_efficiency_curve",
)


@component.add(
    name="COEFFICIENTS_Ni_OTHER_RECYCLING_FRACTION",
    units="DMNL",
    subscripts=["S_CURVE_FIT_ABC_I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def coefficients_ni_other_recycling_fraction():
    """
    a=1,235935e+00 b=2,177529e-04 c=5,863350e+03
    """
    value = xr.DataArray(
        np.nan,
        {"S_CURVE_FIT_ABC_I": _subscript_dict["S_CURVE_FIT_ABC_I"]},
        ["S_CURVE_FIT_ABC_I"],
    )
    value.loc[["A_S_CURVE"]] = 0.9
    value.loc[["B_S_CURVE"]] = 0.000217753
    value.loc[["C_S_CURVE"]] = 5863.35
    return value


@component.add(
    name="COEFFICIENTS_Ni_PRICE_EFFECT_ON_DEMAND",
    units="DMNL",
    subscripts=["LINEAR_LOG_FIT_I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def coefficients_ni_price_effect_on_demand():
    value = xr.DataArray(
        np.nan,
        {"LINEAR_LOG_FIT_I": _subscript_dict["LINEAR_LOG_FIT_I"]},
        ["LINEAR_LOG_FIT_I"],
    )
    value.loc[["A_LINEAR_LOG_FIT"]] = 1.1501
    value.loc[["B_LINEAR_LOG_FIT"]] = -1e-05
    return value


@component.add(
    name="coefficients_ni_price_linear",
    units="DMNL",
    subscripts=["LINEAR_LOG_FIT_I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def coefficients_ni_price_linear():
    value = xr.DataArray(
        np.nan,
        {"LINEAR_LOG_FIT_I": _subscript_dict["LINEAR_LOG_FIT_I"]},
        ["LINEAR_LOG_FIT_I"],
    )
    value.loc[["A_LINEAR_LOG_FIT"]] = -218667
    value.loc[["B_LINEAR_LOG_FIT"]] = 48800
    return value


@component.add(
    name="coefficients_ni_price_logistic",
    units="DMNL",
    subscripts=["LINEAR_LOG_FIT_I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def coefficients_ni_price_logistic():
    value = xr.DataArray(
        np.nan,
        {"LINEAR_LOG_FIT_I": _subscript_dict["LINEAR_LOG_FIT_I"]},
        ["LINEAR_LOG_FIT_I"],
    )
    value.loc[["A_LINEAR_LOG_FIT"]] = 16000
    value.loc[["B_LINEAR_LOG_FIT"]] = -0.763
    return value


@component.add(
    name="coefficients_ni_profit_driver",
    units="DMNL",
    subscripts=["S_CURVE_FIT_ABC_I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def coefficients_ni_profit_driver():
    """
    a=1,258193e+00 b=1,292795e-04 c=5,268404e+03
    """
    value = xr.DataArray(
        np.nan,
        {"S_CURVE_FIT_ABC_I": _subscript_dict["S_CURVE_FIT_ABC_I"]},
        ["S_CURVE_FIT_ABC_I"],
    )
    value.loc[["A_S_CURVE"]] = 1.25819
    value.loc[["B_S_CURVE"]] = 0.00012928
    value.loc[["C_S_CURVE"]] = 5268.4
    return value


@component.add(
    name="COEFFICIENTS_PROSPECTING_FROM_GRADES_TWO",
    subscripts=["ORE_GRADES_I", "S_CURVE_FIT_REVERSE_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_coefficients_prospecting_from_grades_two"
    },
)
def coefficients_prospecting_from_grades_two():
    return _ext_constant_coefficients_prospecting_from_grades_two()


_ext_constant_coefficients_prospecting_from_grades_two = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Nickel",
    "COEFFICIENTS_PROSPECTING_FROM_GRADES*",
    {
        "ORE_GRADES_I": _subscript_dict["ORE_GRADES_I"],
        "S_CURVE_FIT_REVERSE_I": _subscript_dict["S_CURVE_FIT_REVERSE_I"],
    },
    _root,
    {
        "ORE_GRADES_I": _subscript_dict["ORE_GRADES_I"],
        "S_CURVE_FIT_REVERSE_I": _subscript_dict["S_CURVE_FIT_REVERSE_I"],
    },
    "_ext_constant_coefficients_prospecting_from_grades_two",
)


@component.add(
    name="COEFFICIENTS_PROSPECTING_TECHNOLOGY_IMPROVEMENTS_TWO",
    subscripts=["ORE_GRADES_I", "S_CURVE_FIT_ABC_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_coefficients_prospecting_technology_improvements_two"
    },
)
def coefficients_prospecting_technology_improvements_two():
    return _ext_constant_coefficients_prospecting_technology_improvements_two()


_ext_constant_coefficients_prospecting_technology_improvements_two = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Nickel",
    "COEFFICIENTS_PROSPECTING_TECHNOLOGY_IMPROVEMENTS",
    {
        "ORE_GRADES_I": _subscript_dict["ORE_GRADES_I"],
        "S_CURVE_FIT_ABC_I": _subscript_dict["S_CURVE_FIT_ABC_I"],
    },
    _root,
    {
        "ORE_GRADES_I": _subscript_dict["ORE_GRADES_I"],
        "S_CURVE_FIT_ABC_I": _subscript_dict["S_CURVE_FIT_ABC_I"],
    },
    "_ext_constant_coefficients_prospecting_technology_improvements_two",
)


@component.add(
    name="COEFFICIENTS_PROSPECTONG_FROM_ALL_TWO",
    subscripts=["ORE_GRADES_I", "S_CURVE_FIT_REVERSE_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_coefficients_prospectong_from_all_two"},
)
def coefficients_prospectong_from_all_two():
    return _ext_constant_coefficients_prospectong_from_all_two()


_ext_constant_coefficients_prospectong_from_all_two = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Nickel",
    "COEFFICIENTS_PROSPECTING_FROM_ALL*",
    {
        "ORE_GRADES_I": _subscript_dict["ORE_GRADES_I"],
        "S_CURVE_FIT_REVERSE_I": _subscript_dict["S_CURVE_FIT_REVERSE_I"],
    },
    _root,
    {
        "ORE_GRADES_I": _subscript_dict["ORE_GRADES_I"],
        "S_CURVE_FIT_REVERSE_I": _subscript_dict["S_CURVE_FIT_REVERSE_I"],
    },
    "_ext_constant_coefficients_prospectong_from_all_two",
)


@component.add(
    name="COEFFICIENTS_WATER_PER_Ni",
    units="Mt/Years",
    subscripts=["ORE_GRADES_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_coefficients_water_per_ni"},
)
def coefficients_water_per_ni():
    """
    Our own estimates of water use per grade extraction, based on a large literature survey. See the separate report for documentation of setting the value and where the information came from. This is the energy and water used associated with the materials consumed to extract this specific resource grade, expressed in MJ/kg product and m3/ton The actual values are taken from an internal LOCOMOTION report that have extracted the available values from literature and extrapolations. Source: Harald Sverdrup and Anna Hulda Olafsdottir 2021. Assessing with the WORLD7 model the global CO2 emissions and water use by metals, materials and fossil fuels extraction and production. LOCOMOTION working paper. 52 pages.
    """
    return _ext_constant_coefficients_water_per_ni()


_ext_constant_coefficients_water_per_ni = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Nickel",
    "COEFFICIENTS_WATER_PER_Ni*",
    {"ORE_GRADES_I": _subscript_dict["ORE_GRADES_I"]},
    _root,
    {"ORE_GRADES_I": _subscript_dict["ORE_GRADES_I"]},
    "_ext_constant_coefficients_water_per_ni",
)


@component.add(
    name="Cu_inverted_cost_curve",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "coefficient_cu_inverted_cost_curve": 1,
        "imv_cu_mining_efficiency_curve": 1,
    },
)
def cu_inverted_cost_curve():
    """
    This diagram originates from Sverdrup and Ragnarsdottir 2014 and again in Sverdrup et al., 2019, and was constructed from copper extraction cost data we found then. It was inverted to create a technology improvement scaling curve. It is important for validation of model performance in the past, but play less role in the time after 2005, as much of the improvements have already been made. Olafsdottir, A.H., and Sverdrup, H., 2020, System dynamics modelling of mining, supply, recycling, stocks-in-use and market price for nickel. Mining, Metallurgy & Exploration. 1-22. 10.1007/s42461-020-00370- Sverdrup, H, Olafsdottir, A.H., Ragnarsdottir, K.V., 2019., Assessing global copper, zinc and lead extraction rates, supply, price and resources using the WORLD6 integrated assessment model. Resources, Conservation and Recycling 1-26. X4 100007. https://doi.org/10.1016/j.rcrx.2019.100007. Open access publication.
    """
    return coefficient_cu_inverted_cost_curve() / imv_cu_mining_efficiency_curve()


@component.add(
    name="decrease_Ni_plating",
    units="Mt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ni_plating": 1, "ni_plating_loss_rate": 1},
)
def decrease_ni_plating():
    """
    Nickel is plating being worn off and lost diffusively
    """
    return ni_plating() * ni_plating_loss_rate()


@component.add(
    name="delayed_TS_Ni_price_economy_adjusted",
    units="DMNL",
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_ni_price_economy_adjusted": 1},
    other_deps={
        "_delayfixed_delayed_ts_ni_price_economy_adjusted": {
            "initial": {"time_step": 1},
            "step": {"ni_price_economy_adjusted": 1},
        }
    },
)
def delayed_ts_ni_price_economy_adjusted():
    """
    Delayed nickel price economy adjusted.
    """
    return _delayfixed_delayed_ts_ni_price_economy_adjusted()


_delayfixed_delayed_ts_ni_price_economy_adjusted = DelayFixed(
    lambda: ni_price_economy_adjusted(),
    lambda: time_step(),
    lambda: 100,
    time_step,
    "_delayfixed_delayed_ts_ni_price_economy_adjusted",
)


@component.add(
    name="delayed_TS_Ni_profit_average",
    units="DMNL",
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_delayed_ts_ni_profit_average": 1},
    other_deps={
        "_integ_delayed_ts_ni_profit_average": {
            "initial": {"initial_delayed_ts_ni_profit_average": 1},
            "step": {"ni_profit_input": 1, "ni_profit_out_new": 1},
        }
    },
)
def delayed_ts_ni_profit_average():
    """
    Holding the profit signal for a response time before decision. Assumption based or industrial generics Olafsdottir, A.H., and Sverdrup, H., 2020, System dynamics modelling of mining, supply, recycling, stocks-in-use and market price for nickel. Mining, Metallurgy & Exploration. 1-22. 10.1007/s42461-020-00370-
    """
    return _integ_delayed_ts_ni_profit_average()


_integ_delayed_ts_ni_profit_average = Integ(
    lambda: ni_profit_input() - ni_profit_out_new(),
    lambda: initial_delayed_ts_ni_profit_average(),
    "_integ_delayed_ts_ni_profit_average",
)


@component.add(name="DEMAND_Ni_BASE_YEAR", comp_type="Constant", comp_subtype="Normal")
def demand_ni_base_year():
    return 1880.6 / 1000


@component.add(
    name="Global_Ni_other_demand",
    units="Mt/Mpersons",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"coefficients_global_ni_other_demand": 3, "imv_gdp_per_person": 1},
)
def global_ni_other_demand():
    """
    Other demand, based on population and GDP. This is the residual demand affer stainless steel and common steel has been accounted for
    """
    return float(coefficients_global_ni_other_demand().loc["A_S_CURVE"]) / (
        1
        + np.exp(
            -float(coefficients_global_ni_other_demand().loc["B_S_CURVE"])
            * (
                imv_gdp_per_person()
                - float(coefficients_global_ni_other_demand().loc["C_S_CURVE"])
            )
        )
    )


@component.add(
    name="implicit_price_Ni",
    units="Mdollars_2015/Mt",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "initial_output_real_materials": 2,
        "ni_historical_global_consumption_mt": 1,
        "demand_ni_base_year": 1,
    },
)
def implicit_price_ni():
    return if_then_else(
        time() < 2015,
        lambda: sum(
            initial_output_real_materials()
            .loc[:, "MINING_AND_MANUFACTURING_NICKEL"]
            .reset_coords(drop=True)
            .rename({"REGIONS_35_I": "REGIONS_35_I!"}),
            dim=["REGIONS_35_I!"],
        )
        / ni_historical_global_consumption_mt(),
        lambda: sum(
            initial_output_real_materials()
            .loc[:, "MINING_AND_MANUFACTURING_NICKEL"]
            .reset_coords(drop=True)
            .rename({"REGIONS_35_I": "REGIONS_35_I!"}),
            dim=["REGIONS_35_I!"],
        )
        / demand_ni_base_year(),
    )


@component.add(
    name="IMV_Cu_MINED_0",
    units="Mt/Years",
    comp_type="Auxiliary",
    comp_subtype="with Lookup",
    depends_on={"time": 1},
)
def imv_cu_mined_0():
    """
    From the copper module
    """
    return np.interp(
        time(),
        [
            1850.0,
            1851.0,
            1852.0,
            1853.0,
            1854.0,
            1855.0,
            1856.0,
            1857.0,
            1858.0,
            1859.0,
            1860.0,
            1861.0,
            1862.0,
            1863.0,
            1864.0,
            1865.0,
            1866.0,
            1867.0,
            1868.0,
            1869.0,
            1870.0,
            1871.0,
            1872.0,
            1873.0,
            1874.0,
            1875.0,
            1876.0,
            1877.0,
            1878.0,
            1879.0,
            1880.0,
            1881.0,
            1882.0,
            1883.0,
            1884.0,
            1885.0,
            1886.0,
            1887.0,
            1888.0,
            1889.0,
            1890.0,
            1891.0,
            1892.0,
            1893.0,
            1894.0,
            1895.0,
            1896.0,
            1897.0,
            1898.0,
            1899.0,
            1900.0,
            1901.0,
            1902.0,
            1903.0,
            1904.0,
            1905.0,
            1906.0,
            1907.0,
            1908.0,
            1909.0,
            1910.0,
            1911.0,
            1912.0,
            1913.0,
            1914.0,
            1915.0,
            1916.0,
            1917.0,
            1918.0,
            1919.0,
            1920.0,
            1921.0,
            1922.0,
            1923.0,
            1924.0,
            1925.0,
            1926.0,
            1927.0,
            1928.0,
            1929.0,
            1930.0,
            1931.0,
            1932.0,
            1933.0,
            1934.0,
            1935.0,
            1936.0,
            1937.0,
            1938.0,
            1939.0,
            1940.0,
            1941.0,
            1942.0,
            1943.0,
            1944.0,
            1945.0,
            1946.0,
            1947.0,
            1948.0,
            1949.0,
            1950.0,
            1951.0,
            1952.0,
            1953.0,
            1954.0,
            1955.0,
            1956.0,
            1957.0,
            1958.0,
            1959.0,
            1960.0,
            1961.0,
            1962.0,
            1963.0,
            1964.0,
            1965.0,
            1966.0,
            1967.0,
            1968.0,
            1969.0,
            1970.0,
            1971.0,
            1972.0,
            1973.0,
            1974.0,
            1975.0,
            1976.0,
            1977.0,
            1978.0,
            1979.0,
            1980.0,
            1981.0,
            1982.0,
            1983.0,
            1984.0,
            1985.0,
            1986.0,
            1987.0,
            1988.0,
            1989.0,
            1990.0,
            1991.0,
            1992.0,
            1993.0,
            1994.0,
            1995.0,
            1996.0,
            1997.0,
            1998.0,
            1999.0,
            2000.0,
            2001.0,
            2002.0,
            2003.0,
            2004.0,
            2005.0,
            2006.0,
            2007.0,
            2008.0,
            2009.0,
            2010.0,
            2011.0,
            2012.0,
            2013.0,
            2014.0,
            2015.0,
            2016.0,
            2017.0,
            2018.0,
            2019.0,
            2020.0,
            2021.0,
            2022.0,
            2023.0,
            2024.0,
            2025.0,
            2026.0,
            2027.0,
            2028.0,
            2029.0,
            2030.0,
            2031.0,
            2032.0,
            2033.0,
            2034.0,
            2035.0,
            2036.0,
            2037.0,
            2038.0,
            2039.0,
            2040.0,
            2041.0,
            2042.0,
            2043.0,
            2044.0,
            2045.0,
            2046.0,
            2047.0,
            2048.0,
            2049.0,
            2050.0,
            2051.0,
            2052.0,
            2053.0,
            2054.0,
            2055.0,
            2056.0,
            2057.0,
            2058.0,
            2059.0,
            2060.0,
            2061.0,
            2062.0,
            2063.0,
            2064.0,
            2065.0,
            2066.0,
            2067.0,
            2068.0,
            2069.0,
            2070.0,
            2071.0,
            2072.0,
            2073.0,
            2074.0,
            2075.0,
            2076.0,
            2077.0,
            2078.0,
            2079.0,
            2080.0,
            2081.0,
            2082.0,
            2083.0,
            2084.0,
            2085.0,
            2086.0,
            2087.0,
            2088.0,
            2089.0,
            2090.0,
            2091.0,
            2092.0,
            2093.0,
            2094.0,
            2095.0,
            2096.0,
            2097.0,
            2098.0,
            2099.0,
            2100.0,
        ],
        [
            0.29,
            0.29,
            0.29,
            0.29,
            0.29,
            0.29,
            0.29,
            0.29,
            0.29,
            0.29,
            0.29,
            0.29,
            0.29,
            0.29,
            0.29,
            0.29,
            0.29,
            0.29,
            0.29,
            0.29,
            0.29,
            0.29,
            0.29,
            0.29,
            0.29,
            0.29,
            0.29,
            0.29,
            0.29,
            0.29,
            0.29,
            0.29,
            0.29,
            0.29,
            0.29,
            0.29,
            0.29,
            0.29,
            0.29,
            0.29,
            0.29,
            0.29,
            0.29,
            0.29,
            0.29,
            0.29,
            0.29,
            0.29,
            0.29,
            0.29,
            0.29,
            0.537,
            0.784,
            0.86,
            0.86,
            0.883333,
            0.944,
            1.0,
            1.0,
            1.0,
            1.04667,
            1.10733,
            1.168,
            1.22867,
            1.29,
            1.355,
            1.42,
            1.48133,
            1.542,
            1.60267,
            1.66333,
            1.724,
            1.78467,
            1.84533,
            1.91,
            1.975,
            2.07467,
            2.196,
            2.29867,
            2.35933,
            2.42,
            2.485,
            2.55,
            2.612,
            2.67267,
            2.75667,
            2.878,
            3.00433,
            3.19067,
            3.377,
            3.51667,
            3.64233,
            3.766,
            3.88733,
            4.01867,
            4.205,
            4.39133,
            4.52267,
            4.644,
            5.03367,
            5.65333,
            6.158,
            6.27933,
            6.40067,
            6.582,
            6.76833,
            6.992,
            7.239,
            7.50467,
            7.81233,
            8.12,
            8.367,
            8.614,
            8.906,
            9.218,
            9.505,
            9.752,
            10.0037,
            10.3113,
            10.619,
            11.2133,
            11.8937,
            12.316,
            12.4373,
            12.578,
            12.825,
            13.072,
            13.2163,
            13.342,
            13.267,
            13.02,
            12.858,
            12.9793,
            13.1007,
            13.454,
            13.8267,
            14.234,
            14.663,
            15.132,
            15.691,
            16.25,
            16.744,
            17.238,
            17.645,
            18.0133,
            18.4067,
            18.84,
            19.2637,
            19.5713,
            19.879,
            20.4267,
            21.0463,
            21.55,
            21.9183,
            22.2967,
            22.73,
            23.1633,
            23.4903,
            23.798,
            24.2737,
            24.8933,
            25.484,
            25.978,
            26.472,
            26.91,
            27.3433,
            27.814,
            28.308,
            28.7633,
            29.1317,
            29.5,
            29.994,
            30.488,
            30.982,
            31.476,
            31.8983,
            32.206,
            32.528,
            33.022,
            33.516,
            34.1533,
            34.8337,
            35.428,
            35.922,
            36.416,
            36.91,
            37.404,
            38.0557,
            38.736,
            39.3837,
            40.0033,
            40.636,
            41.312,
            41.988,
            42.556,
            43.115,
            43.6713,
            44.226,
            44.9713,
            46.1457,
            47.32,
            47.3807,
            47.4413,
            48.102,
            49.0293,
            49.7417,
            50.11,
            50.4787,
            50.8513,
            51.224,
            51.5,
            51.747,
            52.078,
            52.507,
            52.9367,
            53.37,
            53.8033,
            54.0277,
            54.214,
            54.433,
            54.68,
            54.884,
            54.9447,
            55.0053,
            55.01,
            55.01,
            55.01,
            55.01,
            55.01,
            55.01,
            55.01,
            55.01,
            55.01,
            54.926,
            54.8047,
            54.6583,
            54.472,
            54.281,
            54.034,
            53.787,
            53.54,
            53.293,
            53.074,
            52.8877,
            52.692,
            52.445,
            52.198,
            52.0023,
            51.816,
            51.499,
            51.07,
        ],
    )


@component.add(
    name="IMV_Cu_MINING_EFFICIENCY_CURVE",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="with Lookup",
    depends_on={"time": 1},
)
def imv_cu_mining_efficiency_curve():
    """
    Cost efficiency development curve
    """
    return np.interp(
        time(),
        [
            1850.0,
            1851.0,
            1852.0,
            1853.0,
            1854.0,
            1855.0,
            1856.0,
            1857.0,
            1858.0,
            1859.0,
            1860.0,
            1861.0,
            1862.0,
            1863.0,
            1864.0,
            1865.0,
            1866.0,
            1867.0,
            1868.0,
            1869.0,
            1870.0,
            1871.0,
            1872.0,
            1873.0,
            1874.0,
            1875.0,
            1876.0,
            1877.0,
            1878.0,
            1879.0,
            1880.0,
            1881.0,
            1882.0,
            1883.0,
            1884.0,
            1885.0,
            1886.0,
            1887.0,
            1888.0,
            1889.0,
            1890.0,
            1891.0,
            1892.0,
            1893.0,
            1894.0,
            1895.0,
            1896.0,
            1897.0,
            1898.0,
            1899.0,
            1900.0,
            1901.0,
            1902.0,
            1903.0,
            1904.0,
            1905.0,
            1906.0,
            1907.0,
            1908.0,
            1909.0,
            1910.0,
            1911.0,
            1912.0,
            1913.0,
            1914.0,
            1915.0,
            1916.0,
            1917.0,
            1918.0,
            1919.0,
            1920.0,
            1921.0,
            1922.0,
            1923.0,
            1924.0,
            1925.0,
            1926.0,
            1927.0,
            1928.0,
            1929.0,
            1930.0,
            1931.0,
            1932.0,
            1933.0,
            1934.0,
            1935.0,
            1936.0,
            1937.0,
            1938.0,
            1939.0,
            1940.0,
            1941.0,
            1942.0,
            1943.0,
            1944.0,
            1945.0,
            1946.0,
            1947.0,
            1948.0,
            1949.0,
            1950.0,
            1951.0,
            1952.0,
            1953.0,
            1954.0,
            1955.0,
            1956.0,
            1957.0,
            1958.0,
            1959.0,
            1960.0,
            1961.0,
            1962.0,
            1963.0,
            1964.0,
            1965.0,
            1966.0,
            1967.0,
            1968.0,
            1969.0,
            1970.0,
            1971.0,
            1972.0,
            1973.0,
            1974.0,
            1975.0,
            1976.0,
            1977.0,
            1978.0,
            1979.0,
            1980.0,
            1981.0,
            1982.0,
            1983.0,
            1984.0,
            1985.0,
            1986.0,
            1987.0,
            1988.0,
            1989.0,
            1990.0,
            1991.0,
            1992.0,
            1993.0,
            1994.0,
            1995.0,
            1996.0,
            1997.0,
            1998.0,
            1999.0,
            2000.0,
            2001.0,
            2002.0,
            2003.0,
            2004.0,
            2005.0,
            2006.0,
            2007.0,
            2008.0,
            2009.0,
            2010.0,
            2011.0,
            2012.0,
            2013.0,
            2014.0,
            2015.0,
            2016.0,
            2017.0,
            2018.0,
            2019.0,
            2020.0,
            2021.0,
            2022.0,
            2023.0,
            2024.0,
            2025.0,
            2026.0,
            2027.0,
            2028.0,
            2029.0,
            2030.0,
            2031.0,
            2032.0,
            2033.0,
            2034.0,
            2035.0,
            2036.0,
            2037.0,
            2038.0,
            2039.0,
            2040.0,
            2041.0,
            2042.0,
            2043.0,
            2044.0,
            2045.0,
            2046.0,
            2047.0,
            2048.0,
            2049.0,
            2050.0,
            2051.0,
            2052.0,
            2053.0,
            2054.0,
            2055.0,
            2056.0,
            2057.0,
            2058.0,
            2059.0,
            2060.0,
            2061.0,
            2062.0,
            2063.0,
            2064.0,
            2065.0,
            2066.0,
            2067.0,
            2068.0,
            2069.0,
            2070.0,
            2071.0,
            2072.0,
            2073.0,
            2074.0,
            2075.0,
            2076.0,
            2077.0,
            2078.0,
            2079.0,
            2080.0,
            2081.0,
            2082.0,
            2083.0,
            2084.0,
            2085.0,
            2086.0,
            2087.0,
            2088.0,
            2089.0,
            2090.0,
            2091.0,
            2092.0,
            2093.0,
            2094.0,
            2095.0,
            2096.0,
            2097.0,
            2098.0,
            2099.0,
            2100.0,
        ],
        [
            247.4,
            246.6,
            246.6,
            246.6,
            245.0,
            243.5,
            240.3,
            238.7,
            236.4,
            235.6,
            234.0,
            233.2,
            231.7,
            229.3,
            227.7,
            225.4,
            223.0,
            215.2,
            212.0,
            205.0,
            202.6,
            201.0,
            198.7,
            195.5,
            185.3,
            183.8,
            182.2,
            174.3,
            172.8,
            167.5,
            158.6,
            156.3,
            150.8,
            149.2,
            143.7,
            139.8,
            133.5,
            128.0,
            124.9,
            119.4,
            117.8,
            113.1,
            109.9,
            106.0,
            102.1,
            95.8,
            93.5,
            88.7,
            87.2,
            84.8,
            82.5,
            79.3,
            78.5,
            73.0,
            71.5,
            67.5,
            66.0,
            63.6,
            62.0,
            60.5,
            59.7,
            56.5,
            44.8,
            44.8,
            44.8,
            44.8,
            44.8,
            44.0,
            44.0,
            44.0,
            42.4,
            42.4,
            41.6,
            41.6,
            41.6,
            41.6,
            42.4,
            43.2,
            42.4,
            42.4,
            42.9,
            43.5,
            45.5,
            45.5,
            46.1,
            46.1,
            46.6,
            46.6,
            46.6,
            46.1,
            46.1,
            44.5,
            44.5,
            44.5,
            44.5,
            44.5,
            44.5,
            44.0,
            42.4,
            42.4,
            41.9,
            42.4,
            42.9,
            42.4,
            40.8,
            39.8,
            29.8,
            29.8,
            29.1,
            29.1,
            29.45,
            30.6,
            31.4,
            32.2,
            30.6,
            28.3,
            25.1,
            24.3,
            24.3,
            20.4,
            20.4,
            21.2,
            22.0,
            22.0,
            22.8,
            22.8,
            22.8,
            22.8,
            20.4,
            21.2,
            22.0,
            22.0,
            24.3,
            24.3,
            24.3,
            22.0,
            22.0,
            22.0,
            22.8,
            23.6,
            24.3,
            25.1,
            25.1,
            25.1,
            25.9,
            25.9,
            25.9,
            26.7,
            26.7,
            28.3,
            28.3,
            28.3,
            28.3,
            28.3,
            28.3,
            28.3,
            28.3,
            28.3,
            28.3,
            28.3,
            28.3,
            28.3,
            28.3,
            28.3,
            28.3,
            28.3,
            28.3,
            29.1,
            28.3,
            28.3,
            28.3,
            28.3,
            28.3,
            28.3,
            28.3,
            28.3,
            28.3,
            28.3,
            28.3,
            28.3,
            28.3,
            28.3,
            28.3,
            28.3,
            28.3,
            28.3,
            28.3,
            28.3,
            28.3,
            28.3,
            28.3,
            28.3,
            28.3,
            28.3,
            28.3,
            28.3,
            28.3,
            28.3,
            29.1,
            29.1,
            29.1,
            29.8,
            29.8,
            29.8,
            29.8,
            29.1,
            29.1,
            29.1,
            29.1,
            29.1,
            29.1,
            29.1,
            29.1,
            29.1,
            29.1,
            29.1,
            29.1,
            29.1,
            29.1,
            29.1,
            29.1,
            29.1,
            29.1,
            29.45,
            29.8,
            29.8,
            29.8,
            29.8,
            29.8,
            29.8,
            29.8,
            29.8,
            29.8,
            29.8,
            29.8,
            29.8,
            29.8,
            29.8,
            29.8,
            29.8,
            29.8,
            29.8,
            29.8,
            29.8,
            29.8,
            29.8,
            29.8,
            29.8,
            29.8,
            29.8,
            29.8,
        ],
    )


@component.add(
    name="IMV_Ni_RESIDUAL",
    units="Mt/Years",
    comp_type="Auxiliary",
    comp_subtype="with Lookup",
    depends_on={"time": 1},
)
def imv_ni_residual():
    return np.interp(
        time(),
        [
            1850.0,
            1851.0,
            1852.0,
            1853.0,
            1854.0,
            1855.0,
            1856.0,
            1857.0,
            1858.0,
            1859.0,
            1860.0,
            1861.0,
            1862.0,
            1863.0,
            1864.0,
            1865.0,
            1866.0,
            1867.0,
            1868.0,
            1869.0,
            1870.0,
            1871.0,
            1872.0,
            1873.0,
            1874.0,
            1875.0,
            1876.0,
            1877.0,
            1878.0,
            1879.0,
            1880.0,
            1881.0,
            1882.0,
            1883.0,
            1884.0,
            1885.0,
            1886.0,
            1887.0,
            1888.0,
            1889.0,
            1890.0,
            1891.0,
            1892.0,
            1893.0,
            1894.0,
            1895.0,
            1896.0,
            1897.0,
            1898.0,
            1899.0,
            1900.0,
            1901.0,
            1902.0,
            1903.0,
            1904.0,
            1905.0,
            1906.0,
            1907.0,
            1908.0,
            1909.0,
            1910.0,
            1911.0,
            1912.0,
            1913.0,
            1914.0,
            1915.0,
            1916.0,
            1917.0,
            1918.0,
            1919.0,
            1920.0,
            1921.0,
            1922.0,
            1923.0,
            1924.0,
            1925.0,
            1926.0,
            1927.0,
            1928.0,
            1929.0,
            1930.0,
            1931.0,
            1932.0,
            1933.0,
            1934.0,
            1935.0,
            1936.0,
            1937.0,
            1938.0,
            1939.0,
            1940.0,
            1941.0,
            1942.0,
            1943.0,
            1944.0,
            1945.0,
            1946.0,
            1947.0,
            1948.0,
            1949.0,
            1950.0,
            1951.0,
            1952.0,
            1953.0,
            1954.0,
            1955.0,
            1956.0,
            1957.0,
            1958.0,
            1959.0,
            1960.0,
            1961.0,
            1962.0,
            1963.0,
            1964.0,
            1965.0,
            1966.0,
            1967.0,
            1968.0,
            1969.0,
            1970.0,
            1971.0,
            1972.0,
            1973.0,
            1974.0,
            1975.0,
            1976.0,
            1977.0,
            1978.0,
            1979.0,
            1980.0,
            1981.0,
            1982.0,
            1983.0,
            1984.0,
            1985.0,
            1986.0,
            1987.0,
            1988.0,
            1989.0,
            1990.0,
            1991.0,
            1992.0,
            1993.0,
            1994.0,
            1995.0,
            1996.0,
            1997.0,
            1998.0,
            1999.0,
            2000.0,
            2001.0,
            2002.0,
            2003.0,
            2004.0,
            2005.0,
            2006.0,
            2007.0,
            2008.0,
            2009.0,
            2010.0,
            2011.0,
            2012.0,
            2013.0,
            2014.0,
            2015.0,
            2016.0,
            2017.0,
            2018.0,
            2019.0,
            2020.0,
            2021.0,
            2022.0,
            2023.0,
            2024.0,
            2025.0,
            2026.0,
            2027.0,
            2028.0,
            2029.0,
            2030.0,
            2031.0,
            2032.0,
            2033.0,
            2034.0,
            2035.0,
            2036.0,
            2037.0,
            2038.0,
            2039.0,
            2040.0,
            2041.0,
            2042.0,
            2043.0,
            2044.0,
            2045.0,
            2046.0,
            2047.0,
            2048.0,
            2049.0,
            2050.0,
            2051.0,
            2052.0,
            2053.0,
            2054.0,
            2055.0,
            2056.0,
            2057.0,
            2058.0,
            2059.0,
            2060.0,
            2061.0,
            2062.0,
            2063.0,
            2064.0,
            2065.0,
            2066.0,
            2067.0,
            2068.0,
            2069.0,
            2070.0,
            2071.0,
            2072.0,
            2073.0,
            2074.0,
            2075.0,
            2076.0,
            2077.0,
            2078.0,
            2079.0,
            2080.0,
            2081.0,
            2082.0,
            2083.0,
            2084.0,
            2085.0,
            2086.0,
            2087.0,
            2088.0,
            2089.0,
            2090.0,
            2091.0,
            2092.0,
            2093.0,
            2094.0,
            2095.0,
            2096.0,
            2097.0,
            2098.0,
            2099.0,
            2100.0,
        ],
        [
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            7.80000e-05,
            9.00000e-06,
            4.00000e-06,
            3.00000e-06,
            5.85617e00,
            3.20000e-05,
            1.10000e-05,
            1.30000e-05,
            6.00000e-06,
            3.20000e-04,
            1.57000e-04,
            2.20000e-05,
            2.51000e-04,
            3.47000e-04,
            2.20000e-05,
            3.62000e-03,
            6.66700e-03,
            9.84500e-03,
            8.24400e-03,
            2.76000e-04,
            5.01000e-04,
            4.64000e-04,
            1.14400e-03,
            1.09500e-03,
            4.39000e-04,
            7.07000e-04,
            4.55000e-04,
            3.05000e-04,
            6.47000e-04,
            1.30900e-03,
            1.47600e-03,
            6.74000e-04,
            1.62000e-03,
            4.17000e-04,
            -1.13000e-04,
            4.30000e-05,
            -2.50000e-05,
            4.71000e-04,
            1.34000e-03,
            1.35500e-03,
            8.55000e-04,
            5.41000e-04,
            6.35000e-04,
            1.26800e-03,
            6.92000e-04,
            3.10300e-03,
            1.51200e-03,
            1.87700e-03,
            2.49400e-03,
            1.73700e-03,
            3.15400e-03,
            2.92700e-03,
            3.84000e-04,
            2.28000e-04,
            2.02400e-03,
            2.33800e-03,
            3.47700e-03,
            2.30600e-03,
            2.04400e-03,
            4.70200e-03,
            4.25500e-03,
            5.16000e-03,
            4.97800e-03,
            6.14600e-03,
            4.40700e-03,
            1.87900e-03,
            8.48200e-03,
            5.11200e-03,
            1.39000e-04,
            3.51800e-03,
            6.47300e-03,
            4.08100e-03,
            1.42990e-02,
            2.96510e-02,
            2.80900e-03,
            2.23477e-01,
            3.10514e-01,
            3.04632e-01,
            3.04025e-01,
            3.78572e-01,
            4.76768e-01,
            5.42921e-01,
            5.79699e-01,
            6.07247e-01,
            6.42925e-01,
            6.48042e-01,
            6.36478e-01,
            6.47121e-01,
            6.62738e-01,
            7.28984e-01,
            7.71698e-01,
            7.36641e-01,
            7.31688e-01,
            7.90630e-01,
            8.12628e-01,
            8.70496e-01,
            8.82264e-01,
            9.52070e-01,
            9.83719e-01,
            9.78588e-01,
            9.46252e-01,
            9.26899e-01,
            9.13903e-01,
            9.59378e-01,
            9.62042e-01,
            9.91058e-01,
            1.02051e00,
            1.02472e00,
            9.69090e-01,
            8.71348e-01,
            6.35699e-01,
            7.88453e-01,
            8.99812e-01,
            9.75221e-01,
            1.00748e00,
            8.92873e-01,
            4.37300e-03,
            9.89200e-03,
            1.24330e-02,
            7.33900e-03,
            -2.51150e-02,
            3.02800e-03,
            -3.82500e-03,
            -8.31000e-04,
            -4.80400e-03,
            2.01390e-02,
            4.59500e-03,
            8.68200e-03,
            2.74490e-02,
            1.72420e-02,
            1.71450e-02,
            3.88300e-03,
            9.57100e-03,
            3.52100e-03,
            4.83000e-02,
            5.71200e-03,
            3.55000e-03,
            8.24400e-03,
            1.05490e-02,
            3.29500e-03,
            2.24080e-02,
            2.88500e-02,
            1.77750e-02,
            1.12220e-02,
            8.05100e-03,
            1.59210e-02,
            7.32400e-03,
            9.38600e-03,
            1.34790e-02,
            5.29800e-03,
            2.07200e-02,
            -1.70600e-03,
            -8.64000e-04,
            9.56000e-04,
            -1.49400e-03,
            -1.64000e-04,
            7.04400e-03,
            1.04550e-02,
            4.69900e-03,
            -2.17800e-03,
            -3.72000e-03,
            -7.88500e-03,
            3.68090e-02,
            3.48100e-03,
            -7.29000e-04,
            3.71000e-04,
            1.01250e-02,
            1.43205e00,
            2.39545e00,
            2.64208e00,
            2.68163e00,
            3.10075e-01,
            1.69728e-01,
            1.27374e-01,
            1.96569e-01,
            2.02261e-01,
            1.04518e-01,
            -3.04500e-03,
            -4.61600e-03,
            -4.94900e-03,
            -3.67800e-03,
            5.07100e-03,
            6.48300e-03,
            1.18600e-03,
            1.95120e-02,
            2.27693e-01,
            2.13011e-01,
            2.04485e-01,
            2.06443e-01,
            2.06874e-01,
            2.99472e-01,
            4.10600e-01,
            4.83541e-01,
            4.75759e-01,
            4.72431e-01,
            4.70543e-01,
            4.75971e-01,
            5.12397e-01,
            5.64943e-01,
            1.15869e00,
            1.15444e00,
            1.14290e00,
            1.15875e00,
            1.13965e00,
            1.12659e00,
            1.10571e00,
            1.08708e00,
            1.06962e00,
            1.06303e00,
            1.05377e00,
            1.04283e00,
            1.02953e00,
            1.01788e00,
            1.00857e00,
            9.96309e-01,
            9.83834e-01,
            9.71097e-01,
            9.54858e-01,
        ],
    )


@component.add(
    name="IMV_SS_FAST_IN_USE",
    units="Mt",
    comp_type="Auxiliary",
    comp_subtype="with Lookup",
    depends_on={"time": 1},
)
def imv_ss_fast_in_use():
    """
    IMV from stainless steel. It's a stock in the SS module
    """
    return np.interp(
        time(),
        [
            1850.0,
            1851.0,
            1852.0,
            1853.0,
            1854.0,
            1855.0,
            1856.0,
            1857.0,
            1858.0,
            1859.0,
            1860.0,
            1861.0,
            1862.0,
            1863.0,
            1864.0,
            1865.0,
            1866.0,
            1867.0,
            1868.0,
            1869.0,
            1870.0,
            1871.0,
            1872.0,
            1873.0,
            1874.0,
            1875.0,
            1876.0,
            1877.0,
            1878.0,
            1879.0,
            1880.0,
            1881.0,
            1882.0,
            1883.0,
            1884.0,
            1885.0,
            1886.0,
            1887.0,
            1888.0,
            1889.0,
            1890.0,
            1891.0,
            1892.0,
            1893.0,
            1894.0,
            1895.0,
            1896.0,
            1897.0,
            1898.0,
            1899.0,
            1900.0,
            1901.0,
            1902.0,
            1903.0,
            1904.0,
            1905.0,
            1906.0,
            1907.0,
            1908.0,
            1909.0,
            1910.0,
            1911.0,
            1912.0,
            1913.0,
            1914.0,
            1915.0,
            1916.0,
            1917.0,
            1918.0,
            1919.0,
            1920.0,
            1921.0,
            1922.0,
            1923.0,
            1924.0,
            1925.0,
            1926.0,
            1927.0,
            1928.0,
            1929.0,
            1930.0,
            1931.0,
            1932.0,
            1933.0,
            1934.0,
            1935.0,
            1936.0,
            1937.0,
            1938.0,
            1939.0,
            1940.0,
            1941.0,
            1942.0,
            1943.0,
            1944.0,
            1945.0,
            1946.0,
            1947.0,
            1948.0,
            1949.0,
            1950.0,
            1951.0,
            1952.0,
            1953.0,
            1954.0,
            1955.0,
            1956.0,
            1957.0,
            1958.0,
            1959.0,
            1960.0,
            1961.0,
            1962.0,
            1963.0,
            1964.0,
            1965.0,
            1966.0,
            1967.0,
            1968.0,
            1969.0,
            1970.0,
            1971.0,
            1972.0,
            1973.0,
            1974.0,
            1975.0,
            1976.0,
            1977.0,
            1978.0,
            1979.0,
            1980.0,
            1981.0,
            1982.0,
            1983.0,
            1984.0,
            1985.0,
            1986.0,
            1987.0,
            1988.0,
            1989.0,
            1990.0,
            1991.0,
            1992.0,
            1993.0,
            1994.0,
            1995.0,
            1996.0,
            1997.0,
            1998.0,
            1999.0,
            2000.0,
            2001.0,
            2002.0,
            2003.0,
            2004.0,
            2005.0,
            2006.0,
            2007.0,
            2008.0,
            2009.0,
            2010.0,
            2011.0,
            2012.0,
            2013.0,
            2014.0,
            2015.0,
            2016.0,
            2017.0,
            2018.0,
            2019.0,
            2020.0,
            2021.0,
            2022.0,
            2023.0,
            2024.0,
            2025.0,
            2026.0,
            2027.0,
            2028.0,
            2029.0,
            2030.0,
            2031.0,
            2032.0,
            2033.0,
            2034.0,
            2035.0,
            2036.0,
            2037.0,
            2038.0,
            2039.0,
            2040.0,
            2041.0,
            2042.0,
            2043.0,
            2044.0,
            2045.0,
            2046.0,
            2047.0,
            2048.0,
            2049.0,
            2050.0,
            2051.0,
            2052.0,
            2053.0,
            2054.0,
            2055.0,
            2056.0,
            2057.0,
            2058.0,
            2059.0,
            2060.0,
            2061.0,
            2062.0,
            2063.0,
            2064.0,
            2065.0,
            2066.0,
            2067.0,
            2068.0,
            2069.0,
            2070.0,
            2071.0,
            2072.0,
            2073.0,
            2074.0,
            2075.0,
            2076.0,
            2077.0,
            2078.0,
            2079.0,
            2080.0,
            2081.0,
            2082.0,
            2083.0,
            2084.0,
            2085.0,
            2086.0,
            2087.0,
            2088.0,
            2089.0,
            2090.0,
            2091.0,
            2092.0,
            2093.0,
            2094.0,
            2095.0,
            2096.0,
            2097.0,
            2098.0,
            2099.0,
            2100.0,
        ],
        [
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            3.08700e-03,
            9.46300e-03,
            1.43810e-02,
            1.79920e-02,
            2.06490e-02,
            2.74260e-02,
            3.48050e-02,
            4.07210e-02,
            4.54660e-02,
            5.15490e-02,
            6.69100e-02,
            8.59980e-02,
            1.01041e-01,
            1.23906e-01,
            1.48906e-01,
            1.67635e-01,
            1.94440e-01,
            2.33288e-01,
            2.73812e-01,
            2.81089e-01,
            2.96253e-01,
            3.37959e-01,
            4.05027e-01,
            5.20245e-01,
            6.64367e-01,
            7.98797e-01,
            9.30015e-01,
            1.04929e00,
            1.15515e00,
            1.26634e00,
            1.37997e00,
            1.52755e00,
            1.70204e00,
            1.88609e00,
            2.09554e00,
            2.27579e00,
            2.44963e00,
            2.59827e00,
            2.73924e00,
            2.94801e00,
            3.19027e00,
            3.41338e00,
            3.61230e00,
            3.80730e00,
            3.99455e00,
            4.18323e00,
            4.46747e00,
            4.75513e00,
            5.02682e00,
            5.35368e00,
            5.78498e00,
            6.26148e00,
            6.75459e00,
            7.15395e00,
            7.56538e00,
            8.03163e00,
            8.53049e00,
            9.17823e00,
            9.80145e00,
            1.03917e01,
            1.10268e01,
            1.17415e01,
            1.25181e01,
            1.33398e01,
            1.42200e01,
            1.51106e01,
            1.61355e01,
            1.73567e01,
            1.83418e01,
            1.91717e01,
            2.01210e01,
            2.12396e01,
            2.25308e01,
            2.41208e01,
            2.53677e01,
            2.69370e01,
            2.84042e01,
            2.94949e01,
            3.04401e01,
            3.15425e01,
            3.30825e01,
            3.46653e01,
            3.62672e01,
            3.76682e01,
            3.92680e01,
            4.07373e01,
            4.18383e01,
            4.27283e01,
            4.35855e01,
            4.49649e01,
            4.66677e01,
            4.80734e01,
            4.89720e01,
            4.99619e01,
            5.13093e01,
            5.28114e01,
            5.42053e01,
            5.58838e01,
            5.76461e01,
            5.89610e01,
            5.99379e01,
            6.07083e01,
            6.14663e01,
            6.20736e01,
            6.31599e01,
            6.41759e01,
            6.54932e01,
            6.66819e01,
            6.74808e01,
            6.79371e01,
            6.82598e01,
            6.91247e01,
            7.02168e01,
            7.14347e01,
            7.28298e01,
            7.42454e01,
            7.44859e01,
            7.47204e01,
            7.55505e01,
            7.69407e01,
            7.81143e01,
            7.80371e01,
            7.80112e01,
            7.78630e01,
            7.76227e01,
            7.75285e01,
            7.85333e01,
            7.98731e01,
            8.15713e01,
            8.42265e01,
            8.67693e01,
            8.97560e01,
            9.27840e01,
            9.54457e01,
            9.93008e01,
            1.04144e02,
            1.08518e02,
            1.12668e02,
            1.16727e02,
            1.20531e02,
            1.23923e02,
            1.27447e02,
            1.31520e02,
            1.35596e02,
            1.39490e02,
            1.42837e02,
            1.45527e02,
            1.48336e02,
            1.51055e02,
            1.53821e02,
            1.56916e02,
            1.60501e02,
            1.63148e02,
            1.65468e02,
            1.67406e02,
            1.69007e02,
            1.70423e02,
            1.71707e02,
            1.73739e02,
            1.75941e02,
            1.78018e02,
            1.80060e02,
            1.82093e02,
            1.85571e02,
            1.87928e02,
            1.89866e02,
            1.91641e02,
            1.94071e02,
            1.96953e02,
            1.99275e02,
            2.01028e02,
            2.02267e02,
            2.03127e02,
            2.04227e02,
            2.05772e02,
            2.07510e02,
            2.08857e02,
            2.09721e02,
            2.10494e02,
            2.10853e02,
            2.10798e02,
            2.10838e02,
            2.11416e02,
            2.12415e02,
            2.13372e02,
            2.14158e02,
            2.14304e02,
            2.14479e02,
            2.14242e02,
            2.13964e02,
            2.13740e02,
            2.13309e02,
            2.13233e02,
            2.12851e02,
            2.12569e02,
            2.12376e02,
            2.12262e02,
            2.12295e02,
            2.12322e02,
            2.12536e02,
            2.13078e02,
            2.13242e02,
            2.13209e02,
            2.13178e02,
            2.12987e02,
            2.12945e02,
            2.12918e02,
            2.12898e02,
            2.12911e02,
            2.12844e02,
            2.12907e02,
            2.12841e02,
            2.12558e02,
            2.12285e02,
            2.11784e02,
            2.11371e02,
            2.10940e02,
            2.10247e02,
        ],
    )


@component.add(
    name="IMV_SS_MnCrNi_Recycled",
    units="Mt/Year",
    comp_type="Auxiliary",
    comp_subtype="with Lookup",
    depends_on={"time": 1},
)
def imv_ss_mncrni_recycled():
    return np.interp(
        time(),
        [
            1850.0,
            1851.0,
            1852.0,
            1853.0,
            1854.0,
            1855.0,
            1856.0,
            1857.0,
            1858.0,
            1859.0,
            1860.0,
            1861.0,
            1862.0,
            1863.0,
            1864.0,
            1865.0,
            1866.0,
            1867.0,
            1868.0,
            1869.0,
            1870.0,
            1871.0,
            1872.0,
            1873.0,
            1874.0,
            1875.0,
            1876.0,
            1877.0,
            1878.0,
            1879.0,
            1880.0,
            1881.0,
            1882.0,
            1883.0,
            1884.0,
            1885.0,
            1886.0,
            1887.0,
            1888.0,
            1889.0,
            1890.0,
            1891.0,
            1892.0,
            1893.0,
            1894.0,
            1895.0,
            1896.0,
            1897.0,
            1898.0,
            1899.0,
            1900.0,
            1901.0,
            1902.0,
            1903.0,
            1904.0,
            1905.0,
            1906.0,
            1907.0,
            1908.0,
            1909.0,
            1910.0,
            1911.0,
            1912.0,
            1913.0,
            1914.0,
            1915.0,
            1916.0,
            1917.0,
            1918.0,
            1919.0,
            1920.0,
            1921.0,
            1922.0,
            1923.0,
            1924.0,
            1925.0,
            1926.0,
            1927.0,
            1928.0,
            1929.0,
            1930.0,
            1931.0,
            1932.0,
            1933.0,
            1934.0,
            1935.0,
            1936.0,
            1937.0,
            1938.0,
            1939.0,
            1940.0,
            1941.0,
            1942.0,
            1943.0,
            1944.0,
            1945.0,
            1946.0,
            1947.0,
            1948.0,
            1949.0,
            1950.0,
            1951.0,
            1952.0,
            1953.0,
            1954.0,
            1955.0,
            1956.0,
            1957.0,
            1958.0,
            1959.0,
            1960.0,
            1961.0,
            1962.0,
            1963.0,
            1964.0,
            1965.0,
            1966.0,
            1967.0,
            1968.0,
            1969.0,
            1970.0,
            1971.0,
            1972.0,
            1973.0,
            1974.0,
            1975.0,
            1976.0,
            1977.0,
            1978.0,
            1979.0,
            1980.0,
            1981.0,
            1982.0,
            1983.0,
            1984.0,
            1985.0,
            1986.0,
            1987.0,
            1988.0,
            1989.0,
            1990.0,
            1991.0,
            1992.0,
            1993.0,
            1994.0,
            1995.0,
            1996.0,
            1997.0,
            1998.0,
            1999.0,
            2000.0,
            2001.0,
            2002.0,
            2003.0,
            2004.0,
            2005.0,
            2006.0,
            2007.0,
            2008.0,
            2009.0,
            2010.0,
            2011.0,
            2012.0,
            2013.0,
            2014.0,
            2015.0,
            2016.0,
            2017.0,
            2018.0,
            2019.0,
            2020.0,
            2021.0,
            2022.0,
            2023.0,
            2024.0,
            2025.0,
            2026.0,
            2027.0,
            2028.0,
            2029.0,
            2030.0,
            2031.0,
            2032.0,
            2033.0,
            2034.0,
            2035.0,
            2036.0,
            2037.0,
            2038.0,
            2039.0,
            2040.0,
            2041.0,
            2042.0,
            2043.0,
            2044.0,
            2045.0,
            2046.0,
            2047.0,
            2048.0,
            2049.0,
            2050.0,
            2051.0,
            2052.0,
            2053.0,
            2054.0,
            2055.0,
            2056.0,
            2057.0,
            2058.0,
            2059.0,
            2060.0,
            2061.0,
            2062.0,
            2063.0,
            2064.0,
            2065.0,
            2066.0,
            2067.0,
            2068.0,
            2069.0,
            2070.0,
            2071.0,
            2072.0,
            2073.0,
            2074.0,
            2075.0,
            2076.0,
            2077.0,
            2078.0,
            2079.0,
            2080.0,
            2081.0,
            2082.0,
            2083.0,
            2084.0,
            2085.0,
            2086.0,
            2087.0,
            2088.0,
            2089.0,
            2090.0,
            2091.0,
            2092.0,
            2093.0,
            2094.0,
            2095.0,
            2096.0,
            2097.0,
            2098.0,
            2099.0,
            2100.0,
        ],
        [
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            9.41000e-07,
            8.88347e-06,
            2.16957e-05,
            3.65144e-05,
            5.15793e-05,
            6.80538e-05,
            9.08572e-05,
            1.16336e-04,
            1.42598e-04,
            1.68566e-04,
            2.03060e-04,
            2.51704e-04,
            3.09939e-04,
            3.74971e-04,
            4.50928e-04,
            5.30418e-04,
            6.17526e-04,
            7.65709e-04,
            1.16852e-03,
            2.09967e-03,
            3.43410e-03,
            4.56028e-03,
            5.54066e-03,
            6.28733e-03,
            6.89705e-03,
            7.26178e-03,
            7.27980e-03,
            7.06792e-03,
            6.63678e-03,
            6.04856e-03,
            5.35692e-03,
            4.66147e-03,
            4.02005e-03,
            3.65092e-03,
            3.54119e-03,
            3.60058e-03,
            3.75635e-03,
            3.96683e-03,
            4.20523e-03,
            4.49088e-03,
            4.51837e-03,
            4.22828e-03,
            3.80353e-03,
            3.34194e-03,
            2.89347e-03,
            2.48149e-03,
            2.11488e-03,
            1.79491e-03,
            1.51907e-03,
            1.28318e-03,
            1.08251e-03,
            9.12414e-04,
            7.68583e-04,
            6.47157e-04,
            5.44761e-04,
            4.58478e-04,
            3.85810e-04,
            3.24630e-04,
            2.73135e-04,
            2.29798e-04,
            1.93332e-04,
            1.62649e-04,
            1.36834e-04,
            1.15115e-04,
            9.68427e-05,
            8.14705e-05,
            6.85381e-05,
            5.76585e-05,
            4.85058e-05,
            4.08060e-05,
            3.43284e-05,
            2.88791e-05,
            2.42948e-05,
            2.09352e-05,
            3.19253e-03,
            1.00825e-02,
            1.76402e-02,
            2.36224e-02,
            2.75122e-02,
            3.03989e-02,
            3.36875e-02,
            3.72136e-02,
            4.04108e-02,
            4.31878e-02,
            4.69428e-02,
            5.02937e-02,
            5.18176e-02,
            5.23871e-02,
            5.33999e-02,
            5.68140e-02,
            6.17890e-02,
            6.91397e-02,
            7.29633e-02,
            7.44156e-02,
            7.74655e-02,
            8.04425e-02,
            9.11689e-02,
            1.21192e-01,
            1.65373e-01,
            2.24057e-01,
            2.91604e-01,
            3.57063e-01,
            4.08401e-01,
            4.47784e-01,
            4.79958e-01,
            5.07288e-01,
            5.32022e-01,
            5.65830e-01,
            6.08089e-01,
            6.48468e-01,
            6.73603e-01,
            6.88915e-01,
            7.16787e-01,
            7.67420e-01,
            8.36332e-01,
            8.99443e-01,
            9.18106e-01,
            8.90150e-01,
            8.34591e-01,
            7.70004e-01,
            7.05645e-01,
            6.45366e-01,
            5.90887e-01,
            5.42782e-01,
            5.00957e-01,
            4.64854e-01,
            4.34494e-01,
            4.09528e-01,
            3.89356e-01,
            3.62416e-01,
            3.25048e-01,
            2.85083e-01,
            2.46540e-01,
            2.11276e-01,
            1.79972e-01,
            1.52691e-01,
            1.29197e-01,
            1.09117e-01,
            9.20428e-02,
            7.75745e-02,
            6.53426e-02,
            5.50175e-02,
            4.63113e-02,
            3.89756e-02,
            3.27976e-02,
            2.75965e-02,
            2.32188e-02,
            1.95348e-02,
            1.64348e-02,
            1.38265e-02,
            1.16320e-02,
            9.78569e-03,
            8.23240e-03,
            6.92563e-03,
            5.82628e-03,
            4.90143e-03,
            4.12337e-03,
            3.46883e-03,
            2.91818e-03,
            2.45495e-03,
            2.06524e-03,
            1.73740e-03,
            1.46160e-03,
            2.72684e-03,
            3.54143e-02,
            9.37949e-02,
            1.61009e-01,
            2.28745e-01,
            2.90979e-01,
            3.23344e-01,
            3.30467e-01,
            3.25181e-01,
            3.13937e-01,
            3.02229e-01,
            2.91933e-01,
            2.83494e-01,
            2.91570e-01,
            3.54473e-01,
            4.49408e-01,
            5.61704e-01,
            7.00916e-01,
            8.50639e-01,
            9.99259e-01,
            1.14099e00,
            1.27265e00,
            1.39227e00,
            1.52182e00,
            1.66564e00,
            1.82540e00,
            1.99937e00,
            2.17674e00,
            2.36866e00,
            2.57164e00,
            2.78859e00,
            3.00708e00,
            3.21529e00,
            3.40812e00,
            3.58416e00,
            3.75084e00,
            3.91540e00,
            4.08153e00,
            4.24547e00,
            4.41434e00,
            4.57372e00,
            4.72408e00,
            4.86628e00,
            5.00074e00,
            5.13724e00,
            5.26744e00,
            5.38835e00,
            5.51121e00,
            5.64347e00,
            5.78599e00,
            5.93475e00,
            6.08828e00,
            6.25000e00,
            6.41572e00,
            6.58897e00,
        ],
    )


@component.add(
    name="IMV_SS_MnCrNi_recycled_two",
    comp_type="Auxiliary",
    comp_subtype="with Lookup",
    depends_on={"time": 1},
)
def imv_ss_mncrni_recycled_two():
    return np.interp(
        time(),
        [
            2005.0,
            2006.0,
            2007.0,
            2008.0,
            2009.0,
            2010.0,
            2011.0,
            2012.0,
            2013.0,
            2014.0,
            2015.0,
            2016.0,
            2017.0,
            2018.0,
            2019.0,
            2020.0,
            2021.0,
            2022.0,
            2023.0,
            2024.0,
            2025.0,
            2026.0,
            2027.0,
            2028.0,
            2029.0,
            2030.0,
            2031.0,
            2032.0,
            2033.0,
            2034.0,
            2035.0,
            2036.0,
            2037.0,
            2038.0,
            2039.0,
            2040.0,
            2041.0,
            2042.0,
            2043.0,
            2044.0,
            2045.0,
            2046.0,
            2047.0,
            2048.0,
            2049.0,
            2050.0,
            2051.0,
            2052.0,
            2053.0,
            2054.0,
            2055.0,
            2056.0,
            2057.0,
            2058.0,
            2059.0,
            2060.0,
            2061.0,
            2062.0,
            2063.0,
            2064.0,
            2065.0,
            2066.0,
            2067.0,
            2068.0,
            2069.0,
            2070.0,
            2071.0,
            2072.0,
            2073.0,
            2074.0,
            2075.0,
            2076.0,
            2077.0,
            2078.0,
            2079.0,
            2080.0,
            2081.0,
            2082.0,
            2083.0,
            2084.0,
            2085.0,
            2086.0,
            2087.0,
            2088.0,
            2089.0,
            2090.0,
            2091.0,
            2092.0,
            2093.0,
            2094.0,
            2095.0,
            2096.0,
            2097.0,
            2098.0,
            2099.0,
            2100.0,
        ],
        [
            9.80051,
            9.34287,
            9.22719,
            9.2907,
            9.50508,
            9.77693,
            10.2108,
            12.5851,
            14.5118,
            15.9696,
            16.2652,
            16.5175,
            16.843,
            17.1949,
            17.5216,
            17.8137,
            17.9553,
            18.107,
            18.1964,
            18.3108,
            18.4178,
            18.5212,
            18.6368,
            18.7214,
            18.7891,
            18.8439,
            18.8908,
            18.9392,
            18.9959,
            19.014,
            19.0075,
            19.0369,
            19.1095,
            19.2063,
            19.3538,
            19.5061,
            19.5532,
            19.5422,
            19.5168,
            19.5038,
            19.4812,
            19.4357,
            19.3865,
            19.3395,
            19.2998,
            19.3901,
            19.4292,
            19.4352,
            19.473,
            19.5429,
            19.5215,
            19.5811,
            19.7107,
            19.7015,
            19.7231,
            19.7486,
            19.7554,
            19.7876,
            19.8212,
            19.8499,
            19.8841,
            19.9259,
            19.9714,
            20.011,
            20.0284,
            20.0582,
            20.0715,
            20.1529,
            20.2587,
            20.3563,
            20.446,
            20.5118,
            20.554,
            20.5558,
            20.5542,
            20.5588,
            20.5615,
            20.5448,
            20.5301,
            20.5246,
            20.532,
            20.5498,
            20.5767,
            20.6104,
            20.646,
            20.6824,
            20.7197,
            20.7585,
            20.7966,
            20.8169,
            20.8687,
            20.9514,
            21.006,
            21.1045,
            21.2069,
            21.2625,
        ],
    )


@component.add(
    name="IMV_SS_Ni_WANTED",
    units="Mt/Years",
    comp_type="Auxiliary",
    comp_subtype="with Lookup",
    depends_on={"time": 1},
)
def imv_ss_ni_wanted():
    """
    IMV from stainless steel module
    """
    return np.interp(
        time(),
        [
            1850.0,
            1851.0,
            1852.0,
            1853.0,
            1854.0,
            1855.0,
            1856.0,
            1857.0,
            1858.0,
            1859.0,
            1860.0,
            1861.0,
            1862.0,
            1863.0,
            1864.0,
            1865.0,
            1866.0,
            1867.0,
            1868.0,
            1869.0,
            1870.0,
            1871.0,
            1872.0,
            1873.0,
            1874.0,
            1875.0,
            1876.0,
            1877.0,
            1878.0,
            1879.0,
            1880.0,
            1881.0,
            1882.0,
            1883.0,
            1884.0,
            1885.0,
            1886.0,
            1887.0,
            1888.0,
            1889.0,
            1890.0,
            1891.0,
            1892.0,
            1893.0,
            1894.0,
            1895.0,
            1896.0,
            1897.0,
            1898.0,
            1899.0,
            1900.0,
            1901.0,
            1902.0,
            1903.0,
            1904.0,
            1905.0,
            1906.0,
            1907.0,
            1908.0,
            1909.0,
            1910.0,
            1911.0,
            1912.0,
            1913.0,
            1914.0,
            1915.0,
            1916.0,
            1917.0,
            1918.0,
            1919.0,
            1920.0,
            1921.0,
            1922.0,
            1923.0,
            1924.0,
            1925.0,
            1926.0,
            1927.0,
            1928.0,
            1929.0,
            1930.0,
            1931.0,
            1932.0,
            1933.0,
            1934.0,
            1935.0,
            1936.0,
            1937.0,
            1938.0,
            1939.0,
            1940.0,
            1941.0,
            1942.0,
            1943.0,
            1944.0,
            1945.0,
            1946.0,
            1947.0,
            1948.0,
            1949.0,
            1950.0,
            1951.0,
            1952.0,
            1953.0,
            1954.0,
            1955.0,
            1956.0,
            1957.0,
            1958.0,
            1959.0,
            1960.0,
            1961.0,
            1962.0,
            1963.0,
            1964.0,
            1965.0,
            1966.0,
            1967.0,
            1968.0,
            1969.0,
            1970.0,
            1971.0,
            1972.0,
            1973.0,
            1974.0,
            1975.0,
            1976.0,
            1977.0,
            1978.0,
            1979.0,
            1980.0,
            1981.0,
            1982.0,
            1983.0,
            1984.0,
            1985.0,
            1986.0,
            1987.0,
            1988.0,
            1989.0,
            1990.0,
            1991.0,
            1992.0,
            1993.0,
            1994.0,
            1995.0,
            1996.0,
            1997.0,
            1998.0,
            1999.0,
            2000.0,
            2001.0,
            2002.0,
            2003.0,
            2004.0,
            2005.0,
            2006.0,
            2007.0,
            2008.0,
            2009.0,
            2010.0,
            2011.0,
            2012.0,
            2013.0,
            2014.0,
            2015.0,
            2016.0,
            2017.0,
            2018.0,
            2019.0,
            2020.0,
            2021.0,
            2022.0,
            2023.0,
            2024.0,
            2025.0,
            2026.0,
            2027.0,
            2028.0,
            2029.0,
            2030.0,
            2031.0,
            2032.0,
            2033.0,
            2034.0,
            2035.0,
            2036.0,
            2037.0,
            2038.0,
            2039.0,
            2040.0,
            2041.0,
            2042.0,
            2043.0,
            2044.0,
            2045.0,
            2046.0,
            2047.0,
            2048.0,
            2049.0,
            2050.0,
            2051.0,
            2052.0,
            2053.0,
            2054.0,
            2055.0,
            2056.0,
            2057.0,
            2058.0,
            2059.0,
            2060.0,
            2061.0,
            2062.0,
            2063.0,
            2064.0,
            2065.0,
            2066.0,
            2067.0,
            2068.0,
            2069.0,
            2070.0,
            2071.0,
            2072.0,
            2073.0,
            2074.0,
            2075.0,
            2076.0,
            2077.0,
            2078.0,
            2079.0,
            2080.0,
            2081.0,
            2082.0,
            2083.0,
            2084.0,
            2085.0,
            2086.0,
            2087.0,
            2088.0,
            2089.0,
            2090.0,
            2091.0,
            2092.0,
            2093.0,
            2094.0,
            2095.0,
            2096.0,
            2097.0,
            2098.0,
            2099.0,
            2100.0,
        ],
        [
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            4.68000e-04,
            5.12000e-04,
            5.42000e-04,
            5.57000e-04,
            5.66000e-04,
            1.09000e-03,
            1.11000e-03,
            1.19500e-03,
            1.22100e-03,
            1.97300e-03,
            2.52900e-03,
            2.94000e-03,
            3.34700e-03,
            4.56900e-03,
            4.68700e-03,
            4.93800e-03,
            6.68400e-03,
            9.84300e-03,
            8.27800e-03,
            8.07000e-03,
            9.51300e-03,
            1.21290e-02,
            1.66780e-02,
            2.26100e-02,
            2.66550e-02,
            2.98650e-02,
            3.17350e-02,
            3.34420e-02,
            3.33980e-02,
            3.37100e-02,
            3.40540e-02,
            3.69020e-02,
            4.09660e-02,
            4.42060e-02,
            5.18930e-02,
            5.23420e-02,
            5.67780e-02,
            6.09090e-02,
            6.70470e-02,
            7.36920e-02,
            8.12780e-02,
            8.52770e-02,
            9.23380e-02,
            9.51180e-02,
            1.03591e-01,
            1.09899e-01,
            1.17565e-01,
            1.22027e-01,
            1.27031e-01,
            1.36272e-01,
            1.48932e-01,
            1.54297e-01,
            1.63276e-01,
            1.66096e-01,
            1.88030e-01,
            2.07876e-01,
            2.17189e-01,
            2.41232e-01,
            2.50822e-01,
            2.63611e-01,
            2.80745e-01,
            2.99219e-01,
            3.14167e-01,
            3.31814e-01,
            3.42913e-01,
            3.48596e-01,
            3.87171e-01,
            3.97553e-01,
            4.06229e-01,
            4.27213e-01,
            4.59740e-01,
            4.81731e-01,
            5.17440e-01,
            5.24690e-01,
            5.32047e-01,
            5.84463e-01,
            5.85964e-01,
            5.92555e-01,
            6.10192e-01,
            6.42209e-01,
            6.80211e-01,
            7.04577e-01,
            7.06162e-01,
            7.29273e-01,
            7.58499e-01,
            7.64758e-01,
            7.67298e-01,
            7.75911e-01,
            8.05283e-01,
            8.55745e-01,
            9.18733e-01,
            8.70089e-01,
            8.71386e-01,
            9.14359e-01,
            9.37103e-01,
            9.77777e-01,
            1.10294e00,
            1.65583e00,
            1.89528e00,
            1.98331e00,
            2.01990e00,
            2.05533e00,
            2.05771e00,
            2.11757e00,
            2.15274e00,
            2.20604e00,
            2.25364e00,
            2.28153e00,
            2.26822e00,
            2.26529e00,
            2.29216e00,
            2.35369e00,
            2.40457e00,
            2.46045e00,
            2.50247e00,
            1.45144e00,
            1.31712e00,
            1.33231e00,
            1.38475e00,
            1.40873e00,
            1.36432e00,
            1.35097e00,
            1.33093e00,
            1.33401e00,
            1.32449e00,
            1.37601e00,
            1.41808e00,
            1.50289e00,
            1.61267e00,
            1.76742e00,
            1.84656e00,
            1.90148e00,
            1.95644e00,
            2.01679e00,
            2.27734e00,
            2.33936e00,
            2.39081e00,
            2.45965e00,
            2.51967e00,
            2.56293e00,
            2.62665e00,
            2.71208e00,
            2.82250e00,
            2.86063e00,
            2.91745e00,
            2.96949e00,
            2.99897e00,
            3.07418e00,
            3.07087e00,
            3.08854e00,
            3.17305e00,
            3.17117e00,
            3.14973e00,
            3.19133e00,
            3.18461e00,
            3.19581e00,
            3.23696e00,
            3.23687e00,
            3.31474e00,
            3.30865e00,
            3.32163e00,
            3.30153e00,
            3.35292e00,
            3.37061e00,
            3.34783e00,
            3.34641e00,
            3.37795e00,
            3.43010e00,
            3.46831e00,
            3.45242e00,
            3.44529e00,
            3.43153e00,
            3.43641e00,
            3.44612e00,
            3.51419e00,
            3.51822e00,
            5.63950e00,
            6.47581e00,
            6.79456e00,
            6.85180e00,
            6.88943e00,
            6.93470e00,
            7.00503e00,
            7.05758e00,
            7.07695e00,
            7.05299e00,
            7.04877e00,
            7.03125e00,
            7.00129e00,
            7.00130e00,
            6.97784e00,
            6.98480e00,
            6.96645e00,
            6.95523e00,
            6.95523e00,
            6.95523e00,
            6.96335e00,
            6.96761e00,
            6.97534e00,
            7.00623e00,
            7.04100e00,
            6.98281e00,
            6.99958e00,
            6.98339e00,
            6.97271e00,
            7.00156e00,
            6.97143e00,
            6.98728e00,
            6.98728e00,
            6.97499e00,
            7.00034e00,
            6.96773e00,
            6.94762e00,
            6.93324e00,
            6.89830e00,
            6.91507e00,
            6.86615e00,
            6.84528e00,
        ],
    )


@component.add(
    name="IMV_SS_SLOW_IN_USE",
    units="Mt",
    comp_type="Auxiliary",
    comp_subtype="with Lookup",
    depends_on={"time": 1},
)
def imv_ss_slow_in_use():
    return np.interp(
        time(),
        [
            1850.0,
            1851.0,
            1852.0,
            1853.0,
            1854.0,
            1855.0,
            1856.0,
            1857.0,
            1858.0,
            1859.0,
            1860.0,
            1861.0,
            1862.0,
            1863.0,
            1864.0,
            1865.0,
            1866.0,
            1867.0,
            1868.0,
            1869.0,
            1870.0,
            1871.0,
            1872.0,
            1873.0,
            1874.0,
            1875.0,
            1876.0,
            1877.0,
            1878.0,
            1879.0,
            1880.0,
            1881.0,
            1882.0,
            1883.0,
            1884.0,
            1885.0,
            1886.0,
            1887.0,
            1888.0,
            1889.0,
            1890.0,
            1891.0,
            1892.0,
            1893.0,
            1894.0,
            1895.0,
            1896.0,
            1897.0,
            1898.0,
            1899.0,
            1900.0,
            1901.0,
            1902.0,
            1903.0,
            1904.0,
            1905.0,
            1906.0,
            1907.0,
            1908.0,
            1909.0,
            1910.0,
            1911.0,
            1912.0,
            1913.0,
            1914.0,
            1915.0,
            1916.0,
            1917.0,
            1918.0,
            1919.0,
            1920.0,
            1921.0,
            1922.0,
            1923.0,
            1924.0,
            1925.0,
            1926.0,
            1927.0,
            1928.0,
            1929.0,
            1930.0,
            1931.0,
            1932.0,
            1933.0,
            1934.0,
            1935.0,
            1936.0,
            1937.0,
            1938.0,
            1939.0,
            1940.0,
            1941.0,
            1942.0,
            1943.0,
            1944.0,
            1945.0,
            1946.0,
            1947.0,
            1948.0,
            1949.0,
            1950.0,
            1951.0,
            1952.0,
            1953.0,
            1954.0,
            1955.0,
            1956.0,
            1957.0,
            1958.0,
            1959.0,
            1960.0,
            1961.0,
            1962.0,
            1963.0,
            1964.0,
            1965.0,
            1966.0,
            1967.0,
            1968.0,
            1969.0,
            1970.0,
            1971.0,
            1972.0,
            1973.0,
            1974.0,
            1975.0,
            1976.0,
            1977.0,
            1978.0,
            1979.0,
            1980.0,
            1981.0,
            1982.0,
            1983.0,
            1984.0,
            1985.0,
            1986.0,
            1987.0,
            1988.0,
            1989.0,
            1990.0,
            1991.0,
            1992.0,
            1993.0,
            1994.0,
            1995.0,
            1996.0,
            1997.0,
            1998.0,
            1999.0,
            2000.0,
            2001.0,
            2002.0,
            2003.0,
            2004.0,
            2005.0,
            2006.0,
            2007.0,
            2008.0,
            2009.0,
            2010.0,
            2011.0,
            2012.0,
            2013.0,
            2014.0,
            2015.0,
            2016.0,
            2017.0,
            2018.0,
            2019.0,
            2020.0,
            2021.0,
            2022.0,
            2023.0,
            2024.0,
            2025.0,
            2026.0,
            2027.0,
            2028.0,
            2029.0,
            2030.0,
            2031.0,
            2032.0,
            2033.0,
            2034.0,
            2035.0,
            2036.0,
            2037.0,
            2038.0,
            2039.0,
            2040.0,
            2041.0,
            2042.0,
            2043.0,
            2044.0,
            2045.0,
            2046.0,
            2047.0,
            2048.0,
            2049.0,
            2050.0,
            2051.0,
            2052.0,
            2053.0,
            2054.0,
            2055.0,
            2056.0,
            2057.0,
            2058.0,
            2059.0,
            2060.0,
            2061.0,
            2062.0,
            2063.0,
            2064.0,
            2065.0,
            2066.0,
            2067.0,
            2068.0,
            2069.0,
            2070.0,
            2071.0,
            2072.0,
            2073.0,
            2074.0,
            2075.0,
            2076.0,
            2077.0,
            2078.0,
            2079.0,
            2080.0,
            2081.0,
            2082.0,
            2083.0,
            2084.0,
            2085.0,
            2086.0,
            2087.0,
            2088.0,
            2089.0,
            2090.0,
            2091.0,
            2092.0,
            2093.0,
            2094.0,
            2095.0,
            2096.0,
            2097.0,
            2098.0,
            2099.0,
            2100.0,
        ],
        [
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            0.00000e00,
            1.10400e-03,
            3.92400e-03,
            6.83300e-03,
            9.70300e-03,
            1.25100e-02,
            1.70150e-02,
            2.24910e-02,
            2.80340e-02,
            3.35950e-02,
            3.98980e-02,
            5.03030e-02,
            6.36020e-02,
            7.70730e-02,
            9.47180e-02,
            1.15314e-01,
            1.35549e-01,
            1.60144e-01,
            1.91435e-01,
            2.27305e-01,
            2.53199e-01,
            2.81621e-01,
            3.20829e-01,
            3.72920e-01,
            4.49517e-01,
            5.48342e-01,
            6.56580e-01,
            7.75175e-01,
            8.99653e-01,
            1.02774e00,
            1.16463e00,
            1.30994e00,
            1.47522e00,
            1.66130e00,
            1.86410e00,
            2.08933e00,
            2.31879e00,
            2.55693e00,
            2.79524e00,
            3.03708e00,
            3.31078e00,
            3.61059e00,
            3.91906e00,
            4.23073e00,
            4.55018e00,
            4.87543e00,
            5.20827e00,
            5.58570e00,
            5.98180e00,
            6.38838e00,
            6.83004e00,
            7.33071e00,
            7.87884e00,
            8.46712e00,
            9.05165e00,
            9.66057e00,
            1.03125e01,
            1.10039e01,
            1.17799e01,
            1.25914e01,
            1.34278e01,
            1.43136e01,
            1.52664e01,
            1.62864e01,
            1.73712e01,
            1.85278e01,
            1.97431e01,
            2.10577e01,
            2.25169e01,
            2.39666e01,
            2.54054e01,
            2.69223e01,
            2.85503e01,
            3.03011e01,
            3.22502e01,
            3.41692e01,
            3.62679e01,
            3.84289e01,
            4.05208e01,
            4.25880e01,
            4.47291e01,
            4.70742e01,
            4.95150e01,
            5.20455e01,
            5.45714e01,
            5.72246e01,
            5.99006e01,
            6.24866e01,
            6.50003e01,
            6.74864e01,
            7.01570e01,
            7.29991e01,
            7.58067e01,
            7.84523e01,
            8.11085e01,
            8.39029e01,
            8.67853e01,
            8.96804e01,
            9.27097e01,
            9.58401e01,
            9.88651e01,
            1.01774e02,
            1.04579e02,
            1.07341e02,
            1.09995e02,
            1.12790e02,
            1.15553e02,
            1.18427e02,
            1.21276e02,
            1.23986e02,
            1.26529e02,
            1.28948e02,
            1.31499e02,
            1.34123e02,
            1.36803e02,
            1.39576e02,
            1.42395e02,
            1.44806e02,
            1.47116e02,
            1.49569e02,
            1.52228e02,
            1.54854e02,
            1.57006e02,
            1.59069e02,
            1.60976e02,
            1.62740e02,
            1.64432e02,
            1.66462e02,
            1.68645e02,
            1.71030e02,
            1.73885e02,
            1.76892e02,
            1.80236e02,
            1.83808e02,
            1.87448e02,
            1.91681e02,
            1.96598e02,
            2.01692e02,
            2.06986e02,
            2.12506e02,
            2.18170e02,
            2.23862e02,
            2.29758e02,
            2.36010e02,
            2.42477e02,
            2.49060e02,
            2.55603e02,
            2.61992e02,
            2.68433e02,
            2.74889e02,
            2.81384e02,
            2.88023e02,
            2.94933e02,
            3.01587e02,
            3.08111e02,
            3.14464e02,
            3.20615e02,
            3.26590e02,
            3.32403e02,
            3.38369e02,
            3.44379e02,
            3.50314e02,
            3.56212e02,
            3.62060e02,
            3.68450e02,
            3.74530e02,
            3.80441e02,
            3.86236e02,
            3.92221e02,
            3.98399e02,
            4.04423e02,
            4.10221e02,
            4.15755e02,
            4.21023e02,
            4.26235e02,
            4.31492e02,
            4.36771e02,
            4.41864e02,
            4.46681e02,
            4.51336e02,
            4.55707e02,
            4.59740e02,
            4.63604e02,
            4.67491e02,
            4.71427e02,
            4.75282e02,
            4.79005e02,
            4.82391e02,
            4.85645e02,
            4.88602e02,
            4.91366e02,
            4.93985e02,
            4.96365e02,
            4.98718e02,
            5.00824e02,
            5.02816e02,
            5.04712e02,
            5.06521e02,
            5.08286e02,
            5.09966e02,
            5.11639e02,
            5.13384e02,
            5.14976e02,
            5.16424e02,
            5.17801e02,
            5.19044e02,
            5.20255e02,
            5.21417e02,
            5.22515e02,
            5.23572e02,
            5.24549e02,
            5.25514e02,
            5.26397e02,
            5.27144e02,
            5.27821e02,
            5.28344e02,
            5.28809e02,
            5.29201e02,
            5.29413e02,
        ],
    )


@component.add(
    name="increase_Ni_cumulative",
    units="Mt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ni_total_mining": 1},
)
def increase_ni_cumulative():
    """
    Flow to track cumulative Nickel mining
    """
    return ni_total_mining()


@component.add(
    name="increase_Ni_plating",
    units="Mt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ni_supply_to_society": 1},
)
def increase_ni_plating():
    """
    Input of nickel as being plated onto objects
    """
    return ni_supply_to_society() * 0.08


@component.add(
    name="INITIAL_DELAYED_TS_Ni_PROFIT_AVERAGE",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_delayed_ts_ni_profit_average"},
)
def initial_delayed_ts_ni_profit_average():
    """
    The initial values for the cu known stocks are based on simulation outputs from the world7 for the year 2005. The world7 outputs are based on initial values from 1900. Source: Sverdrup, H. U., & Olafsdottir, A. H. (2019). On the long-term sustainability of copper, zinc and lead supply, using a system dynamics model. Resources, Conservation & Recycling: X, 4(100007). https://doi.org/https://doi.org/10.1016/j.rcrx.2019.100007
    """
    return _ext_constant_initial_delayed_ts_ni_profit_average()


_ext_constant_initial_delayed_ts_ni_profit_average = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Nickel",
    "INITIAL_DELAYED_TS_Ni_PROFIT_AVERAGE",
    {},
    _root,
    {},
    "_ext_constant_initial_delayed_ts_ni_profit_average",
)


@component.add(
    name="INITIAL_Ni_CUMULATIVE_MINING",
    units="Mt",
    comp_type="Constant",
    comp_subtype="Normal",
)
def initial_ni_cumulative_mining():
    """
    Cumulative Nickel mined until 2005 based on source;
    """
    return 69.42


@component.add(
    name="INITIAL_Ni_HIDDEN_RESOURCES",
    units="Mt",
    subscripts=["ORE_GRADES_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_ni_hidden_resources"},
)
def initial_ni_hidden_resources():
    """
    The initial values for the Ni hidden stocks are based on simulation outputs from the world7 for the year 2005. The world7 outputs are based on numbers for in 1900 that were stratified with respect to ore metal content and relative extraction cost based on yield of extraction and energy requirements. The WILLIAM, 2005 initial values are therefore the following for the hidden resources: Ni Hidden Rich 0,004738168 Ni Hidden High 8,4201801 Ni Hidden low 34,44477713 Ni Hidden ULG 168,0875823 Ni Hidden Trace 156 values based on simplification above Ni hidden resources[RICH GRADE] Ni hidden resources[HIGH GRADE] Ni hidden resources[LOW GRADE] Ni hidden resources[ULTRALOW GRADE] Ni hidden resources[TRACE GRADE] Ni hidden resources[OCEANS GRADE] 0,000430742540576 3,51568728811 128,237627352 175,003104349 175 0
    """
    return _ext_constant_initial_ni_hidden_resources()


_ext_constant_initial_ni_hidden_resources = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Nickel",
    "INITIAL_Ni_HIDDEN_RESOURCES*",
    {"ORE_GRADES_I": _subscript_dict["ORE_GRADES_I"]},
    _root,
    {"ORE_GRADES_I": _subscript_dict["ORE_GRADES_I"]},
    "_ext_constant_initial_ni_hidden_resources",
)


@component.add(
    name="INITIAL_Ni_KNOWN_RESERVES",
    units="Mt",
    subscripts=["ORE_GRADES_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_ni_known_reserves"},
)
def initial_ni_known_reserves():
    """
    The initial values for the Ni known stocks are based on simulation outputs from the world7 for the year 2005. The world7 outputs are based on initial values from 1900 that were stratified with respect to ore metal content and relative extraction cost based on yield of extraction and energy requirements. Ni Known HG 29,56360868 Ni Known LG 117,4105285 Ni Known Rich 2,054750863 Ni Known trace 20 Ni Known ULG 33,91241765
    """
    return _ext_constant_initial_ni_known_reserves()


_ext_constant_initial_ni_known_reserves = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Nickel",
    "INITIAL_Ni_KNOWN_RESERVES*",
    {"ORE_GRADES_I": _subscript_dict["ORE_GRADES_I"]},
    _root,
    {"ORE_GRADES_I": _subscript_dict["ORE_GRADES_I"]},
    "_ext_constant_initial_ni_known_reserves",
)


@component.add(
    name="INITIAL_Ni_MARKET",
    units="Mt",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_ni_market"},
)
def initial_ni_market():
    """
    The initial values for the gas market are based on simulation outputs from the world7 for the year 2005. The world7 outputs are based on initial values from 1900 that were stratified with respect to ore metal content and relative extraction cost based on yield of extraction and energy requirements. 0,328867831362
    """
    return _ext_constant_initial_ni_market()


_ext_constant_initial_ni_market = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Nickel",
    "INITIAL_Ni_MARKET",
    {},
    _root,
    {},
    "_ext_constant_initial_ni_market",
)


@component.add(
    name="INITIAL_Ni_OTHER_USE",
    units="Mt",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_ni_other_use"},
)
def initial_ni_other_use():
    """
    The initial values for the Ni other use are based on simulation outputs from the world7 for the year 2005. The world7 outputs are based on numbers for in 1900 that were stratified with respect to ore metal content and relative extraction cost based on yield of extraction and energy requirements.
    """
    return _ext_constant_initial_ni_other_use()


_ext_constant_initial_ni_other_use = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Nickel",
    "INITIAL_Ni_OTHER_USE",
    {},
    _root,
    {},
    "_ext_constant_initial_ni_other_use",
)


@component.add(
    name="INITIAL_Ni_PLATING",
    units="Mt",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_ni_plating"},
)
def initial_ni_plating():
    """
    The initial values for the oil hidden stocks are based on simulation outputs from the world7 for the year 2005. The world7 outputs are based on numbers for in 1900 that were stratified with respect to ore metal content and relative extraction cost based on yield of extraction and energy requirements.
    """
    return _ext_constant_initial_ni_plating()


_ext_constant_initial_ni_plating = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Nickel",
    "INITIAL_Ni_PLATING",
    {},
    _root,
    {},
    "_ext_constant_initial_ni_plating",
)


@component.add(
    name="INITIAL_Ni_SCRAP",
    units="Mt",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_ni_scrap"},
)
def initial_ni_scrap():
    """
    The initial values for the cu known stocks are based on simulation outputs from the world7 for the year 2005. The world7 outputs are based on initial values from 1900. 0,024759307629
    """
    return _ext_constant_initial_ni_scrap()


_ext_constant_initial_ni_scrap = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Nickel",
    "INITIAL_Ni_SCRAP",
    {},
    _root,
    {},
    "_ext_constant_initial_ni_scrap",
)


@component.add(
    name="mining_cost_Ni_$ton",
    units="M$/Mt",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "ni_recycling": 2,
        "ni_grade_cost": 7,
        "ni_mining": 12,
        "avoid_zero_division": 1,
    },
)
def mining_cost_ni_ton():
    """
    Summing up all extraction costs
    """
    return (
        ni_recycling() * float(ni_grade_cost().loc["HIGH_GRADE"])
        + float(ni_grade_cost().loc["RICH_GRADE"])
        * float(ni_mining().loc["RICH_GRADE"])
        + float(ni_mining().loc["HIGH_GRADE"])
        * float(ni_grade_cost().loc["HIGH_GRADE"])
        + float(ni_mining().loc["LOW_GRADE"]) * float(ni_grade_cost().loc["LOW_GRADE"])
        + float(ni_mining().loc["ULTRALOW_GRADE"])
        * float(ni_grade_cost().loc["ULTRALOW_GRADE"])
        + float(ni_mining().loc["TRACE_GRADE"])
        * float(ni_grade_cost().loc["TRACE_GRADE"])
        + float(ni_mining().loc["OCEANS_GRADE"])
        * float(ni_grade_cost().loc["OCEANS_GRADE"])
    ) / (
        float(ni_mining().loc["RICH_GRADE"])
        + float(ni_mining().loc["HIGH_GRADE"])
        + float(ni_mining().loc["LOW_GRADE"])
        + float(ni_mining().loc["ULTRALOW_GRADE"])
        + float(ni_mining().loc["TRACE_GRADE"])
        + float(ni_mining().loc["OCEANS_GRADE"])
        + ni_recycling()
        + avoid_zero_division()
    )


@component.add(
    name="mining_technology_improvements_for_NI",
    units="DMNL",
    subscripts=["ORE_GRADES_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={"coefficients_mining_technology_improvements": 9, "time": 3},
)
def mining_technology_improvements_for_ni():
    """
    The improvement in technology is based on it being the same as for copper. The technologies used are the same
    """
    value = xr.DataArray(
        np.nan, {"ORE_GRADES_I": _subscript_dict["ORE_GRADES_I"]}, ["ORE_GRADES_I"]
    )
    value.loc[["RICH_GRADE"]] = 0
    value.loc[["HIGH_GRADE"]] = 0
    value.loc[["LOW_GRADE"]] = float(
        coefficients_mining_technology_improvements().loc["LOW_GRADE", "A_S_CURVE"]
    ) / (
        1
        + np.exp(
            -float(
                coefficients_mining_technology_improvements().loc[
                    "LOW_GRADE", "B_S_CURVE"
                ]
            )
            * (
                time()
                - float(
                    coefficients_mining_technology_improvements().loc[
                        "LOW_GRADE", "C_S_CURVE"
                    ]
                )
            )
        )
    )
    value.loc[["ULTRALOW_GRADE"]] = float(
        coefficients_mining_technology_improvements().loc["ULTRALOW_GRADE", "A_S_CURVE"]
    ) / (
        1
        + np.exp(
            -float(
                coefficients_mining_technology_improvements().loc[
                    "ULTRALOW_GRADE", "B_S_CURVE"
                ]
            )
            * (
                time()
                - float(
                    coefficients_mining_technology_improvements().loc[
                        "ULTRALOW_GRADE", "C_S_CURVE"
                    ]
                )
            )
        )
    )
    value.loc[["TRACE_GRADE"]] = float(
        coefficients_mining_technology_improvements().loc["TRACE_GRADE", "A_S_CURVE"]
    ) / (
        1
        + np.exp(
            -float(
                coefficients_mining_technology_improvements().loc[
                    "TRACE_GRADE", "B_S_CURVE"
                ]
            )
            * (
                time()
                - float(
                    coefficients_mining_technology_improvements().loc[
                        "TRACE_GRADE", "C_S_CURVE"
                    ]
                )
            )
        )
    )
    value.loc[["OCEANS_GRADE"]] = 0
    return value


@component.add(
    name="Ni_available",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ni_market": 1, "ni_market_supply": 1},
)
def ni_available():
    return ni_market() + ni_market_supply()


@component.add(
    name="Ni_available_DELAYED",
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_ni_available_delayed": 1},
    other_deps={
        "_delayfixed_ni_available_delayed": {
            "initial": {"time_step": 1},
            "step": {"ni_available": 1},
        }
    },
)
def ni_available_delayed():
    return _delayfixed_ni_available_delayed()


_delayfixed_ni_available_delayed = DelayFixed(
    lambda: ni_available(),
    lambda: time_step(),
    lambda: 30,
    time_step,
    "_delayfixed_ni_available_delayed",
)


@component.add(name="Ni_base_price_2000", comp_type="Constant", comp_subtype="Normal")
def ni_base_price_2000():
    return 2000


@component.add(
    name="Ni_change_grade",
    units="DMNL",
    subscripts=["ORE_GRADES_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={"coefficients_ni_change_grade": 12, "ni_price": 4},
)
def ni_change_grade():
    """
    When the price rise above the cost of extraction, the mining of this grade can start Sverdrup, H. U., Ragnarsdottir, K. V. and Koca, D. (2015) Aluminium for the future: Modelling the global production, market supply, demand, price and long term development of the global reservesâ€™, Resources, Conservation and Recycling, 103, pp. 139â€“154. doi: 10.1016/j.resconrec.2015.06.008. Olafsdottir, A.H., and Sverdrup, H., 2020, System dynamics modelling of mining, supply, recycling, stocks-in-use and market price for nickel. Mining, Metallurgy & Exploration. 1-22. 10.1007/s42461-020-00370-
    """
    value = xr.DataArray(
        np.nan, {"ORE_GRADES_I": _subscript_dict["ORE_GRADES_I"]}, ["ORE_GRADES_I"]
    )
    value.loc[["RICH_GRADE"]] = 0
    value.loc[["HIGH_GRADE"]] = float(
        coefficients_ni_change_grade().loc["HIGH_GRADE", "A_S_CURVE"]
    ) / (
        1
        + np.exp(
            -float(coefficients_ni_change_grade().loc["HIGH_GRADE", "B_S_CURVE"])
            * (
                ni_price()
                - float(coefficients_ni_change_grade().loc["HIGH_GRADE", "C_S_CURVE"])
            )
        )
    )
    value.loc[["LOW_GRADE"]] = float(
        coefficients_ni_change_grade().loc["LOW_GRADE", "A_S_CURVE"]
    ) / (
        1
        + np.exp(
            -float(coefficients_ni_change_grade().loc["LOW_GRADE", "B_S_CURVE"])
            * (
                ni_price()
                - float(coefficients_ni_change_grade().loc["LOW_GRADE", "C_S_CURVE"])
            )
        )
    )
    value.loc[["ULTRALOW_GRADE"]] = float(
        coefficients_ni_change_grade().loc["ULTRALOW_GRADE", "A_S_CURVE"]
    ) / (
        1
        + np.exp(
            -float(coefficients_ni_change_grade().loc["ULTRALOW_GRADE", "B_S_CURVE"])
            * (
                ni_price()
                - float(
                    coefficients_ni_change_grade().loc["ULTRALOW_GRADE", "C_S_CURVE"]
                )
            )
        )
    )
    value.loc[["TRACE_GRADE"]] = float(
        coefficients_ni_change_grade().loc["TRACE_GRADE", "A_S_CURVE"]
    ) / (
        1
        + np.exp(
            -float(coefficients_ni_change_grade().loc["TRACE_GRADE", "B_S_CURVE"])
            * (
                ni_price()
                - float(coefficients_ni_change_grade().loc["TRACE_GRADE", "C_S_CURVE"])
            )
        )
    )
    value.loc[["OCEANS_GRADE"]] = 0
    return value


@component.add(
    name="Ni_CONTENT_IN_COMMON_STEEL",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="Normal",
)
def ni_content_in_common_steel():
    """
    This is the average nickel content found in common carbon steel. This was set after reading a number of articles on steelmaking. Not all steel have ni added, but some do and this is what we guess it is in 2018.
    """
    return 0.0003


@component.add(
    name="Ni_CONTENT_IN_METALS",
    units="DMNL",
    subscripts=["NI_CONTENT_IN_METALS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_ni_content_in_metals"},
)
def ni_content_in_metals():
    """
    This is a multiplier for how much of the carrier metal stream is followed by nickel. For copper, we estimate that on the average there will be 3.5 units of nickel produced for every 100 units of copper. With this number, the nickel amount produced on a global scale from copper seems to fit well (100,000 ton Ni/yr) The average ore grade for PGM is a few gram per ton ore. The nickel on average extracted is about 500 times that. Thus, about 2,000 ton nickel/yr is co-produced with PGM from mines. PGM is also co-produced from nickel mines, but that is a separate story.
    """
    return _ext_constant_ni_content_in_metals()


_ext_constant_ni_content_in_metals = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Nickel",
    "Ni_CONTENT_IN_METALS*",
    {"NI_CONTENT_IN_METALS_I": _subscript_dict["NI_CONTENT_IN_METALS_I"]},
    _root,
    {"NI_CONTENT_IN_METALS_I": _subscript_dict["NI_CONTENT_IN_METALS_I"]},
    "_ext_constant_ni_content_in_metals",
)


@component.add(
    name="Ni_CONTENT_IN_SS_STEEL",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_ni_content_in_ss_steel"},
)
def ni_content_in_ss_steel():
    """
    Nickel content in Stainless steel.
    """
    return _ext_constant_ni_content_in_ss_steel()


_ext_constant_ni_content_in_ss_steel = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Nickel",
    "Ni_CONTENT_IN_SS_STEEL",
    {},
    _root,
    {},
    "_ext_constant_ni_content_in_ss_steel",
)


@component.add(
    name="Ni_cumulative_mining",
    units="Mt",
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_ni_cumulative_mining": 1},
    other_deps={
        "_integ_ni_cumulative_mining": {
            "initial": {"initial_ni_cumulative_mining": 1},
            "step": {"increase_ni_cumulative": 1},
        }
    },
)
def ni_cumulative_mining():
    """
    Cumulative Nickel Mined
    """
    return _integ_ni_cumulative_mining()


_integ_ni_cumulative_mining = Integ(
    lambda: increase_ni_cumulative(),
    lambda: initial_ni_cumulative_mining(),
    "_integ_ni_cumulative_mining",
)


@component.add(
    name="Ni_demand",
    units="Mt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "switch_eco2mat_ni_demand": 1,
        "switch_materials": 1,
        "ni_modified_demand_world7": 1,
        "implicit_price_ni": 1,
        "output_real": 1,
    },
)
def ni_demand():
    return if_then_else(
        np.logical_or(
            time() < 2015,
            np.logical_or(switch_eco2mat_ni_demand() == 0, switch_materials() == 0),
        ),
        lambda: ni_modified_demand_world7(),
        lambda: sum(
            output_real()
            .loc[:, "MINING_AND_MANUFACTURING_NICKEL"]
            .reset_coords(drop=True)
            .rename({"REGIONS_35_I": "REGIONS_35_I!"}),
            dim=["REGIONS_35_I!"],
        )
        / implicit_price_ni(),
    )


@component.add(
    name="Ni_energy_all",
    units="TJ/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "ni_energy_use_secondary": 1,
        "ni_energy_use_recycling": 1,
        "ni_energy_use_from_extraction": 1,
    },
)
def ni_energy_all():
    return (
        ni_energy_use_secondary()
        + ni_energy_use_recycling()
        + ni_energy_use_from_extraction()
    )


@component.add(
    name="Ni_ENERGY_SECONDARY",
    units="MJ/kg",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_ni_energy_secondary"},
)
def ni_energy_secondary():
    """
    Refers to Ni which is extracted as a co-product of the extraction of other materials. Sverdrup and Olafsdottir 2021: Assessing the global energy and water use from of metals, materials and fossil fuels extraction and production. Internal report for LOCOMOTION WP7. 44pp
    """
    return _ext_constant_ni_energy_secondary()


_ext_constant_ni_energy_secondary = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Nickel",
    "Ni_ENERGY_SECONDARY",
    {},
    _root,
    {},
    "_ext_constant_ni_energy_secondary",
)


@component.add(
    name="Ni_energy_use",
    units="MJ/kg*Mt/Years",
    subscripts=["ORE_GRADES_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={"coefficients_ni_energy_use": 5, "ni_mining": 5},
)
def ni_energy_use():
    """
    total Cu energy use for extraction and refining
    """
    value = xr.DataArray(
        np.nan, {"ORE_GRADES_I": _subscript_dict["ORE_GRADES_I"]}, ["ORE_GRADES_I"]
    )
    value.loc[["RICH_GRADE"]] = float(
        coefficients_ni_energy_use().loc["RICH_GRADE"]
    ) * float(ni_mining().loc["RICH_GRADE"])
    value.loc[["HIGH_GRADE"]] = float(ni_mining().loc["HIGH_GRADE"]) * float(
        coefficients_ni_energy_use().loc["HIGH_GRADE"]
    )
    value.loc[["LOW_GRADE"]] = float(ni_mining().loc["LOW_GRADE"]) * float(
        coefficients_ni_energy_use().loc["LOW_GRADE"]
    )
    value.loc[["ULTRALOW_GRADE"]] = float(ni_mining().loc["ULTRALOW_GRADE"]) * float(
        coefficients_ni_energy_use().loc["ULTRALOW_GRADE"]
    )
    value.loc[["TRACE_GRADE"]] = float(ni_mining().loc["TRACE_GRADE"]) * float(
        coefficients_ni_energy_use().loc["TRACE_GRADE"]
    )
    value.loc[["OCEANS_GRADE"]] = 0
    return value


@component.add(
    name="Ni_energy_use_from_extraction",
    units="TJ/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "ni_energy_use": 5,
        "unit_conversion_tj_mj": 1,
        "unit_conversion_kg_mt": 1,
    },
)
def ni_energy_use_from_extraction():
    """
    total Ni energy use for extraction and refining Gutowski, T.G., Sahni, S., Allwood, M., Ashby, M.F., Worrell, E., 2016. The energy required to produce materials: constraints on energy-intensity improvements, parameters of demand. Philosophical Transactions of the Royal Society A 371: 20120003. http://dx.doi.org/10.1098/rsta.2012.0003 This is the energy and water used associated with the materials consumed to extract this specific resource grade, expressed in MJ/kg product and m3/ton The actual values are taken from an internal LOCOMOTION report that have extracted the available values from literature and extrapolations. Source: Harald Sverdrup and Anna Hulda Olafsdottir 2021. Assessing with the WORLD7 model the global CO2 emissions and water use by metals, materials and fossil fuels extraction and production. LOCOMOTION working paper. 52 pages.
    """
    return (
        (
            float(ni_energy_use().loc["HIGH_GRADE"])
            + float(ni_energy_use().loc["LOW_GRADE"])
            + float(ni_energy_use().loc["ULTRALOW_GRADE"])
            + float(ni_energy_use().loc["TRACE_GRADE"])
            + float(ni_energy_use().loc["RICH_GRADE"])
        )
        * unit_conversion_tj_mj()
        * unit_conversion_kg_mt()
    )


@component.add(
    name="Ni_energy_use_recycling",
    units="TJ/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "ni_energy_recycling": 1,
        "ni_other_recycling": 1,
        "unit_conversion_kg_mt": 1,
        "unit_conversion_tj_mj": 1,
    },
)
def ni_energy_use_recycling():
    """
    the energy used on recycling This is the energy and water used associated with the materials consumed to extract this specific resource grade, expressed in MJ/kg product and m3/ton The actual values are taken from an internal LOCOMOTION report that have extracted the available values from literature and extrapolations. Source: Harald Sverdrup and Anna Hulda Olafsdottir 2021. Assessing with the WORLD7 model the global CO2 emissions and water use by metals, materials and fossil fuels extraction and production. LOCOMOTION working paper. 52 pages.
    """
    return (
        ni_energy_recycling()
        * ni_other_recycling()
        * unit_conversion_kg_mt()
        * unit_conversion_tj_mj()
    )


@component.add(
    name="Ni_energy_use_secondary",
    units="TJ/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "ni_secondary": 1,
        "ni_energy_secondary": 1,
        "unit_conversion_tj_mj": 1,
        "unit_conversion_kg_mt": 1,
    },
)
def ni_energy_use_secondary():
    """
    the energy used of secondary Ni extraction Gutowski, T.G., Sahni, S., Allwood, M., Ashby, M.F., Worrell, E., 2016. The energy required to produce materials: constraints on energy-intensity improvements, parameters of demand. Philosophical Transactions of the Royal Society A 371: 20120003. http://dx.doi.org/10.1098/rsta.2012.0003 This is the energy and water used associated with the materials consumed to extract this specific resource grade, expressed in MJ/kg product and m3/ton The actual values are taken from an internal LOCOMOTION report that have extracted the available values from literature and extrapolations. Source: Harald Sverdrup and Anna Hulda Olafsdottir 2021. Assessing with the WORLD7 model the global CO2 emissions and water use by metals, materials and fossil fuels extraction and production. LOCOMOTION working paper. 52 pages.
    """
    return (
        ni_secondary()
        * ni_energy_secondary()
        * unit_conversion_tj_mj()
        * unit_conversion_kg_mt()
    )


@component.add(
    name="Ni_extraction",
    units="Mt/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ni_secondary": 1, "ni_total_mining": 1},
)
def ni_extraction():
    """
    Sums up primary mining and secondary extraction
    """
    return ni_secondary() + ni_total_mining()


@component.add(
    name="Ni_extraction_rate_coefficient",
    units="1/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "ni_rate_scaling": 1,
        "ni_profit_out_new": 1,
        "cu_inverted_cost_curve": 1,
    },
)
def ni_extraction_rate_coefficient():
    """
    Ni extraction rate. Fraction of known extracted annually
    """
    return ni_rate_scaling() * ni_profit_out_new() * cu_inverted_cost_curve()


@component.add(
    name="Ni_Fe_demand",
    units="Mt/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"fe_society_output": 1, "ni_content_in_common_steel": 1},
)
def ni_fe_demand():
    """
    The demand of nickel from using small amkunts in some types of common steel, averaged over all steel
    """
    return fe_society_output() * ni_content_in_common_steel()


@component.add(
    name="Ni_find",
    units="Mt/Year",
    subscripts=["ORE_GRADES_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "ni_hidden_resources": 5,
        "ni_rich_find_rate": 1,
        "prospecting_for_ni_from_all": 2,
        "prospekting_rate_ni": 3,
        "prospecting_technology_improvements_for_ni": 4,
        "scaling_numbers_from_ni_hidden_to_ni_known": 2,
        "prospecting_for_ni_from_grades": 3,
        "mining_technology_improvements_for_ni": 1,
    },
)
def ni_find():
    """
    Prospecting seaches for the unknown to find it and transfer it to known
    """
    value = xr.DataArray(
        np.nan, {"ORE_GRADES_I": _subscript_dict["ORE_GRADES_I"]}, ["ORE_GRADES_I"]
    )
    value.loc[["RICH_GRADE"]] = (
        float(ni_hidden_resources().loc["RICH_GRADE"]) * ni_rich_find_rate()
    )
    value.loc[["HIGH_GRADE"]] = (
        float(scaling_numbers_from_ni_hidden_to_ni_known().loc["HIGH_GRADE"])
        * float(prospecting_for_ni_from_all().loc["HIGH_GRADE"])
        * float(ni_hidden_resources().loc["HIGH_GRADE"])
        * prospekting_rate_ni()
        * float(prospecting_technology_improvements_for_ni().loc["HIGH_GRADE"])
    )
    value.loc[["LOW_GRADE"]] = (
        float(scaling_numbers_from_ni_hidden_to_ni_known().loc["LOW_GRADE"])
        * float(prospecting_for_ni_from_grades().loc["LOW_GRADE"])
        * float(prospecting_technology_improvements_for_ni().loc["LOW_GRADE"])
        * float(prospecting_for_ni_from_all().loc["LOW_GRADE"])
        * float(ni_hidden_resources().loc["LOW_GRADE"])
    )
    value.loc[["ULTRALOW_GRADE"]] = (
        float(prospecting_for_ni_from_grades().loc["ULTRALOW_GRADE"])
        * float(prospecting_technology_improvements_for_ni().loc["ULTRALOW_GRADE"])
        * float(ni_hidden_resources().loc["ULTRALOW_GRADE"])
        * prospekting_rate_ni()
    )
    value.loc[["TRACE_GRADE"]] = (
        float(ni_hidden_resources().loc["TRACE_GRADE"])
        * float(prospecting_technology_improvements_for_ni().loc["TRACE_GRADE"])
        * float(prospecting_for_ni_from_grades().loc["TRACE_GRADE"])
        * prospekting_rate_ni()
        * float(mining_technology_improvements_for_ni().loc["TRACE_GRADE"])
    )
    value.loc[["OCEANS_GRADE"]] = 0
    return value


@component.add(
    name="Ni_from_Cu",
    units="Mt/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ni_content_in_metals": 1, "imv_cu_mined_0": 1},
)
def ni_from_cu():
    return float(ni_content_in_metals().loc["Ni_IN_Cu"]) * imv_cu_mined_0()


@component.add(
    name="Ni_from_PGM",
    units="Mt/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "imv_pgm_from_mining": 1,
        "ni_content_in_metals": 1,
        "unit_conversion_mt_kt": 1,
    },
)
def ni_from_pgm():
    return (
        imv_pgm_from_mining()
        * float(ni_content_in_metals().loc["Ni_IN_PGM"])
        * unit_conversion_mt_kt()
    )


@component.add(
    name="Ni_full_recycling",
    units="Mt/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ni_indirectly_recycled": 1, "ni_other_recycling": 1},
)
def ni_full_recycling():
    """
    All recycling, direct and systemic
    """
    return ni_indirectly_recycled() + ni_other_recycling()


@component.add(
    name="Ni_Full_supply",
    units="Mt/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ni_indirectly_recycled": 1, "ni_market_supply": 1},
)
def ni_full_supply():
    """
    All supply, direct and systemic. Some nickel is resupplied as stainless, and it is counted in here
    """
    return ni_indirectly_recycled() + ni_market_supply()


@component.add(
    name="Ni_grade_cost",
    units="M$/Mt",
    subscripts=["ORE_GRADES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"coefficients_ni_grade_cost": 6, "ni_mining_efficiency_curve": 6},
)
def ni_grade_cost():
    """
    Cost for every ore grade mining
    """
    value = xr.DataArray(
        np.nan, {"ORE_GRADES_I": _subscript_dict["ORE_GRADES_I"]}, ["ORE_GRADES_I"]
    )
    value.loc[["RICH_GRADE"]] = (
        float(coefficients_ni_grade_cost().loc["RICH_GRADE"])
        / ni_mining_efficiency_curve()
    )
    value.loc[["HIGH_GRADE"]] = (
        float(coefficients_ni_grade_cost().loc["HIGH_GRADE"])
        / ni_mining_efficiency_curve()
    )
    value.loc[["LOW_GRADE"]] = (
        float(coefficients_ni_grade_cost().loc["LOW_GRADE"])
        / ni_mining_efficiency_curve()
    )
    value.loc[["ULTRALOW_GRADE"]] = (
        float(coefficients_ni_grade_cost().loc["ULTRALOW_GRADE"])
        / ni_mining_efficiency_curve()
    )
    value.loc[["TRACE_GRADE"]] = (
        float(coefficients_ni_grade_cost().loc["TRACE_GRADE"])
        / ni_mining_efficiency_curve()
    )
    value.loc[["OCEANS_GRADE"]] = (
        float(coefficients_ni_grade_cost().loc["OCEANS_GRADE"])
        / ni_mining_efficiency_curve()
    )
    return value


@component.add(
    name="Ni_hidden_resources",
    units="Mt",
    subscripts=["ORE_GRADES_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_ni_hidden_resources": 1},
    other_deps={
        "_integ_ni_hidden_resources": {
            "initial": {"initial_ni_hidden_resources": 1},
            "step": {"ni_find": 1},
        }
    },
)
def ni_hidden_resources():
    """
    Olafsdottir, A.H., and Sverdrup, H., 2020, System dynamics modelling of mining, supply, recycling, stocks-in-use and market price for nickel. Mining, Metallurgy & Exploration. 1-22. 10.1007/s42461-020-00370-
    """
    return _integ_ni_hidden_resources()


_integ_ni_hidden_resources = Integ(
    lambda: -ni_find(),
    lambda: initial_ni_hidden_resources(),
    "_integ_ni_hidden_resources",
)


@component.add(
    name="Ni_high_tech_demand",
    units="Mt/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "global_ni_other_demand": 1,
        "imv_global_population": 1,
        "coefficients_high_tech_ni_demand": 1,
    },
)
def ni_high_tech_demand():
    """
    kg/person*Bp= Billion kg/years = Mt/years Mt/years b=10^9 kg =1/1000t 10^9/1000= 10^6 = Mt Olafsdottir, A.H., and Sverdrup, H., 2020, System dynamics modelling of mining, supply, recycling, stocks-in-use and market price for nickel. Mining, Metallurgy & Exploration. 1-22. 10.1007/s42461-020-00370-
    """
    return (
        global_ni_other_demand()
        * imv_global_population()
        * coefficients_high_tech_ni_demand()
    )


@component.add(
    name="Ni_HISTORICAL_GLOBAL_CONSUMPTION",
    units="Kt/Year",
    comp_type="Auxiliary",
    comp_subtype="with Lookup",
    depends_on={"time": 1},
)
def ni_historical_global_consumption():
    """
    Historical global nickel consumption in kt per year
    """
    return np.interp(
        time(),
        [
            1990.97,
            1991.38,
            1991.79,
            1992.19,
            1992.6,
            1993.01,
            1993.42,
            1993.82,
            1994.23,
            1994.63,
            1995.04,
            1995.45,
            1995.86,
            1996.26,
            1996.67,
            1997.08,
            1997.48,
            1997.89,
            1998.3,
            1998.7,
            1999.11,
            1999.52,
            1999.92,
            2000.33,
            2000.74,
            2001.14,
            2001.55,
            2001.96,
            2002.36,
            2002.77,
            2003.18,
            2003.58,
            2003.99,
            2004.4,
            2004.81,
            2005.16,
            2005.45,
            2005.76,
            2006.13,
            2006.54,
            2006.95,
            2007.36,
            2007.77,
            2008.17,
            2008.58,
            2008.99,
            2009.3,
            2009.52,
            2009.74,
            2009.98,
            2010.28,
            2010.61,
            2010.98,
            2011.38,
            2011.79,
            2012.2,
            2012.6,
            2013.01,
            2013.42,
            2013.82,
            2014.23,
            2014.64,
            2015.04,
            2015.39,
            2015.69,
            2015.98,
            2016.28,
            2016.59,
            2016.92,
            2017.26,
            2017.59,
            2017.96,
            2018.36,
            2018.77,
            2019.18,
            2019.58,
            2019.88,
        ],
        [
            866.614,
            840.986,
            814.575,
            798.73,
            793.449,
            793.059,
            824.169,
            858.8,
            899.888,
            944.693,
            978.737,
            966.413,
            951.35,
            965.634,
            995.374,
            1016.51,
            1014.16,
            1010.84,
            1031.77,
            1061.51,
            1087.14,
            1104.75,
            1120.41,
            1116.69,
            1107.89,
            1114.54,
            1144.09,
            1172.26,
            1191.83,
            1209.05,
            1222.74,
            1233.12,
            1242.31,
            1244.47,
            1247.6,
            1274.33,
            1318.85,
            1365.99,
            1384.11,
            1353.01,
            1322.49,
            1303.9,
            1287.67,
            1269.47,
            1248.34,
            1243.46,
            1303.56,
            1355.11,
            1406.65,
            1458.81,
            1502.53,
            1548.28,
            1594.47,
            1622.45,
            1646.91,
            1685.26,
            1732.41,
            1776.43,
            1812.24,
            1846.09,
            1860.18,
            1863.7,
            1882.48,
            1934.19,
            1980.05,
            2025.64,
            2070.42,
            2117.41,
            2167.23,
            2215.13,
            2262.08,
            2311.12,
            2345.17,
            2376.47,
            2384.3,
            2375.11,
            2368.55,
        ],
    )


@component.add(
    name="Ni_HISTORICAL_GLOBAL_CONSUMPTION_Mt",
    units="Mt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ni_historical_global_consumption": 1, "unit_conversion_mt_kt": 1},
)
def ni_historical_global_consumption_mt():
    """
    Historical Nickel consumption in Mt per year.
    """
    return ni_historical_global_consumption() * unit_conversion_mt_kt()


@component.add(
    name="Ni_indirectly_recycled",
    units="Mt/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"imv_ss_mncrni_recycled_two": 1, "ni_content_in_ss_steel": 1},
)
def ni_indirectly_recycled():
    """
    Recycing of Ni with stainless steel Olafsdottir, A.H., and Sverdrup, H., 2020, System dynamics modelling of mining, supply, recycling, stocks-in-use and market price for nickel. Mining, Metallurgy & Exploration. 1-22. 10.1007/s42461-020-00370-
    """
    return imv_ss_mncrni_recycled_two() * ni_content_in_ss_steel()


@component.add(
    name="Ni_known_reserves",
    units="Mt",
    subscripts=["ORE_GRADES_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_ni_known_reserves": 1},
    other_deps={
        "_integ_ni_known_reserves": {
            "initial": {"initial_ni_known_reserves": 1},
            "step": {"ni_find": 1, "ni_mining": 1},
        }
    },
)
def ni_known_reserves():
    """
    Olafsdottir, A.H., and Sverdrup, H., 2020, System dynamics modelling of mining, supply, recycling, stocks-in-use and market price for nickel. Mining, Metallurgy & Exploration. 1-22. 10.1007/s42461-020-00370-
    """
    return _integ_ni_known_reserves()


_integ_ni_known_reserves = Integ(
    lambda: ni_find() - ni_mining(),
    lambda: initial_ni_known_reserves(),
    "_integ_ni_known_reserves",
)


@component.add(
    name="Ni_known_reserves_all_grades",
    units="Mt",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ni_known_reserves": 6},
)
def ni_known_reserves_all_grades():
    """
    Summing up reserves
    """
    return (
        float(ni_known_reserves().loc["RICH_GRADE"])
        + float(ni_known_reserves().loc["HIGH_GRADE"])
        + float(ni_known_reserves().loc["LOW_GRADE"])
        + float(ni_known_reserves().loc["ULTRALOW_GRADE"])
        + float(ni_known_reserves().loc["TRACE_GRADE"])
        + float(ni_known_reserves().loc["OCEANS_GRADE"])
    )


@component.add(
    name="Ni_market",
    units="Mt",
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_ni_market": 1},
    other_deps={
        "_integ_ni_market": {
            "initial": {"initial_ni_market": 1},
            "step": {"ni_market_supply": 1, "ni_return": 1, "ni_supply_to_society": 1},
        }
    },
)
def ni_market():
    """
    The amount immediately available for commercial transaction. See market paper by Sverdrup and Olafsdottir 2018. Olafsdottir, A.H., and Sverdrup, H., 2020, System dynamics modelling of mining, supply, recycling, stocks-in-use and market price for nickel. Mining, Metallurgy & Exploration. 1-22. 10.1007/s42461-020-00370-
    """
    return _integ_ni_market()


_integ_ni_market = Integ(
    lambda: ni_market_supply() + ni_return() - ni_supply_to_society(),
    lambda: initial_ni_market(),
    "_integ_ni_market",
)


@component.add(
    name="Ni_market_sales",
    units="Mt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ni_supply_to_society": 1},
)
def ni_market_sales():
    return ni_supply_to_society()


@component.add(
    name="Ni_market_supply",
    units="Mt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ni_extraction": 1, "ni_other_recycling": 1},
)
def ni_market_supply():
    """
    Summing up all that goes to market
    """
    return ni_extraction() + ni_other_recycling()


@component.add(
    name="Ni_Mining",
    units="Mt/Year",
    subscripts=["ORE_GRADES_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "ni_known_reserves": 5,
        "ni_extraction_rate_coefficient": 5,
        "ni_change_grade": 4,
        "mining_technology_improvements_for_ni": 3,
    },
)
def ni_mining():
    value = xr.DataArray(
        np.nan, {"ORE_GRADES_I": _subscript_dict["ORE_GRADES_I"]}, ["ORE_GRADES_I"]
    )
    value.loc[["RICH_GRADE"]] = (
        float(ni_known_reserves().loc["RICH_GRADE"]) * ni_extraction_rate_coefficient()
    )
    value.loc[["HIGH_GRADE"]] = (
        ni_extraction_rate_coefficient()
        * float(ni_known_reserves().loc["HIGH_GRADE"])
        * float(ni_change_grade().loc["HIGH_GRADE"])
    )
    value.loc[["LOW_GRADE"]] = (
        float(ni_known_reserves().loc["LOW_GRADE"])
        * ni_extraction_rate_coefficient()
        * float(ni_change_grade().loc["LOW_GRADE"])
        * float(mining_technology_improvements_for_ni().loc["LOW_GRADE"])
    )
    value.loc[["ULTRALOW_GRADE"]] = (
        float(ni_known_reserves().loc["ULTRALOW_GRADE"])
        * ni_extraction_rate_coefficient()
        * float(ni_change_grade().loc["ULTRALOW_GRADE"])
        * float(mining_technology_improvements_for_ni().loc["ULTRALOW_GRADE"])
    )
    value.loc[["TRACE_GRADE"]] = (
        float(ni_known_reserves().loc["TRACE_GRADE"])
        * ni_extraction_rate_coefficient()
        * float(ni_change_grade().loc["TRACE_GRADE"])
        * float(mining_technology_improvements_for_ni().loc["TRACE_GRADE"])
    )
    value.loc[["OCEANS_GRADE"]] = 0
    return value


@component.add(
    name="Ni_mining_efficiency_curve",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"coefficients_ni_mining_efficiency_curve": 3, "time": 1},
)
def ni_mining_efficiency_curve():
    """
    Similar to the curve adopted for copper. Ni and Cu mines in the same way, often together. Olafsdottir, A.H., and Sverdrup, H., 2020, System dynamics modelling of mining, supply, recycling, stocks-in-use and market price for nickel. Mining, Metallurgy & Exploration. 1-22. 10.1007/s42461-020-00370-
    """
    return float(coefficients_ni_mining_efficiency_curve().loc["A_S_CURVE"]) / (
        1
        + np.exp(
            -float(coefficients_ni_mining_efficiency_curve().loc["B_S_CURVE"])
            * (
                time()
                - float(coefficients_ni_mining_efficiency_curve().loc["C_S_CURVE"])
            )
        )
    )


@component.add(
    name="Ni_mining_expences",
    units="M$/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ni_grade_cost": 7, "ni_mining": 6, "ni_secondary": 1},
)
def ni_mining_expences():
    """
    Summing up costs of mining
    """
    return (
        float(ni_grade_cost().loc["RICH_GRADE"]) * float(ni_mining().loc["RICH_GRADE"])
        + float(ni_grade_cost().loc["HIGH_GRADE"])
        * float(ni_mining().loc["HIGH_GRADE"])
        + float(ni_grade_cost().loc["LOW_GRADE"]) * float(ni_mining().loc["LOW_GRADE"])
        + float(ni_grade_cost().loc["ULTRALOW_GRADE"])
        * float(ni_mining().loc["ULTRALOW_GRADE"])
        + float(ni_grade_cost().loc["TRACE_GRADE"])
        * float(ni_mining().loc["TRACE_GRADE"])
        + float(ni_grade_cost().loc["OCEANS_GRADE"])
        * float(ni_mining().loc["OCEANS_GRADE"])
        + ni_secondary() * float(ni_grade_cost().loc["LOW_GRADE"])
    )


@component.add(
    name="Ni_mining_Income",
    units="M$/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ni_secondary": 1, "ni_total_mining": 1, "ni_price": 1},
)
def ni_mining_income():
    """
    Income from Nickel sales on the market
    """
    return (ni_secondary() + ni_total_mining()) * ni_price()


@component.add(
    name="Ni_mining_profit",
    units="M$/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "ni_mining_income": 1,
        "profit_margin_on_extraction": 1,
        "ni_mining_expences": 1,
    },
)
def ni_mining_profit():
    """
    Profit is defined as Income minus Costs. The cost have been multiplied with a 10% markup
    """
    return ni_mining_income() - profit_margin_on_extraction() * ni_mining_expences()


@component.add(
    name="Ni_modified_demand_WORLD7",
    units="Mt/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "ni_fe_demand": 1,
        "ni_other_demand": 1,
        "ni_high_tech_demand": 1,
        "imv_ss_ni_wanted": 1,
        "ni_price_effect_on_demand": 1,
    },
)
def ni_modified_demand_world7():
    return (
        ni_fe_demand() + ni_other_demand() + ni_high_tech_demand() + imv_ss_ni_wanted()
    ) * ni_price_effect_on_demand()


@component.add(
    name="Ni_ore_grade",
    units="Mt",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "ni_mining": 12,
        "amount_of_ni_in_weight_of_rock": 6,
        "avoid_zero_division": 1,
    },
)
def ni_ore_grade():
    """
    Calculation of the average ore grade
    """
    return (
        float(ni_mining().loc["RICH_GRADE"])
        * float(amount_of_ni_in_weight_of_rock().loc["RICH_GRADE"])
        + float(ni_mining().loc["HIGH_GRADE"])
        * float(amount_of_ni_in_weight_of_rock().loc["HIGH_GRADE"])
        + float(ni_mining().loc["LOW_GRADE"])
        * float(amount_of_ni_in_weight_of_rock().loc["LOW_GRADE"])
        + float(ni_mining().loc["ULTRALOW_GRADE"])
        * float(amount_of_ni_in_weight_of_rock().loc["ULTRALOW_GRADE"])
        + float(ni_mining().loc["TRACE_GRADE"])
        * float(amount_of_ni_in_weight_of_rock().loc["TRACE_GRADE"])
        + float(ni_mining().loc["OCEANS_GRADE"])
        * float(amount_of_ni_in_weight_of_rock().loc["OCEANS_GRADE"])
    ) / (
        float(ni_mining().loc["RICH_GRADE"])
        + float(ni_mining().loc["HIGH_GRADE"])
        + float(ni_mining().loc["LOW_GRADE"])
        + float(ni_mining().loc["ULTRALOW_GRADE"])
        + float(ni_mining().loc["TRACE_GRADE"])
        + float(ni_mining().loc["OCEANS_GRADE"])
        + avoid_zero_division()
    )


@component.add(
    name="Ni_other_demand",
    units="Mt/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"imv_cu_mined_0": 1, "ni_units_per_cu_used": 1},
)
def ni_other_demand():
    return imv_cu_mined_0() * ni_units_per_cu_used()


@component.add(
    name="Ni_other_recycled_fraction",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"coefficients_ni_other_recycling_fraction": 3, "ni_price": 1},
)
def ni_other_recycled_fraction():
    """
    Olafsdottir, A.H., and Sverdrup, H., 2020, System dynamics modelling of mining, supply, recycling, stocks-in-use and market price for nickel. Mining, Metallurgy & Exploration. 1-22. 10.1007/s42461-020-00370-
    """
    return float(coefficients_ni_other_recycling_fraction().loc["A_S_CURVE"]) / (
        1
        + np.exp(
            -float(coefficients_ni_other_recycling_fraction().loc["B_S_CURVE"])
            * (
                ni_price()
                - float(coefficients_ni_other_recycling_fraction().loc["C_S_CURVE"])
            )
        )
    )


@component.add(
    name="Ni_other_recycling",
    units="Mt/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ni_other_scrap_recycling": 2},
)
def ni_other_recycling():
    """
    Recycling of non-stainless use of nickel
    """
    return ni_other_scrap_recycling() * ni_other_scrap_recycling()


@component.add(
    name="Ni_other_scrap_recycling",
    units="Mt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ni_scrap": 1, "ni_scrapping_share_recycling_sp": 1},
)
def ni_other_scrap_recycling():
    return ni_scrap() * ni_scrapping_share_recycling_sp()


@component.add(
    name="Ni_other_use",
    units="Mt",
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_ni_other_use": 1},
    other_deps={
        "_integ_ni_other_use": {
            "initial": {"initial_ni_other_use": 1},
            "step": {"ni_other_uses": 1, "ni_scrap_from_other_use": 1},
        }
    },
)
def ni_other_use():
    """
    Olafsdottir, A.H., and Sverdrup, H., 2020, System dynamics modelling of mining, supply, recycling, stocks-in-use and market price for nickel. Mining, Metallurgy & Exploration. 1-22. 10.1007/s42461-020-00370-
    """
    return _integ_ni_other_use()


_integ_ni_other_use = Integ(
    lambda: ni_other_uses() - ni_scrap_from_other_use(),
    lambda: initial_ni_other_use(),
    "_integ_ni_other_use",
)


@component.add(
    name="Ni_Other_uses",
    units="Mt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ni_supply_to_society": 1},
)
def ni_other_uses():
    return ni_supply_to_society() * 0.08


@component.add(
    name="Ni_PLATED_SCRAPPING_RATE",
    units="1/Years",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_ni_plated_scrapping_rate"},
)
def ni_plated_scrapping_rate():
    """
    We assume that only 5% of the global nickel stock in plating is recycled every year. No data have been found, so this is assumption-based. WE assume that the scrapping runs at half the rate of diffusive losses
    """
    return _ext_constant_ni_plated_scrapping_rate()


_ext_constant_ni_plated_scrapping_rate = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Nickel",
    "Ni_PLATED_SCRAPPING_RATE",
    {},
    _root,
    {},
    "_ext_constant_ni_plated_scrapping_rate",
)


@component.add(
    name="Ni_plating",
    units="Mt",
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_ni_plating": 1},
    other_deps={
        "_integ_ni_plating": {
            "initial": {"initial_ni_plating": 1},
            "step": {
                "increase_ni_plating": 1,
                "decrease_ni_plating": 1,
                "ni_scrap_plated_stock": 1,
            },
        }
    },
)
def ni_plating():
    """
    Olafsdottir, A.H., and Sverdrup, H., 2020, System dynamics modelling of mining, supply, recycling, stocks-in-use and market price for nickel. Mining, Metallurgy & Exploration. 1-22. 10.1007/s42461-020-00370-
    """
    return _integ_ni_plating()


_integ_ni_plating = Integ(
    lambda: increase_ni_plating() - decrease_ni_plating() - ni_scrap_plated_stock(),
    lambda: initial_ni_plating(),
    "_integ_ni_plating",
)


@component.add(
    name="Ni_PLATING_LOSS_RATE",
    units="1/Years",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_ni_plating_loss_rate"},
)
def ni_plating_loss_rate():
    """
    The plating loss rate implies that 10% of the plated Ni wears off each year
    """
    return _ext_constant_ni_plating_loss_rate()


_ext_constant_ni_plating_loss_rate = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Nickel",
    "Ni_PLATING_LOSS_RATE",
    {},
    _root,
    {},
    "_ext_constant_ni_plating_loss_rate",
)


@component.add(
    name="Ni_price",
    units="M$/Mt",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "ni_market": 3,
        "split_equation_ni": 1,
        "coefficients_ni_price_logistic": 2,
        "coefficients_ni_price_linear": 2,
    },
)
def ni_price():
    """
    Follows the equation y = 16000e-0,763x when the market is larger than 0,15 Mt, from 0-0,15Mt it followes the equation: y = -218667x + 48800 whenre w - market amount See the Sverdrup and Olafsdotir 2019 market mechanism paper for further information. 414. Sverdrup, H., and Olafsdottir, A.H., 2019. Conceptualization and parameterization of the market price mechanism in the WORLD6 model for metals, materials and fossil fuels. Mineral Economics 1-26. Springer Nature DOI: 10.1007/s13563-019-00182-7. Olafsdottir, A.H., and Sverdrup, H., 2020, System dynamics modelling of mining, supply, recycling, stocks-in-use and market price for nickel. Mining, Metallurgy & Exploration. 1-22. 10.1007/s42461-020-00370-
    """
    return if_then_else(
        ni_market() > split_equation_ni(),
        lambda: float(coefficients_ni_price_logistic().loc["A_LINEAR_LOG_FIT"])
        * np.exp(
            float(coefficients_ni_price_logistic().loc["B_LINEAR_LOG_FIT"])
            * ni_market()
        ),
        lambda: float(coefficients_ni_price_linear().loc["A_LINEAR_LOG_FIT"])
        * ni_market()
        + float(coefficients_ni_price_linear().loc["B_LINEAR_LOG_FIT"]),
    )


@component.add(
    name="Ni_price_economy",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ni_demand": 2, "ni_available_delayed": 2},
)
def ni_price_economy():
    return if_then_else(
        ni_demand() > ni_available_delayed(),
        lambda: 100000,
        lambda: np.exp(
            6.34626 + 0.454773 * np.log(1 / (1 - ni_demand() / ni_available_delayed()))
        ),
    )


@component.add(
    name="Ni_price_economy_adjusted",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "ni_price_index_economy": 1},
)
def ni_price_economy_adjusted():
    return if_then_else(time() == 2005, lambda: 100, lambda: ni_price_index_economy())


@component.add(
    name="Ni_price_effect_on_demand",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"coefficients_ni_price_effect_on_demand": 2, "ni_price": 1},
)
def ni_price_effect_on_demand():
    """
    The curve describes the effect of higher price on on nickel demand. The curve is based on experiences other similar curves used in the WORLD7 model. There is no such curves available in the published literature. See also: Sverdrup, H., and Olafsdottir, A.H., 2019. Conceptualization and parameterization of the market price mechanism in the WORLD6 model for metals, materials and fossil fuels. Mineral Economics 1-26. Springer Nature DOI: 10.1007/s13563-019-00182-7.
    """
    return float(
        coefficients_ni_price_effect_on_demand().loc["A_LINEAR_LOG_FIT"]
    ) * np.exp(
        float(coefficients_ni_price_effect_on_demand().loc["B_LINEAR_LOG_FIT"])
        * ni_price()
    )


@component.add(
    name="Ni_price_index_economy",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_mat2eco_ni_price": 1,
        "ni_base_price_2000": 1,
        "estimated_price_with_tax_metals": 1,
        "price_transformation": 1,
    },
)
def ni_price_index_economy():
    return if_then_else(
        switch_mat2eco_ni_price() == 0,
        lambda: 100,
        lambda: (
            float(estimated_price_with_tax_metals().loc["Ni_W"]) / ni_base_price_2000()
        )
        * price_transformation(),
    )


@component.add(
    name="Ni_profit_average_time",
    units="Years",
    comp_type="Constant",
    comp_subtype="Normal",
)
def ni_profit_average_time():
    return 10


@component.add(
    name="Ni_Profit_driver",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ni_mining_profit": 2, "coefficients_ni_profit_driver": 3},
)
def ni_profit_driver():
    """
    This function makes sure that the nickel operation runs when there is profit. If it becomes unprofitable, mining shuts down. Which is how the world works. The curve has a flat part: no mining at deficit, it rises sharply when passing zero. It has a gentle slope up at higher profit, reflecting that increasing up increase profitability. On the systemic level. too much production compared t demand will lower price and thus in time also profits. See also: Sverdrup, H., and Olafsdottir, A.H., 2019. Conceptualization and parameterization of the market price mechanism in the WORLD6 model for metals, materials and fossil fuels. Mineral Economics 1-26. Springer Nature DOI: 10.1007/s13563-019-00182-7.
    """
    return if_then_else(
        ni_mining_profit() < 0,
        lambda: 0,
        lambda: float(coefficients_ni_profit_driver().loc["A_S_CURVE"])
        / (
            1
            + np.exp(
                -float(coefficients_ni_profit_driver().loc["B_S_CURVE"])
                * (
                    ni_mining_profit()
                    - float(coefficients_ni_profit_driver().loc["C_S_CURVE"])
                )
            )
        ),
    )


@component.add(
    name="Ni_profit_input",
    units="1/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ni_profit_driver": 1},
)
def ni_profit_input():
    """
    Transfer into profit delay in the system
    """
    return ni_profit_driver()


@component.add(
    name="Ni_profit_out_NEW",
    units="1/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"delayed_ts_ni_profit_average": 1, "ni_profit_average_time": 1},
)
def ni_profit_out_new():
    """
    Extraction profits. Assuming one year delay in decision making
    """
    return delayed_ts_ni_profit_average() / ni_profit_average_time()


@component.add(
    name="Ni_RATE_SCALING",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_ni_rate_scaling"},
)
def ni_rate_scaling():
    """
    The extraction rate starts out as low and increase with time with technological advances. This advance is assumed to follow the same track as for copper.
    """
    return _ext_constant_ni_rate_scaling()


_ext_constant_ni_rate_scaling = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Nickel",
    "Ni_RATE_SCALING",
    {},
    _root,
    {},
    "_ext_constant_ni_rate_scaling",
)


@component.add(
    name="Ni_recycling",
    units="Mt/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ni_market_supply": 1, "ni_total_mining": 1},
)
def ni_recycling():
    return ni_market_supply() - ni_total_mining()


@component.add(
    name="Ni_return",
    units="Mt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"imv_ni_residual": 1},
)
def ni_return():
    return imv_ni_residual()


@component.add(
    name="Ni_Rich_find_rate",
    units="1/Years",
    comp_type="Constant",
    comp_subtype="Normal",
)
def ni_rich_find_rate():
    """
    The average finding rate for rich ore grade is assumed to be about 5% per year. There are general numbers available on finding rates for oil, silver and gold, and we have assumed a rate of similar order of magnitude.
    """
    return 0.05


@component.add(
    name="Ni_scrap",
    units="Mt",
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_ni_scrap": 1},
    other_deps={
        "_integ_ni_scrap": {
            "initial": {"initial_ni_scrap": 1},
            "step": {"ni_scrapping": 1, "ni_other_scrap_recycling": 1},
        }
    },
)
def ni_scrap():
    """
    This is scrap not contained in stainless steel Olafsdottir, A.H., and Sverdrup, H., 2020, System dynamics modelling of mining, supply, recycling, stocks-in-use and market price for nickel. Mining, Metallurgy & Exploration. 1-22. 10.1007/s42461-020-00370-
    """
    return _integ_ni_scrap()


_integ_ni_scrap = Integ(
    lambda: ni_scrapping() - ni_other_scrap_recycling(),
    lambda: initial_ni_scrap(),
    "_integ_ni_scrap",
)


@component.add(
    name="Ni_scrap_from_other_use",
    units="Mt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ni_scrapping_rate": 1, "ni_other_use": 1},
)
def ni_scrap_from_other_use():
    return ni_scrapping_rate() * ni_other_use()


@component.add(
    name="Ni_scrap_plated_stock",
    units="Mt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ni_plating": 1, "ni_plated_scrapping_rate": 1},
)
def ni_scrap_plated_stock():
    """
    Fraction of plated going to scrap
    """
    return ni_plating() * ni_plated_scrapping_rate()


@component.add(
    name="Ni_scrapping",
    units="Mt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "ni_scrap_plated_stock": 1,
        "ni_scrapping_share": 2,
        "ni_scrap_from_other_use": 1,
    },
)
def ni_scrapping():
    return (
        ni_scrap_plated_stock() * ni_scrapping_share()
        + ni_scrap_from_other_use() * ni_scrapping_share()
    )


@component.add(
    name="Ni_SCRAPPING_SHARE",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_ni_scrapping_share"},
)
def ni_scrapping_share():
    """
    Expert opinion on what we think the Ni scrapping share is of the total waste stream. Order of magnitude obtained from UNEP International Resource Panel reports.
    """
    return _ext_constant_ni_scrapping_share()


_ext_constant_ni_scrapping_share = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Nickel",
    "Ni_SCRAPPING_SHARE",
    {},
    _root,
    {},
    "_ext_constant_ni_scrapping_share",
)


@component.add(
    name="Ni_SCRAPPING_SHARE_RECYCLING_SP",
    units="1/Years",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_ni_scrapping_share_recycling_sp"},
)
def ni_scrapping_share_recycling_sp():
    """
    Assumes scrap handling time to be 60 days
    """
    return _ext_constant_ni_scrapping_share_recycling_sp()


_ext_constant_ni_scrapping_share_recycling_sp = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Nickel",
    "Ni_SCRAPPING_SHARE_RECYCLING",
    {},
    _root,
    {},
    "_ext_constant_ni_scrapping_share_recycling_sp",
)


@component.add(
    name="Ni_secondary",
    units="Mt/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ni_from_cu": 1, "ni_from_pgm": 1},
)
def ni_secondary():
    """
    Secondary extraction summed
    """
    return ni_from_cu() + ni_from_pgm()


@component.add(
    name="Ni_share_of_secondary_material",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ni_full_recycling": 2, "ni_extraction": 1},
)
def ni_share_of_secondary_material():
    """
    Share of secondary material used to produce new copper to be sold on the market.
    """
    return zidz(ni_full_recycling(), ni_extraction() + ni_full_recycling())


@component.add(
    name="Ni_stock_in_use",
    units="Mt",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "ni_plating": 1,
        "ni_other_use": 1,
        "ni_market": 1,
        "ni_content_in_ss_steel": 1,
        "imv_ss_fast_in_use": 1,
        "imv_ss_slow_in_use": 1,
    },
)
def ni_stock_in_use():
    """
    All nickel employed in society. This is the metal that sits there and participates in creating utility for the population.
    """
    return (
        ni_plating()
        + ni_other_use()
        + ni_market()
        + ni_content_in_ss_steel() * (imv_ss_slow_in_use() + imv_ss_fast_in_use())
    )


@component.add(
    name="Ni_supply_to_society",
    units="Mt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ni_demand": 1},
)
def ni_supply_to_society():
    """
    The nickel that goes to non-stainless uses
    """
    return ni_demand()


@component.add(
    name="Ni_systemic_recycling",
    units="Mt/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ni_other_recycling": 1, "ni_indirectly_recycled": 1},
)
def ni_systemic_recycling():
    """
    Direct Ni recycling and the recycling caused by stainless steel recycling Olafsdottir, A.H., and Sverdrup, H., 2020, System dynamics modelling of mining, supply, recycling, stocks-in-use and market price for nickel. Mining, Metallurgy & Exploration. 1-22. 10.1007/s42461-020-00370-
    """
    return ni_other_recycling() + ni_indirectly_recycled()


@component.add(
    name="Ni_systemic_supply",
    units="Mt/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ni_supply_to_society": 1, "ni_indirectly_recycled": 1},
)
def ni_systemic_supply():
    """
    Supply of nickel both internally in the stainless module and directly
    """
    return ni_supply_to_society() + ni_indirectly_recycled()


@component.add(
    name="Ni_total_mining",
    units="Mt/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ni_mining": 1},
)
def ni_total_mining():
    """
    Sums up mining of all ore grades
    """
    return sum(
        ni_mining().rename({"ORE_GRADES_I": "ORE_GRADES_I!"}), dim=["ORE_GRADES_I!"]
    )


@component.add(
    name="Ni_UNITS_PER_Cu_USED",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="Normal",
)
def ni_units_per_cu_used():
    return 0.02


@component.add(
    name="PROMOTION_OF_PROSPECTING",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_promotion_of_prospecting"},
)
def promotion_of_prospecting():
    """
    This is the annual finding rate for global prospecting, assumed to be in the same order of magnitude, so that finding hidden to become known keeps approximately up with average extraction
    """
    return _ext_constant_promotion_of_prospecting()


_ext_constant_promotion_of_prospecting = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Nickel",
    "PROMOTION_OF_PROSPECTING",
    {},
    _root,
    {},
    "_ext_constant_promotion_of_prospecting",
)


@component.add(
    name="prospecting_for_Ni_from_all",
    units="DMNL",
    subscripts=["ORE_GRADES_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "coefficients_prospecting_from_all": 21,
        "ni_known_reserves_all_grades": 4,
    },
)
def prospecting_for_ni_from_all():
    """
    min+(max-min)/(1+10^(n*(log10(x)-log10(ec_50)))) Sigmoid Fitting - prospecting for Ni high and low min 0,010589989 max 2,005044986 n 7,684334811 ec50 5,53505278 IF Ni_known_reserves > 0 THEN COEFFICIENTS_PROSPECTING[MIN_VALUE;HIGH_GRADE]+(COEFFICIENTS_PROSPECTING[MAX_VALUE;HI GH_GRADE]-COEFFICIENTS_PROSPECTING[MIN_VALUE;HIGH_GRADE])/(1+10^(COEFFICIEN TS_PROSPECTING[N;HIGH_GRADE]*(LOG10(Ni_known_reserves)-LOG10(COEFFICIENTS_P ROSPECTING[EC50;HIGH_GRADE])))) ELSE COEFFICIENTS_PROSPECTING[MIN_VALUE;HIGH_GRADE]+(COEFFICIENTS_PROSPECTING[MAX_VALUE;HI GH_GRADE]-COEFFICIENTS_PROSPECTING[MIN_VALUE;HIGH_GRADE])/(1+10^(COEFFICIEN TS_PROSPECTING[N;HIGH_GRADE]*(LOG10(AVOID_ZERO_DIVISION)-LOG10(COEFFICIENTS _PROSPECTING[EC50;HIGH_GRADE])))) IF Ni_known_reserves >0 THEN COEFFICIENTS_PROSPECTING[MIN_VALUE;LOW_GRADE]+(COEFFICIENTS_PROSPECTING[MAX_VALUE;LOW _GRADE]-COEFFICIENTS_PROSPECTING[MIN_VALUE;LOW_GRADE])/(1+10^(COEFFICIENTS_ PROSPECTING[N;LOW_GRADE]*(LOG10(Ni_known_reserves)-LOG10(COEFFICIENTS_PROSP ECTING[EC50;LOW_GRADE])))) ELSE COEFFICIENTS_PROSPECTING[MIN_VALUE;LOW_GRADE]+(COEFFICIENTS_PROSPECTING[MAX_VALUE;LOW _GRADE]-COEFFICIENTS_PROSPECTING[MIN_VALUE;LOW_GRADE])/(1+10^(COEFFICIENTS_ PROSPECTING[N;LOW_GRADE]*(LOG10(AVOID_ZERO_DIVISION)-LOG10(COEFFICIENTS_PRO SPECTING[EC50;LOW_GRADE])))) IF Ni_Known_resources[TRACE_GRADE] >0 THEN COEFFICIENTS_PROSPECTING[MIN_VALUE;TRACE_GRADE]+(COEFFICIENTS_PROSPECTING[MAX_VALUE;T RACE_GRADE]-COEFFICIENTS_PROSPECTING[MIN_VALUE;TRACE_GRADE])/(1+10^(COEFFIC IENTS_PROSPECTING[N;TRACE_GRADE]*(LOG10(Ni_Known_resources[TRACE_GRADE])-LO G10(COEFFICIENTS_PROSPECTING[EC50;TRACE_GRADE])))) ELSE COEFFICIENTS_PROSPECTING[MIN_VALUE;TRACE_GRADE]+(COEFFICIENTS_PROSPECTING[MAX_VALUE;T RACE_GRADE]-COEFFICIENTS_PROSPECTING[MIN_VALUE;TRACE_GRADE])/(1+10^(COEFFIC IENTS_PROSPECTING[N;TRACE_GRADE]*(LOG10(AVOID_ZERO_DIVISION)-LOG10(COEFFICI ENTS_PROSPECTING[EC50;TRACE_GRADE])))) IF Ni_Known_resources[ULTRALOW_GRADE] >0 THEN COEFFICIENTS_PROSPECTING[MIN_VALUE;ULTRALOW_GRADE]+(COEFFICIENTS_PROSPECTING[MAX_VALU E;ULTRALOW_GRADE]-COEFFICIENTS_PROSPECTING[MIN_VALUE;ULTRALOW_GRADE])/(1+10 ^(COEFFICIENTS_PROSPECTING[N;ULTRALOW_GRADE]*(LOG10(Ni_Known_resources[ULTR ALOW_GRADE])-LOG10(COEFFICIENTS_PROSPECTING[EC50;ULTRALOW_GRADE])))) ELSE COEFFICIENTS_PROSPECTING[MIN_VALUE;ULTRALOW_GRADE]+(COEFFICIENTS_PROSPECTING[MAX_VALU E;ULTRALOW_GRADE]-COEFFICIENTS_PROSPECTING[MIN_VALUE;ULTRALOW_GRADE])/(1+10 ^(COEFFICIENTS_PROSPECTING[N;ULTRALOW_GRADE]*(LOG10(AVOID_ZERO_DIVISION)-LO G10(COEFFICIENTS_PROSPECTING[EC50;ULTRALOW_GRADE])))) Olafsdottir, A.H., and Sverdrup, H., 2020, System dynamics modelling of mining, supply, recycling, stocks-in-use and market price for nickel. Mining, Metallurgy & Exploration. 1-22. 10.1007/s42461-020-00370-
    """
    value = xr.DataArray(
        np.nan, {"ORE_GRADES_I": _subscript_dict["ORE_GRADES_I"]}, ["ORE_GRADES_I"]
    )
    value.loc[["RICH_GRADE"]] = float(
        coefficients_prospecting_from_all().loc["N", "RICH_GRADE"]
    )
    value.loc[["HIGH_GRADE"]] = float(
        coefficients_prospecting_from_all().loc["MIN_VALUE", "HIGH_GRADE"]
    ) + (
        float(coefficients_prospecting_from_all().loc["MAX_VALUE", "HIGH_GRADE"])
        - float(coefficients_prospecting_from_all().loc["MIN_VALUE", "HIGH_GRADE"])
    ) / (
        1
        + 10
        ** (
            float(coefficients_prospecting_from_all().loc["N", "HIGH_GRADE"])
            * (
                (np.log(ni_known_reserves_all_grades()) / np.log(10))
                - (
                    np.log(
                        float(
                            coefficients_prospecting_from_all().loc[
                                "EC50", "HIGH_GRADE"
                            ]
                        )
                    )
                    / np.log(10)
                )
            )
        )
    )
    value.loc[["LOW_GRADE"]] = float(
        coefficients_prospecting_from_all().loc["MIN_VALUE", "LOW_GRADE"]
    ) + (
        float(coefficients_prospecting_from_all().loc["MAX_VALUE", "LOW_GRADE"])
        - float(coefficients_prospecting_from_all().loc["MIN_VALUE", "LOW_GRADE"])
    ) / (
        1
        + 10
        ** (
            float(coefficients_prospecting_from_all().loc["N", "LOW_GRADE"])
            * (
                (np.log(ni_known_reserves_all_grades()) / np.log(10))
                - (
                    np.log(
                        float(
                            coefficients_prospecting_from_all().loc["EC50", "LOW_GRADE"]
                        )
                    )
                    / np.log(10)
                )
            )
        )
    )
    value.loc[["ULTRALOW_GRADE"]] = float(
        coefficients_prospecting_from_all().loc["MIN_VALUE", "ULTRALOW_GRADE"]
    ) + (
        float(coefficients_prospecting_from_all().loc["MAX_VALUE", "ULTRALOW_GRADE"])
        - float(coefficients_prospecting_from_all().loc["MIN_VALUE", "ULTRALOW_GRADE"])
    ) / (
        1
        + 10
        ** (
            float(coefficients_prospecting_from_all().loc["N", "ULTRALOW_GRADE"])
            * (
                (np.log(ni_known_reserves_all_grades()) / np.log(10))
                - (
                    np.log(
                        float(
                            coefficients_prospecting_from_all().loc[
                                "EC50", "ULTRALOW_GRADE"
                            ]
                        )
                    )
                    / np.log(10)
                )
            )
        )
    )
    value.loc[["TRACE_GRADE"]] = float(
        coefficients_prospecting_from_all().loc["MIN_VALUE", "TRACE_GRADE"]
    ) + (
        float(coefficients_prospecting_from_all().loc["MAX_VALUE", "TRACE_GRADE"])
        - float(coefficients_prospecting_from_all().loc["MIN_VALUE", "TRACE_GRADE"])
    ) / (
        1
        + 10
        ** (
            float(coefficients_prospecting_from_all().loc["N", "TRACE_GRADE"])
            * (
                (np.log(ni_known_reserves_all_grades()) / np.log(10))
                - (
                    np.log(
                        float(
                            coefficients_prospecting_from_all().loc[
                                "EC50", "TRACE_GRADE"
                            ]
                        )
                    )
                    / np.log(10)
                )
            )
        )
    )
    value.loc[["OCEANS_GRADE"]] = 0
    return value


@component.add(
    name="prospecting_for_Ni_from_grades",
    units="DMNL",
    subscripts=["ORE_GRADES_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "ni_known_reserves": 6,
        "coefficients_prospecting_from_grades": 30,
        "avoid_zero_division": 3,
    },
)
def prospecting_for_ni_from_grades():
    """
    Sigmoid Fitting - prospecting for Ni min+(max-min)/(1+10^(n*(log10(x)-log10(ec_50)))) High grade: Sigmoid Fitting - prospecting for Ni high and low n 7,684334811 min 0,010589989 max 2,005044986 ec50 5,53505278 low grade: n 7,922850142 min -0,033393353 max 1,975174461 ec50 5,539989466 ULG n 9,293426946 min -0,019635893 max 1,977579607 ec50 6,081686643 trace n 9,293426946 min -0,019635893 max 1,977579607 ec50 6,081686643
    """
    value = xr.DataArray(
        np.nan, {"ORE_GRADES_I": _subscript_dict["ORE_GRADES_I"]}, ["ORE_GRADES_I"]
    )
    value.loc[["RICH_GRADE"]] = 0
    value.loc[["HIGH_GRADE"]] = 0
    value.loc[["LOW_GRADE"]] = if_then_else(
        float(ni_known_reserves().loc["LOW_GRADE"]) > 0,
        lambda: float(
            coefficients_prospecting_from_grades().loc["MIN_VALUE", "LOW_GRADE"]
        )
        + (
            float(coefficients_prospecting_from_grades().loc["MAX_VALUE", "LOW_GRADE"])
            - float(
                coefficients_prospecting_from_grades().loc["MIN_VALUE", "LOW_GRADE"]
            )
        )
        / (
            1
            + 10
            ** (
                float(coefficients_prospecting_from_grades().loc["N", "LOW_GRADE"])
                * (
                    (np.log(float(ni_known_reserves().loc["LOW_GRADE"])) / np.log(10))
                    - (
                        np.log(
                            float(
                                coefficients_prospecting_from_grades().loc[
                                    "EC50", "LOW_GRADE"
                                ]
                            )
                        )
                        / np.log(10)
                    )
                )
            )
        ),
        lambda: float(
            coefficients_prospecting_from_grades().loc["MIN_VALUE", "LOW_GRADE"]
        )
        + (
            float(coefficients_prospecting_from_grades().loc["MAX_VALUE", "LOW_GRADE"])
            - float(
                coefficients_prospecting_from_grades().loc["MIN_VALUE", "LOW_GRADE"]
            )
        )
        / (
            1
            + 10
            ** (
                float(coefficients_prospecting_from_grades().loc["N", "LOW_GRADE"])
                * (
                    (np.log(avoid_zero_division()) / np.log(10))
                    - (
                        np.log(
                            float(
                                coefficients_prospecting_from_grades().loc[
                                    "EC50", "LOW_GRADE"
                                ]
                            )
                        )
                        / np.log(10)
                    )
                )
            )
        ),
    )
    value.loc[["ULTRALOW_GRADE"]] = if_then_else(
        float(ni_known_reserves().loc["ULTRALOW_GRADE"]) > 0,
        lambda: float(
            coefficients_prospecting_from_grades().loc["MIN_VALUE", "ULTRALOW_GRADE"]
        )
        + (
            float(
                coefficients_prospecting_from_grades().loc[
                    "MAX_VALUE", "ULTRALOW_GRADE"
                ]
            )
            - float(
                coefficients_prospecting_from_grades().loc[
                    "MIN_VALUE", "ULTRALOW_GRADE"
                ]
            )
        )
        / (
            1
            + 10
            ** (
                float(coefficients_prospecting_from_grades().loc["N", "ULTRALOW_GRADE"])
                * (
                    (
                        np.log(float(ni_known_reserves().loc["ULTRALOW_GRADE"]))
                        / np.log(10)
                    )
                    - (
                        np.log(
                            float(
                                coefficients_prospecting_from_grades().loc[
                                    "EC50", "ULTRALOW_GRADE"
                                ]
                            )
                        )
                        / np.log(10)
                    )
                )
            )
        ),
        lambda: float(
            coefficients_prospecting_from_grades().loc["MIN_VALUE", "ULTRALOW_GRADE"]
        )
        + (
            float(
                coefficients_prospecting_from_grades().loc[
                    "MAX_VALUE", "ULTRALOW_GRADE"
                ]
            )
            - float(
                coefficients_prospecting_from_grades().loc[
                    "MIN_VALUE", "ULTRALOW_GRADE"
                ]
            )
        )
        / (
            1
            + 10
            ** (
                float(coefficients_prospecting_from_grades().loc["N", "ULTRALOW_GRADE"])
                * (
                    (np.log(avoid_zero_division()) / np.log(10))
                    - (
                        np.log(
                            float(
                                coefficients_prospecting_from_grades().loc[
                                    "EC50", "ULTRALOW_GRADE"
                                ]
                            )
                        )
                        / np.log(10)
                    )
                )
            )
        ),
    )
    value.loc[["TRACE_GRADE"]] = if_then_else(
        float(ni_known_reserves().loc["TRACE_GRADE"]) > 0,
        lambda: float(
            coefficients_prospecting_from_grades().loc["MIN_VALUE", "TRACE_GRADE"]
        )
        + (
            float(
                coefficients_prospecting_from_grades().loc["MAX_VALUE", "TRACE_GRADE"]
            )
            - float(
                coefficients_prospecting_from_grades().loc["MIN_VALUE", "TRACE_GRADE"]
            )
        )
        / (
            1
            + 10
            ** (
                float(coefficients_prospecting_from_grades().loc["N", "TRACE_GRADE"])
                * (
                    (np.log(float(ni_known_reserves().loc["TRACE_GRADE"])) / np.log(10))
                    - (
                        np.log(
                            float(
                                coefficients_prospecting_from_grades().loc[
                                    "EC50", "TRACE_GRADE"
                                ]
                            )
                        )
                        / np.log(10)
                    )
                )
            )
        ),
        lambda: float(
            coefficients_prospecting_from_grades().loc["MIN_VALUE", "TRACE_GRADE"]
        )
        + (
            float(
                coefficients_prospecting_from_grades().loc["MAX_VALUE", "TRACE_GRADE"]
            )
            - float(
                coefficients_prospecting_from_grades().loc["MIN_VALUE", "TRACE_GRADE"]
            )
        )
        / (
            1
            + 10
            ** (
                float(coefficients_prospecting_from_grades().loc["N", "TRACE_GRADE"])
                * (
                    (np.log(avoid_zero_division()) / np.log(10))
                    - (
                        np.log(
                            float(
                                coefficients_prospecting_from_grades().loc[
                                    "EC50", "TRACE_GRADE"
                                ]
                            )
                        )
                        / np.log(10)
                    )
                )
            )
        ),
    )
    value.loc[["OCEANS_GRADE"]] = 0
    return value


@component.add(
    name="prospecting_technology_improvements_for_NI",
    units="DMNL",
    subscripts=["ORE_GRADES_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={"coefficients_prospecting_technology_improvements": 15, "time": 5},
)
def prospecting_technology_improvements_for_ni():
    """
    Olafsdottir, A.H., and Sverdrup, H., 2020, System dynamics modelling of mining, supply, recycling, stocks-in-use and market price for nickel. Mining, Metallurgy & Exploration. 1-22. 10.1007/s42461-020-00370-
    """
    value = xr.DataArray(
        np.nan, {"ORE_GRADES_I": _subscript_dict["ORE_GRADES_I"]}, ["ORE_GRADES_I"]
    )
    value.loc[["RICH_GRADE"]] = float(
        coefficients_prospecting_technology_improvements().loc[
            "RICH_GRADE", "A_S_CURVE"
        ]
    ) / (
        1
        + np.exp(
            -float(
                coefficients_prospecting_technology_improvements().loc[
                    "RICH_GRADE", "B_S_CURVE"
                ]
            )
            * (
                time()
                - float(
                    coefficients_prospecting_technology_improvements().loc[
                        "RICH_GRADE", "C_S_CURVE"
                    ]
                )
            )
        )
    )
    value.loc[["HIGH_GRADE"]] = float(
        coefficients_prospecting_technology_improvements().loc[
            "HIGH_GRADE", "A_S_CURVE"
        ]
    ) / (
        1
        + np.exp(
            -float(
                coefficients_prospecting_technology_improvements().loc[
                    "HIGH_GRADE", "B_S_CURVE"
                ]
            )
            * (
                time()
                - float(
                    coefficients_prospecting_technology_improvements().loc[
                        "HIGH_GRADE", "C_S_CURVE"
                    ]
                )
            )
        )
    )
    value.loc[["LOW_GRADE"]] = float(
        coefficients_prospecting_technology_improvements().loc["LOW_GRADE", "A_S_CURVE"]
    ) / (
        1
        + np.exp(
            -float(
                coefficients_prospecting_technology_improvements().loc[
                    "LOW_GRADE", "B_S_CURVE"
                ]
            )
            * (
                time()
                - float(
                    coefficients_prospecting_technology_improvements().loc[
                        "LOW_GRADE", "C_S_CURVE"
                    ]
                )
            )
        )
    )
    value.loc[["ULTRALOW_GRADE"]] = float(
        coefficients_prospecting_technology_improvements().loc[
            "ULTRALOW_GRADE", "A_S_CURVE"
        ]
    ) / (
        1
        + np.exp(
            -float(
                coefficients_prospecting_technology_improvements().loc[
                    "ULTRALOW_GRADE", "B_S_CURVE"
                ]
            )
            * (
                time()
                - float(
                    coefficients_prospecting_technology_improvements().loc[
                        "ULTRALOW_GRADE", "C_S_CURVE"
                    ]
                )
            )
        )
    )
    value.loc[["TRACE_GRADE"]] = float(
        coefficients_prospecting_technology_improvements().loc[
            "TRACE_GRADE", "A_S_CURVE"
        ]
    ) / (
        1
        + np.exp(
            -float(
                coefficients_prospecting_technology_improvements().loc[
                    "TRACE_GRADE", "B_S_CURVE"
                ]
            )
            * (
                time()
                - float(
                    coefficients_prospecting_technology_improvements().loc[
                        "TRACE_GRADE", "C_S_CURVE"
                    ]
                )
            )
        )
    )
    value.loc[["OCEANS_GRADE"]] = 0
    return value


@component.add(
    name="prospekting_rate_Ni",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ni_mining_efficiency_curve": 1, "promotion_of_prospecting": 1},
)
def prospekting_rate_ni():
    """
    The prospecting rate is scaled up with a technical learning curve. The curve carries the fact that prospecting started out as being surficial and primitive i 1850, and evolved with technical progress allowing for drilling and using high technology for prospecting.
    """
    return ni_mining_efficiency_curve() * promotion_of_prospecting()


@component.add(
    name="SWITCH_ECO2MAT_Ni_DEMAND",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_eco2mat_ni_demand"},
)
def switch_eco2mat_ni_demand():
    """
    Intermodule links SWITCH, it can take two values: 0: the link is broken, the intermodule variable is replaced by an exogenous parameter. 1: the link between modules is operational.
    """
    return _ext_constant_switch_eco2mat_ni_demand()


_ext_constant_switch_eco2mat_ni_demand = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_ECO2MAT_Ni_DEMAND",
    {},
    _root,
    {},
    "_ext_constant_switch_eco2mat_ni_demand",
)


@component.add(
    name="SWITCH_MAT2ECO_Ni_PRICE",
    units="1",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_mat2eco_ni_price"},
)
def switch_mat2eco_ni_price():
    """
    Intermodule links SWITCH, it can take two values: 0: the link is broken, the intermodule variable is replaced by an exogenous parameter. 1: the link between modules is operational.
    """
    return _ext_constant_switch_mat2eco_ni_price()


_ext_constant_switch_mat2eco_ni_price = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_MAT2ECO_Ni_PRICE",
    {},
    _root,
    {},
    "_ext_constant_switch_mat2eco_ni_price",
)


@component.add(
    name="total_Ni_known_reserves",
    units="Mt",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ni_known_reserves": 1},
)
def total_ni_known_reserves():
    """
    Sum of Ni known reserves in different ore grades
    """
    return sum(
        ni_known_reserves().rename({"ORE_GRADES_I": "ORE_GRADES_I!"}),
        dim=["ORE_GRADES_I!"],
    )


@component.add(
    name="water_Ni_all",
    units="Mm3/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"water_use_ni_recycle": 1, "water_ni_extraction": 1},
)
def water_ni_all():
    """
    total Cu energy use for extraction and refining including secondary and from recycling
    """
    return water_use_ni_recycle() + water_ni_extraction()


@component.add(
    name="water_Ni_extraction",
    units="Mm3/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"water_use_ni": 5, "water_use_ni_secondary": 1},
)
def water_ni_extraction():
    """
    total Ni energy use for extraction and refining including secondary extraction This is the energy and water used associated with the materials consumed to extract this specific resource grade, expressed in MJ/kg product and m3/ton The actual values are taken from an internal LOCOMOTION report that have extracted the available values from literature and extrapolations. Source: Harald Sverdrup and Anna Hulda Olafsdottir 2021. Assessing with the WORLD7 model the global CO2 emissions and water use by metals, materials and fossil fuels extraction and production. LOCOMOTION working paper. 52 pages.
    """
    return (
        float(water_use_ni().loc["TRACE_GRADE"])
        + float(water_use_ni().loc["ULTRALOW_GRADE"])
        + float(water_use_ni().loc["LOW_GRADE"])
        + float(water_use_ni().loc["HIGH_GRADE"])
        + float(water_use_ni().loc["RICH_GRADE"])
        + water_use_ni_secondary()
    )


@component.add(
    name="water_per_Ni",
    units="Mt/Years",
    subscripts=["ORE_GRADES_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={"coefficients_water_per_ni": 5},
)
def water_per_ni():
    """
    Water use per resource quality
    """
    value = xr.DataArray(
        np.nan, {"ORE_GRADES_I": _subscript_dict["ORE_GRADES_I"]}, ["ORE_GRADES_I"]
    )
    value.loc[["RICH_GRADE"]] = float(coefficients_water_per_ni().loc["RICH_GRADE"])
    value.loc[["HIGH_GRADE"]] = float(coefficients_water_per_ni().loc["HIGH_GRADE"])
    value.loc[["LOW_GRADE"]] = float(coefficients_water_per_ni().loc["LOW_GRADE"])
    value.loc[["ULTRALOW_GRADE"]] = float(
        coefficients_water_per_ni().loc["ULTRALOW_GRADE"]
    )
    value.loc[["TRACE_GRADE"]] = float(coefficients_water_per_ni().loc["TRACE_GRADE"])
    value.loc[["OCEANS_GRADE"]] = 0
    return value


@component.add(
    name="WATER_PER_Ni_RECYCLE",
    units="Mm3/Mt",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_water_per_ni_recycle"},
)
def water_per_ni_recycle():
    """
    Our own estimates of water use per grade extraction, based on a large literature survey. See the separate report for documentation of setting the value and where the information came from. Sverdrup and Olafsdottir 2021: Assessing the global energy and water use from of metals, materials and fossil fuels extraction and production. Internal report for LOCOMOTION WP7. 44pp
    """
    return _ext_constant_water_per_ni_recycle()


_ext_constant_water_per_ni_recycle = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Nickel",
    "WATER_PER_Ni_RECYCLE",
    {},
    _root,
    {},
    "_ext_constant_water_per_ni_recycle",
)


@component.add(
    name="WATER_PER_Ni_SECONDARY",
    units="Mm3/Mt",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_water_per_ni_secondary"},
)
def water_per_ni_secondary():
    """
    m^3/ton is equivilent to saying Mm^3/Mt Our own estimates of water use per grade extraction, based on a large literature survey. See the separate report for documentation of setting the value and where the information came from. Sverdrup and Olafsdottir 2021: Assessing the global energy and water use from of metals, materials and fossil fuels extraction and production. Internal report for LOCOMOTION WP7. 44pp
    """
    return _ext_constant_water_per_ni_secondary()


_ext_constant_water_per_ni_secondary = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Nickel",
    "WATER_PER_Ni_SECONDARY",
    {},
    _root,
    {},
    "_ext_constant_water_per_ni_secondary",
)


@component.add(
    name="water_use_Ni",
    units="Mt/Years",
    subscripts=["ORE_GRADES_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={"ni_mining": 5, "water_per_ni": 5},
)
def water_use_ni():
    """
    Cu water use for extraction and refining from ore grades
    """
    value = xr.DataArray(
        np.nan, {"ORE_GRADES_I": _subscript_dict["ORE_GRADES_I"]}, ["ORE_GRADES_I"]
    )
    value.loc[["RICH_GRADE"]] = float(ni_mining().loc["RICH_GRADE"]) * float(
        water_per_ni().loc["RICH_GRADE"]
    )
    value.loc[["HIGH_GRADE"]] = float(ni_mining().loc["HIGH_GRADE"]) * float(
        water_per_ni().loc["HIGH_GRADE"]
    )
    value.loc[["LOW_GRADE"]] = float(water_per_ni().loc["LOW_GRADE"]) * float(
        ni_mining().loc["LOW_GRADE"]
    )
    value.loc[["ULTRALOW_GRADE"]] = float(ni_mining().loc["ULTRALOW_GRADE"]) * float(
        water_per_ni().loc["ULTRALOW_GRADE"]
    )
    value.loc[["TRACE_GRADE"]] = float(water_per_ni().loc["TRACE_GRADE"]) * float(
        ni_mining().loc["TRACE_GRADE"]
    )
    value.loc[["OCEANS_GRADE"]] = 0
    return value


@component.add(
    name="water_use_Ni_recycle",
    units="Mm3/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"water_per_ni_recycle": 1, "ni_other_recycling": 1},
)
def water_use_ni_recycle():
    """
    water use for Ni extraction from recycling This is the energy and water used associated with the materials consumed to extract this specific resource grade, expressed in MJ/kg product and m3/ton The actual values are taken from an internal LOCOMOTION report that have extracted the available values from literature and extrapolations. Source: Harald Sverdrup and Anna Hulda Olafsdottir 2021. Assessing with the WORLD7 model the global CO2 emissions and water use by metals, materials and fossil fuels extraction and production. LOCOMOTION working paper. 52 pages.
    """
    return water_per_ni_recycle() * ni_other_recycling()


@component.add(
    name="water_use_Ni_secondary",
    units="Mm3/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"water_per_ni_secondary": 1, "ni_secondary": 1},
)
def water_use_ni_secondary():
    """
    m^3/ton is equivilent to saying Mm^3/Mt This is the energy and water used associated with the materials consumed to extract this specific resource grade, expressed in MJ/kg product and m3/ton The actual values are taken from an internal LOCOMOTION report that have extracted the available values from literature and extrapolations. Source: Harald Sverdrup and Anna Hulda Olafsdottir 2021. Assessing with the WORLD7 model the global CO2 emissions and water use by metals, materials and fossil fuels extraction and production. LOCOMOTION working paper. 52 pages.
    """
    return water_per_ni_secondary() * ni_secondary()
