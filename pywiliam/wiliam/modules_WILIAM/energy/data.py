"""
Module energy.data
Translated using PySD version 3.10.0
"""


@component.add(
    name="IMV_PROSUP_STORAGE_LOSSES",
    units="EJ/Year",
    subscripts=["REGIONS_9_I", "PROSUP_STORAGES_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_imv_prosup_storage_losses"},
)
def imv_prosup_storage_losses():
    """
    Storage Losses for elec, gas and (district-)heat --> TO BE ENDOGENIZED
    """
    return _ext_constant_imv_prosup_storage_losses()


_ext_constant_imv_prosup_storage_losses = ExtConstant(
    "model_parameters/energy/energy.xlsm",
    "CHINA",
    "storage_losses_required_per_process*",
    {
        "REGIONS_9_I": ["CHINA"],
        "PROSUP_STORAGES_I": _subscript_dict["PROSUP_STORAGES_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PROSUP_STORAGES_I": _subscript_dict["PROSUP_STORAGES_I"],
    },
    "_ext_constant_imv_prosup_storage_losses",
)

_ext_constant_imv_prosup_storage_losses.add(
    "model_parameters/energy/energy.xlsm",
    "EASOC",
    "storage_losses_required_per_process*",
    {
        "REGIONS_9_I": ["EASOC"],
        "PROSUP_STORAGES_I": _subscript_dict["PROSUP_STORAGES_I"],
    },
)

_ext_constant_imv_prosup_storage_losses.add(
    "model_parameters/energy/energy.xlsm",
    "EU27",
    "storage_losses_required_per_process*",
    {
        "REGIONS_9_I": ["EU27"],
        "PROSUP_STORAGES_I": _subscript_dict["PROSUP_STORAGES_I"],
    },
)

_ext_constant_imv_prosup_storage_losses.add(
    "model_parameters/energy/energy.xlsm",
    "INDIA",
    "storage_losses_required_per_process*",
    {
        "REGIONS_9_I": ["INDIA"],
        "PROSUP_STORAGES_I": _subscript_dict["PROSUP_STORAGES_I"],
    },
)

_ext_constant_imv_prosup_storage_losses.add(
    "model_parameters/energy/energy.xlsm",
    "LATAM",
    "storage_losses_required_per_process*",
    {
        "REGIONS_9_I": ["LATAM"],
        "PROSUP_STORAGES_I": _subscript_dict["PROSUP_STORAGES_I"],
    },
)

_ext_constant_imv_prosup_storage_losses.add(
    "model_parameters/energy/energy.xlsm",
    "LROW",
    "storage_losses_required_per_process*",
    {
        "REGIONS_9_I": ["LROW"],
        "PROSUP_STORAGES_I": _subscript_dict["PROSUP_STORAGES_I"],
    },
)

_ext_constant_imv_prosup_storage_losses.add(
    "model_parameters/energy/energy.xlsm",
    "RUSSIA",
    "storage_losses_required_per_process*",
    {
        "REGIONS_9_I": ["RUSSIA"],
        "PROSUP_STORAGES_I": _subscript_dict["PROSUP_STORAGES_I"],
    },
)

_ext_constant_imv_prosup_storage_losses.add(
    "model_parameters/energy/energy.xlsm",
    "UK",
    "storage_losses_required_per_process*",
    {"REGIONS_9_I": ["UK"], "PROSUP_STORAGES_I": _subscript_dict["PROSUP_STORAGES_I"]},
)

_ext_constant_imv_prosup_storage_losses.add(
    "model_parameters/energy/energy.xlsm",
    "USMCA",
    "storage_losses_required_per_process*",
    {
        "REGIONS_9_I": ["USMCA"],
        "PROSUP_STORAGES_I": _subscript_dict["PROSUP_STORAGES_I"],
    },
)


@component.add(
    name="PROSUP_ENERGY_SECTOR_OWN_CONSUMPTION_SHARE",
    units="DMNL",
    subscripts=["REGIONS_9_I", "PROSUP_SECTOR_OWN_CONSUMPTION_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_prosup_energy_sector_own_consumption_share"
    },
)
def prosup_energy_sector_own_consumption_share():
    """
    Energy sector own consumption excluding storage losses (to avoid double counting!) as share of Final Energy
    """
    return _ext_constant_prosup_energy_sector_own_consumption_share()


_ext_constant_prosup_energy_sector_own_consumption_share = ExtConstant(
    "model_parameters/energy/energy.xlsm",
    "CHINA",
    "sector_own_consumption_required_per_process*",
    {
        "REGIONS_9_I": ["CHINA"],
        "PROSUP_SECTOR_OWN_CONSUMPTION_I": _subscript_dict[
            "PROSUP_SECTOR_OWN_CONSUMPTION_I"
        ],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PROSUP_SECTOR_OWN_CONSUMPTION_I": _subscript_dict[
            "PROSUP_SECTOR_OWN_CONSUMPTION_I"
        ],
    },
    "_ext_constant_prosup_energy_sector_own_consumption_share",
)

_ext_constant_prosup_energy_sector_own_consumption_share.add(
    "model_parameters/energy/energy.xlsm",
    "EASOC",
    "sector_own_consumption_required_per_process*",
    {
        "REGIONS_9_I": ["EASOC"],
        "PROSUP_SECTOR_OWN_CONSUMPTION_I": _subscript_dict[
            "PROSUP_SECTOR_OWN_CONSUMPTION_I"
        ],
    },
)

_ext_constant_prosup_energy_sector_own_consumption_share.add(
    "model_parameters/energy/energy.xlsm",
    "EU27",
    "sector_own_consumption_required_per_process*",
    {
        "REGIONS_9_I": ["EU27"],
        "PROSUP_SECTOR_OWN_CONSUMPTION_I": _subscript_dict[
            "PROSUP_SECTOR_OWN_CONSUMPTION_I"
        ],
    },
)

_ext_constant_prosup_energy_sector_own_consumption_share.add(
    "model_parameters/energy/energy.xlsm",
    "INDIA",
    "sector_own_consumption_required_per_process*",
    {
        "REGIONS_9_I": ["INDIA"],
        "PROSUP_SECTOR_OWN_CONSUMPTION_I": _subscript_dict[
            "PROSUP_SECTOR_OWN_CONSUMPTION_I"
        ],
    },
)

_ext_constant_prosup_energy_sector_own_consumption_share.add(
    "model_parameters/energy/energy.xlsm",
    "LATAM",
    "sector_own_consumption_required_per_process*",
    {
        "REGIONS_9_I": ["LATAM"],
        "PROSUP_SECTOR_OWN_CONSUMPTION_I": _subscript_dict[
            "PROSUP_SECTOR_OWN_CONSUMPTION_I"
        ],
    },
)

_ext_constant_prosup_energy_sector_own_consumption_share.add(
    "model_parameters/energy/energy.xlsm",
    "LROW",
    "sector_own_consumption_required_per_process*",
    {
        "REGIONS_9_I": ["LROW"],
        "PROSUP_SECTOR_OWN_CONSUMPTION_I": _subscript_dict[
            "PROSUP_SECTOR_OWN_CONSUMPTION_I"
        ],
    },
)

_ext_constant_prosup_energy_sector_own_consumption_share.add(
    "model_parameters/energy/energy.xlsm",
    "RUSSIA",
    "sector_own_consumption_required_per_process*",
    {
        "REGIONS_9_I": ["RUSSIA"],
        "PROSUP_SECTOR_OWN_CONSUMPTION_I": _subscript_dict[
            "PROSUP_SECTOR_OWN_CONSUMPTION_I"
        ],
    },
)

_ext_constant_prosup_energy_sector_own_consumption_share.add(
    "model_parameters/energy/energy.xlsm",
    "UK",
    "sector_own_consumption_required_per_process*",
    {
        "REGIONS_9_I": ["UK"],
        "PROSUP_SECTOR_OWN_CONSUMPTION_I": _subscript_dict[
            "PROSUP_SECTOR_OWN_CONSUMPTION_I"
        ],
    },
)

_ext_constant_prosup_energy_sector_own_consumption_share.add(
    "model_parameters/energy/energy.xlsm",
    "USMCA",
    "sector_own_consumption_required_per_process*",
    {
        "REGIONS_9_I": ["USMCA"],
        "PROSUP_SECTOR_OWN_CONSUMPTION_I": _subscript_dict[
            "PROSUP_SECTOR_OWN_CONSUMPTION_I"
        ],
    },
)


@component.add(
    name="PROSUP_TRANSMISSION_LOSS_SHARES",
    units="DMNL",
    subscripts=["REGIONS_9_I", "PROSUP_TRANSMISSION_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_prosup_transmission_loss_shares"},
)
def prosup_transmission_loss_shares():
    """
    Transmission losses as share of Final Energy (including distribution and transportation losses). Exogeneous input calculated from energy balances.
    """
    return _ext_constant_prosup_transmission_loss_shares()


_ext_constant_prosup_transmission_loss_shares = ExtConstant(
    "model_parameters/energy/energy.xlsm",
    "CHINA",
    "transmission_losses_required_shares*",
    {
        "REGIONS_9_I": ["CHINA"],
        "PROSUP_TRANSMISSION_I": _subscript_dict["PROSUP_TRANSMISSION_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "PROSUP_TRANSMISSION_I": _subscript_dict["PROSUP_TRANSMISSION_I"],
    },
    "_ext_constant_prosup_transmission_loss_shares",
)

_ext_constant_prosup_transmission_loss_shares.add(
    "model_parameters/energy/energy.xlsm",
    "EASOC",
    "transmission_losses_required_shares*",
    {
        "REGIONS_9_I": ["EASOC"],
        "PROSUP_TRANSMISSION_I": _subscript_dict["PROSUP_TRANSMISSION_I"],
    },
)

_ext_constant_prosup_transmission_loss_shares.add(
    "model_parameters/energy/energy.xlsm",
    "EU27",
    "transmission_losses_required_shares*",
    {
        "REGIONS_9_I": ["EU27"],
        "PROSUP_TRANSMISSION_I": _subscript_dict["PROSUP_TRANSMISSION_I"],
    },
)

_ext_constant_prosup_transmission_loss_shares.add(
    "model_parameters/energy/energy.xlsm",
    "INDIA",
    "transmission_losses_required_shares*",
    {
        "REGIONS_9_I": ["INDIA"],
        "PROSUP_TRANSMISSION_I": _subscript_dict["PROSUP_TRANSMISSION_I"],
    },
)

_ext_constant_prosup_transmission_loss_shares.add(
    "model_parameters/energy/energy.xlsm",
    "LATAM",
    "transmission_losses_required_shares*",
    {
        "REGIONS_9_I": ["LATAM"],
        "PROSUP_TRANSMISSION_I": _subscript_dict["PROSUP_TRANSMISSION_I"],
    },
)

_ext_constant_prosup_transmission_loss_shares.add(
    "model_parameters/energy/energy.xlsm",
    "LROW",
    "transmission_losses_required_shares*",
    {
        "REGIONS_9_I": ["LROW"],
        "PROSUP_TRANSMISSION_I": _subscript_dict["PROSUP_TRANSMISSION_I"],
    },
)

_ext_constant_prosup_transmission_loss_shares.add(
    "model_parameters/energy/energy.xlsm",
    "RUSSIA",
    "transmission_losses_required_shares*",
    {
        "REGIONS_9_I": ["RUSSIA"],
        "PROSUP_TRANSMISSION_I": _subscript_dict["PROSUP_TRANSMISSION_I"],
    },
)

_ext_constant_prosup_transmission_loss_shares.add(
    "model_parameters/energy/energy.xlsm",
    "UK",
    "transmission_losses_required_shares*",
    {
        "REGIONS_9_I": ["UK"],
        "PROSUP_TRANSMISSION_I": _subscript_dict["PROSUP_TRANSMISSION_I"],
    },
)

_ext_constant_prosup_transmission_loss_shares.add(
    "model_parameters/energy/energy.xlsm",
    "USMCA",
    "transmission_losses_required_shares*",
    {
        "REGIONS_9_I": ["USMCA"],
        "PROSUP_TRANSMISSION_I": _subscript_dict["PROSUP_TRANSMISSION_I"],
    },
)


@component.add(
    name="PROTRA_CAPACITY_EXPANSION_MAX_GROWTH_RATE",
    units="DMNL",
    subscripts=["REGIONS_9_I", "NRG_PROTRA_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_protra_capacity_expansion_max_growth_rate"
    },
)
def protra_capacity_expansion_max_growth_rate():
    """
    exogeneous limit for max. capacity growth per year (expresed in relative terms, capacity-addition per year).
    """
    return _ext_constant_protra_capacity_expansion_max_growth_rate()


_ext_constant_protra_capacity_expansion_max_growth_rate = ExtConstant(
    "model_parameters/energy/energy.xlsm",
    "CHINA",
    "capacity_expansion_limits_relative_per_transformation_process*",
    {"REGIONS_9_I": ["CHINA"], "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"]},
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
    },
    "_ext_constant_protra_capacity_expansion_max_growth_rate",
)

_ext_constant_protra_capacity_expansion_max_growth_rate.add(
    "model_parameters/energy/energy.xlsm",
    "EASOC",
    "capacity_expansion_limits_relative_per_transformation_process*",
    {"REGIONS_9_I": ["EASOC"], "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"]},
)

_ext_constant_protra_capacity_expansion_max_growth_rate.add(
    "model_parameters/energy/energy.xlsm",
    "EU27",
    "capacity_expansion_limits_relative_per_transformation_process*",
    {"REGIONS_9_I": ["EU27"], "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"]},
)

_ext_constant_protra_capacity_expansion_max_growth_rate.add(
    "model_parameters/energy/energy.xlsm",
    "INDIA",
    "capacity_expansion_limits_relative_per_transformation_process*",
    {"REGIONS_9_I": ["INDIA"], "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"]},
)

_ext_constant_protra_capacity_expansion_max_growth_rate.add(
    "model_parameters/energy/energy.xlsm",
    "LATAM",
    "capacity_expansion_limits_relative_per_transformation_process*",
    {"REGIONS_9_I": ["LATAM"], "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"]},
)

_ext_constant_protra_capacity_expansion_max_growth_rate.add(
    "model_parameters/energy/energy.xlsm",
    "LROW",
    "capacity_expansion_limits_relative_per_transformation_process*",
    {"REGIONS_9_I": ["LROW"], "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"]},
)

_ext_constant_protra_capacity_expansion_max_growth_rate.add(
    "model_parameters/energy/energy.xlsm",
    "RUSSIA",
    "capacity_expansion_limits_relative_per_transformation_process*",
    {"REGIONS_9_I": ["RUSSIA"], "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"]},
)

_ext_constant_protra_capacity_expansion_max_growth_rate.add(
    "model_parameters/energy/energy.xlsm",
    "UK",
    "capacity_expansion_limits_relative_per_transformation_process*",
    {"REGIONS_9_I": ["UK"], "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"]},
)

_ext_constant_protra_capacity_expansion_max_growth_rate.add(
    "model_parameters/energy/energy.xlsm",
    "USMCA",
    "capacity_expansion_limits_relative_per_transformation_process*",
    {"REGIONS_9_I": ["USMCA"], "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"]},
)


@component.add(
    name="PROTRA_INPUT_SHARES_EMPIRIC",
    units="DMNL",
    subscripts=["REGIONS_9_I", "NRG_PROTRA_I", "NRG_TI_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_protra_input_shares_empiric"},
)
def protra_input_shares_empiric():
    """
    Empiric input fuel shares for the year 2015 (some transformation processes can take more than one fuel, e.g. gas plants can be driven with biogas or fossil gas).
    """
    return _ext_constant_protra_input_shares_empiric()


_ext_constant_protra_input_shares_empiric = ExtConstant(
    "model_parameters/energy/energy.xlsm",
    "CHINA",
    "transformation_input_required_shares_of_process_and_commodity",
    {
        "REGIONS_9_I": ["CHINA"],
        "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
        "NRG_TI_I": _subscript_dict["NRG_TI_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
        "NRG_TI_I": _subscript_dict["NRG_TI_I"],
    },
    "_ext_constant_protra_input_shares_empiric",
)

_ext_constant_protra_input_shares_empiric.add(
    "model_parameters/energy/energy.xlsm",
    "EASOC",
    "transformation_input_required_shares_of_process_and_commodity",
    {
        "REGIONS_9_I": ["EASOC"],
        "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
        "NRG_TI_I": _subscript_dict["NRG_TI_I"],
    },
)

_ext_constant_protra_input_shares_empiric.add(
    "model_parameters/energy/energy.xlsm",
    "EU27",
    "transformation_input_required_shares_of_process_and_commodity",
    {
        "REGIONS_9_I": ["EU27"],
        "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
        "NRG_TI_I": _subscript_dict["NRG_TI_I"],
    },
)

_ext_constant_protra_input_shares_empiric.add(
    "model_parameters/energy/energy.xlsm",
    "INDIA",
    "transformation_input_required_shares_of_process_and_commodity",
    {
        "REGIONS_9_I": ["INDIA"],
        "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
        "NRG_TI_I": _subscript_dict["NRG_TI_I"],
    },
)

_ext_constant_protra_input_shares_empiric.add(
    "model_parameters/energy/energy.xlsm",
    "LATAM",
    "transformation_input_required_shares_of_process_and_commodity",
    {
        "REGIONS_9_I": ["LATAM"],
        "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
        "NRG_TI_I": _subscript_dict["NRG_TI_I"],
    },
)

_ext_constant_protra_input_shares_empiric.add(
    "model_parameters/energy/energy.xlsm",
    "LROW",
    "transformation_input_required_shares_of_process_and_commodity",
    {
        "REGIONS_9_I": ["LROW"],
        "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
        "NRG_TI_I": _subscript_dict["NRG_TI_I"],
    },
)

_ext_constant_protra_input_shares_empiric.add(
    "model_parameters/energy/energy.xlsm",
    "RUSSIA",
    "transformation_input_required_shares_of_process_and_commodity",
    {
        "REGIONS_9_I": ["RUSSIA"],
        "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
        "NRG_TI_I": _subscript_dict["NRG_TI_I"],
    },
)

_ext_constant_protra_input_shares_empiric.add(
    "model_parameters/energy/energy.xlsm",
    "UK",
    "transformation_input_required_shares_of_process_and_commodity",
    {
        "REGIONS_9_I": ["UK"],
        "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
        "NRG_TI_I": _subscript_dict["NRG_TI_I"],
    },
)

_ext_constant_protra_input_shares_empiric.add(
    "model_parameters/energy/energy.xlsm",
    "USMCA",
    "transformation_input_required_shares_of_process_and_commodity",
    {
        "REGIONS_9_I": ["USMCA"],
        "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
        "NRG_TI_I": _subscript_dict["NRG_TI_I"],
    },
)


@component.add(
    name="PROTRA_MAX_FULL_LOAD_HOURS",
    units="Hours/Year",
    subscripts=["REGIONS_9_I", "NRG_PROTRA_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_protra_max_full_load_hours"},
)
def protra_max_full_load_hours():
    """
    operating hours of capacity stock
    """
    return _ext_constant_protra_max_full_load_hours()


_ext_constant_protra_max_full_load_hours = ExtConstant(
    "model_parameters/energy/energy.xlsm",
    "CHINA",
    "IMV_annual_operating_hours_maximum_per_transformation_process*",
    {"REGIONS_9_I": ["CHINA"], "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"]},
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
    },
    "_ext_constant_protra_max_full_load_hours",
)

_ext_constant_protra_max_full_load_hours.add(
    "model_parameters/energy/energy.xlsm",
    "EASOC",
    "IMV_annual_operating_hours_maximum_per_transformation_process*",
    {"REGIONS_9_I": ["EASOC"], "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"]},
)

_ext_constant_protra_max_full_load_hours.add(
    "model_parameters/energy/energy.xlsm",
    "EU27",
    "IMV_annual_operating_hours_maximum_per_transformation_process*",
    {"REGIONS_9_I": ["EU27"], "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"]},
)

_ext_constant_protra_max_full_load_hours.add(
    "model_parameters/energy/energy.xlsm",
    "INDIA",
    "IMV_annual_operating_hours_maximum_per_transformation_process*",
    {"REGIONS_9_I": ["INDIA"], "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"]},
)

_ext_constant_protra_max_full_load_hours.add(
    "model_parameters/energy/energy.xlsm",
    "LATAM",
    "IMV_annual_operating_hours_maximum_per_transformation_process*",
    {"REGIONS_9_I": ["LATAM"], "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"]},
)

_ext_constant_protra_max_full_load_hours.add(
    "model_parameters/energy/energy.xlsm",
    "LROW",
    "IMV_annual_operating_hours_maximum_per_transformation_process*",
    {"REGIONS_9_I": ["LROW"], "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"]},
)

_ext_constant_protra_max_full_load_hours.add(
    "model_parameters/energy/energy.xlsm",
    "RUSSIA",
    "IMV_annual_operating_hours_maximum_per_transformation_process*",
    {"REGIONS_9_I": ["RUSSIA"], "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"]},
)

_ext_constant_protra_max_full_load_hours.add(
    "model_parameters/energy/energy.xlsm",
    "UK",
    "IMV_annual_operating_hours_maximum_per_transformation_process*",
    {"REGIONS_9_I": ["UK"], "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"]},
)

_ext_constant_protra_max_full_load_hours.add(
    "model_parameters/energy/energy.xlsm",
    "USMCA",
    "IMV_annual_operating_hours_maximum_per_transformation_process*",
    {"REGIONS_9_I": ["USMCA"], "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"]},
)


@component.add(
    name="PROTRA_UTILIZATION_ALLOCATION_PRIORITIES_SP",
    units="DMNL",
    subscripts=["REGIONS_9_I", "NRG_PROTRA_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_protra_utilization_allocation_priorities_sp"
    },
)
def protra_utilization_allocation_priorities_sp():
    """
    Exogenous allocation priorities for energy transformation technologies (PROTRA). Note: In Technology Utilization Heat is allcoated first to determin CHP-Utilization (and related electricity production), than electricity is allocated in a second step to all PP technologies.
    """
    return _ext_constant_protra_utilization_allocation_priorities_sp()


_ext_constant_protra_utilization_allocation_priorities_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "PROTRA_UTILIZATION_ALLOCATION_PRIORITIES_SP*",
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
    },
    _root,
    {
        "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
        "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
    },
    "_ext_constant_protra_utilization_allocation_priorities_sp",
)


@component.add(
    name="PROTRA_UTILIZATION_PRIORITIES_POLICYWEIGHT_SP",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_protra_utilization_priorities_policyweight_sp"
    },
)
def protra_utilization_priorities_policyweight_sp():
    """
    Weight of the (exogeneous) policy allocation priority. The missing quantity to 1 is the weight of the endogeneous allocation factors. If this parameter = 1 then the endogenous component is omitted.
    """
    return _ext_constant_protra_utilization_priorities_policyweight_sp()


_ext_constant_protra_utilization_priorities_policyweight_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "PROTRA_UTILIZATION_PRIORITIES_POLICYWEIGHT_SP",
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    _root,
    {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]},
    "_ext_constant_protra_utilization_priorities_policyweight_sp",
)
