[En français](readme_obs_insitu_swobdatamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [Observations by station](readme_obs_insitu_en.md) > Observations by station on MSC Datamart

# Surface Weather and Marine Observation Markup Language (SWOB Met-ML) by station in XML format

This page describes the [surface weather and marine observation](readme_obs_insitu_en.md) data available in XML format.

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available using the HTTPS protocol and resides in a directory that is plainly accessible to a web browser. Visiting that directory with an interactive browser will yield a raw listing of links, each link being a downloadable XML file.

Data are available at the following addresses :

* __Land-based observations :__

* [https://dd.weather.gc.ca/today/observations/swob-ml/{YYYYMMDD}/{XXXX}/](https://dd.weather.gc.ca/today/observations/swob-ml)

where :

* __YYYYMMDD__ : Observation date in UTC. 
* __XXXX__ : Station code (WMO ID).

Moreover, there is a special directory containing the last observations received from each station :
[https://dd.weather.gc.ca/today/observations/swob-ml/latest/](https://dd.weather.gc.ca/today/observations/swob-ml/latest/)

__Note__: A [dynamic list of observation stations](https://dd.meteo.gc.ca/today/observations/doc/swob-xml_station_list.csv) is available and updated daily.

* __Marine observations :__

https://dd.weather.gc.ca/today/observations/swob-ml/marine/moored-buoys/{YYYMMDD}/{XXXXXXX}

where :

* __YYYYMMDD__ : Observation date in UTC.
* __XXXXXXX__ : Station code (WMO ID), could be 5 or 7 digits.

__Note__: A [list of marine observations](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_station/swob-xml_marine_station_list.geojson) is available.

* __Partner observations :__
  
https://dd.weather.gc.ca/today/observations/swob-ml/partners/{NETWORK}/{YYYMMDD}/{MSC-ID}

where :

* __NETWORK__ : Acronym of partner's network.
* __YYYYMMDD__ : Observation date in UTC.
* __MSC-ID__ : Partner’s unique MSC station id.

__Notes__:

* A [list of partners stations](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_station/swob-xml_partner_station_list.geojson) is available.
* The Department of Fisheries and Ocean moored buoys (aka Viking buoys) are seasonal. They are typically recalled in November and 
re-deployed in June. From November to June there will be no data transmitted from the buoys

## Nomenclature 

* __SWOB files follow this naming convention :__

YYYY-MM-DD-hhmm-XXXX-TYPE-CCz-swob.xml

where :

* **YYYY-MM-DD-hhmm** : Observation date in UTC.
* __XXXX__ : Station code (WMO ID).
* __TYPE__ : AUTO or MANNED station.
* __CCz__ : Optional. Cor stands for Correction and z is a letter indication the number of corrections ('A' stands for the first, 'B' for the second, etc.). By default, this field would not be there for the first observation.
* __swob.xml__: Constant string indicating the product and the format.

In the 'latest' directory, the file names are static for each station and take the form of:

latest_XXXX_TYPE_swob.xml

where :

* __latest__ : Constant string indicating that this is the latest observation received from this station.
* __XXXX__ : Station code.
* __TYPE__ : AUTO or MANNED station.
* __swob.xml__ : Constant string indicating the product and the format.

Example :

2013-09-20-1300-CYAZ-MAN-swob.xml 

This file contains the manual observation of the September 20th 2013 at 13:00 UTC for the station CYAZ (Tofino).

* __Marine SWOB files follow the naming convention :__

YYYY-MM-DD-hhmm-XXXXXXX-TYPE-swob.xml

where :

* __YYYY-MM-DD-hhmm__ : Observation date and time in UTC.
* __XXXXXXX__ : Station code (WMO ID). Could be either 5 or 7 digits.
* __TYPE__ : AUTO station.
* __swob.xml__ : Constant string indicating the product and the format.

Example :

2019-01-27-0000-4400488-AUTO-swob.xml

* __Partner SWOB files follow the naming convention :__
  
YYYY-MM-DD-hhmm-network-ID-AUTO-swob.xml

where :

* __YYYY-MM-DD-hhmm__ : Observation date in UTC.
* __network__ : Partner's network.
* __ID__ : Partner’s unique MSC station ID.
* __swob.xml__ : constant string indicating the product and the format. 
  
Example :

2018-01-06-1400-bc-env-aq-138-AUTO-swob.xml

## Note

The specification of the data format is available in the [SWOB-ML product guide](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_station/SWOB-ML_Product_User_Guide_e.pdf).

## Support

If you have any questions about this data, [please contact us](https://weather.gc.ca/mainmenu/contact_us_e.html).

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).
