[En français](readme_fr.md)

![ECCC logo](../img_eccc-logo.png)

[TOC](../readme_en.md) > Usage Policy

# MSC Open Data Service Usage Policy

The MSC Open Data Service Usage Policy determines what constitutes an acceptable use of MSC Open Data services and provides users best practices for optimal use. This Service Usage Policy complements the [End-use licence](../licence/readme_en.md).

## Acceptable Use of MSC Open Data

The objective of the Service Usage Policy is to ensure all users benefit from efficient and uninterrupted access to MSC free and open data services.

MSC Open Data users should:

* Clearly display the data source attribution as required by the [End-use licence](../licence/readme_en.md)
* Do not actively or passively encourage copyright infringement
* Request and retrieve only data you intend to use
* Subscribe to the [GeoMet-Info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/geomet-info.comm.collab.science.gc.ca/) and/or [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info.comm.collab.science.gc.ca/) announcement lists to be notified of changes to MSC data services and be able to adapt accordingly 

Please refer to the following usage rules and best practices to ensure proper usage of MSC Open Data services.

## Usage Rules and Best Practices

Best practices:

* Review and assess your application workflow and determine which MSC data access mechanism best suits your needs. For example, building a local archive of data should be performed using MSC Datamart services, not MSC GeoMet services
* Add a meaningful HTTP User-Agent header to HTTP requests
* Ensure there is no usage of 'no-cache' headers in HTTP requests, such as 'Cache-Control: no-cache' and 'Pragma: no-cache'
* Review application logs to ensure valid requests are made and expected workflow is correctly implemented 

Usage rules for MSC GeoMet services:

* Bulk and batch retrieval of WMS tiles is prohibited. MSC Open Data services reserves the right to block applications implementing this behaviour
* For MSC GeoMet layer-specific workflows, the vendor extension for layer-specific WMS GetCapabilities should be used to retrieve smaller XML payloads
    * An example is provided in the MSC GeoMet [usage tip section](../msc-geomet/readme_en.md#Access)

Usage rules for MSC Datamart HTTPS services:

* For real-time data workflows, use the [AMQPS real-time push notification and data retrieval service](../msc-datamart/amqp_en.md)
    * Do not request directory listings to assess the availability of new data, the AMQPS notification service must be used for this need
    * Use of `wget` or `curl` commands is reserved for ad hoc data retrieval only. For systematic data retrieval, the AMQPS service must be used 

## Service Usage Policy Updates

This policy is subject to change to ensure quality of service for MSC data users. Updates will be communicated via the [GeoMet-Info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/geomet-info.comm.collab.science.gc.ca/) and [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info.comm.collab.science.gc.ca/) announcement lists. 