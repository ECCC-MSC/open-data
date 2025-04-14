[In French](readme_radar-dpqpe-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_en.md) > [MSC Data](../readme_en.md) > [DPQPE Data](readme_radar_en.md) > Dual Polarized Quantitative Precipitation Estimation (DPQPE) on the MSC Datamart

# Radar imagery

This page describes the Dual Polarized Quantitative Precipitation Estimation (DPQPE) data in GeoTIFF format available on the MSC Datamart.

This product is exclusively available for all Canadian S-band radars and provides a two-dimensional representation of precipitation rate, based on the 0.4 degree elevation scan data from S-band radars. It therefore provides an estimate of precipitation rate as close as possible to the Earth's surface.

The DPQPE product is built, among other things, on the basis of a series of polarimetric processing steps, which serve primarily as quality control measures to remove non-meteorological artifacts from the raw data. In addition, there is a hybrid option in the DPQPE product designed to fill gaps in precipitation data resulting from radar signal or polarimetric data processing. This hybrid option uses the two adjacent upper elevation scans above 0.4 degrees to help fill these data gaps.

Precipitation rates are calculated in liquid equivalent in MM/HR and converted to CM/HR for snowfall over a maximum coverage range of 240 km. 

## Data address 

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An overview and examples of how to access and use Meteorological Service of Canada open data](../../usage/readme_en.md) is also available.

The data is available via the HTTPS protocol. It can be accessed using a standard browser. In this case, a list of links to a GeoTIFF file is displayed.

The radar images can be found at :

[https://hpfx.collab.science.gc.ca/{YYYMMDD}/radar/dpqpe/{RADAR_ID}](https://hpfx.collab.science.gc.ca/)

where :

* __YYYYMMDD__: Year, month and day
* __RADAR_ID__: Radar identifier, a 5-letter code in uppercase letters (see list below)

__Notes__: 

* A [list of radar sites](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_radar/radars_list.pdf) is available. This list will be updated regularly.

## Nomenclature of file names 

Files have the following nomenclature:

`{YYYYMMDD}T{HHmm}Z_MSC_Radar-DPQPE_{RADAR_ID}_{SCALE}_{res}.hdf5`

where :

* __YYYYMMDD__ : Year, month and day of data emission
* __T__: Time delimiter according to ISO8601 standards
* __HHmm__: Hour and minute at which data is sent
* __Z__: Time zone (UTC time)
* __MSC__: Constant character string for Meteorological Service of Canada, the data source
* __Radar-DPQPE__ : Constant character string indicating that the data contains the DPQPE product
* __RADAR_ID__: 5-letter uppercase code representing the radar identifier
* __SCALE__: Conversion scale used to measure precipitation, may be in millimeters per hour (MMHR) or centimeters per hour (CMHR)
* __res__: Horizontal resolution [1km]
* __hdf5__ : Constant character string indicating that the format is HDF5

Example:

* 20240429T0030Z_MSC_Radar-DPQPE_CASFM_CMHR_1km.tif

## Support

If you have any questions about this data, please [contact us](https://weather.gc.ca/mainmenu/contact_us_f.html).

## dd_info mailing list announcements 

Announcements related to this dataset are available via the [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/) list.
