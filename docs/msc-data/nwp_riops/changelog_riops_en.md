[En français](changelog_riops_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [RIOPS](readme_riops_en.md) > RIOPS Changelog

# Chronology of changes to the Regional Ice and Ocean Prediction System (RIOPS)

## Tuesday June 11, 2024

### Upgrade to Version 2.4.0 of the Regional Ice and Ocean Prediction System (RIOPS) at the Canadian Meteorological Centre

On Tuesday June 11, 2024, the Meteorological Service of Canada's Canadian Meteorological Centre (CMC) will upgrade the Regional Ice and Ocean Prediction System (RIOPS) to version 2.4.0.

Significant change:
* CICE Version 6.2 Upgrade 
* Delta-Eddington Radiation Scheme 
* Global Deterministic Prediction System ([GDPS](../nwp_gdps/readme_gdps_en.md)) Atmospheric Forcing 
* Mean Dynamic Topography (MDT) Update 
* Activation of New Altimetry Datasets 

A brief summary of the innovations included in this upgrade and their impact on performance can be consulted in this document: [RIOPS_2.4.0_innovations](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/fact_sheets/factsheet_riops-240_e.pdf).

A copy of the official note announcing the implementation of these changes [is available at this link](http://dd.meteo.gc.ca/doc/genots/2024/06/11/NOCN03_CWAO_262118___xxxxx).

The technical specifications document for RIOPS 2.4.0 is available [at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_RIOPS_2.4.0_e.pdf)

A technical note with more details on this change is available [at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_riops-240_e.pdf).

## Tuesday November 28, 2023

### Upgrade to Version 2.3.1 of the Regional Ice and Ocean Prediction System (RIOPS) at the Canadian Meteorological Centre

On Tuesday November 28, 2023, the Meteorological Service of Canada's Canadian Meteorological Centre (CMC) will upgrade the Regional Ice and Ocean Prediction System (RIOPS) to version 2.3.1.

For this implementation, there are no change for the numerical model or the assimilation system. The only change comes from the “in situ” dataset used in the data assimilation which are now provided by the new component DFO-QC included in Global Ice and Ocean Prediction System (GIOPS) assimilation.

More details about DFO-QC and the impact of using these data in RIOPS could be found in the [technical note for GIOPS version 3.4.1](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_giops-341_e.pdf).

The technical specifications document for RIOPS 2.3.1 is available [at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_RIOPS_2.3.1_e.pdf)

A technical note with more details on this change is available [at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_riops-220_e.pdf).

## Tuesday June 28, 2022

### Upgrade to Version 2.3.0 of the RIOPS adapted to the New High Performance Computing Infrastructure.

See details [at this link](../changelog_multisystems_en.md).

## Wednesday December 1st, 2021

### Upgrade to Version 2.2.0 of the Regional Ice and Ocean Prediction System (RIOPS) at the Canadian Meteorological Centre

On Wednesday December 1st, 2021, the Canadian Meteorological Centre (CMC) will upgrade the Regional Ice and Ocean Prediction System (RIOPS) to version 2.2.0.

The major changes of RIOPS in this upgrade can be summarized as follow:

* Introduction of a new schema for vertical blending
* Bias correction for temperature and salinity profiles - 3DVar
* Reduction of turbulence due to breaking waves
* Increase ice roughness
* New diurnal cycle 
* New monitoring package

A copy of the official note announcing the implementation of these changes [is available at this link](http://dd.meteo.gc.ca/doc/genots/2021/11/26/NOCN03_CWAO_262118___50159).

The technical specifications document for RIOPS 2.2.0 is available [at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_RIOPS_2.2.0_e.pdf).

A technical note with more details on this change is available [at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_riops-220_e.pdf).

## Tuesday January 21, 2020

### Upgrade to Version 2.1.0 of the RIOPS adapted to the New High Performance Computing Infrastructure.

See details [at this link](../changelog_multisystems_en.md)

## Wednesday July 3, 2019

### Implementation of Version 2.0.0 of the Regional Ice and Ocean Prediction System (RIOPS) at the Canadian Meteorological Centre

On Wednesday July 3rd, 2019, the Meteorological Service of Canada's Canadian Meteorological Centre (CMC) will implement the Regional Ice and Ocean Prediction System (RIOPS) to version 2.0.0. With this upgrade RIOPS will also switch status from an experimental to an operational system.

The major changes in this implementation are summarized as follows:

* Addition of an independent oceanic data assimilation component which replaces a spectral nudging technique.
* Extension of the domain to the North Pacific.

A copy of the official note announcing the implementation of these changes is available at [this link](https://dd.meteo.gc.ca/doc/genots/2019/06/28/NOCN03_CWAO_281850___63233).
The technical specifications document of the RIOPS 2.0.0 is available at [this link](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_specifications/tech_specifications_RIOPS_2.0.0_e.pdf).

A technical note with more details on this change is available at [this link](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_notes/technote_riops-200_e.pdf).

## Tuesday June 21st, 2016

### Implementation of Version 1.1 of the Regional Ice and Ocean Prediction System (RIOPS) at the Canadian Meteorological Centre

On Tuesday June 21st, 2016, the Meteorological Service of Canada's Canadian Meteorological Centre (CMC) will implement the Regional Ice and Ocean Prediction System (RIOPS) to version 1.1 with an experimental status.

The major changes in this implementation relative to the pre-existing and experimental Regional Ice Prediction System (RIPS) are summarized as follows:
* Addition of a 3D oceanic component (NEMO-CICE) with tides.
    * Nudging at large spatial scales of the Global Ice-Ocean Prediction System (GIOPS) analyses during the pseudo-analysis step, prior to the forecast step at 00 UTC.
    * The forecast starts at 00 UTC from the pseudo-analysis and inserts the last available ice concentration analysis.
* Addition of AVHRR data to the ice concentration analysis.

A technical note with more details on this change is available at [this link](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_notes/technote_riops-110_e.pdf).