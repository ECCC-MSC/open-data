[En Français](readme_swob-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC Open Public Data](../readme_en.md) > Observations by station

# Surface Weather and Marine Observation Markup Language (SWOB Met-ML) by station in XML format

This page describes the [surface weather and marine observation](readme_swob_en.md) data available in XML format.

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](.../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](.../../usage-overview/readme_en.md) is also available.

The data is available using the HTTP protocol and resides in a directory that is plainly accessible to a web browser. Visiting that directory with an interactive browser will yield a raw listing of links, each link being a downloadable XML file. In practice, we recommend writing your own script to automate the downloading of the desired data (using wget or equivalent). If you are unsure of how to proceed, you might like to take a look at our brief wget usage guide.

Data are available at the following addresses:

* __Land-based observations :__

https://dd.weather.gc.ca/observations/swob-ml/YYYYMMDD/XXXX/

where :

* YYYYMMDD: observation date in UTC 
* XXXX: station code (WMO ID)

Moreover, there is a special directory containing the last observations received from each station:
https://dd.weather.gc.ca/observations/swob-ml/latest/

__Note__: A [dynamic list of observation stations](https://dd.meteo.gc.ca/observations/doc/swob-xml_station_list.csv) is available and updated daily.

* __Marine observations :__

https://dd.weather.gc.ca/observations/swob-ml/marine/moored-buoys/YYYMMDD/XXXXXXX

where:

* YYYYMMDD: observation date in UTC
* XXXXXXX: station code (WMO ID), could be 5 or 7 digits

__Note__: A [list of marine observations](https://dd.meteo.gc.ca/observations/doc/swob-xml_marine_station_list.csv) is available.

* __Partner observations :__
  
https://dd.weather.gc.ca/observations/swob-ml/partners/NETWORK/YYYMMDD/MSC-ID

where :

* NETWORK: acronym of partner's network
* YYYYMMDD: observation date in UTC
* MSC-ID: partner’s unique MSC station id 

__Note__: A [list of partners stations](https://dd.meteo.gc.ca/observations/doc/swob-xml_partner_station_list.csv) is available.

## Nomenclature 

NOTE: ALL HOURS ARE IN UTC.

* __SWOB files follow this naming convention :__

YYYY-MM-DD-hhmm-XXXX-TYPE-CCz-swob.xml

where:

* YYYY-MM-DD-hhmm: observation date in UTC
* XXXX: station code (WMO ID)
* TYPE: AUTO or MANNED station
* CCz: optional. Cor stands for Correction and z is a letter indication the number of corrections ('A' stands for the first, 'B' for the second, etc.). By default, this field would not be there for the first observation.
* swob.xml: constant string indicating the product and the format

In the 'latest' directory, the file names are static for each station and take the form of:

latest_XXXX_TYPE_swob.xml

where:

* latest: constant string indicating that this is the latest observation received from this station
* XXXX: Station code
* TYPE: AUTO or MANNED station
* swob.xml: constant string indicating the product and the format

Example:

2013-09-20-1300-CYAZ-MAN-swob.xml 

This file contains the manual observation of the September 20th 2013 at 13:00 UTC for the station CYAZ (Tofino).

* __Marine SWOB files follow the naming convention :__

YYYY-MM-DD-hhmm-XXXXXXX-TYPE-swob.xml

where:

* YYYY-MM-DD-hhmm: observation date and time in UTC
* XXXXXXX: Station code (WMO ID). Could be either 5 or 7 digits.
* TYPE: AUTO station
* swob.xml: constant string indicating the product and the format

Example:

2019-01-27-0000-4400488-AUTO-swob.xml

* __Partner SWOB files follow the naming convention :__
  
YYYY-MM-DD-hhmm-network-ID-AUTO-swob.xml

where:

* YYYY-MM-DD-hhmm: observation date in UTC
* network: partner's network
* ID: partner’s unique MSC station ID
* swob.xml: constant string indicating the product and the format 
  
Example:

2018-01-06-1400-bc-env-aq-138-AUTO-swob.xml

## Note

The specification of the data format is available in the [SWOB-ML product guide](http://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_station/SWOB-ML_Product_User_Guide_v8.2_e.pdf).

## Support

If you have any questions about these data, please contact us at: ec.dps-client.ec@canada.ca

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).
