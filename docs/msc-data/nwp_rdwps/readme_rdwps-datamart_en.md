[En français](readme_rdwps-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [RDWPS](readme_rdwps_en.md) > RDWPS on MSC Datamart

# Regional Deterministic Wave Prediction System (RDWPS) Data in GRIB2 Format

This page describes the data of the [Regional Deterministic Wave Prediction System](readme_rdwps_en.md) data available in GRIB2 format.

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available using the HTTPS protocol and resides in a directory that is plainly accessible to a web browser. Visiting that directory with an interactive browser will yield a raw listing of links, each link being a downloadable GRIB2 file.

The data can be accessed at the following URLs :

* [https://dd.weather.gc.ca/model_wave/great_lakes/erie/grib2/{HH}/](https://dd.weather.gc.ca/model_wave/great_lakes/erie/grib2)
* [https://dd.weather.gc.ca/model_wave/great_lakes/huron-michigan/grib2/{HH}/](https://dd.weather.gc.ca/model_wave/great_lakes/huron-michigan/grib2)
* [https://dd.weather.gc.ca/model_wave/great_lakes/ontario/grib2/{HH}/](https://dd.weather.gc.ca/model_wave/great_lakes/ontario/grib2)
* [https://dd.weather.gc.ca/model_wave/great_lakes/superior/grib2/{HH}/](https://dd.weather.gc.ca/model_wave/great_lakes/superior/grib2)
* [https://dd.weather.gc.ca/model_wave/ocean/gulf-st-lawrence/grib2/{HH}/](https://dd.weather.gc.ca/model_wave/ocean/gulf-st-lawrence/grib2)

where :

* __HH__ : Model run start, in UTC [00, 06, 12, 18]

A 24-hour history is stored in this directory.

## Available Domains

### Lake Superior

![](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_rdwps/grille_rdwps_sup.png)

| Parameter | Value |
| ------ | ------ |
| ni | 658 |
| nj | 318 | 
| resolution | 0.0090° x 0.0124° |
| coordinate of first grid point | 46.2590° N  92.3116° W |

### Lake Huron and Michigan

![](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_rdwps/grille_rdwps_hum.png)

| Parameter | Value |
| ------ | ------ |
| ni | 698 |
| nj | 573 | 
| resolution | 0.0090° x 0.0124° |
| coordinate of first grid point | 41.4260° N  88.1452° W |

### Lake Erie

![](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_rdwps/grille_rdwps_erie.png)

| Parameter | Value |
| ------ | ------ |
| ni | 398 |
| nj | 210 | 
| resolution | 0.0090° x 0.0124° |
| coordinate of first grid point | 41.2190° N  83.6068° W |

### Lake Ontario

![](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_rdwps/grille_rdwps_ont.png)

| Parameter | Value |
| ------ | ------ |
| ni | 348 |
| nj | 158 | 
| resolution | 0.0090° x 0.0124° |
| coordinate of first grid point | 43.0640° N  79.9736° W |

### Gulf of St Lawrence

![](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_rdwps/grille_rdwps-gsl.png)

| Parameter | Value |
| ------ | ------ |
| ni | 331 |
| nj | 160 | 
| resolution | 0.05° x 0.05° |
| coordinate of first grid point | 44.075° N  70.925° W |

## File name nomenclature 

NOTE: ALL HOURS ARE IN UTC.

The files have the following nomenclature :

CMC_rdwps_DOMAIN_VAR_LVL_LVLVAL_{grille}{resolution}_YYYYMMDDHH_P{hhh}.grib2

where :

* __CMC__ : Constant string indicating that the data is from the Canadian Meteorological Centre
* __rdwps__ : Constant string indicating that the data is from the Regional Deterministic Wave Prediction System
* __DOMAIN__ : String indicating which domain the data is from
* __VAR__ : Variable type included in this file.
* __LVL__ : Level type.
* __LVLVAL__ : Level value.
* __grille__ : Horizontal grid type [latlon]
* __resolution__ : Indicating resolution in degreee in latitude and longitude direction [e.g.: 0090x0.0124]
* __YYYYMMDD__ : Year, month and day of the beginning of the forecast.
* __HH__ : UTC run time [00, 06, 12, 18]
* __Phhh__ : P is a constant character. hhh is the forecast hour [000, 001, 002, ..., 048]
* __grib2__ : Constant string indicating the GRIB2 format is used

Example of file name :

CMC_rdwps_lake-ontario_HTSGW_SFC_0_latlon0.0090x0.0124_2012032106_P042.grib2

This file originates from the Canadian Meteorological Center (CMC) and contains the data of the Regional Deterministic Wave Prediction System. The data in the file start on March 21th 2012 at 06Z (2012032106). It contains the significant wave height (HTSGW) for Lake Ontario at the surface (SFC_0) on a lat/long grid at 0.0090 degree x 0.0124 degree resolution for the forecast hour 042 (P042) in GRIB2 format (.grib2).

## Levels

Levels that may be applicable to a given parameter are :

* Surface [SFC]
* Fixed height above ground [TGL]
* Mean sea level [MSL]

## List of variables

This table provides, for each GRIB2 parameter number: a short description, an alphabetical abbreviation, the levels available for the parameter, and measurement units.

|GRIB2 discipline/category/parameter number | Parameter description |	Abbreviation |	Level |	Units |
|------|-------------------------------|--------------------|-------|-------|
|10/2/0|  Ice cover                    |              ICEC  | SFC_0 | fraction |
|0/2/2 |  U-Component of Wind          |              UGRD  | TGL_10| m/s |
|0/2/3 |  V-Component of Wind          |              VGRD  | TGL_10| m/s |
|0/3/1 |  Pressure Reduced to MSL      |             PRMSL  | MSL_0 | Pa  |
|10/0/3|  Significant height of combined wind waves and swell|       HTSGW | SFC_0 | m |
|10/0/34 | Peak wave period            |               PWPER | SFC_0 | s |
|10/0/28 | Mean zero-crossing wave period  |           MZWPER| SFC_0 | s |
|10/0/4 | Direction of wind waves      |              WVDIR | SFC_0 | degrees true |
|10/0/5 | Significant height of wind waves  |         WVHGT | SFC_0 | m |
|10/0/6 | Mean period of wind waves         |         WVPER | SFC_0 | s |
|10/0/7 | Direction of primary swell        |         SWDIR | SFC_0 | degrees true |
|10/0/8 | Significant height of primary swell |       SWELL | SFC_0 | m |
|10/0/9 | Peak period of primary swell        |       SWPER | SFC_0 | s |

### Notes

* u and v components of the wind vector are to be resolved relative to the defined grid, in the direction of increasing i and j coordinates.

* Gulf of St Lawrence peak wave period: file name is labelled with __VAR__ PKPER and __LVL__ TGL.

* Pressure Reduced to MSL is available only for the Gulf of Saint Lawrence.

* Mean zero-crossing wave period is available only for the Great Lakes.

* Swell parameters for the Gulf of Saint Lawrence refer to the total swell.

* Swell parameters for the Great Lakes refer to the primary swell. At each point of the domain, the spectra can be divided between wind sea and a certain number of swells. The two swells that contain the most energy are designated in order as the primary and secondary swell. Wind, sea and swell parameters can be undefined at some grid points, for the former if there is little wind, for the latter if there are only locally generated waves.

## Support

If you have any questions about this data, please contact us at : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).
