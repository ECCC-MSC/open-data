[En français](readme_rdps-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC Open Data](../readme_en.md) > [RDPS](readme_rdps_en.md) > RDPS on MSC Datamart

# Regional Deterministic Prediction System (RDPS) data in GRIB2 format

Under the Regional Deterministic Prediction System (RDPS), the numerical weather prediction model is run on a variable-step grid with a 10 km central core resolution. The fields in the 10 km resolution regional GRIB2 dataset are made available on a 935 x 824 polar-stereographic grid covering North America and adjacent waters with a 10 km resolution at 60°N.

## Data location 

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available using the HTTP protocol and resides in a directory that is plainly accessible to a web browser. Visiting that directory with an interactive browser will yield a raw listing of links, each link being a downloadable GRIB2 file.

The data can be accessed at the following URLs: 

* [https://dd.weather.gc.ca/model_gem_regional/10km/grib2/{HH}/{hhh}/](https://dd.weather.gc.ca/model_gem_regional/10km/grib2)

where :

* __HH__: Model run start, in UTC [00, 06, 12, 18]
* __hhh__: Forecast hour [000, 001, 002,..., 048] at 00Z, 12Z and [000, 001, 002,..., 053, 054] at 06Z and 18Z 

A 20-hour history is kept in this directory.

## Technical specification of the grid

![Image de la grille du Système régional de prévision déterministe](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_rdps/grille_rdps-srpd.png)

Values given to the parameters of the stereographic polar grid :

| Parameter | Value |
| ------ | ------ |
| ni | 935 |
| nj | 824 | 
| resolution at 60° N | 10 km |
| coordinates of the first grid point | 18.1429° N  142.8968° W | 
| (i,j) coordinate of North Pole | (456.2; 732.4) |
| grid orientation (with respect to j axis) | -111.0° |

There is also a pre-formatted [ASCII file containing the geographical coordinates](https://meteo.gc.ca/grib/10km_res.bz2) of each grid point. 

## Filename nomenclature 

Note : all hours are in UTC.

The files have the following nomenclature :

CMC_reg_Variable_LevelType_level_ps10km_YYYYMMDDHH_Phhh.grib2

where :

* __CMC__ : constant string indicating that the data is from the Canadian Meteorological Centre
* __reg__ : constant string indicating that the data is from the RDPS
* __Variable__ : Variable type included in this file. To consult a complete list, refer to the variables section.
* __LevelType__ : Level type. To consult a complete list, refer to the variables section.
* __Level__ : Level value. To consult a complete list, refer to the variables section.
* __ps10km__ : constant string indicating that the projection used is polar-stereographic at 10km resolution.
* __YYYYMMDD__ : Year, month and day of the beginning of the forecast.
* __HH__ : UTC run time [00, 06, 12, 18]
* __Phhh__ : P is a constant character. hhh is the forecast hour [000,001,002,...,048] at 00Z and 12Z and up to 54h at 06Z and 18Z
* __grib2__ : constant string indicating the GRIB2 format is used

Example of file name : 

CMC_reg_DEPR_ISBL_1015_ps10km_2010091306_P027.grib2

This file originates from the Canadian Meteorological Center (CMC) and contains the data of the RDPS. The data in the file start on September 13th 2010 at 06Z (2010091306). It contains the dew point depression (DEPR) at the isobaric level 1015 mb (ISBL_1015) on a polar-stereographic at 10km resolution (ps10km) for the forecast hour 27 (P027) in GRIB2 format (.grib2).

## Levels

Vertical coverage of three-dimensional fields is provided by up to 28 isobaric levels.

Isobaric levels (hPa): 1015, 1000, 985, 970, 950, 925, 900, 850, 800, 750, 700, 650, 600, 550, 500, 450, 400, 350, 300, 275, 250, 225, 200, 175, 150, 100, 50.

Some fields receive limited three-dimensional coverage of 4 levels in the vertical.

Isobaric levels (reduced coverage, hPa): 850, 700, 500, 250.

Additional levels that may be applicable to a given parameter are :

* Surface
* Fixed height above ground
* Fixed height below ground
* Thickness between two isobaric levels
* Nominal top of the atmosphere
* Entire atmospheric column

## List of variables

Warning : the tables below are not up to date (to come), some variables are missing. Feel free to [contact us](mailto:ec.dps-client.ec@canada.ca) for more information.

* [0h forecast](https://weather.gc.ca/grib/REG_HR/REGIONAL_ps10km_P000_deterministic_e.html)
* [Non-zero hour forecast](https://weather.gc.ca/grib/REG_HR/REGIONAL_ps10km_PNONZERO_deterministic_e.html)

Notes :

* u (UGRD) and v (VGRD) components of the wind vector are to be resolved relative to the defined grid, in the direction of increasing i and j coordinates. Please refer to Code Table 7 of the GRIB standard for further details.
* Radiation fluxes parameters NLWRS_SFC, DSWRF_NTAT, and DLWRF_NTAT are encoded as accumulated values, as per value 4 of the Time Range Indicator (Code Table 5 of the GRIB format standard). This changes the unit from Watts per square metre to Joules per square meter.
* Specific Humidity (SPFH) is the model's native moisture variable. It should be used in all NWP applications. Dew point depression (DEPR) is a diagnostic parameter and is not meant for use in high-precision applications.

## About the no-data mask

Since September, 7th 2016, a mask called "No-data" has been added to our GRIB2 encoding process in order to better represent the areas where data are unavailable. This mask only concerns a few grid points with no data, always the same ones, located at the edge of the domain. Note that this mask has no negative effect on the product quality.

## Support

If you have any questions about these data, please contact us at: [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).




