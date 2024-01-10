[En français](readme_cansips_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > CanSIPS

# Data and Products of the Canadian Seasonal to Inter-annual Prediction System (CanSIPS)

The Canadian Seasonal to Inter-annual Prediction System (CanSIPS) carries out physics calculations to arrive at probabilistic predictions of atmospheric elements from the beginning of a month out to up to 12 months into the future, resulting in seasonal forecasts. Atmospheric elements include temperature, precipitation, wind speed and direction and others. This product contains raw numerical results of these calculations. Geographical coverage is global. Data is available on a grid at a horizontal resolution of 2.5 degrees and 1 degree and for a few selected vertical levels. In addition, forecast probabilities for below, near, and above normal temperature and precipitation are available at both resolutions. Predictions and corresponding hindcast are made available monthly.

## Access

### How to access the data

This data is available on the [MSC GeoMet](../../msc-geomet/readme_en.md) web service as well as [MSC Datamart](../../msc-datamart/readme_en.md) data server service:

* [Data available via the GeoMet-Weather geospatial web services](readme_cansips-geomet_en.md)
* [Data available on the GeoMet-OGC-API geospatial web services](https://api.weather.gc.ca/):
    * [CanSIPS - members at 250 km](https://api.weather.gc.ca/collections/weather:cansips:250km:forecast:members)
* [Members and products data in GRIB2 available on the MSC Datamart](readme_cansips-datamart_en.md)
* [Indices in CSV format available on the MSC Datamart](readme_cansips-datamartcsv_en.md)

An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is available.

### Licence

The [end-user licence for Environment and Climate Change Canada's data servers](../../licence/readme_en.md) specifies the conditions of use of this data.

### MSC Open Data Service Usage Policy

The [MSC Open Data Service Usage Policy](../../usage-policy/readme_en.md) determines what constitutes an acceptable use of MSC Open Data services and provides users best practices for optimal use.

### Metadata

The [metadata of the Canadian Seasonal to Inter-annual Prediction System are available on the Open Government Portal](https://open.canada.ca/data/en/dataset/922781a9-bfef-56b9-a438-493ada629d47).

## Products

List and links to the products available for this dataset :

### Deterministic forecast maps

* [Temperature deterministic forecasts](https://weather.gc.ca/saisons/det_e.html)
* [Precipitation deterministic forecasts](https://weather.gc.ca/saisons/det_e.html)
* [Current temperature deterministic forecasts](https://weather.gc.ca/saisons/image_e.html?img=sfe1t_s&bc=det)
* [Current precipitation deterministic forecasts](https://weather.gc.ca/saisons/image_e.html?img=sfe1p_s&bc=det)
* [Temperature deterministic forecasts issued at the beginning of the previous month](https://weather.gc.ca/saisons/image_e.html?img=sfe1tm1_s&bc=det)
* [Precipitation deterministic forecasts issued at the beginning of the previous month](https://weather.gc.ca/saisons/image_e.html?img=sfe1pm1_s&bc=det)
* [Temperature deterministic forecasts issued two months ago](https://weather.gc.ca/saisons/image_e.html?img=sfe1tm2_s&bc=det)
* [Precipitation deterministic forecasts issued two months ago](https://weather.gc.ca/saisons/image_e.html?img=sfe1pm2_s&bc=det)

### Probabilistic forecasts maps

* [Temperature and Precipitation Probabilistic Forecasts](https://weather.gc.ca/saisons/prob_e.html)

### Seasonal forecast

* [Skill of the Deterministic Forecast System](https://weather.gc.ca/saisons/skill_e.html)
* [Verification of Past Forecasts](https://weather.gc.ca/saisons/ver_e.html)
* [Climatology of Temperature and Precipitation](https://weather.gc.ca/saisons/clim_e.html)

### Sea Surface Temperature Anomalies, Ice and Snow Cover

* [Surface analysis](https://weather.gc.ca/saisons/sea-snow_e.html)
* [Surface analysis - Daily](https://weather.gc.ca/saisons/image_e.html?id=daily&img=2019061000_054_G6_global_I_SEASON_tm@lg@sd_000&bc=sea)
* [Surface analysis - 1-Year animation](https://weather.gc.ca/saisons/animation_e.html?id=year&bc=sea)
* [Surface analysis - 30-Day Average](https://weather.gc.ca/saisons/image_e.html?id=average&img=2019061000_054_G6_global_I_SEASON_avg@tm@lg@sd@720_000&bc=sea)
* [Surface analysis - 30-Day animation](https://weather.gc.ca/saisons/animation_e.html?id=month&bc=sea)

## Technical documentation

* [Technical note](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_cansips_e.pdf)
* [Scientific article](https://journals.ametsoc.org/doi/abs/10.1175/MWR-D-12-00216.1)
* [Diagram of dependencies](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwep-dependency-diagrams/system_CanSIPS_en.svg)

## Changelog

The chronology of changes to the Canadian Seasonal to Inter-annual Prediction System (CanSIPS) is available [here](changelog_cansips_en.md).
