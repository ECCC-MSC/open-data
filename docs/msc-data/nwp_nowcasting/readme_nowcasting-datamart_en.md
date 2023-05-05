[En français](readme_nowcasting-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [Scribe Nowcasting Matrices](readme_nowcasting_en.md) > Scribe Nowcasting Matrices on MSC Datamart

# Scribe nowcasting matrices

The [scribe nowcasting matrices](readme_nowcasting_en.md) are updated every hour and contain a consistent set of observed and forecasted weather elements for the short term and for a number of forecast points generally corresponding to observation stations. 

There are over 450 forecast points in the file. Hourly surface observations (METAR, SPECI) and synoptic messages are processed as well as lightning observations.

Numerical Weather Prediction models, Statistical models and Nowcasting systems are used in conjunction with the observations to produce a very short term forecast.

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available using the HTTPS protocol and resides in a directory that is plainly accessible to a web browser. Visiting that directory with an interactive browser will yield a raw listing of links, each link being a downloadable GRIB2 file.

The data can be accessed at the following URLs :

* [https://dd.weatheroffice.gc.ca/nowcasting/matrices/](https://dd.weatheroffice.gc.ca/nowcasting/matrices/)

A 24-hour history is kept in this directory.

## File name nomenclature 

NOTE: ALL HOURS ARE IN UTC.

The files have the following nomenclature:

SCRIBE.NWCSTG.10.24.06Z.n.Z

where :

* __SCRIBE__ : Main system production
* __NWCSTG__ : Indentifies the matrix data type (Here Nowcasting) in the file
* __10.24.06Z__ : MM.DD.HHZ MM: Month, DD: date. HH: Run Time UST Z: UTC identification
* __n__ : Nowcasting extension file name
* __Z__ : Unix compression file idenfication

## Data

### Example of a Nowcasting matrix followed by it's content description.


|  1    |  2 | 3 | 4 |  5  | 6|   7  | 8 |  9  | 10| 11| 12 | 13|  14 |  15 |16 | 17| 18|  19 |20|  
|--------|-----|---|---|-----|---|-----|---|-----|----|---|---|---|-----|-----|----|---|---|----|---|
|DATE    |  HR |/10|   |PCPN1|POP|PCPN2|POP|PCPN3|POP|   | Qp | Tp|  T  |  Td | DD| VV|GST|(SM) |TP|
|20040122 0200| 10| 41| -S  |100|     |  0|     |  0|100| 0.2| SN| -6.0| -8.0|200| 22| 33| 2.00|PP|
|20040122 0300| 10| 24| -S  |100|     |  0|     |  0|100| 0.2| SN| -6.0| -7.0|200| 15|   | 1.75|PP|
|20040122 0400| 10| 23| -S  |100|     |  0|     |  0|100| 0.2| SN| -5.0| -6.0|200| 17|   | 2.50|PP|
|20040122 0500|  9| 25| -S  |100|     |  0|     |  0| 90| 0.0|   | -5.0| -6.0|206| 17|   | 7.98|  |
|20040122 0600|  9| 87|     |  0|     |  0|     |  0|  0| 0.0|   | -5.0| -6.0|190| 11|   |12.00|  |
|20040122 0700| 10| 50| -S  |100|     |  0|     |  0|100| 0.0|   | -4.0| -6.0|185|  9|   | 6.75|  |
|20040122 0800| 10| 88| -S  |100|     |  0|     |  0| 80| 0.0|   | -3.0| -5.0|203| 17|   |10.21|  |
|20040122 0900|  9|999| -SW |100|     |  0|     |  0| 60| 0.0|   | -2.7| -5.1|221| 18| 29|15.00|  |
|20040122 1000|  9|999| -SW |100|     |  0|     |  0| 60| 0.0|   | -3.8| -7.2|229| 24| 34|15.00|  |
|20040122 1100|  9|999| -SW |100|     |  0|     |  0| 30| 0.0|   | -4.8| -7.5|236| 30| 40|15.00|  |
|20040122 1200|  9|999|     |  0|     |  0|     |  0|  8| 0.0|   | -5.9| -8.6|242| 36| 46|15.00|  |
|20040122 1300|  9|999|     |  0|     |  0|     |  0| 11| 0.0|   | -5.9| -8.7|252| 38| 48|15.00|  |
|20040122 1400|  9|999|     |  0|     |  0|     |  0| 15| 0.0|   | -6.0| -8.8|261| 39| 49|15.00|  |
|20040122 1500|  9|999|     |  0|     |  0|     |  0| 16| 0.0|   | -6.0| -9.4|270| 41| 51|15.00|  |
|20040122 1600|  9|999|     |  0|     |  0|     |  0| 22| 0.0|   | -6.0|-10.0|274| 41| 51|15.00|  |
|20040122 1700|  9|999| -S  |100|     |  0|     |  0| 80| 0.2| SN| -6.0|-10.0|278| 41| 51|15.00|  |
|20040122 1800| 10|999| -S  |100|     |  0|     |  0|100| 0.5| SN| -6.0|-10.0|282| 41| 51|15.00|  |
|20040122 1900|  9|999| -S  |100|     |  0|     |  0| 80| 0.4| SN| -6.7|-10.8|281| 41| 51|15.00|  |
|20040122 2000|  9|999| -S  |100|     |  0|     |  0| 80| 0.2| SN| -7.3|-11.7|279| 40| 50|15.00|  |


In this example the data sequence begins at 02Z with six hours of observations before the run time 08Z, and ends 12 hours later at 20Z, for a total of 19 hours (6 hours of past observations, plus the current observation (run time) followed by 12 hours of forecast data.  

### Looking at columns from left to right.

__Column no. :__

__1 & 2__ : The first two columns identify the date and time. The current run time
       is the 7th line of the matrix (the one between the two dashed lines)

__3 & 4__ : Column 3 gives the sky cover in tenths, and column 4 the ceiling height in hundreds of feet. 
       If no ceiling is forecasted the code "999" will be used. Note that this ceiling 
       value is there only for technical reasons and is not very reliable, certainly not for 
       aviation forecast.

__5, 6 ,7 ,8 ,9, 10__ : These six columns represent the precipitation types and related
probability of occurrence, which should not be confused with the total (global) probability 
of precipitation or POP in column 11. The precipitation type probability give the probability 
of occurrence of this type, in this example only snow is observed and forecast, 
with a probability of 100%. Total value should not exceed 100%.

The following Scribe Nowcasting precipitation type codes are possible :
|(F): forecasted  |  (O): observed  |
|-----------------|-----------------|
| Rain Showers    |   RW  (F & O)   |
| Rain            |  R   (F & O)    | 
| Snow Showers    |   SW  (F & O)   |
| Snow            |   S   (F & O)   |
| Drizzle         |   L   (F & O)   |
| Freezing Rain   |   ZR  (F & O)   |
| Freezing Drizzle|   ZL  (F & O)   |
| Ice Pellet Shower|  IPW (F & O)   |
| Ice Pellet      |   IP  (F & O)   |
| Thunder         |   T   (F & O)   |
| Hail            |   A   (F & O)   |
| Not Available   |   NA  (F & O)   |     

        
        
__Intensity of precipitation given by :__
* (-) very light to light
* ( ) (no sign) moderate
* (+) heavy

In certain circumstances, for instance when temperatures are near zero, it is possible to have more than one precipitation type at any given moment, for example: snow mixed with rain and occasional freezing rain.  

In that situation the dominant condition (snow) would appear in type 1 (PCPN1) while the associated precipitation would be type 2 (PCPN2) for rain and type 3 (PCPN3) for freezing rain.
       
__11__ :    Column 11 identified "POP" is the all types together probability of precipitation. In the observations 
       section, i.e. from 02Z to 07Z the POP observed could be les then 100%. In other words, 
       although if it is not precipitating at the station, a POP may exist du to some observed 
       information such as "vicinity showers" convective clouds, radar echoes or lightning around the station. 

__12, 13__ : The next two columns refer to the precipitation quantity, in mm/hr of water (or cm/hr for snow) 
       and the type of precipitation corresponding to this accumulation. In the example a total of 0.6 cm 
       of snow (not mm since it is snow) accumulated from 02Z to 04Z included, and a snow amount forecast 
       of 1.3 cm from 17Z to 20Z included. Only the dominant (higher POP type) precipitation type of 
       the possible 3 will be considered for the precipitation accumulated during a given hour.

__14, 15__ : These two columns contain the temperature and the dew point observations and forecasts; 

__16, 17 ,18__ : The  next three columns are dedicated to the wind: direction, speed (km/h) and gust (km/h).  

__19, 20__ : The last two columns indicate the visibility (a reference distance value in statute miles) 
        and the type of obstacle to visibility.  The observed values represent the synthetized visibility based on the reported values
        in the METAR-SPECI surface observation. The forecasted visibilities use a predefined set of values (bins) corresponding 
        to visibility categories, e.g. poor are 0.5, average are 1.0 and 3.0, and good are 9.0 or 15.0. 
        A type of obstacle to the visibility will be associated to the reduction of visibility when lower than 6 miles, 
        for the observed or forecasted values.

The following visibility Scribe Nowcasting codes are possible :

|(F): forecasted |   (O): observed |
|----------------|-----------------|
| Precipitation  |   PP (F & O)    |
| Fog            |   FG (F & O)    |
| Fog banks      |   BF (F & O)    |
| Mist           |   BR (F & O)    |
| Risk Fog       |   RF (F)        |
| Ice Fog        |   IF (F & O)    |
| Blowing snow   |   BS (F & O)    |
| Drifting snow  |   DS (F & O)    |
| Haze           |   HZ (F & O)    |
| Smoke          |   FU (F & O)    |
| Blowing dust   |   BD (F & O)    |
| Not Available  |   NA (F & O)    |
     

### Notes

* Although the nowcasting weather elements are highly dependant and observations, a forecast will always be produced even if surface observations are incomplete, missing or not available at a specific location. Remote sensing observastions such as Radar, Satellite and Lightning detection will be used and utimately the weather elements from the Canadian Regional Deterministic Prediction System (RDPS NWP) will be used.

* A [stations list](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_nowcasting/nowcasting.geojson) is avaiable in GeoJSON format.

## Support

If you have any questions about this data, please contact us at : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).
