[En Français](readme_meteocode-datamartxml_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [Meteocode forecast data](readme_meteocode_en.md) > Meteocode forecast data on MSC Datamart

# Meteocode forecast data in XML format

This page describes the markup language files Canadian Meteorological Service (CMML) on the MSC Datamart. The CMML is an XML format containing Environment and Climate Change Canada's official forecasts, interpolated by hour.

# Data address 

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available via the HTTP protocol. It is possible to access it with a standard browser. In this case, we obtain a list of links giving access to a XML file.

The data is available at the following address : 
                                                                          
[https://dd.weather.gc.ca/meteocode/REGION/cmml/ ](https://dd.weather.gc.ca/meteocode/REGION/cmml/)

where 'REGION' is one of the following value :

* atl
* ont
* pnr
* pyr
* que

A data history of one month is kept in these directories.

The [CMML format specifications](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/meteocode/cmml_specification_en-v3.04.pdf) are available.

Public forecast regions are precisely defined and can be found in a geo-referenced file in Shapefile format.

These files can be found here :

[https://dd.weather.gc.ca/meteocode/geodata/](https://dd.weather.gc.ca/meteocode/geodata/)

## File name nomenclature 

NOTE: ALL HOURS ARE IN UTC.

The forecast emitted for each provinces and territories is located in a specific directory :
* __atl__ : New Brunswick, Nova Scotia, Prince Edward Island, Newfoundland and Labrador
* __ont__ : Ontario
* __pnr__ : Alberta, Saskatchewan, Manitoba, Northwest Territories, Nunavut
* __pyr__ : British Columbia, Yukon
* __que__ : Québec


The filenames follow the convention :

TRANSMIT.FP[A-Z][A-Z][0-9][0-9].MM.DD.HHmmZ[.AMD].xml

where :

* MM.DD.HHmm is the date of emission of the bulletin
* Z is a constant indicating that the time zone of the forecast is
      in UTC.
* __AMD__ : Optionnal. If present, this forecast is an amendement to the previous forecast for this region.
* **FP[A-Z][A-Z][0-9][0-9]** describes the forecast region and period :
    * __New Brunswick ('atl')__
	    * Day 1 and 2 :
	        * FPHX14 : New Brunswick 
	    * Day 3 to 5 :
	        * FPHX54 : New Brunswick 
    * __Nova Scotia ('atl')__
	    * Day 1 and 2 :
	        * FPHX11 : Nova Scotia
	    * Day 3 to 5 :
	        * FPHX51 : Nova Scotia
    * __Prince Edward Island ('atl')__
	    * Day 1 and 2 :
	        * FPHX15 : Prince Edward Island
	    * Day 3 to 5 :
	        * FPHX55 : Prince Edward Island
    * __Newfoundland and Labrador ('atl')__
	    * Day 1 and 2 :
	        * FPHX16 : Newfoundland
	        * FPHX17 : Labrador
	    * Day 3 to 5 :
	        * FPHX56 : Newfoundland
	        * FPHX57 : Labrador
    * __Ontario ('ont')__
	    * Day 1 and 2 :
	        * FPTO11 : Southern Ontario and the National Capital Region
	        * FPTO12 : Northern Ontario
	        * FPTO13 : Far Northern Ontario
	    * Day 3 to 5 :
	        * FPTO51 : Southern Ontario and the National Capital Region
	        * FPTO52 : Northern Ontario
	        * FPTO53 : Far Northern Ontario
    * __Alberta ('pnr')__
	    * Day 1 and 2 :
	        * FPWG15 : Southern Alberta and the mountain parks
	        * FPWG16 : Central and northern Alberta
	    * Day 3 to 5 :
	        * FPWG53 : Southern Alberta and the mountain parks
	        * FPWG54 : Central and northern Alberta
    * __Saskatchewan ('pnr')__
	    * Day 1 and 2 :
	        * FPWG13 : Southern Saskatchewan
	        * FPWG14 : Northern Saskatchewan
	    * Day 3 to 5 :
	        * FPWG52 : Saskatchewan
    * __Manitoba ('pnr')__
	    * Day 1 and 2 :
	        * FPWG11 : Southern Manitoba
	        * FPWG12 : Central and Northern Manitoba
	    * Day 3 to 5 :
	        * FPWG52 : Saskatchewan
    * __Northwest Territories ('pnr')__
	    * Day 1 and 2 :
	        * FPNT11 : Great Slave Lake and Mackenzie River Areas
	        * FPNT12 : Mackenzie Delta and Arctic Coast
	    * Day 3 to 5 :
	        * FPNT51 : Great Slave Lake and Mackenzie River Areas
	        * FPNT52 : Mackenzie Delta and Arctic Coast
    * __Nunavut ('pnr')__
	    * Day 1 and 2 :
	        * FPNT13 : Kivalliq
	        * FPNT14 : Kitikmeot
	        * FPNT15 : High Arctic
	        * FPNT16 : Qikiqtaaluk
	    * Day 3 to 5 :
	        * FPNT53 : Kivalliq
	        * FPNT54 : Kitikmeot
	        * FPNT55 : High Arctic
	        * FPNT56 : Qikiqtaaluk
    * __British Columbia ('pyr')__
	    * Day 1 and 2 :
	        * FPVR11 : Coastal - South 
	        * FPVR12 : Coastal - Central and North
	        * FPVR13 : Southwest interior 
	        * FPVR14 : Columbia districts
	        * FPVR15 : Kootenay districts
	        * FPVR16 : Central interior
	        * FPVR17 : Southeast Yukon and Northern British Columbia
	        * FPVR18 : Peace river district
	        * FPVR19 : Western Yukon and northwestern British Columbia
	    * Day 3 to 5 :
	        * FPVR50 : Coastal British Columbia
	        * FPVR52 : Southwest and central interior
	        * FPVR54 : Columbia and Kootenay districts
	        * FPVR56 : Peace River district
	        * FPVR58 : Yukon and northern British Columbia
    * __Yukon ('pyr')__
	    * Day 1 and 2 :
	        * FPVR17 : Southeast Yukon and Northern British Columbia
	        * FPVR19 : Western Yukon and northwestern British Columbia
	    * Day 3 to 5 :
	        * FPVR58 : Yukon and northern British Columbia
    * __Québec ('que')__
	    * Day 1 and 2 :
	        * FPCN71 : Western Québec
	        * FPCN72 : Northern Québec
	        * FPCN73 : Central Québec
	        * FPCN74 : Eastern Québec
	        * FPCN75 : Extreme northern Québec
        * Day 3 to 5 :
            * FPUL55 : Western Québec
	        * FPXK55 : Eastern Québec
	        * FPQB55 : Central and Northern Québec
	        * FPQB57 : Extreme northern Québec


__Note__ : The year of the forecast is not included in the file name.


File name example :

[https://dd.weather.gc.ca/meteocode/pyr/cmml/TRANSMIT.FPVR11.10.30.2300Z.xml](https://dd.weather.gc.ca/meteocode/pyr/cmml/TRANSMIT.FPVR11.10.30.2300Z.xml)

This file contains the forecast emitted by the Vancouver office (directory 'pyr' and 'VR' in the file name) in English language for day 1 and 2 ('11') starting at 2300 UTC on October 30th ('10.30.2300Z') in CMML format ('.xml').

## Support

If you have any questions about these data, please contact us at: ec.dps-client.ec@canada.ca

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).











