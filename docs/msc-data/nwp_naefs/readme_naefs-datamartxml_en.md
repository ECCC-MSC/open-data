[En français](readme_naefs-datamartxml_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [NAEFS](readme_naefs_en.md) > NAEFS on MSC Datamart

# North American Ensemble Forecast System (NAEFS) Data in XML Format

This page describes the [North American ensemble forecast system](readme_naefs_en.md) data available in GRIB2 format.

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The NAEFS XML files are available at the following address :

* [https://dd.weather.gc.ca/ensemble/naefs/xml/](https://dd.weather.gc.ca/ensemble/naefs/xml/)

A history of 30 days of forecast is kept in this directory.

## Nomenclature of file directories 

The files are grouped in a directory tree that is based on the date
and the variable contained in the XML files. The directories have the 
following nomenclature:

* [https://dd.weather.gc.ca/ensemble/naefs/xml/{AAAAMMJJ}/{ZZ}/{VARIABLE}/{TYPE}](https://dd.weatheroffice.gc.ca/ensemble/naefs/xml)


where :

* __AAAAMMJJ__ : Forecast integration date, year (YYYY), month (MM) and day (DD)
* __ZZ__ : Forecast integration time in UTC. Can be '00' or  '12'
* __VARIABLE__ : Variable in the XML files in the directory. Refer to the 'Variable List' section below for a complete list.
* __TYPE__ : Data type. Currently, only the direct model output ('raw') are
available.

Example : for the 12Z forecast on May 7th 2010, the raw data for the
surface wind speed will be in this directory :

[https://dd.weatheroffice.gc.ca/ensemble/naefs/xml/20100507/12/WIND-SFC/raw/](https://dd.weatheroffice.gc.ca/ensemble/naefs/xml/20100507/12/WIND-SFC/raw/)

## Nomenclature of file names :

NOTE : ALL HOURS ARE IN UTC.

The file name follows this nomenclature :

* AAAAMMJJHH_GEPS-NAEFS-TYPE_LOCATION_PROVSTATE_COUNTRY_VAR_START-END.xml.bz2

where :

* __AAAA__ : Forecast year, 4 digit.
* __MM__ : Forecast month, 2 digit (January = 01).
* __JJ__ : Forecast day, 2 digit.
* __HH__ : Integration time, 2 digit (00 or 12 - representing UTC time).
* __GEPS-NAEFS__ : Constant string indicating the GEM model (GEPS) for the
EPSgrams in the scope of the NAEFS project.
* __TYPE__ : Can take the value 'RAW' for raw data model or 'BC' for
bias corrected data (currently only RAW is available).
* __LOCATION__ : Location name for the given forecast.
* __PROVSTATE__ : Location province (Canada) or State (USA, Mexico). 2
characters code. For other countries, the code 'XX' is used. You can
download the code correspondence list here : 
[http://www.state.ia.us/tax/forms/84055.pdf](http://www.state.ia.us/tax/forms/84055.pdf)
* __COUNTRY__ : Location country for the emitted forecast. CA=Canada,
US=USA, MX=Mexico, etc. For a complete list, refer to the « Country list »
section a the end of this file.
* __VAR__ : Variables. See the following section for a complete list.
* __START__ : Interval start time (in hours after the forecast start time) for
which the forecast is emitted.
* __END__ : Interval end time  (in hours after the forecast start time) for
which the forecast is emitted.


Example :

2010051000_GEPS-NAEFS-RAW_LONDON_ON_CA_MSLP_000-384.xml.bz2

This file contains models data for the date of May 10th 2010 at
00UTC(2010051000), in raw format (RAW) for the city of London (LONDON) in
Ontario (ON), Canada (CA). The mean sea level pressure (MSLP) will be
contained in this file for the first 384 hours of forecast (000-384). This
is an XML files (xml) compressed using bzip algorithm (bz2).

The complete URL would be :

[https://dd.weatheroffice.gc.ca/ensemble/naefs/xml/20100507/00/MSLP/raw/2010050700_GEPS-NAEFS-RAW_LONDON_ON_CA_MSLP_000-384.xml.bz2](http://dd.weatheroffice.gc.ca/ensemble/naefs/xml/20100507/00/MSLP/raw/2010050700_GEPS-NAEFS-RAW_LONDON_ON_CA_MSLP_000-384.xml.bz2)

## File contents

The XML files have been compressed with the bzip2 algorithm. To decompress
them, you can use the bunzip2 software (GNU/Linux, Mac OS X) or 7-zip
(Windows). They are encoded in UTF-8 format.

Each file is made of a header containing the information about the
location, the date and time of the beginning and end of each forecast, the
variable in the file, the unit used to represent it and the date and time 
of the file creation.

Then follows the forecast blocks (<forecast>). Each forecast section
corresponds to a specific forecast hour. Each forecast contains a series
of models (<model>), containing the variable values for each model at this
time (see the Models List in the last section).
Note : Some models do not have a forecast at specific hours.

The file content looks like :
```xml
<?xml version='1.0' encoding='UTF-8'?>
   <naefs_spena_forecast>
      <header>
         <location description="XXXXXXXXX" pays_country="XX" province_state="XX"/>
         <valid-begin-time>XXXXXXXX</valid-begin-time>
         <valid-end-time>XXXXXXXX</valid-end-time>
         <forecast_element no="X" type="XX" niveau_level="X" titre_francais="XXXXXXXXXXXXXXXXXX" unite_francaise="XXX" title_english="XXXXXXXXXXXXX" unit_english="XXX"/>
        <model_description>
          <model id='1' model='GEM' member='000' center='CMC' domain='global' data_type='RAW' member_type='control'/>
          <model id='2' model='GEM' member='001' center='CMC' domain='global' data_type='RAW' member_type='member'/>
          <model id='3' model='GEM' member='002' center='CMC' domain='global' data_type='RAW' member_type='member'/>
               ...
        </model_description>
         <creation_date>XXXXXXXXXXX</creation_date>
      </header>
   <forecast forecast_hour='XXX' valid_time='XXXXXXXXXX'>
      <model id='1'>XXX</model>
               ...
   </forecast>
   <forecast forecast_hour='XXX' valid_time='XXXXXXXXXX'>
      <model id='1'>XXX</model>
      <model id='2'>XXX</model>
               ...
   </forecast>
         ...
</naefs_spena_forecast>
```

## Variable List

The XML files are produced for 10 variables :
* Mean Sea level Pressure (MSLP)
* Accumulated Precipitation at the Surface (APCP-SFC)
* Total Cloud Cover (TCDC)
* Wind Speed at 200 hPa (WIND-200HPA)
* Geopotential Height at 500 hPa (HGT-500HPA)
* Thicknesses 1000-500 (LAYER-1000-500HPA)
* Surface Air Temperature (TMP-SFC)
* Surface Relative Humidity (RELH-SFC)
* Surface Wind Speed (WIND-SFC)
* Surface Wind Direction (WDIR-SFC)

You can find a list in XML format containing the information for all the  
variables. It contains the name of the associated directory and a 
description and the units in both French and English.

The list can be found here:
[https://dd.weatheroffice.gc.ca/ensemble/doc/naefs/xml/elements.xml](https://dd.weatheroffice.gc.ca/ensemble/doc/naefs/xml/elements.xml)

## Available Locations

The XML output of the NAEFS ensemble forecasts are interpolated from grid
points of the forecast at the latitude-longitude coordinates from 540 
locations :
* 273 in Canada
* 137 in United States
* 74 in Mexico
* 56 in the tropics and Greenland

You can find locations list in XML format containing :
* Location name
* State or province
* Country name
* Codes, when applicable: NAEFS, WMO, IATA, ICAO
* Longitude, latitude and altitude (note that altitude is not available   
for some locations)

This list can be found at this address :

[https://dd.weatheroffice.gc.ca/ensemble/doc/naefs/xml/locations.xml](https://dd.weatheroffice.gc.ca/ensemble/doc/naefs/xml/locations.xml)

The correspondence for the 2 letter codes between the Provinces or States
can be found in this PDF document :

[http://www.state.ia.us/tax/forms/84055.pdf](http://www.state.ia.us/tax/forms/84055.pdf)

## Support

If you have any questions about this data, please contact us at : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).
 