[En français](wms_fr.md)

![ECCC logo](../img_eccc-logo.png)

[TOC](../readme_en.md) > [MSC GeoMet](readme_en.md) > WMS

# Web Map Service (WMS)

Requests with the [OGC Web Map Service (WMS)](https://www.opengeospatial.org/standards/wms) standard mainly enable a client to retrieve geospatial data as maps. WMS requests are made over the internet (HTTP) and are primarily used to retrieve an image (e.g. JPEG, PNG) of geospatial data for a given area of interest.

The Web Map Service allows for several different types of request types, each of which are described in further detail below:

* GetCapabilities
* GetMap
* GetFeatureInfo
* GetLegendGraphic
</br></br>

## WMS GetCapabilities

A WMS GetCapabilities request allows the client to retrieve an XML document that contains metadata describing the service. This document contains information relating to the supported request types, supported coordinate reference systems, and most importantly, the list of available layers (data).

A WMS GetCapabilities request is comprised of the following parameters:


| Required parameters                 | Definition |
| ------------------------- | ---------- |
| SERVICE         | The service the client is requesting. In this case, `wms`|
| VERSION         | The version of the service the client is requesting. We recommend using the latest WMS version `1.3.0`|
| REQUEST         | The request type. In this case, `GetCapabilities`|

| Optional parameter                | Definition |
| ------------------------- | ---------- |
| LAYERS         | A vendor extension that allows a client to filter the GetCapabilities document for a single specific layer. This greatly reduces the size of the returned XML document|
| LANG          | A vendor extension that allows a client to display the GetCapabilities document in English(en) or French(fr). Defaults to English if the parameter is not included in the request|

A WMS GetCapabilities request to GeoMet-Weather is then be constructed like this:

[https://geo.weather.gc.ca/geomet/?service=WMS&version=1.3.0&request=GetCapabilities](https://geo.weather.gc.ca/geomet/?lang=en&service=WMS&version=1.3.0&request=GetCapabilities)

Each layer defined in the WMS GetCapabilities XML document has information relating to the layer's name and title, geographic extent, time extent, and available styles.
</br></br>

## WMS GetMap

A WMS GetMap request allows the client to retrieve a map image (JPEG, PNG, etc.) for a given layer within a defined area. A GetMap request is composed of several parameters whose value determine the layer requested, its style, coordinate reference system, the timestep, in addition to the properties of the returned image. The [WMS GetCapabilities request](#wms-getcapabilities) can assist the client in determining the values for several of these parameters.


| Required parameters                 | Definition |
| ------------------------- | ---------- |
| SERVICE         | The service the client is requesting. In this case, `wms`.|
| VERSION         | The version of the service the client is requesting. We recommend using the latest wms version `1.3.0`.|
| REQUEST         | The request type. In this case, `GetMap`.|
| LAYERS          | The name of the layer used to create the image. The name of the layer can be retrieved using a [WMS GetCapabilities](#wms-getcapabilities) request. MSC GeoMet currently supports only a single value for the GetMap LAYERS parameter. This will be improved in a future version to support multiple layers as per OGC WMS 1.3.0.|
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
</br></br></br>

## WMS GetFeatureInfo

A WMS GetFeatureInfo request retrieves raw data for a given geographic location. The GetFeatureInfo request parameters resemble those of a GetMap request but also include three new required parameters: `I`, `J` and `QUERY_LAYERS`. These parameters represent the horizontal and vertical placement of the pixel to query in the map image and the name of the layers to query.


| Required parameters                 | Definition |
| ------------------------- | ---------- |
| SERVICE         | The service the client is requesting. In this case, `wms`|
| VERSION         | The version of the service the client is requesting. We recommend using the latest wms version `1.3.0`|
| REQUEST         | The request type. In this case, `GetFeatureInfo`.|
| LAYERS          | The name of the layer used to query. The name of the layer can be retrieved using a [WMS GetCapabilities](#wms-getcapabilities) request.|
| CRS (version 1.3.0) or SRS (WMS version 1.1.0) | The coordinate reference system (CRS) used to create the map image. **Be careful, this parameter name differs depending on the version specified in the VERSION parameter**.|
| BBOX            | The bounding box of the requested image. Coordinates should be in the units of the CRS/SRS. If using the WMS 1.3.0 specification *and the EPSG:4326* these values are: `minY,minX,maxY,maxX`. If the request uses the WMS 1.1.1 specification or any other CRS, these values are: `minX,minY,maxX,maxY`. The request's bounding box must cover a part of the request layer's geographic extent.|
| FORMAT          | The file format desired for the requested image. Accepted values for this parameter are: `image/png` or `image/jpeg`. Images in the PNG format support transparency, while images in the JPEG format are smaller in size|
| HEIGHT          | The height in pixels of the associated image|
| WIDTH           | The width in pixels of the associated image|
| I (WMS version 1.3.0) or X (WMS version 1.1.0) | The horizontal coordinate of the pixel to query|
| J (WMS version 1.3.0) or Y (WMS version 1.1.0)  | The vertical coordinate of the pixel to query|
| QUERY_LAYERS    | The name of the layer to query|

| Optional parameters                 | Definition |
| ------------------------- | ---------- |
| INFO_FORMAT     | The format of the data returned by the query. Accepted values for this parameter are: `text/plain` (default), `application/json` or  `application/vnd.ogc.gml`|
| FEATURE_COUNT   | The amount of features returned by the request.|
| TIME            | The date and time used to generate the requested image. The format must comply with the ISO8601 standard. For more information regarding managing time in WMS requests, see the [WMS Handling Time](#handling-time) section.|
| DIM_REFERENCE_TIME  | The time of the weather model run to used to generate the requested image. For more information regarding managing time in WMS requests, see the [WMS Handling Time](#handling-time) section.|

A GetFeatureInfo request for the same image requested in the GetMap example above would look like this:

```
https://geo.weather.gc.ca/geomet?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetFeatureInfo&BBOX=45,-75,45.5,-74.5
&CRS=EPSG:4326&WIDTH=10&HEIGHT=10&LAYERS=GDPS.ETA_TT&INFO_FORMAT=application/json&QUERY_LAYERS=GDPS.ETA_TT&I=5&J=5
```
</br></br></br>

## WMS GetLegendGraphic

A WMS GetLegendGraphic request returns an image of the legend in the style requested by the user. The simplest way to access a layer's legend for a given style is to consult the WMS GetCapabilities document for the layer in question. All available layer styles are listed within the layer definition and the `<OnlineResource>` tag will contain a WMS GetLegendGraphic URL.

For example, the GDPS air temperature layer (GPDS.ETA_TT) has several styles defined in the WMS GetCapabilties document. Requesting the `TEMPERATURE-LINEAR` style using the GetLegendGraphic request contained in the `<OnlineResource>` tag returns the legend for this style:

![TEMPERATURE-LINEAR GetLegendGraphic Example](https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=GDPS.ETA_TT&format=image/png&STYLE=TEMPERATURE-LINEAR)


| Required parameters                 | Definition |
| ------------------------- | ---------- |
| SERVICE         | The service the client is requesting. In this case, `wms`|
| VERSION         | The version of the service the client is requesting. We recommend using the latest wms version `1.3.0`|
| REQUEST         | The request type. In this case, `GetLegendGraphic`|
| LAYER           | The name of the layer for which the legend is requested. The name of the layer can be retrieved using a [WMS GetCapabilities](#wms-getcapabilities) request|
| FORMAT          | The file format desired for the requested image. Accepted values for this parameter are: `image/png` or `image/jpeg`|
| SLD_VERSION     | The SLD document version. We recommend using version `1.1.0`|

| Optional parameters                | Definition |
| ------------------------- | ---------- |
| STYLE           | The name of the style used to create the legend image. The name individual layer styles can be retrieved using a [WMS GetCapabilities](#wms-getcapabilities) request. If this parameter is not specified a request will return the layer's default style. Note: Make sure to type the singular form of this parameter in the `GetLegendGraphic` request and not the plural form (i.e. `STYLES`), because it will output the layer's default style instead of the requested style.|
| SLD             | Specifies that the legend should be created with an external SLD document. See the [Handing Styles](#handling-styles) for further information.|
| SLD_BODY        | Allows the user to include an SLD document directly in the request URL.| Note: the value of LAYER in the WMS GetMap request and the value of se:Name (or se%3AName when encoded) in SLD_BODY needs to be different for the request to work.
| LANG          | A vendor extension that allows a client to display the legend in English(en) or French(fr). Defaults to English if the parameter is not included in the request|

A sample GetLegendGraphic request for the Global Deterministic Wave Prediction System's winds layer (GDWPS.UU.1h) would look like this:

```
https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0
&layer=OCEAN.GIOPS.2D_UU2W&format=image/png&STYLE=SEA_CURARROW_0MTO100M_SURFACE
```

And returns:

![Example of ocean current arrows from GIOPS](https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=OCEAN.GIOPS.2D_UU2W&format=image/png&STYLE=SEA_CURARROW_0MTO100M_SURFACE)


## Handling time

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

</br>

#### <span class="badge badge-light">Time handling differences between GeoMet-Weather and GeoMet-Climate</span>

It is important to mention that time is not handled in the same manner between GeoMet-Weather and GeoMet-Climate due to the different nature of the underlying data.

In Geomet-Climate, time intervals are either yearly (YYYY) or monthly (YYYY-MM) depending on the queried layer. A WMS GetCapabilities request to GeoMet-Climate allows the client to properly identify the time dimension for a given layer.

For example, let's take a look at the [CMIP5 Monthly ensembles of Wind Speed projections (5th percentile)](https://geo.weather.gc.ca/geomet-climate?lang=en&service=WMS&version=1.3.0&request=GetCapabilities&Layer=CMIP5.SFCWIND.RCP26.ENS.ABS_PCTL5) layer's `<Dimension>` tag:

```xml
<Dimension name="time" units="ISO8601" default="2100-12" nearestValue="0">2006-01/2100-12/P1M</Dimension>
```

A successful WMS GetMap request with a defined `TIME` parameter would need to have a value between `2006-01` and `2100-12`.
</br></br>

## Handling styles

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
an external style using a [OGC Styled Layer Descriptor (SLD)](https://www.opengeospatial.org/standards/sld) document in the `SLD` parameter or by entering the SLD document directly into the `SLD_BODY` parameter. Note that the `SLD_BODY` definition must be entirely encoded using the URL encoding. Also, for `SLD_BODY`, the value of LAYER in the WMS GetMap request and the value of se:Name (or se%3AName when encoded) in `SLD_BODY` needs to be different for the request to work.

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
