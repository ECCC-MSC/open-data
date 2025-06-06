[En français](readme_riops-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [RIOPS](readme_riops_en.md) > RIOPS data in NetCDF 

# Regional Ice Ocean Prediction System (RIOPS) Data in NetCDF Format

The Canadian Centre for Meteorological and Environmental Prediction (CCMEP) provides instantaneous forecasts of sea ice and ocean fields produced by its operational Regional Ice-Ocean Prediction System (RIOPS) and interpolated to a grid in north-polar stereographic projection with 5 km resolution at the standard parallel 60°N. 

The data files are in NetCDF format (NetCDF-4 classic model) and comply with the Climate and Forecast Conventions. 

RIOPS is based on the NEMO-CICE ice-ocean model and produces regional sea ice and ocean analyses and 84 hours forecasts daily based at [00, 06, 12, 18] UTC on a subset of the 1/12° resolution global tri-polar grid (ORCA12). 

RIOPS includes a 3DVar ice concentration analysis (assimilating sattelite remote sensing and Canadian Ice Service ice charts) while the large scales of the ocean analysis are constrained by spectrally nudging the temperature and salinity fields to those of the CCMEP Global Ice Ocean Prediction System (which itself includes a full multivariate assimilation system that combines satellite observations with in situ observations). 

## Data location 

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available using the HTTP protocol and resides in a directory that is plainly accessible to a web browser. Visiting that directory with an interactive browser will yield a raw listing of links, each link being a downloadable GRIB2 file.

The data can be accessed at the following URLs :

* [https://dd.weather.gc.ca/model_riops/netcdf/forecast/polar_stereographic/nd/HH/hhh/](https://dd.weather.gc.ca/model_riops/netcdf/forecast/polar_stereographic/)

where :

* __nd__ : Number of spatial dimensions of the forecast fields [2d or 3d]
* __HH__ : Start hour of model run in UTC [00, 06, 12, 18]
* __hhh__ : Forecast hour [000, 001, 002, ..., 084] 


## File name nomenclature 

The files have the following nomenclature:

* {YYYYMMDD}T{HH}Z_MSC_RIOPS_VAR_LVL_{Grid}{resolution}_P{hhh}.nc

where :

* __YYYYMMDD__ : Year, month and day of the beginning of the forecast
* __T__ : Time delimiter according to ISO8601 norms
* __HH__ : UTC run time [00, 06, 12, 18]
* __Z__ : Time zone (UTC hour)
* __MSC__ : Constant string indicating the Meteorological Service of Canada, source of data
* __RIOPS__ : Constant string indicating the forecasting system that generated the data (RIOPS)
* __VAR__ : Name of forecast variable available in the file 
* __LVL__ : Vertical level [SFC, DBS-0.5m, DBS-all]; SFC for surface, DBS for Depth Below Surface, 0.5m for depth of 0.5m below the surface, 'all' for all depths 
* __Grid__ : Grid mapping projection [PS]
* __resolution__ : Horizontal resolution [5km], stands for 5 km horizontal resolution at 60°N latitude
* __Phhh__ : P is a constant character. hhh is the forecast hour [000, 001, 002, ..., 084]
* __nc__ : Constant string indicating the NetCDF format


Filenames examples : 

* 20200913T06Z_MSC_RIOPS_IICEVOL_SFC_PS5km_P012.nc 
* 20200913T12Z_MSC_RIOPS_VOSALINE_DBS-all_PS5km_P046.nc
* 20201014T00Z_MSC_RIOPS_VOTEMPER_DBS-0.5m_PS5km_P022.nc

## Levels

The three-dimensional fields are provided on 50 depth levels, which are the levels of the ocean model used in RIOPS.

__Depth levels (m)__ : 0.494025, 1.54138, 2.64567, 3.81949, 5.07822, 6.44061, 7.92956, 9.573, 11.405, 13.4671, 15.8101, 18.4956, 21.5988, 25.2114, 29.4447, 34.4342, 40.3441, 47.3737, 55.7643, 65.8073, 77.8539, 92.3261, 109.729, 130.666, 155.851, 186.126, 222.475, 266.04, 318.127, 380.213, 453.938, 541.089, 643.567, 763.333, 902.339, 1062.44, 1245.29, 1452.25, 1684.28, 1941.89, 2225.08, 2533.34, 2865.7, 3220.82, 3597.03, 3992.48, 4405.22, 4833.29, 5274.78, 5727.92.

Some of the two-dimensional variables represent quantities on the first model level, while others are defined at the sea surface (e.g. sea ice variables).

Visualization of field data from the NetCDF files produced by RIOPS was successfully tested with the following free CF-aware tools: Panoply (version 4.2.2) and IDV (version 5.2).

## List of variables

<table id="csv-table" class="display"></table>

<link href="https://cdn.jsdelivr.net/npm/simple-datatables@latest/dist/style.css" rel="stylesheet" type="text/css">
<script src="https://cdn.jsdelivr.net/npm/simple-datatables@latest"></script>
<script src="../../../js/variables_datatable.js" type="text/javascript"></script>
<script>
  loadTable("csv-table", "../../../assets/csv/RIOPS_Variables-List_en.csv");
</script>

Note: The unit `PSU` (Practical Salinity Unit) is equivalent to g/kg or per thousand (‰). It is based on the properties of sea water conductivity.

## Support

If you have any questions about this data, please [contact us](https://weather.gc.ca/mainmenu/contact_us_e.html).

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).
