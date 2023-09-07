[En français](readme_gdps-statpostproc-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC Open Data](../readme_en.md) > [GDPS](readme_gdps_en.md) > GDPS statistical post-processing on MSC Datamart

# Global Deterministic Prediction System (GDPS) data statistically post-processed in GeoJSON format

Statistical post-processing of weather and environmental forecasts issued by numerical models, including the [Global Deterministic Prediction System (GDPS)](readme_gdps_en.md), reduces systematic bias and error variance of raw numerical forecasts. This is achieved by establishing an optimal relationship between observations recorded at stations and co-located numerical model outputs. The Updatable Model Output Statistics (UMOS) system at Environment Canada carries out this task. The statistical relationships are built using the Model Output Statistics (MOS) method and a multiple linear regression (MLR) technic. The weather and environmental variable being statistically post-processed by UMOS consists of air temperature at approximately 1.5 meters above ground. The absence of a statistically post-processed forecast can be caused by a missing statistical model due to insufficient observation data quality or quantity. Geographical coverage includes weather stations across Canada. Statistically post-processed forecasts are available at the same frequency of emission as the numerical model producing the raw forecasts and at 3-hourly lead times up to 144 hours (6 days) for the GDPS.

## Data location 

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available using the HTTPS protocol and resides in a directory that is plainly accessible to a web browser. Visiting that directory with an interactive browser will yield a raw listing of links, each link being a downloadable GeoJSON file.

The data can be accessed at the following URLs: 

* [https://dd.weather.gc.ca/model_gem_global/stat-post-processing/{HH}/{hhh}/](https://dd.weather.gc.ca/model_gem_global/stat-post-processing)

where :

* __HH__: Model issuing run time, in UTC [00, 12]
* __hhh__: Forecast lead time [000, 003, 006, ..., 144]

A 24-hour history is kept in this directory.

## Technical specifications

* UMOS forecast is offered at observation station locations in North America covered within the following geographical boundaries: 141⁰W, 40⁰N, 42⁰W, 88⁰N
* The datum and geographical projection are respectively: WGS84, latlon.
* Data is bilingual
* Data is in ISO8601 compliant

## Filename nomenclature 

Note : all hours are in UTC.

The files have the following nomenclature :

`{YYYYMMDD}T{HH}Z_MSC_GDPS-{PRODUCT}-{METHOD}_{Var}_{LVLTYPE}-{LVL}_PT{hhh}H.json`

where:

* __YYYYMMDD__ : Year, month and day of the beginning of the issued forecast
* __T__: Time delimiter according to ISO8601 norms
* __HH__ : Issuing run time in UTC [00, 12]
* __Z__: Time zone (UTC hour)
* __MSC__: Constant string indicating that the data is from the Meteorologcal Service of Canada (MSC)
* __GDPS__: Constant string indicating that data is from Global Deterministic Prediction System
* __PRODUCT__: Constant string indicating the post-processing product [UMOS]
* __METHOD__: Constant string indicating the statistical method used [MLR for Multiple Linear Regression]
* __Var__ : Variables included in this file [AirTemp]
* __LVLYPE__: Vertical level type [Sfc for surface level, AGL for Above Ground Level]
* __LVL__: Vertical level value [1.5m]. This parameter is not used for surface level
* __PT{hhh}H__: Forecast hours based on [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) norms. P, T and H are constant characters designating Period, Time and Hour. "hhh" is the forecast lead time [000, 003, 006, ..., 144]
* __json__ : constant string indicating the GeoJSON format

Filename example: 20220128T00Z_MSC_GDPS-UMOS-MLR_AirTemp_AGL-1.5m_PT072H.json

## List of variables

* AirTemp: Surface air dry-bulb temperature (K)

## Support

If you have any questions about this data, please contact us at: [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info.comm.collab.science.gc.ca/).



