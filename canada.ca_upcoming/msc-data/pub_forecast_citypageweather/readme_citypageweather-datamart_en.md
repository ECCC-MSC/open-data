[En Français](readme_citypageweather-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC Open Public Data](../readme_en.md) > Weather forecast files by city

# XML weather forecast data by city

This page describes the XML data of the [weather forecasts by city](readme_citypageweather_en.md).

The XML files are updated hourly at a minimum, but can be updated earlier
with issue of special weather warnings, watches and amendments.


## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](.../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](.../../usage-overview/readme_en.md) is also available.


The data is available via the HTTP protocol. It is possible to access it with a standard browser. In this case, we obtain a list of links giving access to a XML file.

The data can be accessed at the following address:

* https://dd.weather.gc.ca/citypage_weather/xml/

## File name nomenclature 

NOTE: ALL HOURS ARE IN UTC.

The citypage weather XML files are grouped in a directory tree that is based on
province,territory, or high elevation forecast.

1- The directories have the following nomenclature:

/citypage_weather/xml/XX

where:

* __XX__ : 2 letter provincial or territorial code indicating the area
covered by the observations. 
The code is one of the 13 following values:

* AB (Alberta)
* BC (British Columbia)
* MB (Manitoba)
* NB (New Brunswick)
* NL (Newfoundland and Labrador)
* NS (Nova Scotia)
* NT (Northwest Territories)
* NU (Nunavut)
* ON (Ontario)
* PE (Prince Edward Island)
* QC (Québec)
* SK (Saskatchewan)
* YT (Yukon)

In addition, /citypage_weather/xml/HEF contains all high elevation
forecasts. This is a seasonal text bulletin forecast issued for British
Columbia only.

2- The file names have the following nomenclature:

SiteNameCode_L.xml

where:

* __SiteNameCode__ : code corresponding to the site codes used in the city site
list (see URL below)
* __L__ : single letter indicating the language of the file. Can be either: f
(French) or e (English)

Examples of file name:
* s0000001_e.xml - English citypage weather XML for Athabasca
* s0000001_f.xml - French citypage weather XML for Athabasca

Lists with location names and and SiteNameCodes, regrouped according to
various factors, can be found at the following addresses:
* [Site codes](site_list_en.csv)
* [Provinces list](site_list_provinces_en.csv)
* [Towns names](site_list_towns_en.csv)

## Tags, XML schemas and icons

Tables [describing each of the city page weather XML element tags and their
associated attributes](tags_table_e.csv).

The XML schemas for citypage weather data are found in this directory:
https://dd.weather.gc.ca/citypage_weather/schema/

City page weather XML files contain CODED current conditions and forecast
conditions. These codes are used to determine the icon displayed on the
weather office web site's city pages. Tables describing the meteorological
conditions for each code are available at:
* [Current weather conditions](current_conditions_icon_code_descriptions_e.csv)
* [Forecast weather conditions](forecast_conditions_icon_code_descriptions_e.csv)

## Support

If you have any questions about these data, please contact us at: ec.dps-client.ec@canada.ca

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).





