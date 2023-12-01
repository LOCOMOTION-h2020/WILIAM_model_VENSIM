"""
Module materials.embodied_energy_use
Translated using PySD version 3.10.0
"""


@component.add(
    name="dynamic_embodied_PE_intensity_materials",
    units="MJ/kg",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "final_to_primary_energy_by_region_until_2015": 1,
        "embodied_fe_intensity_materials": 2,
        "final_to_primary_energy_by_region": 1,
    },
)
def dynamic_embodied_pe_intensity_materials():
    """
    Dynamic embodied primary energy intensity of materials.
    """
    return if_then_else(
        time() < 2015,
        lambda: zidz(
            embodied_fe_intensity_materials(),
            final_to_primary_energy_by_region_until_2015().expand_dims(
                {"MATERIALS_I": _subscript_dict["MATERIALS_I"]}, 1
            ),
        ),
        lambda: zidz(
            embodied_fe_intensity_materials(),
            final_to_primary_energy_by_region().expand_dims(
                {"MATERIALS_I": _subscript_dict["MATERIALS_I"]}, 1
            ),
        ),
    )


@component.add(
    name="embodied_FE_intensity_materials",
    units="MJ/kg",
    subscripts=["REGIONS_9_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "embodied_pe_intensity_materials_36r": 1,
        "final_to_primary_energy_by_region_until_2015": 1,
    },
)
def embodied_fe_intensity_materials():
    """
    Embodied final energy intensity of materials taking as reference the recycling rates of minerals and the final-to-primary ratio of the year 2015.
    """
    return (
        embodied_pe_intensity_materials_36r()
        .loc[_subscript_dict["REGIONS_9_I"], :]
        .rename({"REGIONS_36_I": "REGIONS_9_I"})
        * final_to_primary_energy_by_region_until_2015()
    )


@component.add(
    name="embodied_PE_intensity_materials_36R",
    units="MJ/kg",
    subscripts=["REGIONS_36_I", "MATERIALS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_mat_embodied_energy_of_material_use": 2,
        "embodied_pe_intensity_recycled_materials": 2,
        "rc_rate_mineral_35r": 2,
        "embodied_pe_intensity_virgin_materials": 2,
        "rc_rate_mineral": 2,
    },
)
def embodied_pe_intensity_materials_36r():
    """
    Embodied primary energy intensity of materials taking as reference the recycling rates of minerals.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_36_I": _subscript_dict["REGIONS_36_I"],
            "MATERIALS_I": _subscript_dict["MATERIALS_I"],
        },
        ["REGIONS_36_I", "MATERIALS_I"],
    )
    value.loc[_subscript_dict["REGIONS_35_I"], :] = if_then_else(
        switch_mat_embodied_energy_of_material_use() == 0,
        lambda: xr.DataArray(
            0,
            {
                "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                "MATERIALS_I": _subscript_dict["MATERIALS_I"],
            },
            ["REGIONS_35_I", "MATERIALS_I"],
        ),
        lambda: rc_rate_mineral_35r() * embodied_pe_intensity_recycled_materials()
        + (1 - rc_rate_mineral_35r()) * embodied_pe_intensity_virgin_materials(),
    ).values
    value.loc[["EU27"], :] = (
        if_then_else(
            switch_mat_embodied_energy_of_material_use() == 0,
            lambda: xr.DataArray(
                0, {"MATERIALS_I": _subscript_dict["MATERIALS_I"]}, ["MATERIALS_I"]
            ),
            lambda: rc_rate_mineral().loc["EU27", :].reset_coords(drop=True)
            * embodied_pe_intensity_recycled_materials()
            + (1 - rc_rate_mineral().loc["EU27", :].reset_coords(drop=True))
            * embodied_pe_intensity_virgin_materials(),
        )
        .expand_dims({"REGIONS_36_I": ["EU27"]}, 0)
        .values
    )
    return value
