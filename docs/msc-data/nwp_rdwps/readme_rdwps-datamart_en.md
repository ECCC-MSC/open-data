[En français](readme_rdwps-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [RDWPS](readme_rdwps_en.md) > RDWPS on MSC Datamart

# Regional Deterministic Wave Prediction System (RDWPS) Data in GRIB2 Format

This page describes the data of the [Regional Deterministic Wave Prediction System](readme_rdwps_en.md).

## Great Lakes

The [Regional Deterministic Wave Prediction System (RDWPS)](readme_rdwps_en.md) produces wave forecasts for the Great Lakes using the third generation spectral wave model WaveWatch III®. The model is forced by the 10 meters winds from the High Resolution Deterministic Prediction System (HRDPS). A sea ice analysis is used by the model to dampen or suppress wave growth in areas covered respectively with 25% to 75% and more than 75% ice.

The WW3 (Tolman and the WAVEWATCH III® Development Group 2014) is a third generation spectral wave prediction model that solves the evolution of the energy balance equation for the 2-D wave energy spectrum without any prior assumptions on the shape of the spectrum. The WW3 model has been implemented by a growing number of national operational forecasting centers over the last several years. 

This system includes four domains:

* Lake Superior
* Lake Huron-Michigan
* Lake Erie
* Lake Ontario

All four domains have a spatial resolution of 1 km (0.0090 deg x 0.0124 deg).

## Gulf of Saint Lawrence

The [Regional Deterministic Wave Prediction System (RDWPS)](readme_rdwps_en.md) produces wave forecasts for the Gulf of Saint Lawrence using the third generation spectral wave model WAM. The model is forced by the 10 meters winds from the Regional Deterministic Prediction System. In addition, an analysis of sea ice is used by the model to suppress wave growth in areas covered with greater than 50% ice.

WAM (WAve Model) (WAMDI Group 1988, Komen et al. 1994) is a third generation spectral wave prediction model that solves the evolution of the energy balance equation for the 2-D wave energy spectrum without any prior assumptions on the shape of the spectrum. The WAM model has been operational in the international community since the early nineties after a long period of development under the WAMDIG (WAve Model Development and Implementation Group).

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available using the HTTP protocol and resides in a directory that is plainly accessible to a web browser. Visiting that directory with an interactive browser will yield a raw listing of links, each link being a downloadable GRIB2 file. In practice, we recommend writing your own script to automate the downloading of the desired data (using wget or equivalent). If you are unsure of how to proceed, you might like to take a look at our brief wget usage guide.

The data can be accessed at the following URLs :

* https://dd.weather.gc.ca/model_wave/great_lakes/erie/grib2/HH/
* https://dd.weather.gc.ca/model_wave/great_lakes/huron-michigan/grib2/HH/
* https://dd.weather.gc.ca/model_wave/great_lakes/ontario/grib2/HH/
* https://dd.weather.gc.ca/model_wave/great_lakes/superior/grib2/HH/
* https://dd.weather.gc.ca/model_wave/ocean/gulf-st-lawrence/grib2/HH/

where :

* __HH__ : Model run start, in UTC [00, 06, 12, 18]

A 24-hour history is stored in this directory.

## Available Domains 

### Lake Superior

![](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_rdwps/grille_rdwps_sup.png)

Table lists the values of various parameters of the Lake Superior :

| Parameter | Value |
| ------ | ------ |
| ni | 658 |
| nj | 318 | 
| resolution | 0.0090° x 0.0124° |
| coordinate of first grid point | 46.2590° N  92.3116° O |

### Lake Huron and Michigan

![](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_rdwps/grille_rdwps_hum.png)

Table lists the values of various parameters of the Lake Huron and Michigan :

| Parameter | Value |
| ------ | ------ |
| ni | 698 |
| nj | 573 | 
| resolution | 0.0090° x 0.0124° |
| coordinate of first grid point | 41.4260° N  88.1452° O |

### Lake Erie

![](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_rdwps/grille_rdwps_erie.png)

Table lists the values of various parameters of the Lake Erie :

| Parameter | Value |
| ------ | ------ |
| ni | 398 |
| nj | 210 | 
| resolution | 0.0090° x 0.0124° |
| coordinate of first grid point | 41.2190° N  83.6068° O |

### Lake Ontario

![](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_rdwps/grille_rdwps_ont.png)

Table lists the values of various parameters of the Lake Ontario :

| Parameter | Value |
| ------ | ------ |
| ni | 348 |
| nj | 158 | 
| resolution | 0.0090° x 0.0124° |
| coordinate of first grid point | 43.0640° N  79.9736° O |

### Gulf of St Lawrence

![](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_rdwps/grille_rdwps-gsl.png)

Table lists the values of various parameters of the Gulf of St Lawrence :

| Parameter | Value |
| ------ | ------ |
| ni | 331 |
| nj | 160 | 
| resolution | 0.05° x 0.05° |
| coordinate of first grid point | 44.075° N  70.925° O |

## File name nomenclature 

NOTE: ALL HOURS ARE IN UTC.

The files have the following nomenclature :

CMC_rdwps_domain_Variable_LevelType_level_latlondddxddd_YYYYMMDDHH_Phhh.grib2

where :

* __CMC__ : Constant string indicating that the data is from the Canadian Meteorological Centre
* __rdwps__ : Constant string indicating that the data is from the Regional Deterministic Wave Prediction System
* __domain__ : Constant string indicating which domain that the data is from
* __Variable__ : Variable type included in this file.
* __LevelType__ : Level type.
* __Level__ : Level value.
* __latlondddxddd__ : Constant string indicating that the projection used is lat/long at ddd x ddd degrees resolution
* __YYYYMMDD__ : Year, month and day of the beginning of the forecast.
* __HH__ : UTC run time [00, 06, 12, 18]
* __Phhh__ : P is a constant character. hhh is the forecast hour [000, 001, 002, ..., 048]
* __grib2__ : Constant string indicating the GRIB2 format is used

Example of file name :

CMC_rdwps_lake-ontario_HTSGW_SFC_0_latlon0.0090x0.0124_2012032106_P042.grib2

This file originates from the Canadian Meteorological Center (CMC) and contains the data of the Regional Deterministic Wave Prediction System. The data in the file start on March 21th 2012 at 06Z (2012032106). It contains the significant wave height (HTSGW) for Lake Ontario at the surface (SFC_0) on a lat/long grid at 0.0090 degree x 0.0124 degree resolution for the forecast hour 042 (P042) in GRIB2 format (.grib2).

## Levels

Levels that may be applicable to a given parameter are :

* Surface
* Fixed height above ground
* Mean sea level

## List of variables

|GRIB2 |  Short description            |              Abbr. | Level | Units |
|------|-------------------------------|--------------------|-------|-------|
|10/2/0|  Ice cover                    |              ICEC  | SFC_0 | fraction |
|0/2/2 |  U-Component of Wind          |              UGRD  | TGL_10| m/s |
|0/2/3 |  V-Component of Wind          |              VGRD  | TGL_10| m/s |
|10/0/3|  Significant height of combined wind waves and swell|       HTSGW | SFC_0 | m |
|10/0/34 | Peak wave period            |               PWPER | SFC_0 | s |
|10/0/28 | Mean zero-crossing wave period  |           MZWPER| SFC_0 | s |
|10/0/4 | Direction of wind waves      |              WVDIR | SFC_0 | degrees true |
|10/0/5 | Significant height of wind waves  |         WVHGT | SFC_0 | m |
|10/0/6 | Mean period of wind waves         |         WVPER | SFC_0 | s |
|10/0/7 | Direction of primary swell        |         SWDIR | SFC_0 | degrees true |
|10/0/8 | Significant height of primary swell |       SWELL | SFC_0 | m |
|10/0/9 | Peak period of primary swell        |       SWPER | SFC_0 | s |

## Support

If you have any questions about these data, please contact us at : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).
