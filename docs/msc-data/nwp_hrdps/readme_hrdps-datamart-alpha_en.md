[En français](readme_hrdps-datamart-alpha_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [HRDPS](readme_hrdps_en.md) > Experimental HRDPS on DD-Alpha 

# Experimental High Resolution Deterministic Prediction System (HRDPS) 1km West data in GRIB2 format

In the summer of 2017 British Columbia was experiencing severe wildfire.  To provide more detailed weather information and pilot the air quality models, HRDPS 1km west domain was implemented in operations in **experimental mode** on 31 July 2018. 

This prediction system uses the Global Environmental Multi-scale Model (GEM). The horizontal grid spacing is approximately 1.0 km and there are 62 vertical levels with lid nesting. 

The lowest momentum level is at an altitude of approximately 40 m. This system is “piloted” by [HRDPS 2.5-km](readme_hrdps_en.md) national domain, which provides initial, lateral and upper boundary conditions for the atmospheric fields.  The initial surface conditions are provided by the 2.5-km Canadian Land Data Assimilation System (CaLDAS) which is coupled to the HRDPS 2.5-km. The initial hydrometeor fields are “recycled” from the 6-h forecast of the HRDPS 2.5-km integration. 

Since the original implementation of the HRDPS 1-km west, the system has been running 2 times per day initialized at 00, and 12 UTC and integrated for 36-h. This product contains raw numerical results of the system. The Geographical coverage of the system is the most part of British Columbia and Western Alberta. Data are available at a horizontal resolution of 1.0 km with 62 vertical levels.

## Data location

MSC testing data repository DD-Alpha data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available using the HTTP protocol and resides in a directory that is plainly accessible to a web browser. Visiting that directory with an interactive browser will yield a raw listing of links, each link being a downloadable GRIB2 file. In practice, we recommend writing your own script to automate the downloading of the desired data (using wget or equivalent). If you are unsure of how to proceed, you might like to take a look at our brief wget usage guide.

The data can be accessed at the following URL:

http://dd.alpha.meteo.gc.ca/model_hrdps/west/1km/grib2/HH/hhh/

where:

* __HH__: Model run start, in UTC [00, 12].
* __hhh__: Forecast hour [000, 001, 002, ..., 036]

A 24-hour history is stored in this directory.

## Available domain

![Image de la grille ouest du domaine 1km du SHRPD](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_hrdps/grille_hrdps1km_west.png)

Table lists the values of various parameters of the West polar-stereographic grid.

| Parameter | Value |
| ------ | ------ |
| ni | 1465 |
| nj | 825 | 
| resolution at 60° N | 1.0 km |
| coordinate of first grid point | ° N  ° W |
| (i,j) coordinate of North Pole | (,) |
| grid orientation (with respect to j axis) | ° |

## File name nomenclature 

NOTE: ALL HOURS ARE IN UTC.

The files have the following nomenclature:

CMC_hrdps_west_Variable_LevelType_level_ps1.0km_YYYYMMDDHH_Phhh-mm.grib2 

where:

* __CMC__: Constant string indicating that the data is from the Canadian Meteorological Centre.
* __hrdps__: Constant string indicating that the data is from the High Resolution Deterministic Prediction System.
* __west__: Constant string indicating the West domain the data is from
* __Variable__: Variable type included in this file.
* __LevelType__: Level type.
* __Level__: Level value.
* __ps1.0km__: Constant string indicating that the projection used is polar-stereographic at 1.0 km resolution.
* __YYYYMMDD__: Year, month and day of the beginning of the forecast.
* __HH__: UTC run time [00, 12].
* __Phhh__: P is a constant character. hhh is the forecast hour [000, 001, 002, ..., 035, 036].
* __mm__: mm are the forecast minutes [Hard-coded to 00 for now. In the future 30 minute timesteps will be available].
* __grib2__: Constant string indicating the GRIB2 format is used.

Example of file name:

CMC_hrdps_west_DEPR_ISBL_0175_ps1.0km_2019082512_P003-00.grib2

This file originates from the Canadian Meteorological Center (CMC) and contains the experimental West data of the High Resolution Deterministic Prediction System. The data in the file start on August 25th 2019 at 12Z (2019082512). It contains the dew point depression (DEPR) at the isobaric level 175 mb (ISBL_0175) on a polar-stereographic at 1.0 km resolution (ps2.5km) for the forecast hour 03 (P003) and 00 minutes (-00) in GRIB2 format (.grib2).

## Levels

Vertical coverage of three-dimensional fields is provided by up to 28 isobaric levels.

Isobaric levels (hPa): 1015, 1000, 0985, 0970, 0950, 0925, 0900, 0850, 0800, 0750, 0700, 0650, 0600, 0550, 0500, 0450, 0400, 0350, 0300, 0275, 0250, 0225, 0200, 0175, 0150, 0100, 0050.

Some fields receive limited three-dimensional coverage of 4 levels in the vertical.

Isobaric levels (reduced coverage, hPa): 0850, 0700, 0500, 0250.

Additional levels that may be applicable to a given parameter are:

* Surface
* Fixed height above ground
* Fixed height below ground
* Thickness between two isobaric levels
* Nominal top of the atmosphere
* Entire atmospheric column

## List of variables

Warning: the tables below are not up to date (to come), some variables are missing. Feel free to [contact us](mailto:ec.dps-client.ec@canada.ca) for more information.

* [000h forecast](https://weather.gc.ca/grib/HRDPS_HR/HRDPS_nat_ps2p5km_P000_deterministic_e.html)
* [Non-zero hour forecast](https://weather.gc.ca/grib/HRDPS_HR/HRDPS_ps2p5km_PNONZERO_deterministic_e.html)

## Support

If you have any questions about these data, please contact us at: [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).

