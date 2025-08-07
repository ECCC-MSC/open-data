[En français](readme_climateltce-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [LTCE](readme_climateltce_en.md) > Climate Climate Records on MSC Datamart

# Daily Long Term Climate Extremes in CSV format

This page describes the [Daily Climate Records (Long Term Climate Extremes)](readme_climateltce_en.md) data in CSV format. Please note that these data should not be used to answer questions about climate trends. For these analyses, please consult the [Adjusted and Homogenized Canadian Climate Data](../climate_ahccd/readme_ahccd_en.md).

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available via the HTTPS protocol. It is possible to access it with a standard browser. In this case, we obtain a list of links giving access to a CSV file.

The data can be accessed at the following URLs:

* [https://dd.weather.gc.ca/today/climate/ltce/daily/{Variable}/{PROVINCE}](https://dd.weather.gc.ca/today/climate/ltce/daily)
* [https://dd.weather.gc.ca/today/climate/ltce/stations](https://dd.weather.gc.ca/today/climate/ltce/stations)

where:

* __Variable__: Taking one of the values [Temperature, Precipitation,Snowfall]
* __PROVINCE__: Two letter string identifying the province that the station resides in [ex: AB, BC, MB, etc.]

## File name nomenclature 

File names have the form:

* `climate_LTCE_{Variable}-Records_{PROVINCE}_{STATION-ID}.csv`

The lists of virtual stations have the form:

* `climate_LTCE_{Variable}_Virtual-Stations.csv`

where:

* __climate__: Constant string indicating climate dataset
* __LTCE__: Constant string indicating the name of the dataset that is long term climate extremes
* __Variable__: Name of variable available in the file, taking one of the values : [Temperature, Precipitation, Snowfall]
* __Records__: Constant string indicating that the data are records
* __PROVINCE__: Two letter string identifying the province that the station resides in, taking one the values : [AB, BC, MB, NB, NL, NS, NT, NU, ON, PE, QC, SK, YT]
* __STATION-ID__: Unique identifier for the station of interest
* __Virtual-Stations__: Constant string indicating that the file is a list of virtual stations
* __csv__: Constant string indicating the CSV format

Examples :

* climate_LTCE_Precipitation-Records_ON_VSON104.csv
* climate_LTCE_Temperature_Virtual-Stations.csv

## Variable list

The available variables and units for the Long Term Climate Extremes of climate indices are:

* High Max Temp: Highest daily temperature (°C)
* High Min Temp: Highest minimum daily temperature (°C)
* Low Max Temp: Coldest maximum daily temperature (°C)
* Low Min Temp: Coldest daily temperature (°C)
* Precipitation: Maximum daily precipitation (mm)
* Snowfall: Maximum daily snowfall (cm)

## Support

If you have any questions about this data, please [contact us](mailto:info.cccs-ccsc@canada.ca).

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).
