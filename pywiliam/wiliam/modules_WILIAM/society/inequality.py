"""
Module society.inequality
Translated using PySD version 3.10.0
"""


@component.add(
    name="Cumulative_Lorenz_GDP_EU27",
    units="DMNL",
    subscripts=["SGINI_EU_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"gdp_share_eu27_ordered": 378},
)
def cumulative_lorenz_gdp_eu27():
    value = xr.DataArray(
        np.nan, {"SGINI_EU_I": _subscript_dict["SGINI_EU_I"]}, ["SGINI_EU_I"]
    )
    value.loc[["SGINI_EU1"]] = float(gdp_share_eu27_ordered().loc["SGINI_EU1"])
    value.loc[["SGINI_EU2"]] = float(gdp_share_eu27_ordered().loc["SGINI_EU1"]) + float(
        gdp_share_eu27_ordered().loc["SGINI_EU2"]
    )
    value.loc[["SGINI_EU3"]] = (
        float(gdp_share_eu27_ordered().loc["SGINI_EU1"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU2"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU3"])
    )
    value.loc[["SGINI_EU4"]] = (
        float(gdp_share_eu27_ordered().loc["SGINI_EU1"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU2"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU3"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU4"])
    )
    value.loc[["SGINI_EU5"]] = (
        float(gdp_share_eu27_ordered().loc["SGINI_EU1"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU2"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU3"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU4"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU5"])
    )
    value.loc[["SGINI_EU6"]] = (
        float(gdp_share_eu27_ordered().loc["SGINI_EU1"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU2"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU3"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU4"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU5"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU6"])
    )
    value.loc[["SGINI_EU7"]] = (
        float(gdp_share_eu27_ordered().loc["SGINI_EU1"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU2"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU3"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU4"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU5"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU6"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU7"])
    )
    value.loc[["SGINI_EU8"]] = (
        float(gdp_share_eu27_ordered().loc["SGINI_EU1"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU2"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU3"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU4"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU5"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU6"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU7"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU8"])
    )
    value.loc[["SGINI_EU9"]] = (
        float(gdp_share_eu27_ordered().loc["SGINI_EU1"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU2"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU3"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU4"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU5"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU6"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU7"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU8"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU9"])
    )
    value.loc[["SGINI_EU10"]] = (
        float(gdp_share_eu27_ordered().loc["SGINI_EU1"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU2"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU3"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU4"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU5"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU6"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU7"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU8"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU9"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU10"])
    )
    value.loc[["SGINI_EU11"]] = (
        float(gdp_share_eu27_ordered().loc["SGINI_EU1"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU2"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU3"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU4"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU5"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU6"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU7"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU8"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU9"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU10"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU11"])
    )
    value.loc[["SGINI_EU12"]] = (
        float(gdp_share_eu27_ordered().loc["SGINI_EU1"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU2"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU3"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU4"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU5"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU6"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU7"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU8"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU9"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU10"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU11"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU12"])
    )
    value.loc[["SGINI_EU13"]] = (
        float(gdp_share_eu27_ordered().loc["SGINI_EU1"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU2"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU3"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU4"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU5"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU6"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU7"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU8"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU9"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU10"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU11"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU12"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU13"])
    )
    value.loc[["SGINI_EU14"]] = (
        float(gdp_share_eu27_ordered().loc["SGINI_EU1"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU2"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU3"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU4"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU5"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU6"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU7"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU8"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU9"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU10"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU11"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU12"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU13"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU14"])
    )
    value.loc[["SGINI_EU15"]] = (
        float(gdp_share_eu27_ordered().loc["SGINI_EU1"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU2"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU3"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU4"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU5"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU6"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU7"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU8"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU9"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU10"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU11"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU12"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU13"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU14"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU15"])
    )
    value.loc[["SGINI_EU16"]] = (
        float(gdp_share_eu27_ordered().loc["SGINI_EU1"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU2"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU3"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU4"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU5"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU6"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU7"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU8"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU9"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU10"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU11"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU12"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU13"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU14"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU15"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU16"])
    )
    value.loc[["SGINI_EU17"]] = (
        float(gdp_share_eu27_ordered().loc["SGINI_EU1"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU2"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU3"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU4"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU5"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU6"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU7"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU8"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU9"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU10"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU11"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU12"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU13"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU14"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU15"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU16"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU17"])
    )
    value.loc[["SGINI_EU18"]] = (
        float(gdp_share_eu27_ordered().loc["SGINI_EU1"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU2"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU3"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU4"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU5"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU6"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU7"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU8"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU9"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU10"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU11"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU12"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU13"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU14"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU15"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU16"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU17"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU18"])
    )
    value.loc[["SGINI_EU19"]] = (
        float(gdp_share_eu27_ordered().loc["SGINI_EU1"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU2"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU3"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU4"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU5"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU6"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU7"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU8"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU9"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU10"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU11"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU12"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU13"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU14"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU15"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU16"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU17"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU18"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU19"])
    )
    value.loc[["SGINI_EU20"]] = (
        float(gdp_share_eu27_ordered().loc["SGINI_EU1"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU2"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU3"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU4"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU5"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU6"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU7"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU8"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU9"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU10"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU11"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU12"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU13"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU14"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU15"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU16"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU17"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU18"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU19"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU20"])
    )
    value.loc[["SGINI_EU21"]] = (
        float(gdp_share_eu27_ordered().loc["SGINI_EU1"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU2"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU3"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU4"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU5"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU6"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU7"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU8"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU9"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU10"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU11"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU12"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU13"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU14"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU15"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU16"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU17"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU18"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU19"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU20"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU21"])
    )
    value.loc[["SGINI_EU22"]] = (
        float(gdp_share_eu27_ordered().loc["SGINI_EU1"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU2"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU3"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU4"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU5"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU6"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU7"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU8"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU9"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU10"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU11"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU12"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU13"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU14"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU15"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU16"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU17"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU18"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU19"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU20"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU21"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU22"])
    )
    value.loc[["SGINI_EU23"]] = (
        float(gdp_share_eu27_ordered().loc["SGINI_EU1"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU2"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU3"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU4"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU5"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU6"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU7"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU8"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU9"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU10"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU11"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU12"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU13"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU14"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU15"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU16"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU17"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU18"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU19"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU20"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU21"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU22"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU23"])
    )
    value.loc[["SGINI_EU24"]] = (
        float(gdp_share_eu27_ordered().loc["SGINI_EU1"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU2"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU3"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU4"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU5"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU6"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU7"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU8"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU9"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU10"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU11"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU12"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU13"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU14"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU15"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU16"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU17"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU18"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU19"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU20"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU21"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU22"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU23"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU24"])
    )
    value.loc[["SGINI_EU25"]] = (
        float(gdp_share_eu27_ordered().loc["SGINI_EU1"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU2"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU3"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU4"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU5"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU6"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU7"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU8"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU9"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU10"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU11"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU12"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU13"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU14"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU15"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU16"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU17"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU18"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU19"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU20"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU21"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU22"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU23"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU24"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU25"])
    )
    value.loc[["SGINI_EU26"]] = (
        float(gdp_share_eu27_ordered().loc["SGINI_EU1"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU2"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU3"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU4"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU5"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU6"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU7"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU8"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU9"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU10"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU11"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU12"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU13"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU14"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU15"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU16"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU17"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU18"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU19"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU20"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU21"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU22"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU23"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU24"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU25"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU26"])
    )
    value.loc[["SGINI_EU27"]] = (
        float(gdp_share_eu27_ordered().loc["SGINI_EU1"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU2"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU3"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU4"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU5"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU6"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU7"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU8"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU9"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU10"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU11"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU12"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU13"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU14"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU15"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU16"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU17"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU18"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU19"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU20"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU21"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU22"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU23"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU24"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU25"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU26"])
        + float(gdp_share_eu27_ordered().loc["SGINI_EU27"])
    )
    return value


@component.add(
    name="Cumulative_Lorenz_GDP_regions",
    units="DMNL",
    subscripts=["SGINI_REGIONS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"gdp_share_regions_ordered": 45},
)
def cumulative_lorenz_gdp_regions():
    """
    construct new vector which includes cumulated GDP: region1 (poorest) has only the GDP share corresponding to it. Region2 has its own GDP share + the one of region 1. The next richest region has its own GDP share + the share of the previous poorer regions and so on.
    """
    value = xr.DataArray(
        np.nan,
        {"SGINI_REGIONS_I": _subscript_dict["SGINI_REGIONS_I"]},
        ["SGINI_REGIONS_I"],
    )
    value.loc[["SGINI_REGION1"]] = float(
        gdp_share_regions_ordered().loc["SGINI_REGION1"]
    )
    value.loc[["SGINI_REGION2"]] = float(
        gdp_share_regions_ordered().loc["SGINI_REGION1"]
    ) + float(gdp_share_regions_ordered().loc["SGINI_REGION2"])
    value.loc[["SGINI_REGION3"]] = (
        float(gdp_share_regions_ordered().loc["SGINI_REGION1"])
        + float(gdp_share_regions_ordered().loc["SGINI_REGION2"])
        + float(gdp_share_regions_ordered().loc["SGINI_REGION3"])
    )
    value.loc[["SGINI_REGION4"]] = (
        float(gdp_share_regions_ordered().loc["SGINI_REGION1"])
        + float(gdp_share_regions_ordered().loc["SGINI_REGION2"])
        + float(gdp_share_regions_ordered().loc["SGINI_REGION3"])
        + float(gdp_share_regions_ordered().loc["SGINI_REGION4"])
    )
    value.loc[["SGINI_REGION5"]] = (
        float(gdp_share_regions_ordered().loc["SGINI_REGION1"])
        + float(gdp_share_regions_ordered().loc["SGINI_REGION2"])
        + float(gdp_share_regions_ordered().loc["SGINI_REGION3"])
        + float(gdp_share_regions_ordered().loc["SGINI_REGION4"])
        + float(gdp_share_regions_ordered().loc["SGINI_REGION5"])
    )
    value.loc[["SGINI_REGION6"]] = (
        float(gdp_share_regions_ordered().loc["SGINI_REGION1"])
        + float(gdp_share_regions_ordered().loc["SGINI_REGION2"])
        + float(gdp_share_regions_ordered().loc["SGINI_REGION3"])
        + float(gdp_share_regions_ordered().loc["SGINI_REGION4"])
        + float(gdp_share_regions_ordered().loc["SGINI_REGION5"])
        + float(gdp_share_regions_ordered().loc["SGINI_REGION6"])
    )
    value.loc[["SGINI_REGION7"]] = (
        float(gdp_share_regions_ordered().loc["SGINI_REGION1"])
        + float(gdp_share_regions_ordered().loc["SGINI_REGION2"])
        + float(gdp_share_regions_ordered().loc["SGINI_REGION3"])
        + float(gdp_share_regions_ordered().loc["SGINI_REGION4"])
        + float(gdp_share_regions_ordered().loc["SGINI_REGION5"])
        + float(gdp_share_regions_ordered().loc["SGINI_REGION6"])
        + float(gdp_share_regions_ordered().loc["SGINI_REGION7"])
    )
    value.loc[["SGINI_REGION8"]] = (
        float(gdp_share_regions_ordered().loc["SGINI_REGION1"])
        + float(gdp_share_regions_ordered().loc["SGINI_REGION2"])
        + float(gdp_share_regions_ordered().loc["SGINI_REGION3"])
        + float(gdp_share_regions_ordered().loc["SGINI_REGION4"])
        + float(gdp_share_regions_ordered().loc["SGINI_REGION5"])
        + float(gdp_share_regions_ordered().loc["SGINI_REGION6"])
        + float(gdp_share_regions_ordered().loc["SGINI_REGION7"])
        + float(gdp_share_regions_ordered().loc["SGINI_REGION8"])
    )
    value.loc[["SGINI_REGION9"]] = (
        float(gdp_share_regions_ordered().loc["SGINI_REGION1"])
        + float(gdp_share_regions_ordered().loc["SGINI_REGION2"])
        + float(gdp_share_regions_ordered().loc["SGINI_REGION3"])
        + float(gdp_share_regions_ordered().loc["SGINI_REGION4"])
        + float(gdp_share_regions_ordered().loc["SGINI_REGION5"])
        + float(gdp_share_regions_ordered().loc["SGINI_REGION6"])
        + float(gdp_share_regions_ordered().loc["SGINI_REGION7"])
        + float(gdp_share_regions_ordered().loc["SGINI_REGION8"])
        + float(gdp_share_regions_ordered().loc["SGINI_REGION9"])
    )
    return value


@component.add(
    name="GDP_pc_EU27_gini",
    units="Mdollars_2015/(Year*person)",
    subscripts=["FGINI_EU_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"gdp_per_capita_eu27": 27},
)
def gdp_pc_eu27_gini():
    value = xr.DataArray(
        np.nan, {"FGINI_EU_I": _subscript_dict["FGINI_EU_I"]}, ["FGINI_EU_I"]
    )
    value.loc[["FGINI_EU1"]] = float(gdp_per_capita_eu27().loc["AUSTRIA"])
    value.loc[["FGINI_EU2"]] = float(gdp_per_capita_eu27().loc["BELGIUM"])
    value.loc[["FGINI_EU3"]] = float(gdp_per_capita_eu27().loc["BULGARIA"])
    value.loc[["FGINI_EU4"]] = float(gdp_per_capita_eu27().loc["CROATIA"])
    value.loc[["FGINI_EU5"]] = float(gdp_per_capita_eu27().loc["CYPRUS"])
    value.loc[["FGINI_EU6"]] = float(gdp_per_capita_eu27().loc["CZECH_REPUBLIC"])
    value.loc[["FGINI_EU7"]] = float(gdp_per_capita_eu27().loc["DENMARK"])
    value.loc[["FGINI_EU8"]] = float(gdp_per_capita_eu27().loc["ESTONIA"])
    value.loc[["FGINI_EU9"]] = float(gdp_per_capita_eu27().loc["FINLAND"])
    value.loc[["FGINI_EU10"]] = float(gdp_per_capita_eu27().loc["FRANCE"])
    value.loc[["FGINI_EU11"]] = float(gdp_per_capita_eu27().loc["GERMANY"])
    value.loc[["FGINI_EU12"]] = float(gdp_per_capita_eu27().loc["GREECE"])
    value.loc[["FGINI_EU13"]] = float(gdp_per_capita_eu27().loc["HUNGARY"])
    value.loc[["FGINI_EU14"]] = float(gdp_per_capita_eu27().loc["IRELAND"])
    value.loc[["FGINI_EU15"]] = float(gdp_per_capita_eu27().loc["ITALY"])
    value.loc[["FGINI_EU16"]] = float(gdp_per_capita_eu27().loc["LATVIA"])
    value.loc[["FGINI_EU17"]] = float(gdp_per_capita_eu27().loc["LITHUANIA"])
    value.loc[["FGINI_EU18"]] = float(gdp_per_capita_eu27().loc["LUXEMBOURG"])
    value.loc[["FGINI_EU19"]] = float(gdp_per_capita_eu27().loc["MALTA"])
    value.loc[["FGINI_EU20"]] = float(gdp_per_capita_eu27().loc["NETHERLANDS"])
    value.loc[["FGINI_EU21"]] = float(gdp_per_capita_eu27().loc["POLAND"])
    value.loc[["FGINI_EU22"]] = float(gdp_per_capita_eu27().loc["PORTUGAL"])
    value.loc[["FGINI_EU23"]] = float(gdp_per_capita_eu27().loc["ROMANIA"])
    value.loc[["FGINI_EU24"]] = float(gdp_per_capita_eu27().loc["SLOVAKIA"])
    value.loc[["FGINI_EU25"]] = float(gdp_per_capita_eu27().loc["SLOVENIA"])
    value.loc[["FGINI_EU26"]] = float(gdp_per_capita_eu27().loc["SPAIN"])
    value.loc[["FGINI_EU27"]] = float(gdp_per_capita_eu27().loc["SWEDEN"])
    return value


@component.add(
    name="GDP_pc_EU27_ordered",
    units="Mdollars_2015/people",
    subscripts=["FGINI_EU_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"gdp_pc_eu27_gini": 1},
)
def gdp_pc_eu27_ordered():
    return vector_sort_order(gdp_pc_eu27_gini(), 1)


@component.add(
    name="GDP_per_capita_EU27",
    units="Mdollars_2015/(Year*person)",
    subscripts=["REGIONS_EU27_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "gross_domestic_product_real_supply_side": 1,
        "population_35_regions": 1,
    },
)
def gdp_per_capita_eu27():
    return gross_domestic_product_real_supply_side().loc[
        _subscript_dict["REGIONS_EU27_I"]
    ].rename({"REGIONS_35_I": "REGIONS_EU27_I"}) / population_35_regions().loc[
        _subscript_dict["REGIONS_EU27_I"]
    ].rename(
        {"REGIONS_35_I": "REGIONS_EU27_I"}
    )


@component.add(
    name="GDP_share_EU27",
    units="1",
    subscripts=["REGIONS_EU27_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"gross_domestic_product_real_supply_side": 2},
)
def gdp_share_eu27():
    return gross_domestic_product_real_supply_side().loc[
        _subscript_dict["REGIONS_EU27_I"]
    ].rename({"REGIONS_35_I": "REGIONS_EU27_I"}) / sum(
        gross_domestic_product_real_supply_side()
        .loc[_subscript_dict["REGIONS_EU27_I"]]
        .rename({"REGIONS_35_I": "REGIONS_EU27_I!"}),
        dim=["REGIONS_EU27_I!"],
    )


@component.add(
    name="GDP_share_EU27_ordered",
    units="1",
    subscripts=["SGINI_EU_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"gdp_shares_eu27_gini": 1, "gdp_pc_eu27_ordered": 1},
)
def gdp_share_eu27_ordered():
    return vector_reorder(
        xr.DataArray(
            gdp_shares_eu27_gini().values,
            {"SGINI_EU_I": _subscript_dict["SGINI_EU_I"]},
            ["SGINI_EU_I"],
        ),
        xr.DataArray(
            gdp_pc_eu27_ordered().values,
            {"SGINI_EU_I": _subscript_dict["SGINI_EU_I"]},
            ["SGINI_EU_I"],
        ),
    )


@component.add(
    name="GDP_share_regions",
    units="1",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"gdp_real_9r": 2},
)
def gdp_share_regions():
    """
    calculate each region's share of GDP of the world
    """
    return gdp_real_9r() / sum(
        gdp_real_9r().rename({"REGIONS_9_I": "REGIONS_9_I!"}), dim=["REGIONS_9_I!"]
    )


@component.add(
    name="GDP_share_regions_ordered",
    units="1",
    subscripts=["SGINI_REGIONS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"gdp_shares_regions_gini": 1, "gdppc_region_ordered": 1},
)
def gdp_share_regions_ordered():
    """
    order region according to smallest GDP p.c.
    """
    return vector_reorder(
        xr.DataArray(
            gdp_shares_regions_gini().values,
            {"SGINI_REGIONS_I": _subscript_dict["SGINI_REGIONS_I"]},
            ["SGINI_REGIONS_I"],
        ),
        xr.DataArray(
            gdppc_region_ordered().values,
            {"SGINI_REGIONS_I": _subscript_dict["SGINI_REGIONS_I"]},
            ["SGINI_REGIONS_I"],
        ),
    )


@component.add(
    name="GDP_shares_EU27_gini",
    units="1",
    subscripts=["FGINI_EU_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"gdp_share_eu27": 27},
)
def gdp_shares_eu27_gini():
    value = xr.DataArray(
        np.nan, {"FGINI_EU_I": _subscript_dict["FGINI_EU_I"]}, ["FGINI_EU_I"]
    )
    value.loc[["FGINI_EU1"]] = float(gdp_share_eu27().loc["AUSTRIA"])
    value.loc[["FGINI_EU2"]] = float(gdp_share_eu27().loc["BELGIUM"])
    value.loc[["FGINI_EU3"]] = float(gdp_share_eu27().loc["BULGARIA"])
    value.loc[["FGINI_EU4"]] = float(gdp_share_eu27().loc["CROATIA"])
    value.loc[["FGINI_EU5"]] = float(gdp_share_eu27().loc["CYPRUS"])
    value.loc[["FGINI_EU6"]] = float(gdp_share_eu27().loc["CZECH_REPUBLIC"])
    value.loc[["FGINI_EU7"]] = float(gdp_share_eu27().loc["DENMARK"])
    value.loc[["FGINI_EU8"]] = float(gdp_share_eu27().loc["ESTONIA"])
    value.loc[["FGINI_EU9"]] = float(gdp_share_eu27().loc["FINLAND"])
    value.loc[["FGINI_EU10"]] = float(gdp_share_eu27().loc["FRANCE"])
    value.loc[["FGINI_EU11"]] = float(gdp_share_eu27().loc["GERMANY"])
    value.loc[["FGINI_EU12"]] = float(gdp_share_eu27().loc["GREECE"])
    value.loc[["FGINI_EU13"]] = float(gdp_share_eu27().loc["HUNGARY"])
    value.loc[["FGINI_EU14"]] = float(gdp_share_eu27().loc["IRELAND"])
    value.loc[["FGINI_EU15"]] = float(gdp_share_eu27().loc["ITALY"])
    value.loc[["FGINI_EU16"]] = float(gdp_share_eu27().loc["LATVIA"])
    value.loc[["FGINI_EU17"]] = float(gdp_share_eu27().loc["LITHUANIA"])
    value.loc[["FGINI_EU18"]] = float(gdp_share_eu27().loc["LUXEMBOURG"])
    value.loc[["FGINI_EU19"]] = float(gdp_share_eu27().loc["MALTA"])
    value.loc[["FGINI_EU20"]] = float(gdp_share_eu27().loc["NETHERLANDS"])
    value.loc[["FGINI_EU21"]] = float(gdp_share_eu27().loc["POLAND"])
    value.loc[["FGINI_EU22"]] = float(gdp_share_eu27().loc["PORTUGAL"])
    value.loc[["FGINI_EU23"]] = float(gdp_share_eu27().loc["ROMANIA"])
    value.loc[["FGINI_EU24"]] = float(gdp_share_eu27().loc["SLOVAKIA"])
    value.loc[["FGINI_EU25"]] = float(gdp_share_eu27().loc["SLOVENIA"])
    value.loc[["FGINI_EU26"]] = float(gdp_share_eu27().loc["SPAIN"])
    value.loc[["FGINI_EU27"]] = float(gdp_share_eu27().loc["SWEDEN"])
    return value


@component.add(
    name="GDP_shares_regions_gini",
    units="1",
    subscripts=["FGINI_REGIONS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"gdp_share_regions": 9},
)
def gdp_shares_regions_gini():
    """
    constructing a new vector including the region's GDP shares
    """
    value = xr.DataArray(
        np.nan,
        {"FGINI_REGIONS_I": _subscript_dict["FGINI_REGIONS_I"]},
        ["FGINI_REGIONS_I"],
    )
    value.loc[["FGINI_REGION1"]] = float(gdp_share_regions().loc["EU27"])
    value.loc[["FGINI_REGION2"]] = float(gdp_share_regions().loc["UK"])
    value.loc[["FGINI_REGION3"]] = float(gdp_share_regions().loc["CHINA"])
    value.loc[["FGINI_REGION4"]] = float(gdp_share_regions().loc["EASOC"])
    value.loc[["FGINI_REGION5"]] = float(gdp_share_regions().loc["INDIA"])
    value.loc[["FGINI_REGION6"]] = float(gdp_share_regions().loc["LATAM"])
    value.loc[["FGINI_REGION7"]] = float(gdp_share_regions().loc["RUSSIA"])
    value.loc[["FGINI_REGION8"]] = float(gdp_share_regions().loc["USMCA"])
    value.loc[["FGINI_REGION9"]] = float(gdp_share_regions().loc["LROW"])
    return value


@component.add(
    name="GDPpc_region_ordered",
    units="Mdollars_2015/people",
    subscripts=["FGINI_REGIONS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"gdppc_regions_gini": 1},
)
def gdppc_region_ordered():
    """
    sorting the vector FGINI_REGIONS, begin with smallest value (=poorest region)
    """
    return vector_sort_order(gdppc_regions_gini(), 1)


@component.add(
    name="GDPpc_regions_gini",
    units="Mdollars_2015/(Year*person)",
    subscripts=["FGINI_REGIONS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"gdppc_9r_real": 9},
)
def gdppc_regions_gini():
    """
    constructing a new vector with the GDP p.c. for each region
    """
    value = xr.DataArray(
        np.nan,
        {"FGINI_REGIONS_I": _subscript_dict["FGINI_REGIONS_I"]},
        ["FGINI_REGIONS_I"],
    )
    value.loc[["FGINI_REGION1"]] = float(gdppc_9r_real().loc["EU27"])
    value.loc[["FGINI_REGION2"]] = float(gdppc_9r_real().loc["UK"])
    value.loc[["FGINI_REGION3"]] = float(gdppc_9r_real().loc["CHINA"])
    value.loc[["FGINI_REGION4"]] = float(gdppc_9r_real().loc["EASOC"])
    value.loc[["FGINI_REGION5"]] = float(gdppc_9r_real().loc["INDIA"])
    value.loc[["FGINI_REGION6"]] = float(gdppc_9r_real().loc["LATAM"])
    value.loc[["FGINI_REGION7"]] = float(gdppc_9r_real().loc["RUSSIA"])
    value.loc[["FGINI_REGION8"]] = float(gdppc_9r_real().loc["USMCA"])
    value.loc[["FGINI_REGION9"]] = float(gdppc_9r_real().loc["LROW"])
    return value


@component.add(
    name="GINI_disposable_income_by_region",
    units="DMNL",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "households_shares_ordered": 61,
        "households_disposable_income_cumulate_ordered": 121,
    },
)
def gini_disposable_income_by_region():
    """
    GINI of disposable income by region
    """
    return 1 - (
        households_shares_ordered().loc[:, "gini1"].reset_coords(drop=True)
        * households_disposable_income_cumulate_ordered()
        .loc[:, "gini1"]
        .reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini2"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini3"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini4"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini5"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini6"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini7"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini8"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini9"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini10"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini11"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini12"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini13"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini14"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini15"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini16"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini17"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini18"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini19"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini20"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini21"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini22"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini23"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini24"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini25"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini26"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini27"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini28"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini29"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini30"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini31"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini32"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini33"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini34"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini35"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini36"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini37"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini38"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini39"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini40"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini41"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini41"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini42"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini41"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini42"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini43"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini42"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini43"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini44"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini43"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini44"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini45"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini44"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini45"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini46"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini45"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini46"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini47"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini46"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini47"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini48"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini47"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini48"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini49"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini48"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini49"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini50"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini49"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini50"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini51"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini50"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini51"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini52"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini51"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini52"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini53"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini52"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini53"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini54"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini53"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini54"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini55"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini54"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini55"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini56"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini55"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini56"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini57"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini56"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini57"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini58"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini57"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini58"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini59"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini58"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini59"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini60"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini59"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini60"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini61"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini60"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini61"].reset_coords(drop=True)
    )


@component.add(
    name="Gini_GDPpc_EU27",
    units="Dnml",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"cumulative_lorenz_gdp_eu27": 53, "pop_shares_eu27_ordered": 27},
)
def gini_gdppc_eu27():
    """
    The Gini GDPpc index measures the extent to which the distribution of GDP between WILIAM regions deviates from a perfectly equal distribution. A Gini index of 0 represents perfect equality, while an index of 1 implies perfect inequality. Formula for calculating Gini: 1 - 2*the area under the lorentz curve (=cumulated GDP). This translates into the above form.
    """
    return 1 - (
        float(cumulative_lorenz_gdp_eu27().loc["SGINI_EU1"])
        * float(pop_shares_eu27_ordered().loc["SGINI_EU1"])
        + (
            float(cumulative_lorenz_gdp_eu27().loc["SGINI_EU1"])
            + float(cumulative_lorenz_gdp_eu27().loc["SGINI_EU2"])
        )
        * float(pop_shares_eu27_ordered().loc["SGINI_EU2"])
        + (
            float(cumulative_lorenz_gdp_eu27().loc["SGINI_EU2"])
            + float(cumulative_lorenz_gdp_eu27().loc["SGINI_EU3"])
        )
        * float(pop_shares_eu27_ordered().loc["SGINI_EU3"])
        + (
            float(cumulative_lorenz_gdp_eu27().loc["SGINI_EU3"])
            + float(cumulative_lorenz_gdp_eu27().loc["SGINI_EU4"])
        )
        * float(pop_shares_eu27_ordered().loc["SGINI_EU4"])
        + (
            float(cumulative_lorenz_gdp_eu27().loc["SGINI_EU4"])
            + float(cumulative_lorenz_gdp_eu27().loc["SGINI_EU5"])
        )
        * float(pop_shares_eu27_ordered().loc["SGINI_EU5"])
        + (
            float(cumulative_lorenz_gdp_eu27().loc["SGINI_EU5"])
            + float(cumulative_lorenz_gdp_eu27().loc["SGINI_EU6"])
        )
        * float(pop_shares_eu27_ordered().loc["SGINI_EU6"])
        + (
            float(cumulative_lorenz_gdp_eu27().loc["SGINI_EU6"])
            + float(cumulative_lorenz_gdp_eu27().loc["SGINI_EU7"])
        )
        * float(pop_shares_eu27_ordered().loc["SGINI_EU7"])
        + (
            float(cumulative_lorenz_gdp_eu27().loc["SGINI_EU7"])
            + float(cumulative_lorenz_gdp_eu27().loc["SGINI_EU8"])
        )
        * float(pop_shares_eu27_ordered().loc["SGINI_EU8"])
        + (
            float(cumulative_lorenz_gdp_eu27().loc["SGINI_EU8"])
            + float(cumulative_lorenz_gdp_eu27().loc["SGINI_EU9"])
        )
        * float(pop_shares_eu27_ordered().loc["SGINI_EU9"])
        + (
            float(cumulative_lorenz_gdp_eu27().loc["SGINI_EU9"])
            + float(cumulative_lorenz_gdp_eu27().loc["SGINI_EU10"])
        )
        * float(pop_shares_eu27_ordered().loc["SGINI_EU10"])
        + (
            float(cumulative_lorenz_gdp_eu27().loc["SGINI_EU10"])
            + float(cumulative_lorenz_gdp_eu27().loc["SGINI_EU11"])
        )
        * float(pop_shares_eu27_ordered().loc["SGINI_EU11"])
        + (
            float(cumulative_lorenz_gdp_eu27().loc["SGINI_EU11"])
            + float(cumulative_lorenz_gdp_eu27().loc["SGINI_EU12"])
        )
        * float(pop_shares_eu27_ordered().loc["SGINI_EU12"])
        + (
            float(cumulative_lorenz_gdp_eu27().loc["SGINI_EU12"])
            + float(cumulative_lorenz_gdp_eu27().loc["SGINI_EU13"])
        )
        * float(pop_shares_eu27_ordered().loc["SGINI_EU13"])
        + (
            float(cumulative_lorenz_gdp_eu27().loc["SGINI_EU13"])
            + float(cumulative_lorenz_gdp_eu27().loc["SGINI_EU14"])
        )
        * float(pop_shares_eu27_ordered().loc["SGINI_EU14"])
        + (
            float(cumulative_lorenz_gdp_eu27().loc["SGINI_EU14"])
            + float(cumulative_lorenz_gdp_eu27().loc["SGINI_EU15"])
        )
        * float(pop_shares_eu27_ordered().loc["SGINI_EU15"])
        + (
            float(cumulative_lorenz_gdp_eu27().loc["SGINI_EU15"])
            + float(cumulative_lorenz_gdp_eu27().loc["SGINI_EU16"])
        )
        * float(pop_shares_eu27_ordered().loc["SGINI_EU16"])
        + (
            float(cumulative_lorenz_gdp_eu27().loc["SGINI_EU16"])
            + float(cumulative_lorenz_gdp_eu27().loc["SGINI_EU17"])
        )
        * float(pop_shares_eu27_ordered().loc["SGINI_EU17"])
        + (
            float(cumulative_lorenz_gdp_eu27().loc["SGINI_EU17"])
            + float(cumulative_lorenz_gdp_eu27().loc["SGINI_EU18"])
        )
        * float(pop_shares_eu27_ordered().loc["SGINI_EU18"])
        + (
            float(cumulative_lorenz_gdp_eu27().loc["SGINI_EU18"])
            + float(cumulative_lorenz_gdp_eu27().loc["SGINI_EU19"])
        )
        * float(pop_shares_eu27_ordered().loc["SGINI_EU19"])
        + (
            float(cumulative_lorenz_gdp_eu27().loc["SGINI_EU19"])
            + float(cumulative_lorenz_gdp_eu27().loc["SGINI_EU20"])
        )
        * float(pop_shares_eu27_ordered().loc["SGINI_EU20"])
        + (
            float(cumulative_lorenz_gdp_eu27().loc["SGINI_EU20"])
            + float(cumulative_lorenz_gdp_eu27().loc["SGINI_EU21"])
        )
        * float(pop_shares_eu27_ordered().loc["SGINI_EU21"])
        + (
            float(cumulative_lorenz_gdp_eu27().loc["SGINI_EU21"])
            + float(cumulative_lorenz_gdp_eu27().loc["SGINI_EU22"])
        )
        * float(pop_shares_eu27_ordered().loc["SGINI_EU22"])
        + (
            float(cumulative_lorenz_gdp_eu27().loc["SGINI_EU22"])
            + float(cumulative_lorenz_gdp_eu27().loc["SGINI_EU23"])
        )
        * float(pop_shares_eu27_ordered().loc["SGINI_EU23"])
        + (
            float(cumulative_lorenz_gdp_eu27().loc["SGINI_EU23"])
            + float(cumulative_lorenz_gdp_eu27().loc["SGINI_EU24"])
        )
        * float(pop_shares_eu27_ordered().loc["SGINI_EU24"])
        + (
            float(cumulative_lorenz_gdp_eu27().loc["SGINI_EU24"])
            + float(cumulative_lorenz_gdp_eu27().loc["SGINI_EU25"])
        )
        * float(pop_shares_eu27_ordered().loc["SGINI_EU25"])
        + (
            float(cumulative_lorenz_gdp_eu27().loc["SGINI_EU25"])
            + float(cumulative_lorenz_gdp_eu27().loc["SGINI_EU26"])
        )
        * float(pop_shares_eu27_ordered().loc["SGINI_EU26"])
        + (
            float(cumulative_lorenz_gdp_eu27().loc["SGINI_EU26"])
            + float(cumulative_lorenz_gdp_eu27().loc["SGINI_EU27"])
        )
        * float(pop_shares_eu27_ordered().loc["SGINI_EU27"])
    )


@component.add(
    name="GINI_GDPpc_regions",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"cumulative_lorenz_gdp_regions": 17, "pop_shares_regions_ordered": 9},
)
def gini_gdppc_regions():
    """
    The Gini GDPpc index measures the extent to which the distribution of GDP between WILIAM regions deviates from a perfectly equal distribution. A Gini index of 0 represents perfect equality, while an index of 1 implies perfect inequality. Formula for calculating Gini: 1 - 2*the area under the lorentz curve (=cumulated GDP). This translates into the above form.
    """
    return 1 - (
        float(cumulative_lorenz_gdp_regions().loc["SGINI_REGION1"])
        * float(pop_shares_regions_ordered().loc["SGINI_REGION1"])
        + (
            float(cumulative_lorenz_gdp_regions().loc["SGINI_REGION1"])
            + float(cumulative_lorenz_gdp_regions().loc["SGINI_REGION2"])
        )
        * float(pop_shares_regions_ordered().loc["SGINI_REGION2"])
        + (
            float(cumulative_lorenz_gdp_regions().loc["SGINI_REGION2"])
            + float(cumulative_lorenz_gdp_regions().loc["SGINI_REGION3"])
        )
        * float(pop_shares_regions_ordered().loc["SGINI_REGION3"])
        + (
            float(cumulative_lorenz_gdp_regions().loc["SGINI_REGION3"])
            + float(cumulative_lorenz_gdp_regions().loc["SGINI_REGION4"])
        )
        * float(pop_shares_regions_ordered().loc["SGINI_REGION4"])
        + (
            float(cumulative_lorenz_gdp_regions().loc["SGINI_REGION4"])
            + float(cumulative_lorenz_gdp_regions().loc["SGINI_REGION5"])
        )
        * float(pop_shares_regions_ordered().loc["SGINI_REGION5"])
        + (
            float(cumulative_lorenz_gdp_regions().loc["SGINI_REGION5"])
            + float(cumulative_lorenz_gdp_regions().loc["SGINI_REGION6"])
        )
        * float(pop_shares_regions_ordered().loc["SGINI_REGION6"])
        + (
            float(cumulative_lorenz_gdp_regions().loc["SGINI_REGION6"])
            + float(cumulative_lorenz_gdp_regions().loc["SGINI_REGION7"])
        )
        * float(pop_shares_regions_ordered().loc["SGINI_REGION7"])
        + (
            float(cumulative_lorenz_gdp_regions().loc["SGINI_REGION7"])
            + float(cumulative_lorenz_gdp_regions().loc["SGINI_REGION8"])
        )
        * float(pop_shares_regions_ordered().loc["SGINI_REGION8"])
        + (
            float(cumulative_lorenz_gdp_regions().loc["SGINI_REGION8"])
            + float(cumulative_lorenz_gdp_regions().loc["SGINI_REGION9"])
        )
        * float(pop_shares_regions_ordered().loc["SGINI_REGION9"])
    )


@component.add(
    name="households_disposable_income_cumulate_ordered",
    units="DMNL",
    subscripts=["REGIONS_35_I", "GINI_ORDER_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"households_disposable_income_share_ordered": 1891},
)
def households_disposable_income_cumulate_ordered():
    """
    cumulative ordered share of households disposable income
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
            "GINI_ORDER_I": _subscript_dict["GINI_ORDER_I"],
        },
        ["REGIONS_35_I", "GINI_ORDER_I"],
    )
    value.loc[:, ["gini1"]] = (
        households_disposable_income_share_ordered()
        .loc[:, "gini1"]
        .reset_coords(drop=True)
        .expand_dims({"GINI_ORDER_I": ["gini1"]}, 1)
        .values
    )
    value.loc[:, ["gini2"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI_ORDER_I": ["gini2"]}, 1)
        .values
    )
    value.loc[:, ["gini3"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI_ORDER_I": ["gini3"]}, 1)
        .values
    )
    value.loc[:, ["gini4"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI_ORDER_I": ["gini4"]}, 1)
        .values
    )
    value.loc[:, ["gini5"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI_ORDER_I": ["gini5"]}, 1)
        .values
    )
    value.loc[:, ["gini6"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI_ORDER_I": ["gini6"]}, 1)
        .values
    )
    value.loc[:, ["gini7"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI_ORDER_I": ["gini7"]}, 1)
        .values
    )
    value.loc[:, ["gini8"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI_ORDER_I": ["gini8"]}, 1)
        .values
    )
    value.loc[:, ["gini9"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI_ORDER_I": ["gini9"]}, 1)
        .values
    )
    value.loc[:, ["gini10"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI_ORDER_I": ["gini10"]}, 1)
        .values
    )
    value.loc[:, ["gini11"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI_ORDER_I": ["gini11"]}, 1)
        .values
    )
    value.loc[:, ["gini12"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI_ORDER_I": ["gini12"]}, 1)
        .values
    )
    value.loc[:, ["gini13"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI_ORDER_I": ["gini13"]}, 1)
        .values
    )
    value.loc[:, ["gini14"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI_ORDER_I": ["gini14"]}, 1)
        .values
    )
    value.loc[:, ["gini15"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI_ORDER_I": ["gini15"]}, 1)
        .values
    )
    value.loc[:, ["gini16"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI_ORDER_I": ["gini16"]}, 1)
        .values
    )
    value.loc[:, ["gini17"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI_ORDER_I": ["gini17"]}, 1)
        .values
    )
    value.loc[:, ["gini18"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI_ORDER_I": ["gini18"]}, 1)
        .values
    )
    value.loc[:, ["gini19"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI_ORDER_I": ["gini19"]}, 1)
        .values
    )
    value.loc[:, ["gini20"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI_ORDER_I": ["gini20"]}, 1)
        .values
    )
    value.loc[:, ["gini21"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI_ORDER_I": ["gini21"]}, 1)
        .values
    )
    value.loc[:, ["gini22"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI_ORDER_I": ["gini22"]}, 1)
        .values
    )
    value.loc[:, ["gini23"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI_ORDER_I": ["gini23"]}, 1)
        .values
    )
    value.loc[:, ["gini24"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI_ORDER_I": ["gini24"]}, 1)
        .values
    )
    value.loc[:, ["gini25"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI_ORDER_I": ["gini25"]}, 1)
        .values
    )
    value.loc[:, ["gini26"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI_ORDER_I": ["gini26"]}, 1)
        .values
    )
    value.loc[:, ["gini27"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI_ORDER_I": ["gini27"]}, 1)
        .values
    )
    value.loc[:, ["gini28"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI_ORDER_I": ["gini28"]}, 1)
        .values
    )
    value.loc[:, ["gini29"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI_ORDER_I": ["gini29"]}, 1)
        .values
    )
    value.loc[:, ["gini30"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI_ORDER_I": ["gini30"]}, 1)
        .values
    )
    value.loc[:, ["gini31"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI_ORDER_I": ["gini31"]}, 1)
        .values
    )
    value.loc[:, ["gini32"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI_ORDER_I": ["gini32"]}, 1)
        .values
    )
    value.loc[:, ["gini33"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI_ORDER_I": ["gini33"]}, 1)
        .values
    )
    value.loc[:, ["gini34"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI_ORDER_I": ["gini34"]}, 1)
        .values
    )
    value.loc[:, ["gini35"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI_ORDER_I": ["gini35"]}, 1)
        .values
    )
    value.loc[:, ["gini36"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI_ORDER_I": ["gini36"]}, 1)
        .values
    )
    value.loc[:, ["gini37"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI_ORDER_I": ["gini37"]}, 1)
        .values
    )
    value.loc[:, ["gini38"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI_ORDER_I": ["gini38"]}, 1)
        .values
    )
    value.loc[:, ["gini39"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI_ORDER_I": ["gini39"]}, 1)
        .values
    )
    value.loc[:, ["gini40"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI_ORDER_I": ["gini40"]}, 1)
        .values
    )
    value.loc[:, ["gini41"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini41"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI_ORDER_I": ["gini41"]}, 1)
        .values
    )
    value.loc[:, ["gini42"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini41"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini42"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI_ORDER_I": ["gini42"]}, 1)
        .values
    )
    value.loc[:, ["gini43"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini41"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini42"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini43"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI_ORDER_I": ["gini43"]}, 1)
        .values
    )
    value.loc[:, ["gini44"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini41"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini42"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini43"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini44"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI_ORDER_I": ["gini44"]}, 1)
        .values
    )
    value.loc[:, ["gini45"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini41"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini42"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini43"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini44"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini45"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI_ORDER_I": ["gini45"]}, 1)
        .values
    )
    value.loc[:, ["gini46"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini41"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini42"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini43"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini44"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini45"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini46"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI_ORDER_I": ["gini46"]}, 1)
        .values
    )
    value.loc[:, ["gini47"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini41"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini42"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini43"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini44"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini45"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini46"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini47"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI_ORDER_I": ["gini47"]}, 1)
        .values
    )
    value.loc[:, ["gini48"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini41"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini42"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini43"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini44"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini45"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini46"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini47"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini48"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI_ORDER_I": ["gini48"]}, 1)
        .values
    )
    value.loc[:, ["gini49"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini41"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini42"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini43"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini44"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini45"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini46"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini47"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini48"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini49"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI_ORDER_I": ["gini49"]}, 1)
        .values
    )
    value.loc[:, ["gini50"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini41"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini42"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini43"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini44"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini45"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini46"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini47"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini48"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini49"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini50"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI_ORDER_I": ["gini50"]}, 1)
        .values
    )
    value.loc[:, ["gini51"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini41"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini42"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini43"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini44"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini45"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini46"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini47"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini48"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini49"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini50"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini51"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI_ORDER_I": ["gini51"]}, 1)
        .values
    )
    value.loc[:, ["gini52"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini41"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini42"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini43"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini44"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini45"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini46"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini47"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini48"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini49"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini50"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini51"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini52"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI_ORDER_I": ["gini52"]}, 1)
        .values
    )
    value.loc[:, ["gini53"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini41"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini42"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini43"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini44"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini45"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini46"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini47"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini48"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini49"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini50"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini51"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini52"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini53"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI_ORDER_I": ["gini53"]}, 1)
        .values
    )
    value.loc[:, ["gini54"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini41"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini42"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini43"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini44"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini45"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini46"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini47"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini48"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini49"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini50"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini51"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini52"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini53"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini54"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI_ORDER_I": ["gini54"]}, 1)
        .values
    )
    value.loc[:, ["gini55"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini41"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini42"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini43"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini44"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini45"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini46"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini47"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini48"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini49"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini50"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini51"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini52"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini53"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini54"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini55"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI_ORDER_I": ["gini55"]}, 1)
        .values
    )
    value.loc[:, ["gini56"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini41"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini42"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini43"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini44"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini45"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini46"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini47"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini48"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini49"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini50"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini51"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini52"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini53"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini54"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini55"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini56"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI_ORDER_I": ["gini56"]}, 1)
        .values
    )
    value.loc[:, ["gini57"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini41"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini42"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini43"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini44"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini45"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini46"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini47"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini48"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini49"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini50"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini51"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini52"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini53"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini54"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini55"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini56"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini57"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI_ORDER_I": ["gini57"]}, 1)
        .values
    )
    value.loc[:, ["gini58"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini41"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini42"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini43"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini44"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini45"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini46"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini47"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini48"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini49"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini50"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini51"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini52"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini53"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini54"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini55"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini56"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini57"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini58"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI_ORDER_I": ["gini58"]}, 1)
        .values
    )
    value.loc[:, ["gini59"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini41"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini42"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini43"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini44"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini45"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini46"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini47"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini48"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini49"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini50"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini51"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini52"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini53"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini54"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini55"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini56"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini57"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini58"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini59"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI_ORDER_I": ["gini59"]}, 1)
        .values
    )
    value.loc[:, ["gini60"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini41"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini42"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini43"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini44"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini45"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini46"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini47"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini48"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini49"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini50"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini51"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini52"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini53"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini54"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini55"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini56"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini57"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini58"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini59"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini60"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI_ORDER_I": ["gini60"]}, 1)
        .values
    )
    value.loc[:, ["gini61"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini41"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini42"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini43"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini44"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini45"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini46"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini47"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini48"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini49"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini50"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini51"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini52"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini53"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini54"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini55"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini56"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini57"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini58"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini59"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini60"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini61"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI_ORDER_I": ["gini61"]}, 1)
        .values
    )
    return value


@component.add(
    name="households_disposable_income_ordered",
    units="$/Year",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"households_disposable_income": 1},
)
def households_disposable_income_ordered():
    """
    households disposable income ordered
    """
    return vector_sort_order(households_disposable_income(), 1)


@component.add(
    name="households_disposable_income_share_ordered",
    units="DMNL",
    subscripts=["REGIONS_35_I", "GINI_ORDER_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "households_disposable_income_shares": 1,
        "households_disposable_income_ordered": 1,
    },
)
def households_disposable_income_share_ordered():
    """
    share of disposable income of each households type on total disposable income, ordered
    """
    return vector_reorder(
        xr.DataArray(
            households_disposable_income_shares().values,
            {
                "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                "GINI_ORDER_I": _subscript_dict["GINI_ORDER_I"],
            },
            ["REGIONS_35_I", "GINI_ORDER_I"],
        ),
        xr.DataArray(
            households_disposable_income_ordered().values,
            {
                "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                "GINI_ORDER_I": _subscript_dict["GINI_ORDER_I"],
            },
            ["REGIONS_35_I", "GINI_ORDER_I"],
        ),
    )


@component.add(
    name="households_disposable_income_shares",
    units="DMNL",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "households_disposable_income": 2,
        "number_of_households_by_income_and_type": 2,
    },
)
def households_disposable_income_shares():
    return zidz(
        households_disposable_income() * number_of_households_by_income_and_type(),
        sum(
            households_disposable_income().rename({"HOUSEHOLDS_I": "HOUSEHOLDS_I!"})
            * number_of_households_by_income_and_type().rename(
                {"HOUSEHOLDS_I": "HOUSEHOLDS_I!"}
            ),
            dim=["HOUSEHOLDS_I!"],
        ).expand_dims({"HOUSEHOLDS_I": _subscript_dict["HOUSEHOLDS_I"]}, 1),
    )


@component.add(
    name="households_shares",
    units="DMNL",
    subscripts=["REGIONS_35_I", "HOUSEHOLDS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"number_of_households_by_income_and_type": 2},
)
def households_shares():
    """
    share of each household type on total households by region
    """
    return number_of_households_by_income_and_type() / sum(
        number_of_households_by_income_and_type().rename(
            {"HOUSEHOLDS_I": "HOUSEHOLDS_I!"}
        ),
        dim=["HOUSEHOLDS_I!"],
    )


@component.add(
    name="households_shares_ordered",
    units="DMNL",
    subscripts=["REGIONS_35_I", "GINI_ORDER_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"households_shares": 1, "households_disposable_income_ordered": 1},
)
def households_shares_ordered():
    """
    share of each household type ordered according to income level
    """
    return vector_reorder(
        xr.DataArray(
            households_shares().values,
            {
                "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                "GINI_ORDER_I": _subscript_dict["GINI_ORDER_I"],
            },
            ["REGIONS_35_I", "GINI_ORDER_I"],
        ),
        xr.DataArray(
            households_disposable_income_ordered().values,
            {
                "REGIONS_35_I": _subscript_dict["REGIONS_35_I"],
                "GINI_ORDER_I": _subscript_dict["GINI_ORDER_I"],
            },
            ["REGIONS_35_I", "GINI_ORDER_I"],
        ),
    )


@component.add(
    name="pop_shares_eu27",
    units="1",
    subscripts=["REGIONS_EU27_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"population_35_regions": 2},
)
def pop_shares_eu27():
    return population_35_regions().loc[_subscript_dict["REGIONS_EU27_I"]].rename(
        {"REGIONS_35_I": "REGIONS_EU27_I"}
    ) / sum(
        population_35_regions()
        .loc[_subscript_dict["REGIONS_EU27_I"]]
        .rename({"REGIONS_35_I": "REGIONS_EU27_I!"}),
        dim=["REGIONS_EU27_I!"],
    )


@component.add(
    name="pop_shares_eu27_gini",
    units="1",
    subscripts=["FGINI_EU_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"pop_shares_eu27": 27},
)
def pop_shares_eu27_gini():
    value = xr.DataArray(
        np.nan, {"FGINI_EU_I": _subscript_dict["FGINI_EU_I"]}, ["FGINI_EU_I"]
    )
    value.loc[["FGINI_EU1"]] = float(pop_shares_eu27().loc["AUSTRIA"])
    value.loc[["FGINI_EU2"]] = float(pop_shares_eu27().loc["BELGIUM"])
    value.loc[["FGINI_EU3"]] = float(pop_shares_eu27().loc["BULGARIA"])
    value.loc[["FGINI_EU4"]] = float(pop_shares_eu27().loc["CROATIA"])
    value.loc[["FGINI_EU5"]] = float(pop_shares_eu27().loc["CYPRUS"])
    value.loc[["FGINI_EU6"]] = float(pop_shares_eu27().loc["CZECH_REPUBLIC"])
    value.loc[["FGINI_EU7"]] = float(pop_shares_eu27().loc["DENMARK"])
    value.loc[["FGINI_EU8"]] = float(pop_shares_eu27().loc["ESTONIA"])
    value.loc[["FGINI_EU9"]] = float(pop_shares_eu27().loc["FINLAND"])
    value.loc[["FGINI_EU10"]] = float(pop_shares_eu27().loc["FRANCE"])
    value.loc[["FGINI_EU11"]] = float(pop_shares_eu27().loc["GERMANY"])
    value.loc[["FGINI_EU12"]] = float(pop_shares_eu27().loc["GREECE"])
    value.loc[["FGINI_EU13"]] = float(pop_shares_eu27().loc["HUNGARY"])
    value.loc[["FGINI_EU14"]] = float(pop_shares_eu27().loc["IRELAND"])
    value.loc[["FGINI_EU15"]] = float(pop_shares_eu27().loc["ITALY"])
    value.loc[["FGINI_EU16"]] = float(pop_shares_eu27().loc["LATVIA"])
    value.loc[["FGINI_EU17"]] = float(pop_shares_eu27().loc["LITHUANIA"])
    value.loc[["FGINI_EU18"]] = float(pop_shares_eu27().loc["LUXEMBOURG"])
    value.loc[["FGINI_EU19"]] = float(pop_shares_eu27().loc["MALTA"])
    value.loc[["FGINI_EU20"]] = float(pop_shares_eu27().loc["NETHERLANDS"])
    value.loc[["FGINI_EU21"]] = float(pop_shares_eu27().loc["POLAND"])
    value.loc[["FGINI_EU22"]] = float(pop_shares_eu27().loc["PORTUGAL"])
    value.loc[["FGINI_EU23"]] = float(pop_shares_eu27().loc["ROMANIA"])
    value.loc[["FGINI_EU24"]] = float(pop_shares_eu27().loc["SLOVAKIA"])
    value.loc[["FGINI_EU25"]] = float(pop_shares_eu27().loc["SLOVENIA"])
    value.loc[["FGINI_EU26"]] = float(pop_shares_eu27().loc["SPAIN"])
    value.loc[["FGINI_EU27"]] = float(pop_shares_eu27().loc["SWEDEN"])
    return value


@component.add(
    name="pop_shares_EU27_ordered",
    units="1",
    subscripts=["SGINI_EU_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"pop_shares_eu27_gini": 1, "gdp_pc_eu27_ordered": 1},
)
def pop_shares_eu27_ordered():
    return vector_reorder(
        xr.DataArray(
            pop_shares_eu27_gini().values,
            {"SGINI_EU_I": _subscript_dict["SGINI_EU_I"]},
            ["SGINI_EU_I"],
        ),
        xr.DataArray(
            gdp_pc_eu27_ordered().values,
            {"SGINI_EU_I": _subscript_dict["SGINI_EU_I"]},
            ["SGINI_EU_I"],
        ),
    )


@component.add(
    name="pop_shares_regions",
    units="1",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"population_9_regions": 2},
)
def pop_shares_regions():
    """
    calculating each region's share of world population
    """
    return population_9_regions() / sum(
        population_9_regions().rename({"REGIONS_9_I": "REGIONS_9_I!"}),
        dim=["REGIONS_9_I!"],
    )


@component.add(
    name="pop_shares_regions_gini",
    units="1",
    subscripts=["FGINI_REGIONS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"pop_shares_regions": 9},
)
def pop_shares_regions_gini():
    """
    constructing a new vector with the population shares
    """
    value = xr.DataArray(
        np.nan,
        {"FGINI_REGIONS_I": _subscript_dict["FGINI_REGIONS_I"]},
        ["FGINI_REGIONS_I"],
    )
    value.loc[["FGINI_REGION1"]] = float(pop_shares_regions().loc["EU27"])
    value.loc[["FGINI_REGION2"]] = float(pop_shares_regions().loc["UK"])
    value.loc[["FGINI_REGION3"]] = float(pop_shares_regions().loc["CHINA"])
    value.loc[["FGINI_REGION4"]] = float(pop_shares_regions().loc["EASOC"])
    value.loc[["FGINI_REGION5"]] = float(pop_shares_regions().loc["INDIA"])
    value.loc[["FGINI_REGION6"]] = float(pop_shares_regions().loc["LATAM"])
    value.loc[["FGINI_REGION7"]] = float(pop_shares_regions().loc["RUSSIA"])
    value.loc[["FGINI_REGION8"]] = float(pop_shares_regions().loc["USMCA"])
    value.loc[["FGINI_REGION9"]] = float(pop_shares_regions().loc["LROW"])
    return value


@component.add(
    name="pop_shares_regions_ordered",
    units="1",
    subscripts=["SGINI_REGIONS_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"pop_shares_regions_gini": 1, "gdppc_region_ordered": 1},
)
def pop_shares_regions_ordered():
    """
    order vector containing the population shares, beginning with the region with the smallest GDP p.c.
    """
    return vector_reorder(
        xr.DataArray(
            pop_shares_regions_gini().values,
            {"SGINI_REGIONS_I": _subscript_dict["SGINI_REGIONS_I"]},
            ["SGINI_REGIONS_I"],
        ),
        xr.DataArray(
            gdppc_region_ordered().values,
            {"SGINI_REGIONS_I": _subscript_dict["SGINI_REGIONS_I"]},
            ["SGINI_REGIONS_I"],
        ),
    )
