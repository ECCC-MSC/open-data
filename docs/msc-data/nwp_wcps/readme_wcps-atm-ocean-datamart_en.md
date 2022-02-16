[In French](readme_wcps_wf-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC Open Data](../readme_en.md) > [WCPS](readme_wcps_en.md) > Coupled WCPS ocean-atmosphere on MSC Datamart 

# Water Cycle Prediction System (WCPS) coupled atmosphere-ocean-sea ice forecasts data in NetCDF format

The coupled atmosphere-ocean-sea ice forecasts of GEM-LAM coupled with NEMO-CICE from WCPS are available as hourly products. These products are in NetCDF format with a latitude and longitude grid, corresponding to about 1km resolution (0.008 x 0.008 degree), over the domain of the Great Lakes, St. Lawrence Rivers and the Gulf of St. Lawrence.

## Data location 

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available using the HTTPS protocol and resides in a directory that is plainly accessible to a web browser. Visiting that directory with an interactive browser will yield a raw listing of links, each link being a downloadable NetCDF file.

The data can be accessed at the following URLs: 

* [https://dd.weather.gc.ca/model_wcps/ocean-atmosphere/1km/{HH}/{hhh}/](https://dd.weather.gc.ca/model_wcps/ocean-atmosphere/1km)                  

where:

* __HH__ : Model run start, in UTC [00,06,12,18]
* __hhh__ : Forecast hour [001, ..., 084] 

A 24h history is kept in this directory.

## Technical specification of the grid

![Image of the coupled WCPS ocean-atmosphere domain](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_wcps/grille_wcps_ocean-atm.png)

In the full domain shown in white, the valid dataset that covers lakes and oceans, is in color. In the rest of the domain, a "no-data" mask is used to specify the absence of data.

| Parameter | Value |
| ------ | ------ |
| ni | 6675 |
| nj | 2364 |
| resolution at 45° N | 1km |

## Filename nomenclature

NOTE: ALL HOURS ARE IN UTC.

The files have the following nomenclature: 

`{YYYYMMDD}T{HH}Z_MSC_WCPS_{VAR}_{LVLTYPE}-{LVL}_{grille}{resolution}_PT{hhh}H.nc`

where:

* __YYYYMMDD__: Year, month and day of the beginning of the forecast
* __T__ : Time delimiter according to ISO8601 norms
* __HH__: UTC run time [00, 06, 12, 18]
* __Z__ : Time zone (UTC hour)
* __MSC__ : Constant string indicating that the data is from the Meteorologcal Service of Canada (MSC)
* __WCPS__ : Constant string indicating that the data is from Water Cycle Prediction System
* __VAR__ : Variables included in this file 
* __LVLTYPE__ : Vertical level type [Sfc for the surface, DBS for depth below the surface, AGL for fixed height above ground]
* __LVL__ : Vertical level value [10m, 0.5m, 1.5m, `0-2m` from surface to 2 meters, `all` for all available levels]
* __grille__ : Constant string indicating the latitude and longitude projection [LatLon]
* __resolution__ : Resolution in degree 0.008 (about 1km) in both latitude and longitude directions 
* __PT{hhh}H__: Forecast hours based on [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) norms. P, T and H are constant character designating Period, Time and Hour. "hhh" is the forecast hour [001, 001, 002, ..., 084]
* __nc__ : constant string indicating the NetCDF format

Examples:

* 20211208T12Z_MSC_WCPS_SeaIceSnowVol_Sfc_LatLon0.008_PT001H.nc
* 20211208T12Z_MSC_WCPS_SoilLiquidWaterCont_DBS-all_LatLon0.008_PT001H.nc

## List of variables 

List of 2D variables available in the files: 

* __AirTemp__ : 1.5m surface air temperature (K)
* __WindU__: 10m surface wind X velocity (m/s) 
* __WindV__: 10m surface wind Y velocity (m/s)
* __Runoff__ : Runoff (mm)
* __SeaSfcHeight__ : Sea surface height above geoid (m)
* __SeaWaterSalinity__ : Sea water salinity at the surface model layer (per 1000) 
* __SeaWaterPotentialTemp__ : Sea water potential temperature at the surface model layer (K)
* __SeaWaterVelocityX__ : Sea water X velocity at the surface model layer (m/s)
* __SeaWaterVelocityY__ : Sea water Y velocity at the surface model layer (m/s)
* __MixedLayerThickness__ : Ocean mixed layer depth based on density criterion (m)
* __TurboclineDepth__ : Turbocline depth (m)
* __SeaIceVelocityX__ : Sea ice X velocity (m/s)
* __SeaIceVelocityY__ : Sea ice Y velocity (m/s)
* __SeaIceAreaFraction__ : Sea ice area fraction (fraction)
* __SeaIceVol__ : Sea ice volume per unit grid cell area (m)
* __SeaIceSnowTemp__ : Surface temperature of snow over sea ice or bare sea ice (K)
* __SeaIceSnowVol__ : Volume of snow on sea ice per unit grid cell area (cm)
* __SeaIceCompressiveStrength__ : Depth-integrated compressive sea ice strength (N/m)
* __SeaIceDivergence__ : Sea ice divergence (%/day)
* __SeaIceInternalPressure__ : Depth-integrated internal sea ice pressure (N/m)
* __SeaIceShear__ : Sea ice shea (%/day)

The variables `AirTemp`, `WindU`, `WindV` and `Runoff` are from GEM-LAM and the rests are from NEMO-CICE. 

## Support

If you have any questions about this data, please contact us at: [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Announcements from the dd_info mailing list

Announcements related to this dataset are available in the [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).

