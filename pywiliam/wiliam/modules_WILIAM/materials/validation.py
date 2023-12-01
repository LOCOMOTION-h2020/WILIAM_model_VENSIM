"""
Module materials.validation
Translated using PySD version 3.10.0
"""


@component.add(
    name="Fe_PRICE_HISTORICAL_0",
    units="$/t",
    comp_type="Auxiliary",
    comp_subtype="with Lookup",
    depends_on={"time": 1},
)
def fe_price_historical_0():
    """
    Iron and Steel Scrap Price in dollars per ton. Iron and Steel Scrap - Historical Statistics (Data Series 140) USGS https://www.usgs.gov/media/files/iron-and-steel-scrap-historical-statistics-data-seri es-140 ds140-iron-steel-scrap-2019.xlsx
    """
    return np.interp(
        time(),
        [
            2005.0,
            2006.0,
            2007.0,
            2008.0,
            2009.0,
            2010.0,
            2011.0,
            2012.0,
            2013.0,
            2014.0,
            2015.0,
            2016.0,
            2017.0,
            2018.0,
            2019.0,
        ],
        [
            192.0,
            219.0,
            250.0,
            351.0,
            204.0,
            326.0,
            411.0,
            367.0,
            365.0,
            351.0,
            213.0,
            196.0,
            266.0,
            323.0,
            249.22,
        ],
    )
