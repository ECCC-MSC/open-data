[En français](readme_radarimage-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [Radar imagery](readme_radar_en.md) > Radar imagery on MSC Datamart

# Radar imagery

This page describes the [weather radar](readme_radar_en.md) imagery available in GIF format via the MSC Datamart.

These images are used to feed the weather radar page on ECCC's [public forecast website](https://meteo.gc.ca/radar/index_e.html).

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available via the HTTPS protocol. It is possible to access it with a standard browser. In this case, we obtain a list of links giving access to a GIF file.

The radar images are available at the following address:

[https://dd.weather.gc.ca/radar/{PRODUCT}/{FORMAT}/{RADAR_STATION}](https://dd.weather.gc.ca/radar/)

where:

* PRODUCT = [24_HR_ACCUM | CAPPI | DPQPE | PRECIPET]
* FORMAT = [GIF] (other formats may appear in the future)
* STATION_RADAR = [WKR, XAM, ...]  radar 3 letter identifier code in capital letters. For the new S-band radars, a 5-letter ID will be used (see section below).

The past 48 hours of data is available in each directory.

__Notes__: 

* Details about these products can be found on the Environment and Climate Change Canada's [About radar](https://www.ec.gc.ca/meteo-weather/default.asp?lang=En&n=2B931828-1) page.
* The Dual Polarization Quantitative Precipitation Estimation (DPQPE) product is only available for S-band radars. It is a two-dimensional representation of radar estimated precipitation rate at the lowest sweep of the radar scan (0.4 degrees elevation for the majority of the S-Band radars). So, the estimated precipitation rate is as close as possible to the earth’s surface. DPQPE product is based, among others, on a series of dual-pol processing steps (quality control) to remove, non-weather artifacts from the raw data (volume scans). It is provided in mm/hr for rainfall rates and cm/hr for snowfall rates. This product is used in our high-resolution North American radar composite available in [WeatherCan](https://www.canada.ca/en/environment-climate-change/services/weather-general-tools-resources/weathercan.html), the official mobile application of ECCC.
* A [list of radar sites](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_radar/radars_list.pdf) is available. This list will be updated regularly.

## Filename nomenclature

NOTE: ALL HOURS ARE IN UTC.

The files have the following nomenclature, with XXX, a 3 letter radar identifier in capital letters. For the new S-band radars, a 5-letter code is used.

* __PRECIPET__

Images for regional composites (5 regions of Canada) and individual radar are available. Two intensities scale (8 and 14 colors) are also available for each image. 

Composites with 14 colors intensity scale:

* YYYMMDDHHmm_XXX_PRECIPET_RAIN_WT.gif 
* YYYMMDDHHmm_XXX_PRECIPET_SNOW_WT.gif 

ex: 201409201350_ATL_PRECIPET_RAIN_WT.gif

Composites with 8 colors intensity scale:

* YYYMMDDHHmm_XXX_PRECIPET_RAIN_A11Y.gif 
* YYYMMDDHHmm_XXX_PRECIPET_SNOW_A11Y.gif 

ex: 201409201350_ATL_PRECIPET_RAIN_A11Y.gif

Individual radar with 14 colors intensity scale:

* YYYMMDDHHmm_XXX_PRECIPET_RAIN.gif 
* YYYMMDDHHmm_XXX_PRECIPET_SNOW.gif (14 colors for Snow)

ex: 201409201400_XFT_PRECIPET_RAIN.gif

Individual radar with 8 colors intensity scale:

* YYYMMDDHHmm_XXX_PRECIPET_RAIN_A11Y.gif 
* YYYMMDDHHmm_XXX_PRECIPET_SNOW_A11Y.gif (14 colors for Snow)

ex: 201409201400_XFT_PRECIPET_RAIN_A11Y.gif

* __PRECIPET contingency products__

When a Canadian radar site is down, an alternate PRECIPET product is made available for contingency purposes. It is a composite product generated from the available neighbouring radars, which in some cases may include US radars. It is also important to note that for some regions, neighbouring radars may not cover the entire domain of the radar out of service. 
To this end and to help the user identify these non-covered areas, red circles have been added to show the contributing radars in the composite.

This product contains the string "COMP" in its file name, as:

YYYMMDDHHmm_XXX_COMP_PRECIPET_RAIN.gif

ex: 201511271400_XWL_COMP_PRECIPET_RAIN.gif

This composite image can be differentiated from the original radar image, by the inscription "Composite" in the legend on the right of the image.

To learn more about how to use the composite images, you can read the documentation on line:

[https://weather.gc.ca/radar/how-to-use_e.html#display](https://weather.gc.ca/radar/how-to-use_e.html#display)

* __CAPPI__

The CAPPI files have the following nomenclature:

* YYYMMDDHHmm_XXX_CAPPI_1.5_RAIN_AGL.gif
* YYYMMDDHHmm_XXX_CAPPI_1.0_SNOW_AGL.gif

ex: 200806191550_WHK_CAPPI_1.5_RAIN_AGL.gif

* __DPQPE__

The DPQPE files have the following nomenclature:

* YYYYMMDDTHHmmZ_MSC_Radar-DPQPE_XXXXX_Rain.gif
* YYYYMMDDTHHmmZ_MSC_Radar-DPQPE_XXXXX_Snow.gif

ex: 20201106T1050Z_MSC_Radar-DPQPE_CASBE_Rain.gif

* __24_HR_ACCUM__ 

Shows the rain accumulation, in mm, over the last 24hr period. 

** Based on PRECIPET 

The product is available every 10 minutes, and for the last 48 hr.
   
* YYYMMDDHHmm_XXX_24_HR_ACCUM_MM.gif

ex: 200806161900_WBI_24_HR_ACCUM_MM.gif

** Based on DPQPE

The product is available every 6 minutes, and for the last 48 hr.
   
* YYYYMMDDTHHmmZ_MSC_Radar-DPQPE-Accum24h_XXXXX.gif

ex: 20201106T1050Z_MSC_Radar-DPQPE-Accum24h_CASBE.gif

## About the new dual-pol S-Band radars

ECCC is in the process of replacing its old C-Band radars with new dual-pol S-Band radars. This radar renewal project extends over several years and the installation of radar is done progressively (For more information, see the Products documentation section below).

The first radar has already been installed in Radisson (Saskatchewan) and some products are already available. Several changes that impact the products/users are planned in this project. Below are the most important:

* Existing products (PRECIPET, CAPPI, …) will remain the same but with better quality.
* The temporal resolution has been improved and the products are going to be available every 6 minutes instead of 10 minutes (impact on the filename).
* The 3-letter radar ID is replaced by a 5-letter ID (example: the current ID C-band Radisson radar is XRA and is replaced by CASRA).
* Some other new products will emerge in the future and be available externally.

What will happen with the availability of these products and the impact on users?

* For a certain period, the product (PRECIPET, CAPPI, …) will be generated with the same 3-letter ID (same filenames) and the same frequency (each 10 minutes). During this period, these products will be pushed in the same directories (ex: [https://dd.meteo.gc.ca/radar/PRECIPET/GIF/XRA](https://dd.meteo.gc.ca/radar/PRECIPET/GIF/XRA)). It help to manage the transition.
* In parallel, we will provide these products with the new 5-letters ID and every 6 minutes in a new directory (ex: [https://dd.meteo.gc.ca/radar/PRECIPET/GIF/XRA/](https://dd.meteo.gc.ca/radar/PRECIPET/GIF/XRA/)).
* Users will be informed as and when new radars are installed and their products are available following the same procedure described above.

Example (the Radisson case):

* __The 3-lettre ID product every 10 minutes (Temporary)__ : [https://dd.meteo.gc.ca/radar/PRECIPET/GIF/XRA/](https://dd.meteo.gc.ca/radar/PRECIPET/GIF/XRA/)
* __The 5-letter ID products every 6 minutes (Permanently)__ : [https://dd.meteo.gc.ca/radar/PRECIPET/GIF/CASRA](https://dd.meteo.gc.ca/radar/PRECIPET/GIF/XRA/)

## Historical radar images

Historical national, regional and local radar images from the network of radar sites across Canada are available, for free, on the Climate data website at this address:

[https://climate.weather.gc.ca/radar/index_e.html](https://climate.weather.gc.ca/radar/index_e.html)

## Support

If you have any questions about this data, please contact us at: [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).