[En français](readme_hrdps-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [HRDPS](readme_hrdps_en.md) > HRDPS on MSC Datamart

# High Resolution Deterministic Prediction System (HRDPS) data in GRIB2 format

The operationnal [High Resolution Deterministic Prediction System or HRDPS](readme_hrdps_en.md) is a set of nested limited-area model (LAM) forecast grids from the non-hydrostatic version of the Global Environmental Multiscale (GEM) model with a 2.5 km horizontal grid spacing over one main Pan-Canadian region. The pilot model of the HRDPS is the Regional Deterministic Prediction System or RDPS (GEM Regional model). The fields in the HRDPS high resolution GRIB2 dataset are made available four times a day for the Pan-Canadian domain for a 48 hour forecast period.

Users who will benefit most from using these data are those for whom a detailed forecast of surface temperatures and winds is important. Especially during the change of seasons and in wintertime when rapid changes in temperature and winds cause phase transitions of precipitation (freezing rain to snow to rain for example), 2.5 km forecasts could add much value. Also in the case of short-term forecasts in the presence of complex terrain or along shores, the influence of changes in altitude, topography and nature of the terrain will be better described for phenomena at this scale (lake or sea breezes, local valley flows, phase changes, etc.). Even over less rugged terrain, or over water away from shore, these more precise forecasts could be useful, repeatedly over a long period. As well, for hydrological forecasts on smaller basins, the HRDPS should be considered.

As part of a modernization plan of the Meteorological Service of Canada (MSC), coherent [weather elements on the grid](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_weong-hrdps_e.pdf) ("WEonG"), merging raw model outputs and post-processed with various diagnostic approaches, are also available to serve the different forecasting programs (public, marine, aviation, air quality, etc.).  Hourly concepts are produced from different algorithms using outputs from the pan-Canadian HRDPS. These data are available on a lat-lon rotated grid. 

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available using the HTTPS protocol and resides in a directory that is plainly accessible to a web browser. Visiting that directory with an interactive browser will yield a raw listing of links, each link being a downloadable GRIB2 file.

The data can be accessed at the following URLs:

* [https://dd.weather.gc.ca/model_hrdps/continental/{res}/{HH}/{hhh}/](https://dd.weather.gc.ca/model_hrdps/continental)

where :

* __res__ : Horizontal resolution [2.5km]
* __HH__ : Model run start, in UTC [00, 06, 12, 18]
* __hhh__ : Forecast hour [000, 001, 002, ..., 048]

A 24-hour history is stored in this directory.

Note: Some weather element of the grid algorithms ("WEonG") need variable values at `t-1`, in order to standardize the data supply, the forecast times start at 001h.

## Technical grid specification

![Image de la grille du domaine continental lat-lon tournée du SHRPD](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_hrdps/grille_hrdps_Rlatlon.png)

Table lists the values of various parameters of the rotated lat-lon continental grid.

| Parameter | Valeur |
| ------ | ------ |
| ni | 2540 |
| nj | 1290 | 
| resolution at 60° N | 2.5 km |
| coordinate of the first grid point | 12°S 15°W |

__Note__ : The [most recent versions of wgrib2](https://www.cpc.ncep.noaa.gov/products/wesley/wgrib2/update_2.0.8.html) and [GDAL](https://gdal.org/) support these rotated grids.

## File name nomenclature 

The files have the following nomenclature :

* `{YYYYMMDD}T{HH}Z_MSC_HRDPS_{VAR}_{LVLTYPE-LVL}_{Grid}{resolution}_PT{hhh}H.grib2`
* `{YYYYMMDD}T{HH}Z_MSC_HRDPS-WEonG_{VAR}{LVLTYPE-LVL}{Grid}{resolution}_PT{hhh}H.grib2`

where :

* __YYYYMMDD__ : Year, month and day of the beginning of the forecast
* __T__ : Time delimiter according to ISO8601 norms
* __HH__ : UTC run time [00, 06, 12, 18]
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
* 20220821T12Z_MSC_HRDPS-WEonG_VISIFG_Sfc_RLatLon0.0225_PT024H.grib2

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

This list contains both the parameters generated from HRDPS outputs and the weather elements on the grid (*HRDPS-WEonG*) calculated in post-processing.

<table id="csv-table" class="display"></table>

<link href="https://cdn.jsdelivr.net/npm/simple-datatables@latest/dist/style.css" rel="stylesheet" type="text/css">
<script src="https://cdn.jsdelivr.net/npm/simple-datatables@latest"></script>
<script src="../../../js/variables_datatable.js" type="text/javascript"></script>
<script>
  loadTable("csv-table", "../../../assets/csv/HRDPS_Variables-List_en.csv");
</script>

## Support

If you have any questions about this data, please [contact us](https://www.weather.gc.ca/mainmenu/contact_us_e.html).

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).




















