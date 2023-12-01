"""
Module climate.radiative_forcing
Translated using PySD version 3.10.0
"""


@component.add(
    name="adjusted_other_forcings",
    units="w/(m*m)",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "other_forcings": 1,
        "time": 1,
        "mineral_aerosols_and_land_rf": 1,
        "last_historical_rf_year": 1,
    },
)
def adjusted_other_forcings():
    """
    RCP does not include solar and albedo in their other forcings; the adjusted values add the values for these from MAGICC. It is the adjusted other forcings that are included in the total radiative forcing. +IF THEN ELSE(Time>=Last historical RF year, Mineral aerosols and land RF, 0)
    """
    return other_forcings() + if_then_else(
        time() > last_historical_rf_year(),
        lambda: mineral_aerosols_and_land_rf(),
        lambda: 0,
    )


@component.add(
    name="adjustment_for_CH4_and_N2O_ref",
    units="w/(m*m)",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "ch4_n2o_interaction_coeffient": 1,
        "ch4_n20_inter_exp_2": 1,
        "ch4_n2o_unit_adj": 5,
        "ch4_n2o_inter_coef_3": 1,
        "ch4_n20_inter_exp": 1,
        "ch4_atm_conc": 3,
        "n2o_reference_conc": 2,
        "ch4_n2o_inter_coef_2": 1,
    },
)
def adjustment_for_ch4_and_n2o_ref():
    """
    Part of the formula for calculating the radiative forcing from CH4 using the N2O Reference Concentration. Source: "AR5 WG1 Chapter 8 Anthropogenic and Natural Radiative Forcing. Table 8.SM.1 Supplementary for Table 8.3: RF formulae for CO2, CH4 and N2O. Adjusts total RF from CH4 and N2O to be less than the sum of RF from each individually to account for interactions between both gases."
    """
    return ch4_n2o_interaction_coeffient() * np.log(
        1
        + ch4_n2o_inter_coef_2()
        * (
            ch4_atm_conc()
            * n2o_reference_conc()
            * ch4_n2o_unit_adj()
            * ch4_n2o_unit_adj()
        )
        ** ch4_n20_inter_exp()
        + ch4_n2o_inter_coef_3()
        * ch4_atm_conc()
        * ch4_n2o_unit_adj()
        * (
            ch4_atm_conc()
            * n2o_reference_conc()
            * ch4_n2o_unit_adj()
            * ch4_n2o_unit_adj()
        )
        ** ch4_n20_inter_exp_2()
    )


@component.add(
    name="adjustment_for_CH4_ref_and_N2O",
    units="w/(m*m)",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "ch4_n2o_interaction_coeffient": 1,
        "ch4_n20_inter_exp_2": 1,
        "ch4_n2o_unit_adj": 5,
        "ch4_n2o_inter_coef_3": 1,
        "ch4_n20_inter_exp": 1,
        "ch4_reference_conc": 3,
        "n2o_atm_conc": 2,
        "ch4_n2o_inter_coef_2": 1,
    },
)
def adjustment_for_ch4_ref_and_n2o():
    """
    Part of the formula for calculating the radiative forcing from N2O using the CH4 Reference Concentration. Source: "AR5 WG1 Chapter 8 Anthropogenic and Natural Radiative Forcing. Table 8.SM.1 Supplementary for Table 8.3: RF formulae for CO2,CH4 and N2O. Adjusts total RF from CH4 and N2O to be less than the sum of RF from each individually to account for interactions between both gases."
    """
    return ch4_n2o_interaction_coeffient() * np.log(
        1
        + ch4_n2o_inter_coef_2()
        * (
            ch4_reference_conc()
            * n2o_atm_conc()
            * ch4_n2o_unit_adj()
            * ch4_n2o_unit_adj()
        )
        ** ch4_n20_inter_exp()
        + ch4_n2o_inter_coef_3()
        * ch4_reference_conc()
        * ch4_n2o_unit_adj()
        * (
            ch4_reference_conc()
            * n2o_atm_conc()
            * ch4_n2o_unit_adj()
            * ch4_n2o_unit_adj()
        )
        ** ch4_n20_inter_exp_2()
    )


@component.add(
    name="ADJUSTMENT_FOR_CH4REF_AND_N2OREF",
    units="w/(m*m)",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "ch4_n2o_interaction_coeffient": 1,
        "ch4_n20_inter_exp_2": 1,
        "ch4_n2o_unit_adj": 5,
        "ch4_n2o_inter_coef_3": 1,
        "ch4_n20_inter_exp": 1,
        "n2o_reference_conc": 2,
        "ch4_reference_conc": 3,
        "ch4_n2o_inter_coef_2": 1,
    },
)
def adjustment_for_ch4ref_and_n2oref():
    """
    Parameter for calculating the radiative forcing from N2O and from CH4 (both formulas) using the CH4 and N2O Reference Concentration. Source: "AR5 WG1 Chapter 8 Anthropogenic and Natural Radiative Forcing. Table 8.SM.1 Supplementary for Table 8.3: RF formulae for CO2, CH4 and N2O. Adjusts total RF from CH4 and N2O to be less than the sum of RF from each individually to account for interactions between both gases."
    """
    return ch4_n2o_interaction_coeffient() * np.log(
        1
        + ch4_n2o_inter_coef_2()
        * (
            ch4_reference_conc()
            * n2o_reference_conc()
            * ch4_n2o_unit_adj()
            * ch4_n2o_unit_adj()
        )
        ** ch4_n20_inter_exp()
        + ch4_n2o_inter_coef_3()
        * ch4_reference_conc()
        * ch4_n2o_unit_adj()
        * (
            ch4_reference_conc()
            * n2o_reference_conc()
            * ch4_n2o_unit_adj()
            * ch4_n2o_unit_adj()
        )
        ** ch4_n20_inter_exp_2()
    )


@component.add(
    name="CH4_and_N2O_radiative_forcing",
    units="w/(m*m)",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ch4_radiative_forcing": 1, "n2o_radiative_forcing": 1},
)
def ch4_and_n2o_radiative_forcing():
    """
    AR5 WG1 Chapter 8 Anthropogenic and Natural Radiative Forcing. Table 8.SM.1 Supplementary for Table 8.3: RF formulae for CO2, CH4 and N2O. Adjusts total RF from CH4 and N2O to be less than the sum of RF from each individually to account for interactions between both gases.
    """
    return ch4_radiative_forcing() + n2o_radiative_forcing()


@component.add(
    name="CH4_radiative_forcing",
    units="w/(m*m)",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "ch4_radiative_efficiency_coefficient": 1,
        "ch4_atm_conc": 1,
        "ch4_reference_conc": 1,
        "ch4_n2o_unit_adj": 2,
        "adjustment_for_ch4_and_n2o_ref": 1,
        "adjustment_for_ch4ref_and_n2oref": 1,
    },
)
def ch4_radiative_forcing():
    """
    AR5 WG1 Chapter 8 Anthropogenic and Natural Radiative Forcing. Table 8.SM.1 Supplementary for Table 8.3: RF formulae for CO2, CH4 and N2O.
    """
    return ch4_radiative_efficiency_coefficient() * (
        np.sqrt(ch4_atm_conc() * ch4_n2o_unit_adj())
        - np.sqrt(ch4_reference_conc() * ch4_n2o_unit_adj())
    ) - (adjustment_for_ch4_and_n2o_ref() - adjustment_for_ch4ref_and_n2oref())


@component.add(
    name="CO2_radiative_forcing",
    units="w/(m*m)",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "co2_rad_force_coefficient": 1,
        "preindustrial_c": 1,
        "c_in_atmosphere": 1,
    },
)
def co2_radiative_forcing():
    """
    Radiative forcing from accumulation of CO2.
    """
    return co2_rad_force_coefficient() * np.log(c_in_atmosphere() / preindustrial_c())


@component.add(
    name="CO2e_ppm_concentrations",
    units="ppm",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "pre_industrial_ppm_co2": 1,
        "co2_rad_force_coefficient": 1,
        "well_mixed_ghg_forcing": 1,
    },
)
def co2e_ppm_concentrations():
    """
    Concentrations of CO2.
    """
    return pre_industrial_ppm_co2() * np.exp(
        zidz(well_mixed_ghg_forcing(), co2_rad_force_coefficient())
    )


@component.add(
    name="effective_radiative_forcing",
    units="w/(m*m)",
    comp_type="Stateful",
    comp_subtype="SampleIfTrue",
    depends_on={"_sampleiftrue_effective_radiative_forcing": 1},
    other_deps={
        "_sampleiftrue_effective_radiative_forcing": {
            "initial": {"total_radiative_forcing": 1},
            "step": {"time": 1, "time_to_commit_rf": 1, "total_radiative_forcing": 1},
        }
    },
)
def effective_radiative_forcing():
    """
    Total Radiative Forcing from All GHGs
    """
    return _sampleiftrue_effective_radiative_forcing()


_sampleiftrue_effective_radiative_forcing = SampleIfTrue(
    lambda: time() <= time_to_commit_rf(),
    lambda: total_radiative_forcing(),
    lambda: total_radiative_forcing(),
    "_sampleiftrue_effective_radiative_forcing",
)


@component.add(
    name="halocarbon_RF",
    units="w/(m*m)",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"rf_from_f_gases": 1, "mp_rf_total": 1},
)
def halocarbon_rf():
    """
    RF from PFCs, SF6, HFCs, and MP gases.
    """
    return rf_from_f_gases() + mp_rf_total()


@component.add(
    name="HFC_RF_total",
    units="w/(m*m)",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"hfc_rf": 1},
)
def hfc_rf_total():
    """
    The sum of the RFs of the individual HFC types.
    """
    return sum(hfc_rf().rename({"HFC_TYPE_I": "HFC_TYPE_I!"}), dim=["HFC_TYPE_I!"])


@component.add(
    name="N2O_radiative_forcing",
    units="w/(m*m)",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "n2o_radiative_efficiency_coefficient": 1,
        "n2o_atm_conc": 1,
        "n2o_reference_conc": 1,
        "ch4_n2o_unit_adj": 2,
        "adjustment_for_ch4ref_and_n2oref": 1,
        "adjustment_for_ch4_ref_and_n2o": 1,
    },
)
def n2o_radiative_forcing():
    """
    AR5 WG1 Chapter 8 Anthropogenic and Natural Radiative Forcing. Table 8.SM.1 Supplementary for Table 8.3: RF formulae for CO2, CH4 and N2O.
    """
    return n2o_radiative_efficiency_coefficient() * (
        np.sqrt(n2o_atm_conc() * ch4_n2o_unit_adj())
        - np.sqrt(n2o_reference_conc() * ch4_n2o_unit_adj())
    ) - (adjustment_for_ch4_ref_and_n2o() - adjustment_for_ch4ref_and_n2oref())


@component.add(
    name="other_forcings",
    units="w/(m*m)",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "last_historical_rf_year": 1,
        "other_forcings_history": 1,
        "other_forcings_rcp": 1,
    },
)
def other_forcings():
    """
    Forcings for all components except well-mixed GHGs. Switch over from historical data to projections in 1995 (GISS) and bridge to RCPs starting in 2010.
    """
    return if_then_else(
        time() <= last_historical_rf_year(),
        lambda: other_forcings_history(),
        lambda: other_forcings_rcp(),
    )


@component.add(
    name="OTHER_FORCINGS_RCP",
    units="w/(m*m)",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_model_explorer": 1,
        "other_forcings_rcp_scenario": 8,
        "model_explorer_rcp_ghg_emissions": 3,
        "select_rcp_for_exogenous_ghg_emissions_sp": 3,
    },
)
def other_forcings_rcp():
    """
    Projections "Representative Concentration Pathways" (RCPs) Choose RCP: 1. RCP 2.6 2. RCP 4.5 3. RCP 6.0 4. RCP 8.5
    """
    return if_then_else(
        switch_model_explorer() == 1,
        lambda: if_then_else(
            model_explorer_rcp_ghg_emissions() == 1,
            lambda: float(other_forcings_rcp_scenario().loc["RCP26"]),
            lambda: if_then_else(
                model_explorer_rcp_ghg_emissions() == 2,
                lambda: float(other_forcings_rcp_scenario().loc["RCP45"]),
                lambda: if_then_else(
                    model_explorer_rcp_ghg_emissions() == 3,
                    lambda: float(other_forcings_rcp_scenario().loc["RCP60"]),
                    lambda: float(other_forcings_rcp_scenario().loc["RCP85"]),
                ),
            ),
        ),
        lambda: if_then_else(
            select_rcp_for_exogenous_ghg_emissions_sp() == 1,
            lambda: float(other_forcings_rcp_scenario().loc["RCP26"]),
            lambda: if_then_else(
                select_rcp_for_exogenous_ghg_emissions_sp() == 2,
                lambda: float(other_forcings_rcp_scenario().loc["RCP45"]),
                lambda: if_then_else(
                    select_rcp_for_exogenous_ghg_emissions_sp() == 3,
                    lambda: float(other_forcings_rcp_scenario().loc["RCP60"]),
                    lambda: float(other_forcings_rcp_scenario().loc["RCP85"]),
                ),
            ),
        ),
    )


@component.add(
    name="other_GHG_rad_forcing_non_CO2",
    units="w/(m*m)",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_radiative_forcing": 1, "co2_radiative_forcing": 1},
)
def other_ghg_rad_forcing_non_co2():
    """
    GHG radiative forcing except CO2 radiative forcing.
    """
    return total_radiative_forcing() - co2_radiative_forcing()


@component.add(
    name="RF_from_F_gases",
    units="w/(m*m)",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"pfc_rf": 1, "sf6_rf": 1, "hfc_rf_total": 1},
)
def rf_from_f_gases():
    """
    Radiative forcing due to fluorinated gases, based on the concentration of each gas multiplied by its radiative forcing coefficient. The RF of HFCs is the sum of the RFs of the individual HFC types:
    """
    return pfc_rf() + sf6_rf() + hfc_rf_total()


@component.add(
    name="total_radiative_forcing",
    units="w/(m*m)",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"well_mixed_ghg_forcing": 1, "adjusted_other_forcings": 1},
)
def total_radiative_forcing():
    """
    Total radiative forcing
    """
    return well_mixed_ghg_forcing() + adjusted_other_forcings()


@component.add(
    name="well_mixed_GHG_forcing",
    units="w/(m*m)",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "co2_radiative_forcing": 1,
        "ch4_and_n2o_radiative_forcing": 1,
        "halocarbon_rf": 1,
    },
)
def well_mixed_ghg_forcing():
    """
    Well mixed GHG radiative forcing
    """
    return co2_radiative_forcing() + ch4_and_n2o_radiative_forcing() + halocarbon_rf()
