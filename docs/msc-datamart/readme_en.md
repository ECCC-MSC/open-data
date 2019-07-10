[En français](readme_fr.md)

![ECCC logo](../img_eccc-logo.png)

[TOC](../readme_en.md) > MSC Datamart

# MSC Datamart

The Meteorological Service of Canada (MSC) HTTP data server is a source of raw weather, water, climate and environmental data. This service is aimed at specialized users with good meteorological and IT knowledge, and is mainly meant to be accessed in an automatic manner via the Internet.

## Access

The MSC Datamart is located at [https://dd.weather.gc.ca/](https://dd.weather.gc.ca/).

### Real-time push notifications and data retrieval
  
To facilitate the retrieval of timely data on the MSC Datamart, the Meteorological Service of Canada (MSC) has set up a data wire for announcing file availability on the MSC Datamart. This data wire uses the 'Advanced Message Queuing Protocol' (AMQP) protocol. Not only does this enable the user to be notified of available products as they're published, but also to receive them automatically.

The service can filter specific sets of files (weather warnings, observations, model data, etc.), enabling notifications only for products of interest to the user.
This is the recommended method to retrieve data from the MSC Datamart.
The documentation for this service is found on the [MSC Datamart AMQP documentation](amqp_en.md).
  
### Additional access methods

An alternative server to the MSC Datamart is available, please refer to [the announcement for details](https://lists.ec.gc.ca/pipermail/dd_info/2019-April/000329.html).
Users requiring one-time data retrieval may use [wget to download data from the MSC Datamart](readme_wget-datamart_en.md).

## Data formats

Data on the MSC Datamart is available in open formats. It includes:

* [GRIB2](../msc-data/readme_grib_en.md)
* [NetCDF](https://www.unidata.ucar.edu/software/netcdf/)
* [GeoJSON](https://geojson.org/)
* [shapefile](https://www.esri.com/library/whitepapers/pdfs/shapefile.pdf)
* CSV
* XML

## Usage

Information on using these services and examples are available on the [usage overview page](../usage/readme_en.md).

## Change management 

The MSC needs to be flexible in the manner in which it offers specialized data to interested users. Therefore, we need to be able to update or change formats or data offerings in a timely manner, as the technology, standards and innovation do change continuously. However, we will do our best to notify our users in advance of upcoming changes. 

Also, as often as possible, we will use the MSC testing data repository, DD-Alpha, to deposit samples of the new modified data to help our users adapt their applications. The server DD-Alpha is located at [http://dd.alpha.weather.gc.ca/](http://dd.alpha.weather.gc.ca/) . This server, which is not operational, provides also access to experimental or other non-operational data.

## Announcement mailing list

We encourage users to subscribe to the [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info) announcement mailing list to be informed of enhancements and changes to the MSC Datamart service.

## Support

The MSC Datamart service is operational 24/7. User support is provided on a best effort basis during normal business hours. Users requesting support are invited to [contact us](https://www.weather.gc.ca/mainmenu/contact_us_e.html).
