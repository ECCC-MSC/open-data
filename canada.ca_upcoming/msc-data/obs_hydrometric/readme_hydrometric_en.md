[En Français](readme_hydrometric_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC Open Public data](../readme_en.md) > Hydrometric data

# Data and products of the Atmosphere-Ocean-Ice forecast system for the Gulf of St. Lawrence

## Description of the system

### Data File

The real-time hydrometric data is provided in a CSV format for the distribution 
by Environment and Climate Change Canada.

The files updated on an hourly basis contain the last 2 complete days of data 
plus the current incomplete day. The files updated on a daily basis contain the 
last 30 complete days of data plus the current incomplete day.

The first line is a bilingual header, followed by data records. Below are the 
English column descriptors:

 ID,Date,Water Level (m),Grade,Symbol,QA/QC,Discharge (cms),Grade,Symbol,QA/QC

where:
*  __ID__ : station identifier. The first two digits indicate the major drainage 
       basin in which the station is located. The next two characters indicate 
       the sub-basin and sub-sub-basin. The last three digits indicate the 
       specific station within the sub-sub-basin.

* __Date__ : data timestamp in ISO 8601 format, Local Standard Time (LST)

* __Water Level (m)__ : water level in meters 

* __Grade__ : future use

* __Symbol__ : future use

* __QA/QC__ : quality assurance/quality control flag for the water level 
         (1 = preliminary, 2 = reviewed, 3 = checked, 4 = approved)

* __Discharge (cms)__ : discharge in cubic meters per second

* __Grade__ : future use

* __Symbol__ : future use

* __QA/QC__ : quality assurance/quality control flag for the discharge

Please note that the timestamps of the data are always in LST at that 
particular station. The timestamps of the data records show the offset from 
UTC.


### Station List File

The list of all the real-time hydrometric stations is available here:

https://dd.weather.gc.ca/hydrometric/doc/hydrometric_StationList.csv

The first line is a bilingual header, followed by station metadata. Below
are the English column descriptors:

 ID,Name,Latitude,Longitude,Prov/Terr,Timezone

where:
*  __ID__ : station identifier

* __Name__ : name of the station. The name is in English or French depending on the 
        location of the station

* __Latitude__ : latitude in decimal format

* __Longitude__ : longitude in decimal format

* __Prov/Terr__ : 2-letter code for the province or territory

* __Timezone__ : LST offset from UTC

## Access

### How to access the data

These data are available on the data server services [MSC Datamart](../../msc-datamart/readme_en.md) and the web services [MSC GeoMet](../../msc-geomet/readme_en.md) respectively:

* [CSV data available on the MSC Datamart](readme_hydrometric-datamart_en.md) 
* Link to the subpage of the dataset for GeoMet [example](../../msc-geomet/giops_en.md), if the subpage exists 
	* NOTE: does not exist for the GDPS

An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage-overview/readme_en.md) is available.

### Licence

The [End-User Licence for Environment and Climate Change Canada's Data Servers](../../licence/readme_en.md) specifies the conditions of use of these data.


### Metadata

The [metadata of the real time hydrometric data tool are available on the Open Government Portal](https://open.canada.ca/data/en/dataset/ef2161a8-b01d-4dfb-ad00-1a70f7c4073b)

## Technical documentation

* [Water Survey of Canada](http://www.ec.gc.ca/rhc-wsc/default.asp?lang=En)
* [Real-time and historical water level and discharge data](http://wateroffice.ec.gc.ca/ )

## Change log

_Not applicable._