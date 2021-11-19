[En français](changelog_geps_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [GEPS](readme_geps_en.md) > GEPS Changelog

# Chronology of changes to the Global Ensemble Prediction System (GEPS)

## Tuesday November 30, 2021

#### Upgrade to Version 7.0.0 of the Global Ensemble Prediction System (GEPS) at the Canadian Meteorological Centre

On Tuesday 30th 2021, starting with the 1200 UTC run, the Meteorological Service of Canada's Canadian Meteorological Centre (CMC) will upgrade the Global Ensemble Prediction System (GEPS) to version 7.0.0.

A brief summary of the innovations included in this upgrade and their impact on performance can be consulted in this document: [GEPS_7.0.0_innovations](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/fact_sheets/not_available.pdf). For detailed description of this upgrade, please see the [Technical note](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/not_available.pdf).


Associated Notes:

* [Official note announcing the implementation](http://dd.weather.gc.ca/doc/genots/2021/11/29/NOCN03_CWAO_XXXX).
* [Technical note](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/not_available.pdf).
* [Technical specifications of GEPS 7.0.0](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/not_available.pdf).


## Tuesday January 26th, 2021

### Replacement of satellite radiance observations

On Tuesday January 26th, 2021, starting with the 0600 UTC run, the Canadian Meteorological Centre (CMC) of the Meteorological Service of Canada (MSC) proceeded with an update to version 6.1.0 of the Global Ensemble Prediction System (GEPS).

Only the data assimilation component was modified to substitute the following observations:

* Replacement of infrared radiances from the IASI instrument aboard the MetOp-2/A satellite by those from MetOp-3/C

## Tuesday December 8th, 2020

### Addition of satellite radiance observations

On Tuesday December 8th, 2020, starting with the 0600 UTC run, the Canadian Meteorological Centre (CMC) of the Meteorological Service of Canada (MSC) proceeded with an update to version 6.1.0 of the Global Ensemble Prediction System (GEPS).

Only the data assimilation component was modified to include the following observations to its 4DEnVar analysis, whereas the EnKF analysis remained unchanged:

* Addition of microwave radiances from the AMSUA and MHS instruments aboard the MetOp-3/C satellite
* Addition of infrared radiances from the CrIS-FSR instrument aboard the NPP satellite
* Addition of CSR (Clear-Sky Radiance) infrared radiances from the GOES-17 satellite

## Friday June 26th, 2020

### Addition of GPSRO observations from the COSMIC-II satellites

On Friday June 26th, 2020, starting with the 0000 UTC run, the Canadian Meteorological Centre (CMC) of the Meteorological Service of Canada (MSC) proceeded with an update to version 6.1.0 of the Global Ensemble Prediction System (GEPS).

Only the data assimilation component was modified to include the following observations:

Addition of GPSRO (Global Positioning System Radio Occultation) observations from the COSMIC II satellites.

## Wednesday April 29th, 2020

### Addition of GPSRO observations from the PAZ and the KOMPSAT-5 satellites

On Wednesday April 29th, 2020, starting with the 0000 UTC run, the Canadian Meteorological Centre (CMC) of the Meteorological Service of Canada (MSC) proceeded with an update to version 6.1.0 of the Global Ensemble Prediction System (GEPS).

Only the data assimilation component was modified to include the following observations:

Addition of GPSRO (Global Positioning System Radio Occultation) observations from the PAZ and the KOMPSAT-5 satellites.

## Tuesday April 28th, 2020

### Addition of AMV observations from the MetOp-3/C satellite

On Tuesday April 28th, 2020, starting with the 0600 UTC run, the Canadian Meteorological Centre (CMC) of the Meteorological Service of Canada (MSC) proceeded with an update to version 6.1.0 of the Global Ensemble Prediction System (GEPS).

Only the data assimilation component was modified to include the following observations:

Addition of AMV (Atmospheric Motion Vector) observations from the MetOp-3/C satellite.

## Tuesday January 21, 2020

### Upgrade to Version 6.1.0 of the GEPS adapted to the New High Performance Computing Infrastructure.

See details [at this link](../changelog_multisystems_en.md)

## Tuesday July 23, 2019

### Additional observations data in the Global Ensemble Prediction System (GEPS) at the Canadian Meteorological Centre

On Tuesday July 23rd 2019, starting with the 0600 UTC run, the Meteorological Service of Canada's Canadian Meteorological Centre (CMC) proceeded with an update of its Global Ensemble Prediction System (GEPS).

The data assimilation component of the GEPS system was modified to use additional observations in seven observations families. All these families were already used, this upgrade mainly increase the data assimilation systems robustness.

The details of these changes can be consulted in the copy of the official note announcing the implementation [at this link](http://dd.meteo.gc.ca/doc/genots/2019/07/23/NOCN03_CWAO_231247___30255).

* The technical specifications document of the GEPS 6.0.0 [is available at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_GEPS_6.0.0_e.pdf).

## Wednesday July 3, 2019

#### Upgrade to Version 6.0.0 of the Global Ensemble Prediction System (GEPS) at the Canadian Meteorological Centre

On Wednesday July 3rd 2019, starting with the 1200 UTC run, the Meteorological Service of Canada's Canadian Meteorological Centre (CMC) will upgrade the Global Ensemble Prediction System (GEPS) to version 6.0.0.

The changes included in this upgrade are summarized as follows:

* Changes to the forecast model:
    * The atmospheric model is upgraded from GEM v4.8-LTS.13 to v4.8-LTS.16.
    * The atmospheric model is now coupled with the NEMO ocean model and the CICE ice model.
    * The ocean and sea-ice initial conditions come from the [GIOPS v3.0.0](../nwp_giops/changelog_giops_en.md) analysis.
    * Land surface initial conditions come from a surface pseudo-analysis using the GDPS 6.0.0 25 km grid and GEM v4.8.
* Changes to the assimilation component:
    * An ECMWF-hybrid gain is introduced to recenter all ensemble members around the mean of the EnKF analyses and the 4D-EnVAR analysis.
    * The EnKF is now assimilating dew-point depression (T-TD) data from radiosondes up to 100 hPa, instead of 200 hPa.
    * New sea-surface temperature and sea-ice analyses at 0.1 deg resolution (from 0.2 deg resolution).


A copy of the official note announcing the implementation of these changes [is available at this link](http://dd.meteo.gc.ca/doc/genots/2019/06/28/NOCN03_CWAO_281708___55818).

A technical note with more details on this change [is available at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_geps-600_e.pdf).

The technical specifications document of the GEPS 6.0.0 [is available at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_GEPS_6.0.0_e.pdf).


## Tuesday September 18, 2018

#### Upgrade to Version 5.0.0 of the Global Ensemble Prediction System (GEPS) at the Canadian Meteorological Centre

On Tuesday September 18th 2018, starting with the 1200 UTC run, the Meteorological Service of Canada's Canadian Meteorological Centre (CMC) will upgrade the Global Ensemble Prediction System (GEPS) to version 5.0.0.

The changes included in this upgrade are summarized as follows:

* Changes common to the assimilation and forecast components:
    * The gem model is upgraded from version 4.6.10 to 4.8.lts13
    * The 800 X 400 global gaussian grid at 50 km resolution is updated to a Yin-Yang grid at 39 km resolution
    * The geophysical fields are now generated using internal genphysX software in place of GENESIS software
* Changes to the assimilation component only:
    * The digital filter (DF) initialization is replaced by an incremental analysis update (IAU) procedure
    * The model has a higher top (from 2 hpa to 0.1 hpa) with 81 vertical levels instead of 74
    * Infrared observations (AIRS, IASI and CrIS) are added
    * Further thinning is applied for satellite wind, radiance, aircraft, and scatterometer observations
    * The RTTOV operator is upgraded from version 10 to 12
* Changes to the forecast component only:
    * The model has a higher top (from 2 hpa to 0.1 hpa) with 45 vertical levels instead of 41
    * New method to generate markov chains
* Reforecats period updated from 1995-2014 to 1998-2017
* Products now available on a new user grid at a 25-km resolution


A copy of the official note announcing the implementation of these changes [is available at this link](http://dd.meteo.gc.ca/doc/genots/2018/09/14/NOCN03_CWAO_142038___52733).

A technical note with more details on this change [is available at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_geps-500_20180918_e.pdf).

The technical specifications document of the GEPS 5.0.0 [is available at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_GEPS_5.0.0_e.pdf).


## Tuesday December 15, 2015

#### Upgrade to Version 4.1.1 of the Global Ensemble Prediction System (GEPS) at the Canadian Meteorological Centre

On Tuesday December 15th 2015, starting with the 1200 UTC run, the Meteorological Service of Canada's Canadian Meteorological Centre (CMC) will upgrade the Global Ensemble Prediction System (GEPS) to version 4.1.1.

The changes included in this upgrade are summarized as follows:

* Numerical diffusion of the potential temperature field is now applied for all ensemble members (rather than only half the members).
* A damping gradient is applied to limit the diffusion of potential temperature near the poles.
* New observation errors for radiance data and GPS Radio-Occultation (GPS-RO) observations
* Addition of radiance observations from the Advanced Microwave Sounding Unit (ATMS)
* Addition of GPS-RO observations from the TanDEM and GRACE-B satellites
* The reforecast period is extended from 18 to 20 years


A copy of the official note announcing the implementation of these changes [is available at this link](http://dd.meteo.gc.ca/doc/genots/2015/12/14/NOCN03_CWAO_142212___00073).

A technical note with more details on this change [is available at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/lib/technote_geps-411_20151215_e.pdf).

The technical specifications document of the GEPS 4.1.1 [is available at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_GEPS_4.1.1_e.pdf).


## Tuesday November 18th 2014

#### Major Upgrade to the Global Ensemble Prediction System (GEPS) version 4.0.0 at the Canadian Meteorological Centre

On Tuesday November 18th 2014, starting with the 1200 UTC run the Meteorological Service of Canada's Canadian Meteorological Centre (CMC) will upgrade the Global Ensemble Prediction System (GEPS) to version 4.0.0.

Summary of the major changes included in this upgrade:

* Coupling with 4D-EnVAR to provide background error covariances
* Ensemble size of the EnKF increased from 192 to 256 members
* Reduction of the GEM model time step from 20 minutes to 15 minutes
* Model top raised from 1.78 hPa to 1.45 hPa
* Changes to observation bias correction and RTTOV operator

A copy of the official note announcing the implementation of these changes [is available at this link](http://dd.meteo.gc.ca/doc/genots/2014/11/14/NOCN03_CWAO_141745___01237).

A technical note with more details on this change [is available at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/lib/technote_geps-400_20141118_e.pdf).

A technical note on the improvements made to the reforecast system [is available at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/lib/Tech_Note_GEPS400_reforecast_v1.1_E.pdf).


## Wednesday December 4th 2013

#### Major Upgrade to the Global Ensemble Prediction System (GEPS) version 3.1.0 at the Canadian Meteorological Centre

On Wednesday December 4th 2013, starting with the 1200 UTC run the Meteorological Service of Canada's Canadian Meteorological Centre (CMC) will upgrade the Global Ensemble Prediction System (GEPS) to version 3.1.0.

This new version of GEPS will use a newer version of the GEM model (from 4.4.1 to 4.4.5). This change purely technical resulting in no difference in the forecasts in GEPS but allows easier system maintenance and greater consistency with other prediction systems at CMC.

On the assimilation part of the GEPS, we can say that radiance data ATOVS and AVHRR polar winds from an additional satellite, the METOP-B, are now assimilated. Also, there was an update of the spectroscopic coefficient used by the RTTOV radiative transfer model for computing the simulated observations of the AMSUB and MHS instruments onboard all satellites. Although the impacts of these changes on the forecasts are neutral, they can improve the robustness of the assimilation component of the system.

For the forecast component of the GEPS, the most important change is in the treatment of the surface temperature of the sea (SST). In the new GEPS, the SST value evolves with the forecast time using the persistence of the anomaly (deviation from the climatology) method. The SST value will change linearly with time (daily interpolation) from the initial value of the analysis of CMC toward the next mid-month value of the SST climatology, plus the initial SST anomaly.

Also, monthly forecasts (32 days) will be produced once a week on every Thursday at 00Z. Although the extended forecasts data will be available with this implementation, the introduction of specific monthly forecasts products is planned for later in 2014.

Another new element in GEPS 3.1.0 is the addition of historical ensemble forecasts for the last 18 years. These historical forecasts will be produced each week with a reduced set of 4 members (instead of 20). The outputs of this reforecast database will be used to generate statistics of climate model forecasts for monthly and eventually to calculate the Extreme Forecast Index (EFI) and to calibrate probabilistic forecasts.

A copy of the official note announcing the implementation of these changes along with information on verification work leading up to this implementation [is available at this link](http://dd.meteo.gc.ca/doc/genots/2013/12/03/NOCN03_CWAO_032258___00953).

A technical note with many more details on this change [is also available at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/lib/technote_geps310_20131204_e.pdf).


## Wednesday February 13, 2013

#### Major upgrade to the Global Ensemble Prediction System (GEPS) version 3.0.0 at the Canadian Meteorological Centre

On Wednesday February 13th 2013, starting with the 1200 UTC run the Meteorological Service of Canada's Canadian Meteorological Centre (CMC) will upgrade the Global Ensemble Prediction System (GEPS) to version 3.0.0.

In this upgrade, major changes are brought to both the assimilation (Ensemble Kalman Filter or ENKF) and forecast components of the system. The ENKF is used to supply initial conditions to the GEPS, while the forecast component provides forecasts out to 16 days using the Canadian Global Environmental Multi-scale model (GEM). Those forecasts are shared with North American Ensemble Forecast System (NAEFS) partners, hence changes to our system will have an impact on the NAEFS forecasts.

Changes common to both the assimilation and forecast components include: a newer version 4.4.1 of the GEM model with improved physics; reduction of the model time step from 30 minutes to 20 minutes; use of a filtered topography; and the use now of only one surface scheme (ISBA) (the previous scheme Force-Restore is no longer used).

Changes installed uniquely into the data assimilation component ENKF include: horizontal localization length scale now increasing with height; higher horizontal resolution (now ~66km); higher vertical resolution increased from 58 to 74 levels with the model top remaining at 2 hPa; an increased volume of AMSU radiance observations; and improved observation bias correction coming from the [newer version 3.0.0 of the GDPS](../nwp_gdps/changelog_gdps_en.md).

Changes installed uniquely into the forecast component include: adjustments to how physics tendencies are perturbed for convective precipitation; the physics tendencies perturbations are applied at every level except the very last one; addition of diffusion into the advection procedure; perturbation of the bulk drag coefficient in the orographic blocking scheme; and fine tuning of the adjustment factor alpha of the stochastic kinetic energy backscattering scheme.

ENKF version 3.0.0 results in overall significant positive impacts on the analyses and trial fields of winds and temperature for almost the entire atmospheric column with some degradation in the bias of the zonal wind component at high levels. The geopotential heights error standard deviations are lowered in the troposphere. The biases of geopotential heights and temperature are reduced significantly.

The forecast component of GEPS-3.0.0 brings a major improvement in upper air 16â¬day forecasts in the extra-tropics. There is less spread in the forecast of the new system while the forecasts are better.

The upper air forecast from the Regional Ensemble Prediction System (REPS) will benefit significantly from having better initial and lateral boundary conditions from the GEPS-3.0.0.

The North American Ensemble Forecast System (NAEFS) upper air forecasts will also improve significantly for day 1 to day 10 lead times with the contribution of GEPS-3.0.0.

Hardware improvements coinciding with this implementation will result in some products being ready between 10 to 120 minutes sooner than their present time of production.

A copy of the official note announcing the implementation of these changes along with information on verification work leading up to this implementation [is available at this link](http://dd.weatheroffice.ec.gc.ca/doc/genots/2013/02/08/NOCN03_CWAO_081500___00884).

A technical note with many more details on this change [is also available at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/lib/op_systems/doc_opchanges/technote_geps300_20130213_e.pdf).
