[In French](readme_wcps_wf-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC Open Data](../readme_en.md) > [WCPS](readme_wcps_en.md) > WCPS-NEMO on MSC Datamart 

# Water Cycle Prediction System (WCPS) Coupled Atmosphere-ocean-sea ice Forecasts data in NetCDF

The coupled atmosphere-ocean-sea ice forecasts of GEM LAM coupled with NEMO-CICE from WCPS are available as hourly products. These products are in NetCDF format with a latitude and longitude grid, corresponding to about 1km resolution (0.008 x 0.008 degree), over the domain of the Great Lakes, St. Lawrence Rivers and the Gulf of St. Lawrence.


## Data location 

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available using the HTTPS protocol and resides in a directory that is plainly accessible to a web browser. Visiting that directory with an interactive browser will yield a raw listing of links, each link being a downloadable NetCDF file.

The data can be accessed at the following URLs: 

* [https://dd.meteo.gc.ca/model_wcps/nemo/netcdf/lat_lon/{nd}/{HH}/{hhh}/](https://dd.meteo.gc.ca/model_wcps/nemo/netcdf/lat_lon)                  

where:

* __nd__ : Spatial dimension, latitude and longitude [2d]
* __HH__ : Model run start, in UTC [00,06,12,18]
* __hhh__ : Forecast hour [001, ..., 084] 

A 30 day history is kept in this directory.

## Technical specification of the grid

![Image of the WCPS-NEMO domain](https://goc-dx.science.gc.ca/~yls000/DD_netcdf/wcps_wf_CI3_nc_domain.png)
In the complete domain indicated by the white rectangle, the valide domain, which covers the lakes and oceans, is in color.

| Parameter | Value |
| ------ | ------ |
| ni | 6675 |
| nj | 2364 |
| resolution at 45° N | 1km |

## Filename nomenclature

NOTE: ALL HOURS ARE IN UTC.

The files have the following nomenclature: 

YYYYMMDDTHHZ_MSC_WCPS_Variable_LevelType_Level_ProjectionResolution_Phhh.nc

where:

* __YYYYMMDD__ : Year, month, and days of the beginning of the forecast
* __THHZ__ : T constant character, HH the run time [00,06,12,18], Z constant character indicating UTC time
* __MSC__ : Constant string indicating that the data is from the Meteorologcal Service of Canada (MSC)
* __WCPS__ : Constant string indicating that the data is from WCPS 
* __Variable__ : Variable type included in this file 
* __LevelType-Value__ : SFC for Surface (SFC), DBS-0.5m for Depth Below Surface (DBS), AGL-1.5m or AGL-10m for Above Ground Level (AGL)
* __Projection__ : Constant string indicating the latitude and longitude projection [latlon]
* __Resolution__ : Resolution in degree 0.008 (about 1km) in both latitude and longitude directions 
* __Phhh__ : P constant character, hhh the forecast hour [001,002, ..., 084] 
* __nc__ : constant string indicating the NetCDF format

Example:

* 20211208T12Z_MSC_WCPS_SOSSHEIG_SFC_LatLon0.008_P001.nc

## List of variables 

List of 2D variables available in the files: 

* __TAIRSURF__ : 1.5m surface air temperature (K)
* __UWINDSURF__: 10m surface wind X velocity (m/s) 
* __VWINDSURF__: 10m surface wind Y velocity (m/s)
* __RUNOFFSURF__ : Surface runoff (mm)
* __SOSSHEIG__ : Sea surface height above geoid (m)
* __VOSALINE__ : Sea water salinity at the surface model layer (per 1000) 
* __VOTEMPER__ : Sea water potential temperature at the surface model layer (K)
* __VOZOCRTX__ : Sea water X velocity at the surface model layer (m/s)
* __VOMECRTY__ : Sea water Y velocity at the surface model layer (m/s)
* __SOKARAML__ : Ocean mixed layer depth based on density criterion (m)
* __SOMIXHGT__ : Turbocline depth (m)
* __ITZOCRTX__ : Sea ice X velocity (m/s)
* __ITMECRTY__ : Sea ice Y velocity (m/s)
* __IICECONC__ : Sea ice area fraction (fraction)
* __IICEVOL__ : Sea ice volume per unit grid cell area (m)
* __IICESURFTEMP__ : Surface temperature of snow over sea ice or bare sea ice (K)
* __ISNOWVOL__ : Volume of snow on sea ice per unit grid cell area (cm)
* __IICESTRENGTH__ : Depth-integrated compressive sea ice strength (N/m)
* __IICEDIVERGENCE__ : Sea ice divergence (%/day)
* __IICEPRESSURE__ : Depth-integrated internal sea ice pressure (N/m)
* __IICESHEAR__ : Sea ice shea (%/day)

The variables of TAIRSURF, UWINDSURF, and UWINDSURF are from GEM-LAM and the rests are from NEMO-CICE. 

## Support

If you have any questions about this data, please contact us at: [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Announcements from the dd_info mailing list

Announcements related to this dataset are available in the [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).

