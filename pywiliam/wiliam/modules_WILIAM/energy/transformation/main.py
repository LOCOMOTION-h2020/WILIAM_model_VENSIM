"""
Module energy.transformation.main
Translated using PySD version 3.10.0
"""


@component.add(
    name="aux_ti_gas_bio",
    units="DMNL",
    subscripts=["REGIONS_9_I", "PROTRA_TI_GAS_I", "NRG_COMMODITIES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "exogenous_protra_input_shares": 2,
        "switch_nrg_limited_res_potentials": 1,
        "delayed_ts_bioenergy_input_share": 1,
        "switch_energy": 1,
    },
)
def aux_ti_gas_bio():
    return if_then_else(
        time() > 2015,
        lambda: if_then_else(
            np.logical_or(
                switch_energy() == 0, switch_nrg_limited_res_potentials() == 0
            ),
            lambda: exogenous_protra_input_shares()
            .loc[:, _subscript_dict["PROTRA_TI_GAS_I"], "TI_gas_bio"]
            .reset_coords(drop=True)
            .rename({"NRG_PROTRA_I": "PROTRA_TI_GAS_I"}),
            lambda: delayed_ts_bioenergy_input_share().expand_dims(
                {"PROTRA_TI_GAS_I": _subscript_dict["PROTRA_TI_GAS_I"]}, 1
            ),
        ),
        lambda: exogenous_protra_input_shares()
        .loc[:, _subscript_dict["PROTRA_TI_GAS_I"], "TI_gas_bio"]
        .reset_coords(drop=True)
        .rename({"NRG_PROTRA_I": "PROTRA_TI_GAS_I"}),
    ).expand_dims({"NRG_COMMODITIES_I": ["TI_gas_bio"]}, 2)


@component.add(
    name="aux_ti_liquid_bio",
    units="DMNL",
    subscripts=["REGIONS_9_I", "PROTRA_TI_LIQUIDS_I", "NRG_COMMODITIES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "exogenous_protra_input_shares": 2,
        "switch_nrg_limited_res_potentials": 1,
        "delayed_ts_bioenergy_input_share": 1,
        "switch_energy": 1,
    },
)
def aux_ti_liquid_bio():
    return if_then_else(
        time() > 2015,
        lambda: if_then_else(
            np.logical_or(
                switch_energy() == 0, switch_nrg_limited_res_potentials() == 0
            ),
            lambda: exogenous_protra_input_shares()
            .loc[:, _subscript_dict["PROTRA_TI_LIQUIDS_I"], "TI_liquid_bio"]
            .reset_coords(drop=True)
            .rename({"NRG_PROTRA_I": "PROTRA_TI_LIQUIDS_I"}),
            lambda: delayed_ts_bioenergy_input_share().expand_dims(
                {"PROTRA_TI_LIQUIDS_I": _subscript_dict["PROTRA_TI_LIQUIDS_I"]}, 1
            ),
        ),
        lambda: exogenous_protra_input_shares()
        .loc[:, _subscript_dict["PROTRA_TI_LIQUIDS_I"], "TI_liquid_bio"]
        .reset_coords(drop=True)
        .rename({"NRG_PROTRA_I": "PROTRA_TI_LIQUIDS_I"}),
    ).expand_dims({"NRG_COMMODITIES_I": ["TI_liquid_bio"]}, 2)


@component.add(
    name="bioenergy_input_share",
    units="1",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"energy_available_from_crops": 1, "ti_gas_liquids": 1},
)
def bioenergy_input_share():
    """
    Endogenous bioenergy input share as given by the availability in the land-use module.
    """
    return zidz(energy_available_from_crops(), ti_gas_liquids())


@component.add(
    name="delayed_TS_bioenergy_input_share",
    units="1",
    subscripts=["REGIONS_9_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_bioenergy_input_share": 1},
    other_deps={
        "_delayfixed_delayed_ts_bioenergy_input_share": {
            "initial": {"time_step": 1},
            "step": {"bioenergy_input_share": 1},
        }
    },
)
def delayed_ts_bioenergy_input_share():
    """
    DELAY to avoid feedback problems. Initial value not relevant since until 2015 the input share takes the empiric values.
    """
    return _delayfixed_delayed_ts_bioenergy_input_share()


_delayfixed_delayed_ts_bioenergy_input_share = DelayFixed(
    lambda: bioenergy_input_share(),
    lambda: time_step(),
    lambda: xr.DataArray(
        0, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
    ),
    time_step,
    "_delayfixed_delayed_ts_bioenergy_input_share",
)


@component.add(
    name="economy_energy_transformation_input",
    units="EJ/Year",
    subscripts=[
        "REGIONS_9_I",
        "PRO_ECONOMY_CORRESPONDENCE_I",
        "SECTORS_TRANSFORMATION_ENERGY_I",
        "SECTORS_TRANSFORMATION_ENERGY_MAP_I",
    ],
    comp_type="Constant",
    comp_subtype="Normal",
)
def economy_energy_transformation_input():
    """
    physical energy flows corresponding to monetary INPUT flows from SECTORS_TRANSFORMATION_ENERGY_I (economic ROW of A-Matrix) to SECTORS_TRANSFORMATION_ENERGY_MAP_I (column of A-Matrix). Note: Stated in one complicated if-then-else equation because of VENSIM-bug with :EXCEPT: economy_energy_transformation_input[REGIONS_9_I,PRO_ECONOMY_CORRESPONDENCE_I,SECTORS_ TRANSFORMATION_ENERGY_I,SECTORS_TRANSFORMATION_ENERGY_MAP_I ]= IF_THEN_ELSE(PRO_ECONOMY_CORRESPONDENCE_I= PROTRA_CHP_gas_fuels:AND:SECTORS_TRANSFORMATION_ENERGY_I=DISTRIBUTION_GAS:A ND: SECTORS_TRANSFORMATION_ENERGY_MAP_I=ELECTRICITY_GAS, TI_by_PROTRA_and_commodity[REGIONS_9_I,PROTRA_CHP_gas_fuels,TI_gas_bio]*ZIDZ(PROTRA_T O_allocated[REGIONS_9_I,TO_elec,PROTRA_CHP_gas_fuels ], SUM(PROTRA_TO_allocated[REGIONS_9_I,NRG_TO_I!,PROTRA_CHP_gas_fuels]))+TI_by _PROTRA_and_commodity[REGIONS_9_I,PROTRA_CHP_gas_fuels ,TI_gas_fossil]*ZIDZ(PROTRA_TO_allocated[REGIONS_9_I,TO_elec,PROTRA_CHP_gas_fuels], SUM(PROTRA_TO_allocated[REGIONS_9_I, NRG_TO_I!,PROTRA_CHP_gas_fuels])), IF_THEN_ELSE(PRO_ECONOMY_CORRESPONDENCE_I= PROTRA_CHP_gas_fuels:AND:SECTORS_TRANSFORMATION_ENERGY_I=DISTRIBUTION_GAS:A ND: SECTORS_TRANSFORMATION_ENERGY_MAP_I=STEAM_HOT_WATER, TI_by_PROTRA_and_commodity[REGIONS_9_I,PROTRA_CHP_gas_fuels,TI_gas_bio]*ZIDZ(PROTRA_T O_allocated[REGIONS_9_I,TO_heat,PROTRA_CHP_gas_fuels ], SUM(PROTRA_TO_allocated[REGIONS_9_I,NRG_TO_I!,PROTRA_CHP_gas_fuels]))+TI_by _PROTRA_and_commodity[REGIONS_9_I,PROTRA_CHP_gas_fuels ,TI_gas_fossil]*ZIDZ(PROTRA_TO_allocated[REGIONS_9_I,TO_heat,PROTRA_CHP_gas_fuels], SUM(PROTRA_TO_allocated[REGIONS_9_I, NRG_TO_I!,PROTRA_CHP_gas_fuels])), IF_THEN_ELSE(PRO_ECONOMY_CORRESPONDENCE_I= PROTRA_CHP_solid_fossil:AND:SECTORS_TRANSFORMATION_ENERGY_I=MINING_COAL:AND : SECTORS_TRANSFORMATION_ENERGY_MAP_I=ELECTRICITY_COAL, TI_by_PROTRA_and_commodity[REGIONS_9_I,PROTRA_CHP_solid_fossil,TI_solid_fossil]*ZIDZ( PROTRA_TO_allocated[REGIONS_9_I,TO_elec ,PROTRA_CHP_solid_fossil], SUM(PROTRA_TO_allocated[REGIONS_9_I,NRG_TO_I!,PROTRA_CHP_solid_fossil])), IF_THEN_ELSE(PRO_ECONOMY_CORRESPONDENCE_I= PROTRA_CHP_solid_fossil:AND:SECTORS_TRANSFORMATION_ENERGY_I=MINING_COAL:AND : SECTORS_TRANSFORMATION_ENERGY_MAP_I=STEAM_HOT_WATER, TI_by_PROTRA_and_commodity[REGIONS_9_I,PROTRA_CHP_solid_fossil,TI_solid_fossil]*ZIDZ( PROTRA_TO_allocated[REGIONS_9_I,TO_heat ,PROTRA_CHP_solid_fossil], SUM(PROTRA_TO_allocated[REGIONS_9_I,NRG_TO_I!,PROTRA_CHP_solid_fossil])), IF_THEN_ELSE(PRO_ECONOMY_CORRESPONDENCE_I= PROTRA_CHP_gas_fuels_CCS:AND:SECTORS_TRANSFORMATION_ENERGY_I=DISTRIBUTION_G AS :AND:SECTORS_TRANSFORMATION_ENERGY_MAP_I=ELECTRICITY_GAS, TI_by_PROTRA_and_commodity[REGIONS_9_I,PROTRA_CHP_gas_fuels_CCS,TI_gas_bio]*ZIDZ(PROT RA_TO_allocated[REGIONS_9_I,TO_elec ,PROTRA_CHP_gas_fuels_CCS], SUM(PROTRA_TO_allocated[REGIONS_9_I,NRG_TO_I!,PROTRA_CHP_gas_fuels_CCS]))+T I_by_PROTRA_and_commodity [REGIONS_9_I,PROTRA_CHP_gas_fuels_CCS,TI_gas_fossil]*ZIDZ(PROTRA_TO_allocated[REGIONS _9_I,TO_elec,PROTRA_CHP_gas_fuels_CCS ], SUM(PROTRA_TO_allocated[REGIONS_9_I,NRG_TO_I!,PROTRA_CHP_gas_fuels_CCS])), IF_THEN_ELSE(PRO_ECONOMY_CORRESPONDENCE_I= PROTRA_CHP_gas_fuels_CCS:AND:SECTORS_TRANSFORMATION_ENERGY_I=DISTRIBUTION_G AS :AND:SECTORS_TRANSFORMATION_ENERGY_MAP_I=STEAM_HOT_WATER, TI_by_PROTRA_and_commodity[REGIONS_9_I,PROTRA_CHP_gas_fuels_CCS,TI_gas_bio]*ZIDZ(PROT RA_TO_allocated[REGIONS_9_I,TO_heat ,PROTRA_CHP_gas_fuels_CCS], SUM(PROTRA_TO_allocated[REGIONS_9_I,NRG_TO_I!,PROTRA_CHP_gas_fuels_CCS]))+T I_by_PROTRA_and_commodity [REGIONS_9_I,PROTRA_CHP_gas_fuels_CCS,TI_gas_fossil]*ZIDZ(PROTRA_TO_allocated[REGIONS _9_I,TO_heat,PROTRA_CHP_gas_fuels_CCS ], SUM(PROTRA_TO_allocated[REGIONS_9_I,NRG_TO_I!,PROTRA_CHP_gas_fuels_CCS])), IF_THEN_ELSE(PRO_ECONOMY_CORRESPONDENCE_I= PROTRA_CHP_solid_fossil_CCS:AND:SECTORS_TRANSFORMATION_ENERGY_I=MINING_COAL :AND: SECTORS_TRANSFORMATION_ENERGY_MAP_I=ELECTRICITY_COAL, TI_by_PROTRA_and_commodity[REGIONS_9_I,PROTRA_CHP_solid_fossil_CCS,TI_solid_fossil]*Z IDZ(PROTRA_TO_allocated[REGIONS_9_I ,TO_elec,PROTRA_CHP_solid_fossil_CCS], SUM(PROTRA_TO_allocated[REGIONS_9_I,NRG_TO_I!,PROTRA_CHP_solid_fossil_CCS]) ), IF_THEN_ELSE(PRO_ECONOMY_CORRESPONDENCE_I= PROTRA_CHP_solid_fossil_CCS:AND:SECTORS_TRANSFORMATION_ENERGY_I=MINING_COAL :AND: SECTORS_TRANSFORMATION_ENERGY_MAP_I=STEAM_HOT_WATER, TI_by_PROTRA_and_commodity[REGIONS_9_I,PROTRA_CHP_solid_fossil_CCS,TI_solid_fossil]*Z IDZ(PROTRA_TO_allocated[REGIONS_9_I ,TO_heat,PROTRA_CHP_solid_fossil_CCS], SUM(PROTRA_TO_allocated[REGIONS_9_I,NRG_TO_I!,PROTRA_CHP_solid_fossil_CCS]) ), IF_THEN_ELSE(PRO_ECONOMY_CORRESPONDENCE_I= PROTRA_CHP_solid_bio_CCS:AND:SECTORS_TRANSFORMATION_ENERGY_I=FORESTRY:AND:S ECTORS_TRANSFORMATION_ENERGY_MAP_I =ELECTRICITY_OTHER, TI_by_PROTRA_and_commodity[REGIONS_9_I,PROTRA_CHP_solid_bio_CCS,TI_solid_bio]*ZIDZ(PR OTRA_TO_allocated[REGIONS_9_I,TO_elec ,PROTRA_CHP_solid_bio_CCS], SUM(PROTRA_TO_allocated[REGIONS_9_I,NRG_TO_I!,PROTRA_CHP_solid_bio_CCS])), IF_THEN_ELSE(PRO_ECONOMY_CORRESPONDENCE_I= PROTRA_CHP_solid_bio_CCS:AND:SECTORS_TRANSFORMATION_ENERGY_I=FORESTRY:AND:S ECTORS_TRANSFORMATION_ENERGY_MAP_I =STEAM_HOT_WATER, TI_by_PROTRA_and_commodity[REGIONS_9_I,PROTRA_CHP_solid_bio_CCS,TI_solid_bio]*ZIDZ(PR OTRA_TO_allocated[REGIONS_9_I,TO_heat ,PROTRA_CHP_solid_bio_CCS], SUM(PROTRA_TO_allocated[REGIONS_9_I,NRG_TO_I!,PROTRA_CHP_solid_bio_CCS])), IF_THEN_ELSE(PRO_ECONOMY_CORRESPONDENCE_I= PROTRA_CHP_liquid_fuels:AND:SECTORS_TRANSFORMATION_ENERGY_I=REFINING:AND:SE CTORS_TRANSFORMATION_ENERGY_MAP_I =ELECTRICITY_OIL, TI_by_PROTRA_and_commodity[REGIONS_9_I,PROTRA_CHP_liquid_fuels,TI_liquid_bio]*ZIDZ(PR OTRA_TO_allocated[REGIONS_9_I,TO_elec ,PROTRA_CHP_liquid_fuels], SUM(PROTRA_TO_allocated[REGIONS_9_I,NRG_TO_I!,PROTRA_CHP_liquid_fuels]))+TI _by_PROTRA_and_commodity [REGIONS_9_I,PROTRA_CHP_liquid_fuels,TI_liquid_fossil]*ZIDZ(PROTRA_TO_allocated[REGIO NS_9_I,TO_elec,PROTRA_CHP_liquid_fuels ], SUM(PROTRA_TO_allocated[REGIONS_9_I,NRG_TO_I!,PROTRA_CHP_liquid_fuels])), IF_THEN_ELSE(PRO_ECONOMY_CORRESPONDENCE_I= PROTRA_CHP_liquid_fuels:AND:SECTORS_TRANSFORMATION_ENERGY_I=REFINING:AND:SE CTORS_TRANSFORMATION_ENERGY_MAP_I =STEAM_HOT_WATER, TI_by_PROTRA_and_commodity[REGIONS_9_I,PROTRA_CHP_liquid_fuels,TI_liquid_bio]*ZIDZ(PR OTRA_TO_allocated[REGIONS_9_I,TO_heat ,PROTRA_CHP_liquid_fuels], SUM(PROTRA_TO_allocated[REGIONS_9_I,NRG_TO_I!,PROTRA_CHP_liquid_fuels]))+TI _by_PROTRA_and_commodity [REGIONS_9_I,PROTRA_CHP_liquid_fuels,TI_liquid_fossil]*ZIDZ(PROTRA_TO_allocated[REGIO NS_9_I,TO_heat,PROTRA_CHP_liquid_fuels ], SUM(PROTRA_TO_allocated[REGIONS_9_I,NRG_TO_I!,PROTRA_CHP_liquid_fuels])), IF_THEN_ELSE(PRO_ECONOMY_CORRESPONDENCE_I= PROTRA_CHP_liquid_fuels_CCS:AND:SECTORS_TRANSFORMATION_ENERGY_I=REFINING:AN D: SECTORS_TRANSFORMATION_ENERGY_MAP_I=ELECTRICITY_OIL, TI_by_PROTRA_and_commodity[REGIONS_9_I,PROTRA_CHP_liquid_fuels_CCS,TI_liquid_bio]*ZID Z(PROTRA_TO_allocated[REGIONS_9_I, TO_elec,PROTRA_CHP_liquid_fuels_CCS], SUM(PROTRA_TO_allocated[REGIONS_9_I,NRG_TO_I!,PROTRA_CHP_liquid_fuels_CCS]) )+TI_by_PROTRA_and_commodity [REGIONS_9_I,PROTRA_CHP_liquid_fuels_CCS,TI_liquid_fossil]*ZIDZ(PROTRA_TO_allocated[R EGIONS_9_I,TO_elec,PROTRA_CHP_liquid_fuels_CCS ], SUM(PROTRA_TO_allocated[REGIONS_9_I,NRG_TO_I!,PROTRA_CHP_liquid_fuels_CCS])), IF_THEN_ELSE(PRO_ECONOMY_CORRESPONDENCE_I= PROTRA_CHP_liquid_fuels_CCS:AND:SECTORS_TRANSFORMATION_ENERGY_I=REFINING:AN D: SECTORS_TRANSFORMATION_ENERGY_MAP_I=STEAM_HOT_WATER, TI_by_PROTRA_and_commodity[REGIONS_9_I,PROTRA_CHP_liquid_fuels_CCS,TI_liquid_bio]*ZID Z(PROTRA_TO_allocated[REGIONS_9_I, TO_heat,PROTRA_CHP_liquid_fuels_CCS], SUM(PROTRA_TO_allocated[REGIONS_9_I,NRG_TO_I!,PROTRA_CHP_liquid_fuels_CCS]) )+TI_by_PROTRA_and_commodity [REGIONS_9_I,PROTRA_CHP_liquid_fuels_CCS,TI_liquid_fossil]*ZIDZ(PROTRA_TO_allocated[R EGIONS_9_I,TO_heat,PROTRA_CHP_liquid_fuels_CCS ], SUM(PROTRA_TO_allocated[REGIONS_9_I,NRG_TO_I!,PROTRA_CHP_liquid_fuels_CCS])), IF_THEN_ELSE(PRO_ECONOMY_CORRESPONDENCE_I= PROTRA_HP_gas_fuels:AND:SECTORS_TRANSFORMATION_ENERGY_I=DISTRIBUTION_GAS:AN D: SECTORS_TRANSFORMATION_ENERGY_MAP_I=STEAM_HOT_WATER, TI_by_PROTRA_and_commodity[REGIONS_9_I,PROTRA_HP_gas_fuels,TI_gas_bio]*ZIDZ(PROTRA_TO _allocated[REGIONS_9_I,TO_heat,PROTRA_HP_gas_fuels ], SUM(PROTRA_TO_allocated[REGIONS_9_I,NRG_TO_I!,PROTRA_HP_gas_fuels]))+TI_by_ PROTRA_and_commodity[REGIONS_9_I,PROTRA_HP_gas_fuels ,TI_gas_fossil]*ZIDZ(PROTRA_TO_allocated[REGIONS_9_I,TO_heat,PROTRA_HP_gas_fuels], SUM(PROTRA_TO_allocated[REGIONS_9_I,NRG_TO_I !,PROTRA_HP_gas_fuels])), IF_THEN_ELSE(PRO_ECONOMY_CORRESPONDENCE_I= PROTRA_HP_liquid_fuels:AND:SECTORS_TRANSFORMATION_ENERGY_I=REFINING:AND:SEC TORS_TRANSFORMATION_ENERGY_MAP_I =STEAM_HOT_WATER, TI_by_PROTRA_and_commodity[REGIONS_9_I,PROTRA_HP_liquid_fuels,TI_liquid_bio]*ZIDZ(PRO TRA_TO_allocated[REGIONS_9_I,TO_heat ,PROTRA_HP_liquid_fuels], SUM(PROTRA_TO_allocated[REGIONS_9_I,NRG_TO_I!,PROTRA_HP_liquid_fuels]))+TI_ by_PROTRA_and_commodity [REGIONS_9_I,PROTRA_HP_liquid_fuels,TI_liquid_fossil]*ZIDZ(PROTRA_TO_allocated[REGION S_9_I,TO_heat,PROTRA_HP_liquid_fuels ], SUM(PROTRA_TO_allocated[REGIONS_9_I,NRG_TO_I!,PROTRA_HP_liquid_fuels])), IF_THEN_ELSE(PRO_ECONOMY_CORRESPONDENCE_I= PROTRA_HP_solid_fossil:AND:SECTORS_TRANSFORMATION_ENERGY_I=MINING_COAL:AND: SECTORS_TRANSFORMATION_ENERGY_MAP_I =STEAM_HOT_WATER, TI_by_PROTRA_and_commodity[REGIONS_9_I,PROTRA_HP_solid_fossil,TI_solid_fossil]*ZIDZ(P ROTRA_TO_allocated[REGIONS_9_I,TO_heat ,PROTRA_HP_solid_fossil], SUM(PROTRA_TO_allocated[REGIONS_9_I,NRG_TO_I!,PROTRA_HP_solid_fossil])), IF_THEN_ELSE(PRO_ECONOMY_CORRESPONDENCE_I=PROTRA_HP_solid_bio:AND:SECTORS_TRANSFORMAT ION_ENERGY_I=FORESTRY:AND:SECTORS_TRANSFORMATION_ENERGY_MAP_I =STEAM_HOT_WATER, TI_by_PROTRA_and_commodity[REGIONS_9_I,PROTRA_HP_solid_bio,TI_solid_bio]*ZIDZ(PROTRA_ TO_allocated[REGIONS_9_I,TO_heat,PROTRA_HP_solid_bio ], SUM(PROTRA_TO_allocated[REGIONS_9_I,NRG_TO_I!,PROTRA_HP_solid_bio])), IF_THEN_ELSE(PRO_ECONOMY_CORRESPONDENCE_I=PROTRA_CHP_solid_bio:AND:SECTORS_TRANSFORMA TION_ENERGY_I=FORESTRY:AND:SECTORS_TRANSFORMATION_ENERGY_MAP_I =ELECTRICITY_OTHER, TI_by_PROTRA_and_commodity[REGIONS_9_I,PROTRA_CHP_solid_bio,TI_solid_bio]*ZIDZ(PROTRA _TO_allocated[REGIONS_9_I,TO_elec, PROTRA_CHP_solid_bio], SUM(PROTRA_TO_allocated[REGIONS_9_I,NRG_TO_I!,PROTRA_CHP_solid_bio])), IF_THEN_ELSE(PRO_ECONOMY_CORRESPONDENCE_I=PROTRA_CHP_solid_bio:AND:SECTORS_TRANSFORMA TION_ENERGY_I=FORESTRY:AND:SECTORS_TRANSFORMATION_ENERGY_MAP_I =STEAM_HOT_WATER, TI_by_PROTRA_and_commodity[REGIONS_9_I,PROTRA_CHP_solid_bio,TI_solid_bio]*ZIDZ(PROTRA _TO_allocated[REGIONS_9_I,TO_heat, PROTRA_CHP_solid_bio], SUM(PROTRA_TO_allocated[REGIONS_9_I,NRG_TO_I!,PROTRA_CHP_solid_bio])), IF_THEN_ELSE(PRO_ECONOMY_CORRESPONDENCE_I=PROTRA_PP_solid_bio:AND:SECTORS_TRANSFORMAT ION_ENERGY_I=FORESTRY:AND:SECTORS_TRANSFORMATION_ENERGY_MAP_I =STEAM_HOT_WATER, TI_by_PROTRA_and_commodity[REGIONS_9_I,PROTRA_PP_solid_bio,TI_solid_bio]*ZIDZ(PROTRA_ TO_allocated[REGIONS_9_I,TO_elec,PROTRA_PP_solid_bio ], SUM(PROTRA_TO_allocated[REGIONS_9_I,NRG_TO_I!,PROTRA_PP_solid_bio])), IF_THEN_ELSE(PRO_ECONOMY_CORRESPONDENCE_I=PROTRA_PP_solid_bio_CCS:AND:SECTORS_TRANSFO RMATION_ENERGY_I=FORESTRY:AND:SECTORS_TRANSFORMATION_ENERGY_MAP_I =ELECTRICITY_OTHER, TI_by_PROTRA_and_commodity[REGIONS_9_I,PROTRA_PP_solid_bio_CCS,TI_solid_bio]*ZIDZ(PRO TRA_TO_allocated[REGIONS_9_I,TO_elec ,PROTRA_PP_solid_bio_CCS], SUM(PROTRA_TO_allocated[REGIONS_9_I,NRG_TO_I!,PROTRA_PP_solid_bio_CCS])), IF_THEN_ELSE(PRO_ECONOMY_CORRESPONDENCE_I=PROTRA_PP_gas_fuels:AND:SECTORS_TRANSFORMAT ION_ENERGY_I=DISTRIBUTION_GAS:AND: SECTORS_TRANSFORMATION_ENERGY_MAP_I=ELECTRICITY_GAS, TI_by_PROTRA_and_commodity[REGIONS_9_I,PROTRA_PP_gas_fuels,TI_gas_bio]*ZIDZ(PROTRA_TO _allocated[REGIONS_9_I,TO_elec,PROTRA_PP_gas_fuels ], SUM(PROTRA_TO_allocated[REGIONS_9_I,NRG_TO_I!,PROTRA_PP_gas_fuels]))+TI_by_ PROTRA_and_commodity[REGIONS_9_I,PROTRA_PP_gas_fuels ,TI_gas_fossil]*ZIDZ(PROTRA_TO_allocated[REGIONS_9_I,TO_elec,PROTRA_PP_gas_fuels], SUM(PROTRA_TO_allocated[REGIONS_9_I,NRG_TO_I !,PROTRA_PP_gas_fuels])), IF_THEN_ELSE(PRO_ECONOMY_CORRESPONDENCE_I=PROTRA_PP_liquid_fuels:AND:SECTORS_TRANSFOR MATION_ENERGY_I=REFINING:AND:SECTORS_TRANSFORMATION_ENERGY_MAP_I =ELECTRICITY_OIL, TI_by_PROTRA_and_commodity[REGIONS_9_I,PROTRA_PP_liquid_fuels,TI_liquid_bio]*ZIDZ(PRO TRA_TO_allocated[REGIONS_9_I,TO_elec ,PROTRA_PP_liquid_fuels], SUM(PROTRA_TO_allocated[REGIONS_9_I,NRG_TO_I!,PROTRA_PP_liquid_fuels]))+TI_ by_PROTRA_and_commodity [REGIONS_9_I,PROTRA_PP_liquid_fuels,TI_liquid_fossil]*ZIDZ(PROTRA_TO_allocated[REGION S_9_I,TO_elec,PROTRA_PP_liquid_fuels ], SUM(PROTRA_TO_allocated[REGIONS_9_I,NRG_TO_I!,PROTRA_PP_liquid_fuels])), IF_THEN_ELSE(PRO_ECONOMY_CORRESPONDENCE_I=PROTRA_PP_nuclear:AND:SECTORS_TRANSFORMATIO N_ENERGY_I=MINING_AND_MANUFACTURING_URANIUM_THORIUM :AND:SECTORS_TRANSFORMATION_ENERGY_MAP_I=ELECTRICITY_NUCLEAR, TI_by_PROTRA_and_commodity[REGIONS_9_I,PROTRA_PP_nuclear,TI_nuclear]*ZIDZ(PROTRA_TO_a llocated[REGIONS_9_I,TO_elec,PROTRA_PP_nuclear ], SUM(PROTRA_TO_allocated[REGIONS_9_I,NRG_TO_I!,PROTRA_PP_nuclear])), IF_THEN_ELSE(PRO_ECONOMY_CORRESPONDENCE_I=PROTRA_PP_solid_fossil:AND:SECTORS_TRANSFOR MATION_ENERGY_I=MINING_COAL:AND:SECTORS_TRANSFORMATION_ENERGY_MAP_I =ELECTRICITY_COAL, TI_by_PROTRA_and_commodity[REGIONS_9_I,PROTRA_PP_solid_fossil,TI_solid_fossil]*ZIDZ(P ROTRA_TO_allocated[REGIONS_9_I,TO_elec ,PROTRA_PP_solid_fossil], SUM(PROTRA_TO_allocated[REGIONS_9_I,NRG_TO_I!,PROTRA_PP_solid_fossil])), IF_THEN_ELSE(PRO_ECONOMY_CORRESPONDENCE_I=PROTRA_PP_solid_fossil_CCS:AND:SECTORS_TRAN SFORMATION_ENERGY_I=MINING_COAL:AND: SECTORS_TRANSFORMATION_ENERGY_MAP_I=ELECTRICITY_COAL, TI_by_PROTRA_and_commodity[REGIONS_9_I,PROTRA_PP_solid_fossil_CCS,TI_solid_fossil]*ZI DZ(PROTRA_TO_allocated[REGIONS_9_I ,TO_elec,PROTRA_PP_solid_fossil_CCS], SUM(PROTRA_TO_allocated[REGIONS_9_I,NRG_TO_I!,PROTRA_PP_solid_fossil_CCS])) , IF_THEN_ELSE(PRO_ECONOMY_CORRESPONDENCE_I=PROTRA_blending_gas_fuels:AND:SECTORS_TRANS FORMATION_ENERGY_I=DISTRIBUTION_GAS :AND:SECTORS_TRANSFORMATION_ENERGY_MAP_I=DISTRIBUTION_GAS, TI_by_PROTRA_and_commodity[REGIONS_9_I,PROTRA_blending_gas_fuels,TI_gas_bio]*ZIDZ(PRO TRA_TO_allocated[REGIONS_9_I,TO_gas ,PROTRA_blending_gas_fuels], SUM(PROTRA_TO_allocated[REGIONS_9_I,NRG_TO_I!,PROTRA_blending_gas_fuels]))+ TI_by_PROTRA_and_commodity [REGIONS_9_I,PROTRA_blending_gas_fuels,TI_gas_fossil]*ZIDZ(PROTRA_TO_allocated[REGION S_9_I,TO_gas,PROTRA_blending_gas_fuels ], SUM(PROTRA_TO_allocated[REGIONS_9_I,NRG_TO_I!,PROTRA_blending_gas_fuels])), IF_THEN_ELSE(PRO_ECONOMY_CORRESPONDENCE_I=PROTRA_blending_liquid_fuels:AND:SECTORS_TR ANSFORMATION_ENERGY_I=REFINING:AND: SECTORS_TRANSFORMATION_ENERGY_MAP_I=REFINING, TI_by_PROTRA_and_commodity[REGIONS_9_I,PROTRA_blending_liquid_fuels,TI_liquid_bio]*ZI DZ(PROTRA_TO_allocated[REGIONS_9_I ,TO_liquid,PROTRA_blending_liquid_fuels], SUM(PROTRA_TO_allocated[REGIONS_9_I,NRG_TO_I!,PROTRA_blending_liquid_fuels] ))+ TI_by_PROTRA_and_commodity[REGIONS_9_I,PROTRA_blending_liquid_fuels,TI_liquid_fossil] *ZIDZ(PROTRA_TO_allocated[REGIONS_9_I ,TO_liquid,PROTRA_blending_liquid_fuels], SUM(PROTRA_TO_allocated[REGIONS_9_I,NRG_TO_I!,PROTRA_blending_liquid_fuels] )), IF_THEN_ELSE(PRO_ECONOMY_CORRESPONDENCE_I=PROTRA_PP_gas_fuels_CCS:AND:SECTORS_TRANSFO RMATION_ENERGY_I=DISTRIBUTION_GAS:AND: SECTORS_TRANSFORMATION_ENERGY_MAP_I=ELECTRICITY_GAS, TI_by_PROTRA_and_commodity[REGIONS_9_I,PROTRA_PP_gas_fuels_CCS,TI_gas_bio]*ZIDZ(PROTR A_TO_allocated[REGIONS_9_I,TO_elec ,PROTRA_PP_gas_fuels_CCS], SUM(PROTRA_TO_allocated[REGIONS_9_I,NRG_TO_I!,PROTRA_PP_gas_fuels_CCS]))+TI _by_PROTRA_and_commodity [REGIONS_9_I,PROTRA_PP_gas_fuels_CCS,TI_gas_fossil]*ZIDZ(PROTRA_TO_allocated[REGIONS_ 9_I,TO_elec,PROTRA_PP_gas_fuels_CCS ], SUM(PROTRA_TO_allocated[REGIONS_9_I,NRG_TO_I!,PROTRA_PP_gas_fuels_CCS])), IF_THEN_ELSE(PRO_ECONOMY_CORRESPONDENCE_I=PROTRA_PP_liquid_fuels_CCS:AND:SECTORS_TRAN SFORMATION_ENERGY_I=REFINING:AND:SECTORS_TRANSFORMATION_ENERGY_MAP_I =ELECTRICITY_OIL, TI_by_PROTRA_and_commodity[REGIONS_9_I,PROTRA_PP_liquid_fuels_CCS,TI_liquid_bio]*ZIDZ (PROTRA_TO_allocated[REGIONS_9_I,TO_elec ,PROTRA_PP_liquid_fuels_CCS], SUM(PROTRA_TO_allocated[REGIONS_9_I,NRG_TO_I!,PROTRA_PP_liquid_fuels_CCS])) +TI_by_PROTRA_and_commodity [REGIONS_9_I,PROTRA_PP_liquid_fuels_CCS,TI_liquid_fossil]*ZIDZ(PROTRA_TO_allocated[RE GIONS_9_I,TO_elec,PROTRA_PP_liquid_fuels_CCS ], SUM(PROTRA_TO_allocated[REGIONS_9_I,NRG_TO_I!,PROTRA_PP_liquid_fuels_CCS])), IF_THEN_ELSE(PRO_ECONOMY_CORRESPONDENCE_I=PROREF_refinery_bio:AND:SECTORS_TRANSFORMAT ION_ENERGY_I=CROPS:AND:SECTORS_TRANSFORMATION_ENERGY_MAP_I =REFINING, PE_by_PROREF_and_commodity[REGIONS_9_I,PROREF_refinery_bio,PE_agriculture_products]*Z IDZ(TI_by_PROREF_and_commodity[REGIONS_9_I ,PROREF_refinery_bio,TI_gas_bio], SUM(TI_by_PROREF_and_commodity[REGIONS_9_I,PROREF_refinery_bio,NRG_TI_I!])) +PE_by_PROREF_and_commodity [REGIONS_9_I,PROREF_refinery_bio,PE_agriculture_products]*ZIDZ(TI_by_PROREF_and_commo dity[REGIONS_9_I,PROREF_refinery_bio ,TI_liquid_bio], SUM(TI_by_PROREF_and_commodity[REGIONS_9_I,PROREF_refinery_bio,NRG_TI_I!])) , IF_THEN_ELSE(PRO_ECONOMY_CORRESPONDENCE_I=PROREF_refinery_bio:AND:SECTORS_TRANSFORMAT ION_ENERGY_I=FORESTRY:AND:SECTORS_TRANSFORMATION_ENERGY_MAP_I =REFINING, PE_by_PROREF_and_commodity[REGIONS_9_I,PROREF_refinery_bio,PE_forestry_products]*ZIDZ (TI_by_PROREF_and_commodity[REGIONS_9_I ,PROREF_refinery_bio,TI_gas_bio], SUM(TI_by_PROREF_and_commodity[REGIONS_9_I,PROREF_refinery_bio,NRG_TI_I!])) +PE_by_PROREF_and_commodity [REGIONS_9_I,PROREF_refinery_bio,PE_forestry_products]*ZIDZ(TI_by_PROREF_and_commodit y[REGIONS_9_I,PROREF_refinery_bio,TI_liquid_bio ], SUM(TI_by_PROREF_and_commodity[REGIONS_9_I,PROREF_refinery_bio,NRG_TI_I!])), IF_THEN_ELSE(PRO_ECONOMY_CORRESPONDENCE_I=PROREF_refinery_bio:AND:SECTORS_TRANSFORMAT ION_ENERGY_I=CROPS:AND:SECTORS_TRANSFORMATION_ENERGY_MAP_I =HYDROGEN_PRODUCTION, PE_by_PROREF_and_commodity[REGIONS_9_I,PROREF_refinery_bio,PE_agriculture_products]*Z IDZ(TI_by_PROREF_and_commodity[REGIONS_9_I ,PROREF_refinery_bio,TI_hydrogen], SUM(TI_by_PROREF_and_commodity[REGIONS_9_I,PROREF_refinery_bio,NRG_TI_I!])) , IF_THEN_ELSE(PRO_ECONOMY_CORRESPONDENCE_I=PROREF_refinery_bio:AND:SECTORS_TRANSFORMAT ION_ENERGY_I=FORESTRY:AND:SECTORS_TRANSFORMATION_ENERGY_MAP_I =HYDROGEN_PRODUCTION, PE_by_PROREF_and_commodity[REGIONS_9_I,PROREF_refinery_bio,PE_forestry_products]*ZIDZ (TI_by_PROREF_and_commodity[REGIONS_9_I ,PROREF_refinery_bio,TI_hydrogen], SUM(TI_by_PROREF_and_commodity[REGIONS_9_I,PROREF_refinery_bio,NRG_TI_I!])) , IF_THEN_ELSE(PRO_ECONOMY_CORRESPONDENCE_I=PROREF_refinery_coal:AND:SECTORS_TRANSFORMA TION_ENERGY_I=MINING_COAL:AND:SECTORS_TRANSFORMATION_ENERGY_MAP_I =REFINING, PE_by_PROREF_and_commodity[REGIONS_9_I,PROREF_refinery_coal,PE_coal]*ZIDZ(TI_by_PRORE F_and_commodity[REGIONS_9_I,PROREF_refinery_coal ,TI_gas_fossil], SUM(TI_by_PROREF_and_commodity[REGIONS_9_I,PROREF_refinery_coal,NRG_TI_I!]) )+PE_by_PROREF_and_commodity [REGIONS_9_I,PROREF_refinery_coal,PE_coal]*ZIDZ(TI_by_PROREF_and_commodity[REGIONS_9_ I,PROREF_refinery_coal,TI_liquid_fossil ], SUM(TI_by_PROREF_and_commodity[REGIONS_9_I,PROREF_refinery_coal,NRG_TI_I!])), IF_THEN_ELSE(PRO_ECONOMY_CORRESPONDENCE_I=PROREF_refinery_coal:AND:SECTORS_TRANSFORMA TION_ENERGY_I=MINING_COAL:AND:SECTORS_TRANSFORMATION_ENERGY_MAP_I =HYDROGEN_PRODUCTION, PE_by_PROREF_and_commodity[REGIONS_9_I,PROREF_refinery_coal,PE_coal]*ZIDZ(TI_by_PRORE F_and_commodity[REGIONS_9_I,PROREF_refinery_coal ,TI_hydrogen], SUM(TI_by_PROREF_and_commodity[REGIONS_9_I,PROREF_refinery_coal,NRG_TI_I!]) ), IF_THEN_ELSE(PRO_ECONOMY_CORRESPONDENCE_I=PROREF_refinery_oil:AND:SECTORS_TRANSFORMAT ION_ENERGY_I=EXTRACTION_OIL:AND:SECTORS_TRANSFORMATION_ENERGY_MAP_I =REFINING, PE_by_PROREF_and_commodity[REGIONS_9_I,PROREF_refinery_oil,PE_oil]*ZIDZ(TI_by_PROREF_ and_commodity[REGIONS_9_I,PROREF_refinery_oil ,TI_gas_fossil], SUM(TI_by_PROREF_and_commodity[REGIONS_9_I,PROREF_refinery_oil,NRG_TI_I!])) +PE_by_PROREF_and_commodity[ REGIONS_9_I,PROREF_refinery_oil,PE_oil]*ZIDZ(TI_by_PROREF_and_commodity[REGIONS_9_I,P ROREF_refinery_oil,TI_liquid_fossil ], SUM(TI_by_PROREF_and_commodity[REGIONS_9_I,PROREF_refinery_oil,NRG_TI_I!])), IF_THEN_ELSE(PRO_ECONOMY_CORRESPONDENCE_I=PROREF_transformation_PE_natural_gas_2_TI_h ydrogen:AND:SECTORS_TRANSFORMATION_ENERGY_I =DISTRIBUTION_GAS:AND:SECTORS_TRANSFORMATION_ENERGY_MAP_I=HYDROGEN_PRODUCTION, PE_by_PROREF_and_commodity[REGIONS_9_I,PROREF_transformation_PE_natural_gas_2_TI_hydr ogen,PE_natural_gas]*ZIDZ(TI_by_PROREF_and_commodity [REGIONS_9_I,PROREF_transformation_PE_natural_gas_2_TI_hydrogen,TI_hydrogen], SUM(TI_by_PROREF_and_commodity[REGIONS_9_I ,PROREF_transformation_PE_natural_gas_2_TI_hydrogen,NRG_TI_I!])), IF_THEN_ELSE(PRO_ECONOMY_CORRESPONDENCE_I=PROSUP_transmission_losses_elec:AND:SECTORS _TRANSFORMATION_ENERGY_I=DISTRIBUTION_ELECTRICITY :AND:SECTORS_TRANSFORMATION_ENERGY_MAP_I=DISTRIBUTION_ELECTRICITY, PROSUP_transmission_losses[REGIONS_9_I,TO_elec], IF_THEN_ELSE(PRO_ECONOMY_CORRESPONDENCE_I=PROSUP_transmission_losses_gas:AND:SECTORS_ TRANSFORMATION_ENERGY_I=DISTRIBUTION_GAS :AND:SECTORS_TRANSFORMATION_ENERGY_MAP_I=DISTRIBUTION_GAS, PROSUP_transmission_losses[REGIONS_9_I,TO_gas], IF_THEN_ELSE(PRO_ECONOMY_CORRESPONDENCE_I=PROSUP_transmission_losses_heat:AND:SECTORS _TRANSFORMATION_ENERGY_I=STEAM_HOT_WATER :AND:SECTORS_TRANSFORMATION_ENERGY_MAP_I=STEAM_HOT_WATER, PROSUP_transmission_losses[REGIONS_9_I,TO_heat], IF_THEN_ELSE(PRO_ECONOMY_CORRESPONDENCE_I=PROSUP_storage_losses_elec:AND:SECTORS_TRAN SFORMATION_ENERGY_I=DISTRIBUTION_ELECTRICITY :AND:SECTORS_TRANSFORMATION_ENERGY_MAP_I=DISTRIBUTION_ELECTRICITY, PROSUP_storage_losses[REGIONS_9_I,TO_elec], IF_THEN_ELSE(PRO_ECONOMY_CORRESPONDENCE_I=PROSUP_storage_losses_gas:AND:SECTORS_TRANS FORMATION_ENERGY_I=DISTRIBUTION_GAS :AND:SECTORS_TRANSFORMATION_ENERGY_MAP_I=DISTRIBUTION_GAS, PROSUP_storage_losses[REGIONS_9_I,TO_gas], IF_THEN_ELSE(PRO_ECONOMY_CORRESPONDENCE_I=PROSUP_storage_losses_heat:AND:SECTORS_TRAN SFORMATION_ENERGY_I=STEAM_HOT_WATER :AND:SECTORS_TRANSFORMATION_ENERGY_MAP_I=STEAM_HOT_WATER, PROSUP_storage_losses[REGIONS_9_I,TO_heat], IF_THEN_ELSE(PRO_ECONOMY_CORRESPONDENCE_I=PROSUP_P2H_heat_pump:AND:SECTORS_TRANSFORMA TION_ENERGY_I=DISTRIBUTION_ELECTRICITY :AND:SECTORS_TRANSFORMATION_ENERGY_MAP_I=STEAM_HOT_WATER, PROSUP_flexibility_technologies[REGIONS_9_I, PROSUP_P2H_heat_pump,TO_elec], IF_THEN_ELSE(PRO_ECONOMY_CORRESPONDENCE_I=PROSUP_P2H_electric_boiler:AND:SECTORS_TRAN SFORMATION_ENERGY_I=DISTRIBUTION_ELECTRICITY :AND:SECTORS_TRANSFORMATION_ENERGY_MAP_I=STEAM_HOT_WATER, PROSUP_flexibility_technologies[REGIONS_9_I, PROSUP_P2H_electric_boiler,TO_elec], IF_THEN_ELSE(PRO_ECONOMY_CORRESPONDENCE_I=PROSUP_elec_2_liquid:AND:SECTORS_TRANSFORMA TION_ENERGY_I=DISTRIBUTION_ELECTRICITY :AND:SECTORS_TRANSFORMATION_ENERGY_MAP_I=HYDROGEN_PRODUCTION, PROSUP_flexibility_technologies[REGIONS_9_I,PROSUP_elec_2_liquid,TO_elec], IF_THEN_ELSE(PRO_ECONOMY_CORRESPONDENCE_I=PROSUP_elec_2_gas:AND:SECTORS_TRANSFORMATIO N_ENERGY_I=DISTRIBUTION_ELECTRICITY :AND:SECTORS_TRANSFORMATION_ENERGY_MAP_I=HYDROGEN_PRODUCTION, PROSUP_flexibility_technologies[REGIONS_9_I,PROSUP_elec_2_gas,TO_elec], IF_THEN_ELSE(PRO_ECONOMY_CORRESPONDENCE_I=PROSUP_sector_energy_own_consumption_elec:A ND:SECTORS_TRANSFORMATION_ENERGY_I =DISTRIBUTION_ELECTRICITY:AND:SECTORS_TRANSFORMATION_ENERGY_MAP_I=DISTRIBUTION_ELECTR ICITY, PROSUP_sector_energy_own_consumption_per_commodity[REGIONS_9_I,TO_elec], IF_THEN_ELSE(PRO_ECONOMY_CORRESPONDENCE_I=PROSUP_sector_energy_own_consumption_gas:AN D:SECTORS_TRANSFORMATION_ENERGY_I= DISTRIBUTION_GAS:AND:SECTORS_TRANSFORMATION_ENERGY_MAP_I=DISTRIBUTION_GAS, PROSUP_sector_energy_own_consumption_per_commodity[REGIONS_9_I,TO_gas], IF_THEN_ELSE(PRO_ECONOMY_CORRESPONDENCE_I=PROSUP_sector_energy_own_consumption_heat:A ND:SECTORS_TRANSFORMATION_ENERGY_I =STEAM_HOT_WATER:AND:SECTORS_TRANSFORMATION_ENERGY_MAP_I=STEAM_HOT_WATER, PROSUP_sector_energy_own_consumption_per_commodity[REGIONS_9_I,TO_heat], IF_THEN_ELSE(PRO_ECONOMY_CORRESPONDENCE_I=PROSUP_sector_energy_own_consumption_liquid :AND:SECTORS_TRANSFORMATION_ENERGY_I =REFINING:AND:SECTORS_TRANSFORMATION_ENERGY_MAP_I=REFINING, PROSUP_sector_energy_own_consumption_per_commodity[REGIONS_9_I,TO_liquid], IF_THEN_ELSE(PRO_ECONOMY_CORRESPONDENCE_I=PROSUP_elec_2_hydrogen:AND:SECTORS_TRANSFOR MATION_ENERGY_I=DISTRIBUTION_ELECTRICITY :AND:SECTORS_TRANSFORMATION_ENERGY_MAP_I=HYDROGEN_PRODUCTION, PROSUP_flexibility_technologies[REGIONS_9_I,PROSUP_elec_2_hydrogen,TO_elec], IF_THEN_ELSE(PRO_ECONOMY_CORRESPONDENCE_I=PROSUP_sector_energy_own_consumption_solid_ fossil:AND:SECTORS_TRANSFORMATION_ENERGY_I =MINING_COAL:AND:SECTORS_TRANSFORMATION_ENERGY_MAP_I=ELECTRICITY_COAL, PROSUP_sector_energy_own_consumption_per_commodity[REGIONS_9_I,TO_solid_fossil] ,0)))))))))))))))))))))))))))))))))))))))))))))))))))))))
    """
    return xr.DataArray(
        0,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "PRO_ECONOMY_CORRESPONDENCE_I": _subscript_dict[
                "PRO_ECONOMY_CORRESPONDENCE_I"
            ],
            "SECTORS_TRANSFORMATION_ENERGY_I": _subscript_dict[
                "SECTORS_TRANSFORMATION_ENERGY_I"
            ],
            "SECTORS_TRANSFORMATION_ENERGY_MAP_I": _subscript_dict[
                "SECTORS_TRANSFORMATION_ENERGY_MAP_I"
            ],
        },
        [
            "REGIONS_9_I",
            "PRO_ECONOMY_CORRESPONDENCE_I",
            "SECTORS_TRANSFORMATION_ENERGY_I",
            "SECTORS_TRANSFORMATION_ENERGY_MAP_I",
        ],
    )


@component.add(
    name="economy_energy_transformation_matrix_input_aggregated",
    units="EJ/Year",
    subscripts=[
        "REGIONS_9_I",
        "SECTORS_TRANSFORMATION_ENERGY_I",
        "SECTORS_TRANSFORMATION_ENERGY_MAP_I",
    ],
    comp_type="Constant",
    comp_subtype="Normal",
)
def economy_energy_transformation_matrix_input_aggregated():
    """
    SUM(economy_energy_transformation_input[REGIONS_9_I,PRO_ECONOMY_CORRESPONDE NCE_I!,SECTORS_TRANSFORMATION_ENERGY_I,SECTORS_TRANSFORMATION_ENERGY_MAP_I] )
    """
    return xr.DataArray(
        0,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "SECTORS_TRANSFORMATION_ENERGY_I": _subscript_dict[
                "SECTORS_TRANSFORMATION_ENERGY_I"
            ],
            "SECTORS_TRANSFORMATION_ENERGY_MAP_I": _subscript_dict[
                "SECTORS_TRANSFORMATION_ENERGY_MAP_I"
            ],
        },
        [
            "REGIONS_9_I",
            "SECTORS_TRANSFORMATION_ENERGY_I",
            "SECTORS_TRANSFORMATION_ENERGY_MAP_I",
        ],
    )


@component.add(
    name="economy_energy_transformation_output",
    units="EJ/Year",
    subscripts=[
        "REGIONS_9_I",
        "PRO_ECONOMY_CORRESPONDENCE_I",
        "SECTORS_TRANSFORMATION_ENERGY_I",
        "SECTORS_TRANSFORMATION_ENERGY_MAP_I",
    ],
    comp_type="Constant",
    comp_subtype="Normal",
)
def economy_energy_transformation_output():
    """
    physical energy flows corresponding to monetary OUTPUT flows from SECTORS_TRANSFORMATION_ENERGY_I (economic ROW of A-Matrix) to SECTORS_TRANSFORMATION_ENERGY_MAP_I (column of A-Matrix). Note: Stated in one complicated if-then-else equation because of VENSIM-bug with :EXCEPT:
    """
    return xr.DataArray(
        0,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "PRO_ECONOMY_CORRESPONDENCE_I": _subscript_dict[
                "PRO_ECONOMY_CORRESPONDENCE_I"
            ],
            "SECTORS_TRANSFORMATION_ENERGY_I": _subscript_dict[
                "SECTORS_TRANSFORMATION_ENERGY_I"
            ],
            "SECTORS_TRANSFORMATION_ENERGY_MAP_I": _subscript_dict[
                "SECTORS_TRANSFORMATION_ENERGY_MAP_I"
            ],
        },
        [
            "REGIONS_9_I",
            "PRO_ECONOMY_CORRESPONDENCE_I",
            "SECTORS_TRANSFORMATION_ENERGY_I",
            "SECTORS_TRANSFORMATION_ENERGY_MAP_I",
        ],
    )


@component.add(
    name="economy_energy_transformation_output_aggregated",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "SECTORS_TRANSFORMATION_ENERGY_I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def economy_energy_transformation_output_aggregated():
    """
    SUM(economy_energy_transformation_output[REGIONS_9_I,PRO_ECONOMY_CORRESPOND ENCE_I!,SECTORS_TRANSFORMATION_ENERGY_I,SECTORS_TRANSFORMATION_ENERGY_MAP_I !])
    """
    return xr.DataArray(
        0,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "SECTORS_TRANSFORMATION_ENERGY_I": _subscript_dict[
                "SECTORS_TRANSFORMATION_ENERGY_I"
            ],
        },
        ["REGIONS_9_I", "SECTORS_TRANSFORMATION_ENERGY_I"],
    )


@component.add(
    name="exogenous_PROTRA_input_shares",
    units="1",
    subscripts=["REGIONS_9_I", "NRG_PROTRA_I", "NRG_TI_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_exogenous_protra_input_shares": 1},
    other_deps={
        "_integ_exogenous_protra_input_shares": {
            "initial": {"protra_input_shares_empiric": 1},
            "step": {"variation_exogenous_protra_input_shares": 1},
        }
    },
)
def exogenous_protra_input_shares():
    """
    Input fuel shares (some transformation processes can take more than one fuel, e.g. gas plants can be driven with biogas or fossil gas).
    """
    return _integ_exogenous_protra_input_shares()


_integ_exogenous_protra_input_shares = Integ(
    lambda: variation_exogenous_protra_input_shares(),
    lambda: protra_input_shares_empiric(),
    "_integ_exogenous_protra_input_shares",
)


@component.add(
    name="FE_domestic",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_FE_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"fe_net_import_share_by_region": 1, "fe_excluding_trade": 1},
)
def fe_domestic():
    """
    domestic part of TFC
    """
    return (
        (
            1
            - fe_net_import_share_by_region()
            .loc[:, _subscript_dict["REGIONS_9_I"]]
            .rename({"REGIONS_36_I": "REGIONS_9_I"})
        )
        * fe_excluding_trade().transpose("NRG_FE_I", "REGIONS_9_I")
    ).transpose("REGIONS_9_I", "NRG_FE_I")


@component.add(
    name="FE_excluding_trade",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_FE_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_nrg_demand_transformation": 1,
        "final_non_energy_demand_by_fe_9r": 1,
        "unit_conversion_tj_ej": 1,
        "final_energy_demand_by_fe_9r": 1,
        "iea_total_fe_empirical": 1,
    },
)
def fe_excluding_trade():
    """
    Final energy Demand coming from End-Use Submodule including both energy end-uses and non-energy uses. does NOT include imports or exports, only domestic demand. equivalent to Total Final Consumpton (TFC) in IEA energy balances.
    """
    return if_then_else(
        switch_nrg_demand_transformation() == 1,
        lambda: (final_energy_demand_by_fe_9r() + final_non_energy_demand_by_fe_9r())
        / unit_conversion_tj_ej(),
        lambda: iea_total_fe_empirical(),
    )


@component.add(
    name="FE_EXPORT_MARKET_SHARE",
    units="DMNL",
    subscripts=["NRG_FE_I", "REGIONS_36_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_fe_export_market_share"},
)
def fe_export_market_share():
    """
    Market share of global export market, extracted from IEA energy balances for 2015 and kept constant over the rest of the modelling horizon
    """
    return _ext_constant_fe_export_market_share()


_ext_constant_fe_export_market_share = ExtConstant(
    "model_parameters/energy/FE_Trade_Shares.xlsx",
    "VENSIM_IMPORT",
    "TFC_EXPORT_MARKET_SHARE",
    {
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
        "REGIONS_36_I": _subscript_dict["REGIONS_36_I"],
    },
    _root,
    {
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
        "REGIONS_36_I": _subscript_dict["REGIONS_36_I"],
    },
    "_ext_constant_fe_export_market_share",
)


@component.add(
    name="FE_net_exports_by_region",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_FE_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"global_fe_trade": 1, "fe_export_market_share": 1},
)
def fe_net_exports_by_region():
    """
    TFC exports
    """
    return (
        global_fe_trade()
        * fe_export_market_share()
        .loc[:, _subscript_dict["REGIONS_9_I"]]
        .rename({"REGIONS_36_I": "REGIONS_9_I"})
    ).transpose("REGIONS_9_I", "NRG_FE_I")


@component.add(
    name="FE_NET_IMPORT_SHARE_BY_REGION",
    units="DMNL",
    subscripts=["NRG_FE_I", "REGIONS_36_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_fe_net_import_share_by_region"},
)
def fe_net_import_share_by_region():
    """
    Import shares gross domestic consumption derived from IEA energy balances (fixed for further simulation)
    """
    return _ext_constant_fe_net_import_share_by_region()


_ext_constant_fe_net_import_share_by_region = ExtConstant(
    "model_parameters/energy/FE_Trade_Shares.xlsx",
    "VENSIM_IMPORT",
    "TFC_IMPORT_SHARE_BY_REGION",
    {
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
        "REGIONS_36_I": _subscript_dict["REGIONS_36_I"],
    },
    _root,
    {
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
        "REGIONS_36_I": _subscript_dict["REGIONS_36_I"],
    },
    "_ext_constant_fe_net_import_share_by_region",
)


@component.add(
    name="FE_net_imports",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_FE_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"fe_excluding_trade": 1, "fe_net_import_share_by_region": 1},
)
def fe_net_imports():
    """
    Imports of final energy calculated from fixed import share.
    """
    return fe_excluding_trade() * fe_net_import_share_by_region().loc[
        :, _subscript_dict["REGIONS_9_I"]
    ].rename({"REGIONS_36_I": "REGIONS_9_I"}).transpose("REGIONS_9_I", "NRG_FE_I")


@component.add(
    name="global_FE_trade",
    units="EJ/Year",
    subscripts=["NRG_FE_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"fe_net_imports": 1},
)
def global_fe_trade():
    """
    Total market size of final energy trade = sum of all regions imports.
    """
    return sum(
        fe_net_imports().rename({"REGIONS_9_I": "REGIONS_9_I!"}), dim=["REGIONS_9_I!"]
    )


@component.add(
    name="IEA_TOTAL_FE_EMPIRICAL",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_FE_I"],
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_iea_total_fe_empirical",
        "__data__": "_ext_data_iea_total_fe_empirical",
        "time": 1,
    },
)
def iea_total_fe_empirical():
    """
    Empiric data for total final energy consumption from IEA energy balances in WILIAM regional aggregation
    """
    return _ext_data_iea_total_fe_empirical(time())


_ext_data_iea_total_fe_empirical = ExtData(
    "model_parameters/energy/FE_Trade_Shares.xlsx",
    "VENSIM_IMPORT",
    "TFC_TIME",
    "TFC_CHINA",
    "interpolate",
    {"REGIONS_9_I": ["CHINA"], "NRG_FE_I": _subscript_dict["NRG_FE_I"]},
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
    "_ext_data_iea_total_fe_empirical",
)

_ext_data_iea_total_fe_empirical.add(
    "model_parameters/energy/FE_Trade_Shares.xlsx",
    "VENSIM_IMPORT",
    "TFC_TIME",
    "TFC_INDIA",
    "interpolate",
    {"REGIONS_9_I": ["INDIA"], "NRG_FE_I": _subscript_dict["NRG_FE_I"]},
)

_ext_data_iea_total_fe_empirical.add(
    "model_parameters/energy/FE_Trade_Shares.xlsx",
    "VENSIM_IMPORT",
    "TFC_TIME",
    "TFC_RUSSIA",
    "interpolate",
    {"REGIONS_9_I": ["RUSSIA"], "NRG_FE_I": _subscript_dict["NRG_FE_I"]},
)

_ext_data_iea_total_fe_empirical.add(
    "model_parameters/energy/FE_Trade_Shares.xlsx",
    "VENSIM_IMPORT",
    "TFC_TIME",
    "TFC_UK",
    "interpolate",
    {"REGIONS_9_I": ["UK"], "NRG_FE_I": _subscript_dict["NRG_FE_I"]},
)

_ext_data_iea_total_fe_empirical.add(
    "model_parameters/energy/FE_Trade_Shares.xlsx",
    "VENSIM_IMPORT",
    "TFC_TIME",
    "TFC_EU27",
    "interpolate",
    {"REGIONS_9_I": ["EU27"], "NRG_FE_I": _subscript_dict["NRG_FE_I"]},
)

_ext_data_iea_total_fe_empirical.add(
    "model_parameters/energy/FE_Trade_Shares.xlsx",
    "VENSIM_IMPORT",
    "TFC_TIME",
    "TFC_EASOC",
    "interpolate",
    {"REGIONS_9_I": ["EASOC"], "NRG_FE_I": _subscript_dict["NRG_FE_I"]},
)

_ext_data_iea_total_fe_empirical.add(
    "model_parameters/energy/FE_Trade_Shares.xlsx",
    "VENSIM_IMPORT",
    "TFC_TIME",
    "TFC_LATAM",
    "interpolate",
    {"REGIONS_9_I": ["LATAM"], "NRG_FE_I": _subscript_dict["NRG_FE_I"]},
)

_ext_data_iea_total_fe_empirical.add(
    "model_parameters/energy/FE_Trade_Shares.xlsx",
    "VENSIM_IMPORT",
    "TFC_TIME",
    "TFC_USMCA",
    "interpolate",
    {"REGIONS_9_I": ["USMCA"], "NRG_FE_I": _subscript_dict["NRG_FE_I"]},
)

_ext_data_iea_total_fe_empirical.add(
    "model_parameters/energy/FE_Trade_Shares.xlsx",
    "VENSIM_IMPORT",
    "TFC_TIME",
    "TFC_LROW",
    "interpolate",
    {"REGIONS_9_I": ["LROW"], "NRG_FE_I": _subscript_dict["NRG_FE_I"]},
)


@component.add(
    name="PE_by_commodity",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_PE_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"pe_by_proref_and_commodity": 1},
)
def pe_by_commodity():
    """
    Domestic primary energy (PE) demand/consumption resulting from final energy (FE) demand and the current energy system setup. +++++++++++ This formula can be used for debugging: IF_THEN_ELSE ( Time < 2006, SUM(PE_by_PROREF_and_commodity[REGIONS_9_I,NRG_PROREF_I!,NRG_PE_I]) , 0 )
    """
    return sum(
        pe_by_proref_and_commodity().rename({"NRG_PROREF_I": "NRG_PROREF_I!"}),
        dim=["NRG_PROREF_I!"],
    )


@component.add(
    name="PE_by_commodity_dem",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_PE_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"pe_by_proref_and_commodity_dem": 1},
)
def pe_by_commodity_dem():
    """
    Domestic primary energy (PE) demand/consumption resulting from final energy (FE) demand and the current energy system setup.
    """
    return sum(
        pe_by_proref_and_commodity_dem().rename({"NRG_PROREF_I": "NRG_PROREF_I!"}),
        dim=["NRG_PROREF_I!"],
    )


@component.add(
    name="PE_by_PROREF",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_PROREF_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ti_by_refinery_process": 1, "proref_conversion_factors": 1},
)
def pe_by_proref():
    """
    PE required taking into account refineration losses (oil refineration, coal refineration, bio refinery, and natural gas 2 hydrogen processing).
    """
    return xidz(ti_by_refinery_process(), proref_conversion_factors(), 0)


@component.add(
    name="PE_by_PROREF_and_commodity",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_PROREF_I", "NRG_PE_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"pe_by_proref": 1, "proref_input_shares_sp": 1},
)
def pe_by_proref_and_commodity():
    """
    PE disaggregated by refinery process and commodity
    """
    return pe_by_proref() * proref_input_shares_sp()


@component.add(
    name="PE_by_PROREF_and_commodity_dem",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_PROREF_I", "NRG_PE_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"pe_by_proref_dem": 1, "proref_input_shares_sp": 1},
)
def pe_by_proref_and_commodity_dem():
    """
    PE disaggregated by refinery process and commodity
    """
    return pe_by_proref_dem() * proref_input_shares_sp()


@component.add(
    name="PE_by_PROREF_dem",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_PROREF_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ti_by_refinery_process_dem": 1, "proref_conversion_factors": 1},
)
def pe_by_proref_dem():
    """
    PE required taking into account refineration losses (oil refineration, coal refineration, bio refinery, and natural gas 2 hydrogen processing).
    """
    return xidz(ti_by_refinery_process_dem(), proref_conversion_factors(), 0)


@component.add(
    name="PROSUP_flexibility_technologies",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_TO_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"prosup_to_p2h_technologies": 1, "to_commodities_h2": 1},
)
def prosup_flexibility_technologies():
    """
    Flexibility Technologies contain: Power2Heat, Synthetic Gas production, FE_Hydrogen production (=H2 & H2 derived Fuels for final consumption). Note: negative values for output values fo the process (because the it reduces the amount of TO that needs to be coveres by other processes), positive values for process-inputs (mostly electricity - because it increases the amount of electricity needed to run these flexibility processes).
    """
    return (
        sum(
            prosup_to_p2h_technologies().rename({"PROSUP_P2H_I": "PROSUP_P2H_I!"}),
            dim=["PROSUP_P2H_I!"],
        )
        + to_commodities_h2()
    )


@component.add(
    name="PROSUP_flexibility_technologies_demand_aggregated",
    subscripts=["REGIONS_9_I", "NRG_TO_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"prosup_flexibility_technologies": 1},
)
def prosup_flexibility_technologies_demand_aggregated():
    return prosup_flexibility_technologies()


@component.add(
    name="PROSUP_sector_energy_own_consumption_per_commodity",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_TO_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "fe_excluding_trade": 5,
        "prosup_energy_sector_own_consumption_share": 5,
    },
)
def prosup_sector_energy_own_consumption_per_commodity():
    """
    Energy sector own consumption for elec, gas, liquids and (district-)heat excluding storage losses (!)
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "NRG_TO_I": _subscript_dict["NRG_TO_I"],
        },
        ["REGIONS_9_I", "NRG_TO_I"],
    )
    value.loc[:, ["TO_elec"]] = (
        (
            fe_excluding_trade().loc[:, "FE_elec"].reset_coords(drop=True)
            * prosup_energy_sector_own_consumption_share()
            .loc[:, "PROSUP_sector_energy_own_consumption_elec"]
            .reset_coords(drop=True)
        )
        .expand_dims({"NRG_COMMODITIES_I": ["TO_elec"]}, 1)
        .values
    )
    value.loc[:, ["TO_gas"]] = (
        (
            fe_excluding_trade().loc[:, "FE_gas"].reset_coords(drop=True)
            * prosup_energy_sector_own_consumption_share()
            .loc[:, "PROSUP_sector_energy_own_consumption_gas"]
            .reset_coords(drop=True)
        )
        .expand_dims({"NRG_COMMODITIES_I": ["TO_gas"]}, 1)
        .values
    )
    value.loc[:, ["TO_heat"]] = (
        (
            fe_excluding_trade().loc[:, "FE_heat"].reset_coords(drop=True)
            * prosup_energy_sector_own_consumption_share()
            .loc[:, "PROSUP_sector_energy_own_consumption_heat"]
            .reset_coords(drop=True)
        )
        .expand_dims({"NRG_COMMODITIES_I": ["TO_heat"]}, 1)
        .values
    )
    value.loc[:, ["TO_hydrogen"]] = 0
    value.loc[:, ["TO_liquid"]] = (
        (
            fe_excluding_trade().loc[:, "FE_liquid"].reset_coords(drop=True)
            * prosup_energy_sector_own_consumption_share()
            .loc[:, "PROSUP_sector_energy_own_consumption_liquid"]
            .reset_coords(drop=True)
        )
        .expand_dims({"NRG_COMMODITIES_I": ["TO_liquid"]}, 1)
        .values
    )
    value.loc[:, ["TO_solid_bio"]] = 0
    value.loc[:, ["TO_solid_fossil"]] = (
        (
            fe_excluding_trade().loc[:, "FE_solid_fossil"].reset_coords(drop=True)
            * prosup_energy_sector_own_consumption_share()
            .loc[:, "PROSUP_sector_energy_own_consumption_solid_fossil"]
            .reset_coords(drop=True)
        )
        .expand_dims({"NRG_COMMODITIES_I": ["TO_solid_fossil"]}, 1)
        .values
    )
    return value


@component.add(
    name="PROSUP_storage_losses",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_TO_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_prosto_losses_elec": 1, "imv_prosup_storage_losses": 2},
)
def prosup_storage_losses():
    """
    Storage losses for elec, gas and heat
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "NRG_TO_I": _subscript_dict["NRG_TO_I"],
        },
        ["REGIONS_9_I", "NRG_TO_I"],
    )
    value.loc[:, ["TO_elec"]] = (
        total_prosto_losses_elec()
        .expand_dims({"NRG_COMMODITIES_I": ["TO_elec"]}, 1)
        .values
    )
    value.loc[:, ["TO_gas"]] = (
        imv_prosup_storage_losses()
        .loc[:, "PROSUP_storage_losses_gas"]
        .reset_coords(drop=True)
        .expand_dims({"NRG_COMMODITIES_I": ["TO_gas"]}, 1)
        .values
    )
    value.loc[:, ["TO_heat"]] = (
        imv_prosup_storage_losses()
        .loc[:, "PROSUP_storage_losses_heat"]
        .reset_coords(drop=True)
        .expand_dims({"NRG_COMMODITIES_I": ["TO_heat"]}, 1)
        .values
    )
    value.loc[:, ["TO_hydrogen"]] = 0
    value.loc[:, ["TO_liquid"]] = 0
    value.loc[:, ["TO_solid_bio"]] = 0
    value.loc[:, ["TO_solid_fossil"]] = 0
    return value


@component.add(
    name="PROSUP_transmission_losses",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_TO_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={"fe_excluding_trade": 3, "prosup_transmission_loss_shares": 3},
)
def prosup_transmission_losses():
    """
    transmission losses for grid-bound energy commodities (elec, gas, heat)
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "NRG_TO_I": _subscript_dict["NRG_TO_I"],
        },
        ["REGIONS_9_I", "NRG_TO_I"],
    )
    value.loc[:, ["TO_elec"]] = (
        (
            fe_excluding_trade().loc[:, "FE_elec"].reset_coords(drop=True)
            * prosup_transmission_loss_shares()
            .loc[:, "PROSUP_transmission_losses_elec"]
            .reset_coords(drop=True)
        )
        .expand_dims({"NRG_COMMODITIES_I": ["TO_elec"]}, 1)
        .values
    )
    value.loc[:, ["TO_gas"]] = (
        (
            fe_excluding_trade().loc[:, "FE_gas"].reset_coords(drop=True)
            * prosup_transmission_loss_shares()
            .loc[:, "PROSUP_transmission_losses_gas"]
            .reset_coords(drop=True)
        )
        .expand_dims({"NRG_COMMODITIES_I": ["TO_gas"]}, 1)
        .values
    )
    value.loc[:, ["TO_heat"]] = (
        (
            fe_excluding_trade().loc[:, "FE_heat"].reset_coords(drop=True)
            * prosup_transmission_loss_shares()
            .loc[:, "PROSUP_transmission_losses_heat"]
            .reset_coords(drop=True)
        )
        .expand_dims({"NRG_COMMODITIES_I": ["TO_heat"]}, 1)
        .values
    )
    value.loc[:, ["TO_hydrogen"]] = 0
    value.loc[:, ["TO_liquid"]] = 0
    value.loc[:, ["TO_solid_bio"]] = 0
    value.loc[:, ["TO_solid_fossil"]] = 0
    return value


@component.add(
    name="PROTRA_conversion_efficiencies_complete_matrix",
    units="DMNL",
    subscripts=["REGIONS_36_I", "NRG_TO_I", "NRG_PROTRA_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_conversion_efficiency_elec_2015": 1,
        "protra_conversion_efficiency_heat_2015": 1,
        "protra_no_process_efficiencies_36r": 5,
    },
)
def protra_conversion_efficiencies_complete_matrix():
    """
    complete matrix (PROTRA x TO) of conversion efficincies for all 36 regions, based on empirical data.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_36_I": _subscript_dict["REGIONS_36_I"],
            "NRG_TO_I": _subscript_dict["NRG_TO_I"],
            "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
        },
        ["REGIONS_36_I", "NRG_TO_I", "NRG_PROTRA_I"],
    )
    value.loc[:, ["TO_elec"], :] = (
        protra_conversion_efficiency_elec_2015()
        .expand_dims({"NRG_COMMODITIES_I": ["TO_elec"]}, 1)
        .values
    )
    value.loc[:, ["TO_heat"], :] = (
        protra_conversion_efficiency_heat_2015()
        .expand_dims({"NRG_COMMODITIES_I": ["TO_heat"]}, 1)
        .values
    )
    value.loc[:, ["TO_hydrogen"], :] = (
        protra_no_process_efficiencies_36r()
        .loc[:, "TO_hydrogen", :]
        .reset_coords(drop=True)
        .expand_dims({"NRG_COMMODITIES_I": ["TO_hydrogen"]}, 1)
        .values
    )
    value.loc[:, ["TO_liquid"], :] = (
        protra_no_process_efficiencies_36r()
        .loc[:, "TO_liquid", :]
        .reset_coords(drop=True)
        .expand_dims({"NRG_COMMODITIES_I": ["TO_liquid"]}, 1)
        .values
    )
    value.loc[:, ["TO_solid_bio"], :] = (
        protra_no_process_efficiencies_36r()
        .loc[:, "TO_solid_bio", :]
        .reset_coords(drop=True)
        .expand_dims({"NRG_COMMODITIES_I": ["TO_solid_bio"]}, 1)
        .values
    )
    value.loc[:, ["TO_solid_fossil"], :] = (
        protra_no_process_efficiencies_36r()
        .loc[:, "TO_solid_fossil", :]
        .reset_coords(drop=True)
        .expand_dims({"NRG_COMMODITIES_I": ["TO_solid_fossil"]}, 1)
        .values
    )
    value.loc[:, ["TO_gas"], :] = (
        protra_no_process_efficiencies_36r()
        .loc[:, "TO_gas", :]
        .reset_coords(drop=True)
        .expand_dims({"NRG_COMMODITIES_I": ["TO_gas"]}, 1)
        .values
    )
    return value


@component.add(
    name="PROTRA_CONVERSION_EFFICIENCY_ELEC_2015",
    units="DMNL",
    subscripts=["REGIONS_36_I", "NRG_PROTRA_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_protra_conversion_efficiency_elec_2015"},
)
def protra_conversion_efficiency_elec_2015():
    """
    elec conversion efficiency (elec output per total input) of PROTRA conversion technologies for all 36 regions, based on empirical data.
    """
    return _ext_constant_protra_conversion_efficiency_elec_2015()


_ext_constant_protra_conversion_efficiency_elec_2015 = ExtConstant(
    "model_parameters/energy/PROTRA_efficiency.xlsx",
    "el_eff",
    "TO_elec_conversion_efficiency_2015",
    {
        "REGIONS_36_I": _subscript_dict["REGIONS_36_I"],
        "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
    },
    _root,
    {
        "REGIONS_36_I": _subscript_dict["REGIONS_36_I"],
        "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
    },
    "_ext_constant_protra_conversion_efficiency_elec_2015",
)


@component.add(
    name="PROTRA_CONVERSION_EFFICIENCY_HEAT_2015",
    units="DMNL",
    subscripts=["REGIONS_36_I", "NRG_PROTRA_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_protra_conversion_efficiency_heat_2015"},
)
def protra_conversion_efficiency_heat_2015():
    """
    heat conversion efficiency (Heat output per total input) of PROTRA conversion technologies for all 36 regions in year 2015, based on empirical data.
    """
    return _ext_constant_protra_conversion_efficiency_heat_2015()


_ext_constant_protra_conversion_efficiency_heat_2015 = ExtConstant(
    "model_parameters/energy/PROTRA_efficiency.xlsx",
    "th_eff",
    "TO_heat_conversion_efficiency_2015",
    {
        "REGIONS_36_I": _subscript_dict["REGIONS_36_I"],
        "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
    },
    _root,
    {
        "REGIONS_36_I": _subscript_dict["REGIONS_36_I"],
        "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
    },
    "_ext_constant_protra_conversion_efficiency_heat_2015",
)


@component.add(
    name="PROTRA_fuel_utilization_ratio",
    units="DMNL",
    subscripts=["REGIONS_36_I", "NRG_PROTRA_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={"protra_conversion_efficiencies_complete_matrix": 1},
)
def protra_fuel_utilization_ratio():
    """
    TO per 1 Unit of TI (CHPs collapsed to fuel utilization ratio)
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_36_I": _subscript_dict["REGIONS_36_I"],
            "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
        },
        ["REGIONS_36_I", "NRG_PROTRA_I"],
    )
    value.loc[
        _subscript_dict["REGIONS_9_I"], _subscript_dict["PROTRA_PP_CHP_HP_I"]
    ] = sum(
        protra_conversion_efficiencies_complete_matrix()
        .loc[_subscript_dict["REGIONS_9_I"], :, _subscript_dict["PROTRA_PP_CHP_HP_I"]]
        .rename(
            {
                "REGIONS_36_I": "REGIONS_9_I",
                "NRG_TO_I": "NRG_TO_I!",
                "NRG_PROTRA_I": "PROTRA_PP_CHP_HP_I",
            }
        ),
        dim=["NRG_TO_I!"],
    ).values
    value.loc[:, _subscript_dict["PROTRA_NP_I"]] = 1
    return value


@component.add(
    name="PROTRA_input_shares",
    units="DMNL",
    subscripts=["REGIONS_9_I", "NRG_PROTRA_I", "NRG_TI_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "exogenous_protra_input_shares": 1,
        "aux_ti_gas_bio": 2,
        "aux_ti_liquid_bio": 2,
    },
)
def protra_input_shares():
    """
    PROTRA inputs shares after accounting for eventual bioenergy limits from land-use module.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
            "NRG_TI_I": _subscript_dict["NRG_TI_I"],
        },
        ["REGIONS_9_I", "NRG_PROTRA_I", "NRG_TI_I"],
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, _subscript_dict["PROTRA_TI_GAS_I"], ["TI_gas_bio"]] = False
    except_subs.loc[:, _subscript_dict["PROTRA_TI_GAS_I"], ["TI_gas_fossil"]] = False
    except_subs.loc[
        :, _subscript_dict["PROTRA_TI_LIQUIDS_I"], ["TI_liquid_bio"]
    ] = False
    except_subs.loc[
        :, _subscript_dict["PROTRA_TI_LIQUIDS_I"], ["TI_liquid_fossil"]
    ] = False
    value.values[except_subs.values] = exogenous_protra_input_shares().values[
        except_subs.values
    ]
    value.loc[:, _subscript_dict["PROTRA_TI_GAS_I"], ["TI_gas_bio"]] = (
        aux_ti_gas_bio()
        .loc[:, :, "TI_gas_bio"]
        .reset_coords(drop=True)
        .expand_dims({"NRG_COMMODITIES_I": ["TI_gas_bio"]}, 2)
        .values
    )
    value.loc[:, _subscript_dict["PROTRA_TI_GAS_I"], ["TI_gas_fossil"]] = (
        (1 - aux_ti_gas_bio().loc[:, :, "TI_gas_bio"].reset_coords(drop=True))
        .expand_dims({"NRG_COMMODITIES_I": ["TI_gas_fossil"]}, 2)
        .values
    )
    value.loc[:, _subscript_dict["PROTRA_TI_LIQUIDS_I"], ["TI_liquid_bio"]] = (
        aux_ti_liquid_bio()
        .loc[:, :, "TI_liquid_bio"]
        .reset_coords(drop=True)
        .expand_dims({"NRG_COMMODITIES_I": ["TI_liquid_bio"]}, 2)
        .values
    )
    value.loc[:, _subscript_dict["PROTRA_TI_LIQUIDS_I"], ["TI_liquid_fossil"]] = (
        (1 - aux_ti_liquid_bio().loc[:, :, "TI_liquid_bio"].reset_coords(drop=True))
        .expand_dims({"NRG_COMMODITIES_I": ["TI_liquid_fossil"]}, 2)
        .values
    )
    return value


@component.add(
    name="PROTRA_NO_PROCESS_EFFICIENCIES",
    units="DMNL",
    subscripts=["NRG_COMMODITIES_I", "NRG_PROTRA_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_protra_no_process_efficiencies"},
)
def protra_no_process_efficiencies():
    """
    instrumental efficiencies, assigning PROTRA processes (blending processes and direct run-through processess) to the acompaning TO-fuels
    """
    return _ext_constant_protra_no_process_efficiencies()


_ext_constant_protra_no_process_efficiencies = ExtConstant(
    "model_parameters/energy/PROTRA_efficiency.xlsx",
    "aux_eff",
    "aux_eff_TO_gas*",
    {"NRG_COMMODITIES_I": ["TO_gas"], "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"]},
    _root,
    {
        "NRG_COMMODITIES_I": _subscript_dict["NRG_COMMODITIES_I"],
        "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
    },
    "_ext_constant_protra_no_process_efficiencies",
)

_ext_constant_protra_no_process_efficiencies.add(
    "model_parameters/energy/PROTRA_efficiency.xlsx",
    "aux_eff",
    "aux_eff_TO_hydrogen*",
    {
        "NRG_COMMODITIES_I": ["TO_hydrogen"],
        "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
    },
)

_ext_constant_protra_no_process_efficiencies.add(
    "model_parameters/energy/PROTRA_efficiency.xlsx",
    "aux_eff",
    "aux_eff_TO_liquid*",
    {
        "NRG_COMMODITIES_I": ["TO_liquid"],
        "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
    },
)

_ext_constant_protra_no_process_efficiencies.add(
    "model_parameters/energy/PROTRA_efficiency.xlsx",
    "aux_eff",
    "aux_eff_TO_solid_bio*",
    {
        "NRG_COMMODITIES_I": ["TO_solid_bio"],
        "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
    },
)

_ext_constant_protra_no_process_efficiencies.add(
    "model_parameters/energy/PROTRA_efficiency.xlsx",
    "aux_eff",
    "aux_eff_TO_solid_fossil*",
    {
        "NRG_COMMODITIES_I": ["TO_solid_fossil"],
        "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
    },
)


@component.add(
    name="PROTRA_no_process_efficiencies_36R",
    units="DMNL",
    subscripts=["REGIONS_36_I", "NRG_COMMODITIES_I", "NRG_PROTRA_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"protra_no_process_efficiencies": 5},
)
def protra_no_process_efficiencies_36r():
    """
    upscaled for 36 regions
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_36_I": _subscript_dict["REGIONS_36_I"],
            "NRG_COMMODITIES_I": _subscript_dict["NRG_COMMODITIES_I"],
            "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
        },
        ["REGIONS_36_I", "NRG_COMMODITIES_I", "NRG_PROTRA_I"],
    )
    value.loc[:, ["TO_gas"], :] = (
        protra_no_process_efficiencies()
        .loc["TO_gas", :]
        .reset_coords(drop=True)
        .expand_dims({"REGIONS_36_I": _subscript_dict["REGIONS_36_I"]}, 0)
        .expand_dims({"NRG_COMMODITIES_I": ["TO_gas"]}, 1)
        .values
    )
    value.loc[:, ["TO_hydrogen"], :] = (
        protra_no_process_efficiencies()
        .loc["TO_hydrogen", :]
        .reset_coords(drop=True)
        .expand_dims({"REGIONS_36_I": _subscript_dict["REGIONS_36_I"]}, 0)
        .expand_dims({"NRG_COMMODITIES_I": ["TO_hydrogen"]}, 1)
        .values
    )
    value.loc[:, ["TO_liquid"], :] = (
        protra_no_process_efficiencies()
        .loc["TO_liquid", :]
        .reset_coords(drop=True)
        .expand_dims({"REGIONS_36_I": _subscript_dict["REGIONS_36_I"]}, 0)
        .expand_dims({"NRG_COMMODITIES_I": ["TO_liquid"]}, 1)
        .values
    )
    value.loc[:, ["TO_solid_bio"], :] = (
        protra_no_process_efficiencies()
        .loc["TO_solid_bio", :]
        .reset_coords(drop=True)
        .expand_dims({"REGIONS_36_I": _subscript_dict["REGIONS_36_I"]}, 0)
        .expand_dims({"NRG_COMMODITIES_I": ["TO_solid_bio"]}, 1)
        .values
    )
    value.loc[:, ["TO_solid_fossil"], :] = (
        protra_no_process_efficiencies()
        .loc["TO_solid_fossil", :]
        .reset_coords(drop=True)
        .expand_dims({"REGIONS_36_I": _subscript_dict["REGIONS_36_I"]}, 0)
        .expand_dims({"NRG_COMMODITIES_I": ["TO_solid_fossil"]}, 1)
        .values
    )
    return value


@component.add(
    name="share_total_transmission_loss",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_TO_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_prosup_transmission_losses": 3, "fe_excluding_trade": 3},
)
def share_total_transmission_loss():
    """
    transmission losses for grid-bound energy commodities (elec, gas, heat)
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "NRG_TO_I": _subscript_dict["NRG_TO_I"],
        },
        ["REGIONS_9_I", "NRG_TO_I"],
    )
    value.loc[:, ["TO_elec"]] = (
        zidz(
            total_prosup_transmission_losses()
            .loc[:, "TO_elec"]
            .reset_coords(drop=True),
            fe_excluding_trade().loc[:, "FE_elec"].reset_coords(drop=True),
        )
        .expand_dims({"NRG_COMMODITIES_I": ["TO_elec"]}, 1)
        .values
    )
    value.loc[:, ["TO_gas"]] = (
        zidz(
            total_prosup_transmission_losses().loc[:, "TO_gas"].reset_coords(drop=True),
            fe_excluding_trade().loc[:, "FE_gas"].reset_coords(drop=True),
        )
        .expand_dims({"NRG_COMMODITIES_I": ["TO_gas"]}, 1)
        .values
    )
    value.loc[:, ["TO_heat"]] = (
        zidz(
            total_prosup_transmission_losses()
            .loc[:, "TO_heat"]
            .reset_coords(drop=True),
            fe_excluding_trade().loc[:, "FE_heat"].reset_coords(drop=True),
        )
        .expand_dims({"NRG_COMMODITIES_I": ["TO_heat"]}, 1)
        .values
    )
    value.loc[:, ["TO_hydrogen"]] = 0
    value.loc[:, ["TO_liquid"]] = 0
    value.loc[:, ["TO_solid_bio"]] = 0
    value.loc[:, ["TO_solid_fossil"]] = 0
    return value


@component.add(
    name="SWITCH_NRG_DEMAND_TRANSFORMATION",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_nrg_demand_transformation"},
)
def switch_nrg_demand_transformation():
    """
    This switch can take two values: 0: the (sub)module runs isolated from the rest of WILIAM, replacing inter(sub)module variables with exogenous parameters. 0=hard-link to Final Energy Consumption 2005-2019 (Source: IEA energy balances) 1: the (sub)module runs integrated with the rest of WILIAM.1=Use endogeneous FE Demand .
    """
    return _ext_constant_switch_nrg_demand_transformation()


_ext_constant_switch_nrg_demand_transformation = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_NRG_DEMAND_TRANSFORMATION",
    {},
    _root,
    {},
    "_ext_constant_switch_nrg_demand_transformation",
)


@component.add(
    name="SWITCH_NRG_TRADE",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_nrg_trade"},
)
def switch_nrg_trade():
    """
    switch: 0 to deactivate FE trade, 1 to activate
    """
    return _ext_constant_switch_nrg_trade()


_ext_constant_switch_nrg_trade = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_NRG_TRADE",
    {},
    _root,
    {},
    "_ext_constant_switch_nrg_trade",
)


@component.add(
    name="SWITCH_POLICY_SHARE_BIOENERGY_IN_TI_FOSSIL_LIQUIDS_AND_GASES_SP",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_switch_policy_share_bioenergy_in_ti_fossil_liquids_and_gases_sp"
    },
)
def switch_policy_share_bioenergy_in_ti_fossil_liquids_and_gases_sp():
    """
    SWITCH policy: 0: policy deactivated (no replacement of oil and natural gas by biofuels and biogases, respectively) 1: poilicy activated (replacement of oil and natural gas by biofuels and biogases, respectively)
    """
    return (
        _ext_constant_switch_policy_share_bioenergy_in_ti_fossil_liquids_and_gases_sp()
    )


_ext_constant_switch_policy_share_bioenergy_in_ti_fossil_liquids_and_gases_sp = (
    ExtConstant(
        "scenario_parameters/scenario_parameters.xlsx",
        "energy",
        "SWITCH_POLICY_SHARE_BIOENERGY_IN_TI_FOSSIL_LIQUIDS_AND_GASES_SP*",
        {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
        _root,
        {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
        "_ext_constant_switch_policy_share_bioenergy_in_ti_fossil_liquids_and_gases_sp",
    )
)


@component.add(
    name="TARGET_SHARE_BIOENERGY_IN_FOSSIL_LIQUIDS_AND_GASES_SP",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_target_share_bioenergy_in_fossil_liquids_and_gases_sp"
    },
)
def target_share_bioenergy_in_fossil_liquids_and_gases_sp():
    """
    Target value by region in the final year.
    """
    return _ext_constant_target_share_bioenergy_in_fossil_liquids_and_gases_sp()


_ext_constant_target_share_bioenergy_in_fossil_liquids_and_gases_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "TARGET_SHARE_BIOENERGY_IN_FOSSIL_LIQUIDS_AND_GASES_SP*",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_target_share_bioenergy_in_fossil_liquids_and_gases_sp",
)


@component.add(
    name="TI_by_commodity",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_TI_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ti_by_protra_and_commodity": 1},
)
def ti_by_commodity():
    """
    TI required to satisfy FE demand from society (aggregated by TI Commodity), taking into account type of fuel (fossil/bio) that the plants are fed with (currently exogeneous).
    """
    return sum(
        ti_by_protra_and_commodity().rename({"NRG_PROTRA_I": "NRG_PROTRA_I!"}),
        dim=["NRG_PROTRA_I!"],
    )


@component.add(
    name="TI_by_commodity_dem",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_TI_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ti_by_protra_and_commodity_dem": 1},
)
def ti_by_commodity_dem():
    """
    TI required to satisfy FE demand from society (aggregated by TI Commodity), taking into account type of fuel (fossil/bio) that the plants are fed with (currently exogeneous).
    """
    return sum(
        ti_by_protra_and_commodity_dem().rename({"NRG_PROTRA_I": "NRG_PROTRA_I!"}),
        dim=["NRG_PROTRA_I!"],
    )


@component.add(
    name="TI_by_process",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_PROTRA_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"to_allocated_by_process": 1, "protra_fuel_utilization_ratio": 1},
)
def ti_by_process():
    """
    TI required to satisfy FE demand from society taking into account conversion efficiencies
    """
    return to_allocated_by_process() / protra_fuel_utilization_ratio().loc[
        _subscript_dict["REGIONS_9_I"], :
    ].rename({"REGIONS_36_I": "REGIONS_9_I"})


@component.add(
    name="TI_by_PROREF_and_commodity",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_PROREF_I", "NRG_TI_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ti_by_commodity": 1, "proref_output_shares": 1},
)
def ti_by_proref_and_commodity():
    return (ti_by_commodity() * proref_output_shares()).transpose(
        "REGIONS_9_I", "NRG_PROREF_I", "NRG_TI_I"
    )


@component.add(
    name="TI_by_PROREF_and_commodity_dem",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_PROREF_I", "NRG_TI_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ti_by_commodity_dem": 1, "proref_output_shares": 1},
)
def ti_by_proref_and_commodity_dem():
    return (ti_by_commodity_dem() * proref_output_shares()).transpose(
        "REGIONS_9_I", "NRG_PROREF_I", "NRG_TI_I"
    )


@component.add(
    name="TI_by_PROTRA_and_commodity",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_PROTRA_I", "NRG_TI_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ti_by_process": 1, "protra_input_shares": 1},
)
def ti_by_protra_and_commodity():
    """
    TI by transformation technology and type of TI-commodity (after Input-fuel-share for those technologies that can take more than one input fuel, e.g. biogas/fossil gas, etc.)
    """
    return ti_by_process() * protra_input_shares()


@component.add(
    name="TI_by_PROTRA_and_commodity_dem",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_PROTRA_I", "NRG_TI_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ti_by_process": 1, "exogenous_protra_input_shares": 1},
)
def ti_by_protra_and_commodity_dem():
    """
    TI by transformation technology and type of TI-commodity (after Input-fuel-share for those technologies that can take more than one input fuel, e.g. biogas/fossil gas, etc.)
    """
    return ti_by_process() * exogenous_protra_input_shares()


@component.add(
    name="TI_by_refinery_process",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_PROREF_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ti_by_proref_and_commodity": 1},
)
def ti_by_refinery_process():
    """
    TI required to satisfy FE demand of society disaggregated to refinery processes with shares.
    """
    return sum(
        ti_by_proref_and_commodity().rename({"NRG_TI_I": "NRG_TI_I!"}),
        dim=["NRG_TI_I!"],
    )


@component.add(
    name="TI_by_refinery_process_dem",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_PROREF_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ti_by_proref_and_commodity_dem": 1},
)
def ti_by_refinery_process_dem():
    """
    TI required to satisfy FE demand of society disaggregated to refinery processes with shares.
    """
    return sum(
        ti_by_proref_and_commodity_dem().rename({"NRG_TI_I": "NRG_TI_I!"}),
        dim=["NRG_TI_I!"],
    )


@component.add(
    name="TI_gas_liquids",
    units="EJ/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ti_by_process": 2},
)
def ti_gas_liquids():
    """
    TI from gas and liquids. Auxiliary variable to implement feedback of crops available for energy.
    """
    return sum(
        ti_by_process()
        .loc[:, _subscript_dict["PROTRA_TI_GAS_I"]]
        .rename({"NRG_PROTRA_I": "PROTRA_TI_GAS_I!"}),
        dim=["PROTRA_TI_GAS_I!"],
    ) + sum(
        ti_by_process()
        .loc[:, _subscript_dict["PROTRA_TI_LIQUIDS_I"]]
        .rename({"NRG_PROTRA_I": "PROTRA_TI_LIQUIDS_I!"}),
        dim=["PROTRA_TI_LIQUIDS_I!"],
    )


@component.add(
    name="TO_allocated_by_process",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_PROTRA_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"protra_to_allocated": 1},
)
def to_allocated_by_process():
    """
    TO required to satisfy FE-demand from society (disaggregated by transformation technology)
    """
    return sum(
        protra_to_allocated().rename({"NRG_TO_I": "NRG_TO_I!"}), dim=["NRG_TO_I!"]
    )


@component.add(
    name="TO_by_commodity",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_TO_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "total_fe_including_net_trade": 7,
        "prosup_transmission_losses": 3,
        "prosup_storage_losses": 7,
        "prosup_sector_energy_own_consumption_per_commodity": 7,
        "prosup_flexibility_technologies": 7,
    },
)
def to_by_commodity():
    """
    Transformation Output required to fulfill final energy demand. TO = Final Energy + Transmission Losses + storage losses + sector energy own consumption + Flexibility Technology Utilization (Hydrogen, P2Heat, P2Gas, P2Liquid).
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "NRG_TO_I": _subscript_dict["NRG_TO_I"],
        },
        ["REGIONS_9_I", "NRG_TO_I"],
    )
    value.loc[:, ["TO_elec"]] = (
        np.maximum(
            0,
            total_fe_including_net_trade().loc[:, "FE_elec"].reset_coords(drop=True)
            + prosup_transmission_losses().loc[:, "TO_elec"].reset_coords(drop=True)
            + prosup_storage_losses().loc[:, "TO_elec"].reset_coords(drop=True)
            + prosup_sector_energy_own_consumption_per_commodity()
            .loc[:, "TO_elec"]
            .reset_coords(drop=True)
            + prosup_flexibility_technologies()
            .loc[:, "TO_elec"]
            .reset_coords(drop=True),
        )
        .expand_dims({"NRG_COMMODITIES_I": ["TO_elec"]}, 1)
        .values
    )
    value.loc[:, ["TO_gas"]] = (
        np.maximum(
            0,
            total_fe_including_net_trade().loc[:, "FE_gas"].reset_coords(drop=True)
            + prosup_transmission_losses().loc[:, "TO_gas"].reset_coords(drop=True)
            + prosup_storage_losses().loc[:, "TO_gas"].reset_coords(drop=True)
            + prosup_sector_energy_own_consumption_per_commodity()
            .loc[:, "TO_gas"]
            .reset_coords(drop=True)
            + prosup_flexibility_technologies()
            .loc[:, "TO_gas"]
            .reset_coords(drop=True),
        )
        .expand_dims({"NRG_COMMODITIES_I": ["TO_gas"]}, 1)
        .values
    )
    value.loc[:, ["TO_heat"]] = (
        np.maximum(
            0,
            total_fe_including_net_trade().loc[:, "FE_heat"].reset_coords(drop=True)
            + prosup_transmission_losses().loc[:, "TO_heat"].reset_coords(drop=True)
            + prosup_storage_losses().loc[:, "TO_heat"].reset_coords(drop=True)
            + prosup_sector_energy_own_consumption_per_commodity()
            .loc[:, "TO_heat"]
            .reset_coords(drop=True)
            + prosup_flexibility_technologies()
            .loc[:, "TO_heat"]
            .reset_coords(drop=True),
        )
        .expand_dims({"NRG_COMMODITIES_I": ["TO_heat"]}, 1)
        .values
    )
    value.loc[:, ["TO_hydrogen"]] = (
        np.maximum(
            0,
            total_fe_including_net_trade().loc[:, "FE_hydrogen"].reset_coords(drop=True)
            + 0
            + prosup_storage_losses().loc[:, "TO_hydrogen"].reset_coords(drop=True)
            + prosup_sector_energy_own_consumption_per_commodity()
            .loc[:, "TO_hydrogen"]
            .reset_coords(drop=True)
            + prosup_flexibility_technologies()
            .loc[:, "TO_hydrogen"]
            .reset_coords(drop=True),
        )
        .expand_dims({"NRG_COMMODITIES_I": ["TO_hydrogen"]}, 1)
        .values
    )
    value.loc[:, ["TO_liquid"]] = (
        np.maximum(
            0,
            total_fe_including_net_trade().loc[:, "FE_liquid"].reset_coords(drop=True)
            + 0
            + prosup_storage_losses().loc[:, "TO_liquid"].reset_coords(drop=True)
            + prosup_sector_energy_own_consumption_per_commodity()
            .loc[:, "TO_liquid"]
            .reset_coords(drop=True)
            + prosup_flexibility_technologies()
            .loc[:, "TO_liquid"]
            .reset_coords(drop=True),
        )
        .expand_dims({"NRG_COMMODITIES_I": ["TO_liquid"]}, 1)
        .values
    )
    value.loc[:, ["TO_solid_bio"]] = (
        np.maximum(
            0,
            total_fe_including_net_trade()
            .loc[:, "FE_solid_bio"]
            .reset_coords(drop=True)
            + 0
            + prosup_storage_losses().loc[:, "TO_solid_bio"].reset_coords(drop=True)
            + prosup_sector_energy_own_consumption_per_commodity()
            .loc[:, "TO_solid_bio"]
            .reset_coords(drop=True)
            + prosup_flexibility_technologies()
            .loc[:, "TO_solid_bio"]
            .reset_coords(drop=True),
        )
        .expand_dims({"NRG_COMMODITIES_I": ["TO_solid_bio"]}, 1)
        .values
    )
    value.loc[:, ["TO_solid_fossil"]] = (
        np.maximum(
            0,
            total_fe_including_net_trade()
            .loc[:, "FE_solid_fossil"]
            .reset_coords(drop=True)
            + 0
            + prosup_storage_losses().loc[:, "TO_solid_fossil"].reset_coords(drop=True)
            + prosup_sector_energy_own_consumption_per_commodity()
            .loc[:, "TO_solid_fossil"]
            .reset_coords(drop=True)
            + prosup_flexibility_technologies()
            .loc[:, "TO_solid_fossil"]
            .reset_coords(drop=True),
        )
        .expand_dims({"NRG_COMMODITIES_I": ["TO_solid_fossil"]}, 1)
        .values
    )
    return value


@component.add(
    name="total_FE_excluding_trade_by_region",
    units="EJ/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"fe_excluding_trade": 1},
)
def total_fe_excluding_trade_by_region():
    return sum(
        fe_excluding_trade().rename({"NRG_FE_I": "NRG_FE_I!"}), dim=["NRG_FE_I!"]
    )


@component.add(
    name="total_FE_IEA_Model_CHECK",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_FE_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"iea_total_fe_empirical": 1, "fe_excluding_trade": 1},
)
def total_fe_iea_model_check():
    return iea_total_fe_empirical() - fe_excluding_trade()


@component.add(
    name="total_FE_including_net_trade",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_FE_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_nrg_trade": 1,
        "fe_domestic": 1,
        "fe_net_exports_by_region": 1,
        "fe_excluding_trade": 1,
    },
)
def total_fe_including_net_trade():
    """
    total final energy demand/consumption, including imports/exports of final energy commodities (or transformation inputs).
    """
    return if_then_else(
        switch_nrg_trade() == 1,
        lambda: fe_domestic() + fe_net_exports_by_region(),
        lambda: fe_excluding_trade(),
    )


@component.add(
    name="total_PE_by_region",
    units="EJ/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"pe_by_commodity": 1},
)
def total_pe_by_region():
    """
    Total domestic primary energy consumption by region.
    """
    return sum(pe_by_commodity().rename({"NRG_PE_I": "NRG_PE_I!"}), dim=["NRG_PE_I!"])


@component.add(
    name="total_PROSUP_transmission_losses",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "NRG_TO_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "prosup_transmission_losses": 7,
        "elec_transmission_losses_by_prosto": 1,
    },
)
def total_prosup_transmission_losses():
    """
    transmission losses for grid-bound energy commodities (elec, gas, heat)
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "NRG_TO_I": _subscript_dict["NRG_TO_I"],
        },
        ["REGIONS_9_I", "NRG_TO_I"],
    )
    value.loc[:, ["TO_elec"]] = (
        (
            prosup_transmission_losses().loc[:, "TO_elec"].reset_coords(drop=True)
            + sum(
                elec_transmission_losses_by_prosto().rename(
                    {"PROSTO_ELEC_I": "PROSTO_ELEC_I!"}
                ),
                dim=["PROSTO_ELEC_I!"],
            )
        )
        .expand_dims({"NRG_COMMODITIES_I": ["TO_elec"]}, 1)
        .values
    )
    value.loc[:, ["TO_gas"]] = (
        prosup_transmission_losses()
        .loc[:, "TO_gas"]
        .reset_coords(drop=True)
        .expand_dims({"NRG_COMMODITIES_I": ["TO_gas"]}, 1)
        .values
    )
    value.loc[:, ["TO_heat"]] = (
        prosup_transmission_losses()
        .loc[:, "TO_heat"]
        .reset_coords(drop=True)
        .expand_dims({"NRG_COMMODITIES_I": ["TO_heat"]}, 1)
        .values
    )
    value.loc[:, ["TO_hydrogen"]] = (
        prosup_transmission_losses()
        .loc[:, "TO_hydrogen"]
        .reset_coords(drop=True)
        .expand_dims({"NRG_COMMODITIES_I": ["TO_hydrogen"]}, 1)
        .values
    )
    value.loc[:, ["TO_liquid"]] = (
        prosup_transmission_losses()
        .loc[:, "TO_liquid"]
        .reset_coords(drop=True)
        .expand_dims({"NRG_COMMODITIES_I": ["TO_liquid"]}, 1)
        .values
    )
    value.loc[:, ["TO_solid_bio"]] = (
        prosup_transmission_losses()
        .loc[:, "TO_solid_bio"]
        .reset_coords(drop=True)
        .expand_dims({"NRG_COMMODITIES_I": ["TO_solid_bio"]}, 1)
        .values
    )
    value.loc[:, ["TO_solid_fossil"]] = (
        prosup_transmission_losses()
        .loc[:, "TO_solid_fossil"]
        .reset_coords(drop=True)
        .expand_dims({"NRG_COMMODITIES_I": ["TO_solid_fossil"]}, 1)
        .values
    )
    return value


@component.add(
    name="variation_exogenous_PROTRA_input_shares",
    units="1/Year",
    subscripts=["REGIONS_9_I", "NRG_PROTRA_I", "NRG_TI_I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_model_explorer": 4,
        "model_explorer_target_share_bioenergy_in_fossil_liquids_and_gases": 4,
        "year_initial_share_bioenergy_in_ti_fossil_liquids_and_gases_sp": 8,
        "year_final_share_bioenergy_in_ti_fossil_liquids_and_gases_sp": 8,
        "target_share_bioenergy_in_fossil_liquids_and_gases_sp": 4,
        "time": 8,
        "switch_policy_share_bioenergy_in_ti_fossil_liquids_and_gases_sp": 4,
        "protra_input_shares_empiric": 4,
    },
)
def variation_exogenous_protra_input_shares():
    """
    PROTRA input shares after applying policies.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
            "NRG_TI_I": _subscript_dict["NRG_TI_I"],
        },
        ["REGIONS_9_I", "NRG_PROTRA_I", "NRG_TI_I"],
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, _subscript_dict["PROTRA_TI_GAS_I"], ["TI_gas_bio"]] = False
    except_subs.loc[:, _subscript_dict["PROTRA_TI_GAS_I"], ["TI_gas_fossil"]] = False
    except_subs.loc[
        :, _subscript_dict["PROTRA_TI_LIQUIDS_I"], ["TI_liquid_bio"]
    ] = False
    except_subs.loc[
        :, _subscript_dict["PROTRA_TI_LIQUIDS_I"], ["TI_liquid_fossil"]
    ] = False
    value.values[except_subs.values] = 0
    value.loc[:, _subscript_dict["PROTRA_TI_GAS_I"], ["TI_gas_bio"]] = (
        if_then_else(
            switch_model_explorer() == 1,
            lambda: model_explorer_target_share_bioenergy_in_fossil_liquids_and_gases()
            .loc[:, _subscript_dict["PROTRA_TI_GAS_I"], "TI_gas_bio"]
            .reset_coords(drop=True)
            .rename({"NRG_PRO_I": "PROTRA_TI_GAS_I"}),
            lambda: if_then_else(
                (
                    switch_policy_share_bioenergy_in_ti_fossil_liquids_and_gases_sp()
                    == 0
                ).expand_dims(
                    {"PROTRA_TI_GAS_I": _subscript_dict["PROTRA_TI_GAS_I"]}, 1
                ),
                lambda: xr.DataArray(
                    0,
                    {
                        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                        "PROTRA_TI_GAS_I": _subscript_dict["PROTRA_TI_GAS_I"],
                    },
                    ["REGIONS_9_I", "PROTRA_TI_GAS_I"],
                ),
                lambda: if_then_else(
                    (
                        time()
                        < year_initial_share_bioenergy_in_ti_fossil_liquids_and_gases_sp()
                    ).expand_dims(
                        {"PROTRA_TI_GAS_I": _subscript_dict["PROTRA_TI_GAS_I"]}, 1
                    ),
                    lambda: xr.DataArray(
                        0,
                        {
                            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                            "PROTRA_TI_GAS_I": _subscript_dict["PROTRA_TI_GAS_I"],
                        },
                        ["REGIONS_9_I", "PROTRA_TI_GAS_I"],
                    ),
                    lambda: if_then_else(
                        (
                            time()
                            < year_final_share_bioenergy_in_ti_fossil_liquids_and_gases_sp()
                        ).expand_dims(
                            {"PROTRA_TI_GAS_I": _subscript_dict["PROTRA_TI_GAS_I"]}, 1
                        ),
                        lambda: zidz(
                            target_share_bioenergy_in_fossil_liquids_and_gases_sp()
                            - protra_input_shares_empiric()
                            .loc[:, _subscript_dict["PROTRA_TI_GAS_I"], "TI_gas_bio"]
                            .reset_coords(drop=True)
                            .rename({"NRG_PROTRA_I": "PROTRA_TI_GAS_I"}),
                            (
                                year_final_share_bioenergy_in_ti_fossil_liquids_and_gases_sp()
                                - year_initial_share_bioenergy_in_ti_fossil_liquids_and_gases_sp()
                            ).expand_dims(
                                {"PROTRA_TI_GAS_I": _subscript_dict["PROTRA_TI_GAS_I"]},
                                1,
                            ),
                        ),
                        lambda: xr.DataArray(
                            0,
                            {
                                "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                                "PROTRA_TI_GAS_I": _subscript_dict["PROTRA_TI_GAS_I"],
                            },
                            ["REGIONS_9_I", "PROTRA_TI_GAS_I"],
                        ),
                    ),
                ),
            ),
        )
        .expand_dims({"NRG_COMMODITIES_I": ["TI_gas_bio"]}, 2)
        .values
    )
    value.loc[:, _subscript_dict["PROTRA_TI_GAS_I"], ["TI_gas_fossil"]] = (
        if_then_else(
            switch_model_explorer() == 1,
            lambda: model_explorer_target_share_bioenergy_in_fossil_liquids_and_gases()
            .loc[:, _subscript_dict["PROTRA_TI_GAS_I"], "TI_gas_fossil"]
            .reset_coords(drop=True)
            .rename({"NRG_PRO_I": "PROTRA_TI_GAS_I"}),
            lambda: if_then_else(
                (
                    switch_policy_share_bioenergy_in_ti_fossil_liquids_and_gases_sp()
                    == 0
                ).expand_dims(
                    {"PROTRA_TI_GAS_I": _subscript_dict["PROTRA_TI_GAS_I"]}, 1
                ),
                lambda: xr.DataArray(
                    0,
                    {
                        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                        "PROTRA_TI_GAS_I": _subscript_dict["PROTRA_TI_GAS_I"],
                    },
                    ["REGIONS_9_I", "PROTRA_TI_GAS_I"],
                ),
                lambda: if_then_else(
                    (
                        time()
                        < year_initial_share_bioenergy_in_ti_fossil_liquids_and_gases_sp()
                    ).expand_dims(
                        {"PROTRA_TI_GAS_I": _subscript_dict["PROTRA_TI_GAS_I"]}, 1
                    ),
                    lambda: xr.DataArray(
                        0,
                        {
                            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                            "PROTRA_TI_GAS_I": _subscript_dict["PROTRA_TI_GAS_I"],
                        },
                        ["REGIONS_9_I", "PROTRA_TI_GAS_I"],
                    ),
                    lambda: if_then_else(
                        (
                            time()
                            < year_final_share_bioenergy_in_ti_fossil_liquids_and_gases_sp()
                        ).expand_dims(
                            {"PROTRA_TI_GAS_I": _subscript_dict["PROTRA_TI_GAS_I"]}, 1
                        ),
                        lambda: zidz(
                            (
                                1
                                - target_share_bioenergy_in_fossil_liquids_and_gases_sp()
                            )
                            - protra_input_shares_empiric()
                            .loc[:, _subscript_dict["PROTRA_TI_GAS_I"], "TI_gas_fossil"]
                            .reset_coords(drop=True)
                            .rename({"NRG_PROTRA_I": "PROTRA_TI_GAS_I"}),
                            (
                                year_final_share_bioenergy_in_ti_fossil_liquids_and_gases_sp()
                                - year_initial_share_bioenergy_in_ti_fossil_liquids_and_gases_sp()
                            ).expand_dims(
                                {"PROTRA_TI_GAS_I": _subscript_dict["PROTRA_TI_GAS_I"]},
                                1,
                            ),
                        ),
                        lambda: xr.DataArray(
                            0,
                            {
                                "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                                "PROTRA_TI_GAS_I": _subscript_dict["PROTRA_TI_GAS_I"],
                            },
                            ["REGIONS_9_I", "PROTRA_TI_GAS_I"],
                        ),
                    ),
                ),
            ),
        )
        .expand_dims({"NRG_COMMODITIES_I": ["TI_gas_fossil"]}, 2)
        .values
    )
    value.loc[:, _subscript_dict["PROTRA_TI_LIQUIDS_I"], ["TI_liquid_bio"]] = (
        if_then_else(
            switch_model_explorer() == 1,
            lambda: model_explorer_target_share_bioenergy_in_fossil_liquids_and_gases()
            .loc[:, _subscript_dict["PROTRA_TI_LIQUIDS_I"], "TI_liquid_bio"]
            .reset_coords(drop=True)
            .rename({"NRG_PRO_I": "PROTRA_TI_LIQUIDS_I"}),
            lambda: if_then_else(
                (
                    switch_policy_share_bioenergy_in_ti_fossil_liquids_and_gases_sp()
                    == 0
                ).expand_dims(
                    {"PROTRA_TI_LIQUIDS_I": _subscript_dict["PROTRA_TI_LIQUIDS_I"]}, 1
                ),
                lambda: xr.DataArray(
                    0,
                    {
                        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                        "PROTRA_TI_LIQUIDS_I": _subscript_dict["PROTRA_TI_LIQUIDS_I"],
                    },
                    ["REGIONS_9_I", "PROTRA_TI_LIQUIDS_I"],
                ),
                lambda: if_then_else(
                    (
                        time()
                        < year_initial_share_bioenergy_in_ti_fossil_liquids_and_gases_sp()
                    ).expand_dims(
                        {"PROTRA_TI_LIQUIDS_I": _subscript_dict["PROTRA_TI_LIQUIDS_I"]},
                        1,
                    ),
                    lambda: xr.DataArray(
                        0,
                        {
                            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                            "PROTRA_TI_LIQUIDS_I": _subscript_dict[
                                "PROTRA_TI_LIQUIDS_I"
                            ],
                        },
                        ["REGIONS_9_I", "PROTRA_TI_LIQUIDS_I"],
                    ),
                    lambda: if_then_else(
                        (
                            time()
                            < year_final_share_bioenergy_in_ti_fossil_liquids_and_gases_sp()
                        ).expand_dims(
                            {
                                "PROTRA_TI_LIQUIDS_I": _subscript_dict[
                                    "PROTRA_TI_LIQUIDS_I"
                                ]
                            },
                            1,
                        ),
                        lambda: zidz(
                            target_share_bioenergy_in_fossil_liquids_and_gases_sp()
                            - protra_input_shares_empiric()
                            .loc[
                                :,
                                _subscript_dict["PROTRA_TI_LIQUIDS_I"],
                                "TI_liquid_bio",
                            ]
                            .reset_coords(drop=True)
                            .rename({"NRG_PROTRA_I": "PROTRA_TI_LIQUIDS_I"}),
                            (
                                year_final_share_bioenergy_in_ti_fossil_liquids_and_gases_sp()
                                - year_initial_share_bioenergy_in_ti_fossil_liquids_and_gases_sp()
                            ).expand_dims(
                                {
                                    "PROTRA_TI_LIQUIDS_I": _subscript_dict[
                                        "PROTRA_TI_LIQUIDS_I"
                                    ]
                                },
                                1,
                            ),
                        ),
                        lambda: xr.DataArray(
                            0,
                            {
                                "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                                "PROTRA_TI_LIQUIDS_I": _subscript_dict[
                                    "PROTRA_TI_LIQUIDS_I"
                                ],
                            },
                            ["REGIONS_9_I", "PROTRA_TI_LIQUIDS_I"],
                        ),
                    ),
                ),
            ),
        )
        .expand_dims({"NRG_COMMODITIES_I": ["TI_liquid_bio"]}, 2)
        .values
    )
    value.loc[:, _subscript_dict["PROTRA_TI_LIQUIDS_I"], ["TI_liquid_fossil"]] = (
        if_then_else(
            switch_model_explorer() == 1,
            lambda: model_explorer_target_share_bioenergy_in_fossil_liquids_and_gases()
            .loc[:, _subscript_dict["PROTRA_TI_LIQUIDS_I"], "TI_liquid_fossil"]
            .reset_coords(drop=True)
            .rename({"NRG_PRO_I": "PROTRA_TI_LIQUIDS_I"}),
            lambda: if_then_else(
                (
                    switch_policy_share_bioenergy_in_ti_fossil_liquids_and_gases_sp()
                    == 0
                ).expand_dims(
                    {"PROTRA_TI_LIQUIDS_I": _subscript_dict["PROTRA_TI_LIQUIDS_I"]}, 1
                ),
                lambda: xr.DataArray(
                    0,
                    {
                        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                        "PROTRA_TI_LIQUIDS_I": _subscript_dict["PROTRA_TI_LIQUIDS_I"],
                    },
                    ["REGIONS_9_I", "PROTRA_TI_LIQUIDS_I"],
                ),
                lambda: if_then_else(
                    (
                        time()
                        < year_initial_share_bioenergy_in_ti_fossil_liquids_and_gases_sp()
                    ).expand_dims(
                        {"PROTRA_TI_LIQUIDS_I": _subscript_dict["PROTRA_TI_LIQUIDS_I"]},
                        1,
                    ),
                    lambda: xr.DataArray(
                        0,
                        {
                            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                            "PROTRA_TI_LIQUIDS_I": _subscript_dict[
                                "PROTRA_TI_LIQUIDS_I"
                            ],
                        },
                        ["REGIONS_9_I", "PROTRA_TI_LIQUIDS_I"],
                    ),
                    lambda: if_then_else(
                        (
                            time()
                            < year_final_share_bioenergy_in_ti_fossil_liquids_and_gases_sp()
                        ).expand_dims(
                            {
                                "PROTRA_TI_LIQUIDS_I": _subscript_dict[
                                    "PROTRA_TI_LIQUIDS_I"
                                ]
                            },
                            1,
                        ),
                        lambda: zidz(
                            (
                                1
                                - target_share_bioenergy_in_fossil_liquids_and_gases_sp()
                            )
                            - protra_input_shares_empiric()
                            .loc[
                                :,
                                _subscript_dict["PROTRA_TI_LIQUIDS_I"],
                                "TI_liquid_fossil",
                            ]
                            .reset_coords(drop=True)
                            .rename({"NRG_PROTRA_I": "PROTRA_TI_LIQUIDS_I"}),
                            (
                                year_final_share_bioenergy_in_ti_fossil_liquids_and_gases_sp()
                                - year_initial_share_bioenergy_in_ti_fossil_liquids_and_gases_sp()
                            ).expand_dims(
                                {
                                    "PROTRA_TI_LIQUIDS_I": _subscript_dict[
                                        "PROTRA_TI_LIQUIDS_I"
                                    ]
                                },
                                1,
                            ),
                        ),
                        lambda: xr.DataArray(
                            0,
                            {
                                "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
                                "PROTRA_TI_LIQUIDS_I": _subscript_dict[
                                    "PROTRA_TI_LIQUIDS_I"
                                ],
                            },
                            ["REGIONS_9_I", "PROTRA_TI_LIQUIDS_I"],
                        ),
                    ),
                ),
            ),
        )
        .expand_dims({"NRG_COMMODITIES_I": ["TI_liquid_fossil"]}, 2)
        .values
    )
    return value


@component.add(
    name="world_FE_excluding_trade_by_commodity",
    units="EJ/Year",
    subscripts=["NRG_FE_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"fe_excluding_trade": 1},
)
def world_fe_excluding_trade_by_commodity():
    return sum(
        fe_excluding_trade().rename({"REGIONS_9_I": "REGIONS_9_I!"}),
        dim=["REGIONS_9_I!"],
    )


@component.add(
    name="world_PE_by_commodity",
    units="EJ/Year",
    subscripts=["NRG_PE_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"pe_by_commodity": 1},
)
def world_pe_by_commodity():
    """
    World primary energy demand aggregated by PE (primary energy) commodity.
    """
    return sum(
        pe_by_commodity().rename({"REGIONS_9_I": "REGIONS_9_I!"}), dim=["REGIONS_9_I!"]
    )


@component.add(
    name="YEAR_FINAL_SHARE_BIOENERGY_IN_TI_FOSSIL_LIQUIDS_AND_GASES_SP",
    units="Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_year_final_share_bioenergy_in_ti_fossil_liquids_and_gases_sp"
    },
)
def year_final_share_bioenergy_in_ti_fossil_liquids_and_gases_sp():
    return _ext_constant_year_final_share_bioenergy_in_ti_fossil_liquids_and_gases_sp()


_ext_constant_year_final_share_bioenergy_in_ti_fossil_liquids_and_gases_sp = (
    ExtConstant(
        "scenario_parameters/scenario_parameters.xlsx",
        "energy",
        "YEAR_FINAL_SHARE_BIOENERGY_IN_TI_FOSSIL_LIQUIDS_AND_GASES_SP*",
        {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
        _root,
        {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
        "_ext_constant_year_final_share_bioenergy_in_ti_fossil_liquids_and_gases_sp",
    )
)


@component.add(
    name="YEAR_INITIAL_SHARE_BIOENERGY_IN_TI_FOSSIL_LIQUIDS_AND_GASES_SP",
    units="Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_year_initial_share_bioenergy_in_ti_fossil_liquids_and_gases_sp"
    },
)
def year_initial_share_bioenergy_in_ti_fossil_liquids_and_gases_sp():
    return (
        _ext_constant_year_initial_share_bioenergy_in_ti_fossil_liquids_and_gases_sp()
    )


_ext_constant_year_initial_share_bioenergy_in_ti_fossil_liquids_and_gases_sp = (
    ExtConstant(
        "scenario_parameters/scenario_parameters.xlsx",
        "energy",
        "YEAR_INITIAL_SHARE_BIOENERGY_IN_TI_FOSSIL_LIQUIDS_AND_GASES_SP*",
        {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
        _root,
        {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
        "_ext_constant_year_initial_share_bioenergy_in_ti_fossil_liquids_and_gases_sp",
    )
)
