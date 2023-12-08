[En français](readme_hrdps-north_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > HRDPS-North

# Data and Products of the High Resolution Deterministic Prediction System North

The High Resolution Deterministic Prediction System North (HRDPS-North) is an experimental forecast system based on a limited-area (LAM) configuration of the Global Environmental Multiscale model (GEM). It covers the entire Arctic basin and Hudson Bay. The horizontal grid spacing is approximately 3 km with 2250 x 1850 grid points and 62 vertical levels. The lowest momentum level is at an altitude of approximately 40 m. The HRDPS-North is piloted by ECCC’s Global Deterministic Prediction System (GDPS), which provides initial and lateral boundary conditions for the atmospheric fields. The initial hydrometeor fields are recycled from the 12h forecast of the previous HRDPS-North integration. The ocean-ice surface fields for sea ice and temperature are provided by the Regional Ice Ocean Prediction System (RIOPS). The HRDPS-North runs on a rotated lat-lon grid twice per day and is initialized at 00 and 12 UTC respectively with 48h integration.

As part of a modernization plan of the Meteorological Service of Canada (MSC), coherent weather elements on the grid ("WEonG"), merging raw model outputs and post-processed with various diagnostic approaches, are also available to serve the different forecasting programs (public, marine, aviation, air quality, etc.).  Hourly concepts are produced from different algorithms using outputs from the pan-Canadian HRDPS. These data are also available on the lat-lon rotated grid. 

## Access

### How to access the data

This data are available on the data server services [MSC Datamart](../../msc-datamart/readme_en.md) and the web services [MSC GeoMet](../../msc-geomet/readme_en.md) respectively:

* [GRIB2 data available on the MSC Datamart](readme_hrdps-north-datamart_en.md) 
* [Data available via geospatial web services GeoMet-Weather](../../msc-geomet/readme_en.md)

An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is available.

### Licence

The [end-user licence for Environment and Climate Change Canada's data servers](../../licence/readme_en.md) specifies the conditions of use of this data.

### MSC Open Data Service Usage Policy

The [MSC Open Data Service Usage Policy](../../usage-policy/readme_en.md) determines what constitutes an acceptable use of MSC Open Data services and provides users best practices for optimal use.

### Metadata

* To come
* The [metadata of the Weather Elements on Grid based on the High Resolution Deterministic Prediction System is available on the Open Government Portal](https://open.canada.ca/data/en/dataset/9eaf8b65-a734-432e-925c-7fbe8fc65670).

## Technical documentation

* [Current version of the High Resolution Deterministic Prediction System North](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_HRDPS-NORTH_e.pdf)
* [Diagram of dependencies](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwep-dependency-diagrams/system_HRDPS-N_en.svg)
* [Technical Note](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_hrdps-north_e.pdf)
* [Weather elements on the grid (WEonG) technical Note](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_weong-hrdps_e.pdf)

## Changelog

The chronology of changes to the High Resolution Deterministic Prediction System (HRDPS) is available [here](changelog_hrdps-north_en.md).

