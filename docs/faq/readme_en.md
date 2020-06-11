[En français](readme_fr.md)

![ECCC logo](../img_eccc-logo.png)

[TOC](../readme_en.md) > FAQ

# MSC Open Data FAQ

This section contains the most frequently asked questions about the MSC open data.

## Table of Content

* [Can we have access to the verification scores of your numerical weather prediction models and how do they compare with other international centres ?](#can-we-have-access-to-the-verification-scores-of-your-numerical-weather-prediction-models-and-how-do-they-compare-with-other-international-centres)
* [I would like to use your data for profit, am I allowed to do so ?](#i-would-like-to-use-your-data-for-profit-am-i-allowed-to-do-so)
* [Why are message queues terminated after several hours of inactivity when using AMQP ?](#why-are-message-queues-terminated-after-several-hours-of-inactivity-when-using-amqp)
* [Can I have weather radar data ?](#can-i-have-weather-radar-data)
* [Can I have archived radar data ?](#can-i-have-archived-radar-data)
* [Are historical data forecasts from your numerical weather prediction models available ?](#are-historical-data-forecasts-from-your-numerical-weather-prediction-models-available)
* [How to be informed of any change to bulletins or numerical weather prediction model format and content ?](#how-to-be-informed-of-any-change-to-bulletins-or-numerical-weather-prediction-model-format-and-content)
* [How to be informed about problems with  numerical weather prediction model data production ?](#how-to-be-informed-about-problems-with-numerical-weather-prediction-model-data-production)
* [Why not produce just one big GRIB file with all the variables ?](#why-not-produce-just-one-big-grib-file-with-all-the-variables)
* [What is the reference coordinate system or datum of a numerical weather prediction model ?](#what-is-the-reference-coordinate-system-or-datum-of-a-numerical-weather-prediction-model)
* [Can I have the topography of a numerical weather prediction model ?](#can-i-have-the-topography-of-a-numerical-weather-prediction-model)
* [Can I have the land sea mask of a numerical weather prediction model ?](#can-i-have-the-land-sea-mask-of-a-numerical-weather-prediction-model)
* [Is it possible to access numerical weather prediction parameters other than those currently available on the MSC Datamart or is the list exhaustive ?](#is-it-possible-to-access-numerical-weather-prediction-parameters-other-than-those-currently-available-on-the-msc-datamart-or-is-the-list-exhaustive)
* [Can I have snow water equivalent data ?](#can-i-have-snow-water-equivalent-data)
* [In the numerical weather prediction systems changelog, I see several systems (e.g. SRPEOT) not mentioned in the list of systems with available data, where can I find this data ?](#in-the-numerical-weather-prediction-systems-changelog-i-see-several-systems-e-g-SRPEOT-not-mentioned-in-the-list-of-systems-with-available-data-where-can-i-find-this-data)
* [What is the difference between the two sets of observational data available on the MSC Datamart ?](#what-is-the-difference-between-the-two-sets-of-observational-data-available-on-the-msc-datamart)
* [How often are the observational data collected by province and territory refreshed ?](#how-often-are-the-observational-data-collected-by-province-and-territory-refreshed)
* [Can I have buoys data ?](#can-i-have-buoys-data)
* [Can I have access to weather warnings ?](#can-i-have-access-to-weather-warnings)
* [What are the main differences between RSS ATOM feeds and AMQP protocol to retrieve alerts ?](#what-are-the-main-differences-between-rss-atom-feeds-and-amqp-protocol-to-retreive-alerts)
* [Can I have satellite images ?](#can-i-have-satellite-images)
* [Are lightning data available ?](#are-lightning-data-available)
* [Can I have CSV minimum and maximum forecast temperature ?](#can-i-have-csv-minimum-and-maximum-forecast-temperature)
* [Can I have rainfall amount data ?](#can-i-have-rainfall-amount-data)
* [I do not see a condition under the corresponding element of the Citypage XML file, is this normal ?](#i-do-not-see-a-condition-under-the-corresponding-element-of-the-citypage-xml-file-is-this-normal)
* [Is it possible to access past observed air quality data and pollutant emission data used to calculate the Air Quality Health Index ?](#is-it-possible-to-access-past-observed-air-quality-data-and-pollutant-emission-data-used-to-calculate-the-air-quality-health-index)
* [Is there a discussion platform for users ?](#is-there-a-discussion-platform-for-users)

## Can we have access to the verification scores of your numerical weather prediction models and how do they compare with other international centres ?

The [European Centre for Medium-Range Weather Forecasting (ECMWF)](https://www.ecmwf.int/), designated in 2011 as the [WMO Lead Centre for Deterministic NWP Verification](https://confluence.ecmwf.int/pages/viewpage.action?pageId=24316358&src=sidebar), makes available all altitude and surface scores of all centres participating in the [World Meteorological Organization (WMO)](https://public.wmo.int/en) score exchange.

Thus, it is possible to obtain [upper air scores](https://apps.ecmwf.int/wmolcdnv/scores/time_series/msl) from Environment and Climate Change Canada's forecast models and compare them to the scores of other centres, according to the desired domain (e.g. northern hemisphere), for the parameters of interest (e.g. temperature at 850hPa), from 1998 to the present.

In addition, we publish daily [scores against radiosonde observations and against model analyses](https://weather.gc.ca/verification/index_e.html) for the [Global Deterministic Prediction System (GDPS)](../msc-data/nwp_gdps/readme_gdps_en.md) and the [Regional Deterministic Prediction System (RDPS)](../msc-data/nwp_rdps/readme_rdps_en.md), following the standards defined by the WMO.

## I would like to use your data for profit, am I allowed to do so ?

Yes, it is possible to use our data for profit-making purposes. You will find all the information you need to use our data in the [user licence](../licence/readme_en.md).

## Why are message queues terminated after several hours of inactivity when using AMQP ?

Users of the [AMQPS](../msc-datamart/amqp_en.md) service are supposed to run a daemon that downloads data continuously, such as the one provided by [Sarracenia](https://github.com/MetPX/sarracenia/blob/master/doc/sarra.rst). In the AMQP language, a pump, i.e. a host running Sarracenia, is a [broker](https://github.com/MetPX/sarracenia/blob/master/doc/Install.rst). The broker has a limited ability to queue products when a user experiences a long unintended interruption, for example, from a few hours to a few days. 
The performance of the overall service is affected by the presence of large queues for a single consumer, so queues should not be allowed to build up indefinitely. 

We keep the queues alive as long as we can reasonably do so, but this practice is only intended to give customers time to restart their service in the event of a failure. The length of disconnections that can be safely supported depends on the number of products subscribed to, which in turn determines the number of products queued. Typically, when there is a queue of more than 25,000 products and there are no customers, the queue is purged.

In general, it is preferable to use continuous access rather than periodic access, as this eliminates server download and load bandwidth spikes and reduces the risk of queues being purged on the server. Careful use of the "subtopic" directive in configurations will reduce the size of the queues, so that they can remain active during long interruptions.

## Can I have weather radar data ?

The weather radar data that we freely provide to the public are the [GIF images]( ../msc-data/obs_radar/readme_radarimage-datamart_en.md) on the MSC open data server. We also offer the [North American Radar Mosaic](../msc-data/obs_radar/readme_radar_geomet_en.md) via WMS Geospatial Web Services.

The raw data, as well as various other products, are provided by a [cost-recovered service](../cost-recovered/readme_en.md#dedicated-data-feed). As part of this service, we push the data to the client's FTP server and provide a 24/7 service. The documentation for [radar products](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/produits/samples/radar/vscan/Radar_Products_Available_CMC_Mai_2015_external.pdf) and [radar data formats](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/produits/samples/radar/vscan/Formats_used_in_URP_En_last_version.pdf) is available.

For the data feeds, the following formats are available:

* NUMERIC (ASCII)
* GIF format (recent GIFs available for free on the MSC Datamart)
* [IRIS](http://www.vaisala.com/en/defense/products/weatherradar/Pages/IRIS.aspx) raw format for the old C-Band radars 
* [ODIM_H5](https://support.hdfgroup.org/HDF5/users5.html) raw format for the new S-band radars

## Can I have archived radar data ?

Environment and Climate Change Canada does not have an online service to retrieve archived data.

The data retrieval service from our archive is under a [cost recovery policy](../cost-recovered/readme_en.md#archived-data-retrieval). We charge 99$/hour, with a minimum charge of 99$, to retrieve/recreate the requested data. The data itself is free.

Archive data are available in either raw format (IRIS/ODIM_H5) or products in ASCII format. Documentation regarding [radar products](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/produits/samples/radar/vscan/Radar_Products_Available_CMC_Mai_2015_external.pdf) and [radar data formats](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/produits/samples/radar/vscan/Formats_used_in_URP_En_last_version.pdf) is available.

Typical archived data retrieval requests require between 2-4 hours to process. If interested, please complete the order form below and send it via e-mail using the address: ec.dps-client.ec@canada.ca


| Information | Value |
|-------------|:-----:|
|Radar name(s) |       |       
|Product type (Raw, CAPPI, PRECIP, ECHOTOP, etc.) |       |
|Unit (dBZ, mm/hr) |       |
|Format (GIF, Numeric, IRIS/ODIM_H5) |       |
|Period (UTC) |       |
|Frequency (default: 10 minutes) |       |
|Delivery format (zip, tar, other) |       |
|Expected delivery date (when?) |       |
|Other information |       |
|Billing name and coordinates |       |

## Are historical data forecasts from your numerical weather prediction models available ?

Environment and Climate Change Canada does not have an online service to retrieve archived data.

The data retrieval service from our archive is under a [cost recovery policy](../cost-recovered/readme_en.md#archived-data-retrieval). We charge 99$/hour, with a minimum of 99$, to retrieve/recreate the requested data. The data itself is free.

Once users provide specifications for the required data, we can produce a sample and send it to the user for validation. An estimate can then be provided once the request is confirmed. Depending on the nature of the request this is usually in the low hundreds. If interested, please complete the order form below and send it via e-mail using the address: ec.dps-client.ec@canada.ca


| Information | Value |
|-------------|:-----:|
|Model (e.g. GDPS, RDPS, HRDPS, GIOPS) |       |       
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

* Forecast data are archived for 5 years. Other types of data (analyses for example) may have longer retention periods.
* Given the large volume of requests, a certain delay is to be expected. Please indicate if the request is urgent, we will try to prioritize it.

## How to be informed of any change to bulletins or model format and or content ?

For Canadian station bulletins, any change in the heading and station name is announced via what we call a GENOT (GEneral NOTification) message. We have a mailing list to distribute GENOTs for station and header changes. If you are interested in this e-mail notification, please send us your e-mail and we will add it to this mailing list.

In parallel, these [bulletins are available on the MSC Datamart](https://dd.meteo.gc.ca/doc/genots/).

To be advised of major changes, such as model resolution, you can subscribe to the GENOT 03 mailing list.
You can find an [example of a GENOT 03 bulletin](https://dd.meteo.gc.ca/doc/genots/2014/02/18/NOCN03_CWAO_182045___01117).

[](https://dd.meteo.gc.ca/doc/genots/2014/02/18/NOCN03_CWAO_182045___01117)

Finally, we strongly recommend to subscribe to our mailing lists [dd_info](https://lists.ec.gc.ca/mailman/listinfo/dd_info) and [GeoMet-Info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/geomet-info) to be warned of any updates or changes regarding the data availability.

## How to be informed about problems with model data production ?

Occasionally, NWP model data are late or even absent from our data dissemination services. To find out if this delay or absence is due to a production problem, you can consult the AACN01 CWAO bulletins.  These are bulletins issued by the CCPEC as required to inform MSC offices and other clients of any problems that may disrupt or delay the issuance and/or distribution of operational products.

To view the latest AACN01 CWAO bulletins, you can use the [Script Search Utility](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/bulletins/CMC_Bulletin_Search_Help_en.pdf) provided by ECCC. [Example to obtain the current AACN01 bulletins](https://dd.meteo.ec.gc.ca/cgi-bin/bulletin_search.pl?product=AA&location=CN01). For a specific day, you can refine your search. [Example to get the information for May 19, 2020](https://dd.meteo.gc.ca/cgi-bin/bulletin_search.pl?product=AA&location=CN01&day=19&month=05&year=2020).

There is also a mailing list for AACN01 bulletins. If you are interested, please contact us at ec.dps-client.ec@canada.ca and we will add you to the mailing list.

## Why not produce just one big GRIB file with all the variables ?

Environment and Climate Change Canada opted to put one variable per file because we presumed that most users would not require all the variables. This will then reach the same download speed as if all the GRIB files were in a single zip file.

## What is the reference coordinate system or datum of a numerical weather prediction model ?

To know the reference coordinate system of a numerical weather prediction model and the projection used to produce our numerical weather prediction files, just use the [GDAL](https://www.gdal.org/GDAL) tools (free software). The following command will provide you with the reference coordinate system and the projection of the file: `gdalinfo -proj4 file.grib2`.

The output information starts with `The coordinates system is:`. This command also gives access to the projection in Proj4 format which is commonly used in geospatial tools.

## Can I have the topography of a numerical weather prediction model ?

The topography of a numerical weather prediction model whose data is available in GRIB2 format can be obtained using the `HGT_SFC` parameter (smoothed topography of the model).

## Can I have the land sea mask of a numerical weather prediction model ?

You can use the variable `LAND_SFC` (Land cover) of prognostic hour 00 to determine this mask. When the value is 0, it is sea, when the value is not 0, it is land (or portion of it).

## Is it possible to access numerical weather prediction parameters other than those currently available on the MSC Datamart or is the list exhaustive ?

The list is not exhaustive. We are always very open to receive feedback from users and to know their needs. It is possible to communicate with us via the email address: ec.dps-client.ec@canada.ca.

## Can I have snow water equivalent data ?

The estimation of the snow mass is mainly valid for the ground. The GRIB parameter `SNOD` representing the snow depth on the ground is available as an aggregated value but the parameter `SDEN` (snow density) is only available for the fraction of soil. The `SNODxSDENxfactor` product for the units probably provides the best estimate currently available for snow water equivalent. Be aware that the `SDEN` parameter for the soil fraction may or may not be representative of snow density for other surface types.

Therefore, the micro equation for calculating snow water equivalent in mm (equivalent to kg/m2) from the absolute density `SDEN` and the thickness `SNOD` is expressed as :

* If the thickness is given in "cm" and `SDEN` in "kg/m3", which we have at operations, then `SWE = (SNOD * SDEN) / 100`; `SWE` is in mm (or kg/m2, which is the equivalent for water)
* If the thickness is given in "m" and the `SDEN` in "kg/m3", then `SWE = SNOD * SDEN`; `SWE` is in mm (kg/m2)

## In the numerical weather prediction systems changelog, I see several systems (e.g. SRPEOT) not mentioned in the list of systems with available data, where can I find this data ?

These data are not yet available on the MSC Datamart. To be informed when new datasets are added, you can subscribe to the [dd-info](https://lists.ec.gc.ca/mailman/listinfo/dd_info) and [GeoMet-Info](http://lists.ec.gc.ca/cgi-bin/mailman/listinfo/geomet-info) mailing lists.

## What is the difference between the two sets of observational data available on the MSC Datamart ?

We have 2 products that contain observations from the Environment and Climate Change Canada station network.

One is a one-station-per-file type, consisting of ground and marine weather observations per station, the [SWOB data](../msc-data/obs_station/readme_obs_insitu_swobdatamart_en.md), available in XML format. All Canadian station data are available in this product.

The second one groups [observational data from the same province or territory](../msc-data/obs_station/readme_obs_insitu_xmldatamart_en.md) by file, in XML format. Not all Canadian stations are contained in this product. These data are used in the official forecast web site weather.gc.ca. As a result, they are subject to certain rules (e.g. for winds, use of the average observed over a 2-minute period, if it is not possible to use a 10-minute average).

Consequently, it is not really possible to compare these 2 sets of data and it is strongly recommended to use the SWOB data, which are more complete and subject to no rules, for the region of interest.

## How often are the observational data collected by province and territory refreshed ?

The [provincial summary files](../msc-data/obs_station/readme_obs_insitu_xmldatamart_en.md) are updated 6 times per hour, but the simple fact that we update them does not necessarily mean that any of the stations in the summary file have updated their data since the last run. We update the observations on an hourly (not minute-by-minute) basis for each station at the beginning of the hour, but another update (called a "special obs" or "speci") within the hour is also possible if the observer feels that there has been a change large enough to warrant an update. 

It is possible, for example, that the 1614Z file may not contain observations different from those in 1611Z, so the user should not always expect changes in values for an individual station within the hour. We present only the data we obtain and, in this case, most stations report only once per hour.

## Can I have buoys data ?

Buoy data (marine observations) are available on the MSC Datamart at this address:

[https://dd.meteo.gc.ca/observations/swob-ml/marine/moored-buoys]( https://dd.meteo.gc.ca/observations/swob-ml/marine/moored-buoys)

You will find in the [documentation](../msc-data/obs_station/readme_obs_insitu_swobdatamart_en.md), a list of buoys currently available. Others will be added in the course of time.

Daily reports of MSC buoys are also published on the [Fisheries and Oceans Canada website](http://www.meds-sdmm.dfo-mpo.gc.ca/isdm-gdsi/waves-vagues/msc-smc/index-eng.html). Information on [drifting buoys](http://www.dfo-mpo.gc.ca/science/data-donnees/drib-bder/index-eng.html) is also available. 

Finally, these buoy data are accessible through the [alphanumeric bulletins](../msc-data/bulletins/readme_bulletins-datamart_en.md) available on the MSC Datamart with SM/SN/SIVD17 headings.

## Can I have access to weather warnings ?

You can find information about Environment and Climate Change Canada's warning in several places :

* First of all, the [official warnings are available in CAP-XML format on the MSC Datamart](https://dd.meteo.gc.ca/alerts/cap). The [documentation](../msc-data/alerts/readme_alerts-datamart_en.md) details these data and also gives information on the alert criteria of the public forecast and geographical information of the forecast locations, for all messages in CAP format.

* Our geospatial web services allow to display the warnings layer only in the [Beta version](../msc-geomet/readme_en.md) currently. Please monitor our [GeoMet-Info](http://lists.ec.gc.ca/cgi-bin/mailman/listinfo/geomet-info) mailing list to be informed when these warnings are available in GeoMet-Weather.

* In addition, ECCC has set up an [ATOM news feed through which alerts and warnings are available](https://weather.gc.ca/business/index_e.html#rss).

* Finally, ECCC has set up the [experimental EC Alert Me service](https://ecalertme.weather.gc.ca/guides/quickstart_en.php) to send warnings by email. 

## What are the main differences between RSS ATOM feeds and AMQP protocol to retrieve alerts ?

The main difference between RSS feeds (ATOM) and AMQP is that in the case of the RSS feed, user needs to send a request to know if new files
are available, whereas with AMQP, user is advised without sending any request.

If one wants to make an analogy, RSS feeds can be considered as a mailman who deposes letters in the mailbox, whereas AMQP can be considered as a delivery who rings at the door to give the postal package.

We recommend to use the AMQP protocol if it is important for users to receive the announcement and data once available, also AMQP is a longer-term solution.

## Can I have satellite images ?

Environment and Climate Change Canada does not provide satellite images or products to external users, apart those from our [web site](https://weather.gc.ca/satellite/index_e.html), as we are not the data producer.

A recommended site for freely available satellite images is from the [University of Washington](https://www.atmos.washington.edu/~ovens/loops/).

If you require a data feed of satellite images, we suggest users contact our U.S. counterparts at NOAA or to seek a provider in the private sector.

## Are lightning data available ?

Currently, only the [Canadian Lightning Danger Map](https://weather.gc.ca/lightning/) is available. Please note that you must manually update the website. It does not update itself, unlike the radar image site. The data are not yet available as part of the open data offer, please watch our mailing lists [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info) and [GeoMet-Info](http://lists.ec.gc.ca/cgi-bin/mailman/listinfo/geomet-info) for updates.
 
In the meantime, if you are interested in purchasing real-time or archived lightning data from the Canadian Lightning Detection Network (CLDN), please contact our colleagues at ec.rcdf-cldn.ec@canada.ca . There is a cost for private companies. The price depends on the area they need for the live data and the duration of the archived data. If the customer sends the CLDN their specifications, an estimate of the cost will be forwarded (request sent to Vaisala). 

## Can I have CSV minimum and maximum forecast temperature ?

To obtain extreme forecast temperature data in CSV format, you can consult either:

* Forecast bulletins FMCN31 to FMCN38 (CSV format), based on the [Global Deterministic Prediction System (GDPS)](../msc-data/nwp_gdps/readme_gdps_en.md). The forecast at 00Z contains the maximum for the current day, the minimum and maximum for the second day, and the minimum for the third day. The forecast at 12Z contains the minima and maxima of day two and day three.

* Forecast bulletins FMCN41 to FMCN48 (CSV format), based on the [Regional Deterministic Prediction System (RDPS)](../msc-data/nwp_rdps/readme_rdps_en.md). The 12Z forecast contains the minima and maxima of day two and the minima of day three. The forecast based on data at 00Z contains the maximum of the current day and the minimum and maximum of day two.

These bulletins are available on the MSC Datamart at the address: https://dd.weather.gc.ca/bulletins/alphanumeric/YYYYMMDD/FM/CWAO/

## Can I have rainfall amount data ?

Regarding QPF (Quantitative Precipitation Forecast) data in CSV format, you may be interested in the FOCN03 bulletins, i.e. grid point forecasts of meteorological variables obtained from the direct outputs of the RDPS (Regional Deterministic Prediction System).

Each of these bulletins is produced specifically for individual canadian forecast sites. The content is therefore variable. For example, values of forecast parameters are available at 6-hour intervals from 0 to 48 hours for some bulletins, and at 6-hour intervals from 0 to 24 hours and at 12-hour intervals from 24 to 48 hours for some others. The weather forecast elements may also vary from one message to another.

These [bulletins are available on the MSC Datamart](https://dd.meteo.gc.ca/bulletins/focn03). A [bulletin search interface](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/bulletins/CMC_Bulletin_Search_Help_en.pdf) for the Meteorological Service of Canada's HTTPS data server is also [available](https://dd.weather.gc.ca/cgi-bin/bulletin_search.pl).

Also, an optimal estimate of the amount of precipitation that has occurred during recent past periods of 6h or 24h is available through the [Regional Deterministic Precipitation Analysis](../msc-data/nwp_rdpa/readme_rdpa_en.md) data. This estimate integrates readings from precipitation sensors, weather radar and numerical weather prediction models. The geographical coverage is North America (Canada, United States and Mexico).

## I do not see a condition under the corresponding element of the Citypage XML file, is this normal ?

Some weather stations are automatic (unmanned) and do not report the current condition. If you look to the corresponding page on our web site, for example [Edmonton](https://weather.gc.ca/city/pages/ab-50_metric_e.html), you will see that it is written <em>Not observed</em> for the condition.

This is why there is no icon or condition reported in the corresponding Citypage XML file.

## Is it possible to access past observed air quality data and pollutant emission data used to calculate the Air Quality Health Index ?

In Canada, observed air quality data are generally produced by provinces and municipalities and collected by ECCC. This is true for both real-time and "official" data that are subject to detailed quality control and are usually published the following year. These official data are assembled in the [National Air Pollution Surveillance (NAPS)](http://data.ec.gc.ca/data/air/monitor/national-air-pollution-surveillance-naps-program/?lang=en) program, now on the ECCC data catalogue.

Also, a number of Canadian stations are available in the U.S. [AirNow](https://www.airnow.gov/aqi-and-health/) database, and are also downloadable from the Open Project [OpenAQ](https://openaq.org/#/map?parameter=o3&_k=6p035e). On the other hand, ECCC only publishes observations in the form of the Air Quality Health Index, which can be found in the [MSC Datamart](../msc-data/aqhi/readme_aqhi_en.md).

Finally, the [National Pollutant Release Inventory](https://www.canada.ca/en/environment-climate-change/services/national-pollutant-release-inventory/tools-resources-data/exploredata.html) is available. Please note that polluting facilities are given considerable time to report their emissions, therefore the information is published more than one year after the current date, on an annual basis.

## Is there a discussion platform for users ?

A discussion platform dedicated to MSC open data has been set up by a third party to allow the user community to interact more easily and benefit from each other's experience:

[http://meteocentre.com/help/msc-open-data/](http://meteocentre.com/help/msc-open-data/)

While we approve and applaud this initiative, we would like to make it clear that ECCC and MSC are not responsible for this site and their employees are not obligated to respond to the questions asked. When ECCC or MSC employees participate, they do so in their personal capacity.

