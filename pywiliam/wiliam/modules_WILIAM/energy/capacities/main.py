"""
Module energy.capacities.main
Translated using PySD version 3.10.0
"""


@component.add(
    name="applied_TO_reserve_factor_by_commodity",
    units="DMNL",
    subscripts=["REGIONS_9_I", "NRG_TO_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"exogenous_to_reserve_factor": 1},
)
def applied_to_reserve_factor_by_commodity():
    """
    Reserve factor accounting for excess-capacities that need to be installed in order to ensure sufficient transformation capacities. Only Elec and Heat used.
    """
    return exogenous_to_reserve_factor()


@component.add(
    name="capacity_stock_PROTRA_PP_solar_PV_by_subtechnology",
    units="TW",
    subscripts=[
        "REGIONS_9_I",
        "PROTRA_PP_SOLAR_PV_I",
        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I",
    ],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={
        "_integ_capacity_stock_protra_pp_solar_pv_by_subtechnology": 1,
        "_integ_capacity_stock_protra_pp_solar_pv_by_subtechnology_1": 1,
    },
    other_deps={
        "_integ_capacity_stock_protra_pp_solar_pv_by_subtechnology": {
            "initial": {
                "initial_protra_capacity_stock": 1,
                "share_pv_subtechnologies_before_2020": 1,
            },
            "step": {
                "protra_pp_solar_pv_by_subtechnology_capacity_expansion": 1,
                "protra_pp_solar_pv_by_subtechnology_capacity_decomissioning": 1,
            },
        },
        "_integ_capacity_stock_protra_pp_solar_pv_by_subtechnology_1": {
            "initial": {
                "initial_protra_capacity_stock": 1,
                "share_pv_subtechnologies_before_2020": 1,
            },
            "step": {
                "protra_pp_solar_pv_by_subtechnology_capacity_expansion": 1,
                "protra_pp_solar_pv_by_subtechnology_capacity_decomissioning": 1,
            },
        },
    },
)
def capacity_stock_protra_pp_solar_pv_by_subtechnology():
    """
    solar PV capacity installed by panel subtechnology
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "PROTRA_PP_SOLAR_PV_I": _subscript_dict["PROTRA_PP_SOLAR_PV_I"],
            "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": _subscript_dict[
                "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"
            ],
        },
        ["REGIONS_9_I", "PROTRA_PP_SOLAR_PV_I", "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"],
    )
    value.loc[
        :, ["PROTRA_PP_solar_open_space_PV"], :
    ] = _integ_capacity_stock_protra_pp_solar_pv_by_subtechnology().values
    value.loc[
        :, ["PROTRA_PP_solar_urban_PV"], :
    ] = _integ_capacity_stock_protra_pp_solar_pv_by_subtechnology_1().values
    return value


_integ_capacity_stock_protra_pp_solar_pv_by_subtechnology = Integ(
    lambda: (
        protra_pp_solar_pv_by_subtechnology_capacity_expansion()
        .loc[:, "PROTRA_PP_solar_open_space_PV", :]
        .reset_coords(drop=True)
        - protra_pp_solar_pv_by_subtechnology_capacity_decomissioning()
        .loc[:, "PROTRA_PP_solar_open_space_PV", :]
        .reset_coords(drop=True)
    ).expand_dims({"NRG_PRO_I": ["PROTRA_PP_solar_open_space_PV"]}, 1),
    lambda: (
        initial_protra_capacity_stock()
        .loc[_subscript_dict["REGIONS_9_I"], "TO_elec", "PROTRA_PP_solar_open_space_PV"]
        .reset_coords(drop=True)
        .rename({"REGIONS_36_I": "REGIONS_9_I"})
        * share_pv_subtechnologies_before_2020()
    ).expand_dims({"NRG_PRO_I": ["PROTRA_PP_solar_open_space_PV"]}, 1),
    "_integ_capacity_stock_protra_pp_solar_pv_by_subtechnology",
)

_integ_capacity_stock_protra_pp_solar_pv_by_subtechnology_1 = Integ(
    lambda: (
        protra_pp_solar_pv_by_subtechnology_capacity_expansion()
        .loc[:, "PROTRA_PP_solar_urban_PV", :]
        .reset_coords(drop=True)
        - protra_pp_solar_pv_by_subtechnology_capacity_decomissioning()
        .loc[:, "PROTRA_PP_solar_urban_PV", :]
        .reset_coords(drop=True)
    ).expand_dims({"NRG_PRO_I": ["PROTRA_PP_solar_urban_PV"]}, 1),
    lambda: (
        initial_protra_capacity_stock()
        .loc[_subscript_dict["REGIONS_9_I"], "TO_elec", "PROTRA_PP_solar_urban_PV"]
        .reset_coords(drop=True)
        .rename({"REGIONS_36_I": "REGIONS_9_I"})
        * share_pv_subtechnologies_before_2020()
    ).expand_dims({"NRG_PRO_I": ["PROTRA_PP_solar_urban_PV"]}, 1),
    "_integ_capacity_stock_protra_pp_solar_pv_by_subtechnology_1",
)


@component.add(
    name="CF_LOSS_SHARE_STOPPING_PROTRA_CAPACITY_EXPANSION_SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_cf_loss_share_stopping_protra_capacity_expansion_sp"
    },
)
def cf_loss_share_stopping_protra_capacity_expansion_sp():
    """
    If the configuration of the power system cannot deal with variabilty of RES, the regressions estimate a reduction in the effective annual load hours. This parameter represents the threshold beyond which the loss in the CF would prevent investors to continue expanding the capacity of this technology.
    """
    return _ext_constant_cf_loss_share_stopping_protra_capacity_expansion_sp()


_ext_constant_cf_loss_share_stopping_protra_capacity_expansion_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "CF_LOSS_SHARE_STOPPING_PROTRA_CAPACITY_EXPANSION_SP",
    {},
    _root,
    {},
    "_ext_constant_cf_loss_share_stopping_protra_capacity_expansion_sp",
)


@component.add(
    name="check_aggregated_shortfall_allocation",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_TO_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"protra_shortfall_allocation": 1},
)
def check_aggregated_shortfall_allocation():
    """
    shortfall aggregated by commodity
    """
    return sum(
        protra_shortfall_allocation().rename({"NRG_PROTRA_I": "NRG_PROTRA_I!"}),
        dim=["NRG_PROTRA_I!"],
    )


@component.add(
    name="check_CHP_elec_capacity_expansion",
    units="TW/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"protra_capacity_expansion": 1},
)
def check_chp_elec_capacity_expansion():
    return sum(
        protra_capacity_expansion()
        .loc[:, "TO_elec", _subscript_dict["PROTRA_CHP_I"]]
        .reset_coords(drop=True)
        .rename({"NRG_PROTRA_I": "PROTRA_CHP_I!"}),
        dim=["PROTRA_CHP_I!"],
    )


@component.add(
    name="check_CHP_elec_capacity_stock",
    units="TW",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"protra_capacity_stock": 1},
)
def check_chp_elec_capacity_stock():
    return sum(
        protra_capacity_stock()
        .loc[:, "TO_elec", _subscript_dict["PROTRA_CHP_I"]]
        .reset_coords(drop=True)
        .rename({"NRG_PROTRA_I": "PROTRA_CHP_I!"}),
        dim=["PROTRA_CHP_I!"],
    )


@component.add(
    name="check_CHP_heat_capacity_expansion",
    units="TW/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"protra_capacity_expansion": 1},
)
def check_chp_heat_capacity_expansion():
    return sum(
        protra_capacity_expansion()
        .loc[:, "TO_heat", _subscript_dict["PROTRA_CHP_I"]]
        .reset_coords(drop=True)
        .rename({"NRG_PROTRA_I": "PROTRA_CHP_I!"}),
        dim=["PROTRA_CHP_I!"],
    )


@component.add(
    name="check_CHP_heat_capacity_stock",
    units="TW",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"protra_capacity_stock": 1},
)
def check_chp_heat_capacity_stock():
    return sum(
        protra_capacity_stock()
        .loc[:, "TO_heat", _subscript_dict["PROTRA_CHP_I"]]
        .reset_coords(drop=True)
        .rename({"NRG_PROTRA_I": "PROTRA_CHP_I!"}),
        dim=["PROTRA_CHP_I!"],
    )


@component.add(
    name="check_global_aggregated_shortfall_allocation",
    units="EJ/Year",
    subscripts=["NRG_TO_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"protra_shortfall_allocation": 1},
)
def check_global_aggregated_shortfall_allocation():
    return sum(
        protra_shortfall_allocation().rename(
            {"REGIONS_9_I": "REGIONS_9_I!", "NRG_PROTRA_I": "NRG_PROTRA_I!"}
        ),
        dim=["REGIONS_9_I!", "NRG_PROTRA_I!"],
    )


@component.add(
    name="check_global_PROTRA_capacity_expansion",
    units="TW/Year",
    subscripts=["NRG_TO_I", "NRG_PROTRA_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"protra_capacity_expansion": 1},
)
def check_global_protra_capacity_expansion():
    """
    aggregated capacity expansion
    """
    return sum(
        protra_capacity_expansion().rename({"REGIONS_9_I": "REGIONS_9_I!"}),
        dim=["REGIONS_9_I!"],
    )


@component.add(
    name="check_HP_capacity_expansion",
    units="TW/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"protra_capacity_expansion": 1},
)
def check_hp_capacity_expansion():
    return sum(
        protra_capacity_expansion()
        .loc[:, "TO_heat", _subscript_dict["PROTRA_HP_I"]]
        .reset_coords(drop=True)
        .rename({"NRG_PROTRA_I": "PROTRA_HP_I!"}),
        dim=["PROTRA_HP_I!"],
    )


@component.add(
    name="check_HP_capacity_stock",
    units="TW",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"protra_capacity_stock": 1},
)
def check_hp_capacity_stock():
    return sum(
        protra_capacity_stock()
        .loc[:, "TO_heat", _subscript_dict["PROTRA_HP_I"]]
        .reset_coords(drop=True)
        .rename({"NRG_PROTRA_I": "PROTRA_HP_I!"}),
        dim=["PROTRA_HP_I!"],
    )


@component.add(
    name="check_PP_capacity_expansion",
    units="TW/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"protra_capacity_expansion": 1},
)
def check_pp_capacity_expansion():
    return sum(
        protra_capacity_expansion()
        .loc[:, "TO_elec", _subscript_dict["PROTRA_PP_I"]]
        .reset_coords(drop=True)
        .rename({"NRG_PROTRA_I": "PROTRA_PP_I!"}),
        dim=["PROTRA_PP_I!"],
    )


@component.add(
    name="check_PP_capacity_stock",
    units="TW",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"protra_capacity_stock": 1},
)
def check_pp_capacity_stock():
    return sum(
        protra_capacity_stock()
        .loc[:, "TO_elec", _subscript_dict["PROTRA_PP_I"]]
        .reset_coords(drop=True)
        .rename({"NRG_PROTRA_I": "PROTRA_PP_I!"}),
        dim=["PROTRA_PP_I!"],
    )


@component.add(
    name="check_PROTRA_elec_shortfall_allocation",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_elec_expansion_request": 1,
        "remaining_elec_shortfall_to_be_allocated": 1,
        "protra_elec_shortfall_allocation": 1,
    },
)
def check_protra_elec_shortfall_allocation():
    return np.minimum(
        sum(
            protra_elec_expansion_request()
            .loc[:, "TO_elec", :]
            .reset_coords(drop=True)
            .rename({"NRG_PRO_I": "NRG_PRO_I!"}),
            dim=["NRG_PRO_I!"],
        ),
        remaining_elec_shortfall_to_be_allocated()
        .loc[:, "TO_elec"]
        .reset_coords(drop=True),
    ) - sum(
        protra_elec_shortfall_allocation()
        .loc[:, "TO_elec", :]
        .reset_coords(drop=True)
        .rename({"NRG_PRO_I": "NRG_PRO_I!"}),
        dim=["NRG_PRO_I!"],
    )


@component.add(
    name="check_PROTRA_heat_shortfall_allocation",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_chp_and_hp_expansion_request": 1,
        "to_shortfall": 1,
        "protra_heat_shortfall_allocation": 1,
    },
)
def check_protra_heat_shortfall_allocation():
    return np.minimum(
        sum(
            protra_chp_and_hp_expansion_request()
            .loc[:, "TO_heat", :]
            .reset_coords(drop=True)
            .rename({"NRG_PRO_I": "NRG_PRO_I!"}),
            dim=["NRG_PRO_I!"],
        ),
        to_shortfall().loc[:, "TO_heat"].reset_coords(drop=True),
    ) - sum(
        protra_heat_shortfall_allocation()
        .loc[:, "TO_heat", :]
        .reset_coords(drop=True)
        .rename({"NRG_PRO_I": "NRG_PRO_I!"}),
        dim=["NRG_PRO_I!"],
    )


@component.add(
    name="CHECK_remaining_global_shortfall_after_elec_allocation",
    units="EJ/Year",
    subscripts=["NRG_TO_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "remaining_global_shortfall_after_heat_allocation": 2,
        "protra_elec_shortfall_allocation": 1,
    },
)
def check_remaining_global_shortfall_after_elec_allocation():
    """
    check variable: remaining global shortfall by commodity
    """
    value = xr.DataArray(
        np.nan, {"NRG_TO_I": _subscript_dict["NRG_TO_I"]}, ["NRG_TO_I"]
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[["TO_elec"]] = False
    value.values[
        except_subs.values
    ] = remaining_global_shortfall_after_heat_allocation().values[except_subs.values]
    value.loc[["TO_elec"]] = float(
        remaining_global_shortfall_after_heat_allocation().loc["TO_elec"]
    ) - sum(
        protra_elec_shortfall_allocation()
        .loc[:, "TO_elec", _subscript_dict["PROTRA_PP_I"]]
        .reset_coords(drop=True)
        .rename({"REGIONS_9_I": "REGIONS_9_I!", "NRG_PRO_I": "PROTRA_PP_I!"}),
        dim=["REGIONS_9_I!", "PROTRA_PP_I!"],
    )
    return value


@component.add(
    name="CHP_capacity_utilization_rate",
    subscripts=["REGIONS_9_I", "NRG_COMMODITIES_I", "NRG_PROTRA_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={"protra_capacity_utilization_rate": 1},
)
def chp_capacity_utilization_rate():
    """
    Rate of CHP capacity utilization to adjust the allocates.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "NRG_COMMODITIES_I": _subscript_dict["NRG_COMMODITIES_I"],
            "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
        },
        ["REGIONS_9_I", "NRG_COMMODITIES_I", "NRG_PROTRA_I"],
    )
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[:, ["TO_elec"], :] = True
    except_subs.loc[:, ["TO_elec"], _subscript_dict["PROTRA_CHP_I"]] = False
    value.values[except_subs.values] = 1
    value.loc[:, ["TO_elec"], _subscript_dict["PROTRA_CHP_I"]] = (
        protra_capacity_utilization_rate()
        .loc[:, _subscript_dict["PROTRA_CHP_I"]]
        .rename({"NRG_PROTRA_I": "PROTRA_CHP_I"})
        .expand_dims({"NRG_COMMODITIES_I": ["TO_elec"]}, 1)
        .values
    )
    return value


@component.add(
    name="DELAYED_PROTRA_CAPACITY_EMPIRICAL",
    units="TW",
    subscripts=["REGIONS_36_I", "NRG_TO_I", "NRG_PROTRA_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_protra_capacity_empirical": 1},
    other_deps={
        "_delayfixed_delayed_protra_capacity_empirical": {
            "initial": {"initial_protra_capacity_stock": 1},
            "step": {"protra_capacity_empirical_in_tw": 1},
        }
    },
)
def delayed_protra_capacity_empirical():
    """
    delayed capacity
    """
    return _delayfixed_delayed_protra_capacity_empirical()


_delayfixed_delayed_protra_capacity_empirical = DelayFixed(
    lambda: protra_capacity_empirical_in_tw(),
    lambda: 1,
    lambda: initial_protra_capacity_stock(),
    time_step,
    "_delayfixed_delayed_protra_capacity_empirical",
)


@component.add(
    name="EXOGENOUS_TO_RESERVE_FACTOR",
    units="DMNL",
    subscripts=["REGIONS_9_I", "NRG_TO_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"overcapacity_factor_empiric": 1},
)
def exogenous_to_reserve_factor():
    """
    exogeneous factor for the reserve factor in capacity expansion for stability testing purposes elec: 1.296 heat: 1.15 rest: 1.00
    """
    return overcapacity_factor_empiric()


@component.add(
    name="global_max_TO_available_from_existing_stock_by_commodity",
    units="EJ/Year",
    subscripts=["NRG_TO_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"to_available_by_commodity": 1},
)
def global_max_to_available_from_existing_stock_by_commodity():
    return sum(
        to_available_by_commodity().rename({"REGIONS_9_I": "REGIONS_9_I!"}),
        dim=["REGIONS_9_I!"],
    )


@component.add(
    name="global_PROTRA_capacity_stock",
    units="TW",
    subscripts=["NRG_TO_I", "NRG_PROTRA_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"protra_capacity_stock": 1},
)
def global_protra_capacity_stock():
    """
    globaly aggregated capacity stock
    """
    return sum(
        protra_capacity_stock().rename({"REGIONS_9_I": "REGIONS_9_I!"}),
        dim=["REGIONS_9_I!"],
    )


@component.add(
    name="global_TO_decomissioned_by_commodity",
    units="EJ/Year",
    subscripts=["NRG_TO_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"to_decomissioned_by_commodity": 1},
)
def global_to_decomissioned_by_commodity():
    return sum(
        to_decomissioned_by_commodity().rename({"REGIONS_9_I": "REGIONS_9_I!"}),
        dim=["REGIONS_9_I!"],
    )


@component.add(
    name="global_TO_required",
    units="EJ/Year",
    subscripts=["NRG_TO_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"to_required": 1},
)
def global_to_required():
    return sum(
        to_required().rename({"REGIONS_9_I": "REGIONS_9_I!"}), dim=["REGIONS_9_I!"]
    )


@component.add(
    name="global_TO_shortfall",
    units="EJ/Year",
    subscripts=["NRG_TO_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"to_shortfall": 1},
)
def global_to_shortfall():
    """
    total global shortfall to be allocated to the different technologies
    """
    return sum(
        to_shortfall().rename({"REGIONS_9_I": "REGIONS_9_I!"}), dim=["REGIONS_9_I!"]
    )


@component.add(
    name="INITIAL_PROTRA_CAPACITY_STOCK",
    units="TW",
    subscripts=["REGIONS_36_I", "NRG_TO_I", "NRG_PROTRA_I"],
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_initial_protra_capacity_stock": 1},
    other_deps={
        "_initial_initial_protra_capacity_stock": {
            "initial": {"protra_capacity_empirical_in_tw": 1},
            "step": {},
        }
    },
)
def initial_protra_capacity_stock():
    """
    initial capacity stock (in year 2005)
    """
    return _initial_initial_protra_capacity_stock()


_initial_initial_protra_capacity_stock = Initial(
    lambda: protra_capacity_empirical_in_tw(), "_initial_initial_protra_capacity_stock"
)


@component.add(
    name="max_TO_from_existing_stock_by_PROTRA_delayed",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_TO_I", "NRG_PROTRA_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_max_to_from_existing_stock_by_protra_delayed": 1},
    other_deps={
        "_delayfixed_max_to_from_existing_stock_by_protra_delayed": {
            "initial": {"time_step": 1},
            "step": {"max_to_from_existing_stock_by_protra": 1},
        }
    },
)
def max_to_from_existing_stock_by_protra_delayed():
    return _delayfixed_max_to_from_existing_stock_by_protra_delayed()


_delayfixed_max_to_from_existing_stock_by_protra_delayed = DelayFixed(
    lambda: max_to_from_existing_stock_by_protra()
    .loc[:, :, _subscript_dict["NRG_PROTRA_I"]]
    .rename({"NRG_PRO_I": "NRG_PROTRA_I"}),
    lambda: time_step(),
    lambda: xr.DataArray(
        0,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "NRG_TO_I": _subscript_dict["NRG_TO_I"],
            "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
        },
        ["REGIONS_9_I", "NRG_TO_I", "NRG_PROTRA_I"],
    ),
    time_step,
    "_delayfixed_max_to_from_existing_stock_by_protra_delayed",
)


@component.add(
    name="net_PROTRA_capacity_expansion_annual_growth",
    units="1/Year",
    subscripts=["REGIONS_9_I", "NRG_TO_I", "NRG_PROTRA_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_capacity_expansion": 1,
        "protra_capacity_decommissioning": 1,
        "protra_capacity_stock": 1,
    },
)
def net_protra_capacity_expansion_annual_growth():
    """
    Net annual growth of capacity expansion (expressed as a decimal).
    """
    return zidz(
        protra_capacity_expansion() - protra_capacity_decommissioning(),
        protra_capacity_stock(),
    )


@component.add(
    name="OVERCAPACITY_FACTOR_EMPIRIC",
    units="DMNL",
    subscripts=["REGIONS_9_I", "NRG_TO_I"],
    comp_type="Constant",
    comp_subtype="External, Normal",
    depends_on={"__external__": "_ext_constant_overcapacity_factor_empiric"},
)
def overcapacity_factor_empiric():
    """
    Empirical overcapacity factors for electricity and heat. Note that for heat overcapacity factors are generally higher (in those regions where we have significant heat demand and capacities), for those countries without significant demand it was set to 1.25 on default.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "NRG_TO_I": _subscript_dict["NRG_TO_I"],
        },
        ["REGIONS_9_I", "NRG_TO_I"],
    )
    def_subs = xr.zeros_like(value, dtype=bool)
    def_subs.loc[:, ["TO_elec"]] = True
    def_subs.loc[:, ["TO_heat"]] = True
    value.values[def_subs.values] = _ext_constant_overcapacity_factor_empiric().values[
        def_subs.values
    ]
    value.loc[:, ["TO_gas"]] = 1
    value.loc[:, ["TO_hydrogen"]] = 1
    value.loc[:, ["TO_liquid"]] = 1
    value.loc[:, ["TO_solid_bio"]] = 1
    value.loc[:, ["TO_solid_fossil"]] = 1
    return value


_ext_constant_overcapacity_factor_empiric = ExtConstant(
    "model_parameters/energy/energy.xlsm",
    "Common",
    "OVERCAPACITY_FACTOR_ELEC*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"], "NRG_TO_I": ["TO_elec"]},
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "NRG_TO_I": _subscript_dict["NRG_TO_I"],
    },
    "_ext_constant_overcapacity_factor_empiric",
)

_ext_constant_overcapacity_factor_empiric.add(
    "model_parameters/energy/energy.xlsm",
    "Common",
    "OVERCAPACITY_FACTOR_HEAT*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"], "NRG_TO_I": ["TO_heat"]},
)


@component.add(
    name="production_from_CHP_expansion",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_TO_I", "PROTRA_CHP_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "max_to_from_existing_stock_by_protra": 1,
        "protra_heat_shortfall_allocation": 2,
        "chp_heat_power_ratio_9r": 1,
    },
)
def production_from_chp_expansion():
    """
    elec and heat production from heat allocation IF_THEN_ELSE( max_TO_from_existing_stock_by_PROTRA[REGIONS_9_I, TO_heat, PROTRA_CHP_I] = 0 , 0 , PROTRA_heat_shortfall_allocation[REGIONS_9_I, TO_heat, PROTRA_CHP_I] / max_TO_from_existing_stock_by_PROTRA[REGIONS_9_I, TO_heat, PROTRA_CHP_I] * max_TO_from_existing_stock_by_PROTRA[REGIONS_9_I, TO_elec, PROTRA_CHP_I] )
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "NRG_TO_I": _subscript_dict["NRG_TO_I"],
            "PROTRA_CHP_I": _subscript_dict["PROTRA_CHP_I"],
        },
        ["REGIONS_9_I", "NRG_TO_I", "PROTRA_CHP_I"],
    )
    value.loc[:, ["TO_elec"], :] = (
        if_then_else(
            max_to_from_existing_stock_by_protra()
            .loc[:, "TO_heat", _subscript_dict["PROTRA_CHP_I"]]
            .reset_coords(drop=True)
            .rename({"NRG_PRO_I": "PROTRA_CHP_I"})
            == 0,
            lambda: xr.DataArray(
                0,
                {
                    "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                    "PROTRA_CHP_I": _subscript_dict["PROTRA_CHP_I"],
                },
                ["REGIONS_9_I", "PROTRA_CHP_I"],
            ),
            lambda: protra_heat_shortfall_allocation()
            .loc[:, "TO_heat", _subscript_dict["PROTRA_CHP_I"]]
            .reset_coords(drop=True)
            .rename({"NRG_PRO_I": "PROTRA_CHP_I"})
            / chp_heat_power_ratio_9r(),
        )
        .expand_dims({"NRG_COMMODITIES_I": ["TO_elec"]}, 1)
        .values
    )
    value.loc[:, ["TO_heat"], :] = (
        protra_heat_shortfall_allocation()
        .loc[:, "TO_heat", _subscript_dict["PROTRA_CHP_I"]]
        .reset_coords(drop=True)
        .rename({"NRG_PRO_I": "PROTRA_CHP_I"})
        .expand_dims({"NRG_COMMODITIES_I": ["TO_heat"]}, 1)
        .values
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, ["TO_elec"], :] = False
    except_subs.loc[:, ["TO_heat"], :] = False
    value.values[except_subs.values] = 0
    return value


@component.add(
    name="production_from_HP_expansion",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_TO_I", "NRG_PRO_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={"protra_heat_shortfall_allocation": 1},
)
def production_from_hp_expansion():
    """
    production of Heatplants from heat shortfall allocation
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "NRG_TO_I": _subscript_dict["NRG_TO_I"],
            "NRG_PRO_I": _subscript_dict["NRG_PRO_I"],
        },
        ["REGIONS_9_I", "NRG_TO_I", "NRG_PRO_I"],
    )
    value.loc[:, ["TO_heat"], _subscript_dict["PROTRA_HP_I"]] = (
        protra_heat_shortfall_allocation()
        .loc[:, "TO_heat", _subscript_dict["PROTRA_HP_I"]]
        .reset_coords(drop=True)
        .rename({"NRG_PRO_I": "PROTRA_HP_I"})
        .expand_dims({"NRG_COMMODITIES_I": ["TO_heat"]}, 1)
        .values
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, ["TO_heat"], _subscript_dict["PROTRA_HP_I"]] = False
    value.values[except_subs.values] = 0
    return value


@component.add(
    name="PROTRA_capacity_decommissioning",
    units="TW/Year",
    subscripts=["REGIONS_9_I", "NRG_TO_I", "NRG_PROTRA_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 2,
        "protra_capacity_variation_empirical": 3,
        "protra_capacity_stock": 1,
        "protra_lifetime": 1,
    },
)
def protra_capacity_decommissioning():
    """
    Transformation capacities that are being decomissioned each year (depends solely on the lifetime/depreciation periode of the power plant)
    """
    return if_then_else(
        np.logical_and(
            time() < 2020,
            protra_capacity_variation_empirical()
            .loc[_subscript_dict["REGIONS_9_I"], :, :]
            .rename({"REGIONS_36_I": "REGIONS_9_I"})
            < 0,
        ),
        lambda: -protra_capacity_variation_empirical()
        .loc[_subscript_dict["REGIONS_9_I"], :, :]
        .rename({"REGIONS_36_I": "REGIONS_9_I"}),
        lambda: if_then_else(
            np.logical_and(
                time() < 2020,
                protra_capacity_variation_empirical()
                .loc[_subscript_dict["REGIONS_9_I"], :, :]
                .rename({"REGIONS_36_I": "REGIONS_9_I"})
                >= 0,
            ),
            lambda: xr.DataArray(
                0,
                {
                    "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                    "NRG_TO_I": _subscript_dict["NRG_TO_I"],
                    "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
                },
                ["REGIONS_9_I", "NRG_TO_I", "NRG_PROTRA_I"],
            ),
            lambda: protra_capacity_stock() / protra_lifetime(),
        ),
    )


@component.add(
    name="PROTRA_capacity_decommissioning_35R",
    units="TW/Year",
    subscripts=["REGIONS_35_I", "NRG_TO_I", "NRG_PROTRA_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_capacity_decommissioning": 1,
        "protra_capacity_decommissioning_eu27": 1,
    },
)
def protra_capacity_decommissioning_35r():
    """
    Capacity decommissioning of the PROTRA for the 35 regions downscaling the information from EU27 aggregated to the 27 EU countries taking as reference the empirical variation of capacity stock for each country.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "NRG_TO_I": _subscript_dict["NRG_TO_I"],
            "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
        },
        ["REGIONS_35_I", "NRG_TO_I", "NRG_PROTRA_I"],
    )
    value.loc[_subscript_dict["REGIONS_8_I"], :, :] = (
        protra_capacity_decommissioning()
        .loc[_subscript_dict["REGIONS_8_I"], :, :]
        .rename({"REGIONS_9_I": "REGIONS_8_I"})
        .values
    )
    value.loc[
        _subscript_dict["REGIONS_EU27_I"], :, :
    ] = protra_capacity_decommissioning_eu27().values
    return value


@component.add(
    name="PROTRA_capacity_decommissioning_EU27",
    units="TW/Year",
    subscripts=["REGIONS_EU27_I", "NRG_TO_I", "NRG_PROTRA_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "protra_capacity_variation_empirical": 1,
        "protra_capacity_stock_eu27": 1,
        "protra_lifetime": 1,
    },
)
def protra_capacity_decommissioning_eu27():
    """
    PROTRA capacity stock decommissioning for the 27 EU countries. Until 2020 historic data and thereafter downscaling the information from the aggregated EU27. The MIN function takes only those empirical negative values which mean new capacity.
    """
    return if_then_else(
        time() <= 2020,
        lambda: -np.minimum(
            0,
            protra_capacity_variation_empirical()
            .loc[_subscript_dict["REGIONS_EU27_I"], :, :]
            .rename({"REGIONS_36_I": "REGIONS_EU27_I"}),
        ),
        lambda: protra_capacity_stock_eu27()
        / protra_lifetime().loc["EU27", :].reset_coords(drop=True),
    )


@component.add(
    name="PROTRA_CAPACITY_EMPIRICAL",
    units="GW",
    subscripts=["REGIONS_36_I", "NRG_TO_I", "NRG_PROTRA_I"],
    comp_type="Data, Constant",
    comp_subtype="External, Normal",
    depends_on={
        "__external__": "_ext_data_protra_capacity_empirical",
        "__data__": "_ext_data_protra_capacity_empirical",
        "time": 1,
    },
)
def protra_capacity_empirical():
    """
    Empirical capacites of conversion technologies, disaggregated in WILIAM technologies. Source: JRC_IDEES, IEA, IRENA, IAE; (note: unit in excel file is GW)
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_36_I": _subscript_dict["REGIONS_36_I"],
            "NRG_TO_I": _subscript_dict["NRG_TO_I"],
            "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
        },
        ["REGIONS_36_I", "NRG_TO_I", "NRG_PROTRA_I"],
    )
    def_subs = xr.zeros_like(value, dtype=bool)
    def_subs.loc[
        ["AUSTRIA"],
        ["TO_heat"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_HP_gas_fuels",
            "PROTRA_HP_solid_bio",
            "PROTRA_HP_geothermal",
            "PROTRA_HP_liquid_fuels",
            "PROTRA_HP_solar_DEACTIVATED",
            "PROTRA_HP_solid_fossil",
            "PROTRA_HP_waste",
        ],
    ] = True
    def_subs.loc[
        ["AUSTRIA"],
        ["TO_elec"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_PP_solid_bio",
            "PROTRA_PP_solid_bio_CCS",
            "PROTRA_PP_gas_fuels",
            "PROTRA_PP_gas_fuels_CCS",
            "PROTRA_PP_geothermal",
            "PROTRA_PP_hydropower_dammed",
            "PROTRA_PP_hydropower_run_of_river",
            "PROTRA_PP_liquid_fuels",
            "PROTRA_PP_liquid_fuels_CCS",
            "PROTRA_PP_nuclear",
            "PROTRA_PP_oceanic",
            "PROTRA_PP_solar_CSP",
            "PROTRA_PP_solar_open_space_PV",
            "PROTRA_PP_solar_urban_PV",
            "PROTRA_PP_solid_fossil",
            "PROTRA_PP_solid_fossil_CCS",
            "PROTRA_PP_waste",
            "PROTRA_PP_waste_CCS",
            "PROTRA_PP_wind_offshore",
            "PROTRA_PP_wind_onshore",
        ],
    ] = True
    def_subs.loc[
        ["BELGIUM"],
        ["TO_heat"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_HP_gas_fuels",
            "PROTRA_HP_solid_bio",
            "PROTRA_HP_geothermal",
            "PROTRA_HP_liquid_fuels",
            "PROTRA_HP_solar_DEACTIVATED",
            "PROTRA_HP_solid_fossil",
            "PROTRA_HP_waste",
        ],
    ] = True
    def_subs.loc[
        ["BELGIUM"],
        ["TO_elec"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_PP_solid_bio",
            "PROTRA_PP_solid_bio_CCS",
            "PROTRA_PP_gas_fuels",
            "PROTRA_PP_gas_fuels_CCS",
            "PROTRA_PP_geothermal",
            "PROTRA_PP_hydropower_dammed",
            "PROTRA_PP_hydropower_run_of_river",
            "PROTRA_PP_liquid_fuels",
            "PROTRA_PP_liquid_fuels_CCS",
            "PROTRA_PP_nuclear",
            "PROTRA_PP_oceanic",
            "PROTRA_PP_solar_CSP",
            "PROTRA_PP_solar_open_space_PV",
            "PROTRA_PP_solar_urban_PV",
            "PROTRA_PP_solid_fossil",
            "PROTRA_PP_solid_fossil_CCS",
            "PROTRA_PP_waste",
            "PROTRA_PP_waste_CCS",
            "PROTRA_PP_wind_offshore",
            "PROTRA_PP_wind_onshore",
        ],
    ] = True
    def_subs.loc[
        ["BULGARIA"],
        ["TO_heat"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_HP_gas_fuels",
            "PROTRA_HP_solid_bio",
            "PROTRA_HP_geothermal",
            "PROTRA_HP_liquid_fuels",
            "PROTRA_HP_solar_DEACTIVATED",
            "PROTRA_HP_solid_fossil",
            "PROTRA_HP_waste",
        ],
    ] = True
    def_subs.loc[
        ["BULGARIA"],
        ["TO_elec"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_PP_solid_bio",
            "PROTRA_PP_solid_bio_CCS",
            "PROTRA_PP_gas_fuels",
            "PROTRA_PP_gas_fuels_CCS",
            "PROTRA_PP_geothermal",
            "PROTRA_PP_hydropower_dammed",
            "PROTRA_PP_hydropower_run_of_river",
            "PROTRA_PP_liquid_fuels",
            "PROTRA_PP_liquid_fuels_CCS",
            "PROTRA_PP_nuclear",
            "PROTRA_PP_oceanic",
            "PROTRA_PP_solar_CSP",
            "PROTRA_PP_solar_open_space_PV",
            "PROTRA_PP_solar_urban_PV",
            "PROTRA_PP_solid_fossil",
            "PROTRA_PP_solid_fossil_CCS",
            "PROTRA_PP_waste",
            "PROTRA_PP_waste_CCS",
            "PROTRA_PP_wind_offshore",
            "PROTRA_PP_wind_onshore",
        ],
    ] = True
    def_subs.loc[
        ["CHINA"],
        ["TO_heat"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_HP_gas_fuels",
            "PROTRA_HP_solid_bio",
            "PROTRA_HP_geothermal",
            "PROTRA_HP_liquid_fuels",
            "PROTRA_HP_solar_DEACTIVATED",
            "PROTRA_HP_solid_fossil",
            "PROTRA_HP_waste",
        ],
    ] = True
    def_subs.loc[
        ["CHINA"],
        ["TO_elec"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_PP_solid_bio",
            "PROTRA_PP_solid_bio_CCS",
            "PROTRA_PP_gas_fuels",
            "PROTRA_PP_gas_fuels_CCS",
            "PROTRA_PP_geothermal",
            "PROTRA_PP_hydropower_dammed",
            "PROTRA_PP_hydropower_run_of_river",
            "PROTRA_PP_liquid_fuels",
            "PROTRA_PP_liquid_fuels_CCS",
            "PROTRA_PP_nuclear",
            "PROTRA_PP_oceanic",
            "PROTRA_PP_solar_CSP",
            "PROTRA_PP_solar_open_space_PV",
            "PROTRA_PP_solar_urban_PV",
            "PROTRA_PP_solid_fossil",
            "PROTRA_PP_solid_fossil_CCS",
            "PROTRA_PP_waste",
            "PROTRA_PP_waste_CCS",
            "PROTRA_PP_wind_offshore",
            "PROTRA_PP_wind_onshore",
        ],
    ] = True
    def_subs.loc[
        ["CROATIA"],
        ["TO_heat"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_HP_gas_fuels",
            "PROTRA_HP_solid_bio",
            "PROTRA_HP_geothermal",
            "PROTRA_HP_liquid_fuels",
            "PROTRA_HP_solar_DEACTIVATED",
            "PROTRA_HP_solid_fossil",
            "PROTRA_HP_waste",
        ],
    ] = True
    def_subs.loc[
        ["CROATIA"],
        ["TO_elec"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_PP_solid_bio",
            "PROTRA_PP_solid_bio_CCS",
            "PROTRA_PP_gas_fuels",
            "PROTRA_PP_gas_fuels_CCS",
            "PROTRA_PP_geothermal",
            "PROTRA_PP_hydropower_dammed",
            "PROTRA_PP_hydropower_run_of_river",
            "PROTRA_PP_liquid_fuels",
            "PROTRA_PP_liquid_fuels_CCS",
            "PROTRA_PP_nuclear",
            "PROTRA_PP_oceanic",
            "PROTRA_PP_solar_CSP",
            "PROTRA_PP_solar_open_space_PV",
            "PROTRA_PP_solar_urban_PV",
            "PROTRA_PP_solid_fossil",
            "PROTRA_PP_solid_fossil_CCS",
            "PROTRA_PP_waste",
            "PROTRA_PP_waste_CCS",
            "PROTRA_PP_wind_offshore",
            "PROTRA_PP_wind_onshore",
        ],
    ] = True
    def_subs.loc[
        ["CYPRUS"],
        ["TO_heat"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_HP_gas_fuels",
            "PROTRA_HP_solid_bio",
            "PROTRA_HP_geothermal",
            "PROTRA_HP_liquid_fuels",
            "PROTRA_HP_solar_DEACTIVATED",
            "PROTRA_HP_solid_fossil",
            "PROTRA_HP_waste",
        ],
    ] = True
    def_subs.loc[
        ["CYPRUS"],
        ["TO_elec"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_PP_solid_bio",
            "PROTRA_PP_solid_bio_CCS",
            "PROTRA_PP_gas_fuels",
            "PROTRA_PP_gas_fuels_CCS",
            "PROTRA_PP_geothermal",
            "PROTRA_PP_hydropower_dammed",
            "PROTRA_PP_hydropower_run_of_river",
            "PROTRA_PP_liquid_fuels",
            "PROTRA_PP_liquid_fuels_CCS",
            "PROTRA_PP_nuclear",
            "PROTRA_PP_oceanic",
            "PROTRA_PP_solar_CSP",
            "PROTRA_PP_solar_open_space_PV",
            "PROTRA_PP_solar_urban_PV",
            "PROTRA_PP_solid_fossil",
            "PROTRA_PP_solid_fossil_CCS",
            "PROTRA_PP_waste",
            "PROTRA_PP_waste_CCS",
            "PROTRA_PP_wind_offshore",
            "PROTRA_PP_wind_onshore",
        ],
    ] = True
    def_subs.loc[
        ["CZECH_REPUBLIC"],
        ["TO_heat"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_HP_gas_fuels",
            "PROTRA_HP_solid_bio",
            "PROTRA_HP_geothermal",
            "PROTRA_HP_liquid_fuels",
            "PROTRA_HP_solar_DEACTIVATED",
            "PROTRA_HP_solid_fossil",
            "PROTRA_HP_waste",
        ],
    ] = True
    def_subs.loc[
        ["CZECH_REPUBLIC"],
        ["TO_elec"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_PP_solid_bio",
            "PROTRA_PP_solid_bio_CCS",
            "PROTRA_PP_gas_fuels",
            "PROTRA_PP_gas_fuels_CCS",
            "PROTRA_PP_geothermal",
            "PROTRA_PP_hydropower_dammed",
            "PROTRA_PP_hydropower_run_of_river",
            "PROTRA_PP_liquid_fuels",
            "PROTRA_PP_liquid_fuels_CCS",
            "PROTRA_PP_nuclear",
            "PROTRA_PP_oceanic",
            "PROTRA_PP_solar_CSP",
            "PROTRA_PP_solar_open_space_PV",
            "PROTRA_PP_solar_urban_PV",
            "PROTRA_PP_solid_fossil",
            "PROTRA_PP_solid_fossil_CCS",
            "PROTRA_PP_waste",
            "PROTRA_PP_waste_CCS",
            "PROTRA_PP_wind_offshore",
            "PROTRA_PP_wind_onshore",
        ],
    ] = True
    def_subs.loc[
        ["DENMARK"],
        ["TO_heat"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_HP_gas_fuels",
            "PROTRA_HP_solid_bio",
            "PROTRA_HP_geothermal",
            "PROTRA_HP_liquid_fuels",
            "PROTRA_HP_solar_DEACTIVATED",
            "PROTRA_HP_solid_fossil",
            "PROTRA_HP_waste",
        ],
    ] = True
    def_subs.loc[
        ["DENMARK"],
        ["TO_elec"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_PP_solid_bio",
            "PROTRA_PP_solid_bio_CCS",
            "PROTRA_PP_gas_fuels",
            "PROTRA_PP_gas_fuels_CCS",
            "PROTRA_PP_geothermal",
            "PROTRA_PP_hydropower_dammed",
            "PROTRA_PP_hydropower_run_of_river",
            "PROTRA_PP_liquid_fuels",
            "PROTRA_PP_liquid_fuels_CCS",
            "PROTRA_PP_nuclear",
            "PROTRA_PP_oceanic",
            "PROTRA_PP_solar_CSP",
            "PROTRA_PP_solar_open_space_PV",
            "PROTRA_PP_solar_urban_PV",
            "PROTRA_PP_solid_fossil",
            "PROTRA_PP_solid_fossil_CCS",
            "PROTRA_PP_waste",
            "PROTRA_PP_waste_CCS",
            "PROTRA_PP_wind_offshore",
            "PROTRA_PP_wind_onshore",
        ],
    ] = True
    def_subs.loc[
        ["EASOC"],
        ["TO_heat"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_HP_gas_fuels",
            "PROTRA_HP_solid_bio",
            "PROTRA_HP_geothermal",
            "PROTRA_HP_liquid_fuels",
            "PROTRA_HP_solar_DEACTIVATED",
            "PROTRA_HP_solid_fossil",
            "PROTRA_HP_waste",
        ],
    ] = True
    def_subs.loc[
        ["EASOC"],
        ["TO_elec"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_PP_solid_bio",
            "PROTRA_PP_solid_bio_CCS",
            "PROTRA_PP_gas_fuels",
            "PROTRA_PP_gas_fuels_CCS",
            "PROTRA_PP_geothermal",
            "PROTRA_PP_hydropower_dammed",
            "PROTRA_PP_hydropower_run_of_river",
            "PROTRA_PP_liquid_fuels",
            "PROTRA_PP_liquid_fuels_CCS",
            "PROTRA_PP_nuclear",
            "PROTRA_PP_oceanic",
            "PROTRA_PP_solar_CSP",
            "PROTRA_PP_solar_open_space_PV",
            "PROTRA_PP_solar_urban_PV",
            "PROTRA_PP_solid_fossil",
            "PROTRA_PP_solid_fossil_CCS",
            "PROTRA_PP_waste",
            "PROTRA_PP_waste_CCS",
            "PROTRA_PP_wind_offshore",
            "PROTRA_PP_wind_onshore",
        ],
    ] = True
    def_subs.loc[
        ["ESTONIA"],
        ["TO_heat"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_HP_gas_fuels",
            "PROTRA_HP_solid_bio",
            "PROTRA_HP_geothermal",
            "PROTRA_HP_liquid_fuels",
            "PROTRA_HP_solar_DEACTIVATED",
            "PROTRA_HP_solid_fossil",
            "PROTRA_HP_waste",
        ],
    ] = True
    def_subs.loc[
        ["ESTONIA"],
        ["TO_elec"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_PP_solid_bio",
            "PROTRA_PP_solid_bio_CCS",
            "PROTRA_PP_gas_fuels",
            "PROTRA_PP_gas_fuels_CCS",
            "PROTRA_PP_geothermal",
            "PROTRA_PP_hydropower_dammed",
            "PROTRA_PP_hydropower_run_of_river",
            "PROTRA_PP_liquid_fuels",
            "PROTRA_PP_liquid_fuels_CCS",
            "PROTRA_PP_nuclear",
            "PROTRA_PP_oceanic",
            "PROTRA_PP_solar_CSP",
            "PROTRA_PP_solar_open_space_PV",
            "PROTRA_PP_solar_urban_PV",
            "PROTRA_PP_solid_fossil",
            "PROTRA_PP_solid_fossil_CCS",
            "PROTRA_PP_waste",
            "PROTRA_PP_waste_CCS",
            "PROTRA_PP_wind_offshore",
            "PROTRA_PP_wind_onshore",
        ],
    ] = True
    def_subs.loc[
        ["EU27"],
        ["TO_heat"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_HP_gas_fuels",
            "PROTRA_HP_solid_bio",
            "PROTRA_HP_geothermal",
            "PROTRA_HP_liquid_fuels",
            "PROTRA_HP_solar_DEACTIVATED",
            "PROTRA_HP_solid_fossil",
            "PROTRA_HP_waste",
        ],
    ] = True
    def_subs.loc[
        ["EU27"],
        ["TO_elec"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_PP_solid_bio",
            "PROTRA_PP_solid_bio_CCS",
            "PROTRA_PP_gas_fuels",
            "PROTRA_PP_gas_fuels_CCS",
            "PROTRA_PP_geothermal",
            "PROTRA_PP_hydropower_dammed",
            "PROTRA_PP_hydropower_run_of_river",
            "PROTRA_PP_liquid_fuels",
            "PROTRA_PP_liquid_fuels_CCS",
            "PROTRA_PP_nuclear",
            "PROTRA_PP_oceanic",
            "PROTRA_PP_solar_CSP",
            "PROTRA_PP_solar_open_space_PV",
            "PROTRA_PP_solar_urban_PV",
            "PROTRA_PP_solid_fossil",
            "PROTRA_PP_solid_fossil_CCS",
            "PROTRA_PP_waste",
            "PROTRA_PP_waste_CCS",
            "PROTRA_PP_wind_offshore",
            "PROTRA_PP_wind_onshore",
        ],
    ] = True
    def_subs.loc[
        ["FINLAND"],
        ["TO_heat"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_HP_gas_fuels",
            "PROTRA_HP_solid_bio",
            "PROTRA_HP_geothermal",
            "PROTRA_HP_liquid_fuels",
            "PROTRA_HP_solar_DEACTIVATED",
            "PROTRA_HP_solid_fossil",
            "PROTRA_HP_waste",
        ],
    ] = True
    def_subs.loc[
        ["FINLAND"],
        ["TO_elec"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_PP_solid_bio",
            "PROTRA_PP_solid_bio_CCS",
            "PROTRA_PP_gas_fuels",
            "PROTRA_PP_gas_fuels_CCS",
            "PROTRA_PP_geothermal",
            "PROTRA_PP_hydropower_dammed",
            "PROTRA_PP_hydropower_run_of_river",
            "PROTRA_PP_liquid_fuels",
            "PROTRA_PP_liquid_fuels_CCS",
            "PROTRA_PP_nuclear",
            "PROTRA_PP_oceanic",
            "PROTRA_PP_solar_CSP",
            "PROTRA_PP_solar_open_space_PV",
            "PROTRA_PP_solar_urban_PV",
            "PROTRA_PP_solid_fossil",
            "PROTRA_PP_solid_fossil_CCS",
            "PROTRA_PP_waste",
            "PROTRA_PP_waste_CCS",
            "PROTRA_PP_wind_offshore",
            "PROTRA_PP_wind_onshore",
        ],
    ] = True
    def_subs.loc[
        ["FRANCE"],
        ["TO_heat"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_HP_gas_fuels",
            "PROTRA_HP_solid_bio",
            "PROTRA_HP_geothermal",
            "PROTRA_HP_liquid_fuels",
            "PROTRA_HP_solar_DEACTIVATED",
            "PROTRA_HP_solid_fossil",
            "PROTRA_HP_waste",
        ],
    ] = True
    def_subs.loc[
        ["FRANCE"],
        ["TO_elec"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_PP_solid_bio",
            "PROTRA_PP_solid_bio_CCS",
            "PROTRA_PP_gas_fuels",
            "PROTRA_PP_gas_fuels_CCS",
            "PROTRA_PP_geothermal",
            "PROTRA_PP_hydropower_dammed",
            "PROTRA_PP_hydropower_run_of_river",
            "PROTRA_PP_liquid_fuels",
            "PROTRA_PP_liquid_fuels_CCS",
            "PROTRA_PP_nuclear",
            "PROTRA_PP_oceanic",
            "PROTRA_PP_solar_CSP",
            "PROTRA_PP_solar_open_space_PV",
            "PROTRA_PP_solar_urban_PV",
            "PROTRA_PP_solid_fossil",
            "PROTRA_PP_solid_fossil_CCS",
            "PROTRA_PP_waste",
            "PROTRA_PP_waste_CCS",
            "PROTRA_PP_wind_offshore",
            "PROTRA_PP_wind_onshore",
        ],
    ] = True
    def_subs.loc[
        ["GERMANY"],
        ["TO_heat"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_HP_gas_fuels",
            "PROTRA_HP_solid_bio",
            "PROTRA_HP_geothermal",
            "PROTRA_HP_liquid_fuels",
            "PROTRA_HP_solar_DEACTIVATED",
            "PROTRA_HP_solid_fossil",
            "PROTRA_HP_waste",
        ],
    ] = True
    def_subs.loc[
        ["GERMANY"],
        ["TO_elec"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_PP_solid_bio",
            "PROTRA_PP_solid_bio_CCS",
            "PROTRA_PP_gas_fuels",
            "PROTRA_PP_gas_fuels_CCS",
            "PROTRA_PP_geothermal",
            "PROTRA_PP_hydropower_dammed",
            "PROTRA_PP_hydropower_run_of_river",
            "PROTRA_PP_liquid_fuels",
            "PROTRA_PP_liquid_fuels_CCS",
            "PROTRA_PP_nuclear",
            "PROTRA_PP_oceanic",
            "PROTRA_PP_solar_CSP",
            "PROTRA_PP_solar_open_space_PV",
            "PROTRA_PP_solar_urban_PV",
            "PROTRA_PP_solid_fossil",
            "PROTRA_PP_solid_fossil_CCS",
            "PROTRA_PP_waste",
            "PROTRA_PP_waste_CCS",
            "PROTRA_PP_wind_offshore",
            "PROTRA_PP_wind_onshore",
        ],
    ] = True
    def_subs.loc[
        ["GREECE"],
        ["TO_heat"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_HP_gas_fuels",
            "PROTRA_HP_solid_bio",
            "PROTRA_HP_geothermal",
            "PROTRA_HP_liquid_fuels",
            "PROTRA_HP_solar_DEACTIVATED",
            "PROTRA_HP_solid_fossil",
            "PROTRA_HP_waste",
        ],
    ] = True
    def_subs.loc[
        ["GREECE"],
        ["TO_elec"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_PP_solid_bio",
            "PROTRA_PP_solid_bio_CCS",
            "PROTRA_PP_gas_fuels",
            "PROTRA_PP_gas_fuels_CCS",
            "PROTRA_PP_geothermal",
            "PROTRA_PP_hydropower_dammed",
            "PROTRA_PP_hydropower_run_of_river",
            "PROTRA_PP_liquid_fuels",
            "PROTRA_PP_liquid_fuels_CCS",
            "PROTRA_PP_nuclear",
            "PROTRA_PP_oceanic",
            "PROTRA_PP_solar_CSP",
            "PROTRA_PP_solar_open_space_PV",
            "PROTRA_PP_solar_urban_PV",
            "PROTRA_PP_solid_fossil",
            "PROTRA_PP_solid_fossil_CCS",
            "PROTRA_PP_waste",
            "PROTRA_PP_waste_CCS",
            "PROTRA_PP_wind_offshore",
            "PROTRA_PP_wind_onshore",
        ],
    ] = True
    def_subs.loc[
        ["HUNGARY"],
        ["TO_heat"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_HP_gas_fuels",
            "PROTRA_HP_solid_bio",
            "PROTRA_HP_geothermal",
            "PROTRA_HP_liquid_fuels",
            "PROTRA_HP_solar_DEACTIVATED",
            "PROTRA_HP_solid_fossil",
            "PROTRA_HP_waste",
        ],
    ] = True
    def_subs.loc[
        ["HUNGARY"],
        ["TO_elec"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_PP_solid_bio",
            "PROTRA_PP_solid_bio_CCS",
            "PROTRA_PP_gas_fuels",
            "PROTRA_PP_gas_fuels_CCS",
            "PROTRA_PP_geothermal",
            "PROTRA_PP_hydropower_dammed",
            "PROTRA_PP_hydropower_run_of_river",
            "PROTRA_PP_liquid_fuels",
            "PROTRA_PP_liquid_fuels_CCS",
            "PROTRA_PP_nuclear",
            "PROTRA_PP_oceanic",
            "PROTRA_PP_solar_CSP",
            "PROTRA_PP_solar_open_space_PV",
            "PROTRA_PP_solar_urban_PV",
            "PROTRA_PP_solid_fossil",
            "PROTRA_PP_solid_fossil_CCS",
            "PROTRA_PP_waste",
            "PROTRA_PP_waste_CCS",
            "PROTRA_PP_wind_offshore",
            "PROTRA_PP_wind_onshore",
        ],
    ] = True
    def_subs.loc[
        ["INDIA"],
        ["TO_heat"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_HP_gas_fuels",
            "PROTRA_HP_solid_bio",
            "PROTRA_HP_geothermal",
            "PROTRA_HP_liquid_fuels",
            "PROTRA_HP_solar_DEACTIVATED",
            "PROTRA_HP_solid_fossil",
            "PROTRA_HP_waste",
        ],
    ] = True
    def_subs.loc[
        ["INDIA"],
        ["TO_elec"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_PP_solid_bio",
            "PROTRA_PP_solid_bio_CCS",
            "PROTRA_PP_gas_fuels",
            "PROTRA_PP_gas_fuels_CCS",
            "PROTRA_PP_geothermal",
            "PROTRA_PP_hydropower_dammed",
            "PROTRA_PP_hydropower_run_of_river",
            "PROTRA_PP_liquid_fuels",
            "PROTRA_PP_liquid_fuels_CCS",
            "PROTRA_PP_nuclear",
            "PROTRA_PP_oceanic",
            "PROTRA_PP_solar_CSP",
            "PROTRA_PP_solar_open_space_PV",
            "PROTRA_PP_solar_urban_PV",
            "PROTRA_PP_solid_fossil",
            "PROTRA_PP_solid_fossil_CCS",
            "PROTRA_PP_waste",
            "PROTRA_PP_waste_CCS",
            "PROTRA_PP_wind_offshore",
            "PROTRA_PP_wind_onshore",
        ],
    ] = True
    def_subs.loc[
        ["IRELAND"],
        ["TO_heat"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_HP_gas_fuels",
            "PROTRA_HP_solid_bio",
            "PROTRA_HP_geothermal",
            "PROTRA_HP_liquid_fuels",
            "PROTRA_HP_solar_DEACTIVATED",
            "PROTRA_HP_solid_fossil",
            "PROTRA_HP_waste",
        ],
    ] = True
    def_subs.loc[
        ["IRELAND"],
        ["TO_elec"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_PP_solid_bio",
            "PROTRA_PP_solid_bio_CCS",
            "PROTRA_PP_gas_fuels",
            "PROTRA_PP_gas_fuels_CCS",
            "PROTRA_PP_geothermal",
            "PROTRA_PP_hydropower_dammed",
            "PROTRA_PP_hydropower_run_of_river",
            "PROTRA_PP_liquid_fuels",
            "PROTRA_PP_liquid_fuels_CCS",
            "PROTRA_PP_nuclear",
            "PROTRA_PP_oceanic",
            "PROTRA_PP_solar_CSP",
            "PROTRA_PP_solar_open_space_PV",
            "PROTRA_PP_solar_urban_PV",
            "PROTRA_PP_solid_fossil",
            "PROTRA_PP_solid_fossil_CCS",
            "PROTRA_PP_waste",
            "PROTRA_PP_waste_CCS",
            "PROTRA_PP_wind_offshore",
            "PROTRA_PP_wind_onshore",
        ],
    ] = True
    def_subs.loc[
        ["ITALY"],
        ["TO_heat"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_HP_gas_fuels",
            "PROTRA_HP_solid_bio",
            "PROTRA_HP_geothermal",
            "PROTRA_HP_liquid_fuels",
            "PROTRA_HP_solar_DEACTIVATED",
            "PROTRA_HP_solid_fossil",
            "PROTRA_HP_waste",
        ],
    ] = True
    def_subs.loc[
        ["ITALY"],
        ["TO_elec"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_PP_solid_bio",
            "PROTRA_PP_solid_bio_CCS",
            "PROTRA_PP_gas_fuels",
            "PROTRA_PP_gas_fuels_CCS",
            "PROTRA_PP_geothermal",
            "PROTRA_PP_hydropower_dammed",
            "PROTRA_PP_hydropower_run_of_river",
            "PROTRA_PP_liquid_fuels",
            "PROTRA_PP_liquid_fuels_CCS",
            "PROTRA_PP_nuclear",
            "PROTRA_PP_oceanic",
            "PROTRA_PP_solar_CSP",
            "PROTRA_PP_solar_open_space_PV",
            "PROTRA_PP_solar_urban_PV",
            "PROTRA_PP_solid_fossil",
            "PROTRA_PP_solid_fossil_CCS",
            "PROTRA_PP_waste",
            "PROTRA_PP_waste_CCS",
            "PROTRA_PP_wind_offshore",
            "PROTRA_PP_wind_onshore",
        ],
    ] = True
    def_subs.loc[
        ["LATAM"],
        ["TO_heat"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_HP_gas_fuels",
            "PROTRA_HP_solid_bio",
            "PROTRA_HP_geothermal",
            "PROTRA_HP_liquid_fuels",
            "PROTRA_HP_solar_DEACTIVATED",
            "PROTRA_HP_solid_fossil",
            "PROTRA_HP_waste",
        ],
    ] = True
    def_subs.loc[
        ["LATAM"],
        ["TO_elec"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_PP_solid_bio",
            "PROTRA_PP_solid_bio_CCS",
            "PROTRA_PP_gas_fuels",
            "PROTRA_PP_gas_fuels_CCS",
            "PROTRA_PP_geothermal",
            "PROTRA_PP_hydropower_dammed",
            "PROTRA_PP_hydropower_run_of_river",
            "PROTRA_PP_liquid_fuels",
            "PROTRA_PP_liquid_fuels_CCS",
            "PROTRA_PP_nuclear",
            "PROTRA_PP_oceanic",
            "PROTRA_PP_solar_CSP",
            "PROTRA_PP_solar_open_space_PV",
            "PROTRA_PP_solar_urban_PV",
            "PROTRA_PP_solid_fossil",
            "PROTRA_PP_solid_fossil_CCS",
            "PROTRA_PP_waste",
            "PROTRA_PP_waste_CCS",
            "PROTRA_PP_wind_offshore",
            "PROTRA_PP_wind_onshore",
        ],
    ] = True
    def_subs.loc[
        ["LATVIA"],
        ["TO_heat"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_HP_gas_fuels",
            "PROTRA_HP_solid_bio",
            "PROTRA_HP_geothermal",
            "PROTRA_HP_liquid_fuels",
            "PROTRA_HP_solar_DEACTIVATED",
            "PROTRA_HP_solid_fossil",
            "PROTRA_HP_waste",
        ],
    ] = True
    def_subs.loc[
        ["LATVIA"],
        ["TO_elec"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_PP_solid_bio",
            "PROTRA_PP_solid_bio_CCS",
            "PROTRA_PP_gas_fuels",
            "PROTRA_PP_gas_fuels_CCS",
            "PROTRA_PP_geothermal",
            "PROTRA_PP_hydropower_dammed",
            "PROTRA_PP_hydropower_run_of_river",
            "PROTRA_PP_liquid_fuels",
            "PROTRA_PP_liquid_fuels_CCS",
            "PROTRA_PP_nuclear",
            "PROTRA_PP_oceanic",
            "PROTRA_PP_solar_CSP",
            "PROTRA_PP_solar_open_space_PV",
            "PROTRA_PP_solar_urban_PV",
            "PROTRA_PP_solid_fossil",
            "PROTRA_PP_solid_fossil_CCS",
            "PROTRA_PP_waste",
            "PROTRA_PP_waste_CCS",
            "PROTRA_PP_wind_offshore",
            "PROTRA_PP_wind_onshore",
        ],
    ] = True
    def_subs.loc[
        ["LITHUANIA"],
        ["TO_heat"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_HP_gas_fuels",
            "PROTRA_HP_solid_bio",
            "PROTRA_HP_geothermal",
            "PROTRA_HP_liquid_fuels",
            "PROTRA_HP_solar_DEACTIVATED",
            "PROTRA_HP_solid_fossil",
            "PROTRA_HP_waste",
        ],
    ] = True
    def_subs.loc[
        ["LITHUANIA"],
        ["TO_elec"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_PP_solid_bio",
            "PROTRA_PP_solid_bio_CCS",
            "PROTRA_PP_gas_fuels",
            "PROTRA_PP_gas_fuels_CCS",
            "PROTRA_PP_geothermal",
            "PROTRA_PP_hydropower_dammed",
            "PROTRA_PP_hydropower_run_of_river",
            "PROTRA_PP_liquid_fuels",
            "PROTRA_PP_liquid_fuels_CCS",
            "PROTRA_PP_nuclear",
            "PROTRA_PP_oceanic",
            "PROTRA_PP_solar_CSP",
            "PROTRA_PP_solar_open_space_PV",
            "PROTRA_PP_solar_urban_PV",
            "PROTRA_PP_solid_fossil",
            "PROTRA_PP_solid_fossil_CCS",
            "PROTRA_PP_waste",
            "PROTRA_PP_waste_CCS",
            "PROTRA_PP_wind_offshore",
            "PROTRA_PP_wind_onshore",
        ],
    ] = True
    def_subs.loc[
        ["LROW"],
        ["TO_heat"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_HP_gas_fuels",
            "PROTRA_HP_solid_bio",
            "PROTRA_HP_geothermal",
            "PROTRA_HP_liquid_fuels",
            "PROTRA_HP_solar_DEACTIVATED",
            "PROTRA_HP_solid_fossil",
            "PROTRA_HP_waste",
        ],
    ] = True
    def_subs.loc[
        ["LROW"],
        ["TO_elec"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_PP_solid_bio",
            "PROTRA_PP_solid_bio_CCS",
            "PROTRA_PP_gas_fuels",
            "PROTRA_PP_gas_fuels_CCS",
            "PROTRA_PP_geothermal",
            "PROTRA_PP_hydropower_dammed",
            "PROTRA_PP_hydropower_run_of_river",
            "PROTRA_PP_liquid_fuels",
            "PROTRA_PP_liquid_fuels_CCS",
            "PROTRA_PP_nuclear",
            "PROTRA_PP_oceanic",
            "PROTRA_PP_solar_CSP",
            "PROTRA_PP_solar_open_space_PV",
            "PROTRA_PP_solar_urban_PV",
            "PROTRA_PP_solid_fossil",
            "PROTRA_PP_solid_fossil_CCS",
            "PROTRA_PP_waste",
            "PROTRA_PP_waste_CCS",
            "PROTRA_PP_wind_offshore",
            "PROTRA_PP_wind_onshore",
        ],
    ] = True
    def_subs.loc[
        ["LUXEMBOURG"],
        ["TO_heat"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_HP_gas_fuels",
            "PROTRA_HP_solid_bio",
            "PROTRA_HP_geothermal",
            "PROTRA_HP_liquid_fuels",
            "PROTRA_HP_solar_DEACTIVATED",
            "PROTRA_HP_solid_fossil",
            "PROTRA_HP_waste",
        ],
    ] = True
    def_subs.loc[
        ["LUXEMBOURG"],
        ["TO_elec"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_PP_solid_bio",
            "PROTRA_PP_solid_bio_CCS",
            "PROTRA_PP_gas_fuels",
            "PROTRA_PP_gas_fuels_CCS",
            "PROTRA_PP_geothermal",
            "PROTRA_PP_hydropower_dammed",
            "PROTRA_PP_hydropower_run_of_river",
            "PROTRA_PP_liquid_fuels",
            "PROTRA_PP_liquid_fuels_CCS",
            "PROTRA_PP_nuclear",
            "PROTRA_PP_oceanic",
            "PROTRA_PP_solar_CSP",
            "PROTRA_PP_solar_open_space_PV",
            "PROTRA_PP_solar_urban_PV",
            "PROTRA_PP_solid_fossil",
            "PROTRA_PP_solid_fossil_CCS",
            "PROTRA_PP_waste",
            "PROTRA_PP_waste_CCS",
            "PROTRA_PP_wind_offshore",
            "PROTRA_PP_wind_onshore",
        ],
    ] = True
    def_subs.loc[
        ["MALTA"],
        ["TO_heat"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_HP_gas_fuels",
            "PROTRA_HP_solid_bio",
            "PROTRA_HP_geothermal",
            "PROTRA_HP_liquid_fuels",
            "PROTRA_HP_solar_DEACTIVATED",
            "PROTRA_HP_solid_fossil",
            "PROTRA_HP_waste",
        ],
    ] = True
    def_subs.loc[
        ["MALTA"],
        ["TO_elec"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_PP_solid_bio",
            "PROTRA_PP_solid_bio_CCS",
            "PROTRA_PP_gas_fuels",
            "PROTRA_PP_gas_fuels_CCS",
            "PROTRA_PP_geothermal",
            "PROTRA_PP_hydropower_dammed",
            "PROTRA_PP_hydropower_run_of_river",
            "PROTRA_PP_liquid_fuels",
            "PROTRA_PP_liquid_fuels_CCS",
            "PROTRA_PP_nuclear",
            "PROTRA_PP_oceanic",
            "PROTRA_PP_solar_CSP",
            "PROTRA_PP_solar_open_space_PV",
            "PROTRA_PP_solar_urban_PV",
            "PROTRA_PP_solid_fossil",
            "PROTRA_PP_solid_fossil_CCS",
            "PROTRA_PP_waste",
            "PROTRA_PP_waste_CCS",
            "PROTRA_PP_wind_offshore",
            "PROTRA_PP_wind_onshore",
        ],
    ] = True
    def_subs.loc[
        ["NETHERLANDS"],
        ["TO_heat"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_HP_gas_fuels",
            "PROTRA_HP_solid_bio",
            "PROTRA_HP_geothermal",
            "PROTRA_HP_liquid_fuels",
            "PROTRA_HP_solar_DEACTIVATED",
            "PROTRA_HP_solid_fossil",
            "PROTRA_HP_waste",
        ],
    ] = True
    def_subs.loc[
        ["NETHERLANDS"],
        ["TO_elec"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_PP_solid_bio",
            "PROTRA_PP_solid_bio_CCS",
            "PROTRA_PP_gas_fuels",
            "PROTRA_PP_gas_fuels_CCS",
            "PROTRA_PP_geothermal",
            "PROTRA_PP_hydropower_dammed",
            "PROTRA_PP_hydropower_run_of_river",
            "PROTRA_PP_liquid_fuels",
            "PROTRA_PP_liquid_fuels_CCS",
            "PROTRA_PP_nuclear",
            "PROTRA_PP_oceanic",
            "PROTRA_PP_solar_CSP",
            "PROTRA_PP_solar_open_space_PV",
            "PROTRA_PP_solar_urban_PV",
            "PROTRA_PP_solid_fossil",
            "PROTRA_PP_solid_fossil_CCS",
            "PROTRA_PP_waste",
            "PROTRA_PP_waste_CCS",
            "PROTRA_PP_wind_offshore",
            "PROTRA_PP_wind_onshore",
        ],
    ] = True
    def_subs.loc[
        ["POLAND"],
        ["TO_heat"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_HP_gas_fuels",
            "PROTRA_HP_solid_bio",
            "PROTRA_HP_geothermal",
            "PROTRA_HP_liquid_fuels",
            "PROTRA_HP_solar_DEACTIVATED",
            "PROTRA_HP_solid_fossil",
            "PROTRA_HP_waste",
        ],
    ] = True
    def_subs.loc[
        ["POLAND"],
        ["TO_elec"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_PP_solid_bio",
            "PROTRA_PP_solid_bio_CCS",
            "PROTRA_PP_gas_fuels",
            "PROTRA_PP_gas_fuels_CCS",
            "PROTRA_PP_geothermal",
            "PROTRA_PP_hydropower_dammed",
            "PROTRA_PP_hydropower_run_of_river",
            "PROTRA_PP_liquid_fuels",
            "PROTRA_PP_liquid_fuels_CCS",
            "PROTRA_PP_nuclear",
            "PROTRA_PP_oceanic",
            "PROTRA_PP_solar_CSP",
            "PROTRA_PP_solar_open_space_PV",
            "PROTRA_PP_solar_urban_PV",
            "PROTRA_PP_solid_fossil",
            "PROTRA_PP_solid_fossil_CCS",
            "PROTRA_PP_waste",
            "PROTRA_PP_waste_CCS",
            "PROTRA_PP_wind_offshore",
            "PROTRA_PP_wind_onshore",
        ],
    ] = True
    def_subs.loc[
        ["PORTUGAL"],
        ["TO_heat"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_HP_gas_fuels",
            "PROTRA_HP_solid_bio",
            "PROTRA_HP_geothermal",
            "PROTRA_HP_liquid_fuels",
            "PROTRA_HP_solar_DEACTIVATED",
            "PROTRA_HP_solid_fossil",
            "PROTRA_HP_waste",
        ],
    ] = True
    def_subs.loc[
        ["PORTUGAL"],
        ["TO_elec"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_PP_solid_bio",
            "PROTRA_PP_solid_bio_CCS",
            "PROTRA_PP_gas_fuels",
            "PROTRA_PP_gas_fuels_CCS",
            "PROTRA_PP_geothermal",
            "PROTRA_PP_hydropower_dammed",
            "PROTRA_PP_hydropower_run_of_river",
            "PROTRA_PP_liquid_fuels",
            "PROTRA_PP_liquid_fuels_CCS",
            "PROTRA_PP_nuclear",
            "PROTRA_PP_oceanic",
            "PROTRA_PP_solar_CSP",
            "PROTRA_PP_solar_open_space_PV",
            "PROTRA_PP_solar_urban_PV",
            "PROTRA_PP_solid_fossil",
            "PROTRA_PP_solid_fossil_CCS",
            "PROTRA_PP_waste",
            "PROTRA_PP_waste_CCS",
            "PROTRA_PP_wind_offshore",
            "PROTRA_PP_wind_onshore",
        ],
    ] = True
    def_subs.loc[
        ["ROMANIA"],
        ["TO_heat"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_HP_gas_fuels",
            "PROTRA_HP_solid_bio",
            "PROTRA_HP_geothermal",
            "PROTRA_HP_liquid_fuels",
            "PROTRA_HP_solar_DEACTIVATED",
            "PROTRA_HP_solid_fossil",
            "PROTRA_HP_waste",
        ],
    ] = True
    def_subs.loc[
        ["ROMANIA"],
        ["TO_elec"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_PP_solid_bio",
            "PROTRA_PP_solid_bio_CCS",
            "PROTRA_PP_gas_fuels",
            "PROTRA_PP_gas_fuels_CCS",
            "PROTRA_PP_geothermal",
            "PROTRA_PP_hydropower_dammed",
            "PROTRA_PP_hydropower_run_of_river",
            "PROTRA_PP_liquid_fuels",
            "PROTRA_PP_liquid_fuels_CCS",
            "PROTRA_PP_nuclear",
            "PROTRA_PP_oceanic",
            "PROTRA_PP_solar_CSP",
            "PROTRA_PP_solar_open_space_PV",
            "PROTRA_PP_solar_urban_PV",
            "PROTRA_PP_solid_fossil",
            "PROTRA_PP_solid_fossil_CCS",
            "PROTRA_PP_waste",
            "PROTRA_PP_waste_CCS",
            "PROTRA_PP_wind_offshore",
            "PROTRA_PP_wind_onshore",
        ],
    ] = True
    def_subs.loc[
        ["RUSSIA"],
        ["TO_heat"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_HP_gas_fuels",
            "PROTRA_HP_solid_bio",
            "PROTRA_HP_geothermal",
            "PROTRA_HP_liquid_fuels",
            "PROTRA_HP_solar_DEACTIVATED",
            "PROTRA_HP_solid_fossil",
            "PROTRA_HP_waste",
        ],
    ] = True
    def_subs.loc[
        ["RUSSIA"],
        ["TO_elec"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_PP_solid_bio",
            "PROTRA_PP_solid_bio_CCS",
            "PROTRA_PP_gas_fuels",
            "PROTRA_PP_gas_fuels_CCS",
            "PROTRA_PP_geothermal",
            "PROTRA_PP_hydropower_dammed",
            "PROTRA_PP_hydropower_run_of_river",
            "PROTRA_PP_liquid_fuels",
            "PROTRA_PP_liquid_fuels_CCS",
            "PROTRA_PP_nuclear",
            "PROTRA_PP_oceanic",
            "PROTRA_PP_solar_CSP",
            "PROTRA_PP_solar_open_space_PV",
            "PROTRA_PP_solar_urban_PV",
            "PROTRA_PP_solid_fossil",
            "PROTRA_PP_solid_fossil_CCS",
            "PROTRA_PP_waste",
            "PROTRA_PP_waste_CCS",
            "PROTRA_PP_wind_offshore",
            "PROTRA_PP_wind_onshore",
        ],
    ] = True
    def_subs.loc[
        ["SLOVAKIA"],
        ["TO_heat"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_HP_gas_fuels",
            "PROTRA_HP_solid_bio",
            "PROTRA_HP_geothermal",
            "PROTRA_HP_liquid_fuels",
            "PROTRA_HP_solar_DEACTIVATED",
            "PROTRA_HP_solid_fossil",
            "PROTRA_HP_waste",
        ],
    ] = True
    def_subs.loc[
        ["SLOVAKIA"],
        ["TO_elec"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_PP_solid_bio",
            "PROTRA_PP_solid_bio_CCS",
            "PROTRA_PP_gas_fuels",
            "PROTRA_PP_gas_fuels_CCS",
            "PROTRA_PP_geothermal",
            "PROTRA_PP_hydropower_dammed",
            "PROTRA_PP_hydropower_run_of_river",
            "PROTRA_PP_liquid_fuels",
            "PROTRA_PP_liquid_fuels_CCS",
            "PROTRA_PP_nuclear",
            "PROTRA_PP_oceanic",
            "PROTRA_PP_solar_CSP",
            "PROTRA_PP_solar_open_space_PV",
            "PROTRA_PP_solar_urban_PV",
            "PROTRA_PP_solid_fossil",
            "PROTRA_PP_solid_fossil_CCS",
            "PROTRA_PP_waste",
            "PROTRA_PP_waste_CCS",
            "PROTRA_PP_wind_offshore",
            "PROTRA_PP_wind_onshore",
        ],
    ] = True
    def_subs.loc[
        ["SLOVENIA"],
        ["TO_heat"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_HP_gas_fuels",
            "PROTRA_HP_solid_bio",
            "PROTRA_HP_geothermal",
            "PROTRA_HP_liquid_fuels",
            "PROTRA_HP_solar_DEACTIVATED",
            "PROTRA_HP_solid_fossil",
            "PROTRA_HP_waste",
        ],
    ] = True
    def_subs.loc[
        ["SLOVENIA"],
        ["TO_elec"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_PP_solid_bio",
            "PROTRA_PP_solid_bio_CCS",
            "PROTRA_PP_gas_fuels",
            "PROTRA_PP_gas_fuels_CCS",
            "PROTRA_PP_geothermal",
            "PROTRA_PP_hydropower_dammed",
            "PROTRA_PP_hydropower_run_of_river",
            "PROTRA_PP_liquid_fuels",
            "PROTRA_PP_liquid_fuels_CCS",
            "PROTRA_PP_nuclear",
            "PROTRA_PP_oceanic",
            "PROTRA_PP_solar_CSP",
            "PROTRA_PP_solar_open_space_PV",
            "PROTRA_PP_solar_urban_PV",
            "PROTRA_PP_solid_fossil",
            "PROTRA_PP_solid_fossil_CCS",
            "PROTRA_PP_waste",
            "PROTRA_PP_waste_CCS",
            "PROTRA_PP_wind_offshore",
            "PROTRA_PP_wind_onshore",
        ],
    ] = True
    def_subs.loc[
        ["SPAIN"],
        ["TO_heat"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_HP_gas_fuels",
            "PROTRA_HP_solid_bio",
            "PROTRA_HP_geothermal",
            "PROTRA_HP_liquid_fuels",
            "PROTRA_HP_solar_DEACTIVATED",
            "PROTRA_HP_solid_fossil",
            "PROTRA_HP_waste",
        ],
    ] = True
    def_subs.loc[
        ["SPAIN"],
        ["TO_elec"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_PP_solid_bio",
            "PROTRA_PP_solid_bio_CCS",
            "PROTRA_PP_gas_fuels",
            "PROTRA_PP_gas_fuels_CCS",
            "PROTRA_PP_geothermal",
            "PROTRA_PP_hydropower_dammed",
            "PROTRA_PP_hydropower_run_of_river",
            "PROTRA_PP_liquid_fuels",
            "PROTRA_PP_liquid_fuels_CCS",
            "PROTRA_PP_nuclear",
            "PROTRA_PP_oceanic",
            "PROTRA_PP_solar_CSP",
            "PROTRA_PP_solar_open_space_PV",
            "PROTRA_PP_solar_urban_PV",
            "PROTRA_PP_solid_fossil",
            "PROTRA_PP_solid_fossil_CCS",
            "PROTRA_PP_waste",
            "PROTRA_PP_waste_CCS",
            "PROTRA_PP_wind_offshore",
            "PROTRA_PP_wind_onshore",
        ],
    ] = True
    def_subs.loc[
        ["SWEDEN"],
        ["TO_heat"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_HP_gas_fuels",
            "PROTRA_HP_solid_bio",
            "PROTRA_HP_geothermal",
            "PROTRA_HP_liquid_fuels",
            "PROTRA_HP_solar_DEACTIVATED",
            "PROTRA_HP_solid_fossil",
            "PROTRA_HP_waste",
        ],
    ] = True
    def_subs.loc[
        ["SWEDEN"],
        ["TO_elec"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_PP_solid_bio",
            "PROTRA_PP_solid_bio_CCS",
            "PROTRA_PP_gas_fuels",
            "PROTRA_PP_gas_fuels_CCS",
            "PROTRA_PP_geothermal",
            "PROTRA_PP_hydropower_dammed",
            "PROTRA_PP_hydropower_run_of_river",
            "PROTRA_PP_liquid_fuels",
            "PROTRA_PP_liquid_fuels_CCS",
            "PROTRA_PP_nuclear",
            "PROTRA_PP_oceanic",
            "PROTRA_PP_solar_CSP",
            "PROTRA_PP_solar_open_space_PV",
            "PROTRA_PP_solar_urban_PV",
            "PROTRA_PP_solid_fossil",
            "PROTRA_PP_solid_fossil_CCS",
            "PROTRA_PP_waste",
            "PROTRA_PP_waste_CCS",
            "PROTRA_PP_wind_offshore",
            "PROTRA_PP_wind_onshore",
        ],
    ] = True
    def_subs.loc[
        ["UK"],
        ["TO_heat"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_HP_gas_fuels",
            "PROTRA_HP_solid_bio",
            "PROTRA_HP_geothermal",
            "PROTRA_HP_liquid_fuels",
            "PROTRA_HP_solar_DEACTIVATED",
            "PROTRA_HP_solid_fossil",
            "PROTRA_HP_waste",
        ],
    ] = True
    def_subs.loc[
        ["UK"],
        ["TO_elec"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_PP_solid_bio",
            "PROTRA_PP_solid_bio_CCS",
            "PROTRA_PP_gas_fuels",
            "PROTRA_PP_gas_fuels_CCS",
            "PROTRA_PP_geothermal",
            "PROTRA_PP_hydropower_dammed",
            "PROTRA_PP_hydropower_run_of_river",
            "PROTRA_PP_liquid_fuels",
            "PROTRA_PP_liquid_fuels_CCS",
            "PROTRA_PP_nuclear",
            "PROTRA_PP_oceanic",
            "PROTRA_PP_solar_CSP",
            "PROTRA_PP_solar_open_space_PV",
            "PROTRA_PP_solar_urban_PV",
            "PROTRA_PP_solid_fossil",
            "PROTRA_PP_solid_fossil_CCS",
            "PROTRA_PP_waste",
            "PROTRA_PP_waste_CCS",
            "PROTRA_PP_wind_offshore",
            "PROTRA_PP_wind_onshore",
        ],
    ] = True
    def_subs.loc[
        ["USMCA"],
        ["TO_heat"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_HP_gas_fuels",
            "PROTRA_HP_solid_bio",
            "PROTRA_HP_geothermal",
            "PROTRA_HP_liquid_fuels",
            "PROTRA_HP_solar_DEACTIVATED",
            "PROTRA_HP_solid_fossil",
            "PROTRA_HP_waste",
        ],
    ] = True
    def_subs.loc[
        ["USMCA"],
        ["TO_elec"],
        [
            "PROTRA_CHP_gas_fuels",
            "PROTRA_CHP_gas_fuels_CCS",
            "PROTRA_CHP_geothermal_DEACTIVATED",
            "PROTRA_CHP_liquid_fuels",
            "PROTRA_CHP_liquid_fuels_CCS",
            "PROTRA_CHP_solid_fossil",
            "PROTRA_CHP_solid_fossil_CCS",
            "PROTRA_CHP_waste",
            "PROTRA_CHP_solid_bio",
            "PROTRA_CHP_solid_bio_CCS",
            "PROTRA_PP_solid_bio",
            "PROTRA_PP_solid_bio_CCS",
            "PROTRA_PP_gas_fuels",
            "PROTRA_PP_gas_fuels_CCS",
            "PROTRA_PP_geothermal",
            "PROTRA_PP_hydropower_dammed",
            "PROTRA_PP_hydropower_run_of_river",
            "PROTRA_PP_liquid_fuels",
            "PROTRA_PP_liquid_fuels_CCS",
            "PROTRA_PP_nuclear",
            "PROTRA_PP_oceanic",
            "PROTRA_PP_solar_CSP",
            "PROTRA_PP_solar_open_space_PV",
            "PROTRA_PP_solar_urban_PV",
            "PROTRA_PP_solid_fossil",
            "PROTRA_PP_solid_fossil_CCS",
            "PROTRA_PP_waste",
            "PROTRA_PP_waste_CCS",
            "PROTRA_PP_wind_offshore",
            "PROTRA_PP_wind_onshore",
        ],
    ] = True
    value.values[def_subs.values] = _ext_data_protra_capacity_empirical(time()).values[
        def_subs.values
    ]
    value.loc[:, ["TO_gas"], ["PROTRA_blending_gas_fuels"]] = 10000
    value.loc[:, ["TO_liquid"], ["PROTRA_blending_liquid_fuels"]] = 10000
    value.loc[:, ["TO_hydrogen"], ["PROTRA_no_process_TI_hydrogen"]] = 10000
    value.loc[:, ["TO_solid_bio"], ["PROTRA_no_process_TI_solid_bio"]] = 10000
    value.loc[:, ["TO_solid_fossil"], ["PROTRA_no_process_TI_solid_fossil"]] = 10000
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[:, :, _subscript_dict["PROTRA_HP_I"]] = True
    except_subs.loc[:, ["TO_heat"], _subscript_dict["PROTRA_HP_I"]] = False
    value.values[except_subs.values] = 0
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[:, :, _subscript_dict["PROTRA_CHP_I"]] = True
    except_subs.loc[:, ["TO_elec"], _subscript_dict["PROTRA_CHP_I"]] = False
    except_subs.loc[:, ["TO_heat"], _subscript_dict["PROTRA_CHP_I"]] = False
    value.values[except_subs.values] = 0
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[:, :, _subscript_dict["PROTRA_NP_I"]] = True
    except_subs.loc[:, ["TO_hydrogen"], ["PROTRA_no_process_TI_hydrogen"]] = False
    except_subs.loc[:, ["TO_solid_bio"], ["PROTRA_no_process_TI_solid_bio"]] = False
    except_subs.loc[
        :, ["TO_solid_fossil"], ["PROTRA_no_process_TI_solid_fossil"]
    ] = False
    except_subs.loc[:, ["TO_gas"], ["PROTRA_blending_gas_fuels"]] = False
    except_subs.loc[:, ["TO_liquid"], ["PROTRA_blending_liquid_fuels"]] = False
    value.values[except_subs.values] = 0
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[:, :, _subscript_dict["PROTRA_PP_I"]] = True
    except_subs.loc[:, ["TO_elec"], _subscript_dict["PROTRA_PP_I"]] = False
    value.values[except_subs.values] = 0
    return value


_ext_data_protra_capacity_empirical = ExtData(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "AUSTRIA_TO_heat",
    None,
    {
        "REGIONS_36_I": ["AUSTRIA"],
        "NRG_TO_I": ["TO_heat"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_HP_I"],
    },
    _root,
    {
        "REGIONS_36_I": _subscript_dict["REGIONS_36_I"],
        "NRG_TO_I": _subscript_dict["NRG_TO_I"],
        "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
    },
    "_ext_data_protra_capacity_empirical",
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "AUSTRIA_TO_elec",
    None,
    {
        "REGIONS_36_I": ["AUSTRIA"],
        "NRG_TO_I": ["TO_elec"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_PP_I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "BELGIUM_TO_heat",
    None,
    {
        "REGIONS_36_I": ["BELGIUM"],
        "NRG_TO_I": ["TO_heat"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_HP_I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "BELGIUM_TO_elec",
    None,
    {
        "REGIONS_36_I": ["BELGIUM"],
        "NRG_TO_I": ["TO_elec"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_PP_I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "BULGARIA_TO_heat",
    None,
    {
        "REGIONS_36_I": ["BULGARIA"],
        "NRG_TO_I": ["TO_heat"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_HP_I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "BULGARIA_TO_elec",
    None,
    {
        "REGIONS_36_I": ["BULGARIA"],
        "NRG_TO_I": ["TO_elec"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_PP_I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "CHINA_TO_heat",
    None,
    {
        "REGIONS_36_I": ["CHINA"],
        "NRG_TO_I": ["TO_heat"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_HP_I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "CHINA_TO_elec",
    None,
    {
        "REGIONS_36_I": ["CHINA"],
        "NRG_TO_I": ["TO_elec"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_PP_I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "CROATIA_TO_heat",
    None,
    {
        "REGIONS_36_I": ["CROATIA"],
        "NRG_TO_I": ["TO_heat"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_HP_I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "CROATIA_TO_elec",
    None,
    {
        "REGIONS_36_I": ["CROATIA"],
        "NRG_TO_I": ["TO_elec"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_PP_I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "CYPRUS_TO_heat",
    None,
    {
        "REGIONS_36_I": ["CYPRUS"],
        "NRG_TO_I": ["TO_heat"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_HP_I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "CYPRUS_TO_elec",
    None,
    {
        "REGIONS_36_I": ["CYPRUS"],
        "NRG_TO_I": ["TO_elec"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_PP_I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "CZECH_REPUBLIC_TO_heat",
    None,
    {
        "REGIONS_36_I": ["CZECH_REPUBLIC"],
        "NRG_TO_I": ["TO_heat"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_HP_I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "CZECH_REPUBLIC_TO_elec",
    None,
    {
        "REGIONS_36_I": ["CZECH_REPUBLIC"],
        "NRG_TO_I": ["TO_elec"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_PP_I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "DENMARK_TO_heat",
    None,
    {
        "REGIONS_36_I": ["DENMARK"],
        "NRG_TO_I": ["TO_heat"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_HP_I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "DENMARK_TO_elec",
    None,
    {
        "REGIONS_36_I": ["DENMARK"],
        "NRG_TO_I": ["TO_elec"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_PP_I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "EASOC_TO_heat",
    None,
    {
        "REGIONS_36_I": ["EASOC"],
        "NRG_TO_I": ["TO_heat"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_HP_I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "EASOC_TO_elec",
    None,
    {
        "REGIONS_36_I": ["EASOC"],
        "NRG_TO_I": ["TO_elec"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_PP_I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "ESTONIA_TO_heat",
    None,
    {
        "REGIONS_36_I": ["ESTONIA"],
        "NRG_TO_I": ["TO_heat"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_HP_I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "ESTONIA_TO_elec",
    None,
    {
        "REGIONS_36_I": ["ESTONIA"],
        "NRG_TO_I": ["TO_elec"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_PP_I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "EU27_TO_heat",
    None,
    {
        "REGIONS_36_I": ["EU27"],
        "NRG_TO_I": ["TO_heat"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_HP_I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "EU27_TO_elec",
    None,
    {
        "REGIONS_36_I": ["EU27"],
        "NRG_TO_I": ["TO_elec"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_PP_I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "FINLAND_TO_heat",
    None,
    {
        "REGIONS_36_I": ["FINLAND"],
        "NRG_TO_I": ["TO_heat"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_HP_I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "FINLAND_TO_elec",
    None,
    {
        "REGIONS_36_I": ["FINLAND"],
        "NRG_TO_I": ["TO_elec"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_PP_I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "FRANCE_TO_heat",
    None,
    {
        "REGIONS_36_I": ["FRANCE"],
        "NRG_TO_I": ["TO_heat"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_HP_I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "FRANCE_TO_elec",
    None,
    {
        "REGIONS_36_I": ["FRANCE"],
        "NRG_TO_I": ["TO_elec"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_PP_I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "GERMANY_TO_heat",
    None,
    {
        "REGIONS_36_I": ["GERMANY"],
        "NRG_TO_I": ["TO_heat"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_HP_I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "GERMANY_TO_elec",
    None,
    {
        "REGIONS_36_I": ["GERMANY"],
        "NRG_TO_I": ["TO_elec"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_PP_I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "GREECE_TO_heat",
    None,
    {
        "REGIONS_36_I": ["GREECE"],
        "NRG_TO_I": ["TO_heat"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_HP_I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "GREECE_TO_elec",
    None,
    {
        "REGIONS_36_I": ["GREECE"],
        "NRG_TO_I": ["TO_elec"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_PP_I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "HUNGARY_TO_heat",
    None,
    {
        "REGIONS_36_I": ["HUNGARY"],
        "NRG_TO_I": ["TO_heat"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_HP_I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "HUNGARY_TO_elec",
    None,
    {
        "REGIONS_36_I": ["HUNGARY"],
        "NRG_TO_I": ["TO_elec"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_PP_I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "INDIA_TO_heat",
    None,
    {
        "REGIONS_36_I": ["INDIA"],
        "NRG_TO_I": ["TO_heat"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_HP_I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "INDIA_TO_elec",
    None,
    {
        "REGIONS_36_I": ["INDIA"],
        "NRG_TO_I": ["TO_elec"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_PP_I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "IRELAND_TO_heat",
    None,
    {
        "REGIONS_36_I": ["IRELAND"],
        "NRG_TO_I": ["TO_heat"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_HP_I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "IRELAND_TO_elec",
    None,
    {
        "REGIONS_36_I": ["IRELAND"],
        "NRG_TO_I": ["TO_elec"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_PP_I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "ITALY_TO_heat",
    None,
    {
        "REGIONS_36_I": ["ITALY"],
        "NRG_TO_I": ["TO_heat"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_HP_I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "ITALY_TO_elec",
    None,
    {
        "REGIONS_36_I": ["ITALY"],
        "NRG_TO_I": ["TO_elec"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_PP_I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "LATAM_TO_heat",
    None,
    {
        "REGIONS_36_I": ["LATAM"],
        "NRG_TO_I": ["TO_heat"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_HP_I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "LATAM_TO_elec",
    None,
    {
        "REGIONS_36_I": ["LATAM"],
        "NRG_TO_I": ["TO_elec"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_PP_I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "LATVIA_TO_heat",
    None,
    {
        "REGIONS_36_I": ["LATVIA"],
        "NRG_TO_I": ["TO_heat"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_HP_I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "LATVIA_TO_elec",
    None,
    {
        "REGIONS_36_I": ["LATVIA"],
        "NRG_TO_I": ["TO_elec"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_PP_I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "LITHUANIA_TO_heat",
    None,
    {
        "REGIONS_36_I": ["LITHUANIA"],
        "NRG_TO_I": ["TO_heat"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_HP_I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "LITHUANIA_TO_elec",
    None,
    {
        "REGIONS_36_I": ["LITHUANIA"],
        "NRG_TO_I": ["TO_elec"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_PP_I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "LROW_TO_heat",
    None,
    {
        "REGIONS_36_I": ["LROW"],
        "NRG_TO_I": ["TO_heat"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_HP_I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "LROW_TO_elec",
    None,
    {
        "REGIONS_36_I": ["LROW"],
        "NRG_TO_I": ["TO_elec"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_PP_I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "LUXEMBOURG_TO_heat",
    None,
    {
        "REGIONS_36_I": ["LUXEMBOURG"],
        "NRG_TO_I": ["TO_heat"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_HP_I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "LUXEMBOURG_TO_elec",
    None,
    {
        "REGIONS_36_I": ["LUXEMBOURG"],
        "NRG_TO_I": ["TO_elec"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_PP_I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "MALTA_TO_heat",
    None,
    {
        "REGIONS_36_I": ["MALTA"],
        "NRG_TO_I": ["TO_heat"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_HP_I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "MALTA_TO_elec",
    None,
    {
        "REGIONS_36_I": ["MALTA"],
        "NRG_TO_I": ["TO_elec"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_PP_I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "NETHERLANDS_TO_heat",
    None,
    {
        "REGIONS_36_I": ["NETHERLANDS"],
        "NRG_TO_I": ["TO_heat"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_HP_I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "NETHERLANDS_TO_elec",
    None,
    {
        "REGIONS_36_I": ["NETHERLANDS"],
        "NRG_TO_I": ["TO_elec"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_PP_I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "POLAND_TO_heat",
    None,
    {
        "REGIONS_36_I": ["POLAND"],
        "NRG_TO_I": ["TO_heat"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_HP_I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "POLAND_TO_elec",
    None,
    {
        "REGIONS_36_I": ["POLAND"],
        "NRG_TO_I": ["TO_elec"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_PP_I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "PORTUGAL_TO_heat",
    None,
    {
        "REGIONS_36_I": ["PORTUGAL"],
        "NRG_TO_I": ["TO_heat"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_HP_I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "PORTUGAL_TO_elec",
    None,
    {
        "REGIONS_36_I": ["PORTUGAL"],
        "NRG_TO_I": ["TO_elec"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_PP_I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "ROMANIA_TO_heat",
    None,
    {
        "REGIONS_36_I": ["ROMANIA"],
        "NRG_TO_I": ["TO_heat"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_HP_I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "ROMANIA_TO_elec",
    None,
    {
        "REGIONS_36_I": ["ROMANIA"],
        "NRG_TO_I": ["TO_elec"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_PP_I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "RUSSIA_TO_heat",
    None,
    {
        "REGIONS_36_I": ["RUSSIA"],
        "NRG_TO_I": ["TO_heat"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_HP_I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "RUSSIA_TO_elec",
    None,
    {
        "REGIONS_36_I": ["RUSSIA"],
        "NRG_TO_I": ["TO_elec"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_PP_I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "SLOVAKIA_TO_heat",
    None,
    {
        "REGIONS_36_I": ["SLOVAKIA"],
        "NRG_TO_I": ["TO_heat"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_HP_I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "SLOVAKIA_TO_elec",
    None,
    {
        "REGIONS_36_I": ["SLOVAKIA"],
        "NRG_TO_I": ["TO_elec"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_PP_I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "SLOVENIA_TO_heat",
    None,
    {
        "REGIONS_36_I": ["SLOVENIA"],
        "NRG_TO_I": ["TO_heat"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_HP_I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "SLOVENIA_TO_elec",
    None,
    {
        "REGIONS_36_I": ["SLOVENIA"],
        "NRG_TO_I": ["TO_elec"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_PP_I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "SPAIN_TO_heat",
    None,
    {
        "REGIONS_36_I": ["SPAIN"],
        "NRG_TO_I": ["TO_heat"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_HP_I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "SPAIN_TO_elec",
    None,
    {
        "REGIONS_36_I": ["SPAIN"],
        "NRG_TO_I": ["TO_elec"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_PP_I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "SWEDEN_TO_heat",
    None,
    {
        "REGIONS_36_I": ["SWEDEN"],
        "NRG_TO_I": ["TO_heat"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_HP_I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "SWEDEN_TO_elec",
    None,
    {
        "REGIONS_36_I": ["SWEDEN"],
        "NRG_TO_I": ["TO_elec"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_PP_I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "UK_TO_heat",
    None,
    {
        "REGIONS_36_I": ["UK"],
        "NRG_TO_I": ["TO_heat"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_HP_I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "UK_TO_elec",
    None,
    {
        "REGIONS_36_I": ["UK"],
        "NRG_TO_I": ["TO_elec"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_PP_I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "USMCA_TO_heat",
    None,
    {
        "REGIONS_36_I": ["USMCA"],
        "NRG_TO_I": ["TO_heat"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_HP_I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "USMCA_TO_elec",
    None,
    {
        "REGIONS_36_I": ["USMCA"],
        "NRG_TO_I": ["TO_elec"],
        "NRG_PROTRA_I": _subscript_dict["PROTRA_CHP_PP_I"],
    },
)


@component.add(
    name="PROTRA_CAPACITY_EMPIRICAL_IN_TW",
    units="TW",
    subscripts=["REGIONS_36_I", "NRG_TO_I", "NRG_PROTRA_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"protra_capacity_empirical": 1, "unit_conversion_gw_tw": 1},
)
def protra_capacity_empirical_in_tw():
    """
    empirical capacities in TW
    """
    return protra_capacity_empirical() / unit_conversion_gw_tw()


@component.add(
    name="PROTRA_capacity_expansion",
    units="TW/Year",
    subscripts=["REGIONS_9_I", "NRG_TO_I", "NRG_PROTRA_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 2,
        "protra_capacity_variation_empirical": 3,
        "protra_max_full_load_hours_after_constraints": 1,
        "protra_shortfall_allocation": 1,
        "unit_conversion_tw_per_ej_per_year": 1,
        "one_year": 1,
    },
)
def protra_capacity_expansion():
    """
    New transformation capacity added to the energy transformation system
    """
    return (
        if_then_else(
            np.logical_and(
                time() < 2020,
                protra_capacity_variation_empirical()
                .loc[_subscript_dict["REGIONS_9_I"], :, :]
                .rename({"REGIONS_36_I": "REGIONS_9_I"})
                > 0,
            ),
            lambda: protra_capacity_variation_empirical()
            .loc[_subscript_dict["REGIONS_9_I"], :, :]
            .rename({"REGIONS_36_I": "REGIONS_9_I"}),
            lambda: if_then_else(
                np.logical_and(
                    time() < 2020,
                    protra_capacity_variation_empirical()
                    .loc[_subscript_dict["REGIONS_9_I"], :, :]
                    .rename({"REGIONS_36_I": "REGIONS_9_I"})
                    <= 0,
                ),
                lambda: xr.DataArray(
                    0,
                    {
                        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                        "NRG_TO_I": _subscript_dict["NRG_TO_I"],
                        "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
                    },
                    ["REGIONS_9_I", "NRG_TO_I", "NRG_PROTRA_I"],
                ),
                lambda: zidz(
                    protra_shortfall_allocation(),
                    protra_max_full_load_hours_after_constraints().expand_dims(
                        {"NRG_TO_I": _subscript_dict["NRG_TO_I"]}, 1
                    ),
                )
                / unit_conversion_tw_per_ej_per_year(),
            ),
        )
        / one_year()
    )


@component.add(
    name="PROTRA_capacity_expansion_35R",
    units="TW/Year",
    subscripts=["REGIONS_35_I", "NRG_TO_I", "NRG_PROTRA_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"protra_capacity_expansion": 1, "protra_capacity_expansion_eu27": 1},
)
def protra_capacity_expansion_35r():
    """
    Capacity expansion of the PROTRA for the 35 regions downscaling the information from EU27 aggregated to the 27 EU countries taking as reference the empirical variation of capacity stock for each country.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "NRG_TO_I": _subscript_dict["NRG_TO_I"],
            "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
        },
        ["REGIONS_35_I", "NRG_TO_I", "NRG_PROTRA_I"],
    )
    value.loc[_subscript_dict["REGIONS_8_I"], :, :] = (
        protra_capacity_expansion()
        .loc[_subscript_dict["REGIONS_8_I"], :, :]
        .rename({"REGIONS_9_I": "REGIONS_8_I"})
        .values
    )
    value.loc[
        _subscript_dict["REGIONS_EU27_I"], :, :
    ] = protra_capacity_expansion_eu27().values
    return value


@component.add(
    name="PROTRA_capacity_expansion_EU27",
    units="TW/Year",
    subscripts=["REGIONS_EU27_I", "NRG_TO_I", "NRG_PROTRA_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "protra_capacity_variation_empirical": 1,
        "protra_capacity_expansion": 1,
        "share_protra_capacity_stock_eu27": 1,
    },
)
def protra_capacity_expansion_eu27():
    """
    Until 2020 historic data and thereafter downscaling of the capacity expansion for the 27 EU countries taking as reference the capacity stock of each country. The MAX function takes only those empirical positive values which mean new capacity.
    """
    return if_then_else(
        time() <= 2020,
        lambda: np.maximum(
            0,
            protra_capacity_variation_empirical()
            .loc[_subscript_dict["REGIONS_EU27_I"], :, :]
            .rename({"REGIONS_36_I": "REGIONS_EU27_I"}),
        ),
        lambda: (
            protra_capacity_expansion().loc["EU27", :, :].reset_coords(drop=True)
            * share_protra_capacity_stock_eu27().transpose(
                "NRG_TO_I", "NRG_PROTRA_I", "REGIONS_EU27_I"
            )
        ).transpose("REGIONS_EU27_I", "NRG_TO_I", "NRG_PROTRA_I"),
    )


@component.add(
    name="PROTRA_CAPACITY_EXPANSION_POLICY_WEIGHT_SP",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_protra_capacity_expansion_policy_weight_sp"
    },
)
def protra_capacity_expansion_policy_weight_sp():
    """
    capacity expansion policy weight: 0=only endogenous LCOE signal, 1 = only exogenous signal
    """
    return _ext_constant_protra_capacity_expansion_policy_weight_sp()


_ext_constant_protra_capacity_expansion_policy_weight_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "PROTRA_CAPACITY_EXPANSION_POLICY_WEIGHT_SP",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_protra_capacity_expansion_policy_weight_sp",
)


@component.add(
    name="PROTRA_CAPACITY_EXPANSION_PRIORITIES_VECTOR_SP",
    units="DMNL",
    subscripts=["REGIONS_9_I", "NRG_PROTRA_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_protra_capacity_expansion_priorities_vector_sp"
    },
)
def protra_capacity_expansion_priorities_vector_sp():
    """
    scenario parameter for policy parameters
    """
    return _ext_constant_protra_capacity_expansion_priorities_vector_sp()


_ext_constant_protra_capacity_expansion_priorities_vector_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "CAPACITY_EXPANSION_POLICY_PRIORITIES_SP*",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
    },
    "_ext_constant_protra_capacity_expansion_priorities_vector_sp",
)


@component.add(
    name="PROTRA_capacity_stock",
    units="TW",
    subscripts=["REGIONS_9_I", "NRG_TO_I", "NRG_PROTRA_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_protra_capacity_stock": 1},
    other_deps={
        "_integ_protra_capacity_stock": {
            "initial": {"initial_protra_capacity_stock": 1},
            "step": {
                "protra_capacity_expansion": 1,
                "protra_capacity_decommissioning": 1,
            },
        }
    },
)
def protra_capacity_stock():
    """
    Capacity stock of TI-TO transformation technology capacities by TO (PROTRA)
    """
    return _integ_protra_capacity_stock()


_integ_protra_capacity_stock = Integ(
    lambda: protra_capacity_expansion() - protra_capacity_decommissioning(),
    lambda: initial_protra_capacity_stock()
    .loc[_subscript_dict["REGIONS_9_I"], :, :]
    .rename({"REGIONS_36_I": "REGIONS_9_I"}),
    "_integ_protra_capacity_stock",
)


@component.add(
    name="PROTRA_capacity_stock_35R",
    units="TW/Year",
    subscripts=["REGIONS_35_I", "NRG_TO_I", "NRG_PROTRA_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"protra_capacity_stock": 1, "protra_capacity_stock_eu27": 1},
)
def protra_capacity_stock_35r():
    """
    Capacity stock of the PROTRA for the 35 regions downscaling the information from EU27 aggregated to the 27 EU countries taking as reference the empirical variation of capacity stock for each country.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "NRG_TO_I": _subscript_dict["NRG_TO_I"],
            "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
        },
        ["REGIONS_35_I", "NRG_TO_I", "NRG_PROTRA_I"],
    )
    value.loc[_subscript_dict["REGIONS_8_I"], :, :] = (
        protra_capacity_stock()
        .loc[_subscript_dict["REGIONS_8_I"], :, :]
        .rename({"REGIONS_9_I": "REGIONS_8_I"})
        .values
    )
    value.loc[
        _subscript_dict["REGIONS_EU27_I"], :, :
    ] = protra_capacity_stock_eu27().values
    return value


@component.add(
    name="PROTRA_capacity_stock_EU27",
    units="TW",
    subscripts=["REGIONS_EU27_I", "NRG_TO_I", "NRG_PROTRA_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_protra_capacity_stock_eu27": 1},
    other_deps={
        "_integ_protra_capacity_stock_eu27": {
            "initial": {"protra_capacity_empirical_in_tw": 1},
            "step": {
                "protra_capacity_expansion_eu27": 1,
                "protra_capacity_decommissioning_eu27": 1,
            },
        }
    },
)
def protra_capacity_stock_eu27():
    """
    PROTRA capacity stock for the 27 EU countries downscaling the information from the aggregated EU27.
    """
    return _integ_protra_capacity_stock_eu27()


_integ_protra_capacity_stock_eu27 = Integ(
    lambda: protra_capacity_expansion_eu27() - protra_capacity_decommissioning_eu27(),
    lambda: protra_capacity_empirical_in_tw()
    .loc[_subscript_dict["REGIONS_EU27_I"], :, :]
    .rename({"REGIONS_36_I": "REGIONS_EU27_I"}),
    "_integ_protra_capacity_stock_eu27",
)


@component.add(
    name="PROTRA_CAPACITY_VARIATION_EMPIRICAL",
    units="TW",
    subscripts=["REGIONS_36_I", "NRG_TO_I", "NRG_PROTRA_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_capacity_empirical_in_tw": 1,
        "delayed_protra_capacity_empirical": 1,
    },
)
def protra_capacity_variation_empirical():
    """
    net capacity addition (positiv) or reduction (negativ) calculated from empirical values
    """
    return protra_capacity_empirical_in_tw() - delayed_protra_capacity_empirical()


@component.add(
    name="PROTRA_CHP_and_HP_expansion_request",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_COMMODITIES_I", "NRG_PRO_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_heat_expansion_request_with_res_potentials": 2,
        "select_availability_unmature_energy_technologies_sp": 2,
    },
)
def protra_chp_and_hp_expansion_request():
    """
    Request of heat to be generated by each PROTRA CHP and HP. Priority is given to heat allocation. We assign the same amount for all technologies (if they are not affected by a potential) in order to avoid biases. We take the TO_shortfall of heat as reference. TESTING: [REGIONS_9_I,TO_heat,PROTRA_CHP_HP_I] -> max_TO_from_existing_stock_by_PROTRA_delayed[REGIONS_9_I,TO_heat,PROTRA_CHP _HP_I]
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "NRG_COMMODITIES_I": _subscript_dict["NRG_COMMODITIES_I"],
            "NRG_PRO_I": _subscript_dict["NRG_PRO_I"],
        },
        ["REGIONS_9_I", "NRG_COMMODITIES_I", "NRG_PRO_I"],
    )
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[:, ["TO_heat"], :] = True
    except_subs.loc[:, ["TO_heat"], _subscript_dict["PROTRA_CHP_HP_I"]] = False
    value.values[except_subs.values] = 0
    value.loc[:, ["TO_heat"], _subscript_dict["PROTRA_CHP_HP_NON_CCS_I"]] = (
        protra_heat_expansion_request_with_res_potentials()
        .loc[:, "TO_heat", _subscript_dict["PROTRA_CHP_HP_NON_CCS_I"]]
        .reset_coords(drop=True)
        .rename({"PROTRA_CHP_HP_I": "PROTRA_CHP_HP_NON_CCS_I"})
        .expand_dims({"NRG_COMMODITIES_I": ["TO_heat"]}, 1)
        .values
    )
    value.loc[:, ["TO_heat"], _subscript_dict["PROTRA_CHP_HP_CCS_I"]] = (
        if_then_else(
            np.logical_or(
                select_availability_unmature_energy_technologies_sp() == 1,
                select_availability_unmature_energy_technologies_sp() == 4,
            ),
            lambda: protra_heat_expansion_request_with_res_potentials()
            .loc[:, "TO_heat", _subscript_dict["PROTRA_CHP_HP_CCS_I"]]
            .reset_coords(drop=True)
            .rename({"PROTRA_CHP_HP_I": "PROTRA_CHP_HP_CCS_I"}),
            lambda: xr.DataArray(
                0,
                {
                    "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                    "PROTRA_CHP_HP_CCS_I": _subscript_dict["PROTRA_CHP_HP_CCS_I"],
                },
                ["REGIONS_9_I", "PROTRA_CHP_HP_CCS_I"],
            ),
        )
        .expand_dims({"NRG_COMMODITIES_I": ["TO_heat"]}, 1)
        .values
    )
    return value


@component.add(
    name="PROTRA_elec_expansion_request",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_COMMODITIES_I", "NRG_PRO_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_elec_expansion_request_with_limits": 2,
        "select_availability_unmature_energy_technologies_sp": 2,
    },
)
def protra_elec_expansion_request():
    """
    Request of electricity to be generated by each PROTRA PP (after substracting the electricity generation from CHP, since priority is first given to heat allocation). We assign the same amount for all technologies (if they are not affected by a potential) in order to avoid biases. We take the TO_shortfall of electricity as reference.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "NRG_COMMODITIES_I": _subscript_dict["NRG_COMMODITIES_I"],
            "NRG_PRO_I": _subscript_dict["NRG_PRO_I"],
        },
        ["REGIONS_9_I", "NRG_COMMODITIES_I", "NRG_PRO_I"],
    )
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[:, ["TO_elec"], :] = True
    except_subs.loc[:, ["TO_elec"], _subscript_dict["PROTRA_PP_I"]] = False
    value.values[except_subs.values] = 0
    value.loc[:, ["TO_elec"], _subscript_dict["PROTRA_PP_NON_CCS_I"]] = (
        protra_elec_expansion_request_with_limits()
        .loc[:, "TO_elec", _subscript_dict["PROTRA_PP_NON_CCS_I"]]
        .reset_coords(drop=True)
        .rename({"PROTRA_PP_I": "PROTRA_PP_NON_CCS_I"})
        .expand_dims({"NRG_COMMODITIES_I": ["TO_elec"]}, 1)
        .values
    )
    value.loc[:, ["TO_elec"], _subscript_dict["PROTRA_PP_CCS_I"]] = (
        if_then_else(
            np.logical_or(
                select_availability_unmature_energy_technologies_sp() == 1,
                select_availability_unmature_energy_technologies_sp() == 4,
            ),
            lambda: protra_elec_expansion_request_with_limits()
            .loc[:, "TO_elec", _subscript_dict["PROTRA_PP_CCS_I"]]
            .reset_coords(drop=True)
            .rename({"PROTRA_PP_I": "PROTRA_PP_CCS_I"}),
            lambda: xr.DataArray(
                0,
                {
                    "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                    "PROTRA_PP_CCS_I": _subscript_dict["PROTRA_PP_CCS_I"],
                },
                ["REGIONS_9_I", "PROTRA_PP_CCS_I"],
            ),
        )
        .expand_dims({"NRG_COMMODITIES_I": ["TO_elec"]}, 1)
        .values
    )
    return value


@component.add(
    name="PROTRA_elec_expansion_request_with_limits",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_COMMODITIES_I", "PROTRA_PP_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_elec_expansion_request_with_limits_res": 1,
        "protra_elec_expansion_request_with_limits_nres": 1,
    },
)
def protra_elec_expansion_request_with_limits():
    """
    Capacity expansion request for PROTRA elec incorporating RES potentials and global uranium maximum extraction curve. To avoid errors with low RES potentials' estimates, we consider the following cases: - The limitation cannot influence during historic time (i.e., before 2020). - If "remaining potential" < 0, then the new capacity is set to 0, and we let the capacity stock decrease due to decommissioning until the capacity stock and CF (before curtailment) matches the potential. - If "remaining potential" > 0, we let the potential limit the new additions in the future.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "NRG_COMMODITIES_I": _subscript_dict["NRG_COMMODITIES_I"],
            "PROTRA_PP_I": _subscript_dict["PROTRA_PP_I"],
        },
        ["REGIONS_9_I", "NRG_COMMODITIES_I", "PROTRA_PP_I"],
    )
    value.loc[:, ["TO_elec"], _subscript_dict["PROTRA_RES_PP_I"]] = (
        protra_elec_expansion_request_with_limits_res()
        .loc[:, "TO_elec", :]
        .reset_coords(drop=True)
        .expand_dims({"NRG_COMMODITIES_I": ["TO_elec"]}, 1)
        .values
    )
    value.loc[:, ["TO_elec"], _subscript_dict["PROTRA_PP_NRES_I"]] = (
        protra_elec_expansion_request_with_limits_nres()
        .loc[:, "TO_elec", :]
        .reset_coords(drop=True)
        .expand_dims({"NRG_COMMODITIES_I": ["TO_elec"]}, 1)
        .values
    )
    return value


@component.add(
    name="PROTRA_elec_expansion_request_with_limits_NRES",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_COMMODITIES_I", "PROTRA_PP_NRES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "remaining_elec_shortfall_to_be_allocated": 3,
        "switch_energy": 1,
        "switch_mat2nrg_uranium_availability": 1,
        "share_remaining_potential_uranium_extraction_rate_vs_pe_demand": 1,
    },
)
def protra_elec_expansion_request_with_limits_nres():
    """
    Capacity expansion request for PROTRA elec incorporating RES potentials and global uranium maximum extraction curve. To avoid errors with low RES potentials' estimates, we consider the following cases: - The limitation cannot influence during historic time (i.e., before 2020). - If "remaining potential" < 0, then the new capacity is set to 0, and we let the capacity stock decrease due to decommissioning until the capacity stock and CF (before curtailment) matches the potential. - If "remaining potential" > 0, we let the potential limit the new additions in the future.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "NRG_COMMODITIES_I": _subscript_dict["NRG_COMMODITIES_I"],
            "PROTRA_PP_NRES_I": _subscript_dict["PROTRA_PP_NRES_I"],
        },
        ["REGIONS_9_I", "NRG_COMMODITIES_I", "PROTRA_PP_NRES_I"],
    )
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[:, ["TO_elec"], :] = True
    except_subs.loc[:, ["TO_elec"], ["PROTRA_PP_nuclear"]] = False
    value.values[except_subs.values] = (
        remaining_elec_shortfall_to_be_allocated()
        .loc[:, "TO_elec"]
        .reset_coords(drop=True)
        .expand_dims({"NRG_COMMODITIES_I": ["TO_elec"]}, 1)
        .expand_dims({"PROTRA_PP_NRES_I": _subscript_dict["PROTRA_PP_NRES_I"]}, 2)
        .values[except_subs.loc[:, ["TO_elec"], :].values]
    )
    value.loc[:, ["TO_elec"], ["PROTRA_PP_nuclear"]] = (
        if_then_else(
            np.logical_or(
                switch_energy() == 1, switch_mat2nrg_uranium_availability() == 1
            ),
            lambda: if_then_else(
                share_remaining_potential_uranium_extraction_rate_vs_pe_demand() > 0,
                lambda: remaining_elec_shortfall_to_be_allocated()
                .loc[:, "TO_elec"]
                .reset_coords(drop=True),
                lambda: xr.DataArray(
                    0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
                ),
            ),
            lambda: remaining_elec_shortfall_to_be_allocated()
            .loc[:, "TO_elec"]
            .reset_coords(drop=True),
        )
        .expand_dims({"NRG_COMMODITIES_I": ["TO_elec"]}, 1)
        .expand_dims({"NRG_PRO_I": ["PROTRA_PP_nuclear"]}, 2)
        .values
    )
    return value


@component.add(
    name="PROTRA_elec_expansion_request_with_limits_RES",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_COMMODITIES_I", "PROTRA_RES_PP_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "remaining_potential_protra_res_pp": 5,
        "remaining_elec_shortfall_to_be_allocated": 9,
        "switch_nrg_limited_res_potentials": 4,
        "switch_law2nrg_solarland": 1,
        "switch_nrg_variability_effects": 4,
        "unlimited_protra_res_parameter": 1,
        "stress_signal_protra_curtailed": 4,
        "stress_signal_solar_land": 1,
        "switch_energy": 1,
    },
)
def protra_elec_expansion_request_with_limits_res():
    """
    Capacity expansion request for PROTRA elec incorporating RES potentials and global uranium maximum extraction curve. To avoid errors with low RES potentials' estimates, we consider the following cases: - The limitation cannot influence during historic time (i.e., before 2020). - If "remaining potential" < 0, then the new capacity is set to 0, and we let the capacity stock decrease due to decommissioning until the capacity stock and CF (before curtailment) matches the potential. - If "remaining potential" > 0, we let the potential limit the new additions in the future.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "NRG_COMMODITIES_I": _subscript_dict["NRG_COMMODITIES_I"],
            "PROTRA_RES_PP_I": _subscript_dict["PROTRA_RES_PP_I"],
        },
        ["REGIONS_9_I", "NRG_COMMODITIES_I", "PROTRA_RES_PP_I"],
    )
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[:, ["TO_elec"], :] = True
    except_subs.loc[:, ["TO_elec"], _subscript_dict["PROTRA_WIND_I"]] = False
    except_subs.loc[:, ["TO_elec"], ["PROTRA_PP_solar_open_space_PV"]] = False
    except_subs.loc[:, ["TO_elec"], ["PROTRA_PP_solar_urban_PV"]] = False
    except_subs.loc[:, ["TO_elec"], ["PROTRA_PP_solar_CSP"]] = False
    value.values[except_subs.values] = (
        if_then_else(
            remaining_potential_protra_res_pp()
            .loc[:, "TO_elec", :]
            .reset_coords(drop=True)
            > 0,
            lambda: remaining_elec_shortfall_to_be_allocated()
            .loc[:, "TO_elec"]
            .reset_coords(drop=True)
            .expand_dims({"PROTRA_RES_PP_I": _subscript_dict["PROTRA_RES_PP_I"]}, 1),
            lambda: xr.DataArray(
                0,
                {
                    "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                    "PROTRA_RES_PP_I": _subscript_dict["PROTRA_RES_PP_I"],
                },
                ["REGIONS_9_I", "PROTRA_RES_PP_I"],
            ),
        )
        .expand_dims({"NRG_COMMODITIES_I": ["TO_elec"]}, 1)
        .values[except_subs.loc[:, ["TO_elec"], :].values]
    )
    value.loc[:, ["TO_elec"], ["PROTRA_PP_solar_open_space_PV"]] = (
        (
            if_then_else(
                switch_nrg_limited_res_potentials() == 0,
                lambda: xr.DataArray(
                    unlimited_protra_res_parameter(),
                    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
                    ["REGIONS_9_I"],
                ),
                lambda: if_then_else(
                    np.logical_or(
                        switch_energy() == 0, switch_law2nrg_solarland() == 0
                    ),
                    lambda: if_then_else(
                        remaining_potential_protra_res_pp()
                        .loc[:, "TO_elec", "PROTRA_PP_solar_open_space_PV"]
                        .reset_coords(drop=True)
                        > 0,
                        lambda: remaining_elec_shortfall_to_be_allocated()
                        .loc[:, "TO_elec"]
                        .reset_coords(drop=True),
                        lambda: xr.DataArray(
                            0,
                            {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
                            ["REGIONS_9_I"],
                        ),
                    ),
                    lambda: remaining_elec_shortfall_to_be_allocated()
                    .loc[:, "TO_elec"]
                    .reset_coords(drop=True)
                    * stress_signal_solar_land(),
                ),
            )
            * (
                1
                - stress_signal_protra_curtailed()
                .loc[:, "TO_elec", "PROTRA_PP_solar_open_space_PV"]
                .reset_coords(drop=True)
                * switch_nrg_variability_effects()
            )
        )
        .expand_dims({"NRG_COMMODITIES_I": ["TO_elec"]}, 1)
        .expand_dims({"NRG_PRO_I": ["PROTRA_PP_solar_open_space_PV"]}, 2)
        .values
    )
    value.loc[:, ["TO_elec"], _subscript_dict["PROTRA_WIND_I"]] = (
        (
            if_then_else(
                switch_nrg_limited_res_potentials() == 1,
                lambda: if_then_else(
                    remaining_potential_protra_res_pp()
                    .loc[:, "TO_elec", _subscript_dict["PROTRA_WIND_I"]]
                    .reset_coords(drop=True)
                    .rename({"PROTRA_RES_PP_I": "PROTRA_WIND_I"})
                    > 0,
                    lambda: remaining_elec_shortfall_to_be_allocated()
                    .loc[:, "TO_elec"]
                    .reset_coords(drop=True)
                    .expand_dims(
                        {"PROTRA_WIND_I": _subscript_dict["PROTRA_WIND_I"]}, 1
                    ),
                    lambda: xr.DataArray(
                        0,
                        {
                            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                            "PROTRA_WIND_I": _subscript_dict["PROTRA_WIND_I"],
                        },
                        ["REGIONS_9_I", "PROTRA_WIND_I"],
                    ),
                ),
                lambda: remaining_elec_shortfall_to_be_allocated()
                .loc[:, "TO_elec"]
                .reset_coords(drop=True)
                .expand_dims({"PROTRA_WIND_I": _subscript_dict["PROTRA_WIND_I"]}, 1),
            )
            * (
                1
                - stress_signal_protra_curtailed()
                .loc[:, "TO_elec", _subscript_dict["PROTRA_WIND_I"]]
                .reset_coords(drop=True)
                .rename({"NRG_PROTRA_I": "PROTRA_WIND_I"})
                * switch_nrg_variability_effects()
            )
        )
        .expand_dims({"NRG_COMMODITIES_I": ["TO_elec"]}, 1)
        .values
    )
    value.loc[:, ["TO_elec"], ["PROTRA_PP_solar_urban_PV"]] = (
        (
            if_then_else(
                switch_nrg_limited_res_potentials() == 1,
                lambda: if_then_else(
                    remaining_potential_protra_res_pp()
                    .loc[:, "TO_elec", "PROTRA_PP_solar_urban_PV"]
                    .reset_coords(drop=True)
                    > 0,
                    lambda: remaining_elec_shortfall_to_be_allocated()
                    .loc[:, "TO_elec"]
                    .reset_coords(drop=True),
                    lambda: xr.DataArray(
                        0,
                        {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
                        ["REGIONS_9_I"],
                    ),
                ),
                lambda: remaining_elec_shortfall_to_be_allocated()
                .loc[:, "TO_elec"]
                .reset_coords(drop=True),
            )
            * (
                1
                - stress_signal_protra_curtailed()
                .loc[:, "TO_elec", "PROTRA_PP_solar_urban_PV"]
                .reset_coords(drop=True)
                * switch_nrg_variability_effects()
            )
        )
        .expand_dims({"NRG_COMMODITIES_I": ["TO_elec"]}, 1)
        .expand_dims({"NRG_PRO_I": ["PROTRA_PP_solar_urban_PV"]}, 2)
        .values
    )
    value.loc[:, ["TO_elec"], ["PROTRA_PP_solar_CSP"]] = (
        (
            if_then_else(
                switch_nrg_limited_res_potentials() == 1,
                lambda: if_then_else(
                    remaining_potential_protra_res_pp()
                    .loc[:, "TO_elec", "PROTRA_PP_solar_CSP"]
                    .reset_coords(drop=True)
                    > 0,
                    lambda: remaining_elec_shortfall_to_be_allocated()
                    .loc[:, "TO_elec"]
                    .reset_coords(drop=True),
                    lambda: xr.DataArray(
                        0,
                        {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
                        ["REGIONS_9_I"],
                    ),
                ),
                lambda: remaining_elec_shortfall_to_be_allocated()
                .loc[:, "TO_elec"]
                .reset_coords(drop=True),
            )
            * (
                1
                - stress_signal_protra_curtailed()
                .loc[:, "TO_elec", "PROTRA_PP_solar_CSP"]
                .reset_coords(drop=True)
                * switch_nrg_variability_effects()
            )
        )
        .expand_dims({"NRG_COMMODITIES_I": ["TO_elec"]}, 1)
        .expand_dims({"NRG_PRO_I": ["PROTRA_PP_solar_CSP"]}, 2)
        .values
    )
    return value


@component.add(
    name="PROTRA_elec_shortfall_allocation",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_TO_I", "NRG_PRO_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_elec_expansion_request": 1,
        "protra_priority_vector": 1,
        "remaining_elec_shortfall_to_be_allocated": 1,
    },
)
def protra_elec_shortfall_allocation():
    """
    Allocating remaining elec shortfall (after deducting elec-production from CHPs) to PP-technologies ALLOCATE_BY_PRIORITY( PROTRA_expansion_limit[REGIONS 9 I,TO elec,PROTRA PP I], PROTRA CAPACITY EXPANSION PRIORITIES VECTOR SP[REGIONS 9 I,PROTRA PP I], ELMCOUNT(PROTRA PP I), 0.1, remaining_shortfall_to_be_allocated[REGIONS 9 I,TO elec] )
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "NRG_TO_I": _subscript_dict["NRG_TO_I"],
            "NRG_PRO_I": _subscript_dict["NRG_PRO_I"],
        },
        ["REGIONS_9_I", "NRG_TO_I", "NRG_PRO_I"],
    )
    value.loc[:, ["TO_elec"], :] = (
        allocate_available(
            protra_elec_expansion_request()
            .loc[:, "TO_elec", :]
            .reset_coords(drop=True),
            protra_priority_vector(),
            remaining_elec_shortfall_to_be_allocated()
            .loc[:, "TO_elec"]
            .reset_coords(drop=True),
        )
        .expand_dims({"NRG_COMMODITIES_I": ["TO_elec"]}, 1)
        .values
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, ["TO_elec"], :] = False
    value.values[except_subs.values] = 0
    return value


@component.add(
    name="PROTRA_heat_expansion_request_with_RES_potentials",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_COMMODITIES_I", "PROTRA_CHP_HP_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "to_shortfall": 3,
        "switch_nrg_limited_res_potentials": 1,
        "remaining_potential_protra_res_chp_hp": 1,
    },
)
def protra_heat_expansion_request_with_res_potentials():
    """
    Capacity expansion request for PROTRA elec incorporating RES potentials. To avoid errors with low potentials' estimates, we consider the following cases: - The limitation cannot influence during historic time (i.e., before 2020). - If "remaining potential" < 0, then the new capacity is set to 0, and we let the capacity stock decrease due to decommissioning until the capacity stock and CF (before curtailment) matches the potential. - If "remaining potential" > 0, we let the potential limit the new additions in the future.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "NRG_COMMODITIES_I": _subscript_dict["NRG_COMMODITIES_I"],
            "PROTRA_CHP_HP_I": _subscript_dict["PROTRA_CHP_HP_I"],
        },
        ["REGIONS_9_I", "NRG_COMMODITIES_I", "PROTRA_CHP_HP_I"],
    )
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[:, ["TO_heat"], :] = True
    except_subs.loc[:, ["TO_heat"], _subscript_dict["PROTRA_RES_CHP_HP_I"]] = False
    value.values[except_subs.values] = (
        to_shortfall()
        .loc[:, "TO_heat"]
        .reset_coords(drop=True)
        .expand_dims({"NRG_COMMODITIES_I": ["TO_heat"]}, 1)
        .expand_dims({"PROTRA_CHP_HP_I": _subscript_dict["PROTRA_CHP_HP_I"]}, 2)
        .values[except_subs.loc[:, ["TO_heat"], :].values]
    )
    value.loc[:, ["TO_heat"], _subscript_dict["PROTRA_RES_CHP_HP_I"]] = (
        if_then_else(
            switch_nrg_limited_res_potentials() == 1,
            lambda: if_then_else(
                remaining_potential_protra_res_chp_hp()
                .loc[:, "TO_heat", :]
                .reset_coords(drop=True)
                > 0,
                lambda: to_shortfall()
                .loc[:, "TO_heat"]
                .reset_coords(drop=True)
                .expand_dims(
                    {"PROTRA_RES_CHP_HP_I": _subscript_dict["PROTRA_RES_CHP_HP_I"]}, 1
                ),
                lambda: xr.DataArray(
                    0,
                    {
                        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                        "PROTRA_RES_CHP_HP_I": _subscript_dict["PROTRA_RES_CHP_HP_I"],
                    },
                    ["REGIONS_9_I", "PROTRA_RES_CHP_HP_I"],
                ),
            ),
            lambda: to_shortfall()
            .loc[:, "TO_heat"]
            .reset_coords(drop=True)
            .expand_dims(
                {"PROTRA_RES_CHP_HP_I": _subscript_dict["PROTRA_RES_CHP_HP_I"]}, 1
            ),
        )
        .expand_dims({"NRG_COMMODITIES_I": ["TO_heat"]}, 1)
        .values
    )
    return value


@component.add(
    name="PROTRA_heat_shortfall_allocation",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_COMMODITIES_I", "NRG_PRO_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_chp_and_hp_expansion_request": 1,
        "protra_priority_vector": 1,
        "to_shortfall": 1,
    },
)
def protra_heat_shortfall_allocation():
    """
    Allocating heat shortfall to new heat (CHP and HP) capacities
    """
    return allocate_available(
        protra_chp_and_hp_expansion_request()
        .loc[:, "TO_heat", :]
        .reset_coords(drop=True),
        protra_priority_vector(),
        to_shortfall().loc[:, "TO_heat"].reset_coords(drop=True),
    ).expand_dims({"NRG_COMMODITIES_I": ["TO_heat"]}, 1)


@component.add(
    name="PROTRA_LIFETIME",
    units="Year",
    subscripts=["REGIONS_9_I", "NRG_PROTRA_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_protra_lifetime"},
)
def protra_lifetime():
    return _ext_constant_protra_lifetime()


_ext_constant_protra_lifetime = ExtConstant(
    "model_parameters/energy/energy.xlsm",
    "CHINA",
    "PROTRA_LIFETIME*",
    {"REGIONS_9_I": ["CHINA"], "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"]},
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
    },
    "_ext_constant_protra_lifetime",
)

_ext_constant_protra_lifetime.add(
    "model_parameters/energy/energy.xlsm",
    "EASOC",
    "PROTRA_LIFETIME*",
    {"REGIONS_9_I": ["EASOC"], "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"]},
)

_ext_constant_protra_lifetime.add(
    "model_parameters/energy/energy.xlsm",
    "EU27",
    "PROTRA_LIFETIME*",
    {"REGIONS_9_I": ["EU27"], "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"]},
)

_ext_constant_protra_lifetime.add(
    "model_parameters/energy/energy.xlsm",
    "INDIA",
    "PROTRA_LIFETIME*",
    {"REGIONS_9_I": ["INDIA"], "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"]},
)

_ext_constant_protra_lifetime.add(
    "model_parameters/energy/energy.xlsm",
    "LATAM",
    "PROTRA_LIFETIME*",
    {"REGIONS_9_I": ["LATAM"], "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"]},
)

_ext_constant_protra_lifetime.add(
    "model_parameters/energy/energy.xlsm",
    "LROW",
    "PROTRA_LIFETIME*",
    {"REGIONS_9_I": ["LROW"], "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"]},
)

_ext_constant_protra_lifetime.add(
    "model_parameters/energy/energy.xlsm",
    "RUSSIA",
    "PROTRA_LIFETIME*",
    {"REGIONS_9_I": ["RUSSIA"], "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"]},
)

_ext_constant_protra_lifetime.add(
    "model_parameters/energy/energy.xlsm",
    "UK",
    "PROTRA_LIFETIME*",
    {"REGIONS_9_I": ["UK"], "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"]},
)

_ext_constant_protra_lifetime.add(
    "model_parameters/energy/energy.xlsm",
    "USMCA",
    "PROTRA_LIFETIME*",
    {"REGIONS_9_I": ["USMCA"], "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"]},
)


@component.add(
    name="PROTRA_PP_solar_PV_by_subtechnology_capacity_decomissioning",
    units="TW/Year",
    subscripts=[
        "REGIONS_9_I",
        "PROTRA_PP_SOLAR_PV_I",
        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "capacity_stock_protra_pp_solar_pv_by_subtechnology": 2,
        "protra_lifetime": 2,
    },
)
def protra_pp_solar_pv_by_subtechnology_capacity_decomissioning():
    """
    Decomissed solar PV capacity installed by panel subtechnology
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "PROTRA_PP_SOLAR_PV_I": _subscript_dict["PROTRA_PP_SOLAR_PV_I"],
            "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": _subscript_dict[
                "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"
            ],
        },
        ["REGIONS_9_I", "PROTRA_PP_SOLAR_PV_I", "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"],
    )
    value.loc[:, ["PROTRA_PP_solar_open_space_PV"], :] = (
        np.maximum(
            capacity_stock_protra_pp_solar_pv_by_subtechnology()
            .loc[:, "PROTRA_PP_solar_open_space_PV", :]
            .reset_coords(drop=True)
            * zidz(
                xr.DataArray(
                    1, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
                ),
                protra_lifetime()
                .loc[:, "PROTRA_PP_solar_open_space_PV"]
                .reset_coords(drop=True),
            ),
            0,
        )
        .expand_dims({"NRG_PRO_I": ["PROTRA_PP_solar_open_space_PV"]}, 1)
        .values
    )
    value.loc[:, ["PROTRA_PP_solar_urban_PV"], :] = (
        np.maximum(
            capacity_stock_protra_pp_solar_pv_by_subtechnology()
            .loc[:, "PROTRA_PP_solar_urban_PV", :]
            .reset_coords(drop=True)
            * zidz(
                xr.DataArray(
                    1, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
                ),
                protra_lifetime()
                .loc[:, "PROTRA_PP_solar_urban_PV"]
                .reset_coords(drop=True),
            ),
            0,
        )
        .expand_dims({"NRG_PRO_I": ["PROTRA_PP_solar_urban_PV"]}, 1)
        .values
    )
    return value


@component.add(
    name="PROTRA_PP_solar_PV_by_subtechnology_capacity_expansion",
    units="TW/Year",
    subscripts=[
        "REGIONS_9_I",
        "PROTRA_PP_SOLAR_PV_I",
        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_capacity_expansion": 2,
        "share_new_pv_subtechn_land": 1,
        "share_new_pv_subtechn_urban": 1,
    },
)
def protra_pp_solar_pv_by_subtechnology_capacity_expansion():
    """
    new solar PV capacity installed by panel subtechnology
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "PROTRA_PP_SOLAR_PV_I": _subscript_dict["PROTRA_PP_SOLAR_PV_I"],
            "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": _subscript_dict[
                "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"
            ],
        },
        ["REGIONS_9_I", "PROTRA_PP_SOLAR_PV_I", "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"],
    )
    value.loc[:, ["PROTRA_PP_solar_open_space_PV"], :] = (
        (
            protra_capacity_expansion()
            .loc[:, "TO_elec", "PROTRA_PP_solar_open_space_PV"]
            .reset_coords(drop=True)
            * share_new_pv_subtechn_land()
        )
        .expand_dims({"NRG_PRO_I": ["PROTRA_PP_solar_open_space_PV"]}, 1)
        .values
    )
    value.loc[:, ["PROTRA_PP_solar_urban_PV"], :] = (
        (
            protra_capacity_expansion()
            .loc[:, "TO_elec", "PROTRA_PP_solar_urban_PV"]
            .reset_coords(drop=True)
            * share_new_pv_subtechn_urban()
        )
        .expand_dims({"NRG_PRO_I": ["PROTRA_PP_solar_urban_PV"]}, 1)
        .values
    )
    return value


@component.add(
    name="protra_priority_vector",
    subscripts=["REGIONS_9_I", "NRG_PRO_I", "pprofile"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "pwidth_protra_capacity_expansion_priorities_vector_sp": 1,
        "protra_capacity_expansion_policy_weight_sp": 2,
        "model_explorer_protra_capacity_expansion": 1,
        "switch_model_explorer": 1,
        "protra_capacity_expansion_priorities_vector_sp": 1,
        "lcoe_by_protra_priority_signal": 1,
    },
)
def protra_priority_vector():
    """
    PROTRA_CAPACITY_EXPANSION_PRIORITIES_VECTOR_SP[REGIONS 9 I,NRG PROTRA I]
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "NRG_PRO_I": _subscript_dict["NRG_PRO_I"],
            "pprofile": _subscript_dict["pprofile"],
        },
        ["REGIONS_9_I", "NRG_PRO_I", "pprofile"],
    )
    value.loc[:, :, ["ptype"]] = 3
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[:, :, ["ppriority"]] = True
    except_subs.loc[:, _subscript_dict["NRG_PROTRA_I"], ["ppriority"]] = False
    value.values[except_subs.values] = 0
    value.loc[
        :, :, ["pwidth"]
    ] = pwidth_protra_capacity_expansion_priorities_vector_sp()
    value.loc[:, :, ["pextra"]] = 0
    value.loc[:, _subscript_dict["NRG_PROTRA_I"], ["ppriority"]] = (
        if_then_else(
            switch_model_explorer() == 1,
            lambda: model_explorer_protra_capacity_expansion(),
            lambda: protra_capacity_expansion_policy_weight_sp()
            * protra_capacity_expansion_priorities_vector_sp()
            + (1 - protra_capacity_expansion_policy_weight_sp())
            * lcoe_by_protra_priority_signal(),
        )
        .expand_dims({"pprofile": ["ppriority"]}, 2)
        .values
    )
    return value


@component.add(
    name="PROTRA_shortfall_allocation",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_TO_I", "NRG_PROTRA_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "production_from_chp_expansion": 1,
        "protra_elec_shortfall_allocation": 1,
        "production_from_hp_expansion": 1,
    },
)
def protra_shortfall_allocation():
    """
    Shortfall allocated to PROTRA. Equals the energy production potential of the new production capacity. No-Process processes (gas, hydrogen etc.) are set to 0 (no expansion, as capacity is very big already anyway)
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "NRG_TO_I": _subscript_dict["NRG_TO_I"],
            "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
        },
        ["REGIONS_9_I", "NRG_TO_I", "NRG_PROTRA_I"],
    )
    value.loc[
        :, :, _subscript_dict["PROTRA_CHP_I"]
    ] = production_from_chp_expansion().values
    value.loc[:, :, _subscript_dict["PROTRA_PP_I"]] = (
        protra_elec_shortfall_allocation()
        .loc[:, :, _subscript_dict["PROTRA_PP_I"]]
        .rename({"NRG_PRO_I": "PROTRA_PP_I"})
        .values
    )
    value.loc[:, :, _subscript_dict["PROTRA_HP_I"]] = (
        production_from_hp_expansion()
        .loc[:, :, _subscript_dict["PROTRA_HP_I"]]
        .rename({"NRG_PRO_I": "PROTRA_HP_I"})
        .values
    )
    value.loc[:, :, _subscript_dict["PROTRA_NP_I"]] = 0
    return value


@component.add(
    name="PWIDTH_PROTRA_CAPACITY_EXPANSION_PRIORITIES_VECTOR_SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_pwidth_protra_capacity_expansion_priorities_vector_sp"
    },
)
def pwidth_protra_capacity_expansion_priorities_vector_sp():
    """
    One of the parameters of the Vensim ALLOCATE_AVAILABLE function used to specify the curves to be used for supply and demand. Note that the priorities and widths specified should all be of the same order of magnitude. For example, it does not make sense to have one priority be 20 and another 2e6 if width is 100.
    """
    return _ext_constant_pwidth_protra_capacity_expansion_priorities_vector_sp()


_ext_constant_pwidth_protra_capacity_expansion_priorities_vector_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "PWIDTH_PROTRA_CAPACITY_EXPANSION_PRIORITIES_VECTOR_SP",
    {},
    _root,
    {},
    "_ext_constant_pwidth_protra_capacity_expansion_priorities_vector_sp",
)


@component.add(
    name="remaining_elec_shortfall_to_be_allocated",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_COMMODITIES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"to_shortfall": 1, "production_from_chp_expansion": 1},
)
def remaining_elec_shortfall_to_be_allocated():
    """
    TO_elec quantity that remains to be allocated after deducting CHP-Production.
    """
    return np.maximum(
        to_shortfall().loc[:, "TO_elec"].reset_coords(drop=True)
        - sum(
            production_from_chp_expansion()
            .loc[:, "TO_elec", :]
            .reset_coords(drop=True)
            .rename({"PROTRA_CHP_I": "PROTRA_CHP_I!"}),
            dim=["PROTRA_CHP_I!"],
        ),
        0,
    ).expand_dims({"NRG_COMMODITIES_I": ["TO_elec"]}, 1)


@component.add(
    name="remaining_global_shortfall_after_heat_allocation",
    units="EJ/Year",
    subscripts=["NRG_TO_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "remaining_elec_shortfall_to_be_allocated": 1,
        "to_shortfall": 2,
        "protra_heat_shortfall_allocation": 1,
    },
)
def remaining_global_shortfall_after_heat_allocation():
    """
    check variable: remaining global shortfall after heat allocation
    """
    value = xr.DataArray(
        np.nan, {"NRG_TO_I": _subscript_dict["NRG_TO_I"]}, ["NRG_TO_I"]
    )
    value.loc[["TO_elec"]] = sum(
        remaining_elec_shortfall_to_be_allocated()
        .loc[:, "TO_elec"]
        .reset_coords(drop=True)
        .rename({"REGIONS_9_I": "REGIONS_9_I!"}),
        dim=["REGIONS_9_I!"],
    )
    value.loc[["TO_heat"]] = sum(
        to_shortfall()
        .loc[:, "TO_heat"]
        .reset_coords(drop=True)
        .rename({"REGIONS_9_I": "REGIONS_9_I!"}),
        dim=["REGIONS_9_I!"],
    ) - sum(
        protra_heat_shortfall_allocation()
        .loc[:, "TO_heat", _subscript_dict["PROTRA_CHP_HP_I"]]
        .reset_coords(drop=True)
        .rename({"REGIONS_9_I": "REGIONS_9_I!", "NRG_PRO_I": "PROTRA_CHP_HP_I!"}),
        dim=["REGIONS_9_I!", "PROTRA_CHP_HP_I!"],
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[["TO_elec"]] = False
    except_subs.loc[["TO_heat"]] = False
    value.values[except_subs.values] = sum(
        to_shortfall().rename({"REGIONS_9_I": "REGIONS_9_I!"}), dim=["REGIONS_9_I!"]
    ).values[except_subs.values]
    return value


@component.add(
    name="share_capacity_stock_PROTRA_PP_solar_PV_by_subtechnology",
    units="1",
    subscripts=[
        "REGIONS_9_I",
        "PROTRA_PP_SOLAR_PV_I",
        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"capacity_stock_protra_pp_solar_pv_by_subtechnology": 4},
)
def share_capacity_stock_protra_pp_solar_pv_by_subtechnology():
    """
    Share of each subtechnoly solar PV capacity installed respect total PV capacity.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "PROTRA_PP_SOLAR_PV_I": _subscript_dict["PROTRA_PP_SOLAR_PV_I"],
            "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": _subscript_dict[
                "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"
            ],
        },
        ["REGIONS_9_I", "PROTRA_PP_SOLAR_PV_I", "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"],
    )
    value.loc[:, ["PROTRA_PP_solar_open_space_PV"], :] = (
        zidz(
            capacity_stock_protra_pp_solar_pv_by_subtechnology()
            .loc[:, "PROTRA_PP_solar_open_space_PV", :]
            .reset_coords(drop=True),
            sum(
                capacity_stock_protra_pp_solar_pv_by_subtechnology()
                .loc[:, "PROTRA_PP_solar_open_space_PV", :]
                .reset_coords(drop=True)
                .rename(
                    {
                        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!"
                    }
                ),
                dim=["PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!"],
            ).expand_dims(
                {
                    "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": _subscript_dict[
                        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"
                    ]
                },
                1,
            ),
        )
        .expand_dims({"NRG_PRO_I": ["PROTRA_PP_solar_open_space_PV"]}, 1)
        .values
    )
    value.loc[:, ["PROTRA_PP_solar_urban_PV"], :] = (
        zidz(
            capacity_stock_protra_pp_solar_pv_by_subtechnology()
            .loc[:, "PROTRA_PP_solar_urban_PV", :]
            .reset_coords(drop=True),
            sum(
                capacity_stock_protra_pp_solar_pv_by_subtechnology()
                .loc[:, "PROTRA_PP_solar_urban_PV", :]
                .reset_coords(drop=True)
                .rename(
                    {
                        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!"
                    }
                ),
                dim=["PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!"],
            ).expand_dims(
                {
                    "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": _subscript_dict[
                        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"
                    ]
                },
                1,
            ),
        )
        .expand_dims({"NRG_PRO_I": ["PROTRA_PP_solar_urban_PV"]}, 1)
        .values
    )
    return value


@component.add(
    name="share_PROTRA_capacity_stock_EU27",
    units="DMNL",
    subscripts=["REGIONS_EU27_I", "NRG_TO_I", "NRG_PROTRA_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"protra_capacity_stock_eu27": 2},
)
def share_protra_capacity_stock_eu27():
    """
    Share of PROTRA capacity stock of each EU 27 country with relation to the total EU27.
    """
    return zidz(
        protra_capacity_stock_eu27(),
        sum(
            protra_capacity_stock_eu27().rename({"REGIONS_EU27_I": "REGIONS_EU27_I!"}),
            dim=["REGIONS_EU27_I!"],
        ).expand_dims({"REGIONS_EU27_I": _subscript_dict["REGIONS_EU27_I"]}, 0),
    )


@component.add(
    name="share_PV_capacity_by_subtechnology",
    units="1",
    subscripts=[
        "REGIONS_9_I",
        "PROTRA_PP_SOLAR_PV_I",
        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"capacity_stock_protra_pp_solar_pv_by_subtechnology": 4},
)
def share_pv_capacity_by_subtechnology():
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "PROTRA_PP_SOLAR_PV_I": _subscript_dict["PROTRA_PP_SOLAR_PV_I"],
            "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": _subscript_dict[
                "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"
            ],
        },
        ["REGIONS_9_I", "PROTRA_PP_SOLAR_PV_I", "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"],
    )
    value.loc[:, ["PROTRA_PP_solar_open_space_PV"], :] = (
        zidz(
            capacity_stock_protra_pp_solar_pv_by_subtechnology()
            .loc[:, "PROTRA_PP_solar_open_space_PV", :]
            .reset_coords(drop=True),
            sum(
                capacity_stock_protra_pp_solar_pv_by_subtechnology()
                .loc[:, "PROTRA_PP_solar_open_space_PV", :]
                .reset_coords(drop=True)
                .rename(
                    {
                        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!"
                    }
                ),
                dim=["PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!"],
            ).expand_dims(
                {
                    "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": _subscript_dict[
                        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"
                    ]
                },
                1,
            ),
        )
        .expand_dims({"NRG_PRO_I": ["PROTRA_PP_solar_open_space_PV"]}, 1)
        .values
    )
    value.loc[:, ["PROTRA_PP_solar_urban_PV"], :] = (
        zidz(
            capacity_stock_protra_pp_solar_pv_by_subtechnology()
            .loc[:, "PROTRA_PP_solar_urban_PV", :]
            .reset_coords(drop=True),
            sum(
                capacity_stock_protra_pp_solar_pv_by_subtechnology()
                .loc[:, "PROTRA_PP_solar_urban_PV", :]
                .reset_coords(drop=True)
                .rename(
                    {
                        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!"
                    }
                ),
                dim=["PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!"],
            ).expand_dims(
                {
                    "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": _subscript_dict[
                        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"
                    ]
                },
                1,
            ),
        )
        .expand_dims({"NRG_PRO_I": ["PROTRA_PP_solar_urban_PV"]}, 1)
        .values
    )
    return value


@component.add(
    name="SHARE_PV_SUBTECHNOLOGIES_BEFORE_2020",
    units="DMNL",
    subscripts=["PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"],
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_share_pv_subtechnologies_before_2020",
        "__data__": "_ext_data_share_pv_subtechnologies_before_2020",
        "time": 1,
    },
)
def share_pv_subtechnologies_before_2020():
    """
    historical share data from photovoltaics report (Fraunhofer)
    """
    return _ext_data_share_pv_subtechnologies_before_2020(time())


_ext_data_share_pv_subtechnologies_before_2020 = ExtData(
    "model_parameters/energy/energy.xlsm",
    "PV",
    "SHARE_PV_BEFORE_2020_TIME",
    "SHARE_PV_BEFORE_2020",
    "interpolate",
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
    "_ext_data_share_pv_subtechnologies_before_2020",
)


@component.add(
    name="stress_signal_PROTRA_curtailed",
    units="DMNL",
    subscripts=["REGIONS_9_I", "NRG_COMMODITIES_I", "NRG_PROTRA_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cf_loss_share_stopping_protra_capacity_expansion_sp": 1,
        "variation_cf_curtailed_protra": 1,
    },
)
def stress_signal_protra_curtailed():
    """
    Capacity expansion request falls to 0 when the variation of CF falls to the value of CF_LOSS_SHARE_STOPPING_PROTRA_CAPACITY_EXPANSION_SP.
    """
    return np.minimum(
        1,
        np.maximum(
            0,
            (0 - 1)
            / (0 - cf_loss_share_stopping_protra_capacity_expansion_sp())
            * variation_cf_curtailed_protra()
            .loc[:, "TO_elec", :]
            .reset_coords(drop=True),
        ),
    ).expand_dims({"NRG_COMMODITIES_I": ["TO_elec"]}, 1)


@component.add(
    name="SWITCH_LAW2NRG_SOLARLAND",
    units="1",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_law2nrg_solarland"},
)
def switch_law2nrg_solarland():
    """
    Intermodule links SWITCH, it can take two values: 0: the link is broken, the intermodule variable is replaced by an exogenous parameter. 1: the link between modules is operational.
    """
    return _ext_constant_switch_law2nrg_solarland()


_ext_constant_switch_law2nrg_solarland = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_LAW2NRG_SOLARLAND",
    {},
    _root,
    {},
    "_ext_constant_switch_law2nrg_solarland",
)


@component.add(
    name="SWITCH_MAT2NRG_URANIUM_AVAILABILITY",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_mat2nrg_uranium_availability"},
)
def switch_mat2nrg_uranium_availability():
    """
    This SWITCH can take 2 values: 1: uranium use is constrained by uranium availability in materials module 0: uranium use is unlimited
    """
    return _ext_constant_switch_mat2nrg_uranium_availability()


_ext_constant_switch_mat2nrg_uranium_availability = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_MAT2NRG_URANIUM_AVAILABILITY",
    {},
    _root,
    {},
    "_ext_constant_switch_mat2nrg_uranium_availability",
)


@component.add(
    name="TO_available_by_commodity",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_TO_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_capacity_stock": 2,
        "protra_max_full_load_hours_after_constraints": 2,
        "unit_conversion_tw_per_ej_per_year": 2,
        "chp_capacity_utilization_rate": 1,
    },
)
def to_available_by_commodity():
    """
    max TO that can be produced from existing PROTRA stock; Max heat production is based on max. full load hours (of CHPs and HP). Max elec production is based on ACTUAL full load hours of CHPs (neccesary because of the stepwise allocation approach) and max. full load hours of PP.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "NRG_TO_I": _subscript_dict["NRG_TO_I"],
        },
        ["REGIONS_9_I", "NRG_TO_I"],
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, ["TO_elec"]] = False
    value.values[except_subs.values] = vector_select(
        protra_capacity_stock().rename({"NRG_PROTRA_I": "NRG_PROTRA_I!"}),
        (
            protra_max_full_load_hours_after_constraints().rename(
                {"NRG_PROTRA_I": "NRG_PROTRA_I!"}
            )
            * unit_conversion_tw_per_ej_per_year()
        ).expand_dims({"NRG_TO_I": _subscript_dict["NRG_TO_I"]}, 1),
        ["NRG_PROTRA_I!"],
        0,
        0,
        0,
    ).values[except_subs.values]
    value.loc[:, ["TO_elec"]] = (
        vector_select(
            protra_capacity_stock()
            .loc[:, "TO_elec", :]
            .reset_coords(drop=True)
            .rename({"NRG_PROTRA_I": "NRG_PROTRA_I!"}),
            protra_max_full_load_hours_after_constraints().rename(
                {"NRG_PROTRA_I": "NRG_PROTRA_I!"}
            )
            * chp_capacity_utilization_rate()
            .loc[:, "TO_elec", :]
            .reset_coords(drop=True)
            .rename({"NRG_PROTRA_I": "NRG_PROTRA_I!"})
            * unit_conversion_tw_per_ej_per_year(),
            ["NRG_PROTRA_I!"],
            0,
            0,
            0,
        )
        .expand_dims({"NRG_COMMODITIES_I": ["TO_elec"]}, 1)
        .values
    )
    return value


@component.add(
    name="TO_decomissioned_by_commodity",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_TO_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_capacity_decommissioning": 1,
        "protra_max_full_load_hours_after_constraints": 1,
        "unit_conversion_tw_per_ej_per_year": 1,
    },
)
def to_decomissioned_by_commodity():
    """
    TO that is missing in the next year because of decomissioned PROTRA capacities
    """
    return vector_select(
        protra_capacity_decommissioning().rename({"NRG_PROTRA_I": "NRG_PROTRA_I!"}),
        (
            protra_max_full_load_hours_after_constraints().rename(
                {"NRG_PROTRA_I": "NRG_PROTRA_I!"}
            )
            * unit_conversion_tw_per_ej_per_year()
        ).expand_dims({"NRG_TO_I": _subscript_dict["NRG_TO_I"]}, 1),
        ["NRG_PROTRA_I!"],
        0,
        0,
        0,
    )


@component.add(
    name="TO_required",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_TO_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"to_by_commodity": 1, "applied_to_reserve_factor_by_commodity": 1},
)
def to_required():
    """
    TO required including overcapacity to account for next timesteps growth
    """
    return to_by_commodity() * applied_to_reserve_factor_by_commodity()


@component.add(
    name="TO_shortfall",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_TO_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"to_required": 1, "to_available_by_commodity": 1},
)
def to_shortfall():
    """
    Additional TO that needs to be provided to account for current demand (in time t) and additional demand for decomissioned capacities and demand growth (in t+1)
    """
    return np.maximum(0, to_required() - to_available_by_commodity())
