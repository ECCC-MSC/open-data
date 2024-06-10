[En français](changelog_rdwps_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [RDWPS](readme_rdwps_en.md) > RDWPS Changelog

# Chronology of changes to the Regional Deterministic Wave Prediction System (RDWPS)

## Tuesday June 11, 2024

### Upgrade to Version 4.2.0 of the Regional Deterministic Wave Prediction System (RDWPS) at the Canadian Meteorological Centre

On Tuesday June 11, 2024, starting with the 1200 UTC run, the Meteorological Service of Canada's Canadian Meteorological Centre (CMC) will upgrade the Regional Deterministic Wave Prediction System (RDWPS) to v4.2.0

Significant changes:

* Use of wind forcings from the latest version of the High Resolution Deterministic Prediction System (HRDPS), v7.0.0
* Use of ice concentration forcings from the latest versions of the Water Cycle Prediction Systems (WCPS), v3.3.0 and the Regional Ice-Ocean Prediction System (RIOPS), v2.4.0
* Ocean domains: correct interpolation of wind to model grid
* Great Lakes domains: activate Miche style shallow water limiter

The official note announcing this implementation is available [at this link](https://dd.meteo.gc.ca/doc/genots/2021/11/26/NOCN03_CWAO_262118___xxxxx).

The technical specifications document for RDWPS 4.2.0 is available [at this link](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_specifications/tech_specifications_RDWPS_4.2.0_e.pdf).

## Tuesday June 28, 2022

### Upgrade to Version 4.1.0 of the RDWPS adapted to the New High Performance Computing Infrastructure.

See details [at this link](../changelog_multisystems_en.md).

## Wednesday December 1st, 2021

### Upgrade to Version 4.0.0 of the Regional Deterministic Wave Prediction System (RDWPS) at the Canadian Meteorological Centre

On Wednesday December 1st, 2021, starting with the 1200 UTC run, the Canadian Meteorological Centre (CMC) will upgrade the Regional Deterministic Wave Prediction System (RDWPS) to version 4.0.0.

A brief summary of the innovations included in this upgrade and their impact on performance can be consulted in this document: [RDWPS_4.0.0_innovations](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/fact_sheets/factsheet_rdwps-400_e.pdf). For detailed description of this upgrade, please see the [Technical note](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_rdwps-400_e.pdf).

The major changes of RDWPS in this upgrade can be summarized as follows:

* Use of HRDPS v6.0.0
* Addition of a pseudo-analysis cycle
* Addition of two new domains: Northeast Pacific and Northwest Atlantic
* Retirement of WAM Regional for the Gulf of St. Lawrence

Associated Notes:

* [Official note announcing the implementation](http://dd.weather.gc.ca/doc/genots/2021/11/26/NOCN03_CWAO_262118___50159).
* [Technical note](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_rdwps-400_e.pdf).
* [Technical specifications of RDWPS 4.0.0](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_RDWPS_4.0.0_e.pdf).


## Tuesday January 21, 2020

### Upgrade to Version 3.4.0 of the RDWPS adapted to the New High Performance Computing Infrastructure.

See details [at this link](../changelog_multisystems_en.md)

## Monday March 4, 2019

### Upgrades to the Regional Deterministic Wave Prediction System (RDWPS) at the Canadian Meteorological Centre (CMC)

Effective March 4, 2019, the Canadian Meteorological Centre (CMC) of the Meteorological Service of Canada will update the Regional Deterministic Wave Prediction System (RDWPS) to v3.2.0.

RDWPS v3.2.0 is different from the previous operational system in that the ice analysis used as input for it has been replaced by an ice forecast provided by the Water Cycle Prediction System (WCPS v2.0.0), which was declared operational on March 4, 2019.

A copy of the official note announcing the implementation of these changes is available [at this link](http://dd.meteo.gc.ca/doc/genots/2019/03/05/NOCN03_CWAO_051918___12705).

The technical specifications document for RDWPS 3.2.0 is available [at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_RDWPS_3.2.0_e.pdf).


## Wednesday April 4, 2018

### The new Regional Deterministic Wave Prediction System (RDWPS) is declared operational at the Canadian Meteorological Centre (CMC)

Effective April 4, 2018, the Canadian Meteorological Centre (CMC) of the Meteorological Service of Canada declared operational the new Regional Deterministic Wave Prediction System (RDWPS v3.0.0).

A copy of the official note announcing the implementation of these changes is available [at this link](http://dd.meteo.gc.ca/doc/genots/2018/04/03/NOCN03_CWAO_032022___00001).

A technical note with more details on the RDWPS will be available soon.

The technical specifications document for RDWPS 3.0.0 is available [at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_RDWPS_3.0.0_e.pdf).


## Monday May 7 2012

### The Canadian Meteorological Centre Upgrades its Regional Deterministic Wave Prediction System

On Monday May 07, 2012, beginning with the 1200 UTC model run, the Canadian Meteorological Centre (CMC) implemented a number of changes to its Regional Deterministic Wave Prediction System (RDWPS), to become RDWPS version 2.0. The changes include an upgrade to the wave model, addition of new products into the production suite and modifications to existing ones.

A copy of the official note describing these changes [is available by clicking here](http://dd.weatheroffice.ec.gc.ca/doc/genots/2012/05/07/NOCN03_CWAO_071403___55624).

A technical note with detailed information on this system [is available by clicking here](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/lib/op_systems/doc_opchanges/technote_rdwps_20120524_e.pdf).