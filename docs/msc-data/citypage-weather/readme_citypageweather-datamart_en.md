[En français](readme_citypageweather-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [Weather forecast files by city](readme_citypageweather_en.md) > Weather forecast files by city on MSC Datamart

# Weather forecast data by city in XML format

This page describes the XML data of the [weather forecasts by city](readme_citypageweather_en.md) available in the MSC Datamart.

The XML files are updated hourly at a minimum, but can be updated earlier with issue of special weather warnings, watches and amendments.

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available via the HTTP protocol. It is possible to access it with a standard browser. In this case, we obtain a list of links giving access to a XML file.

* The weather forecast data by city are available according to this hierarchy :

  [https://dd.weather.gc.ca/citypage_weather/xml/{XX}](https://dd.weather.gc.ca/citypage_weather/xml)
  
  where __XX__ is a 2 letter provincial or territorial code indicating the area covered by the forecasts. 

  The code is one of the 13 following values :

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
  
* The high elevation forecasts, for seasonal text bulletin forecasts issued only for British Columbia, are available at the following address :
   
   [https://dd.weather.gc.ca/citypage_weather/xml/HEF](https://dd.weather.gc.ca/citypage_weather/xml/HEF)
   
## File name nomenclature 

NOTE: ALL HOURS ARE IN UTC.

The file names have the following nomenclature :

SiteNameCode_L.xml

where:

* SiteNameCode: code corresponding to the site codes used in the city site list 
* L: single letter indicating the language of the file. Can be either: f
(French) or e (English)

Examples of filenames :

* s0000001_e.xml - English citypage weather XML for Athabasca.
* s0000001_f.xml - French citypage weather XML for Athabasca.

A [list with location names and SiteNameCodes](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/citypage-weather/site_list_en.geojson) is available in GeoJSON format.

## Tags, XML schemas and icons

* A table [describing each of the city page weather XML element tags and their associated attributes](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/citypage-weather/citypage_tags_table_e.csv) is available.

* The XML schemas for citypage weather data are found in this directory :

  [https://dd.weather.gc.ca/citypage_weather/schema/](https://dd.weather.gc.ca/citypage_weather/schema/)

* City page weather XML files contain __coded__ current conditions and forecast conditions. These codes are used to determine the icon displayed on the weather office web site's city pages. Tables describing the meteorological conditions for each code are available at:
    * [Current weather conditions](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/citypage-weather/current_conditions_icon_code_descriptions_e.csv)
    * [Forecast weather conditions](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/citypage-weather/forecast_conditions_icon_code_descriptions_e.csv)

## Support

If you have any questions about these data, please contact us at : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).





