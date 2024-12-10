[In French](readme_ohps-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_en.md) > [MSC Data](../readme_en.md) > [OHPS](readme_ohps_en.md) > OHPS on the MSC Datamart

# NetCDF data for the Operation Hydrodynamic Prediction System (OHPS)

This page describes analyses and forecasts data of the [Operation Hydrodynamic Prediction System](./readme_ohps_en.md) available in NetCDF format.

## Data address 

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../.../msc-datamart/amqp_en.md) as soon as it becomes available. An overview and examples to access and use [Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available using the HTTPS protocol and resides in a directory that is plainly accessible to a web browser. Visiting that directory with an interactive browser will yield a raw listing of links, each link being a downloadable NetCDF file.

The data can be accessed at the following address:

* [https://dd.weather.gc.ca/model_ohps/slfe/100m/{HH}/{hhh}](https://dd.weather.gc.ca/model_ohps/slfe/100m)

where :

* __HH__: Reference time, in UTC [00, 01, 02, ..., 23]
* __hhh__ : Forecast hour [000, 001, 002, ..., 048]

Analyses are hourly available in each reference time directory [00, 01, ..., 23], under the `000` forecast hour directory. Forecasts are available for each synoptic hour in model run directories [00, 06, 12, 18].

## Technical specification of the grid

![](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_ohps/grille_ohps.png)

| Parameter | Value |
| ------ | ------ |
| ni | 3600 |
| nj | 2700 | 
| resolution at 60° N | 100m |
| Angle (between 0 and 360, counter-clockwise) between the Greenwich meridian and the horizontal axis of the grid. e | 343° | 

## File name nomenclature 

Files have the following nomenclature:

* Forecasts: `{YYYYMMDD}T{HH}Z_MSC_OHPS-{DOMAIN}_{VAR}_{LVL}_{Grid}{resolution}_PT{hhh}H.nc`
* Analyses: `{YYYYMMDD}T{HH}Z_MSC_OHPS-{DOMAIN}_{VAR}_{LVL}_{Grid}{resolution}_PT0H.nc`

where :

* __YYYYMMDD__: Year, month and day of the beginning of the forecast
* __T__: Time delimiter according to ISO8601 standards
* __HH__: UTC reference time [00, 01, 02, ..., 23]
* __MSC__ : Constant character string indicating that the Canadian Meteorological Service is issuing the forecast.
* __OHPS__ : Constant string indicating that the data comes from the Operation Hydrodynamic Prediction System. 
* __DOMAIN__ : Constant string indicating the domain [SLFE, for "Saint Lawrence Fluvial Estuary"].
* __VAR__: Type of variable contained in the file
* __LVL__: Type of vertical level [Sfc for surface, DBS-Avg for mean below water surface]
* __Grid__: Horizontal grid type [PS for polar stereographic grid]
* __resolution__ : Indicates resolution [100m]
* __PT{hhh}H__: Time scale according to standard [ISO8601](https://en.wikipedia.org/wiki/ISO_8601). P, T and H are constant characters for period, time and hour. "hhh" represents the forecast hours [000, 001, 002, ..., 048].
* __PT0H__ : Constant character string indicating an analysis, based on ISO8601 standards. P, T and H are constant characters for period, time and hour.
* __nc__: Constant character string indicating NetCDF format.

File examples:

* 20230911T18Z_MSC_OHPS-SLFE_WaterLvlRiver_Sfc_PS100m_PT029H.nc
* 20230911T18Z_MSC_OHPS-SLFE_RiverVelocityY_DBS-Avg_PS100m_PT005H.nc
* 20231009T07Z_MSC_OHPS-SLFE_WaterLvlRiver_Sfc_PS100m_PT0H.nc

## Variable list

<table id="csv-table" class="display"></table>

<link href="https://cdn.jsdelivr.net/npm/simple-datatables@latest/dist/style.css" rel="stylesheet" type="text/css">
<script src="https://cdn.jsdelivr.net/npm/simple-datatables@latest"></script>
<script src="../../../js/variables_datatable.js" type="text/javascript"></script>
<script>
  loadTable("csv-table", "../../../assets/csv/OHPS_Variables-List_en.csv");
</script>

## Support

If you have any questions about this data, please [contact us](https://weather.gc.ca/mainmenu/contact_us_e.html)

## dd_info mailing list announcements 

Announcements related to this dataset are available via the [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/) list.
