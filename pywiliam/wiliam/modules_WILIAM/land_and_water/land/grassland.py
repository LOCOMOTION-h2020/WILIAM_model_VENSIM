"""
Module land_and_water.land.grassland
Translated using PySD version 3.10.0
"""


@component.add(
    name="carbon_capture_due_to_change_to_regenerative_grasslands",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "share_of_grasslands_under_inmature_regenerative_management": 1,
        "land_use_area_by_region": 1,
        "factor_of_carbon_capture_of_regenerative_grasslands": 1,
        "factor_of_carbon_capture_of_grasslands": 1,
    },
)
def carbon_capture_due_to_change_to_regenerative_grasslands():
    return (
        share_of_grasslands_under_inmature_regenerative_management()
        * land_use_area_by_region().loc[:, "GRASSLAND"].reset_coords(drop=True)
        * (
            factor_of_carbon_capture_of_regenerative_grasslands()
            - factor_of_carbon_capture_of_grasslands()
        )
        * 0
    )


@component.add(
    name="factor_of_grassland_production",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "factor_of_gain_of_regenerative_grazing": 1,
        "share_of_grasslands_under_mature_regenerative_management": 1,
        "share_of_grasslands_under_inmature_regenerative_management": 1,
    },
)
def factor_of_grassland_production():
    return 1 + factor_of_gain_of_regenerative_grazing() * (
        share_of_grasslands_under_inmature_regenerative_management()
        + share_of_grasslands_under_mature_regenerative_management()
    )


@component.add(
    name="increase_of_share_of_mature_regenerative_grasslands",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "share_of_grasslands_under_inmature_regenerative_management": 1,
        "saturation_time_of_regenerative_grasslands": 1,
    },
)
def increase_of_share_of_mature_regenerative_grasslands():
    return share_of_grasslands_under_inmature_regenerative_management() * (
        1 / saturation_time_of_regenerative_grasslands()
    )


@component.add(
    name="increase_of_share_of_regenerative_grasslands",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "share_of_grasslands_under_inmature_regenerative_management": 1,
        "share_of_grasslands_under_mature_regenerative_management": 1,
        "soil_management_in_grasslands_sp": 1,
    },
)
def increase_of_share_of_regenerative_grasslands():
    return if_then_else(
        share_of_grasslands_under_inmature_regenerative_management()
        + share_of_grasslands_under_mature_regenerative_management()
        < 1,
        lambda: soil_management_in_grasslands_sp(),
        lambda: xr.DataArray(
            0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
        ),
    )


@component.add(
    name="share_of_grasslands_under_inmature_regenerative_management",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_share_of_grasslands_under_inmature_regenerative_management": 1},
    other_deps={
        "_integ_share_of_grasslands_under_inmature_regenerative_management": {
            "initial": {},
            "step": {
                "increase_of_share_of_regenerative_grasslands": 1,
                "increase_of_share_of_mature_regenerative_grasslands": 1,
            },
        }
    },
)
def share_of_grasslands_under_inmature_regenerative_management():
    return _integ_share_of_grasslands_under_inmature_regenerative_management()


_integ_share_of_grasslands_under_inmature_regenerative_management = Integ(
    lambda: increase_of_share_of_regenerative_grasslands()
    - increase_of_share_of_mature_regenerative_grasslands(),
    lambda: xr.DataArray(
        0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
    ),
    "_integ_share_of_grasslands_under_inmature_regenerative_management",
)


@component.add(
    name="share_of_grasslands_under_mature_regenerative_management",
    subscripts=["REGIONS_9_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_share_of_grasslands_under_mature_regenerative_management": 1},
    other_deps={
        "_integ_share_of_grasslands_under_mature_regenerative_management": {
            "initial": {},
            "step": {"increase_of_share_of_mature_regenerative_grasslands": 1},
        }
    },
)
def share_of_grasslands_under_mature_regenerative_management():
    return _integ_share_of_grasslands_under_mature_regenerative_management()


_integ_share_of_grasslands_under_mature_regenerative_management = Integ(
    lambda: increase_of_share_of_mature_regenerative_grasslands(),
    lambda: xr.DataArray(
        0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
    ),
    "_integ_share_of_grasslands_under_mature_regenerative_management",
)


@component.add(
    name="share_of_grasslands_under_regenerative_grasslands",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "share_of_grasslands_under_mature_regenerative_management": 1,
        "share_of_grasslands_under_inmature_regenerative_management": 1,
    },
)
def share_of_grasslands_under_regenerative_grasslands():
    return (
        share_of_grasslands_under_mature_regenerative_management()
        + share_of_grasslands_under_inmature_regenerative_management()
    )


@component.add(
    name="soil_management_in_grasslands_sp",
    units="1/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_soil_management_in_grasslands_sp": 1,
        "time": 2,
        "year_initial_soil_management_in_grasslands_sp": 2,
        "year_final_soil_management_in_grasslands_sp": 2,
        "objective_soil_management_in_grasslands_sp": 1,
    },
)
def soil_management_in_grasslands_sp():
    return if_then_else(
        np.logical_and(
            switch_soil_management_in_grasslands_sp() == 1,
            np.logical_and(
                time() > year_initial_soil_management_in_grasslands_sp(),
                time() < year_final_soil_management_in_grasslands_sp(),
            ),
        ),
        lambda: objective_soil_management_in_grasslands_sp()
        / (
            year_final_soil_management_in_grasslands_sp()
            - year_initial_soil_management_in_grasslands_sp()
        ),
        lambda: xr.DataArray(
            0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
        ),
    )
