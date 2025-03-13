[En français](readme_radar-composite-extrapolation-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [Radar data and products](readme_radar_en.md) > Extrapolated North American radar composite on MSC Datamart

# Extrapolated North American radar composite

This product is the Radar Extrapolation Composite at 1 km resolution over the North American domain. It uses only the 6-minute high-resolution (1 km) radar composite (the one displayed on the different government public platforms) as input.

Using a modification of the open source PySTEPS library, a motion field is computed, and radar echoes are projected forward in time. The motion is based on similarities between radar reflectivity in a time sequence at multiple spatial scales.

Future radar reflectivity is extrapolated, followed by conversion to precipitation rates of MM/HR (Rain) or CM/HR (Snow). An output sequence of future radar is generated every 6 minutes.

It is important to note that this output is only a projection of existing echoes with no account for the growth and decay that is expected in a real radar sequence. Errors will exist, especially near the edges of radar coverage, or near geographic features. Therefore, the product should be used with caution considering that no perfect solution can exist given the limits of predictability.

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available via the HTTPS protocol. It is possible to access it with a standard browser. In this case, we obtain a list of links giving access to a GeoTIFF file.

The data are available at the address :

[https://hpfx.collab.science.gc.ca/{YYYYMMDD}/radar/composite-extrapolation](https://hpfx.collab.science.gc.ca/)

where:

* __YYYYMMDD__ : Year, month and day

__Note__: 

* A [list of radar sites](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_radar/radars_list.pdf) is available. This list will be updated regularly.

## Technical specifications

Extrapolation is carried out exclusively within the coverage area of the radar network in the North American domain (Canada and the United States), with a maximum range of 240 km for Canadian radars and 460 km for U.S. radars.

The product is available in dBZ, MM/HR, and CM/HR.

The composite is available every 6 minutes, with a production and availability delay of approximately 7 minutes after the valid time.

## Filename nomenclature

Files follow the following nomenclature:

`{YYYYYMMDD}T{HHmm}Z_MSC_Radar-Composite-Extrapolation_{UNIT}_{res}_PT{mmm}M.tif`

where:

* __YYYYMMDD__ : Year, month and day of the data emission
* __T__ : Time delimiter according to ISO8601 standards
* __HHmm__: Hour and minute at which the data is sent
* __Z__: Time zone (UTC time)
* __MSC__: Constant string for Meteorological Service of Canada, the data source
* __Radar-Composite-Extrapolation__ : Constant string indicating that the data contains the extrapolated north-american radar composite
* __UNIT__ : String indicating the unit [MMHR,CMHR] according to the precipitation type (rain, snow)
* __res__ : Horizontal resolution [1km]
* __PT{mmm}M__ : Validity time in minutes
* __tif__ : Constant string indicating that the format is GeoTIFF

Example:

* 20240110T0030Z_MSC_Radar-Composite-Extrapolation_MMHR_1km_PT042M.tif

## Support

If you have any questions about this data, please [contact us](https://weather.gc.ca/mainmenu/contact_us_e.html).

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).
