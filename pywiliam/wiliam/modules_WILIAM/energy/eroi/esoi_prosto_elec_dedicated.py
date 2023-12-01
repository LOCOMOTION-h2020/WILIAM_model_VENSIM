"""
Module energy.eroi.esoi_prosto_elec_dedicated
Translated using PySD version 3.10.0
"""


@component.add(
    name="dynESOIst_PROSTO_elec_dedicated",
    units="DMNL",
    subscripts=["REGIONS_9_I", "PROSTO_ELEC_DEDICATED_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"stored_energy_output_by_prosto": 1, "fenust_prosto_elec_dedicated": 1},
)
def dynesoist_prosto_elec_dedicated():
    """
    Dynamic evolution of the ESOIst of PROSTO elec dedicated (PHS and stationary batteries).
    """
    return zidz(
        stored_energy_output_by_prosto()
        .loc[:, _subscript_dict["PROSTO_ELEC_DEDICATED_I"]]
        .rename({"PROSTO_ELEC_I": "PROSTO_ELEC_DEDICATED_I"}),
        fenust_prosto_elec_dedicated(),
    )


@component.add(
    name="ESOIst_initial_PHS",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "eroist_ini_hydro_2015": 1,
        "cf_protra_full_load_hours": 1,
        "cf_prosto": 1,
    },
)
def esoist_initial_phs():
    """
    ESOI over the lifetime of PHS when the full potential is available.
    """
    return eroist_ini_hydro_2015() * (
        cf_prosto().loc[:, "PROSTO_PHS"].reset_coords(drop=True)
        / cf_protra_full_load_hours()
        .loc[:, "PROTRA_PP_hydropower_dammed"]
        .reset_coords(drop=True)
    )


@component.add(
    name="ESOIst_PHS",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cf_prosto": 1,
        "prosto_dedicated_lifetime": 1,
        "unit_conversion_wh_we": 1,
        "unit_conversion_j_wh": 1,
        "matrix_unit_prefixes": 1,
        "fenust_intensity_phs_exogenous": 1,
    },
)
def esoist_phs():
    """
    ESOIst over the lifetime of PHS.
    """
    return zidz(
        cf_prosto().loc[:, "PROSTO_PHS"].reset_coords(drop=True)
        * float(prosto_dedicated_lifetime().loc["PROSTO_PHS"])
        * (
            (unit_conversion_j_wh() / float(matrix_unit_prefixes().loc["exa", "tera"]))
            / (1 / unit_conversion_wh_we())
        ),
        fenust_intensity_phs_exogenous(),
    )


@component.add(
    name="FEnUst_intensity_PHS_exogenous",
    units="EJ/TW",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cf_prosto": 1,
        "prosto_dedicated_lifetime": 1,
        "unit_conversion_wh_we": 1,
        "unit_conversion_j_wh": 1,
        "matrix_unit_prefixes": 1,
        "esoist_initial_phs": 1,
    },
)
def fenust_intensity_phs_exogenous():
    """
    Energy use (in final energy terms) per new installed capacity (TW) over lifetime for PHS. We assume the same lifetime for PHS than for hydro. Exogenous EROI assumed.
    """
    return zidz(
        cf_prosto().loc[:, "PROSTO_PHS"].reset_coords(drop=True)
        * float(prosto_dedicated_lifetime().loc["PROSTO_PHS"])
        * (
            unit_conversion_j_wh()
            * unit_conversion_wh_we()
            / float(matrix_unit_prefixes().loc["exa", "tera"])
        ),
        esoist_initial_phs(),
    )


@component.add(
    name="FEnUst_intensity_stationary_batteries",
    units="EJ/TW",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "materials_per_new_capacity_installed_ev_batteries_lfp": 1,
        "embodied_fe_intensity_materials": 1,
        "unit_conversion_mj_ej": 1,
        "unit_conversion_mw_tw": 1,
    },
)
def fenust_intensity_stationary_batteries():
    """
    Energy use (in final energy terms) per new installed capacity (MW) over lifetime for electric stationary batteries. LFP are assumed.
    """
    return sum(
        materials_per_new_capacity_installed_ev_batteries_lfp().rename(
            {"MATERIALS_I": "MATERIALS_I!"}
        )
        * embodied_fe_intensity_materials()
        .rename({"MATERIALS_I": "MATERIALS_I!"})
        .transpose("MATERIALS_I!", "REGIONS_9_I"),
        dim=["MATERIALS_I!"],
    ) * (unit_conversion_mw_tw() / unit_conversion_mj_ej())


@component.add(
    name="FEnUst_PROSTO_elec_dedicated",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "PROSTO_ELEC_DEDICATED_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_fei_elec_storage0": 2,
        "prosto_dedicated_capacity_expansion": 2,
        "fenust_intensity_phs_exogenous": 1,
        "fenust_intensity_stationary_batteries": 1,
    },
)
def fenust_prosto_elec_dedicated():
    """
    Energy use (in final terms) over the lifetime for installing PHS.
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
        if_then_else(
            switch_fei_elec_storage0() == 1,
            lambda: xr.DataArray(
                0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
            ),
            lambda: prosto_dedicated_capacity_expansion()
            .loc[:, "PROSTO_PHS"]
            .reset_coords(drop=True)
            * fenust_intensity_phs_exogenous(),
        )
        .expand_dims({"NRG_PRO_I": ["PROSTO_PHS"]}, 1)
        .values
    )
    value.loc[:, ["PROSTO_STATIONARY_BATTERIES"]] = (
        if_then_else(
            switch_fei_elec_storage0() == 1,
            lambda: xr.DataArray(
                0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
            ),
            lambda: prosto_dedicated_capacity_expansion()
            .loc[:, "PROSTO_STATIONARY_BATTERIES"]
            .reset_coords(drop=True)
            * fenust_intensity_stationary_batteries(),
        )
        .expand_dims({"NRG_PRO_I": ["PROSTO_STATIONARY_BATTERIES"]}, 1)
        .values
    )
    return value
