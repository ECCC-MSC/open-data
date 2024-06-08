[En français](changelog_reps_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [REPS](readme_reps_en.md) > REPS Changelog

# Chronology of changes to the Regional Ensemble Prediction System (REPS)

## Tuesday June 11, 2024

### Upgrade to Version 5.0.0 of the Regional Ensemble Prediction System (REPS) at the Canadian Meteorological Centre

On Tuesday June 11, 2024, starting with the 1200 UTC run, the Canadian Meteorological Centre (CMC) will upgrade the Regional Ensemble Prediction System (REPS) to version 5.0.0.

Significant changes:
* Boundary conditions coming from new [Global Ensemble Prediction System (GEPS)](../nwp_gdps/readme_geps_en.md) at 25 km resolution.
* Use of a 10km component of the [Global Deterministic Prediction System (GDPS)](../nwp_gdps/readme_gdps_en.md), for initial conditions as a replacement of the Regional Deterministic Prediction System (RDPS).
* Use of the Global Ice-Ocean Prediction System (GIOPS) analyses and modification to the physics configuration.
* Transition to the Smooth LEvel Vertical (SLEVE) coordinate.


A brief summary of the innovations included in this upgrade and their impact on performance can be consulted in [this document](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/fact_sheets/factsheet_reps-500_e.pdf). 

A copy of the official note announcing the implementation of these changes is available at [this link](http://dd.meteo.gc.ca/doc/genots/2024/06/11/NOCN03_CWAO_311455___xxxxx).

A technical note with more details on this system is available [at this link](http://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_reps-500_e.pdf).

The technical specifications document for REPS 5.0.0 is available [at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_REPS_5.0.0_e.pdf) .



## Tuesday June 28, 2022

### Upgrade to Version 4.1.0 of the REPS adapted to the New High Performance Computing Infrastructure.

See details [at this link](../changelog_multisystems_en.md).

## Wednesday December 1st, 2021

### Upgrade to Version 4.0.0 of the Regional Ensemble Prediction System (REPS) at the Canadian Meteorological Centre

On Wednesday December 1st, 2021, starting with the 1200 UTC run, the Canadian Meteorological Centre (CMC) will upgrade the Regional Ensemble Prediction System (REPS) to version 4.0.0.


A brief summary of the innovations included in this upgrade and their impact on performance can be consulted in this document: [REPS_4.0.0_innovations](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/fact_sheets/factsheet_reps-400_e.pdf). For detailed description of this upgrade, please see the [Technical note](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_reps-400_e.pdf).

Associated Notes:

* [Official note announcing the implementation](http://dd.weather.gc.ca/doc/genots/2021/11/26/NOCN03_CWAO_262118___50159).
* [Technical note](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_reps-400_e.pdf).
* [Technical specifications of REPS 4.0.0](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_REPS_4.0.0_e.pdf).


## Tuesday January 21, 2020

### Upgrade to Version 3.1.0 of the REPS adapted to the New High Performance Computing Infrastructure.

See details [at this link](../changelog_multisystems_en.md)

## Wednesday July 3, 2019

### Upgrade to Version 3.0.0 of the Regional Ensemble Prediction System (REPS) at the Canadian Meteorological Centre

On Wednesday, July 3rd, 2019, starting with the 1200 UTC run, the Canadian Meteorological Centre (CMC) of the Meteorological Service of Canada will upgrade the Regional Ensemble Prediction System (REPS) to version 3.0.0.
The changes included in this upgrade are summarized as follows:

* [GEPS v6.0.0](../nwp_geps/changelog_geps_en.md) replaces v5.0.0 as the pilot system.
* Upgrade from GEM v4.8-LTS.16 to GEM v5.0.0. For more informations on GEM-5, please consult [this document](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/GEM5_paper_submitted_JAMES_20190614.pdf).
* Increase in horizontal resolution from 15 to 10 km.
* Increase in the number of vertical levels from 48 to 84.
* Model top raised from 16 hPa to 0.1 hPa.
* Increase from 2 runs per day (00 and 12 UTC) to 4 runs per day (00, 06, 12, and 18 UTC).
* Recentering of ensemble members around the RDPS analysis.
* All 20 REPS members are configured the same as the RDPS.

A copy of the official note announcing the implementation of these changes [is available at this link](http://dd.meteo.gc.ca/doc/genots/2019/06/28/NOCN03_CWAO_281735___13093).

A technical note with more details on this change [is available at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_reps-300_20190703_e.pdf).

The technical specifications document for REPS 3.0.0 [is available at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_REPS_3.0.0_e.pdf).


## Tuesday September 18, 2018

### Upgrade to Version 2.4.0 of the Regional Ensemble Prediction System (REPS) at the Canadian Meteorological Centre

On Tuesday, September 18, 2018, starting with the 1200 UTC run, the Canadian Meteorological Centre (CMC) of the Meteorological Service of Canada will upgrade the Regional Ensemble Prediction System (REPS) to version 2.4.0.
The changes included in this upgrade are summarized as follows:

* The system is now piloted by GEPS 5.0.0 (see [here](../nwp_geps/changelog_geps_en.md) for further details), rather than GEPS 4.3.0.
* The Canadian Global Environmental Multi-scale (GEM) model is upgraded from v4.6 to v4.8.
* The "trapezoidal-cubic" option for the interpolation of the computation of trajectories in the context of semi-lagrangian advection has been activated.

A copy of the official note announcing the implementation of these changes [is available at this link](http://dd.meteo.gc.ca/doc/genots/2018/09/17/NOCN03_CWAO_171325___27325).

A technical note with more details on this change [is available at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_reps-240_20180918_e.pdf).


## Tuesday December 15, 2015

### Upgrade to Version 2.2.0 of the Regional Ensemble Prediction System (REPS) at the Canadian Meteorological Centre

On Tuesday December 15th 2015, starting with the 1200 UTC run, the Meteorological Service of Canada's Canadian Meteorological Centre (CMC) will upgrade the Regional Ensemble Prediction System (REPS) to version 2.2.0.
The only change to REPS is that it is now piloted by GEPS 4.1.1 (see [here](../nwp_geps/changelog_geps_en.md) for further details), rather than by the previous GEPS 4.0.0.

The technical specifications document of the REPS 2.2.0 [is available at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_REPS_2.2.0_e.pdf).


## Wednesday December 4th 2013

### Major Upgrade to the Regional Ensemble Prediction System (REPS) version 2.0.1 at the Canadian Meteorological Centre

On Wednesday December 4th 2013, starting with the 1200 UTC run the Meteorological Service of Canada's Canadian Meteorological Centre (CMC) will upgrade the Regional Ensemble Prediction System (REPS) to version 2.0.1.

In this upgrade, important changes were made to the model dynamic used into the REPS 2.0.1. The new REPS includes a more recent version (from version 4.2.1. to 4.5.1) of the global environmental multi-scale (GEM), model. The horizontal grid spacing for the new system is reduced from 0.3 degre (33 km) to 0.1375 degre (15 km). The time step is reduced from 15 minutes to 7.5 minutes. The number of vertical levels of the new system is increased from 28 to 48 levels.

The configuration of the physics was also upgraded. The main change is the introduction of a physically-based hysteresis effect in the turbulent mixing scheme that improves the forecast of precipitation types.

The new REPS is still making use of the perturbation of the physics tendencies scheme (PTP). However, in the new system the perturbation are not applied to areas where there are convective instabilities and where the vertical velocities are greater than 0.5 m/s. These modifications avoid the generation of unrealistically high precipitation amounts that were occasionally present in the previous REPS.

A copy of the official note announcing the implementation of these changes along with information on verification work leading up to this implementation [is available at this link](http://dd.meteo.gc.ca/doc/genots/2013/12/03/NOCN03_CWAO_032214___00940).

A technical note with many more details on this change [is also available at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/lib/technote_reps201_20131204_e.pdf).


## Thursday September 22 2011

The Canadian Meteorological Centre makes its Regional Ensemble Prediction System (REPS 1.0.0) Operational

On Thursday September 22 2011 starting with the 12UTC run the Canadian Meteorological Centre made fully operational its Regional Ensemble Prediction System (REPS 1.0.0).

Presently, products from the REPS are only available internaly to Environment Canada but plans are underway to also make these products available to external users.

A copy of the official note [is available by clicking here](http://dd.weather.gc.ca/doc/genots/2011/09/26/NOCN03_CWAO_261345_CCA__98421).

Addtional technical information is [available in the technical note by clicking here](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/lib/op_systems/doc_opchanges/technote_reps_20111004_e.pdf).
