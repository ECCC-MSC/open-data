[En français](readme_gewps-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [GEWPS](readme_gewps_en.md) > GEWPS on MSC Datamart

# Global Ensemble Wave Prediction System (GEWPS) data in GRIB2 format

This page describes the [Global Ensemble Wave Prediction System](readme_gewps_en.md) data available in GRIB2 format.

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available via the HTTP protocol. It is possible to access it with a standard browser. In this case, we obtain a list of links giving access to a GRIB2 file.

The data can be accessed at the following URL :

* [https://dd.weather.gc.ca/model_gewps/25km/{HH}/](https://dd.weather.gc.ca/model_gewps/25km)

where :

* __HH__ : Model run start, in UTC [00 or 12]

A history of 24 hours is maintained in this directory.

## Available Domain

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

`{YYYYMMDD}T{HH}Z_MSC_GEWPS_{VAR}_{LVL}_{Grille}{resolution}_PT{hhh}H.grib2`

Where:

* __YYYYMMDD__: Year, month and day of the beginning of the forecast
* __T__ : Time delimiter according to ISO8601 norms
* __HH__: UTC run time [00, 12]
* __Z__ : Time zone (UTC hour)
* __MSC__ : Constant string indicating the Meteorological Service of Canada, source of data
* __GEWPS__ : Constant string indicating that data is from the Global Ensemble Wave Prediction System
* __VAR__ : Variables included in the file
* __LVL__ : Vertical level [Sfc for the surface]
* __Grille__ : Horizontal grid type [LatLon]
* __resolution__ : Indicating resolution in degreee in latitude and longitude directions [0.25]
* __PT{hhh}H__: Forecast hours based on [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) norms. P, T and H are constant character designating Period, Time and Hour. "hhh" is the forecast hour [000, 003, 006, ..., 384]
* __grib2__: constant string indicating the GRIB2 format is used

Example of file name:

20210225T12Z_MSC_GEWPS_HTSGW_Sfc_LatLon0.25_PT015H.grib2

## Variable List

<table id="csv-table" class="display"></table>

<link href="https://cdn.jsdelivr.net/npm/simple-datatables@latest/dist/style.css" rel="stylesheet" type="text/css">
<script src="https://cdn.jsdelivr.net/npm/simple-datatables@latest"></script>
<script src="../../../js/variables_datatable.js" type="text/javascript"></script>
<script>
  loadTable("csv-table", "../../../assets/csv/GEWPS_en.csv");
</script>

## Support

If you have any questions about this data, please contact us at : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Announcements from the dd_info mailing list

Announcements related to this dataset are available in the [dd_info list](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info.comm.collab.science.gc.ca/).
