[En Français](readme_aqhi-datamartxml_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > AQHI

# Air Quality Health Index (AQHI) observation and forecast data in XML format

This page describes the the observation and forecast data available in XML format for the [Air Quality Health Index AQHI](readme_aqhi_en.md) that are also available on the [Environment and Climate Change Canada website](https://meteo.gc.ca/airquality/pages/index_e.html). 

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available via the HTTP protocol. It is possible to access it with a standard browser. In this case, we obtain a list of links giving access to a XML file.

The data can be accessed at the following address :

* Observations :

    * Atlantic region: [https://dd.weather.gc.ca/air_quality/aqhi/atl/observation/realtime/xml](https://dd.weather.gc.ca/air_quality/aqhi/atl/observation/realtime/xml)
    * Ontario region: [https://dd.weather.gc.ca/air_quality/aqhi/ont/observation/realtime/xml](https://dd.weather.gc.ca/air_quality/aqhi/ont/observation/realtime/xml)
    * Prairie and Northern Region: [https://dd.weather.gc.ca/air_quality/aqhi/pnr/observation/realtime/xml](https://dd.weather.gc.ca/air_quality/aqhi/pnr/observation/realtime/xml)
    * Pacific and Yukon Region: [https://dd.weather.gc.ca/air_quality/aqhi/pyr/observation/realtime/xml](https://dd.weather.gc.ca/air_quality/aqhi/pyr/observation/realtime/xml)
    * Quebec region: [https://dd.weather.gc.ca/air_quality/aqhi/que/observation/realtime/xml](https://dd.weather.gc.ca/air_quality/aqhi/que/observation/realtime/xml)
      
* Public forecasts:

    * Atlantic region: [https://dd.weather.gc.ca/air_quality/aqhi/atl/forecast/realtime/xml](https://dd.weather.gc.ca/air_quality/aqhi/atl/forecast/realtime/xml)
    * Ontario region: [https://dd.weather.gc.ca/air_quality/aqhi/ont/forecast/realtime/xml](https://dd.weather.gc.ca/air_quality/aqhi/ont/forecast/realtime/xml)
    * Prairie and Northern Region: [https://dd.weather.gc.ca/air_quality/aqhi/pnr/forecast/realtime/xml](https://dd.weather.gc.ca/air_quality/aqhi/pnr/forecast/realtime/xml)
    * Pacific and Yukon Region: [https://dd.weather.gc.ca/air_quality/aqhi/pyr/forecast/realtime/xml](https://dd.weather.gc.ca/air_quality/aqhi/pyr/forecast/realtime/xml)
    * Quebec region: [https://dd.weather.gc.ca/air_quality/aqhi/que/forecast/realtime/xml](https://dd.weather.gc.ca/air_quality/aqhi/que/forecast/realtime/xml)

The real-time XML files are kept on the MSC Datamart for a period of 48 hours.

A file that makes it easier for automated systems to access [real-time updated data](https://dd.meteo.gc.ca/air_quality/doc/AQHI_XML_File_List.xml) is available. 

A [complete list of cities](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/aqhi/aqhi_station.geojson), with the codes of [CGNDB](http://www4.rncan.gc.ca/search-place-names/unique), Canada's toponymic data maintained by Natural Resources Canada, is available in GeoJSON format. 

## File name nomenclature 

NOTE : ALL HOURS ARE IN UTC.

* **Observations** (Note: monthly summary XML files are not yet available)

  * Hourly file: AQ_OBS_CGNDBcode_YYYYMMDDhhmm.xml
  * Copy of the most recent real-time observation file: AQ_OBS_CGNDBcode_CURRENT.xml

where :

* __'AQ_OBS'__ : Filename prefix. Constant string.
* __CGNDBcode__ : 5-letter [CGNDB](http://www4.rncan.gc.ca/search-place-names/unique) code which identifies each [AQHI communitiy](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/aqhi/aqhi_community.geojson). 
* __YYYY__ : Year of the observation, 4 digits.
* __MM__ : Month of the observation, 2 digits (January = 01).
* __DD__ : Day of the observation, 2 digits.
* __hh__: Hour of the observation, 2 digits.
* __mm__ : Minute of the observation, 2 digits.

* **Public forecasts** (Note: monthly summary XML files are not yet available) :
    * __Regular issue__ :     AQ_FCST_CGNDBcode_YYYYMMDDhhmm.xml
    * __Amended forecasts__ : AQ_FCST_CGNDBcode_YYYYMMDDhhmm_AMD.xml
    * __Copy of the most recent real-time forecast file__ : AQ_FCST_CGNDBcode_CURRENT.xml
   
where :

* __'AQ_FCST'__ :  Filename prefix. Constant string.
* __CGNDBcode__ : 5-letter [CGNDB](http://www4.rncan.gc.ca/search-place-names/unique) code which identifies each [AQHI communitiy](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/aqhi/aqhi_community.geojson). 
* __YYYY__ : Year of the forecast issue time, 4 digits.
* __MM__ : Month of the forecast issue time, 2 digits (January = 01).
* __DD__ : Day of the forecast issue time, 2 digits.
* __hh__ : Hour of the forecast issue time, 2 digits.
* __mm__ : Minute of the forecast issue time, 2 digits.
* __'AMD'__ : The suffix appended to the filename to indicate that the file is
an amendment.

## Notes

* The XML observation files are produced hourly, at approximately 40 minutes past the hour,
and are available on Datamart for a period of 48 hours. The XML public forecast files are issued
twice per day at approximately 6am and 5pm local time and are available on the MSC Datamart for a
period of 48 hours.

* Air quality observations are provided by provinces and municipalities. Provincial jurisdictions also control how observations are communicated to the public. Quebec did not agree to the publication of current air quality in the form of an air quality health index (AQHI). This explains why no observation are available at the address: [https://dd.weather.gc.ca/air_quality/aqhi/que/observation/](https://dd.weather.gc.ca/air_quality/aqhi/que/observation/). However, the Ministère du Développement durable, Environnement et Lutte contre les changements climatiques (MDDELCC) and Ville de Montreal also redistribute some of their data on the American AirNow portal:
[https://www.airnowtech.org/index.cfm?page=login](https://www.airnowtech.org/index.cfm?page=login)

## Support

If you have any questions about these data, please contact us at: ec.dps-client.ec@canada.ca

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).

