[En français](readme_ahccd-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [AHCCD](readme_ahccd_en.md) > AHCCD on MSC Datamart

# Adjusted and Homogenized Canadian Climate Data (AHCCD) in GeoJSON format

The AHCCD data are climate station datasets with adjustments (derived from statistical procedures) to the original historical station data to account for discontinuities from non-climatic factors, such as instrument changes or station relocation. 

This dataset was developed for use in climate research, including climate change studies. Long-term data records are often impacted by changes (e.g. site exposure, location, instrumentation, observer, and observing procedures) that are not related to climate. These non-climatic changes were detected and removed using statistical procedures. 

When necessary, data were corrected for some measurement techniques that are known to possibly lead to underestimations or overestimations. In addition, data from nearby stations were sometimes combined to create longer time series.

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available via the HTTPS protocol. It is possible to access it with a standard browser. In this case, we obtain a list of links giving access to a GeoJSON file.

The data can be accessed at the following URLs :

* [https://dd.weather.gc.ca/climate/ahccd/geojson/historical/annual/{[AB,BC,MB,NB,NL,NS,NT,NU,ON,PE,QC,SK,YT]}](https://dd.weather.gc.ca/climate/ahccd/geojson/historical/annual)
* [https://dd.weather.gc.ca/climate/ahccd/geojson/historical/seasonal/{[DJF,MAM,JJA,SON]/[AB,BC,MB,NB,NL,NS,NT,NU,ON,PE,QC,SK,YT]}](https://dd.weather.gc.ca/climate/ahccd/geojson/historical/seasonal)
* [https://dd.weather.gc.ca/climate/ahccd/geojson/historical/monthly/{[AB,BC,MB,NB,NL,NS,NT,NU,ON,PE,QC,SK,YT]}](https://dd.weather.gc.ca/climate/ahccd/geojson/historical/monthly)

where :

* __historical__ : Historical data from 1840. Annually updated.
* __seasonal__ : The standard meteorological seasons are used: (March to May (MAM, spring), June to August (JJA, summer),  September to November (SON, autumn/fall), and December to February (DJF, winter)]
* __monthly__ : January to December
*  AB,BC,MB,NB,NL,NS,NT,NU,ON,PE,QC,SK,YT : The 10 Canadian provinces and 3 territories 

## File name nomenclature 

NOTE : ALL HOURS ARE IN UTC.

File names have the form :

AHCCD_hist_TemporalResolution_ProvTerr_XXXXXXX_Variable_TimeStep.json

where :

* __AHCCD__ : Constant string indicating the data source, namely the adjusted and homogenized climate data for many climatological stations in Canada
* __hist__ : Constant string indicating historical data. Varies per station, per variable with data availability ranging between 1840 to the year preceding current year
* __TemporalResoltion__ : Time period, taking one of the values : [annual, monthly, DJF, MAM, JJA, SON]
* __ProvTerr__ : 2-letter code for the province or territory. The code is one of the 13 following values :
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
* __Variable__ : Name of the variable available in the file, taking one of the values : [TMEAN,TMIN,TMAX,PCP,RA,SN,SLP,PSFC,SFCWND]; TMEAN stands for mean temperature, TMIN stands for minimum temperature, TMAX stands for maximum temperature, PCP stands for total precipitation, RA stands for rain; SN stands for snow; SLP stands for sea level pressure; PSFC stands for surface pressure; SFCWND stands for surface wind speed
* __TimeStep__ : Time step, taking one of the values : [P1Y, P1M]; P1Y stand for 1 year time step and P1M stands for 1 month time step
* __json__ : Constant string indicating the GeoJSON format

Example :  AHCCD_hist_annual_QC_7040446_SLP_P1Y.json

## List of variables

Warning : the tables below are not up to date (to come), some variables are missing. Feel free to [contact us](mailto:ec.dps-client.ec@canada.ca) for more information.

The available variables and units for AHCCD are :

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

If you have any questions about this data, please contact us at : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info.comm.collab.science.gc.ca/).

