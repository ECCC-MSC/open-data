[En français](ogc_api_fr.md)

![ECCC logo](../img_eccc-logo.png)

[TdM](../readme_en.md) > [MSC GeoMet](readme_en.md) > OGC API

# OGC API
The Open Geospatial Consortium (OGC) API standards are a set of specifications developed by the OGC to facilitate the interoperable exchange of geospatial data and services over the web. These standards are designed to enable seamless integration and sharing of geospatial information across different systems, applications, and organizations. The following documentation will go over the basics of the OGC API - Features and OGC API - Coverages standards and provide examples of how to query GeoMet-OGC-API using these standards.

## Main endpoints

##### <span class="badge badge-info">GET /</span> - Landing page
[https://api.weather.gc.ca/](https://api.weather.gc.ca/)

The GeoMet-OGC-API landing page with links to view the data collections, processes, and conformance classes implemented by the API.
</br>

##### <span class="badge badge-info">GET /collections</span> - All data collections
[https://api.weather.gc.ca/collections](https://api.weather.gc.ca/collections)

Retrieves information describing the set of supported collections and provides a list of collections with data type and a brief description.

##### <span class="badge badge-info">GET collections/{collectionID}</span> - Collection-specific information
[https://api.weather.gc.ca/collections/hydrometric-daily-mean](https://api.weather.gc.ca/collections/hydrometric-stations)

Retrieves descriptive information about a specific collection, either of type feature or type coverage. For example, the URL above returns
the root page for the Hydrometric Monitoring Stations feature collection.

##### <span class="badge badge-info">GET /openapi</span> - OpenAPI documentation
[https://api.weather.gc.ca/openapi](https://api.weather.gc.ca/openapi)

The API documentation links provide a Swagger page of the API as a tool for developers to provide example request/response/query capabilities. A JSON representation is also provided.
</br>

##### <span class="badge badge-info">GET /conformance</span> - API conformance definition
[https://api.weather.gc.ca/conformance](https://api.weather.gc.ca/conformance)

The conformance page provides a list of URLs corresponding to the OGC API conformance classes supported by GeoMet-OGC-API.
</br>

## <strong>Common Query Parameters</strong>
The following section provides information regarding common query parameters often used when making requests to both feature and coverage collections. Query parameters are passed with the request URL using the `?` character to separate the query parameter from the URL and the `&` character to separate multiple query parameters.

##### <span class="badge badge-info">f</span> - Format query parameter
[https://api.weather.gc.ca/collections/?f=json](https://api.weather.gc.ca/collections/?f=json)

The format query paremeter is used to specify the format of the server response. Depending on the collection type, the value of the format query parameter could be one of of the following: html, json. The example above returns the list of available collections from GeoMet-OGC-API as a JSON object.

For feature collections, results can also be returned as a CSV file via `?f=csv`.

For coverage collections, the output format of the coverage can be specified via this parameter. Depending on the collection and its supported output formats, the following values are supported: `GRIB`, `GTiff`, and `NetCDF` in GeoMet-OGC-API but their support is on a per coverage collection basis.

##### <span class="badge badge-info">bbox</span> - Bounding box query parameter
[https://api.weather.gc.ca/collections/aqhi-observations-realtime/items?bbox=-71,46,-65,49](https://api.weather.gc.ca/collections/aqhi-observations-realtime/items?bbox=-71,46,-65,49)

Retrieves information according to a specific region or bounding box. It is a rectangular area defined by two sets of coordinates that represent the minimum and maximum extents of the box. `bbox` coordinate values must be fall within the bounds of [EPSG:4326](https://epsg.io/4326). The coordinates specified must be in the following order: `minX, minY, maxX, maxY`.

##### <span class="badge badge-info">datetime</span> - Datetime query parameter
[https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?datetime=1972-10-30](https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?datetime=1972-10-30)

Retrieves information according to a specific date, year or time interval. It is highly recommend to use RFC 3339 compliant datetime strings (i.e. `YYYY-MM-DD` or `YYYY-MM-DDTHH:MM:SSZ`). The datetime parameter can be used in conjunction with the `..` keyword to specify a time extent. For example, `datetime=2012-05-20/..` returns all items from 2015-05-20 onwards. `datetime=../2015-11-11` returns all items older than 2015-11-11.
</br></br>

## OGC API - Features

The [OGC API - Features](https://ogcapi.ogc.org/features/) (OAFeat) standard provides a list of standardized specifications for querying vector-based geospatial data (points, lines and polygons) on the web. Listed below are example OGC-API feature collection endpoints, examples for spatial, temporal and property filtering, and further details regarding pagination.

##### <span class="badge badge-info">GET collections/{collectionID}/items</span> - Feature collection items
[https://api.weather.gc.ca/collections/hydrometric-daily-mean/items](https://api.weather.gc.ca/collections/hydrometric-daily-mean/items)

Returns items from a specified collection.

The above URL returns items from the `hydrometric-daily-mean` collection:
![Hydrometric Daily Mean Items](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-geomet/GET_items.png)

##### <span class="badge badge-info">GET collections/{collectionID}/items/{itemID}</span> - Single feature overview
[https://api.weather.gc.ca/collections/hydrometric-daily-mean/items/01AA002](https://api.weather.gc.ca/collections/hydrometric-stations/items/01AA002)

Returns the item with the corresponding ID from the requested collection and provides its full set of properties.

The above URL returns the item with ID `01AA002` from the `hydrometric-stations` collection:
![Item 01AA002](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-geomet/GET_itemID_01AA002.png)
</br>

##### <span class="badge badge-info">GET collections/{collectionID}/items?{query parameters}</span> - Query a feature collection

Feature collection queries allow for spatial, temporal, and property filtering. Filter parameters can be combined to formulate a more complex query. The first parameter of a query must be specified with `?` and subsequent parameters with `&`.</br>
</br>
Below are a few examples of various types of queries, ranging from simple bbox and datetime filtering queries to more complex queries comprised of multiple query parameters. All queries are made to the [hydometric-daily-mean](https://api.weather.gc.ca/collections/hydrometric-daily-mean) feature collection.


### <span class="badge badge-light">Spatial</span>

 Query by bounding box (minx, miny,maxx, maxy).</br>
</br>
[https://api.weather.gc.ca/collections/hydrometric-stations/items?bbox=-71,46,-65,49](https://api.weather.gc.ca/collections/hydrometric-stations/items?bbox=-71,46,-65,49)

Returns items from the feature collection that intersect the provided bounding box:
![Map with selected area](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-geomet/GET_items_bbox.png)

### <span class="badge badge-light">Temporal</span>

Query for an instantaneous value with a single date:</br>
</br>
[https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?datetime=1972-10-30](https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?datetime=1972-10-30)

Returns feature collection items that match the provided datetime value:
![Items from collection that match datetime](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-geomet/GET_items&_1_datetime.png)

Query for a time interval:</br>
</br>
[https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?datetime=1972-10-30/2010-07-31](https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?datetime=1972-10-30/2010-07-31)

Returns feature collection items that fall within the provided datetime range:
![Items from collection that fall within the provided datetime range](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-geomet/GET_items&_intervalle_datetime.png)

Query by time extent with the open ended `..` keyword:

*   Since a specific datetime:</br>
    [https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?f=json&STATION_NUMBER=07DA006&datetime=2012-05-20/..](https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?f=json&STATION_NUMBER=07DA006&datetime=2012-05-20/..)

*   Returns feature collection items from 2015-05-20 onwards.

    Until a specific datetime:</br>
    [https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?f=json&STATION_NUMBER=07DA006&datetime=../2015-11-11](https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?f=json&STATION_NUMBER=07DA006&datetime=../2015-11-11)</br>

    Returns feature collection items older than 2015-11-11.

### <span class="badge badge-light">Property</span>

Query by an entity collection property:</br>

[https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=10CD001](https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=10CD001)

Returns feature collection items that have `STATION_NUMBER = 10CD001`
![Features by station number](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-geomet/GET_items_stationNumber.png)


### <span class="badge badge-light">Paging</span>

*   #### <span class="badge badge-light">Offset</span>
    The `offset` parameter can be used to specify the record to start at when extracting
    features. The default value is `0` (first feature).</br>
    </br>
*    #### <span class="badge badge-light">Total number of items</span>

    The `resulttype=hits` parameter is used to return the number of features found in a collection, without returning any features from the collection. The number of features is found in the response's `numberMatched` key.</br>

    [https://api.weather.gc.ca/collections/ltce-stations/items?f=json&resulttype=hits](https://api.weather.gc.ca/collections/ltce-stations/items?f=json&resulttype=hits)

    ![numberMatched](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-geomet/numberMatched.png)

*   #### <span class="badge badge-light">Limit</span>

    The `limit` parameter is used to define the maximum records to return in the response. The default response size is 500 features.</br>
    In the following query, a single entity is requested, for example, to inspect its geometry and properties:
    </br></br>

    [https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?limit=1](https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?limit=1)

    Returns a single feature from the collection:

    ![Items with a limit of 1](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-geomet/GET_items_limit.png)

    The `offset` and `limit` parameters can be used in tandem to cycle through feature collections. The examples below demonstrate how to adjust and page through query results.

    *   Query and limit to items 1 to 100:</br>

        [https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=10CD001&limit=100](https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=10CD001&limit=100)

    *   Query and limit to items 101-200:</br>

        [https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=10CD001&offsetx=101&limit=100](https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=10CD001&offset=101&limit=100)
        </br>

*   #### <span class="badge badge-light">Strategies for paging</span>

    The paging strategy is commonly used when extract large amounts of data. For example, a client could page by 1000 features to cycle through an entire station record, starting with the first 1000 items and subsquently requesting the next 1000 items, until all items are returned.</br>
        </br>
    [https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=01AP004&offset=0&limit=1000](https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=01AP004&offset=0&limit=1000)

    [https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=01AP004&offset=1000&limit=1000](https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=01AP004&offset=1000&limit=1000)</br>

    The above queries return the first 1000 items and the next 1000 items respectively.
    The client can then simply cycle through all items until there are no longer any records. This would constitute the entire record.
    </br>

### <span class="badge badge-light">Combining filter parameters</span>

Query all hydrometric daily mean data from a single station between 2001 and 2010:</br>

[https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=10CD001&datetime=2001-01-01/2010-12-31](https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=10CD001&datetime=2001-01-01/2010-12-31)

### <span class="badge badge-light">Exporting to CSV format</span>

Results from queries made against feature collections can be exported to the CSV format by adding `&f=csv` to the request, or by clicking on the `CSV` top-right icon on the collection page.</br>

[https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?f=csv](https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?f=csv)

### <span class="badge badge-light">Sorting</span>

Results from a query can be sorted by using the `sortby` parameter. By default, the sort order is ascending. For a descending sort, add the `-` (minus) character prior to the property name. Sorting by multiple properties is supported by providing a comma-separated list of properties to the `sortby` query parameter.</br>
    </br>
`&sortby=PROPERTY` sorts the property in ascending order
`&sortby=-PROPERTY` sorts the property in descending order.

Examples with the `DATE` property:

[https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=01AP004&offset=1000&limit=1000&sortby=DATE]( https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=01AP004&offset=1000&limit=1000&sortby=DATE) `ascending`

[https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=01AP004&offset=1000&limit=1000&sortby=-DATE]( https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=01AP004&offset=1000&limit=1000&sortby=-DATE) `descending`


## OGC API - Coverages

The [OGC API - Coverages](https://ogcapi.ogc.org/coverages/) standard specifies the fundamental API building blocks for interacting with coverages (raster data). The spatial data community uses the term "coverage" to refer to homogeneous sets of values ​​located in space and time, such as data from spatiotemporal sensors, images, simulation and statistics.

##### <span class="badge badge-info">GET collections/{coverageId}</span> - Coverage collection landing page

[https://api.weather.gc.ca/collections/climate:cmip5:historical:annual:anomaly](https://api.weather.gc.ca/collections/climate:cmip5:historical:annual:anomaly)

Retrieves detailed coverage metadata for the specified collection. This page displays the collections geographic extent, supported output forms and related links.


##### <span class="badge badge-info">GET collections/{coverageId}/coverage</span> - Coverage query with no parameters

[https://api.weather.gc.ca/collections/climate:cmip5:historical:annual:anomaly/coverage](https://api.weather.gc.ca/collections/climate:cmip5:historical:annual:anomaly/coverage)

Retrieves the coverage data and related self-describing information (range set, domain set, range type, metadata). It is comparable to a WCS GetCoverage response. By default, the response is returned as JSON. The URL above returns the entire coverage data for the default coverage field "tas" (surface temperature).


##### <span class="badge badge-info">GET collections/{coverageId}/coverage/rangetype</span> - Coverage range type

[https://api.weather.gc.ca/collections/climate:cmip5:historical:annual:anomaly/coverage/rangetype?](https://api.weather.gc.ca/collections/climate:cmip5:historical:annual:anomaly/coverage/rangetype?)

Returns the range type of the coverage, that is, the semantics of the data values ​​(their components and the data type). The range type response returns a list of fields that can be queried against the coverage. For example, the query below returns the range type for the CMIP5 Historical annual anomaly collection.
![RangeType](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-geomet/COV_rangeType.png)

##### <span class="badge badge-info">GET collections/{coverageId}/coverage/domainset</span> - Coverage domain set

[https://api.weather.gc.ca/collections/climate:cmip5:historical:annual:anomaly/coverage/domainset](https://api.weather.gc.ca/collections/climate:cmip5:historical:annual:anomaly/coverage/domainset)

Returns the domain of the coverage (the detailed n-dimensional space covered by the data). Domains include available axis labels, extent of coverage, pixel size, and resolution.

![Domainset](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-geomet/COV_domainset.png)

##### <span class="badge badge-info">GET collections/{coverageId}/coverage?{params}</span> - Coverage with query parameters

Queries against coverage collections allow for spatial, temporal, and range type filtering against the n-dimensionsal space (domain set axes) of the coverage itself. The first parameter of a query must be specified with `?` and subsequent parameters with `&`.

### <span class="badge badge-light">Spatial</span>

Query by bounding box (minx, miny,maxx, maxy).</br>
    </br>
[https://api.weather.gc.ca/collections/climate:cmip5:historical:annual:anomaly/coverage?f=json&bbox=-80.557251,42.561173,-75.135498,44.805224](https://api.weather.gc.ca/collections/climate:cmip5:historical:annual:anomaly/coverage?f=json&bbox=-80.557251,42.561173,-75.135498,44.805224) or
[https://api.weather.gc.ca/collections/climate:cmip5:historical:annual:anomaly/coverage?f=json&bbox=-80.557251,42.561173,-75.135498,44.805224&f=NetCDF](https://api.weather.gc.ca/collections/climate:cmip5:historical:annual:anomaly/coverage?f=json&bbox=-80.557251,42.561173,-75.135498,44.805224&f=NetCDF)


### <span class="badge badge-light">Temporal</span>

Query for an instantaneous value for a single period if a "time" axis label is available, for this specific coverage:</br>
    </br>
[https://api.weather.gc.ca/collections/climate:cmip5:historical:annual:anomaly/coverage?f=json&datetime=1905](https://api.weather.gc.ca/collections/climate:cmip5:historical:annual:anomaly/coverage?f=json&datetime=1905)


Query for a time interval:</br>
    </br>
[https://api.weather.gc.ca/collections/climate:cmip5:historical:annual:anomaly/coverage?f=json&datetime=1901/1905](https://api.weather.gc.ca/collections/climate:cmip5:historical:annual:anomaly/coverage?f=json&datetime=1901/1905)

### <span class="badge badge-light">Rangetype field</span>

Query for a specifc range type field with the `properties` query parameter. For example, the query below retrieves coverage data for the rangetype field named "sit" (sea ice thickness).
</br></br>
[https://api.weather.gc.ca/collections/climate:cmip5:historical:annual:anomaly/coverage?properties=sit](https://api.weather.gc.ca/collections/climate:cmip5:historical:annual:anomaly/coverage?properties=sit)

### <span class="badge badge-light">Domain set dimension</span>

Query by a dimension specificied in the domain set with the `subset` query parameter.
    </br></br>
[https://api.weather.gc.ca/collections/climate:cmip5:historical:annual:anomaly/coverage?subset=percentile(25)](https://api.weather.gc.ca/collections/climate:cmip5:historical:annual:anomaly/coverage?subset=percentile(25))

### <span class="badge badge-light">Combination of filter parameters</span>

Query the coverage with a spatial and temporal filter, for a a specific rangetype field via the `properties` query parameter.</br>
    </br>
Returns in json format by default:

[https://api.weather.gc.ca/collections/climate:cmip5:historical:annual:anomaly/coverage?bbox=-80.557251,42.561173,-75.135498,44.805224&properties=sfcWind&datetime=1901/1905 ](https://api.weather.gc.ca/collections/climate:cmip5:historical:annual:anomaly/coverage?bbox=-80.557251,42.561173,-75.135498,44.805224&properties=sfcWind&datetime=1901/1905 )


### <span class="badge badge-light">Export to GTiff or NetCDF format</span>

Queries pointing to collections pages can be exported in GTiff format and NetCDF format if available. Consult the root of a given coverage collection to identify the available response data formats. For example:

[https://api.weather.gc.ca/collections/climate:cmip5:projected:annual:absolute?f=json](https://api.weather.gc.ca/collections/climate:cmip5:projected:annual:absolute?f=json)

Under the `links` key, the available values for the `?f` parameter can be found. In this case the coverage data can be requested in JSON via `?f=json` or as NetCDF via `?f=NetCDF`.