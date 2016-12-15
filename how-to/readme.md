[En français](readme_fr.md)

![ECCC logo](../img_eccc-logo.png)

[TOC](../readme.md) > How to


How to
========

Short description

Table of Content
----------------

Short description + disclaimer that we don't endorse any software
Viewing data

    Static
    Static maps over an area (habillées ou non)
    Time series
    I want to interactively view the weather data
    On the web
    in ArcGIS Online
    KML (Google Earth examples)
    On your own web page
        in GoC OpenMaps (Federal Government only)
        In a desktop software, such as QGIS and Google Earth
        On a mobile phone

* [Viewing data](#Viewing data)
    * [WMS](#WMS)
        * [GetMap](#GetMap)
        * [GetFeatureInfo](#GetFeatureInfo)
        * [GetLegendGraphic](#GetLegendGraphic)

	* [WFS](#WFS)
	* [WCS](#WCS)
	
## Viewing data

### WMS 

#### GetMap

http://geo.weather.gc.ca/geomet/?service=WMS&version=1.3.0&request=GetMap&bbox=-180,-90,90,180&crs=EPSG:4326&width=800&height=600&layers=GDPS.ETA_TT&style=DEFAULT

#### GetFeatureInfo

http://geo.weather.gc.ca/geomet/?service=WMS&version=1.1.1&request=GetFeatureInfo&query_layers=GDPS.ETA_TT&info_format=text/plain&x=1&y=1&exceptions=xml&layers=GDPS.ETA_TT&crs=CRS:84&bbox=-73.5,45.6,-73.6,45.4&width=1&height=1

#### GetLegendGraphic

GetLegendGraphic request can be found in [GetCapabilities](http://geo.weather.gc.ca/geomet/?version=1.3.0&service=WMS&request=GetCapabilities)

http://geo.weather.gc.ca/geomet/?service=WMS&version=1.1.1&request=GetLegendGraphic&style=TEMPERATURE&layer=GDPS.ETA_TT&format=image/png




