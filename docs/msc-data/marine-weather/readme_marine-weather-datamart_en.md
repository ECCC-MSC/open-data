[En français](readme_marine-weather-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [Marine weather](readme_marine-weather_en.md) > Marine weather on MSC Datamart

# Data of the marine weather forecasts

This page describes the data of the [marine weather](readme_marine-weather_en.md) forecasts available on the MSC Datamart.

The XML files contain the weather forecast, marine weather warnings (warning and watch), ice alerts and the end of season announcement. They are updated two to four times a day, or more often in the case of amendments, marine weather warnings (alert or watch) or ice warnings.

The [Environment and Climate Change Canada's guide to the marine forecast](https://www.canada.ca/en/environment-climate-change/services/general-marine-weather-information/publications/guide-forecasts.html) includes information on the issuing time of forecasts, time period covered by forecast, determination of forecast regions, forecast time period terminology, information included in the forecast, and forecast revision.

__Notes__:

* The marine XML files do not include ice forecast information, but do include [ice alert information](https://www.canada.ca/en/environment-climate-change/services/ice-forecasts-observations/latest-conditions/products-guides/iceberg-bulletin-overview.html#warnings).

* Ice forecast information can be found on the [Environment and Climate Change Canada web site](https://www.canada.ca/en/environment-climate-change/services/ice-forecasts-observations.html) and on the [Canadian Ice Service](https://www.canada.ca/fr/environnement-changement-climatique/services/previsions-observations-glaces/conditions-glaces-plus-recentes.html) web site.

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available via the HTTPS protocol. It is possible to access it with a standard browser. In this case, we obtain a list of links giving access to a XML file.

Marine weather XML forecasts, disseminated in dated files (single files) are available according to this hierarchy :

  [https://dd.weather.gc.ca/marine_weather/{DOMAIN}/{HH}](https://dd.weather.gc.ca/marine_weather/)
  
  where:
  
    * __DOMAIN__ : Name of the region covered by the forecast
    * __HH__ : Hour (UTC) of forecast data emission 

  The domain is one of the 8 following values :

   * arctic
   * atlantic
   * great_lakes
   * hudson
   * mackenzie
   * pacific
   * prairies
   * st_lawrence

[__Tables describing each of the marine weather XML element tags and their associated attributes__](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/marine-weather/marine_tags_table_e.csv) are available.

The __XML schemas__ for marine weather data are found in this directory :

https://dd.weather.gc.ca/today/marine_weather/schema/

## File name nomenclature 

The file names have the following nomenclature :

  `{YYYYMMDD}T{HHmmss.sss}Z_MSC_MarineWeather_{SiteCode}_{L}.xml`

  where :

    * __SiteCode__ : Marine region code (see below)
    * __L__ : Letter indicating file language: fr (French) or en (English)

  Examples of file names:

    * 20250219T070026.074Z_MSC_MarineWeather_m0000109_en.xml
    * 20250219T070026.074Z_MSC_MarineWeather_m0000109_fr.xml

A [__list with location names and RegionNameCodes__](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/marine-weather/marine_region_list_en.csv) is available.

## Support

If you have any questions about this data, please [contact us](https://weather.gc.ca/mainmenu/contact_us_e.html).

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).

