[En français](readme_rdwps_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > RDWPS


# Data and Products of the Regional Deterministic Wave Prediction System (RDWPS)

The Regional Deterministic Wave Prediction System (RDWPS) produces wave forecasts out to 48 hours in the future using the third generation spectral wave forecast model WaveWatch III® (WW3). The model is forced by the 10 meters winds from the [High Resolution Deterministic Prediction System (HRDPS)](../nwp_hrdps/readme_hrdps_en.md). Over the Great Lakes, an ice forecast from the [Water Cycle Prediction System of the Great Lakes (WCPS)](../nwp_wcps/readme_wcps_en.md) )  is used by the model to attenuate or suppress wave growth in areas covered by 25% to 75% and more than 75% ice, respectively. Over the ocean, an ice forecast from the [Regional Ice Ocean Prediction System (RIOPS)](../nwp_riops/readme_riops_en.md)  is used: in the Northeast Pacific, waves propagate freely for ice concentrations below 50%, above this threshold there is no propagation; in the Northwest Atlantic the same logic is used as in the Great Lakes. Forecast elements include significant wave height, peak period, partitioned parameters and others. This system includes several domains: Lake Superior, Lake Huron-Michigan, Lake Erie, Lake Ontario, Atlantic North-West and Pacific North-East.

## Access

### How to access the data

This data is available on the [MSC Datamart](../../msc-datamart/readme_en.md) data server service as well as [MSC GeoMet](../../msc-geomet/readme_en.md):

* [GRIB2 data available on the MSC Datamart](readme_rdwps-datamart_en.md) 
* [Data available via geospatial web services GeoMet-Weather](../../msc-geomet/readme_en.md)

An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is available.

### Licence

The [end-user licence for Environment and Climate Change Canada's data servers](../../licence/readme_en.md) specifies the conditions of use of this data.

### MSC Open Data Service Usage Policy

The [MSC Open Data Service Usage Policy](../../usage-policy/readme_en.md) determines what constitutes an acceptable use of MSC Open Data services and provides users best practices for optimal use.

### Discovery metadata

* The [metadata of the Regional Deterministic Wave Prediction System - National is available on the Open Government Portal](https://open.canada.ca/data/en/dataset/9a6594f9-ad0e-4421-ba9d-16338e5a9cbe).
* The [metadata of the Regional Deterministic Wave Prediction System - Lake Erie is available on the Open Government Portal](https://open.canada.ca/data/en/dataset/bf1884e2-cbbb-4a50-ab40-c5b417723d17).
* The [metadata of the Regional Deterministic Wave Prediction System - Lake Huron-Michigan is available on the Open Government Portal](https://open.canada.ca/data/en/dataset/631e570e-59c3-42d7-aa7b-5a4666ab62b5).
* The [metadata of the Regional Deterministic Wave Prediction System - Lake Ontario is available on the Open Government Portal](https://open.canada.ca/data/en/dataset/38414289-4beb-4854-af58-5ab3b66665eb).
* The [metadata of the Regional Deterministic Wave Prediction System - Lake Superior is available on the Open Government Portal](https://open.canada.ca/data/en/dataset/88a5111c-136c-42a7-907f-523ad4365165).

## Products

List and links to the products available for this dataset :

### Forecast maps

* [Maps of wave models](https://weather.gc.ca/model_forecast/wave_e.html)

## Technical documentation

* [Current version of the Regional Deterministic Wave Prediction System](http://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_specifications/tech_specifications_RDWPS_e.pdf)
* [Technical note](http://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_notes/technote_rdwps_e.pdf)
* [Diagram of dependencies](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwep-dependency-diagrams/system_RDWPS_en.svg)
* [Factsheet associated with the latest innovation cycle](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/fact_sheets/factsheet_rdwps_e.pdf)

## Changelog

The chronology of changes to the Regional Deterministic Wave Prediction System (RDWPS) is available [here](changelog_rdwps_en.md).
