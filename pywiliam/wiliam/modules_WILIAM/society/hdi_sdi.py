"""
Module society.hdi_sdi
Translated using PySD version 3.10.0
"""


@component.add(
    name="AO_SDI",
    units="1",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "world_material_footprint": 2,
        "pb_material_footprint": 2,
        "sdi_co2_emissions": 2,
        "pb_co2": 2,
    },
)
def ao_sdi():
    """
    AO parameter of the sustainable development index
    """
    return np.sqrt(
        if_then_else(
            world_material_footprint() / pb_material_footprint() < 1,
            lambda: 1,
            lambda: world_material_footprint() / pb_material_footprint(),
        )
        * if_then_else(
            sdi_co2_emissions() / pb_co2() < 1,
            lambda: 1,
            lambda: sdi_co2_emissions() / pb_co2(),
        )
    )


@component.add(
    name="ecological_impact_index",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ao_sdi": 3},
)
def ecological_impact_index():
    """
    Ecological impact index used to calculate the sustainable development index https://www.sustainabledevelopmentindex.org/methods
    """
    return if_then_else(
        ao_sdi() > 4,
        lambda: ao_sdi() - 2,
        lambda: 1 + (np.exp(ao_sdi()) - np.exp(1)) / (np.exp(4) - np.exp(1)),
    )


@component.add(
    name="gdp_per_capital_real_purchasing_parity_power",
    units="dollars_2017PPP/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "gross_domestic_product_real_supply_side": 1,
        "population_35_regions": 1,
        "conversion_to_purchasing_parity_power_mp": 1,
        "matrix_unit_prefixes": 1,
    },
)
def gdp_per_capital_real_purchasing_parity_power():
    """
    The transformation has been done maintaining the ratio between real gdp (2015) and real gdp ppp (2017) of 2015.
    """
    return (
        zidz(gross_domestic_product_real_supply_side(), population_35_regions())
        * conversion_to_purchasing_parity_power_mp()
        * float(matrix_unit_prefixes().loc["mega", "BASE_UNIT"])
    )


@component.add(
    name="HDI",
    units="DMNL",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "knowledge_index": 1,
        "long_and_healthy_life_index": 1,
        "standard_of_living_index": 1,
    },
)
def hdi():
    """
    Human Development Index. Formula proposed by UNDP and revisable in technical-notes-calculating-human-development-indices.pdf (undp.org)
    """
    return (
        knowledge_index() * long_and_healthy_life_index() * standard_of_living_index()
    ) ** (1 / 3)


@component.add(
    name="HDI_9R",
    units="DMNL",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"hdi": 1, "hdi_eu_27": 1},
)
def hdi_9r():
    """
    HDI_9R
    """
    value = xr.DataArray(
        np.nan, {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, ["REGIONS_9_I"]
    )
    value.loc[_subscript_dict["REGIONS_8_I"]] = (
        hdi()
        .loc[_subscript_dict["REGIONS_8_I"]]
        .rename({"REGIONS_35_I": "REGIONS_8_I"})
        .values
    )
    value.loc[["EU27"]] = hdi_eu_27()
    return value


@component.add(
    name="HDI_EU_27",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"hdi": 1, "population_35_regions": 2},
)
def hdi_eu_27():
    return zidz(
        sum(
            hdi()
            .loc[_subscript_dict["REGIONS_EU27_I"]]
            .rename({"REGIONS_35_I": "REGIONS_EU27_I!"})
            * population_35_regions()
            .loc[_subscript_dict["REGIONS_EU27_I"]]
            .rename({"REGIONS_35_I": "REGIONS_EU27_I!"}),
            dim=["REGIONS_EU27_I!"],
        ),
        sum(
            population_35_regions()
            .loc[_subscript_dict["REGIONS_EU27_I"]]
            .rename({"REGIONS_35_I": "REGIONS_EU27_I!"}),
            dim=["REGIONS_EU27_I!"],
        ),
    )


@component.add(
    name="HDI_world",
    units="1",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"hdi_9r": 1, "population_9_regions": 2},
)
def hdi_world():
    """
    Human development index (HDI) of the world
    """
    return zidz(
        sum(
            hdi_9r().rename({"REGIONS_9_I": "REGIONS_9_I!"})
            * population_9_regions().rename({"REGIONS_9_I": "REGIONS_9_I!"}),
            dim=["REGIONS_9_I!"],
        ),
        sum(
            population_9_regions().rename({"REGIONS_9_I": "REGIONS_9_I!"}),
            dim=["REGIONS_9_I!"],
        ),
    )


@component.add(
    name="knowledge_index",
    units="DMNL",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"means_years_of_schooling": 1, "schooling_life_expectancy": 1},
)
def knowledge_index():
    """
    Formula proposed by UNDP and revisable in technical-notes-calculating-human-development-indices.pdf (undp.org)
    """
    return zidz(means_years_of_schooling() / 15 + schooling_life_expectancy() / 18, 2)


@component.add(
    name="long_and_healthy_life_index",
    units="DMNL",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"life_expectancy_at_birth": 2},
)
def long_and_healthy_life_index():
    """
    Formula proposed by UNDP and revisable in technical-notes-calculating-human-development-indices.pdf (undp.org)
    """
    return zidz(
        (
            life_expectancy_at_birth().loc[:, "FEMALE"].reset_coords(drop=True)
            + life_expectancy_at_birth().loc[:, "MALE"].reset_coords(drop=True)
        )
        / 2
        - 20,
        85 - 20,
    )


@component.add(
    name="means_years_of_schooling",
    units="Years",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "percentage_of_workforce_in_each_educational_level": 3,
        "years_of_education_corresponding_to_each_level_for_means_years_of_schooling_mp": 3,
    },
)
def means_years_of_schooling():
    """
    The years for calculating mean years of schooling are different from the years for calculating schooling life expectancy because in general the levels for reaching certain levels of schooling were lower in the past than they are today. It should be noted that the mean years of schooling takes data from the working age population (there is a population that studied decades ago), while schooling life expectancy takes current enrollments, which in the model is approximated by the percentages of the population that becomes part of the working age population.
    """
    return (
        sum(
            percentage_of_workforce_in_each_educational_level()
            .loc[:, "LOW_EDUCATION", :]
            .reset_coords(drop=True)
            .rename({"SEX_I": "SEX_I!"}),
            dim=["SEX_I!"],
        )
        * float(
            years_of_education_corresponding_to_each_level_for_means_years_of_schooling_mp().loc[
                "LOW_EDUCATION"
            ]
        )
        + sum(
            percentage_of_workforce_in_each_educational_level()
            .loc[:, "MEDIUM_EDUCATION", :]
            .reset_coords(drop=True)
            .rename({"SEX_I": "SEX_I!"}),
            dim=["SEX_I!"],
        )
        * float(
            years_of_education_corresponding_to_each_level_for_means_years_of_schooling_mp().loc[
                "MEDIUM_EDUCATION"
            ]
        )
        + sum(
            percentage_of_workforce_in_each_educational_level()
            .loc[:, "HIGH_EDUCATION", :]
            .reset_coords(drop=True)
            .rename({"SEX_I": "SEX_I!"}),
            dim=["SEX_I!"],
        )
        * float(
            years_of_education_corresponding_to_each_level_for_means_years_of_schooling_mp().loc[
                "HIGH_EDUCATION"
            ]
        )
    ) / 200


@component.add(
    name="PB_CO2", units="t/(Year*person)", comp_type="Constant", comp_subtype="Normal"
)
def pb_co2():
    """
    Reference: 2015. Jason Hickel, The sustainable development index: Measuring the ecological efficiency of human development in the anthropocene, Ecological Economics, Volume 167, 2020, 106331, ISSN 0921-8009, https://doi.org/10.1016/j.ecolecon.2019.05.011.
    """
    return 7.91


@component.add(
    name="PB_MATERIAL_FOOTPRINT",
    units="t/(Year*person)",
    comp_type="Constant",
    comp_subtype="Normal",
)
def pb_material_footprint():
    """
    Reference: 2015. Jason Hickel, The sustainable development index: Measuring the ecological efficiency of human development in the anthropocene, Ecological Economics, Volume 167, 2020, 106331, ISSN 0921-8009, https://doi.org/10.1016/j.ecolecon.2019.05.011.
    """
    return 5.09


@component.add(
    name="schooling_life_expectancy",
    units="Years",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "percentage_of_new_workforce_in_each_educational_level": 3,
        "years_of_education_corresponding_to_each_level_for_schooling_life_expectancy_mp": 3,
    },
)
def schooling_life_expectancy():
    """
    The years for calculating mean years of schooling are different from the years for calculating schooling life expectancy because in general the levels for reaching certain levels of schooling were lower in the past than they are today. It should be noted that the mean years of schooling takes data from the working age population (there is a population that studied decades ago), while schooling life expectancy takes current enrollments, which in the model is approximated by the percentages of the population that becomes part of the working age population.
    """
    return (
        sum(
            percentage_of_new_workforce_in_each_educational_level()
            .loc[:, "LOW_EDUCATION", :]
            .reset_coords(drop=True)
            .rename({"SEX_I": "SEX_I!"}),
            dim=["SEX_I!"],
        )
        * float(
            years_of_education_corresponding_to_each_level_for_schooling_life_expectancy_mp().loc[
                "LOW_EDUCATION"
            ]
        )
        + sum(
            percentage_of_new_workforce_in_each_educational_level()
            .loc[:, "MEDIUM_EDUCATION", :]
            .reset_coords(drop=True)
            .rename({"SEX_I": "SEX_I!"}),
            dim=["SEX_I!"],
        )
        * float(
            years_of_education_corresponding_to_each_level_for_schooling_life_expectancy_mp().loc[
                "MEDIUM_EDUCATION"
            ]
        )
        + sum(
            percentage_of_new_workforce_in_each_educational_level()
            .loc[:, "HIGH_EDUCATION", :]
            .reset_coords(drop=True)
            .rename({"SEX_I": "SEX_I!"}),
            dim=["SEX_I!"],
        )
        * float(
            years_of_education_corresponding_to_each_level_for_schooling_life_expectancy_mp().loc[
                "HIGH_EDUCATION"
            ]
        )
    ) / 200


@component.add(
    name="SDI",
    units="1",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"hdi_world": 1, "ecological_impact_index": 1},
)
def sdi():
    """
    Sustainable development index (SDI). Source: https://www.sustainabledevelopmentindex.org/
    """
    return hdi_world() / ecological_impact_index()


@component.add(
    name="SDI_CO2_emissions",
    units="t/(Year*person)",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "total_co2_energy_emissions_9r": 1,
        "world_population": 1,
        "unit_conversion_t_gt": 1,
    },
)
def sdi_co2_emissions():
    """
    Proxy of CO2 emissions to calculate the sustainable development index (SDI)
    """
    return (
        sum(
            total_co2_energy_emissions_9r().rename({"REGIONS_9_I": "REGIONS_9_I!"}),
            dim=["REGIONS_9_I!"],
        )
        / world_population()
        * unit_conversion_t_gt()
    )


@component.add(
    name="standard_of_living_index",
    units="DMNL",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"gdp_per_capital_real_purchasing_parity_power": 2},
)
def standard_of_living_index():
    """
    Formula proposed by UNDP and revisable in technical-notes-calculating-human-development-indices.pdf (undp.org)
    """
    return zidz(
        np.log(gdp_per_capital_real_purchasing_parity_power()) - np.log(100),
        np.maximum(
            np.log(
                vmax(
                    gdp_per_capital_real_purchasing_parity_power().rename(
                        {"REGIONS_35_I": "REGIONS_35_I!"}
                    ),
                    dim=["REGIONS_35_I!"],
                )
            ),
            np.log(75000),
        )
        - np.log(100),
    )


@component.add(
    name="world_material_footprint",
    units="t/(Year*person)",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "al_market_sales": 1,
        "cu_market_sales": 1,
        "fe_market_sales": 1,
        "ni_market_sales": 1,
        "unit_conversion_mj_ej": 6,
        "unit_conversion_kg_mt": 6,
        "world_pe_by_commodity": 6,
        "pe_energy_density_mj_kg": 6,
        "world_population": 1,
        "unit_conversion_t_mt": 1,
    },
)
def world_material_footprint():
    """
    Proxy of the global material footprint
    """
    return (
        (
            al_market_sales()
            + cu_market_sales()
            + fe_market_sales()
            + ni_market_sales()
            + float(world_pe_by_commodity().loc["PE_agriculture_products"])
            * unit_conversion_mj_ej()
            / float(pe_energy_density_mj_kg().loc["PE_agriculture_products"])
            / unit_conversion_kg_mt()
            + float(world_pe_by_commodity().loc["PE_coal"])
            * unit_conversion_mj_ej()
            / float(pe_energy_density_mj_kg().loc["PE_coal"])
            / unit_conversion_kg_mt()
            + float(world_pe_by_commodity().loc["PE_oil"])
            * unit_conversion_mj_ej()
            / float(pe_energy_density_mj_kg().loc["PE_oil"])
            / unit_conversion_kg_mt()
            + float(world_pe_by_commodity().loc["PE_natural_gas"])
            * unit_conversion_mj_ej()
            / float(pe_energy_density_mj_kg().loc["PE_natural_gas"])
            / unit_conversion_kg_mt()
            + float(world_pe_by_commodity().loc["PE_forestry_products"])
            * unit_conversion_mj_ej()
            / float(pe_energy_density_mj_kg().loc["PE_forestry_products"])
            / unit_conversion_kg_mt()
            + float(world_pe_by_commodity().loc["PE_waste"])
            * unit_conversion_mj_ej()
            / float(pe_energy_density_mj_kg().loc["PE_waste"])
            / unit_conversion_kg_mt()
        )
        / world_population()
        * unit_conversion_t_mt()
    )
