[In French](readme_cmip6-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_en.md) > [MSC Data](../readme_en.md) > [CMIP6](readme_cmip6_en.md) > CMIP6 on the MSC Datamart

# Climate scenario data, based on a set of global climate model projections from phase 6 of the Coupled Model Intercomparison Project (CMIP6) in NetCDF format

Multimodel ensembles for a range of variables based on global climate model (GCM) projections from Phase 6 of the Coupled Model Intercomparison Project (CMIP6) are available for 1900 to 2100 on a common 1 x 1 degree global grid.

## Data address 

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](.../.../msc-datamart/amqp_en.md) as soon as they become available. An overview and examples of how to access and use Meteorological Service of Canada open data](../../usage/readme_en.md) is also available.

The data is available via the HTTPS protocol. It can be accessed using a standard browser. In this case, a list of links to a NetCDF file is displayed.

CMIP6 files can be found at the following address:

* https://dd.weather.gc.ca/climate/cmip6/100km/historical/
* https://dd.weather.gc.ca/climate/cmip6/100km/scenarios/{ssp126,ssp245,ssp370,ssp585}                                                         

where:

* __historical__: Historical simulations over the period 1900-2014
* __scenarios__ : Refers to different shared socioeconomic profiles [ssp126, ssp245, ssp370, ssp585] for several 20-year periods, i.e. short term [2021-2040], medium term [2041-2060 and 2061-2080] and end of century [2081-2100].

## Nomenclature of file names

* `{period}_ECCC_CMIP6_{variable}-Pct{percentile}_Sfc_LatLon1.0_{timestep}.nc`
* `{period}_ECCC_CMIP6-{scenario}_{variable}-Pct{percentile}_Sfc_LatLon1.0_{timestep}.nc`

with :

* __period__: Period associated with each data set, in {year of period start}-{year of period end} format: [1900-2014; 2015-2100; etc.].
* __ECCC__ : Constant character string for Environment and Climate Change Canada, the data source
* __CMIP6__ : Constant string indicating the data sets for phase 6 of the Coupled Model Intercomparison Project
* __variable__: Name of the climate variable available in the file, taking one of the following values: [AirTemp, Precip, SeaIceConcentration, SeaIceThickness, Wind, SnowDepth]. For anomalies: [AirTempAnomaly, PrecipAnomaly, SeaIceConcentrationAnomaly, SeaIceThicknessAnomaly, WindAnomaly, SnowDepthAnomaly]
* __scenario__ : Shared Socioeconomic Profiles (SSP), taking one of the values: [SSP126, SSP245, SSP370, SSP585]
* __percentile__: Ensemble percentile, taking one of the values: [Pct5, Pct25, Pct50, Pct75, Pct95]; Pct5 represents the 5th ensemble percentile; Pct25 represents the 25th ensemble percentile, etc.
* __Sfc__ : Constant character string indicating that data are available on the surface
* __LatLon__ : Constant string indicating lat-lon grid projection 
* __1.0__: Grid resolution of 1 degree in latitudinal and longitudinal directions
* __timeStep__ : Time step, taking one of the following values: [P1Y, P1M]; P1Y represents a time step of one year, P1M represents a time step of one month; [P1Y-{DJF, MAM, JJA, SON}] represents the seasonal period (ex: DJF: December-January-February) ; [P0Y-{DJF, MAM, JJA, SON}] represents the average over 20 years, P0Y indicates a single period of time in the file
* __nc__: Constant string indicating NetCDF format

Examples:

* 1900-2014_ECCC_CMIP6_AirTempAnomaly-Pct50_Sfc_LatLon1.0_P1M.nc
* 1900-2014_ECCC_CMIP6_SeaIceThickness-Pct25_Sfc_LatLon1.0_P1Y-SON.nc
* 2015-2100_ECCC_CMIP6-SSP370_Precip-Pct05_Sfc_LatLon1.0_P1M.nc
* 2015-2100_ECCC_CMIP6-SSP126_PrecipAnomaly-Pct50_Sfc_LatLon1.0_P1Y-JJA.nc

## List of variables

The variables and units available for CMIP6 datasets on the MSC Datamart are :

* CMIP6 ensemble multi-model mean precipitation projections (mm/day)
* CMIP6 ensemble multi-model sea ice concentration projections (percentage, %, of grid cell area)
* CMIP6 ensemble multi-model sea ice thickness projections (m)
* CMIP6 ensemble multi-model snow depth projections (m)
* CMIP6 ensemble multi-model surface wind speed projections (m/s)
* CMIP6 ensemble multi-model mean temperature projections (°C)
* Projected mean change in precipitation, based on CMIP6 ensemble multi-models (%)
* Projected change in sea ice concentration based on CMIP6 multimodel ensembles (%) 
* Projected change in sea ice thickness based on CMIP6 multimodel ensembles (%)
* Projected variation in snow depth based on CMIP6 multimodel ensembles (%)
* Projected change in surface wind speed based on CMIP6 multimodel ensembles (%)
* Projected mean temperature change based on CMIP6 multimodel ensembles (°C)

## Support

If you have any questions about these data, please [contact us](mailto:info.cccs-ccsc@canada.ca).

## dd_info mailing list announcements 

Announcements related to this dataset are available via the [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/) list.




















[En français](readme_cmip6-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [CMIP6](readme_cmip5_fr.md) > CMIP6 on MSC Datamart

# ClimMulti-model ensembles for a suite of variables based on projections from Coupled Model Intercomparison Project Phase 6 (CMIP6) global climate models (GCMs) are available for 1850-2100 on a common 1x1 degree global grid.


Multi-model ensembles of modelled output and projected change are available for historical simulations and three emission scenarios, RCP2.6, RCP4.5 and RCP8.5, at a 1x1 degree grid resolution. Projected changes are expressed as anomalies with respect to the reference period of 1986-2005. 

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available via the HTTPS protocol. It is possible to access it with a standard browser. In this case, we obtain a list of links giving access to a NetCDF file.

The data can be accessed at the following URLs :

* [https://dd.weather.gc.ca/climate/cmip6/netcdf/historical/annual/{[anomaly,absolute]}](https://dd.weather.gc.ca/climate/cmip6/netcdf/historical/annual)
* [https://dd.weather.gc.ca/climate/cmip6/netcdf/historical/seasonal/{[DJF,MAM,JJA,SON]}/{[anomaly,absolute]}](https://dd.weather.gc.ca/climate/cmip6/netcdf/historical/seasonal)
* [https://dd.weather.gc.ca/climate/cmip6/netcdf/historical/monthly_ens/absolute](https://dd.weather.gc.ca/climate/cmip6/netcdf/historical/monthly_ens/absolute)
* [https://dd.weather.gc.ca/climate/cmip6/netcdf/scenarios/{[RCP2.6,RCP4.5,RCP8.5]}/annual/{[anomaly,absolute,avg_20years]}](https://dd.weather.gc.ca/climate/cmip6/netcdf/scenarios)                                                                
* [https://dd.weather.gc.ca/climate/cmip6/netcdf/scenarios/{[RCP2.6,RCP4.5,RCP8.5]}/seasonal/{[DJF,MAM,JJA,SON]}/{[anomaly,absolute,avg_20years]}](https://dd.weather.gc.ca/climate/cmip6/netcdf/scenarios)                                                                     
* [https://dd.weather.gc.ca/climate/cmip6/netcdf/scenarios/{[RCP2.6,RCP4.5,RCP8.5]}/monthly_ens/absolute](https://dd.weather.gc.ca/climate/cmip6/netcdf/scenarios)

where :

* __historical__ : Historical simulations from 1950-2005
* __scenarios__ : Refers to different emission scenarios [RCP2.6, RCP4.5,RCP8.5] from 2006-2100
* __seasonal__ : The standard meteorological seasons are used: (March to May (MAM, spring), June to August (JJA, summer),September to November (SON, autumn/fall), and December to February (DJF, winter)]
* __avg_20year__ : 20-year averages of projected change are available for four future time periods: 2021-2040; 2041-2060; 2061-2080; 2081-2100
* __Anomaly__ : Represents projected change to the reference period, 1986-2005
* __Absolute__ : Represents the multi-modelled ensemble projections (actual value)

## File name nomenclature 

NOTE : ALL HOURS ARE IN UTC.

* CMIP6_hist_TemporalResolution_Value_ProjectionResolution_Variable_pctlPP_TimeStep.nc
* CMIP6_rcpx.y_TemporalResolution_Value_ProjectionResolution_Variable_pctlPP_TimeStep.nc

where:

* __CMIP6__ : Constant string indicating Coupled Model Intercomparison Project Phase6 global climate model ensemble datasets.
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

Example : CMIP6_rcp4.5_DJF_2021-2040_latlon1x1_PCP_pctl50_P1Y.nc

The file represents the 50th percentile of the CMIP6 multi-model ensemble of projected relative changes in mean precipitation (i.e., anomalies) with respect to the reference period of 1986-2005, in winter (3 month average across December, January, February), expressed as percentage change. The bands in the NetCDF file are yearly time steps.


## List of variables

The available variables and units for the CMIP6 datasets on the MSC Datamart are :

* CMIP6 multi-model ensembles of mean precipitation projections (mm/day)
* CMIP6 multi-model ensembles of sea ice concentration projections (percentage, %, of grid cell area)
* CMIP6 multi-model ensembles of sea ice thickness projections (m)
* CMIP6 multi-model ensembles of snow depth projections (m)
* CMIP6 multi-model ensembles of surface wind speed projections (m/s)
* CMIP6 multi-model ensembles of mean temperature projections (°C)
* Projected mean precipitation change based on CMIP6 multi-model ensembles (%)
* Projected sea ice concentration change based on CMIP6 multi-model ensembles (%) 
* Projected sea ice thickness change based on CMIP6 multi-model ensembles (%)
* Projected snow depth change based on CMIP6 multi-model ensembles (%)
* Projected surface wind speed change based on CMIP6 multi-model ensembles (%)
* Projected mean temperature change based on CMIP6 multi-model ensembles (°C)

## Support

If you have any questions about this data, please [contact us](mailto:info.cccs-ccsc@canada.ca).

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).

