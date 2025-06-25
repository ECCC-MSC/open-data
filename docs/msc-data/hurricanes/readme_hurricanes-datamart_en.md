[En français](readme_hurricanes-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [Hurricane trajectories](readme_hurricanes_en.md) > Hurricane trajectories on MSC Datamart

# Data of the hurricane trajectories

This page describes the data of the [hurricane trajectories](readme_hurricanes_en.md) available on the MSC Datamart in shapefile and GeoJSON format

There is four shapefiles (*.shp) formats that are produced and include each a 6-hour forecast bulletin when storms of tropical origin threatens or risks to threaten Canadian territory.

NOTES:

* Hurricane tracks in the Atlantic region, from the [NOAA National Hurricane Center](https://www.nhc.noaa.gov/) are republished by the [Canadian Hurricane Centre](https://www.canada.ca/en/environment-climate-change/services/hurricane-forecasts-facts/products.html) and are also available in GeoJSON format (but not in Shapefile format).
* Data in GeoJSON format is currently shared as experimental data because the format used does not comply with the latest [RFC7946](https://datatracker.ietf.org/doc/html/rfc7946) specifications. Once the format has been corrected in autumn 2025, this data will be hosted on the MSC Datamart as operational data and will replace the shapefile data. An announcement will be made via the [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info) mailing list.

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available via the HTTPS protocol. It is possible to access it with a standard browser. In this case, we obtain a list of links giving access to shapefile or GeoJSON files, according to the selected format.

* __Data in shapefile format__ can be found at this address:

    * [https://dd.weather.gc.ca/trajectoires/hurricane/shapefile/{NAME}](https://dd.weather.gc.ca/trajectoires/hurricane/shapefile)

With {NAME} : hurricane name in uppercase (e.g. 'BERTHA')

* __Data in GeoJSON format__ can be found on the MSC testing data repository DD-Alpha, at this address:

    * [https://dd.alpha.weather.gc.ca/hurricanes](https://dd.alpha.weather.gc.ca/hurricanes)

## File name nomenclature

File naming convention is:

* __Data in shapefile format__

`{YYYYMMDD}_{HHMM}Z_{NAME}.{TYPE}.shp`

where:

* __YYYYMMDD__ : Forecast issuance date
* __HHMM__ : Time in UTC 
* __Z__ : Constant string, indicating Zulu time (UTC code name)
* __NAME__ : Hurricane name (e.g. BERTHA)
* __TYPE__ : Type of shapefile:

    * "pts" - The forecast locations (points) 
    * "lin" - The line segments connecting forecast track points
    * "rad" - Contains forecast wind radii information (wind quadrants)
    * "err" - Contains information on track forecast error ("error cone")
	
When querying the points (pts) shapefile, the contents of each column are given as follows:

| Element   |   Description    |
|-----------|------------------|
|ADVDATE  |	Forecast issue time YYMMDD/HHMM format (UTC)|
|BASIN  |	Region - 'al' for Atlantic (always 'al' for Canadian Hurricane Centre)|
|DATELBL |	Label to use on a map|
|ERRCT |	Track forecast error radius in nautical miles which, when mapped, represents the zone/cone of average uncertainty in the track (storm centre) forecast  |
|LAT |	Latitude of storm centre position|
|LON |		Longitude of storm centre position|
|MAXWND |		Intensity - maximum sustained wind in knots (nautical miles per hour).  To get km/h, multiply by 1.84|
|MSLP  |	Minimum central pressure in millibars|
|RXXYY Columns |	Twelve columns represent wind radii (R) in nautical miles for 3 primary forcast categories: 34 (34 kts gale-force winds), 48 (48 kts storm-force winds), and 64 (64 kts hurricane-force wind speed). NE, SE, SW, NW represent the 4 primary geographcal quadrants around the storm.|
|STORMNAME |	Same as in the filename - e.g. BERTHA|
|STORMTYPE |	Storm type at forecast issue time: TD = tropical depression; TS = tropical storm; HU = hurricane; PT = post-tropical|
|TAU |		Forecast hour from issue time. e.g. 48 = 48 hours / 2 days|
|TCDVLP |		Storm status at forecast time TAU (TD,TS,HU,PT) |
|TIMEZONE |	Local time zone reflecting geographical region of an active storm|
|VALIDTIME |	Time that the forecast at TAU hours is valid for. DD/HHMM format (UTC) |
|TIMESTAMP |     ISO format for the VALIDTIME. Format:  YYYY-MM-DDTHH:MMZ |

When querying the 'lin' shapefile, the elements have the same definition as in the 'pts' file.

* __Data in GeoJSON format__

`{YYYYMMDD}T{HHmm}Z_MSC_Hurricane_{NAME}.json`

Where :

* __YYYYMMDD__ : Year, month and day of data transmission
* __T__: Time delimiter according to ISO8601 standards
* __HHmm__ : Hour and minute of data transmission
* __Z__: Time zone (UTC hour)
* __MSC__: Constant character string for Meteorological Service of Canada, the data source
* __Hurricane__ : Constant string indicating the name of the product contained in the files, i.e. hurricane trajectories
* __NAME__ : Constant string indicating the name of the hurricane
* __json__: Constant string indicating that the format is GeoJSON

Ex: `20240708T2100Z_MSC_Hurricane_BERYL.json`


## Support

If you have any questions about this data, please [contact us](https://weather.gc.ca/mainmenu/contact_us_e.html).

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).
