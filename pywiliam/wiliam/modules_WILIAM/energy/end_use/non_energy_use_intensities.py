"""
Module energy.end_use.non_energy_use_intensities
Translated using PySD version 3.10.0
"""


@component.add(
    name="final_non_energy_demand_by_FE_35R",
    units="TJ/Year",
    subscripts=["REGIONS_35_I", "NRG_FE_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"final_non_energy_demand_by_sectors_and_fe": 1},
)
def final_non_energy_demand_by_fe_35r():
    """
    Final energy demand by final energy 35 regions
    """
    return sum(
        final_non_energy_demand_by_sectors_and_fe().rename({"SECTORS_I": "SECTORS_I!"}),
        dim=["SECTORS_I!"],
    )


@component.add(
    name="final_non_energy_demand_by_FE_9R",
    units="TJ/Year",
    subscripts=["REGIONS_9_I", "NRG_FE_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "final_non_energy_demand_by_fe_eu27": 3,
        "final_non_energy_demand_by_fe_35r": 3,
        "switch_hydrogen_industrial_demand": 2,
        "h2_total_demand_lhv_basis": 2,
    },
)
def final_non_energy_demand_by_fe_9r():
    """
    Final energy demand by final energy 9 regions
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "NRG_FE_I": _subscript_dict["NRG_FE_I"],
        },
        ["REGIONS_9_I", "NRG_FE_I"],
    )
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[["EU27"], :] = True
    except_subs.loc[["EU27"], ["FE_hydrogen"]] = False
    value.values[except_subs.values] = (
        final_non_energy_demand_by_fe_eu27()
        .expand_dims({"REGIONS_36_I": ["EU27"]}, 0)
        .values[except_subs.loc[["EU27"], :].values]
    )
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[_subscript_dict["REGIONS_8_I"], :] = True
    except_subs.loc[_subscript_dict["REGIONS_8_I"], ["FE_hydrogen"]] = False
    value.values[except_subs.values] = (
        final_non_energy_demand_by_fe_35r()
        .loc[_subscript_dict["REGIONS_8_I"], :]
        .rename({"REGIONS_35_I": "REGIONS_8_I"})
        .values[except_subs.loc[_subscript_dict["REGIONS_8_I"], :].values]
    )
    value.loc[["EU27"], ["FE_hydrogen"]] = if_then_else(
        switch_hydrogen_industrial_demand() == 1,
        lambda: float(final_non_energy_demand_by_fe_eu27().loc["FE_hydrogen"])
        + float(h2_total_demand_lhv_basis().loc["EU27"]),
        lambda: float(final_non_energy_demand_by_fe_eu27().loc["FE_hydrogen"]),
    )
    value.loc[_subscript_dict["REGIONS_8_I"], ["FE_hydrogen"]] = (
        if_then_else(
            switch_hydrogen_industrial_demand() == 1,
            lambda: final_non_energy_demand_by_fe_35r()
            .loc[_subscript_dict["REGIONS_8_I"], "FE_hydrogen"]
            .reset_coords(drop=True)
            .rename({"REGIONS_35_I": "REGIONS_8_I"})
            + h2_total_demand_lhv_basis()
            .loc[_subscript_dict["REGIONS_8_I"]]
            .rename({"REGIONS_9_I": "REGIONS_8_I"}),
            lambda: final_non_energy_demand_by_fe_35r()
            .loc[_subscript_dict["REGIONS_8_I"], "FE_hydrogen"]
            .reset_coords(drop=True)
            .rename({"REGIONS_35_I": "REGIONS_8_I"}),
        )
        .expand_dims({"NRG_COMMODITIES_I": ["FE_hydrogen"]}, 1)
        .values
    )
    return value


@component.add(
    name="final_non_energy_demand_by_FE_EU27",
    units="TJ/Year",
    subscripts=["NRG_FE_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"final_non_energy_demand_by_fe_35r": 1},
)
def final_non_energy_demand_by_fe_eu27():
    """
    Final energy demand by final energy EU27
    """
    return sum(
        final_non_energy_demand_by_fe_35r()
        .loc[_subscript_dict["REGIONS_EU27_I"], :]
        .rename({"REGIONS_35_I": "REGIONS_EU27_I!"}),
        dim=["REGIONS_EU27_I!"],
    )


@component.add(
    name="final_non_energy_demand_by_sectors_and_FE",
    units="TJ/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I", "NRG_FE_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_energy": 1,
        "non_energy_use_intensities_by_sector_and_fe": 3,
        "base_output_real": 2,
        "switch_eco2nrg_output_real": 1,
        "output_real": 1,
    },
)
def final_non_energy_demand_by_sectors_and_fe():
    """
    Final energy demand by non energy sectors and final energy
    """
    return if_then_else(
        switch_energy() == 0,
        lambda: non_energy_use_intensities_by_sector_and_fe() * base_output_real(),
        lambda: if_then_else(
            switch_eco2nrg_output_real() == 0,
            lambda: non_energy_use_intensities_by_sector_and_fe() * base_output_real(),
            lambda: non_energy_use_intensities_by_sector_and_fe() * output_real(),
        ),
    )


@component.add(
    name="HISTORICAL_GROWTH_NON_ENERGY_USE_INTENSITY_BY_FE",
    subscripts=["REGIONS_35_I", "NRG_FE_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_historical_growth_non_energy_use_intensity_by_fe"
    },
)
def historical_growth_non_energy_use_intensity_by_fe():
    return _ext_constant_historical_growth_non_energy_use_intensity_by_fe()


_ext_constant_historical_growth_non_energy_use_intensity_by_fe = ExtConstant(
    "model_parameters/energy/energy-end_use.xlsx",
    "Hist_non_energy_use_int_variati",
    "HISTORIC_NON_ENERGY_USE_INTENSITY_VARIATION_BY_FINAL_ENERGY",
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
    _root,
    {
        "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
        "NRG_FE_I": _subscript_dict["NRG_FE_I"],
    },
    "_ext_constant_historical_growth_non_energy_use_intensity_by_fe",
)


@component.add(
    name="non_energy_use_intensities_by_sector_and_FE",
    units="TJ/million$",
    subscripts=["REGIONS_35_I", "SECTORS_I", "NRG_FE_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_non_energy_use_intensities_by_sector_and_fe": 1},
    other_deps={
        "_integ_non_energy_use_intensities_by_sector_and_fe": {
            "initial": {"historical_non_energy_use_intensities_by_sector_and_fe": 1},
            "step": {"variation_non_energy_use_intensity": 1},
        }
    },
)
def non_energy_use_intensities_by_sector_and_fe():
    """
    Energy intensities of non energy sectors
    """
    return _integ_non_energy_use_intensities_by_sector_and_fe()


_integ_non_energy_use_intensities_by_sector_and_fe = Integ(
    lambda: variation_non_energy_use_intensity(),
    lambda: historical_non_energy_use_intensities_by_sector_and_fe(),
    "_integ_non_energy_use_intensities_by_sector_and_fe",
)


@component.add(
    name="SELECT_NON_ENERGY_USE_INTENSITIES_SECTOR",
    comp_type="Constant",
    comp_subtype="Normal",
)
def select_non_energy_use_intensities_sector():
    """
    0- Constant 1- Historic trends
    """
    return 1


@component.add(
    name="SWITCH_HYDROGEN_INDUSTRIAL_DEMAND",
    units="DMML",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_hydrogen_industrial_demand"},
)
def switch_hydrogen_industrial_demand():
    """
    This switch can take two values: 0: the energy module runs isolated from hydrogen views. 1: the energy module runs integrated with hydrogen views.
    """
    return _ext_constant_switch_hydrogen_industrial_demand()


_ext_constant_switch_hydrogen_industrial_demand = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_TEST_HYDROGEN",
    {},
    _root,
    {},
    "_ext_constant_switch_hydrogen_industrial_demand",
)


@component.add(
    name="variation_non_energy_use_intensity",
    units="TJ/million$/Year",
    subscripts=["REGIONS_35_I", "SECTORS_I", "NRG_FE_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_non_energy_use_intensities_sector": 1,
        "time": 1,
        "historical_growth_non_energy_use_intensity_by_fe": 3,
        "non_energy_use_intensities_by_sector_and_fe": 1,
        "historical_non_energy_use_intensities_by_sector_and_fe": 1,
    },
)
def variation_non_energy_use_intensity():
    """
    Inertial trend of energy intensities of non energy sectors Test Oil with change Time switch set from 2015 to 2040
    """
    return if_then_else(
        select_non_energy_use_intensities_sector() == 0,
        lambda: xr.DataArray(
            0,
            {
                "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                "NRG_FE_I": _subscript_dict["NRG_FE_I"],
                "SECTORS_I": _subscript_dict["SECTORS_I"],
            },
            ["REGIONS_35_I", "NRG_FE_I", "SECTORS_I"],
        ),
        lambda: if_then_else(
            time() < 2015,
            lambda: xr.DataArray(
                0,
                {
                    "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                    "NRG_FE_I": _subscript_dict["NRG_FE_I"],
                    "SECTORS_I": _subscript_dict["SECTORS_I"],
                },
                ["REGIONS_35_I", "NRG_FE_I", "SECTORS_I"],
            ),
            lambda: if_then_else(
                (historical_growth_non_energy_use_intensity_by_fe() < 0).expand_dims(
                    {"SECTORS_I": _subscript_dict["SECTORS_I"]}, 2
                ),
                lambda: (
                    non_energy_use_intensities_by_sector_and_fe()
                    * historical_growth_non_energy_use_intensity_by_fe()
                ).transpose("REGIONS_35_I", "NRG_FE_I", "SECTORS_I"),
                lambda: historical_growth_non_energy_use_intensity_by_fe()
                * historical_non_energy_use_intensities_by_sector_and_fe().transpose(
                    "REGIONS_35_I", "NRG_FE_I", "SECTORS_I"
                ),
            ),
        ),
    ).transpose("REGIONS_35_I", "SECTORS_I", "NRG_FE_I")
