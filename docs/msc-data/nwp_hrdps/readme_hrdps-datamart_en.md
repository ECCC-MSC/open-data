[En français](readme_hrdps-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [HRDPS](readme_hrdps_en.md) > HRDPS on MSC Datamart

# High Resolution Deterministic Prediction System (HRDPS) data in GRIB2 format

The [High Resolution Deterministic Prediction System or HRDPS](readme_hrdps_en.md) is a set of nested limited-area model (LAM) forecast grids from the non-hydrostatic version of the Global Environmental Multiscale (GEM) model with a 2.5 km horizontal grid spacing for the inner domain over one main Pan-Canadian region and a northern region over the Arctic archipelago and Greenland. The pilot model of the HRDPS is the Regional Deterministic Prediction System or RDPS (GEM Regional model). The HRDPS is operational except the northern domain which remains experimental. The fields in the HRDPS high resolution GRIB2 dataset are made available four times a day for the Pan-Canadian domain for a 48 hour forecast period (except the northern domain).

Users who will benefit most from using these data are those for whom a detailed forecast of surface temperatures and winds is important. Especially during the change of seasons and in wintertime when rapid changes in temperature and winds cause phase transitions of precipitation (freezing rain to snow to rain for example), 2.5 km forecasts could add much value. Also in the case of short-term forecasts in the presence of complex terrain or along shores, the influence of changes in altitude, topography and nature of the terrain will be better described for phenomena at this scale (lake or sea breezes, local valley flows, phase changes, etc.). Even over less rugged terrain, or over water away from shore, these more precise forecasts could be useful, repeatedly over a long period. As well, for hydrological forecasts on smaller basins, the HRDPS should be considered.

As part of a modernization plan of the Meteorological Service of Canada (MSC), coherent [weather elements on the grid](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_weong-hrdps_e.pdf) ("WEonG"), merging raw model outputs and post-processed with various diagnostic approaches, are also available to serve the different forecasting programs (public, marine, aviation, air quality, etc.).  Hourly concepts are produced from different algorithms using outputs from the pan-Canadian HRDPS. These data are available on a lat-lon rotated grid. 

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available using the HTTPS protocol and resides in a directory that is plainly accessible to a web browser. Visiting that directory with an interactive browser will yield a raw listing of links, each link being a downloadable GRIB2 file.

The data can be accessed at the following URLs:

* Continental domain: [https://dd.weather.gc.ca/model_hrdps/continental/{HH}/{hhh}/](https://dd.weather.gc.ca/model_hrdps/continental)
* North domain (experimental): [https://dd.weather.gc.ca/model_hrdps/north/grib2/{HH}/{hhh}/](https://dd.weather.gc.ca/model_hrdps/north/grib2)

where :

* __res__ : Horizontal resolution [2.5km]
* __HH__ : Model run start, in UTC [00, 06, 12, 18], except the North domain [00, 12]
* __hhh__ : Forecast hour [000, 001, 002, ..., 048]

A 24-hour history is stored in this directory.

Note: Some weather element of the grid algorithms ("WEonG") need variable values at `t-1`, in order to standardize the data supply, the forecast times start at 001h.

## Technical grids specification

* __Rotated lat-lon grid of the continental domain__

![Image de la grille du domaine continental lat-lon tournée du SHRPD](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_hrdps/grille_hrdps_Rlatlon.png)

Table lists the values of various parameters of the rotated lat-lon continental grid.

| Parameter | Valeur |
| ------ | ------ |
| ni | 2540 |
| nj | 1290 | 
| resolution at 60° N | 2.5 km |
| coordinate of the first grid point | 12°S 15°W |

__Note__ : The [most recent versions of wgrib2](https://www.cpc.ncep.noaa.gov/products/wesley/wgrib2/update_2.0.8.html) and [GDAL](https://gdal.org/) support these rotated grids.

* __Polar-stereographic grid of the North domain (experimental)__

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

## File name nomenclature 

* __Continental domain__

The files have the following nomenclature :

* `{YYYYMMDD}T{HH}Z_MSC_HRDPS_{VAR}_{LVLTYPE-LVL}_{Grid}{resolution}_PT{hhh}H.grib2`
* `{YYYYMMDD}T{HH}Z_MSC_HRDPS-WEonG_{VAR}{LVLTYPE-LVL}{Grid}{resolution}_PT{hhh}H.grib2`

where :

* __YYYYMMDD__ : Year, month and day of the beginning of the forecast
* __T__ : Time delimiter according to ISO8601 norms
* __HH__ : UTC run time [00, 12]
* __Z__ : Time zone (UTC hour)
* __MSC__ : Constant string indicating the Meteorological Service of Canada, source of data
* __HRDPS__ : Constant string indicating that the data is from the High Resolution Deterministic Prediction System
* __HRDPS-WEonG__ : Constant string indicating that the data is from the weather elements on the grid of the High Resolution Deterministic Prediction System
* __VAR__ : Variable type included in the file (ex: UGRD)
* __LVLTYPE-LVL__ : Vertical level type and level value [ex: Sfc for surface, EATM for the entire atmospheric column, DBS-10-20cm layer between 10 and 20cm under surface, AGL-10m for 10m above ground level]
* __Grid__ : Horizontal grid [RLatLon]
* __resolution__ : 0.0225. Indicating resolution in degree [0.0225°(environ 2.5km)] in latitude and longitude directions
* __PT{hhh}H__ : Forecast hours based on [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) norms. P, T and H are constant character designating Period, Time and Hour. "hhh" is the forecast hour [000, 001, 002, ..., 048]
* __grib2__ : Constant string indicating the GRIB2 format is used

Examples of filenames : 

* 20201123T00Z_MSC_HRDPS_GUST_AGL-10m_RLatLon0.0225_PT012H.grib2
* 20220821T12Z_MSC_HRDPS-WEonG_VISIFOG_Sfc_RLatLon0.0225_PT024H.grib2

* __North domain (experimental)__

The files have the following nomenclature :

* `CMC_hrdps_north_{VAR}_{LVLTYPE-LVL}_{Grid}{resolution}_{YYYYMMDDHH}_P{hhh}-{mm}.grib2`

where :

* __CMC__ : Constant string indicating that the data is from the Canadian Meteorological Centre
* __hrdps__ : Constant string indicating that the data is from the High Resolution Deterministic Prediction System
* __north__ : Constant string indicating the North domain
* __VAR__ : Variable type included in this file (ex. : UGRD)
* __LVLTYPE-LVL__ : Level type and level value [ex: SFC for the surface, TGL_120 for the height of 120m above ground level]
* __Grid__ : Horizontal grid [ps for polar stereographic]
* __resolution__ : 2.5 km resolution
* __YYYYMMDD__ : Year, month and day of the beginning of the forecast
* __HH__ : UTC run time [00, 12]
* __P{hhh}__ : P is a constant character. hhh is the forecast hour [000, 001, 002, ..., 048]
* __mm__ : mm are the forecast minutes [Hard-coded to 00 for now. In the future 30 minute timesteps will be available]
* __grib2__ : Constant string indicating the GRIB2 format is used

Example of file name :

* CMC_hrdps_north_DEPR_ISBL_0175_ps2.5km_2021092412_P003-00.grib2

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

Warning : the tables below are not up to date (to come), some variables are missing. Feel free to [contact us](https://www.weather.gc.ca/mainmenu/contact_us_e.html) for more information.

* [000h forecast](https://weather.gc.ca/grib/HRDPS_HR/HRDPS_nat_ps2p5km_P000_deterministic_e.html)
* [Non-zero hour forecast](https://weather.gc.ca/grib/HRDPS_HR/HRDPS_ps2p5km_PNONZERO_deterministic_e.html)

List of weather elements on the grid (*HRDPS-WEonG*):

| GRIB2 parameter abreviation | Description | Unity  |
|------------------------|-------------|----------|
| BSNOW | Presence of blowing snow | binary (0/1) |
| CFRZR | Probability of freezing rain	| %|
| CICEP | Probability of ice pellets | %|
| CONDARAIN | Conditional amount of liquid precipitation | m |
| CONDASNOW | Conditional amount of solid snow | m |
| CONDICEP | Conditional amount of solide ice pellets | m |
| CP |	Character of precipitation | 0=none; 1=showers; 2=intermittent; 3=continuous |
| CRAIN | Probability of rain | % |
| CSNOW | Probability of snow | % |
| DIST | Model orography |m |
| DPT |	Dew point temperature |	C |
| DPTYPE | Dominant precipitation type | 101=rain; 110=hail; 111=drizzle; 203=freezing rain; 212=freezing drizzle; 308=ice pellets; 405=snow; 409=snow pellets; 413=ice crystals; 414=snow grains |
| FZPRATE | Conditional freezing precipitation amount | m |
| GUST | Gust | m/s |
| HSNOWL | Height of snow level | m |
| LAND | Water/land mask | fraction |
| PARAIN | Probability of liquid precipitation | % |
| PBSNOW | Probability of blowing snow | % |
| PDZ |	Probability of drizzle |	% |
| PFRDZ | Probability of freezing drizzle | % |
| PFRZR | Probability of freezing precipitation | % |
| POP |	Probability of precipitation | % |
| PRATE | Conditional precipitation rate | m |
| PSNOWS | Probability of snow squalls  |	% |
| PTYPE | Instantaneous precipitation type | 1=rain; 2=rain/snow; 3=freezing rain; 4=ice pellets; 5=snow; 6=none; 7=drizzle; 8=freezing drizzlee; 9=freezing rain/ice pellets  |
| SCNDPTYPE | Secondary precipitation type | 101=rain; 110=hail; 111=drizzle; 203=freezing rain; 212=freezing drizzle; 308=ice pellets; 405=snow; 409=snow pellets; 413=ice crystals; 414=snow grains |
| SK | day/night sky state (combined cloud cover and opacity)  | 0-1=sunny/clear; 2-3=mainly sunny/cloudy periods; 4-5-6=mix of sun and clouds/partly cloudy; 7-8=mainly cloudy/mainly cloudy; 9=cloudy/cloudy; 10=cloudy/overcast |
| TMP |	Temperature | C |
| TPII | Total precipitation intensity index | 0=no intensity; 1=light; 2=moderate; 3=heavy	|
| TSTM | Probability of thunderstorm occurence | % |
| VISIFOG | Visibility through ice fog | m |
| VISLFOG | Visibility through liquid fog | m |
| WDIR | Wind direction | True degree |
| WIND | Wind speed | m/s |

## Support

If you have any questions about this data, please [contact us](https://www.weather.gc.ca/mainmenu/contact_us_e.html).

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).




















