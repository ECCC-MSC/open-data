[In French](readme_hrdlps-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC Open Data](../readme_en.md) > [HRDLPS](readme_hrdlps_en.md) > HRDLPS on MSC Datamart 

# High Resolution Deterministic Land Surface Prediction System (HRDLPS) data in NetCDF format

This page describes the experimental [High Resolution Deterministic Land Surface Prediction System](./readme_hrdlp-datamart_en.md) data available in NetCDF format on the MSC testing data repository DD-Alpha.

## Data location 

MSC testing data repository DD-Alpha can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available using the HTTPS protocol and resides in a directory that is plainly accessible to a web browser. Visiting that directory with an interactive browser will yield a raw listing of links, each link being a downloadable NetCDF file.

The data can be accessed at the following URLs:

* [https://dd.alpha.weather.gc.ca/model_hrdlps/2.5km/{HH}/{hhh}/](https://dd.weather.meteo.gc.ca/model_hrdlps/2.5km)                  

where:

* __HH__ : Model run start, in UTC [00, 12]
* __hhh__ : Forecast hour [000, 001, ..., 144] 

A 24h history is kept in this directory.

## Technical specification of the grid

![Image of the HRDLPS domain](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_hrdlps/grille_hrdlps.png) 

The table below lists the values of the rotated latitude-longitude grid parameters:

| Parameter | Value |
| ------ | ------ |
| ni | 2540 |
| nj | 1290 |
| resolution at 45° N | 2.5 km |

## Filename nomenclature


The files have the following nomenclature: 

`{YYYYMMDD}T{HH}Z_MSC_HRDLPS_{VAR}_{LVLTYPE}-{LVL}_{grid}{resolution}_PT{hhh}H.nc`

where:

* __YYYYMMDD__: Year, month and day of the beginning of the forecast
* __T__ : Time delimiter according to ISO8601 norms
* __HH__: UTC run time [00, 06, 12, 18]
* __Z__ : Time zone (UTC hour)
* __MSC__ : Constant string indicating that the data is from the Meteorologcal Service of Canada (MSC)
* __HRDLPS__ : Constant string indicating that the data is from High Resolution Deterministic Land Surface Prediction System
* __VAR__ : Variables included in this file (see section below). This parameter includes also the statistical measure, if relevant (ex: Accum143h pour an accumulation over 143 hours).
* __LVLTYPE__ : Vertical level type [Sfc for the surface, DBS for depth below the surface, AGL for fixed height above ground]
* __LVL__ : Vertical level value [10 m, 0.5 m, 1.5 m, 2 m, `0-2m` from surface to 2 meters]
* __grid__ : Horizontal grid [RLatLon]
* __resolution__ : Resolution in degree 0.0225 (about 2.5 km) in both latitude and longitude directions 
* __PT{hhh}H__: Forecast hours based on [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) norms. P, T and H are constant character designating Period, Time and Hour. "hhh" is the forecast hour [000, 001, 002, ..., 144]
* __nc__ : constant string indicating the NetCDF format

Examples:

* 20210927T00Z_MSC_HRDLPS_AirTemp_AGL-1.5m_RLatLon0.0225_PT143H.nc
* 20210927T00Z_MSC_HRDLPS_Runoff-Accum143h_DBS-0-2m_RLatLon0.0225_PT143H.nc

## List of variables 

List of variables available in the files: 

|Name   | Description|  Level|    Units|
|---------|---------------|----------|----------|
|tj     |Air Temperature                            |   AGL|     K|
|tdk      |Dew Point Temperature |   AGL|    K|
|acwf      |Land Surface Evaporation Amount |   Sfc|     kg.m-2|
|tg      |Aggregate Surface Radiative Temperature |   Sfc|       K|
|traf      |Surface Runoff Amount |   Sfc|     kg.m-2|
|wt      |Surface Area Fraction |   Sfc|   1|
|mf      |Model Orography |   Sfc|      m|
|wsol      |Volumetric Water Content of Soil |   DBS|    m3.m-3|
|o1      |Drainage Amount Through Base of Soil Model |   DBS|     kg.m-2|
|alat      |Lateral Subsurface Runoff Amount |   DBS|     kg.m-2|


## Support

If you have any questions about this data, please contact us at: [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Announcements from the dd_info mailing list

Announcements related to this dataset are available in the [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).

