[In French](readme_wcps-nemo-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC Open Data](../readme_en.md) > [WCPS](readme_wcps_en.md) > WCPS-NEMO on MSC Datamart 

# Water Cycle Prediction System (WCPS) NEMO data in NetCDF over the Great Lakes and St. Lawrence River 

NEMO netCDF files from Water Cycle Prediction System (WCPS) are available with a latitude and longitude grid of 1681x3181 grid points, corresponding to a 1km resolution (0.009 x 0.009 degree).

## Data location 

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available using the HTTP protocol and resides in a directory that is plainly accessible to a web browser. Visiting that directory with an interactive browser will yield a raw listing of links, each link being a downloadable NetCDF file.

The data can be accessed at the following URLs: 

* [https://dd.meteo.gc.ca/model_wcps/nemo/netcdf/lat_lon/{nd}/{HH}/{hhh}/ ](https://dd.meteo.gc.ca/model_wcps/nemo/netcdf/lat_lon)                  

where :

* __nd__ : Spatial dimension, latitude and longitude  [2d]
* __HH__ : Model run start, in UTC [00,12]
* __hhh__ : Forecast hour [001, ..., 084] 

A 30 day history is kept in this directory.

## Technical specification of the grid
![](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_wcps/grille_wcps_nemo.png)

In the complete domain indicated by the black rectangle, the valide domain, which covers the lakes, is in color. 

| Parameter | Value |
| ------ | ------ |
| ni | 1681 |
| nj | 3181 | 
| resolution at 45° N | 1km |

## Filename nomenclature

Note : all hours are in UTC. 

The files have the following nomenclature : 

CMC_wcps-nemo_Variable_LevelType_Level_ProjectionResolution_YYYYMMDDHH_Phhh.nc

where :

* __CMC__ : constant string indicating that the data is from the Canadian Meteorological Centre (CMC)
* __wcps_nemo__ : constant string indicating that the data is from WCPS-NEMO component 
* __Variable__ : Variable type included in this file  
* __LevelType__ : Level type [sfc, depth, tgl]
* __Level__ : Level value: 0 for sfc (surface), 0.5 for depth (lake depth in meters), 40 for tgl (altitude in meter) 
* __Projection__ : constant string indicating the latitude and longitude projection [latlon]
* __Resolution__ : 0.009x0.009. resolution in degree (about 1km) in latitude and longitude directions 
* __YYYYMMDD__ : Year, month and days of the beginning of the forecast 
* __HH__ : UTC run time [00,12]
* __Phhh__ : P constant character, hhh the forecast hour [001,002, ..., 084] 
* __nc__ : constant string indicating the NetCDF format

Example :

* CMC_wcps_nemo_vomecrty_depth_0.5_latlon0.009x0.009_2019011100_P036.nc

## List of variables 

List of variables available in the files containing 2D variables : 

* __tairsurf__ : Air temperature at about 40 meters in height
* __uwindsurf__ : Wind X velocity at about 40 meters in height 
* __vwindsurf__ : Wind Y velocity at about 40 meters in height 
* __vozocrtx__ : Sea water X velocity at the first model layer 
* __vomecrty__ : Sea water Y velocity at the first model layer  
* __votemper__ : Sea water potential temperature at the first model layer  
* __vosaline__ : Sea water salinity at the surface   
* __sossheig__ : Sea surface height above geoid 
* __sokaraml__ : Ocean mixed layer depth based on density criterion 
* __iiceconc__ : Sea ice area fraction 
* __iicevol__ : Sea ice volume per unit grid cell area
* __itzocrtx__ : Sea ice X velocity 
* __itmecrty__ : Sea ice Y velocity 
* __iicepressure__ : Depth-integrated internal sea ice pressure
* __iicestrength__ : Depth-integrated compressive sea ice strength

## Support

If you have any questions about these data, please contact us at: [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Announcements from the dd_info mailing list

Announcements related to this dataset are available in the [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).

