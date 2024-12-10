[En français](readme_gdsps-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [GDSPS](readme_gdsps_en.md) > GDSPS on MSC Datamart

# Global Deterministic Storm Surge Prediction System (GDSPS) data in NetCDF format

This page describes the [Global Deterministic Storm Surge Prediction System](readme_gdsps_en.md) data available in NetCDF format.

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available via the HTTP protocol. It is possible to access it with a standard browser. In this case, we obtain a list of links giving access to a NetCDF file.

The data can be accessed at the following address :

* [https://dd.weather.gc.ca/model_gdsps/15km/{HH}/](https://dd.weather.gc.ca/model_gdsps/15km)

where :

* __HH__ : Model run start, in UTC [00 or 12]

## Available domain

Global latitude-longitude grid.

| Parameter | Value |
| ------ | ------ |
| ni | 1801 |
| nj | 1251 |
| resolution | 0.144° x 0.200° |

##    Nomenclature of file directories

NOTE: ALL HOURS ARE IN UTC.

File names have the form:

`{YYYYMMDD}T{HH}Z_MSC_GDSPS_{VAR}_{LVL}_{grille}{resolution}_PT{hhh}H.nc`

Where:

* __YYYYMMDD__: Year, month and day of the beginning of the forecast
* __T__ : Time delimiter according to ISO8601 norms
* __HH__: UTC run time [00, 12]
* __Z__ : Time zone (UTC hour)
* __MSC__ : Constant string indicating the Meteorological Service of Canada, source of data
* __GDSPS__ : Constant string indicating that data is from the Global Deterministic Storm Surge Prediction System 
* __VAR__ : Variable type included in the file [ETAS, SSH]
* __LVL__ : Vertical level [Sfc for the surface]
* __grille__ : Horizontal grid lat-lon [LatLon]
* __resolution__ : Indicating resolution in degreee in latitude and longitude directions [0.144x0.200] 
* __PT{hhh}H__: Forecast hours based on [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) norms. P, T and H are constant character designating Period, Time and Hour. "hhh" is the forecast hour [000, 001, 002, ..., 240]
* __nc__: constant string indicating the NetCDF format is used

Example of file name:

20180417T12Z_MSC_GDSPS_ETAS_Sfc_LatLon0.144x0.200_PT024H.nc

## Variable list

<table id="csv-table" class="display"></table>

<link href="https://cdn.jsdelivr.net/npm/simple-datatables@latest/dist/style.css" rel="stylesheet" type="text/css">
<script src="https://cdn.jsdelivr.net/npm/simple-datatables@latest"></script>
<script src="../../../js/variables_datatable.js" type="text/javascript"></script>
<script>
  loadTable("csv-table", "../../../assets/csv/GDSPS_Variables-List_en.csv");
</script>

__NOTE__ :

* Total water level (`zos`) is relative to Mean Water Level (MWL) as defined by the average the total water level over the last 365 days of pseudo-analysis.
* During the post-processing phase, storm surge elevation (`etas`) is derived from total water level (`zos`) by harmonic analysis using t_tide (Foreman et al. 2009). The storm surge elevation has been computed for the [150W, 40W] X [40 N, 80 N] region around Canada and for a band 100 km wide along the shore worldwide. Elsewhere, `etas` is masked. The model tidal heights can be obtained by taking the difference `zos-etas` where `etas` is defined.

## Support

If you have any questions about this data, please [contact us](https://weather.gc.ca/mainmenu/contact_us_e.html).

## Announcements from the dd_info mailing list

Announcements related to this dataset are available in the [dd_info list](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).
