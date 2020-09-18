[En français](readme_riops-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [RIOPS](readme_riops_en.md) > RIOPS data in NetCDF 

# Regional Ice Ocean Prediction System (RIOPS) Data in NetCDF Format

The Canadian Centre for Meteorological and Environmental Prediction (CCMEP) provides instantaneous forecasts of sea ice and ocean fields produced by its operationtal Regional Ice-Ocean Prediction System (RIOPS) and interpolated to a grid in north-polar stereographic projection with 5 km resolution at the standard parallel 60°N. 

The data files are in NetCDF format (NetCDF-4 classic model) and comply with the Climate and Forecast Conventions. 

RIOPS is based on the NEMO-CICE ice-ocean model and produces regional sea ice and ocean analyses and 2 day forecasts daily based at [00, 06, 12, 18] UTC on a subset of the 1/12° resolution global tri-polar grid (ORCA12). 

RIOPS includes a 3DVar ice concentration analysis (assimilating sattelite remote sensing and Canadian Ice Service ice charts) while the large scales of the ocean analysis are constrained by spectrally nudging the temperature and salinity fields to those of the CCMEP Global Ice Ocean Prediction System (which itself includes a full multivariate assimilation system that combines satellite observations with in situ observations). 

## Data location 

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available using the HTTP protocol and resides in a directory that is plainly accessible to a web browser. Visiting that directory with an interactive browser will yield a raw listing of links, each link being a downloadable GRIB2 file.

The data can be accessed at the following URLs :

* [https://dd.weather.gc.ca/model_riops/netcdf/forecast/polar_stereographic/nd/HH/hhh/](https://dd.weather.gc.ca/model_riops/netcdf/forecast/polar_stereographic/)

where :

* __nd__ : Number of spatial dimensions of the forecast fields [2d or 3d]
* __HH__ : Start hour of model run in UTC [00, 06, 12, 18]
* __hhh__ : Forecast hour [000, 001, 002, ..., 048] 

A history of 2 days of forecast is kept in this directory.

## File name nomenclature 

NOTE : ALL HOURS ARE IN UTC.

The files have the following nomenclature:

* {YYYYMMDD}T{HH}Z_MSC_RIOPS_VAR_LVL_{Grid}{resolution}_P{hhh}.nc

where :

* __YYYYMMDD__ : Year, month and day of the beginning of the forecast
* __T__ : Time delimiter according to ISO8601 norms
* __HH__ : UTC run time [00, 06, 12, 18]
* __Z__ : Time zone (UTC hour)
* __MSC__ : Constant string indicating the Meteorological Service of Canada, source of data
* __RIOPS__ : Constant string indicating the forecasting system that generated the data (RIOPS)
* __VAR__ : Name of forecast variable available in the file 
* __LVL__ : Vertical level [SFC, DBS-0.5m, DBS-all]; SFC for surface, DBS for Depth Below Surface, 0.5m for depth of 0.5m below the surface, 'all' for all depths 
* __Grid__ : Grid mapping projection [PS]
* __resolution__ : Horizontal resolution [5km], stands for 5 km horizontal resolution at 60°N latitude
* __Phhh__ : P is a constant character. hhh is the forecast hour [000, 001, 002, ..., 048]
* __nc__ : Constant string indicating the NetCDF format


Filenames examples : 

* 20200913T06Z_MSC_RIOPS_IICEVOL_SFC_PS5km_P012.nc 
* 20200913T12Z_MSC_RIOPS_VOSALINE_DBS-all_PS5km_P046.nc
* 20201014T00Z_MSC_RIOPS_VOTEMPER_DBS-0.5m_PS5km_P022.nc

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

If you have any questions about this data, please contact us at: [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).