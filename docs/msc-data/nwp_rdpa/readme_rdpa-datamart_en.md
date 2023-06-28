[En français](readme_rdpa-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [RDPA](readme_rdpa_en.md) > RDPA on MSC Datamart

# Regional Deterministic Precipitation Analysis (RDPA - CaPA) data in GRIB2 format

This page describes the [Regional Deterministic Precipitation Analysis (RDPA)](readme_rdpa_en.md) data based on the Canadian Precipitation Analysis (CaPA) system. 

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available using the HTTPS protocol and resides in a directory that is plainly accessible to a web browser. Visiting that directory with an interactive browser will yield a raw listing of links, each link being a downloadable GRIB2 file.

The data can be accessed at the following URLs :

* Polar-stereographic grid: [https://dd.weather.gc.ca/analysis/precip/rdpa/grib2/polar_stereographic/{hh}](https://dd.weather.gc.ca/analysis/precip/rdpa/grib2/polar_stereographic)
* Rotated lat-lon grid: [https://hpfx.collab.science.gc.ca/{YYYMMDD}/WXO-DD/model_rdpa/10km/{HH}](https://hpfx.collab.science.gc.ca/)

where :

* __YYYYMMDD__: Year, month and day
* __hh__ : time interval of 06 or 24 hours in which precipitation accumulations are analyzed
* __HH__ :  UTC run time [00, 06, 12, 18]

A 30-day history is kept on the MSC Datamart and a history of several weeks is kept on HPFX, the MSC Datamart alternative server.

## Technical specification of the grids

* __Polar-stereographic grid__

![](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_rdpa/grille_rdpa.png)

Values given to the parameters of the stereographic polar grid:

| Parameter | Value |
| ------ | ------ |
| ni | 935 |
| nj | 824 | 
| resolution at 60° N | 10 km |
| coordinates of the first grid point | 18.1429° N  142.8968° W | 
| (i,j) coordinate of North Pole | (456.2; 732.4) |
| grid orientation (with respect to j axis) | -111.0° |

* __Rotated lat-lon grid__

![Rlatlon RDPA grid](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_rdpa/grille_rdpa_rlatlon.png)

The following table lists the values of various parameters of the rotated lat-lon grid:

| Parameter | Valeur |
| ------ | ------ |
| ni | 1102 |
| nj | 1076 | 
| resolution at 60° N | 10 km |
| coordinate of the first grid point | -31.76° N ; 92.40° W |

__Note__ : The [most recent versions of wgrib2](https://www.cpc.ncep.noaa.gov/products/wesley/wgrib2/update_2.0.8.html) and [GDAL](https://gdal.org/) support these rotated grids.

## File name nomenclature 

NOTE: ALL HOURS ARE IN UTC.

### Polar-stereographic grid

The files have one of the following nomenclature :

* CMC_RDPA_APCP-006-0100cutoff_SFC_0_ps10km_AAAAMMJJHH_000.grib2
* CMC_RDPA_APCP-006-0700cutoff_SFC_0_ps10km_AAAAMMJJHH_000.grib2
* CMC_RDPA_APCP-024-0100cutoff_SFC_0_ps10km_YYYYMMDDHH_000.grib2
* CMC_RDPA_APCP-024-0700cutoff_SFC_0_ps10km_YYYYMMDDHH_000.grib2

where :

* __CMC__: Constant string indicating the data is from the Canadian Meteorological Centre
* __RDPA__: Constant string indicating the data is from the regional deterministic precipitation analysis (RDPA)
* __APCP__: Constant string indicating the variable included in this file is in this case the accumulated precipitation which has been analyzed.
* __006__: Precipitation accumulation interval is 006 hours
* __024__: Precipitation accumulation interval is 024 hours
* __0100cutoff__: Observation cut-off time is one hour after the time YYYYMMDDHH indicating that possibly not all observations have been collected
* __0700cutoff__: Observation cut-off time is about 007 hours after the time YYYYMMDDHH indicating that a maximum of observations has likely been collected
* __SFC__: Constant string indicating the type of level is at the surface.
* __0__: Elevation of the above level type where here 0 indicates the surface. For RDPA grib2 data this is the only level available.
* __ps10km__: Constant string indicating the projection used is polar-stereographic at 10km resolution.
* __YYYYMMDDHH__: Year, month, day and hour of valid date of the analysis.
* __HH__: UTC run time [00, 06, 12, 18]
* __000__: Represents the number of hours after the YYYYMMDDHH time at which the analysis is valid.
* __grib2__: Constant string indicating the GRIB2 format is used

Example of file name :

CMC_RDPA_APCP-006-0100cutoff_SFC_0_ps10km_2015011212_000.grib2

This file originates from the Canadian Meteorological Center (CMC) and contains data of the regional deterministic precipitation analysis (RDPA).
It contains the preliminary analysis of the accumulated precipitation represented here by APCP over a 6 (006) hour time interval starting at 2015011206 and ending at 2015011212. It is considered preliminary because the analysis has been produced using observations collected in a short 0100 hour period i.e. before all observations have been collected. The data is on a polar-stereographic grid at 10km resolution (ps10km). The file name contains the valid time of the analysis which in this case is 2015011212_000.

### Rotated lat-lon grid

Files have one of the following nomenclatures:

* {YYYYMMDD}T{HH}Z_MSC_RDPA_{VAR}_Sfc_RLatLon0.09_PT0H.grib2
* {YYYYMMDD}T{HH}Z_MSC_RDPA-Prelim_{VAR}_Sfc_RLatLon0.09_PT0H.grib2

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

This table provides the variable name, level, abbreviation, units and a link to additional grib2 encoding information for each parameter encoded in GRIB2 format.

<table id="csv-table" class="display"></table>

<link href="https://cdn.jsdelivr.net/npm/simple-datatables@latest/dist/style.css" rel="stylesheet" type="text/css">
<script src="https://cdn.jsdelivr.net/npm/simple-datatables@latest"></script>
<script src="../../../js/variables_datatable.js" type="text/javascript"></script>
<script>
  loadTable("csv-table", "../../../assets/csv/RDPA_en.csv", "EN");
</script>

## About the polar stereographic grid no-data mask

Since January, 13th 2016, a mask called "No-data" has been added to our GRIB2 encoding process in order to better represent the areas where data are unavailable. This mask only concerns a few grid points with no data, always the same ones, located at the edge of the domain. Note that this mask has no negative effect on the product quality.

## Online archives

* An [RDPA data archive](https://collaboration.cmc.ec.gc.ca/science/outgoing/capa.grib/) since 6 April 2011 is available online in GRIB2 format. Note that contrary to what is indicated in the "About the No-Data mask" section above, the data available here were encoded with the mask over the entire period, not from 13 January 2016.

* An [archive of re-analyses](https://collaboration.cmc.ec.gc.ca/science/outgoing/capa.grib/hindcast/), covering the period from January 2002 to June 2012, is available online in GRIB2 format.

## Support

If you have any questions about this data, please contact us at : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).
