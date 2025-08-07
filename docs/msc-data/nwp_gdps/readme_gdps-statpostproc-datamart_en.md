[En français](readme_gdps-statpostproc-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC Open Data](../readme_en.md) > [GDPS](readme_gdps_en.md) > GDPS statistical post-processing on MSC Datamart

# Global Deterministic Prediction System (GDPS) data statistically post-processed in GeoJSON format

Statistical post-processing of forecasts from numerical weather and environmental models, including the [Global Deterministic Prediction System (GDPS)](readme_gdps_en.md), helps reduce systematic biases and error variance in raw forecasts. This is achieved by establishing optimized statistical relationships between observations recorded at stations and numerical model outputs at nearby grid points.

The "Updatable Model Output Statistics" (**UMOS**) system is a software package developed by Environment and Climate Change Canada that enables this. Relationships are built using the "Model Output Statistics" (MOS) method and multiple linear regression (MLR). After 25 years of dedicated service, **UMOS** will soon be replaced by a more modern software package, **PROGNOS**.

For both systems, at present, only the air temperature at 1.5 meters above the Earth's surface is statistically post-processed.

The absence of statistically post-processed forecasts can be due to the unavailability of a statistical model caused by insufficient observation quality or quantity.

The geographical region covered by this data includes the territory covered by Canadian meteorological stations and some American buoys.

## Data location 

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available using the HTTPS protocol and resides in a directory that is plainly accessible to a web browser. Visiting that directory with an interactive browser will yield a raw listing of links, each link being a downloadable GeoJSON file.

The data can be accessed at the following URLs: 

* [https://dd.weather.gc.ca/today/model_gem_global/stat-post-processing/{HH}/{hhh}/](https://dd.weather.gc.ca/today/model_gem_global/stat-post-processing)

where :

* __HH__ : UTC hour of the model run start [00, 12]
* __hhh__ : Forecast lead time [000, 003, 006, ..., 144] for UMOS data
* __hhh__ : Forecast lead time [000, 001, 002, ..., 084, 087, 090, ..., 165, 168] for PROGNOS data according to observation stations

## Technical specifications

* UMOS and PROGNOS forecasts are offered at observation station locations in North America covered within the following geographical boundaries: 149⁰W, 40⁰N, 42⁰W, 88⁰N
* The datum and geographical projection are respectively: WGS84, latlon.
* Data is bilingual
* Data is in ISO8601 compliant

## Filename nomenclature 

The files have the following nomenclature :

`{YYYYMMDD}T{HH}Z_MSC_GDPS-{PRODUCT}-{METHOD}_{Var}_{LVLTYPE}-{LVL}_PT{hhh}H.json`

where:

* __YYYYMMDD__ : Year, month and day of the beginning of the issued forecast
* __T__: Time delimiter according to ISO8601 norms
* __HH__ : Issuing run time in UTC [00, 12]
* __Z__: Time zone (UTC hour)
* __MSC__: Constant string indicating that the data is from the Meteorologcal Service of Canada (MSC)
* __GDPS__: Constant string indicating that data is from Global Deterministic Prediction System
* __PRODUCT__: Constant string indicating the post-processing product [UMOS, PROGNOS]
* __METHOD__: Constant string indicating the statistical method used [MLR for Multiple Linear Regression]
* __Var__ : Variables included in this file [AirTemp]
* __LVLYPE__: Vertical level type [Sfc for surface level, AGL for Above Ground Level]
* __LVL__: Vertical level value [1.5m]. This parameter is not used for surface level
* __PT{hhh}H__: Forecast hours based on [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) norms. P, T and H are constant characters designating Period, Time and Hour. "hhh" is the forecast lead time [000, 003, 006, ..., 144] for UMOS data and [000, 001, 002, ..., 084, 087, 090, ..., 165, 168] for PROGNOS data according to observation stations
* __json__ : constant string indicating the GeoJSON format

Examples of file names: 

* 20220128T00Z_MSC_GDPS-UMOS-MLR_AirTemp_AGL-1.5m_PT072H.json
* 20250703T06Z_MSC_GDPS-PROGNOS-MLR_AirTemp_AGL-1.5m_PT024H.json

## List of variables

* AirTemp: Surface air dry-bulb temperature (K)

## Support

If you have any questions about this data, please [contact us](https://weather.gc.ca/mainmenu/contact_us_e.html).

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).



