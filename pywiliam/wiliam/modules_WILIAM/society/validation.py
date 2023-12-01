"""
Module society.validation
Translated using PySD version 3.10.0
"""


@component.add(
    name="check_education_population",
    units="people",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"workforce_per_educational_level": 1, "population_by_cohorts": 1},
)
def check_education_population():
    """
    Adjustment against the demographic module
    """
    return sum(
        workforce_per_educational_level().rename(
            {
                "REGIONS_35_I": "REGIONS_35_I!",
                "EDUCATIONAL_LEVEL_I": "EDUCATIONAL_LEVEL_I!",
                "SEX_I": "SEX_I!",
            }
        ),
        dim=["REGIONS_35_I!", "EDUCATIONAL_LEVEL_I!", "SEX_I!"],
    ) - sum(
        population_by_cohorts()
        .loc[:, :, _subscript_dict["AGE_EDUCATION_I"]]
        .rename(
            {
                "REGIONS_35_I": "REGIONS_35_I!",
                "SEX_I": "SEX_I!",
                "AGE_COHORTS_I": "AGE_EDUCATION_I!",
            }
        ),
        dim=["REGIONS_35_I!", "SEX_I!", "AGE_EDUCATION_I!"],
    )
