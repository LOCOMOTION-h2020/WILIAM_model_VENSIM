"""
Module energy.exogenous_inputs
Translated using PySD version 3.10.0
"""


@component.add(
    name='"Activate_dem_elec_storage?"',
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_activate_dem_elec_storage"},
)
def activate_dem_elec_storage():
    """
    1. demand of electric storage activated 0. demand of electric storage NOT activated
    """
    return _ext_constant_activate_dem_elec_storage()


_ext_constant_activate_dem_elec_storage = ExtConstant(
    "model_parameters/energy/energy.xlsm",
    "World",
    "Activate_dem_elec_storage?",
    {},
    _root,
    {},
    "_ext_constant_activate_dem_elec_storage",
)


@component.add(
    name="bateries_ratio_2w_E",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_bateries_ratio_2w_e"},
)
def bateries_ratio_2w_e():
    """
    Ratio between the size of the electric 2 wheeler batteries and the standard 21,3KWh batteries, per vehicle
    """
    return _ext_constant_bateries_ratio_2w_e()


_ext_constant_bateries_ratio_2w_e = ExtConstant(
    "model_parameters/energy/energy.xlsm",
    "World",
    "bateries_2_wheels_elec",
    {},
    _root,
    {},
    "_ext_constant_bateries_ratio_2w_e",
)


@component.add(
    name="bateries_ratio_bus_E",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_bateries_ratio_bus_e"},
)
def bateries_ratio_bus_e():
    """
    Ratio between the size of the electric bus batteries and the standard 21,3KWh batteries, per vehicle
    """
    return _ext_constant_bateries_ratio_bus_e()


_ext_constant_bateries_ratio_bus_e = ExtConstant(
    "model_parameters/energy/energy.xlsm",
    "World",
    "bateries_bus_elec",
    {},
    _root,
    {},
    "_ext_constant_bateries_ratio_bus_e",
)


@component.add(
    name="bateries_ratio_ebikes",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_bateries_ratio_ebikes"},
)
def bateries_ratio_ebikes():
    """
    Ratio between the size of the electric bikes batteries and the standard 21,3KWh batteries, per vehicle
    """
    return _ext_constant_bateries_ratio_ebikes()


_ext_constant_bateries_ratio_ebikes = ExtConstant(
    "model_parameters/energy/energy.xlsm",
    "World",
    "ebikes_bateries_ratio",
    {},
    _root,
    {},
    "_ext_constant_bateries_ratio_ebikes",
)


@component.add(
    name="bateries_ratio_elec_LV",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_bateries_ratio_elec_lv"},
)
def bateries_ratio_elec_lv():
    """
    Ratio between the size of the electric LV batteries and the standard 21,3KWh batteries, per vehicle
    """
    return _ext_constant_bateries_ratio_elec_lv()


_ext_constant_bateries_ratio_elec_lv = ExtConstant(
    "model_parameters/energy/energy.xlsm",
    "World",
    "bateries_LV_elec",
    {},
    _root,
    {},
    "_ext_constant_bateries_ratio_elec_lv",
)


@component.add(
    name="bateries_ratio_hyb_bus",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_bateries_ratio_hyb_bus"},
)
def bateries_ratio_hyb_bus():
    """
    Ratio between the size of the hybrid bus batteries and the standard 21,3KWh batteries, per vehicle
    """
    return _ext_constant_bateries_ratio_hyb_bus()


_ext_constant_bateries_ratio_hyb_bus = ExtConstant(
    "model_parameters/energy/energy.xlsm",
    "World",
    "bateries_bus_hib",
    {},
    _root,
    {},
    "_ext_constant_bateries_ratio_hyb_bus",
)


@component.add(
    name="bateries_ratio_hyb_HV",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_bateries_ratio_hyb_hv"},
)
def bateries_ratio_hyb_hv():
    """
    Ratio between the size of the hybrid HV batteries and the standard 21,3KWh batteries, per vehicle
    """
    return _ext_constant_bateries_ratio_hyb_hv()


_ext_constant_bateries_ratio_hyb_hv = ExtConstant(
    "model_parameters/energy/energy.xlsm",
    "World",
    "bateries_HV_hyb",
    {},
    _root,
    {},
    "_ext_constant_bateries_ratio_hyb_hv",
)


@component.add(
    name="bateries_ratio_hyb_LV",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_bateries_ratio_hyb_lv"},
)
def bateries_ratio_hyb_lv():
    """
    Ratio between the size of the electric LV hybrid batteries and the standard 21,3KWh batteries, per vehicle
    """
    return _ext_constant_bateries_ratio_hyb_lv()


_ext_constant_bateries_ratio_hyb_lv = ExtConstant(
    "model_parameters/energy/energy.xlsm",
    "World",
    "bateries_LV_hyb",
    {},
    _root,
    {},
    "_ext_constant_bateries_ratio_hyb_lv",
)


@component.add(
    name="BATTERIES_PER_EV_VEHICLE",
    units="batteries/vehicle",
    comp_type="Constant",
    comp_subtype="Normal",
)
def batteries_per_ev_vehicle():
    return 1


@component.add(
    name="CF_EV_batteries_for_Transp",
    units="DMNL",
    subscripts=["EV_BATTERIES_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_cf_ev_batteries_for_transp"},
)
def cf_ev_batteries_for_transp():
    """
    CF of EV batteries for Transportation use.
    """
    return _ext_constant_cf_ev_batteries_for_transp()


_ext_constant_cf_ev_batteries_for_transp = ExtConstant(
    "model_parameters/energy/energy.xlsm",
    "World",
    "CF_EV_batteries",
    {"EV_BATTERIES_I": ["LMO"]},
    _root,
    {"EV_BATTERIES_I": _subscript_dict["EV_BATTERIES_I"]},
    "_ext_constant_cf_ev_batteries_for_transp",
)

_ext_constant_cf_ev_batteries_for_transp.add(
    "model_parameters/energy/energy.xlsm",
    "World",
    "CF_EV_batteries",
    {"EV_BATTERIES_I": ["NMC622"]},
)

_ext_constant_cf_ev_batteries_for_transp.add(
    "model_parameters/energy/energy.xlsm",
    "World",
    "CF_EV_batteries",
    {"EV_BATTERIES_I": ["NMC811"]},
)

_ext_constant_cf_ev_batteries_for_transp.add(
    "model_parameters/energy/energy.xlsm",
    "World",
    "CF_EV_batteries",
    {"EV_BATTERIES_I": ["NCA"]},
)

_ext_constant_cf_ev_batteries_for_transp.add(
    "model_parameters/energy/energy.xlsm",
    "World",
    "CF_EV_batteries",
    {"EV_BATTERIES_I": ["LFP"]},
)


@component.add(
    name="cumulated_coal_extraction_to_2005_W",
    units="EJ",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_cumulated_coal_extraction_to_2005_w"},
)
def cumulated_coal_extraction_to_2005_w():
    """
    Cumulated coal extraction to 2005 (Mohr et al., 2015).
    """
    return _ext_constant_cumulated_coal_extraction_to_2005_w()


_ext_constant_cumulated_coal_extraction_to_2005_w = ExtConstant(
    "model_parameters/energy/energy.xlsm",
    "World",
    "cumulated_coal_extraction_to_2005",
    {},
    _root,
    {},
    "_ext_constant_cumulated_coal_extraction_to_2005_w",
)


@component.add(
    name="cumulated_conv_oil_extraction_to_2005_W",
    units="EJ",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_cumulated_conv_oil_extraction_to_2005_w"
    },
)
def cumulated_conv_oil_extraction_to_2005_w():
    """
    Cumulated conventional oil extraction to 2005 (Mohr et al., 2015).
    """
    return _ext_constant_cumulated_conv_oil_extraction_to_2005_w()


_ext_constant_cumulated_conv_oil_extraction_to_2005_w = ExtConstant(
    "model_parameters/energy/energy.xlsm",
    "World",
    "cumulated_conv_oil_extraction_to_2005",
    {},
    _root,
    {},
    "_ext_constant_cumulated_conv_oil_extraction_to_2005_w",
)


@component.add(
    name="cumulated_unconv_oil_extraction_to_2005_W",
    units="EJ",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_cumulated_unconv_oil_extraction_to_2005_w"
    },
)
def cumulated_unconv_oil_extraction_to_2005_w():
    """
    Cumulated unconventional oil extraction to 2005 (Mohr et al., 2015).
    """
    return _ext_constant_cumulated_unconv_oil_extraction_to_2005_w()


_ext_constant_cumulated_unconv_oil_extraction_to_2005_w = ExtConstant(
    "model_parameters/energy/energy.xlsm",
    "World",
    "cumulated_unconv_oil_extraction_to_2005",
    {},
    _root,
    {},
    "_ext_constant_cumulated_unconv_oil_extraction_to_2005_w",
)


@component.add(
    name="ebike_average_price",
    units="dollars",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_ebike_average_price"},
)
def ebike_average_price():
    """
    Avarege price of a ebike vehicle
    """
    return _ext_constant_ebike_average_price()


_ext_constant_ebike_average_price = ExtConstant(
    "model_parameters/energy/energy.xlsm",
    "World",
    "ebike_average_price",
    {},
    _root,
    {},
    "_ext_constant_ebike_average_price",
)


@component.add(
    name="ENERGY_VARIABILITY_LINEAR_REGRESSION_COEFFICIENTS",
    units="DMNL",
    subscripts=["OUTPUTS_NGR_VARIABILITY_I", "PREDICTORS_NGR_VARIABILITY_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_energy_variability_linear_regression_coefficients"
    },
)
def energy_variability_linear_regression_coefficients():
    """
    Coefficients of the multiple linear regression models
    """
    return _ext_constant_energy_variability_linear_regression_coefficients()


_ext_constant_energy_variability_linear_regression_coefficients = ExtConstant(
    "model_parameters/energy/intermittency_coefficients.xlsx",
    "COEFFICIENTS",
    "COEFFICIENTS_LINEAR",
    {
        "OUTPUTS_NGR_VARIABILITY_I": _subscript_dict["OUTPUTS_NGR_VARIABILITY_I"],
        "PREDICTORS_NGR_VARIABILITY_I": _subscript_dict["PREDICTORS_NGR_VARIABILITY_I"],
    },
    _root,
    {
        "OUTPUTS_NGR_VARIABILITY_I": _subscript_dict["OUTPUTS_NGR_VARIABILITY_I"],
        "PREDICTORS_NGR_VARIABILITY_I": _subscript_dict["PREDICTORS_NGR_VARIABILITY_I"],
    },
    "_ext_constant_energy_variability_linear_regression_coefficients",
)


@component.add(
    name="ENERGY_VARIABILITY_LINEAR_REGRESSION_INTERCEPT",
    units="DMNL",
    subscripts=["OUTPUTS_NGR_VARIABILITY_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_energy_variability_linear_regression_intercept"
    },
)
def energy_variability_linear_regression_intercept():
    """
    Independent term of the multiple logistic regression equations in the energy variability submodule
    """
    return _ext_constant_energy_variability_linear_regression_intercept()


_ext_constant_energy_variability_linear_regression_intercept = ExtConstant(
    "model_parameters/energy/intermittency_coefficients.xlsx",
    "COEFFICIENTS",
    "INTERCEPT_LINEAR*",
    {"OUTPUTS_NGR_VARIABILITY_I": _subscript_dict["OUTPUTS_NGR_VARIABILITY_I"]},
    _root,
    {"OUTPUTS_NGR_VARIABILITY_I": _subscript_dict["OUTPUTS_NGR_VARIABILITY_I"]},
    "_ext_constant_energy_variability_linear_regression_intercept",
)


@component.add(
    name="ENERGY_VARIABILITY_LOGISTIC_REGRESSION_COEFFICIENTS",
    units="DMNL",
    subscripts=["OUTPUTS_NGR_VARIABILITY_I", "PREDICTORS_NGR_VARIABILITY_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_energy_variability_logistic_regression_coefficients"
    },
)
def energy_variability_logistic_regression_coefficients():
    """
    Coefficients of the multiple logistic regression models
    """
    return _ext_constant_energy_variability_logistic_regression_coefficients()


_ext_constant_energy_variability_logistic_regression_coefficients = ExtConstant(
    "model_parameters/energy/intermittency_coefficients.xlsx",
    "COEFFICIENTS",
    "COEFFICIENTS_LOGISTIC",
    {
        "OUTPUTS_NGR_VARIABILITY_I": _subscript_dict["OUTPUTS_NGR_VARIABILITY_I"],
        "PREDICTORS_NGR_VARIABILITY_I": _subscript_dict["PREDICTORS_NGR_VARIABILITY_I"],
    },
    _root,
    {
        "OUTPUTS_NGR_VARIABILITY_I": _subscript_dict["OUTPUTS_NGR_VARIABILITY_I"],
        "PREDICTORS_NGR_VARIABILITY_I": _subscript_dict["PREDICTORS_NGR_VARIABILITY_I"],
    },
    "_ext_constant_energy_variability_logistic_regression_coefficients",
)


@component.add(
    name="ENERGY_VARIABILITY_LOGISTIC_REGRESSION_INTERCEPT",
    units="DMNL",
    subscripts=["OUTPUTS_NGR_VARIABILITY_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_energy_variability_logistic_regression_intercept"
    },
)
def energy_variability_logistic_regression_intercept():
    """
    Independent term of the multiple logistic regression equations in the energy variability submodule
    """
    return _ext_constant_energy_variability_logistic_regression_intercept()


_ext_constant_energy_variability_logistic_regression_intercept = ExtConstant(
    "model_parameters/energy/intermittency_coefficients.xlsx",
    "COEFFICIENTS",
    "INTERCEPT_LOGISTIC*",
    {"OUTPUTS_NGR_VARIABILITY_I": _subscript_dict["OUTPUTS_NGR_VARIABILITY_I"]},
    _root,
    {"OUTPUTS_NGR_VARIABILITY_I": _subscript_dict["OUTPUTS_NGR_VARIABILITY_I"]},
    "_ext_constant_energy_variability_logistic_regression_intercept",
)


@component.add(
    name="EROIst_ini_hydro_2015",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_eroist_ini_hydro_2015"},
)
def eroist_ini_hydro_2015():
    return _ext_constant_eroist_ini_hydro_2015()


_ext_constant_eroist_ini_hydro_2015 = ExtConstant(
    "model_parameters/energy/energy.xlsm",
    "World",
    "EROIst_ini_hydro_2015",
    {},
    _root,
    {},
    "_ext_constant_eroist_ini_hydro_2015",
)


@component.add(
    name="EXO_TOTAL_TRANSPORT_DEMAND_BY_REGION_AND_TYPE_OF_HH",
    units="persons*km",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_exo_total_transport_demand_by_region_and_type_of_hh"
    },
)
def exo_total_transport_demand_by_region_and_type_of_hh():
    return _ext_constant_exo_total_transport_demand_by_region_and_type_of_hh()


_ext_constant_exo_total_transport_demand_by_region_and_type_of_hh = ExtConstant(
    "model_parameters/energy/energy-transport.xlsx",
    "TRANSPORT_DEMAND",
    "TOTAL_TRANSPORT_DEMAND_BY_REGION_AND_TYPE_OF_HH",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
    "_ext_constant_exo_total_transport_demand_by_region_and_type_of_hh",
)


@component.add(
    name="FACTOR_BACKUP_POWER_SYSTEM",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_factor_backup_power_system"},
)
def factor_backup_power_system():
    """
    Factor of overcapacity to represent the reserves in the power system (related to the stability and reliability of the power grid)
    """
    return _ext_constant_factor_backup_power_system()


_ext_constant_factor_backup_power_system = ExtConstant(
    "model_parameters/energy/energy.xlsm",
    "Common",
    "FACTOR_BACKUP_POWER_SYSTEM",
    {},
    _root,
    {},
    "_ext_constant_factor_backup_power_system",
)


@component.add(
    name="FINAL_ENERGY_CONSUMPTION_INITIAL",
    units="MJ/(km*vehicle)",
    subscripts=[
        "REGIONS_35_I",
        "TRANSPORT_POWER_TRAIN_I",
        "PASSENGERS_TRANSPORT_MODE_I",
    ],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_final_energy_consumption_initial"},
)
def final_energy_consumption_initial():
    """
    Energy vehicle consumption by region, power train and transport mode in MJ/(vehicle*km)
    """
    return _ext_constant_final_energy_consumption_initial()


_ext_constant_final_energy_consumption_initial = ExtConstant(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "FINAL_ENERGY_CONSUMPTION_AUSTRIA",
    {
        "REGIONS_35_I": ["AUSTRIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
    "_ext_constant_final_energy_consumption_initial",
)

_ext_constant_final_energy_consumption_initial.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "FINAL_ENERGY_CONSUMPTION_BELGIUM",
    {
        "REGIONS_35_I": ["BELGIUM"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_final_energy_consumption_initial.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "FINAL_ENERGY_CONSUMPTION_BULGARIA",
    {
        "REGIONS_35_I": ["BULGARIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_final_energy_consumption_initial.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "FINAL_ENERGY_CONSUMPTION_CROATIA",
    {
        "REGIONS_35_I": ["CROATIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_final_energy_consumption_initial.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "FINAL_ENERGY_CONSUMPTION_CYPRUS",
    {
        "REGIONS_35_I": ["CYPRUS"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_final_energy_consumption_initial.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "FINAL_ENERGY_CONSUMPTION_CZECH_REPUBLIC",
    {
        "REGIONS_35_I": ["CZECH_REPUBLIC"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_final_energy_consumption_initial.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "FINAL_ENERGY_CONSUMPTION_DENMARK",
    {
        "REGIONS_35_I": ["DENMARK"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_final_energy_consumption_initial.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "FINAL_ENERGY_CONSUMPTION_ESTONIA",
    {
        "REGIONS_35_I": ["ESTONIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_final_energy_consumption_initial.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "FINAL_ENERGY_CONSUMPTION_FINLAND",
    {
        "REGIONS_35_I": ["FINLAND"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_final_energy_consumption_initial.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "FINAL_ENERGY_CONSUMPTION_FRANCE",
    {
        "REGIONS_35_I": ["FRANCE"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_final_energy_consumption_initial.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "FINAL_ENERGY_CONSUMPTION_GERMANY",
    {
        "REGIONS_35_I": ["GERMANY"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_final_energy_consumption_initial.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "FINAL_ENERGY_CONSUMPTION_GREECE",
    {
        "REGIONS_35_I": ["GREECE"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_final_energy_consumption_initial.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "FINAL_ENERGY_CONSUMPTION_HUNGARY",
    {
        "REGIONS_35_I": ["HUNGARY"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_final_energy_consumption_initial.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "FINAL_ENERGY_CONSUMPTION_IRELAND",
    {
        "REGIONS_35_I": ["IRELAND"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_final_energy_consumption_initial.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "FINAL_ENERGY_CONSUMPTION_ITALY",
    {
        "REGIONS_35_I": ["ITALY"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_final_energy_consumption_initial.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "FINAL_ENERGY_CONSUMPTION_LATVIA",
    {
        "REGIONS_35_I": ["LATVIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_final_energy_consumption_initial.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "FINAL_ENERGY_CONSUMPTION_LITHUANIA",
    {
        "REGIONS_35_I": ["LITHUANIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_final_energy_consumption_initial.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "FINAL_ENERGY_CONSUMPTION_LUXEMBOURG",
    {
        "REGIONS_35_I": ["LUXEMBOURG"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_final_energy_consumption_initial.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "FINAL_ENERGY_CONSUMPTION_MALTA",
    {
        "REGIONS_35_I": ["MALTA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_final_energy_consumption_initial.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "FINAL_ENERGY_CONSUMPTION_NETHERLANDS",
    {
        "REGIONS_35_I": ["NETHERLANDS"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_final_energy_consumption_initial.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "FINAL_ENERGY_CONSUMPTION_POLAND",
    {
        "REGIONS_35_I": ["POLAND"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_final_energy_consumption_initial.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "FINAL_ENERGY_CONSUMPTION_PORTUGAL",
    {
        "REGIONS_35_I": ["PORTUGAL"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_final_energy_consumption_initial.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "FINAL_ENERGY_CONSUMPTION_ROMANIA",
    {
        "REGIONS_35_I": ["ROMANIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_final_energy_consumption_initial.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "FINAL_ENERGY_CONSUMPTION_SLOVAKIA",
    {
        "REGIONS_35_I": ["SLOVAKIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_final_energy_consumption_initial.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "FINAL_ENERGY_CONSUMPTION_SLOVENIA",
    {
        "REGIONS_35_I": ["SLOVENIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_final_energy_consumption_initial.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "FINAL_ENERGY_CONSUMPTION_SPAIN",
    {
        "REGIONS_35_I": ["SPAIN"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_final_energy_consumption_initial.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "FINAL_ENERGY_CONSUMPTION_SWEDEN",
    {
        "REGIONS_35_I": ["SWEDEN"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_final_energy_consumption_initial.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "FINAL_ENERGY_CONSUMPTION_UK",
    {
        "REGIONS_35_I": ["UK"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_final_energy_consumption_initial.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "FINAL_ENERGY_CONSUMPTION_CHINA",
    {
        "REGIONS_35_I": ["CHINA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_final_energy_consumption_initial.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "FINAL_ENERGY_CONSUMPTION_EASOC",
    {
        "REGIONS_35_I": ["EASOC"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_final_energy_consumption_initial.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "FINAL_ENERGY_CONSUMPTION_INDIA",
    {
        "REGIONS_35_I": ["INDIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_final_energy_consumption_initial.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "FINAL_ENERGY_CONSUMPTION_LATAM",
    {
        "REGIONS_35_I": ["LATAM"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_final_energy_consumption_initial.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "FINAL_ENERGY_CONSUMPTION_RUSSIA",
    {
        "REGIONS_35_I": ["RUSSIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_final_energy_consumption_initial.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "FINAL_ENERGY_CONSUMPTION_USMCA",
    {
        "REGIONS_35_I": ["USMCA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_final_energy_consumption_initial.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "FINAL_ENERGY_CONSUMPTION_LROW",
    {
        "REGIONS_35_I": ["LROW"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)


@component.add(
    name="HISTORIC_CO2_EMISSIONS_ENERGY_AND_WASTE",
    units="Mt/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_historic_co2_emissions_energy_and_waste",
        "__data__": "_ext_data_historic_co2_emissions_energy_and_waste",
        "time": 1,
    },
)
def historic_co2_emissions_energy_and_waste():
    """
    Historic CO2 emissions from energy and waste (IPCC categories).
    """
    return _ext_data_historic_co2_emissions_energy_and_waste(time())


_ext_data_historic_co2_emissions_energy_and_waste = ExtData(
    "model_parameters/energy/energy-emission_factors.xlsx",
    "historic_GHG_emissions",
    "historic_time_index",
    "HISTORIC_CO2_EMISSIONS_FROM_ENERGY_AND_WASTE",
    "interpolate",
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    _root,
    {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
    "_ext_data_historic_co2_emissions_energy_and_waste",
)


@component.add(
    name="Historic_coal_extraction",
    units="EJ/Year",
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_historic_coal_extraction",
        "__data__": "_ext_data_historic_coal_extraction",
        "time": 1,
    },
)
def historic_coal_extraction():
    """
    "Memo: Coal, peat and oil shale" PES 1990-2014 (IEA Balances).
    """
    return _ext_data_historic_coal_extraction(time())


_ext_data_historic_coal_extraction = ExtData(
    "model_parameters/energy/energy.xlsm",
    "World",
    "time_index",
    "Historic_coal_extraction",
    "interpolate",
    {},
    _root,
    {},
    "_ext_data_historic_coal_extraction",
)


@component.add(
    name="Historic_crude_oil_extraction",
    units="EJ/Year",
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_historic_crude_oil_extraction",
        "__data__": "_ext_data_historic_crude_oil_extraction",
        "time": 1,
    },
)
def historic_crude_oil_extraction():
    """
    "Crude oil" extraction 1990-2014 (IEA Balances).
    """
    return _ext_data_historic_crude_oil_extraction(time())


_ext_data_historic_crude_oil_extraction = ExtData(
    "model_parameters/energy/energy.xlsm",
    "World",
    "time_index",
    "Historic_crude_oil_extraction",
    "interpolate",
    {},
    _root,
    {},
    "_ext_data_historic_crude_oil_extraction",
)


@component.add(
    name="Historic_electricity_consumption",
    units="TWh/Year",
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_historic_electricity_consumption",
        "__data__": "_ext_data_historic_electricity_consumption",
        "time": 1,
    },
)
def historic_electricity_consumption():
    """
    Historic electricity consumption 1990-2014 from US EIA database.
    """
    return _ext_data_historic_electricity_consumption(time())


_ext_data_historic_electricity_consumption = ExtData(
    "model_parameters/energy/energy.xlsm",
    "World",
    "time_index",
    "Historic_electricity_consumption",
    "interpolate",
    {},
    _root,
    {},
    "_ext_data_historic_electricity_consumption",
)


@component.add(
    name="Historic_liquids_extraction",
    units="EJ/Year",
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_historic_liquids_extraction",
        "__data__": "_ext_data_historic_liquids_extraction",
        "time": 1,
    },
)
def historic_liquids_extraction():
    """
    Memo: Primary and secondary oil (Liquids) 1990-2014 from IEA Balances.
    """
    return _ext_data_historic_liquids_extraction(time())


_ext_data_historic_liquids_extraction = ExtData(
    "model_parameters/energy/energy.xlsm",
    "World",
    "time_index",
    "Historic_liquids_extraction",
    "interpolate",
    {},
    _root,
    {},
    "_ext_data_historic_liquids_extraction",
)


@component.add(
    name="Historic_natural_gas_extraction",
    units="EJ/Year",
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_historic_natural_gas_extraction",
        "__data__": "_ext_data_historic_natural_gas_extraction",
        "time": 1,
    },
)
def historic_natural_gas_extraction():
    """
    "Natural gas" PES 1990-2014 from IEA Balances.
    """
    return _ext_data_historic_natural_gas_extraction(time())


_ext_data_historic_natural_gas_extraction = ExtData(
    "model_parameters/energy/energy.xlsm",
    "World",
    "time_index",
    "Historic_natural_gas_extraction",
    "interpolate",
    {},
    _root,
    {},
    "_ext_data_historic_natural_gas_extraction",
)


@component.add(
    name="Historic_total_RES_extraction",
    units="EJ/Year",
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_historic_total_res_extraction",
        "__data__": "_ext_data_historic_total_res_extraction",
        "time": 1,
    },
)
def historic_total_res_extraction():
    """
    "Memo: Renewables" PES 1990-2014 from IEA Balances.
    """
    return _ext_data_historic_total_res_extraction(time())


_ext_data_historic_total_res_extraction = ExtData(
    "model_parameters/energy/energy.xlsm",
    "World",
    "time_index",
    "Historic_total_RES_extraction",
    "interpolate",
    {},
    _root,
    {},
    "_ext_data_historic_total_res_extraction",
)


@component.add(
    name="Historic_TPES",
    units="EJ/Year",
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_historic_tpes",
        "__data__": "_ext_data_historic_tpes",
        "time": 1,
    },
)
def historic_tpes():
    """
    TPES 1990-2014 (IEA Balances).
    """
    return _ext_data_historic_tpes(time())


_ext_data_historic_tpes = ExtData(
    "model_parameters/energy/energy.xlsm",
    "World",
    "time_index",
    "Historic_TPES",
    "interpolate",
    {},
    _root,
    {},
    "_ext_data_historic_tpes",
)


@component.add(
    name="HISTORICAL_ENERGY_INTENSITIES_TOP_DOWN_BY_SECTOR_AND_FE",
    units="TJ/million$",
    subscripts=["REGIONS_35_I", "SECTORS_I", "NRG_FE_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe"
    },
)
def historical_energy_intensities_top_down_by_sector_and_fe():
    """
    Initial final energy intensities by sector and final energy obtained from EXIOBASE only for year 2015
    """
    return _ext_constant_historical_energy_intensities_top_down_by_sector_and_fe()


_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe = ExtConstant(
    "model_parameters/energy/energy-end_use.xlsx",
    "Energy_intensities_by_sector",
    "AUSTRIA_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS_35_I": ["AUSTRIA"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
    "_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe",
)

_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use.xlsx",
    "Energy_intensities_by_sector",
    "BELGIUM_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS_35_I": ["BELGIUM"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
)

_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use.xlsx",
    "Energy_intensities_by_sector",
    "BULGARIA_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS_35_I": ["BULGARIA"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
)

_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use.xlsx",
    "Energy_intensities_by_sector",
    "CROATIA_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS_35_I": ["CROATIA"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
)

_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use.xlsx",
    "Energy_intensities_by_sector",
    "CYPRUS_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS_35_I": ["CYPRUS"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
)

_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use.xlsx",
    "Energy_intensities_by_sector",
    "CZECH_REPUBLIC_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS_35_I": ["CZECH_REPUBLIC"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
)

_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use.xlsx",
    "Energy_intensities_by_sector",
    "DENMARK_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS_35_I": ["DENMARK"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
)

_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use.xlsx",
    "Energy_intensities_by_sector",
    "ESTONIA_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS_35_I": ["ESTONIA"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
)

_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use.xlsx",
    "Energy_intensities_by_sector",
    "FINLAND_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS_35_I": ["FINLAND"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
)

_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use.xlsx",
    "Energy_intensities_by_sector",
    "FRANCE_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS_35_I": ["FRANCE"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
)

_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use.xlsx",
    "Energy_intensities_by_sector",
    "GERMANY_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS_35_I": ["GERMANY"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
)

_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use.xlsx",
    "Energy_intensities_by_sector",
    "GREECE_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS_35_I": ["GREECE"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
)

_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use.xlsx",
    "Energy_intensities_by_sector",
    "HUNGARY_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS_35_I": ["HUNGARY"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
)

_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use.xlsx",
    "Energy_intensities_by_sector",
    "IRELAND_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS_35_I": ["IRELAND"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
)

_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use.xlsx",
    "Energy_intensities_by_sector",
    "ITALY_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS_35_I": ["ITALY"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
)

_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use.xlsx",
    "Energy_intensities_by_sector",
    "LATVIA_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS_35_I": ["LATVIA"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
)

_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use.xlsx",
    "Energy_intensities_by_sector",
    "LITHUANIA_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS_35_I": ["LITHUANIA"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
)

_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use.xlsx",
    "Energy_intensities_by_sector",
    "LUXEMBOURG_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS_35_I": ["LUXEMBOURG"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
)

_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use.xlsx",
    "Energy_intensities_by_sector",
    "MALTA_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS_35_I": ["MALTA"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
)

_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use.xlsx",
    "Energy_intensities_by_sector",
    "NETHERLANDS_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS_35_I": ["NETHERLANDS"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
)

_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use.xlsx",
    "Energy_intensities_by_sector",
    "POLAND_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS_35_I": ["POLAND"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
)

_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use.xlsx",
    "Energy_intensities_by_sector",
    "PORTUGAL_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS_35_I": ["PORTUGAL"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
)

_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use.xlsx",
    "Energy_intensities_by_sector",
    "ROMANIA_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS_35_I": ["ROMANIA"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
)

_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use.xlsx",
    "Energy_intensities_by_sector",
    "SLOVAKIA_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS_35_I": ["SLOVAKIA"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
)

_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use.xlsx",
    "Energy_intensities_by_sector",
    "SLOVENIA_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS_35_I": ["SLOVENIA"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
)

_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use.xlsx",
    "Energy_intensities_by_sector",
    "SPAIN_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS_35_I": ["SPAIN"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
)

_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use.xlsx",
    "Energy_intensities_by_sector",
    "SWEDEN_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS_35_I": ["SWEDEN"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
)

_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use.xlsx",
    "Energy_intensities_by_sector",
    "UK_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS_35_I": ["UK"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
)

_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use.xlsx",
    "Energy_intensities_by_sector",
    "CHINA_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS_35_I": ["CHINA"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
)

_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use.xlsx",
    "Energy_intensities_by_sector",
    "EASOC_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS_35_I": ["EASOC"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
)

_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use.xlsx",
    "Energy_intensities_by_sector",
    "INDIA_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS_35_I": ["INDIA"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
)

_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use.xlsx",
    "Energy_intensities_by_sector",
    "LATAM_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS_35_I": ["LATAM"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
)

_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use.xlsx",
    "Energy_intensities_by_sector",
    "RUSSIA_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS_35_I": ["RUSSIA"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
)

_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use.xlsx",
    "Energy_intensities_by_sector",
    "USMCA_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS_35_I": ["USMCA"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
)

_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use.xlsx",
    "Energy_intensities_by_sector",
    "LROW_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS_35_I": ["LROW"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
)


@component.add(
    name="HISTORICAL_NON_ENERGY_USE_INTENSITIES_BY_SECTOR_AND_FE",
    units="TJ/million$",
    subscripts=["REGIONS_35_I", "SECTORS_I", "NRG_FE_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe"
    },
)
def historical_non_energy_use_intensities_by_sector_and_fe():
    """
    Energy intensities of non energy sectors obtained from EXIOBASE for 2015
    """
    return _ext_constant_historical_non_energy_use_intensities_by_sector_and_fe()


_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe = ExtConstant(
    "model_parameters/energy/energy-end_use.xlsx",
    "Non-energy-use_intensities_by_s",
    "AUSTRIA_NON_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS_35_I": ["AUSTRIA"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
    "_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe",
)

_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use.xlsx",
    "Non-energy-use_intensities_by_s",
    "BELGIUM_NON_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS_35_I": ["BELGIUM"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
)

_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use.xlsx",
    "Non-energy-use_intensities_by_s",
    "BULGARIA_NON_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS_35_I": ["BULGARIA"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
)

_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use.xlsx",
    "Non-energy-use_intensities_by_s",
    "CROATIA_NON_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS_35_I": ["CROATIA"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
)

_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use.xlsx",
    "Non-energy-use_intensities_by_s",
    "CYPRUS_NON_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS_35_I": ["CYPRUS"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
)

_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use.xlsx",
    "Non-energy-use_intensities_by_s",
    "CZECH_REPUBLIC_NON_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS_35_I": ["CZECH_REPUBLIC"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
)

_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use.xlsx",
    "Non-energy-use_intensities_by_s",
    "DENMARK_NON_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS_35_I": ["DENMARK"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
)

_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use.xlsx",
    "Non-energy-use_intensities_by_s",
    "ESTONIA_NON_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS_35_I": ["ESTONIA"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
)

_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use.xlsx",
    "Non-energy-use_intensities_by_s",
    "FINLAND_NON_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS_35_I": ["FINLAND"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
)

_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use.xlsx",
    "Non-energy-use_intensities_by_s",
    "FRANCE_NON_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS_35_I": ["FRANCE"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
)

_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use.xlsx",
    "Non-energy-use_intensities_by_s",
    "GERMANY_NON_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS_35_I": ["GERMANY"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
)

_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use.xlsx",
    "Non-energy-use_intensities_by_s",
    "GREECE_NON_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS_35_I": ["GREECE"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
)

_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use.xlsx",
    "Non-energy-use_intensities_by_s",
    "HUNGARY_NON_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS_35_I": ["HUNGARY"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
)

_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use.xlsx",
    "Non-energy-use_intensities_by_s",
    "IRELAND_NON_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS_35_I": ["IRELAND"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
)

_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use.xlsx",
    "Non-energy-use_intensities_by_s",
    "ITALY_NON_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS_35_I": ["ITALY"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
)

_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use.xlsx",
    "Non-energy-use_intensities_by_s",
    "LATVIA_NON_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS_35_I": ["LATVIA"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
)

_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use.xlsx",
    "Non-energy-use_intensities_by_s",
    "LITHUANIA_NON_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS_35_I": ["LITHUANIA"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
)

_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use.xlsx",
    "Non-energy-use_intensities_by_s",
    "LUXEMBOURG_NON_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS_35_I": ["LUXEMBOURG"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
)

_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use.xlsx",
    "Non-energy-use_intensities_by_s",
    "MALTA_NON_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS_35_I": ["MALTA"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
)

_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use.xlsx",
    "Non-energy-use_intensities_by_s",
    "NETHERLANDS_NON_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS_35_I": ["NETHERLANDS"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
)

_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use.xlsx",
    "Non-energy-use_intensities_by_s",
    "POLAND_NON_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS_35_I": ["POLAND"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
)

_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use.xlsx",
    "Non-energy-use_intensities_by_s",
    "PORTUGAL_NON_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS_35_I": ["PORTUGAL"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
)

_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use.xlsx",
    "Non-energy-use_intensities_by_s",
    "ROMANIA_NON_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS_35_I": ["ROMANIA"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
)

_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use.xlsx",
    "Non-energy-use_intensities_by_s",
    "SLOVAKIA_NON_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS_35_I": ["SLOVAKIA"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
)

_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use.xlsx",
    "Non-energy-use_intensities_by_s",
    "SLOVENIA_NON_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS_35_I": ["SLOVENIA"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
)

_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use.xlsx",
    "Non-energy-use_intensities_by_s",
    "SPAIN_NON_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS_35_I": ["SPAIN"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
)

_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use.xlsx",
    "Non-energy-use_intensities_by_s",
    "SWEDEN_NON_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS_35_I": ["SWEDEN"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
)

_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use.xlsx",
    "Non-energy-use_intensities_by_s",
    "UK_NON_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS_35_I": ["UK"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
)

_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use.xlsx",
    "Non-energy-use_intensities_by_s",
    "CHINA_NON_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS_35_I": ["CHINA"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
)

_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use.xlsx",
    "Non-energy-use_intensities_by_s",
    "EASOC_NON_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS_35_I": ["EASOC"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
)

_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use.xlsx",
    "Non-energy-use_intensities_by_s",
    "INDIA_NON_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS_35_I": ["INDIA"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
)

_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use.xlsx",
    "Non-energy-use_intensities_by_s",
    "LATAM_NON_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS_35_I": ["LATAM"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
)

_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use.xlsx",
    "Non-energy-use_intensities_by_s",
    "RUSSIA_NON_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS_35_I": ["RUSSIA"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
)

_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use.xlsx",
    "Non-energy-use_intensities_by_s",
    "USMCA_NON_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS_35_I": ["USMCA"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
)

_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use.xlsx",
    "Non-energy-use_intensities_by_s",
    "LROW_NON_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS_35_I": ["LROW"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
)


@component.add(
    name="IEA_GDC_BY_COMMODITY_EMPIRICAL",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_PE_I"],
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_iea_gdc_by_commodity_empirical",
        "__data__": "_ext_data_iea_gdc_by_commodity_empirical",
        "time": 1,
    },
)
def iea_gdc_by_commodity_empirical():
    """
    Empirical primary energy demand (=GDC, Gross Domestic Demand) + Exports / - Imports by PE-commodity and region. Source: IEA Energy balances.
    """
    return _ext_data_iea_gdc_by_commodity_empirical(time())


_ext_data_iea_gdc_by_commodity_empirical = ExtData(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_GDC",
    "GDC_TIME",
    "EU27_PE_IEA",
    "interpolate",
    {"REGIONS_9_I": ["EU27"], "NRG_PE_I": _subscript_dict["NRG_PE_I"]},
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "NRG_PE_I": _subscript_dict["NRG_PE_I"],
    },
    "_ext_data_iea_gdc_by_commodity_empirical",
)

_ext_data_iea_gdc_by_commodity_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_GDC",
    "GDC_TIME",
    "UK_PE_IEA",
    "interpolate",
    {"REGIONS_9_I": ["UK"], "NRG_PE_I": _subscript_dict["NRG_PE_I"]},
)

_ext_data_iea_gdc_by_commodity_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_GDC",
    "GDC_TIME",
    "EASOC_PE_IEA",
    "interpolate",
    {"REGIONS_9_I": ["EASOC"], "NRG_PE_I": _subscript_dict["NRG_PE_I"]},
)

_ext_data_iea_gdc_by_commodity_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_GDC",
    "GDC_TIME",
    "INDIA_PE_IEA",
    "interpolate",
    {"REGIONS_9_I": ["INDIA"], "NRG_PE_I": _subscript_dict["NRG_PE_I"]},
)

_ext_data_iea_gdc_by_commodity_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_GDC",
    "GDC_TIME",
    "LATAM_PE_IEA",
    "interpolate",
    {"REGIONS_9_I": ["LATAM"], "NRG_PE_I": _subscript_dict["NRG_PE_I"]},
)

_ext_data_iea_gdc_by_commodity_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_GDC",
    "GDC_TIME",
    "RUSSIA_PE_IEA",
    "interpolate",
    {"REGIONS_9_I": ["RUSSIA"], "NRG_PE_I": _subscript_dict["NRG_PE_I"]},
)

_ext_data_iea_gdc_by_commodity_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_GDC",
    "GDC_TIME",
    "USMCA_PE_IEA",
    None,
    {"REGIONS_9_I": ["USMCA"], "NRG_PE_I": _subscript_dict["NRG_PE_I"]},
)

_ext_data_iea_gdc_by_commodity_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_GDC",
    "GDC_TIME",
    "LROW_PE_IEA",
    None,
    {"REGIONS_9_I": ["LROW"], "NRG_PE_I": _subscript_dict["NRG_PE_I"]},
)

_ext_data_iea_gdc_by_commodity_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_GDC",
    "GDC_TIME",
    "CHINA_PE_IEA",
    None,
    {"REGIONS_9_I": ["CHINA"], "NRG_PE_I": _subscript_dict["NRG_PE_I"]},
)


@component.add(
    name="INITIAL_2W_3W_FLEET",
    units="vehicle",
    subscripts=["REGIONS_35_I", "TRANSPORT_POWER_TRAIN_I", "HOUSEHOLDS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_2w_3w_fleet"},
)
def initial_2w_3w_fleet():
    """
    Initial LDV fleet by type of household in 2015.
    """
    return _ext_constant_initial_2w_3w_fleet()


_ext_constant_initial_2w_3w_fleet = ExtConstant(
    "model_parameters/energy/energy-transport.xlsx",
    "2W_3W_FLEET",
    "INITIAL_2W_3W_AUSTRIA_FLEET",
    {
        "REGIONS_35_I": ["AUSTRIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
    "_ext_constant_initial_2w_3w_fleet",
)

_ext_constant_initial_2w_3w_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "2W_3W_FLEET",
    "INITIAL_2W_3W_BELGIUM_FLEET",
    {
        "REGIONS_35_I": ["BELGIUM"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
)

_ext_constant_initial_2w_3w_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "2W_3W_FLEET",
    "INITIAL_2W_3W_BULGARIA_FLEET",
    {
        "REGIONS_35_I": ["BULGARIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
)

_ext_constant_initial_2w_3w_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "2W_3W_FLEET",
    "INITIAL_2W_3W_CROATIA_FLEET",
    {
        "REGIONS_35_I": ["CROATIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
)

_ext_constant_initial_2w_3w_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "2W_3W_FLEET",
    "INITIAL_2W_3W_CYPRUS_FLEET",
    {
        "REGIONS_35_I": ["CYPRUS"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
)

_ext_constant_initial_2w_3w_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "2W_3W_FLEET",
    "INITIAL_2W_3W_CZECH_REPUBLIC_FLEET",
    {
        "REGIONS_35_I": ["CZECH_REPUBLIC"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
)

_ext_constant_initial_2w_3w_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "2W_3W_FLEET",
    "INITIAL_2W_3W_DENMARK_FLEET",
    {
        "REGIONS_35_I": ["DENMARK"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
)

_ext_constant_initial_2w_3w_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "2W_3W_FLEET",
    "INITIAL_2W_3W_ESTONIA_FLEET",
    {
        "REGIONS_35_I": ["ESTONIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
)

_ext_constant_initial_2w_3w_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "2W_3W_FLEET",
    "INITIAL_2W_3W_FINLAND_FLEET",
    {
        "REGIONS_35_I": ["FINLAND"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
)

_ext_constant_initial_2w_3w_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "2W_3W_FLEET",
    "INITIAL_2W_3W_FRANCE_FLEET",
    {
        "REGIONS_35_I": ["FRANCE"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
)

_ext_constant_initial_2w_3w_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "2W_3W_FLEET",
    "INITIAL_2W_3W_GERMANY_FLEET",
    {
        "REGIONS_35_I": ["GERMANY"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
)

_ext_constant_initial_2w_3w_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "2W_3W_FLEET",
    "INITIAL_2W_3W_GREECE_FLEET",
    {
        "REGIONS_35_I": ["GREECE"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
)

_ext_constant_initial_2w_3w_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "2W_3W_FLEET",
    "INITIAL_2W_3W_HUNGARY_FLEET",
    {
        "REGIONS_35_I": ["HUNGARY"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
)

_ext_constant_initial_2w_3w_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "2W_3W_FLEET",
    "INITIAL_2W_3W_IRELAND_FLEET",
    {
        "REGIONS_35_I": ["IRELAND"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
)

_ext_constant_initial_2w_3w_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "2W_3W_FLEET",
    "INITIAL_2W_3W_ITALY_FLEET",
    {
        "REGIONS_35_I": ["ITALY"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
)

_ext_constant_initial_2w_3w_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "2W_3W_FLEET",
    "INITIAL_2W_3W_LATVIA_FLEET",
    {
        "REGIONS_35_I": ["LATVIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
)

_ext_constant_initial_2w_3w_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "2W_3W_FLEET",
    "INITIAL_2W_3W_LITHUANIA_FLEET",
    {
        "REGIONS_35_I": ["LITHUANIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
)

_ext_constant_initial_2w_3w_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "2W_3W_FLEET",
    "INITIAL_2W_3W_LUXEMBOURG_FLEET",
    {
        "REGIONS_35_I": ["LUXEMBOURG"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
)

_ext_constant_initial_2w_3w_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "2W_3W_FLEET",
    "INITIAL_2W_3W_MALTA_FLEET",
    {
        "REGIONS_35_I": ["MALTA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
)

_ext_constant_initial_2w_3w_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "2W_3W_FLEET",
    "INITIAL_2W_3W_NETHERLANDS_FLEET",
    {
        "REGIONS_35_I": ["NETHERLANDS"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
)

_ext_constant_initial_2w_3w_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "2W_3W_FLEET",
    "INITIAL_2W_3W_POLAND_FLEET",
    {
        "REGIONS_35_I": ["POLAND"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
)

_ext_constant_initial_2w_3w_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "2W_3W_FLEET",
    "INITIAL_2W_3W_PORTUGAL_FLEET",
    {
        "REGIONS_35_I": ["PORTUGAL"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
)

_ext_constant_initial_2w_3w_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "2W_3W_FLEET",
    "INITIAL_2W_3W_ROMANIA_FLEET",
    {
        "REGIONS_35_I": ["ROMANIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
)

_ext_constant_initial_2w_3w_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "2W_3W_FLEET",
    "INITIAL_2W_3W_SLOVAKIA_FLEET",
    {
        "REGIONS_35_I": ["SLOVAKIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
)

_ext_constant_initial_2w_3w_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "2W_3W_FLEET",
    "INITIAL_2W_3W_SLOVENIA_FLEET",
    {
        "REGIONS_35_I": ["SLOVENIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
)

_ext_constant_initial_2w_3w_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "2W_3W_FLEET",
    "INITIAL_2W_3W_SPAIN_FLEET",
    {
        "REGIONS_35_I": ["SPAIN"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
)

_ext_constant_initial_2w_3w_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "2W_3W_FLEET",
    "INITIAL_2W_3W_SWEDEN_FLEET",
    {
        "REGIONS_35_I": ["SWEDEN"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
)

_ext_constant_initial_2w_3w_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "2W_3W_FLEET",
    "INITIAL_2W_3W_UK_FLEET",
    {
        "REGIONS_35_I": ["UK"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
)

_ext_constant_initial_2w_3w_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "2W_3W_FLEET",
    "INITIAL_2W_3W_CHINA_FLEET",
    {
        "REGIONS_35_I": ["CHINA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
)

_ext_constant_initial_2w_3w_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "2W_3W_FLEET",
    "INITIAL_2W_3W_EASOC_FLEET",
    {
        "REGIONS_35_I": ["EASOC"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
)

_ext_constant_initial_2w_3w_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "2W_3W_FLEET",
    "INITIAL_2W_3W_INDIA_FLEET",
    {
        "REGIONS_35_I": ["INDIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
)

_ext_constant_initial_2w_3w_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "2W_3W_FLEET",
    "INITIAL_2W_3W_LATAM_FLEET",
    {
        "REGIONS_35_I": ["LATAM"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
)

_ext_constant_initial_2w_3w_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "2W_3W_FLEET",
    "INITIAL_2W_3W_RUSSIA_FLEET",
    {
        "REGIONS_35_I": ["RUSSIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
)

_ext_constant_initial_2w_3w_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "2W_3W_FLEET",
    "INITIAL_2W_3W_USMCA_FLEET",
    {
        "REGIONS_35_I": ["USMCA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
)

_ext_constant_initial_2w_3w_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "2W_3W_FLEET",
    "INITIAL_2W_3W_LROW_FLEET",
    {
        "REGIONS_35_I": ["LROW"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
)


@component.add(
    name="INITIAL_LDV_FLEET",
    units="vehicle",
    subscripts=["REGIONS_35_I", "TRANSPORT_POWER_TRAIN_I", "HOUSEHOLDS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_ldv_fleet"},
)
def initial_ldv_fleet():
    """
    Initial LDV fleet by type of household in 2015.
    """
    return _ext_constant_initial_ldv_fleet()


_ext_constant_initial_ldv_fleet = ExtConstant(
    "model_parameters/energy/energy-transport.xlsx",
    "LDV_FLEET",
    "INITIAL_LDV_AUSTRIA_FLEET",
    {
        "REGIONS_35_I": ["AUSTRIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
    "_ext_constant_initial_ldv_fleet",
)

_ext_constant_initial_ldv_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "LDV_FLEET",
    "INITIAL_LDV_BELGIUM_FLEET",
    {
        "REGIONS_35_I": ["BELGIUM"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
)

_ext_constant_initial_ldv_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "LDV_FLEET",
    "INITIAL_LDV_BULGARIA_FLEET",
    {
        "REGIONS_35_I": ["BULGARIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
)

_ext_constant_initial_ldv_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "LDV_FLEET",
    "INITIAL_LDV_CROATIA_FLEET",
    {
        "REGIONS_35_I": ["CROATIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
)

_ext_constant_initial_ldv_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "LDV_FLEET",
    "INITIAL_LDV_CYPRUS_FLEET",
    {
        "REGIONS_35_I": ["CYPRUS"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
)

_ext_constant_initial_ldv_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "LDV_FLEET",
    "INITIAL_LDV_CZECH_REPUBLIC_FLEET",
    {
        "REGIONS_35_I": ["CZECH_REPUBLIC"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
)

_ext_constant_initial_ldv_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "LDV_FLEET",
    "INITIAL_LDV_DENMARK_FLEET",
    {
        "REGIONS_35_I": ["DENMARK"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
)

_ext_constant_initial_ldv_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "LDV_FLEET",
    "INITIAL_LDV_ESTONIA_FLEET",
    {
        "REGIONS_35_I": ["ESTONIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
)

_ext_constant_initial_ldv_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "LDV_FLEET",
    "INITIAL_LDV_FINLAND_FLEET",
    {
        "REGIONS_35_I": ["FINLAND"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
)

_ext_constant_initial_ldv_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "LDV_FLEET",
    "INITIAL_LDV_FRANCE_FLEET",
    {
        "REGIONS_35_I": ["FRANCE"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
)

_ext_constant_initial_ldv_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "LDV_FLEET",
    "INITIAL_LDV_GERMANY_FLEET",
    {
        "REGIONS_35_I": ["GERMANY"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
)

_ext_constant_initial_ldv_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "LDV_FLEET",
    "INITIAL_LDV_GREECE_FLEET",
    {
        "REGIONS_35_I": ["GREECE"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
)

_ext_constant_initial_ldv_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "LDV_FLEET",
    "INITIAL_LDV_HUNGARY_FLEET",
    {
        "REGIONS_35_I": ["HUNGARY"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
)

_ext_constant_initial_ldv_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "LDV_FLEET",
    "INITIAL_LDV_IRELAND_FLEET",
    {
        "REGIONS_35_I": ["IRELAND"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
)

_ext_constant_initial_ldv_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "LDV_FLEET",
    "INITIAL_LDV_ITALY_FLEET",
    {
        "REGIONS_35_I": ["ITALY"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
)

_ext_constant_initial_ldv_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "LDV_FLEET",
    "INITIAL_LDV_LATVIA_FLEET",
    {
        "REGIONS_35_I": ["LATVIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
)

_ext_constant_initial_ldv_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "LDV_FLEET",
    "INITIAL_LDV_LITHUANIA_FLEET",
    {
        "REGIONS_35_I": ["LITHUANIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
)

_ext_constant_initial_ldv_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "LDV_FLEET",
    "INITIAL_LDV_LUXEMBOURG_FLEET",
    {
        "REGIONS_35_I": ["LUXEMBOURG"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
)

_ext_constant_initial_ldv_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "LDV_FLEET",
    "INITIAL_LDV_MALTA_FLEET",
    {
        "REGIONS_35_I": ["MALTA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
)

_ext_constant_initial_ldv_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "LDV_FLEET",
    "INITIAL_LDV_NETHERLANDS_FLEET",
    {
        "REGIONS_35_I": ["NETHERLANDS"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
)

_ext_constant_initial_ldv_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "LDV_FLEET",
    "INITIAL_LDV_POLAND_FLEET",
    {
        "REGIONS_35_I": ["POLAND"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
)

_ext_constant_initial_ldv_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "LDV_FLEET",
    "INITIAL_LDV_PORTUGAL_FLEET",
    {
        "REGIONS_35_I": ["PORTUGAL"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
)

_ext_constant_initial_ldv_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "LDV_FLEET",
    "INITIAL_LDV_ROMANIA_FLEET",
    {
        "REGIONS_35_I": ["ROMANIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
)

_ext_constant_initial_ldv_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "LDV_FLEET",
    "INITIAL_LDV_SLOVAKIA_FLEET",
    {
        "REGIONS_35_I": ["SLOVAKIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
)

_ext_constant_initial_ldv_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "LDV_FLEET",
    "INITIAL_LDV_SLOVENIA_FLEET",
    {
        "REGIONS_35_I": ["SLOVENIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
)

_ext_constant_initial_ldv_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "LDV_FLEET",
    "INITIAL_LDV_SPAIN_FLEET",
    {
        "REGIONS_35_I": ["SPAIN"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
)

_ext_constant_initial_ldv_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "LDV_FLEET",
    "INITIAL_LDV_SWEDEN_FLEET",
    {
        "REGIONS_35_I": ["SWEDEN"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
)

_ext_constant_initial_ldv_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "LDV_FLEET",
    "INITIAL_LDV_UK_FLEET",
    {
        "REGIONS_35_I": ["UK"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
)

_ext_constant_initial_ldv_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "LDV_FLEET",
    "INITIAL_LDV_CHINA_FLEET",
    {
        "REGIONS_35_I": ["CHINA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
)

_ext_constant_initial_ldv_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "LDV_FLEET",
    "INITIAL_LDV_EASOC_FLEET",
    {
        "REGIONS_35_I": ["EASOC"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
)

_ext_constant_initial_ldv_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "LDV_FLEET",
    "INITIAL_LDV_INDIA_FLEET",
    {
        "REGIONS_35_I": ["INDIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
)

_ext_constant_initial_ldv_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "LDV_FLEET",
    "INITIAL_LDV_LATAM_FLEET",
    {
        "REGIONS_35_I": ["LATAM"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
)

_ext_constant_initial_ldv_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "LDV_FLEET",
    "INITIAL_LDV_RUSSIA_FLEET",
    {
        "REGIONS_35_I": ["RUSSIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
)

_ext_constant_initial_ldv_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "LDV_FLEET",
    "INITIAL_LDV_USMCA_FLEET",
    {
        "REGIONS_35_I": ["USMCA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
)

_ext_constant_initial_ldv_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "LDV_FLEET",
    "INITIAL_LDV_LROW_FLEET",
    {
        "REGIONS_35_I": ["LROW"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"],
    },
)


@component.add(
    name="INITIAL_LOAD_FACTOR_PASSENGERS_VEHICLES",
    units="persons/vehicle",
    subscripts=[
        "REGIONS_35_I",
        "TRANSPORT_POWER_TRAIN_I",
        "PASSENGERS_TRANSPORT_MODE_I",
    ],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_initial_load_factor_passengers_vehicles"
    },
)
def initial_load_factor_passengers_vehicles():
    """
    Capacity of vehicles in passengers per vehicle
    """
    return _ext_constant_initial_load_factor_passengers_vehicles()


_ext_constant_initial_load_factor_passengers_vehicles = ExtConstant(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "LOAD_FACTOR_AUSTRIA",
    {
        "REGIONS_35_I": ["AUSTRIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
    "_ext_constant_initial_load_factor_passengers_vehicles",
)

_ext_constant_initial_load_factor_passengers_vehicles.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "LOAD_FACTOR_BELGIUM",
    {
        "REGIONS_35_I": ["BELGIUM"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_load_factor_passengers_vehicles.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "LOAD_FACTOR_BULGARIA",
    {
        "REGIONS_35_I": ["BULGARIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_load_factor_passengers_vehicles.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "LOAD_FACTOR_CROATIA",
    {
        "REGIONS_35_I": ["CROATIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_load_factor_passengers_vehicles.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "LOAD_FACTOR_CYPRUS",
    {
        "REGIONS_35_I": ["CYPRUS"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_load_factor_passengers_vehicles.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "LOAD_FACTOR_CZECH_REPUBLIC",
    {
        "REGIONS_35_I": ["CZECH_REPUBLIC"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_load_factor_passengers_vehicles.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "LOAD_FACTOR_DENMARK",
    {
        "REGIONS_35_I": ["DENMARK"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_load_factor_passengers_vehicles.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "LOAD_FACTOR_ESTONIA",
    {
        "REGIONS_35_I": ["ESTONIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_load_factor_passengers_vehicles.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "LOAD_FACTOR_FINLAND",
    {
        "REGIONS_35_I": ["FINLAND"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_load_factor_passengers_vehicles.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "LOAD_FACTOR_FRANCE",
    {
        "REGIONS_35_I": ["FRANCE"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_load_factor_passengers_vehicles.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "LOAD_FACTOR_GERMANY",
    {
        "REGIONS_35_I": ["GERMANY"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_load_factor_passengers_vehicles.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "LOAD_FACTOR_GREECE",
    {
        "REGIONS_35_I": ["GREECE"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_load_factor_passengers_vehicles.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "LOAD_FACTOR_HUNGARY",
    {
        "REGIONS_35_I": ["HUNGARY"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_load_factor_passengers_vehicles.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "LOAD_FACTOR_IRELAND",
    {
        "REGIONS_35_I": ["IRELAND"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_load_factor_passengers_vehicles.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "LOAD_FACTOR_ITALY",
    {
        "REGIONS_35_I": ["ITALY"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_load_factor_passengers_vehicles.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "LOAD_FACTOR_LATVIA",
    {
        "REGIONS_35_I": ["LATVIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_load_factor_passengers_vehicles.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "LOAD_FACTOR_LITHUANIA",
    {
        "REGIONS_35_I": ["LITHUANIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_load_factor_passengers_vehicles.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "LOAD_FACTOR_LUXEMBOURG",
    {
        "REGIONS_35_I": ["LUXEMBOURG"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_load_factor_passengers_vehicles.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "LOAD_FACTOR_MALTA",
    {
        "REGIONS_35_I": ["MALTA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_load_factor_passengers_vehicles.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "LOAD_FACTOR_NETHERLANDS",
    {
        "REGIONS_35_I": ["NETHERLANDS"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_load_factor_passengers_vehicles.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "LOAD_FACTOR_POLAND",
    {
        "REGIONS_35_I": ["POLAND"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_load_factor_passengers_vehicles.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "LOAD_FACTOR_PORTUGAL",
    {
        "REGIONS_35_I": ["PORTUGAL"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_load_factor_passengers_vehicles.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "LOAD_FACTOR_ROMANIA",
    {
        "REGIONS_35_I": ["ROMANIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_load_factor_passengers_vehicles.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "LOAD_FACTOR_SLOVAKIA",
    {
        "REGIONS_35_I": ["SLOVAKIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_load_factor_passengers_vehicles.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "LOAD_FACTOR_SLOVENIA",
    {
        "REGIONS_35_I": ["SLOVENIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_load_factor_passengers_vehicles.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "LOAD_FACTOR_SPAIN",
    {
        "REGIONS_35_I": ["SPAIN"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_load_factor_passengers_vehicles.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "LOAD_FACTOR_SWEDEN",
    {
        "REGIONS_35_I": ["SWEDEN"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_load_factor_passengers_vehicles.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "LOAD_FACTOR_UK",
    {
        "REGIONS_35_I": ["UK"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_load_factor_passengers_vehicles.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "LOAD_FACTOR_CHINA",
    {
        "REGIONS_35_I": ["CHINA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_load_factor_passengers_vehicles.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "LOAD_FACTOR_EASOC",
    {
        "REGIONS_35_I": ["EASOC"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_load_factor_passengers_vehicles.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "LOAD_FACTOR_INDIA",
    {
        "REGIONS_35_I": ["INDIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_load_factor_passengers_vehicles.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "LOAD_FACTOR_LATAM",
    {
        "REGIONS_35_I": ["LATAM"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_load_factor_passengers_vehicles.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "LOAD_FACTOR_RUSSIA",
    {
        "REGIONS_35_I": ["RUSSIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_load_factor_passengers_vehicles.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "LOAD_FACTOR_USMCA",
    {
        "REGIONS_35_I": ["USMCA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_load_factor_passengers_vehicles.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "LOAD_FACTOR_LROW",
    {
        "REGIONS_35_I": ["LROW"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)


@component.add(
    name="INITIAL_PASSENGER_TRANSPORT_DEMAND_SHARE",
    units="DMNL",
    subscripts=[
        "REGIONS_35_I",
        "TRANSPORT_POWER_TRAIN_I",
        "PASSENGERS_TRANSPORT_MODE_I",
    ],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_initial_passenger_transport_demand_share"
    },
)
def initial_passenger_transport_demand_share():
    """
    Demand transport share by transport mode and power train in 2015 year.
    """
    return _ext_constant_initial_passenger_transport_demand_share()


_ext_constant_initial_passenger_transport_demand_share = ExtConstant(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_DEMAND_SHARE_AUSTRIA",
    {
        "REGIONS_35_I": ["AUSTRIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
    "_ext_constant_initial_passenger_transport_demand_share",
)

_ext_constant_initial_passenger_transport_demand_share.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_DEMAND_SHARE_BELGIUM",
    {
        "REGIONS_35_I": ["BELGIUM"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_passenger_transport_demand_share.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_DEMAND_SHARE_BULGARIA",
    {
        "REGIONS_35_I": ["BULGARIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_passenger_transport_demand_share.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_DEMAND_SHARE_CROATIA",
    {
        "REGIONS_35_I": ["CROATIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_passenger_transport_demand_share.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_DEMAND_SHARE_CYPRUS",
    {
        "REGIONS_35_I": ["CYPRUS"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_passenger_transport_demand_share.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_DEMAND_SHARE_CZECH_REPUBLIC",
    {
        "REGIONS_35_I": ["CZECH_REPUBLIC"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_passenger_transport_demand_share.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_DEMAND_SHARE_DENMARK",
    {
        "REGIONS_35_I": ["DENMARK"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_passenger_transport_demand_share.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_DEMAND_SHARE_ESTONIA",
    {
        "REGIONS_35_I": ["ESTONIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_passenger_transport_demand_share.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_DEMAND_SHARE_FINLAND",
    {
        "REGIONS_35_I": ["FINLAND"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_passenger_transport_demand_share.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_DEMAND_SHARE_FRANCE",
    {
        "REGIONS_35_I": ["FRANCE"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_passenger_transport_demand_share.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_DEMAND_SHARE_GERMANY",
    {
        "REGIONS_35_I": ["GERMANY"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_passenger_transport_demand_share.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_DEMAND_SHARE_GREECE",
    {
        "REGIONS_35_I": ["GREECE"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_passenger_transport_demand_share.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_DEMAND_SHARE_HUNGARY",
    {
        "REGIONS_35_I": ["HUNGARY"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_passenger_transport_demand_share.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_DEMAND_SHARE_IRELAND",
    {
        "REGIONS_35_I": ["IRELAND"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_passenger_transport_demand_share.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_DEMAND_SHARE_ITALY",
    {
        "REGIONS_35_I": ["ITALY"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_passenger_transport_demand_share.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_DEMAND_SHARE_LATVIA",
    {
        "REGIONS_35_I": ["LATVIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_passenger_transport_demand_share.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_DEMAND_SHARE_LITHUANIA",
    {
        "REGIONS_35_I": ["LITHUANIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_passenger_transport_demand_share.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_DEMAND_SHARE_LUXEMBOURG",
    {
        "REGIONS_35_I": ["LUXEMBOURG"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_passenger_transport_demand_share.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_DEMAND_SHARE_MALTA",
    {
        "REGIONS_35_I": ["MALTA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_passenger_transport_demand_share.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_DEMAND_SHARE_NETHERLANDS",
    {
        "REGIONS_35_I": ["NETHERLANDS"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_passenger_transport_demand_share.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_DEMAND_SHARE_POLAND",
    {
        "REGIONS_35_I": ["POLAND"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_passenger_transport_demand_share.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_DEMAND_SHARE_PORTUGAL",
    {
        "REGIONS_35_I": ["PORTUGAL"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_passenger_transport_demand_share.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_DEMAND_SHARE_ROMANIA",
    {
        "REGIONS_35_I": ["ROMANIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_passenger_transport_demand_share.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_DEMAND_SHARE_SLOVAKIA",
    {
        "REGIONS_35_I": ["SLOVAKIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_passenger_transport_demand_share.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_DEMAND_SHARE_SLOVENIA",
    {
        "REGIONS_35_I": ["SLOVENIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_passenger_transport_demand_share.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_DEMAND_SHARE_SPAIN",
    {
        "REGIONS_35_I": ["SPAIN"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_passenger_transport_demand_share.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_DEMAND_SHARE_SWEDEN",
    {
        "REGIONS_35_I": ["SWEDEN"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_passenger_transport_demand_share.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_DEMAND_SHARE_UK",
    {
        "REGIONS_35_I": ["UK"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_passenger_transport_demand_share.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_DEMAND_SHARE_CHINA",
    {
        "REGIONS_35_I": ["CHINA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_passenger_transport_demand_share.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_DEMAND_SHARE_EASOC",
    {
        "REGIONS_35_I": ["EASOC"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_passenger_transport_demand_share.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_DEMAND_SHARE_INDIA",
    {
        "REGIONS_35_I": ["INDIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_passenger_transport_demand_share.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_DEMAND_SHARE_LATAM",
    {
        "REGIONS_35_I": ["LATAM"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_passenger_transport_demand_share.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_DEMAND_SHARE_RUSSIA",
    {
        "REGIONS_35_I": ["RUSSIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_passenger_transport_demand_share.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_DEMAND_SHARE_USMCA",
    {
        "REGIONS_35_I": ["USMCA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_passenger_transport_demand_share.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_DEMAND_SHARE_LROW",
    {
        "REGIONS_35_I": ["LROW"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)


@component.add(
    name="INITIAL_PASSENGERS_PRIVATE_FLEET",
    units="vehicle",
    subscripts=["REGIONS_35_I", "TRANSPORT_POWER_TRAIN_I", "PRIVATE_TRANSPORT_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_passengers_private_fleet"},
)
def initial_passengers_private_fleet():
    """
    Initial private vehicle fleet in 2015.
    """
    return _ext_constant_initial_passengers_private_fleet()


_ext_constant_initial_passengers_private_fleet = ExtConstant(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_PRIVATE_FLEET_AUSTRIA",
    {
        "REGIONS_35_I": ["AUSTRIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PRIVATE_TRANSPORT_I": _subscript_dict["PRIVATE_TRANSPORT_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PRIVATE_TRANSPORT_I": _subscript_dict["PRIVATE_TRANSPORT_I"],
    },
    "_ext_constant_initial_passengers_private_fleet",
)

_ext_constant_initial_passengers_private_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_PRIVATE_FLEET_BELGIUM",
    {
        "REGIONS_35_I": ["BELGIUM"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PRIVATE_TRANSPORT_I": _subscript_dict["PRIVATE_TRANSPORT_I"],
    },
)

_ext_constant_initial_passengers_private_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_PRIVATE_FLEET_BULGARIA",
    {
        "REGIONS_35_I": ["BULGARIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PRIVATE_TRANSPORT_I": _subscript_dict["PRIVATE_TRANSPORT_I"],
    },
)

_ext_constant_initial_passengers_private_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_PRIVATE_FLEET_CROATIA",
    {
        "REGIONS_35_I": ["CROATIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PRIVATE_TRANSPORT_I": _subscript_dict["PRIVATE_TRANSPORT_I"],
    },
)

_ext_constant_initial_passengers_private_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_PRIVATE_FLEET_CYPRUS",
    {
        "REGIONS_35_I": ["CYPRUS"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PRIVATE_TRANSPORT_I": _subscript_dict["PRIVATE_TRANSPORT_I"],
    },
)

_ext_constant_initial_passengers_private_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_PRIVATE_FLEET_CZECH_REPUBLIC",
    {
        "REGIONS_35_I": ["CZECH_REPUBLIC"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PRIVATE_TRANSPORT_I": _subscript_dict["PRIVATE_TRANSPORT_I"],
    },
)

_ext_constant_initial_passengers_private_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_PRIVATE_FLEET_DENMARK",
    {
        "REGIONS_35_I": ["DENMARK"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PRIVATE_TRANSPORT_I": _subscript_dict["PRIVATE_TRANSPORT_I"],
    },
)

_ext_constant_initial_passengers_private_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_PRIVATE_FLEET_ESTONIA",
    {
        "REGIONS_35_I": ["ESTONIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PRIVATE_TRANSPORT_I": _subscript_dict["PRIVATE_TRANSPORT_I"],
    },
)

_ext_constant_initial_passengers_private_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_PRIVATE_FLEET_FINLAND",
    {
        "REGIONS_35_I": ["FINLAND"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PRIVATE_TRANSPORT_I": _subscript_dict["PRIVATE_TRANSPORT_I"],
    },
)

_ext_constant_initial_passengers_private_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_PRIVATE_FLEET_FRANCE",
    {
        "REGIONS_35_I": ["FRANCE"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PRIVATE_TRANSPORT_I": _subscript_dict["PRIVATE_TRANSPORT_I"],
    },
)

_ext_constant_initial_passengers_private_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_PRIVATE_FLEET_GERMANY",
    {
        "REGIONS_35_I": ["GERMANY"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PRIVATE_TRANSPORT_I": _subscript_dict["PRIVATE_TRANSPORT_I"],
    },
)

_ext_constant_initial_passengers_private_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_PRIVATE_FLEET_GREECE",
    {
        "REGIONS_35_I": ["GREECE"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PRIVATE_TRANSPORT_I": _subscript_dict["PRIVATE_TRANSPORT_I"],
    },
)

_ext_constant_initial_passengers_private_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_PRIVATE_FLEET_HUNGARY",
    {
        "REGIONS_35_I": ["HUNGARY"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PRIVATE_TRANSPORT_I": _subscript_dict["PRIVATE_TRANSPORT_I"],
    },
)

_ext_constant_initial_passengers_private_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_PRIVATE_FLEET_IRELAND",
    {
        "REGIONS_35_I": ["IRELAND"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PRIVATE_TRANSPORT_I": _subscript_dict["PRIVATE_TRANSPORT_I"],
    },
)

_ext_constant_initial_passengers_private_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_PRIVATE_FLEET_ITALY",
    {
        "REGIONS_35_I": ["ITALY"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PRIVATE_TRANSPORT_I": _subscript_dict["PRIVATE_TRANSPORT_I"],
    },
)

_ext_constant_initial_passengers_private_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_PRIVATE_FLEET_LATVIA",
    {
        "REGIONS_35_I": ["LATVIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PRIVATE_TRANSPORT_I": _subscript_dict["PRIVATE_TRANSPORT_I"],
    },
)

_ext_constant_initial_passengers_private_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_PRIVATE_FLEET_LITHUANIA",
    {
        "REGIONS_35_I": ["LITHUANIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PRIVATE_TRANSPORT_I": _subscript_dict["PRIVATE_TRANSPORT_I"],
    },
)

_ext_constant_initial_passengers_private_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_PRIVATE_FLEET_LUXEMBOURG",
    {
        "REGIONS_35_I": ["LUXEMBOURG"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PRIVATE_TRANSPORT_I": _subscript_dict["PRIVATE_TRANSPORT_I"],
    },
)

_ext_constant_initial_passengers_private_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_PRIVATE_FLEET_MALTA",
    {
        "REGIONS_35_I": ["MALTA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PRIVATE_TRANSPORT_I": _subscript_dict["PRIVATE_TRANSPORT_I"],
    },
)

_ext_constant_initial_passengers_private_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_PRIVATE_FLEET_NETHERLANDS",
    {
        "REGIONS_35_I": ["NETHERLANDS"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PRIVATE_TRANSPORT_I": _subscript_dict["PRIVATE_TRANSPORT_I"],
    },
)

_ext_constant_initial_passengers_private_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_PRIVATE_FLEET_POLAND",
    {
        "REGIONS_35_I": ["POLAND"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PRIVATE_TRANSPORT_I": _subscript_dict["PRIVATE_TRANSPORT_I"],
    },
)

_ext_constant_initial_passengers_private_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_PRIVATE_FLEET_PORTUGAL",
    {
        "REGIONS_35_I": ["PORTUGAL"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PRIVATE_TRANSPORT_I": _subscript_dict["PRIVATE_TRANSPORT_I"],
    },
)

_ext_constant_initial_passengers_private_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_PRIVATE_FLEET_ROMANIA",
    {
        "REGIONS_35_I": ["ROMANIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PRIVATE_TRANSPORT_I": _subscript_dict["PRIVATE_TRANSPORT_I"],
    },
)

_ext_constant_initial_passengers_private_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_PRIVATE_FLEET_SLOVAKIA",
    {
        "REGIONS_35_I": ["SLOVAKIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PRIVATE_TRANSPORT_I": _subscript_dict["PRIVATE_TRANSPORT_I"],
    },
)

_ext_constant_initial_passengers_private_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_PRIVATE_FLEET_SLOVENIA",
    {
        "REGIONS_35_I": ["SLOVENIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PRIVATE_TRANSPORT_I": _subscript_dict["PRIVATE_TRANSPORT_I"],
    },
)

_ext_constant_initial_passengers_private_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_PRIVATE_FLEET_SPAIN",
    {
        "REGIONS_35_I": ["SPAIN"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PRIVATE_TRANSPORT_I": _subscript_dict["PRIVATE_TRANSPORT_I"],
    },
)

_ext_constant_initial_passengers_private_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_PRIVATE_FLEET_SWEDEN",
    {
        "REGIONS_35_I": ["SWEDEN"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PRIVATE_TRANSPORT_I": _subscript_dict["PRIVATE_TRANSPORT_I"],
    },
)

_ext_constant_initial_passengers_private_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_PRIVATE_FLEET_UK",
    {
        "REGIONS_35_I": ["UK"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PRIVATE_TRANSPORT_I": _subscript_dict["PRIVATE_TRANSPORT_I"],
    },
)

_ext_constant_initial_passengers_private_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_PRIVATE_FLEET_CHINA",
    {
        "REGIONS_35_I": ["CHINA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PRIVATE_TRANSPORT_I": _subscript_dict["PRIVATE_TRANSPORT_I"],
    },
)

_ext_constant_initial_passengers_private_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_PRIVATE_FLEET_EASOC",
    {
        "REGIONS_35_I": ["EASOC"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PRIVATE_TRANSPORT_I": _subscript_dict["PRIVATE_TRANSPORT_I"],
    },
)

_ext_constant_initial_passengers_private_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_PRIVATE_FLEET_INDIA",
    {
        "REGIONS_35_I": ["INDIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PRIVATE_TRANSPORT_I": _subscript_dict["PRIVATE_TRANSPORT_I"],
    },
)

_ext_constant_initial_passengers_private_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_PRIVATE_FLEET_LATAM",
    {
        "REGIONS_35_I": ["LATAM"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PRIVATE_TRANSPORT_I": _subscript_dict["PRIVATE_TRANSPORT_I"],
    },
)

_ext_constant_initial_passengers_private_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_PRIVATE_FLEET_RUSSIA",
    {
        "REGIONS_35_I": ["RUSSIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PRIVATE_TRANSPORT_I": _subscript_dict["PRIVATE_TRANSPORT_I"],
    },
)

_ext_constant_initial_passengers_private_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_PRIVATE_FLEET_USMCA",
    {
        "REGIONS_35_I": ["USMCA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PRIVATE_TRANSPORT_I": _subscript_dict["PRIVATE_TRANSPORT_I"],
    },
)

_ext_constant_initial_passengers_private_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_PRIVATE_FLEET_LROW",
    {
        "REGIONS_35_I": ["LROW"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PRIVATE_TRANSPORT_I": _subscript_dict["PRIVATE_TRANSPORT_I"],
    },
)


@component.add(
    name="INITIAL_PASSENGERS_PUBLIC_FLEET",
    units="vehicle",
    subscripts=["REGIONS_35_I", "TRANSPORT_POWER_TRAIN_I", "PUBLIC_TRANSPORT_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_passengers_public_fleet"},
)
def initial_passengers_public_fleet():
    """
    Initial public vehicle fleet in 2015.
    """
    return _ext_constant_initial_passengers_public_fleet()


_ext_constant_initial_passengers_public_fleet = ExtConstant(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_PUBLIC_FLEET_AUSTRIA",
    {
        "REGIONS_35_I": ["AUSTRIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PUBLIC_TRANSPORT_I": _subscript_dict["PUBLIC_TRANSPORT_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PUBLIC_TRANSPORT_I": _subscript_dict["PUBLIC_TRANSPORT_I"],
    },
    "_ext_constant_initial_passengers_public_fleet",
)

_ext_constant_initial_passengers_public_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_PUBLIC_FLEET_BELGIUM",
    {
        "REGIONS_35_I": ["BELGIUM"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PUBLIC_TRANSPORT_I": _subscript_dict["PUBLIC_TRANSPORT_I"],
    },
)

_ext_constant_initial_passengers_public_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_PUBLIC_FLEET_BULGARIA",
    {
        "REGIONS_35_I": ["BULGARIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PUBLIC_TRANSPORT_I": _subscript_dict["PUBLIC_TRANSPORT_I"],
    },
)

_ext_constant_initial_passengers_public_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_PUBLIC_FLEET_CROATIA",
    {
        "REGIONS_35_I": ["CROATIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PUBLIC_TRANSPORT_I": _subscript_dict["PUBLIC_TRANSPORT_I"],
    },
)

_ext_constant_initial_passengers_public_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_PUBLIC_FLEET_CYPRUS",
    {
        "REGIONS_35_I": ["CYPRUS"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PUBLIC_TRANSPORT_I": _subscript_dict["PUBLIC_TRANSPORT_I"],
    },
)

_ext_constant_initial_passengers_public_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_PUBLIC_FLEET_CZECH_REPUBLIC",
    {
        "REGIONS_35_I": ["CZECH_REPUBLIC"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PUBLIC_TRANSPORT_I": _subscript_dict["PUBLIC_TRANSPORT_I"],
    },
)

_ext_constant_initial_passengers_public_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_PUBLIC_FLEET_DENMARK",
    {
        "REGIONS_35_I": ["DENMARK"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PUBLIC_TRANSPORT_I": _subscript_dict["PUBLIC_TRANSPORT_I"],
    },
)

_ext_constant_initial_passengers_public_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_PUBLIC_FLEET_ESTONIA",
    {
        "REGIONS_35_I": ["ESTONIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PUBLIC_TRANSPORT_I": _subscript_dict["PUBLIC_TRANSPORT_I"],
    },
)

_ext_constant_initial_passengers_public_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_PUBLIC_FLEET_FINLAND",
    {
        "REGIONS_35_I": ["FINLAND"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PUBLIC_TRANSPORT_I": _subscript_dict["PUBLIC_TRANSPORT_I"],
    },
)

_ext_constant_initial_passengers_public_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_PUBLIC_FLEET_FRANCE",
    {
        "REGIONS_35_I": ["FRANCE"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PUBLIC_TRANSPORT_I": _subscript_dict["PUBLIC_TRANSPORT_I"],
    },
)

_ext_constant_initial_passengers_public_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_PUBLIC_FLEET_GERMANY",
    {
        "REGIONS_35_I": ["GERMANY"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PUBLIC_TRANSPORT_I": _subscript_dict["PUBLIC_TRANSPORT_I"],
    },
)

_ext_constant_initial_passengers_public_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_PUBLIC_FLEET_GREECE",
    {
        "REGIONS_35_I": ["GREECE"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PUBLIC_TRANSPORT_I": _subscript_dict["PUBLIC_TRANSPORT_I"],
    },
)

_ext_constant_initial_passengers_public_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_PUBLIC_FLEET_HUNGARY",
    {
        "REGIONS_35_I": ["HUNGARY"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PUBLIC_TRANSPORT_I": _subscript_dict["PUBLIC_TRANSPORT_I"],
    },
)

_ext_constant_initial_passengers_public_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_PUBLIC_FLEET_IRELAND",
    {
        "REGIONS_35_I": ["IRELAND"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PUBLIC_TRANSPORT_I": _subscript_dict["PUBLIC_TRANSPORT_I"],
    },
)

_ext_constant_initial_passengers_public_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_PUBLIC_FLEET_ITALY",
    {
        "REGIONS_35_I": ["ITALY"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PUBLIC_TRANSPORT_I": _subscript_dict["PUBLIC_TRANSPORT_I"],
    },
)

_ext_constant_initial_passengers_public_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_PUBLIC_FLEET_LATVIA",
    {
        "REGIONS_35_I": ["LATVIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PUBLIC_TRANSPORT_I": _subscript_dict["PUBLIC_TRANSPORT_I"],
    },
)

_ext_constant_initial_passengers_public_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_PUBLIC_FLEET_LITHUANIA",
    {
        "REGIONS_35_I": ["LITHUANIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PUBLIC_TRANSPORT_I": _subscript_dict["PUBLIC_TRANSPORT_I"],
    },
)

_ext_constant_initial_passengers_public_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_PUBLIC_FLEET_LUXEMBOURG",
    {
        "REGIONS_35_I": ["LUXEMBOURG"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PUBLIC_TRANSPORT_I": _subscript_dict["PUBLIC_TRANSPORT_I"],
    },
)

_ext_constant_initial_passengers_public_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_PUBLIC_FLEET_MALTA",
    {
        "REGIONS_35_I": ["MALTA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PUBLIC_TRANSPORT_I": _subscript_dict["PUBLIC_TRANSPORT_I"],
    },
)

_ext_constant_initial_passengers_public_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_PUBLIC_FLEET_NETHERLANDS",
    {
        "REGIONS_35_I": ["NETHERLANDS"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PUBLIC_TRANSPORT_I": _subscript_dict["PUBLIC_TRANSPORT_I"],
    },
)

_ext_constant_initial_passengers_public_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_PUBLIC_FLEET_POLAND",
    {
        "REGIONS_35_I": ["POLAND"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PUBLIC_TRANSPORT_I": _subscript_dict["PUBLIC_TRANSPORT_I"],
    },
)

_ext_constant_initial_passengers_public_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_PUBLIC_FLEET_PORTUGAL",
    {
        "REGIONS_35_I": ["PORTUGAL"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PUBLIC_TRANSPORT_I": _subscript_dict["PUBLIC_TRANSPORT_I"],
    },
)

_ext_constant_initial_passengers_public_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_PUBLIC_FLEET_ROMANIA",
    {
        "REGIONS_35_I": ["ROMANIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PUBLIC_TRANSPORT_I": _subscript_dict["PUBLIC_TRANSPORT_I"],
    },
)

_ext_constant_initial_passengers_public_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_PUBLIC_FLEET_SLOVAKIA",
    {
        "REGIONS_35_I": ["SLOVAKIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PUBLIC_TRANSPORT_I": _subscript_dict["PUBLIC_TRANSPORT_I"],
    },
)

_ext_constant_initial_passengers_public_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_PUBLIC_FLEET_SLOVENIA",
    {
        "REGIONS_35_I": ["SLOVENIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PUBLIC_TRANSPORT_I": _subscript_dict["PUBLIC_TRANSPORT_I"],
    },
)

_ext_constant_initial_passengers_public_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_PUBLIC_FLEET_SPAIN",
    {
        "REGIONS_35_I": ["SPAIN"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PUBLIC_TRANSPORT_I": _subscript_dict["PUBLIC_TRANSPORT_I"],
    },
)

_ext_constant_initial_passengers_public_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_PUBLIC_FLEET_SWEDEN",
    {
        "REGIONS_35_I": ["SWEDEN"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PUBLIC_TRANSPORT_I": _subscript_dict["PUBLIC_TRANSPORT_I"],
    },
)

_ext_constant_initial_passengers_public_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_PUBLIC_FLEET_UK",
    {
        "REGIONS_35_I": ["UK"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PUBLIC_TRANSPORT_I": _subscript_dict["PUBLIC_TRANSPORT_I"],
    },
)

_ext_constant_initial_passengers_public_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_PUBLIC_FLEET_CHINA",
    {
        "REGIONS_35_I": ["CHINA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PUBLIC_TRANSPORT_I": _subscript_dict["PUBLIC_TRANSPORT_I"],
    },
)

_ext_constant_initial_passengers_public_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_PUBLIC_FLEET_EASOC",
    {
        "REGIONS_35_I": ["EASOC"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PUBLIC_TRANSPORT_I": _subscript_dict["PUBLIC_TRANSPORT_I"],
    },
)

_ext_constant_initial_passengers_public_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_PUBLIC_FLEET_INDIA",
    {
        "REGIONS_35_I": ["INDIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PUBLIC_TRANSPORT_I": _subscript_dict["PUBLIC_TRANSPORT_I"],
    },
)

_ext_constant_initial_passengers_public_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_PUBLIC_FLEET_LATAM",
    {
        "REGIONS_35_I": ["LATAM"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PUBLIC_TRANSPORT_I": _subscript_dict["PUBLIC_TRANSPORT_I"],
    },
)

_ext_constant_initial_passengers_public_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_PUBLIC_FLEET_RUSSIA",
    {
        "REGIONS_35_I": ["RUSSIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PUBLIC_TRANSPORT_I": _subscript_dict["PUBLIC_TRANSPORT_I"],
    },
)

_ext_constant_initial_passengers_public_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_PUBLIC_FLEET_USMCA",
    {
        "REGIONS_35_I": ["USMCA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PUBLIC_TRANSPORT_I": _subscript_dict["PUBLIC_TRANSPORT_I"],
    },
)

_ext_constant_initial_passengers_public_fleet.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "INITIAL_PUBLIC_FLEET_LROW",
    {
        "REGIONS_35_I": ["LROW"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PUBLIC_TRANSPORT_I": _subscript_dict["PUBLIC_TRANSPORT_I"],
    },
)


@component.add(
    name="INITIAL_PASSENGERS_VEHICLE_DISTANCE",
    units="km",
    subscripts=[
        "REGIONS_35_I",
        "TRANSPORT_POWER_TRAIN_I",
        "PASSENGERS_TRANSPORT_MODE_I",
    ],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_passengers_vehicle_distance"},
)
def initial_passengers_vehicle_distance():
    """
    Annual vehicle distance travelled by type of transport mode and power train in 2015 year in km.
    """
    return _ext_constant_initial_passengers_vehicle_distance()


_ext_constant_initial_passengers_vehicle_distance = ExtConstant(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "VEHICLE_DISTANCE_AUSTRIA",
    {
        "REGIONS_35_I": ["AUSTRIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
    "_ext_constant_initial_passengers_vehicle_distance",
)

_ext_constant_initial_passengers_vehicle_distance.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "VEHICLE_DISTANCE_BELGIUM",
    {
        "REGIONS_35_I": ["BELGIUM"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_passengers_vehicle_distance.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "VEHICLE_DISTANCE_BULGARIA",
    {
        "REGIONS_35_I": ["BULGARIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_passengers_vehicle_distance.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "VEHICLE_DISTANCE_CROATIA",
    {
        "REGIONS_35_I": ["CROATIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_passengers_vehicle_distance.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "VEHICLE_DISTANCE_CYPRUS",
    {
        "REGIONS_35_I": ["CYPRUS"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_passengers_vehicle_distance.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "VEHICLE_DISTANCE_CZECH_REPUBLIC",
    {
        "REGIONS_35_I": ["CZECH_REPUBLIC"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_passengers_vehicle_distance.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "VEHICLE_DISTANCE_DENMARK",
    {
        "REGIONS_35_I": ["DENMARK"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_passengers_vehicle_distance.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "VEHICLE_DISTANCE_ESTONIA",
    {
        "REGIONS_35_I": ["ESTONIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_passengers_vehicle_distance.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "VEHICLE_DISTANCE_FINLAND",
    {
        "REGIONS_35_I": ["FINLAND"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_passengers_vehicle_distance.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "VEHICLE_DISTANCE_FRANCE",
    {
        "REGIONS_35_I": ["FRANCE"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_passengers_vehicle_distance.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "VEHICLE_DISTANCE_GERMANY",
    {
        "REGIONS_35_I": ["GERMANY"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_passengers_vehicle_distance.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "VEHICLE_DISTANCE_GREECE",
    {
        "REGIONS_35_I": ["GREECE"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_passengers_vehicle_distance.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "VEHICLE_DISTANCE_HUNGARY",
    {
        "REGIONS_35_I": ["HUNGARY"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_passengers_vehicle_distance.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "VEHICLE_DISTANCE_IRELAND",
    {
        "REGIONS_35_I": ["IRELAND"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_passengers_vehicle_distance.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "VEHICLE_DISTANCE_ITALY",
    {
        "REGIONS_35_I": ["ITALY"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_passengers_vehicle_distance.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "VEHICLE_DISTANCE_LATVIA",
    {
        "REGIONS_35_I": ["LATVIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_passengers_vehicle_distance.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "VEHICLE_DISTANCE_LITHUANIA",
    {
        "REGIONS_35_I": ["LITHUANIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_passengers_vehicle_distance.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "VEHICLE_DISTANCE_LUXEMBOURG",
    {
        "REGIONS_35_I": ["LUXEMBOURG"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_passengers_vehicle_distance.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "VEHICLE_DISTANCE_MALTA",
    {
        "REGIONS_35_I": ["MALTA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_passengers_vehicle_distance.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "VEHICLE_DISTANCE_NETHERLANDS",
    {
        "REGIONS_35_I": ["NETHERLANDS"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_passengers_vehicle_distance.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "VEHICLE_DISTANCE_POLAND",
    {
        "REGIONS_35_I": ["POLAND"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_passengers_vehicle_distance.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "VEHICLE_DISTANCE_PORTUGAL",
    {
        "REGIONS_35_I": ["PORTUGAL"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_passengers_vehicle_distance.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "VEHICLE_DISTANCE_ROMANIA",
    {
        "REGIONS_35_I": ["ROMANIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_passengers_vehicle_distance.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "VEHICLE_DISTANCE_SLOVAKIA",
    {
        "REGIONS_35_I": ["SLOVAKIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_passengers_vehicle_distance.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "VEHICLE_DISTANCE_SLOVENIA",
    {
        "REGIONS_35_I": ["SLOVENIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_passengers_vehicle_distance.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "VEHICLE_DISTANCE_SPAIN",
    {
        "REGIONS_35_I": ["SPAIN"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_passengers_vehicle_distance.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "VEHICLE_DISTANCE_SWEDEN",
    {
        "REGIONS_35_I": ["SWEDEN"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_passengers_vehicle_distance.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "VEHICLE_DISTANCE_UK",
    {
        "REGIONS_35_I": ["UK"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_passengers_vehicle_distance.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "VEHICLE_DISTANCE_CHINA",
    {
        "REGIONS_35_I": ["CHINA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_passengers_vehicle_distance.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "VEHICLE_DISTANCE_EASOC",
    {
        "REGIONS_35_I": ["EASOC"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_passengers_vehicle_distance.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "VEHICLE_DISTANCE_INDIA",
    {
        "REGIONS_35_I": ["INDIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_passengers_vehicle_distance.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "VEHICLE_DISTANCE_LATAM",
    {
        "REGIONS_35_I": ["LATAM"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_passengers_vehicle_distance.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "VEHICLE_DISTANCE_RUSSIA",
    {
        "REGIONS_35_I": ["RUSSIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_passengers_vehicle_distance.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "VEHICLE_DISTANCE_USMCA",
    {
        "REGIONS_35_I": ["USMCA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_initial_passengers_vehicle_distance.add(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "VEHICLE_DISTANCE_LROW",
    {
        "REGIONS_35_I": ["LROW"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)


@component.add(
    name="kW_per_battery_EV",
    units="kW/battery",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_kw_per_battery_ev"},
)
def kw_per_battery_ev():
    """
    Average kW per battery of electrical vehicle.
    """
    return _ext_constant_kw_per_battery_ev()


_ext_constant_kw_per_battery_ev = ExtConstant(
    "model_parameters/energy/energy.xlsm",
    "World",
    "Wattios_per_battery_EV",
    {},
    _root,
    {},
    "_ext_constant_kw_per_battery_ev",
)


@component.add(
    name="lifetime_RES_elec",
    units="Years",
    subscripts=["RES_ELEC_MEDEAS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_lifetime_res_elec"},
)
def lifetime_res_elec():
    """
    Lifetime of each RES technology for electricity generation.
    """
    return _ext_constant_lifetime_res_elec()


_ext_constant_lifetime_res_elec = ExtConstant(
    "model_parameters/energy/energy.xlsm",
    "World",
    "lifetime_RES_elec*",
    {"RES_ELEC_MEDEAS_I": _subscript_dict["RES_ELEC_MEDEAS_I"]},
    _root,
    {"RES_ELEC_MEDEAS_I": _subscript_dict["RES_ELEC_MEDEAS_I"]},
    "_ext_constant_lifetime_res_elec",
)


@component.add(
    name="MAX_LIFETIME_EV_BATTERIES",
    units="Years",
    subscripts=["EV_BATTERIES_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_max_lifetime_ev_batteries"},
)
def max_lifetime_ev_batteries():
    """
    Maximum lifetime of the batteries for electric vehicles if used solely for mobility.
    """
    return _ext_constant_max_lifetime_ev_batteries()


_ext_constant_max_lifetime_ev_batteries = ExtConstant(
    "model_parameters/energy/energy.xlsm",
    "World",
    "max_lifetime_EV_batteries",
    {"EV_BATTERIES_I": ["LMO"]},
    _root,
    {"EV_BATTERIES_I": _subscript_dict["EV_BATTERIES_I"]},
    "_ext_constant_max_lifetime_ev_batteries",
)

_ext_constant_max_lifetime_ev_batteries.add(
    "model_parameters/energy/energy.xlsm",
    "World",
    "max_lifetime_EV_batteries",
    {"EV_BATTERIES_I": ["NMC622"]},
)

_ext_constant_max_lifetime_ev_batteries.add(
    "model_parameters/energy/energy.xlsm",
    "World",
    "max_lifetime_EV_batteries",
    {"EV_BATTERIES_I": ["NMC811"]},
)

_ext_constant_max_lifetime_ev_batteries.add(
    "model_parameters/energy/energy.xlsm",
    "World",
    "max_lifetime_EV_batteries",
    {"EV_BATTERIES_I": ["NCA"]},
)

_ext_constant_max_lifetime_ev_batteries.add(
    "model_parameters/energy/energy.xlsm",
    "World",
    "max_lifetime_EV_batteries",
    {"EV_BATTERIES_I": ["LFP"]},
)


@component.add(
    name="MAXIMUM_PREDICTORS_VARIABILITY_REGRESSION",
    units="DMNL",
    subscripts=["BASIC_PREDICTORS_NGR_VARIABILITY_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_maximum_predictors_variability_regression"
    },
)
def maximum_predictors_variability_regression():
    """
    Maximum value in the range of regression models for the energy variability submodule
    """
    return _ext_constant_maximum_predictors_variability_regression()


_ext_constant_maximum_predictors_variability_regression = ExtConstant(
    "model_parameters/energy/intermittency_coefficients.xlsx",
    "RANGES",
    "MAXIMUM_RANGE_VARIABILITY*",
    {
        "BASIC_PREDICTORS_NGR_VARIABILITY_I": _subscript_dict[
            "BASIC_PREDICTORS_NGR_VARIABILITY_I"
        ]
    },
    _root,
    {
        "BASIC_PREDICTORS_NGR_VARIABILITY_I": _subscript_dict[
            "BASIC_PREDICTORS_NGR_VARIABILITY_I"
        ]
    },
    "_ext_constant_maximum_predictors_variability_regression",
)


@component.add(
    name="MILEAGE_VEHICLES",
    units="km",
    subscripts=["TRANSPORT_POWER_TRAIN_I", "TRANSPORT_MODE_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_mileage_vehicles"},
)
def mileage_vehicles():
    return _ext_constant_mileage_vehicles()


_ext_constant_mileage_vehicles = ExtConstant(
    "model_parameters/energy/energy-transport.xlsx",
    "electrified_transport",
    "MILEAGE_VEHICLES",
    {
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "TRANSPORT_MODE_I": _subscript_dict["TRANSPORT_MODE_I"],
    },
    _root,
    {
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "TRANSPORT_MODE_I": _subscript_dict["TRANSPORT_MODE_I"],
    },
    "_ext_constant_mileage_vehicles",
)


@component.add(
    name="min_lifetime_EV_batteries",
    units="Years",
    subscripts=["EV_BATTERIES_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_min_lifetime_ev_batteries"},
)
def min_lifetime_ev_batteries():
    """
    Minimum lifetime of the batteries for electric vehicles. When used for electricity storage for back-up to the system besides its use for mobility we assume that the lifetime of the battery decreases proportionally to the number of additional cycles.
    """
    return _ext_constant_min_lifetime_ev_batteries()


_ext_constant_min_lifetime_ev_batteries = ExtConstant(
    "model_parameters/energy/energy.xlsm",
    "World",
    "min_lifetime_EV_batteries",
    {"EV_BATTERIES_I": ["LMO"]},
    _root,
    {"EV_BATTERIES_I": _subscript_dict["EV_BATTERIES_I"]},
    "_ext_constant_min_lifetime_ev_batteries",
)

_ext_constant_min_lifetime_ev_batteries.add(
    "model_parameters/energy/energy.xlsm",
    "World",
    "min_lifetime_EV_batteries",
    {"EV_BATTERIES_I": ["NMC622"]},
)

_ext_constant_min_lifetime_ev_batteries.add(
    "model_parameters/energy/energy.xlsm",
    "World",
    "min_lifetime_EV_batteries",
    {"EV_BATTERIES_I": ["NMC811"]},
)

_ext_constant_min_lifetime_ev_batteries.add(
    "model_parameters/energy/energy.xlsm",
    "World",
    "min_lifetime_EV_batteries",
    {"EV_BATTERIES_I": ["NCA"]},
)

_ext_constant_min_lifetime_ev_batteries.add(
    "model_parameters/energy/energy.xlsm",
    "World",
    "min_lifetime_EV_batteries",
    {"EV_BATTERIES_I": ["LFP"]},
)


@component.add(
    name="MINIMUM_PREDICTORS_VARIABILITY_REGRESSION",
    units="DMNL",
    subscripts=["BASIC_PREDICTORS_NGR_VARIABILITY_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_minimum_predictors_variability_regression"
    },
)
def minimum_predictors_variability_regression():
    """
    Minimum value in the range of regression models for the energy variability submodule
    """
    return _ext_constant_minimum_predictors_variability_regression()


_ext_constant_minimum_predictors_variability_regression = ExtConstant(
    "model_parameters/energy/intermittency_coefficients.xlsx",
    "RANGES",
    "MINIMUM_RANGE_VARIABILITY*",
    {
        "BASIC_PREDICTORS_NGR_VARIABILITY_I": _subscript_dict[
            "BASIC_PREDICTORS_NGR_VARIABILITY_I"
        ]
    },
    _root,
    {
        "BASIC_PREDICTORS_NGR_VARIABILITY_I": _subscript_dict[
            "BASIC_PREDICTORS_NGR_VARIABILITY_I"
        ]
    },
    "_ext_constant_minimum_predictors_variability_regression",
)


@component.add(
    name="Net_stored_energy_EV_battery_over_lifetime",
    units="MJ",
    subscripts=["EV_BATTERIES_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_net_stored_energy_ev_battery_over_lifetime"
    },
)
def net_stored_energy_ev_battery_over_lifetime():
    """
    Net stored energy EV battery in whole lifetime.
    """
    return _ext_constant_net_stored_energy_ev_battery_over_lifetime()


_ext_constant_net_stored_energy_ev_battery_over_lifetime = ExtConstant(
    "model_parameters/energy/energy.xlsm",
    "World",
    "Net_stored_energy_EV_battery_over_lifetime",
    {"EV_BATTERIES_I": ["LMO"]},
    _root,
    {"EV_BATTERIES_I": _subscript_dict["EV_BATTERIES_I"]},
    "_ext_constant_net_stored_energy_ev_battery_over_lifetime",
)

_ext_constant_net_stored_energy_ev_battery_over_lifetime.add(
    "model_parameters/energy/energy.xlsm",
    "World",
    "Net_stored_energy_EV_battery_over_lifetime",
    {"EV_BATTERIES_I": ["NMC622"]},
)

_ext_constant_net_stored_energy_ev_battery_over_lifetime.add(
    "model_parameters/energy/energy.xlsm",
    "World",
    "Net_stored_energy_EV_battery_over_lifetime",
    {"EV_BATTERIES_I": ["NMC811"]},
)

_ext_constant_net_stored_energy_ev_battery_over_lifetime.add(
    "model_parameters/energy/energy.xlsm",
    "World",
    "Net_stored_energy_EV_battery_over_lifetime",
    {"EV_BATTERIES_I": ["NCA"]},
)

_ext_constant_net_stored_energy_ev_battery_over_lifetime.add(
    "model_parameters/energy/energy.xlsm",
    "World",
    "Net_stored_energy_EV_battery_over_lifetime",
    {"EV_BATTERIES_I": ["LFP"]},
)


@component.add(
    name='"2w_vehicle_average_price"',
    units="dollars",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_nvs_2w_vehicle_average_price"},
)
def nvs_2w_vehicle_average_price():
    """
    Average price of a new 2 wheleers vehicle
    """
    return _ext_constant_nvs_2w_vehicle_average_price()


_ext_constant_nvs_2w_vehicle_average_price = ExtConstant(
    "model_parameters/energy/energy.xlsm",
    "World",
    "average_price_2w_vehicle",
    {},
    _root,
    {},
    "_ext_constant_nvs_2w_vehicle_average_price",
)


@component.add(
    name='"4w_vehicle_average_price"',
    units="dollars",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_nvs_4w_vehicle_average_price"},
)
def nvs_4w_vehicle_average_price():
    """
    Average price of a new 4 wheleers vehicle
    """
    return _ext_constant_nvs_4w_vehicle_average_price()


_ext_constant_nvs_4w_vehicle_average_price = ExtConstant(
    "model_parameters/energy/energy.xlsm",
    "World",
    "average_price_4w_vehicle",
    {},
    _root,
    {},
    "_ext_constant_nvs_4w_vehicle_average_price",
)


@component.add(
    name="OBJECTIVE_FUEL_CONSUMPTION_EFFICIENCY_CHANGE_SP",
    units="DMNL",
    subscripts=["TRANSPORT_POWER_TRAIN_I", "PASSENGERS_TRANSPORT_MODE_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_objective_fuel_consumption_efficiency_change_sp"
    },
)
def objective_fuel_consumption_efficiency_change_sp():
    return _ext_constant_objective_fuel_consumption_efficiency_change_sp()


_ext_constant_objective_fuel_consumption_efficiency_change_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "OBJECTIVE_FUEL_CONSUMPTION_EFFICIENCY_CHANGE_SP",
    {
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
    _root,
    {
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
    "_ext_constant_objective_fuel_consumption_efficiency_change_sp",
)


@component.add(
    name="OBJECTIVE_LOAD_FACTOR_MOD_SP",
    units="DMNL",
    subscripts=["PRIVATE_TRANSPORT_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_objective_load_factor_mod_sp"},
)
def objective_load_factor_mod_sp():
    return _ext_constant_objective_load_factor_mod_sp()


_ext_constant_objective_load_factor_mod_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "OBJECTIVE_LOAD_FACTOR_MOD_SP*",
    {"PRIVATE_TRANSPORT_I": _subscript_dict["PRIVATE_TRANSPORT_I"]},
    _root,
    {"PRIVATE_TRANSPORT_I": _subscript_dict["PRIVATE_TRANSPORT_I"]},
    "_ext_constant_objective_load_factor_mod_sp",
)


@component.add(
    name="OBJECTIVE_PASSENGER_TRANSPORT_DEMAND_MODAL_SHARE_SP",
    units="DMNL",
    subscripts=[
        "REGIONS_35_I",
        "TRANSPORT_POWER_TRAIN_I",
        "PASSENGERS_TRANSPORT_MODE_I",
    ],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_objective_passenger_transport_demand_modal_share_sp"
    },
)
def objective_passenger_transport_demand_modal_share_sp():
    return _ext_constant_objective_passenger_transport_demand_modal_share_sp()


_ext_constant_objective_passenger_transport_demand_modal_share_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "OBJECTIVE_DEMAND_SHARE_AUSTRIA",
    {
        "REGIONS_35_I": ["AUSTRIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
    "_ext_constant_objective_passenger_transport_demand_modal_share_sp",
)

_ext_constant_objective_passenger_transport_demand_modal_share_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "OBJECTIVE_DEMAND_SHARE_BELGIUM",
    {
        "REGIONS_35_I": ["BELGIUM"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_objective_passenger_transport_demand_modal_share_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "OBJECTIVE_DEMAND_SHARE_BULGARIA",
    {
        "REGIONS_35_I": ["BULGARIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_objective_passenger_transport_demand_modal_share_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "OBJECTIVE_DEMAND_SHARE_CROATIA",
    {
        "REGIONS_35_I": ["CROATIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_objective_passenger_transport_demand_modal_share_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "OBJECTIVE_DEMAND_SHARE_CYPRUS",
    {
        "REGIONS_35_I": ["CYPRUS"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_objective_passenger_transport_demand_modal_share_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "OBJECTIVE_DEMAND_SHARE_CZECH_REPUBLIC",
    {
        "REGIONS_35_I": ["CZECH_REPUBLIC"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_objective_passenger_transport_demand_modal_share_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "OBJECTIVE_DEMAND_SHARE_DENMARK",
    {
        "REGIONS_35_I": ["DENMARK"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_objective_passenger_transport_demand_modal_share_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "OBJECTIVE_DEMAND_SHARE_ESTONIA",
    {
        "REGIONS_35_I": ["ESTONIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_objective_passenger_transport_demand_modal_share_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "OBJECTIVE_DEMAND_SHARE_FINLAND",
    {
        "REGIONS_35_I": ["FINLAND"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_objective_passenger_transport_demand_modal_share_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "OBJECTIVE_DEMAND_SHARE_FRANCE",
    {
        "REGIONS_35_I": ["FRANCE"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_objective_passenger_transport_demand_modal_share_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "OBJECTIVE_DEMAND_SHARE_GERMANY",
    {
        "REGIONS_35_I": ["GERMANY"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_objective_passenger_transport_demand_modal_share_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "OBJECTIVE_DEMAND_SHARE_GREECE",
    {
        "REGIONS_35_I": ["GREECE"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_objective_passenger_transport_demand_modal_share_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "OBJECTIVE_DEMAND_SHARE_HUNGARY",
    {
        "REGIONS_35_I": ["HUNGARY"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_objective_passenger_transport_demand_modal_share_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "OBJECTIVE_DEMAND_SHARE_IRELAND",
    {
        "REGIONS_35_I": ["IRELAND"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_objective_passenger_transport_demand_modal_share_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "OBJECTIVE_DEMAND_SHARE_ITALY",
    {
        "REGIONS_35_I": ["ITALY"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_objective_passenger_transport_demand_modal_share_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "OBJECTIVE_DEMAND_SHARE_LATVIA",
    {
        "REGIONS_35_I": ["LATVIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_objective_passenger_transport_demand_modal_share_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "OBJECTIVE_DEMAND_SHARE_LITHUANIA",
    {
        "REGIONS_35_I": ["LITHUANIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_objective_passenger_transport_demand_modal_share_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "OBJECTIVE_DEMAND_SHARE_LUXEMBOURG",
    {
        "REGIONS_35_I": ["LUXEMBOURG"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_objective_passenger_transport_demand_modal_share_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "OBJECTIVE_DEMAND_SHARE_MALTA",
    {
        "REGIONS_35_I": ["MALTA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_objective_passenger_transport_demand_modal_share_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "OBJECTIVE_DEMAND_SHARE_NETHERLANDS",
    {
        "REGIONS_35_I": ["NETHERLANDS"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_objective_passenger_transport_demand_modal_share_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "OBJECTIVE_DEMAND_SHARE_POLAND",
    {
        "REGIONS_35_I": ["POLAND"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_objective_passenger_transport_demand_modal_share_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "OBJECTIVE_DEMAND_SHARE_PORTUGAL",
    {
        "REGIONS_35_I": ["PORTUGAL"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_objective_passenger_transport_demand_modal_share_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "OBJECTIVE_DEMAND_SHARE_ROMANIA",
    {
        "REGIONS_35_I": ["ROMANIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_objective_passenger_transport_demand_modal_share_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "OBJECTIVE_DEMAND_SHARE_SLOVAKIA",
    {
        "REGIONS_35_I": ["SLOVAKIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_objective_passenger_transport_demand_modal_share_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "OBJECTIVE_DEMAND_SHARE_SLOVENIA",
    {
        "REGIONS_35_I": ["SLOVENIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_objective_passenger_transport_demand_modal_share_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "OBJECTIVE_DEMAND_SHARE_SPAIN",
    {
        "REGIONS_35_I": ["SPAIN"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_objective_passenger_transport_demand_modal_share_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "OBJECTIVE_DEMAND_SHARE_SWEDEN",
    {
        "REGIONS_35_I": ["SWEDEN"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_objective_passenger_transport_demand_modal_share_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "OBJECTIVE_DEMAND_SHARE_UK",
    {
        "REGIONS_35_I": ["UK"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_objective_passenger_transport_demand_modal_share_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "OBJECTIVE_DEMAND_SHARE_CHINA",
    {
        "REGIONS_35_I": ["CHINA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_objective_passenger_transport_demand_modal_share_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "OBJECTIVE_DEMAND_SHARE_EASOC",
    {
        "REGIONS_35_I": ["EASOC"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_objective_passenger_transport_demand_modal_share_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "OBJECTIVE_DEMAND_SHARE_INDIA",
    {
        "REGIONS_35_I": ["INDIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_objective_passenger_transport_demand_modal_share_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "OBJECTIVE_DEMAND_SHARE_LATAM",
    {
        "REGIONS_35_I": ["LATAM"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_objective_passenger_transport_demand_modal_share_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "OBJECTIVE_DEMAND_SHARE_RUSSIA",
    {
        "REGIONS_35_I": ["RUSSIA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_objective_passenger_transport_demand_modal_share_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "OBJECTIVE_DEMAND_SHARE_USMCA",
    {
        "REGIONS_35_I": ["USMCA"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)

_ext_constant_objective_passenger_transport_demand_modal_share_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "OBJECTIVE_DEMAND_SHARE_LROW",
    {
        "REGIONS_35_I": ["LROW"],
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
)


@component.add(
    name="OBJECTIVE_REDUCTION_PASSENGER_TRANSPORT_DEMAND_SP",
    units="1",
    subscripts=["TRANSPORT_POWER_TRAIN_I", "PASSENGERS_TRANSPORT_MODE_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_objective_reduction_passenger_transport_demand_sp"
    },
)
def objective_reduction_passenger_transport_demand_sp():
    return _ext_constant_objective_reduction_passenger_transport_demand_sp()


_ext_constant_objective_reduction_passenger_transport_demand_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "OBJECTIVE_REDUCTION_TRANSPORT_DEMAND_SP",
    {
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
    _root,
    {
        "TRANSPORT_POWER_TRAIN_I": _subscript_dict["TRANSPORT_POWER_TRAIN_I"],
        "PASSENGERS_TRANSPORT_MODE_I": _subscript_dict["PASSENGERS_TRANSPORT_MODE_I"],
    },
    "_ext_constant_objective_reduction_passenger_transport_demand_sp",
)


@component.add(
    name="PE_coal_for_CHP_plants_IEA_EJ",
    units="EJ/Year",
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_pe_coal_for_chp_plants_iea_ej",
        "__data__": "_ext_data_pe_coal_for_chp_plants_iea_ej",
        "time": 1,
    },
)
def pe_coal_for_chp_plants_iea_ej():
    return _ext_data_pe_coal_for_chp_plants_iea_ej(time())


_ext_data_pe_coal_for_chp_plants_iea_ej = ExtData(
    "model_parameters/energy/energy.xlsm",
    "World",
    "time_index",
    "Primary_energy_coal_for_Heat_plants_IOT_EJ",
    "interpolate",
    {},
    _root,
    {},
    "_ext_data_pe_coal_for_chp_plants_iea_ej",
)


@component.add(
    name="PE_demand_coal_Elec_plants_IEA_EJ",
    units="EJ/Year",
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_pe_demand_coal_elec_plants_iea_ej",
        "__data__": "_ext_data_pe_demand_coal_elec_plants_iea_ej",
        "time": 1,
    },
)
def pe_demand_coal_elec_plants_iea_ej():
    return _ext_data_pe_demand_coal_elec_plants_iea_ej(time())


_ext_data_pe_demand_coal_elec_plants_iea_ej = ExtData(
    "model_parameters/energy/energy.xlsm",
    "World",
    "time_index",
    "Primary_energy_coal_for_Elec_plants_IOT_EJ",
    "interpolate",
    {},
    _root,
    {},
    "_ext_data_pe_demand_coal_elec_plants_iea_ej",
)


@component.add(
    name="PE_demand_coal_for_Heat_plants_IEA_EJ",
    units="EJ/Year",
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_pe_demand_coal_for_heat_plants_iea_ej",
        "__data__": "_ext_data_pe_demand_coal_for_heat_plants_iea_ej",
        "time": 1,
    },
)
def pe_demand_coal_for_heat_plants_iea_ej():
    return _ext_data_pe_demand_coal_for_heat_plants_iea_ej(time())


_ext_data_pe_demand_coal_for_heat_plants_iea_ej = ExtData(
    "model_parameters/energy/energy.xlsm",
    "World",
    "time_index",
    "Primary_energy_coal_for_CHP_plants_IOT_EJ",
    "interpolate",
    {},
    _root,
    {},
    "_ext_data_pe_demand_coal_for_heat_plants_iea_ej",
)


@component.add(
    name="PE_demand_for_liquids_Heat_plants_IEA_EJ",
    units="EJ/Year",
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_pe_demand_for_liquids_heat_plants_iea_ej",
        "__data__": "_ext_data_pe_demand_for_liquids_heat_plants_iea_ej",
        "time": 1,
    },
)
def pe_demand_for_liquids_heat_plants_iea_ej():
    return _ext_data_pe_demand_for_liquids_heat_plants_iea_ej(time())


_ext_data_pe_demand_for_liquids_heat_plants_iea_ej = ExtData(
    "model_parameters/energy/energy.xlsm",
    "World",
    "time_index",
    "Primary_energy_liquids_for_CHP_plants_IOT_EJ",
    "interpolate",
    {},
    _root,
    {},
    "_ext_data_pe_demand_for_liquids_heat_plants_iea_ej",
)


@component.add(
    name="PE_demand_gas_Elec_plants_IEA_EJ",
    units="EJ/Year",
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_pe_demand_gas_elec_plants_iea_ej",
        "__data__": "_ext_data_pe_demand_gas_elec_plants_iea_ej",
        "time": 1,
    },
)
def pe_demand_gas_elec_plants_iea_ej():
    return _ext_data_pe_demand_gas_elec_plants_iea_ej(time())


_ext_data_pe_demand_gas_elec_plants_iea_ej = ExtData(
    "model_parameters/energy/energy.xlsm",
    "World",
    "time_index",
    "Primary_energy_gas_for_Elec_plants_IOT_EJ",
    "interpolate",
    {},
    _root,
    {},
    "_ext_data_pe_demand_gas_elec_plants_iea_ej",
)


@component.add(
    name="PE_demand_gases_for_Heat_plants_IEA_EJ",
    units="EJ/Year",
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_pe_demand_gases_for_heat_plants_iea_ej",
        "__data__": "_ext_data_pe_demand_gases_for_heat_plants_iea_ej",
        "time": 1,
    },
)
def pe_demand_gases_for_heat_plants_iea_ej():
    return _ext_data_pe_demand_gases_for_heat_plants_iea_ej(time())


_ext_data_pe_demand_gases_for_heat_plants_iea_ej = ExtData(
    "model_parameters/energy/energy.xlsm",
    "World",
    "time_index",
    "Primary_energy_gas_for_CHP_plants_IOT_EJ",
    "interpolate",
    {},
    _root,
    {},
    "_ext_data_pe_demand_gases_for_heat_plants_iea_ej",
)


@component.add(
    name="PE_demand_liquids_Elec_plants_IEA_EJ",
    units="EJ/Year",
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_pe_demand_liquids_elec_plants_iea_ej",
        "__data__": "_ext_data_pe_demand_liquids_elec_plants_iea_ej",
        "time": 1,
    },
)
def pe_demand_liquids_elec_plants_iea_ej():
    return _ext_data_pe_demand_liquids_elec_plants_iea_ej(time())


_ext_data_pe_demand_liquids_elec_plants_iea_ej = ExtData(
    "model_parameters/energy/energy.xlsm",
    "World",
    "time_index",
    "Primary_energy_liquids_for_Elec_plants_IOT_EJ",
    "interpolate",
    {},
    _root,
    {},
    "_ext_data_pe_demand_liquids_elec_plants_iea_ej",
)


@component.add(
    name="PE_gas_for_CHP_plants_IEA_EJ",
    units="EJ/Year",
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_pe_gas_for_chp_plants_iea_ej",
        "__data__": "_ext_data_pe_gas_for_chp_plants_iea_ej",
        "time": 1,
    },
)
def pe_gas_for_chp_plants_iea_ej():
    return _ext_data_pe_gas_for_chp_plants_iea_ej(time())


_ext_data_pe_gas_for_chp_plants_iea_ej = ExtData(
    "model_parameters/energy/energy.xlsm",
    "World",
    "time_index",
    "Primary_energy_gas_for_Heat_plants_IOT_EJ",
    "interpolate",
    {},
    _root,
    {},
    "_ext_data_pe_gas_for_chp_plants_iea_ej",
)


@component.add(
    name="PE_liquids_for_CHP_plants_IEA_EJ",
    units="EJ/Year",
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_pe_liquids_for_chp_plants_iea_ej",
        "__data__": "_ext_data_pe_liquids_for_chp_plants_iea_ej",
        "time": 1,
    },
)
def pe_liquids_for_chp_plants_iea_ej():
    return _ext_data_pe_liquids_for_chp_plants_iea_ej(time())


_ext_data_pe_liquids_for_chp_plants_iea_ej = ExtData(
    "model_parameters/energy/energy.xlsm",
    "World",
    "time_index",
    "Primary_energy_liquids_for_Heat_plants_IOT_EJ",
    "interpolate",
    {},
    _root,
    {},
    "_ext_data_pe_liquids_for_chp_plants_iea_ej",
)


@component.add(
    name="PROREF_CONVERSION_FACTORS",
    units="DMNL",
    subscripts=["REGIONS_9_I", "NRG_PROREF_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_proref_conversion_factors"},
)
def proref_conversion_factors():
    """
    refinery process transformation efficiencies (oil refinery, coal refinery, bio refinery, gas2hydrogen)
    """
    return _ext_constant_proref_conversion_factors()


_ext_constant_proref_conversion_factors = ExtConstant(
    "model_parameters/energy/energy.xlsm",
    "CHINA",
    "conversion_efficiency_per_refinery_process*",
    {"REGIONS_9_I": ["CHINA"], "NRG_PROREF_I": _subscript_dict["NRG_PROREF_I"]},
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "NRG_PROREF_I": _subscript_dict["NRG_PROREF_I"],
    },
    "_ext_constant_proref_conversion_factors",
)

_ext_constant_proref_conversion_factors.add(
    "model_parameters/energy/energy.xlsm",
    "EASOC",
    "conversion_efficiency_per_refinery_process*",
    {"REGIONS_9_I": ["EASOC"], "NRG_PROREF_I": _subscript_dict["NRG_PROREF_I"]},
)

_ext_constant_proref_conversion_factors.add(
    "model_parameters/energy/energy.xlsm",
    "EU27",
    "conversion_efficiency_per_refinery_process*",
    {"REGIONS_9_I": ["EU27"], "NRG_PROREF_I": _subscript_dict["NRG_PROREF_I"]},
)

_ext_constant_proref_conversion_factors.add(
    "model_parameters/energy/energy.xlsm",
    "INDIA",
    "conversion_efficiency_per_refinery_process*",
    {"REGIONS_9_I": ["INDIA"], "NRG_PROREF_I": _subscript_dict["NRG_PROREF_I"]},
)

_ext_constant_proref_conversion_factors.add(
    "model_parameters/energy/energy.xlsm",
    "LATAM",
    "conversion_efficiency_per_refinery_process*",
    {"REGIONS_9_I": ["LATAM"], "NRG_PROREF_I": _subscript_dict["NRG_PROREF_I"]},
)

_ext_constant_proref_conversion_factors.add(
    "model_parameters/energy/energy.xlsm",
    "LROW",
    "conversion_efficiency_per_refinery_process*",
    {"REGIONS_9_I": ["LROW"], "NRG_PROREF_I": _subscript_dict["NRG_PROREF_I"]},
)

_ext_constant_proref_conversion_factors.add(
    "model_parameters/energy/energy.xlsm",
    "RUSSIA",
    "conversion_efficiency_per_refinery_process*",
    {"REGIONS_9_I": ["RUSSIA"], "NRG_PROREF_I": _subscript_dict["NRG_PROREF_I"]},
)

_ext_constant_proref_conversion_factors.add(
    "model_parameters/energy/energy.xlsm",
    "USMCA",
    "conversion_efficiency_per_refinery_process*",
    {"REGIONS_9_I": ["USMCA"], "NRG_PROREF_I": _subscript_dict["NRG_PROREF_I"]},
)

_ext_constant_proref_conversion_factors.add(
    "model_parameters/energy/energy.xlsm",
    "UK",
    "conversion_efficiency_per_refinery_process*",
    {"REGIONS_9_I": ["UK"], "NRG_PROREF_I": _subscript_dict["NRG_PROREF_I"]},
)


@component.add(
    name="PROREF_INPUT_SHARES_SP",
    units="DMNL",
    subscripts=["REGIONS_9_I", "NRG_PROREF_I", "NRG_PE_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_proref_input_shares_sp"},
)
def proref_input_shares_sp():
    """
    Input-split of the refineration process
    """
    return _ext_constant_proref_input_shares_sp()


_ext_constant_proref_input_shares_sp = ExtConstant(
    "model_parameters/energy/energy.xlsm",
    "Common",
    "primary_energy_shares_of_process_and_commodity",
    {
        "REGIONS_9_I": ["CHINA"],
        "NRG_PROREF_I": _subscript_dict["NRG_PROREF_I"],
        "NRG_PE_I": _subscript_dict["NRG_PE_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "NRG_PROREF_I": _subscript_dict["NRG_PROREF_I"],
        "NRG_PE_I": _subscript_dict["NRG_PE_I"],
    },
    "_ext_constant_proref_input_shares_sp",
)

_ext_constant_proref_input_shares_sp.add(
    "model_parameters/energy/energy.xlsm",
    "Common",
    "primary_energy_shares_of_process_and_commodity",
    {
        "REGIONS_9_I": ["EASOC"],
        "NRG_PROREF_I": _subscript_dict["NRG_PROREF_I"],
        "NRG_PE_I": _subscript_dict["NRG_PE_I"],
    },
)

_ext_constant_proref_input_shares_sp.add(
    "model_parameters/energy/energy.xlsm",
    "Common",
    "primary_energy_shares_of_process_and_commodity",
    {
        "REGIONS_9_I": ["EU27"],
        "NRG_PROREF_I": _subscript_dict["NRG_PROREF_I"],
        "NRG_PE_I": _subscript_dict["NRG_PE_I"],
    },
)

_ext_constant_proref_input_shares_sp.add(
    "model_parameters/energy/energy.xlsm",
    "Common",
    "primary_energy_shares_of_process_and_commodity",
    {
        "REGIONS_9_I": ["INDIA"],
        "NRG_PROREF_I": _subscript_dict["NRG_PROREF_I"],
        "NRG_PE_I": _subscript_dict["NRG_PE_I"],
    },
)

_ext_constant_proref_input_shares_sp.add(
    "model_parameters/energy/energy.xlsm",
    "Common",
    "primary_energy_shares_of_process_and_commodity",
    {
        "REGIONS_9_I": ["LATAM"],
        "NRG_PROREF_I": _subscript_dict["NRG_PROREF_I"],
        "NRG_PE_I": _subscript_dict["NRG_PE_I"],
    },
)

_ext_constant_proref_input_shares_sp.add(
    "model_parameters/energy/energy.xlsm",
    "Common",
    "primary_energy_shares_of_process_and_commodity",
    {
        "REGIONS_9_I": ["LROW"],
        "NRG_PROREF_I": _subscript_dict["NRG_PROREF_I"],
        "NRG_PE_I": _subscript_dict["NRG_PE_I"],
    },
)

_ext_constant_proref_input_shares_sp.add(
    "model_parameters/energy/energy.xlsm",
    "Common",
    "primary_energy_shares_of_process_and_commodity",
    {
        "REGIONS_9_I": ["RUSSIA"],
        "NRG_PROREF_I": _subscript_dict["NRG_PROREF_I"],
        "NRG_PE_I": _subscript_dict["NRG_PE_I"],
    },
)

_ext_constant_proref_input_shares_sp.add(
    "model_parameters/energy/energy.xlsm",
    "Common",
    "primary_energy_shares_of_process_and_commodity",
    {
        "REGIONS_9_I": ["UK"],
        "NRG_PROREF_I": _subscript_dict["NRG_PROREF_I"],
        "NRG_PE_I": _subscript_dict["NRG_PE_I"],
    },
)

_ext_constant_proref_input_shares_sp.add(
    "model_parameters/energy/energy.xlsm",
    "Common",
    "primary_energy_shares_of_process_and_commodity",
    {
        "REGIONS_9_I": ["USMCA"],
        "NRG_PROREF_I": _subscript_dict["NRG_PROREF_I"],
        "NRG_PE_I": _subscript_dict["NRG_PE_I"],
    },
)


@component.add(
    name="PROREF_OUTPUT_SHARES",
    units="DMNL",
    subscripts=["REGIONS_9_I", "NRG_TI_I", "NRG_PROREF_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_proref_output_shares"},
)
def proref_output_shares():
    """
    How much individual processes contribute to total TI.
    """
    return _ext_constant_proref_output_shares()


_ext_constant_proref_output_shares = ExtConstant(
    "model_parameters/energy/energy.xlsm",
    "CHINA",
    "process_refinery_required_shares_of_process_and_commodity_max",
    {
        "REGIONS_9_I": ["CHINA"],
        "NRG_TI_I": _subscript_dict["NRG_TI_I"],
        "NRG_PROREF_I": _subscript_dict["NRG_PROREF_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "NRG_TI_I": _subscript_dict["NRG_TI_I"],
        "NRG_PROREF_I": _subscript_dict["NRG_PROREF_I"],
    },
    "_ext_constant_proref_output_shares",
)

_ext_constant_proref_output_shares.add(
    "model_parameters/energy/energy.xlsm",
    "EASOC",
    "process_refinery_required_shares_of_process_and_commodity_max",
    {
        "REGIONS_9_I": ["EASOC"],
        "NRG_TI_I": _subscript_dict["NRG_TI_I"],
        "NRG_PROREF_I": _subscript_dict["NRG_PROREF_I"],
    },
)

_ext_constant_proref_output_shares.add(
    "model_parameters/energy/energy.xlsm",
    "EU27",
    "process_refinery_required_shares_of_process_and_commodity_max",
    {
        "REGIONS_9_I": ["EU27"],
        "NRG_TI_I": _subscript_dict["NRG_TI_I"],
        "NRG_PROREF_I": _subscript_dict["NRG_PROREF_I"],
    },
)

_ext_constant_proref_output_shares.add(
    "model_parameters/energy/energy.xlsm",
    "INDIA",
    "process_refinery_required_shares_of_process_and_commodity_max",
    {
        "REGIONS_9_I": ["INDIA"],
        "NRG_TI_I": _subscript_dict["NRG_TI_I"],
        "NRG_PROREF_I": _subscript_dict["NRG_PROREF_I"],
    },
)

_ext_constant_proref_output_shares.add(
    "model_parameters/energy/energy.xlsm",
    "LATAM",
    "process_refinery_required_shares_of_process_and_commodity_max",
    {
        "REGIONS_9_I": ["LATAM"],
        "NRG_TI_I": _subscript_dict["NRG_TI_I"],
        "NRG_PROREF_I": _subscript_dict["NRG_PROREF_I"],
    },
)

_ext_constant_proref_output_shares.add(
    "model_parameters/energy/energy.xlsm",
    "LROW",
    "process_refinery_required_shares_of_process_and_commodity_max",
    {
        "REGIONS_9_I": ["LROW"],
        "NRG_TI_I": _subscript_dict["NRG_TI_I"],
        "NRG_PROREF_I": _subscript_dict["NRG_PROREF_I"],
    },
)

_ext_constant_proref_output_shares.add(
    "model_parameters/energy/energy.xlsm",
    "RUSSIA",
    "process_refinery_required_shares_of_process_and_commodity_max",
    {
        "REGIONS_9_I": ["RUSSIA"],
        "NRG_TI_I": _subscript_dict["NRG_TI_I"],
        "NRG_PROREF_I": _subscript_dict["NRG_PROREF_I"],
    },
)

_ext_constant_proref_output_shares.add(
    "model_parameters/energy/energy.xlsm",
    "UK",
    "process_refinery_required_shares_of_process_and_commodity_max",
    {
        "REGIONS_9_I": ["UK"],
        "NRG_TI_I": _subscript_dict["NRG_TI_I"],
        "NRG_PROREF_I": _subscript_dict["NRG_PROREF_I"],
    },
)

_ext_constant_proref_output_shares.add(
    "model_parameters/energy/energy.xlsm",
    "USMCA",
    "process_refinery_required_shares_of_process_and_commodity_max",
    {
        "REGIONS_9_I": ["USMCA"],
        "NRG_TI_I": _subscript_dict["NRG_TI_I"],
        "NRG_PROREF_I": _subscript_dict["NRG_PROREF_I"],
    },
)


@component.add(
    name='"RES_elec_variables?"',
    units="DMNL",
    subscripts=["RES_ELEC_MEDEAS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_res_elec_variables"},
)
def res_elec_variables():
    """
    Vector to distinguis between RES elec variables and dispatchables: *If=1, RES elec variables (fully endogenous calculation from the materials requirements). *If=0, RES elec dispatchables (partially endogenous calculation requiring a value of EROI as starting point).
    """
    return _ext_constant_res_elec_variables()


_ext_constant_res_elec_variables = ExtConstant(
    "model_parameters/energy/energy.xlsm",
    "World",
    "RES_elec_variables*",
    {"RES_ELEC_MEDEAS_I": _subscript_dict["RES_ELEC_MEDEAS_I"]},
    _root,
    {"RES_ELEC_MEDEAS_I": _subscript_dict["RES_ELEC_MEDEAS_I"]},
    "_ext_constant_res_elec_variables",
)


@component.add(
    name="RT_STORAGE_EFFICIENCY_EV_BATTERIES",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_rt_storage_efficiency_ev_batteries"},
)
def rt_storage_efficiency_ev_batteries():
    """
    Round-trip storage efficiency of electric batteries frome electric vehicles.
    """
    return _ext_constant_rt_storage_efficiency_ev_batteries()


_ext_constant_rt_storage_efficiency_ev_batteries = ExtConstant(
    "model_parameters/energy/energy.xlsm",
    "World",
    "Round_trip_storage_efficiency_EV_batteries",
    {},
    _root,
    {},
    "_ext_constant_rt_storage_efficiency_ev_batteries",
)


@component.add(
    name="RT_STORAGE_EFFICIENCY_PHS",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_rt_storage_efficiency_phs"},
)
def rt_storage_efficiency_phs():
    """
    Round-trip storage efficiency.
    """
    return _ext_constant_rt_storage_efficiency_phs()


_ext_constant_rt_storage_efficiency_phs = ExtConstant(
    "model_parameters/energy/energy.xlsm",
    "World",
    "Round_trip_storage_efficiency_PHS",
    {},
    _root,
    {},
    "_ext_constant_rt_storage_efficiency_phs",
)


@component.add(
    name="SELECT_URANIUM_MAXIMUM_SUPPLY_CURVE_SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_select_uranium_maximum_supply_curve_sp"},
)
def select_uranium_maximum_supply_curve_sp():
    """
    Select uranium maximum supply curve from literature, or user-defined.
    """
    return _ext_constant_select_uranium_maximum_supply_curve_sp()


_ext_constant_select_uranium_maximum_supply_curve_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "materials",
    "SELECT_URANIUM_MAX_SUPPLY_CURVE_SP",
    {},
    _root,
    {},
    "_ext_constant_select_uranium_maximum_supply_curve_sp",
)


@component.add(
    name="share_Coal_Elec_IEA",
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_share_coal_elec_iea",
        "__data__": "_ext_data_share_coal_elec_iea",
        "time": 1,
    },
)
def share_coal_elec_iea():
    return _ext_data_share_coal_elec_iea(time())


_ext_data_share_coal_elec_iea = ExtData(
    "model_parameters/energy/energy.xlsm",
    "World",
    "time_index",
    "Memo_Coal_peat_and_oil_shale_Elec",
    None,
    {},
    _root,
    {},
    "_ext_data_share_coal_elec_iea",
)


@component.add(
    name="share_coal_Heat_IEA_EJ",
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_share_coal_heat_iea_ej",
        "__data__": "_ext_data_share_coal_heat_iea_ej",
        "time": 1,
    },
)
def share_coal_heat_iea_ej():
    return _ext_data_share_coal_heat_iea_ej(time())


_ext_data_share_coal_heat_iea_ej = ExtData(
    "model_parameters/energy/energy.xlsm",
    "World",
    "time_index",
    "Memo_Coal_peat_and_oil_shale_Heat",
    None,
    {},
    _root,
    {},
    "_ext_data_share_coal_heat_iea_ej",
)


@component.add(
    name="SHARE_ELEC_IN_PHEV",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_share_elec_in_phev"},
)
def share_elec_in_phev():
    """
    Share of electricity consumption in PHEV power trains.
    """
    return _ext_constant_share_elec_in_phev()


_ext_constant_share_elec_in_phev = ExtConstant(
    "model_parameters/energy/energy-transport.xlsx",
    "Data",
    "SHARE_ELEC_IN_PHEV",
    {},
    _root,
    {},
    "_ext_constant_share_elec_in_phev",
)


@component.add(
    name="share_fossil_fuel_CHP_IEA_EJ",
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_share_fossil_fuel_chp_iea_ej",
        "__data__": "_ext_data_share_fossil_fuel_chp_iea_ej",
        "time": 1,
    },
)
def share_fossil_fuel_chp_iea_ej():
    return _ext_data_share_fossil_fuel_chp_iea_ej(time())


_ext_data_share_fossil_fuel_chp_iea_ej = ExtData(
    "model_parameters/energy/energy.xlsm",
    "World",
    "time_index",
    "Fossil_Fuel_CHP_Heat",
    None,
    {},
    _root,
    {},
    "_ext_data_share_fossil_fuel_chp_iea_ej",
)


@component.add(
    name="share_fossil_fuel_Elec_CHP_IEA",
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_share_fossil_fuel_elec_chp_iea",
        "__data__": "_ext_data_share_fossil_fuel_elec_chp_iea",
        "time": 1,
    },
)
def share_fossil_fuel_elec_chp_iea():
    return _ext_data_share_fossil_fuel_elec_chp_iea(time())


_ext_data_share_fossil_fuel_elec_chp_iea = ExtData(
    "model_parameters/energy/energy.xlsm",
    "World",
    "time_index",
    "Fossil_fuel_CHP_Elec",
    None,
    {},
    _root,
    {},
    "_ext_data_share_fossil_fuel_elec_chp_iea",
)


@component.add(
    name="share_gases_Elec_IEA",
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_share_gases_elec_iea",
        "__data__": "_ext_data_share_gases_elec_iea",
        "time": 1,
    },
)
def share_gases_elec_iea():
    return _ext_data_share_gases_elec_iea(time())


_ext_data_share_gases_elec_iea = ExtData(
    "model_parameters/energy/energy.xlsm",
    "World",
    "time_index",
    "Natural_gas_Elec",
    None,
    {},
    _root,
    {},
    "_ext_data_share_gases_elec_iea",
)


@component.add(
    name="share_gases_Heat_IEA_EJ",
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_share_gases_heat_iea_ej",
        "__data__": "_ext_data_share_gases_heat_iea_ej",
        "time": 1,
    },
)
def share_gases_heat_iea_ej():
    return _ext_data_share_gases_heat_iea_ej(time())


_ext_data_share_gases_heat_iea_ej = ExtData(
    "model_parameters/energy/energy.xlsm",
    "World",
    "time_index",
    "Natural_gas_Heat",
    None,
    {},
    _root,
    {},
    "_ext_data_share_gases_heat_iea_ej",
)


@component.add(
    name="share_liquids_Elec_IEA",
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_share_liquids_elec_iea",
        "__data__": "_ext_data_share_liquids_elec_iea",
        "time": 1,
    },
)
def share_liquids_elec_iea():
    return _ext_data_share_liquids_elec_iea(time())


_ext_data_share_liquids_elec_iea = ExtData(
    "model_parameters/energy/energy.xlsm",
    "World",
    "time_index",
    "Memo_Primary_and_secondary_oil_Elec",
    None,
    {},
    _root,
    {},
    "_ext_data_share_liquids_elec_iea",
)


@component.add(
    name="share_liquids_Heat_IEA_EJ",
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_share_liquids_heat_iea_ej",
        "__data__": "_ext_data_share_liquids_heat_iea_ej",
        "time": 1,
    },
)
def share_liquids_heat_iea_ej():
    return _ext_data_share_liquids_heat_iea_ej(time())


_ext_data_share_liquids_heat_iea_ej = ExtData(
    "model_parameters/energy/energy.xlsm",
    "World",
    "time_index",
    "Memo_Primary_and_secondary_oil_Heat",
    None,
    {},
    _root,
    {},
    "_ext_data_share_liquids_heat_iea_ej",
)


@component.add(
    name="share_Nuclear_Elec_IEA",
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_share_nuclear_elec_iea",
        "__data__": "_ext_data_share_nuclear_elec_iea",
        "time": 1,
    },
)
def share_nuclear_elec_iea():
    return _ext_data_share_nuclear_elec_iea(time())


_ext_data_share_nuclear_elec_iea = ExtData(
    "model_parameters/energy/energy.xlsm",
    "World",
    "time_index",
    "Nuclear_Elec",
    None,
    {},
    _root,
    {},
    "_ext_data_share_nuclear_elec_iea",
)


@component.add(
    name="share_nuclear_Heat_IEA_EJ",
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_share_nuclear_heat_iea_ej",
        "__data__": "_ext_data_share_nuclear_heat_iea_ej",
        "time": 1,
    },
)
def share_nuclear_heat_iea_ej():
    return _ext_data_share_nuclear_heat_iea_ej(time())


_ext_data_share_nuclear_heat_iea_ej = ExtData(
    "model_parameters/energy/energy.xlsm",
    "World",
    "time_index",
    "Nuclear_Heat",
    None,
    {},
    _root,
    {},
    "_ext_data_share_nuclear_heat_iea_ej",
)


@component.add(
    name="share_renewables_Elec_CHP_IEA",
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_share_renewables_elec_chp_iea",
        "__data__": "_ext_data_share_renewables_elec_chp_iea",
        "time": 1,
    },
)
def share_renewables_elec_chp_iea():
    return _ext_data_share_renewables_elec_chp_iea(time())


_ext_data_share_renewables_elec_chp_iea = ExtData(
    "model_parameters/energy/energy.xlsm",
    "World",
    "time_index",
    "Renewables_CHP_Elec",
    None,
    {},
    _root,
    {},
    "_ext_data_share_renewables_elec_chp_iea",
)


@component.add(
    name="share_Renewables_Elec_IEA",
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_share_renewables_elec_iea",
        "__data__": "_ext_data_share_renewables_elec_iea",
        "time": 1,
    },
)
def share_renewables_elec_iea():
    return _ext_data_share_renewables_elec_iea(time())


_ext_data_share_renewables_elec_iea = ExtData(
    "model_parameters/energy/energy.xlsm",
    "World",
    "time_index",
    "Memo_Renewables_Elec",
    None,
    {},
    _root,
    {},
    "_ext_data_share_renewables_elec_iea",
)


@component.add(
    name="share_renewables_fuel_CHP_IEA_EJ",
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_share_renewables_fuel_chp_iea_ej",
        "__data__": "_ext_data_share_renewables_fuel_chp_iea_ej",
        "time": 1,
    },
)
def share_renewables_fuel_chp_iea_ej():
    return _ext_data_share_renewables_fuel_chp_iea_ej(time())


_ext_data_share_renewables_fuel_chp_iea_ej = ExtData(
    "model_parameters/energy/energy.xlsm",
    "World",
    "time_index",
    "Renewables_CHP_Heat",
    None,
    {},
    _root,
    {},
    "_ext_data_share_renewables_fuel_chp_iea_ej",
)


@component.add(
    name="share_renewables_Heat_IEA_EJ",
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_share_renewables_heat_iea_ej",
        "__data__": "_ext_data_share_renewables_heat_iea_ej",
        "time": 1,
    },
)
def share_renewables_heat_iea_ej():
    return _ext_data_share_renewables_heat_iea_ej(time())


_ext_data_share_renewables_heat_iea_ej = ExtData(
    "model_parameters/energy/energy.xlsm",
    "World",
    "time_index",
    "Renewables_Heat",
    None,
    {},
    _root,
    {},
    "_ext_data_share_renewables_heat_iea_ej",
)


@component.add(
    name="SWITCH_computation_static_EROI",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_computation_static_eroi"},
)
def switch_computation_static_eroi():
    """
    This variable activates the computation of the 'static' EROIst by technology: 0. 'Dynamic' EROI calculation (endogenous) 1. 'Static' EROIst calculation (recycling rate of minerals constant at 2015 levels, "Take into account of RES variability?"=0, do not include material requirements for overgrids, "FEI elec storage"=0).
    """
    return _ext_constant_switch_computation_static_eroi()


_ext_constant_switch_computation_static_eroi = ExtConstant(
    "model_parameters/energy/energy.xlsm",
    "World",
    "Computation_static_EROIst?",
    {},
    _root,
    {},
    "_ext_constant_switch_computation_static_eroi",
)


@component.add(
    name="SWITCH_FUEL_CONSUMPTION_EFFICIENCY_CHANGE_SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_switch_fuel_consumption_efficiency_change_sp"
    },
)
def switch_fuel_consumption_efficiency_change_sp():
    return _ext_constant_switch_fuel_consumption_efficiency_change_sp()


_ext_constant_switch_fuel_consumption_efficiency_change_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "SWITCH_FUEL_CONSUMPTION_EFFICIENCY_CHANGE_SP",
    {},
    _root,
    {},
    "_ext_constant_switch_fuel_consumption_efficiency_change_sp",
)


@component.add(
    name="SWITCH_LOAD_FACTOR_MOD_SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_load_factor_mod_sp"},
)
def switch_load_factor_mod_sp():
    """
    1: deactivate policy the scenario parameter 0: Activate the scenario parameter
    """
    return _ext_constant_switch_load_factor_mod_sp()


_ext_constant_switch_load_factor_mod_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "SWITCH_LOAD_FACTOR_MOD_SP",
    {},
    _root,
    {},
    "_ext_constant_switch_load_factor_mod_sp",
)


@component.add(
    name="SWITCH_PASSENGER_TRANSPORT_MODAL_SHARE_SP",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_switch_passenger_transport_modal_share_sp"
    },
)
def switch_passenger_transport_modal_share_sp():
    return _ext_constant_switch_passenger_transport_modal_share_sp()


_ext_constant_switch_passenger_transport_modal_share_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "SWITCH_TRANSPORT_SHARE_SP",
    {},
    _root,
    {},
    "_ext_constant_switch_passenger_transport_modal_share_sp",
)


@component.add(
    name="SWITCH_REDUCTION_PASSENGER_TRANSPORT_DEMAND_SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_switch_reduction_passenger_transport_demand_sp"
    },
)
def switch_reduction_passenger_transport_demand_sp():
    return _ext_constant_switch_reduction_passenger_transport_demand_sp()


_ext_constant_switch_reduction_passenger_transport_demand_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "SWITCH_REDUCTION_TRANSPORT_DEMAND_SP",
    {},
    _root,
    {},
    "_ext_constant_switch_reduction_passenger_transport_demand_sp",
)


@component.add(
    name="TABLE_MAX_EXTRACTION_EWG2006",
    units="EJ/Year",
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_table_max_extraction_ewg2006",
        "__lookup__": "_ext_lookup_table_max_extraction_ewg2006",
    },
)
def table_max_extraction_ewg2006(x, final_subs=None):
    return _ext_lookup_table_max_extraction_ewg2006(x, final_subs)


_ext_lookup_table_max_extraction_ewg2006 = ExtLookup(
    "model_parameters/energy/energy.xlsm",
    "World",
    "RURR_uranium_EWG06",
    "MAXIMUM_EXTRACTION_URANIUM_EWG06",
    {},
    _root,
    {},
    "_ext_lookup_table_max_extraction_ewg2006",
)


@component.add(
    name="TABLE_MAX_EXTRACTION_URANIUM_USER_DEFINED_SP",
    units="EJ/Year",
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_table_max_extraction_uranium_user_defined_sp",
        "__lookup__": "_ext_lookup_table_max_extraction_uranium_user_defined_sp",
    },
)
def table_max_extraction_uranium_user_defined_sp(x, final_subs=None):
    """
    Maximum global supply curve for uranium defined by the model user.
    """
    return _ext_lookup_table_max_extraction_uranium_user_defined_sp(x, final_subs)


_ext_lookup_table_max_extraction_uranium_user_defined_sp = ExtLookup(
    "scenario_parameters/scenario_parameters.xlsx",
    "materials",
    "RURR_URANIUM_USER_DEFINED_SP",
    "MAXIMUM_EXTRACTION_URANIUM_USER_DEFINED_SP",
    {},
    _root,
    {},
    "_ext_lookup_table_max_extraction_uranium_user_defined_sp",
)


@component.add(
    name="TABLE_MAX_EXTRACTION_URANIUM_ZITTEL2012",
    units="EJ/Year",
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_table_max_extraction_uranium_zittel2012",
        "__lookup__": "_ext_lookup_table_max_extraction_uranium_zittel2012",
    },
)
def table_max_extraction_uranium_zittel2012(x, final_subs=None):
    return _ext_lookup_table_max_extraction_uranium_zittel2012(x, final_subs)


_ext_lookup_table_max_extraction_uranium_zittel2012 = ExtLookup(
    "model_parameters/energy/energy.xlsm",
    "World",
    "Zittel12_uranium_remaining",
    "Zittel12_uranium_extraction",
    {},
    _root,
    {},
    "_ext_lookup_table_max_extraction_uranium_zittel2012",
)


@component.add(
    name="TABLE_MAXIMUM_EXTRACTION_URANIUM_EWG2013",
    units="EJ/Year",
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_table_maximum_extraction_uranium_ewg2013",
        "__lookup__": "_ext_lookup_table_maximum_extraction_uranium_ewg2013",
    },
)
def table_maximum_extraction_uranium_ewg2013(x, final_subs=None):
    return _ext_lookup_table_maximum_extraction_uranium_ewg2013(x, final_subs)


_ext_lookup_table_maximum_extraction_uranium_ewg2013 = ExtLookup(
    "model_parameters/energy/energy.xlsm",
    "World",
    "EWG13_Uranium_remaining",
    "EWG13_Uranium_extraction",
    {},
    _root,
    {},
    "_ext_lookup_table_maximum_extraction_uranium_ewg2013",
)


@component.add(
    name="URR_URANIUM_EWG2006",
    units="EJ",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_urr_uranium_ewg2006"},
)
def urr_uranium_ewg2006():
    return _ext_constant_urr_uranium_ewg2006()


_ext_constant_urr_uranium_ewg2006 = ExtConstant(
    "model_parameters/energy/energy.xlsm",
    "World",
    "URR_EWG06",
    {},
    _root,
    {},
    "_ext_constant_urr_uranium_ewg2006",
)


@component.add(
    name="URR_URANIUM_EWG2013",
    units="EJ",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_urr_uranium_ewg2013"},
)
def urr_uranium_ewg2013():
    """
    3900 Según [EWG2013] (curvas_recursos.xlsx).
    """
    return _ext_constant_urr_uranium_ewg2013()


_ext_constant_urr_uranium_ewg2013 = ExtConstant(
    "model_parameters/energy/energy.xlsm",
    "World",
    "EWG13_Uranium",
    {},
    _root,
    {},
    "_ext_constant_urr_uranium_ewg2013",
)


@component.add(
    name="URR_URANIUM_USER_DEFINED",
    units="EJ",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_urr_uranium_user_defined"},
)
def urr_uranium_user_defined():
    return _ext_constant_urr_uranium_user_defined()


_ext_constant_urr_uranium_user_defined = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "materials",
    "USER_DEFINED_URANIUM_URR",
    {},
    _root,
    {},
    "_ext_constant_urr_uranium_user_defined",
)


@component.add(
    name="URR_URANIUM_ZITTEL2012",
    units="EJ",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_urr_uranium_zittel2012"},
)
def urr_uranium_zittel2012():
    return _ext_constant_urr_uranium_zittel2012()


_ext_constant_urr_uranium_zittel2012 = ExtConstant(
    "model_parameters/energy/energy.xlsm",
    "World",
    "Zittel12_uranium",
    {},
    _root,
    {},
    "_ext_constant_urr_uranium_zittel2012",
)


@component.add(
    name="YEAR_FINAL_FUEL_CONSUMPTION_EFFICIENCY_CHANGE_SP",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_year_final_fuel_consumption_efficiency_change_sp"
    },
)
def year_final_fuel_consumption_efficiency_change_sp():
    return _ext_constant_year_final_fuel_consumption_efficiency_change_sp()


_ext_constant_year_final_fuel_consumption_efficiency_change_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "YEAR_FINAL_FUEL_CONSUMPTION_EFFICIENCY_CHANGE_SP",
    {},
    _root,
    {},
    "_ext_constant_year_final_fuel_consumption_efficiency_change_sp",
)


@component.add(
    name="YEAR_FINAL_LOAD_FACTOR_MOD_SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_year_final_load_factor_mod_sp"},
)
def year_final_load_factor_mod_sp():
    return _ext_constant_year_final_load_factor_mod_sp()


_ext_constant_year_final_load_factor_mod_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "YEAR_FINAL_LOAD_FACTOR_MOD_SP",
    {},
    _root,
    {},
    "_ext_constant_year_final_load_factor_mod_sp",
)


@component.add(
    name="YEAR_FINAL_PASSENGER_TRANSPORT_SHARE_SP",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_year_final_passenger_transport_share_sp"
    },
)
def year_final_passenger_transport_share_sp():
    return _ext_constant_year_final_passenger_transport_share_sp()


_ext_constant_year_final_passenger_transport_share_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "YEAR_FINAL_TRANSPORT_SHARE_SP",
    {},
    _root,
    {},
    "_ext_constant_year_final_passenger_transport_share_sp",
)


@component.add(
    name="YEAR_FINAL_REDUCTION_PASSENGER_TRANSPORT_DEMAND_SP",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_year_final_reduction_passenger_transport_demand_sp"
    },
)
def year_final_reduction_passenger_transport_demand_sp():
    return _ext_constant_year_final_reduction_passenger_transport_demand_sp()


_ext_constant_year_final_reduction_passenger_transport_demand_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "YEAR_FINAL_REDUCTION_TRANSPORT_DEMAND_SP",
    {},
    _root,
    {},
    "_ext_constant_year_final_reduction_passenger_transport_demand_sp",
)


@component.add(
    name="YEAR_INITIAL_FUEL_CONSUMPTION_EFFICIENCY_CHANGE_SP",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_year_initial_fuel_consumption_efficiency_change_sp"
    },
)
def year_initial_fuel_consumption_efficiency_change_sp():
    return _ext_constant_year_initial_fuel_consumption_efficiency_change_sp()


_ext_constant_year_initial_fuel_consumption_efficiency_change_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "YEAR_INITIAL_FUEL_CONSUMPTION_EFFICIENCY_CHANGE_SP",
    {},
    _root,
    {},
    "_ext_constant_year_initial_fuel_consumption_efficiency_change_sp",
)


@component.add(
    name="YEAR_INITIAL_LOAD_FACTOR_MOD_SP",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_year_initial_load_factor_mod_sp"},
)
def year_initial_load_factor_mod_sp():
    return _ext_constant_year_initial_load_factor_mod_sp()


_ext_constant_year_initial_load_factor_mod_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "YEAR_INITIAL_LOAD_FACTOR_MOD_SP",
    {},
    _root,
    {},
    "_ext_constant_year_initial_load_factor_mod_sp",
)


@component.add(
    name="YEAR_INITIAL_PASSENGER_TRANSPORT_SHARE_SP",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_year_initial_passenger_transport_share_sp"
    },
)
def year_initial_passenger_transport_share_sp():
    """
    Start year of the modal share modification policy
    """
    return _ext_constant_year_initial_passenger_transport_share_sp()


_ext_constant_year_initial_passenger_transport_share_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "YEAR_INITIAL_TRANSPORT_SHARE_SP",
    {},
    _root,
    {},
    "_ext_constant_year_initial_passenger_transport_share_sp",
)


@component.add(
    name="YEAR_INITIAL_REDUCTION_PASSENGER_TRANSPORT_DEMAND_SP",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_year_initial_reduction_passenger_transport_demand_sp"
    },
)
def year_initial_reduction_passenger_transport_demand_sp():
    return _ext_constant_year_initial_reduction_passenger_transport_demand_sp()


_ext_constant_year_initial_reduction_passenger_transport_demand_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "YEAR_INITIAL_REDUCTION_TRANSPORT_DEMAND_SP",
    {},
    _root,
    {},
    "_ext_constant_year_initial_reduction_passenger_transport_demand_sp",
)
