[En français](readme_raqdps-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [RAQDPS](readme_raqdps_en.md) > Regional Air Quality Deterministic Prediction System on MSC Datamart

# Regional Air Quality Deterministic Prediction System (RAQDPS) data in GRIB2 Format

This page describes the [Regional Air Quality Deterministic Prediction System (RAQDPS)](readme_raqdps_fr.md) GRIB2 data. The system is run twice daily to produce 72-hour forecasts of some pollutants such as hourly ozone (O3), nitrogen dioxide (NO2), or particulate matter with aerodynamic diameter smaller than 2.5 μm (PM2.5) fields on a North American grid. 

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data can be accessed at the following URLs:

* [https://dd.weather.gc.ca/model_raqdps/10km/grib2/{HH}/{hhh}](https://dd.weather.gc.ca/model_raqdps/10km/grib2) 

where:

* __HH__ : Model run start, in UTC [00, 12]
* __hhh__ : Forecast hour [000, 001, 002, ..., 072] 

A history of 24 days of forecast is kept in this directory.

## Technical specification of the grid

![RAQDPS grid image](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_raqdps-fw/grille_raqdps-fw.png)

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

`{YYYYMMDD}T{HH}Z_MSC_RAQDPS_{VAR}_{LVL}_{Grille}(resolution}_PT{hhh}H.grib2`

Where:

* __YYYYMMDD__: Year, month and day of the beginning of the forecast
* __T__ : Time delimiter according to ISO8601 norms
* __HH__: UTC run time [00, 12]
* __Z__ : Time zone (UTC hour)
* __MSC__ : Constant string indicating the Meteorological Service of Canada, source of data
* __RAQDPS__ : Constant string indicating that data is from the Regional Air Quality Deterministic Prediction System 
* __VAR__ : Variable type included in the file [PM2.5, PM10, NO2, NO, O3, SO2]
* __LVL__ : Vertical level [Sfc for the surface, EAtm for the column integral]
* __Grille__ : Horizontal grid rotated lat-lon [RLatLon]
* __resolution__ : Indicating resolution in degreee, here 0.09°x0.09° (about 10km) in latitude and longitude directions [0.09]
* __PT{hhh}H__: Forecast hours based on [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) norms. P, T and H are constant character designating Period, Time and Hour. "hhh" is the forecast hour [000, 001, 002, ..., 072]
* __grib2__: Constant string indicating the GRIB2 format is used

Example of forecast file name:

* 20200521T00Z_MSC_RAQDPS_NO2_Sfc_RLatLon0.09_PT003H.grib2

## List of variables

List of 2D variables available in the files:

* PM2.5: PM2.5 concentration (&mu;g.m-3)
* PM10: PM10 concentration (&mu;g.m-3)
* NO: Nitrogen oxide (ppb)
* NO2: Nitrogen dioxide (ppb)
* O3: Ozone (ppb)
* SO2: Sulfure dioxide (ppb)

## Support

If you have any questions about this data, please contact us at: [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).
