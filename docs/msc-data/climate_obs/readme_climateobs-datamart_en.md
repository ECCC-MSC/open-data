[En français](readme_climateobs-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [Climate  data (normals, daily, monthly)](readme_climateobs_en.md) > Climate  data (normals, daily, monthly) on MSC Datamart

# Climate  data (normals, daily, monthly) in CSV format

This document describes three climate data sets, climate normal, daily climate observations and monthly climate observations summaries at various climate stations across Canada.

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The  climate  data is available using the HTTP protocol and resides in a directory that is plainly accessible to a web browser.

The data can be accessed at the following URLs :

* https://dd.meteo.gc.ca/climate/observations/normals/csv/1981-2010/[AB,BC,MB,NB,NL,NS,NT,NU,ON,PE,QC,SK,YT]
* https://dd.meteo.gc.ca/climate/observations/daily/csv/[AB,BC,MB,NB,NL,NS,NT,NU,ON,PE,QC,SK,YT]
* https://dd.meteo.gc.ca/climate/observations/monthly/csv/[AB,BC,MB,NB,NL,NS,NT,NU,ON,PE,QC,SK,YT]

where :

* __normals__ : Climate normals and averages are used to summarize or describe the average climatic conditions of a particular location with at least 15 years of data between 1981-2010.
* __daily__ : Climate daily data from daily climate stations and hourly stations.
* __monthly__ : A cross-country summary of the averages and extremes for the month, including precipitation totals, max-min temperatures, and degree days.  This data is available from stations that produce daily data. 
* __(AB,BC,MB,NB,NL,NS,NT,NU,ON,PE,QC,SK,YT)__ : List of the 13 provinces/territories.

## File name nomenclature 

NOTE : ALL HOURS ARE IN UTC.

File names have the form :

* climate_normals_PROVTERR_XXXXXXX_YYY1-YYY2.csv
* climate_daily_PROVTERR_XXXXXXX_YYYY-MM_P1D.csv
* Climate_monthly_PROVTERR_XXXXXXX_YYYY_P1M.csv

where :

* __climate__ : Constant string indicating the data source, namely climate data 
* __normals__ : Constant string indicating climate data that critically contributes to the characterization of Earth’ s climate
* __daily__ : Constant string indicating daily climate data
* __monthly__ : Constant string indicating monthy climate data 
* __PROVTERR__ : 2-letter code for the province or territory, and 1 string for National coverage. The code is one of the 13 following values :
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
    * QC (Quebec)
    * SK (Saskatchewan)
    * YT (Yukon)
* __XXXXXXX__ : Climate_ID of the climate stations (see note)
* __YYY1__ : Year of the beginning of the climate period of interest : [1981]
* __YYY2__  : Year of the end of the climate period of interest : [2010]
* __YYYY__ : Year of the climate daily data
* __MM__ :  Month of the climate daily/monthly data
* __P1D__ : Constant string indicating 1 day time step (ISO8601 standard)
* __P1M__ : Constant string indicating 1 month time step (ISO8601 standard)
* __csv__ : Constant string indicating the CSV format

Examples :

•	climate_normals_QC_7040446_1981-2010.csv 
•	climate_daily_QC_7025280_1993-03_P1D.csv 
•	climate_monthly_QC_7025280_2001_P1M.csv

## List of variables

The available variables and units for Climate data are documented here :

* [Climate normals](https://www.canada.ca/en/environment-climate-change/services/climate-change/canadian-centre-climate-services/display-download/technical-documentation-climate-normals.html#toc1)
* [Climate daily](https://www.canada.ca/en/environment-climate-change/services/climate-change/canadian-centre-climate-services/display-download/technical-documentation-daily-data.html#toc0)
* [Climate monthly](https://www.canada.ca/en/environment-climate-change/services/climate-change/canadian-centre-climate-services/display-download/technical-documentation-monthly-climate-summaries.html#toc0)

## File contents

* __Climate normals__

Averages and Extremes offered here are based on Canadian climate stations with at least 15 years of data between 1981 to 2010.

"Climate averages", "climate means" or "climate normals" are all interchangeable terms. They refer to arithmetic calculations based on observed climate values for a given location over a specified time period. 

The World Meteorological Organization (WMO) recommends that countries prepare climate normals for the official 30-year normals periods ending in 1930, 1960 and 1990, for which the WMO World Climate Normals are published. In addition, WMO recommends the updating of climate normals at the end of every decade as provided here for 1981 to 2010.

See detailed documentation here :

[https://www.canada.ca/en/environment-climate-change/services/climate-change/canadian-centre-climate-services/display-download/technical-documentation-climate-normals.html](https://www.canada.ca/en/environment-climate-change/services/climate-change/canadian-centre-climate-services/display-download/technical-documentation-climate-normals.html)

* __Climate daily__

Daily data is derived from two sources of data. The first are Daily Climate Stations producing one or two observations per day of temperature, precipitation. The second are hourly stations (see hourly data sets) that typically produce more weather elements e.g. wind or snow on ground. Data is available for stations that are currently operational with a long period of record.

See detailed documentation here :

[https://www.canada.ca/en/environment-climate-change/services/climate-change/canadian-centre-climate-services/display-download/technical-documentation-daily-data.html](https://www.canada.ca/en/environment-climate-change/services/climate-change/canadian-centre-climate-services/display-download/technical-documentation-daily-data.html)

* __Climate monthly__

A cross-country summary of the averages and extremes for the month, including precipitation totals, max-min temperatures, and degree days.  This data is available from stations that produce daily data.

See detailed documentation here :

[https://www.canada.ca/en/environment-climate-change/services/climate-change/canadian-centre-climate-services/display-download/technical-documentation-monthly-climate-summaries.html](https://www.canada.ca/en/environment-climate-change/services/climate-change/canadian-centre-climate-services/display-download/technical-documentation-monthly-climate-summaries.html)

## Support

If you have any questions about these data, please contact us at : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).


