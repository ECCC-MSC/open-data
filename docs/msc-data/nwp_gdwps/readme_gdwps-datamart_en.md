[En français](readme_gdwps-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [GDWPS](readme_gdwps_en.md) > GDWPS on MSC Datamart

# Global Deterministic Wave Prediction System (GDWPS) data in GRIB2 format

This page describes the [Global Deterministic Wave Prediction System](readme_gdwps_en.md) data available in GRIB2 format.

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.


The data is available via the HTTPS protocol. It is possible to access it with a standard browser. In this case, we obtain a list of links giving access to a GRIB2 file.

The data can be accessed at the following address :

* [https://dd.weather.gc.ca/model_wave/ocean/global/grib2/{HH}/](https://dd.weather.gc.ca/model_wave/ocean/global/grib2)

where :

* __HH__ : Model run start, in UTC [00 or 12]

A history of 24 hours is maintained in this directory.

## Nomenclature of file directories 

NOTE: ALL HOURS ARE IN UTC.

CMC_gdwps_domain_Variable_LevelType_level_latlondddxddd_YYYYMMDDHH_Phhh.grib2

where :

* __CMC__ : Constant string indicating that the data is from the Canadian Meteorological Centre
* __gdwps__ : Constant string indicating that the data is from the Global Deterministic Wave Prediction System
* __domain__ : Constant string indicating which domain that the data is from
* __Variable__ : Variable type included in this file
* __LevelType__ : Level type.
* __Level__ : Level value.
* __latlon0.dx0.dd__ : Constant string indicating that the projection used is lat/long at 0.dd x 0.dd degrees resolution
* __YYYYMMDD__ : Year, month and day of the beginning of the forecast
* __HH__ : UTC run time [00, 12]
* __Phhh__ : P is a constant character. hhh is the forecast hour [000, 001, 002, ..., 048, 051, ..., 120]
* __grib2__ : Constant string indicating the GRIB2 format is used

Example of file name :

CMC_gdwps_global_HTSGW_SFC_0_latlon0.25x0.25_2017092112_P096.grib2

This file originates from the Canadian Meteorological Center (CMC) and contains the data of the Global Deterministic Wave Prediction System. The data in the file start on September 21th 2017 at 12Z (2017092112). It contains the significant wave height (HTSGW) for the world at the surface (SFC_0) on a lat/long grid at 0.25 degree x 0.25 degree resolution for the forecast hour 096 (P096) in GRIB2 format (.grib2).

## Levels

Levels that may be applicable to a given parameter are :

* Surface
* Fixed height above ground

Note : Swell parameters no longer refer to the total swell, they now refer to the primary swell. At each point of the domain, the spectra can be divided between wind sea and a certain number of swells. The two swells that contain the most energy are designated in order as the primary and secondary swell. Wind, sea and swell parameters can be undefined at some grid points, for the former if there is little wind, for the latter if there are only locally generated waves.

## Variable List

__Available fields : parameter numbers and units__
__This table provides, for each GRIB2 parameter number: a short description, an alphabetical abbreviation, the levels available for the parameter, and measurement units.__ 

|GRIB2 discipline/category/parameter number | Parameter description |	Abbreviation |	Level |	Units |
|-------------------------------------------|-----------------------|----------------|--------|-------|
|10/2/0 |	Ice cover |	ICEC |	SFC_0 	|fraction|
|0/2/2 |	U-Component of Wind |	UGRD |	TGL_10 (10m above ground) |	m/s|
|0/2/3 |	V-Component of Wind |	VGRD |	TGL_10 (10m above ground) |	m/s|
|10/0/3 |	Significant height of combined wind waves and swell |	HTSGW |	SFC_0 |	m|
|10/0/34 |	Peak wave period |	PWPER |	SFC_0 |	s|
|10/0/28 |	Mean zero-crossing wave period |	MZWPER |	SFC_0 |	s|
|10/0/4 |	Direction of wind waves (from which) |	WVDIR |	SFC_0 |	degrees true|
|10/0/5 |	Significant height of wind waves |	WVHGT |	SFC_0 |	m|
|10/0/6 |	Mean period of wind waves |	WVPER |	SFC_0 |	s|
|10/0/7 |	Direction of primary swell |	SWDIR |	SFC_0 	|degrees true|
|10/0/8 |	Significant height of primary swell |	SWELL |	SFC_0 |	m|
|10/0/9 |	Peak period of primary swell 	|SWPER |	SFC_0 |	s|

Note :

* u and v components of the wind vector are to be resolved relative to the defined grid, in the direction of increasing i and j coordinates.

## Support

If you have any questions about this data, please contact us at : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).
 
 
 
 