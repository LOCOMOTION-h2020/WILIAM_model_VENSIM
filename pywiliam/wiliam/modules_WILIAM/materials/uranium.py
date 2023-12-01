"""
Module materials.uranium
Translated using PySD version 3.10.0
"""


@component.add(
    name="cumulated_uranium_extraction",
    units="EJ",
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_cumulated_uranium_extraction": 1},
    other_deps={
        "_integ_cumulated_uranium_extraction": {
            "initial": {"cumulated_uranium_extraction_in_2005": 1},
            "step": {"uranium_extraction_rate": 1},
        }
    },
)
def cumulated_uranium_extraction():
    """
    Cumulated uranium extraction.
    """
    return _integ_cumulated_uranium_extraction()


_integ_cumulated_uranium_extraction = Integ(
    lambda: uranium_extraction_rate(),
    lambda: cumulated_uranium_extraction_in_2005(),
    "_integ_cumulated_uranium_extraction",
)


@component.add(
    name="CUMULATED_URANIUM_EXTRACTION_IN_2005",
    units="EJ",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_cumulated_uranium_extraction_in_2005"},
)
def cumulated_uranium_extraction_in_2005():
    """
    Cumulated coal extraction to 2005 (EWG 2006).
    """
    return _ext_constant_cumulated_uranium_extraction_in_2005()


_ext_constant_cumulated_uranium_extraction_in_2005 = ExtConstant(
    "model_parameters/energy/energy.xlsm",
    "World",
    "cumulated_uranium_extraction_to_2005",
    {},
    _root,
    {},
    "_ext_constant_cumulated_uranium_extraction_in_2005",
)


@component.add(
    name="delayed_TS_uranium_extraction_rate",
    units="EJ/Year",
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_uranium_extraction_rate": 1},
    other_deps={
        "_delayfixed_delayed_ts_uranium_extraction_rate": {
            "initial": {"initial_global_uranium_extraction_rate": 1, "time_step": 1},
            "step": {"uranium_extraction_rate": 1},
        }
    },
)
def delayed_ts_uranium_extraction_rate():
    """
    Delay to break simulataneous equations in the feedback demand nuclear -> demand uranium -> uranium availability -> demand nuclear.
    """
    return _delayfixed_delayed_ts_uranium_extraction_rate()


_delayfixed_delayed_ts_uranium_extraction_rate = DelayFixed(
    lambda: uranium_extraction_rate(),
    lambda: time_step(),
    lambda: initial_global_uranium_extraction_rate(),
    time_step,
    "_delayfixed_delayed_ts_uranium_extraction_rate",
)


@component.add(
    name="INITIAL_GLOBAL_URANIUM_EXTRACTION_RATE",
    units="EJ/Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_global_uranium_extraction_rate"},
)
def initial_global_uranium_extraction_rate():
    """
    Global uranium extraction in the year 2005 loaded exogenously to avoid simultaneous equations.
    """
    return _ext_constant_initial_global_uranium_extraction_rate()


_ext_constant_initial_global_uranium_extraction_rate = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "World",
    "INITIAL_GLOBAL_URANIUM_EXTRACTION_RATE",
    {},
    _root,
    {},
    "_ext_constant_initial_global_uranium_extraction_rate",
)


@component.add(
    name="INITIAL_PE_global_demand_uranium",
    units="EJ/Year",
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_initial_pe_global_demand_uranium": 1},
    other_deps={
        "_initial_initial_pe_global_demand_uranium": {
            "initial": {"pe_global_demand_uranium": 1},
            "step": {},
        }
    },
)
def initial_pe_global_demand_uranium():
    return _initial_initial_pe_global_demand_uranium()


_initial_initial_pe_global_demand_uranium = Initial(
    lambda: pe_global_demand_uranium(), "_initial_initial_pe_global_demand_uranium"
)


@component.add(
    name="INITIAL_URR_URANIUM",
    units="EJ",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"urr_uranium": 1, "cumulated_uranium_extraction_in_2005": 1},
)
def initial_urr_uranium():
    """
    initial availability of resources+reserves of Uranium
    """
    return urr_uranium() - cumulated_uranium_extraction_in_2005()


@component.add(
    name="maximum_uranium_extraction_rate",
    units="EJ/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_model_explorer": 1,
        "table_max_extraction_uranium_zittel2012": 2,
        "table_max_extraction_ewg2006": 2,
        "model_explorer_uranium_maximum_supply_curve": 3,
        "table_max_extraction_uranium_user_defined_sp": 2,
        "table_maximum_extraction_uranium_ewg2013": 2,
        "rurr_uranium": 8,
        "select_uranium_maximum_supply_curve_sp": 3,
    },
)
def maximum_uranium_extraction_rate():
    """
    Maximum extraction curve selected for the simulations.
    """
    return if_then_else(
        switch_model_explorer() == 1,
        lambda: if_then_else(
            model_explorer_uranium_maximum_supply_curve() == 1,
            lambda: table_max_extraction_ewg2006(rurr_uranium()),
            lambda: if_then_else(
                model_explorer_uranium_maximum_supply_curve() == 2,
                lambda: table_max_extraction_uranium_zittel2012(rurr_uranium()),
                lambda: if_then_else(
                    model_explorer_uranium_maximum_supply_curve() == 3,
                    lambda: table_maximum_extraction_uranium_ewg2013(rurr_uranium()),
                    lambda: table_max_extraction_uranium_user_defined_sp(
                        rurr_uranium()
                    ),
                ),
            ),
        ),
        lambda: if_then_else(
            select_uranium_maximum_supply_curve_sp() == 1,
            lambda: table_max_extraction_ewg2006(rurr_uranium()),
            lambda: if_then_else(
                select_uranium_maximum_supply_curve_sp() == 2,
                lambda: table_max_extraction_uranium_zittel2012(rurr_uranium()),
                lambda: if_then_else(
                    select_uranium_maximum_supply_curve_sp() == 3,
                    lambda: table_maximum_extraction_uranium_ewg2013(rurr_uranium()),
                    lambda: table_max_extraction_uranium_user_defined_sp(
                        rurr_uranium()
                    ),
                ),
            ),
        ),
    )


@component.add(
    name="PE_global_demand_uranium",
    units="EJ/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"pe_by_commodity": 1},
)
def pe_global_demand_uranium():
    """
    Primary energy demand of uranium for nuclear power generation.
    """
    return sum(
        pe_by_commodity()
        .loc[:, "PE_nuclear"]
        .reset_coords(drop=True)
        .rename({"REGIONS_9_I": "REGIONS_9_I!"}),
        dim=["REGIONS_9_I!"],
    )


@component.add(
    name="RURR_uranium",
    units="EJ",
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_rurr_uranium": 1},
    other_deps={
        "_integ_rurr_uranium": {
            "initial": {"initial_urr_uranium": 1},
            "step": {"uranium_extraction_rate": 1},
        }
    },
)
def rurr_uranium():
    """
    RURR uranium. 720 EJ extracted before 1990.
    """
    return _integ_rurr_uranium()


_integ_rurr_uranium = Integ(
    lambda: -uranium_extraction_rate(),
    lambda: initial_urr_uranium(),
    "_integ_rurr_uranium",
)


@component.add(
    name="share_remaining_potential_uranium_extraction_rate_vs_PE_demand",
    units="1",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"maximum_uranium_extraction_rate": 1, "pe_global_demand_uranium": 2},
)
def share_remaining_potential_uranium_extraction_rate_vs_pe_demand():
    """
    Remaining "potential extraction rate" with relation to current extraction rate of uranium as a share of the uranium primary energy demand.
    """
    return zidz(
        maximum_uranium_extraction_rate() - pe_global_demand_uranium(),
        pe_global_demand_uranium(),
    )


@component.add(
    name="UNLIMITED_URR_NRE_PARAMETER",
    units="EJ",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_unlimited_urr_nre_parameter"},
)
def unlimited_urr_nre_parameter():
    """
    Arbitrary very high value to simulate, in practical terms, unlimited non-renewable energy stocks.
    """
    return _ext_constant_unlimited_urr_nre_parameter()


_ext_constant_unlimited_urr_nre_parameter = ExtConstant(
    "model_parameters/energy/energy.xlsm",
    "World",
    "Unlimited_URR_NRE",
    {},
    _root,
    {},
    "_ext_constant_unlimited_urr_nre_parameter",
)


@component.add(
    name="uranium_extraction_rate",
    units="EJ/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_model_explorer": 1,
        "initial_pe_global_demand_uranium": 2,
        "switch_materials": 2,
        "model_explorer_uranium_maximum_supply_curve": 1,
        "maximum_uranium_extraction_rate": 2,
        "pe_global_demand_uranium": 4,
        "select_uranium_maximum_supply_curve_sp": 1,
    },
)
def uranium_extraction_rate():
    """
    Annual extraction of uranium.
    """
    return if_then_else(
        switch_model_explorer() == 1,
        lambda: if_then_else(
            switch_materials() == 0,
            lambda: initial_pe_global_demand_uranium(),
            lambda: if_then_else(
                model_explorer_uranium_maximum_supply_curve() == 0,
                lambda: pe_global_demand_uranium(),
                lambda: np.minimum(
                    pe_global_demand_uranium(), maximum_uranium_extraction_rate()
                ),
            ),
        ),
        lambda: if_then_else(
            switch_materials() == 0,
            lambda: initial_pe_global_demand_uranium(),
            lambda: if_then_else(
                select_uranium_maximum_supply_curve_sp() == 0,
                lambda: pe_global_demand_uranium(),
                lambda: np.minimum(
                    pe_global_demand_uranium(), maximum_uranium_extraction_rate()
                ),
            ),
        ),
    )


@component.add(
    name="uranium_extraction_rate_weight",
    units="Kt/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"uranium_extraction_rate": 1, "unit_conversion_kt_uranium_ej": 1},
)
def uranium_extraction_rate_weight():
    """
    Annual extraction of uranium in kt.
    """
    return xr.DataArray(
        uranium_extraction_rate() * unit_conversion_kt_uranium_ej(),
        {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
        ["REGIONS_9_I"],
    )


@component.add(
    name="URR_uranium",
    units="EJ",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_model_explorer": 1,
        "urr_uranium_zittel2012": 2,
        "urr_uranium_user_defined": 2,
        "unlimited_urr_nre_parameter": 2,
        "urr_uranium_ewg2006": 2,
        "model_explorer_uranium_maximum_supply_curve": 4,
        "urr_uranium_ewg2013": 2,
        "select_uranium_maximum_supply_curve_sp": 4,
    },
)
def urr_uranium():
    """
    Ultimately Recoverable Resources (URR) associated to the selected depletion curve. Global value.
    """
    return if_then_else(
        switch_model_explorer() == 1,
        lambda: if_then_else(
            model_explorer_uranium_maximum_supply_curve() == 0,
            lambda: unlimited_urr_nre_parameter(),
            lambda: if_then_else(
                model_explorer_uranium_maximum_supply_curve() == 1,
                lambda: urr_uranium_ewg2006(),
                lambda: if_then_else(
                    model_explorer_uranium_maximum_supply_curve() == 2,
                    lambda: urr_uranium_zittel2012(),
                    lambda: if_then_else(
                        model_explorer_uranium_maximum_supply_curve() == 3,
                        lambda: urr_uranium_ewg2013(),
                        lambda: urr_uranium_user_defined(),
                    ),
                ),
            ),
        ),
        lambda: if_then_else(
            select_uranium_maximum_supply_curve_sp() == 0,
            lambda: unlimited_urr_nre_parameter(),
            lambda: if_then_else(
                select_uranium_maximum_supply_curve_sp() == 1,
                lambda: urr_uranium_ewg2006(),
                lambda: if_then_else(
                    select_uranium_maximum_supply_curve_sp() == 2,
                    lambda: urr_uranium_zittel2012(),
                    lambda: if_then_else(
                        select_uranium_maximum_supply_curve_sp() == 3,
                        lambda: urr_uranium_ewg2013(),
                        lambda: urr_uranium_user_defined(),
                    ),
                ),
            ),
        ),
    )
