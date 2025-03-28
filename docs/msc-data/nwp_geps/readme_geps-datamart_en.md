[En français](readme_geps-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [GEPS](readme_geps_en.md) > GEPS on MSC Datamart

# Global Ensemble Prediction System (GEPS) Data in GRIB2 Format

This page describes the [Global Ensemble Prediction System](readme_geps_en.md) data available in GRIB2 format.

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available using the HTTPS protocol and resides in a directory that is plainly accessible to a web browser. Visiting that directory with an interactive browser will yield a raw listing of links, each link being a downloadable GRIB2 file.

The data can be accessed at the following URLs :

* [https://dd.weather.gc.ca/ensemble/geps/grib2/{TYPE}/{HH}/{hhh}/](https://dd.weather.gc.ca/ensemble/geps/grib2)

where :

* __TYPE__ : String indicating individual members direct model outputs (not processed) or probabilistic products created from all members [raw, products]
* __HH__ : Model run start, in UTC [00,12]
* __hhh__ : Forecast hour [000, 003, …, 192, 198, 204, ..., 378, 384] and [000, 003, …, 192, 198, 204, ..., 930, 936] each Monday and Thursday at 000UTC

## Grid specifications

This table lists details of the latitude-longitude grid used in the encoding of the GRIB variables.

| Grid Parameter          | Value of Parameter       |
|-------------------------|--------------------------|
| ni                      | 720 points               |
| nj                      | 361 points               |
| resolution              | 0.5°                     |
| first gris point coordinate | 90° S 000° E         |

## File name nomenclature 

The files have the following nomenclature :

* CMC_geps-raw_Variable_LevelType_Level_latlonResolution_YYYYMMDDHH_Phhh_allmbrs.grib2
* CMC_geps-prob_Variable_LevelType_Level_latlonResolution_YYYYMMDDHH_Phhh_all-products.grib2

where :

* __CMC_geps__ : Constant string indicating that the data is from the Canadian Meteorological Centre (CMC), the model used (geps: Global Ensemble Prediction System).
* __raw__ : individual members direct model output
* __prob__ : probabilistic products created from all members
* __Resolution__ : Constant string indicating the data resolution (0p5x0p5)
* __Variable__ : Variable type included in this file. To consult a complete list, refer to the variables section.
* __LevelType__ : Level type. To consult a complete list, refer to the variables section.
* __Level__ : Level value. To consult a complete list, refer to the variables section.
* __YYYYMMDD__ : Year, month and day of the beginning of the forecast.
* __HH__ : UTC run time [00,12]
* __Phhh__ : P is a constant character. hhh is the forecast hour [000, 003, …, 192, 198, 204, ..., 378, 384] or [000, 003, …, 192, 198, 204, ..., 930, 936] each Monday and Thursday at 000UTC
* __allmbrs__ : Constant string indicating that all the members of the ensemble are included in this file
* __all-products__ : indicating that all probabilistic products for this variable are contain in the file
* __grib2__ : Constant string indicating the GRIB2 format is used

Example of file name :

CMC_geps-raw_UGRD_ISBL_0925_latlon0p5x0p5_2010090100_P078_allmbrs.grib2

This file originates from the Canadian Meteorological Center (CMC) and contains the raw data of the Global Ensemble Prediction System (CMC_geps-raw). The data in the file start on September 1st 2010 at 00Z (2010090100). It contains the U-component wind (UGRD) at the isobaric level 925 mb (ISBL_0925) for the forecast hour 78 (P078), for all members (allmbrs) in GRIB2 format (.grib2).

## List of variables

__Individual members__:

<table id="csv-table" class="display"></table>

<link href="https://cdn.jsdelivr.net/npm/simple-datatables@latest/dist/style.css" rel="stylesheet" type="text/css">
<script src="https://cdn.jsdelivr.net/npm/simple-datatables@latest"></script>
<script src="../../../js/variables_datatable.js" type="text/javascript"></script>
<script>
  loadTable("csv-table", "../../../assets/csv/GEPS_Variables-List_en.csv");
</script>

__Ensemble products__:

<table id="csv-prob-table" class="display"></table>

<script>
  loadTable("csv-prob-table", "../../../assets/csv/GEPS-Products_Variables-List_en.csv");
</script>

The files contain probability products by member counting above or below different thresholds, percentiles, means, medians and standard deviations. Note that products and thresholds are defined in the file metadata. The following products are available for each of the variables listed below.

###### HGT

* Minimum (0 percentile), maximum (100th percentile), standard deviation and mean

###### HEATX

* Probability above 298.14, 303.14, 308.14, 311.14, 313.14 and 315.14 K
* Minimum (0 percentile), maximum (100th percentile), median (50th percentile), standard deviation and mean
* 10 percentile, 25 percentile, 75 percentile and 90 percentile

###### FPRATE

* Probability above 1, 2.5, 5, 10, 15, 20, 25, 30, 40 and 50 kg/(m<sup>2</sup>*s)
* Minimum (0 percentile), maximum (100th percentile), median (50th percentile), standard deviation and mean
* 10 percentile, 25 percentile, 75 percentile and 90 percentile

###### GUST

* Probability above 10, 15 and 25 m/s

###### IPRATE

* Probability above 1, 2.5, 5, 10, 15, 20, 25, 30, 40 and 50 kg/(m<sup>2</sup>*s)
* Minimum (0 percentile), maximum (100th percentile), median (50th percentile), standard deviation and mean
* 10 percentile, 25 percentile, 75 percentile and 90 percentile

###### RPRATE

* Probability above 1, 2.5, 5, 10, 15, 20, 25, 30, 40, 50, 75, 100 and 150 kg/(m<sup>2</sup>*s)
* Minimum (0 percentile), maximum (100th percentile), median (50th percentile), standard deviation and mean
* 10 percentile, 25 percentile, 75 percentile and 90 percentile

###### SPRATE

* Probability above 1, 2.5, 5, 10, 15, 20, 25, 30, 40, 50 and 75 kg/(m<sup>2</sup>*s)
* Minimum (0 percentile), maximum (100th percentile), median (50th percentile), standard deviation and mean
* 10 percentile, 25 percentile, 75 percentile and 90 percentile

###### TPRATE

* Probability above 1, 2.5, 5, 10, 15, 20, 25, 30, 40, 50, 75, 100 and 150 
* Minimum (0 percentile), maximum (100th percentile), median (50th percentile), standard deviation and mean
* 10 percentile, 25 percentile, 50 percentile, 75 percentile and 90 percentile

###### PRMSL

* Minimum (0 percentile), maximum (100th percentile), standard deviation and mean

###### TMP

* Probability above 243.14, 248.14, 253.14, 258.14, 263.14, 268.14, 273.14, 278.14, 283.14, 288.14, 293.14, 298.14, 303.14, 308.14 and 313.14 K
* Probability below 238.14, 243.14, 248.14, 253.14, 258.14, 263.14, 268.14, 273.14, 278.14, 283.14, 288.14, 293.14 and 298.14 K
* Minimum (0 percentile), maximum (100th percentile), median (50th percentile), standard deviation and mean
* 10 percentile, 25 percentile, 50 percentile, 75 percentile and 90 percentile

###### TCDC

* Minimum (0 percentile), maximum (100th percentile), median (50th percentile), standard deviation and mean
* 10 percentile, 25 percentile, 75 percentile and 90 percentile

###### WCF

* Probability below 223.14, 228.14, 233.14, 238.14, 243.14, 248.14, 253.14, 258.14, 263.14, 268.14 and 273.14 K
* Minimum (0 percentile), maximum (100th percentile), median (50th percentile), standard deviation and mean
* 10 percentile, 25 percentile, 75 percentile and 90 percentile

###### WIND

* Probability above 5.5556, 8.3333, 10.278, 11.111, 13.889, 17.222, 18.056, 20.833, 24.444, 25, 27.778 and 32.778 m/s
* Minimum (0 percentile), maximum (100th percentile), median (50th percentile), standard deviation and mean
* 10 percentile, 25 percentile, 75 percentile and 90 percentile

###### MUCAPE

* 25 percentile, 50 percentile and 75 percentile

###### VWSH

* 25 percentile, 50 percentile and 75 percentile

Note : An [XML list](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_geps/geps_element.xml) containing information for all variables, including descriptions and units, in both French and English is available.

## Support

If you have any questions about this data, please [contact us](https://weather.gc.ca/mainmenu/contact_us_e.html).

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).
