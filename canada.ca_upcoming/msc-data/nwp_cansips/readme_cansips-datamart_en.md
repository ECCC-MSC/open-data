[En Français](readme_cansips-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC Open Public Data](../readme_en.md) > CanSIPS

# Canadian Seasonal to Inter-annual Prediction System (CanSIPS) Data in GRIB2 Format

The [Canadian Seasonal to Inter-annual Prediction System (CanSIPS)](readme_cansips_en.md) is a long-term prediction system whose objective is to forecast the evolution of global climate conditions. CanSIPS is a multi-model ensemble (MME) system using two climate models developed by the Canadian Centre for Climate Modelling and Analysis (CCCma). It is a fully coupled atmosphere-ocean-ice-land prediction system relying on the operationnal data assimilation infrastructure for the initial state of the atmosphere, sea surface temperature and sea ice. For further technical information about CanSIPS please refer to the technical note.
Principal components of CanSIPS

## Principal components of CanSIPS
    
* __Assimilation mode__: CanSIPS uses a continuous assimilation cycle for the following 3D atmospheric variables: temperature, wind and humidity. The oceanic variables: sea surface temperature and the sea ice are also assimilated by the system. The assimilated data are provided by the global atmospheric analysis available every 6 hours and the daily sea surface temperature and sea ice analysis. Also a 3D ocean temperature analysis is integrated to CanSIPS trial field before launching the integration.
* __Forecast mode__: The CanSIPS forecasts are based on a 10-member ensemble of forecasts produced with each of two CCCma climate models for a total ensemble size of 20. Monthly to multi-seasonal forecasts extending to 12 months are issued on the first day of each month.
* __Hindcast mode__: CanSIPS climatology is based on series of historical forecasts covering the period 1981-2010. This climatology of the system is very useful for the interpretation of the forecast since the anomaly is generally used instead of the actual raw forecast.

## Data address 

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](.../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](.../../how-to/readme_en.md) is also available.

The data is available using the HTTP protocol and resides in a directory that is plainly accessible to a web browser. Visiting that directory with an interactive browser will yield a raw listing of links, each link being a downloadable GRIB2 file.

The data can be accessed at the following URLs:

* https://dd.weather.gc.ca/ensemble/cansips/grib2/forecast/raw/YYYY/MM/
* https://dd.weather.gc.ca/ensemble/cansips/grib2/hindcast/raw/YYYY/MM/

where:

* __forecast__ : constant string indicating that the file contains the data from the forecast part of CanSIPS, in opposition to the hindcats part.
* __hindcast__ : constant string indicating that the file contains the data from the hindcast part of CanSIPS, in opposition to the forecast part.
* __MM__ : Month of the forecast start [01, 02, 03, ..., 12]
* __YYYY__ : Year of the forecast start [2012, 2013, ...]

## Technical specification of the grid

Table lists the values of various parameters of the CanSIPS lat-lon grid.

| Parameter | Value |
| ------ | ------ |
| ni | 145 |
| nj | 73 | 
| resolution | 2.5° |
| coordinates of the first grid point | 90° S  0° E | 

## File name nomenclature 

NOTE: ALL HOURS ARE IN UTC.

The files have the following nomenclature:

* Filename for the forecast: cansips_forecast_raw_latlon2.5x2.5_VAR_YYYY-MM_allmembers.grib2
* Filename for the hindcast: cansips_hindcast_raw_latlon2.5x2.5_VAR_YYYY-MM_allmembers.grib2

where:

* __cansips__ : constant string indicating that the data is from the CanSIPS system.
* __forecast__ : constant string indicating that the file contains the data from the forecast part of CanSIPS, in opposition to the hindcats part.
* __hindcast__ : constant string indicating that the file contains the data from the hindcast part of CanSIPS, in opposition to the forecast part.
* __raw__ : constant string indicating that the file contains raw data without bias correction
* __latlon2.5x2.5__ : constant string indicating the latitude-longitude projection at a resolution of 2.5 x 2.5 degrees.
* __VAR__ : Variable type included in this file. To consult a complete list, refer to the variables section
* __MM__ : Month of the forecast start [01, 02, 03, ..., 12]
* __YYYY__ : Year of the forecast start [2012, 2013, ...]
* __allmembers__ : constant string indicating that all members [01, 02, 03, ..., 20] are grouped into the file.
* __grib2__ : constant string indicating the GRIB2 format is used.

Example of file name: cansips_forecast_raw_latlon2.5x2.5_HGT_ISBL_0500_2012-10_allmembers.grib2

This GRIB2 file originates from CMC CanSIPS system. The data in the file have a start time on the first day of October 2012. The variable in the file is the monthly mean of the geopontential height at 500hpa, for all the members of the ensemble. The projection used is the latitude-longitude projection at a resolution of 2.5 x 2.5 degrees.

## Levels

The data are available at surface and for certain isobaric levels.

## List of variables

Warning: the tables below are not up to date (to come), some variables are missing. Feel free to [contact us](mailto:ec.dps-client.ec@canada.ca) for more information.

* [Zero lead time forecast](https://weather.gc.ca/grib/CANSIPS/CANSIPS_latlon2.5x2.5_ALL_VAR_Lead-time-month-ZERO_hindcast_e.html)
* [Non-zero lead time forecast](https://weather.gc.ca/grib/CANSIPS/CANSIPS_latlon2.5x2.5_ALL_VAR_Lead-time-month-NONZERO_hindcast_e.html)

## Support

If you have any questions about these data, please contact us at: ec.dps-client.ec@canada.ca

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).
