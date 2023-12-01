"""
Module materials.al
Translated using PySD version 3.10.0
"""


@component.add(
    name="Al_available",
    units="Mt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"al_market": 1, "al_market_supply": 1},
)
def al_available():
    """
    All the Aluminium- on the market and moving to the market.
    """
    return al_market() + al_market_supply()


@component.add(
    name="Al_available_DELAYED",
    units="Mt/Year",
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_al_available_delayed": 1},
    other_deps={
        "_delayfixed_al_available_delayed": {
            "initial": {"initial_al_available": 1, "time_step": 1},
            "step": {"al_available": 1},
        }
    },
)
def al_available_delayed():
    """
    All Aluminium, going to the market and shipped to the market. Delayed to prevent simoultanous equation in vensim.Initial used to have a first value.
    """
    return _delayfixed_al_available_delayed()


_delayfixed_al_available_delayed = DelayFixed(
    lambda: al_available(),
    lambda: time_step(),
    lambda: initial_al_available(),
    time_step,
    "_delayfixed_al_available_delayed",
)


@component.add(
    name="Al_BASE_PRICE_2006",
    units="$/t",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_al_base_price_2006"},
)
def al_base_price_2006():
    """
    Base price in the year 2015. Base year is used to calculate the start price in the year 2015 which needs to be one hundred for the economic module. New value: 2538 old value: 4735.72
    """
    return _ext_constant_al_base_price_2006()


_ext_constant_al_base_price_2006 = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Aluminium",
    "Al_BASE_PRICE_2006",
    {},
    _root,
    {},
    "_ext_constant_al_base_price_2006",
)


@component.add(
    name="Al_costs",
    units="Mdollars/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"al_grade_cost": 2, "mining_al_known_reserves": 2},
)
def al_costs():
    """
    Extraction cost for Aluminium from high and from low grade.
    """
    return float(al_grade_cost().loc["HIGH_GRADE"]) * float(
        mining_al_known_reserves().loc["HIGH_GRADE"]
    ) + float(al_grade_cost().loc["LOW_GRADE"]) * float(
        mining_al_known_reserves().loc["LOW_GRADE"]
    )


@component.add(
    name="Al_cumulative_mining",
    units="Mt",
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_al_cumulative_mining": 1},
    other_deps={
        "_integ_al_cumulative_mining": {
            "initial": {"initial_al_cumulative_mining": 1},
            "step": {"increase_al_cumulative": 1},
        }
    },
)
def al_cumulative_mining():
    """
    Al cumulativly mined.
    """
    return _integ_al_cumulative_mining()


_integ_al_cumulative_mining = Integ(
    lambda: increase_al_cumulative(),
    lambda: initial_al_cumulative_mining(),
    "_integ_al_cumulative_mining",
)


@component.add(
    name="Al_demand",
    units="Mt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "switch_eco2mat_al_demand": 1,
        "switch_materials": 1,
        "al_modified_demand_world7": 1,
        "implicit_price_al": 1,
        "output_real": 1,
    },
)
def al_demand():
    """
    Aluminium demand-either historical or after 2015 coming from the economic module.
    """
    return if_then_else(
        np.logical_or(
            time() < 2015,
            np.logical_or(switch_eco2mat_al_demand() == 0, switch_materials() == 0),
        ),
        lambda: al_modified_demand_world7(),
        lambda: sum(
            output_real()
            .loc[:, "MINING_AND_MANUFACTURING_ALUMINIUM"]
            .reset_coords(drop=True)
            .rename({"REGIONS_35_I": "REGIONS_35_I!"}),
            dim=["REGIONS_35_I!"],
        )
        / implicit_price_al(),
    )


@component.add(
    name="Al_DEMAND_BASE_YEAR",
    units="Mt/Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_al_demand_base_year"},
)
def al_demand_base_year():
    """
    Al demand historical in the Year 2015 is 73 Mt
    """
    return _ext_constant_al_demand_base_year()


_ext_constant_al_demand_base_year = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Aluminium",
    "Al_DEMAND_BASE_YEAR",
    {},
    _root,
    {},
    "_ext_constant_al_demand_base_year",
)


@component.add(
    name="Al_DEMAND_DEVELOPMENT_WOLRD_7",
    units="Mt/Year",
    comp_type="Auxiliary",
    comp_subtype="with Lookup",
    depends_on={"time": 1},
)
def al_demand_development_wolrd_7():
    """
    Demand development according to Al model in World 7 Source : Sverdrup, H. U., Ragnarsdottir, K. V. and Koca, D. (2015) Aluminium for the future: Modelling the global production, market supply, demand, price and long term development of the global reserves, Resources, Conservation and Recycling, 103, pp. 139-154. doi: 10.1016/j.resconrec.2015.06.008. Sverdrup, H., & Ragnarsdóttir, K. V. (2014). Natural Resources in a Planetary Perspective. Geochemical Perspectives, 3(2), 129–341. https://doi.org/10.7185/geochempersp.3.2
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
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.43802,
            0.444297,
            0.649828,
            0.649824,
            0.858288,
            0.870251,
            0.886433,
            0.912746,
            0.935409,
            1.20246,
            1.20198,
            1.44108,
            1.45601,
            1.50006,
            1.77849,
            1.75095,
            1.88143,
            1.62898,
            1.44649,
            1.48349,
            1.46174,
            1.49513,
            1.5222,
            1.58976,
            1.65954,
            1.70326,
            1.76147,
            1.82548,
            1.94215,
            2.05645,
            2.11358,
            2.14952,
            2.27257,
            2.38954,
            2.49818,
            2.67324,
            2.80411,
            2.86873,
            2.9669,
            3.0442,
            2.84477,
            2.96801,
            3.18459,
            3.28092,
            3.38173,
            3.61685,
            3.83124,
            4.04279,
            4.31221,
            4.58893,
            4.63196,
            4.86394,
            5.0183,
            5.17059,
            5.85324,
            6.34303,
            6.91912,
            7.21676,
            7.69413,
            8.13305,
            8.58274,
            9.50148,
            10.111,
            11.0849,
            12.9304,
            13.527,
            14.359,
            15.6308,
            17.522,
            18.1024,
            19.6997,
            20.3554,
            21.5063,
            22.7357,
            24.4886,
            25.2224,
            26.8164,
            28.0977,
            29.7377,
            30.9125,
            32.2016,
            33.74,
            35.0519,
            35.9833,
            37.3338,
            38.9679,
            41.8437,
            43.6952,
            46.4594,
            48.0917,
            49.9427,
            52.7455,
            55.0369,
            58.7263,
            61.3103,
            62.888,
            64.8878,
            66.608,
            69.6328,
            73.6658,
            75.7774,
            79.6213,
            81.3006,
            85.3277,
            87.1989,
            90.4828,
            91.8225,
            93.2084,
            97.5255,
            99.3784,
            101.642,
            105.066,
            107.011,
            109.976,
            112.445,
            115.305,
            117.857,
            120.802,
            124.04,
            125.435,
            127.584,
            129.5,
            132.015,
            134.976,
            138.216,
            140.301,
            142.242,
            143.755,
            145.529,
            146.93,
            148.432,
            149.446,
            150.868,
            152.691,
            154.362,
            155.916,
            156.661,
            157.879,
            158.935,
            159.581,
            160.395,
            161.655,
            163.05,
            163.738,
            164.222,
            164.466,
            164.893,
            165.134,
            165.899,
            167.749,
            169.925,
            170.223,
            171.41,
            171.572,
            171.533,
            171.726,
            172.36,
            173.122,
            173.106,
            173.426,
            173.734,
            173.682,
            173.867,
            173.348,
            172.825,
            172.645,
            172.116,
            171.586,
            171.054,
            170.522,
            170.188,
            170.186,
            170.066,
            169.531,
            168.996,
            168.462,
            167.929,
            167.397,
            166.866,
            166.658,
            166.558,
            166.204,
            165.675,
            165.147,
            164.621,
            164.096,
            163.572,
            163.099,
            162.997,
            162.893,
            162.388,
            161.868,
        ],
    )


@component.add(
    name="Al_DEMAND_DEVELOPMENT_WORLD_ALUMINIUM",
    units="Mt/Year",
    comp_type="Auxiliary",
    comp_subtype="with Lookup",
    depends_on={"time": 1},
)
def al_demand_development_world_aluminium():
    """
    Historical Al ingot demand development according to Source: https://alucycle.world-aluminium.org/public-access/ accessed 01.03.2023
    """
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
        ],
        [
            47.488,
            52.427,
            57.262,
            60.518,
            58.008,
            65.673,
            72.373,
            74.705,
            78.364,
            83.313,
            86.083,
            88.43,
            96.472,
            96.784,
            98.364,
            100.286,
            105.33,
        ],
    )


@component.add(
    name="Al_demand_HISTORICAL_WORLD_7",
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_al_demand_historical_world_7",
        "__data__": "_ext_data_al_demand_historical_world_7",
        "time": 1,
    },
)
def al_demand_historical_world_7():
    """
    Historical Aluminium demand coming from from the World 7 model.
    """
    return _ext_data_al_demand_historical_world_7(time())


_ext_data_al_demand_historical_world_7 = ExtData(
    "model_parameters/materials/materials.xlsx",
    "Aluminium",
    "TIME_SERIES_Al",
    "Al_DEMAND_HISTORICAL_WORLD_7",
    None,
    {},
    _root,
    {},
    "_ext_data_al_demand_historical_world_7",
)


@component.add(
    name="Al_demand_including_semifinished_products",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "al_demand": 1,
        "al_demand_scaling_factor_for_semi_finished_products": 1,
    },
)
def al_demand_including_semifinished_products():
    return al_demand() * al_demand_scaling_factor_for_semi_finished_products()


@component.add(
    name="Al_demand_price_reponse",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"price_sensitivity_s_curve_fit": 3, "al_price_economy": 1},
)
def al_demand_price_reponse():
    """
    This variable captures the relation of the market price and the demand. An increase of the market price will have a reducing effect on the demand. Reference: Sverdrup, H., and Olafsdottir, A.H., 2019. Conceptualization and parameterization of the market price mechanism in the WORLD6 model for metals, materials and fossil fuels. Mineral Economics 1-26. Springer Nature DOI: 10.1007/s13563-019-00182-7. Olafsdottir, A.H.; Gudbrandsdottir, I.; Sverdrup, H.U.; Olafsdottir, G.; Bogason, S.G.; 2018 On modelling the price of beef and salmon using a fully dynamic approach.. The 36nd International Conference of the System Dynamics Society, System Dynamics Society, Reykjavik. Iceland. Sverdrup, H. U., Ragnarsdottir, K. V. and Koca, D. (2015) Aluminium for the future: Modelling the global production, market supply, demand, price and long term development of the global reservesâ€™, Resources, Conservation and Recycling, 103, pp. 139â€“154. doi: 10.1016/j.resconrec.2015.06.008.
    """
    return (
        float(price_sensitivity_s_curve_fit().loc["A_S_CURVE_FIT"])
        * (
            1
            - np.exp(
                -float(price_sensitivity_s_curve_fit().loc["k_S_CURVE_FIT"])
                * al_price_economy()
                ** float(price_sensitivity_s_curve_fit().loc["n_S_CURVE_FIT"])
            )
        )
        + 1
    )


@component.add(
    name="Al_DEMAND_PROJECTION_IAI",
    units="Mt/Year",
    comp_type="Auxiliary",
    comp_subtype="with Lookup",
    depends_on={"time": 1},
)
def al_demand_projection_iai():
    """
    Source: International Aluminium Institute (IAI) updated version of its material flow model https://international-aluminium.org/resource/iai-material-flow-model-2021-u pdate/
    """
    return np.interp(
        time(),
        [
            1950.0,
            1960.0,
            1970.0,
            1980.0,
            1990.0,
            2000.0,
            2010.0,
            2020.0,
            2030.0,
            2040.0,
            2050.0,
        ],
        [
            4.54545,
            6.36364,
            12.7273,
            20.0,
            28.1818,
            37.2727,
            64.0909,
            98.6364,
            120.0,
            153.636,
            175.455,
        ],
    )


@component.add(
    name="Al_DEMAND_SCALING_FACTOR_FOR_SEMI_FINISHED_PRODUCTS",
    units="1/Year",
    comp_type="Constant",
    comp_subtype="Normal",
)
def al_demand_scaling_factor_for_semi_finished_products():
    """
    Al demand scaled to be Al Ingot demand. Al Ingot is used to produce products that are caputred with Al demand. Around ca. 15% of Aluminiun used for Semi finished to finished products is recycled as new scrap. New scrap enters the market supply directly as new supply of recycled Al. Parameter Estimation Based on : (Bertram et al., 2017)Bertram, M., Ramkumar, S., Rechberger, H., Rombach, G., Bayliss, C., Martchek, K. J., Müller, D. B., & Liu, G. (2017). A regionally-linked, dynamic material flow modelling tool for rolled, extruded and cast aluminium products. Resources, Conservation and Recycling, 125(May), 48–69. https://doi.org/10.1016/j.resconrec.2017.05.014 And: Public Access - International Aluminium Institute. (n.d.). Retrieved March 3, 2023, from https://alucycle.world-aluminium.org/public-access/ (Public Access - International Aluminium Institute, n.d.)
    """
    return 1.144


@component.add(
    name="Al_demand_WORLD7",
    units="Mt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "world_pop": 1,
        "imv_al_target_demand_per_person": 1,
        "scaling_faktor_in_al_demand": 1,
        "al_material_yield_in_manufacture": 1,
    },
)
def al_demand_world7():
    """
    Total demand. Function of the variables IMV GLOBAL POPULATION*IMV Al TARGET DEMAND PER PERSON*SCALING FAKTOR IN Al DEMAND/MATERIAL YIELD IN MANUFACTURE.
    """
    return (
        world_pop()
        * imv_al_target_demand_per_person()
        * scaling_faktor_in_al_demand()
        / al_material_yield_in_manufacture()
    )


@component.add(
    name="Al_ENERGY_NEEDED_FOR_DIFFERENT_GRADE",
    units="TJ/Mt",
    subscripts=["Al_ORE_GRADES_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_al_energy_needed_for_different_grade"},
)
def al_energy_needed_for_different_grade():
    """
    Our own estimates of water use per grade extraction, based on a large literature survey. See the separate report for documentation of setting the value and where the information came from. HIGH GRADE 240 LOW GRADE 380 Sverdrup and Olafsdottir 2021: Assessing the global energy and water use from of metals, materials and fossil fuels extraction and production. Internal report for LOCOMOTION WP7. 44pp
    """
    return _ext_constant_al_energy_needed_for_different_grade()


_ext_constant_al_energy_needed_for_different_grade = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Aluminium",
    "Al_ENERGY_NEEDED_FOR_DIFFERENT_GRADE*",
    {"Al_ORE_GRADES_I": _subscript_dict["Al_ORE_GRADES_I"]},
    _root,
    {"Al_ORE_GRADES_I": _subscript_dict["Al_ORE_GRADES_I"]},
    "_ext_constant_al_energy_needed_for_different_grade",
)


@component.add(
    name="Al_energy_use",
    units="TJ/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"al_energy_use_ore_grades_mining": 2, "al_energy_use_recycling": 1},
)
def al_energy_use():
    """
    Energy used to produce Aluminium from high grade, Aluminium low grade and FROM Aluminium recycling.
    """
    return (
        float(al_energy_use_ore_grades_mining().loc["HIGH_GRADE"])
        + float(al_energy_use_ore_grades_mining().loc["LOW_GRADE"])
        + al_energy_use_recycling()
    )


@component.add(
    name="Al_energy_use_ore_grades_mining",
    units="TJ/Year",
    subscripts=["Al_ORE_GRADES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "mining_al_known_reserves": 2,
        "al_energy_needed_for_different_grade": 2,
        "imv_al_energy_efficiency": 2,
    },
)
def al_energy_use_ore_grades_mining():
    """
    Energy reqiurement for mining and producing Aluminium from High grade and low grade ore.
    """
    value = xr.DataArray(
        np.nan,
        {"Al_ORE_GRADES_I": _subscript_dict["Al_ORE_GRADES_I"]},
        ["Al_ORE_GRADES_I"],
    )
    value.loc[["HIGH_GRADE"]] = (
        float(mining_al_known_reserves().loc["HIGH_GRADE"])
        * float(al_energy_needed_for_different_grade().loc["HIGH_GRADE"])
        / imv_al_energy_efficiency()
    )
    value.loc[["LOW_GRADE"]] = (
        float(mining_al_known_reserves().loc["LOW_GRADE"])
        * float(al_energy_needed_for_different_grade().loc["LOW_GRADE"])
        / imv_al_energy_efficiency()
    )
    return value


@component.add(
    name="Al_energy_use_recycling",
    units="TJ/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "decrease_al_scrapped_metal_recycling": 1,
        "recycling_energy_use": 1,
        "imv_al_energy_efficiency": 1,
    },
)
def al_energy_use_recycling():
    """
    Energy Reqiurement for Aluminium recycling.
    """
    return (
        decrease_al_scrapped_metal_recycling() * recycling_energy_use()
    ) / imv_al_energy_efficiency()


@component.add(
    name="Al_energy_use_TOE",
    units="Mt*OE/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "al_energy_use": 1,
        "al_energy_use_toe_coefficient": 1,
        "al_energy_use_toe_coefficient_two": 1,
    },
)
def al_energy_use_toe():
    """
    Engery required for Aluminium extraction and production in TOE.
    """
    return (
        al_energy_use()
        * al_energy_use_toe_coefficient()
        / al_energy_use_toe_coefficient_two()
    )


@component.add(
    name="Al_ENERGY_USE_TOE_COEFFICIENT",
    units="Mt*OE/TJ",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_al_energy_use_toe_coefficient"},
)
def al_energy_use_toe_coefficient():
    """
    Our own estimates of water use per grade extraction, based on a large literature survey. See the separate report for documentation of setting the value and where the information came from. Al ENERGY USE TOE COEFFICIENT 41.8 Mt*OE/TJ Sverdrup and Olafsdottir 2021: Assessing the global energy and water use from of metals, materials and fossil fuels extraction and production. Internal report for LOCOMOTION WP7. 44pp
    """
    return _ext_constant_al_energy_use_toe_coefficient()


_ext_constant_al_energy_use_toe_coefficient = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Aluminium",
    "Al_ENERGY_USE_TOE_COEFFICIENT",
    {},
    _root,
    {},
    "_ext_constant_al_energy_use_toe_coefficient",
)


@component.add(
    name="Al_ENERGY_USE_TOE_COEFFICIENT_TWO",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_al_energy_use_toe_coefficient_two"},
)
def al_energy_use_toe_coefficient_two():
    """
    Our own estimates of water use per grade extraction, based on a large literature survey. See the separate report for documentation of setting the value and where the information came from. Al_ENERGY_USE_TOE_COEFFICIENT_TWO 1000 DMNL Sverdrup and Olafsdottir 2021: Assessing the global energy and water use from of metals, materials and fossil fuels extraction and production. Internal report for LOCOMOTION WP7. 44pp
    """
    return _ext_constant_al_energy_use_toe_coefficient_two()


_ext_constant_al_energy_use_toe_coefficient_two = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Aluminium",
    "Al_ENERGY_USE_TOE_COEFFICIENT_TWO",
    {},
    _root,
    {},
    "_ext_constant_al_energy_use_toe_coefficient_two",
)


@component.add(
    name="Al_EOL_RECYCLING_RATE_SP", comp_type="Constant", comp_subtype="Normal"
)
def al_eol_recycling_rate_sp():
    """
    Parameter Estimation Based on : (Bertram et al., 2017)Bertram, M., Ramkumar, S., Rechberger, H., Rombach, G., Bayliss, C., Martchek, K. J., Müller, D. B., & Liu, G. (2017). A regionally-linked, dynamic material flow modelling tool for rolled, extruded and cast aluminium products. Resources, Conservation and Recycling, 125(May), 48–69. https://doi.org/10.1016/j.resconrec.2017.05.014 And: Public Access - International Aluminium Institute. (n.d.). Retrieved March 3, 2023, from https://alucycle.world-aluminium.org/public-access/ (Public Access - International Aluminium Institute, n.d.)
    """
    return 0.7


@component.add(
    name="Al_extraction_coefficient",
    units="1/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "coefficients_al_production_rate_factor": 1,
        "decrease_al_profit": 1,
        "imv_al_mining_and_refining_improvement_technology": 1,
    },
)
def al_extraction_coefficient():
    """
    Mining of bauxite and processing to Aluminium is driven by profit in the model. Al extraction coefficient is increased with increasing profits. When the Al extraction coefficient is increased the extraction of Aluminium is increasing. Sverdrup, H. U., Ragnarsdottir, K. V. and Koca, D. (2015) Aluminium for the future: Modelling the global production, market supply, demand, price and long term development of the global reservesâ€™, Resources, Conservation and Recycling, 103, pp. 139â€“154. doi: 10.1016/j.resconrec.2015.06.008. *0.72
    """
    return (
        coefficients_al_production_rate_factor()
        * decrease_al_profit()
        * imv_al_mining_and_refining_improvement_technology()
    )


@component.add(
    name="Al_GRADE_COST",
    units="M$/Mt",
    subscripts=["Al_ORE_GRADES_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_al_grade_cost"},
)
def al_grade_cost():
    """
    Price to mine, extract and refine one ton of Aluminium from high grade Bauxite. Value: 600 Price to mine, extract and refine one ton of Aluminium from low grade Bauxite. Value: 1860 Source: Sverdrup, H. U., Ragnarsdottir, K. V., & Koca, D. (2015). Aluminium for the future: Modelling the global production, market supply, demand, price and long term development of the global reserves. Resources, Conservation and Recycling, 103, 139-154. doi:10.1016/j.resconrec.2015.06.008.
    """
    return _ext_constant_al_grade_cost()


_ext_constant_al_grade_cost = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Aluminium",
    "Al_GRADE_COST*",
    {"Al_ORE_GRADES_I": _subscript_dict["Al_ORE_GRADES_I"]},
    _root,
    {"Al_ORE_GRADES_I": _subscript_dict["Al_ORE_GRADES_I"]},
    "_ext_constant_al_grade_cost",
)


@component.add(
    name="Al_grades_hidden_resources_to_Al_reserves",
    units="Mt/Year",
    subscripts=["Al_ORE_GRADES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "al_prospecting": 2,
        "al_hidden_resources": 2,
        "change_al_mining_technology_s_curve": 2,
    },
)
def al_grades_hidden_resources_to_al_reserves():
    """
    Amount of Aluminium that move from resources to reservers per year.
    """
    value = xr.DataArray(
        np.nan,
        {"Al_ORE_GRADES_I": _subscript_dict["Al_ORE_GRADES_I"]},
        ["Al_ORE_GRADES_I"],
    )
    value.loc[["HIGH_GRADE"]] = (
        al_prospecting()
        * float(al_hidden_resources().loc["HIGH_GRADE"])
        * change_al_mining_technology_s_curve()
    )
    value.loc[["LOW_GRADE"]] = (
        al_prospecting()
        * change_al_mining_technology_s_curve()
        * float(al_hidden_resources().loc["LOW_GRADE"])
    )
    return value


@component.add(
    name="Al_hidden_resources",
    units="Mt",
    subscripts=["Al_ORE_GRADES_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_al_hidden_resources": 1},
    other_deps={
        "_integ_al_hidden_resources": {
            "initial": {"initial_al_hidden_resources": 1},
            "step": {"al_grades_hidden_resources_to_al_reserves": 1},
        }
    },
)
def al_hidden_resources():
    """
    World 7 name was Al hidden high grade, Al hidden low grade, the initial values for the Al hidden stocks are based on simulation outputs from the World 7 for the year 2005. high grade is 5138,453716 Mt low grade is 6963,113157 Mt Estimations about the resource stocks that are hidden are based on: Sverdrup, H. U., Ragnarsdottir, K. V. and Koca, D. (2015) Aluminium for the future: Modelling the global production, market supply, demand, price and long term development of the global reserves, Resources, Conservation and Recycling, 103, pp. 139-154. doi: 10.1016/j.resconrec.2015.06.008. Sverdrup, H., & Ragnarsdóttir, K. V. (2014). Natural Resources in a Planetary Perspective. Geochemical Perspectives, 3(2), 129–341. https://doi.org/10.7185/geochempersp.3.2
    """
    return _integ_al_hidden_resources()


_integ_al_hidden_resources = Integ(
    lambda: -al_grades_hidden_resources_to_al_reserves(),
    lambda: initial_al_hidden_resources(),
    "_integ_al_hidden_resources",
)


@component.add(
    name="Al_in_use_per_person",
    units="Mt/Billion_People",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"al_stocks_in_use": 1, "imv_global_population": 1},
)
def al_in_use_per_person():
    """
    Aluminium in use per person.
    """
    return al_stocks_in_use() / imv_global_population()


@component.add(
    name="Al_income",
    units="Mdollars/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"al_mined": 1, "al_price_economy": 1},
)
def al_income():
    """
    Aluminium income from mining.
    """
    return al_mined() * al_price_economy()


@component.add(
    name="Al_known_reseveres",
    units="Mt",
    subscripts=["Al_ORE_GRADES_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_al_known_reseveres": 1},
    other_deps={
        "_integ_al_known_reseveres": {
            "initial": {"initial_al_known_reserves": 1},
            "step": {
                "al_grades_hidden_resources_to_al_reserves": 1,
                "mining_al_known_reserves": 1,
            },
        }
    },
)
def al_known_reseveres():
    """
    World 7 name was Al known high grade, Al known low grade, the initial values for the Al hidden stocks are based on simulation outputs from the World 7 for the year 2005. high grade is 4074,746287 Mt low grade is 5096,813181 Mt Estimations about the resource stocks that are hidden are based on: Sverdrup, H. U., Ragnarsdottir, K. V. and Koca, D. (2015) Aluminium for the future: Modelling the global production, market supply, demand, price and long term development of the global reserves, Resources, Conservation and Recycling, 103, pp. 139-154. doi: 10.1016/j.resconrec.2015.06.008. Sverdrup, H., & Ragnarsdóttir, K. V. (2014). Natural Resources in a Planetary Perspective. Geochemical Perspectives, 3(2), 129–341. https://doi.org/10.7185/geochempersp.3.2
    """
    return _integ_al_known_reseveres()


_integ_al_known_reseveres = Integ(
    lambda: al_grades_hidden_resources_to_al_reserves() - mining_al_known_reserves(),
    lambda: initial_al_known_reserves(),
    "_integ_al_known_reseveres",
)


@component.add(
    name="Al_low_grade_change_price",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"coefficients_change_al_grade": 3, "al_price_economy": 1},
)
def al_low_grade_change_price():
    """
    Describes the relation of price to the efforts started to extract Aluminium from more costly (lower ore grade) reserves. Y= A *(1-EXP(-k*t^n)) A= k= t= Al market price n= References: Sverdrup, H. U., Ragnarsdottir, K. V. and Koca, D. (2015) Aluminium for the future: Modelling the global production, market supply, demand, price and long term development of the global reservesâ€™, Resources, Conservation and Recycling, 103, pp. 139â€“154. doi: 10.1016/j.resconrec.2015.06.008. Harald Sverdrup, 2021: LOCOMOTION Project report: Estimating the cost of extraction and the price required for changing between mining of different ore grades in the WORLD7 model. 20 pp.
    """
    return float(coefficients_change_al_grade().loc["A_S_CURVE_FIT"]) * (
        1
        - np.exp(
            -float(coefficients_change_al_grade().loc["k_S_CURVE_FIT"])
            * al_price_economy()
            ** float(coefficients_change_al_grade().loc["n_S_CURVE_FIT"])
        )
    )


@component.add(
    name="Al_market",
    units="Mt",
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_al_market": 1},
    other_deps={
        "_integ_al_market": {
            "initial": {"initial_al_market": 1},
            "step": {"al_market_supply": 1, "al_market_sales": 1},
        }
    },
)
def al_market():
    """
    World_7_name: Al_market The initial values for the Al_market stocks are based on simulation outputs from the World 7 for the year 2005. World 7 name was AL market, The initial values for the Li market stock is based on simulation outputs from the World 7 for the year 2005. The World 7 outputs are based on initial values from 1850. Source: Sverdrup, H. U., Ragnarsdottir, K. V. and Koca, D. (2015) Aluminium for the future: Modelling the global production, market supply, demand, price and long term development of the global reservesâ€™, Resources, Conservation and Recycling, 103, pp. 139â€“154. doi: 10.1016/j.resconrec.2015.06.008.
    """
    return _integ_al_market()


_integ_al_market = Integ(
    lambda: np.maximum(0, al_market_supply() - al_market_sales()),
    lambda: initial_al_market(),
    "_integ_al_market",
)


@component.add(
    name="Al_market_sales",
    units="Mt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"al_market": 1, "al_demand_including_semifinished_products": 2},
)
def al_market_sales():
    """
    Aluminium that is sold according to the demand, if that can be forfilled and than goes into use.
    """
    return if_then_else(
        al_market() <= 0.1,
        lambda: np.maximum(al_demand_including_semifinished_products(), 0),
        lambda: al_demand_including_semifinished_products(),
    )


@component.add(
    name="Al_market_supply",
    units="Mt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "decrease_al_scrapped_metal_recycling": 1,
        "al_mined": 1,
        "al_new_scrap": 1,
    },
)
def al_market_supply():
    """
    Aluminium entering the market from recycling and from mining.
    """
    return decrease_al_scrapped_metal_recycling() + al_mined() + al_new_scrap()


@component.add(
    name="Al_MATERIAL_YIELD_IN_MANUFACTURE",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_al_material_yield_in_manufacture"},
)
def al_material_yield_in_manufacture():
    """
    How much of the material is used and the rest is returned to scrap. Value: 0.65
    """
    return _ext_constant_al_material_yield_in_manufacture()


_ext_constant_al_material_yield_in_manufacture = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Aluminium",
    "Al_MATERIAL_YIELD_IN_MANUFACTURE",
    {},
    _root,
    {},
    "_ext_constant_al_material_yield_in_manufacture",
)


@component.add(
    name="Al_mined",
    units="Mt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"mining_al_known_reserves": 2},
)
def al_mined():
    """
    world 7 name: Al total mining 1 This variable sums the total mining from different ore grades, i.e. Al_mining_different_grades[HIGH_GRADE]+Al_mining_different_grades[LOW_GRADE ]
    """
    return float(mining_al_known_reserves().loc["HIGH_GRADE"]) + float(
        mining_al_known_reserves().loc["LOW_GRADE"]
    )


@component.add(
    name="Al_mined_and_Al_recycled_EOL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"decrease_al_scrapped_metal_recycling": 1, "al_mined": 1},
)
def al_mined_and_al_recycled_eol():
    """
    Aluminium mined and Aluminium recycled EOL
    """
    return decrease_al_scrapped_metal_recycling() + al_mined()


@component.add(
    name="Al_modified_demand_WORLD7",
    units="Mt/Year",
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_al_modified_demand_world7": 1},
    other_deps={
        "_delayfixed_al_modified_demand_world7": {
            "initial": {"time_step": 1},
            "step": {"al_demand_price_reponse": 1, "al_demand_world7": 1},
        }
    },
)
def al_modified_demand_world7():
    """
    Variable from the world 7 model that reduces the demand when the price is getting to high. Reference: Sverdrup, H., and Olafsdottir, A.H., 2019. Conceptualization and parameterization of the market price mechanism in the WORLD6 model for metals, materials and fossil fuels. Mineral Economics 1-26. Springer Nature DOI: 10.1007/s13563-019-00182-7 Sverdrup, H. U., Ragnarsdottir, K. V. and Koca, D. (2015) Aluminium for the future: Modelling the global production, market supply, demand, price and long term development of the global reservesâ€™, Resources, Conservation and Recycling, 103, pp. 139â€“154. doi: 10.1016/j.resconrec.2015.06.008.
    """
    return _delayfixed_al_modified_demand_world7()


_delayfixed_al_modified_demand_world7 = DelayFixed(
    lambda: al_demand_price_reponse() * al_demand_world7(),
    lambda: time_step(),
    lambda: 42.41,
    time_step,
    "_delayfixed_al_modified_demand_world7",
)


@component.add(
    name="Al_new_scrap",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"al_market_sales": 1, "al_new_scrap_rate": 1},
)
def al_new_scrap():
    """
    Parameter Estimation Based on : (Bertram et al., 2017)Bertram, M., Ramkumar, S., Rechberger, H., Rombach, G., Bayliss, C., Martchek, K. J., Müller, D. B., & Liu, G. (2017). A regionally-linked, dynamic material flow modelling tool for rolled, extruded and cast aluminium products. Resources, Conservation and Recycling, 125(May), 48–69. https://doi.org/10.1016/j.resconrec.2017.05.014 And: Public Access - International Aluminium Institute. (n.d.). Retrieved March 3, 2023, from https://alucycle.world-aluminium.org/public-access/ (Public Access - International Aluminium Institute, n.d.)
    """
    return al_market_sales() * al_new_scrap_rate()


@component.add(
    name="Al_NEW_SCRAP_RATE",
    units="1/Year",
    comp_type="Constant",
    comp_subtype="Normal",
)
def al_new_scrap_rate():
    """
    Parameter Estimation Based on : (Bertram et al., 2017)Bertram, M., Ramkumar, S., Rechberger, H., Rombach, G., Bayliss, C., Martchek, K. J., Müller, D. B., & Liu, G. (2017). A regionally-linked, dynamic material flow modelling tool for rolled, extruded and cast aluminium products. Resources, Conservation and Recycling, 125(May), 48–69. https://doi.org/10.1016/j.resconrec.2017.05.014 And: Public Access - International Aluminium Institute. (n.d.). Retrieved March 3, 2023, from https://alucycle.world-aluminium.org/public-access/ (Public Access - International Aluminium Institute, n.d.)
    """
    return 0.144


@component.add(
    name="Al_output_economy",
    units="Mdollars_2015/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"output_real": 1},
)
def al_output_economy():
    """
    Sum Output real from economy model to check the value.
    """
    return sum(
        output_real()
        .loc[:, "MINING_AND_MANUFACTURING_ALUMINIUM"]
        .reset_coords(drop=True)
        .rename({"REGIONS_35_I": "REGIONS_35_I!"}),
        dim=["REGIONS_35_I!"],
    )


@component.add(
    name="Al_price",
    units="M$/Mt",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"al_price_exp_fit": 2, "al_market": 1},
)
def al_price():
    """
    This variable captures the relation ship of product (Aluminium) available on the market in relation to the market price. The factor is used to reproduce the observed price and extraction. Factor determined by parameterization Reference: Sverdrup, H., and Olafsdottir, A.H., 2019. Conceptualization and parameterization of the market price mechanism in the WORLD6 model for metals, materials and fossil fuels. Mineral Economics 1-26. Springer Nature DOI: 10.1007/s13563-019-00182-7
    """
    return float(al_price_exp_fit().loc["A_EXP_CURVE"]) * np.exp(
        -float(al_price_exp_fit().loc["B_EXP_CURVE"]) * al_market()
    )


@component.add(
    name="Al_price_economy",
    units="$/t",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "initial_al_price": 1,
        "al_demand": 2,
        "maximum_al_price": 1,
        "al_available_delayed": 2,
        "coefficients_al_price_economy": 3,
    },
)
def al_price_economy():
    """
    Price function to calculate the aluminium price in $/t. IF THEN ELSE(Time=2005, 2538 ,IF THEN ELSE (Al demand>Al available DELAYED, 10000 , EXP( 6.34626 +0.454773 *LN(1/(1-Al demand/Al available DELAYED ))))) New Try c b a 0.046 -0.379595007 7.666996188
    """
    return if_then_else(
        time() == 2005,
        lambda: initial_al_price(),
        lambda: if_then_else(
            al_demand() > al_available_delayed(),
            lambda: maximum_al_price(),
            lambda: np.exp(
                float(coefficients_al_price_economy().loc["A_EXP_CURVE"])
                + float(coefficients_al_price_economy().loc["B_EXP_CURVE"])
                * np.log(
                    1 / (1 - al_demand() / al_available_delayed())
                    + float(coefficients_al_price_economy().loc["C_EXP_CURVE"]) * 0.8
                )
            ),
        ),
    )


@component.add(
    name="Al_price_economy_adjusted",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "al_price_index_economy": 1},
)
def al_price_economy_adjusted():
    """
    Cu price for the first Year is set to 100 as a starting value-nominal price in the economy model. The connection with the economy model starts at the year 2015.
    """
    return if_then_else(time() <= 2015, lambda: 100, lambda: al_price_index_economy())


@component.add(
    name="Al_PRICE_EXP_FIT",
    units="M$/Mt",
    subscripts=["EXP_CURVE_FIT_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_al_price_exp_fit"},
)
def al_price_exp_fit():
    """
    The Al price was a graphical function in world 7, in WILLIAM the graphical function will be described by a exponatial function which fit the previously used graphical function. This variable captures the relation ship of product (Aluminium) available on the market in relation to the market price. The factor is used to reproduce the observed price and extraction. Factor determined by parameterization A EXP CURVE 10000 B EXP CURVE 0.42 Reference: Sverdrup, H., and Olafsdottir, A.H., 2019. Conceptualization and parameterization of the market price mechanism in the WORLD6 model for metals, materials and fossil fuels. Mineral Economics 1-26. Springer Nature DOI: 10.1007/s13563-019-00182-7
    """
    return _ext_constant_al_price_exp_fit()


_ext_constant_al_price_exp_fit = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Aluminium",
    "Al_PRICE_EXP_FIT*",
    {"EXP_CURVE_FIT_I": _subscript_dict["EXP_CURVE_FIT_I"]},
    _root,
    {"EXP_CURVE_FIT_I": _subscript_dict["EXP_CURVE_FIT_I"]},
    "_ext_constant_al_price_exp_fit",
)


@component.add(
    name="Al_PRICE_HISTORICAL",
    units="$/t",
    comp_type="Auxiliary",
    comp_subtype="with Lookup",
    depends_on={"time": 1},
)
def al_price_historical():
    """
    Look up table to test the effect of the price signal and the economy module. Source:
    """
    return np.interp(
        time(),
        [
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
        ],
        [
            1357.47,
            1348.36,
            1544.07,
            1454.49,
            1347.93,
            1423.06,
            1689.27,
            1888.77,
            2509.77,
            2655.33,
            2554.43,
            1665.77,
            2157.63,
            2392.89,
            2027.26,
            1871.12,
            1849.77,
            1710.08,
            1586.81,
            1934.05,
            2105.69,
            1813.77,
            1713.86,
            2401.72,
            2828.4,
            2400.0,
            2400.0,
        ],
    )


@component.add(
    name="Al_price_index_economy",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_mat2eco_al_price": 1,
        "price_transformation": 1,
        "al_base_price_2006": 1,
        "estimated_price_with_tax_metals": 1,
    },
)
def al_price_index_economy():
    """
    Aluminium price index, used to track the change between the price in the start zear and it's development overtime. (Cu price economy test/Cu base price 2006)*PERCENT PRICE TRANSFORMATION
    """
    return if_then_else(
        switch_mat2eco_al_price() == 0,
        lambda: 100,
        lambda: (
            float(estimated_price_with_tax_metals().loc["Al_W"]) / al_base_price_2006()
        )
        * price_transformation(),
    )


@component.add(
    name="Al_primary_share_IAI_projection",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"share_of_primary": 1},
)
def al_primary_share_iai_projection():
    return share_of_primary() / 100


@component.add(
    name="Al_profit",
    units="Mdollars/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"al_income": 1, "al_costs": 1},
)
def al_profit():
    """
    Profit from Aluminium mining.
    """
    return al_income() - al_costs()


@component.add(
    name="Al_profit_delay",
    units="DMNL",
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_al_profit_delay": 1},
    other_deps={
        "_integ_al_profit_delay": {
            "initial": {"initial_al_profit_delay": 1},
            "step": {"increase_al_profit": 1, "decrease_al_profit": 1},
        }
    },
)
def al_profit_delay():
    """
    Al profit delay This is a workaround to avoid circular error, any short time delay works. The delayed TIME STEP, is typically used in system dynamics models to avoid algebraic loops. Any short delay will do... Engine is used to filter short term disturbances in the market price that have an effect on the mining adjustment rate. The underlaying idea is that a increase in Li market price will trigger an increase in mining. The increase in mining will be triggered when the price is high or low for a longer time step. Source: Sverdrup, H. U., & Olafsdottir, A. H. (2019). On the long-term sustainability of copper, zinc and lead supply, using a system dynamics model. Resources, Conservation & Recycling: X, 4(100007). https://doi.org/https://doi.org/10.1016/j.rcrx.2019.100007 Sverdrup, H. U., Ragnarsdottir, K. V. and Koca, D. (2015) Aluminium for the future: Modelling the global production, market supply, demand, price and long term development of the global reservesâ€™, Resources, Conservation and Recycling, 103, pp. 139â€“154. doi: 10.1016/j.resconrec.2015.06.008
    """
    return _integ_al_profit_delay()


_integ_al_profit_delay = Integ(
    lambda: increase_al_profit() - decrease_al_profit(),
    lambda: initial_al_profit_delay(),
    "_integ_al_profit_delay",
)


@component.add(
    name="Al_profit_effect_on_mining",
    units="Mdollars/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "al_profit": 5,
        "coefficients_al_profit_effect_on_mining_s_curve": 3,
        "coefficients_al_profit_effect_on_mining_logistic": 2,
    },
)
def al_profit_effect_on_mining():
    """
    This function makes sure that the Aluminium mining runs when there is profit. If it becomes unprofitable, mining shuts down. Which is how the world works. The curve has a flat part: no mining at deficit, it rises sharply when passing zero. It has a gentle slope up at higher profit, reflecting that increasing up increase profitability. On the systemic level. too much production compared t demand will lower price and thus in time also profits. See also: Sverdrup, H., and Olafsdottir, A.H., 2019. Conceptualization and parameterization of the market price mechanism in the WORLD6 model for metals, materials and fossil fuels. Mineral Economics 1-26. Springer Nature DOI: 10.1007/s13563-019-00182-7.
    """
    return if_then_else(
        al_profit() < -1600,
        lambda: 0,
        lambda: if_then_else(
            np.logical_and(al_profit() < -1600, al_profit() < 0),
            lambda: float(
                coefficients_al_profit_effect_on_mining_logistic().loc[
                    "A_LINEAR_LOG_FIT"
                ]
            )
            * np.exp(
                float(
                    coefficients_al_profit_effect_on_mining_logistic().loc[
                        "B_LINEAR_LOG_FIT"
                    ]
                )
                * al_profit()
            ),
            lambda: float(
                coefficients_al_profit_effect_on_mining_s_curve().loc["A_S_CURVE_FIT"]
            )
            / (
                1
                + np.exp(
                    -float(
                        coefficients_al_profit_effect_on_mining_s_curve().loc[
                            "k_S_CURVE_FIT"
                        ]
                    )
                    * (
                        al_profit()
                        - float(
                            coefficients_al_profit_effect_on_mining_s_curve().loc[
                                "n_S_CURVE_FIT"
                            ]
                        )
                    )
                )
            ),
        ),
    )


@component.add(
    name="Al_PROFIT_SCALE",
    units="1/Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_al_profit_scale"},
)
def al_profit_scale():
    """
    Dimesionles Multiplier only used for unit consitancy.->
    """
    return _ext_constant_al_profit_scale()


_ext_constant_al_profit_scale = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Aluminium",
    "Al_PROFIT_SCALE",
    {},
    _root,
    {},
    "_ext_constant_al_profit_scale",
)


@component.add(
    name="Al_PROSPECTING",
    units="1/Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_al_prospecting"},
)
def al_prospecting():
    """
    Assumption: Represents the finding rate and effort made to find each ton of Aluminium. The value is chosen by paramitization of the model on historical data for price and extracted amounts.Fraction of the hidden resources found every year and put into known reserves. Value: 0.01
    """
    return _ext_constant_al_prospecting()


_ext_constant_al_prospecting = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Aluminium",
    "Al_PROSPECTING",
    {},
    _root,
    {},
    "_ext_constant_al_prospecting",
)


@component.add(
    name="Al_recycling_drive",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"recycling_drive_exp_fit": 3, "al_price_economy": 1},
)
def al_recycling_drive():
    """
    This variable describes the effect of of the Al price on the incentive and motivation to recycle. With a higher price the recycling drive is increasing. With a lower price the recycling drive is decreasing. The scaling is on Assumption based on the following papers: Dahmus, J. B., & Gutowski, T. G. (2007). What gets recycled: an information theory based model for product recycling. Environmental Science & Technology, 41(23), 7543-7550. Gutowski, T.G., Wolf, M.L., Dahmus, J.B., Albino, D.C., 2008. Analaysis of recycling sys- tems. Knoxville, Tennessee. Proceedinc Ìgs of the 2008 NSF Engineering and Research and Innovation Conference8 pages. Gutowski, T.G., Sahni, S., Allwood, M., Ashby, M.F., Worrell, E., 2016. The energy re- quired to produce materials: constraints on energy-intensity improvements, parame- ters of demand. Philos. Trans. Math. Phys. Eng. Sci. 371, 20120003https://doi.org/ 10.1098/rsta.2012.0003.
    """
    return (
        1
        / float(recycling_drive_exp_fit().loc["B_EXP_CURVE"])
        * np.exp(
            (float(recycling_drive_exp_fit().loc["A_EXP_CURVE"]) + al_price_economy())
            / float(recycling_drive_exp_fit().loc["B_EXP_CURVE"])
        )
    )


@component.add(
    name="Al_recycling_drive_scaling",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"al_recycling_drive": 1, "al_recycling_scaling_factor": 1},
)
def al_recycling_drive_scaling():
    return al_recycling_drive() * al_recycling_scaling_factor()


@component.add(
    name="Al_RECYCLING_RATE",
    units="1/Year",
    comp_type="Constant",
    comp_subtype="Normal",
)
def al_recycling_rate():
    """
    The recycling rate is set to be a fraction of 0,6 and is based on the following sources (see below).It implies that the aluminium stays as scrap for 1.6 years from coming into the waste stream somewhere in the World, then is collected and sorted, transported to a smelter,before it comes out as lost or new, recycled material. This is not the actual recycling rate in the system, Since it is also influenced by the price. GET DIRECT CONSTANTS('model_parameters/materials/materials.xlsx', 'Aluminium', 'Al_RECYCLING_RATE') Source: Dahmus, J. B., & Gutowski, T. G. (2007). What gets recycled: an information theory based model for product recycling. Environmental Science & Technology, 41(23), 7543-7550. Graedel, T. E., Buckert, M., & Reck, B. K. (2011). Assessing mineral resources in society: Metal stocks and recycling rates. United Nations Environment Programme. ISBN 978-92-807-3182-0 Parameter Estimation Based on : (Bertram et al., 2017)Bertram, M., Ramkumar, S., Rechberger, H., Rombach, G., Bayliss, C., Martchek, K. J., Müller, D. B., & Liu, G. (2017). A regionally-linked, dynamic material flow modelling tool for rolled, extruded and cast aluminium products. Resources, Conservation and Recycling, 125(May), 48–69. https://doi.org/10.1016/j.resconrec.2017.05.014 And: Public Access - International Aluminium Institute. (n.d.). Retrieved March 3, 2023, from https://alucycle.world-aluminium.org/public-access/ (Public Access - International Aluminium Institute, n.d.)
    """
    return 1.2


@component.add(
    name="Al_RECYCLING_SCALING_FACTOR", comp_type="Constant", comp_subtype="Normal"
)
def al_recycling_scaling_factor():
    return 12


@component.add(
    name="Al_SCRAP_LOSS", units="1/Year", comp_type="Constant", comp_subtype="Normal"
)
def al_scrap_loss():
    """
    This assumes that 5% of the scrap is lost in the scrap heap, through slag, wear and corrosion. value= 0.05 GET DIRECT CONSTANTS('model_parameters/materials/materials.xlsx', 'Aluminium', 'Al_SCRAP_LOSS') Parameter Estimation Based on : (Bertram et al., 2017)Bertram, M., Ramkumar, S., Rechberger, H., Rombach, G., Bayliss, C., Martchek, K. J., Müller, D. B., & Liu, G. (2017). A regionally-linked, dynamic material flow modelling tool for rolled, extruded and cast aluminium products. Resources, Conservation and Recycling, 125(May), 48–69. https://doi.org/10.1016/j.resconrec.2017.05.014 And: Public Access - International Aluminium Institute. (n.d.). Retrieved March 3, 2023, from https://alucycle.world-aluminium.org/public-access/ (Public Access - International Aluminium Institute, n.d.)
    """
    return 0.29


@component.add(
    name="Al_scrapped_metal",
    units="Mt",
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_al_scrapped_metal": 1},
    other_deps={
        "_integ_al_scrapped_metal": {
            "initial": {"initial_al_scrapped_metal": 1},
            "step": {
                "increase_al_scrapped_metal": 1,
                "decrease_al_scrapped_metal_loss": 1,
                "decrease_al_scrapped_metal_recycling": 1,
            },
        }
    },
)
def al_scrapped_metal():
    """
    World 7 name was Al scrapped metal , The initial values for the Al scrapped metal is based on simulation outputs from the World 7 for the year 2005. The World 7 outputs are based on initial values from 1850. Source: Sverdrup, H. U., Ragnarsdottir, K. V., & Koca, D. (2015). Aluminium for the future: Modelling the global production, market supply, demand, price and long term development of the global reserves. Resources, Conservation and Recycling, 103, 139-154. doi:10.1016/j.resconrec.2015.06.008. The article you mentioned, "Aluminum for the Future: Modelling the Global Production, Market Supply, Demand, Price and Long-Term Development of the Global Reserves," was published in the journal Resources, Conservation and Recycling in 2015. The authors of the article are H.U. Sverdrup, K.V. Ragnarsdottir, and D. Koca. The article discusses the use of modeling to analyze the global production, market supply, demand, price, and long-term development of aluminum reserves. The authors conclude that aluminum will continue to be an important resource in the future, and that efficient management of global reserves will be essential to ensure its continued availability.
    """
    return _integ_al_scrapped_metal()


_integ_al_scrapped_metal = Integ(
    lambda: increase_al_scrapped_metal()
    - decrease_al_scrapped_metal_loss()
    - decrease_al_scrapped_metal_recycling(),
    lambda: initial_al_scrapped_metal(),
    "_integ_al_scrapped_metal",
)


@component.add(
    name="Al_SCRAPPING_RATE",
    units="1/Year",
    comp_type="Constant",
    comp_subtype="Normal",
)
def al_scrapping_rate():
    """
    The rate of stocks in use imply that we assume that aluminium stay 30 years in use on the average before it is taken out as scrap. Value: 0.03 GET DIRECT CONSTANTS('model_parameters/materials/materials.xlsx', 'Aluminium', 'Al_SCRAPPING_RATE') 0.0165
    """
    return 0.025


@component.add(
    name="Al_secondary_share_IAI_projection",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"share_of_secondary": 1},
)
def al_secondary_share_iai_projection():
    return share_of_secondary() / 100


@component.add(
    name="Al_share_of_secondary_material",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "decrease_al_scrapped_metal_recycling": 1,
        "al_new_scrap": 1,
        "al_market_supply": 1,
    },
)
def al_share_of_secondary_material():
    """
    Share of secondary material used to produce new copper to be sold on the market.
    """
    return zidz(
        decrease_al_scrapped_metal_recycling() + al_new_scrap(), al_market_supply()
    )


@component.add(
    name="Al_SOCIETY_LOSS_RATE",
    units="1/Year",
    comp_type="Constant",
    comp_subtype="Normal",
)
def al_society_loss_rate():
    """
    Assumption that 2% of the stocks in use are lost diffusively thorough neglectance, wear and corrosion. Probably a low estimate, but we have to start somewhere. value: 0.02 GET DIRECT CONSTANTS('model_parameters/materials/materials.xlsx', 'Aluminium', 'Al_SOCIETY_LOSS_RATE') 0.009
    """
    return 0


@component.add(
    name="Al_stocks_in_use",
    units="Mt",
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_al_stocks_in_use": 1},
    other_deps={
        "_integ_al_stocks_in_use": {
            "initial": {"initial_al_use": 1},
            "step": {
                "increase_al_stock_in_use": 1,
                "decrease_al_stock_in_use_loss": 1,
                "decrease_stock_in_use_scrap": 1,
            },
        }
    },
)
def al_stocks_in_use():
    """
    This is all aluminium in use in society. Aluminium that is used in products, building and other things and providing service to society.
    """
    return _integ_al_stocks_in_use()


_integ_al_stocks_in_use = Integ(
    lambda: increase_al_stock_in_use()
    - decrease_al_stock_in_use_loss()
    - decrease_stock_in_use_scrap(),
    lambda: initial_al_use(),
    "_integ_al_stocks_in_use",
)


@component.add(
    name="Al_water_per_recycle",
    units="MtW/Mt",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "imv_al_mining_water_use_efficiency": 1,
        "coefficient_al_water_per_recycling": 1,
    },
)
def al_water_per_recycle():
    """
    Alumiunium water use for aluminium recycling.
    """
    return imv_al_mining_water_use_efficiency() * coefficient_al_water_per_recycling()


@component.add(
    name="Al_water_use_all",
    units="MtW/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"al_water_use_for_ore_extraction": 1, "al_water_use_recycle": 1},
)
def al_water_use_all():
    """
    Total water use for the extraction and production of Aluminium from Ore and from recycled Aluminium.
    """
    return al_water_use_for_ore_extraction() + al_water_use_recycle()


@component.add(
    name="Al_water_use_for_ore_extraction",
    units="MtW/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"al_water_use_per_per_ore_grade": 2},
)
def al_water_use_for_ore_extraction():
    """
    Total use of water for Aluminium extraction and production from HIGH ORE GRADE and LOW ORE GRADE.
    """
    return float(al_water_use_per_per_ore_grade().loc["HIGH_GRADE"]) + float(
        al_water_use_per_per_ore_grade().loc["LOW_GRADE"]
    )


@component.add(
    name="Al_WATER_USE_PER_ORE_GRADE",
    units="MtW/Mt",
    subscripts=["Al_ORE_GRADES_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_al_water_use_per_ore_grade"},
)
def al_water_use_per_ore_grade():
    """
    Our own estimates of water use per grade extraction, based on a large literature survey. See the separate report for documentation of setting the value and where the information came from. Low grade 44 MtW/Mt High grade 22 MtW/Mt Sverdrup and Olafsdottir 2021: Assessing the global energy and water use from of metals, materials and fossil fuels extraction and production.Internal report for LOCOMOTION WP7.44pp
    """
    return _ext_constant_al_water_use_per_ore_grade()


_ext_constant_al_water_use_per_ore_grade = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Aluminium",
    "Al_WATER_USE_PER_ORE_GRADE*",
    {"Al_ORE_GRADES_I": _subscript_dict["Al_ORE_GRADES_I"]},
    _root,
    {"Al_ORE_GRADES_I": _subscript_dict["Al_ORE_GRADES_I"]},
    "_ext_constant_al_water_use_per_ore_grade",
)


@component.add(
    name="Al_water_use_per_per_ore_grade",
    units="MtW/Year",
    subscripts=["Al_ORE_GRADES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "al_water_use_per_ore_grade": 2,
        "imv_al_mining_water_use_efficiency": 2,
        "mining_al_known_reserves": 2,
    },
)
def al_water_use_per_per_ore_grade():
    """
    Waterusage per ore grade calculated.
    """
    value = xr.DataArray(
        np.nan,
        {"Al_ORE_GRADES_I": _subscript_dict["Al_ORE_GRADES_I"]},
        ["Al_ORE_GRADES_I"],
    )
    value.loc[["HIGH_GRADE"]] = (
        float(al_water_use_per_ore_grade().loc["HIGH_GRADE"])
        * imv_al_mining_water_use_efficiency()
    ) * float(mining_al_known_reserves().loc["HIGH_GRADE"])
    value.loc[["LOW_GRADE"]] = (
        float(al_water_use_per_ore_grade().loc["LOW_GRADE"])
        * imv_al_mining_water_use_efficiency()
    ) * float(mining_al_known_reserves().loc["LOW_GRADE"])
    return value


@component.add(
    name="Al_water_use_recycle",
    units="MtW/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"decrease_al_scrapped_metal_recycling": 1, "al_water_per_recycle": 1},
)
def al_water_use_recycle():
    """
    Water use for the production of recycled Aluminium.
    """
    return decrease_al_scrapped_metal_recycling() * al_water_per_recycle()


@component.add(
    name="change_Al_mining_technology_S_curve",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"coefficients_change_al_mining_technology_s_curve": 3, "time": 1},
)
def change_al_mining_technology_s_curve():
    """
    Assumption: The "S Curve" innovation thinking is attributed to Richard Foster (1986) and made famous by Clayton Christensen in the book "Innovator's Dilemma," where he discusses how each successive computer hard drive industry was disrupted. Each of these S curves represents a technology platform. Movement up an "S" curve represents incremental innovation, while stepping down to a lower new "S" curve may lead to radical innovation as the new "S" curve surpasses the existing one. There is a risk that the lower "S" curve does not improve. As, U. S. T., Stephen, A. G., & Novel, K. (1995). Jumping the technology S-curve. IEEE SPECTRUM, 49-54. As, Al Mining technology: Now Al prospecting technology Increase in Al prospecting technology can be explained with the corresponding improvement of technology in prospecting due to the increase in interest and experience prospecting of Al. Reference: Sverdrup, H. U., Ragnarsdottir, K. V. and Koca, D. (2015) Aluminium for the future: Modelling the global production, market supply, demand, price and long term development of the global reservesâ€™, Resources, Conservation and Recycling, 103, pp. 139â€“154. doi: 10.1016/j.resconrec.2015.06.008. Sverdrup, H. U., Ragnarsdottir, K. V. and Koca, D. (2014) â€˜On modelling the global copper mining rates, market supply, copper price and the end of copper reservesâ€™, Resources, Conservation and Recycling, 87, pp. 158â€“174. doi: 10.1016/j. Sverdrup, H. U., Olafsdottir, A. H. and Ragnarsdottir, K. V. (2019) â€˜On the long-term sustainability of copper, zinc and lead supply, using a system dynamics modelâ€™, Resources, Conservation and Recycling: X, 4, p. 100007. doi: 10.1016/j.rcrx.2019.100007.resconrec.2014.03.007.
    """
    return float(
        coefficients_change_al_mining_technology_s_curve().loc["A_S_CURVE_FIT"]
    ) / (
        1
        + np.exp(
            -float(
                coefficients_change_al_mining_technology_s_curve().loc["k_S_CURVE_FIT"]
            )
            * (
                time()
                - float(
                    coefficients_change_al_mining_technology_s_curve().loc[
                        "n_S_CURVE_FIT"
                    ]
                )
            )
        )
    )


@component.add(
    name="COEFFICIENTS_Al_PRICE_ECONOMY",
    subscripts=["EXP_CURVE_FIT_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_coefficients_al_price_economy"},
)
def coefficients_al_price_economy():
    """
    Coefficients used to calculate the Al price. parameter derived from efforts made to match the historical price has much a possible.
    """
    return _ext_constant_coefficients_al_price_economy()


_ext_constant_coefficients_al_price_economy = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Aluminium",
    "COEFFICIENTS_Al_PRICE_ECONOMY*",
    {"EXP_CURVE_FIT_I": _subscript_dict["EXP_CURVE_FIT_I"]},
    _root,
    {"EXP_CURVE_FIT_I": _subscript_dict["EXP_CURVE_FIT_I"]},
    "_ext_constant_coefficients_al_price_economy",
)


@component.add(
    name="COEFFICIENTS_Al_PRODUCTION_RATE_FACTOR",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_coefficients_al_production_rate_factor"},
)
def coefficients_al_production_rate_factor():
    """
    Assumption: Scaling Factor to get a good fit with the historical data for extraction and price. These numbers give the best fit to the historical data and therefore they are assumptions based parametersation of the Al production rate. 0,005 -> 0,008--> 0.010 0.005
    """
    return _ext_constant_coefficients_al_production_rate_factor()


_ext_constant_coefficients_al_production_rate_factor = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Aluminium",
    "COEFFICIENTS_Al_PRODUCTION_RATE_FACTOR",
    {},
    _root,
    {},
    "_ext_constant_coefficients_al_production_rate_factor",
)


@component.add(
    name="COEFFICIENTS_Al_PROFIT_EFFECT_ON_MINING_LOGISTIC",
    units="DMNL",
    subscripts=["LINEAR_LOG_FIT_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_coefficients_al_profit_effect_on_mining_logistic"
    },
)
def coefficients_al_profit_effect_on_mining_logistic():
    """
    This function makes sure that the Aluminium mining runs when there is profit. If it becomes unprofitable, mining shuts down. Which is how the world works. The curve has a flat part: no mining at deficit, it rises sharply when passing zero. It has a gentle slope up at higher profit, reflecting that increasing up increase profitability. A LINEAR LOG FIT = 0.1409 B LINEAR LOG FIT = 0.0002 On the systemic level. too much production compared t demand will lower price and thus in time also profits. See also: Sverdrup, H., and Olafsdottir, A.H., 2019. Conceptualization and parameterization of the market price mechanism in the WORLD6 model for metals, materials and fossil fuels. Mineral Economics 1-26. Springer Nature DOI: 10.1007/s13563-019-00182-7
    """
    return _ext_constant_coefficients_al_profit_effect_on_mining_logistic()


_ext_constant_coefficients_al_profit_effect_on_mining_logistic = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Aluminium",
    "COEFFICIENTS_Al_PROFIT_EFFECT_ON_MINING_LOGISTIC*",
    {"LINEAR_LOG_FIT_I": _subscript_dict["LINEAR_LOG_FIT_I"]},
    _root,
    {"LINEAR_LOG_FIT_I": _subscript_dict["LINEAR_LOG_FIT_I"]},
    "_ext_constant_coefficients_al_profit_effect_on_mining_logistic",
)


@component.add(
    name="COEFFICIENTS_Al_PROFIT_EFFECT_ON_MINING_S_CURVE",
    units="DMNL",
    subscripts=["S_CURVE_FIT_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_coefficients_al_profit_effect_on_mining_s_curve"
    },
)
def coefficients_al_profit_effect_on_mining_s_curve():
    """
    This function makes sure that the Aluminium mining runs when there is profit. If it becomes unprofitable, mining shuts down. Which is how the world works. The curve has a flat part: no mining at deficit, it rises sharply when passing zero. It has a gentle slope up at higher profit, reflecting that increasing up increase profitability. A S CURVE FIT 5.3 k S CURVE FIT 1e-05 n S CURVE FIT 100000 On the systemic level. too much production compared t demand will lower price and thus in time also profits. See also: Sverdrup, H., and Olafsdottir, A.H., 2019. Conceptualization and parameterization of the market price mechanism in the WORLD6 model for metals, materials and fossil fuels. Mineral Economics 1-26. Springer Nature DOI: 10.1007/s13563-019-00182-7 a=1,258193e+00 b=1,292795e-04 c=5,268404e+03
    """
    return _ext_constant_coefficients_al_profit_effect_on_mining_s_curve()


_ext_constant_coefficients_al_profit_effect_on_mining_s_curve = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Aluminium",
    "COEFFICIENTS_Al_PROFIT_EFFECT_ON_MINING_S_CURVE*",
    {"S_CURVE_FIT_I": _subscript_dict["S_CURVE_FIT_I"]},
    _root,
    {"S_CURVE_FIT_I": _subscript_dict["S_CURVE_FIT_I"]},
    "_ext_constant_coefficients_al_profit_effect_on_mining_s_curve",
)


@component.add(
    name="COEFFICIENTS_CHANGE_Al_GRADE",
    units="DMNL",
    subscripts=["S_CURVE_FIT_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_coefficients_change_al_grade"},
)
def coefficients_change_al_grade():
    """
    S Curve fit from the curve origanating from the World 7 model. With higher price it is more likely that Lower grade Aluminium is getting exctracted. A S CURVE FIT = 1 k S CURVE FIT = 1e-12 n S CURVE FIT = 3.61 Sverdrup, H. U., Ragnarsdottir, K. V. and Koca, D. (2015) Aluminium for the future: Modelling the global production, market supply, demand, price and long term development of the global reservesâ€™, Resources, Conservation and Recycling, 103, pp. 139â€“154. doi: 10.1016/j.resconrec.2015.06.008. Harald Sverdrup, 2021: LOCOMOTION Project report: Estimating the cost of extraction and the price required for changing between mining of different ore grades in the WORLD7 model. 20 pp.
    """
    return _ext_constant_coefficients_change_al_grade()


_ext_constant_coefficients_change_al_grade = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Aluminium",
    "COEFFICIENTS_CHANGE_Al_GRADE*",
    {"S_CURVE_FIT_I": _subscript_dict["S_CURVE_FIT_I"]},
    _root,
    {"S_CURVE_FIT_I": _subscript_dict["S_CURVE_FIT_I"]},
    "_ext_constant_coefficients_change_al_grade",
)


@component.add(
    name="COEFFICIENTS_CHANGE_Al_MINING_TECHNOLOGY_S_CURVE",
    units="DMNL",
    subscripts=["S_CURVE_FIT_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_coefficients_change_al_mining_technology_s_curve"
    },
)
def coefficients_change_al_mining_technology_s_curve():
    """
    S curve fit originating from World 7. The S Curve innovation thinking is attributed to Richard Foster (1986) and made famous by Clayton Christensen in the book ân Innovators Dilemma, where he discusses how each successive computer hard drive industry got wiped out. Each of these S curves represent a technology platform. Movement up an S curve is incremental innovation while stepping down on a lower new Scurve now, may lead to radical innovation, as the new S curve surpasses your existing S curve. There is a risk that the lower S curve does not get better. As, U. S. T., Stephen, A. G., & Novel, K. (1995). Jumping the technology S-curve. IEEE SPECTRUM, 49â€“54.
    """
    return _ext_constant_coefficients_change_al_mining_technology_s_curve()


_ext_constant_coefficients_change_al_mining_technology_s_curve = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Aluminium",
    "COEFFICIENTS_CHANGE_Al_MINING_TECHNOLOGY_S_CURVE*",
    {"S_CURVE_FIT_I": _subscript_dict["S_CURVE_FIT_I"]},
    _root,
    {"S_CURVE_FIT_I": _subscript_dict["S_CURVE_FIT_I"]},
    "_ext_constant_coefficients_change_al_mining_technology_s_curve",
)


@component.add(
    name="decrease_Al_profit",
    units="1/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"al_profit_delay": 1, "decrease_faktor_al_profit": 1},
)
def decrease_al_profit():
    """
    decrease Al profit With a higher profit more money will be invested in mining-here the mining coefficient is rising. The Stock and flow structure is used to avoid circular error and simultanous.. This is a workaround to avoid circular error, any short time delay works. The delayed TIME STEP, is typically used in system dynamics models to avoid algebraic loops. Any short delay will do... Engine is used to filter short term disturbances in the market price that have an effect on the mining adjustment rate. The underlaying idea is that a increase in Li market price will trigger an increase in mining. The increase in mining will be triggered when the price is high or low for a longer time step. Source: Sverdrup, H. U., & Olafsdottir, A. H. (2019). On the long-term sustainability of copper, zinc and lead supply, using a system dynamics model. Resources, Conservation & Recycling: X, 4(100007). https://doi.org/https://doi.org/10.1016/j.rcrx.2019.100007 Sverdrup, H. U., Ragnarsdottir, K. V. and Koca, D. (2015) Aluminium for the future: Modelling the global production, market supply, demand, price and long term development of the global reservesâ€™, Resources, Conservation and Recycling, 103, pp. 139â€“154. doi: 10.1016/j.resconrec.2015.06.008
    """
    return al_profit_delay() * decrease_faktor_al_profit()


@component.add(
    name="decrease_Al_scrapped_metal_loss",
    units="Mt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_al_recycling_policy": 1,
        "al_eol_recycling_rate_sp": 1,
        "al_scrapped_metal": 2,
        "al_recycling_drive_scaling": 1,
    },
)
def decrease_al_scrapped_metal_loss():
    """
    Parameter Estimation Based on : (Bertram et al., 2017)Bertram, M., Ramkumar, S., Rechberger, H., Rombach, G., Bayliss, C., Martchek, K. J., Müller, D. B., & Liu, G. (2017). A regionally-linked, dynamic material flow modelling tool for rolled, extruded and cast aluminium products. Resources, Conservation and Recycling, 125(May), 48–69. https://doi.org/10.1016/j.resconrec.2017.05.014 And: Public Access - International Aluminium Institute. (n.d.). Retrieved March 3, 2023, from https://alucycle.world-aluminium.org/public-access/ (Public Access - International Aluminium Institute, n.d.) "This assumes that 5% of the scrap in the stock is lost in the scrap heap, through slag, wear and corrosion." old must be deleted
    """
    return if_then_else(
        switch_al_recycling_policy() == 1,
        lambda: al_scrapped_metal() * (1 - al_eol_recycling_rate_sp()),
        lambda: al_scrapped_metal() * (1 - al_recycling_drive_scaling()),
    )


@component.add(
    name="decrease_Al_scrapped_metal_recycling",
    units="Mt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_al_recycling_policy": 1,
        "al_eol_recycling_rate_sp": 1,
        "al_scrapped_metal": 2,
        "al_recycling_drive_scaling": 1,
    },
)
def decrease_al_scrapped_metal_recycling():
    """
    Amount of aluminium recycled, depending on the amount of Aluminium available that is available in the Al scrap stock, The price and the Al recycling rate.
    """
    return if_then_else(
        switch_al_recycling_policy() == 1,
        lambda: al_eol_recycling_rate_sp() * al_scrapped_metal(),
        lambda: al_scrapped_metal() * al_recycling_drive_scaling(),
    )


@component.add(
    name="decrease_Al_stock_in_use_loss",
    units="Mt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"al_stocks_in_use": 1, "al_society_loss_rate": 1},
)
def decrease_al_stock_in_use_loss():
    """
    Assumption that 2% of the stocks in use are lost diffusively thorough neglectance, wear and corrosion. Probably a low estimate, but we have to start somewhere.
    """
    return al_stocks_in_use() * al_society_loss_rate()


@component.add(
    name="DECREASE_FAKTOR_Al_PROFIT",
    units="1/Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_decrease_faktor_al_profit"},
)
def decrease_faktor_al_profit():
    """
    The fraction of 0,2 is used to create a delay and to filter out short term disturbances of the market price that in reality do not have any effect on the Al production rate. also tried 0.05 now 0.2
    """
    return _ext_constant_decrease_faktor_al_profit()


_ext_constant_decrease_faktor_al_profit = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Aluminium",
    "DECREASE_FACTOR_Al_PROFIT",
    {},
    _root,
    {},
    "_ext_constant_decrease_faktor_al_profit",
)


@component.add(
    name="decrease_stock_in_use_scrap",
    units="Mt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"al_stocks_in_use": 1, "al_scrapping_rate": 1},
)
def decrease_stock_in_use_scrap():
    """
    Aluminium that is leaving the Aluminium stock in use to go to recycling. Al stocks in use*Al SCRAPPING RATE+increase Al stock in use*(1-Al MATERIAL YIELD IN MANUFACTURE)
    """
    return al_stocks_in_use() * al_scrapping_rate()


@component.add(
    name="delayed_TS_Al_price_economy_adjusted",
    units="DMNL",
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_al_price_economy_adjusted": 1},
    other_deps={
        "_delayfixed_delayed_ts_al_price_economy_adjusted": {
            "initial": {"time_step": 1},
            "step": {"al_price_economy_adjusted": 1},
        }
    },
)
def delayed_ts_al_price_economy_adjusted():
    """
    Delayed aluminium price economy adjusted.
    """
    return _delayfixed_delayed_ts_al_price_economy_adjusted()


_delayfixed_delayed_ts_al_price_economy_adjusted = DelayFixed(
    lambda: al_price_economy_adjusted(),
    lambda: time_step(),
    lambda: 100,
    time_step,
    "_delayfixed_delayed_ts_al_price_economy_adjusted",
)


@component.add(
    name="energy_use_in_oil_equivalents",
    units="Mt*OE/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"al_energy_use": 1, "energy_use_in_oil_equivalents_scale": 1},
)
def energy_use_in_oil_equivalents():
    """
    Energy use in Oil Equivalents.
    """
    return al_energy_use() * energy_use_in_oil_equivalents_scale()


@component.add(
    name="ENERGY_USE_IN_OIL_EQUIVALENTS_SCALE",
    units="Mt*OE/TJ",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_energy_use_in_oil_equivalents_scale"},
)
def energy_use_in_oil_equivalents_scale():
    """
    Our own estimates of water use per grade extraction, based on a large literature survey. See the separate report for documentation of setting the value and where the information came from. ENERGY USE IN OIL EQUIVALENTS SCALE =2.388e-05 Mt*OE/TJ Sverdrup and Olafsdottir 2021: Assessing the global energy and water use from of metals, materials and fossil fuels extraction and production. Internal report for LOCOMOTION WP7. 44pp
    """
    return _ext_constant_energy_use_in_oil_equivalents_scale()


_ext_constant_energy_use_in_oil_equivalents_scale = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Aluminium",
    "ENERGY_USE_IN_OIL_EQUIVALENTS_SCALE",
    {},
    _root,
    {},
    "_ext_constant_energy_use_in_oil_equivalents_scale",
)


@component.add(
    name="Energy_use_per_supplied_aluminium_unit",
    units="Mt*OE/Mt",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"energy_use_in_oil_equivalents": 1, "al_market_sales": 1},
)
def energy_use_per_supplied_aluminium_unit():
    """
    Energy used per supplied unit of Aluminium.
    """
    return energy_use_in_oil_equivalents() / (al_market_sales() + 0.0001)


@component.add(
    name="HISTORICAL_Al_PRICE",
    units="$/t",
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_historical_al_price",
        "__data__": "_ext_data_historical_al_price",
        "time": 1,
    },
)
def historical_al_price():
    """
    Historical Aluminium Price from Indixmundi- average over each year.
    """
    return _ext_data_historical_al_price(time())


_ext_data_historical_al_price = ExtData(
    "model_parameters/materials/materials.xlsx",
    "Aluminium",
    "TIME_SERIES_Al",
    "HISTORICAL_Al_PRICE",
    "interpolate",
    {},
    _root,
    {},
    "_ext_data_historical_al_price",
)


@component.add(
    name="IMPLICIT_PRICE_Al",
    units="Mdollars_2015/Mt",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "initial_output_real_materials": 2,
        "al_demand_historical_world_7": 1,
        "al_demand_base_year": 1,
    },
)
def implicit_price_al():
    """
    Implicit price is used to translate the monetary units from the economic module to physical units in the Materieals module-each materials has a different implicit price to match the demand from 2015. 584.78 implicit price Al
    """
    return if_then_else(
        time() < 2015,
        lambda: sum(
            initial_output_real_materials()
            .loc[:, "MINING_AND_MANUFACTURING_ALUMINIUM"]
            .reset_coords(drop=True)
            .rename({"REGIONS_35_I": "REGIONS_35_I!"}),
            dim=["REGIONS_35_I!"],
        )
        / al_demand_historical_world_7(),
        lambda: sum(
            initial_output_real_materials()
            .loc[:, "MINING_AND_MANUFACTURING_ALUMINIUM"]
            .reset_coords(drop=True)
            .rename({"REGIONS_35_I": "REGIONS_35_I!"}),
            dim=["REGIONS_35_I!"],
        )
        / al_demand_base_year(),
    )


@component.add(
    name="IMV_Al_ENERGY_EFFICIENCY",
    units="Years",
    comp_type="Auxiliary",
    comp_subtype="with Lookup",
    depends_on={"time": 1},
)
def imv_al_energy_efficiency():
    """
    Aluminium Energy Efficiency- S-Curve technological improvement of the Energy efficiency overtime due technological improvements.
    """
    return np.interp(
        time(),
        [
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
            2101.0,
            2102.0,
            2103.0,
            2104.0,
            2105.0,
            2106.0,
            2107.0,
            2108.0,
            2109.0,
            2110.0,
            2111.0,
            2112.0,
            2113.0,
            2114.0,
            2115.0,
            2116.0,
            2117.0,
            2118.0,
            2119.0,
            2120.0,
            2121.0,
            2122.0,
            2123.0,
            2124.0,
            2125.0,
            2126.0,
            2127.0,
            2128.0,
            2129.0,
            2130.0,
            2131.0,
            2132.0,
            2133.0,
            2134.0,
            2135.0,
            2136.0,
            2137.0,
            2138.0,
            2139.0,
            2140.0,
            2141.0,
            2142.0,
            2143.0,
            2144.0,
            2145.0,
            2146.0,
            2147.0,
            2148.0,
            2149.0,
            2150.0,
            2151.0,
            2152.0,
            2153.0,
            2154.0,
            2155.0,
            2156.0,
            2157.0,
            2158.0,
            2159.0,
            2160.0,
            2161.0,
            2162.0,
            2163.0,
            2164.0,
            2165.0,
            2166.0,
            2167.0,
            2168.0,
            2169.0,
            2170.0,
            2171.0,
            2172.0,
            2173.0,
            2174.0,
            2175.0,
            2176.0,
            2177.0,
            2178.0,
            2179.0,
            2180.0,
            2181.0,
            2182.0,
            2183.0,
            2184.0,
            2185.0,
            2186.0,
            2187.0,
            2188.0,
            2189.0,
            2190.0,
            2191.0,
            2192.0,
            2193.0,
            2194.0,
            2195.0,
            2196.0,
            2197.0,
            2198.0,
            2199.0,
            2200.0,
            2201.0,
            2202.0,
            2203.0,
            2204.0,
            2205.0,
            2206.0,
            2207.0,
            2208.0,
            2209.0,
            2210.0,
            2211.0,
            2212.0,
            2213.0,
            2214.0,
            2215.0,
            2216.0,
            2217.0,
            2218.0,
            2219.0,
            2220.0,
            2221.0,
            2222.0,
            2223.0,
            2224.0,
            2225.0,
            2226.0,
            2227.0,
            2228.0,
            2229.0,
            2230.0,
            2231.0,
            2232.0,
            2233.0,
            2234.0,
            2235.0,
            2236.0,
            2237.0,
            2238.0,
            2239.0,
            2240.0,
            2241.0,
            2242.0,
            2243.0,
            2244.0,
            2245.0,
            2246.0,
            2247.0,
            2248.0,
            2249.0,
            2250.0,
            2251.0,
            2252.0,
            2253.0,
            2254.0,
            2255.0,
            2256.0,
            2257.0,
            2258.0,
            2259.0,
            2260.0,
            2261.0,
            2262.0,
            2263.0,
            2264.0,
            2265.0,
            2266.0,
            2267.0,
            2268.0,
            2269.0,
            2270.0,
            2271.0,
            2272.0,
            2273.0,
            2274.0,
            2275.0,
            2276.0,
            2277.0,
            2278.0,
            2279.0,
            2280.0,
            2281.0,
            2282.0,
            2283.0,
            2284.0,
            2285.0,
            2286.0,
            2287.0,
            2288.0,
            2289.0,
            2290.0,
            2291.0,
            2292.0,
            2293.0,
            2294.0,
            2295.0,
            2296.0,
            2297.0,
            2298.0,
            2299.0,
            2300.0,
            2301.0,
            2302.0,
            2303.0,
            2304.0,
            2305.0,
            2306.0,
            2307.0,
            2308.0,
            2309.0,
            2310.0,
            2311.0,
            2312.0,
            2313.0,
            2314.0,
            2315.0,
            2316.0,
            2317.0,
            2318.0,
            2319.0,
            2320.0,
            2321.0,
            2322.0,
            2323.0,
            2324.0,
            2325.0,
            2326.0,
            2327.0,
            2328.0,
            2329.0,
            2330.0,
            2331.0,
            2332.0,
            2333.0,
            2334.0,
            2335.0,
            2336.0,
            2337.0,
            2338.0,
            2339.0,
            2340.0,
            2341.0,
            2342.0,
            2343.0,
            2344.0,
            2345.0,
            2346.0,
            2347.0,
            2348.0,
            2349.0,
            2350.0,
            2351.0,
            2352.0,
            2353.0,
            2354.0,
            2355.0,
            2356.0,
            2357.0,
            2358.0,
            2359.0,
            2360.0,
            2361.0,
            2362.0,
            2363.0,
            2364.0,
            2365.0,
            2366.0,
            2367.0,
            2368.0,
            2369.0,
            2370.0,
            2371.0,
            2372.0,
            2373.0,
            2374.0,
            2375.0,
            2376.0,
            2377.0,
            2378.0,
            2379.0,
            2380.0,
            2381.0,
            2382.0,
            2383.0,
            2384.0,
            2385.0,
            2386.0,
            2387.0,
            2388.0,
            2389.0,
            2390.0,
            2391.0,
            2392.0,
            2393.0,
            2394.0,
            2395.0,
            2396.0,
            2397.0,
            2398.0,
            2399.0,
            2400.0,
        ],
        [
            0.566,
            0.57,
            0.57,
            0.572,
            0.574,
            0.574,
            0.579,
            0.581,
            0.585,
            0.587,
            0.589,
            0.591,
            0.591,
            0.593,
            0.595,
            0.597,
            0.601,
            0.603,
            0.605,
            0.61,
            0.612,
            0.614,
            0.616,
            0.62,
            0.622,
            0.626,
            0.63,
            0.632,
            0.636,
            0.643,
            0.645,
            0.653,
            0.655,
            0.659,
            0.663,
            0.665,
            0.671,
            0.678,
            0.684,
            0.69,
            0.696,
            0.702,
            0.709,
            0.713,
            0.719,
            0.726,
            0.729,
            0.736,
            0.742,
            0.75,
            0.756,
            0.767,
            0.771,
            0.779,
            0.785,
            0.793,
            0.802,
            0.806,
            0.812,
            0.82,
            0.824,
            0.833,
            0.839,
            0.843,
            0.845,
            0.855,
            0.857,
            0.866,
            0.872,
            0.884,
            0.89,
            0.895,
            0.901,
            0.905,
            0.913,
            0.915,
            0.919,
            0.926,
            0.93,
            0.934,
            0.942,
            0.946,
            0.948,
            0.952,
            0.955,
            0.957,
            0.961,
            0.963,
            0.965,
            0.969,
            0.971,
            0.975,
            0.977,
            0.979,
            0.981,
            0.983,
            0.986,
            0.988,
            0.99,
            0.992,
            0.994,
            0.994,
            0.996,
            0.996,
            0.998,
            0.998,
            0.998,
            0.998,
            0.998,
            0.998,
            0.998,
            0.998,
            0.998,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
        ],
    )


@component.add(
    name="IMV_Al_MINING_AND_REFINING_IMPROVEMENT_TECHNOLOGY",
    units="Years",
    comp_type="Auxiliary",
    comp_subtype="with Lookup",
    depends_on={"time": 1},
)
def imv_al_mining_and_refining_improvement_technology():
    """
    Technology improvement curve for mining and refining. Based on historical observation. Implementet from the World7 model. Source: Sverdrup, H. U., Ragnarsdottir, K. V., & Koca, D. (2015). Aluminium for the future: Modelling the global production, market supply, demand, price and long term development of the global reserves. Resources, Conservation and Recycling, 103, 139-154. doi:10.1016/j.resconrec.2015.06.008.
    """
    return np.interp(
        time(),
        [
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
            0.011,
            0.011,
            0.019,
            0.019,
            0.019,
            0.019,
            0.019,
            0.019,
            0.019,
            0.019,
            0.019,
            0.019,
            0.019,
            0.019,
            0.019,
            0.019,
            0.019,
            0.019,
            0.019,
            0.019,
            0.019,
            0.024,
            0.024,
            0.024,
            0.024,
            0.024,
            0.028,
            0.028,
            0.028,
            0.033,
            0.033,
            0.033,
            0.038,
            0.038,
            0.038,
            0.043,
            0.043,
            0.047,
            0.047,
            0.047,
            0.047,
            0.057,
            0.057,
            0.0595,
            0.062,
            0.062,
            0.062,
            0.066,
            0.066,
            0.066,
            0.0685,
            0.071,
            0.076,
            0.076,
            0.081,
            0.081,
            0.085,
            0.095,
            0.1,
            0.104,
            0.114,
            0.118,
            0.128,
            0.133,
            0.142,
            0.152,
            0.161,
            0.175,
            0.18,
            0.185,
            0.213,
            0.237,
            0.2395,
            0.242,
            0.289,
            0.313,
            0.341,
            0.3435,
            0.365,
            0.379,
            0.389,
            0.393,
            0.403,
            0.412,
            0.417,
            0.422,
            0.427,
            0.436,
            0.441,
            0.455,
            0.4575,
            0.479,
            0.488,
            0.507,
            0.526,
            0.573,
            0.5755,
            0.602,
            0.621,
            0.649,
            0.682,
            0.701,
            0.72,
            0.725,
            0.735,
            0.744,
            0.758,
            0.768,
            0.863,
            0.882,
            0.891,
            0.905,
            0.915,
            0.919,
            0.924,
            0.929,
            0.934,
            0.948,
            0.957,
            0.962,
            0.991,
            0.995,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
        ],
    )


@component.add(
    name="IMV_Al_MINING_HISTORICAL",
    units="t/Year",
    comp_type="Auxiliary",
    comp_subtype="with Lookup",
    depends_on={"time": 1},
)
def imv_al_mining_historical():
    """
    Aluminium Historical mining in t/per year
    """
    return np.interp(
        time(),
        [
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
        ],
        [
            6.80e03,
            6.80e03,
            7.90e03,
            8.50e03,
            1.00e04,
            1.30e04,
            1.70e04,
            2.20e04,
            1.70e04,
            3.00e04,
            4.50e04,
            4.60e04,
            5.80e04,
            6.50e04,
            6.90e04,
            7.80e04,
            1.06e05,
            1.23e05,
            1.28e05,
            1.21e05,
            1.25e05,
            7.00e04,
            8.70e04,
            1.41e05,
            1.68e05,
            1.78e05,
            1.95e05,
            2.20e05,
            2.58e05,
            2.80e05,
            2.72e05,
            2.20e05,
            1.53e05,
            1.42e05,
            1.70e05,
            2.59e05,
            3.60e05,
            4.82e05,
            5.79e05,
            7.20e05,
            7.87e05,
            1.04e06,
            1.40e06,
            1.95e06,
            1.69e06,
            8.70e05,
            7.90e05,
            1.08e06,
            1.27e06,
            1.31e06,
            1.49e06,
            1.80e06,
            2.06e06,
            2.47e06,
            2.81e06,
            3.14e06,
            3.37e06,
            3.37e06,
            3.51e06,
            4.06e06,
            4.49e06,
            4.70e06,
            5.06e06,
            5.32e06,
            5.94e06,
            6.31e06,
            6.88e06,
            7.57e06,
            8.02e06,
            8.97e06,
            9.65e06,
            1.03e07,
            1.10e07,
            1.21e07,
            1.32e07,
            1.21e07,
            1.26e07,
            1.38e07,
            1.41e07,
            1.46e07,
            1.54e07,
            1.51e07,
            1.34e07,
            1.39e07,
            1.57e07,
            1.54e07,
            1.54e07,
            1.65e07,
            1.85e07,
            1.90e07,
            1.93e07,
            1.97e07,
            1.95e07,
            1.98e07,
            1.92e07,
            1.97e07,
            2.08e07,
            2.17e07,
            2.40e07,
            2.50e07,
            2.70e07,
            2.90e07,
            3.00e07,
            3.10e07,
            3.40e07,
            4.10e07,
            4.40e07,
            4.50e07,
            4.30e07,
            4.40e07,
            5.40e07,
            5.50e07,
            6.30e07,
            6.50e07,
            7.10e07,
            7.30e07,
            7.60e07,
            7.90e07,
            7.90e07,
            7.90e07,
            7.90e07,
        ],
    )


@component.add(
    name="IMV_AL_MINING_WATER_USE_EFFICIENCY",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="with Lookup",
    depends_on={"time": 1},
)
def imv_al_mining_water_use_efficiency():
    """
    Aluminium Water use effiency-Variable from World 7. Improvement of Water use Efficiency overtime. From 1850 until 2250
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
            2101.0,
            2102.0,
            2103.0,
            2104.0,
            2105.0,
            2106.0,
            2107.0,
            2108.0,
            2109.0,
            2110.0,
            2111.0,
            2112.0,
            2113.0,
            2114.0,
            2115.0,
            2116.0,
            2117.0,
            2118.0,
            2119.0,
            2120.0,
            2121.0,
            2122.0,
            2123.0,
            2124.0,
            2125.0,
            2126.0,
            2127.0,
            2128.0,
            2129.0,
            2130.0,
            2131.0,
            2132.0,
            2133.0,
            2134.0,
            2135.0,
            2136.0,
            2137.0,
            2138.0,
            2139.0,
            2140.0,
            2141.0,
            2142.0,
            2143.0,
            2144.0,
            2145.0,
            2146.0,
            2147.0,
            2148.0,
            2149.0,
            2150.0,
            2151.0,
            2152.0,
            2153.0,
            2154.0,
            2155.0,
            2156.0,
            2157.0,
            2158.0,
            2159.0,
            2160.0,
            2161.0,
            2162.0,
            2163.0,
            2164.0,
            2165.0,
            2166.0,
            2167.0,
            2168.0,
            2169.0,
            2170.0,
            2171.0,
            2172.0,
            2173.0,
            2174.0,
            2175.0,
            2176.0,
            2177.0,
            2178.0,
            2179.0,
            2180.0,
            2181.0,
            2182.0,
            2183.0,
            2184.0,
            2185.0,
            2186.0,
            2187.0,
            2188.0,
            2189.0,
            2190.0,
            2191.0,
            2192.0,
            2193.0,
            2194.0,
            2195.0,
            2196.0,
            2197.0,
            2198.0,
            2199.0,
            2200.0,
            2201.0,
            2202.0,
            2203.0,
            2204.0,
            2205.0,
            2206.0,
            2207.0,
            2208.0,
            2209.0,
            2210.0,
            2211.0,
            2212.0,
            2213.0,
            2214.0,
            2215.0,
            2216.0,
            2217.0,
            2218.0,
            2219.0,
            2220.0,
            2221.0,
            2222.0,
            2223.0,
            2224.0,
            2225.0,
            2226.0,
            2227.0,
            2228.0,
            2229.0,
            2230.0,
            2231.0,
            2232.0,
            2233.0,
            2234.0,
            2235.0,
            2236.0,
            2237.0,
            2238.0,
            2239.0,
            2240.0,
            2241.0,
            2242.0,
            2243.0,
            2244.0,
            2245.0,
            2246.0,
            2247.0,
            2248.0,
            2249.0,
            2250.0,
        ],
        [
            2.0,
            2.0,
            2.0,
            1.998,
            1.996,
            1.988,
            1.988,
            1.979,
            1.975,
            1.971,
            1.969,
            1.963,
            1.959,
            1.955,
            1.95,
            1.946,
            1.938,
            1.934,
            1.93,
            1.926,
            1.917,
            1.913,
            1.909,
            1.905,
            1.901,
            1.897,
            1.8925,
            1.888,
            1.88,
            1.872,
            1.868,
            1.864,
            1.85967,
            1.85533,
            1.851,
            1.839,
            1.83275,
            1.8265,
            1.82025,
            1.814,
            1.81,
            1.806,
            1.802,
            1.79575,
            1.7895,
            1.78325,
            1.777,
            1.769,
            1.756,
            1.75,
            1.736,
            1.736,
            1.731,
            1.715,
            1.707,
            1.698,
            1.69,
            1.686,
            1.661,
            1.645,
            1.64,
            1.624,
            1.607,
            1.603,
            1.591,
            1.587,
            1.579,
            1.574,
            1.57,
            1.562,
            1.558,
            1.545,
            1.533,
            1.521,
            1.517,
            1.504,
            1.496,
            1.4855,
            1.479,
            1.471,
            1.463,
            1.45,
            1.438,
            1.43,
            1.421,
            1.413,
            1.409,
            1.3945,
            1.388,
            1.372,
            1.36,
            1.347,
            1.343,
            1.339,
            1.318,
            1.31,
            1.302,
            1.285,
            1.281,
            1.269,
            1.26,
            1.252,
            1.24,
            1.2295,
            1.219,
            1.21333,
            1.20767,
            1.202,
            1.197,
            1.192,
            1.187,
            1.182,
            1.169,
            1.161,
            1.161,
            1.161,
            1.157,
            1.145,
            1.1385,
            1.132,
            1.128,
            1.124,
            1.116,
            1.1126,
            1.1092,
            1.1058,
            1.1024,
            1.099,
            1.095,
            1.093,
            1.091,
            1.087,
            1.083,
            1.08,
            1.077,
            1.074,
            1.07,
            1.066,
            1.064,
            1.062,
            1.06067,
            1.05933,
            1.058,
            1.05517,
            1.05233,
            1.0495,
            1.04667,
            1.04383,
            1.041,
            1.037,
            1.033,
            1.031,
            1.029,
            1.025,
            1.021,
            1.017,
            1.0145,
            1.012,
            1.008,
            1.006,
            1.004,
            1.004,
            1.004,
            1.004,
            1.004,
            1.004,
            1.004,
            1.004,
            1.004,
            1.004,
            1.004,
            1.004,
            0.996,
            0.992,
            0.992,
            0.992,
            0.992,
            0.992,
            0.992,
            0.992,
            0.992,
            0.992,
            0.992,
            0.992,
            0.992,
            0.992,
            0.992,
            0.992,
            0.992,
            0.992,
            0.992,
            0.992,
            0.992,
            0.992,
            0.992,
            0.992,
            0.992,
            0.992,
            0.992,
            0.992,
            0.992,
            0.992,
            0.992,
            0.99,
            0.988,
            0.988,
            0.988,
            0.988,
            0.988,
            0.988,
            0.988,
            0.988,
            0.988,
            0.988,
            0.988,
            0.988,
            0.988,
            0.988,
            0.988,
            0.988,
            0.988,
            0.988,
            0.988,
            0.988,
            0.988,
            0.988,
            0.988,
            0.988,
            0.988,
            0.988,
            0.988,
            0.988,
            0.988,
            0.988,
            0.988,
            0.988,
            0.988,
            0.988,
            0.988,
            0.983,
            0.983,
            0.983,
            0.983,
            0.983,
            0.983,
            0.981,
            0.979,
            0.979,
            0.979,
            0.979,
            0.979,
            0.979,
            0.979,
            0.979,
            0.979,
            0.979,
            0.979,
            0.979,
            0.979,
            0.979,
            0.979,
            0.979,
            0.979,
            0.979,
            0.979,
            0.979,
            0.979,
            0.979,
            0.979,
            0.981,
            0.983,
            0.983,
            0.983,
            0.983,
            0.9855,
            0.988,
            0.988,
            0.988,
            0.988,
            0.988,
            0.988,
            0.988,
            0.988,
            0.988,
            0.988,
            0.988,
            0.988,
            0.988,
            0.988,
            0.988,
            0.988,
            0.988,
            0.988,
            0.988,
            0.99,
            0.992,
            0.992,
            0.992,
            0.992,
            0.992,
            0.992,
            0.992,
            0.993333,
            0.994667,
            0.996,
            0.996,
            0.996,
            0.996,
            0.996,
            0.996,
            0.996,
            0.996,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.001,
            1.002,
            1.003,
            1.004,
            1.004,
            1.004,
            1.004,
            1.004,
            1.004,
            1.004,
            1.004,
            1.004,
            1.00267,
            1.00133,
            1.0,
            1.0,
            1.0,
            0.998,
            0.996,
            0.996,
            0.996,
            0.996,
            0.996,
            0.996,
            0.996,
            0.996,
            0.996,
            0.996,
            0.996,
            0.996,
            0.996,
            0.996,
            0.996,
            0.996,
            0.996,
            0.996,
            0.996,
            0.996,
            0.996,
            0.996,
            0.996,
            0.996,
            0.996,
            0.996,
            0.998,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.004,
            1.004,
            1.004,
            1.004,
            1.004,
            1.004,
            1.004,
            1.004,
            1.004,
            1.004,
            1.004,
            1.004,
            1.004,
            1.004,
            1.006,
            1.008,
            1.008,
            1.008,
            1.008,
            1.008,
        ],
    )


@component.add(
    name="IMV_Al_PRICE_HISTORICAL",
    units="$/per_ton",
    comp_type="Auxiliary",
    comp_subtype="with Lookup",
    depends_on={"time": 1},
)
def imv_al_price_historical():
    """
    Aluminium Historical Price developement.
    """
    return np.interp(
        time(),
        [
            1900,
            1901,
            1902,
            1903,
            1904,
            1905,
            1906,
            1907,
            1908,
            1909,
            1910,
            1911,
            1912,
            1913,
            1914,
            1915,
            1916,
            1917,
            1918,
            1919,
            1920,
            1921,
            1922,
            1923,
            1924,
            1925,
            1926,
            1927,
            1928,
            1929,
            1930,
            1931,
            1932,
            1933,
            1934,
            1935,
            1936,
            1937,
            1938,
            1939,
            1940,
            1941,
            1942,
            1943,
            1944,
            1945,
            1946,
            1947,
            1948,
            1949,
            1950,
            1951,
            1952,
            1953,
            1954,
            1955,
            1956,
            1957,
            1958,
            1959,
            1960,
            1961,
            1962,
            1963,
            1964,
            1965,
            1966,
            1967,
            1968,
            1969,
            1970,
            1971,
            1972,
            1973,
            1974,
            1975,
            1976,
            1977,
            1978,
            1979,
            1980,
            1981,
            1982,
            1983,
            1984,
            1985,
            1986,
            1987,
            1988,
            1989,
            1990,
            1991,
            1992,
            1993,
            1994,
            1995,
            1996,
            1997,
            1998,
            1999,
            2000,
            2001,
            2002,
            2003,
            2004,
            2005,
            2006,
            2007,
            2008,
            2009,
            2010,
            2011,
            2012,
            2013,
            2014,
            2015,
            2016,
            2017,
        ],
        [
            14000,
            14000,
            14000,
            13000,
            14000,
            14000,
            14000,
            17000,
            12000,
            8800,
            8600,
            7800,
            8200,
            8550,
            6660,
            12000,
            20000,
            14500,
            8000,
            6680,
            5860,
            4430,
            4000,
            5330,
            5670,
            5510,
            5460,
            5230,
            5100,
            5100,
            5150,
            5500,
            6130,
            6470,
            6290,
            5240,
            5320,
            4980,
            5100,
            5180,
            4790,
            4030,
            3310,
            3120,
            3060,
            3010,
            2760,
            2420,
            2340,
            2570,
            2640,
            2640,
            2630,
            2810,
            2920,
            3180,
            3170,
            3240,
            3090,
            3040,
            3150,
            3050,
            2830,
            2650,
            2750,
            2780,
            2710,
            2690,
            2650,
            2670,
            2660,
            2570,
            2150,
            2130,
            3140,
            2320,
            2600,
            2820,
            2800,
            3500,
            3320,
            2370,
            1740,
            2470,
            2120,
            1640,
            1830,
            2280,
            3350,
            2550,
            2030,
            1570,
            1480,
            1330,
            1730,
            2020,
            1630,
            1730,
            1440,
            1420,
            1550,
            1400,
            1300,
            1330,
            1600,
            1670,
            2160,
            2120,
            2010,
            1330,
            1720,
            2445,
            2113,
            2000,
            1900,
            1900,
            2200,
            2300,
        ],
    )


@component.add(
    name="IMV_Al_TARGET_DEMAND_PER_PERSON",
    units="kg/person",
    comp_type="Auxiliary",
    comp_subtype="with Lookup",
    depends_on={"time": 1},
)
def imv_al_target_demand_per_person():
    """
    Aluminium kg/per person-Variable from Wolrd 7- Historical Aluminium kg/ person and projected Aluminium kg/person
    """
    return np.interp(
        time(),
        [
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
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            1.1,
            1.1,
            1.6,
            1.6,
            2.1,
            2.1,
            2.1,
            2.1,
            2.1,
            2.7,
            2.7,
            3.2,
            3.2,
            3.2,
            3.7,
            3.7,
            4.3,
            4.3,
            4.3,
            4.8,
            4.8,
            4.8,
            4.8,
            4.8,
            4.8,
            4.8,
            4.8,
            4.8,
            4.8,
            4.8,
            4.8,
            4.8,
            4.8,
            4.8,
            4.8,
            4.8,
            4.8,
            4.8,
            4.8,
            4.8,
            4.3,
            4.3,
            4.5,
            4.5,
            4.5,
            4.7,
            4.9,
            5.1,
            5.3,
            5.5,
            5.5,
            5.7,
            5.7,
            5.7,
            6.3,
            6.7,
            7.2,
            7.4,
            7.8,
            8.2,
            8.6,
            9.4,
            9.8,
            10.4,
            11.9,
            12.5,
            13.1,
            13.9,
            15.3,
            15.7,
            17.0,
            17.4,
            18.2,
            19.2,
            20.9,
            21.5,
            22.8,
            23.8,
            25.1,
            25.9,
            26.7,
            28.0,
            28.8,
            29.4,
            29.8,
            30.2,
            31.5,
            32.5,
            34.2,
            35.2,
            36.2,
            37.7,
            38.9,
            41.0,
            42.2,
            42.9,
            44.1,
            45.1,
            47.4,
            48.9,
            49.7,
            52.2,
            52.8,
            55.3,
            55.7,
            57.3,
            58.0,
            58.8,
            61.1,
            61.3,
            62.5,
            64.4,
            65.4,
            67.1,
            68.3,
            69.6,
            70.4,
            71.0,
            72.0,
            72.7,
            74.1,
            74.9,
            76.2,
            77.4,
            78.7,
            79.5,
            80.5,
            81.2,
            82.2,
            83.0,
            84.1,
            84.7,
            85.3,
            86.3,
            87.2,
            88.0,
            88.2,
            89.0,
            89.9,
            90.5,
            90.9,
            91.5,
            92.5,
            93.0,
            93.4,
            93.8,
            94.5,
            94.8,
            95.7,
            96.3,
            97.1,
            97.1,
            97.7,
            97.9,
            98.1,
            98.3,
            98.6,
            99.0,
            99.0,
            99.2,
            99.4,
            99.4,
            99.8,
            99.8,
            99.8,
            100.0,
            100.0,
            100.0,
            100.0,
            100.0,
            100.0,
            100.0,
            100.0,
            100.0,
            100.0,
            100.0,
            100.0,
            100.0,
            100.0,
            100.0,
            100.0,
            100.0,
            100.0,
            100.0,
            100.0,
            100.0,
            100.0,
            100.0,
            100.0,
            100.0,
            100.0,
            100.0,
        ],
    )


@component.add(
    name="IMV_ALUMINUM_MINING_HISTORICAL",
    units="Mt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "imv_al_mining_historical": 1,
        "imv_unit_conversion_ton_to_million_ton": 1,
    },
)
def imv_aluminum_mining_historical():
    """
    Historical Aluminium mining Mt per year.
    """
    return imv_al_mining_historical() * imv_unit_conversion_ton_to_million_ton()


@component.add(
    name="IMV_GLOBAL_POPULATION",
    units="Billion_persons",
    comp_type="Auxiliary",
    comp_subtype="with Lookup",
    depends_on={"time": 1},
)
def imv_global_population():
    """
    From World 7 population module. Historical Population and projected population in the future-World 7
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
            0.59,
            0.636364,
            0.682727,
            0.69,
            0.69,
            0.69,
            0.69,
            0.69,
            0.69,
            0.698636,
            0.721818,
            0.74,
            0.74,
            0.74,
            0.74,
            0.74,
            0.765091,
            0.792909,
            0.8,
            0.8,
            0.8,
            0.8,
            0.81,
            0.833182,
            0.856364,
            0.879545,
            0.903273,
            0.931091,
            0.958909,
            0.96,
            0.96,
            0.978636,
            1.00182,
            1.025,
            1.04818,
            1.07364,
            1.10145,
            1.12,
            1.12,
            1.12409,
            1.14727,
            1.171,
            1.222,
            1.273,
            1.28,
            1.28,
            1.29636,
            1.31955,
            1.358,
            1.409,
            1.44909,
            1.47227,
            1.49,
            1.49,
            1.49182,
            1.515,
            1.53818,
            1.56564,
            1.59345,
            1.61773,
            1.64091,
            1.65,
            1.65,
            1.66045,
            1.68364,
            1.715,
            1.766,
            1.81,
            1.81,
            1.81,
            1.83273,
            1.85591,
            1.92109,
            1.99527,
            2.03545,
            2.05864,
            2.07,
            2.07,
            2.088,
            2.139,
            2.19,
            2.241,
            2.29182,
            2.33818,
            2.38455,
            2.39,
            2.39,
            2.464,
            2.566,
            2.63636,
            2.68273,
            2.71,
            2.71,
            2.74191,
            2.86709,
            2.98727,
            3.06146,
            3.13564,
            3.17273,
            3.2075,
            3.22409,
            3.23568,
            3.272,
            3.323,
            3.374,
            3.425,
            3.48327,
            3.55746,
            3.62,
            3.62,
            3.62,
            3.69418,
            3.76836,
            3.84255,
            3.91673,
            3.98136,
            4.04164,
            4.07736,
            4.09127,
            4.11727,
            4.16364,
            4.22833,
            4.3597,
            4.48433,
            4.50133,
            4.51833,
            4.60782,
            4.70518,
            4.768,
            4.819,
            4.88364,
            4.95782,
            5.0,
            5.0,
            5.014,
            5.065,
            5.11546,
            5.16182,
            5.20818,
            5.23673,
            5.26454,
            5.27,
            5.27,
            5.366,
            5.51436,
            5.64341,
            5.75236,
            5.82886,
            5.84046,
            5.86309,
            5.93727,
            6.01245,
            6.13764,
            6.26282,
            6.3,
            6.32318,
            6.33,
            6.33,
            6.37073,
            6.44491,
            6.51,
            6.561,
            6.62291,
            6.72027,
            6.81,
            6.81,
            6.81,
            6.89973,
            6.99709,
            7.02886,
            7.04045,
            7.06895,
            7.10836,
            7.16346,
            7.23764,
            7.33364,
            7.482,
            7.61,
            7.61,
            7.61,
            7.65546,
            7.70182,
            7.794,
            7.896,
            7.94546,
            7.96864,
            7.99182,
            8.015,
            8.03,
            8.03,
            8.04,
            8.091,
            8.14182,
            8.18818,
            8.23454,
            8.26455,
            8.29236,
            8.3,
            8.3,
            8.34218,
            8.41636,
            8.46955,
            8.49273,
            8.51,
            8.51,
            8.51227,
            8.53545,
            8.55864,
            8.608,
            8.659,
            8.68818,
            8.71136,
            8.72,
            8.72,
            8.73309,
            8.76091,
            8.78727,
            8.81046,
            8.83364,
            8.85682,
            8.88,
            8.88,
            8.88,
            8.88,
            8.88,
            8.88,
            8.88,
            8.88,
            8.88,
            8.89036,
            8.91818,
            8.94,
            8.94,
            8.94,
            8.94,
            8.94,
            8.94,
            8.94,
            8.95727,
            8.98046,
            8.99,
            8.99,
            8.99,
            8.99,
            8.99,
            8.99,
            8.99273,
            9.01591,
            9.03909,
            9.04,
            9.04,
        ],
    )


@component.add(
    name="IMV_UNIT_CONVERSION_TON_TO_MILLION_TON",
    units="Mt/t",
    comp_type="Constant",
    comp_subtype="Normal",
)
def imv_unit_conversion_ton_to_million_ton():
    """
    Unit conversion from t to Mt
    """
    return 1 / 1000000.0


@component.add(
    name="increase_Al_cumulative",
    units="Mt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"al_mined": 1},
)
def increase_al_cumulative():
    """
    Flow to track the Al cumulative mining
    """
    return al_mined()


@component.add(
    name="increase_Al_profit",
    units="1/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"al_profit_effect_on_mining": 1, "al_profit_scale": 1},
)
def increase_al_profit():
    """
    Al profit delay This is a workaround to avoid circular error, any short time delay works. The delayed TIME STEP, is typically used in system dynamics models to avoid algebraic loops. Any short delay will do... Engine is used to filter short term disturbances in the market price that have an effect on the mining adjustment rate. The underlaying idea is that a increase in Li market price will trigger an increase in mining. The increase in mining will be triggered when the price is high or low for a longer time step. Source: Sverdrup, H. U., & Olafsdottir, A. H. (2019). On the long-term sustainability of copper, zinc and lead supply, using a system dynamics model. Resources, Conservation & Recycling: X, 4(100007). https://doi.org/https://doi.org/10.1016/j.rcrx.2019.100007 Sverdrup, H. U., Ragnarsdottir, K. V. and Koca, D. (2015) Aluminium for the future: Modelling the global production, market supply, demand, price and long term development of the global reservesâ€™, Resources, Conservation and Recycling, 103, pp. 139â€“154. doi: 10.1016/j.resconrec.2015.06.008
    """
    return al_profit_effect_on_mining() * al_profit_scale()


@component.add(
    name="increase_Al_scrapped_metal",
    units="Mt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"decrease_stock_in_use_scrap": 1},
)
def increase_al_scrapped_metal():
    return decrease_stock_in_use_scrap()


@component.add(
    name="increase_Al_stock_in_use",
    units="Mt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"al_market_sales": 1},
)
def increase_al_stock_in_use():
    """
    All the Aluminium that is sold on the market is entering the Aluminium Stock in Use. Products made of Aluminium or containing Aluminium are entering the use stage.
    """
    return al_market_sales() * (1 - 0.144)


@component.add(
    name="INITIAL_Al_AVAILABLE",
    units="Mt/Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_al_available"},
)
def initial_al_available():
    """
    All Aluminium, going to the market and shipped to the market. Delayed to prevent simoultanous equation in vensim.Initial used to have a first value.
    """
    return _ext_constant_initial_al_available()


_ext_constant_initial_al_available = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Aluminium",
    "INITIAL_Al_MARKET",
    {},
    _root,
    {},
    "_ext_constant_initial_al_available",
)


@component.add(
    name="INITIAL_Al_CUMULATIVE_MINING",
    units="Mt",
    comp_type="Constant",
    comp_subtype="Normal",
)
def initial_al_cumulative_mining():
    """
    Al mining until 2005 based on: https://international-aluminium.org/statistics/primary-aluminium-production /
    """
    return 1528.23


@component.add(
    name="INITIAL_Al_HIDDEN_RESOURCES",
    units="Mt",
    subscripts=["Al_ORE_GRADES_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_al_hidden_resources"},
)
def initial_al_hidden_resources():
    """
    World 7 name was Al hidden high grade, Al hidden low grade, The initial values for the Al hidden stocks are based on simulation outputs from the World 7 for the year 2005. high grade is 5138,453716 Mt low grade is 6963,113157 Mt Estimations about the resource stocks that are hidden are based on: Sverdrup, H. U., Ragnarsdottir, K. V. and Koca, D. (2015) Aluminium for the future: Modelling the global production, market supply, demand, price and long term development of the global reserves, Resources, Conservation and Recycling, 103, pp. 139-154. doi: 10.1016/j.resconrec.2015.06.008. Sverdrup, H., & Ragnarsdóttir, K. V. (2014). Natural Resources in a Planetary Perspective. Geochemical Perspectives, 3(2), 129–341. https://doi.org/10.7185/geochempersp.3.2
    """
    return _ext_constant_initial_al_hidden_resources()


_ext_constant_initial_al_hidden_resources = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Aluminium",
    "INITIAL_Al_HIDDEN_RESOURCES*",
    {"Al_ORE_GRADES_I": _subscript_dict["Al_ORE_GRADES_I"]},
    _root,
    {"Al_ORE_GRADES_I": _subscript_dict["Al_ORE_GRADES_I"]},
    "_ext_constant_initial_al_hidden_resources",
)


@component.add(
    name="INITIAL_Al_KNOWN_RESERVES",
    units="Mt",
    subscripts=["Al_ORE_GRADES_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_al_known_reserves"},
)
def initial_al_known_reserves():
    """
    World 7 name was Al hidden high grade, Al hidden low grade, The initial values for the Al hidden stocks are based on simulation outputs from the World 7 for the year 2005. known high grade is 4074,746287 Mt known low grade is 5096,813181 Mt Estimations about the resource stocks that are hidden are based on: Sverdrup, H. U., Ragnarsdottir, K. V. and Koca, D. (2015) Aluminium for the future: Modelling the global production, market supply, demand, price and long term development of the global reserves, Resources, Conservation and Recycling, 103, pp. 139-154. doi: 10.1016/j.resconrec.2015.06.008. Sverdrup, H., & Ragnarsdóttir, K. V. (2014). Natural Resources in a Planetary Perspective. Geochemical Perspectives, 3(2), 129–341. https://doi.org/10.7185/geochempersp.3.2
    """
    return _ext_constant_initial_al_known_reserves()


_ext_constant_initial_al_known_reserves = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Aluminium",
    "INITIAL_Al_KNOWN_RESERVES*",
    {"Al_ORE_GRADES_I": _subscript_dict["Al_ORE_GRADES_I"]},
    _root,
    {"Al_ORE_GRADES_I": _subscript_dict["Al_ORE_GRADES_I"]},
    "_ext_constant_initial_al_known_reserves",
)


@component.add(
    name="INITIAL_Al_MARKET",
    units="Mt",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_al_market"},
)
def initial_al_market():
    """
    World 7 name was Al Market, The initial values for the Al market stock is based on simulation outputs from the World 7 for the year 2005. 3.68661 The World 7 outputs are based on initial values from 1850. Source: Sverdrup, H. U., Ragnarsdottir, K. V. and Koca, D. (2015) Aluminium for the future: Modelling the global production, market supply, demand, price and long term development of the global reservesâ€™, Resources, Conservation and Recycling, 103, pp. 139â€“154. doi: 10.1016/j.resconrec.2015.06.008.
    """
    return _ext_constant_initial_al_market()


_ext_constant_initial_al_market = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Aluminium",
    "INITIAL_Al_MARKET",
    {},
    _root,
    {},
    "_ext_constant_initial_al_market",
)


@component.add(name="INITIAL_Al_PRICE", comp_type="Constant", comp_subtype="Normal")
def initial_al_price():
    """
    The Aluminium price of the year 2005 in $/t GET DIRECT CONSTANTS('model_parameters/materials/materials.xlsx', 'Aluminium', 'INITIAL_Al_PRICE')
    """
    return 1853


@component.add(
    name="INITIAL_Al_PROFIT_DELAY",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="Normal",
)
def initial_al_profit_delay():
    """
    World 7 name was Al Profit Delay, The initial values for the Al Profit Delay stock is based on simulation outputs from the World 7 for the year 2005. The World 7 outputs are based on initial values from 1850. GET DIRECT CONSTANTS('model_parameters/materials/materials.xlsx', 'Aluminium', 'INITIAL_Al_PROFIT_DELAY') Source: Sverdrup, H. U., Ragnarsdottir, K. V. and Koca, D. (2015) Aluminium for the future: Modelling the global production, market supply, demand, price and long term development of the global reservesâ€™, Resources, Conservation and Recycling, 103, pp. 139â€“154. doi: 10.1016/j.resconrec.2015.06.008.
    """
    return 8


@component.add(
    name="INITIAL_Al_SCRAPPED_METAL",
    units="Mt",
    comp_type="Constant",
    comp_subtype="Normal",
)
def initial_al_scrapped_metal():
    """
    World 7 name was Al scrapped metal, The initial values for the Al scrapped metal stock is based on simulation outputs from the World 7 for the year 2005. The World 7 outputs are based on initial values from 1850. Source: Sverdrup, H. U., Ragnarsdottir, K. V., & Koca, D. (2015). Aluminium for the future: Modelling the global production, market supply, demand, price and long term development of the global reserves. Resources, Conservation and Recycling, 103, 139-154. doi:10.1016/j.resconrec.2015.06.008. GET DIRECT CONSTANTS('model_parameters/materials/materials.xlsx', 'Aluminium', 'INITIAL_Al_SCRAPPED_METAL')
    """
    return 13.4


@component.add(
    name="INITIAL_Al_USE",
    units="Mt",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_al_use"},
)
def initial_al_use():
    """
    World 7 name was Al STOCKS IN USE, The initial values for the Al STOCKS IN USE ,stock is based on simulation outputs from the World 7 for the year 2005. The World 7 outputs are based on initial values from 1850. Source: Sverdrup, H. U., Ragnarsdottir, K. V., & Koca, D. (2015). Aluminium for the future: Modelling the global production, market supply, demand, price and long term development of the global reserves. Resources, Conservation and Recycling, 103, 139-154. doi:10.1016/j.resconrec.2015.06.008.
    """
    return _ext_constant_initial_al_use()


_ext_constant_initial_al_use = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Aluminium",
    "INITIAL_Al_IN_USE",
    {},
    _root,
    {},
    "_ext_constant_initial_al_use",
)


@component.add(
    name="MAXIMUM_Al_PRICE",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_maximum_al_price"},
)
def maximum_al_price():
    """
    Set Maximum of the Aluminium price for the case that supply is higher than demand. Used to avoid floating point error in Vesnim and due to the fact that the could not effect the demand in the same time step.
    """
    return _ext_constant_maximum_al_price()


_ext_constant_maximum_al_price = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Aluminium",
    "MAXIMUM_Al_PRICE",
    {},
    _root,
    {},
    "_ext_constant_maximum_al_price",
)


@component.add(
    name="mining_Al_known_reserves",
    units="Mt/Year",
    subscripts=["Al_ORE_GRADES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "al_known_reseveres": 2,
        "al_extraction_coefficient": 2,
        "al_low_grade_change_price": 1,
        "al_low_grade_factor_mining": 1,
    },
)
def mining_al_known_reserves():
    """
    Mining of low and high grade Aluminium. Mining is the action that extracts Aluminium from “known reserves”. There are fundamental differences in how mining in an individual mine is modelled on the business level and what happens when a whole population of mines are operated. Then host dynamics and group behaviour come into play, changing the equations. Many of the particulars of a single mine are distributed over time in a population of mines, leading to the good sense of working with averages and where discrete events become. Sverdrup, H. U., Ragnarsdottir, K. V. and Koca, D. (2015) Aluminium for the future: Modelling the global production, market supply, demand, price and long term development of the global reserves’, Resources, Conservation and Recycling, 103, pp. 139–154. doi: 10.1016/j.resconrec.2015.06.008
    """
    value = xr.DataArray(
        np.nan,
        {"Al_ORE_GRADES_I": _subscript_dict["Al_ORE_GRADES_I"]},
        ["Al_ORE_GRADES_I"],
    )
    value.loc[["HIGH_GRADE"]] = np.maximum(
        float(al_known_reseveres().loc["HIGH_GRADE"]) * al_extraction_coefficient(), 0
    )
    value.loc[["LOW_GRADE"]] = np.maximum(
        al_low_grade_change_price()
        * al_extraction_coefficient()
        * float(al_known_reseveres().loc["LOW_GRADE"])
        * al_low_grade_factor_mining(),
        0,
    )
    return value


@component.add(
    name="PRICE_SENSITIVITY_S_CURVE_FIT",
    units="DMNL",
    subscripts=["S_CURVE_FIT_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_price_sensitivity_s_curve_fit"},
)
def price_sensitivity_s_curve_fit():
    """
    This is an experience-based response curve for how the increase in price reduces the demand for aluminium. A S CURVE FIT -0.869609 k S CURVE FIT 1.97191e-09 n S CURVE FIT 2.28547 Sverdrup, H. U., Ragnarsdottir, K. V. and Koca, D. (2015) Aluminium for the future: Modelling the global production, market supply, demand, price and long term development of the global reservesâ€™, Resources, Conservation and Recycling, 103, pp. 139â€“154. doi: 10.1016/j.resconrec.2015.06.008.
    """
    return _ext_constant_price_sensitivity_s_curve_fit()


_ext_constant_price_sensitivity_s_curve_fit = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Aluminium",
    "PRICE_SENSITIVITY_S_CURVE_FIT*",
    {"S_CURVE_FIT_I": _subscript_dict["S_CURVE_FIT_I"]},
    _root,
    {"S_CURVE_FIT_I": _subscript_dict["S_CURVE_FIT_I"]},
    "_ext_constant_price_sensitivity_s_curve_fit",
)


@component.add(
    name="Primary_Al_mined_hist",
    comp_type="Auxiliary",
    comp_subtype="with Lookup",
    depends_on={"time": 1},
)
def primary_al_mined_hist():
    """
    https://international-aluminium.org/statistics/primary-aluminium-production /
    """
    return np.interp(
        time(),
        [
            1973,
            1974,
            1975,
            1976,
            1977,
            1978,
            1979,
            1980,
            1981,
            1982,
            1983,
            1984,
            1985,
            1986,
            1987,
            1988,
            1989,
            1990,
            1991,
            1992,
            1993,
            1994,
            1995,
            1996,
            1997,
            1998,
            1999,
            2000,
            2001,
            2002,
            2003,
            2004,
            2005,
            2006,
            2007,
            2008,
            2009,
            2010,
            2011,
            2012,
            2013,
            2014,
            2015,
            2016,
            2017,
            2018,
            2019,
            2020,
            2021,
            2022,
        ],
        [
            12017,
            13463,
            12326,
            12629,
            13793,
            14152,
            14560,
            15390,
            15116,
            13544,
            13967,
            15781,
            15486,
            15583,
            16497,
            18577,
            19138,
            19514,
            19650,
            19455,
            19724,
            19147,
            19610,
            20859,
            21807,
            22721,
            23721,
            24657,
            24510,
            26156,
            27986,
            29857,
            31905,
            33938,
            38132,
            39971,
            37706,
            42353,
            46275,
            49167,
            52291,
            54647,
            58456,
            59890,
            63404,
            64166,
            63657,
            65325,
            67092,
            68461,
        ],
    )


@component.add(
    name="primary_Al_mined_hist_Mt",
    units="Mt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"primary_al_mined_hist": 1},
)
def primary_al_mined_hist_mt():
    """
    https://international-aluminium.org/statistics/primary-aluminium-production /
    """
    return primary_al_mined_hist() / 1000


@component.add(
    name="RECYCLING_DRIVE_EXP_FIT",
    units="Mt/M$",
    subscripts=["EXP_CURVE_FIT_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_recycling_drive_exp_fit"},
)
def recycling_drive_exp_fit():
    """
    Parameters extracted from curve fitting the graphical function previously used in the WORLD7 model. A EXP CURVE 17479.1 B EXP CURVE 3665.02 Source: Sverdrup, H. U., Ragnarsdottir, K. V., & Koca, D. (2015). Aluminium for the future: Modelling the global production, market supply, demand, price and long term development of the global reserves. Resources, Conservation and Recycling, 103, 139-154. doi:10.1016/j.resconrec.2015.06.008.
    """
    return _ext_constant_recycling_drive_exp_fit()


_ext_constant_recycling_drive_exp_fit = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Aluminium",
    "RECYCLING_DRIVE_EXP_FIT*",
    {"EXP_CURVE_FIT_I": _subscript_dict["EXP_CURVE_FIT_I"]},
    _root,
    {"EXP_CURVE_FIT_I": _subscript_dict["EXP_CURVE_FIT_I"]},
    "_ext_constant_recycling_drive_exp_fit",
)


@component.add(name="Scaling_Factor_low", comp_type="Constant", comp_subtype="Normal")
def scaling_factor_low():
    return 0.75


@component.add(
    name="Share_of_Primary",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="with Lookup",
    depends_on={"time": 1},
)
def share_of_primary():
    """
    Source: International Aluminium Institute (IAI) updated version of its material flow model https://international-aluminium.org/resource/iai-material-flow-model-2021-u pdate/
    """
    return np.interp(
        time(),
        [
            1950.0,
            1960.0,
            1970.0,
            1980.0,
            1990.0,
            2000.0,
            2010.0,
            2020.0,
            2030.0,
            2040.0,
            2050.0,
        ],
        [
            89.1648,
            86.2302,
            83.2957,
            77.4266,
            72.912,
            67.7201,
            67.7201,
            66.8172,
            57.1106,
            53.9503,
            49.4357,
        ],
    )


@component.add(
    name="Share_of_Secondary",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="with Lookup",
    depends_on={"time": 1},
)
def share_of_secondary():
    """
    Source: International Aluminium Institute (IAI) updated version of its material flow model https://international-aluminium.org/resource/iai-material-flow-model-2021-u pdate/
    """
    return np.interp(
        time(),
        [
            1950.0,
            1960.0,
            1970.0,
            1980.0,
            1990.0,
            2000.0,
            2010.0,
            2020.0,
            2030.0,
            2040.0,
            2050.0,
        ],
        [
            12.6411,
            14.6727,
            18.0587,
            23.4763,
            28.2167,
            32.9571,
            34.0858,
            33.6343,
            44.6953,
            46.7269,
            51.693,
        ],
    )


@component.add(
    name="Smooth_Price",
    comp_type="Stateful",
    comp_subtype="Smooth",
    depends_on={"_smooth_smooth_price": 1},
    other_deps={
        "_smooth_smooth_price": {
            "initial": {"al_price_historical": 1},
            "step": {"al_price_historical": 1},
        }
    },
)
def smooth_price():
    return _smooth_smooth_price()


_smooth_smooth_price = Smooth(
    lambda: al_price_historical(),
    lambda: 6,
    lambda: al_price_historical(),
    lambda: 3,
    "_smooth_smooth_price",
)


@component.add(
    name="SUM_OUT_PUT_REAL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"output_real": 1},
)
def sum_out_put_real():
    """
    Sum Output real from economy model to check the value.
    """
    return sum(
        output_real()
        .loc[:, "MINING_AND_MANUFACTURING_ALUMINIUM"]
        .reset_coords(drop=True)
        .rename({"REGIONS_35_I": "REGIONS_35_I!"}),
        dim=["REGIONS_35_I!"],
    )


@component.add(
    name="SWITCH_Al_RECYCLING_POLICY",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="Normal",
)
def switch_al_recycling_policy():
    """
    This switch can take two values: 0: the (sub)module runs with BASE SCENARIIO for recycling 1: the (sub)module runs wit RECYCLING POLICY
    """
    return 0


@component.add(
    name="SWITCH_ECO2MAT_Al_DEMAND",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_eco2mat_al_demand"},
)
def switch_eco2mat_al_demand():
    """
    Intermodule links SWITCH, it can take two values: 0: the link is broken, the intermodule variable is replaced by an exogenous parameter. 1: the link between modules is operational.
    """
    return _ext_constant_switch_eco2mat_al_demand()


_ext_constant_switch_eco2mat_al_demand = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_ECO2MAT_Al_DEMAND",
    {},
    _root,
    {},
    "_ext_constant_switch_eco2mat_al_demand",
)


@component.add(
    name="SWITCH_MAT2ECO_Al_PRICE",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_mat2eco_al_price"},
)
def switch_mat2eco_al_price():
    """
    Intermodule links SWITCH, it can take two values: 0: the link is broken, the intermodule variable is replaced by an exogenous parameter. 1: the link between modules is operational.
    """
    return _ext_constant_switch_mat2eco_al_price()


_ext_constant_switch_mat2eco_al_price = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_MAT2ECO_Al_PRICE",
    {},
    _root,
    {},
    "_ext_constant_switch_mat2eco_al_price",
)


@component.add(
    name="total_Al_known_reserves",
    units="Mt",
    subscripts=["ORE_GRADES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"al_known_reseveres": 1},
)
def total_al_known_reserves():
    """
    Sum of Aluminiun in different ore grade.
    """
    return xr.DataArray(
        sum(
            al_known_reseveres().rename({"Al_ORE_GRADES_I": "Al_ORE_GRADES_I!"}),
            dim=["Al_ORE_GRADES_I!"],
        ),
        {"ORE_GRADES_I": _subscript_dict["ORE_GRADES_I"]},
        ["ORE_GRADES_I"],
    )


@component.add(
    name="Total_Secondary_new_and_old_scrap",
    units="Mt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "al_demand_including_semifinished_products": 1,
        "primary_al_mined_hist_mt": 1,
    },
)
def total_secondary_new_and_old_scrap():
    return al_demand_including_semifinished_products() - primary_al_mined_hist_mt()


@component.add(
    name="World_Pop",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"world_population": 1},
)
def world_pop():
    return world_population() / 10**9
