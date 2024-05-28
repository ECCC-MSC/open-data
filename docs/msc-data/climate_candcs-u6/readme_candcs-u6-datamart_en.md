[In French](readme_candcs-u6-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_en.md) > [MSC Data](../readme_en.md) > [CanDCS-U6](readme_candcs-u6_en.md) > CanDCS-U6 on the MSC Datamart

# Statistically scaled climate scenario data from CMIP6 global climate models (CanDCS-U6) in NetCDF format

Multimodel ensembles of model outputs and projected gridded changes are available for historical simulations and four emission scenarios, SSP126, SSP245 and SSP585, at 1/10th degree resolution. Projected changes are expressed as anomalies relative to the 1950-2014 and 1971-2000 reference periods.
.

## Data address 

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](.../.../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples of how to access and use Meteorological Service of Canada open data](../../usage/readme_en.md) is also available.

The data is available via the HTTPS protocol. It can be accessed using a standard browser. In this case, a list of links to a NetCDF file is displayed.

CanDCS-U6 files can be found at the following address:

* [https://dd.weather.gc.ca/climate/candcsu6/10km/historical/](https://dd.weather.gc.ca/climate/candcsu6/10km/historical)
* [https://dd.weather.gc.ca/climate/candcsu6/10km/scenarios/{ssp126,ssp245,ssp585}](https://dd.weather.gc.ca/climate/candcsu6/10km/scenarios)

where :

* __historical__: Historical simulations for the periods 1950-2014 and 1971-2000
* __scenarios__ : Refers to different future emission scenarios [ssp126, ssp245, ssp585] for several periods, i.e. 2015-2100, 2021-2050 and 2041-2070 and 2071-2100

## Nomenclature of file names

The files have the following nomenclature:

* `{period}_ECCC_CanDCSU6_{variable}-Pct{percentile}_Sfc_LatLon0.86_{timestep}.nc`
* `{period}_ECCC_CanDCSU6-{scenario}_{variable}-Pct{percentile}_Sfc_LatLon0.86_{timestep}.nc`

with :

* __period__: Period associated with each data set, in {year of period start}-{year of period end} format: [1900-2014; 2015-2100; etc.].
 * __ECCC__ : Constant character string for Environment and Climate Change Canada, the data source
* __CanDCSU6__ : Constant string indicating statistically scaled climate scenario data from CMIP6 global climate models
* __variable__: Name of the climate variable available in the file, taking one of the following values: [AirTemp, AirTempMin, AirTempMax, Precip]. For anomalies: [AirTempAnomaly, AirTempMinAnomaly, AirTempMaxAnomaly, PrecipAnomaly]
* __scenario__ : Scenarios emissions, taking one of the values: [SSP126, SSP245, SSP585]
* __percentile__: Ensemble percentile, taking one of the values: [Pct5, Pct25, Pct50, Pct75, Pct95]; Pct5 represents the 5th ensemble percentile; Pct25 represents the 25th ensemble percentile, etc.
* __Sfc__ : Constant character string indicating that data are available on the surface
* __LatLon__ : Constant string indicating lat-lon grid projection 
* __0.86__ : Horizontal grid resolution of 0.86 degrees 
* __timeStep__: Time step, taking one of the following values: [P1Y, P1M]; P1Y represents a time step of one year, P1M represents a time step of one month; [P1Y-{DJF, MAM, JJA, SON}] represents the seasonal period (ex: DJF: December-January-February) ; [P0Y-{DJF, MAM, JJA, SON}] represents the 30-year average, P0Y indicates a single time period in the file
* __nc__: Constant string indicating NetCDF format

Examples:

* 1950-2014_ECCC_CanDCSU6_AirTemp-Pct50_Sfc_LatLon0.86_P1M.nc
* 1971-2000_ECCC_CanDCSU6_Precip-Pct25_Sfc_LatLon0.86_P1Y-SON.nc
* 2041-2070_ECCC_CanDCSU6-SSP126_PrecipAnomaly-Pct50_Sfc_LatLon0.86_P1Y-JJA.nc

## List of variables

The variables and units available for CanDCS-U6 datasets on the MSC Datamart are :

* Average temperature (°C)
* Projected change in mean temperature (°C)
* Minimum temperature (°C)
* Projected change in minimum temperature (°C)
* Maximum temperature (°C)
* Projected change in maximum temperature (°C)
* Total precipitation (mm)
* Projected relative change in total precipitation (mm)

## Support

If you have any questions about these data, please [contact us](mailto:info.cccs-ccsc@canada.ca).

## dd_info mailing list announcements 

Announcements related to this dataset are available via the [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/) list.



