"""
Module energy.land_requirements
Translated using PySD version 3.10.0
"""


@component.add(
    name="AVERAGE_REGIONAL_LATITUDE_SOLAR_PV_BY_EROI_MIN",
    units="arcdegree",
    subscripts=["REGIONS_36_I", "EROI_MIN_POTENTIAL_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_average_regional_latitude_solar_pv_by_eroi_min"
    },
)
def average_regional_latitude_solar_pv_by_eroi_min():
    """
    Average of latitudes which belong to solar PV potential for each model region. Given the dependence of the solar potencial on EROImin (which is an hypothesis selected by the model users when running it), different latitude-average are considered. For the sake of simplicity, static values are computed for the year 2015 with panel PV efficiency of 15%, hence we assume that in general more panels will be located in more sunny locations.
    """
    return _ext_constant_average_regional_latitude_solar_pv_by_eroi_min()


_ext_constant_average_regional_latitude_solar_pv_by_eroi_min = ExtConstant(
    "model_parameters/energy/energy-potentials.xlsx",
    "PROTRA",
    "AVERAGE_REGIONAL_LATITUDE_SOLAR_PV_POTENTIAL_BY_EROI_MIN",
    {
        "REGIONS_36_I": _subscript_dict["REGIONS_36_I"],
        "EROI_MIN_POTENTIAL_I": _subscript_dict["EROI_MIN_POTENTIAL_I"],
    },
    _root,
    {
        "REGIONS_36_I": _subscript_dict["REGIONS_36_I"],
        "EROI_MIN_POTENTIAL_I": _subscript_dict["EROI_MIN_POTENTIAL_I"],
    },
    "_ext_constant_average_regional_latitude_solar_pv_by_eroi_min",
)


@component.add(
    name="AVERAGE_REGOINAL_LATITUDE_SOLAR_PV_EROImin",
    units="radians",
    subscripts=["REGIONS_36_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_eroi_min_potential_wind_solar_sp": 8,
        "average_regional_latitude_solar_pv_by_eroi_min": 8,
        "radians_per_arcdegree": 1,
    },
)
def average_regoinal_latitude_solar_pv_eroimin():
    """
    Average regional latitude for computing solar PV land occupation ratio depending on the level of EROI minimum.
    """
    return np.abs(
        if_then_else(
            select_eroi_min_potential_wind_solar_sp() == 0,
            lambda: average_regional_latitude_solar_pv_by_eroi_min()
            .loc[:, "EROI_MIN_0"]
            .reset_coords(drop=True),
            lambda: if_then_else(
                select_eroi_min_potential_wind_solar_sp() == 2,
                lambda: average_regional_latitude_solar_pv_by_eroi_min()
                .loc[:, "EROI_MIN_2_1"]
                .reset_coords(drop=True),
                lambda: if_then_else(
                    select_eroi_min_potential_wind_solar_sp() == 3,
                    lambda: average_regional_latitude_solar_pv_by_eroi_min()
                    .loc[:, "EROI_MIN_3_1"]
                    .reset_coords(drop=True),
                    lambda: if_then_else(
                        select_eroi_min_potential_wind_solar_sp() == 5,
                        lambda: average_regional_latitude_solar_pv_by_eroi_min()
                        .loc[:, "EROI_MIN_5_1"]
                        .reset_coords(drop=True),
                        lambda: if_then_else(
                            select_eroi_min_potential_wind_solar_sp() == 8,
                            lambda: average_regional_latitude_solar_pv_by_eroi_min()
                            .loc[:, "EROI_MIN_8_1"]
                            .reset_coords(drop=True),
                            lambda: if_then_else(
                                select_eroi_min_potential_wind_solar_sp() == 10,
                                lambda: average_regional_latitude_solar_pv_by_eroi_min()
                                .loc[:, "EROI_MIN_10_1"]
                                .reset_coords(drop=True),
                                lambda: if_then_else(
                                    select_eroi_min_potential_wind_solar_sp() == 12,
                                    lambda: average_regional_latitude_solar_pv_by_eroi_min()
                                    .loc[:, "EROI_MIN_12_1"]
                                    .reset_coords(drop=True),
                                    lambda: if_then_else(
                                        select_eroi_min_potential_wind_solar_sp() == 15,
                                        lambda: average_regional_latitude_solar_pv_by_eroi_min()
                                        .loc[:, "EROI_MIN_15_1"]
                                        .reset_coords(drop=True),
                                        lambda: xr.DataArray(
                                            np.nan,
                                            {
                                                "REGIONS_36_I": _subscript_dict[
                                                    "REGIONS_36_I"
                                                ]
                                            },
                                            ["REGIONS_36_I"],
                                        ),
                                    ),
                                ),
                            ),
                        ),
                    ),
                ),
            ),
        )
        * radians_per_arcdegree()
    )


@component.add(
    name="DELAY_land_use_efficiency_PROTRA",
    units="MW/km2",
    subscripts=["REGIONS_9_I", "NRG_PROTRA_I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={
        "_delayfixed_delay_land_use_efficiency_protra": 1,
        "_delayfixed_delay_land_use_efficiency_protra_1": 1,
        "_delayfixed_delay_land_use_efficiency_protra_2": 1,
        "_delayfixed_delay_land_use_efficiency_protra_3": 1,
        "_delayfixed_delay_land_use_efficiency_protra_4": 1,
        "_delayfixed_delay_land_use_efficiency_protra_5": 1,
        "_delayfixed_delay_land_use_efficiency_protra_6": 1,
        "_delayfixed_delay_land_use_efficiency_protra_7": 1,
        "_delayfixed_delay_land_use_efficiency_protra_8": 1,
        "_delayfixed_delay_land_use_efficiency_protra_9": 1,
        "_delayfixed_delay_land_use_efficiency_protra_10": 1,
        "_delayfixed_delay_land_use_efficiency_protra_11": 1,
        "_delayfixed_delay_land_use_efficiency_protra_12": 1,
        "_delayfixed_delay_land_use_efficiency_protra_13": 1,
        "_delayfixed_delay_land_use_efficiency_protra_14": 1,
        "_delayfixed_delay_land_use_efficiency_protra_15": 1,
        "_delayfixed_delay_land_use_efficiency_protra_16": 1,
        "_delayfixed_delay_land_use_efficiency_protra_17": 1,
        "_delayfixed_delay_land_use_efficiency_protra_18": 1,
        "_delayfixed_delay_land_use_efficiency_protra_19": 1,
        "_delayfixed_delay_land_use_efficiency_protra_20": 1,
        "_delayfixed_delay_land_use_efficiency_protra_21": 1,
        "_delayfixed_delay_land_use_efficiency_protra_22": 1,
        "_delayfixed_delay_land_use_efficiency_protra_23": 1,
        "_delayfixed_delay_land_use_efficiency_protra_24": 1,
        "_delayfixed_delay_land_use_efficiency_protra_25": 1,
        "_delayfixed_delay_land_use_efficiency_protra_26": 1,
        "_delayfixed_delay_land_use_efficiency_protra_27": 1,
        "_delayfixed_delay_land_use_efficiency_protra_28": 1,
        "_delayfixed_delay_land_use_efficiency_protra_29": 1,
        "_delayfixed_delay_land_use_efficiency_protra_30": 1,
        "_delayfixed_delay_land_use_efficiency_protra_31": 1,
        "_delayfixed_delay_land_use_efficiency_protra_32": 1,
        "_delayfixed_delay_land_use_efficiency_protra_33": 1,
        "_delayfixed_delay_land_use_efficiency_protra_34": 1,
        "_delayfixed_delay_land_use_efficiency_protra_35": 1,
        "_delayfixed_delay_land_use_efficiency_protra_36": 1,
        "_delayfixed_delay_land_use_efficiency_protra_37": 1,
        "_delayfixed_delay_land_use_efficiency_protra_38": 1,
        "_delayfixed_delay_land_use_efficiency_protra_39": 1,
        "_delayfixed_delay_land_use_efficiency_protra_40": 1,
        "_delayfixed_delay_land_use_efficiency_protra_41": 1,
        "_delayfixed_delay_land_use_efficiency_protra_42": 1,
        "_delayfixed_delay_land_use_efficiency_protra_43": 1,
        "_delayfixed_delay_land_use_efficiency_protra_44": 1,
        "_delayfixed_delay_land_use_efficiency_protra_45": 1,
        "_delayfixed_delay_land_use_efficiency_protra_46": 1,
        "_delayfixed_delay_land_use_efficiency_protra_47": 1,
        "_delayfixed_delay_land_use_efficiency_protra_48": 1,
        "_delayfixed_delay_land_use_efficiency_protra_49": 1,
        "_delayfixed_delay_land_use_efficiency_protra_50": 1,
        "_delayfixed_delay_land_use_efficiency_protra_51": 1,
        "_delayfixed_delay_land_use_efficiency_protra_52": 1,
        "_delayfixed_delay_land_use_efficiency_protra_53": 1,
        "_delayfixed_delay_land_use_efficiency_protra_54": 1,
        "_delayfixed_delay_land_use_efficiency_protra_55": 1,
        "_delayfixed_delay_land_use_efficiency_protra_56": 1,
        "_delayfixed_delay_land_use_efficiency_protra_57": 1,
        "_delayfixed_delay_land_use_efficiency_protra_58": 1,
        "_delayfixed_delay_land_use_efficiency_protra_59": 1,
        "_delayfixed_delay_land_use_efficiency_protra_60": 1,
        "_delayfixed_delay_land_use_efficiency_protra_61": 1,
        "_delayfixed_delay_land_use_efficiency_protra_62": 1,
        "_delayfixed_delay_land_use_efficiency_protra_63": 1,
        "_delayfixed_delay_land_use_efficiency_protra_64": 1,
        "_delayfixed_delay_land_use_efficiency_protra_65": 1,
        "_delayfixed_delay_land_use_efficiency_protra_66": 1,
        "_delayfixed_delay_land_use_efficiency_protra_67": 1,
        "_delayfixed_delay_land_use_efficiency_protra_68": 1,
        "_delayfixed_delay_land_use_efficiency_protra_69": 1,
        "_delayfixed_delay_land_use_efficiency_protra_70": 1,
        "_delayfixed_delay_land_use_efficiency_protra_71": 1,
        "_delayfixed_delay_land_use_efficiency_protra_72": 1,
        "_delayfixed_delay_land_use_efficiency_protra_73": 1,
        "_delayfixed_delay_land_use_efficiency_protra_74": 1,
        "_delayfixed_delay_land_use_efficiency_protra_75": 1,
        "_delayfixed_delay_land_use_efficiency_protra_76": 1,
        "_delayfixed_delay_land_use_efficiency_protra_77": 1,
        "_delayfixed_delay_land_use_efficiency_protra_78": 1,
        "_delayfixed_delay_land_use_efficiency_protra_79": 1,
        "_delayfixed_delay_land_use_efficiency_protra_80": 1,
        "_delayfixed_delay_land_use_efficiency_protra_81": 1,
        "_delayfixed_delay_land_use_efficiency_protra_82": 1,
        "_delayfixed_delay_land_use_efficiency_protra_83": 1,
        "_delayfixed_delay_land_use_efficiency_protra_84": 1,
        "_delayfixed_delay_land_use_efficiency_protra_85": 1,
        "_delayfixed_delay_land_use_efficiency_protra_86": 1,
        "_delayfixed_delay_land_use_efficiency_protra_87": 1,
        "_delayfixed_delay_land_use_efficiency_protra_88": 1,
        "_delayfixed_delay_land_use_efficiency_protra_89": 1,
        "_delayfixed_delay_land_use_efficiency_protra_90": 1,
        "_delayfixed_delay_land_use_efficiency_protra_91": 1,
        "_delayfixed_delay_land_use_efficiency_protra_92": 1,
        "_delayfixed_delay_land_use_efficiency_protra_93": 1,
        "_delayfixed_delay_land_use_efficiency_protra_94": 1,
        "_delayfixed_delay_land_use_efficiency_protra_95": 1,
        "_delayfixed_delay_land_use_efficiency_protra_96": 1,
        "_delayfixed_delay_land_use_efficiency_protra_97": 1,
        "_delayfixed_delay_land_use_efficiency_protra_98": 1,
        "_delayfixed_delay_land_use_efficiency_protra_99": 1,
        "_delayfixed_delay_land_use_efficiency_protra_100": 1,
        "_delayfixed_delay_land_use_efficiency_protra_101": 1,
        "_delayfixed_delay_land_use_efficiency_protra_102": 1,
        "_delayfixed_delay_land_use_efficiency_protra_103": 1,
        "_delayfixed_delay_land_use_efficiency_protra_104": 1,
        "_delayfixed_delay_land_use_efficiency_protra_105": 1,
        "_delayfixed_delay_land_use_efficiency_protra_106": 1,
        "_delayfixed_delay_land_use_efficiency_protra_107": 1,
        "_delayfixed_delay_land_use_efficiency_protra_108": 1,
        "_delayfixed_delay_land_use_efficiency_protra_109": 1,
        "_delayfixed_delay_land_use_efficiency_protra_110": 1,
        "_delayfixed_delay_land_use_efficiency_protra_111": 1,
        "_delayfixed_delay_land_use_efficiency_protra_112": 1,
        "_delayfixed_delay_land_use_efficiency_protra_113": 1,
        "_delayfixed_delay_land_use_efficiency_protra_114": 1,
        "_delayfixed_delay_land_use_efficiency_protra_115": 1,
        "_delayfixed_delay_land_use_efficiency_protra_116": 1,
        "_delayfixed_delay_land_use_efficiency_protra_117": 1,
        "_delayfixed_delay_land_use_efficiency_protra_118": 1,
        "_delayfixed_delay_land_use_efficiency_protra_119": 1,
        "_delayfixed_delay_land_use_efficiency_protra_120": 1,
        "_delayfixed_delay_land_use_efficiency_protra_121": 1,
        "_delayfixed_delay_land_use_efficiency_protra_122": 1,
        "_delayfixed_delay_land_use_efficiency_protra_123": 1,
        "_delayfixed_delay_land_use_efficiency_protra_124": 1,
        "_delayfixed_delay_land_use_efficiency_protra_125": 1,
        "_delayfixed_delay_land_use_efficiency_protra_126": 1,
        "_delayfixed_delay_land_use_efficiency_protra_127": 1,
        "_delayfixed_delay_land_use_efficiency_protra_128": 1,
        "_delayfixed_delay_land_use_efficiency_protra_129": 1,
        "_delayfixed_delay_land_use_efficiency_protra_130": 1,
        "_delayfixed_delay_land_use_efficiency_protra_131": 1,
        "_delayfixed_delay_land_use_efficiency_protra_132": 1,
        "_delayfixed_delay_land_use_efficiency_protra_133": 1,
        "_delayfixed_delay_land_use_efficiency_protra_134": 1,
        "_delayfixed_delay_land_use_efficiency_protra_135": 1,
        "_delayfixed_delay_land_use_efficiency_protra_136": 1,
        "_delayfixed_delay_land_use_efficiency_protra_137": 1,
        "_delayfixed_delay_land_use_efficiency_protra_138": 1,
        "_delayfixed_delay_land_use_efficiency_protra_139": 1,
        "_delayfixed_delay_land_use_efficiency_protra_140": 1,
        "_delayfixed_delay_land_use_efficiency_protra_141": 1,
        "_delayfixed_delay_land_use_efficiency_protra_142": 1,
        "_delayfixed_delay_land_use_efficiency_protra_143": 1,
        "_delayfixed_delay_land_use_efficiency_protra_144": 1,
        "_delayfixed_delay_land_use_efficiency_protra_145": 1,
        "_delayfixed_delay_land_use_efficiency_protra_146": 1,
        "_delayfixed_delay_land_use_efficiency_protra_147": 1,
        "_delayfixed_delay_land_use_efficiency_protra_148": 1,
        "_delayfixed_delay_land_use_efficiency_protra_149": 1,
        "_delayfixed_delay_land_use_efficiency_protra_150": 1,
        "_delayfixed_delay_land_use_efficiency_protra_151": 1,
        "_delayfixed_delay_land_use_efficiency_protra_152": 1,
        "_delayfixed_delay_land_use_efficiency_protra_153": 1,
        "_delayfixed_delay_land_use_efficiency_protra_154": 1,
        "_delayfixed_delay_land_use_efficiency_protra_155": 1,
        "_delayfixed_delay_land_use_efficiency_protra_156": 1,
        "_delayfixed_delay_land_use_efficiency_protra_157": 1,
        "_delayfixed_delay_land_use_efficiency_protra_158": 1,
        "_delayfixed_delay_land_use_efficiency_protra_159": 1,
        "_delayfixed_delay_land_use_efficiency_protra_160": 1,
        "_delayfixed_delay_land_use_efficiency_protra_161": 1,
        "_delayfixed_delay_land_use_efficiency_protra_162": 1,
        "_delayfixed_delay_land_use_efficiency_protra_163": 1,
        "_delayfixed_delay_land_use_efficiency_protra_164": 1,
        "_delayfixed_delay_land_use_efficiency_protra_165": 1,
        "_delayfixed_delay_land_use_efficiency_protra_166": 1,
        "_delayfixed_delay_land_use_efficiency_protra_167": 1,
        "_delayfixed_delay_land_use_efficiency_protra_168": 1,
        "_delayfixed_delay_land_use_efficiency_protra_169": 1,
        "_delayfixed_delay_land_use_efficiency_protra_170": 1,
        "_delayfixed_delay_land_use_efficiency_protra_171": 1,
        "_delayfixed_delay_land_use_efficiency_protra_172": 1,
        "_delayfixed_delay_land_use_efficiency_protra_173": 1,
        "_delayfixed_delay_land_use_efficiency_protra_174": 1,
        "_delayfixed_delay_land_use_efficiency_protra_175": 1,
        "_delayfixed_delay_land_use_efficiency_protra_176": 1,
        "_delayfixed_delay_land_use_efficiency_protra_177": 1,
        "_delayfixed_delay_land_use_efficiency_protra_178": 1,
        "_delayfixed_delay_land_use_efficiency_protra_179": 1,
        "_delayfixed_delay_land_use_efficiency_protra_180": 1,
        "_delayfixed_delay_land_use_efficiency_protra_181": 1,
        "_delayfixed_delay_land_use_efficiency_protra_182": 1,
        "_delayfixed_delay_land_use_efficiency_protra_183": 1,
        "_delayfixed_delay_land_use_efficiency_protra_184": 1,
        "_delayfixed_delay_land_use_efficiency_protra_185": 1,
        "_delayfixed_delay_land_use_efficiency_protra_186": 1,
        "_delayfixed_delay_land_use_efficiency_protra_187": 1,
        "_delayfixed_delay_land_use_efficiency_protra_188": 1,
        "_delayfixed_delay_land_use_efficiency_protra_189": 1,
        "_delayfixed_delay_land_use_efficiency_protra_190": 1,
        "_delayfixed_delay_land_use_efficiency_protra_191": 1,
        "_delayfixed_delay_land_use_efficiency_protra_192": 1,
        "_delayfixed_delay_land_use_efficiency_protra_193": 1,
        "_delayfixed_delay_land_use_efficiency_protra_194": 1,
        "_delayfixed_delay_land_use_efficiency_protra_195": 1,
        "_delayfixed_delay_land_use_efficiency_protra_196": 1,
        "_delayfixed_delay_land_use_efficiency_protra_197": 1,
        "_delayfixed_delay_land_use_efficiency_protra_198": 1,
        "_delayfixed_delay_land_use_efficiency_protra_199": 1,
        "_delayfixed_delay_land_use_efficiency_protra_200": 1,
        "_delayfixed_delay_land_use_efficiency_protra_201": 1,
        "_delayfixed_delay_land_use_efficiency_protra_202": 1,
        "_delayfixed_delay_land_use_efficiency_protra_203": 1,
        "_delayfixed_delay_land_use_efficiency_protra_204": 1,
        "_delayfixed_delay_land_use_efficiency_protra_205": 1,
        "_delayfixed_delay_land_use_efficiency_protra_206": 1,
        "_delayfixed_delay_land_use_efficiency_protra_207": 1,
        "_delayfixed_delay_land_use_efficiency_protra_208": 1,
        "_delayfixed_delay_land_use_efficiency_protra_209": 1,
        "_delayfixed_delay_land_use_efficiency_protra_210": 1,
        "_delayfixed_delay_land_use_efficiency_protra_211": 1,
        "_delayfixed_delay_land_use_efficiency_protra_212": 1,
        "_delayfixed_delay_land_use_efficiency_protra_213": 1,
        "_delayfixed_delay_land_use_efficiency_protra_214": 1,
        "_delayfixed_delay_land_use_efficiency_protra_215": 1,
        "_delayfixed_delay_land_use_efficiency_protra_216": 1,
        "_delayfixed_delay_land_use_efficiency_protra_217": 1,
        "_delayfixed_delay_land_use_efficiency_protra_218": 1,
        "_delayfixed_delay_land_use_efficiency_protra_219": 1,
        "_delayfixed_delay_land_use_efficiency_protra_220": 1,
        "_delayfixed_delay_land_use_efficiency_protra_221": 1,
        "_delayfixed_delay_land_use_efficiency_protra_222": 1,
        "_delayfixed_delay_land_use_efficiency_protra_223": 1,
        "_delayfixed_delay_land_use_efficiency_protra_224": 1,
        "_delayfixed_delay_land_use_efficiency_protra_225": 1,
        "_delayfixed_delay_land_use_efficiency_protra_226": 1,
        "_delayfixed_delay_land_use_efficiency_protra_227": 1,
        "_delayfixed_delay_land_use_efficiency_protra_228": 1,
        "_delayfixed_delay_land_use_efficiency_protra_229": 1,
        "_delayfixed_delay_land_use_efficiency_protra_230": 1,
        "_delayfixed_delay_land_use_efficiency_protra_231": 1,
        "_delayfixed_delay_land_use_efficiency_protra_232": 1,
        "_delayfixed_delay_land_use_efficiency_protra_233": 1,
        "_delayfixed_delay_land_use_efficiency_protra_234": 1,
        "_delayfixed_delay_land_use_efficiency_protra_235": 1,
        "_delayfixed_delay_land_use_efficiency_protra_236": 1,
        "_delayfixed_delay_land_use_efficiency_protra_237": 1,
        "_delayfixed_delay_land_use_efficiency_protra_238": 1,
        "_delayfixed_delay_land_use_efficiency_protra_239": 1,
        "_delayfixed_delay_land_use_efficiency_protra_240": 1,
        "_delayfixed_delay_land_use_efficiency_protra_241": 1,
        "_delayfixed_delay_land_use_efficiency_protra_242": 1,
        "_delayfixed_delay_land_use_efficiency_protra_243": 1,
        "_delayfixed_delay_land_use_efficiency_protra_244": 1,
        "_delayfixed_delay_land_use_efficiency_protra_245": 1,
        "_delayfixed_delay_land_use_efficiency_protra_246": 1,
        "_delayfixed_delay_land_use_efficiency_protra_247": 1,
        "_delayfixed_delay_land_use_efficiency_protra_248": 1,
        "_delayfixed_delay_land_use_efficiency_protra_249": 1,
        "_delayfixed_delay_land_use_efficiency_protra_250": 1,
        "_delayfixed_delay_land_use_efficiency_protra_251": 1,
        "_delayfixed_delay_land_use_efficiency_protra_252": 1,
        "_delayfixed_delay_land_use_efficiency_protra_253": 1,
        "_delayfixed_delay_land_use_efficiency_protra_254": 1,
        "_delayfixed_delay_land_use_efficiency_protra_255": 1,
        "_delayfixed_delay_land_use_efficiency_protra_256": 1,
        "_delayfixed_delay_land_use_efficiency_protra_257": 1,
        "_delayfixed_delay_land_use_efficiency_protra_258": 1,
        "_delayfixed_delay_land_use_efficiency_protra_259": 1,
        "_delayfixed_delay_land_use_efficiency_protra_260": 1,
        "_delayfixed_delay_land_use_efficiency_protra_261": 1,
        "_delayfixed_delay_land_use_efficiency_protra_262": 1,
        "_delayfixed_delay_land_use_efficiency_protra_263": 1,
        "_delayfixed_delay_land_use_efficiency_protra_264": 1,
        "_delayfixed_delay_land_use_efficiency_protra_265": 1,
        "_delayfixed_delay_land_use_efficiency_protra_266": 1,
        "_delayfixed_delay_land_use_efficiency_protra_267": 1,
        "_delayfixed_delay_land_use_efficiency_protra_268": 1,
        "_delayfixed_delay_land_use_efficiency_protra_269": 1,
        "_delayfixed_delay_land_use_efficiency_protra_270": 1,
        "_delayfixed_delay_land_use_efficiency_protra_271": 1,
        "_delayfixed_delay_land_use_efficiency_protra_272": 1,
        "_delayfixed_delay_land_use_efficiency_protra_273": 1,
        "_delayfixed_delay_land_use_efficiency_protra_274": 1,
        "_delayfixed_delay_land_use_efficiency_protra_275": 1,
        "_delayfixed_delay_land_use_efficiency_protra_276": 1,
        "_delayfixed_delay_land_use_efficiency_protra_277": 1,
        "_delayfixed_delay_land_use_efficiency_protra_278": 1,
        "_delayfixed_delay_land_use_efficiency_protra_279": 1,
        "_delayfixed_delay_land_use_efficiency_protra_280": 1,
        "_delayfixed_delay_land_use_efficiency_protra_281": 1,
        "_delayfixed_delay_land_use_efficiency_protra_282": 1,
        "_delayfixed_delay_land_use_efficiency_protra_283": 1,
        "_delayfixed_delay_land_use_efficiency_protra_284": 1,
        "_delayfixed_delay_land_use_efficiency_protra_285": 1,
        "_delayfixed_delay_land_use_efficiency_protra_286": 1,
        "_delayfixed_delay_land_use_efficiency_protra_287": 1,
        "_delayfixed_delay_land_use_efficiency_protra_288": 1,
        "_delayfixed_delay_land_use_efficiency_protra_289": 1,
        "_delayfixed_delay_land_use_efficiency_protra_290": 1,
        "_delayfixed_delay_land_use_efficiency_protra_291": 1,
        "_delayfixed_delay_land_use_efficiency_protra_292": 1,
        "_delayfixed_delay_land_use_efficiency_protra_293": 1,
        "_delayfixed_delay_land_use_efficiency_protra_294": 1,
        "_delayfixed_delay_land_use_efficiency_protra_295": 1,
        "_delayfixed_delay_land_use_efficiency_protra_296": 1,
        "_delayfixed_delay_land_use_efficiency_protra_297": 1,
        "_delayfixed_delay_land_use_efficiency_protra_298": 1,
        "_delayfixed_delay_land_use_efficiency_protra_299": 1,
        "_delayfixed_delay_land_use_efficiency_protra_300": 1,
        "_delayfixed_delay_land_use_efficiency_protra_301": 1,
        "_delayfixed_delay_land_use_efficiency_protra_302": 1,
        "_delayfixed_delay_land_use_efficiency_protra_303": 1,
        "_delayfixed_delay_land_use_efficiency_protra_304": 1,
        "_delayfixed_delay_land_use_efficiency_protra_305": 1,
        "_delayfixed_delay_land_use_efficiency_protra_306": 1,
        "_delayfixed_delay_land_use_efficiency_protra_307": 1,
        "_delayfixed_delay_land_use_efficiency_protra_308": 1,
        "_delayfixed_delay_land_use_efficiency_protra_309": 1,
        "_delayfixed_delay_land_use_efficiency_protra_310": 1,
        "_delayfixed_delay_land_use_efficiency_protra_311": 1,
        "_delayfixed_delay_land_use_efficiency_protra_312": 1,
        "_delayfixed_delay_land_use_efficiency_protra_313": 1,
        "_delayfixed_delay_land_use_efficiency_protra_314": 1,
        "_delayfixed_delay_land_use_efficiency_protra_315": 1,
        "_delayfixed_delay_land_use_efficiency_protra_316": 1,
        "_delayfixed_delay_land_use_efficiency_protra_317": 1,
        "_delayfixed_delay_land_use_efficiency_protra_318": 1,
        "_delayfixed_delay_land_use_efficiency_protra_319": 1,
        "_delayfixed_delay_land_use_efficiency_protra_320": 1,
        "_delayfixed_delay_land_use_efficiency_protra_321": 1,
        "_delayfixed_delay_land_use_efficiency_protra_322": 1,
        "_delayfixed_delay_land_use_efficiency_protra_323": 1,
        "_delayfixed_delay_land_use_efficiency_protra_324": 1,
        "_delayfixed_delay_land_use_efficiency_protra_325": 1,
        "_delayfixed_delay_land_use_efficiency_protra_326": 1,
        "_delayfixed_delay_land_use_efficiency_protra_327": 1,
        "_delayfixed_delay_land_use_efficiency_protra_328": 1,
        "_delayfixed_delay_land_use_efficiency_protra_329": 1,
        "_delayfixed_delay_land_use_efficiency_protra_330": 1,
        "_delayfixed_delay_land_use_efficiency_protra_331": 1,
        "_delayfixed_delay_land_use_efficiency_protra_332": 1,
        "_delayfixed_delay_land_use_efficiency_protra_333": 1,
        "_delayfixed_delay_land_use_efficiency_protra_334": 1,
        "_delayfixed_delay_land_use_efficiency_protra_335": 1,
        "_delayfixed_delay_land_use_efficiency_protra_336": 1,
        "_delayfixed_delay_land_use_efficiency_protra_337": 1,
        "_delayfixed_delay_land_use_efficiency_protra_338": 1,
        "_delayfixed_delay_land_use_efficiency_protra_339": 1,
        "_delayfixed_delay_land_use_efficiency_protra_340": 1,
        "_delayfixed_delay_land_use_efficiency_protra_341": 1,
        "_delayfixed_delay_land_use_efficiency_protra_342": 1,
        "_delayfixed_delay_land_use_efficiency_protra_343": 1,
        "_delayfixed_delay_land_use_efficiency_protra_344": 1,
        "_delayfixed_delay_land_use_efficiency_protra_345": 1,
        "_delayfixed_delay_land_use_efficiency_protra_346": 1,
        "_delayfixed_delay_land_use_efficiency_protra_347": 1,
        "_delayfixed_delay_land_use_efficiency_protra_348": 1,
        "_delayfixed_delay_land_use_efficiency_protra_349": 1,
        "_delayfixed_delay_land_use_efficiency_protra_350": 1,
        "_delayfixed_delay_land_use_efficiency_protra_351": 1,
        "_delayfixed_delay_land_use_efficiency_protra_352": 1,
        "_delayfixed_delay_land_use_efficiency_protra_353": 1,
        "_delayfixed_delay_land_use_efficiency_protra_354": 1,
        "_delayfixed_delay_land_use_efficiency_protra_355": 1,
        "_delayfixed_delay_land_use_efficiency_protra_356": 1,
        "_delayfixed_delay_land_use_efficiency_protra_357": 1,
        "_delayfixed_delay_land_use_efficiency_protra_358": 1,
        "_delayfixed_delay_land_use_efficiency_protra_359": 1,
        "_delayfixed_delay_land_use_efficiency_protra_360": 1,
        "_delayfixed_delay_land_use_efficiency_protra_361": 1,
        "_delayfixed_delay_land_use_efficiency_protra_362": 1,
        "_delayfixed_delay_land_use_efficiency_protra_363": 1,
        "_delayfixed_delay_land_use_efficiency_protra_364": 1,
        "_delayfixed_delay_land_use_efficiency_protra_365": 1,
        "_delayfixed_delay_land_use_efficiency_protra_366": 1,
        "_delayfixed_delay_land_use_efficiency_protra_367": 1,
        "_delayfixed_delay_land_use_efficiency_protra_368": 1,
        "_delayfixed_delay_land_use_efficiency_protra_369": 1,
        "_delayfixed_delay_land_use_efficiency_protra_370": 1,
        "_delayfixed_delay_land_use_efficiency_protra_371": 1,
        "_delayfixed_delay_land_use_efficiency_protra_372": 1,
        "_delayfixed_delay_land_use_efficiency_protra_373": 1,
        "_delayfixed_delay_land_use_efficiency_protra_374": 1,
        "_delayfixed_delay_land_use_efficiency_protra_375": 1,
        "_delayfixed_delay_land_use_efficiency_protra_376": 1,
        "_delayfixed_delay_land_use_efficiency_protra_377": 1,
    },
    other_deps={
        "_delayfixed_delay_land_use_efficiency_protra": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_1": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_2": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_3": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_4": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_5": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_6": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_7": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_8": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_9": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_10": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_11": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_12": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_13": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_14": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_15": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_16": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_17": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_18": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_19": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_20": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_21": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_22": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_23": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_24": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_25": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_26": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_27": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_28": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_29": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_30": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_31": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_32": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_33": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_34": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_35": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_36": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_37": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_38": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_39": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_40": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_41": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_42": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_43": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_44": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_45": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_46": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_47": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_48": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_49": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_50": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_51": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_52": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_53": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_54": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_55": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_56": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_57": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_58": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_59": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_60": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_61": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_62": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_63": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_64": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_65": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_66": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_67": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_68": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_69": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_70": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_71": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_72": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_73": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_74": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_75": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_76": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_77": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_78": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_79": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_80": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_81": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_82": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_83": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_84": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_85": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_86": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_87": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_88": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_89": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_90": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_91": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_92": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_93": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_94": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_95": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_96": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_97": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_98": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_99": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_100": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_101": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_102": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_103": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_104": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_105": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_106": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_107": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_108": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_109": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_110": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_111": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_112": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_113": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_114": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_115": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_116": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_117": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_118": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_119": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_120": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_121": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_122": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_123": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_124": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_125": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_126": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_127": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_128": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_129": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_130": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_131": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_132": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_133": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_134": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_135": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_136": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_137": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_138": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_139": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_140": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_141": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_142": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_143": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_144": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_145": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_146": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_147": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_148": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_149": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_150": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_151": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_152": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_153": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_154": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_155": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_156": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_157": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_158": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_159": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_160": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_161": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_162": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_163": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_164": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_165": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_166": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_167": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_168": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_169": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_170": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_171": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_172": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_173": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_174": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_175": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_176": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_177": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_178": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_179": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_180": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_181": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_182": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_183": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_184": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_185": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_186": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_187": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_188": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_189": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_190": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_191": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_192": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_193": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_194": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_195": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_196": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_197": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_198": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_199": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_200": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_201": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_202": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_203": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_204": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_205": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_206": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_207": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_208": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_209": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_210": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_211": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_212": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_213": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_214": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_215": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_216": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_217": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_218": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_219": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_220": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_221": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_222": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_223": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_224": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_225": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_226": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_227": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_228": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_229": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_230": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_231": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_232": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_233": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_234": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_235": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_236": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_237": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_238": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_239": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_240": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_241": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_242": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_243": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_244": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_245": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_246": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_247": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_248": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_249": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_250": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_251": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_252": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_253": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_254": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_255": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_256": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_257": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_258": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_259": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_260": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_261": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_262": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_263": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_264": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_265": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_266": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_267": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_268": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_269": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_270": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_271": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_272": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_273": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_274": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_275": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_276": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_277": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_278": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_279": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_280": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_281": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_282": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_283": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_284": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_285": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_286": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_287": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_288": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_289": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_290": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_291": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_292": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_293": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_294": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_295": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_296": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_297": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_298": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_299": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_300": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_301": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_302": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_303": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_304": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_305": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_306": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_307": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_308": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_309": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_310": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_311": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_312": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_313": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_314": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_315": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_316": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_317": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_318": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_319": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_320": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_321": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_322": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_323": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_324": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_325": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_326": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_327": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_328": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_329": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_330": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_331": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_332": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_333": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_334": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_335": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_336": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_337": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_338": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_339": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_340": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_341": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_342": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_343": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_344": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_345": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_346": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_347": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_348": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_349": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_350": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_351": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_352": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_353": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_354": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_355": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_356": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_357": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_358": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_359": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_360": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_361": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_362": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_363": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_364": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_365": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_366": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_367": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_368": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_369": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_370": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_371": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_372": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_373": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_374": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_375": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_376": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
        "_delayfixed_delay_land_use_efficiency_protra_377": {
            "initial": {"land_use_efficiency_protra": 1, "protra_lifetime": 1},
            "step": {"land_use_efficiency_protra": 1},
        },
    },
)
def delay_land_use_efficiency_protra():
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
        },
        ["REGIONS_9_I", "NRG_PROTRA_I"],
    )
    value.loc[
        ["EU27"], ["PROTRA_CHP_gas_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra().values
    value.loc[
        ["EU27"], ["PROTRA_CHP_gas_fuels_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_1().values
    value.loc[
        ["EU27"], ["PROTRA_CHP_geothermal_DEACTIVATED"]
    ] = _delayfixed_delay_land_use_efficiency_protra_2().values
    value.loc[
        ["EU27"], ["PROTRA_CHP_liquid_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_3().values
    value.loc[
        ["EU27"], ["PROTRA_CHP_liquid_fuels_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_4().values
    value.loc[
        ["EU27"], ["PROTRA_CHP_solid_fossil"]
    ] = _delayfixed_delay_land_use_efficiency_protra_5().values
    value.loc[
        ["EU27"], ["PROTRA_CHP_solid_fossil_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_6().values
    value.loc[
        ["EU27"], ["PROTRA_CHP_waste"]
    ] = _delayfixed_delay_land_use_efficiency_protra_7().values
    value.loc[
        ["EU27"], ["PROTRA_CHP_solid_bio"]
    ] = _delayfixed_delay_land_use_efficiency_protra_8().values
    value.loc[
        ["EU27"], ["PROTRA_CHP_solid_bio_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_9().values
    value.loc[
        ["EU27"], ["PROTRA_HP_gas_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_10().values
    value.loc[
        ["EU27"], ["PROTRA_HP_solid_bio"]
    ] = _delayfixed_delay_land_use_efficiency_protra_11().values
    value.loc[
        ["EU27"], ["PROTRA_HP_geothermal"]
    ] = _delayfixed_delay_land_use_efficiency_protra_12().values
    value.loc[
        ["EU27"], ["PROTRA_HP_liquid_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_13().values
    value.loc[
        ["EU27"], ["PROTRA_HP_solar_DEACTIVATED"]
    ] = _delayfixed_delay_land_use_efficiency_protra_14().values
    value.loc[
        ["EU27"], ["PROTRA_HP_solid_fossil"]
    ] = _delayfixed_delay_land_use_efficiency_protra_15().values
    value.loc[
        ["EU27"], ["PROTRA_HP_waste"]
    ] = _delayfixed_delay_land_use_efficiency_protra_16().values
    value.loc[
        ["EU27"], ["PROTRA_PP_solid_bio"]
    ] = _delayfixed_delay_land_use_efficiency_protra_17().values
    value.loc[
        ["EU27"], ["PROTRA_PP_solid_bio_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_18().values
    value.loc[
        ["EU27"], ["PROTRA_PP_gas_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_19().values
    value.loc[
        ["EU27"], ["PROTRA_PP_gas_fuels_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_20().values
    value.loc[
        ["EU27"], ["PROTRA_PP_geothermal"]
    ] = _delayfixed_delay_land_use_efficiency_protra_21().values
    value.loc[
        ["EU27"], ["PROTRA_PP_hydropower_dammed"]
    ] = _delayfixed_delay_land_use_efficiency_protra_22().values
    value.loc[
        ["EU27"], ["PROTRA_PP_hydropower_run_of_river"]
    ] = _delayfixed_delay_land_use_efficiency_protra_23().values
    value.loc[
        ["EU27"], ["PROTRA_PP_liquid_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_24().values
    value.loc[
        ["EU27"], ["PROTRA_PP_liquid_fuels_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_25().values
    value.loc[
        ["EU27"], ["PROTRA_PP_nuclear"]
    ] = _delayfixed_delay_land_use_efficiency_protra_26().values
    value.loc[
        ["EU27"], ["PROTRA_PP_oceanic"]
    ] = _delayfixed_delay_land_use_efficiency_protra_27().values
    value.loc[
        ["EU27"], ["PROTRA_PP_solar_CSP"]
    ] = _delayfixed_delay_land_use_efficiency_protra_28().values
    value.loc[
        ["EU27"], ["PROTRA_PP_solar_open_space_PV"]
    ] = _delayfixed_delay_land_use_efficiency_protra_29().values
    value.loc[
        ["EU27"], ["PROTRA_PP_solar_urban_PV"]
    ] = _delayfixed_delay_land_use_efficiency_protra_30().values
    value.loc[
        ["EU27"], ["PROTRA_PP_solid_fossil"]
    ] = _delayfixed_delay_land_use_efficiency_protra_31().values
    value.loc[
        ["EU27"], ["PROTRA_PP_solid_fossil_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_32().values
    value.loc[
        ["EU27"], ["PROTRA_PP_waste"]
    ] = _delayfixed_delay_land_use_efficiency_protra_33().values
    value.loc[
        ["EU27"], ["PROTRA_PP_waste_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_34().values
    value.loc[
        ["EU27"], ["PROTRA_PP_wind_offshore"]
    ] = _delayfixed_delay_land_use_efficiency_protra_35().values
    value.loc[
        ["EU27"], ["PROTRA_PP_wind_onshore"]
    ] = _delayfixed_delay_land_use_efficiency_protra_36().values
    value.loc[
        ["EU27"], ["PROTRA_blending_gas_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_37().values
    value.loc[
        ["EU27"], ["PROTRA_blending_liquid_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_38().values
    value.loc[
        ["EU27"], ["PROTRA_no_process_TI_hydrogen"]
    ] = _delayfixed_delay_land_use_efficiency_protra_39().values
    value.loc[
        ["EU27"], ["PROTRA_no_process_TI_solid_bio"]
    ] = _delayfixed_delay_land_use_efficiency_protra_40().values
    value.loc[
        ["EU27"], ["PROTRA_no_process_TI_solid_fossil"]
    ] = _delayfixed_delay_land_use_efficiency_protra_41().values
    value.loc[
        ["UK"], ["PROTRA_CHP_gas_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_42().values
    value.loc[
        ["UK"], ["PROTRA_CHP_gas_fuels_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_43().values
    value.loc[
        ["UK"], ["PROTRA_CHP_geothermal_DEACTIVATED"]
    ] = _delayfixed_delay_land_use_efficiency_protra_44().values
    value.loc[
        ["UK"], ["PROTRA_CHP_liquid_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_45().values
    value.loc[
        ["UK"], ["PROTRA_CHP_liquid_fuels_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_46().values
    value.loc[
        ["UK"], ["PROTRA_CHP_solid_fossil"]
    ] = _delayfixed_delay_land_use_efficiency_protra_47().values
    value.loc[
        ["UK"], ["PROTRA_CHP_solid_fossil_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_48().values
    value.loc[
        ["UK"], ["PROTRA_CHP_waste"]
    ] = _delayfixed_delay_land_use_efficiency_protra_49().values
    value.loc[
        ["UK"], ["PROTRA_CHP_solid_bio"]
    ] = _delayfixed_delay_land_use_efficiency_protra_50().values
    value.loc[
        ["UK"], ["PROTRA_CHP_solid_bio_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_51().values
    value.loc[
        ["UK"], ["PROTRA_HP_gas_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_52().values
    value.loc[
        ["UK"], ["PROTRA_HP_solid_bio"]
    ] = _delayfixed_delay_land_use_efficiency_protra_53().values
    value.loc[
        ["UK"], ["PROTRA_HP_geothermal"]
    ] = _delayfixed_delay_land_use_efficiency_protra_54().values
    value.loc[
        ["UK"], ["PROTRA_HP_liquid_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_55().values
    value.loc[
        ["UK"], ["PROTRA_HP_solar_DEACTIVATED"]
    ] = _delayfixed_delay_land_use_efficiency_protra_56().values
    value.loc[
        ["UK"], ["PROTRA_HP_solid_fossil"]
    ] = _delayfixed_delay_land_use_efficiency_protra_57().values
    value.loc[
        ["UK"], ["PROTRA_HP_waste"]
    ] = _delayfixed_delay_land_use_efficiency_protra_58().values
    value.loc[
        ["UK"], ["PROTRA_PP_solid_bio"]
    ] = _delayfixed_delay_land_use_efficiency_protra_59().values
    value.loc[
        ["UK"], ["PROTRA_PP_solid_bio_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_60().values
    value.loc[
        ["UK"], ["PROTRA_PP_gas_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_61().values
    value.loc[
        ["UK"], ["PROTRA_PP_gas_fuels_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_62().values
    value.loc[
        ["UK"], ["PROTRA_PP_geothermal"]
    ] = _delayfixed_delay_land_use_efficiency_protra_63().values
    value.loc[
        ["UK"], ["PROTRA_PP_hydropower_dammed"]
    ] = _delayfixed_delay_land_use_efficiency_protra_64().values
    value.loc[
        ["UK"], ["PROTRA_PP_hydropower_run_of_river"]
    ] = _delayfixed_delay_land_use_efficiency_protra_65().values
    value.loc[
        ["UK"], ["PROTRA_PP_liquid_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_66().values
    value.loc[
        ["UK"], ["PROTRA_PP_liquid_fuels_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_67().values
    value.loc[
        ["UK"], ["PROTRA_PP_nuclear"]
    ] = _delayfixed_delay_land_use_efficiency_protra_68().values
    value.loc[
        ["UK"], ["PROTRA_PP_oceanic"]
    ] = _delayfixed_delay_land_use_efficiency_protra_69().values
    value.loc[
        ["UK"], ["PROTRA_PP_solar_CSP"]
    ] = _delayfixed_delay_land_use_efficiency_protra_70().values
    value.loc[
        ["UK"], ["PROTRA_PP_solar_open_space_PV"]
    ] = _delayfixed_delay_land_use_efficiency_protra_71().values
    value.loc[
        ["UK"], ["PROTRA_PP_solar_urban_PV"]
    ] = _delayfixed_delay_land_use_efficiency_protra_72().values
    value.loc[
        ["UK"], ["PROTRA_PP_solid_fossil"]
    ] = _delayfixed_delay_land_use_efficiency_protra_73().values
    value.loc[
        ["UK"], ["PROTRA_PP_solid_fossil_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_74().values
    value.loc[
        ["UK"], ["PROTRA_PP_waste"]
    ] = _delayfixed_delay_land_use_efficiency_protra_75().values
    value.loc[
        ["UK"], ["PROTRA_PP_waste_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_76().values
    value.loc[
        ["UK"], ["PROTRA_PP_wind_offshore"]
    ] = _delayfixed_delay_land_use_efficiency_protra_77().values
    value.loc[
        ["UK"], ["PROTRA_PP_wind_onshore"]
    ] = _delayfixed_delay_land_use_efficiency_protra_78().values
    value.loc[
        ["UK"], ["PROTRA_blending_gas_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_79().values
    value.loc[
        ["UK"], ["PROTRA_blending_liquid_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_80().values
    value.loc[
        ["UK"], ["PROTRA_no_process_TI_hydrogen"]
    ] = _delayfixed_delay_land_use_efficiency_protra_81().values
    value.loc[
        ["UK"], ["PROTRA_no_process_TI_solid_bio"]
    ] = _delayfixed_delay_land_use_efficiency_protra_82().values
    value.loc[
        ["UK"], ["PROTRA_no_process_TI_solid_fossil"]
    ] = _delayfixed_delay_land_use_efficiency_protra_83().values
    value.loc[
        ["CHINA"], ["PROTRA_CHP_gas_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_84().values
    value.loc[
        ["CHINA"], ["PROTRA_CHP_gas_fuels_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_85().values
    value.loc[
        ["CHINA"], ["PROTRA_CHP_geothermal_DEACTIVATED"]
    ] = _delayfixed_delay_land_use_efficiency_protra_86().values
    value.loc[
        ["CHINA"], ["PROTRA_CHP_liquid_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_87().values
    value.loc[
        ["CHINA"], ["PROTRA_CHP_liquid_fuels_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_88().values
    value.loc[
        ["CHINA"], ["PROTRA_CHP_solid_fossil"]
    ] = _delayfixed_delay_land_use_efficiency_protra_89().values
    value.loc[
        ["CHINA"], ["PROTRA_CHP_solid_fossil_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_90().values
    value.loc[
        ["CHINA"], ["PROTRA_CHP_waste"]
    ] = _delayfixed_delay_land_use_efficiency_protra_91().values
    value.loc[
        ["CHINA"], ["PROTRA_CHP_solid_bio"]
    ] = _delayfixed_delay_land_use_efficiency_protra_92().values
    value.loc[
        ["CHINA"], ["PROTRA_CHP_solid_bio_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_93().values
    value.loc[
        ["CHINA"], ["PROTRA_HP_gas_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_94().values
    value.loc[
        ["CHINA"], ["PROTRA_HP_solid_bio"]
    ] = _delayfixed_delay_land_use_efficiency_protra_95().values
    value.loc[
        ["CHINA"], ["PROTRA_HP_geothermal"]
    ] = _delayfixed_delay_land_use_efficiency_protra_96().values
    value.loc[
        ["CHINA"], ["PROTRA_HP_liquid_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_97().values
    value.loc[
        ["CHINA"], ["PROTRA_HP_solar_DEACTIVATED"]
    ] = _delayfixed_delay_land_use_efficiency_protra_98().values
    value.loc[
        ["CHINA"], ["PROTRA_HP_solid_fossil"]
    ] = _delayfixed_delay_land_use_efficiency_protra_99().values
    value.loc[
        ["CHINA"], ["PROTRA_HP_waste"]
    ] = _delayfixed_delay_land_use_efficiency_protra_100().values
    value.loc[
        ["CHINA"], ["PROTRA_PP_solid_bio"]
    ] = _delayfixed_delay_land_use_efficiency_protra_101().values
    value.loc[
        ["CHINA"], ["PROTRA_PP_solid_bio_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_102().values
    value.loc[
        ["CHINA"], ["PROTRA_PP_gas_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_103().values
    value.loc[
        ["CHINA"], ["PROTRA_PP_gas_fuels_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_104().values
    value.loc[
        ["CHINA"], ["PROTRA_PP_geothermal"]
    ] = _delayfixed_delay_land_use_efficiency_protra_105().values
    value.loc[
        ["CHINA"], ["PROTRA_PP_hydropower_dammed"]
    ] = _delayfixed_delay_land_use_efficiency_protra_106().values
    value.loc[
        ["CHINA"], ["PROTRA_PP_hydropower_run_of_river"]
    ] = _delayfixed_delay_land_use_efficiency_protra_107().values
    value.loc[
        ["CHINA"], ["PROTRA_PP_liquid_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_108().values
    value.loc[
        ["CHINA"], ["PROTRA_PP_liquid_fuels_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_109().values
    value.loc[
        ["CHINA"], ["PROTRA_PP_nuclear"]
    ] = _delayfixed_delay_land_use_efficiency_protra_110().values
    value.loc[
        ["CHINA"], ["PROTRA_PP_oceanic"]
    ] = _delayfixed_delay_land_use_efficiency_protra_111().values
    value.loc[
        ["CHINA"], ["PROTRA_PP_solar_CSP"]
    ] = _delayfixed_delay_land_use_efficiency_protra_112().values
    value.loc[
        ["CHINA"], ["PROTRA_PP_solar_open_space_PV"]
    ] = _delayfixed_delay_land_use_efficiency_protra_113().values
    value.loc[
        ["CHINA"], ["PROTRA_PP_solar_urban_PV"]
    ] = _delayfixed_delay_land_use_efficiency_protra_114().values
    value.loc[
        ["CHINA"], ["PROTRA_PP_solid_fossil"]
    ] = _delayfixed_delay_land_use_efficiency_protra_115().values
    value.loc[
        ["CHINA"], ["PROTRA_PP_solid_fossil_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_116().values
    value.loc[
        ["CHINA"], ["PROTRA_PP_waste"]
    ] = _delayfixed_delay_land_use_efficiency_protra_117().values
    value.loc[
        ["CHINA"], ["PROTRA_PP_waste_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_118().values
    value.loc[
        ["CHINA"], ["PROTRA_PP_wind_offshore"]
    ] = _delayfixed_delay_land_use_efficiency_protra_119().values
    value.loc[
        ["CHINA"], ["PROTRA_PP_wind_onshore"]
    ] = _delayfixed_delay_land_use_efficiency_protra_120().values
    value.loc[
        ["CHINA"], ["PROTRA_blending_gas_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_121().values
    value.loc[
        ["CHINA"], ["PROTRA_blending_liquid_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_122().values
    value.loc[
        ["CHINA"], ["PROTRA_no_process_TI_hydrogen"]
    ] = _delayfixed_delay_land_use_efficiency_protra_123().values
    value.loc[
        ["CHINA"], ["PROTRA_no_process_TI_solid_bio"]
    ] = _delayfixed_delay_land_use_efficiency_protra_124().values
    value.loc[
        ["CHINA"], ["PROTRA_no_process_TI_solid_fossil"]
    ] = _delayfixed_delay_land_use_efficiency_protra_125().values
    value.loc[
        ["EASOC"], ["PROTRA_CHP_gas_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_126().values
    value.loc[
        ["EASOC"], ["PROTRA_CHP_gas_fuels_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_127().values
    value.loc[
        ["EASOC"], ["PROTRA_CHP_geothermal_DEACTIVATED"]
    ] = _delayfixed_delay_land_use_efficiency_protra_128().values
    value.loc[
        ["EASOC"], ["PROTRA_CHP_liquid_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_129().values
    value.loc[
        ["EASOC"], ["PROTRA_CHP_liquid_fuels_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_130().values
    value.loc[
        ["EASOC"], ["PROTRA_CHP_solid_fossil"]
    ] = _delayfixed_delay_land_use_efficiency_protra_131().values
    value.loc[
        ["EASOC"], ["PROTRA_CHP_solid_fossil_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_132().values
    value.loc[
        ["EASOC"], ["PROTRA_CHP_waste"]
    ] = _delayfixed_delay_land_use_efficiency_protra_133().values
    value.loc[
        ["EASOC"], ["PROTRA_CHP_solid_bio"]
    ] = _delayfixed_delay_land_use_efficiency_protra_134().values
    value.loc[
        ["EASOC"], ["PROTRA_CHP_solid_bio_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_135().values
    value.loc[
        ["EASOC"], ["PROTRA_HP_gas_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_136().values
    value.loc[
        ["EASOC"], ["PROTRA_HP_solid_bio"]
    ] = _delayfixed_delay_land_use_efficiency_protra_137().values
    value.loc[
        ["EASOC"], ["PROTRA_HP_geothermal"]
    ] = _delayfixed_delay_land_use_efficiency_protra_138().values
    value.loc[
        ["EASOC"], ["PROTRA_HP_liquid_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_139().values
    value.loc[
        ["EASOC"], ["PROTRA_HP_solar_DEACTIVATED"]
    ] = _delayfixed_delay_land_use_efficiency_protra_140().values
    value.loc[
        ["EASOC"], ["PROTRA_HP_solid_fossil"]
    ] = _delayfixed_delay_land_use_efficiency_protra_141().values
    value.loc[
        ["EASOC"], ["PROTRA_HP_waste"]
    ] = _delayfixed_delay_land_use_efficiency_protra_142().values
    value.loc[
        ["EASOC"], ["PROTRA_PP_solid_bio"]
    ] = _delayfixed_delay_land_use_efficiency_protra_143().values
    value.loc[
        ["EASOC"], ["PROTRA_PP_solid_bio_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_144().values
    value.loc[
        ["EASOC"], ["PROTRA_PP_gas_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_145().values
    value.loc[
        ["EASOC"], ["PROTRA_PP_gas_fuels_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_146().values
    value.loc[
        ["EASOC"], ["PROTRA_PP_geothermal"]
    ] = _delayfixed_delay_land_use_efficiency_protra_147().values
    value.loc[
        ["EASOC"], ["PROTRA_PP_hydropower_dammed"]
    ] = _delayfixed_delay_land_use_efficiency_protra_148().values
    value.loc[
        ["EASOC"], ["PROTRA_PP_hydropower_run_of_river"]
    ] = _delayfixed_delay_land_use_efficiency_protra_149().values
    value.loc[
        ["EASOC"], ["PROTRA_PP_liquid_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_150().values
    value.loc[
        ["EASOC"], ["PROTRA_PP_liquid_fuels_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_151().values
    value.loc[
        ["EASOC"], ["PROTRA_PP_nuclear"]
    ] = _delayfixed_delay_land_use_efficiency_protra_152().values
    value.loc[
        ["EASOC"], ["PROTRA_PP_oceanic"]
    ] = _delayfixed_delay_land_use_efficiency_protra_153().values
    value.loc[
        ["EASOC"], ["PROTRA_PP_solar_CSP"]
    ] = _delayfixed_delay_land_use_efficiency_protra_154().values
    value.loc[
        ["EASOC"], ["PROTRA_PP_solar_open_space_PV"]
    ] = _delayfixed_delay_land_use_efficiency_protra_155().values
    value.loc[
        ["EASOC"], ["PROTRA_PP_solar_urban_PV"]
    ] = _delayfixed_delay_land_use_efficiency_protra_156().values
    value.loc[
        ["EASOC"], ["PROTRA_PP_solid_fossil"]
    ] = _delayfixed_delay_land_use_efficiency_protra_157().values
    value.loc[
        ["EASOC"], ["PROTRA_PP_solid_fossil_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_158().values
    value.loc[
        ["EASOC"], ["PROTRA_PP_waste"]
    ] = _delayfixed_delay_land_use_efficiency_protra_159().values
    value.loc[
        ["EASOC"], ["PROTRA_PP_waste_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_160().values
    value.loc[
        ["EASOC"], ["PROTRA_PP_wind_offshore"]
    ] = _delayfixed_delay_land_use_efficiency_protra_161().values
    value.loc[
        ["EASOC"], ["PROTRA_PP_wind_onshore"]
    ] = _delayfixed_delay_land_use_efficiency_protra_162().values
    value.loc[
        ["EASOC"], ["PROTRA_blending_gas_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_163().values
    value.loc[
        ["EASOC"], ["PROTRA_blending_liquid_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_164().values
    value.loc[
        ["EASOC"], ["PROTRA_no_process_TI_hydrogen"]
    ] = _delayfixed_delay_land_use_efficiency_protra_165().values
    value.loc[
        ["EASOC"], ["PROTRA_no_process_TI_solid_bio"]
    ] = _delayfixed_delay_land_use_efficiency_protra_166().values
    value.loc[
        ["EASOC"], ["PROTRA_no_process_TI_solid_fossil"]
    ] = _delayfixed_delay_land_use_efficiency_protra_167().values
    value.loc[
        ["INDIA"], ["PROTRA_CHP_gas_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_168().values
    value.loc[
        ["INDIA"], ["PROTRA_CHP_gas_fuels_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_169().values
    value.loc[
        ["INDIA"], ["PROTRA_CHP_geothermal_DEACTIVATED"]
    ] = _delayfixed_delay_land_use_efficiency_protra_170().values
    value.loc[
        ["INDIA"], ["PROTRA_CHP_liquid_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_171().values
    value.loc[
        ["INDIA"], ["PROTRA_CHP_liquid_fuels_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_172().values
    value.loc[
        ["INDIA"], ["PROTRA_CHP_solid_fossil"]
    ] = _delayfixed_delay_land_use_efficiency_protra_173().values
    value.loc[
        ["INDIA"], ["PROTRA_CHP_solid_fossil_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_174().values
    value.loc[
        ["INDIA"], ["PROTRA_CHP_waste"]
    ] = _delayfixed_delay_land_use_efficiency_protra_175().values
    value.loc[
        ["INDIA"], ["PROTRA_CHP_solid_bio"]
    ] = _delayfixed_delay_land_use_efficiency_protra_176().values
    value.loc[
        ["INDIA"], ["PROTRA_CHP_solid_bio_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_177().values
    value.loc[
        ["INDIA"], ["PROTRA_HP_gas_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_178().values
    value.loc[
        ["INDIA"], ["PROTRA_HP_solid_bio"]
    ] = _delayfixed_delay_land_use_efficiency_protra_179().values
    value.loc[
        ["INDIA"], ["PROTRA_HP_geothermal"]
    ] = _delayfixed_delay_land_use_efficiency_protra_180().values
    value.loc[
        ["INDIA"], ["PROTRA_HP_liquid_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_181().values
    value.loc[
        ["INDIA"], ["PROTRA_HP_solar_DEACTIVATED"]
    ] = _delayfixed_delay_land_use_efficiency_protra_182().values
    value.loc[
        ["INDIA"], ["PROTRA_HP_solid_fossil"]
    ] = _delayfixed_delay_land_use_efficiency_protra_183().values
    value.loc[
        ["INDIA"], ["PROTRA_HP_waste"]
    ] = _delayfixed_delay_land_use_efficiency_protra_184().values
    value.loc[
        ["INDIA"], ["PROTRA_PP_solid_bio"]
    ] = _delayfixed_delay_land_use_efficiency_protra_185().values
    value.loc[
        ["INDIA"], ["PROTRA_PP_solid_bio_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_186().values
    value.loc[
        ["INDIA"], ["PROTRA_PP_gas_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_187().values
    value.loc[
        ["INDIA"], ["PROTRA_PP_gas_fuels_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_188().values
    value.loc[
        ["INDIA"], ["PROTRA_PP_geothermal"]
    ] = _delayfixed_delay_land_use_efficiency_protra_189().values
    value.loc[
        ["INDIA"], ["PROTRA_PP_hydropower_dammed"]
    ] = _delayfixed_delay_land_use_efficiency_protra_190().values
    value.loc[
        ["INDIA"], ["PROTRA_PP_hydropower_run_of_river"]
    ] = _delayfixed_delay_land_use_efficiency_protra_191().values
    value.loc[
        ["INDIA"], ["PROTRA_PP_liquid_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_192().values
    value.loc[
        ["INDIA"], ["PROTRA_PP_liquid_fuels_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_193().values
    value.loc[
        ["INDIA"], ["PROTRA_PP_nuclear"]
    ] = _delayfixed_delay_land_use_efficiency_protra_194().values
    value.loc[
        ["INDIA"], ["PROTRA_PP_oceanic"]
    ] = _delayfixed_delay_land_use_efficiency_protra_195().values
    value.loc[
        ["INDIA"], ["PROTRA_PP_solar_CSP"]
    ] = _delayfixed_delay_land_use_efficiency_protra_196().values
    value.loc[
        ["INDIA"], ["PROTRA_PP_solar_open_space_PV"]
    ] = _delayfixed_delay_land_use_efficiency_protra_197().values
    value.loc[
        ["INDIA"], ["PROTRA_PP_solar_urban_PV"]
    ] = _delayfixed_delay_land_use_efficiency_protra_198().values
    value.loc[
        ["INDIA"], ["PROTRA_PP_solid_fossil"]
    ] = _delayfixed_delay_land_use_efficiency_protra_199().values
    value.loc[
        ["INDIA"], ["PROTRA_PP_solid_fossil_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_200().values
    value.loc[
        ["INDIA"], ["PROTRA_PP_waste"]
    ] = _delayfixed_delay_land_use_efficiency_protra_201().values
    value.loc[
        ["INDIA"], ["PROTRA_PP_waste_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_202().values
    value.loc[
        ["INDIA"], ["PROTRA_PP_wind_offshore"]
    ] = _delayfixed_delay_land_use_efficiency_protra_203().values
    value.loc[
        ["INDIA"], ["PROTRA_PP_wind_onshore"]
    ] = _delayfixed_delay_land_use_efficiency_protra_204().values
    value.loc[
        ["INDIA"], ["PROTRA_blending_gas_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_205().values
    value.loc[
        ["INDIA"], ["PROTRA_blending_liquid_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_206().values
    value.loc[
        ["INDIA"], ["PROTRA_no_process_TI_hydrogen"]
    ] = _delayfixed_delay_land_use_efficiency_protra_207().values
    value.loc[
        ["INDIA"], ["PROTRA_no_process_TI_solid_bio"]
    ] = _delayfixed_delay_land_use_efficiency_protra_208().values
    value.loc[
        ["INDIA"], ["PROTRA_no_process_TI_solid_fossil"]
    ] = _delayfixed_delay_land_use_efficiency_protra_209().values
    value.loc[
        ["LATAM"], ["PROTRA_CHP_gas_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_210().values
    value.loc[
        ["LATAM"], ["PROTRA_CHP_gas_fuels_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_211().values
    value.loc[
        ["LATAM"], ["PROTRA_CHP_geothermal_DEACTIVATED"]
    ] = _delayfixed_delay_land_use_efficiency_protra_212().values
    value.loc[
        ["LATAM"], ["PROTRA_CHP_liquid_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_213().values
    value.loc[
        ["LATAM"], ["PROTRA_CHP_liquid_fuels_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_214().values
    value.loc[
        ["LATAM"], ["PROTRA_CHP_solid_fossil"]
    ] = _delayfixed_delay_land_use_efficiency_protra_215().values
    value.loc[
        ["LATAM"], ["PROTRA_CHP_solid_fossil_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_216().values
    value.loc[
        ["LATAM"], ["PROTRA_CHP_waste"]
    ] = _delayfixed_delay_land_use_efficiency_protra_217().values
    value.loc[
        ["LATAM"], ["PROTRA_CHP_solid_bio"]
    ] = _delayfixed_delay_land_use_efficiency_protra_218().values
    value.loc[
        ["LATAM"], ["PROTRA_CHP_solid_bio_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_219().values
    value.loc[
        ["LATAM"], ["PROTRA_HP_gas_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_220().values
    value.loc[
        ["LATAM"], ["PROTRA_HP_solid_bio"]
    ] = _delayfixed_delay_land_use_efficiency_protra_221().values
    value.loc[
        ["LATAM"], ["PROTRA_HP_geothermal"]
    ] = _delayfixed_delay_land_use_efficiency_protra_222().values
    value.loc[
        ["LATAM"], ["PROTRA_HP_liquid_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_223().values
    value.loc[
        ["LATAM"], ["PROTRA_HP_solar_DEACTIVATED"]
    ] = _delayfixed_delay_land_use_efficiency_protra_224().values
    value.loc[
        ["LATAM"], ["PROTRA_HP_solid_fossil"]
    ] = _delayfixed_delay_land_use_efficiency_protra_225().values
    value.loc[
        ["LATAM"], ["PROTRA_HP_waste"]
    ] = _delayfixed_delay_land_use_efficiency_protra_226().values
    value.loc[
        ["LATAM"], ["PROTRA_PP_solid_bio"]
    ] = _delayfixed_delay_land_use_efficiency_protra_227().values
    value.loc[
        ["LATAM"], ["PROTRA_PP_solid_bio_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_228().values
    value.loc[
        ["LATAM"], ["PROTRA_PP_gas_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_229().values
    value.loc[
        ["LATAM"], ["PROTRA_PP_gas_fuels_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_230().values
    value.loc[
        ["LATAM"], ["PROTRA_PP_geothermal"]
    ] = _delayfixed_delay_land_use_efficiency_protra_231().values
    value.loc[
        ["LATAM"], ["PROTRA_PP_hydropower_dammed"]
    ] = _delayfixed_delay_land_use_efficiency_protra_232().values
    value.loc[
        ["LATAM"], ["PROTRA_PP_hydropower_run_of_river"]
    ] = _delayfixed_delay_land_use_efficiency_protra_233().values
    value.loc[
        ["LATAM"], ["PROTRA_PP_liquid_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_234().values
    value.loc[
        ["LATAM"], ["PROTRA_PP_liquid_fuels_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_235().values
    value.loc[
        ["LATAM"], ["PROTRA_PP_nuclear"]
    ] = _delayfixed_delay_land_use_efficiency_protra_236().values
    value.loc[
        ["LATAM"], ["PROTRA_PP_oceanic"]
    ] = _delayfixed_delay_land_use_efficiency_protra_237().values
    value.loc[
        ["LATAM"], ["PROTRA_PP_solar_CSP"]
    ] = _delayfixed_delay_land_use_efficiency_protra_238().values
    value.loc[
        ["LATAM"], ["PROTRA_PP_solar_open_space_PV"]
    ] = _delayfixed_delay_land_use_efficiency_protra_239().values
    value.loc[
        ["LATAM"], ["PROTRA_PP_solar_urban_PV"]
    ] = _delayfixed_delay_land_use_efficiency_protra_240().values
    value.loc[
        ["LATAM"], ["PROTRA_PP_solid_fossil"]
    ] = _delayfixed_delay_land_use_efficiency_protra_241().values
    value.loc[
        ["LATAM"], ["PROTRA_PP_solid_fossil_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_242().values
    value.loc[
        ["LATAM"], ["PROTRA_PP_waste"]
    ] = _delayfixed_delay_land_use_efficiency_protra_243().values
    value.loc[
        ["LATAM"], ["PROTRA_PP_waste_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_244().values
    value.loc[
        ["LATAM"], ["PROTRA_PP_wind_offshore"]
    ] = _delayfixed_delay_land_use_efficiency_protra_245().values
    value.loc[
        ["LATAM"], ["PROTRA_PP_wind_onshore"]
    ] = _delayfixed_delay_land_use_efficiency_protra_246().values
    value.loc[
        ["LATAM"], ["PROTRA_blending_gas_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_247().values
    value.loc[
        ["LATAM"], ["PROTRA_blending_liquid_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_248().values
    value.loc[
        ["LATAM"], ["PROTRA_no_process_TI_hydrogen"]
    ] = _delayfixed_delay_land_use_efficiency_protra_249().values
    value.loc[
        ["LATAM"], ["PROTRA_no_process_TI_solid_bio"]
    ] = _delayfixed_delay_land_use_efficiency_protra_250().values
    value.loc[
        ["LATAM"], ["PROTRA_no_process_TI_solid_fossil"]
    ] = _delayfixed_delay_land_use_efficiency_protra_251().values
    value.loc[
        ["RUSSIA"], ["PROTRA_CHP_gas_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_252().values
    value.loc[
        ["RUSSIA"], ["PROTRA_CHP_gas_fuels_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_253().values
    value.loc[
        ["RUSSIA"], ["PROTRA_CHP_geothermal_DEACTIVATED"]
    ] = _delayfixed_delay_land_use_efficiency_protra_254().values
    value.loc[
        ["RUSSIA"], ["PROTRA_CHP_liquid_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_255().values
    value.loc[
        ["RUSSIA"], ["PROTRA_CHP_liquid_fuels_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_256().values
    value.loc[
        ["RUSSIA"], ["PROTRA_CHP_solid_fossil"]
    ] = _delayfixed_delay_land_use_efficiency_protra_257().values
    value.loc[
        ["RUSSIA"], ["PROTRA_CHP_solid_fossil_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_258().values
    value.loc[
        ["RUSSIA"], ["PROTRA_CHP_waste"]
    ] = _delayfixed_delay_land_use_efficiency_protra_259().values
    value.loc[
        ["RUSSIA"], ["PROTRA_CHP_solid_bio"]
    ] = _delayfixed_delay_land_use_efficiency_protra_260().values
    value.loc[
        ["RUSSIA"], ["PROTRA_CHP_solid_bio_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_261().values
    value.loc[
        ["RUSSIA"], ["PROTRA_HP_gas_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_262().values
    value.loc[
        ["RUSSIA"], ["PROTRA_HP_solid_bio"]
    ] = _delayfixed_delay_land_use_efficiency_protra_263().values
    value.loc[
        ["RUSSIA"], ["PROTRA_HP_geothermal"]
    ] = _delayfixed_delay_land_use_efficiency_protra_264().values
    value.loc[
        ["RUSSIA"], ["PROTRA_HP_liquid_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_265().values
    value.loc[
        ["RUSSIA"], ["PROTRA_HP_solar_DEACTIVATED"]
    ] = _delayfixed_delay_land_use_efficiency_protra_266().values
    value.loc[
        ["RUSSIA"], ["PROTRA_HP_solid_fossil"]
    ] = _delayfixed_delay_land_use_efficiency_protra_267().values
    value.loc[
        ["RUSSIA"], ["PROTRA_HP_waste"]
    ] = _delayfixed_delay_land_use_efficiency_protra_268().values
    value.loc[
        ["RUSSIA"], ["PROTRA_PP_solid_bio"]
    ] = _delayfixed_delay_land_use_efficiency_protra_269().values
    value.loc[
        ["RUSSIA"], ["PROTRA_PP_solid_bio_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_270().values
    value.loc[
        ["RUSSIA"], ["PROTRA_PP_gas_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_271().values
    value.loc[
        ["RUSSIA"], ["PROTRA_PP_gas_fuels_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_272().values
    value.loc[
        ["RUSSIA"], ["PROTRA_PP_geothermal"]
    ] = _delayfixed_delay_land_use_efficiency_protra_273().values
    value.loc[
        ["RUSSIA"], ["PROTRA_PP_hydropower_dammed"]
    ] = _delayfixed_delay_land_use_efficiency_protra_274().values
    value.loc[
        ["RUSSIA"], ["PROTRA_PP_hydropower_run_of_river"]
    ] = _delayfixed_delay_land_use_efficiency_protra_275().values
    value.loc[
        ["RUSSIA"], ["PROTRA_PP_liquid_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_276().values
    value.loc[
        ["RUSSIA"], ["PROTRA_PP_liquid_fuels_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_277().values
    value.loc[
        ["RUSSIA"], ["PROTRA_PP_nuclear"]
    ] = _delayfixed_delay_land_use_efficiency_protra_278().values
    value.loc[
        ["RUSSIA"], ["PROTRA_PP_oceanic"]
    ] = _delayfixed_delay_land_use_efficiency_protra_279().values
    value.loc[
        ["RUSSIA"], ["PROTRA_PP_solar_CSP"]
    ] = _delayfixed_delay_land_use_efficiency_protra_280().values
    value.loc[
        ["RUSSIA"], ["PROTRA_PP_solar_open_space_PV"]
    ] = _delayfixed_delay_land_use_efficiency_protra_281().values
    value.loc[
        ["RUSSIA"], ["PROTRA_PP_solar_urban_PV"]
    ] = _delayfixed_delay_land_use_efficiency_protra_282().values
    value.loc[
        ["RUSSIA"], ["PROTRA_PP_solid_fossil"]
    ] = _delayfixed_delay_land_use_efficiency_protra_283().values
    value.loc[
        ["RUSSIA"], ["PROTRA_PP_solid_fossil_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_284().values
    value.loc[
        ["RUSSIA"], ["PROTRA_PP_waste"]
    ] = _delayfixed_delay_land_use_efficiency_protra_285().values
    value.loc[
        ["RUSSIA"], ["PROTRA_PP_waste_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_286().values
    value.loc[
        ["RUSSIA"], ["PROTRA_PP_wind_offshore"]
    ] = _delayfixed_delay_land_use_efficiency_protra_287().values
    value.loc[
        ["RUSSIA"], ["PROTRA_PP_wind_onshore"]
    ] = _delayfixed_delay_land_use_efficiency_protra_288().values
    value.loc[
        ["RUSSIA"], ["PROTRA_blending_gas_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_289().values
    value.loc[
        ["RUSSIA"], ["PROTRA_blending_liquid_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_290().values
    value.loc[
        ["RUSSIA"], ["PROTRA_no_process_TI_hydrogen"]
    ] = _delayfixed_delay_land_use_efficiency_protra_291().values
    value.loc[
        ["RUSSIA"], ["PROTRA_no_process_TI_solid_bio"]
    ] = _delayfixed_delay_land_use_efficiency_protra_292().values
    value.loc[
        ["RUSSIA"], ["PROTRA_no_process_TI_solid_fossil"]
    ] = _delayfixed_delay_land_use_efficiency_protra_293().values
    value.loc[
        ["USMCA"], ["PROTRA_CHP_gas_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_294().values
    value.loc[
        ["USMCA"], ["PROTRA_CHP_gas_fuels_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_295().values
    value.loc[
        ["USMCA"], ["PROTRA_CHP_geothermal_DEACTIVATED"]
    ] = _delayfixed_delay_land_use_efficiency_protra_296().values
    value.loc[
        ["USMCA"], ["PROTRA_CHP_liquid_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_297().values
    value.loc[
        ["USMCA"], ["PROTRA_CHP_liquid_fuels_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_298().values
    value.loc[
        ["USMCA"], ["PROTRA_CHP_solid_fossil"]
    ] = _delayfixed_delay_land_use_efficiency_protra_299().values
    value.loc[
        ["USMCA"], ["PROTRA_CHP_solid_fossil_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_300().values
    value.loc[
        ["USMCA"], ["PROTRA_CHP_waste"]
    ] = _delayfixed_delay_land_use_efficiency_protra_301().values
    value.loc[
        ["USMCA"], ["PROTRA_CHP_solid_bio"]
    ] = _delayfixed_delay_land_use_efficiency_protra_302().values
    value.loc[
        ["USMCA"], ["PROTRA_CHP_solid_bio_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_303().values
    value.loc[
        ["USMCA"], ["PROTRA_HP_gas_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_304().values
    value.loc[
        ["USMCA"], ["PROTRA_HP_solid_bio"]
    ] = _delayfixed_delay_land_use_efficiency_protra_305().values
    value.loc[
        ["USMCA"], ["PROTRA_HP_geothermal"]
    ] = _delayfixed_delay_land_use_efficiency_protra_306().values
    value.loc[
        ["USMCA"], ["PROTRA_HP_liquid_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_307().values
    value.loc[
        ["USMCA"], ["PROTRA_HP_solar_DEACTIVATED"]
    ] = _delayfixed_delay_land_use_efficiency_protra_308().values
    value.loc[
        ["USMCA"], ["PROTRA_HP_solid_fossil"]
    ] = _delayfixed_delay_land_use_efficiency_protra_309().values
    value.loc[
        ["USMCA"], ["PROTRA_HP_waste"]
    ] = _delayfixed_delay_land_use_efficiency_protra_310().values
    value.loc[
        ["USMCA"], ["PROTRA_PP_solid_bio"]
    ] = _delayfixed_delay_land_use_efficiency_protra_311().values
    value.loc[
        ["USMCA"], ["PROTRA_PP_solid_bio_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_312().values
    value.loc[
        ["USMCA"], ["PROTRA_PP_gas_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_313().values
    value.loc[
        ["USMCA"], ["PROTRA_PP_gas_fuels_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_314().values
    value.loc[
        ["USMCA"], ["PROTRA_PP_geothermal"]
    ] = _delayfixed_delay_land_use_efficiency_protra_315().values
    value.loc[
        ["USMCA"], ["PROTRA_PP_hydropower_dammed"]
    ] = _delayfixed_delay_land_use_efficiency_protra_316().values
    value.loc[
        ["USMCA"], ["PROTRA_PP_hydropower_run_of_river"]
    ] = _delayfixed_delay_land_use_efficiency_protra_317().values
    value.loc[
        ["USMCA"], ["PROTRA_PP_liquid_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_318().values
    value.loc[
        ["USMCA"], ["PROTRA_PP_liquid_fuels_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_319().values
    value.loc[
        ["USMCA"], ["PROTRA_PP_nuclear"]
    ] = _delayfixed_delay_land_use_efficiency_protra_320().values
    value.loc[
        ["USMCA"], ["PROTRA_PP_oceanic"]
    ] = _delayfixed_delay_land_use_efficiency_protra_321().values
    value.loc[
        ["USMCA"], ["PROTRA_PP_solar_CSP"]
    ] = _delayfixed_delay_land_use_efficiency_protra_322().values
    value.loc[
        ["USMCA"], ["PROTRA_PP_solar_open_space_PV"]
    ] = _delayfixed_delay_land_use_efficiency_protra_323().values
    value.loc[
        ["USMCA"], ["PROTRA_PP_solar_urban_PV"]
    ] = _delayfixed_delay_land_use_efficiency_protra_324().values
    value.loc[
        ["USMCA"], ["PROTRA_PP_solid_fossil"]
    ] = _delayfixed_delay_land_use_efficiency_protra_325().values
    value.loc[
        ["USMCA"], ["PROTRA_PP_solid_fossil_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_326().values
    value.loc[
        ["USMCA"], ["PROTRA_PP_waste"]
    ] = _delayfixed_delay_land_use_efficiency_protra_327().values
    value.loc[
        ["USMCA"], ["PROTRA_PP_waste_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_328().values
    value.loc[
        ["USMCA"], ["PROTRA_PP_wind_offshore"]
    ] = _delayfixed_delay_land_use_efficiency_protra_329().values
    value.loc[
        ["USMCA"], ["PROTRA_PP_wind_onshore"]
    ] = _delayfixed_delay_land_use_efficiency_protra_330().values
    value.loc[
        ["USMCA"], ["PROTRA_blending_gas_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_331().values
    value.loc[
        ["USMCA"], ["PROTRA_blending_liquid_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_332().values
    value.loc[
        ["USMCA"], ["PROTRA_no_process_TI_hydrogen"]
    ] = _delayfixed_delay_land_use_efficiency_protra_333().values
    value.loc[
        ["USMCA"], ["PROTRA_no_process_TI_solid_bio"]
    ] = _delayfixed_delay_land_use_efficiency_protra_334().values
    value.loc[
        ["USMCA"], ["PROTRA_no_process_TI_solid_fossil"]
    ] = _delayfixed_delay_land_use_efficiency_protra_335().values
    value.loc[
        ["LROW"], ["PROTRA_CHP_gas_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_336().values
    value.loc[
        ["LROW"], ["PROTRA_CHP_gas_fuels_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_337().values
    value.loc[
        ["LROW"], ["PROTRA_CHP_geothermal_DEACTIVATED"]
    ] = _delayfixed_delay_land_use_efficiency_protra_338().values
    value.loc[
        ["LROW"], ["PROTRA_CHP_liquid_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_339().values
    value.loc[
        ["LROW"], ["PROTRA_CHP_liquid_fuels_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_340().values
    value.loc[
        ["LROW"], ["PROTRA_CHP_solid_fossil"]
    ] = _delayfixed_delay_land_use_efficiency_protra_341().values
    value.loc[
        ["LROW"], ["PROTRA_CHP_solid_fossil_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_342().values
    value.loc[
        ["LROW"], ["PROTRA_CHP_waste"]
    ] = _delayfixed_delay_land_use_efficiency_protra_343().values
    value.loc[
        ["LROW"], ["PROTRA_CHP_solid_bio"]
    ] = _delayfixed_delay_land_use_efficiency_protra_344().values
    value.loc[
        ["LROW"], ["PROTRA_CHP_solid_bio_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_345().values
    value.loc[
        ["LROW"], ["PROTRA_HP_gas_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_346().values
    value.loc[
        ["LROW"], ["PROTRA_HP_solid_bio"]
    ] = _delayfixed_delay_land_use_efficiency_protra_347().values
    value.loc[
        ["LROW"], ["PROTRA_HP_geothermal"]
    ] = _delayfixed_delay_land_use_efficiency_protra_348().values
    value.loc[
        ["LROW"], ["PROTRA_HP_liquid_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_349().values
    value.loc[
        ["LROW"], ["PROTRA_HP_solar_DEACTIVATED"]
    ] = _delayfixed_delay_land_use_efficiency_protra_350().values
    value.loc[
        ["LROW"], ["PROTRA_HP_solid_fossil"]
    ] = _delayfixed_delay_land_use_efficiency_protra_351().values
    value.loc[
        ["LROW"], ["PROTRA_HP_waste"]
    ] = _delayfixed_delay_land_use_efficiency_protra_352().values
    value.loc[
        ["LROW"], ["PROTRA_PP_solid_bio"]
    ] = _delayfixed_delay_land_use_efficiency_protra_353().values
    value.loc[
        ["LROW"], ["PROTRA_PP_solid_bio_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_354().values
    value.loc[
        ["LROW"], ["PROTRA_PP_gas_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_355().values
    value.loc[
        ["LROW"], ["PROTRA_PP_gas_fuels_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_356().values
    value.loc[
        ["LROW"], ["PROTRA_PP_geothermal"]
    ] = _delayfixed_delay_land_use_efficiency_protra_357().values
    value.loc[
        ["LROW"], ["PROTRA_PP_hydropower_dammed"]
    ] = _delayfixed_delay_land_use_efficiency_protra_358().values
    value.loc[
        ["LROW"], ["PROTRA_PP_hydropower_run_of_river"]
    ] = _delayfixed_delay_land_use_efficiency_protra_359().values
    value.loc[
        ["LROW"], ["PROTRA_PP_liquid_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_360().values
    value.loc[
        ["LROW"], ["PROTRA_PP_liquid_fuels_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_361().values
    value.loc[
        ["LROW"], ["PROTRA_PP_nuclear"]
    ] = _delayfixed_delay_land_use_efficiency_protra_362().values
    value.loc[
        ["LROW"], ["PROTRA_PP_oceanic"]
    ] = _delayfixed_delay_land_use_efficiency_protra_363().values
    value.loc[
        ["LROW"], ["PROTRA_PP_solar_CSP"]
    ] = _delayfixed_delay_land_use_efficiency_protra_364().values
    value.loc[
        ["LROW"], ["PROTRA_PP_solar_open_space_PV"]
    ] = _delayfixed_delay_land_use_efficiency_protra_365().values
    value.loc[
        ["LROW"], ["PROTRA_PP_solar_urban_PV"]
    ] = _delayfixed_delay_land_use_efficiency_protra_366().values
    value.loc[
        ["LROW"], ["PROTRA_PP_solid_fossil"]
    ] = _delayfixed_delay_land_use_efficiency_protra_367().values
    value.loc[
        ["LROW"], ["PROTRA_PP_solid_fossil_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_368().values
    value.loc[
        ["LROW"], ["PROTRA_PP_waste"]
    ] = _delayfixed_delay_land_use_efficiency_protra_369().values
    value.loc[
        ["LROW"], ["PROTRA_PP_waste_CCS"]
    ] = _delayfixed_delay_land_use_efficiency_protra_370().values
    value.loc[
        ["LROW"], ["PROTRA_PP_wind_offshore"]
    ] = _delayfixed_delay_land_use_efficiency_protra_371().values
    value.loc[
        ["LROW"], ["PROTRA_PP_wind_onshore"]
    ] = _delayfixed_delay_land_use_efficiency_protra_372().values
    value.loc[
        ["LROW"], ["PROTRA_blending_gas_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_373().values
    value.loc[
        ["LROW"], ["PROTRA_blending_liquid_fuels"]
    ] = _delayfixed_delay_land_use_efficiency_protra_374().values
    value.loc[
        ["LROW"], ["PROTRA_no_process_TI_hydrogen"]
    ] = _delayfixed_delay_land_use_efficiency_protra_375().values
    value.loc[
        ["LROW"], ["PROTRA_no_process_TI_solid_bio"]
    ] = _delayfixed_delay_land_use_efficiency_protra_376().values
    value.loc[
        ["LROW"], ["PROTRA_no_process_TI_solid_fossil"]
    ] = _delayfixed_delay_land_use_efficiency_protra_377().values
    return value


_delayfixed_delay_land_use_efficiency_protra = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_CHP_gas_fuels"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_CHP_gas_fuels"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EU27", "PROTRA_CHP_gas_fuels"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_CHP_gas_fuels"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_CHP_gas_fuels"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra",
)

_delayfixed_delay_land_use_efficiency_protra_1 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_CHP_gas_fuels_CCS"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_CHP_gas_fuels_CCS"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EU27", "PROTRA_CHP_gas_fuels_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_CHP_gas_fuels_CCS"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_CHP_gas_fuels_CCS"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_1",
)

_delayfixed_delay_land_use_efficiency_protra_2 = DelayFixed(
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc[
                "EU27", "PROTRA_CHP_geothermal_DEACTIVATED"
            ]
        ),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_CHP_geothermal_DEACTIVATED"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EU27", "PROTRA_CHP_geothermal_DEACTIVATED"]),
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc[
                "EU27", "PROTRA_CHP_geothermal_DEACTIVATED"
            ]
        ),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_CHP_geothermal_DEACTIVATED"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_2",
)

_delayfixed_delay_land_use_efficiency_protra_3 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_CHP_liquid_fuels"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_CHP_liquid_fuels"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EU27", "PROTRA_CHP_liquid_fuels"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_CHP_liquid_fuels"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_CHP_liquid_fuels"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_3",
)

_delayfixed_delay_land_use_efficiency_protra_4 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_CHP_liquid_fuels_CCS"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_CHP_liquid_fuels_CCS"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EU27", "PROTRA_CHP_liquid_fuels_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_CHP_liquid_fuels_CCS"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_CHP_liquid_fuels_CCS"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_4",
)

_delayfixed_delay_land_use_efficiency_protra_5 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_CHP_solid_fossil"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_CHP_solid_fossil"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EU27", "PROTRA_CHP_solid_fossil"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_CHP_solid_fossil"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_CHP_solid_fossil"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_5",
)

_delayfixed_delay_land_use_efficiency_protra_6 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_CHP_solid_fossil_CCS"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_CHP_solid_fossil_CCS"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EU27", "PROTRA_CHP_solid_fossil_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_CHP_solid_fossil_CCS"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_CHP_solid_fossil_CCS"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_6",
)

_delayfixed_delay_land_use_efficiency_protra_7 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_CHP_waste"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_CHP_waste"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EU27", "PROTRA_CHP_waste"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_CHP_waste"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_CHP_waste"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_7",
)

_delayfixed_delay_land_use_efficiency_protra_8 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_CHP_solid_bio"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_CHP_solid_bio"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EU27", "PROTRA_CHP_solid_bio"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_CHP_solid_bio"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_CHP_solid_bio"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_8",
)

_delayfixed_delay_land_use_efficiency_protra_9 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_CHP_solid_bio_CCS"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_CHP_solid_bio_CCS"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EU27", "PROTRA_CHP_solid_bio_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_CHP_solid_bio_CCS"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_CHP_solid_bio_CCS"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_9",
)

_delayfixed_delay_land_use_efficiency_protra_10 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_HP_gas_fuels"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_HP_gas_fuels"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EU27", "PROTRA_HP_gas_fuels"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_HP_gas_fuels"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_HP_gas_fuels"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_10",
)

_delayfixed_delay_land_use_efficiency_protra_11 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_HP_solid_bio"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_HP_solid_bio"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EU27", "PROTRA_HP_solid_bio"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_HP_solid_bio"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_HP_solid_bio"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_11",
)

_delayfixed_delay_land_use_efficiency_protra_12 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_HP_geothermal"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_HP_geothermal"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EU27", "PROTRA_HP_geothermal"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_HP_geothermal"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_HP_geothermal"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_12",
)

_delayfixed_delay_land_use_efficiency_protra_13 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_HP_liquid_fuels"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_HP_liquid_fuels"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EU27", "PROTRA_HP_liquid_fuels"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_HP_liquid_fuels"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_HP_liquid_fuels"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_13",
)

_delayfixed_delay_land_use_efficiency_protra_14 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_HP_solar_DEACTIVATED"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_HP_solar_DEACTIVATED"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EU27", "PROTRA_HP_solar_DEACTIVATED"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_HP_solar_DEACTIVATED"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_HP_solar_DEACTIVATED"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_14",
)

_delayfixed_delay_land_use_efficiency_protra_15 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_HP_solid_fossil"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_HP_solid_fossil"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EU27", "PROTRA_HP_solid_fossil"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_HP_solid_fossil"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_HP_solid_fossil"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_15",
)

_delayfixed_delay_land_use_efficiency_protra_16 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_HP_waste"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_HP_waste"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EU27", "PROTRA_HP_waste"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_HP_waste"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_HP_waste"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_16",
)

_delayfixed_delay_land_use_efficiency_protra_17 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_PP_solid_bio"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_PP_solid_bio"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EU27", "PROTRA_PP_solid_bio"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_PP_solid_bio"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_PP_solid_bio"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_17",
)

_delayfixed_delay_land_use_efficiency_protra_18 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_PP_solid_bio_CCS"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_PP_solid_bio_CCS"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EU27", "PROTRA_PP_solid_bio_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_PP_solid_bio_CCS"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_PP_solid_bio_CCS"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_18",
)

_delayfixed_delay_land_use_efficiency_protra_19 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_PP_gas_fuels"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_PP_gas_fuels"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EU27", "PROTRA_PP_gas_fuels"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_PP_gas_fuels"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_PP_gas_fuels"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_19",
)

_delayfixed_delay_land_use_efficiency_protra_20 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_PP_gas_fuels_CCS"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_PP_gas_fuels_CCS"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EU27", "PROTRA_PP_gas_fuels_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_PP_gas_fuels_CCS"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_PP_gas_fuels_CCS"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_20",
)

_delayfixed_delay_land_use_efficiency_protra_21 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_PP_geothermal"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_PP_geothermal"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EU27", "PROTRA_PP_geothermal"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_PP_geothermal"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_PP_geothermal"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_21",
)

_delayfixed_delay_land_use_efficiency_protra_22 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_PP_hydropower_dammed"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_PP_hydropower_dammed"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EU27", "PROTRA_PP_hydropower_dammed"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_PP_hydropower_dammed"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_PP_hydropower_dammed"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_22",
)

_delayfixed_delay_land_use_efficiency_protra_23 = DelayFixed(
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc[
                "EU27", "PROTRA_PP_hydropower_run_of_river"
            ]
        ),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_PP_hydropower_run_of_river"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EU27", "PROTRA_PP_hydropower_run_of_river"]),
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc[
                "EU27", "PROTRA_PP_hydropower_run_of_river"
            ]
        ),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_PP_hydropower_run_of_river"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_23",
)

_delayfixed_delay_land_use_efficiency_protra_24 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_PP_liquid_fuels"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_PP_liquid_fuels"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EU27", "PROTRA_PP_liquid_fuels"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_PP_liquid_fuels"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_PP_liquid_fuels"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_24",
)

_delayfixed_delay_land_use_efficiency_protra_25 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_PP_liquid_fuels_CCS"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_PP_liquid_fuels_CCS"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EU27", "PROTRA_PP_liquid_fuels_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_PP_liquid_fuels_CCS"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_PP_liquid_fuels_CCS"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_25",
)

_delayfixed_delay_land_use_efficiency_protra_26 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_PP_nuclear"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_PP_nuclear"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EU27", "PROTRA_PP_nuclear"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_PP_nuclear"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_PP_nuclear"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_26",
)

_delayfixed_delay_land_use_efficiency_protra_27 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_PP_oceanic"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_PP_oceanic"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EU27", "PROTRA_PP_oceanic"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_PP_oceanic"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_PP_oceanic"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_27",
)

_delayfixed_delay_land_use_efficiency_protra_28 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_PP_solar_CSP"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_PP_solar_CSP"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EU27", "PROTRA_PP_solar_CSP"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_PP_solar_CSP"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_PP_solar_CSP"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_28",
)

_delayfixed_delay_land_use_efficiency_protra_29 = DelayFixed(
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["EU27", "PROTRA_PP_solar_open_space_PV"]
        ),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_PP_solar_open_space_PV"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EU27", "PROTRA_PP_solar_open_space_PV"]),
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["EU27", "PROTRA_PP_solar_open_space_PV"]
        ),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_PP_solar_open_space_PV"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_29",
)

_delayfixed_delay_land_use_efficiency_protra_30 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_PP_solar_urban_PV"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_PP_solar_urban_PV"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EU27", "PROTRA_PP_solar_urban_PV"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_PP_solar_urban_PV"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_PP_solar_urban_PV"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_30",
)

_delayfixed_delay_land_use_efficiency_protra_31 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_PP_solid_fossil"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_PP_solid_fossil"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EU27", "PROTRA_PP_solid_fossil"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_PP_solid_fossil"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_PP_solid_fossil"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_31",
)

_delayfixed_delay_land_use_efficiency_protra_32 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_PP_solid_fossil_CCS"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_PP_solid_fossil_CCS"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EU27", "PROTRA_PP_solid_fossil_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_PP_solid_fossil_CCS"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_PP_solid_fossil_CCS"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_32",
)

_delayfixed_delay_land_use_efficiency_protra_33 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_PP_waste"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_PP_waste"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EU27", "PROTRA_PP_waste"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_PP_waste"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_PP_waste"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_33",
)

_delayfixed_delay_land_use_efficiency_protra_34 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_PP_waste_CCS"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_PP_waste_CCS"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EU27", "PROTRA_PP_waste_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_PP_waste_CCS"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_PP_waste_CCS"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_34",
)

_delayfixed_delay_land_use_efficiency_protra_35 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_PP_wind_offshore"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_PP_wind_offshore"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EU27", "PROTRA_PP_wind_offshore"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_PP_wind_offshore"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_PP_wind_offshore"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_35",
)

_delayfixed_delay_land_use_efficiency_protra_36 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_PP_wind_onshore"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_PP_wind_onshore"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EU27", "PROTRA_PP_wind_onshore"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_PP_wind_onshore"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_PP_wind_onshore"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_36",
)

_delayfixed_delay_land_use_efficiency_protra_37 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_blending_gas_fuels"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_blending_gas_fuels"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EU27", "PROTRA_blending_gas_fuels"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_blending_gas_fuels"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_blending_gas_fuels"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_37",
)

_delayfixed_delay_land_use_efficiency_protra_38 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_blending_liquid_fuels"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_blending_liquid_fuels"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EU27", "PROTRA_blending_liquid_fuels"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EU27", "PROTRA_blending_liquid_fuels"]),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_blending_liquid_fuels"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_38",
)

_delayfixed_delay_land_use_efficiency_protra_39 = DelayFixed(
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["EU27", "PROTRA_no_process_TI_hydrogen"]
        ),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_no_process_TI_hydrogen"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EU27", "PROTRA_no_process_TI_hydrogen"]),
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["EU27", "PROTRA_no_process_TI_hydrogen"]
        ),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_no_process_TI_hydrogen"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_39",
)

_delayfixed_delay_land_use_efficiency_protra_40 = DelayFixed(
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["EU27", "PROTRA_no_process_TI_solid_bio"]
        ),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_no_process_TI_solid_bio"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EU27", "PROTRA_no_process_TI_solid_bio"]),
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["EU27", "PROTRA_no_process_TI_solid_bio"]
        ),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_no_process_TI_solid_bio"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_40",
)

_delayfixed_delay_land_use_efficiency_protra_41 = DelayFixed(
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc[
                "EU27", "PROTRA_no_process_TI_solid_fossil"
            ]
        ),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_no_process_TI_solid_fossil"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EU27", "PROTRA_no_process_TI_solid_fossil"]),
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc[
                "EU27", "PROTRA_no_process_TI_solid_fossil"
            ]
        ),
        {"REGIONS_36_I": ["EU27"], "NRG_PRO_I": ["PROTRA_no_process_TI_solid_fossil"]},
        ["REGIONS_36_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_41",
)

_delayfixed_delay_land_use_efficiency_protra_42 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_CHP_gas_fuels"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_CHP_gas_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["UK", "PROTRA_CHP_gas_fuels"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_CHP_gas_fuels"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_CHP_gas_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_42",
)

_delayfixed_delay_land_use_efficiency_protra_43 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_CHP_gas_fuels_CCS"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_CHP_gas_fuels_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["UK", "PROTRA_CHP_gas_fuels_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_CHP_gas_fuels_CCS"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_CHP_gas_fuels_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_43",
)

_delayfixed_delay_land_use_efficiency_protra_44 = DelayFixed(
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["UK", "PROTRA_CHP_geothermal_DEACTIVATED"]
        ),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_CHP_geothermal_DEACTIVATED"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["UK", "PROTRA_CHP_geothermal_DEACTIVATED"]),
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["UK", "PROTRA_CHP_geothermal_DEACTIVATED"]
        ),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_CHP_geothermal_DEACTIVATED"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_44",
)

_delayfixed_delay_land_use_efficiency_protra_45 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_CHP_liquid_fuels"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_CHP_liquid_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["UK", "PROTRA_CHP_liquid_fuels"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_CHP_liquid_fuels"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_CHP_liquid_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_45",
)

_delayfixed_delay_land_use_efficiency_protra_46 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_CHP_liquid_fuels_CCS"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_CHP_liquid_fuels_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["UK", "PROTRA_CHP_liquid_fuels_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_CHP_liquid_fuels_CCS"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_CHP_liquid_fuels_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_46",
)

_delayfixed_delay_land_use_efficiency_protra_47 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_CHP_solid_fossil"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_CHP_solid_fossil"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["UK", "PROTRA_CHP_solid_fossil"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_CHP_solid_fossil"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_CHP_solid_fossil"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_47",
)

_delayfixed_delay_land_use_efficiency_protra_48 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_CHP_solid_fossil_CCS"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_CHP_solid_fossil_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["UK", "PROTRA_CHP_solid_fossil_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_CHP_solid_fossil_CCS"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_CHP_solid_fossil_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_48",
)

_delayfixed_delay_land_use_efficiency_protra_49 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_CHP_waste"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_CHP_waste"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["UK", "PROTRA_CHP_waste"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_CHP_waste"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_CHP_waste"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_49",
)

_delayfixed_delay_land_use_efficiency_protra_50 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_CHP_solid_bio"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_CHP_solid_bio"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["UK", "PROTRA_CHP_solid_bio"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_CHP_solid_bio"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_CHP_solid_bio"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_50",
)

_delayfixed_delay_land_use_efficiency_protra_51 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_CHP_solid_bio_CCS"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_CHP_solid_bio_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["UK", "PROTRA_CHP_solid_bio_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_CHP_solid_bio_CCS"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_CHP_solid_bio_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_51",
)

_delayfixed_delay_land_use_efficiency_protra_52 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_HP_gas_fuels"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_HP_gas_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["UK", "PROTRA_HP_gas_fuels"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_HP_gas_fuels"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_HP_gas_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_52",
)

_delayfixed_delay_land_use_efficiency_protra_53 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_HP_solid_bio"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_HP_solid_bio"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["UK", "PROTRA_HP_solid_bio"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_HP_solid_bio"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_HP_solid_bio"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_53",
)

_delayfixed_delay_land_use_efficiency_protra_54 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_HP_geothermal"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_HP_geothermal"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["UK", "PROTRA_HP_geothermal"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_HP_geothermal"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_HP_geothermal"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_54",
)

_delayfixed_delay_land_use_efficiency_protra_55 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_HP_liquid_fuels"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_HP_liquid_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["UK", "PROTRA_HP_liquid_fuels"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_HP_liquid_fuels"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_HP_liquid_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_55",
)

_delayfixed_delay_land_use_efficiency_protra_56 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_HP_solar_DEACTIVATED"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_HP_solar_DEACTIVATED"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["UK", "PROTRA_HP_solar_DEACTIVATED"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_HP_solar_DEACTIVATED"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_HP_solar_DEACTIVATED"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_56",
)

_delayfixed_delay_land_use_efficiency_protra_57 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_HP_solid_fossil"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_HP_solid_fossil"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["UK", "PROTRA_HP_solid_fossil"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_HP_solid_fossil"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_HP_solid_fossil"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_57",
)

_delayfixed_delay_land_use_efficiency_protra_58 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_HP_waste"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_HP_waste"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["UK", "PROTRA_HP_waste"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_HP_waste"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_HP_waste"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_58",
)

_delayfixed_delay_land_use_efficiency_protra_59 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_PP_solid_bio"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_PP_solid_bio"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["UK", "PROTRA_PP_solid_bio"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_PP_solid_bio"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_PP_solid_bio"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_59",
)

_delayfixed_delay_land_use_efficiency_protra_60 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_PP_solid_bio_CCS"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_PP_solid_bio_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["UK", "PROTRA_PP_solid_bio_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_PP_solid_bio_CCS"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_PP_solid_bio_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_60",
)

_delayfixed_delay_land_use_efficiency_protra_61 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_PP_gas_fuels"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_PP_gas_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["UK", "PROTRA_PP_gas_fuels"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_PP_gas_fuels"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_PP_gas_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_61",
)

_delayfixed_delay_land_use_efficiency_protra_62 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_PP_gas_fuels_CCS"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_PP_gas_fuels_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["UK", "PROTRA_PP_gas_fuels_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_PP_gas_fuels_CCS"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_PP_gas_fuels_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_62",
)

_delayfixed_delay_land_use_efficiency_protra_63 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_PP_geothermal"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_PP_geothermal"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["UK", "PROTRA_PP_geothermal"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_PP_geothermal"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_PP_geothermal"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_63",
)

_delayfixed_delay_land_use_efficiency_protra_64 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_PP_hydropower_dammed"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_PP_hydropower_dammed"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["UK", "PROTRA_PP_hydropower_dammed"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_PP_hydropower_dammed"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_PP_hydropower_dammed"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_64",
)

_delayfixed_delay_land_use_efficiency_protra_65 = DelayFixed(
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["UK", "PROTRA_PP_hydropower_run_of_river"]
        ),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_PP_hydropower_run_of_river"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["UK", "PROTRA_PP_hydropower_run_of_river"]),
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["UK", "PROTRA_PP_hydropower_run_of_river"]
        ),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_PP_hydropower_run_of_river"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_65",
)

_delayfixed_delay_land_use_efficiency_protra_66 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_PP_liquid_fuels"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_PP_liquid_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["UK", "PROTRA_PP_liquid_fuels"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_PP_liquid_fuels"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_PP_liquid_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_66",
)

_delayfixed_delay_land_use_efficiency_protra_67 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_PP_liquid_fuels_CCS"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_PP_liquid_fuels_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["UK", "PROTRA_PP_liquid_fuels_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_PP_liquid_fuels_CCS"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_PP_liquid_fuels_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_67",
)

_delayfixed_delay_land_use_efficiency_protra_68 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_PP_nuclear"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_PP_nuclear"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["UK", "PROTRA_PP_nuclear"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_PP_nuclear"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_PP_nuclear"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_68",
)

_delayfixed_delay_land_use_efficiency_protra_69 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_PP_oceanic"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_PP_oceanic"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["UK", "PROTRA_PP_oceanic"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_PP_oceanic"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_PP_oceanic"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_69",
)

_delayfixed_delay_land_use_efficiency_protra_70 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_PP_solar_CSP"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_PP_solar_CSP"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["UK", "PROTRA_PP_solar_CSP"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_PP_solar_CSP"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_PP_solar_CSP"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_70",
)

_delayfixed_delay_land_use_efficiency_protra_71 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_PP_solar_open_space_PV"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_PP_solar_open_space_PV"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["UK", "PROTRA_PP_solar_open_space_PV"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_PP_solar_open_space_PV"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_PP_solar_open_space_PV"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_71",
)

_delayfixed_delay_land_use_efficiency_protra_72 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_PP_solar_urban_PV"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_PP_solar_urban_PV"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["UK", "PROTRA_PP_solar_urban_PV"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_PP_solar_urban_PV"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_PP_solar_urban_PV"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_72",
)

_delayfixed_delay_land_use_efficiency_protra_73 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_PP_solid_fossil"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_PP_solid_fossil"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["UK", "PROTRA_PP_solid_fossil"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_PP_solid_fossil"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_PP_solid_fossil"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_73",
)

_delayfixed_delay_land_use_efficiency_protra_74 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_PP_solid_fossil_CCS"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_PP_solid_fossil_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["UK", "PROTRA_PP_solid_fossil_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_PP_solid_fossil_CCS"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_PP_solid_fossil_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_74",
)

_delayfixed_delay_land_use_efficiency_protra_75 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_PP_waste"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_PP_waste"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["UK", "PROTRA_PP_waste"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_PP_waste"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_PP_waste"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_75",
)

_delayfixed_delay_land_use_efficiency_protra_76 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_PP_waste_CCS"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_PP_waste_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["UK", "PROTRA_PP_waste_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_PP_waste_CCS"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_PP_waste_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_76",
)

_delayfixed_delay_land_use_efficiency_protra_77 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_PP_wind_offshore"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_PP_wind_offshore"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["UK", "PROTRA_PP_wind_offshore"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_PP_wind_offshore"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_PP_wind_offshore"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_77",
)

_delayfixed_delay_land_use_efficiency_protra_78 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_PP_wind_onshore"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_PP_wind_onshore"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["UK", "PROTRA_PP_wind_onshore"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_PP_wind_onshore"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_PP_wind_onshore"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_78",
)

_delayfixed_delay_land_use_efficiency_protra_79 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_blending_gas_fuels"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_blending_gas_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["UK", "PROTRA_blending_gas_fuels"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_blending_gas_fuels"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_blending_gas_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_79",
)

_delayfixed_delay_land_use_efficiency_protra_80 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_blending_liquid_fuels"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_blending_liquid_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["UK", "PROTRA_blending_liquid_fuels"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_blending_liquid_fuels"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_blending_liquid_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_80",
)

_delayfixed_delay_land_use_efficiency_protra_81 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_no_process_TI_hydrogen"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_no_process_TI_hydrogen"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["UK", "PROTRA_no_process_TI_hydrogen"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_no_process_TI_hydrogen"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_no_process_TI_hydrogen"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_81",
)

_delayfixed_delay_land_use_efficiency_protra_82 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_no_process_TI_solid_bio"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_no_process_TI_solid_bio"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["UK", "PROTRA_no_process_TI_solid_bio"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["UK", "PROTRA_no_process_TI_solid_bio"]),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_no_process_TI_solid_bio"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_82",
)

_delayfixed_delay_land_use_efficiency_protra_83 = DelayFixed(
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["UK", "PROTRA_no_process_TI_solid_fossil"]
        ),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_no_process_TI_solid_fossil"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["UK", "PROTRA_no_process_TI_solid_fossil"]),
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["UK", "PROTRA_no_process_TI_solid_fossil"]
        ),
        {"REGIONS_35_I": ["UK"], "NRG_PRO_I": ["PROTRA_no_process_TI_solid_fossil"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_83",
)

_delayfixed_delay_land_use_efficiency_protra_84 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["CHINA", "PROTRA_CHP_gas_fuels"]),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_CHP_gas_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["CHINA", "PROTRA_CHP_gas_fuels"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["CHINA", "PROTRA_CHP_gas_fuels"]),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_CHP_gas_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_84",
)

_delayfixed_delay_land_use_efficiency_protra_85 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["CHINA", "PROTRA_CHP_gas_fuels_CCS"]),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_CHP_gas_fuels_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["CHINA", "PROTRA_CHP_gas_fuels_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["CHINA", "PROTRA_CHP_gas_fuels_CCS"]),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_CHP_gas_fuels_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_85",
)

_delayfixed_delay_land_use_efficiency_protra_86 = DelayFixed(
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc[
                "CHINA", "PROTRA_CHP_geothermal_DEACTIVATED"
            ]
        ),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_CHP_geothermal_DEACTIVATED"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["CHINA", "PROTRA_CHP_geothermal_DEACTIVATED"]),
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc[
                "CHINA", "PROTRA_CHP_geothermal_DEACTIVATED"
            ]
        ),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_CHP_geothermal_DEACTIVATED"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_86",
)

_delayfixed_delay_land_use_efficiency_protra_87 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["CHINA", "PROTRA_CHP_liquid_fuels"]),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_CHP_liquid_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["CHINA", "PROTRA_CHP_liquid_fuels"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["CHINA", "PROTRA_CHP_liquid_fuels"]),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_CHP_liquid_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_87",
)

_delayfixed_delay_land_use_efficiency_protra_88 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["CHINA", "PROTRA_CHP_liquid_fuels_CCS"]),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_CHP_liquid_fuels_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["CHINA", "PROTRA_CHP_liquid_fuels_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["CHINA", "PROTRA_CHP_liquid_fuels_CCS"]),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_CHP_liquid_fuels_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_88",
)

_delayfixed_delay_land_use_efficiency_protra_89 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["CHINA", "PROTRA_CHP_solid_fossil"]),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_CHP_solid_fossil"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["CHINA", "PROTRA_CHP_solid_fossil"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["CHINA", "PROTRA_CHP_solid_fossil"]),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_CHP_solid_fossil"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_89",
)

_delayfixed_delay_land_use_efficiency_protra_90 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["CHINA", "PROTRA_CHP_solid_fossil_CCS"]),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_CHP_solid_fossil_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["CHINA", "PROTRA_CHP_solid_fossil_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["CHINA", "PROTRA_CHP_solid_fossil_CCS"]),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_CHP_solid_fossil_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_90",
)

_delayfixed_delay_land_use_efficiency_protra_91 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["CHINA", "PROTRA_CHP_waste"]),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_CHP_waste"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["CHINA", "PROTRA_CHP_waste"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["CHINA", "PROTRA_CHP_waste"]),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_CHP_waste"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_91",
)

_delayfixed_delay_land_use_efficiency_protra_92 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["CHINA", "PROTRA_CHP_solid_bio"]),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_CHP_solid_bio"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["CHINA", "PROTRA_CHP_solid_bio"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["CHINA", "PROTRA_CHP_solid_bio"]),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_CHP_solid_bio"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_92",
)

_delayfixed_delay_land_use_efficiency_protra_93 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["CHINA", "PROTRA_CHP_solid_bio_CCS"]),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_CHP_solid_bio_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["CHINA", "PROTRA_CHP_solid_bio_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["CHINA", "PROTRA_CHP_solid_bio_CCS"]),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_CHP_solid_bio_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_93",
)

_delayfixed_delay_land_use_efficiency_protra_94 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["CHINA", "PROTRA_HP_gas_fuels"]),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_HP_gas_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["CHINA", "PROTRA_HP_gas_fuels"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["CHINA", "PROTRA_HP_gas_fuels"]),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_HP_gas_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_94",
)

_delayfixed_delay_land_use_efficiency_protra_95 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["CHINA", "PROTRA_HP_solid_bio"]),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_HP_solid_bio"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["CHINA", "PROTRA_HP_solid_bio"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["CHINA", "PROTRA_HP_solid_bio"]),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_HP_solid_bio"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_95",
)

_delayfixed_delay_land_use_efficiency_protra_96 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["CHINA", "PROTRA_HP_geothermal"]),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_HP_geothermal"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["CHINA", "PROTRA_HP_geothermal"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["CHINA", "PROTRA_HP_geothermal"]),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_HP_geothermal"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_96",
)

_delayfixed_delay_land_use_efficiency_protra_97 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["CHINA", "PROTRA_HP_liquid_fuels"]),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_HP_liquid_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["CHINA", "PROTRA_HP_liquid_fuels"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["CHINA", "PROTRA_HP_liquid_fuels"]),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_HP_liquid_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_97",
)

_delayfixed_delay_land_use_efficiency_protra_98 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["CHINA", "PROTRA_HP_solar_DEACTIVATED"]),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_HP_solar_DEACTIVATED"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["CHINA", "PROTRA_HP_solar_DEACTIVATED"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["CHINA", "PROTRA_HP_solar_DEACTIVATED"]),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_HP_solar_DEACTIVATED"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_98",
)

_delayfixed_delay_land_use_efficiency_protra_99 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["CHINA", "PROTRA_HP_solid_fossil"]),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_HP_solid_fossil"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["CHINA", "PROTRA_HP_solid_fossil"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["CHINA", "PROTRA_HP_solid_fossil"]),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_HP_solid_fossil"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_99",
)

_delayfixed_delay_land_use_efficiency_protra_100 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["CHINA", "PROTRA_HP_waste"]),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_HP_waste"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["CHINA", "PROTRA_HP_waste"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["CHINA", "PROTRA_HP_waste"]),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_HP_waste"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_100",
)

_delayfixed_delay_land_use_efficiency_protra_101 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["CHINA", "PROTRA_PP_solid_bio"]),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_PP_solid_bio"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["CHINA", "PROTRA_PP_solid_bio"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["CHINA", "PROTRA_PP_solid_bio"]),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_PP_solid_bio"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_101",
)

_delayfixed_delay_land_use_efficiency_protra_102 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["CHINA", "PROTRA_PP_solid_bio_CCS"]),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_PP_solid_bio_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["CHINA", "PROTRA_PP_solid_bio_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["CHINA", "PROTRA_PP_solid_bio_CCS"]),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_PP_solid_bio_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_102",
)

_delayfixed_delay_land_use_efficiency_protra_103 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["CHINA", "PROTRA_PP_gas_fuels"]),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_PP_gas_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["CHINA", "PROTRA_PP_gas_fuels"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["CHINA", "PROTRA_PP_gas_fuels"]),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_PP_gas_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_103",
)

_delayfixed_delay_land_use_efficiency_protra_104 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["CHINA", "PROTRA_PP_gas_fuels_CCS"]),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_PP_gas_fuels_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["CHINA", "PROTRA_PP_gas_fuels_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["CHINA", "PROTRA_PP_gas_fuels_CCS"]),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_PP_gas_fuels_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_104",
)

_delayfixed_delay_land_use_efficiency_protra_105 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["CHINA", "PROTRA_PP_geothermal"]),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_PP_geothermal"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["CHINA", "PROTRA_PP_geothermal"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["CHINA", "PROTRA_PP_geothermal"]),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_PP_geothermal"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_105",
)

_delayfixed_delay_land_use_efficiency_protra_106 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["CHINA", "PROTRA_PP_hydropower_dammed"]),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_PP_hydropower_dammed"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["CHINA", "PROTRA_PP_hydropower_dammed"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["CHINA", "PROTRA_PP_hydropower_dammed"]),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_PP_hydropower_dammed"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_106",
)

_delayfixed_delay_land_use_efficiency_protra_107 = DelayFixed(
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc[
                "CHINA", "PROTRA_PP_hydropower_run_of_river"
            ]
        ),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_PP_hydropower_run_of_river"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["CHINA", "PROTRA_PP_hydropower_run_of_river"]),
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc[
                "CHINA", "PROTRA_PP_hydropower_run_of_river"
            ]
        ),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_PP_hydropower_run_of_river"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_107",
)

_delayfixed_delay_land_use_efficiency_protra_108 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["CHINA", "PROTRA_PP_liquid_fuels"]),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_PP_liquid_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["CHINA", "PROTRA_PP_liquid_fuels"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["CHINA", "PROTRA_PP_liquid_fuels"]),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_PP_liquid_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_108",
)

_delayfixed_delay_land_use_efficiency_protra_109 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["CHINA", "PROTRA_PP_liquid_fuels_CCS"]),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_PP_liquid_fuels_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["CHINA", "PROTRA_PP_liquid_fuels_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["CHINA", "PROTRA_PP_liquid_fuels_CCS"]),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_PP_liquid_fuels_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_109",
)

_delayfixed_delay_land_use_efficiency_protra_110 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["CHINA", "PROTRA_PP_nuclear"]),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_PP_nuclear"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["CHINA", "PROTRA_PP_nuclear"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["CHINA", "PROTRA_PP_nuclear"]),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_PP_nuclear"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_110",
)

_delayfixed_delay_land_use_efficiency_protra_111 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["CHINA", "PROTRA_PP_oceanic"]),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_PP_oceanic"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["CHINA", "PROTRA_PP_oceanic"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["CHINA", "PROTRA_PP_oceanic"]),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_PP_oceanic"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_111",
)

_delayfixed_delay_land_use_efficiency_protra_112 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["CHINA", "PROTRA_PP_solar_CSP"]),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_PP_solar_CSP"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["CHINA", "PROTRA_PP_solar_CSP"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["CHINA", "PROTRA_PP_solar_CSP"]),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_PP_solar_CSP"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_112",
)

_delayfixed_delay_land_use_efficiency_protra_113 = DelayFixed(
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["CHINA", "PROTRA_PP_solar_open_space_PV"]
        ),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_PP_solar_open_space_PV"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["CHINA", "PROTRA_PP_solar_open_space_PV"]),
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["CHINA", "PROTRA_PP_solar_open_space_PV"]
        ),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_PP_solar_open_space_PV"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_113",
)

_delayfixed_delay_land_use_efficiency_protra_114 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["CHINA", "PROTRA_PP_solar_urban_PV"]),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_PP_solar_urban_PV"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["CHINA", "PROTRA_PP_solar_urban_PV"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["CHINA", "PROTRA_PP_solar_urban_PV"]),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_PP_solar_urban_PV"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_114",
)

_delayfixed_delay_land_use_efficiency_protra_115 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["CHINA", "PROTRA_PP_solid_fossil"]),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_PP_solid_fossil"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["CHINA", "PROTRA_PP_solid_fossil"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["CHINA", "PROTRA_PP_solid_fossil"]),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_PP_solid_fossil"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_115",
)

_delayfixed_delay_land_use_efficiency_protra_116 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["CHINA", "PROTRA_PP_solid_fossil_CCS"]),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_PP_solid_fossil_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["CHINA", "PROTRA_PP_solid_fossil_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["CHINA", "PROTRA_PP_solid_fossil_CCS"]),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_PP_solid_fossil_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_116",
)

_delayfixed_delay_land_use_efficiency_protra_117 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["CHINA", "PROTRA_PP_waste"]),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_PP_waste"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["CHINA", "PROTRA_PP_waste"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["CHINA", "PROTRA_PP_waste"]),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_PP_waste"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_117",
)

_delayfixed_delay_land_use_efficiency_protra_118 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["CHINA", "PROTRA_PP_waste_CCS"]),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_PP_waste_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["CHINA", "PROTRA_PP_waste_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["CHINA", "PROTRA_PP_waste_CCS"]),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_PP_waste_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_118",
)

_delayfixed_delay_land_use_efficiency_protra_119 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["CHINA", "PROTRA_PP_wind_offshore"]),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_PP_wind_offshore"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["CHINA", "PROTRA_PP_wind_offshore"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["CHINA", "PROTRA_PP_wind_offshore"]),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_PP_wind_offshore"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_119",
)

_delayfixed_delay_land_use_efficiency_protra_120 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["CHINA", "PROTRA_PP_wind_onshore"]),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_PP_wind_onshore"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["CHINA", "PROTRA_PP_wind_onshore"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["CHINA", "PROTRA_PP_wind_onshore"]),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_PP_wind_onshore"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_120",
)

_delayfixed_delay_land_use_efficiency_protra_121 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["CHINA", "PROTRA_blending_gas_fuels"]),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_blending_gas_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["CHINA", "PROTRA_blending_gas_fuels"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["CHINA", "PROTRA_blending_gas_fuels"]),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_blending_gas_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_121",
)

_delayfixed_delay_land_use_efficiency_protra_122 = DelayFixed(
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["CHINA", "PROTRA_blending_liquid_fuels"]
        ),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_blending_liquid_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["CHINA", "PROTRA_blending_liquid_fuels"]),
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["CHINA", "PROTRA_blending_liquid_fuels"]
        ),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_blending_liquid_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_122",
)

_delayfixed_delay_land_use_efficiency_protra_123 = DelayFixed(
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["CHINA", "PROTRA_no_process_TI_hydrogen"]
        ),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_no_process_TI_hydrogen"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["CHINA", "PROTRA_no_process_TI_hydrogen"]),
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["CHINA", "PROTRA_no_process_TI_hydrogen"]
        ),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_no_process_TI_hydrogen"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_123",
)

_delayfixed_delay_land_use_efficiency_protra_124 = DelayFixed(
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["CHINA", "PROTRA_no_process_TI_solid_bio"]
        ),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_no_process_TI_solid_bio"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["CHINA", "PROTRA_no_process_TI_solid_bio"]),
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["CHINA", "PROTRA_no_process_TI_solid_bio"]
        ),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_no_process_TI_solid_bio"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_124",
)

_delayfixed_delay_land_use_efficiency_protra_125 = DelayFixed(
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc[
                "CHINA", "PROTRA_no_process_TI_solid_fossil"
            ]
        ),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_no_process_TI_solid_fossil"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["CHINA", "PROTRA_no_process_TI_solid_fossil"]),
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc[
                "CHINA", "PROTRA_no_process_TI_solid_fossil"
            ]
        ),
        {"REGIONS_35_I": ["CHINA"], "NRG_PRO_I": ["PROTRA_no_process_TI_solid_fossil"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_125",
)

_delayfixed_delay_land_use_efficiency_protra_126 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EASOC", "PROTRA_CHP_gas_fuels"]),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_CHP_gas_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EASOC", "PROTRA_CHP_gas_fuels"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EASOC", "PROTRA_CHP_gas_fuels"]),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_CHP_gas_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_126",
)

_delayfixed_delay_land_use_efficiency_protra_127 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EASOC", "PROTRA_CHP_gas_fuels_CCS"]),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_CHP_gas_fuels_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EASOC", "PROTRA_CHP_gas_fuels_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EASOC", "PROTRA_CHP_gas_fuels_CCS"]),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_CHP_gas_fuels_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_127",
)

_delayfixed_delay_land_use_efficiency_protra_128 = DelayFixed(
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc[
                "EASOC", "PROTRA_CHP_geothermal_DEACTIVATED"
            ]
        ),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_CHP_geothermal_DEACTIVATED"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EASOC", "PROTRA_CHP_geothermal_DEACTIVATED"]),
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc[
                "EASOC", "PROTRA_CHP_geothermal_DEACTIVATED"
            ]
        ),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_CHP_geothermal_DEACTIVATED"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_128",
)

_delayfixed_delay_land_use_efficiency_protra_129 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EASOC", "PROTRA_CHP_liquid_fuels"]),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_CHP_liquid_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EASOC", "PROTRA_CHP_liquid_fuels"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EASOC", "PROTRA_CHP_liquid_fuels"]),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_CHP_liquid_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_129",
)

_delayfixed_delay_land_use_efficiency_protra_130 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EASOC", "PROTRA_CHP_liquid_fuels_CCS"]),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_CHP_liquid_fuels_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EASOC", "PROTRA_CHP_liquid_fuels_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EASOC", "PROTRA_CHP_liquid_fuels_CCS"]),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_CHP_liquid_fuels_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_130",
)

_delayfixed_delay_land_use_efficiency_protra_131 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EASOC", "PROTRA_CHP_solid_fossil"]),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_CHP_solid_fossil"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EASOC", "PROTRA_CHP_solid_fossil"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EASOC", "PROTRA_CHP_solid_fossil"]),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_CHP_solid_fossil"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_131",
)

_delayfixed_delay_land_use_efficiency_protra_132 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EASOC", "PROTRA_CHP_solid_fossil_CCS"]),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_CHP_solid_fossil_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EASOC", "PROTRA_CHP_solid_fossil_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EASOC", "PROTRA_CHP_solid_fossil_CCS"]),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_CHP_solid_fossil_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_132",
)

_delayfixed_delay_land_use_efficiency_protra_133 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EASOC", "PROTRA_CHP_waste"]),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_CHP_waste"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EASOC", "PROTRA_CHP_waste"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EASOC", "PROTRA_CHP_waste"]),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_CHP_waste"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_133",
)

_delayfixed_delay_land_use_efficiency_protra_134 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EASOC", "PROTRA_CHP_solid_bio"]),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_CHP_solid_bio"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EASOC", "PROTRA_CHP_solid_bio"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EASOC", "PROTRA_CHP_solid_bio"]),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_CHP_solid_bio"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_134",
)

_delayfixed_delay_land_use_efficiency_protra_135 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EASOC", "PROTRA_CHP_solid_bio_CCS"]),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_CHP_solid_bio_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EASOC", "PROTRA_CHP_solid_bio_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EASOC", "PROTRA_CHP_solid_bio_CCS"]),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_CHP_solid_bio_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_135",
)

_delayfixed_delay_land_use_efficiency_protra_136 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EASOC", "PROTRA_HP_gas_fuels"]),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_HP_gas_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EASOC", "PROTRA_HP_gas_fuels"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EASOC", "PROTRA_HP_gas_fuels"]),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_HP_gas_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_136",
)

_delayfixed_delay_land_use_efficiency_protra_137 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EASOC", "PROTRA_HP_solid_bio"]),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_HP_solid_bio"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EASOC", "PROTRA_HP_solid_bio"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EASOC", "PROTRA_HP_solid_bio"]),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_HP_solid_bio"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_137",
)

_delayfixed_delay_land_use_efficiency_protra_138 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EASOC", "PROTRA_HP_geothermal"]),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_HP_geothermal"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EASOC", "PROTRA_HP_geothermal"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EASOC", "PROTRA_HP_geothermal"]),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_HP_geothermal"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_138",
)

_delayfixed_delay_land_use_efficiency_protra_139 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EASOC", "PROTRA_HP_liquid_fuels"]),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_HP_liquid_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EASOC", "PROTRA_HP_liquid_fuels"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EASOC", "PROTRA_HP_liquid_fuels"]),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_HP_liquid_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_139",
)

_delayfixed_delay_land_use_efficiency_protra_140 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EASOC", "PROTRA_HP_solar_DEACTIVATED"]),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_HP_solar_DEACTIVATED"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EASOC", "PROTRA_HP_solar_DEACTIVATED"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EASOC", "PROTRA_HP_solar_DEACTIVATED"]),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_HP_solar_DEACTIVATED"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_140",
)

_delayfixed_delay_land_use_efficiency_protra_141 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EASOC", "PROTRA_HP_solid_fossil"]),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_HP_solid_fossil"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EASOC", "PROTRA_HP_solid_fossil"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EASOC", "PROTRA_HP_solid_fossil"]),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_HP_solid_fossil"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_141",
)

_delayfixed_delay_land_use_efficiency_protra_142 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EASOC", "PROTRA_HP_waste"]),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_HP_waste"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EASOC", "PROTRA_HP_waste"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EASOC", "PROTRA_HP_waste"]),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_HP_waste"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_142",
)

_delayfixed_delay_land_use_efficiency_protra_143 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EASOC", "PROTRA_PP_solid_bio"]),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_PP_solid_bio"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EASOC", "PROTRA_PP_solid_bio"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EASOC", "PROTRA_PP_solid_bio"]),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_PP_solid_bio"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_143",
)

_delayfixed_delay_land_use_efficiency_protra_144 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EASOC", "PROTRA_PP_solid_bio_CCS"]),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_PP_solid_bio_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EASOC", "PROTRA_PP_solid_bio_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EASOC", "PROTRA_PP_solid_bio_CCS"]),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_PP_solid_bio_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_144",
)

_delayfixed_delay_land_use_efficiency_protra_145 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EASOC", "PROTRA_PP_gas_fuels"]),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_PP_gas_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EASOC", "PROTRA_PP_gas_fuels"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EASOC", "PROTRA_PP_gas_fuels"]),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_PP_gas_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_145",
)

_delayfixed_delay_land_use_efficiency_protra_146 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EASOC", "PROTRA_PP_gas_fuels_CCS"]),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_PP_gas_fuels_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EASOC", "PROTRA_PP_gas_fuels_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EASOC", "PROTRA_PP_gas_fuels_CCS"]),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_PP_gas_fuels_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_146",
)

_delayfixed_delay_land_use_efficiency_protra_147 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EASOC", "PROTRA_PP_geothermal"]),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_PP_geothermal"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EASOC", "PROTRA_PP_geothermal"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EASOC", "PROTRA_PP_geothermal"]),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_PP_geothermal"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_147",
)

_delayfixed_delay_land_use_efficiency_protra_148 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EASOC", "PROTRA_PP_hydropower_dammed"]),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_PP_hydropower_dammed"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EASOC", "PROTRA_PP_hydropower_dammed"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EASOC", "PROTRA_PP_hydropower_dammed"]),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_PP_hydropower_dammed"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_148",
)

_delayfixed_delay_land_use_efficiency_protra_149 = DelayFixed(
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc[
                "EASOC", "PROTRA_PP_hydropower_run_of_river"
            ]
        ),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_PP_hydropower_run_of_river"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EASOC", "PROTRA_PP_hydropower_run_of_river"]),
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc[
                "EASOC", "PROTRA_PP_hydropower_run_of_river"
            ]
        ),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_PP_hydropower_run_of_river"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_149",
)

_delayfixed_delay_land_use_efficiency_protra_150 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EASOC", "PROTRA_PP_liquid_fuels"]),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_PP_liquid_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EASOC", "PROTRA_PP_liquid_fuels"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EASOC", "PROTRA_PP_liquid_fuels"]),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_PP_liquid_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_150",
)

_delayfixed_delay_land_use_efficiency_protra_151 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EASOC", "PROTRA_PP_liquid_fuels_CCS"]),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_PP_liquid_fuels_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EASOC", "PROTRA_PP_liquid_fuels_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EASOC", "PROTRA_PP_liquid_fuels_CCS"]),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_PP_liquid_fuels_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_151",
)

_delayfixed_delay_land_use_efficiency_protra_152 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EASOC", "PROTRA_PP_nuclear"]),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_PP_nuclear"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EASOC", "PROTRA_PP_nuclear"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EASOC", "PROTRA_PP_nuclear"]),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_PP_nuclear"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_152",
)

_delayfixed_delay_land_use_efficiency_protra_153 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EASOC", "PROTRA_PP_oceanic"]),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_PP_oceanic"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EASOC", "PROTRA_PP_oceanic"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EASOC", "PROTRA_PP_oceanic"]),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_PP_oceanic"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_153",
)

_delayfixed_delay_land_use_efficiency_protra_154 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EASOC", "PROTRA_PP_solar_CSP"]),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_PP_solar_CSP"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EASOC", "PROTRA_PP_solar_CSP"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EASOC", "PROTRA_PP_solar_CSP"]),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_PP_solar_CSP"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_154",
)

_delayfixed_delay_land_use_efficiency_protra_155 = DelayFixed(
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["EASOC", "PROTRA_PP_solar_open_space_PV"]
        ),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_PP_solar_open_space_PV"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EASOC", "PROTRA_PP_solar_open_space_PV"]),
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["EASOC", "PROTRA_PP_solar_open_space_PV"]
        ),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_PP_solar_open_space_PV"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_155",
)

_delayfixed_delay_land_use_efficiency_protra_156 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EASOC", "PROTRA_PP_solar_urban_PV"]),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_PP_solar_urban_PV"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EASOC", "PROTRA_PP_solar_urban_PV"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EASOC", "PROTRA_PP_solar_urban_PV"]),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_PP_solar_urban_PV"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_156",
)

_delayfixed_delay_land_use_efficiency_protra_157 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EASOC", "PROTRA_PP_solid_fossil"]),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_PP_solid_fossil"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EASOC", "PROTRA_PP_solid_fossil"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EASOC", "PROTRA_PP_solid_fossil"]),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_PP_solid_fossil"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_157",
)

_delayfixed_delay_land_use_efficiency_protra_158 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EASOC", "PROTRA_PP_solid_fossil_CCS"]),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_PP_solid_fossil_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EASOC", "PROTRA_PP_solid_fossil_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EASOC", "PROTRA_PP_solid_fossil_CCS"]),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_PP_solid_fossil_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_158",
)

_delayfixed_delay_land_use_efficiency_protra_159 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EASOC", "PROTRA_PP_waste"]),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_PP_waste"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EASOC", "PROTRA_PP_waste"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EASOC", "PROTRA_PP_waste"]),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_PP_waste"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_159",
)

_delayfixed_delay_land_use_efficiency_protra_160 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EASOC", "PROTRA_PP_waste_CCS"]),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_PP_waste_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EASOC", "PROTRA_PP_waste_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EASOC", "PROTRA_PP_waste_CCS"]),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_PP_waste_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_160",
)

_delayfixed_delay_land_use_efficiency_protra_161 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EASOC", "PROTRA_PP_wind_offshore"]),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_PP_wind_offshore"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EASOC", "PROTRA_PP_wind_offshore"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EASOC", "PROTRA_PP_wind_offshore"]),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_PP_wind_offshore"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_161",
)

_delayfixed_delay_land_use_efficiency_protra_162 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EASOC", "PROTRA_PP_wind_onshore"]),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_PP_wind_onshore"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EASOC", "PROTRA_PP_wind_onshore"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EASOC", "PROTRA_PP_wind_onshore"]),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_PP_wind_onshore"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_162",
)

_delayfixed_delay_land_use_efficiency_protra_163 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EASOC", "PROTRA_blending_gas_fuels"]),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_blending_gas_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EASOC", "PROTRA_blending_gas_fuels"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["EASOC", "PROTRA_blending_gas_fuels"]),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_blending_gas_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_163",
)

_delayfixed_delay_land_use_efficiency_protra_164 = DelayFixed(
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["EASOC", "PROTRA_blending_liquid_fuels"]
        ),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_blending_liquid_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EASOC", "PROTRA_blending_liquid_fuels"]),
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["EASOC", "PROTRA_blending_liquid_fuels"]
        ),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_blending_liquid_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_164",
)

_delayfixed_delay_land_use_efficiency_protra_165 = DelayFixed(
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["EASOC", "PROTRA_no_process_TI_hydrogen"]
        ),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_no_process_TI_hydrogen"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EASOC", "PROTRA_no_process_TI_hydrogen"]),
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["EASOC", "PROTRA_no_process_TI_hydrogen"]
        ),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_no_process_TI_hydrogen"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_165",
)

_delayfixed_delay_land_use_efficiency_protra_166 = DelayFixed(
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["EASOC", "PROTRA_no_process_TI_solid_bio"]
        ),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_no_process_TI_solid_bio"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EASOC", "PROTRA_no_process_TI_solid_bio"]),
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["EASOC", "PROTRA_no_process_TI_solid_bio"]
        ),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_no_process_TI_solid_bio"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_166",
)

_delayfixed_delay_land_use_efficiency_protra_167 = DelayFixed(
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc[
                "EASOC", "PROTRA_no_process_TI_solid_fossil"
            ]
        ),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_no_process_TI_solid_fossil"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["EASOC", "PROTRA_no_process_TI_solid_fossil"]),
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc[
                "EASOC", "PROTRA_no_process_TI_solid_fossil"
            ]
        ),
        {"REGIONS_35_I": ["EASOC"], "NRG_PRO_I": ["PROTRA_no_process_TI_solid_fossil"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_167",
)

_delayfixed_delay_land_use_efficiency_protra_168 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["INDIA", "PROTRA_CHP_gas_fuels"]),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_CHP_gas_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["INDIA", "PROTRA_CHP_gas_fuels"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["INDIA", "PROTRA_CHP_gas_fuels"]),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_CHP_gas_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_168",
)

_delayfixed_delay_land_use_efficiency_protra_169 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["INDIA", "PROTRA_CHP_gas_fuels_CCS"]),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_CHP_gas_fuels_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["INDIA", "PROTRA_CHP_gas_fuels_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["INDIA", "PROTRA_CHP_gas_fuels_CCS"]),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_CHP_gas_fuels_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_169",
)

_delayfixed_delay_land_use_efficiency_protra_170 = DelayFixed(
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc[
                "INDIA", "PROTRA_CHP_geothermal_DEACTIVATED"
            ]
        ),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_CHP_geothermal_DEACTIVATED"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["INDIA", "PROTRA_CHP_geothermal_DEACTIVATED"]),
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc[
                "INDIA", "PROTRA_CHP_geothermal_DEACTIVATED"
            ]
        ),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_CHP_geothermal_DEACTIVATED"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_170",
)

_delayfixed_delay_land_use_efficiency_protra_171 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["INDIA", "PROTRA_CHP_liquid_fuels"]),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_CHP_liquid_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["INDIA", "PROTRA_CHP_liquid_fuels"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["INDIA", "PROTRA_CHP_liquid_fuels"]),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_CHP_liquid_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_171",
)

_delayfixed_delay_land_use_efficiency_protra_172 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["INDIA", "PROTRA_CHP_liquid_fuels_CCS"]),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_CHP_liquid_fuels_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["INDIA", "PROTRA_CHP_liquid_fuels_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["INDIA", "PROTRA_CHP_liquid_fuels_CCS"]),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_CHP_liquid_fuels_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_172",
)

_delayfixed_delay_land_use_efficiency_protra_173 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["INDIA", "PROTRA_CHP_solid_fossil"]),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_CHP_solid_fossil"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["INDIA", "PROTRA_CHP_solid_fossil"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["INDIA", "PROTRA_CHP_solid_fossil"]),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_CHP_solid_fossil"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_173",
)

_delayfixed_delay_land_use_efficiency_protra_174 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["INDIA", "PROTRA_CHP_solid_fossil_CCS"]),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_CHP_solid_fossil_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["INDIA", "PROTRA_CHP_solid_fossil_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["INDIA", "PROTRA_CHP_solid_fossil_CCS"]),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_CHP_solid_fossil_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_174",
)

_delayfixed_delay_land_use_efficiency_protra_175 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["INDIA", "PROTRA_CHP_waste"]),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_CHP_waste"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["INDIA", "PROTRA_CHP_waste"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["INDIA", "PROTRA_CHP_waste"]),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_CHP_waste"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_175",
)

_delayfixed_delay_land_use_efficiency_protra_176 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["INDIA", "PROTRA_CHP_solid_bio"]),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_CHP_solid_bio"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["INDIA", "PROTRA_CHP_solid_bio"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["INDIA", "PROTRA_CHP_solid_bio"]),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_CHP_solid_bio"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_176",
)

_delayfixed_delay_land_use_efficiency_protra_177 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["INDIA", "PROTRA_CHP_solid_bio_CCS"]),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_CHP_solid_bio_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["INDIA", "PROTRA_CHP_solid_bio_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["INDIA", "PROTRA_CHP_solid_bio_CCS"]),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_CHP_solid_bio_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_177",
)

_delayfixed_delay_land_use_efficiency_protra_178 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["INDIA", "PROTRA_HP_gas_fuels"]),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_HP_gas_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["INDIA", "PROTRA_HP_gas_fuels"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["INDIA", "PROTRA_HP_gas_fuels"]),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_HP_gas_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_178",
)

_delayfixed_delay_land_use_efficiency_protra_179 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["INDIA", "PROTRA_HP_solid_bio"]),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_HP_solid_bio"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["INDIA", "PROTRA_HP_solid_bio"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["INDIA", "PROTRA_HP_solid_bio"]),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_HP_solid_bio"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_179",
)

_delayfixed_delay_land_use_efficiency_protra_180 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["INDIA", "PROTRA_HP_geothermal"]),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_HP_geothermal"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["INDIA", "PROTRA_HP_geothermal"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["INDIA", "PROTRA_HP_geothermal"]),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_HP_geothermal"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_180",
)

_delayfixed_delay_land_use_efficiency_protra_181 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["INDIA", "PROTRA_HP_liquid_fuels"]),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_HP_liquid_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["INDIA", "PROTRA_HP_liquid_fuels"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["INDIA", "PROTRA_HP_liquid_fuels"]),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_HP_liquid_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_181",
)

_delayfixed_delay_land_use_efficiency_protra_182 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["INDIA", "PROTRA_HP_solar_DEACTIVATED"]),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_HP_solar_DEACTIVATED"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["INDIA", "PROTRA_HP_solar_DEACTIVATED"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["INDIA", "PROTRA_HP_solar_DEACTIVATED"]),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_HP_solar_DEACTIVATED"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_182",
)

_delayfixed_delay_land_use_efficiency_protra_183 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["INDIA", "PROTRA_HP_solid_fossil"]),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_HP_solid_fossil"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["INDIA", "PROTRA_HP_solid_fossil"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["INDIA", "PROTRA_HP_solid_fossil"]),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_HP_solid_fossil"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_183",
)

_delayfixed_delay_land_use_efficiency_protra_184 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["INDIA", "PROTRA_HP_waste"]),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_HP_waste"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["INDIA", "PROTRA_HP_waste"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["INDIA", "PROTRA_HP_waste"]),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_HP_waste"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_184",
)

_delayfixed_delay_land_use_efficiency_protra_185 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["INDIA", "PROTRA_PP_solid_bio"]),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_PP_solid_bio"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["INDIA", "PROTRA_PP_solid_bio"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["INDIA", "PROTRA_PP_solid_bio"]),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_PP_solid_bio"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_185",
)

_delayfixed_delay_land_use_efficiency_protra_186 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["INDIA", "PROTRA_PP_solid_bio_CCS"]),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_PP_solid_bio_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["INDIA", "PROTRA_PP_solid_bio_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["INDIA", "PROTRA_PP_solid_bio_CCS"]),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_PP_solid_bio_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_186",
)

_delayfixed_delay_land_use_efficiency_protra_187 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["INDIA", "PROTRA_PP_gas_fuels"]),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_PP_gas_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["INDIA", "PROTRA_PP_gas_fuels"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["INDIA", "PROTRA_PP_gas_fuels"]),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_PP_gas_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_187",
)

_delayfixed_delay_land_use_efficiency_protra_188 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["INDIA", "PROTRA_PP_gas_fuels_CCS"]),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_PP_gas_fuels_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["INDIA", "PROTRA_PP_gas_fuels_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["INDIA", "PROTRA_PP_gas_fuels_CCS"]),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_PP_gas_fuels_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_188",
)

_delayfixed_delay_land_use_efficiency_protra_189 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["INDIA", "PROTRA_PP_geothermal"]),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_PP_geothermal"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["INDIA", "PROTRA_PP_geothermal"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["INDIA", "PROTRA_PP_geothermal"]),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_PP_geothermal"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_189",
)

_delayfixed_delay_land_use_efficiency_protra_190 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["INDIA", "PROTRA_PP_hydropower_dammed"]),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_PP_hydropower_dammed"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["INDIA", "PROTRA_PP_hydropower_dammed"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["INDIA", "PROTRA_PP_hydropower_dammed"]),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_PP_hydropower_dammed"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_190",
)

_delayfixed_delay_land_use_efficiency_protra_191 = DelayFixed(
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc[
                "INDIA", "PROTRA_PP_hydropower_run_of_river"
            ]
        ),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_PP_hydropower_run_of_river"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["INDIA", "PROTRA_PP_hydropower_run_of_river"]),
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc[
                "INDIA", "PROTRA_PP_hydropower_run_of_river"
            ]
        ),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_PP_hydropower_run_of_river"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_191",
)

_delayfixed_delay_land_use_efficiency_protra_192 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["INDIA", "PROTRA_PP_liquid_fuels"]),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_PP_liquid_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["INDIA", "PROTRA_PP_liquid_fuels"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["INDIA", "PROTRA_PP_liquid_fuels"]),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_PP_liquid_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_192",
)

_delayfixed_delay_land_use_efficiency_protra_193 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["INDIA", "PROTRA_PP_liquid_fuels_CCS"]),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_PP_liquid_fuels_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["INDIA", "PROTRA_PP_liquid_fuels_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["INDIA", "PROTRA_PP_liquid_fuels_CCS"]),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_PP_liquid_fuels_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_193",
)

_delayfixed_delay_land_use_efficiency_protra_194 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["INDIA", "PROTRA_PP_nuclear"]),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_PP_nuclear"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["INDIA", "PROTRA_PP_nuclear"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["INDIA", "PROTRA_PP_nuclear"]),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_PP_nuclear"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_194",
)

_delayfixed_delay_land_use_efficiency_protra_195 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["INDIA", "PROTRA_PP_oceanic"]),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_PP_oceanic"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["INDIA", "PROTRA_PP_oceanic"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["INDIA", "PROTRA_PP_oceanic"]),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_PP_oceanic"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_195",
)

_delayfixed_delay_land_use_efficiency_protra_196 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["INDIA", "PROTRA_PP_solar_CSP"]),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_PP_solar_CSP"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["INDIA", "PROTRA_PP_solar_CSP"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["INDIA", "PROTRA_PP_solar_CSP"]),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_PP_solar_CSP"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_196",
)

_delayfixed_delay_land_use_efficiency_protra_197 = DelayFixed(
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["INDIA", "PROTRA_PP_solar_open_space_PV"]
        ),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_PP_solar_open_space_PV"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["INDIA", "PROTRA_PP_solar_open_space_PV"]),
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["INDIA", "PROTRA_PP_solar_open_space_PV"]
        ),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_PP_solar_open_space_PV"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_197",
)

_delayfixed_delay_land_use_efficiency_protra_198 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["INDIA", "PROTRA_PP_solar_urban_PV"]),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_PP_solar_urban_PV"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["INDIA", "PROTRA_PP_solar_urban_PV"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["INDIA", "PROTRA_PP_solar_urban_PV"]),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_PP_solar_urban_PV"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_198",
)

_delayfixed_delay_land_use_efficiency_protra_199 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["INDIA", "PROTRA_PP_solid_fossil"]),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_PP_solid_fossil"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["INDIA", "PROTRA_PP_solid_fossil"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["INDIA", "PROTRA_PP_solid_fossil"]),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_PP_solid_fossil"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_199",
)

_delayfixed_delay_land_use_efficiency_protra_200 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["INDIA", "PROTRA_PP_solid_fossil_CCS"]),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_PP_solid_fossil_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["INDIA", "PROTRA_PP_solid_fossil_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["INDIA", "PROTRA_PP_solid_fossil_CCS"]),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_PP_solid_fossil_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_200",
)

_delayfixed_delay_land_use_efficiency_protra_201 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["INDIA", "PROTRA_PP_waste"]),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_PP_waste"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["INDIA", "PROTRA_PP_waste"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["INDIA", "PROTRA_PP_waste"]),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_PP_waste"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_201",
)

_delayfixed_delay_land_use_efficiency_protra_202 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["INDIA", "PROTRA_PP_waste_CCS"]),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_PP_waste_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["INDIA", "PROTRA_PP_waste_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["INDIA", "PROTRA_PP_waste_CCS"]),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_PP_waste_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_202",
)

_delayfixed_delay_land_use_efficiency_protra_203 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["INDIA", "PROTRA_PP_wind_offshore"]),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_PP_wind_offshore"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["INDIA", "PROTRA_PP_wind_offshore"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["INDIA", "PROTRA_PP_wind_offshore"]),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_PP_wind_offshore"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_203",
)

_delayfixed_delay_land_use_efficiency_protra_204 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["INDIA", "PROTRA_PP_wind_onshore"]),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_PP_wind_onshore"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["INDIA", "PROTRA_PP_wind_onshore"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["INDIA", "PROTRA_PP_wind_onshore"]),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_PP_wind_onshore"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_204",
)

_delayfixed_delay_land_use_efficiency_protra_205 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["INDIA", "PROTRA_blending_gas_fuels"]),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_blending_gas_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["INDIA", "PROTRA_blending_gas_fuels"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["INDIA", "PROTRA_blending_gas_fuels"]),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_blending_gas_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_205",
)

_delayfixed_delay_land_use_efficiency_protra_206 = DelayFixed(
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["INDIA", "PROTRA_blending_liquid_fuels"]
        ),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_blending_liquid_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["INDIA", "PROTRA_blending_liquid_fuels"]),
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["INDIA", "PROTRA_blending_liquid_fuels"]
        ),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_blending_liquid_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_206",
)

_delayfixed_delay_land_use_efficiency_protra_207 = DelayFixed(
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["INDIA", "PROTRA_no_process_TI_hydrogen"]
        ),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_no_process_TI_hydrogen"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["INDIA", "PROTRA_no_process_TI_hydrogen"]),
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["INDIA", "PROTRA_no_process_TI_hydrogen"]
        ),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_no_process_TI_hydrogen"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_207",
)

_delayfixed_delay_land_use_efficiency_protra_208 = DelayFixed(
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["INDIA", "PROTRA_no_process_TI_solid_bio"]
        ),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_no_process_TI_solid_bio"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["INDIA", "PROTRA_no_process_TI_solid_bio"]),
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["INDIA", "PROTRA_no_process_TI_solid_bio"]
        ),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_no_process_TI_solid_bio"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_208",
)

_delayfixed_delay_land_use_efficiency_protra_209 = DelayFixed(
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc[
                "INDIA", "PROTRA_no_process_TI_solid_fossil"
            ]
        ),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_no_process_TI_solid_fossil"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["INDIA", "PROTRA_no_process_TI_solid_fossil"]),
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc[
                "INDIA", "PROTRA_no_process_TI_solid_fossil"
            ]
        ),
        {"REGIONS_35_I": ["INDIA"], "NRG_PRO_I": ["PROTRA_no_process_TI_solid_fossil"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_209",
)

_delayfixed_delay_land_use_efficiency_protra_210 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LATAM", "PROTRA_CHP_gas_fuels"]),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_CHP_gas_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LATAM", "PROTRA_CHP_gas_fuels"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LATAM", "PROTRA_CHP_gas_fuels"]),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_CHP_gas_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_210",
)

_delayfixed_delay_land_use_efficiency_protra_211 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LATAM", "PROTRA_CHP_gas_fuels_CCS"]),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_CHP_gas_fuels_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LATAM", "PROTRA_CHP_gas_fuels_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LATAM", "PROTRA_CHP_gas_fuels_CCS"]),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_CHP_gas_fuels_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_211",
)

_delayfixed_delay_land_use_efficiency_protra_212 = DelayFixed(
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc[
                "LATAM", "PROTRA_CHP_geothermal_DEACTIVATED"
            ]
        ),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_CHP_geothermal_DEACTIVATED"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LATAM", "PROTRA_CHP_geothermal_DEACTIVATED"]),
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc[
                "LATAM", "PROTRA_CHP_geothermal_DEACTIVATED"
            ]
        ),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_CHP_geothermal_DEACTIVATED"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_212",
)

_delayfixed_delay_land_use_efficiency_protra_213 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LATAM", "PROTRA_CHP_liquid_fuels"]),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_CHP_liquid_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LATAM", "PROTRA_CHP_liquid_fuels"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LATAM", "PROTRA_CHP_liquid_fuels"]),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_CHP_liquid_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_213",
)

_delayfixed_delay_land_use_efficiency_protra_214 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LATAM", "PROTRA_CHP_liquid_fuels_CCS"]),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_CHP_liquid_fuels_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LATAM", "PROTRA_CHP_liquid_fuels_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LATAM", "PROTRA_CHP_liquid_fuels_CCS"]),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_CHP_liquid_fuels_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_214",
)

_delayfixed_delay_land_use_efficiency_protra_215 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LATAM", "PROTRA_CHP_solid_fossil"]),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_CHP_solid_fossil"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LATAM", "PROTRA_CHP_solid_fossil"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LATAM", "PROTRA_CHP_solid_fossil"]),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_CHP_solid_fossil"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_215",
)

_delayfixed_delay_land_use_efficiency_protra_216 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LATAM", "PROTRA_CHP_solid_fossil_CCS"]),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_CHP_solid_fossil_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LATAM", "PROTRA_CHP_solid_fossil_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LATAM", "PROTRA_CHP_solid_fossil_CCS"]),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_CHP_solid_fossil_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_216",
)

_delayfixed_delay_land_use_efficiency_protra_217 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LATAM", "PROTRA_CHP_waste"]),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_CHP_waste"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LATAM", "PROTRA_CHP_waste"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LATAM", "PROTRA_CHP_waste"]),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_CHP_waste"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_217",
)

_delayfixed_delay_land_use_efficiency_protra_218 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LATAM", "PROTRA_CHP_solid_bio"]),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_CHP_solid_bio"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LATAM", "PROTRA_CHP_solid_bio"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LATAM", "PROTRA_CHP_solid_bio"]),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_CHP_solid_bio"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_218",
)

_delayfixed_delay_land_use_efficiency_protra_219 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LATAM", "PROTRA_CHP_solid_bio_CCS"]),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_CHP_solid_bio_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LATAM", "PROTRA_CHP_solid_bio_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LATAM", "PROTRA_CHP_solid_bio_CCS"]),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_CHP_solid_bio_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_219",
)

_delayfixed_delay_land_use_efficiency_protra_220 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LATAM", "PROTRA_HP_gas_fuels"]),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_HP_gas_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LATAM", "PROTRA_HP_gas_fuels"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LATAM", "PROTRA_HP_gas_fuels"]),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_HP_gas_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_220",
)

_delayfixed_delay_land_use_efficiency_protra_221 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LATAM", "PROTRA_HP_solid_bio"]),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_HP_solid_bio"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LATAM", "PROTRA_HP_solid_bio"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LATAM", "PROTRA_HP_solid_bio"]),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_HP_solid_bio"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_221",
)

_delayfixed_delay_land_use_efficiency_protra_222 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LATAM", "PROTRA_HP_geothermal"]),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_HP_geothermal"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LATAM", "PROTRA_HP_geothermal"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LATAM", "PROTRA_HP_geothermal"]),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_HP_geothermal"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_222",
)

_delayfixed_delay_land_use_efficiency_protra_223 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LATAM", "PROTRA_HP_liquid_fuels"]),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_HP_liquid_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LATAM", "PROTRA_HP_liquid_fuels"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LATAM", "PROTRA_HP_liquid_fuels"]),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_HP_liquid_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_223",
)

_delayfixed_delay_land_use_efficiency_protra_224 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LATAM", "PROTRA_HP_solar_DEACTIVATED"]),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_HP_solar_DEACTIVATED"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LATAM", "PROTRA_HP_solar_DEACTIVATED"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LATAM", "PROTRA_HP_solar_DEACTIVATED"]),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_HP_solar_DEACTIVATED"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_224",
)

_delayfixed_delay_land_use_efficiency_protra_225 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LATAM", "PROTRA_HP_solid_fossil"]),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_HP_solid_fossil"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LATAM", "PROTRA_HP_solid_fossil"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LATAM", "PROTRA_HP_solid_fossil"]),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_HP_solid_fossil"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_225",
)

_delayfixed_delay_land_use_efficiency_protra_226 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LATAM", "PROTRA_HP_waste"]),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_HP_waste"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LATAM", "PROTRA_HP_waste"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LATAM", "PROTRA_HP_waste"]),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_HP_waste"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_226",
)

_delayfixed_delay_land_use_efficiency_protra_227 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LATAM", "PROTRA_PP_solid_bio"]),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_PP_solid_bio"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LATAM", "PROTRA_PP_solid_bio"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LATAM", "PROTRA_PP_solid_bio"]),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_PP_solid_bio"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_227",
)

_delayfixed_delay_land_use_efficiency_protra_228 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LATAM", "PROTRA_PP_solid_bio_CCS"]),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_PP_solid_bio_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LATAM", "PROTRA_PP_solid_bio_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LATAM", "PROTRA_PP_solid_bio_CCS"]),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_PP_solid_bio_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_228",
)

_delayfixed_delay_land_use_efficiency_protra_229 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LATAM", "PROTRA_PP_gas_fuels"]),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_PP_gas_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LATAM", "PROTRA_PP_gas_fuels"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LATAM", "PROTRA_PP_gas_fuels"]),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_PP_gas_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_229",
)

_delayfixed_delay_land_use_efficiency_protra_230 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LATAM", "PROTRA_PP_gas_fuels_CCS"]),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_PP_gas_fuels_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LATAM", "PROTRA_PP_gas_fuels_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LATAM", "PROTRA_PP_gas_fuels_CCS"]),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_PP_gas_fuels_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_230",
)

_delayfixed_delay_land_use_efficiency_protra_231 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LATAM", "PROTRA_PP_geothermal"]),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_PP_geothermal"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LATAM", "PROTRA_PP_geothermal"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LATAM", "PROTRA_PP_geothermal"]),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_PP_geothermal"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_231",
)

_delayfixed_delay_land_use_efficiency_protra_232 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LATAM", "PROTRA_PP_hydropower_dammed"]),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_PP_hydropower_dammed"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LATAM", "PROTRA_PP_hydropower_dammed"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LATAM", "PROTRA_PP_hydropower_dammed"]),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_PP_hydropower_dammed"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_232",
)

_delayfixed_delay_land_use_efficiency_protra_233 = DelayFixed(
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc[
                "LATAM", "PROTRA_PP_hydropower_run_of_river"
            ]
        ),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_PP_hydropower_run_of_river"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LATAM", "PROTRA_PP_hydropower_run_of_river"]),
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc[
                "LATAM", "PROTRA_PP_hydropower_run_of_river"
            ]
        ),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_PP_hydropower_run_of_river"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_233",
)

_delayfixed_delay_land_use_efficiency_protra_234 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LATAM", "PROTRA_PP_liquid_fuels"]),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_PP_liquid_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LATAM", "PROTRA_PP_liquid_fuels"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LATAM", "PROTRA_PP_liquid_fuels"]),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_PP_liquid_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_234",
)

_delayfixed_delay_land_use_efficiency_protra_235 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LATAM", "PROTRA_PP_liquid_fuels_CCS"]),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_PP_liquid_fuels_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LATAM", "PROTRA_PP_liquid_fuels_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LATAM", "PROTRA_PP_liquid_fuels_CCS"]),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_PP_liquid_fuels_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_235",
)

_delayfixed_delay_land_use_efficiency_protra_236 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LATAM", "PROTRA_PP_nuclear"]),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_PP_nuclear"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LATAM", "PROTRA_PP_nuclear"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LATAM", "PROTRA_PP_nuclear"]),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_PP_nuclear"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_236",
)

_delayfixed_delay_land_use_efficiency_protra_237 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LATAM", "PROTRA_PP_oceanic"]),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_PP_oceanic"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LATAM", "PROTRA_PP_oceanic"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LATAM", "PROTRA_PP_oceanic"]),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_PP_oceanic"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_237",
)

_delayfixed_delay_land_use_efficiency_protra_238 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LATAM", "PROTRA_PP_solar_CSP"]),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_PP_solar_CSP"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LATAM", "PROTRA_PP_solar_CSP"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LATAM", "PROTRA_PP_solar_CSP"]),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_PP_solar_CSP"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_238",
)

_delayfixed_delay_land_use_efficiency_protra_239 = DelayFixed(
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["LATAM", "PROTRA_PP_solar_open_space_PV"]
        ),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_PP_solar_open_space_PV"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LATAM", "PROTRA_PP_solar_open_space_PV"]),
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["LATAM", "PROTRA_PP_solar_open_space_PV"]
        ),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_PP_solar_open_space_PV"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_239",
)

_delayfixed_delay_land_use_efficiency_protra_240 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LATAM", "PROTRA_PP_solar_urban_PV"]),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_PP_solar_urban_PV"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LATAM", "PROTRA_PP_solar_urban_PV"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LATAM", "PROTRA_PP_solar_urban_PV"]),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_PP_solar_urban_PV"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_240",
)

_delayfixed_delay_land_use_efficiency_protra_241 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LATAM", "PROTRA_PP_solid_fossil"]),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_PP_solid_fossil"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LATAM", "PROTRA_PP_solid_fossil"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LATAM", "PROTRA_PP_solid_fossil"]),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_PP_solid_fossil"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_241",
)

_delayfixed_delay_land_use_efficiency_protra_242 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LATAM", "PROTRA_PP_solid_fossil_CCS"]),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_PP_solid_fossil_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LATAM", "PROTRA_PP_solid_fossil_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LATAM", "PROTRA_PP_solid_fossil_CCS"]),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_PP_solid_fossil_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_242",
)

_delayfixed_delay_land_use_efficiency_protra_243 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LATAM", "PROTRA_PP_waste"]),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_PP_waste"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LATAM", "PROTRA_PP_waste"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LATAM", "PROTRA_PP_waste"]),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_PP_waste"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_243",
)

_delayfixed_delay_land_use_efficiency_protra_244 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LATAM", "PROTRA_PP_waste_CCS"]),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_PP_waste_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LATAM", "PROTRA_PP_waste_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LATAM", "PROTRA_PP_waste_CCS"]),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_PP_waste_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_244",
)

_delayfixed_delay_land_use_efficiency_protra_245 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LATAM", "PROTRA_PP_wind_offshore"]),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_PP_wind_offshore"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LATAM", "PROTRA_PP_wind_offshore"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LATAM", "PROTRA_PP_wind_offshore"]),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_PP_wind_offshore"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_245",
)

_delayfixed_delay_land_use_efficiency_protra_246 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LATAM", "PROTRA_PP_wind_onshore"]),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_PP_wind_onshore"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LATAM", "PROTRA_PP_wind_onshore"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LATAM", "PROTRA_PP_wind_onshore"]),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_PP_wind_onshore"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_246",
)

_delayfixed_delay_land_use_efficiency_protra_247 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LATAM", "PROTRA_blending_gas_fuels"]),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_blending_gas_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LATAM", "PROTRA_blending_gas_fuels"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LATAM", "PROTRA_blending_gas_fuels"]),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_blending_gas_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_247",
)

_delayfixed_delay_land_use_efficiency_protra_248 = DelayFixed(
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["LATAM", "PROTRA_blending_liquid_fuels"]
        ),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_blending_liquid_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LATAM", "PROTRA_blending_liquid_fuels"]),
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["LATAM", "PROTRA_blending_liquid_fuels"]
        ),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_blending_liquid_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_248",
)

_delayfixed_delay_land_use_efficiency_protra_249 = DelayFixed(
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["LATAM", "PROTRA_no_process_TI_hydrogen"]
        ),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_no_process_TI_hydrogen"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LATAM", "PROTRA_no_process_TI_hydrogen"]),
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["LATAM", "PROTRA_no_process_TI_hydrogen"]
        ),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_no_process_TI_hydrogen"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_249",
)

_delayfixed_delay_land_use_efficiency_protra_250 = DelayFixed(
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["LATAM", "PROTRA_no_process_TI_solid_bio"]
        ),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_no_process_TI_solid_bio"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LATAM", "PROTRA_no_process_TI_solid_bio"]),
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["LATAM", "PROTRA_no_process_TI_solid_bio"]
        ),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_no_process_TI_solid_bio"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_250",
)

_delayfixed_delay_land_use_efficiency_protra_251 = DelayFixed(
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc[
                "LATAM", "PROTRA_no_process_TI_solid_fossil"
            ]
        ),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_no_process_TI_solid_fossil"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LATAM", "PROTRA_no_process_TI_solid_fossil"]),
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc[
                "LATAM", "PROTRA_no_process_TI_solid_fossil"
            ]
        ),
        {"REGIONS_35_I": ["LATAM"], "NRG_PRO_I": ["PROTRA_no_process_TI_solid_fossil"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_251",
)

_delayfixed_delay_land_use_efficiency_protra_252 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["RUSSIA", "PROTRA_CHP_gas_fuels"]),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_CHP_gas_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["RUSSIA", "PROTRA_CHP_gas_fuels"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["RUSSIA", "PROTRA_CHP_gas_fuels"]),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_CHP_gas_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_252",
)

_delayfixed_delay_land_use_efficiency_protra_253 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["RUSSIA", "PROTRA_CHP_gas_fuels_CCS"]),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_CHP_gas_fuels_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["RUSSIA", "PROTRA_CHP_gas_fuels_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["RUSSIA", "PROTRA_CHP_gas_fuels_CCS"]),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_CHP_gas_fuels_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_253",
)

_delayfixed_delay_land_use_efficiency_protra_254 = DelayFixed(
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc[
                "RUSSIA", "PROTRA_CHP_geothermal_DEACTIVATED"
            ]
        ),
        {
            "REGIONS_35_I": ["RUSSIA"],
            "NRG_PRO_I": ["PROTRA_CHP_geothermal_DEACTIVATED"],
        },
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["RUSSIA", "PROTRA_CHP_geothermal_DEACTIVATED"]),
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc[
                "RUSSIA", "PROTRA_CHP_geothermal_DEACTIVATED"
            ]
        ),
        {
            "REGIONS_35_I": ["RUSSIA"],
            "NRG_PRO_I": ["PROTRA_CHP_geothermal_DEACTIVATED"],
        },
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_254",
)

_delayfixed_delay_land_use_efficiency_protra_255 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["RUSSIA", "PROTRA_CHP_liquid_fuels"]),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_CHP_liquid_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["RUSSIA", "PROTRA_CHP_liquid_fuels"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["RUSSIA", "PROTRA_CHP_liquid_fuels"]),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_CHP_liquid_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_255",
)

_delayfixed_delay_land_use_efficiency_protra_256 = DelayFixed(
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["RUSSIA", "PROTRA_CHP_liquid_fuels_CCS"]
        ),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_CHP_liquid_fuels_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["RUSSIA", "PROTRA_CHP_liquid_fuels_CCS"]),
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["RUSSIA", "PROTRA_CHP_liquid_fuels_CCS"]
        ),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_CHP_liquid_fuels_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_256",
)

_delayfixed_delay_land_use_efficiency_protra_257 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["RUSSIA", "PROTRA_CHP_solid_fossil"]),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_CHP_solid_fossil"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["RUSSIA", "PROTRA_CHP_solid_fossil"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["RUSSIA", "PROTRA_CHP_solid_fossil"]),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_CHP_solid_fossil"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_257",
)

_delayfixed_delay_land_use_efficiency_protra_258 = DelayFixed(
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["RUSSIA", "PROTRA_CHP_solid_fossil_CCS"]
        ),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_CHP_solid_fossil_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["RUSSIA", "PROTRA_CHP_solid_fossil_CCS"]),
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["RUSSIA", "PROTRA_CHP_solid_fossil_CCS"]
        ),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_CHP_solid_fossil_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_258",
)

_delayfixed_delay_land_use_efficiency_protra_259 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["RUSSIA", "PROTRA_CHP_waste"]),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_CHP_waste"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["RUSSIA", "PROTRA_CHP_waste"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["RUSSIA", "PROTRA_CHP_waste"]),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_CHP_waste"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_259",
)

_delayfixed_delay_land_use_efficiency_protra_260 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["RUSSIA", "PROTRA_CHP_solid_bio"]),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_CHP_solid_bio"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["RUSSIA", "PROTRA_CHP_solid_bio"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["RUSSIA", "PROTRA_CHP_solid_bio"]),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_CHP_solid_bio"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_260",
)

_delayfixed_delay_land_use_efficiency_protra_261 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["RUSSIA", "PROTRA_CHP_solid_bio_CCS"]),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_CHP_solid_bio_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["RUSSIA", "PROTRA_CHP_solid_bio_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["RUSSIA", "PROTRA_CHP_solid_bio_CCS"]),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_CHP_solid_bio_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_261",
)

_delayfixed_delay_land_use_efficiency_protra_262 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["RUSSIA", "PROTRA_HP_gas_fuels"]),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_HP_gas_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["RUSSIA", "PROTRA_HP_gas_fuels"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["RUSSIA", "PROTRA_HP_gas_fuels"]),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_HP_gas_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_262",
)

_delayfixed_delay_land_use_efficiency_protra_263 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["RUSSIA", "PROTRA_HP_solid_bio"]),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_HP_solid_bio"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["RUSSIA", "PROTRA_HP_solid_bio"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["RUSSIA", "PROTRA_HP_solid_bio"]),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_HP_solid_bio"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_263",
)

_delayfixed_delay_land_use_efficiency_protra_264 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["RUSSIA", "PROTRA_HP_geothermal"]),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_HP_geothermal"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["RUSSIA", "PROTRA_HP_geothermal"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["RUSSIA", "PROTRA_HP_geothermal"]),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_HP_geothermal"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_264",
)

_delayfixed_delay_land_use_efficiency_protra_265 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["RUSSIA", "PROTRA_HP_liquid_fuels"]),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_HP_liquid_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["RUSSIA", "PROTRA_HP_liquid_fuels"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["RUSSIA", "PROTRA_HP_liquid_fuels"]),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_HP_liquid_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_265",
)

_delayfixed_delay_land_use_efficiency_protra_266 = DelayFixed(
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["RUSSIA", "PROTRA_HP_solar_DEACTIVATED"]
        ),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_HP_solar_DEACTIVATED"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["RUSSIA", "PROTRA_HP_solar_DEACTIVATED"]),
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["RUSSIA", "PROTRA_HP_solar_DEACTIVATED"]
        ),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_HP_solar_DEACTIVATED"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_266",
)

_delayfixed_delay_land_use_efficiency_protra_267 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["RUSSIA", "PROTRA_HP_solid_fossil"]),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_HP_solid_fossil"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["RUSSIA", "PROTRA_HP_solid_fossil"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["RUSSIA", "PROTRA_HP_solid_fossil"]),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_HP_solid_fossil"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_267",
)

_delayfixed_delay_land_use_efficiency_protra_268 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["RUSSIA", "PROTRA_HP_waste"]),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_HP_waste"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["RUSSIA", "PROTRA_HP_waste"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["RUSSIA", "PROTRA_HP_waste"]),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_HP_waste"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_268",
)

_delayfixed_delay_land_use_efficiency_protra_269 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["RUSSIA", "PROTRA_PP_solid_bio"]),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_PP_solid_bio"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["RUSSIA", "PROTRA_PP_solid_bio"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["RUSSIA", "PROTRA_PP_solid_bio"]),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_PP_solid_bio"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_269",
)

_delayfixed_delay_land_use_efficiency_protra_270 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["RUSSIA", "PROTRA_PP_solid_bio_CCS"]),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_PP_solid_bio_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["RUSSIA", "PROTRA_PP_solid_bio_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["RUSSIA", "PROTRA_PP_solid_bio_CCS"]),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_PP_solid_bio_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_270",
)

_delayfixed_delay_land_use_efficiency_protra_271 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["RUSSIA", "PROTRA_PP_gas_fuels"]),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_PP_gas_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["RUSSIA", "PROTRA_PP_gas_fuels"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["RUSSIA", "PROTRA_PP_gas_fuels"]),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_PP_gas_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_271",
)

_delayfixed_delay_land_use_efficiency_protra_272 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["RUSSIA", "PROTRA_PP_gas_fuels_CCS"]),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_PP_gas_fuels_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["RUSSIA", "PROTRA_PP_gas_fuels_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["RUSSIA", "PROTRA_PP_gas_fuels_CCS"]),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_PP_gas_fuels_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_272",
)

_delayfixed_delay_land_use_efficiency_protra_273 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["RUSSIA", "PROTRA_PP_geothermal"]),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_PP_geothermal"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["RUSSIA", "PROTRA_PP_geothermal"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["RUSSIA", "PROTRA_PP_geothermal"]),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_PP_geothermal"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_273",
)

_delayfixed_delay_land_use_efficiency_protra_274 = DelayFixed(
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["RUSSIA", "PROTRA_PP_hydropower_dammed"]
        ),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_PP_hydropower_dammed"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["RUSSIA", "PROTRA_PP_hydropower_dammed"]),
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["RUSSIA", "PROTRA_PP_hydropower_dammed"]
        ),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_PP_hydropower_dammed"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_274",
)

_delayfixed_delay_land_use_efficiency_protra_275 = DelayFixed(
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc[
                "RUSSIA", "PROTRA_PP_hydropower_run_of_river"
            ]
        ),
        {
            "REGIONS_35_I": ["RUSSIA"],
            "NRG_PRO_I": ["PROTRA_PP_hydropower_run_of_river"],
        },
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["RUSSIA", "PROTRA_PP_hydropower_run_of_river"]),
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc[
                "RUSSIA", "PROTRA_PP_hydropower_run_of_river"
            ]
        ),
        {
            "REGIONS_35_I": ["RUSSIA"],
            "NRG_PRO_I": ["PROTRA_PP_hydropower_run_of_river"],
        },
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_275",
)

_delayfixed_delay_land_use_efficiency_protra_276 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["RUSSIA", "PROTRA_PP_liquid_fuels"]),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_PP_liquid_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["RUSSIA", "PROTRA_PP_liquid_fuels"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["RUSSIA", "PROTRA_PP_liquid_fuels"]),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_PP_liquid_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_276",
)

_delayfixed_delay_land_use_efficiency_protra_277 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["RUSSIA", "PROTRA_PP_liquid_fuels_CCS"]),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_PP_liquid_fuels_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["RUSSIA", "PROTRA_PP_liquid_fuels_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["RUSSIA", "PROTRA_PP_liquid_fuels_CCS"]),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_PP_liquid_fuels_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_277",
)

_delayfixed_delay_land_use_efficiency_protra_278 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["RUSSIA", "PROTRA_PP_nuclear"]),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_PP_nuclear"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["RUSSIA", "PROTRA_PP_nuclear"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["RUSSIA", "PROTRA_PP_nuclear"]),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_PP_nuclear"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_278",
)

_delayfixed_delay_land_use_efficiency_protra_279 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["RUSSIA", "PROTRA_PP_oceanic"]),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_PP_oceanic"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["RUSSIA", "PROTRA_PP_oceanic"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["RUSSIA", "PROTRA_PP_oceanic"]),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_PP_oceanic"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_279",
)

_delayfixed_delay_land_use_efficiency_protra_280 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["RUSSIA", "PROTRA_PP_solar_CSP"]),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_PP_solar_CSP"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["RUSSIA", "PROTRA_PP_solar_CSP"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["RUSSIA", "PROTRA_PP_solar_CSP"]),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_PP_solar_CSP"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_280",
)

_delayfixed_delay_land_use_efficiency_protra_281 = DelayFixed(
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["RUSSIA", "PROTRA_PP_solar_open_space_PV"]
        ),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_PP_solar_open_space_PV"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["RUSSIA", "PROTRA_PP_solar_open_space_PV"]),
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["RUSSIA", "PROTRA_PP_solar_open_space_PV"]
        ),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_PP_solar_open_space_PV"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_281",
)

_delayfixed_delay_land_use_efficiency_protra_282 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["RUSSIA", "PROTRA_PP_solar_urban_PV"]),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_PP_solar_urban_PV"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["RUSSIA", "PROTRA_PP_solar_urban_PV"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["RUSSIA", "PROTRA_PP_solar_urban_PV"]),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_PP_solar_urban_PV"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_282",
)

_delayfixed_delay_land_use_efficiency_protra_283 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["RUSSIA", "PROTRA_PP_solid_fossil"]),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_PP_solid_fossil"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["RUSSIA", "PROTRA_PP_solid_fossil"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["RUSSIA", "PROTRA_PP_solid_fossil"]),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_PP_solid_fossil"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_283",
)

_delayfixed_delay_land_use_efficiency_protra_284 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["RUSSIA", "PROTRA_PP_solid_fossil_CCS"]),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_PP_solid_fossil_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["RUSSIA", "PROTRA_PP_solid_fossil_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["RUSSIA", "PROTRA_PP_solid_fossil_CCS"]),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_PP_solid_fossil_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_284",
)

_delayfixed_delay_land_use_efficiency_protra_285 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["RUSSIA", "PROTRA_PP_waste"]),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_PP_waste"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["RUSSIA", "PROTRA_PP_waste"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["RUSSIA", "PROTRA_PP_waste"]),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_PP_waste"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_285",
)

_delayfixed_delay_land_use_efficiency_protra_286 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["RUSSIA", "PROTRA_PP_waste_CCS"]),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_PP_waste_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["RUSSIA", "PROTRA_PP_waste_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["RUSSIA", "PROTRA_PP_waste_CCS"]),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_PP_waste_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_286",
)

_delayfixed_delay_land_use_efficiency_protra_287 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["RUSSIA", "PROTRA_PP_wind_offshore"]),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_PP_wind_offshore"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["RUSSIA", "PROTRA_PP_wind_offshore"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["RUSSIA", "PROTRA_PP_wind_offshore"]),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_PP_wind_offshore"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_287",
)

_delayfixed_delay_land_use_efficiency_protra_288 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["RUSSIA", "PROTRA_PP_wind_onshore"]),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_PP_wind_onshore"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["RUSSIA", "PROTRA_PP_wind_onshore"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["RUSSIA", "PROTRA_PP_wind_onshore"]),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_PP_wind_onshore"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_288",
)

_delayfixed_delay_land_use_efficiency_protra_289 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["RUSSIA", "PROTRA_blending_gas_fuels"]),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_blending_gas_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["RUSSIA", "PROTRA_blending_gas_fuels"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["RUSSIA", "PROTRA_blending_gas_fuels"]),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_blending_gas_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_289",
)

_delayfixed_delay_land_use_efficiency_protra_290 = DelayFixed(
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["RUSSIA", "PROTRA_blending_liquid_fuels"]
        ),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_blending_liquid_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["RUSSIA", "PROTRA_blending_liquid_fuels"]),
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["RUSSIA", "PROTRA_blending_liquid_fuels"]
        ),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_blending_liquid_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_290",
)

_delayfixed_delay_land_use_efficiency_protra_291 = DelayFixed(
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["RUSSIA", "PROTRA_no_process_TI_hydrogen"]
        ),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_no_process_TI_hydrogen"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["RUSSIA", "PROTRA_no_process_TI_hydrogen"]),
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["RUSSIA", "PROTRA_no_process_TI_hydrogen"]
        ),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_no_process_TI_hydrogen"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_291",
)

_delayfixed_delay_land_use_efficiency_protra_292 = DelayFixed(
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["RUSSIA", "PROTRA_no_process_TI_solid_bio"]
        ),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_no_process_TI_solid_bio"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["RUSSIA", "PROTRA_no_process_TI_solid_bio"]),
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["RUSSIA", "PROTRA_no_process_TI_solid_bio"]
        ),
        {"REGIONS_35_I": ["RUSSIA"], "NRG_PRO_I": ["PROTRA_no_process_TI_solid_bio"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_292",
)

_delayfixed_delay_land_use_efficiency_protra_293 = DelayFixed(
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc[
                "RUSSIA", "PROTRA_no_process_TI_solid_fossil"
            ]
        ),
        {
            "REGIONS_35_I": ["RUSSIA"],
            "NRG_PRO_I": ["PROTRA_no_process_TI_solid_fossil"],
        },
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["RUSSIA", "PROTRA_no_process_TI_solid_fossil"]),
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc[
                "RUSSIA", "PROTRA_no_process_TI_solid_fossil"
            ]
        ),
        {
            "REGIONS_35_I": ["RUSSIA"],
            "NRG_PRO_I": ["PROTRA_no_process_TI_solid_fossil"],
        },
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_293",
)

_delayfixed_delay_land_use_efficiency_protra_294 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["USMCA", "PROTRA_CHP_gas_fuels"]),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_CHP_gas_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["USMCA", "PROTRA_CHP_gas_fuels"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["USMCA", "PROTRA_CHP_gas_fuels"]),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_CHP_gas_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_294",
)

_delayfixed_delay_land_use_efficiency_protra_295 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["USMCA", "PROTRA_CHP_gas_fuels_CCS"]),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_CHP_gas_fuels_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["USMCA", "PROTRA_CHP_gas_fuels_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["USMCA", "PROTRA_CHP_gas_fuels_CCS"]),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_CHP_gas_fuels_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_295",
)

_delayfixed_delay_land_use_efficiency_protra_296 = DelayFixed(
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc[
                "USMCA", "PROTRA_CHP_geothermal_DEACTIVATED"
            ]
        ),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_CHP_geothermal_DEACTIVATED"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["USMCA", "PROTRA_CHP_geothermal_DEACTIVATED"]),
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc[
                "USMCA", "PROTRA_CHP_geothermal_DEACTIVATED"
            ]
        ),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_CHP_geothermal_DEACTIVATED"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_296",
)

_delayfixed_delay_land_use_efficiency_protra_297 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["USMCA", "PROTRA_CHP_liquid_fuels"]),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_CHP_liquid_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["USMCA", "PROTRA_CHP_liquid_fuels"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["USMCA", "PROTRA_CHP_liquid_fuels"]),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_CHP_liquid_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_297",
)

_delayfixed_delay_land_use_efficiency_protra_298 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["USMCA", "PROTRA_CHP_liquid_fuels_CCS"]),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_CHP_liquid_fuels_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["USMCA", "PROTRA_CHP_liquid_fuels_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["USMCA", "PROTRA_CHP_liquid_fuels_CCS"]),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_CHP_liquid_fuels_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_298",
)

_delayfixed_delay_land_use_efficiency_protra_299 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["USMCA", "PROTRA_CHP_solid_fossil"]),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_CHP_solid_fossil"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["USMCA", "PROTRA_CHP_solid_fossil"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["USMCA", "PROTRA_CHP_solid_fossil"]),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_CHP_solid_fossil"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_299",
)

_delayfixed_delay_land_use_efficiency_protra_300 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["USMCA", "PROTRA_CHP_solid_fossil_CCS"]),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_CHP_solid_fossil_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["USMCA", "PROTRA_CHP_solid_fossil_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["USMCA", "PROTRA_CHP_solid_fossil_CCS"]),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_CHP_solid_fossil_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_300",
)

_delayfixed_delay_land_use_efficiency_protra_301 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["USMCA", "PROTRA_CHP_waste"]),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_CHP_waste"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["USMCA", "PROTRA_CHP_waste"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["USMCA", "PROTRA_CHP_waste"]),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_CHP_waste"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_301",
)

_delayfixed_delay_land_use_efficiency_protra_302 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["USMCA", "PROTRA_CHP_solid_bio"]),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_CHP_solid_bio"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["USMCA", "PROTRA_CHP_solid_bio"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["USMCA", "PROTRA_CHP_solid_bio"]),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_CHP_solid_bio"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_302",
)

_delayfixed_delay_land_use_efficiency_protra_303 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["USMCA", "PROTRA_CHP_solid_bio_CCS"]),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_CHP_solid_bio_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["USMCA", "PROTRA_CHP_solid_bio_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["USMCA", "PROTRA_CHP_solid_bio_CCS"]),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_CHP_solid_bio_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_303",
)

_delayfixed_delay_land_use_efficiency_protra_304 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["USMCA", "PROTRA_HP_gas_fuels"]),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_HP_gas_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["USMCA", "PROTRA_HP_gas_fuels"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["USMCA", "PROTRA_HP_gas_fuels"]),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_HP_gas_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_304",
)

_delayfixed_delay_land_use_efficiency_protra_305 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["USMCA", "PROTRA_HP_solid_bio"]),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_HP_solid_bio"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["USMCA", "PROTRA_HP_solid_bio"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["USMCA", "PROTRA_HP_solid_bio"]),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_HP_solid_bio"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_305",
)

_delayfixed_delay_land_use_efficiency_protra_306 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["USMCA", "PROTRA_HP_geothermal"]),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_HP_geothermal"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["USMCA", "PROTRA_HP_geothermal"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["USMCA", "PROTRA_HP_geothermal"]),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_HP_geothermal"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_306",
)

_delayfixed_delay_land_use_efficiency_protra_307 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["USMCA", "PROTRA_HP_liquid_fuels"]),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_HP_liquid_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["USMCA", "PROTRA_HP_liquid_fuels"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["USMCA", "PROTRA_HP_liquid_fuels"]),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_HP_liquid_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_307",
)

_delayfixed_delay_land_use_efficiency_protra_308 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["USMCA", "PROTRA_HP_solar_DEACTIVATED"]),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_HP_solar_DEACTIVATED"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["USMCA", "PROTRA_HP_solar_DEACTIVATED"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["USMCA", "PROTRA_HP_solar_DEACTIVATED"]),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_HP_solar_DEACTIVATED"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_308",
)

_delayfixed_delay_land_use_efficiency_protra_309 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["USMCA", "PROTRA_HP_solid_fossil"]),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_HP_solid_fossil"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["USMCA", "PROTRA_HP_solid_fossil"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["USMCA", "PROTRA_HP_solid_fossil"]),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_HP_solid_fossil"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_309",
)

_delayfixed_delay_land_use_efficiency_protra_310 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["USMCA", "PROTRA_HP_waste"]),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_HP_waste"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["USMCA", "PROTRA_HP_waste"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["USMCA", "PROTRA_HP_waste"]),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_HP_waste"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_310",
)

_delayfixed_delay_land_use_efficiency_protra_311 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["USMCA", "PROTRA_PP_solid_bio"]),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_PP_solid_bio"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["USMCA", "PROTRA_PP_solid_bio"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["USMCA", "PROTRA_PP_solid_bio"]),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_PP_solid_bio"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_311",
)

_delayfixed_delay_land_use_efficiency_protra_312 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["USMCA", "PROTRA_PP_solid_bio_CCS"]),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_PP_solid_bio_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["USMCA", "PROTRA_PP_solid_bio_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["USMCA", "PROTRA_PP_solid_bio_CCS"]),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_PP_solid_bio_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_312",
)

_delayfixed_delay_land_use_efficiency_protra_313 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["USMCA", "PROTRA_PP_gas_fuels"]),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_PP_gas_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["USMCA", "PROTRA_PP_gas_fuels"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["USMCA", "PROTRA_PP_gas_fuels"]),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_PP_gas_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_313",
)

_delayfixed_delay_land_use_efficiency_protra_314 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["USMCA", "PROTRA_PP_gas_fuels_CCS"]),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_PP_gas_fuels_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["USMCA", "PROTRA_PP_gas_fuels_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["USMCA", "PROTRA_PP_gas_fuels_CCS"]),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_PP_gas_fuels_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_314",
)

_delayfixed_delay_land_use_efficiency_protra_315 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["USMCA", "PROTRA_PP_geothermal"]),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_PP_geothermal"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["USMCA", "PROTRA_PP_geothermal"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["USMCA", "PROTRA_PP_geothermal"]),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_PP_geothermal"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_315",
)

_delayfixed_delay_land_use_efficiency_protra_316 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["USMCA", "PROTRA_PP_hydropower_dammed"]),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_PP_hydropower_dammed"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["USMCA", "PROTRA_PP_hydropower_dammed"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["USMCA", "PROTRA_PP_hydropower_dammed"]),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_PP_hydropower_dammed"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_316",
)

_delayfixed_delay_land_use_efficiency_protra_317 = DelayFixed(
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc[
                "USMCA", "PROTRA_PP_hydropower_run_of_river"
            ]
        ),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_PP_hydropower_run_of_river"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["USMCA", "PROTRA_PP_hydropower_run_of_river"]),
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc[
                "USMCA", "PROTRA_PP_hydropower_run_of_river"
            ]
        ),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_PP_hydropower_run_of_river"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_317",
)

_delayfixed_delay_land_use_efficiency_protra_318 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["USMCA", "PROTRA_PP_liquid_fuels"]),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_PP_liquid_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["USMCA", "PROTRA_PP_liquid_fuels"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["USMCA", "PROTRA_PP_liquid_fuels"]),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_PP_liquid_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_318",
)

_delayfixed_delay_land_use_efficiency_protra_319 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["USMCA", "PROTRA_PP_liquid_fuels_CCS"]),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_PP_liquid_fuels_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["USMCA", "PROTRA_PP_liquid_fuels_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["USMCA", "PROTRA_PP_liquid_fuels_CCS"]),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_PP_liquid_fuels_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_319",
)

_delayfixed_delay_land_use_efficiency_protra_320 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["USMCA", "PROTRA_PP_nuclear"]),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_PP_nuclear"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["USMCA", "PROTRA_PP_nuclear"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["USMCA", "PROTRA_PP_nuclear"]),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_PP_nuclear"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_320",
)

_delayfixed_delay_land_use_efficiency_protra_321 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["USMCA", "PROTRA_PP_oceanic"]),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_PP_oceanic"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["USMCA", "PROTRA_PP_oceanic"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["USMCA", "PROTRA_PP_oceanic"]),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_PP_oceanic"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_321",
)

_delayfixed_delay_land_use_efficiency_protra_322 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["USMCA", "PROTRA_PP_solar_CSP"]),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_PP_solar_CSP"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["USMCA", "PROTRA_PP_solar_CSP"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["USMCA", "PROTRA_PP_solar_CSP"]),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_PP_solar_CSP"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_322",
)

_delayfixed_delay_land_use_efficiency_protra_323 = DelayFixed(
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["USMCA", "PROTRA_PP_solar_open_space_PV"]
        ),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_PP_solar_open_space_PV"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["USMCA", "PROTRA_PP_solar_open_space_PV"]),
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["USMCA", "PROTRA_PP_solar_open_space_PV"]
        ),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_PP_solar_open_space_PV"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_323",
)

_delayfixed_delay_land_use_efficiency_protra_324 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["USMCA", "PROTRA_PP_solar_urban_PV"]),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_PP_solar_urban_PV"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["USMCA", "PROTRA_PP_solar_urban_PV"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["USMCA", "PROTRA_PP_solar_urban_PV"]),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_PP_solar_urban_PV"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_324",
)

_delayfixed_delay_land_use_efficiency_protra_325 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["USMCA", "PROTRA_PP_solid_fossil"]),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_PP_solid_fossil"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["USMCA", "PROTRA_PP_solid_fossil"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["USMCA", "PROTRA_PP_solid_fossil"]),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_PP_solid_fossil"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_325",
)

_delayfixed_delay_land_use_efficiency_protra_326 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["USMCA", "PROTRA_PP_solid_fossil_CCS"]),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_PP_solid_fossil_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["USMCA", "PROTRA_PP_solid_fossil_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["USMCA", "PROTRA_PP_solid_fossil_CCS"]),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_PP_solid_fossil_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_326",
)

_delayfixed_delay_land_use_efficiency_protra_327 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["USMCA", "PROTRA_PP_waste"]),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_PP_waste"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["USMCA", "PROTRA_PP_waste"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["USMCA", "PROTRA_PP_waste"]),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_PP_waste"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_327",
)

_delayfixed_delay_land_use_efficiency_protra_328 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["USMCA", "PROTRA_PP_waste_CCS"]),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_PP_waste_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["USMCA", "PROTRA_PP_waste_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["USMCA", "PROTRA_PP_waste_CCS"]),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_PP_waste_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_328",
)

_delayfixed_delay_land_use_efficiency_protra_329 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["USMCA", "PROTRA_PP_wind_offshore"]),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_PP_wind_offshore"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["USMCA", "PROTRA_PP_wind_offshore"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["USMCA", "PROTRA_PP_wind_offshore"]),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_PP_wind_offshore"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_329",
)

_delayfixed_delay_land_use_efficiency_protra_330 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["USMCA", "PROTRA_PP_wind_onshore"]),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_PP_wind_onshore"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["USMCA", "PROTRA_PP_wind_onshore"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["USMCA", "PROTRA_PP_wind_onshore"]),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_PP_wind_onshore"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_330",
)

_delayfixed_delay_land_use_efficiency_protra_331 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["USMCA", "PROTRA_blending_gas_fuels"]),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_blending_gas_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["USMCA", "PROTRA_blending_gas_fuels"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["USMCA", "PROTRA_blending_gas_fuels"]),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_blending_gas_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_331",
)

_delayfixed_delay_land_use_efficiency_protra_332 = DelayFixed(
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["USMCA", "PROTRA_blending_liquid_fuels"]
        ),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_blending_liquid_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["USMCA", "PROTRA_blending_liquid_fuels"]),
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["USMCA", "PROTRA_blending_liquid_fuels"]
        ),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_blending_liquid_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_332",
)

_delayfixed_delay_land_use_efficiency_protra_333 = DelayFixed(
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["USMCA", "PROTRA_no_process_TI_hydrogen"]
        ),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_no_process_TI_hydrogen"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["USMCA", "PROTRA_no_process_TI_hydrogen"]),
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["USMCA", "PROTRA_no_process_TI_hydrogen"]
        ),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_no_process_TI_hydrogen"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_333",
)

_delayfixed_delay_land_use_efficiency_protra_334 = DelayFixed(
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["USMCA", "PROTRA_no_process_TI_solid_bio"]
        ),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_no_process_TI_solid_bio"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["USMCA", "PROTRA_no_process_TI_solid_bio"]),
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["USMCA", "PROTRA_no_process_TI_solid_bio"]
        ),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_no_process_TI_solid_bio"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_334",
)

_delayfixed_delay_land_use_efficiency_protra_335 = DelayFixed(
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc[
                "USMCA", "PROTRA_no_process_TI_solid_fossil"
            ]
        ),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_no_process_TI_solid_fossil"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["USMCA", "PROTRA_no_process_TI_solid_fossil"]),
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc[
                "USMCA", "PROTRA_no_process_TI_solid_fossil"
            ]
        ),
        {"REGIONS_35_I": ["USMCA"], "NRG_PRO_I": ["PROTRA_no_process_TI_solid_fossil"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_335",
)

_delayfixed_delay_land_use_efficiency_protra_336 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_CHP_gas_fuels"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_CHP_gas_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LROW", "PROTRA_CHP_gas_fuels"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_CHP_gas_fuels"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_CHP_gas_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_336",
)

_delayfixed_delay_land_use_efficiency_protra_337 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_CHP_gas_fuels_CCS"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_CHP_gas_fuels_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LROW", "PROTRA_CHP_gas_fuels_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_CHP_gas_fuels_CCS"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_CHP_gas_fuels_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_337",
)

_delayfixed_delay_land_use_efficiency_protra_338 = DelayFixed(
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc[
                "LROW", "PROTRA_CHP_geothermal_DEACTIVATED"
            ]
        ),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_CHP_geothermal_DEACTIVATED"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LROW", "PROTRA_CHP_geothermal_DEACTIVATED"]),
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc[
                "LROW", "PROTRA_CHP_geothermal_DEACTIVATED"
            ]
        ),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_CHP_geothermal_DEACTIVATED"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_338",
)

_delayfixed_delay_land_use_efficiency_protra_339 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_CHP_liquid_fuels"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_CHP_liquid_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LROW", "PROTRA_CHP_liquid_fuels"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_CHP_liquid_fuels"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_CHP_liquid_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_339",
)

_delayfixed_delay_land_use_efficiency_protra_340 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_CHP_liquid_fuels_CCS"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_CHP_liquid_fuels_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LROW", "PROTRA_CHP_liquid_fuels_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_CHP_liquid_fuels_CCS"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_CHP_liquid_fuels_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_340",
)

_delayfixed_delay_land_use_efficiency_protra_341 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_CHP_solid_fossil"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_CHP_solid_fossil"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LROW", "PROTRA_CHP_solid_fossil"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_CHP_solid_fossil"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_CHP_solid_fossil"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_341",
)

_delayfixed_delay_land_use_efficiency_protra_342 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_CHP_solid_fossil_CCS"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_CHP_solid_fossil_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LROW", "PROTRA_CHP_solid_fossil_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_CHP_solid_fossil_CCS"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_CHP_solid_fossil_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_342",
)

_delayfixed_delay_land_use_efficiency_protra_343 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_CHP_waste"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_CHP_waste"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LROW", "PROTRA_CHP_waste"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_CHP_waste"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_CHP_waste"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_343",
)

_delayfixed_delay_land_use_efficiency_protra_344 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_CHP_solid_bio"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_CHP_solid_bio"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LROW", "PROTRA_CHP_solid_bio"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_CHP_solid_bio"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_CHP_solid_bio"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_344",
)

_delayfixed_delay_land_use_efficiency_protra_345 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_CHP_solid_bio_CCS"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_CHP_solid_bio_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LROW", "PROTRA_CHP_solid_bio_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_CHP_solid_bio_CCS"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_CHP_solid_bio_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_345",
)

_delayfixed_delay_land_use_efficiency_protra_346 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_HP_gas_fuels"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_HP_gas_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LROW", "PROTRA_HP_gas_fuels"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_HP_gas_fuels"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_HP_gas_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_346",
)

_delayfixed_delay_land_use_efficiency_protra_347 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_HP_solid_bio"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_HP_solid_bio"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LROW", "PROTRA_HP_solid_bio"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_HP_solid_bio"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_HP_solid_bio"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_347",
)

_delayfixed_delay_land_use_efficiency_protra_348 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_HP_geothermal"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_HP_geothermal"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LROW", "PROTRA_HP_geothermal"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_HP_geothermal"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_HP_geothermal"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_348",
)

_delayfixed_delay_land_use_efficiency_protra_349 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_HP_liquid_fuels"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_HP_liquid_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LROW", "PROTRA_HP_liquid_fuels"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_HP_liquid_fuels"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_HP_liquid_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_349",
)

_delayfixed_delay_land_use_efficiency_protra_350 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_HP_solar_DEACTIVATED"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_HP_solar_DEACTIVATED"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LROW", "PROTRA_HP_solar_DEACTIVATED"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_HP_solar_DEACTIVATED"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_HP_solar_DEACTIVATED"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_350",
)

_delayfixed_delay_land_use_efficiency_protra_351 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_HP_solid_fossil"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_HP_solid_fossil"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LROW", "PROTRA_HP_solid_fossil"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_HP_solid_fossil"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_HP_solid_fossil"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_351",
)

_delayfixed_delay_land_use_efficiency_protra_352 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_HP_waste"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_HP_waste"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LROW", "PROTRA_HP_waste"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_HP_waste"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_HP_waste"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_352",
)

_delayfixed_delay_land_use_efficiency_protra_353 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_PP_solid_bio"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_PP_solid_bio"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LROW", "PROTRA_PP_solid_bio"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_PP_solid_bio"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_PP_solid_bio"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_353",
)

_delayfixed_delay_land_use_efficiency_protra_354 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_PP_solid_bio_CCS"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_PP_solid_bio_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LROW", "PROTRA_PP_solid_bio_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_PP_solid_bio_CCS"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_PP_solid_bio_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_354",
)

_delayfixed_delay_land_use_efficiency_protra_355 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_PP_gas_fuels"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_PP_gas_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LROW", "PROTRA_PP_gas_fuels"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_PP_gas_fuels"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_PP_gas_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_355",
)

_delayfixed_delay_land_use_efficiency_protra_356 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_PP_gas_fuels_CCS"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_PP_gas_fuels_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LROW", "PROTRA_PP_gas_fuels_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_PP_gas_fuels_CCS"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_PP_gas_fuels_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_356",
)

_delayfixed_delay_land_use_efficiency_protra_357 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_PP_geothermal"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_PP_geothermal"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LROW", "PROTRA_PP_geothermal"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_PP_geothermal"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_PP_geothermal"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_357",
)

_delayfixed_delay_land_use_efficiency_protra_358 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_PP_hydropower_dammed"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_PP_hydropower_dammed"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LROW", "PROTRA_PP_hydropower_dammed"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_PP_hydropower_dammed"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_PP_hydropower_dammed"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_358",
)

_delayfixed_delay_land_use_efficiency_protra_359 = DelayFixed(
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc[
                "LROW", "PROTRA_PP_hydropower_run_of_river"
            ]
        ),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_PP_hydropower_run_of_river"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LROW", "PROTRA_PP_hydropower_run_of_river"]),
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc[
                "LROW", "PROTRA_PP_hydropower_run_of_river"
            ]
        ),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_PP_hydropower_run_of_river"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_359",
)

_delayfixed_delay_land_use_efficiency_protra_360 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_PP_liquid_fuels"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_PP_liquid_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LROW", "PROTRA_PP_liquid_fuels"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_PP_liquid_fuels"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_PP_liquid_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_360",
)

_delayfixed_delay_land_use_efficiency_protra_361 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_PP_liquid_fuels_CCS"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_PP_liquid_fuels_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LROW", "PROTRA_PP_liquid_fuels_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_PP_liquid_fuels_CCS"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_PP_liquid_fuels_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_361",
)

_delayfixed_delay_land_use_efficiency_protra_362 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_PP_nuclear"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_PP_nuclear"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LROW", "PROTRA_PP_nuclear"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_PP_nuclear"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_PP_nuclear"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_362",
)

_delayfixed_delay_land_use_efficiency_protra_363 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_PP_oceanic"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_PP_oceanic"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LROW", "PROTRA_PP_oceanic"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_PP_oceanic"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_PP_oceanic"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_363",
)

_delayfixed_delay_land_use_efficiency_protra_364 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_PP_solar_CSP"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_PP_solar_CSP"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LROW", "PROTRA_PP_solar_CSP"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_PP_solar_CSP"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_PP_solar_CSP"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_364",
)

_delayfixed_delay_land_use_efficiency_protra_365 = DelayFixed(
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["LROW", "PROTRA_PP_solar_open_space_PV"]
        ),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_PP_solar_open_space_PV"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LROW", "PROTRA_PP_solar_open_space_PV"]),
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["LROW", "PROTRA_PP_solar_open_space_PV"]
        ),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_PP_solar_open_space_PV"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_365",
)

_delayfixed_delay_land_use_efficiency_protra_366 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_PP_solar_urban_PV"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_PP_solar_urban_PV"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LROW", "PROTRA_PP_solar_urban_PV"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_PP_solar_urban_PV"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_PP_solar_urban_PV"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_366",
)

_delayfixed_delay_land_use_efficiency_protra_367 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_PP_solid_fossil"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_PP_solid_fossil"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LROW", "PROTRA_PP_solid_fossil"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_PP_solid_fossil"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_PP_solid_fossil"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_367",
)

_delayfixed_delay_land_use_efficiency_protra_368 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_PP_solid_fossil_CCS"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_PP_solid_fossil_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LROW", "PROTRA_PP_solid_fossil_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_PP_solid_fossil_CCS"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_PP_solid_fossil_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_368",
)

_delayfixed_delay_land_use_efficiency_protra_369 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_PP_waste"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_PP_waste"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LROW", "PROTRA_PP_waste"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_PP_waste"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_PP_waste"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_369",
)

_delayfixed_delay_land_use_efficiency_protra_370 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_PP_waste_CCS"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_PP_waste_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LROW", "PROTRA_PP_waste_CCS"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_PP_waste_CCS"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_PP_waste_CCS"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_370",
)

_delayfixed_delay_land_use_efficiency_protra_371 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_PP_wind_offshore"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_PP_wind_offshore"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LROW", "PROTRA_PP_wind_offshore"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_PP_wind_offshore"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_PP_wind_offshore"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_371",
)

_delayfixed_delay_land_use_efficiency_protra_372 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_PP_wind_onshore"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_PP_wind_onshore"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LROW", "PROTRA_PP_wind_onshore"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_PP_wind_onshore"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_PP_wind_onshore"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_372",
)

_delayfixed_delay_land_use_efficiency_protra_373 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_blending_gas_fuels"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_blending_gas_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LROW", "PROTRA_blending_gas_fuels"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_blending_gas_fuels"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_blending_gas_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_373",
)

_delayfixed_delay_land_use_efficiency_protra_374 = DelayFixed(
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_blending_liquid_fuels"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_blending_liquid_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LROW", "PROTRA_blending_liquid_fuels"]),
    lambda: xr.DataArray(
        float(land_use_efficiency_protra().loc["LROW", "PROTRA_blending_liquid_fuels"]),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_blending_liquid_fuels"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_374",
)

_delayfixed_delay_land_use_efficiency_protra_375 = DelayFixed(
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["LROW", "PROTRA_no_process_TI_hydrogen"]
        ),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_no_process_TI_hydrogen"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LROW", "PROTRA_no_process_TI_hydrogen"]),
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["LROW", "PROTRA_no_process_TI_hydrogen"]
        ),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_no_process_TI_hydrogen"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_375",
)

_delayfixed_delay_land_use_efficiency_protra_376 = DelayFixed(
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["LROW", "PROTRA_no_process_TI_solid_bio"]
        ),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_no_process_TI_solid_bio"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LROW", "PROTRA_no_process_TI_solid_bio"]),
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc["LROW", "PROTRA_no_process_TI_solid_bio"]
        ),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_no_process_TI_solid_bio"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_376",
)

_delayfixed_delay_land_use_efficiency_protra_377 = DelayFixed(
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc[
                "LROW", "PROTRA_no_process_TI_solid_fossil"
            ]
        ),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_no_process_TI_solid_fossil"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    lambda: float(protra_lifetime().loc["LROW", "PROTRA_no_process_TI_solid_fossil"]),
    lambda: xr.DataArray(
        float(
            land_use_efficiency_protra().loc[
                "LROW", "PROTRA_no_process_TI_solid_fossil"
            ]
        ),
        {"REGIONS_35_I": ["LROW"], "NRG_PRO_I": ["PROTRA_no_process_TI_solid_fossil"]},
        ["REGIONS_35_I", "NRG_PRO_I"],
    ),
    time_step,
    "_delayfixed_delay_land_use_efficiency_protra_377",
)


@component.add(
    name="INITIAL_TOTAL_LAND_PROTRA",
    units="km2",
    subscripts=["NRG_PROTRA_I", "REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"land_use_efficiency_protra": 1, "protra_capacity_stock": 1},
)
def initial_total_land_protra():
    """
    Total land occupied by energy PROTRA infrastructures in the initial year of the simulation. For simplicity, we assume that the installed capacities in 2005 had the same LUE than in 2005 (this is valid only in the case of constant LUEs, but in the case of improving LUEs due to e.g., efficiency improvements this would be an underestaimtion of total land). If we would have information about the evolution of LUE for the years before 2005, a matrix of data could be loaded instead.
    """
    return (
        land_use_efficiency_protra()
        * protra_capacity_stock().loc[:, "TO_elec", :].reset_coords(drop=True)
    ).transpose("NRG_PROTRA_I", "REGIONS_9_I")


@component.add(
    name="land_decommissioned_PROTRA",
    units="km2/Year",
    subscripts=["REGIONS_9_I", "NRG_TO_I", "NRG_PROTRA_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_capacity_decommissioning": 1,
        "delay_land_use_efficiency_protra": 1,
        "unit_conversion_mw_tw": 1,
    },
)
def land_decommissioned_protra():
    """
    Annual decommissioned land due to energy plants reaching the end of their lifetime.
    """
    return (
        zidz(
            protra_capacity_decommissioning(),
            delay_land_use_efficiency_protra().expand_dims(
                {"NRG_TO_I": _subscript_dict["NRG_TO_I"]}, 1
            ),
        )
        * unit_conversion_mw_tw()
    )


@component.add(
    name="land_use_by_PROTRA",
    units="km2",
    subscripts=["REGIONS_9_I", "NRG_TO_I", "NRG_PROTRA_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_land_use_by_protra": 1},
    other_deps={
        "_integ_land_use_by_protra": {
            "initial": {"initial_total_land_protra": 1},
            "step": {
                "new_land_requirements_protra": 1,
                "land_decommissioned_protra": 1,
            },
        }
    },
)
def land_use_by_protra():
    """
    Total land occupied by energy technologies in operation.
    """
    return _integ_land_use_by_protra()


_integ_land_use_by_protra = Integ(
    lambda: new_land_requirements_protra() - land_decommissioned_protra(),
    lambda: initial_total_land_protra()
    .transpose("REGIONS_9_I", "NRG_PROTRA_I")
    .expand_dims({"NRG_TO_I": _subscript_dict["NRG_TO_I"]}, 1),
    "_integ_land_use_by_protra",
)


@component.add(
    name="LAND_USE_EFFICIENCY_EXOGENOUS_PROTRA",
    units="MW/km2",
    subscripts=["NRG_PROTRA_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_land_use_efficiency_exogenous_protra": 2,
        "land_use_efficiency_exogenous_protra_low": 1,
        "land_use_efficiency_exogenous_protra_high": 1,
        "land_use_efficiency_exogenous_protra_medium": 1,
    },
)
def land_use_efficiency_exogenous_protra():
    """
    Selected values from literature for those PROTRA for which (direct occupation) land-use efficiency (LUE) is set exogenously. Same values for all regions for the sake of simplicity. This excludes solar technologies.
    """
    return if_then_else(
        select_land_use_efficiency_exogenous_protra() == 0,
        lambda: land_use_efficiency_exogenous_protra_low(),
        lambda: if_then_else(
            select_land_use_efficiency_exogenous_protra() == 1,
            lambda: land_use_efficiency_exogenous_protra_medium(),
            lambda: land_use_efficiency_exogenous_protra_high(),
        ),
    )


@component.add(
    name="LAND_USE_EFFICIENCY_EXOGENOUS_PROTRA_HIGH",
    units="MW/km2",
    subscripts=["NRG_PROTRA_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_land_use_efficiency_exogenous_protra_high"
    },
)
def land_use_efficiency_exogenous_protra_high():
    """
    High values from literature for those PROTRA for which (direct occupation) land-use efficiency (LUE) is set exogenously. Same values for all regions for the sake of simplicity. This excludes solar technologies.
    """
    return _ext_constant_land_use_efficiency_exogenous_protra_high()


_ext_constant_land_use_efficiency_exogenous_protra_high = ExtConstant(
    "model_parameters/energy/energy-land_use_efficiencies.xlsx",
    "land_use_efficiencies",
    "LAND_USE_EFFICIENCY_PROTRA_HIGH*",
    {"NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"]},
    _root,
    {"NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"]},
    "_ext_constant_land_use_efficiency_exogenous_protra_high",
)


@component.add(
    name="LAND_USE_EFFICIENCY_EXOGENOUS_PROTRA_LOW",
    units="MW/km2",
    subscripts=["NRG_PROTRA_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_land_use_efficiency_exogenous_protra_low"
    },
)
def land_use_efficiency_exogenous_protra_low():
    """
    Low values from literature for those PROTRA for which (direct occupation) land-use efficiency (LUE) is set exogenously. Same values for all regions for the sake of simplicity. This excludes solar technologies.
    """
    return _ext_constant_land_use_efficiency_exogenous_protra_low()


_ext_constant_land_use_efficiency_exogenous_protra_low = ExtConstant(
    "model_parameters/energy/energy-land_use_efficiencies.xlsx",
    "land_use_efficiencies",
    "LAND_USE_EFFICIENCY_PROTRA_LOW*",
    {"NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"]},
    _root,
    {"NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"]},
    "_ext_constant_land_use_efficiency_exogenous_protra_low",
)


@component.add(
    name="LAND_USE_EFFICIENCY_EXOGENOUS_PROTRA_MEDIUM",
    units="MW/km2",
    subscripts=["NRG_PROTRA_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_land_use_efficiency_exogenous_protra_medium"
    },
)
def land_use_efficiency_exogenous_protra_medium():
    """
    Medium values from literature for those PROTRA for which (direct occupation) land-use efficiency (LUE) is set exogenously. Same values for all regions for the sake of simplicity. This excludes solar technologies.
    """
    return _ext_constant_land_use_efficiency_exogenous_protra_medium()


_ext_constant_land_use_efficiency_exogenous_protra_medium = ExtConstant(
    "model_parameters/energy/energy-land_use_efficiencies.xlsx",
    "land_use_efficiencies",
    "LAND_USE_EFFICIENCY_PROTRA_MEDIUM*",
    {"NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"]},
    _root,
    {"NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"]},
    "_ext_constant_land_use_efficiency_exogenous_protra_medium",
)


@component.add(
    name="land_use_efficiency_PROTRA",
    units="MW/km2",
    subscripts=["REGIONS_9_I", "NRG_PROTRA_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"land_use_efficiency_exogenous_protra": 1, "lue_solar_pv": 1},
)
def land_use_efficiency_protra():
    """
    Land-use efficiency of PROTRA energy technologies combining exogenous with endogenous calculations.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS_9_I": _subscript_dict["REGIONS_9_I"],
            "NRG_PROTRA_I": _subscript_dict["NRG_PROTRA_I"],
        },
        ["REGIONS_9_I", "NRG_PROTRA_I"],
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, ["PROTRA_PP_solar_open_space_PV"]] = False
    value.values[except_subs.values] = (
        land_use_efficiency_exogenous_protra()
        .expand_dims({"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, 0)
        .values[except_subs.values]
    )
    value.loc[:, ["PROTRA_PP_solar_open_space_PV"]] = (
        lue_solar_pv()
        .expand_dims({"NRG_PRO_I": ["PROTRA_PP_solar_open_space_PV"]}, 1)
        .values
    )
    return value


@component.add(
    name="LAND_USE_EFFICIENCY_WIND_FARM_AREA",
    units="MW/km2",
    subscripts=["PROTRA_WIND_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_land_use_efficiency_exogenous_protra": 2,
        "land_use_efficiency_wind_farm_area_low": 1,
        "land_use_efficiency_wind_farm_area_medium": 1,
        "land_use_efficiency_wind_farm_area_high": 1,
    },
)
def land_use_efficiency_wind_farm_area():
    """
    Selected values from literature for wind farm land-use efficiency. These values refer to the total area encompassing the turbines, i.e., it is much higher than the turbine direct land use.
    """
    return if_then_else(
        select_land_use_efficiency_exogenous_protra() == 0,
        lambda: land_use_efficiency_wind_farm_area_low(),
        lambda: if_then_else(
            select_land_use_efficiency_exogenous_protra() == 1,
            lambda: land_use_efficiency_wind_farm_area_medium(),
            lambda: land_use_efficiency_wind_farm_area_high(),
        ),
    )


@component.add(
    name="LAND_USE_EFFICIENCY_WIND_FARM_AREA_HIGH",
    units="MW/km2",
    subscripts=["PROTRA_WIND_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_land_use_efficiency_wind_farm_area_high"
    },
)
def land_use_efficiency_wind_farm_area_high():
    """
    High values from literature for wind farm land-use efficiency. These values refer to the total area encompassing the turbines, i.e., it is much higher than the turbine direct land use.
    """
    return _ext_constant_land_use_efficiency_wind_farm_area_high()


_ext_constant_land_use_efficiency_wind_farm_area_high = ExtConstant(
    "model_parameters/energy/energy-land_use_efficiencies.xlsx",
    "land_use_efficiencies",
    "LAND_USE_EFFICIENCY_WIND_FARM_AREA_HIGH*",
    {"PROTRA_WIND_I": _subscript_dict["PROTRA_WIND_I"]},
    _root,
    {"PROTRA_WIND_I": _subscript_dict["PROTRA_WIND_I"]},
    "_ext_constant_land_use_efficiency_wind_farm_area_high",
)


@component.add(
    name="LAND_USE_EFFICIENCY_WIND_FARM_AREA_LOW",
    units="MW/km2",
    subscripts=["PROTRA_WIND_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_land_use_efficiency_wind_farm_area_low"},
)
def land_use_efficiency_wind_farm_area_low():
    """
    Low values from literature for wind farm land-use efficiency. These values refer to the total area encompassing the turbines, i.e., it is much higher than the turbine direct land use.
    """
    return _ext_constant_land_use_efficiency_wind_farm_area_low()


_ext_constant_land_use_efficiency_wind_farm_area_low = ExtConstant(
    "model_parameters/energy/energy-land_use_efficiencies.xlsx",
    "land_use_efficiencies",
    "LAND_USE_EFFICIENCY_WIND_FARM_AREA_LOW*",
    {"PROTRA_WIND_I": _subscript_dict["PROTRA_WIND_I"]},
    _root,
    {"PROTRA_WIND_I": _subscript_dict["PROTRA_WIND_I"]},
    "_ext_constant_land_use_efficiency_wind_farm_area_low",
)


@component.add(
    name="LAND_USE_EFFICIENCY_WIND_FARM_AREA_MEDIUM",
    units="MW/km2",
    subscripts=["PROTRA_WIND_I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_land_use_efficiency_wind_farm_area_medium"
    },
)
def land_use_efficiency_wind_farm_area_medium():
    """
    Medium values from literature for wind farm land-use efficiency. These values refer to the total area encompassing the turbines, i.e., it is much higher than the turbine direct land use.
    """
    return _ext_constant_land_use_efficiency_wind_farm_area_medium()


_ext_constant_land_use_efficiency_wind_farm_area_medium = ExtConstant(
    "model_parameters/energy/energy-land_use_efficiencies.xlsx",
    "land_use_efficiencies",
    "LAND_USE_EFFICIENCY_WIND_FARM_AREA_MEDIUM*",
    {"PROTRA_WIND_I": _subscript_dict["PROTRA_WIND_I"]},
    _root,
    {"PROTRA_WIND_I": _subscript_dict["PROTRA_WIND_I"]},
    "_ext_constant_land_use_efficiency_wind_farm_area_medium",
)


@component.add(
    name="LUE_solar_PV",
    units="MW/km2",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "lue_solar_pv_by_technology": 1,
        "share_capacity_stock_protra_pp_solar_pv_by_subtechnology": 1,
    },
)
def lue_solar_pv():
    """
    Land-use efficiency of solar PV for all subtechnologies (weighted-average).
    """
    return sum(
        lue_solar_pv_by_technology()
        .loc[_subscript_dict["REGIONS_9_I"], :]
        .rename(
            {
                "REGIONS_36_I": "REGIONS_9_I",
                "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!",
            }
        )
        * share_capacity_stock_protra_pp_solar_pv_by_subtechnology()
        .loc[:, "PROTRA_PP_solar_open_space_PV", :]
        .reset_coords(drop=True)
        .rename(
            {
                "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I": "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!"
            }
        ),
        dim=["PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I!"],
    )


@component.add(
    name="LUE_solar_PV_by_technology",
    units="MW/km2",
    subscripts=["REGIONS_36_I", "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "power_pv_per_panel_area": 1,
        "average_regoinal_latitude_solar_pv_eroimin": 1,
        "pv_land_occupation_ratio": 1,
    },
)
def lue_solar_pv_by_technology():
    """
    Dynamic land-use efficiency of solar PV open-space.
    """
    return (
        power_pv_per_panel_area()
        * np.cos(average_regoinal_latitude_solar_pv_eroimin())
        * pv_land_occupation_ratio()
    ).transpose("REGIONS_36_I", "PROTRA_PP_SOLAR_PV_SUBTECHNOLOGIES_I")


@component.add(
    name="net_new_land_requirements_PROTRA_on_built_up_land",
    units="km2/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"new_land_requirements_protra": 1, "land_decommissioned_protra": 1},
)
def net_new_land_requirements_protra_on_built_up_land():
    """
    Net annual new land requirements for PROTRA in urban land. This excludes solar on land (PV + CSP), solar PV rooftop and ocean technologies (wind offshore and oceanic). This approach gives priority to repowering over occupying new sites. This calculation is only correct if the land-use efficiencies are constant over time.
    """
    return sum(
        new_land_requirements_protra()
        .loc[:, :, _subscript_dict["PROTRA_BUILT_UP_LAND_I"]]
        .rename({"NRG_TO_I": "NRG_TO_I!", "NRG_PROTRA_I": "PROTRA_BUILT_UP_LAND_I!"}),
        dim=["NRG_TO_I!", "PROTRA_BUILT_UP_LAND_I!"],
    ) - sum(
        land_decommissioned_protra()
        .loc[:, :, _subscript_dict["PROTRA_BUILT_UP_LAND_I"]]
        .rename({"NRG_TO_I": "NRG_TO_I!", "NRG_PROTRA_I": "PROTRA_BUILT_UP_LAND_I!"}),
        dim=["NRG_TO_I!", "PROTRA_BUILT_UP_LAND_I!"],
    )


@component.add(
    name="net_new_land_requirements_solar_on_land",
    units="km2/Year",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"new_land_requirements_protra": 2, "land_decommissioned_protra": 2},
)
def net_new_land_requirements_solar_on_land():
    """
    Net annual new land requirements for solar on land (PV + CSP). This approach gives priority to repowering over occupying new sites. This calculation is only correct if the land-use efficiencies are constant over time.
    """
    return (
        new_land_requirements_protra()
        .loc[:, "TO_elec", "PROTRA_PP_solar_open_space_PV"]
        .reset_coords(drop=True)
        + new_land_requirements_protra()
        .loc[:, "TO_elec", "PROTRA_PP_solar_CSP"]
        .reset_coords(drop=True)
        - (
            land_decommissioned_protra()
            .loc[:, "TO_elec", "PROTRA_PP_solar_open_space_PV"]
            .reset_coords(drop=True)
            + land_decommissioned_protra()
            .loc[:, "TO_elec", "PROTRA_PP_solar_CSP"]
            .reset_coords(drop=True)
        )
    )


@component.add(
    name="new_land_requirements_PROTRA",
    units="km2/Year",
    subscripts=["REGIONS_9_I", "NRG_TO_I", "NRG_PROTRA_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_capacity_expansion": 1,
        "land_use_efficiency_protra": 1,
        "unit_conversion_mw_tw": 1,
    },
)
def new_land_requirements_protra():
    """
    New land requeriments of PROTRA installations.
    """
    return (
        zidz(
            protra_capacity_expansion(),
            land_use_efficiency_protra().expand_dims(
                {"NRG_TO_I": _subscript_dict["NRG_TO_I"]}, 1
            ),
        )
        * unit_conversion_mw_tw()
    )


@component.add(
    name="PV_GENERATOR_TO_SYSTEM_AREA_RATIO",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_pv_generator_to_system_area_ratio"},
)
def pv_generator_to_system_area_ratio():
    """
    Generator-to-system area represents the share of the full area enclosed by the site boundary of the power plant which is covered by the PV panels and heliostats including the separation between them. We assume the same value for all regions.
    """
    return _ext_constant_pv_generator_to_system_area_ratio()


_ext_constant_pv_generator_to_system_area_ratio = ExtConstant(
    "model_parameters/energy/energy-land_use_efficiencies.xlsx",
    "land_use_efficiencies",
    "PV_GENERATOR_TO_SYSTEM_AREA_RATIO",
    {},
    _root,
    {},
    "_ext_constant_pv_generator_to_system_area_ratio",
)


@component.add(
    name="PV_LAND_OCCUPATION_RATIO",
    units="DMNL",
    subscripts=["REGIONS_36_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"pv_generator_to_system_area_ratio": 1, "pv_packing_factor": 1},
)
def pv_land_occupation_ratio():
    """
    Share of land covered by PV panels.
    """
    return pv_generator_to_system_area_ratio() * pv_packing_factor()


@component.add(
    name="PV_PACKING_FACTOR",
    units="DMNL",
    subscripts=["REGIONS_36_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"average_regoinal_latitude_solar_pv_eroimin": 3},
)
def pv_packing_factor():
    """
    Packing factor. Ratio between the PV panels or heliostats and the ground area required for arrays’ installation including separation to avoid excessive self-shading.
    """
    return 1 / (
        np.cos(average_regoinal_latitude_solar_pv_eroimin())
        + np.sin(average_regoinal_latitude_solar_pv_eroimin())
        / np.tan(1.16152 - average_regoinal_latitude_solar_pv_eroimin())
    )


@component.add(
    name="SELECT_LAND_USE_EFFICIENCY_EXOGENOUS_PROTRA",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_select_land_use_efficiency_exogenous_protra"
    },
)
def select_land_use_efficiency_exogenous_protra():
    """
    This 'select' has the following options: 0: low values from literature for land-use efficiency (direct) and for wind farm area 1: medium values from literature for land-use efficiency (direct) and for wind farm area 2: high values from literature for land-use efficiency (direct) and for wind farm area
    """
    return _ext_constant_select_land_use_efficiency_exogenous_protra()


_ext_constant_select_land_use_efficiency_exogenous_protra = ExtConstant(
    "model_parameters/energy/energy-land_use_efficiencies.xlsx",
    "land_use_efficiencies",
    "SELECT_LUE_PROTRA",
    {},
    _root,
    {},
    "_ext_constant_select_land_use_efficiency_exogenous_protra",
)


@component.add(
    name="total_land_use_PROTRA",
    units="km2",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"land_use_by_protra": 1, "total_sea_area_use_protra": 1},
)
def total_land_use_protra():
    """
    Total direct land-use for PROTRA.
    """
    return (
        sum(
            land_use_by_protra().rename(
                {"NRG_TO_I": "NRG_TO_I!", "NRG_PROTRA_I": "NRG_PROTRA_I!"}
            ),
            dim=["NRG_TO_I!", "NRG_PROTRA_I!"],
        )
        - total_sea_area_use_protra()
    )


@component.add(
    name="total_sea_area_use_PROTRA",
    units="km2",
    subscripts=["REGIONS_9_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"land_use_by_protra": 2},
)
def total_sea_area_use_protra():
    """
    Total direct sea area use for PROTRA including wind offshore and oceanic technologies.
    """
    return land_use_by_protra().loc[
        :, "TO_elec", "PROTRA_PP_wind_offshore"
    ].reset_coords(drop=True) + land_use_by_protra().loc[
        :, "TO_elec", "PROTRA_PP_oceanic"
    ].reset_coords(
        drop=True
    )


@component.add(
    name="wind_farm_area",
    units="km2",
    subscripts=["REGIONS_9_I", "PROTRA_WIND_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_capacity_stock": 1,
        "land_use_efficiency_wind_farm_area": 1,
        "unit_conversion_mw_tw": 1,
    },
)
def wind_farm_area():
    """
    Wind farm occupation, which refer to the total area encompassing the turbines, i.e., it is much higher than the turbine direct land use.
    """
    return (
        zidz(
            protra_capacity_stock()
            .loc[:, "TO_elec", _subscript_dict["PROTRA_WIND_I"]]
            .reset_coords(drop=True)
            .rename({"NRG_PROTRA_I": "PROTRA_WIND_I"}),
            land_use_efficiency_wind_farm_area().expand_dims(
                {"REGIONS_9_I": _subscript_dict["REGIONS_9_I"]}, 0
            ),
        )
        * unit_conversion_mw_tw()
    )
