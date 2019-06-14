[En français](web-services_fr.md)

![ECCC logo](../img_eccc-logo.png)

[TOC](../readme_en.md) > MSC GeoMet web services

# Geospatial Web Services

Web services are systems designed to support machine to machine interaction over a network, and are typically utilized in a client/server computing environment made available through programmatic access, associated tools and applications.

The MSC GeoMet web services adhere to open standards ratified by the [Open Geospatial Consortium (OGC)](https://www.opengeospatial.org/), and the [International Organization for Standardization (ISO)](https://www.isotc211.org/) which enable interoperability and thus make data easy to discover, access, visualize and integrate. OGC and ISO standards play an important role in [World Meteorological Organization interoperability](https://www.wmo.int/pages/prog/www/WIS/documents/MOAWMO_OGC.pdf) as part of the [WMO Information System](https://www.wmo.int/pages/prog/www/WIS/) and are supported by numerous off the shelf open source or commercial tools.

The following OGC Web Services are served by MSC GeoMet:
* Web Map Service (WMS)
* Web Coverage Service (WCS)
* OGC API - Features

## Web Map Service (WMS)

The [OGC Web Map Service](https://www.opengeospatial.org/standards/wms) Web Map Service (WMS) requests enable a client to retrieve geospatial data as maps.  WMS requests are made over the internet (HTTP) and are primarily used to retrieve an image (JPEG, PNG, etc.) of geospatial data for a given area of interest. 

The Web Map Service allows for several different types of request types, each of which are described in further detail below.

### WMS GetCapabilities

A WMS Get Capabilities request allows the client to retrieve an XML document that contains metadata describing the service. This document contains information relating to the supported request types, supported coordinate reference systems, and most importantly, the layers (data) for which clients can request maps. 

A WMS GetCapabilities request is comprised of the following parameters:

<br>

| Parameter                 | Definition |
| ------------------------- | ---------- |
| SERVICE (required)        | The service the client is requesting. In this case, `wms`.|
| VERSION (required)        | The version of the service the client is requesting. We recommend using the latest wms version `1.3.0`.|
| REQUEST (required)        | The request type. In this case, `GetCapabilities`.|
| LAYER (optional)         | A vendor extension that allows a client to filter the GetCapabilities document for a single named layer. This greatly reduces the size of the returned XML document.|

A WMS GetCapabilities request to MSC GeoMet would then be constructed 
like this:

[https://geo.weather.gc.ca/geomet/?service=WMS&version=1.3.0&request=GetCapabilities](https://geo.weather.gc.ca/geomet/?lang=en&service=WMS&version=1.3.0&request=GetCapabilities)

Each layer defined in the GetCapabilities document will have information 
relating to the layer's name and title, geographic extent, time extent, 
and available styles.

### WMS GetMap

A WMS GetMap request allows the client to retrieve a map image (JPEG, PNG, etc.) for a given layer within a defined area. A GetMap request is composed of several parameters whose value determine the layer requested, its style, coordinate reference system, temporal extent, in addition to the properties of the returned image. The [WMS GetCapabilities request](#getcapabilities) can assist the client in determining the values for several of these parameters.

<br>

| Parameter                 | Definition |
| ------------------------- | ---------- |
| SERVICE (required)        | The service the client is requesting. In this case, `wms`.|
| VERSION (required)        | The version of the service the client is requesting. We recommend using the latest wms version `1.3.0`.|
| REQUEST (required)        | The request type. In this case, `GetMap`.|
| LAYERS                    | The name of the layers used to create the image. The name of the layer can be retrieved using a [WMS GetCapabilities](#getcapabilities) request.|
| CRS (version 1.3.0) or SRS (version 1.1.0) (required)| The coordinate reference system (CRS) used to create the map image. **Be careful, this parameter name differs depending on the version specified in the VERSION parameter**.|
| BBOX (required)           | TThe bounding box of the requested image. Coordinates should be in the units of the CRS/SRS. If using the WMS 1.3.0 specification *and the EPSG:4326* these values are: `minY,minX,maxY,maxX`. If the request uses the WMS 1.1.1 specification or any other CRS, these values are: `minX,minY,maxX,maxY`.|
| FORMAT (required)         | The file format desired for the requested image. Accepted values for this parameter are: `image/png` or `image/jpeg`.|
| HEIGHT (required)         | The height in pixels of the returned image.|
| WIDTH (required)          | The width in pixels of the returned image.|
| TIME (optional)           | The date and time used to generate the requested image. The format must respect . For more information regarding managing time in WMS requests, see the [WMS Handling Time](#handling-time) section.|
| DIM_REFERENCE_TIME (optional) | The time of the weather model run to used to generate the requested image. For more information regarding managing time in WMS requests, see the [WMS Handling Time](#handling-time) section.|

A GetMap request for the Global Deterministic Prediction System's air temperature layer (GDPS.ETA_TT) would look like this:

```
https://geo.weather.gc.ca/geomet?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&BBOX=-90,-180,90,180
&CRS=EPSG:4326&WIDTH=600&HEIGHT=301&LAYERS=GDPS.ETA_TT&FORMAT=image/png
```

And returns:

![Global Deterministic Prediction System (GDPS) surface temperature](https://geo.weather.gc.ca/geomet?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&BBOX=-90,-180,90,180&CRS=EPSG:4326&WIDTH=600&HEIGHT=301&LAYERS=GDPS.ETA_TT&FORMAT=image/png)              

### WMS GetFeatureInfo

A WMS GetFeatureInfo request retrieves data for a given pixel of a map image. MSC GeoMet currently supports retrieving data as plain text or Geographic Markup Language (GML). The GetFeatureInfo request parameters resemble those of a GetMap request but also include three new required parameters: `I`, `J` and `QUERY_LAYERS`. These parameters represent the horizontal and vertical placement of the pixel to query in the map image and the name of the layers to query.

<br>

| Parameter                 | Definition |
| ------------------------- | ---------- |
| SERVICE (required)        | The service the client is requesting. In this case, `wms`.|
| VERSION (required)        | The version of the service the client is requesting. We recommend using the latest wms version `1.3.0`.|
| REQUEST (required)        | The request type. In this case, `GetFeatureInfo`.|
| LAYERS (required)         | The name of the layer(s) used to create the image. The name of the layer can be retrieved using a [WMS GetCapabilities](#getcapabilities) request.|
| CRS (version 1.3.0) or SRS (WMS version 1.1.0) (required)| The coordinate reference system (CRS) used to create the map image. **Be careful, this parameter name differs depending on the version specified in the VERSION parameter**.|
| BBOX (required)           | The bounding box of the requested image. Coordinates should be in the units of the CRS/SRS. If using the WMS 1.3.0 specification *and the EPSG:4326* these values are: `minY,minX,maxY,maxX`. If the request uses the WMS 1.1.1 specification or any other CRS, these values are: `minX,minY,maxX,maxY`. The request's bounding box must cover a part of the request layer's geographic extent.|
| FORMAT (required)         | The file format desired for the requested image. Accepted values for this parameter are: `image/png` or `image/jpeg`.|
| HEIGHT (required)         | The height in pixels of the returned image.|
| WIDTH (required)          | The width in pixels of the returned image.|
| I (WMS version 1.3.0) or X (WMS version 1.1.0) (required| The horizontal coordinate of the pixel to query.|
| J (WMS version 1.3.0)or Y (WMS version 1.1.0) (required)| The verticial coordinate of the pixel to query.|
| QUERY_LAYERS (required)   | The name of layers to query (comma-seperated).|
| INFO_FORMAT (optional)    | The format of the data returned by the query. Accepted values for this parameter are: `text/plain` (default) or `application/vnd.ogc.gml`|
| FEATURE_COUNT (optional)  | The amount of features returned by the request.|
| TIME (optional)           | The date and time used to generate the requested image. The format must respect . For more information regarding managing time in WMS requests, see the [WMS Handling Time](#handling-time) section.|
| DIM_REFERENCE_TIME (optional) | The time of the weather model run to used to generate the requested image. For more information regarding managing time in WMS requests, see the [WMS Handling Time](#handling-time) section.|


A GetFeatureInfo request for the same image requested in the GetMap example above would look like this:
```
https://geo.weather.gc.ca/geomet?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetFeatureInfo&BBOX=-90,-180,90,180
&CRS=EPSG:4326&WIDTH=600&HEIGHT=301&LAYERS=GDPS.ETA_TT&FORMAT=image/png&QUERY_LAYERS=GDPS.ETA_TT&I=300&J=150
```

### WMS GetLegendGraphic

A WMS GetLegendGraphic request, returns an image of the legend in the style requested by the user. The simplest way to access a layer's legend for a given style is to consult the WMS GetCapabilities document for the layer in question. All available layer styles are listed within the layer definition and the `<OnlineResource>` tag will contain a WMS GetLegendGraphic URL. 

For example, the GDPS air temperature layer (GPDS.ETA_TT) has several styles defined in the WMS GetCapabilties document. Requesting the `TEMPERATURE-LINEAR` style using the GetLegendGraphic request contained in the `<OnlineResource>` tag returns the legend for this style:

![TEMPERATURE-LINEAR GetLegendGraphic Example](https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=GDPS.ETA_TT&format=image/png&STYLE=TEMPERATURE-LINEAR)

<br>

<br>

| Parameter                 | Definition |
| ------------------------- | ---------- |
| SERVICE (required)        | The service the client is requesting. In this case, `wms`.|
| VERSION (required)        | The version of the service the client is requesting. We recommend using the latest wms version `1.3.0`.|
| REQUEST (required)        | The request type. In this case, `GetLegendGraphic`.|
| LAYER (required)          | The name of the layer for which the legend is requested. The name of the layer can be retrieved using a [WMS GetCapabilities](#getcapabilities) request.|
| FORMAT (required)         | The file format desired for the requested image. Accepted values for this parameter are: `image/png` or `image/jpeg`.|
| SLD_VERSION (required)    | The SLD document version. We recommend using version `1.1.0`.
| STYLE (optional)          | The name of the style used to create the legend image. The name individual layer styles can be retrieved using a [WMS GetCapabilities](#getcapabilities) request. If this parameter is not specified a request will return the layer's default style.|
| SLD (optional)            | Specifies that the legend should be created with an external SLD document. See the [Handing Styles](#handling-styles) for further information.|
| SLD_BODY (optional)       | Allows the user to include an SLD document directly in the request URL.|


A sample GetLegendGraphic request for the Global Deterministic Wave Prediction System's winds layer (GDWPS.UU.1h) would look like this:

```
https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0
&layer=GDWPS.UU.1h&format=image/png&STYLE=WINDARROW
```

And returns:

![GDWPS Wind Arrow Style Example](https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=GDWPS.UU.1h&format=image/png&STYLE=WINDARROW)

### Handling Time

Given the important temporal dimension of weather data, it is important for users to understand how MSC GeoMet handles time in WMS requests. By default, if no `TIME` or `DIM_REFERENCE_TIME` parameters are passed in the request, MSC GeoMet will, by default, return the closest elapsed time interval available for the nearest past model run.

If the client desires to make a request for another date and time, the `TIME` or `DIM_REFERENCE_TIME` can be used in both GetMap and GetFeatureInfo requests. Date and times must adhere to the ISO8601 standard and are always in UTC (Coordinate Universal Time).

To make a request for a specific time and/or model run, a client must first determine the available model runs and time intervals. This information is available in the layer's `<Dimension>` tags in the WMS GetCapabilities document.

For example, the Global Deterministic Prediction System's air temperature layer (GDPS.ETA_TT) time dimensions are:
```xml
<Dimension name="time" units="ISO8601" default="2019-06-12T15:00:00Z" 
nearestValue="0">2019-06-12T00:00:00Z/2019-06-22T00:00:00Z/PT3H</Dimension>

<Dimension name="reference_time" units="ISO8601" default="2019-06-12T00:00:00Z" 
multipleValues="1" nearestValue="0">2019-06-11T00:00:00Z/2019-06-12T00:00:00Z/PT12H</Dimension>
```

The first `<Dimension>` tag represents the time intervals available for this layer. The `default` attribute is the time value set if no `TIME` parameter was included in the request. The tag value (i.e `2019-06-12T00:00:00Z/2019-06-22T00:00:00Z/PT3H`) informs the client of the available datetime values. At the time the GetCapabilities request was made, a client could request a map  (GetMap) or data (GetFeatureInfo) for any day between 2019-06-12T00:00:00Z and 2019-06-22T00:00:00Z at 3 hour intervals (PT3H).

The second `<Dimension>` tag represents the available model runs for the layer. The `default` attribute is the start time of the model run for the nearest past model run. The tag value informs the client of the available model run times for this layer. In this case, model runs are available every 12 hour (PT12H) between `2019-06-11T00:00:00Z` and `2019-06-12T00:00:00Z` (inclusive)

Given this information, a client could make a GetMap image request for the GDPS air temperature layer for 12:00:00 UTC on June 21st 2019 using the most recent model run (2019-06-12T00:00:00Z) as the data source. The request would look like this:

```
https://geo.weather.gc.ca/geomet?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&BBOX=-90,-180,90,180
&CRS=EPSG:4326&WIDTH=600&HEIGHT=301&LAYERS=GDPS.ETA_TT&FORMAT=image/png
&TIME=2019-06-21T12:00:00Z&DIM_REFERENCE_TIME=2019-06-14T00:00:00Z
```

#### Time handling differences between MSC GeoMet-Weather and MSC GeoMet-Climate

It is important to mention that time is not handled in the same manner between MSC Geomet-Weather and MSC Geomet-Climate due to the different nature of the underlying data.

In MSC Geomet-Climate, time intervals are either yearly (YYYY) or monthly (YYYY-MM) depending on the queried layer. A WMS GetCapabilities request to MSC GeoMet-Climate allows the client to properly identify the time dimension for a given layer.

For example, let's take a look at the [CMIP5 Monthly ensembles of Wind Speed projections (5th percentile)](https://geo.weather.gc.ca/geomet-climate?lang=en&service=WMS&version=1.3.0&request=GetCapabilities&Layer=CMIP5.SFCWIND.RCP26.ENS.ABS_PCTL5) layer's `<Dimension>` tag:

```xml
<Dimension name="time" units="ISO8601" default="2100-12" nearestValue="0">2006-01/2100-12/P1M</Dimension>
```

A successful GetMap request with a defined `TIME` parameter would need to have a value between `2006-01` and `2100-12`.

### Handling Styles

The graphical representation of information and data can have a significant impact on the way data is interpreted by an end-user. MSC GeoMet often provides several different graphical representations for a single layer. The client can choose to display the data using the style most appropriate for their use case.

Using the `STYLE` parameter in both GetMap and GetLegendFeature requests, a client can specify the style they choose to apply to the underlying data. Available styles for any given layer are described in the WMS GetCapabilities document.

Below is an example of two GetMap requests for the Deterministic 
Precipitation Analysis' Quantity of precipitation layer (RDPA.24F_PR)
that each specify a different `STYLE` parameter value to render the 
returned map.

RDPA.24F_PR with CAPA24-LINEAR style:

```
http://geo.weather.gc.ca/geomet?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&LAYERS=RDPA.24F_PR
&STYLES=CAPA24-LINEAR&CRS=EPSG:4326&BBOX=35,-150,85,-45&WIDTH=600&HEIGHT=400&FORMAT=image/png
```

![RDPA.24F_PR with CAPA24-LINEAR style](http://geo.weather.gc.ca/geomet?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&LAYERS=RDPA.24F_PR&STYLES=CAPA24-LINEAR&CRS=EPSG:4326&BBOX=35,-150,85,-45&WIDTH=600&HEIGHT=400&FORMAT=image/png)

RDPA.24F_PR with RDPA-WXO style:

```
http://geo.weather.gc.ca/geomet?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&LAYERS=RDPA.24F_PR
&STYLES=RDPA-WXO&CRS=EPSG:4326&BBOX=35,-150,85,-45&WIDTH=600&HEIGHT=400&FORMAT=image/png
```

![RDPA.24F_PR with CAPA24-LINEAR style](http://geo.weather.gc.ca/geomet?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&LAYERS=RDPA.24F_PR&STYLES=RDPA-WXO&CRS=EPSG:4326&BBOX=35,-150,85,-45&WIDTH=600&HEIGHT=400&FORMAT=image/png)

Users can also choose to apply their own styles either by pointing to
an external style using a [OGC Styled Layer Descriptor (SLD)](https://www.opengeospatial.org/standards/sld) document in the `SLD` parameter 
or by entering the SLD document directly into the `SLD_BODY` parameter. Note that the `SLD_BODY` definition must be encoded using the URL encoding.

```
http://geo.weather.gc.ca/geomet?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&LAYERS=GDPS.ETA_NT
&STYLES=&CRS=EPSG:4326&BBOX=35,-150,85,-45&WIDTH=1800&HEIGHT=1200&FORMAT=image/png
&SLD_BODY=%3C%3Fxml+version%3D%221.0%22+encoding%3D%22UTF-8%22%3F%3E+%3C
StyledLayerDescriptor+version%3D%221.0.0%22+xmlns%3D%22http%3A%2F%2F
www.opengis.net%2Fsld%22+xmlns%3Aogc%3D%22http%3A%2F%2Fwww.opengis.net
%2Fogc%22+xmlns%3Axlink%3D%22http%3A%2F%2Fwww.w3.org%2F1999%2Fxlink%22+xmlns%3
Axsi%3D%22http%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema-instance%22+xsi%3A
schemaLocation%3D%22http%3A%2F%2Fwww.opengis.net%2Fsld+http%3A%2F%2Fschemas.opengis.net
%2Fsld%2F1.0.0%2FStyledLayerDescriptor.xsd%22%3E+%3CNamedLayer%3E+%3Cse%3AName%3E
GDPS.ETA_NT%3C%2Fse%3AName%3E+%3CUserStyle%3E+%3Cse%3AName%3ETEST%3C%2Fse%3AName%3E+%3Cse%3A
FeatureTypeStyle%3E+%3Cse%3ARule%3E+%3Cse%3ARasterSymbolizer%3E+%3Cse%3AOpacity%3E1.0
%3C%2Fse%3AOpacity%3E+%3CColorMap%3E+%3CColorMapEntry+color%3D%22%238cff66%22+quantity
%3D%220%22%2F%3E+%3CColorMapEntry+color%3D%22%23ffff00%22+quantity%3D%2225%22%2F%3E+%3C
ColorMapEntry+color%3D%22%23b38600%22+quantity%3D%2250%22%2F%3E+%3CColorMapEntry+color
%3D%22%23cc0000%22+quantity%3D%2275%22%2F%3E+%3CColorMapEntry+color%3D%22%234d0000%22+
quantity%3D%22100%22%2F%3E+%3C%2FColorMap%3E+%3C%2Fse%3ARasterSymbolizer%3E+%3C%2Fse%3A
Rule%3E+%3C%2Fse%3AFeatureTypeStyle%3E+%3C%2FUserStyle%3E+%3C%2FNamedLayer%3E+%3C%2FStyledLayerDescriptor%3E
```
![RDPA.24F_PR with CAPA24-LINEAR style](http://geo.weather.gc.ca/geomet?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&LAYERS=GDPS.ETA_NT&STYLES=&CRS=EPSG:4326&BBOX=35,-150,85,-45&WIDTH=600&HEIGHT=400&FORMAT=image/png&SLD_BODY=%3C%3Fxml+version%3D%221.0%22+encoding%3D%22UTF-8%22%3F%3E+%3CStyledLayerDescriptor+version%3D%221.0.0%22+xmlns%3D%22http%3A%2F%2Fwww.opengis.net%2Fsld%22+xmlns%3Aogc%3D%22http%3A%2F%2Fwww.opengis.net%2Fogc%22+xmlns%3Axlink%3D%22http%3A%2F%2Fwww.w3.org%2F1999%2Fxlink%22+xmlns%3Axsi%3D%22http%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema-instance%22+xsi%3AschemaLocation%3D%22http%3A%2F%2Fwww.opengis.net%2Fsld+http%3A%2F%2Fschemas.opengis.net%2Fsld%2F1.0.0%2FStyledLayerDescriptor.xsd%22%3E+%3CNamedLayer%3E+%3Cse%3AName%3EGDPS.ETA_NT%3C%2Fse%3AName%3E+%3CUserStyle%3E+%3Cse%3AName%3ETEST%3C%2Fse%3AName%3E+%3Cse%3AFeatureTypeStyle%3E+%3Cse%3ARule%3E+%3Cse%3ARasterSymbolizer%3E+%3Cse%3AOpacity%3E1.0%3C%2Fse%3AOpacity%3E+%3CColorMap%3E+%3CColorMapEntry+color%3D%22%238cff66%22+quantity%3D%220%22%2F%3E+%3CColorMapEntry+color%3D%22%23ffff00%22+quantity%3D%2225%22%2F%3E+%3CColorMapEntry+color%3D%22%23b38600%22+quantity%3D%2250%22%2F%3E+%3CColorMapEntry+color%3D%22%23cc0000%22+quantity%3D%2275%22%2F%3E+%3CColorMapEntry+color%3D%22%234d0000%22+quantity%3D%22100%22%2F%3E+%3C%2FColorMap%3E+%3C%2Fse%3ARasterSymbolizer%3E+%3C%2Fse%3ARule%3E+%3C%2Fse%3AFeatureTypeStyle%3E+%3C%2FUserStyle%3E+%3C%2FNamedLayer%3E+%3C%2FStyledLayerDescriptor%3E)


## Web Coverage Service (WCS)

The [OGC Web Coverage Service](https://www.opengeospatial.org/standards/wcs) requests enable a client to retrieve coverage information from a geospatial
data for a given area of interest. WCS requests are made over the internet (HTTP) and give the user more flexibility when requesting information about the coverage of a layer compared with the more traditional way of downloading of flat files.

The Web Coverage Service allows for several different types of request types, each of which are described in further detail below.

Note that only the WCS 2.0.1 version is currently supported by the GeoMet services, thus we strongly advise the users to use WCS version 2.0.1. Requests using WCS 1.1.1 might work, but no tests and no efforts are put in supporting this older version of the WCS standard.
 
### WCS GetCapabilities

A WCS GetCapabilities request allows the client to retrieve an XML
document that contains metadata describing the service. This document
contains information relating to the supported request types, supported
coordinate reference systems, and most importantly, the layers (data)
for which clients can request raw data.

A GetCapabilities request is comprised of the following parameters:
<br>

| Required parameters       | Definition |
| ------------------------- | ---------- |
| SERVICE      | The service the client is requesting. In this case, `wcs`.|
| VERSION      | The version of the service the client is requesting. We recommend using the latest wms version `2.0.1`|
| REQUEST      | The request type. In this case, `GetCapabilities`.|

| Optional parameter        | Definition |
| ------------------------- | ---------- |
| COVERAGEID                | A vendor extension that allows a client to filter the GetCapabilities document for a single named layer. This greatly reduces the size of the returned XML document.|


A WCS GetCapabilities request to MSC GeoMet would then be constructed
like this:

[https://geo.weather.gc.ca/geomet?SERVICE=WCS&VERSION=2.0.1&REQUEST=GetCapabilities](https://geo.weather.gc.ca/geomet?SERVICE=WCS&VERSION=2.0.1&REQUEST=GetCapabilities)
 
The GetCapabilities document will have information
relating to the service's name and title, geographic extent, available layers 
and available format.
 
### WCS DescribeCoverage

A WCS DescribeCoverage requets allows the user to access more information about a given layer
then using the [WCS GetCapabilities](#wcsgetcap). Information in the DescribeCoverage request includes:
extent, CRS, available format


| Required parameters       | Definition |
| ------------------------- | ---------- |
| SERVICE      | The service the client is requesting. In this case, `wcs`.|
| VERSION      | The version of the service the client is requesting. We recommend using the latest wms version `2.0.1`|
| REQUEST      | The request type. In this case, `DescribeCoverage`.|
| COVERAGEID   | The name of the layer for which to return the metadata. The name of the layer can be retrieved using a [WCS GetCapabilities](#wcsgetcap) request. This greatly reduces the size of the returned XML document.|

A WCS DescribeCoverage request to MSC GeoMet for the GDPS.ETA_TT layer would then be constructed
like this:

[https://geo.weather.gc.ca/geomet?SERVICE=WCS&VERSION=2.0.1&REQUEST=DescribeCoverage&COVERAGEID=GDPS.ETA_TT](https://geo.weather.gc.ca/geomet?SERVICE=WCS&VERSION=2.0.1&REQUEST=DescribeCoverage&COVERAGEID=GDPS.ETA_TT)

### WCS GetCoverage

A WCS GetCoverage request is used to retrieve the actual coverage information (raw data).
The most interesting aspect for a user is to be able to request a subdomain of a layer in the projection 
he wants and in the format he wants with the possibility to obtain the layer 
in a different resolution from the original one.

| Required parameters       | Definition |
| ------------------------- | ---------- |
| SERVICE      | The service the client is requesting. In this case, `wcs`.|
| VERSION      | The version of the service the client is requesting. We recommend using the latest wms version `2.0.1`|
| REQUEST      | The request type. In this case, `GetCoverage`.|
| COVERAGEID   | The name of the layer for which to return the coverage information.|
| FORMAT       | The file format desired for the requested coverage. Accepted values for this parameter are: `image/tiff` (GeoTIFF) or `image/netcdf` (NetCDF).|

| Optional parameter        | Definition |
| ------------------------- | ---------- |
|SUBSETTINGCRS     | The coordinate reference system (CRS) used to request the coverage layer to the server.|
|OUTPUTCRS         | The coordinate reference system (CRS) used to return the coverage layer to the user. This parameter can be different from `SUBSETTINGCRS`|
|SUBSET=axis()     | The bounding box of the requested coverage per axis. One can use one of the recognize axis sub-parameter:  `x`, `xaxis`, `x-axis`, `x_axis`, `long`, `long_axis`, `long-axis`, `lon`, `lon_axis`, `lon-axis`, `y`, `yaxis`, `y-axis`, `y_axis`, `lat`, `lat_axis` and `lat-axis`. Coordinates should be in the units of the SUBSETTINGCRS. The request's subset must cover a part of the request layer's geographic extent.|
|RESOLUTION=axis() | Resolution (pixel/unit) per axis of the returned coverage to the user. If none is set, the coverage resolution returned might not be the one of the original data.|
|SIZE=axis()       | Size (pixel) per axis of the returned coverage to the user. If none is set, the coverage size returned might not be the one of the original data.|
|INTERPOLATION     | Interpolation method used for the requested coverage when a rescaling is needed. Three method can be used: `NEAREST`, `BILINEAR`, `AVERAGE`. If none is specified, default is `NEAREST`|
|RANGESUBSET       | This parameter allows the user to specify a band of a coverage layer to be returned. Either the band band name or the band number can be used.|
|TIME              | The date and time used to generate the requested coverage. The format must respect the ISO8601 standard. For more information regarding managing time in WCS requests, see the [WCS Handling Time](#wcstime) section.|
|DIM_REFERENCE_TIME| The time of the weather model run (when available) to use to generate the requested coverage. The format must respect the ISO8601 standard. For more information regarding managing time in WCS requests, see the [WCS Handling Time](#wcstime) section.|

Note that `RESOLUTION` and `SIZE` are mutually exclusive on one axis and should never be used for the same axis in the same request.

A WCS GetCoverage request to MSC GeoMet for the GDPS.ETA_TT layer could then be constructed
like this: 
[https://geo.weather.gc.ca/geomet?SERVICE=WCS&VERSION=2.0.1&REQUEST=GetCoverage&COVERAGEID=GDPS.ETA_TT&SUBSETTINGCRS=EPSG:4326&SUBSET=x(-120,-85)&SUBSET=y(48,66)&RESOLUTION=x(0.24)&RESOLUTION=y(0.24)&FORMAT=image/tiff](https://geo.weather.gc.ca/geomet?SERVICE=WCS&VERSION=2.0.1&REQUEST=GetCoverage&COVERAGEID=GDPS.ETA_TT&SUBSETTINGCRS=EPSG:4326&SUBSET=x(-120,-85)&SUBSET=y(48,66)&RESOLUTION=x(0.24)&RESOLUTION=y(0.24)&FORMAT=image/tiff)

### <a name="wcstime"></a>Handling Time

Given the important temporal dimension of weather data, it is important
for users to understand how MSC GeoMet handles time in wcs requests. By
default, if no `TIME` or `DIM_REFERENCE_TIME` parameters are passed in
the request, MSC GeoMet will, by default, return the closest
elapsed time interval available for the current model run.

If the user wants to make a request for another date and time, the
`TIME` or `DIM_REFERENCE_TIME` can be used in a GetCoverage request. Date and times must adhere to the ISO8601
standard and are always in UTC (Coordinate Universal Time).

#### GeoMet-Climate

GeoMet-Climate's WCS does not support request with `TIME` or `DIM_REFERENCE_TIME`.
Instead, the WCS time information is stored in different bands, each one representing a particular timestamp.
This means that a user will need the `RANGESUBSET` parameter to access the desired time coverage.

The name of the different bands can be retrieved from the DescribeCovareg request. 
Here is an example using a GeoMet-Climate layer (DCS.TM.RCP26.YEAR.ANO_PCTL50):

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

In this example, the `field` keys give the user the available band names.
In GeoMet-Climate, the bands will always use the same nomenclature which is: `B` followed by one of the two 
ISO8601 time format supported: `YYYY` for annual time interval and `YYYY-MM` for monthly time interval.

In GeoMet-CLimate one can either request coverage for a single time step or for a time range:
* Single time step: `RANGESUBSET=B20015`
* Time range: `RANGESUBSET=B2015:B2019`

Note that a user cannot, in a single GetCoverage request, ask for more than 256 bands.

#### GeoMet-Weather

Please refer to the previous [WMS Handling Time](#handling-time) section, as for GeoMet-Weather,
the `TIME` and `DIM_REFERENCE_TIME` usage is the same.

Note that the layers time metadata are not available in the WCS GetCapabilities or the WCS DescribeCoverage. 
The time metadata can only be access through the WMS GetCapabilities.

### Usage example
GeoMet-Climate and GeoMet-Weather WCS are used through the [Climate data extraction tool](https://climate-change.canada.ca/climate-data/#/) of the
[Canadian Centre for Climate Services portal](https://www.canada.ca/en/environment-climate-change/services/climate-change/canadian-centre-climate-services.html)

One can select a variable, region of interest, temporal information and output format on the extraction tool
to retrieve the raw coverage information.

## OGC API - Features

http://geo.weather.gc.ca/geomet/features/?f=html

----------------------------------------------------------------
This page will provide details on the MSC GeoMet web services, especially the capabilities and parameters. These come in addition to the usage-overview page

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

If an incorrect time is specified in a request, it will return an error message. Time parameter must be in ISO8601.

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