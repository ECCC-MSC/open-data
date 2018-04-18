What's missing in this page:
* The Table of Content
* The mouseover tooltip for ISO: "International Standards Organization"
* The mouseover tooltip for MSC: "Meteorological Services of Canada", typo included
* The mouseover tooltip for WMS: "Web Map Service", in the section: FAQ / Can I get an overview... and in the FAQ / Can I display layers' legends... and FAQ / Can I add contours... and FAQ / Can I access Hurricane...
* The FAQ section has its subsections folded by default

# Geospatial web services


GeoMet provides access to the Environment Canada's Meteorological Service of Canada (MSC) raw numerical weather prediction (NWP) model data layers and the weather radar mosaic via two Open Geospatial Consortium web service standards: [Web Map Service (WMS)](http://www.opengeospatial.org/standards/wms) and Keyhole Markup Language (KML). Meteorological layers are dynamically served through the Web Map Service (WMS) standard to enable end-users to display meteorological data within their own tools and on interactive web maps, and served through KML standard for easy display in tools such as Google Earth™.

We're readying the next version of these web services, please refer to the [MSC GeoMet 2 Migration Guide](http://lists.ec.gc.ca/pipermail/geomet-info/2017-March/000039.html) for a summary of improvements and breaking changes. The new version can be tested right away on GeoMet-Beta.

## Targeted Users


This service is aimed at specialized users and developers with good meteorological and information technology knowledge who want to visualize raw NWP models and the weather radar mosaic layers in common geospatial tools; want to integrate meteorological layers into their own platforms, or; want to display meteorological layers on interactive web maps for the web or on mobile devices.

Data provided through GeoMet is not appropriate for meteorological data processing. Please consult the [Meteorological Service of Canada's Datamart](http://dd.meteo.gc.ca/about_dd_apropos.txt) for such uses.

## How to use the service

### Web Map Service

GeoMet serves meteorological layers at multiple time steps in the [WMS standard](http://www.opengeospatial.org/standards/wms) along with the associated metadata in the ISO 19115 standard.

GeoMet WMS server is found on :<br>
http://geo.weather.gc.ca/geomet/?lang=E&service=WMS&request=GetCapabilities.

### Keyhole Markup Language (KML)

GeoMet data is available in .KMZ format for use with Google Earth™ and other software that supports the KML standard.

To use Google Earth™ to view the GeoMet layers:

1. [Download Google Earth™](http://earth.google.com/intl/en/) (available at no charge from the Google Earth™ website) if it is not already installed on your computer.

2. Download and open the [GeoMet KML: GeoMet-E.kmz](https://www.canada.ca/content/dam/eccc/migration/main/meteo-weather/c0d9b3d8-d256-407d-a68f-c606d703105e/geomet-e.kmz) layers.

### Changes to the GeoMet Services

The MSC needs to be flexible in the manner in which it offers specialized data to interested users. Therefore, we need to be able to update or change formats or data offerings in a timely manner, as the technology and standards do change continuously. The MSC does not guarantee using any specific formats for any prolonged period of time. We are under no obligation to notify the users in advance of any changes, but we will make every effort, when possible, to inform users subscribed to our mailing list. With that information available, it will be the responsibility of users to ensure they can adapt to upcoming changes in formats, times of issuance, types of data, etc. In order to subscribe to our GeoMet-Information mailing list, please go to: [GeoMet-Info Mailing List](http://lists.ec.gc.ca/cgi-bin/mailman/listinfo/geomet-info).

### License

The conditions of use and need for attribution to Environment Canada are contained in the [license text](http://dd.weatheroffice.gc.ca/doc/LICENCE_GENERAL.txt).

## Frequently Asked Questions

### How can I use this data?

There are two ways to access GeoMet weather layers, either through the Web Map Service (WMS) standard or through the GeoMet KeyHole Markup Language (KML) file.

* The layers can be accessed from the GeoMet KML file by using the free software Google Earth™ or other KML-supporting software.
* The layers available in the WMS standard can be used to build interactive web maps with tools like OpenLayers.
* The layers available in the WMS standard can be accessed with a variety of software going from proprietary programs such as Esri's ArcGIS to open source solutions like Quantum GIS.

It is anticipated that GeoMet weather layers will reach consumers through the development of applications by third parties.

### Can I get an overview of the weather layers provided by GeoMet?

Yes. You can view the GeoMet weather layers available in WMS by opening the GeoMet [KML](https://www.canada.ca/content/dam/eccc/migration/main/meteo-weather/c0d9b3d8-d256-407d-a68f-c606d703105e/geomet.kmz) file in Google Earth™.

### What are the benefits of using the GeoMet web services?

With the GeoMet web services you get:

* Ability to integrate, combine and incorporate meteorological layers with your organization’s own data and tools.
* You can build custom interactive web maps with little effort.
* No downloading of files is required to access the weather layers.
* Ability to view data over your specific area of interest without the need to download or load data outside your area of interest.
* The data is always up to date.
* Ability to view multiple layers or data fields simultaneously.

### Can I use the GeoMet services in commercial products?

Yes. You need to specify that the data comes from Environment Canada, see the details in the [license text](http://dd.weatheroffice.gc.ca/doc/LICENCE_GENERAL.txt).

### Can I display the layers' legends?

Yes. Access to legends are specified by the WMS GetCapabilities request.

### Why are the KML animations slower than typical GIF animations?

The KML animations are generated on-the-fly for the region and zoom level currently defined. Due to the way Google Earth™ requests and processes time stamped images, a few loop iterations might be required for the whole animation to be loaded. This effect can be seen on Google's own radar animation to a lesser degree.

### Can I change the colour scheme of the GeoMet layers?

No, GeoMet does not currently support the Styled Layer Descriptor standard which allows users to specify the colour scheme of a WMS layer. Users needing to apply their own colour schemes are invited to use the GRIB data available on MSC’s Datamart.

### Can I add contours to the GeoMet fields that do not have any?

No, not with the WMS standard. Users needing to generate contour maps not currently provided are invited to use the GRIB data available on MSC’s Datamart.

### Can I Access Hurricane and Tropical Storm Track Forecasts in WMS?

No, the [Canadian Hurricane Centre](http://www.ec.gc.ca/ouragans-hurricanes/)'s hurricane and tropical storm track forecasts are only available in the GeoMet KML file.

### Do I need to be connected to the Internet to use GeoMet?

Yes. GeoMet weather layers are served on-the-fly and require an Internet connection.