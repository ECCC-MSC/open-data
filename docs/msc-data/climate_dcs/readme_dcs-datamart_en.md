[En français](readme_dcs-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [DCS](readme_dcs_en.md) > DCS on MSC Datamart

# Climate scenarios datasets based on an ensemble of global climate model projections from the Coupled Model Intercomparison Project Phase 5 (CMIP5) in NetCDF format

Statistically downscaled multi-model ensembles of modelled output and projected changes are available for historical simulations and three emission scenarios, RCP2.6, RCP4.5, RCP8.5, at a 10km resolution.  Projected changes are expressed as anomalies with respect to the reference period of 1986-2005.

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available via the HTTP protocol. It is possible to access it with a standard browser. In this case, we obtain a list of links giving access to a NetCDF file.

The data can be accessed at the following URLs :

* [https://dd.weather.gc.ca/climate/dcs/netcdf/historical/annual/{[anomaly,absolute]}](https://dd.weather.gc.ca/climate/dcs/netcdf/historical/annual)
* [https://dd.weather.gc.ca/climate/dcs/netcdf/historical/seasonal/{[DJF,MAM,JJA,SON]}/{[anomaly,absolute]}](https://dd.weather.gc.ca/climate/dcs/netcdf/historical/seasonal)
* [https://dd.weather.gc.ca/climate/dcs/netcdf/historical/monthly_ens/absolute](https://dd.weather.gc.ca/climate/dcs/netcdf/historical/monthly_ens/absolute)
* [https://dd.weather.gc.ca/climate/dcs/netcdf/scenarios/{[RCP2.6,RCP4.5,RCP8.5]}/annual/{[anomaly,absolute,avg_20years]}](https://dd.weather.gc.ca/climate/dcs/netcdf/scenarios)                                                                
* [https://dd.weather.gc.ca/climate/dcs/netcdf/scenarios/{[RCP2.6,RCP4.5,RCP8.5]}/seasonal/{[DJF,MAM,JJA,SON]}/{[anomaly,absolute,avg_20years]}](https://dd.weather.gc.ca/climate/dcs/netcdf/scenarios)                                                                     
* [https://dd.weather.gc.ca/climate/dcs/netcdf/scenarios/{[RCP2.6,RCP4.5,RCP8.5]}/monthly_ens/absolute](https://dd.weather.gc.ca/climate/dcs/netcdf/scenarios)

where :

* __historical__ : Historical simulations from 1950-2005
* __scenarios__ : Refers to different emission scenarios [RCP2.6, RCP4.5,RCP8.5] from 2006-2100
* __seasonal__ : The standard meteorological seasons are used: (March to May (MAM, spring), June to August (JJA, summer),September to November (SON, autumn/fall), and December to February (DJF, winter)]
* __avg_20year__ : 20-year averages of projected change are available for four future time periods: 2021-2040; 2041-2060; 2061-2080; 2081-2100
* __Anomaly__ : Represents projected change to the reference period, 1986-2005
* __Absolute__ : Represents the multi-modelled ensemble projections (actual value)

## File name nomenclature 

NOTE: ALL HOURS ARE IN UTC.

* DCS_hist_TemporalResolution_Value_ProjectionResolution_Variable_pctlPP_TimeStep.nc
* DCS_rcpx.y_TemporalResolution_Value_ProjectionResolution_Variable_pctlPP_TimeStep.nc

where :

* __DCS__ : Constant string indicating Coupled Model Intercomparison Project Phase5 global climate model ensemble datasets.
* __hist__ : Constant string indicating historical simulations.
* __rcpx.y__ : Type of Representative Concentration Pathways (emission scenarios), taking one of the values : [rcp2.6, rcp4.5, rcp8.5].
* __TemporalResolution__ : Time period, taking one of the values : [annual, monthly, DJF, MAM, JJA, SON].
* __Value__ : Values category, taking one of the values :  [ abs, anom, 2021-2040, 2041-2060, 2061-2080, 2081-2100]; abs stands for absolute values (actual values / modelled projections); anom stands for anomalies.
* __Projection__ : Grid mapping (projection) taking the value : [latlon].
* __Resolution__ : Grid resolution taking one of the values : [1x1]; 1x1 stands for 1-degree grid resolution in both the latitudinal and longitudinal directions.
* __Variable__ : Name of climate variable available in the file, taking one of the values : [PCP, TEMP, , SICETHKN, SICECONC, SNDPT, SFCWND]; PCP stands for mean precipitation, TEMP for mean temperature, , SICETHKN stands for sea ice thickness, SICECONC stands for sea ice concentration, SNDPT stands for snow depth, SFCWND stands for surface wind speed.
* __PctlPP__ : Ensemble percentile, taking one of the values : [pctl5, pctl25, pctl50, pctl75, pctl95]; pctl5 stands for the 5th percentile of the ensemble; pctl25 stands for the 25th percentile of the ensemble; pctl50 stands for the 50th percentile, also referred to as the median, of the ensemble; pctl75 stands for the 75th percentile of the ensemble; pctl95 stands for the 95th percentile of the ensemble.
* __TimeStep__ : Time step, taking one of the values : [P1Y, P1M]; P1Y stand for 1 year time step and P1M stands for 1 month time step.
* __nc__ : Constant string indicating the NetCDF format.

Example : DCS_rcp4.5_DJF_2021-2040_latlon0.086x0.086_PCP_pctl50_P1Y.nc

The file represents the 50th percentile of the statistically downscaled multi-model ensemble of projected relative changes in total precipitation (i.e., anomalies) averaged for 2021-2040 under the emission scenario of RCP4.5, with respect to the reference period of 1986-2005, in winter (3 month average across December, January, February), expressed as percentage change. The bands in the NetCDF file are yearly time steps.

## List of variables

The available variables and units for the statistically downscaled multimodel ensembles are :

* Statistically downscaled multi-model ensembles of mean temperature (°C)
* Statistically downscaled multi-model ensembles of minimum temperature (°C)
* Statistically downscaled multi-model ensembles of maximum temperature (°C)
* Statistically downscaled multi-model ensembles of total precipitation (mm/day)
* Projected changes in mean temperature based on statistically downscaled multi-model ensembles (°C)
* Projected changes in minimum temperature based on statistically downscaled multi-model ensembles (°C)
* Projected changes in maximum temperature based on statistically downscaled multi-model ensembles (°C)
* Projected relative changes in total precipitation based on statistically downscaled multi-model ensembles (%)

## Support

If you have any questions about this data, please contact us at : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).


