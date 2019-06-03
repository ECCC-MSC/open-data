[En français](web-services_fr.md)

![ECCC logo](../img_eccc-logo.png)

[TOC](../readme_en.md) > MSC GeoMet web services


This page will provide details on the MSC GeoMet web services, especially the capabilities and parameters. These come in addition to the how-to page

We need a link from the readme_en.md to here
____


Get the list of available datasets and corresponding time range from the GetCapabilities (not correct name for wfs3)

Make a query, give example of the CCCS QueryUI for building Regional Deterministic Precipitation Analysis (RDPA) raw data queries, including from 2010???? to today’s analysis.

Formats see getcapa.. including GeoTIFF and netCDF

NEW handling time section above. Examples with all services above, nothing time enabled on WFS1/2, right?  Link to WFS3 nonetheless

what about time series?

[R interface](https://github.com/bcgov/geometr) - this is for GeoMet-Features only, right?

----

list supported CRS / geographic projections

### Handling time

SHOULD THIS BE HERE or in a section in itself? given the parameters also applies to WCS (below)... maybe we can have a summary of parameters here, with [details in a GeoMet subpage?] - yes?

The WMS GetCapability response for that layer

Temporal by default is now, closest past for model data.

Users can use &layer= in WMS GetCapabilities requests to point to a specific layer and retrieve a smaller XML payload with up to date temporal dimensions
* Example for the 1km radar snow layer: https://geo.weather.gc.ca/geomet?service=WMS&version=1.3.0&request=GetCapabilities&layer=RADAR_1KM_RSNO

mention that ArcGIS supports WMS Time ?

* Available timesteps for a layer is provided in the WMS GetCapabilities response
* The TIME and DIM_REFERENCE_TIME parameters should be in the form: &TIME=:YYYY-MM-DDThh:mm:ssZ
* MSC GeoMet supports the OGC Best Practice for using Web Map Services (WMS) with Time-Dependent or Elevation-Dependent Data. Reference document: [https://www.opengis.net/doc/bp/wms-tnz/1.0]
* If no TIME or DIM_REFERENCE_TIME parameter is specified, then the data corresponding to the request time is provided by default
* Layer-specific GetCapabilities: 
 * MSC GeoMet's WMS GetCapabilities response is large given the number of layers available. Users accessing information for a specific layer, such as its currently valid temporal dimensions, can use the "LAYERS=" parameter to access the GetCapabilities information specific to that layer. Note that this feature is an extension to the WMS specification.
 * Example of such a request: https://geo.weather.gc.ca/geomet?service=WMS&version=1.3.0&request=GetCapabilities&layers=RADAR_1KM_RRAI
* Example of requests:
 * [TIME](https://geo.weather.gc.ca/geomet/?service=WMS&version=1.3.0&request=GetMap&bbox=-180,-90,90,180&crs=EPSG:4326&TIME=2018-06-15T12:00:00Z&width=800&height=600&layers=GDPS.ETA_TT&style=DEFAULT&FORMAT=image/png)
 * [REFERENCE_TIME](https://geo.weather.gc.ca/geomet/?service=WMS&version=1.3.0&request=GetMap&bbox=-180,-90,90,180&crs=EPSG:4326&TIME=2018-29-15T12:00:00Z&DIM_REFERENCE_TIME=2018-08-28T00:00:00Z&width=800&height=600&layers=GDPS.ETA_TT&style=DEFAULT&FORMAT=image/png) - this example does not work
* Support of time in off-the-shelf tools:
 * https://openlayers.org/en/latest/examples/wms-time.html
 * https://leafletjs.com/examples/wms/wms.html

### Legends

### Customizing colors

TOPICS = (A) Default styles and (B) SLD


SLD standard… which software supports SLD for WMS… and provide an SLD file in the doc that for display in a leaflet window… do something cool with using the live clouds layer with some funky colorscale.

The [OGC Styled Layer Descriptor](https://www.opengeospatial.org/standards/sld) defines an encoding that extends the WMS standard to allow user-defined symbolization and coloring of geographic feature and coverage data.

* Ex. https://geo.weather.gc.ca/geomet-beta?version=1.1.1&service=WMS&request=GetMap&bbox=-180,-90,180,90&layers=GDPS.ETA_TT&srs=EPSG:4326&height=600&width=800&format=png

Simply add this to a regular GetMap request : sld=link_to_sld


---

## Viewing data

### WMS


#### Get raw data on a specific pixel (GetFeatureInfo)

https://geo.weather.gc.ca/geomet/?service=WMS&version=1.1.1&request=GetFeatureInfo&query_layers=GDPS.ETA_TT&info_format=text/plain&x=1&y=1&exceptions=xml&layers=GDPS.ETA_TT&crs=CRS:84&bbox=-73.5,45.6,-73.6,45.4&width=1&height=1

In this example, we can get raw data values of layer GDPS.ETA_TT which correspond to temperature on a specific area determined by the bounding box. In that area, we select pixels (x,y) based on their size (width, height). Note that pixel (0,0) is at the top left.

#### Display legend of a layer (GetLegendGraphic)

GetLegendGraphic request can be found in [GetCapabilities](https://geo.weather.gc.ca/geomet/?version=1.3.0&service=WMS&request=GetCapabilities)

https://geo.weather.gc.ca/geomet/?service=WMS&version=1.1.1&request=GetLegendGraphic&style=TEMPERATURE&layer=GDPS.ETA_TT&format=image/png

In this example, we get the legend for a layer with the specified style, which can be customize using a SLD. If no style is specified, it's the default one. Otherwise, default style can be directly specified with style=DEFAULT

### WFS

#### GetFeature

https://geo.weather.gc.ca/geomet-beta/?version=1.1.0&service=WFS&request=GetFeature&typename=CURRENT_CONDITIONS&SRS=EPSG:4326&BBOX=-73.6,45.4,-73.5,45.6

#### Get description of features in vector layers (DescribeFeatureType)

https://geo.weather.gc.ca/geomet-beta/?version=1.1.0&service=WFS&request=DescribeFeatureType

### WCS

#### Get raw data on a specific area (GetCoverage)

https://geo.weather.gc.ca/geomet-beta/?version=1.0.0&service=WCS&request=GetCoverage&coverage=GDPS.ETA_TT&format=GTiff&bbox=-180,-90,180,90&crs=EPSG:4326&width=800&height=600

In this example, we get raw data on a specified extent for the layer GDPS.ETA_TT which correspond to temperature. In GTiff format, values will be in RGB code, but if format is GEOTIFF_16, it will be the raw values.

#### DescribeCoverage

https://geo.weather.gc.ca/geomet-beta/?version=1.0.0&service=WCS&request=DescribeCoverage&coverage=GDPS.ETA_TT&format=GTiff&bbox=-180,-90,180,90&crs=EPSG:4326&width=800&height=600

This example delivers XML-encoded descriptions of coverage such as their location, type of projection supported, interpolation, etc.

### Use time series

TIME parameter is use to get information on layer on a specific time, multiple time values or time range. In GetCapabilities, information on time can be retrieve on time enabled layers.

Ex. 2016-12-15T12:00:00Z/2016-12-25T12:00:00Z/PT3H that correspond to begin_time/end_time/interval_time

If an incorrect time is specified in a request, it will return an error message. Time parameter must be in ISO-8601.

**Specific time** : https://geo.weather.gc.ca/geomet/?service=WMS&version=1.1.1&request=GetFeatureInfo&query_layers=GDPS.ETA_TT,GDPS.ETA_UU&info_format=text/plain&x=1&y=1&exceptions=xml&layers=GDPS.ETA_TT,GDPS.ETA_UU&crs=CRS:84&bbox=-73.5,45.6,-73.6,45.4&width=1&height=1&time=2016-12-16T12:00:00Z

**Multiple times** : https://geo.weather.gc.ca/geomet/?service=WMS&version=1.1.1&request=GetFeatureInfo&query_layers=GDPS.ETA_TT,GDPS.ETA_UU&info_format=text/plain&x=1&y=1&exceptions=xml&layers=GDPS.ETA_TT,GDPS.ETA_UU&crs=CRS:84&bbox=-73.5,45.6,-73.6,45.4&width=1&height=1&time=2016-12-16T12:00:00Z,2016-12-15T16:00:00Z,2016-12-16T18:00:00Z

**Time range** : https://geo.weather.gc.ca/geomet/?service=WMS&version=1.1.1&request=GetFeatureInfo&query_layers=GDPS.ETA_TT,GDPS.ETA_UU&info_format=text/plain&x=1&y=1&exceptions=xml&layers=GDPS.ETA_TT,GDPS.ETA_UU&crs=CRS:84&bbox=-73.5,45.6,-73.6,45.4&width=1&height=1&time=2016-12-16T12:00:00Z/2016-12-17T12:00:00Z



* Geospatial web services
	* Short description of WMS, WCS, WFS 2/3, SLD (copy from WOUDC)

second group to clean up as well:

* Table of Layer groups (list of first level, e.g. GDPS, GIOPS, radar, AQHI, Citypage, etc) with description, formats available (e.g. WMS: styles, WFS: formats, WCS: formats) as columns... NOT ON A PER LAYER BASIS
	* manually updated table content updates from GeoMet’s GetCapabilities [TO DO, NOT AN ITEM]
	* full list of layers only in get capabilities?
	* add layers by model, layers by type; e.g. wind layers = global, regional, maximum gust, probabilities, and so on

* [Services](#Services)
	* [WMS](#WMS)
	* [WFS](#WFS)
	* [WCS](#WCS)
	* [WPS](#WPS)
    * [SLD](#SLD)
* Link to layer list, give examples of requests and explain query parameters

Salvage content from current GeoMet doc: https://www.ec.gc.ca/meteo-weather/default.asp?lang=En&n=C0D9B3D8-1

## Services

_remove all this?_

In addition to traditional data access mechanisms, GeoMet has made the archive (NOT TRUE) available using geospatial web services adhering to publicly available international standards. Web services are systems designed to support machine to machine interaction over a network, and are typically utilized in a client/server computing environment made available through programmatic access, associated tools and applications.

The GeoMet web services adhere to open standards ratified by the [Open Geospatial Consortium (OGC)](https://www.opengeospatial.org/), and the [International Organization for Standardization (ISO)](https://www.isotc211.org/) which enable interoperability and thus make data easy to discover, access, visualize and integrate. OGC and ISO standards play an important role in [World Meteorological Organization interoperability](https://www.wmo.int/pages/prog/www/WIS/documents/MOAWMO_OGC.pdf) as part of the [WMO Information System](https://www.wmo.int/pages/prog/www/WIS/) and are supported by numerous off the shelf open source or commercial tools.

### WMS
The [OGC Web Map Service](https://www.opengeospatial.org/standards/wms) provides a common interface to visualize geospatial data layers. Typical use of WMS includes simple visualization in web or desktop GIS applications via web friendly image formats such as PNG or JPEG.

Type of request :
* [GetCapabilities](https://geo.weather.gc.ca/geomet/?version=1.3.0&service=WMS&request=GetCapabilities)
* [GetMap for GDPS TT](https://geo.weather.gc.ca/geomet/?service=WMS&version=1.3.0&request=GetMap&bbox=-180,-90,90,180&crs=EPSG:4326&width=800&height=600&layers=GDPS.ETA_TT&style=DEFAULT&FORMAT=image/png)
* [GetMap for CanSIPS TT](https://geo.weather.gc.ca/geomet/?SERVICE=WMS&VERSION=1.3.0&TIME=2019-06-01T00:00:00Z&REFERENCE_TIME=2013-04-01T00:00:00Z&REQUEST=GetMap&BBOX=-90,-180,90,180&CRS=EPSG:4326&WIDTH=1021&HEIGHT=511&LAYERS=CANSIPS.MEM.ETA_TT.05&STYLES=&FORMAT=image/png&DPI=94&MAP_RESOLUTION=94&FORMAT_OPTIONS=dpi:94&TRANSPARENT=TRUE)
* [GetMap for RDPA-ARC PR](https://geo.weather.gc.ca/geomet/?SERVICE=WMS&VERSION=1.3.0&TIME=2018-07-02T18:00:00Z&REQUEST=GetMap&BBOX=17.29939999999999856,-180,90,180&CRS=EPSG:4326&WIDTH=1021&HEIGHT=207&LAYERS=RDPA.ARC_10km.6F_PR&STYLES=&FORMAT=image/png&DPI=94&MAP_RESOLUTION=94&FORMAT_OPTIONS=dpi:94&TRANSPARENT=TRUE)
* [GetFeatureInfo](https://geo.weather.gc.ca/geomet/?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetFeatureInfo&QUERY_LAYERS=GDPS.ETA_TT&INFO_FORMAT=text/plain&X=100&Y=100&EXCEPTIONS=xml&LAYERS=GDPS.ETA_TT&CRS=EPSG:4326&BBOX=-180,-90,180,90&WIDTH=600&HEIGHT=400)
* [GetLegendGraphic](https://geo.weather.gc.ca/geomet/?LANG=EN&SERVICE=WMS&VERSION=1.3.0&REQUEST=GetLegendGraphic&STYLE=TEMPERATURE&LAYER=GDPS.ETA_TT&format=image/png&sld_version=1.1.0)

Version 1.1.1 & 1.3.0 are supported.

#### Styles

Browsing existing styles for a layer: users can use QGIS (free & open source: qgis.org) to view the list and visualize the available "WMS styles" (aka colorramps). In QGIS, menu Layer => Add layer => Add WMS layer, then connect to GeoMet, browse to the radar layer, expand the layer by clicking on the triangle, tadam! Here's all the available styles. There's 6 styles per 1km radar layer at the moment. You can add them all to the map and then toggle them on/off at will to view the differences in the existing styles.

For GetMap requests, simply specify the style by appending &STYLES=

The default style: https://geo.weather.gc.ca/geomet/?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&BBOX=17,-150,70,-50&CRS=EPSG:4326&WIDTH=800&HEIGHT=607&LAYERS=RADAR_1KM_RRAI&STYLES=&FORMAT=image/png

With &STYLES=RADARURPPRECIPR8 : https://geo.weather.gc.ca/geomet/?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&BBOX=17,-150,70,-50&CRS=EPSG:4326&WIDTH=800&HEIGHT=607&LAYERS=RADAR_1KM_RRAI&STYLES=&FORMAT=image/png&STYLES=RADARURPPRECIPR8

Choosing amongst existing styles is done client-side.

### WFS

The [OGC Web Feature Service](https://www.opengeospatial.org/standards/wfs) provides a common interface to access geospatial data. Typical use of WFS includes custom query / raw access to geospatial features. The WOUDC WFS provides archive data in numerous formats, including Extended CSV, KML, CSV, GML, ESRI Shapefile, MapInfo, and GeoJSON.

Type of request :

* [GetCapabilities](https://geo.weather.gc.ca/geomet/?version=1.1.0&service=WFS&request=GetCapabilities)
* [GetFeature](https://geo.weather.gc.ca/geomet-beta/?version=1.1.0&service=WFS&request=GetFeature&typename=CURRENT_CONDITIONS&SRS=EPSG:4326&BBOX=-73.6,45.4,-73.5,45.6)
* [DescribeFeatureType](https://geo.weather.gc.ca/geomet-beta/?version=1.1.0&service=WFS&request=DescribeFeatureType) => this results in an Internal Server Error!

Version 1.0.0 & 1.1.0 are supported.

### WCS

The [OGC Web Coverage Service](https://www.opengeospatial.org/standards/wcs) provides access to coverage data (raw) that is detailed which may be processed (interpolation, resizing, reprojection, etc.). It allows to choose portions of a layer based on spatial constraints and other criteria just like WMS and WFS.

Type of request :
* [GetCapabilities](https://geo.weather.gc.ca/geomet-beta?version=1.0.0&service=WCS&request=GetCapabilities)
* [DescribeCoverage for GDPS TT](https://geo.weather.gc.ca/geomet-beta/?version=1.0.0&service=WCS&request=DescribeCoverage&coverage=GDPS.ETA_TT&format=GTiff&bbox=-180,-90,180,90&crs=EPSG:4326&width=800&height=600)
* [GetCoverage for GDPS TT](https://geo.weather.gc.ca/geomet-beta/?version=1.0.0&service=WCS&request=GetCoverage&coverage=GDPS.ETA_TT&format=GTiff&bbox=-180,-90,180,90&crs=EPSG:4326&width=800&height=600)
* [GetCoverage for RDPS TT](geo.weather.gc.ca/geomet-beta/?SERVICE=wcs&VERSION=1.0.0&REQUEST=GetCoverage&coverage=RDPS.ETA_TT&CRS=EPSG:4326&BBOX=-100,0,-45,80&WIDTH=1300&HEIGHT=1300&FORMAT=GEOTIFF_16)
* [GetCoverage for CanSIPS PN](geo.weather.gc.ca/geomet-beta/?SERVICE=WCS&VERSION=2.0.1&REQUEST=GetCoverage&COVERAGEID=CANSIPS.HIND.MEM.ETA_PN-SLP.01&SUBSETTINGCRS=EPSG:4326&SUBSET=x(-91.58203125000001,-56.42578125000001)&SUBSET=y(30.751277776257812,55.7765730186677)&FORMAT=image/tiff&TIME=2019-06-01T00:00:00Z&REFERENCE_TIME=2018-06-01T00:00:00Z)
* [GetCoverage for RDPA-ARC PR](geo.weather.gc.ca/geomet-beta/?SERVICE=WCS&VERSION=2.0.1&REQUEST=GetCoverage&COVERAGEID=RDPA.ARC_15km.24F_PR&SUBSETTINGCRS=EPSG:4326&SUBSET=x(-154,-49)&SUBSET=y(38,81)&FORMAT=image/tiff&TIME=2018-07-02T18:00:00Z)

Version 1.0.0 and 2.0.1 are supported.

