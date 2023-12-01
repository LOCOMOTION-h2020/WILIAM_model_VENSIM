"""
Module materials.lifecycle_medeas
Translated using PySD version 3.10.0
"""


@component.add(
    name="compare_RC_RR",
    units="DMNL",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"current_rc_rr_minerals": 1, "rc_rate_mineral": 1},
)
def compare_rc_rr():
    """
    comparison of the RC ratio of endogenous recycling and that set out by UNEP (2011)
    """
    return (
        -1
        + zidz(
            current_rc_rr_minerals().expand_dims(
                {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, 1
            ),
            rc_rate_mineral().transpose("MATERIALS_I", "REGIONS_9_I"),
        )
    ).transpose("REGIONS_9_I", "MATERIALS_I")


@component.add(
    name="decrease_remaining_mineral_reserves",
    units="Mt/Year",
    subscripts=["MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"mineral_mined_at": 1, "mineral_mined_re": 1},
)
def decrease_remaining_mineral_reserves():
    """
    decrease in mineral reserves due to mining
    """
    return sum(
        mineral_mined_at().rename({"REGIONS_9_I": "REGIONS_9_I!"})
        + mineral_mined_re().rename({"REGIONS_9_I": "REGIONS_9_I!"}),
        dim=["REGIONS_9_I!"],
    )


@component.add(
    name="decrease_remaining_mineral_resources",
    units="Mt/Year",
    subscripts=["MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"mineral_mined_at": 1, "mineral_mined_re": 1},
)
def decrease_remaining_mineral_resources():
    """
    decrease in mineral resources due to mining
    """
    return sum(
        mineral_mined_at().rename({"REGIONS_9_I": "REGIONS_9_I!"})
        + mineral_mined_re().rename({"REGIONS_9_I": "REGIONS_9_I!"}),
        dim=["REGIONS_9_I!"],
    )


@component.add(
    name="increase_remaining_mineral_reserves",
    units="Mt/Year",
    subscripts=["MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "demand_projection_materials_roe": 2,
        "one_year": 2,
        "mineral_recycled_re": 2,
        "total_materials_required_bu": 2,
        "mineral_recycled_at": 2,
        "over_recycling_at": 1,
        "mineral_mined_re": 1,
        "mineral_mined_at": 1,
        "over_recycling_re": 1,
    },
)
def increase_remaining_mineral_reserves():
    """
    increase in mineral reserves due to recycling
    """
    return if_then_else(
        sum(
            demand_projection_materials_roe().rename({"REGIONS_9_I": "REGIONS_9_I!"})
            / one_year(),
            dim=["REGIONS_9_I!"],
        )
        - sum(
            mineral_recycled_re().rename({"REGIONS_9_I": "REGIONS_9_I!"}),
            dim=["REGIONS_9_I!"],
        )
        > 0,
        lambda: if_then_else(
            sum(
                total_materials_required_bu().rename({"REGIONS_9_I": "REGIONS_9_I!"}),
                dim=["REGIONS_9_I!"],
            )
            - sum(
                mineral_recycled_at().rename({"REGIONS_9_I": "REGIONS_9_I!"}),
                dim=["REGIONS_9_I!"],
            )
            > 0,
            lambda: xr.DataArray(
                0, {"MATERIALS_I": _subscript_dict["MATERIALS_I"]}, ["MATERIALS_I"]
            ),
            lambda: sum(
                mineral_mined_re().rename({"REGIONS_9_I": "REGIONS_9_I!"}),
                dim=["REGIONS_9_I!"],
            )
            + sum(
                mineral_recycled_re().rename({"REGIONS_9_I": "REGIONS_9_I!"}),
                dim=["REGIONS_9_I!"],
            )
            + sum(
                over_recycling_at().rename({"REGIONS_9_I": "REGIONS_9_I!"}),
                dim=["REGIONS_9_I!"],
            )
            - sum(
                demand_projection_materials_roe().rename(
                    {"REGIONS_9_I": "REGIONS_9_I!"}
                )
                / one_year(),
                dim=["REGIONS_9_I!"],
            ),
        ),
        lambda: sum(
            mineral_mined_at().rename({"REGIONS_9_I": "REGIONS_9_I!"}),
            dim=["REGIONS_9_I!"],
        )
        + sum(
            mineral_recycled_at().rename({"REGIONS_9_I": "REGIONS_9_I!"}),
            dim=["REGIONS_9_I!"],
        )
        + sum(
            over_recycling_re().rename({"REGIONS_9_I": "REGIONS_9_I!"}),
            dim=["REGIONS_9_I!"],
        )
        - sum(
            total_materials_required_bu().rename({"REGIONS_9_I": "REGIONS_9_I!"}),
            dim=["REGIONS_9_I!"],
        ),
    )


@component.add(
    name="increase_remaining_mineral_resources",
    units="Mt/Year",
    subscripts=["MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "mineral_recycled_at": 2,
        "mineral_mined_at": 2,
        "mineral_recycled_re": 2,
        "mineral_mined_re": 2,
    },
)
def increase_remaining_mineral_resources():
    """
    increase in mineral resources due to recycling
    """
    return if_then_else(
        sum(
            mineral_recycled_at().rename({"REGIONS_9_I": "REGIONS_9_I!"}),
            dim=["REGIONS_9_I!"],
        )
        > sum(
            mineral_mined_at().rename({"REGIONS_9_I": "REGIONS_9_I!"}),
            dim=["REGIONS_9_I!"],
        ),
        lambda: sum(
            mineral_recycled_at().rename({"REGIONS_9_I": "REGIONS_9_I!"}),
            dim=["REGIONS_9_I!"],
        )
        - sum(
            mineral_mined_at().rename({"REGIONS_9_I": "REGIONS_9_I!"}),
            dim=["REGIONS_9_I!"],
        ),
        lambda: xr.DataArray(
            0, {"MATERIALS_I": _subscript_dict["MATERIALS_I"]}, ["MATERIALS_I"]
        ),
    ) + if_then_else(
        sum(
            mineral_recycled_re().rename({"REGIONS_9_I": "REGIONS_9_I!"}),
            dim=["REGIONS_9_I!"],
        )
        > sum(
            mineral_mined_re().rename({"REGIONS_9_I": "REGIONS_9_I!"}),
            dim=["REGIONS_9_I!"],
        ),
        lambda: sum(
            mineral_recycled_re().rename({"REGIONS_9_I": "REGIONS_9_I!"}),
            dim=["REGIONS_9_I!"],
        )
        - sum(
            mineral_mined_re().rename({"REGIONS_9_I": "REGIONS_9_I!"}),
            dim=["REGIONS_9_I!"],
        ),
        lambda: xr.DataArray(
            0, {"MATERIALS_I": _subscript_dict["MATERIALS_I"]}, ["MATERIALS_I"]
        ),
    )


@component.add(
    name="indicator_of_mineral_scarcity",
    units="DMNL",
    subscripts=["MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "remaining_minerals_reserves": 1,
        "mineral_recycled_re": 2,
        "remaining_mineral_resources": 2,
        "global_mineral_resources": 2,
        "global_mineral_reserves": 2,
        "mineral_recycled_at": 2,
    },
)
def indicator_of_mineral_scarcity():
    """
    Indicator of mineral scarcity;factor that varies its value from 0 ('not scarce') to 1 ('very scarce') depending on the remaining resources and reserves of each mineral and the amount of each mineral recycled.
    """
    return if_then_else(
        remaining_minerals_reserves() > 0,
        lambda: xr.DataArray(
            0, {"MATERIALS_I": _subscript_dict["MATERIALS_I"]}, ["MATERIALS_I"]
        ),
        lambda: if_then_else(
            remaining_mineral_resources() > 0,
            lambda: zidz(
                global_mineral_resources()
                - remaining_mineral_resources()
                - global_mineral_reserves(),
                (
                    global_mineral_resources()
                    + sum(
                        mineral_recycled_at().rename({"REGIONS_9_I": "REGIONS_9_I!"}),
                        dim=["REGIONS_9_I!"],
                    )
                    + sum(
                        mineral_recycled_re().rename({"REGIONS_9_I": "REGIONS_9_I!"}),
                        dim=["REGIONS_9_I!"],
                    )
                )
                - (
                    global_mineral_reserves()
                    + sum(
                        mineral_recycled_at().rename({"REGIONS_9_I": "REGIONS_9_I!"}),
                        dim=["REGIONS_9_I!"],
                    )
                    + sum(
                        mineral_recycled_re().rename({"REGIONS_9_I": "REGIONS_9_I!"}),
                        dim=["REGIONS_9_I!"],
                    )
                ),
            ),
            lambda: xr.DataArray(
                1, {"MATERIALS_I": _subscript_dict["MATERIALS_I"]}, ["MATERIALS_I"]
            ),
        ),
    )


@component.add(
    name="mineral_end_of_use_AT",
    units="Mt/Year",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "mineral_of_decom_batteries_9r": 1,
        "material_intensity_new_capacity_wind_onshore": 1,
        "protra_capacity_decommissioning": 4,
        "material_intensity_weighted_average_new_pv": 1,
        "material_intensity_new_capacity_wind_offshore": 1,
        "unit_conversion_mw_tw": 1,
        "unit_conversion_kg_mt": 1,
        "material_intensity_new_capacity_csp": 1,
    },
)
def mineral_end_of_use_at():
    """
    Mineral of the Alternative technologies dispositives end of use
    """
    return (
        mineral_of_decom_batteries_9r()
        + (
            sum(
                protra_capacity_decommissioning()
                .loc[:, :, "PROTRA_PP_solar_CSP"]
                .reset_coords(drop=True)
                .rename({"NRG_TO_I": "NRG_TO_I!"}),
                dim=["NRG_TO_I!"],
            )
            * material_intensity_new_capacity_csp()
            + sum(
                protra_capacity_decommissioning()
                .loc[:, :, "PROTRA_PP_solar_open_space_PV"]
                .reset_coords(drop=True)
                .rename({"NRG_TO_I": "NRG_TO_I!"}),
                dim=["NRG_TO_I!"],
            )
            * material_intensity_weighted_average_new_pv()
            .loc[:, :, "PROTRA_PP_solar_open_space_PV"]
            .reset_coords(drop=True)
            + sum(
                protra_capacity_decommissioning()
                .loc[:, :, "PROTRA_PP_wind_offshore"]
                .reset_coords(drop=True)
                .rename({"NRG_TO_I": "NRG_TO_I!"}),
                dim=["NRG_TO_I!"],
            )
            * material_intensity_new_capacity_wind_offshore()
            + sum(
                protra_capacity_decommissioning()
                .loc[:, :, "PROTRA_PP_wind_onshore"]
                .reset_coords(drop=True)
                .rename({"NRG_TO_I": "NRG_TO_I!"}),
                dim=["NRG_TO_I!"],
            )
            * material_intensity_new_capacity_wind_onshore()
        )
        * unit_conversion_mw_tw()
        / unit_conversion_kg_mt()
    )


@component.add(
    name="mineral_end_of_use_RE",
    units="Mt/Year",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "stock_mineral_re": 1,
        "average_residence_time_mineral_in_rest_of_the_economy": 1,
    },
)
def mineral_end_of_use_re():
    """
    decom materials of the Rest of the economy
    """
    return stock_mineral_re() / average_residence_time_mineral_in_rest_of_the_economy()


@component.add(
    name="mineral_mined_AT",
    units="Mt/Year",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "total_materials_required_bu": 2,
        "mineral_recycled_at": 2,
        "over_recycling_at": 2,
        "over_recycling_re": 2,
    },
)
def mineral_mined_at():
    """
    mineral mined demand of the Alternative technologies
    """
    return if_then_else(
        total_materials_required_bu()
        - mineral_recycled_at()
        - over_recycling_at()
        - over_recycling_re()
        > 0,
        lambda: total_materials_required_bu()
        - mineral_recycled_at()
        - over_recycling_at()
        - over_recycling_re(),
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
    name="mineral_mined_RE",
    units="Mt/Year",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "demand_projection_materials_roe": 2,
        "one_year": 2,
        "mineral_recycled_re": 2,
        "over_recycling_re": 2,
        "over_recycling_at": 2,
    },
)
def mineral_mined_re():
    """
    mineral mined for the mineral demand of the Rest of the economy
    """
    return if_then_else(
        demand_projection_materials_roe() / one_year()
        - mineral_recycled_re()
        - over_recycling_re()
        - over_recycling_at()
        > 0,
        lambda: demand_projection_materials_roe() / one_year()
        - mineral_recycled_re()
        - over_recycling_re()
        - over_recycling_at(),
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
    name="mineral_recycled_AT",
    units="Mt/Year",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "mineral_end_of_use_at": 1,
        "eol_recycling_rates_minerals_alt_techn": 1,
    },
)
def mineral_recycled_at():
    """
    mineral from decom Alternative technologies that can be recycled
    """
    return mineral_end_of_use_at() * eol_recycling_rates_minerals_alt_techn()


@component.add(
    name="mineral_recycled_RE",
    units="Mt/Year",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"mineral_end_of_use_re": 1, "eol_recycling_rates_minerals_rest": 1},
)
def mineral_recycled_re():
    """
    mineral recycled of the Rest of the economy
    """
    return mineral_end_of_use_re() * eol_recycling_rates_minerals_rest()


@component.add(
    name="mineral_supply_AT",
    units="Mt/Year",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "mineral_mined_at": 2,
        "mineral_recycled_at": 2,
        "over_recycling_re": 2,
        "total_materials_required_bu": 2,
    },
)
def mineral_supply_at():
    """
    total supply of minerals for Alternative technologies
    """
    return if_then_else(
        mineral_mined_at() + mineral_recycled_at() + over_recycling_re()
        > total_materials_required_bu(),
        lambda: total_materials_required_bu(),
        lambda: mineral_mined_at() + mineral_recycled_at() + over_recycling_re(),
    )


@component.add(
    name="mineral_supply_RE",
    units="Mt/Year",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "mineral_mined_re": 2,
        "mineral_recycled_re": 2,
        "over_recycling_at": 2,
        "demand_projection_materials_roe": 2,
        "one_year": 2,
    },
)
def mineral_supply_re():
    """
    mineral supply for the Rest of the economy
    """
    return if_then_else(
        mineral_mined_re() + mineral_recycled_re() + over_recycling_at()
        > demand_projection_materials_roe() / one_year(),
        lambda: demand_projection_materials_roe() / one_year(),
        lambda: mineral_mined_re() + mineral_recycled_re() + over_recycling_at(),
    )


@component.add(
    name='"MW/Battery"', units="MW/battery", comp_type="Constant", comp_subtype="Normal"
)
def mwbattery():
    """
    Unit change: standard battery has a 100kw of power
    """
    return 0.1


@component.add(
    name="over_recycling_AT",
    units="Mt/Year",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"mineral_recycled_at": 2, "total_materials_required_bu": 2},
)
def over_recycling_at():
    """
    Mt of minerals used in alternative technologies for which the amount recycled is greater than the amount demanded by the alternative technologies.
    """
    return if_then_else(
        mineral_recycled_at() > total_materials_required_bu(),
        lambda: mineral_recycled_at() - total_materials_required_bu(),
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
    name="over_recycling_RE",
    units="Mt/Year",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "mineral_recycled_re": 2,
        "demand_projection_materials_roe": 2,
        "one_year": 2,
    },
)
def over_recycling_re():
    """
    Mt of minerals used in the rest of economy for which the amount recycled is greater than the amount demanded by the rest of the economy.
    """
    return if_then_else(
        mineral_recycled_re() > demand_projection_materials_roe() / one_year(),
        lambda: mineral_recycled_re() - demand_projection_materials_roe() / one_year(),
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
    name="RC_rate_mineral",
    units="DMNL",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_recycled_mineral": 2, "total_demand_mineral": 2},
)
def rc_rate_mineral():
    """
    Recycled content rate of the all materials
    """
    return if_then_else(
        zidz(total_recycled_mineral(), total_demand_mineral()) > 1,
        lambda: xr.DataArray(
            1,
            {
                "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                "MATERIALS_I": _subscript_dict["MATERIALS_I"],
            },
            ["REGIONS_9_I", "MATERIALS_I"],
        ),
        lambda: zidz(total_recycled_mineral(), total_demand_mineral()),
    )


@component.add(
    name="remaining_mineral_resources",
    units="Mt",
    subscripts=["MATERIALS_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_remaining_mineral_resources": 1},
    other_deps={
        "_integ_remaining_mineral_resources": {
            "initial": {"global_mineral_resources": 1},
            "step": {
                "increase_remaining_mineral_resources": 1,
                "decrease_remaining_mineral_resources": 1,
            },
        }
    },
)
def remaining_mineral_resources():
    """
    Remaining mineral resources at each point in the simulation
    """
    return _integ_remaining_mineral_resources()


_integ_remaining_mineral_resources = Integ(
    lambda: increase_remaining_mineral_resources()
    - decrease_remaining_mineral_resources(),
    lambda: global_mineral_resources(),
    "_integ_remaining_mineral_resources",
)


@component.add(
    name="remaining_minerals_reserves",
    units="Mt",
    subscripts=["MATERIALS_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_remaining_minerals_reserves": 1},
    other_deps={
        "_integ_remaining_minerals_reserves": {
            "initial": {"global_mineral_reserves": 1},
            "step": {
                "increase_remaining_mineral_reserves": 1,
                "decrease_remaining_mineral_reserves": 1,
            },
        }
    },
)
def remaining_minerals_reserves():
    """
    Remaining mineral reserves at each point in the simulation
    """
    return _integ_remaining_minerals_reserves()


_integ_remaining_minerals_reserves = Integ(
    lambda: increase_remaining_mineral_reserves()
    - decrease_remaining_mineral_reserves(),
    lambda: global_mineral_reserves(),
    "_integ_remaining_minerals_reserves",
)


@component.add(
    name="stock_mineral_RE",
    units="Mt",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_stock_mineral_re": 1},
    other_deps={
        "_integ_stock_mineral_re": {
            "initial": {"initial_stock_mineral_rest_of_the_economy": 1},
            "step": {"mineral_supply_re": 1, "mineral_end_of_use_re": 1},
        }
    },
)
def stock_mineral_re():
    """
    stock of minerals in the Rest of the economy
    """
    return _integ_stock_mineral_re()


_integ_stock_mineral_re = Integ(
    lambda: mineral_supply_re() - mineral_end_of_use_re(),
    lambda: initial_stock_mineral_rest_of_the_economy().expand_dims(
        {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, 0
    ),
    "_integ_stock_mineral_re",
)


@component.add(
    name="total_demand_mineral",
    units="Mt/Year",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "total_materials_required_bu": 1,
        "demand_projection_materials_roe": 1,
        "one_year": 1,
    },
)
def total_demand_mineral():
    """
    Total demand of mineral
    """
    return (
        total_materials_required_bu() + demand_projection_materials_roe() / one_year()
    )


@component.add(
    name="total_mineral_mined",
    units="Mt/Year",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"mineral_mined_at": 1, "mineral_mined_re": 1},
)
def total_mineral_mined():
    """
    Total mineral mined (AT+RE)
    """
    return mineral_mined_at() + mineral_mined_re()


@component.add(
    name="total_mineral_supply",
    units="Mt/Year",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"mineral_supply_at": 1, "mineral_supply_re": 1},
)
def total_mineral_supply():
    """
    Total mineral supply (AT+RE)
    """
    return mineral_supply_at() + mineral_supply_re()


@component.add(
    name="total_recycled_mineral",
    units="Mt/Year",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"mineral_recycled_at": 1, "mineral_recycled_re": 1},
)
def total_recycled_mineral():
    """
    total recycled mineral
    """
    return mineral_recycled_at() + mineral_recycled_re()
