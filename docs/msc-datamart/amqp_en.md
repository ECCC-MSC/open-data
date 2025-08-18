[En français](amqp_fr.md)

![ECCC logo](../img_eccc-logo.png)

[TOC](../readme_en.md) > [MSC Datamart](readme_en.md) > AMQP


# Advanced Message Queuing Protocol

## About

The HTTPS raw data server called 'MSC Datamart' is a real-time on-demand download service.  The user must, in effect, act to retrieve particular data, and the request will only be successful if the data was previously published on the server.  

The exact time of publication of the data on the MSC Datamart is more or less predictable: a new weather warning can appear at any time, while other data are produced on a fairly regular schedule (but still subject to occasional interruptions).  However, it may be important for some applications that data is obtained as soon as it is published.   

Attempts to obtain MSC Datamart data as soon as they appear on the server generate numerous premature queries that are obviously unsuccessful. This motivates the use of a more elegant and convenient solution for users.    

To facilitate the retrieval of timely data on the MSC Datamart, the Meteorological Service of Canada (MSC) has set up a data wire for announcing file availability on the MSC Datamart.  This data wire uses the 'Advanced Message Queuing Protocol' (AMQP) protocol, making it  possible not only to be notified of the availability of products on the MSC Datamart as they are published, but also to receive them automatically. 

The service permits targeting notifications for a specific set of files (weather warnings, observations, data model, etc.) and thus notification for only those products of interest to the user.

A sample script using this protocol is made available by Environment and Climate Change Canada.  See "Script" section below.

## Description

The script uses the python language ([https://www.python.org/](https://www.python.org/)) and must be installed on the system where it will be run.  Moreover, the python-amqp library must also be installed.  Please read the documentation specific to your operating system for instructions on installing the software and this library.

The SSL (Secure Sockets Layers) AMQP server is located at this address: dd.weather.gc.ca

It is possible to connect anonymously using the following credentials:

- __User name__: anonymous
- __Password__: anonymous 

### Path

For the subtopic, one only needs to  write the directory where the product is found, replacing the slash "/" with a dot ".".

This subtopic is: PRODUCT.DIRECTORY.ON.THE.DATAMART

- '__\*__'  character is a wildcard (only one '*' per directory)
- '__#__'  means all remaining possibilities and must appear at the end of the key.

### Script

The script allowing to recover products on the MSC Datamart and to place them in a local directory chosen by the user uses the client Sarracenia (Subscribe And Recursively Re-advertise Ad nauseam to Communicate Everything Nearly Instantly and Always).

This client is designed to perform downloads in a very reliable manner and is widely used within the Government of Canada:

[https://metpx.github.io/sarracenia/](https://metpx.github.io/sarracenia/)

An overview is available here: [https://metpx.github.io/sarracenia/Explanation/Overview.html](https://metpx.github.io/sarracenia/Explanation/Overview.html)

The installation guide can be found at this address :
[https://metpx.github.io/sarracenia/Tutorials/Install.html](https://metpx.github.io/sarracenia/Tutorials/Install.html)

Regarding the user guide, please consult : 
[https://metpx.github.io/sarracenia/How2Guides/subscriber.html](https://metpx.github.io/sarracenia/How2Guides/subscriber.html)

Several examples of configuration files are also available to users, see:
[https://github.com/MetPX/sarracenia/tree/stable/sarracenia/examples/subscribe](https://github.com/MetPX/sarracenia/tree/stable/sarracenia/examples/subscribe)

__NOTE__:

To __facilitate support__, our analysts suggest that users identify themselves, in order to more easily track down queues in case of problems. It is therefore highly recommended to add one of the following lines in the Sarracenia configuration:

* `queueName q_${BROKER_USER}.${PROGRAM}.${CONFIG}.${HOSTNAME}` (dynamic option)
* `queueName q_anonymous.subscribe.config_name.company_name` (static option)

Example: `q_anonymous.subscribe.citypage.companyX`

Also, here is a list of recommendations for the "anonymous" user who wishes to retrieve a significant subset of data without fear of losing information:

* The `expire` option reflects the user's desired retention period. We suggest a value greater than 5 minutes, which is the default.  
* Increase the number of instances in the configuration which allows for more efficient processing of messages to minimize their number in the queue.
* Split the configurations into several smaller configurations to avoid reaching the maximum of 10,000 messages in a queue (the name of the queues must be different between the configurations)

## Windows environment

Working with the Windows environment, simply download the latest version of Sarracenia at this address:

[https://github.com/MetPX/sarracenia/releases](https://github.com/MetPX/sarracenia/releases)

This is an EXE file that can be used without having to [install](https://github.com/MetPX/sarracenia/blob/master/doc/fr/Install.rst) a Python environment.

## Examples

Here are some specific examples to receive alerts, citypage_weather data for one city and RDPS GRIB parameters:

Here are some specific examples to receive alerts, citypage_weather data and RDPS GRIB parameters:

* The available commands are:

    * [alerts](https://github.com/MetPX/sarracenia/blob/development/sarracenia/examples/subscribe/ddc_cap-xml.conf):
    
        * `sr3 add subscribe/ddc_cap-xml.conf`
        * `sr3 start subscribe/ddc_cap-xml.conf`
        * `sr3 stop subscribe/ddc_cap-xml.conf`
        * `sr3 cleanup subscribe/ddc_cap-xml.conf`
	
    * [citypage_weather](https://github.com/MetPX/sarracenia/blob/development/sarracenia/examples/subscribe/dd_citypage.conf):
    
        * `sr3 add subscribe/dd_citypage.conf`
        * `sr3 start subscribe/dd_citypage.conf`
        * `sr3 stop subscribe/dd_citypage.conf`
        * `sr3 cleanup subscribe/dd_citypage.conf`
	
    * [RDPS](https://github.com/MetPX/sarracenia/blob/development/sarracenia/examples/subscribe/dd_citypage.conf):
    
        * `sr3 add subscribe/dd_rdps.conf`
        * `sr3 start subscribe/dd_rdps.conf` 
        * `sr3 stop subscribe/dd_rdps.conf`
        * `sr3 cleanup subscribe/dd_rdps.conf`
	
    * [bulletins](https://github.com/MetPX/sarracenia/blob/development/sarracenia/examples/subscribe/dd_aacn_bulletins.conf):

        * `sr3 add subscribe/dd_aacn_bulletins.conf`
        * `sr3 start subscribe/dd_aacn_bulletins.conf`
        * `sr3 stop subscribe/dd_aacn_bulletins.conf`
        * `sr3 cleanup subscribe/dd_aacn_bulletins.conf`

* The subscriber config files are placed in `~/.config/sr3/subscribe`
* The logs are available under `~/.cache/sr3/log`
* To make a cleanup, use: `sr3 cleanup subscribe/config_name.conf`

Note: The `sr3 add` command automatically places the example config file into the user’s `~/.config/sr3/subscribe` directory.

## External links

* AMQP protocol on Wikipedia:
[https://en.wikipedia.org/wiki/Advanced_Message_Queuing_Protocol](https://en.wikipedia.org/wiki/Advanced_Message_Queuing_Protocol)

* AMQP python library: 
[https://pypi.python.org/pypi/amqplib](https://pypi.python.org/pypi/amqplib)

## Contact Us

If you use the data available on the MSC Datamart, it is strongly recommend that you subscribe to the MSC Datamart's mailing list in order to be warned of any updates or changes regarding the data available. You can subscribe here:

[https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/)

User support is provided on a best effort basis during normal business hours. Users requesting support are invited to [contact us](https://www.weather.gc.ca/mainmenu/contact_us_e.html).
