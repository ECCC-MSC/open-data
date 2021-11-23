[En français](readme_raqdps-fw-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [RAQDPS-FW](readme_raqdps-fw_en.md) > Regional Air Quality Deterministic Prediction System FireWork on MSC Datamart

# Regional Air Quality Deterministic Prediction System FireWork (RAQDPS-FW) data in GRIB2 Format

This page describes data from the FireWork system, an air quality forecasting system incorporating emissions from forest fires. The system is run twice a day, initialized at 00:00 and 12:00 UTC, in conjunction with the Regional Air Quality Deterministic Prediction System (RAQDPS). Forest fire emissions are estimated using data on hotspots and fuel consumed on Canadian and U.S. lands provided by Natural Resources Canada's [Canadian Wildland Fire Information System](http://cwfis.cfs.nrcan.gc.ca/). The hotspot data set is downloaded twice daily, prior to the FireWork system running. This system has the advantage of presenting the complete emissions inventory as well as added intermittent fire sources.

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data can be accessed at the following URLs:

* [https://dd.weather.gc.ca/model_raqdps-fw/10km/grib2/{HH}/{hhh}](https://dd.weather.gc.ca/model_raqdps-fw/10km/grib2) 

where:

* __HH__ : Model run start, in UTC [00, 12]
* __hhh__ : Forecast hour [000, 001, 002, ..., 072] 

A history of 24 days of forecast is kept in this directory.

## Technical specification of the grid

![RAQDPS-FW grid image](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_raqdps-fw/grille_raqdps-fw.png)

Table lists the values of various parameters of the rotated lat-lon grid:

| Parameter | Value |
| ------ | ------ |
| ni | 729 |
| nj | 599 | 
| resolution at 60° N | 10 km |
| coordinate of first grid point (with respect to the used grid) | 32 ° S ; 39.5 ° W |

__Note__ : The [most recent versions of wgrib2](https://www.cpc.ncep.noaa.gov/products/wesley/wgrib2/update_2.0.8.html) and [GDAL](https://gdal.org/) support these rotated grids.

## File nomenclature

NOTE: ALL HOURS ARE IN UTC.

The files have the following nomenclature:

* {YYYYMMDD}T{HH}Z_MSC_RAQDPS-FW_VAR_LVL_{Grille}(resolution}_PT{hhh}H.grib2

Where:

* __YYYYMMDD__: Year, month and day of the beginning of the forecast
* __T__ : Time delimiter according to ISO8601 norms
* __HH__: UTC run time [00, 12]
* __Z__ : Time zone (UTC hour)
* __MSC__ : Constant string indicating the Meteorological Service of Canada, source of data
* __RAQDPS-FW__ : Constant string indicating that data is from the Regional Air Quality Deterministic Prediction System FireWork
* __VAR__ : Variable type included in the file (ex. : PM2.5-Diff-RAQDPS)
* __LVL__ : Vertical level [Sfc for the surface, EAtm for the column integral]
* __Grille__ : Horizontal grid rotated lat-lon [RLatLon]
* __resolution__ : Indicating resolution in degreee, here 0.09°x0.09° (about 10km) in latitude and longitude directions [0.09]
* __PT{hhh}H__: Forecast hours based on [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) norms. P, T and H are constant character designating Period, Time and Hour. "hhh" is the forecast hour [000, 001, 002, ..., 072]
* __grib2__: Constant string indicating the GRIB2 format is used

Example of forecast file name:

* 20200521T00Z_MSC_RAQDPS-FW_PM2.5-Diff-RAQDPS_EAtm_RLatLon0.09_PT003H.grib2

## List of variables

List of 2D variables available in the files:

* PM2.5: PM2.5 concentration (&mu;g.m-3)
* PM2.5-Diff-RAQDPS : PM2.5 concentration (&mu;g.m-3) difference with the RAQDPS model. Indicates the forest fires contribution to the PM2.5 concentration
* PM10: PM10 concentration (&mu;g.m-3)
* PM10-Diff-RAQDPS : PM10 concentration (&mu;g.m-3) difference with the RAQDPS model. Indicates the forest fires contribution to the PM10 concentration

## Support

If you have any questions about this data, please contact us at: [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).
