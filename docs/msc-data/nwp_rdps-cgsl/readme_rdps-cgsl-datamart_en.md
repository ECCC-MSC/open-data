[En français](readme_rdps-cgsl-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [Atmosphere-Ocean-Ice forecast system for the Gulf of St. Lawrence](readme_rdps-cgsl_en.md) > Atmosphere-Ocean-Ice forecast system for the Gulf of St. Lawrence on MSC Datamart

# Atmosphere-Ocean-Ice forecast system for the Gulf of St. Lawrence data in GRIB2 format

This page describes the [Atmosphere-Ocean-Ice forecast system for the Gulf of St. Lawrence](readme_rdps-cgsl_en.md) data available in GRIB2 format.

## Data address 

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available using the HTTP protocol and resides in a directory that is plainly accessible to a web browser. Visiting that directory with an interactive browser will yield a raw listing of links, each link being a downloadable GRIB2 file.

The data can be accessed at the following URLs :

* [https://dd.weather.gc.ca/model_gem_regional/coupled/gulf_st-lawrence/grib2/{HH}/{hhh}](https://dd.weather.gc.ca/model_gem_regional/coupled/gulf_st-lawrence/grib2)

__where__ :

* __HH__ : Model run start, in UTC [00, 06, 12, 18]
* __hhh__ : Forecast hour [001, 002, 003, ..., 048]

A 24-hour history is stored in this directory.

## Technical specification of the grid

![](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_rdps-cgsl/grille_rdwps-gsl.png)

Table lists the values of various parameters of latitude-longtitude grid :

| Parameter | Value |
| ------ | ------ |
| ni | 500 |
| nj | 325 | 
| resolution | 0.02° x 0.03° |
| coordinate of first grid point | 45° 30' N  71° W |

## Data specifications 

The fields in the GRIB2 data set for the two components of the system are made available on a latitude-longitude grid of 500 x 325 (with 0.02 x 0.03 degrees of resolution). The list of fields made available in GRIB2 format are :

|Variable |  Description                                                     | System      |
|---------|------------------------------------------------------------------|-------------|
|UGRD     |Zonal component of wind at diagnostic (surface) level [m/s]       | Atmospheric |
|VGRD     |Meridional component of wind at diagnostic (surface) level [m/s]  | Atmospheric |
|TMP      |Sea surface temperature (between 0 and 5m)  [Kelvin]              | Oceanic     |
|ICEC     |Ice fraction                                                      | Oceanic     |
|ICETK    |Ice thickness (averaged over model grid cell) [m]                 | Oceanic     |
|UICE     |Zonal component of Ice speed vector [m/s]                         | Oceanic     |
|VICE     |Meridional component of Ice speed vector [m/s]                    | Oceanic     |
|UOGRD    |Zonal component of the surface ocean current [m/s]                | Oceanic     |
|VOGRD    |Meridional component of the surface ocean current [m/s]           | Oceanic     |
|WTMP     |Sea surface temperature [Kelvin]                                  | Oceanic     |
|ICET     |Ice surface temperature [Kelvin]                                  | Oceanic     |
|ICEPRS   |Vertically integrated ice internal pressure (or stress) [N/m or Pa x m] | Oceanic |
|ICESTG   |Vertically integrated compressive ice strength [N/m or Pa x m]    | Oceanic     |

## File name nomenclature 

NOTE : ALL HOURS ARE IN UTC.

The files have the following nomenclature :

* __File name for the atmospheric data__ : CMC_coupled-rdps-stlawrence-atmosphere_latlon0.02x0.03_AAAAMMJJHH_P0hh.grib2
* __File name for the oceanic data__ : CMC_coupled-rdps-stlawrence-ocean_latlon0.02x0.03_AAAAMMJJHH_P0hh.grib2

where :

* __CMC__ : Constant string indicating that the data is from the Canadian Meteorological Centre.
* __coupled-rdps-stlawrence-ocean__ : Constant string indicating that the data is from the Atmosphere-Ocean-Ice forecast system for the Gulf of St. Lawrence.
* __latlon0.02x0.03__ : Constant string indicating that the projection used is latitude-longitude grid of 500 x 325 (with 0.02 x 0.03 degrees of resolution).
* __YYYYMMDD__ : Year (YYYY), month (MM) and day (DD) of the beginning of the forecast.
* __HH__ : UTC run time [00, 06, 12, 18].
* __Phhh__ : "P" is a constant character. "hhh" is the forecast hour [001, 002, 003, ..., 048].
* __grib2__ : Constant string indicating the GRIB2 format is used.

Example of file name :

* __Atmospheric data__ : CMC_coupled-rdps-stlawrence-atmosphere_latlon0.02x0.03_2015011200_P048.grib2
* __Oceanic data__ : CMC_coupled-rdps-stlawrence-ocean_latlon0.02x0.03_2015011200_P048.grib2

These files originate from the Canadian Meteorological Center (CMC) and contain the data of the Atmosphere-Ocean-Ice forecast system for the Gulf of St. Lawrence using a latitude-longitude grid of 500 x 325 (with 0.02 x 0.03 degrees of resolution). The forecast has been produced on January 12th 2015 at 00Z (2015011200) and contains the 48 hour forecast (P048) in GRIB2 format (.grib2).

## Levels

These variables are only available for the surface level. 

## List of variables

Warning: the tables below are not up to date (to come), some variables are missing. Feel free to [contact us](mailto:ec.dps-client.ec@canada.ca) for more information.

* [Atmospheric component](https://weather.gc.ca/grib/GF_COUPLED/GULF-ST-LAWRENCE-ATMOSPHERE_latlon0.02x0.03_NONZERO_coupled_e.html)
* [Oceanic component](https://weather.gc.ca/grib/GF_COUPLED/GULF-ST-LAWRENCE-OCEAN_latlon0.02x0.03_NONZERO_coupled_e.html)

## Support

If you have any questions about this data, please contact us at : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).
