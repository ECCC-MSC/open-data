[En Français](readme_radarimage-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC Open Public Data](../readme_en.md) > Weather forecast files by city

# Radar imagery

This page describes the [radar](readme_radar_en.md) imagery in GIF format, available on the MSC Datamart.

These images are used to feed the public forecast website:

https://meteo.gc.ca/radar/index_e.html

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](.../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](.../../usage/readme_en.md) is also available.

The data is available via the HTTP protocol. It is possible to access it with a standard browser. In this case, we obtain a list of links giving access to a GIF file.

The radar images are available at the address:

http://dd.weather.gc.ca/radar/PRODUCT/FORMAT/RADAR/file name.extension

where:

* PRODUCT  = [24_HR_ACCUM | CAPPI | PRECIPET]
* FORMAT   = [GIF] (other formats may appear in the future)
* RADAR    = [WKR, XAM, ...]  radar 3 letter identifier code in capital letters. For the new S-band radars, a 5-letter ID will be used (see section below)

An history of 48 hours of data is kept in each directory.

__Note__: Details about these products can be found on the Environment and Climate Change Canada web page at:

http://www.ec.gc.ca/meteo-weather/default.asp?lang=En&n=2B931828-1 

## Filename nomenclature

NOTE: ALL HOURS ARE IN UTC.

The files have the following nomenclature, with XXX, a 3 letter radar identifier in capital letters. For the new S-band radars, a 5-letter code is used.

* __PRECIPET__

Images for regional composites (5 regions of Canada) and individual radar are available. Two intensities scale (8 and 14 colors) are also available for each image. 

Composites with 14 colors intensity scale:

*  YYYMMDDHHmm_XXX_PRECIPET_RAIN_WT.gif 
*  YYYMMDDHHmm_XXX_PRECIPET_SNOW_WT.gif 

   ex: 201409201350_ATL_PRECIPET_RAIN_WT.gif

Composites with 8 colors intensity scale:

*  YYYMMDDHHmm_XXX_PRECIPET_RAIN_A11Y.gif 
*  YYYMMDDHHmm_XXX_PRECIPET_SNOW_A11Y.gif 

   ex: 201409201350_ATL_PRECIPET_RAIN_A11Y.gif

Individual radar with 14 colors intensity scale:

*  YYYMMDDHHmm_XXX_PRECIPET_RAIN.gif 
*  YYYMMDDHHmm_XXX_PRECIPET_SNOW.gif (14 colors for Snow)

   ex: 201409201400_XFT_PRECIPET_RAIN.gif

Individual radar with 8 colors intensity scale:

*  YYYMMDDHHmm_XXX_PRECIPET_RAIN_A11Y.gif 
*  YYYMMDDHHmm_XXX_PRECIPET_SNOW_A11Y.gif (14 colors for Snow)

   ex: 201409201400_XFT_PRECIPET_RAIN_A11Y.gif

* __PRECIPET contingency products__

When a Canadian radar site is down, an alternate PRECIPET product is made available for contingency purposes. It is a composite product generated from the available neighbouring radars, which in some cases may include US radars. It is also important to note that for some regions, neighbouring radars may not cover the entire domain of the radar out of service. 
To this end and to help the user identify these non-covered areas, red circles have been added to show the contributing radars in the composite.

This product contains the string "COMP" in its file name, as :

YYYMMDDHHmm_XXX_COMP_PRECIPET_RAIN.gif

ex: 201511271400_XWL_COMP_PRECIPET_RAIN.gif

This composite image can be differentiated from the original radar image, by the inscription "Composite" in the legend on the right of the image.

To learn more about how to use the composite images, you can read the documentation on line:

http://weather.gc.ca/radar/how-to-use_e.html#display

* __CAPPI__

The CAPPI files have the following nomenclature:

*  YYYMMDDHHmm_XXX_CAPPI_1.5_RAIN_AGL.gif
*  YYYMMDDHHmm_XXX_CAPPI_1.0_SNOW_AGL.gif

   ex: 200806191550_WHK_CAPPI_1.5_RAIN_AGL.gif

* __24_HR_ACCUM__ (based on the PRECIPET product)

Shows the rain accumulation, in mm, over the last 24hr period. The product is available every 10 minutes, and for the last 48 hr.
   
*  YYYMMDDHHmm_XXX_24_HR_ACCUM_MM.gif

   ex: 200806161900_WBI_24_HR_ACCUM_MM.gif

## About the new dual-pol S-Band radars

ECCC is in the process of replacing its old C-Band radars with new dual-pol S-Band radars. This radar renewal project extends over several years and the installation of radar is done progressively (For more information, see the Products documentation section below).

The first radar has already been installed in Radisson (Saskatchewan) and some products are already available. Several changes that impact the products/users are planned in this project. Below are the most important:

* Existing products (PRECIPET, CAPPI, …) will remain the same but with better quality 
* The temporal resolution has been improved and the products are going to be available every 6 minutes instead of 10 minutes (impact on the filename)
* The 3-letter radar ID is replaced by a 5-letter ID (example: the current ID C-band Radisson radar is XRA and is replaced by CASRA)
* Some other new products will emerge in the future and be available externally 

What will happen with the availability of these products and the impact on users?

* For a certain period, the product (PRECIPET, CAPPI, …) will be generated with the same 3-letter ID (same filenames) and the same frequency (each 10 minutes). During this period, these products will be pushed in the same directories (ex: http://dd.meteo.gc.ca/radar/PRECIPET/GIF/XRA). It help to manage the transition
* In parallel, we will provide these products with the new 5-letters ID and every 6 minutes in a new directory (ex: http://dd.meteo.gc.ca/radar/PRECIPET/GIF/CASRA )
* Users will be informed as and when new radars are installed and their products are available following the same procedure described above

Example (The Radisson case):

* The 3-lettre ID product every 10 minutes (Temporary) : http://dd.meteo.gc.ca/radar/PRECIPET/GIF/XRA/
* The 5-letter ID products every 6 minutes (Permanently) : http://dd.meteo.gc.ca/radar/PRECIPET/GIF/CASRA

## Support

If you have any questions about these data, please contact us at: ec.dps-client.ec@canada.ca

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).





