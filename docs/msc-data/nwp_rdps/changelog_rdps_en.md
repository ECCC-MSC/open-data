[En français](changelog_rdps_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [RDPS](readme_rdps_en.md) > RDPS Changelog

# Chronology of changes to the Regional Deterministic Prediction System (RDPS)

## Wednesday July 3, 2019

### Major upgrade to Version 7.0.0 of the Regional Deterministic Prediction System (RDPS) at the Canadian Meteorological Centre

On Wednesday, July 3, 2019, starting with the 1200 UTC run, the Canadian Meteorological Centre (CMC) of the Meteorological Service of Canada will upgrade the Regional Deterministic Prediction System (RDPS) to version 7.0.0.
The changes included in this upgrade are summarized as follows:

* Changes to the forecast model:
    * [GDPS v7.0.0]((../nwp_gdps/changelog_gdps_en.md)) replaces v6.1.0 as the pilot system.
    * Upgrade from GEM v4.8-LTS.16 to GEM v5.0.0. For more informations on GEM-5, please consult this document.
    * Increase in the number of vertical levels from 80 to 84.
    * Improvements to the land surface scheme ISBA.
* Changes to the assimilation system:
    * Uniform cut-off for all daily runs at 7h.
    * New sea-surface temperature and sea-ice analyses at 0.1 deg resolution (from 0.2 deg resolution).

A copy of the official note announcing the implementation of these changes [is available at this link](http://dd.meteo.gc.ca/doc/genots/2019/06/28/NOCN03_CWAO_281748___44556).

A technical note with more details on this change [is available at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_rdps-700_20190703_e.pdfhttps://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_rdps-700_20190703_e.pdf).

The technical specifications document for RDPS 7.0.0 [is available at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_RDPS_7.0.0_e.pdf).


## Tuesday September 18, 2018

### Major upgrade to Version 6.0.0 of the Regional Deterministic Prediction System (RDPS) at the Canadian Meteorological Centre

On Tuesday, September 18, 2018, starting with the 1200 UTC run, the Canadian Meteorological Centre (CMC) of the Meteorological Service of Canada will upgrade the Regional Deterministic Prediction System (RDPS) to version 6.0.0.
The changes included in this upgrade are summarized as follows:

* Changes to the forecast model:
    * No modifications were made to the forecast model component in this upgrade of the RDPS.
* Changes to the assimilation system:
    * Replacement of the intermittent analysis cycling strategy by a continuous cycle (like the GDPS).
    * An increase in the resolution of the analysis increment from 50 to 39 km.
    * The analysis increment is now applied incrementally (IAU approach), which permits the cycling of several physics variables.
    * Upgrade in the RTTOV radiative transfer package (From v10.2 to v12).
    * Changes to the weighting of the error covariances to give more weight to GEPS trial fields.
* Changes to observations:
    * Several improvements to the processing of radiosonde observations, atmospheric motion vectors (AMV), ground-based GPS, and aircraft data.
    * Addition of near-surface observations from the METAR network and MSC partner networks.
    * Addition of several clear-sky radiance (CSR) channels, primarily for water vapour.

A copy of the official note announcing the implementation of these changes [is available at this link](http://dd.meteo.gc.ca/doc/genots/2018/09/17/NOCN03_CWAO_171330___59181).

A technical note with more details on this change [is available at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_rdps-600_20180918_e.pdf).

The technical specifications document for RDPS 6.0.0 [is available at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_RDPS_6.0.0_e.pdf).


## Wednesday September 7, 2016

### Upgrade to Version 5.0.0 of the Regional Deterministic Prediction System (RDPS) at the Canadian Meteorological Centre

On Wednesday, September 7th 2016, starting with the 1200 UTC run, the Meteorological Service of Canada's Canadian Meteorological Centre (CMC) will upgrade the Regional Deterministic Prediction System (RDPS) to version 5.0.0.
The changes included in this upgrade are summarized as follows:

* Changes to the forecast model:
    * The version of GEM is upgraded from v3.3.8.2-isba (unstaggered vertical levels) to v4.8.2 (staggered vertical levels).
    * The Global Deterministic Prediction System (GDPS) replaces the previous pilot model thanks to the introduction of a new GDPS run (G0) with cut-off of 120 min.
    * A new grid based on the GDPS Yin grid replaces the existing rotated lat-lon grid.
    * The representation of model output at the surface has been modified.
    * The OCM sequencer is replaced by the new Maestro sequencer.
* Changes to the assimilation system:
    * None.
* Changes to observations:
    * None.


A copy of the official note announcing the implementation of these changes [is available at this link](http://dd.meteo.gc.ca/doc/genots/2016/09/02/NOCN03_CWAO_022050___00740).

A technical note with more details on this change [is available at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/lib/technote_rdps-500_20160907_e.pdf).

The technical specifications document for RDPS 5.0.0 [is available at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_RDPS_5.0.0_e.pdf).


## Tuesday December 15, 2015

### Upgrade to Version 4.1.0 of the Regional Deterministic Prediction System (RDPS) at the Canadian Meteorological Centre

On Tuesday December 15th 2015, starting with the 1200 UTC run, the Meteorological Service of Canada's Canadian Meteorological Centre (CMC) will upgrade the Regional Deterministic Prediction System (RDPS) to version 4.1.0.
The changes included in this upgrade are summarized as follows:

* Changes to the forecast model:
    * The horizontal grid spacing of the global driver model decreases from 33 to 25 km.
    * The lateral boundary conditions of the driver model are now provided every 30 minutes (rather than every 60 minutes).
* Changes to observations:
    * Addition of radiance observations from 17 channels of the Advanced Microwave Sounding Unit (ATMS).
    * 103 additional Cross-track Infrared Sounder (CrIS) channels.
    * More than 600 additional ground-based GPS sites (mostly in Europe).
    * Introduction of inter-channel correlations for all infrared and microwave radiances.


A copy of the official note announcing the implementation of these changes [is available at this link](http://dd.meteo.gc.ca/doc/genots/2015/12/14/NOCN03_CWAO_142130___00044).

A technical note with more details on this change [is available at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/lib/technote_rdps-410_20151215_e.pdf).

The technical specifications document for RDPS 4.1.0 [is available at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_RDPS_4.1.0_e.pdf).


## Tuesday November 18th 2014

### Major Upgrade to the Regional Deterministic Prediction System (RDPS) version 4.0.0 at the Canadian Meteorological Centre

On Tuesday November 18th 2014, starting with the 1200 UTC run the Meteorological Service of Canada's Canadian Meteorological Centre (CMC) will upgrade the Regional Deterministic Prediction System (RDPS) to version 4.0.0.
Summary of the major changes included in this upgrade:

* New 4D-EnVAR assimilation technique replaces 4D-VAR.
    * Coupling with the ensemble Kalman filtre (EnKF) to obtain background-error covariances.
* Changes to observations
    * Improved treatment of radiosonde and aircraft observations.
    * Assimilation of ground-based GPS data.
    * Improved satellite radiance bias correction procedure.
    * Additional AIRS/IASI channels assimilated.
* New sea-ice concentration analysis.


A copy of the official note announcing the implementation of these changes [is available at this link](http://dd.meteo.gc.ca/doc/genots/2014/11/14/NOCN03_CWAO_141800___00705).

A technical note with more details on this change [is available at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/lib/technote_rdps-400_20141118_e.pdf).


## Tuesday July 3rd 2013

### Update to the RDPS binary (in support of the production of the variable PX)


## Wednesday February 13, 2013

### Regional Deterministic Prediction System (RDPS) version 3.1.0 installed at the Canadian Meteorological Centre

On Wednesday February 13 2013, starting with the 1200 UTC run, the Canadian Meteorological Centre (CMC) will implement version 3.1.0 of the Regional Deterministic Prediction System (RDPS) in order to harmonize it with the [implementation on that same day of the GDPS-3.0.0](../nwp_gdps/changelog_gdps_en.md). As a result, RDPS forecasts are improved as a result.

Please consult the documentation available regarding the GDPS-3.0.0 implementation [at this link for more information](../nwp_gdps/changelog_gdps_en.md).


## Wednesday October 19 2012

### Regional Deterministic Prediction System (RDPS) Data Assimilation Window extended by 5 minutes

Starting with the 18Z run of October 19 2012, the [00,06,12,18]Z runs of the RDPS will now be launched at [00,06,12,18]Z+2:00 allowing those runs to collect an additional 5 minutes of observation data prior to the model integration.


## Wednesday October 3 2012

### Major Upgrade to the Regional Deterministic Prediction System (RDPS) at the Canadian Meteorological Centre

On Wednesday October 3 2012, starting with the 1200 UTC run, the Canadian Meteorological Centre (CMC) will implement version 3.0.0 of the Regional Deterministic Prediction System (RDPS). This version includes an increase in resolution to 10 km from the previous 15 km, a 4D-Var data assimilation system replacing the previous 3D-Var, as well as important changes in the GEM model physics. This results in significant forecast improvements especially for the winter season.

As part of this implementation the cutoff time for collecting observations has been reduced by 10 minutes and is now [00,06,12,18]Z+1:55

Objective scores show improvements in the forecasts with most metrics throughout most of the atmosphere, in particular for the lower portion of the atmosphere and at the surface. A subjective evaluation by operational meteorologists confirmed those improvements. Other forecast systems which depend on RDPS ouput include similar changes and as a result they also benefit from this version of the RDPS.

A copy of the official note describing these changes and the verification work leading up to this implementation [is available by clicking here](http://dd.weatheroffice.ec.gc.ca/doc/genots/2012/10/02/NOCN03_CWAO_021644___00044).

A technical note with more details on this change [is available at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/lib/op_systems/doc_opchanges/technote_rdps300_20121003_e.pdf).
