[In French](readme_thunderstorm-outlooks_datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_en.md) > [MSC Data](../readme_en.md) > [Thunderstorm Outlooks](readme_thunderstorm-outlooks_en.md) > Thunderstorm outlooks on MSC Datamart

# Thunderstorm outlooks data 

This page describes the [thunderstorm outlooks](readme_thunderstorm-outlooks_en.md) data in GeoJSON format available on the MSC Datamart.

## Data address 

MSC testing data repository DD-Alpha data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../.../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples of how to access and use Meteorological Service of Canada open data](../../usage/readme_en.md) is also available.

The data is available via the HTTPS protocol. It can be accessed using a standard browser. In this case, a list of links to a GeoJSON file is displayed.

Thunderstorm outlooks data can be found at :

[https://dd.alpha.weather.gc.ca/thunderstorm-outlooks/](https://dd.alpha.weather.gc.ca/thunderstorm-outlooks)

## File name nomenclature 

File names follow the nomenclature below:

`{YYYYYMMDD}T{HHmm}Z_MSC_ThunderstormOutlook_{SPC-Code}_{coverage-code}_{PTxxxH}_{version-id}.json`

where :

* __YYYYMMDD__ : Year, month and day of data transmission
* __T__: Time delimiter according to ISO8601 standards
* __HHmm__: Hour and minute at which data is transmitted
* __Z__: Time zone (UTC hour)
* __MSC__: Constant character string for Meteorological Service of Canada, the data source
* __ThunderstormOutlook__ : Constant string indicating the name of the product contained in the files, i.e. thunderstorm outlook
* __SPC-code__: Identifier of the Storm Prediction Center responsible for issuing and distributing the product [ASPC, NLWO, OSPC, PASPC, PSPC, QSPC]. See list of issuing offices below
* __coverage-code__: Region covered for the coastal flooding risk index. See list of regions covered for each issuing office below
* __PTxxxH__ : Validity time 
     * __PTxxxHxxM__: Validity time with minutes 
     * NOTE: the filename can use either {PTxxxH} or {PTxxxHxxM}, at the discretion of the data provider
* __version-id__ : 
     * v1 for the original version
     * v2 for the new version after an amendment, v3 for another amendment, v4 and so on.
* __json__: Constant string indicating that the format is GeoJSON.

Example:

*  20240627T1900Z_MSC_ThunderstormOutlook_PASPC_PRAIRIES_PT036H00M_v1.json

**Notes**:

* Thunderstorm outlooks are issued by storm prediction centres across Canada once per day at around 12:00 pm regional local time during the convective season each year. 

* Forecasters may choose from four time periods for which the thunderstorm outlook is valid:

     * Day 1 (PM) – Valid from 12pm to 12am on the same day it was issued. 
     * Day 2 (AM) – Valid from 12am to 12pm on the day after it was issued. 
     * Day 2 (PM) – Valid from 12pm to 12am on the day after it was issued. 
     * Day 3 (full day) – Valid from 12am to 12am two days after it was issued. 

* The forecaster could provide information for more than one time period by creating separate thunderstorm outlooks for each time period. 

* Subsequent amendments to existing thunderstorm outlooks are issued on an as-needed basis during the day. The Thunderstorm outlook may not be updated with active severe weather alerts. Users are asked to check with the latest watches and warnings for the most current conditions.

* Files may be generated containing no information in the absence of thunderstorm outlook.

### List of issuing offices and regions covered:

| SPC-code | Name of issuing office | coverage-code | Region covered |
| ------ | ------ | ------ | ------ |
| ASPC | Atlantic Storm Prediction Center | ATLANTIC | Atlantic |
| OSPC | Ontario Storm Prediction Centre | ON | Ontario |
| PASPC | Prairie and Arctic Storm Prediction Centre | PRAIRIES | Prairies |
| PASPC | Prairie and Arctic Storm Prediction Centre | MK | Mackenzie river |
| PSPC | Pacific and Yukon Storm Prediction Centre | BC-YT | British Columbia and Yukon Territory |
| QSPC | Quebec Storm Prediction Centre | QC | Quebec |

## Support

If you have any questions about this data, please [contact us](https://weather.gc.ca/mainmenu/contact_us_f.html).

## dd_info mailing list announcements 

Announcements related to this dataset are available via the [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/) list.
