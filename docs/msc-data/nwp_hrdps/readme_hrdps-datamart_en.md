[En français](readme_hrdps-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [HRDPS](readme_hrdps_en.md) > HRDPS on MSC Datamart

# High Resolution Deterministic Prediction System (HRDPS) data in GRIB2 format

The [High Resolution Deterministic Prediction System or HRDPS](readme_hrdps_en.md) is a set of nested limited-area model (LAM) forecast grids from the non hydrostatic version of the Global Environmental Multiscale (GEM) model with a 2.5 km horizontal grid spacing for the inner domain over one main Pan-Canadian region and a northern region over the Arctic archipelago and Greenland. The pilot model of the HRDPS is the Regional Deterministic Prediction System or RDPS (GEM Regional model). The HRDPS is operational except the northern domain which remains experimental. The fields in the HRDPS high resolution GRIB2 dataset are made available four times a day for the Pan-Canadian domain for a 48 hour forecast period (except the northern domain).

Users who will benefit most from using these new data are those for whom a detailed forecast of surface temperatures and winds is important. Especially during the change of seasons and in wintertime when rapid changes in temperature and winds cause phase transitions of precipitation (freezing rain to snow to rain for example), 2.5 km forecasts could add much value. Also in the case of short-term forecasts in the presence of complex terrain or along shores, the influence of changes in altitude, topography and nature of the terrain will be better described for phenomena at this scale (lake or sea breezes, local valley flows, phase changes, etc.). Even over less rugged terrain, or over water away from shore, these more precise forecasts could be useful, repeatedly over a long period. As well, for hydrological forecasts on smaller basins, the HRDPS should be considered.

The HRDPS not yet being equipped with its own data assimilation system, so its quality depends largely on the RDPS, which provides initial and boundary conditions, and on the global data assimilation system acting upstream. So if the forecast of the RDPS is questionable over the region of interest, it is likely that the higher resolution forecast will magnify the problems of the regional forecast. However, initial cloud and surface data are now provided by a coupled HRDPS-Caldas (Canadian Land Data Assimilation System) cycle, improving clouds, precipitation and surface fields. For forecast lead times of more than 24 hours the use of the regional or global forecasts might be required.

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available using the HTTP protocol and resides in a directory that is plainly accessible to a web browser. Visiting that directory with an interactive browser will yield a raw listing of links, each link being a downloadable GRIB2 file. In practice, we recommend writing your own script to automate the downloading of the desired data (using wget or equivalent). If you are unsure of how to proceed, you might like to take a look at our brief wget usage guide.

The data can be accessed at the following URLs :

* https://dd.weather.gc.ca/model_hrdps/continental/grib2/HH/hhh/
* https://dd.weather.gc.ca/model_hrdps/north/grib2/HH/hhh/
* https://dd.weather.gc.ca/model_hrdps/east/grib2/HH/hhh/
* https://dd.weather.gc.ca/model_hrdps/prairies/grib2/HH/hhh/
* https://dd.weather.gc.ca/model_hrdps/west/grib2/HH/hhh/
* https://dd.weather.gc.ca/model_hrdps/maritimes/grib2/HH/hhh/

where :

* __HH__ : Model run start, in UTC [00, 06, 12, 18].
* __hhh__ : Forecast hour [000, 001, 002, ..., 024] for Maritimes and East.
* __hhh__ : Forecast hour [000, 001, 002, ..., 042] for West.
* __hhh__ : Forecast hour [000, 001, 002, ..., 048] for Continental.
* __hhh__ : Forecast hour [000, 001, 002, ..., 048] for North at 00Z and 12Z.

A 24-hour history is stored in this directory.

## Available Domains 

### Continental grid specifications

![Image de la grille du domaine continental du SHRPD](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_hrdps/grille_hrdps_cont.png)

Table lists the values of various parameters of the Continental polar-stereographic grid.

| Parameter | Value |
| ------ | ------ |
| ni | 1465 |
| nj | 825 | 
| resolution at 60° N | 2.5 km |
| coordinate of first grid point | 67.9601° N  140.7611° W |
| (i,j) coordinate of North Pole | (389.0, 842.0) |
| grid orientation (with respect to j axis) | -116.0° |

### North (experimental) grid specifications

![Image de la grille du domaine nord du SHRPD](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_hrdps/grille_hrdps_north.png)

Table lists the values of various parameters of the North polar-stereographic grid.

| Parameter | Value |
| ------ | ------ |
| ni | 765 |
| nj | 570 | 
| resolution at 60° N | 2.5 km |
| coordinate of first grid point | 38.6985° N  91.3395° W |
| (i,j) coordinate of North Pole | (450.0, 2240.0) |
| grid orientation (with respect to j axis) | -80.0° |

### East grid specifications

![Image de la grille du domaine est du SHRPD](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_hrdps/grille_hrdps_east.png)

Table lists the values of various parameters of the East polar-stereographic grid.

| Parameter | Value|
| ------ | ------ |
| ni | 765 |
| nj | 570 | 
| resolution at 60° N | 2.5 km |
| coordinate of first grid point | 38.6985° N  91.3395° W |
| (i,j) coordinate of North Pole | (450.0, 2240.0) |
| grid orientation (with respect to j axis) | -80.0° |

### Prairies grid specifications

![Image de la grille du domaine Prairies du SHRPD](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_hrdps/grille_hrdps_prairies.png)

Table lists the values of various parameters of the Prairie polar-stereographic grid.

| Parameter | Value |
| ------ | ------ |
| ni | 655 |
| nj | 570 | 
| resolution at 60° N | 2.5 km |
| coordinate of first grid point | 41.8344° N  108.4943° W |
| (i,j) coordinate of North Pole | (1015.0, 1869.0) |
| grid orientation (with respect to j axis) | -80.0° |

### West grid specifications

![Image de la grille du domaine ouest du SHRPD](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_hrdps/grille_hrdps_west.png)

Table lists the values of various parameters of the West polar-stereographic grid.

| Parameter | Value |
| ------ | ------ |
| ni | 685 |
| nj | 485 | 
| resolution at 60° N | 2.5 km |
| coordinate of first grid point | 44.6922° N  129.9011° W |
| (i,j) coordinate of North Pole | (578.0, 1900.0) |
| grid orientation (with respect to j axis) | -113.0° |


### Maritimes grid specifications

![Image de la grille du domaine Maritimes du SHRPD](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_hrdps/grille_hrdps_marit.png)

Table lists the values of various parameters of the Maritime polar-stereographic grid.

| Parameter | Value |
| ------ | ------ |
| ni | 595 |
| nj | 451 | 
| resolution at 60° N | 2.5 km |
| coordinate of first grid point | 41.2405° N  66.1830° W |
| (i,j) coordinate of North Pole | (1078.0, 1867.7) |
| grid orientation (with respect to j axis) | -36.2° |

## File name nomenclature 

NOTE: ALL HOURS ARE IN UTC.

The files have the following nomenclature :

CMC_hrdps_domain_Variable_LevelType_level_ps2.5km_YYYYMMDDHH_Phhh-mm.grib2

where :

* __CMC__ : Constant string indicating that the data is from the Canadian Meteorological Centre.
* __hrdps__ : Constant string indicating that the data is from the High Resolution Deterministic Prediction System.
* __domain__ : Constant string indicating which domain that the data is from.
* __Variable__ : Variable type included in this file.
* __LevelType__ : Level type.
* __Level__ : Level value.
* __ps2.5km__ : Constant string indicating that the projection used is polar-stereographic at 2.5 km resolution.
* __YYYYMMDD__ : Year, month and day of the beginning of the forecast.
* __HH__ : UTC run time [00, 06, 12, 18].
* __Phhh__ : P is a constant character. hhh is the forecast hour [000, 001, 002, ..., 024/030/042/048].
* __mm__ : mm are the forecast minutes [Hard-coded to 00 for now. In the future 30 minute timesteps will be available].
* __grib2__ : Constant string indicating the GRIB2 format is used.

Example of file name :

CMC_hrdps_east_DEPR_ISBL_0175_ps2.5km_2011092412_P003-00.grib2

This file originates from the Canadian Meteorological Center (CMC) and contains the data of the High Resolution Deterministic Prediction System. The data in the file start on September 24th 2011 at 12Z (2011092412). It contains the dew point depression (DEPR) at the isobaric level 175 mb (ISBL_0175) on a polar-stereographic at 2.5 km resolution (ps2.5km) for the forecast hour 03 (P003) and 00 minutes (-00) in GRIB2 format (.grib2).

## Levels

Vertical coverage of three-dimensional fields is provided by up to 28 isobaric levels.

Isobaric levels (hPa): 1015, 1000, 0985, 0970, 0950, 0925, 0900, 0850, 0800, 0750, 0700, 0650, 0600, 0550, 0500, 0450, 0400, 0350, 0300, 0275, 0250, 0225, 0200, 0175, 0150, 0100, 0050.

Some fields receive limited three-dimensional coverage of 4 levels in the vertical.

Isobaric levels (reduced coverage, hPa): 0850, 0700, 0500, 0250.

Additional levels that may be applicable to a given parameter are :

* Surface
* Fixed height above ground
* Fixed height below ground
* Thickness between two isobaric levels
* Nominal top of the atmosphere
* Entire atmospheric column

## List of variables

Warning : the tables below are not up to date (to come), some variables are missing. Feel free to [contact us](mailto:ec.dps-client.ec@canada.ca) for more information.

* [000h forecast](https://weather.gc.ca/grib/HRDPS_HR/HRDPS_nat_ps2p5km_P000_deterministic_e.html)
* [Non-zero hour forecast](https://weather.gc.ca/grib/HRDPS_HR/HRDPS_ps2p5km_PNONZERO_deterministic_e.html)

## About the No-data mask

Since October, 18th 2016, a mask called "No-data" has been added to our GRIB2 encoding process in order to better represent the areas where data are unavailable. This mask only concerns a few grid points with no data, always the same ones, located at the edge of the domain. Note that this mask has no negative effect on the product quality.

## Support

If you have any questions about these data, please contact us at : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)


## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).




















