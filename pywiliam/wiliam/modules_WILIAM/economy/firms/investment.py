"""
Module economy.firms.investment
Translated using PySD version 3.10.0
"""


@component.add(
    name="annual_change_capital_productivity_sp",
    units="DMNL/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "initial_year_capital_productivity_variation_sp": 1,
        "capital_productivity_variation_historic": 1,
        "capital_productivity_variation_sp": 1,
    },
)
def annual_change_capital_productivity_sp():
    """
    Annual change in capital productivity IF_THEN_ELSE(Time<INITIAL_YEAR_CAPITAL_PRODUCTIVITY_VARIATION_SP,CAPITAL_PRODUCTIVITY _VARIATION_HISTORIC[REGIONS_35_I,SECTORS_I], IF_THEN_ELSE(SIMPLIFIED_MODEL_CAPITAL_PRODUCTIVITY_VARIATION_SP=1:OR:SELECT_CAPITAL_P RODUCTIVITY_VARIATION_SP=1, CAPITAL_PRODUCTIVITY_VARIATION_1R_1S_SP, IF_THEN_ELSE(SELECT_CAPITAL_PRODUCTIVITY_VARIATION_SP=2, CAPITAL_PRODUCTIVITY_VARIATION_SP[REGIONS_35_I,SECTORS_I], CAPITAL_PRODUCTIVITY_VARIATION_HISTORIC[REGIONS_35_I,SECTORS_I])))
    """
    return if_then_else(
        time() < initial_year_capital_productivity_variation_sp(),
        lambda: capital_productivity_variation_historic(),
        lambda: capital_productivity_variation_sp(),
    )


@component.add(
    name="BASE_PRICE_GROSS_FIXED_CAPITAL_FORMATION",
    units="DMNL",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_base_price_gross_fixed_capital_formation"
    },
)
def base_price_gross_fixed_capital_formation():
    """
    Base price gross fixed capital formation.
    """
    return _ext_constant_base_price_gross_fixed_capital_formation()


_ext_constant_base_price_gross_fixed_capital_formation = ExtConstant(
    "model_parameters/economy/Investment_BASE.xlsx",
    "BASE_Price_GFCF",
    "BASE_PRICE_GROSS_FIXED_CAPITAL_FORMATION",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
    "_ext_constant_base_price_gross_fixed_capital_formation",
)


@component.add(
    name="capital_depreciation",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"real_capital_stock": 1, "depreciation_rate": 1},
)
def capital_depreciation():
    """
    Capital depreciation: decline in the value of the stock of capital. Note that the depreciation rate is annual, thus it is divided by the time step
    """
    return real_capital_stock() * depreciation_rate()


@component.add(
    name="capital_productivity",
    units="Mdollars_2015/Mdollars_2015",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_capital_productivity": 1},
    other_deps={
        "_integ_capital_productivity": {
            "initial": {"initial_delayed_capital_productivity": 1},
            "step": {"change_capital_productivity": 1},
        }
    },
)
def capital_productivity():
    """
    Capital productivity
    """
    return _integ_capital_productivity()


_integ_capital_productivity = Integ(
    lambda: change_capital_productivity(),
    lambda: initial_delayed_capital_productivity(),
    "_integ_capital_productivity",
)


@component.add(
    name="CAPITAL_PRODUCTIVITY_VARIATION_SP",
    units="1/Year/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_capital_productivity_variation_sp"},
)
def capital_productivity_variation_sp():
    return _ext_constant_capital_productivity_variation_sp()


_ext_constant_capital_productivity_variation_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "CAPITAL_PRODUCTIVITY_GROWTH_SP",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "SECTORS_I": _subscript_dict["SECTORS_I"],
    },
    "_ext_constant_capital_productivity_variation_sp",
)


@component.add(
    name="change_capital_productivity",
    units="Mdollars_2015/(Mdollars_2015*Year)",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"annual_change_capital_productivity_sp": 1, "capital_productivity": 1},
)
def change_capital_productivity():
    """
    Change capital productivity
    """
    return annual_change_capital_productivity_sp() * capital_productivity()


@component.add(
    name="climate_change_damage_on_capital_stock",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_climate_change_damage": 1,
        "switch_eco_climate_change_damage_capital": 1,
        "climate_change_incremental_damage_rate_to_capital_stock": 1,
        "climate_change_incremental_damage_rate_to_capital_stock_extrapolations_included": 1,
        "select_climate_change_impacts_sensitivity_sp": 1,
        "real_capital_stock": 1,
    },
)
def climate_change_damage_on_capital_stock():
    """
    Damages of the capital stock due to climate change.
    """
    return if_then_else(
        np.logical_or(
            switch_climate_change_damage() == 0,
            switch_eco_climate_change_damage_capital() == 0,
        ),
        lambda: xr.DataArray(
            0,
            {
                "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                "SECTORS_I": _subscript_dict["SECTORS_I"],
            },
            ["REGIONS_35_I", "SECTORS_I"],
        ),
        lambda: real_capital_stock()
        * if_then_else(
            select_climate_change_impacts_sensitivity_sp() == 0,
            lambda: climate_change_incremental_damage_rate_to_capital_stock(),
            lambda: climate_change_incremental_damage_rate_to_capital_stock_extrapolations_included(),
        ),
    )


@component.add(
    name="climate_change_incremental_damage_rate_to_capital_stock_extrapolations_included",
    units="DMNL",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"climate_change_incremental_damage_rate_to_capital_stock": 2},
)
def climate_change_incremental_damage_rate_to_capital_stock_extrapolations_included():
    """
    Climate change damage rate to capital stock adjusted to be 0 in 2015, since we assume that historical data already accounts for the implicit damage. This variable is defined to allow to include extrapolations.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "SECTORS_I": _subscript_dict["SECTORS_I"],
        },
        ["REGIONS_35_I", "SECTORS_I"],
    )
    value.loc[:, _subscript_dict["SECTORS_CLIMATE_CHANGE_IMPACTS_ORIGINAL"]] = (
        climate_change_incremental_damage_rate_to_capital_stock()
        .loc[:, _subscript_dict["SECTORS_CLIMATE_CHANGE_IMPACTS_ORIGINAL"]]
        .rename({"SECTORS_I": "SECTORS_CLIMATE_CHANGE_IMPACTS_ORIGINAL"})
        .values
    )
    value.loc[:, _subscript_dict["SECTORS_CLIMATE_CHANGE_IMPACTS_EXTRAPOLATED"]] = (
        climate_change_incremental_damage_rate_to_capital_stock()
        .loc[:, "OTHER_SERVICES"]
        .reset_coords(drop=True)
        .expand_dims(
            {
                "SECTORS_CLIMATE_CHANGE_IMPACTS_EXTRAPOLATED": _subscript_dict[
                    "SECTORS_CLIMATE_CHANGE_IMPACTS_EXTRAPOLATED"
                ]
            },
            1,
        )
        .values
    )
    return value


@component.add(
    name="consumption_fixed_capital",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_investment": 1,
        "base_price_gross_fixed_capital_formation": 1,
        "consumption_fixed_capital_real": 2,
        "price_transformation": 2,
        "price_gfcf": 1,
    },
)
def consumption_fixed_capital():
    """
    Consumption of fixed cpaital in nominal terms.
    """
    return if_then_else(
        switch_eco_investment() == 0,
        lambda: consumption_fixed_capital_real()
        * (base_price_gross_fixed_capital_formation() / price_transformation()),
        lambda: consumption_fixed_capital_real()
        * (
            price_gfcf().rename({"SECTORS_MAP_I": "SECTORS_I"}) / price_transformation()
        ),
    )


@component.add(
    name="consumption_fixed_capital_real",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"capital_depreciation": 1, "climate_change_damage_on_capital_stock": 1},
)
def consumption_fixed_capital_real():
    """
    Consumption of fixed capital in real terms.
    """
    return capital_depreciation() + climate_change_damage_on_capital_stock()


@component.add(
    name="desired_real_capital_stock",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Stateful",
    comp_subtype="Smooth",
    depends_on={"_smooth_desired_real_capital_stock": 1},
    other_deps={
        "_smooth_desired_real_capital_stock": {
            "initial": {"delayed_ts_output_real": 1, "capital_productivity": 1},
            "step": {"delayed_ts_output_real": 1, "capital_productivity": 1},
        }
    },
)
def desired_real_capital_stock():
    return _smooth_desired_real_capital_stock()


_smooth_desired_real_capital_stock = Smooth(
    lambda: zidz(delayed_ts_output_real(), capital_productivity()),
    lambda: xr.DataArray(
        3,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "SECTORS_I": _subscript_dict["SECTORS_I"],
        },
        ["REGIONS_35_I", "SECTORS_I"],
    ),
    lambda: zidz(delayed_ts_output_real(), capital_productivity()),
    lambda: 1,
    "_smooth_desired_real_capital_stock",
)


@component.add(
    name="gross_fixed_capital_formation_by_good",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_investment": 1,
        "price_transformation": 2,
        "gross_fixed_capital_formation_real": 2,
        "gross_fixed_capital_formation_structure": 2,
        "base_price_output": 1,
        "price_output": 1,
    },
)
def gross_fixed_capital_formation_by_good():
    """
    Gross fixed capital formation by type of investment good in purchasers prices and nominal terms.
    """
    return if_then_else(
        switch_eco_investment() == 0,
        lambda: sum(
            gross_fixed_capital_formation_real().rename({"SECTORS_I": "SECTORS_MAP_I!"})
            * gross_fixed_capital_formation_structure()
            .rename({"SECTORS_MAP_I": "SECTORS_MAP_I!"})
            .transpose("REGIONS_35_I", "SECTORS_MAP_I!", "SECTORS_I"),
            dim=["SECTORS_MAP_I!"],
        )
        * zidz(base_price_output(), price_transformation()),
        lambda: sum(
            gross_fixed_capital_formation_real().rename({"SECTORS_I": "SECTORS_MAP_I!"})
            * gross_fixed_capital_formation_structure()
            .rename({"SECTORS_MAP_I": "SECTORS_MAP_I!"})
            .transpose("REGIONS_35_I", "SECTORS_MAP_I!", "SECTORS_I"),
            dim=["SECTORS_MAP_I!"],
        )
        * zidz(price_output(), price_transformation()),
    )


@component.add(
    name="gross_fixed_capital_formation_real",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "desired_real_capital_stock": 3,
        "gross_fixed_capital_formation_to_desired_real_capital": 3,
        "private_gfcf_to_replace_climate_damage": 3,
        "switch_nrg2eco_investment_costs": 1,
        "switch_economy": 1,
        "delayed_ts_gfcf_protra_sectors_35r": 1,
        "switch_eco_investment": 1,
    },
)
def gross_fixed_capital_formation_real():
    """
    Gross fixed capital formation in real terms. desired_real_capital_stock[REGIONS_35_I,SECTORS_I]*GROSS_FIXED_CAPITAL_FORMATION_TO_D ESIRED_REAL_CAPITAL[REGIONS_35_I,SECTORS_I ]+climate_change_damage_on_capital_stock[REGIONS_35_I,SECTORS_I]
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "SECTORS_I": _subscript_dict["SECTORS_I"],
        },
        ["REGIONS_35_I", "SECTORS_I"],
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, _subscript_dict["SECTORS_ENERGY_I"]] = False
    except_subs.loc[:, ["REAL_ESTATE"]] = False
    value.values[except_subs.values] = (
        desired_real_capital_stock()
        * gross_fixed_capital_formation_to_desired_real_capital()
        + private_gfcf_to_replace_climate_damage()
    ).values[except_subs.values]
    value.loc[:, _subscript_dict["SECTORS_ENERGY_I"]] = if_then_else(
        np.logical_or(
            switch_economy() == 0,
            np.logical_or(
                switch_eco_investment() == 0, switch_nrg2eco_investment_costs() == 0
            ),
        ),
        lambda: desired_real_capital_stock()
        .loc[:, _subscript_dict["SECTORS_ENERGY_I"]]
        .rename({"SECTORS_I": "SECTORS_ENERGY_I"})
        * gross_fixed_capital_formation_to_desired_real_capital()
        .loc[:, _subscript_dict["SECTORS_ENERGY_I"]]
        .rename({"SECTORS_I": "SECTORS_ENERGY_I"})
        + private_gfcf_to_replace_climate_damage()
        .loc[:, _subscript_dict["SECTORS_ENERGY_I"]]
        .rename({"SECTORS_I": "SECTORS_ENERGY_I"}),
        lambda: delayed_ts_gfcf_protra_sectors_35r(),
    ).values
    value.loc[:, ["REAL_ESTATE"]] = (
        (
            desired_real_capital_stock().loc[:, "REAL_ESTATE"].reset_coords(drop=True)
            * gross_fixed_capital_formation_to_desired_real_capital()
            .loc[:, "REAL_ESTATE"]
            .reset_coords(drop=True)
            + private_gfcf_to_replace_climate_damage()
            .loc[:, "REAL_ESTATE"]
            .reset_coords(drop=True)
        )
        .expand_dims({"CLUSTER_CONSTRUCTION_REAL_ESTATE": ["REAL_ESTATE"]}, 1)
        .values
    )
    return value


@component.add(
    name="INITIAL_YEAR_CAPITAL_PRODUCTIVITY_VARIATION_SP",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_initial_year_capital_productivity_variation_sp"
    },
)
def initial_year_capital_productivity_variation_sp():
    return _ext_constant_initial_year_capital_productivity_variation_sp()


_ext_constant_initial_year_capital_productivity_variation_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "INITIAL_YEAR_CAPITAL_PRODUCTIVITY_VARIATION_SP",
    {},
    _root,
    {},
    "_ext_constant_initial_year_capital_productivity_variation_sp",
)


@component.add(
    name="private_GFCF_to_replace_climate_damage",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={"climate_change_damage_on_capital_stock": 1},
)
def private_gfcf_to_replace_climate_damage():
    """
    Gross fixed capital formation to replace cliamte damages
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "SECTORS_I": _subscript_dict["SECTORS_I"],
        },
        ["REGIONS_35_I", "SECTORS_I"],
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, ["PUBLIC_ADMINISTRATION"]] = False
    value.values[except_subs.values] = climate_change_damage_on_capital_stock().values[
        except_subs.values
    ]
    value.loc[:, ["PUBLIC_ADMINISTRATION"]] = 0
    return value


@component.add(
    name="public_GFCF_to_replace_climate_damage",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"climate_change_damage_on_capital_stock": 1},
)
def public_gfcf_to_replace_climate_damage():
    """
    Gross fixed capital formation to replace cliamte damages
    """
    return (
        climate_change_damage_on_capital_stock()
        .loc[:, "PUBLIC_ADMINISTRATION"]
        .reset_coords(drop=True)
    )


@component.add(
    name="real_capital_stock",
    units="Mdollars_2015",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_real_capital_stock": 1},
    other_deps={
        "_integ_real_capital_stock": {
            "initial": {"initial_capital_stock": 1},
            "step": {
                "time": 1,
                "climate_change_damage_on_capital_stock": 2,
                "gross_fixed_capital_formation_real": 1,
                "capital_depreciation": 1,
            },
        }
    },
)
def real_capital_stock():
    """
    Stock of capital in real terms.
    """
    return _integ_real_capital_stock()


_integ_real_capital_stock = Integ(
    lambda: if_then_else(
        time() <= 2015,
        lambda: -climate_change_damage_on_capital_stock(),
        lambda: gross_fixed_capital_formation_real()
        - climate_change_damage_on_capital_stock()
        - capital_depreciation(),
    ),
    lambda: initial_capital_stock(),
    "_integ_real_capital_stock",
)


@component.add(
    name="SELECT_CLIMATE_CHANGE_IMPACTS_SENSITIVITY_SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_select_climate_change_impacts_sensitivity_sp"
    },
)
def select_climate_change_impacts_sensitivity_sp():
    """
    0: Extrapolations are off to apply damages to all sectors. 1: Extrapolations are included to apply damages to all sectors.
    """
    return _ext_constant_select_climate_change_impacts_sensitivity_sp()


_ext_constant_select_climate_change_impacts_sensitivity_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "SELECT_CLIMATE_CHANGE_IMPACTS_SENSITIVITY_SP",
    {},
    _root,
    {},
    "_ext_constant_select_climate_change_impacts_sensitivity_sp",
)


@component.add(
    name="SWITCH_ECO_INVESTMENT",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_eco_investment"},
)
def switch_eco_investment():
    """
    This switch can take two values: 0: the (sub)module runs isolated from the rest of WILIAM, replacing inter(sub)module variables with exogenous parameters. 1: the (sub)module runs integrated with the rest of WILIAM.
    """
    return _ext_constant_switch_eco_investment()


_ext_constant_switch_eco_investment = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_ECO_INVESTMENT",
    {},
    _root,
    {},
    "_ext_constant_switch_eco_investment",
)


@component.add(
    name="SWITCH_NRG2ECO_INVESTMENT_COSTS",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_nrg2eco_investment_costs"},
)
def switch_nrg2eco_investment_costs():
    """
    This switch can take two values: 0: investment costs are computed for all sectors in the economy module. 1: the investment costs associated to energy sectors come from the energy module.
    """
    return _ext_constant_switch_nrg2eco_investment_costs()


_ext_constant_switch_nrg2eco_investment_costs = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_NRG2ECO_INVESTMENT_COSTS",
    {},
    _root,
    {},
    "_ext_constant_switch_nrg2eco_investment_costs",
)
