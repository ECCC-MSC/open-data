[In French](readme_spcog-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC Open Data](../readme_en.md) > [CIOPS](readme_ciops_en.md) > Coastal Ice Ocean Prediction System (CIOPS) on MSC Datamart 

# Coastal Ice Ocean Prediction System (CIOPS) ocean-ice forecasts data in NetCDF format

The ocean-ice forecasts of NEMO-CICE from the CIOPS-East and CIOPS-West systems are available as hourly products. These products are available in NetCDF format on a latitude and longitude grid. The CIOPS-East domain covers the Gulf of St. Lawrence, the North West Atlantic and the east coast of Canada at a resolution of 2km (0.03 x 0.02 degree). The CIOPS-West main domain covers the North East Pacific and the west coast of Canada, also at a resolution of 2km (0.03 x 0.02 degree). The CIOPS-West system also outputs a regional enhancement at 500m resolution (0.008 x 0.005 degree) that covers the Salish Sea region only.

## Data location 

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available using the HTTPS protocol and resides in a directory that is plainly accessible via web browser. Visiting that directory with an interactive browser will yield a raw listing of links, each link being a downloadable NetCDF file.

The data can be accessed at the following URLs: 

* [https://dd.weather.gc.ca/model_ciops/east/2km/{HH}/{hhh}/](https://dd.weather.gc.ca/model_ciops/east/2km)
* [https://dd.weather.gc.ca/model_ciops/west/2km/{HH}/{hhh}/](https://dd.weather.gc.ca/model_ciops/west/2km)
* [https://dd.weather.gc.ca/model_ciops/salish-sea/500m/{HH}/{hhh}/](https://dd.weather.gc.ca/model_ciops/salish-sea/500m)                  

where:

* __HH__ : Model run start, in UTC [00,06,12,18]
* __hhh__ : Forecast hour [001, ..., 084] 

A 24h history is kept in this directory.

## Technical specification of the grid

![Image of the CIOPS - East ocean domain](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_ciops/grille_ciops-east.png)

| Parameter | Value |
| ------ | ------ |
| ni | 1333 |
| nj | 980 |
| nk | 99 |
| resolution | 2km |

![Image of the CIOPS - West ocean domain](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_ciops/grille_ciops-west.png)

| Parameter | Value |
| ------ | ------ |
| ni | 600 |
| nj | 785 |
| nk | 68 |
| resolution | 2km |

![Image of the CIOPS - Salish Sea ocean domain](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_ciops/grille_ciops-salishsea.png)

In the full domain shown in white, the valid dataset that covers lakes and oceans, is in color. In the rest of the domain, a "no-data" mask is used to specify the absence of data.

| Parameter | Value |
| ------ | ------ |
| ni | 629 |
| nj | 888 |
| nk | 39 |
| resolution | 500km |

## Filename nomenclature

NOTE: ALL HOURS ARE IN UTC.

The files have the following nomenclature: 

`{YYYYMMDD}T{HH}Z_MSC_CIOPS-{DOMAIN}_{VAR}_{LVLTYPE}-{LVL}_{grid}{resolution}_PT{hhh}H.nc`

where:

* __YYYYMMDD__: Year, month and day of the beginning of the forecast
* __T__ : Time delimiter according to ISO8601 norms
* __HH__: UTC run time [00, 06, 12, 18]
* __Z__ : Time zone (UTC hour)
* __MSC__ : Constant string indicating that the data is from the Meteorologcal Service of Canada (MSC)
* __CIOPS__ : Constant string indicating that the data is from the Coastal Ice Ocean Prediction System
* __DOMAIN__ : One of East, West or SalishSea indicating the domain
* __VAR__ : Variable included in the file 
* __LVLTYPE__ : Vertical level type [Sfc for the surface, DBS for depth below the surface]
* __LVL__ : Vertical level value where applicable [0.5m, `all` for all available levels]
* __grid__ : Constant string indicating the grid projection [here, LatLon]
* __resolution__ : Resolution in degree (latitude x longitude) 
* __PT{hhh}H__: Forecast hours based on [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) norms. P, T and H are constant character designating Period, Time and Hour. "hhh" is the forecast hour [001, 001, 002, ..., 084]
* __.nc__ : file extention indicating the NetCDF format

Examples:

* 20220225T00Z_MSC_CIOPS-East_SeaIceDivergence_Sfc_LatLon0.03x0.02_PT002H.nc
* 20220301T00Z_MSC_CIOPS-West_SeaWaterSalinity_DBS-0.5m_LatLon0.03x0.02_PT002H.nc
* 20220301T00Z_MSC_CIOPS-SalishSea_SeaWaterPotentialTemp_DBS-all_LatLon0.008x0.005_PT002H.nc

## List of variables 

List of available 3D ocean variable files: 

* __SeaWaterSalinity__ : Sea water salinity (psu) 
* __SeaWaterPotentialTemp__ : Sea water potential temperature (K)
* __SeaWaterVelocityX__ : Sea water X velocity (m/s)
* __SeaWaterVelocityY__ : Sea water Y velocity (m/s)

List of available 2D ocean variable files: 

* __SeaWaterSalinity__ : Sea water salinity at the surface model layer (psu) 
* __SeaWaterPotentialTemp__ : Sea water potential temperature at the surface model layer (K)
* __SeaWaterVelocityX__ : Sea water X velocity at the surface model layer (m/s)
* __SeaWaterVelocityY__ : Sea water Y velocity at the surface model layer (m/s)
* __SeaSfcHeight__ : Sea surface height above geoid (m).
* __MixedLayerThickness__ : Ocean mixed layer depth based on density criterion (m)
* __TurboclineDepth__ : Turbocline depth (m)

List of available 2D ice variables files for CIOPS-East only:

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

## Support

If you have any questions about this data, please contact us at: [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Announcements from the dd_info mailing list

Announcements related to this dataset are available in the [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).

