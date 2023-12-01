"""
Module materials.exogenous_inputs
Translated using PySD version 3.10.0
"""


@component.add(
    name="\"'a'_demand_projection_materials_RoE\"",
    subscripts=["MATERIALS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_a_demand_projection_materials_roe"},
)
def a_demand_projection_materials_roe():
    return _ext_constant_a_demand_projection_materials_roe()


_ext_constant_a_demand_projection_materials_roe = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "World",
    "a_demand_proyection_minerals_rest*",
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    _root,
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    "_ext_constant_a_demand_projection_materials_roe",
)


@component.add(
    name="ADDITIONAL_CU_EBIKES_IN_RELATION_TO_ICE",
    units="kg/vehicle",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_additional_cu_ebikes_in_relation_to_ice"
    },
)
def additional_cu_ebikes_in_relation_to_ice():
    """
    Cu requirements per vehicle (without taking account the battery) respect to traditional bike. The electrified vehicle possesses copper in addition to the battery content, this amount of copper can be seen that it is higher than the amount of copper used in a combustion vehicle which is about 23 kg (IDTechEx, 2017). To see the difference between the copper demand of these vehicles and the combustion or non-electrified vehicles, that they are intended to replace, only the amount of copper that electrified vehicles have over the latter will be taken into account in the evaluation. Hypotheses presented in order to obtain all necessary data: Ebikes vehicles -Single person electric vehicles (SEV/Ebike): The amount of copper is established by making it proportional to the weight of the 4-wheeled hybrid vehicle.
    """
    return _ext_constant_additional_cu_ebikes_in_relation_to_ice()


_ext_constant_additional_cu_ebikes_in_relation_to_ice = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "World",
    "ADDITIONAL_CU_EBIKES_IN_RELATION_TO_ICE",
    {},
    _root,
    {},
    "_ext_constant_additional_cu_ebikes_in_relation_to_ice",
)


@component.add(
    name="ADDITIONAL_CU_INLAND_EV_IN_RELATION_TO_ICE",
    units="kg/vehicle",
    subscripts=["TRANSPORT_POWER_TRAIN_I", "BATTERY_VEHICLES_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_additional_cu_inland_ev_in_relation_to_ice"
    },
)
def additional_cu_inland_ev_in_relation_to_ice():
    """
    Cu requirements per vehicle (without taking account the battery)respect to ICE vehicles. The electrified vehicle possesses copper in addition to the battery content, this amount of copper can be seen that it is higher than the amount of copper used in a combustion vehicle which is about 23 kg (IDTechEx, 2017). To see the difference between the copper demand of these vehicles and the combustion or non-electrified vehicles, that they are intended to replace, only the amount of copper that electrified vehicles have over the latter will be taken into account in the evaluation. Hypotheses presented in order to obtain all necessary data: Commercial vehicles -Heavy hybrid vehicles (HV HEV) (Lorry): Due to its similarities with the hybrid bus, the same amount of copper is established. -Lightweight electric vehicles (LV BEV) (small truck/van): Due to its similarities with the 4-wheel electric vehicle, the same amount of copper is established. -Lightweight hybrid vehicles (LV HEV) (small truck/van): Due to its similarities with the hybrid 4-wheeled private vehicle the same amount of copper is established. -Hybrid bus (bus HEV): This data has been obtained from the reference (IDTechEx study, How Important are Electric Vehicles for Future Copper Demand,2017). -Electric bus (bus BEV): The same ratio in the amount of copper is used between this bus and the hybrid bus as between the 4-wheel electric and the 4-wheel hybrid private vehicle.
    """
    return _ext_constant_additional_cu_inland_ev_in_relation_to_ice()


_ext_constant_additional_cu_inland_ev_in_relation_to_ice = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "World",
    "ADDITIONAL_CU_INLAND_VEHICLES_IN_RELATION_TO_ICE",
    {
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "BATTERY_VEHICLES_I": _subscript_dict["BATTERY_VEHICLES_I"],
    },
    _root,
    {
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "BATTERY_VEHICLES_I": _subscript_dict["BATTERY_VEHICLES_I"],
    },
    "_ext_constant_additional_cu_inland_ev_in_relation_to_ice",
)


@component.add(
    name="Al_LOW_GRADE_FACTOR_MINING",
    units="1/Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_al_low_grade_factor_mining"},
)
def al_low_grade_factor_mining():
    """
    This factor compensates for the fact that the high grade is much easier to mine - the Low grade needs more work. These numbers give the best fit to the historical data and therefore they are assumptions based parametersation of the ore grade curve. This consideration is taking the difference between high grade ores vs. lower grade ores into account. This particular parameter is for the low grade. -> 0.2
    """
    return _ext_constant_al_low_grade_factor_mining()


_ext_constant_al_low_grade_factor_mining = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Aluminium",
    "Al_LOW_GRADE_FACTOR_MINING",
    {},
    _root,
    {},
    "_ext_constant_al_low_grade_factor_mining",
)


@component.add(
    name='"All_minerals_virgin?"',
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_all_minerals_virgin"},
)
def all_minerals_virgin():
    """
    Switch for performing sensitivity analysis: 0. All minerals are virgin: current and future recycling rates set to W% (option to compare with results offline MEDEAS). 1. Real share of virgin/recycled minerals (for normal simulations).
    """
    return _ext_constant_all_minerals_virgin()


_ext_constant_all_minerals_virgin = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "World",
    "all_minerals_virgin",
    {},
    _root,
    {},
    "_ext_constant_all_minerals_virgin",
)


@component.add(
    name="AMOUNT_OF_Cu_IN_WEIGHT_OF_ROCK",
    units="DMNL",
    subscripts=["ORE_GRADES_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_amount_of_cu_in_weight_of_rock"},
)
def amount_of_cu_in_weight_of_rock():
    """
    This is in fractions, i.e. when it says 18, it is 18% of the ore weight, when it says 4 it is 4% of the ore weight This is based on averages found in the literature. See Olafsdottir, A.H., and Sverdrup, H., 2020, System dynamics modelling of mining, supply, recycling, stocks-in-use and market price for nickel. Mining, Metallurgy & Exploration. 1-22. 10.1007/s42461-020-00370- Sverdrup, H, Olafsdottir, A.H., Ragnarsdottir, K.V., 2019., Assessing global copper, zinc and lead extraction rates, supply, price and resources using the WORLD6 integrated assessment model. Resources, Conservation and Recycling 1-26. X4 100007. https://doi.org/10.1016/j.rcrx.2019.100007. Open access publication. Sverdrup, H., Olofsdottir, A.H., Ragnarsdottir, K.V., Koca, D., 2018. A system dynamics assessment of the supply of molybdenum and rhenium used for superalloys and specialty steels, using the WORLD6 model. Biophysical Economics and Resource Quality 4: 1-52 (DOI: 10.1007/s41247-018-0040-9)
    """
    return _ext_constant_amount_of_cu_in_weight_of_rock()


_ext_constant_amount_of_cu_in_weight_of_rock = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Copper",
    "AMOUNT_OF_Cu_IN_WEIGHT_OF_ROCK*",
    {"ORE_GRADES_I": _subscript_dict["ORE_GRADES_I"]},
    _root,
    {"ORE_GRADES_I": _subscript_dict["ORE_GRADES_I"]},
    "_ext_constant_amount_of_cu_in_weight_of_rock",
)


@component.add(
    name="AUTONOMY_EV_VEHICLES",
    units="km/cycle",
    subscripts=["TRANSPORT_POWER_TRAIN_I", "BATTERY_VEHICLES_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_autonomy_ev_vehicles"},
)
def autonomy_ev_vehicles():
    """
    Electric household vehicle range
    """
    return _ext_constant_autonomy_ev_vehicles()


_ext_constant_autonomy_ev_vehicles = ExtConstant(
    "model_parameters/energy/energy-transport.xlsx",
    "electrified_transport",
    "AUTONOMY_BATTERY_VEHICLES",
    {
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "BATTERY_VEHICLES_I": _subscript_dict["BATTERY_VEHICLES_I"],
    },
    _root,
    {
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "BATTERY_VEHICLES_I": _subscript_dict["BATTERY_VEHICLES_I"],
    },
    "_ext_constant_autonomy_ev_vehicles",
)


@component.add(
    name="AVERAGE_RESIDENCE_TIME_MINERAL_IN_REST_OF_THE_ECONOMY",
    units="Year",
    subscripts=["MATERIALS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_average_residence_time_mineral_in_rest_of_the_economy"
    },
)
def average_residence_time_mineral_in_rest_of_the_economy():
    """
    Average residence time of the minerals in the rest of the economy
    """
    return _ext_constant_average_residence_time_mineral_in_rest_of_the_economy()


_ext_constant_average_residence_time_mineral_in_rest_of_the_economy = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "World",
    "Average_residence_time*",
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    _root,
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    "_ext_constant_average_residence_time_mineral_in_rest_of_the_economy",
)


@component.add(
    name="AVERAGING_PROFIT_SIGNAL",
    units="Years",
    comp_type="Constant",
    comp_subtype="Normal",
)
def averaging_profit_signal():
    """
    Averaging the price signal over 1 year
    """
    return 1


@component.add(
    name="\"'b'_demand_projection_minerals_Rest\"",
    units="$/ton",
    subscripts=["MATERIALS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_b_demand_projection_minerals_rest"},
)
def b_demand_projection_minerals_rest():
    return _ext_constant_b_demand_projection_minerals_rest()


_ext_constant_b_demand_projection_minerals_rest = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "World",
    "b_demand_proyection_minerals_rest*",
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    _root,
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    "_ext_constant_b_demand_projection_minerals_rest",
)


@component.add(
    name="BATTERY_WEAR_FACTOR",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_battery_wear_factor"},
)
def battery_wear_factor():
    """
    Battery wear factor.The battery loses capacity over its useful life.
    """
    return _ext_constant_battery_wear_factor()


_ext_constant_battery_wear_factor = ExtConstant(
    "model_parameters/energy/energy-transport.xlsx",
    "electrified_transport",
    "BATTERY_WEAR_FACTOR",
    {},
    _root,
    {},
    "_ext_constant_battery_wear_factor",
)


@component.add(
    name="CAPACITY_PER_EV_CHARGER",
    units="kW/charger",
    subscripts=["EV_CHARGERS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_capacity_per_ev_charger"},
)
def capacity_per_ev_charger():
    """
    Capacity per EV chargers by type.The capacity has been estimated based on the chargers that are installed and those that are on the market.
    """
    return _ext_constant_capacity_per_ev_charger()


_ext_constant_capacity_per_ev_charger = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "World",
    "CAPACITY_PER_EV_CHARGER*",
    {"EV_CHARGERS_I": _subscript_dict["EV_CHARGERS_I"]},
    _root,
    {"EV_CHARGERS_I": _subscript_dict["EV_CHARGERS_I"]},
    "_ext_constant_capacity_per_ev_charger",
)


@component.add(
    name="CHEMICAL_RETENTION_TIME",
    units="Years",
    comp_type="Constant",
    comp_subtype="Normal",
)
def chemical_retention_time():
    """
    Chemicals have a short lifetime is society, we have assumed 1/4 year. The range is 0.1 to 1.5 years. Expert assumption
    """
    return 0.25


@component.add(
    name="CLEAN_WATER_INTENSITY_CSP_OM",
    units="kg/MW",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_clean_water_intensity_csp_om"},
)
def clean_water_intensity_csp_om():
    """
    Clean, pumper water intensity for operation and maintenance of solar CSP.
    """
    return _ext_constant_clean_water_intensity_csp_om()


_ext_constant_clean_water_intensity_csp_om = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "World",
    "clean_water_intensity_CSP_OM",
    {},
    _root,
    {},
    "_ext_constant_clean_water_intensity_csp_om",
)


@component.add(
    name="COEFFFICIENT_Mn_WATER_PER_RECYCLE",
    units="MtW/Mt",
    comp_type="Constant",
    comp_subtype="Normal",
)
def coeffficient_mn_water_per_recycle():
    """
    This is the energy and water used associated with the materials consumed to extract this specific resource grade, expressed in MJ/kg product and m3/ton. The actual values are taken from an internal LOCOMOTION report that have extracted the available values from literature and extrapolations. Source: Harald Sverdrup and Anna Hulda Olafsdottir 2021. Assessing with the WORLD7 model the global CO2 emissions and water use by metals, materials and fossil fuels extraction and production. LOCOMOTION working paper. 52 pages.
    """
    return 12


@component.add(
    name="COEFFICIENT_Al_WATER_PER_RECYCLING",
    units="MtW/Mt",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_coefficient_al_water_per_recycling"},
)
def coefficient_al_water_per_recycling():
    """
    Our own estimates of water use per grade extraction, based on a large literature survey. See the separate report for documentation of setting the value and where the information came from. value = 2MtW/Mt Sverdrup and Olafsdottir 2021: Assessing the global energy and water use from of metals, materials and fossil fuels extraction and production. Internal report for LOCOMOTION WP7. 44pp
    """
    return _ext_constant_coefficient_al_water_per_recycling()


_ext_constant_coefficient_al_water_per_recycling = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Aluminium",
    "COEFFICIENT_Al_WATER_PER_RECYCLING",
    {},
    _root,
    {},
    "_ext_constant_coefficient_al_water_per_recycling",
)


@component.add(
    name="COEFFICIENT_EQUATION_ELECTRIFIED_CONSTANT_A",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="Normal",
)
def coefficient_equation_electrified_constant_a():
    """
    Constants of the equation of the parabola joining the points (0.0) and (1.1) through the point (0.5.0.27)
    """
    return 0.92


@component.add(
    name="COEFFICIENT_EQUATION_ELECTRIFIED_CONSTANT_B",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="Normal",
)
def coefficient_equation_electrified_constant_b():
    """
    Constants of the equation of the parabola joining the points (0.0) and (1.1) through the point (0.5.0.27)
    """
    return 0.08


@component.add(
    name="COEFFICIENTS_CHANGE_Cu_GRADE",
    units="DMNL",
    subscripts=["ORE_GRADES_I", "S_CURVE_FIT_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_coefficients_change_cu_grade"},
)
def coefficients_change_cu_grade():
    """
    The switch grade curves are fitted to S curves with the following equation : y-fit=A*(1-exp(-k*t^n)) These are constants for s curve fit to switch to high grade: A= 1,004611737 k= 9,19418E-06 n= 3,032743095 t= 1% of Cu price per ton These are constants for s curve fit to switch to lowgrade: A=1,000399603 k= 1,03652E-05 n= 2,765444489 t= 1% of Cu price per ton These are constants for s curve fit to switch to ultralow grade: A= 1,126911355 k= 1,06041E-05 n= 2,415050438 t= 1% of Cu price per ton Constants for an s curve to switch to trace grade: A=1,018309484 k= 2,88082E-10 n= 4,316057291 t= 1% of Cu price per ton
    """
    return _ext_constant_coefficients_change_cu_grade()


_ext_constant_coefficients_change_cu_grade = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Copper",
    "COEFFICIENTS_CHANGE_Cu_GRADE",
    {
        "ORE_GRADES_I": _subscript_dict["ORE_GRADES_I"],
        "S_CURVE_FIT_I": _subscript_dict["S_CURVE_FIT_I"],
    },
    _root,
    {
        "ORE_GRADES_I": _subscript_dict["ORE_GRADES_I"],
        "S_CURVE_FIT_I": _subscript_dict["S_CURVE_FIT_I"],
    },
    "_ext_constant_coefficients_change_cu_grade",
)


@component.add(
    name="COEFFICIENTS_CHANGE_Cu_MINING_TECHNOLOGY_S_CURVE",
    units="DMNL",
    subscripts=["ORE_GRADES_I", "S_CURVE_FIT_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_coefficients_change_cu_mining_technology_s_curve"
    },
)
def coefficients_change_cu_mining_technology_s_curve():
    """
    This is a constant (1) representing the mining technology curves for rich, high and low grade. It is assumed that there are no such curves needed to include at this stage, therefore we use the constant 1 for these ore grades. The switch grade curves for ultra, trace and ocean technology are fitted to S curves with the following equation : y-fit=A*(1-exp(-k*t^n)) These are constants for s curve fit to switch to ultralow grade: A= 1 k= 2,88E-10 n= 4,4 t = time-start time These are constants for an s curve to switch to trace grade: A=1,34461147 k=1,15E-08 n=3,425207257 t = start time- time These are constants for an s curve to switch to ocean grade: A= 0,65 k= 1,01E-08 n= 3,655207257 t = start time- time The "S curve" innovation thinking is attributed to Richard Foster (1986) and made famous by Clayton Christensen in the book "Innovator's Dilemma," where he discusses how each successive computer hard drive industry was disrupted by a newer, more advanced technology.. Each of these S curves represent a technology platform. Movement up an S curve is incremental innovation while stepping down on a lower new S curve now, may lead to radical innovation, as the new Smcurve surpasses your existing S curve. There is a risk that the lower S curve does not get better. As, U. S. T., Stephen, A. G., & Novel, K. (1995). Jumping the technology S-curve. IEEE SPECTRUM, 49â€“54.
    """
    return _ext_constant_coefficients_change_cu_mining_technology_s_curve()


_ext_constant_coefficients_change_cu_mining_technology_s_curve = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Copper",
    "COEFFICIENTS_CHANGE_Cu_MINING_TECHNOLOGY_S_CURVE",
    {
        "ORE_GRADES_I": _subscript_dict["ORE_GRADES_I"],
        "S_CURVE_FIT_I": _subscript_dict["S_CURVE_FIT_I"],
    },
    _root,
    {
        "ORE_GRADES_I": _subscript_dict["ORE_GRADES_I"],
        "S_CURVE_FIT_I": _subscript_dict["S_CURVE_FIT_I"],
    },
    "_ext_constant_coefficients_change_cu_mining_technology_s_curve",
)


@component.add(
    name="COEFFICIENTS_Cu_DEMAND_BRAKES",
    units="DMNL",
    subscripts=["S_CURVE_FIT_REVERSE_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_coefficients_cu_demand_brakes"},
)
def coefficients_cu_demand_brakes():
    """
    The variable controls the modified demand so that when the price is reasonable the variable has no effect on the demand but when the price gets higher it will modify the demand more and more. It's starts to kick in when the price is 3800 This array variable contains the constants for the fitted reversed sigmund curve. Following are the values: min 0,3 max 1 n 5 ec50 10 These are used in the equation: min+(max-min)/(1+10^(n*(log10(x)-log10(ec_50)))) This equations is the reversed S curve. It is 1 when it is close to zero and then starts to curve down when it reaches 3,8 and contiues to go down until it reaces 0,3 (min value) when x is 20. The x values are the "Cu price per ton" multiplied with 0,001 (needed to fit to the reversed S curve). Source: Sverdrup, H. U., & Olafsdottir, A. H. (2019). On the long-term sustainability of copper, zinc and lead supply, using a system dynamics model. Resources, Conservation & Recycling: X, 4(100007). https://doi.org/https://doi.org/10.1016/j.rcrx.2019.100007
    """
    return _ext_constant_coefficients_cu_demand_brakes()


_ext_constant_coefficients_cu_demand_brakes = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Copper",
    "COEFFICIENTS_Cu_DEMAND_BRAKES*",
    {"S_CURVE_FIT_REVERSE_I": _subscript_dict["S_CURVE_FIT_REVERSE_I"]},
    _root,
    {"S_CURVE_FIT_REVERSE_I": _subscript_dict["S_CURVE_FIT_REVERSE_I"]},
    "_ext_constant_coefficients_cu_demand_brakes",
)


@component.add(
    name="COEFFICIENTS_Cu_DEMAND_PER_PERSON_BASED_ON_GDP",
    units="DMNL",
    subscripts=["LINEAR_LOG_FIT_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_coefficients_cu_demand_per_person_based_on_gdp"
    },
)
def coefficients_cu_demand_per_person_based_on_gdp():
    """
    This variable containes constants for the linear fit of the Cu demand per person based on gdp, that variable was a graphical variable in world7 but can be described with the following equation: y = 0,0004x + 3,55
    """
    return _ext_constant_coefficients_cu_demand_per_person_based_on_gdp()


_ext_constant_coefficients_cu_demand_per_person_based_on_gdp = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Copper",
    "COEFFICIENTS_Cu_DEMAND_PER_PERSON_BASED_ON_GDP*",
    {"LINEAR_LOG_FIT_I": _subscript_dict["LINEAR_LOG_FIT_I"]},
    _root,
    {"LINEAR_LOG_FIT_I": _subscript_dict["LINEAR_LOG_FIT_I"]},
    "_ext_constant_coefficients_cu_demand_per_person_based_on_gdp",
)


@component.add(
    name="COEFFICIENTS_Cu_ENERGY_USE",
    units="MJ/kg",
    subscripts=["ORE_GRADES_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_coefficients_cu_energy_use"},
)
def coefficients_cu_energy_use():
    """
    Table 4 in Koopelaar & Koppelaar (2016) give estimate that the total energy costs in MJ/kg for Cu consentrate range from both underground and surface between 5,6-66,6 MJ/Kg, with mean of 30,3 MJ/Kg Koppelaar, R. H. E. M., & Koppelaar, H. (2016). The Ore Grade and Depth Influence on Copper Energy Inputs. Biophysical Economics and Resource Quality, 1(2), 1-16. https://doi.org/10.1007/s41247-016-0012-x adjusted values based on the above: RG: 5,6 HG: 10 LG: 30,3 UL: 40 TG: 66,6 ------ OLD values Rich grade = 30 High grade = 60 Low grade = 180 Ultra low = 360 trace =720 values that fit to the data 8 15 25 100 720
    """
    return _ext_constant_coefficients_cu_energy_use()


_ext_constant_coefficients_cu_energy_use = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Copper",
    "COEFFICIENTS_Cu_ENERGY_USE*",
    {"ORE_GRADES_I": _subscript_dict["ORE_GRADES_I"]},
    _root,
    {"ORE_GRADES_I": _subscript_dict["ORE_GRADES_I"]},
    "_ext_constant_coefficients_cu_energy_use",
)


@component.add(
    name="COEFFICIENTS_Cu_EXTRACTION_COEFFICIENT",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_coefficients_cu_extraction_coefficient"},
)
def coefficients_cu_extraction_coefficient():
    """
    Constants for the Cu extraction Coeffiecient function. Function was previously a graphical variable. The function is calibrated to match the historical extraction. Graphical function and parameters of the function got estimated by curve fitting.
    """
    return _ext_constant_coefficients_cu_extraction_coefficient()


_ext_constant_coefficients_cu_extraction_coefficient = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Copper",
    "COEFFICIENTS_Cu_EXTRACTION_COEFFICIENT*",
    {},
    _root,
    {},
    "_ext_constant_coefficients_cu_extraction_coefficient",
)


@component.add(
    name="COEFFICIENTS_Cu_MARKET_PRICE",
    units="DMNL",
    subscripts=["LINEAR_LOG_FIT_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_coefficients_cu_market_price"},
)
def coefficients_cu_market_price():
    """
    This array variable contains the constants for the Cu price_per_ton variable: -9780*LN(cu_market) + 34798
    """
    return _ext_constant_coefficients_cu_market_price()


_ext_constant_coefficients_cu_market_price = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Copper",
    "COEFFICIENTS_Cu_MARKET_PRICE*",
    {"LINEAR_LOG_FIT_I": _subscript_dict["LINEAR_LOG_FIT_I"]},
    _root,
    {"LINEAR_LOG_FIT_I": _subscript_dict["LINEAR_LOG_FIT_I"]},
    "_ext_constant_coefficients_cu_market_price",
)


@component.add(
    name="COEFFICIENTS_Cu_MINING_EFFICIENCY_CURVE",
    units="DMNL",
    subscripts=["LINEAR_LOG_FIT_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_coefficients_cu_mining_efficiency_curve"
    },
)
def coefficients_cu_mining_efficiency_curve():
    """
    The Cu efficiency curve was a graphical variable in the world 7 model. A variable dependent on time that is expected to increase from 1850 until simulation end. It takes the value 1 around 1940-1960 and after that it increases up to 1,4 around 2000 and is expected to increase even more after that. The For simplification the curve was fitted with a linear equation, but this will be re-evaluated. =0,0089*TIME-16,315
    """
    return _ext_constant_coefficients_cu_mining_efficiency_curve()


_ext_constant_coefficients_cu_mining_efficiency_curve = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Copper",
    "COEFFICIENTS_Cu_MINING_EFFICIENCY_CURVE*",
    {"LINEAR_LOG_FIT_I": _subscript_dict["LINEAR_LOG_FIT_I"]},
    _root,
    {"LINEAR_LOG_FIT_I": _subscript_dict["LINEAR_LOG_FIT_I"]},
    "_ext_constant_coefficients_cu_mining_efficiency_curve",
)


@component.add(
    name="COEFFICIENTS_Cu_PRIMARY_DEMAND",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_coefficients_cu_primary_demand"},
)
def coefficients_cu_primary_demand():
    """
    COEFFIECIENT used to modify the demand to match the historical values.
    """
    return _ext_constant_coefficients_cu_primary_demand()


_ext_constant_coefficients_cu_primary_demand = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Copper",
    "COEFFICIENTS_Cu_PRIMARY_DEMAND*",
    {},
    _root,
    {},
    "_ext_constant_coefficients_cu_primary_demand",
)


@component.add(
    name="COEFFICIENTS_Cu_PROFIT_PUSH_OCEAN",
    units="DMNL",
    subscripts=["S_CURVE_FIT_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_coefficients_cu_profit_push_ocean"},
)
def coefficients_cu_profit_push_ocean():
    """
    This array contains constants for the Cu profit push ocean equation: A=1,46121186 k=9,43E-02 n=0,67837078
    """
    return _ext_constant_coefficients_cu_profit_push_ocean()


_ext_constant_coefficients_cu_profit_push_ocean = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Copper",
    "COEFFICIENTS_Cu_PROFIT_PUSH_OCEAN*",
    {"S_CURVE_FIT_I": _subscript_dict["S_CURVE_FIT_I"]},
    _root,
    {"S_CURVE_FIT_I": _subscript_dict["S_CURVE_FIT_I"]},
    "_ext_constant_coefficients_cu_profit_push_ocean",
)


@component.add(
    name="COEFFICIENTS_Cu_RECYCLED_TO_Cu_MARKET",
    units="1/Years",
    comp_type="Constant",
    comp_subtype="Normal",
)
def coefficients_cu_recycled_to_cu_market():
    """
    This says that it takes 0.5 years for copper from the moment it is scraped until it is ready refined. Expert Judgement of the Author: Harald U. Sverdrups personal industrial experience. GET DIRECT CONSTANTS('model_parameters/materials/materials.xlsx', 'Copper', 'COEFFICIENTS_Cu_RECYCLED_TO_Cu_MARKET*')
    """
    return 1.5


@component.add(
    name="COEFFICIENTS_Cu_SCRAP_COEFFICIENT",
    units="DMNL",
    subscripts=["S_CURVE_FIT_ABC_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_coefficients_cu_scrap_coefficient"},
)
def coefficients_cu_scrap_coefficient():
    """
    This array contains constants for the Cu scrapping coefficient equation: a=7,148535e-01 b=1,532671e-04 c=1,119455e+04
    """
    return _ext_constant_coefficients_cu_scrap_coefficient()


_ext_constant_coefficients_cu_scrap_coefficient = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Copper",
    "COEFFICIENTS_Cu_SCRAP_COEFFICIENT*",
    {"S_CURVE_FIT_ABC_I": _subscript_dict["S_CURVE_FIT_ABC_I"]},
    _root,
    {"S_CURVE_FIT_ABC_I": _subscript_dict["S_CURVE_FIT_ABC_I"]},
    "_ext_constant_coefficients_cu_scrap_coefficient",
)


@component.add(
    name="COEFFICIENTS_Cu_SCRAPPING",
    units="DMNL",
    subscripts=["S_CURVE_FIT_ABC_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_coefficients_cu_scrapping"},
)
def coefficients_cu_scrapping():
    """
    This array contains constants for the Cu scrapping coefficient equation. a= 1,253103e+01 b=9,626724e-05 c=3,390583e+04
    """
    return _ext_constant_coefficients_cu_scrapping()


_ext_constant_coefficients_cu_scrapping = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Copper",
    "COEFFICIENTS_Cu_SCRAPPING*",
    {"S_CURVE_FIT_ABC_I": _subscript_dict["S_CURVE_FIT_ABC_I"]},
    _root,
    {"S_CURVE_FIT_ABC_I": _subscript_dict["S_CURVE_FIT_ABC_I"]},
    "_ext_constant_coefficients_cu_scrapping",
)


@component.add(
    name="COEFFICIENTS_DECREASE_Cu_DEMAND_DELAY",
    units="1/Years",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_coefficients_decrease_cu_demand_delay"},
)
def coefficients_decrease_cu_demand_delay():
    """
    Internal delay to avoid circular connection. Can be any number implying a short delay
    """
    return _ext_constant_coefficients_decrease_cu_demand_delay()


_ext_constant_coefficients_decrease_cu_demand_delay = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Copper",
    "COEFFICIENTS_DECREASE_Cu_DEMAND_DELAY",
    {},
    _root,
    {},
    "_ext_constant_coefficients_decrease_cu_demand_delay",
)


@component.add(
    name="COEFFICIENTS_Fe_PRICE_INDEX",
    units="DMNL",
    subscripts=["LINEAR_LOG_FIT_I", "EQUATION_SPLIT_I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def coefficients_fe_price_index():
    """
    Original graphical variable from world 7- parameters derived from curve fitting. Source: Sverdrup, H., and Olafsdottir, A.H., 2019., Assessing the Longâ€Term Global Sustainability of the Production and Supply for Stainless Steel. Biophysical Economics and Resource Quality 1-26. https://doi.org/10.1007/s41247-019-0056-9 Open access publication. Sverdrup, H. and Ragnarsdottir, K.V., 2014. Natural Resources in a planetary perspective. Geochemical Perspectives Vol. 3, number 2, October issue 2014. 2:129-341. European Geochemical Society. Open access Sverdrup, H., and Olafsdottir, A.H., 2019. Conceptualization and parameterization of the market price mechanism in the WORLD6 model for metals, materials and fossil fuels. Mineral Economics 1-26. Springer Nature DOI: 10.1007/s13563-019-00182-7.
    """
    value = xr.DataArray(
        np.nan,
        {
            "LINEAR_LOG_FIT_I": _subscript_dict["LINEAR_LOG_FIT_I"],
            "EQUATION_SPLIT_I": _subscript_dict["EQUATION_SPLIT_I"],
        },
        ["LINEAR_LOG_FIT_I", "EQUATION_SPLIT_I"],
    )
    value.loc[["A_LINEAR_LOG_FIT"], ["EQUATION_ONE"]] = -2.5829
    value.loc[["A_LINEAR_LOG_FIT"], ["EQUATION_TWO"]] = 727.7
    value.loc[["A_LINEAR_LOG_FIT"], ["EQUATION_THREE"]] = 231.39
    value.loc[["B_LINEAR_LOG_FIT"], ["EQUATION_ONE"]] = 1109.5
    value.loc[["B_LINEAR_LOG_FIT"], ["EQUATION_TWO"]] = -0.001
    value.loc[["B_LINEAR_LOG_FIT"], ["EQUATION_THREE"]] = -0.0004
    return value


@component.add(
    name="COEFFICIENTS_INCREASE_Cu_DEMAND_DELAY",
    units="1/Years",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_coefficients_increase_cu_demand_delay"},
)
def coefficients_increase_cu_demand_delay():
    """
    Adjustment factor to match demand to reported demand. Sverdrup, H, Olafsdottir, A.H., Ragnarsdottir, K.V., 2019., Assessing global copper, zinc and lead extraction rates, supply, price and resources using the WORLD6 integrated assessment model. Resources, Conservation and Recycling 1-26. X4 100007. https://doi.org/10.1016/j.rcrx.2019.100007. Open access publication.
    """
    return _ext_constant_coefficients_increase_cu_demand_delay()


_ext_constant_coefficients_increase_cu_demand_delay = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Copper",
    "COEFFICIENTS_INCREASE_Cu_DEMAND_DELAY*",
    {},
    _root,
    {},
    "_ext_constant_coefficients_increase_cu_demand_delay",
)


@component.add(
    name="COEFFICIENTS_MINING_TECHNOLOGY_IMPROVEMENTS",
    units="DMNL",
    subscripts=["ORE_GRADES_I", "S_CURVE_FIT_ABC_I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def coefficients_mining_technology_improvements():
    """
    min+(max-min)/(1+10^(n*(log10(x)-log10(ec_50)))) Sigmoid Fitting - prospecting for Ni high and low low a=1,0358892 b=0,1549951 c=2023,9907121 Ultralow a= 0,9927459 b=0,1802690 c=2030,8311151
    """
    value = xr.DataArray(
        np.nan,
        {
            "ORE_GRADES_I": _subscript_dict["ORE_GRADES_I"],
            "S_CURVE_FIT_ABC_I": _subscript_dict["S_CURVE_FIT_ABC_I"],
        },
        ["ORE_GRADES_I", "S_CURVE_FIT_ABC_I"],
    )
    value.loc[["RICH_GRADE"], ["A_S_CURVE"]] = 0
    value.loc[["RICH_GRADE"], ["B_S_CURVE"]] = 0
    value.loc[["RICH_GRADE"], ["C_S_CURVE"]] = 0
    value.loc[["HIGH_GRADE"], ["A_S_CURVE"]] = 0
    value.loc[["HIGH_GRADE"], ["B_S_CURVE"]] = 0
    value.loc[["HIGH_GRADE"], ["C_S_CURVE"]] = 0
    value.loc[["LOW_GRADE"], ["A_S_CURVE"]] = 1.03589
    value.loc[["LOW_GRADE"], ["B_S_CURVE"]] = 0.154995
    value.loc[["LOW_GRADE"], ["C_S_CURVE"]] = 2023.99
    value.loc[["ULTRALOW_GRADE"], ["A_S_CURVE"]] = 0.992746
    value.loc[["ULTRALOW_GRADE"], ["B_S_CURVE"]] = 0.180269
    value.loc[["ULTRALOW_GRADE"], ["C_S_CURVE"]] = 2030.83
    value.loc[["TRACE_GRADE"], ["A_S_CURVE"]] = 0.992746
    value.loc[["TRACE_GRADE"], ["B_S_CURVE"]] = 0.180269
    value.loc[["TRACE_GRADE"], ["C_S_CURVE"]] = 2030.83
    value.loc[["OCEANS_GRADE"], ["A_S_CURVE"]] = 0
    value.loc[["OCEANS_GRADE"], ["B_S_CURVE"]] = 0
    value.loc[["OCEANS_GRADE"], ["C_S_CURVE"]] = 0
    return value


@component.add(
    name="COEFFICIENTS_Mo_DEMAND_PER_PERSON",
    units="Mt/Million_persons",
    subscripts=["S_CURVE_FIT_ABC_I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def coefficients_mo_demand_per_person():
    """
    A=9,315790209 B=0,027165746 C=2016,457217 response curve transformation
    """
    value = xr.DataArray(
        np.nan,
        {"S_CURVE_FIT_ABC_I": _subscript_dict["S_CURVE_FIT_ABC_I"]},
        ["S_CURVE_FIT_ABC_I"],
    )
    value.loc[["A_S_CURVE"]] = 9.31579
    value.loc[["B_S_CURVE"]] = 0.0271657
    value.loc[["C_S_CURVE"]] = 2016.46
    return value


@component.add(
    name="COEFFICIENTS_Mo_MINING_EFFICIENCY",
    units="DMNL",
    subscripts=["S_CURVE_FIT_ABC_I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def coefficients_mo_mining_efficiency():
    """
    A=0,901585882 B=0,148171518 C=1908,0398 Curve parameterization
    """
    value = xr.DataArray(
        np.nan,
        {"S_CURVE_FIT_ABC_I": _subscript_dict["S_CURVE_FIT_ABC_I"]},
        ["S_CURVE_FIT_ABC_I"],
    )
    value.loc[["A_S_CURVE"]] = 0.901586
    value.loc[["B_S_CURVE"]] = 0.148172
    value.loc[["C_S_CURVE"]] = 1908.04
    return value


@component.add(
    name="COEFFICIENTS_Mo_PROFIT_EFFECT_ON_MINING",
    units="DMNL",
    subscripts=["S_CURVE_FIT_ABC_I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def coefficients_mo_profit_effect_on_mining():
    value = xr.DataArray(
        np.nan,
        {"S_CURVE_FIT_ABC_I": _subscript_dict["S_CURVE_FIT_ABC_I"]},
        ["S_CURVE_FIT_ABC_I"],
    )
    value.loc[["A_S_CURVE"]] = 3.6
    value.loc[["B_S_CURVE"]] = 0.00015
    value.loc[["C_S_CURVE"]] = 10000
    return value


@component.add(
    name="COEFFICIENTS_Mo_PROSPECTING_RATE",
    units="DMNL",
    subscripts=["S_CURVE_FIT_ABC_I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def coefficients_mo_prospecting_rate():
    """
    A=0,010920687 B=0,048152583 C=1956,553193 Parameterization of the response curve for prospecting activity over time. Follow a general technology development curve as used for Cu
    """
    value = xr.DataArray(
        np.nan,
        {"S_CURVE_FIT_ABC_I": _subscript_dict["S_CURVE_FIT_ABC_I"]},
        ["S_CURVE_FIT_ABC_I"],
    )
    value.loc[["A_S_CURVE"]] = 0.0109207
    value.loc[["B_S_CURVE"]] = 0.0481526
    value.loc[["C_S_CURVE"]] = 1956.55
    return value


@component.add(
    name="COEFFICIENTS_Mo_RECYCLING_PROFIT_DRIVE",
    units="DMNL",
    subscripts=["S_CURVE_FIT_ABC_I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def coefficients_mo_recycling_profit_drive():
    """
    A=1,024718121 B=5,3913E-05 C=40446,02658 parameterization of response curve Sverdrup, H., Olofsdottir, A.H., Ragnarsdottir, K.V., Koca, D., 2018. A system dynamics assessment of the supply of molybdenum and rhenium used for superalloys and specialty steels, using the WORLD6 model. Biophysical Economics and Resource Quality 4: 1-52 (DOI: 10.1007/s41247-018-0040-9)
    """
    value = xr.DataArray(
        np.nan,
        {"S_CURVE_FIT_ABC_I": _subscript_dict["S_CURVE_FIT_ABC_I"]},
        ["S_CURVE_FIT_ABC_I"],
    )
    value.loc[["A_S_CURVE"]] = 1.02472
    value.loc[["B_S_CURVE"]] = 5.3913e-05
    value.loc[["C_S_CURVE"]] = 40446
    return value


@component.add(
    name="COEFFICIENTS_Mo_TECHNOLOGY_PROGRESS",
    subscripts=["S_CURVE_FIT_ABC_I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def coefficients_mo_technology_progress():
    value = xr.DataArray(
        np.nan,
        {"S_CURVE_FIT_ABC_I": _subscript_dict["S_CURVE_FIT_ABC_I"]},
        ["S_CURVE_FIT_ABC_I"],
    )
    value.loc[["A_S_CURVE"]] = 0.998934
    value.loc[["B_S_CURVE"]] = 0.559513
    value.loc[["C_S_CURVE"]] = 1911.14
    return value


@component.add(
    name="COEFFICIENTS_Ni_CHANGE_GRADE",
    units="DMNL",
    subscripts=["ORE_GRADES_I", "S_CURVE_FIT_ABC_I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def coefficients_ni_change_grade():
    """
    High a b c 1.011893e+00 9.304567e-04 5.732495e+03 low a b c 1.007316e+00 3.649836e-04 1.283400e+04 ultralow a b c 9.935764e-01 4.086965e-04 2.853978e+04 trace a b c 9.843507e-01 3.697002e-04 4.576003e+04 Harald Sverdrup, 2021: LOCOMOTION Project report: Estimating the cost of extraction and the price required for changing between mining of different ore grades in the WORLD7 model. 20 pp.
    """
    value = xr.DataArray(
        np.nan,
        {
            "ORE_GRADES_I": _subscript_dict["ORE_GRADES_I"],
            "S_CURVE_FIT_ABC_I": _subscript_dict["S_CURVE_FIT_ABC_I"],
        },
        ["ORE_GRADES_I", "S_CURVE_FIT_ABC_I"],
    )
    value.loc[["RICH_GRADE"], ["A_S_CURVE"]] = 0
    value.loc[["RICH_GRADE"], ["B_S_CURVE"]] = 0
    value.loc[["RICH_GRADE"], ["C_S_CURVE"]] = 0
    value.loc[["HIGH_GRADE"], ["A_S_CURVE"]] = 1
    value.loc[["HIGH_GRADE"], ["B_S_CURVE"]] = 0.000930457
    value.loc[["HIGH_GRADE"], ["C_S_CURVE"]] = 5732.5
    value.loc[["LOW_GRADE"], ["A_S_CURVE"]] = 1
    value.loc[["LOW_GRADE"], ["B_S_CURVE"]] = 0.000364984
    value.loc[["LOW_GRADE"], ["C_S_CURVE"]] = 12834
    value.loc[["ULTRALOW_GRADE"], ["A_S_CURVE"]] = 1
    value.loc[["ULTRALOW_GRADE"], ["B_S_CURVE"]] = 0.000408697
    value.loc[["ULTRALOW_GRADE"], ["C_S_CURVE"]] = 28539.8
    value.loc[["TRACE_GRADE"], ["A_S_CURVE"]] = 1
    value.loc[["TRACE_GRADE"], ["B_S_CURVE"]] = 0.0003697
    value.loc[["TRACE_GRADE"], ["C_S_CURVE"]] = 45760
    value.loc[["OCEANS_GRADE"], ["A_S_CURVE"]] = 0
    value.loc[["OCEANS_GRADE"], ["B_S_CURVE"]] = 0
    value.loc[["OCEANS_GRADE"], ["C_S_CURVE"]] = 0
    return value


@component.add(
    name="COEFFICIENTS_PROSPECTING_ACTIVITY",
    subscripts=["LINEAR_LOG_FIT_I", "EQUATION_SPLIT_I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def coefficients_prospecting_activity():
    """
    Activity regarding prospecting is effected by the Fe price. With a higher price the prospecting activity, the will to prospect is rising with lower price the will to prospect is lower since the profit incentive is lower. Curve originates from World7. In world7 variables were graphical variables. Coefficients are derived from curve fitting the graphical variables. Source: Sverdrup, H., and Olafsdottir, A.H., 2019., Assessing the Longâ€Term Global Sustainability of the Production and Supply for Stainless Steel. Biophysical Economics and Resource Quality 1-26. https://doi.org/10.1007/s41247-019-0056-9 Open access publication. Sverdrup, H. and Ragnarsdottir, K.V., 2014. Natural Resources in a planetary perspective. Geochemical Perspectives Vol. 3, number 2, October issue 2014. 2:129-341. European Geochemical Society. Open access
    """
    value = xr.DataArray(
        np.nan,
        {
            "LINEAR_LOG_FIT_I": _subscript_dict["LINEAR_LOG_FIT_I"],
            "EQUATION_SPLIT_I": _subscript_dict["EQUATION_SPLIT_I"],
        },
        ["LINEAR_LOG_FIT_I", "EQUATION_SPLIT_I"],
    )
    value.loc[["A_LINEAR_LOG_FIT"], ["EQUATION_ONE"]] = 0.0085
    value.loc[["A_LINEAR_LOG_FIT"], ["EQUATION_TWO"]] = 0.0405
    value.loc[["A_LINEAR_LOG_FIT"], ["EQUATION_THREE"]] = 0
    value.loc[["B_LINEAR_LOG_FIT"], ["EQUATION_ONE"]] = 0.0507
    value.loc[["B_LINEAR_LOG_FIT"], ["EQUATION_TWO"]] = 0.0214
    value.loc[["B_LINEAR_LOG_FIT"], ["EQUATION_THREE"]] = 0
    return value


@component.add(
    name="COEFFICIENTS_PROSPECTING_DRIVE",
    units="DMNL",
    subscripts=["LINEAR_LOG_FIT_I", "EQUATION_SPLIT_I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def coefficients_prospecting_drive():
    """
    Parameterization of prospecting and finding response curve. Sverdrup, H., and Olafsdottir, A.H., 2019., Assessing the Longâ€Term Global Sustainability of the Production and Supply for Stainless Steel. Biophysical Economics and Resource Quality 1-26. https://doi.org/10.1007/s41247-019-0056-9 Open access publication. Sverdrup, H. and Ragnarsdottir, K.V., 2014. Natural Resources in a planetary perspective. Geochemical Perspectives Vol. 3, number 2, October issue 2014. 2:129-341. European Geochemical Society. Open access
    """
    value = xr.DataArray(
        np.nan,
        {
            "LINEAR_LOG_FIT_I": _subscript_dict["LINEAR_LOG_FIT_I"],
            "EQUATION_SPLIT_I": _subscript_dict["EQUATION_SPLIT_I"],
        },
        ["LINEAR_LOG_FIT_I", "EQUATION_SPLIT_I"],
    )
    value.loc[["A_LINEAR_LOG_FIT"], ["EQUATION_ONE"]] = -0.0003
    value.loc[["A_LINEAR_LOG_FIT"], ["EQUATION_TWO"]] = 2.877
    value.loc[["A_LINEAR_LOG_FIT"], ["EQUATION_THREE"]] = 0
    value.loc[["B_LINEAR_LOG_FIT"], ["EQUATION_ONE"]] = 2.753
    value.loc[["B_LINEAR_LOG_FIT"], ["EQUATION_TWO"]] = -0.109
    value.loc[["B_LINEAR_LOG_FIT"], ["EQUATION_THREE"]] = 0
    return value


@component.add(
    name="COEFFICIENTS_PROSPECTING_FROM_ALL",
    units="DMNL",
    subscripts=["S_CURVE_FIT_REVERSE_I", "ORE_GRADES_I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def coefficients_prospecting_from_all():
    """
    min+(max-min)/(1+10^(n*(log10(x)-log10(ec_50)))) High grade: Sigmoid Fitting - prospecting for Ni high and low n 7,684334811 min 0,010589989 max 2,005044986 ec50 5,53505278 low grade: n 7,922850142 min -0,033393353 max 1,975174461 ec50 5,539989466 ULG n 9,293426946 min -0,019635893 max 1,977579607 ec50 6,081686643 trace n 9,293426946 min -0,019635893 max 1,977579607 ec50 6,081686643
    """
    value = xr.DataArray(
        np.nan,
        {
            "S_CURVE_FIT_REVERSE_I": _subscript_dict["S_CURVE_FIT_REVERSE_I"],
            "ORE_GRADES_I": _subscript_dict["ORE_GRADES_I"],
        },
        ["S_CURVE_FIT_REVERSE_I", "ORE_GRADES_I"],
    )
    value.loc[["N"], ["RICH_GRADE"]] = 0.05
    value.loc[["N"], ["HIGH_GRADE"]] = 7.68433
    value.loc[["N"], ["LOW_GRADE"]] = 7.6
    value.loc[["N"], ["ULTRALOW_GRADE"]] = 9.29343
    value.loc[["N"], ["TRACE_GRADE"]] = 9.29343
    value.loc[["N"], ["OCEANS_GRADE"]] = 0
    value.loc[["MIN_VALUE"], ["RICH_GRADE"]] = 0.05
    value.loc[["MIN_VALUE"], ["HIGH_GRADE"]] = 0.05
    value.loc[["MIN_VALUE"], ["LOW_GRADE"]] = 0.05
    value.loc[["MIN_VALUE"], ["ULTRALOW_GRADE"]] = 0
    value.loc[["MIN_VALUE"], ["TRACE_GRADE"]] = 0
    value.loc[["MIN_VALUE"], ["OCEANS_GRADE"]] = 0
    value.loc[["MAX_VALUE"], ["RICH_GRADE"]] = 0.05
    value.loc[["MAX_VALUE"], ["HIGH_GRADE"]] = 2.00504
    value.loc[["MAX_VALUE"], ["LOW_GRADE"]] = 2.00504
    value.loc[["MAX_VALUE"], ["ULTRALOW_GRADE"]] = 1.97758
    value.loc[["MAX_VALUE"], ["TRACE_GRADE"]] = 2
    value.loc[["MAX_VALUE"], ["OCEANS_GRADE"]] = 0
    value.loc[["EC50"], ["RICH_GRADE"]] = 0.05
    value.loc[["EC50"], ["HIGH_GRADE"]] = 5.53505
    value.loc[["EC50"], ["LOW_GRADE"]] = 5.53
    value.loc[["EC50"], ["ULTRALOW_GRADE"]] = 6.08169
    value.loc[["EC50"], ["TRACE_GRADE"]] = 6.08169
    value.loc[["EC50"], ["OCEANS_GRADE"]] = 0
    return value


@component.add(
    name="COEFFICIENTS_PROSPECTING_FROM_GRADES",
    units="DMNL",
    subscripts=["S_CURVE_FIT_REVERSE_I", "ORE_GRADES_I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def coefficients_prospecting_from_grades():
    """
    min+(max-min)/(1+10^(n*(log10(x)-log10(ec_50)))) High grade: Sigmoid Fitting - prospecting for Ni high and low n 7,684334811 min 0,010589989 max 2,005044986 ec50 5,53505278 low grade: n 7,922850142 min -0,033393353 max 1,975174461 ec50 5,539989466 ULG n 9,293426946 min -0,019635893 max 1,977579607 ec50 6,081686643 trace n 9,293426946 min -0,019635893 max 1,977579607 ec50 6,081686643 Olafsdottir, A.H., and Sverdrup, H., 2020, System dynamics modelling of mining, supply, recycling, stocks-in-use and market price for nickel. Mining, Metallurgy & Exploration. 1-22. 10.1007/s42461-020-00370-
    """
    value = xr.DataArray(
        np.nan,
        {
            "S_CURVE_FIT_REVERSE_I": _subscript_dict["S_CURVE_FIT_REVERSE_I"],
            "ORE_GRADES_I": _subscript_dict["ORE_GRADES_I"],
        },
        ["S_CURVE_FIT_REVERSE_I", "ORE_GRADES_I"],
    )
    value.loc[["N"], ["RICH_GRADE"]] = 0.05
    value.loc[["N"], ["HIGH_GRADE"]] = 7.68433
    value.loc[["N"], ["LOW_GRADE"]] = 7.92285
    value.loc[["N"], ["ULTRALOW_GRADE"]] = 9.29343
    value.loc[["N"], ["TRACE_GRADE"]] = 9.29343
    value.loc[["N"], ["OCEANS_GRADE"]] = 0
    value.loc[["MIN_VALUE"], ["RICH_GRADE"]] = 0.05
    value.loc[["MIN_VALUE"], ["HIGH_GRADE"]] = 0
    value.loc[["MIN_VALUE"], ["LOW_GRADE"]] = 0.05
    value.loc[["MIN_VALUE"], ["ULTRALOW_GRADE"]] = 0.01
    value.loc[["MIN_VALUE"], ["TRACE_GRADE"]] = 0.05
    value.loc[["MIN_VALUE"], ["OCEANS_GRADE"]] = 0
    value.loc[["MAX_VALUE"], ["RICH_GRADE"]] = 0.05
    value.loc[["MAX_VALUE"], ["HIGH_GRADE"]] = 2.00504
    value.loc[["MAX_VALUE"], ["LOW_GRADE"]] = 1.97517
    value.loc[["MAX_VALUE"], ["ULTRALOW_GRADE"]] = 1.97758
    value.loc[["MAX_VALUE"], ["TRACE_GRADE"]] = 2
    value.loc[["MAX_VALUE"], ["OCEANS_GRADE"]] = 0
    value.loc[["EC50"], ["RICH_GRADE"]] = 0.05
    value.loc[["EC50"], ["HIGH_GRADE"]] = 5.53505
    value.loc[["EC50"], ["LOW_GRADE"]] = 5.53999
    value.loc[["EC50"], ["ULTRALOW_GRADE"]] = 6.08169
    value.loc[["EC50"], ["TRACE_GRADE"]] = 6.08169
    value.loc[["EC50"], ["OCEANS_GRADE"]] = 0
    return value


@component.add(
    name="COEFFICIENTS_PROSPECTING_TECHNOLOGY_IMPROVEMENTS",
    units="DMNL",
    subscripts=["ORE_GRADES_I", "S_CURVE_FIT_ABC_I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def coefficients_prospecting_technology_improvements():
    """
    min+(max-min)/(1+10^(n*(log10(x)-log10(ec_50)))) Sigmoid Fitting - prospecting for Ni high and low rich, high, low grade: a=1,002058e+01 b=2,783543e-02 c=1,967250e+03 ultralow grade: a=1,040143e+01 b=1,332233e-02 c=2,148622e+03 trace a= 0,9927459 b=0,1802690 c=2030,8311151 new a=1,040143e+01 b=1,332233e-02 c=2,148622e+03
    """
    value = xr.DataArray(
        np.nan,
        {
            "ORE_GRADES_I": _subscript_dict["ORE_GRADES_I"],
            "S_CURVE_FIT_ABC_I": _subscript_dict["S_CURVE_FIT_ABC_I"],
        },
        ["ORE_GRADES_I", "S_CURVE_FIT_ABC_I"],
    )
    value.loc[["RICH_GRADE"], ["A_S_CURVE"]] = 10.0206
    value.loc[["RICH_GRADE"], ["B_S_CURVE"]] = 0.0278354
    value.loc[["RICH_GRADE"], ["C_S_CURVE"]] = 1967.25
    value.loc[["HIGH_GRADE"], ["A_S_CURVE"]] = 10.0206
    value.loc[["HIGH_GRADE"], ["B_S_CURVE"]] = 0.0278354
    value.loc[["HIGH_GRADE"], ["C_S_CURVE"]] = 1967.25
    value.loc[["LOW_GRADE"], ["A_S_CURVE"]] = 10.0206
    value.loc[["LOW_GRADE"], ["B_S_CURVE"]] = 0.0278354
    value.loc[["LOW_GRADE"], ["C_S_CURVE"]] = 1967.25
    value.loc[["ULTRALOW_GRADE"], ["A_S_CURVE"]] = 10.4014
    value.loc[["ULTRALOW_GRADE"], ["B_S_CURVE"]] = 0.0133223
    value.loc[["ULTRALOW_GRADE"], ["C_S_CURVE"]] = 2148.62
    value.loc[["TRACE_GRADE"], ["A_S_CURVE"]] = 10.4014
    value.loc[["TRACE_GRADE"], ["B_S_CURVE"]] = 0.0133223
    value.loc[["TRACE_GRADE"], ["C_S_CURVE"]] = 2148.62
    value.loc[["OCEANS_GRADE"], ["A_S_CURVE"]] = 0
    value.loc[["OCEANS_GRADE"], ["B_S_CURVE"]] = 0
    value.loc[["OCEANS_GRADE"], ["C_S_CURVE"]] = 0
    return value


@component.add(
    name="COEFFICIENTS_SUPERALLOYS_TECHNOLOGY_PROGRESS",
    units="DMNL",
    subscripts=["S_CURVE_FIT_ABC_I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def coefficients_superalloys_technology_progress():
    """
    A=0,942779135 B=0,031955642 C=2003,786697 Parameterization of the increase in superalloy use over time. Sverdrup, H., Olofsdottir, A.H., Ragnarsdottir, K.V., Koca, D., 2018. A system dynamics assessment of the supply of molybdenum and rhenium used for superalloys and specialty steels, using the WORLD6 model. Biophysical Economics and Resource Quality 4: 1-52 (DOI: 10.1007/s41247-018-0040-9)
    """
    value = xr.DataArray(
        np.nan,
        {"S_CURVE_FIT_ABC_I": _subscript_dict["S_CURVE_FIT_ABC_I"]},
        ["S_CURVE_FIT_ABC_I"],
    )
    value.loc[["A_S_CURVE"]] = 0.942779
    value.loc[["B_S_CURVE"]] = 0.0319556
    value.loc[["C_S_CURVE"]] = 2003.79
    return value


@component.add(
    name="CONVERTER_X_VALUES_FOR_Cu_DEMAND_BRAKES",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_converter_x_values_for_cu_demand_brakes"
    },
)
def converter_x_values_for_cu_demand_brakes():
    """
    X values for for the Cu demand brake function.
    """
    return _ext_constant_converter_x_values_for_cu_demand_brakes()


_ext_constant_converter_x_values_for_cu_demand_brakes = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Copper",
    "CONVERTER_X_VALUES_FOR_Cu_DEMAND_BRAKES*",
    {},
    _root,
    {},
    "_ext_constant_converter_x_values_for_cu_demand_brakes",
)


@component.add(
    name="Cu_CONTENT_IN_METALS",
    units="DMNL",
    subscripts=["CU_CONTENT_IN_METALS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_cu_content_in_metals"},
)
def cu_content_in_metals():
    """
    This is an array variable that shows the fractions of cu content in other metals. CU_CONTENT_IN_METALS[CU_IN_ZN] = 0,15 CU_CONTENT_IN_METALS[CU_IN_MO] = 3,8 CU_CONTENT_IN_METALS[CU_IN_NI] = 1 CU_CONTENT_IN_METALS[CU_IN_AG] = 0,08 CU_CONTENT_IN_METALS[CU_IN_PGM] = 500 Reference: Olafsdottir, A.H., and Sverdrup, H., 2020, System dynamics modelling of mining, supply, recycling, stocks-in-use and market price for nickel. Mining, Metallurgy & Exploration. 1-22. 10.1007/s42461-020-00370- Sverdrup, H, Olafsdottir, A.H., Ragnarsdottir, K.V., 2019., Assessing global copper, zinc and lead extraction rates, supply, price and resources using the WORLD6 integrated assessment model. Resources, Conservation and Recycling 1-26. X4 100007. https://doi.org/10.1016/j.rcrx.2019.100007. Open access publication. Sverdrup, H., Olofsdottir, A.H., Ragnarsdottir, K.V., Koca, D., 2018. A system dynamics assessment of the supply of molybdenum and rhenium used for superalloys and specialty steels, using the WORLD6 model. Biophysical Economics and Resource Quality 4: 1-52 (DOI: 10.1007/s41247-018-0040-9)
    """
    return _ext_constant_cu_content_in_metals()


_ext_constant_cu_content_in_metals = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Copper",
    "Cu_CONTENT_IN_METALS*",
    {"CU_CONTENT_IN_METALS_I": _subscript_dict["CU_CONTENT_IN_METALS_I"]},
    _root,
    {"CU_CONTENT_IN_METALS_I": _subscript_dict["CU_CONTENT_IN_METALS_I"]},
    "_ext_constant_cu_content_in_metals",
)


@component.add(
    name="Cu_COST_GRADE_CONSTANTS",
    units="M$",
    subscripts=["ORE_GRADES_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_cu_cost_grade_constants"},
)
def cu_cost_grade_constants():
    """
    A lower ore grade implies that more rock must be moved to mine the copper. The implication is that a higher copper price is necessary to keep the copper production up when the ore grade declines. Source: Sverdrup, H. U., & Olafsdottir, A. H. (2019). On the long-term sustainability of copper, zinc and lead supply, using a system dynamics model. Resources, Conservation & Recycling: X, 4(100007). https://doi.org/https://doi.org/10.1016/j.rcrx.2019.100007 CU_COST_GRADE_CONSTANTS[RICH_GRADE]= 1000 CU_COST_GRADE_CONSTANTS[HIGH_GRADE]= 3400 CU_COST_GRADE_CONSTANTS[LOW_GRADE]=5600 CU_COST_GRADE_CONSTANTS[ULTRALOW_GRADE]=9000 CU_COST_GRADE_CONSTANTS[TRACE]=14500 CU_COST_GRADE_CONSTANTS[OCEANS]=2500
    """
    return _ext_constant_cu_cost_grade_constants()


_ext_constant_cu_cost_grade_constants = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Copper",
    "Cu_COST_GRADE_CONSTANTS*",
    {"ORE_GRADES_I": _subscript_dict["ORE_GRADES_I"]},
    _root,
    {"ORE_GRADES_I": _subscript_dict["ORE_GRADES_I"]},
    "_ext_constant_cu_cost_grade_constants",
)


@component.add(
    name="Cu_ENERGY_RECYCLING",
    units="MJ/kg",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_cu_energy_recycling"},
)
def cu_energy_recycling():
    """
    Table 2 from Rankin (2012) estimates that embodied energy for recycling Cu as a % that of primary production is 15 GJ/tonne = 1500MJ/tonne = 1,5MJ/kg. Rankin, J. (2012). Energy Use in Metal Production. High Temperature Processing Symposium, Table 1, 7â€“9. https://publications.csiro.au/rpr/download?pid=csiro:EP12183&dsid=DS3 1500MJ/tonne*tonne/kg=1500MJ/kg*1/1000= 1,5MJ/Kg (old 15)
    """
    return _ext_constant_cu_energy_recycling()


_ext_constant_cu_energy_recycling = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Copper",
    "Cu_ENERGY_RECYCLING*",
    {},
    _root,
    {},
    "_ext_constant_cu_energy_recycling",
)


@component.add(
    name="Cu_ENERGY_SECONDARY",
    units="MJ/kg",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_cu_energy_secondary"},
)
def cu_energy_secondary():
    """
    Table 2 from Rankin (2012) estimates that embodied energy from secondary is on average 21 GJ/tonne = 2100MJ/tonne = 2,1MJ/kg. Rankin, J. (2012). Energy Use in Metal Production. High Temperature Processing Symposium, Table 1, 7â€“9. https://publications.csiro.au/rpr/download?pid=csiro:EP12183&dsid=DS3 2100MJ/tonne*tonne/kg=2100MJ/kg*1/1000= 2,1MJ/Kg ------ Gutowski, T.G., Sahni, S., Allwood, M., Ashby, M.F., Worrell, E., 2016. The energy required to produce materials: constraints on energy-intensity improvements, parameters of demand. Philosophical Transactions of the Royal Society A 371: 20120003. http://dx.doi.org/10.1098/rsta.2012.0003
    """
    return _ext_constant_cu_energy_secondary()


_ext_constant_cu_energy_secondary = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Copper",
    "Cu_ENERGY_SECONDARY*",
    {},
    _root,
    {},
    "_ext_constant_cu_energy_secondary",
)


@component.add(
    name="Cu_Mo_MINES_WITH_Cu",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_cu_mo_mines_with_cu"},
)
def cu_mo_mines_with_cu():
    """
    Fraction of Mo mining being matched by copper content. See Molybdenum paper Sverdrup, H, Olafsdottir, A.H., Ragnarsdottir, K.V., 2019., Assessing global copper, zinc and lead extraction rates, supply, price and resources using the WORLD6 integrated assessment model. Resources, Conservation and Recycling 1-26. X4 100007. https://doi.org/10.1016/j.rcrx.2019.100007. Open access publication. Sverdrup, H., Olofsdottir, A.H., Ragnarsdottir, K.V., Koca, D., 2018. A system dynamics assessment of the supply of molybdenum and rhenium used for superalloys and specialty steels, using the WORLD6 model. Biophysical Economics and Resource Quality 4: 1-52 (DOI: 10.1007/s41247-018-0040-9)
    """
    return _ext_constant_cu_mo_mines_with_cu()


_ext_constant_cu_mo_mines_with_cu = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Copper",
    "Cu_Mo_MINES_WITH_Cu*",
    {},
    _root,
    {},
    "_ext_constant_cu_mo_mines_with_cu",
)


@component.add(
    name="Cu_PROFIT_DELAY",
    units="1/Years",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_cu_profit_delay"},
)
def cu_profit_delay():
    """
    Used to prevent circular connection. Profit moves fast in the system.
    """
    return _ext_constant_cu_profit_delay()


_ext_constant_cu_profit_delay = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Copper",
    "Cu_PROFIT_DELAY*",
    {},
    _root,
    {},
    "_ext_constant_cu_profit_delay",
)


@component.add(
    name="Cu_PROFIT_PUSH_MINING_POLYNOMAL_FIT",
    units="DMNL",
    subscripts=["POLYNOMAL_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_cu_profit_push_mining_polynomal_fit"},
)
def cu_profit_push_mining_polynomal_fit():
    """
    g (Profit), or Cu profit push mining, is a feed-back from profit of the mining operation. Sverdrup, H. U., & Olafsdottir, A. H. (2019). On the long-term sustainability of copper, zinc and lead supply, using a system dynamics model. Resources, Conservation & Recycling: X, 4(100007). https://doi.org/https://doi.org/10.1016/j.rcrx.2019.100007 This variable was a graphic variable in world7 but has now been fitted with the polynomal: y = 2E-32x^6 + 5E-27x^5 - 2E-21x^4 - 4E-16x^3 + 4E-11x^2 + 1E-05^x + 0,3732 This vektor containes the constants for the fit
    """
    return _ext_constant_cu_profit_push_mining_polynomal_fit()


_ext_constant_cu_profit_push_mining_polynomal_fit = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Copper",
    "Cu_PROFIT_PUSH_MINING_POLYNOMAL_FIT*",
    {"POLYNOMAL_I": _subscript_dict["POLYNOMAL_I"]},
    _root,
    {"POLYNOMAL_I": _subscript_dict["POLYNOMAL_I"]},
    "_ext_constant_cu_profit_push_mining_polynomal_fit",
)


@component.add(
    name="Cu_PROSPECTING",
    units="1/Years",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_cu_prospecting"},
)
def cu_prospecting():
    """
    Exploration finds more resources, allowing for more mining. The prospecting coefficient depend on the amount of effort spent and the technical method used for prospecting Sverdrup, H. U., & Olafsdottir, A. H. (2019). On the long-term sustainability of copper, zinc and lead supply, using a system dynamics model. Resources, Conservation & Recycling: X, 4(100007). https://doi.org/https://doi.org/10.1016/j.rcrx.2019.100007
    """
    return _ext_constant_cu_prospecting()


_ext_constant_cu_prospecting = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Copper",
    "Cu_PROSPECTING*",
    {},
    _root,
    {},
    "_ext_constant_cu_prospecting",
)


@component.add(
    name="Cu_PROSPECTING_RICH",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_cu_prospecting_rich"},
)
def cu_prospecting_rich():
    """
    Rich ore is basically pure copper and is easier to find and extract at nearly no cost. A marginal part of the copper resource.
    """
    return _ext_constant_cu_prospecting_rich()


_ext_constant_cu_prospecting_rich = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Copper",
    "Cu_PROSPECTING_RICH",
    {},
    _root,
    {},
    "_ext_constant_cu_prospecting_rich",
)


@component.add(
    name="Cu_PUSH_OCEAN",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_cu_push_ocean"},
)
def cu_push_ocean():
    """
    0,1% ???
    """
    return _ext_constant_cu_push_ocean()


_ext_constant_cu_push_ocean = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Copper",
    "Cu_PUSH_OCEAN*",
    {},
    _root,
    {},
    "_ext_constant_cu_push_ocean",
)


@component.add(
    name="Cu_SCRAPPING_LOSSES",
    units="1/Years",
    comp_type="Constant",
    comp_subtype="Normal",
)
def cu_scrapping_losses():
    """
    EOL scrap not accounted for and lost, abondand copper. Rate estimate based on Source: Loibl, A., & Tercero Espinoza, L. A. (2021). Current challenges in copper recycling: aligning insights from material flow analysis with technological research developments and industry issues in Europe and North America. Resources, Conservation and Recycling, 169(January), 105462. https://doi.org/10.1016/j.resconrec.2021.105462 GET DIRECT CONSTANTS('model_parameters/materials/materials.xlsx', 'Copper', 'Cu_SCRAPPING_LOSSES_CONSTANT*')
    """
    return 0.56


@component.add(
    name="Cu_SCRAPPING_RATE",
    units="1/Years",
    comp_type="Constant",
    comp_subtype="Normal",
)
def cu_scrapping_rate():
    """
    The WORLD 7 name: Cu Scrapping rate Annual fraction of copper in stocks-in-use that is scrapped/recycled. Estimated by looking up the modelled size of the stock and the scrapping flow reported in 2018 by the mining industry. Source: Loibl, A., & Tercero Espinoza, L. A. (2021). Current challenges in copper recycling: aligning insights from material flow analysis with technological research developments and industry issues in Europe and North America. Resources, Conservation and Recycling, 169(January), 105462. https://doi.org/10.1016/j.resconrec.2021.105462 GET DIRECT CONSTANTS('scenario_parameters/scenario_parameters.xlsx', 'materials', 'Cu_SCRAPPING_RATE*')
    """
    return 0.02866


@component.add(
    name="Cu_SOCIETY_LOSS_RATE",
    units="1/Years",
    comp_type="Constant",
    comp_subtype="Normal",
)
def cu_society_loss_rate():
    """
    old world7 name: Cu Society loss rate Amount copper diffusively lost from wear and corrosion on things that are used in society. Ends up as dust, chemical wash-off or landfill waste. GET DIRECT CONSTANTS('model_parameters/materials/materials.xlsx', 'Copper', 'Cu_SOCIETY_LOSS_RATE*') Assumption made by authors Sverdrup and Olafsdottir. Source: Sverdrup, H. U., & Olafsdottir, A. H. (2019). On the long-term sustainability of copper, zinc and lead supply, using a system dynamics model. Resources, Conservation & Recycling: X, 4(100007). https://doi.org/https://doi.org/10.1016/j.rcrx.2019.100007
    """
    return 0


@component.add(
    name="Cu_YIELDS",
    units="DMNL",
    subscripts=["ORE_GRADES_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_cu_yields"},
)
def cu_yields():
    """
    Yield: 1. When ore is extracted, the conversion of copper in stone to copper metal is not complete. Yield is the fraction of the content that ends up as metal. So when you dig up ore with 100 ton of copper, you get 96 ton copper as metal and 4 ton still in the slag with all the molten rock when the yield is 0.96. Yield is well established industrial term. h(Yield) or YIELDS is a rate adjustment factor to account for differences in extraction yield when the ore grade decreases. YIELDS[RICH_GRADE] =0,99 YIELDS[HIGH_GRADE]= 0,97 YIELDS[LOW_GRADE]= 0,94 YIELDS[ULTRALOW_GRADE] = 0,9 YIELDS[TRACE] = 0,75 YIELDS[OCEANS] =0,7 Sverdrup, H. U., & Olafsdottir, A. H. (2019). On the long-term sustainability of copper, zinc and lead supply, using a system dynamics model. Resources, Conservation & Recycling: X, 4(100007). https://doi.org/https://doi.org/10.1016/j.rcrx.2019.100007
    """
    return _ext_constant_cu_yields()


_ext_constant_cu_yields = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Copper",
    "Cu_YIELDS*",
    {"ORE_GRADES_I": _subscript_dict["ORE_GRADES_I"]},
    _root,
    {"ORE_GRADES_I": _subscript_dict["ORE_GRADES_I"]},
    "_ext_constant_cu_yields",
)


@component.add(
    name="current_EOL_RR_minerals",
    units="DMNL",
    subscripts=["MATERIALS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_current_eol_rr_minerals"},
)
def current_eol_rr_minerals():
    """
    Current End-Of-Life recycling rates from UNEP (2011)
    """
    return _ext_constant_current_eol_rr_minerals()


_ext_constant_current_eol_rr_minerals = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "World",
    "current_EOL_rr_minerals*",
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    _root,
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    "_ext_constant_current_eol_rr_minerals",
)


@component.add(
    name="CURRENT_RC_RR_MINERALS",
    units="DMNL",
    subscripts=["MATERIALS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_current_rc_rr_minerals"},
)
def current_rc_rr_minerals():
    """
    Current recycling content ratio (RC) presented by UNEP(2011)
    """
    return _ext_constant_current_rc_rr_minerals()


_ext_constant_current_rc_rr_minerals = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "World",
    "current_RC_rr_minerals*",
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    _root,
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    "_ext_constant_current_rc_rr_minerals",
)


@component.add(
    name="DISTILLED_WATER_INTENSITY_CSP_OM",
    units="kg/MW",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_distilled_water_intensity_csp_om"},
)
def distilled_water_intensity_csp_om():
    """
    Distilled water intensity for operation and maintenance of solar CSP.
    """
    return _ext_constant_distilled_water_intensity_csp_om()


_ext_constant_distilled_water_intensity_csp_om = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "World",
    "distilled_water_intensity_CSP_OM",
    {},
    _root,
    {},
    "_ext_constant_distilled_water_intensity_csp_om",
)


@component.add(
    name="DISTILLED_WATER_INTENSITY_PV_OM",
    units="kg/MW",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_distilled_water_intensity_pv_om"},
)
def distilled_water_intensity_pv_om():
    """
    Distilled water intensity for operation and maintenance of solar PV.
    """
    return _ext_constant_distilled_water_intensity_pv_om()


_ext_constant_distilled_water_intensity_pv_om = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "World",
    "distilled_water_intensity_PV_OM",
    {},
    _root,
    {},
    "_ext_constant_distilled_water_intensity_pv_om",
)


@component.add(
    name="EABE",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_eabe"},
)
def eabe():
    """
    Coefficient of energy losses of the battery in its own cooling or systems to ensure the proper functioning of the battery.
    """
    return _ext_constant_eabe()


_ext_constant_eabe = ExtConstant(
    "model_parameters/energy/energy-transport.xlsx",
    "electrified_transport",
    "EAB_E",
    {},
    _root,
    {},
    "_ext_constant_eabe",
)


@component.add(
    name="EMBODIED_PE_INTENSITY_CLEAN_WATER",
    units="MJ/kg",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_embodied_pe_intensity_clean_water"},
)
def embodied_pe_intensity_clean_water():
    """
    Embodied primary energy intensity for clean water consumption in RES plants for generation of electricity.
    """
    return _ext_constant_embodied_pe_intensity_clean_water()


_ext_constant_embodied_pe_intensity_clean_water = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "World",
    "Embodied_PE_intensity_clean_water",
    {},
    _root,
    {},
    "_ext_constant_embodied_pe_intensity_clean_water",
)


@component.add(
    name="EMBODIED_PE_INTENSITY_DISTILLED_WATER",
    units="MJ/kg",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_embodied_pe_intensity_distilled_water"},
)
def embodied_pe_intensity_distilled_water():
    """
    Embodied primary energy intensity for distilled water consumption in RES plants for generation of electricity.
    """
    return _ext_constant_embodied_pe_intensity_distilled_water()


_ext_constant_embodied_pe_intensity_distilled_water = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "World",
    "Embodied_PE_intensity_distilled_water",
    {},
    _root,
    {},
    "_ext_constant_embodied_pe_intensity_distilled_water",
)


@component.add(
    name="Embodied_PE_intensity_recycled_materials",
    units="MJ/kg",
    subscripts=["MATERIALS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_embodied_pe_intensity_recycled_materials"
    },
)
def embodied_pe_intensity_recycled_materials():
    return _ext_constant_embodied_pe_intensity_recycled_materials()


_ext_constant_embodied_pe_intensity_recycled_materials = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "World",
    "Embodied_PE_intensity_recycled_materials*",
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    _root,
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    "_ext_constant_embodied_pe_intensity_recycled_materials",
)


@component.add(
    name="Embodied_PE_intensity_virgin_materials",
    units="MJ/kg",
    subscripts=["MATERIALS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_embodied_pe_intensity_virgin_materials"},
)
def embodied_pe_intensity_virgin_materials():
    return _ext_constant_embodied_pe_intensity_virgin_materials()


_ext_constant_embodied_pe_intensity_virgin_materials = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "World",
    "Embodied_PE_intensity_virgin_materials*",
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    _root,
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    "_ext_constant_embodied_pe_intensity_virgin_materials",
)


@component.add(
    name="EV_CHARGE_LOSSES_SHARE",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_ev_charge_losses_share"},
)
def ev_charge_losses_share():
    """
    Share of energy lost in the charge EV vehicle battery process (including losses in the charger and the battery). Taken from "elCar: Guidelines for the LCA of electric vehicles".
    """
    return _ext_constant_ev_charge_losses_share()


_ext_constant_ev_charge_losses_share = ExtConstant(
    "model_parameters/energy/energy-transport.xlsx",
    "electrified_transport",
    "EV_CHARGE_LOSSES_SHARE",
    {},
    _root,
    {},
    "_ext_constant_ev_charge_losses_share",
)


@component.add(
    name="EV_DISCHARGE_LOSSES_SHARE",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_ev_discharge_losses_share"},
)
def ev_discharge_losses_share():
    """
    Share of energy lost in the discharge EV vehicle battery process. The same share than for charging is assumed.
    """
    return _ext_constant_ev_discharge_losses_share()


_ext_constant_ev_discharge_losses_share = ExtConstant(
    "model_parameters/energy/energy-transport.xlsx",
    "electrified_transport",
    "EV_DISCHARGE_LOSSES_SHARE",
    {},
    _root,
    {},
    "_ext_constant_ev_discharge_losses_share",
)


@component.add(
    name="global_mineral_reserves",
    units="Mt",
    subscripts=["MATERIALS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_global_mineral_reserves"},
)
def global_mineral_reserves():
    return _ext_constant_global_mineral_reserves()


_ext_constant_global_mineral_reserves = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "World",
    "current_reserves*",
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    _root,
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    "_ext_constant_global_mineral_reserves",
)


@component.add(
    name="global_mineral_resources",
    units="Mt",
    subscripts=["MATERIALS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_global_mineral_resources"},
)
def global_mineral_resources():
    return _ext_constant_global_mineral_resources()


_ext_constant_global_mineral_resources = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "World",
    "current_resources*",
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    _root,
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    "_ext_constant_global_mineral_resources",
)


@component.add(
    name="HIGH_GRADE_FACTOR",
    units="1/Years",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_high_grade_factor"},
)
def high_grade_factor():
    """
    This factor compensates for the fact that the high grade and the rich grade are much easier to mine - the others need more work. These numbers give the best fit to the historical data and therefore they are assumptions based parametersation of the ore grade curve. This consideration the difference between rich and high grade ores vs. lower grade ores. This particular parameter is for the high grade.
    """
    return _ext_constant_high_grade_factor()


_ext_constant_high_grade_factor = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Copper",
    "HIGH_GRADE_FACTOR*",
    {},
    _root,
    {},
    "_ext_constant_high_grade_factor",
)


@component.add(
    name="Historic_improvement_recycling_rates_minerals",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_historic_improvement_recycling_rates_minerals"
    },
)
def historic_improvement_recycling_rates_minerals():
    """
    Due to the large uncertainty and slow evolution of these data, historical recycling rates minerals correspond with the current estimates (UNEP, 2011).
    """
    return _ext_constant_historic_improvement_recycling_rates_minerals()


_ext_constant_historic_improvement_recycling_rates_minerals = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "World",
    "historic_improvement_recycling_rates_minerals",
    {},
    _root,
    {},
    "_ext_constant_historic_improvement_recycling_rates_minerals",
)


@component.add(
    name="Historical_consumption_materials_RoE",
    units="tonnes",
    subscripts=["MATERIALS_I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_historical_consumption_materials_roe",
        "__lookup__": "_ext_lookup_historical_consumption_materials_roe",
    },
)
def historical_consumption_materials_roe(x, final_subs=None):
    return _ext_lookup_historical_consumption_materials_roe(x, final_subs)


_ext_lookup_historical_consumption_materials_roe = ExtLookup(
    "model_parameters/materials/materials.xlsx",
    "World",
    "time_hist_minerals_index",
    "historical_consumption_minerals_rest",
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    _root,
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    "_ext_lookup_historical_consumption_materials_roe",
)


@component.add(
    name="INITIAL_Cu_CUMULATIVE_MINING",
    units="Mt",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_cu_cumulative_mining"},
)
def initial_cu_cumulative_mining():
    """
    The initial values for the cu known stocks are based on simulation outputs from the world7 for the year 2005. The world7 outputs are based on initial values from 1900. Source: Sverdrup, H. U., & Olafsdottir, A. H. (2019). On the long-term sustainability of copper, zinc and lead supply, using a system dynamics model. Resources, Conservation & Recycling: X, 4(100007). https://doi.org/https://doi.org/10.1016/j.rcrx.2019.100007
    """
    return _ext_constant_initial_cu_cumulative_mining()


_ext_constant_initial_cu_cumulative_mining = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Copper",
    "INITIAL_Cu_CUMULATIVE_MINING*",
    {},
    _root,
    {},
    "_ext_constant_initial_cu_cumulative_mining",
)


@component.add(
    name="INITIAL_Cu_CUMULATIVE_MINING_DATA",
    units="Mt",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_cu_cumulative_mining_data"},
)
def initial_cu_cumulative_mining_data():
    """
    Initial cumulative amount of copper that has already been mined. Source:
    """
    return _ext_constant_initial_cu_cumulative_mining_data()


_ext_constant_initial_cu_cumulative_mining_data = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Copper",
    "INITIAL_Cu_CUMULATIVE_MINING_DATA*",
    {},
    _root,
    {},
    "_ext_constant_initial_cu_cumulative_mining_data",
)


@component.add(
    name="INITIAL_Cu_DEMAND_DELAY",
    units="Mt",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_cu_demand_delay"},
)
def initial_cu_demand_delay():
    """
    The initial values for the Cu known stocks are based on simulation outputs from the world7 for the year 2005. The world7 outputs are based on initial values from 1900. Source: Sverdrup, H. U., & Olafsdottir, A. H. (2019). On the long-term sustainability of copper, zinc and lead supply, using a system dynamics model. Resources, Conservation & Recycling: X, 4(100007). https://doi.org/https://doi.org/10.1016/j.rcrx.2019.100007
    """
    return _ext_constant_initial_cu_demand_delay()


_ext_constant_initial_cu_demand_delay = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Copper",
    "INITIAL_Cu_DEMAND_DELAY*",
    {},
    _root,
    {},
    "_ext_constant_initial_cu_demand_delay",
)


@component.add(
    name="INITIAL_Cu_HIDDEN_RESOURCES",
    units="Mt",
    subscripts=["ORE_GRADES_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_cu_hidden_resources"},
)
def initial_cu_hidden_resources():
    """
    The initial values for the cu hidden stocks are based on simulation outputs from the world7 for the year 2005. The world7 outputs are based on numbers for in 1900 that were stratified with respect to ore metal content and relative extraction cost based on yield of extraction and energy requirements. The WILLIAM, 2005 initial values are therefore the following for the hidden resources: Rich grade is 0, high grade is 157, low grade is 538, ultralow grade is 1122, trace is 550 and oceans is 300. Source: Sverdrup, H. U., & Olafsdottir, A. H. (2019). On the long-term sustainability of copper, zinc and lead supply, using a system dynamics model. Resources, Conservation & Recycling: X, 4(100007). https://doi.org/https://doi.org/10.1016/j.rcrx.2019.100007 Olafsdottir, A. H., Sverdrup, H. U., & Ragnarsdottir, K. V. (2017). On the metal contents of ocean floor nodules, crusts and massive sulphides and a preliminary assessment of the extractable amounts. In C. Ludwig & S. Valdivia (Eds.), World resources Forum 2017 (pp. 150â€“156). Villigen PSI and World Resources Forum. https://www.wrforum.org/profile/ss1-14/#
    """
    return _ext_constant_initial_cu_hidden_resources()


_ext_constant_initial_cu_hidden_resources = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Copper",
    "INITIAL_Cu_HIDDEN_RESOURCES*",
    {"ORE_GRADES_I": _subscript_dict["ORE_GRADES_I"]},
    _root,
    {"ORE_GRADES_I": _subscript_dict["ORE_GRADES_I"]},
    "_ext_constant_initial_cu_hidden_resources",
)


@component.add(
    name="INITIAL_Cu_IN_USE_IN_SOCIETY",
    units="Mt",
    comp_type="Constant",
    comp_subtype="Normal",
)
def initial_cu_in_use_in_society():
    """
    The initial values for the cu known stocks are based on simulation outputs from the world7 for the year 2005. The world7 outputs are based on initial values from 1900. GET DIRECT CONSTANTS('model_parameters/materials/materials.xlsx', 'Copper', 'INITIAL_Cu_IN_USE_IN_SOCIETY*') Source: Sverdrup, H. U., & Olafsdottir, A. H. (2019). On the long-term sustainability of copper, zinc and lead supply, using a system dynamics model. Resources, Conservation & Recycling: X, 4(100007). https://doi.org/https://doi.org/10.1016/j.rcrx.2019.100007
    """
    return 355


@component.add(
    name="INITIAL_Cu_KNOWN_RESERVES",
    units="Mt",
    subscripts=["ORE_GRADES_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_cu_known_reserves"},
)
def initial_cu_known_reserves():
    """
    The initial values for the cu known stocks are based on simulation outputs from the world7 for the year 2005. The world7 outputs are based on initial values from 1900 that were stratified with respect to ore metal content and relative extraction cost based on yield of extraction and energy requirements. The initial values for the cu known stocks are based on simulation outputs from the world7 for the year 2005. Rich grade is 2,6, high grade is 113, low grade is 826, ultralow grade is 174, trace is 15 and oceans is 0. Source: Sverdrup, H. U., & Olafsdottir, A. H. (2019). On the long-term sustainability of copper, zinc and lead supply, using a system dynamics model. Resources, Conservation & Recycling: X, 4(100007). https://doi.org/https://doi.org/10.1016/j.rcrx.2019.100007 Olafsdottir, A. H., Sverdrup, H. U., & Ragnarsdottir, K. V. (2017). On the metal contents of ocean floor nodules, crusts and massive sulphides and a preliminary assessment of the extractable amounts. In C. Ludwig & S. Valdivia (Eds.), World resources Forum 2017 (pp. 150â€“156). Villigen PSI and World Resources Forum. https://www.wrforum.org/profile/ss1-14/#
    """
    return _ext_constant_initial_cu_known_reserves()


_ext_constant_initial_cu_known_reserves = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Copper",
    "INITIAL_Cu_KNOWN_RESERVES*",
    {"ORE_GRADES_I": _subscript_dict["ORE_GRADES_I"]},
    _root,
    {"ORE_GRADES_I": _subscript_dict["ORE_GRADES_I"]},
    "_ext_constant_initial_cu_known_reserves",
)


@component.add(
    name="INITIAL_Cu_MARKET",
    units="Mt",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_cu_market"},
)
def initial_cu_market():
    """
    The initial values for the cu known stocks are based on simulation outputs from the world7 for the year 2005. The world7 outputs are based on initial values from 1900. Source: Sverdrup, H. U., & Olafsdottir, A. H. (2019). On the long-term sustainability of copper, zinc and lead supply, using a system dynamics model. Resources, Conservation & Recycling: X, 4(100007). https://doi.org/https://doi.org/10.1016/j.rcrx.2019.100007
    """
    return _ext_constant_initial_cu_market()


_ext_constant_initial_cu_market = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Copper",
    "INITIAL_Cu_MARKET*",
    {},
    _root,
    {},
    "_ext_constant_initial_cu_market",
)


@component.add(
    name="INITIAL_Cu_OCEAN_PROFIT_DELAY",
    units="M$",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_cu_ocean_profit_delay"},
)
def initial_cu_ocean_profit_delay():
    """
    The initial values for the cu known stocks are based on simulation outputs from the world7 for the year 2005. The world7 outputs are based on initial values from 1900. Source: Sverdrup, H. U., & Olafsdottir, A. H. (2019). On the long-term sustainability of copper, zinc and lead supply, using a system dynamics model. Resources, Conservation & Recycling: X, 4(100007). https://doi.org/https://doi.org/10.1016/j.rcrx.2019.100007
    """
    return _ext_constant_initial_cu_ocean_profit_delay()


_ext_constant_initial_cu_ocean_profit_delay = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Copper",
    "INITIAL_Cu_OCEAN_PROFIT_DELAY*",
    {},
    _root,
    {},
    "_ext_constant_initial_cu_ocean_profit_delay",
)


@component.add(
    name="INITIAL_Cu_PROFIT_DELAY",
    units="M$",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_cu_profit_delay"},
)
def initial_cu_profit_delay():
    """
    The initial values for the INITIAL Cu PROFIT DELAY are based on simulation outputs from the world7 for the year 2005. The world7 outputs are based on initial values for 1900. Source: Sverdrup, H. U., & Olafsdottir, A. H. (2019). On the long-term sustainability of copper, zinc and lead supply, using a system dynamics model. Resources, Conservation & Recycling: X, 4(100007). https://doi.org/https://doi.org/10.1016/j.rcrx.2019.100007
    """
    return _ext_constant_initial_cu_profit_delay()


_ext_constant_initial_cu_profit_delay = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Copper",
    "INITIAL_Cu_PROFIT_DELAY*",
    {},
    _root,
    {},
    "_ext_constant_initial_cu_profit_delay",
)


@component.add(
    name="INITIAL_Cu_SCRAPPED", units="Mt", comp_type="Constant", comp_subtype="Normal"
)
def initial_cu_scrapped():
    """
    The initial values for the cu known stocks are based on simulation outputs from the world7 for the year 2005. The world7 outputs are based on initial values from 1900. Source: Sverdrup, H. U., & Olafsdottir, A. H. (2019). On the long-term sustainability of copper, zinc and lead supply, using a system dynamics model. Resources, Conservation & Recycling: X, 4(100007). https://doi.org/https://doi.org/10.1016/j.rcrx.2019.100007 GET DIRECT CONSTANTS('model_parameters/materials/materials.xlsx', 'Copper', 'INITIAL_Cu_SCRAPPED*')
    """
    return 12


@component.add(
    name="INITIAL_LENGTH_ELECTRIC_GRID_TO_CONNECT_EV_CHARGERS",
    units="km",
    subscripts=["EV_CHARGERS_I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def initial_length_electric_grid_to_connect_ev_chargers():
    """
    Initial km of electric grid to connect the EV chargers.
    """
    return xr.DataArray(
        0, {"EV_CHARGERS_I": _subscript_dict["EV_CHARGERS_I"]}, ["EV_CHARGERS_I"]
    )


@component.add(
    name="INITIAL_MATERIAL_INTENSITY_PV_CELLS",
    units="kg/MW",
    subscripts=["MATERIALS_I", "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_material_intensity_pv_cells"},
)
def initial_material_intensity_pv_cells():
    """
    Materials requirements per MW of new cell of solar C-SI mono PV. Take from Al (Gervais et al., 2021), Ag (Gervais et al., 2021), Cu (Gervais et al., 2021), Ni (Elshkaki and Graedel, 2013), Si (PSE, n.d.), Sn (Gervais et al., 2021), Pb (Gervais et al., 2021), Mg (European Commission. Joint Research Centre. Institute for Energy and Transport. et al., 2011; Moss et al., 2013)
    """
    return _ext_constant_initial_material_intensity_pv_cells()


_ext_constant_initial_material_intensity_pv_cells = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "PV",
    "MATERIAL_INTENSITY_PV_CELLS",
    {
        "MATERIALS_I": _subscript_dict["MATERIALS_I"],
        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": _subscript_dict[
            "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"
        ],
    },
    _root,
    {
        "MATERIALS_I": _subscript_dict["MATERIALS_I"],
        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": _subscript_dict[
            "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"
        ],
    },
    "_ext_constant_initial_material_intensity_pv_cells",
)


@component.add(
    name="initial_mineral_consumption_RoE",
    units="tonnes",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"initial_mineral_consumption_roe_w": 1, "number_of_regions": 1},
)
def initial_mineral_consumption_roe():
    """
    initial_mineral_consumption_RoE
    """
    return (initial_mineral_consumption_roe_w() / number_of_regions()).expand_dims(
        {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, 0
    )


@component.add(
    name="initial_mineral_consumption_RoE_W",
    units="tonnes",
    subscripts=["MATERIALS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_mineral_consumption_roe_w"},
)
def initial_mineral_consumption_roe_w():
    """
    initial_mineral_consumption_RoE
    """
    return _ext_constant_initial_mineral_consumption_roe_w()


_ext_constant_initial_mineral_consumption_roe_w = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "World",
    "initial_mineral_consumption_RoE*",
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    _root,
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    "_ext_constant_initial_mineral_consumption_roe_w",
)


@component.add(
    name="INITIAL_NUMBER_EV_CHARGERS_BY_TYPE",
    units="chargers",
    subscripts=["EV_CHARGERS_I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def initial_number_ev_chargers_by_type():
    """
    Initial number of EV chargers by type
    """
    return xr.DataArray(
        0, {"EV_CHARGERS_I": _subscript_dict["EV_CHARGERS_I"]}, ["EV_CHARGERS_I"]
    )


@component.add(
    name="INITIAL_RAILWAY_TRACKS_LENGTH",
    units="km",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_railway_tracks_length"},
)
def initial_railway_tracks_length():
    """
    initial length of railway tracks
    """
    return _ext_constant_initial_railway_tracks_length()


_ext_constant_initial_railway_tracks_length = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "World",
    "INITIAL_RAILWAY_TRACKS_LENGTH",
    {},
    _root,
    {},
    "_ext_constant_initial_railway_tracks_length",
)


@component.add(
    name="INITIAL_SC_SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_sc_sp"},
)
def initial_sc_sp():
    """
    percentage base of vehicles using Smart charging
    """
    return _ext_constant_initial_sc_sp()


_ext_constant_initial_sc_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "INITIAL_SC_SP",
    {},
    _root,
    {},
    "_ext_constant_initial_sc_sp",
)


@component.add(
    name="INITIAL_SHARE_WEIGHTS_EVS_BATTERIES",
    units="DMNL",
    subscripts=["EV_BATTERIES_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_share_weights_evs_batteries"},
)
def initial_share_weights_evs_batteries():
    """
    initial share weights, from the logit model functions
    """
    return _ext_constant_initial_share_weights_evs_batteries()


_ext_constant_initial_share_weights_evs_batteries = ExtConstant(
    "model_parameters/energy/energy.xlsm",
    "allocation_new_capacity_subtech",
    "INITIAL_SHARE_WEIGHTS_EVS_BATTERIES*",
    {"EV_BATTERIES_I": _subscript_dict["EV_BATTERIES_I"]},
    _root,
    {"EV_BATTERIES_I": _subscript_dict["EV_BATTERIES_I"]},
    "_ext_constant_initial_share_weights_evs_batteries",
)


@component.add(
    name="INITIAL_STOCK_MINERAL_REST_OF_THE_ECONOMY",
    units="Mt",
    subscripts=["MATERIALS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_initial_stock_mineral_rest_of_the_economy"
    },
)
def initial_stock_mineral_rest_of_the_economy():
    """
    initial stock mineral of the Rest of the economy
    """
    return _ext_constant_initial_stock_mineral_rest_of_the_economy()


_ext_constant_initial_stock_mineral_rest_of_the_economy = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "World",
    "Initial_stocks*",
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    _root,
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    "_ext_constant_initial_stock_mineral_rest_of_the_economy",
)


@component.add(
    name="INITIAL_V2G_SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_v2g_sp"},
)
def initial_v2g_sp():
    """
    percentage base of vehicles using V2G
    """
    return _ext_constant_initial_v2g_sp()


_ext_constant_initial_v2g_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "START_VALUE_V2G_SP",
    {},
    _root,
    {},
    "_ext_constant_initial_v2g_sp",
)


@component.add(
    name="INITIAL_YEAR_REDUCTION_MATERIAL_INTENSITY_PV_SP",
    units="DMNL/Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_initial_year_reduction_material_intensity_pv_sp"
    },
)
def initial_year_reduction_material_intensity_pv_sp():
    """
    Initial year to apply the assumption of improvement of material intensities of solar PV subtechnologies.
    """
    return _ext_constant_initial_year_reduction_material_intensity_pv_sp()


_ext_constant_initial_year_reduction_material_intensity_pv_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "materials",
    "INITIAL_YEAR_REDUCTION_MATERIAL_INTENSITY_PV_SP",
    {},
    _root,
    {},
    "_ext_constant_initial_year_reduction_material_intensity_pv_sp",
)


@component.add(
    name="INVERTER_PV_LIFETIME",
    units="Years",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_inverter_pv_lifetime"},
)
def inverter_pv_lifetime():
    """
    Lifetime of a PV inverter take from De Castro et al 2020
    """
    return _ext_constant_inverter_pv_lifetime()


_ext_constant_inverter_pv_lifetime = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "PV",
    "INVERTER_PV_LIFETIME*",
    {},
    _root,
    {},
    "_ext_constant_inverter_pv_lifetime",
)


@component.add(
    name="LENGTH_ELECTRIC_GRID_TO_CONNECT_EV_CHARGERS",
    units="m/charger",
    subscripts=["EV_CHARGERS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_length_electric_grid_to_connect_ev_chargers"
    },
)
def length_electric_grid_to_connect_ev_chargers():
    """
    Meters of electric grid corresponding to each type of charger. The length has been estimated based on experience and visualization of similar installations, but this length is subject to each specific case being very variable depending on the situation.
    """
    return _ext_constant_length_electric_grid_to_connect_ev_chargers()


_ext_constant_length_electric_grid_to_connect_ev_chargers = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "World",
    "LENGTH_ELECTRIC_GRID_TO_CONNECT_EV_CHARGERS*",
    {"EV_CHARGERS_I": _subscript_dict["EV_CHARGERS_I"]},
    _root,
    {"EV_CHARGERS_I": _subscript_dict["EV_CHARGERS_I"]},
    "_ext_constant_length_electric_grid_to_connect_ev_chargers",
)


@component.add(
    name="LENGTH_PER_MW_BUILDING_WIRING_BASELINE",
    units="m/MW",
    subscripts=["PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_length_per_mw_building_wiring_baseline"},
)
def length_per_mw_building_wiring_baseline():
    """
    Initial metres per MW of PV rooftop building installation. Estimated cable metres are stated with the help, on the one hand, of comments obtained from the literature source (Lucas et al., 2012) and, on the other hand, using assumptions based on experience (observing existing installations, although this is a value subject to much variability, so assumptions are used).
    """
    return _ext_constant_length_per_mw_building_wiring_baseline()


_ext_constant_length_per_mw_building_wiring_baseline = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "PV",
    "LENGTH_PER_MW_BUILDING_WIRING_BASELINE*",
    {
        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": _subscript_dict[
            "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"
        ]
    },
    _root,
    {
        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": _subscript_dict[
            "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"
        ]
    },
    "_ext_constant_length_per_mw_building_wiring_baseline",
)


@component.add(
    name="LENGTH_PER_MW_HOUSE_WIRING_BASELINE",
    units="m/MW",
    subscripts=["PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_length_per_mw_house_wiring_baseline"},
)
def length_per_mw_house_wiring_baseline():
    """
    initial metres per MW of PV rooftop house installation. Estimated cable metres are stated with the help, on the one hand, of comments obtained from the literature source (Lucas et al., 2012) and, on the other hand, using assumptions based on experience (observing existing installations, although this is a value subject to much variability, so assumptions are used).
    """
    return _ext_constant_length_per_mw_house_wiring_baseline()


_ext_constant_length_per_mw_house_wiring_baseline = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "PV",
    "LENGTH_PER_MW_HOUSE_WIRING_BASELINE*",
    {
        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": _subscript_dict[
            "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"
        ]
    },
    _root,
    {
        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": _subscript_dict[
            "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"
        ]
    },
    "_ext_constant_length_per_mw_house_wiring_baseline",
)


@component.add(
    name="LENGTH_PER_MW_INVERTER_TO_TRANSFORMER_BASELINE",
    units="m/MW",
    subscripts=["PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_length_per_mw_inverter_to_transformer_baseline"
    },
)
def length_per_mw_inverter_to_transformer_baseline():
    """
    initial metres per MW of ground PV installation from the inverter to the transformer. Estimated cable metres are stated with the help, on the one hand, of comments obtained from the literature source (Lucas et al., 2012) and, on the other hand, using assumptions based on experience (observing existing installations, although this is a value subject to much variability, so assumptions are used).
    """
    return _ext_constant_length_per_mw_inverter_to_transformer_baseline()


_ext_constant_length_per_mw_inverter_to_transformer_baseline = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "PV",
    "LENGTH_PER_MW_INVERTER_TO_TRANSFORMER_BASELINE*",
    {
        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": _subscript_dict[
            "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"
        ]
    },
    _root,
    {
        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": _subscript_dict[
            "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"
        ]
    },
    "_ext_constant_length_per_mw_inverter_to_transformer_baseline",
)


@component.add(
    name="LENGTH_PER_MW_PANEL_TO_INVERTER_BASELINE",
    units="m/MW",
    subscripts=["PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_length_per_mw_panel_to_inverter_baseline"
    },
)
def length_per_mw_panel_to_inverter_baseline():
    """
    initial metres per MW of PV ground installation from the panel to the inverter. Estimated cable metres are stated with the help, on the one hand, of comments obtained from the literature source (Lucas et al., 2012) and, on the other hand, using assumptions based on experience (observing existing installations, although this is a value subject to much variability, so assumptions are used).
    """
    return _ext_constant_length_per_mw_panel_to_inverter_baseline()


_ext_constant_length_per_mw_panel_to_inverter_baseline = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "PV",
    "LENGTH_PER_MW_PANEL_TO_INVERTER_BASELINE*",
    {
        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": _subscript_dict[
            "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"
        ]
    },
    _root,
    {
        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": _subscript_dict[
            "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"
        ]
    },
    "_ext_constant_length_per_mw_panel_to_inverter_baseline",
)


@component.add(
    name="LENGTH_RAILWAY_LINES_PER_LOCOMOTIVE_HISTORIC",
    units="km/locomotive",
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_length_railway_lines_per_locomotive_historic",
        "__data__": "_ext_data_length_railway_lines_per_locomotive_historic",
        "time": 1,
    },
)
def length_railway_lines_per_locomotive_historic():
    """
    Historic length of railway length per locomotive. -The estimation of the track length is modelled depending on two parameters (UIC, «Railway handbook 2013» and «UIC statistics», UIC, 2021): the ratio of total length of railway track vs length lines and the ratio of the length of railway lines vs the number of locomotives which for the sake of simplicity we maintain constant in the model in their estimated values for the base year 2015, at the values 1.5 and 3, respectively. The total track length is then estimated multiplying these parameters by the total number of trains which is an endogenous variable of the MEDEAS-W model depending on the demand of this type of transport.
    """
    return _ext_data_length_railway_lines_per_locomotive_historic(time())


_ext_data_length_railway_lines_per_locomotive_historic = ExtData(
    "model_parameters/materials/materials.xlsx",
    "World",
    "time_train",
    "LENGTH_RAILWAY_LINES_PER_LOCOMOTIVE_HISTORIC",
    "interpolate",
    {},
    _root,
    {},
    "_ext_data_length_railway_lines_per_locomotive_historic",
)


@component.add(
    name="LIFETIME_EBIKE_VEHICLE",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_lifetime_ebike_vehicle"},
)
def lifetime_ebike_vehicle():
    """
    lifetime of Ebikes
    """
    return _ext_constant_lifetime_ebike_vehicle()


_ext_constant_lifetime_ebike_vehicle = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "World",
    "LIFETIME_EBIKE_VEHICLE",
    {},
    _root,
    {},
    "_ext_constant_lifetime_ebike_vehicle",
)


@component.add(
    name="LIFETIME_ELECTRIC_GRID_TO_CONNECT_EV_CHARGERS",
    units="Years",
    subscripts=["EV_CHARGERS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_lifetime_electric_grid_to_connect_ev_chargers"
    },
)
def lifetime_electric_grid_to_connect_ev_chargers():
    """
    lifetime of electric grids to connect the EV chargers. The useful life of these infrastructures from study of “ATS energía”, 2017(Vida util de los elementos de transmisión)
    """
    return _ext_constant_lifetime_electric_grid_to_connect_ev_chargers()


_ext_constant_lifetime_electric_grid_to_connect_ev_chargers = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "World",
    "LIFETIME_ELECTRIC_GRID_TO_CONNECT_EV_CHARGERS*",
    {"EV_CHARGERS_I": _subscript_dict["EV_CHARGERS_I"]},
    _root,
    {"EV_CHARGERS_I": _subscript_dict["EV_CHARGERS_I"]},
    "_ext_constant_lifetime_electric_grid_to_connect_ev_chargers",
)


@component.add(
    name="LIFETIME_EV_CHARGERS",
    units="Years",
    subscripts=["EV_CHARGERS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_lifetime_ev_chargers"},
)
def lifetime_ev_chargers():
    """
    Lifetime of EV chargers by type. The useful life has been obtained from Lucas et al, 2012.
    """
    return _ext_constant_lifetime_ev_chargers()


_ext_constant_lifetime_ev_chargers = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "World",
    "LIFETIME_EV_CHARGERS*",
    {"EV_CHARGERS_I": _subscript_dict["EV_CHARGERS_I"]},
    _root,
    {"EV_CHARGERS_I": _subscript_dict["EV_CHARGERS_I"]},
    "_ext_constant_lifetime_ev_chargers",
)


@component.add(
    name="LIFETIME_RAILWAY_CATENARY",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_lifetime_railway_catenary"},
)
def lifetime_railway_catenary():
    """
    lifetime of railway catenary. The useful life of these infrastructures from study of “Plasser Española” (Rendimiento, precisión y fiabilidad en la construcción de catenaria, 2008).
    """
    return _ext_constant_lifetime_railway_catenary()


_ext_constant_lifetime_railway_catenary = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "World",
    "LIFETIME_RAILWAY_CATENARY",
    {},
    _root,
    {},
    "_ext_constant_lifetime_railway_catenary",
)


@component.add(
    name="LIFETIME_RAILWAY_TRACKS",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_lifetime_railway_tracks"},
)
def lifetime_railway_tracks():
    """
    lifetime of railway tracks
    """
    return _ext_constant_lifetime_railway_tracks()


_ext_constant_lifetime_railway_tracks = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "World",
    "LIFETIME_RAILWAY_TRACKS",
    {},
    _root,
    {},
    "_ext_constant_lifetime_railway_tracks",
)


@component.add(
    name="LOGIT_MODEL_COEFFICIENT_OR_EXPONENT",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_logit_model_coefficient_or_exponent"},
)
def logit_model_coefficient_or_exponent():
    """
    Depending on which logit model is chosen: - Logit model: this parameter represents the logit coefficient. - Modified logit model: this parameter represents the logit exponent. Positive values (given that we want to give preference to highest values of the choice indicator: ESOIxMAB (for storage) and EROI*MAB (for generation). Typical values: 3, 6, 9, 12. cf. https://jgcri.github.io/gcam-doc/choice.html
    """
    return _ext_constant_logit_model_coefficient_or_exponent()


_ext_constant_logit_model_coefficient_or_exponent = ExtConstant(
    "model_parameters/energy/energy.xlsm",
    "allocation_new_capacity_subtech",
    "LOGIT_MODEL_COEFFICIENT_OR_EXPONENT",
    {},
    _root,
    {},
    "_ext_constant_logit_model_coefficient_or_exponent",
)


@component.add(
    name="MACHINING_RATE_EV_BATTERIES",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_machining_rate_ev_batteries"},
)
def machining_rate_ev_batteries():
    """
    Ratio that translates the energy costs of manufacturing electric EVs batteries (15%)
    """
    return _ext_constant_machining_rate_ev_batteries()


_ext_constant_machining_rate_ev_batteries = ExtConstant(
    "model_parameters/energy/energy-transport.xlsx",
    "electrified_transport",
    "MACHINING_RATE_EV_BATTERIES",
    {},
    _root,
    {},
    "_ext_constant_machining_rate_ev_batteries",
)


@component.add(
    name="MATERIAL_AUX_INTENSITY_PV_LAND",
    units="kg/MW",
    subscripts=["MATERIALS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_material_aux_intensity_pv_land"},
)
def material_aux_intensity_pv_land():
    """
    Building materials requirements per MW of solar ground technology. Take from De Castro et al 2020.
    """
    return _ext_constant_material_aux_intensity_pv_land()


_ext_constant_material_aux_intensity_pv_land = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "PV",
    "MATERIAL_AUX_INTENSITY_PV_LAND*",
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    _root,
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    "_ext_constant_material_aux_intensity_pv_land",
)


@component.add(
    name="MATERIAL_INTENSITY_CATENARY_RAILWAY",
    units="kg/m",
    subscripts=["MATERIALS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_material_intensity_catenary_railway"},
)
def material_intensity_catenary_railway():
    """
    Materials requeriment per km of track. - It should be noted that the catenary uses copper-PTE alloys and not pure copper, but these alloys have a copper weight of more than 99.90% (Aurubis, «Cu-ETP Material datasheet», 2021.). - ADIF's (Spanish railway infrastructure manager) CA-220 catenary has been assumed as electrification due to its versatility and its capacity to be used in different situations and conditions. (ADIF, «Memoria descriptiva CA-220», ene. 2012.)
    """
    return _ext_constant_material_intensity_catenary_railway()


_ext_constant_material_intensity_catenary_railway = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "World",
    "Electrification_railway_track*",
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    _root,
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    "_ext_constant_material_intensity_catenary_railway",
)


@component.add(
    name="MATERIAL_INTENSITY_EV_GRID_TO_CHARGER_HIGH_VOLTAGE",
    units="kg/m",
    subscripts=["MATERIALS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_material_intensity_ev_grid_to_charger_high_voltage"
    },
)
def material_intensity_ev_grid_to_charger_high_voltage():
    """
    Materials requirements per EV charger grid. -Medium and high voltage grids: Data from Bumby et al(2010), and HidroCantábrico distribución electrica S.A.U(2011) have been taken as reference. A two-pipe pipe of 160 mm diameter inserted in a concrete cube with 45 cm of side and about 5 cm of thickness, taken from the instructions of the reference HidroCantábrico distribusión electrica S.A.U., (Especificacion tecnica de las canalizaciones subterraneas de baja y media tension, 2011), has been chosen as a reference pipe. The concrete weight of this last reference has been compared with the weight of concrete from Bumby et al(2010) using this relation to apply it to the other materials.
    """
    return _ext_constant_material_intensity_ev_grid_to_charger_high_voltage()


_ext_constant_material_intensity_ev_grid_to_charger_high_voltage = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "World",
    "EV_grid_high*",
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    _root,
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    "_ext_constant_material_intensity_ev_grid_to_charger_high_voltage",
)


@component.add(
    name="MATERIAL_INTENSITY_EV_GRID_TO_CHARGER_LOW_VOLTAGE",
    units="kg/m",
    subscripts=["MATERIALS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_material_intensity_ev_grid_to_charger_low_voltage"
    },
)
def material_intensity_ev_grid_to_charger_low_voltage():
    """
    Materials requirements per EV charger grid. -Low voltage grids: Data estimated with formula 16 of Annex 2 of the Spanish Low Voltage Guide. (Ministerio de ciencia y tecnología, «Guia tecnica de aplicacion- Caidas de tensión, Anexo 2»).
    """
    return _ext_constant_material_intensity_ev_grid_to_charger_low_voltage()


_ext_constant_material_intensity_ev_grid_to_charger_low_voltage = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "World",
    "EV_grid_low*",
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    _root,
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    "_ext_constant_material_intensity_ev_grid_to_charger_low_voltage",
)


@component.add(
    name="MATERIAL_INTENSITY_EV_GRID_TO_CHARGER_LOWMEDIUM_VOLTAGE",
    units="kg/m",
    subscripts=["MATERIALS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_material_intensity_ev_grid_to_charger_lowmedium_voltage"
    },
)
def material_intensity_ev_grid_to_charger_lowmedium_voltage():
    """
    Materials requirements per EV charger grid. -Low-medium voltage grids: Data estimated with formula 16 of Annex 2 of the Spanish Low Voltage Guide. (Ministerio de ciencia y tecnología, «Guia tecnica de aplicacion- Caidas de tensión, Anexo 2»).
    """
    return _ext_constant_material_intensity_ev_grid_to_charger_lowmedium_voltage()


_ext_constant_material_intensity_ev_grid_to_charger_lowmedium_voltage = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "World",
    "EV_grid_low_medium*",
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    _root,
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    "_ext_constant_material_intensity_ev_grid_to_charger_lowmedium_voltage",
)


@component.add(
    name="MATERIAL_INTENSITY_EV_GRID_TO_CHARGER_MEDIUM_VOLTAGE",
    units="kg/m",
    subscripts=["MATERIALS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_material_intensity_ev_grid_to_charger_medium_voltage"
    },
)
def material_intensity_ev_grid_to_charger_medium_voltage():
    """
    Materials requirements per EV charger grid. -Medium and high voltage grids: Data from Bumby et al(2010), and HidroCantábrico distribución electrica S.A.U(2011) have been taken as reference. A two-pipe pipe of 160 mm diameter inserted in a concrete cube with 45 cm of side and about 5 cm of thickness, taken from the instructions of the reference HidroCantábrico distribusión electrica S.A.U., (Especificacion tecnica de las canalizaciones subterraneas de baja y media tension, 2011), has been chosen as a reference pipe. The concrete weight of this last reference has been compared with the weight of concrete from Bumby et al(2010) using this relation to apply it to the other materials.
    """
    return _ext_constant_material_intensity_ev_grid_to_charger_medium_voltage()


_ext_constant_material_intensity_ev_grid_to_charger_medium_voltage = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "World",
    "EV_grid_medium*",
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    _root,
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    "_ext_constant_material_intensity_ev_grid_to_charger_medium_voltage",
)


@component.add(
    name="MATERIAL_INTENSITY_EV_HOME_CHARGER",
    units="kg/charger",
    subscripts=["MATERIALS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_material_intensity_ev_home_charger"},
)
def material_intensity_ev_home_charger():
    """
    Materials requirements per EV charger. Hypotheses presented in order to obtain all necessary data: - All mineral intensity data have been obtained from Lucas et al,2012. The useful life has been obtained from Lucas et al, 2012.
    """
    return _ext_constant_material_intensity_ev_home_charger()


_ext_constant_material_intensity_ev_home_charger = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "World",
    "EV_charger_home*",
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    _root,
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    "_ext_constant_material_intensity_ev_home_charger",
)


@component.add(
    name="MATERIAL_INTENSITY_EV_NORMAL_CHARGER",
    units="kg/charger",
    subscripts=["MATERIALS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_material_intensity_ev_normal_charger"},
)
def material_intensity_ev_normal_charger():
    """
    Materials requirements per EV charger. Hypotheses presented in order to obtain all necessary data: - All mineral intensity data have been obtained from Lucas et al,2012.The useful life has been obtained from Lucas et al, 2012.
    """
    return _ext_constant_material_intensity_ev_normal_charger()


_ext_constant_material_intensity_ev_normal_charger = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "World",
    "EV_charger_normal*",
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    _root,
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    "_ext_constant_material_intensity_ev_normal_charger",
)


@component.add(
    name="MATERIAL_INTENSITY_EV_QUICK_CHARGER",
    units="kg/charger",
    subscripts=["MATERIALS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_material_intensity_ev_quick_charger"},
)
def material_intensity_ev_quick_charger():
    """
    Materials requirements per EV charger. Hypotheses presented in order to obtain all necessary data: - All mineral intensity data have been obtained from Lucas et al,2012 except for the copper of the fast charger (obtained from IDTechx, 2017) and the iron of this same charger (obtained by establishing the same ratio between the copper weight of Lucas et al, 2012 and IDTechEx (study, How Important are Electric Vehicles for Future Copper Demand, 2017), that is, taking a 21.05% reduction of material with respect to Lucas et al). The useful life has been obtained from Lucas et al, 2012.
    """
    return _ext_constant_material_intensity_ev_quick_charger()


_ext_constant_material_intensity_ev_quick_charger = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "World",
    "EV_charger_quick*",
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    _root,
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    "_ext_constant_material_intensity_ev_quick_charger",
)


@component.add(
    name="MATERIAL_INTENSITY_NEW_CAPACITY_CSP",
    units="kg/MW",
    subscripts=["MATERIALS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_material_intensity_new_capacity_csp"},
)
def material_intensity_new_capacity_csp():
    """
    Materials requirements per unit of new installed capacity of solar CSP.
    """
    return _ext_constant_material_intensity_new_capacity_csp()


_ext_constant_material_intensity_new_capacity_csp = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "World",
    "material_intensity_CSP*",
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    _root,
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    "_ext_constant_material_intensity_new_capacity_csp",
)


@component.add(
    name="MATERIAL_INTENSITY_NEW_CAPACITY_HVDCS",
    subscripts=["MATERIALS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_material_intensity_new_capacity_hvdcs"},
)
def material_intensity_new_capacity_hvdcs():
    return _ext_constant_material_intensity_new_capacity_hvdcs()


_ext_constant_material_intensity_new_capacity_hvdcs = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "World",
    "material_intensity_HVDC*",
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    _root,
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    "_ext_constant_material_intensity_new_capacity_hvdcs",
)


@component.add(
    name="MATERIAL_INTENSITY_NEW_CAPACITY_OVERGRID_HIGH_POWER",
    subscripts=["MATERIALS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_material_intensity_new_capacity_overgrid_high_power"
    },
)
def material_intensity_new_capacity_overgrid_high_power():
    return _ext_constant_material_intensity_new_capacity_overgrid_high_power()


_ext_constant_material_intensity_new_capacity_overgrid_high_power = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "World",
    "material_intensity_overgrid_high_power*",
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    _root,
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    "_ext_constant_material_intensity_new_capacity_overgrid_high_power",
)


@component.add(
    name="MATERIAL_INTENSITY_NEW_CAPACITY_WIND_OFFSHORE",
    units="kg/MW",
    subscripts=["MATERIALS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_material_intensity_new_capacity_wind_offshore"
    },
)
def material_intensity_new_capacity_wind_offshore():
    """
    Materials requirements per unit of new installed capacity of wind offshore.
    """
    return _ext_constant_material_intensity_new_capacity_wind_offshore()


_ext_constant_material_intensity_new_capacity_wind_offshore = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "World",
    "material_intensity_wind_offshore*",
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    _root,
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    "_ext_constant_material_intensity_new_capacity_wind_offshore",
)


@component.add(
    name="MATERIAL_INTENSITY_NEW_CAPACITY_WIND_ONSHORE",
    units="kg/MW",
    subscripts=["MATERIALS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_material_intensity_new_capacity_wind_onshore"
    },
)
def material_intensity_new_capacity_wind_onshore():
    """
    Materials requirements per unit of new installed capacity of wind onshore.
    """
    return _ext_constant_material_intensity_new_capacity_wind_onshore()


_ext_constant_material_intensity_new_capacity_wind_onshore = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "World",
    "material_intensity_wind_onshore*",
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    _root,
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    "_ext_constant_material_intensity_new_capacity_wind_onshore",
)


@component.add(
    name="MATERIAL_INTENSITY_OM_CSP",
    units="kg/(Year*MW)",
    subscripts=["MATERIALS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_material_intensity_om_csp"},
)
def material_intensity_om_csp():
    """
    Materials requirements for operation and maintenance per unit of new installed capacity of solar CSP.
    """
    return _ext_constant_material_intensity_om_csp()


_ext_constant_material_intensity_om_csp = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "World",
    "materials_OM_per_capacity_installed_CSP*",
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    _root,
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    "_ext_constant_material_intensity_om_csp",
)


@component.add(
    name="MATERIAL_INTENSITY_OM_WIND_OFFSHORE",
    units="kg/(Year*MW)",
    subscripts=["MATERIALS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_material_intensity_om_wind_offshore"},
)
def material_intensity_om_wind_offshore():
    return _ext_constant_material_intensity_om_wind_offshore()


_ext_constant_material_intensity_om_wind_offshore = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "World",
    "materials_OM_per_capacity_installed_wind_offshore*",
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    _root,
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    "_ext_constant_material_intensity_om_wind_offshore",
)


@component.add(
    name="MATERIAL_INTENSITY_OM_WIND_ONSHORE",
    units="kg/(Year*MW)",
    subscripts=["MATERIALS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_material_intensity_om_wind_onshore"},
)
def material_intensity_om_wind_onshore():
    return _ext_constant_material_intensity_om_wind_onshore()


_ext_constant_material_intensity_om_wind_onshore = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "World",
    "materials_OM_per_capacity_installed_wind_onshore*",
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    _root,
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    "_ext_constant_material_intensity_om_wind_onshore",
)


@component.add(
    name="MATERIAL_INTENSITY_PV_INVERTER",
    units="kg/MW",
    subscripts=["MATERIALS_I", "PROTRA_PP_SOLAR_PV_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_material_intensity_pv_inverter"},
)
def material_intensity_pv_inverter():
    """
    Materials requirements per MW for inverter of solar PV. The material requirements of these systems as stated by (Tschümperlin et al., n.d.) have been extrapolated to obtain the requirements of a 1 MW inverter.
    """
    return _ext_constant_material_intensity_pv_inverter()


_ext_constant_material_intensity_pv_inverter = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "PV",
    "MATERIAL_INTENSITY_PV_INVERTER",
    {
        "MATERIALS_I": _subscript_dict["MATERIALS_I"],
        "PROTRA_PP_SOLAR_PV_I": _subscript_dict["PROTRA_PP_SOLAR_PV_I"],
    },
    _root,
    {
        "MATERIALS_I": _subscript_dict["MATERIALS_I"],
        "PROTRA_PP_SOLAR_PV_I": _subscript_dict["PROTRA_PP_SOLAR_PV_I"],
    },
    "_ext_constant_material_intensity_pv_inverter",
)


@component.add(
    name="MATERIAL_INTENSITY_PV_SUBTECHNOLOGY_PANEL_FRAME",
    units="kg/m2",
    subscripts=["MATERIALS_I", "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_material_intensity_pv_subtechnology_panel_frame"
    },
)
def material_intensity_pv_subtechnology_panel_frame():
    """
    Materials requirements per m2 of new panel structures of solar C-SI mono PV technology. The material intensities of panel construction have been obtained from (Frischknecht et al., 2015) except for aluminium, titanium and vanadium. In the case of aluminium, the intensities from (Frischknecht et al., 2015) and (Gervais et al., 2021) have been added. Titanium and vanadium have been obtained from (de Castro and Capellán-Pérez, 2020).
    """
    return _ext_constant_material_intensity_pv_subtechnology_panel_frame()


_ext_constant_material_intensity_pv_subtechnology_panel_frame = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "PV",
    "MATERIAL_INTENSITY_PV_SUBTECHNOLOGY_PANEL_FRAME",
    {
        "MATERIALS_I": _subscript_dict["MATERIALS_I"],
        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": _subscript_dict[
            "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"
        ],
    },
    _root,
    {
        "MATERIALS_I": _subscript_dict["MATERIALS_I"],
        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": _subscript_dict[
            "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"
        ],
    },
    "_ext_constant_material_intensity_pv_subtechnology_panel_frame",
)


@component.add(
    name="MATERIAL_INTENSITY_PV_TRANSFORMER_LAND",
    units="kg/MW",
    subscripts=["MATERIALS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_material_intensity_pv_transformer_land"},
)
def material_intensity_pv_transformer_land():
    """
    Materials requirements per MW for transformer of solar ground technology.A 1MW step-up transformer up to 24kV from Ormazabal (ORMAZABAL, 2022) has been chosen.
    """
    return _ext_constant_material_intensity_pv_transformer_land()


_ext_constant_material_intensity_pv_transformer_land = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "PV",
    "MATERIAL_INTENSITY_PV_TRANSFORMER_LAND*",
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    _root,
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    "_ext_constant_material_intensity_pv_transformer_land",
)


@component.add(
    name="MATERIAL_INTENSITY_RATIO_OM_PV_PANELS",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_material_intensity_ratio_om_pv_panels"},
)
def material_intensity_ratio_om_pv_panels():
    """
    Ratio used to calculate the O&M materials demand of the PV panels. Taken from De Castro et al 2020.
    """
    return _ext_constant_material_intensity_ratio_om_pv_panels()


_ext_constant_material_intensity_ratio_om_pv_panels = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "PV",
    "O_M_PV_TECHNOLOGIES_RATIO*",
    {},
    _root,
    {},
    "_ext_constant_material_intensity_ratio_om_pv_panels",
)


@component.add(
    name="MATERIAL_REQUIREMENTS_PV_MOUNTING_STRUCTURES_BASELINE",
    units="kg/m2",
    subscripts=["MATERIALS_I", "PROTRA_PP_SOLAR_PV_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_material_requirements_pv_mounting_structures_baseline"
    },
)
def material_requirements_pv_mounting_structures_baseline():
    """
    Materials requirements per m2 of panel of new mounting structures of solar PV technology. The construction requirements of the panel mounting structures have been obtained from (Frischknecht et al., 2015) except for the cement which has been obtained from (de Castro and Capellán-Pérez, 2020).
    """
    return _ext_constant_material_requirements_pv_mounting_structures_baseline()


_ext_constant_material_requirements_pv_mounting_structures_baseline = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "PV",
    "MATERIAL_REQUIREMENTS_PV_MOUNTING_STRUCTURES_BASELINE",
    {
        "MATERIALS_I": _subscript_dict["MATERIALS_I"],
        "PROTRA_PP_SOLAR_PV_I": _subscript_dict["PROTRA_PP_SOLAR_PV_I"],
    },
    _root,
    {
        "MATERIALS_I": _subscript_dict["MATERIALS_I"],
        "PROTRA_PP_SOLAR_PV_I": _subscript_dict["PROTRA_PP_SOLAR_PV_I"],
    },
    "_ext_constant_material_requirements_pv_mounting_structures_baseline",
)


@component.add(
    name="MATERIAL_REQUIREMENTS_PV_WIRING_BUILDING",
    units="kg/m",
    subscripts=["MATERIALS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_material_requirements_pv_wiring_building"
    },
)
def material_requirements_pv_wiring_building():
    """
    Mineral requirements per metre for the wiring of a photovoltaic system in a building. Photovoltaic cables of 10mm2 have been considered for installations whose power is higher but whose purpose is also not to produce energy. The consideration of these sizes has been taken due to two fundamental factors. The first, the experience visualising the wiring that is usually used in these installations (Andreu Rico, 2018; José Alfonso Alonso Lorenzo, n.d.). The second, the calculation of the wiring sections using the ICT-18 voltage drop and heating criteria, which indicates that these sizes are suitable for most of these types of installations (Andreu Rico, 2018; José Alfonso Alonso Lorenzo, n.d.; Ministerio de ciencia y tecnología, 2003).
    """
    return _ext_constant_material_requirements_pv_wiring_building()


_ext_constant_material_requirements_pv_wiring_building = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "PV",
    "MATERIAL_REQUIREMENTS_PV_WIRING_BUILDING*",
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    _root,
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    "_ext_constant_material_requirements_pv_wiring_building",
)


@component.add(
    name="MATERIAL_REQUIREMENTS_PV_WIRING_HOUSE",
    units="kg/m",
    subscripts=["MATERIALS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_material_requirements_pv_wiring_house"},
)
def material_requirements_pv_wiring_house():
    """
    Mineral requirements per metre for the wiring of a photovoltaic system in a house. Photovoltaic cables of 6 mm2 have been considered for smaller installations. The consideration of these sizes has been taken due to two fundamental factors. The first, the experience visualising the wiring that is usually used in these installations (Andreu Rico, 2018; José Alfonso Alonso Lorenzo, n.d.). The second, the calculation of the wiring sections using the ICT-18 voltage drop and heating criteria, which indicates that these sizes are suitable for most of these types of installations (Andreu Rico, 2018; José Alfonso Alonso Lorenzo, n.d.; Ministerio de ciencia y tecnología, 2003).
    """
    return _ext_constant_material_requirements_pv_wiring_house()


_ext_constant_material_requirements_pv_wiring_house = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "PV",
    "MATERIAL_REQUIREMENTS_PV_WIRING_HOUSE*",
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    _root,
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    "_ext_constant_material_requirements_pv_wiring_house",
)


@component.add(
    name="MATERIAL_REQUIREMENTS_PV_WIRING_LAND_INVERTER_TO_TRANSFORMER",
    units="kg/m",
    subscripts=["MATERIALS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_material_requirements_pv_wiring_land_inverter_to_transformer"
    },
)
def material_requirements_pv_wiring_land_inverter_to_transformer():
    """
    Mineral requirements per metre for the wiring of a photovoltaic ground system from the inverter to the transformer. With regard to the connection of the installation with the transmission grid (up to the transformer), the data of (Bumby et al., 2010, 2011) have been taken as a reference. A two-pipe pipe with a diameter of 160 mm inserted in a concrete cube with a side of 45 cm and a thickness of about 5 cm, taken from the instructions of the low and medium voltage guide (Ministry of Science and Technology, 2003), was chosen as the reference pipe. The weight of concrete from the latter reference has been compared with the weight of concrete from Bumby et al. (Bumby et al., 2010) using this ratio to apply to the other materials.
    """
    return _ext_constant_material_requirements_pv_wiring_land_inverter_to_transformer()


_ext_constant_material_requirements_pv_wiring_land_inverter_to_transformer = (
    ExtConstant(
        "model_parameters/materials/materials.xlsx",
        "PV",
        "MATERIAL_REQUIREMENTS_PV_WIRING_LAND_INVERTER_TO_TRANSFORMER*",
        {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
        _root,
        {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
        "_ext_constant_material_requirements_pv_wiring_land_inverter_to_transformer",
    )
)


@component.add(
    name="MATERIAL_REQUIREMENTS_PV_WIRING_LAND_PANEL_TO_INVERTER",
    units="kg/m",
    subscripts=["MATERIALS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_material_requirements_pv_wiring_land_panel_to_inverter"
    },
)
def material_requirements_pv_wiring_land_panel_to_inverter():
    """
    Mineral requirements per metre for the wiring of a photovoltaic ground system from panel to the inverter. A 16 mm2 photovoltaic cable has been chosen to connect the panels and inverters of the electricity production installations (solar farms and solar parks). The consideration of these sizes has been taken due to two fundamental factors. The first, the experience visualising the wiring that is usually used in these installations (Andreu Rico, 2018; José Alfonso Alonso Lorenzo, n.d.). The second, the calculation of the wiring sections using the ICT-18 voltage drop and heating criteria, which indicates that these sizes are suitable for most of these types of installations (Andreu Rico, 2018; José Alfonso Alonso Lorenzo, n.d.; Ministerio de ciencia y tecnología, 2003).
    """
    return _ext_constant_material_requirements_pv_wiring_land_panel_to_inverter()


_ext_constant_material_requirements_pv_wiring_land_panel_to_inverter = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "PV",
    "MATERIAL_REQUIREMENTS_PV_WIRING_LAND_PANEL_TO_INVERTER*",
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    _root,
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    "_ext_constant_material_requirements_pv_wiring_land_panel_to_inverter",
)


@component.add(
    name='"materials_for_O&M_per_capacity_installed_PV"',
    subscripts=["MATERIALS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_materials_for_om_per_capacity_installed_pv"
    },
)
def materials_for_om_per_capacity_installed_pv():
    return _ext_constant_materials_for_om_per_capacity_installed_pv()


_ext_constant_materials_for_om_per_capacity_installed_pv = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "World",
    "materials_OM_per_capacity_installed_PV*",
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    _root,
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    "_ext_constant_materials_for_om_per_capacity_installed_pv",
)


@component.add(
    name="MATERIALS_PER_NEW_CAPACITY_INSTALLED_EV_BATTERIES_LFP",
    units="kg/MW",
    subscripts=["MATERIALS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_materials_per_new_capacity_installed_ev_batteries_lfp"
    },
)
def materials_per_new_capacity_installed_ev_batteries_lfp():
    """
    Materials requirements per EV battery LFP. It has been established that each battery has a capacity of 60 kWh (as several models on the market at 2021) and 100 kW of power. -LFP: From Dunn et al 2014 has been achieved the (%) of Aluminium and cooper of an EV battery From Linda Gaines et al 2009 has been achieved the amount of phosphorus and iron from the LFP battery From Luis De La Torre Palacios et al 2019 has been achieved the minerals from the cathodes. From Dunn et al 2015 has been obtained the EnU of some components of the battery in percentage (Graphite).
    """
    return _ext_constant_materials_per_new_capacity_installed_ev_batteries_lfp()


_ext_constant_materials_per_new_capacity_installed_ev_batteries_lfp = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "World",
    "LFP_battery*",
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    _root,
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    "_ext_constant_materials_per_new_capacity_installed_ev_batteries_lfp",
)


@component.add(
    name="MATERIALS_PER_NEW_CAPACITY_INSTALLED_EV_BATTERIES_LMO",
    units="kg/MW",
    subscripts=["MATERIALS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_materials_per_new_capacity_installed_ev_batteries_lmo"
    },
)
def materials_per_new_capacity_installed_ev_batteries_lmo():
    """
    Materials requirements per EV battery LiMnO2.It has been established that each battery has a capacity of 60 kWh (as several models on the market at 2021) and 100 kW of power. -LiMnO2: From Dunn et al 2014 has been obtained the weight (%) of Aluminium and cooper of an EV battery, from Dunn et al 2015 has been achieved the EnU of some components of the battery in percentage (Lithium, Manganese and Graphite).
    """
    return _ext_constant_materials_per_new_capacity_installed_ev_batteries_lmo()


_ext_constant_materials_per_new_capacity_installed_ev_batteries_lmo = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "World",
    "LiMnO2_battery*",
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    _root,
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    "_ext_constant_materials_per_new_capacity_installed_ev_batteries_lmo",
)


@component.add(
    name="MATERIALS_PER_NEW_CAPACITY_INSTALLED_EV_BATTERIES_NCA",
    units="kg/MW",
    subscripts=["MATERIALS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_materials_per_new_capacity_installed_ev_batteries_nca"
    },
)
def materials_per_new_capacity_installed_ev_batteries_nca():
    """
    Materials requirements per EV battery NCA.It has been established that each battery has a capacity of 60 kWh (as several models on the market at 2021) and 100 kW of power. -NCA: From Dunn et al 2014 has been achieved the (%) of Aluminium and cooper of an EV battery, from Luis De La Torre Palacios et al 2019 has been achieved the minerals from the cathodes. From Dunn et al 2015 has been obtained the EnU of some components of the battery in percentage (Graphite) assuming a similar percentage to NMC batteries.
    """
    return _ext_constant_materials_per_new_capacity_installed_ev_batteries_nca()


_ext_constant_materials_per_new_capacity_installed_ev_batteries_nca = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "World",
    "NCA_battery*",
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    _root,
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    "_ext_constant_materials_per_new_capacity_installed_ev_batteries_nca",
)


@component.add(
    name="MATERIALS_PER_NEW_CAPACITY_INSTALLED_EV_BATTERIES_NMC622",
    units="kg/MW",
    subscripts=["MATERIALS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_materials_per_new_capacity_installed_ev_batteries_nmc622"
    },
)
def materials_per_new_capacity_installed_ev_batteries_nmc622():
    """
    Materials requirements per EV battery NMC622.It has been established that each battery has a capacity of 60 kWh (as several models on the market at 2021) and 100 kW of power. -NMC-622: From Dunn et al 2014 has been obtained the weight (%) of Aluminium and copper of an EV battery, from Luis De La Torre Palacios et al 2019 has been achieved the minerals from the cathodes. From Dunn et al 2015 has been obtained the EnU of some components of the battery in percentage (Graphite).
    """
    return _ext_constant_materials_per_new_capacity_installed_ev_batteries_nmc622()


_ext_constant_materials_per_new_capacity_installed_ev_batteries_nmc622 = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "World",
    "NMC622_battery*",
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    _root,
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    "_ext_constant_materials_per_new_capacity_installed_ev_batteries_nmc622",
)


@component.add(
    name="MATERIALS_PER_NEW_CAPACITY_INSTALLED_EV_BATTERIES_NMC811",
    units="kg/MW",
    subscripts=["MATERIALS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_materials_per_new_capacity_installed_ev_batteries_nmc811"
    },
)
def materials_per_new_capacity_installed_ev_batteries_nmc811():
    """
    Materials requirements per EV battery NMC811. It has been established that each battery has a capacity of 60 kWh (as several models on the market at 2021) and 100 kW of power. -NMC-811: From Dunn et al 2014 has been obtained the weight (%) of Aluminium and cooper of an EV battery, from Luis De La Torre Palacios et al 2019 has been achieved the minerals from the cathodes. From Dunn et al 2015 has been obtained the EnU of some components of the battery in percentage (Graphite).
    """
    return _ext_constant_materials_per_new_capacity_installed_ev_batteries_nmc811()


_ext_constant_materials_per_new_capacity_installed_ev_batteries_nmc811 = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "World",
    "NMC811_battery*",
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    _root,
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    "_ext_constant_materials_per_new_capacity_installed_ev_batteries_nmc811",
)


@component.add(
    name="Max_recycling_rates_minerals",
    units="Dnml",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_max_recycling_rates_minerals"},
)
def max_recycling_rates_minerals():
    """
    Maximum assumed recycling rate per mineral.
    """
    return _ext_constant_max_recycling_rates_minerals()


_ext_constant_max_recycling_rates_minerals = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "World",
    "max_recycling_rates_minerals",
    {},
    _root,
    {},
    "_ext_constant_max_recycling_rates_minerals",
)


@component.add(
    name="Mn_ENERGY_REQUIRED_PER_ORE_GRADE",
    units="MJ/kg",
    subscripts=["Mn_ORE_GRADES_I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def mn_energy_required_per_ore_grade():
    """
    This is the energy and water used associated with the materials consumed to extract this specific resource grade, expressed in MJ/kg product and m3/ton. The actual values are taken from an internal LOCOMOTION report that have extracted the available values from literature and extrapolations. Source: Harald Sverdrup and Anna Hulda Olafsdottir 2021. Assessing with the WORLD7 model the global CO2 emissions and water use by metals, materials and fossil fuels extraction and production. LOCOMOTION working paper. 52 pages.
    """
    value = xr.DataArray(
        np.nan,
        {"Mn_ORE_GRADES_I": _subscript_dict["Mn_ORE_GRADES_I"]},
        ["Mn_ORE_GRADES_I"],
    )
    value.loc[["RICH_GRADE"]] = 22
    value.loc[["HIGH_GRADE"]] = 27
    value.loc[["LOW_GRADE"]] = 44
    return value


@component.add(
    name="Mn_IN_Al", units="DMNL", comp_type="Constant", comp_subtype="Normal"
)
def mn_in_al():
    """
    Derived from literature as explained in Sverdrup, H., and Olafsdottir, A.H., 2019., Assessing the Longâ€Term Global Sustainability of the Production and Supply for Stainless Steel. Biophysical Economics and Resource Quality 1-26. https://doi.org/10.1007/s41247-019-0056-9 Open access publication.
    """
    return 0.001


@component.add(
    name="Mo_CONTENT_IN_Ni", units="DMNL", comp_type="Constant", comp_subtype="Normal"
)
def mo_content_in_ni():
    """
    Sverdrup, H., Olofsdottir, A.H., Ragnarsdottir, K.V., Koca, D., 2018. A system dynamics assessment of the supply of molybdenum and rhenium used for superalloys and specialty steels, using the WORLD6 model. Biophysical Economics and Resource Quality 4: 1-52 (DOI: 10.1007/s41247-018-0040-9)
    """
    return 0.004


@component.add(
    name="Mo_MINING_COEFFICIENT",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="Normal",
)
def mo_mining_coefficient():
    """
    The average modern extraction rate as the ratio between amount extracted and the konown reserve in 2005. The adjusted with feedbacks. Sverdrup, H., Olofsdottir, A.H., Ragnarsdottir, K.V., Koca, D., 2018. A system dynamics assessment of the supply of molybdenum and rhenium used for superalloys and specialty steels, using the WORLD6 model. Biophysical Economics and Resource Quality 4: 1-52 (DOI: 10.1007/s41247-018-0040-9)
    """
    return 0.035


@component.add(
    name="Mo_retention_time", units="Years", comp_type="Constant", comp_subtype="Normal"
)
def mo_retention_time():
    """
    Retention time of Mo i alloys. This has been set to 30 years, based on the assumption that it goes into high quality specialty steels that tend to saty long in use. Typical uses are machinery, quality tools, technological infra structure. Mo is not very much used in short term consumer goods. Sverdrup, H., Olofsdottir, A.H., Ragnarsdottir, K.V., Koca, D., 2018. A system dynamics assessment of the supply of molybdenum and rhenium used for superalloys and specialty steels, using the WORLD6 model. Biophysical Economics and Resource Quality 4: 1-52 (DOI: 10.1007/s41247-018-0040-9)
    """
    return 30


@component.add(
    name="Mo_YIELD_IN_Cu", units="DMNL", comp_type="Constant", comp_subtype="Normal"
)
def mo_yield_in_cu():
    """
    Sverdrup, H., Olofsdottir, A.H., Ragnarsdottir, K.V., Koca, D., 2018. A system dynamics assessment of the supply of molybdenum and rhenium used for superalloys and specialty steels, using the WORLD6 model. Biophysical Economics and Resource Quality 4: 1-52 (DOI: 10.1007/s41247-018-0040-9)
    """
    return 0.9


@component.add(
    name="Ni_ENERGY_RECYCLING",
    units="MJ/kg",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_ni_energy_recycling"},
)
def ni_energy_recycling():
    """
    Our own estimates of water use per grade extraction, based on a large literature survey. See the separate report for documentation of setting the value and where the information came from. Sverdrup and Olafsdottir 2021: Assessing the global energy and water use from of metals, materials and fossil fuels extraction and production. Internal report for LOCOMOTION WP7. 44pp
    """
    return _ext_constant_ni_energy_recycling()


_ext_constant_ni_energy_recycling = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Nickel",
    "Ni_ENERGY_RECYCLING",
    {},
    _root,
    {},
    "_ext_constant_ni_energy_recycling",
)


@component.add(
    name="Ni_SCRAPPING_RATE",
    units="1/Years",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_ni_scrapping_rate"},
)
def ni_scrapping_rate():
    """
    Our own assumption on what gets scrapped from other use, implying a life time of 3 years in society.
    """
    return _ext_constant_ni_scrapping_rate()


_ext_constant_ni_scrapping_rate = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Nickel",
    "Ni_SCRAPPING_RATE",
    {},
    _root,
    {},
    "_ext_constant_ni_scrapping_rate",
)


@component.add(
    name="NUMBER_CHARGERS_PER_TYPE_OF_VEHICLE",
    units="chargers/vehicle",
    subscripts=["TRANSPORT_POWER_TRAIN_I", "BATTERY_VEHICLES_I", "EV_CHARGERS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_number_chargers_per_type_of_vehicle"},
)
def number_chargers_per_type_of_vehicle():
    """
    Estimated number of different types of chargers per vehicle. Household vehicles: -4-wheeled electric vehicles (H4w BEV) (Car/Cab): This data has been obtained from the Lucas et al, 2012. -2-wheeled electric vehicles (H2w BEV) (Motorcycle): As this type of vehicles has a similar use to 4-wheeled electric vehicles in the urban environment, the same number of home chargers and conventional chargers are established, but as these vehicles are not made for the purpose of traveling, 0 fast chargers have been arranged.
    """
    return _ext_constant_number_chargers_per_type_of_vehicle()


_ext_constant_number_chargers_per_type_of_vehicle = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "World",
    "NUMBER_HOME_CHARGERS_PER_TYPE_OF_VEHICLE",
    {
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "BATTERY_VEHICLES_I": _subscript_dict["BATTERY_VEHICLES_I"],
        "EV_CHARGERS_I": ["home"],
    },
    _root,
    {
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "BATTERY_VEHICLES_I": _subscript_dict["BATTERY_VEHICLES_I"],
        "EV_CHARGERS_I": _subscript_dict["EV_CHARGERS_I"],
    },
    "_ext_constant_number_chargers_per_type_of_vehicle",
)

_ext_constant_number_chargers_per_type_of_vehicle.add(
    "model_parameters/materials/materials.xlsx",
    "World",
    "NUMBER_NORMAL_CHARGERS_PER_TYPE_OF_VEHICLE",
    {
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "BATTERY_VEHICLES_I": _subscript_dict["BATTERY_VEHICLES_I"],
        "EV_CHARGERS_I": ["normal"],
    },
)

_ext_constant_number_chargers_per_type_of_vehicle.add(
    "model_parameters/materials/materials.xlsx",
    "World",
    "NUMBER_QUICK_CHARGERS_PER_TYPE_OF_VEHICLE",
    {
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "BATTERY_VEHICLES_I": _subscript_dict["BATTERY_VEHICLES_I"],
        "EV_CHARGERS_I": ["quick"],
    },
)


@component.add(
    name="OBJECTIVE_SC_SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_objective_sc_sp"},
)
def objective_sc_sp():
    """
    percentage target of vehicles using Smart charging
    """
    return _ext_constant_objective_sc_sp()


_ext_constant_objective_sc_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "OBJECTIVE_SC_SP",
    {},
    _root,
    {},
    "_ext_constant_objective_sc_sp",
)


@component.add(
    name="OBJECTIVE_V2G_SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_objective_v2g_sp"},
)
def objective_v2g_sp():
    """
    percentage target of vehicles using V2G
    """
    return _ext_constant_objective_v2g_sp()


_ext_constant_objective_v2g_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "TARGET_VALUE_V2G_SP",
    {},
    _root,
    {},
    "_ext_constant_objective_v2g_sp",
)


@component.add(
    name="OL_EV_BATTERIES",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_ol_ev_batteries"},
)
def ol_ev_batteries():
    """
    The coefficient represents the fixed electricity losses of the batteries, it is the energy lost by the self-discharge of the batteries together with the energy that could not be stored in the battery due to its loss of capacity over time.
    """
    return _ext_constant_ol_ev_batteries()


_ext_constant_ol_ev_batteries = ExtConstant(
    "model_parameters/energy/energy-transport.xlsx",
    "electrified_transport",
    "OL_EV_BATTERIES",
    {},
    _root,
    {},
    "_ext_constant_ol_ev_batteries",
)


@component.add(
    name="POLICY_COMMON_RR_MINERALS_VARIATION_ALT_TECHN_SP",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"policy_common_rr_minerals_variation_alt_techn_sp_w": 1},
)
def policy_common_rr_minerals_variation_alt_techn_sp():
    """
    Annual recycling rate improvement per mineral for alternative technologies (RES elec & EV batteries).
    """
    return xr.DataArray(
        policy_common_rr_minerals_variation_alt_techn_sp_w(),
        {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
        ["REGIONS_9_I"],
    )


@component.add(
    name="POLICY_COMMON_RR_MINERALS_VARIATION_ALT_TECHN_SP_W",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_policy_common_rr_minerals_variation_alt_techn_sp_w"
    },
)
def policy_common_rr_minerals_variation_alt_techn_sp_w():
    """
    Annual recycling rate improvement per mineral for alternative technologies (RES elec & EV batteries).
    """
    return _ext_constant_policy_common_rr_minerals_variation_alt_techn_sp_w()


_ext_constant_policy_common_rr_minerals_variation_alt_techn_sp_w = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "materials",
    "P_recycling_minerals_alternative_technologies_RES_elec_EV_batteries",
    {},
    _root,
    {},
    "_ext_constant_policy_common_rr_minerals_variation_alt_techn_sp_w",
)


@component.add(
    name="POLICY_COMMON_RR_MINERALS_VARIATION_REST_SP",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"policy_common_rr_minerals_variation_rest_sp_w": 1},
)
def policy_common_rr_minerals_variation_rest_sp():
    """
    Annual recycling rate improvement per mineral for the rest of the economy.
    """
    return xr.DataArray(
        policy_common_rr_minerals_variation_rest_sp_w(),
        {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
        ["REGIONS_9_I"],
    )


@component.add(
    name="POLICY_COMMON_RR_MINERALS_VARIATION_REST_SP_W",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_policy_common_rr_minerals_variation_rest_sp_w"
    },
)
def policy_common_rr_minerals_variation_rest_sp_w():
    """
    Annual recycling rate improvement per mineral for the rest of the economy.
    """
    return _ext_constant_policy_common_rr_minerals_variation_rest_sp_w()


_ext_constant_policy_common_rr_minerals_variation_rest_sp_w = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "materials",
    "P_recycling_minerals_Rest",
    {},
    _root,
    {},
    "_ext_constant_policy_common_rr_minerals_variation_rest_sp_w",
)


@component.add(
    name="PROFIT_MARGIN_ON_EXTRACTION",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="Normal",
)
def profit_margin_on_extraction():
    """
    This variable makes certain that there is a 10% profit margin on extraction
    """
    return 1.1


@component.add(
    name="RECYCLE_FRACTION_FROM_CHEMICALS",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="Normal",
)
def recycle_fraction_from_chemicals():
    """
    Sverdrup, H., Olofsdottir, A.H., Ragnarsdottir, K.V., Koca, D., 2018. A system dynamics assessment of the supply of molybdenum and rhenium used for superalloys and specialty steels, using the WORLD6 model. Biophysical Economics and Resource Quality 4: 1-52 (DOI: 10.1007/s41247-018-0040-9)
    """
    return 0.05


@component.add(
    name="RECYCLING_ENERGY_USE",
    units="TJ/Mt",
    comp_type="Constant",
    comp_subtype="Normal",
)
def recycling_energy_use():
    """
    Our own estimates of water use per grade extraction, based on a large literature survey. See the separate report for documentation of setting the value and where the information came from. Sverdrup and Olafsdottir 2021: Assessing the global energy and water use from of metals, materials and fossil fuels extraction and production. Internal report for LOCOMOTION WP7. 44pp
    """
    return 45


@component.add(
    name="REDUCTION_RATE_MATERIAL_INTENSITY_C_SI_PV_Si_SP",
    units="DMNL/Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_reduction_rate_material_intensity_c_si_pv_si_sp"
    },
)
def reduction_rate_material_intensity_c_si_pv_si_sp():
    """
    Annual reduction rate of silicon (Si) intensity in PV cells. A negative value corresponds with an increase in the material intensity. Trends obtained in the master's thesis of Daniel Pulido Sanchez, Material requirements and EROI of photovoltaic technologies in the energy transition (2022).
    """
    return _ext_constant_reduction_rate_material_intensity_c_si_pv_si_sp()


_ext_constant_reduction_rate_material_intensity_c_si_pv_si_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "materials",
    "REDUCTION_MINERAL_DEMAND_PV_SI_SP*",
    {},
    _root,
    {},
    "_ext_constant_reduction_rate_material_intensity_c_si_pv_si_sp",
)


@component.add(
    name="REDUCTION_RATE_MATERIAL_INTENSITY_C_SI_PV_Sn_SP",
    units="DMNL/Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_reduction_rate_material_intensity_c_si_pv_sn_sp"
    },
)
def reduction_rate_material_intensity_c_si_pv_sn_sp():
    """
    Annual reduction rate of tin (Sn) intensity in PV cells. A negative value corresponds with an increase in the material intensity. Trends obtained in the master's thesis of Daniel Pulido Sanchez, Material requirements and EROI of photovoltaic technologies in the energy transition (2022).
    """
    return _ext_constant_reduction_rate_material_intensity_c_si_pv_sn_sp()


_ext_constant_reduction_rate_material_intensity_c_si_pv_sn_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "materials",
    "REDUCTION_MINERAL_DEMAND_PV_TIN_SP*",
    {},
    _root,
    {},
    "_ext_constant_reduction_rate_material_intensity_c_si_pv_sn_sp",
)


@component.add(
    name="REDUCTION_RATE_MATERIAL_INTENSITY_PV_REST_OF_MATERIALS_SP",
    units="DMNL/Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_reduction_rate_material_intensity_pv_rest_of_materials_sp"
    },
)
def reduction_rate_material_intensity_pv_rest_of_materials_sp():
    """
    Reduction annual rate of material intensities of PV cells for the rest of materials (i.e., excluding Tin and Silicon). A negative value corresponds with an increase in the material intensity. No clear trends for most of the minerals, so it is modelled assuming same improvement rate for all of them.
    """
    return _ext_constant_reduction_rate_material_intensity_pv_rest_of_materials_sp()


_ext_constant_reduction_rate_material_intensity_pv_rest_of_materials_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "materials",
    "REDUCTION_MATERIAL_INTENSITY_PV_REST_OF_MATERIALS_SP",
    {},
    _root,
    {},
    "_ext_constant_reduction_rate_material_intensity_pv_rest_of_materials_sp",
)


@component.add(
    name="RICH_GRADE_FACTOR",
    units="1/Years",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_rich_grade_factor"},
)
def rich_grade_factor():
    """
    This factor compensates for the fact that the high grade and the rich grade are much easier to mine - the others need more work. These numbers give the best fit to the historical data and therefore they are assumptions based parametersation of the ore grade curve. This consideration the difference between rich and high grade ores vs. lower grade ores. This particular parameter is for the rich grade.
    """
    return _ext_constant_rich_grade_factor()


_ext_constant_rich_grade_factor = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Copper",
    "RICH_GRADE_FACTOR*",
    {},
    _root,
    {},
    "_ext_constant_rich_grade_factor",
)


@component.add(
    name='"RR_minerals_alt_techn_RES_vs._total_economy"',
    units="Dnml",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_rr_minerals_alt_techn_res_vs_total_economy"
    },
)
def rr_minerals_alt_techn_res_vs_total_economy():
    """
    Recycling rate of minerals used in variable RES technologies in relation to the total economy. Since these technologies are novel and often include materials which are used in small quantities in complex products, the recycling rates of the used minerals are lower than for the whole economy.
    """
    return _ext_constant_rr_minerals_alt_techn_res_vs_total_economy()


_ext_constant_rr_minerals_alt_techn_res_vs_total_economy = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "World",
    "EOL_RR_minerals_alt_techn_RES_vs_total_economy",
    {},
    _root,
    {},
    "_ext_constant_rr_minerals_alt_techn_res_vs_total_economy",
)


@component.add(
    name="SCALING_FAKTOR_IN_Al_DEMAND",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="Normal",
)
def scaling_faktor_in_al_demand():
    """
    Scaling factor to match the histrorical demand development.
    """
    return 0.12


@component.add(
    name="SCALING_NUMBERS_FROM_Ni_HIDDEN_TO_Ni_KNOWN",
    units="DMNL",
    subscripts=["ORE_GRADES_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_scaling_numbers_from_ni_hidden_to_ni_known"
    },
)
def scaling_numbers_from_ni_hidden_to_ni_known():
    """
    These are scaling numbers to get the finding from the different ore grades from hidden to known. The factors are not applied to Rich and Ultralow grades, it would be the same as setting them to 1 for these grades
    """
    return _ext_constant_scaling_numbers_from_ni_hidden_to_ni_known()


_ext_constant_scaling_numbers_from_ni_hidden_to_ni_known = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Nickel",
    "SCALING_NUMBERS_FROM_Ni_HIDDEN_TO_Ni_KNOWN*",
    {"ORE_GRADES_I": _subscript_dict["ORE_GRADES_I"]},
    _root,
    {"ORE_GRADES_I": _subscript_dict["ORE_GRADES_I"]},
    "_ext_constant_scaling_numbers_from_ni_hidden_to_ni_known",
)


@component.add(
    name="SCRAP_RATE",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_scrap_rate"},
)
def scrap_rate():
    """
    10% of Scrap rate take from Carlos de Castro et al (2020) paper
    """
    return _ext_constant_scrap_rate()


_ext_constant_scrap_rate = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "World",
    "SCRAP_RATE",
    {},
    _root,
    {},
    "_ext_constant_scrap_rate",
)


@component.add(
    name="SELECT_LOGIT_MODEL_EV_BATTERIES_SUBTECH_ALLOCATION",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_select_logit_model_ev_batteries_subtech_allocation"
    },
)
def select_logit_model_ev_batteries_subtech_allocation():
    """
    1: modified logit model 0: logit model
    """
    return _ext_constant_select_logit_model_ev_batteries_subtech_allocation()


_ext_constant_select_logit_model_ev_batteries_subtech_allocation = ExtConstant(
    "model_parameters/energy/energy.xlsm",
    "allocation_new_capacity_subtech",
    "SELECT_LOGIT_MODEL_EV_BATTERIES_SUBTECH_ALLOCATION",
    {},
    _root,
    {},
    "_ext_constant_select_logit_model_ev_batteries_subtech_allocation",
)


@component.add(
    name="SELECT_MINERAL_RR_TARGETS_SP",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"select_mineral_rr_targets_sp_w": 1},
)
def select_mineral_rr_targets_sp():
    """
    1- Disaggregated by mineral. 2- Common annual variation for all minerals.
    """
    return xr.DataArray(
        select_mineral_rr_targets_sp_w(),
        {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
        ["REGIONS_9_I"],
    )


@component.add(
    name="SELECT_MINERAL_RR_TARGETS_SP_W",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_select_mineral_rr_targets_sp_w"},
)
def select_mineral_rr_targets_sp_w():
    """
    1- Disaggregated by mineral. 2- Common annual variation for all minerals.
    """
    return _ext_constant_select_mineral_rr_targets_sp_w()


_ext_constant_select_mineral_rr_targets_sp_w = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "materials",
    "Disaggregated_by_mineral_1_or_common_annual_variation_for_all_minerals_2",
    {},
    _root,
    {},
    "_ext_constant_select_mineral_rr_targets_sp_w",
)


@component.add(
    name="SHARE_ENERGY_REQUIREMENTS_FOR_DECOM_EV_BATTERIES",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_share_energy_requirements_for_decom_ev_batteries"
    },
)
def share_energy_requirements_for_decom_ev_batteries():
    """
    Share energy requirements for decomissioning EV batteries as a share of the energy requirements for the manufacture of the battery.
    """
    return _ext_constant_share_energy_requirements_for_decom_ev_batteries()


_ext_constant_share_energy_requirements_for_decom_ev_batteries = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "World",
    "share_energy_requirements_for_decom_EV_batteries",
    {},
    _root,
    {},
    "_ext_constant_share_energy_requirements_for_decom_ev_batteries",
)


@component.add(
    name="SHARE_ENERGY_REQUIREMENTS_FOR_DECOMM_PROTRA",
    units="DMNL",
    subscripts=["NRG_PROTRA_I"],
    comp_type="Constant",
    comp_subtype="External, Normal",
    depends_on={
        "__external__": "_ext_constant_share_energy_requirements_for_decomm_protra"
    },
)
def share_energy_requirements_for_decomm_protra():
    """
    Share energy requirements for decomissioning PROTRA plants as a share of the energy requirements for the construction of new capacity.
    """
    value = xr.DataArray(
        np.nan, {"NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"]}, ["NRG_PROTRA_I"]
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[["PROTRA_PP_solar_CSP"]] = False
    except_subs.loc[_subscript_dict["PROTRA_PP_SOLAR_PV_I"]] = False
    except_subs.loc[["PROTRA_PP_wind_offshore"]] = False
    except_subs.loc[["PROTRA_PP_wind_onshore"]] = False
    value.values[except_subs.values] = 0
    def_subs = xr.zeros_like(value, dtype=bool)
    def_subs.loc[["PROTRA_PP_wind_onshore"]] = True
    def_subs.loc[["PROTRA_PP_wind_offshore"]] = True
    def_subs.loc[["PROTRA_PP_solar_open_space_PV"]] = True
    def_subs.loc[["PROTRA_PP_solar_urban_PV"]] = True
    def_subs.loc[["PROTRA_PP_solar_CSP"]] = True
    value.values[
        def_subs.values
    ] = _ext_constant_share_energy_requirements_for_decomm_protra().values[
        def_subs.values
    ]
    return value


_ext_constant_share_energy_requirements_for_decomm_protra = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "World",
    "self_energy_requirements_for_decom_wind_onshore",
    {"NRG_PROTRA_I": ["PROTRA_PP_wind_onshore"]},
    _root,
    {"NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"]},
    "_ext_constant_share_energy_requirements_for_decomm_protra",
)

_ext_constant_share_energy_requirements_for_decomm_protra.add(
    "model_parameters/materials/materials.xlsx",
    "World",
    "self_energy_requirements_for_decom_wind_offshore",
    {"NRG_PROTRA_I": ["PROTRA_PP_wind_offshore"]},
)

_ext_constant_share_energy_requirements_for_decomm_protra.add(
    "model_parameters/materials/materials.xlsx",
    "World",
    "self_energy_requirements_for_decom_solar_pv",
    {"NRG_PROTRA_I": ["PROTRA_PP_solar_open_space_PV"]},
)

_ext_constant_share_energy_requirements_for_decomm_protra.add(
    "model_parameters/materials/materials.xlsx",
    "World",
    "self_energy_requirements_for_decom_solar_pv",
    {"NRG_PROTRA_I": ["PROTRA_PP_solar_urban_PV"]},
)

_ext_constant_share_energy_requirements_for_decomm_protra.add(
    "model_parameters/materials/materials.xlsx",
    "World",
    "self_energy_requirements_for_decom_CSP",
    {"NRG_PROTRA_I": ["PROTRA_PP_solar_CSP"]},
)


@component.add(
    name="SHARE_EV_BATTERIES_BEFORE_2015",
    units="DMNL",
    subscripts=["REGIONS_35_I", "EV_BATTERIES_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_share_ev_batteries_before_2015"},
)
def share_ev_batteries_before_2015():
    """
    Due to the lack of data at global level, we assume LMO dominated fully the market in all regions before 2015, and ffrom 2015 onwards we let the model allocate endogenously the EV batteries subtechnologies.
    """
    return _ext_constant_share_ev_batteries_before_2015()


_ext_constant_share_ev_batteries_before_2015 = ExtConstant(
    "model_parameters/energy/energy-transport.xlsx",
    "electrified_transport",
    "SHARE_EV_BATTERIES_BEFORE_2015",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "EV_BATTERIES_I": _subscript_dict["EV_BATTERIES_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "EV_BATTERIES_I": _subscript_dict["EV_BATTERIES_I"],
    },
    "_ext_constant_share_ev_batteries_before_2015",
)


@component.add(
    name="SHARE_OF_Cu_PRICE",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_share_of_cu_price"},
)
def share_of_cu_price():
    """
    This is a constant used to calculate 1%
    """
    return _ext_constant_share_of_cu_price()


_ext_constant_share_of_cu_price = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Copper",
    "SHARE_OF_Cu_PRICE*",
    {},
    _root,
    {},
    "_ext_constant_share_of_cu_price",
)


@component.add(
    name="SHARE_SELF_ELECTRICITY_CONSUMPTION_PROTRA",
    units="DMNL",
    subscripts=["NRG_PROTRA_I"],
    comp_type="Constant",
    comp_subtype="External, Normal",
    depends_on={
        "__external__": "_ext_constant_share_self_electricity_consumption_protra"
    },
)
def share_self_electricity_consumption_protra():
    """
    Self-electricity consumption from PROTRA.
    """
    value = xr.DataArray(
        np.nan, {"NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"]}, ["NRG_PROTRA_I"]
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[["PROTRA_PP_solar_CSP"]] = False
    except_subs.loc[["PROTRA_PP_wind_onshore"]] = False
    except_subs.loc[["PROTRA_PP_wind_offshore"]] = False
    except_subs.loc[_subscript_dict["PROTRA_PP_SOLAR_PV_I"]] = False
    value.values[except_subs.values] = 0
    def_subs = xr.zeros_like(value, dtype=bool)
    def_subs.loc[["PROTRA_PP_solar_CSP"]] = True
    def_subs.loc[["PROTRA_PP_wind_onshore"]] = True
    def_subs.loc[["PROTRA_PP_wind_offshore"]] = True
    def_subs.loc[["PROTRA_PP_solar_open_space_PV"]] = True
    def_subs.loc[["PROTRA_PP_solar_urban_PV"]] = True
    value.values[
        def_subs.values
    ] = _ext_constant_share_self_electricity_consumption_protra().values[
        def_subs.values
    ]
    return value


_ext_constant_share_self_electricity_consumption_protra = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "World",
    "self_electricity_consumption_solar_CSP",
    {"NRG_PROTRA_I": ["PROTRA_PP_solar_CSP"]},
    _root,
    {"NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"]},
    "_ext_constant_share_self_electricity_consumption_protra",
)

_ext_constant_share_self_electricity_consumption_protra.add(
    "model_parameters/materials/materials.xlsx",
    "World",
    "self_electricity_consumption_wind_onshore",
    {"NRG_PROTRA_I": ["PROTRA_PP_wind_onshore"]},
)

_ext_constant_share_self_electricity_consumption_protra.add(
    "model_parameters/materials/materials.xlsx",
    "World",
    "self_electricity_consumption_wind_offshore",
    {"NRG_PROTRA_I": ["PROTRA_PP_wind_offshore"]},
)

_ext_constant_share_self_electricity_consumption_protra.add(
    "model_parameters/materials/materials.xlsx",
    "World",
    "self_electricity_consumption_solar_pv",
    {"NRG_PROTRA_I": ["PROTRA_PP_solar_open_space_PV"]},
)

_ext_constant_share_self_electricity_consumption_protra.add(
    "model_parameters/materials/materials.xlsx",
    "World",
    "self_electricity_consumption_solar_pv",
    {"NRG_PROTRA_I": ["PROTRA_PP_solar_urban_PV"]},
)


@component.add(name="split_equation_Ni", comp_type="Constant", comp_subtype="Normal")
def split_equation_ni():
    return 0.15


@component.add(
    name="start_year_P_common_rr_minerals_alt_techn",
    units="Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"start_year_p_common_rr_minerals_alt_techn_w": 1},
)
def start_year_p_common_rr_minerals_alt_techn():
    """
    Start year of variation recycling rate of minerals for alternative technologies (RES elec & EV batteries).
    """
    return xr.DataArray(
        start_year_p_common_rr_minerals_alt_techn_w(),
        {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
        ["REGIONS_9_I"],
    )


@component.add(
    name="start_year_P_common_rr_minerals_alt_techn_W",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_start_year_p_common_rr_minerals_alt_techn_w"
    },
)
def start_year_p_common_rr_minerals_alt_techn_w():
    """
    Start year of variation recycling rate of minerals for alternative technologies (RES elec & EV batteries).
    """
    return _ext_constant_start_year_p_common_rr_minerals_alt_techn_w()


_ext_constant_start_year_p_common_rr_minerals_alt_techn_w = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "materials",
    "start_year_P_recycling_minerals_alt_technologies",
    {},
    _root,
    {},
    "_ext_constant_start_year_p_common_rr_minerals_alt_techn_w",
)


@component.add(
    name="start_year_P_common_rr_minerals_Rest",
    units="Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"start_year_p_common_rr_minerals_rest_w": 1},
)
def start_year_p_common_rr_minerals_rest():
    """
    Start year of variation recycling rate of minerals of the rest of the economy.
    """
    return xr.DataArray(
        start_year_p_common_rr_minerals_rest_w(),
        {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
        ["REGIONS_9_I"],
    )


@component.add(
    name="start_year_P_common_rr_minerals_Rest_W",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_start_year_p_common_rr_minerals_rest_w"},
)
def start_year_p_common_rr_minerals_rest_w():
    """
    Start year of variation recycling rate of minerals of the rest of the economy.
    """
    return _ext_constant_start_year_p_common_rr_minerals_rest_w()


_ext_constant_start_year_p_common_rr_minerals_rest_w = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "materials",
    "start_year_P_recycling_minerals_Rest",
    {},
    _root,
    {},
    "_ext_constant_start_year_p_common_rr_minerals_rest_w",
)


@component.add(
    name="start_year_P_rr_minerals_alt_techn",
    units="Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"start_year_p_rr_minerals_alt_techn_w": 1},
)
def start_year_p_rr_minerals_alt_techn():
    """
    Start year of variation recycling rate of minerals for alternative technologies (RES elec & EV batteries).
    """
    return xr.DataArray(
        start_year_p_rr_minerals_alt_techn_w(),
        {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
        ["REGIONS_9_I"],
    )


@component.add(
    name="start_year_P_rr_minerals_alt_techn_W",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_start_year_p_rr_minerals_alt_techn_w"},
)
def start_year_p_rr_minerals_alt_techn_w():
    """
    Start year of variation recycling rate of minerals for alternative technologies (RES elec & EV batteries).
    """
    return _ext_constant_start_year_p_rr_minerals_alt_techn_w()


_ext_constant_start_year_p_rr_minerals_alt_techn_w = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "materials",
    "Recycling_rates_by_mineral_starting_year",
    {},
    _root,
    {},
    "_ext_constant_start_year_p_rr_minerals_alt_techn_w",
)


@component.add(
    name="start_year_P_rr_minerals_Rest",
    units="Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"start_year_p_rr_minerals_rest_w": 1},
)
def start_year_p_rr_minerals_rest():
    """
    Start year of variation recycling rate of minerals for the rest of the economy.
    """
    return xr.DataArray(
        start_year_p_rr_minerals_rest_w(),
        {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
        ["REGIONS_9_I"],
    )


@component.add(
    name="start_year_P_rr_minerals_Rest_W",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_start_year_p_rr_minerals_rest_w"},
)
def start_year_p_rr_minerals_rest_w():
    """
    Start year of variation recycling rate of minerals for the rest of the economy.
    """
    return _ext_constant_start_year_p_rr_minerals_rest_w()


_ext_constant_start_year_p_rr_minerals_rest_w = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "materials",
    "Recycling_rates_by_mineral_starting_year",
    {},
    _root,
    {},
    "_ext_constant_start_year_p_rr_minerals_rest_w",
)


@component.add(
    name="TARGET_RR_ALTERNATIVE_TECHNOLOGIES_SP",
    units="DMNL",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"target_rr_alternative_technologies_sp_w": 1},
)
def target_rr_alternative_technologies_sp():
    return target_rr_alternative_technologies_sp_w().expand_dims(
        {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, 0
    )


@component.add(
    name="TARGET_RR_ALTERNATIVE_TECHNOLOGIES_SP_W",
    units="DMNL",
    subscripts=["MATERIALS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_target_rr_alternative_technologies_sp_w"
    },
)
def target_rr_alternative_technologies_sp_w():
    return _ext_constant_target_rr_alternative_technologies_sp_w()


_ext_constant_target_rr_alternative_technologies_sp_w = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "materials",
    "Recycling_rates_alternative_technologies_all_materials*",
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    _root,
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    "_ext_constant_target_rr_alternative_technologies_sp_w",
)


@component.add(
    name="TARGET_RR_REST_SP",
    units="DMNL",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"target_rr_rest_sp_w": 1},
)
def target_rr_rest_sp():
    """
    Rest_of_the_economy_current_rates
    """
    return target_rr_rest_sp_w().expand_dims(
        {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, 0
    )


@component.add(
    name="TARGET_RR_REST_SP_W",
    units="DMNL",
    subscripts=["MATERIALS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_target_rr_rest_sp_w"},
)
def target_rr_rest_sp_w():
    """
    Rest_of_the_economy_current_rates
    """
    return _ext_constant_target_rr_rest_sp_w()


_ext_constant_target_rr_rest_sp_w = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "materials",
    "Rest_of_the_economy_current_rates_all_materials*",
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    _root,
    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]},
    "_ext_constant_target_rr_rest_sp_w",
)


@component.add(
    name="target_year_P_rr_minerals_alt_techn",
    units="Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"target_year_p_rr_minerals_alt_techn_w": 1},
)
def target_year_p_rr_minerals_alt_techn():
    """
    Target year of variation recycling rate of minerals for alternative technologies (RES elec & EV batteries).
    """
    return xr.DataArray(
        target_year_p_rr_minerals_alt_techn_w(),
        {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
        ["REGIONS_9_I"],
    )


@component.add(
    name="target_year_P_rr_minerals_alt_techn_W",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_target_year_p_rr_minerals_alt_techn_w"},
)
def target_year_p_rr_minerals_alt_techn_w():
    """
    Target year of variation recycling rate of minerals for alternative technologies (RES elec & EV batteries).
    """
    return _ext_constant_target_year_p_rr_minerals_alt_techn_w()


_ext_constant_target_year_p_rr_minerals_alt_techn_w = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "materials",
    "Recycling_rates_by_mineral_target_year",
    {},
    _root,
    {},
    "_ext_constant_target_year_p_rr_minerals_alt_techn_w",
)


@component.add(
    name="target_year_P_rr_minerals_Rest",
    units="Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"target_year_p_rr_minerals_rest_w": 1},
)
def target_year_p_rr_minerals_rest():
    """
    Target year of variation recycling rate of minerals for the rest of the economy.
    """
    return xr.DataArray(
        target_year_p_rr_minerals_rest_w(),
        {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
        ["REGIONS_9_I"],
    )


@component.add(
    name="target_year_P_rr_minerals_Rest_W",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_target_year_p_rr_minerals_rest_w"},
)
def target_year_p_rr_minerals_rest_w():
    """
    Target year of variation recycling rate of minerals for the rest of the economy.
    """
    return _ext_constant_target_year_p_rr_minerals_rest_w()


_ext_constant_target_year_p_rr_minerals_rest_w = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "materials",
    "Recycling_rates_by_mineral_target_year",
    {},
    _root,
    {},
    "_ext_constant_target_year_p_rr_minerals_rest_w",
)


@component.add(
    name="TOTAL_LENGTH_RAIL_TRACKS_VS_LINES_HISTORIC",
    units="DMNL",
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_total_length_rail_tracks_vs_lines_historic",
        "__data__": "_ext_data_total_length_rail_tracks_vs_lines_historic",
        "time": 1,
    },
)
def total_length_rail_tracks_vs_lines_historic():
    """
    Total length of rails tracks in relation to historic lines length. -The estimation of the track length is modelled depending on two parameters (UIC, «Railway handbook 2013» and «UIC statistics», UIC, 2021): the ratio of total length of railway track vs length lines and the ratio of the length of railway lines vs the number of locomotives which for the sake of simplicity we maintain constant in the model in their estimated values for the base year 2015, at the values 1.5 and 3, respectively. The total track length is then estimated multiplying these parameters by the total number of trains which is an endogenous variable of the MEDEAS-W model depending on the demand of this type of transport.
    """
    return _ext_data_total_length_rail_tracks_vs_lines_historic(time())


_ext_data_total_length_rail_tracks_vs_lines_historic = ExtData(
    "model_parameters/materials/materials.xlsx",
    "World",
    "time_train",
    "TOTAL_LENGTH_RAIL_TRACKS_vs_LINES_HISTORIC",
    "interpolate",
    {},
    _root,
    {},
    "_ext_data_total_length_rail_tracks_vs_lines_historic",
)


@component.add(
    name='"UNIT_CONVERSION_MW/BATTERY"',
    units="MW/battery",
    comp_type="Constant",
    comp_subtype="Normal",
)
def unit_conversion_mwbattery():
    """
    Unit change: It has been established that each battery has a capacity of 60 kWh (as several models on the market at 2021) and 100 kW of power.
    """
    return 0.1


@component.add(
    name="VEHICLE_ELECTRIC_POWER",
    units="kW/battery",
    subscripts=["TRANSPORT_POWER_TRAIN_I", "BATTERY_VEHICLES_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_vehicle_electric_power"},
)
def vehicle_electric_power():
    return _ext_constant_vehicle_electric_power()


_ext_constant_vehicle_electric_power = ExtConstant(
    "model_parameters/energy/energy-transport.xlsx",
    "electrified_transport",
    "VEHICLE_ELECTRIC_POWER",
    {
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "BATTERY_VEHICLES_I": _subscript_dict["BATTERY_VEHICLES_I"],
    },
    _root,
    {
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "BATTERY_VEHICLES_I": _subscript_dict["BATTERY_VEHICLES_I"],
    },
    "_ext_constant_vehicle_electric_power",
)


@component.add(
    name="WATER_PER_Cu",
    units="m3/t",
    subscripts=["ORE_GRADES_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_water_per_cu"},
)
def water_per_cu():
    """
    It is noted that these values are the best values available for now but they could change substancially at any point in the future if better data will be available. The values based on table 2, in report by Mussey et. al from 1955. The parameters are estimated as in the Rich grade ore are estimated to require the min water estimates and the ultralowgrade is estimated to require the max reported water since the estimates reported are for 1955, the trace grade is based on own estimates and the grades in between are based on the given numbers. The table reports on: min water to be 0,4 gallons/pound = 3,34 m^3/ton average water to be 3,93 gallons/pound = 32,86 m^3/ton max water to be 58,62 gallons/pound = 489,21 m^3/ton therefore the rough estimates become the following: RG: 3,34 m3/ton HG: 32,86 m^3/ton LG: 50 m^3/ton ULG: 489,21 m^3/ton TRACE: 550 m^3/ton OG: 0 secondary: 50 m^3/ton recycling: 15 m^3/ton source: Mussey, O. D., Conklin, H. L., Durfor, C. N., Otts Jr., L. E., & Walling, F. B. (1955). Water requirements of selected industries. In Water Supply Paper. https://doi.org/10.3133/wsp1330
    """
    return _ext_constant_water_per_cu()


_ext_constant_water_per_cu = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Copper",
    "WATER_PER_Cu*",
    {"ORE_GRADES_I": _subscript_dict["ORE_GRADES_I"]},
    _root,
    {"ORE_GRADES_I": _subscript_dict["ORE_GRADES_I"]},
    "_ext_constant_water_per_cu",
)


@component.add(
    name="WATER_PER_Cu_RECYCLE",
    units="m3/t",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_water_per_cu_recycle"},
)
def water_per_cu_recycle():
    """
    This is own estimate. Source or base for the estimate ?
    """
    return _ext_constant_water_per_cu_recycle()


_ext_constant_water_per_cu_recycle = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Copper",
    "WATER_PER_Cu_RECYCLE*",
    {},
    _root,
    {},
    "_ext_constant_water_per_cu_recycle",
)


@component.add(
    name="WATER_PER_Cu_SECONDARY",
    units="m3/t",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_water_per_cu_secondary"},
)
def water_per_cu_secondary():
    """
    m3/ton is equivilent to saying Mm^3/Mt This is own estimate- Source ? or base of estimate ?
    """
    return _ext_constant_water_per_cu_secondary()


_ext_constant_water_per_cu_secondary = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Copper",
    "WATER_PER_Cu_SECONDARY*",
    {},
    _root,
    {},
    "_ext_constant_water_per_cu_secondary",
)


@component.add(
    name="WORLD_SHARE",
    units="TJ/Years",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_world_share"},
)
def world_share():
    """
    Data from figure 1 in (Lagos et at al, 2018). Data is for total energy concumption of Cu mining for chile, but chile is estimated to have 30% pruduction in the world, therefore we have multiplied with 3,3 Lagos, C., Carrasco, R., Soto, I., Fuertes, G., Alfaro, M., & Vargas, M. (2018). Predictive analysis of energy consumption in minining for making decisions. 2018 7th International Conference on Computers Communications and Control, ICCCC 2018 - Proceedings, 19, 270â€“275. https://doi.org/10.1109/ICCCC.2018.8390470
    """
    return _ext_constant_world_share()


_ext_constant_world_share = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "Copper",
    "WORLD_SHARE",
    {},
    _root,
    {},
    "_ext_constant_world_share",
)


@component.add(
    name="YEAR_FINAL_SC_SP",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_year_final_sc_sp"},
)
def year_final_sc_sp():
    """
    Target year of implementation of vehicles using Smart charging
    """
    return _ext_constant_year_final_sc_sp()


_ext_constant_year_final_sc_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "YEAR_FINAL_SC_SP",
    {},
    _root,
    {},
    "_ext_constant_year_final_sc_sp",
)


@component.add(
    name="YEAR_FINAL_V2G_SP",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_year_final_v2g_sp"},
)
def year_final_v2g_sp():
    """
    Target year of implementation of vehicles using V2G
    """
    return _ext_constant_year_final_v2g_sp()


_ext_constant_year_final_v2g_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "TARGET_YEAR_V2G_SP",
    {},
    _root,
    {},
    "_ext_constant_year_final_v2g_sp",
)


@component.add(
    name="YEAR_INITIAL_SC_SP",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_year_initial_sc_sp"},
)
def year_initial_sc_sp():
    """
    initial year of implementation of vehicles using smart charging
    """
    return _ext_constant_year_initial_sc_sp()


_ext_constant_year_initial_sc_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "YEAR_INITIAL_SC_SP",
    {},
    _root,
    {},
    "_ext_constant_year_initial_sc_sp",
)


@component.add(
    name="YEAR_INITIAL_V2G_SP",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_year_initial_v2g_sp"},
)
def year_initial_v2g_sp():
    """
    initial year of implementation of vehicles using V2G
    """
    return _ext_constant_year_initial_v2g_sp()


_ext_constant_year_initial_v2g_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "START_YEAR_V2G_SP",
    {},
    _root,
    {},
    "_ext_constant_year_initial_v2g_sp",
)
