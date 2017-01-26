# RDPS

Id                | Nom                                                                 | Services web | Styles                                                                                     | Notes
------------------|---------------------------------------------------------------------|--------------|--------------------------------------------------------------------------------------------|------
RDPS.ETA_NT       | RDPS.ETA - Couverture nuageuse totale (fraction)                    | WMS, WCS     | DEFAULT: CLOUD                                                                             |      
RDPS.ETA_ES       | RDPS.ETA - Écart du point de rosée                                  | WMS, WCS     | DEFAULT: DEWPOINTDEP                                                                       |      
RDPS.ETA_TD       | RDPS.ETA - Température du point de rosée                            | WMS, WCS     | DEFAULT: DEWPOINT                                                                          |      
RDPS.ETA_RT       | RDPS.ETA - Taux de précipitation instantané (m/s)                   | WMS, WCS     | DEFAULT: PRECIPPRTMMH                                                                      |      
RDPS.ETA_TT       | RDPS.ETA - Température de l'air                                     | WMS, WCS     | DEFAULT: TEMPWINTER-LINEAR, TEMPERATURE, TEMPSUMMER, TEMPWINTER, TEMPERATURE-LINEAR        |      
RDPS.ETA_GZ       | RDPS.ETA - Hauteur géopotentielle                                   | WMS, WCS     | DEFAULT: GPHEIGHT                                                                          |      
RDPS.ETA_HU       | RDPS.ETA - Humidité spécifique                                      | WMS, WCS     | DEFAULT: HUMIDITYSPEC                                                                      |      
RDPS.ETA_FR       | RDPS.ETA -  Pluie verglaçante accumulée                             | WMS, WCS     | DEFAULT: CAPA24-LINEAR, PRECIPMM, PRECIPMM-LINEAR                                          |      
RDPS.ETA_P0       | RDPS.ETA - Pression à la surface                                    | WMS, WCS     | DEFAULT: PRESSURE                                                                          |      
RDPS.ETA_PR       | RDPS.ETA - Précipitations accumulées                                | WMS, WCS     | DEFAULT: CAPA24-LINEAR, PRECIPMM, PRECIPMM-LINEAR                                          |      
RDPS.ETA_RN       | RDPS.ETA - Pluie accumulée                                          | WMS, WCS     | DEFAULT: CAPA24-LINEAR, PRECIPMM, PRECIPMM-LINEAR                                          |      
RDPS.ETA_SN       | RDPS.ETA - Neige accumulée                                          | WMS, WCS     | DEFAULT: PRECIPSNOW-LINEAR                                                                 |      
RDPS.ETA_I0       | RDPS.ETA - Température de la surface et du sol (Profondeur/moyenne) | WMS, WCS     | DEFAULT: TEMPSOIL-NONLINEAR                                                                |      
RDPS.ETA_PN       | RDPS.ETA - Pression au niveau de la mer (contour)                   | WFS, WMS     | DEFAULT: PRESSURE4_LINE                                                                    |      
RDPS.ETA_PN-SLP   | RDPS.ETA - Pression au niveau de la mer                             | WMS, WCS     | DEFAULT: PRESSURE4-LINEAR, PRESSURE4, PRESSURESEAHIGH                                      |      
RDPS.ETA_UU       | RDPS.ETA - Vents                                                    | WFS, WMS     | DEFAULT: WINDARROW                                                                         |      
RDPS.PRES_UU.1000 | RDPS.PRES - Vents à 1000.0 mb                                       | WFS, WMS     | DEFAULT: WINDARROW                                                                         |      
RDPS.PRES_UU.925  | RDPS.PRES - Vents à 925.0 mb                                        | WFS, WMS     | DEFAULT: WINDARROW                                                                         |      
RDPS.PRES_UU.850  | RDPS.PRES - Vents à 850.0 mb                                        | WFS, WMS     | DEFAULT: WINDARROW                                                                         |      
RDPS.PRES_UU.700  | RDPS.PRES - Vents à 700.0 mb                                        | WFS, WMS     | DEFAULT: WINDARROW                                                                         |      
RDPS.PRES_UU.500  | RDPS.PRES - Vents à 500.0 mb                                        | WFS, WMS     | DEFAULT: WINDARROW                                                                         |      
RDPS.PRES_TT.1000 | RDPS.PRES - Température de l'air à 1000.0 mb                        | WMS, WCS     | DEFAULT: TEMPWINTER-LINEAR, TEMPERATURE, TEMPERATURE-LINEAR, TEMPSUMMER, TEMPSUMMER-LINEAR |      
RDPS.PRES_TT.925  | RDPS.PRES - Température de l'air à 925.0 mb                         | WMS, WCS     | DEFAULT: TEMPWINTER-LINEAR, TEMPERATURE, TEMPERATURE-LINEAR, TEMPSUMMER, TEMPSUMMER-LINEAR |      
RDPS.PRES_TT.850  | RDPS.PRES - Température de l'air à 850.0 mb                         | WMS, WCS     | DEFAULT: TEMPWINTER-LINEAR, TEMPERATURE, TEMPERATURE-LINEAR, TEMPSUMMER, TEMPSUMMER-LINEAR |      
RDPS.PRES_TT.700  | RDPS.PRES - Température de l'air à 700.0 mb                         | WMS, WCS     | DEFAULT: TEMPWINTER-LINEAR, TEMPERATURE, TEMPERATURE-LINEAR, TEMPSUMMER, TEMPSUMMER-LINEAR |      
RDPS.PRES_TT.500  | RDPS.PRES - Température de l'air à 500.0 mb                         | WMS, WCS     | DEFAULT: TEMPWINTER-LINEAR, TEMPERATURE, TEMPERATURE-LINEAR, TEMPSUMMER, TEMPSUMMER-LINEAR |      
RDPS.PRES_GZ.1000 | RDPS.PRES - Hauteur géopotentielle à 1000.0 mb                      | WMS, WCS     | DEFAULT: GEOPOTENTIELHEIGHT-1000mb-NONLINEAR                                               |      
RDPS.PRES_GZ.925  | RDPS.PRES - Hauteur géopotentielle à 925.0 mb                       | WMS, WCS     | DEFAULT: GEOPOTENTIELHEIGHT-925mb-NONLINEAR                                                |      
RDPS.PRES_GZ.850  | RDPS.PRES - Hauteur géopotentielle à 850.0 mb                       | WMS, WCS     | DEFAULT: GEOPOTENTIELHEIGHT-850mb-NONLINEAR                                                |      
RDPS.PRES_GZ.700  | RDPS.PRES - Hauteur géopotentielle à 700.0 mb                       | WMS, WCS     | DEFAULT: GEOPOTENTIELHEIGHT-700mb-NONLINEAR                                                |      
RDPS.PRES_GZ.500  | RDPS.PRES - Hauteur géopotentielle à 500.0 mb                       | WMS, WCS     | DEFAULT: GEOPOTENTIELHEIGHT-500mb-NONLINEAR                                                |      
RDPS.PRES_ES.1000 | RDPS.PRES - Écart du point de rosée à 1000.0 mb                     | WMS, WCS     | DEFAULT: DEWPOINTDEP                                                                       |      
RDPS.PRES_ES.925  | RDPS.PRES - Écart du point de rosée à 925.0 mb                      | WMS, WCS     | DEFAULT: DEWPOINTDEP                                                                       |      
RDPS.PRES_ES.850  | RDPS.PRES - Écart du point de rosée à 850.0 mb                      | WMS, WCS     | DEFAULT: DEWPOINTDEP                                                                       |      
RDPS.PRES_ES.700  | RDPS.PRES - Écart du point de rosée à 700.0 mb                      | WMS, WCS     | DEFAULT: DEWPOINTDEP                                                                       |      
RDPS.PRES_ES.500  | RDPS.PRES - Écart du point de rosée à 500.0 mb                      | WMS, WCS     | DEFAULT: DEWPOINTDEP                                                                       |      
RDPS.PRES_HU.1000 | RDPS.PRES - Humidité spécifique à 1000.0 mb                         | WMS, WCS     | DEFAULT: HUMIDITYSPEC                                                                      |      
RDPS.PRES_HU.925  | RDPS.PRES - Humidité spécifique à 925.0 mb                          | WMS, WCS     | DEFAULT: HUMIDITYSPEC                                                                      |      
RDPS.PRES_HU.850  | RDPS.PRES - Humidité spécifique à 850.0 mb                          | WMS, WCS     | DEFAULT: HUMIDITYSPEC                                                                      |      
RDPS.PRES_HU.700  | RDPS.PRES - Humidité spécifique à 700.0 mb                          | WMS, WCS     | DEFAULT: HUMIDITYSPEC                                                                      |      
RDPS.PRES_HU.500  | RDPS.PRES - Humidité spécifique à 500.0 mb                          | WMS, WCS     | DEFAULT: HUMIDITYSPEC                                                                      |      

