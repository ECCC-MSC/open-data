[En Français](readme_meteocode-datamartcsv_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC Open Public Data](../readme_en.md) > Meteocode forecast data

# Meteocode forecast data in CSV format

This document describes the content of the [meteocode data](readme_meteocode_en.md) in CSV format.

The files for meteocode data in CSV format are created from the CMML files
using the XSLT technology. The CSV files does not contain more information than
the CMML files, they are only in a different format. Moreover, each CMML files contains
many regions while each CSV file contains only one region.

## Data address 

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](.../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](.../../how-to/readme_en.md) is also available.

The data is available via the HTTP protocol. It is possible to access it with a standard browser. In this case, we obtain a list of links giving access to a GRIB2 file.

The files are available at the following address:

* https://dd.weather.gc.ca/meteocode/mtm/csv/
* https://dd.weather.gc.ca/meteocode/ont/csv/
* https://dd.weather.gc.ca/meteocode/pnr/csv/
* https://dd.weather.gc.ca/meteocode/pyr/csv/
* https://dd.weather.gc.ca/meteocode/que/csv/

An history of 24 hours is kept in these directories.

## File name nomenclature 

NOTE: ALL HOURS ARE IN UTC.

The filenames of the meteocode CSV files have the following nomenclature:

YYYY-MM-DDTHH-MM-SSZ_FPAANN_rRRRR_BB.csv

where:
* __YYYY-MM-DDTHH-MM-SSZ__ : time of emission for the forecast. Date is in ISO 8601 format. 
* __FP__ : constant string meaning "Forecast Public".
* __AANN__ : See the section 'Filename' in the CMML README at http://dd.weather.gc.ca/meteocode/doc/cmml/README_CMML.txt
* __r__ : constant string indicating the beginning of the region code.
* __RRRR__ : alphanumerical code indicating the region of the public forecast. Can be of an arbitrary length (ex: 3pe, 10zf, 71.14). The complete list of forecast region and their associated code can be found at the end of this file in the section "Region's code and name".
* __BB__ : string indicating the weather elements. Can be one of the following values: TA (Air Temperature), TD (Dew Point), PA (Precipitation accumulation), POP (Probability Of Precipitation), WS (Wind Speed and Direction), WG (Wind Gust), CC (Cloud Cover).

## File content

* For each forecast region, 7 files are created. The content of each file is described below.
* The ''-9999.00'' value is for a missing or an invalid data for air temperature or dew point.
* If no wind gust is available for the forecast valid time in the CMML files, then the 
  associated CSV file contains no data for this specific date.
* All dates are in ISO 8601 format.

__1. Air Temperature (TA)__

This file contains the air temperature.

The first line of these files contains:
 " Region_en | Region_fr ; CMML : 'cmml_filename.xml'","Valid time | Heure de validité;Air temperature (° Celsius) | Température de l'air (° Celsius)"

where:
* Region_en: English name of the forecast region;
* Region_fr: French name of the forecast region;
* CMML: constant string;
* cmml_filename.xml: name of the CMML file from which this CSV file originates;
* The 2 other values describe the content of each column:
    * Forecast valid time
    * Air temperature in degree Celsius.

Example of CSV file for air temperature:

|Fort Good Hope Region / Région de Fort Good Hope ; CMML : 'TRANSMIT.FPNT11.01.30.12Z.1128.xml'  Valid time / Heure de validité | Air temperature (° Celsius) / Température de l'air (° Celsius) |
|--------------------|--------|
|2009-01-30T10:00:00Z|-9999.00|
|2009-01-30T11:00:00Z|-9999.00|
|2009-01-30T12:00:00Z|-31.00|
|2009-01-30T13:00:00Z|-30.67|
|2009-01-30T14:00:00Z|-30.33|

__2. Dew Point (TD)__

This file contains dew point temperature.

The first line of these files contains:
 " Region_en | Region_fr ; CMML : 'cmml_filename.xml'","Valid time | Heure de validité;Dew point (° Celsius) | Point de rosée (° Celsius)"

where:
* Region_en: English name of the forecast region;
* Region_fr: French name of the forecast region;
* CMML: constant string;
* cmml_filename.xml: name of the CMML file from which this CSV file originates;
* The 2 other values describe the content of each column:
    * Forecast valid time
    * Dew point in degree Celsius.

Example of CSV file for dew point temperature:

|Fort Good Hope Region / Région de Fort Good Hope ; CMML : 'TRANSMIT.FPNT11.01.30.12Z.1128.xml' Valid time / Heure de validité | Dew point (° Celsius) / Point de rosée (° Celsius) |
|---------------------|--------|
|2009-01-30T10:00:00Z |-9999.00|
|2009-01-30T11:00:00Z|-9999.00|
|2009-01-30T12:00:00Z|-36.00|
|2009-01-30T13:00:00Z|-35.00|
|2009-01-30T14:00:00Z|-34.00|

__3. Precipitation Accumulation (PA)__

This file contains the precipitation accumulation and type.

The first line of these files contains:
 " Region_en | Region_fr ; CMML : 'cmml_filename.xml''","Start | Début;End | Fin;Total accumulation min (mm) | Accumulation totale min (mm);Total accumulation max (mm | Accumulation totale max (mm);Hourly accumulation min (mm) | Accumulation horaire min (mm);Hourly accumulation max (mm) | Accumulation horaire max (mm);Precipitation type | Type de précipitation","","","","",""

where:
* Region_en: English name of the forecast region;
* Region_fr: French name of the forecast region;
* CMML: constant string;
* cmml_filename.xml: name of the CMML file from which this CSV file originates;
* The other values describe the content of each column:
    * Starting time of accumulation period;
    * Ending time of accumulation period;
    * Value of lower cumulative precipitation amount in mm;
    * Value of upper cumulative precipitation amount in mm;
    * Lower limit value of precipitation amount in mm;
    * Upper limit value of precipitation amount in mm;
    * Precipitation type. Can be amongst the following values::
        * rain
        * snow
        * ice pellet
        * freezing rain

Example of CSV file for accumulation of precipitations:

|Metro Montréal - Laval / Montréal métropolitain - Laval ; CMML : 'TRANSMIT.FPCN71.12.08.1630Z.xml'  Start / Début | End / Fin | Total accumulation min (mm) / Accumulation totale min (mm) |Total accumulation max (mm) / Accumulation totale max (mm) | Hourly accumulation min (mm) / Accumulation horaire min (mm) | Hourly accumulation max (mm) / Accumulation horaire max (mm) | Precipitation type / Type de précipitation |
|--------------------|--------------------|-----|-----|-----|-----|----|
|2009-12-09T11:00:00Z|2009-12-09T12:00:00Z|10.00|10.00|10.00|10.00|snow|
|2009-12-09T12:00:00Z|2009-12-09T13:00:00Z|20.00|20.00|10.00|10.00|snow|
|2009-12-09T13:00:00Z|2009-12-09T14:00:00Z|30.00|30.00|10.00|10.00|snow|
|2009-12-09T14:00:00Z|2009-12-09T15:00:00Z|40.00|40.00|10.00|10.00|snow|
|2009-12-09T15:00:00Z|2009-12-09T16:00:00Z|50.00|50.00|10.00|10.00|snow|
 
__4. Probability of precipitation (POP)__

This file contains the probability of precipitation in percent.

The first line of these files contains:
 " Region_en | Region_fr ; CMML : 'cmml_filename.xml''","Start | Début;End | Fin;Probability of precipitation (%) | Probabilité de précipitation (%)",""

where:
* Region_en: English name of the forecast region;
* Region_fr: French name of the forecast region;
* CMML: constant string;
* cmml_filename.xml: name of the CMML file from which this CSV file originates;
* The other values describe the content of each column:
    * Starting time of period for this probability of precipitation;
    * Ending time of period for this probability of precipitation;
    * Probability of precipitation, in percent.

Example of CSV file for probability of precipitations:
 "Saguenay | Saguenay ; CMML : 'TRANSMIT.FPCN73.12.08.1630Z.xml'","Start | Début;End | Fin;Probability of precipitation (%) | Probabilité de précipitation (%)",""
 2009-12-08T17:00:00Z,2009-12-08T23:00:00Z, 40
 2009-12-08T23:00:00Z,2009-12-09T19:00:00Z,  0
 2009-12-09T19:00:00Z,2009-12-10T05:00:00Z,100

Example of CSV file for probability of precipitations:

|Saguenay ; CMML : 'TRANSMIT.FPCN73.12.08.1630Z.xml'  Start / Début | End / Fin | Probability of precipitation (%) / Probabilité de précipitation (%) |
|----------------------|------------------|----|
|2009-12-08T17:00:00Z|2009-12-08T23:00:00Z| 40|
|2009-12-08T23:00:00Z|2009-12-09T19:00:00Z| 0|
|2009-12-09T19:00:00Z|2009-12-10T05:00:00Z|100|

__5. Wind (WS)__

This file contains the values of wind speed and direction.

The first line of these files contains:
 " Region_en | Region_fr ; CMML : 'cmml_filename.xml''","Start | Début;End | Fin; Wind speed min (km/h) | Vitesse du vent min (km/h);Wind speed max (km/h) | Vitesse du vent max (km/h);Wind direction | Direction du vent",""

where:
* Region_en: English name of the forecast region;
* Region_fr: French name of the forecast region;
* CMML: constant string;
* cmml_filename.xml: name of the CMML file from which this CSV file originates;
* The other values describe the content of each column:
    * Starting time of period;
    * Ending time of period;
    * Lower value of wind speed, in km/h.
    * Higher value of wind speed, in km/h.
    * String for wind direction. Can be one of these values:
        *east
        * nil
        * north
        * northeast
        * northwest
        * west
        * easterly
        * northerly
        * northeasterly
        * northwesterly
        * westerly
        * southerly
        * southeasterly
        * southwesterly
        * south
        * southeast
        * southwest
        * variable 

Example of CSV file for wind speed and direction:

| Rimouski - Mont-Joli ; CMML : 'TRANSMIT.FPCN74.12.08.1630Z.xml'  Start / Début | End / Fin  | Wind speed min (km/h) / Vitesse du vent min (km/h) | Wind speed max (km/h) / Vitesse du vent max (km/h) | Wind direction / Direction du vent  |
|-----------------------------------------------------------------------------------------------------|-----------|--------------------------------------------------|---------------------------------------------------|---------------------------------------|
|2009-12-08T17:00:00Z |2009-12-09T05:00:00Z|20|20|northwest|
|2009-12-09T05:00:00Z |2009-12-09T11:00:00Z|10|10|west|
|2009-12-09T11:00:00Z |2009-12-09T17:00:00Z|15|15|east|
|2009-12-09T17:00:00Z |2009-12-10T02:00:00Z|20|20|northeast|
|2009-12-10T02:00:00Z |2009-12-10T05:00:00Z|40|40|northeast|

__6. Wind Gust (WG)__

This file contains the values of wind gust.

The first line of these files contains:
 " Region_en | Region_fr ; CMML : 'cmml_filename.xml'","Start | Début;End | Fin; Wind gust min (km/h) | Vitesse des rafales min (km/h);Wind gust max (km/h) | Vitesse des rafales max (km/h)"
 
where:
* Region_en: English name of the forecast region;
* Region_fr: French name of the forecast region;
* CMML: constant string;
* cmml_filename.xml: name of the CMML file from which this CSV file originates;
* The other values describe the content of each column:
    * Starting time of period;
    * Ending time of period;
    * Lower value of wind gust, in km/h.
    * Higher value of wind gust, in km/h.

Example of CSV file for wind gust:

|New Carlisle - Chandler ; CMML : 'TRANSMIT.FPXK55.10.04.1500Z.xml'; Time zone Fuseau horaire : EST5EDT   Start / Début |  End / Fin  | Wind gust min (km/h) / Vitesse des rafales min (km/h) |Wind gust max (km/h) / Vitesse des rafales max (km/h)   |
|------------------------------------------------------|--------------------------|-----------------------------------------------------|-----------------------------------|
|2016-10-05T22:00:00Z|2016-10-06T03:00:00Z|70|70|
|2016-10-06T03:00:00Z|2016-10-06T12:00:00Z|70|70|
|2016-10-06T12:00:00Z|2016-10-06T15:00:00Z|60|60|
|2016-10-06T15:00:00Z|2016-10-07T03:00:00Z|70|70|
|2016-10-07T03:00:00Z|2016-10-07T12:00:00Z|  |  |
|2016-10-07T12:00:00Z|2016-10-08T00:00:00Z|  |  |

__7. Cloud Cover (CC)__

This file contains the cloud cover in decimal format.

The first line of these files contains:
 " Region_en | Region_fr ; CMML : 'cmml_filename.xml''","Valid time | Heure de validité;Cloud cover (tenth) | Couverture nuageuse (dixième)"

where:
* Region_en: English name of the forecast region;
* Region_fr: French name of the forecast region;
* CMML: constant string;
* cmml_filename.xml: name of the CMML file from which this CSV file originates;
* The other values describe the content of each column:
    * Valid time for this cloud cover;
    * Cloud cover value, decimal.

Example of CSV file for cloud cover:

|Queens County P.E.I. / comté de Queens Î.-P.-É. ; CMML : 'TRANSMIT.FPHX55.11.23.2000Z.xml' Valid time / Heure de validité | Cloud cover (tenth) / Couverture nuageuse (dixième)|
|-----------------|----|
|2009-11-25T10:00:00Z|9|
|2009-11-25T11:00:00Z|9|
|2009-11-25T12:00:00Z|10|
|2009-11-25T13:00:00Z|10|
|2009-11-25T14:00:00Z|10|
|2009-11-25T15:00:00Z|10|

## Support

If you have any questions about these data, please contact us at: ec.dps-client.ec@canada.ca

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).
