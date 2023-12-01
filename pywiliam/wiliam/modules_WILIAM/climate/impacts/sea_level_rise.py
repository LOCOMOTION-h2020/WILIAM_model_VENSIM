"""
Module climate.impacts.sea_level_rise
Translated using PySD version 3.10.0
"""


@component.add(
    name="adjusted_sensitivity_of_sea_level_rise_to_temperature",
    units="mm/(Year*DegreesC)",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "sensitivity_of_sea_level_rise_to_temperature": 1,
        "time": 1,
        "sea_level_sensitivity_from_ice_sheet_melting": 1,
        "slr_ice_sheet_melting_year": 1,
    },
)
def adjusted_sensitivity_of_sea_level_rise_to_temperature():
    """
    The sensitivity of SLR to temperature after 2000 can be adjusted above or below the V&R estimate of 5.6 mm/year/degree C. The adjustment is multiplicative on top of the base value.
    """
    return sensitivity_of_sea_level_rise_to_temperature() * (
        1
        + step(
            __data["time"],
            sea_level_sensitivity_from_ice_sheet_melting(),
            slr_ice_sheet_melting_year(),
        )
    )


@component.add(
    name="adjusted_temperature_change_from_preindustrial_for_SLR_estimation",
    units="DegreesC",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"temperature_change": 1, "temp_adjustment_for_slr": 1},
)
def adjusted_temperature_change_from_preindustrial_for_slr_estimation():
    """
    Temperature change from preindustrial levels adjusted to the model generated average global surface temperature that is used in the calculation of sea level rise from the Vermeer and Rahmstorf (2009) model.
    """
    return temperature_change() - temp_adjustment_for_slr()


@component.add(
    name="Change_in_Relative_Temperature",
    units="DegreesC/Year",
    comp_type="Stateful",
    comp_subtype="Smooth",
    depends_on={
        "adjusted_temperature_change_from_preindustrial_for_slr_estimation": 1,
        "_smooth_change_in_relative_temperature": 1,
        "time_step": 1,
    },
    other_deps={
        "_smooth_change_in_relative_temperature": {
            "initial": {
                "adjusted_temperature_change_from_preindustrial_for_slr_estimation": 1,
                "time_step": 1,
            },
            "step": {
                "adjusted_temperature_change_from_preindustrial_for_slr_estimation": 1,
                "time_step": 1,
            },
        }
    },
)
def change_in_relative_temperature():
    """
    approximates dT/dt
    """
    return (
        adjusted_temperature_change_from_preindustrial_for_slr_estimation()
        - _smooth_change_in_relative_temperature()
    ) / time_step()


_smooth_change_in_relative_temperature = Smooth(
    lambda: adjusted_temperature_change_from_preindustrial_for_slr_estimation(),
    lambda: time_step(),
    lambda: adjusted_temperature_change_from_preindustrial_for_slr_estimation(),
    lambda: 1,
    "_smooth_change_in_relative_temperature",
)


@component.add(
    name="change_in_sea_level",
    units="mm/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"equilibrium_change_in_sea_level": 1, "instant_change_in_sea_level": 1},
)
def change_in_sea_level():
    """
    Change in Sea Level Rise
    """
    return equilibrium_change_in_sea_level() + instant_change_in_sea_level()


@component.add(
    name="check_historic_sea_level",
    units="percent",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 2, "historic_sea_level_rise": 2, "sea_level_rise": 1},
)
def check_historic_sea_level():
    """
    Verification of historic Sea-level.
    """
    return if_then_else(
        np.logical_and(time() < 2018, time() > 2000),
        lambda: (sea_level_rise() - historic_sea_level_rise())
        * 100
        / historic_sea_level_rise(),
        lambda: 0,
    )


@component.add(
    name="check_shares_between_two_methods_of_calculation_of_sea_level_rise",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"sea_level_rise_from_mm_to_m": 1, "sea_level_rise_for_world": 1},
)
def check_shares_between_two_methods_of_calculation_of_sea_level_rise():
    """
    shares between Mohamed and Noelia/David calculations
    """
    return zidz(sea_level_rise_from_mm_to_m(), sea_level_rise_for_world())


@component.add(
    name="equilibrium_change_in_sea_level",
    units="mm/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "adjusted_sensitivity_of_sea_level_rise_to_temperature": 1,
        "adjusted_temperature_change_from_preindustrial_for_slr_estimation": 1,
        "reference_temperature": 1,
    },
)
def equilibrium_change_in_sea_level():
    """
    Vermeer & Rahmstorf (2009) sea level rise rate (open loop approx to initial transient). Rahmstorf (2007) is recovered when Sensitivity of SLR rate to temp rate = W.
    """
    return adjusted_sensitivity_of_sea_level_rise_to_temperature() * (
        adjusted_temperature_change_from_preindustrial_for_slr_estimation()
        - reference_temperature()
    )


@component.add(
    name="instant_change_in_sea_level",
    units="mm/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "sensitivity_of_slr_rate_to_temp_rate": 1,
        "change_in_relative_temperature": 1,
    },
)
def instant_change_in_sea_level():
    """
    Vermeer & Rahmstorf (2009) instantaneous sea level rise rate on the time scales under consideration. Rahmstorf (2007) is recovered when Sensitivity of SLR rate to temp rate = W.
    """
    return sensitivity_of_slr_rate_to_temp_rate() * change_in_relative_temperature()


@component.add(
    name="sea_level_rise",
    units="mm",
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_sea_level_rise": 1},
    other_deps={
        "_integ_sea_level_rise": {
            "initial": {"initial_sea_level_rise_in_2005": 1},
            "step": {"change_in_sea_level": 1},
        }
    },
)
def sea_level_rise():
    """
    Estimated Sea Level Rise (from initial level) is the accumulation of the rate of sea level rise. Source: Rahmstorf, S. 2007. Science, 315, 368.
    """
    return _integ_sea_level_rise()


_integ_sea_level_rise = Integ(
    lambda: change_in_sea_level(),
    lambda: initial_sea_level_rise_in_2005(),
    "_integ_sea_level_rise",
)


@component.add(
    name="sea_level_rise_by_region",
    units="m",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "sea_level_rise_parameter_alpha": 1,
        "temperature_change": 1,
        "sea_level_rise_parameter_beta": 1,
        "vertical_land_movement": 1,
        "time": 1,
    },
)
def sea_level_rise_by_region():
    """
    sea level rise by region
    """
    return (
        sea_level_rise_parameter_alpha()
        + sea_level_rise_parameter_beta() * temperature_change()
        - vertical_land_movement()
    ) * (time() - 2000)


@component.add(
    name="sea_level_rise_for_world",
    units="m",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"sea_level_rise_by_region": 1},
)
def sea_level_rise_for_world():
    """
    sea level rise for world
    """
    return (
        sum(
            sea_level_rise_by_region().rename({"REGIONS_9_I": "REGIONS_9_I!"}),
            dim=["REGIONS_9_I!"],
        )
        / 9
    )


@component.add(
    name="sea_level_rise_from_2000",
    units="mm",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "slr_in_2000": 1, "sea_level_rise": 1},
)
def sea_level_rise_from_2000():
    """
    Sea Level Rise indexed to zero in the year 2000.
    """
    return if_then_else(
        time() < 2000, lambda: np.nan, lambda: sea_level_rise() - slr_in_2000()
    )


@component.add(
    name="sea_level_rise_from_mm_to_m",
    units="m",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"sea_level_rise": 1, "unit_conversion_m_mm": 1},
)
def sea_level_rise_from_mm_to_m():
    """
    Sea level rise from mm to m
    """
    return sea_level_rise() * unit_conversion_m_mm()


@component.add(
    name="SLR_in_2000",
    units="mm",
    comp_type="Stateful",
    comp_subtype="SampleIfTrue",
    depends_on={"_sampleiftrue_slr_in_2000": 1},
    other_deps={
        "_sampleiftrue_slr_in_2000": {
            "initial": {"sea_level_rise": 1},
            "step": {"time": 1, "sea_level_rise": 1},
        }
    },
)
def slr_in_2000():
    """
    Sea Level Rise in the year 2000.
    """
    return _sampleiftrue_slr_in_2000()


_sampleiftrue_slr_in_2000 = SampleIfTrue(
    lambda: time() <= 2000,
    lambda: sea_level_rise(),
    lambda: sea_level_rise(),
    "_sampleiftrue_slr_in_2000",
)
