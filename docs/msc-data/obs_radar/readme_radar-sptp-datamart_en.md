[In French](readme_radar-sptp-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_en.md) > [MSC Data](../readme_en.md) > [Radar Data and Products](readme_radar_en.md) > SPTP product on the MSC Datamart

# Surface precipitation type product (SPTP)

This product is a 1km resolution composite over the North American domain, which, for areas with radar coverage, can distinguish the occurrence, type and intensity of precipitation. This product uses two 1km radar composites as input: a North American composite cleaned using dual polarization technology, another particle classification radar composite (precipitation) and surface temperature from the [High Resolution Deterministic Prediction System (HRDPS)](../nwp_hrdps/readme_hrdps_en.md)(HRDPS). The SPTP product is produced every 6 minutes.

## Data Address 

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as it becomes available. An [overview and examples to access and use Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available via the HTTPS protocol. It is possible to access it with a standard browser. In this case, we obtain a list of links giving access to an hdf5 file.

The data are available at the address :

[https://hpfx.collab.science.gc.ca/{YYYYMMDD}/radar/sptp](https://hpfx.collab.science.gc.ca/)

where:

* __YYYYMMDD__ : Year, month and day

A history of several weeks is kept in this directory.

__Note__: 

* A [list of radar sites](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_radar/radars_list.pdf) is available. This list will be updated regularly.

## Nomenclature of file names

Files follow the following nomenclature:

`{YYYYYMMDD}T{HHmm}Z_MSC_Radar-Composite_SfcPrecipType_{res}.tif`

where:

* __YYYYMMDD__ : Year, month and day of the data emission
* __T__ : Time delimiter according to ISO8601 standards
* __HHmm__: Hour and minute at which the data is sent
* __Z__: Time zone (UTC time)
* __MSC__: Constant string for Meteorological Service of Canada, the data source
* __Radar-Composite__ : Constant string indicating that the data contains a radar composite
* __SfcPrecipType__ : Constant string indicating that the data contains the surface precipitation type product (SPTP)
* __res__ : horizontal resolution [1km]
* __tif__ : Constant string indicating that the format is GeoTIFF

Example:

* 20240110T0030Z_MSC_Radar-Composite_SfcPrecipType_1km.tif

## Support

If you have any questions about these data, [please contact us](https://meteo.gc.ca/mainmenu/contact_us_f.html)

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available via the [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/) list.
