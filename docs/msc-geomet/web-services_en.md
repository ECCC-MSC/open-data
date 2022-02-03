[En français](web-services_fr.md)

![ECCC logo](../img_eccc-logo.png)

[TOC](../readme_en.md) > [MSC GeoMet](readme_en.md) > Technical documentation

# Table of contents
- [Web Map Service (WMS)](#web-map-service-wms)
    * [WMS GetCapabilities](#wms-getcapabilities)
    * [WMS GetMap](#wms-getmap)
    * [WMS GetFeatureInfo](#wms-getfeatureinfo)
    * [WMS GetLegendGraphic](#wms-getlegendgraphic)
    * [Handling Time](#handling-time)
    * [Handling Styles](#handling-styles)
- [Web Coverage Service (WCS)](#web-coverage-service-wcs)
    * [WCS GetCapabilities](#wcs-getcapabilities)
    * [WCS DescribeCoverage](#wcs-describecoverage)
    * [WCS GetCoverage](#wcs-getcoverage)
    * [Handling Time](#wcstime)
    * [Usage Example](#usage-example)
- [OGC API - Features (WFS 3)](#ogc-api-features)

# Geospatial web services

Web services are protocols designed to support machine to machine interaction over a network, and are typically utilized in a client/server computing environment made available through programmatic access, associated tools and applications.

The MSC GeoMet web services adhere to open standards ratified by the [Open Geospatial Consortium (OGC)](https://www.opengeospatial.org/), and the [International Organization for Standardization (ISO)](https://www.isotc211.org/) which enable interoperability and thus make data easy to discover, access, visualize and integrate. OGC and ISO standards play an important role in [World Meteorological Organization interoperability](https://www.wmo.int/pages/prog/www/WIS/documents/MOAWMO_OGC.pdf) as part of the [WMO Information System](https://www.wmo.int/pages/prog/www/WIS/) and are supported by numerous off the shelf open source or commercial tools.

The following OGC web services are supported by MSC GeoMet:

* Web Map Service (WMS)
* Web Coverage Service (WCS)
* OGC API - Features (WFS 3)

## Web Map Service (WMS)

Requests with the [OGC Web Map Service (WMS)](https://www.opengeospatial.org/standards/wms) standard mainly enable a client to retrieve geospatial data as maps. WMS requests are made over the internet (HTTP) and are primarily used to retrieve an image (e.g. JPEG, PNG) of geospatial data for a given area of interest. 

The Web Map Service allows for several different types of request types, each of which are described in further detail below.

### WMS GetCapabilities

A WMS GetCapabilities request allows the client to retrieve an XML document that contains metadata describing the service. This document contains information relating to the supported request types, supported coordinate reference systems, and most importantly, the list of available layers (data). 

A WMS GetCapabilities request is comprised of the following parameters:


| Required parameters                 | Definition |
| ------------------------- | ---------- |
| SERVICE         | The service the client is requesting. In this case, `wms`|
| VERSION         | The version of the service the client is requesting. We recommend using the latest WMS version `1.3.0`|
| REQUEST         | The request type. In this case, `GetCapabilities`|

| Optional parameter                | Definition |
| ------------------------- | ---------- |
| LAYER         | A vendor extension that allows a client to filter the GetCapabilities document for a single specific layer. This greatly reduces the size of the returned XML document|
| LANG          | A vendor extension that allows a client to display the GetCapabilities document in English(en) or French(fr). Defaults to English if the parameter is not included in the request|

A WMS GetCapabilities request to GeoMet-Weather is then be constructed like this:

[https://geo.weather.gc.ca/geomet/?service=WMS&version=1.3.0&request=GetCapabilities](https://geo.weather.gc.ca/geomet/?lang=en&service=WMS&version=1.3.0&request=GetCapabilities)

Each layer defined in the WMS GetCapabilities XML document has information relating to the layer's name and title, geographic extent, time extent, and available styles.

### WMS GetMap

A WMS GetMap request allows the client to retrieve a map image (JPEG, PNG, etc.) for a given layer within a defined area. A GetMap request is composed of several parameters whose value determine the layer requested, its style, coordinate reference system, the timestep, in addition to the properties of the returned image. The [WMS GetCapabilities request](#getcapabilities) can assist the client in determining the values for several of these parameters.


| Required parameters                 | Definition |
| ------------------------- | ---------- |
| SERVICE         | The service the client is requesting. In this case, `wms`.|
| VERSION         | The version of the service the client is requesting. We recommend using the latest wms version `1.3.0`.|
| REQUEST         | The request type. In this case, `GetMap`.|
| LAYERS          | The name of the layer used to create the image. The name of the layer can be retrieved using a [WMS GetCapabilities](#getcapabilities) request. MSC GeoMet currently supports only a single value for the GetMap LAYERS parameter. This will be improved in a future version to support multiple layers as per OGC WMS 1.3.0.|
| STYLES          | Styles with which to display the layer. If this parameter is not specified, the default layer style will be used for rendering.
| CRS (version 1.3.0) or SRS (version 1.1.0) | The coordinate reference system (CRS) used to create the map image. **Be careful, this parameter name differs depending on the WMS version specified in the VERSION parameter**.|
| BBOX            | The bounding box of the requested image. Coordinates should be in the units of the CRS/SRS. If using the WMS 1.3.0 specification *and the EPSG:4326* these values are: `minY,minX,maxY,maxX`. In WMS 1.3.0, the axis order depends on the projection. If the request uses the WMS 1.1.1 specification, these values are: `minX,minY,maxX,maxY`.|
| FORMAT          | The file format desired for the requested image. Accepted values for this parameter are: `image/png` or `image/jpeg`. Images in the PNG format support transparency, while images in the JPEG format will be smaller in size|
| HEIGHT          | The height in pixels of the returned image.|
| WIDTH           | The width in pixels of the returned image.|

| Optional parameters                 | Definition |
| ------------------------- | ---------- |
| TIME            | The date and time used to generate the requested image. The format must respect ISO8601. For more information regarding managing time in WMS requests, see the [WMS Handling Time](#handling-time) section.|
| DIM_REFERENCE_TIME  | The time of the weather model run to used to generate the requested image. For more information regarding managing time in WMS requests, see the [WMS Handling Time](#handling-time) section.|

A GetMap request for the Global Deterministic Prediction System's air temperature layer (GDPS.ETA_TT) would look like this:

```
https://geo.weather.gc.ca/geomet?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&BBOX=-90,-180,90,180
&CRS=EPSG:4326&WIDTH=600&HEIGHT=301&LAYERS=GDPS.ETA_TT&FORMAT=image/png
```

And returns:

![Global Deterministic Prediction System (GDPS) surface temperature](https://geo.weather.gc.ca/geomet?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&BBOX=-90,-180,90,180&CRS=EPSG:4326&WIDTH=600&HEIGHT=301&LAYERS=GDPS.ETA_TT&FORMAT=image/png) 

### WMS GetFeatureInfo

A WMS GetFeatureInfo request retrieves raw data for a given geographic location. The GetFeatureInfo request parameters resemble those of a GetMap request but also include three new required parameters: `I`, `J` and `QUERY_LAYERS`. These parameters represent the horizontal and vertical placement of the pixel to query in the map image and the name of the layers to query.


| Required parameters                 | Definition |
| ------------------------- | ---------- |
| SERVICE         | The service the client is requesting. In this case, `wms`|
| VERSION         | The version of the service the client is requesting. We recommend using the latest wms version `1.3.0`|
| REQUEST         | The request type. In this case, `GetFeatureInfo`.|
| LAYERS          | The name of the layer(s) used to query. The name of the layer can be retrieved using a [WMS GetCapabilities](#getcapabilities) request.|
| CRS (version 1.3.0) or SRS (WMS version 1.1.0) | The coordinate reference system (CRS) used to create the map image. **Be careful, this parameter name differs depending on the version specified in the VERSION parameter**.|
| BBOX            | The bounding box of the requested image. Coordinates should be in the units of the CRS/SRS. If using the WMS 1.3.0 specification *and the EPSG:4326* these values are: `minY,minX,maxY,maxX`. If the request uses the WMS 1.1.1 specification or any other CRS, these values are: `minX,minY,maxX,maxY`. The request's bounding box must cover a part of the request layer's geographic extent.|
| FORMAT          | The file format desired for the requested image. Accepted values for this parameter are: `image/png` or `image/jpeg`. Images in the PNG format support transparency, while images in the JPEG format are smaller in size|
| HEIGHT          | The height in pixels of the associated image|
| WIDTH           | The width in pixels of the associated image|
| I (WMS version 1.3.0) or X (WMS version 1.1.0) | The horizontal coordinate of the pixel to query|
| J (WMS version 1.3.0) or Y (WMS version 1.1.0)  | The vertical coordinate of the pixel to query|
| QUERY_LAYERS    | The name of layers to query (comma-separated)|

| Optional parameters                 | Definition |
| ------------------------- | ---------- |
| INFO_FORMAT     | The format of the data returned by the query. Accepted values for this parameter are: `text/plain` (default), `application/json` or  `application/vnd.ogc.gml`|
| FEATURE_COUNT   | The amount of features returned by the request.|
| TIME            | The date and time used to generate the requested image. The format must respect . For more information regarding managing time in WMS requests, see the [WMS Handling Time](#handling-time) section.|
| DIM_REFERENCE_TIME  | The time of the weather model run to used to generate the requested image. For more information regarding managing time in WMS requests, see the [WMS Handling Time](#handling-time) section.|

A GetFeatureInfo request for the same image requested in the GetMap example above would look like this:

```
https://geo.weather.gc.ca/geomet?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetFeatureInfo&BBOX=45,-75,45.5,-74.5
&CRS=EPSG:4326&WIDTH=10&HEIGHT=10&LAYERS=GDPS.ETA_TT&INFO_FORMAT=application/json&QUERY_LAYERS=GDPS.ETA_TT&I=5&J=5
```

### WMS GetLegendGraphic

A WMS GetLegendGraphic request returns an image of the legend in the style requested by the user. The simplest way to access a layer's legend for a given style is to consult the WMS GetCapabilities document for the layer in question. All available layer styles are listed within the layer definition and the `<OnlineResource>` tag will contain a WMS GetLegendGraphic URL. 

For example, the GDPS air temperature layer (GPDS.ETA_TT) has several styles defined in the WMS GetCapabilties document. Requesting the `TEMPERATURE-LINEAR` style using the GetLegendGraphic request contained in the `<OnlineResource>` tag returns the legend for this style:

![TEMPERATURE-LINEAR GetLegendGraphic Example](https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=GDPS.ETA_TT&format=image/png&STYLE=TEMPERATURE-LINEAR)


| Required parameters                 | Definition |
| ------------------------- | ---------- |
| SERVICE         | The service the client is requesting. In this case, `wms`|
| VERSION         | The version of the service the client is requesting. We recommend using the latest wms version `1.3.0`|
| REQUEST         | The request type. In this case, `GetLegendGraphic`|
| LAYER           | The name of the layer for which the legend is requested. The name of the layer can be retrieved using a [WMS GetCapabilities](#getcapabilities) request|
| FORMAT          | The file format desired for the requested image. Accepted values for this parameter are: `image/png` or `image/jpeg`|
| SLD_VERSION     | The SLD document version. We recommend using version `1.1.0`|

| Optional parameters                | Definition |
| ------------------------- | ---------- |
| STYLE           | The name of the style used to create the legend image. The name individual layer styles can be retrieved using a [WMS GetCapabilities](#getcapabilities) request. If this parameter is not specified a request will return the layer's default style. Note: Make sure to type the singular form of this parameter in the `GetLegendGraphic` request and not the plural form (i.e. `STYLES`), because it will output the layer's default style instead of the requested style.|
| SLD             | Specifies that the legend should be created with an external SLD document. See the [Handing Styles](#handling-styles) for further information.|
| SLD_BODY        | Allows the user to include an SLD document directly in the request URL.|
| LANG          | A vendor extension that allows a client to display the legend in English(en) or French(fr). Defaults to English if the parameter is not included in the request|

A sample GetLegendGraphic request for the Global Deterministic Wave Prediction System's winds layer (GDWPS.UU.1h) would look like this:

```
https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0
&layer=GDWPS.UU.1h&format=image/png&STYLE=WINDARROW
```

And returns:

![GDWPS Wind Arrow Style Example](https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=GDWPS.UU.1h&format=image/png&STYLE=WINDARROW)

### Handling time

Given the importance of temporal dimension for weather data, it is important for users to understand how MSC GeoMet handles time in WMS requests. By default, if no `TIME` or `DIM_REFERENCE_TIME` parameters are passed in the request, MSC GeoMet will return the closest time interval available for the nearest past model run.

If the client desires to make a request for another date and time, the `TIME` or `DIM_REFERENCE_TIME` can be used in both GetMap and GetFeatureInfo requests. Date and times must adhere to the ISO8601 standard and are always in UTC (Coordinate Universal Time).

To make a request for a specific time and/or model run, a client must first determine the available model runs and time intervals. This information is available in the layer's `<Dimension>` tags in the WMS GetCapabilities document.

For example, the Global Deterministic Prediction System's air temperature layer (GDPS.ETA_TT) time dimensions resemble:

```xml
<Dimension name="time" units="ISO8601" default="2019-06-12T15:00:00Z" 
nearestValue="0">2019-06-12T00:00:00Z/2019-06-22T00:00:00Z/PT3H</Dimension>

<Dimension name="reference_time" units="ISO8601" default="2019-06-12T00:00:00Z" 
multipleValues="1" nearestValue="0">2019-06-11T00:00:00Z/2019-06-12T00:00:00Z/PT12H</Dimension>
```

The first `<Dimension>` tag represents the time intervals available for this layer. The `default` attribute is the time value set if no `TIME` parameter was included in the request. The tag value (i.e `2019-06-12T00:00:00Z/2019-06-22T00:00:00Z/PT3H`) informs the client of the available datetime values. At the time the GetCapabilities request was made, a client could request a map  (GetMap) or data (GetFeatureInfo) for any time between 2019-06-12T00:00:00Z and 2019-06-22T00:00:00Z at 3 hour intervals (PT3H).

The second `<Dimension>` tag represents the available model runs for the layer. The `default` attribute is the start time of the model run for the nearest past model run. The tag value informs the client of the available model run times for this layer. In this case, model runs are available every 12 hour (PT12H) between `2019-06-11T00:00:00Z` and `2019-06-12T00:00:00Z` (inclusive).

Given this information, a client could make a GetMap image request for the GDPS air temperature layer for 12:00:00 UTC on June 21st 2019 using the most recent model run (2019-06-12T00:00:00Z) as the data source. The request would look like this:

```
https://geo.weather.gc.ca/geomet?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&BBOX=-90,-180,90,180
&CRS=EPSG:4326&WIDTH=600&HEIGHT=301&LAYERS=GDPS.ETA_TT&FORMAT=image/png
&TIME=2019-06-21T12:00:00Z&DIM_REFERENCE_TIME=2019-06-12T00:00:00Z
```

Note that queries with time ranges or multiple time values are not currently supported on GeoMet for both `TIME` or `DIM_REFERENCE_TIME` parameters. Only single time queries are supported.

#### Time handling differences between GeoMet-Weather and GeoMet-Climate

It is important to mention that time is not handled in the same manner between GeoMet-Weather and GeoMet-Climate due to the different nature of the underlying data.

In Geomet-Climate, time intervals are either yearly (YYYY) or monthly (YYYY-MM) depending on the queried layer. A WMS GetCapabilities request to GeoMet-Climate allows the client to properly identify the time dimension for a given layer.

For example, let's take a look at the [CMIP5 Monthly ensembles of Wind Speed projections (5th percentile)](https://geo.weather.gc.ca/geomet-climate?lang=en&service=WMS&version=1.3.0&request=GetCapabilities&Layer=CMIP5.SFCWIND.RCP26.ENS.ABS_PCTL5) layer's `<Dimension>` tag:

```xml
<Dimension name="time" units="ISO8601" default="2100-12" nearestValue="0">2006-01/2100-12/P1M</Dimension>
```

A successful WMS GetMap request with a defined `TIME` parameter would need to have a value between `2006-01` and `2100-12`.

### Handling Styles

The graphical representation of information and data can have a significant impact on the way data is interpreted by an end-user. MSC GeoMet often provides several different graphical representations for a single layer. The client can choose to display the data using the style most appropriate for their use case.

Using the `STYLE` parameter in both WMS GetMap and WMS GetFeatureInfo requests, a client can specify the style they choose to apply to the underlying data. Available styles for any given layer are described in the WMS GetCapabilities document.

Below are two examples of GetMap requests for the Regional Deterministic Precipitation Analysis' quantity of precipitation layer (RDPA.24F_PR) that each specify a different `STYLE` parameter value to render the returned map.

RDPA.24F_PR with CAPA24-LINEAR style:

```
https://geo.weather.gc.ca/geomet?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&LAYERS=RDPA.24F_PR
&STYLES=CAPA24-LINEAR&CRS=EPSG:4326&BBOX=35,-150,85,-45&WIDTH=600&HEIGHT=400&FORMAT=image/png
```

![RDPA.24F_PR with CAPA24-LINEAR style](https://geo.weather.gc.ca/geomet?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&LAYERS=RDPA.24F_PR&STYLES=CAPA24-LINEAR&CRS=EPSG:4326&BBOX=35,-150,85,-45&WIDTH=600&HEIGHT=400&FORMAT=image/png)

RDPA.24F_PR with RDPA-WXO style:

```
https://geo.weather.gc.ca/geomet?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&LAYERS=RDPA.24F_PR
&STYLES=RDPA-WXO&CRS=EPSG:4326&BBOX=35,-150,85,-45&WIDTH=600&HEIGHT=400&FORMAT=image/png
```

![RDPA.24F_PR with CAPA24-LINEAR style](https://geo.weather.gc.ca/geomet?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&LAYERS=RDPA.24F_PR&STYLES=RDPA-WXO&CRS=EPSG:4326&BBOX=35,-150,85,-45&WIDTH=600&HEIGHT=400&FORMAT=image/png)

Users can also choose to apply their own styles either by pointing to
an external style using a [OGC Styled Layer Descriptor (SLD)](https://www.opengeospatial.org/standards/sld) document in the `SLD` parameter or by entering the SLD document directly into the `SLD_BODY` parameter. Note that the `SLD_BODY` definition must be entirely encoded using the URL encoding.

```
https://geo.weather.gc.ca/geomet?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&LAYERS=GDPS.ETA_NT
&STYLES=&CRS=EPSG:4326&BBOX=35,-150,85,-45&WIDTH=1800&HEIGHT=1200&FORMAT=image/png
&SLD_BODY=%22%3C%3Fxml%20version%3D%221.0%22%20encoding%3D%22UTF-8%22%3F%3E%20%3C
StyledLayerDescriptor%20version%3D%221.0.0%22%20xmlns%3D%22http%3A%2F%2Fwww.opengis.net
%2Fsld%22%20xmlns%3Aogc%3D%22http%3A%2F%2Fwww.opengis.net%2Fogc%22%20xmlns%3Axlink%3D%22
http%3A%2F%2Fwww.w3.org%2F1999%2Fxlink%22%20xmlns%3Axsi%3D%22http%3A%2F%2Fwww.w3.org%2F
2001%2FXMLSchema-instance%22%20xsi%3AschemaLocation%3D%22http%3A%2F%2Fwww.opengis.net%2Fsld
%20http%3A%2F%2Fschemas.opengis.net%2Fsld%2F1.0.0%2FStyledLayerDescriptor.xsd%22%3E%20%3C
NamedLayer%3E%20%3Cse%3AName%3EGDPS.ETA_NT%3C%2Fse%3AName%3E%20%3CUserStyle%3E%20%3CTitle
%3ETEST%3C%2FTitle%3E%20%3Cse%3AFeatureTypeStyle%3E%20%3Cse%3ARule%3E%20%3Cse%3A
RasterSymbolizer%3E%20%3Cse%3AOpacity%3E1.0%3C%2Fse%3AOpacity%3E%20%3CColorMap%3E%20%3C
ColorMapEntry%20color%3D%22%238cff66%22%20quantity%3D%220%22%2F%3E%20%3C
ColorMapEntry%20color%3D%22%23ffff00%22%20quantity%3D%2225%22%2F%3E%20%3C
ColorMapEntry%20color%3D%22%23b38600%22%20quantity%3D%2250%22%2F%3E%20%3C
ColorMapEntry%20color%3D%22%23cc0000%22%20quantity%3D%2275%22%2F%3E%20%3C
ColorMapEntry%20color%3D%22%234d0000%22%20quantity%3D%22100%22%2F%3E%20%3C%2FColorMap%3E
%20%3C%2Fse%3ARasterSymbolizer%3E%20%3C%2Fse%3ARule%3E%20%3C%2Fse%3AFeatureTypeStyle%3E
%20%3C%2FUserStyle%3E%20%3C%2FNamedLayer%3E%20%3C%2FStyledLayerDescriptor%3E%0A
```
![GDPS layer with a custom user-provided SLD style](https://geo.weather.gc.ca/geomet?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&LAYERS=GDPS.ETA_NT&STYLES=&CRS=EPSG:4326&BBOX=35,-150,85,-45&WIDTH=1800&HEIGHT=1200&FORMAT=image/png&SLD_BODY=%22%3C%3Fxml%20version%3D%221.0%22%20encoding%3D%22UTF-8%22%3F%3E%20%3CStyledLayerDescriptor%20version%3D%221.0.0%22%20xmlns%3D%22http%3A%2F%2Fwww.opengis.net%2Fsld%22%20xmlns%3Aogc%3D%22http%3A%2F%2Fwww.opengis.net%2Fogc%22%20xmlns%3Axlink%3D%22http%3A%2F%2Fwww.w3.org%2F1999%2Fxlink%22%20xmlns%3Axsi%3D%22http%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema-instance%22%20xsi%3AschemaLocation%3D%22http%3A%2F%2Fwww.opengis.net%2Fsld%20http%3A%2F%2Fschemas.opengis.net%2Fsld%2F1.0.0%2FStyledLayerDescriptor.xsd%22%3E%20%3CNamedLayer%3E%20%3Cse%3AName%3EGDPS.ETA_NT%3C%2Fse%3AName%3E%20%3CUserStyle%3E%20%3CTitle%3ETEST%3C%2FTitle%3E%20%3Cse%3AFeatureTypeStyle%3E%20%3Cse%3ARule%3E%20%3Cse%3ARasterSymbolizer%3E%20%3Cse%3AOpacity%3E1.0%3C%2Fse%3AOpacity%3E%20%3CColorMap%3E%20%3CColorMapEntry%20color%3D%22%238cff66%22%20quantity%3D%220%22%2F%3E%20%3CColorMapEntry%20color%3D%22%23ffff00%22%20quantity%3D%2225%22%2F%3E%20%3CColorMapEntry%20color%3D%22%23b38600%22%20quantity%3D%2250%22%2F%3E%20%3CColorMapEntry%20color%3D%22%23cc0000%22%20quantity%3D%2275%22%2F%3E%20%3CColorMapEntry%20color%3D%22%234d0000%22%20quantity%3D%22100%22%2F%3E%20%3C%2FColorMap%3E%20%3C%2Fse%3ARasterSymbolizer%3E%20%3C%2Fse%3ARule%3E%20%3C%2Fse%3AFeatureTypeStyle%3E%20%3C%2FUserStyle%3E%20%3C%2FNamedLayer%3E%20%3C%2FStyledLayerDescriptor%3E%0A)


## Web Coverage Service (WCS)

The [OGC Web Coverage Service](https://www.opengeospatial.org/standards/wcs) requests enable a client to retrieve coverage information from a geospatial data for a given area of interest. WCS requests are made over the internet (HTTP) and give the user more flexibility when requesting information about the coverage of a layer compared with the more traditional way of downloading of flat files. The Web Coverage Service allows for several different types of requests, each of which are described in further detail below.

Note that only the WCS 2.0.1 version is currently supported by the GeoMet services. We invite users to use exclusively version 2.0.1 of the WCS standard. Also, note that WCS 2.0.1 is not supported in QGIS and ArcGIS.
 
### WCS GetCapabilities

A WCS GetCapabilities request allows the client to retrieve an XML document that contains metadata describing the service. This document contains information relating to the supported request types, supported coordinate reference systems, and most importantly, the layers (data) for which clients can request raw data.

A GetCapabilities request is comprised of the following parameters:

| Required parameters       | Definition |
| ------------------------- | ---------- |
| SERVICE      | The service the client is requesting. In this case, `wcs`|
| VERSION      | The version of the service the client is requesting. We recommend using the supported version, WCS version `2.0.1`|
| REQUEST      | The request type. In this case, `GetCapabilities`|

| Optional parameter        | Definition |
| ------------------------- | ---------- |
| COVERAGEID                | A vendor extension that allows a client to filter the GetCapabilities document for a single named layer. This greatly reduces the size of the returned XML document|
| LANG          | A vendor extension that allows a client to display the GetCapabilities document in English(en) or French(fr). Defaults to English if the parameter is not included in the request|


A WCS GetCapabilities request to MSC GeoMet would then be constructed
like this:

[https://geo.weather.gc.ca/geomet?SERVICE=WCS&VERSION=2.0.1&REQUEST=GetCapabilities](https://geo.weather.gc.ca/geomet?SERVICE=WCS&VERSION=2.0.1&REQUEST=GetCapabilities)
 
The GetCapabilities document will have information relating to the service's name and title, geographic extent, available layers and available format.
 
### WCS DescribeCoverage

A WCS DescribeCoverage request allows the user to access more information about a given layer than using the [WCS GetCapabilities](#wcsgetcap). Information in the DescribeCoverage request includes: extent, CRS, available format


| Required parameters       | Definition |
| ------------------------- | ---------- |
| SERVICE      | The service the client is requesting. In this case, `wcs`.|
| VERSION      | The version of the service the client is requesting. We recommend using the latest wms version `2.0.1`|
| REQUEST      | The request type. In this case, `DescribeCoverage`.|
| COVERAGEID   | The name of the layer for which to return the metadata. The name of the layer can be retrieved using a [WCS GetCapabilities](#wcsgetcap) request|

A WCS DescribeCoverage request to GeoMet-Weather for the GDPS.ETA_TT layer would then be constructed like this:

[https://geo.weather.gc.ca/geomet?SERVICE=WCS&VERSION=2.0.1&REQUEST=DescribeCoverage&COVERAGEID=GDPS.ETA_TT](https://geo.weather.gc.ca/geomet?SERVICE=WCS&VERSION=2.0.1&REQUEST=DescribeCoverage&COVERAGEID=GDPS.ETA_TT)

### WCS GetCoverage

A WCS GetCoverage request is used to retrieve the actual coverage information (raw data). The most interesting aspect for a user is to be able to request a subdomain of a layer in the projection he wants and in the format he wants with the possibility to obtain the layer in a different spatial resolution and file format from the original one.

| Required parameters       | Definition |
| ------------------------- | ---------- |
| SERVICE      | The service the client is requesting. In this case, `wcs`.|
| VERSION      | The version of the service the client is requesting. We recommend using the latest wms version `2.0.1`|
| REQUEST      | The request type. In this case, `GetCoverage`.|
| COVERAGEID   | The name of the layer for which to return the coverage information.|
| FORMAT       | The file format desired for the requested coverage. Accepted values for this parameter are: `image/tiff` (GeoTIFF) or `image/netcdf` (NetCDF).|

| Optional parameter        | Definition |
| ------------------------- | ---------- |
|SUBSETTINGCRS     | The coordinate reference system (CRS) used to request the coverage layer to the server|
|OUTPUTCRS         | The coordinate reference system (CRS) used to return the coverage layer to the user. This parameter can be different from `SUBSETTINGCRS`. Note: The use of this parameter is **strongly recommended** to guarantee accuracy for `WCS GetCoverage` responses.|
|SUBSET=axis()     | The bounding box of the requested coverage per axis. One can use one of the recognize axis sub-parameter:  `x`, `xaxis`, `x-axis`, `x_axis`, `long`, `long_axis`, `long-axis`, `lon`, `lon_axis`, `lon-axis`, `y`, `yaxis`, `y-axis`, `y_axis`, `lat`, `lat_axis` and `lat-axis`. Coordinates should be in the units of the SUBSETTINGCRS. The request's subset must cover a part of the request layer's geographic extent|
|RESOLUTION=axis() | Resolution (pixel/unit) per axis of the returned coverage to the user. If none is set, the coverage resolution returned might not be the one of the original data, thus it is recommended to specify the spatial resolution in the request. Note that `RESOLUTION` and `SIZE` are mutually exclusive on one axis and should never be used for the same axis in the same request|
|SIZE=axis()       | Size (pixel) per axis of the returned coverage to the user. If none is set, the coverage size returned might not be the one of the original data, thus it is recommended to specify the spatial resolution in the request. Note that `RESOLUTION` and `SIZE` are mutually exclusive on one axis and should never be used for the same axis in the same request|
|INTERPOLATION     | Interpolation method used for the requested coverage when a rescaling is needed. Three method can be used: `NEAREST`, `BILINEAR`, `AVERAGE`. If none is specified, default is `NEAREST`|
|RANGESUBSET       | This parameter allows the user to specify a band of a coverage layer to be returned. Either the band name or the band number can be used|
|TIME              | The date and time associated to the requested coverage. The format must respect the ISO8601 standard. For more information regarding managing time in WCS requests, see the [WCS Handling Time](#wcstime) section|
|DIM_REFERENCE_TIME| The time of the weather model run (when available) to use to generate the requested coverage. The format must respect the ISO8601 standard. For more information regarding managing time in WCS requests, see the [WCS Handling Time](#wcstime) section|

A WCS GetCoverage request to MSC GeoMet for the GDPS.ETA_TT layer could then be constructed
like this: 
[https://geo.weather.gc.ca/geomet?SERVICE=WCS&VERSION=2.0.1&REQUEST=GetCoverage&COVERAGEID=GDPS.ETA_TT&SUBSETTINGCRS=EPSG:4326&SUBSET=x(-120,-85)&SUBSET=y(48,66)&RESOLUTION=x(0.24)&RESOLUTION=y(0.24)&FORMAT=image/tiff](https://geo.weather.gc.ca/geomet?SERVICE=WCS&VERSION=2.0.1&REQUEST=GetCoverage&COVERAGEID=GDPS.ETA_TT&SUBSETTINGCRS=EPSG:4326&SUBSET=x(-120,-85)&SUBSET=y(48,66)&RESOLUTION=x(0.24)&RESOLUTION=y(0.24)&FORMAT=image/tiff)

### <a name="wcstime"></a>Handling time

Given the important temporal dimension of weather data, it is important for users to understand how MSC GeoMet handles time in WCS requests. By default, if no `TIME` or `DIM_REFERENCE_TIME` parameters are passed in the request, MSC GeoMet will, by default, return the closest time interval available for the latest model run.

If the user wants to make a request for another date and time, the `TIME` or `DIM_REFERENCE_TIME` can be used in a WCS GetCoverage request. Date and times must adhere to the ISO8601 standard and are always in UTC (Coordinate Universal Time).

#### GeoMet-Climate

GeoMet-Climate's WCS service does not support request with `TIME` or `DIM_REFERENCE_TIME`. Instead, the WCS time information is stored in different bands, each one representing a particular timestamp. This means that a user will need the `RANGESUBSET` parameter to access the desired time coverage.

The name of the different bands can be retrieved from the DescribeCoverage request. Here is an example using a GeoMet-Climate layer (DCS.TM.RCP26.YEAR.ANO_PCTL50):

```
https://geo.weather.gc.ca/geomet-climate?SERVICE=WCS&VERSION=2.0.1
&REQUEST=DescribeCoverage&COVERAGEID=DCS.TM.RCP26.YEAR.ANO_PCTL50
```

```xml
...
<swe:field name="B2006">
    <swe:Quantity>
        <swe:nilValues/>
        <swe:uom code="W.m-2.Sr-1"/>
        <swe:constraint>
            <swe:AllowedValues>
                <swe:interval>-3.4028e+38 3.4028e+38</swe:interval>
                <swe:significantFigures>12</swe:significantFigures>
            </swe:AllowedValues>
        </swe:constraint>
    </swe:Quantity>
</swe:field>
<swe:field name="B2007">
    <swe:Quantity>
        <swe:nilValues/>
        <swe:uom code="W.m-2.Sr-1"/>
        <swe:constraint>
            <swe:AllowedValues>
                <swe:interval>-3.4028e+38 3.4028e+38</swe:interval>
                <swe:significantFigures>12</swe:significantFigures>
            </swe:AllowedValues>
        </swe:constraint>
    </swe:Quantity>
</swe:field>
<swe:field name="B2008">
...
```

In this example, the `field` keys give the user the available band names. In GeoMet-Climate, the bands will always use the same nomenclature which is: `B` followed by one of the two ISO8601 time format supported: `YYYY` for annual time interval and `YYYY-MM` for monthly time interval.

In GeoMet-Climate one can either request coverage for a single time step or for a time range:

* Single time step: `RANGESUBSET=B2015`
* Time range: `RANGESUBSET=B2015:B2019`

Note that a user cannot, in a single GetCoverage request, ask for more than 256 bands.

#### GeoMet-Weather

Please refer to the previous [WMS Handling Time](#handling-time) section, as for GeoMet-Weather,
the `TIME` and `DIM_REFERENCE_TIME` usage is the same.

Note that the layers time metadata are not available in the WCS GetCapabilities or the WCS DescribeCoverage. The time metadata can only be access through the WMS GetCapabilities.

### Usage example

GeoMet-Climate and GeoMet-Weather WCS are used through the [Climate data extraction tool](https://climate-change.canada.ca/climate-data/#/) of the [Canadian Centre for Climate Services portal](https://www.canada.ca/en/environment-climate-change/services/climate-change/canadian-centre-climate-services.html).

One can select a variable, region of interest, temporal information and output format on the extraction tool to retrieve the raw coverage information.

## OGC API - Features

The [OGC API - Features](https://github.com/opengeospatial/WFS_FES) (WFS 3) provides a specification to querying geospatial data on the web. The service operates over HTTPS and requests are made via HTTPS GET requests. No HTTPS authentication is required.

### Service endpoints

* [https://api.weather.gc.ca/](https://api.weather.gc.ca/)

#### OpenAPI 3.0 document

* [https://api.weather.gc.ca/openapi?f=html](https://api.weather.gc.ca/openapi?f=html)

### Feature collections

List all feature collections available:

* [https://api.weather.gc.ca/collections](https://api.weather.gc.ca/collections)

The response provides a list of feature collections with associated metadata (title, description, links, extent, CRS).

### Feature collection 

List a single feature collection:

* [https://api.weather.gc.ca/collections/hydrometric-stations](https://api.weather.gc.ca/collections/hydrometric-stations)

### Inspecting feature collection schema

Issue a query returning a single feature to inspect geometry and properties:

* [https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?limit=1](https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?limit=1)

### Querying

Querying feature collections allows for spatial, temporal and property filtering. Filter parameters can be combined to formulate an exclusive ('and') search. The first parameter in a query is specified with `?` and subsequent parameters with `&`.

The examples that follow use the [hydrometric daily mean](https://api.weather.gc.ca/collections/hydrometric-daily-mean) feature collection.

Default query, no filters:

* [https://api.weather.gc.ca/collections/hydrometric-daily-mean/items](https://api.weather.gc.ca/collections/hydrometric-daily-mean/items)

#### Spatial

Query by bounding box (minx, miny, maxx, maxy):

* [https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?bbox=-140,43.2,-65,67](https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?bbox=-140,43.2,-65,67)

#### Temporal

Query by a single time instant:

* [https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?datetime=1972-10-30](https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?datetime=1972-10-30)

Query by a time extent:

* [https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?datetime=1972-10-30/2010-07-31](https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?datetime=1972-10-30/2010-07-31)

Query by time extent with the open ended `..` keyword:

* Since a specific datetime: [https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?f=json&STATION_NUMBER=07DA006&datetime=2012-05-20/..](https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?f=json&STATION_NUMBER=07DA006&datetime=2012-05-20/..)
* Until a specific datetime: [https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?f=json&STATION_NUMBER=07DA006&datetime=../2015-11-11](https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?f=json&STATION_NUMBER=07DA006&datetime=../2015-11-11)

#### Property

Query by a feature collection property:

* [https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=10CD001](https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=10CD001)

#### Paging

##### Startindex

The `startindex` parameter can be used to specify the record to start at when extracting
features. The default value is 0 (first feature).

##### Total number of items

The `resulttype=hits` parameter is used to return the number of features found in a collection, without the actual features returned. The number of features is found in the response's `numberMatched` key.

* Example: [https://api.weather.gc.ca/collections/ltce-stations/items?f=json&resulttype=hits](https://api.weather.gc.ca/collections/ltce-stations/items?f=json&resulttype=hits)

##### Limit

The `limit` parameter is used to define the maximum records to return as part of querying
for features. The default response size is 500 features.

##### Paging through results

The `startindex` and `limit` parameters can be used in tandem to cycle through feature collections. The examples below demonstrate how to adjust and page through query results.

Query and limit to features 1-2:

* [https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=10CD001&limit=2](https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=10CD001&limit=2)

Query and limit to features 1-100:

* [https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=10CD001&limit=100](https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=10CD001&limit=100)

Query and limit to features 101-200:

* [https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=10CD001&startindex=101&limit=100](https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=10CD001&startindex=101&limit=100)

##### Strategies for paging

The paging strategy is commonly used in support of performance when returning large data extraction. For example, a client could page by 1000 features to cycle through an entire station record:

* [https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=01AP004&startindex=0&limit=1000](https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=01AP004&startindex=0&limit=1000)
* [https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=01AP004&startindex=1000&limit=1000](https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=01AP004&startindex=1000&limit=1000)

The client can then simply cycle through all items until there no longer any records. This would constitute the entire record.


#### Combining filter parameters

Query all daily mean data from a single station between 2001 and 2010:

* [https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=10CD001&datetime=2001-01-01/2010-12-31](https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=10CD001&datetime=2001-01-01/2010-12-31)

#### Exporting to CSV format

Any query can be exported to CSV by adding `&f=csv` to the request.

#### Sorting

Any query can be sorted by using the `sortby` parameter. The sort order is ascending by default and add the `-` sign the property name for descending order. Sorting by multiple properties is supported by providing a comma-separated list to the `sortby` parameter. Examples:

* `&sortby=PROPERTY` sorts the property in ascending order
* `&sortby=-PROPERTY` sorts the property in descending order

### Access by identifier

Fetch a single feature by identifier:

* [https://api.weather.gc.ca/collections/hydrometric-daily-mean/items/11AC016.1926-06-12](https://api.weather.gc.ca/collections/hydrometric-daily-mean/items/11AC016.1926-06-12)
