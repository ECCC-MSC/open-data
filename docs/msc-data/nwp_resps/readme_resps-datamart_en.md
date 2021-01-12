[En français](readme_resps-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [RESPS](readme_resps_en.md) > RESPS on MSC Datamart

# Regional Ensemble Storm Surge Prediction System (RESPS) data in NetCDF format

This page describes the [Regional Ensemble Storm Surge Prediction System](readme_resps_en.md) data available in NetCDF format.

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available via the HTTP protocol. It is possible to access it with a standard browser. In this case, we obtain a list of links giving access to a NetCDF file.

The data can be accessed at the following address :

* [https://dd.alpha.weather.gc.ca/model_resps/atlantic-nw/netcdf/{HH}/](https://dd.alpha.weather.gc.ca/model_resps/atlantic-nw/netcdf)

where :

* __HH__ : Model run start, in UTC [00 or 12]

A history of 24 hours is maintained in this directory.

## Grid technical specification

This table lists the values of different parameters of the RESPS grid:

| Parameter | Value |
| ------ | ------ |
| ni | 333 |
| nj | 217 |
| resolution | 0.083° x 0.083° |


##    Nomenclature of file directories

NOTE:  ALL HOURS ARE IN UTC.

File names have the form:

{YYYYMMDD}T{HH}Z_MSC_RESPS-Atlantic-North-West_VAR_LVL_{Grille}{resolution}_P{hhh}.nc 

Where:

* __YYYYMMDD__: Year, month and day of the beginning of the forecast
* __T__ : Time delimiter according to ISO8601 norms
* __HH__: UTC run time [00, 12]
* __Z__ : Time zone (UTC hour)
* __MSC__ : Constant string indicating the Meteorological Service of Canada, source of data
* __RESPS-Atlantic-North-West__ : Constant string indicating that data is from the Regional Ensemble Storm Surge Prediction System over the North-West domain
* __VAR__ : Variable type included in the file [ETAS]
* __LVL__ : Vertical level [SFC for the surface]
* __Grille__ : Horizontal grid lat-lon [LatLon]
* __Resolution__ : 0.083x0.083. Indicating resolution in degreee 0.083x0.083 in latitude and longitude directions
* __Phhh__: P is a constant character. hhh is the forecast hour [000, 001, 002, ..., 240]
* __nc__: constant string indicating the NetCDF format is used

Example of file name:

20180417T12Z_MSC_RESPS-Atlantic-North-West_ETAS_SFC_LatLon0.083x0.083_P024.nc

##    Variable list

The list below provides, for each variable: a short description, an alphabetical abbreviation, the levels available for the parameter, and measurement units.

|NetCDF  | Short description|                          Abbr.|  Level|  Units|
|--------|---------------|----------|----------|----------|
|etas    |Storm surge    |                            ETAS|   SFC|    m|
|zos     |Total water level|                            SSH|   SFC|    m|


## Support

If you have any questions about this data, please contact us at : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Announcements from the dd_info mailing list

Announcements related to this dataset are available in the [dd_info list](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).
