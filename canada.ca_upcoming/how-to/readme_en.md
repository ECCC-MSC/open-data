[En français](readme_fr.md)

![ECCC logo](../img_eccc-logo.png)

[TOC](../readme_en.md) > How to


# How to

Information and examples on how to access and use Meteorological Service of Canada open data.

## Table of content

* [Learn about the available data](#learn-about-the-available-data)
* [How to visualize the data](#how-to-visualize-the-data)
  * [Desktop software](#desktop-software)
  * [Interactive web maps and mobile apps](#interactive-web-maps-and-mobile-apps)
  * [On-the-fly images](#on-the-fly-images)
* [How to access raw data](#how-to-access-raw-data)
  * [Raw data download](#raw-data-download)
  * [Raw data web services](#raw-data-web-services)


## Learn about the available data

The Meteorological Service of Canada provides up-to-date information on past, present and future weather conditions, climate, water and environmental information over Canada and the world. [Details  on the available data is provided here](../msc-data/readme_en.md).

## How to visualize the data

### Desktop software 

MSC open data can be visualized in any software that supports the OGC Web Map Service (WMS) standard such as the free and open source software [QGIS](https://qgis.org) and in Esri ArcGIS software.

+ mention that ArcGIS supports WMS Time ?
+ data can be downloaded and visualized from the raw file (below !)


### Interactive web maps and mobile apps

Leaflet, OpenLayers. Libraries can display be used to live web maps browsers, leaflet, openlayers, amongst many others. 

include an leaflet map with the radar composite layer

Example of animated WMS in mobile app: MeteoCAN app interactive radar animation. Add image from ahmed with the radar layer with whirling

link to [details on using web services](../msc-geomet/web-services_en.md) : time / temporal, legends, accessing the other provided color scales and even customizing colors, 

### On-the-fly images

![Global Deterministic Prediction System (GDPS) surface temperature](http://geo.weather.gc.ca/geomet?service=WMS&version=1.3.0&request=GetMap&bbox=-180,-90,90,180&crs=EPSG:4326&width=800&height=600&layers=GDPS.ETA_TT&format=image/png)              

![Sea Water Salinity from the Global Ice Ocean Prediction System (GIOPS) model](https://geo.weather.gc.ca/geomet?service=WMS&version=1.3.0&request=GetMap&bbox=-180,-90,90,180&crs=EPSG:4326&width=800&height=600&layers=OCEAN.GIOPS.2D_SALW&format=image/png)              

* careful, the height is breaking aspect ratio!!!
* there's also west part of Canada is missing... crazy! QGIS shows it properly

on montre l'image qui est associé au code et ensuite on explique les paramètres, un par un, avec les détails dans une sous-pages de la section de geomet

/CP FROM ABOVE/ link to [details on using web services](../msc-geomet/web-services_en.md) : time / temporal, legends, accessing the other provided color scales and even customizing colors, 


## How to access raw data

### Raw data download

Data feeds: the MSC offers its data ..AMQP

Direct access from the web browser and from scripting commands such as LINK-WGET.


### Raw data web services

WMS GetFeatureInfo (with example), WCS , WFS or WFS3, with links. 

Get the list of available datasets and corresponding time range from the GetCapabilities (not correct name for wfs3)

Make a query, give example of the CCCS QueryUI for building Regional Deterministic Precipitation Analysis (RDPA) raw data queries, including from 2010???? to today’s analysis.

Formats see getcapa.. including GeoTIFF and netCDF

NEW handling time section above. Examples with all services above, nothing time enabled on WFS1/2, right?  Link to WFS3 nonetheless

what about time series?

[R interface](https://github.com/bcgov/geometr)