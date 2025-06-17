[En français](readme_hrdps-north-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [HRDPS-North](readme_hrdps-north_en.md) > HRDPS-North on MSC Datamart

# GRIB2 data from the High Resolution Deterministic Prediction System North (HRDPS-North)

This page describes all the data from the experimental [High Resolution Deterministic Prediction System North (HRDPS-North)](readme_hrdps-north_en.md) available in GRIB2 format on a rotated lat-lon grid at 3km resolution over an extended domain.

## Data address 

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as it becomes available. An [overview and examples to access and use Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available using the HTTPS protocol and resides in a directory that is plainly accessible to a web browser. Visiting that directory with an interactive browser will yield a raw listing of links, each link being a downloadable GRIB2 file.

The data can be accessed at the following URLs:

* [https://dd.weather.gc.ca/model_hrdps/north/3km/{HH}/{hhh}/](https://dd.weather.gc.ca/model_hrdps/north/3km/)

where :

* __HH__: UTC run time [00, 12] 
* __hhh__ : Forecast hour [000, 001, 002, ..., 048]

Note: Some weather elements on the grid algorithms ("WEonG") require variable values at `t-1`, so in order to standardize data supply, forecast times start at 001h.

## Technical specification of the grid 

![Rotated lat-lon grid image of HRDPS's northern domain](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_hrdps-north/grilleRLatLon_hrdps-north.png)

Values given to rotated lat-lon grid parameters at 3km resolution:

| Parameter | Value |
| ------ | ------ |
| ni | 2230 |
| nj | 1830 | 
| resolution at 60° N | 3 km |
| coordinates of first grid point | 0°N ; 97°W |

__Note__ : The [most recent versions of wgrib2](https://www.cpc.ncep.noaa.gov/products/wesley/wgrib2/update_2.0.8.html) and [GDAL](https://gdal.org/) support these rotated grids. 

## Nomenclature of file names

Files have the following nomenclature:

* `{YYYYMMDD}T{HH}Z_MSC_HRDPS-North_{VAR}_{LVLTYPE-LVL}_{Grid}{resolution}_PT{hhh}H.grib2`
* `{YYYYMMDD}T{HH}Z_MSC_HRDPS-North-WEonG_{VAR}_{LVLTYPE-LVL}_{Grid}{resolution}_PT{hhh}H.grib2`

where :

* __YYYYMMDD__ : Year, month and day of the beginning of the forecast
* __T__: Time delimiter according to ISO8601 standards
* __HH__: UTC run time [00, 12]
* __Z__: Time zone (UTC time)
* __MSC__: Constant string for Meteorological Service of Canada, the data source
* __HRDPS-North__: Constant string indicating that the data come from the High Resolution Deterministic Prediction System North
* __HRDPS-WEonG__: Constant character string indicating that the data originates from the weather elements on the grid ("WEonG") of the High Resolution Deterministic Prediction System North
* __VAR__: Type of variable contained in the file (e.g. UGRD)
* __LVLTYPE-LVL__ : Vertical level and height [ex: Sfc for the surface, EATM for the integral of the column, DBS-10-20cm layer between 10 and 20cm below the surface, AGL-10m for the height of 10m above ground]
* __Grid__ : Horizontal grid [RLatLon]
* __resolution__ : 0.03. Means a resolution of 0.03° (approx. 3km) in longitudinal and latitudinal directions
* __PT{hhh}H__: Timing according to [ISO8601](https://en.wikipedia.org/wiki/ISO_8601). P, T and H are constant characters for Period, Time and Hour. "hhh" represents the forecast time [000, 001, 002, ..., 048].
* __grib2__: Constant character string indicating that the format is GRIB2.

Examples of file names:

* 20231210T00Z_MSC_HRDPS-North_GUST_AGL-10m_RLatLon0.03_PT012H.grib2
* 20231211T12Z_MSC_HRDPS-North-WEonG_VISIFG_Sfc_RLatLon0.03_PT024H.grib2

## Variable list

This list contains both the parameters generated from HRDPS-North outputs and the weather elements on the grid (*HRDPS-WEonG*) calculated in post-processing. 

<table id="csv-table" class="display"></table>

<link href="https://cdn.jsdelivr.net/npm/simple-datatables@latest/dist/style.css" rel="stylesheet" type="text/css">
<script src="https://cdn.jsdelivr.net/npm/simple-datatables@latest"></script>
<script src="../../../js/variables_datatable.js" type="text/javascript"></script>
<script>
  loadTable("csv-table", "../../../assets/csv/HRDPS-North_Variables-List_en.csv");
</script>

## Support

If you have any questions about this data, please [contact us](https://meteo.gc.ca/mainmenu/contact_us_f.html).

## dd_info mailing list announcements 

Announcements related to this dataset are available via the [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/) list.
















