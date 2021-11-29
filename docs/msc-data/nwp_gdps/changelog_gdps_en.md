[En français](changelog_gdps_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [GDPS](readme_gdps_en.md) > GDPS Changelog

# Chronology of changes to the Global Deterministic Prediction System (GDPS)

## Wednesday December 1st, 2021

### Upgrade to Version 8.0.0 of the Global Deterministic Prediction System (GDPS) at the Canadian Meteorological Centre

On Wednesday December 1st, 2021, starting with the 1200 UTC run, the Canadian Meteorological Centre (CMC) will upgrade the Global Deterministic Prediction System (GDPS) to version 8.0.0.

A brief summary of the innovations included in this upgrade and their impact on performance can be consulted in this document: [GDPS_8.0.0_innovations](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/fact_sheets/factsheet_gdps-800_e.pdf). For detailed description of this upgrade, please see the [Technical note](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_gdps-800_e.pdf).


Associated Notes:

* [Official note announcing the implementation](http://dd.weather.gc.ca/doc/genots/2021/11/26/NOCN03_CWAO_262118___50159).
* [Technical note](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_gdps-800_e.pdf).
* [Technical specifications of GDPS 8.0.0](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_GDPS_8.0.0_e.pdf).


## Tuesday January 26th, 2021

### Addition and replacement of satellite radiance observations

On Tuesday January 26th, 2021, starting with the 0600 UTC run, the Canadian Meteorological Centre (CMC) of the Meteorological Service of Canada (MSC) proceeded with an update to version 7.1.0 of the Global Deterministic Prediction System (GDPS).

Only the data assimilation component was modified to include and substitute the following observations:

* Addition of microwave radiances from the MWHS-2 instrument aboard the FY-3C satellite
* Replacement of infrared radiances from the IASI instrument aboard the MetOp-2/A satellite by those from MetOp-3/C

## Tuesday December 8th, 2020

### Addition of satellite radiance observations

On Tuesday December 8th, 2020, starting with the 0600 UTC run, the Canadian Meteorological Centre (CMC) of the Meteorological Service of Canada (MSC) proceeded with an update to version 7.1.0 of the Global Deterministic Prediction System (GDPS).

Only the data assimilation component was modified to include the following observations:

* Addition of microwave radiances from the AMSUA and MHS instruments aboard the MetOp-3/C satellite
* Addition of infrared radiances from the CrIS-FSR instrument aboard the NPP satellite
* Addition of CSR (Clear-Sky Radiance) infrared radiances from the GOES-17 satellite

## Friday June 26th, 2020

### Addition of GPSRO observations from the COSMIC-II satellites

On Friday June 26th, 2020, starting with the 0000 UTC run, the Canadian Meteorological Centre (CMC) of the Meteorological Service of Canada (MSC) proceeded with an update to version 7.1.0 of the Global Deterministic Prediction System (GDPS).

Only the data assimilation component was modified to include the following observations:

Addition of GPSRO (Global Positioning System Radio Occultation) observations from the COSMIC II satellites.

## Wednesday April 29th, 2020

### Addition of GPSRO observations from the PAZ and the KOMPSAT-5 satellites

On Wednesday April 29th, 2020, starting with the 0000 UTC run, the Canadian Meteorological Centre (CMC) of the Meteorological Service of Canada (MSC) proceeded with an update to version 7.1.0 of the Global Deterministic Prediction System (GDPS).

Only the data assimilation component was modified to include the following observations:

Addition of GPSRO (Global Positioning System Radio Occultation) observations from the PAZ and the KOMPSAT-5 satellites.

## Tuesday April 28th, 2020

### Addition of AMV observations from the MetOp-3/C satellite

On Tuesday April 28th, 2020, starting with the 0600 UTC run, the Canadian Meteorological Centre (CMC) of the Meteorological Service of Canada (MSC) proceeded with an update to version 7.1.0 of the Global Deterministic Prediction System (GDPS.

Only the data assimilation component was modified to include the following observations:

Addition of AMV (Atmospheric Motion Vector) observations from the MetOp-3/C satellite.

## Tuesday January 21, 2020

### Upgrade to Version 7.1.0 of the GDPS adapted to the New High Performance Computing Infrastructure.

See details [at this link](../changelog_multisystems_en.md)

## Tuesday July 23, 2019

### Additional observations data in the Global Deterministic Prediction System (GDPS) at the Canadian Meteorological Centre

On Tuesday July 23rd 2019, starting with the 0600 UTC run, the Meteorological Service of Canada's Canadian Meteorological Centre (CMC) proceeded with an update of its Global Deterministic Prediction System (GDPS).

The data assimilation component of the GDPS system was modified to use additional observations in seven observations families. All these families were already used, this upgrade mainly increase the data assimilation systems robustness.

[Details of these changes can be consulted in the official note](http://dd.meteo.gc.ca/doc/genots/2019/07/23/NOCN03_CWAO_231247___30255).

* [Technical specifications document of the GDPS 7.0.0](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_GDPS_7.0.0_e.pdf).

## Wednesday July 3, 2019

### Upgrade to Version 7.0.0 of the Global Deterministic Prediction System (GDPS) at the Canadian Meteorological Centre

On Wednesday July 3rd 2019, starting with the 1200 UTC run, the Canadian Meteorological Centre (CMC) of the Meteorological Service of Canada will upgrade the Global Deterministic Prediction System (GDPS) to version 7.0.0.
The changes included in this upgrade are summarized as follows:

* Changes to the atmospheric component of the forecast model:
    * Upgrade from GEM v4.8-LTS.16 to GEM v5.0.0. [More informations on GEM-5](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/GEM5_paper_submitted_JAMES_20190614.pdf).
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

Notes:

* [Official note announcing the implementation](http://dd.weather.gc.ca/doc/genots/2019/06/28/NOCN03_CWAO_281719___09158).
* [Technical note](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_gdps-700_e.pdf).
* [Technical specifications of the GDPS 7.0.0](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_GDPS_7.0.0_e.pdf).


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

Notes:

* [Official note announcing the implementation](http://dd.weather.gc.ca/doc/genots/2018/09/14/NOCN03_CWAO_142110___13748).
* [Technical note](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_gdps-610_20180918_e.pdf).
* [Technical specifications of the GDPS 6.1.0](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_GDPS_6.1.0_e.pdf).


## Wednesday November 1, 2017

### Major Upgrade to Version 6.0.0 of the Global Deterministic Prediction System (GDPS) at the Canadian Meteorological Centre

On Wednesday November 1st 2017, starting with the 1200 UTC run, the Meteorological Service of Canada's Canadian Meteorological Centre (CMC) will upgrade the Global Deterministic Prediction System (GDPS) to version 6.0.0.
The changes included in this upgrade are summarized as follows:

* Changes to the forecast model:
    * Introduction of two-way coupling with an ice-ocean model. In the GDPS-6.0.0 forecast system, surface conditions evolve through coupling with the forecast component of the [Global Ice Ocean Prediction System (GIOPS)](../nwp_giops/changelog_giops_en.md). 
    * GDPS 6.0.0 is using GEM model version 4.8.2 (the main changes are associated with the surface interface, with only minor changes made to model physics and dynamics).
* No modifications were made to the assimilation component nor observations ingested in this upgrade of the GDPS.

Notes:

* [Official note announcing the implementation](http://dd.weather.gc.ca/doc/genots/2017/10/30/NOCN03_CWAO_301922___01740).
* [Technical note](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_gdps-600_20171101_e.pdf).
* [Technical specifications of the GDPS 6.0.0](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_GDPS_6.0.0_e.pdf).


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

Notes:

* [Official note announcing the implementation](http://dd.meteo.gc.ca/doc/genots/2015/12/14/NOCN03_CWAO_142125___00050).
* [Technical note](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_gdps-500_20151215_e.pdf).
* [Technical specifications of the GDPS 5.0.0](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_GDPS_5.0.0_e.pdf).


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


Notes:

* [Official note announcing the implementation](http://dd.meteo.gc.ca/doc/genots/2014/11/14/NOCN03_CWAO_141410___00630).
* [Technical note](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/lib/technote_gdps-400_20141118_e.pdf).

## Tuesday May 6th 2014

### Addition of IASI observations from METOP-B/1 to the operational data of the GDPS

On April 30th, 2014, starting with the 0600 UTC trial-field run of the Global Deterministic Prediction System (GDPS), the Canadian Meteorological Centre (CMC) of Environment Canada added radiance observations from the IASI instrument aboard the METOP-B/1 satellite to the operational data assimilation system. IASI is the last of the instruments on-board the METOP-B/1 satellite to be included in the operational data assimilation systems.

Motivation for the incorporation of IASI observations from METOP-B/1 in the operational data of the GDPS:

* Although IASI data from METOP-A/2 will continue to be assimilated into our forecast systems, METOP-B/1 is now the operational METOP satellite of the EUMETSAT agency. The two satellites METOP-A/2 and METOP-B/1 have similar trajectories, but offset by a half-orbit, so the addition of METOP-B/1 IASI data will almost double the number of IASI data assimilated. Furthermore, these new data add robustness to the data assimilation system in the event of a failure of the IASI instrument on-board either METOP-A/2 or METOP-B/1.

Following this change, the version of the GDPS system is changed from 3.1.0 to 3.1.1.
You can also access the GDPS products page by [clicking here](readme_gdps_en.md).

[Official note of the implementation  with information on verification work](http://dd.meteo.gc.ca/doc/genots/2014/05/08/NOCN03_CWAO_081640___00938).

## Thursday November 7 2013

### Additional satellite data (CSR, ATOVS, polar winds) added to the GDPS assimilation systems and various other adjustments

On Thursday November 7 2013, additional satellite data was added to the operational data assimilation system of the Global Deterministic Prediction System (GDPS). Changes include the following: additional CSR (Clear Sky Radiance) radiances from MeteoSat10, additional ATOVS radiances from Metop-B and additional AVHRR polar winds from Metop-B.

Along with the addition of satellite data, there were also other adjustments made to the systems. There was an update of the spectroscopic coefficient files used by the RTTOV radiative transfer model for computing the simulated observations (the 6-hour "P"rognosis portion of the Observations-Prognosis (O-P) of the AMSUB and MHS instruments onboard all satellites. These new coefficients labelled as "Newstyle" do not separate out water vapor transmittances into line absorption and continuum absorption. The impact on the results are neutral.

As a result of all of the above changes installed in this implementation, the GDPS operational system becomes version 3.1.0.

## Monday August 12 2013

### Adjustments made so that scribe global matrices now available about 30 minutes earlier.

## Wednesday February 13, 2013

### Major Upgrade to the Global Deterministic Prediction System (GDPS) version 3.0.0 at the Canadian Meteorological Centre

On Wednesday February 13 2013, starting with the 1200 UTC run, the Canadian Meteorological Centre (CMC) will implement version 3.0.0 of the Global Deterministic Prediction System (GDPS).

This major upgrade includes a new version to the GEM model, important changes to the 4D-Var data assimilation scheme and to some of the model's physics schemes.

In this version, the grid of the model is also increased to a resolution of 25km. Also, this version now uses staggered hybrid vertical coordinates. [Information on staggered hybrid vertical coordinates](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/lib/op_systems/doc_opchanges/HybridVerticalCoordinateDefinitions_20130213.pdf) on the topic along with [a diagram](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/lib/op_systems/doc_opchanges/VerticalCoordinatesDiagram_afsysed_20130213.jpg).

Objective Scores show improvements in the forecasts with most metrics throughout most of the atmosphere, in particular over North America in winter. A subjective evaluation by operational meteorologists confirmed those improvements.

As part of this implementation the cutoff time for collecting observations has been reduced and is now [00,12]Z+3:05

Changes were also brought to the Regional Determnistic Prediction System (RDPS) to harmonize it with GDPS-3.0.0, and the RDPS forecasts are also improved. As a result of these RDPS adjustments, the version of RDPS is now 3.1.0

Notes:

* [Official note describing these changes and the verification work](http://dd.weatheroffice.ec.gc.ca/doc/genots/2013/02/07/NOCN03_CWAO_071810___00179).
* [Technical note](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/lib/op_systems/doc_opchanges/technote_gdps300_20130213_e.pdf).


## Wednesday November 16, 2011

### Improvements to the Global Deterministic Prediction System (GDPS v 2.2.0) of the Canadian Meteorological Centre

Starting on November 16 2011 at 06 UTC, the Canadian Meteorological Centre (CMC) will implement changes to the global and regional data assimilation systems by incorporating additional satellite data and by introducing a higher quality analysis of the sea surface temperature.

Here is an overview of changes involving global data assimilation system:

A. New Satellite Data: The following satellite data will be incorporated in the global and regional data assimilation systems:
- Sixty-two (62) infrared channels from the IASI instrument on board the METOP satellite.
- Seven (7) microwave channels from the SSM/IS instrument on board the DMSP F16 satellite.
- One (1) water vapor channel from the GOES-W, METSAT-1R and both METEOSAT satellites.
- A restriction to the infrared channels of the AIRS instrument in the polar regions will be removed.
- The horizontal thinning of all satellite radiance data, currently done at 250 km (except 200 km for SSM/I) will be reduced to 150 km, therefore adding much more satellite data to the systems.

B. Other Assimilation Changes:
- Moisture observations measured from properly equipped aircraft (AMDAR) will be assimilated.
- A new satellite data bias correction scheme will replace the current one. The main impact is the reduction of the time period to compute the bias corrections from 15 to 7 days. the same code is used for all radiance data.
- A modified version of the RTTOV radiative transfer code will be used for satellite radiance data.
- Also, a new sea surface temperature analysis on a grid of 0.20 degrees resolution will be used now by both global and regional systems.

As a consequence of these changes, the amount of observational data assimilated in the global data assimilation system will increase from about 1.9 million to 4.2 million pieces of information per day.

All of the above changes were combined and tested extensively during winter and summer seasons, including a parallel run of the global system. 

[Official note](http://dd.weatheroffice.ec.gc.ca/doc/genots/2011/11/15/NOCN03_CWAO_152020___05806).

With these changes the GDPS system is now version 2.2.0.
