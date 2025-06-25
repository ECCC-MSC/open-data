[En français](readme_citypageweather-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [Weather forecast files by city](readme_citypageweather_en.md) > Weather forecast files by city on MSC Datamart

# Weather forecast data by city in XML format

This page describes the XML data of the [weather forecasts by city](readme_citypageweather_en.md) available in the MSC Datamart.

The XML files are updated hourly at a minimum, but can be updated earlier with issue of special weather warnings, watches and amendments.

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available via the HTTPS protocol. It is possible to access it with a standard browser. In this case, we obtain a list of links giving access to a XML file.

Weather forecast data by city, disseminated in dated files (single files) are available according to this hierarchy :

  [https://dd.weather.gc.ca/citypage_weather/{PROV}/{HH}](https://dd.weather.gc.ca/citypage_weather/)
  
  where:
  
    * __PROV__ : Two letter provincial or territorial code indicating the area covered by the forecasts
    * __HH__ : Hour (UTC) of forecast data emission 

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

  Note: the `HEF` directory contains high elevation forecasts for seasonal forecast bulletins published only for British Columbia.

## File name nomenclature 

The files have the following nomenclature:

  `{YYYYMMDD}T{HHmmss.sss}Z_MSC_CitypageWeather_{SiteCode}_{L}.xml`

  where :

    * __SiteCode__ : City code (see below)
    * __L__ : Letter indicating file language: fr (French) or en (English)

  Examples of file names:

    * 20240815T154059.89Z_MSC_CitypageWeather_s0000011_fr.xml
    * 20240815T154059.89Z_MSC_CitypageWeather_s0000011_en.xml

A [list with location names and SiteNameCodes](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/citypage-weather/site_list_en.geojson) is available in GeoJSON format.

## Tags and XML schemas 

* A table [describing each of the city page weather XML element tags and their associated attributes](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/citypage-weather/citypage_tags_table_e.csv) is available.

* The XML schemas for citypage weather data are found in this directory :

  [https://dd.weather.gc.ca/citypage_weather/schema/](https://dd.weather.gc.ca/citypage_weather/schema/)

## Icons of the XML product

* City page weather XML files contain __coded__ current conditions and forecast conditions. These codes are used to determine the icon displayed on the weather office web site's city pages. Tables describing the meteorological conditions for each code are available at:

     * [Current weather conditions](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/citypage-weather/current_conditions_icon_code_descriptions_e.csv)
     * [Forecast weather conditions](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/citypage-weather/forecast_conditions_icon_code_descriptions_e.csv)

* These icons are covered by the standard Environment Canada Terms and Conditions: [https://www.canada.ca/en/transparency/terms.html](https://www.canada.ca/en/transparency/terms.html). To make a commercial usage of these icons, you must obtain prior explicit consent.

* You can also create your own icons using WMO World Weather Symbols. See <em>A complete set of WMO weather symbols in SVG with full metadata and fallback PNGs</em> at this address: [https://github.com/OGCMetOceanDWG/WorldWeatherSymbols](https://github.com/OGCMetOceanDWG/WorldWeatherSymbols)

## Support

If you have any questions about this data, please [contact us](https://weather.gc.ca/mainmenu/contact_us_e.html).

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).





