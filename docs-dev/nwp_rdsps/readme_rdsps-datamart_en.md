[En français](readme_rdsps-datamart_fr.md)


![ECCC logo](../../docs/img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [GDWPS](readme_rdsps_en.md) > RDSPS on MSC Datamart


# Global Deterministic Storm Surge Prediction System (RDSPS) data in NetCDF format

This page describes the [Regional Deterministic Storm Surge Prediction System](readme_rdsps_en.md) data available in NetCDF format.

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.


The data is available via the HTTP protocol. It is possible to access it with a standard browser. In this case, we obtain a list of links giving access to a NetCDF file.

The data can be accessed at the following address :

* [https://dd.weather.gc.ca/model_surge/nw-atlantic/netcdf/{HH}/](https://dd.weather.gc.ca/model_surge/nw-atlantic/netcdf)

where :

* __HH__ : Model run start, in UTC [00 or 12]

A history of 24 hours is maintained in this directory.

## Grid technical specification

This table lists the values of different parameters of the RDSPS grid:

| Parameter | Value |
| ------ | ------ |
| ni | 841 |
| nj | 541 |
| resolution | 0.033° x 0.033° |


##    Nomenclature of file directories

NOTE:  ALL HOURS ARE IN UTC.

 (*TODO: implement T, Z in the name*)

File names have the form:

CMC_rdsps_domain_Variable_LevelType_level_latlond.dddxd.ddd_YYYYMMDDTHHZ_Phhh.nc

Where:

* CMC: constant string indicating that the data is from the Canadian Meteorological Centre
* rdsps: constant string indicating that the data is from the Regional Deterministic storm Surge Prediction System
* domain: constant string indicating which domain the data is from
* Variable: Variable type included in this file
* LevelType: Level type
* Level: Level value
* latlond.dddxd.ddd: constant string indicating that the projection used is lat/long at d.ddd x d.ddd degrees resolution
* YYYYMMDD: Year, month and day of the beginning of the forecast
* HH: UTC run time `[00, 06, 12, 18]`
* Phhh : P is a constant character. hhh represents the forecast hour `[000, 001, 002, ..., 240]`
* nc: constant string indicating the NetCDF format is used
* T: time date separator
* Z: time zone indicator (UTC)

Example of file name:

( *TODO: implement SFC - lowercase *)
CMC_rdsps_nw-atlantic_etas_sfc_0_latlon0.033x0.033_20180417T12Z_P024.nc

This file originates from the Canadian Meteorological Center (CMC) and contains
the data of the Regional Deterministic storm Surge Prediction System. The data in the
file start on April 17th 2018 at 12Z (2018041712). It contains the storm surge water level (ETAS) at the surface (SFC_0) on a lat/long grid
at 0.033 degree x 0.033 degree resolution for the forecast hour 24 (P024) in
NetCDF format (.nc).


##  Levels

Levels that may be applicable to a given parameter are:

* sfc: surface




##    Variable list

The list below provides, for each variable: a short description, an alphabetical abbreviation, the levels available for the parameter, and measurement units.

|NetCDF  | Short description|                          Abbr.|  Level|  Units|
|--------|---------------|----------|----------|----------|
|etas    |Storm surge    |                            ETAS|   src_0|    m|



## File contents

The data files are in NetCDF format. The NetCDF files comply with Climate and Forecast (CF) conventions to facilitate
processing and sharing.
Levels that may be applicable to a given parameter are:

NetCDF is a file format for the storage and transport of gridded meteorological
data, such as Numerical Weather Prediction model output. It is designed to be
self-describing, compact and portable across computer architectures.  The NetCDF standard was designed and is maintained by
the University Corporation for Atmospheric Research (UCAR).
* sfc: surface

Information about this format and software to manipulate and display NetCDF data are available here:
https://www.unidata.ucar.edu/software/netcdf/docs/index.html

Climate and Forecast Conventions:
http://cfconventions.org/


## Support

If you have any questions about these data, please contact us at : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Announcements from the dd_info mailing list

Announcements related to this dataset are available in the [dd_info list](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).
