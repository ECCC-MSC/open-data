[En français](readme_obs_insitu_xmldatamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [Observations summary](readme_obs_insitu_en.md) > Observations summary on MSC Datamart

# Observations summary data in XML format by province or territory 

This page describes the [observation](readme_obs_insitu_en.md) data available in XML format.

The provincial and territory summary pages provide the observations of all available stations for the selected province or territory. Data is made available through a number of sources and may not be QA/QC.

The files are in XML format and follow an Environment and Climate Change Canada defined schema.

Update frequency of XML files will be generated as follows:

* Hourly - every 5 minutes
* Today - every 5 minutes
* Yesterday - twice per day at 06:30 UTC and 08:00 UTC

There are 6 XML files for each province/territory as follows:

* English and French for Hourly Provincial Summary
* English and French for Today's Provincial Summary
* English and French for Yesterday's Provincial Summary

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available using the HTTPS protocol and resides in a directory that is plainly accessible to a web browser. Visiting that directory with an interactive browser will yield a raw listing of links, each link being a downloadable XML file.

The provincial and territorial summary XML files are grouped in a directory tree that is based on the province/territory and the summary type.

The provincial summary XML files are available at the following address :

* [https://dd.weather.gc.ca/observations/xml/{PC}/{TYPE}](https://dd.weather.gc.ca/observations/xml)

where :

* __PC__ : indicates the 2 letter provincial code in lower case. Could be one of the 13 values below:
    * AB (Alberta)
    * BC (British Columbia)
    * MB (Manitoba)
    * NB (New-Brunswick)
    * NL (Newfounland and Labrador)
    * NS (Nova Scotia)
    * NT (Northwest Territories)
    * NU (Nunavut)
    * ON (Ontario)
    * PE (Prince-Edouard Island)
    * QC (Quebec)
    * SK (Saskatchewan)
    * YT (Yukon)

* __TYPE__ : String indicating the summary type. Could be one of those 3 types: [hourly | today | yesterday]. See Description below for more information.

A history of data (30 days) is kept in the directory.

## Nomenclature 

NOTE: ALL HOURS ARE IN UTC.

The file names have the following nomenclature :

TYPE_PC_YYYYMMDD_L.xml

where :

* TYPE : String indicating the summary type. Could be one of those 3 types: [hourly | today | yesterday]. See Description below for more information.
* PC : Indicates the 2 letter provincial code in lower case. See above for the values.
* YYYYMMDDHH : Observations date. HH is present only in 'hourly' product type.
* L : 1 letter indicating the language of the file. Can be one of the values :
    * f (French)
    * e (English)

Examples of filename:

* hourly_ab_2010030517_e.xml
* today_mb_20100306_e.xml
* yesterday_qc_20100306_f.xml

## Description

__1- Hourly summary__

The Hourly summary contains the most recent observations available.

This file is regenerated at 8, 11, 14, 25, 35 and 50 minutes past each hour. The file is overwritten by every new version, until the last one created. The last one remaining on the server is the last created within the hour indicated in the file name, i.e. at 50 minutes. For every hour, a file is then kept for 30 days on the server.

If current data is missing, use the previous hour's data temporarily. Hourly observation data will be set to blank if it hasn't been updated within 2 hours and 15 minutes. 

These observations have QA/QC applied to them. Any values that do not pass QA/QC will be suppressed. This includes values that are flagged as doubtful.

Parameters contained in each file for the selected province or territory are:

* This Hour's Hot and Cold spots for Canada
* This Hour's Hot and Cold spots for the selected province/territory
* The current hour observations for each station available. It contains:
    * Present Condition (string)
    * Mean sea level pressure (kPa)
    * Value of pressure tendency (kPa)
    * Pressure tendency (rising, falling, stable)
    * Visibility (km)
    * Air temperature (°C)
    * Dew point (°C)
    * Relative humidity (%)
    * Wind speed (km/h)
    * Wind direction (code)
    * Gust speed (km/h)
    * Cloud cover
    * Wind chill
    * Humidex

__2- Today's summary__

Today's summary is generated at 8, 11, 14, 25, 35 and 50 minutes past each hour. The file is overwritten by every new version, until the last one created. The last one remaining on the server is the last created within the day indicated in the file name. For every day, a file is kept for 30 days on the server.   

Depending on the time of day, the data is obtained from either hourly data or synoptic data. If obtained from hourly data, QA/QC is applied. If obtained from synoptic data, QA/QC is not applied.

For example, on March 9 at 14:40 UTC, the today's observations file would contain the observations for the day starting on March 9 at 06 UTC and ending on March 9 at 14:40 UTC.

Today's component starts to accumulate the high/lows for each station at the start of the climate day (06Z each day). At 06Z each day the daily products high/lows are reset, then with each passing hour it accumulates the data, and generates the high and low from the start of the climate day.                                  

Some stations only report during day time, so they don't have any value before the first hour of observation. 

This file contains for the selected province or territory:

* Today so far Hot and Cold spots for Canada
* Today so far Hot and Cold spots for the selected province/territory
* The observations and records for each station available:
    * Maximum air temperature for today (°C)
    * Minimum air temperature for today (°C)
    * Wind direction of the peak wind (code)
    * Peak gust speed so far in the day (km/h)
    * Record value for maximum air temperature (°C)
    * Year of the record value for maximum air temperature
    * Record value for minimum air temperature (°C)
    * Year of the record value for minimum air temperature
    * Record value for rain precipitation (mm)
    * Year of the record value for rain precipitation
    * Record value for snow precipitation (cm)
    * Year of the record value for snow precipitation
    * Year from which this station acquired temperature data
    * Year from which this station acquired precipitation data

__3- Yesterday's summary__

Yesterday's summary is defined as the summary for the most recently completed climate day. A climate day goes from 06 UTC to 06 UTC. 

This product is based on the 06 UTC SYNO bulletins produced for each station. The data does not undergo QA/QC. Please refer to the [climatological official data sets](http://climat.meteo.gc.ca/index_e.html).

Some stations have observations but do not have a SYNO bulletins. These stations will be included in the 'hourly' and 'today' products but not in 'yesterday'.

Yesterday's summary is generated at 8, 11, 14, 25, 35 and 50 minutes past each hour. The file is overwritten by every new version, until the last one created. The last one remaining on the server is the last created within the day indicated in the file name. For every day, a file is kept for 30 days on the server.   

This file provides a list of all available stations for the selected province/territory displaying:

* Yesterday's Hot and Cold spots for Canada
* Yesterday's Hot and Cold spots for the selected province/territory
* Yesterday's record values for highest and lowest temperature, rain and snow amount for each station available
* Yesterday's values for highest and lowest temperature, peak wind, total precipitation, rain and snow amount for each station available

### Stations

For each station, the following information is provided:

* Station name
* Latitude (decimal degree)
* Longitude (decimal (degree)
* Transport Canada identification number
* Observations time in UTC and local time
* Climate station number
* WMO station number

There are in excess of 500 observation stations in Canada. However this number is continually changing. Stations only appear if data is available for that station.

## Notes

* A [complete documentation of the Meteorological Point Observation Mark-up Language Schema Description](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_station/Met-ML-SchemaDescriptionV2_e.pdf) is available.
* To be displayed, any record for an element must have a period of at least 15 years in the Climate Site database, as stated on the Climate Site: [http://climate.weather.gc.ca/historical_data/search_historic_data_e.html](http://climate.weather.gc.ca/historical_data/search_historic_data_e.html).
* Station Metadata is provided in English or French
* Any floating values that are below 0.05 are rounded to 0.0
* Any floating values that are 0.05 and above are rounded up to 0.1
* The creation date of the file is included in the header of each XML file
* ISO 8601 standard is used for all time/date formats
* All date/time are both in UTC and local time
* Historical data (record data) has undergone QA/QC procedures

## Support

If you have any questions about this data, [please contact us](https://weather.gc.ca/mainmenu/contact_us_e.html).

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).
