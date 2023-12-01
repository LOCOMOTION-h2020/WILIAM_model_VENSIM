"""
Module energy.end_use.industrial_h2_demand
Translated using PySD version 3.10.0
"""


@component.add(
    name="Ammonia_demand",
    units="tonnes/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_energy": 1,
        "fertilizer_to_ammonia_intensity": 1,
        "fertilizers_demanded": 1,
        "ammonia_demand_2005": 1,
    },
)
def ammonia_demand():
    """
    Ammonia demand (assumed to evolve analogously to fertilizer demand.). If SWITCH ENERGY = 0 (isolated from the rest of sub-modules), ammonia demand is constant and the same as in 2005.
    """
    return if_then_else(
        switch_energy() == 1,
        lambda: fertilizer_to_ammonia_intensity() * fertilizers_demanded(),
        lambda: ammonia_demand_2005(),
    )


@component.add(
    name="AMMONIA_DEMAND_2005",
    units="tonnes/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_ammonia_demand_2005"},
)
def ammonia_demand_2005():
    """
    Ammonia demand corresponding to the year 2005
    """
    return _ext_constant_ammonia_demand_2005()


_ext_constant_ammonia_demand_2005 = ExtConstant(
    "model_parameters/energy/energy-hydrogen.xlsx",
    "hydrogen_demand",
    "AMMONIA_DEMAND_2005*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_ammonia_demand_2005",
)


@component.add(
    name="FERTILIZER_TO_AMMONIA_INTENSITY",
    units="tonnes/tonnes",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_fertilizer_to_ammonia_intensity"},
)
def fertilizer_to_ammonia_intensity():
    """
    Intensity calculated which "translates" fertilizer demand into ammonia demand.
    """
    return _ext_constant_fertilizer_to_ammonia_intensity()


_ext_constant_fertilizer_to_ammonia_intensity = ExtConstant(
    "model_parameters/energy/energy-hydrogen.xlsx",
    "hydrogen_demand",
    "FERTILIZER_TO_AMMONIA_INTENSITY*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_fertilizer_to_ammonia_intensity",
)


@component.add(
    name="H2_demand_in_refineries",
    units="tonnes/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"h2_intensity_oil_refining": 1, "pe_oil_demand_in_toe": 1},
)
def h2_demand_in_refineries():
    """
    Hydrogen used in refineries to upgrade oil
    """
    return h2_intensity_oil_refining() * pe_oil_demand_in_toe()


@component.add(
    name="H2_demand_to_produce_ammonia",
    units="tonnes/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"h2_intensity_ammonia_production": 1, "ammonia_demand": 1},
)
def h2_demand_to_produce_ammonia():
    """
    Hydrogen used in ammonia production process
    """
    return h2_intensity_ammonia_production() * ammonia_demand()


@component.add(
    name="H2_INTENSITY_AMMONIA_PRODUCTION",
    units="tonnes/tonnes",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_h2_intensity_ammonia_production"},
)
def h2_intensity_ammonia_production():
    """
    Tonnes of hydrogen required to produce 1 ton of ammonia.
    """
    return _ext_constant_h2_intensity_ammonia_production()


_ext_constant_h2_intensity_ammonia_production = ExtConstant(
    "model_parameters/energy/energy-hydrogen.xlsx",
    "hydrogen_demand",
    "H2_INTENSITY_AMMONIA_PRODUCTION",
    {},
    _root,
    {},
    "_ext_constant_h2_intensity_ammonia_production",
)


@component.add(
    name="H2_INTENSITY_OIL_REFINING",
    units="tonnes/toe",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_h2_intensity_oil_refining"},
)
def h2_intensity_oil_refining():
    """
    kg hydrogen per tonne oil intake (i.e. kg H2 per toe)
    """
    return _ext_constant_h2_intensity_oil_refining()


_ext_constant_h2_intensity_oil_refining = ExtConstant(
    "model_parameters/energy/energy-hydrogen.xlsx",
    "hydrogen_demand",
    "H2_INTENSITY_OIL_REFINING",
    {},
    _root,
    {},
    "_ext_constant_h2_intensity_oil_refining",
)


@component.add(
    name="H2_total_demand_in_tonnes",
    units="tonnes/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"h2_demand_in_refineries": 1, "h2_demand_to_produce_ammonia": 1},
)
def h2_total_demand_in_tonnes():
    """
    Total H2 requirements to satisfy the demand, measured in mass units
    """
    return h2_demand_in_refineries() + h2_demand_to_produce_ammonia()


@component.add(
    name="H2_total_demand_LHV_basis",
    units="TJ/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "h2_total_demand_in_tonnes": 1,
        "lhv_hydrogen": 1,
        "unit_conversion_tj_mj": 1,
    },
)
def h2_total_demand_lhv_basis():
    """
    Total H2 requirements to satisfy the demand, measured in energy units (LHV basis)
    """
    return h2_total_demand_in_tonnes() * lhv_hydrogen() * unit_conversion_tj_mj()


@component.add(
    name="LHV_HYDROGEN",
    units="MJ/tonnes",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_lhv_hydrogen"},
)
def lhv_hydrogen():
    """
    H2 low heating value
    """
    return _ext_constant_lhv_hydrogen()


_ext_constant_lhv_hydrogen = ExtConstant(
    "model_parameters/energy/energy-hydrogen.xlsx",
    "hydrogen_constants",
    "H2_LHV",
    {},
    _root,
    {},
    "_ext_constant_lhv_hydrogen",
)


@component.add(
    name="PE_oil_demand",
    units="EJ/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"pe_by_commodity": 1},
)
def pe_oil_demand():
    """
    Oil intakes in refineries measured in EJ/Year
    """
    return pe_by_commodity().loc[:, "PE_oil"].reset_coords(drop=True)


@component.add(
    name="PE_OIL_DEMAND_2005",
    units="EJ/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_pe_oil_demand_2005"},
)
def pe_oil_demand_2005():
    """
    Oil intakes in refineries measured in EJ/Year corresponding to the year 2005
    """
    return _ext_constant_pe_oil_demand_2005()


_ext_constant_pe_oil_demand_2005 = ExtConstant(
    "model_parameters/energy/energy-hydrogen.xlsx",
    "hydrogen_demand",
    "PE_OIL_DEMAND_2005*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_pe_oil_demand_2005",
)


@component.add(
    name="PE_oil_demand_delayed",
    units="EJ/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_pe_oil_demand_delayed": 1},
    other_deps={
        "_delayfixed_pe_oil_demand_delayed": {
            "initial": {"pe_oil_demand_2005": 1, "time_step": 1},
            "step": {"pe_oil_demand": 1},
        }
    },
)
def pe_oil_demand_delayed():
    """
    Oil intakes in refineries measured in EJ/Year
    """
    return _delayfixed_pe_oil_demand_delayed()


_delayfixed_pe_oil_demand_delayed = DelayFixed(
    lambda: pe_oil_demand(),
    lambda: time_step(),
    lambda: pe_oil_demand_2005(),
    time_step,
    "_delayfixed_pe_oil_demand_delayed",
)


@component.add(
    name="PE_oil_demand_in_toe",
    units="toe/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "pe_oil_demand_delayed": 1,
        "unit_conversion_j_ej": 1,
        "unit_conversion_j_toe": 1,
    },
)
def pe_oil_demand_in_toe():
    """
    Oil intakes in refineries measured in toe/Year
    """
    return pe_oil_demand_delayed() * unit_conversion_j_ej() / unit_conversion_j_toe()
