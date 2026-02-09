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

    The `limit` parameter is used to define the maximum records to return in the response. The response size is limited to 10 000 features per query.</br>
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

    The paging strategy is commonly used when extract large amounts of data. For example, a client could page by 500 features to cycle through an entire station record, starting with the first 500 items and subsquently requesting the next 500 items, until all items are returned.</br>
        </br>
    [https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=01AP004&offset=0&limit=500](https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=01AP004&offset=0&limit=500)

    [https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=01AP004&offset=500&limit=500](https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=01AP004&offset=500&limit=500)</br>

    The above queries return the first 500 items and the next 500 items respectively. The client can then simply cycle through all items until there are no longer any records. This would constitute the entire record. The `/items` endpoint will also return a `next` link in the response, which can be used to retrieve the next page of results. The `next` link will contain the updated `offset` value for the next page of results.
    </br>

### <span class="badge badge-light">Filter the list of properties of a queried element</span>

Query a feature collection and return features for which the list of associated properties is restricted to the properties listed in the `properties=`. For example, the query below returns properties related to atmospheric pressure observations, in JSON format.
</br>

[https://api.weather.gc.ca/collections/swob-realtime/items?lang=en&offset=0&sortby=-date_tm-value&url=CYRV&properties=date_tm-value%2Cmslp%2Cmslp-uom%2Cmslp-qa&f=json](https://api.weather.gc.ca/collections/swob-realtime/items?lang=en&offset=0&sortby=-date_tm-value&url=CYRV&properties=date_tm-value%2Cmslp%2Cmslp-uom%2Cmslp-qa&f=json)

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

---------------------

## OGC API - Coverages

The [OGC API - Coverages](https://ogcapi.ogc.org/coverages/) standard specifies the fundamental API building blocks for interacting with coverages (raster data). The spatial data community uses the term "coverage" to refer to homogeneous sets of values ​​located in space and time, such as data from spatiotemporal sensors, images, simulation and statistics.

##### <span class="badge badge-info">GET collections/{coverageId}</span> - Coverage collection landing page

[https://api.weather.gc.ca/collections/climate:cmip5:historical:annual:anomaly](https://api.weather.gc.ca/collections/climate:cmip5:historical:annual:anomaly)

Retrieves detailed coverage metadata for the specified collection. The JSON response for this page displays the collection's geographic extent, grid size, temporal extent (if available), and any other additional dimensions. The collection root page also lists supported other collection-related links such as the collection schema (available fields) and coverage URLs for each format support by the collection.

##### <span class="badge badge-info">GET collections/{coverageId}/schema</span> - Coverage schema

[https://api.weather.gc.ca/collections/climate:cmip5:historical:annual:anomaly/schema](https://api.weather.gc.ca/collections/climate:cmip5:historical:annual:anomaly/schema)

Retrieves the schema of the coverage collection. The schema provides a list of available fields and their data types. The schema can be returned in JSON or HTML format and can be used to understand the available fields of the coverage data.


##### <span class="badge badge-info">GET collections/{coverageId}/coverage</span> - Coverage query with no parameters

[https://api.weather.gc.ca/collections/climate:cmip5:historical:annual:anomaly/coverage](https://api.weather.gc.ca/collections/climate:cmip5:historical:annual:anomaly/coverage)

Returns the coverage data for the specified collection. The response will include all available data for the collection, which may be a large amount of data. It is recommended to use query parameters to filter the data returned by the coverage query. The data can be returned in different formats, such as [CoverageJSON](https://covjson.org/), GRIB, or NetCDF, depending on the collection and its supported output formats. See the links contained in the collection's root page for its available formats.

##### <span class="badge badge-info">GET collections/{coverageId}/coverage?{params}</span> - Coverage with query parameters

Queries against coverage collections allow for spatial, temporal, and field filtering against the n-dimensionsal space of the coverage itself//. The first parameter of a query must be specified with `?` and subsequent parameters with `&`.

### <span class="badge badge-light">Spatial</span>

Query by bounding box (minx, miny,maxx, maxy).</br>
    </br>
[https://api.weather.gc.ca/collections/climate:cmip5:historical:annual:anomaly/coverage?f=json&bbox=-80.557251,42.561173,-75.135498,44.805224](https://api.weather.gc.ca/collections/climate:cmip5:historical:annual:anomaly/coverage?f=json&bbox=-80.557251,42.561173,-75.135498,44.805224)

### <span class="badge badge-light">Temporal</span>

Query for an instantaneous value for a single period if a "time" axis label is available, for this specific coverage:</br>
    </br>
[https://api.weather.gc.ca/collections/climate:cmip5:historical:annual:anomaly/coverage?f=json&datetime=1905](https://api.weather.gc.ca/collections/climate:cmip5:historical:annual:anomaly/coverage?f=json&datetime=1905)


Query for a time interval:</br>
    </br>
[https://api.weather.gc.ca/collections/climate:cmip5:historical:annual:anomaly/coverage?f=json&datetime=1901/1905](https://api.weather.gc.ca/collections/climate:cmip5:historical:annual:anomaly/coverage?f=json&datetime=1901/1905)

### <span class="badge badge-light">Schema field</span>

Query for a specifc coverage field listed in the coverage schema via the `properties` query parameter. For example, the query below retrieves coverage data for the schema field named "sit" (sea ice thickness).
</br></br>
[https://api.weather.gc.ca/collections/climate:cmip5:historical:annual:anomaly/coverage?properties=sit](https://api.weather.gc.ca/collections/climate:cmip5:historical:annual:anomaly/coverage?properties=sit)

### <span class="badge badge-light">Additional dimensions</span>

Query additional dimensions (other than the spatial and temporal, which are queried via the `bbox` and `datetime` query parameters respectively) with the `subset` query parameter. Additional available dimensions are listed under the `extent` key at the coverage collection root via the JSON response only.
    </br></br>
[https://api.weather.gc.ca/collections/climate:cmip5:historical:annual:anomaly/coverage?subset=percentile(25)](https://api.weather.gc.ca/collections/climate:cmip5:historical:annual:anomaly/coverage?subset=percentile(25))

### <span class="badge badge-light">Combination of filter parameters</span>

Query the coverage with a spatial filter, temporal filter, and for a specific coverage field via the `properties` query parameter.</br>
    </br>
Returns in json format by default:

[https://api.weather.gc.ca/collections/climate:cmip5:historical:annual:anomaly/coverage?bbox=-80.557251,42.561173,-75.135498,44.805224&properties=sfcWind&datetime=1901/1905 ](https://api.weather.gc.ca/collections/climate:cmip5:historical:annual:anomaly/coverage?bbox=-80.557251,42.561173,-75.135498,44.805224&properties=sfcWind&datetime=1901/1905 )


### <span class="badge badge-light">Export to GTiff or NetCDF format</span>

Queries pointing to collections pages can be exported in GTiff format and NetCDF format if available. Consult the root of a given coverage collection to identify the available response data formats. For example:

[https://api.weather.gc.ca/collections/climate:cmip5:projected:annual:absolute?f=json](https://api.weather.gc.ca/collections/climate:cmip5:projected:annual:absolute?f=json)

Under the `links` key, the available values for the `?f` parameter can be found. In this case the coverage data can be requested in JSON via `?f=json` or as NetCDF via `?f=NetCDF`.


---------------------

## OGC API - Advanced filtering with CQL2

GeoMet-OGC-API supports data filtering using Common Query Language (CQL2) though the `?filter` query parameter in the HTTP request. `CQL2` is an [OGC standard](https://docs.ogc.org/is/21-065r2/21-065r2.html) designed to support advanced query of geospatial data and perform filtering directly on the server. By using CQL2, clients can reduce the amount of data returned and retrieve only data of interest.


CQL2 allows users to construct flexible and precise queries based on feature attributes and geometry.</br>

* Exact matches: `=` match features where an attribute has exact value;</br>
* Partial string or keywords: `LIKE` with `%` wildcard;</br>
* Comparison operators: `>`, `<`, `>=`, `<=` filter numeric or temporal values;</br>
* Logical operators:`AND`, `OR`, `NOT` compare conditions;</br>
* Spatial predicates: `INTERCEPTS`, `DISJOINT` filter based on geometry.</br>

The full list of predicates available is accessible from the [OGC CQL2 standard](https://docs.ogc.org/is/21-065r2/21-065r2.html).

String values must be enclosed in single quotes `''` and the property path (`properties.attribute`) must exactly match the attribute name defined in the collection schema (is case-sensitive). For GeoMet-OGC-API collections the synthax is:
```html
https://api.weather.gc.ca/collections/{collectionID}/items?filter=<CQL2 expression>&<CQL2 expression>
```

---------------------
##### <span class="badge badge-info">1. Searching exact matches</span>

**1.1)** Filter all meteorological bulletin that have the type `CA`, and are from issuing office `AO`. </br>
```python
CQL2: ?filter=properties.type=CA AND properties.issuing_office=AO
```
[https://api.weather.gc.ca/collections/bulletins-realtime/items?filter=properties.type=CA AND properties.issuing_office=AO](https://api.weather.gc.ca/collections/bulletins-realtime/items?filter=properties.type=CA%20AND%20properties.issuing_office=AO)
</br> </br>

**1.2)** Filter `Climate - Daily Observations` by attribute `LOCAL_DAY`. Here, `LOCAL_DAY` must be in capital letters, as defined in schema.
```python
CQL2: ?filter=properties.LOCAL_DAY=15
```
[https://api.weather.gc.ca/collections/climate-daily/items?filter=properties.LOCAL_DAY=15](https://api.weather.gc.ca/collections/climate-daily/items?filter=properties.LOCAL_DAY=15)


---------------------
##### <span class="badge badge-info">2. Searching partial keywords</span>

CQL supports partial text matching using the `LIKE` operator. It allows you to search for substrings within text attributes by using the `%` character as a wildcard, which can represent zero or more characters. The comparison is case-insensitive, but search string **must** be entered as <u>lowercase</u> and in between <u>single quote</u>. If the attribute value contains multiple words, the `LIKE` predicate is applied to the entire text value, matching the pattern against any substring within it.

**2.1)** Find all `STATION_NAME` containing the keyword `LAKE`. In that case, `'%lak%'` matches case insensitive keywords such as `Lake, lak5, SPOKIN LAKE 4E, 2LAKE9, LaK`.</br>
```
CQL2: ?filter=properties.STATION_NAME LIKE '%lak%'
```
[https://api.weather.gc.ca/collections/climate-normals/items?filter=properties.STATION_NAME LIKE '%lak%'](https://api.weather.gc.ca/collections/climate-normals/items?filter=properties.STATION_NAME%20LIKE%20%27%lak%%27)
</br></br>

**2.2)** Filter only specific name of station whose name is (or is `NOT`) in a given list. The wildcard `%` can also be used in the list.</br>
```
CQL2: ?filter=properties.STATION_NAME NOT IN ('lake', 'river')
```
[https://api.weather.gc.ca/collections/climate-normals/items?filter=properties.STATION_NAME NOT IN ('lake', 'river')](https://api.weather.gc.ca/collections/climate-normals/items?filter=properties.STATION_NAME%20NOT%20IN%20(%27lake%27,%20%27river%27))
</br></br>

**2.3)** To filter for <u>more than a word</u>, you need two different `LIKE` predicates. In this case, specifying 'quinsam' `AND` 'river' allows to filter for station name containing **both** 'quinsam' and 'river' keywords. Using `OR` would return station name containing either 'quinsam', 'river' or both.</br>
```
CQL2: ?filter=properties.STATION_NAME LIKE '%quisam%' AND properties.STATION_NAME LIKE '%river%'
```
[https://api.weather.gc.ca/collections/climate-normals/items?filter=properties.STATION_NAME LIKE '%quinsam%' AND properties.STATION_NAME LIKE '%river%'](https://api.weather.gc.ca/collections/climate-normals/items?filter=properties.STATION_NAME%20LIKE%20%27%quinsam%%27%20AND%20properties.STATION_NAME%20LIKE%20%27%river%%27)
</br></br>

**2.4)** Extracts station name starting with the letter `K`. You can place the wildcard `%` accordingly. Here, you see that it is not necessarily the first word of the station name that is a match. The `LIKE` predicate will compare every keywords of the text.
```
CQL2: ?filter=properties.STATION_NAME LIKE 'k%'
```
[https://api.weather.gc.ca/collections/climate-normals/items?filter=properties.STATION_NAME LIKE 'k%'](https://api.weather.gc.ca/collections/climate-normals/items?filter=properties.STATION_NAME%20LIKE%20%27k%%27)

![CQL LIKE Wildcard Start](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-geomet/cql/CQL_Like_Wildcard_Start_en.png)
</br>

**2.5)** Extracts station name ending with the letter `T`. You can place the wildcard `%` accordingly. Here, you see that it is not necessarily the last word of the station name that is a match. The `LIKE` predicate will compare every keywords of the text.
```
CQL2: ?filter=properties.STATION_NAME LIKE '%t'
```
[https://api.weather.gc.ca/collections/climate-normals/items?filter=properties.STATION_NAME LIKE '%t'](https://api.weather.gc.ca/collections/climate-normals/items?filter=properties.STATION_NAME+LIKE+%27%25t%27&limit=10&offset=0)

![CQL LIKE Wildcard End](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-geomet/cql/CQL_Like_Wildcard_End_en.png)
</br>

**2.6)** Searching meteorological bulletins by the identifier. It's not possible to manually search by `id` on the interface. Users can use CQL filters and leverage the [bulletin filename nomenclature documentation](https://eccc-msc.github.io/open-data/msc-data/bulletins/readme_bulletins-datamart_en/#directory-and-file-name-nomenclature).</br>
```
CQL2: ?filter=properties.identifier LIKE '%WWCN70%'
```
[https://api.weather.gc.ca/collections/bulletins-realtime/items/?filter=properties.identifier LIKE '%wwcn70%'](https://api.weather.gc.ca/collections/bulletins-realtime/items/?filter=properties.identifier%20LIKE%20%27%wwcn70%%27)
</br></br>

**2.7)** Search bulletins with partial keyword `CYOY` in the url.
```
CQL2: ?filter=properties.type=SA AND properties.issuer_code=CWAO AND properties.url LIKE '%cyoy%'
```
[https://api.weather.gc.ca/collections/bulletins-realtime/items?filter=properties.type=SA AND properties.issuer_code=CWAO AND properties.url LIKE '%cyoy%'](https://api.weather.gc.ca/collections/bulletins-realtime/items?filter=properties.type=SA%20AND%20properties.issuer_code=CWAO%20AND%20properties.url%20LIKE%20%27%cyoy%%27) </br>

`?q=` is the "full text search" capability in the MSC GeoMet OGC API. The equivalent query is:
```html
https://api.weather.gc.ca/collections/bulletins-realtime/items?type=SA&issuer_code=CWAO&q=*CYOY*
```
</br>

**2.8)**  Search bulletins by type and issuer code.
```python
CQL2: ?filter=((properties.type=SA OR properties.type=SP) AND (properties.issuer_code=CWAO OR properties.issuer_code=CYOY))
```
[https://api.weather.gc.ca/collections/bulletins-realtime/items/?filter=((properties.type=SA OR properties.type=SP) AND (properties.issuer_code=CWAO OR properties.issuer_code=CYOY))](https://api.weather.gc.ca/collections/bulletins-realtime/items/?filter=((properties.type=SA%20OR%20properties.type=SP)%20AND%20(properties.issuer_code=CWAO%20OR%20properties.issuer_code=CYOY)))
</br>

---------------------
##### <span class="badge badge-info">3. Searching comparison operators</span>

CQL2 supports numeric comparisons using operators.

**3.1)** Filter for temperature `TEMP` values less than 10°C.
```python
CQL2: ?filter=properties.TEMP < 10
```
[https://api.weather.gc.ca/collections/climate-hourly/items?filter=properties.TEMP < 10](https://api.weather.gc.ca/collections/climate-hourly/items?filter=properties.TEMP%20%3C10)
</br></br>

**3.2)** Filter for Air Quality Health Index (AQHI) forecasts classified as low risk (1-3).
```python
CQL2: ?filter=properties.aqhi<=3
```
[https://api.weather.gc.ca/collections/aqhi-forecasts-realtime/items?filter=properties.aqhi<=3](https://api.weather.gc.ca/collections/aqhi-forecasts-realtime/items?filter=properties.aqhi%3C=3)
</br></br>

**3.3)** Filter for AQHI observations lower than 2 that is in a specified bounding box (Nova Scotia).
```python
CQL2: ?bbox=-70,42,-60,45&filter=properties.aqhi<2
```
[https://api.weather.gc.ca/collections/aqhi-observations-realtime/items?bbox=-70,42,-60,45&filter=properties.aqhi<2](https://api.weather.gc.ca/collections/aqhi-observations-realtime/items?bbox=-70,42,-60,45&filter=properties.aqhi%3C2)

![CQL Nova Scotia AQHI](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-geomet/cql/CQL_NovaScotia_AQHI_en.png)
</br>
---------------------
##### <span class="badge badge-info">4. Searching with logical operator</span>

CQL supports range-based filtering using the `BETWEEN` operator. This operator is inclusive for both boundary values. Using `BETWEEN` is the equivalent of `>=` and `<=`, but improves readability.
```
synthax: [`NOT`] <attribute> BETWEEN <lower_bound> AND <upper_bound>
```

**4.1)** Filter items for temperature `TEMP` between 10°C and 12.5°C. For numeric values (number), no quotes required.
```python
CQL2: ?filter=properties.TEMP BETWEEN 10 AND 12.5
```
[https://api.weather.gc.ca/collections/climate-hourly/items?filter=properties.TEMP BETWEEN 10 AND 12.5](https://api.weather.gc.ca/collections/climate-hourly/items?filter=properties.TEMP%20BETWEEN%2010%20AND%2015)
</br></br>

**4.2)** Filter for wind direction between north-northeast (NNE 23°) and northeast (NE 45°) and speed above 25 km/h.
```python
CQL2: ?filter=properties.WIND_DIRECTION BETWEEN 23 AND 45 AND properties.WIND_SPEED >= 25
```
[https://api.weather.gc.ca/collections/climate-hourly/items?filter=properties.WIND_DIRECTION BETWEEN 23 AND 45 AND properties.WIND_SPEED >= 25](https://api.weather.gc.ca/collections/climate-hourly/items?filter=properties.WIND_DIRECTION%20BETWEEN%2023%20AND%2045%20AND%20properties.WIND_SPEED%20%3E=%2025)
</br></br>

**4.3)** Filter items between two datetime. Datetime values must be enclosed in single quotes, because it is defined as `string` in the collection queryables.
```
CQL2: ?filter=properties.LOCAL_DATE BETWEEN '2023-11-28 14:00:00' AND '2024-11-28 14:00:00'
```
[https://api.weather.gc.ca/collections/climate-hourly/items?filter=properties.LOCAL_DATE BETWEEN '2023-11-28 14:00:00' AND '2024-11-28 14:00:00'](https://api.weather.gc.ca/collections/climate-hourly/items?limit=100&filter=properties.LOCAL_DATE+BETWEEN+%272023-11-28+14%3A00%3A00%27+AND+%272024-11-28+14%3A00%3A00%27)

![CQL Climate Hourly](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-geomet/cql/CQL_Schema_ClimateHourly_en.png)
</br>

**4.4)** Search for Air Quality Health Index observations with moderate risk only (`BETWEEN 4 AND 6`) in a `BBOX`.
```
CQL2: ?filter=BBOX(geometry, -140, 50, -85, 63) AND properties.aqhi BETWEEN 4 AND 6
CQL2: ?filter=BBOX(geometry, -140, 50, -85, 63) AND properties.aqhi>=7 (high risk)
```
[https://api.weather.gc.ca/collections/aqhi-observations-realtime/items?filter=BBOX(geometry, -140, 50, -85, 63) AND properties.aqhi BETWEEN 4 AND 6](https://api.weather.gc.ca/collections/aqhi-observations-realtime/items?filter=BBOX(geometry,%20-140,%2050,%20-85,%2063)%20AND%20properties.aqhi%20BETWEEN%204%20AND%206)
</br>

---------------------
##### <span class="badge badge-info">5. Spatial searches</span>

Spatial searches allow users to personalize their queries based on geographical locations.

**5.1)** Find features that `INTERSECTS` a polygon. Returns all features that touch, crosses, fall in or overlaps a polygon. A polygon of `x` sides has to have `x+1` points because the last point repeats the first one to close the shape of the polygon. Specify the longitude fist, then the latitude. </br>
```python
CQL2: ?filter=INTERSECTS(geometry, POLYGON((lon_1 lat_1,lon_2 lat_2,lon_3 lat_3,lon_4 lat_4,lon_1 lat_1)))
CQL2: ?filter=INTERSECTS(geometry, POLYGON((-56 47,-55 47,-55 48,-56 48,-56 47)))
```
[https://api.weather.gc.ca/collections/swob-stations/items?filter=INTERSECTS(geometry, POLYGON((-56 47,-55 47,-55 48,-56 48,-56 47)))](https://api.weather.gc.ca/collections/swob-stations/items?filter=INTERSECTS(geometry,%20POLYGON((-56%2047,-55%2047,-55%2048,-56%2048,-56%2047))))
→ Returns all SWOB stations intersecting the polygon that has a width of 1 degree (west-east longitudes) and a height of 1 degree (north-south latitude).</br>
</br></br>

**5.2)** Find features with `DISJOINT`. Returns all features outside of a polygon, that do not intersect the geometry. It is the opposite of `INTERSECTS`.
```python
CQL2: ?filter=DISJOINT(geometry, POLYGON((lon_1 lat_1,lon_2 lat_2,lon_3 lat_3,lon_4 lat_4,lon_1 lat_1)))
CQL2: ?filter=DISJOINT(geometry, POLYGON((-80 42,-50 42,-50 60,-80 60,-80 42)))
```
[https://api.weather.gc.ca/collections/swob-stations/items?filter=DISJOINT(geometry, POLYGON((-80 42,-50 42,-50 60,-80 60,-80 42)))](https://api.weather.gc.ca/collections/swob-stations/items?filter=DISJOINT(geometry,%20POLYGON((-80%2042,-50%2042,-50%2060,-80%2060,-80%2042))))
→ Returns all SWOB stations that **do not** intersect the polygon that has a width of 30 degrees (longitudes) and 18 degrees (latitudes) in Eastern Canada.</br>
![CQL SWOB station](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-geomet/cql/CQL_SWOB_Station_en.png)

---------------------


##### <span class="badge badge-info">6. Examples of multi-parameter filtering</span>

**6.1)** Filtering `Climate - Daily Observations` for a weather station in Lanaudiere for wet and warms summer months for a station where:</br>

* The `CLIMATE_IDENTIFIER` is 7014160 (L'Assomption station);</br>
* The `MEAN_TEMPERATURE` is 18°C and 28°C;</br>
* The `TOTAL_PRECIPITATION` is between 5 and 40 mm;</br>
* The `LOCAL_YEAR` is between 2010 and 2020;</br>
* The `LOCAL_MONTH` is between June and September (JJAS).</br>
```
CQL2: ?filter=CLIMATE_IDENTIFIER = '7014160' AND properties.MEAN_TEMPERATURE BETWEEN 18 AND 28 AND properties.TOTAL_PRECIPITATION BETWEEN 5 AND 40 AND properties.LOCAL_YEAR BETWEEN 2010 AND 2020 AND properties.LOCAL_MONTH BETWEEN 6 AND 9
```
[https://api.weather.gc.ca/collections/climate-daily/items?filter=CLIMATE_IDENTIFIER = '7014160' AND properties.MEAN_TEMPERATURE BETWEEN 18 AND 28 AND properties.TOTAL_PRECIPITATION BETWEEN 5 AND 40 AND properties.LOCAL_YEAR BETWEEN 2010 AND 2020 AND properties.LOCAL_MONTH BETWEEN 6 AND 9](https://api.weather.gc.ca/collections/climate-daily/items?filter=properties.CLIMATE_IDENTIFIER=%277014160%27%20AND%20properties.MEAN_TEMPERATURE%20BETWEEN%2018%20AND%2028%20AND%20properties.TOTAL_PRECIPITATION%20BETWEEN%205%20AND%2040%20AND%20properties.LOCAL_YEAR%20BETWEEN%202010%20AND%202020%20AND%20properties.LOCAL_MONTH%20BETWEEN%206%20AND%209)

![CQL Assomption Station](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-geomet/cql/CQL_Items_AssomptionStation_en.png)
</br>

**6.2)** Find all AQHI observations in a polygon around Calgary for today where the AQHI value is greater than 6 (high risk) within a polygon.
```python
CQL2: ?filter=INTERSECTS(geometry,POLYGON((-114.2 50.9, -113.8 50.9, -113.8 51.2, -114.2 51.2, -114.2 50.9))) AND properties.aqhi>6
```
[https://api.weather.gc.ca/collections/aqhi-observations-realtime/items?filter=INTERSECTS(geometry,POLYGON((-114.2 50.9, -113.8 50.9, -113.8 51.2, -114.2 51.2, -114.2 50.9))) AND properties.aqhi>4](https://api.weather.gc.ca/collections/aqhi-observations-realtime/items?filter=INTERSECTS(geometry,POLYGON((-114.2%2050.9,%20-113.8%2050.9,%20-113.8%2051.2,%20-114.2%2051.2,%20-114.2%2050.9)))%20AND%20properties.aqhi%3E4&lang=en)

![CQL Intersects Calgary](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-geomet/cql/CQL_Intersects_Calgary_en.png)
</br>

**6.3)** Retrieve meteorogical stations meeting all of the following conditions: </br>

* Located within a specified polygon (Western canada region) with `INTERSECTS`; </br>
* Have a station containing the keyword "LAKE" with `LIKE`;</br>
* Reports minimum temperature `BETWEEN` -20 and -10°C;</br>
* Either have maximum speed gusts above 20 km/h.</br>
```python
CQL2: ?filter=INTERSECTS(geometry,POLYGON((-140 48,-95 48,-95 60,-140 60,-140 48))) AND properties.STATION_NAME LIKE '%lake%' AND properties.MIN_TEMPERATURE BETWEEN -20 AND -10 AND properties.SPEED_MAX_GUST >= 20
```
[https://api.weather.gc.ca/collections/climate-daily/items?filter=INTERSECTS(geometry,POLYGON((-140 48,-95 48,-95 60,-140 60,-140 48))) AND properties.STATION_NAME LIKE '%lake%' AND properties.MIN_TEMPERATURE BETWEEN -20 AND -10 AND properties.SPEED_MAX_GUST >= 20](https://api.weather.gc.ca/collections/climate-daily/items?filter=INTERSECTS(geometry,POLYGON((-140%2048,-95%2048,-95%2060,-140%2060,-140%2048)))%20AND%20properties.STATION_NAME%20LIKE%20%27%lake%%27%20AND%20properties.MIN_TEMPERATURE%20BETWEEN%20-20%20AND%20-10%20AND%20properties.SPEED_MAX_GUST%20%3E=%2020)
 </br></br>

**6.4a)** Identify regions of elevated risk of wildfire (dry, hot and windy conditions) for the 2025 wildfire season.</br>

* During the wildfire 2025 season (April to October);</br>
* High temperatures (`>=` 30°C);</br>
* Low relative humidity (`<=` 30%);</br>
* Strong winds (speed `>=` 30 km/h).</br>
```python
Climate - Hourly Observations
CQL2: ?filter=properties.LOCAL_YEAR=2025 AND properties.LOCAL_HOUR=12 AND properties.LOCAL_MONTH BETWEEN 4 AND 10 AND properties.TEMP >=30 AND properties.RELATIVE_HUMIDITY <=30 AND properties.WIND_SPEED >= 30
```
[https://api.weather.gc.ca/collections/climate-hourly/items?filter=properties.LOCAL_YEAR=2025 AND properties.LOCAL_HOUR=12 AND properties.LOCAL_MONTH BETWEEN 5 AND 8 AND properties.TEMP >=30 AND properties.RELATIVE_HUMIDITY <=30 AND properties.WIND_SPEED >= 30](https://api.weather.gc.ca/collections/climate-hourly/items?filter=properties.LOCAL_YEAR=2025%20AND%20properties.LOCAL_HOUR=12%20AND%20properties.LOCAL_MONTH%20BETWEEN%205%20AND%208%20AND%20properties.TEMP%20%3E=30%20AND%20properties.RELATIVE_HUMIDITY%20%3C=30%20AND%20properties.WIND_SPEED%20%3E=%2030%20&f=json)
</br></br>

**6.4b)** Using the same conditions as for the hourly observations, now we add the `24h` total precipitation amount from `Climate - Daily observations` to account for the dryness. Total rainfall over 24 hours less than an arbitrary value of 3 mm.
```python
Climate - Daily Observations
CQL2: ?filter=properties.LOCAL_YEAR=2025 AND properties.LOCAL_MONTH BETWEEN 4 AND 10 AND properties.MAX_TEMPERATURE>=30 AND properties.MIN_REL_HUMIDITY<=30 AND properties.SPEED_MAX_GUST>30 AND properties.TOTAL_PRECIPITATION<=3
```
[https://api.weather.gc.ca/collections/climate-daily/items?filter=properties.LOCAL_YEAR=2025 AND properties.LOCAL_MONTH BETWEEN 5 AND 8 AND properties.MAX_TEMPERATURE>=30 AND properties.MIN_REL_HUMIDITY<=30 AND properties.SPEED_MAX_GUST>30 AND properties.TOTAL_PRECIPITATION<=3](https://api.weather.gc.ca/collections/climate-daily/items?filter=properties.LOCAL_YEAR=2025%20AND%20properties.LOCAL_MONTH%20BETWEEN%205%20AND%208%20AND%20properties.MAX_TEMPERATURE%3E=30%20AND%20properties.MIN_REL_HUMIDITY%3C=30%20AND%20properties.SPEED_MAX_GUST%3E30%20AND%20properties.TOTAL_PRECIPITATION%3C=3%20&f=json)

![CQL URL Wildfire](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-geomet/cql/CQL_URL_Wildfire_en.png)
![CQL Wildfire](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-geomet/cql/CQL_Wildfire_en.png)
---------------------

##### <span class="badge badge-info">Curl command and Python</span>

It was shown that it's possible to make `HTTP` request with CQL filters directly in the search bar of the search engine. It's also possible to retrieve the data via the `curl` command in the terminal. To save the output of what the request returns, use the `-o` option.

* Using curl with the full encoded url.
```
curl [encoded_url] [option]
curl https://api.weather.gc.ca/collections/climate-hourly/items?filter=properties.WIND_DIRECTION%20BETWEEN%2023%20AND%2045%20AND%20properties.WIND_SPEED%20%3E=%2025%20&lang=en -o /path/to/output_file.json
```
* Encoding the url directly with the `--data-urlencode` and `-G` GET request options. Users can add multiple `--data-urlencode` parameters (equivalent to `&`).
```
curl -G [basepath] --data-urlencode [CQL EXPRESSION]
curl -G "https://api.weather.gc.ca/collections/climate-hourly/items?" --data-urlencode "filter=properties.WIND_DIRECTION BETWEEN 23 AND 45 AND properties.WIND_SPEED >=25" --data-urlencode "lang=en"
```

**Query with Python** <br>
To parse CQL filters and make HTTP requests, install the `pygeofilter` and `requests` Python modules.

```bash
pip3 install pygeofilter requests
```
```python
import requests
import json
from pygeofilter.parsers.ecql import parse

# GeoMet-OGC-API endpoint.
api_url = "https://api.weather.gc.ca/collections/climate-daily/items"

# CQL filters.
cql_filter = (
    "properties.LOCAL_YEAR = 2025 AND "
    "properties.LOCAL_MONTH BETWEEN 6 AND 9 AND "
    "properties.MAX_TEMPERATURE >= 30"
)
# Validate CQL filters before API request.
try:
    parse(cql_filter)
except Exception as e:
    raise ValueError(f"Invalid CQL filter: {e}")

params = {
    "filter": cql_filter,
    "lang": "en",
    "limit": 100
}
# Sends GET request to the API and encode url.
response = requests.get(api_url, params=params)
print(f"The encoded url is: {response.url}")

# Format json in output file.
data = response.json()
climate_output_file = "climate_daysAbove30deg_JJAS_2025.json"
with open(climate_output_file, "w") as fh:
    json.dump(data, fh)
```
