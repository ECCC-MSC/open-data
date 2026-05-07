[In French](readme_aviation-iwxxm-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [MSC Data](../readme_fr.md) > [Aviation Weather Data](readme_aviation-iwxxm_en.md) > Aviation Weather Data in IWXXM Format on the MSC Datamart

# Aviation Weather Data in IWXXM Format

This page describes specialized aviation bulletins distributed in the [IWXXM format](https://community. wmo.int/iwxxm), an ICAO meteorological information exchange model introduced in November 2013 by Amendment 76 to ICAO Annex 3, allowing States to exchange their OPMET (Expert Group on Operational Meteorology) not only in TAC (traditional alphanumeric code) format but also in Extensible Markup Language (XML) and, more specifically, in Geographic Markup Language (GML).

IWXXM information exchange became a recommendation through Amendment 77 to ICAO Annex 3 in November 2016 and a standard in November 2020, as specified in Amendment 78 to ICAO Annex 3.

This page describes both the [aviation meteorological data in IWXXM format](readme_aviation-iwxxm_en.md) available on the MSC Datamart and the schema used to encode Canada-specific data.

## Data Address 

Data from the MSC Datamart can be [automatically retrieved using the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_fr.md) as soon as it becomes available. An [overview and examples for accessing and using the Meteorological Service of Canada’s open data](../../usage/readme_fr.md) is also available.

The data is available via the HTTPS protocol. It can be accessed using a standard web browser. In this case, a list of links providing access to an XML file is displayed.

Meteorological data in IWXXM format, as well as the schema associated with [Canadian data specifics](https://dd.meteo.gc.ca/today/aviation/iwxxm/code-ca/), can be found respectively at:

* [https://dd.weather.gc.ca/today/aviation/iwxxm/{product}/{code_issuer}/{HH}](https://dd.weather.gc.ca/today/aviation/iwxxm)
* [https://dd.weather.gc.ca/today/aviation/iwxxm/schema](https://dd.weather.gc.ca/today/aviation/iwxxm/schema)

With:

* __product__: Weather product (see list below)
* __code_issuer__: International code of issuing offices (see list below)
* __HH__: Time of data issuance

#### Product descriptions

* __vaa__:
* __qvaci__:
* __taf__:
* __metar__:
* __speci__:
* __airmet__:
* __sigmet__:

#### List of Issuing Offices

| Code | Issuing Office Name | City | Time Zone Code |
|-------------|---------------------------|--------------------- -|-------------------------|
| cwao | Canadian Meteorological Centre | Montreal | EST5EDT |
| | | | |
| | | | |

... _To be completed via https://eccc-msc.github.io/open-data/msc-data/alerts/readme_alerts-datamart_en/#notes ??_


## File naming convention 

File names follow the convention below:

`A_{TTAAiiCCCCYYGGggBBB}_C_{CCC}_{YYYYMMddhhmmss}.xml`

where:

* __A__: Permanent constant string
* __TTAAiiCCCCYYGGgg__: Current WMO header with date and time group
* __HHmm__: Hour and minute at which the data is transmitted
* __BBB__: Optional character string
* __C__: Permanent constant character string
* __CCC__: Identifier of the `TTAAiiCCCC` element that is repeated
* __YYYYMMddhhmmss__: Date and time group
* __xml__: File extension (XML format)

Example:

* A_LTCN33CWAO102300RRA_C_CWAO_20260210230000.xml

Notes:

* Data is generated X times per day (??) and is valid for the next 24 hours (??). More specifically, the data is valid from ??
* _Information on Canadian code text files: https://dd.weather.gc.ca/today/aviation/iwxxm/code-ca ???_

## Support

If you have any questions about this data, please [contact us](https://weather.gc.ca/mainmenu/contact_us_f.html).

## dd_info mailing list announcements 

Announcements related to this dataset are available via the [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/) list.

