[En français](readme_lightning-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [Lightning](readme_lightning_en.md) > Lightning data on MSC Datamart

# Lightning density data

This page describes the [lightning](readme_lightning_en.md) data available in GeoTIFF format via the MSC Datamart.

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available via the HTTPS protocol. It is possible to access it with a standard browser. In this case, we obtain a list of links giving access to a GeoTIFF file.

The MetNotes data are available at the following address:

[https://hpfx.collab.science.gc.ca/{YYYYMMDD}/WXO-DD/lightning](https://hpfx.collab.science.gc.ca/)

where:

* __YYYYMMDD__: Year, month and day

A history of several weeks is kept in this directory.

## Filename nomenclature

The files have the following nomenclature:

`{YYYYMMDD}T{HHmm}Z_MSC_Lightning_2.5km.tif`

where:

* __YYYYMMDD__ : Year, month and day of data emission
* __T__ : Time delimiter according to ISO8601 norms
* __HHmm__ : Hour and minute when data are produced
* __Z__ : Time zone (UTC hour)
* __MSC__ : Constant string indicating that the data is from the Meteorological Service of Canada (MSC)
* __Lightning__ : Constant string indicating that data contain observed flash density (km-2.min-1)
* __2.5km__ : Constant string indicating the horizontal data resolution
* __tif__ : File extention indicating the GeoTIFF format

## Support

If you have any questions about this data, please contact us at: [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).
