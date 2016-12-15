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
Downloading data

    AMQP
        Pattern matching and triggers (on part, on file, on message)
        Working examples of retrieving MSC data with AMQP
    Vector data in WFS
    link to list of WFS accessible layers
    Raster data in WCS
    link to list of WCS accessible layers
    Time series
    ASCII

* [Viewing data](#Viewing data)
    * [WMS](#WMS)
        * [GetMap](#GetMap)
        * [GetFeatureInfo](#GetFeatureInfo)
        * [GetLegendGraphic](#GetLegendGraphic)

	* [WFS](#WFS)
	    * [GetFeature](#GetFeature)
	    * [DescribeFeatureType](#DescribeFeatureType)
	    
	* [WCS](#WCS)
	    * [GetCoverage](#GetCoverage)
	    * [DescribeCoverage](#DescribeCoverage)
    * [Time series](#Time series)
    
    * [Desktop software](#Desktop software)
        * [ArcGIS](#ArcGIS)
        * [QGIS](#QGIS)
        * [Google Earth](#Google Earth)
        * [SPI](#SPI)


    

## Viewing data

### WMS 

#### GetMap

http://geo.weather.gc.ca/geomet/?service=WMS&version=1.3.0&request=GetMap&bbox=-180,-90,90,180&crs=EPSG:4326&width=800&height=600&layers=GDPS.ETA_TT&style=DEFAULT

#### GetFeatureInfo

http://geo.weather.gc.ca/geomet/?service=WMS&version=1.1.1&request=GetFeatureInfo&query_layers=GDPS.ETA_TT&info_format=text/plain&x=1&y=1&exceptions=xml&layers=GDPS.ETA_TT&crs=CRS:84&bbox=-73.5,45.6,-73.6,45.4&width=1&height=1

#### GetLegendGraphic

GetLegendGraphic request can be found in [GetCapabilities](http://geo.weather.gc.ca/geomet/?version=1.3.0&service=WMS&request=GetCapabilities)

http://geo.weather.gc.ca/geomet/?service=WMS&version=1.1.1&request=GetLegendGraphic&style=TEMPERATURE&layer=GDPS.ETA_TT&format=image/png


### WFS

#### GetFeature

http://geo.weather.gc.ca/geomet-beta/?version=1.1.0&service=WFS&request=GetFeature&typename=CURRENT_CONDITIONS&SRS=EPSG:4326&BBOX=-73.6,45.4,-73.5,45.6

#### DescribeFeatureType

http://geo.weather.gc.ca/geomet-beta/?version=1.1.0&service=WFS&request=DescribeFeatureType

### WCS

#### GetCoverage

http://geo.weather.gc.ca/geomet-beta/?version=1.0.0&service=WCS&request=GetCoverage&coverage=GDPS.ETA_TT&format=GTiff&bbox=-180,-90,180,90&crs=EPSG:4326&width=800&height=600

#### DescribeCoverage

http://geo.weather.gc.ca/geomet-beta/?version=1.0.0&service=WCS&request=DescribeCoverage&coverage=GDPS.ETA_TT&format=GTiff&bbox=-180,-90,180,90&crs=EPSG:4326&width=800&height=600


### Time series

TIME parameter is use to get information on layer on a specific time, multiple time values or time range. In GetCapabilities, information on time can be retrieve on time enabled layers.

Ex. 2016-12-15T12:00:00Z/2016-12-25T12:00:00Z/PT3H that correspond to begin_time/end_time/interval_time

If an incorrect time is specified in a request, it will return an error message. Time parameter must be in ISO-8601.

**Specific time** : http://geo.weather.gc.ca/geomet/?service=WMS&version=1.1.1&request=GetFeatureInfo&query_layers=GDPS.ETA_TT,GDPS.ETA_UU&info_format=text/plain&x=1&y=1&exceptions=xml&layers=GDPS.ETA_TT,GDPS.ETA_UU&crs=CRS:84&bbox=-73.5,45.6,-73.6,45.4&width=1&height=1&time=2016-12-16T12:00:00Z

**Multiple times** : http://geo.weather.gc.ca/geomet/?service=WMS&version=1.1.1&request=GetFeatureInfo&query_layers=GDPS.ETA_TT,GDPS.ETA_UU&info_format=text/plain&x=1&y=1&exceptions=xml&layers=GDPS.ETA_TT,GDPS.ETA_UU&crs=CRS:84&bbox=-73.5,45.6,-73.6,45.4&width=1&height=1&time=2016-12-16T12:00:00Z,2016-12-15T16:00:00Z,2016-12-16T18:00:00Z

**Range time** : http://geo.weather.gc.ca/geomet/?service=WMS&version=1.1.1&request=GetFeatureInfo&query_layers=GDPS.ETA_TT,GDPS.ETA_UU&info_format=text/plain&x=1&y=1&exceptions=xml&layers=GDPS.ETA_TT,GDPS.ETA_UU&crs=CRS:84&bbox=-73.5,45.6,-73.6,45.4&width=1&height=1&time=2016-12-16T12:00:00Z/2016-12-17T12:00:00Z


### Desktop software

#### ArcGIS

Select Add data. Look in GIS Server. Then Add WMS Server. Simply enter URL (http://geoweather.gc.ca/geomet/) and Get Layers.

It it the same steps for WFS and WCS.

#### QGIS

Select Layer/Add WMS. Create new WMS connection. Enter a name and URL. 

Name : GeoMet

URL : http://geo.weather.gc.ca/geomet/ 

It it the same steps for WFS and WCS.

#### Google Earth

Select Add then Image Overlay. Go in Refresh, then click on WMS parameters.Add URL (http://geoweather.gc.ca/geomet/).

#### SPI

Within the Data digging section, use the + button. Enter a name for the service and select the WMS type. You will then be able to enter the server URL (http://geo.weather.gc.ca/geomet/) which you want to access.
Once added, the server will appear in the data tree where you will be able to parse it's available layers. Double click on to display it in SPI. You can select the style and timestep to display int the raster parameter if available. 


