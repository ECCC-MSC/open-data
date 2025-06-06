[In French](readme_caps-weong-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [CAPS](readme_caps_en.md) > CAPS Weather Elements on the Grid on MSC Datamart

# Experimental GRIB2 Weather Elements on the Grid data based on the Canadian Arctic Prediction System (CAPS)

As part of a larger modernization plan for the Meteorological Service of Canada (MSC), [Weather Elements on the Grid](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_weong-hrdps_e.pdf) ("WEonG") based on the Canadian Arctic Prediction System (CAPS), amalgaming numerical and post-processed data using various diagnostic approaches are available to serve different forecasting  programs (public, marine, aviation, air quality, etc.). Hourly concepts are thus produced from different algorithms using outputs from the CAPS. This data is available on the system's rotated lat-lon grid.

## Data Address

MSC testing data repository DD-Alpha data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as it becomes available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available using the HTTP protocol and resides in a directory that is plainly accessible to a web browser. Visiting that directory with an interactive browser will yield a raw listing of links, each link being a downloadable GRIB2 file.

The rotated lat-lon grid data can be accessed at the following address: 

[https://dd.alpha.meteo.gc.ca/model_caps/3km/{HH}/{hhh}/](https://dd.alpha.meteo.gc.ca/model_caps/3km/)

where :

* __HH__: Model run start, in UTC [00, 12]
* __hhh__ : Forecast hour [001, 002, 003, ..., 048]

A 24-hour history is kept in this directory.

Note: Some algorithms require variable values at `t-1`, in order to standardize the data supply, the forecast times start at 001h.

## Technical specification of the grid

![Rotated lat-lon grid of the CAPS domain](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_hrdps-north/grilleRLatLon_hrdps-north.png)

Values given to the parameters of the rotated lat-lon grid:

| Parameter | Value |
| ------ | ------ |
| ni | 1102 |
| nj | 1076 | 
| resolution at 60° N | 10km |
| coordinates of first grid point | 48.5° S; 62.6° W | 

## Nomenclature of file names 

The files have the following nomenclature:

`{YYYYMMDD}T{HH}Z_MSC_CAPS-WEonG_{VAR}_{LVLTYPE-LVL}_{Grid}{resolution}_PT{hhh}H.grib2`

where:

* __YYYYMMDD__ : Year, month and day of the beginning of the forecast
* __T__: Time delimiter according to ISO8601 standards
* __HH__: UTC run time [00, 12] 
* __Z__: Time zone (UTC hour)
* __MSC__: Constant string for Meteorological Service of Canada, the data source
* __CAPS-WEonG__ : Constant string indicating that the data are from the Canadian Arctic Prediction System weather elements on the grid ("WEonG")
* __VAR__ : Variables contained in the files (ex: AirTemp).
* __LVLTYPE-LVL__ : Vertical level [Sfc for the surface]
* __Grid__ : Horizontal grid [RLatLon]
* __resolution__ : 0.03. Means a resolution of 0.03° (about 3km) in the longitudinal and latitudinal directions
* __PT{hhh}H__ : Time delay according to the standard [ISO8601](https://en.wikipedia.org/wiki/ISO_8601). P, T and H are constant characters designating Period, Time and Hour. "hhh" represents the forecast time [001, 002, 003, ..., 048]
* __grib2__: Constant string indicating that the format is GRIB2.

Example of file name:

* 20250602T12Z_MSC_CAPS-WEonG_BlowingSnow-Prob_Sfc_RLatLon0.03_PT006H.grib2

## List of variables

List of surface weather elements on the grid:

<table id="csv-table" class="display"></table>

<link href="https://cdn.jsdelivr.net/npm/simple-datatables@latest/dist/style.css" rel="stylesheet" type="text/css">
<script src="https://cdn.jsdelivr.net/npm/simple-datatables@latest"></script>
<script src="../../../js/variables_datatable.js" type="text/javascript"></script>
<script>
  loadTable("csv-table", "../../../assets/csv/RDPS-WEonG_Variables-List_en.csv");
</script>

## Support

If you have any questions regarding this data, please [contact us](https://meteo.gc.ca/mainmenu/contact_us_e.html).

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available via the [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/) list.

