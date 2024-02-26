[En français](readme_rdwps-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [RDWPS](readme_rdwps_en.md) > RDWPS on MSC Datamart

# Regional Deterministic Wave Prediction System (RDWPS) Data in GRIB2 Format

This page describes the data of the [Regional Deterministic Wave Prediction System](readme_rdwps_en.md) data available in GRIB2 format.

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available using the HTTPS protocol and resides in a directory that is plainly accessible to a web browser. Visiting that directory with an interactive browser will yield a raw listing of links, each link being a downloadable GRIB2 file.

The data can be accessed at the following URLs :

Lat-lon grids:

* [https://dd.weather.gc.ca/model_rdwps/erie/1km/{HH}/](https://dd.weather.gc.ca/model_rdwps/erie/1km)
* [https://dd.weather.gc.ca/model_rdwps/huron-michigan/1km/{HH}/](https://dd.weather.gc.ca/model_rdwps/huron-michigan/1km)
* [https://dd.weather.gc.ca/model_rdwps/ontario/1km/{HH}/](https://dd.weather.gc.ca/model_rdwps/ontario/1km)
* [https://dd.weather.gc.ca/model_rdwps/superior/1km/{HH}/](https://dd.weather.gc.ca/model_rdwps/superior/1km)

Rotated lat-lon grid:

* [https://dd.meteo.gc.ca/model_rdwps/national/2.5km/{HH}/](https://dd.meteo.gc.ca/model_rdwps/national/2.5km)

where :

* __HH__ : Model run start, in UTC [00, 06, 12, 18]

A 24-hour history is stored in this directory.

Note: The national domain is a post-processed composite of all the RDWPS domains.

## Available Domains

### Lake Superior

* __Lat-lon grid__

![](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_rdwps/grille_rdwps_sup.png)

| Parameter | Value |
| ------ | ------ |
| ni | 658 |
| nj | 318 | 
| resolution | 0.0090° x 0.0124° |
| coordinate of first grid point | 46.2590° N  92.3116° W |

### Lake Huron and Michigan

* __Lat-lon grid__

![](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_rdwps/grille_rdwps_hum.png)

| Parameter | Value |
| ------ | ------ |
| ni | 698 |
| nj | 573 | 
| resolution | 0.0090° x 0.0124° |
| coordinate of first grid point | 41.4260° N  88.1452° W |

### Lake Erie

* __Lat-lon grid__

![](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_rdwps/grille_rdwps_erie.png)

| Parameter | Value |
| ------ | ------ |
| ni | 398 |
| nj | 210 | 
| resolution | 0.0090° x 0.0124° |
| coordinate of first grid point | 41.2190° N  83.6068° W |

### Lake Ontario

* __Lat-lon grid__

![](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_rdwps/grille_rdwps_ont.png)

| Parameter | Value |
| ------ | ------ |
| ni | 348 |
| nj | 158 | 
| resolution | 0.0090° x 0.0124° |
| coordinate of first grid point | 43.0640° N  79.9736° W |

### National

* __Rotated lat-lon grid__

![](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_rdwps/grille_rdwps_nat.png)

| Parameter | Value |
| ------ | ------ |
| ni | 2536 |
| nj | 1286 | 
| resolution | 0.0225° x 0.0225° |
| coordinate of first grid point | 39.681° N  226.410° W | 


## File name nomenclature 

NOTE: ALL HOURS ARE IN UTC.

The files have the following nomenclature :

`{YYYYMMDD}T{HH}Z_MSC_RDWPS-{DOMAIN}_{VAR}_{LVL}_{Grid}{resolution}_PT{hhh}H.grib2`

where :

* __YYYYMMDD__: Year, month and day of the beginning of the forecast
* __T__ : Time delimiter according to ISO8601 norms
* __HH__: UTC run time [00, 12]
* __Z__ : Time zone (UTC hour)
* __MSC__ : Constant string indicating the Meteorological Service of Canada, source of data
* __RDWPS__ : Constant string indicating that data is from the Regional Deterministic Wave Prediction System
* __DOMAIN__ : Constant string indicating the domain [erie, huron-michigan, ontario, superior, national]
* __VAR__ : Variables included in the file
* __LVL__ : Vertical level [Sfc for the surface, AGL for fixed height above ground]
* __Grid__ : Horizontal grid type [LatLon, RLatLon]
* __resolution__ : Indicating resolution in degreee in latitude and longitude directions [0.009x0.012, 0.045, 0.0225]
* __PT{hhh}H__: Forecast hours based on [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) norms. P, T and H are constant character designating Period, Time and Hour. "hhh" is the forecast hour [000, 001, 002, ..., 048]
* __grib2__: constant string indicating the GRIB2 format is used

NOTE: No domain is specified in the filenames for the national domain

Examples of file name :

* 20211014T00Z_MSC_RDWPS-Lake-Erie_HTSGW_Sfc_LatLon0.009x0.012_PT003H.grib2
* 20211014T00Z_MSC_RDWPS_VGRD_AGL-10m_RLatLon0.0225_PT037H.grib2

## Levels

Levels that may be applicable to a given parameter are :

* Surface [Sfc]
* Fixed height above ground [AGL]

## List of variables

<table id="csv-table" class="display"></table>

<link href="https://cdn.jsdelivr.net/npm/simple-datatables@latest/dist/style.css" rel="stylesheet" type="text/css">
<script src="https://cdn.jsdelivr.net/npm/simple-datatables@latest"></script>
<script src="../../../js/variables_datatable.js" type="text/javascript"></script>
<script>
  loadTable("csv-table", "../../../assets/csv/RDWPS_Variables-List_en.csv");
</script>

### Notes

* u and v components of the wind vector are to be resolved relative to the defined grid, in the direction of increasing i and j coordinates.

* At each point of the domain, the spectra can be divided between wind sea and a certain number of swells. The two swells that contain the most energy are designated in order as the primary and secondary swell. Wind, sea and swell parameters can be undefined at some grid points, for the former if there is little wind, for the latter if there are only locally generated waves.

## Support

If you have any questions about this data, please [contact us](https://weather.gc.ca/mainmenu/contact_us_e.html).

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).
