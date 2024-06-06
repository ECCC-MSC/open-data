[En français](changelog_hrdps-north_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [HRDPS-North](readme_hrdps-north_en.md) > HRDPS-North Changelog

# Chronology of changes to the High Resolution Deterministic Prediction System North (HRDPS-North)

## Tuesday June 11, 2024

### Upgrade to Version 2.1.0 of the High Resolution Deterministic Prediction System North (HRDPS-North) at the Canadian Meteorological Centre

On Tuesday June 11st, 2024, starting with the 1200 UTC run, the Canadian Meteorological Centre (CMC) will upgrade the High Resolution Deterministic Prediction System North (HRDPS-North) to version 2.1.0.


Significant change:

* Upgraded to GEM version 5.2.1, enhancing atmospheric physics and improving model performance. 
* Bourgouin approach for surface precipitation phase partitioning.  
* Improved initial and boundary conditions sourced from the upgraded [10-km GDPS](../nwp_gdps/readme_gdps_en.md).  
* Updated ocean-ice initial conditions from the Regional Ice-Ocean Prediction System (RIOPS), providing more accurate sea-ice data. 
* Implemented the SLEVE vertical coordinate system.

A brief summary of the innovations included in this upgrade and their impact on performance can be consulted in this document: [HRDPS-North_2.1.0_innovations](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/fact_sheets/factsheet_hrdps-north-210_e.pdf).


The official note announcing the implementation of these changes is available [at this link](http://dd.meteo.gc.ca/doc/genots/2024/06/11/NOCN03_CWAO_262118___xxxxx).

A technical note with more details on HRDPS-North 2.1.0 is available [at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_hrdps-north-210_e.pdf).

The technical specifications document for HRDPS-North 2.1.0 is available [at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_HRDPS-NORTH_2.1.0_e.pdf).



## Wednesday August 30, 2023

### Upgrade to Version 2.0.0 of the High Resolution Deterministic Prediction System North (HRDPS-N) at the Canadian Meteorological Centre

On Wednesday, August 30, 2023, starting with the 1200 UTC run, the Canadian Meteorological Centre (CMC) will upgrade the High Resolution Deterministic Prediction System North (HRDPS-N) to version 2.0.0.

The major changes included in this upgrade are summarized as follows:

* Fields calculated on a much large domain
* Initial and lateral boundary conditions for the atmosphere from the latest operational version of the Global Deterministic Prediction System (GDPS) whose details are available [at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_GDPS_8.0.0_e.pdf) 
* Oceanic initial conditions are provided by the Regional Ice Ocean Prediction System (RIOPS) whose details are available [at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_RIOPS_2.2.0_e.pdf)

The official note announcing the implementation of these changes is available [at this link](https://dd.weather.gc.ca/doc/genots/2023/08/29/NOCN03_CWAO_292016___46915).

A technical note with more details on the HRDPS-N 2.0.0 is available [at this link](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_notes/technote_hrdps-north-200_e.pdf).

The technical specifications document for the HRDPS-N 2.0.0 is available [at this link](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_specifications/tech_specifications_HRDPS-NORTH_2.0.0_e.pdf).

## Tuesday June 28, 2022

### Upgrade to Version 1.2.0 of the HRDPS-N adapted to the New High Performance Computing Infrastructure.

See details [at this link](../changelog_multisystems_en.md).

## Wednesday December 1st, 2021

### Upgrade to Version 1.0.0 of the High Resolution Deterministic Prediction System North (HRDPS-N) at the Canadian Meteorological Centre

On Wednesday December 1st, 2021, starting with the 1200 UTC run, the Canadian Meteorological Centre (CMC) will retire the Canadian Arctic Prediction System ([CAPS](../nwp_caps/readme_caps_en.md)) and replace it with the High Resolution Deterministic Prediction System North (HRDPS-N) version 1.0.0.

The changes included in this upgrade are summarized as follows :

* Remove the ice-ocean coupling (CAPS was coupled).
* Migration to GEM version 5.1 with retro-physic.
* Model configuration similar to HRDPS-National.
* New geophysical fields.
* New version of the RDPS pilot model, [version 8.0.0](../nwp_rdps/changelog_rdps_en.md#wednesday-december-1st-2021).


The official note announcing the implementation of these changes is available [at this link](http://dd.meteo.gc.ca/doc/genots/2021/11/26/NOCN03_CWAO_262118___50159).

A technical note with more details on HRDPS-North 1.0.0 is available [at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_hrdps-north-100_e.pdf).

The technical specifications document for HRDPS-North 1.0.0 is available [at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_HRDPS-NORTH_1.0.0_e.pdf).

