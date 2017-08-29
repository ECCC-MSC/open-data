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

* Services
	* WMS
	* WFS
	* WCS
	* WPS
    * SLD
* Link to layer list, give examples of requests and explain query parameters
* GeoMet-Info
* Geomet-beta

Salvage content from current GeoMet doc: http://www.ec.gc.ca/meteo-weather/default.asp?lang=En&n=C0D9B3D8-1

## Services

In addition to traditional data access mechanisms, GeoMet has made the archive available using geospatial web services adhering to publically available international standards. Web services are systems designed to support machine to machine interaction over a network, and are typically utilized in a client/server computing environment made available through programmatic access, associated tools and applications.

The GeoMet web services adhere to open standards ratified by the Open Geospatial Consortium (OGC) (http://www.opengeospatial.org/), and the International Organization for Standardization (ISO) (http://www.isotc211.org/) which enable interoperability and thus make data easy to discover, access, visualize and integrate. OGC and ISO standards play an important role in World Meteorological Organization interoperability (http://www.wmo.int/pages/prog/www/WIS/documents/MOAWMO_OGC.pdf) as part of the WMO Information System (http://www.wmo.int/pages/prog/www/WIS/) and are supported by numerous off the shelf open source or commercial tools.

### WMS
The OGC Web Map Service (http://www.opengeospatial.org/standards/wms) provides a common interface to visualize geospatial data layers. Typical use of WMS includes simple visualization in web or desktop GIS applications via web friendly image formats such as PNG or JPEG.

Type of request :
* GetCapabilities (http://geo.weather.gc.ca/geomet/?version=1.3.0&service=WMS&request=GetCapabilities)
* GetMap (http://geo.weather.gc.ca/geomet/?service=WMS&version=1.3.0&request=GetMap&bbox=-180,-90,90,180&crs=EPSG:4326&width=800&height=600&layers=GDPS.ETA_TT&style=DEFAULT)
* GetFeatureInfo (http://geo.weather.gc.ca/geomet/?SERVICE=WMS&VERSION=1.1.1&REQUEST=GetFeatureInfo&QUERY_LAYERS=GDPS.ETA_TT&INFO_FORMAT=text/plain&X=1&Y=1&EXCEPTIONS=xml&LAYERS=GDPS.ETA_TT&CRS=CRS:84&BBOX=-73.5,45.6,-73.6,45.4&WIDTH=1&HEIGHT=1)
* GetLegendGraphic (http://geo.weather.gc.ca/geomet//?LANG=E%26SERVICE=WMS%26VERSION=1.1.1%26REQUEST=GetLegendGraphic%26STYLE=TEMPERATURE%26LAYER=GDPS.ETA_TT%26format=image/png)

Version 1.1.1 & 1.3.0 are supported.

### WFS

The OGC Web Feature Service (http://www.opengeospatial.org/standards/wfs) provides a common interface to access geospatial data. Typical use of WFS includes custom query / raw access to geospatial features. The WOUDC WFS provides archive data in numerous formats, including Extended CSV, KML, CSV, GML, ESRI Shapefile, MapInfo, and GeoJSON.

Type of request :

* GetCapabilities (http://geo.weather.gc.ca/geomet/?version=1.1.0&service=WFS&request=GetCapabilities)
* GetFeature (http://geo.weather.gc.ca/geomet-beta/?version=1.1.0&service=WFS&request=GetFeature&typename=CURRENT_CONDITIONS&SRS=EPSG:4326&BBOX=-73.6,45.4,-73.5,45.6)
* DescribeFeatureType (http://geo.weather.gc.ca/geomet-beta/?version=1.1.0&service=WFS&request=DescribeFeatureType)

Version 1.0.0 & 1.1.0 are supported.

### WCS

The OGC Web Coverage Service (http://www.opengeospatial.org/standards/wcs) provides access to coverage data (raw) that is detailed which may be processed (interpolation, resizing, reprojection, etc.). It allows to choose portions of a layer based on spatial constraints and other criteria just like WMS and WFS.

Type of request :
* GetCapabilities (http://geo.weather.gc.ca/geomet-beta?version=1.0.0&service=WCS&request=GetCapabilities)
* DescribeCoverage for GDPS TT (http://geo.weather.gc.ca/geomet-beta/?version=1.0.0&service=WCS&request=DescribeCoverage&coverage=GDPS.ETA_TT&format=GTiff&bbox=-180,-90,180,90&crs=EPSG:4326&width=800&height=600)
* GetCoverage for GDPS TT (http://geo.weather.gc.ca/geomet-beta/?version=1.0.0&service=WCS&request=GetCoverage&coverage=GDPS.ETA_TT&format=GTiff&bbox=-180,-90,180,90&crs=EPSG:4326&width=800&height=600)
* GetCoverage for RDPS TT (http://dd.weather.gc.ca/doc/geo.weather.gc.ca/geomet-beta/?SERVICE=wcs&VERSION=1.0.0&REQUEST=GetCoverage&coverage=RDPS.ETA_TT&CRS=EPSG:4326&BBOX=-100,0,-45,80&WIDTH=1300&HEIGHT=1300&FORMAT=GEOTIFF_16)

Version 1.0.0 and 2.0.1 are supported.

### WPS

The OGC Web Processing Service (http://www.opengeospatial.org/standards/wps) provides a common interface to define rules, inputs, outputs for geospatial processing / calculations. Typical use of WPS includes custom processes (buffer, overlay). It is not implemented yet in GeoMet.

### SLD

The OGC Styled Layer Descriptor (http://www.opengeospatial.org/standards/sld) defines an encoding that extends the WMS standard to allow user-defined symbolization and coloring of geographic feature and coverage data.

* Ex. http://geo.weather.gc.ca/geomet-beta?version=1.1.1&service=WMS&request=GetMap&bbox=-180,-90,180,90&layers=GDPS.ETA_TT&srs=EPSG:4326&height=600&width=800&format=png

Simply add this to a regular GetMap request : sld=link_to_sld

### Time

* mention TIME=
* mention the best practices and REFERENCE_TIME for model runs
* examples
 * https://openlayers.org/en/latest/examples/wms-time.html
 * http://leafletjs.com/examples/wms/wms.html