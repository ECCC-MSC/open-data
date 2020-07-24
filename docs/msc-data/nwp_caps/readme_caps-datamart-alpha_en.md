[En français](readme_caps-datamart-alpha_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [CAPS](readme_caps_en.md) > CAPS data in GRIB2 on DD-Alpha

# Experimental Canadian Arctic Prediction System (CAPS) Data in GRIB2 Format

This page describes the data of the [Canadian Arctic Prediction System (CAPS)](readme_caps_en.md) available on the MSC testing data repository DD-Alpha.

## Data location 

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available using the HTTP protocol and resides in a directory that is plainly accessible to a web browser. Visiting that directory with an interactive browser will yield a raw listing of links, each link being a downloadable GRIB2 file.

The data can be accessed at the following URLs :

* [https://dd.alpha.weather.gc.ca/yopp/model_caps/grib2/polar_stereographic/{YYYY}}/{MM}/{DD}/{HH}/{Phhh}](https://dd.alpha.weather.gc.ca/yopp/model_caps/grib2/polar_stereographic/)

where :

* __Phhh__ : P is a constant character. hhh is the forecast hour [000, 001, 002, ..., 048]
* __HH__ : Start hour of model run in UTC [00, 12] 
* __DD__ : Day of the forecast start [01, 02, 03, ..., 31]
* __MM__ : Month of the forecast start [01, 02, 03, ..., 12]
* __YYYY__ : Year of the forecast start [2012, 2013, ...]

A 2-years history is kept in this directory.

## File name nomenclature 

NOTE : ALL HOURS ARE IN UTC.

The files have the following nomenclature:

* CMC_caps_Variable_LevelType_Level_ProjectionResolution_YYYYMMDDHH_Phhh.grib2

where :

* __CMC__: Constant string indicating the data source (Canadian Meteorological Centre)
* __caps__: Constant string indicating the forecasting system that generated the data (CAPS)
* __Variable__: Name of forecast variable available in the file 
* __LevelType__: Level type taking one of the values: [sfc, depth]
* __Level__: Level value
* __Projection__: Grid mapping (projection), taking one value: ps for polar stereographic
* __Resolution__: Resolution, taking one value: 3km
* __YYYYMMDD__: Year, month and day of the beginning of the forecast
* __HH__: Start hour of model run in UTC [00, 12] 
* __Phhh__: P is a constant character. hhh is the forecast hour [000, 001, 002, ..., 048]
* __grib2__: Constant string indicating the GRIB2 format


Examples : 

* CMC_caps_HGT_ISBL_0500_ps3km_2018011200_P024.grib2

The files originates from the Canadian Meteorological Center (CMC) and contains the data of the Canadian Arctic Prediction System. The data in the file start on January 12th 2018 at 00Z (2018011200). It contains the geopotential height (HGT) au niveau isobarique 500 mb (ISBL_0500) on a polar stereographic grid at 3km resolution (ps3km) for the forecast hour 24 (P024) in GRIB2 format (.grib2).

## Levels

The data are available at surface and for certain isobaric levels.

## List of variables

Currently, the variables are the same as the one produced by the HRDPS.

Hence, for the CAPS variables at 000h forecast, please consult the list here:
* https://weather.gc.ca/grib/HRDPS_HR/HRDPS_nat_ps2p5km_P000_deterministic_e.html

Regarding the CAPS variables at non-zero hour forecasts, see:
* https://weather.gc.ca/grib/HRDPS_HR/HRDPS_ps2p5km_PNONZERO_deterministic_e.html

The vertical coverage of three-dimensional fields is provided by up to 28 isobaric levels (hPa):
1015, 1000, 0985, 0970, 0950, 0925, 0900, 0850, 0800, 0750, 0700, 0650, 0600, 0550, 0500, 0450, 0400, 0350, 0300, 0275, 0250, 0225, 0200, 0175, 0150, 0100, 0050.

Some fields receive limited three-dimensional coverage of 4 levels in the vertical (ex: absolute vorticity) :0850, 0700, 0500, 0250.

Additional levels which may be applicable to a given parameter:

* Surface 
* Fixed height above ground 
* Fixed height below ground
* Thickness between two isobaric levels
* Nominal top of the atmosphere
* Entire atmospheric column

## Support

If you have any questions about this data, please contact us at: [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).