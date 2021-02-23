[En français](readme_astro-rdps-datamart-alpha_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC Open Data](../readme_en.md) > [RDPS](readme_rdps_en.md) > Astronomy products on DD-Alpha based on RDPS

# Astronomy products based on the Regional Deterministic Prediction System (RDPS) in GRIB2 format

This page describes [seeing](https://meteo.gc.ca/astro/seeing_e.html) and [transparency](https://meteo.gc.ca/astro/transparence_e.html) prediction data. Seing is used in astronomy to describe the state of atmospheric turbulence while transparency refers to the clarity of the sky and is measured as the ability to observe stars according to their brightness or magnitude. 

These data are generated from the [Regional Deterministic Prediction System](./readme_rdps_en.md) respectively every 3 hours and hourly up to 84 hours and projected on a polar-stereographic grid at 35km resolution.

They will allow amateur and professional astronomers, but also any user interested in sky conditions, to better plan their activities.

## Data location 

MSC testing data repository DD-Alpha data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available using the HTTPS protocol and resides in a directory that is plainly accessible to a web browser. Visiting that directory with an interactive browser will yield a raw listing of links, each link being a downloadable GRIB2 file.

The data can be accessed at the following URL: 

[https://dd.alpha.meteo.gc.ca/model_gem_regional/astronomy/grib2/{HH}](https://dd.alpha.meteo.gc.ca/model_gem_regional/astronomy/grib2)

where :

* __HH__: Model run start, in UTC [00, 06, 12, 18]

A 24-hour history is kept in this directory.

## Technical specification of the grid

![Image de la grille PS astro-SRPD](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_rdps/grille_rdps-astro_PS.png)

Values given to the parameters of the polar-stereographic grid :

| Parameter | Value |
| ------ | ------ |
| ni | 245 |
| nj | 190 | 
| resolution at 60° N | 35 km |
| coordinates of the first grid point | 20.10° N ; 136.48° W | 
| grid orientation (with respect to j axis) | -111.0° |

## Filename nomenclature 

NOTE : ALL HOURS ARE IN UTC.

The files have the following nomenclature :

```
{YYYYMMDD}T{HH}Z_MSC_RDPS_{VAR}_EATM_{Grille}{resolution}_PT{hh}H.grib2
```

where :

* __YYYYMMDD__ : Year, month and day of the beginning of the forecast
* __T__ : Time delimiter according to [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) norms
* __HH__ : UTC run time [00, 06, 12, 18]
* __Z__ : Time zone (UTC hour)
* __MSC__ : Constant string indicating the Meteorological Service of Canada, source of data
* __RDPS__ : Constant string indicating that data is based on the Regional Deterministic Prediction System (RDPS)
* __VAR__ : Variable included in the file [SEEI, TRSP]
* __EATM__ : Entire atmosphere. Considered as a single layer
* __Grille__ : Horizontal grid [PS]
* __resolution__ : Horizontal resolution [35km]
* __PT{h}H__ : Forecast hours based on [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) norms. « h » is the forecast hour [0, 1, 2, ..., 84]
* __grib2__ : Constant string indicating the GRIB2 format is used

Example of file name : 

20210208T00Z_MSC_RDPS_SEEI_EATM_PS35km_PT84H.grib2

## List of variables

The forecasted variables available in the 2D files are described below.

* __SEEI__: seeing index. Qualifies the level of turbulence and the stability of the atmosphere that influences the resolution of celestial objects (ex. planets)
* __TRSP__: transparency index. Qualifies the depth of the sky according to the composition of the atmosphere

## Support

If you have any questions about this data, please contact us at: [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).




