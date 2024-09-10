[En français](readme_hrdpa-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [HRDPA](readme_hrdpa_en.md) > HRDPA on MSC Datamart

# High Resolution Deterministic Precipitation Analysis (HRDPA) Data in GRIB2 Format

This page describes the [High Resolution Deterministic Precipitation Analysis](./readme_hrdpa-datamart_en.md) data available in GRIB2 format.

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available using the HTTPS protocol and resides in a directory that is plainly accessible to a web browser. Visiting that directory with an interactive browser will yield a raw listing of links, each link being a downloadable GRIB2 file.

The data can be accessed at the following URL :

*  [https://dd.weather.gc.ca/model_hrdpa/2.5km/{HH}](https://dd.weather.gc.ca/model_hrdpa/2.5km)

where :

* __HH__ :  UTC run time [00, 06, 12, 18]

A history of 30 days is maintained in this directory.

## Grid specifications of the grid

![Rlatlon HRDPA grid](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_hrdpa/grille_hrdpa_rlatlon.png)

The following table lists the values of various parameters of the rotated lat-lon grid:

| Parameter | Valeur |
| ------ | ------ |
| ni | 2538 |
| nj | 1288 | 
| resolution at 60° N | 2.5 km |
| coordinate of the first grid point | -36.09° N ; 114.70° W |

__Note__ : The [most recent versions of wgrib2](https://www.cpc.ncep.noaa.gov/products/wesley/wgrib2/update_2.0.8.html) and [GDAL](https://gdal.org/) support these rotated grids.

## File name nomenclature 

Files have one of the following nomenclatures:

* {YYYYMMDD}T{HH}Z_MSC_HRDPA_{VAR}_Sfc_RLatLon0.0225_PT0H.grib2
* {YYYYMMDD}T{HH}Z_MSC_HRDPA-Prelim_{VAR}_Sfc_RLatLon0.0225_PT0H.grib2

where:

* __YYYYMMDD__: Year, month and day of the beginning of the forecast
* __T__ : Time delimiter according to ISO8601 norms
* __HH__: UTC run time [00, 06, 12, 18]
* __Z__ : Time zone (UTC hour)
* __MSC__ : Constant string indicating the Meteorological Service of Canada, source of data
* __HRDPA__ : Constant string indicating that data is from the High Resolution Deterministic Precipitation Analysis. Observation cut-off time is about 007 hours after the time YYYYMMDDHH indicating that a maximum of observations has likely been collected
* __HRDPA-Prelim__: Constant string indicating that data is from the High Resolution Deterministic Precipitation Analysis. Observation cut-off time is one hour after the time YYYYMMDDHH indicating that possibly not all observations have been collected
* __VAR__ : Constant string indicating the variable included in the file namely in this case, the accumulated precipitation which has been analyzed over a specific period [APCP-Accum6h, APCP-Accum24h]
* __Sfc__ : Constant string indicating that the surface is the vertical level 
* __RLatLon0.0225__ : Constant string indicating a rotated lat-lon grid with 0.0225 deg resolution (about 2.5km)
* __PT0H__ : Based on ISO8601 norms. P, T and H are constant character designating Period, Time and Hour. Here PT0H indicates an analysis.
* __grib2__ : constant string indicating the GRIB2 format is used

Examples of files names :

* 20231106T00Z_MSC_HRDPA-Prelim_APCP-Accum6h_Sfc_RLatLon0.0225_PT0H.grib2

The file originates from the Meteorological Service of Canada (MSC) and contains a High Resolution Deterministic Precipitation Analysis (HRDPA). It contains a preliminary analysis of precipitation accumulation represented by the APCP variable over a 6 hour interval. The data are on a lat-lon rotated grid at a 2.5 km resolution (RLatLon0.0225). The analysis was produced on November 6, 2023 at 00Z (20231106T00Z). The 006-hour interval in which the precipitation is analyzed is 2023110600 to 2023110606. 

* 20231106T12Z_MSC_HRDPA_APCP-Accum24h_Sfc_RLatLon0.0225_PT0H.grib2


The file originates from the Meteorological Service of Canada (MSC) and contains a High Resolution Deterministic Precipitation Analysis (HRDPA). It contains a final analysis of precipitation accumulation represented by the APCP variable over a 24-hour interval. The data are on a lat-lon grid rotated to a 2.5 km resolution (RLatLon0.0225). The analysis was produced on November 6, 2023 at 12Z (20231106T12Z). The 24-hour interval in which precipitation is analyzed is 2023110612 to 2023110712.

__NOTE__: A second variable is also included in this file and it is the confidence index for the analysis.


## List of variables

<table id="csv-table" class="display"></table>

<link href="https://cdn.jsdelivr.net/npm/simple-datatables@latest/dist/style.css" rel="stylesheet" type="text/css">
<script src="https://cdn.jsdelivr.net/npm/simple-datatables@latest"></script>
<script src="../../../js/variables_datatable.js" type="text/javascript"></script>
<script>
  loadTable("csv-table", "../../../assets/csv/HRDPA_Variables-List_en.csv");
</script>

## Support

If you have any questions about this data, please [contact us](https://weather.gc.ca/mainmenu/contact_us_e.html)

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).
