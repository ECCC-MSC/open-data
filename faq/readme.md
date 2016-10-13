[En français](readme_fr.md)

![ECCC logo](../img_eccc-logo.png)

[TOC](../readme.md) > FAQ

MSC Public Data FAQ
==========================================================

This section contains the most frequently asked questions about the MSC open data available on the Datamart.


Table of Content
----------------

* [What data can I find?](#what-data-can-i-find)
* [Do you provide an API through which we can access weather data for a given area and time?](#do-you-provide-an-api-through-which-we-can-access-weather-data-for-a-given-area-and-time)
* [How can I download data?](#how-can-i-download-data)
* [Why message queues when using AMQP are being terminated after several hours of inactivity?](#why-message-queues-when-using-amqp-are-being-terminated-after-several-hours-of-inactivity)
* [Could I be aware of any change in the bulletins or model format and or content?](#could-i-be-aware-of-any-change-in-the-bulletins-or-model-format-and-or-content)
* [Can I have radar data?](#can-i-have-radar-data)
* [Can I have archived radar data?](#can-i-have-archived-radar-data)
* [Are past forecasts from your model available?](#are-past-forecasts-from-your-model-available)
* [Could I have a GRIB data feed?](#could-i-have-a-grib-data-feed)
* [Why not making just one big GRIB file with all the variables?](#why-not-making-just-one-big-grib-file-with-all-the-variables)

## What data can I find?

A lot of our data is accessible through our open data server named the Meteorological Service of Canada (MSC) Datamart. You will find a short description of every product available, as well as a link to a more detailed documentation for each of them, in this README:
http://dd.meteo.gc.ca/about_dd_apropos.txt

The terms and conditions of use of Meteorological Data from Environment and Climate Change Canada can be found here:
http://dd.meteo.gc.ca/doc/LICENCE_GENERAL.txt

We also offer geospatial web services named MSC GeoMet. The documentation is available here:
http://www.ec.gc.ca/meteo-weather/default.asp?lang=En&n=C0D9B3D8-1c

Another source of product description can be found on the CMC Product Guide publicly available on our Collaboration web site:
http://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/table_of_contents_e.html

If you need more information about our services or products, do not hesitate to contact us, using the e-mail address: ec.dps-client.ec@canada.ca

## Do you provide an API through which we can access weather data for a given area and time? 

Environment and Climate Change Canada offers an API to access Canadian weather data via geospatial web services named MSC GeoMet, through the recognized WMS international standard. 
The documentation is available here: 
http://www.ec.gc.ca/meteo-weather/default.asp?lang=En&n=C0D9B3D8-1c

Data available in the WMS can easily be integrated into iOS applications and we're aware of several clients successfully doing so.

We are also in the process of making a lot more of our weather data available in the OGC family of standards (e.g. WMS, WCS, WFS, SLD). 
See the announcing GeoMet-Beta version: 
http://lists.ec.gc.ca/pipermail/geomet-info/2016-June/000033.html

Changes to the GeoMet-Beta Geospatial Web Services will be announced on the GeoMet-Info list: 
http://lists.ec.gc.ca/cgi-bin/mailman/listinfo/geomet-info

Finally, please note that because GeoMet is leveraging open standards, users are not affected when the underlying data is modified: methods to access the data remain stable and reliable. 
GeoMet serves well over 1 million requests daily and is free to use as long as the source is attributed, see licence below for details: 
http://dd.meteo.gc.ca/doc/LICENCE_GENERAL.txt 


## How can I download data?

The Meteorological Service of Canada has set up a data wire for announcing file availability on the Datamart.  This data wire uses the 'Advanced Message Queuing Protocol' (AMQP) protocol. Not only does this 
enable the user to be notified of available products as they're published, but also to receive them automatically.
The service may apply to a specific set of files (weather warnings, observations, model data, etc.) and thus may concern only those products of interest to the user.

The documentation about this service can be found here:
http://dd.weather.gc.ca/doc/README_AMQP.txt

Please, note that the current documentation mentions the script "dd_subscribe" which runs with both Python2 and Python3.
However, we should migrate shortly to "sr_subscribe" which runs only with Python3. Some documentation is available here:
http://metpx.sourceforge.net/sr_subscribe.1.html
http://metpx.sourceforge.net/Install.html

## Why message queues when using AMQP are being terminated after several hours of inactivity?

Users are expected to run a daemon that downloads data constantly, such as the one provided by Sarracenia (http://metpx.sf.net).  
The broker has a limited ability to queue products up when a user has an unintended outage,  this can be anywhere from a few hours to a few days. The performance of the entire service is adversely affected by the presence of large queues for any single consumer, 
so queues cannot be allowed to accumulate indefinitely.  
We keep queues alive as long as we can reasonably do so, but this practice is just meant to give clients time to restart their consumers in case of failure. The duration of disconnects that can be safely withstood depends on the number of products subscribed which in turn determines how many products get queued.   Generally when there is a queue of more than 25,000 products, and no consumer, the queue will get purged.   

In General, one should use continuous access, rather than periodic polling, as it will remove peaks in download bandwidth and server load, and reduce the risk of queues being purged on the server. 
Judicious use of the 'subtopic' directive in configurations will minimize the size of queues, so they can last through longer outages.


## Could I be aware of any change in the bulletins or model format and or content? 

For Canadian stations bulletins, any change in the heading and station name is announced by what we call a GENOT (GEneral NOTification) message. 
We have a mailing list to distribute the GENOT for the station and the header change. If you are interested in this e-mail notificaiton, please send us your e-mail and we will add it to this mailing list. 

To be advised of major changed, like model resolution, you can subscribe to the GENOT 03 mailing list.
You can find an example of a GENOT 03 bulletin here: http://dd.meteo.gc.ca/doc/genots/2014/02/18/NOCN03_CWAO_182045___01117 

Finally, we strongly recommand to subscribe to the datamart's mailing list in order to be warned of any updates or changes regarding the data available. 
You can subscribe here:
http://lists.cmc.ec.gc.ca/mailman/listinfo/dd_info

Please use the following address to contact us for any comments or questions:
ec.dps-client.ec@canada.ca

## Can I have radar data?

The weather radar data we freely provide to the public are the GIFs on the MSC Open data server. You will find the documentation about this service here:
http://dd.meteo.gc.ca/radar/doc/README_radar.txt 

We also provide the North-American weather radar mosaic as WMS geospatial web services:
http://www.ec.gc.ca/meteo-weather/default.asp?lang=En&n=C0D9B3D8-1 

The license terms for these products can be read here:
http://dd.meteo.gc.ca/doc/LICENCE_GENERAL.txt 

In both case, it does not include raw radar data. Other radar data products are provided as a cost-recovered service. 
As part of this service, we push data to your FTP server and provide 24/7 support. The terms under which these products are provided are similar to those described in the license above.

Documentation about radar formats can be found at the following location:
http://collaboration.cmc.ec.gc.ca/cmc/CMOI/produits/samples/radar/vscan/Formats_in_URP.pdf 

For data feeds, available formats goes like this:

    - NUMERICA (ASCII)
    - GIF format (recent GIFs available for free on the MSC Datamart)
    - IRIS (raw) format
        Specifications: http://www.vaisala.com/en/hydrology/offering/weatherradars/Pages/IRIS.aspx 

Regarding pricing, here are the details:

    - 1-5 radars (QC, Atl or Pac region) : $1,600/month
    - 6-10 (any whole region): $1,800/month
    - 11+: $2,000/month
    - Plus a one-time setup fee of $2,000 

For information about file sizes:

    - 1 hour of volume scan for 1 radar without precipitation: ~ 4.5 Mb
    - 1 hour of volume scan for 1 radar with precipitation: ~ 13 Mb 

## Can I have archived radar data?

Environment and Climate Change Canada does not have on online service to retrieve archived data.
The data retrieval service from our archive is under a cost recovery policy. We charge 99$/hour it takes, with a minimum of 99$, to retrieve/recreate the requested data. The data by itself is free.

It is available in both raw format (IRIS) or products in ASCII format. You will find more information about our products and formats at the address: (<em>to come</em>)

Typical archived data retrieval requests required between 2-4 hours to process. 
If interested, please provide us the completed form:


| Information | Value |
|-------------|:-----:|
|Radar name(s) |       |       
|Product type (Raw, CAPPI, PRECIP, ECHOTOP, etc.) |       |
|Unit (dBZ, mm/hr) |       |
|Format (GIF, NumericA, IRIS/MRO) |       |
|Period (UTC) |       |
|Frequency (default: 10 minutes) |       |
|Delivery format (zip, tar, other) |       |
|Expected delivery date (when?) |       |
|Other information |       |
|Billing name and coordinates |       |

## Are past forecasts from your model available? 

Environment and Climate Change Canada does not have on online service to retrieve archived data.

The data retrieval service from our archive is under a cost recovery policy. We charge 99$/hour it takes, with a minimum of 99$, to retrieve/recreate the requested data. The data by itself is free.

If users give us specifications for the data we can extract it to GRIB format and send it to them. Depending on the nature of the request this is usually in the low hundreds. We can provide users with an estimate once we know more about their requirements.
If interested, please provide us the completed form:


| Information | Value |
|-------------|:-----:|
|Model (e.g. GDPS, RDPS, HRDPS, NAEFS) |       |       
|Data type (forecast, analysis or map)  |       |
|Weather variables (e.g. WIND_TGL_40m) |       |
|Dates (e.g. 2006-01-01 to 2008-12-31 )  |       |
|Run hours (e.g. 00Z, 12Z) |     |
|Forecast hours (e.g. 000, 003, 006) |       |
|Data domain (user defined lat-lon box, existing Datamart domain)  |       |
|Horizontal spatial resolution (e.g. 10km/0.24 degrees)  |       |
|Levels (surface, isobaric levels, meters above ground) |        |
|Delivery mode 	FTP |       |
|Contact name and billing coordinates |         |

Notes: 
- Request such as "all variables at all levels" is not accepted. Be specific
- Data are archived 5 years back, depending of their availability 

## Could I have a GRIB data feed?

Environment and Climate Change Canada offers a push feed for its NWP data in GRIB format. This service is 24/7 supported and the cost is function of the amount of data: it starts at $500/month + $500 set-up fee from 0 to 1 Gb/day. Add 500$/month for each daily Gb.

Contact us if you are insterested by this service. 

## Why not making just one big GRIB file with all the variables?

Environment and Climate Change Canada opted to put one variable per file because we estimated that most of our users would not used all the variables. 
Moreover, would have we made packages with many variables, users would have made requests to have their choice of variables in the packages.

This is why we still believe that is the right strategy to disseminate GRIB data.

That being said, to streamline their download process users could write all the download file paths in one text file and use it as an argument to the command "wget -i list.txt". 
By proceeding like this, one socket will be open for all your requests and the web server will send you the files as fast at it is configured, without being queued for each file. 
Users will then reach the same download speed as if all the GRIB files were in a single zip file.



