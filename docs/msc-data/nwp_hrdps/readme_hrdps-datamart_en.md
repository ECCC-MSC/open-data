[En français](readme_hrdps-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [HRDPS](readme_hrdps_en.md) > HRDPS on MSC Datamart

# High Resolution Deterministic Prediction System (HRDPS) data in GRIB2 format

The [High Resolution Deterministic Prediction System or HRDPS](readme_hrdps_en.md) is a set of nested limited-area model (LAM) forecast grids from the non hydrostatic version of the Global Environmental Multiscale (GEM) model with a 2.5 km horizontal grid spacing for the inner domain over one main Pan-Canadian region and a northern region over the Arctic archipelago and Greenland. The pilot model of the HRDPS is the Regional Deterministic Prediction System or RDPS (GEM Regional model). The HRDPS is operational except the northern domain which remains experimental. The fields in the HRDPS high resolution GRIB2 dataset are made available four times a day for the Pan-Canadian domain for a 48 hour forecast period (except the northern domain).

Users who will benefit most from using these new data are those for whom a detailed forecast of surface temperatures and winds is important. Especially during the change of seasons and in wintertime when rapid changes in temperature and winds cause phase transitions of precipitation (freezing rain to snow to rain for example), 2.5 km forecasts could add much value. Also in the case of short-term forecasts in the presence of complex terrain or along shores, the influence of changes in altitude, topography and nature of the terrain will be better described for phenomena at this scale (lake or sea breezes, local valley flows, phase changes, etc.). Even over less rugged terrain, or over water away from shore, these more precise forecasts could be useful, repeatedly over a long period. As well, for hydrological forecasts on smaller basins, the HRDPS should be considered.

The HRDPS not yet being equipped with its own data assimilation system, so its quality depends largely on the RDPS, which provides initial and boundary conditions, and on the global data assimilation system acting upstream. So if the forecast of the RDPS is questionable over the region of interest, it is likely that the higher resolution forecast will magnify the problems of the regional forecast. However, initial cloud and surface data are now provided by a coupled HRDPS-Caldas (Canadian Land Data Assimilation System) cycle, improving clouds, precipitation and surface fields. For forecast lead times of more than 24 hours the use of the regional or global forecasts might be required.

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available using the HTTPS protocol and resides in a directory that is plainly accessible to a web browser. Visiting that directory with an interactive browser will yield a raw listing of links, each link being a downloadable GRIB2 file.

The data can be accessed at the following URLs:

* Polar-stereographic grids: [https://dd.weather.gc.ca/model_hrdps/{domain}/grib2/{HH}/{hhh}/](https://dd.weather.gc.ca/model_hrdps)
* Rotated lat-lon grid: [https://dd.weather.gc.ca/model_hrdps/continental/{res}/grib2/{HH}/{hhh}/](https://dd.weather.gc.ca/model_hrdps/continental/2.5km/grib2)

where :

* __domain__ : Constant string indicating the available domain [continental, north, east, prairies, west, maritimes]
* __res__ : Horizontal resolution [2.5km]
* __HH__ : Model run start, in UTC [00, 06, 12, 18], except the North domain [00, 12]
* __hhh__ : Forecast hour [000, 001, 002, ..., 048] 

A 24-hour history is stored in this directory.

## Available Domains 

### Continental grids specifications

* __Polar-stereographic grid__

![Image de la grille du domaine continental du SHRPD](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_hrdps/grille_hrdps_cont.png)

Table lists the values of various parameters of the Continental polar-stereographic grid.

| Parameter | Value |
| ------ | ------ |
| ni | 2576 |
| nj | 1456 | 
| resolution at 60° N | 2.5 km |
| coordinate of first grid point | 35.6073° N  128.0813° W |
| (i,j) coordinate of North Pole | (840.0, 2296.0) |
| grid orientation (with respect to j axis) | -108.0° |

* __Rotated lat-lon grid__

![Image de la grille du domaine continental lat-lon tournée du SHRPD](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_hrdps/grille_hrdps_Rlatlon.png)

Table lists the values of various parameters of the rotated lat-lon Continental grid.

| Parameter | Valeur |
| ------ | ------ |
| ni | 2540 |
| nj | 1290 | 
| resolution at 60° N | 2.5 km |
| coordinate of the first grid point | 12°S 15°W |

__Note__ : The [most recent versions of wgrib2](https://www.cpc.ncep.noaa.gov/products/wesley/wgrib2/update_2.0.8.html) and [GDAL](https://gdal.org/) support these rotated grids.

### North (experimental) grid specifications

![Image de la grille du domaine nord du SHRPD](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_hrdps/grille_hrdps_north.png)

Table lists the values of various parameters of the North polar-stereographic grid.

| Parameter | Value |
| ------ | ------ |
| ni | 1465 |
| nj | 825 | 
| resolution at 60° N | 2.5 km |
| coordinate of first grid point | 67.9601° N  140.7611° W |
| (i,j) coordinate of North Pole | (389.0, 842.0) |
| grid orientation (with respect to j axis) | -116.0° |

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

### Polar-stereographic grid

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

### Rotated lat-lon grid

The files have the following nomenclature :

{YYYYMMDD}T{HH}Z_MSC_HRDPS_{VAR}_{LVLTYPE-LVL}_{Grille}{resolution}_P{hhh}.grib2

where :

* __YYYYMMDD__ : Year, month and day of the beginning of the forecast
* __T__ : Time delimiter according to ISO8601 norms
* __HH__ : UTC run time [00, 12]
* __Z__ : Time zone (UTC hour)
* __MSC__ : Constant string indicating the Meteorological Service of Canada, source of data
* __HRDPS__ : Constant string indicating that the data is from the High Resolution Deterministic Prediction System
* __VAR__ : Variable type included in the file (ex: UGRD)
* __LVLTYPE-LVL__ : Vertical level type and level value [ex: SFC for surface, EATM for the entire atmospheric column, DBS-10-20cm layer between 10 and 20cm under surface]
* __Grille__ : Horizontal grid [RLatLon]
* __resolution__ : 0.0225. Indicating resolution in degree [0.0225°(environ 2.5km)] in latitude and longitude directions
* __P{hhh}__ : « P »  is a constant character, « hhh » is the forecast hour [000, 001, 002, ..., 024/030/042/048]
* __grib2__ : Constant string indicating the GRIB2 format is used

Example of filename : 

20201123T00Z_MSC_HRDPS_GUST_AGL-10m_RLatLon0.0225_P012.grib2

This file has been produced by the MSC and contains the data of the High Resolution Deterministic Prediction System. It contains wind gust (GUST) at 10m above ground (AGL-10m), on a 2.5km (0.0225) resolution rotated lat-lon grid. The forecast starts on November 23th at 00Z (20201123T00Z) and contains forecast hour 12 (P012) in GRIB2 format (grib2).

## Levels

Vertical coverage of three-dimensional fields is provided by up to 31 isobaric levels.

Isobaric levels (hPa): 1015, 1000, 985, 970, 950, 925, 900, 850, 800, 750, 700, 650, 600, 550, 500, 450, 400, 350, 300, 275, 250, 225, 200, 175, 150, 100, 50.

Additional levels 30, 20 and 10 hPa for the variables TMP, HGT, UGRD, VGRD, WIND, WDIR, SPFH, RH and DEPR.

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

## About the no-data mask for the Continental polar-stereographic grid

Since October, 18th 2016, a mask called "No-data" has been added to our GRIB2 encoding process in order to better represent the areas where data are unavailable. This mask only concerns a few grid points with no data, always the same ones, located at the edge of the domain. Note that this mask has no negative effect on the product quality.

## Support

If you have any questions about this data, please contact us at: [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).




















