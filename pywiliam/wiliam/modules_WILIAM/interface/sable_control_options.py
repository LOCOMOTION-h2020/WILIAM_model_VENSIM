"""
Module interface.sable_control_options
Translated using PySD version 3.10.0
"""


@component.add(
    name="Activate_all_fuels_start_year_policy",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_activate_all_fuels_start_year_policy"},
)
def activate_all_fuels_start_year_policy():
    """
    Sable switch to change start year policy for all final fuels at once 0= read the inputs excel variables for each final fuel 1= "star year efficiency policy" variable change year for all final fuels at once
    """
    return _ext_constant_activate_all_fuels_start_year_policy()


_ext_constant_activate_all_fuels_start_year_policy = ExtConstant(
    "model_parameters/sable.xlsx",
    "World",
    "Switch_Sable_or_excel_read",
    {},
    _root,
    {},
    "_ext_constant_activate_all_fuels_start_year_policy",
)


@component.add(
    name="Coal_availability",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_coal_availability"},
)
def coal_availability():
    """
    Dummy variable for the model interface in SABLE software
    """
    return _ext_constant_coal_availability()


_ext_constant_coal_availability = ExtConstant(
    "model_parameters/sable.xlsx",
    "World",
    "Coal",
    {},
    _root,
    {},
    "_ext_constant_coal_availability",
)


@component.add(
    name="Gas_availability",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_gas_availability"},
)
def gas_availability():
    """
    Dummy variable for the model interface in SABLE software
    """
    return _ext_constant_gas_availability()


_ext_constant_gas_availability = ExtConstant(
    "model_parameters/sable.xlsx",
    "World",
    "Gas",
    {},
    _root,
    {},
    "_ext_constant_gas_availability",
)


@component.add(
    name="Hypothesis_1",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_hypothesis_1"},
)
def hypothesis_1():
    """
    Dummy variable for the model interface in SABLE software
    """
    return _ext_constant_hypothesis_1()


_ext_constant_hypothesis_1 = ExtConstant(
    "model_parameters/sable.xlsx",
    "World",
    "H1_sable",
    {},
    _root,
    {},
    "_ext_constant_hypothesis_1",
)


@component.add(
    name="Hypothesis_2",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_hypothesis_2"},
)
def hypothesis_2():
    """
    Dummy variable for the model interface in SABLE software
    """
    return _ext_constant_hypothesis_2()


_ext_constant_hypothesis_2 = ExtConstant(
    "model_parameters/sable.xlsx",
    "World",
    "H2_sable",
    {},
    _root,
    {},
    "_ext_constant_hypothesis_2",
)


@component.add(
    name="Oil_availability",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_oil_availability"},
)
def oil_availability():
    """
    Dummy variable for the model interface in SABLE software
    """
    return _ext_constant_oil_availability()


_ext_constant_oil_availability = ExtConstant(
    "model_parameters/sable.xlsx",
    "World",
    "Oil",
    {},
    _root,
    {},
    "_ext_constant_oil_availability",
)


@component.add(
    name="SABLE_interface_FEC_objective",
    units="GJ/(Year*person)",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_sable_interface_fec_objective"},
)
def sable_interface_fec_objective():
    """
    Dummy variable for the model interface in SABLE software
    """
    return _ext_constant_sable_interface_fec_objective()


_ext_constant_sable_interface_fec_objective = ExtConstant(
    "model_parameters/sable.xlsx",
    "World",
    "FEC",
    {},
    _root,
    {},
    "_ext_constant_sable_interface_fec_objective",
)


@component.add(
    name="Sable_Postgrowth_Matrix_W",
    units="DMNL",
    subscripts=["SECTORS_MEDEAS_I", "SECTORS1_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_sable_postgrowth_matrix_w"},
)
def sable_postgrowth_matrix_w():
    return _ext_constant_sable_postgrowth_matrix_w()


_ext_constant_sable_postgrowth_matrix_w = ExtConstant(
    "model_parameters/sable.xlsx",
    "World",
    "sable_postgrowth_matrix",
    {
        "SECTORS_MEDEAS_I": _subscript_dict["SECTORS_MEDEAS_I"],
        "SECTORS1_I": _subscript_dict["SECTORS1_I"],
    },
    _root,
    {
        "SECTORS_MEDEAS_I": _subscript_dict["SECTORS_MEDEAS_I"],
        "SECTORS1_I": _subscript_dict["SECTORS1_I"],
    },
    "_ext_constant_sable_postgrowth_matrix_w",
)


@component.add(
    name="Start_year_efficiency_H_policy",
    units="Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_start_year_efficiency_h_policy"},
)
def start_year_efficiency_h_policy():
    """
    Start year efficiency policy
    """
    return _ext_constant_start_year_efficiency_h_policy()


_ext_constant_start_year_efficiency_h_policy = ExtConstant(
    "model_parameters/sable.xlsx",
    "World",
    "Start_year_H",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_start_year_efficiency_h_policy",
)


@component.add(
    name="Start_year_efficiency_policy",
    units="Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_start_year_efficiency_policy"},
)
def start_year_efficiency_policy():
    """
    Start year efficiency policy
    """
    return _ext_constant_start_year_efficiency_policy()


_ext_constant_start_year_efficiency_policy = ExtConstant(
    "model_parameters/sable.xlsx",
    "World",
    "Start_year_sectors",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_start_year_efficiency_policy",
)


@component.add(
    name="Target_1",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_target_1"},
)
def target_1():
    """
    Dummy variable for the model interface in SABLE software
    """
    return _ext_constant_target_1()


_ext_constant_target_1 = ExtConstant(
    "model_parameters/sable.xlsx",
    "World",
    "T1_sable",
    {},
    _root,
    {},
    "_ext_constant_target_1",
)


@component.add(
    name="Target_10",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_target_10"},
)
def target_10():
    """
    Dummy variable for the model interface in SABLE software
    """
    return _ext_constant_target_10()


_ext_constant_target_10 = ExtConstant(
    "model_parameters/sable.xlsx",
    "World",
    "T10_sable",
    {},
    _root,
    {},
    "_ext_constant_target_10",
)


@component.add(
    name="Target_11",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_target_11"},
)
def target_11():
    """
    Dummy variable for the model interface in SABLE software
    """
    return _ext_constant_target_11()


_ext_constant_target_11 = ExtConstant(
    "model_parameters/sable.xlsx",
    "World",
    "T11_sable",
    {},
    _root,
    {},
    "_ext_constant_target_11",
)


@component.add(
    name="Target_12",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_target_12"},
)
def target_12():
    """
    Dummy variable for the model interface in SABLE software
    """
    return _ext_constant_target_12()


_ext_constant_target_12 = ExtConstant(
    "model_parameters/sable.xlsx",
    "World",
    "T12_sable",
    {},
    _root,
    {},
    "_ext_constant_target_12",
)


@component.add(
    name="Target_2",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_target_2"},
)
def target_2():
    """
    Dummy variable for the model interface in SABLE software
    """
    return _ext_constant_target_2()


_ext_constant_target_2 = ExtConstant(
    "model_parameters/sable.xlsx",
    "World",
    "T2_sable",
    {},
    _root,
    {},
    "_ext_constant_target_2",
)


@component.add(
    name="Target_3",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_target_3"},
)
def target_3():
    """
    Dummy variable for the model interface in SABLE software
    """
    return _ext_constant_target_3()


_ext_constant_target_3 = ExtConstant(
    "model_parameters/sable.xlsx",
    "World",
    "T3_sable",
    {},
    _root,
    {},
    "_ext_constant_target_3",
)


@component.add(
    name="Target_4",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_target_4"},
)
def target_4():
    """
    Dummy variable for the model interface in SABLE software
    """
    return _ext_constant_target_4()


_ext_constant_target_4 = ExtConstant(
    "model_parameters/sable.xlsx",
    "World",
    "T4_sable",
    {},
    _root,
    {},
    "_ext_constant_target_4",
)


@component.add(
    name="Target_5",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_target_5"},
)
def target_5():
    """
    Dummy variable for the model interface in SABLE software
    """
    return _ext_constant_target_5()


_ext_constant_target_5 = ExtConstant(
    "model_parameters/sable.xlsx",
    "World",
    "T5_sable",
    {},
    _root,
    {},
    "_ext_constant_target_5",
)


@component.add(
    name="Target_6",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_target_6"},
)
def target_6():
    """
    Dummy variable for the model interface in SABLE software
    """
    return _ext_constant_target_6()


_ext_constant_target_6 = ExtConstant(
    "model_parameters/sable.xlsx",
    "World",
    "T6_sable",
    {},
    _root,
    {},
    "_ext_constant_target_6",
)


@component.add(
    name="Target_7",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_target_7"},
)
def target_7():
    """
    Dummy variable for the model interface in SABLE software
    """
    return _ext_constant_target_7()


_ext_constant_target_7 = ExtConstant(
    "model_parameters/sable.xlsx",
    "World",
    "T7_sable",
    {},
    _root,
    {},
    "_ext_constant_target_7",
)


@component.add(
    name="Target_8",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_target_8"},
)
def target_8():
    """
    Dummy variable for the model interface in SABLE software
    """
    return _ext_constant_target_8()


_ext_constant_target_8 = ExtConstant(
    "model_parameters/sable.xlsx",
    "World",
    "T8_sable",
    {},
    _root,
    {},
    "_ext_constant_target_8",
)


@component.add(
    name="Target_9",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_target_9"},
)
def target_9():
    """
    Dummy variable for the model interface in SABLE software
    """
    return _ext_constant_target_9()


_ext_constant_target_9 = ExtConstant(
    "model_parameters/sable.xlsx",
    "World",
    "T9_sable",
    {},
    _root,
    {},
    "_ext_constant_target_9",
)


@component.add(
    name="Temp_ref_user_defined",
    units="DegreesC",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_temp_ref_user_defined"},
)
def temp_ref_user_defined():
    """
    Dummy variable for the model interface in SABLE software, reference initial temperature.
    """
    return _ext_constant_temp_ref_user_defined()


_ext_constant_temp_ref_user_defined = ExtConstant(
    "model_parameters/sable.xlsx",
    "World",
    "Temp",
    {},
    _root,
    {},
    "_ext_constant_temp_ref_user_defined",
)


@component.add(
    name="Uranium_availability",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_uranium_availability"},
)
def uranium_availability():
    """
    Dummy variable for the model interface in SABLE software
    """
    return _ext_constant_uranium_availability()


_ext_constant_uranium_availability = ExtConstant(
    "model_parameters/sable.xlsx",
    "World",
    "Uranium",
    {},
    _root,
    {},
    "_ext_constant_uranium_availability",
)
