What's missing in this page:
* The Table of Content
* The mouseover tooltip for ISO: "International Standards Organization"
* The mouseover tooltip for MSC: "Meteorological Service of Canada", careful: the currently published version has a typo
* The mouseover tooltip for WMS: "Web Map Service", in the section: FAQ / Can I display layers' legends...
* The FAQ section has its subsections folded by default


# Geospatial web services

MSC GeoMet provides access to the Environment and Climate Change Canada's Meteorological Service of Canada (MSC) open data, including raw numerical weather prediction (NWP) model data layers, the weather radar composite and hydrometric data, via Open Geospatial Consortium (OGC) standards such as the [Web Map Service (WMS)](https://www.opengeospatial.org/standards/wms). Meteorological and hydrological layers are served dynamically through the Web Map Service (WMS) standard to enable end-users to display meteorological data within their own tools, on interactive web maps and in mobile apps.


## Targeted Users

This service is intended for specialized users and developers with knowledge of meteorological and geospatial information technology. Users may visualize or process weather data with common geospatial tools; integrate meteorological layers with other data into their own platforms, or; display meteorological layers on interactive web maps on the web or on mobile devices.


## How to use the service

### Web Map Service and Web Coverage Service

MSC GeoMet serves meteorological, environmental and hydrometric layers at multiple time steps in the [Web Map Service (WMS) standard](https://www.opengeospatial.org/standards/wms) and  [Web Coverage Service (WCS)](https://www.opengeospatial.org/standards/wcs) standards.

MSC GeoMet web services are found on:<br>
WMS: https://geo.weather.gc.ca/geomet?service=WMS&version=1.3.0&request=GetCapabilities<br>
WCS: https://geo.weather.gc.ca/geomet?service=WCS&version=2.0.1request=GetCapabilities<br>

### Changes to the MSC GeoMet Services

The MSC needs to be flexible in the manner in which it offers specialized data to interested users. Therefore, we need to be able to update or change formats or data offerings in a timely manner, as the technology and standards do change continuously. The MSC does not guarantee using any specific formats for any prolonged period of time. We are under no obligation to notify the users in advance of any changes, but we will make every effort, when possible, to inform users subscribed to our mailing list. With that information available, it will be the responsibility of users to ensure they can adapt to upcoming changes in formats, times of issuance, types of data, etc. In order to subscribe to our GeoMet-Information mailing list, please go to: [GeoMet-Info Mailing List](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/geomet-info).

### License

The conditions of use and need for attribution to Environment and Climate Change Canada are contained in the [license text](https://dd.weatheroffice.gc.ca/doc/LICENCE_GENERAL.txt).


## Frequently Asked Questions

### How can I use this data?

MSC GeoMet weather layers may be accessed through the Web Map Service (WMS) standard.

* The layers available in the WMS standard can be used to build interactive web maps and mobile apps with tools like OpenLayers and Leaflet.
* The layers available in the WMS standard can be accessed with a variety of software going from proprietary programs such as Esri's ArcGIS to open source solutions like QGIS.

It is anticipated that MSC GeoMet weather layers will reach consumers through the development of applications by third parties.

### What are the benefits of using the MSC GeoMet web services?

With the MSC GeoMet web services you get:

* Ability to integrate, combine and incorporate meteorological layers with your organization’s own data and tools.
* You can build custom interactive web maps and mobile apps with little effort.
* No downloading of files is required to access the weather layers.
* Ability to view data over your specific area of interest without the need to download or load data outside your area of interest.
* The data is always up to date.
* Ability to view multiple layers or data fields simultaneously.

### Can I use the MSC GeoMet services in commercial products?

Yes. You need to specify that the data comes from Environment and Climate Change Canada, see the details in the [license text](https://dd.weatheroffice.gc.ca/doc/LICENCE_GENERAL.txt).

### Can I display the layers' legends?

Yes. Access to legends are specified by the WMS GetCapabilities request.

### Do I need to be connected to the Internet to use MSC GeoMet?

Yes. MSC GeoMet weather layers are served on-the-fly and require an Internet connection.