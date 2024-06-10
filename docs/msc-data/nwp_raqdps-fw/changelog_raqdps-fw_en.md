[En français](changelog_raqdps-fw_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [RAQDPS-FW](readme_raqdps-fw_en.md) > Regional Air Quality Deterministic Prediction System Firework Changelog

# Chronology of changes to the Regional Air Quality Deterministic Prediction System Firework (RAQDPS-FW)

## Tuesday June 11, 2024

### The Regional Air Quality Deterministic Prediction System FireWork (RAQSPS-FW) is merged with The Regional Air Quality Deterministic Prediction System (RAQDPS)

On Tuesday June 11, 2024, starting with the 1200 UTC run, the Canadian Meteorological Centre (CMC) of the Meteorological Service of Canada (MSC) will stop running a separate system forecasting air quality with near-real-Time wildfire emissions.  The wildfire emissions are included into the regular Regional Air Quality Deterministic Prediction System (RAQDPS) version 25.


All documentaion regarding Regional Air Quality Deterministic Prediction System (RAQDPS) version 25 [can be found here](../nwp_raqdps/changelog_raqdps_en.md#tuesday-june-11-2024).



## Tuesday June 28, 2022

### Upgrade to Version 24 of the RAQDPS-FW adapted to the New High Performance Computing Infrastructure.

See details [at this link](../changelog_multisystems_en.md).

## Wednesday December 1st, 2021

### Upgrade to the Regional Air Quality Deterministic Prediction System FireWork (RAQSPS-FW) 

On Wednesday December 1st, 2021, starting with the 1200 UTC run, the Canadian Meteorological Centre (CMC) of the Meteorological Service of Canada (MSC) will upgrade the Regional Air Quality Deterministic Prediction System with Near-Real-Time Wildfire Emissions Firework (RAQDPS-FW) from version 22 to version 23.

The changes included in this upgrade are summarized as follows:

* The RAQDPS-FW is now piloted by [RDPS v8.0.0](https://eccc-msc.github.io/open-data/msc-data/nwp_rdps/changelog_rdps_en/), rather than RDPS v7.1.0.
*  New anthropogenic emissions inventories
    * Canada:  From 2013 Air Pollutant Emission Inventory (APEI) to projected 2020 APEI.
    * U.S.:    From 2017 projected National Emissions Inventory to projected 2023 NEI.
    * Mexico:  Ftom 2008 National Emissions Inventory (NEI)	to projected 2023 NEI.
* Improved representation of particle sedimentation
* New meteorological and chemical libraries 
    * Meteorology:  GEM 5.0.2 => GEM 5.1.0
    * Chemistry:    GEM-MACH 3.0.0.2 => GEM-MACH 3.1.0.0
* Canadian Forest Fire Emission Prediction System (CFFEPS) upgraded from version 2.06 to 4 

A brief summary of the innovations included in this upgrade and their impact on performance [can be found in this document](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/fact_sheets/factsheet_raqdps023_e.pdf )

A copy of the official note announcing the implementation of these changes [is available at this link](http://dd.meteo.gc.ca/doc/genots/2021/11/26/NOCN03_CWAO_262118___50159).

The technical specifications document for RAQSPS-FW v23 is available [at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_RAQDPS_023_e.pdf).

A technical note with more details on this change [is available at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_raqdps023fw_e.pdf).


## Wednesday April 1, 2020

## Installation of the FireWork Prediction System for the Summer Wildfire Season of 2020

On Wednesday April 1st, 2020, starting with the 00 UTC run, the Canadian Meteorological Centre (CMC) of the Meteorological Service of Canada (MSC) will reactivate the FireWork prediction system for the summer period of 2020. FireWork is a seasonal modelling system based on the Regional Air Quality Deterministic Prediction System (RAQDPS) which incorporates additional emissions from wildfire events over North America.

For further information, please consult the official note announcing the implementation of FireWork for Summer 2020 [at this link](https://dd.meteo.gc.ca/doc/genots/2020/04/03/NOCN03_CWAO_031510___44016).

A technical note with more details is available [at this link](http://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_notes/technote_raqdpsfw_e.pdf).




## Tuesday January 21, 2020

### Upgrade FireWork version adapted to the New High Performance Computing Infrastructure.

See details [at this link](../changelog_multisystems_en.md)

## Wednesday July 3, 2019

### Upgrade to the Regional Air Quality Deterministic Prediction System FireWork (RAQSPS-FW) 

On Wednesday July 3rd, 2019, starting with the 1200 UTC run, the Canadian Meteorological Centre (CMC) of the Meteorological Service of Canada (MSC) will upgrade the Regional Air Quality Deterministic Prediction System Firework (RAQDPS-FW) from version 20 to version 21.

The changes included in this upgrade are summarized as follows:

* The RAQDPS is now piloted by [RDPS v7.0.0](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/changes_e.html#20190703_rdps_7.0.0), rather than RDPS v6.0.0.
* Upgrade from GEM v4.8-LTS.16 to GEM v5.0.0. For more informations on GEM-5, please consult [this document](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_notes/GEM5_paper_submitted_JAMES_20190614.pdf).
* Improvements to chemistry processing.

A copy of the official note announcing the implementation of these changes in FireWork is [available at this link](http://dd.meteo.gc.ca/doc/genots/2019/06/28/NOCN03_CWAO_281935___12903).

A technical note for FireWork with more details on this change will be available soon.

## Monday April 15, 2019

## Installation of the FireWork Prediction System for the Summer Wildfire Season of 2019

On Monday April 15, 2019, starting with the 00 UTC run, the Canadian Meteorological Centre (CMC) of the Meteorological Service of Canada (MSC) will reactivate the FireWork prediction system for the summer period of 2019. FireWork is a seasonal modelling system based on the Regional Air Quality Deterministic Prediction System (RAQDPS) which incorporates additional emissions from wildfire events over North America.

For further information, please consult the official note announcing the implementation of FireWork for Summer 2019 [at this link](https://dd.meteo.gc.ca/doc/genots/2019/04/15/NOCN03_CWAO_151930___14392).

A technical note with more details is available [at this link](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_notes/technote_raqdps020.2fw_20190415_e.pdf).

## Tuesday September 18, 2018

### Upgrade to the Regional Air Quality Deterministic Prediction System FireWork 

On Tuesday, September 18, 2018, starting with the 1200 UTC run, the Canadian Meteorological Centre (CMC) of the Meteorological Service of Canada (MSC) will upgrade the Regional Air Quality Deterministic Prediction System FireWork, from version 19 to version 20.

The changes included in this upgrade are summarized as follows:

* The meteorological analyses and pilot model are now linked to [RDPS v6.0.0](/../nwp_rdps/changelog_rdps_en.md#tuesday-september-18-2018) rather than RDPS v5.1.0.
* Adoption of the RDPS v6.0.0 configuration, including recycling of key physics variables and the incremental analysis update (IAU) based meteorological initialization.
* Implementation of a new version of the RAQDPS model code (v2.3.1), to improve processing speed and provide increased robustness, as well as improve chemistry (gas-phase dry deposition over snow-covered surfaces and sea-ice).
* Introduction of a new set of input emissions files based on more recent national emissions inventories.

A copy of the official note announcing the implementation of these changes is available [at this link](https://dd.meteo.gc.ca/doc/genots/2018/09/17/NOCN03_CWAO_171403___42412).

A technical note with more details on this change is available [at this link](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_notes/technote_raqdps-v20_20180918_e.pdf).

## Tuesday April 3, 2018

### Installation of the FireWork Prediction System for the Summer Wildfire Season of 2018

On Tuesday April 3, 2018, starting with the 1200 UTC run, the Canadian Meteorological Centre (CMC) of the Meteorological Service of Canada (MSC) will begin execution of the FireWork prediction system for the summer period of 2018. FireWork is a seasonal modelling system based on the Regional Air Quality Deterministic Prediction System (RAQDPS) which incorporates additional emissions from wildfire events over North America.

For further information, please consult the official note announcing the implementation of FireWork for Summer 2018 [at this link](https://dd.meteo.gc.ca/doc/genots/2018/04/03/NOCN03_CWAO_031838___00001).

A technical note with more details on this system is available [at this link](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_notes/technote_raqdps015fw_20160428_e.pdf).

## Wednesday July 3, 2019

### Upgrade to the FireWork Prediction System

On Wednesday July 3rd, 2019, starting with the 1200 UTC run, the Canadian Meteorological Centre (CMC) of the Meteorological Service of Canada (MSC) will upgrade the Regional Air Quality Deterministic Prediction System (RAQDPS), and it's companion system, FireWork, from version 20 to version 21.

The changes included in this upgrade are summarized as follows:
* The RAQDPS is now piloted by RDPS v7.0.0, rather than RDPS v6.0.0.
* Upgrade from GEM v4.8-LTS.16 to GEM v5.0.0. For more informations on GEM-5, please consult this document.
* Improvements to chemistry processing.

A copy of the official note announcing the implementation of these changes in FireWork is available [at this link](https://dd.meteo.gc.ca/doc/genots/2019/06/28/NOCN03_CWAO_281935___12903).

A technical note for FireWork with more details on this change will be available soon.

## Tuesday September 18, 2018

### Upgrade to the FireWork Prediction System

On Tuesday, September 18, 2018, starting with the 1200 UTC run, the Canadian Meteorological Centre (CMC) of the Meteorological Service of Canada (MSC) will upgrade the Regional Air Quality Deterministic Prediction System (RAQDPS), and it's companion system, FireWork, from version 19 to version 20.

The changes included in this upgrade are summarized as follows:
* The meteorological analyses and pilot model are now linked to RDPS v6.0.0 rather than RDPS v5.1.0.
* Adoption of the RDPS v6.0.0 configuration, including recycling of key physics variables and the incremental analysis update (IAU) based meteorological initialization.
* Implementation of a new version of the RAQDPS model code (v2.3.1), to improve processing speed and provide increased robustness, as well as improve chemistry (gas-phase dry deposition over snow-covered surfaces and sea-ice).
* Introduction of a new set of input emissions files based on more recent national emissions inventories.

A copy of the official note announcing the implementation of these changes is available [at this link](https://dd.meteo.gc.ca/doc/genots/2018/09/17/NOCN03_CWAO_171403___42412).

## Wednesday September 7, 2016

### Major Upgrade to the FireWork Prediction System

On Wednesday, September 7th, 2016, starting with the 1200 UTC run, the Canadian Meteorological Centre (CMC) of the Meteorological Service of Canada (MSC) will upgrade the FireWork prediction system. FireWork is a seasonal modelling system based on the Regional Air Quality Deterministic Prediction System (RAQDPS) which incorporates near-real-time biomass burning emissions over North America. It executes during the wildfire season which normally ends towards the end of October.

The changes included in this upgrade are equivalent to those described above for [RAQDPS016](/../nwp_raqdps/changelog_raqdps_en.md).

For further information, please consult the official note announcing the implementation of these changes available [at this link](https://dd.meteo.gc.ca/doc/genots/2016/09/02/NOCN03_CWAO_022112___00754).

## Thursday April 14th, 2016

### Installation of the FireWork Prediction System for the Summer Season of 2016

On Thursday April 14th, 2016, starting with the 1200 UTC run, the Canadian Meteorological Centre (CMC) of the Meteorological Service of Canada (MSC) will begin execution of the FireWork prediction system for the summer period of 2016. FireWork is a seasonal modelling system based on the Regional Air Quality Deterministic Prediction System (RAQDPS) which incorporates additional emissions from wildfire events over North America.

For further information, please consult the official note announcing the implementation of FireWork for summer 2016 [at this link](https://dd.meteo.gc.ca/doc/genots/2016/04/13/NOCN03_CWAO_131900___00844).

A technical note with more details on this change is available [at this link](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_notes/technote_raqdps015fw_20160428_e.pdf).
