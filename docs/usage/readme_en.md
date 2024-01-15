[En français](readme_fr.md)

![ECCC logo](../img_eccc-logo.png)

[TOC](../readme_en.md) > Usage overview


# Usage overview

Overview and examples on how to access and use Meteorological Service of Canada open data.

* [Learn about the available data](#learn-about-the-available-data)
* [How to visualize the data](#how-to-visualize-the-data)
    * [Desktop software](#desktop-software)
    * [Interactive web maps and mobile apps](#interactive-web-maps-and-mobile-apps)
    * [On-demand images](#on-demand-images)
* [How to access raw data](#how-to-access-raw-data)
    * [Raw data web services](#raw-data-web-services)
    * [Raw data download](#raw-data-download)
    * [Work with raw data from the command line](#work-with-raw-data-from-the-command-line)


## Learn about the available data

The Meteorological Service of Canada provides up-to-date information on past, present and future weather conditions, climate, water and environmental information over Canada and the world. [The list of available data is provided here](../msc-data/readme_en.md).

## How to visualize the data

### MSC AniMet

[MSC AniMet](../msc-animet/readme_en.md) is a simple tool enabling users to interact with MSC Open Data weather data and create custom weather animations for any area in the world. The resulting animations can be downloaded and shared with a permalink.

### Desktop software 

MSC open data can be visualized in desktop software by either (A) connecting to [MSC GeoMet](../msc-geomet/readme_en.md) Web Map Service (WMS) web services or (B) by downloading the raw data from [MSC Datamart](../msc-datamart/readme_en.md) or MSC GeoMet Web Coverage Service (WCS) and OGC API- Features (WFS 3) web services and loading the raw data in the application.

MSC open data can be interactively visualized in software that supports the Open Geospatial Consortium (OGC) Web Map Service (WMS) standard such as the free and open source software [QGIS](https://qgis.org) and in Esri ArcGIS software. Instructions for adding MSC GeoMet WMS services to [QGIS](https://docs.qgis.org/3.4/en/docs/training_manual/online_resources/wms.html) and [ArcGIS](https://desktop.arcgis.com/en/arcmap/latest/map/web-maps-and-services/adding-wms-services.htm) are available. Desktop software may allow users to change the layer colors (WMS styles) and animate the layers amongst the available timesteps. Details on the available WMS parameters are available in the [web services section](../msc-geomet/wms_en.md). For downloading raw data, refer to the [How to access raw data](#how-to-access-raw-data) section.

The following tutorials are available for the QGIS desktop software: [add, query and animate WMS layers](tutorial_WMS_QGIS_en.md), [add and query OGC API Features layers](tutorial_OAFeat_QGIS_en.md) and [add raw data](tutorial_raw-data_QGIS_en.md). The following image presents the root of the GeoMet-Weather layer tree in QGIS:

![GeoMet-Weather layer tree in QGIS](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/usage/GeoMet-Weather_QGIS_Layer-tree_en.jpg)

### Interactive web maps and mobile apps

MSC open data can also easily be integrated into interactive maps in browsers and mobile applications. 

#### In a web browser

By using JavaScript libraries such as [Leaflet](https://leafletjs.com/) and [Openlayers](https://openlayers.org/), amongst others, users can integrate data available via MSC GeoMet into their own interactive web maps.

The following [tutorial is available for creating interactive web maps with OpenLayers and Leaflet](tutorial_web-maps_en.md), demonstrating how to add layers, display popup dialog boxes and animate temporal layers.

Below is an example of an OpenLayers web map configured to display [weather radar composite Web Map Service (WMS) layers served by MSC GeoMet](../msc-data/obs_radar/readme_radar_geomet_en.md).

<div id="map" style="height: 400px; position: relative">
  <div id="legend-popup">
  <div id="legend-popup-content">
    <img id="legend-img" src="https://geo.weather.gc.ca/geomet?lang=fr&version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=RADAR_1KM_RRAI&format=image/png&STYLE=Radar-Rain_Dis-14colors_Fr"/>
  </div>
</div>
</div>
<div id="controller" role="group" aria-label="Animation controls" style="background: #ececec; padding: 0.5rem;">
  <button id="fast-backward" class="btn btn-primary btn-sm" type="button"><i class="fa fa-fast-backward" style="padding: 0rem 1rem"></i></button>
  <button id="step-backward" class="btn btn-primary btn-sm" type="button"><i class="fa fa-step-backward" style="padding: 0rem 1rem"></i></button>
  <button id="play-pause" class="btn btn-primary btn-sm" type="button"><i class="fa fa-play" style="padding: 0rem 1rem"></i></button>
  <button id="step-forward" class="btn btn-primary btn-sm" type="button"><i class="fa fa-step-forward" style="padding: 0rem 1rem"></i></button>
  <button id="fast-forward" class="btn btn-primary btn-sm" type="button"><i class="fa fa-fast-forward" style="padding: 0rem 1rem"></i></button>
  <button id="exportmap" class="btn btn-primary btn-sm" type="button"><i class="fa fa-download" style="padding: 0rem 1rem"></i></button>
  <a id="image-download" download="msc-geomet_web-map_export.png"></a>
  <span id="info" style="padding-left: 0.5rem;cursor: pointer;"></span>
</div>

#### In a mobile application

MSC Geomet Web Map Services (WMS) can also be integrated into mobile applications, with JavaScript libraries such as [Leaflet](https://leafletjs.com/) and [Openlayers](https://openlayers.org/) among others. In fact, Environment and Climate Change Canada's [WeatherCAN application](https://www.canada.ca/en/environment-climate-change/services/weather-general-tools-resources/weathercan.html) (available on iOS and Android) uses MSC GeoMet to display high resolution weather radar data on an interactive map:

![Example of radar imagery in WeatherCan](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/usage/WeatherCan_MSC-GeoMet_weather-radar_20200207_en.jpg)

For additional information regarding the capabilities and parameters for MSC GeoMet web services (ie. WMS, WCS) refer to the [technical MSC GeoMet web services documentation](../../msc-geomet/readme_en/#available-ogc-standards).

### On-demand images

MSC Geomet can also serve images on-demand via a WMS GetMap request. See the examples below.

#### Example 1 - Global Deterministic Prediction System (GDPS) Surface Temperature

The following WMS GetMap request returns an image of the Global Deterministic Prediction System (GDPS) air temperature layer. The image is created on-demand at the time of the request.

```
https://geo.weather.gc.ca/geomet?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&BBOX=-90,-180,90,180
&CRS=EPSG:4326&WIDTH=600&HEIGHT=301&LAYERS=GDPS.ETA_TT&FORMAT=image/png
```
Returns:

![Global Deterministic Prediction System (GDPS) surface temperature](https://geo.weather.gc.ca/geomet?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&BBOX=-90,-180,90,180&CRS=EPSG:4326&WIDTH=600&HEIGHT=301&LAYERS=GDPS.ETA_TT&FORMAT=image/png) 

#### Example 2 - Global Ice Ocean Prediction System (GIOPS) Sea Water Salinity

The following WMS GetMap request returns an image of the Global Ice Ocean Prediction System (GIOPS) sea water salinity layer. The image is created on-demand at the time of the request.
```
https://geo.weather.gc.ca/geomet?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&BBOX=-90,-180,90,180
&CRS=EPSG:4326&WIDTH=600&HEIGHT=301&LAYERS=OCEAN.GIOPS.2D_SALW&FORMAT=image/png
```
Returns:

![Sea Water Salinity from the Global Ice Ocean Prediction System (GIOPS) model](https://geo.weather.gc.ca/geomet?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&BBOX=-90,-180,90,180&CRS=EPSG:4326&WIDTH=600&HEIGHT=301&LAYERS=OCEAN.GIOPS.2D_SALW&FORMAT=image/png)

#### Overview of WMS GetMap parameters used in the examples

The examples above define a handful of parameters and send a GetMap request to MSC GeoMet. Below is a short explanation of each parameter in the request:

* **SERVICE** - The name of the Open GeoSpatial Consortium Web Service to use in the request. In both examples, the OGC Web Map Service (WMS) is used
* **VERSION** - The service version, in this case `1.3.0`
* **REQUEST** - The specified request type. The WMS services specifies several different request types. In this case, a GetMap request is specified, which returns a map image
* **BBOX** - The bounding box of the requested image. In our case, we are making a request for an image that covers the entire surface of the Earth. Coordinates are provided in the units of the Coordinate Reference System defined in the following parameter
* **CRS** - The coordinate reference system (CRS) used to create the map image. In both examples, we set the CRS to `EPSG:4326` (i.e. WGS 84), the coordinate reference system used for the Global Positioning System (GPS)
* **WIDTH** - The width in pixels of the returned image
* **HEIGHT** - The height in pixels of the returned image
* **LAYERS** - The name of the layer used to create the image. The list and name of the available layers can be retrieved using a WMS GetCapabilities request. For best performances, it is recommended to specify one layer per WMS GetMap request
* **FORMAT** - The format of the image returned by the WMS GetMap request. In both cases case, the returned image will be in the PNG format

For further information regarding these and other WMS GetMap parameters, refer to the [technical MSC GeoMet web services documentation](../msc-geomet/wms_en.md).

## How to access raw data

### Raw data web services

Raw MSC data can be retrieved from the [MSC GeoMet web services](../msc-geomet/readme_en.md). These web services allow users to retrieve raw data by specifying the geographic coordinates, the cartographic projection, the temporal dimensions and choose amongst available data formats. Details on the available parameters are provided in the [web services](../../msc-geomet/readme_en.md#available-ogc-standards) section of the technical documentation.

The following use case examples are provided:

* [Arthur: profits based on the probability of precipitation](../use-case_arthur/use-case_arthur_en/):
    * Access and use the MSC GeoMet data API directly from a Python script, specifically the OGC Web Map Service (WMS) standard to create data tables and graphs
* [Cathy: tracking water levels at hydrometric stations](../use-case_oafeat/use-case_oafeat-script_en/):
    * Access and use the MSC GeoMet data API directly from a Python script, specifically the OGC API - Features (OAFeat) standard to create time series and interactive maps
* [Gerald: upper air observations for safe travel](../use-case_skewt/use-case_skewt_en/):
    * Access and use the MSC GeoMet data API directly from a Python script, specifically the OGC API - Process (OAProc) standard to create data tables and graphs

Raw data at specific geographic locations can be retrieved with a Web Map Service (WMS) GetFeatureInfo request. Details are provided [in the technical documentation](../msc-geomet/wms_en.md#wms-getfeatureinfo). Example of a [WMS GetFeatureInfo request for temperature from the Global Deterministic Prediction System (GDPS) model over Montreal, Canada](https://geo.weather.gc.ca/geomet/?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetFeatureInfo&QUERY_LAYERS=GDPS.ETA_TT&INFO_FORMAT=application/json&i=5&j=5&EXCEPTIONS=xml&LAYERS=GDPS.ETA_TT&CRS=EPSG:4326&BBOX=45.50,-73.56,45.51,-73.55&WIDTH=10&HEIGHT=10).

Raw data for vector data can be retrieved with a OGC API - Features (WFS 3) request. Example of a [WFS 3 query for the Winnipeg River hydrometric station daily means](https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=05PF049) which returns the corresponding data as a GeoJSON file.

Raw data for raster data can be retrieved with a Web Coverage Service (WCS) request. Example of a [WCS 2 query for the Regional Deterministic Precipitation Analysis (RDPA) model in the netCDF format for a specific time](https://geo.weather.gc.ca/geomet?SERVICE=WCS&VERSION=2.0.1&REQUEST=GetCoverage&COVERAGEID=RDPA.6F_PR&SUBSETTINGCRS=EPSG:4326&FORMAT=image/netcdf&TIME=2019-05-14T12:00:00Z). [A tutorial is available for saving a WCS request output to disk](../tutorial_gdal/tutorial_gdal_en/). A tip to build WCS queries is to use the [Canadian Centre for Climate Services WCS Query builder interface for an RDPA layer](https://climate-change.canada.ca/climate-data/#/regional-deterministic-precipitation-analysis) and replace the COVERAGEID value from RDPA.* to another available layer.

### Raw data download

MSC raw data can be [automatically retrieved as soon as it becomes available on the MSC Datamart through the Advanced Message Queuing Protocol (AMQP)](../msc-datamart/amqp_en.md). Alternatively, the raw data can also be directly downloaded on the web from the [MSC Datamart](../msc-datamart/readme_en.md) data repository.

### Work with raw data from the command line

Data can be manipulated using commands from the GDAL software library. A [tutorial showcasing the most common commands of the GDAL software library](../tutorial_gdal/tutorial_gdal_en/) is available.

<style>
  #legend-img {
    margin: 0px;
  }
  #legend-popup {
    position: absolute;
    top: 40px;
    right: 8px;
    z-index: 2;
  }
  .legend-switch{
    top: 8px;
    right: .5em;
  }
  .ol-touch .legend-switch {
    top: 80px;
  }
  .distinguish-switch{
    top: 8px;
    right: 2.25em;
    width: 10rem;
  }
  .ol-touch .distinguish-switch{
    top: 80px;
  }
  .distinguish-switch.ol-unselectable.ol-control button{
    width: 10rem;
  }
</style>

<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/ol@v7.3.0/ol.css" type="text/css"/>
<script src="https://cdn.polyfill.io/v2/polyfill.min.js?features=requestAnimationFrame,Element.prototype.classList,URL"></script>
<script src="https://cdn.jsdelivr.net/npm/ol@v7.3.0/dist/ol.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/FileSaver.js/1.3.3/FileSaver.min.js"></script>
<script>
    function isIE() {
      return window.navigator.userAgent.match(/(MSIE|Trident)/);
    }
    var head = document.getElementsByTagName('head')[0];
    var js = document.createElement("script");
    js.type = "text/javascript";
    if (isIE())
    {
        js.src = "../../js/radar_ie.js";
        document.getElementById("controller").setAttribute("hidden", true);
    }
    else
    {
        js.src = "../../js/radar.js";
    }
    head.appendChild(js);
</script>