[In French](readme_ciops_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > CIOPS

# Data and products of the Coastal Ice Ocean Prediction System (CIOPS)

The Coastal Ice Ocean Predicton Systems (CIOPS) provide a 48 hour ocean and ice (CIOPS-E only) forecast four times a day at 1/36° resolution. A pseudo-analysis component is forced at the ocean boundaries by the Regional Ice Ocean Predicton System (RIOPS) forecasts and spectrally nudged to the RIOPS solution in the deep ocean. Fields from the pseudo-analysis are used to initialize the 00Z forecast, whilst the 06, 12 and 18Z forecasts use a restart files saved at hour 6 from the previous forecast. The atmospheric fluxes for both the pseudo-analysis and forecast components are provided by the High Resolution Deterministic Prediction System (HRDPS) blended both spatially and temporally with either the Global Deterministic Prediction System (GDPS for CIOPS-East) or the Regional Deterministic Predicton System (RDPS for CIOPS-West) for areas not covered by the HRDPS.

## Access

### How to access the data 

This data is available on the [MSC Datamart](../../msc-datamart/readme_en.md) data server:

* [CIOPS NetCDF data available on the MSC Datamart](readme_ciops_nemo-datamart_en.md)  

An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is available.

### Licence

The [end-user licence for Environment and Climate Change Canada's data servers](../../licence/readme_en.md) specifies the conditions of use of this data.

### MSC Open Data Service Usage Policy

The [MSC Open Data Service Usage Policy](../../usage-policy/readme_en.md) determines what constitutes an acceptable use of MSC Open Data services and provides users best practices for optimal use.

### Metadata

To come.

## Technical documentation

* [Current version of the CIOPS-East](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_specifications/tech_specifications_CIOPS-EAST_e.pdf)
* [Current version of the CIOPS-West](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_specifications/tech_specifications_CIOPS-WEST_e.pdf)
* [Technical note for CIOPS-East](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_notes/technote_ciops-east_e.pdf)
* [Technical note for CIOPS-West](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_notes/technote_ciops-west_e.pdf)

## Changelog 

The chronology of changes to the CIOPS is available [here](changelog_ciops_en.md).

