[En français](wcs_fr.md)

![ECCC logo](../img_eccc-logo.png)

[TOC](../readme_en.md) > [MSC GeoMet](readme_en.md) > WCS

# Web Coverage Service (WCS)

The [OGC Web Coverage Service](https://www.opengeospatial.org/standards/wcs) requests enable a client to retrieve coverage information from a geospatial data for a given area of interest. WCS requests are made over the internet (HTTP) and give the user more flexibility when requesting information about the coverage of a layer compared with the more traditional way of downloading of flat files. The Web Coverage Service allows for several different types of requests, each of which are described in further detail below.

Note that only the WCS 2.0.1 version is currently supported by the GeoMet services. We invite users to use exclusively version 2.0.1 of the WCS standard. Also, note that WCS 2.0.1 is not supported in QGIS and ArcGIS.

The Web Coverage Service allows for several different types of request types, each of which are described in further detail below:

* GetCapabilities
* DescribeCoverage
* GetCoverage
* GetLegendGraphic
</br></br>

## WCS GetCapabilities


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

</br></br>

## WCS DescribeCoverage

A WCS DescribeCoverage request allows the user to access more information about a given layer than using the [WCS GetCapabilities](#wcsgetcap). Information in the DescribeCoverage request includes: extent, CRS, available format


| Required parameters       | Definition |
| ------------------------- | ---------- |
| SERVICE      | The service the client is requesting. In this case, `wcs`.|
| VERSION      | The version of the service the client is requesting. We recommend using the latest WCS version `2.0.1`|
| REQUEST      | The request type. In this case, `DescribeCoverage`.|
| COVERAGEID   | The name of the layer for which to return the metadata. The name of the layer can be retrieved using a [WCS GetCapabilities](#wcs-getcapabilities) request|

A WCS DescribeCoverage request to GeoMet-Weather for the GDPS.ETA_TT layer would then be constructed like this:

[https://geo.weather.gc.ca/geomet?SERVICE=WCS&VERSION=2.0.1&REQUEST=DescribeCoverage&COVERAGEID=GDPS.ETA_TT](https://geo.weather.gc.ca/geomet?SERVICE=WCS&VERSION=2.0.1&REQUEST=DescribeCoverage&COVERAGEID=GDPS.ETA_TT)

</br></br>

## WCS GetCoverage

A WCS GetCoverage request is used to retrieve the actual coverage information (raw data). The most interesting aspect for a user is to be able to request a subdomain of a layer in the projection he wants and in the format he wants with the possibility to obtain the layer in a different spatial resolution and file format from the original one.

| Required parameters       | Definition |
| ------------------------- | ---------- |
| SERVICE      | The service the client is requesting. In this case, `wcs`.|
| VERSION      | The version of the service the client is requesting. We recommend using the latest WCS version `2.0.1`|
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
|TIME              | The date and time associated to the requested coverage. The format must respect the ISO8601 standard. For more information regarding managing time in WCS requests, see the [WCS Handling Time](#handling-time) section|
|DIM_REFERENCE_TIME| The time of the weather model run (when available) to use to generate the requested coverage. The format must respect the ISO8601 standard. For more information regarding managing time in WCS requests, see the [WCS Handling Time](#handling-time) section|

A WCS GetCoverage request to MSC GeoMet for the GDPS.ETA_TT layer could then be constructed
like this:

[https://geo.meteo.gc.ca/geomet?SERVICE=WCS&VERSION=2.0.1&REQUEST=GetCoverage&COVERAGEID=GDPS.ETA_TT&
SUBSETTINGCRS=EPSG:4326&SUBSET=x(-120,-85)&SUBSET=y(48,66)&RESOLUTION=x(0.24)&
RESOLUTION=y(0.24)&FORMAT=image/tiff](https://geo.meteo.gc.ca/geomet?SERVICE=WCS&VERSION=2.0.1&REQUEST=GetCoverage&COVERAGEID=GDPS.ETA_TT&SUBSETTINGCRS=EPSG:4326&SUBSET=x(-120,-85)&SUBSET=y(48,66)&RESOLUTION=x(0.24)&RESOLUTION=y(0.24)&FORMAT=image/tiff)

</br></br>

## Handling time

Given the important temporal dimension of weather data, it is important for users to understand how MSC GeoMet handles time in WCS requests. By default, if no `TIME` or `DIM_REFERENCE_TIME` parameters are passed in the request, MSC GeoMet will, by default, return the closest time interval available for the latest model run.

If the user wants to make a request for another date and time, the `TIME` or `DIM_REFERENCE_TIME` can be used in a WCS GetCoverage request. Date and times must adhere to the ISO8601 standard and are always in UTC (Coordinate Universal Time).

</br>

#### <span class="badge badge-light">GeoMet-Climate</span>
</br>

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
</br>

#### <span class="badge badge-light">GeoMet-Weather</span>

Please refer to the page [WMS Handling Time](../WMS_en/#handling-time) section, as for GeoMet-Weather,
the `TIME` and `DIM_REFERENCE_TIME` usage is the same.

Note that the layers time metadata are not available in the WCS GetCapabilities or the WCS DescribeCoverage. The time metadata can only be access through the WMS GetCapabilities.
</br></br>


## Usage example

GeoMet-Climate and GeoMet-Weather WCS are used through the [Climate data extraction tool](https://climate-change.canada.ca/climate-data/#/) of the [Canadian Centre for Climate Services portal](https://www.canada.ca/en/environment-climate-change/services/climate-change/canadian-centre-climate-services.html).

One can select a variable, region of interest, temporal information and output format on the extraction tool to retrieve the raw coverage information.
</br></br>