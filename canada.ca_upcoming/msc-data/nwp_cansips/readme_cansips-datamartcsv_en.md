[En Français](readme_cansips-datamartcsv_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC Open Public Data](../readme_en.md) > CanSIPS

# Canadian Seasonal to Inter-annual Prediction System (CanSIPS) Data in CSV Format

The [Canadian Seasonal to Inter-annual Prediction System (CanSIPS)](readme_cansips_en.md) is a long-term prediction system whose objective is to forecast the evolution of global climate conditions. CanSIPS is a multi-model ensemble (MME) system using two climate models developed by the Canadian Centre for Climate Modelling and Analysis (CCCma). It is a fully coupled atmosphere-ocean-ice-land prediction system relying on the operationnal data assimilation infrastructure for the initial state of the atmosphere, sea surface temperature and sea ice. For further technical information about CanSIPS please refer to the technical note.
Principal components of CanSIPS

## Principal components of CanSIPS
    
* __Assimilation mode__: CanSIPS uses a continuous assimilation cycle for the following 3D atmospheric variables: temperature, wind and humidity. The oceanic variables: sea surface temperature and the sea ice are also assimilated by the system. The assimilated data are provided by the global atmospheric analysis available every 6 hours and the daily sea surface temperature and sea ice analysis. Also a 3D ocean temperature analysis is integrated to CanSIPS trial field before launching the integration.
* __Forecast mode__: The CanSIPS forecasts are based on a 10-member ensemble of forecasts produced with each of two CCCma climate models for a total ensemble size of 20. Monthly to multi-seasonal forecasts extending to 12 months are issued on the first day of each month.
* __Hindcast mode__: CanSIPS climatology is based on series of historical forecasts covering the period 1981-2010. This climatology of the system is very useful for the interpretation of the forecast since the anomaly is generally used instead of the actual raw forecast.

## Data address 

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](.../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](.../../how-to/readme_en.md) is also available.

CanSIPS calculates a suite of oceanic and atmospheric indices (e.g. monsoon indices, PNA, NAO, El NINO, etc.) which can be used for seasonal climate forecasting and monitoring. 

A more detailed description of the indices is available [HERE](indices_CANSIPS_e.pdf).

The files containing atmospheric and oceanic CanSIPS indices can be accessed at the following URLs:

__Forecast files__ :

* https://dd.weather.gc.ca/ensemble/cansips/csv/indices/forecast/seasonal
* https://dd.weather.gc.ca/ensemble/cansips/csv/indices/forecast/monthly

__Hindcast files__ :

* https://dd.weather.gc.ca/ensemble/cansips/csv/indices/hindcast/seasonal
* https://dd.weather.gc.ca/ensemble/cansips/csv/indices/hindcast/monthly

__Observations__ :

* https://dd.weather.gc.ca/ensemble/cansips/csv/indices/observation/seasonal
* https://dd.weather.gc.ca/ensemble/cansips/csv/indices/observation/monthly

## File name nomenclature 

NOTE: ALL HOURS ARE IN UTC.

The forecast and hindcast files have the following nomenclature:

* YYYYMMDD00_indices_month_YYYY1MM1-YYYY2MM2.csv
* YYYYMMDD00_indices_season_YYYY1MM1-YYYY2MM2.csv

where:
* __YYYY__ : Year of the forecast initiation
* __MMDD__ : Month and day of the forecast initiation
* __YYYY1MM1__ : Year and month of the forecast start
* __YYYY2MM2__ : Year and month of the forecast end 

The observation files have the following nomenclature:

* observed_indices_month_YYYY1MM1-YYYY2MM2.csv

where:
* __YYYY1MM1__ : Year and month the index calculation starts
* __YYYY2MM2__ : Year and month the index calculation ends

Observational indices based on the sea surface temperature anomalies are calculated with respect to the optimal interpolation SST dataset (OISST, Reynolds et al. 2002) while the remaining indices are calculated using ERA-interim reanalysis (Dee et al. 2011).

## Support

If you have any questions about these data, please contact us at: ec.dps-client.ec@canada.ca

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).
