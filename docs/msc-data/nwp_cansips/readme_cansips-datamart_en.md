[En français](readme_cansips-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [CanSIPS](readme_cansips_en.md) > CanSIPS data in GRIB2 on MSC Datamart

# Canadian Seasonal to Inter-annual Prediction System (CanSIPS) Data in GRIB2 Format

The Canadian Seasonal to Inter-annual Prediction System (CanSIPS) is a long-term prediction system whose objective is to forecast the evolution of global climate conditions. CanSIPS is a multi-model ensemble (MME) system using two atmosphere-ocean-land coupled models developed by the Canadian Centre for Climate Modelling and Analysis (CCCma) and the Canadian Meteorological Centre (CMC). It is a fully coupled atmosphere-ocean-ice-land prediction system relying on the operational data assimilation infrastructure for the initial state of the atmosphere, sea surface temperature and sea ice. For further technical information about CanSIPS please refer to the technical note.

## Principal components of CanSIPS
    
* __Assimilation mode__: CanCM4 uses a continuous assimilation cycle for the following 3D atmospheric variables: temperature, wind and humidity. The oceanic variables: sea surface temperature and the sea ice are also assimilated by the system. The assimilated data are provided by the global atmospheric analysis available every 6 hours and the daily sea surface temperature and sea ice analysis. Also a 3D ocean temperature analysis is integrated to CanCM4 trial field before launching the integration. GEM-NEMO uses atmospheric initial condition of the Global Ensemble Prediction System (GEPS) which are generated from the Ensemble Kalman Filter (EnKF) with observations that are background-checked and bias-corrected by the Global Deterministic Prediction System (GDPS). The ocean and sea ice initial conditions come from the CMC GIOPS analysis. To initialize the land surface fields, the CMC Surface Prediction System (SPS) is run offline forced by the near-surface atmospheric and precipitation fields of the CMC analysis.
* __Forecast mode__: The CanSIPS forecasts are based on a 10-member ensemble of forecasts produced with each of the two models for a total ensemble size of 20. Monthly to multi-seasonal forecasts extending to 12 months are issued on the first day of each month.
* __Hindcast mode__: CanSIPS climatology is based on a series of retrograde forecasts (e. g. historical forecasts) covering the period 1980 to 2020. This climatology is very useful for interpreting realistic forecasts because real-time forecast anomalies are generated instead of raw forecasts.

## How is the CanSIPS forecast configured ?

Ensemble size for the forecast is 20 members (10 GEM-NEMO members + 10 CanCM4 members). At the last day of the each month, a 12-month forecast is produced. There are no lagged initial conditions, all the 20 members start on the first of the month and are initialised with different initial conditions originating from separate assimilating coupled model runs. When the ensemble forecasts are finished we construct seasonal mean anomalies with respect to the 30-year hindcasts for each ensemble member. Subsequently we implement deterministic (ensemble mean) and probabilistic (different categories with respect to the ensemble size) approaches to forecast the upcoming seasons. 

## Data location 

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available using the HTTPS protocol and resides in a directory that is plainly accessible to a web browser. Visiting that directory with an interactive browser will yield a raw listing of links, each link being a downloadable GRIB2 file.

The data can be accessed at the following URLs :

* [https://dd.weather.gc.ca/ensemble/cansips/grib2/forecast/raw/{YYYY}/{MM}/](https://dd.weather.gc.ca/ensemble/cansips/grib2/forecast/raw) (forecast members and products at 2.5 degrees, members at 1 degree)
* [https://dd.weather.gc.ca/model_cansips/100km/forecast/{YYYY}/{MM}/](https://dd.weather.gc.ca/model_cansips/100km/forecast) (forecast products at 1 degree)
* [https://dd.weather.gc.ca/ensemble/cansips/grib2/hindcast/raw/{YYYY}/{MM}/](https://dd.weather.gc.ca/ensemble/cansips/grib2/hindcast/raw) (hindcast)

where :

* __forecast__ : Constant string indicating that the file contains the data from the forecast part of CanSIPS, in opposition to the hindcast part.
* __hindcast__ : Constant string indicating that the file contains the data from the hindcast part of CanSIPS, in opposition to the forecast part.
* __100km__ : Indicate a 1 degree resolution (around 100km)
* __MM__ : Month of the forecast start [01, 02, 03, ..., 12]
* __YYYY__ : Year of the forecast start [2012, 2013, ...]

A 1-month history is kept in these directories (except for hindcast).

## Technical specification of the grid

Tables list the values of various parameters of the CanSIPS lat-lon grid, according to the resolution.

### Data at 2.5x2.5 degrees resolution

| Parameter | Value |
| ------ | ------ |
| ni | 145 |
| nj | 73 | 
| resolution | 2.5° |
| coordinates of the first grid point | 90° S  0° E | 

### Data at 1.0x1.0 degree resolution

| Parameter | Value |
| ------ | ------ |
| ni | 360 |
| nj | 180 | 
| resolution | 1.0° |
| coordinates of the first grid point | 89.5° S  0.5° E | 

## File name nomenclature 

The files have the following nomenclature:

* Members and products at 2.5 degrees:

    * Forecasts : `cansips_forecast_raw_latlon2.5x2.5_{VAR}_{LVLTYPE}_{LVL}_{YYYY}-{MM}_allmembers.grib2`
    * Probability products: `cansips_forecast_prob-{StatProcess}_latlon2.5x2.5_{VAR}_{LVLTYPE}_{LVL}_{YYYY}-{MM}_{PPP}.grib2`

* Members and products at 1 degree:

    * Forecasts : `cansips_forecast_raw_latlon1.0x1.0_{VAR}_{LVLTYPE}_{LVL}_{YYYY}-{MM}_allmembers.grib2`
    * Probability products: `{YYYYMM}_MSC_CanSIPS_{Var}-{StatProcess}_{Level}_LatLon1.0_{Month}.grib2`

* Hindcast:

    * `cansips_hindcast_raw_latlon1.0x1.0_{VAR}_{YYYY}-{MM}_allmembers.grib2`

where :

* __cansips|CanSIPS__ : Constant string indicating that the data is from the CanSIPS system
* __MSC__ : Constant string indicating that the data is from the Meteorologcal Service of Canada (MSC)
* __forecast__ : Constant string indicating that the file contains the data from the forecast part of CanSIPS, in opposition to the hindcast part
* __hindcast__ : Constant string indicating that the file contains the data from the hindcast part of CanSIPS, in opposition to the forecast part
* __raw__ : Constant string indicating that the file contains raw data without bias correction
* __VAR__ : Variables included in the files. To consult a complete list, refer to the variables section
* __Var__ : Variables included in the files [PrecipRate, AirTemp]
* __StatProcess__ : Statistic process [prob-near-normal, prob-below-normal, prob-above-normal, ProbNearNormal, ProbBelowNormal, ProbAboveNormal]
* __LVLTYPE__ : Vertical level type [SFC for the surface, TGL for height above the ground, ISBL for pressure level, MSL for mean sea level]
* __LVL__ : Vertical level value
* __Level__ : Vertical level [Sfc for the surface, AGL-2m for 2m above ground level]
* __MM__ : Month of the forecast start [01, 02, 03, ..., 12]
* __YYYY__ : Year of the forecast start [2012, 2013, ...]
* __allmembers__ : Constant string indicating that all members [01, 02, 03, ..., 20] are grouped into the file
* __PPP__ : Forecast product time length ex: P3M is for a product with forecast a period of 3 months
* __Month__ : Months concerned from the beginning of the forecast, either 1 month [ex: P07M for December if the beginning of the forecast is May] or several months starting from the beginning of the forecast [ex: P01M-P03M for June to August if the beginning of the forecast is May]
* __grib2__ : Constant string indicating the GRIB2 format is used

Examples : 

* cansips_forecast_raw_latlon2.5x2.5_HGT_ISBL_0500_2012-10_allmembers.grib2
* cansips_forecast_raw_latlon1.0x1.0_PRATE_SFC_0_2019-08_allmembers.grib2
* cansips_forecast_prob-below-normal_latlon2.5x2.5_TMP_TGL_2m_P3M_2018-12.grib2
* 202305_MSC_CanSIPS_AirTemp-ProbBelowNormal_AGL-2m_LatLon1.0_P06M-P09M.grib2
* cansips_hindcast_raw_latlon2.5x2.5_HGT_ISBL_0500_1990-11_allmembers.grib2

## Internal Structure of the Files

The internal structure of the forecast and hindcast files is the following : 

Each file contains 240 temporal records (12 months times 20 ensemble members) and starts with the first ensemble member. Ensemble members are placed in an incremental order within the CanSIPS files.

Each forecast or the hindcast file starts with a lead time of zero months. This means that if for example a CanSIPS file has a 2016-02 date-tag (e.g. cansips_forecast_raw_latlon-1x1_PRATE_SFC_0_2016-02_allmembers.grib2),data will start from the month 02 of the year of 2016 and will be finished (for the first member) in the month 01 of the year of 2017. This means that the forecast was initialised on the last day of the January 2016 and that the results are starting to appear in the month of February 2016 (zero lead time).

Following the temporal record of the month 01 of the year 2017, a second CanSIPS ensemble member appears from the month 02 of the year 2016 following the same logic as described earlier.

## List of variables

__Individual members:__

<table id="csv-table" class="display"></table>

<link href="https://cdn.jsdelivr.net/npm/simple-datatables@latest/dist/style.css" rel="stylesheet" type="text/css">
<script src="https://cdn.jsdelivr.net/npm/simple-datatables@latest"></script>
<script src="../../../js/variables_datatable.js" type="text/javascript"></script>
<script>
  loadTable("csv-table", "../../../assets/csv/CanSIPS_en.csv");
</script>

__Ensemble products:__

<table id="csv-prob-table" class="display"></table>

<script>
  loadTable("csv-prob-table", "../../../assets/csv/CanSIPS_prob_en.csv");
</script>

The files contain probability products by member counting above or below different thresholds, percentiles, means, medians and standard deviations. Note that products and thresholds are defined in the file metadata. The following products are available for each of the variables listed below.

###### APCP

* Probability above 0 kg/(m<sup>2</sup>*s)
* Minimum (0 percentile), maximum (100th percentile), standard deviation and mean

###### TMP

* Probability above 0 K
* Minimum (0 percentile), maximum (100th percentile), standard deviation and mean

## Tips for Computing Anomaly Forecasts

It is recommended to use anomaly forecasts instead of the raw forecasts. Anomaly forecasts can be obtained by subtracting from the forecast a climatology based on the hindcasts. The recipe is as follows for a given variable:

For a specific forecast month (e.g. 2016-02) an ensemble mean file needs to be created and we can call it ensm_for_02_2016 for the purpose of this example. This file now contains only 12 temporal records since the mean of 20 ensemble members is performed. The temporal record of this file starts in the month 02 of the year 2016 and stretches until the month 01 of the year 2017.

Subsequently, the same procedure is repeted for the hindcast files but separately for each of the hindcasts that start in 1981 and stretch until the year of 2010. Each year will have an ensemble mean file for the month 02, ensm_hin_02_YYYY, but for the particular hindcast year (YYYY stands for a particular hindcast year). By making the mean of all of the 30 ensm_hin_02_YYYY files, the climatology of the ensemble mean hindcast for the month of February is obtained, which can be called ensm_hinclim_02 in this example.

The subtraction of ensm_hinclim_02 and ensm_for_02_2016 allows for anomaly forecast production for the month 02 of the year 2016. Since this anomaly forecast now contains 12 temporal records, starting from the month of February 2016, we can say that the anomaly forecast for the month of February has zero lead time, for the month of March 2016 a one month lead time and finally for the month of January 2017 (last of the 12 record) an eleven month lead time.

Similar approach applies for the seasonal forecasts only with the seasonal means (e.g. DJF, JFM, FMA, or any other running season) being calculated before the anomaly forecast is computed.

## Support

If you have any questions about this data, please contact us at: [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).
