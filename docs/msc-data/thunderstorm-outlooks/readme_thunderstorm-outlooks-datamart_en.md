[In French](readme_thunderstorm-outlooks_datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_en.md) > [MSC Data](../readme_en.md) > [thunderstorm-outlooks](readme_thunderstorm-outlooks_en.md) > Thunderstorm outlooks on MSC Datamart

# Thunderstorm outlooks data 

This page describes the [thunderstorm outlooks](readme_thunderstorm-outlooks_en.md) data in GeoJSON format available on the MSC Datamart.

## Data address 

MSC testing data repository DD-Alpha data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../.../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples of how to access and use Meteorological Service of Canada open data](../../usage/readme_en.md) is also available.

The data is available via the HTTPS protocol. It can be accessed using a standard browser. In this case, a list of links to a GeoJSON file is displayed.

Thunderstorm outlooks data can be found at :

[https://dd.alpha.weather.gc.ca/thunderstorm-outlooks/](https://dd.alpha.weather.gc.ca/thunderstorm-outlooks)

A 7-day history is kept in this directory.

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
* __SPC-code__: Identifier of the Storm Prediction Center responsible for issuing and distributing the product [aspc, nlwo, ospc, paspc, pspc, qspc]. See list of issuing offices below
* __coverage-code__: Region covered for the coastal flooding risk index. See list of regions covered for each issuing office below
* __PTxxxH__ : Validity time 
     * __PTxxxHxxM__: Validity time with minutes 
     * NOTE: the filename can use either {PTxxxH} or {PTxxxHxxM}, at the discretion of the data provider
* __version-id__ : 
     * v1 for the original version
     * v2 for the new version after an amendment, v3 for another amendment, v4 and so on.
* __json__: Constant string indicating that the format is GeoJSON.

Example:

* 20240410T2200Z_MSC_ThunderstormOutlook_pspc_bc-yt_PT014H00M_v1.json

Note:

* Data is generated once per day and is valid for the next 24 hours, namely data is valid from 12UTC that day to 12Z the next day.

### List of issuing offices and regions covered:

| SPC-code | Name of issuing office | coverage-code | Region covered |
| ------ | ------ | ------ | ------ |
| aspc | Atlantic Storm Prediction Center | aspc | Atlantic |
| aspc | Atlantic Storm Prediction Centre | aspc-magdalen | Magdalen Island |
| aspc | Atlantic Storm Prediction Centre | aspc-nb | New Brunswick |
| aspc | Atlantic Storm Prediction Centre | aspc-ns | Nova Scotia |
| aspc | Atlantic Storm Prediction Centre | aspc-pei | Prince Edward Island |
| nlwo | Newfoundland and Labrador Weather Office | nlwo | Newfoundland and Labrador |
| ospc | Ontario Storm Prediction Centre | ospc | Ontario |
| ospc | Ontario Storm Prediction Centre | ospc-n | Northern Ontario |
| paspc | Prairie and Arctic Storm Prediction Centre | paspc | Arctic and Manitoba |
| paspc | Prairie and Arctic Storm Prediction Centre | paspc-baffin | Baffin Island |
| paspc | Prairie and Arctic Storm Prediction Centre | paspc-qujuqtaaluk | Northern Baffin |
| paspc | Prairie and Arctic Storm Prediction Centre | paspc-higharctic | High Arctic |
| paspc | Prairie and Arctic Storm Prediction Centre | paspc-kitikmeot | Nunavut Administrative Region (*) |
| paspc | Prairie and Arctic Storm Prediction Centre | paspc-kivalliq | Nunavut Administrative Region (**) |
| paspc | Prairie and Arctic Storm Prediction Centre | paspc-mb | Manitoba |
| paspc | Prairie and Arctic Storm Prediction Centre | paspc-nwt | Northwest Territories |
| paspc | Prairie and Arctic Storm Prediction Centre | paspc-yt | Yukon Territory |
| pspc | Pacific and Yukon Storm Prediction Centre | pspc | British Columbia |
| pspc | Pacific and Yukon Storm Prediction Centre | pspc-n | Northern British Columbia |
| pspc | Pacific and Yukon Storm Prediction Centre | pspc-s | Southern British Columbia |
| qspc | Quebec Storm Prediction Centre | qspc | Quebec |
| qspc | Quebec Storm Prediction Centre | qspc-n | Northern Quebec |
| qspc | Quebec Storm Prediction Centre | qspc-s | Southern Quebec |

(*) The Kitikmeot region includes the southern and eastern parts of Victoria Island and the adjacent mainland to the Boothia Peninsula, as well as King William Island and the southern part of Prince of Wales Island.

(**) The Kivalliq region includes the part of the continent west of Hudson Bay, as well as Southampton Island and Coats Island.

## Support

If you have any questions about this data, please [contact us](https://weather.gc.ca/mainmenu/contact_us_f.html).

## dd_info mailing list announcements 

Announcements related to this dataset are available via the [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/) list.
