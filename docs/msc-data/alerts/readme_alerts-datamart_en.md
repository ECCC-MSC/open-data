[En français](readme_alerts-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [Alerts](readme_alerts_en.md) > Alerts on MSC Datamart

# Weather warning XML data in the format of the Common Alerting Protocol (CAP)

This page describes the [weather warning data in the format of the Common Alerting Protocol (CAP)](readme_alerts_en.md).

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available using the HTTPS protocol and resides in a directory that is plainly accessible to a web browser. Visiting that directory with an interactive browser will yield a raw listing of links, each link being a downloadable XML file.

The __data can be accessed__ at the following URLs:

[https://dd.weather.gc.ca/alerts/cap/{YYYYMMDD}/{EEEE}/{hh}/](https://dd.weather.gc.ca/alerts/cap)

A 30-day history is kept in this directory.

where:

* __YYYYMMDD__: warning transmission day.
* __EEEE__: 4 letters for the responsible office code except LAND or WATR for tornado warning and severe thunderstorm warning alerts.
* __hh__: warning transmission hour.

* The CAP-XML are grouped in a directory tree that is based on the date and the responsible office (see note1) code for the alert. The exception is for tornado warning and severe thunderstorm warning alerts which are grouped based on a LAND or WATR (see note2) designation rather than responsible office. 

* The LAND directory contains the CAP-XML files for all tornado warning and severe thunderstorm warning alerts that are issued over land zones in Canada. 

* The WATR directory contains the CAP-XML files for all tornado warning alerts that are issued over water zones in Canada. 

* Not all WATR areas in Canada are configured for tornado warning alerts. No WATR areas in Canada are configured for severe thunderstorm warning alerts.

A history of 1 month is maintained in this directory.

A __standardized package of GIS (Geographical Information System) based forecast location shapefiles__, for all the forecast locations used in ECCC CAP Messages, are available at the following address:

[https://dd.weather.gc.ca/meteocode/geodata/](https://dd.weather.gc.ca/meteocode/geodata/)

Shapefile packages found there are the same Shapefiles that are used in the operational environment where ECCC warnings are initially generated. The Shapefile packages are versioned in order to track the available packages to the package used in the operational environment at any given time. Beginning with version 5.0.3 of the GIS package, usage dates for the package will be included in the documentation.

## File name nomenclature 

NOTE: ALL HOURS ARE IN UTC.

__The directories have the following nomenclature :__

alerts/cap/YYYYMMDD/

__The filenames have the following nomenclature :__

T_BBBBNN_C_EEEE_YYYYMMDDhh_##########.cap

where:
                                                                                                                       
* T: constant string. Literal specification from WMO-386 manual as a prefix for this file 
  naming convention.                                                                               
* BBBBNN (for tornado and severe thunderstorm alerts): 4 letters and 2 numbers representing the 2 letter province or water body code, the 2 letter country code CN (from the WMO list), and a 2 digit numeric code set to 00 to satisfy the format of the existing filename structure. Ex: ABCN00.
* BBBBNN (for all other alerts): 4 letters and 2 numbers representing the traditional WMO bulletin header used for the alert bulletin on the WMO transmission circuits. Ex: WWCN11.

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
 
* C: constant string. Specified by the WMO, as a prefix for the CCCC group.                                      
* EEEE: 4 letters for the responsible office code (CWAO, CWTO, etc.). The exception is for tornado warning and severe thunderstorm warning alerts where the 4 letters are either LAND or WATR rather than responsible office.                              
* YYYYMMDDhhmm: warning transmission date/time (UTC).
* '##########': the 10 numeric digit CAP message identifier found in the CAP file

**Examples of the filename nomenclature**:

* T_WWCN11_C_CWTO_201608041031_8263481729.cap: WWCN11 alert bulletin type for the responsible office of CWTO - Ontario Storm Prediction Centre. 
  The alert was transmitted on August 4, 2016 at 1031 UTC.

* T_ABCN00_C_LAND_201608041521_0615296639.cap: LAND alert bulletin type for the province of Alberta - AB. The alert type would be either tornado warning or severe thunderstorm warning. 
  The alert was transmitted on August 4, 2016 at 1521 UTC.

* T_QCCN00_C_WATR_201608041521_1920353215.cap: WATR alert bulletin type for the province of Quebec - QC. The alert type would be a tornado warning (severe thunderstorm warnings are not issued over water zones). 
  The alert was transmitted on August 4, 2016 at 1521 UTC.                                                                                   

## Notes

*  The term "responsible" office is used as it is independent of the "issuing" office which sends the alert. Normally, the "responsible" office is also the "issuing" office. However, in contingency situations the "issuing" office can be different. 

* The "Responsible" office is used for routing and distribution purposes (the right message to the right place) and the “issuing” office is used for accounting and performance measurement purposes (who wrote it).

* List of the issuing offices:


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

## Support

If you have any questions about this data, please contact us at: [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).



