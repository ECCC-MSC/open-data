[En français](readme_metnotes-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [MetNotes](readme_metnotes_en.md) > MetNotes data on MSC Datamart

# MetNotes data

This page describes the [MetNotes](readme_metnotes_en.md) data available in GeoJSON format via the MSC Datamart.

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available via the HTTPS protocol. It is possible to access it with a standard browser. In this case, we obtain a list of links giving access to a GeoJSON file.

The MetNotes data are available at the following address:

[https://hpfx.collab.science.gc.ca/{YYYYMMDD}/WXO-DD/metnotes](https://hpfx.collab.science.gc.ca/)

where:

* __YYYYMMDD__: Year, month and day

A history of several weeks is kept in this directory.

## Filename nomenclature

NOTE: ALL HOURS ARE IN UTC.

The files have the following nomenclature:

`{YYYYMMDD}T{hhmmss.mss}Z_MSC_MetNotes.json`

where:

* __YYYYMMDD__ : Year, month and day of data emission
* __T__ : Time delimiter according to ISO8601 norms
* __hhmmss.mss__ : Hour, minute, second and milliseconds when data are produced
* __Z__ : Time zone (UTC hour)
* __MSC__ : Constant string indicating that the data is from the Meteorologcal Service of Canada (MSC)
* __MetNotes__ : Constant string indicating that data is from MetNotes
* __json__ : File extention indicating the GeoJSON format

## Support

If you have any questions about this data, please contact us at: [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).