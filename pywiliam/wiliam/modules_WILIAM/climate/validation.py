"""
Module climate.validation
Translated using PySD version 3.10.0
"""


@component.add(
    name="check_hist_GHG_emissions",
    units="percent",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "total_ghg_emissions": 1,
        "total_ghg_emissions_including_land_use_change_and_forestry": 2,
    },
)
def check_hist_ghg_emissions():
    """
    Percentage difference of CO2 emissions from fossil fuel consumption in the model vs historic.
    """
    return xr.DataArray(
        if_then_else(
            time() < 2012,
            lambda: (
                sum(
                    total_ghg_emissions().rename({"REGIONS_9_I": "REGIONS_9_I!"}),
                    dim=["REGIONS_9_I!"],
                )
                - total_ghg_emissions_including_land_use_change_and_forestry()
            )
            * 100
            / total_ghg_emissions_including_land_use_change_and_forestry(),
            lambda: 0,
        ),
        {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
        ["REGIONS_9_I"],
    )
