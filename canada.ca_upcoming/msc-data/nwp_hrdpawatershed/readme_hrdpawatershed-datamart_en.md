[En Français](readme_hrdpawatershed-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC Open Public Data](../readme_en.md) > HRDPA Watershed

# High Resolution Deterministic Precipitation Analysis (HRDPA) average watershed precipitation Data in GRIB2 Format

Data for over 1900 watersheds is available. In order to reduce the number of files on the Datamart, it has been necessary to group these watersheds by drainage basin:

 - Maritime Provinces
 - St. Lawrence
 - Northern Quebec and Labrador
 - Southwest Hudson Bay
 - Nelson River
 - Western Hudson Bay
 - Great Slave Lake
 - Pacific
 - Yukon River
 - Arctic
 - Mississipi River

In addition to the average precipitation, the average confidence index of the analysis is also provided. As explained in the documentation of the HRDPA, the analysis is a weighted average of a numerical weather prediction and of observations (both in-situ and radar). The total weight given to observations (from zero to one) in the final computation is reported alongside the precipitation amount in the gridded HRDPA data files. 

This number can also be averaged so as to reflect the average weight given to observations in the computation of watershed precipitation. It can be interpreted as a confidence index for the precipitation amount reporter. Values close to one indicate that the HRDPA estimate comes essentially from observed precipitation data, whereas values close to zero indicate that the HRDPA estimate comes essentially from a short-term precipitation forecast.

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](.../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](.../../usage-overview/readme_en.md) is also available.

The data is available using the HTTP protocol and resides in a directory that is plainly accessible to a web browser. Visiting that directory with an interactive browser will yield a raw listing of links, each link being a downloadable GRIB2 file. In practice, we recommend writing your own script to automate the downloading of the desired data (using wget or equivalent). If you are unsure of how to proceed, you might like to take a look at our brief wget usage guide.

The data can be accessed at the following URLs:

* https://dd.weather.gc.ca/analysis/precip/hrdpa_watershed/shapefile/HH

where:

* __HH__ :  Accumulation period in hours: 06 or 24 

## File name nomenclature 

NOTE: ALL HOURS ARE IN UTC.

The files have the following nomenclature:

CMC_HRDPA_WATERSHED-HHH-CC00cutoff_SFC_0_ps2.5km_YYYYMMDDHH_000_ID.SUF

where:

* __HHH__ : Accumulation period in hours (006 or 024)
* __CC__ : cutoff time in hours (01 or 07) after the end of the accumulation period
* __YYYYMMDDHH__ : Analysis validity date and hour (timestamp associated with the end of the accumulation period)
* __ID__ : Drainage basin ID, from 01 to 11:
	01 Maritime Provinces
	02 St. Lawrence
	03 Northern Quebec and Labrador
	04 Southwest Hudson Bay
	05 Nelson River
	06 Western Hudson Bay
	07 Great Slave Lake
	08 Pacific
	09 Yukon River
	10 Arctic
	11 Mississipi River

* __SUF__ : suffix of Shapefile:
	"dbf" - attributes of the shapes found in the Shapefile
	"prj" - text file describing the projection of the data
	"shp" - binary file containing the geometry data
	"shx" - index file for the geometry data

Example: 
CMC_HRDPA_WATERSHED-024-0700cutoff_SFC_0_ps2.5km_2018021612_000_10.dbf
CMC_HRDPA_WATERSHED-024-0700cutoff_SFC_0_ps2.5km_2018021612_000_10.prj
CMC_HRDPA_WATERSHED-024-0700cutoff_SFC_0_ps2.5km_2018021612_000_10.shp
CMC_HRDPA_WATERSHED-024-0700cutoff_SFC_0_ps2.5km_2018021612_000_10.shx

This set of files would contain average precipitation for a 24h accumulation period ending at 12 UTC on February 16, 2018 for watersheds in the arctic basin, and the analysis would have been produced 7 hours after the end of that accumulation period.

The area associated with each watershed is defined by a single polygon.

Seven attributes are provided for each watershed:

* __Station__    : Station ID
* __StationNam__ : Station Name
* __Stn_UID__    : Station unique ID (at the moment, corresponds to the Station ID, followed by _1)
* __Shp_Area__   : Area associated with the polygon (in km2)
* __Shp_Perime__ : Perimeter associated with the polygon (in km)
* __PR_mm__      : Average watershed precipitation associated with the polygon (in mm)
* __CFIA__       : Average confidence index associated with the polygon (from zero to one), which reflects the average weight given to observations (in-situ and radar) in the computation of the watershed precipitation

## List of variables

Warning: the tables below are not up to date (to come), some variables are missing. Feel free to [contact us](mailto:ec.dps-client.ec@canada.ca) for more information.

* __Station__    : Station ID
* __StationNam__ : Station Name
* __Stn_UID__    : Station unique ID (at the moment, corresponds to the Station ID, followed by _1)
* __Shp_Area__   : Area associated with the polygon (in km2)
* __Shp_Perime__ : Perimeter associated with the polygon (in km)
* __PR_mm__      : Average watershed precipitation associated with the polygon (in mm)
* __CFIA__       : Average confidence index associated with the polygon (from zero to one), which reflects the average weight given to observations (in-situ and radar) in the computation of the watershed precipitation

## Support

If you have any questions about these data, please contact us at: ec.dps-client.ec@canada.ca

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).
