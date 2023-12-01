"""
Module climate.auxiliary_outputs_and_indicators
Translated using PySD version 3.10.0
"""


@component.add(
    name="annual_variation_CO2_emissions",
    units="Gt/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_co2_emissions": 2, "delayed_total_co2_emissions": 4},
)
def annual_variation_co2_emissions():
    """
    Annual variation of the CO2 emissions. Europe has the same variation in all the countries to account for the same effect
    """
    value = xr.DataArray(
        np.nan, {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]}, ["REGIONS_35_I"]
    )
    value.loc[_subscript_dict["REGIONS_8_I"]] = (
        (
            total_co2_emissions()
            .loc[_subscript_dict["REGIONS_8_I"]]
            .rename({"REGIONS_9_I": "REGIONS_8_I"})
            - delayed_total_co2_emissions()
            .loc[_subscript_dict["REGIONS_8_I"]]
            .rename({"REGIONS_9_I": "REGIONS_8_I"})
        )
        / delayed_total_co2_emissions()
        .loc[_subscript_dict["REGIONS_8_I"]]
        .rename({"REGIONS_9_I": "REGIONS_8_I"})
        * 100
    ).values
    value.loc[_subscript_dict["REGIONS_EU27_I"]] = (
        (
            float(total_co2_emissions().loc["EU27"])
            - float(delayed_total_co2_emissions().loc["EU27"])
        )
        / float(delayed_total_co2_emissions().loc["EU27"])
        * 100
    )
    return value


@component.add(
    name="delayed_total_CO2_emissions",
    units="Gt/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Stateful",
    comp_subtype="Delay",
    depends_on={"_delay_delayed_total_co2_emissions": 1},
    other_deps={
        "_delay_delayed_total_co2_emissions": {
            "initial": {"total_co2_emissions": 1},
            "step": {"total_co2_emissions": 1},
        }
    },
)
def delayed_total_co2_emissions():
    """
    Delayed one year the total carbon emissions
    """
    return _delay_delayed_total_co2_emissions()


_delay_delayed_total_co2_emissions = Delay(
    lambda: total_co2_emissions(),
    lambda: xr.DataArray(
        1, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
    ),
    lambda: total_co2_emissions(),
    lambda: 1,
    time_step,
    "_delay_delayed_total_co2_emissions",
)
