[En français](readme_cansips-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [CanSIPS](readme_cansips_en.md) > CanSIPS data in GRIB2 on MSC Datamart

# Canadian Seasonal to Inter-annual Prediction System (CanSIPS) Data in GRIB2 Format

The [Canadian Seasonal to Inter-annual Prediction System (CanSIPS)](readme_cansips_en.md) is a long-term prediction system whose objective is to forecast the evolution of global climate conditions. CanSIPS is a multi-model ensemble (MME) system using two atmosphere-ocean-land coupled models (CanESM5 and GEM5.2-NEMO) developed by the Canadian Centre for Climate Modelling and Analysis (CCCma), Meteorological Research Division (MRD) and the Canadian Centre for Meteorological and Environmental Prediction (CCMEP). It is a fully coupled atmosphere-ocean-ice-land prediction system relying on the operational data assimilation infrastructure for the initial state of the atmosphere, sea surface temperature and sea ice. For further technical information about CanSIPS please refer to the technical note.

## Principal components of CanSIPS
    
* __Initialization procedure__:

     * CanESM5: Initial atmospheric and oceanic conditions are obtained by running a coupled atmosphere-ocean-sec ice assimilation process constrained by CMC (GDPS) atmospheric analysis and GIOPS oceanic analysis through the same nudging procedure. Modelled sea ice thickness in the Northern Hemisphere is constrained near values from the SMv3 statistical model. Modelled sea ice concentration and sea surface temperature are constrained near values from GDPS G6. Land variables are initialized through the response of CLASS/CTEM to the assimilating atmosphere component.
     * GEM5.2-NEMO: The atmospheric initial conditions of GEM5.2-NEMO come from those of the Global Ensemble Prediction System (GEPS).The ocean and sea ice initial conditions in the forecast come from the CMC GIOPS analysis whereas land surface initial conditions is from CMC (GDPS) analysis after adjusting it to the hindcast climatology.
     
* __Forecast mode__: CanSIPS official forecasts are based on a 20-member ensemble of forecasts produced with each of the two models for a total ensemble size of 40. The 20 members, 12 month forecasts from each model are produced by combining the forecasts produced on the last day of each month (ensemble members 1-10)  with forecasts issued four-days prior to that (ensemble members 11-20).

* __Hindcast mode__: CanSIPS climatology is based on a series of retrograde forecasts (e. g. historical forecasts) covering the period 1990 to 2020. This climatology is very useful for interpreting realistic forecasts because real-time forecast anomalies are generated instead of raw forecasts.

* __Verification mode__ : To assess the performance of past CanSIPS forecasts, 3-month deterministic forecasts of normalized temperature and precipitation anomalies (in tercile categories: above, below, and near normal) are evaluated globally by comparing them to observed anomalies (tercile categories) based on the ECMWF ERA5 data for the same climatological period.

## How is the CanSIPS forecast configured ?


In CanSIPSv3, the ensemble size of the forecast has been increased from 20 members to 40 members (20 GEM-NEMO members + 20 CanESM5 members). This is achieved by combining the forecasts initialized on the last day of the month with the forecasts initialized four days prior to that.  For each model, a 12-month forecast is produced with the first 10 members of each model obtained from the last day of the month and the second set of 10 members from the forecasts initialized four days prior to that.  When the ensemble forecasts are completed, we construct seasonal mean anomalies with respect to the 30-year hindcasts for each ensemble member. Subsequently we implement deterministic (ensemble mean) and probabilistic (different categories with respect to the ensemble size) approaches to forecast the upcoming seasons. 

## Data location 

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available using the HTTPS protocol and resides in a directory that is plainly accessible to a web browser. Visiting that directory with an interactive browser will yield a raw listing of links, each link being a downloadable GRIB2 file.

The data can be accessed at the following URLs :

* [https://dd.weather.gc.ca/ensemble/cansips/grib2/forecast/raw/{YYYY}/{MM}/](https://dd.weather.gc.ca/ensemble/cansips/grib2/forecast/raw) (forecast members and products at 2.5 degrees)
* [https://dd.weather.gc.ca/model_cansips/100km/forecast/{YYYY}/{MM}/](https://dd.weather.gc.ca/model_cansips/100km/forecast) (forecast members and products at 1 degree)
* [https://dd.weather.gc.ca/model_cansips/100km/hindcast/{YYYY}/{MM}/](https://dd.weather.gc.ca/model_cansips/100km/hindcast) (hindcast)
* [https://dd.weather.gc.ca/model_cansips/100km/verification/{YYYY}](https://dd.weather.gc.ca/model_cansips/100km/verification) (vérification products at 1 degree)

where :

* __forecast__ : Constant string indicating that the file contains the data from the forecast part of CanSIPS, in opposition to the hindcast part.
* __hindcast__ : Constant string indicating that the file contains the data from the hindcast part of CanSIPS, in opposition to the forecast part.
* __verification__ : Constant string indicating that the file contains verification data against observations or reanalyses
* __100km__ : Indicate a 1 degree resolution (around 100km)
* __MM__ : Month of the forecast start [01, 02, 03, ..., 12]
* __YYYY__ : Year of the forecast start [Ex: 2012, 2013, ...]


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

     * Individual members: `cansips_forecast_raw_latlon2.5x2.5_{VAR}_{LVLTYPE}_{LVL}_{YYYY}-{MM}_allmembers.grib2`
     * Probability products: `cansips_forecast_prob-{StatProcess}_latlon2.5x2.5_{VAR}_{LVLTYPE}_{LVL}_{YYYY}-{MM}_{PPP}.grib2`

* Members and products at 1 degree:

     * Individual members: `{YYYYMM}_MSC_CanSIPS_{Var}_{Level}_LatLon1.0_P{Month}M.grib2` 
     * Probability products: `{YYYYMM}_MSC_CanSIPS_{Var}-{StatProcess}_{Level}_LatLon1.0_{Month}.grib2`

* Hindcast:

    * `{YYYYMM}_MSC_CanSIPS-Hindcast_{Var}_{Level}_LatLon1.0_P{Month}M.grib2`

* Verification products:

    * `{YYYYMM}_MSC_CanSIPS_{Var-Anomaly}-ERA5_{Level}_LatLon1.0_P{Month}M-P{Month}M.grib2`

where :

* __cansips|CanSIPS__ : Constant string indicating that the data is from the CanSIPS system
* __MSC__ : Constant string indicating that the data is from the Meteorologcal Service of Canada (MSC)
* __forecast__ : Constant string indicating that the file contains the data from the forecast part of CanSIPS, in opposition to the hindcast part
* __CanSIPS-Hindcast__ : Constant string indicating that the file contains the data from the hindcast part of CanSIPS, in opposition to the forecast part
* __raw__ : Constant string indicating that the file contains raw data without bias correction
* __VAR__ : Variables included in the 2 degrees files [TMP, HGT, PRATE, SSHG, PRMSL, UGRD, VGRD]
* __Var__ : Variables included in the 1 degree files [AirTemp, GeopotentialHeight, PrecipRate, SeaSfcHeight-Geoid, Pressure, WindU, WindV]
* __Var-Anomaly__ : Anomaly variables included in the 1 degree files [AirTempAnomaly, PrecipAccumAnomaly]
* __StatProcess__ : Statistic process [prob-near-normal, prob-below-normal, prob-above-normal, ProbNearNormal, ProbBelowNormal, ProbAboveNormal]
* __ERA5__ : Constant string indicating that verification products are generated based on ECMWF ERA5 reanalysis
* __LVLTYPE__ : Vertical level type [SFC for the surface, TGL for height above the ground, ISBL for pressure level, MSL for mean sea level]
* __LVL__ : Vertical level value
* __Level__ : Vertical level [Sfc for the surface, AGL-2m for 2m above ground level]
* __MM__ : Month of the forecast start [01, 02, 03, ..., 12]
* __YYYY__ : Year of the forecast start
* __allmembers__ : Constant string indicating that all members [01, 02, 03, ..., 20] are grouped into the file
* __PPP__ : Forecast product time length ex: P3M is for a product with forecast a period of 3 months
* __Month__ : Months concerned from the beginning of the forecast, either 1 month [ex: P07M for December if the beginning of the forecast is May] or several months starting from the beginning of the forecast [ex: P01M-P03M for June to August if the beginning of the forecast is May]
* __P{Month}M-P{Month}M__ : Three months period covered for the verification
* __grib2__ : Constant string indicating the GRIB2 format is used

Examples : 

* cansips_forecast_raw_latlon2.5x2.5_HGT_ISBL_0500_2012-10_allmembers.grib2
* cansips_forecast_prob-below-normal_latlon2.5x2.5_TMP_TGL_2m_P3M_2018-12.grib2
* 202309_MSC_CanSIPS_AirTemp_AGL-2m_LatLon1.0_P00M.grib2
* 202305_MSC_CanSIPS_AirTemp-ProbBelowNormal_AGL-2m_LatLon1.0_P06M-P09M.grib2
* 202010_MSC_CanSIPS-Hindcast_WaterTemp_Sfc_LatLon1.0_P10M.grib2
* 202503_MSC_CanSIPS_AirTempAnomaly-ERA5_AGL-2m_LatLon1.0_P12M-P02M.grib2
* 202504_MSC_CanSIPS_PrecipAccumAnomaly-ERA5_Sfc_LatLon1.0_P01M-P03M.grib2

## Internal Structure of the Files

The internal structure of the forecast and hindcast files is the following : 

Each file contains 40 records (corresponding to the 40 ensemble members) and the first 20 ensemble members belong to GEM5.2-NEMO whereas the last 20 ensemble members are from CanESM5. Please, find below the detailed classification of ensemble members with respect to model and start date.

* ensemble 1-10 : from GEM5.2-NEMO with forecasts initialized on the last day of the month
* ensemble 11-20: from GEM5.2-NEMO with forecasts initialized four days prior to the last day of the month
* ensemble 21-30: from CanESM5 with forecasts initialized on the last day of the month
* ensemble 31-40: from CanESM5 with forecasts initialized four days prior to the last day of the month

## List of variables

__Individual members:__

<table id="csv-table" class="display"></table>

<link href="https://cdn.jsdelivr.net/npm/simple-datatables@latest/dist/style.css" rel="stylesheet" type="text/css">
<script src="https://cdn.jsdelivr.net/npm/simple-datatables@latest"></script>
<script src="../../../js/variables_datatable.js" type="text/javascript"></script>
<script>
  loadTable("csv-table", "../../../assets/csv/CanSIPS_Variables-List_en.csv");
</script>

__Ensemble products:__

<table id="csv-prob-table" class="display"></table>

<script>
  loadTable("csv-prob-table", "../../../assets/csv/CanSIPS-Products_Variables-List_en.csv");
</script>

__Tercile probability products:__

The files contain tercile probability values for above, near or below normal categories.  The variables considered are precipitation and temperature. For each of the two variables, there are three files to represent the three tercile probabilities and are described below.

* APCP

    * Probability above the 66.7 percentile threshold (unitless)- often known as Probability of precip being above normal
    * Minimum (0 percent), maximum (100 percent)
    * Probability below the 33.3 percentile threshold (unitless)- often known as Probability of precip being below normal
    * Minimum (0 percent), maximum (100 percent)
    * Probability between 33.3 and 66.7 percentiles (unitless)  – often known as Probability of precipitation being near normal/climatology
    * Minimum (0 percent), maximum (100 percent)

* TMP

    * Probability above the 66.7 percentile threshold (unitless)- often known as Probability of temperature being above normal
    * Minimum (0 percent), maximum (100 percent)
    * Probability below the 33.3 percentile threshold (unitless)- often known as Probability of temperature being below normal
    * Minimum (0 percent), maximum (100 percent)
    * Probability between 33.3 and 66.7 percentiles (unitless)  – often known as Probability of temperature being near normal/climatology
    * Minimum (0 percent), maximum (100 percent)

__Exceedance probability products:__

These files contain exceedance probabilities and are available based on nine thresholds, namely:

1. Probability of temperature/precipitation of being above 10 percentile
2. Probability of temperature/Precipitation of being above 20 percentile
3. Probability of temperature/Precipitation of being above 30 percentile

……

8. Probability of temperature/Precipitation of being above 80 percentile
9. Probability of temperature/Precipitation of being above 90 percentile

## Tips for Computing Anomaly Forecasts

It is recommended to use anomaly forecasts instead of the raw forecasts. Anomaly forecasts can be obtained by subtracting from the forecast a climatology based on the hindcasts. The recipe is as follows for a given variable:

For a specific forecast month (e.g. 2016-02) an ensemble mean file needs to be created and we can call it ensm_for_02_2016 for the purpose of this example. This file now contains only 12 temporal records since the mean of 40 ensemble members is performed. The temporal record of this file starts in the month 02 of the year 2016 and stretches until the month 01 of the year 2017.

Subsequently, the same procedure is repeted for the hindcast files but separately for each of the hindcasts that start in 1981 and stretch until the year of 2010. Each year will have an ensemble mean file for the month 02, ensm_hin_02_YYYY, but for the particular hindcast year (YYYY stands for a particular hindcast year). By making the mean of all of the 30 ensm_hin_02_YYYY files, the climatology of the ensemble mean hindcast for the month of February is obtained, which can be called ensm_hinclim_02 in this example.

The subtraction of ensm_hinclim_02 and ensm_for_02_2016 allows for anomaly forecast production for the month 02 of the year 2016. Since this anomaly forecast now contains 12 temporal records, starting from the month of February 2016, we can say that the anomaly forecast for the month of February has zero lead time, for the month of March 2016 a one month lead time and finally for the month of January 2017 (last of the 12 record) an eleven month lead time.

Similar approach applies for the seasonal forecasts only with the seasonal means (e.g. DJF, JFM, FMA, or any other running season) being calculated before the anomaly forecast is computed.

## Support

If you have any questions about this data, please [contact us](https://weather.gc.ca/mainmenu/contact_us_e.html).

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).
