[En français](changelog_ohps_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > OHPS Changelog

# Chronology of changes to the Operational Hydrodynamic Prediction system (OHPS)

## Wednesday September 20, 2023

### Operational Hydrodynamic Prediction System (OHPS) 3.3.0 is declared operational at the Canadian Meteorological Centre

Effective September 20, 2023, the Canadian Meteorological Centre (CMC) of Environment and Climate Change Canada declares the Operational Hydrodynamic Prediction System (OHPS v3.3.0) as operational, following its period of experimental status since 2013.

A copy of the official note announcing the implementation of these changes is available [at this link](https://dd.weather.gc.ca/doc/genots/2023/09/19/NOCN03_CWAO_191340___27844).

## Thrusday August 3, 2023

### Upgrade to Version 3.3.0 of the Operational Hydrodynamic Prediction System (OHPS)

Effective August 3, 2023, the Canadian Meteorological Centre (CMC) of Environment and Climate Change Canada updates the Operational Hydrodynamic Prediction system (OHPS) to version v3.3.0.

To prepare for the request of OHPS's operational status, the following two scientific changes are implemented in this version:

* Replacing the discharge-sources DHPS (experimental) by WCPS (operational) for generating forecast discharge boundary conditions for OHPS.
* Replacing the dependencies on both NSRPS-CaLDAS (experimental) and NSRPS-HRDLPS (experimental) by HRDPS (operational) in OHPS' Precipitation-Evaporation module.

A technical note with more details on v3.3.0 of this system is available [at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_shop-330_e.pdf ).

The updated dependency diagram is available [at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwep-dependency-diagrams/system_NSRPS-OHPS_en.svg).

## Tuesday June 28, 2022

### Upgrade to Version 3.1.0 of the OHPS adapted to the New High Performance Computing Infrastructure.

See details [at this link](../changelog_multisystems_en.md).

## Wednesday December 1st, 2021

### Upgrade to Version 3.0.0 of the Operational Hydrodynamic Prediction system (OHPS) at the Canadian Meteorological Centre

Effective Wednesday, December 1st, 2021, the Canadian Meteorological Centre (CMC) will update the Operational Hydrodynamic Prediction system (OHPS) to v3.0.0.

The modifications to OHPS v3.0.0 compared with the previous operational version are as follows:

* New harmonic boundary conditions
* Discharge is now from the Deterministic Hydrological Prediction System (DHPS))
   * Previously was from the Water Cycle Prediction System (WCPS) 
* Bias-correction of the discharge is removed
* Surface temperature now comes from the Canadian Land Data Assimilation System (CaLDAS), rather than the Regional Deterministic Precipitation Analysis (RDPA-CaPA)

The official note announcing this implementation is available [at this location](https://dd.meteo.gc.ca/doc/genots/2021/11/26/NOCN03_CWAO_262118___50159).

## Monday May 13, 2013

### The Canadian Meteorological Centre (CMC) implements version 1.0.0 of the Operational Hydrodynamic Prediction System (OHPS)

On Monday May 13 2013, CMC implemented the Operational Hydrodynamic Prediction System (OHPS) in order to produce a daily analysis of the portion of the St-Lawrence river between Montreal and Trois-Rivieres. Please consult the OHPS page in the CMC product guide [here](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/submenus/shop_e.html) for more information.
