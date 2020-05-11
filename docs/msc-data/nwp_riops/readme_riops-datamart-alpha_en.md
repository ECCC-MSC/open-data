[En français](readme_riops-datamart-alpha_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [RIOPS](readme_riops_en.md) > RIOPS data in GRIB2 on DD-Alpha

# Regional Ice Ocean Prediction System (RIOPS) Data in GRIB2 Format

The Canadian Centre for Meteorological and Environmental Prediction (CCMEP) provides instantaneous sea ice and time-mean ocean forecast fields produced by its experimental Regional Ice-Ocean Prediction System (RIOPS) and interpolated to a grid in north-polar stereographic projection with 5km resolution at the standard parallel 60° N (ps5km60N). 

The data files are in NetCDF format (NetCDF-4 classic model) and comply with the Climate and Forecast Conventions. 

RIOPS is based on the NEMO-CICE ice-ocean model and produces regional sea ice and ocean analyses and 2 day forecasts daily based at [00, 12] UTC on a subset of the 1/12° resolution global tri-polar grid (ORCA12). 

RIOPS includes a 3DVar ice concentration analysis (assimilating sattelite remote sensing and Canadian Ice Service ice charts) while the large scales of the ocean analysis are constrained by spectrally nudging the temperature and salinity fields to those of the CCMEP Global Ice Ocean Prediction System (which itself includes a full multivariate assimilation system that combines satellite observations with in situ observations). 

Surface air-sea fluxes for 2 day forecasts are calculated by coupling NEMO-CICE to the atmospheric model run in the Canadian Arctic Prediction System. As such, the present RIOPS forecasts are now produced inside [CAPS](../nwp_caps/readme_caps_en.md).

This system makes an important contribution to various scientific experiments that are part of the [Year of the Polar Forecast (YOPP)](https://www.polarprediction.net/) by providing numerical weather forecasts at the kilometre scale in the Canadian Arctic.

## Data location 

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available using the HTTP protocol and resides in a directory that is plainly accessible to a web browser. Visiting that directory with an interactive browser will yield a raw listing of links, each link being a downloadable GRIB2 file.

The data can be accessed at the following URLs :

* [https://dd.alpha.weather.gc.ca/yopp/model_riops/netcdf/forecast/polar_stereographic/nd/YYYY/MM/DD/HH/hhh/](https://dd.alpha.meteo.gc.ca/yopp/model_riops/netcdf/forecast/polar_stereographic/)

* __nd__ : Number of spatial dimensions of the forecast fields [2d or 3d].
* __YYYY__ : Year of the forecast start [2018, 2019, ...].
* __MM__ : Month of the forecast start [01, 02, 03, ..., 12].
* __DD__ : Day of the forecast start.
* __HH__ : Start hour of model run in UTC [00,12].
* __hhh__ : Forecast hour.

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

## List of variables

List of variables (forecast fields) available in the files containing 2D fields:

* __votemper__ :	Potential temperature of sea water at the first model level
* __vosaline__ :	Sea water salinity at the first model level
* __vozocrtx__ :	X-component of water velocity at the first model level
* __vomecrty__ :	Y-component of water velocity at the first model level
* __sossheig__ :	Sea surface height
* __somixhgt__ :	Turbocline depth
* __sokaraml__ :	Mixed layer depth based on a density criterion
* __iiceconc__ :	Sea ice  fraction	
* __iicevol__ :		Volume of sea ice per unit grid cell area
* __itzocrtx__ :	X-component of sea ice velocity	
* __itmecrty__ :	Y-component of sea ice velocity	
* __isnowvol__ :	Volume of snow on sea ice per unit grid cell area
* __iicesurftemp__ :	Surface temperature of sea ice/snow
* __iicepressure__ :	Vertically integrated ice internal pressure
* __iicestrength__ :	Vertically integrated compressive ice strength


List of variables (forecast fields) available in the files containing 3D fields:

* __votemper__ :	Potential temperature of sea water
* __vosaline__ :	Sea water salinity
* __vozocrtx__ :	X-component of water velocity
* __vomecrty__ :	Y-component of water velocity

## Support

If you have any questions about these data, please contact us at: [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).