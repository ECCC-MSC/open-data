[En français](readme_fr.md)

![ECCC logo](../img_eccc-logo.png)

[TOC](../readme_en.md) > How to


How to
========

Short description

Table of Content
----------------

NEED TO CLEAN UP THIS TOC

* Short description + disclaimer that we don't endorse any software
* Viewing data
* Static maps over an area (habillées ou non)
* Time series
  * Interactively view the weather data
  * in ArcGIS Online
* On the web
* On your own web page
  * in GoC OpenMaps (Federal Government only)
* In a desktop software, such as QGIS and Google Earth
* On a mobile phone
* Downloading data
    * AMQP, wget
  * Pattern matching and triggers (on part, on file, on message)
  * Working examples of retrieving MSC data with AMQP
    * Vector data in WFS
* Raster data in WCS
* Time series

second group, to clean up as well:
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

#### Display static map (GetMap)

http://geo.weather.gc.ca/geomet/?service=WMS&version=1.3.0&request=GetMap&bbox=-180,-90,90,180&crs=EPSG:4326&width=800&height=600&layers=GDPS.ETA_TT&style=DEFAULT&format=PNG

In this example, we can see a map of the layer GPDS.ETA_TT which correspond to temperature in an extent of the whole world on a png of 800 x 600 pixels.

#### Get raw data on a specific pixel (GetFeatureInfo)

http://geo.weather.gc.ca/geomet/?service=WMS&version=1.1.1&request=GetFeatureInfo&query_layers=GDPS.ETA_TT&info_format=text/plain&x=1&y=1&exceptions=xml&layers=GDPS.ETA_TT&crs=CRS:84&bbox=-73.5,45.6,-73.6,45.4&width=1&height=1

In this example, we can get raw data values of layer GDPS.ETA_TT which correspond to temperature on a specific area determined by the bounding box. In that area, we select pixels (x,y) based on their size (width, height). Note that pixel (0,0) is at the top left.

#### Display legend of a layer (GetLegendGraphic)

GetLegendGraphic request can be found in [GetCapabilities](http://geo.weather.gc.ca/geomet/?version=1.3.0&service=WMS&request=GetCapabilities)

http://geo.weather.gc.ca/geomet/?service=WMS&version=1.1.1&request=GetLegendGraphic&style=TEMPERATURE&layer=GDPS.ETA_TT&format=image/png

In this example, we get the legend for a layer with the specified style, which can be customize using a SLD. If no style is specified, it's the default one. Otherwise, default style can be directly specified with style=DEFAULT

### WFS

#### GetFeature

http://geo.weather.gc.ca/geomet-beta/?version=1.1.0&service=WFS&request=GetFeature&typename=CURRENT_CONDITIONS&SRS=EPSG:4326&BBOX=-73.6,45.4,-73.5,45.6

#### Get description of features in vector layers (DescribeFeatureType)

http://geo.weather.gc.ca/geomet-beta/?version=1.1.0&service=WFS&request=DescribeFeatureType

### WCS

#### Get raw data on a specific area (GetCoverage)

http://geo.weather.gc.ca/geomet-beta/?version=1.0.0&service=WCS&request=GetCoverage&coverage=GDPS.ETA_TT&format=GTiff&bbox=-180,-90,180,90&crs=EPSG:4326&width=800&height=600

In this example, we get raw data on a specified extent for the layer GDPS.ETA_TT which correspond to temperature. In GTiff format, values will be in RGB code, but if format is GEOTIFF_16, it will be the raw values.

#### DescribeCoverage

http://geo.weather.gc.ca/geomet-beta/?version=1.0.0&service=WCS&request=DescribeCoverage&coverage=GDPS.ETA_TT&format=GTiff&bbox=-180,-90,180,90&crs=EPSG:4326&width=800&height=600

This example delivers XML-encoded descriptions of coverage such as their location, type of projection supported, interpolation, etc.

### Use time series

TIME parameter is use to get information on layer on a specific time, multiple time values or time range. In GetCapabilities, information on time can be retrieve on time enabled layers.

Ex. 2016-12-15T12:00:00Z/2016-12-25T12:00:00Z/PT3H that correspond to begin_time/end_time/interval_time

If an incorrect time is specified in a request, it will return an error message. Time parameter must be in ISO-8601.

**Specific time** : http://geo.weather.gc.ca/geomet/?service=WMS&version=1.1.1&request=GetFeatureInfo&query_layers=GDPS.ETA_TT,GDPS.ETA_UU&info_format=text/plain&x=1&y=1&exceptions=xml&layers=GDPS.ETA_TT,GDPS.ETA_UU&crs=CRS:84&bbox=-73.5,45.6,-73.6,45.4&width=1&height=1&time=2016-12-16T12:00:00Z

**Multiple times** : http://geo.weather.gc.ca/geomet/?service=WMS&version=1.1.1&request=GetFeatureInfo&query_layers=GDPS.ETA_TT,GDPS.ETA_UU&info_format=text/plain&x=1&y=1&exceptions=xml&layers=GDPS.ETA_TT,GDPS.ETA_UU&crs=CRS:84&bbox=-73.5,45.6,-73.6,45.4&width=1&height=1&time=2016-12-16T12:00:00Z,2016-12-15T16:00:00Z,2016-12-16T18:00:00Z

**Time range** : http://geo.weather.gc.ca/geomet/?service=WMS&version=1.1.1&request=GetFeatureInfo&query_layers=GDPS.ETA_TT,GDPS.ETA_UU&info_format=text/plain&x=1&y=1&exceptions=xml&layers=GDPS.ETA_TT,GDPS.ETA_UU&crs=CRS:84&bbox=-73.5,45.6,-73.6,45.4&width=1&height=1&time=2016-12-16T12:00:00Z/2016-12-17T12:00:00Z


### Use GeoMet with desktop software

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
