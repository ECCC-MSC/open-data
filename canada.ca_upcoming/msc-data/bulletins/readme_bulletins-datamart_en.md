[En Français](readme_bulletins-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC Open Public Data](../readme_en.md) > Alphanumerical bulletins

# Data of the alphanumerical bulletins 

This page describes the data of the [alphanumerical bulletins](readme_bulletins_en.md).

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage-overview/readme_en.md) is also available.

The data is available via the HTTP protocol. It is possible to access it with a standard browser. 

The bulletin files are available at the following address :

* [https://dd.weather.gc.ca/bulletins/alphanumeric/](https://dd.weather.gc.ca/bulletins/alphanumeric/)

A short history of data is kept in the directory.

## Directory and file name nomenclature 

NOTE: ALL HOURS ARE IN UTC.

The bulletins are grouped in a directory tree that is based on the date
and on the type of bulletin.
The directories have the following nomenclature :

YYYYMMDD/AA/BBBB/HH

where :
* __YYYYMMDD__ : Reception date of the bulletin (warning: not the date of issue!)
* __AA__ : 2 letters indicating the type of bulletin. The complete reference of 
the different types can be found in the WMO's Manual on the Global
Telecommunication System, in the section 'Attachment II-5' that
corresponds to the pages 103-108. The file is online here:
http://www.wmo.int/pages/prog/www/ois/Operational_Information/Publications/WMO_386/WMO_386_Vol_I_2009_en.pdf
See the following section for specific details about Warning bulletins. 
* __BBBB__ : 4 letter identifier of the bulletin issuer. Usually an 

The 2 letters after "CW" or "CY" in the directory name indicates the issuing office :
    * QX = Gander, (N.F.) 
    * HX = Halifax (now Dartmouth)  
    * UL = Montréal  
    * QB = Québec 
    * XK = Rimouski  
    * TO = Toronto  
    * WG = Winnipeg  
    * NT = North West Territory  
    * VR = Vancouver  
    * CN = Canada  
    * US = United States 
* __HH__ : The hour of the reception of the bulletin

The filenames have the following nomenclature :

BULLETIN_REGION_CODE1__CODE2

Example :

SOVD02_CWOW_250553___14352

A complete listing of all bulletins posted on the MSC Datamart is not available. 
However, once you know which ones you are looking for after consulting the WMO documents, 
then you can easily checked if they are on our http server using the [bulletin search script](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/bulletins/CMC_Bulletin_Search_Help_en.pdf).

### Weather Warnings

The specific 2 letter codes for the Warnings refer to :
* __WA__ : Airmet
* __WC__ : Cyclone
* __WE__ : Tsunami
* __WF__ : Tornado
* __WH__ : Flood
* __WL__ : Smog
* __WO__ : Special
* __WO__ : Hurricane
* __WP__ : Weather
* __WS__ : SIGMET
* __WT__ : Tropical
* __WU__ : Thunderstorm
* __WV__ : Volcano
* __WW__ : Weather

An example of Weather Warning received on June 9th 2010 at 07 UTC by the 
Halifax office is :

[https://dd.weatheroffice.gc.ca/bulletins/alphanumeric/20100609/WW/CWHX/07/WWCN14_CWHX_090744___64416](https://dd.weatheroffice.gc.ca/bulletins/alphanumeric/20100609/WW/CWHX/07/WWCN14_CWHX_090744___64416)

## Support

If you have any questions about these data, please contact us at: ec.dps-client.ec@canada.ca

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).

