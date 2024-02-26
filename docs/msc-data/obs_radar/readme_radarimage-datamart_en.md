[En français](readme_radarimage-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [Radar imagery](readme_radar_en.md) > Radar imagery on MSC Datamart

# Radar imagery

This page describes the [weather radar](readme_radar_en.md) imagery available in GIF format via the MSC Datamart.

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available via the HTTPS protocol. It is possible to access it with a standard browser. In this case, we obtain a list of links giving access to a GIF file.

The radar images are available at the following address:

[https://dd.weather.gc.ca/radar/{PRODUCT}/{FORMAT}/{RADAR_STATION}](https://dd.weather.gc.ca/radar/)

where:

* PRODUCT = [24_HR_ACCUM | CAPPI | DPQPE | PRECIPET]
* FORMAT = [GIF] 
* STATION_RADAR = [CASBV, CASRA ...]  radar 5 letter identifier code in capital letters. 

The past 48 hours of data is available in each directory.

__Notes__: 

* Details about these products can be found on the Environment and Climate Change Canada's [About radar](https://www.ec.gc.ca/meteo-weather/default.asp?lang=En&n=2B931828-1) page.
* The Dual Polarization Quantitative Precipitation Estimation (DPQPE) product is a two-dimensional representation of radar estimated precipitation rate at the lowest sweep of the radar scan (0.4 degrees elevation for the majority of the S-Band radars). So, the estimated precipitation rate is as close as possible to the earth’s surface. DPQPE product is based, among others, on a series of dual-pol processing steps (quality control) to remove, non-weather artifacts from the raw data (volume scans). It is provided in mm/hr for rainfall rates and cm/hr for snowfall rates. This product is used in our high-resolution North American radar composite available in [WeatherCan](https://www.canada.ca/en/environment-climate-change/services/weather-general-tools-resources/weathercan.html), the official mobile application of ECCC.
* A [list of radar sites](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_radar/radars_list.pdf) is available. This list will be updated regularly.

## Filename nomenclature

The files have the following nomenclature, with XXXXX, a 5 letter radar identifier in capital letters. 

* __PRECIPET__

Images for regional composites (5 regions of Canada), national composite and individual radars are available. Two intensities scale (8 and 14 colors) are also available for each image. 

Regional composites with 14 and 8 colors intensity scale, respectively:

* YYYMMDDHHmm_YYY_PRECIPET_RAIN_[WT,A11Y].gif 
* YYYMMDDHHmm_YYY_PRECIPET_SNOW_[WT,A11Y].gif 

Where YYY = [ATL, ONT, PNR, PYR, QUE]

ex: 201409201350_ATL_PRECIPET_RAIN_WT.gif

National Composites with 8 colors intensity scale:

* YYYMMDDHHmm_NATIONAL_PRECIPET_[RAIN,SNOW]_A11Y.gif  

ex: 201409201350_NATIONAL_PRECIPET_RAIN_A11Y.gif

Individual radars with 14 colors intensity scale:

* YYYMMDDHHmm_XXXXX_PRECIPET_[RAIN,SNOW].gif 

ex: 201409201400_CASBV_PRECIPET_RAIN.gif

Individual radars with 8 colors intensity scale:

* YYYMMDDHHmm_XXXXX_PRECIPET_RAIN_A11Y.gif 
* YYYMMDDHHmm_XXXXX_PRECIPET_SNOW_A11Y.gif (14 colors for Snow)

ex: 201409201400_CASRA_PRECIPET_SNOW_A11Y.gif

* __CAPPI__

The CAPPI files have the following nomenclature:

* YYYMMDDHHmm_XXXXX_CAPPI_1.0_SNOW.gif
* YYYMMDDHHmm_XXXXX_CAPPI_1.5_RAIN.gif
* YYYMMDDHHmm_XXXXX_CAPPI_1.0_SNOW_A11Y.gif
* YYYMMDDHHmm_XXXXX_CAPPI_1.5_RAIN_A11Y.gif

ex: 200806191550_CASFT_CAPPI_1.5_RAIN.gif

* __DPQPE__

The DPQPE files have the following nomenclature:

* YYYYMMDDTHHmmZ_MSC_Radar-DPQPE_XXXXX_[Rain,Snow].gif

ex: 20201106T1050Z_MSC_Radar-DPQPE_CASBE_Rain.gif

* __Contingency products__

When a Canadian radar site is down, an alternate product is made available for contingency purposes. It is a composite product generated from the available neighbouring radars, which in some cases may include US radars. It is also important to note that for some regions, neighbouring radars may not cover the entire domain of the radar out of service. 
To this end and to help the user identify these non-covered areas, red circles have been added to show the contributing radars in the composite.

These products are identified in the file names by the words "COMP" for contingency products based on PRECIPET, and "Contingency" for contingency products based on DPQPE:

* YYYMMDDHHmm_XXXXX_COMP_PRECIPET_[RAIN,SNOW].gif; YYYMMDDHHmm_XXXXX_COMP_PRECIPET_[RAIN,SNOW]_A11Y.gif
* YYYYMMDDTHHmmZ_MSC_Radar-DPQPE_XXXXX_[Rain,Snow]-Contingency.gif

ex: 201511271400_CASET_COMP_PRECIPET_RAIN.gif; 20240112T1636Z_MSC_Radar-DPQPE_CASET_Snow-Contingency.gif

This composite image can be differentiated from the original radar image, by the inscription "Composite" in the legend on the right of the image.

* __24_HR_ACCUM__ 

Shows the rain accumulation, in mm, over the last 24hr period. This product is available every 6 minutes for S-Band radars.
   
__Based on PRECIPET__

* YYYMMDDHHmm_XXXXX_24_HR_ACCUM_MM.gif

ex: 200806161900_CASMR_24_HR_ACCUM_MM.gif

__Based on DPQPE__
   
* YYYYMMDDTHHmmZ_MSC_Radar-DPQPE-XXXXX_Accum24h.gif

ex: 20201106T1050Z_MSC_Radar-DPQPE-CASBE_Accum24h.gif

## Historical radar images

Historical national, regional and local radar images from the network of radar sites across Canada are available, for free, on the Climate data website at this address:

[https://climate.weather.gc.ca/radar/index_e.html](https://climate.weather.gc.ca/radar/index_e.html)

## Support

If you have any questions about this data, please [contact us](https://weather.gc.ca/mainmenu/contact_us_e.html).

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).