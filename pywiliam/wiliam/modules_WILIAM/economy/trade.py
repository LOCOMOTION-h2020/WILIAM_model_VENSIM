"""
Module economy.trade
Translated using PySD version 3.10.0
"""


@component.add(
    name="delayed_TS_import_shares_final_demand",
    units="DMNL",
    subscripts=["REGIONS_35_I", "SECTORS_I", "FINAL_DEMAND_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_import_shares_final_demand": 1},
    other_deps={
        "_delayfixed_delayed_ts_import_shares_final_demand": {
            "initial": {
                "initial_delayed_import_shares_final_demand": 1,
                "time_step": 1,
            },
            "step": {
                "time": 1,
                "initial_delayed_import_shares_final_demand": 1,
                "import_shares_final_demand_constrained": 1,
            },
        }
    },
)
def delayed_ts_import_shares_final_demand():
    """
    Delayed import shares for final demand
    """
    return _delayfixed_delayed_ts_import_shares_final_demand()


_delayfixed_delayed_ts_import_shares_final_demand = DelayFixed(
    lambda: if_then_else(
        time() <= 2015,
        lambda: initial_delayed_import_shares_final_demand(),
        lambda: import_shares_final_demand_constrained(),
    ),
    lambda: time_step(),
    lambda: initial_delayed_import_shares_final_demand(),
    time_step,
    "_delayfixed_delayed_ts_import_shares_final_demand",
)


@component.add(
    name="delayed_TS_import_shares_intermediates",
    units="DMNL",
    subscripts=["REGIONS_35_I", "SECTORS_I", "SECTORS_MAP_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_import_shares_intermediates": 1},
    other_deps={
        "_delayfixed_delayed_ts_import_shares_intermediates": {
            "initial": {
                "initial_delayed_import_shares_intermediates": 1,
                "time_step": 1,
            },
            "step": {
                "time": 1,
                "initial_delayed_import_shares_intermediates": 1,
                "import_shares_intermediates_constrained": 1,
            },
        }
    },
)
def delayed_ts_import_shares_intermediates():
    """
    Delayed import shares for intermediates
    """
    return _delayfixed_delayed_ts_import_shares_intermediates()


_delayfixed_delayed_ts_import_shares_intermediates = DelayFixed(
    lambda: if_then_else(
        time() <= 2015,
        lambda: initial_delayed_import_shares_intermediates(),
        lambda: import_shares_intermediates_constrained(),
    ),
    lambda: time_step(),
    lambda: initial_delayed_import_shares_intermediates(),
    time_step,
    "_delayfixed_delayed_ts_import_shares_intermediates",
)


@component.add(
    name="import_shares_final_demand",
    units="DMNL",
    subscripts=["REGIONS_35_I", "SECTORS_I", "FINAL_DEMAND_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_fixed_import_shares": 1,
        "base_import_shares_final_demand": 2,
        "delayed_ts_price_ratio_households": 1,
        "epsilon_import_shares_final_demand": 1,
        "delayed_ts_import_shares_final_demand": 4,
        "beta_import_shares_final_demand": 1,
        "constant_import_shares_final_demand": 1,
    },
)
def import_shares_final_demand():
    """
    Import shares for final demand
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "SECTORS_I": _subscript_dict["SECTORS_I"],
            "FINAL_DEMAND_I": _subscript_dict["FINAL_DEMAND_I"],
        },
        ["REGIONS_35_I", "SECTORS_I", "FINAL_DEMAND_I"],
    )
    value.loc[:, :, ["CONSUMPTION_W"]] = (
        if_then_else(
            switch_fixed_import_shares() == 0,
            lambda: base_import_shares_final_demand()
            .loc[:, :, "CONSUMPTION_W"]
            .reset_coords(drop=True),
            lambda: np.minimum(
                1,
                np.maximum(
                    0,
                    if_then_else(
                        delayed_ts_import_shares_final_demand()
                        .loc[:, :, "CONSUMPTION_W"]
                        .reset_coords(drop=True)
                        == 1,
                        lambda: xr.DataArray(
                            1,
                            {
                                "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                                "SECTORS_I": _subscript_dict["SECTORS_I"],
                            },
                            ["REGIONS_35_I", "SECTORS_I"],
                        ),
                        lambda: if_then_else(
                            delayed_ts_import_shares_final_demand()
                            .loc[:, :, "CONSUMPTION_W"]
                            .reset_coords(drop=True)
                            == 0,
                            lambda: xr.DataArray(
                                0,
                                {
                                    "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                                    "SECTORS_I": _subscript_dict["SECTORS_I"],
                                },
                                ["REGIONS_35_I", "SECTORS_I"],
                            ),
                            lambda: (
                                1
                                - delayed_ts_import_shares_final_demand()
                                .loc[:, :, "CONSUMPTION_W"]
                                .reset_coords(drop=True)
                                + 1e-07
                            )
                            * np.exp(
                                constant_import_shares_final_demand()
                                .loc[:, :, "CONSUMPTION_W"]
                                .reset_coords(drop=True)
                                + (
                                    beta_import_shares_final_demand()
                                    .loc[:, "CONSUMPTION_W"]
                                    .reset_coords(drop=True)
                                    * np.log(
                                        delayed_ts_import_shares_final_demand()
                                        .loc[:, :, "CONSUMPTION_W"]
                                        .reset_coords(drop=True)
                                        + 1e-07
                                    ).transpose("SECTORS_I", "REGIONS_35_I")
                                ).transpose("REGIONS_35_I", "SECTORS_I")
                                + (
                                    epsilon_import_shares_final_demand()
                                    .loc[:, "CONSUMPTION_W"]
                                    .reset_coords(drop=True)
                                    * np.log(
                                        delayed_ts_price_ratio_households() + 1e-07
                                    ).transpose("SECTORS_I", "REGIONS_35_I")
                                ).transpose("REGIONS_35_I", "SECTORS_I")
                            ),
                        ),
                    ),
                ),
            ),
        )
        .expand_dims(
            {"FINAL_DEMAND_CONSUMPTION_INVESTMENT_GOVERNMENT_I": ["CONSUMPTION_W"]}, 2
        )
        .values
    )
    value.loc[:, :, _subscript_dict["FINAL_DEMAND_EXCEPT_HOUSEHOLDS"]] = (
        base_import_shares_final_demand()
        .loc[:, :, _subscript_dict["FINAL_DEMAND_EXCEPT_HOUSEHOLDS"]]
        .rename({"FINAL_DEMAND_I": "FINAL_DEMAND_EXCEPT_HOUSEHOLDS"})
        .values
    )
    return value


@component.add(
    name="import_shares_final_demand_constrained",
    units="DMNL",
    subscripts=["REGIONS_35_I", "SECTORS_I", "FINAL_DEMAND_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "import_shares_final_demand": 3,
        "delayed_ts_import_shares_final_demand": 4,
    },
)
def import_shares_final_demand_constrained():
    """
    Import shares by origin for final demand constrined: change in each time step limited to +- 5%
    """
    return if_then_else(
        zidz(import_shares_final_demand(), delayed_ts_import_shares_final_demand())
        > 1.05,
        lambda: delayed_ts_import_shares_final_demand(),
        lambda: if_then_else(
            zidz(import_shares_final_demand(), delayed_ts_import_shares_final_demand())
            < 0.95,
            lambda: delayed_ts_import_shares_final_demand(),
            lambda: import_shares_final_demand(),
        ),
    )


@component.add(
    name="import_shares_intermediates",
    units="DMNL",
    subscripts=["REGIONS_35_I", "SECTORS_I", "SECTORS_MAP_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_fixed_import_shares": 1,
        "base_import_shares_intermediates": 4,
        "beta_import_shares_intermediates": 1,
        "epsilon_import_shares_intermediates": 1,
        "constant_import_shares_intermediates": 1,
        "delayed_ts_import_shares_intermediates": 4,
        "delayed_ts_price_ratio_sectors": 1,
    },
)
def import_shares_intermediates():
    """
    Import shares for intermediates
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "SECTORS_I": _subscript_dict["SECTORS_I"],
            "SECTORS_MAP_I": _subscript_dict["SECTORS_MAP_I"],
        },
        ["REGIONS_35_I", "SECTORS_I", "SECTORS_MAP_I"],
    )
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[:, _subscript_dict["SECTORS_VARIABLE_IMPORT_SHARES_I"], :] = True
    except_subs.loc[
        ["MALTA"], _subscript_dict["SECTORS_VARIABLE_IMPORT_SHARES_I"], :
    ] = False
    except_subs.loc[
        ["CYPRUS"], _subscript_dict["SECTORS_VARIABLE_IMPORT_SHARES_I"], :
    ] = False
    value.values[except_subs.values] = if_then_else(
        switch_fixed_import_shares() == 1,
        lambda: base_import_shares_intermediates()
        .loc[:, _subscript_dict["SECTORS_VARIABLE_IMPORT_SHARES_I"]]
        .rename({"SECTORS_I": "SECTORS_VARIABLE_IMPORT_SHARES_I"})
        .expand_dims({"SECTORS_MAP_I": _subscript_dict["SECTORS_MAP_I"]}, 2),
        lambda: np.minimum(
            1,
            np.maximum(
                0,
                if_then_else(
                    delayed_ts_import_shares_intermediates()
                    .loc[:, _subscript_dict["SECTORS_VARIABLE_IMPORT_SHARES_I"], :]
                    .rename({"SECTORS_I": "SECTORS_VARIABLE_IMPORT_SHARES_I"})
                    == 1,
                    lambda: xr.DataArray(
                        1,
                        {
                            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                            "SECTORS_VARIABLE_IMPORT_SHARES_I": _subscript_dict[
                                "SECTORS_VARIABLE_IMPORT_SHARES_I"
                            ],
                            "SECTORS_MAP_I": _subscript_dict["SECTORS_MAP_I"],
                        },
                        [
                            "REGIONS_35_I",
                            "SECTORS_VARIABLE_IMPORT_SHARES_I",
                            "SECTORS_MAP_I",
                        ],
                    ),
                    lambda: if_then_else(
                        delayed_ts_import_shares_intermediates()
                        .loc[:, _subscript_dict["SECTORS_VARIABLE_IMPORT_SHARES_I"], :]
                        .rename({"SECTORS_I": "SECTORS_VARIABLE_IMPORT_SHARES_I"})
                        == 0,
                        lambda: xr.DataArray(
                            0,
                            {
                                "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                                "SECTORS_VARIABLE_IMPORT_SHARES_I": _subscript_dict[
                                    "SECTORS_VARIABLE_IMPORT_SHARES_I"
                                ],
                                "SECTORS_MAP_I": _subscript_dict["SECTORS_MAP_I"],
                            },
                            [
                                "REGIONS_35_I",
                                "SECTORS_VARIABLE_IMPORT_SHARES_I",
                                "SECTORS_MAP_I",
                            ],
                        ),
                        lambda: (
                            1
                            - delayed_ts_import_shares_intermediates()
                            .loc[
                                :,
                                _subscript_dict["SECTORS_VARIABLE_IMPORT_SHARES_I"],
                                :,
                            ]
                            .rename({"SECTORS_I": "SECTORS_VARIABLE_IMPORT_SHARES_I"})
                            + 1e-07
                        )
                        * np.exp(
                            constant_import_shares_intermediates()
                            .loc[
                                :,
                                _subscript_dict["SECTORS_VARIABLE_IMPORT_SHARES_I"],
                                :,
                            ]
                            .rename({"SECTORS_I": "SECTORS_VARIABLE_IMPORT_SHARES_I"})
                            + (
                                beta_import_shares_intermediates()
                                .loc[
                                    _subscript_dict["SECTORS_VARIABLE_IMPORT_SHARES_I"],
                                    :,
                                ]
                                .rename(
                                    {"SECTORS_I": "SECTORS_VARIABLE_IMPORT_SHARES_I"}
                                )
                                * np.log(
                                    1e-07
                                    + delayed_ts_import_shares_intermediates()
                                    .loc[
                                        :,
                                        _subscript_dict[
                                            "SECTORS_VARIABLE_IMPORT_SHARES_I"
                                        ],
                                        :,
                                    ]
                                    .rename(
                                        {
                                            "SECTORS_I": "SECTORS_VARIABLE_IMPORT_SHARES_I"
                                        }
                                    )
                                ).transpose(
                                    "SECTORS_VARIABLE_IMPORT_SHARES_I",
                                    "SECTORS_MAP_I",
                                    "REGIONS_35_I",
                                )
                            ).transpose(
                                "REGIONS_35_I",
                                "SECTORS_VARIABLE_IMPORT_SHARES_I",
                                "SECTORS_MAP_I",
                            )
                            + (
                                epsilon_import_shares_intermediates()
                                .loc[
                                    _subscript_dict["SECTORS_VARIABLE_IMPORT_SHARES_I"],
                                    :,
                                ]
                                .rename(
                                    {"SECTORS_I": "SECTORS_VARIABLE_IMPORT_SHARES_I"}
                                )
                                * np.log(
                                    1e-07
                                    + delayed_ts_price_ratio_sectors()
                                    .loc[
                                        :,
                                        _subscript_dict[
                                            "SECTORS_VARIABLE_IMPORT_SHARES_I"
                                        ],
                                        :,
                                    ]
                                    .rename(
                                        {
                                            "SECTORS_I": "SECTORS_VARIABLE_IMPORT_SHARES_I"
                                        }
                                    )
                                ).transpose(
                                    "SECTORS_VARIABLE_IMPORT_SHARES_I",
                                    "SECTORS_MAP_I",
                                    "REGIONS_35_I",
                                )
                            ).transpose(
                                "REGIONS_35_I",
                                "SECTORS_VARIABLE_IMPORT_SHARES_I",
                                "SECTORS_MAP_I",
                            )
                        ),
                    ),
                ),
            ),
        ),
    ).values[
        except_subs.loc[
            :, _subscript_dict["SECTORS_VARIABLE_IMPORT_SHARES_I"], :
        ].values
    ]
    value.loc[:, _subscript_dict["SECTORS_FIXED_IMPORT_SHARES_I"], :] = (
        base_import_shares_intermediates()
        .loc[:, _subscript_dict["SECTORS_FIXED_IMPORT_SHARES_I"], :]
        .rename({"SECTORS_I": "SECTORS_FIXED_IMPORT_SHARES_I"})
        .values
    )
    value.loc[["MALTA"], _subscript_dict["SECTORS_VARIABLE_IMPORT_SHARES_I"], :] = (
        base_import_shares_intermediates()
        .loc["MALTA", _subscript_dict["SECTORS_VARIABLE_IMPORT_SHARES_I"], :]
        .reset_coords(drop=True)
        .rename({"SECTORS_I": "SECTORS_VARIABLE_IMPORT_SHARES_I"})
        .expand_dims({"REGIONS_35_I": ["MALTA"]}, 0)
        .values
    )
    value.loc[["CYPRUS"], _subscript_dict["SECTORS_VARIABLE_IMPORT_SHARES_I"], :] = (
        base_import_shares_intermediates()
        .loc["CYPRUS", _subscript_dict["SECTORS_VARIABLE_IMPORT_SHARES_I"], :]
        .reset_coords(drop=True)
        .rename({"SECTORS_I": "SECTORS_VARIABLE_IMPORT_SHARES_I"})
        .expand_dims({"REGIONS_35_I": ["CYPRUS"]}, 0)
        .values
    )
    return value


@component.add(
    name="import_shares_intermediates_constrained",
    units="DMNL",
    subscripts=["REGIONS_35_I", "SECTORS_I", "SECTORS_MAP_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "import_shares_intermediates": 3,
        "delayed_ts_import_shares_intermediates": 4,
    },
)
def import_shares_intermediates_constrained():
    """
    Import shares by origin for intermediates constrined: change in each time step limited to +- 5%
    """
    return if_then_else(
        zidz(import_shares_intermediates(), delayed_ts_import_shares_intermediates())
        > 1.05,
        lambda: delayed_ts_import_shares_intermediates(),
        lambda: if_then_else(
            zidz(
                import_shares_intermediates(), delayed_ts_import_shares_intermediates()
            )
            < 0.95,
            lambda: delayed_ts_import_shares_intermediates(),
            lambda: import_shares_intermediates(),
        ),
    )


@component.add(
    name="import_shares_origin_final_demand",
    units="DMNL",
    subscripts=["REGIONS_35_MAP_I", "SECTORS_I", "REGIONS_35_I", "FINAL_DEMAND_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "base_import_shares_origin_final_demand": 1,
        "import_shares_origin_final_demand_except_households": 1,
    },
)
def import_shares_origin_final_demand():
    """
    Import shares by origin for final demand
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_35_MAP_I": _subscript_dict["REGIONS_35_MAP_I"],
            "SECTORS_I": _subscript_dict["SECTORS_I"],
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "FINAL_DEMAND_I": _subscript_dict["FINAL_DEMAND_I"],
        },
        ["REGIONS_35_MAP_I", "SECTORS_I", "REGIONS_35_I", "FINAL_DEMAND_I"],
    )
    value.loc[:, :, :, ["CONSUMPTION_W"]] = (
        base_import_shares_origin_final_demand()
        .loc[:, :, :, "CONSUMPTION_W"]
        .reset_coords(drop=True)
        .expand_dims(
            {"FINAL_DEMAND_CONSUMPTION_INVESTMENT_GOVERNMENT_I": ["CONSUMPTION_W"]}, 3
        )
        .values
    )
    value.loc[:, :, :, _subscript_dict["FINAL_DEMAND_EXCEPT_HOUSEHOLDS"]] = (
        import_shares_origin_final_demand_except_households()
        .loc[:, :, :, _subscript_dict["FINAL_DEMAND_EXCEPT_HOUSEHOLDS"]]
        .rename({"FINAL_DEMAND_I": "FINAL_DEMAND_EXCEPT_HOUSEHOLDS"})
        .values
    )
    return value


@component.add(
    name="import_shares_origin_intermediates",
    units="DMNL",
    subscripts=["REGIONS_35_MAP_I", "SECTORS_I", "REGIONS_35_I", "SECTORS_MAP_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"base_import_shares_origin_intermediates": 1},
)
def import_shares_origin_intermediates():
    """
    Import shares by origin for intermediates.
    """
    return base_import_shares_origin_intermediates()


@component.add(
    name="SWITCH_FIXED_IMPORT_SHARES", comp_type="Constant", comp_subtype="Normal"
)
def switch_fixed_import_shares():
    return 0


@component.add(
    name="total_exports_by_product",
    units="Mdollars/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_exports_real_by_product": 1, "price_output": 1},
)
def total_exports_by_product():
    """
    Total exports in real terms by product
    """
    return total_exports_real_by_product() * price_output()


@component.add(
    name="total_exports_real_by_product",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_intermediate_exports_real": 1, "final_exports_real": 1},
)
def total_exports_real_by_product():
    """
    Total exports in real terms by product
    """
    return total_intermediate_exports_real() + final_exports_real()


@component.add(
    name="total_imports_real_by_product",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "final_demand_imports_in_basic_prices_real": 1,
        "total_intermediate_imports_real": 1,
    },
)
def total_imports_real_by_product():
    """
    Total imports in real terms by product
    """
    return (
        sum(
            final_demand_imports_in_basic_prices_real().rename(
                {
                    "REGIONS_35_I": "REGIONS_35_I!",
                    "REGIONS_35_MAP_I": "REGIONS_35_I",
                    "FINAL_DEMAND_I": "FINAL_DEMAND_I!",
                }
            ),
            dim=["REGIONS_35_I!", "FINAL_DEMAND_I!"],
        )
        + total_intermediate_imports_real()
        .rename({"REGIONS_35_MAP_I": "REGIONS_35_I", "SECTORS_MAP_I": "SECTORS_I"})
        .transpose("SECTORS_I", "REGIONS_35_I")
    ).transpose("REGIONS_35_I", "SECTORS_I")


@component.add(
    name="trade_balance_real_by_product",
    units="Mdollars_2015/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_exports_real_by_product": 1, "total_imports_real_by_product": 1},
)
def trade_balance_real_by_product():
    """
    Trade balance in rela terms
    """
    return total_exports_real_by_product() - total_imports_real_by_product()
