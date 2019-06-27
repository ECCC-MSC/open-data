[En Français](readme_marineweather-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC Open Public Data](../readme_en.md) > Marine weather

# Data of the alphanumerical bulletins 

This page describes the data of the [marine weather](readme_marineweather_en.md).

The XML files are updated 2-4 times daily at a minimum, but can be updated
"as needed" with issuance of forecast amendments, marine weather alerts
(warnings and watches) and Ice alert information.

Environment and Climate Change Canada's guide to the marine forecast includes information on the issuing time of forecasts, time period
covered by forecast, determination of forecast regions, forecast time
period terminology, information included in the forecast, and forecast
revision.

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](.../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](.../../usage-overview/readme_en.md) is also available.

The data is available via the HTTP protocol. It is possible to access it with a standard browser. In this case, we obtain a list of links giving access to a XML file.

The marine weather XML files are available at the following address:

* https://dd.weather.gc.ca/marine_weather/xml/


## Directory and file name nomenclature 

NOTE: ALL HOURS ARE IN UTC.

The marine weather XML files are grouped in a directory tree that is based
on Canadian marine regions.

__1- The directories have the following nomenclature :__

/marine_weather/xml/REGION

where:
* __REGION__ : name of the region covered by the forecast.
The region name is one of the 8 following values:
    * arctic
    * atlantic
    * great_lakes
    * hudson
    * mackenzie
    * pacific
    * prairies
    * st_lawrence

__2- The file names have the following nomenclature :__

RegionNameCode_L.xml

where:
* __RegionNameCode__ : site code used in the marine region list (see URL below)
* __L__ : single letter indicating the language of the file. Can be either :
f (French) or e (English)

Examples of file name:

* m0000001_e.xml - English marine weather XML for area Tuktoyaktuk

* m0000001_f.xml - French marine weather XML for area Tuktoyaktuk

Lists with location names and RegionNameCodes, regrouped according to
various factors, can be found at the following addresses :
* https://dd.weather.gc.ca/marine_weather/docs/region_list_en.csv
* https://dd.weather.gc.ca/marine_weather/docs/region_list_regions_en.csv
* https://dd.weather.gc.ca/marine_weather/docs/region_list_areas_en.csv

## Support

If you have any questions about these data, please contact us at: ec.dps-client.ec@canada.ca

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).

