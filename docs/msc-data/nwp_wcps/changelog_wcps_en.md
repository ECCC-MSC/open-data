[En français](changelog_wcps_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [WCPS](readme_wcps_en.md) > WCPS Changelog

# Chronology of changes to the Water Cycle Prediction System (WCPS)

## Thursday February 24th, 2022

### Upgrade to Version 3.1.0 of the Water Cycle Prediction System (WCPS) at the Canadian Meteorological Centre

Effective Thursday, February 24th, 2022, the Canadian Meteorological Centre (CMC) will update the Water Cycle Prediction System (WCPS) to v3.1.0.

The modifications to WCPS v3.1.0 compared with the previous operational version are as follows:

* For the pseudo-analysis/forecast components:
    * Ice loading over Great Lakes is correctly set up in the pseudo-analysis
    * River connectors between Lake Huron and Lake St-Claire have been revised to correct for some of unaccounted inter-lake flow
    * Regions of artificially enhanced mixing have been revised in order to better mix water in front of some lake outlets
    * Larger regions of data assimilation of bogus (zero) ice concentration have been set up to avoid numerical instability at lake outlet (which also relates to the embedded ice—and loading option) due to artificial ice pileups.
* For the river component:
    * No change

For more information, please consult the technical specifications document for WCPS v3.0.0 available [at this link](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_specifications/tech_specifications_WCPS_3.1.0_e.pdf).

A technical note with more details on this change is available [at this link](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_notes/technote_wcps-310_e.pdf).
## Wednesday December 1st, 2021

### Upgrade to Version 3.0.0 of the Water Cycle Prediction System (WCPS) at the Canadian Meteorological Centre

Effective Wednesday, December 1st, 2021, the Canadian Meteorological Centre (CMC) will update the Water Cycle Prediction System (WCPS) to v3.0.0.

The modifications to WCPS v3.0.0 compared with the previous operational version are as follows:

* [RDPS v8.0.0](../nwp_rdps/changelog_rdps_en.md) replaces v7.1.0 as the pilot system
* New larger domain covering the Gulf of St. Lawrence (as well as the Great Lakes)
* For the pseudo-analysis/forecast components:
    * Increased resolution from 2km/5km (interior/coastlines) to 1km/2km
    * Ice loading over Great Lakes
    * Atmospheric pressure gradient forcing (inverse barometric effect for storm-surges)
* For the hydrological component: 
    * New observation stations of river discharge: Quebec, United States Geologicial Survey (USGS) 
    * Upstream propagation of information derived from observations of river discharge 
    * New climatological fields of drainage
    * Implementation of the Dynamically Zoned Target Release (DZTR) model to represent management rules of individual regulated reservoirs 
    * A new numerical solver in WATROUTE

The official note announcing this implementation is available [at this location](https://dd.meteo.gc.ca/doc/genots/2021/11/26/NOCN03_CWAO_262118___50159).

For more information, please consult the technical specifications document for WCPS v3.0.0 available [at this link](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_specifications/tech_specifications_WCPS_3.0.0_e.pdf).

A technical note with more details on this change is available [at this link](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_notes/technote_wcps-300_e.pdf).

## Tuesday January 21, 2020

### Upgrade to Version 2.2.1 of WCPS adapted to the New High Performance Computing Infrastructure.

See details [at this link](../changelog_multisystems_en.md)

## Wednesday July 3, 2019

### Upgrade to Version 2.1.0 of the Water Cycle Prediction System (WCPS) at the Canadian Meteorological Centre

Effective Wednesday July 3rd, 2019, the Canadian Meteorological Centre (CMC) will update the Water Cycle Prediction System (WCPS) to v2.1.0.

The modifications to WCPS v2.1.0 compared with the previous operational version are as follows:

* [RDPS v7.0.0](../nwp_rdps/changelog_rdps_en.md) replaces v6.0.0 as the pilot system.

For more information, please consult the technical specifications document for WCPS v2.1.0 available [at this link](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_specifications/tech_specifications_WCPS_2.1.0_e.pdf).

A technical note with more details on this change is available [at this link](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_notes/technote_wcps-210_e.pdf).

## Monday March 4, 2019

### New Water Cycle Prediction System (WCPS) declared operational at the Canadian Meteorological Centre

On Monday March 4th 2019, the Meteorological Service of Canada's Canadian Meteorological Centre (CMC) declared operational the Water Cycle Prediction System (WCPS v2.0.0) after having run in experimental mode for almost 3 years.

A copy of the official note announcing this important implementation is available [at this link](http://dd.meteo.gc.ca/doc/genots/2019/03/04/NOCN03_CWAO_041525___40141).

A technical note with more details on this system is available [at this link](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_notes/technote_wcps-200_20190304_e.pdf).

The technical specifications document for WCPS 2.0.0 is available [at this link](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_specifications/tech_specifications_WCPS_2.0.0_e.pdf).

