"""
Module materials.recycling_rates_of_minerals_medeas
Translated using PySD version 3.10.0
"""


@component.add(
    name="a_lineal_regr_rr_alt_techn",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "target_rr_alternative_technologies_sp": 1,
        "current_recycling_rates_minerals_alt_techn": 1,
        "start_year_p_rr_minerals_alt_techn": 1,
        "target_year_p_rr_minerals_alt_techn": 1,
    },
)
def a_lineal_regr_rr_alt_techn():
    """
    a parameter of lineal regression "y=a*TIME+b" where y corresponds to the evolution of the recycling rate of each mineral over time ("by mineral rr alt technology").
    """
    return (
        target_rr_alternative_technologies_sp()
        - current_recycling_rates_minerals_alt_techn()
    ) / (target_year_p_rr_minerals_alt_techn() - start_year_p_rr_minerals_alt_techn())


@component.add(
    name="a_lineal_regr_rr_Rest",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "target_rr_rest_sp": 1,
        "current_eol_rr_minerals": 1,
        "target_year_p_rr_minerals_rest": 1,
        "start_year_p_rr_minerals_rest": 1,
    },
)
def a_lineal_regr_rr_rest():
    """
    a parameter of lineal regression "y=a*TIME+b" where y corresponds to the evolution of the recycling rate of each mineral over time ("by mineral rr Rest").
    """
    return (target_rr_rest_sp() - current_eol_rr_minerals()) / (
        target_year_p_rr_minerals_rest() - start_year_p_rr_minerals_rest()
    )


@component.add(
    name="b_lineal_regr_rr_alt_techn",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "target_rr_alternative_technologies_sp": 1,
        "a_lineal_regr_rr_alt_techn": 1,
        "target_year_p_rr_minerals_alt_techn": 1,
    },
)
def b_lineal_regr_rr_alt_techn():
    """
    b parameter of lineal regression "y=a*TIME+b" where y corresponds to the evolution of the recycling rate of each mineral over time ("by mineral rr alt technology").
    """
    return (
        target_rr_alternative_technologies_sp()
        - a_lineal_regr_rr_alt_techn() * target_year_p_rr_minerals_alt_techn()
    )


@component.add(
    name="b_lineal_regr_rr_Rest",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "target_rr_rest_sp": 1,
        "a_lineal_regr_rr_rest": 1,
        "target_year_p_rr_minerals_rest": 1,
    },
)
def b_lineal_regr_rr_rest():
    """
    b parameter of lineal regression "y=a*TIME+b" where y corresponds to the evolution of the recycling rate of each mineral over time ("by mineral rr Rest").
    """
    return (
        target_rr_rest_sp() - a_lineal_regr_rr_rest() * target_year_p_rr_minerals_rest()
    )


@component.add(
    name="by_mineral_rr_alt_techn",
    units="DMNL",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "a_lineal_regr_rr_alt_techn": 1,
        "time": 1,
        "b_lineal_regr_rr_alt_techn": 1,
    },
)
def by_mineral_rr_alt_techn():
    """
    Recycling rates over time by mineral for alternative technologies (RES elec & EV batteries).
    """
    return a_lineal_regr_rr_alt_techn() * time() + b_lineal_regr_rr_alt_techn()


@component.add(
    name="by_mineral_rr_alt_techn_1yr",
    units="DMNL",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_by_mineral_rr_alt_techn_1yr": 1},
    other_deps={
        "_delayfixed_by_mineral_rr_alt_techn_1yr": {
            "initial": {"current_recycling_rates_minerals_alt_techn": 1},
            "step": {"by_mineral_rr_alt_techn": 1},
        }
    },
)
def by_mineral_rr_alt_techn_1yr():
    """
    Recycling rates over time delayed 1 year by mineral for alternative technologies (RES elec & EV batteries).
    """
    return _delayfixed_by_mineral_rr_alt_techn_1yr()


_delayfixed_by_mineral_rr_alt_techn_1yr = DelayFixed(
    lambda: by_mineral_rr_alt_techn(),
    lambda: 1,
    lambda: current_recycling_rates_minerals_alt_techn().expand_dims(
        {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, 0
    ),
    time_step,
    "_delayfixed_by_mineral_rr_alt_techn_1yr",
)


@component.add(
    name="by_mineral_rr_Rest",
    units="DMNL",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"a_lineal_regr_rr_rest": 1, "time": 1, "b_lineal_regr_rr_rest": 1},
)
def by_mineral_rr_rest():
    """
    Recycling rates over time by mineral for the rest of the economy.
    """
    return a_lineal_regr_rr_rest() * time() + b_lineal_regr_rr_rest()


@component.add(
    name="by_mineral_rr_Rest_1yr",
    units="DMNL",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_by_mineral_rr_rest_1yr": 1},
    other_deps={
        "_delayfixed_by_mineral_rr_rest_1yr": {
            "initial": {"current_recycling_rates_minerals_alt_techn": 1},
            "step": {"by_mineral_rr_rest": 1},
        }
    },
)
def by_mineral_rr_rest_1yr():
    """
    Recycling rates over time delayed 1 year by mineral for the rest of the economy.
    """
    return _delayfixed_by_mineral_rr_rest_1yr()


_delayfixed_by_mineral_rr_rest_1yr = DelayFixed(
    lambda: by_mineral_rr_rest(),
    lambda: 1,
    lambda: current_recycling_rates_minerals_alt_techn().expand_dims(
        {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, 0
    ),
    time_step,
    "_delayfixed_by_mineral_rr_rest_1yr",
)


@component.add(
    name="by_mineral_rr_variation_alt_techn",
    units="DMNL",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 2,
        "historic_improvement_recycling_rates_minerals": 2,
        "by_mineral_rr_alt_techn": 1,
        "start_year_p_rr_minerals_alt_techn": 1,
        "by_mineral_rr_alt_techn_1yr": 1,
    },
)
def by_mineral_rr_variation_alt_techn():
    """
    Variation of recycling rates per mineral for alternative technologies (RES elec & EV batteries).
    """
    return if_then_else(
        time() < 2015,
        lambda: xr.DataArray(
            historic_improvement_recycling_rates_minerals(),
            {
                "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                "MATERIALS_I": _subscript_dict["MATERIALS_I"],
            },
            ["REGIONS_9_I", "MATERIALS_I"],
        ),
        lambda: if_then_else(
            (time() < start_year_p_rr_minerals_alt_techn()).expand_dims(
                {"MATERIALS_I": _subscript_dict["MATERIALS_I"]}, 1
            ),
            lambda: xr.DataArray(
                historic_improvement_recycling_rates_minerals(),
                {
                    "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                    "MATERIALS_I": _subscript_dict["MATERIALS_I"],
                },
                ["REGIONS_9_I", "MATERIALS_I"],
            ),
            lambda: by_mineral_rr_alt_techn() - by_mineral_rr_alt_techn_1yr(),
        ),
    )


@component.add(
    name="by_mineral_rr_variation_Rest",
    units="DMNL",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 2,
        "historic_improvement_recycling_rates_minerals": 2,
        "by_mineral_rr_rest": 1,
        "start_year_p_rr_minerals_rest": 1,
        "by_mineral_rr_rest_1yr": 1,
    },
)
def by_mineral_rr_variation_rest():
    """
    Variation of recycling rates per mineral for the rest of the economy.
    """
    return if_then_else(
        time() < 2015,
        lambda: xr.DataArray(
            historic_improvement_recycling_rates_minerals(),
            {
                "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                "MATERIALS_I": _subscript_dict["MATERIALS_I"],
            },
            ["REGIONS_9_I", "MATERIALS_I"],
        ),
        lambda: if_then_else(
            (time() < start_year_p_rr_minerals_rest()).expand_dims(
                {"MATERIALS_I": _subscript_dict["MATERIALS_I"]}, 1
            ),
            lambda: xr.DataArray(
                historic_improvement_recycling_rates_minerals(),
                {
                    "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                    "MATERIALS_I": _subscript_dict["MATERIALS_I"],
                },
                ["REGIONS_9_I", "MATERIALS_I"],
            ),
            lambda: by_mineral_rr_rest() - by_mineral_rr_rest_1yr(),
        ),
    )


@component.add(
    name="common_rr_minerals_variation_alt_techn",
    units="DMNL",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "start_year_p_common_rr_minerals_alt_techn": 1,
        "historic_improvement_recycling_rates_minerals": 1,
        "policy_common_rr_minerals_variation_alt_techn_sp": 1,
    },
)
def common_rr_minerals_variation_alt_techn():
    """
    Recycling rates of minererals (common annual variation).
    """
    return if_then_else(
        time() < start_year_p_common_rr_minerals_alt_techn(),
        lambda: xr.DataArray(
            historic_improvement_recycling_rates_minerals(),
            {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
            ["REGIONS_9_I"],
        ),
        lambda: policy_common_rr_minerals_variation_alt_techn_sp(),
    ).expand_dims({"MATERIALS_I": _subscript_dict["MATERIALS_I"]}, 1)


@component.add(
    name="common_rr_minerals_variation_Rest",
    units="DMNL",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "start_year_p_common_rr_minerals_rest": 1,
        "historic_improvement_recycling_rates_minerals": 1,
        "policy_common_rr_minerals_variation_rest_sp": 1,
    },
)
def common_rr_minerals_variation_rest():
    """
    Recycling rates of minererals (common annual variation).
    """
    return if_then_else(
        time() < start_year_p_common_rr_minerals_rest(),
        lambda: xr.DataArray(
            historic_improvement_recycling_rates_minerals(),
            {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
            ["REGIONS_9_I"],
        ),
        lambda: policy_common_rr_minerals_variation_rest_sp(),
    ).expand_dims({"MATERIALS_I": _subscript_dict["MATERIALS_I"]}, 1)


@component.add(
    name="constrain_rr_improv_for_alt_techn_per_mineral",
    units="DMNL",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "eol_recycling_rates_minerals_alt_techn": 1,
        "max_recycling_rates_minerals": 1,
    },
)
def constrain_rr_improv_for_alt_techn_per_mineral():
    """
    Constraint recycling rate improvement for alternative technologies (RES elec & EV batteries) per material.
    """
    return if_then_else(
        eol_recycling_rates_minerals_alt_techn() < max_recycling_rates_minerals(),
        lambda: xr.DataArray(
            1,
            {
                "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                "MATERIALS_I": _subscript_dict["MATERIALS_I"],
            },
            ["REGIONS_9_I", "MATERIALS_I"],
        ),
        lambda: xr.DataArray(
            0,
            {
                "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                "MATERIALS_I": _subscript_dict["MATERIALS_I"],
            },
            ["REGIONS_9_I", "MATERIALS_I"],
        ),
    )


@component.add(
    name="constrain_rr_improv_for_Rest_per_mineral",
    units="DMNL",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "eol_recycling_rates_minerals_rest": 1,
        "max_recycling_rates_minerals": 1,
    },
)
def constrain_rr_improv_for_rest_per_mineral():
    """
    Remaining recycling rate improvement for the rest of the economy per material.
    """
    return if_then_else(
        eol_recycling_rates_minerals_rest() < max_recycling_rates_minerals(),
        lambda: xr.DataArray(
            1,
            {
                "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                "MATERIALS_I": _subscript_dict["MATERIALS_I"],
            },
            ["REGIONS_9_I", "MATERIALS_I"],
        ),
        lambda: xr.DataArray(
            0,
            {
                "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                "MATERIALS_I": _subscript_dict["MATERIALS_I"],
            },
            ["REGIONS_9_I", "MATERIALS_I"],
        ),
    )


@component.add(
    name="current_recycling_rates_minerals_alt_techn",
    units="DMNL",
    subscripts=["MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "current_eol_rr_minerals": 1,
        "rr_minerals_alt_techn_res_vs_total_economy": 1,
    },
)
def current_recycling_rates_minerals_alt_techn():
    """
    Current recycling rates of minerales for alternative technologies. Since these technologies are novel and often include materials which are used in small quantities in complex products, the recycling rates of the used minerals are lower than for the whole economy (following the parameter "EOL-RR minerals alt techn RES vs. total economy").
    """
    return current_eol_rr_minerals() * rr_minerals_alt_techn_res_vs_total_economy()


@component.add(
    name="EOL_recycling_rates_minerals_alt_techn",
    units="DMNL",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_eol_recycling_rates_minerals_alt_techn": 1},
    other_deps={
        "_integ_eol_recycling_rates_minerals_alt_techn": {
            "initial": {
                "current_recycling_rates_minerals_alt_techn": 1,
                "all_minerals_virgin": 1,
            },
            "step": {"improvement_recycling_rates_minerals_alt_techn": 1},
        }
    },
)
def eol_recycling_rates_minerals_alt_techn():
    """
    Recycling rates minerals of alternative technologies (RES elec & EV batteries).
    """
    return _integ_eol_recycling_rates_minerals_alt_techn()


_integ_eol_recycling_rates_minerals_alt_techn = Integ(
    lambda: improvement_recycling_rates_minerals_alt_techn(),
    lambda: (
        current_recycling_rates_minerals_alt_techn() * all_minerals_virgin()
    ).expand_dims({"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, 0),
    "_integ_eol_recycling_rates_minerals_alt_techn",
)


@component.add(
    name="EOL_recycling_rates_minerals_Rest",
    units="DMNL",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_eol_recycling_rates_minerals_rest": 1},
    other_deps={
        "_integ_eol_recycling_rates_minerals_rest": {
            "initial": {"current_eol_rr_minerals": 1, "all_minerals_virgin": 1},
            "step": {"improvement_recycling_rates_minerals_rest": 1},
        }
    },
)
def eol_recycling_rates_minerals_rest():
    """
    Recycling rates minerals for the rest of the economy.
    """
    return _integ_eol_recycling_rates_minerals_rest()


_integ_eol_recycling_rates_minerals_rest = Integ(
    lambda: improvement_recycling_rates_minerals_rest(),
    lambda: (current_eol_rr_minerals() * all_minerals_virgin()).expand_dims(
        {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, 0
    ),
    "_integ_eol_recycling_rates_minerals_rest",
)


@component.add(
    name="improvement_recycling_rates_minerals_alt_techn",
    units="DMNL",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "historic_improvement_recycling_rates_minerals": 1,
        "select_mineral_rr_targets_sp": 1,
        "by_mineral_rr_variation_alt_techn": 1,
        "eol_recycling_rates_minerals_alt_techn": 1,
        "switch_computation_static_eroi": 1,
        "common_rr_minerals_variation_alt_techn": 1,
        "constrain_rr_improv_for_alt_techn_per_mineral": 1,
    },
)
def improvement_recycling_rates_minerals_alt_techn():
    """
    Annual improvement of the recycling rates of minerals for alternative technologies (RES elec & EV batteries).
    """
    return (
        if_then_else(
            time() < 2015,
            lambda: xr.DataArray(
                historic_improvement_recycling_rates_minerals(),
                {
                    "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                    "MATERIALS_I": _subscript_dict["MATERIALS_I"],
                },
                ["REGIONS_9_I", "MATERIALS_I"],
            ),
            lambda: if_then_else(
                switch_computation_static_eroi() == 1,
                lambda: xr.DataArray(
                    0,
                    {
                        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                        "MATERIALS_I": _subscript_dict["MATERIALS_I"],
                    },
                    ["REGIONS_9_I", "MATERIALS_I"],
                ),
                lambda: if_then_else(
                    (select_mineral_rr_targets_sp() == 2).expand_dims(
                        {"MATERIALS_I": _subscript_dict["MATERIALS_I"]}, 1
                    ),
                    lambda: common_rr_minerals_variation_alt_techn()
                    * eol_recycling_rates_minerals_alt_techn(),
                    lambda: by_mineral_rr_variation_alt_techn(),
                ),
            ),
        )
        * constrain_rr_improv_for_alt_techn_per_mineral()
    )


@component.add(
    name="improvement_recycling_rates_minerals_Rest",
    units="DMNL",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "historic_improvement_recycling_rates_minerals": 1,
        "by_mineral_rr_variation_rest": 1,
        "common_rr_minerals_variation_rest": 1,
        "eol_recycling_rates_minerals_rest": 1,
        "select_mineral_rr_targets_sp": 1,
        "constrain_rr_improv_for_rest_per_mineral": 1,
    },
)
def improvement_recycling_rates_minerals_rest():
    """
    Annual improvement of the recycling rates of minerals for the rest of the economy.
    """
    return (
        if_then_else(
            time() < 2015,
            lambda: xr.DataArray(
                historic_improvement_recycling_rates_minerals(),
                {
                    "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                    "MATERIALS_I": _subscript_dict["MATERIALS_I"],
                },
                ["REGIONS_9_I", "MATERIALS_I"],
            ),
            lambda: if_then_else(
                (select_mineral_rr_targets_sp() == 2).expand_dims(
                    {"MATERIALS_I": _subscript_dict["MATERIALS_I"]}, 1
                ),
                lambda: common_rr_minerals_variation_rest()
                * eol_recycling_rates_minerals_rest(),
                lambda: by_mineral_rr_variation_rest(),
            ),
        )
        * constrain_rr_improv_for_rest_per_mineral()
    )
