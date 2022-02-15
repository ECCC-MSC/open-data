[En Français](readme_hrepa-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_fr.md) > [MSC data](../readme_fr.md) > [HREPA](readme_hrepa_fr.md) > HREPA on MSC Datamart

# High Resolution Ensemble Precipitation Analysis (HREPA) Data in netCDF Format

This page describes the [High Resolution Ensemble Precipitation Analysis](./readme_hrepa-datamart_en.md) data available in netCDF format.


## Adresse des données 

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available using the HTTPS protocol and resides in a directory that is plainly accessible to a web browser. Visiting that directory with an interactive browser will yield a raw listing of links, each link being a downloadable netCDF file.

The data can be accessed at the following URLs :

* [https://dd.meteo.gc.ca/model_hrepa/{AC}](https://dd.meteo.gc.ca/model_hrepa/)

where :
* __AC_ : Accumulation period in hours: 06

## Grid specifications

Table lists the values of parameters of the rotated latitude-longitude grid on which the variables in netCDF format are available

| Parameter | Value |
| ------ | ------ |
| ni | 2500 |
| nj | 1222 | 
| resolution at 60° N | 2.5 km |
| coordinates of the first grid point | 42.2504° N  131.0928° W | 
| grid orientation (with respect to j axis) | -115.0° |

## File name nomenclature 

NOTE : TOUTES LES HEURES SONT EN UTC.

Les fichiers ont la nomenclature suivante :
* `<YYYYMMDD>T<HH>_MSC_HREPA_<Variable>_Sfc_<grille>RLatLon0.0225.nc`

où : 

* __YYYYMMDD__ : Analysis valid date: YYYY=year, MM=Month, DD=Day (e.g: 20220214)
* __HH__ : Analysis valid hour UTC (00, 06, 12 and 18UTC)
* __MSC__: Data is produced by the Meteorological Service of Canada (Constant string)
* __HREPA__: Ensemble precipitation analysis (Constant string)
* __Variable__ : variale available in the file. To see the complete variable list, see section « List of variables»
* __Sfc__: Level type is Surface (Constant string)
* __RLatLon__ : Projection type is Polar-Stereographic (Constant string)
* __0.0225__ : The resolution is 0.025° (2.5 km) (Constant string)
* __nc__ : netCDF format (Constant string)


Example :
20220214T06Z_MSC_HREPA_Precip-Accum06h_Sfc_RLatLon0.0225.nc

This file originates from the Meteorological Service of Canada (MSC) and contains data of the High Resolution Ensemble Precipitation Analysis (HREPA). This is an ensemble precipitation analysis of 6 hour amounts (006) where the accumulation period goes from 20220214 at 00UTC to 20220214 at 06UTC. This file contains 25 members, the first member is the control and corresponds to a deterministic analysis (without perturbations) while the 24 other members are the analyses obtained after perturbations of the inputs.

Note that a second variable is also included in this file and it is the confidence index for the analysis (CFIA).

## List of variables

The variables for the package products available in the netCDFs are described below. For each variable, the definition and frequency of availability are mentioned.

Pour la variable **Precip-Accum06h**

* __pr__ : Ensemble of analyses of the total amount of precipitation, available at synoptic hours (mm)
* __cfia__ : Confidence Index of the Analysis. Range of values from 0 to 1 (no unit), available at synoptic hours (mm)

Pour la variable **Precip-Accum06h-Pct25**
* __q025__ : 25th percentile estimated on the 25-member ensemble of precipitation analysis, available at synoptic hours (mm)

Pour la variable **Precip-Accum06h-Pct75**
* __q075__ : 75th percentile estimated on the 25-member ensemble of precipitation analysis, available at synoptic hours (mm)

## Support

If you have any questions about this data, please contact us at: [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).





























