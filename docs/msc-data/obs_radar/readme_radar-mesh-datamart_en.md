[In French](readme_radar-mesh-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_en.md) > [MSC Data](../readme_en.md) > [Radar Data and Products](readme_radar_en.md) > MESH product on the MSC Datamart

# Hail radar product MESH (Maximum Expected Size of Hail)

The product MESH is for Maximum Estimated Size of Hail and is determined as follows: The volume of radar reflectivity at a given pixel location is integrated in the vertical from the lowest elevation scan up to the height of the -20oC temperature level. The temperature level is determined from the [High-Resolution Deterministic Prediction System (HRDPS)](../nwp_hrdps/readme_hrdps_en.md). The weighted reflectivity is processed through several intermediary steps and an empirical relation is used to estimate the maximum hail sizes. The resulting hail size estimates are displayed as a 2-dimensional field or PPI (Plan Position Indicator). The unit of the MESH product is in millimeters.

## Data Address 

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as it becomes available. An [overview and examples to access and use Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available via the HTTPS protocol. It is possible to access it with a standard browser. In this case, we obtain a list of links giving access to an hdf5 file.

The data are available at the address :

[https://hpfx.collab.science.gc.ca/{YYYYMMDD}/radar/mesh/{RADAR_ID}](https://hpfx.collab.science.gc.ca/)

where:

* __YYYYMMDD__ : Year, month and day
* __RADAR_ID__ : Radar identifier, a 5 letter code in capital letters (see list below).

A history of several weeks is kept in this directory.

__Note__: 

* A [list of radar sites](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_radar/radars_list.pdf) is available. This list will be updated regularly.

## Nomenclature of file names

Files follow the following nomenclature:

`{YYYYYMMDD}T{HHmm}Z_MSC_Radar-MESH_{RADAR_ID}_{res}.tif`

where:

* __YYYYMMDD__ : Year, month and day of the data emission
* __T__ : Time delimiter according to ISO8601 standards
* __HHmm__: Hour and minute at which the data is sent
* __Z__: Time zone (UTC time)
* __MSC__: Constant string for Meteorological Service of Canada, the data source
* __Radar-MESH__ : Constant string indicating that the data contains radar product MESH data 
* __RADAR_ID__ : 5-letter uppercase code representing the radar identifier
* __res__ : horizontal resolution [1km]
* __tif__ : Constant string indicating that the format is GeoTIFF

Example:

* 20240110T0030Z_MSC_Radar-MESH_CASBV_1km.tif

## Support

If you have any questions about these data, [please contact us](https://meteo.gc.ca/mainmenu/contact_us_f.html)

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available via the [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/) list.
