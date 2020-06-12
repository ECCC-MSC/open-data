[En français](readme_raqdps-fw-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [RAQDPS-FW](readme_raqdps-fw_en.md) > Regional Air Quality Deterministic Prediction System FireWork on MSC Datamart

# Regional Air Quality Deterministic Prediction System FireWork (RAQDPS-FW) data in GRIB2 Format

This page describes data from the FireWork system, an air quality forecasting system incorporating emissions from forest fires. The system is run twice a day, initialized at 00:00 and 12:00 UTC, in conjunction with the Regional Deterministic Air Quality Forecasting System (RDAFS). Forest fire emissions are estimated using data on hot spots and fuel consumed on Canadian and U.S. lands provided by Natural Resources Canada's [Canadian Wildland Fire Information System]( http://cwfis.cfs.nrcan.gc.ca/). The hotspot data set is downloaded twice daily, prior to the FireWork system running. This system has the advantage of presenting the complete emissions inventory as well as added intermittent fire sources.

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data can be accessed at the following URLs:

* []()

A history of XXXX days of forecast is kept in this directory.

## File nomenclature

NOTE: ALL HOURS ARE IN UTC.

The files have the following nomenclature:

* XXXXXX

where:

* __xx__ : XXXXXX

Example of forecast file name:
* XXXX

## Support

If you have any questions about these data, please contact us at: [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).
