"""
Module materials.list_outputs_and_indicators
Translated using PySD version 3.10.0
"""


@component.add(
    name="materials_consumption_per_capita",
    units="Mt/(Year*person)",
    subscripts=["METALS_W_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "al_consumption_per_capita": 1,
        "fe_consumption_per_capita": 1,
        "cu_consumption_per_capita": 1,
        "ni_consumption_per_capita": 1,
    },
)
def materials_consumption_per_capita():
    """
    mateials consumption in kg/person/year.
    """
    value = xr.DataArray(
        np.nan, {"METALS_W_I": _subscript_dict["METALS_W_I"]}, ["METALS_W_I"]
    )
    value.loc[["Al_W"]] = al_consumption_per_capita()
    value.loc[["Fe_W"]] = fe_consumption_per_capita()
    value.loc[["Cu_W"]] = cu_consumption_per_capita()
    value.loc[["Ni_W"]] = ni_consumption_per_capita()
    return value


@component.add(
    name="materials_share_of_secondary_material",
    units="DMNL",
    subscripts=["METALS_W_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "al_share_of_secondary_material": 1,
        "cu_share_of_secondary_material": 1,
        "fe_share_of_secondary_material": 1,
        "ni_share_of_secondary_material": 1,
    },
)
def materials_share_of_secondary_material():
    """
    Share of secondary material used to produce new material to be sold on the market.
    """
    value = xr.DataArray(
        np.nan, {"METALS_W_I": _subscript_dict["METALS_W_I"]}, ["METALS_W_I"]
    )
    value.loc[["Al_W"]] = al_share_of_secondary_material()
    value.loc[["Cu_W"]] = cu_share_of_secondary_material()
    value.loc[["Fe_W"]] = fe_share_of_secondary_material()
    value.loc[["Ni_W"]] = ni_share_of_secondary_material()
    return value
