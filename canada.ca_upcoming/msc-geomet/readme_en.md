[En français](readme_fr.md)

![ECCC logo](../img_eccc-logo.png)

[TOC](../readme_en.md) > MSC GeoMet


MSC GeoMet Web Services
=======================

Short description: MSC GeoMet, Interactively accessing MSC data via geospatial web services

Table of Content
----------------

NEED TO CLEAN UP THIS TOC

* Geospatial web services
	* Short description of WMS, WCS, WFS, SLD (copy from WOUDC)
* Available data
	* Link to layer list, give examples of requests and explain query parameters
	* Table of Layer groups (list of first level, e.g. GDPS, GIOPS, radar, AQHI, Citypage, etc) with description, formats available (e.g. WMS: styles, WFS: formats, WCS: formats) as columns...
* Support
* GeoMet-Info

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
* GeoMet-Info
* Geomet-beta

Salvage content from current GeoMet doc: http://www.ec.gc.ca/meteo-weather/default.asp?lang=En&n=C0D9B3D8-1

## Services

In addition to traditional data access mechanisms, GeoMet has made the archive available using geospatial web services adhering to publically available international standards. Web services are systems designed to support machine to machine interaction over a network, and are typically utilized in a client/server computing environment made available through programmatic access, associated tools and applications.

The GeoMet web services adhere to open standards ratified by the [Open Geospatial Consortium (OGC)](http://www.opengeospatial.org/), and the [International Organization for Standardization (ISO)](http://www.isotc211.org/) which enable interoperability and thus make data easy to discover, access, visualize and integrate. OGC and ISO standards play an important role in [World Meteorological Organization interoperability](http://www.wmo.int/pages/prog/www/WIS/documents/MOAWMO_OGC.pdf) as part of the [WMO Information System](http://www.wmo.int/pages/prog/www/WIS/) and are supported by numerous off the shelf open source or commercial tools.

### WMS
The [OGC Web Map Service](http://www.opengeospatial.org/standards/wms) provides a common interface to visualize geospatial data layers. Typical use of WMS includes simple visualization in web or desktop GIS applications via web friendly image formats such as PNG or JPEG.

Type of request :
* [GetCapabilities](http://geo.weather.gc.ca/geomet/?version=1.3.0&service=WMS&request=GetCapabilities)
* [GetMap for GDPS TT](http://geo.weather.gc.ca/geomet/?service=WMS&version=1.3.0&request=GetMap&bbox=-180,-90,90,180&crs=EPSG:4326&width=800&height=600&layers=GDPS.ETA_TT&style=DEFAULT&FORMAT=image/png)
* [GetMap for CanSIPS TT](http://geo.weather.gc.ca/geomet/?SERVICE=WMS&VERSION=1.3.0&TIME=2019-06-01T00:00:00Z&REFERENCE_TIME=2013-04-01T00:00:00Z&REQUEST=GetMap&BBOX=-90,-180,90,180&CRS=EPSG:4326&WIDTH=1021&HEIGHT=511&LAYERS=CANSIPS.MEM.ETA_TT.05&STYLES=&FORMAT=image/png&DPI=94&MAP_RESOLUTION=94&FORMAT_OPTIONS=dpi:94&TRANSPARENT=TRUE)
* [GetMap for RDPA-ARC PR](http://geo.weather.gc.ca/geomet/?SERVICE=WMS&VERSION=1.3.0&TIME=2018-07-02T18:00:00Z&REQUEST=GetMap&BBOX=17.29939999999999856,-180,90,180&CRS=EPSG:4326&WIDTH=1021&HEIGHT=207&LAYERS=RDPA.ARC_10km.6F_PR&STYLES=&FORMAT=image/png&DPI=94&MAP_RESOLUTION=94&FORMAT_OPTIONS=dpi:94&TRANSPARENT=TRUE)
* [GetFeatureInfo](http://geo.weather.gc.ca/geomet/?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetFeatureInfo&QUERY_LAYERS=GDPS.ETA_TT&INFO_FORMAT=text/plain&X=100&Y=100&EXCEPTIONS=xml&LAYERS=GDPS.ETA_TT&CRS=EPSG:4326&BBOX=-180,-90,180,90&WIDTH=600&HEIGHT=400)
* [GetLegendGraphic](http://geo.weather.gc.ca/geomet/?LANG=EN&SERVICE=WMS&VERSION=1.3.0&REQUEST=GetLegendGraphic&STYLE=TEMPERATURE&LAYER=GDPS.ETA_TT&format=image/png&sld_version=1.1.0)

Version 1.1.1 & 1.3.0 are supported.

#### Styles

Browsing existing styles for a layer: users can use QGIS (free & open source: qgis.org) to view the list and visualize the available "WMS styles" (aka colorramps). In QGIS, menu Layer => Add layer => Add WMS layer, then connect to GeoMet, browse to the radar layer, expand the layer by clicking on the triangle, tadam! Here's all the available styles. There's 6 styles per 1km radar layer at the moment. You can add them all to the map and then toggle them on/off at will to view the differences in the existing styles.

For GetMap requests, simply specify the style by appending &STYLES=

The default style: http://geo.weather.gc.ca/geomet/?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&BBOX=17,-150,70,-50&CRS=EPSG:4326&WIDTH=800&HEIGHT=607&LAYERS=RADAR_1KM_RRAI&STYLES=&FORMAT=image/png

With &STYLE=RADARURPPRECIPR8 : http://geo.weather.gc.ca/geomet/?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&BBOX=17,-150,70,-50&CRS=EPSG:4326&WIDTH=800&HEIGHT=607&LAYERS=RADAR_1KM_RRAI&STYLES=&FORMAT=image/png&STYLES=RADARURPPRECIPR8

Choosing amongst existing styles is done client-side.

### WFS

The [OGC Web Feature Service](http://www.opengeospatial.org/standards/wfs) provides a common interface to access geospatial data. Typical use of WFS includes custom query / raw access to geospatial features. The WOUDC WFS provides archive data in numerous formats, including Extended CSV, KML, CSV, GML, ESRI Shapefile, MapInfo, and GeoJSON.

Type of request :

* [GetCapabilities](http://geo.weather.gc.ca/geomet/?version=1.1.0&service=WFS&request=GetCapabilities)
* [GetFeature](http://geo.weather.gc.ca/geomet-beta/?version=1.1.0&service=WFS&request=GetFeature&typename=CURRENT_CONDITIONS&SRS=EPSG:4326&BBOX=-73.6,45.4,-73.5,45.6)
* [DescribeFeatureType](http://geo.weather.gc.ca/geomet-beta/?version=1.1.0&service=WFS&request=DescribeFeatureType)

Version 1.0.0 & 1.1.0 are supported.

### WCS

The [OGC Web Coverage Service](http://www.opengeospatial.org/standards/wcs) provides access to coverage data (raw) that is detailed which may be processed (interpolation, resizing, reprojection, etc.). It allows to choose portions of a layer based on spatial constraints and other criteria just like WMS and WFS.

Type of request :
* [GetCapabilities](http://geo.weather.gc.ca/geomet-beta?version=1.0.0&service=WCS&request=GetCapabilities)
* [DescribeCoverage for GDPS TT](http://geo.weather.gc.ca/geomet-beta/?version=1.0.0&service=WCS&request=DescribeCoverage&coverage=GDPS.ETA_TT&format=GTiff&bbox=-180,-90,180,90&crs=EPSG:4326&width=800&height=600)
* [GetCoverage for GDPS TT](http://geo.weather.gc.ca/geomet-beta/?version=1.0.0&service=WCS&request=GetCoverage&coverage=GDPS.ETA_TT&format=GTiff&bbox=-180,-90,180,90&crs=EPSG:4326&width=800&height=600)
* [GetCoverage for RDPS TT](geo.weather.gc.ca/geomet-beta/?SERVICE=wcs&VERSION=1.0.0&REQUEST=GetCoverage&coverage=RDPS.ETA_TT&CRS=EPSG:4326&BBOX=-100,0,-45,80&WIDTH=1300&HEIGHT=1300&FORMAT=GEOTIFF_16)
* [GetCoverage for CanSIPS PN](geo.weather.gc.ca/geomet-beta/?SERVICE=WCS&VERSION=2.0.1&REQUEST=GetCoverage&COVERAGEID=CANSIPS.HIND.MEM.ETA_PN-SLP.01&SUBSETTINGCRS=EPSG:4326&SUBSET=x(-91.58203125000001,-56.42578125000001)&SUBSET=y(30.751277776257812,55.7765730186677)&FORMAT=image/tiff&TIME=2019-06-01T00:00:00Z&REFERENCE_TIME=2018-06-01T00:00:00Z)
* [GetCoverage for RDPA-ARC PR](geo.weather.gc.ca/geomet-beta/?SERVICE=WCS&VERSION=2.0.1&REQUEST=GetCoverage&COVERAGEID=RDPA.ARC_15km.24F_PR&SUBSETTINGCRS=EPSG:4326&SUBSET=x(-154,-49)&SUBSET=y(38,81)&FORMAT=image/tiff&TIME=2018-07-02T18:00:00Z)

Version 1.0.0 and 2.0.1 are supported.

### WPS

The [OGC Web Processing Service](http://www.opengeospatial.org/standards/wps) provides a common interface to define rules, inputs, outputs for geospatial processing / calculations. Typical use of WPS includes custom processes (buffer, overlay). It is not implemented yet in GeoMet.

### SLD

The [OGC Styled Layer Descriptor](http://www.opengeospatial.org/standards/sld) defines an encoding that extends the WMS standard to allow user-defined symbolization and coloring of geographic feature and coverage data.

* Ex. http://geo.weather.gc.ca/geomet-beta?version=1.1.1&service=WMS&request=GetMap&bbox=-180,-90,180,90&layers=GDPS.ETA_TT&srs=EPSG:4326&height=600&width=800&format=png

Simply add this to a regular GetMap request : sld=link_to_sld

### Time

* Available timesteps for a layer is provided in the WMS GetCapabilities response
* The TIME and DIM_REFERENCE_TIME parameters should be in the form: &TIME=:YYYY-MM-DDThh:mm:ssZ
* MSC GeoMet supports the OGC Best Practice for using Web Map Services (WMS) with Time-Dependent or Elevation-Dependent Data. Reference document: [http://www.opengis.net/doc/bp/wms-tnz/1.0]
* If no TIME or DIM_REFERENCE_TIME parameter is specified, then the data corresponding to the request time is provided by default
* Layer-specific GetCapabilities: 
 * MSC GeoMet's WMS GetCapabilities response is large given the number of layers available. Users accessing information for a specific layer, such as its currently valid temporal dimensions, can use the "LAYERS=" parameter to access the GetCapabilities information specific to that layer. Note that this feature is an extension to the WMS specification.
 * Example of such a request: http://geo.weather.gc.ca/geomet?service=WMS&version=1.3.0&request=GetCapabilities&layers=RADAR_1KM_RRAI
* Example of requests:
 * [TIME](http://geo.weather.gc.ca/geomet/?service=WMS&version=1.3.0&request=GetMap&bbox=-180,-90,90,180&crs=EPSG:4326&TIME=2018-06-15T12:00:00Z&width=800&height=600&layers=GDPS.ETA_TT&style=DEFAULT&FORMAT=image/png)
 * [REFERENCE_TIME](http://geo.weather.gc.ca/geomet/?service=WMS&version=1.3.0&request=GetMap&bbox=-180,-90,90,180&crs=EPSG:4326&TIME=2018-29-15T12:00:00Z&DIM_REFERENCE_TIME=2018-08-28T00:00:00Z&width=800&height=600&layers=GDPS.ETA_TT&style=DEFAULT&FORMAT=image/png) - this example does not work
* Support of time in off-the-shelf tools:
 * https://openlayers.org/en/latest/examples/wms-time.html
 * http://leafletjs.com/examples/wms/wms.html
 
### Software

See also what's in the how-to and merge with this?
Are provided as a starting point for MSC GeoMet users, we do not endorse nor provide support for any of those software.

QGIS, OpenLayers, Leaflet, [R interface](https://github.com/bcgov/geometr), ArcGIS (time support).