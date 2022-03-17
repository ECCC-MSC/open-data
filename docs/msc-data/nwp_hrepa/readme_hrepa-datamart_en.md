[En Français](readme_hrepa-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_fr.md) > [MSC data](../readme_fr.md) > [HREPA](readme_hrepa_fr.md) > HREPA on MSC DD-Alpha

# High Resolution Ensemble Precipitation Analysis (HREPA) Data in NetCDF Format

This page describes the experimental [High Resolution Ensemble Precipitation Analysis](./readme_hrepa-datamart_en.md) data available in NetCDF format on the MSC testing data repository DD-Alpha.


## Data location

MSC testing data repository DD-Alpha data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available using the HTTPS protocol and resides in a directory that is plainly accessible to a web browser. Visiting that directory with an interactive browser will yield a raw listing of links, each link being a downloadable netCDF file.

The data can be accessed at the following URLs :

* [https://dd-alpha.meteo.gc.ca/model_hrepa/2.5km/{HH}](https://dd.meteo.gc.ca/model_hrepa/2.5km)

where :
* __HH__ : validy hour of the analysis, in UTC [00,06,12,18]

## Grid specifications

![image de la grille HREPA](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_hrepa/grille_hrepa.png)

Table lists the values of parameters of the rotated latitude-longitude grid on which the variables in netCDF format are available

| Parameter | Value |
| ------ | ------ |
| ni | 2438 |
| nj | 1188 | 
| résolution        | 0,0225°                  |
| coordinates of the first grid point | 41.0269° N ; 132.5993° W | 
| grid orientation (with respect to j axis) | -115.0° |

## File name nomenclature 

NOTE : ALL HOURS ARE IN UTC.

The files have the following nomenclature:

`{YYYYMMDD}T{HH}Z_MSC_HREPA_{Var}_Sfc_{Grid}{resolution}_PT0H.nc`

where : 

* __YYYYMMDD__ : Year, month and day of the beginning of the forecast
* __T__: Time delimiter according to ISO8601 norms
* __HH__ : UTC run time [00, 06, 12, 18]
* __Z__: Time zone (UTC hour)
* __MSC__: Constant string indicating that the data is from the Meteorologcal Service of Canada (MSC)
* __HREPA__: Constant string indicating that data is from High Resolution Ensemble Precipitation Analysis (HREPA) system
* __Var__ : Variables included in this file. See the list below
* __Sfc__: Constant string indicating that the level type is Surface
* __Grid__ : Constant string indicating the rotated latitude and longitude projection [RLatLon]
* __resolution__ : Constant string indicating that the resolution in degree 0.025° (about 2.5 km) in both latitude and longitude directions
* __PT0H__ : Constant string indicating an analysis, based on ISO8601 norms. P, T and H are constant character designating Period, Time and Hour.
* __nc__ : constant string indicating the NetCDF format

Example :

20220214T06Z_MSC_HREPA_Precip-Accum06h_Sfc_RLatLon0.0225_PT0H.nc

This file originates from the Meteorological Service of Canada (MSC) and contains the High Resolution Ensemble Precipitation Analysis (HREPA) data. HREPA is an ensemble precipitation analysis of 6-hour amounts where the accumulation period goes from 20220214 at 00UTC to 20220214 at 06UTC. This file contains 25 members. The first member is the control and corresponds to a deterministic analysis (without perturbations), while the 24 other members are the analyses obtained after perturbations of the inputs.

Note that a second variable is also included in this file, and it is the confidence index for the analysis (CFIA).

## List of variables

Three types of files exist for a given valid date; each file has its variables for the package products available in the NetCDF are described below. For each file, the variable, the definition, and frequency of availability are mentioned.

* For files of type "Precip-Accum06h":
   * __pr__ : 25-member ensemble of the 6-hour precipitation analyses, available at synoptic hours (mm)
   * __cfia__ : Confidence Index of the Analysis of the control member. Range of values from 0 to 1 (no unit), available at synoptic hours (mm)

* For the files of type "Precip-Accum06h-Pct25":
   * __q025__ : 25th percentile estimated on the 25-member HREPA, available at synoptic hours (mm)

* For the files of type "Precip-Accum06h-Pct75":
   * __q075__ : 75th percentile estimated on the 25-member HREPA, available at synoptic hours (mm)

## Support

If you have any questions about this data, please contact us at: [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).





























