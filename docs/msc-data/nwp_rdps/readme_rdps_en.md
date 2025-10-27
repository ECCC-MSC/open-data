[En français](readme_rdps_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > RDPS

# Data and products of the Regional Deterministic Prediction System

The Regional Deterministic Prediction System (RDPS) carries out physics calculations to arrive at deterministic predictions of atmospheric elements from the current day out to 84 hours into the future. Atmospheric elements include temperature, precipitation, cloud cover, wind speed and direction, humidity and others. This product contains raw numerical results of these calculations. Geographical coverage includes Canada and the United States. Data is available at horizontal resolution of about 10 km up to 33 vertical levels. Predictions are performed four times a day.

Note:  The Regional Deterministic Prediction System is now a component of the [Global Deterministic Prediction System (GDPS)](../nwp_gdps/readme_gdps_en.md) at 10 km resolution, over a North American domain.

## Access

### How to access the data

This data is available on the [MSC Datamart](../../msc-datamart/readme_en.md) data server service as well as [MSC GeoMet](../../msc-geomet/readme_en.md):

* [Data available via geospatial web services GeoMet-Weather](../../msc-geomet/readme_en.md)
* [GRIB2 data available on the MSC Datamart](readme_rdps-datamart_en.md)
* [GeoJSON statistically post-processed data on the MSC Datamart](readme_rdps-statpostproc-datamart_en.md)
* [Experimental GRIB2 weather elements on the grid data available on the MSC testing data repository DD-Alpha](readme_rdps-datamart-alpha_en.md)
* [Experimental GRIB2 astronomy products available on the MSC testing data repository DD-Alpha](readme_astro-rdps-datamart-alpha_en.md)

An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is available.

### Licence

The [end-user licence for Environment and Climate Change Canada's data servers](../../licence/readme_en.md) specifies the conditions of use of this data.

### MSC Open Data Service Usage Policy

The [MSC Open Data Service Usage Policy](../../usage-policy/readme_en.md) determines what constitutes an acceptable use of MSC Open Data services and provides users best practices for optimal use.

### Discovery metadata

* The [metadata of the Regional Deterministic Prediction System is available on the Open Government Portal](https://open.canada.ca/data/en/dataset/a9f2828c-0d78-5eb6-a4c7-1fc1219f1e3d).

## Products

List and links to the products available for this dataset :

### Forecast maps

* [4-panel charts](https://meteo.gc.ca/model_forecast/index_e.html)
* [Severe weather prediction products](https://meteo.gc.ca/model_forecast/severe_weather_e.html)

### Aerological analysis maps

* [250hPa: Geopotential height, wind speed](https://meteo.gc.ca/data/analysis/sah_100.gif)
* [500 hPa: Geopotential height, thicknesses 1000-500hPa](https://meteo.gc.ca/data/analysis/sai_100.gif)
* [700 hPa: Geopotential height, temperature, dew point deviation](https://meteo.gc.ca/data/analysis/saj_100.gif)
* [850 hPa: Geopotential height, temperature ](https://meteo.gc.ca/data/analysis/saa_100.gif)

### Aviation products

* [Turbulence and icing](https://meteo.gc.ca/model_forecast/turb_e.html)
* [Documentation - 4-panel aviation package](aviation-package_en.md)
* [Documentation - 4-panel ceiling forecasts](ceiling_en.md)

### Astronomy products

* [Cloud forecast](https://meteo.gc.ca/astro/clds_vis_e.html)
* [Star scintillation prediction](https://meteo.gc.ca/astro/seeing_e.html)
* [Prediction of sky transparency](https://meteo.gc.ca/astro/transparence_e.html)
* [Near-surface forecast](https://meteo.gc.ca/astro/meteo_e.html)

## Technical documentation

* [Current version of the Regional Deterministic Prediction System](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_RDPS_e.pdf)
* [Current version of the statistical post-processing software package of the Regional Deterministic Prediction System](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_PROGNOS_e.pdf)
* [Technical note](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_rdps_e.pdf)
* [Technical note of the statistical post-processing software package of the Regional Deterministic Prediction System](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/not_available.pdf)
* [Diagram of dependencies](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwep-dependency-diagrams/system_RDPS_en.svg)
* [Factsheet associated with the latest innovation cycle](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/fact_sheets/factsheet_rdps_e.pdf)

## Changelog 

The chronology of changes to the Regional Deterministic Prediction System (RDPS) is available [here](changelog_rdps_en.md).
