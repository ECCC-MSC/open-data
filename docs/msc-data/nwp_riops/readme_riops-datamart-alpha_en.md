[En français](readme_riops-datamart-alpha_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [RIOPS](readme_riops_en.md) > RIOPS data in GRIB2 on DD-Alpha

# Experimental Regional Ice Ocean Prediction System (RIOPS) Data in GRIB2 Format

This page describes the data of the [Regional Ice Ocean Prediction System (RIOPS)](readme_riops_en.md) available on the MSC testing data repository DD-Alpha.

## Data location 

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available using the HTTP protocol and resides in a directory that is plainly accessible to a web browser. Visiting that directory with an interactive browser will yield a raw listing of links, each link being a downloadable GRIB2 file.

The data can be accessed at the following URLs :

* [https://dd.alpha.meteo.gc.ca/model_riops/netcdf](https://dd.alpha.meteo.gc.ca/model_riops/netcdf)

An on-line archive is available during the YOPP project

## File name nomenclature 

NOTE : ALL HOURS ARE IN UTC.

The files have the following nomenclature:

* CMC_riops_Variable_LevelType_Level_ProjectionResolution_TimeMean_YYYYMMDDHH_Phhh.nc

where :

* __CMC__ : constant string indicating the data source (Canadian Meteorological Centre)
* __riops__ : constant string indicating the forecasting system that generated the data (RIOPS)
* __Variable__ : name of forecast variable available in the file 
* __LevelType__ : level type taking one of the values: [sfc, depth]
* __Level__ : level value; 0 for the 'sfc' (surface) level and either 0.5 (metres) or 'all' (all model depths) for depth level type
* __Projection__ : grid mapping (projection) taking one value: ps
* __Resolution__ : resolution taking one of value, 5km60N, which stands for 5-km resolution at 60° N latitude
* __TimeMean__ : This takes the value 3h-mean and indicates that the variable is a time mean calculated over the specified time interval (3 hours for 3h). Note that the validity time of the forecast variable is set at the end of the time averaging period. Note also this exception: the ice variables are actually instantaneous.
* __YYYYMMDD__ : year, month and day of the beginning of the forecast
* __HH__ : Start hour of model run in UTC [00, 12] 
* __Phhh__ : P is a constant character. hhh is the forecast hour [000, 003, 006, ..., 048]
* __nc__ : constant string indicating the NetCDF format


Examples : 

* CMC_riops_iiceconc_sfc_0_ps5km60N_3h-mean_2016020312_P003.nc

The files containing data on the ps5km60N grid can be found at the following address:
* http://dd.alpha.meteo.gc.ca/yopp/model_riops/netcdf/forecast/polar_stereographic/nd/YYYY/MM/DD/HH/hhh/ 

where:

* __n__ : number of spatial dimensions of the forecast fields [2 or 3]
* __HH__ : Start hour of model run in UTC [00, 12]
* __hhh__ : forecast hour: every 3 hours starting from hour 0 [000, 003, ..., 048] for n=2 and from hour 3 [003, 006, ..., 048] for n=3

## List of variables

List of variables (forecast fields) available in the files containing 2D fields:

* votemper :	Potential temperature of sea water at the first model level
* vosaline :	Sea water salinity at the first model level
* vozocrtx :	X-component of water velocity at the first model level
* vomecrty :	Y-component of water velocity at the first model level
* sossheig :	Sea surface height
* somixhgt :	Turbocline depth
* sokaraml :	Mixed layer depth based on a density criterion
* iiceconc :	Sea ice  fraction	
* iicevol :		Volume of sea ice per unit grid cell area
* itzocrtx :	X-component of sea ice velocity	
* itmecrty :	Y-component of sea ice velocity	
* isnowvol :	Volume of snow on sea ice per unit grid cell area
* iicesurftemp :	Surface temperature of sea ice/snow
* iicepressure :	Vertically integrated ice internal pressure
* iicestrength :	Vertically integrated compressive ice strength


List of variables (forecast fields) available in the files containing 3D fields:

* votemper :	Potential temperature of sea water
* vosaline :	Sea water salinity
* vozocrtx :	X-component of water velocity
* vomecrty :	Y-component of water velocity

## Support

If you have any questions about these data, please contact us at: [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).