[En français](readme_gdwps-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [GDWPS](readme_gdwps_en.md) > GDWPS on MSC Datamart

# Global Deterministic Wave Prediction System (GDWPS) data in GRIB2 format

This page describes the [Global Deterministic Wave Prediction System](readme_gdwps_en.md) data available in GRIB2 format.

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available via the HTTPS protocol. It is possible to access it with a standard browser. In this case, we obtain a list of links giving access to a GRIB2 file.

The data can be accessed at the following URL :

* [https://dd.weather.gc.ca/model_gdwps/25km/{HH}/](https://dd.weather.gc.ca/model_gdwps/25km)

where :

* __HH__ : Model run start, in UTC [00 or 12]

A history of 24 hours is maintained in this directory.

## Available Domains

Global latitude-longitude grid.

| Parameter | Value |
| ------ | ------ |
| ni | 1440 |
| nj |  721 |
| resolution | 0.25° |
| coordinate of first grid point | 90° S  0° E |

## File name nomenclature

NOTE: ALL HOURS ARE IN UTC.

File names have the form:

`{YYYYMMDD}T{HH}Z_MSC_GDWPS_{VAR}_{LVL}_{Grille}{resolution}_PT{hhh}H.grib2`

where :

* __YYYYMMDD__: Year, month and day of the beginning of the forecast
* __T__ : Time delimiter according to ISO8601 norms
* __HH__: UTC run time [00, 12]
* __Z__ : Time zone (UTC hour)
* __MSC__ : Constant string indicating the Meteorological Service of Canada, source of data
* __GDWPS__ : Constant string indicating that data is from the Global Deterministic Wave Prediction System
* __VAR__ : Variables included in the file
* __LVL__ : Vertical level [Sfc for the surface, AGL for fixed height above ground]
* __Grille__ : Horizontal grid type [LatLon]
* __resolution__ : Indicating resolution in degreee in latitude and longitude directions [0.25]
* __PT{hhh}H__: Forecast hours based on [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) norms. P, T and H are constant character designating Period, Time and Hour. "hhh" is the forecast hour [000, 001, 002, ...048, 051, ..., 117, 120]
* __grib2__: constant string indicating the GRIB2 format is used

Example of file name :

20211007T00Z_MSC_GDWPS_HTSGW_Sfc_LatLon0.25_PT051H.grib2

This file originates from the MSC and contains the data of the Global Deterministic Wave Prediction System. The data in the file start on October 7th 2021 at 00Z (2021100700). It contains the significant wave height (HTSGW) for the world at the surface on a lat/long grid at 0.25 degree x 0.25 degree resolution for the forecast hour 51 (PT051H) in GRIB2 format (.grib2).

## Variable List

This table provides, for each GRIB2 parameter number: a short description, an alphabetical abbreviation, the levels available for the parameter, and measurement units.

|GRIB2 discipline/category/parameter number | Parameter description |	Abbreviation |	Level |	Units |
|-------------------------------------------|-----------------------|----------------|--------|-------|
|10/2/0 |	Ice cover |	ICEC |	Sfc 	|fraction|
|0/2/2 |	U-Component of Wind |	UGRD |	AGL-10 (10m above ground) |	m/s|
|0/2/3 |	V-Component of Wind |	VGRD |	AGL-10 (10m above ground) |	m/s|
|10/0/3 |	Significant height of combined wind waves and swell |	HTSGW |	Sfc |	m|
|10/0/34 |	Peak wave period |	PWPER |	Sfc |	s|
|10/0/28 |	Mean zero-crossing wave period |	MZWPER |	Sfc |	s|
|10/0/46 |	Peak wave direction |	PWAVEDIR |	Sfc |	degrees true|
|10/0/4 |	Direction of wind waves |	WVDIR |	Sfc |	degrees true|
|10/0/5 |	Significant height of wind waves |	WVHGT |	Sfc |	m|
|10/0/35 |	Peak period of wind waves |	PPERWW |	Sfc |	s|
|10/0/53 |	Mean wave direction of first swell partition |	MWDFSWEL |	Sfc 	|degrees true|
|10/0/47 |	Significant wave height of first swell partition |	SWHFSWEL |	Sfc |	m|
|10/0/65 |	Peak wave period of first swell partition 	|PWPFSWEL |	Sfc |	s|
|10/0/54 |	Mean wave direction of second swell partition |	MWDSSWEL |	Sfc	|degrees true|
|10/0/48 |	Significant wave height of second swell partition |	SWHSSWEL |	Sfc |	m|
|10/0/66 |	Peak wave period of second swell partition 	|PWPSSWEL |	Sfc |	s|

### Notes

* u and v components of the wind vector are to be resolved relative to the defined grid, in the direction of increasing i and j coordinates.

* At each point of the domain, the spectra can be divided between wind sea and a certain number of swells. The two swells that contain the most energy are designated in order as the primary and secondary swell. Wind, sea and swell parameters can be undefined at some grid points, for the former if there is little wind, for the latter if there are only locally generated waves.

## Support

If you have any questions about this data, please contact us at : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).

