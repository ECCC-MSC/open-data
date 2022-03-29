[In French](readme_ciops_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > CIOPS

# Data and products of the Coastal Ice Ocean Prediction System (CIOPS)

The Coastal Ice Ocean Predicton System (CIOPS) provides a 48 hour ocean and ice forecast over different domains (East, West, Salish Sea) four times a day at 1/36° resolution. A pseudo-analysis component is forced at the ocean boundaries by the [Regional Ice Ocean Prediction System (RIOPS)](../nwp_riops/readme_riops_en.md) forecasts and spectrally nudged to the RIOPS solution in the deep ocean. Fields from the pseudo-analysis are used to initialize the 00Z forecast, whilst the 06, 12 and 18Z forecasts use a restart files saved at hour 6 from the previous forecast. The atmospheric fluxes for both the pseudo-analysis and forecast components are provided by the [High Resolution Deterministic Prediction System (HRDPS)](../nwp_hrdps/readme_hrdps_en.md) blended both spatially and temporally with either the [Global Deterministic Prediction System (GDPS)](../nwp_gdps/readme_gdps_en.md) (for CIOPS-East) or the [Regional Deterministic Predicton System (RDPS)](../nwp_rdps/readme_rdps_en.md) (for CIOPS-West) for areas not covered by the HRDPS.

## Access

### How to access the data 

This data is available on the [MSC Datamart](../../msc-datamart/readme_en.md) data server:

* [NetCDF data available on the MSC Datamart](readme_ciops-datamart_en.md)  

An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is available.

### Licence

The [end-user licence for Environment and Climate Change Canada's data servers](../../licence/readme_en.md) specifies the conditions of use of this data.

### MSC Open Data Service Usage Policy

The [MSC Open Data Service Usage Policy](../../usage-policy/readme_en.md) determines what constitutes an acceptable use of MSC Open Data services and provides users best practices for optimal use.

### Metadata

To come.

## Technical documentation

* [Current version of the Coastal Ice Ocean Prediction System over the East domain (CIOPS-East)](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_specifications/tech_specifications_CIOPS-EAST_e.pdf)
* [Current version of the Coastal Ice Ocean Prediction System over the West domain (CIOPS-West)](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_specifications/tech_specifications_CIOPS-WEST_e.pdf)
* [Technical note for CIOPS-East](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_notes/technote_ciops-east_e.pdf)
* [Technical note for CIOPS-West](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_notes/technote_ciops-west_e.pdf)

## Changelog 

The chronology of changes to the CIOPS is available [here](changelog_ciops_en.md).
