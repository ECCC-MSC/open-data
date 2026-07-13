[En français](readme_satellite-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_en.md) > [MSC Data](../readme_en.md) > [Satellite Observations](readme_satellite_en.md) > Satellite Observations on the MSC Datamart

# Satellite data and products

This page describes data and products derived from the [satellite Himawari-8/9 instruments](https://www.jma.go.jp/jma/jma-eng/satellite/materials/Himawari89/himawari89_leaflet/201703_leaflet89.pdf) in GeoTIFF format available on the MSC Datamart every 10 minutes covering Asia, the Western Pacific and Australia, as well as a partial portion of the U.S. Pacific regions.

These products are derived from [RGB](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_satellite/what_is_an_rgb_en.pdf) (red/green/blue) images, a satellite processing technique that uses a combination of satellite sensor bands (also called channels) and applies a red/green/blue (RGB) filter to each of them. The result is a false-color image, i.e. an image that does not correspond to what the human eye would see, but offers high contrast between different cloud types and surface features. The on-board sensor of a weather satellite obtains two basic types of information: visible light data (reflected light) reflecting off clouds and different surface types, also known as "reflectance", and infrared data (emitted radiation) which are short-wave and long-wave radiation emitted by clouds and surface features. RGBs are specially designed to combine this type of satellite data, resulting in an information-rich final product.

Other products are based on the enhancement of channel data for a single wavelength, also aimed at highlighting meteorological features of the observed surface or clouds, but in a simpler way since only a single wavelength is involved. This older approach is still useful today, as its simplicity makes image interpretation easier in some cases.

## Data location 

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as it becomes available. An [overview and examples of how to access and use Meteorological Service of Canada open data](../../usage/readme_en.md) is also available.

The data is available via the HTTPS protocol. It can be accessed using a standard browser. In this case, a list of links to a GeoTIFF file is displayed.

Himawari products can be found at :

* [https://dd.weather.gc.ca/today/satellite/himawari/{HH}/](https://dd.weather.gc.ca/today/satellite/himawari/)

where :

* __HH__: Time in UTC of image validity [00, 01, .., 23]

## File name nomenclature 

File names follow the nomenclature below:

`{YYYYMMDD}T{HHmm}Z_MSC_Himawari-North_{Product}_{resolution}.tif`

where :

* __YYYYMMDD__: Year, month and day of image validity
* __T__: Time delimiter according to ISO8601 standards
* __HHmm__: Hour and minute in UTC of image validity time [00, 01, 02, ...., 22, 23] 
* __Z__: Time zone (UTC time)
* __MSC__: Constant string for Meteorological Service of Canada, the data source
* __Himawari-North__ : String indicating that data are derived from Himawari over the North Hemisphere
* __Product__: String indicating the type of satellite product generated [Ash, C03, C13, C15, Dust, NaturalColor, SO2]. See the section on file contents
* __resolution__ : Horizontal resolution of data [2km]
* __tif__ : Constant string indicating that the format is GeoTIFF 

Examples: 

* 20260713T0020Z_MSC_Himawari-North_Dust_2km.tif
* 20260713T0110Z_MSC_Himawari-North_C13_2km.tif

## File contents

Himawari data complement the observations provided by the GOES satellites by providing:

* An equivalent rate of observation: imaging every 10 minutes  
* Comparable spectral and radiometric characteristics  
* A strategic geographical extension towards:  
    * Western Pacific
    * Cyclone regions of Asia and Oceania  

This complementarity ensures better overall continuity of geostationary observations. 

| Characteristic | Himawari | GOES | 
| ------ | ------ | ------ | 
| Operator | Japan Meteorological Agency (JMA) | National Oceanic and Atmospheric Administration (NOAA) |
| Orbital Position | 140°E (Geostationary) | 75°W (GOES-East), 137°W (GOES-West) |
| Coverage | Asia-Pacific, Australia | North America, Central America, Atlantic |
| Observation Frequency | 10 minutes | 5 to 10 minutes (depending on GOES position)|
| Resolution | 0,5 km (visible), 2 km (infrared) | 0,5 km (visible), 2 km (infrared) |
| Main Instrument / Meteorological Products  | ABI (Advanced Baseline Imager) – similar capabilities, plus additional instruments (e.g., GLM). Provides sea surface temperature, cloud, precipitation, and wind products |
| Operational Start Date | 2015 (Himawari-8), 2022 (Himawari-9) | 2017 (GOES-16), 2019 (GOES-17), 2023 (GOES-18), 2025 (GOES-19)  |

## Support

If you have any questions about these data, [please contact us](https://weather.gc.ca/mainmenu/contact_us_e.html).
## dd_info mailing list announcements 

Announcements related to this dataset are available via the [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/) list.
