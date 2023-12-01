"""
Module materials.cu
Translated using PySD version 3.10.0
"""


@component.add(
    name="AVOID_DIVIDING_WITH_ZERO",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_avoid_dividing_with_zero"},
)
def avoid_dividing_with_zero():
    """
    this is just to avoid dividing with zero
    """
    return _ext_constant_avoid_dividing_with_zero()


_ext_constant_avoid_dividing_with_zero = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Copper",
    "AVOID_DIVIDING_WITH_ZERO",
    {},
    _root,
    {},
    "_ext_constant_avoid_dividing_with_zero",
)


@component.add(
    name="avoid_zero_Cu_market",
    units="Mt/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"cu_market": 1},
)
def avoid_zero_cu_market():
    """
    This variable is here to avoid 100% scarsity so that the market won't run empty and the whole WILIAM model stops running. This will be reavaluated in the next version.
    """
    return if_then_else(cu_market() < 1, lambda: 1, lambda: 0)


@component.add(
    name="change_Cu_grade",
    units="DMNL",
    subscripts=["ORE_GRADES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"coefficients_change_cu_grade": 14, "cu_price_per_ton_share": 8},
)
def change_cu_grade():
    """
    This variable is there to for us to compare the price to the cost of extraction for a certain ore grade. The ore grade is not extracted until the price is above the extraction cost. This is described in the McGlade and Ekins for oil, gas and coal, and many similar charts are available for copper: McGlade, C., & Ekins, P. (2015). The geographical distribution of fossil fuels unused when limiting global warming to 2Â°C. Nature, 517 (7533), 187â€“190. https://doi.org/10.1038/nature14016 Sverdrup, H, Olafsdottir, A.H., Ragnarsdottir, K.V., 2019. Assessing global copper, zinc and lead extraction rates, supply, price and resources using the WORLD6 integrated assessment model. Resources, Conservation and Recycling 1-26. X4 100007. https://doi.org/10.1016/j.rcrx.2019.100007. Gruber and Medina (2010) â€˜Global Lithium Availability: A Constraint for electric Vehiclesâ€™, April, 2010 Sverdrup, H. U. (2016) â€˜Modelling global extraction, supply, price and depletion of the extractable geological resources with the LITHIUM modelâ€™, Resources, Conservation and Recycling, 114, pp. 112â€“129. doi: 10.1016/j.resconrec.2016.07.002.
    """
    value = xr.DataArray(
        np.nan, {"ORE_GRADES_I": _subscript_dict["ORE_GRADES_I"]}, ["ORE_GRADES_I"]
    )
    value.loc[["RICH_GRADE"]] = float(
        coefficients_change_cu_grade().loc["RICH_GRADE", "A_S_CURVE_FIT"]
    )
    value.loc[["HIGH_GRADE"]] = if_then_else(
        cu_price_per_ton_share() > 0,
        lambda: float(coefficients_change_cu_grade().loc["HIGH_GRADE", "A_S_CURVE_FIT"])
        * (
            1
            - np.exp(
                -float(
                    coefficients_change_cu_grade().loc["HIGH_GRADE", "k_S_CURVE_FIT"]
                )
                * cu_price_per_ton_share()
                ** float(
                    coefficients_change_cu_grade().loc["HIGH_GRADE", "n_S_CURVE_FIT"]
                )
            )
        ),
        lambda: 0,
    )
    value.loc[["LOW_GRADE"]] = if_then_else(
        cu_price_per_ton_share() > 0,
        lambda: float(coefficients_change_cu_grade().loc["LOW_GRADE", "A_S_CURVE_FIT"])
        * (
            1
            - np.exp(
                -float(coefficients_change_cu_grade().loc["LOW_GRADE", "k_S_CURVE_FIT"])
                * cu_price_per_ton_share()
                ** float(
                    coefficients_change_cu_grade().loc["LOW_GRADE", "n_S_CURVE_FIT"]
                )
            )
        ),
        lambda: 0,
    )
    value.loc[["ULTRALOW_GRADE"]] = if_then_else(
        cu_price_per_ton_share() > 0,
        lambda: float(
            coefficients_change_cu_grade().loc["ULTRALOW_GRADE", "A_S_CURVE_FIT"]
        )
        * (
            1
            - np.exp(
                -float(
                    coefficients_change_cu_grade().loc[
                        "ULTRALOW_GRADE", "k_S_CURVE_FIT"
                    ]
                )
                * cu_price_per_ton_share()
                ** float(
                    coefficients_change_cu_grade().loc[
                        "ULTRALOW_GRADE", "n_S_CURVE_FIT"
                    ]
                )
            )
        ),
        lambda: 0,
    )
    value.loc[["TRACE_GRADE"]] = if_then_else(
        cu_price_per_ton_share() > 0,
        lambda: float(
            coefficients_change_cu_grade().loc["TRACE_GRADE", "A_S_CURVE_FIT"]
        )
        * (
            1
            - np.exp(
                -float(
                    coefficients_change_cu_grade().loc["TRACE_GRADE", "k_S_CURVE_FIT"]
                )
                * cu_price_per_ton_share()
                ** float(
                    coefficients_change_cu_grade().loc["TRACE_GRADE", "n_S_CURVE_FIT"]
                )
            )
        ),
        lambda: 0,
    )
    value.loc[["OCEANS_GRADE"]] = float(
        coefficients_change_cu_grade().loc["OCEANS_GRADE", "A_S_CURVE_FIT"]
    )
    return value


@component.add(
    name="change_Cu_mining_technology_S_curve",
    units="DMNL",
    subscripts=["ORE_GRADES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "coefficients_change_cu_mining_technology_s_curve": 12,
        "time": 3,
        "imv_start_time": 3,
    },
)
def change_cu_mining_technology_s_curve():
    """
    The "S Curve" innovation thinking is attributed to Richard Foster (1986) and made famous by Clayton Christensen in his book "The Innovator's Dilemma." In the book, Christensen discusses how each successive computer hard drive industry was disrupted. Each of these S curves represents a technology platform. Movement up an "S" curve is incremental innovation, while stepping down to a lower new "S" curve may lead to radical innovation as the new "S" curve surpasses the existing one. However, there is a risk that the lower "S" curve does not improve. Source: U.S.T., Stephen, A.G., & Novel, K. (1995). Jumping the technology S-curve. IEEE Spectrum, 32(6), 49-54. Fitting constants for an s curve Cu ocean technology y-fit=A*(1-exp(-k*t^n)) A= 0,65 k= 1,01E-08 n= 3,655207257 t = start time- time Fitting constants for an s curve for Cu mining technology trace: y-fit=A*(1-exp(-k*t^n)) A=1,34461147 k=1,15E-08 n=3,425207257 t = start time- time Fitting constants for an s curve, Cu mining technology ultra: y-fit=A*(1-exp(-k*t^n)) A= 1 k= 2,88E-10 n= 4,4 t = start time- time
    """
    value = xr.DataArray(
        np.nan, {"ORE_GRADES_I": _subscript_dict["ORE_GRADES_I"]}, ["ORE_GRADES_I"]
    )
    value.loc[["RICH_GRADE"]] = float(
        coefficients_change_cu_mining_technology_s_curve().loc[
            "RICH_GRADE", "A_S_CURVE_FIT"
        ]
    )
    value.loc[["HIGH_GRADE"]] = float(
        coefficients_change_cu_mining_technology_s_curve().loc[
            "HIGH_GRADE", "A_S_CURVE_FIT"
        ]
    )
    value.loc[["LOW_GRADE"]] = float(
        coefficients_change_cu_mining_technology_s_curve().loc[
            "LOW_GRADE", "A_S_CURVE_FIT"
        ]
    )
    value.loc[["ULTRALOW_GRADE"]] = float(
        coefficients_change_cu_mining_technology_s_curve().loc[
            "ULTRALOW_GRADE", "A_S_CURVE_FIT"
        ]
    ) * (
        1
        - np.exp(
            -float(
                coefficients_change_cu_mining_technology_s_curve().loc[
                    "ULTRALOW_GRADE", "k_S_CURVE_FIT"
                ]
            )
            * (time() - imv_start_time())
            ** float(
                coefficients_change_cu_mining_technology_s_curve().loc[
                    "ULTRALOW_GRADE", "n_S_CURVE_FIT"
                ]
            )
        )
    )
    value.loc[["TRACE_GRADE"]] = float(
        coefficients_change_cu_mining_technology_s_curve().loc[
            "TRACE_GRADE", "A_S_CURVE_FIT"
        ]
    ) * (
        1
        - np.exp(
            -float(
                coefficients_change_cu_mining_technology_s_curve().loc[
                    "TRACE_GRADE", "k_S_CURVE_FIT"
                ]
            )
            * (time() - imv_start_time())
            ** float(
                coefficients_change_cu_mining_technology_s_curve().loc[
                    "TRACE_GRADE", "n_S_CURVE_FIT"
                ]
            )
        )
    )
    value.loc[["OCEANS_GRADE"]] = float(
        coefficients_change_cu_mining_technology_s_curve().loc[
            "OCEANS_GRADE", "A_S_CURVE_FIT"
        ]
    ) * (
        1
        - np.exp(
            -float(
                coefficients_change_cu_mining_technology_s_curve().loc[
                    "OCEANS_GRADE", "k_S_CURVE_FIT"
                ]
            )
            * (time() - imv_start_time())
            ** float(
                coefficients_change_cu_mining_technology_s_curve().loc[
                    "OCEANS_GRADE", "n_S_CURVE_FIT"
                ]
            )
        )
    )
    return value


@component.add(
    name="CHILE_TOTAL_ENERGY_CONSUMPTION_OF_Cu_MINING_HISTORICAL",
    units="TJ/Years",
    comp_type="Auxiliary",
    comp_subtype="with Lookup",
    depends_on={"time": 1},
)
def chile_total_energy_consumption_of_cu_mining_historical():
    """
    Data from figure 1 in (Lagos et at al, 2018). Data is for total energy concumption of Cu mining for chile, but chile is estimated to have 30% pruduction in the world. Lagos, C., Carrasco, R., Soto, I., Fuertes, G., Alfaro, M., & Vargas, M. (2018). Predictive analysis of energy consumption in minining for making decisions. 2018 7th International Conference on Computers Communications and Control, ICCCC 2018 - Proceedings, 19, 270â€“275. https://doi.org/10.1109/ICCCC.2018.8390470
    """
    return np.interp(
        time(),
        [
            2001.0,
            2001.15,
            2001.29,
            2001.44,
            2001.58,
            2001.73,
            2001.88,
            2002.02,
            2002.17,
            2002.31,
            2002.46,
            2002.6,
            2002.75,
            2002.9,
            2003.04,
            2003.19,
            2003.33,
            2003.48,
            2003.63,
            2003.77,
            2003.92,
            2004.06,
            2004.21,
            2004.35,
            2004.5,
            2004.65,
            2004.79,
            2004.94,
            2005.08,
            2005.23,
            2005.38,
            2005.52,
            2005.67,
            2005.81,
            2005.96,
            2006.1,
            2006.25,
            2006.4,
            2006.54,
            2006.69,
            2006.83,
            2006.98,
            2007.13,
            2007.27,
            2007.42,
            2007.56,
            2007.71,
            2007.85,
            2008.0,
            2008.15,
            2008.29,
            2008.44,
            2008.58,
            2008.73,
            2008.88,
            2009.02,
            2009.17,
            2009.31,
            2009.46,
            2009.6,
            2009.75,
            2009.9,
            2010.04,
            2010.19,
            2010.33,
            2010.48,
            2010.63,
            2010.77,
            2010.92,
            2011.06,
            2011.21,
            2011.35,
            2011.5,
            2011.65,
            2011.79,
            2011.94,
            2012.08,
            2012.23,
            2012.38,
            2012.52,
            2012.67,
            2012.81,
            2012.96,
            2013.1,
            2013.25,
            2013.4,
            2013.54,
            2013.69,
            2013.83,
            2013.98,
            2014.13,
            2014.27,
            2014.42,
            2014.56,
            2014.71,
            2014.85,
            2015.0,
        ],
        [
            86191.8,
            86026.9,
            86199.6,
            86498.0,
            86639.3,
            86890.6,
            87136.6,
            87554.4,
            88445.3,
            89450.4,
            90455.4,
            91491.9,
            92496.9,
            93517.7,
            94485.1,
            95245.2,
            96030.4,
            96815.6,
            97600.8,
            98386.0,
            99227.7,
            99658.0,
            99940.7,
            100019.0,
            100286.0,
            100365.0,
            100632.0,
            100776.0,
            101027.0,
            101480.0,
            101872.0,
            102281.0,
            102673.0,
            103050.0,
            103491.0,
            104891.0,
            106741.0,
            108562.0,
            110462.0,
            112284.0,
            114090.0,
            115957.0,
            116812.0,
            117561.0,
            118252.0,
            118974.0,
            119681.0,
            120387.0,
            121218.0,
            122696.0,
            124282.0,
            125915.0,
            127501.0,
            129103.0,
            130788.0,
            132032.0,
            131631.0,
            131176.0,
            130674.0,
            130250.0,
            129810.0,
            129315.0,
            129380.0,
            130485.0,
            131647.0,
            132809.0,
            133987.0,
            135133.0,
            136380.0,
            137804.0,
            139939.0,
            142043.0,
            144132.0,
            146221.0,
            148325.0,
            150531.0,
            151578.0,
            152000.0,
            152392.0,
            152753.0,
            153256.0,
            153649.0,
            154133.0,
            154836.0,
            155831.0,
            156852.0,
            157873.0,
            158831.0,
            159852.0,
            161006.0,
            161105.0,
            161422.0,
            161516.0,
            161768.0,
            161925.0,
            162207.0,
            162436.0,
        ],
    )


@component.add(
    name="COEFFICIENTS_Cu_PRICE_ECONOMY",
    units="DMNL",
    subscripts=["LINEAR_LOG_FIT_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_coefficients_cu_price_economy"},
)
def coefficients_cu_price_economy():
    """
    Function that is used to describe the relation between demand, supply and price. If the supply is low and the demand is high, the price will be high. If demand is low and the supply is high, the price will be low. The if than else function is used for the case that the demand exceeds the supply- price artificcialy increased to a very high max. to decrease the demand via the economic model to match supply and demand again in the next timestep.IF THEN ELSE(Cu demand>Cu available DELAYED, 100000 , EXP( 8.05097+0.572903*LN(1/(1-Cu demand/Cu available DELAYED )))) Parameters derived be fitting the historical price and extraction.
    """
    return _ext_constant_coefficients_cu_price_economy()


_ext_constant_coefficients_cu_price_economy = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Copper",
    "COEFFICIENTS_Cu_PRICE_ECONOMY*",
    {"LINEAR_LOG_FIT_I": _subscript_dict["LINEAR_LOG_FIT_I"]},
    _root,
    {"LINEAR_LOG_FIT_I": _subscript_dict["LINEAR_LOG_FIT_I"]},
    "_ext_constant_coefficients_cu_price_economy",
)


@component.add(
    name="Cu_available",
    units="Mt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"cu_market": 1, "cu_market_supply": 1},
)
def cu_available():
    """
    All copper available during one year.
    """
    return cu_market() + cu_market_supply()


@component.add(
    name="Cu_available_DELAYED",
    units="Mt/Year",
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_cu_available_delayed": 1},
    other_deps={
        "_delayfixed_cu_available_delayed": {
            "initial": {"cu_available_delayed_initial": 1, "time_step": 1},
            "step": {"cu_available": 1},
        }
    },
)
def cu_available_delayed():
    """
    Copper available delayed to prevent simultaneous equations.
    """
    return _delayfixed_cu_available_delayed()


_delayfixed_cu_available_delayed = DelayFixed(
    lambda: cu_available(),
    lambda: time_step(),
    lambda: cu_available_delayed_initial(),
    time_step,
    "_delayfixed_cu_available_delayed",
)


@component.add(
    name="Cu_AVAILABLE_DELAYED_INITIAL",
    units="Mt/Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_cu_available_delayed_initial"},
)
def cu_available_delayed_initial():
    """
    Initial value that is available copper. Used to prevent simultanous equations error.
    """
    return _ext_constant_cu_available_delayed_initial()


_ext_constant_cu_available_delayed_initial = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Copper",
    "Cu_AVAILABLE_DELAYED_INITIAL",
    {},
    _root,
    {},
    "_ext_constant_cu_available_delayed_initial",
)


@component.add(
    name="Cu_BASE_PRICE_2015",
    units="$/t",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_cu_base_price_2015"},
)
def cu_base_price_2015():
    """
    4541.62 4735.72 6417.8 Price of Cu in the year 2015 of the similation.Used to calculate/adjust the nominal price for the economy module.
    """
    return _ext_constant_cu_base_price_2015()


_ext_constant_cu_base_price_2015 = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Copper",
    "Cu_BASE_PRICE_2015",
    {},
    _root,
    {},
    "_ext_constant_cu_base_price_2015",
)


@component.add(
    name="Cu_cost_grade",
    units="M$/Mt",
    subscripts=["ORE_GRADES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"cu_cost_grade_constants": 6, "cu_mining_efficiency_curve": 6},
)
def cu_cost_grade():
    """
    A lower ore grade implies that more rock must be moved to mine the copper. The implication is that a higher copper price is necessary to keep the copper production up when the ore grade declines (Sverdrup, Olafsdottir, 2019). The energy cost rise with declining copper ore grade (Gutowski et al., 2008), see figure 1 in (Sverdrup, Olafsdottir, 2019). Sverdrup, H. U., & Olafsdottir, A. H. (2019). On the long-term sustainability of copper, zinc and lead supply, using a system dynamics model. Resources, Conservation & Recycling: X, 4(100007). https://doi.org/https://doi.org/10.1016/j.rcrx.2019.100007 Gutowski, T., Wolf, M. I., Dahmus, J., & Albino, D. (2008). Analysis of Recycling Systems. Proceedings of 2008 NSF Engineering Research and Innovation Conference, Knoxville, Tennessee, 8. Metals News. (n.d.). Latest Data from SNL Metals & Mining Shows Copper Mine Production Costs Continue to Fall. Retrieved May 10, 2021, from http://www.metalsnews.com/Metals+News/MetalsNews/Al+Alper/MNNEWS985640/Late st+Data+from+SNL+Metals++Mining+Shows+Copper+Mine+Production+Costs+Continue +to+Fall.htm Webb, A. (2017). Copper Profit Margins To Continue Improving ; S&P Global Market Intelligence. https://www.spglobal.com/marketintelligence/en/news-insights/research/coppe r-profit-margins-to-continue-improving
    """
    value = xr.DataArray(
        np.nan, {"ORE_GRADES_I": _subscript_dict["ORE_GRADES_I"]}, ["ORE_GRADES_I"]
    )
    value.loc[["RICH_GRADE"]] = (
        float(cu_cost_grade_constants().loc["RICH_GRADE"])
        / cu_mining_efficiency_curve()
    )
    value.loc[["HIGH_GRADE"]] = (
        float(cu_cost_grade_constants().loc["HIGH_GRADE"])
        / cu_mining_efficiency_curve()
    )
    value.loc[["LOW_GRADE"]] = (
        float(cu_cost_grade_constants().loc["LOW_GRADE"]) / cu_mining_efficiency_curve()
    )
    value.loc[["ULTRALOW_GRADE"]] = (
        float(cu_cost_grade_constants().loc["ULTRALOW_GRADE"])
        / cu_mining_efficiency_curve()
    )
    value.loc[["TRACE_GRADE"]] = (
        float(cu_cost_grade_constants().loc["TRACE_GRADE"])
        / cu_mining_efficiency_curve()
    )
    value.loc[["OCEANS_GRADE"]] = (
        float(cu_cost_grade_constants().loc["OCEANS_GRADE"])
        / cu_mining_efficiency_curve()
    )
    return value


@component.add(
    name="Cu_cumulative_mining",
    units="Mt",
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_cu_cumulative_mining": 1},
    other_deps={
        "_integ_cu_cumulative_mining": {
            "initial": {"initial_cu_cumulative_mining": 1},
            "step": {"increase_cu_cumulative_mining": 1},
        }
    },
)
def cu_cumulative_mining():
    """
    All Cu minig counted up.The initial values for the Cu known stocks are based on simulation outputs from the world7 for the year 2005. The world7 outputs are based on initial values from 1900 that were stratified with respect to ore metal content and relative extraction cost based on yield of extraction and energy requirements. INIT Cu_cumulative_mining = 531,760136271 / Cu_cumulative_mining(t - dt) + (Cu_mining_in) * dt Source: Sverdrup, H. U., & Olafsdottir, A. H. (2019). On the long-term sustainability of copper, zinc and lead supply, using a system dynamics model. Resources, Conservation & Recycling: X, 4(100007). https://doi.org/https://doi.org/10.1016/j.rcrx.2019.100007
    """
    return _integ_cu_cumulative_mining()


_integ_cu_cumulative_mining = Integ(
    lambda: increase_cu_cumulative_mining(),
    lambda: initial_cu_cumulative_mining(),
    "_integ_cu_cumulative_mining",
)


@component.add(
    name="Cu_demand",
    units="Mt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "switch_eco2mat_cu_demand": 1,
        "switch_materials": 1,
        "historical_cu_demand": 1,
        "implicit_price_materials_cu": 1,
        "output_real": 1,
    },
)
def cu_demand():
    """
    Changed the Switch to 2015 from 2005 Demand switch
    """
    return if_then_else(
        np.logical_or(
            time() < 2015,
            np.logical_or(switch_eco2mat_cu_demand() == 0, switch_materials() == 0),
        ),
        lambda: historical_cu_demand(),
        lambda: sum(
            output_real()
            .loc[:, "MINING_AND_MANUFACTURING_COPPER"]
            .reset_coords(drop=True)
            .rename({"REGIONS_35_I": "REGIONS_35_I!"}),
            dim=["REGIONS_35_I!"],
        )
        / implicit_price_materials_cu(),
    )


@component.add(
    name="Cu_demand_brakes",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"x_values_for_cu_demand_brakes": 2, "coefficients_cu_demand_brakes": 7},
)
def cu_demand_brakes():
    """
    The variable controls the modified demand so that when the price is reasonable the variable has no effect on the demand but when the price gets higher it will modify the demand more and more. It's starts to kick in when the price is 3800 This array variable contains the constants for the fitted reversed sigmund curve. Following are the values: min 0,3 max 1 n 5 ec50 10 These are used in the equation: min+(max-min)/(1+10^(n*(log10(x)-log10(ec_50)))) This equations is the reversed S curve. It is 1 when it is close to zero and then starts to curve down when it reaches 3,8 and contiues to go down until it reaces 0,3 (min value) when x is 20. The x values are the "Cu price per ton" multiplied with 0,001 (needed to fit to the reversed S curve). Source: Sverdrup, H. U., & Olafsdottir, A. H. (2019). On the long-term sustainability of copper, zinc and lead supply, using a system dynamics model. Resources, Conservation & Recycling: X, 4(100007). https://doi.org/https://doi.org/10.1016/j.rcrx.2019.100007
    """
    return if_then_else(
        x_values_for_cu_demand_brakes() > 0,
        lambda: float(coefficients_cu_demand_brakes().loc["MIN_VALUE"])
        + (
            float(coefficients_cu_demand_brakes().loc["MAX_VALUE"])
            - float(coefficients_cu_demand_brakes().loc["MIN_VALUE"])
        )
        / (
            float(coefficients_cu_demand_brakes().loc["MAX_VALUE"])
            + float(coefficients_cu_demand_brakes().loc["EC50"])
            ** (
                float(coefficients_cu_demand_brakes().loc["N"])
                * (
                    (np.log(x_values_for_cu_demand_brakes()) / np.log(10))
                    - (
                        np.log(float(coefficients_cu_demand_brakes().loc["EC50"]))
                        / np.log(10)
                    )
                )
            )
        ),
        lambda: 1,
    )


@component.add(
    name="Cu_demand_economy",
    units="Mdollars_2015/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"output_real": 1},
)
def cu_demand_economy():
    """
    Sum of copper extraction over all regions..
    """
    return sum(
        output_real()
        .loc[:, "MINING_AND_MANUFACTURING_COPPER"]
        .reset_coords(drop=True)
        .rename({"REGIONS_35_I": "REGIONS_35_I!"}),
        dim=["REGIONS_35_I!"],
    )


@component.add(
    name='"Cu_demand_incl._semi_product_demand"',
    units="Mt/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"cu_demand": 1, "cu_demand_scaling_factor_for_semi_products": 1},
)
def cu_demand_incl_semi_product_demand():
    """
    Copper demand reported is not accounting for the Copper demand that is needed to produce the final products. With the scaling factor we account for the amount of copper that is needed for semi products. Most of this will end up as new scrap. The reported copper demand is the amount of copper that is consumed in final products. Estimation based on the Source: Loibl, A., & Tercero Espinoza, L. A. (2021). Current challenges in copper recycling: aligning insights from material flow analysis with technological research developments and industry issues in Europe and North America. Resources, Conservation and Recycling, 169(January), 105462. https://doi.org/10.1016/j.resconrec.2021.105462
    """
    return cu_demand() * cu_demand_scaling_factor_for_semi_products()


@component.add(
    name="Cu_demand_per_person_based_on_gdp",
    units='"$/persons"',
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "coefficients_cu_demand_per_person_based_on_gdp": 2,
        "imv_gdp_per_person": 1,
    },
)
def cu_demand_per_person_based_on_gdp():
    """
    old world7 name: Cu Demand per person based on GDP linear relationship between gdp per person (in $/per person) with cu demand per person in Mt/per person. This variable was a graphical variable in world7 but can be described with the following equation: y = 0,0004x + 3,55
    """
    return float(
        coefficients_cu_demand_per_person_based_on_gdp().loc["A_LINEAR_LOG_FIT"]
    ) * imv_gdp_per_person() + float(
        coefficients_cu_demand_per_person_based_on_gdp().loc["B_LINEAR_LOG_FIT"]
    )


@component.add(
    name="Cu_DEMAND_SCALING_FACTOR_FOR_SEMI_PRODUCTS",
    units="1/Year",
    comp_type="Constant",
    comp_subtype="Normal",
)
def cu_demand_scaling_factor_for_semi_products():
    """
    Factor of is used to higher the Copper demand, since copper demand is based on finial consumption (final products) does not account for the reqiured copper for semi finished products. factor derived from Source: Loibl, A., & Tercero Espinoza, L. A. (2021). Current challenges in copper recycling: aligning insights from material flow analysis with technological research developments and industry issues in Europe and North America. Resources, Conservation and Recycling, 169(January), 105462. https://doi.org/10.1016/j.resconrec.2021.105462 GET DIRECT CONSTANTS('model_parameters/materials/materials.xlsx', 'Copper', 'Cu_DEMAND_SCALING_FACTOR_FOR_SEMI_PRODUCTS')
    """
    return 1.155


@component.add(
    name="Cu_energy_use",
    units="MJ/kg*Mt/Years",
    subscripts=["ORE_GRADES_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={"coefficients_cu_energy_use": 5, "mining_cu_known_reserves": 5},
)
def cu_energy_use():
    """
    Energy required for mining and refining of different ore grades. This Variable calculates the energy that is is associatied for mining and refining from a ore grade with the amount of Cu extracted from that Ore grade.
    """
    value = xr.DataArray(
        np.nan, {"ORE_GRADES_I": _subscript_dict["ORE_GRADES_I"]}, ["ORE_GRADES_I"]
    )
    value.loc[["RICH_GRADE"]] = float(
        coefficients_cu_energy_use().loc["RICH_GRADE"]
    ) * float(mining_cu_known_reserves().loc["RICH_GRADE"])
    value.loc[["HIGH_GRADE"]] = float(
        mining_cu_known_reserves().loc["HIGH_GRADE"]
    ) * float(coefficients_cu_energy_use().loc["HIGH_GRADE"])
    value.loc[["LOW_GRADE"]] = float(
        mining_cu_known_reserves().loc["LOW_GRADE"]
    ) * float(coefficients_cu_energy_use().loc["LOW_GRADE"])
    value.loc[["ULTRALOW_GRADE"]] = float(
        mining_cu_known_reserves().loc["ULTRALOW_GRADE"]
    ) * float(coefficients_cu_energy_use().loc["ULTRALOW_GRADE"])
    value.loc[["TRACE_GRADE"]] = float(
        mining_cu_known_reserves().loc["TRACE_GRADE"]
    ) * float(coefficients_cu_energy_use().loc["TRACE_GRADE"])
    value.loc[["OCEANS_GRADE"]] = 0
    return value


@component.add(
    name="Cu_energy_use_recycling",
    units="MJ/kg*Mt/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"cu_recycled_to_cu_market": 1, "cu_energy_recycling": 1},
)
def cu_energy_use_recycling():
    """
    Energy requiered for copper recycling.
    """
    return cu_recycled_to_cu_market() * cu_energy_recycling()


@component.add(
    name="Cu_energy_use_secondary",
    units="MJ/kg*Mt/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"cu_secondary": 1, "cu_energy_secondary": 1},
)
def cu_energy_use_secondary():
    """
    Energy required for mining and refining of Cu from secondary mining and refining. This Variable calculates the energy that is is associatied for mining and refining from a secondary Cu mining with the amount of Cu extracted from secondary sources. Gutowski, T.G., Sahni, S., Allwood, M., Ashby, M.F., Worrell, E., 2016. The energy required to produce materials: constraints on energy-intensity improvements, parameters of demand. Philosophical Transactions of the Royal Society A 371: 20120003. http://dx.doi.org/10.1098/rsta.2012.0003
    """
    return cu_secondary() * cu_energy_secondary()


@component.add(
    name="Cu_EOL_RECYCLING_RATE_SP",
    units="1/Year",
    comp_type="Constant",
    comp_subtype="Normal",
)
def cu_eol_recycling_rate_sp():
    """
    Copper EOL RECYCLED rate- estimation based on source: Loibl, A., & Tercero Espinoza, L. A. (2021). Current challenges in copper recycling: aligning insights from material flow analysis with technological research developments and industry issues in Europe and North America. Resources, Conservation and Recycling, 169(January), 105462. https://doi.org/10.1016/j.resconrec.2021.105462
    """
    return 0.31


@component.add(
    name="Cu_extraction",
    units="Mt/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"cu_secondary": 1, "cu_mined": 1},
)
def cu_extraction():
    """
    Total amount of minend Cu from primary Cu and secondary Cu mining. Sverdrup, H. U., & Olafsdottir, A. H. (2019). On the long-term sustainability of copper, zinc and lead supply, using a system dynamics model. Resources, Conservation & Recycling: X, 4(100007). https://doi.org/https://doi.org/10.1016/j.rcrx.2019.100007
    """
    return cu_secondary() + cu_mined()


@component.add(
    name="Cu_extraction_coefficient",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "coefficients_cu_extraction_coefficient": 1,
        "cu_mining_efficiency_curve": 1,
        "cu_profit_push_mining": 1,
    },
)
def cu_extraction_coefficient():
    """
    This variable was named k cu mining in world7. It's a rate coefficient. A fraction of the known stock that is mined every year. Rarely more than 6%. Normally around 2% and 5% Olafsdottir, A.H., and Sverdrup, H., 2020, System dynamics modelling of mining, supply, recycling, stocks-in-use and market price for nickel. Mining, Metallurgy & Exploration. 1-22. 10.1007/s42461-020-00370- Sverdrup, H, Olafsdottir, A.H., Ragnarsdottir, K.V., 2019., Assessing global copper, zinc and lead extraction rates, supply, price and resources using the WORLD6 integrated assessment model. Resources, Conservation and Recycling 1-26. X4 100007. https://doi.org/10.1016/j.rcrx.2019.100007. Open access publication. Sverdrup, H., Olofsdottir, A.H., Ragnarsdottir, K.V., Koca, D., 2018. A system dynamics assessment of the supply of molybdenum and rhenium used for superalloys and specialty steels, using the WORLD6 model. Biophysical Economics and Resource Quality 4: 1-52 (DOI: 10.1007/s41247-018-0040-9)
    """
    return (
        coefficients_cu_extraction_coefficient()
        * cu_mining_efficiency_curve()
        * cu_profit_push_mining()
    )


@component.add(
    name="Cu_from_Ag",
    units="Mt/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "imv_ag_mining": 1,
        "cu_content_in_metals": 1,
        "unit_conversion_mt_kt": 1,
    },
)
def cu_from_ag():
    """
    This variable gives the amount of Cu that comes from mining Ag, i.e. the amount mined of Ag times the Cu content in Ag
    """
    return (
        imv_ag_mining()
        * float(cu_content_in_metals().loc["Cu_IN_Ag"])
        * unit_conversion_mt_kt()
    )


@component.add(
    name="Cu_from_Mo",
    units="Mt/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cu_content_in_metals": 1,
        "imv_mo_total_mining": 1,
        "cu_mo_mines_with_cu": 1,
    },
)
def cu_from_mo():
    """
    This variable gives the amount of Cu that comes from mining Mo, i.e. the amount mined of Mo times the Cu content in Mo
    """
    return (
        float(cu_content_in_metals().loc["Cu_IN_Mo"])
        * imv_mo_total_mining()
        * cu_mo_mines_with_cu()
    )


@component.add(
    name="Cu_from_Ni",
    units="Mt/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"imv_ni_total_mining": 1, "cu_content_in_metals": 1},
)
def cu_from_ni():
    """
    This variable gives the amount of Cu that comes from mining Ni, i.e. the amount mined of Ni times the Cu content in Ni
    """
    return imv_ni_total_mining() * float(cu_content_in_metals().loc["Cu_IN_Ni"])


@component.add(
    name="Cu_from_pgm",
    units="Mt/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "imv_pgm_from_mining": 1,
        "cu_content_in_metals": 1,
        "unit_conversion_mt_kt": 1,
    },
)
def cu_from_pgm():
    """
    WORLD7 name: Cu from PGM This variable gives the amount of Cu that comes from mining PGM, i.e. the amount mined of PGM times the Cu content in PGM
    """
    return (
        imv_pgm_from_mining()
        * float(cu_content_in_metals().loc["Cu_IN_PGM"])
        * unit_conversion_mt_kt()
    )


@component.add(
    name="Cu_from_Zn",
    units="Mt/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"cu_content_in_metals": 1, "imv_zn_mined": 1},
)
def cu_from_zn():
    """
    This variable gives the amount of Cu that comes from mining Zn, i.e. the amount mined of Zn times the Cu content in Zn
    """
    return float(cu_content_in_metals().loc["Cu_IN_Zn"]) * imv_zn_mined()


@component.add(
    name="Cu_hidden_resources",
    units="Mt",
    subscripts=["ORE_GRADES_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_cu_hidden_resources": 1},
    other_deps={
        "_integ_cu_hidden_resources": {
            "initial": {"initial_cu_hidden_resources": 1},
            "step": {"cu_hidden_resources_to_cu_known_reserves": 1},
        }
    },
)
def cu_hidden_resources():
    """
    The resources are divided into Cu known resources and Cu hidden resources, and stratified into 5 levels of ore quality; rich grade, high grade, low grade, ultra low grade and extreme low grade (trace grade) and additionally a dimension for the ocean grade is added. Cu resources move from hidden to known because of prospecting. The initial values for the cu known stocks are based on simulation outputs from the world7 for the year 2005. The world7 outputs are based on initial values from 1900 that were stratified with respect to ore metal content and relative extraction cost based on yield of extraction and energy requirements. The WILLIAM, 2005 initial values are therefore the following for the hidden resources: Rich grade is 0, high grade is 157, low grade is 538, ultralow grade is 1122, trace is 550 and oceans is 300. Source: Sverdrup, H. U., & Olafsdottir, A. H. (2019). On the long-term sustainability of copper, zinc and lead supply, using a system dynamics model. Resources, Conservation & Recycling: X, 4(100007). https://doi.org/https://doi.org/10.1016/j.rcrx.2019.100007
    """
    return _integ_cu_hidden_resources()


_integ_cu_hidden_resources = Integ(
    lambda: -cu_hidden_resources_to_cu_known_reserves(),
    lambda: initial_cu_hidden_resources(),
    "_integ_cu_hidden_resources",
)


@component.add(
    name="Cu_hidden_resources_to_Cu_known_reserves",
    units="Mt/Years",
    subscripts=["ORE_GRADES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cu_hidden_resources": 6,
        "cu_prospecting": 6,
        "cu_prospecting_rich": 1,
        "change_cu_mining_technology_s_curve": 3,
    },
)
def cu_hidden_resources_to_cu_known_reserves():
    """
    Cu moves from the hidden stocks to being known based on prospecting.
    """
    value = xr.DataArray(
        np.nan, {"ORE_GRADES_I": _subscript_dict["ORE_GRADES_I"]}, ["ORE_GRADES_I"]
    )
    value.loc[["RICH_GRADE"]] = np.maximum(
        float(cu_hidden_resources().loc["RICH_GRADE"])
        * cu_prospecting()
        * cu_prospecting_rich(),
        0,
    )
    value.loc[["HIGH_GRADE"]] = np.maximum(
        float(cu_hidden_resources().loc["HIGH_GRADE"]) * cu_prospecting(), 0
    )
    value.loc[["LOW_GRADE"]] = np.maximum(
        float(cu_hidden_resources().loc["LOW_GRADE"]) * cu_prospecting(), 0
    )
    value.loc[["ULTRALOW_GRADE"]] = np.maximum(
        float(cu_hidden_resources().loc["ULTRALOW_GRADE"])
        * cu_prospecting()
        * float(change_cu_mining_technology_s_curve().loc["ULTRALOW_GRADE"]),
        0,
    )
    value.loc[["TRACE_GRADE"]] = np.maximum(
        float(cu_hidden_resources().loc["TRACE_GRADE"])
        * cu_prospecting()
        * float(change_cu_mining_technology_s_curve().loc["TRACE_GRADE"]),
        0,
    )
    value.loc[["OCEANS_GRADE"]] = np.maximum(
        float(cu_hidden_resources().loc["OCEANS_GRADE"])
        * cu_prospecting()
        * float(change_cu_mining_technology_s_curve().loc["OCEANS_GRADE"]),
        0,
    )
    return value


@component.add(
    name="Cu_in_use_in_society",
    units="Mt",
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_cu_in_use_in_society": 1},
    other_deps={
        "_integ_cu_in_use_in_society": {
            "initial": {"initial_cu_in_use_in_society": 1},
            "step": {
                "cu_supply_to_society": 1,
                "cu_in_use_in_society_to_cu_scrapping": 1,
                "decrease_cu_in_use_in_society": 1,
            },
        }
    },
)
def cu_in_use_in_society():
    """
    Copper that is in use in different Products in society in million tons.
    """
    return _integ_cu_in_use_in_society()


_integ_cu_in_use_in_society = Integ(
    lambda: cu_supply_to_society()
    - cu_in_use_in_society_to_cu_scrapping()
    - decrease_cu_in_use_in_society(),
    lambda: initial_cu_in_use_in_society(),
    "_integ_cu_in_use_in_society",
)


@component.add(
    name="Cu_in_use_in_society_to_Cu_scrapping",
    units="Mt/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"cu_in_use_in_society": 1, "cu_scrapping_rate": 1},
)
def cu_in_use_in_society_to_cu_scrapping():
    """
    old world7 name: Cu Urban mining The outflow from the cu_in_use_in_society is the cu urban mining, it is the scrapping rate, the amount in society and an amplifier multiplied together, the amplifier servers as an insentive curve, i.e. if there is more value (higher coper price) in scrapping Cu more will be scrapped. CU_SCRAPPING_RATE_DMNL*cu_in_use_in_society*Cu_Scrapping_amplifier Cu SCRAPPING RATE*Cu in use in society*Cu scrapping amplifier
    """
    return cu_in_use_in_society() * cu_scrapping_rate()


@component.add(
    name="Cu_in_use_per_person",
    units="kg/persons",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"cu_in_use_in_society": 1, "imv_global_population": 1},
)
def cu_in_use_per_person():
    """
    the amount of Cu that is used per person Mt/(Billion persons) = kg/persons
    """
    return cu_in_use_in_society() / imv_global_population()


@component.add(
    name="Cu_income_ocean",
    units="M$",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"mining_cu_known_reserves": 1, "cu_price_economy": 1},
)
def cu_income_ocean():
    """
    The income that comes from mining in the ocean Mt/year*$/ton
    """
    return float(mining_cu_known_reserves().loc["OCEANS_GRADE"]) * cu_price_economy()


@component.add(
    name="Cu_known_reserves",
    units="Mt",
    subscripts=["ORE_GRADES_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_cu_known_reserves": 1},
    other_deps={
        "_integ_cu_known_reserves": {
            "initial": {"initial_cu_known_reserves": 1},
            "step": {
                "cu_hidden_resources_to_cu_known_reserves": 1,
                "mining_cu_known_reserves": 1,
            },
        }
    },
)
def cu_known_reserves():
    """
    World 7 name was Cu Rich, Cu Highgrade, Cu lowgrade, Cu Ultaralowgrade, Cu trace, Cu oceans The resources are divided into Cu known resources and Cu hidden resources, and stratified into 5 levels of ore quality; rich grade, high grade, low grade, ultra low grade and extreme low grade (trace grade) and additionally a dimension for the ocean grade is added. Cu resources move from hidden to known because of prospecting. The initial values for the cu known stocks are based on simulation outputs from the world7 for the year 2005. The world7 outputs are based on initial values from 1900 that were stratified with respect to ore metal content and relative extraction cost based on yield of extraction and energy requirements. The initial values for the cu known stocks are based on simulation outputs from the world7 for the year 2005. Rich grade is 2,6, high grade is 113, low grade is 826, ultralow grade is 174, trace is 15 and oceans is 0. Source: Sverdrup, H. U., & Olafsdottir, A. H. (2019). On the long-term sustainability of copper, zinc and lead supply, using a system dynamics model. Resources, Conservation & Recycling: X, 4(100007). https://doi.org/https://doi.org/10.1016/j.rcrx.2019.100007
    """
    return _integ_cu_known_reserves()


_integ_cu_known_reserves = Integ(
    lambda: cu_hidden_resources_to_cu_known_reserves() - mining_cu_known_reserves(),
    lambda: initial_cu_known_reserves(),
    "_integ_cu_known_reserves",
)


@component.add(
    name="cu_losses_during_production",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"cu_market_sales": 1, "cu_production_loss_rate": 1},
)
def cu_losses_during_production():
    """
    Losses during production and fabrication Source: Loibl, A., & Tercero Espinoza, L. A. (2021). Current challenges in copper recycling: aligning insights from material flow analysis with technological research developments and industry issues in Europe and North America. Resources, Conservation and Recycling, 169(January), 105462. https://doi.org/10.1016/j.resconrec.2021.105462
    """
    return cu_market_sales() * cu_production_loss_rate()


@component.add(
    name="Cu_market",
    units="Mt",
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_cu_market": 1},
    other_deps={
        "_integ_cu_market": {
            "initial": {"initial_cu_market": 1},
            "step": {"cu_market_supply": 1, "cu_market_sales": 1},
        }
    },
)
def cu_market():
    """
    The amount of Cu that is available in the market old world 7 name: Cu market The initial values for the cu market is based on simulation outputs from the world7 for the year 2005. The world7 outputs are based on initial values from 1900. INIT Cu_market = 2,63936501975 /Cu_market(t - dt) + (increase_cu_Market - decrease_cu_market) * dt Source: Sverdrup, H. U., & Olafsdottir, A. H. (2019). On the long-term sustainability of copper, zinc and lead supply, using a system dynamics model. Resources, Conservation & Recycling: X, 4(100007). https://doi.org/https://doi.org/10.1016/j.rcrx.2019.100007
    """
    return _integ_cu_market()


_integ_cu_market = Integ(
    lambda: cu_market_supply() - cu_market_sales(),
    lambda: initial_cu_market(),
    "_integ_cu_market",
)


@component.add(
    name="Cu_market_price_proxy",
    units="$/t",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"cu_market": 2, "coefficients_cu_market_price": 4},
)
def cu_market_price_proxy():
    """
    The price is determined by how much metal is immediately available for trade in the market. A high metal price will stimulate the mining rate through profits and with a delay, increase supply to the market, and limit demand. More supply to the market will increase the amount available for trade and that will lower the price This variable was a graphical variable in world7 and was described with the following equation in: Sverdrup, H. U., & Olafsdottir, A. H. (2019). On the long-term sustainability of copper, zinc and lead supply, using a system dynamics model. Resources, Conservation & Recycling: X, 4(100007). https://doi.org/https://doi.org/10.1016/j.rcrx.2019.100007 Copper price=2,212 * Cu-market amountÂ´^-0.57 With r^2 = 0.80 But it has been re-evaluated for a better fit with the following: -9780*LN(cu_market) + 34798
    """
    return if_then_else(
        cu_market() <= 0,
        lambda: float(coefficients_cu_market_price().loc["A_LINEAR_LOG_FIT"])
        * np.log(0.1)
        + float(coefficients_cu_market_price().loc["B_LINEAR_LOG_FIT"]),
        lambda: float(coefficients_cu_market_price().loc["A_LINEAR_LOG_FIT"])
        * np.log(cu_market())
        + float(coefficients_cu_market_price().loc["B_LINEAR_LOG_FIT"]),
    )


@component.add(
    name="Cu_market_sales",
    units="Mt/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"cu_market": 2, "cu_demand_incl_semi_product_demand": 1},
)
def cu_market_sales():
    """
    "There is a flow between the copper market and the usage of copper in society, and this flow is influenced by changes in the price of copper. The price of copper can modify the demand for copper in the market, which in turn affects the amount of copper used in society.". In the broader picture, industrial activities contribute through wages and profits to the overall disposable income in society, which in turn contributes to consumption and demand, a reinforcing loop. Sverdrup, H. U., & Olafsdottir, A. H. (2019). On the long-term sustainability of copper, zinc and lead supply, using a system dynamics model. Resources, Conservation & Recycling: X, 4(100007). https://doi.org/https://doi.org/10.1016/j.rcrx.2019.100007
    """
    return if_then_else(
        cu_market() <= 0.1,
        lambda: np.maximum(cu_market(), 0),
        lambda: cu_demand_incl_semi_product_demand(),
    )


@component.add(
    name="Cu_market_supply",
    units="Mt/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cu_extraction": 1,
        "cu_recycled_to_cu_market": 1,
        "cu_new_scrap": 1,
        "avoid_zero_cu_market": 1,
    },
)
def cu_market_supply():
    """
    The old WORLD7 name: Cu Market input Flow of all the Cu extracted and the Cu coming from recycling and Cu recovered from electronics entering the market.
    """
    return (
        cu_extraction()
        + cu_recycled_to_cu_market()
        + cu_new_scrap()
        + avoid_zero_cu_market()
    )


@component.add(
    name="Cu_MINE_PRODUCTION_HISTORICAL",
    units="ton/Years",
    comp_type="Auxiliary",
    comp_subtype="with Lookup",
    depends_on={"time": 1},
)
def cu_mine_production_historical():
    """
    Cu mine production, data from 1900-2020 Data between 2015 and 2020 was complemented with information from the statista webpage: Historical Statistics for Mineral and Material Commodities in the United States, Thomas D. Kelly and Grecia R. Matos, with major contributions provided by David A. Buckingham, Carl A. DiFrancesco, Kenneth E. Porter, and USGS mineral commodity specialists https://www.usgs.gov/centers/nmic/historical-statistics-mineral-and-materia l-commodities-united-states U.S. Geological Survey, 2013, 2017, 2018, 2020) U.S. Geological Survey, 2013, Mineral commodity summaries 2013: U.S. Geological Survey, 198 p U.S. Geological Survey, 2017, Mineral commodity summaries 2017: U.S. Geological Survey, 202 p., https://doi.org/10.3133/70180197 U.S. Geological Survey, 2018, Mineral commodity summaries 2018: U.S. Geological Survey, 200 p., https://doi.org/10.3133/70194932. U.S. Geological Survey, 2020, Mineral commodity summaries 2020: U.S. Geological Survey, 200 p., https://doi.org/10.3133/ mcs2020. ISBN
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
        ],
        [
            495000.0,
            516882.0,
            537934.0,
            559946.0,
            588765.0,
            629990.0,
            672296.0,
            709882.0,
            720059.0,
            722704.0,
            723285.0,
            738588.0,
            784345.0,
            831315.0,
            854471.0,
            876834.0,
            924916.0,
            992715.0,
            997177.0,
            970796.0,
            963129.0,
            1038470.0,
            1253320.0,
            1404420.0,
            1429060.0,
            1430000.0,
            1259550.0,
            1026230.0,
            967235.0,
            762905.0,
            667910.0,
            846228.0,
            1111060.0,
            1280490.0,
            1369090.0,
            1480000.0,
            1515810.0,
            1514040.0,
            1518240.0,
            1631990.0,
            1782490.0,
            1889280.0,
            1730000.0,
            1541720.0,
            1337120.0,
            1024530.0,
            983448.0,
            1098890.0,
            1252350.0,
            1409410.0,
            1564710.0,
            1772190.0,
            2122350.0,
            2145610.0,
            2057750.0,
            2109980.0,
            2272940.0,
            2403750.0,
            2478920.0,
            2551180.0,
            2597580.0,
            2583560.0,
            2494790.0,
            2295290.0,
            2053770.0,
            1883440.0,
            1985880.0,
            2139050.0,
            2184440.0,
            2160590.0,
            2239580.0,
            2376880.0,
            2468440.0,
            2532350.0,
            2573450.0,
            2599660.0,
            2625880.0,
            2735300.0,
            2923620.0,
            3119280.0,
            3247060.0,
            3261050.0,
            3243680.0,
            3331180.0,
            3588680.0,
            3876090.0,
            4045240.0,
            4143530.0,
            4221250.0,
            4286020.0,
            4374710.0,
            4501950.0,
            4604340.0,
            4610330.0,
            4597650.0,
            4699270.0,
            4929960.0,
            5250000.0,
            5577750.0,
            5813280.0,
            5924890.0,
            6116470.0,
            6502510.0,
            6797510.0,
            6994120.0,
            7006340.0,
            6891740.0,
            7015290.0,
            7292230.0,
            7367910.0,
            7337310.0,
            7304710.0,
            7314590.0,
            7286080.0,
            7430590.0,
            7648970.0,
            7609260.0,
            7601720.0,
            7668820.0,
            7807020.0,
            7923050.0,
            7969410.0,
            7996100.0,
            8203840.0,
            8492070.0,
            8795290.0,
            9001820.0,
            9142180.0,
            9245880.0,
            9339090.0,
            9428370.0,
            9479370.0,
            9491770.0,
            9545520.0,
            9809780.0,
            10294100.0,
            10943200.0,
            11358300.0,
            11747100.0,
            12183300.0,
            12654900.0,
            13013800.0,
            13317600.0,
            13619300.0,
            13646700.0,
            13670600.0,
            13877800.0,
            14457500.0,
            14838900.0,
            15017600.0,
            15106200.0,
            15328000.0,
            15529400.0,
            15625600.0,
            15936500.0,
            16100000.0,
            16100000.0,
            16129300.0,
            16531500.0,
            17229400.0,
            18171000.0,
            18374900.0,
            18647500.0,
            19158800.0,
            19847200.0,
            20055300.0,
            20070600.0,
            20348800.0,
            20398600.0,
            20282400.0,
            20000000.0,
        ],
    )


@component.add(
    name="Cu_MINE_PRODUCTION_HISTORICAL_MT",
    units="Mt/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"cu_mine_production_historical": 1, "unit_conversion_mt_t": 1},
)
def cu_mine_production_historical_mt():
    """
    Cu MINE PRODUCTION HISTORICAL converted to MT Cu mine production, data from 1900-2020 Data between 2015 and 2020 was complemented with information from the statista webpage: Historical Statistics for Mineral and Material Commodities in the United States, Thomas D. Kelly and Grecia R. Matos, with major contributions provided by David A. Buckingham, Carl A. DiFrancesco, Kenneth E. Porter, and USGS mineral commodity specialists https://www.usgs.gov/centers/nmic/historical-statistics-mineral-and-materia l-commodities-united-states U.S. Geological Survey, 2013, 2017, 2018, 2020) U.S. Geological Survey, 2013, Mineral commodity summaries 2013: U.S. Geological Survey, 198 p U.S. Geological Survey, 2017, Mineral commodity summaries 2017: U.S. Geological Survey, 202 p., https://doi.org/10.3133/70180197 U.S. Geological Survey, 2018, Mineral commodity summaries 2018: U.S. Geological Survey, 200 p., https://doi.org/10.3133/70194932. U.S. Geological Survey, 2020, Mineral commodity summaries 2020: U.S. Geological Survey, 200 p., https://doi.org/10.3133/ mcs2020. ISBN
    """
    return cu_mine_production_historical() * unit_conversion_mt_t()


@component.add(
    name="Cu_mined",
    units="Mt/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"mining_cu_known_reserves": 6, "cu_yields": 6},
)
def cu_mined():
    """
    Mining is the action that extracts copper from reserves and puts it to refining. The general mining rate equation from the paper referenced below and used is: rMining = kMining *mKnown * f(Technology)*g(Profit)* h(Yield) rMining is the rate of mining, kMining is the rate coefficient named "Cu extraction coefficient", mKnown is the mass of the ore body, "Cu known resources" f(Technology) is a technology factor describing mining efficiency improvement dependent on time g (Profit) is a feed-back from profit of the mining operation. h(Yield) is a rate adjustment factor to account for differences in extraction yield when the ore grade decreases. Sverdrup, H. U., & Olafsdottir, A. H. (2019). On the long-term sustainability of copper, zinc and lead supply, using a system dynamics model. Resources, Conservation & Recycling: X, 4(100007). https://doi.org/https://doi.org/10.1016/j.rcrx.2019.100007
    """
    return (
        float(mining_cu_known_reserves().loc["RICH_GRADE"])
        * float(cu_yields().loc["RICH_GRADE"])
        + float(mining_cu_known_reserves().loc["HIGH_GRADE"])
        * float(cu_yields().loc["HIGH_GRADE"])
        + float(mining_cu_known_reserves().loc["LOW_GRADE"])
        * float(cu_yields().loc["LOW_GRADE"])
        + float(mining_cu_known_reserves().loc["ULTRALOW_GRADE"])
        * float(cu_yields().loc["ULTRALOW_GRADE"])
        + float(mining_cu_known_reserves().loc["TRACE_GRADE"])
        * float(cu_yields().loc["TRACE_GRADE"])
        + float(mining_cu_known_reserves().loc["OCEANS_GRADE"])
        * float(cu_yields().loc["OCEANS_GRADE"])
    )


@component.add(
    name="Cu_mined_and_Cu_recycled_EOL",
    units="Mt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"cu_extraction": 1, "cu_recycled_to_cu_market": 1},
)
def cu_mined_and_cu_recycled_eol():
    """
    Copper recycled from EOL and Copper mined.
    """
    return cu_extraction() + cu_recycled_to_cu_market()


@component.add(
    name="Cu_mining_cost",
    units="M$/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"cu_primary_mining_cost": 6},
)
def cu_mining_cost():
    """
    world7 name: Cu primary costs This variable sums up the cost from mining primary mining of Copper from all the grades, i.e. Cu_primary_mining_cost[RICH_GRADE]+Cu_primary_mining_cost[HIGH_GRADE]+Cu_pr imary_mining_cost[LOW_GRADE]+Cu_primary_mining_cost[ULTRALOW_GRADE]+Cu_prim ary_mining_cost[TRACE_GRADE]+Cu_primary_mining_cost[OCEANS_GRADE]
    """
    return (
        float(cu_primary_mining_cost().loc["RICH_GRADE"])
        + float(cu_primary_mining_cost().loc["HIGH_GRADE"])
        + float(cu_primary_mining_cost().loc["LOW_GRADE"])
        + float(cu_primary_mining_cost().loc["ULTRALOW_GRADE"])
        + float(cu_primary_mining_cost().loc["TRACE_GRADE"])
        + float(cu_primary_mining_cost().loc["OCEANS_GRADE"])
    )


@component.add(
    name="Cu_mining_efficiency_curve",
    units="Mt",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"coefficients_cu_mining_efficiency_curve": 2, "time": 1},
)
def cu_mining_efficiency_curve():
    """
    The Cu efficiency curve was a graphical variable in the world 7 model. A variable dependent on time that is expected to increase from 1850 until simulation end. It takes the value 1 around 1940-1960 and after that it increases up to 1,4 around 2000 and is expected to increase even more after that. The For simplification the curve was fitted with a linear equation but this will be re-evaluated. =0,0089*TIME-16,315
    """
    return float(
        coefficients_cu_mining_efficiency_curve().loc["A_LINEAR_LOG_FIT"]
    ) * time() - float(
        coefficients_cu_mining_efficiency_curve().loc["B_LINEAR_LOG_FIT"]
    )


@component.add(
    name="Cu_mining_income",
    units="M$/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"cu_mined": 1, "cu_price_economy": 1},
)
def cu_mining_income():
    """
    Income from mining Copper. Mt*$/t= M$
    """
    return cu_mined() * cu_price_economy()


@component.add(
    name="Cu_mining_profits",
    units="M$/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"cu_mining_income": 1, "cu_mining_cost": 1},
)
def cu_mining_profits():
    """
    world7: Cu_mining_income-Cu_primary_costs The profitis affected by the mining cost and how that is modified with changing oil price and variations in ore grade. ? Sverdrup, H. U., & Olafsdottir, A. H. (2019). On the long-term sustainability of copper, zinc and lead supply, using a system dynamics model. Resources, Conservation & Recycling: X, 4(100007). https://doi.org/https://doi.org/10.1016/j.rcrx.2019.100007
    """
    return cu_mining_income() - cu_mining_cost()


@component.add(
    name="Cu_modified_demand",
    units="Mt/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"cu_primary_demand": 1, "cu_demand_brakes": 1},
)
def cu_modified_demand():
    """
    The price is used to modify the demand to become â€œCu market to Cu in use in society". In the broader picture, industrial activities contribute through wages and profits to the overall disposable income in society, which in turn contributes to consumption and demand, a reinforcing loop. Sverdrup, H. U., & Olafsdottir, A. H. (2019). On the long-term sustainability of copper, zinc and lead supply, using a system dynamics model. Resources, Conservation & Recycling: X, 4(100007). https://doi.org/https://doi.org/10.1016/j.rcrx.2019.100007
    """
    return cu_primary_demand() * cu_demand_brakes()


@component.add(
    name="Cu_new_scrap",
    units="Mt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"cu_market_sales": 1, "cu_rate_of_new_scrap": 1},
)
def cu_new_scrap():
    """
    Copper that is produced during the production of final products. Enters directly into market supply again as new scrap.
    """
    return cu_market_sales() * cu_rate_of_new_scrap()


@component.add(
    name="Cu_ore_grade",
    units="Mt",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "mining_cu_known_reserves": 10,
        "amount_of_cu_in_weight_of_rock": 5,
        "avoid_dividing_with_zero": 1,
    },
)
def cu_ore_grade():
    """
    This variable multiplies the amount that is mined from each with the amount of Cu in each grade. The equation in WORLD7: (Cu_Out_Rich*Cu_Rich_grade+Cu_Out_High*Cu_High_grade+Cu_Out_Low*Cu_Low_grad e+Cu_Out_Ultra_Low*Cu_Ultralow_grade+Cu_Out_trace*Cu_trac_grade)/(Cu_Out_Ri ch+Cu_Out_High+Cu_Out_Low+Cu_Out_Ultra_Low+Cu_Out_trace+0,001)
    """
    return (
        float(mining_cu_known_reserves().loc["RICH_GRADE"])
        * float(amount_of_cu_in_weight_of_rock().loc["RICH_GRADE"])
        + float(mining_cu_known_reserves().loc["HIGH_GRADE"])
        * float(amount_of_cu_in_weight_of_rock().loc["HIGH_GRADE"])
        + float(mining_cu_known_reserves().loc["LOW_GRADE"])
        * float(amount_of_cu_in_weight_of_rock().loc["LOW_GRADE"])
        + float(mining_cu_known_reserves().loc["ULTRALOW_GRADE"])
        * float(amount_of_cu_in_weight_of_rock().loc["ULTRALOW_GRADE"])
        + float(mining_cu_known_reserves().loc["TRACE_GRADE"])
        * float(amount_of_cu_in_weight_of_rock().loc["TRACE_GRADE"])
    ) / (
        float(mining_cu_known_reserves().loc["RICH_GRADE"])
        + float(mining_cu_known_reserves().loc["HIGH_GRADE"])
        + float(mining_cu_known_reserves().loc["LOW_GRADE"])
        + float(mining_cu_known_reserves().loc["ULTRALOW_GRADE"])
        + float(mining_cu_known_reserves().loc["TRACE_GRADE"])
        + avoid_dividing_with_zero()
    )


@component.add(
    name="Cu_ORE_GRADE_HISTORICAL",
    units="Mt",
    comp_type="Auxiliary",
    comp_subtype="with Lookup",
    depends_on={"time": 1},
)
def cu_ore_grade_historical():
    """
    Data from 1800-2010 The observed data are extracted (Sverdrup and Olafsdottir, 2019) from diagrams in the publications of Mudd (2009, 2010a,b, Mudd et al., 2013, MUDD and Jowirr, 2018) source: Sverdrup, H. U., & Olafsdottir, A. H. (2019). On the long-term sustainability of copper, zinc and lead supply, using a system dynamics model. Resources, Conservation & Recycling: X, 4(100007). https://doi.org/https://doi.org/10.1016/j.rcrx.2019.100007 Mudd, G. M. (2009). Historical Trends in Base Metal Mining: Backcasting to Understand the Sustainability of Mining. Proceedings of the 48th Annual Conference of Metallurgists, August Issue. Mudd, G. M. (2010a). The Environmental sustainability of mining in Australia: key mega-trends and looming constraints. Resources Policy, 35(2), 98â€“115. https://doi.org/10.1016/j.resourpol.2009.12.001 Mudd, G. M. (2010b). The Arrival of Peak Lead : Peak Environmental Impacts ? LEAD Action News, 11(1), 1â€“6. Mudd, G.M., Weng, Z., Jowitt, S.M., 2013. A detailed assessment of global Cu resource trends and endownments. Econ. Geol. 108, 1163â€“1183 Mudd, G. M., & Jowitt, S. M. (2018). Growing global copper resources, reserves and production: Discovery is not the only control on supply. Economic Geology, 113(6), 1235â€“1267. https://doi.org/10.5382/econgeo.2018.4590
    """
    return np.interp(
        time(),
        [
            1800.0,
            1801.0,
            1802.0,
            1803.0,
            1804.0,
            1805.0,
            1806.0,
            1807.0,
            1808.0,
            1809.0,
            1810.0,
            1811.0,
            1812.0,
            1813.0,
            1814.0,
            1815.0,
            1816.0,
            1817.0,
            1818.0,
            1819.0,
            1820.0,
            1821.0,
            1822.0,
            1823.0,
            1824.0,
            1825.0,
            1826.0,
            1827.0,
            1828.0,
            1829.0,
            1830.0,
            1831.0,
            1832.0,
            1833.0,
            1834.0,
            1835.0,
            1836.0,
            1837.0,
            1838.0,
            1839.0,
            1840.0,
            1841.0,
            1842.0,
            1843.0,
            1844.0,
            1845.0,
            1846.0,
            1847.0,
            1848.0,
            1849.0,
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
        ],
        [
            29.26,
            30.7936,
            19.2177,
            19.2177,
            19.4404,
            19.5578,
            19.5578,
            19.5578,
            19.5173,
            18.5131,
            18.1001,
            17.5332,
            17.3469,
            17.3469,
            17.4603,
            17.517,
            17.9381,
            18.2621,
            18.7237,
            18.8317,
            19.2177,
            19.5578,
            19.5578,
            19.5578,
            19.4121,
            19.1259,
            18.9585,
            18.4645,
            18.1973,
            18.0272,
            18.0272,
            18.0272,
            18.0272,
            18.0272,
            18.1973,
            18.3673,
            18.3673,
            18.3673,
            18.3026,
            18.0029,
            17.8571,
            17.5008,
            17.3469,
            17.3469,
            17.2093,
            16.2658,
            14.2695,
            12.504,
            12.9616,
            13.3787,
            15.7272,
            15.9864,
            15.9864,
            16.1484,
            16.1565,
            16.1565,
            16.1565,
            16.1565,
            16.1565,
            16.1565,
            16.1565,
            16.1241,
            15.9864,
            15.9864,
            15.8325,
            15.6463,
            15.6463,
            15.7515,
            16.3346,
            16.5695,
            16.7234,
            16.8367,
            16.448,
            18.2864,
            19.0962,
            17.6992,
            17.3469,
            17.3469,
            16.4723,
            15.3952,
            15.3061,
            15.3061,
            15.3061,
            15.3061,
            13.7755,
            13.6054,
            13.6054,
            13.1924,
            12.9252,
            12.4879,
            11.9048,
            11.0544,
            10.9842,
            10.3984,
            7.31292,
            7.31292,
            7.31292,
            7.31292,
            7.31292,
            6.70554,
            6.63265,
            6.63265,
            6.63265,
            6.63265,
            5.59605,
            5.27211,
            4.94817,
            4.93197,
            5.05345,
            5.19382,
            5.36119,
            5.44218,
            5.44218,
            5.40168,
            5.17493,
            5.10204,
            5.10204,
            5.24781,
            5.3369,
            5.44218,
            5.61225,
            5.61225,
            5.61225,
            5.61225,
            5.61225,
            5.95238,
            5.95238,
            5.95238,
            5.95238,
            6.29252,
            6.29252,
            6.55167,
            6.87561,
            6.97279,
            7.35342,
            7.65306,
            7.66926,
            8.31714,
            9.11079,
            8.79495,
            7.93651,
            6.97279,
            6.8918,
            6.68529,
            6.43829,
            5.57985,
            5.27211,
            5.27211,
            4.96437,
            3.91157,
            3.91157,
            3.7415,
            3.40136,
            3.23129,
            2.89116,
            2.89116,
            2.79398,
            2.72109,
            2.6806,
            2.59961,
            2.42144,
            1.92744,
            1.87075,
            1.87075,
            1.87075,
            1.82216,
            1.70068,
            1.70068,
            1.70068,
            1.70068,
            1.70068,
            1.70068,
            1.70068,
            1.70068,
            1.70068,
            1.70068,
            1.70068,
            1.50632,
            1.36054,
            1.36054,
            1.36054,
            1.36054,
            1.87075,
            1.96793,
            2.1218,
            2.38095,
            2.42954,
            2.72109,
            2.72109,
            2.72109,
            2.72109,
            2.72109,
            2.59961,
            2.55102,
            2.55102,
            2.40525,
            2.21088,
            2.17039,
            2.04082,
            2.04082,
            2.04082,
            2.04082,
            2.04082,
            2.04082,
            2.04082,
            2.04082,
            2.04082,
            2.04082,
            1.87075,
            1.70068,
            0.0,
        ],
    )


@component.add(
    name="Cu_price_economy",
    units="$/t",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cu_demand": 2,
        "cu_available_delayed": 2,
        "max_cu_price": 1,
        "coefficients_cu_price_economy": 2,
    },
)
def cu_price_economy():
    """
    Function that is used to describe the relation between demand, supply and price. If the supply is low and the demand is high, the price will be high. If demand is low and the supply is high, the price will be low. The if than else function is used for the case that the demand exceeds the supply- price artificcialy increased to a very high max. to decrease the demand via the economic model to match supply and demand again in the next timestep.IF THEN ELSE(Cu demand>Cu available DELAYED, 100000 , EXP( 8.05097+0.572903*LN(1/(1-Cu demand/Cu available DELAYED ))))
    """
    return if_then_else(
        cu_demand() > cu_available_delayed(),
        lambda: max_cu_price(),
        lambda: np.exp(
            float(coefficients_cu_price_economy().loc["A_LINEAR_LOG_FIT"])
            + float(coefficients_cu_price_economy().loc["B_LINEAR_LOG_FIT"])
            * np.log(1 / (1 - cu_demand() / cu_available_delayed()))
        ),
    )


@component.add(
    name="Cu_price_economy_adjusted",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "cu_price_index_economy": 1},
)
def cu_price_economy_adjusted():
    """
    Cu price for the years 2005 to 2015 is set to 100 as a starting value-nominal price in the economy module. After 2015- Cu price index economy. The reason for this is that the materials module is starting in 2005, and is simulating with an historical demand until 2015. The economy modules starts to simulate in the year 2015. The material module reports fixed values from 2005 to 2015 to the economy module, at 2015 dynamic values are involved in the economy module.
    """
    return if_then_else(time() <= 2015, lambda: 100, lambda: cu_price_index_economy())


@component.add(
    name="Cu_PRICE_ECONOMY_INITIAL",
    units="$/t",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_cu_price_economy_initial"},
)
def cu_price_economy_initial():
    """
    4735.72
    """
    return _ext_constant_cu_price_economy_initial()


_ext_constant_cu_price_economy_initial = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Copper",
    "Cu_PRICE_ECONOMY_INITIAL",
    {},
    _root,
    {},
    "_ext_constant_cu_price_economy_initial",
)


@component.add(
    name="Cu_PRICE_HISTORICAL",
    units="$/t",
    comp_type="Auxiliary",
    comp_subtype="with Lookup",
    depends_on={"time": 1},
)
def cu_price_historical():
    """
    Data from 2009-2019 The observed data are extracted (Sverdrup and Olafsdottir, 2019) from diagrams in the publications of Mudd (2009, 2010a,b, Mudd et al., 2013, MUDD and Jowirr, 2018, U.S. Geological Survey, 2013, 2017, 2018, 2020) source: Sverdrup, H. U., & Olafsdottir, A. H. (2019). On the long-term sustainability of copper, zinc and lead supply, using a system dynamics model. Resources, Conservation & Recycling: X, 4(100007). https://doi.org/https://doi.org/10.1016/j.rcrx.2019.100007 Mudd, G. M. (2009). Historical Trends in Base Metal Mining: Backcasting to Understand the Sustainability of Mining. Proceedings of the 48th Annual Conference of Metallurgists, August Issue. Mudd, G. M. (2010a). The Environmental sustainability of mining in Australia: key mega-trends and looming constraints. Resources Policy, 35(2), 98â€“115. https://doi.org/10.1016/j.resourpol.2009.12.001 Mudd, G. M. (2010b). The Arrival of Peak Lead : Peak Environmental Impacts ? LEAD Action News, 11(1), 1â€“6. Mudd, G.M., Weng, Z., Jowitt, S.M., 2013. A detailed assessment of global Cu resource trends and endownments. Econ. Geol. 108, 1163â€“1183 Mudd, G. M., & Jowitt, S. M. (2018). Growing global copper resources, reserves and production: Discovery is not the only control on supply. Economic Geology, 113(6), 1235â€“1267. https://doi.org/10.5382/econgeo.2018.4590 U.S. Geological Survey, 2013, Mineral commodity summaries 2013: U.S. Geological Survey, 198 p U.S. Geological Survey, 2017, Mineral commodity summaries 2017: U.S. Geological Survey, 202 p., https://doi.org/10.3133/70180197 U.S. Geological Survey, 2018, Mineral commodity summaries 2018: U.S. Geological Survey, 200 p., https://doi.org/10.3133/70194932. U.S. Geological Survey, 2020, Mineral commodity summaries 2020: U.S. Geological Survey, 200 p., https://doi.org/10.3133/ mcs2020. ISBN
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
            2018,
            2019,
        ],
        [
            7000,
            7000,
            4800,
            5300,
            5100,
            6300,
            7700,
            7700,
            5300,
            5300,
            5000,
            4900,
            6200,
            5630,
            4760,
            6180,
            9360,
            8190,
            5890,
            3780,
            3140,
            2540,
            2900,
            3100,
            2790,
            2920,
            2840,
            2690,
            3110,
            3850,
            2860,
            1980,
            1520,
            2020,
            2330,
            2330,
            2520,
            3350,
            2610,
            2900,
            2960,
            2930,
            2650,
            2500,
            2450,
            2410,
            2580,
            3420,
            3320,
            2940,
            3210,
            3400,
            3310,
            3910,
            4000,
            5040,
            5540,
            3840,
            3280,
            3820,
            3920,
            3630,
            3670,
            3640,
            3750,
            4020,
            3990,
            4100,
            4260,
            4650,
            5380,
            4620,
            4420,
            4810,
            5630,
            4290,
            4390,
            3960,
            3630,
            4570,
            4420,
            3330,
            2710,
            2760,
            2310,
            2240,
            2170,
            2610,
            3660,
            3800,
            3380,
            2890,
            2750,
            2280,
            2690,
            3260,
            2500,
            2400,
            1730,
            1640,
            1840,
            1560,
            1510,
            1670,
            2550,
            3200,
            5610,
            5680,
            5330,
            4040,
            5740,
            6490,
            5750,
            5240,
            4830,
            4290,
            5900,
            6450,
            6106,
            6323,
        ],
    )


@component.add(
    name="Cu_price_index_economy",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_mat2eco_cu_price": 1,
        "price_transformation": 1,
        "cu_base_price_2015": 1,
        "estimated_price_with_tax_metals": 1,
    },
)
def cu_price_index_economy():
    """
    Calculation of the Cu price index economy based on the price of Cu price economy test divided by the base price for the starting year of the economy module (2015) the result should be in the first year (2015) = 1 and then multiplied with hundered. This is the nominal price signal used in the economy module. With changes of the Cu price economy test variable which will be depending on the supply and demand situation changes in the nominal price will occour. previous version: (Cu price economy test/Cu base price 2015)*PERCENT PRICE TRANSFORMATION
    """
    return if_then_else(
        switch_mat2eco_cu_price() == 0,
        lambda: 100,
        lambda: (
            float(estimated_price_with_tax_metals().loc["Cu_W"]) / cu_base_price_2015()
        )
        * price_transformation(),
    )


@component.add(
    name="Cu_price_per_ton",
    units="$/t",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"cu_market_price_proxy": 1},
)
def cu_price_per_ton():
    """
    The price is determined by how much metal is immediately available for trade in the market. A high metal price will stimulate the mining rate through profits and with a delay, increase supply to the market, and limit demand. More supply to the market will increase the amount available for trade and that will lower the price This is the price per ton Sverdrup, H. U., & Olafsdottir, A. H. (2019). On the long-term sustainability of copper, zinc and lead supply, using a system dynamics model. Resources, Conservation & Recycling: X, 4(100007). https://doi.org/https://doi.org/10.1016/j.rcrx.2019.100007
    """
    return cu_market_price_proxy()


@component.add(
    name="Cu_price_per_ton_share",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"share_of_cu_price": 1, "delayed_cu_price_economy_adjusted_test": 1},
)
def cu_price_per_ton_share():
    """
    This is just one percent of the price that is only used as part of the equations used to calculate the switch between ore grades.
    """
    return share_of_cu_price() * delayed_cu_price_economy_adjusted_test()


@component.add(
    name="Cu_primary_demand",
    units="Mt/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "coefficients_cu_primary_demand": 1,
        "decrease_cu_demand_delay": 1,
        "imv_cu_all_vehicle_demand": 1,
    },
)
def cu_primary_demand():
    """
    world7 old name Cu primary demand Calculation of the primary demand before the price iseffecting the demand. The demand is taken from the market, and when the market amount decrease, then the prices increase. The higher prices push mining, causing the price to decrease. The source: Sverdrup, H. U., Olafsdottir, A. H., & Ragnarsdottir, K. V. (2019). On the long-term sustainability of copper, zinc and lead supply, using a system dynamics model. Resources, Conservation and Recycling: X, 4, 100007. https://doi.org/10.1016/j.rcrx.2019.100007
    """
    return (
        coefficients_cu_primary_demand() * decrease_cu_demand_delay()
        + imv_cu_all_vehicle_demand()
    )


@component.add(
    name="Cu_primary_mining_cost",
    units="M$/Year",
    subscripts=["ORE_GRADES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"mining_cu_known_reserves": 1, "cu_cost_grade": 1},
)
def cu_primary_mining_cost():
    """
    Cost for copper mining from different ore grades from primary mining.
    """
    return mining_cu_known_reserves() * cu_cost_grade()


@component.add(
    name="CU_PRODUCTION_LOSS_RATE",
    units="1/Year",
    comp_type="Constant",
    comp_subtype="Normal",
)
def cu_production_loss_rate():
    """
    Rate of copper per year that is lost during the production and fabrication on the step from copper to semi product to final products. Source: Loibl, A., & Tercero Espinoza, L. A. (2021). Current challenges in copper recycling: aligning insights from material flow analysis with technological research developments and industry issues in Europe and North America. Resources, Conservation and Recycling, 169(January), 105462. https://doi.org/10.1016/j.resconrec.2021.105462 GET DIRECT CONSTANTS('model_parameters/materials/materials.xlsx', 'Copper', 'CU_PRODUCTION_LOSS_RATE')
    """
    return 0.01


@component.add(
    name="Cu_profit_ocean",
    units="M$",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"cu_income_ocean": 1, "cu_primary_mining_cost": 1},
)
def cu_profit_ocean():
    """
    The profit from mining in the ocean eqauls the incom - cost world 7: Cu_income_ocean-Cu_mining_cost_ocean
    """
    return cu_income_ocean() - float(cu_primary_mining_cost().loc["OCEANS_GRADE"])


@component.add(
    name="Cu_profit_push_mining",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cu_profit_push_mining_polynomal_fit": 7,
        "decrease_delayed_ts_cu_profit": 6,
    },
)
def cu_profit_push_mining():
    """
    g (Profit), or Cu profit push mining, is a feed-back from profit of the mining operation. Sverdrup, H. U., & Olafsdottir, A. H. (2019). On the long-term sustainability of copper, zinc and lead supply, using a system dynamics model. Resources, Conservation & Recycling: X, 4(100007). https://doi.org/https://doi.org/10.1016/j.rcrx.2019.100007 This variable was a graphic variable in world7 but has now been fitted with the polynomal: y = 2E-32x^6 + 5E-27x^5 - 2E-21x^4 - 4E-16x^3 + 4E-11x^2 + 1E-05^x + 0,3732
    """
    return (
        float(cu_profit_push_mining_polynomal_fit().loc["SIXTH_ORDER_FIT"])
        * decrease_delayed_ts_cu_profit() ** 6
        + float(cu_profit_push_mining_polynomal_fit().loc["FIFTH_ORDER_FIT"])
        * decrease_delayed_ts_cu_profit() ** 5
        - float(cu_profit_push_mining_polynomal_fit().loc["FOURTH_ORDER_FIT"])
        * decrease_delayed_ts_cu_profit() ** 4
        - float(cu_profit_push_mining_polynomal_fit().loc["THIRD_ORDER_FIT"])
        * decrease_delayed_ts_cu_profit() ** 3
        + float(cu_profit_push_mining_polynomal_fit().loc["SECOND_ORDER_FIT"])
        * decrease_delayed_ts_cu_profit() ** 2
        + float(cu_profit_push_mining_polynomal_fit().loc["FIRST_ORDER_FIT"])
        * decrease_delayed_ts_cu_profit()
        + float(cu_profit_push_mining_polynomal_fit().loc["ZERO_ORDER_FIT"])
    )


@component.add(
    name="Cu_profit_push_ocean",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "coefficients_cu_profit_push_ocean": 3,
        "fraction_of_the_decrease_cu_ocean_profit_delay": 1,
    },
)
def cu_profit_push_ocean():
    """
    g (Profit) or profit push ocean is a feed-back from profit of the mining operation. This variable was a graphical variable in world7 but has been fitted to a s curver equation with: y-fit=A*(1-exp(-k*t^n)): A=1,46121186 k=9,43E-02 n=0,67837078 and x = decrease cu ocean profit delay * 0,001 Sverdrup, H. U., & Olafsdottir, A. H. (2019). On the long-term sustainability of copper, zinc and lead supply, using a system dynamics model. Resources, Conservation & Recycling: X, 4(100007). https://doi.org/https://doi.org/10.1016/j.rcrx.2019.100007
    """
    return float(coefficients_cu_profit_push_ocean().loc["A_S_CURVE_FIT"]) * (
        1
        - np.exp(
            -float(coefficients_cu_profit_push_ocean().loc["k_S_CURVE_FIT"])
            * fraction_of_the_decrease_cu_ocean_profit_delay()
            ** float(coefficients_cu_profit_push_ocean().loc["n_S_CURVE_FIT"])
        )
    )


@component.add(
    name="Cu_RATE_OF_NEW_SCRAP",
    units="Mt/Years",
    comp_type="Constant",
    comp_subtype="Normal",
)
def cu_rate_of_new_scrap():
    """
    Copper lost during production of final products. derived from the source: Loibl, A., & Tercero Espinoza, L. A. (2021). Current challenges in copper recycling: aligning insights from material flow analysis with technological research developments and industry issues in Europe and North America. Resources, Conservation and Recycling, 169(January), 105462. https://doi.org/10.1016/j.resconrec.2021.105462 GET DIRECT CONSTANTS('model_parameters/materials/materials.xlsx', 'Copper', 'Cu_RATE_OF_NEW_SCRAP')
    """
    return 0.155


@component.add(
    name="cu_recycled_to_cu_market",
    units="Mt/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_cu_recycling_policy": 1,
        "cu_eol_recycling_rate_sp": 1,
        "cu_scrapped": 1,
        "cu_recycling_test": 1,
    },
)
def cu_recycled_to_cu_market():
    """
    Recycling is amplified by higher copper prices. With a higher price the recycling is increasing. When price is low the recycling is decreasing. Recycling creates recycling profits, driving more recycling COEFFICIENTS Cu RECYCLED TO Cu MARKET*Cu scrapped*Cu scrap coefficient Sverdrup, H. U., & Olafsdottir, A. H. (2019). On the long-term sustainability of copper, zinc and lead supply, using a system dynamics model. Resources, Conservation & Recycling: X, 4(100007). https://doi.org/https://doi.org/10.1016/j.rcrx.2019.100007
    """
    return if_then_else(
        switch_cu_recycling_policy() == 1,
        lambda: cu_eol_recycling_rate_sp(),
        lambda: cu_scrapped() * cu_recycling_test(),
    )


@component.add(
    name="Cu_recycling_test",
    units="DMNL/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"coefficients_cu_recycled_to_cu_market": 1, "cu_scrap_coefficient": 1},
)
def cu_recycling_test():
    return coefficients_cu_recycled_to_cu_market() * cu_scrap_coefficient()


@component.add(
    name="Cu_scrap_coefficient",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"coefficients_cu_scrap_coefficient": 3, "cu_price_economy": 1},
)
def cu_scrap_coefficient():
    """
    This is a function that causes more recycling when the price increases, a consequence of the causal loop diagram. This CLD is shown in the copper paper (Sverdrup et al, 2019). This is a result of what is called the Sherwood function, presented here as an s shaped curve with y values from 0,14 to 0,6 and with x values from 0 to 25000 cu $/t and is represented here with the following S curve equation: y=a/(1 + EXP(-b * (x-c))) where: a=7,148535e-01 b=1,532671e-04 c=1,119455e+04 Sources: Dahmus, J.B. and Gutowski, T.G., 2007. What gets recycled: an information theory based model for product recycling. Environ. Sci. Technol. 41, 7543â€“7550. Gutowski, T.G., Wolf, M.L., Dahmus, J.B., Albino, D.C., 2008. Analysis of recycling systems. Knoxville, Tennessee. Proceedings of the 2008 NSF Engineering and Research and Innovation Conference 8 pages., Gutowski, T.G., Sahni, S., Allwood, M., Ashby, M.F., Worrell, E., 2016. The energy re- quired to produce materials: constraints on energy-intensity improvements, parameters of demand. Philos. Trans. Math. Phys. Eng. Sci. 371, 20120003https://doi.org/ 10.1098/rsta.2012.0003. Sverdrup, H, Olafsdottir, A.H., Ragnarsdottir, K.V., 2019. Assessing global copper, zinc and lead extraction rates, supply, price and resources using the WORLD6 integrated assessment model. Resources, Conservation and Recycling 1-26. X4 100007. https://doi.org/10.1016/j.rcrx.2019.100007. Open access publication.
    """
    return float(coefficients_cu_scrap_coefficient().loc["A_S_CURVE"]) / (
        1
        + np.exp(
            -float(coefficients_cu_scrap_coefficient().loc["B_S_CURVE"])
            * (
                cu_price_economy()
                - float(coefficients_cu_scrap_coefficient().loc["C_S_CURVE"])
            )
        )
    )


@component.add(
    name="Cu_scrapped",
    units="Mt",
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_cu_scrapped": 1},
    other_deps={
        "_integ_cu_scrapped": {
            "initial": {"initial_cu_scrapped": 1},
            "step": {
                "cu_in_use_in_society_to_cu_scrapping": 1,
                "cu_recycled_to_cu_market": 1,
                "cu_scrapped_losses": 1,
                "loss_during_separtion_and_proccessing": 1,
            },
        }
    },
)
def cu_scrapped():
    """
    The amount of Cu that is scrapped. Source: Sverdrup, H. U., & Olafsdottir, A. H. (2019). On the long-term sustainability of copper, zinc and lead supply, using a system dynamics model. Resources, Conservation & Recycling: X, 4(100007). https://doi.org/https://doi.org/10.1016/j.rcrx.2019.100007
    """
    return _integ_cu_scrapped()


_integ_cu_scrapped = Integ(
    lambda: cu_in_use_in_society_to_cu_scrapping()
    - cu_recycled_to_cu_market()
    - cu_scrapped_losses()
    - loss_during_separtion_and_proccessing(),
    lambda: initial_cu_scrapped(),
    "_integ_cu_scrapped",
)


@component.add(
    name="Cu_scrapped_losses",
    units="Mt/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_cu_recycling_policy": 1,
        "cu_scrapped": 2,
        "cu_eol_recycling_rate_sp": 1,
        "cu_separation_loss_rate": 2,
        "cu_recycling_test": 1,
    },
)
def cu_scrapped_losses():
    """
    The outflow of Cu is the flow of copper that is lost during the scrapping process.
    """
    return if_then_else(
        switch_cu_recycling_policy() == 1,
        lambda: cu_scrapped()
        * (1 - cu_eol_recycling_rate_sp() + cu_separation_loss_rate()),
        lambda: cu_scrapped() * (1 - cu_recycling_test() - cu_separation_loss_rate()),
    )


@component.add(
    name="Cu_scrapping_amplifier",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"coefficients_cu_scrapping": 3, "cu_price_economy": 1},
)
def cu_scrapping_amplifier():
    """
    This is a function that causes more scrapping when the price increases, a consequence of the causal loop diagram. This CLD is shown in the copper paper. This is a result of what is called the Sherwood function and is represented here with the following S curve: y=a/(1 + EXP(-b * (x-c))) where: x= Cu_price_per_ton a= 1,253103e+01 b=9,626724e-05 c=3,390583e+04 it looks like an s shape curve, that amplifies up to 10 if the Cu $ per ton is very high. The amplification is very low when the price is very low. Concept is based on the following sources: Dahmus, J.B., & Gutowski, T.G. (2007). What gets recycled: an information theory based model for product recycling. Environmental Science & Technology, 41(24), 7543-7550. Gutowski, T.G., Wolf, M.L., Dahmus, J.B., Albino, D.C., 2008. Analysis of recycling systems. Knoxville, Tennessee. Proceedings of the 2008 NSF Engineering and Research and Innovation Conference 8 pages., Gutowski, T.G., Sahni, S., Allwood, M., Ashby, M.F., Worrell, E., 2016. The energy re- quired to produce materials: constraints on energy-intensity improvements, parameters of demand. Philos. Trans. Math. Phys. Eng. Sci. 371, 20120003https://doi.org/ 10.1098/rsta.2012.0003. Sverdrup, H, Olafsdottir, A.H., Ragnarsdottir, K.V., 2019. Assessing global copper, zinc and lead extraction rates, supply, price and resources using the WORLD6 integrated assessment model. Resources, Conservation and Recycling 1-26. X4 100007. https://doi.org/10.1016/j.rcrx.2019.100007. Open access publication.
    """
    return float(coefficients_cu_scrapping().loc["A_S_CURVE"]) / (
        1
        + np.exp(
            -float(coefficients_cu_scrapping().loc["B_S_CURVE"])
            * (cu_price_economy() - float(coefficients_cu_scrapping().loc["C_S_CURVE"]))
        )
    )


@component.add(
    name="Cu_secondary",
    units="Mt/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cu_from_mo": 1,
        "cu_from_ni": 1,
        "cu_from_zn": 1,
        "cu_from_ag": 1,
        "cu_from_pgm": 1,
    },
)
def cu_secondary():
    """
    Name in the WORLD7 model Cu secondary. Is summing up the Cu that is coming from mining of other materials.
    """
    return cu_from_mo() + cu_from_ni() + cu_from_zn() + cu_from_ag() + cu_from_pgm()


@component.add(
    name="Cu_secondary_cost",
    units="M$/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"cu_cost_grade": 1, "cu_secondary": 1},
)
def cu_secondary_cost():
    """
    The cost of refining from secondary Cu mining is set as the same value as low grade, as these costs were similar. This is a simplification based on an estimate and might be broken out as a separate variable if in future versions.
    """
    return float(cu_cost_grade().loc["LOW_GRADE"]) * cu_secondary()


@component.add(
    name="Cu_secondary_profits",
    units="M$",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"cu_secondary": 1, "cu_price_economy": 1, "cu_secondary_cost": 1},
)
def cu_secondary_profits():
    """
    Profit from Cu secondary mining. Profit is defined as income- costs. Mt*$/ton-M$
    """
    return cu_secondary() * cu_price_economy() - cu_secondary_cost()


@component.add(
    name="Cu_SEPARATION_LOSS_RATE",
    units="1/Year",
    comp_type="Constant",
    comp_subtype="Normal",
)
def cu_separation_loss_rate():
    """
    Copper losses during separation and processing. estimatation based on Source: Loibl, A., & Tercero Espinoza, L. A. (2021). Current challenges in copper recycling: aligning insights from material flow analysis with technological research developments and industry issues in Europe and North America. Resources, Conservation and Recycling, 169(January), 105462. https://doi.org/10.1016/j.resconrec.2021.105462
    """
    return 0.13


@component.add(
    name="Cu_share_entering_recycling",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"cu_in_use_in_society_to_cu_scrapping": 1, "cu_market_sales": 1},
)
def cu_share_entering_recycling():
    """
    Share of copper that is leaving the stage of being in use. Share of what is sent to scrapping copared to what enters the use phase.
    """
    return zidz(cu_in_use_in_society_to_cu_scrapping(), cu_market_sales())


@component.add(
    name="Cu_share_of_secondary_material",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"cu_recycled_to_cu_market": 2, "cu_new_scrap": 2, "cu_extraction": 1},
)
def cu_share_of_secondary_material():
    """
    Share of secondary material used to produce new copper to be sold on the market.
    """
    return zidz(
        cu_recycled_to_cu_market() + cu_new_scrap(),
        cu_extraction() + cu_recycled_to_cu_market() + cu_new_scrap(),
    )


@component.add(
    name="Cu_supply",
    units="Mt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"cu_market_sales": 1},
)
def cu_supply():
    return cu_market_sales()


@component.add(
    name="Cu_supply_kg_per_person",
    units="kg/(persons*Years)",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"cu_market_sales": 1, "imv_global_population": 1},
)
def cu_supply_kg_per_person():
    """
    The amount of Cu in kg that is supplied per person Mt/(Billion persons*Years) = kg/persons*years
    """
    return cu_market_sales() / imv_global_population()


@component.add(
    name="Cu_supply_rate_from_recycling",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cu_recycled_to_cu_market": 2,
        "imv_electronics_cu_recovered": 2,
        "cu_extraction": 1,
    },
)
def cu_supply_rate_from_recycling():
    """
    The rate of material in this case copper coming from Cu-recycling. So it is the fraction of the demand that gets satisfied buy recycled materials.
    """
    return (cu_recycled_to_cu_market() + imv_electronics_cu_recovered()) / (
        cu_extraction() + cu_recycled_to_cu_market() + imv_electronics_cu_recovered()
    )


@component.add(
    name="Cu_supply_to_society",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"cu_market_sales": 1},
)
def cu_supply_to_society():
    """
    "There is a flow between the copper market and the usage of copper in society, and this flow is influenced by changes in the price of copper. The price of copper can modify the demand for copper in the market, which in turn affects the amount of copper used in society.". In the broader picture, industrial activities contribute through wages and profits to the overall disposable income in society, which in turn contributes to consumption and demand, a reinforcing loop. Sverdrup, H. U., & Olafsdottir, A. H. (2019). On the long-term sustainability of copper, zinc and lead supply, using a system dynamics model. Resources, Conservation & Recycling: X, 4(100007). https://doi.org/https://doi.org/10.1016/j.rcrx.2019.100007
    """
    return cu_market_sales() * 0.835


@component.add(
    name="Cu_total_above_ground",
    units="Mt",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"cu_in_use_in_society": 1, "cu_scrapped": 1, "cu_market": 1},
)
def cu_total_above_ground():
    """
    W7 name: Cu Total above ground The total amount of CU above ground in use, on the market and in scrapping.
    """
    return cu_in_use_in_society() + cu_scrapped() + cu_market()


@component.add(
    name="Cu_total_energy_use_from_extraction_and_refining",
    units="TJ/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cu_energy_use": 5,
        "cu_energy_use_recycling": 1,
        "cu_energy_use_secondary": 1,
        "unit_conversion_kg_mt": 1,
        "unit_conversion_tj_mj": 1,
    },
)
def cu_total_energy_use_from_extraction_and_refining():
    """
    Copper total energy use for mining and refining. Sum over the different ore grades and sum of the energy used for recycling and the energy used for mining and refining from secondary mining. Gutowski, T.G., Sahni, S., Allwood, M., Ashby, M.F., Worrell, E., 2016. The energy required to produce materials: constraints on energy-intensity improvements, parameters of demand. Philosophical Transactions of the Royal Society A 371: 20120003. http://dx.doi.org/10.1098/rsta.2012.0003 MJ/kg*Mt/years *kg/Mt
    """
    return (
        (
            float(cu_energy_use().loc["HIGH_GRADE"])
            + float(cu_energy_use().loc["LOW_GRADE"])
            + float(cu_energy_use().loc["ULTRALOW_GRADE"])
            + float(cu_energy_use().loc["TRACE_GRADE"])
            + cu_energy_use_recycling()
            + float(cu_energy_use().loc["RICH_GRADE"])
            + cu_energy_use_secondary()
        )
        * unit_conversion_kg_mt()
        * unit_conversion_tj_mj()
    )


@component.add(
    name="decrease_Cu_demand_delay",
    units="Mt/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"delayed_ts_cu_demand": 1, "coefficients_decrease_cu_demand_delay": 1},
)
def decrease_cu_demand_delay():
    """
    old World7 name: Cu demand delay out Demand, stock flow structere is used to eliminate short term disturbances.
    """
    return delayed_ts_cu_demand() * coefficients_decrease_cu_demand_delay()


@component.add(
    name="decrease_Cu_in_use_in_society",
    units="Mt/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"cu_in_use_in_society": 1, "cu_society_loss_rate": 1},
)
def decrease_cu_in_use_in_society():
    """
    Old world 7 name: Cu Societal losses Copper lost from the used in sociaty.
    """
    return cu_in_use_in_society() * cu_society_loss_rate()


@component.add(
    name="decrease_delayed_TS_Cu_ocean_profit_delay",
    units="M$/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"delayed_ts_cu_ocean_profit": 1},
)
def decrease_delayed_ts_cu_ocean_profit_delay():
    """
    To prevent circular connection in the model the profit signal is delayed.
    """
    return delayed_ts_cu_ocean_profit()


@component.add(
    name="decrease_delayed_TS_Cu_profit",
    units="M$/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"delayed_ts_cu_profit": 1, "cu_profit_delay": 1},
)
def decrease_delayed_ts_cu_profit():
    """
    Profit out flow, profit stock and flow structure used to avoid short term disturbances in the model and Copper market. Higher profit triggers higher mining.
    """
    return np.maximum(delayed_ts_cu_profit() * cu_profit_delay(), 0)


@component.add(
    name="DELAYED_Cu_price_economy_adjusted_test",
    units="$/t",
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_cu_price_economy_adjusted_test": 1},
    other_deps={
        "_delayfixed_delayed_cu_price_economy_adjusted_test": {
            "initial": {"cu_price_economy_initial": 1, "time_step": 1},
            "step": {"cu_price_economy": 1},
        }
    },
)
def delayed_cu_price_economy_adjusted_test():
    """
    Delayed price variable to avoid issues with simoultanous equation in vensim
    """
    return _delayfixed_delayed_cu_price_economy_adjusted_test()


_delayfixed_delayed_cu_price_economy_adjusted_test = DelayFixed(
    lambda: cu_price_economy(),
    lambda: time_step(),
    lambda: cu_price_economy_initial(),
    time_step,
    "_delayfixed_delayed_cu_price_economy_adjusted_test",
)


@component.add(
    name="DELAYED_MARKET_INCREASE",
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_market_increase": 1},
    other_deps={
        "_delayfixed_delayed_market_increase": {
            "initial": {"time_step": 1},
            "step": {"cu_market_supply": 1},
        }
    },
)
def delayed_market_increase():
    return _delayfixed_delayed_market_increase()


_delayfixed_delayed_market_increase = DelayFixed(
    lambda: cu_market_supply(),
    lambda: time_step(),
    lambda: 38.0475,
    time_step,
    "_delayfixed_delayed_market_increase",
)


@component.add(
    name="delayed_TS_Cu_demand",
    units="Mt",
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_delayed_ts_cu_demand": 1},
    other_deps={
        "_integ_delayed_ts_cu_demand": {
            "initial": {"initial_cu_demand_delay": 1},
            "step": {"increase_cu_demand_delay": 1, "decrease_cu_demand_delay": 1},
        }
    },
)
def delayed_ts_cu_demand():
    """
    old world7 name Cu demand delay Here we have a demand that is driven by population and copper use per person, but is adjusted up or down with price. Cu_deman_delay(t - dt) + (Cu_demand_delay_in - Cu_demand_delay_out) * dt The initial values for the cu kdemand delay is based on simulation outputs from the world7 for the year 2005. The world7 outputs are based on initial values from 1900. initial value comes from WORLD7 outputs from 2005: INIT Cu_deman_delay = 2,37570209044 Source: Sverdrup, H. U., & Olafsdottir, A. H. (2019). On the long-term sustainability of copper, zinc and lead supply, using a system dynamics model. Resources, Conservation & Recycling: X, 4(100007). https://doi.org/https://doi.org/10.1016/j.rcrx.2019.100007
    """
    return _integ_delayed_ts_cu_demand()


_integ_delayed_ts_cu_demand = Integ(
    lambda: increase_cu_demand_delay() - decrease_cu_demand_delay(),
    lambda: initial_cu_demand_delay(),
    "_integ_delayed_ts_cu_demand",
)


@component.add(
    name="delayed_TS_Cu_ocean_profit",
    units="M$",
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_delayed_ts_cu_ocean_profit": 1},
    other_deps={
        "_integ_delayed_ts_cu_ocean_profit": {
            "initial": {"initial_cu_ocean_profit_delay": 1},
            "step": {
                "increase_delayed_ts_cu_ocean_profit_delay": 1,
                "decrease_delayed_ts_cu_ocean_profit_delay": 1,
            },
        }
    },
)
def delayed_ts_cu_ocean_profit():
    """
    This is a workaround to avoid circular error, any short time delay works. The delayed TIME STEP, is typically used in system dynamics models to avoid algebraic loops. world7 name cu ocean delay The initial values for the cu known stocks are based on simulation outputs from the world7 for the year 2005. The world7 outputs are based on initial values from 1900 that were stratified with respect to ore metal content and relative extraction cost based on yield of extraction and energy requirements. Source: Sverdrup, H. U., & Olafsdottir, A. H. (2019). On the long-term sustainability of copper, zinc and lead supply, using a system dynamics model. Resources, Conservation & Recycling: X, 4(100007). https://doi.org/https://doi.org/10.1016/j.rcrx.2019.100007
    """
    return _integ_delayed_ts_cu_ocean_profit()


_integ_delayed_ts_cu_ocean_profit = Integ(
    lambda: increase_delayed_ts_cu_ocean_profit_delay()
    - decrease_delayed_ts_cu_ocean_profit_delay(),
    lambda: initial_cu_ocean_profit_delay(),
    "_integ_delayed_ts_cu_ocean_profit",
)


@component.add(
    name="delayed_TS_Cu_price_economy_adjusted",
    units="DMNL",
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_cu_price_economy_adjusted": 1},
    other_deps={
        "_delayfixed_delayed_ts_cu_price_economy_adjusted": {
            "initial": {"time_step": 1},
            "step": {"cu_price_economy_adjusted": 1},
        }
    },
)
def delayed_ts_cu_price_economy_adjusted():
    """
    Delayed copper price economy adjusted. The delay is used to prevent simsimoultanous equation in vensim.
    """
    return _delayfixed_delayed_ts_cu_price_economy_adjusted()


_delayfixed_delayed_ts_cu_price_economy_adjusted = DelayFixed(
    lambda: cu_price_economy_adjusted(),
    lambda: time_step(),
    lambda: 100,
    time_step,
    "_delayfixed_delayed_ts_cu_price_economy_adjusted",
)


@component.add(
    name="delayed_TS_Cu_profit",
    units="M$",
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_delayed_ts_cu_profit": 1},
    other_deps={
        "_integ_delayed_ts_cu_profit": {
            "initial": {"initial_cu_profit_delay": 1},
            "step": {
                "increase_delayed_ts_cu_profit": 1,
                "decrease_delayed_ts_cu_profit": 1,
            },
        }
    },
)
def delayed_ts_cu_profit():
    """
    Profit stock, profit stock and flow structure used to avoid short term disturbances in the model and Copper market. Higher profit triggers higher mining. This is a workaround to avoid circular error, any short time delay works. The delayed TIME STEP, is typically used in system dynamics models to avoid algebraic loops. Any short delay will do... INIT Cu_profit_delay = 219722,746564 Source: Sverdrup, H. U., & Olafsdottir, A. H. (2019). On the long-term sustainability of copper, zinc and lead supply, using a system dynamics model. Resources, Conservation & Recycling: X, 4(100007). https://doi.org/https://doi.org/10.1016/j.rcrx.2019.100007
    """
    return _integ_delayed_ts_cu_profit()


_integ_delayed_ts_cu_profit = Integ(
    lambda: increase_delayed_ts_cu_profit() - decrease_delayed_ts_cu_profit(),
    lambda: initial_cu_profit_delay(),
    "_integ_delayed_ts_cu_profit",
)


@component.add(
    name="DEMAND_CU_BASE_YEAR",
    units="Mt/Years",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_demand_cu_base_year"},
)
def demand_cu_base_year():
    """
    The HISTORICAL demand of the year 2005. It is used to calculate the implicit price to convert economc terms of million dollars to million tons. Source:
    """
    return _ext_constant_demand_cu_base_year()


_ext_constant_demand_cu_base_year = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Copper",
    "DEMAND_CU_BASE_YEAR",
    {},
    _root,
    {},
    "_ext_constant_demand_cu_base_year",
)


@component.add(
    name="fraction_of_the_decrease_Cu_ocean_profit_delay",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"decrease_delayed_ts_cu_ocean_profit_delay": 1, "cu_push_ocean": 1},
)
def fraction_of_the_decrease_cu_ocean_profit_delay():
    """
    0,1% of the output of "decrease_Cu_ocean_profit_delay" so the values can be fitted to an s curve
    """
    return decrease_delayed_ts_cu_ocean_profit_delay() * cu_push_ocean()


@component.add(
    name="Growth_in_Cu_price",
    units="$/t",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 2},
)
def growth_in_cu_price():
    """
    Growth in Cu price test variable.
    """
    return if_then_else(time() >= 2020, lambda: (1 + 0.2) ** (time() - 2020), lambda: 1)


@component.add(
    name="HISTORICAL_Cu_DEMAND",
    units="Mt/Year",
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_historical_cu_demand",
        "__data__": "_ext_data_historical_cu_demand",
        "time": 1,
    },
)
def historical_cu_demand():
    """
    Historical Copper demand from 2005 until 2022. And projection from 2022 until 2024. Source:
    """
    return _ext_data_historical_cu_demand(time())


_ext_data_historical_cu_demand = ExtData(
    "model_parameters/materials/materials.xlsx",
    "Copper",
    "TIME_SERIES",
    "HISTORICAL_Cu_DEMAND",
    None,
    {},
    _root,
    {},
    "_ext_data_historical_cu_demand",
)


@component.add(
    name="IMPLICIT_PRICE_MATERIALS_Cu",
    units="Mdollars_2015/Mt",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "historical_cu_demand": 1,
        "initial_output_real_materials": 2,
        "demand_cu_base_year": 1,
    },
)
def implicit_price_materials_cu():
    """
    25470.5 Implicit price is used to convert values from the economic module Mdollars to Mt to match the value of 2015 mt copper. 16989.8
    """
    return if_then_else(
        time() < 2015,
        lambda: sum(
            initial_output_real_materials()
            .loc[:, "MINING_AND_MANUFACTURING_COPPER"]
            .reset_coords(drop=True)
            .rename({"REGIONS_35_I": "REGIONS_35_I!"}),
            dim=["REGIONS_35_I!"],
        )
        / historical_cu_demand(),
        lambda: sum(
            initial_output_real_materials()
            .loc[:, "MINING_AND_MANUFACTURING_COPPER"]
            .reset_coords(drop=True)
            .rename({"REGIONS_35_I": "REGIONS_35_I!"}),
            dim=["REGIONS_35_I!"],
        )
        / demand_cu_base_year(),
    )


@component.add(
    name="IMV_Ag_MINING",
    units="Kt/Years",
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_imv_ag_mining",
        "__data__": "_ext_data_imv_ag_mining",
        "time": 1,
    },
)
def imv_ag_mining():
    """
    THIS IS AN INTER MODULE VARIABLE - it will be hooked up dynamically with other modules-not in the current version of Wiliam due to time. Presently it has simulation outputs from World 7 for time - 2005-2100. Source: Sverdrup, H. U., & Olafsdottir, A. H. (2019). On the long-term sustainability of copper, zinc and lead supply, using a system dynamics model. Resources, Conservation & Recycling: X, 4(100007). https://doi.org/https://doi.org/10.1016/j.rcrx.2019.100007
    """
    return _ext_data_imv_ag_mining(time())


_ext_data_imv_ag_mining = ExtData(
    "model_parameters/materials/materials.xlsx",
    "Copper",
    "TIME_SERIES",
    "IMV_Ag_MINING",
    None,
    {},
    _root,
    {},
    "_ext_data_imv_ag_mining",
)


@component.add(
    name="IMV_Cu_ALL_VEHICLE_DEMAND",
    units="Mt/Years",
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_imv_cu_all_vehicle_demand",
        "__data__": "_ext_data_imv_cu_all_vehicle_demand",
        "time": 1,
    },
)
def imv_cu_all_vehicle_demand():
    """
    THIS IS AN INTER MODULE VARIABLE - it will be hooked up dynamically with other modules-not in the current version of Wiliam due to time. Presently it has simulation outputs from World 7 for time - 2005-2100. Source: Sverdrup, H. U., & Olafsdottir, A. H. (2019). On the long-term sustainability of copper, zinc and lead supply, using a system dynamics model. Resources, Conservation & Recycling: X, 4(100007). https://doi.org/https://doi.org/10.1016/j.rcrx.2019.100007
    """
    return _ext_data_imv_cu_all_vehicle_demand(time())


_ext_data_imv_cu_all_vehicle_demand = ExtData(
    "model_parameters/materials/materials.xlsx",
    "Copper",
    "TIME_SERIES",
    "IMV_CuALL_VEHICLE_DEMAND",
    None,
    {},
    _root,
    {},
    "_ext_data_imv_cu_all_vehicle_demand",
)


@component.add(
    name="IMV_ELECTRONICS_Cu_DEMAND",
    units="kg/(persons*Years)",
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_imv_electronics_cu_demand",
        "__data__": "_ext_data_imv_electronics_cu_demand",
        "time": 1,
    },
)
def imv_electronics_cu_demand():
    """
    This variable is an IMV = inter module variable. It comes from another module that has yet to be connected to this module. (the electronics module in world7) Currently the variable is represented as a graph variable but this will be changed later that matches the output from the WORLD7. The variable shows the electronics Cu demand From the economic sector we can have production of electronics in whole demand for copper. IMV_ELECTRONICS_Cu_RECOVERED
    """
    return _ext_data_imv_electronics_cu_demand(time())


_ext_data_imv_electronics_cu_demand = ExtData(
    "model_parameters/materials/materials.xlsx",
    "Copper",
    "TIME_SERIES",
    "IMV_ELECTRONICS_Cu_DEMAND",
    "interpolate",
    {},
    _root,
    {},
    "_ext_data_imv_electronics_cu_demand",
)


@component.add(
    name="IMV_ELECTRONICS_Cu_RECOVERED",
    units="Mt/Years",
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_imv_electronics_cu_recovered",
        "__data__": "_ext_data_imv_electronics_cu_recovered",
        "time": 1,
    },
)
def imv_electronics_cu_recovered():
    """
    THIS IS AN INTER MODULE VARIABLE - it will be hooked up dynamically with other modules in due time but presently it has simulation outputs from world7 for time - 2005-2100. It comes from the electronics module in world7 Currently the variable is represented as a graph variable but this will be changed laiter that matches the output from the WORLD7. The variable shows the Cu recovered from the electronics that have been scrapped. Source: Sverdrup, H. U., & Olafsdottir, A. H. (2019). On the long-term sustainability of copper, zinc and lead supply, using a system dynamics model. Resources, Conservation & Recycling: X, 4(100007). https://doi.org/https://doi.org/10.1016/j.rcrx.2019.100007
    """
    return _ext_data_imv_electronics_cu_recovered(time())


_ext_data_imv_electronics_cu_recovered = ExtData(
    "model_parameters/materials/materials.xlsx",
    "Copper",
    "TIME_SERIES",
    "IMV_ELECTRONICS_Cu_RECOVERED",
    "interpolate",
    {},
    _root,
    {},
    "_ext_data_imv_electronics_cu_recovered",
)


@component.add(
    name="IMV_Mo_TOTAL_MINING",
    units="Mt/Years",
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_imv_mo_total_mining",
        "__data__": "_ext_data_imv_mo_total_mining",
        "time": 1,
    },
)
def imv_mo_total_mining():
    """
    THIS IS AN INTER MODULE VARIABLE - it will be hooked up dynamically with other modules-not in the current version of Wiliam due to time. Presently it has simulation outputs from World 7 for time - 2005-2100. Source: Sverdrup, H. U., & Olafsdottir, A. H. (2019). On the long-term sustainability of copper, zinc and lead supply, using a system dynamics model. Resources, Conservation & Recycling: X, 4(100007). https://doi.org/https://doi.org/10.1016/j.rcrx.2019.100007.
    """
    return _ext_data_imv_mo_total_mining(time())


_ext_data_imv_mo_total_mining = ExtData(
    "model_parameters/materials/materials.xlsx",
    "Copper",
    "TIME_SERIES",
    "IMV_Mo_TOTAL_MINING",
    None,
    {},
    _root,
    {},
    "_ext_data_imv_mo_total_mining",
)


@component.add(
    name="IMV_Ni_TOTAL_MINING",
    units="Mt/Years",
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_imv_ni_total_mining",
        "__data__": "_ext_data_imv_ni_total_mining",
        "time": 1,
    },
)
def imv_ni_total_mining():
    """
    THIS IS AN INTER MODULE VARIABLE - it will be hooked up dynamically with other modules-not in the current version of Wiliam due to time. Presently it has simulation outputs from World 7 for time - 2005-2100. Source: Sverdrup, H. U., & Olafsdottir, A. H. (2019). On the long-term sustainability of copper, zinc and lead supply, using a system dynamics model. Resources, Conservation & Recycling: X, 4(100007). https://doi.org/https://doi.org/10.1016/j.rcrx.2019.100007
    """
    return _ext_data_imv_ni_total_mining(time())


_ext_data_imv_ni_total_mining = ExtData(
    "model_parameters/materials/materials.xlsx",
    "Copper",
    "TIME_SERIES",
    "IMV_Ni_TOTAL_MINING",
    None,
    {},
    _root,
    {},
    "_ext_data_imv_ni_total_mining",
)


@component.add(
    name="IMV_PGM_FROM_MINING",
    units="Kt/Years",
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_imv_pgm_from_mining",
        "__data__": "_ext_data_imv_pgm_from_mining",
        "time": 1,
    },
)
def imv_pgm_from_mining():
    """
    THIS IS AN INTER MODULE VARIABLE - it will be hooked up dynamically with other modules-not in the current version of Wiliam due to time. Presently it has simulation outputs from World 7 for time - 2005-2100. Source: Sverdrup, H. U., & Olafsdottir, A. H. (2019). On the long-term sustainability of copper, zinc and lead supply, using a system dynamics model. Resources, Conservation & Recycling: X, 4(100007). https://doi.org/https://doi.org/10.1016/j.rcrx.2019.100007
    """
    return _ext_data_imv_pgm_from_mining(time())


_ext_data_imv_pgm_from_mining = ExtData(
    "model_parameters/materials/materials.xlsx",
    "Copper",
    "TIME_SERIES",
    "IMV_PGM_FROM_MINING",
    None,
    {},
    _root,
    {},
    "_ext_data_imv_pgm_from_mining",
)


@component.add(
    name="IMV_START_TIME",
    units="Years",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_imv_start_time"},
)
def imv_start_time():
    """
    Start time of the William model.
    """
    return _ext_constant_imv_start_time()


_ext_constant_imv_start_time = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Copper",
    "IMV_START_TIME",
    {},
    _root,
    {},
    "_ext_constant_imv_start_time",
)


@component.add(
    name="IMV_Zn_MINED",
    units="Mt/Years",
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_imv_zn_mined",
        "__data__": "_ext_data_imv_zn_mined",
        "time": 1,
    },
)
def imv_zn_mined():
    """
    THIS IS AN INTER MODULE VARIABLE - it will be hooked up dynamically with other modules-not in the current version of Wiliam due to time. Presently it has simulation outputs from World 7 for time - 2005-2100. Source: Sverdrup, H. U., & Olafsdottir, A. H. (2019). On the long-term sustainability of copper, zinc and lead supply, using a system dynamics model. Resources, Conservation & Recycling: X, 4(100007). https://doi.org/https://doi.org/10.1016/j.rcrx.2019.100007
    """
    return _ext_data_imv_zn_mined(time())


_ext_data_imv_zn_mined = ExtData(
    "model_parameters/materials/materials.xlsx",
    "Copper",
    "TIME_SERIES",
    "IMV_Zn_MINED",
    None,
    {},
    _root,
    {},
    "_ext_data_imv_zn_mined",
)


@component.add(
    name="increase_Cu_cumulative_mining",
    units="Mt/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"cu_mined": 1},
)
def increase_cu_cumulative_mining():
    """
    world 7 old name: Cu mining in Flow of Cu mined to feed the Stock of Cumulative mining. Used to track the amount of copper which is minined in total.
    """
    return cu_mined()


@component.add(
    name="increase_cu_demand_delay",
    units="Mt/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cu_demand_per_person_based_on_gdp": 1,
        "coefficients_increase_cu_demand_delay": 1,
        "imv_global_population": 2,
        "imv_electronics_cu_demand": 1,
    },
)
def increase_cu_demand_delay():
    """
    world7 name: Cu demand delay in Demand calculated based on the input variables. Stock and flow structe is used to eliminate short term disturbances. cu_demand_per_person_based_on_gdp*0,12*GV_world_population+GV_e_cu_demand*GV_world_po pulation kg/person* Billion persons
    """
    return (
        cu_demand_per_person_based_on_gdp()
        * coefficients_increase_cu_demand_delay()
        * imv_global_population()
        + imv_electronics_cu_demand() * imv_global_population()
    )


@component.add(
    name="increase_delayed_TS_Cu_ocean_profit_delay",
    units="M$/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"cu_profit_ocean": 1},
)
def increase_delayed_ts_cu_ocean_profit_delay():
    """
    the increase in the Cu ocean profit delay is the Cu profit from ocean mining, with higher profit more ocean mining will take place. If the profit is zero no ocean mining will take place.
    """
    return cu_profit_ocean()


@component.add(
    name="increase_delayed_TS_Cu_profit",
    units="M$/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"cu_mining_profits": 1},
)
def increase_delayed_ts_cu_profit():
    """
    Profit in flow, profit stock and flow structure used to avoid short term disturbances in the model and Copper market. Higher profit triggers higher mining.
    """
    return cu_mining_profits()


@component.add(
    name="INITIAL_OUTPUT_REAL_MATERIALS",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_initial_output_real_materials": 1},
    other_deps={
        "_initial_initial_output_real_materials": {
            "initial": {"output_real": 1},
            "step": {},
        }
    },
)
def initial_output_real_materials():
    """
    Initial (2015) output real in million dollars per year. Used to calculate the Initial outputs of the extraction sector to calibrate the implicit price.
    """
    return _initial_initial_output_real_materials()


_initial_initial_output_real_materials = Initial(
    lambda: output_real(), "_initial_initial_output_real_materials"
)


@component.add(
    name="Loss_during_separtion_and_proccessing",
    units="Mt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"cu_separation_loss_rate": 1, "cu_scrapped": 1},
)
def loss_during_separtion_and_proccessing():
    """
    Copper losses during separation and proccessing.
    """
    return cu_separation_loss_rate() * cu_scrapped()


@component.add(
    name="MAX_Cu_PRICE",
    units="$/t",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_max_cu_price"},
)
def max_cu_price():
    """
    Set maximum copper price if the demand is higher than the supply. This is chosen by the authors of the model. A max. is choosen since vensim did not offer the option to increase the price until demand and price match simultanously.
    """
    return _ext_constant_max_cu_price()


_ext_constant_max_cu_price = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Copper",
    "MAX_Cu_PRICE",
    {},
    _root,
    {},
    "_ext_constant_max_cu_price",
)


@component.add(
    name="mining_Cu_known_reserves",
    units="Mt/Years",
    subscripts=["ORE_GRADES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cu_known_reserves": 6,
        "cu_extraction_coefficient": 6,
        "rich_grade_factor": 1,
        "change_cu_grade": 4,
        "high_grade_factor": 1,
        "change_cu_mining_technology_s_curve": 3,
        "cu_profit_push_ocean": 1,
    },
)
def mining_cu_known_reserves():
    """
    Cu leaves the known reserve stock by minig, therefore this variable is the action of mining, but named here "decrease Cu known resoures" for the sake of the WILLIAM naming rules. Mining is the action that extracts copper from known reserves and puts it to refining. There are fundamental differences in how mining in an individual mine is modelled on the business level and what happens when a whole population of mines are operated. Then host dynamics and group behaviour come into play, changing the equations. Many of the particulars of a single mine are distributed over time in a population of mines, leading to the good sense of working with averages and where discrete events become continuous when they are many and distributed over time. Sverdrup, H. U., & Olafsdottir, A. H. (2019). On the long-term sustainability of copper, zinc and lead supply, using a system dynamics model. Resources, Conservation & Recycling: X, 4(100007). https://doi.org/https://doi.org/10.1016/j.rcrx.2019.100007
    """
    value = xr.DataArray(
        np.nan, {"ORE_GRADES_I": _subscript_dict["ORE_GRADES_I"]}, ["ORE_GRADES_I"]
    )
    value.loc[["RICH_GRADE"]] = np.maximum(
        float(cu_known_reserves().loc["RICH_GRADE"])
        * cu_extraction_coefficient()
        * rich_grade_factor(),
        0,
    )
    value.loc[["HIGH_GRADE"]] = np.maximum(
        high_grade_factor()
        * float(cu_known_reserves().loc["HIGH_GRADE"])
        * cu_extraction_coefficient()
        * float(change_cu_grade().loc["HIGH_GRADE"]),
        0,
    )
    value.loc[["LOW_GRADE"]] = np.maximum(
        float(change_cu_grade().loc["LOW_GRADE"])
        * float(cu_known_reserves().loc["LOW_GRADE"])
        * cu_extraction_coefficient(),
        0,
    )
    value.loc[["ULTRALOW_GRADE"]] = np.maximum(
        float(change_cu_grade().loc["ULTRALOW_GRADE"])
        * cu_extraction_coefficient()
        * float(cu_known_reserves().loc["ULTRALOW_GRADE"])
        * float(change_cu_mining_technology_s_curve().loc["ULTRALOW_GRADE"]),
        0,
    )
    value.loc[["TRACE_GRADE"]] = np.maximum(
        float(change_cu_grade().loc["TRACE_GRADE"])
        * float(cu_known_reserves().loc["TRACE_GRADE"])
        * float(change_cu_mining_technology_s_curve().loc["TRACE_GRADE"])
        * cu_extraction_coefficient(),
        0,
    )
    value.loc[["OCEANS_GRADE"]] = np.maximum(
        float(change_cu_mining_technology_s_curve().loc["OCEANS_GRADE"])
        * cu_profit_push_ocean()
        * cu_extraction_coefficient()
        * float(cu_known_reserves().loc["OCEANS_GRADE"]),
        0,
    )
    return value


@component.add(
    name="Policy_recycling",
    comp_type="Auxiliary",
    comp_subtype="with Lookup",
    depends_on={"cu_price_economy": 1},
)
def policy_recycling():
    """
    Recycling amplifier influenced by price
    """
    return np.interp(
        cu_price_economy(),
        [
            0.0,
            250.0,
            500.0,
            750.0,
            1000.0,
            1250.0,
            1500.0,
            1750.0,
            2000.0,
            2250.0,
            2500.0,
            2750.0,
            3000.0,
            3250.0,
            3500.0,
            3750.0,
            4000.0,
            4250.0,
            4500.0,
            4750.0,
            5000.0,
            5250.0,
            5500.0,
            5750.0,
            6000.0,
            6250.0,
            6500.0,
            6750.0,
            7000.0,
            7250.0,
            7500.0,
            7750.0,
            8000.0,
            8250.0,
            8500.0,
            8750.0,
            9000.0,
            9250.0,
            9500.0,
            9750.0,
            10000.0,
            10250.0,
            10500.0,
            10750.0,
            11000.0,
            11250.0,
            11500.0,
            11750.0,
            12000.0,
            12250.0,
            12500.0,
            12750.0,
            13000.0,
            13250.0,
            13500.0,
            13750.0,
            14000.0,
            14250.0,
            14500.0,
            14750.0,
            15000.0,
            15250.0,
            15500.0,
            15750.0,
            16000.0,
            16250.0,
            16500.0,
            16750.0,
            17000.0,
            17250.0,
            17500.0,
            17750.0,
            18000.0,
            18250.0,
            18500.0,
            18750.0,
            19000.0,
            19250.0,
            19500.0,
            19750.0,
            20000.0,
            20250.0,
            20500.0,
            20750.0,
            21000.0,
            21250.0,
            21500.0,
            21750.0,
            22000.0,
            22250.0,
            22500.0,
            22750.0,
            23000.0,
            23250.0,
            23500.0,
            23750.0,
            24000.0,
            24250.0,
            24500.0,
            24750.0,
            25000.0,
        ],
        [
            0.286,
            0.274,
            0.274,
            0.274,
            0.286,
            0.286,
            0.286,
            0.286,
            0.286,
            0.286,
            0.298,
            0.298,
            0.298,
            0.308,
            0.32,
            0.332,
            0.342,
            0.354,
            0.366,
            0.378,
            0.388,
            0.4,
            0.412,
            0.4,
            0.412,
            0.422,
            0.434,
            0.446,
            0.468,
            0.48,
            0.486,
            0.492,
            0.502,
            0.526,
            0.538,
            0.572,
            0.582,
            0.594,
            0.606,
            0.628,
            0.628,
            0.64,
            0.652,
            0.663,
            0.674,
            0.698,
            0.72,
            0.731,
            0.742,
            0.766,
            0.778,
            0.788,
            0.812,
            0.822,
            0.834,
            0.858,
            0.868,
            0.88,
            0.891,
            0.902,
            0.926,
            0.938,
            0.96,
            0.972,
            0.982,
            0.994,
            1.018,
            1.029,
            1.04,
            1.062,
            1.068,
            1.074,
            1.098,
            1.108,
            1.12,
            1.12,
            1.132,
            1.132,
            1.142,
            1.154,
            1.166,
            1.166,
            1.178,
            1.188,
            1.2,
            1.206,
            1.212,
            1.222,
            1.222,
            1.234,
            1.234,
            1.234,
            1.234,
            1.23,
            1.23,
            1.23,
            1.23,
            1.23,
            1.23,
            1.23,
            1.23,
        ],
    )


@component.add(
    name="Policy_recycling_2",
    comp_type="Auxiliary",
    comp_subtype="with Lookup",
    depends_on={"cu_price_economy": 1},
)
def policy_recycling_2():
    return np.interp(
        cu_price_economy(),
        [
            0.0,
            187.5,
            375.0,
            562.5,
            750.0,
            937.5,
            1125.0,
            1312.5,
            1500.0,
            1687.5,
            1875.0,
            2062.5,
            2250.0,
            2437.5,
            2625.0,
            2812.5,
            3000.0,
            3187.5,
            3375.0,
            3562.5,
            3750.0,
            3937.5,
            4125.0,
            4312.5,
            4500.0,
            4687.5,
            4875.0,
            5062.5,
            5250.0,
            5437.5,
            5625.0,
            5812.5,
            6000.0,
            6187.5,
            6375.0,
            6562.5,
            6750.0,
            6937.5,
            7125.0,
            7312.5,
            7500.0,
            7687.5,
            7875.0,
            8062.5,
            8250.0,
            8437.5,
            8625.0,
            8812.5,
            9000.0,
            9187.5,
            9375.0,
            9562.5,
            9750.0,
            9937.5,
            10125.0,
            10312.5,
            10500.0,
            10687.5,
            10875.0,
            11062.5,
            11250.0,
            11437.5,
            11625.0,
            11812.5,
            12000.0,
            12187.5,
            12375.0,
            12562.5,
            12750.0,
            12937.5,
            13125.0,
            13312.5,
            13500.0,
            13687.5,
            13875.0,
            14062.5,
            14250.0,
            14437.5,
            14625.0,
            14812.5,
            15000.0,
            15187.5,
            15375.0,
            15562.5,
            15750.0,
            15937.5,
            16125.0,
            16312.5,
            16500.0,
            16687.5,
            16875.0,
            17062.5,
            17250.0,
            17437.5,
            17625.0,
            17812.5,
            18000.0,
            18187.5,
            18375.0,
            18562.5,
            18750.0,
        ],
        [
            0.286,
            0.274,
            0.274,
            0.274,
            0.286,
            0.286,
            0.286,
            0.286,
            0.286,
            0.286,
            0.298,
            0.298,
            0.298,
            0.308,
            0.32,
            0.332,
            0.342,
            0.354,
            0.366,
            0.378,
            0.388,
            0.4,
            0.412,
            0.4,
            0.412,
            0.422,
            0.434,
            0.446,
            0.468,
            0.48,
            0.486,
            0.492,
            0.502,
            0.526,
            0.538,
            0.572,
            0.582,
            0.594,
            0.606,
            0.628,
            0.628,
            0.64,
            0.652,
            0.663,
            0.674,
            0.698,
            0.72,
            0.731,
            0.742,
            0.766,
            0.778,
            0.788,
            0.812,
            0.822,
            0.834,
            0.858,
            0.868,
            0.88,
            0.891,
            0.902,
            0.926,
            0.938,
            0.96,
            0.972,
            0.982,
            0.994,
            1.018,
            1.029,
            1.04,
            1.062,
            1.068,
            1.074,
            1.098,
            1.108,
            1.12,
            1.12,
            1.132,
            1.132,
            1.142,
            1.154,
            1.166,
            1.166,
            1.178,
            1.188,
            1.2,
            1.206,
            1.212,
            1.222,
            1.222,
            1.234,
            1.234,
            1.234,
            1.234,
            1.23,
            1.23,
            1.23,
            1.23,
            1.23,
            1.23,
            1.23,
            1.23,
        ],
    )


@component.add(
    name="sum_hidden_resources",
    units="Mt",
    subscripts=["ORE_GRADES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"cu_hidden_resources": 1},
)
def sum_hidden_resources():
    """
    Sum of copper in all ore grades of resources.
    """
    return xr.DataArray(
        sum(
            cu_hidden_resources().rename({"ORE_GRADES_I": "ORE_GRADES_I!"}),
            dim=["ORE_GRADES_I!"],
        ),
        {"ORE_GRADES_I": _subscript_dict["ORE_GRADES_I"]},
        ["ORE_GRADES_I"],
    )


@component.add(
    name="sum_known_reserves",
    units="Mt",
    subscripts=["ORE_GRADES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"cu_known_reserves": 1},
)
def sum_known_reserves():
    """
    Sum of Copper in reserves over all ore grades.
    """
    return xr.DataArray(
        sum(
            cu_known_reserves().rename({"ORE_GRADES_I": "ORE_GRADES_I!"}),
            dim=["ORE_GRADES_I!"],
        ),
        {"ORE_GRADES_I": _subscript_dict["ORE_GRADES_I"]},
        ["ORE_GRADES_I"],
    )


@component.add(
    name="Sum_output_real",
    units="Mdollars_2015/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"output_real": 1},
)
def sum_output_real():
    """
    Sum of output real in the copper sector.
    """
    return sum(
        output_real()
        .loc[:, "MINING_AND_MANUFACTURING_COPPER"]
        .reset_coords(drop=True)
        .rename({"REGIONS_35_I": "REGIONS_35_I!"}),
        dim=["REGIONS_35_I!"],
    )


@component.add(
    name="Sum_total",
    units="Mt",
    subscripts=["ORE_GRADES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"sum_known_reserves": 1, "sum_hidden_resources": 1},
)
def sum_total():
    """
    Sum of all copper from all ore grade reserves and resources.
    """
    return sum_known_reserves() + sum_hidden_resources()


@component.add(
    name="SWITCH_Cu_RECYCLING_POLICY", comp_type="Constant", comp_subtype="Normal"
)
def switch_cu_recycling_policy():
    """
    This switch can take two values: 0: the (sub)module runs with BASE SCENARIIO for recycling 1: the (sub)module runs wit RECYCLING POLICY
    """
    return 0


@component.add(
    name="SWITCH_ECO2MAT_Cu_DEMAND",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_eco2mat_cu_demand"},
)
def switch_eco2mat_cu_demand():
    """
    Intermodule links SWITCH, it can take two values: 0: the link is broken, the intermodule variable is replaced by an exogenous parameter. 1: the link between modules is operational.
    """
    return _ext_constant_switch_eco2mat_cu_demand()


_ext_constant_switch_eco2mat_cu_demand = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_ECO2MAT_Cu_DEMAND",
    {},
    _root,
    {},
    "_ext_constant_switch_eco2mat_cu_demand",
)


@component.add(
    name="SWITCH_MAT2ECO_Cu_PRICE",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_mat2eco_cu_price"},
)
def switch_mat2eco_cu_price():
    """
    Intermodule links SWITCH, it can take two values: 0: the link is broken, the intermodule variable is replaced by an exogenous parameter. 1: the link between modules is operational.
    """
    return _ext_constant_switch_mat2eco_cu_price()


_ext_constant_switch_mat2eco_cu_price = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_MAT2ECO_Cu_PRICE",
    {},
    _root,
    {},
    "_ext_constant_switch_mat2eco_cu_price",
)


@component.add(
    name="SWITCH_MATERIALS",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_materials"},
)
def switch_materials():
    """
    This switch can take two values: 0: the (sub)module runs isolated from the rest of WILIAM, replacing inter(sub)module variables with exogenous parameters. 1: the (sub)module runs integrated with the rest of WILIAM.
    """
    return _ext_constant_switch_materials()


_ext_constant_switch_materials = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_MATERIALS",
    {},
    _root,
    {},
    "_ext_constant_switch_materials",
)


@component.add(
    name="TEST_LOOK_UP_Cu",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="with Lookup",
    depends_on={"time": 1},
)
def test_look_up_cu():
    """
    Economy Price signal- used to test the feedback of the model.
    """
    return np.interp(
        time(),
        [
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
        ],
        [100, 100, 80, 60, 60, 50, 40, 30, 30, 30, 30, 30, 30, 30, 30, 30],
    )


@component.add(
    name="total_Cu_known_reserves",
    units="Mt",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"cu_known_reserves": 1},
)
def total_cu_known_reserves():
    """
    Sum of reserves of copper from different Ore grades
    """
    return sum(
        cu_known_reserves().rename({"ORE_GRADES_I": "ORE_GRADES_I!"}),
        dim=["ORE_GRADES_I!"],
    )


@component.add(
    name="TOTAL_INITIAL_Cu_URR",
    units="Mt",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"initial_cu_hidden_resources": 1, "initial_cu_known_reserves": 1},
)
def total_initial_cu_urr():
    """
    initial availability of resources+reserves of copper
    """
    return sum(
        initial_cu_hidden_resources().rename({"ORE_GRADES_I": "ORE_GRADES_I!"})
        + initial_cu_known_reserves().rename({"ORE_GRADES_I": "ORE_GRADES_I!"}),
        dim=["ORE_GRADES_I!"],
    )


@component.add(
    name="Total_supply_from_scrap_old_and_new",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"cu_new_scrap": 1, "cu_recycled_to_cu_market": 1},
)
def total_supply_from_scrap_old_and_new():
    return cu_new_scrap() + cu_recycled_to_cu_market()


@component.add(
    name="water_Cu_extraction",
    units="Mm3/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"water_use_cu": 5, "water_use_cu_secondary": 1},
)
def water_cu_extraction():
    """
    Sum of water used for mining the different ore grades.
    """
    return (
        float(water_use_cu().loc["TRACE_GRADE"])
        + float(water_use_cu().loc["ULTRALOW_GRADE"])
        + float(water_use_cu().loc["LOW_GRADE"])
        + float(water_use_cu().loc["HIGH_GRADE"])
        + float(water_use_cu().loc["RICH_GRADE"])
        + water_use_cu_secondary()
    )


@component.add(
    name="WATER_FORECAST_COCHILICO_FOR_CHILE",
    units="Mm3/Years",
    comp_type="Auxiliary",
    comp_subtype="with Lookup",
    depends_on={"time": 1},
)
def water_forecast_cochilico_for_chile():
    """
    Data from figure 1 in (Lagos et at al, 2018). Data is for total energy concumption of Cu mining for chile, but chile is estimated to have 30% production in the world. Lagos, C., Carrasco, R., Soto, I., Fuertes, G., Alfaro, M., & Vargas, M. (2018). Predictive analysis of energy consumption in minining for making decisions. 2018 7th International Conference on Computers Communications and Control, ICCCC 2018 - Proceedings, 19, 270â€“275. https://doi.org/10.1109/ICCCC.2018.8390470
    """
    return np.interp(
        time(),
        [
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
        ],
        [
            499.824,
            569.03,
            614.553,
            633.315,
            677.608,
            694.217,
            727.129,
            731.127,
            732.973,
            742.815,
            765.269,
            779.725,
        ],
    )


@component.add(
    name="water_use_Cu",
    units="Mm3/Years",
    subscripts=["ORE_GRADES_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "mining_cu_known_reserves": 5,
        "water_use_per_cu": 5,
        "unit_conversion_mm3_m3": 5,
        "unit_conversion_t_mt": 5,
    },
)
def water_use_cu():
    """
    Water is a critical resource for mining and metal production processes. Use of water in the mining industry shares many of the characteristics of other industrial uses but it has some distinctive features that make it worth considering in further detail. (Prosser et al, 2011) Industrial water is used in the copper industry for various purposes, including direct and indirect cooling, waste transport, flotation, slag granulation and electrolysis. Copper Alliance members use the best available wastewater treatment techniques (as defined by the European Commission), which ensure that dissolved metals and solids are effectively removed. In addition, the purified water is increasingly reused, which significantly reduces the consumption of fresh water and further protects the environment and reduces the use of natural resources. (Prosser et al, 2011) Increasing production has used up most of the higher-grade ores so that the industry is increasingly accessing ores of lower quality, which require greater volumes of water to be used per tonne of metal produced. (Prosser et al, 2011) The average amount of water used per pound of copper mined varies from mine to mine and from year to year, as mining and processing rates change and as market prices fluctuate (Singh, 2010). Singh reports on water use (gallons) per pound of copper from 6,7-62,3 based on production data from DMMR files (Department of Minerals and Mines Resources). Prosser, I., Wolf, L., & Littleboy, A. (2011). Water in mining and industry. Water: Science and Solutions for Australia, 135â€“146. Singh, M. M. (2010). Water Consumption at Copper Mines in Arizona. State of Arizona Department of Mines and Mineral Resources, Special Report 29, December. m^3/t *Mt/years = Mm^3/years
    """
    value = xr.DataArray(
        np.nan, {"ORE_GRADES_I": _subscript_dict["ORE_GRADES_I"]}, ["ORE_GRADES_I"]
    )
    value.loc[["RICH_GRADE"]] = (
        float(mining_cu_known_reserves().loc["RICH_GRADE"])
        * float(water_use_per_cu().loc["RICH_GRADE"])
        * unit_conversion_mm3_m3()
        * unit_conversion_t_mt()
    )
    value.loc[["HIGH_GRADE"]] = (
        float(mining_cu_known_reserves().loc["HIGH_GRADE"])
        * float(water_use_per_cu().loc["HIGH_GRADE"])
        * unit_conversion_mm3_m3()
        * unit_conversion_t_mt()
    )
    value.loc[["LOW_GRADE"]] = (
        float(water_use_per_cu().loc["LOW_GRADE"])
        * float(mining_cu_known_reserves().loc["LOW_GRADE"])
        * unit_conversion_mm3_m3()
        * unit_conversion_t_mt()
    )
    value.loc[["ULTRALOW_GRADE"]] = (
        float(mining_cu_known_reserves().loc["ULTRALOW_GRADE"])
        * float(water_use_per_cu().loc["ULTRALOW_GRADE"])
        * unit_conversion_mm3_m3()
        * unit_conversion_t_mt()
    )
    value.loc[["TRACE_GRADE"]] = (
        float(water_use_per_cu().loc["TRACE_GRADE"])
        * float(mining_cu_known_reserves().loc["TRACE_GRADE"])
        * unit_conversion_mm3_m3()
        * unit_conversion_t_mt()
    )
    value.loc[["OCEANS_GRADE"]] = 0
    return value


@component.add(
    name="water_use_Cu_mining_and_recycling",
    units="Mm3/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"water_use_cu_recycle": 1, "water_cu_extraction": 1},
)
def water_use_cu_mining_and_recycling():
    """
    Increasing production has used up most of the higher-grade ores so that the industry is increasingly accessing ores of lower quality, which require greater volumes of water to be used per tonne of metal produced. There are strong prospects for further growth in iron ore extraction in coming decades and exponential growth of the burgeoning coal seam gas industry, which is also a major water user. Demand for water by the mining sector is therefore likely to increase, with projections ranging from 810 GL/year to 940 GL/year use by 2027 for Western Australia alone. Water is used by the minerals industry for the following operational activities: -Transport of ore and waste in slurries and suspensions -Separation of minerals through chemical processes -Physical separation of materials, such as in centrifugal separation -Cooling systems for power generation -Suppression of dust during mineral processing and around conveyors and roads -Washing equipment -Dewatering of mines. Prosser, I., Wolf, L., & Littleboy, A. (2011). Water in mining and industry. In Water: Science and Solutions for Australia (pp. 135-146).
    """
    return water_use_cu_recycle() + water_cu_extraction()


@component.add(
    name="water_use_Cu_recycle",
    units="Mm3/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"water_per_cu_recycle": 1, "cu_recycled_to_cu_market": 1},
)
def water_use_cu_recycle():
    """
    Water used for the recycled copper per year.
    """
    return water_per_cu_recycle() * cu_recycled_to_cu_market()


@component.add(
    name="water_use_Cu_secondary",
    units="Mm3/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"water_per_cu_secondary": 1, "cu_extraction": 1},
)
def water_use_cu_secondary():
    """
    Water reqiured for Cu mining and production from secondary mining. m3/ton is equivilent to saying Mm^3/Mt
    """
    return water_per_cu_secondary() * cu_extraction()


@component.add(
    name="water_use_per_Cu",
    units="m3/t",
    subscripts=["ORE_GRADES_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={"water_per_cu": 5},
)
def water_use_per_cu():
    """
    Water in m^3 needed per ton of different grade (ore quality)
    """
    value = xr.DataArray(
        np.nan, {"ORE_GRADES_I": _subscript_dict["ORE_GRADES_I"]}, ["ORE_GRADES_I"]
    )
    value.loc[["RICH_GRADE"]] = float(water_per_cu().loc["RICH_GRADE"])
    value.loc[["HIGH_GRADE"]] = float(water_per_cu().loc["HIGH_GRADE"])
    value.loc[["LOW_GRADE"]] = float(water_per_cu().loc["LOW_GRADE"])
    value.loc[["ULTRALOW_GRADE"]] = float(water_per_cu().loc["ULTRALOW_GRADE"])
    value.loc[["TRACE_GRADE"]] = float(water_per_cu().loc["TRACE_GRADE"])
    value.loc[["OCEANS_GRADE"]] = 0
    return value


@component.add(
    name="WORLD_TOTAL_ENERGY_CONSUMPTION_OF_Cu_MINING_HISTORICAL",
    units="TJ/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "world_share": 1,
        "chile_total_energy_consumption_of_cu_mining_historical": 1,
    },
)
def world_total_energy_consumption_of_cu_mining_historical():
    """
    Data from figure 1 in (Lagos et at al, 2018). Data is for total energy concumption of Cu mining for chile, but chile is estimated to have 30% production in the world, therefore we have multiplied with 3,3 Lagos, C., Carrasco, R., Soto, I., Fuertes, G., Alfaro, M., & Vargas, M. (2018). Predictive analysis of energy consumption in minining for making decisions. 2018 7th International Conference on Computers Communications and Control, ICCCC 2018 - Proceedings, 19, 270â€“275. https://doi.org/10.1109/ICCCC.2018.8390470
    """
    return world_share() * chile_total_energy_consumption_of_cu_mining_historical()


@component.add(
    name="WORLD_WATER_FORCAST_COCHILICO",
    units="Mm3/Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"world_share": 1, "water_forecast_cochilico_for_chile": 1},
)
def world_water_forcast_cochilico():
    """
    Data from figure 1 in (Lagos et at al, 2018). Data is for total energy concumption of Cu mining for chile, but chile is estimated to have 30% production in the world, therefore we have multiplied with 3,3 Lagos, C., Carrasco, R., Soto, I., Fuertes, G., Alfaro, M., & Vargas, M. (2018). Predictive analysis of energy consumption in minining for making decisions. 2018 7th International Conference on Computers Communications and Control, ICCCC 2018 - Proceedings, 19, 270â€“275. https://doi.org/10.1109/ICCCC.2018.8390470
    """
    return world_share() * water_forecast_cochilico_for_chile()


@component.add(
    name="x_values_for_Cu_demand_brakes",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"cu_price_per_ton": 1, "converter_x_values_for_cu_demand_brakes": 1},
)
def x_values_for_cu_demand_brakes():
    """
    This is the effect of price on demand and follows from the causal loop diagram in the copper paper. How this is conceptualized and parameterized is explained in the market papers. The actual curve itself has no previous documentation worth anything in earlier economy literature. The curve we use is our expert estimation, based on our research in the field and our experiments with the WORLD7 model. The variable controls the modified demand so that when the price is reasonable the variable has no effect on the demand but when the price gets higher it will modify the demand more and more. It's starts to kick in when the price is 3800 This array variable contains the constants for the fitted reversed sigmund curve. Following are the values: min 0,3 max 1 n 5 ec50 10 These are used in the equation: min+(max-min)/(1+10^(n*(log10(x)-log10(ec_50)))) This equations is the reversed S curve. It is 1 when it is close to zero and then starts to curve down when it reaches 3,8 and contiues to go down until it reaces 0,3 (min value) when x is 20. The x values are the "Cu price per ton" multiplied with 0,001 (needed to fit to the reversed S curve). Source: Sverdrup, H. U., & Olafsdottir, A. H. (2019). On the long-term sustainability of copper, zinc and lead supply, using a system dynamics model. Resources, Conservation & Recycling: X, 4(100007). https://doi.org/https://doi.org/10.1016/j.rcrx.2019.100007 Sverdrup, H. and Olafsdottir, A.H., 2019. Conceptualization and parameterization of the market price mechanism in the WORLD6 model for metals, materials and fossil fuels. Mineral Economics 1-26. Springer Nature DOI: 10.1007/s13563-019-00182-7. Olafsdottir, A.H. and Sverdrup, H., 2019. Defining a conceptual model for market mechanisms in food supply chains, and parameterizing price functions for coffee, wheat, corn, soy beans, beef and salmon. International Journal of Food System Dynamics 10: 151-175. doi:https://doi.org/10.18461/ijfsd.v10i2.14
    """
    return cu_price_per_ton() * converter_x_values_for_cu_demand_brakes()
