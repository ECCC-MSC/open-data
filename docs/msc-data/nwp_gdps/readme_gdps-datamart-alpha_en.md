[In French](readme_gdps-datamart-alpha_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [SGPD](readme_gdps_en.md) > GDPS Weather Elements on the Grid on DD-Alpha

# Experimental GRIB2 Weather Elements on the Grid data based on the Global Deterministic Prediction System (GDPS)

For nearly three decades, the [SCRIBE system](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/product-pages/alpha_glb_scrib_scribe-documentation_gen_e.html) has been used to assist meteorologists in preparing weather reports. The philosophy behind SCRIBE is that a set of weather element matrices are generated for selected stations or sample points and then transmitted to regional weather centers. The matrices are then decoded by SCRIBE and can be modified via the graphical interface by the users. The resulting data is then provided to a text generator, which produces bilingual public forecasts in plain language.

The various rules related to the Scribe matrices hinder scientific innovation, do not exploit the richness of the Numerical Weather Prediction (NWP), reduce the understanding of weather forecasts, and and may require frequent interventions from forecasters.

As part of a larger modernization plan for the Meteorological Service of Canada (MSC), in which the role of the forecaster is evolving, the goal is to replace the Scribe matrices, [available on the MSC Datamart](https://dd.meteo.gc.ca/model_gem_regional/matrices/land_regions/), and their limited number of points across Canada with [Weather Elements on the Grid](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_weong-hrdps_e.pdf) ("WEonG").

Weather Elements on Grid (WEonG) based on the Global Deterministic Prediction System (GDPS) is a post-processing system designed to compute the weather elements required by different forecast programs (public, marine, aviation, air quality, etc.). This system amalgamates numerical and post-processed data using various diagnostic approaches. Hourly concepts are produced from different algorithms using outputs from the [Global Deterministic Prediction System (GDPS)](readme_gdps_en.md).

## Data Address 

MSC testing data repository DD-Alpha data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as it becomes available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available using the HTTP protocol and resides in a directory that is plainly accessible to a web browser. Visiting that directory with an interactive browser will yield a raw listing of links, each link being a downloadable GRIB2 file.

The rotated lat-lon grid data can be accessed at the following address: 

[https://dd.alpha.meteo.gc.ca/model_gem_global/15km/{HH}/{hhh}/](https://dd.alpha.meteo.gc.ca/model_gem_global/15km/)

where :

* __HH__ : Model run start, in UTC [00, 12]
* __hhh__ : Forecast hour [001, 002, 003, ..., 084, 087, 090, ..., 141, 144]

A 24-hour history is kept in this directory.

Note: Some algorithms require variable values at `t-1`, in order to standardize the data supply, the forecast times start at 001h.

## Technical specification of the grid

Values given to the parameters of the lat-lon grid:

| Parameter | Value |
| ------ | ------ |
| ni | 2400 |
| nj | 1201 | 
| resolution at 60° N | 15km |
| coordinates of first grid point | 90° S; 180° W | 

## Nomenclature of file names 

The files have the following nomenclature:

`{YYYYMMDD}T{HH}Z_MSC_GDPS-WEonG_{VAR}_{LVLTYPE-LVL}_{Grid}{resolution}_PT{hhh}H.grib2`

where:

* __YYYYMMDD__ : Year, month and day of the beginning of the forecast
* __T__: Time delimiter according to ISO8601 standards
* __HH__: UTC run time [00, 06, 12, 18] 
* __Z__: Time zone (UTC hour)
* __MSC__: Constant string for Meteorological Service of Canada, the data source
* __GDPS-WEonG__ : Constant string indicating that the data are from the Global Deterministic Prediction System weather elements on the grid ("WEonG")
* __VAR__ : Variables contained in the files (ex: VISIFG).
* __LVLTYPE-LVL__ : Vertical level [Sfc for the surface]
* __Grid__ : Horizontal grid [LatLon]
* __resolution__ : 0.15. Means a resolution of 0.15° (about 15km) in the longitudinal and latitudinal directions
* __PT{hhh}H__ : Time delay according to the standard [ISO8601](https://en.wikipedia.org/wiki/ISO_8601). P, T and H are constant characters designating Period, Time and Hour. "hhh" represents the forecast time [001, 002, 003, ..., 084, 087, 090, ..., 141, 144]
* __grib2__: Constant string indicating that the format is GRIB2.

Example file name:

* 20220821T12Z_MSC_GDPS-WEonG_BLSN_Sfc_LatLon0.15_PT024H.grib2

## List of variables

List of surface weather elements on the grid:

<table id="csv-table" class="display"></table>

<link href="https://cdn.jsdelivr.net/npm/simple-datatables@latest/dist/style.css" rel="stylesheet" type="text/css">
<script src="https://cdn.jsdelivr.net/npm/simple-datatables@latest"></script>
<script src="../../../js/variables_datatable.js" type="text/javascript"></script>
<script>
  loadTable("csv-table", "../../../assets/csv/GDPS-WEonG_Variables-List_en.csv");
</script>

## Support

If you have any questions regarding this data, please [contact us](https://meteo.gc.ca/mainmenu/contact_us_e.html).

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available via the [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/) list.
