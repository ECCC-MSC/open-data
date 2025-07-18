[En français](changelog_hrdps_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [HRDPS](readme_hrdps_en.md) > HRDPS Changelog

# Chronology of changes to the High Resolution Deterministic Prediction System (HRDPS)

## Wednesday July 23, 2025

### Implementation of a statistical post-processing system, PROGNOS v1.0.0, for the High Resolution Deterministic Prediction System (HRDPS) 7.0.0 of the Canadian Meteorological Centre (CMC)

On Wednesday, July 23, 2025, starting with the 1200 UTC run, the Canadian Meteorological Centre (CMC) will implement a new statistical post-processing system PROGNOS.

A copy of the official note announcing this implementation [is available via this link](https://dd.weather.gc.ca/doc/genots/2025/07/23/NOCN03_CWAO_DDHHHH___XXX).

The technical specifications document for PROGNOS v1.0.0 is available [via this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/PROGNOS_Specifications_techniques-202507.pdf).

## Monday May 26th, 2025

Addition of ATMS and CrIS observations from the NOAA-21 satellite and RARS-MWHS2 observations from the FY-3D and FY-3E satellites in the HRDPS
On Monday May 26th, 2025, starting with the 0600 UTC run, the Canadian Meteorological Centre (CMC) of the Meteorological Service of Canada (MSC) proceeded with an update to version 7.0.0 of the High-Resolution Deterministic Prediction System (HRDPS).

Only the data assimilation component was modified to add the following satellite observation sources:

* Addition of ATMS and CrIS observations from the NOAA-21 satellite,
* Addition of (DBnet) RARS-MWHS2 observations from the FY-3D and FY-3E satellites.

## Wednesday April 2, 2025

### Technical update of atmospheric data assimilation systems

On Wednesday April 2nd, 2025, starting with the 0600 UTC run, the Canadian Meteorological Centre (CMC) of the Meteorological Service of Canada (MSC) proceeded with an update to version 7.0.0 of the High Resolution Deterministic Prediction System (HRDPS).

Only the data assimilation component was modified:

* Different thinning scheme for SSMIS satellite observations allowing for more data assimilated
* Correction to the azimuth angle for slant-path computation for AMSUA and MHS radiances

## Wednesday October 23, 2024

### Addition of new satellite observation sources in the HRDPS

On Wednesday October 23rd, 2024, starting with the 0600 UTC run, the Canadian Meteorological Centre (CMC) of the Meteorological Service of Canada (MSC) proceeded with an update to version 7.0.0 of the High Resolution Deterministic Prediction System (HRDPS).

Only the data assimilation component was modified to add the following satellite observation sources:

* Addition of sea surface wind observations from the HSCAT scatterometer of the HY-2B and HY-2C satellites.

## Tuesday June 11, 2024

### Major upgrade to Version 7.0.0 of the High Resolution Deterministic Prediction System (HRDPS) at the Canadian Meteorological Centre

On Tuesday June 11, 2024, starting with the 1200 UTC run, the Canadian Meteorological Centre (CMC) will upgrade the High Resolution Deterministic Prediction System (HRDPS) to version 7.0.0.

Significant changes:

* Asssimilation cycle now using boundary conditions from the [Global Deterministic Prediction System (GDPS)](../nwp_gdps/readme_gdps_en.md).
* Upgrade from GEM 5.1.2 to 5.2.1.
* Forecast component now using boundary conditions from a 10km component of the [Global Deterministic Prediction System (GDPS)](../nwp_gdps/readme_gdps_en.md).


A brief summary of the innovations included in this upgrade and their impact on performance can be found [in this document](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/fact_sheets/factsheet_hrdps-700_e.pdf).

A copy of the official note announcing the implementation of these changes is available at [this link](https://dd.meteo.gc.ca/doc/genots/2024/06/10/NOCN03_CWAO_101857___46443).

A technical note with more details on HRDPS v7.0.0 is available [at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_hrdps-700_e.pdf).

The technical specifications document for HRDPS v7.0.0 is available [at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_HRDPS_7.0.0_e.pdf).



## Thursday November 2, 2023

### Addition of CSR observations from the GOES-18 satellite in the HRDPS

On Thursday November 2nd, 2023, starting with the 1200 UTC run, the Canadian Meteorological Centre (CMC) of the Meteorological Service of Canada (MSC) proceeded with an update to version 6.1.0 of the High Resolution Deterministic Prediction System (HRDPS).

Only the data assimilation component was modified to include the following observations:

Addition of CSR (Clear-Sky Radiance) infrared radiances from the GOES-18 satellite.

## Tuesday December 12, 2023

### Canadian Meteorological Centre's High Resolution Deterministic Prediction System (HRDPS) weather elements on the grid (WEonG) updated to version 2.2.0

On Tuesday, December 12, 2023, as of the 1200 UTC run, the Canadian Meteorological Centre (CMC) has updated the weather elements on the grid (WEonG) of the High Resolution Deterministic Prediction System (HRDPS) to version 2.2.0.

Summary of the changes included in this update:

* Interpolate to the grid the statistically corrected values of surface temperatures at points, supplied by UMOS using the MIDAS interpolation tool
* Production of integrated concepts over three-hour periods 
* Addition of significant precipitation type
* Modifications to the snow squall detection probability algorithm
* Activation of the "Garry Morning Patch" to prolong the presence of morning radiation fog until the solar angle reaches a specific threshold

The official note announcing the implementation of these changes is available [at this link](https://dd.weather.gc.ca/doc/genots/2023/12/19/NOCN03_CWAO_191614___49612).

A technical note on this subject is available [via this link](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_notes/technote_weong-hrdps-220_e.pdf).

## Thursday September 14, 2023

### Addition of commercial GNSS-RO observations from PlanetIQ in the HRDPS

On Thursday September 14th, 2023, starting with the 0000 UTC run, the Canadian Meteorological Centre (CMC) of the Meteorological Service of Canada (MSC) proceeded with an update to version 6.1.0 of the High Resolution Deterministic Prediction System (HRDPS).

Only the data assimilation component was modified to include the following observations:

Addition of commercial GNSS-RO (Global Navigation Satellite System Radio Occultation) observations from PlanetIQ’s constellation of GNOMES small satellites.

## Wednesday July 5, 2023

### Addition of commercial GNSS-RO observations from Spire in the HRDPS

On Wednesday July 5th, 2023, starting with the 0000 UTC run, the Canadian Meteorological Centre (CMC) of the Meteorological Service of Canada (MSC) proceeded with an update to version 6.1.0 of the High Resolution Deterministic Prediction System (HRDPS).

Only the data assimilation component was modified to include the following observations:

Addition of commercial GNSS-RO (Global Navigation Satellite System Radio Occultation) observations from Spire’s constellation of LEMUR nanosatellites.

## Wednesday February 15, 2023

### Addition of GPSRO observations from the Sentinel-6A satellite in the HRDPS

On Wednesday February 15th, 2023, starting with the 0000 UTC run, the Canadian Meteorological Centre (CMC) of the Meteorological Service of Canada (MSC) proceeded with an update to version 6.1.0 of the High Resolution Deterministic Prediction System (HRDPS).

Only the data assimilation component was modified to include the following observations:

Addition of GPSRO (Global Positioning System Radio Occultation) observations from the Sentinel-6A.

## Wednesday January 4, 2023

### Replacement of Atmospheric Motion wind Vectors from GOES-17 by those from GOES-18 in the HRDPS

On Wednesday January 4th, 2023, starting with the 1800 UTC run, the Canadian Meteorological Centre (CMC) of the Meteorological Service of Canada (MSC) proceeded with an update of version 6.1.0 of the High Resolution Deterministic Prediction System (HRDPS).

Only the data assimilation component was modified to include the following observations:

Replacement of Atmospheric Motion wind Vectors (AMV) from GOES-17 by those from GOES-18.

## Thursday November 3, 2022

### Addition of surface observations received from ships in BUFR format in the HRDPS

On Thursday November 3rd, 2022, starting with the 0600 UTC run, the Canadian Meteorological Centre (CMC) of the Meteorological Service of Canada (MSC) proceeded with an update of version 6.1.0 of the High Resolution Deterministic Prediction System (HRDPS).

Only the data assimilation component was modified to include the following observations:

Addition of surface observations received from ships in BUFR (Binary Universal Form for the Representation of meteorological data) format. TAC (Traditional Alphanumeric Codes) observations were already being assimilated previously.

## Tuesday June 28, 2022

### Upgrade to Version 6.1.0 of the HRDPS adapted to the New High Performance Computing Infrastructure.

See details [at this link](../changelog_multisystems_en.md).

## Wednesday February 16, 2022

### Addition of GPSRO observations from the GRACE-C and GRACE-D satellites in the HRDPS

On Wednesday February 16th, 2022, starting with the 0000 UTC run, the Canadian Meteorological Centre (CMC) of the Meteorological Service of Canada (MSC) proceeded with an update to version 6.0.0 of the High Resolution Deterministic Prediction System (HRDPS).

Only the data assimilation component was modified to include the following observations:

Addition of GPSRO (Global Positioning System Radio Occultation) observations from the GRACE-C and GRACE-D satellites.

## Wednesday December 1st, 2021

### Major upgrade to Version 6.0.0 of the High Resolution Deterministic Prediction System (HRDPS) at the Canadian Meteorological Centre

On Wednesday December 1st, 2021, starting with the 1200 UTC run, the Canadian Meteorological Centre (CMC) will upgrade the High Resolution Deterministic Prediction System (HRDPS) to version 6.0.0.

A brief summary of the innovations included in this upgrade and their impact on performance can be found [in this document](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/fact_sheets/factsheet_hrdps-600_e.pdf).

The official note announcing the implementation of these changes is available [at this link](http://dd.meteo.gc.ca/doc/genots/2021/11/26/NOCN03_CWAO_262118___50159).

A technical note with more details on HRDPS v6.0.0 is available [at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_hrdps-600_e.pdf).

The technical specifications document for HRDPS v6.0.0 is available [at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_HRDPS_6.0.0_e.pdf).


## Tuesday January 21, 2020

### Upgrade to Version 5.2.0 of the HRDPS adapted to the New High Performance Computing Infrastructure.

See details [at this link](../changelog_multisystems_en.md)


## Wednesday July 3, 2019

### Major upgrade to Version 5.1.0 of the High Resolution Deterministic Prediction System (HRDPS) at the Canadian Meteorological Centre

On Wednesday July 3rd, 2019, starting with the 1200 UTC run, the Canadian Meteorological Centre (CMC) will upgrade the High Resolution Deterministic Prediction System (HRDPS) to version 5.1.0.

The changes included in this upgrade are summarized as follows:

* Initial and boundary conditions are now provided by [RDPS v7.0.0](../nwp_rdps/changelog_rdps_en.md) instead of v6.0.0.
* RDPS-CGSL v3.4.0 replaces v3.3.0 as a pilot system over the St. Lawrence region.
* Upgrade from GEM v4.9.5 to GEM v4.9.8.

A copy of the official note announcing the implementation of these changes is available at [this link](http://dd.meteo.gc.ca/doc/genots/2019/06/28/NOCN03_CWAO_281830___34641).

The technical specifications document of the HRDPS 5.1.0 [is available at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_HRDPS_5.1.0_e.pdf).

A technical note with more details on HRDPS 5.1.0 is available [at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_hrdps-510_20190703_e.pdf).


## Tuesday September 18, 2018

### Major upgrade to Version 5.0.0 of the High Resolution Deterministic Prediction System (HRDPS) at the Canadian Meteorological Centre

On Tuesday, September 18, 2018, starting with the 1200 UTC run, the Canadian Meteorological Centre (CMC) will upgrade the High Resolution Deterministic Prediction System (HRDPS) to version 5.0.0.
The changes included in this upgrade are summarized as follows:

* Initial and boundery conditions comming from [RDPS v6.0.0](../nwp_rdps/changelog_rdps_en.md) instead of v5.1.0.
* Update GEM model from v4.8-LTS.13 to v4.9.4.
* New microphysics scheme "Predicted Particle Properties (P3)" replaces Milbrandt-Yau (MY2).
* Inclusion of the Town Energy Balance (TEB) urban parameterization scheme

A copy of the official note announcing the implementation of these changes is available at [this link](http://dd.meteo.gc.ca/doc/genots/2018/09/17/NOCN03_CWAO_171332___49260).

A technical note with more details on HRDPS 5.0.0 is available [at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_hrdps-500_20180918_e.pdf).


## Thursday December 14, 2017

### The High Resolution Deterministic Prediction System (HRDPS) is declared operational at the Canadian Meteorological Centre

Effective December 14, 2017, after several years running in experimental mode, the Canadian Meteorological Centre (CMC) of the Meteorological Service of Canada declared operational the High Resolution Deterministic Prediction System (HRDPS v4.4.0).

A copy of the official note announcing the implementation of these changes [is available at this link](http://dd.meteo.gc.ca/doc/genots/2017/12/13/NOCN03_CWAO_132058___00004).

A technical note with more details on v4.2.0 of this system [is available at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_hrdps-420_20160907_e.pdf).


## Wednesday September 7, 2016

### Upgrade to Version 4.2.0 of the High Resolution Regional Deterministic Prediction System (HRDPS)

On Wednesday, September 7th 2016, starting with the 1200 UTC run, the Meteorological Service of Canada's Canadian Meteorological Centre (CMC) will upgrade the High Resolution Regional Deterministic Prediction System (HRDPS) to version 4.2.0.
The changes included in this upgrade are summarized as follows:

* Changes to the forecast model:
    * The version of GEM is upgraded from version 4.7.3 to version 4.8.2.
    * The introduction of a physically-based hysteresis effect in the turbulent mixing scheme that improves the forecast of precipitation types.
    * Change to the horizontal diffusion for the momentum variables, (from a del-4 operator to a del-2) in order to reduce noise in the precipitation field
    * Minor changes to the surface data assimilation system (CaLDAS).
* Changes to the grid configuration:
    * A new forecast domain has been added to the HRDPS which is called 'North' and covers the Canadian arctic region.
    * As a result, forecasts for the domains known as 'Arctic' and 'Lancaster' will be discontinued.
    * View [this image](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/hrdps/hrdps_4.2.0_grids_snapshot.png) which illustrates the changes.


A copy of the official note announcing the implementation of these changes [is available at this link](http://dd.meteo.gc.ca/doc/genots/2016/09/02/NOCN03_CWAO_022055___00741).

A technical note with more details on this change [is available at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/lib/technote_hrdps-420_20160907_e.pdf).


## Tuesday December 15 2015

### Upgrade to Version 4.1.0 of the High Resolution Deterministic Prediction System (HRDPS) at the Canadian Meteorological Centre

On Tuesday December 15th 2015, starting with the 1200 UTC run, the Meteorological Service of Canada's Canadian Meteorological Centre (CMC) will upgrade the Resolution Deterministic Prediction System (HRDPS) to version 4.1.0.
The changes included in this upgrade are summarized as follows:

* The use of an implicit convection scheme Kain & Fritsch
* Correction for freezing rain events that were largely under-estimated in the HRDPS-4.0.0

A copy of the official note announcing the implementation of these changes [is available at this link](http://dd.meteo.gc.ca/doc/genots/2015/12/14/NOCN03_CWAO_142228___00074).

A technical note with more details on this change [is available at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/lib/technote_hrdps-410_20151215_e.pdf).


## Tuesday November 18th 2014

### Major Upgrade to the High Resolution Deterministic Prediction System (HRDPS) version 4.0.0 at the Canadian Meteorological Centre

On Tuesday November 18th 2014, starting with the 1200 UTC run the Meteorological Service of Canada's Canadian Meteorological Centre (CMC) will upgrade the experimental High Resolution Deterministic Prediction System (HRDPS) to version 4.0.0.

A copy of the official note announcing the implementation of these changes [is available at this link](http://dd.meteo.gc.ca/doc/genots/2014/11/17/NOCN03_CWAO_171911___00921).

A technical note with more details on this change [is available at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/lib/technote_hrdps-400_20141118_e.pdf).


## Friday July 12 2013

### Adjustments to High Resolution Deterministic Prediction System (HRDPS) to version 3.0.1

The Canadian Meteorological Centre adjusts the HRDPS system.

On July 12 2013, the native grid of the HRDPS arctic domain was adjusted so that the native grid is shifted slightly westward and extended farther north and south.

The [image at this link here](http://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/hrdps/20130710_HRDPSArcticGrid_BluePrevious_BlackNew.jpg) shows the original operational HRDPS arctic grid (blue box) and the newly installed HRDPS arctic domain grid (black box).

This change follows requests by operational meteorologists for a HRDPS arctic domain that could provide forecast data for Ungava Bay and eastern portions of Hudson Bay, especially in the busy summer season.

Users of the Ninjo workstation should be made aware that despite this change to the native HRDPS arctic grid, that Ninjo workstations will continue to receive the same configuration of HRDPS arctic grib2 files. This means that after July 12 2013, users of Ninjo HRDPS arctic grib2 data should not use lam arctic data east of longitude 60 west for decision making. These HRDPS arctic Ninjo grib2 files will only be updated at the next scheduled software update.

On the other hand, the HRDPS grib2 files distributed via the datamart have been adjusted to present data on the new HRDPS arctic grid. The documentation associated with these grib2 files can only be updated however at a later date.

Another adjustment to the HRDPS system was installed on June 18 2013 and this was a correction to the post processed calculations of the HRDPS summer severe weather parameters. This correction applies to the calculations performed on all HRDPS domains.

A copy of the official note describing these changes [is available by clicking here](http://dd.weatheroffice.ec.gc.ca/doc/genots/2013/07/12/NOCN03_CWAO_122020___01071).


## Wednesday October 3 2012

### The Canadian Meteorological Centre Upgrades Its High Resolution Deterministic Prediction System (HRDPS) to version 3.0.0

On Wednesday October 3 2012, starting with the implementation of a new 1800 UTC run of the west domain, the Canadian Meteorological Centre (CMC) will procede with an update to version 3.0.0 of the High Resolution Deterministic Prediction System (HRDPS) at 2.5 km resolution.

Modifications to all HRDPS domains involve the use of a newer version of the CMC GEM model and adjustments to the model dynamics and physics. For the west HRDPS only, the nesting configuration, the run frequency and the forecast lead times have been changed.

Note that this HRDPS update is done in conjunction with the major upgrade to the CMC Regional Deterministic Prediction System (RDPS) which provides initial and lateral boundary conditions to the HRDPS. For details on the [RDPS upgrade please refer to the information at this link](../nwp_rdps/changelog_rdps_en.md).

All forecast products presently available for HRDPS will continue to be available. For the west domain the previous datafiles labelled 12 UTC will now use earlier data from the RDPS and as a result will be labelled 06 UTC. There is also the addition of a second daily west domain run that will be labelled 18 UTC. It must be noted that for some time, in spite of the longer lead times extending to 42 hours for the west domain, meteorological fields will displayed in the NINJO visualization platform will only be visible up to the 24-hour lead time.

With this implementation all HRPDS domains continue to maintain their status as experimental. The are plans to make the HRDPS west domain fully operational and this announcement should follow in the near future.

A copy of the official note describing these changes [is available by clicking here](http://dd.weatheroffice.ec.gc.ca/doc/genots/2012/10/02/NOCN03_CWAO_021948___00154).

A technical note with more details on these changes [will be made available at this link here](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/lib/op_systems/doc_opchanges/technote_hrdps_20121003_e.pdf).


## Thursday December 22, 2011

### The Canadian Meteorological Centre implements a correction to its HRDPS snow analysis

A correction was made to grid of the High Resolution Deterministic Prediction System (HRDPS) snow analysis starting with the 06 UTC snow analysis of Dec 22 2011.

With this correction the HRDPS is now version 2.2.1




