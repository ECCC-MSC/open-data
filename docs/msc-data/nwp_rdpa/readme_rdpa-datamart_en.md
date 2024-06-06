[En français](readme_rdpa-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [RDPA](readme_rdpa_en.md) > RDPA on MSC Datamart

# Regional Deterministic Precipitation Analysis (RDPA - CaPA) data in GRIB2 format

This page describes the [Regional Deterministic Precipitation Analysis (RDPA)](readme_rdpa_en.md) data based on the Canadian Precipitation Analysis (CaPA) system. 

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available using the HTTPS protocol and resides in a directory that is plainly accessible to a web browser. Visiting that directory with an interactive browser will yield a raw listing of links, each link being a downloadable GRIB2 file.

Data on a rotated lat-lon grid can be accessed at the following URL :

* [https://dd.weather.gc.ca/model_rdpa/10km/{HH}](https://dd.weather.gc.ca/model_rdpa/10km)

where :

* __hh__ : time interval of 06 or 24 hours in which precipitation accumulations are analyzed
* __HH__ :  UTC run time [00, 06, 12, 18]

A 30-day history is kept on the MSC Datamart.

## Technical specification of the grid

![Rlatlon RDPA grid](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_rdpa/grille_RDPA.png)

The following table lists the values of various parameters of the rotated lat-lon grid:

| Parameter | Valeur |
| ------ | ------ |
| ni | 1140 |
| nj | 1045 | 
| resolution at 60° N | 10 km |
| coordinate of the first grid point | -31.76° N ; 92.40° W |

__Note__ : The [most recent versions of wgrib2](https://www.cpc.ncep.noaa.gov/products/wesley/wgrib2/update_2.0.8.html) and [GDAL](https://gdal.org/) support these rotated grids.

## File name nomenclature 

Files have one of the following nomenclatures:

* `{YYYYMMDD}T{HH}Z_MSC_RDPA_{VAR}_Sfc_RLatLon0.09_PT0H.grib2`
* `{YYYYMMDD}T{HH}Z_MSC_RDPA-Prelim_{VAR}_Sfc_RLatLon0.09_PT0H.grib2`

where:

* __YYYYMMDD__: Year, month and day of the beginning of the forecast
* __T__ : Time delimiter according to ISO8601 norms
* __HH__: UTC run time [00, 06, 12, 18]
* __Z__ : Time zone (UTC hour)
* __MSC__ : Constant string indicating the Meteorological Service of Canada, source of data
* __RDPA__ : Constant string indicating that data is from the Regional Deterministic Precipitation Analysis. Observation cut-off time is about 007 hours after the time YYYYMMDDHH indicating that a maximum of observations has likely been collected
* __RDPA-Prelim__: Constant string indicating that data is from the Regional Deterministic Precipitation Analysis. Observation cut-off time is one hour after the time YYYYMMDDHH indicating that possibly not all observations have been collected
* __VAR__ : Constant string indicating the variable included in the file namely in this case, the accumulated precipitation which has been analyzed over a specific period [APCP-Accum6h, APCP-Accum24h]
* __Sfc__ : Constant string indicating that the surface is the vertical level 
* __RLatLon0.09__ : Constant string indicating a rotated lat-lon grid with 0.09 deg resolution (about 10km)
* __PT0H__ : Based on ISO8601 norms. P, T and H are constant character designating Period, Time and Hour. Here PT0H indicates an analysis.
* __grib2__ : constant string indicating the GRIB2 format is used

Examples of files names :

* 20220301T00Z_MSC_RDPA-Prelim_APCP-Accum6h_Sfc_RLatLon0.09_PT0H.grib2

The file originates from the Meteorological Service of Canada (MSC) and contains a Regional Deterministic Precipitation Analysis (RDPA). It contains a preliminary analysis of precipitation accumulation represented by the APCP variable over a 6 hour interval. The data are on a lat-lon rotated grid at a 10 km resolution (RLatLon0.09). The analysis was produced on March 01, 2022 at 00Z (20220301T00Z). The 006-hour interval in which the precipitation is analyzed is 2022030100 to 2022030106. 

* 20220302T12Z_MSC_RDPA_APCP-Accum24h_Sfc_RLatLon0.09_PT0H.grib2

The file originates from the Meteorological Service of Canada (MSC) and contains a Regional Deterministic Precipitation Analysis (RDPA). It contains a final analysis of precipitation accumulation represented by the APCP variable over a 24-hour interval. The data are on a lat-lon grid rotated to a 10 km resolution (RLatLon0.09). The analysis was produced on 02 March 2022 at 12Z (2022030212). The 24-hour interval in which precipitation is analyzed is 2022030212 to 2022030312.

__NOTE__: A second variable is also included in this file and it is the confidence index for the analysis.

## List of variables

<table id="csv-table" class="display"></table>

<link href="https://cdn.jsdelivr.net/npm/simple-datatables@latest/dist/style.css" rel="stylesheet" type="text/css">
<script src="https://cdn.jsdelivr.net/npm/simple-datatables@latest"></script>
<script src="../../../js/variables_datatable.js" type="text/javascript"></script>
<script>
  loadTable("csv-table", "../../../assets/csv/RDPA_Variables-List_en.csv");
</script>

## Online archives

* An [RDPA data archive](https://collaboration.cmc.ec.gc.ca/science/outgoing/capa.grib/) from April, 6th 2011 to September 23th, 2023 is available online in GRIB2 format. 

* An [archive of re-analyses](https://collaboration.cmc.ec.gc.ca/science/outgoing/capa.grib/hindcast/), covering the period from January 2002 to June 2012, is available online in GRIB2 format.

## Support

If you have any questions about this data, please [contact us](https://weather.gc.ca/mainmenu/contact_us_e.html).

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).
