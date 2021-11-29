[En français](changelog_rdpa_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [RDPA](readme_rdpa_en.md) > RDPA Changelog

# Chronology of changes to the Regional Deterministic Precipitation Analysis system (CaPA-RDPA)

## Wednesday December 1st, 2021

### Upgrade to version 5.2.0 of the Regional Deterministic Precipitation Analysis System (CaPA-RDPA) at the Canadian Meteorological Centre (CMC)

On Wednesday, December 1st, 2021, the Canadian Meteorological Centre (CMC) of the Meteorological Service of Canada (MSC) will upgrade its Regional Deterministic Precipitation Analysis systems (CaPA-RDPA (10km)) to version 5.2.0.

The changes included in this upgrade are summarized as follows :

* [RDPS v8.0.0](../nwp_hrdps/changelog_rdps_en.md) now provides the trial field instead of RDPS v7.1.0
* Addition of 14 Canadian S-band radars
* Assimilation of observations from the Ontario Ministry of Natural Resources (MNR) network
* Updates to the static quality control masks for 8 radars
* Enlargement of the grid to cover the same domain as the [RDPS](../nwp_rdps)

The official note announcing this implementation is available [at this location](https://dd.meteo.gc.ca/doc/genots/2021/11/29/NOCN03_CWAO_xxxx).

A technical note with more details on these changes is available [at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_capa_rdpa-520_e.pdf).

The technical specifications document for RDPA v5.2.0 is available [at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_RDPA_5.2.0_e.pdf).

## Wednesday June 9, 2021

### Upgrade to version 5.0.0 of the Regional Deterministic Precipitation Analysis System (CaPA-RDPA) at the Canadian Meteorological Centre (CMC)

On Wednesday, June 9, 2021, starting with the 1200 UTC run, the Canadian Meteorological Centre (CMC) of the Meteorological Service of Canada (MSC) will upgrade its Regional Deterministic Precipitation Analysis systems (CaPA-RDPA (10km)) to version 5.0.0.

The changes included in this upgrade are summarized as follows :

* Assimilation of three new precipitation observation networks:
     * Manitoba Agriculture (MBAG),
     * Grand River Conservation Authority (GRCA),
     * Toronto River Conservation Authority (TRCA).
* Changes in the radar composite:
     * 5 Canadian S-band radars replacing the corresponding obsolete C-band radars. 
     * 29 additional U.S. S-band radars.
* Assimilation of the “Integrated Multi-SatellitE Retrievals for GPM” (IMERG) satellite data in the final analysis. 

A copy of the official note announcing this implementation is available at this location: [CaPA-RDPA official announcement](https://dd.meteo.gc.ca/doc/genots/2021/06/08/NOCN03_CWAO_081408___31851)

A technical note with more details on these changes is available at this link: [CaPA-RDPA technical note](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_capa_rdpa-500_e.pdf)

## Tuesday January 21, 2020

### Upgrade to Version 4.7.0 of the CaPA-RDPA adapted to the New High Performance Computing Infrastructure.

See details [at this link](../changelog_multisystems_en.md)

## Wednesday July 3, 2019

### Upgrade to version 4.6.0 of the Regional Deterministic Precipitation Analysis system (CaPA-RDPA) at the Canadian Meteorological Centre (CMC)

On Wednesday July 3rd 2019, starting with the 1200 UTC run, the Canadian Meteorological Centre (CMC) of the Meteorological Service of Canada (MSC) will upgrade the Regional Deterministic Precipication Analysis system (CaPA-RDPA) to version 4.6.0.

Changes are summarized as follows:

* [RDPS v7.0.0](../nwp_rdps/changelog_rdps_en.md) now provides the trial field instead of RDPS v6.0.0.
* The lead times 6 and 12 hours for the total precipitation forecast (PR) will be used instead of 0 and 6 hours as in the previous version.

A copy of the official note announcing the implementation of these changes [is available at this link](http://dd.meteo.gc.ca/doc/genots/2019/07/03/NOCN03_CWAO_031225___18175).


## Tuesday September 18, 2018

### Upgrade to version 4.5.0 of the Regional Deterministic Precipitation Analysis System (CaPA-RDPA) at the Canadian Meteorological Centre (CMC)

On Tuesday, September 18, 2018, starting with the 1200 UTC run, the Canadian Meteorological Centre (CMC) of the Meteorological Service of Canada (MSC) will upgrade its Regional Deterministic Precipitation Analysis systems (CaPA-RDPA (10km)) to version 4.5.0.

The changes included in this upgrade are summarized as follows :

* The trial fields for these precipitaion analyses are generated from the new version of the system implemented on September 18, 2018:
    * CaPA-RDPA now builds its trial fields from [RDPS v6.0.0](../nwp_rdps/changelog_rdps_en.md)
* Assimilation of the observations from the CoCoRaHS network. (CaPA-RDPA)
* New 24h analysis valid at 06h00 UTC in line with the climatological day. (CaPA-RDPA)
* CaPA-RDPA v4.5.0 will be using the 0 and 6 hour lead times of the total precipitation field instead of the 6 and 12 hour. This is made possible because the RDPS v6.0.0 can now generate precipitation right from the beginning of the integration.

A copy of the official note announcing this implementation is available at this location:

* [CaPA-RDPA official announcement](http://dd.meteo.gc.ca/doc/genots/2018/09/17/NOCN03_CWAO_171415___18584)

A technical note with more details on these changes is available at this link:

* [CaPA-RDPA technical note](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_capa_rdpa-450_e.pdf)


## Wednesday November 9, 2016

### Upgrade to the Regional Deterministic Precipitation Analysis system (CaPA-RDPA) at the Canadian Meteorological Centre (CMC)

On Wednesday November 9th 2016, starting with the 1200 UTC run the Meteorological Service of Canada's Canadian Meteorological Centre (CMC) will upgrade the Regional Deterministic Precipitation Analysis System (CaPA-RDPA) by replacing CaPA-RDPA 3.2.0 by version 4.0.0. This new version assimilates precipitation observations provided by two networks of stations newly available at CMC. Pseudo-observations of 0 mm inferred from the American METAR network are added to the dataset submitted to CaPA system. Finally, 33 American weather radars are added to the composite of quantitative precipitation estimates (QPE) which is also assimilated by the system. All these modifications allow producing a better precipitation analysis.
A copy of the official note announcing the implementation of these changes [is available at this link](http://dd.meteo.gc.ca/doc/genots/2016/11/09/NOCN03_CWAO_091420___00557).

A technical note with more details on this change [is available at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/lib/technote_capa-400_20161109_e.pdf).


## Tuesday December 15, 2015

### Upgrade to the Regional Deterministic Precipitation Analysis (RDPA (CaPA)) version 3.2.0 at the Canadian Meteorological Centre (CMC)

On Tuesday December 15th 2015, starting with the 1200 UTC run the Meteorological Service of Canada's Canadian Meteorological Centre (CMC) will upgrade the Regional Deterministic Precipitation Analysis (RDPA (CaPA)) by  replacing CaPA-RDPA 3.1.0 by version 3.2.0. This version will solve two minor problems: The first of which is related to the processing of precipitation reports and the second which affects the GRIB2 encoding procedure by adding a mask to represent well the No-Data regions.
A copy of the official note announcing the implementation of these changes [is available at this link](http://dd.meteo.gc.ca/doc/genots/2015/12/10/NOCN03_CWAO_102100___00779).

An information leaflet on this change [is available at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/lib/capa_information_leaflet_20141118_e.pdf).


## Wednesday June 03, 2015

### Upgrade to the Regional Deterministic Precipitation Analysis (RDPA (CaPA)) version 3.1.0 at the Canadian Meteorological Centre (CMC)

On Wednesday June 03th 2015, starting with the 1200 UTC run the Meteorological Service of Canada's Canadian Meteorological Centre (CMC) will upgrade the Regional Deterministic Precipitation Analysis (RDPA (CaPA)) by  replacing CaPA-RDPA 3.0.0 by version 3.1.0. This version will lead mainly  to the assimilation of a higher number of solid precipitation observations.
A copy of the official note announcing the implementation of these changes [is available at this link](http://dd.meteo.gc.ca/doc/genots/2015/06/03/NOCN03_CWAO_031900___00790).

An information leaflet on this change [is available at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/lib/capa_information_leaflet_20141118_e.pdf).


## Tuesday November 18th, 2014

### Major Upgrade to the Regional Deterministic Precipitation Analysis (RDPA (CaPA)) version 3.0.0 at the Canadian Meteorological Centre

On Tuesday November 18th 2014, starting with the 1200 UTC run the Meteorological Service of Canada's Canadian Meteorological Centre (CMC) will upgrade the Regional Deterministic Precipitation Analysis (RDPA (CaPA)) to version 3.0.0. Here are the major changes:

* This version will assimilate an additional source of important information, the quantitative precipitation estimates (QPE) provided by the Canadian weather radar.
* The Regional Deterministic Prediction System (RDPS) which will provide the required trial field to the CaPA system is also updated to RDPS 4.0.0.
* The the number of analysis produced daily is increased from 9 to 10.

A copy of the official note announcing the implementation of these changes [is available at this link](http://dd.meteo.gc.ca/doc/genots/2014/11/14/NOCN03_CWAO_141831___01258).

An information leaflet on this change [is available at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/lib/capa_information_leaflet_20141118_e.pdf).


## August 20 2013

### Version 2.4 of RDPA (CaPA) installed in operations


## Wednesday October 3 2012

### The Canadian Meteorological Centre Upgrades the RDPA (CaPA) system to version 2.3.0

On Wednesday October 3 2012, starting with the 1200 UTC run, the Canadian Meteorological Centre (CMC) will implement version 2.3.0 of the regional deterministic precipitation analysis. This upgrade is done concurrently with the upgrade to the Regional Deterministic Prediction System version 3.0.0 which will now povide a higher resolution trial field to the precipitation analysis system. For details on the [RDPS upgrade please refer to the information at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/changes_e.html#20121003_rdps).

In addition to the introduction of the higher resolution which is fairly influential on the analysis results, several significant improvements are made to the system and these changes are described in the announcement and technical note avaialble below.

A copy of the official note describing these changes [is available by clicking here](http://dd.weatheroffice.ec.gc.ca/doc/genots/2012/10/02/NOCN03_CWAO_022152___00156).

A technical note with more details of these changes [is available at this link here](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/lib/op_systems/doc_opchanges/technote_rdpa_20121018_e.pdf).







