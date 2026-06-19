[En français](readme_hurricanes-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [Hurricane trajectories](readme_hurricanes_en.md) > Hurricane trajectories on MSC Datamart

# Data of the hurricane trajectories

This page describes the data of the [hurricane trajectories](readme_hurricanes_en.md) available on the MSC Datamart in GeoJSON format when storms of tropical origin threatens or risks to threaten Canadian territory.

Hurricane tracks in the Atlantic region, from the [NOAA National Hurricane Center](https://www.nhc.noaa.gov/) are republished by the [Canadian Hurricane Centre](https://www.canada.ca/en/environment-climate-change/services/hurricane-forecasts-facts/products.html) and are also available in GeoJSON format.

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available via the HTTPS protocol. It is possible to access it with a standard browser. In this case, we obtain a list of links giving access to GeoJSON files.

Data can be found on the MSC Datamart at this address:

* [https://dd.weather.gc.ca/today/hurricanes](https://dd.weather.gc.ca/today/hurricanes)

## File name nomenclature

File naming convention is:

`{YYYYMMDD}T{HHmm}Z_MSC_Hurricane_{NAME}.json`

Where :

* __YYYYMMDD__ : Year, month and day of data transmission
* __T__: Time delimiter according to ISO8601 standards
* __HHmm__ : Hour and minute of data transmission
* __Z__: Time zone (UTC hour)
* __MSC__: Constant character string for Meteorological Service of Canada, the data source
* __Hurricane__ : Constant string indicating the name of the product contained in the files, i.e. hurricane trajectories
* __NAME__ : Constant string indicating the name of the hurricane
* __json__: Constant string indicating that the format is GeoJSON

Ex: `20240708T2100Z_MSC_Hurricane_BERYL.json`

## Support

If you have any questions about this data, please [contact us](https://weather.gc.ca/mainmenu/contact_us_e.html).

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).
