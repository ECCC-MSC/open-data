[En français](readme_rdps-statpostproc-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC Open Data](../readme_en.md) > [RDPS](readme_rdps_en.md) > RDPS statistical post-processing on MSC Datamart

# Regional Deterministic Prediction System (RDPS) data statistically post-processed in GeoJSON format

Statistical post-processing of forecasts from numerical weather and environmental models, including the [Regional Deterministic Prediction System (RDPS)](readme_rdps_en.md), helps reduce systematic biases and error variance in raw forecasts. This is achieved by establishing optimized statistical relationships between observations recorded at stations and numerical model outputs at nearby grid points.

The "Updatable Model Output Statistics" (**UMOS**) system is a software package developed by Environment and Climate Change Canada that enables this. Relationships are built using the "Model Output Statistics" (MOS) method and multiple linear regression (MLR). After 25 years of dedicated service, **UMOS** will soon be replaced by a more modern software package, **PROGNOS**.

For both systems, the statistically post-processed weather and environmental variables include:

* Air and dew point temperatures at 1.5 meters above the Earth's surface
* Wind speed and direction at 10 meters above the Earth's surface or at anemometer level in the case of a buoy

The absence of statistically post-processed forecasts can be due to the unavailability of a statistical model caused by insufficient observation quality or quantity.

Furthermore, the absence of wind direction forecasts can also be due to predicted wind components being too weak to provide a reliable result. Wind direction and speed forecasts are derived from independent statistical post-processing models.

The geographical region covered by this data includes the territory covered by Canadian meteorological stations and some American buoys.

## Data location 

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available using the HTTPS protocol and resides in a directory that is plainly accessible to a web browser. Visiting that directory with an interactive browser will yield a raw listing of links, each link being a downloadable GeoJSON file.

The data can be accessed at the following URLs: 

* UMOS data: [https://dd.weather.gc.ca/model_gem_regional/stat-post-processing/{HH}/{hhh}/](https://dd.weather.gc.ca/model_gem_regional/stat-post-processing)
* PROGNOS data: [https://dd.weather.gc.ca/model_rdps/stat-post-processing/{HH}/{hhh}/](https://dd.weather.gc.ca/model_rdps/stat-post-processing)

where :

* __HH__: Model run start, in UTC [00, 06, 12, 18]
* __hhh__: Forecast hour [000, 003, 006,..., 084] for UMOS data
* __hhh__: Forecast hour [000, 001, 002,..., 084] for PROGNOS data, according to the observation stations

## Technical specifications

* UMOS and PROGNOS forecasts are offered at observation station locations in North America covered within the following geographical bounding box : 149⁰W, 40⁰N, 42⁰W, 88⁰N
* The datum and geographical projection are respectively: WGS84, latlon.
* Data is bilingual
* Data is in ISO8601 compliant

## Filename nomenclature 

The files have the following nomenclature :

`{YYYYMMDD}T{HH}Z_MSC_RDPS-{PRODUCT}-{METHOD}_{Var}_{LVLTYPE}-{LVL}_PT{hhh}H.json`

where:

* __YYYYMMDD__ : Year, month and day of the beginning of the forecast
* __T__: Time delimiter according to ISO8601 norms
* __HH__ : UTC run time [00, 06, 12, 18]
* __Z__: Time zone (UTC hour)
* __MSC__: Constant string indicating that the data is from the Meteorologcal Service of Canada (MSC)
* __RDPS__: Constant string indicating that data is from Regional Deterministic Prediction System
* __PRODUCT__: Constant string indicating the post-processing product [UMOS, PROGNOS]
* __METHOD__: Constant string indicating the [statistical method used](https://link.springer.com/book/10.1007/978-0-387-84858-7) [MLR for Multiple Linear Regression, LASSO for Least Absolute Shrinkage and Selection Operator, WDLASSO2 for LASSO applied to zonal and meridional winds components]
* __Var__ : Variables included in this file [AirTemp, DewPoint, WindSpeed, WindDir]
* __LVLYPE__: Vertical level type [Sfc for surface level, AGL for Above Ground Level]
* __LVL__: Vertical level value [1.5m, 10m]. This parameter is not used for surface level
* __PT{hhh}H__: Forecast hours based on [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) norms. P, T and H are constant character designating Period, Time and Hour. "hhh" is the forecast hour from 00h to 84h according to the products (evry 3 hours for UMOS and hourly for PROGNOS according to the stations observations)
* __json__ : constant string indicating the GeoJSON format

Filenames examples: 

* 20220128T00Z_MSC_RDPS-UMOS-MLR_AirTemp_AGL-1.5m_PT072H.json
* 20250702T12Z_MSC_RDPS-PROGNOS-MLR_DewPoint_Sfc_PT024H.json
* 20250714T00Z_MSC_RDPS-PROGNOS-LASSO-WindSpeed_AGL-10m_PT006H.json
* 20250714T00Z_MSC_RDPS-PROGNOS-WDLASSO2-WindDir_AGL-10m_PT000H.json

## List of variables

* AirTemp: Surface air dry-bulb temperature (K)
* DewPoint: Surface dew point temperature (K)
* WindSpeed: Surface wind speed (km/h)
* WindDir: Surface wind direction (°)

## Support

If you have any questions about this data, please [contact us](https://weather.gc.ca/mainmenu/contact_us_e.html).

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).




