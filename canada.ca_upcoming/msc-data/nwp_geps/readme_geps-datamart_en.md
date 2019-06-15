[En Français](readme_geps-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC Open Public Data](../readme_en.md) > GEPS

# Global Ensemble Prediction System (GEPS) Data in GRIB2 Format

This page describes the [Global Ensemble Prediction System](readme_geps_en.md) data available in GRIB2 format.

## Data address 

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](.../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](.../../usage-overview/readme_en.md) is also available.

The data is available using the HTTP protocol and resides in a directory that is plainly accessible to a web browser. Visiting that directory with an interactive browser will yield a raw listing of links, each link being a downloadable GRIB2 file. In practice, we recommend writing your own script to automate the downloading of the desired data (using wget or equivalent). If you are unsure of how to proceed, you might like to take a look at our brief wget usage guide.

The data can be accessed at the following URLs:

* https://dd.weather.gc.ca/ensemble/geps/grib2/raw/HH/hhh/

where:

* __raw__ : is a constant string indicating model data is raw (not processed)
* __HH__ : model run start, in UTC [00,12]
* __hhh__ : forecast hour [000, 003, …, 192, 198, 204, ..., 378, 384] and [000, 003, …, 192, 198, 204, ..., 762, 768] each Thursday at 000UTC

## Grid specifications

This table lists details of the latitude-longitude grid used in the encoding of the GRIB variables.

| Grid Parameter          | Value of Parameter       |
|-------------------------|--------------------------|
| ni                      | 720 points               |
| nj                      | 361 points               |
| resolution              | 0.5°                     |
| first gris point coordinate | 90° S 000° E         |

## File name nomenclature 

NOTE: ALL HOURS ARE IN UTC.

The files have the following nomenclature:

CMC_geps-raw_Variable_LevelType_Level_latlonResolution_YYYYMMDDHH_Phhh_allmbrs.grib2

where:

* __CMC_geps-raw__ : constant string indicating that the data is from the Canadian Meteorological Centre (CMC), the model used (geps: Global Ensemble Prediction System) and the data type (raw).
* __Resolution__ : Constant string indicating the data resolution (0p5x0p5)
* __Variable__ : Variable type included in this file. To consult a complete list, refer to the variables section.
* __LevelType__ : Level type. To consult a complete list, refer to the variables section.
* __Level__ : Level value. To consult a complete list, refer to the variables section.
* __YYYYMMDD__ : Year, month and day of the beginning of the forecast.
* __HH__ : UTC run time [00,12]
* __Phhh__ : P is a constant character. hhh is the forecast hour [000, 003, …, 192, 198, 204, ..., 378, 384] or [000, 003, …, 192, 198, 204, ..., 762, 768] each Thursday at 000UTC
* __allmbrs__ : constant string indicating that all the members of the ensemble are included in this file
* __grib2__ : constant string indicating the GRIB2 format is used

Example of file name:
CMC_geps-raw_UGRD_ISBL_0925_latlon0p5x0p5_2010090100_P078_allmbrs.grib2

This file originates from the Canadian Meteorological Center (CMC) and contains the raw data of the Global Ensemble Prediction System (CMC_geps-raw). The data in the file start on September 1st 2010 at 00Z (2010090100). It contains the U-component wind (UGRD) at the isobaric level 925 mb (ISBL_0925) for the forecast hour 78 (P078), for all members (allmbrs) in GRIB2 format (.grib2).

## List of variables

Warning: the tables below are not up to date (to come), some variables are missing. Feel free to [contact us](mailto:ec.dps-client.ec@canada.ca) for more information.

| Ensemble members                   | Forecast hour                      |
|-----------------------------------------|-----------------------------------------|
| Control member (member 0)              | [0-hour forecast](https://weather.gc.ca/grib/GEPS_HR/GEPS_latlon0p5x0p5_P000_MBRZERO_e.html) ; [Non-zero forecast hours](https://weather.gc.ca/grib/GEPS_HR/GEPS_latlon0p5x0p5_PNONZERO_MBRZERO_e.html) |
| Perturbed members                       | [0-hour forecast](https://weather.gc.ca/grib/GEPS_HR/GEPS_latlon0p5x0p5_P000_MBRNONZERO_e.html) ; [Non-zero forecast hours](https://weather.gc.ca/grib/GEPS_HR/GEPS_latlon0p5x0p5_PNONZERO_MBRNONZERO_e.html)|       

## Support

If you have any questions about these data, please contact us at: ec.dps-client.ec@canada.ca

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).
