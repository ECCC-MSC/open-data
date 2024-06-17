[En français](readme_satellite-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_en.md) > [MSC Data](../readme_en.md) > [Satellite Observations](readme_satellite_en.md) > Satellite Observations on the MSC Datamart

# Satellite data and products

This page describes data and products derived from GOES-West and GOES-East [satellite](readme_satellite_en.md) instruments in GeoTIFF format available on the MSC Datamart. 

These products are derived from [RGB](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_satellite/what_is_an_rgb_en.pdf) (red/green/blue) images, a satellite processing technique that uses a combination of satellite sensor bands (also called channels) and applies a red/green/blue (RGB) filter to each of them. The result is a false-color image, i.e. an image that does not correspond to what the human eye would see, but offers high contrast between different cloud types and surface features. The on-board sensor of a weather satellite obtains two basic types of information: visible light data (reflected light) reflecting off clouds and different surface types, also known as "reflectance", and infrared data (emitted radiation) which are long-wave radiations emitted by clouds and surface features. RGBs are specially designed to combine this type of satellite data, resulting in an information-rich final product.

Other products are based on the enhancement of channel data for a single wavelength, also aimed at highlighting meteorological features of the observed surface or clouds, but in a simpler way since only a single wavelength is involved. This older approach is still useful today, as its simplicity makes image interpretation easier in some cases.

## Data location 

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](.../.../msc-datamart/amqp_en.md) as soon as it becomes available. An overview and examples of how to access and use Meteorological Service of Canada open data](../../usage/readme_en.md) is also available.

The data is available via the HTTPS protocol. It can be accessed using a standard browser. In this case, a list of links to a GeoTIFF file is displayed.

GOES-R series products can be found at :

* [https://dd.weather.gc.ca/satellite/goes/[west|east]/{HH}/](https://dd.weather.gc.ca/satellite/goes/)

where :

* __HH__: Time in UTC of image validity [00, 01, .., 23]

A 54-hour history of data is stored in each directory.

## File name nomenclature 

File names follow the nomenclature below:

`{YYYYMMDD}T{HHmm}Z_MSC_{GOES-Sat}_{Product}_{resolution}.tif`

where :

* __YYYYMMDD__: Year, month and day of image validity
* __T__: Time delimiter according to ISO8601 standards
* __HHmm__: Hour and minute in UTC of image validity time [00, 01, 02, ...., 22, 23] 
* __Z__: Time zone (UTC time)
* __MSC__: Constant string for Meteorological Service of Canada, the data source
* __GOES-Sat__ : String indicating that data are derived from GOES satellites [GOES-East, GOES-West]
* __Product__: String indicating the type of satellite product generated [Ash, FireTemperature, etc.]. See the section on file contents
* __resolution__ : Horizontal resolution of data [1km, 2km]
* __tif__ : Constant string indicating that the format is GeoTIFF 

Examples: 

* 20231109T0800Z_MSC_GOES-East_NaturalColor_1km.tif
* 20231109T0510Z_MSC_GOES-West_SnowFog-NightMicrophysics_1km.tif

## File contents

It is important to note that products using visible light channels cannot be generated during the hours of the night when no portion of the Earth's disk seen by the satellite is directly illuminated by the sun. These products have a nominal resolution of 1km. Their higher resolution makes the latter products more popular, but when produced individually they are not available during most of the night (between 02UTC and 07UTC for GOES-East, and between 06UTC and 11UTC for GOES-West). On the other hand, products using only infrared channels are generated day and night, and are therefore available 24 hours a day at a nominal resolution of 2km.
 
By combining products using only infrared radiation with products using reflected sunlight, we obtain combined products generated around the clock, where the daytime illuminated part uses visible light channels, and the night-time part uses only infrared radiation channels.
 
Fifteen types of product are currently generated from the GOES-West and GOES-East satellites. They are described below according to the type of individual or combined "day-night" products (see links in tables and list of available combinations) : 

### Individual products : 

| Individual products | Resolution | Application | Note | 
| ------ | ------ | ------ | ------ | 
| [Natural Colour](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_satellite/natural_colour_en.pdf) | 1km | Various applications (e.g. natural appearance of surfaces, tracking smoke from forest fires, warm season) | Only available during the day | 
| [Ash](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_satellite/ash_en.pdf) | 2km | Detection of volcanic ash | Available 24/24 with infrared channels, so visible day and night | 
| [SO2](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_satellite/so2_en.pdf) | 2km | Detection of sulfur dioxide, a volcanic gas that can pose a threat to the environment and human health at high concentrations | Available 24/24 with infrared channels so visible night and day | 
| [Dust](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_satellite/dust_en.pdf) | 2km | Detection of dust clouds and moisture fronts | Available 24/24 with infrared channels so visible night and day |

### Individual or combined "day-night" products:

| Individual or combined "day-night" products | Resolution | Application | Note | 
| ------ | ------ | ------ | ------ | 
| [Day Cloud Convection](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_satellite/day_cloud_convection_en.pdf) | 1km | Creation of contrast between high and low clouds, detection of convective clouds causing thunderstorms | Only available during the day if used in isolation or in "day-night" combination with other products | 
| [Night IR](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_satellite/night_ir_en.pdf) | 2km | Night cloud monitoring, similar appearance to RGB "Day Cloud Convection" | Available 24/24 or in "day-night" combination with other products, with infrared channels so visible night and day | 
| [Night Microphysics](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_satellite/night_microphysics_en.pdf) | 2km | Contrast analysis between high and low clouds, and fog. Allows identification of fire hotspots | Available 24 hours a day or in "day-night" combination with other products, with infrared channels so visible night and day | 

### "Day-night" combination products : 

| "Day-night" combination products | Resolution | Application | Note | 
| ------ | ------ | ------ | ------ | 
| [Fire Temperature](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_satellite/firetemperature_en.pdf) | 1km | Forest fire detection | Uses visible light and only appears in the daytime portion of a combination | 
| [Day Cloud Type](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_satellite/daycloudtype_en.pdf) | 1km | Distinguishes between high and low clouds, reveals the vertical development stage of convective clouds | Uses visible light and only appears in the daytime portion of a combination | 
| [Day Land Cloud Fire](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_satellite/daylandcloudfire_en.pdf) | 1km | Detection of fire hotspots, smoke, burn scars | Uses visible light and appears only in the daytime portion of a combination | 
| [Snow Fog](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_satellite/snowfog_en.pdf) | 1km | Distinguish between snow on the ground, fog and low clouds | Uses visible light and appears only in the daytime portion of a combination |  
| [Visible IR Sandwich](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_satellite/visibleirsandwich_en.pdf) | 1km | Monitoring of deep convection, top features of mature convective clouds causing severe weather | Uses visible light and only appears in the daytime portion of a combination | 
| [Smoke ABI Band1](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_satellite/smokeabiband1_en.pdf) | 1km | Detection of smoke, dust storms | Uses visible light and only appears in the daytime portion of a combination | 
| [SWIR](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_satellite/swir_en.pdf) | 2km | Forest fire hotspot monitoring | Appears only in the night portion of a product combination | 
| [Night Microphysics IR](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_satellite/nightmicrophysicsir_en.pdf) | 2km | Monitoring of nocturnal convective storms | Appears only in the night portion of a product combination |

Here is the list of available "day-night" combinations:

* Day Cloud Convection (or DayVis) / Night IR
* Day Cloud Type / Night Microphysics
* Snow Fog / Night Microphysics
* Visible IR Sandwich / Night Microphysics IR 
* Smoke ABI band1 / SWIR
* Fire Temperature / SWIR
* Day Land Cloud Fire / SWIR

Other RGB products will gradually be added in the future to serve a wider range of needs.

## Support

If you have any questions about these data, [please contact us](https://weather.gc.ca/mainmenu/contact_us_e.html).
## dd_info mailing list announcements 

Announcements related to this dataset are available via the [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/) list.
