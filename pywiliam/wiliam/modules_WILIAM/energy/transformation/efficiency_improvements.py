"""
Module energy.transformation.efficiency_improvements
Translated using PySD version 3.10.0
"""


@component.add(
    name="ANNUAL_EFFICIENCY_INCREASE_PV_SP",
    units="DMNL/Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_annual_efficiency_increase_pv_sp"},
)
def annual_efficiency_increase_pv_sp():
    """
    annual increase of PV panel efficiency. An expected 0.3%/year improvement in efficiency across all technologies has been estimated after observing efficiency improvement trends in previous years (IHS Markit, 2019).
    """
    return _ext_constant_annual_efficiency_increase_pv_sp()


_ext_constant_annual_efficiency_increase_pv_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "ANNUAL_EFFICIENCY_INCREASE_PV_SP",
    {},
    _root,
    {},
    "_ext_constant_annual_efficiency_increase_pv_sp",
)


@component.add(
    name="area_PV_panel_per_power",
    units="m2/w",
    subscripts=["PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"power_per_panel_by_pv_technology": 1, "surface_pv_panel": 1},
)
def area_pv_panel_per_power():
    """
    Area of photovoltaic panels which produce a MW of maximum power (Wp).
    """
    return (1 / power_per_panel_by_pv_technology()) * surface_pv_panel()


@component.add(
    name="EFFICIENCES_MAX_PV_TECHNOLOGY",
    units="DMNL",
    subscripts=["PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_efficiences_max_pv_technology"},
)
def efficiences_max_pv_technology():
    """
    maximum efficiencies of photovoltaic panels. Photovoltaic panels have a theoretical maximum efficiency, called the Shockley-Queisser limit (Shockley and Queisser, 1961). This maximum efficiency is 29.1% for silicon panels and 33.7% for thin-film panels (Rühle, 2016).
    """
    return _ext_constant_efficiences_max_pv_technology()


_ext_constant_efficiences_max_pv_technology = ExtConstant(
    "model_parameters/energy/energy.xlsm",
    "PV",
    "EFFICIENCES_MAX_PV_TECHNOLOGY*",
    {
        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": _subscript_dict[
            "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"
        ]
    },
    _root,
    {
        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": _subscript_dict[
            "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"
        ]
    },
    "_ext_constant_efficiences_max_pv_technology",
)


@component.add(
    name="efficiences_PV_technology_panels",
    units="DMNL",
    subscripts=["PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_efficiences_pv_technology_panels": 1},
    other_deps={
        "_integ_efficiences_pv_technology_panels": {
            "initial": {"initial_pv_modules_efficiency": 1},
            "step": {"efficiency_increase_pv_panels": 1},
        }
    },
)
def efficiences_pv_technology_panels():
    """
    Efficiencies of photovoltaic panels over time.
    """
    return _integ_efficiences_pv_technology_panels()


_integ_efficiences_pv_technology_panels = Integ(
    lambda: efficiency_increase_pv_panels(),
    lambda: initial_pv_modules_efficiency(),
    "_integ_efficiences_pv_technology_panels",
)


@component.add(
    name="efficiency_increase_PV_panels",
    units="1/Year",
    subscripts=["PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 4,
        "historic_pv_modules_efficiency": 2,
        "efficiences_max_pv_technology": 1,
        "annual_efficiency_increase_pv_sp": 1,
        "efficiences_pv_technology_panels": 1,
        "initial_year_efficiency_increase_rate_pv_sp": 1,
    },
)
def efficiency_increase_pv_panels():
    """
    Annual increase in PV panel efficiency
    """
    return if_then_else(
        time() < 2022,
        lambda: historic_pv_modules_efficiency(time() + 1)
        - historic_pv_modules_efficiency(time()),
        lambda: if_then_else(
            np.logical_and(
                time() > initial_year_efficiency_increase_rate_pv_sp(),
                efficiences_pv_technology_panels() < efficiences_max_pv_technology(),
            ),
            lambda: xr.DataArray(
                annual_efficiency_increase_pv_sp(),
                {
                    "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": _subscript_dict[
                        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"
                    ]
                },
                ["PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"],
            ),
            lambda: xr.DataArray(
                0,
                {
                    "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": _subscript_dict[
                        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"
                    ]
                },
                ["PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"],
            ),
        ),
    )


@component.add(
    name="HISTORIC_PV_MODULES_EFFICIENCY",
    units="DMNL",
    subscripts=["PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_historic_pv_modules_efficiency",
        "__lookup__": "_ext_lookup_historic_pv_modules_efficiency",
    },
)
def historic_pv_modules_efficiency(x, final_subs=None):
    """
    Historic efficiencies of photovoltaic panels. Own estimation.
    """
    return _ext_lookup_historic_pv_modules_efficiency(x, final_subs)


_ext_lookup_historic_pv_modules_efficiency = ExtLookup(
    "model_parameters/energy/energy.xlsm",
    "PV",
    "TIME_INDEX_HISTORIC_PV_MODULES_EFFICIENCY",
    "HISTORIC_PV_MODULES_EFFICIENCY",
    {
        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": _subscript_dict[
            "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"
        ]
    },
    _root,
    {
        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": _subscript_dict[
            "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"
        ]
    },
    "_ext_lookup_historic_pv_modules_efficiency",
)


@component.add(
    name="INITIAL_AREA_PV_PANEL_PER_POWER",
    subscripts=["PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"power_pv_panel_baseline": 1, "surface_pv_panel": 1},
)
def initial_area_pv_panel_per_power():
    return (1 / power_pv_panel_baseline()) * surface_pv_panel()


@component.add(
    name="INITIAL_PV_MODULES_EFFICIENCY",
    units="DMNL",
    subscripts=["PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_pv_modules_efficiency"},
)
def initial_pv_modules_efficiency():
    return _ext_constant_initial_pv_modules_efficiency()


_ext_constant_initial_pv_modules_efficiency = ExtConstant(
    "model_parameters/energy/energy.xlsm",
    "PV",
    "INITIAL_PV_MODULES_EFFICIENCY*",
    {
        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": _subscript_dict[
            "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"
        ]
    },
    _root,
    {
        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": _subscript_dict[
            "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"
        ]
    },
    "_ext_constant_initial_pv_modules_efficiency",
)


@component.add(
    name="INITIAL_YEAR_EFFICIENCY_INCREASE_RATE_PV_SP",
    units="DMNL/Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_initial_year_efficiency_increase_rate_pv_sp"
    },
)
def initial_year_efficiency_increase_rate_pv_sp():
    """
    Initial year to apply the improvement of PV panel efficiencies for solar PV technologies.
    """
    return _ext_constant_initial_year_efficiency_increase_rate_pv_sp()


_ext_constant_initial_year_efficiency_increase_rate_pv_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "INITIAL_YEAR_EFFICIENCY_INCREASE_RATE_PV_SP",
    {},
    _root,
    {},
    "_ext_constant_initial_year_efficiency_increase_rate_pv_sp",
)


@component.add(
    name="IRRADIANCE_STANDAR_CONDITIONS",
    units="w/(m*m)",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_irradiance_standar_conditions"},
)
def irradiance_standar_conditions():
    """
    irradiance in standar conditions (1000 W/M2) and 25 º
    """
    return _ext_constant_irradiance_standar_conditions()


_ext_constant_irradiance_standar_conditions = ExtConstant(
    "model_parameters/energy/energy.xlsm",
    "PV",
    "IRRADIANCE_STANDAR_CONDITIONS",
    {},
    _root,
    {},
    "_ext_constant_irradiance_standar_conditions",
)


@component.add(
    name="power_per_panel_by_PV_technology",
    units="w/panel",
    subscripts=["PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"power_pv_panel_baseline": 1, "efficiences_pv_technology_panels": 1},
)
def power_per_panel_by_pv_technology():
    """
    Power of 1 photovoltaic panel by PV subtechnology over time.
    """
    return power_pv_panel_baseline() * efficiences_pv_technology_panels()


@component.add(
    name="POWER_PV_PANEL_BASELINE",
    units="w/panel",
    subscripts=["PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_power_pv_panel_baseline"},
)
def power_pv_panel_baseline():
    """
    initial power of photovoltaic panels. The chosen commercial panel (SUNPOWER MAXEON 5, 22.2%) has been adapted to the chosen 24.4% efficiency by increasing its power linearly with the efficiency. For the rest of the panels, these values have only been varied proportionally to the difference in efficiency with the monocrystalline silicon panel.
    """
    return _ext_constant_power_pv_panel_baseline()


_ext_constant_power_pv_panel_baseline = ExtConstant(
    "model_parameters/energy/energy.xlsm",
    "PV",
    "POWER_PV_PANEL_BASELINE*",
    {
        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": _subscript_dict[
            "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"
        ]
    },
    _root,
    {
        "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": _subscript_dict[
            "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"
        ]
    },
    "_ext_constant_power_pv_panel_baseline",
)


@component.add(
    name="power_PV_per_panel_area",
    units="MW/km2",
    subscripts=["PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "efficiences_pv_technology_panels": 1,
        "irradiance_standar_conditions": 1,
        "unit_conversion_m2_km2": 1,
        "unit_conversion_w_mw": 1,
    },
)
def power_pv_per_panel_area():
    """
    Power in MW per km2 of area of panels.
    """
    return (
        efficiences_pv_technology_panels()
        * irradiance_standar_conditions()
        * unit_conversion_m2_km2()
        * (1 / unit_conversion_w_mw())
    )


@component.add(
    name="SURFACE_PV_PANEL",
    units="m2/panel",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_surface_pv_panel"},
)
def surface_pv_panel():
    """
    Surface of a PV panel. The SUN POWER Maxeon 5 (SUNPOWER, 2020), a monocrystalline panel with 2.12 m2, has been chosen as the base commercial panel.
    """
    return _ext_constant_surface_pv_panel()


_ext_constant_surface_pv_panel = ExtConstant(
    "model_parameters/energy/energy.xlsm",
    "PV",
    "SURFACE_PV_PANEL",
    {},
    _root,
    {},
    "_ext_constant_surface_pv_panel",
)
