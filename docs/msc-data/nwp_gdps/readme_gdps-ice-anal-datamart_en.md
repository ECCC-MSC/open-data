[En français](readme_gdps-ice-anal-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [GDPS](readme_gdps_en.md) > GDPS on MSC Datamart

# Global ice analysis data in NetCDF format

Environment and Climate Change Canada provides global sea-ice analysis fields produced by its operational [Global Deterministic Prediction System (GDPS)](readme_gdps_en.md) and interpolated to a rotated latitude-longitude grid with 0.09 x 0.09 degree resolution.
The data files are in NetCDF format (NetCDF-4 classic model) and comply with the Climate and Forecast Conventions.
 
The Global Sea-Ice Analysis System is an analysis system based on 3D-Var assimilation covering all waters (ocean and lakes) at a 10km horizontal resolution on a YIN-YANG grid and using a 6 hours persistence forecast for the background state. This analysis assimilates 4 times a day satellite remote sensing data and [Canadian Ice Service](https://www.canada.ca/en/environment-climate-change/services/ice-forecasts-observations/latest-conditions.html) ice charts. 

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available via the HTTPS protocol. It is possible to access it with a standard browser. In this case, we obtain a list of links giving access to a NetCDF file.

The data can be accessed at the following address :

[https://dd.weather.gc.ca/model_gem_global/{RES}/{HH}](https://dd.weather.gc.ca/model_gem_global/10km)

where :

* __RES__ : Horizontal resolution [10km]
* __HH__ : UTC time of the beginning of the model run [00, 06, 12, 18]

A one week history is kept in this directory.

## Technical specification of the grid

Values given to the various parameters of the latitude-longitude grid according to the resolution.

| Parameter | Value |
| ------ | ------ |
| ni | 4000 |
| nj | 2000 | 
| resolution | 0.09° x 0.09° |

## File name nomenclature 

NOTE: ALL HOURS ARE IN UTC.

The files have the following nomenclature:

```
{YYYYMMDD}T{HH}Z_MSC_GDPS-Analysis_{VAR}_{LVLTYPE-LVL}_{Grille}{resolution}_PT{hhh}H.nc
```

where :

* __YYYYMMDD__ : Year, month, and day of the beginning of the forecast
* __T__ : Time delimiter according to ISO8601 norms
* __HH__ : UTC run time [00, 12]
* __Z__ : Time zone (UTC hour)
* __MSC__ : Constant string indicating the Meteorological Service of Canada, source of data
* __GDPS-Analysis__ : Constant string indicating that the data is from the Global Deterministic Prediction System ice analysis
* __VAR__ : Variables included in the file [IICECONC]. See variables section below
* __LVLTYPE-LVL__ : Vertical level type and level value [SFC]
* __Grille__ : Horizontal grid [RLatLon]
* __resolution__ : 0.09. Indicating resolution in degrees [0.09°(about 10km)] for latitude and longitude directions
* __PT{hhh}H__ : Forecast hours based on [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) norms. P, T and H are constant character designating Period, Time and Hour. "hhh" is the forecast hour [000 for analysis] 
* __nc__ : Constant string indicating that NetCDF format is used

Example of filename :  20210111T00Z_MSC_GDPS-Analysis_IICECONC_SFC_RLatLon0.09x0.09_PT000H.nc

## List of variables

The table below provides a short description of the parameter, the level available and measurement unit, available in NetDCF format.

<table id="csv-table" class="display"></table>

<link href="https://cdn.jsdelivr.net/npm/simple-datatables@latest/dist/style.css" rel="stylesheet" type="text/css">
<script src="https://cdn.jsdelivr.net/npm/simple-datatables@latest"></script>
<script src="../../../js/variables_datatable.js" type="text/javascript"></script>
<script>
  loadTable("csv-table", "../../../assets/csv/GDPS-Ice-Analysis_en.csv");
</script>

## Support

If you have any questions about this data, please contact us at : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info.comm.collab.science.gc.ca/).

