[En français](readme_rdps-statpostproc-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC Open Data](../readme_en.md) > [RDPS](readme_rdps_en.md) > RDPS statistical post-processing on MSC Datamart

# Regional Deterministic Prediction System (RDPS) data statistically post-processed in GeoJSON format

Statistical post-processing of weather and environmental forecasts issued by numerical models, including the [Regional Deterministic Prediction System (RDPS)](../readme_rdps_en.md), reduces systematic biases and error variance of raw forecasts. This is achieved by establishing an optimal relationship between observations recorded at stations and co-located numerical model outputs. The Updatable Model Output Statistics (UMOS) system at Environment and Climate Change Canada carries out this task. The statistical relationships are built using the Model Output Statistics (MOS) method and a multiple linear regression (MLR) technic. The weather and environmental variables being statistically post-processed by UMOS include air temperature and dew point temperature at approximately 1.5 meters above ground as well as wind speed and direction at 10 meters above ground or at the anemometer level in the case of a buoy. The absence of a statistically post-processed forecast can be caused by a missing statistical model due to insufficient observation data quality or quantity. In addition, the absence of a post-processed forecast for wind direction could also be due to weak forecasted wind components preventing the calculation of reliable results. The forecasts of wind speed and direction are produced from independent statstistical post-processing models. Geographical coverage includes weather stations accross Canada and a few American buoys. Statistically post-processed forecasts is available at the same frequency of emission as the numerical model producing the raw forecasts and at 3-hourly lead times for the RDPS.

## Data location 

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available using the HTTPS protocol and resides in a directory that is plainly accessible to a web browser. Visiting that directory with an interactive browser will yield a raw listing of links, each link being a downloadable GeoJSON file.

The data can be accessed at the following URLs: 

* [https://dd.weather.gc.ca/model_gem_regional/stat-post-processing/{HH}/{hhh}/](https://dd.weather.gc.ca/model_gem_regional/stat-post-processing)

where :

* __HH__: Model run start, in UTC [00, 06, 12, 18]
* __hhh__: Forecast hour [000, 003, 006,..., 084]

## Technical specifications

* UMOS forecast is offered at observation station locations in North America covered within the following geographical bounding box : 141⁰W, 40⁰N, 42⁰W, 88⁰N
* The datum and geographical projection are respectively: WGS84, latlon.
* Data is bilingual
* Data is in ISO8601 compliant

## Filename nomenclature 

Note : all hours are in UTC.

The files have the following nomenclature :

`{YYYYMMDD}T{HH}Z_MSC_RDPS-{PRODUCT}-{METHOD}_{Var}_{LVLTYPE}-{LVL}_PT{hhh}H.json`

where:

* __YYYYMMDD__ : Year, month and day of the beginning of the forecast
* __T__: Time delimiter according to ISO8601 norms
* __HH__ : UTC run time [00, 06, 12, 18]
* __Z__: Time zone (UTC hour)
* __MSC__: Constant string indicating that the data is from the Meteorologcal Service of Canada (MSC)
* __RDPS__: Constant string indicating that data is from Regional Deterministic Prediction System
* __PRODUCT__: Constant string indicating the post-processing product [UMOS]
* __METHOD__: Constant string indicating the statistical method used [MLR for Multiple Linear Regression]
* __Var__ : Variables included in this file [AirTemp, Dewpoint, WindSpeed, WindDir]
* __LVLYPE__: Vertical level type [Sfc for surface level, AGL for Above Ground Level]
* __LVL__: Vertical level value [1.5m, 10m]. This parameter is not used for surface level
* __PT{hhh}H__: Forecast hours based on [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) norms. P, T and H are constant character designating Period, Time and Hour. "hhh" is the forecast hour [000, 003, 006, ..., 084]
* __json__ : constant string indicating the GeoJSON format

Filename example: 20220128T00Z_MSC_RDPS-UMOS-MLR_AirTemp_AGL-1.5m_PT072H.json

## List of variables

* AirTemp: Surface air dry-bulb temperature (K)
* Dewpoint: Surface dew point temperature (K)
* WindSpeed: Surface wind speed (km/h)
* WindDir: Surface wind direction (°)

## Support

If you have any questions about this data, please [contact us](https://weather.gc.ca/mainmenu/contact_us_e.html).

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).




