[En français](readme_spei-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [SPEI](readme_spei_en.md) > SPEI on MSC Datamart

# Standardized Precipitation Evapotranspiration Index (SPEI) in NetCDF format

This document describes the content of the [SPEI data](readme_spei_en.md) in NetCDF format.

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available via the HTTP protocol. It is possible to access it with a standard browser. In this case, we obtain a list of links giving access to a NetCDF file.

The data can be accessed at the following URLs :

* [https://dd.weather.gc.ca/climate/spei/netcdf/historical/{[SPEI-1, SPEI-3, SPEI-12]}](https://dd.weather.gc.ca/climate/spei/netcdf/historical)
* [https://dd.weather.gc.ca/climate/spei/netcdf/scenarios/{[RCP2.6,RCP4.5,RCP8.5]}/{[SPEI-1, SPEI-3, SPEI-12]}](https://dd.weather.gc.ca/climate/spei/netcdf/scenarios)

where :

* __historical__ : Historical simulations from 1900-2005.
* __scenarios__ : Refers to different emission scenarios [RCP2.6, RCP4.5,RCP8.5] from 2006-2100.
* __SPEI__ : Refers to the time scale in months that SPEI was calculated for. SPEI-1 corresponds to SPEI of one month; SPEI-3 corresponds to SPEI of one month and the previous 2 months, and SPEI-12 corresponds to SPEI of one month and the previous 11 months. 

## File name nomenclature 

NOTE : ALL HOURS ARE IN UTC.

File names have the form :

* CMIP5_hist_TimeScale_Value_ProjectionResolution_Variable_pctlPP.nc
* CMIP5_rcpx.y_TimeScale_Value_ProjectionResolution_Variable_pctlPP.nc

where :

* __rcpx.y__ : Version of the Representative Concentration Pathways (scenario experiments), taking one of the values : [rcp2.6, rcp4.5, rcp8.5]
* __Time-Scale__ : SPEI-1, SPEI-3 and SPEI-12. SPEI-1 corresponds to SPEI of one month; SPEI-3 corresponds to SPEI of one month and the previous 2 months, and SPEI-12 corresponds to SPEI of one month and the previous 11 months. 
* __Value__ : Values category representing time period of the dataset, taking one of these two values :  [ RCP= 2006-2100. Historical= 1900-2005]
* __Projection__ : Grid mapping (projection) taking the value : [latlon]
* __Resolution__ : Grid resolution taking one of the values : [1x1]; 1 stands for 1-degree resolution in both the latitudinal and longitudinal directions.
* __Variable__ : Name of variable available in the file: Always SPEI which means 'Standardized Precipitation Evapotranspiration Index'.
* __PctlPP__ : Ensemble percentile number, taking one of the values : [pctl25, pctl50, pctl75]


Examples :

* CMIP5_RCP8.5_SPEI-12_2006-2100_latlon1x1_SPEI_pctl50.nc

## Support

If you have any questions about these data, please contact us at : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).

