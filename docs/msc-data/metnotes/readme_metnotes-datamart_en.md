[En français](readme_metnotes-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [MetNotes](readme_metnotes_en.md) > MetNotes data on MSC Datamart

# MetNotes data

This page describes the [MetNotes](readme_metnotes_en.md) data available in GeoJSON format via the MSC Datamart.

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available via the HTTPS protocol. It is possible to access it with a standard browser. In this case, we obtain a list of links giving access to a GeoJSON file.

The MetNotes data are available at the following address:

[https://dd.weather.gc.ca/metnotes](https://dd.weather.gc.ca/metnotes)

A history of 24 hours is kept in this directory.

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

Example :

* 20220207T000000.123Z_MSC_MetNotes.json

__Note__ : The use of milliseconds is required to ensure the uniqueness of the notes issued.

## File content

The temporal fields in the GeoJSON file are defined as follows:

| Element   |   Description    |
|-----------|------------------|
|start_datetime |   The forecaster defined time when the weather conditions addressed by the MetNote are expected to begin.|
|end_datetime |     The forecaster-defined time when the weather conditions addressed by the MetNote are no longer expected.|
|expire_datetime |  If more than 27 hours have passed since a MetNote has been published (Stale time + 3 hour’s grace), it will be considered Expired and automatically removed from dissemination platforms.|
|publish_datetime | The time that the forecaster indicates a MetNote MetObject is ready for product generation.|

## Support

If you have any questions about this data, please [contact us](https://weather.gc.ca/mainmenu/contact_us_e.html).

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).