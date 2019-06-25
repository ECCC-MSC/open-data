[En Français](readme_ahccd-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC Open Public Data](../readme_en.md) > AHCCD

# Adjusted and Homogenized Canadian Climate Data (AHCCD) in GeoJSON format

The data consist of monthly, seasonal and annual means of homogenized daily maximum, minimum and mean surface air temperatures for more than 330 locations in Canada; monthly, seasonal and annual totals of adjusted daily rainfall, snowfall and total precipitation for more than 460 locations; homogenized monthly, seasonal and annual means of hourly surface wind speed at more than 110 locations; monthly, seasonal and annual means of hourly station and sea level pressure adjusted for more than 630 locations. The data are given for the entire period of observation. Please refer to the papers below for detailed information regarding the procedures for homogenization and adjustment. 

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](.../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](.../../usage-overview/readme_en.md) is also available.

The data is available via the HTTP protocol. It is possible to access it with a standard browser. In this case, we obtain a list of links giving access to a GeoJSON file.

The data can be accessed at the following URLs:

/climate/ahccd/geojson/historical/annual/[AB,BC,MB,NB,NL,NS,NT,NU,ON,PE,QC,SK,YT]

/climate/ahccd/geojson/historical/seasonal/[DJF,MAM,JJA,SON]/[AB,BC,MB,NB,NL,NS,NT,NU,ON,PE,QC,SK,YT]

/climate/ahccd/geojson/historical/monthly/[AB,BC,MB,NB,NL,NS,NT,NU,ON,PE,QC,SK,YT]

Where :

* __historical__ : Historical data from 1840. Annually updated.
* __seasonal__ : The standard meteorological seasons are used: (March to May (MAM, spring), June to August (JJA, summer),  September to November (SON, autumn/fall), and December to February (DJF, winter)]
* __monthly__ : January to December
*  AB,BC,MB,NB,NL,NS,NT,NU,ON,PE,QC,SK,YT : The 10 Canadian provinces and 3 territories 

## File name nomenclature 

NOTE: ALL HOURS ARE IN UTC.

File names have the form:

AHCCD_hist_TemporalResolution_ProvTerr_XXXXXXX_Variable_TimeStep.json

Where:

* __AHCCD__ : constant string indicating the data source, namely the adjusted and homogenized climate data for many climatological stations in Canada
* __hist__ : constant string indicating historical data. Varies per station, per variable with data availability ranging between 1840 to the year preceding current year
* __TemporalResoltion__ : time period, taking one of the values : [annual, monthly, DJF, MAM, JJA, SON]
* __ProvTerr__ : 2-letter code for the province or territory 
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
            * QC (Quebec)
            * SK (Saskatchewan)
            * YT (Yukon)
* __XXXXXXX__ : Climate_ID of the climate stations
* __Variable__ : name of the variable available in the file, taking one of the values : [TMEAN,TMIN,TMAX,PCP,RA,SN,SLP,PSFC,SFCWND]; TMEAN stands for mean temperature, TMIN stands for minimum temperature, TMAX stands for maximum temperature, PCP stands for total precipitation, RA stands for rain; SN stands for snow; SLP stands for sea level pressure; PSFC stands for surface pressure; SFCWND stands for surface wind speed
* __TimeStep__ : time step, taking one of the values : [P1Y, P1M]; P1Y stand for 1 year time step and P1M stands for 1 month time step
* __json__ : constant string indicating the GeoJSON format

Example:  AHCCD_hist_annual_QC_7040446_SLP_P1Y.json

## List of variables

Warning: the tables below are not up to date (to come), some variables are missing. Feel free to [contact us](mailto:ec.dps-client.ec@canada.ca) for more information.

The available variables and units for AHCCD are:

* Maximum temperature (°C)
* Minimum temperature (°C)
* Mean temperature (°C)
* Rainfall (mm/period)
* Snowfall (mm/period)
* Total precipitation (mm/period)
* Wind speed (m/s)
* Station level  pressure (Pa) 
* Sea level pressure (Pa)

## Support

If you have any questions about these data, please contact us at: ec.dps-client.ec@canada.ca

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).

