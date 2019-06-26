[En Français](readme_hydrometric-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC Open Public Data](../readme_en.md) > Hydrometric data

# Hydrometric data in CSV format

This page describes the [real time hydrometric](readme_hydrometric_en.md) data available in CSV format.

# Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](.../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](.../../usage-overview/readme_en.md) is also available.

The data is available using the HTTP protocol and resides in a directory that is plainly accessible to a web browser. Visiting that directory with an interactive browser will yield a raw listing of links, each link being a downloadable GRIB2 file. In practice, we recommend writing your own script to automate the downloading of the desired data (using wget or equivalent). If you are unsure of how to proceed, you might like to take a look at our brief wget usage guide.

The data is available at the following address:
* https://dd.weather.gc.ca/hydrometric/csv/[PROVTERR]/[FREQUENCY]/

where :
* __PROVTERR__ : 2-letter code for the province or territory. The code is one of 
            the 13 following values:
    * AB (Alberta)
    * BC (British Columbia)
    * MB (Manitoba)
    * NB (New Brunswick)
    * NL (Newfoundland and Labrador)
    * NS (Nova Scotia)
    * NT (Northwest Territories)
    * NU (Nunavut)
    * ON (Ontario)
    * PE (Prince Edward Island)
    * QC (Quebec)
    * SK (Saskatchewan)
    * YT (Yukon)

* __FREQUENCY__ :  frequency of update, "hourly" or "daily"

## File name nomenclature 

NOTE: ALL HOURS ARE IN UTC.

The files have the following nomenclature:

CMC-reps-srpe-EnsembleDataType_Variable_LevelType_Level_Resolution_YYYYMMDDHH_Phhh_FileContent.grib2

where :

* __EnsembleDataType__ : Can be raw for individual members direct model output or prob for probabilistic products created from all members.
* __Variable__ : Variable name (ex: WIND) 
* __LevelType__ : Level type (ex: TGL for above ground level)
* __Level__ : Level value (ex: 10m for 10 meters)
* __Resolution__ : Grid resolution (ex: ps15km)
* __YYYYMMDDHH__ : Date of the model run in UTC
* __Phhh__ : Forecast hour
* __FileContent__ : can be all-products or allmbrs, indicating that all the members or all the probabilistic products for this variable are contain in the file 

## Support

If you have any questions about these data, please contact us at: ec.dps-client.ec@canada.ca

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).
