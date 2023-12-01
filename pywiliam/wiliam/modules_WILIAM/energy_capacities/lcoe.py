"""
Module energy_capacities.lcoe
Translated using PySD version 3.10.0
"""


@component.add(
    name="LCOE_by_PROTRA_priority_signal",
    units="DMNL",
    subscripts=["REGIONS_9_I", "NRG_PROTRA_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={"lcoe_protra": 1, "min_lcoe": 1, "max_lcoe": 1},
)
def lcoe_by_protra_priority_signal():
    """
    approximation of levelized cost of electricity, NOT taking into account capital cost, discount rate etc.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
        },
        ["REGIONS_9_I", "NRG_PROTRA_I"],
    )
    value.loc[:, _subscript_dict["PROTRA_PP_CHP_HP_I"]] = (
        1
        - zidz(
            lcoe_protra() - min_lcoe(),
            max_lcoe().expand_dims(
                {"PROTRA_PP_CHP_HP_I": _subscript_dict["PROTRA_PP_CHP_HP_I"]}, 1
            ),
        )
    ).values
    value.loc[:, _subscript_dict["PROTRA_NP_I"]] = 1
    return value


@component.add(
    name="LCOE_PROTRA",
    units="dollars/MWh",
    subscripts=["REGIONS_9_I", "PROTRA_PP_CHP_HP_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "dynamic_capacity_investment_cost_protra_development_36r": 1,
        "protra_lifetime": 1,
        "opex_by_protra_and_region": 1,
        "protra_max_full_load_hours_after_constraints": 1,
    },
)
def lcoe_protra():
    """
    Levelized cost of electricity for transformation processes (technologies). A minimum for 'protra_max_full_load_hours_after_constraints' of 1h is set ad hoc to avoid potential issues dividing by 0 when curtailement is 100%.
    """
    return (
        dynamic_capacity_investment_cost_protra_development_36r()
        .loc[_subscript_dict["REGIONS_9_I"], :]
        .rename({"REGIONS_36_I": "REGIONS_9_I"})
        / 1000000.0
        / protra_lifetime()
        .loc[:, _subscript_dict["PROTRA_PP_CHP_HP_I"]]
        .rename({"NRG_PROTRA_I": "PROTRA_PP_CHP_HP_I"})
        + opex_by_protra_and_region()
        .loc[:, _subscript_dict["PROTRA_PP_CHP_HP_I"]]
        .rename({"NRG_PROTRA_I": "PROTRA_PP_CHP_HP_I"})
        * 277.778
    ) / np.maximum(
        protra_max_full_load_hours_after_constraints()
        .loc[:, _subscript_dict["PROTRA_PP_CHP_HP_I"]]
        .rename({"NRG_PROTRA_I": "PROTRA_PP_CHP_HP_I"}),
        1,
    )


@component.add(
    name="max_LCOE",
    units="$/MWh",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"lcoe_protra": 1},
)
def max_lcoe():
    return vmax(
        lcoe_protra().rename({"PROTRA_PP_CHP_HP_I": "PROTRA_PP_CHP_HP_I!"}),
        dim=["PROTRA_PP_CHP_HP_I!"],
    )


@component.add(
    name="min_LCOE",
    units="$/MWh",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"lcoe_protra": 1},
)
def min_lcoe():
    return vmin(
        lcoe_protra().rename({"PROTRA_PP_CHP_HP_I": "PROTRA_PP_CHP_HP_I!"}),
        dim=["PROTRA_PP_CHP_HP_I!"],
    )
