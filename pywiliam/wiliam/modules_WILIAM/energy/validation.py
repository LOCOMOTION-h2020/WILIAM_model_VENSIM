"""
Module energy.validation
Translated using PySD version 3.10.0
"""


@component.add(
    name="check_energy_capacity_expansion_deficit",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_COMMODITIES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "to_shortfall": 1,
        "protra_heat_shortfall_allocation": 1,
        "remaining_elec_shortfall_to_be_allocated": 1,
        "protra_elec_shortfall_allocation": 1,
    },
)
def check_energy_capacity_expansion_deficit():
    """
    Variable to detect if there is deficit in the capacity expansion (in energy terms) demanded (FE) scarcity by region and TO type.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "NRG_COMMODITIES_I": _subscript_dict["NRG_COMMODITIES_I"],
        },
        ["REGIONS_9_I", "NRG_COMMODITIES_I"],
    )
    value.loc[:, ["TO_heat"]] = (
        (
            to_shortfall().loc[:, "TO_heat"].reset_coords(drop=True)
            - sum(
                protra_heat_shortfall_allocation()
                .loc[:, "TO_heat", :]
                .reset_coords(drop=True)
                .rename({"NRG_PRO_I": "NRG_PRO_I!"}),
                dim=["NRG_PRO_I!"],
            )
        )
        .expand_dims({"NRG_COMMODITIES_I": ["TO_heat"]}, 1)
        .values
    )
    value.loc[:, ["TO_elec"]] = (
        (
            remaining_elec_shortfall_to_be_allocated()
            .loc[:, "TO_elec"]
            .reset_coords(drop=True)
            - sum(
                protra_elec_shortfall_allocation()
                .loc[:, "TO_elec", :]
                .reset_coords(drop=True)
                .rename({"NRG_PRO_I": "NRG_PRO_I!"}),
                dim=["NRG_PRO_I!"],
            )
        )
        .expand_dims({"NRG_COMMODITIES_I": ["TO_elec"]}, 1)
        .values
    )
    return value


@component.add(
    name="CHECK_GDC_IEA_model_by_commodity_world",
    units="EJ/Year",
    subscripts=["NRG_PE_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"world_pe_by_commodity": 1, "iea_world_pe_by_commodity": 1},
)
def check_gdc_iea_model_by_commodity_world():
    """
    Check-varaible comparing historic and calculate gross domestic consumption (PE); pos: model > empiric (overestimation) neg: empiric > model (understimation)
    """
    return world_pe_by_commodity() - iea_world_pe_by_commodity()


@component.add(
    name="CHECK_GDC_IEA_model_by_region",
    units="EJ/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_pe_by_region": 1, "iea_pe_total": 1},
)
def check_gdc_iea_model_by_region():
    """
    Check-varaible comparing historic and calculate gross domestic consumption (PE); Check-varaible comparing historic and calculate gross domestic consumption (PE); pos: model > empiric (overestimation) neg: empiric > model (understimation)
    """
    return total_pe_by_region() - iea_pe_total()


@component.add(
    name="CHECK_GDC_IEA_model_by_region_and_commodity",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_PE_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"pe_by_commodity": 1, "iea_gdc_by_commodity_empirical": 1},
)
def check_gdc_iea_model_by_region_and_commodity():
    """
    Comparison of empirical data and model results by region and PE-commodity. Negative value = underestimated demand, empirical values higher than modeled values;
    """
    return pe_by_commodity() - iea_gdc_by_commodity_empirical()


@component.add(
    name="CHECK_GDC_IEA_model_total_world",
    units="EJ/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"pe_total_world": 1, "iea_pe_total_world": 1},
)
def check_gdc_iea_model_total_world():
    """
    Check-varaible comparing historic and calculate gross domestic consumption (PE); Check-varaible comparing historic and calculate gross domestic consumption (PE); pos: model > empiric (overestimation) neg: empiric > model (understimation)
    """
    return pe_total_world() - iea_pe_total_world()


@component.add(
    name="check_global_TO_demand_fulfilled",
    units="EJ/Year",
    subscripts=["NRG_TO_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"check_to_demand_fulfilled": 1},
)
def check_global_to_demand_fulfilled():
    """
    positiv numbers indicate that the global demand could not be satisfied
    """
    return sum(
        check_to_demand_fulfilled().rename({"REGIONS_9_I": "REGIONS_9_I!"}),
        dim=["REGIONS_9_I!"],
    )


@component.add(
    name="check_historic_CO2_emissions_energy_and_waste",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "total_co2_emissions_pe": 1,
        "historic_co2_emissions_energy_and_waste_9r": 1,
    },
)
def check_historic_co2_emissions_energy_and_waste():
    return -1 + zidz(
        total_co2_emissions_pe(), historic_co2_emissions_energy_and_waste_9r()
    )


@component.add(
    name="check_historic_CO2_emissions_energy_and_waste_35R",
    units="1",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "ghg_all_emissions_35r": 1,
        "historic_co2_emissions_energy_and_waste": 1,
    },
)
def check_historic_co2_emissions_energy_and_waste_35r():
    return -1 + zidz(
        ghg_all_emissions_35r().loc[:, "CO2"].reset_coords(drop=True),
        historic_co2_emissions_energy_and_waste(),
    )


@component.add(
    name="check_historic_CO2_emissions_energy_and_waste_9R",
    units="1",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "total_ghg_energy_chain_emissions_9r": 1,
        "historic_co2_emissions_energy_and_waste_9r": 1,
    },
)
def check_historic_co2_emissions_energy_and_waste_9r():
    return -1 + zidz(
        total_ghg_energy_chain_emissions_9r().loc[:, "CO2"].reset_coords(drop=True),
        historic_co2_emissions_energy_and_waste_9r(),
    )


@component.add(
    name="check_maximum_PROTRA_capacity_expansion_annual_growth",
    units="1/Year",
    subscripts=["REGIONS_9_I", "NRG_TO_I", "NRG_PROTRA_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"net_protra_capacity_expansion_annual_growth": 1},
)
def check_maximum_protra_capacity_expansion_annual_growth():
    return xr.DataArray(
        vmax(
            net_protra_capacity_expansion_annual_growth().rename(
                {
                    "REGIONS_9_I": "REGIONS_9_I!",
                    "NRG_TO_I": "NRG_TO_I!",
                    "NRG_PROTRA_I": "NRG_PROTRA_I!",
                }
            ),
            dim=["REGIONS_9_I!", "NRG_TO_I!", "NRG_PROTRA_I!"],
        ),
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "NRG_TO_I": _subscript_dict["NRG_TO_I"],
            "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
        },
        ["REGIONS_9_I", "NRG_TO_I", "NRG_PROTRA_I"],
    )


@component.add(
    name="check_PE_method_Vs_all_energy_chain_method_emissions",
    units="1",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "total_co2_emissions_pe": 1,
        "unit_conversion_mt_gt": 1,
        "total_ghg_energy_chain_emissions_9r": 1,
    },
)
def check_pe_method_vs_all_energy_chain_method_emissions():
    return -1 + zidz(
        total_co2_emissions_pe() / unit_conversion_mt_gt(),
        total_ghg_energy_chain_emissions_9r().loc[:, "CO2"].reset_coords(drop=True),
    )


@component.add(
    name="CHECK_RELATIVE_GDC_IEA_model_by_commodity",
    units="1",
    subscripts=["NRG_PE_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "iea_world_pe_by_commodity": 1, "world_pe_by_commodity": 1},
)
def check_relative_gdc_iea_model_by_commodity():
    """
    Comparison of empirical data and model results by PE-commodity in relative terms.
    """
    return if_then_else(
        time() < 2020,
        lambda: -1 + zidz(world_pe_by_commodity(), iea_world_pe_by_commodity()),
        lambda: xr.DataArray(
            0, {"NRG_PE_I": _subscript_dict["NRG_PE_I"]}, ["NRG_PE_I"]
        ),
    )


@component.add(
    name="CHECK_RELATIVE_GDC_IEA_model_by_region",
    units="1",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "iea_pe_total": 1, "total_pe_by_region": 1},
)
def check_relative_gdc_iea_model_by_region():
    """
    Comparison of empirical data and model results by region in relative terms.
    """
    return if_then_else(
        time() < 2020,
        lambda: -1 + zidz(total_pe_by_region(), iea_pe_total()),
        lambda: xr.DataArray(
            0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
        ),
    )


@component.add(
    name="CHECK_RELATIVE_GDC_IEA_model_by_region_and_commodity",
    units="1",
    subscripts=["REGIONS_9_I", "NRG_PE_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "pe_by_commodity": 1, "iea_gdc_by_commodity_empirical": 1},
)
def check_relative_gdc_iea_model_by_region_and_commodity():
    """
    Comparison of empirical data and model results by region and PE-commodity in relative terms.
    """
    return if_then_else(
        time() < 2020,
        lambda: -1 + zidz(pe_by_commodity(), iea_gdc_by_commodity_empirical()),
        lambda: xr.DataArray(
            0,
            {
                "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                "NRG_PE_I": _subscript_dict["NRG_PE_I"],
            },
            ["REGIONS_9_I", "NRG_PE_I"],
        ),
    )


@component.add(
    name="CHECK_RELATIVE_GDC_IEA_model_total_world",
    units="1",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "iea_pe_total_world": 1, "pe_total_world": 1},
)
def check_relative_gdc_iea_model_total_world():
    """
    Comparison of empirical data and model results for al PE-commodities and at world level in relative terms.
    """
    return if_then_else(
        time() < 2020,
        lambda: -1 + zidz(pe_total_world(), iea_pe_total_world()),
        lambda: 0,
    )


@component.add(
    name="check_TO_demand_fulfilled",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_TO_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"to_by_commodity": 1, "protra_to_allocated": 1},
)
def check_to_demand_fulfilled():
    """
    Check variable if transformation output is sufficient to satisfy demand (coming from final energy + supply processes like transmission losses, storage losses, flexibility processes). Positive numbers = not enought PROTRA output to satisfy demand (GAP); negative numbers should not appear because of allocation (we would see a under-utilization of stock).
    """
    return to_by_commodity() - sum(
        protra_to_allocated().rename({"NRG_PROTRA_I": "NRG_PROTRA_I!"}),
        dim=["NRG_PROTRA_I!"],
    )


@component.add(
    name="global_TO_demand_by_commodity",
    units="EJ/Year",
    subscripts=["NRG_TO_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"to_by_commodity": 1},
)
def global_to_demand_by_commodity():
    """
    global to demand (before allocation to PROTRA) by commodity
    """
    return sum(
        to_by_commodity().rename({"REGIONS_9_I": "REGIONS_9_I!"}), dim=["REGIONS_9_I!"]
    )


@component.add(
    name="global_TO_production_by_commodity",
    units="EJ/Year",
    subscripts=["NRG_TO_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"aggregated_to_production_by_commodity": 1},
)
def global_to_production_by_commodity():
    """
    global production from PROTRA (after energy technology utilization allocation)
    """
    return sum(
        aggregated_to_production_by_commodity().rename({"REGIONS_9_I": "REGIONS_9_I!"}),
        dim=["REGIONS_9_I!"],
    )


@component.add(
    name="HISTORIC_CO2_EMISSIONS_ENERGY_AND_WASTE_9R",
    units="Mt/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "historic_co2_emissions_energy_and_waste": 1,
        "historic_co2_emissions_energy_and_waste_eu27": 1,
    },
)
def historic_co2_emissions_energy_and_waste_9r():
    value = xr.DataArray(
        np.nan, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
    )
    value.loc[_subscript_dict["REGIONS_8_I"]] = (
        historic_co2_emissions_energy_and_waste()
        .loc[_subscript_dict["REGIONS_8_I"]]
        .rename({"REGIONS_35_I": "REGIONS_8_I"})
        .values
    )
    value.loc[["EU27"]] = historic_co2_emissions_energy_and_waste_eu27()
    return value


@component.add(
    name="HISTORIC_CO2_EMISSIONS_ENERGY_AND_WASTE_EU27",
    units="Mt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"historic_co2_emissions_energy_and_waste": 1},
)
def historic_co2_emissions_energy_and_waste_eu27():
    return sum(
        historic_co2_emissions_energy_and_waste()
        .loc[_subscript_dict["REGIONS_EU27_I"]]
        .rename({"REGIONS_35_I": "REGIONS_EU27_I!"}),
        dim=["REGIONS_EU27_I!"],
    )


@component.add(
    name="IEA_PE_total",
    units="EJ/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"iea_gdc_by_commodity_empirical": 1},
)
def iea_pe_total():
    """
    total PE by region; source: IEA energy balances
    """
    return sum(
        iea_gdc_by_commodity_empirical().rename({"NRG_PE_I": "NRG_PE_I!"}),
        dim=["NRG_PE_I!"],
    )


@component.add(
    name="IEA_PE_total_world",
    units="EJ/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"iea_pe_total": 1},
)
def iea_pe_total_world():
    """
    total PE world; source: IEA energy balances
    """
    return sum(
        iea_pe_total().rename({"REGIONS_9_I": "REGIONS_9_I!"}), dim=["REGIONS_9_I!"]
    )


@component.add(
    name="IEA_TO_BY_PROTRA_EMPIRICAL",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "PROTRA_NON_CCS_I", "NRG_COMMODITIES_I"],
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_iea_to_by_protra_empirical",
        "__data__": "_ext_data_iea_to_by_protra_empirical",
        "time": 1,
    },
)
def iea_to_by_protra_empirical():
    """
    Empirical Transformation-Output heat and electricity from CHP, PP and HP from IEA extended energy balance. Note: Wind, PV and Hydropower is more disaggregated in WILIAM, so it was split up with help of secondary data (IRENA).
    """
    return _ext_data_iea_to_by_protra_empirical(time())


_ext_data_iea_to_by_protra_empirical = ExtData(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_TO_by_PROTRA",
    "TO_by_PROTRA_TIME",
    "PROTRA_CHP_gas_fuels_TO_elec",
    None,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PROTRA_NON_CCS_I": ["PROTRA_CHP_gas_fuels"],
        "NRG_COMMODITIES_I": ["TO_elec"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PROTRA_NON_CCS_I": _subscript_dict["PROTRA_NON_CCS_I"],
        "NRG_COMMODITIES_I": _subscript_dict["NRG_COMMODITIES_I"],
    },
    "_ext_data_iea_to_by_protra_empirical",
)

_ext_data_iea_to_by_protra_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_TO_by_PROTRA",
    "TO_by_PROTRA_TIME",
    "PROTRA_CHP_gas_fuels_TO_heat",
    None,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PROTRA_NON_CCS_I": ["PROTRA_CHP_gas_fuels"],
        "NRG_COMMODITIES_I": ["TO_heat"],
    },
)

_ext_data_iea_to_by_protra_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_TO_by_PROTRA",
    "TO_by_PROTRA_TIME",
    "PROTRA_CHP_geothermal_TO_elec",
    "interpolate",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PROTRA_NON_CCS_I": ["PROTRA_CHP_geothermal_DEACTIVATED"],
        "NRG_COMMODITIES_I": ["TO_elec"],
    },
)

_ext_data_iea_to_by_protra_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_TO_by_PROTRA",
    "TO_by_PROTRA_TIME",
    "PROTRA_CHP_geothermal_TO_heat",
    "interpolate",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PROTRA_NON_CCS_I": ["PROTRA_CHP_geothermal_DEACTIVATED"],
        "NRG_COMMODITIES_I": ["TO_heat"],
    },
)

_ext_data_iea_to_by_protra_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_TO_by_PROTRA",
    "TO_by_PROTRA_TIME",
    "PROTRA_CHP_liquid_fuels_TO_elec",
    None,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PROTRA_NON_CCS_I": ["PROTRA_CHP_liquid_fuels"],
        "NRG_COMMODITIES_I": ["TO_elec"],
    },
)

_ext_data_iea_to_by_protra_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_TO_by_PROTRA",
    "TO_by_PROTRA_TIME",
    "PROTRA_CHP_liquid_fuels_TO_heat",
    None,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PROTRA_NON_CCS_I": ["PROTRA_CHP_liquid_fuels"],
        "NRG_COMMODITIES_I": ["TO_heat"],
    },
)

_ext_data_iea_to_by_protra_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_TO_by_PROTRA",
    "TO_by_PROTRA_TIME",
    "PROTRA_CHP_solid_fossil_TO_elec",
    None,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PROTRA_NON_CCS_I": ["PROTRA_CHP_solid_fossil"],
        "NRG_COMMODITIES_I": ["TO_elec"],
    },
)

_ext_data_iea_to_by_protra_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_TO_by_PROTRA",
    "TO_by_PROTRA_TIME",
    "PROTRA_CHP_solid_fossil_TO_heat",
    None,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PROTRA_NON_CCS_I": ["PROTRA_CHP_solid_fossil"],
        "NRG_COMMODITIES_I": ["TO_heat"],
    },
)

_ext_data_iea_to_by_protra_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_TO_by_PROTRA",
    "TO_by_PROTRA_TIME",
    "PROTRA_CHP_waste_TO_elec",
    None,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PROTRA_NON_CCS_I": ["PROTRA_CHP_waste"],
        "NRG_COMMODITIES_I": ["TO_elec"],
    },
)

_ext_data_iea_to_by_protra_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_TO_by_PROTRA",
    "TO_by_PROTRA_TIME",
    "PROTRA_CHP_waste_TO_heat",
    None,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PROTRA_NON_CCS_I": ["PROTRA_CHP_waste"],
        "NRG_COMMODITIES_I": ["TO_heat"],
    },
)

_ext_data_iea_to_by_protra_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_TO_by_PROTRA",
    "TO_by_PROTRA_TIME",
    "PROTRA_HP_gas_fuels_TO_elec",
    None,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PROTRA_NON_CCS_I": ["PROTRA_HP_gas_fuels"],
        "NRG_COMMODITIES_I": ["TO_elec"],
    },
)

_ext_data_iea_to_by_protra_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_TO_by_PROTRA",
    "TO_by_PROTRA_TIME",
    "PROTRA_HP_gas_fuels_TO_heat",
    None,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PROTRA_NON_CCS_I": ["PROTRA_HP_gas_fuels"],
        "NRG_COMMODITIES_I": ["TO_heat"],
    },
)

_ext_data_iea_to_by_protra_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_TO_by_PROTRA",
    "TO_by_PROTRA_TIME",
    "PROTRA_HP_geothermal_TO_elec",
    None,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PROTRA_NON_CCS_I": ["PROTRA_HP_geothermal"],
        "NRG_COMMODITIES_I": ["TO_elec"],
    },
)

_ext_data_iea_to_by_protra_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_TO_by_PROTRA",
    "TO_by_PROTRA_TIME",
    "PROTRA_HP_geothermal_TO_heat",
    None,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PROTRA_NON_CCS_I": ["PROTRA_HP_geothermal"],
        "NRG_COMMODITIES_I": ["TO_heat"],
    },
)

_ext_data_iea_to_by_protra_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_TO_by_PROTRA",
    "TO_by_PROTRA_TIME",
    "PROTRA_HP_liquid_fuels_TO_elec",
    None,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PROTRA_NON_CCS_I": ["PROTRA_HP_liquid_fuels"],
        "NRG_COMMODITIES_I": ["TO_elec"],
    },
)

_ext_data_iea_to_by_protra_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_TO_by_PROTRA",
    "TO_by_PROTRA_TIME",
    "PROTRA_HP_liquid_fuels_TO_heat",
    None,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PROTRA_NON_CCS_I": ["PROTRA_HP_liquid_fuels"],
        "NRG_COMMODITIES_I": ["TO_heat"],
    },
)

_ext_data_iea_to_by_protra_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_TO_by_PROTRA",
    "TO_by_PROTRA_TIME",
    "PROTRA_HP_solar_TO_elec",
    "interpolate",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PROTRA_NON_CCS_I": ["PROTRA_HP_solar_DEACTIVATED"],
        "NRG_COMMODITIES_I": ["TO_elec"],
    },
)

_ext_data_iea_to_by_protra_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_TO_by_PROTRA",
    "TO_by_PROTRA_TIME",
    "PROTRA_HP_solar_TO_heat",
    "interpolate",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PROTRA_NON_CCS_I": ["PROTRA_HP_solar_DEACTIVATED"],
        "NRG_COMMODITIES_I": ["TO_heat"],
    },
)

_ext_data_iea_to_by_protra_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_TO_by_PROTRA",
    "TO_by_PROTRA_TIME",
    "PROTRA_HP_solid_fossil_TO_elec",
    None,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PROTRA_NON_CCS_I": ["PROTRA_HP_solid_fossil"],
        "NRG_COMMODITIES_I": ["TO_elec"],
    },
)

_ext_data_iea_to_by_protra_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_TO_by_PROTRA",
    "TO_by_PROTRA_TIME",
    "PROTRA_HP_solid_fossil_TO_heat",
    None,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PROTRA_NON_CCS_I": ["PROTRA_HP_solid_fossil"],
        "NRG_COMMODITIES_I": ["TO_heat"],
    },
)

_ext_data_iea_to_by_protra_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_TO_by_PROTRA",
    "TO_by_PROTRA_TIME",
    "PROTRA_HP_waste_TO_elec",
    None,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PROTRA_NON_CCS_I": ["PROTRA_HP_waste"],
        "NRG_COMMODITIES_I": ["TO_elec"],
    },
)

_ext_data_iea_to_by_protra_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_TO_by_PROTRA",
    "TO_by_PROTRA_TIME",
    "PROTRA_HP_waste_TO_heat",
    None,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PROTRA_NON_CCS_I": ["PROTRA_HP_waste"],
        "NRG_COMMODITIES_I": ["TO_heat"],
    },
)

_ext_data_iea_to_by_protra_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_TO_by_PROTRA",
    "TO_by_PROTRA_TIME",
    "PROTRA_PP_gas_fuels_TO_elec",
    None,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PROTRA_NON_CCS_I": ["PROTRA_PP_gas_fuels"],
        "NRG_COMMODITIES_I": ["TO_elec"],
    },
)

_ext_data_iea_to_by_protra_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_TO_by_PROTRA",
    "TO_by_PROTRA_TIME",
    "PROTRA_PP_gas_fuels_TO_heat",
    None,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PROTRA_NON_CCS_I": ["PROTRA_PP_gas_fuels"],
        "NRG_COMMODITIES_I": ["TO_heat"],
    },
)

_ext_data_iea_to_by_protra_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_TO_by_PROTRA",
    "TO_by_PROTRA_TIME",
    "PROTRA_PP_geothermal_TO_elec",
    None,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PROTRA_NON_CCS_I": ["PROTRA_PP_geothermal"],
        "NRG_COMMODITIES_I": ["TO_elec"],
    },
)

_ext_data_iea_to_by_protra_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_TO_by_PROTRA",
    "TO_by_PROTRA_TIME",
    "PROTRA_PP_geothermal_TO_heat",
    None,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PROTRA_NON_CCS_I": ["PROTRA_PP_geothermal"],
        "NRG_COMMODITIES_I": ["TO_heat"],
    },
)

_ext_data_iea_to_by_protra_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_TO_by_PROTRA",
    "TO_by_PROTRA_TIME",
    "PROTRA_PP_hydropower_dammed_TO_elec",
    None,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PROTRA_NON_CCS_I": ["PROTRA_PP_hydropower_dammed"],
        "NRG_COMMODITIES_I": ["TO_elec"],
    },
)

_ext_data_iea_to_by_protra_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_TO_by_PROTRA",
    "TO_by_PROTRA_TIME",
    "PROTRA_PP_hydropower_dammed_TO_heat",
    None,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PROTRA_NON_CCS_I": ["PROTRA_PP_hydropower_dammed"],
        "NRG_COMMODITIES_I": ["TO_heat"],
    },
)

_ext_data_iea_to_by_protra_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_TO_by_PROTRA",
    "TO_by_PROTRA_TIME",
    "PROTRA_PP_hydropower_run_of_river_TO_elec",
    None,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PROTRA_NON_CCS_I": ["PROTRA_PP_hydropower_run_of_river"],
        "NRG_COMMODITIES_I": ["TO_elec"],
    },
)

_ext_data_iea_to_by_protra_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_TO_by_PROTRA",
    "TO_by_PROTRA_TIME",
    "PROTRA_PP_hydropower_run_of_river_TO_heat",
    None,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PROTRA_NON_CCS_I": ["PROTRA_PP_hydropower_run_of_river"],
        "NRG_COMMODITIES_I": ["TO_heat"],
    },
)

_ext_data_iea_to_by_protra_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_TO_by_PROTRA",
    "TO_by_PROTRA_TIME",
    "PROTRA_PP_liquid_fuels_TO_elec",
    None,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PROTRA_NON_CCS_I": ["PROTRA_PP_liquid_fuels"],
        "NRG_COMMODITIES_I": ["TO_elec"],
    },
)

_ext_data_iea_to_by_protra_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_TO_by_PROTRA",
    "TO_by_PROTRA_TIME",
    "PROTRA_PP_liquid_fuels_TO_heat",
    None,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PROTRA_NON_CCS_I": ["PROTRA_PP_liquid_fuels"],
        "NRG_COMMODITIES_I": ["TO_heat"],
    },
)

_ext_data_iea_to_by_protra_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_TO_by_PROTRA",
    "TO_by_PROTRA_TIME",
    "PROTRA_PP_nuclear_TO_elec",
    None,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PROTRA_NON_CCS_I": ["PROTRA_PP_nuclear"],
        "NRG_COMMODITIES_I": ["TO_elec"],
    },
)

_ext_data_iea_to_by_protra_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_TO_by_PROTRA",
    "TO_by_PROTRA_TIME",
    "PROTRA_PP_nuclear_TO_heat",
    None,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PROTRA_NON_CCS_I": ["PROTRA_PP_nuclear"],
        "NRG_COMMODITIES_I": ["TO_heat"],
    },
)

_ext_data_iea_to_by_protra_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_TO_by_PROTRA",
    "TO_by_PROTRA_TIME",
    "PROTRA_PP_oceanic_TO_elec",
    None,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PROTRA_NON_CCS_I": ["PROTRA_PP_oceanic"],
        "NRG_COMMODITIES_I": ["TO_elec"],
    },
)

_ext_data_iea_to_by_protra_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_TO_by_PROTRA",
    "TO_by_PROTRA_TIME",
    "PROTRA_PP_oceanic_TO_heat",
    None,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PROTRA_NON_CCS_I": ["PROTRA_PP_oceanic"],
        "NRG_COMMODITIES_I": ["TO_heat"],
    },
)

_ext_data_iea_to_by_protra_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_TO_by_PROTRA",
    "TO_by_PROTRA_TIME",
    "PROTRA_PP_solar_CSP_TO_elec",
    None,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PROTRA_NON_CCS_I": ["PROTRA_PP_solar_CSP"],
        "NRG_COMMODITIES_I": ["TO_elec"],
    },
)

_ext_data_iea_to_by_protra_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_TO_by_PROTRA",
    "TO_by_PROTRA_TIME",
    "PROTRA_PP_solar_CSP_TO_heat",
    None,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PROTRA_NON_CCS_I": ["PROTRA_PP_solar_CSP"],
        "NRG_COMMODITIES_I": ["TO_heat"],
    },
)

_ext_data_iea_to_by_protra_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_TO_by_PROTRA",
    "TO_by_PROTRA_TIME",
    "PROTRA_PP_solar_PV_TO_elec",
    "interpolate",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PROTRA_NON_CCS_I": ["PROTRA_PP_solar_open_space_PV"],
        "NRG_COMMODITIES_I": ["TO_elec"],
    },
)

_ext_data_iea_to_by_protra_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_TO_by_PROTRA",
    "TO_by_PROTRA_TIME",
    "PROTRA_PP_solar_PV_TO_heat",
    "interpolate",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PROTRA_NON_CCS_I": ["PROTRA_PP_solar_open_space_PV"],
        "NRG_COMMODITIES_I": ["TO_heat"],
    },
)

_ext_data_iea_to_by_protra_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_TO_by_PROTRA",
    "TO_by_PROTRA_TIME",
    "PROTRA_PP_solar_urban_PV_TO_elec",
    None,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PROTRA_NON_CCS_I": ["PROTRA_PP_solar_urban_PV"],
        "NRG_COMMODITIES_I": ["TO_elec"],
    },
)

_ext_data_iea_to_by_protra_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_TO_by_PROTRA",
    "TO_by_PROTRA_TIME",
    "PROTRA_PP_solar_urban_PV_TO_heat",
    None,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PROTRA_NON_CCS_I": ["PROTRA_PP_solar_urban_PV"],
        "NRG_COMMODITIES_I": ["TO_heat"],
    },
)

_ext_data_iea_to_by_protra_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_TO_by_PROTRA",
    "TO_by_PROTRA_TIME",
    "PROTRA_PP_solid_fossil_TO_elec",
    None,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PROTRA_NON_CCS_I": ["PROTRA_PP_solid_fossil"],
        "NRG_COMMODITIES_I": ["TO_elec"],
    },
)

_ext_data_iea_to_by_protra_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_TO_by_PROTRA",
    "TO_by_PROTRA_TIME",
    "PROTRA_PP_solid_fossil_TO_heat",
    None,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PROTRA_NON_CCS_I": ["PROTRA_PP_solid_fossil"],
        "NRG_COMMODITIES_I": ["TO_heat"],
    },
)

_ext_data_iea_to_by_protra_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_TO_by_PROTRA",
    "TO_by_PROTRA_TIME",
    "PROTRA_PP_waste_TO_elec",
    None,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PROTRA_NON_CCS_I": ["PROTRA_PP_waste"],
        "NRG_COMMODITIES_I": ["TO_elec"],
    },
)

_ext_data_iea_to_by_protra_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_TO_by_PROTRA",
    "TO_by_PROTRA_TIME",
    "PROTRA_PP_waste_TO_heat",
    None,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PROTRA_NON_CCS_I": ["PROTRA_PP_waste"],
        "NRG_COMMODITIES_I": ["TO_heat"],
    },
)

_ext_data_iea_to_by_protra_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_TO_by_PROTRA",
    "TO_by_PROTRA_TIME",
    "PROTRA_PP_wind_offshore_TO_elec",
    None,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PROTRA_NON_CCS_I": ["PROTRA_PP_wind_offshore"],
        "NRG_COMMODITIES_I": ["TO_elec"],
    },
)

_ext_data_iea_to_by_protra_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_TO_by_PROTRA",
    "TO_by_PROTRA_TIME",
    "PROTRA_PP_wind_offshore_TO_heat",
    None,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PROTRA_NON_CCS_I": ["PROTRA_PP_wind_offshore"],
        "NRG_COMMODITIES_I": ["TO_heat"],
    },
)

_ext_data_iea_to_by_protra_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_TO_by_PROTRA",
    "TO_by_PROTRA_TIME",
    "PROTRA_PP_wind_onshore_TO_elec",
    None,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PROTRA_NON_CCS_I": ["PROTRA_PP_wind_onshore"],
        "NRG_COMMODITIES_I": ["TO_elec"],
    },
)

_ext_data_iea_to_by_protra_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_TO_by_PROTRA",
    "TO_by_PROTRA_TIME",
    "PROTRA_PP_wind_onshore_TO_heat",
    None,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PROTRA_NON_CCS_I": ["PROTRA_PP_wind_onshore"],
        "NRG_COMMODITIES_I": ["TO_heat"],
    },
)

_ext_data_iea_to_by_protra_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_TO_by_PROTRA",
    "TO_by_PROTRA_TIME",
    "PROTRA_CHP_solid_bio_TO_elec",
    None,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PROTRA_NON_CCS_I": ["PROTRA_CHP_solid_bio"],
        "NRG_COMMODITIES_I": ["TO_elec"],
    },
)

_ext_data_iea_to_by_protra_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_TO_by_PROTRA",
    "TO_by_PROTRA_TIME",
    "PROTRA_CHP_solid_bio_TO_heat",
    None,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PROTRA_NON_CCS_I": ["PROTRA_CHP_solid_bio"],
        "NRG_COMMODITIES_I": ["TO_heat"],
    },
)

_ext_data_iea_to_by_protra_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_TO_by_PROTRA",
    "TO_by_PROTRA_TIME",
    "PROTRA_PP_solid_bio_TO_elec",
    None,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PROTRA_NON_CCS_I": ["PROTRA_PP_solid_bio"],
        "NRG_COMMODITIES_I": ["TO_elec"],
    },
)

_ext_data_iea_to_by_protra_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_TO_by_PROTRA",
    "TO_by_PROTRA_TIME",
    "PROTRA_PP_solid_bio_TO_heat",
    None,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PROTRA_NON_CCS_I": ["PROTRA_PP_solid_bio"],
        "NRG_COMMODITIES_I": ["TO_heat"],
    },
)

_ext_data_iea_to_by_protra_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_TO_by_PROTRA",
    "TO_by_PROTRA_TIME",
    "PROTRA_HP_solid_bio_TO_elec",
    None,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PROTRA_NON_CCS_I": ["PROTRA_HP_solid_bio"],
        "NRG_COMMODITIES_I": ["TO_elec"],
    },
)

_ext_data_iea_to_by_protra_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_TO_by_PROTRA",
    "TO_by_PROTRA_TIME",
    "PROTRA_HP_solid_bio_TO_heat",
    None,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PROTRA_NON_CCS_I": ["PROTRA_HP_solid_bio"],
        "NRG_COMMODITIES_I": ["TO_heat"],
    },
)


@component.add(
    name="IEA_world_PE_by_commodity",
    units="EJ/Year",
    subscripts=["NRG_PE_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"iea_gdc_by_commodity_empirical": 1},
)
def iea_world_pe_by_commodity():
    """
    total gross domestic energy consumption
    """
    return sum(
        iea_gdc_by_commodity_empirical().rename({"REGIONS_9_I": "REGIONS_9_I!"}),
        dim=["REGIONS_9_I!"],
    )


@component.add(
    name="PROTRA_TO_allocated_in_TWh",
    units="TW*h/Year",
    subscripts=["REGIONS_9_I", "NRG_COMMODITIES_I", "NRG_PROTRA_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_to_allocated": 2,
        "unit_conversion_j_ej": 2,
        "unit_conversion_w_tw": 2,
        "unit_conversion_j_wh": 2,
    },
)
def protra_to_allocated_in_twh():
    """
    Output of heat and electricity from PROTRA in TWh
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "NRG_COMMODITIES_I": _subscript_dict["NRG_COMMODITIES_I"],
            "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
        },
        ["REGIONS_9_I", "NRG_COMMODITIES_I", "NRG_PROTRA_I"],
    )
    value.loc[:, ["TO_elec"], :] = (
        (
            protra_to_allocated().loc[:, "TO_elec", :].reset_coords(drop=True)
            * unit_conversion_j_ej()
            / unit_conversion_w_tw()
            / unit_conversion_j_wh()
        )
        .expand_dims({"NRG_COMMODITIES_I": ["TO_elec"]}, 1)
        .values
    )
    value.loc[:, ["TO_heat"], :] = (
        (
            protra_to_allocated().loc[:, "TO_heat", :].reset_coords(drop=True)
            * unit_conversion_j_ej()
            / unit_conversion_w_tw()
            / unit_conversion_j_wh()
        )
        .expand_dims({"NRG_COMMODITIES_I": ["TO_heat"]}, 1)
        .values
    )
    return value


@component.add(
    name="TO_IEA_Model_Check",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "PROTRA_NON_CCS_I", "NRG_COMMODITIES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"protra_to_allocated": 2, "iea_to_by_protra_empirical": 2},
)
def to_iea_model_check():
    """
    positive values: model > empiric (overutilization of stock) negative values: emipiric > model (underutilization of stock) NOTE: China HP_solid_fossil: HP_solid_fossil output is 0: this is known to be an error in IEA energy balance data, where all heat-output is attributed to CHPs.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "PROTRA_NON_CCS_I": _subscript_dict["PROTRA_NON_CCS_I"],
            "NRG_COMMODITIES_I": _subscript_dict["NRG_COMMODITIES_I"],
        },
        ["REGIONS_9_I", "PROTRA_NON_CCS_I", "NRG_COMMODITIES_I"],
    )
    value.loc[:, :, ["TO_elec"]] = (
        (
            protra_to_allocated()
            .loc[:, "TO_elec", _subscript_dict["PROTRA_NON_CCS_I"]]
            .reset_coords(drop=True)
            .rename({"NRG_PROTRA_I": "PROTRA_NON_CCS_I"})
            - iea_to_by_protra_empirical().loc[:, :, "TO_elec"].reset_coords(drop=True)
        )
        .expand_dims({"NRG_COMMODITIES_I": ["TO_elec"]}, 2)
        .values
    )
    value.loc[:, :, ["TO_heat"]] = (
        (
            iea_to_by_protra_empirical().loc[:, :, "TO_heat"].reset_coords(drop=True)
            - protra_to_allocated()
            .loc[:, "TO_heat", _subscript_dict["PROTRA_NON_CCS_I"]]
            .reset_coords(drop=True)
            .rename({"NRG_PROTRA_I": "PROTRA_NON_CCS_I"})
        )
        .expand_dims({"NRG_COMMODITIES_I": ["TO_heat"]}, 2)
        .values
    )
    return value
