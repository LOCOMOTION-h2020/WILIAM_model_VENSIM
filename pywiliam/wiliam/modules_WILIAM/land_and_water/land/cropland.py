"""
Module land_and_water.land.cropland
Translated using PySD version 3.10.0
"""


@component.add(
    name="area_of_crops_all_managements",
    units="km2",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "land_use_area_by_region": 2,
        "shares_of_crops_all_managements": 1,
        "land_area_adjust_coefficient": 1,
    },
)
def area_of_crops_all_managements():
    return (
        (
            land_use_area_by_region().loc[:, "CROPLAND_RAINFED"].reset_coords(drop=True)
            + land_use_area_by_region()
            .loc[:, "CROPLAND_IRRIGATED"]
            .reset_coords(drop=True)
        )
        * shares_of_crops_all_managements()
        * land_area_adjust_coefficient()
    )


@component.add(
    name="area_of_irrigated_crops",
    units="km2",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "land_use_area_by_region": 1,
        "shares_of_irrigated_crops": 1,
        "land_area_adjust_coefficient": 1,
    },
)
def area_of_irrigated_crops():
    """
    irrigated crops area by region and AEZ
    """
    return (
        land_use_area_by_region().loc[:, "CROPLAND_IRRIGATED"].reset_coords(drop=True)
        * shares_of_irrigated_crops()
        * land_area_adjust_coefficient()
    )


@component.add(
    name="area_of_rainfed_crops",
    units="km2",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "land_use_area_by_region": 1,
        "shares_of_rainfed_crops": 1,
        "land_area_adjust_coefficient": 1,
    },
)
def area_of_rainfed_crops():
    """
    rainfed crops area by region and AEZ
    """
    return (
        land_use_area_by_region().loc[:, "CROPLAND_RAINFED"].reset_coords(drop=True)
        * shares_of_rainfed_crops()
        * land_area_adjust_coefficient()
    )


@component.add(
    name="aux_shortage_crops",
    units="DMNL",
    subscripts=["LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ratio_shortage_of_crops": 1},
)
def aux_shortage_crops():
    return np.maximum(ratio_shortage_of_crops(), 1) - 1


@component.add(
    name="availability_of_crops",
    units="DMNL",
    subscripts=["LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "time_historical_data_land_module": 1,
        "mask_crops": 2,
        "land_products_available_all_regions": 2,
        "land_products_demanded_world": 4,
    },
)
def availability_of_crops():
    """
    if it is greater than 0 excess of crops production, lower than zero, shortage
    """
    return if_then_else(
        time() < time_historical_data_land_module(),
        lambda: mask_crops()
        * zidz(
            land_products_available_all_regions() - land_products_demanded_world(),
            land_products_demanded_world(),
        ),
        lambda: mask_crops()
        * zidz(
            land_products_available_all_regions() - land_products_demanded_world(),
            land_products_demanded_world(),
        ),
    )


@component.add(
    name="crops_available_all_managements",
    units="t/Year",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "area_of_crops_all_managements": 1,
        "yields_of_crops_all_managements": 1,
    },
)
def crops_available_all_managements():
    return area_of_crops_all_managements() * yields_of_crops_all_managements()


@component.add(
    name="factor_maximum_irrigated",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"shares_of_irrigated_crops": 1, "maximum_irrigated_crops_shares": 1},
)
def factor_maximum_irrigated():
    return if_then_else(
        shares_of_irrigated_crops() < maximum_irrigated_crops_shares(),
        lambda: xr.DataArray(
            1,
            {
                "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
            },
            ["REGIONS_9_I", "LAND_PRODUCTS_I"],
        ),
        lambda: xr.DataArray(
            0,
            {
                "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
            },
            ["REGIONS_9_I", "LAND_PRODUCTS_I"],
        ),
    )


@component.add(
    name="factor_maximum_rainfed_crops",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"shares_of_rainfed_crops": 1, "maximum_rainfed_crops_shares": 1},
)
def factor_maximum_rainfed_crops():
    return if_then_else(
        shares_of_rainfed_crops() < maximum_rainfed_crops_shares(),
        lambda: xr.DataArray(
            1,
            {
                "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
            },
            ["REGIONS_9_I", "LAND_PRODUCTS_I"],
        ),
        lambda: xr.DataArray(
            0,
            {
                "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
            },
            ["REGIONS_9_I", "LAND_PRODUCTS_I"],
        ),
    )


@component.add(
    name="factor_minimum_irrigated",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"shares_of_irrigated_crops": 1},
)
def factor_minimum_irrigated():
    return if_then_else(
        shares_of_irrigated_crops() > 0,
        lambda: xr.DataArray(
            1,
            {
                "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
            },
            ["REGIONS_9_I", "LAND_PRODUCTS_I"],
        ),
        lambda: xr.DataArray(
            0,
            {
                "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
            },
            ["REGIONS_9_I", "LAND_PRODUCTS_I"],
        ),
    )


@component.add(
    name="factor_minimum_rainfed",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"shares_of_rainfed_crops": 1},
)
def factor_minimum_rainfed():
    return if_then_else(
        shares_of_rainfed_crops() > 0,
        lambda: xr.DataArray(
            1,
            {
                "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
            },
            ["REGIONS_9_I", "LAND_PRODUCTS_I"],
        ),
        lambda: xr.DataArray(
            0,
            {
                "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
            },
            ["REGIONS_9_I", "LAND_PRODUCTS_I"],
        ),
    )


@component.add(
    name="factor_of_maximum_crops",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"shares_of_crops_all_managements": 1, "maximum_crop_shares": 1},
)
def factor_of_maximum_crops():
    return if_then_else(
        shares_of_crops_all_managements() < maximum_crop_shares(),
        lambda: xr.DataArray(
            1,
            {
                "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
            },
            ["REGIONS_9_I", "LAND_PRODUCTS_I"],
        ),
        lambda: xr.DataArray(
            0,
            {
                "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
            },
            ["REGIONS_9_I", "LAND_PRODUCTS_I"],
        ),
    )


@component.add(
    name="factor_of_minimum_crops",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"shares_of_crops_all_managements": 1},
)
def factor_of_minimum_crops():
    return if_then_else(
        shares_of_crops_all_managements() > 0,
        lambda: xr.DataArray(
            1,
            {
                "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
            },
            ["REGIONS_9_I", "LAND_PRODUCTS_I"],
        ),
        lambda: xr.DataArray(
            0,
            {
                "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
            },
            ["REGIONS_9_I", "LAND_PRODUCTS_I"],
        ),
    )


@component.add(
    name="global_availability_of_crops",
    units="DMNL",
    comp_type="Stateful",
    comp_subtype="Smooth",
    depends_on={
        "time": 1,
        "time_historical_data_land_module": 1,
        "_smooth_global_availability_of_crops": 1,
        "availability_of_crops": 1,
    },
    other_deps={
        "_smooth_global_availability_of_crops": {
            "initial": {"availability_of_crops": 1},
            "step": {"availability_of_crops": 1},
        }
    },
)
def global_availability_of_crops():
    """
    if it is greater than 0 excess of crops production
    """
    return if_then_else(
        time() <= time_historical_data_land_module(),
        lambda: _smooth_global_availability_of_crops(),
        lambda: sum(
            availability_of_crops().rename({"LAND_PRODUCTS_I": "LAND_PRODUCTS_I!"}),
            dim=["LAND_PRODUCTS_I!"],
        )
        / len(
            xr.DataArray(
                np.arange(1, len(_subscript_dict["LAND_PRODUCTS_I"]) + 1),
                {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"]},
                ["LAND_PRODUCTS_I"],
            )
        ),
    )


_smooth_global_availability_of_crops = Smooth(
    lambda: sum(
        availability_of_crops().rename({"LAND_PRODUCTS_I": "LAND_PRODUCTS_I!"}),
        dim=["LAND_PRODUCTS_I!"],
    )
    / len(
        xr.DataArray(
            np.arange(1, len(_subscript_dict["LAND_PRODUCTS_I"]) + 1),
            {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"]},
            ["LAND_PRODUCTS_I"],
        )
    ),
    lambda: 5,
    lambda: sum(
        availability_of_crops().rename({"LAND_PRODUCTS_I": "LAND_PRODUCTS_I!"}),
        dim=["LAND_PRODUCTS_I!"],
    )
    / len(
        xr.DataArray(
            np.arange(1, len(_subscript_dict["LAND_PRODUCTS_I"]) + 1),
            {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"]},
            ["LAND_PRODUCTS_I"],
        )
    ),
    lambda: 1,
    "_smooth_global_availability_of_crops",
)


@component.add(
    name="global_shortage_of_crops",
    comp_type="Stateful",
    comp_subtype="Smooth",
    depends_on={"_smooth_global_shortage_of_crops": 1},
    other_deps={
        "_smooth_global_shortage_of_crops": {
            "initial": {"shortage_of_crops": 1},
            "step": {"shortage_of_crops": 1},
        }
    },
)
def global_shortage_of_crops():
    return _smooth_global_shortage_of_crops()


_smooth_global_shortage_of_crops = Smooth(
    lambda: sum(
        shortage_of_crops().rename({"LAND_PRODUCTS_I": "LAND_PRODUCTS_I!"}),
        dim=["LAND_PRODUCTS_I!"],
    )
    / (
        len(
            xr.DataArray(
                np.arange(1, len(_subscript_dict["LAND_PRODUCTS_I"]) + 1),
                {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"]},
                ["LAND_PRODUCTS_I"],
            )
        )
        - 4
    ),
    lambda: 4,
    lambda: sum(
        shortage_of_crops().rename({"LAND_PRODUCTS_I": "LAND_PRODUCTS_I!"}),
        dim=["LAND_PRODUCTS_I!"],
    )
    / (
        len(
            xr.DataArray(
                np.arange(1, len(_subscript_dict["LAND_PRODUCTS_I"]) + 1),
                {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"]},
                ["LAND_PRODUCTS_I"],
            )
        )
        - 4
    ),
    lambda: 1,
    "_smooth_global_shortage_of_crops",
)


@component.add(
    name="historical_area_of_crops_all_managements",
    units="km2",
    subscripts=["LAND_PRODUCTS_I", "REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "historical_shares_of_crops_all_management": 1,
        "land_use_area_by_region": 2,
        "land_area_adjust_coefficient": 1,
    },
)
def historical_area_of_crops_all_managements():
    return (
        historical_shares_of_crops_all_management(time())
        * (
            land_use_area_by_region().loc[:, "CROPLAND_RAINFED"].reset_coords(drop=True)
            + land_use_area_by_region()
            .loc[:, "CROPLAND_IRRIGATED"]
            .reset_coords(drop=True)
        )
        * land_area_adjust_coefficient()
    )


@component.add(
    name="historical_area_of_irrigated_crops",
    units="km2",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "historical_area_of_crops_all_management": 1,
        "share_of_irrigation_per_crop": 1,
    },
)
def historical_area_of_irrigated_crops():
    return (
        historical_area_of_crops_all_management(time())
        * share_of_irrigation_per_crop().transpose("LAND_PRODUCTS_I", "REGIONS_9_I")
    ).transpose("REGIONS_9_I", "LAND_PRODUCTS_I")


@component.add(
    name="historical_area_of_rainfed_crops",
    units="km2",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "historical_area_of_crops_all_management": 1,
        "share_of_irrigation_per_crop": 1,
    },
)
def historical_area_of_rainfed_crops():
    return (
        historical_area_of_crops_all_management(time())
        * (1 - share_of_irrigation_per_crop()).transpose(
            "LAND_PRODUCTS_I", "REGIONS_9_I"
        )
    ).transpose("REGIONS_9_I", "LAND_PRODUCTS_I")


@component.add(
    name="historical_change_of_shares_of_irrigated_crops",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "historical_share_of_irrigated_crops": 1,
        "historical_shares_irrigated_delayed": 1,
    },
)
def historical_change_of_shares_of_irrigated_crops():
    return historical_share_of_irrigated_crops() - historical_shares_irrigated_delayed()


@component.add(
    name="historical_change_of_shares_rainfed_crops",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "historical_share_of_rainfed_crops": 1,
        "historical_shares_rainfed_delayed": 1,
    },
)
def historical_change_of_shares_rainfed_crops():
    return historical_share_of_rainfed_crops() - historical_shares_rainfed_delayed()


@component.add(
    name="historical_increase_of_shares_of_crops_all_managements",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "historical_shares_of_crops_all_management": 1,
        "historical_shares_of_crops_delayed_all_managements": 1,
    },
)
def historical_increase_of_shares_of_crops_all_managements():
    return (
        historical_shares_of_crops_all_management(time())
        - historical_shares_of_crops_delayed_all_managements().transpose(
            "LAND_PRODUCTS_I", "REGIONS_9_I"
        )
    ).transpose("REGIONS_9_I", "LAND_PRODUCTS_I")


@component.add(
    name="historical_share_of_irrigated_crops",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"historical_area_of_irrigated_crops": 2},
)
def historical_share_of_irrigated_crops():
    return zidz(
        historical_area_of_irrigated_crops(),
        sum(
            historical_area_of_irrigated_crops().rename(
                {"LAND_PRODUCTS_I": "LAND_PRODUCTS_I!"}
            ),
            dim=["LAND_PRODUCTS_I!"],
        ).expand_dims({"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"]}, 1),
    )


@component.add(
    name="historical_share_of_rainfed_crops",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"historical_area_of_rainfed_crops": 2},
)
def historical_share_of_rainfed_crops():
    return zidz(
        historical_area_of_rainfed_crops(),
        sum(
            historical_area_of_rainfed_crops().rename(
                {"LAND_PRODUCTS_I": "LAND_PRODUCTS_I!"}
            ),
            dim=["LAND_PRODUCTS_I!"],
        ).expand_dims({"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"]}, 1),
    )


@component.add(
    name="historical_shares_irrigated_delayed",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_historical_shares_irrigated_delayed": 1},
    other_deps={
        "_delayfixed_historical_shares_irrigated_delayed": {
            "initial": {"initial_shares_of_irrigated_crops": 1},
            "step": {"historical_share_of_irrigated_crops": 1},
        }
    },
)
def historical_shares_irrigated_delayed():
    return _delayfixed_historical_shares_irrigated_delayed()


_delayfixed_historical_shares_irrigated_delayed = DelayFixed(
    lambda: historical_share_of_irrigated_crops(),
    lambda: 1,
    lambda: initial_shares_of_irrigated_crops(),
    time_step,
    "_delayfixed_historical_shares_irrigated_delayed",
)


@component.add(
    name="historical_shares_of_crops_delayed_all_managements",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_historical_shares_of_crops_delayed_all_managements": 1},
    other_deps={
        "_delayfixed_historical_shares_of_crops_delayed_all_managements": {
            "initial": {"initial_shares_of_crops_all_managements": 1},
            "step": {"time": 1, "historical_shares_of_crops_all_management": 1},
        }
    },
)
def historical_shares_of_crops_delayed_all_managements():
    return _delayfixed_historical_shares_of_crops_delayed_all_managements()


_delayfixed_historical_shares_of_crops_delayed_all_managements = DelayFixed(
    lambda: historical_shares_of_crops_all_management(time()).transpose(
        "REGIONS_9_I", "LAND_PRODUCTS_I"
    ),
    lambda: 1,
    lambda: initial_shares_of_crops_all_managements(),
    time_step,
    "_delayfixed_historical_shares_of_crops_delayed_all_managements",
)


@component.add(
    name="historical_shares_rainfed_delayed",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_historical_shares_rainfed_delayed": 1},
    other_deps={
        "_delayfixed_historical_shares_rainfed_delayed": {
            "initial": {"initial_shares_of_rainfed_crops": 1},
            "step": {"historical_share_of_rainfed_crops": 1},
        }
    },
)
def historical_shares_rainfed_delayed():
    return _delayfixed_historical_shares_rainfed_delayed()


_delayfixed_historical_shares_rainfed_delayed = DelayFixed(
    lambda: historical_share_of_rainfed_crops(),
    lambda: 1,
    lambda: initial_shares_of_rainfed_crops(),
    time_step,
    "_delayfixed_historical_shares_rainfed_delayed",
)


@component.add(
    name="increase_of_shares_of_crops_all_managements",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 10,
        "time_historical_data_land_module": 10,
        "historical_increase_of_shares_of_crops_all_managements": 10,
        "matrix_of_changes_of_crops_all_managements": 20,
    },
)
def increase_of_shares_of_crops_all_managements():
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
        },
        ["REGIONS_9_I", "LAND_PRODUCTS_I"],
    )
    value.loc[:, ["CORN"]] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_increase_of_shares_of_crops_all_managements()
            .loc[:, "CORN"]
            .reset_coords(drop=True),
            lambda: sum(
                matrix_of_changes_of_crops_all_managements()
                .loc[:, :, "CORN"]
                .reset_coords(drop=True)
                .rename({"LAND_PRODUCTS_I": "LAND_PRODUCTS_I!"}),
                dim=["LAND_PRODUCTS_I!"],
            )
            - sum(
                matrix_of_changes_of_crops_all_managements()
                .loc[:, "CORN", :]
                .reset_coords(drop=True)
                .rename({"LAND_PRODUCTS_MAP_I": "LAND_PRODUCTS_I!"}),
                dim=["LAND_PRODUCTS_I!"],
            ),
        )
        .expand_dims({"LAND_PRODUCTS_I": ["CORN"]}, 1)
        .values
    )
    value.loc[:, ["RICE"]] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_increase_of_shares_of_crops_all_managements()
            .loc[:, "RICE"]
            .reset_coords(drop=True),
            lambda: sum(
                matrix_of_changes_of_crops_all_managements()
                .loc[:, :, "RICE"]
                .reset_coords(drop=True)
                .rename({"LAND_PRODUCTS_I": "LAND_PRODUCTS_I!"}),
                dim=["LAND_PRODUCTS_I!"],
            )
            - sum(
                matrix_of_changes_of_crops_all_managements()
                .loc[:, "RICE", :]
                .reset_coords(drop=True)
                .rename({"LAND_PRODUCTS_MAP_I": "LAND_PRODUCTS_I!"}),
                dim=["LAND_PRODUCTS_I!"],
            ),
        )
        .expand_dims({"LAND_PRODUCTS_I": ["RICE"]}, 1)
        .values
    )
    value.loc[:, ["CEREALS_OTHER"]] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_increase_of_shares_of_crops_all_managements()
            .loc[:, "CEREALS_OTHER"]
            .reset_coords(drop=True),
            lambda: sum(
                matrix_of_changes_of_crops_all_managements()
                .loc[:, :, "CEREALS_OTHER"]
                .reset_coords(drop=True)
                .rename({"LAND_PRODUCTS_I": "LAND_PRODUCTS_I!"}),
                dim=["LAND_PRODUCTS_I!"],
            )
            - sum(
                matrix_of_changes_of_crops_all_managements()
                .loc[:, "CEREALS_OTHER", :]
                .reset_coords(drop=True)
                .rename({"LAND_PRODUCTS_MAP_I": "LAND_PRODUCTS_I!"}),
                dim=["LAND_PRODUCTS_I!"],
            ),
        )
        .expand_dims({"LAND_PRODUCTS_I": ["CEREALS_OTHER"]}, 1)
        .values
    )
    value.loc[:, ["TUBERS"]] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_increase_of_shares_of_crops_all_managements()
            .loc[:, "TUBERS"]
            .reset_coords(drop=True),
            lambda: sum(
                matrix_of_changes_of_crops_all_managements()
                .loc[:, :, "TUBERS"]
                .reset_coords(drop=True)
                .rename({"LAND_PRODUCTS_I": "LAND_PRODUCTS_I!"}),
                dim=["LAND_PRODUCTS_I!"],
            )
            - sum(
                matrix_of_changes_of_crops_all_managements()
                .loc[:, "TUBERS", :]
                .reset_coords(drop=True)
                .rename({"LAND_PRODUCTS_MAP_I": "LAND_PRODUCTS_I!"}),
                dim=["LAND_PRODUCTS_I!"],
            ),
        )
        .expand_dims({"LAND_PRODUCTS_I": ["TUBERS"]}, 1)
        .values
    )
    value.loc[:, ["SOY"]] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_increase_of_shares_of_crops_all_managements()
            .loc[:, "SOY"]
            .reset_coords(drop=True),
            lambda: sum(
                matrix_of_changes_of_crops_all_managements()
                .loc[:, :, "SOY"]
                .reset_coords(drop=True)
                .rename({"LAND_PRODUCTS_I": "LAND_PRODUCTS_I!"}),
                dim=["LAND_PRODUCTS_I!"],
            )
            - sum(
                matrix_of_changes_of_crops_all_managements()
                .loc[:, "SOY", :]
                .reset_coords(drop=True)
                .rename({"LAND_PRODUCTS_MAP_I": "LAND_PRODUCTS_I!"}),
                dim=["LAND_PRODUCTS_I!"],
            ),
        )
        .expand_dims({"LAND_PRODUCTS_I": ["SOY"]}, 1)
        .values
    )
    value.loc[:, ["PULSES_NUTS"]] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_increase_of_shares_of_crops_all_managements()
            .loc[:, "PULSES_NUTS"]
            .reset_coords(drop=True),
            lambda: sum(
                matrix_of_changes_of_crops_all_managements()
                .loc[:, :, "PULSES_NUTS"]
                .reset_coords(drop=True)
                .rename({"LAND_PRODUCTS_I": "LAND_PRODUCTS_I!"}),
                dim=["LAND_PRODUCTS_I!"],
            )
            - sum(
                matrix_of_changes_of_crops_all_managements()
                .loc[:, "PULSES_NUTS", :]
                .reset_coords(drop=True)
                .rename({"LAND_PRODUCTS_MAP_I": "LAND_PRODUCTS_I!"}),
                dim=["LAND_PRODUCTS_I!"],
            ),
        )
        .expand_dims({"LAND_PRODUCTS_I": ["PULSES_NUTS"]}, 1)
        .values
    )
    value.loc[:, ["OILCROPS"]] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_increase_of_shares_of_crops_all_managements()
            .loc[:, "OILCROPS"]
            .reset_coords(drop=True),
            lambda: sum(
                matrix_of_changes_of_crops_all_managements()
                .loc[:, :, "OILCROPS"]
                .reset_coords(drop=True)
                .rename({"LAND_PRODUCTS_I": "LAND_PRODUCTS_I!"}),
                dim=["LAND_PRODUCTS_I!"],
            )
            - sum(
                matrix_of_changes_of_crops_all_managements()
                .loc[:, "OILCROPS", :]
                .reset_coords(drop=True)
                .rename({"LAND_PRODUCTS_MAP_I": "LAND_PRODUCTS_I!"}),
                dim=["LAND_PRODUCTS_I!"],
            ),
        )
        .expand_dims({"LAND_PRODUCTS_I": ["OILCROPS"]}, 1)
        .values
    )
    value.loc[:, ["SUGAR_CROPS"]] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_increase_of_shares_of_crops_all_managements()
            .loc[:, "SUGAR_CROPS"]
            .reset_coords(drop=True),
            lambda: sum(
                matrix_of_changes_of_crops_all_managements()
                .loc[:, :, "SUGAR_CROPS"]
                .reset_coords(drop=True)
                .rename({"LAND_PRODUCTS_I": "LAND_PRODUCTS_I!"}),
                dim=["LAND_PRODUCTS_I!"],
            )
            - sum(
                matrix_of_changes_of_crops_all_managements()
                .loc[:, "SUGAR_CROPS", :]
                .reset_coords(drop=True)
                .rename({"LAND_PRODUCTS_MAP_I": "LAND_PRODUCTS_I!"}),
                dim=["LAND_PRODUCTS_I!"],
            ),
        )
        .expand_dims({"LAND_PRODUCTS_I": ["SUGAR_CROPS"]}, 1)
        .values
    )
    value.loc[:, ["FRUITS_VEGETABLES"]] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_increase_of_shares_of_crops_all_managements()
            .loc[:, "FRUITS_VEGETABLES"]
            .reset_coords(drop=True),
            lambda: sum(
                matrix_of_changes_of_crops_all_managements()
                .loc[:, :, "FRUITS_VEGETABLES"]
                .reset_coords(drop=True)
                .rename({"LAND_PRODUCTS_I": "LAND_PRODUCTS_I!"}),
                dim=["LAND_PRODUCTS_I!"],
            )
            - sum(
                matrix_of_changes_of_crops_all_managements()
                .loc[:, "FRUITS_VEGETABLES", :]
                .reset_coords(drop=True)
                .rename({"LAND_PRODUCTS_MAP_I": "LAND_PRODUCTS_I!"}),
                dim=["LAND_PRODUCTS_I!"],
            ),
        )
        .expand_dims({"LAND_PRODUCTS_I": ["FRUITS_VEGETABLES"]}, 1)
        .values
    )
    value.loc[:, ["BIOFUEL_2GCROP"]] = 0
    value.loc[:, ["OTHER_CROPS"]] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_increase_of_shares_of_crops_all_managements()
            .loc[:, "OTHER_CROPS"]
            .reset_coords(drop=True),
            lambda: sum(
                matrix_of_changes_of_crops_all_managements()
                .loc[:, :, "OTHER_CROPS"]
                .reset_coords(drop=True)
                .rename({"LAND_PRODUCTS_I": "LAND_PRODUCTS_I!"}),
                dim=["LAND_PRODUCTS_I!"],
            )
            - sum(
                matrix_of_changes_of_crops_all_managements()
                .loc[:, "OTHER_CROPS", :]
                .reset_coords(drop=True)
                .rename({"LAND_PRODUCTS_MAP_I": "LAND_PRODUCTS_I!"}),
                dim=["LAND_PRODUCTS_I!"],
            ),
        )
        .expand_dims({"LAND_PRODUCTS_I": ["OTHER_CROPS"]}, 1)
        .values
    )
    value.loc[:, ["WOOD"]] = 0
    value.loc[:, ["RESIDUES"]] = 0
    return value


@component.add(
    name="increase_of_shares_of_irrigated_crops",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "time_historical_data_land_module": 1,
        "historical_change_of_shares_of_irrigated_crops": 1,
        "increase_of_shares_of_irrigated_crops_aux": 1,
    },
)
def increase_of_shares_of_irrigated_crops():
    return if_then_else(
        time() < time_historical_data_land_module(),
        lambda: historical_change_of_shares_of_irrigated_crops(),
        lambda: increase_of_shares_of_irrigated_crops_aux(),
    )


@component.add(
    name="increase_of_shares_of_irrigated_crops_aux",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 11,
        "time_historical_data_land_module": 11,
        "historical_change_of_shares_of_irrigated_crops": 11,
        "matrix_of_changes_of_irrigated_crops": 22,
    },
)
def increase_of_shares_of_irrigated_crops_aux():
    """
    the matrix goes from taking share of LAND_PRODUCTS_I and sending it to LAND_PRODUCTS_MAP_I the ones that give to that use minus the ones that go from that use to others
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
        },
        ["REGIONS_9_I", "LAND_PRODUCTS_I"],
    )
    value.loc[:, ["CORN"]] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_change_of_shares_of_irrigated_crops()
            .loc[:, "CORN"]
            .reset_coords(drop=True),
            lambda: sum(
                matrix_of_changes_of_irrigated_crops()
                .loc[:, :, "CORN"]
                .reset_coords(drop=True)
                .rename({"LAND_PRODUCTS_I": "LAND_PRODUCTS_I!"}),
                dim=["LAND_PRODUCTS_I!"],
            )
            - sum(
                matrix_of_changes_of_irrigated_crops()
                .loc[:, "CORN", :]
                .reset_coords(drop=True)
                .rename({"LAND_PRODUCTS_MAP_I": "LAND_PRODUCTS_MAP_I!"}),
                dim=["LAND_PRODUCTS_MAP_I!"],
            ),
        )
        .expand_dims({"LAND_PRODUCTS_I": ["CORN"]}, 1)
        .values
    )
    value.loc[:, ["RICE"]] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_change_of_shares_of_irrigated_crops()
            .loc[:, "RICE"]
            .reset_coords(drop=True),
            lambda: sum(
                matrix_of_changes_of_irrigated_crops()
                .loc[:, :, "RICE"]
                .reset_coords(drop=True)
                .rename({"LAND_PRODUCTS_I": "LAND_PRODUCTS_I!"}),
                dim=["LAND_PRODUCTS_I!"],
            )
            - sum(
                matrix_of_changes_of_irrigated_crops()
                .loc[:, "RICE", :]
                .reset_coords(drop=True)
                .rename({"LAND_PRODUCTS_MAP_I": "LAND_PRODUCTS_MAP_I!"}),
                dim=["LAND_PRODUCTS_MAP_I!"],
            ),
        )
        .expand_dims({"LAND_PRODUCTS_I": ["RICE"]}, 1)
        .values
    )
    value.loc[:, ["CEREALS_OTHER"]] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_change_of_shares_of_irrigated_crops()
            .loc[:, "CEREALS_OTHER"]
            .reset_coords(drop=True),
            lambda: sum(
                matrix_of_changes_of_irrigated_crops()
                .loc[:, :, "CEREALS_OTHER"]
                .reset_coords(drop=True)
                .rename({"LAND_PRODUCTS_I": "LAND_PRODUCTS_I!"}),
                dim=["LAND_PRODUCTS_I!"],
            )
            - sum(
                matrix_of_changes_of_irrigated_crops()
                .loc[:, "CEREALS_OTHER", :]
                .reset_coords(drop=True)
                .rename({"LAND_PRODUCTS_MAP_I": "LAND_PRODUCTS_MAP_I!"}),
                dim=["LAND_PRODUCTS_MAP_I!"],
            ),
        )
        .expand_dims({"LAND_PRODUCTS_I": ["CEREALS_OTHER"]}, 1)
        .values
    )
    value.loc[:, ["TUBERS"]] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_change_of_shares_of_irrigated_crops()
            .loc[:, "TUBERS"]
            .reset_coords(drop=True),
            lambda: sum(
                matrix_of_changes_of_irrigated_crops()
                .loc[:, :, "TUBERS"]
                .reset_coords(drop=True)
                .rename({"LAND_PRODUCTS_I": "LAND_PRODUCTS_I!"}),
                dim=["LAND_PRODUCTS_I!"],
            )
            - sum(
                matrix_of_changes_of_irrigated_crops()
                .loc[:, "TUBERS", :]
                .reset_coords(drop=True)
                .rename({"LAND_PRODUCTS_MAP_I": "LAND_PRODUCTS_MAP_I!"}),
                dim=["LAND_PRODUCTS_MAP_I!"],
            ),
        )
        .expand_dims({"LAND_PRODUCTS_I": ["TUBERS"]}, 1)
        .values
    )
    value.loc[:, ["SOY"]] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_change_of_shares_of_irrigated_crops()
            .loc[:, "SOY"]
            .reset_coords(drop=True),
            lambda: sum(
                matrix_of_changes_of_irrigated_crops()
                .loc[:, :, "SOY"]
                .reset_coords(drop=True)
                .rename({"LAND_PRODUCTS_I": "LAND_PRODUCTS_I!"}),
                dim=["LAND_PRODUCTS_I!"],
            )
            - sum(
                matrix_of_changes_of_irrigated_crops()
                .loc[:, "SOY", :]
                .reset_coords(drop=True)
                .rename({"LAND_PRODUCTS_MAP_I": "LAND_PRODUCTS_MAP_I!"}),
                dim=["LAND_PRODUCTS_MAP_I!"],
            ),
        )
        .expand_dims({"LAND_PRODUCTS_I": ["SOY"]}, 1)
        .values
    )
    value.loc[:, ["PULSES_NUTS"]] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_change_of_shares_of_irrigated_crops()
            .loc[:, "PULSES_NUTS"]
            .reset_coords(drop=True),
            lambda: sum(
                matrix_of_changes_of_irrigated_crops()
                .loc[:, :, "PULSES_NUTS"]
                .reset_coords(drop=True)
                .rename({"LAND_PRODUCTS_I": "LAND_PRODUCTS_I!"}),
                dim=["LAND_PRODUCTS_I!"],
            )
            - sum(
                matrix_of_changes_of_irrigated_crops()
                .loc[:, "PULSES_NUTS", :]
                .reset_coords(drop=True)
                .rename({"LAND_PRODUCTS_MAP_I": "LAND_PRODUCTS_MAP_I!"}),
                dim=["LAND_PRODUCTS_MAP_I!"],
            ),
        )
        .expand_dims({"LAND_PRODUCTS_I": ["PULSES_NUTS"]}, 1)
        .values
    )
    value.loc[:, ["OILCROPS"]] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_change_of_shares_of_irrigated_crops()
            .loc[:, "OILCROPS"]
            .reset_coords(drop=True),
            lambda: sum(
                matrix_of_changes_of_irrigated_crops()
                .loc[:, :, "OILCROPS"]
                .reset_coords(drop=True)
                .rename({"LAND_PRODUCTS_I": "LAND_PRODUCTS_I!"}),
                dim=["LAND_PRODUCTS_I!"],
            )
            - sum(
                matrix_of_changes_of_irrigated_crops()
                .loc[:, "OILCROPS", :]
                .reset_coords(drop=True)
                .rename({"LAND_PRODUCTS_MAP_I": "LAND_PRODUCTS_MAP_I!"}),
                dim=["LAND_PRODUCTS_MAP_I!"],
            ),
        )
        .expand_dims({"LAND_PRODUCTS_I": ["OILCROPS"]}, 1)
        .values
    )
    value.loc[:, ["SUGAR_CROPS"]] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_change_of_shares_of_irrigated_crops()
            .loc[:, "SUGAR_CROPS"]
            .reset_coords(drop=True),
            lambda: sum(
                matrix_of_changes_of_irrigated_crops()
                .loc[:, :, "SUGAR_CROPS"]
                .reset_coords(drop=True)
                .rename({"LAND_PRODUCTS_I": "LAND_PRODUCTS_I!"}),
                dim=["LAND_PRODUCTS_I!"],
            )
            - sum(
                matrix_of_changes_of_irrigated_crops()
                .loc[:, "SUGAR_CROPS", :]
                .reset_coords(drop=True)
                .rename({"LAND_PRODUCTS_MAP_I": "LAND_PRODUCTS_MAP_I!"}),
                dim=["LAND_PRODUCTS_MAP_I!"],
            ),
        )
        .expand_dims({"LAND_PRODUCTS_I": ["SUGAR_CROPS"]}, 1)
        .values
    )
    value.loc[:, ["FRUITS_VEGETABLES"]] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_change_of_shares_of_irrigated_crops()
            .loc[:, "FRUITS_VEGETABLES"]
            .reset_coords(drop=True),
            lambda: sum(
                matrix_of_changes_of_irrigated_crops()
                .loc[:, :, "FRUITS_VEGETABLES"]
                .reset_coords(drop=True)
                .rename({"LAND_PRODUCTS_I": "LAND_PRODUCTS_I!"}),
                dim=["LAND_PRODUCTS_I!"],
            )
            - sum(
                matrix_of_changes_of_irrigated_crops()
                .loc[:, "FRUITS_VEGETABLES", :]
                .reset_coords(drop=True)
                .rename({"LAND_PRODUCTS_MAP_I": "LAND_PRODUCTS_MAP_I!"}),
                dim=["LAND_PRODUCTS_MAP_I!"],
            ),
        )
        .expand_dims({"LAND_PRODUCTS_I": ["FRUITS_VEGETABLES"]}, 1)
        .values
    )
    value.loc[:, ["BIOFUEL_2GCROP"]] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_change_of_shares_of_irrigated_crops()
            .loc[:, "BIOFUEL_2GCROP"]
            .reset_coords(drop=True),
            lambda: sum(
                matrix_of_changes_of_irrigated_crops()
                .loc[:, :, "BIOFUEL_2GCROP"]
                .reset_coords(drop=True)
                .rename({"LAND_PRODUCTS_I": "LAND_PRODUCTS_I!"}),
                dim=["LAND_PRODUCTS_I!"],
            )
            - sum(
                matrix_of_changes_of_irrigated_crops()
                .loc[:, "BIOFUEL_2GCROP", :]
                .reset_coords(drop=True)
                .rename({"LAND_PRODUCTS_MAP_I": "LAND_PRODUCTS_MAP_I!"}),
                dim=["LAND_PRODUCTS_MAP_I!"],
            ),
        )
        .expand_dims({"LAND_PRODUCTS_I": ["BIOFUEL_2GCROP"]}, 1)
        .values
    )
    value.loc[:, ["OTHER_CROPS"]] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_change_of_shares_of_irrigated_crops()
            .loc[:, "OTHER_CROPS"]
            .reset_coords(drop=True),
            lambda: sum(
                matrix_of_changes_of_irrigated_crops()
                .loc[:, :, "OTHER_CROPS"]
                .reset_coords(drop=True)
                .rename({"LAND_PRODUCTS_I": "LAND_PRODUCTS_I!"}),
                dim=["LAND_PRODUCTS_I!"],
            )
            - sum(
                matrix_of_changes_of_irrigated_crops()
                .loc[:, "OTHER_CROPS", :]
                .reset_coords(drop=True)
                .rename({"LAND_PRODUCTS_MAP_I": "LAND_PRODUCTS_MAP_I!"}),
                dim=["LAND_PRODUCTS_MAP_I!"],
            ),
        )
        .expand_dims({"LAND_PRODUCTS_I": ["OTHER_CROPS"]}, 1)
        .values
    )
    value.loc[:, ["WOOD"]] = 0
    value.loc[:, ["RESIDUES"]] = 0
    return value


@component.add(
    name="increase_of_shares_of_rainfed_crops",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"increase_of_shares_of_rainfed_crops_aux": 1},
)
def increase_of_shares_of_rainfed_crops():
    """
    IF_THEN_ELSE( Time<TIME_HISTORICAL_DATA_LAND_MODULE:AND:SWITCH_CROPLANDS_TEST_HISTORICAL= 1, HISTORICAL_VARIATION_OF_SHARES_OF_RAINFED_CROPS[LAND PRODUCTS I,REGIONS 9 I](Time), restricted control signal crops rainfed[REGIONS 9 I,LAND PRODUCTS I] )
    """
    return increase_of_shares_of_rainfed_crops_aux()


@component.add(
    name="increase_of_shares_of_rainfed_crops_aux",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 11,
        "time_historical_data_land_module": 11,
        "historical_change_of_shares_rainfed_crops": 11,
        "matrix_of_changes_of_rainfed_crops": 22,
    },
)
def increase_of_shares_of_rainfed_crops_aux():
    """
    the matrix goes from taking share of LAND_PRODUCTS_I and sending it to LAND_PRODUCTS_MAP_I the ones that give to that use minus the ones that go from that use to others
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
        },
        ["REGIONS_9_I", "LAND_PRODUCTS_I"],
    )
    value.loc[:, ["CORN"]] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_change_of_shares_rainfed_crops()
            .loc[:, "CORN"]
            .reset_coords(drop=True),
            lambda: sum(
                matrix_of_changes_of_rainfed_crops()
                .loc[:, :, "CORN"]
                .reset_coords(drop=True)
                .rename({"LAND_PRODUCTS_I": "LAND_PRODUCTS_I!"}),
                dim=["LAND_PRODUCTS_I!"],
            )
            - sum(
                matrix_of_changes_of_rainfed_crops()
                .loc[:, "CORN", :]
                .reset_coords(drop=True)
                .rename({"LAND_PRODUCTS_MAP_I": "LAND_PRODUCTS_MAP_I!"}),
                dim=["LAND_PRODUCTS_MAP_I!"],
            ),
        )
        .expand_dims({"LAND_PRODUCTS_I": ["CORN"]}, 1)
        .values
    )
    value.loc[:, ["RICE"]] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_change_of_shares_rainfed_crops()
            .loc[:, "RICE"]
            .reset_coords(drop=True),
            lambda: sum(
                matrix_of_changes_of_rainfed_crops()
                .loc[:, :, "RICE"]
                .reset_coords(drop=True)
                .rename({"LAND_PRODUCTS_I": "LAND_PRODUCTS_I!"}),
                dim=["LAND_PRODUCTS_I!"],
            )
            - sum(
                matrix_of_changes_of_rainfed_crops()
                .loc[:, "RICE", :]
                .reset_coords(drop=True)
                .rename({"LAND_PRODUCTS_MAP_I": "LAND_PRODUCTS_MAP_I!"}),
                dim=["LAND_PRODUCTS_MAP_I!"],
            ),
        )
        .expand_dims({"LAND_PRODUCTS_I": ["RICE"]}, 1)
        .values
    )
    value.loc[:, ["CEREALS_OTHER"]] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_change_of_shares_rainfed_crops()
            .loc[:, "CEREALS_OTHER"]
            .reset_coords(drop=True),
            lambda: sum(
                matrix_of_changes_of_rainfed_crops()
                .loc[:, :, "CEREALS_OTHER"]
                .reset_coords(drop=True)
                .rename({"LAND_PRODUCTS_I": "LAND_PRODUCTS_I!"}),
                dim=["LAND_PRODUCTS_I!"],
            )
            - sum(
                matrix_of_changes_of_rainfed_crops()
                .loc[:, "CEREALS_OTHER", :]
                .reset_coords(drop=True)
                .rename({"LAND_PRODUCTS_MAP_I": "LAND_PRODUCTS_MAP_I!"}),
                dim=["LAND_PRODUCTS_MAP_I!"],
            ),
        )
        .expand_dims({"LAND_PRODUCTS_I": ["CEREALS_OTHER"]}, 1)
        .values
    )
    value.loc[:, ["TUBERS"]] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_change_of_shares_rainfed_crops()
            .loc[:, "TUBERS"]
            .reset_coords(drop=True),
            lambda: sum(
                matrix_of_changes_of_rainfed_crops()
                .loc[:, :, "TUBERS"]
                .reset_coords(drop=True)
                .rename({"LAND_PRODUCTS_I": "LAND_PRODUCTS_I!"}),
                dim=["LAND_PRODUCTS_I!"],
            )
            - sum(
                matrix_of_changes_of_rainfed_crops()
                .loc[:, "TUBERS", :]
                .reset_coords(drop=True)
                .rename({"LAND_PRODUCTS_MAP_I": "LAND_PRODUCTS_MAP_I!"}),
                dim=["LAND_PRODUCTS_MAP_I!"],
            ),
        )
        .expand_dims({"LAND_PRODUCTS_I": ["TUBERS"]}, 1)
        .values
    )
    value.loc[:, ["SOY"]] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_change_of_shares_rainfed_crops()
            .loc[:, "SOY"]
            .reset_coords(drop=True),
            lambda: sum(
                matrix_of_changes_of_rainfed_crops()
                .loc[:, :, "SOY"]
                .reset_coords(drop=True)
                .rename({"LAND_PRODUCTS_I": "LAND_PRODUCTS_I!"}),
                dim=["LAND_PRODUCTS_I!"],
            )
            - sum(
                matrix_of_changes_of_rainfed_crops()
                .loc[:, "SOY", :]
                .reset_coords(drop=True)
                .rename({"LAND_PRODUCTS_MAP_I": "LAND_PRODUCTS_MAP_I!"}),
                dim=["LAND_PRODUCTS_MAP_I!"],
            ),
        )
        .expand_dims({"LAND_PRODUCTS_I": ["SOY"]}, 1)
        .values
    )
    value.loc[:, ["PULSES_NUTS"]] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_change_of_shares_rainfed_crops()
            .loc[:, "PULSES_NUTS"]
            .reset_coords(drop=True),
            lambda: sum(
                matrix_of_changes_of_rainfed_crops()
                .loc[:, :, "PULSES_NUTS"]
                .reset_coords(drop=True)
                .rename({"LAND_PRODUCTS_I": "LAND_PRODUCTS_I!"}),
                dim=["LAND_PRODUCTS_I!"],
            )
            - sum(
                matrix_of_changes_of_rainfed_crops()
                .loc[:, "PULSES_NUTS", :]
                .reset_coords(drop=True)
                .rename({"LAND_PRODUCTS_MAP_I": "LAND_PRODUCTS_MAP_I!"}),
                dim=["LAND_PRODUCTS_MAP_I!"],
            ),
        )
        .expand_dims({"LAND_PRODUCTS_I": ["PULSES_NUTS"]}, 1)
        .values
    )
    value.loc[:, ["OILCROPS"]] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_change_of_shares_rainfed_crops()
            .loc[:, "OILCROPS"]
            .reset_coords(drop=True),
            lambda: sum(
                matrix_of_changes_of_rainfed_crops()
                .loc[:, :, "OILCROPS"]
                .reset_coords(drop=True)
                .rename({"LAND_PRODUCTS_I": "LAND_PRODUCTS_I!"}),
                dim=["LAND_PRODUCTS_I!"],
            )
            - sum(
                matrix_of_changes_of_rainfed_crops()
                .loc[:, "OILCROPS", :]
                .reset_coords(drop=True)
                .rename({"LAND_PRODUCTS_MAP_I": "LAND_PRODUCTS_MAP_I!"}),
                dim=["LAND_PRODUCTS_MAP_I!"],
            ),
        )
        .expand_dims({"LAND_PRODUCTS_I": ["OILCROPS"]}, 1)
        .values
    )
    value.loc[:, ["SUGAR_CROPS"]] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_change_of_shares_rainfed_crops()
            .loc[:, "SUGAR_CROPS"]
            .reset_coords(drop=True),
            lambda: sum(
                matrix_of_changes_of_rainfed_crops()
                .loc[:, :, "SUGAR_CROPS"]
                .reset_coords(drop=True)
                .rename({"LAND_PRODUCTS_I": "LAND_PRODUCTS_I!"}),
                dim=["LAND_PRODUCTS_I!"],
            )
            - sum(
                matrix_of_changes_of_rainfed_crops()
                .loc[:, "SUGAR_CROPS", :]
                .reset_coords(drop=True)
                .rename({"LAND_PRODUCTS_MAP_I": "LAND_PRODUCTS_MAP_I!"}),
                dim=["LAND_PRODUCTS_MAP_I!"],
            ),
        )
        .expand_dims({"LAND_PRODUCTS_I": ["SUGAR_CROPS"]}, 1)
        .values
    )
    value.loc[:, ["FRUITS_VEGETABLES"]] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_change_of_shares_rainfed_crops()
            .loc[:, "FRUITS_VEGETABLES"]
            .reset_coords(drop=True),
            lambda: sum(
                matrix_of_changes_of_rainfed_crops()
                .loc[:, :, "FRUITS_VEGETABLES"]
                .reset_coords(drop=True)
                .rename({"LAND_PRODUCTS_I": "LAND_PRODUCTS_I!"}),
                dim=["LAND_PRODUCTS_I!"],
            )
            - sum(
                matrix_of_changes_of_rainfed_crops()
                .loc[:, "FRUITS_VEGETABLES", :]
                .reset_coords(drop=True)
                .rename({"LAND_PRODUCTS_MAP_I": "LAND_PRODUCTS_MAP_I!"}),
                dim=["LAND_PRODUCTS_MAP_I!"],
            ),
        )
        .expand_dims({"LAND_PRODUCTS_I": ["FRUITS_VEGETABLES"]}, 1)
        .values
    )
    value.loc[:, ["BIOFUEL_2GCROP"]] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_change_of_shares_rainfed_crops()
            .loc[:, "BIOFUEL_2GCROP"]
            .reset_coords(drop=True),
            lambda: sum(
                matrix_of_changes_of_rainfed_crops()
                .loc[:, :, "BIOFUEL_2GCROP"]
                .reset_coords(drop=True)
                .rename({"LAND_PRODUCTS_I": "LAND_PRODUCTS_I!"}),
                dim=["LAND_PRODUCTS_I!"],
            )
            - sum(
                matrix_of_changes_of_rainfed_crops()
                .loc[:, "BIOFUEL_2GCROP", :]
                .reset_coords(drop=True)
                .rename({"LAND_PRODUCTS_MAP_I": "LAND_PRODUCTS_MAP_I!"}),
                dim=["LAND_PRODUCTS_MAP_I!"],
            ),
        )
        .expand_dims({"LAND_PRODUCTS_I": ["BIOFUEL_2GCROP"]}, 1)
        .values
    )
    value.loc[:, ["OTHER_CROPS"]] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_change_of_shares_rainfed_crops()
            .loc[:, "OTHER_CROPS"]
            .reset_coords(drop=True),
            lambda: sum(
                matrix_of_changes_of_rainfed_crops()
                .loc[:, :, "OTHER_CROPS"]
                .reset_coords(drop=True)
                .rename({"LAND_PRODUCTS_I": "LAND_PRODUCTS_I!"}),
                dim=["LAND_PRODUCTS_I!"],
            )
            - sum(
                matrix_of_changes_of_rainfed_crops()
                .loc[:, "OTHER_CROPS", :]
                .reset_coords(drop=True)
                .rename({"LAND_PRODUCTS_MAP_I": "LAND_PRODUCTS_MAP_I!"}),
                dim=["LAND_PRODUCTS_MAP_I!"],
            ),
        )
        .expand_dims({"LAND_PRODUCTS_I": ["OTHER_CROPS"]}, 1)
        .values
    )
    value.loc[:, ["WOOD"]] = 0
    value.loc[:, ["RESIDUES"]] = 0
    return value


@component.add(
    name="irrigated_crops_available_by_region",
    units="t/Year",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"area_of_irrigated_crops": 1, "yields_of_irrigated_crops": 1},
)
def irrigated_crops_available_by_region():
    return area_of_irrigated_crops() * yields_of_irrigated_crops()


@component.add(
    name="land_products_available_from_croplands",
    units="t/Year",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_separate_irrigated_rainfed": 11,
        "crops_available_all_managements": 11,
        "irrigated_crops_available_by_region": 11,
        "rainfed_crops_available_by_region": 11,
        "residues_available_from_crops": 1,
    },
)
def land_products_available_from_croplands():
    """
    Land products produced from rainfed croplands
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
        },
        ["REGIONS_9_I", "LAND_PRODUCTS_I"],
    )
    value.loc[:, ["CORN"]] = (
        if_then_else(
            switch_separate_irrigated_rainfed() == 1,
            lambda: crops_available_all_managements()
            .loc[:, "CORN"]
            .reset_coords(drop=True),
            lambda: irrigated_crops_available_by_region()
            .loc[:, "CORN"]
            .reset_coords(drop=True)
            + rainfed_crops_available_by_region()
            .loc[:, "CORN"]
            .reset_coords(drop=True),
        )
        .expand_dims({"LAND_PRODUCTS_I": ["CORN"]}, 1)
        .values
    )
    value.loc[:, ["RICE"]] = (
        if_then_else(
            switch_separate_irrigated_rainfed() == 1,
            lambda: crops_available_all_managements()
            .loc[:, "RICE"]
            .reset_coords(drop=True),
            lambda: irrigated_crops_available_by_region()
            .loc[:, "RICE"]
            .reset_coords(drop=True)
            + rainfed_crops_available_by_region()
            .loc[:, "RICE"]
            .reset_coords(drop=True),
        )
        .expand_dims({"LAND_PRODUCTS_I": ["RICE"]}, 1)
        .values
    )
    value.loc[:, ["CEREALS_OTHER"]] = (
        if_then_else(
            switch_separate_irrigated_rainfed() == 1,
            lambda: crops_available_all_managements()
            .loc[:, "CEREALS_OTHER"]
            .reset_coords(drop=True),
            lambda: irrigated_crops_available_by_region()
            .loc[:, "CEREALS_OTHER"]
            .reset_coords(drop=True)
            + rainfed_crops_available_by_region()
            .loc[:, "CEREALS_OTHER"]
            .reset_coords(drop=True),
        )
        .expand_dims({"LAND_PRODUCTS_I": ["CEREALS_OTHER"]}, 1)
        .values
    )
    value.loc[:, ["TUBERS"]] = (
        if_then_else(
            switch_separate_irrigated_rainfed() == 1,
            lambda: crops_available_all_managements()
            .loc[:, "TUBERS"]
            .reset_coords(drop=True),
            lambda: irrigated_crops_available_by_region()
            .loc[:, "TUBERS"]
            .reset_coords(drop=True)
            + rainfed_crops_available_by_region()
            .loc[:, "TUBERS"]
            .reset_coords(drop=True),
        )
        .expand_dims({"LAND_PRODUCTS_I": ["TUBERS"]}, 1)
        .values
    )
    value.loc[:, ["SOY"]] = (
        if_then_else(
            switch_separate_irrigated_rainfed() == 1,
            lambda: crops_available_all_managements()
            .loc[:, "SOY"]
            .reset_coords(drop=True),
            lambda: irrigated_crops_available_by_region()
            .loc[:, "SOY"]
            .reset_coords(drop=True)
            + rainfed_crops_available_by_region().loc[:, "SOY"].reset_coords(drop=True),
        )
        .expand_dims({"LAND_PRODUCTS_I": ["SOY"]}, 1)
        .values
    )
    value.loc[:, ["PULSES_NUTS"]] = (
        if_then_else(
            switch_separate_irrigated_rainfed() == 1,
            lambda: crops_available_all_managements()
            .loc[:, "PULSES_NUTS"]
            .reset_coords(drop=True),
            lambda: irrigated_crops_available_by_region()
            .loc[:, "PULSES_NUTS"]
            .reset_coords(drop=True)
            + rainfed_crops_available_by_region()
            .loc[:, "PULSES_NUTS"]
            .reset_coords(drop=True),
        )
        .expand_dims({"LAND_PRODUCTS_I": ["PULSES_NUTS"]}, 1)
        .values
    )
    value.loc[:, ["OILCROPS"]] = (
        if_then_else(
            switch_separate_irrigated_rainfed() == 1,
            lambda: crops_available_all_managements()
            .loc[:, "OILCROPS"]
            .reset_coords(drop=True),
            lambda: irrigated_crops_available_by_region()
            .loc[:, "OILCROPS"]
            .reset_coords(drop=True)
            + rainfed_crops_available_by_region()
            .loc[:, "OILCROPS"]
            .reset_coords(drop=True),
        )
        .expand_dims({"LAND_PRODUCTS_I": ["OILCROPS"]}, 1)
        .values
    )
    value.loc[:, ["SUGAR_CROPS"]] = (
        if_then_else(
            switch_separate_irrigated_rainfed() == 1,
            lambda: crops_available_all_managements()
            .loc[:, "SUGAR_CROPS"]
            .reset_coords(drop=True),
            lambda: irrigated_crops_available_by_region()
            .loc[:, "SUGAR_CROPS"]
            .reset_coords(drop=True)
            + rainfed_crops_available_by_region()
            .loc[:, "SUGAR_CROPS"]
            .reset_coords(drop=True),
        )
        .expand_dims({"LAND_PRODUCTS_I": ["SUGAR_CROPS"]}, 1)
        .values
    )
    value.loc[:, ["FRUITS_VEGETABLES"]] = (
        if_then_else(
            switch_separate_irrigated_rainfed() == 1,
            lambda: crops_available_all_managements()
            .loc[:, "FRUITS_VEGETABLES"]
            .reset_coords(drop=True),
            lambda: irrigated_crops_available_by_region()
            .loc[:, "FRUITS_VEGETABLES"]
            .reset_coords(drop=True)
            + rainfed_crops_available_by_region()
            .loc[:, "FRUITS_VEGETABLES"]
            .reset_coords(drop=True),
        )
        .expand_dims({"LAND_PRODUCTS_I": ["FRUITS_VEGETABLES"]}, 1)
        .values
    )
    value.loc[:, ["BIOFUEL_2GCROP"]] = (
        if_then_else(
            switch_separate_irrigated_rainfed() == 1,
            lambda: crops_available_all_managements()
            .loc[:, "BIOFUEL_2GCROP"]
            .reset_coords(drop=True),
            lambda: irrigated_crops_available_by_region()
            .loc[:, "BIOFUEL_2GCROP"]
            .reset_coords(drop=True)
            + rainfed_crops_available_by_region()
            .loc[:, "BIOFUEL_2GCROP"]
            .reset_coords(drop=True),
        )
        .expand_dims({"LAND_PRODUCTS_I": ["BIOFUEL_2GCROP"]}, 1)
        .values
    )
    value.loc[:, ["OTHER_CROPS"]] = (
        if_then_else(
            switch_separate_irrigated_rainfed() == 1,
            lambda: crops_available_all_managements()
            .loc[:, "OTHER_CROPS"]
            .reset_coords(drop=True),
            lambda: irrigated_crops_available_by_region()
            .loc[:, "OTHER_CROPS"]
            .reset_coords(drop=True)
            + rainfed_crops_available_by_region()
            .loc[:, "OTHER_CROPS"]
            .reset_coords(drop=True),
        )
        .expand_dims({"LAND_PRODUCTS_I": ["OTHER_CROPS"]}, 1)
        .values
    )
    value.loc[:, ["WOOD"]] = 0
    value.loc[:, ["RESIDUES"]] = (
        residues_available_from_crops()
        .expand_dims({"LAND_PRODUCTS_I": ["RESIDUES"]}, 1)
        .values
    )
    return value


@component.add(
    name="matrix_of_changes_of_crops_all_managements",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I", "LAND_PRODUCTS_MAP_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "ratio_shortage_of_crops": 4,
        "factor_of_minimum_crops": 1,
        "factor_of_maximum_crops": 1,
        "parameter_of_crop_share_change": 1,
    },
)
def matrix_of_changes_of_crops_all_managements():
    return if_then_else(
        (
            ratio_shortage_of_crops().rename({"LAND_PRODUCTS_I": "LAND_PRODUCTS_MAP_I"})
            > ratio_shortage_of_crops()
        ).expand_dims({"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, 2),
        lambda: (
            parameter_of_crop_share_change()
            * (
                ratio_shortage_of_crops().rename(
                    {"LAND_PRODUCTS_I": "LAND_PRODUCTS_MAP_I"}
                )
                - ratio_shortage_of_crops()
            ).transpose("LAND_PRODUCTS_I", "LAND_PRODUCTS_MAP_I")
            * factor_of_minimum_crops().transpose("LAND_PRODUCTS_I", "REGIONS_9_I")
            * factor_of_maximum_crops()
            .rename({"LAND_PRODUCTS_I": "LAND_PRODUCTS_MAP_I"})
            .transpose("LAND_PRODUCTS_MAP_I", "REGIONS_9_I")
        ).transpose("LAND_PRODUCTS_MAP_I", "LAND_PRODUCTS_I", "REGIONS_9_I"),
        lambda: xr.DataArray(
            0,
            {
                "LAND_PRODUCTS_MAP_I": _subscript_dict["LAND_PRODUCTS_MAP_I"],
                "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
                "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            },
            ["LAND_PRODUCTS_MAP_I", "LAND_PRODUCTS_I", "REGIONS_9_I"],
        ),
    ).transpose("REGIONS_9_I", "LAND_PRODUCTS_I", "LAND_PRODUCTS_MAP_I")


@component.add(
    name="matrix_of_changes_of_irrigated_crops",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I", "LAND_PRODUCTS_MAP_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "ratio_shortage_of_crops": 4,
        "factor_minimum_irrigated": 1,
        "factor_maximum_irrigated": 1,
        "parameter_of_crop_share_change": 1,
    },
)
def matrix_of_changes_of_irrigated_crops():
    """
    CHANGES of shares from LAND_PRODUCTS_I to LAND_PRODUCTS_MAP_I , stop cultivating LAND_PRODUCTS_I to cultivate LAND_PRODUCTS_MAP_I IF_THEN_ELSE( (drivers_of_rainfed_crop_changes[REGIONS_9_I,LAND_PRODUCTS_MAP_I]-drivers_o f_rainfed_crop_changes[REGIONS_9_I,LAND_PRODUCTS_I])>0 , MAXIMUM_CHANGE_OF_CROP_SHARE_PER_YEAR*ABS(drivers_of_rainfed_crop_changes[REGIONS_9_I ,LAND_PRODUCTS_MAP_I]-drivers_of_rainfed_crop_changes [REGIONS_9_I,LAND_PRODUCTS_I]), 0 )* factor_of_minimum_rainfed_crop_share[REGIONS_9_I ,AEZ_I,LAND_PRODUCTS_I]*factor_of_maximum_rainfed_crop_share[REGIONS_9_I,AEZ_I,LAND_P RODUCTS_MAP_I]*mask_crops[LAND_PRODUCTS_I]*mask_crops [LAND_PRODUCTS_MAP_I]
    """
    return if_then_else(
        (
            ratio_shortage_of_crops().rename({"LAND_PRODUCTS_I": "LAND_PRODUCTS_MAP_I"})
            > ratio_shortage_of_crops()
        ).expand_dims({"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, 2),
        lambda: (
            parameter_of_crop_share_change()
            * (
                ratio_shortage_of_crops().rename(
                    {"LAND_PRODUCTS_I": "LAND_PRODUCTS_MAP_I"}
                )
                - ratio_shortage_of_crops()
            ).transpose("LAND_PRODUCTS_I", "LAND_PRODUCTS_MAP_I")
            * factor_minimum_irrigated().transpose("LAND_PRODUCTS_I", "REGIONS_9_I")
            * factor_maximum_irrigated()
            .rename({"LAND_PRODUCTS_I": "LAND_PRODUCTS_MAP_I"})
            .transpose("LAND_PRODUCTS_MAP_I", "REGIONS_9_I")
        ).transpose("LAND_PRODUCTS_MAP_I", "LAND_PRODUCTS_I", "REGIONS_9_I"),
        lambda: xr.DataArray(
            0,
            {
                "LAND_PRODUCTS_MAP_I": _subscript_dict["LAND_PRODUCTS_MAP_I"],
                "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
                "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            },
            ["LAND_PRODUCTS_MAP_I", "LAND_PRODUCTS_I", "REGIONS_9_I"],
        ),
    ).transpose("REGIONS_9_I", "LAND_PRODUCTS_I", "LAND_PRODUCTS_MAP_I")


@component.add(
    name="matrix_of_changes_of_rainfed_crops",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I", "LAND_PRODUCTS_MAP_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "ratio_shortage_of_crops": 4,
        "factor_maximum_rainfed_crops": 1,
        "parameter_of_crop_share_change": 1,
        "factor_minimum_rainfed": 1,
    },
)
def matrix_of_changes_of_rainfed_crops():
    """
    CHANGES of shares from LAND_PRODUCTS_I to LAND_PRODUCTS_MAP_I , stop cultivating LAND_PRODUCTS_I to cultivate LAND_PRODUCTS_MAP_I IF_THEN_ELSE( ratio_availability_of_crops[LAND_PRODUCTS_MAP_I]>ratio_availability_of_crop s[LAND_PRODUCTS_I], PARAMETER_OF_CROP_SHARE_CHANGE*(ratio_availability_of_crops[LAND_PRODUCTS_MAP_I]-rati o_availability_of_crops[LAND_PRODUCTS_I ])*factor_minimum_rainfed[REGIONS_9_I,LAND_PRODUCTS_I]*(factor_maximum_rainfed_crops[ REGIONS_9_I,LAND_PRODUCTS_MAP_I]), PARAMETER_OF_CROP_SHARE_CHANGE*(-ratio_availability_of_crops[LAND_PRODUCTS_MAP_I]+rat io_availability_of_crops[LAND_PRODUCTS_I ])*factor_minimum_rainfed[REGIONS_9_I,LAND_PRODUCTS_MAP_I]*(factor_maximum_ rainfed_crops[REGIONS_9_I,LAND_PRODUCTS_I]) )
    """
    return if_then_else(
        (
            ratio_shortage_of_crops().rename({"LAND_PRODUCTS_I": "LAND_PRODUCTS_MAP_I"})
            > ratio_shortage_of_crops()
        ).expand_dims({"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, 2),
        lambda: (
            parameter_of_crop_share_change()
            * (
                ratio_shortage_of_crops().rename(
                    {"LAND_PRODUCTS_I": "LAND_PRODUCTS_MAP_I"}
                )
                - ratio_shortage_of_crops()
            ).transpose("LAND_PRODUCTS_I", "LAND_PRODUCTS_MAP_I")
            * factor_minimum_rainfed().transpose("LAND_PRODUCTS_I", "REGIONS_9_I")
            * factor_maximum_rainfed_crops()
            .rename({"LAND_PRODUCTS_I": "LAND_PRODUCTS_MAP_I"})
            .transpose("LAND_PRODUCTS_MAP_I", "REGIONS_9_I")
        ).transpose("LAND_PRODUCTS_MAP_I", "LAND_PRODUCTS_I", "REGIONS_9_I"),
        lambda: xr.DataArray(
            0,
            {
                "LAND_PRODUCTS_MAP_I": _subscript_dict["LAND_PRODUCTS_MAP_I"],
                "LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"],
                "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            },
            ["LAND_PRODUCTS_MAP_I", "LAND_PRODUCTS_I", "REGIONS_9_I"],
        ),
    ).transpose("REGIONS_9_I", "LAND_PRODUCTS_I", "LAND_PRODUCTS_MAP_I")


@component.add(
    name="parameter_of_crop_share_change",
    units="DMNL",
    subscripts=["LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"mask_crops": 1},
)
def parameter_of_crop_share_change():
    return 0.01 * mask_crops()


@component.add(
    name="rainfed_crops_available_by_region",
    units="t/Year",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"area_of_rainfed_crops": 1, "yields_of_rainfed_crops": 1},
)
def rainfed_crops_available_by_region():
    return area_of_rainfed_crops() * yields_of_rainfed_crops()


@component.add(
    name="ratio_shortage_of_crops",
    units="DMNL",
    subscripts=["LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "mask_crops": 1,
        "land_products_demanded_world": 2,
        "land_products_available_all_regions": 1,
    },
)
def ratio_shortage_of_crops():
    """
    If =1 demand of land product equals production >1 shortage <1 excess of production
    """
    return if_then_else(
        np.logical_and(mask_crops() == 1, land_products_demanded_world() > 20),
        lambda: zidz(
            land_products_demanded_world(), land_products_available_all_regions()
        ),
        lambda: xr.DataArray(
            0,
            {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"]},
            ["LAND_PRODUCTS_I"],
        ),
    )


@component.add(
    name="residues_available_from_crops",
    units="t/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_separate_irrigated_rainfed": 1,
        "share_of_residuals_from_crops": 2,
        "crops_available_all_managements": 1,
        "irrigated_crops_available_by_region": 1,
        "rainfed_crops_available_by_region": 1,
    },
)
def residues_available_from_crops():
    return if_then_else(
        switch_separate_irrigated_rainfed() == 1,
        lambda: sum(
            crops_available_all_managements().rename(
                {"LAND_PRODUCTS_I": "LAND_PRODUCTS_I!"}
            ),
            dim=["LAND_PRODUCTS_I!"],
        )
        * share_of_residuals_from_crops(),
        lambda: (
            sum(
                rainfed_crops_available_by_region().rename(
                    {"LAND_PRODUCTS_I": "LAND_PRODUCTS_I!"}
                ),
                dim=["LAND_PRODUCTS_I!"],
            )
            + sum(
                irrigated_crops_available_by_region().rename(
                    {"LAND_PRODUCTS_I": "LAND_PRODUCTS_I!"}
                ),
                dim=["LAND_PRODUCTS_I!"],
            )
        )
        * share_of_residuals_from_crops(),
    )


@component.add(
    name="share_of_irrigation_per_crop",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "initial_share_of_irrigation": 1},
)
def share_of_irrigation_per_crop():
    return initial_share_of_irrigation(time()).transpose(
        "REGIONS_9_I", "LAND_PRODUCTS_I"
    )


@component.add(
    name="shares_of_crops_all_managements",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_shares_of_crops_all_managements": 1},
    other_deps={
        "_integ_shares_of_crops_all_managements": {
            "initial": {"initial_shares_of_crops_all_managements": 1},
            "step": {"increase_of_shares_of_crops_all_managements": 1},
        }
    },
)
def shares_of_crops_all_managements():
    """
    EQUATIONS NOT SET
    """
    return _integ_shares_of_crops_all_managements()


_integ_shares_of_crops_all_managements = Integ(
    lambda: increase_of_shares_of_crops_all_managements(),
    lambda: initial_shares_of_crops_all_managements(),
    "_integ_shares_of_crops_all_managements",
)


@component.add(
    name="shares_of_irrigated_crops",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_shares_of_irrigated_crops": 1},
    other_deps={
        "_integ_shares_of_irrigated_crops": {
            "initial": {"initial_shares_of_irrigated_crops": 1},
            "step": {"increase_of_shares_of_irrigated_crops": 1},
        }
    },
)
def shares_of_irrigated_crops():
    return _integ_shares_of_irrigated_crops()


_integ_shares_of_irrigated_crops = Integ(
    lambda: increase_of_shares_of_irrigated_crops(),
    lambda: initial_shares_of_irrigated_crops(),
    "_integ_shares_of_irrigated_crops",
)


@component.add(
    name="shares_of_rainfed_crops",
    units="DMNL",
    subscripts=["REGIONS_9_I", "LAND_PRODUCTS_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_shares_of_rainfed_crops": 1},
    other_deps={
        "_integ_shares_of_rainfed_crops": {
            "initial": {"initial_shares_of_rainfed_crops": 1},
            "step": {"increase_of_shares_of_rainfed_crops": 1},
        }
    },
)
def shares_of_rainfed_crops():
    return _integ_shares_of_rainfed_crops()


_integ_shares_of_rainfed_crops = Integ(
    lambda: increase_of_shares_of_rainfed_crops(),
    lambda: initial_shares_of_rainfed_crops(),
    "_integ_shares_of_rainfed_crops",
)


@component.add(
    name="shortage_of_crops",
    units="DMNL",
    subscripts=["LAND_PRODUCTS_I"],
    comp_type="Stateful",
    comp_subtype="Smooth",
    depends_on={"_smooth_shortage_of_crops": 1},
    other_deps={
        "_smooth_shortage_of_crops": {
            "initial": {"time": 1, "aux_shortage_crops": 1},
            "step": {"time": 1, "aux_shortage_crops": 1},
        }
    },
)
def shortage_of_crops():
    """
    shortage_of_crops
    """
    return _smooth_shortage_of_crops()


_smooth_shortage_of_crops = Smooth(
    lambda: if_then_else(
        time() > 2020,
        lambda: aux_shortage_crops(),
        lambda: xr.DataArray(
            0,
            {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"]},
            ["LAND_PRODUCTS_I"],
        ),
    ),
    lambda: xr.DataArray(
        3, {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"]}, ["LAND_PRODUCTS_I"]
    ),
    lambda: if_then_else(
        time() > 2020,
        lambda: aux_shortage_crops(),
        lambda: xr.DataArray(
            0,
            {"LAND_PRODUCTS_I": _subscript_dict["LAND_PRODUCTS_I"]},
            ["LAND_PRODUCTS_I"],
        ),
    ),
    lambda: 1,
    "_smooth_shortage_of_crops",
)


@component.add(
    name="SWITCH_SEPARATE_IRRIGATED_RAINFED",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_separate_irrigated_rainfed"},
)
def switch_separate_irrigated_rainfed():
    """
    =1: crops production and yields are calculated NOT separating irrigated and rainfed crops =0: crops production and yields are calculated separating irrigated and rainfed crops, in this case irrigated and rainfed yields are stimated
    """
    return _ext_constant_switch_separate_irrigated_rainfed()


_ext_constant_switch_separate_irrigated_rainfed = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_SEPARATE_IRRIGATED_RAINFED",
    {},
    _root,
    {},
    "_ext_constant_switch_separate_irrigated_rainfed",
)
