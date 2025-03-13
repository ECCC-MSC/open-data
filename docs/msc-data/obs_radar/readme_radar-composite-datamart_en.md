[En français](readme_radar-composite-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [Radar data and products](readme_radar_en.md) > North American radar composite on MSC Datamart

# North American radar composite

This mosaic is calculated over the North American domain with a horizontal spatial resolution of 1 km. This mosaic therefore includes all the Canadian and American radars available in the network and which can reach a maximum of 200 contributing radars.

To better represent precipitation over the different seasons, this mosaic renders in mm/h to represent rain and in cm/h to represent snow. For the two precipitation types (rain and snow), we use two different mathematical relationships to convert the reflectivity by rainfall rates (mm/h rain cm/h for snow).

This mosaic is based on the DPQPE (Dual-Pol Quantitative Precipitation Estimation) product for S-Band radars. For the US Nexrad radars, ECCC uses the most similar product from the US Meteorological Service (NOAA). This product displays radar reflectivity converted into precipitation rates, using the same formulas as the Canadian radars.

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available via the HTTPS protocol. It is possible to access it with a standard browser. In this case, we obtain a list of links giving access to a GeoTIFF file.

The data are available at the address :

[https://hpfx.collab.science.gc.ca/{YYYYMMDD}/radar/composite](https://hpfx.collab.science.gc.ca/)

where:

* __YYYYMMDD__ : Year, month and day

__Note__: 

* A [list of radar sites](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_radar/radars_list.pdf) is available. This list will be updated regularly.

## Technical specifications

Here are more details regarding the two products used to generate the radar composite:

* __DPQPE product__: The acronym DPQPE stands for Dual Polarization Quantitative Precipitation Estimation. It is a two-dimensional representation of the precipitation rate estimated from the lowest radar scan (elevation angle of 0.4 degrees for most S-band radars). Thus, the estimated precipitation rate is as close as possible to the Earth's surface. The EQPDP product is based, among other things, on a series of polarimetric processing steps (quality control based on dual-polarization technology) to remove non-meteorological artifacts from the raw data (volumetric scans). It is provided in mm/h for rain and cm/h for snow. This product is calculated with a maximum coverage range of 240 km.

* __American product__: ECCC uses base reflectivity mosaics from the NOAA (National Oceanic and Atmospheric Administration) Multi-Radar-Multi-Sensor (MRMS) system, with quality control to eliminate ground echoes and non-meteorological echoes. These mosaics cover the entire contiguous United States, as well as the domains of Alaska and Hawaii. This product is calculated with a maximum coverage range of 460 km for most U.S. radars. We have adapted this composite to our specific needs to ensure it is consistent and compatible with Canadian radar data, thus ensuring smooth integration between the two networks.

## Filename nomenclature

Files follow the following nomenclature:

`{YYYYYMMDD}T{HHmm}Z_MSC_Radar-Composite_{UNIT}_{res}.tif`

where:

* __YYYYMMDD__ : Year, month and day of the data emission
* __T__ : Time delimiter according to ISO8601 standards
* __HHmm__: Hour and minute at which the data is sent
* __Z__: Time zone (UTC time)
* __MSC__: Constant string for Meteorological Service of Canada, the data source
* __Radar-Composite__ : Constant string indicating that the data contains the north-american radar composite
* __UNIT__ : String indicating the unit [MMHR,CMHR] according to the precipitation type (rain, snow)
* __res__ : horizontal resolution [1km]
* __tif__ : Constant string indicating that the format is GeoTIFF

Example:

* 20240110T0030Z_MSC_Radar-Composite_MMHR_1km.tif

## Support

If you have any questions about this data, please [contact us](https://weather.gc.ca/mainmenu/contact_us_e.html).

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).
