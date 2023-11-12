[En français](readme_hrdpa-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [HRDPA](readme_hrdpa_en.md) > HRDPA on MSC Datamart

# High Resolution Deterministic Precipitation Analysis (HRDPA) Data in GRIB2 Format

This page describes the [High Resolution Deterministic Precipitation Analysis](./readme_hrdpa-datamart_en.md) data available in GRIB2 format.

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available using the HTTPS protocol and resides in a directory that is plainly accessible to a web browser. Visiting that directory with an interactive browser will yield a raw listing of links, each link being a downloadable GRIB2 file.

The data can be accessed at the following URLs :

* Polar-stereographic grid: [https://dd.weather.gc.ca/analysis/precip/hrdpa/grib2/polar_stereographic/{hh}](https://dd.weather.gc.ca/analysis/precip/hrdpa/grib2/polar_stereographic)
* Rotated lat-lon grid: [https://dd.weather.gc.ca/model_hrdpa/2.5km/{HH}](https://dd.weather.gc.ca/model_hrdpa/2.5km)

where :

* __polar_stereographic__ :  Grid projection
* __hh__ : time interval of 06 or 24 hours in which precipitation accumulations are analyzed
* __HH__ :  UTC run time [00, 06, 12, 18]

A history of 30 days is maintained in this directory.

## Grid specifications of the grids

* __Polar-stereographic grid__

![HRDPA grid specification image](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_hrdpa/grille_hrdpa.png)

Table lists the values of parameters of the polar-stereographic grid.

| Parameter | Value |
| ------ | ------ |
| ni | 2500 |
| nj | 1222 | 
| resolution at 60° N | 2.5 km |
| coordinates of the first grid point | 42.2504° N  131.0928° W | 
| grid orientation (with respect to j axis) | -115.0° |

* __Rotated lat-lon grid__

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

### Polar-stereographic grid

The files have the following nomenclature:

CMC_HRDPA_APCP-TotalPrecipAmount-HHMMcutoff_SFC_0_ps2.5km_YYYYMMDDHH_000.grib2

where :

* __CMC__ : Data is produced by the Canadian Meteorological Centre (Constant string)
* __HRDPA__ : High Resolution Deterministic Precipitation Analysis (Constant string)
* __APCP__ : Analysis of Precipitation (Constant string)
* __TotalPrecipAmountPeriod__ : Total precipitation amount over a period of time in number of hours (006 or 024)
* __HHMMcutoff__ : Observation cuttoff time in number of hours and minutes after valid time. (0100cutoff or 0700cutoff)
* __SFC_0__ : Level type is Surface and level value is 0 (Constant string)
* __ps2.5km__ : Projection type is Polar-Stereographic and the resolution is 2.5 km (Constant string)
* __YYYYMMDDHH__ : Analysis valid time in UTC. YYYY=Year, MM=Month, DD=Day, HH=Hour (ex: 2018020912)
* __000__ : The projection time in number of hours. Always 000 for an analysis product (Constant string)

Example :

CMC_HRDPA_APCP-006-0100cutoff_SFC_0_ps2.5km_2018020912_000.grib2

This file originates from the Canadian Meteorological Center (CMC) and contains data of the High Resolution Deterministic Precipitation Analysis (HRDPA). This is a precipitation analysis (APCP) of 6 hour amounts (006) where the accumulation period goes from 2018020906 to 2018020912. It is considered preliminary because observations have been collected up to 2018020913, which is 1 hour after valid time (0100cutoff). The data is on a polar-stereographic grid at a resolution of 2.5 km (ps2.5km). The valid time of the analysis is 2018020912_000 and the suffix _000 means that the projection time in the future is null, which is always the case for an analysis. The data is encoded in GRIB2 format (.grib2).

Note that a second variable is also included in this file and it is the confidence index for the analysis (CFIA).

### Rotated lat-lon grid

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

## About the polar stereographic grid no-data mask

A mask called "No-data" has been added to our GRIB2 encoding process in order to better represent the areas where data are unavailable. This mask only concerns a few grid points with no data, always the same ones, located at the edge of the domain. Note that this mask has no negative effect on the product quality.

## Support

If you have any questions about this data, please contact us at: [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).
