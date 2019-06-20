[En Français](readme_aqhi-datamartcsv_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC Open Public Data](../readme_en.md) > AQHI

# Air Quality Health Index (AQHI) observation and forecast data in CSV format

The [Air Quality Health Index AQHI](readme_aqhi_en.md) is a scale designed to help quantify the quality of the air in a certain region on a scale from 1 to 10. When the amount of air pollution is very high, the number is reported as 10+. It also includes a category that describes the health risk associated with the index reading e.g. Low, Moderate, High, or Very High Health Risk . The AQHI is calculated based on the relative risks of a combination of common air pollutants that are known to harm human health, including ground-level ozone, particulate matter, and nitrogen dioxide. The AQHI formulation captures only the short term or acute health risk exposure of hour or days at a maximum .
The formulation of the AQHI may change over time to reflect new understanding associated with air pollution health effects. The AQHI is calculated from data observed in real time, without being verified quality control.

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](.../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](.../../usage-overview/readme_en.md) is also available.

The data is available via the HTTP protocol. It is possible to access it with a standard browser. In this case, we obtain a list of links giving access to a CSV file.

The data can be accessed at the following address:
* https://dd.weather.gc.ca/air_quality/aqhi/

where:

![Description de la structure des répertoires](https://dd.meteo.gc.ca/air_quality/doc/aqhi_structure.png)

## File name nomenclature 

NOTE: ALL HOURS ARE IN UTC.

__2. CSV Files :__

    2.1  Observations:
       Real-time CSV files:                     YYYYMMDDhh_AQHI_REGION_OBSTYPE.csv
       Location: https://dd.weather.gc.ca/air_quality/aqhi/[atl|ont|pnr|pyr|que]/observation/realtime/csv

       Monthly summary CSV files:               YYYYMM_MONTHLY_AQHI_REGION_OBSTYPE.csv
       Location: https://dd.weather.gc.ca/air_quality/aqhi/[atl|ont|pnr|pyr|que]/observation/monthly/csv

       Monthly summary CSV files with back-filled data: YYYYMM_MONTHLY_AQHI_REGION_OBSTYPE_BACKFILLED.csv
       Location: https://dd.weather.gc.ca/air_quality/aqhi/[atl|ont|pnr|pyr|que]/observation/monthly/csv

where :

* __YYYY__ : Year of the observation, 4 digits;
* __MM__ : Month of the observation, 2 digits (January = 01);
* __DD__ : Day of the observation, 2 digits;
* __hh__ : Hour of the observation, 2 digits;
* __'MONTHLY'__ : fixed string which is present when the file contains data for the entire month;
* __REGION__ : Name of Environment and Climate Change Canada region within which the observations are located. Options are:
    * 'ATL'=Atlantic;
    * 'ON'=Ontario,
    * 'PNR'=Prairie and Northern Region,
    * 'PYR'=Pacific and Yukon Region,
    * 'QC'=Quebec,
* __OBSTYPE__ : Type of observation contained in the file. Options are:
    * 'SiteObs'=file contains AQHI observations for communities,
    * 'StationObs'=file contains AQHI observations for individual monitoring stations associated to communities
    (not available as of January 2012).
* __'BACKFILLED'__ : fixed string which is present when the file contains the AQHI computed NOT from real-time data,
                but rather from the back-filled, corrected data received within 48 hours of the valid hour.

Note: The "real-time" CSV files are produced hourly, contain observations for the previous 7 days, and
are available on Datamart for a period of 8 days. The "MONTHLY" CSV files are produced at the end of
every month and are available on Datamart for a period of 12 months.

__2.2  Public forecasts :__

       Monthly summary CSV files:                YYYYMM_MONTHLY_AQHI_CGNDBcode_SiteFcst.csv
       Location: https://dd.weather.gc.ca/air_quality/aqhi/[atl|ont|pnr|pyr|que]/forecast/monthly/csv

where : 

* __YYYY__ : Year of the forecasts, 4 digits;
* __MM__ : Month of the forecasts, 2 digits (January = 01);
* __'MONTHLY'__ : fixed string to indicate that the file contains data for the entire month;
* __CGNDBcode__ : 5-letter CGNDB code which identifies each AQHI community. A list of CGNDB codes is given
at the end of this README file.
* __'SiteFcst'__ : fixed string to indicate that the file contains AQHI forecasts for a community.

__2.3  Model guidance :__

       CSV files:                               YYYYMMDDhh_SPECIES_REGION_MODELTYPE.csv
       Location: https://dd.weather.gc.ca/air_quality/aqhi/[atl|ont|pnr|pyr|que]/forecast/model/csv

where :

* __YYYY__ : Year the model guidance was generated, 4 digits;
* __MM__ : Month the model guidance was generated, 2 digits (January = 01);
* __DD__ : Day the model guidance was generated, 2 digits;
* __hh__ : Hour the model guidance was generated, 2 digits (00 or 12 UTC);
* __'SPECIES'__ : fixed string which indicates which chemical species the model guidance represents. Options are:
    * 'O3'=ozone,
    * 'NO2'=nitrogen dioxide,
    * 'PM2.5'=particulate matter of less than 2.5 um,
    * 'PM10'=particulate matter of less than 10 um,
    * 'AQHI'=Air Quaility Health Index,
* __REGION__ : Name of Environment and Climate Change Canada region within which the model guidance is valid. Options are:
    * 'ATL'=Atlantic;
    * 'ON'=Ontario,
    * 'PNR'=Prairie and Northern Region,
    * 'PYR'=Pacific and Yukon Region,
    * 'QC'=Quebec,
* __MODELTYPE__ : Indicates the system used to generate the model guidance. Options are:
    * 'AQFM'=operational Air Quality Forecast Model,
    * 'UMOSAQ'=Updateable Model Output Statistics post-processing approach applied to the AQFM raw model output;
    * 'UMOSAQMIST'=blended AQFM and UMOSAQ guidance; generated to provide additional guidance to meteorologists since
    UMOSAQ data may not be available directly at observation points.

## Support

If you have any questions about these data, please contact us at: ec.dps-client.ec@canada.ca

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).

