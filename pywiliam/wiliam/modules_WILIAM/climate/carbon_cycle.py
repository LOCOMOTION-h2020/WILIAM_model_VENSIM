"""
Module climate.carbon_cycle
Translated using PySD version 3.10.0
"""


@component.add(
    name="atmospheric_concentrations_CO2",
    units="ppm",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"c_in_atmosphere": 1, "unit_conversion_gtc_ppm": 1},
)
def atmospheric_concentrations_co2():
    """
    1 part per million of atmospheric CO2 is equivalent to 2.13 Gigatonnes Carbon. Historical Mauna Loa CO2 Record: ftp://ftp.cmdl.noaa.gov/products/trends/co2/co2_mm_mlo.txt
    """
    return c_in_atmosphere() / unit_conversion_gtc_ppm()


@component.add(
    name="BIOSTIMULATION_COEFF",
    units="DMNL",
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_biostimulation_coeff": 1},
    other_deps={
        "_initial_biostimulation_coeff": {
            "initial": {
                "biostimulation_coeff_index": 1,
                "biostimulation_coeff_mean": 1,
            },
            "step": {},
        }
    },
)
def biostimulation_coeff():
    """
    Coefficient for response of primary production to carbon concentration.
    """
    return _initial_biostimulation_coeff()


_initial_biostimulation_coeff = Initial(
    lambda: biostimulation_coeff_index() * biostimulation_coeff_mean(),
    "_initial_biostimulation_coeff",
)


@component.add(
    name="buffer_factor",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"_active_initial_buffer_factor": 1},
    other_deps={
        "_active_initial_buffer_factor": {
            "initial": {"ref_buffer_factor": 1},
            "step": {
                "ref_buffer_factor": 1,
                "c_in_mixed_layer": 1,
                "buff_c_coeff": 1,
                "preind_c_in_mixed_layer": 1,
            },
        }
    },
)
def buffer_factor():
    """
    Buffer factor for atmosphere/mixed ocean carbon equilibration.
    """
    return active_initial(
        __data["time"].stage,
        lambda: ref_buffer_factor()
        * (c_in_mixed_layer() / preind_c_in_mixed_layer()) ** buff_c_coeff(),
        ref_buffer_factor(),
    )


@component.add(
    name="C_from_CH4_oxidation",
    units="Gt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "ch4_uptake": 1,
        "unit_conversion_ch4_c": 1,
        "unit_conversion_mt_gt": 1,
    },
)
def c_from_ch4_oxidation():
    """
    Flux of C into the atmosphere from the oxidation of CH4, the mode of removal of CH4 from atmosphere.
    """
    return ch4_uptake() / unit_conversion_ch4_c() / unit_conversion_mt_gt()


@component.add(
    name="C_in_atmosphere",
    units="Gt",
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_c_in_atmosphere": 1},
    other_deps={
        "_integ_c_in_atmosphere": {
            "initial": {"init_c_in_atmosphere": 1},
            "step": {
                "c_from_ch4_oxidation": 1,
                "flux_biomass_to_atmosphere": 1,
                "flux_humus_to_atmosphere": 1,
                "total_c_anthro_emissions": 1,
                "flux_atm_to_biomass": 1,
                "flux_atm_to_ocean": 1,
                "flux_c_from_permafrost_release": 1,
            },
        }
    },
)
def c_in_atmosphere():
    """
    Carbon in atmosphere.
    """
    return _integ_c_in_atmosphere()


_integ_c_in_atmosphere = Integ(
    lambda: c_from_ch4_oxidation()
    + flux_biomass_to_atmosphere()
    + flux_humus_to_atmosphere()
    + total_c_anthro_emissions()
    - flux_atm_to_biomass()
    - flux_atm_to_ocean()
    + flux_c_from_permafrost_release(),
    lambda: init_c_in_atmosphere(),
    "_integ_c_in_atmosphere",
)


@component.add(
    name="C_in_biomass",
    units="Gt",
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_c_in_biomass": 1},
    other_deps={
        "_integ_c_in_biomass": {
            "initial": {"init_c_in_biomass": 1},
            "step": {
                "flux_atm_to_biomass": 1,
                "flux_biomass_to_atmosphere": 1,
                "flux_biomass_to_ch4": 1,
                "flux_biomass_to_humus": 1,
            },
        }
    },
)
def c_in_biomass():
    """
    Carbon in biomass.
    """
    return _integ_c_in_biomass()


_integ_c_in_biomass = Integ(
    lambda: flux_atm_to_biomass()
    - flux_biomass_to_atmosphere()
    - flux_biomass_to_ch4()
    - flux_biomass_to_humus(),
    lambda: init_c_in_biomass(),
    "_integ_c_in_biomass",
)


@component.add(
    name="C_in_deep_ocean",
    units="Gt",
    subscripts=["LAYERS_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_c_in_deep_ocean": 1, "_integ_c_in_deep_ocean_1": 1},
    other_deps={
        "_integ_c_in_deep_ocean": {
            "initial": {"init_c_in_deep_ocean_per_meter": 1, "layer_depth": 1},
            "step": {"diffusion_flux": 2},
        },
        "_integ_c_in_deep_ocean_1": {
            "initial": {"init_c_in_deep_ocean_per_meter": 1, "layer_depth": 1},
            "step": {"diffusion_flux": 1},
        },
    },
)
def c_in_deep_ocean():
    """
    Carbon in deep ocean.
    """
    value = xr.DataArray(
        np.nan, {"LAYERS_I": _subscript_dict["LAYERS_I"]}, ["LAYERS_I"]
    )
    value.loc[_subscript_dict["upper"]] = _integ_c_in_deep_ocean().values
    value.loc[["Layer4"]] = _integ_c_in_deep_ocean_1().values
    return value


_integ_c_in_deep_ocean = Integ(
    lambda: diffusion_flux().loc[_subscript_dict["upper"]].rename({"LAYERS_I": "upper"})
    - xr.DataArray(
        diffusion_flux()
        .loc[_subscript_dict["lower"]]
        .rename({"LAYERS_I": "lower"})
        .values,
        {"upper": _subscript_dict["upper"]},
        ["upper"],
    ),
    lambda: init_c_in_deep_ocean_per_meter()
    .loc[_subscript_dict["upper"]]
    .rename({"LAYERS_I": "upper"})
    * layer_depth().loc[_subscript_dict["upper"]].rename({"LAYERS_I": "upper"}),
    "_integ_c_in_deep_ocean",
)

_integ_c_in_deep_ocean_1 = Integ(
    lambda: xr.DataArray(
        float(diffusion_flux().loc["Layer4"]),
        {"bottom": _subscript_dict["bottom"]},
        ["bottom"],
    ),
    lambda: xr.DataArray(
        float(init_c_in_deep_ocean_per_meter().loc["Layer4"])
        * float(layer_depth().loc["Layer4"]),
        {"bottom": _subscript_dict["bottom"]},
        ["bottom"],
    ),
    "_integ_c_in_deep_ocean_1",
)


@component.add(
    name="C_in_deep_ocean_per_meter",
    units="Gt/m",
    subscripts=["LAYERS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"c_in_deep_ocean": 1, "layer_depth": 1},
)
def c_in_deep_ocean_per_meter():
    """
    Concentration of carbon in ocean layers.
    """
    return c_in_deep_ocean() / layer_depth()


@component.add(
    name="C_in_humus",
    units="Gt",
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_c_in_humus": 1},
    other_deps={
        "_integ_c_in_humus": {
            "initial": {"init_c_in_humus": 1},
            "step": {
                "flux_biomass_to_humus": 1,
                "flux_humus_to_atmosphere": 1,
                "flux_humus_to_ch4": 1,
            },
        }
    },
)
def c_in_humus():
    """
    Carbon in humus.
    """
    return _integ_c_in_humus()


_integ_c_in_humus = Integ(
    lambda: flux_biomass_to_humus() - flux_humus_to_atmosphere() - flux_humus_to_ch4(),
    lambda: init_c_in_humus(),
    "_integ_c_in_humus",
)


@component.add(
    name="C_in_mixed_layer",
    units="Gt",
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_c_in_mixed_layer": 1},
    other_deps={
        "_integ_c_in_mixed_layer": {
            "initial": {"init_c_in_mixed_ocean_per_meter": 1, "mixed_depth": 1},
            "step": {"flux_atm_to_ocean": 1, "diffusion_flux": 1},
        }
    },
)
def c_in_mixed_layer():
    """
    Carbon in mixed layer.
    """
    return _integ_c_in_mixed_layer()


_integ_c_in_mixed_layer = Integ(
    lambda: flux_atm_to_ocean() - float(diffusion_flux().loc["Layer1"]),
    lambda: init_c_in_mixed_ocean_per_meter() * mixed_depth(),
    "_integ_c_in_mixed_layer",
)


@component.add(
    name="C_in_mixed_layer_per_meter",
    units="Gt/m",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"c_in_mixed_layer": 1, "mixed_depth": 1},
)
def c_in_mixed_layer_per_meter():
    """
    Concentration of carbon in mixed layers.
    """
    return c_in_mixed_layer() / mixed_depth()


@component.add(
    name="diffusion_flux",
    units="Gt/Year",
    subscripts=["LAYERS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "c_in_mixed_layer_per_meter": 1,
        "c_in_deep_ocean_per_meter": 3,
        "eddy_diff_coeff": 2,
        "mean_depth_of_adjacent_layers": 2,
    },
)
def diffusion_flux():
    """
    Diffusion flux between ocean layers.
    """
    value = xr.DataArray(
        np.nan, {"LAYERS_I": _subscript_dict["LAYERS_I"]}, ["LAYERS_I"]
    )
    value.loc[["Layer1"]] = (
        (
            c_in_mixed_layer_per_meter()
            - float(c_in_deep_ocean_per_meter().loc["Layer1"])
        )
        * eddy_diff_coeff()
        / float(mean_depth_of_adjacent_layers().loc["Layer1"])
    )
    value.loc[_subscript_dict["lower"]] = (
        (
            xr.DataArray(
                c_in_deep_ocean_per_meter()
                .loc[_subscript_dict["upper"]]
                .rename({"LAYERS_I": "upper"})
                .values,
                {"lower": _subscript_dict["lower"]},
                ["lower"],
            )
            - c_in_deep_ocean_per_meter()
            .loc[_subscript_dict["lower"]]
            .rename({"LAYERS_I": "lower"})
        )
        * eddy_diff_coeff()
        / mean_depth_of_adjacent_layers()
        .loc[_subscript_dict["lower"]]
        .rename({"LAYERS_I": "lower"})
    ).values
    return value


@component.add(
    name="EDDY_DIFF_COEFF",
    units="m*m/Year",
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_eddy_diff_coeff": 1},
    other_deps={
        "_initial_eddy_diff_coeff": {
            "initial": {"eddy_diff_coeff_index": 1, "eddy_diff_mean": 1},
            "step": {},
        }
    },
)
def eddy_diff_coeff():
    """
    Multiplier of eddy diffusion coefficient mean
    """
    return _initial_eddy_diff_coeff()


_initial_eddy_diff_coeff = Initial(
    lambda: eddy_diff_coeff_index() * eddy_diff_mean(), "_initial_eddy_diff_coeff"
)


@component.add(
    name="effect_of_temp_on_dic_p_CO2",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"sensitivity_of_pco2_dic_to_temperature": 1, "temperature_change": 1},
)
def effect_of_temp_on_dic_p_co2():
    """
    The fractional reduction in the solubility of CO2 in ocean falls with rising temperatures. We assume a linear relationship, likely a good approximation over the typical range for warming by 2100.
    """
    return 1 - sensitivity_of_pco2_dic_to_temperature() * temperature_change()


@component.add(
    name="effect_of_warming_on_C_flux_to_biomass",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "strength_of_temp_effect_on_c_flux_to_land": 1,
        "temperature_change": 1,
    },
)
def effect_of_warming_on_c_flux_to_biomass():
    """
    The fractional reduction in the flux of C from the atmosphere to biomass with rising temperatures. We assume a linear relationship, likely a good approxim
    """
    return 1 + strength_of_temp_effect_on_c_flux_to_land() * temperature_change()


@component.add(
    name="effect_of_warming_on_CH4_release_from_biological_activity",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "sensitivity_of_methane_emissions_to_temperature": 1,
        "temperature_change": 1,
        "reference_temperature_change_for_effect_of_warming_on_ch4_from_respiration": 1,
    },
)
def effect_of_warming_on_ch4_release_from_biological_activity():
    """
    The fractional increase in the flux of C as CH4 from humus with rising temperatures. We assume a linear relationship, likely a good approximation over the typical range for warming by 2100.
    """
    return (
        1
        + sensitivity_of_methane_emissions_to_temperature()
        * temperature_change()
        / reference_temperature_change_for_effect_of_warming_on_ch4_from_respiration()
    )


@component.add(
    name="equil_C_in_mixed_layer",
    units="Gt",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "preind_c_in_mixed_layer": 1,
        "effect_of_temp_on_dic_p_co2": 1,
        "buffer_factor": 1,
        "preindustrial_c": 1,
        "c_in_atmosphere": 1,
    },
)
def equil_c_in_mixed_layer():
    """
    Equilibrium carbon content of mixed layer. Determined by the Revelle buffering factor, and by temperature. For simplicity, we assume a linear impact of warming on the equilibrium solubility of CO2 in the ocean.
    """
    return (
        preind_c_in_mixed_layer()
        * effect_of_temp_on_dic_p_co2()
        * (c_in_atmosphere() / preindustrial_c()) ** (1 / buffer_factor())
    )


@component.add(
    name="equilibrium_C_per_meter_in_mixed_layer",
    units="Gt/m",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"equil_c_in_mixed_layer": 1, "mixed_depth": 1},
)
def equilibrium_c_per_meter_in_mixed_layer():
    """
    The equilibrium concentration of C in the mixed layer, in GtC/meter, based on the total quantity of C in that layer and the average layer depth.
    """
    return equil_c_in_mixed_layer() / mixed_depth()


@component.add(
    name="flux_atm_to_biomass",
    units="Gt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "init_npp": 1,
        "preindustrial_c": 1,
        "biostimulation_coeff": 1,
        "c_in_atmosphere": 1,
        "effect_of_warming_on_c_flux_to_biomass": 1,
    },
)
def flux_atm_to_biomass():
    """
    Carbon flux from atmosphere to biosphere (from primary production)
    """
    return (
        init_npp()
        * (1 + biostimulation_coeff() * np.log(c_in_atmosphere() / preindustrial_c()))
        * effect_of_warming_on_c_flux_to_biomass()
    )


@component.add(
    name="flux_atm_to_ocean",
    units="Gt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"equil_c_in_mixed_layer": 1, "c_in_mixed_layer": 1, "mixing_time": 1},
)
def flux_atm_to_ocean():
    """
    Carbon flux from atmosphere to mixed ocean layer.
    """
    return (equil_c_in_mixed_layer() - c_in_mixed_layer()) / mixing_time()


@component.add(
    name="flux_biomass_to_atmosphere",
    units="Gt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "c_in_biomass": 1,
        "residential_time_of_biomass": 1,
        "humification_fraction": 1,
    },
)
def flux_biomass_to_atmosphere():
    """
    Carbon flux from biomass to atmosphere.
    """
    return (
        c_in_biomass() / residential_time_of_biomass() * (1 - humification_fraction())
    )


@component.add(
    name="flux_biomass_to_CH4",
    units="Gt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "c_in_biomass": 1,
        "ch4_generation_rate_from_biomass": 1,
        "effect_of_warming_on_ch4_release_from_biological_activity": 1,
    },
)
def flux_biomass_to_ch4():
    """
    The natural flux of methane from C in biomass. The sum of the flux of methane from C in humus and the flux of methane from C in biomass yields the natural emissions of methane. Adjusted to account for temperature feedback.
    """
    return (
        c_in_biomass()
        * ch4_generation_rate_from_biomass()
        * effect_of_warming_on_ch4_release_from_biological_activity()
    )


@component.add(
    name="flux_biomass_to_humus",
    units="Gt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "c_in_biomass": 1,
        "residential_time_of_biomass": 1,
        "humification_fraction": 1,
    },
)
def flux_biomass_to_humus():
    """
    Carbon flux from biomass to humus.
    """
    return c_in_biomass() / residential_time_of_biomass() * humification_fraction()


@component.add(
    name="flux_biosphere_to_CH4",
    units="Gt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"flux_biomass_to_ch4": 1, "flux_humus_to_ch4": 1},
)
def flux_biosphere_to_ch4():
    """
    Carbon flux from biosphere as methane, in GtC/year, arising from anaerobic respiration.
    """
    return flux_biomass_to_ch4() + flux_humus_to_ch4()


@component.add(
    name="flux_humus_to_atmosphere",
    units="Gt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"c_in_humus": 1, "humus_res_time": 1},
)
def flux_humus_to_atmosphere():
    """
    Carbon flux from humus to atmosphere.
    """
    return c_in_humus() / humus_res_time()


@component.add(
    name="flux_humus_to_CH4",
    units="Gt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "c_in_humus": 1,
        "ch4_generation_rate_from_humus": 1,
        "effect_of_warming_on_ch4_release_from_biological_activity": 1,
    },
)
def flux_humus_to_ch4():
    """
    The natural flux of methane from C in humus. The sum of the flux of methane from C in humus and the flux of methane from C in biomass yields the natural emissions of methane. Adjusted to account for temperature feedback.
    """
    return (
        c_in_humus()
        * ch4_generation_rate_from_humus()
        * effect_of_warming_on_ch4_release_from_biological_activity()
    )


@component.add(
    name="INIT_C_IN_ATMOSPHERE",
    units="Gt",
    limits=(500.0, 1000.0),
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"init_co2_in_atmosphere_ppm": 1, "unit_conversion_gtc_ppm": 1},
)
def init_c_in_atmosphere():
    """
    Initial C in atmosphere. [DICE-1994] Initial Greenhouse Gases in Atmosphere 1965 [M(t)] (tC equivalent). [Cowles, pg. 21] /6.77e+011 / [DICE-2013R] mat0: Initial concentration in atmosphere 2010 (GtC) /830.4 /
    """
    return init_co2_in_atmosphere_ppm() * unit_conversion_gtc_ppm()


@component.add(
    name="LAYER_TIME_CONSTANT",
    units="Year",
    subscripts=["LAYERS_I"],
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_layer_time_constant": 1, "_initial_layer_time_constant_1": 1},
    other_deps={
        "_initial_layer_time_constant": {
            "initial": {
                "layer_depth": 1,
                "eddy_diff_coeff": 1,
                "mean_depth_of_adjacent_layers": 1,
            },
            "step": {},
        },
        "_initial_layer_time_constant_1": {
            "initial": {
                "layer_depth": 1,
                "eddy_diff_coeff": 1,
                "mean_depth_of_adjacent_layers": 1,
            },
            "step": {},
        },
    },
)
def layer_time_constant():
    """
    Time constant of exchange between layers.
    """
    value = xr.DataArray(
        np.nan, {"LAYERS_I": _subscript_dict["LAYERS_I"]}, ["LAYERS_I"]
    )
    value.loc[["Layer1"]] = _initial_layer_time_constant().values
    value.loc[_subscript_dict["lower"]] = _initial_layer_time_constant_1().values
    return value


_initial_layer_time_constant = Initial(
    lambda: xr.DataArray(
        float(layer_depth().loc["Layer1"])
        / (eddy_diff_coeff() / float(mean_depth_of_adjacent_layers().loc["Layer1"])),
        {"LAYERS_I": ["Layer1"]},
        ["LAYERS_I"],
    ),
    "_initial_layer_time_constant",
)

_initial_layer_time_constant_1 = Initial(
    lambda: layer_depth().loc[_subscript_dict["lower"]].rename({"LAYERS_I": "lower"})
    / (
        eddy_diff_coeff()
        / mean_depth_of_adjacent_layers()
        .loc[_subscript_dict["lower"]]
        .rename({"LAYERS_I": "lower"})
    ),
    "_initial_layer_time_constant_1",
)


@component.add(
    name="MEAN_DEPTH_OF_ADJACENT_LAYERS",
    units="m",
    subscripts=["LAYERS_I"],
    comp_type="Auxiliary, Stateful",
    comp_subtype="Initial, Normal",
    depends_on={"_initial_mean_depth_of_adjacent_layers": 1, "layer_depth": 2},
    other_deps={
        "_initial_mean_depth_of_adjacent_layers": {
            "initial": {"mixed_depth": 1, "layer_depth": 1},
            "step": {},
        }
    },
)
def mean_depth_of_adjacent_layers():
    """
    The mean depth of adjacent ocean layers.
    """
    value = xr.DataArray(
        np.nan, {"LAYERS_I": _subscript_dict["LAYERS_I"]}, ["LAYERS_I"]
    )
    value.loc[["Layer1"]] = _initial_mean_depth_of_adjacent_layers().values
    value.loc[_subscript_dict["lower"]] = (
        (
            xr.DataArray(
                layer_depth()
                .loc[_subscript_dict["upper"]]
                .rename({"LAYERS_I": "upper"})
                .values,
                {"lower": _subscript_dict["lower"]},
                ["lower"],
            )
            + layer_depth().loc[_subscript_dict["lower"]].rename({"LAYERS_I": "lower"})
        )
        / 2
    ).values
    return value


_initial_mean_depth_of_adjacent_layers = Initial(
    lambda: xr.DataArray(
        (mixed_depth() + float(layer_depth().loc["Layer1"])) / 2,
        {"LAYERS_I": ["Layer1"]},
        ["LAYERS_I"],
    ),
    "_initial_mean_depth_of_adjacent_layers",
)


@component.add(
    name="natural_CH4_emissions",
    units="Mt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "flux_biosphere_to_ch4": 1,
        "unit_conversion_ch4_c": 1,
        "unit_conversion_mt_gt": 1,
    },
)
def natural_ch4_emissions():
    """
    Flux of methane from anaerobic respiration in the biosphere, in Mtons CH4/year.
    """
    return flux_biosphere_to_ch4() * unit_conversion_ch4_c() * unit_conversion_mt_gt()


@component.add(
    name="PREIND_C_IN_MIXED_LAYER",
    units="Gt",
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_preind_c_in_mixed_layer": 1},
    other_deps={
        "_initial_preind_c_in_mixed_layer": {
            "initial": {"preind_ocean_c_per_meter": 1, "mixed_depth": 1},
            "step": {},
        }
    },
)
def preind_c_in_mixed_layer():
    """
    Initial carbon concentration of mixed ocean layer.
    """
    return _initial_preind_c_in_mixed_layer()


_initial_preind_c_in_mixed_layer = Initial(
    lambda: preind_ocean_c_per_meter() * mixed_depth(),
    "_initial_preind_c_in_mixed_layer",
)


@component.add(
    name="SENSITIVITY_OF_PCO2_DIC_TO_TEMPERATURE",
    units="1/DegreesC",
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_sensitivity_of_pco2_dic_to_temperature": 1},
    other_deps={
        "_initial_sensitivity_of_pco2_dic_to_temperature": {
            "initial": {
                "sensitivity_of_c_uptake_to_temperature": 1,
                "sensitivity_of_pco2_dic_to_temperature_mean": 1,
            },
            "step": {},
        }
    },
)
def sensitivity_of_pco2_dic_to_temperature():
    """
    Sensitivity of pCO2 of dissolved inorganic carbon in ocean to temperature.
    """
    return _initial_sensitivity_of_pco2_dic_to_temperature()


_initial_sensitivity_of_pco2_dic_to_temperature = Initial(
    lambda: sensitivity_of_c_uptake_to_temperature()
    * sensitivity_of_pco2_dic_to_temperature_mean(),
    "_initial_sensitivity_of_pco2_dic_to_temperature",
)


@component.add(
    name="STRENGTH_OF_TEMP_EFFECT_ON_C_FLUX_TO_LAND",
    units="1/DegreesC",
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_strength_of_temp_effect_on_c_flux_to_land": 1},
    other_deps={
        "_initial_strength_of_temp_effect_on_c_flux_to_land": {
            "initial": {
                "sensitivity_of_c_uptake_to_temperature": 1,
                "strength_of_temp_effect_on_land_c_flux_mean": 1,
            },
            "step": {},
        }
    },
)
def strength_of_temp_effect_on_c_flux_to_land():
    """
    Strength of temperature effect on C flux to the land.
    """
    return _initial_strength_of_temp_effect_on_c_flux_to_land()


_initial_strength_of_temp_effect_on_c_flux_to_land = Initial(
    lambda: sensitivity_of_c_uptake_to_temperature()
    * strength_of_temp_effect_on_land_c_flux_mean(),
    "_initial_strength_of_temp_effect_on_c_flux_to_land",
)


@component.add(
    name="total_C_anthro_emissions",
    units="Gt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_co2_emission_world": 1, "unit_conversion_c_co2": 1},
)
def total_c_anthro_emissions():
    """
    Total annual CO2 emissions converted to GtonsC/year.
    """
    return total_co2_emission_world() * unit_conversion_c_co2()


@component.add(
    name="total_CO2_emission_world",
    units="Gt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_co2_emissions": 1},
)
def total_co2_emission_world():
    """
    Total global CO2 emissions.
    """
    return sum(
        total_co2_emissions().rename({"REGIONS_9_I": "REGIONS_9_I!"}),
        dim=["REGIONS_9_I!"],
    )
