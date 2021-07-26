[En français](readme_aqhi-hpfxjson_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC Data](../readme_en.md) > [AQHI](readme_aqhi_en.md) > AQHI data in GeoJSON on MSC Datamart

# Air Quality Health Index (AQHI) observation and forecast data in GeoJSON format

This page describes the the observation and forecast data available in GeoJSON format for the [Air Quality Health Index AQHI](readme_aqhi_en.md) that are also available on the [Environment and Climate Change Canada website](https://meteo.gc.ca/airquality/pages/index_e.html). 

## Data location

HPFX data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available via the HTTPS protocol. It is possible to access it with a standard browser. In this case, we obtain a list of links giving access to a GeoJSON file.

The data can be accessed at the following address:

* __Observations__: [http://hpfx.collab.science.gc.ca/YYYMMDD/WXO-DD/air_quality/aqhi/[atl,ont,pnr,pyr,que]/observation/realtime/json](http://hpfx.collab.science.gc.ca/)

* __Public forecasts__: [http://hpfx.collab.science.gc.ca/YYYMMDD/WXO-DD/air_quality/aqhi/[atl,ont,pnr,pyr,que]/forecast/realtime/json](http://hpfx.collab.science.gc.ca/)

With:

    * atl: Atlantic region 
    * ont: Ontario region 
    * pnr: Prairie and Northern Region 
    * pyr: Pacific and Yukon Region
    * que: Quebec region

A [complete list of cities](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/aqhi/aqhi_station.geojson), with the codes of [CGNDB](http://www4.rncan.gc.ca/search-place-names/unique), Canada's toponymic data maintained by Natural Resources Canada, is available in GeoJSON format. 

## File name nomenclature 

NOTE: ALL HOURS ARE IN UTC.

* __Observations__

    * {YYYYMMDD}T{HH}{mm}Z_MSC_AQHI-Observation_{CGNDBcode}.json

* where:

    * __YYYYMMDD__ : Year, month and day of the observation
    * __T__ : Time delimiter according to ISO8601 norms
    * __HH__ : UTC time of the observation
    * __mm__ : Minute of the observation
    * __Z__ : Time zone (UTC hour)
    * __MSC__ : Constant string indicating the Meteorological Service of Canada, source of data 
    * __AQHI__ : Constant string for "Air Quality Health Index"
    * __Observation__ : Constant string for AQHI observation 
    * __CGNDBcode__ :  A 5-letter [CGNDB](http://www4.rncan.gc.ca/search-place-names/unique) code which identifies each [AQHI community](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/aqhi/aqhi_community.geojson). 
    * __json__ : Constant string for GeoJSON format

* __Public forecasts__ :

    * {YYYYMMDD}T{HH}{mm}Z_MSC_AQHI-Forecasts_{CGNDBcode}.json   
   
* where:
    
    * __YYYYMMDD__ : Year, month and day of the forecast issue time
    * __T__ : Time delimiter according to ISO8601 norms
    * __HH__ : Hour of the forecast issue time
    * __mm__ : Minute of the forecast issue time
    * __Z__ : Time zone (UTC hour)
    * __MSC__ : Constant string indicating the Meteorological Service of Canada, source of data 
    * __AQHI__ : Constant string for "Air Quality Health Index"
    * __Forecasts__ : Constant string for AQHI forecasts
    * __CGNDBcode__ :  A 5-letter [CGNDB](http://www4.rncan.gc.ca/search-place-names/unique) code which identifies each [AQHI community](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/aqhi/aqhi_community.geojson). 
    * __json__ : Constant string for GeoJSON format

## Notes

* The GeoJSON observation files are produced hourly, at approximately 40 minutes past the hour. The GeoJSON public forecast files are issued twice per day at approximately 6am and 5pm local time.

* When forecast data is amended, a parameter associated with the file status is updated accordingly in the GeoJSON file.

* Air quality observations are provided by provinces and municipalities. Provincial jurisdictions also control how observations are communicated to the public. Quebec did not agree to the publication of current air quality in the form of an air quality health index (AQHI). This explains why no observation are available at the address: [http://hpfx.collab.science.gc.ca/YYYMMDD/WXO-DD/air_quality/aqhi/que/observation/realtime/json](http://hpfx.collab.science.gc.ca). However, the Ministère du Développement durable, Environnement et Lutte contre les changements climatiques (MDDELCC) and Ville de Montreal also redistribute some of their data on [the American AirNow portal](https://www.epa.gov/outdoor-air-quality-data/download-daily-data).

## Support

If you have any questions about this data, please contact us at: [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).