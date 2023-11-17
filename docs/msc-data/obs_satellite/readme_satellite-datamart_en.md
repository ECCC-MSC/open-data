[In French](readme_satellite-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_en.md) > [MSC Data](../readme_en.md) > [Satellite Observations](readme_satellite_en.md) > Satellite Observations on the MSC Datamart

# Satellite data and products

This page describes data and products derived from GOES-West and GOES-East [satellite](readme_satellite_en.md) instruments in GeoTIFF format available on the MSC Datamart. 

These products are derived from [RGB](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_satellite/what_is_an_rgb_en.pdf) (red/green/blue) images, a satellite processing technique that uses a combination of satellite sensor bands (also called channels) and applies a red/green/blue (RGB) filter to each of them. The result is a false-color image, i.e. an image that does not correspond to what the human eye would see, but offers high contrast between different cloud types and surface features. The on-board sensor of a weather satellite obtains two basic types of information: visible light data (reflected light) reflecting off clouds and different surface types, also known as "reflectance", and infrared data (emitted radiation) which are long-wave radiations emitted by clouds and surface features. RGBs are specially designed to combine this type of satellite data, resulting in an information-rich final product.

Four types of products are currently generated from the GOES-West and GOES-East satellites: ["NightIR"](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_satellite/night_ir_en.pdf) and ["NightMicrophysics"](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_satellite/night_microphysics_en.pdf), at 2km resolution, are generated 24 hours a day with infrared channels, so are visible both night and day, and ["NaturalColour"](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_satellite/natural_colour_en.pdf) and ["DayCloudConvection"](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_satellite/day_cloud_convection_en.pdf), at 1km resolution, which combine visible light channels with infrared channels; their higher resolution makes the latter two products more popular, but they are not available during most of the night (between 02UTC and 07UTC for GOES-Est, and between 06UTC and 11UTC for GOES-Ouest) given the absence of reflected sunlight. Other RGB products should be added gradually in the future to meet different needs. 

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
* __Product__: String indicating the type of satellite product generated [NaturalColor, DayVis, NighIR, NightMicrophysics]
* __resolution__ : Horizontal resolution of data [1km, 2km]
* __tif__ : Constant string indicating that the format is GeoTIFF 

Examples: 

* 20231109T0800Z_MSC_GOES-East_NaturalColor_1km.tif
* 20231109T0510Z_MSC_GOES-West_NightMicrophysics_2km.tif

## Support

If you have any questions about these data, please contact us at: [dps-client@ec.gc.ca](mailto:ec.dps-client.ec@canada.ca)

## dd_info mailing list announcements 

Announcements related to this dataset are available via the [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/) list.
