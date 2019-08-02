[En français](readme_cansips_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > CanSIPS

# Data and Products of the Canadian Seasonal to Inter-annual Prediction System (CanSIPS)

The Canadian Seasonal to Inter-annual Prediction System (CanSIPS) carries out physics calculations to arrive at probabilistic predictions of atmospheric elements from the beginning of a month out to up to 12 months into the future. Atmospheric elements include temperature, precipitation, wind speed and direction and others. This product contains raw numerical results of these calculations. Geographical coverage is global. Data is available on a grid at a horizontal resolution of 2.5 degrees and for a few selected vertical levels. Predictions and corresponding hindcast are made available monthly.

## System description

CanSIPS is a multi-model ensemble (MME) system using two climate models developed by the Canadian Centre for Climate Modelling and Analysis (CCCma). It is a fully coupled atmosphere-ocean-ice-land prediction system relying on the operational data assimilation infrastructure for the initial state of the atmosphere, sea surface temperature and sea ice.

For more information on the system please see :  

[https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/lib/op_systems/doc_opchanges/technote_cansips_20111124_e.pdf](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/lib/op_systems/doc_opchanges/technote_cansips_20111124_e.pdf)

__Models__ :

* CanCM3 and CanCM4 - coupled climate models
* CanAM3 and CanAM4 - atmospheric components
* CanOM4 - ocean component

Atmospheric models CanAM3 and CanAM4 are coupled to the oceanic model CanOM4 in CanCM3 and CanCM4, respectively. 

For a more detailed description of the models please visit this link :

[https://www.canada.ca/en/environment-climate-change/services/climate-change/science-research-data/modeling-projections-analysis/centre-modelling-analysis/models.html](https://www.canada.ca/en/environment-climate-change/services/climate-change/science-research-data/modeling-projections-analysis/centre-modelling-analysis/models.html)

__CanSIPS forecast configuration__ :

Ensemble size for the forecast is 20 members (10 CanCM3 members + 10 CanCM4 members). At the last day of the each month, a 12-month forecast is produced. There are no lagged initial conditions, all the 20 members start on the first of the month and are initialised with different initial conditions originating from separate assimilating coupled model runs. When the ensemble forecasts are finished we construct seasonal mean anomalies with respect to the 30-year hindcasts for each ensemble member. Subsequently we implement deterministic (ensemble mean) and probabilistic (different categories with respect to the ensemble size) approaches to forecast the upcoming seasons.

## Access

### How to access the data

These data are available on the data server services [MSC Datamart](../../msc-datamart/readme_en.md) and the web services [MSC GeoMet](../../msc-geomet/readme_en.md) respectively :

* [GRIB2 data available on the MSC Datamart](readme_cansips-datamart_en.md) 
* [Indices in CSV format available on the MSC Datamart](readme_cansips-datamartcsv_en.md)
* [Data available via geospatial web services](../../msc-geomet/readme_en.md) 

An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is available.

### Licence

The [end-user licence for Environment and Climate Change Canada's data servers](../../licence/readme_en.md) specifies the conditions of use of these data.

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

* [Technical note](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_cansips-v2_20190703_e.pdf)
* [Scientific article](https://journals.ametsoc.org/doi/abs/10.1175/MWR-D-12-00216.1)

## Change log

The chronology of changes to the Canadian Seasonal to Inter-annual Prediction System (CanSIPS) is available [here](changelog_cansips_en.md).
