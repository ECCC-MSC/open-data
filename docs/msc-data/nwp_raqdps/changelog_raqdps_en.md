[En français](changelog_raqdps_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > RAQDPS Changelog

# Chronology of changes to the Regional Air Quality Deterministic Prediction System (RAQDPS)

## Tuesday June 28, 2022

### Upgrade to Version 24 of the RAQDPS adapted to the New High Performance Computing Infrastructure.

See details [at this link](../changelog_multisystems_en.md).

## Wednesday December 1st, 2021

### Upgrade to the Regional Air Quality Deterministic Prediction System (RAQDPS) 

On Wednesday December 1st, 2021, starting with the 1200 UTC run, the Canadian Meteorological Centre (CMC) will upgrade the Regional Air Quality Deterministic Prediction System (RAQDPS) from version 22 to version 23.

The changes included in this upgrade are summarized as follows:

* The RAQDPS is now piloted by [RDPS v8.0.0](https://eccc-msc.github.io/open-data/msc-data/nwp_rdps/changelog_rdps_en/), rather than RDPS v7.1.0.
*  New anthropogenic emissions inventories
    * Canada:  From 2013 Air Pollutant Emission Inventory (APEI) to projected 2020 APEI.
    * U.S.:    From 2017 projected National Emissions Inventory to projected 2023 NEI.
    * Mexico:  From 2008 National Emissions Inventory (NEI)	to projected 2023 NEI.
* Improved representation of particle sedimentation
* New meteorological and chemical libraries 
    * Meteorology:  GEM 5.0.2 => GEM 5.1.0
    * Chemistry:    GEM-MACH 3.0.0.2 => GEM-MACH 3.1.0.0

A brief summary of the innovations included in this upgrade and their impact on performance [can be found in this document](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/fact_sheets/factsheet_raqdps023_e.pdf )

A copy of the official note announcing the implementation of these changes [is available at this link](http://dd.meteo.gc.ca/doc/genots/2021/11/26/NOCN03_CWAO_262118___50159).

The technical specifications document for RAQDPS 23 [is available at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_RAQDPS_023_e.pdf).

A technical note with more details on this change [is available at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_raqdps023_e.pdf).


## Tuesday January 21, 2020

### Upgrade to Version 22.0.0 of the RAQDPS adapted to the New High Performance Computing Infrastructure.

See details [at this link](../changelog_multisystems_en.md)

## Wednesday July 3, 2019

### Upgrade to the Regional Air Quality Deterministic Prediction System (RAQDPS) and FireWork Prediction System

On Wednesday July 3rd, 2019, starting with the 1200 UTC run, the Canadian Meteorological Centre (CMC) of the Meteorological Service of Canada (MSC) will upgrade the Regional Air Quality Deterministic Prediction System (RAQDPS), and it's companion system, FireWork, from version 20 to version 21.

The changes included in this upgrade are summarized as follows:

* The RAQDPS is now piloted by [RDPS v7.0.0](/../nwp_rdps/changelog_rdps_en.md#wednesday-july-3-2019), rather than RDPS v6.0.0.
* Upgrade from GEM v4.8-LTS.16 to GEM v5.0.0.  For more informations on GEM-5, please consult [this document](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_notes/GEM5_paper_submitted_JAMES_20190614.pdf).
* Improvements to chemistry processing.
A copy of the official note announcing the implementation of these changes in RAQDPS is available [at this link](https://dd.meteo.gc.ca/doc/genots/2019/06/28/NOCN03_CWAO_281933___34219).

A copy of the official note announcing the implementation of these changes in FireWork is available [at this link](https://dd.meteo.gc.ca/doc/genots/2019/06/28/NOCN03_CWAO_281935___12903).

A technical note for RAQDPS with more details on this change is available [at this link](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_notes/technote_raqdps-021_20190703_e.pdf).

A technical note for FireWork with more details on this change will be available soon.

## Tuesday September 18, 2018

### Upgrade to the Regional Air Quality Deterministic Prediction System (RAQDPS) and FireWork Prediction System

On Tuesday, September 18, 2018, starting with the 1200 UTC run, the Canadian Meteorological Centre (CMC) of the Meteorological Service of Canada (MSC) will upgrade the Regional Air Quality Deterministic Prediction System (RAQDPS), and it's companion system, FireWork, from version 19 to version 20.

The changes included in this upgrade are summarized as follows:

* The meteorological analyses and pilot model are now linked to [RDPS v6.0.0](/../nwp_rdps/changelog_rdps_en.md#tuesday-september-18-2018) rather than RDPS v5.1.0.
* Adoption of the RDPS v6.0.0 configuration, including recycling of key physics variables and the incremental analysis update (IAU) based meteorological initialization.
* Implementation of a new version of the RAQDPS model code (v2.3.1), to improve processing speed and provide increased robustness, as well as improve chemistry (gas-phase dry deposition over snow-covered surfaces and sea-ice).
* Introduction of a new set of input emissions files based on more recent national emissions inventories.

A copy of the official note announcing the implementation of these changes is available [at this link](https://dd.meteo.gc.ca/doc/genots/2018/09/17/NOCN03_CWAO_171403___42412).

A technical note with more details on this change is available [at this link](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_notes/technote_raqdps-v20_20180918_e.pdf).

## Wednesday September 7, 2016

### Major Upgrade to the Regional Air Quality Deterministic Prediction System (RAQDPS)

On Wednesday, September 7th, 2016, starting with the 1200 UTC run, the Canadian Meteorological Centre (CMC) of the Meteorological Service of Canada (MSC) will upgrade the Regional Air Quality Deterministic Prediction System (RAQDPS) from version 015 to version 016.

The changes included in this upgrade are summarized as follows:

* The version of GEM is upgraded from a modified v4.6.2 to v4.8.0.

* The meteorological analyses and pilot model are now linked to RDPS 5.0.0 rather than RDPS 4.2.0.

* The grid is rotated to correspond to the new RDPS 5.0.0 grid (see [description of changes](/../nwp_rdps/changelog_rdps_en.md#wednesday-september-7-2016)).

* An important change is made to the use of the Monin-Obukov parameter.

* Other minor bug fixes.

A copy of the official note announcing the implementation of these changes is available [at this link](https://dd.meteo.gc.ca/doc/genots/2016/09/02/NOCN03_CWAO_022109___00871).

A technical note with more details on these changes will be forthcoming on this page.

## Thursday April 7th, 2016

### Major Upgrade to the Regional Air Quality Deterministic Prediction System (RAQDPS)

On Thursday April 7th, 2016, starting with the 1200 UTC run, the Canadian Meteorological Centre (CMC) of the Meteorological Service of Canada (MSC) will upgrade the Regional Air Quality Deterministic Prediction System (RAQDPS) from version 013 (previously 1.5.4) to version 015. This update includes the following changes:

* Slight change to the model grid size, though horizontal grid spacing (10 km) and grid orientation remain unchanged.

* The GEM model employed by the RAQDPS changes from version 3.3.8.2 to 4.6.2.

* New chemical lateral boundary conditions.

* Updates to the chemistry module, including two important bug fixes.

A copy of the official note announcing the implementation of these changes is available [at this link](https://dd.meteo.gc.ca/doc/genots/2016/04/05/NOCN03_CWAO_051925___00885).

A technical note with more details on these changes will be forthcoming on this page.

## Thursday June 11, 2015

### Upgrade to the Regional Air Quality Deterministic Prediction System (RAQDPS) at the Canadian Meteorological Centre (CMC)

On Thursday, June 11 2015, the Canadian Meteorological Centre implemented a new emissions data set for the operational Regional Air Quality Deterministic Prediction System (RAQDPS). The new emissions set is based on the 2010 Canadian Inventory/2011 USA Inventory, updating from the 2006 Canadian Inventory/2005 USA Inventory.

A copy of the official note announcing the implementation of these changes is available [at this link](https://dd.meteo.gc.ca/doc/genots/2015/06/10/NOCN03_CWAO_101245___00612).

More technical/scientific details about this system is available [at this link](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/lib/op_systems/doc_opchanges/Technical_Note_GEM-MACH10_v1.5.3+SET2.1.1_Emissions_9Nov2015.pdf).

## Tuesday November 18th 2014

### Minor Upgrade to the Regional Air Quality Deterministic Prediction System (RAQDPS) version 1.5.3 at the Canadian Meteorological Centre

On Tuesday November 18th 2014, starting with the 1200 UTC run the Meteorological Service of Canada's Canadian Meteorological Centre (CMC) will upgrade the Regional Air Quality Deterministic Prediction System (RAQDPS). The version of the system is changed from 1.5.2 to 1.5.3. The update include the following changes:

1. The system now feeds from the Regional Deterministic Prediction System (RDPS) version 4.0.0

2. The GEM model employed by the RAQDPS changes from version 3.3.8.1 to 3.3.8.2.

## Tuesday February 26, 2013

### Update to the Regional Air Quality Deterministic Prediction System (RAQDPS - version 1.5.1) at the Canadian Meteorological Centre

On Tuesday, February 26, 2013, starting with the 1200 UTC run, the Canadian Meteorological Centre (CMC) will implement version 1.5.1 of the Regional Air Quality Deterministic Prediction System (RAQDPS). This version contains three bug fixes in the chemistry component which bring significant improvements to the operational air quality forecast system.

During the summer of 2012, three bugs were discovered in the RAQDPS, all of which had been present since operational implementation in 2009. The bugs mainly impacted wet removal of chemical species by convective precipitation (both rain-out and below-cloud scavenging); and vertical mixing particularly in stable atmospheric conditions.

RAQDPS-1.5.1 has been tested extensively over the summer and winter of 2012. Objective evaluation scores indicate an improvement in RAQDPS-1.5.1 forecasts when compared to those of version 1.5.0 for the three main pollutants: ozone (O3), fine particulate matter (PM2.5), and nitrogen dioxide (NO2). The most significant improvement with RAQDPS-1.5.1 is observed for winter PM2.5 concentrations, especially for the daily maximum values. The new system represents better the observed values with an important reduction of the peak daily concentration in cases where the RAQDPS had over-forecast the PM2.5.

Categorical scores such as: percentage correct, critical success index, and false alarm ratio show an improvement with RAQDPS-1.5.1 in both summer and winter seasons for all three pollutants: O3, NO2 and PM2.5.

For approximately 90% of stations, UMOS-AQ performs similarly during both cold and warm seasons when connected to RAQDPS-1.5.0 and RAQDPS-1.5.1. For the majority of the remaining stations, UMOS-AQ performance is improved with RAQDPS-1.5.1.

There will be no changes to product availability as a result of this implementation.

A copy of the official note describing these changes and the verification work leading up to this implementation is available [here](https://dd.weather.gc.ca/doc/genots/2013/02/26/NOCN03_CWAO_262210___00308).

A copy of the technical note with more details on this change is available [at this link](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/lib/op_systems/doc_opchanges/technote_raqdps_20130226_e.pdf).

## Wednesday October 3 2012

### The Canadian Meteorological Centre Upgrades the Regional Air Quality Deterministic Prediction System (RAQDPS) to version 1.5

On Wednesday October 3 2012, starting with the 1200 UTC run, the Canadian Meteorological Centre (CMC) will implement version 1.5.0 of the Regional Air Quality Deterministic Prediction System (RAQDPS). This version of RAQDPS replaces version 1.4.6 which was also formerly known as GEM-MACH15 which had been in service since November 2009.

Improvements to the air quality forecast system are provided as a result of changes in grid resolution (from 15 to 10 km) and to the vertical grid spacing, an updated version of the GEM model, and an improved set of emissions files.

Please note that this update is made necessary as a result of major upgrades to the Regional Deterministic Prediction System (RDPS) which provides initial and lateral boundary conditions to the RAQDPS. For details on the RDPS upgrade please refer to the information [at this link](/../nwp_rdps/changelog_rdps_en.md).

Products from this system are expected to be available a few minutes later than they were previously, due to the slightly longer execution time caused by the model's higher resolution.

A copy of the official note describing these changes is available [at this link here](https://dd.weather.gc.ca/doc/genots/2012/10/02/NOCN03_CWAO_022002___00095).

A technical note with details on changes including version 1.5.0 and 1.5.1 is available [at this link here](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/lib/op_systems/doc_opchanges/technote_raqdps_20121003_e.pdf).

## Thursday December 22, 2011

### The Canadian Meteorological Centre implements a correction for GEM-MACH15

Starting with the 12 UTC run of December 22 2011, an updated binary was installed in the GEM-MACH15 system to better process humidity and cloud information in the very upper levels of the model's atmosphere.

With this correction the GEM-MACH15 system is now versiuon 1.4.5.
