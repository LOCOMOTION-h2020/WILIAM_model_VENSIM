"""
Module climate.impacts.ph_ocean
Translated using PySD version 3.10.0
"""


@component.add(
    name="aragonite_saturation",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "aragonite_saturation_constant_1": 1,
        "ph_ocean": 2,
        "aragonite_saturation_constant_2": 1,
    },
)
def aragonite_saturation():
    """
    Calculated Ocean Aragonite saturation.
    """
    return (
        aragonite_saturation_constant_1() * ph_ocean() ** 2
        - aragonite_saturation_constant_2() * ph_ocean()
        + 213.544
    )


@component.add(
    name="delta_pH_from_2000",
    units="pH",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "ph_ocean": 1, "ph_in_2000": 1},
)
def delta_ph_from_2000():
    """
    Change in pH from the pH in 2000.
    """
    return if_then_else(
        time() < 2000, lambda: np.nan, lambda: ph_ocean() - ph_in_2000()
    )


@component.add(
    name="OCEANIC_PH_THRESHOLD",
    units="pH",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "ph_constant_1": 1,
        "ph_constant_2": 1,
        "ppm_to_calculate_oceanic_ph_threshold": 3,
        "ph_constant_3": 1,
        "ph_constant_4": 1,
    },
)
def oceanic_ph_threshold():
    """
    Coral Reefs Under Rapid Climate Change and Ocean Acidification O. Hoegh-Guldberg, et al. Science 318, 1737 (2007)
    """
    return (
        ph_constant_1()
        - ph_constant_2() * ppm_to_calculate_oceanic_ph_threshold()
        + ph_constant_3() * ppm_to_calculate_oceanic_ph_threshold() ** 2
        - ph_constant_4() * ppm_to_calculate_oceanic_ph_threshold() ** 3
    )


@component.add(
    name="pH_in_2000",
    units="pH",
    comp_type="Stateful",
    comp_subtype="SampleIfTrue",
    depends_on={"_sampleiftrue_ph_in_2000": 1},
    other_deps={
        "_sampleiftrue_ph_in_2000": {
            "initial": {"ph_ocean": 1},
            "step": {"time": 1, "ph_ocean": 1},
        }
    },
)
def ph_in_2000():
    """
    pH in 2000.
    """
    return _sampleiftrue_ph_in_2000()


_sampleiftrue_ph_in_2000 = SampleIfTrue(
    lambda: time() <= 2000,
    lambda: ph_ocean(),
    lambda: ph_ocean(),
    "_sampleiftrue_ph_in_2000",
)


@component.add(
    name="pH_ocean",
    units="pH",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "ph_constant_1": 1,
        "ph_constant_2": 1,
        "atmospheric_concentrations_co2": 3,
        "ph_constant_3": 1,
        "ph_constant_4": 1,
    },
)
def ph_ocean():
    """
    pH of the ocean. Bernie, D., J. Lowe, T. Tyrrell, and O. Legge (2010), Influence of mitigation policy on ocean acidification, Geophys. Res. Lett., 37, L15704, doi:10.1029/2010GL043181.
    """
    return (
        ph_constant_1()
        - ph_constant_2() * atmospheric_concentrations_co2()
        + ph_constant_3() * atmospheric_concentrations_co2() ** 2
        - ph_constant_4() * atmospheric_concentrations_co2() ** 3
    )
