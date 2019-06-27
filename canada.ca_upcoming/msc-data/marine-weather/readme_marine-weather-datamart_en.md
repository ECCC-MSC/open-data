[En Français](readme_marine-weather-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC Open Public Data](../readme_en.md) > Marine weather

# Data of the marine weather forecasts

This page describes the data of the [marine weather](readme_marine-weather_en.md) forecasts available on the MSC Datamart.

The XML files contain the weather forecast, marine weather warnings (warning and watch), ice alerts and the end of season announcement. They are updated two to four times a day, or more often in the case of amendments, marine weather warnings (alert or watch) or ice warnings.

The [Environment and Climate Change Canada's guide to the marine forecast](https://www.canada.ca/en/environment-climate-change/services/general-marine-weather-information/publications/guide-forecasts.html) includes information on the issuing time of forecasts, time period covered by forecast, determination of forecast regions, forecast time period terminology, information included in the forecast, and forecast revision.

__Notes__:

* The marine XML files do not include ice forecast information, but do include [ice alert information](https://www.canada.ca/en/environment-climate-change/services/ice-forecasts-observations/latest-conditions/products-guides/iceberg-bulletin-overview.html#warnings).
http://www.ec.gc.ca/glaces-ice/default.asp?lang=En&n=E568E9D7-1#warnings

* Ice forecast information can be found on the [Environment and Climate Change Canada web site](https://www.canada.ca/en/environment-climate-change/services/ice-forecasts-observations.html) and on the [Canadian Ice Service](https://www.canada.ca/fr/environnement-changement-climatique/services/previsions-observations-glaces/conditions-glaces-plus-recentes.html) web site.

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](.../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](.../../usage-overview/readme_en.md) is also available.

The data is available via the HTTP protocol. It is possible to access it with a standard browser. In this case, we obtain a list of links giving access to a XML file.

* __The marine weather XML files__ are available according to Canadian marine regions, at the following address:

  https://dd.weather.gc.ca/marine_weather/xml/REGION

where:

 __REGION__ : name of the region covered by the forecast.The region name is one of the 8 following values:
    * arctic
    * atlantic
    * great_lakes
    * hudson
    * mackenzie
    * pacific
    * prairies
    * st_lawrence

* [__Tables describing each of the marine weather XML element tags and their associated attributes__](http://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/marine-weather/marine_tags_table_e.csv) are available.

* The __XML schemas__ for marine weather data are found in this directory:

http://dd.weather.gc.ca/marine_weather/schema/

## File name nomenclature 

NOTE: ALL HOURS ARE IN UTC.

The file names have the following nomenclature:

RegionNameCode_L.xml

where:

* __RegionNameCode__ : site code used in the marine region list (see URL below)
* __L__ : single letter indicating the language of the file. Can be either : f (French) or e (English)

Examples of file name:

* m0000001_e.xml - English marine weather XML for area Tuktoyaktuk

* m0000001_f.xml - French marine weather XML for area Tuktoyaktuk

A [__list with location names and RegionNameCodes__](http://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/marine-weather/marine_region_list_en.csv) is available.

## Support

If you have any questions about these data, please contact us at: ec.dps-client.ec@canada.ca

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).

