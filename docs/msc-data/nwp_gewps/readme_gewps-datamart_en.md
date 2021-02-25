[En français](readme_gewps-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [GEWPS](readme_gewps_en.md) > GEWPS on MSC Datamart

# Global Ensemble Wave Prediction System (GEWPS) data in GRIB2 format

This page describes the experimental [Global Ensemble Wave Prediction System](readme_gewps_en.md) data available in GRIB2 format.

## Data location

MSC testing data repository DD-Alpha data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available via the HTTP protocol. It is possible to access it with a standard browser. In this case, we obtain a list of links giving access to a NetCDF file.

The experimental data can be accessed at the following URL :

* [https://dd.alpha.weather.gc.ca/model_gewps/global/grib2/{HH}/](https://dd.alpha.weather.gc.ca/model_gewps/global/grib2)

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

NOTE:  ALL HOURS ARE IN UTC.

File names have the form:

{YYYYMMDD}T{HH}Z_MSC_GEWPS_VAR_LVL_{grille}{resolution}_PT{hhh}H.grib2

Where:

* __YYYYMMDD__: Year, month and day of the beginning of the forecast
* __T__ : Time delimiter according to ISO8601 norms
* __HH__: UTC run time [00, 12]
* __Z__ : Time zone (UTC hour)
* __MSC__ : Constant string indicating the Meteorological Service of Canada, source of data
* __GEWPS__ : Constant string indicating that data is from the Global Ensemble Wave Prediction System
* __VAR__ : Variables included in the file
* __LVL__ : Vertical level [SFC for the surface]
* __grille__ : Horizontal grid type [LatLon]
* __resolution__ : Indicating resolution in degreee in latitude and longitude directions [0.25x0.25]
* __PT{hhh}H__: Forecast hours based on [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) norms. P, T and H are constant character designating Period, Time and Hour. "hhh" is the forecast hour [000, 003, 006, ..., 384]
* __grib2__: constant string indicating the GRIB2 format is used

Example of file name:

20210225T12Z_MSC_GEWPS_HTSGW_SFC_LatLon0.25x0.25_PT015H.grib2

## Variable List

This table provides, for each GRIB2 parameter number: a short description, an alphabetical abbreviation, the levels available for the parameter, and measurement units.

|GRIB2 discipline/category/parameter number | Parameter description |	Abbreviation |	Level |	Units |
|-------------------------------------------|-----------------------|----------------|--------|-------|
|10/0/3 |	Significant height of combined wind waves and swell |	HTSGW |	SFC |	m|
|10/0/34 |	Peak wave period |	PWPER |	SFC |	s|
|10/0/28 |	Mean zero-crossing wave period |	MZWPER |	SFC |	s|
|10/0/46 |	Peak wave direction |	PWAVEDIR |	SFC |	degrees true|
|10/0/4 |	Direction of wind waves |	WVDIR |	SFC |	degrees true|
|10/0/5 |	Significant height of wind waves |	WVHGT |	SFC |	m|
|10/0/35 |	Peak period of wind waves |	PPERWW |	SFC |	s|
|10/0/53 |	Mean wave direction of first swell partition |	MWDFSWEL |	SFC 	|degrees true|
|10/0/47 |	Significant wave height of first swell partition |	SWHFSWEL |	SFC |	m|
|10/0/65 |	Peak wave period of first swell partition 	|PWPFSWEL |	SFC |	s|
|10/0/54 |	Mean wave direction of second swell partition |	MWDSSWEL |	SFC 	|degrees true|
|10/0/48 |	Significant wave height of second swell partition |	SWHSSWEL |	SFC |	m|
|10/0/66 |	Peak wave period of second swell partition 	|PWPSSWEL |	SFC |	s|

## Support

If you have any questions about this data, please contact us at : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Announcements from the dd_info mailing list

Announcements related to this dataset are available in the [dd_info list](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).
