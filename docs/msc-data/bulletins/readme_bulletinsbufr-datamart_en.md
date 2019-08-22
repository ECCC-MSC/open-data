[En français](readme_bulletinsbufr-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [Binary bulletins](readme_bulletins_en.md) > Binary bulletins on MSC Datamart

# Data of the binary bulletins 

This page describes the data of the binary [bulletins](readme_bulletins_en.md).

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available via the HTTP protocol. It is possible to access it with a standard browser. 

The data can be accessed at the following URLs :

* https://dd.weather.gc.ca/bulletins/alphanumeric/YYYYMMDD/IO

* https://dd.weather.gc.ca/bulletins/alphanumeric/YYYYMMDD/IU

where :

__YYYYMMDD__ : Date of the BUFR bulletin emission in UTC

As other alphanumeric bulletins, the retention period is 6 months.

__Note__: In the context of the migration from alphanumeric to BUFR format, binary bulletins are available in the same directory than alphanumeric ones.

## File name nomenclature 

NOTE : ALL HOURS ARE IN UTC.

File  names have the form :

IUnB0x_Ciii_DDHHHH__BUFR

where :

    * __n__ : Bulletin type identifier. 
    * __x__ : Location grid identifier 
    * __iii__ : Transport Canada station ID
    * __DD__ : Date of bulletin
    * __HHHH__ : Standard hour of bulletin

Example :

IUKB02_CWLT_130000__BUFR

## File content

These bulletins are part of the world-wide exchange of radiosonde data undertaken under the auspices of the World Meteorological Organization (WMO).
This radiosonde data is collected and formatted in accordance with standards managed by the WMO at the behest of its members. The data is formatted 
using the BUFR Edition 4 code form (FM94), specified in the WMO Manual on Codes (WMO-No. 306), Volume I.2 
[(http://www.wmo.int/pages/prog/www/WMOCodes/WMO306_vI2/VolumeI.2.html)](https://www.wmo.int/pages/prog/www/WMOCodes/WMO306_vI2/VolumeI.2.html).
  
The specific template and BUFR encoding rules used in the encoding of this data are detailed in the B/C25 regulations: 
[https://www.wmo.int/pages/prog/www/WMOCodes/WMO306_vI2/LatestVERSION/BC25-TEMP.pdf](https://www.wmo.int/pages/prog/www/WMOCodes/WMO306_vI2/LatestVERSION/BC25-TEMP.pdf)
[https://www.wmo.int/pages/prog/www/WMOCodes/WMO306_vI2/LatestVERSION/BC20-PILOT.pdf](https://www.wmo.int/pages/prog/www/WMOCodes/WMO306_vI2/LatestVERSION/BC20-PILOT.pdf)

This data is in binary form and requires BUFR compliant software to be processed for viewing or decoding into ASCII or other formats. Several major 
meteorological centers and meteorological research establishments make BUFR software available under free licenses. 
The MSC provides libECBUFR, a BUFR library with user tools for decoding or encoding BUFR to and from ASCII : https://launchpad.net/libecbufr
Once libECBUFR is correctly installed, the following command line (under Unix/Linux/OSX) will provide a human-readable dump of the BUFR TEMP data: 
bufr_decoder -inbufr data.bufr 
where data.bufr is a BUFR file.

Much useful information on installing and running libECBUFR is available in the FAQ list located at: 
[https://answers.launchpad.net/libecbufr/+faqs](https://answers.launchpad.net/libecbufr/+faqs)

## Bulletin search script

To help you in your search, please refer to our bulletin search script which is available directly on the Datamart at:
[https://dd.weather.gc.ca/cgi-bin/bulletin_search.pl](https://dd.weather.gc.ca/cgi-bin/bulletin_search.pl)

Complete documentation with examples of use of the script can be found in the [PDF document](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/bulletins/CMC_Bulletin_Search_Help_en.pdf).

## Support

If you have any questions about these data, please contact us at : ec.dps-client.ec@canada.ca

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).

