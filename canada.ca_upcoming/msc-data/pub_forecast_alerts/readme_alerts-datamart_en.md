[En Français](readme_alerts-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC Open Public Data](../readme_en.md) > CAP

# Weather warning XML data in the format of the Common Alerting Protocol (CAP)

This page describes the [weather warning data in the format of the Common Alerting Protocol (CAP)](readme_alerts_en.md).

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](.../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](.../../usage-overview/readme_en.md) is also available.

The data is available using the HTTP protocol and resides in a directory that is plainly accessible to a web browser. Visiting that directory with an interactive browser will yield a raw listing of links, each link being a downloadable XML file. In practice, we recommend writing your own script to automate the downloading of the desired data (using wget or equivalent). If you are unsure of how to proceed, you might like to take a look at our brief wget usage guide.

The data can be accessed at the following URLs:

https://dd.weather.gc.ca/alerts/cap/

A history of 1 month is maintained in this directory.

A Standardized package of GIS (Geographical Information System) based
forecast location shapefiles, for all the forecast locations used in
ECCC CAP Messages, are available at the following address:

https://dd.weather.gc.ca/meteocode/geodata/

Shapefile packages found there are the same Shapefiles that are used
in the operational environment where ECCC warnings are initially
generated. The Shapefile packages are versioned in order to track the
available packages to the package used in the operational environment
at any given time. Beginning with version 5.0.3 of the GIS package, 
usage dates for the package will be included in the documentation.

## File name nomenclature 

The CAP-XML are grouped in a directory tree that is based on the date
and the responsible office (see note1) code for the alert. The exception is for 
tornado warning and severe thunderstorm warning alerts which are grouped 
based on a LAND or WATR (see note2) designation rather than responsible office. 
The LAND directory contains the CAP-XML files for all tornado warning and 
severe thunderstorm warning alerts that are issued over land zones in Canada. 
The WATR directory contains the CAP-XML files for all tornado warning alerts 
that are issued over water zones in Canada. 

Note1: The term "responsible" office is used as it is independent of the 
"issuing" office which sends the alert. Normally, the "responsible" office is also 
the "issuing" office. However, in contingency situations the "issuing" office can 
be different. "Responsible" office is used for routing and distribution 
purposes (the right message to the right place) and the “issuing” office is used 
for accounting and performance measurement purposes (who wrote it).


| Code        |  Name English             |   Name French        |  Acronym English    |  Acronym French  |  City        | Time Zone Code  |
|-------------|---------------------------|----------------------|---------------------|------------------|--------------|-----------------|
| CWUL | Quebec Storm Prediction Centre |centre de prévision des intempéries du Québec|QSPC | CPIQ        | Montréal     | EST5EDT         |
| CWEG |Prairie and Arctic Storm Prediction Centre|centre de prévision des intempéries des Prairies et de l'Arctique|PASPC|CPIPA|Edmonton|MST7MDT|
| CWNT |Prairie and Arctic Storm Prediction Centre|centre de prévision des intempéries des Prairies et de l'Arctique|PASPC|CPIPA|Edmonton|MST7MDT|
| CWWG |Prairie and Arctic Storm Prediction Centre|centre de prévision des intempéries des Prairies et de l'Arctique|PASPC|CPIPA|Winnipeg|CST6CDT|
| CWVR |Pacific and Yukon Storm Prediction Centre|centre de prévision des intempéries de la région du Pacfique et du Yukon|PSPC|CPIP|Vancouver|PST8PDT|
| CWTO |Ontario Storm Prediction Centre|centre de prévision des intempéries de l'Ontario|OSPC|CPIO|Toronto|EST5EDT|
| CYQX |Newfoundland and Labrador Weather Office|centre de prévision des intempéries de Terre-Neuve-et-Labrador|NLWO|CPITNL|Gander|NST3:30NDT|
| CWAO |Canadian Meteorological Centre|Centre météorologique canadien|CMC|CMC|Montréal|EST5EDT|
| CWIS |Canadian Ice Service|Service canadien des glaces|CIS|SCG|Ottawa|EST5EDT|
| CWHX |Atlantic Storm Prediction Centre|centre de prévision des intempéries de la région de l'Atlantique|ASPC|CPIRA|Dartmouth|AST4ADT|

**The above table can be found at the following address : https://wiki.cmc.ec.gc.ca/images/b/b2/Offices_transm_alerts.docx** 

Note2: Not all WATR areas in Canada are configured for tornado warning alerts. 
No WATR areas in Canada are configured for severe thunderstorm warning alerts.

NOTE: ALL HOURS ARE IN UTC.

__The directories have the following nomenclature :__

alerts/cap/YYYYMMDD/EEEE/hh/

where:

* __YYYYMMDD__ : warning transmission day.
* __EEEE__ : 4 letters for the responsible office code except LAND or WATR for tornado warning 
  and severe thunderstorm warning alerts.
* __hh__ : warning transmission hour.

__The filenames have the following nomenclature :__

T_BBBBNN_C_EEEE_YYYYMMDDhh_##########.cap

where:
                                                                                                                       
* __T__ : constant string. Literal specification from WMO-386 manual as a prefix for this file 
  naming convention.                                                                               
* __BBBBNN (for tornado and severe thunderstorm alerts)__ : 4 letters and 2 numbers representing 
  the 2 letter province or water body code, the 2 letter country code CN (from the WMO list), and a 2 digit 
  numeric code set to 00 to satisfy the format of the existing filename structure. Ex: ABCN00.
  BBBBNN (for all other alerts): 4 letters and 2 numbers representing the traditional WMO bulletin 
  header used for the alert bulletin on the WMO transmission circuits. Ex: WWCN11.

In the case of the 2 letter province or water body codes, the list of provincial or territorial codes includes: 

* BC – British Columbia
* AB - Alberta
* SK - Saskatchewan
* MB - Manitoba
* ON – Ontario
* QC - Quebec
* YT - Yukon
* NU - Nunavut
* NT - Northwest Territories
* NS – Nova Scotia
* NB – New Brunswick
* PE – Prince Edward Island
* NL – Newfoundland and Labrador
* GL - Great Lakes
* PC - Pacific Waters
* AT - Atlantic Waters
* AC - Arctic Waters
                                                                                        
* __C__ : constant string. Specified by the WMO, as a prefix for the CCCC group.                                                        
* __EEEE__ : 4 letters for the responsible office code (CWAO, CWTO, etc.). The exception is 
  for tornado warning and severe thunderstorm warning alerts where the 4 letters are 
  either LAND or WATR rather than responsible office.                                                              
* __YYYYMMDDhhmm__ : warning transmission date/time (UTC).
* __##########__ : the 10 numeric digit CAP message identifier found in the CAP file

## Support

If you have any questions about these data, please contact us at: ec.dps-client.ec@canada.ca

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).



