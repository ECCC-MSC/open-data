[En Français](readme_hurricane-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC Open Public Data](../readme_en.md) > Hurricane trajectories

# Data of the hurricane trajectories

This page describes the data of the [hurricane trajectories](readme_hurricane_en.md).

The Canadian Hurricane Centre provides files in shapefile format as part of the regular hurricane season forecast.

The files will allow users to plot the route of the storms forecast in a map system of their choice. There is four shapefiles (*.shp) formats that are produced and include each a 6-hour forecast bulletin when storms of tropical origin threatens or risks to threaten Canadian territory.

Hurricane tracks issued by the Canadian Hurricane Centre hurricanes are published on the MSC Datamart. These data are rendered available in experimental mode in order to offer users an opportunity to ingest and test the data in real time. The service will be provided to the best of our ability but please note that there is a significant possibility of occasional unannounced interruptions and non-received from this experimental data service, up to new announcement.

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage-overview/readme_en.md) is also available.

The data is available via the HTTP protocol. It is possible to access it with a standard browser. In this case, we obtain a list of links giving access to a  shapefile.

You can find the shapefiles at :

https://dd.weather.gc.ca/trajectoires/hurricane/shapefile/storm-name/

where :
* storm-name is the storm name in uppercase (e.g. 'BERTHA' )

## Directory and file name nomenclature 

NOTE : ALL HOURS ARE IN UTC.

File naming convention is :

YYYYMMDD_HHMMZ_STORM-NAME.TYPE.shp

where :
* __YYYYMMDD__ : Forecast issuance date
* __HHMM__ : Time in UTC 
* __Z__ : Constant string, indicating Zulu time (UTC code name)
* __STORM-NAME__ : Storm name (e.g. BERTHA - hurricane, post-tropical, etc)
* __TYPE__ : Type of shapefile:
    * "pts" - The forecast locations (points) 
    * "lin" - The line segments connecting forecast track points
    * "rad" - Contains forecast wind radii information (wind quadrants)
    * "err" - Contains information on track forecast error ("error cone")
	
## File content

When querying the points (pts) shapefile, the contents of each column are given
as follows :

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

## Support

If you have any questions about these data, please contact us at : ec.dps-client.ec@canada.ca

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).

