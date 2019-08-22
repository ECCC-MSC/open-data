[En français](readme_cangrd-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [CanGRD](readme_cangrd_en.md) > CanGRD on MSC Datamart

# Canadian Gridded Temperature and Precipitation Anomalies (CANGRD) in GeoTIFF format

The CANGRD is based on the Adjusted and Homogenized Canadian Climate Data (AHCCD) for historical climate observations from 1948 for all of Canada, and from 1900 for southern Canada, until the end of the previous calendar year. The monthly, seasonal and annual mean daily maximum and minimum temperature anomalies are computed at each observing station and for each year by subtracting the relevant baseline average (defined as average over 1961-1990 reference period) from the relevant monthly, seasonal, and annual values. The monthly, seasonal and annual total precipitation anomalies are computed similarly. Additionally, the precipitation anomalies are then normalized by dividing by the mean reference period and expressed in percentage to produce normalized precipitation departures.

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available via the HTTP protocol. It is possible to access it with a standard browser. In this case, we obtain a list of links giving access to a GeoTIFF file.

The data can be accessed at the following URLs :

* https://dd.meteo.gc.ca/climate/cangrd/geotiff/historical/annual/[anomaly, trend]
* https://dd.meteo.gc.ca/climate/cangrd/geotiff/historical/seasonal/[DJF,MAM,JJA,SON]/[anomaly, trend]
* https://dd.meteo.gc.ca/climate/cangrd/geotiff/historical/monthly_ens/anomaly

where :

* __historical__ : Historical simulations from 1948 for all of Canada, and from 1900 for southern Canada, until the end of the previous calendar year.
* __monthly__ : January to December 
* __seasonal__ : The standard meteorological seasons are used: (March to May (MAM, spring), June to August (JJA, summer),  September to November (SON, autumn/fall), and December to February (DJF, winter)]
* __anomaly__ : Anomalies are computed at each observing station and for each year by subtracting the relevant baseline average (defined as average over 1961-1990 reference period) from the relevant monthly, seasonal, and annual values (temperature and precipitation anomalies: 1948-2017)
* __trend__ : Trend data represents the change in temperature or relative precipitation departure over the period of record (mean temperature trend: 1948-2016; precipitation trend: 1948-2012)

## File name nomenclature 

NOTE : ALL HOURS ARE IN UTC.

File names have the form :

CANGRD_hist_TemporalResolution_Value_ProjectionResolution_Variable_TimePeriod.tif

where :

* __CANGRD__ : Constant string indicating the data source, namely the Canadian gridded annual, seasonal, and monthly temperature and precipitation anomalies, which were interpolated from stations in the Adjusted and Homogenized Canadian Climate Data AHCCD.
* __hist__ : Constant string indicating historical data.
* __TemporalResolution__ : Temporal resolution, taking one of the values : [annual, monthly, DJF, MAM, JJA, SON].
* __Value__ : Values category, taking one of the values :  [ anom, trend].
* __Projection__ : Grid mapping (projection) taking the value : [ps]; ps stands for polar stereographic projection.
* __Resolution__ : Grid resolution taking the value : [50km].
* __Variable__ : Name of forecast variable available in the file, taking one of the values : [PCP, TMIN, TMAX, TMEAN]; PCP stands for total precipitation, TMIN stands for minimum temperature, TMAX stands for maximum temperature, TMEAN stands for mean temperature.
* __TimePeriod__ : Time period, taking one of the values : [YYYY, YYYY-MM, YYY1-YYY2]; YYYY-MM  stands for year-month for the monthly anomalies, YYY1-YYY2 stands for the years interval used in the trends.
* __tif__ : Constant string indicating the GeoTIFF format.

Examples :

* CANGRD_hist_annual_anom_ps50km_TMEAN_1903.tiff
* CANGRD_hist_DJF_trend_ps50km_PCP_1948-2012.tiff

## Grid specifications

The CANGRD grid is in polar stereographic projection with a 50 km spatial resolution. The grid is a 125 (columns) by 95 (rows) matrix, where the SW corner (0,0) is at 40.0451°N latitude and 129.8530°W longitude. The projection is true at 60.0°N and centered on 110.0°W. 

## List of variables

The available variables and units for CANGRD are :

* Maximum temperature anomaly (°C)
* Minimum temperature anomaly (°C)
* Mean temperature anomaly (°C)
* Mean temperature trend (°C)
* Total precipitation anomaly (%)
* Relative total precipitation trend (%)

## Support

If you have any questions about these data, please contact us at : ec.dps-client.ec@canada.ca

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).

