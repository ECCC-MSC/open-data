[In French](readme_caldas-nsrps-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC Open Data](../readme_en.md) > [CaLDAS-NSRPS](readme_caldas-nsrps_en.md) > CaLDAS-NSRPS on MSC Datamart 

# The Canadian Land Data Assimilation System in the National Surface and River Prediction System (CaLDAS-NSRPS) data in NetCDF format

This page describes the [The Canadian Land Data Assimilation System](./readme_caldas-nsrps_en.md) data available in NetCDF format on the MSC Datamart.

## Data location 

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available using the HTTPS protocol and resides in a directory that is plainly accessible to a web browser. Visiting that directory with an interactive browser will yield a raw listing of links, each link being a downloadable NetCDF file.

The data can be accessed at the following URLs:

* [https://dd.weather.gc.ca/model_nsrps-caldas/2.5km/{HH}/](https://dd.weather.gc.ca/model_nsrps-caldas/2.5km)                  

where:

* __HH__ : Analysis validity time, in UTC [00, 03, 06, 09, 12, 15, 18, 21]

## Technical specification of the grid

![Image of the CaLDAS-NSRPS domain](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_caldas-nsrps/grille_caldas-nsrps.png)

The table below lists the values of the rotated latitude-longitude grid parameters:

| Parameter | Value |
| ------ | ------ |
| ni | _2578_ |
| nj | _1328_ |
| resolution along the rotated equator | 2.5km |

## Filename nomenclature

The files have the following nomenclature: 

`{YYYYMMDD}T{HH}Z_MSC_NSRPS-CaLDAS_{VAR}_{LVLTYPE}-{LVL}_{grid}{resolution}_PT0H.nc`

where:

* __YYYYMMDD__: Year, month and day of the beginning of the forecast
* __T__ : Time delimiter according to ISO8601 norms
* __HH__: Analysis validity time, in UTC [00, 03, 06, 09, 12, 15, 18, 21]
* __Z__ : Time zone (UTC hour)
* __MSC__ : Constant string indicating that the data is from the Meteorologcal Service of Canada (MSC)
* __NSRPS-CaLDAS__ : Constant string indicating that the data is from The Canadian Land Data Assimilation System in the National Surface and River Prediction SystemThe Canadian Land Data Assimilation System
* __VAR__ : Variables included in the file (see section below).
* __LVLTYPE__ : Vertical level type [Sfc for the surface, DBS for depth below the surface, AGL for fixed height above ground]
* __LVL__ :  Vertical level value [`1.5m`; `all` includes all levels `0.025m, 0.075m, 0.15m, 0.3m, 0.7m, 1.5m, 2.5m`]. This parameter is not available for the surface. 
* __grid__ : Horizontal grid [RLatLon]
* __resolution__ : Resolution in degree 0.0225 (about 2.5km) in both latitude and longitude directions 
* __PT0H__: Forecast hours based on [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) norms. P, T and H are constant character designating Period, Time and Hour. Here, PTOH indicates an analysis.
* __nc__ : constant string indicating the NetCDF format

Examples:

* 20220307T00Z_MSC_NSRPS-CaLDAS_AirTemp_AGL-1.5m_RLatLon0.0225_PT0H.nc
* 20220307T00Z_MSC_NSRPS-CaLDAS_Dewpoint_AGL-1.5m_RLatLon0.0225_PT0H.nc
* 20220307T00Z_MSC_NSRPS-CaLDAS_RadiativeTemp_Sfc_RLatLon0.0225_PT0H.nc
* 20220307T00Z_MSC_NSRPS-CaLDAS_SoilLiquidWaterCont_DBS-all_RLatLon0.0225_PT0H.nc
* 20230220T00Z_MSC_NSRPS-CaLDAS_SnowDepth_Sfc_RLatLon0.0225_PT0H.nc
* 20230220T00Z_MSC_NSRPS-CaLDAS_SnowWaterEquiv_Sfc_RLatLon0.0225_PT0H.nc

Note: The soil moisture content in each layer corresponds to the average value, typically referenced at the midpoint of the respective layer

## List of variables 

List of variables available in the files:

<table id="csv-table" class="display"></table>

<link href="https://cdn.jsdelivr.net/npm/simple-datatables@latest/dist/style.css" rel="stylesheet" type="text/css">
<script src="https://cdn.jsdelivr.net/npm/simple-datatables@latest"></script>
<script src="../../../js/variables_datatable.js" type="text/javascript"></script>
<script>
  loadTable("csv-table", "../../../assets/csv/NSRPS_Variables-List_en.csv");
</script>

## Support

If you have any questions about this data, please [contact us](https://weather.gc.ca/mainmenu/contact_us_e.html).

## Announcements from the dd_info mailing list

Announcements related to this dataset are available in the [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).

