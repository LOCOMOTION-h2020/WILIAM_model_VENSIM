"""
Module materials.mo
Translated using PySD version 3.10.0
"""


@component.add(
    name="COEFFICIENT_Mo_DEMAND",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="Normal",
)
def coefficient_mo_demand():
    """
    Demand scaling for fitting to data
    """
    return 0.0184


@component.add(
    name="COEFFICIENTS_Mo_CHANGE_GRADE",
    units="DMNL",
    subscripts=["Mo_Ore_GRADES_I", "S_CURVE_FIT_ABC_I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def coefficients_mo_change_grade():
    """
    When the price exceeds the extraction cost for an ore quality, then it can be extracted with profit. Harald Sverdrup, 2021: LOCOMOTION Project report: Estimating the cost of extraction and the price required for changing between mining of different ore grades in the WORLD7 model. 20 pp.
    """
    value = xr.DataArray(
        np.nan,
        {
            "Mo_Ore_GRADES_I": _subscript_dict["Mo_Ore_GRADES_I"],
            "S_CURVE_FIT_ABC_I": _subscript_dict["S_CURVE_FIT_ABC_I"],
        },
        ["Mo_Ore_GRADES_I", "S_CURVE_FIT_ABC_I"],
    )
    value.loc[["HIGH_GRADE"], ["A_S_CURVE"]] = 1
    value.loc[["HIGH_GRADE"], ["B_S_CURVE"]] = 1
    value.loc[["HIGH_GRADE"], ["C_S_CURVE"]] = 1
    value.loc[["LOW_GRADE"], ["A_S_CURVE"]] = 1.00296
    value.loc[["LOW_GRADE"], ["B_S_CURVE"]] = 0.00193797
    value.loc[["LOW_GRADE"], ["C_S_CURVE"]] = 4131.91
    value.loc[["ULTRALOW_GRADE"], ["A_S_CURVE"]] = 1.00346
    value.loc[["ULTRALOW_GRADE"], ["B_S_CURVE"]] = 0.000685758
    value.loc[["ULTRALOW_GRADE"], ["C_S_CURVE"]] = 12562.2
    value.loc[["TRACE_GRADE"], ["A_S_CURVE"]] = 1.01519
    value.loc[["TRACE_GRADE"], ["B_S_CURVE"]] = 0.000419748
    value.loc[["TRACE_GRADE"], ["C_S_CURVE"]] = 19382.3
    return value


@component.add(
    name="COEFFICIENTS_Mo_DEMAND_PRICE_EFFECT",
    units="DMNL",
    subscripts=["S_CURVE_FIT_ABC_I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def coefficients_mo_demand_price_effect():
    """
    A=0,952348536 B=0,000279581 C=16438,78487 Transforming the price-demand response curve to equation
    """
    value = xr.DataArray(
        np.nan,
        {"S_CURVE_FIT_ABC_I": _subscript_dict["S_CURVE_FIT_ABC_I"]},
        ["S_CURVE_FIT_ABC_I"],
    )
    value.loc[["A_S_CURVE"]] = 0.952349
    value.loc[["B_S_CURVE"]] = 0.000279581
    value.loc[["C_S_CURVE"]] = 16438.8
    return value


@component.add(
    name="coefficients_mo_price",
    units="DMNL",
    subscripts=["EQUATION_SPLIT_I", "LINEAR_LOG_FIT_I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def coefficients_mo_price():
    value = xr.DataArray(
        np.nan,
        {
            "EQUATION_SPLIT_I": _subscript_dict["EQUATION_SPLIT_I"],
            "LINEAR_LOG_FIT_I": _subscript_dict["LINEAR_LOG_FIT_I"],
        },
        ["EQUATION_SPLIT_I", "LINEAR_LOG_FIT_I"],
    )
    value.loc[["EQUATION_ONE"], ["A_LINEAR_LOG_FIT"]] = 159758
    value.loc[["EQUATION_ONE"], ["B_LINEAR_LOG_FIT"]] = -106.4
    value.loc[["EQUATION_TWO"], ["A_LINEAR_LOG_FIT"]] = 64533
    value.loc[["EQUATION_TWO"], ["B_LINEAR_LOG_FIT"]] = -49.42
    value.loc[["EQUATION_THREE"], ["A_LINEAR_LOG_FIT"]] = 0
    value.loc[["EQUATION_THREE"], ["B_LINEAR_LOG_FIT"]] = 0
    return value


@component.add(
    name="IMV_Cu_MINED",
    units="Mt/Years",
    comp_type="Auxiliary",
    comp_subtype="with Lookup",
    depends_on={"time": 1},
)
def imv_cu_mined():
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
    name="IMV_Cu_MINED_to_Mo",
    units="Mt/Years",
    comp_type="Auxiliary",
    comp_subtype="with Lookup",
    depends_on={"time": 1},
)
def imv_cu_mined_to_mo():
    """
    From the copper module
    """
    return np.interp(
        time(),
        [
            1900.0,
            1902.31,
            1904.62,
            1906.92,
            1909.23,
            1911.54,
            1913.85,
            1916.15,
            1918.46,
            1920.77,
            1923.08,
            1925.38,
            1927.69,
            1930.0,
            1932.31,
            1934.62,
            1936.92,
            1939.23,
            1941.54,
            1943.85,
            1946.15,
            1948.46,
            1950.77,
            1953.08,
            1955.38,
            1957.69,
            1960.0,
            1962.31,
            1964.62,
            1966.92,
            1969.23,
            1971.54,
            1973.85,
            1976.15,
            1978.46,
            1980.77,
            1983.08,
            1985.38,
            1987.69,
            1990.0,
            1992.31,
            1994.62,
            1996.92,
            1999.23,
            2001.54,
            2003.85,
            2006.15,
            2008.46,
            2010.77,
            2013.08,
            2015.38,
            2017.69,
            2020.0,
            2022.31,
            2024.62,
            2026.92,
            2029.23,
            2031.54,
            2033.85,
            2036.15,
            2038.46,
            2040.77,
            2043.08,
            2045.38,
            2047.69,
            2050.0,
            2052.31,
            2054.62,
            2056.92,
            2059.23,
            2061.54,
            2063.85,
            2066.15,
            2068.46,
            2070.77,
            2073.08,
            2075.38,
            2077.69,
            2080.0,
            2082.31,
            2084.62,
            2086.92,
            2089.23,
            2091.54,
            2093.85,
            2096.15,
            2098.46,
            2100.77,
            2103.08,
            2105.38,
            2107.69,
            2110.0,
            2112.31,
            2114.62,
            2116.92,
            2119.23,
            2121.54,
            2123.85,
            2126.15,
            2128.46,
            2130.77,
            2133.08,
            2135.38,
            2137.69,
            2140.0,
            2142.31,
            2144.62,
            2146.92,
            2149.23,
            2151.54,
            2153.85,
            2156.15,
            2158.46,
            2160.77,
            2163.08,
            2165.38,
            2167.69,
            2170.0,
            2172.31,
            2174.62,
            2176.92,
            2179.23,
            2181.54,
            2183.85,
            2186.15,
            2188.46,
            2190.77,
            2193.08,
            2195.38,
            2197.69,
            2200.0,
        ],
        [
            0.29,
            0.86,
            0.86,
            1.0,
            1.0,
            1.14,
            1.28,
            1.43,
            1.57,
            1.71,
            1.85,
            2.0,
            2.28,
            2.42,
            2.57,
            2.71,
            2.99,
            3.42,
            3.71,
            3.99,
            4.42,
            4.7,
            6.13,
            6.41,
            6.84,
            7.41,
            8.12,
            8.69,
            9.41,
            9.98,
            10.69,
            12.26,
            12.54,
            13.11,
            13.4,
            12.83,
            13.11,
            13.97,
            14.96,
            16.25,
            17.39,
            18.24,
            19.24,
            19.95,
            21.38,
            22.23,
            23.23,
            23.94,
            25.37,
            26.51,
            27.51,
            28.65,
            29.5,
            30.64,
            31.78,
            32.49,
            33.63,
            35.2,
            36.34,
            37.48,
            39.05,
            40.48,
            42.04,
            43.33,
            44.61,
            47.32,
            47.46,
            49.6,
            50.45,
            51.31,
            51.88,
            52.87,
            53.87,
            54.3,
            54.87,
            55.01,
            55.01,
            55.01,
            55.01,
            55.01,
            54.73,
            54.3,
            53.73,
            53.16,
            52.73,
            52.16,
            51.73,
            50.74,
            50.31,
            49.88,
            49.31,
            48.88,
            48.17,
            47.46,
            46.89,
            46.32,
            45.18,
            44.75,
            44.04,
            43.47,
            42.9,
            42.19,
            41.76,
            41.47,
            40.76,
            40.05,
            39.33,
            38.76,
            38.34,
            37.77,
            37.05,
            35.63,
            34.63,
            33.92,
            33.35,
            32.78,
            31.78,
            30.93,
            30.36,
            28.93,
            28.08,
            27.22,
            26.79,
            26.22,
            25.8,
            25.51,
            24.94,
            24.51,
            23.66,
            23.09,
            22.38,
        ],
    )


@component.add(
    name="IMV_Mo_SECOND_SPECULATION",
    units="Mt/Years",
    comp_type="Auxiliary",
    comp_subtype="with Lookup",
    depends_on={"time": 1},
)
def imv_mo_second_speculation():
    """
    Metal trader informal information Sverdrup, H., Olofsdottir, A.H., Ragnarsdottir, K.V., Koca, D., 2018. A system dynamics assessment of the supply of molybdenum and rhenium used for superalloys and specialty steels, using the WORLD6 model. Biophysical Economics and Resource Quality 4: 1-52 (DOI: 10.1007/s41247-018-0040-9)
    """
    return np.interp(
        time(),
        [
            2000.0,
            2000.07,
            2000.13,
            2000.2,
            2000.27,
            2000.33,
            2000.4,
            2000.47,
            2000.53,
            2000.6,
            2000.67,
            2000.73,
            2000.8,
            2000.87,
            2000.93,
            2001.0,
            2001.07,
            2001.13,
            2001.2,
            2001.27,
            2001.33,
            2001.4,
            2001.47,
            2001.53,
            2001.6,
            2001.67,
            2001.73,
            2001.8,
            2001.87,
            2001.93,
            2002.0,
            2002.07,
            2002.13,
            2002.2,
            2002.27,
            2002.33,
            2002.4,
            2002.47,
            2002.53,
            2002.6,
            2002.67,
            2002.73,
            2002.8,
            2002.87,
            2002.93,
            2003.0,
            2003.07,
            2003.13,
            2003.2,
            2003.27,
            2003.33,
            2003.4,
            2003.47,
            2003.53,
            2003.6,
            2003.67,
            2003.73,
            2003.8,
            2003.87,
            2003.93,
            2004.0,
            2004.07,
            2004.13,
            2004.2,
            2004.27,
            2004.33,
            2004.4,
            2004.47,
            2004.53,
            2004.6,
            2004.67,
            2004.73,
            2004.8,
            2004.87,
            2004.93,
            2005.0,
            2005.07,
            2005.13,
            2005.2,
            2005.27,
            2005.33,
            2005.4,
            2005.47,
            2005.53,
            2005.6,
            2005.67,
            2005.73,
            2005.8,
            2005.87,
            2005.93,
            2006.0,
            2006.07,
            2006.13,
            2006.2,
            2006.27,
            2006.33,
            2006.4,
            2006.47,
            2006.53,
            2006.6,
            2006.67,
            2006.73,
            2006.8,
            2006.87,
            2006.93,
            2007.0,
            2007.07,
            2007.13,
            2007.2,
            2007.27,
            2007.33,
            2007.4,
            2007.47,
            2007.53,
            2007.6,
            2007.67,
            2007.73,
            2007.8,
            2007.87,
            2007.93,
            2008.0,
            2008.07,
            2008.13,
            2008.2,
            2008.27,
            2008.33,
            2008.4,
            2008.47,
            2008.53,
            2008.6,
            2008.67,
            2008.73,
            2008.8,
            2008.87,
            2008.93,
            2009.0,
            2009.07,
            2009.13,
            2009.2,
            2009.27,
            2009.33,
            2009.4,
            2009.47,
            2009.53,
            2009.6,
            2009.67,
            2009.73,
            2009.8,
            2009.87,
            2009.93,
            2010.0,
            2010.07,
            2010.13,
            2010.2,
            2010.27,
            2010.33,
            2010.4,
            2010.47,
            2010.53,
            2010.6,
            2010.67,
            2010.73,
            2010.8,
            2010.87,
            2010.93,
            2011.0,
            2011.07,
            2011.13,
            2011.2,
            2011.27,
            2011.33,
            2011.4,
            2011.47,
            2011.53,
            2011.6,
            2011.67,
            2011.73,
            2011.8,
            2011.87,
            2011.93,
            2012.0,
            2012.07,
            2012.13,
            2012.2,
            2012.27,
            2012.33,
            2012.4,
            2012.47,
            2012.53,
            2012.6,
            2012.67,
            2012.73,
            2012.8,
            2012.87,
            2012.93,
            2013.0,
            2013.07,
            2013.13,
            2013.2,
            2013.27,
            2013.33,
            2013.4,
            2013.47,
            2013.53,
            2013.6,
            2013.67,
            2013.73,
            2013.8,
            2013.87,
            2013.93,
            2014.0,
            2014.07,
            2014.13,
            2014.2,
            2014.27,
            2014.33,
            2014.4,
            2014.47,
            2014.53,
            2014.6,
            2014.67,
            2014.73,
            2014.8,
            2014.87,
            2014.93,
            2015.0,
            2015.07,
            2015.13,
            2015.2,
            2015.27,
            2015.33,
            2015.4,
            2015.47,
            2015.53,
            2015.6,
            2015.67,
            2015.73,
            2015.8,
            2015.87,
            2015.93,
            2016.0,
            2016.07,
            2016.13,
            2016.2,
            2016.27,
            2016.33,
            2016.4,
            2016.47,
            2016.53,
            2016.6,
            2016.67,
            2016.73,
            2016.8,
            2016.87,
            2016.93,
            2017.0,
            2017.07,
            2017.13,
            2017.2,
            2017.27,
            2017.33,
            2017.4,
            2017.47,
            2017.53,
            2017.6,
            2017.67,
            2017.73,
            2017.8,
            2017.87,
            2017.93,
            2018.0,
            2018.07,
            2018.13,
            2018.2,
            2018.27,
            2018.33,
            2018.4,
            2018.47,
            2018.53,
            2018.6,
            2018.67,
            2018.73,
            2018.8,
            2018.87,
            2018.93,
            2019.0,
            2019.07,
            2019.13,
            2019.2,
            2019.27,
            2019.33,
            2019.4,
            2019.47,
            2019.53,
            2019.6,
            2019.67,
            2019.73,
            2019.8,
            2019.87,
            2019.93,
            2020.0,
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
            0.000643,
            0.000643,
            0.000643,
            0.001929,
            0.005788,
            0.006431,
            0.007717,
            0.00836,
            0.009003,
            0.010289,
            0.011576,
            0.012862,
            0.014148,
            0.016077,
            0.02701,
            0.1423,
            0.039871,
            0.04373,
            0.045659,
            0.048875,
            0.055949,
            0.066238,
            0.092605,
            0.1955,
            0.124116,
            0.126045,
            0.1964,
            0.1955,
            0.126688,
            0.124759,
            0.124116,
            0.1937,
            0.072026,
            0.005788,
            0.005145,
            0.004502,
            0.004502,
            0.004502,
            0.003859,
            0.003859,
            0.003215,
            0.002572,
            0.001929,
            0.001929,
            0.001286,
            0.001286,
            0.000643,
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
        ],
    )


@component.add(
    name="IMV_SS_Mo_DEMAND",
    units="Mt/Years",
    comp_type="Auxiliary",
    comp_subtype="with Lookup",
    depends_on={"time": 1},
)
def imv_ss_mo_demand():
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
            0.097924,
            0.097579,
            0.095866,
            0.09935,
            0.101377,
            0.104268,
            0.108738,
            0.114048,
            0.117136,
            0.121395,
            0.124307,
            0.124779,
            0.140529,
            0.144124,
            0.147501,
            0.153659,
            0.158081,
            0.160371,
            0.165696,
            0.170188,
            0.177334,
            0.18053,
            0.185293,
            0.187185,
            0.187703,
            0.19406,
            0.195426,
            0.19817,
            0.205321,
            0.206268,
            0.205676,
            0.208071,
            0.207861,
            0.20832,
            0.210728,
            0.211005,
            0.215793,
            0.215603,
            0.217796,
            0.217674,
            0.221819,
            0.226092,
            0.223055,
            0.221493,
            0.221509,
            0.223033,
            0.222026,
            0.222776,
            0.2233,
            0.223906,
            0.224542,
            0.273322,
            0.280615,
            0.277543,
            0.275833,
            0.274574,
            0.283088,
            0.283406,
            0.282047,
            0.281563,
            0.287075,
            0.291343,
            0.291862,
            0.29259,
            0.293323,
            0.292294,
            0.290127,
            0.288478,
            0.290273,
            0.29339,
            0.293674,
            0.291922,
            0.290843,
            0.289709,
            0.290051,
            0.289706,
            0.287635,
            0.292776,
            0.294401,
            0.290116,
            0.288307,
            0.285455,
            0.284511,
            0.287581,
            0.293726,
            0.297843,
            0.295563,
            0.299665,
            0.305045,
            0.303196,
            0.30146,
            0.300476,
            0.301811,
            0.302581,
            0.301773,
            0.301039,
        ],
    )


@component.add(
    name="INITIAL_Mo_FILTER_PROFIT",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="Normal",
)
def initial_mo_filter_profit():
    """
    World 7 name was Li Ceramics, The initial values for the Li Ceramics stock is based on simulation outputs from the World 7 for the year 2005. The World 7 outputs are based on initial values from 1850. Source: Sverdrup, H. U. (2016) â€˜Modelling global extraction, supply, price and depletion of the extractable geological resources with the LITHIUM modelâ€™, Resources, Conservation and Recycling, 114, pp. 112â€“129. doi: 10.1016/j.resconrec.2016.07.002.
    """
    return 7.68924


@component.add(
    name="INITIAL_Mo_HIDDEN",
    units="Mt",
    subscripts=["Mo_Ore_GRADES_I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def initial_mo_hidden():
    """
    World 7 name was Li hidden high grade, Li hidden low grade, Li hidden ultralow grade The initial values for the Li hidden stocks are based on simulation outputs from the World7 for the year 2005. The World7 outputs are based on initial values from 1850. high grade is 0,65 low grade is 19,88 ultralow grade is 2,89 Source: Sverdrup, H. U. (2016) â€˜Modelling global extraction, supply, price and depletion of the extractable geological resources with the LITHIUM modelâ€™, Resources, Conservation and Recycling, 114, pp. 112â€“129. doi: 10.1016/j.resconrec.2016.07.002.
    """
    value = xr.DataArray(
        np.nan,
        {"Mo_Ore_GRADES_I": _subscript_dict["Mo_Ore_GRADES_I"]},
        ["Mo_Ore_GRADES_I"],
    )
    value.loc[["HIGH_GRADE"]] = 1.067
    value.loc[["LOW_GRADE"]] = 8.66
    value.loc[["ULTRALOW_GRADE"]] = 17.42
    value.loc[["TRACE_GRADE"]] = 32.09
    return value


@component.add(
    name="INITIAL_Mo_IN_ALLOYS", units="Mt", comp_type="Constant", comp_subtype="Normal"
)
def initial_mo_in_alloys():
    """
    World 7 name was Li Air conditioning, The initial values for the Li Air conditioning stock is based on simulation outputs from the World 7 for the year 2005. The World 7 outputs are based on initial values from 1850. Source: Sverdrup, H. U. (2016) â€˜Modelling global extraction, supply, price and depletion of the extractable geological resources with the LITHIUM modelâ€™, Resources, Conservation and Recycling, 114, pp. 112â€“129. doi: 10.1016/j.resconrec.2016.07.002.
    """
    return 3.38


@component.add(
    name="INITIAL_Mo_IN_CHEMICALS",
    units="Mt",
    comp_type="Constant",
    comp_subtype="Normal",
)
def initial_mo_in_chemicals():
    """
    World 7 name was Li Air conditioning, The initial values for the Li Air conditioning stock is based on simulation outputs from the World 7 for the year 2005. The World 7 outputs are based on initial values from 1850. Source: Sverdrup, H. U. (2016) â€˜Modelling global extraction, supply, price and depletion of the extractable geological resources with the LITHIUM modelâ€™, Resources, Conservation and Recycling, 114, pp. 112â€“129. doi: 10.1016/j.resconrec.2016.07.002.
    """
    return 0.024


@component.add(
    name="INITIAL_Mo_KNOWN",
    units="Mt",
    subscripts=["Mo_Ore_GRADES_I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def initial_mo_known():
    """
    World 7 name was Li known high grade, Li known low grade, Li known ultralow grade. The initial values for the Li hidden stocks are based on simulation outputs from the World 7 for the year 2005. The World 7 outputs are based on initial values from 1850. high grade is 18,73 low grade is 4,06 ultralow grade is 0,00 Source: Sverdrup, H. U. (2016) â€˜Modelling global extraction, supply, price and depletion of the extractable geological resources with the LITHIUM modelâ€™, Resources, Conservation and Recycling, 114, pp. 112â€“129. doi: 10.1016/j.resconrec.2016.07.002.
    """
    value = xr.DataArray(
        np.nan,
        {"Mo_Ore_GRADES_I": _subscript_dict["Mo_Ore_GRADES_I"]},
        ["Mo_Ore_GRADES_I"],
    )
    value.loc[["HIGH_GRADE"]] = 0.48
    value.loc[["LOW_GRADE"]] = 4.37
    value.loc[["ULTRALOW_GRADE"]] = 10.77
    value.loc[["TRACE_GRADE"]] = 17.69
    return value


@component.add(
    name="INITIAL_Mo_MARKET", units="Mt", comp_type="Constant", comp_subtype="Normal"
)
def initial_mo_market():
    """
    World 7 name was Li Batteries, The initial values for the Li Batteries stock is based on simulation outputs from the World 7 for the year 2005. The World 7 outputs are based on initial values from 1850. Source: Sverdrup, H. U. (2016) â€˜Modelling global extraction, supply, price and depletion of the extractable geological resources with the LITHIUM modelâ€™, Resources, Conservation and Recycling, 114, pp. 112â€“129. doi: 10.1016/j.resconrec.2016.07.002.
    """
    return 1.25889


@component.add(
    name="INITIAL_Mo_SCRAP", units="Mt", comp_type="Constant", comp_subtype="Normal"
)
def initial_mo_scrap():
    """
    World 7 name was Li Effect averanger, The initial values for the Li Effect averanger stock is based on simulation outputs from the World 7 for the year 2005. The World 7 outputs are based on initial values from 1850. Source: Sverdrup, H. U. (2016) â€˜Modelling global extraction, supply, price and depletion of the extractable geological resources with the LITHIUM modelâ€™, Resources, Conservation and Recycling, 114, pp. 112â€“129. doi: 10.1016/j.resconrec.2016.07.002.
    """
    return 0.645


@component.add(
    name="Mo_change_grade",
    units="DMNL",
    subscripts=["Mo_Ore_GRADES_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={"coefficients_mo_change_grade": 9, "mo_price_per_ton": 3},
)
def mo_change_grade():
    """
    When the price exceeds the extraction cost for an ore quality, then it can be extracted with profit. Harald Sverdrup, 2021: LOCOMOTION Project report: Estimating the cost of extraction and the price required for changing between mining of different ore grades in the WORLD7 model. 20 pp.
    """
    value = xr.DataArray(
        np.nan,
        {"Mo_Ore_GRADES_I": _subscript_dict["Mo_Ore_GRADES_I"]},
        ["Mo_Ore_GRADES_I"],
    )
    value.loc[["HIGH_GRADE"]] = 1
    value.loc[["LOW_GRADE"]] = float(
        coefficients_mo_change_grade().loc["LOW_GRADE", "A_S_CURVE"]
    ) / (
        1
        + np.exp(
            -float(coefficients_mo_change_grade().loc["LOW_GRADE", "B_S_CURVE"])
            * (
                mo_price_per_ton()
                - float(coefficients_mo_change_grade().loc["LOW_GRADE", "C_S_CURVE"])
            )
        )
    )
    value.loc[["ULTRALOW_GRADE"]] = float(
        coefficients_mo_change_grade().loc["ULTRALOW_GRADE", "A_S_CURVE"]
    ) / (
        1
        + np.exp(
            -float(coefficients_mo_change_grade().loc["ULTRALOW_GRADE", "B_S_CURVE"])
            * (
                mo_price_per_ton()
                - float(
                    coefficients_mo_change_grade().loc["ULTRALOW_GRADE", "C_S_CURVE"]
                )
            )
        )
    )
    value.loc[["TRACE_GRADE"]] = float(
        coefficients_mo_change_grade().loc["TRACE_GRADE", "A_S_CURVE"]
    ) / (
        1
        + np.exp(
            -float(coefficients_mo_change_grade().loc["TRACE_GRADE", "B_S_CURVE"])
            * (
                mo_price_per_ton()
                - float(coefficients_mo_change_grade().loc["TRACE_GRADE", "C_S_CURVE"])
            )
        )
    )
    return value


@component.add(
    name="Mo_CONTENT_IN_Cu", units="DMNL", comp_type="Constant", comp_subtype="Normal"
)
def mo_content_in_cu():
    """
    Sverdrup, H., Olofsdottir, A.H., Ragnarsdottir, K.V., Koca, D., 2018. A system dynamics assessment of the supply of molybdenum and rhenium used for superalloys and specialty steels, using the WORLD6 model. Biophysical Economics and Resource Quality 4: 1-52 (DOI: 10.1007/s41247-018-0040-9)
    """
    return 0.005


@component.add(
    name="Mo_demand",
    units="Mt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco2mat_mo_demand": 1,
        "time": 1,
        "output_real": 1,
        "rate_mo_of_other_metals": 1,
        "mo_implicit_price": 1,
        "mo_modified_demand_world7": 1,
    },
)
def mo_demand():
    return if_then_else(
        np.logical_and(switch_eco2mat_mo_demand() == 1, time() >= 2015),
        lambda: (
            sum(
                output_real()
                .loc[:, "MINING_AND_MANUFACTURING_OTHER_METALS"]
                .reset_coords(drop=True)
                .rename({"REGIONS_35_I": "REGIONS_35_I!"}),
                dim=["REGIONS_35_I!"],
            )
            * rate_mo_of_other_metals()
        )
        / mo_implicit_price(),
        lambda: mo_modified_demand_world7(),
    )


@component.add(
    name="Mo_demand_per_person",
    units="Mt/Billion_persons",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"coefficients_mo_demand_per_person": 3, "time": 1},
)
def mo_demand_per_person():
    """
    Demand per person time series curve for Mo
    """
    return float(coefficients_mo_demand_per_person().loc["A_S_CURVE"]) / (
        1
        + np.exp(
            -float(coefficients_mo_demand_per_person().loc["B_S_CURVE"])
            * (time() - float(coefficients_mo_demand_per_person().loc["C_S_CURVE"]))
        )
    )


@component.add(
    name="Mo_demand_price_effect",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"coefficients_mo_demand_price_effect": 3, "mo_price_per_ton": 1},
)
def mo_demand_price_effect():
    """
    The relationship between price and demand for Mo. The response curve is similar to the ones used for Ni and Cu. Sverdrup, H., Olofsdottir, A.H., Ragnarsdottir, K.V., Koca, D., 2018. A system dynamics assessment of the supply of molybdenum and rhenium used for superalloys and specialty steels, using the WORLD6 model. Biophysical Economics and Resource Quality 4: 1-52 (DOI: 10.1007/s41247-018-0040-9)
    """
    return (
        -float(coefficients_mo_demand_price_effect().loc["A_S_CURVE"])
        / (
            1
            + np.exp(
                -float(coefficients_mo_demand_price_effect().loc["B_S_CURVE"])
                * (
                    mo_price_per_ton()
                    - float(coefficients_mo_demand_price_effect().loc["C_S_CURVE"])
                )
            )
        )
        + 1
    )


@component.add(
    name="Mo_demand_WORLD7",
    units="Mt/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "mo_demand_per_person": 1,
        "imv_global_population": 1,
        "coefficient_mo_demand": 1,
        "mo_first_speculation": 1,
        "imv_mo_second_speculation": 1,
        "imv_ss_mo_demand": 1,
    },
)
def mo_demand_world7():
    """
    Global Mo demand as dependent on GDP and populations Sverdrup, H. and Ragnarsdottir, K.V., 2014. Natural Resources in a planetary perspective. Geochemical Perspectives Vol. 3, number 2, October issue 2014. 2:129-341. European Geochemical Society. Open access
    """
    return (
        mo_demand_per_person() * imv_global_population() * coefficient_mo_demand()
        + mo_first_speculation()
        + imv_mo_second_speculation()
        + imv_ss_mo_demand()
    )


@component.add(
    name="Mo_diluted_to_stainless_steel",
    units="Mt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"mo_scrap": 1, "mo_retention_time": 1},
)
def mo_diluted_to_stainless_steel():
    """
    Amount Mo not recyled as Mo but lost into scrap iron
    """
    return mo_scrap() / mo_retention_time()


@component.add(
    name="Mo_extraction_rate_coefficient",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "mo_mining_coefficient": 1,
        "mo_profit_effect_on_mining": 1,
        "superalloys_technology_progress": 1,
        "mo_mining_efficiency_curve": 1,
    },
)
def mo_extraction_rate_coefficient():
    """
    Extraction rate which has been adapted to reflect the relationship between extraction rate and known reseves in 2005. Sverdrup, H., Olofsdottir, A.H., Ragnarsdottir, K.V., Koca, D., 2018. A system dynamics assessment of the supply of molybdenum and rhenium used for superalloys and specialty steels, using the WORLD6 model. Biophysical Economics and Resource Quality 4: 1-52 (DOI: 10.1007/s41247-018-0040-9)
    """
    return (
        mo_mining_coefficient()
        * mo_profit_effect_on_mining()
        * superalloys_technology_progress()
        * mo_mining_efficiency_curve()
    )


@component.add(
    name="Mo_EXTRACTION_RATE_HIST",
    units="Mt/Years",
    comp_type="Auxiliary",
    comp_subtype="with Lookup",
    depends_on={"time": 1},
)
def mo_extraction_rate_hist():
    """
    USGS Mineral Commodities Summaries DS-140 series, downloaded from their website. Annual updates available Sverdrup, H. and Ragnarsdottir, K.V., 2014. Natural Resources in a planetary perspective. Geochemical Perspectives Vol. 3, number 2, October issue 2014. 2:129-341. European Geochemical Society. Open access
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
        ],
        [
            1.00e01,
            2.20e01,
            4.60e01,
            1.48e02,
            6.20e01,
            9.08e01,
            9.08e01,
            9.08e01,
            1.36e02,
            9.10e01,
            9.10e01,
            9.10e01,
            1.81e02,
            9.10e01,
            1.36e02,
            2.72e02,
            4.54e02,
            5.90e02,
            8.16e02,
            4.08e02,
            1.81e02,
            4.50e01,
            4.50e01,
            1.36e02,
            2.72e02,
            6.80e02,
            8.16e02,
            1.22e03,
            1.72e03,
            2.00e03,
            1.91e03,
            1.59e03,
            1.32e03,
            2.99e03,
            5.13e03,
            6.53e03,
            9.03e03,
            1.48e04,
            1.64e04,
            1.56e04,
            1.74e04,
            2.03e04,
            2.90e04,
            3.16e04,
            2.15e04,
            1.63e04,
            1.08e04,
            1.40e04,
            1.36e04,
            1.14e04,
            1.45e04,
            2.03e04,
            2.26e04,
            2.84e04,
            2.97e04,
            3.40e04,
            3.19e04,
            3.46e04,
            2.62e04,
            3.24e04,
            4.04e04,
            3.36e04,
            2.69e04,
            3.40e04,
            3.53e04,
            4.47e04,
            5.67e04,
            6.43e04,
            6.57e04,
            7.23e04,
            8.23e04,
            7.76e04,
            7.93e04,
            8.17e04,
            8.42e04,
            8.18e04,
            8.87e04,
            9.51e04,
            1.00e05,
            1.04e05,
            1.11e05,
            1.09e05,
            9.50e04,
            6.38e04,
            9.77e04,
            9.84e04,
            9.32e04,
            9.95e04,
            1.13e05,
            1.36e05,
            1.27e05,
            1.15e05,
            1.14e05,
            9.92e04,
            1.08e05,
            1.36e05,
            1.27e05,
            1.38e05,
            1.35e05,
            1.29e05,
            1.35e05,
            1.32e05,
            1.22e05,
            1.31e05,
            1.59e05,
            1.86e05,
            1.86e05,
            2.12e05,
            2.21e05,
            2.21e05,
            2.45e05,
            2.69e05,
            2.58e05,
            2.58e05,
            2.64e05,
        ],
    )


@component.add(
    name="Mo_EXTRACTION_RATE_HISTORICAL",
    units="Mt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"mo_extraction_rate_hist": 1},
)
def mo_extraction_rate_historical():
    """
    USGS Mineral Commodities Summaries DS-140 series, downloaded from their website. Annual updates available Sverdrup, H. and Ragnarsdottir, K.V., 2014. Natural Resources in a planetary perspective. Geochemical Perspectives Vol. 3, number 2, October issue 2014. 2:129-341. European Geochemical Society. Open access
    """
    return mo_extraction_rate_hist() / 1000000.0


@component.add(
    name="Mo_filter_profit",
    units="M$",
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_mo_filter_profit": 1},
    other_deps={
        "_integ_mo_filter_profit": {
            "initial": {"initial_mo_filter_profit": 1},
            "step": {"mo_price_signal_in": 1, "mo_profit_signal_out": 1},
        }
    },
)
def mo_filter_profit():
    """
    averager
    """
    return _integ_mo_filter_profit()


_integ_mo_filter_profit = Integ(
    lambda: mo_price_signal_in() - mo_profit_signal_out(),
    lambda: initial_mo_filter_profit(),
    "_integ_mo_filter_profit",
)


@component.add(
    name="Mo_FIRST_SPECULATION",
    units="Mt/Years",
    comp_type="Auxiliary",
    comp_subtype="with Lookup",
    depends_on={"time": 1},
)
def mo_first_speculation():
    """
    Metal trader informal information Sverdrup, H., Olofsdottir, A.H., Ragnarsdottir, K.V., Koca, D., 2018. A system dynamics assessment of the supply of molybdenum and rhenium used for superalloys and specialty steels, using the WORLD6 model. Biophysical Economics and Resource Quality 4: 1-52 (DOI: 10.1007/s41247-018-0040-9)
    """
    return np.interp(
        time(),
        [
            1970.0,
            1970.07,
            1970.13,
            1970.2,
            1970.27,
            1970.33,
            1970.4,
            1970.47,
            1970.53,
            1970.6,
            1970.67,
            1970.73,
            1970.8,
            1970.87,
            1970.93,
            1971.0,
            1971.07,
            1971.13,
            1971.2,
            1971.27,
            1971.33,
            1971.4,
            1971.47,
            1971.53,
            1971.6,
            1971.67,
            1971.73,
            1971.8,
            1971.87,
            1971.93,
            1972.0,
            1972.07,
            1972.13,
            1972.2,
            1972.27,
            1972.33,
            1972.4,
            1972.47,
            1972.53,
            1972.6,
            1972.67,
            1972.73,
            1972.8,
            1972.87,
            1972.93,
            1973.0,
            1973.07,
            1973.13,
            1973.2,
            1973.27,
            1973.33,
            1973.4,
            1973.47,
            1973.53,
            1973.6,
            1973.67,
            1973.73,
            1973.8,
            1973.87,
            1973.93,
            1974.0,
            1974.07,
            1974.13,
            1974.2,
            1974.27,
            1974.33,
            1974.4,
            1974.47,
            1974.53,
            1974.6,
            1974.67,
            1974.73,
            1974.8,
            1974.87,
            1974.93,
            1975.0,
            1975.07,
            1975.13,
            1975.2,
            1975.27,
            1975.33,
            1975.4,
            1975.47,
            1975.53,
            1975.6,
            1975.67,
            1975.73,
            1975.8,
            1975.87,
            1975.93,
            1976.0,
            1976.07,
            1976.13,
            1976.2,
            1976.27,
            1976.33,
            1976.4,
            1976.47,
            1976.53,
            1976.6,
            1976.67,
            1976.73,
            1976.8,
            1976.87,
            1976.93,
            1977.0,
            1977.07,
            1977.13,
            1977.2,
            1977.27,
            1977.33,
            1977.4,
            1977.47,
            1977.53,
            1977.6,
            1977.67,
            1977.73,
            1977.8,
            1977.87,
            1977.93,
            1978.0,
            1978.07,
            1978.13,
            1978.2,
            1978.27,
            1978.33,
            1978.4,
            1978.47,
            1978.53,
            1978.6,
            1978.67,
            1978.73,
            1978.8,
            1978.87,
            1978.93,
            1979.0,
            1979.07,
            1979.13,
            1979.2,
            1979.27,
            1979.33,
            1979.4,
            1979.47,
            1979.53,
            1979.6,
            1979.67,
            1979.73,
            1979.8,
            1979.87,
            1979.93,
            1980.0,
            1980.07,
            1980.13,
            1980.2,
            1980.27,
            1980.33,
            1980.4,
            1980.47,
            1980.53,
            1980.6,
            1980.67,
            1980.73,
            1980.8,
            1980.87,
            1980.93,
            1981.0,
            1981.07,
            1981.13,
            1981.2,
            1981.27,
            1981.33,
            1981.4,
            1981.47,
            1981.53,
            1981.6,
            1981.67,
            1981.73,
            1981.8,
            1981.87,
            1981.93,
            1982.0,
            1982.07,
            1982.13,
            1982.2,
            1982.27,
            1982.33,
            1982.4,
            1982.47,
            1982.53,
            1982.6,
            1982.67,
            1982.73,
            1982.8,
            1982.87,
            1982.93,
            1983.0,
            1983.07,
            1983.13,
            1983.2,
            1983.27,
            1983.33,
            1983.4,
            1983.47,
            1983.53,
            1983.6,
            1983.67,
            1983.73,
            1983.8,
            1983.87,
            1983.93,
            1984.0,
            1984.07,
            1984.13,
            1984.2,
            1984.27,
            1984.33,
            1984.4,
            1984.47,
            1984.53,
            1984.6,
            1984.67,
            1984.73,
            1984.8,
            1984.87,
            1984.93,
            1985.0,
            1985.07,
            1985.13,
            1985.2,
            1985.27,
            1985.33,
            1985.4,
            1985.47,
            1985.53,
            1985.6,
            1985.67,
            1985.73,
            1985.8,
            1985.87,
            1985.93,
            1986.0,
            1986.07,
            1986.13,
            1986.2,
            1986.27,
            1986.33,
            1986.4,
            1986.47,
            1986.53,
            1986.6,
            1986.67,
            1986.73,
            1986.8,
            1986.87,
            1986.93,
            1987.0,
            1987.07,
            1987.13,
            1987.2,
            1987.27,
            1987.33,
            1987.4,
            1987.47,
            1987.53,
            1987.6,
            1987.67,
            1987.73,
            1987.8,
            1987.87,
            1987.93,
            1988.0,
            1988.07,
            1988.13,
            1988.2,
            1988.27,
            1988.33,
            1988.4,
            1988.47,
            1988.53,
            1988.6,
            1988.67,
            1988.73,
            1988.8,
            1988.87,
            1988.93,
            1989.0,
            1989.07,
            1989.13,
            1989.2,
            1989.27,
            1989.33,
            1989.4,
            1989.47,
            1989.53,
            1989.6,
            1989.67,
            1989.73,
            1989.8,
            1989.87,
            1989.93,
            1990.0,
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
            0.000643,
            0.000643,
            0.000643,
            0.001286,
            0.001286,
            0.001286,
            0.001286,
            0.001929,
            0.001929,
            0.0023,
            0.0023,
            0.0023,
            0.0023,
            0.0023,
            0.0023,
            0.0023,
            0.0023,
            0.0023,
            0.0023,
            0.00285,
            0.0034,
            0.0034,
            0.00455,
            0.0057,
            0.0063,
            0.008,
            0.008,
            0.0091,
            0.0091,
            0.01025,
            0.0114,
            0.012,
            0.0126,
            0.0149,
            0.0149,
            0.0149,
            0.01545,
            0.016,
            0.01655,
            0.1892,
            0.0229,
            0.02345,
            0.0297,
            0.1883,
            0.0331,
            0.03425,
            0.0389,
            0.0423,
            0.0423,
            0.1928,
            0.04855,
            0.0697,
            0.07145,
            0.1989,
            0.2,
            0.2,
            0.2,
            0.2,
            0.2,
            0.0743,
            0.0743,
            0.0423,
            0.1676,
            0.0389,
            0.0383,
            0.0354,
            0.024,
            0.024,
            0.0206,
            0.0865,
            0.0194,
            0.01885,
            0.0171,
            0.0126,
            0.012,
            0.008,
            0.00745,
            0.0046,
            0.0046,
            0.0046,
            0.0046,
            0.003859,
            0.001286,
            0.000643,
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
        ],
    )


@component.add(
    name="Mo_fraction_recycled_of_scrap",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"coefficients_mo_recycling_profit_drive": 3, "mo_price_per_ton": 1},
)
def mo_fraction_recycled_of_scrap():
    """
    A=1,024718121 B=5,3913E-05 C=40446,02658 Fraction of the total Mo scrap that gets to be recycled Sverdrup, H., Olofsdottir, A.H., Ragnarsdottir, K.V., Koca, D., 2018. A system dynamics assessment of the supply of molybdenum and rhenium used for superalloys and specialty steels, using the WORLD6 model. Biophysical Economics and Resource Quality 4: 1-52 (DOI: 10.1007/s41247-018-0040-9)
    """
    return float(coefficients_mo_recycling_profit_drive().loc["A_S_CURVE"]) / (
        1
        + np.exp(
            -float(coefficients_mo_recycling_profit_drive().loc["B_S_CURVE"])
            * (
                mo_price_per_ton()
                - float(coefficients_mo_recycling_profit_drive().loc["C_S_CURVE"])
            )
        )
    )


@component.add(
    name="Mo_FRACTION_TO_CHEMICALS",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="Normal",
)
def mo_fraction_to_chemicals():
    """
    allocation of mo to chemicals, here set to 30%. This may change towards less in the future, how much is not really known. Sverdrup, H., Olofsdottir, A.H., Ragnarsdottir, K.V., Koca, D., 2018. A system dynamics assessment of the supply of molybdenum and rhenium used for superalloys and specialty steels, using the WORLD6 model. Biophysical Economics and Resource Quality 4: 1-52 (DOI: 10.1007/s41247-018-0040-9)
    """
    return 0.3


@component.add(
    name="Mo_from_Cu",
    units="Mt/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "imv_cu_mined_to_mo": 1,
        "mo_content_in_cu": 1,
        "mo_yield_in_cu": 1,
        "mo_mining_efficiency_curve": 1,
    },
)
def mo_from_cu():
    """
    Sverdrup, H., Olofsdottir, A.H., Ragnarsdottir, K.V., Koca, D., 2018. A system dynamics assessment of the supply of molybdenum and rhenium used for superalloys and specialty steels, using the WORLD6 model. Biophysical Economics and Resource Quality 4: 1-52 (DOI: 10.1007/s41247-018-0040-9)
    """
    return (
        imv_cu_mined_to_mo()
        * mo_content_in_cu()
        * mo_yield_in_cu()
        * mo_mining_efficiency_curve()
    )


@component.add(
    name="Mo_from_Nickel",
    units="Mt/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "ni_total_mining": 1,
        "mo_content_in_ni": 1,
        "mo_yield_from_ni": 1,
        "mo_mining_efficiency_curve": 1,
    },
)
def mo_from_nickel():
    """
    Secondary from Nickel Sverdrup, H., Olofsdottir, A.H., Ragnarsdottir, K.V., Koca, D., 2018. A system dynamics assessment of the supply of molybdenum and rhenium used for superalloys and specialty steels, using the WORLD6 model. Biophysical Economics and Resource Quality 4: 1-52 (DOI: 10.1007/s41247-018-0040-9)
    """
    return (
        ni_total_mining()
        * mo_content_in_ni()
        * mo_yield_from_ni()
        * mo_mining_efficiency_curve()
    )


@component.add(
    name="Mo_hidden",
    units="Mt",
    subscripts=["Mo_Ore_GRADES_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_mo_hidden": 1},
    other_deps={
        "_integ_mo_hidden": {
            "initial": {"initial_mo_hidden": 1},
            "step": {"mo_hidden_to_known": 1},
        }
    },
)
def mo_hidden():
    """
    Sverdrup, H., Olofsdottir, A.H., Ragnarsdottir, K.V., Koca, D., 2018. A system dynamics assessment of the supply of molybdenum and rhenium used for superalloys and specialty steels, using the WORLD6 model. Biophysical Economics and Resource Quality 4: 1-52 (DOI: 10.1007/s41247-018-0040-9) se also Sverdrup, H. and Ragnarsdottir, K.V., 2014. Natural Resources in a planetary perspective. Geochemical Perspectives Vol. 3, number 2, October issue 2014. 2:129-341. European Geochemical Society. Open access Sverdrup, H, Olafsdottir, A.H., Ragnarsdottir, K.V., 2019., Assessing global copper, zinc and lead extraction rates, supply, price and resources using the WORLD6 integrated assessment model. Resources, Conservation and Recycling 1-26. X4 100007. https://doi.org/10.1016/j.rcrx.2019.100007. Open access publication.
    """
    return _integ_mo_hidden()


_integ_mo_hidden = Integ(
    lambda: -mo_hidden_to_known(), lambda: initial_mo_hidden(), "_integ_mo_hidden"
)


@component.add(
    name="Mo_hidden_to_known",
    units="Mt/Year",
    subscripts=["Mo_Ore_GRADES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"mo_hidden": 4, "mo_prospecting_rate": 4},
)
def mo_hidden_to_known():
    """
    Finding hidden resources to add then to known and extractable reserves Sverdrup, H., Olofsdottir, A.H., Ragnarsdottir, K.V., Koca, D., 2018. A system dynamics assessment of the supply of molybdenum and rhenium used for superalloys and specialty steels, using the WORLD6 model. Biophysical Economics and Resource Quality 4: 1-52 (DOI: 10.1007/s41247-018-0040-9)
    """
    value = xr.DataArray(
        np.nan,
        {"Mo_Ore_GRADES_I": _subscript_dict["Mo_Ore_GRADES_I"]},
        ["Mo_Ore_GRADES_I"],
    )
    value.loc[["HIGH_GRADE"]] = (
        float(mo_hidden().loc["HIGH_GRADE"]) * mo_prospecting_rate()
    )
    value.loc[["LOW_GRADE"]] = (
        float(mo_hidden().loc["LOW_GRADE"]) * mo_prospecting_rate()
    )
    value.loc[["ULTRALOW_GRADE"]] = (
        float(mo_hidden().loc["ULTRALOW_GRADE"]) * mo_prospecting_rate()
    )
    value.loc[["TRACE_GRADE"]] = (
        float(mo_hidden().loc["TRACE_GRADE"]) * mo_prospecting_rate()
    )
    return value


@component.add(
    name="Mo_IMPLICIT_PRICE",
    units="Mdollars_2015/Mt",
    comp_type="Constant",
    comp_subtype="Normal",
)
def mo_implicit_price():
    return 14800


@component.add(
    name="Mo_in_alloys",
    units="Mt",
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_mo_in_alloys": 1},
    other_deps={
        "_integ_mo_in_alloys": {
            "initial": {"initial_mo_in_alloys": 1},
            "step": {"mo_into_alloys": 1, "mo_scrap_alloys": 1},
        }
    },
)
def mo_in_alloys():
    """
    Stocks-in-use of Mo in alloys Sverdrup, H., Olofsdottir, A.H., Ragnarsdottir, K.V., Koca, D., 2018. A system dynamics assessment of the supply of molybdenum and rhenium used for superalloys and specialty steels, using the WORLD6 model. Biophysical Economics and Resource Quality 4: 1-52 (DOI: 10.1007/s41247-018-0040-9)
    """
    return _integ_mo_in_alloys()


_integ_mo_in_alloys = Integ(
    lambda: mo_into_alloys() - mo_scrap_alloys(),
    lambda: initial_mo_in_alloys(),
    "_integ_mo_in_alloys",
)


@component.add(
    name="Mo_in_chemicals",
    units="Mt",
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_mo_in_chemicals": 1},
    other_deps={
        "_integ_mo_in_chemicals": {
            "initial": {"initial_mo_in_chemicals": 1},
            "step": {"mo_into_chemicals_new": 1, "mo_used_chemicals_new": 1},
        }
    },
)
def mo_in_chemicals():
    """
    Mo chemicals in use in society
    """
    return _integ_mo_in_chemicals()


_integ_mo_in_chemicals = Integ(
    lambda: mo_into_chemicals_new() - mo_used_chemicals_new(),
    lambda: initial_mo_in_chemicals(),
    "_integ_mo_in_chemicals",
)


@component.add(
    name="Mo_into_alloys",
    units="Mt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"mo_supply_from_market": 1, "mo_fraction_to_chemicals": 1},
)
def mo_into_alloys():
    """
    Mo supplied to alloys Sverdrup, H., Olofsdottir, A.H., Ragnarsdottir, K.V., Koca, D., 2018. A system dynamics assessment of the supply of molybdenum and rhenium used for superalloys and specialty steels, using the WORLD6 model. Biophysical Economics and Resource Quality 4: 1-52 (DOI: 10.1007/s41247-018-0040-9)
    """
    return mo_supply_from_market() * (1 - mo_fraction_to_chemicals())


@component.add(
    name="Mo_into_chemicals_NEW",
    units="Mt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"mo_supply_from_market": 1, "mo_fraction_to_chemicals": 1},
)
def mo_into_chemicals_new():
    """
    Mo chemicals into use as driven by demand for it
    """
    return mo_supply_from_market() * mo_fraction_to_chemicals()


@component.add(
    name="Mo_into_market",
    units="Mt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "mo_total_extraction": 1,
        "mo_recycled": 1,
        "recycle_fraction_from_chemicals": 1,
        "mo_used_chemicals_new": 1,
    },
)
def mo_into_market():
    """
    Mo supplied to the market Sverdrup, H., Olofsdottir, A.H., Ragnarsdottir, K.V., Koca, D., 2018. A system dynamics assessment of the supply of molybdenum and rhenium used for superalloys and specialty steels, using the WORLD6 model. Biophysical Economics and Resource Quality 4: 1-52 (DOI: 10.1007/s41247-018-0040-9)
    """
    return (
        mo_total_extraction()
        + mo_recycled()
        + recycle_fraction_from_chemicals() * mo_used_chemicals_new()
    )


@component.add(
    name="Mo_known",
    units="Mt",
    subscripts=["Mo_Ore_GRADES_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_mo_known": 1},
    other_deps={
        "_integ_mo_known": {
            "initial": {"initial_mo_known": 1},
            "step": {"mo_hidden_to_known": 1, "mo_mining": 1},
        }
    },
)
def mo_known():
    """
    Sverdrup, H., Olofsdottir, A.H., Ragnarsdottir, K.V., Koca, D., 2018. A system dynamics assessment of the supply of molybdenum and rhenium used for superalloys and specialty steels, using the WORLD6 model. Biophysical Economics and Resource Quality 4: 1-52 (DOI: 10.1007/s41247-018-0040-9) see also Olafsdottir, A.H., and Sverdrup, H., 2020, System dynamics modelling of mining, supply, recycling, stocks-in-use and market price for nickel. Mining, Metallurgy & Exploration. 1-22. 10.1007/s42461-020-00370- Sverdrup, H. and Ragnarsdottir, K.V., 2014. Natural Resources in a planetary perspective. Geochemical Perspectives Vol. 3, number 2, October issue 2014. 2:129-341. European Geochemical Society. Open access
    """
    return _integ_mo_known()


_integ_mo_known = Integ(
    lambda: mo_hidden_to_known() - mo_mining(),
    lambda: initial_mo_known(),
    "_integ_mo_known",
)


@component.add(
    name="Mo_market",
    units="Mt",
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_mo_market": 1},
    other_deps={
        "_integ_mo_market": {
            "initial": {"initial_mo_market": 1},
            "step": {"mo_into_market": 1, "mo_supply_from_market": 1},
        }
    },
)
def mo_market():
    """
    Sverdrup, H., and Olafsdottir, A.H., 2019. Conceptualization and parameterization of the market price mechanism in the WORLD6 model for metals, materials and fossil fuels. Mineral Economics 1-26. Springer Nature DOI: 10.1007/s13563-019-00182-7.
    """
    return _integ_mo_market()


_integ_mo_market = Integ(
    lambda: mo_into_market() - mo_supply_from_market(),
    lambda: initial_mo_market(),
    "_integ_mo_market",
)


@component.add(
    name="Mo_mining",
    units="Mt/Year",
    subscripts=["Mo_Ore_GRADES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "mo_mining_rate": 4,
        "mo_extraction_rate_coefficient": 4,
        "mo_known": 4,
        "mo_technology_progress": 4,
        "mo_change_grade": 3,
    },
)
def mo_mining():
    """
    Sverdrup, H., Olofsdottir, A.H., Ragnarsdottir, K.V., Koca, D., 2018. A system dynamics assessment of the supply of molybdenum and rhenium used for superalloys and specialty steels, using the WORLD6 model. Biophysical Economics and Resource Quality 4: 1-52 (DOI: 10.1007/s41247-018-0040-9)
    """
    value = xr.DataArray(
        np.nan,
        {"Mo_Ore_GRADES_I": _subscript_dict["Mo_Ore_GRADES_I"]},
        ["Mo_Ore_GRADES_I"],
    )
    value.loc[["HIGH_GRADE"]] = (
        (float(mo_mining_rate().loc["HIGH_GRADE"]) + mo_extraction_rate_coefficient())
        * float(mo_known().loc["HIGH_GRADE"])
        * mo_technology_progress()
    )
    value.loc[["LOW_GRADE"]] = (
        float(mo_mining_rate().loc["LOW_GRADE"])
        * mo_extraction_rate_coefficient()
        * float(mo_known().loc["LOW_GRADE"])
        * float(mo_change_grade().loc["LOW_GRADE"])
        * mo_technology_progress()
    )
    value.loc[["ULTRALOW_GRADE"]] = (
        float(mo_mining_rate().loc["ULTRALOW_GRADE"])
        * mo_extraction_rate_coefficient()
        * float(mo_change_grade().loc["ULTRALOW_GRADE"])
        * float(mo_known().loc["ULTRALOW_GRADE"])
        * mo_technology_progress()
    )
    value.loc[["TRACE_GRADE"]] = (
        float(mo_mining_rate().loc["TRACE_GRADE"])
        * mo_extraction_rate_coefficient()
        * float(mo_known().loc["TRACE_GRADE"])
        * float(mo_change_grade().loc["TRACE_GRADE"])
        * mo_technology_progress()
    )
    return value


@component.add(
    name="Mo_mining_cost",
    units="M$/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"mo_mining_grade_costs": 4, "mo_mining": 4},
)
def mo_mining_cost():
    """
    Cost as total amount extracted times cost per ton Sverdrup, H., Olofsdottir, A.H., Ragnarsdottir, K.V., Koca, D., 2018. A system dynamics assessment of the supply of molybdenum and rhenium used for superalloys and specialty steels, using the WORLD6 model. Biophysical Economics and Resource Quality 4: 1-52 (DOI: 10.1007/s41247-018-0040-9)
    """
    return (
        float(mo_mining_grade_costs().loc["HIGH_GRADE"])
        * float(mo_mining().loc["HIGH_GRADE"])
        + float(mo_mining_grade_costs().loc["LOW_GRADE"])
        * float(mo_mining().loc["LOW_GRADE"])
        + float(mo_mining_grade_costs().loc["ULTRALOW_GRADE"])
        * float(mo_mining().loc["ULTRALOW_GRADE"])
        + float(mo_mining_grade_costs().loc["TRACE_GRADE"])
        * float(mo_mining().loc["TRACE_GRADE"])
    )


@component.add(
    name="Mo_mining_efficiency_curve",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"coefficients_mo_mining_efficiency": 3, "time": 1},
)
def mo_mining_efficiency_curve():
    """
    Mo mines like Cu and Ni. Often co-produced with Cu. Sverdrup, H., Olofsdottir, A.H., Ragnarsdottir, K.V., Koca, D., 2018. A system dynamics assessment of the supply of molybdenum and rhenium used for superalloys and specialty steels, using the WORLD6 model. Biophysical Economics and Resource Quality 4: 1-52 (DOI: 10.1007/s41247-018-0040-9) A=0,952348459 B=0,00027958 C=16438,79816
    """
    return float(coefficients_mo_mining_efficiency().loc["A_S_CURVE"]) / (
        1
        + np.exp(
            -float(coefficients_mo_mining_efficiency().loc["B_S_CURVE"])
            * (time() - float(coefficients_mo_mining_efficiency().loc["C_S_CURVE"]))
        )
    )


@component.add(
    name="Mo_MINING_GRADE_COSTS",
    units="M$/Mt",
    subscripts=["Mo_Ore_GRADES_I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def mo_mining_grade_costs():
    """
    from Sverdrup, H., Olofsdottir, A.H., Ragnarsdottir, K.V., Koca, D., 2018. A system dynamics assessment of the supply of molybdenum and rhenium used for superalloys and specialty steels, using the WORLD6 model. Biophysical Economics and Resource Quality 4: 1-52 (DOI: 10.1007/s41247-018-0040-9)
    """
    value = xr.DataArray(
        np.nan,
        {"Mo_Ore_GRADES_I": _subscript_dict["Mo_Ore_GRADES_I"]},
        ["Mo_Ore_GRADES_I"],
    )
    value.loc[["HIGH_GRADE"]] = 480
    value.loc[["LOW_GRADE"]] = 880
    value.loc[["ULTRALOW_GRADE"]] = 2180
    value.loc[["TRACE_GRADE"]] = 4280
    return value


@component.add(
    name="Mo_mining_income",
    units="M$/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"mo_total_mining": 1, "mo_price_per_ton": 1},
)
def mo_mining_income():
    """
    Income from delivered to market times price Sverdrup, H., Olofsdottir, A.H., Ragnarsdottir, K.V., Koca, D., 2018. A system dynamics assessment of the supply of molybdenum and rhenium used for superalloys and specialty steels, using the WORLD6 model. Biophysical Economics and Resource Quality 4: 1-52 (DOI: 10.1007/s41247-018-0040-9)
    """
    return mo_total_mining() * mo_price_per_ton()


@component.add(
    name="Mo_MINING_RATE",
    units="1/Years",
    subscripts=["Mo_Ore_GRADES_I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def mo_mining_rate():
    """
    Effort factors for the mining rate Sverdrup, H., Olofsdottir, A.H., Ragnarsdottir, K.V., Koca, D., 2018. A system dynamics assessment of the supply of molybdenum and rhenium used for superalloys and specialty steels, using the WORLD6 model. Biophysical Economics and Resource Quality 4: 1-52 (DOI: 10.1007/s41247-018-0040-9)
    """
    value = xr.DataArray(
        np.nan,
        {"Mo_Ore_GRADES_I": _subscript_dict["Mo_Ore_GRADES_I"]},
        ["Mo_Ore_GRADES_I"],
    )
    value.loc[["HIGH_GRADE"]] = 0.04
    value.loc[["LOW_GRADE"]] = 1.5
    value.loc[["ULTRALOW_GRADE"]] = 0.8
    value.loc[["TRACE_GRADE"]] = 0.4
    return value


@component.add(
    name="Mo_modified_demand_WORLD7",
    units="Mt/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"mo_demand_world7": 1, "mo_demand_price_effect": 1},
)
def mo_modified_demand_world7():
    """
    Applying the response curve to reduce demand at higher prices. The basic demand is derived from affluency (GDP) and global population. Sverdrup, H., Olofsdottir, A.H., Ragnarsdottir, K.V., Koca, D., 2018. A system dynamics assessment of the supply of molybdenum and rhenium used for superalloys and specialty steels, using the WORLD6 model. Biophysical Economics and Resource Quality 4: 1-52 (DOI: 10.1007/s41247-018-0040-9)
    """
    return mo_demand_world7() * mo_demand_price_effect()


@component.add(
    name="Mo_PRICE_HISTORICAL",
    units="M$/Mt",
    comp_type="Auxiliary",
    comp_subtype="with Lookup",
    depends_on={"time": 1},
)
def mo_price_historical():
    """
    USGS Mineral Commodities Summaries DS-140 series, downloaded from their website. Annual updates available Sverdrup, H. and Ragnarsdottir, K.V., 2014. Natural Resources in a planetary perspective. Geochemical Perspectives Vol. 3, number 2, October issue 2014. 2:129-341. European Geochemical Society. Open access
    """
    return np.interp(
        time(),
        [
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
            2023,
            2024,
            2025,
            2026,
            2027,
            2028,
            2029,
            2030,
            2031,
            2032,
            2033,
            2034,
            2035,
            2036,
            2037,
            2038,
            2039,
            2040,
            2041,
            2042,
            2043,
            2044,
            2045,
            2046,
            2047,
            2048,
            2049,
            2050,
            2051,
            2052,
            2053,
            2054,
            2055,
            2056,
            2057,
            2058,
            2059,
            2060,
            2061,
            2062,
            2063,
            2064,
            2065,
            2066,
            2067,
            2068,
            2069,
            2070,
            2071,
            2072,
            2073,
            2074,
            2075,
            2076,
            2077,
            2078,
            2079,
            2080,
            2081,
            2082,
            2083,
            2084,
            2085,
            2086,
            2087,
            2088,
            2089,
            2090,
            2091,
            2092,
            2093,
            2094,
            2095,
            2096,
            2097,
            2098,
            2099,
            2100,
        ],
        [
            5330,
            4780,
            7500,
            10400,
            31700,
            58500,
            44200,
            52500,
            47700,
            19600,
            26000,
            24900,
            19900,
            16000,
            22000,
            15000,
            16000,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
        ],
    )


@component.add(
    name="Mo_price_$_per_ton",
    units="M$/Mt",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"mo_market": 3, "coefficients_mo_price": 4},
)
def mo_price_per_ton():
    """
    Sverdrup, H., Olofsdottir, A.H., Ragnarsdottir, K.V., Koca, D., 2018. A system dynamics assessment of the supply of molybdenum and rhenium used for superalloys and specialty steels, using the WORLD6 model. Biophysical Economics and Resource Quality 4: 1-52 (DOI: 10.1007/s41247-018-0040-9) Sverdrup, H., and Olafsdottir, A.H., 2019. Conceptualization and parameterization of the market price mechanism in the WORLD6 model for metals, materials and fossil fuels. Mineral Economics 1-26. Springer Nature DOI: 10.1007/s13563-019-00182-7. If Mo market < 0,012 then (y = 159758*exp(-106,4*Mo market )) else y = 64533*exp(-49,42*Mo market)
    """
    return if_then_else(
        mo_market() < 0.012,
        lambda: float(coefficients_mo_price().loc["EQUATION_ONE", "A_LINEAR_LOG_FIT"])
        * np.exp(
            float(coefficients_mo_price().loc["EQUATION_ONE", "B_LINEAR_LOG_FIT"])
            * mo_market()
        ),
        lambda: float(coefficients_mo_price().loc["EQUATION_TWO", "A_LINEAR_LOG_FIT"])
        * np.exp(
            float(coefficients_mo_price().loc["EQUATION_TWO", "B_LINEAR_LOG_FIT"])
            * mo_market()
        ),
    )


@component.add(
    name="Mo_price_Signal_in",
    units="Mt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"mo_profit": 1},
)
def mo_price_signal_in():
    """
    Profit signal into filter
    """
    return mo_profit()


@component.add(
    name="Mo_profit",
    units="M$/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"mo_mining_income": 1, "mo_mining_cost": 1},
)
def mo_profit():
    """
    Profit defined as income minus costs Sverdrup, H., Olofsdottir, A.H., Ragnarsdottir, K.V., Koca, D., 2018. A system dynamics assessment of the supply of molybdenum and rhenium used for superalloys and specialty steels, using the WORLD6 model. Biophysical Economics and Resource Quality 4: 1-52 (DOI: 10.1007/s41247-018-0040-9)
    """
    return mo_mining_income() - mo_mining_cost()


@component.add(
    name="Mo_profit_effect_on_mining",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "mo_profit_signal_out": 3,
        "coefficients_mo_profit_effect_on_mining": 3,
    },
)
def mo_profit_effect_on_mining():
    """
    This function makes sure that the nickel operation runs when there is profit. If it becomes unprofitable, mining shuts down. Which is how the world works. The curve has a flat part: no mining at deficit, it rises sharply when passing zero. It has a gentle slope up at higher profit, reflecting that increasing up increase profitability. On the systemic level. too much production compared t demand will lower price and thus in time also profits. See also: Sverdrup, H., and Olafsdottir, A.H., 2019. Conceptualization and parameterization of the market price mechanism in the WORLD6 model for metals, materials and fossil fuels. Mineral Economics 1-26. Springer Nature DOI: 10.1007/s13563-019-00182-7.
    """
    return if_then_else(
        np.logical_or(mo_profit_signal_out() < 0, mo_profit_signal_out() == 0),
        lambda: 0,
        lambda: float(coefficients_mo_profit_effect_on_mining().loc["A_S_CURVE"])
        / (
            1
            + np.exp(
                -float(coefficients_mo_profit_effect_on_mining().loc["B_S_CURVE"])
                * (
                    mo_profit_signal_out()
                    - float(coefficients_mo_profit_effect_on_mining().loc["C_S_CURVE"])
                )
            )
        ),
    )


@component.add(
    name="Mo_profit_signal_out",
    units="Mt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"mo_filter_profit": 1, "averaging_profit_signal": 1},
)
def mo_profit_signal_out():
    """
    Filtering the profit signal to take away noise
    """
    return mo_filter_profit() / averaging_profit_signal()


@component.add(
    name="Mo_prospecting_rate",
    units="1/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"coefficients_mo_prospecting_rate": 3, "time": 1},
)
def mo_prospecting_rate():
    """
    The rate of prospecting to find unknown resources and make thenm known and extractable reserves. Sverdrup, H., Olofsdottir, A.H., Ragnarsdottir, K.V., Koca, D., 2018. A system dynamics assessment of the supply of molybdenum and rhenium used for superalloys and specialty steels, using the WORLD6 model. Biophysical Economics and Resource Quality 4: 1-52 (DOI: 10.1007/s41247-018-0040-9)
    """
    return float(coefficients_mo_prospecting_rate().loc["A_S_CURVE"]) / (
        1
        + np.exp(
            -float(coefficients_mo_prospecting_rate().loc["B_S_CURVE"])
            * (time() - float(coefficients_mo_prospecting_rate().loc["C_S_CURVE"]))
        )
    )


@component.add(
    name="Mo_recycled",
    units="Mt/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "mo_fraction_recycled_of_scrap": 1,
        "mo_scrap_alloys": 1,
        "superalloys_technology_progress": 1,
    },
)
def mo_recycled():
    """
    Mo actually recycled back to the market
    """
    return (
        mo_fraction_recycled_of_scrap()
        * mo_scrap_alloys()
        * superalloys_technology_progress()
    )


@component.add(
    name="Mo_scrap",
    units="Mt",
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_mo_scrap": 1},
    other_deps={
        "_integ_mo_scrap": {
            "initial": {"initial_mo_scrap": 1},
            "step": {"mo_scrapping_mo": 1, "mo_diluted_to_stainless_steel": 1},
        }
    },
)
def mo_scrap():
    """
    Mo scrap remaining that is recycled with scrap iron and thus in principle lost as Mo
    """
    return _integ_mo_scrap()


_integ_mo_scrap = Integ(
    lambda: mo_scrapping_mo() - mo_diluted_to_stainless_steel(),
    lambda: initial_mo_scrap(),
    "_integ_mo_scrap",
)


@component.add(
    name="Mo_scrap_alloys",
    units="Mt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"mo_in_alloys": 1, "mo_retention_time": 1},
)
def mo_scrap_alloys():
    """
    Mo alloys being scrapped after ended use
    """
    return mo_in_alloys() / mo_retention_time()


@component.add(
    name="mo_scrapping_Mo",
    units="Mt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"mo_scrap_alloys": 1, "mo_fraction_recycled_of_scrap": 1},
)
def mo_scrapping_mo():
    """
    Incoming scrap of Mo, minus the amount being taken straight to recycling. This is mostly as valuable specialty alloys. Sverdrup, H., Olofsdottir, A.H., Ragnarsdottir, K.V., Koca, D., 2018. A system dynamics assessment of the supply of molybdenum and rhenium used for superalloys and specialty steels, using the WORLD6 model. Biophysical Economics and Resource Quality 4: 1-52 (DOI: 10.1007/s41247-018-0040-9)
    """
    return mo_scrap_alloys() * (1 - mo_fraction_recycled_of_scrap())


@component.add(
    name="Mo_supply_from_market",
    units="Mt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"mo_demand": 1},
)
def mo_supply_from_market():
    """
    supplied to society Sverdrup, H., Olofsdottir, A.H., Ragnarsdottir, K.V., Koca, D., 2018. A system dynamics assessment of the supply of molybdenum and rhenium used for superalloys and specialty steels, using the WORLD6 model. Biophysical Economics and Resource Quality 4: 1-52 (DOI: 10.1007/s41247-018-0040-9)
    """
    return mo_demand()


@component.add(
    name="Mo_technology_progress",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"coefficients_mo_technology_progress": 3, "time": 1},
)
def mo_technology_progress():
    """
    Technology learning curve analogous with what was done for Cu and Ni. Mo mines like Ni and Cu and is often co-extracted with copper. Sverdrup, H., Olofsdottir, A.H., Ragnarsdottir, K.V., Koca, D., 2018. A system dynamics assessment of the supply of molybdenum and rhenium used for superalloys and specialty steels, using the WORLD6 model. Biophysical Economics and Resource Quality 4: 1-52 (DOI: 10.1007/s41247-018-0040-9)
    """
    return float(coefficients_mo_technology_progress().loc["A_S_CURVE"]) / (
        1
        + np.exp(
            -float(coefficients_mo_technology_progress().loc["B_S_CURVE"])
            * (time() - float(coefficients_mo_technology_progress().loc["C_S_CURVE"]))
        )
    )


@component.add(
    name="Mo_total_extraction",
    units="Mt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"mo_from_cu": 1, "mo_total_mining": 1, "mo_from_nickel": 1},
)
def mo_total_extraction():
    """
    Summing up all extraction
    """
    return mo_from_cu() + mo_total_mining() + mo_from_nickel()


@component.add(
    name="Mo_total_mining",
    units="Mt/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"mo_mining": 4},
)
def mo_total_mining():
    """
    Total Mo mining Sverdrup, H., Olofsdottir, A.H., Ragnarsdottir, K.V., Koca, D., 2018. A system dynamics assessment of the supply of molybdenum and rhenium used for superalloys and specialty steels, using the WORLD6 model. Biophysical Economics and Resource Quality 4: 1-52 (DOI: 10.1007/s41247-018-0040-9)
    """
    return (
        float(mo_mining().loc["HIGH_GRADE"])
        + float(mo_mining().loc["LOW_GRADE"])
        + float(mo_mining().loc["ULTRALOW_GRADE"])
        + float(mo_mining().loc["TRACE_GRADE"])
    )


@component.add(
    name="Mo_used_chemicals",
    units="Mt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"mo_in_chemicals": 1, "chemical_retention_time": 1},
)
def mo_used_chemicals():
    """
    Discharge of used chemicals
    """
    return mo_in_chemicals() / chemical_retention_time()


@component.add(
    name="Mo_used_chemicals_NEW",
    units="Mt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"mo_in_chemicals": 1, "chemical_retention_time": 1},
)
def mo_used_chemicals_new():
    """
    Discharge of used chemicals
    """
    return mo_in_chemicals() / chemical_retention_time()


@component.add(
    name="Mo_YIELD_FROM_Ni", units="DMNL", comp_type="Constant", comp_subtype="Normal"
)
def mo_yield_from_ni():
    """
    Sverdrup, H., Olofsdottir, A.H., Ragnarsdottir, K.V., Koca, D., 2018. A system dynamics assessment of the supply of molybdenum and rhenium used for superalloys and specialty steels, using the WORLD6 model. Biophysical Economics and Resource Quality 4: 1-52 (DOI: 10.1007/s41247-018-0040-9)
    """
    return 0.75


@component.add(
    name="RATE_Mo_OF_OTHER_METALS",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="Normal",
)
def rate_mo_of_other_metals():
    return 1


@component.add(
    name="superalloys_technology_progress",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"coefficients_superalloys_technology_progress": 3, "time": 1},
)
def superalloys_technology_progress():
    """
    From a paper to be published in 2021
    """
    return float(coefficients_superalloys_technology_progress().loc["A_S_CURVE"]) / (
        1
        + np.exp(
            -float(coefficients_superalloys_technology_progress().loc["B_S_CURVE"])
            * (
                time()
                - float(coefficients_superalloys_technology_progress().loc["C_S_CURVE"])
            )
        )
    )


@component.add(
    name="SWITCH_ECO2MAT_Mo_DEMAND",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="Normal",
)
def switch_eco2mat_mo_demand():
    """
    Intermodule links SWITCH, it can take two values: 0: the link is broken, the intermodule variable is replaced by an exogenous parameter. 1: the link between modules is operational.
    """
    return 0
