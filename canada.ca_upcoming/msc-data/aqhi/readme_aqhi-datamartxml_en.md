[En Français](readme_aqhi-datamartxml_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC Open Public Data](../readme_en.md) > AQHI

# Air Quality Health Index (AQHI) observation and forecast data in XML format

The [Air Quality Health Index AQHI](readme_aqhi_en.md) is a scale designed to help quantify the quality of the air in a certain region on a scale from 1 to 10. When the amount of air pollution is very high, the number is reported as 10+. It also includes a category that describes the health risk associated with the index reading e.g. Low, Moderate, High, or Very High Health Risk . The AQHI is calculated based on the relative risks of a combination of common air pollutants that are known to harm human health, including ground-level ozone, particulate matter, and nitrogen dioxide. The AQHI formulation captures only the short term or acute health risk exposure of hour or days at a maximum .
The formulation of the AQHI may change over time to reflect new understanding associated with air pollution health effects. The AQHI is calculated from data observed in real time, without being verified quality control.

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](.../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](.../../usage-overview/readme_en.md) is also available.

The data is available via the HTTP protocol. It is possible to access it with a standard browser. In this case, we obtain a list of links giving access to a XML file.

The data can be accessed at the following address:
* https://dd.weather.gc.ca/air_quality/aqhi/

where:

![Description de la structure des répertoires](https://dd.meteo.gc.ca/air_quality/doc/aqhi_structure.png)

## File name nomenclature 

NOTE: ALL HOURS ARE IN UTC.

__1. XML Files :__

    1.1  Observations (Note: monthly summary XML files are not yet available):
       Hourly file:   AQ_OBS_CGNDBcode_YYYYMMDDhhmm.xml
                      AQ_OBS_CGNDBcode_CURRENT.xml (copy of the most recent real-time observation file)
       Location: https://dd.weather.gc.ca/air_quality/aqhi/[atl|ont|pnr|pyr|que]/observation/realtime/xml

where:

* **'AQ_OBS_'** : Filename prefix. Constant string.
* __CGNDBcode__ : 5-letter CGNDB code which identifies each AQHI community. A list of CGNDB codes is given
at the end of this README file.
* __YYYY__ : Year of the observation, 4 digits;
* __MM__ : Month of the observation, 2 digits (January = 01);
* __DD__ : Day of the observation, 2 digits;
* __hh__ : Hour of the observation, 2 digits;
* __mm__ : Minute of the observation, 2 digits.

__1.2  Public forecasts (Note: monthly summary XML files are not yet available) :__

       Regular issue:     AQ_FCST_CGNDBcode_YYYYMMDDhhmm.xml
       Amended forecasts: AQ_FCST_CGNDBcode_YYYYMMDDhhmm_AMD.xml
                          AQ_FCST_CGNDBcode_CURRENT.xml (copy of the most recent real-time forecast file)
       Location: https://dd.weather.gc.ca/air_quality/aqhi/[atl|ont|pnr|pyr|que]/forecast/realtime/xml

where:
* **'AQ_FCST_'**:  Filename prefix. Constant string.
* __CGNDBcode__ : 5-letter CGNDB code which identifies each AQHI communitiy. A list of CGNDB codes is given
at the end of this README file.
* __YYYY__ : Year of the forecast issue time, 4 digits;
* __MM__ : Month of the forecast issue time, 2 digits (January = 01);
* __DD__ : Day of the forecast issue time, 2 digits;
* __hh__ : Hour of the forecast issue time, 2 digits;
* __mm__ : Minute of the forecast issue time, 2 digits;
* __'AMD'__ : the suffix appended to the filename to indicate that the file is
an amendment.

Note: The XML observation files are produced hourly, at approximately 40 minutes past the hour,
and are available on Datamart for a period of 48 hours. The XML public forecast files are issued
twice per day at approximately 6am and 5pm local time and are available on Datamart for a
period of 48 hours.

## Support

If you have any questions about these data, please contact us at: ec.dps-client.ec@canada.ca

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).

