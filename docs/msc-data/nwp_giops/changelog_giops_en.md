[En français](changelog_giops_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [GIOPS](readme_giops_en.md) > GIOPS Changelog

# Chronology of changes to the Global Ice and Ocean Prediction System (GIOPS)

## Tuesday June 11, 2024

### Upgrade to Version 3.5.0 of the Global Ice and Ocean Prediction System (GIOPS) at the Canadian Meteorological Centre

On Tuesday June 11, 2024, the Meteorological Service of Canada's Canadian Meteorological Centre (CMC) will upgrade the Global Ice and Ocean Prediction System (GIOPS) to version 3.5.0.

Significant changes:

* Updated from CICE version 4.0 to 6.2
* Introduced new features such as the Delta-Eddington radiation scheme

A brief summary of the innovations included in this upgrade and their impact on performance can be consulted in [this document](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/fact_sheets/factsheet_giops-350_e.pdf).

A copy of the official note announcing the implementation of these changes is available [at this link](http://dd.meteo.gc.ca/doc/genots/2024/06/11/NOCN03_CWAO_262118___xxxxx).

The technical specifications document for GIOPS 3.5.0 is available [at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_GIOPS_3.5.0_e.pdf).

A technical note with more details on this change [at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_giops-350_e.pdf).

## Tuesday November 28, 2023

### Upgrade to Version 3.4.1 of the Global Ice and Ocean Prediction System (GIOPS) at the Canadian Meteorological Centre

On Tuesday November 28, 2023, the Meteorological Service of Canada's Canadian Meteorological Centre (CMC) will upgrade the Global Ice and Ocean Prediction System (GIOPS) to version 3.4.1.

The only change included in this version is the addition of a quality control component for in situ observations used in data assimilation.

A copy of the official note announcing the implementation of this change is available [at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_giops-341_e.pdf).

The technical specifications document for GIOPS 3.4.1 is available [at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_GIOPS_3.4.1_e.pdf).

## Tuesday June 28, 2022

### Upgrade to Version 3.4.0 of the GIOPS adapted to the New High Performance Computing Infrastructure.

See details [at this link](../changelog_multisystems_en.md).

## Wednesday December 1st, 2021

### Upgrade to Version 3.3.0 of the Global Ice and Ocean Prediction System (GIOPS) at the Canadian Meteorological Centre

On Wednesday December 1st, 2021, the Meteorological Service of Canada's Canadian Meteorological Centre (CMC) will upgrade the Global Ice and Ocean Prediction System (GIOPS) to version 3.3.0.

The major changes of GIOPS in this upgrade can be summarized as follows:

* Inclusion of a diurnal cycle
* Ice strength parameter updated
* Ice roughness adjusted to fit GEM model value
* Atmospheric forcing taken from the assimilation run instead of the forecast run
* New monitoring system


A copy of the official note announcing the implementation of these changes [is available at this link](http://dd.meteo.gc.ca/doc/genots/2021/11/26/NOCN03_CWAO_262118___50159).

The technical specifications document for GIOPS 3.3.0 [is available at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_GIOPS_3.3.0_e.pdf).

A technical note with more details on this change [is available at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_giops-330_e.pdf).

## Tuesday January 21, 2020

### Upgrade to Version 3.2.1 of GIOPS adapted to the New High Performance Computing Infrastructure.

See details [at this link](../changelog_multisystems_en.md)

## Wednesday July 3, 2019

### Upgrade to Version 3.0.0 of the Global Ice and Ocean Prediction System (GIOPS) at the Canadian Meteorological Centre

On Wednesday July 3rd, 2019, the Meteorological Service of Canada's Canadian Meteorological Centre (CMC) will upgrade the Global Ice and Ocean Prediction System (GIOPS) to version 3.0.0.
The major changes of GIOPS in this upgrade are in the forecast component.

* Update to SAM2 (Système d'Assimilation Mercator).
* New sea-surface temperature and sea-ice analyses at 0.1 deg resolution (from 0.2 deg resolution).


A copy of the official note announcing the implementation of these changes [is available at this link](http://dd.meteo.gc.ca/doc/genots/2019/06/28/NOCN03_CWAO_281844___55878).

The technical specifications document of the GIOPS 3.0.0 [is available at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_GIOPS_3.0.0_e.pdf).

A technical note with more details on this change [is available at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_giops-300_e.pdf).


## Wednesday November 1, 2017

### Upgrade to Version 2.3 of the Global Ice and Ocean Prediction System (GIOPS) at the Canadian Meteorological Centre

On Wednesday November 1st, 2017, the Meteorological Service of Canada's Canadian Meteorological Centre (CMC) will upgrade the Global Ice and Ocean Prediction System (GIOPS) to version 2.3.
The major changes of GIOPS in this upgrade are in the forecast component.

* Introduction of two-way coupling between the forecasts of GIOPS and GDPS. This coupling allows two-way interactions between the atmospheric model and the ice-ocean model, such that the evolution of surface marine conditions affects the atmosphere in the GDPS, which in turn affects the GIOPS oceanic forecast fields.

No significant modifications were made to the assimilation component of GIOPS in this upgrade.

The official announcement for the implementation of these changes is included in the GENOT issued for [GDPS 6.0.0](../nwp_gdps/changelog_gdps_en.md).

A technical note with more details on this change [is available at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_giops-230_e.pdf).


## Tuesday June 21st, 2016

### Upgrade to Version 2.1 of the Global Ice and Ocean Prediction System (GIOPS) at the Canadian Meteorological Centre

On Tuesday June 21st, 2016, the Meteorological Service of Canada's Canadian Meteorological Centre (CMC) will upgrade the Global Ice and Ocean Prediction System (GIOPS) to version 2.1.
The major changes in the data assimilation component of GIOPS included in this upgrade are summarized as follows:

* New assimilation source code based on Mercator-Océan’s 2015 version of the Système d’Assimilation Mercator (SAM).
    * Introduction of the 4D Incremental Analysis Update (4D-IAU) approach.
    * Various small modifications to analysis kernel.
* Improved Mean Dynamic Topography (MDT).
* Use of bogus observations in key regions such as under sea ice.
* Refinements in the use of operational CMC SST and sea ice analyses.

No significant modifications were made to the forecast component of GIOPS 2.1.

A copy of the official note announcing the implementation of these changes [is available at this link](http://dd.meteo.gc.ca/doc/genots/2016/06/21/NOCN03_CWAO_211410___00536).

A technical note with more details on this change [is available at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_giops-210_e.pdf).


## Thursday August 20, 2015

### The Canadian Meteorological Centre declared GIOPS version 1.1.1 operational

On August 20, 2015 the Canadian Meteorological Centre (CMC) declared operational the Global Ice Ocean Prediction System (GIOPS) version 1.1.1.

A copy of the official note announcing this change [is available by clicking here](http://dd.weatheroffice.ec.gc.ca/doc/genots/2015/08/20/NOCN03_CWAO_201145___00738).

The technical note of GIOPS 1.1.1 with detailed information on this system [is available at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/lib/technote_giops-111_e.pdf).

A product manual containing a description of GIOPS outputs [is also available at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/lib/product_manual_giops-111_e.pdf).





