[En Français](readme_prev-vertical-pfl-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC Data](../readme_en.md) > [Vertical profiles forecast](readme_prev-vertical-pfl_en.md) > Vertical profiles forecast on MSC Datamart

# Vertical profiles forecast data from the Regional Deterministic Prediction System

This page describes the [vertical profiles of the Regional Deterministic Prediction System (RDPS)](readme_prev-vertical-pfl_fr.md), available on the MSC Datamart.

## Data location 

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available using the HTTP protocol and resides in a directory that is plainly accessible to a web browser. Visiting that directory with an interactive browser will yield a raw listing of links, each link being a downloadable CSV file.

The vertical profiles files are available at the following address :

[https://dd.weatheroffice.ec.gc.ca/vertical_profile/forecast/csv](https://dd.weatheroffice.ec.gc.ca/vertical_profile/forecast/csv)

The data are available at 00Z and 12Z, from 00h to 48h, every 3 hours.

An history of 24 hours of data is kept in the directory.

## Filename nomenclature 

NOTE : ALL HOURS ARE IN UTC.

The filenames have the following nomenclature :

ProgTephi_HH_AAAA.csv

where :

* __HH__ : Run hour. Can be "00" or "12"
* __AAAA__ : 4 letters station code. A [complete list of stations](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/prev_vertical-profiles/station_list_for_vertical_profile.geojson) is available.

Example : 

ProgTephi_12_WASA.csv
 
## Data description 

Data provided and units are as the following :

* __TT__ : Temperature  (deg C)
* __ES__ : Dew point depression (deg C)
* __WD__ : Wind direction (deg true)
* __UV__ : Wind speed (knots)
* __HR__ : Relative humidity (decimal fraction; e.g.  .58 = 58%) 
* __GZ__ : Geopotential height (decametres with 2 digits after the decimal)
* __WW__ : Vertical velocity  (Pa/sec)

The data are available on the following pressure levels :

* Surface level
* GZ, ES, UV, WD, HR and TT available at: SFC 1000 985 970 950 925 900 875 850 800 750 700 650 600 550 500 450 400 350 300 275 250 225 200175  150 100  70  50  30  20  10 mb
* WW for 29 levels (Not at 70, 30 or 20 mb)

__Note__ : Some of the pressure levels may be below the elevation of the station. 

## Note

While Environment and Climate Change Canada does not provide a display software nor does not recommend any particular third party programs to display this data in graphical format some users have suggested :

* [Buffkit](https://training.weather.gov/wdtd/tools/BUFKIT/index.php)
* [RAOB de la compganie Environmental Research Services](https://www.raob.com/)
* [NCAR Command Language](https://www.ncl.ucar.edu/get_started.shtml)

## Support

If you have any questions about these data, please contact us at: ec.dps-client.ec@canada.ca

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).




