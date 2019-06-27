[En Français](readme_prev-vertical-pfl-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC Open Data](../readme_en.md) > Vertical profiles' forecast

# Vertical profiles' forecast data in CSV format

This page describes the forecast data of the vertical profiles.

## Description 

Prognostic 'Tephigram' data for various locations across Canada.

Prog tephi data consists of forecast values derived from the Canadian GEM regional model (10 km resolution).

Data provided and units (not necessarily in this order):

* __TT__ : Temperature  (deg C)
* __ES__ : Dew point depression (deg C)
* __WD__ : Wind direction (deg true)
* __UV__ : Wind speed (knots)
* __HR__ : Relative humidity (decimal fraction; e.g.  .58 = 58%) 
* __GZ__ : Geopotential height (decametres with 2 digits after the decimal)
* __WW__ : Vertical velocity  (Pa/sec)

Pressure levels :
* start at surface
* GZ, ES, UV, WD, HR and TT available at: SFC 1000 985 970 950 925 900 875 850 800 750 700 650 600 550 500 450 400 350 300 275 250 225 200175  150 100  70  50  30  20  10 mb
* WW for 29 levels (Not at 70, 30 or 20 mb)

Note: Some of the pressure levels may be below the elevation of the station. 

Time steps :
* Data values are provided in time steps of 3 hrs from 00-48 hrs

Data Format :
* data are in ASCII in .csv file
* data may be switched to BUFR format in the future  

Possible display programs

While Environment and Climate Change Canada does not provide a display software nor does not recommend any particular third party programs to display this data in graphical format some users have suggested:

* Buffkit :
    * http://wdtb.noaa.gov/tools/BUFKIT/index.html
* RAOB from Environmental Research Services :
    * http://www.raob.com/ 
* NCAR Command Language :
    * http://www.ncl.ucar.edu/get_started.shtm

## Data location 

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](.../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](.../../usage/readme_en.md) is also available.

The data is available using the HTTP protocol and resides in a directory that is plainly accessible to a web browser. Visiting that directory with an interactive browser will yield a raw listing of links, each link being a downloadable GRIB2 file.

The vertical profiles files are available at the following address:
* https://dd.weatheroffice.ec.gc.ca/vertical_profile/

An history of 24 hours of data is kept in the directory.

## Directory and filename nomenclature 

NOTE: ALL HOURS ARE IN UTC.

The files are grouped in a directory tree that is based on the type of vertical profile (observation or forecast) and the format  (currently only CSV is available).

__1- The directories have the following nomenclature :__
* https://dd.weatheroffice.ec.gc.ca/vertical_profile/TYPE/FORMAT/

where:
* __TYPE__ : string for the product type. Can be "forecast" or "observation"
* __FORMAT__ : format of data. Currently only 'csv' is available

Example : 
https://dd.weatheroffice.ec.gc.ca/vertical_profile/forecast/csv/

__2- The filenames have the following nomenclature :__
TYPE_HH_AAAA.csv

where :
* __TYPE__ : string for the product type. Can be "ObsTephi" or "ProgTephi"
* __HH__ : Run hour. Can be "00" or "12"
* __AAAA__ : 4 letters station code. The complete list can be found here:
    * https://dd.ec.gc.ca/vertical_profile/doc/station_list_for_vertical_profile.txt

Example : 
ProgTephi_12_WASA.csv

## Support

If you have any questions about these data, please contact us at: ec.dps-client.ec@canada.ca

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).




