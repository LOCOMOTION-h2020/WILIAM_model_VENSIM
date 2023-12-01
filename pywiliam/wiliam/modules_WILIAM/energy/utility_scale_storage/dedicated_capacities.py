"""
Module energy.utility_scale_storage.dedicated_capacities
Translated using PySD version 3.10.0
"""


@component.add(
    name="ANNUAL_VARIATION_CAPACITY_EXPANSION_PROSTO_DEDICATED_SP",
    units="1/Year",
    subscripts=["REGIONS_9_I", "PROSTO_ELEC_DEDICATED_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_annual_variation_capacity_expansion_prosto_dedicated_sp"
    },
)
def annual_variation_capacity_expansion_prosto_dedicated_sp():
    return _ext_constant_annual_variation_capacity_expansion_prosto_dedicated_sp()


_ext_constant_annual_variation_capacity_expansion_prosto_dedicated_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "ANNUAL_VARIATION_CAPACITY_EXPANSION_PROSTO_DEDICATED_SP",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PROSTO_ELEC_DEDICATED_I": _subscript_dict["PROSTO_ELEC_DEDICATED_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PROSTO_ELEC_DEDICATED_I": _subscript_dict["PROSTO_ELEC_DEDICATED_I"],
    },
    "_ext_constant_annual_variation_capacity_expansion_prosto_dedicated_sp",
)


@component.add(
    name="HISTORIC_ANNUAL_GROWTH_CAPACITY_EXPANSION_PROSTO_DEDICATED",
    units="1/Year",
    subscripts=["REGIONS_9_I", "PROSTO_ELEC_DEDICATED_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_historic_annual_growth_capacity_expansion_prosto_dedicated"
    },
)
def historic_annual_growth_capacity_expansion_prosto_dedicated():
    """
    Historic annual growth capacity expansion of dedicated facilities to store energy at utility-scale level.
    """
    return _ext_constant_historic_annual_growth_capacity_expansion_prosto_dedicated()


_ext_constant_historic_annual_growth_capacity_expansion_prosto_dedicated = ExtConstant(
    "model_parameters/energy/energy-storage.xlsx",
    "Dedicated_capacities",
    "RELATIVE_HISTORIC_GROWTH_CAPACITY_EXPANSION_PROSTO_DEDICATED",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PROSTO_ELEC_DEDICATED_I": _subscript_dict["PROSTO_ELEC_DEDICATED_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PROSTO_ELEC_DEDICATED_I": _subscript_dict["PROSTO_ELEC_DEDICATED_I"],
    },
    "_ext_constant_historic_annual_growth_capacity_expansion_prosto_dedicated",
)


@component.add(
    name="HISTORIC_CAPACITY_EXPANSION_STATIONARY_BATERIES",
    units="TW/Year",
    subscripts=["REGIONS_9_I", "NRG_PRO_I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_historic_capacity_expansion_stationary_bateries",
        "__lookup__": "_ext_lookup_historic_capacity_expansion_stationary_bateries",
    },
)
def historic_capacity_expansion_stationary_bateries(x, final_subs=None):
    """
    Historic evolution of new capacity additions of stationary batteries per region.
    """
    return _ext_lookup_historic_capacity_expansion_stationary_bateries(x, final_subs)


_ext_lookup_historic_capacity_expansion_stationary_bateries = ExtLookup(
    "model_parameters/energy/energy-storage.xlsx",
    "Dedicated_capacities",
    "Time_stationary_batteries",
    "HIST_CAPACITY_STATIONATY_BATTERIES_ADDITION",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "NRG_PRO_I": ["PROSTO_STATIONARY_BATTERIES"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "NRG_PRO_I": _subscript_dict["NRG_PRO_I"],
    },
    "_ext_lookup_historic_capacity_expansion_stationary_bateries",
)


@component.add(
    name="INITIAL_PROSTO_DEDICATED_CAPACITY_STOCK",
    units="MW",
    subscripts=["REGIONS_9_I", "PROSTO_ELEC_DEDICATED_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_initial_prosto_dedicated_capacity_stock"
    },
)
def initial_prosto_dedicated_capacity_stock():
    """
    Capacity stock of dedicated facilities to store energy at utility-scale level in the initial year of the simulation.
    """
    return _ext_constant_initial_prosto_dedicated_capacity_stock()


_ext_constant_initial_prosto_dedicated_capacity_stock = ExtConstant(
    "model_parameters/energy/energy-storage.xlsx",
    "Dedicated_capacities",
    "INITIAL_PROSTO_CAPACITY_STOCK",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PROSTO_ELEC_DEDICATED_I": _subscript_dict["PROSTO_ELEC_DEDICATED_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PROSTO_ELEC_DEDICATED_I": _subscript_dict["PROSTO_ELEC_DEDICATED_I"],
    },
    "_ext_constant_initial_prosto_dedicated_capacity_stock",
)


@component.add(
    name="INITIAL_YEAR_ANNUAL_VARIATION_CAPACITY_EXPANSION_PROSTO_DEDICATED_SP",
    units="Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_initial_year_annual_variation_capacity_expansion_prosto_dedicated_sp"
    },
)
def initial_year_annual_variation_capacity_expansion_prosto_dedicated_sp():
    return (
        _ext_constant_initial_year_annual_variation_capacity_expansion_prosto_dedicated_sp()
    )


_ext_constant_initial_year_annual_variation_capacity_expansion_prosto_dedicated_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "INITIAL_YEAR_ANNUAL_VARIATION_CAPACITY_EXPANSION_PROSTO_DEDICATED_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_initial_year_annual_variation_capacity_expansion_prosto_dedicated_sp",
)


@component.add(
    name="limited_capacity_expansion_PROSTO_dedicated",
    units="TW/Year",
    subscripts=["REGIONS_9_I", "PROSTO_ELEC_DEDICATED_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "initial_year_annual_variation_capacity_expansion_prosto_dedicated_sp": 1,
        "historic_annual_growth_capacity_expansion_prosto_dedicated": 1,
        "annual_variation_capacity_expansion_prosto_dedicated_sp": 1,
        "remaining_potential_capacity_by_prosto": 1,
        "prosto_dedicated_capacity_stock": 1,
    },
)
def limited_capacity_expansion_prosto_dedicated():
    """
    Capacity expansion of dedicated storage utility-scale facilities taking into account scenario and techno-sustainable limits.
    """
    return (
        if_then_else(
            (
                time()
                < initial_year_annual_variation_capacity_expansion_prosto_dedicated_sp()
            ).expand_dims(
                {"PROSTO_ELEC_DEDICATED_I": _subscript_dict["PROSTO_ELEC_DEDICATED_I"]},
                1,
            ),
            lambda: historic_annual_growth_capacity_expansion_prosto_dedicated(),
            lambda: annual_variation_capacity_expansion_prosto_dedicated_sp(),
        )
        * remaining_potential_capacity_by_prosto()
        * prosto_dedicated_capacity_stock()
    )


@component.add(
    name="maximum_PROSTO_dedicated",
    units="TW",
    subscripts=["REGIONS_9_I", "PROSTO_ELEC_DEDICATED_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"phs_potential": 1, "stationary_batteries_maximum_sp": 1},
)
def maximum_prosto_dedicated():
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "PROSTO_ELEC_DEDICATED_I": _subscript_dict["PROSTO_ELEC_DEDICATED_I"],
        },
        ["REGIONS_9_I", "PROSTO_ELEC_DEDICATED_I"],
    )
    value.loc[:, ["PROSTO_PHS"]] = (
        phs_potential().expand_dims({"NRG_PRO_I": ["PROSTO_PHS"]}, 1).values
    )
    value.loc[:, ["PROSTO_STATIONARY_BATTERIES"]] = (
        stationary_batteries_maximum_sp()
        .expand_dims({"NRG_PRO_I": ["PROSTO_STATIONARY_BATTERIES"]}, 1)
        .values
    )
    return value


@component.add(
    name="PHS_POTENTIAL",
    units="TW",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_phs_potential"},
)
def phs_potential():
    """
    Techno-sustainable potential of PHS by region. Stylized approach based on MEDEAS method (1 * potential of hydropower to account for both open and closed loops).
    """
    return _ext_constant_phs_potential()


_ext_constant_phs_potential = ExtConstant(
    "model_parameters/energy/energy-potentials.xlsx",
    "PROSTO",
    "PHS_POTENTIAL*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_phs_potential",
)


@component.add(
    name="PROSTO_dedicated_capacity_decomissioning",
    units="TW/Year",
    subscripts=["REGIONS_9_I", "PROSTO_ELEC_DEDICATED_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"prosto_dedicated_capacity_stock": 1, "prosto_dedicated_lifetime": 1},
)
def prosto_dedicated_capacity_decomissioning():
    """
    Capacity decommmissioning due to end of lifetime of dedicated storage utility-scale facilities.
    """
    return prosto_dedicated_capacity_stock() / prosto_dedicated_lifetime()


@component.add(
    name="PROSTO_dedicated_capacity_expansion",
    units="TW/Year",
    subscripts=["REGIONS_9_I", "PROSTO_ELEC_DEDICATED_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "prosto_dedicated_capacity_decomissioning": 2,
        "limited_capacity_expansion_prosto_dedicated": 2,
        "prosup_flexopt_elec_capacity_expansion": 2,
        "switch_nrg_proflex_capacity_expansion_endogenous": 1,
        "time": 2,
        "historic_capacity_expansion_stationary_bateries": 1,
    },
)
def prosto_dedicated_capacity_expansion():
    """
    Capacity expansion of dedicated storage utility-scale facilities.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "PROSTO_ELEC_DEDICATED_I": _subscript_dict["PROSTO_ELEC_DEDICATED_I"],
        },
        ["REGIONS_9_I", "PROSTO_ELEC_DEDICATED_I"],
    )
    value.loc[:, ["PROSTO_PHS"]] = (
        (
            prosto_dedicated_capacity_decomissioning()
            .loc[:, "PROSTO_PHS"]
            .reset_coords(drop=True)
            + if_then_else(
                switch_nrg_proflex_capacity_expansion_endogenous() == 0,
                lambda: limited_capacity_expansion_prosto_dedicated()
                .loc[:, "PROSTO_PHS"]
                .reset_coords(drop=True),
                lambda: prosup_flexopt_elec_capacity_expansion()
                .loc[:, "PROSTO_PHS"]
                .reset_coords(drop=True),
            )
        )
        .expand_dims({"NRG_PRO_I": ["PROSTO_PHS"]}, 1)
        .values
    )
    value.loc[:, ["PROSTO_STATIONARY_BATTERIES"]] = (
        if_then_else(
            time() < 2020,
            lambda: historic_capacity_expansion_stationary_bateries(time())
            .loc[:, "PROSTO_STATIONARY_BATTERIES"]
            .reset_coords(drop=True),
            lambda: prosto_dedicated_capacity_decomissioning()
            .loc[:, "PROSTO_STATIONARY_BATTERIES"]
            .reset_coords(drop=True)
            + np.minimum(
                limited_capacity_expansion_prosto_dedicated()
                .loc[:, "PROSTO_STATIONARY_BATTERIES"]
                .reset_coords(drop=True),
                prosup_flexopt_elec_capacity_expansion()
                .loc[:, "PROSTO_STATIONARY_BATTERIES"]
                .reset_coords(drop=True),
            ),
        )
        .expand_dims({"NRG_PRO_I": ["PROSTO_STATIONARY_BATTERIES"]}, 1)
        .values
    )
    return value


@component.add(
    name="PROSTO_dedicated_capacity_stock",
    units="TW",
    subscripts=["REGIONS_9_I", "PROSTO_ELEC_DEDICATED_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_prosto_dedicated_capacity_stock": 1},
    other_deps={
        "_integ_prosto_dedicated_capacity_stock": {
            "initial": {"initial_prosto_dedicated_capacity_stock": 1},
            "step": {
                "prosto_dedicated_capacity_expansion": 1,
                "prosto_dedicated_capacity_decomissioning": 1,
            },
        }
    },
)
def prosto_dedicated_capacity_stock():
    """
    Capacity stock of dedicated facilities to store energy at utility-scale level.
    """
    return _integ_prosto_dedicated_capacity_stock()


_integ_prosto_dedicated_capacity_stock = Integ(
    lambda: prosto_dedicated_capacity_expansion()
    - prosto_dedicated_capacity_decomissioning(),
    lambda: initial_prosto_dedicated_capacity_stock(),
    "_integ_prosto_dedicated_capacity_stock",
)


@component.add(
    name="PROSTO_DEDICATED_LIFETIME",
    units="Year",
    subscripts=["PROSTO_ELEC_DEDICATED_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_prosto_dedicated_lifetime"},
)
def prosto_dedicated_lifetime():
    """
    Lifetime of dedicated facilities to store energy at utility-scale level.
    """
    return _ext_constant_prosto_dedicated_lifetime()


_ext_constant_prosto_dedicated_lifetime = ExtConstant(
    "model_parameters/energy/energy-storage.xlsx",
    "Dedicated_capacities",
    "PROSTO_LIFETIME",
    {"PROSTO_ELEC_DEDICATED_I": _subscript_dict["PROSTO_ELEC_DEDICATED_I"]},
    _root,
    {"PROSTO_ELEC_DEDICATED_I": _subscript_dict["PROSTO_ELEC_DEDICATED_I"]},
    "_ext_constant_prosto_dedicated_lifetime",
)


@component.add(
    name="remaining_potential_capacity_by_PROSTO",
    units="DMNL",
    subscripts=["REGIONS_9_I", "PROSTO_ELEC_DEDICATED_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"maximum_prosto_dedicated": 2, "prosto_dedicated_capacity_stock": 1},
)
def remaining_potential_capacity_by_prosto():
    """
    Remaining potential taking into account scenario and techno-sustainable limits.
    """
    return zidz(
        maximum_prosto_dedicated() - prosto_dedicated_capacity_stock(),
        maximum_prosto_dedicated(),
    )


@component.add(
    name="STATIONARY_BATTERIES_MAXIMUM_SP",
    units="TW",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_stationary_batteries_maximum_sp"},
)
def stationary_batteries_maximum_sp():
    """
    Scenario-defined maximum capacity of stationary batteries.
    """
    return _ext_constant_stationary_batteries_maximum_sp()


_ext_constant_stationary_batteries_maximum_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "MAXIMUM_CAPACITY_STOCK_STATIONARY_BATTERIES*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_stationary_batteries_maximum_sp",
)
