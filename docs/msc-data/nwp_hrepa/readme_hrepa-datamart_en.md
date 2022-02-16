[En Français](readme_hrepa-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_fr.md) > [MSC data](../readme_fr.md) > [HREPA](readme_hrepa_fr.md) > HREPA on MSC Datamart

# High Resolution Ensemble Precipitation Analysis (HREPA) Data in netCDF Format

This page describes the [High Resolution Ensemble Precipitation Analysis](./readme_hrepa-datamart_en.md) data available in netCDF format.


## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available using the HTTPS protocol and resides in a directory that is plainly accessible to a web browser. Visiting that directory with an interactive browser will yield a raw listing of links, each link being a downloadable netCDF file.

The data can be accessed at the following URLs :

* [https://dd.meteo.gc.ca/model_hrepa/{AC}](https://dd.meteo.gc.ca/model_hrepa/)

where :
* __AC__ : Accumulation period in hours: 06

## Grid specifications

Table lists the values of parameters of the rotated latitude-longitude grid on which the variables in netCDF format are available

| Parameter | Value |
| ------ | ------ |
| ni | 2560 |
| nj | 1310 | 
| résolution        | 0,0225°                  |
| coordinates of the first grid point | 42.2504° N ; 131.0928° W | 
| grid orientation (with respect to j axis) | -115.0° |

## File name nomenclature 

NOTE : ALL HOURS ARE IN UTC.

The files have the following nomenclature:
* `<YYYYMMDD>T<HH>_MSC_HREPA_<VariableType>_Sfc_<grille>RLatLon0.0225.nc`

where : 

* __YYYYMMDD__ : Analysis valid date: YYYY=year, MM=Month, DD=Day (e.g: 20220214)
* __HH__ : Analysis valid hour UTC (00, 06, 12 and 18UTC)
* __MSC__: Data is produced by the Meteorological Service of Canada (Constant string)
* __HREPA__: Ensemble precipitation analysis (Constant string)
* __VariableType__ : variale available in the file. To see the complete variable list, see section « List of variables/files»
* __Sfc__: Level type is Surface (Constant string)
* __RLatLon__ : Rotated grid (Constant string)
* __0.0225__ : The resolution is 0.025° (2.5 km) (Constant string)
* __nc__ : netCDF format (Constant string)


Example :
20220214T06Z_MSC_HREPA_Precip-Accum06h_Sfc_RLatLon0.0225.nc

This file originates from the Meteorological Service of Canada (MSC) and contains the High Resolution Ensemble Precipitation Analysis (HREPA) data. HREPA is an ensemble precipitation analysis of 6-hour amounts where the accumulation period goes from 20220214 at 00UTC to 20220214 at 06UTC. This file contains 25 members. The first member is the control and corresponds to a deterministic analysis (without perturbations), while the 24 other members are the analyses obtained after perturbations of the inputs.

Note that a second variable is also included in this file, and it is the confidence index for the analysis (CFIA).

## List of variables/files

Three types of files exist for a given valid date; each file has its variables for the package products available in the netCDFs are described below. For each file, the variable, the definition, and frequency of availability are mentioned.

For the file **Precip-Accum06h**:
* __pr__ : 25-member ensemble of the 6-hour precipitation analyses, available at synoptic hours (mm)
* __cfia__ : Confidence Index of the Analysis of the control member. Range of values from 0 to 1 (no unit), available at synoptic hours (mm)

For the file  **Precip-Accum06h-Pct25**:
* __q025__ : 25th percentile estimated on the 25-member HREPA, available at synoptic hours (mm)

For the file  **Precip-Accum06h-Pct75**:
* __q075__ : 75th percentile estimated on the 25-member HREPA, available at synoptic hours (mm)

## Support

If you have any questions about this data, please contact us at: [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).





























