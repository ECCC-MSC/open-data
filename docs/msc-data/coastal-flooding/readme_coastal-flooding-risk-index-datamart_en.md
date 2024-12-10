[In French](readme_coastal-flooding-risk-index-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_en.md) > [MSC Data](../readme_en.md) > [Coastal Flooding](readme_coastal-flooding_en.md) > Coastal Flooding Risk Index on MSC Datamart

# Coastal flooding risk index data 

This page describes the [coastal flooding](readme_coastal-flooding_en.md) risk index data in GeoJSON format available on the MSC Datamart.

## Data address 

MSC testing data repository DD-Alpha data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../.../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples of how to access and use Meteorological Service of Canada open data](../../usage/readme_en.md) is also available.

The data is available via the HTTPS protocol. It can be accessed using a standard browser. In this case, a list of links to a GeoJSON file is displayed.

Coastal flooding risk index data can be found at :

[https://dd.alpha.weather.gc.ca/coastal-flooding/risk-index/](https://dd.alpha.weather.gc.ca/coastal-flooding/risk-index)

## File name nomenclature 

File names follow the nomenclature below:

`{YYYYYMMDD}T{HHmm}Z_MSC_CoastalFloodRiskIndex_{SPC-Code}_{coverage-code}_{PTxxxH}_{version-id}.json`

where :

* __YYYYMMDD__ : Year, month and day of data transmission
* __T__: Time delimiter according to ISO8601 standards
* __HHmm__: Hour and minute at which data is transmitted
* __Z__: Time zone (UTC hour)
* __MSC__: Constant character string for Meteorological Service of Canada, the data source
* __CoastalFloodRiskIndex__ : Constant string indicating the name of the product contained in the files, i.e. the coastal flooding risk index.
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

* 20240410T2200Z_MSC_CoastalFloodRiskIndex_aspc_atlantic_PT014H00M_v1.json

Notes:

* Data is generated once per day and is valid for the next 24 hours, namely data is valid from 12UTC that day to 12Z the next day.

* Files may be generated containing no information in the absence of coastal flooding risk.

### List of issuing offices and regions covered:

| SPC-code | Name of issuing office | coverage-code | Region covered |
| ------ | ------ | ------ | ------ |
| ASPC | Atlantic Storm Prediction Center | ASPC | Canada’s Atlantic coasts (the Maritimes) |
| NLWO | Newfoundland and Labrador Weather Office | NLWO | Newfoundland and Labrador coasts |
| OSPC | Ontario Storm Prediction Centre | OSPC | Great Lakes and Hudson Bay |
| PASPC | Prairie and Arctic Storm Prediction Centre | PASPC | Arctic coasts (including Manitoba and Yukon) |
| PSPC | Pacific and Yukon Storm Prediction Centre | PSPC | Pacific coasts |
| QSPC | Quebec Storm Prediction Centre | QSPC | St. Lawrence (Quebec), Hudson Bay, and Hudson strait |

## Support

If you have any questions about this data, please [contact us](https://weather.gc.ca/mainmenu/contact_us_f.html).

## dd_info mailing list announcements 

Announcements related to this dataset are available via the [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/) list.
