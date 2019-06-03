[En français](readme_fr.md)

![ECCC logo](../img_eccc-logo.png)

[TOC](../readme_en.md) > How to


# How to

Overview and examples on how to access and use Meteorological Service of Canada open data.

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

MSC open data can be visualized in desktop software by either (A) connecting to MSC GeoMet Web Map Service (WMS) web services or (B) by downloading the raw data from MSC Datamart or MSC GeoMet Web Coverage Service (WCS) web services and loading the raw data in the application.

MSC open data can be interactively visualized in software that supports the OGC Web Map Service (WMS) standard such as the free and open source software [QGIS](https://qgis.org) and in Esri ArcGIS software. Instructions for adding [MSC GeoMet WMS services](../msc-geomet/readme_en.md) to [QGIS](https://docs.qgis.org/3.4/en/docs/training_manual/online_resources/wms.html) and [ArcGIS](https://desktop.arcgis.com/en/arcmap/latest/map/web-maps-and-services/adding-wms-services.htm) are available. Desktop software may allow users to change the layer colors (WMS styles) and animate the layers amongst the available timesteps. Details on the available WMS parameters are available in the [web services](../msc-geomet/web-services.md) section.

For downloading raw data, refer to the [How to access raw data](#how-to-access-raw-data) section.


### Interactive web maps and mobile apps

INCOMPLETE

Leaflet, OpenLayers. Libraries can display be used to live web maps browsers, leaflet, openlayers, amongst many others. 

include an leaflet map with the radar composite layer

Example of animated WMS in mobile app: MeteoCAN app interactive radar animation. Add image from ahmed with the radar layer with whirling

link to [details on using web services](../msc-geomet/web-services_en.md) : time / temporal, legends, accessing the other provided color scales and even customizing colors, 

### On-the-fly images

INCOMPLETE

![Global Deterministic Prediction System (GDPS) surface temperature](https://geo.weather.gc.ca/geomet?service=WMS&version=1.3.0&request=GetMap&bbox=-180,-90,90,180&crs=EPSG:4326&width=800&height=600&layers=GDPS.ETA_TT&format=image/png)              

![Sea Water Salinity from the Global Ice Ocean Prediction System (GIOPS) model](https://geo.weather.gc.ca/geomet?service=WMS&version=1.3.0&request=GetMap&bbox=-180,-90,90,180&crs=EPSG:4326&width=800&height=600&layers=OCEAN.GIOPS.2D_SALW&format=image/png)              

* careful, the height is breaking aspect ratio!!!
* there's also west part of Canada is missing... crazy! QGIS shows it properly

on montre l'image qui est associé au code et ensuite on explique les paramètres, un par un, avec les détails dans une sous-pages de la section de geomet

/CP FROM ABOVE/ link to [details on using web services](../msc-geomet/web-services_en.md) : time / temporal, legends, accessing the other provided color scales and even customizing colors, 


## How to access raw data

### Raw data download

MSC data can be [automatically retrieved as soon as it becomes available through the Advanced Message Queuing Protocol (AMQP)](../msc-datamart/amqp_en.md).

The raw data can also be directly downloaded from the web on the MSC Datamart data repository.

Details for using AMQP and direct access are provided in the [MSC Datamart](../msc-datamart/readme_en.md) section.


### Raw data web services

Raw MSC data can be retrieved from the MSC GeoMet web services. These web services allow users to retrieve raw data by specifying the geographic coordinates, geographic projection, the temporal dimension and choose amongst available data formats. Details on the available parameters are provided in the [web services](../msc-geomet/web-services_en.md) section.

Raw data at specific geographic locations can be retrieved with a Web Map Service (WMS) GetFeatureInfo request. Example of a [WMS GetFeatureInfo request for temperature from the Global Deterministic Prediction System (GDPS) model over Montreal, Canada](https://geo.weather.gc.ca/geomet/?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetFeatureInfo&QUERY_LAYERS=GDPS.ETA_TT&INFO_FORMAT=text/plain&X=100&Y=100&EXCEPTIONS=xml&LAYERS=GDPS.ETA_TT&CRS=EPSG:4326&BBOX=-73.56,45.50,-73.55,45.51&WIDTH=100&HEIGHT=100). _CAREFUL, seems like something's wrong with the coordinates and response for this request_

Raw data for vector data can be retrieved with a Web Feature Service (WFS) request. Example of a [WFS 3 query for the Winnipeg River hydrometric station daily means](https://geo.weather.gc.ca/geomet/features/collections/hydrometric-daily-mean/items?STATION_NUMBER=05PF049).

Raw data for raster data can be retrieved with a Web Coverage Service (WCS) request. Example of a [WCS 2 query for the Regional Deterministic Precipitation Analysis (RDPA) model in the netCDF format for a specific time](https://geo.weather.gc.ca/geomet?SERVICE=WCS&VERSION=2.0.1&REQUEST=GetCoverage&COVERAGEID=RDPA.6F_PR&SUBSETTINGCRS=EPSG:4326&FORMAT=image/netcdf&TIME=2019-05-14T12:00:00Z). A tip to build WCS queries is to use the [Canadian Centre for Climate Services WCS Query builder interface for an RDPA layer](https://climate-change.canada.ca/climate-data/#/regional-deterministic-precipitation-analysis) and replace the COVERAGEID value from RDPA.* to another available layer.