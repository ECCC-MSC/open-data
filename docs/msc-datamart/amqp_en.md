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

- '__*__'  character is a wildcard (only one '*' per directory)
- '__#__'  means all remaining possibilities and must appear at the end of the key.

### Script

The script allowing to recover products on the MSC Datamart and to place them in a local directory chosen by the user uses the client Sarracenia (Subscribe And Recursively Re-advertise Ad nauseam to Communicate Everything Nearly Instantly and Always).

This client is designed to perform downloads in a very reliable manner and is widely used within the Government of Canada:

https://github.com/MetPX/Sarracenia 

An overview is available here: [https://github.com/MetPX/sarracenia/blob/master/doc/sarra.rst](https://github.com/MetPX/sarracenia/blob/master/doc/sarra.rst)

The installation guide can be found at this address :
[https://github.com/MetPX/sarracenia/blob/master/doc/Install.rst](https://github.com/MetPX/sarracenia/blob/master/doc/Install.rst)

Regarding the user guide, please consult : 
[https://github.com/MetPX/sarracenia/blob/master/doc/subscriber.rst](https://github.com/MetPX/sarracenia/blob/master/doc/subscriber.rst)

Several examples of configuration files are also available to users, see:
[https://github.com/MetPX/sarracenia/tree/master/sarra/examples/subscribe](https://github.com/MetPX/sarracenia/tree/master/sarra/examples/subscribe)

__NOTE__:

To __facilitate support__, our analysts suggest that users identify themselves, in order to more easily track down queues in case of problems. It is therefore highly recommended to add one of the following lines in the sr_subscribe configuration:

* queue_name q_${BROKER_USER}.${PROGRAM}.${CONFIG}.${HOSTNAME} (dynamic option)
* q_anonymous.sr_subscribe.config_name.company_name (static option)

Example: q_anonymous.sr_subscribe.citypage.companyX

## Windows environment

Working with the Windows environment, simply download the latest version of Sarracenia at this address:

[https://hpfx.collab.science.gc.ca/~pas037/Sarracenia_Releases/](https://hpfx.collab.science.gc.ca/~pas037/Sarracenia_Releases/)

This is an EXE file that can be used without having to [install](https://github.com/MetPX/sarracenia/blob/master/doc/fr/Install.rst) a Python environment.

## Examples

Here are some specific examples to receive alerts, citypage_weather data for one city and RDPS GRIB parameters:

* The available commands are:
    * alerts : sr_subscribe [amqp_cap.xml.conf](./amqp_cap-xml.conf) start/stop/status
    * citypage_weather : sr_subscribe [amqp_citypage.conf](./amqp_citypage.conf) start/stop/status
    * rdps_grib : sr_subscribe [amqp_rdps-grib.conf](./amqp_rdps-grib.conf) start/stop/status
* The logs are available under ~/.cache/sarra/log
* To make a cleanup, use : sr_subscribe configname.conf cleanup

## External links

* AMQP protocol on Wikipedia:
[https://en.wikipedia.org/wiki/Advanced_Message_Queuing_Protocol](https://en.wikipedia.org/wiki/Advanced_Message_Queuing_Protocol)

* AMQP python library: 
[https://pypi.python.org/pypi/amqplib](https://pypi.python.org/pypi/amqplib)


## Contact Us

If you use the data available on the MSC Datamart, it is strongly recommend that you subscribe to the MSC Datamart's mailing list in order to be warned of any updates or changes regarding the data available. You can subscribe here:

[https://lists.ec.gc.ca/mailman/listinfo/dd_info](https://lists.ec.gc.ca/mailman/listinfo/dd_info)

Please use the following address to contact us for any comments or questions: [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca) 
