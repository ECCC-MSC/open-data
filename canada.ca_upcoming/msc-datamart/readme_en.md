[En français](readme_fr.md)

![ECCC logo](../img_eccc-logo.png)

[TOC](../readme_en.md) > MSC Datamart


# MSC Datamart

The Meteorological Service of Canada (MSC) HTTP data server is a source of raw meteorological, environmental, hydrometric and climate data. This service is aimed at specialized users with good meteorological and IT knowledge, and is mainly meant to be accessed in an automatic manner via the Internet.


## Access

The MSC Datamart is located at https://dd.meteo.gc.ca/ .

### Real-time push notifications and data retrieval
  
To facilitate the retrieval of timely data on the Datamart, the Meteorological Service of Canada (MSC) has set up a data wire for announcing file availability on the Datamart.  This data wire uses the 'Advanced Message Queuing Protocol' (AMQP) protocol. Not only does this enable the user to be notified of available products as they're published, but also to receive them automatically.

The service can filter specific sets of files (weather warnings, observations, model data, etc.), enabling notifications only for products of interest to the user.

This is the recommended method to retrieve data from the MSC Datamart.

The documentation about this service is found on the [MSC Datamart AMQP documentation](https://dd.meteo.gc.ca/doc/README_AMQP.txt).
  
### Additional access methods


* wget ... reference: https://weather.gc.ca/grib/usage_tips_e.html

In case of issues with the , an [alternative server is available](https://lists.ec.gc.ca/pipermail/dd_info/2019-April/000329.html).

### MSC Datamart-Alpha

http://dd.alpha.weather.gc.ca/



## Data formats

Data on the MSC Datamart is available in open formats. It includes:

* [GRIB2](https://weather.gc.ca/grib/index_e.html)
* netCDF
* csv
* XML

do we need to mention the following here?
* SWOB-XML
* CAP-XML
* GIF (the radar GIFs)

## Announcement mailing list

We encourage users to subscribe to the [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info) MSC Datamart announcement mailing list to be informed of enhancements and changes to the MSC Datamart service.


## Support

The MSC Datamart service is operational 24/7. User support is provided on a best effort basis during normal business hours. Users requesting support are invited to [contact us](http://www.weather.gc.ca/mainmenu/contact_us_e.html).