[En français](readme_giops-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [GIOPS](readme_giops_en.md) > GIOPS on MSC Datamart

# Global Ice-Ocean Prediction System (GIOPS) Data in NetCDF Format

The Canadian Centre for Meteorological and Environmental Prediction (CCMEP) provides sea ice and ocean forecast fields produced by its [Global Ice-Ocean Prediction System (GIOPS)](readme_giops_en.md) and interpolated to two grids: a 0.2° resolution regular latitude-longitude grid (latlon0.2x0.2) and a grid in north-polar stereographic projection with 5km resolution at the standard parallel 60°N (ps5km60N).  Fields provided at 00Z and at forecast hour 0 represent the GIOPS analysis, which is nominally valid at 00Z.  At all other forecast hours the fields represent the model forecast and are averaged in time.  The data files are in NetCDF format (NetCDF-4 classic model) and comply with the Climate and Forecast Conventions.

The data files are in NetCDF format (NetCDF-4 classic model) and comply with the Climate and Forecast (CF) Conventions. Being self-described, the NetCDF files contain both data and sufficient information in their metadata describing the data.  For forecast hours greater than 0, the files contain time-mean sea ice and ocean forecast fields, where the length of the averaging period is 3 hours for two-dimensional fields and 24 hours for three-dimensional fields (both periods ending at the validity time of the respective fields).  For forecast hour 0 at 00Z, the files contain analysed fields, nominally valid at 00Z. The time in the file is encoded as the time in units of seconds elapsed since January 1st, 1950, 0h00 UTC.

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data can be accessed at the following URLs:

* [https://dd.weather.gc.ca/model_giops/netcdf](https://dd.weather.gc.ca/model_giops/netcdf)

A history of 5 days of forecast is kept in this directory.

* Files containing data on the latlon0.2x0.2 grid can be found at the following address:

[https://dd.weather.gc.ca/model_giops/netcdf/lat_lon/{nd}/{HH}/{hhh}/](https://dd.weather.gc.ca/model_giops/netcdf/lat_lon/)

* Files containing data on the ps5km60N grid can be found at the following address:

[https://dd.weather.gc.ca/model_giops/netcdf/polar_stereographic/{nd}/{HH}/{hhh}/](https://dd.weather.gc.ca/model_giops/netcdf/polar_stereographic)

where:

* __nd__ : Number of spatial dimensions of the forecast fields [2d or 3d].
* __HH__ : Start hour of model run in UTC [00,12].
* __hhh__ : Forecast hour: every 3 hours [000, 003, ..., 240] for N=2  and every 24 hours [000, 024, ..., 240] for N=3.

Note that because the forecast hour 0 at 00Z files are based on the analysis rather than the forecast, a reduced set of variables is provided at this forecast hour compared to other forecast hours.

NOTE: ALL HOURS ARE IN UTC.

The files have the following nomenclature:

* CMC_giops_Variable_LevelType_Level_ProjectionResolution_TimeMean_YYYYMMDDHH_FileTypehhh.nc

where:

* __CMC__ : Constant string indicating the data source (Canadian Meteorological Centre).
* __giops__ : Constant string indicating the forecasting system that generated the data (GIOPS).
* __Variable__ : Name of forecast variable available in the file.
* __LevelType__ : Level type taking one of the values: sfc, depth.
* __Level__ : Level value; 0 for the sfc (surface) level and either 0.5 (metres) or "all" (all model depths) for depth
level type.
* __Projection__ : Grid mapping (projection) taking one of the values: latlon, ps.
* __Resolution__ : Resolution taking one of the values: 0.2x0.2, 5km60N; 0.2x0.2 stands for 0.2-degree resolution in both.
the latitudinal and longitudinal directions, whereas 5km60N stands for 5-km resolution at 60°N latitude.
* __TimeMean__ : For forecast hours greater than 0, this takes either the value 3h-mean or 24h-mean and indicates that the variable is a time mean calculated over the specified time interval (3 hours for 3h, 24 hours for 24h). Note that the validity time of the forecast variable is set at the end of the time averaging period.  For forecast hour 0 this string is null (i.e. the fields provided are not time-averaged and are said to be valid at 00Z).
* __YYYYMMDD__ : Year, month and day of the beginning of the forecast.
* __HH__ : Start hour of model run in UTC [00,12].
* __FileTypehhh__ : For forecast hours greater than 0, FileType equals P and hhh is the forecast hour [003, 006, ..., 240].
For forecast hour 0 at run 00Z, FileType equals Anal and hhh equals 000.
* __nc__ : Constant string indicating the NetCDF format.

Example of forecast file name:
CMC_giops_votemper_depth_0.5_latlon0.2x0.2_3h-mean_2016020800_P036.nc

## Levels

The three-dimensional fields are provided on 50 depth levels, which are the levels of the ocean model used in GIOPS.

__Depth levels (m)__ : 0.494025, 1.54138, 2.64567, 3.81949, 5.07822, 6.44061, 7.92956, 9.573, 11.405, 13.4671, 15.8101, 18.4956, 21.5988, 25.2114, 29.4447, 34.4342, 40.3441, 47.3737, 55.7643, 65.8073, 77.8539, 92.3261, 109.729, 130.666, 155.851, 186.126, 222.475, 266.04, 318.127, 380.213, 453.938, 541.089, 643.567, 763.333, 902.339, 1062.44, 1245.29, 1452.25, 1684.28, 1941.89, 2225.08, 2533.34, 2865.7, 3220.82, 3597.03, 3992.48, 4405.22, 4833.29, 5274.78, 5727.92.

Some of the two-dimensional variables represent quantities on the first model level, while others are defined at the sea surface (e.g. sea ice variables).

Visualization of field data from the NetCDF files produced by GIOPS was successfully tested with the following free CF-aware tools: Panoply (version 4.2.2) and IDV (version 5.2).

## List of variables

<table id="csv-table" class="display"></table>

<link href="https://cdn.jsdelivr.net/npm/simple-datatables@latest/dist/style.css" rel="stylesheet" type="text/css">
<script src="https://cdn.jsdelivr.net/npm/simple-datatables@latest"></script>
<script src="../../../js/variables_datatable.js" type="text/javascript"></script>
<script>
  loadTable("csv-table", "../../../assets/csv/GIOPS_Variables-List_en.csv");
</script>

Note: The unit `PSU` (Practical Salinity Unit) is equivalent to g/kg or per thousand (‰). It is based on the properties of sea water conductivity.

Note that since forecast hour 0 fields at 00Z are not time-averaged, one can simply extract the surface level of votemper, vosaline, vozocrtx and vomecrty from the 3D files to obtain the corresponding 2D fields.

## Support

If you have any questions about , please contact us at: [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).
