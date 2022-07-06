[In French](readme_caldas-nsrps-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC Open Data](../readme_en.md) > [CaLDAS-NSRPS](readme_caldas-nsrps_en.md) > CaLDAS-NSRPS on MSC Datamart 

# The Canadian Land Data Assimilation System in the National Surface and River Prediction System (CaLDAS-NSRPS) data in NetCDF format

This page describes the experimental [The Canadian Land Data Assimilation System](./readme_caldas-nsrps-datamart_en.md) data available in NetCDF format on the MSC testing data repository DD-Alpha.

## Data location 

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available using the HTTPS protocol and resides in a directory that is plainly accessible to a web browser. Visiting that directory with an interactive browser will yield a raw listing of links, each link being a downloadable NetCDF file.

The data can be accessed at the following URLs:

* [https://dd.alpha.meteo.gc.ca/model_nsrps-caldas/2.5km/{HH}/](https://dd.alpha.meteo.gc.ca/model_hrdlps/2.5km)                  

where:

* __HH__ : Model run start, in UTC [00,03,06,09,12,15,18,21]

A 24h history is kept in this directory.

## Technical specification of the grid

![Image of the CaLDAS-NSRPS domain](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_caldas-nsrps/grille_hrdlps.png) ... _To be completed_ ...

The table below lists the values of the rotated latitude-longitude grid parameters:

| Parameter | Value |
| ------ | ------ |
| ni | _2578_ |
| nj | _1328_ |
| resolution along the rotated equator | 2.5km |

## Filename nomenclature

NOTE: ALL HOURS ARE IN UTC.

The files have the following nomenclature: 

`{YYYYMMDD}T{HH}Z_MSC_NSRPS-CaLDAS_{VAR}_{LVLTYPE}-{LVL}_{grid}{resolution}_PT{hhh}H.nc`

where:

* __YYYYMMDD__: Year, month and day of the beginning of the forecast
* __T__ : Time delimiter according to ISO8601 norms
* __HH__: UTC run time [00, 12]
* __Z__ : Time zone (UTC hour)
* __MSC__ : Constant string indicating that the data is from the Meteorologcal Service of Canada (MSC)
* __NSRPS-CaLDAS__ : Constant string indicating that the data is from The Canadian Land Data Assimilation System in the National Surface and River Prediction SystemThe Canadian Land Data Assimilation System
* __VAR__ : Variables included in the file (see section below). This parameter includes also the statistical measure, if relevant (ex: Accum143h for an accumulation over 143 hours).
* __LVLTYPE__ : Vertical level type [Sfc for the surface, DBS for depth below the surface, AGL for fixed height above ground]
* __LVL__ : Vertical levels values are listed in the table below  
* __grid__ : Horizontal grid [RLatLon]
* __resolution__ : Resolution in degree 0.0225 (about 2.5km) in both latitude and longitude directions 
* __PT{hhh}H__: Forecast hours based on [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) norms. P, T and H are constant character designating Period, Time and Hour. "hhh" is the forecast hour [000,001,002, ...,144]
* __nc__ : constant string indicating the NetCDF format

Examples:

* 20220307T00Z_MSC_NSRPS-CaLDAS_AirTemp_AGL-1.5m_RLatLon0.0225_PT0H.nc
* 20220307T00Z_MSC_NSRPS-CaLDAS_Dewpoint_AGL-1.5m_RLatLon0.0225_PT0H.nc
* 20220307T00Z_MSC_NSRPS-CaLDAS_RadiativeTemp_Sfc_RLatLon0.0225_PT0H.nc
* 20220307T00Z_MSC_NSRPS-CaLDAS_SoilLiquidWaterCont_DBS-all_RLatLon0.0225_PT0H.nc


## List of variables 

List of variables available in the files:

|Name   | Description|  Level|                          Depth [m]/ Height [m]|  Output Frequency|  Units|
|---------|---------------|----------|----------|----------|----------|
|tt     |Air Temperature                            |   AGL|    1.5|    hourly|    K|
|td      |Dew Point Temperature |   AGL|     1.5|    hourly|    K|
|tg      |Aggregate Surface Radiative Temperature |   Sfc|     0.0|    hourly|    K|
|wsol      |Volumetric Water Content of Soil |   DBS|     0.025, 0.075, 0.150, 0.300, 0.700, 1.500, 2.500|    hourly|    m3 m-3|

Notes: DBS - Depth Below Surface; AGL - Above Ground Level; Sfc - Surface 

## Support

If you have any questions about this data, please contact us at: [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Announcements from the dd_info mailing list

Announcements related to this dataset are available in the [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).

