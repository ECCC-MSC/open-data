[En français](readme_fr.md)

![ECCC logo](../img_eccc-logo.png)

[TOC](../readme_en.md) > MSC GeoMet


# MSC GeoMet

The MSC GeoMet platform provides public access to the Meteorological Service of Canada (MSC) and Environment and Climate Change Canada (ECCC) data via interoperable web services and application programming interfaces (API). Through open standards, users can freely and quickly access thousands of real-time and archived weather, climate and water datasets and products and integrate them in their domain-specific applications and decision support systems. Users can build mobile apps, create interactive web maps, and display and animate MSC data in desktop software. MSC GeoMet also enables on demand raw data clipping and reprojection, on demand format conversion and custom visualization.


## Usage, tutorials and technical documentation

Overview, examples and tutorials to access and use MSC GeoMet data:

* [Usage overview](../usage/readme_en.md)
* Tutorials:
    * Use data in the QGIS desktop software:
        * [Add, query and animate WMS layers](../usage/tutorial_WMS_QGIS_en.md)
        * [Add and query OGC API Features layers](../usage/tutorial_OAFeat_QGIS_en.md)
    * [Create interactive web maps with OpenLayers and Leaflet](../usage/tutorial_web-maps_en.md):
        * Add layers
        * Display popup dialog boxes
        * Animate temporal layers
* Use cases:
    * [Arthur: profits based on the probability of precipitation](../../usage/use-case_arthur/use-case_arthur_en/):
        * Access and use the MSC GeoMet data API directly from a Python script, specifically the OGC Web Map Service (WMS) standard to create data tables and graphs
    * [Cathy: tracking water levels at hydrometric stations](../../usage/use-case_oafeat/use-case_oafeat-script_en/):
        * Access and use the MSC GeoMet data API directly from a Python script, specifically the OGC API - Features (OAFeat) standard to create time series and interactive maps
* Technical documentation:
    * [API / geospatial web services technical documentation](web-services_en.md)

## Access

Access to the MSC GeoMet services is anonymous and free of charge. These services must be accessed with software that supports geospatial web services. The supported geospatial web services are the following Open Geospatial Consortium (OGC) standards: [Web Map Service (WMS)](https://www.opengeospatial.org/standards/wms), [Web Coverage Service (WCS)](https://www.opengeospatial.org/standards/wcs) and [OGC API - Features (WFS 3)](https://github.com/opengeospatial/WFS_FES).

### GeoMet-Weather

GeoMet-Weather provides access to the Meteorological Service of Canada (MSC) weather, and environmental data via interoperable web services. It provides access to data such as weather alerts and public forecasts, observations and numerical weather prediction forecasts.

Service capabilities:

* GeoMet-Weather WMS URL: [https://geo.weather.gc.ca/geomet?lang=en&service=WMS&version=1.3.0&request=GetCapabilities](https://geo.weather.gc.ca/geomet?lang=en&service=WMS&version=1.3.0&request=GetCapabilities)
* GeoMet-Weather WCS URL: [https://geo.weather.gc.ca/geomet?lang=en&service=WCS&version=2.0.1&request=GetCapabilities](https://geo.weather.gc.ca/geomet?lang=en&service=WCS&version=2.0.1&request=GetCapabilities)

Usage tip:

* Users can use `&layer=` in WMS GetCapabilities requests to point to a
specific layer and retrieve a smaller XML payload with up to date
temporal dimensions
    * Example for the 1km radar snow layer: [https://geo.weather.gc.ca/geomet?service=WMS&version=1.3.0&request=GetCapabilities&layer=RADAR_1KM_RSNO](https://geo.weather.gc.ca/geomet?service=WMS&version=1.3.0&request=GetCapabilities&layer=RADAR_1KM_RSNO)

### GeoMet-Climate

GeoMet-Climate provides access to Environment and Climate Change Canada (ECCC) climate data via interoperable web services. It provides access to historical climate datasets such daily observation data, monthly summaries and climate normals for climate stations across the country. The GeoMet-Climate services are a data source for the [Canadian Centre for Climate Services](https://canada.ca/climate-services).

Service capabilities:

* GeoMet-Climate WMS URL: [https://geo.weather.gc.ca/geomet-climate?service=WMS&version=1.3.0&request=GetCapabilities](https://geo.weather.gc.ca/geomet-climate?service=WMS&version=1.3.0&request=GetCapabilities)
* GeoMet-Climate WCS URL: [https://geo.weather.gc.ca/geomet-climate?service=WCS&version=2.0.1&request=GetCapabilities](https://geo.weather.gc.ca/geomet-climate?service=WCS&version=2.0.1&request=GetCapabilities)

The source code for GeoMet-Climate and the Climate Data Extraction Tool is publicly available on GitHub:

* [https://github.com/ECCC-CCCS/geomet-climate](https://github.com/ECCC-CCCS/geomet-climate)
* [https://github.com/ECCC-CCCS/climate-data-extraction-tool](https://github.com/ECCC-CCCS/geomet-climate)

### GeoMet-OGC-API

GeoMet-OGC-API provides access to the Meteorological Service of Canada (MSC) and Environment and Climate Change Canada (ECCC) data via the emerging Open Geospatial Consortium [OGC API - Features (WFS 3) standard](https://github.com/opengeospatial/ogcapi-features).

Service capabilities:

* GeoMet-OGC-API URL: [https://api.weather.gc.ca/](https://api.weather.gc.ca/)

### GeoMet-Beta

GeoMet-Beta provides access to experimental and other non-operational data. This service is not operationally supported.

Service capabilities:

* GeoMet-Beta WMS URL: [https://geo.weather.gc.ca/geomet-beta?lang=en&service=WMS&version=1.3.0&request=GetCapabilities](https://geo.weather.gc.ca/geomet-beta?lang=en&service=WMS&version=1.3.0&request=GetCapabilities)
* GeoMet-Beta WCS URL: [https://geo.weather.gc.ca/geomet-beta?lang=en&service=WCS&version=2.0.1&request=GetCapabilities](https://geo.weather.gc.ca/geomet-beta?lang=en&service=WCS&version=2.0.1&request=GetCapabilities)

### SpatioTemporal Asset Catalog

Experimental support for the [SpatioTemporal Asset Catalog (STAC) specification](https://github.com/radiantearth/stac-spec) is available for content of the [MSC Datamart](../msc-datamart/readme_en.md).

* Experimental STAC URL: [https://api.weather.gc.ca/stac/](https://api.weather.gc.ca/stac/)

## Announcement mailing list

We encourage users to subscribe to the [GeoMet-Info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/geomet-info) announcement mailing list to be informed of enhancements and changes to the MSC GeoMet services.


## Support

The MSC GeoMet services are operational 24/7. User support is provided on a best effort basis during normal business hours. Users requesting support are invited to [contact us](https://www.weather.gc.ca/mainmenu/contact_us_e.html).