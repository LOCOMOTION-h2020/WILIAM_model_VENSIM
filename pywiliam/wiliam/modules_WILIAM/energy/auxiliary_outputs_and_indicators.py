"""
Module energy.auxiliary_outputs_and_indicators
Translated using PySD version 3.10.0
"""


@component.add(
    name="annual_FE_GDP_intensity_change_rate",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"fe_gdp_intensity": 1, "delayed_fe_gdp_intensity": 1},
)
def annual_fe_gdp_intensity_change_rate():
    """
    Annual FE GDP intensity change rate.
    """
    return -1 + zidz(fe_gdp_intensity(), delayed_fe_gdp_intensity())


@component.add(
    name="annual_PE_GDP_intensity_change_rate",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"pe_gdp_intensity": 1, "delayed_pe_gdp_intensity": 1},
)
def annual_pe_gdp_intensity_change_rate():
    """
    Annual PE GDP intensity change rate.
    """
    return -1 + zidz(pe_gdp_intensity(), delayed_pe_gdp_intensity())


@component.add(
    name="aux_final_to_primary_energy_by_region_until_2015",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_aux_final_to_primary_energy_by_region_until_2015": 1},
    other_deps={
        "_delayfixed_aux_final_to_primary_energy_by_region_until_2015": {
            "initial": {"time_step": 1},
            "step": {"final_to_primary_energy_by_region_until_2015": 1},
        }
    },
)
def aux_final_to_primary_energy_by_region_until_2015():
    """
    Auxiliary variable to estimate the final-to-primary energy ratio in the year 2015. The method is not mathematically exact, but the error tends to 0 when the TIME STEP decreases.
    """
    return _delayfixed_aux_final_to_primary_energy_by_region_until_2015()


_delayfixed_aux_final_to_primary_energy_by_region_until_2015 = DelayFixed(
    lambda: final_to_primary_energy_by_region_until_2015(),
    lambda: time_step(),
    lambda: xr.DataArray(
        0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
    ),
    time_step,
    "_delayfixed_aux_final_to_primary_energy_by_region_until_2015",
)


@component.add(
    name="auxiliary_FE_GDP_intensity",
    units="TJ/Mdollars_2015",
    subscripts=["REGIONS_9_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_auxiliary_fe_gdp_intensity": 1},
    other_deps={
        "_delayfixed_auxiliary_fe_gdp_intensity": {
            "initial": {"time_step": 1},
            "step": {"fe_gdp_intensity_until_2015": 1},
        }
    },
)
def auxiliary_fe_gdp_intensity():
    """
    Auxiliary variable to estimate the cumulative TPES intensity change until 2009.
    """
    return _delayfixed_auxiliary_fe_gdp_intensity()


_delayfixed_auxiliary_fe_gdp_intensity = DelayFixed(
    lambda: fe_gdp_intensity_until_2015(),
    lambda: time_step(),
    lambda: xr.DataArray(
        0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
    ),
    time_step,
    "_delayfixed_auxiliary_fe_gdp_intensity",
)


@component.add(
    name="auxiliary_PE_GDP_intensity",
    units="TJ/Mdollars_2015",
    subscripts=["REGIONS_9_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_auxiliary_pe_gdp_intensity": 1},
    other_deps={
        "_delayfixed_auxiliary_pe_gdp_intensity": {
            "initial": {"time_step": 1},
            "step": {"pe_gdp_intensity_until_2015": 1},
        }
    },
)
def auxiliary_pe_gdp_intensity():
    """
    Auxiliary variable to estimate the cumulative TPES intensity change until 2009.
    """
    return _delayfixed_auxiliary_pe_gdp_intensity()


_delayfixed_auxiliary_pe_gdp_intensity = DelayFixed(
    lambda: pe_gdp_intensity_until_2015(),
    lambda: time_step(),
    lambda: xr.DataArray(
        0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
    ),
    time_step,
    "_delayfixed_auxiliary_pe_gdp_intensity",
)


@component.add(
    name="CF_power_system",
    units="TWh/(TW*h)",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_to_allocated": 1,
        "unit_conversion_twh_ej": 1,
        "unit_conversion_hours_year": 1,
        "protra_capacity_stock": 1,
    },
)
def cf_power_system():
    """
    Capacity factor of the whole power system
    """
    return zidz(
        sum(
            protra_to_allocated()
            .loc[:, "TO_elec", :]
            .reset_coords(drop=True)
            .rename({"NRG_PROTRA_I": "NRG_PROTRA_I!"}),
            dim=["NRG_PROTRA_I!"],
        )
        * unit_conversion_twh_ej(),
        sum(
            protra_capacity_stock()
            .loc[:, "TO_elec", :]
            .reset_coords(drop=True)
            .rename({"NRG_PROTRA_I": "NRG_PROTRA_I!"}),
            dim=["NRG_PROTRA_I!"],
        )
        * unit_conversion_hours_year(),
    )


@component.add(
    name="CO2_EMISSION_FACTORS_PE",
    units="kg/TJ",
    subscripts=["NRG_PE_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_co2_emission_factors_pe"},
)
def co2_emission_factors_pe():
    """
    CO2 emission factors per type of primary energy (Source: IPCC 2006 Guidelines). Only fossil fuels, for RES the convention is to assign 0 kg/TJ (consistency with land-use module).
    """
    return _ext_constant_co2_emission_factors_pe()


_ext_constant_co2_emission_factors_pe = ExtConstant(
    "model_parameters/energy/energy-emission_factors.xlsx",
    "GHG_emission_factors",
    "CO2_EMISSION_FACTORS_PE*",
    {"NRG_PE_I": _subscript_dict["NRG_PE_I"]},
    _root,
    {"NRG_PE_I": _subscript_dict["NRG_PE_I"]},
    "_ext_constant_co2_emission_factors_pe",
)


@component.add(
    name="CO2_EMISSION_FACTORS_PROTRA_TI_STATIONARY_COMBUSTION",
    units="kg/TJ",
    subscripts=["NRG_PROTRA_I", "NRG_TI_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_co2_emission_factors_protra_ti_stationary_combustion"
    },
)
def co2_emission_factors_protra_ti_stationary_combustion():
    return _ext_constant_co2_emission_factors_protra_ti_stationary_combustion()


_ext_constant_co2_emission_factors_protra_ti_stationary_combustion = ExtConstant(
    "model_parameters/energy/energy-emission_factors.xlsx",
    "GHG_emission_factors",
    "CO2_EMISSION_FACTORS_PROTRA_TI_STATIONARY_COMBUSTION",
    {
        "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
        "NRG_TI_I": _subscript_dict["NRG_TI_I"],
    },
    _root,
    {
        "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
        "NRG_TI_I": _subscript_dict["NRG_TI_I"],
    },
    "_ext_constant_co2_emission_factors_protra_ti_stationary_combustion",
)


@component.add(
    name="CO2_emissions_by_PROTRA",
    units="Mt/Year",
    subscripts=["REGIONS_9_I", "NRG_PROTRA_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "co2_emission_factors_protra_ti_stationary_combustion": 1,
        "ti_by_protra_and_commodity": 1,
        "unit_conversion_tj_ej": 1,
        "unit_conversion_kg_mt": 1,
    },
)
def co2_emissions_by_protra():
    """
    CO2 emissions by process transformation.
    """
    return (
        sum(
            co2_emission_factors_protra_ti_stationary_combustion().rename(
                {"NRG_TI_I": "NRG_TI_I!"}
            )
            * ti_by_protra_and_commodity()
            .rename({"NRG_TI_I": "NRG_TI_I!"})
            .transpose("NRG_PROTRA_I", "NRG_TI_I!", "REGIONS_9_I"),
            dim=["NRG_TI_I!"],
        )
        * unit_conversion_tj_ej()
        / unit_conversion_kg_mt()
    ).transpose("REGIONS_9_I", "NRG_PROTRA_I")


@component.add(
    name="CO2_emissions_captured_CCS",
    units="Mt/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"co2_emissions_by_protra": 1},
)
def co2_emissions_captured_ccs():
    """
    CO2 emissions captured through CCS
    """
    return -sum(
        co2_emissions_by_protra()
        .loc[:, _subscript_dict["PROTRA_CCS_I"]]
        .rename({"NRG_PROTRA_I": "PROTRA_CCS_I!"}),
        dim=["PROTRA_CCS_I!"],
    )


@component.add(
    name="CO2_emissions_PE_combustion_before_CCS",
    units="Mt/Year",
    subscripts=["REGIONS_9_I", "NRG_PE_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "pe_by_commodity": 1,
        "co2_emission_factors_pe": 1,
        "unit_conversion_tj_ej": 1,
        "unit_conversion_kg_mt": 1,
    },
)
def co2_emissions_pe_combustion_before_ccs():
    """
    Total CO2 emissions from primery energy combustion without accounting for CCS sequestration.
    """
    return (
        pe_by_commodity()
        * co2_emission_factors_pe()
        * unit_conversion_tj_ej()
        / unit_conversion_kg_mt()
    )


@component.add(
    name="CO2_emissions_per_capita_9R",
    units="t/(Year*person)",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ghg_emissions_per_capita_9r": 1},
)
def co2_emissions_per_capita_9r():
    """
    CO2 emissions per capita by region.
    """
    return ghg_emissions_per_capita_9r().loc[:, "CO2"].reset_coords(drop=True)


@component.add(
    name="CO2_emissions_TO_elec",
    units="Mt/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"co2_emissions_by_protra": 2, "share_to_elec_chp_plants": 1},
)
def co2_emissions_to_elec():
    """
    CO2 emissions of electricity production.
    """
    return sum(
        co2_emissions_by_protra()
        .loc[:, _subscript_dict["PROTRA_PP_I"]]
        .rename({"NRG_PROTRA_I": "PROTRA_PP_I!"}),
        dim=["PROTRA_PP_I!"],
    ) + sum(
        share_to_elec_chp_plants().rename({"PROTRA_CHP_I": "PROTRA_CHP_I!"})
        * co2_emissions_by_protra()
        .loc[:, _subscript_dict["PROTRA_CHP_I"]]
        .rename({"NRG_PROTRA_I": "PROTRA_CHP_I!"}),
        dim=["PROTRA_CHP_I!"],
    )


@component.add(
    name="CO2_emissions_TO_heat",
    units="Mt/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"co2_emissions_by_protra": 2, "share_to_elec_chp_plants": 1},
)
def co2_emissions_to_heat():
    """
    CO2 emissions of heat production.
    """
    return sum(
        co2_emissions_by_protra()
        .loc[:, _subscript_dict["PROTRA_HP_I"]]
        .rename({"NRG_PROTRA_I": "PROTRA_HP_I!"}),
        dim=["PROTRA_HP_I!"],
    ) + (
        1
        - sum(
            share_to_elec_chp_plants().rename({"PROTRA_CHP_I": "PROTRA_CHP_I!"})
            * co2_emissions_by_protra()
            .loc[:, _subscript_dict["PROTRA_CHP_I"]]
            .rename({"NRG_PROTRA_I": "PROTRA_CHP_I!"}),
            dim=["PROTRA_CHP_I!"],
        )
    )


@component.add(
    name="CO2_intensity_TO_elec",
    units="Mt/EJ",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"co2_emissions_to_elec": 1, "to_by_commodity": 1},
)
def co2_intensity_to_elec():
    """
    CO2 mass per unit of electricity generation.
    """
    return zidz(
        co2_emissions_to_elec(),
        to_by_commodity().loc[:, "TO_elec"].reset_coords(drop=True),
    )


@component.add(
    name="CO2_intensity_TO_elec_gCO2_per_kWh",
    units="gCO2/kWh/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"co2_intensity_to_elec": 1},
)
def co2_intensity_to_elec_gco2_per_kwh():
    return co2_intensity_to_elec() * 10**12 / (2.777 * 10**11)


@component.add(
    name="CO2_intensity_TO_heat",
    units="Mt/EJ",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"co2_emissions_to_heat": 1, "to_by_commodity": 1},
)
def co2_intensity_to_heat():
    """
    CO2 mass per unit of heat generation.
    """
    return zidz(
        co2_emissions_to_heat(),
        to_by_commodity().loc[:, "TO_heat"].reset_coords(drop=True),
    )


@component.add(
    name="CO2e_emissions_per_unit_of_sector_output",
    units="tCO2eq/Mdollars_2015",
    subscripts=["REGIONS_9_I", "SECTORS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "ghg_emissions_by_sector": 3,
        "unit_conversion_t_mt": 3,
        "gwp_20_year": 3,
        "select_gwp_time_frame_sp": 3,
        "gwp_100_year": 3,
        "output_real_9r": 1,
    },
)
def co2e_emissions_per_unit_of_sector_output():
    return zidz(
        ghg_emissions_by_sector().loc[:, :, "CO2"].reset_coords(drop=True)
        * unit_conversion_t_mt()
        * if_then_else(
            select_gwp_time_frame_sp() == 1,
            lambda: float(gwp_20_year().loc["CO2"]),
            lambda: float(gwp_100_year().loc["CO2"]),
        )
        + ghg_emissions_by_sector().loc[:, :, "CH4"].reset_coords(drop=True)
        * unit_conversion_t_mt()
        * if_then_else(
            select_gwp_time_frame_sp() == 1,
            lambda: float(gwp_20_year().loc["CH4"]),
            lambda: float(gwp_100_year().loc["CH4"]),
        )
        + ghg_emissions_by_sector().loc[:, :, "N2O"].reset_coords(drop=True)
        * unit_conversion_t_mt()
        * if_then_else(
            select_gwp_time_frame_sp() == 1,
            lambda: float(gwp_20_year().loc["N2O"]),
            lambda: float(gwp_100_year().loc["N2O"]),
        ),
        output_real_9r(),
    )


@component.add(
    name="CO2e_intensity_of_final_energy",
    units="GtCO2eq/EJ",
    subscripts=["REGIONS_9_I", "NRG_FE_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_ghg_emissions": 1, "final_energy_demand_by_fe_ej_9r": 1},
)
def co2e_intensity_of_final_energy():
    return zidz(
        total_ghg_emissions().expand_dims({"NRG_FE_I": _subscript_dict["NRG_FE_I"]}, 1),
        final_energy_demand_by_fe_ej_9r(),
    )


@component.add(
    name="CO2e_intensity_of_final_energy_1R",
    units="GtCO2eq/EJ",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"co2e_intensity_of_final_energy": 1},
)
def co2e_intensity_of_final_energy_1r():
    """
    Total carbon dioxide equivalent intensity of final energy.
    """
    return sum(
        co2e_intensity_of_final_energy().rename(
            {"REGIONS_9_I": "REGIONS_9_I!", "NRG_FE_I": "NRG_FE_I!"}
        ),
        dim=["REGIONS_9_I!", "NRG_FE_I!"],
    )


@component.add(
    name="cumulative_FE_GDP_intensity_change_from_2015",
    units="1",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "fe_gdp_intensity": 1, "fe_gdp_intensity_until_2015": 1},
)
def cumulative_fe_gdp_intensity_change_from_2015():
    """
    Cumulative TFES intensity change from 2015.
    """
    return if_then_else(
        time() < 2015,
        lambda: xr.DataArray(
            0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
        ),
        lambda: -1 + fe_gdp_intensity() / fe_gdp_intensity_until_2015(),
    )


@component.add(
    name="cumulative_PE_GDP_intensity_change_from_2015",
    units="1",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "pe_gdp_intensity": 1, "pe_gdp_intensity_until_2015": 1},
)
def cumulative_pe_gdp_intensity_change_from_2015():
    """
    Cumulative TPES intensity change from 2015.
    """
    return if_then_else(
        time() < 2015,
        lambda: xr.DataArray(
            0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
        ),
        lambda: -1 + zidz(pe_gdp_intensity(), pe_gdp_intensity_until_2015()),
    )


@component.add(
    name="delayed_FE_GDP_intensity",
    units="TJ/Mdollars_2015",
    subscripts=["REGIONS_9_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_fe_gdp_intensity": 1},
    other_deps={
        "_delayfixed_delayed_fe_gdp_intensity": {
            "initial": {},
            "step": {"fe_gdp_intensity": 1},
        }
    },
)
def delayed_fe_gdp_intensity():
    return _delayfixed_delayed_fe_gdp_intensity()


_delayfixed_delayed_fe_gdp_intensity = DelayFixed(
    lambda: fe_gdp_intensity(),
    lambda: 1,
    lambda: xr.DataArray(
        0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
    ),
    time_step,
    "_delayfixed_delayed_fe_gdp_intensity",
)


@component.add(
    name="delayed_PE_GDP_intensity",
    units="TJ/Mdollars_2015",
    subscripts=["REGIONS_9_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_pe_gdp_intensity": 1},
    other_deps={
        "_delayfixed_delayed_pe_gdp_intensity": {
            "initial": {},
            "step": {"pe_gdp_intensity": 1},
        }
    },
)
def delayed_pe_gdp_intensity():
    return _delayfixed_delayed_pe_gdp_intensity()


_delayfixed_delayed_pe_gdp_intensity = DelayFixed(
    lambda: pe_gdp_intensity(),
    lambda: 1,
    lambda: xr.DataArray(
        0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
    ),
    time_step,
    "_delayfixed_delayed_pe_gdp_intensity",
)


@component.add(
    name="FE_GDP_intensity",
    units="TJ/Mdollars_2015",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "total_fe_energy_uses": 1,
        "unit_conversion_tj_ej": 1,
        "gdp_real_9r": 1,
    },
)
def fe_gdp_intensity():
    """
    Final energy vs GDP ratio per region.
    """
    return zidz(total_fe_energy_uses() * unit_conversion_tj_ej(), gdp_real_9r())


@component.add(
    name="FE_GDP_intensity_until_2015",
    units="TJ/Mdollars_2015",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "fe_gdp_intensity": 1, "auxiliary_fe_gdp_intensity": 1},
)
def fe_gdp_intensity_until_2015():
    """
    PE GDP intensity until the year 2015.
    """
    return if_then_else(
        time() < 2015, lambda: fe_gdp_intensity(), lambda: auxiliary_fe_gdp_intensity()
    )


@component.add(
    name="FE_including_trade_by_commodity_per_capita",
    units="GJ/(Year*person)",
    subscripts=["REGIONS_9_I", "NRG_FE_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "total_fe_including_net_trade": 1,
        "population_9_regions": 1,
        "unit_conversion_gj_ej": 1,
    },
)
def fe_including_trade_by_commodity_per_capita():
    return (
        zidz(
            total_fe_including_net_trade(),
            population_9_regions().expand_dims(
                {"NRG_FE_I": _subscript_dict["NRG_FE_I"]}, 1
            ),
        )
        * unit_conversion_gj_ej()
    )


@component.add(
    name="final_to_primary_energy_by_region",
    units="1",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "final_energy_demand_by_fe_9r": 1,
        "unit_conversion_tj_ej": 1,
        "pe_by_commodity": 1,
    },
)
def final_to_primary_energy_by_region():
    """
    Share of total final energy (excluing non-energy uses) vs total primary energy by region.
    """
    return zidz(
        sum(
            final_energy_demand_by_fe_9r().rename({"NRG_FE_I": "NRG_FE_I!"}),
            dim=["NRG_FE_I!"],
        )
        / unit_conversion_tj_ej(),
        sum(pe_by_commodity().rename({"NRG_PE_I": "NRG_PE_I!"}), dim=["NRG_PE_I!"]),
    )


@component.add(
    name="final_to_primary_energy_by_region_until_2015",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "aux_final_to_primary_energy_by_region_until_2015": 1,
        "final_to_primary_energy_by_region": 1,
    },
)
def final_to_primary_energy_by_region_until_2015():
    """
    final-to-primary energy ratio by region until the year 2015.
    """
    return if_then_else(
        time() > 2015,
        lambda: aux_final_to_primary_energy_by_region_until_2015(),
        lambda: final_to_primary_energy_by_region(),
    )


@component.add(
    name="final_to_primary_energy_world",
    units="1",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "final_energy_demand_by_fe_9r": 1,
        "unit_conversion_tj_ej": 1,
        "pe_by_commodity": 1,
    },
)
def final_to_primary_energy_world():
    """
    World share of total final energy (excluing non-energy uses) vs total primary energy.
    """
    return xr.DataArray(
        zidz(
            sum(
                final_energy_demand_by_fe_9r().rename(
                    {"REGIONS_9_I": "REGIONS_9_I!", "NRG_FE_I": "NRG_FE_I!"}
                ),
                dim=["REGIONS_9_I!", "NRG_FE_I!"],
            )
            / unit_conversion_tj_ej(),
            sum(
                pe_by_commodity().rename(
                    {"REGIONS_9_I": "REGIONS_9_I!", "NRG_PE_I": "NRG_PE_I!"}
                ),
                dim=["REGIONS_9_I!", "NRG_PE_I!"],
            ),
        ),
        {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
        ["REGIONS_9_I"],
    )


@component.add(
    name="GHG_emissions_all_sectors",
    units="Gt/Year",
    subscripts=["REGIONS_9_I", "GHG_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ghg_emissions_by_sector": 1, "unit_conversion_mt_gt": 1},
)
def ghg_emissions_all_sectors():
    return (
        sum(
            ghg_emissions_by_sector().rename({"SECTORS_I": "SECTORS_I!"}),
            dim=["SECTORS_I!"],
        )
        / unit_conversion_mt_gt()
    )


@component.add(
    name="GHG_emissions_per_capita_9R",
    units="t/(Year*person)",
    subscripts=["REGIONS_9_I", "GHG_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "total_ghg_energy_chain_emissions_9r": 3,
        "population_9_regions": 6,
        "unit_conversion_t_gt": 3,
        "pfc_emissions": 1,
        "global_sf6_emissions": 1,
        "global_hfc_emissions": 1,
    },
)
def ghg_emissions_per_capita_9r():
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "GHG_I": _subscript_dict["GHG_I"],
        },
        ["REGIONS_9_I", "GHG_I"],
    )
    value.loc[:, ["CO2"]] = (
        (
            zidz(
                total_ghg_energy_chain_emissions_9r()
                .loc[:, "CO2"]
                .reset_coords(drop=True),
                population_9_regions(),
            )
            * unit_conversion_t_gt()
        )
        .expand_dims({"GHG_ENERGY_USE_I": ["CO2"]}, 1)
        .values
    )
    value.loc[:, ["CH4"]] = (
        (
            zidz(
                total_ghg_energy_chain_emissions_9r()
                .loc[:, "CH4"]
                .reset_coords(drop=True),
                population_9_regions(),
            )
            * unit_conversion_t_gt()
        )
        .expand_dims({"GHG_ENERGY_USE_I": ["CH4"]}, 1)
        .values
    )
    value.loc[:, ["N2O"]] = (
        (
            zidz(
                total_ghg_energy_chain_emissions_9r()
                .loc[:, "N2O"]
                .reset_coords(drop=True),
                population_9_regions(),
            )
            * unit_conversion_t_gt()
        )
        .expand_dims({"GHG_ENERGY_USE_I": ["N2O"]}, 1)
        .values
    )
    value.loc[:, ["PFCs"]] = (
        zidz(pfc_emissions(), population_9_regions())
        .expand_dims({"GHG_I": ["PFCs"]}, 1)
        .values
    )
    value.loc[:, ["SF6"]] = (
        zidz(
            xr.DataArray(
                global_sf6_emissions(),
                {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
                ["REGIONS_9_I"],
            ),
            population_9_regions(),
        )
        .expand_dims({"GHG_I": ["SF6"]}, 1)
        .values
    )
    value.loc[:, _subscript_dict["HFC_TYPE_I"]] = (
        zidz(
            global_hfc_emissions().expand_dims(
                {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, 1
            ),
            population_9_regions().expand_dims(
                {"HFC_TYPE_I": _subscript_dict["HFC_TYPE_I"]}, 0
            ),
        )
        .transpose("REGIONS_9_I", "HFC_TYPE_I")
        .values
    )
    return value


@component.add(
    name="GHG_emissions_sectors_and_households",
    units="Gt/Year",
    subscripts=["REGIONS_9_I", "GHG_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "ghg_emissions_all_sectors": 1,
        "households_end_use_energy_emissions_9r": 1,
        "unit_conversion_mt_gt": 1,
    },
)
def ghg_emissions_sectors_and_households():
    return (
        ghg_emissions_all_sectors()
        + households_end_use_energy_emissions_9r() / unit_conversion_mt_gt()
    )


@component.add(
    name="GHG_intensity_of_final_energy",
    units="Mt/EJ",
    subscripts=["REGIONS_9_I", "NRG_FE_I", "GHG_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "total_ghg_energy_chain_emissions_9r": 1,
        "final_energy_demand_by_fe_ej_9r": 1,
    },
)
def ghg_intensity_of_final_energy():
    return zidz(
        total_ghg_energy_chain_emissions_9r().expand_dims(
            {"NRG_FE_I": _subscript_dict["NRG_FE_I"]}, 2
        ),
        final_energy_demand_by_fe_ej_9r().expand_dims(
            {"GHG_I": _subscript_dict["GHG_I"]}, 1
        ),
    ).transpose("REGIONS_9_I", "NRG_FE_I", "GHG_I")


@component.add(
    name="INITIAL_PROSTO_DEDICATED_CAPACITY_EXPANSION",
    units="DMNL",
    subscripts=["REGIONS_9_I", "PROSTO_ELEC_DEDICATED_I"],
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_initial_prosto_dedicated_capacity_expansion": 1},
    other_deps={
        "_initial_initial_prosto_dedicated_capacity_expansion": {
            "initial": {"prosto_dedicated_capacity_expansion": 1},
            "step": {},
        }
    },
)
def initial_prosto_dedicated_capacity_expansion():
    return _initial_initial_prosto_dedicated_capacity_expansion()


_initial_initial_prosto_dedicated_capacity_expansion = Initial(
    lambda: prosto_dedicated_capacity_expansion(),
    "_initial_initial_prosto_dedicated_capacity_expansion",
)


@component.add(
    name="INITIAL_PROTRA_CAPACITY_EXPANSION",
    units="DMNL",
    subscripts=["REGIONS_9_I", "NRG_TO_I", "NRG_PROTRA_I"],
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_initial_protra_capacity_expansion": 1},
    other_deps={
        "_initial_initial_protra_capacity_expansion": {
            "initial": {"protra_capacity_expansion": 1},
            "step": {},
        }
    },
)
def initial_protra_capacity_expansion():
    return _initial_initial_protra_capacity_expansion()


_initial_initial_protra_capacity_expansion = Initial(
    lambda: protra_capacity_expansion(), "_initial_initial_protra_capacity_expansion"
)


@component.add(
    name="INITIAL_SHARE_NEW_PV_SUBTECHN_LAND",
    units="DMNL",
    subscripts=["REGIONS_9_I", "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"],
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_initial_share_new_pv_subtechn_land": 1},
    other_deps={
        "_initial_initial_share_new_pv_subtechn_land": {
            "initial": {"share_new_pv_subtechn_land": 1},
            "step": {},
        }
    },
)
def initial_share_new_pv_subtechn_land():
    return _initial_initial_share_new_pv_subtechn_land()


_initial_initial_share_new_pv_subtechn_land = Initial(
    lambda: share_new_pv_subtechn_land(), "_initial_initial_share_new_pv_subtechn_land"
)


@component.add(
    name="INITIAL_SHARE_NEW_PV_SUBTECHN_URBAN",
    units="DMNL",
    subscripts=["REGIONS_9_I", "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"],
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_initial_share_new_pv_subtechn_urban": 1},
    other_deps={
        "_initial_initial_share_new_pv_subtechn_urban": {
            "initial": {"share_new_pv_subtechn_urban": 1},
            "step": {},
        }
    },
)
def initial_share_new_pv_subtechn_urban():
    return _initial_initial_share_new_pv_subtechn_urban()


_initial_initial_share_new_pv_subtechn_urban = Initial(
    lambda: share_new_pv_subtechn_urban(),
    "_initial_initial_share_new_pv_subtechn_urban",
)


@component.add(
    name="INITIAL_SHARE_PV_CAPACITY_BY_SUBTECHNOLOGY",
    units="DMNL",
    subscripts=[
        "REGIONS_9_I",
        "PROTRA_PP_SOLAR_PV_I",
        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I",
    ],
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_initial_share_pv_capacity_by_subtechnology": 1},
    other_deps={
        "_initial_initial_share_pv_capacity_by_subtechnology": {
            "initial": {"share_pv_capacity_by_subtechnology": 1},
            "step": {},
        }
    },
)
def initial_share_pv_capacity_by_subtechnology():
    return _initial_initial_share_pv_capacity_by_subtechnology()


_initial_initial_share_pv_capacity_by_subtechnology = Initial(
    lambda: share_pv_capacity_by_subtechnology(),
    "_initial_initial_share_pv_capacity_by_subtechnology",
)


@component.add(
    name="investment_costs_PROTRA_vs_GDP",
    units="1",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "total_protra_investment_cost_35r": 1,
        "gross_domestic_product_real_supply_side": 1,
    },
)
def investment_costs_protra_vs_gdp():
    return zidz(
        total_protra_investment_cost_35r(), gross_domestic_product_real_supply_side()
    )


@component.add(
    name="LUE_solar_PV_by_technology_per_ha",
    units="ha/MW",
    subscripts=["REGIONS_36_I", "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"lue_solar_pv_by_technology": 1, "unit_conversion_km2_ha": 1},
)
def lue_solar_pv_by_technology_per_ha():
    """
    Land use efficiency of solar PV by technology in ha/MW.
    """
    return zidz(
        xr.DataArray(
            1,
            {
                "REGIONS_36_I": _subscript_dict["REGIONS_36_I"],
                "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": _subscript_dict[
                    "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"
                ],
            },
            ["REGIONS_36_I", "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"],
        ),
        lue_solar_pv_by_technology() * unit_conversion_km2_ha(),
    )


@component.add(
    name="net_TFEC_energy_uses",
    units="EJ/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_fe_energy_uses": 1, "fenust_system": 1},
)
def net_tfec_energy_uses():
    """
    Net total final energy consumption (final energy minus energy invested to produce energy).
    """
    return total_fe_energy_uses() - fenust_system()


@component.add(
    name="net_TFEC_energy_uses_per_capita",
    units="GJ/(Year*person)",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "net_tfec_energy_uses": 1,
        "unit_conversion_gj_ej": 1,
        "population_9_regions": 1,
    },
)
def net_tfec_energy_uses_per_capita():
    """
    Net total final energy consumption per capita.
    """
    return zidz(
        net_tfec_energy_uses() * unit_conversion_gj_ej(), population_9_regions()
    )


@component.add(
    name="passengers_transport_real_1R",
    units="km*person",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"passenger_transport_real_supply_by_mode": 1},
)
def passengers_transport_real_1r():
    """
    Transport supply after all policy and endogenous modifications, in persons*km.
    """
    return sum(
        passenger_transport_real_supply_by_mode().rename(
            {
                "REGIONS_35_I": "REGIONS_35_I!",
                "PASSENGERS_TRANSPORT_MODE_I": "PASSENGERS_TRANSPORT_MODE_I!",
                "HOUSEHOLDS_I": "HOUSEHOLDS_I!",
            }
        ),
        dim=["REGIONS_35_I!", "PASSENGERS_TRANSPORT_MODE_I!", "HOUSEHOLDS_I!"],
    )


@component.add(
    name="PE_by_commodity_per_capita",
    units="GJ/(Year*person)",
    subscripts=["REGIONS_9_I", "NRG_PE_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "pe_by_commodity": 1,
        "population_9_regions": 1,
        "unit_conversion_gj_ej": 1,
    },
)
def pe_by_commodity_per_capita():
    return (
        zidz(
            pe_by_commodity(),
            population_9_regions().expand_dims(
                {"NRG_PE_I": _subscript_dict["NRG_PE_I"]}, 1
            ),
        )
        * unit_conversion_gj_ej()
    )


@component.add(
    name="PE_GDP_intensity",
    units="TJ/Mdollars_2015",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_pe_by_region": 1, "unit_conversion_tj_ej": 1, "gdp_real_9r": 1},
)
def pe_gdp_intensity():
    """
    Primary energy vs GDP ratio per region.
    """
    return zidz(total_pe_by_region() * unit_conversion_tj_ej(), gdp_real_9r())


@component.add(
    name="PE_GDP_intensity_until_2015",
    units="TJ/Mdollars_2015",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "pe_gdp_intensity": 1, "auxiliary_pe_gdp_intensity": 1},
)
def pe_gdp_intensity_until_2015():
    """
    PE GDP intensity until the year 2015.
    """
    return if_then_else(
        time() < 2015, lambda: pe_gdp_intensity(), lambda: auxiliary_pe_gdp_intensity()
    )


@component.add(
    name="PE_total_world",
    units="EJ/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_pe_by_region": 1},
)
def pe_total_world():
    """
    Total world domestic primary energy consumption.
    """
    return sum(
        total_pe_by_region().rename({"REGIONS_9_I": "REGIONS_9_I!"}),
        dim=["REGIONS_9_I!"],
    )


@component.add(
    name="physical_energy_intensity_TPE_vs_net_energy_uses",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"share_total_net_energy_vs_tpe_energy_uses": 1},
)
def physical_energy_intensity_tpe_vs_net_energy_uses():
    """
    Physical energy intensity
    """
    return zidz(
        xr.DataArray(
            1, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
        ),
        share_total_net_energy_vs_tpe_energy_uses(),
    )


@component.add(
    name="physical_energy_intensity_TPES_vs_final",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"final_to_primary_energy_by_region": 1},
)
def physical_energy_intensity_tpes_vs_final():
    """
    Physical energy intensity by region.
    """
    return zidz(
        xr.DataArray(
            1, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
        ),
        final_to_primary_energy_by_region(),
    )


@component.add(
    name="power_density_solar_PV_by_technology",
    units="w/m2",
    subscripts=["REGIONS_35_I", "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "lue_solar_pv_by_technology": 2,
        "cf_protra": 2,
        "unit_conversion_w_mw": 2,
        "unit_conversion_m2_km2": 2,
    },
)
def power_density_solar_pv_by_technology():
    """
    Land use efficiency of solar PV by technology in power density terms, ie. We/m2 (1 We = 8760 Wh).
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": _subscript_dict[
                "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"
            ],
        },
        ["REGIONS_35_I", "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"],
    )
    value.loc[_subscript_dict["REGIONS_8_I"], :] = (
        lue_solar_pv_by_technology()
        .loc[_subscript_dict["REGIONS_8_I"], :]
        .rename({"REGIONS_36_I": "REGIONS_8_I"})
        * cf_protra()
        .loc[_subscript_dict["REGIONS_8_I"], "TO_elec", "PROTRA_PP_solar_open_space_PV"]
        .reset_coords(drop=True)
        .rename({"REGIONS_9_I": "REGIONS_8_I"})
        * (unit_conversion_w_mw() / unit_conversion_m2_km2())
    ).values
    value.loc[_subscript_dict["REGIONS_EU27_I"], :] = (
        lue_solar_pv_by_technology()
        .loc[_subscript_dict["REGIONS_EU27_I"], :]
        .rename({"REGIONS_36_I": "REGIONS_EU27_I"})
        * float(cf_protra().loc["EU27", "TO_elec", "PROTRA_PP_solar_open_space_PV"])
        * (unit_conversion_w_mw() / unit_conversion_m2_km2())
    ).values
    return value


@component.add(
    name="PROTRA_capacity_stock_1R",
    units="TW",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"protra_capacity_stock": 1},
)
def protra_capacity_stock_1r():
    """
    Capacity stock of TI-TO transformation technology capacities by TO (PROTRA)
    """
    return sum(
        protra_capacity_stock().rename(
            {
                "REGIONS_9_I": "REGIONS_9_I!",
                "NRG_TO_I": "NRG_TO_I!",
                "NRG_PROTRA_I": "NRG_PROTRA_I!",
            }
        ),
        dim=["REGIONS_9_I!", "NRG_TO_I!", "NRG_PROTRA_I!"],
    )


@component.add(
    name="PROTRA_capacity_stock_total_TO",
    units="TW",
    subscripts=["REGIONS_9_I", "NRG_PROTRA_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"protra_capacity_stock": 1},
)
def protra_capacity_stock_total_to():
    return sum(
        protra_capacity_stock().rename({"NRG_TO_I": "NRG_TO_I!"}), dim=["NRG_TO_I!"]
    )


@component.add(
    name="public_vehicle_fleet_EU27",
    units="vehicles",
    subscripts=["TRANSPORT_POWER_TRAIN_I", "PUBLIC_TRANSPORT_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"public_passenger_vehicle_fleet": 1},
)
def public_vehicle_fleet_eu27():
    return sum(
        public_passenger_vehicle_fleet()
        .loc[_subscript_dict["REGIONS_EU27_I"], :, :, :]
        .rename({"REGIONS_35_I": "REGIONS_EU27_I!", "HOUSEHOLDS_I": "HOUSEHOLDS_I!"}),
        dim=["REGIONS_EU27_I!", "HOUSEHOLDS_I!"],
    )


@component.add(
    name="required_embodied_PE_materials_BU",
    units="EJ/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "required_embodied_fe_materials_for_protra": 1,
        "required_embodied_pe_materials_for_ev_batteries_9r": 1,
        "required_embodied_fe_materials_for_new_grids": 1,
    },
)
def required_embodied_pe_materials_bu():
    """
    Total required embodied primary energy of total material consumption for BU technologies (PROTRA, PROSUP and electric transport).
    """
    return (
        required_embodied_fe_materials_for_protra()
        + sum(
            required_embodied_pe_materials_for_ev_batteries_9r().rename(
                {"EV_BATTERIES_I": "EV_BATTERIES_I!"}
            ),
            dim=["EV_BATTERIES_I!"],
        )
        + sum(
            required_embodied_fe_materials_for_new_grids().rename(
                {"NRG_PROTRA_I": "NRG_PROTRA_I!"}
            ),
            dim=["NRG_PROTRA_I!"],
        )
    )


@component.add(
    name="share_FE_demand_commodity",
    units="1",
    subscripts=["REGIONS_9_I", "NRG_FE_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"fe_excluding_trade": 2},
)
def share_fe_demand_commodity():
    """
    Share for each final energy (FE, demand) by region over the total FE demand (including energy and non-energy uses).
    """
    return zidz(
        fe_excluding_trade(),
        sum(
            fe_excluding_trade().rename({"NRG_FE_I": "NRG_FE_I!"}), dim=["NRG_FE_I!"]
        ).expand_dims({"NRG_FE_I": _subscript_dict["NRG_FE_I"]}, 1),
    )


@component.add(
    name="share_required_embodied_PE_materials_BU_vs_PE_total",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"required_embodied_pe_materials_bu": 1, "total_pe_by_region": 1},
)
def share_required_embodied_pe_materials_bu_vs_pe_total():
    """
    Share of required embodied primary energy of total material consumption for BU technologies (PROTRA, PROSUP and electric transport) vs total primary energy.
    """
    return zidz(required_embodied_pe_materials_bu(), total_pe_by_region())


@component.add(
    name="share_RES_in_PE",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"pe_by_commodity": 2},
)
def share_res_in_pe():
    """
    Share of renewable energies in total primary energy (including non-energy uses).
    """
    return zidz(
        sum(
            pe_by_commodity()
            .loc[:, _subscript_dict["NRG_PE_RES_I"]]
            .rename({"NRG_PE_I": "NRG_PE_RES_I!"}),
            dim=["NRG_PE_RES_I!"],
        ),
        sum(pe_by_commodity().rename({"NRG_PE_I": "NRG_PE_I!"}), dim=["NRG_PE_I!"]),
    )


@component.add(
    name="share_RES_vs_TO_elec",
    units="1",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"protra_to_allocated": 2},
)
def share_res_vs_to_elec():
    """
    Share renewables in electricity generation.
    """
    return zidz(
        sum(
            protra_to_allocated()
            .loc[:, "TO_elec", _subscript_dict["PROTRA_RES_I"]]
            .reset_coords(drop=True)
            .rename({"NRG_PROTRA_I": "PROTRA_RES_I!"}),
            dim=["PROTRA_RES_I!"],
        ),
        sum(
            protra_to_allocated()
            .loc[:, "TO_elec", :]
            .reset_coords(drop=True)
            .rename({"NRG_PROTRA_I": "NRG_PROTRA_I!"}),
            dim=["NRG_PROTRA_I!"],
        ),
    )


@component.add(
    name="share_TO_by_commodity",
    units="1",
    subscripts=["REGIONS_9_I", "NRG_TO_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"to_by_commodity": 2},
)
def share_to_by_commodity():
    """
    Share for each transformation output (TO, production) by region over the total TO.
    """
    return zidz(
        to_by_commodity(),
        sum(
            to_by_commodity().rename({"NRG_TO_I": "NRG_TO_I!"}), dim=["NRG_TO_I!"]
        ).expand_dims({"NRG_TO_I": _subscript_dict["NRG_TO_I"]}, 1),
    )


@component.add(
    name="share_TO_elec_CHP_plants",
    units="1",
    subscripts=["REGIONS_9_I", "PROTRA_CHP_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"protra_to_allocated": 3},
)
def share_to_elec_chp_plants():
    """
    Share of electricity generation in CHP plants vs total generated (electricity + heat).
    """
    return zidz(
        protra_to_allocated()
        .loc[:, "TO_elec", _subscript_dict["PROTRA_CHP_I"]]
        .reset_coords(drop=True)
        .rename({"NRG_PROTRA_I": "PROTRA_CHP_I"}),
        protra_to_allocated()
        .loc[:, "TO_elec", _subscript_dict["PROTRA_CHP_I"]]
        .reset_coords(drop=True)
        .rename({"NRG_PROTRA_I": "PROTRA_CHP_I"})
        + protra_to_allocated()
        .loc[:, "TO_heat", _subscript_dict["PROTRA_CHP_I"]]
        .reset_coords(drop=True)
        .rename({"NRG_PROTRA_I": "PROTRA_CHP_I"}),
    )


@component.add(
    name="share_total_net_energy_vs_TPE_energy_uses",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"net_tfec_energy_uses": 1, "total_pe_energy_uses": 1},
)
def share_total_net_energy_vs_tpe_energy_uses():
    """
    Share of total net final energy vs total primary energy supply (without accounting for non-energy uses).
    """
    return zidz(net_tfec_energy_uses(), total_pe_energy_uses())


@component.add(
    name="share_total_PROSTO_losses_vs_TO",
    units="DMNL",
    subscripts=["REGIONS_9_I", "NRG_TO_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"prosup_storage_losses": 1, "to_by_commodity": 1},
)
def share_total_prosto_losses_vs_to():
    """
    Share of total storage losses by utility-scale facilities and the transformation outputs.
    """
    return zidz(prosup_storage_losses(), to_by_commodity())


@component.add(
    name="share_VRES_vs_RES_TO_elec",
    units="1",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"protra_to_allocated": 2},
)
def share_vres_vs_res_to_elec():
    """
    Share variable renewables in renewable electricity generation.
    """
    return zidz(
        sum(
            protra_to_allocated()
            .loc[:, "TO_elec", _subscript_dict["PROTRA_VRES_I"]]
            .reset_coords(drop=True)
            .rename({"NRG_PROTRA_I": "PROTRA_VRES_I!"}),
            dim=["PROTRA_VRES_I!"],
        ),
        sum(
            protra_to_allocated()
            .loc[:, "TO_elec", _subscript_dict["PROTRA_RES_I"]]
            .reset_coords(drop=True)
            .rename({"NRG_PROTRA_I": "PROTRA_RES_I!"}),
            dim=["PROTRA_RES_I!"],
        ),
    )


@component.add(
    name="share_VRES_vs_TO_elec",
    units="1",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"protra_to_allocated": 2},
)
def share_vres_vs_to_elec():
    """
    Share variable renewables in electricity generation.
    """
    return zidz(
        sum(
            protra_to_allocated()
            .loc[:, "TO_elec", _subscript_dict["PROTRA_VRES_I"]]
            .reset_coords(drop=True)
            .rename({"NRG_PROTRA_I": "PROTRA_VRES_I!"}),
            dim=["PROTRA_VRES_I!"],
        ),
        sum(
            protra_to_allocated()
            .loc[:, "TO_elec", :]
            .reset_coords(drop=True)
            .rename({"NRG_PROTRA_I": "NRG_PROTRA_I!"}),
            dim=["NRG_PROTRA_I!"],
        ),
    )


@component.add(
    name="total_CO2_emissions_PE",
    units="Mt/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_co2_emissions_pe_combustion": 1},
)
def total_co2_emissions_pe():
    """
    CO2 emissions PE.
    """
    return total_co2_emissions_pe_combustion()


@component.add(
    name="total_CO2_emissions_PE_combustion",
    units="Mt/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "co2_emissions_pe_combustion_before_ccs": 1,
        "co2_emissions_captured_ccs": 1,
    },
)
def total_co2_emissions_pe_combustion():
    """
    CO2 emissions PE combustion accounting for CCS.
    """
    return (
        sum(
            co2_emissions_pe_combustion_before_ccs().rename({"NRG_PE_I": "NRG_PE_I!"}),
            dim=["NRG_PE_I!"],
        )
        - co2_emissions_captured_ccs()
    )


@component.add(
    name="total_CO2e_emissions_per_capita_1R",
    units="t/(Year*person)",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_co2e_emissions_per_capita_9r": 1},
)
def total_co2e_emissions_per_capita_1r():
    """
    Total world emissions of carbon dioxide equivalent.
    """
    return (
        sum(
            total_co2e_emissions_per_capita_9r().rename(
                {"REGIONS_9_I": "REGIONS_9_I!"}
            ),
            dim=["REGIONS_9_I!"],
        )
        / 9
    )


@component.add(
    name="total_CO2e_emissions_per_capita_9R",
    units="t/(Year*person)",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "total_ghg_emissions": 1,
        "population_9_regions": 1,
        "unit_conversion_t_gt": 1,
    },
)
def total_co2e_emissions_per_capita_9r():
    """
    total_CO2e_emissions_per_capita_9R
    """
    return zidz(total_ghg_emissions(), population_9_regions()) * unit_conversion_t_gt()


@component.add(
    name="total_energy_capacities_investment_costs_vs_GDP",
    units="1",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_energy_capacities_investment_cost": 1, "gdp_real_9r": 1},
)
def total_energy_capacities_investment_costs_vs_gdp():
    return zidz(total_energy_capacities_investment_cost(), gdp_real_9r())


@component.add(
    name="total_energy_consumption_passengers_transport_1S",
    units="EJ",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_energy_consumption_passenger_transport": 1},
)
def total_energy_consumption_passengers_transport_1s():
    """
    Total energy passengers transport consumption of final energy in EJ.
    """
    return sum(
        total_energy_consumption_passenger_transport().rename(
            {"NRG_FE_I": "NRG_FE_I!"}
        ),
        dim=["NRG_FE_I!"],
    )


@component.add(
    name="total_FE_energy_uses",
    units="EJ/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"final_energy_demand_by_fe_9r": 1, "unit_conversion_tj_ej": 1},
)
def total_fe_energy_uses():
    """
    Total final energy demand for 9 regions (not including non-energy uses).
    """
    return (
        sum(
            final_energy_demand_by_fe_9r().rename({"NRG_FE_I": "NRG_FE_I!"}),
            dim=["NRG_FE_I!"],
        )
        / unit_conversion_tj_ej()
    )


@component.add(
    name="total_FE_including_trade_per_capita",
    units="GJ/(Year*person)",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "total_fe_including_net_trade": 1,
        "population_9_regions": 1,
        "unit_conversion_gj_ej": 1,
    },
)
def total_fe_including_trade_per_capita():
    return (
        zidz(
            sum(
                total_fe_including_net_trade().rename({"NRG_FE_I": "NRG_FE_I!"}),
                dim=["NRG_FE_I!"],
            ),
            population_9_regions(),
        )
        * unit_conversion_gj_ej()
    )


@component.add(
    name="total_FE_including_trade_per_capita_1R",
    units="GJ/(Year*person)",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_fe_including_trade_per_capita": 1},
)
def total_fe_including_trade_per_capita_1r():
    """
    Total iron includin trade per capita.
    """
    return sum(
        total_fe_including_trade_per_capita().rename({"REGIONS_9_I": "REGIONS_9_I!"}),
        dim=["REGIONS_9_I!"],
    )


@component.add(
    name="total_FE_per_capita",
    units="GJ/(Year*person)",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_fe_including_trade_per_capita": 1},
)
def total_fe_per_capita():
    """
    total_FE_per_capita
    """
    return total_fe_including_trade_per_capita()


@component.add(
    name="total_final_energy_demand_by_FE",
    units="TJ/Year",
    subscripts=["REGIONS_9_I", "NRG_FE_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "final_energy_demand_by_fe_9r": 1,
        "final_non_energy_demand_by_fe_9r": 1,
    },
)
def total_final_energy_demand_by_fe():
    return final_energy_demand_by_fe_9r() + final_non_energy_demand_by_fe_9r()


@component.add(
    name="total_final_energy_intensities_1R_1S",
    units="TJ/million$",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_final_energy_intensities_by_sector": 1},
)
def total_final_energy_intensities_1r_1s():
    """
    Final energy intensities estimated with a top-down approach
    """
    return sum(
        total_final_energy_intensities_by_sector().rename(
            {
                "REGIONS_35_I": "REGIONS_35_I!",
                "SECTORS_NON_ENERGY_I": "SECTORS_NON_ENERGY_I!",
            }
        ),
        dim=["REGIONS_35_I!", "SECTORS_NON_ENERGY_I!"],
    )


@component.add(
    name="total_PE_energy_uses",
    units="EJ/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "pe_by_commodity": 1,
        "total_final_energy_demand_by_fe": 1,
        "final_energy_demand_by_fe_9r": 1,
    },
)
def total_pe_energy_uses():
    """
    Approximation to estimate the total amount of PE for energy uses,taking as proxy the share of energy vs non-energy final energy demand.
    """
    return sum(
        pe_by_commodity().rename({"NRG_PE_I": "NRG_PE_I!"}), dim=["NRG_PE_I!"]
    ) * zidz(
        sum(
            final_energy_demand_by_fe_9r().rename({"NRG_FE_I": "NRG_FE_I!"}),
            dim=["NRG_FE_I!"],
        ),
        sum(
            total_final_energy_demand_by_fe().rename({"NRG_FE_I": "NRG_FE_I!"}),
            dim=["NRG_FE_I!"],
        ),
    )


@component.add(
    name="total_PE_per_region_per_capita",
    units="GJ/(Year*person)",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "total_pe_by_region": 1,
        "population_9_regions": 1,
        "unit_conversion_gj_ej": 1,
    },
)
def total_pe_per_region_per_capita():
    return zidz(total_pe_by_region(), population_9_regions()) * unit_conversion_gj_ej()


@component.add(
    name="total_PROTRA_CO2_emissions",
    units="Mt/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"co2_emissions_by_protra": 1},
)
def total_protra_co2_emissions():
    """
    Total CO2 emissions in process transformations.
    """
    return sum(
        co2_emissions_by_protra().rename({"NRG_PROTRA_I": "NRG_PROTRA_I!"}),
        dim=["NRG_PROTRA_I!"],
    )


@component.add(
    name="total_public_vehicle_fleet_9R",
    units="vehicles",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"public_passenger_vehicle_fleet": 1, "public_vehicle_fleet_eu27": 1},
)
def total_public_vehicle_fleet_9r():
    value = xr.DataArray(
        np.nan, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
    )
    value.loc[_subscript_dict["REGIONS_8_I"]] = sum(
        public_passenger_vehicle_fleet()
        .loc[_subscript_dict["REGIONS_8_I"], :, :, :]
        .rename(
            {
                "REGIONS_35_I": "REGIONS_8_I",
                "TRANSPORT_POWER_TRAIN_I": "TRANSPORT_POWER_TRAIN_I!",
                "PUBLIC_TRANSPORT_I": "PUBLIC_TRANSPORT_I!",
                "HOUSEHOLDS_I": "HOUSEHOLDS_I!",
            }
        ),
        dim=["TRANSPORT_POWER_TRAIN_I!", "PUBLIC_TRANSPORT_I!", "HOUSEHOLDS_I!"],
    ).values
    value.loc[["EU27"]] = sum(
        public_vehicle_fleet_eu27().rename(
            {
                "TRANSPORT_POWER_TRAIN_I": "TRANSPORT_POWER_TRAIN_I!",
                "PUBLIC_TRANSPORT_I": "PUBLIC_TRANSPORT_I!",
            }
        ),
        dim=["TRANSPORT_POWER_TRAIN_I!", "PUBLIC_TRANSPORT_I!"],
    )
    return value


@component.add(
    name="world_FE_energy_uses",
    units="EJ/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_fe_energy_uses": 1},
)
def world_fe_energy_uses():
    return sum(
        total_fe_energy_uses().rename({"REGIONS_9_I": "REGIONS_9_I!"}),
        dim=["REGIONS_9_I!"],
    )


@component.add(
    name="world_final_energy_demand_sectors",
    units="EJ/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"world_final_energy_demand_sectors_by_fe": 1},
)
def world_final_energy_demand_sectors():
    """
    Global final energy demand (energy uses) from sectors.
    """
    return sum(
        world_final_energy_demand_sectors_by_fe().rename({"NRG_FE_I": "NRG_FE_I!"}),
        dim=["NRG_FE_I!"],
    )


@component.add(
    name="world_final_energy_demand_sectors_by_FE",
    units="EJ/Year",
    subscripts=["NRG_FE_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"final_energy_demand_by_sector_and_fe": 1, "unit_conversion_tj_ej": 1},
)
def world_final_energy_demand_sectors_by_fe():
    """
    Global final energy demand (energy uses) from sectors by type of final energy.
    """
    return (
        sum(
            final_energy_demand_by_sector_and_fe().rename(
                {
                    "REGIONS_35_I": "REGIONS_35_I!",
                    "SECTORS_NON_ENERGY_I": "SECTORS_NON_ENERGY_I!",
                }
            ),
            dim=["REGIONS_35_I!", "SECTORS_NON_ENERGY_I!"],
        )
        / unit_conversion_tj_ej()
    )


@component.add(
    name="world_final_non_energy_demand",
    units="EJ/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"world_final_non_energy_demand_by_sectors_and_fe": 1},
)
def world_final_non_energy_demand():
    """
    Global final energy demand (non-energy uses) from sectors.
    """
    return sum(
        world_final_non_energy_demand_by_sectors_and_fe().rename(
            {"NRG_FE_I": "NRG_FE_I!"}
        ),
        dim=["NRG_FE_I!"],
    )


@component.add(
    name="world_final_non_energy_demand_by_sectors_and_FE",
    units="EJ/Year",
    subscripts=["NRG_FE_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "final_non_energy_demand_by_sectors_and_fe": 1,
        "unit_conversion_tj_ej": 1,
    },
)
def world_final_non_energy_demand_by_sectors_and_fe():
    """
    Global final energy demand (non-energy uses) from sectors by type of final energy.
    """
    return (
        sum(
            final_non_energy_demand_by_sectors_and_fe().rename(
                {"REGIONS_35_I": "REGIONS_35_I!", "SECTORS_I": "SECTORS_I!"}
            ),
            dim=["REGIONS_35_I!", "SECTORS_I!"],
        )
        / unit_conversion_tj_ej()
    )


@component.add(
    name="world_households_final_energy_demand_by_FE",
    units="EJ/Year",
    subscripts=["NRG_FE_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"households_final_energy_demand_by_fe": 1, "unit_conversion_tj_ej": 1},
)
def world_households_final_energy_demand_by_fe():
    """
    Global final energy demand from households by type of final energy.
    """
    return (
        sum(
            households_final_energy_demand_by_fe().rename(
                {"REGIONS_35_I": "REGIONS_35_I!"}
            ),
            dim=["REGIONS_35_I!"],
        )
        / unit_conversion_tj_ej()
    )


@component.add(
    name="world_households_total_final_energy_demand",
    units="EJ/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"world_households_final_energy_demand_by_fe": 1},
)
def world_households_total_final_energy_demand():
    """
    Global final energy demand from households.
    """
    return sum(
        world_households_final_energy_demand_by_fe().rename({"NRG_FE_I": "NRG_FE_I!"}),
        dim=["NRG_FE_I!"],
    )
