[En français](readme_climateindices-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [Climate Indices](readme_spei_en.md) > Climate Indices on MSC Datamart

# Statistically downscaled climate indices in NetCDF format

This document describes the content of the [climate indices data](readme_climateindices_en.md) in NetCDF format.

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available via the HTTP protocol. It is possible to access it with a standard browser. In this case, we obtain a list of links giving access to a NetCDF file.

The data can be accessed at the following URLs:

* [https://dd.meteo.gc.ca/climate/indicies/netcdf/historical/absolute/](https://dd.meteo.gc.ca/climate/indicies/netcdf/historical/absolute/)
* [https://dd.meteo.gc.ca/climate/indicies/netcdf/scenarios/[RCP2.6,RCP4.5,RCP8.5]/absolute/](https://dd.meteo.gc.ca/climate/indicies/netcdf/scenarios/)

where:

* __historical__: Historical simulations from 1900-2005.
* __scenarios__: Refers to different emission scenarios [RCP2.6, RCP4.5,RCP8.5] from 2006-2100.
* __absolute__: Représente les projections des ensembles multimodélisés (valeur réelle)

## File name nomenclature 

NOTE : ALL HOURS ARE IN UTC.

File names have the form:

* INDICES_hist _Value_ProjectionResolution_Variable_pctlPP.nc
* INDICES_rcpx.y_Value_ProjectionResolution_Variable_pctlPP.nc


where:

* __INDICES__: Constant string indicating that the datasets are statistically downscaled climate indices 
* __hist__: Constant string indicating historical data
* __rcpx.y__: Version of the Representative Concentration Pathways (scenario experiments), taking one of the values : [RCP2.6, RCP4.5, RCP8.5]
* __Value__: Values category, taking one of the two values : [ RCP, 2006-2100 | Historical = 1951-2005]
* __Projection__: Grid mapping (projection) taking the value : [latlon]
* __Resolution__: Grid resolution taking one of the values : [0.086x0.086]; 0.086 stands for 0.086-degree resolution in both the latitudinal and longitudinal directions
* __Variable__: Name of variable available in the file, taking one of the values : [CDD, GSC, GSO, GSW, HDD, TX30, TN20, PREP1]; CDD stands for cooling degree days, GSC stands for length of growing season for cool season crops, GSO stands for length of growing season for overwintering crops, GSW stands for length of growing season for warm season crops, HDD stands for heating degree days, TX30 stands for hot days (number of days with maximum temperature above 30°C), TN20 stands for hot nights (number of days with minimum temperature above 20°C), PREP1 stands for number of days with precipitation greater than 1mm.
* __PctlPP__: Ensemble percentile number, taking one of the values : [pctl5, pctl25, pctl50, pctl75, pctl95]
* __nc__: Constant string indicating the NetCDF format

Examples :

* CMIP5_RCP8.5_SPEI-12_2006-2100_latlon1x1_SPEI_pctl50.nc

## Variable list

The available variables and units for the statistically downscaled multimodel ensembles of climate indices are:

* __CDD__: Cooling degree days (°C - day)
* __HDD__: Heating degree days (°C - day)
* __GSC__: Length of growing season for cool season crops (days)
* __GSO__: Length of growing season for overwintering crops (days)
* __GSW__: Length of growing season for warm season crops (days)
* __PREP1__: Number of days with precipitation > 1mm (days)
* __TN20__: Hot nights (number of days with minimum temperature above 20°C) (days)
* __TX30__: Hot days (number of days with maximum temperature above 30°C) (days)

## Support

If you have any questions about these data, please contact us at : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).
