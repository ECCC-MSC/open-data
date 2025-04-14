[In French](readme_cmip6-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_en.md) > [MSC Data](../readme_en.md) > [CMIP6](readme_cmip6_en.md) > CMIP6 on the MSC Datamart

# Climate scenario data, based on a set of global climate model projections from phase 6 of the Coupled Model Intercomparison Project (CMIP6) in NetCDF format

Multimodel ensembles for a range of variables based on global climate model (GCM) projections from Phase 6 of the Coupled Model Intercomparison Project (CMIP6) are available for 1900 to 2100 on a common 1 x 1 degree global grid.

## Data address 

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. [An overview and examples of how to access and use Meteorological Service of Canada open data](../../usage/readme_en.md) is also available.

The data is available via the HTTPS protocol. It can be accessed using a standard browser. In this case, a list of links to a NetCDF file is displayed.

CMIP6 files can be found at the following address:

* [https://dd.weather.gc.ca/climate/cmip6/100km/historical/](https://dd.weather.gc.ca/climate/cmip6/100km/historical)
* [https://dd.weather.gc.ca/climate/cmip6/100km/scenarios/{ssp126,ssp245,ssp370,ssp585}](https://dd.weather.gc.ca/climate/cmip6/100km/scenarios)                                                         

where:

* __historical__: Historical simulations over the period 1900-2014
* __scenarios__ : Refers to different shared socioeconomic profiles [ssp126, ssp245, ssp370, ssp585] for several 20-year periods, i.e. short term [2021-2040], medium term [2041-2060 and 2061-2080] and end of century [2081-2100].

## Nomenclature of file names

The files have the following nomenclature:

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
