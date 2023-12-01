"""
Module climate.impacts.temperature_change
Translated using PySD version 3.10.0
"""


@component.add(
    name="ATM_AND_UPPER_OCEAN_HEAT_CAP",
    units="w*Year/(m*m*DegreesC)",
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_atm_and_upper_ocean_heat_cap": 1},
    other_deps={
        "_initial_atm_and_upper_ocean_heat_cap": {
            "initial": {
                "upper_layer_volume_vu": 1,
                "volumetric_heat_capacity": 1,
                "global_surface_area": 1,
            },
            "step": {},
        }
    },
)
def atm_and_upper_ocean_heat_cap():
    """
    Volumetric heat capacity for the land, atmosphere,and upper ocean layer, i.e., upper layer heat capacity Ru.
    """
    return _initial_atm_and_upper_ocean_heat_cap()


_initial_atm_and_upper_ocean_heat_cap = Initial(
    lambda: upper_layer_volume_vu()
    * volumetric_heat_capacity()
    / global_surface_area(),
    "_initial_atm_and_upper_ocean_heat_cap",
)


@component.add(
    name="average_temperature_change_from_2015",
    units="DegreesC",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 2,
        "nvs_1975_1995_temp_change_lt": 1,
        "temperature_change": 2,
        "delayed_20_temperature_change_from_2015": 1,
    },
)
def average_temperature_change_from_2015():
    """
    Average temperature change from 2015 (set by default to 20 years, to change the period the code must be changed).
    """
    return if_then_else(
        time() < 2015,
        lambda: (nvs_1975_1995_temp_change_lt(time() - 20) + temperature_change()) / 2,
        lambda: (delayed_20_temperature_change_from_2015() + temperature_change()) / 2,
    )


@component.add(
    name="CLIMATE_FEEDBACK_PARAM",
    units="w/(m*m*DegreesC)",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"double_co2_forcing": 1, "ecs": 1},
)
def climate_feedback_param():
    """
    Climate Feedback Parameter - determines feedback effect from temperature increase.
    """
    return double_co2_forcing() / ecs()


@component.add(
    name="DEEP_OCEAN_HEAT_CAP",
    units="w*Year/(m*m)/DegreesC",
    subscripts=["LAYERS_I"],
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_deep_ocean_heat_cap": 1},
    other_deps={
        "_initial_deep_ocean_heat_cap": {
            "initial": {
                "lower_layer_volume_vu": 1,
                "volumetric_heat_capacity": 1,
                "global_surface_area": 1,
            },
            "step": {},
        }
    },
)
def deep_ocean_heat_cap():
    """
    Volumetric heat capacity for the deep ocean by layer, i.e., lower layer heat capacity Ru.
    """
    return _initial_deep_ocean_heat_cap()


_initial_deep_ocean_heat_cap = Initial(
    lambda: lower_layer_volume_vu()
    * volumetric_heat_capacity()
    / global_surface_area(),
    "_initial_deep_ocean_heat_cap",
)


@component.add(
    name="delayed_20_temperature_change_from_2015",
    units="DegreesC",
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_20_temperature_change_from_2015": 1},
    other_deps={
        "_delayfixed_delayed_20_temperature_change_from_2015": {
            "initial": {"temperature_change_in_1995": 1},
            "step": {"temperature_change": 1},
        }
    },
)
def delayed_20_temperature_change_from_2015():
    """
    Temperature change delayed 20 years.
    """
    return _delayfixed_delayed_20_temperature_change_from_2015()


_delayfixed_delayed_20_temperature_change_from_2015 = DelayFixed(
    lambda: temperature_change(),
    lambda: 20,
    lambda: temperature_change_in_1995(),
    time_step,
    "_delayfixed_delayed_20_temperature_change_from_2015",
)


@component.add(
    name="DOUBLE_CO2_FORCING",
    units="w/(m*m)",
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_double_co2_forcing": 1},
    other_deps={
        "_initial_double_co2_forcing": {
            "initial": {"co2_rad_force_coefficient": 1},
            "step": {},
        }
    },
)
def double_co2_forcing():
    """
    Forcing due to double concentration of Carbon.
    """
    return _initial_double_co2_forcing()


_initial_double_co2_forcing = Initial(
    lambda: co2_rad_force_coefficient() * np.log(2), "_initial_double_co2_forcing"
)


@component.add(
    name="ECS",
    units="DegreesC",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_model_explorer": 1,
        "model_explorer_climate_sensitivity": 1,
        "time": 1,
        "selection_ecs_input_method": 1,
        "climate_sensitivity_sp": 1,
        "probabilistic_ecs": 1,
    },
)
def ecs():
    """
    Equilibrium Climate Sensitivity.
    """
    return if_then_else(
        switch_model_explorer() == 1,
        lambda: model_explorer_climate_sensitivity(),
        lambda: if_then_else(
            time() < 2015,
            lambda: 3,
            lambda: if_then_else(
                selection_ecs_input_method() == 0,
                lambda: climate_sensitivity_sp(),
                lambda: probabilistic_ecs(),
            ),
        ),
    )


@component.add(
    name="feedback_cooling",
    units="w/(m*m)",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"temperature_change": 1, "climate_feedback_param": 1},
)
def feedback_cooling():
    """
    Feedback cooling of atmosphere/upper ocean system due to blackbody radiation. [Cowles, pg. 27]
    """
    return temperature_change() * climate_feedback_param()


@component.add(
    name="heat_in_atmosphere_and_upper_ocean",
    units="w*Year/(m*m)",
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_heat_in_atmosphere_and_upper_ocean": 1},
    other_deps={
        "_integ_heat_in_atmosphere_and_upper_ocean": {
            "initial": {"init_atmos_uocean_temp": 1, "atm_and_upper_ocean_heat_cap": 1},
            "step": {
                "effective_radiative_forcing": 1,
                "feedback_cooling": 1,
                "heat_transfer": 1,
            },
        }
    },
)
def heat_in_atmosphere_and_upper_ocean():
    """
    Heat of the Atmosphere and Upper Ocean
    """
    return _integ_heat_in_atmosphere_and_upper_ocean()


_integ_heat_in_atmosphere_and_upper_ocean = Integ(
    lambda: effective_radiative_forcing()
    - feedback_cooling()
    - float(heat_transfer().loc["Layer1"]),
    lambda: init_atmos_uocean_temp() * atm_and_upper_ocean_heat_cap(),
    "_integ_heat_in_atmosphere_and_upper_ocean",
)


@component.add(
    name="heat_in_deep_ocean",
    units="w*Year/(m*m)",
    subscripts=["LAYERS_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_heat_in_deep_ocean": 1, "_integ_heat_in_deep_ocean_1": 1},
    other_deps={
        "_integ_heat_in_deep_ocean": {
            "initial": {"init_deep_ocean_temp": 1, "deep_ocean_heat_cap": 1},
            "step": {"heat_transfer": 2},
        },
        "_integ_heat_in_deep_ocean_1": {
            "initial": {"init_deep_ocean_temp": 1, "deep_ocean_heat_cap": 1},
            "step": {"heat_transfer": 1},
        },
    },
)
def heat_in_deep_ocean():
    """
    Heat content of each layer of the deep ocean.
    """
    value = xr.DataArray(
        np.nan, {"LAYERS_I": _subscript_dict["LAYERS_I"]}, ["LAYERS_I"]
    )
    value.loc[_subscript_dict["upper"]] = _integ_heat_in_deep_ocean().values
    value.loc[["Layer4"]] = _integ_heat_in_deep_ocean_1().values
    return value


_integ_heat_in_deep_ocean = Integ(
    lambda: heat_transfer().loc[_subscript_dict["upper"]].rename({"LAYERS_I": "upper"})
    - xr.DataArray(
        heat_transfer()
        .loc[_subscript_dict["lower"]]
        .rename({"LAYERS_I": "lower"})
        .values,
        {"upper": _subscript_dict["upper"]},
        ["upper"],
    ),
    lambda: init_deep_ocean_temp()
    .loc[_subscript_dict["upper"]]
    .rename({"LAYERS_I": "upper"})
    * deep_ocean_heat_cap().loc[_subscript_dict["upper"]].rename({"LAYERS_I": "upper"}),
    "_integ_heat_in_deep_ocean",
)

_integ_heat_in_deep_ocean_1 = Integ(
    lambda: xr.DataArray(
        float(heat_transfer().loc["Layer4"]),
        {"bottom": _subscript_dict["bottom"]},
        ["bottom"],
    ),
    lambda: xr.DataArray(
        float(init_deep_ocean_temp().loc["Layer4"])
        * float(deep_ocean_heat_cap().loc["Layer4"]),
        {"bottom": _subscript_dict["bottom"]},
        ["bottom"],
    ),
    "_integ_heat_in_deep_ocean_1",
)


@component.add(
    name="heat_transfer",
    units="w/(m*m)",
    subscripts=["LAYERS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "temperature_change": 1,
        "relative_deep_ocean_temp": 3,
        "heat_transfer_coeff": 2,
        "mean_depth_of_adjacent_layers": 2,
    },
)
def heat_transfer():
    """
    Heat Transfer from the Atmosphere & Upper Ocean to the Deep Ocean
    """
    value = xr.DataArray(
        np.nan, {"LAYERS_I": _subscript_dict["LAYERS_I"]}, ["LAYERS_I"]
    )
    value.loc[["Layer1"]] = (
        (temperature_change() - float(relative_deep_ocean_temp().loc["Layer1"]))
        * heat_transfer_coeff()
        / float(mean_depth_of_adjacent_layers().loc["Layer1"])
    )
    value.loc[_subscript_dict["lower"]] = (
        (
            xr.DataArray(
                relative_deep_ocean_temp()
                .loc[_subscript_dict["upper"]]
                .rename({"LAYERS_I": "upper"})
                .values,
                {"lower": _subscript_dict["lower"]},
                ["lower"],
            )
            - relative_deep_ocean_temp()
            .loc[_subscript_dict["lower"]]
            .rename({"LAYERS_I": "lower"})
        )
        * heat_transfer_coeff()
        / mean_depth_of_adjacent_layers()
        .loc[_subscript_dict["lower"]]
        .rename({"LAYERS_I": "lower"})
    ).values
    return value


@component.add(
    name="HEAT_TRANSFER_COEFF",
    units="w/(m*m)/(DegreesC/m)",
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_heat_transfer_coeff": 1},
    other_deps={
        "_initial_heat_transfer_coeff": {
            "initial": {
                "heat_transfer_rate": 1,
                "mean_depth_of_adjacent_layers": 1,
                "eddy_diff_coeff": 1,
                "eddy_diff_mean": 1,
                "heat_diffusion_covar": 2,
            },
            "step": {},
        }
    },
)
def heat_transfer_coeff():
    """
    The ratio of the actual to the mean of the heat transfer coefficient, which controls the movement of heat through the climate sector, is a function of the ratio of the actual to the mean of the eddy diffusion coefficient, which controls the movement of carbon through the deep ocean.
    """
    return _initial_heat_transfer_coeff()


_initial_heat_transfer_coeff = Initial(
    lambda: (
        heat_transfer_rate() * float(mean_depth_of_adjacent_layers().loc["Layer1"])
    )
    * (
        heat_diffusion_covar() * (eddy_diff_coeff() / eddy_diff_mean())
        + (1 - heat_diffusion_covar())
    ),
    "_initial_heat_transfer_coeff",
)


@component.add(
    name="LOWER_LAYER_VOLUME_VU",
    units="m*m*m",
    subscripts=["LAYERS_I"],
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_lower_layer_volume_vu": 1},
    other_deps={
        "_initial_lower_layer_volume_vu": {
            "initial": {
                "global_surface_area": 1,
                "land_area_fraction": 1,
                "layer_depth": 1,
            },
            "step": {},
        }
    },
)
def lower_layer_volume_vu():
    """
    Water equivalent volume of the deep ocean by layer.
    """
    return _initial_lower_layer_volume_vu()


_initial_lower_layer_volume_vu = Initial(
    lambda: global_surface_area() * (1 - land_area_fraction()) * layer_depth(),
    "_initial_lower_layer_volume_vu",
)


@component.add(
    name="PROBABILISTIC_ECS",
    units="DegreesC",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"sample_for_monte_carlo_ecs": 1, "ecdf_ecs_ar5_lt": 1},
)
def probabilistic_ecs():
    """
    Probabilistic ECS.
    """
    return ecdf_ecs_ar5_lt(sample_for_monte_carlo_ecs())


@component.add(
    name="relative_deep_ocean_temp",
    units="DegreesC",
    subscripts=["LAYERS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"heat_in_deep_ocean": 1, "deep_ocean_heat_cap": 1},
)
def relative_deep_ocean_temp():
    """
    Temperature of each layer of the deep ocean.
    """
    return heat_in_deep_ocean() / deep_ocean_heat_cap()


@component.add(
    name="SEC_PER_YR",
    units="s/Year",
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_sec_per_yr": 1},
    other_deps={
        "_initial_sec_per_yr": {
            "initial": {
                "unit_conversion_days_year": 1,
                "unit_conversion_seconds_day": 1,
            },
            "step": {},
        }
    },
)
def sec_per_yr():
    """
    Converts seconds to years
    """
    return _initial_sec_per_yr()


_initial_sec_per_yr = Initial(
    lambda: unit_conversion_days_year() * unit_conversion_seconds_day(),
    "_initial_sec_per_yr",
)


@component.add(
    name="temperature_change",
    units="DegreesC",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "heat_in_atmosphere_and_upper_ocean": 1,
        "atm_and_upper_ocean_heat_cap": 1,
    },
)
def temperature_change():
    """
    Temperature of the Atmosphere and Upper Ocean, relative to preindustrial reference period
    """
    return heat_in_atmosphere_and_upper_ocean() / atm_and_upper_ocean_heat_cap()


@component.add(
    name="UPPER_LAYER_VOLUME_VU",
    units="m*m*m",
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_upper_layer_volume_vu": 1},
    other_deps={
        "_initial_upper_layer_volume_vu": {
            "initial": {
                "global_surface_area": 1,
                "land_area_fraction": 2,
                "land_thickness": 1,
                "mixed_depth": 1,
            },
            "step": {},
        }
    },
)
def upper_layer_volume_vu():
    """
    Water equivalent volume of the upper box, which is a weighted combination of land, atmosphere,and upper ocean volumes.
    """
    return _initial_upper_layer_volume_vu()


_initial_upper_layer_volume_vu = Initial(
    lambda: global_surface_area()
    * (
        land_area_fraction() * land_thickness()
        + (1 - land_area_fraction()) * mixed_depth()
    ),
    "_initial_upper_layer_volume_vu",
)


@component.add(
    name="VOLUMETRIC_HEAT_CAPACITY",
    units="w*Year/(m*m*m*DegreesC)",
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_volumetric_heat_capacity": 1},
    other_deps={
        "_initial_volumetric_heat_capacity": {
            "initial": {
                "specific_heat_capacity_water": 1,
                "unit_conversion_w_j_s": 1,
                "sec_per_yr": 1,
                "water_density": 1,
            },
            "step": {},
        }
    },
)
def volumetric_heat_capacity():
    """
    Volumetric heat capacity of water, i.e., amount of heat in watt*year required to raise 1 cubic meter of water by one degree C.
    """
    return _initial_volumetric_heat_capacity()


_initial_volumetric_heat_capacity = Initial(
    lambda: specific_heat_capacity_water()
    * unit_conversion_w_j_s()
    / sec_per_yr()
    * water_density(),
    "_initial_volumetric_heat_capacity",
)
