[En français](readme_rewps-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [REWPS](readme_rewps_en.md) > REWPS on MSC Datamart

# Regional Ensemble Wave Prediction System (REWPS) Data in GRIB2 Format

This page describes the data of the [Regional Ensemble Wave Prediction System](readme_rewps_en.md).

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available using the HTTPS protocol and resides in a directory that is plainly accessible to a web browser. Visiting that directory with an interactive browser will yield a raw listing of links, each link being a downloadable GRIB2 file.

The data can be accessed at the following address :

* [https://dd.weather.gc.ca/model_rewps/great-lakes/grib2/{HH}/](https://dd.weather.gc.ca/model_rewps/great-lakes/grib2)

where :

* __HH__ : Model run start, in UTC [00, 12]

A 24-hour history is stored in this directory.

## Grid technical specification

The REWPS data are available on the Great Lakes domain.

![Image de la grille du SRPEV](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_rewps/grille_rewps_grl.png)

This table lists the values of different parameters of the REWPS grid:

| Parameter | Value |
| ------ | ------ |
| ni | 550 |
| nj | 365 |
| resolution | 0.0224° x 0.0310° |
| coordinate of first grid point | 41.0984° N  92.4790° O |


## File name nomenclature

NOTE:  ALL HOURS ARE IN UTC.

File names have the form:

`{YYYYMMDD}T{HH}Z_MSC_REWPS-{DOMAIN}_{VAR}_{LVL}_{Grille}{resolution}_PT{hhh}H.grib2`

Where:

* __YYYYMMDD__: Year, month and day of the beginning of the forecast
* __T__ : Time delimiter according to ISO8601 norms
* __HH__: UTC run time [00, 12]
* __Z__ : Time zone (UTC hour)
* __MSC__ : Constant string indicating the Meteorological Service of Canada, source of data
* __REWPS__ : Constant string indicating that data is from the Regional Ensemble Wave Prediction System
* __DOMAIN__ : String indicating which domain the data is from [Great-Lakes]
* __VAR__ : Variables included in the file
* __LVL__ : Vertical level [Sfc for the surface]
* __Grille__ : Horizontal grid type [LatLon]
* __resolution__ : Indicating resolution in degreee in latitude and longitude direction [0.022x0.031]
* __PT{hhh}H__: Forecast hours based on [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) norms. P, T and H are constant character designating Period, Time and Hour. "hhh" is the forecast hour [000, 003, 006, ..., 072].
* __grib2__: constant string indicating the GRIB2 format is used

Example of file name:

20210202T12Z_MSC_REWPS-Great-Lakes_HTSGW_Sfc_LatLon0.022x0.031_PT066H.grib2

## Variable List

<table id="csv-table" class="display"></table>

<link href="https://cdn.jsdelivr.net/npm/simple-datatables@latest/dist/style.css" rel="stylesheet" type="text/css">
<script src="https://cdn.jsdelivr.net/npm/simple-datatables@latest"></script>
<script src="../../../js/variables_datatable.js" type="text/javascript"></script>
<script>
  loadTable("csv-table", "../../../assets/csv/REWPS_en.csv");
</script>

## Support

If you have any questions about this data, please contact us at : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Announcements from the dd_info mailing list

Announcements related to this dataset are available in the [dd_info list](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).


