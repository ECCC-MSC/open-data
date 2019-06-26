[En Français](readme_rdpa-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC Open Public Data](../readme_en.md) > RDPA

# Regional Deterministic Precipitation Analysis (RDPA - CaPA) data in GRIB2 format

The [Regional Deterministic Precipitation Analysis (RDPA)](readme_rdpa_en.md) based on the Canadian Precipitation Analysis (CaPA) system is on a domain that corresponds to that of the operational regional model, i.e. the Regional Deterministic Prediction System (RDPS-LAM3D) except for areas over the Pacific ocean where the western limit of the RDPA domain is slightly shifted eastward with respect to the regional model domain. The resolution of the RDPA analysis is identical to the resolution of the operational regional system RDPS LAM3D. The fields in the RDPA GRIB2 dataset are on a polar-stereographic (PS) grid covering North America and adjacent waters with a 10 km resolution at 60 degrees north. 

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](.../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](.../../usage/readme_en.md) is also available.

The data is available using the HTTP protocol and resides in a directory that is plainly accessible to a web browser. Visiting that directory with an interactive browser will yield a raw listing of links, each link being a downloadable GRIB2 file.

The data can be accessed at the following URLs:

* https://dd.weatheroffice.gc.ca/analysis/precip/rdpa/grib2/polar_stereographic/hh

where:

* __hh__ : time interval of 06 or 24 hours in which precipitation accumulations are analyzed

## File name nomenclature 

NOTE: ALL HOURS ARE IN UTC.

The files have one of the following nomenclature:

* CMC_RDPA_APCP-006-0100cutoff_SFC_0_ps10km_AAAAMMJJHH_000.grib2
* CMC_RDPA_APCP-006-0700cutoff_SFC_0_ps10km_AAAAMMJJHH_000.grib2
* CMC_RDPA_APCP-024-0100cutoff_SFC_0_ps10km_YYYYMMDDHH_000.grib2
* CMC_RDPA_APCP-024-0700cutoff_SFC_0_ps10km_YYYYMMDDHH_000.grib2

where:

* __CMC__: constant string indicating the data is from the Canadian Meteorological Centre
* __RDPA__: constant string indicating the data is from the regional deterministic precipitation analysis (RDPA)
* __APCP__: constant string indicating the variable included in this file is in this case the accumulated precipitation which has been analyzed.
* __006__: Precipitation accumulation interval is 006 hours
* __024__: Precipitation accumulation interval is 024 hours
* __0100cutoff__: Observation cut-off time is one hour after the time YYYYMMDDHH indicating that possibly not all observations have been collected
* __0700cutoff__: Observation cut-off time is about 007 hours after the time YYYYMMDDHH indicating that a maximum of observations has likely been collected
* __SFC__: constant string indicating the type of level is at the surface.
* __0__: elevation of the above level type where here 0 indicates the surface. For RDPA grib2 data this is the only level available.
* __ps10km__: constant string indicating the projection used is polar-stereographic at 10km resolution.
* __YYYYMMDDHH__: Year, month, day and hour of valid date of the analysis.
* __HH__: UTC run time [00,06, 12, 18]
* __000__: represents the number of hours after the YYYYMMDDHH time at which the analysis is valid.
* __grib2__: constant string indicating the GRIB2 format is used

Example of file name:

CMC_RDPA_APCP-006-0100cutoff_SFC_0_ps10km_2015011212_000.grib2

This file originates from the Canadian Meteorological Center (CMC) and contains data of the regional deterministic precipitation analysis (RDPA).
It contains the preliminary analysis of the accumulated precipitation represented here by APCP over a 6 (006) hour time interval starting at 2015011206 and ending at 2015011212. It is considered preliminary because the analysis has been produced using observations collected in a short 0100 hour period i.e. before all observations have been collected.

The data is on a polar-stereographic grid at 10km resolution (ps10km).
The file name contains the valid time of the analysis which in this case is 2015011212_000.

The data encoded in GRIB2 format (.grib2).
Note that a second variable is also included in this file and it is the confidence index for the analysis.

## Levels

RDPA variables are only available for the surface level.

## List of variables


This table provides the variable name, level, abbreviation, units and a link to additional grib2 encoding information for each parameter encoded in GRIB2 format

|Number  |	                Variable 	                                       | Level      | 	Abbreviation    |	Units    	 | Description        |
|--------|---------------------------------------------------------------------|------------|-------------------|----------------|--------------------|
| 0 	 | Analysis of Accumulated Precipitation on a 06hr or 24hr interval    | Surface 	| APCP-0[06,24]_SFC_0| 	kg m-2       |[Sections 0 to 6](https://weather.gc.ca/grib/display_e.html?type=rdpa&res=ps10km&hour=A000&desc=analysis&nombre=0)     |
| 1      | Confidence Index for Analysis 	                                   | Surface 	| CFIA_SFC_0 |varies from 0 to 1, no units | [Sections 0 to 6](https://weather.gc.ca/grib/display_e.html?type=rdpa&res=ps10km&hour=A000&desc=analysis&nombre=1) |

## About the No-data mask

Since January, 13th 2016, a mask called "No-data" has been added to our GRIB2 encoding process in order to better represent the areas where data are unavailable. This mask only concerns a few grid points with no data, always the same ones, located at the edge of the domain. Note that this mask has no negative effect on the product quality.

## Online archives

* An [ARDP data archive](http://collaboration.cmc.ec.gc.ca/science/outgoing/capa.grib/) since 6 April 2011 is available online in GRIB2 format. Note that contrary to what is indicated in the "About the No-Data mask" section above, the data available here were encoded with the mask over the entire period, not from 13 January 2016.

* An [archive of re-analyses](http://collaboration.cmc.ec.gc.ca/science/outgoing/capa.grib/hindcast/), covering the period from January 2002 to June 2012, is available online in GRIB2 format.

## Support

If you have any questions about these data, please contact us at: ec.dps-client.ec@canada.ca

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).