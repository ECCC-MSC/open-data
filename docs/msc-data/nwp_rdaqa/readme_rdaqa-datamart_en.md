[En français](readme_rdaqa-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [RDAQA](readme_rdaqa_en.md) > Regional Deterministic Air Quality Analysis on MSC Datamart

# Regional Deterministic Air Quality Analysis (RDAQA) data in GRIB2 Format

This page describes the [Regional Deterministic Air Quality Analysis (RDAQA)](readme_rdaqa_en.md) GRIB2 data. The system is run hourly to produce analysis of some pollutants such as hourly ozone (O3), nitrogen dioxide (NO2), or particulate matter with aerodynamic diameter smaller than 2.5 μm (PM2.5) fields on a North American grid. 

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data can be accessed at the following URLs:

* [https://dd.weather.gc.ca/today/model_rdaqa/10km/{HH}](https://dd.weather.gc.ca/today/model_rdaqa/10km/) 

where:

* __HH__ : Analysis validity time, in UTC [00, 01, 02, ..., 22, 23]


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

The files have the following nomenclature:

`{YYYYMMDD}T{HH}Z_MSC_{SYSTEM}_{VAR}_{LVLTYPE}_{grid}{resolution}_PT0H.grib2`

where:

* __YYYYMMDD__: Year, month and day of the beginning of the forecast
* __T__ : Time delimiter according to ISO8601 norms
* __HH__: Analysis validity time, in UTC [00, 01, 02, ..., 22, 23]
* __Z__ : Time zone (UTC hour)
* __MSC__ : Constant string indicating that the data is from the Meteorologcal Service of Canada (MSC)
* __SYSTEM__ : Constant string indicating the system from which the analysis was generated [RDAQA; RDAQA-Prelim for the observation cut-off time within one hour of time YYYYMMDDHH, indicating that all observations may not have been collected; RDAQA-FW for analysis generated from the Firework component of the system].
* __VAR__ : Variables included in the file (see section below).
* __LVLTYPE__ : Vertical level type [Sfc for the surface]
* __grid__ : Horizontal grid [RLatLon]
* __resolution__ : Resolution in degree 0.09 (about 10km) in both latitude and longitude directions 
* __PT0H__: Forecast hours based on [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) norms. P, T and H are constant character designating Period, Time and Hour. Here, PTOH indicates an analysis.
* __grib2__ : constant string indicating the GRIB2 format

Examples:

* 20230808T04Z_MSC_RDAQA-Prelim_PM10_Sfc_RLatLon0.09_PT0H.grib2
* 20230808T04Z_MSC_RDAQA_PM10_Sfc_RLatLon0.09_PT0H.grib2
* 20230808T04Z_MSC_RDAQA-FW_PM10_Sfc_RLatLon0.09_PT0H.grib2

## List of variables

List of 2D variables available in the files:

<table id="csv-table" class="display"></table>

<link href="https://cdn.jsdelivr.net/npm/simple-datatables@latest/dist/style.css" rel="stylesheet" type="text/css">
<script src="https://cdn.jsdelivr.net/npm/simple-datatables@latest"></script>
<script src="../../../js/variables_datatable.js" type="text/javascript"></script>
<script>
  loadTable("csv-table", "../../../assets/csv/RDAQA_Variables-List_en.csv");
</script>

## Support

If you have any questions about this data, please [contact us](https://weather.gc.ca/mainmenu/contact_us_e.html).

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).
