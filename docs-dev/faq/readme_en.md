[En français](readme_fr.md)

![ECCC logo](../img_eccc-logo.png)

[TOC](../readme_en.md) > FAQ

# MSC Public Data FAQ

This section contains the most frequently asked questions about the MSC open data.

Alex's note: ideally content in the FAQ should be included in the actual documentation whenever possible and removed from this FAQ section


## Table of Content

* [What data can I find on the MSC Datamart?](#what-data-can-i-find-on-the-msc-datamart)
* [Do you provide an API through which we can access weather data for a given area and time?](#do-you-provide-an-api-through-which-we-can-access-weather-data-for-a-given-area-and-time)
* [How can I download data?](#how-can-i-download-data)
* [Why are message queues terminated after several hours of inactivity when using AMQP?](#why-are-message-queues-terminated-after-several-hours-of-inactivity-when-using-amqp)
* [How to use AMQP under Windows?](#how-to-use-amqp-under-windows)
* [Can I have radar data?](#can-i-have-radar-data)
* [Can I have archived radar data?](#can-i-have-archived-radar-data)
* [Are past forecasts from your model available?](#are-past-forecasts-from-your-model-available)
* [Could I be made aware of any change to bulletins or model format and or content?](#could-i-be-made-aware-of-any-change-to-bulletins-or-model-format-and-or-content)
* [How to be informed about problems with model data production?](#how-to-be-informed-about-problems-with-model-data-production)
* [Could I have a GRIB data feed?](#could-i-have-a-grib-data-feed)
* [Why not make just one big GRIB file with all the variables?](#why-not-make-just-one-big-grib-file-with-all-the-variables)
* [The data available for an X system is only in NetCDF format, how to manipulate files in this format?](#the-data-available-for-an-x-system-is-only-in-netcdf-format-how-to-manipulate-files-in-this-format)
* [What is the datum of model X?](#what-is-the-datum-of-model-x)
* [Can I have the topography of model X?](#can-i-have-the-topography-of-model-x)
* [Can I have the land sea mask of model X?](#can-i-have-the-land-sea-mask-of-model-x)
* [Is it possible to download the data in another format than the one available on the MSC Datamart?](#is-it-possible-to-download-the-data-in-another-format-than-the-one-available-on-the-msc-datamart)
* [Is it possible to access variables other than those available on the MSC Datamart for system X or is the list exhaustive?](#is-it-possible-to-access-variables-other-than-those-available-on-the-msc-datamart-for-system-x-or-is-the-list-exhaustive)
* [Can I have the current weather observation?](#can-i-have-the-current-weather-observation)
* [How often are the observational data collected by province and territory refreshed?](#how-often-are-the-observational-data-collected-by-province-and-territory-refreshed)
* [Can I have buoys data?](#can-i-have-buoys-data)
* [Can I have access to weather warnings?](#can-i-have-access-to-weather-warnings)
* [Which are the main differences between RSS ATOM feeds and AMQP protocol to consume alerts?](#Which-are-the-main-differences-between-rss-atom-feeds-and-amqp-protocol-to-consume-alerts)
* [Can I have a shapefile of the warning regions?](#can-i-have-a-shapefile-of-the-warning-regions)
* [Can I have satellite images?](#can-i-have-satellite-images)
* [Can I have access and use of icons displayed in the Citypage XML product?](#can-i-have-access-and-use-of-icons-displayed-in-the-citypage-xml-product)
* [Can I have CSV minimum and maximum forecast temperature?](#can-i-have-csv-minimum-and-maximum-forecast-temperature)
* [Can I have rainfall depth data?](#can-i-have-rainfall-amount-data)
* [Can I have snow water equivalent data?](#can-i-have-snow-water-equivalent-data)
* [I do not see a condition under the corresponding element of the Citypage XML file, is this normal?](#i-do-not-see-a-condition-under-the-corresponding-element-of-the-citypage-xml-file-is-this-normal)
* [In the NWP systems changelog, I see several systems (e.g. SRPEOT) not mentioned in the list of systems with available data, where can I find this data?](#in-the-nwp-systems-changelog-i-see-several-systems-e-g-SRPEOT-not-mentioned-in-the-list-of-systems-with-available-data-where-can-i-find-this-data)
* [I'd like to use your data for profit, am I allowed to do that?](#i-d-like-to-use-your-data-for-profit-am-I-allowed-to-do-that)
* [What are the minimum requirements (processor, RAM) of my PC to be able to download data and/or use the GeoMet services?](#what-are-the-minimum-requirements-processor-ram-of-my-PC-to-be-able-to-download-data-and-or-use-the-geomet-services)
* [In GeoMet, what styles are available for a WMS layer? Can I display a WMS layer in GeoMet with another style than the ones proposed?](#in-geomet-what-styles-are-available-for-a-wms-layer-can-i-display-a-wms-layer-in-geomet-with-another-style-than-the-ones-proposed)
* [I see that you are using the QGIS (Geographic Information System) to visualize and manipulate the GeoMet layers and geospatial data in the Datamart, can I use other software to manipulate this data?](#i-see-that-you-are-using-the-qgis-geographic-information-system-to-visualize-and-manipulate-the-geomet-layers-and-geospatial-data-in-the-datamart-can-i-use-other-software-to-manipulate-this-data)
* [Contact us](#contact-us)

## What data can I find on the MSC Datamart?

A lot of our data is accessible through our open data server named the Meteorological Service of Canada (MSC) Datamart. You will find a short description of all available products, as well as a link to a more detailed documentation for each of them, in this README:

[https://dd.meteo.gc.ca/about_dd_apropos.txt](https://dd.meteo.gc.ca/about_dd_apropos.txt)

The terms and conditions of use of Meteorological Data from Environment and Climate Change Canada can be found here:

[https://dd.meteo.gc.ca/doc/LICENCE_GENERAL.txt](https://dd.meteo.gc.ca/doc/LICENCE_GENERAL.txt)

We also offer geospatial web services named MSC GeoMet. The documentation is available here:

[https://www.ec.gc.ca/meteo-weather/default.asp?lang=En&n=C0D9B3D8-1c](https://www.ec.gc.ca/meteo-weather/default.asp?lang=En&n=C0D9B3D8-1c)

Another source of product description can be found on the CMC Product Guide publicly available on our Collaboration web site:

[https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/table_of_contents_e.html](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/table_of_contents_e.html)

If you need more information about our services or products, do not hesitate to contact us, using the e-mail address: ec.dps-client.ec@canada.ca

## Do you provide an API through which we can access weather data for a given area and time?

Environment and Climate Change Canada offers an API to access Canadian weather data via geospatial web services named MSC GeoMet, through the recognized WMS international standard.
The documentation is available here:

[https://www.canada.ca/en/environment-climate-change/services/weather-general-tools-resources/weather-tools-specialized-data/geospatial-web-services.html
](https://www.canada.ca/en/environment-climate-change/services/weather-general-tools-resources/weather-tools-specialized-data/geospatial-web-services.html)

Data available through WMS can easily be integrated into iOS applications and we're aware of several clients successfully doing so.

For your information, more than 400 layers are available in the WMS GetCapabilities:

[https://geo.weather.gc.ca/geomet/?lang=E&service=WMS&request=GetCapabilities](https://geo.weather.gc.ca/geomet/?lang=E&service=WMS&request=GetCapabilities)

We are also in the process of making a lot more of our weather data available in the OGC family of standards (e.g. WMS, WCS, WFS, SLD).
See the announcement of the GeoMet-Beta version:

[https://lists.ec.gc.ca/pipermail/geomet-info/2016-June/000033.html](https://lists.ec.gc.ca/pipermail/geomet-info/2016-June/000033.html)

Changes to the GeoMet-Beta Geospatial Web Services will be announced on the GeoMet-Info list:

[https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/geomet-info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/geomet-info)

Finally, please note that because GeoMet is leveraging open standards, users are not affected when the underlying data is modified: methods to access the data remain stable and reliable.
GeoMet serves well over 1 million requests daily and is free to use as long as the source is attributed. See the licence below for details:

[https://dd.meteo.gc.ca/doc/LICENCE_GENERAL.txt](https://dd.meteo.gc.ca/doc/LICENCE_GENERAL.txt)

## How can I download data?

The Meteorological Service of Canada has set up a data wire for announcing file availability on the MSC Datamart.  This data wire uses the 'Advanced Message Queuing Protocol' (AMQP), an open
protocol with free libraries in numerous programming languages. This enables the user not only to be notified of available products as they're published, but also to receive them automatically if
he so chooses.
The service may be configured by the user to apply to a specific set of files (weather warnings, observations, model data, etc.) and thus may concern only those products of interest to the user.

The documentation about this service can be found here:

[https://dd.weather.gc.ca/doc/README_AMQP.txt](https://dd.weather.gc.ca/doc/README_AMQP.txt)

Please, note that while the original documentation mentions the script "dd_subscribe" which runs with both Python2 and Python3, we will be migrating
to "sr_subscribe" which runs only with Python3. Some documentation is available here:

[http://metpx.sourceforge.net/sr_subscribe.1.html](http://metpx.sourceforge.net/sr_subscribe.1.html)

[http://metpx.sourceforge.net/Install.html](http://metpx.sourceforge.net/Install.html)

## Why are message queues terminated after several hours of inactivity when using AMQP?

Users are expected to run a daemon that downloads data constantly, such as the one provided by Sarracenia ([http://metpx.sf.net](http://metpx.sf.net). In AMQP parlance, a pump, namely a host running Sarracenia, is a broker (see Glossary section at the address: [http://metpx.sourceforge.net/Install.html](http://metpx.sourceforge.net/Install.html)). The broker has a limited ability to queue products when a user has an unintended lengthy outage, say anywhere from a few hours to a few days. The performance of the entire service is adversely affected by the presence of large queues for any single consumer,
so queues cannot be allowed to accumulate indefinitely. We keep queues alive as long as we can reasonably do so, but this practice is only meant to give clients time to restart their session in case of failure. The duration of disconnects that can be safely withstood depends on the number of products subscribed which in turn determines how many products get queued. Generally when there is a queue of more than 25,000 products, and no consumer, the queue will be purged.   

In General, one should use continuous access, rather than periodic polling, as it will remove peaks in download bandwidth and server load, and reduce the risk of queues being purged on the server. Judicious use of the 'subtopic' directive in configurations will minimize the size of queues, so they can last through longer outages.

## How to use AMQP under Windows?

If you are using the Windows environment, you need to download the latest version of Sarracenia at this address :

[https://hpfx.collab.science.gc.ca/~pas037/Sarracenia_Releases/](https://hpfx.collab.science.gc.ca/~pas037/Sarracenia_Releases/)

This is an EXE file that can be used without having to install a Python environment.

See details here: [https://github.com/MetPX/sarracenia/blob/master/doc/Install.rst]( https://github.com/MetPX/sarracenia/blob/master/doc/Install.rst)

## Can I have radar data?

The weather radar data we freely provide to the public are the GIF images on the MSC Open data server. You will find the documentation about this service here:

[https://dd.meteo.gc.ca/radar/doc/README_radar.txt](https://dd.meteo.gc.ca/radar/doc/README_radar.txt)

We also provide the North-American weather radar mosaic as WMS geospatial web services:

[https://www.canada.ca/en/environment-climate-change/services/weather-general-tools-resources/weather-tools-specialized-data/geospatial-web-services.html
](https://www.canada.ca/en/environment-climate-change/services/weather-general-tools-resources/weather-tools-specialized-data/geospatial-web-services.html)

The license terms for these products can be read here:

[https://dd.meteo.gc.ca/doc/LICENCE_GENERAL.txt](https://dd.meteo.gc.ca/doc/LICENCE_GENERAL.txt)

Neither of the above cases includes raw radar data. This and other radar data products are provided as a cost-recovered service.
As part of this service, we push data to your FTP server and provide 24/7 support. The terms under which these products are provided are similar to those described in the license above.

Documentation about radar formats can be found at the following location:

[https://collaboration.cmc.ec.gc.ca/cmc/CMOI/produits/samples/radar/vscan/Formats_used_in_URP_En_last_version.pdf](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/produits/samples/radar/vscan/Formats_used_in_URP_En_last_version.pdf)

Documentation about radar products can be found at the following location:

[https://collaboration.cmc.ec.gc.ca/cmc/CMOI/produits/samples/radar/vscan/Radar_Products_Available_CMC_Mai_2015_external.pdf](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/produits/samples/radar/vscan/Radar_Products_Available_CMC_Mai_2015_external.pdf)

For data feeds, available formats are as follows:

* NUMERICA (ASCII)
* GIF format (recent GIFs available for free on the MSC Datamart)
* IRIS (raw) format for the old C-Band radars and ODIM_H5 format for the new S-band radars
* Specifications: 
    * [https://my.vaisala.net/en/hydrology/offering/weatherradars/Pages/IRIS.aspx](https://my.vaisala.net/en/hydrology/offering/weatherradars/Pages/IRIS.aspx)
    * [https://support.hdfgroup.org/HDF5/users5.html](https://support.hdfgroup.org/HDF5/users5.html)

Details regards pricing are as follows:

* 1-5 radars (QC, Atl or Pac region) : $1,600/month
* 6-10 (any whole region): $1,800/month
* 11+: $2,000/month
* Plus a one-time setup fee of $2,000

Please, note that these rates are indicative only and may change.

Regarding file sizes:

* 1 hour of volume scan for 1 radar without precipitation: ~ 4.5 Mb
* 1 hour of volume scan for 1 radar with precipitation: ~ 13 Mb

Please, note that the estimate above depends on meteorological conditions and is for reference purposes only.

## Can I have archived radar data?

Environment and Climate Change Canada does not have on online service to retrieve archived data.
The data retrieval service from our archive is under a cost recovery policy. We charge 99$/hour, with a minimum charge of 99$, to retrieve/recreate the requested data. The data itself is free.

It is available in either raw format (IRIS) or products in ASCII format. You will find more information about our formats and products at the addresses:

[https://collaboration.cmc.ec.gc.ca/cmc/CMOI/produits/samples/radar/vscan/Formats_used_in_URP_En_last_version.pdf](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/produits/samples/radar/vscan/Formats_used_in_URP_En_last_version.pdf)

[https://collaboration.cmc.ec.gc.ca/cmc/CMOI/produits/samples/radar/vscan/Radar_Products_Available_CMC_Mai_2015_external.pdf](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/produits/samples/radar/vscan/Radar_Products_Available_CMC_Mai_2015_external.pdf)

Typical archived data retrieval requests require between 2-4 hours to process.
If interested, please complete the order form below and send it via e-mail using the address: ec.dps-client.ec@canada.ca


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

The data retrieval service from our archive is under a cost recovery policy. We charge 99$/hour, with a minimum of 99$, to retrieve/recreate the requested data. The data itself is free.

Once users provide specifications for the required data, we can extract it to GRIB format and send it to them. An estimate can be provided once requierements are known.
Depending on the nature of the request this is usually in the low hundreds.
If interested, please complete the order form below and send it via e-mail using the address: ec.dps-client.ec@canada.ca


| Information | Value |
|-------------|:-----:|
|Model (e.g. GDPS, RDPS, HRDPS, NAEFS) |       |       
|Data type (forecast, analysis or map)  |       |
|Weather variables (e.g. WIND_TGL_40m) |       |
|Dates (e.g. 2006-01-01 to 2008-12-31 )  |       |
|Run hours (e.g. 00Z, 12Z) |     |
|Forecast hours (e.g. 000, 003, 006) |       |
|Data domain (user defined lat-lon box, existing MSC Datamart domain)  |       |
|Horizontal spatial resolution (e.g. 10km/0.24 degrees)  |       |
|Levels (surface, isobaric levels, meters above ground) |        |
|Delivery mode 	FTP |       |
|Contact name and billing coordinates |         |

Notes:
- Requests such as "all variables at all levels" cannot be accepted. Please, be specific.
- Forecast data are archived for 5 years. Other types of data (analyses for example) may have longer retention periods.

## Could I be made aware of any change to bulletins or model format and or content?

For Canadian station bulletins, any change in the heading and station name is announced via what we call a GENOT (GEneral NOTification) message.
We have a mailing list to distribute GENOTs for station and header changes. If you are interested in this e-mail notification, please send us your e-mail and we will add it to this mailing list.

To be advised of major changes, such as model resolution, you can subscribe to the GENOT 03 mailing list.
You can find an example of a GENOT 03 bulletin here:

[https://dd.meteo.gc.ca/doc/genots/2014/02/18/NOCN03_CWAO_182045___01117](https://dd.meteo.gc.ca/doc/genots/2014/02/18/NOCN03_CWAO_182045___01117)

Finally, we strongly recommend to subscribe to the MSC Datamart's mailing list in order to be warned of any updates or changes regarding the data available.

You can subscribe here:
[https://lists.ec.gc.ca/mailman/listinfo/dd_info](https://lists.ec.gc.ca/mailman/listinfo/dd_info)

Please use the following address to contact us for any comments or questions:
ec.dps-client.ec@canada.ca

## How to be informed about problems with model data production?

Sometimes model data is late or even missing from our HTTPS data server.

To find out if this delay or absence is due to a production problem, you can consult the AACN01 CWAO bulletins.  These are bulletins issued by the CCPAC as required to inform MSC offices and
other customers of any problems that may disrupt or delay the issuance and/or distribution of operational products.

To consult the latest AACN01 CWAO bulletins, you can use the script search utility provided by ECCC:

[https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/bulletins/CMC_Bulletin_Search_Help_en.pdf](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/bulletins/CMC_Bulletin_Search_Help_en.pdf)

For example, to obtain the AACN01 bulletins of the day, you can click on the following URL :

[http://dd.meteo.ec.gc.ca/cgi-bin/bulletin_search.pl?product=AA&location=CN01]( http://dd.meteo.ec.gc.ca/cgi-bin/bulletin_search.pl?product=AA&location=CN01)

For a specific day, you can refine your search. For example, to have the information for May 19, 2020, you can use this link :

[https://dd.meteo.gc.ca/cgi-bin/bulletin_search.pl?product=AA&location=CN01&day=19&month=05&year=2020]( https://dd.meteo.gc.ca/cgi-bin/bulletin_search.pl?product=AA&location=CN01&day=19&month=05&year=2020)

There is also a mailing list for AACN01 bulletins. If you are interested, please contact us at ec.dps-client.ec@canada.ca and we will add you to the mailing list.

## Could I have a GRIB data feed?

Environment and Climate Change Canada offers a push feed for its NWP data in GRIB format. This service is supported 24/7 and the cost is a function of the amount of data requested: at the starting price is $500/month + $500 set-up fee for up to 1 Gb/day. Add 500$/month for each additional Gb per day.

Please, contact us if you are interested in this service.

## Why not make just one big GRIB file with all the variables?

Environment and Climate Change Canada opted to put one variable per file because we presumed that most users would not require all the variables.
Moreover, would have we made packages with many variables, users would have made requests to have their choice of variables in the packages.

This is why we still believe that is the right strategy to disseminate GRIB data.

That being said, the web utility [wget](https://www.gnu.org/software/wget/wget) possesses features that aim to optimize the download process. For instance, users could write all the download file paths in one text file and use it as an argument to the command "wget -i list.txt".
By proceeding like this, a single socket will be open and the request for all the listed files is treated as a single download, without opening and closing sockets for each file.

This will then reach the same download speed as if all the GRIB files were in a single zip file.

## The data available for an X system is only in NetCDF format, how to manipulate files in this format?

There is a section on [data format](../msc-datamart/readme_en#data-formats) where information about the NetCDF data format can be found. In addition, the __GDAL__ function allows you to manipulate this data format more easily by giving precise information about the data matrix.

## What is the datum of model X?

You can use the free [GDAL](https://www.gdal.org/) tool to retrieve datum and projection information for our GRIB2 files.
The following command will provide the datum and projection of the file:

gdalinfo file.grib2

In the output, information starts with "Coordinate System is:".

## Can I have the topography of model X?

The model topography is the field HGT_SFC (Model topography - Smoothed) of the prognostic hour 00.

## Can I have the land sea mask of model X?

You can use the variable LAND_SFC_0 (Land cover) of prognostic hour 00 to determine this mask.
Where the value is 0, it is sea, where the value is not 0, it is land (or portion of it).

## Is it possible to download the data in another format than the one available on the MSC Datamart?

Unfortunately, it is not possible to download data from the MSC Datamart in any other format than the one available. However, the section on [data format](../msc-datamart/readme_en#data-formats) can help you manipulate the data more easily. Also, with the [Web Coverage Service (WCS)](../msc-geomet/ web-services_en.md #web-coverage-service-wcs) section of GeoMet, it is possible to convert the raster formats GeoTIFF and NetCDF. Soon, it will also be possible to convert GRIB2 data with GeoMet. Note that, for example, it is not possible to convert a GRIB2 format to a CSV format. GRIB2 is a raster data format (with pixels) while CSV is for vector data (point line polygon).

## Is it possible to access variables other than those available on the MSC Datamart for system X or is the list exhaustive?

The list is not exhaustive. We are always very open to receive feedback from users and to know their needs. It is possible to communicate with us via the email address: ec.dps-client.ec@canada.ca.

## Can I have the current weather observation?

We have two XML products that contain the observations of the Environment and Climate Change Canada station network.

One is on a station basis, one file per station. All Canadian stations are included in this product. The documentation can be found here:

[https://dd.meteo.gc.ca/observations/doc/README_SWOB.txt](https://dd.meteo.gc.ca/observations/doc/README_SWOB.txt)

The other product is on a provincial/territorial basis. One file contains stations of only one province or territory. Not all the stations are included in this product. The documentation is here:

[https://dd.meteo.gc.ca/observations/doc/README_observations.txt](https://dd.meteo.gc.ca/observations/doc/README_observations.txt)

## How often are the observational data collected by province and territory refreshed?

The provincial summary files are updated 6 times per hour, but the simple fact that we update them does not necessarily mean that any of the stations in the summary file have updated their data since the last run.
   
We update the observations on an hourly (not minute-by-minute) basis for each station at the beginning of the hour, but another update (called a "special obs" or "speci") within the hour is also possible if the observer feels that there has been a change large enough to warrant an update.

It is possible, for example, that the 1614Z file may not contain observations different from those in 1611Z, so the user should not always expect changes in values for an individual station within the hour.

We present only the data we obtain and, in this case, most stations report only once per hour.

## Can I have buoys data?

The buoys observations are available on the Canadian Coast Guard web site here:

[http://www.meds-sdmm.dfo-mpo.gc.ca/isdm-gdsi/waves-vagues/msc-smc/index-eng.html](http://www.meds-sdmm.dfo-mpo.gc.ca/isdm-gdsi/waves-vagues/msc-smc/index-eng.html)

Informations regarding drifting buoys are available here:

[http://www.meds-sdmm.dfo-mpo.gc.ca/isdm-gdsi/drib-bder/index-eng.html](http://www.meds-sdmm.dfo-mpo.gc.ca/isdm-gdsi/drib-bder/index-eng.html)

You can also retrieve the buoys alphanumeric bulletin on the MSC Datamart. The buoys header are SM/SN/SIVD17. They are available in the "bulletins" directory:

[https://dd.meteo.gc.ca/bulletins/doc/README_bulletins.txt](https://dd.meteo.gc.ca/bulletins/doc/README_bulletins.txt)

Since there is a lot of bulletins there, you may want to use the bulletin search tool:

[https://dd.weather.gc.ca/bulletins/doc/CMC_Bulletin_Search_Help_en.pdf](https://dd.weather.gc.ca/bulletins/doc/CMC_Bulletin_Search_Help_en.pdf)

## Can I have access to weather warnings?

You can find information about Environment and Climate Change Canada's warning in several places.

Firstly, you can find documentation about our warnings here:

[https://ec.gc.ca/meteo-weather/default.asp?lang=En&n=D9553AB5-1](https://ec.gc.ca/meteo-weather/default.asp?lang=En&n=D9553AB5-1)

You can access warnings through the RSS feed. See this page for more information:

[https://weather.gc.ca/business/index_e.html#rss](https://weather.gc.ca/business/index_e.html#rss)

You can also find warnings in CAP-XML format on our open data server. Documentation of this service can be found here:

[https://dd.meteo.gc.ca/alerts/doc/README_CAP.txt](https://dd.meteo.gc.ca/alerts/doc/README_CAP.txt)

ECCC also has an experimental service to send warnings or regions by email. See documentation on this service here:

[https://ecalertme.weather.gc.ca/](https://ecalertme.weather.gc.ca/)

Pelmorex Media Inc. also has a service for sending ECCC Warnings. You can find the information here:

[https://alerts.pelmorex.com/](https://alerts.pelmorex.com/)

## Which are the main differences between RSS ATOM feeds and AMQP protocol to consume alerts?

The main difference between RSS feeds (ATOM) and AMQP is that in the case of the RSS feed, user needs to send a request to know if new files
are available, whereas with AMQP, user is advised without sending any request.

If one wants to make an analogy, RSS feeds may be considering as a mailman who deposes letters in the mailbox, whereas AMQP may be considering as a deliver
who rings at the door to give the postal package.

We recommend to use the AMQP protocol if it is important for users to receive the announcement and data once available, also AMQP is a longer-term solution.

## Can I have a shapefile of the warning regions?

You can find the shapefiles of the public forecast regions here (pick the latest version):

[https://dd.meteo.gc.ca/meteocode/geodata/](https://dd.meteo.gc.ca/meteocode/geodata/)

Please, note that there is no shapefile which includes all the possible regions for a given warning. Any warning can cover multiple regions and sub-regions, depending of the nature and extent of the warning. This is why the polygon is included in each of the CAP files, as described in the README file here:

[https://dd.meteo.gc.ca/alerts/doc/README_CAP.txt](https://dd.meteo.gc.ca/alerts/doc/README_CAP.txt)

## Can I have satellite images?

Environment and Climate Change Canada does not provide satellite images or products to external users, apart those from our web site ([https://weather.gc.ca/satellite/index_e.html](https://weather.gc.ca/satellite/index_e.html)), as we are not the data producer.
A recommended site for freely available satellite images is from the University of Washington:

[https://www.atmos.washington.edu/~ovens/loops/](https://www.atmos.washington.edu/~ovens/loops/)

If you require a data feed of satellite images, we suggest users contact our U.S. counterparts at NOAA or to seek a provider in the private sector.

## Can I have access and use of icons displayed in the Citypage XML product?

These icons are covered by the standard Environment Canada Terms and Conditions: [ttps://www.canada.ca/en/transparency/terms.html](https://www.canada.ca/en/transparency/terms.html)
To make a commercial usage of these icons, you must obtain prior explicit consent.

You can download all ECCC weather icons from the following URL: [https://meteo.gc.ca/weathericons/NN.gif](https://meteo.gc.ca/weathericons/NN.gif)

where NN is a number between 00 and 45.

You can also create your own icons using WMO World Weather Symbols. See <em>A complete set of WMO weather symbols in SVG with full metadata and fallback PNGs</em> at this address:

[https://github.com/OGCMetOceanDWG/WorldWeatherSymbols](https://github.com/OGCMetOceanDWG/WorldWeatherSymbols)

## Can I have CSV minimum and maximum forecast temperature?

To obtain extreme forecast temperature data in CSV format, you can consult either:

* FMCN31 to FMCN38 forecast bulletins (CSV format), based on the Global Deterministic Prediction System (GDPS).
  0000 UTC forecasts contain the maximum of the current day, the minimum and maximum of day two and the minimum of day three.
  1200 UTC forecasts contain the minima and maxima of day two and day three.

* FMCN41 to FMCN48 forecast bulletins (CSV format), based on the Regional Deterministic Prediction System (RDPS). .
  1200 UTC forecasts contain the minimum and maximum of day two and the minimum of day three.
  Forecasts based on 0000 UTC data contain the maximum of the current day and the minimum and maximum of day two.

These bulletins are available on the MSC Datamart at this address:

[https://dd.meteo.gc.ca/bulletins/alphanumeric/YYYYMMDD/FM/CWAO/](https://dd.meteo.gc.ca/bulletins/alphanumeric/YYYYMMDD/FM/CWAO/)

The documentation can be found here:

[https://dd.meteo.gc.ca/bulletins/doc/README_bulletins.txt](https://dd.meteo.gc.ca/bulletins/doc/README_bulletins.txt)

## Can I have rainfall depth data?

Regarding QPF (Quantitative Precipitation Forecast) data in CSV format, you may be interested in the FOCN03 bulletins, namely spot forecasts of meteorological variables obtained from direct RDPS (Regional Deterministic Prediction System) output .
Each of these bulletins are produced specifically for individual Canadian forecast sites. The content is therefore variable. For example, values of forecast parameters are available at 6-hour intervals from 0 to 48 hours for some bulletins, and at 6-hour intervals from 0 to 24 hours and 12-hour intervals from 24 to 48 hours for some others.
Forecast weather elements may also differ from message to message.

These bulletins are available on the MSC Datamart at this address:

[https://dd.meteo.gc.ca/bulletins/focn03/YYYYMMDD/FO/](https://dd.meteo.gc.ca/bulletins/focn03/YYYYMMDD/FO/)

You can find documentation about alphanumeric bulletins on the MSC Datamart at the adress:

[https://dd.meteo.gc.ca/bulletins/doc/README_bulletins.txt](https://dd.meteo.gc.ca/bulletins/doc/README_bulletins.txt),

A bulletin search interface for the Meteorological Service of Canada http data server is available at:

[https://dd.weather.gc.ca/cgi-bin/bulletin_search.pl](https://dd.weather.gc.ca/cgi-bin/bulletin_search.pl),
and the associated documentation can be found here:

[https://dd.meteo.gc.ca/bulletins/doc/CMC_Bulletin_Search_Help_en.pdf](https://dd.meteo.gc.ca/bulletins/doc/CMC_Bulletin_Search_Help_en.pdf)

Finally, one could mention our geospatial services, and more specifically the GeoMet-Beta services. See: [https://lists.ec.gc.ca/pipermail/geomet-info/2016-July/000034.html](https://lists.ec.gc.ca/pipermail/geomet-info/2016-July/000034.html).
You can find RDPA-CaPA layers and in a near future you will be able to download directly CSV or other formats of data directly through the GRIB files.
If you wish to be advise of any update, we recommend you to subscribe to the mailing list through :

[https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/geomet-info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/geomet-info)

## Can I have snow water equivalent data?

The estimate for snow mass is likely valid over soil only. SNOD is available as an aggregated value but SDEN is available only for the soil fraction. The product SNOD x SDEN x factor for units likely provides the best estimate currently available for SWE. Be aware that SDEN from the soil fraction may or may not be representative of SDEN for the other surface types. 

Hence, the micro equation for the calculation of the SWE in mm (equivalent to kg/m2) from the absolute density SDEN and the thickness SNOD is:

    If the thickness is given in "cm" and SDEN in "kg/m3", what we have at the operations then : 

SWE = (SNOD * SDEN) / 100 -- SWE is in mm (or kg/m2, it is the equivalent for water) 

    If the thickness is given in "m" and SDEN in "kg/m3": 

SWE = SNOD * SDEN -- SWE is in mm (kg/2)

## I do not see a condition under the corresponding element of the Citypage XML file, is this normal?

Some weather stations are automatic (unmanned) and do not report the current condition.
If you look to the corresponding page on our web site, for example Edmonton, you will see that it is written <em>Not observed</em> for the condition, see:

[https://weather.gc.ca/city/pages/ab-50_metric_e.html](https://weather.gc.ca/city/pages/ab-50_metric_e.html)

This is why there is no icon or condition reported in the corresponding Citypage XML file.

## In the NWP systems changelog, I see several systems (e.g. SRPEOT) not mentioned in the list of systems with available data, where can I find this data?

These data are not yet available on the MSC Datamart. To be informed when new datasets are added, you can subscribe to the dd-info mailing list.

You can subscribe here:

[https://lists.ec.gc.ca/mailman/listinfo/dd_info](https://lists.ec.gc.ca/mailman/listinfo/dd_info)

## I'd like to use your data for profit, am I allowed to do that?

Yes, it is possible to use our data for profit-making purposes. You will find all the information you need to use our data [here](../licence/readme_en.md).

## What are the minimum requirements (processor, RAM) of my PC to be able to download data and/or use the GeoMet services?

There are no minimum specifications. However, internet access is required.

## In GeoMet, what styles are available for a WMS layer? Can I display a WMS layer in GeoMet with another style than the ones proposed?

To have a list of the styles available for a layer in GeoMet, you have to make a WMS request __GetCapabilities__ with the parameter __LAYERS__= which refers to the layer you want to display. For example, if you are looking for the list of available styles for the air temperature layer at 2 meters above the surface of the Global Deterministic Prediction System (GDPS.ETA_TT), here is the request that must be made: 

[https://geo.weather.gc.ca/geomet?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetCapabilities&LAYERS=GDPS.ETA_TT](https://geo.weather.gc.ca/geomet?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetCapabilities&LAYERS=GDPS.ETA_TT)

It is then possible to navigate through the XML to find the different Style parameters within the __Layer__ block.
Users can also specify their own styles by providing through the OGC Styled Layer Descriptor (SLD) standard, either by pointing to an external SLD document with the SLD parameter, or by specifying the SLD content directly in the SLD_BODY parameter. Note that the SLD_BODY content must be encoded as an HTTP URL.

## I see that you are using the QGIS (Geographic Information System) to visualize and manipulate the GeoMet layers and geospatial data in the Datamart, can I use other software to manipulate this data?

Yes, it is also possible to use the ArcGIS suite (ESRI's proprietary solution) which is also a GIS type software.

## Contact us

If you use the data available on the MSC Datamart, we strongly recommend to subscribe to the MSC Datamart's mailing list in order to be warned of any updates or changes regarding the data available. You can subscribe here:

[https://lists.ec.gc.ca/mailman/listinfo/dd_info](https://lists.ec.gc.ca/mailman/listinfo/dd_info)

Please use the following address to contact us for any comments or questions:
ec.dps-client.ec@canada.ca
