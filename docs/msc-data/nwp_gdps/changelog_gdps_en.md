[En français](changelog_gdps_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [GDPS](readme_gdps_en.md) > GDPS Changelog

# Chronology of changes to the Global Deterministic Prediction System (GDPS)

## Wednesday July 3, 2019

### Upgrade to Version 7.0.0 of the Global Deterministic Prediction System (GDPS) at the Canadian Meteorological Centre

On Wednesday July 3rd 2019, starting with the 1200 UTC run, the Canadian Meteorological Centre (CMC) of the Meteorological Service of Canada will upgrade the Global Deterministic Prediction System (GDPS) to version 7.0.0.
The changes included in this upgrade are summarized as follows:

* Changes to the atmospheric component of the forecast model:
    * Upgrade from GEM v4.8-LTS.16 to GEM v5.0.0. For more informations on GEM-5, please consult [this document](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/GEM5_paper_submitted_JAMES_20190614.pdf).
    * Increase in horizontal resolution from 25 to 15 km.
    * Increase in the number of vertical levels from 80 to 84.
    * Improvements to the land surface scheme ISBA.
* Changes to the oceanic component of the forecast model:
    * Update to the NEMO ocean model from v3.1 to v3.6.
* Changes to the atmospheric component of the data assimilation:
    * Uniform cut-off for all daily runs at 7h.
* Changes to the oceanic component of the data assimilation:
    * Upgrade to GIOPS v3.0.0 from v2.3.0.
    * Update to SAM2 (Système d'Assimilation Mercator).
    * New sea-surface temperature and sea-ice analyses at 0.1 deg resolution (from 0.2 deg resolution).


A copy of the official note announcing the implementation of these changes is available at [this link](http://dd.weather.gc.ca/doc/genots/2019/06/28/NOCN03_CWAO_281719___09158).

A technical note with more details on this change [is available at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_gdps-700_e.pdf).

The technical specifications document of the GDPS 7.0.0 [is available at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_GDPS_7.0.0_e.pdf).


## Tuesday September 18, 2018

### Upgrade to Version 6.1.0 of the Global Deterministic Prediction System (GDPS) at the Canadian Meteorological Centre

On Tuesday September 18th 2018, starting with the 1200 UTC run, the Canadian Meteorological Centre (CMC) of the Meteorological Service of Canada will upgrade the Global Deterministic Prediction System (GDPS) to version 6.1.0.
The changes included in this upgrade are summarized as follows:

* Changes to the forecast model:
    * No modifications were made to the forecast model component in this upgrade of the GDPS.
* Changes to the data assimilation component:
    * Improved observation processing (RAOBS, AMV, GB-GPS, aircraft).
    * Additional observations (increase of ~1.7%; primarily CSR water vapour channels)
    * The RTTOV operator is upgraded from version 10 to 12.1
    * Increased horizontal resolution of analysis increment in 4D-EnVar (from 50 to 37 km)


A copy of the official note announcing the implementation of these changes [is available at this link](http://dd.weather.gc.ca/doc/genots/2018/09/14/NOCN03_CWAO_142110___13748).

A technical note with more details on this change [is available at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_gdps-610_20180918_e.pdf).

The technical specifications document of the GDPS 6.1.0 [is available at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_GDPS_6.1.0_e.pdf).


## Wednesday November 1, 2017

### Major Upgrade to Version 6.0.0 of the Global Deterministic Prediction System (GDPS) at the Canadian Meteorological Centre

On Wednesday November 1st 2017, starting with the 1200 UTC run, the Meteorological Service of Canada's Canadian Meteorological Centre (CMC) will upgrade the Global Deterministic Prediction System (GDPS) to version 6.0.0.
The changes included in this upgrade are summarized as follows:

* Changes to the forecast model:
    * Introduction of two-way coupling with an ice-ocean model. In the GDPS-6.0.0 forecast system, surface conditions evolve through coupling with the forecast component of the Global Ice Ocean Prediction System (GIOPS). [Click here for GIOPS details](../nwp_giops/changelog_giops_en.md). 
    * GDPS 6.0.0 is using GEM model version 4.8.2 (the main changes are associated with the surface interface, with only minor changes made to model physics and dynamics).
* No modifications were made to the assimilation component nor observations ingested in this upgrade of the GDPS.


A copy of the official note announcing the implementation of these changes [is available at this link](http://dd.weather.gc.ca/doc/genots/2017/10/30/NOCN03_CWAO_301922___01740).

A technical note with more details on this change [is available at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_gdps-600_20171101_e.pdf).

The technical specifications document of the GDPS 6.0.0 [is available at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_GDPS_6.0.0_e.pdf).


## Tuesday December 15, 2015

### Major Upgrade to Version 5.0.0 of the Global Deterministic Prediction System (GDPS) at the Canadian Meteorological Centre

On Tuesday December 15th 2015, starting with the 1200 UTC run, the Meteorological Service of Canada's Canadian Meteorological Centre (CMC) will upgrade the Global Deterministic Prediction System (GDPS) to version 5.0.0.
The changes included in this upgrade are summarized as follows:

* Changes to the forecast model:
    * Overlapping LAM domains (in Yin-Yang grid formation) replace a global uniform lat-lon grid (horizontal resolution remains at 25 km).
    * Introduction of the trapezoidal method for trajectory calculation, combined with a cubic interpolation scheme.
    * Addition of an extra momentum level to the vertical coordinate above 10 hPa to improve computing efficiency.
    * Modification to the rate of flattening of the terrain-following levels.
    * Addition of two diagnostic levels at 1.5 m and 10 m above model ground level.
* Changes to the assimilation system:
    * Introduction of the same staggered vertical coordinate used by the forecast model.
* Changes to observations:
    * Addition of radiance observations from 17 channels of the Advanced Microwave Sounding Unit (ATMS).
    * 103 additional Cross-track Infrared Sounder (CrIS) channels.
    * More than 600 additional ground-based GPS sites (mostly in Europe).
    * Introduction of inter-channel correlations for all infrared and microwave radiances.


A copy of the official note announcing the implementation of these changes [is available at this link](http://dd.meteo.gc.ca/doc/genots/2015/12/14/NOCN03_CWAO_142125___00050).

A technical note with more details on this change [is available at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_gdps-500_20151215_e.pdf).

The technical specifications document of the GDPS 5.0.0 [is available at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_GDPS_5.0.0_e.pdf).


## Tuesday November 18th 2014

### Major Upgrade to the Global Deterministic Prediction System (GDPS) version 4.0.0 at the Canadian Meteorological Centre

On Tuesday November 18th 2014, starting with the 1200 UTC run the Meteorological Service of Canada's Canadian Meteorological Centre (CMC) will upgrade the Global Deterministic Prediction System (GDPS) to version 4.0.0.
Summary of the major changes included in this upgrade:

* New 4D-EnVAR assimilation technique replaces 4D-VAR.
    * Coupling with the ensemble Kalman filter (EnKF) to obtain background-error covariances.
* Changes to observations
    * Improved treatment of radiosonde and aircraft observations.
    * Assimilation of ground-based GPS data.
    * Improved satellite radiance bias correction procedure.
    * Additional AIRS/IASI channels assimilated.
* Changes to the forecast model
    * 4D Incremental Analysis Update (4D-IAU) approach.
    * Recycling of several key prognostic variables.
* New sea-ice concentration analysis.


A copy of the official note announcing the implementation of these changes [is available at this link](http://dd.meteo.gc.ca/doc/genots/2014/11/14/NOCN03_CWAO_141410___00630).

A technical note with more details on this change [is available at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/lib/technote_gdps-400_20141118_e.pdf).


## Wednesday February 13, 2013

### Major Upgrade to the Global Deterministic Prediction System (GDPS) version 3.0.0 at the Canadian Meteorological Centre

On Wednesday February 13 2013, starting with the 1200 UTC run, the Canadian Meteorological Centre (CMC) will implement version 3.0.0 of the Global Deterministic Prediction System (GDPS).

This major upgrade includes a new version to the GEM model, important changes to the 4D-Var data assimilation scheme and to some of the model's physics schemes.

In this version, the grid of the model is also increased to a resolution of 25km. Also, this version now uses staggered hybrid vertical coordinates. For information on staggered hybrid vertical coordinates [users can consult this short note](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/lib/op_systems/doc_opchanges/HybridVerticalCoordinateDefinitions_20130213.pdf) on the topic along with [this diagram here](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/lib/op_systems/doc_opchanges/VerticalCoordinatesDiagram_afsysed_20130213.jpg).

Objective Scores show improvements in the forecasts with most metrics throughout most of the atmosphere, in particular over North America in winter. A subjective evaluation by operational meteorologists confirmed those improvements.

As part of this implementation the cutoff time for collecting observations has been reduced and is now [00,12]Z+3:05

Changes were also brought to the Regional Determnistic Prediction System (RDPS) to harmonize it with GDPS-3.0.0, and the RDPS forecasts are also improved. As a result of these RDPS adjustments, the version of RDPS is now 3.1.0

A copy of the official note describing these changes and the verification work leading up to this implementation [is available here](http://dd.weatheroffice.ec.gc.ca/doc/genots/2013/02/07/NOCN03_CWAO_071810___00179).

A technical note with more details on this change [is available at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/lib/op_systems/doc_opchanges/technote_gdps300_20130213_e.pdf).

