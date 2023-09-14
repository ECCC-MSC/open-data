[En français](readme_reps-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [REPS](readme_reps_en.md) > REPS on MSC Datamart

# Regional Ensemble Prediction System (REPS) Data in GRIB2 Format

This page describes [Regional Ensemble Prediction System](readme_reps_en.md) data available in GRIB2 format.

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as it becomes available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

This data is available using the HTTPS protocol and resides in a directory that is plainly accessible from a web browser. Visiting this directory with an interactive browser will yield a raw listing of links, each link being a downloadable GRIB2 file. 

This data can be accessed at the following URLs:

* Polar-stereographic grid at 15km resolution: [https://dd.weather.gc.ca/ensemble/reps/15km/grib2/{EnsembleDataType}/{HH}/{hhh}](https://dd.weather.gc.ca/ensemble/reps/15km/grib2)
* Rotated lat-lon grid at 10km resolution: [https://dd.meteo.gc.ca/ensemble/reps/10km/grib2/{HH}/{hhh}](https://dd.meteo.gc.ca/ensemble/reps/10km/grib2)

where :

* __EnsembleDataType__ : Can be "raw" for individual members direct model output or prob for probabilistic products created from all members
* __HH__ : Forecast run hour in UTC
* __hhh__ : Forecast time

A 24-hour history is stored in this directory.

## Technical specification of the grid

* __Polar-stereographic grid__

![REPS grid ps](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_reps/grille_reps_ps.png)

Values assigned to the parameters of the stereographic polar grid at 15km resolution:

| Parameter | Value |
| ------ | ------ |
| ni | 600 |
| nj | 510 | 
| resolution at 60° N | 15 km |
| coordinates of the first grid point | 19.3206° N  141.5411° W | 
| grid orientation (with respect to j axis) | -110.0° |

* __Rotated lat-lon grid__

![Grille du SRPE Rlatlon](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_reps/grille_reps_rlatlon.png)

The following table lists the values of various parameters of the rotated lat-lon grid at 10km resolution:

| Parameter | Valeur |
| ------ | ------ |
| ni | 908 |
| nj | 960 | 
| resolution at 60° N | 10 km |
| coordinate of the first grid point |  50.76° N ; 20.81° W |

__Note__ : The [most recent versions of wgrib2](https://www.cpc.ncep.noaa.gov/products/wesley/wgrib2/update_2.0.8.html) and [GDAL](https://gdal.org/) support these rotated grids.

## File name nomenclature 

NOTE: ALL HOURS ARE IN UTC.

### Polar-stereographic grid at 15km resolution 

Files have the following nomenclature:

```
CMC-reps-srpe-{datatype}_{VAR}_{LVLTYPE}_{LVL}_{resolution}_{YYYYMMDDHH}_P{hhh}_{content}.grib2
```

where:

* __datatype__ : Can be "raw" for individual member direct model output or prob for probabilistic products created from all members
* __VAR__ : Variable name (ex: WIND) 
* __LVLTYPE__ : Level type (ex: SFC for surface, NTAT for the top of the atmosphere, DBLL_10cm for 10cm under the surface, TGL for above ground level)
* __LVL__ : Level value (ex: 10m for 10 meters)
* __resolution__ : Grid resolution (ex: ps15km)
* __YYYYMMDDHH__ : Year, month, and day of the beginning of the forecast and model run in UTC [00, 06, 12, 18]
* __P{hhh}__ : P is a constant character. "hhh" is the forecast hour [000, 003, 006, ..., 072].
* __FileContent__ : can be "all-products" or "allmbrs", indicating that all the members or all the probabilistic products for this variable are contained in the file 
* __grib2__ : Constant string indicating that the GRIB2 format is used

Example of filname: CMC-reps-srpe-prob_TEMP_TGL_2m_ps15km_2021012700_P009_all-products.grib2

### Rotated lat-lon grid at 10km resolution

Files have the following nomenclature:

```
{YYYYMMDD}T{HH}Z_MSC_REPS_{VAR}_{LVLTYPE-LVL}_{Grille}{resolution}_PT{hhh}H.grib2
```
where:

* __YYYYMMDD__ : Year, month, and day of the beginning of the forecast
* __T__ : Time delimiter according to ISO8601 norms
* __HH__ : UTC run time [00, 06, 12, 18]
* __Z__ : Time zone (UTC hour)
* __MSC__ : Constant string indicating the Meteorological Service of Canada, source of data
* __REPS__ : Constant string indicating that the data is from the Regional Ensemble Prediction System
* __VAR__ : Variable type included in the file (ex: UGRD). This parameter includes also the statistical measure, if relevant (ex: Accum, MAX, Min). See also the note below.
* __LVLTYPE-LVL__ : Vertical level type and level value [ex: SFC for surface, AGL-10m for 10m above ground level]
* __Grille__ : Horizontal grid [RLatLon]
* __resolution__ : 0.09. Indicating resolution in degrees [0.09°(about 10km)] for latitude and longitude directions
* __PT{hhh}H__ : Forecast hours based on [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) norms. P, T and H are constant character designating Period, Time and Hour. "hhh" is the forecast hour [000, 003, 006, ..., 072]
* __grib2__ : Constant string indicating that the GRIB2 format is used

Example of filename :  20201007T00Z_MSC_REPS_TPRATE-Accum24h_SFC_RLatLon0.09x0.09_PT024H.grib2

__Note__: Files contain by default all ensemble members. Files containing __probabilistic products__ are identified according to the parameter '-Prob' attached to the variable (ex: 20201007T00Z_MSC_REPS_TPRATE-Accum24h-Prob_SFC_RLatLon0.09x0.09_PT024H.grib2)

## List of variables

__Individual members:__ 

<table id="csv-table" class="display"></table>

<link href="https://cdn.jsdelivr.net/npm/simple-datatables@latest/dist/style.css" rel="stylesheet" type="text/css">
<script src="https://cdn.jsdelivr.net/npm/simple-datatables@latest"></script>
<script src="../../../js/variables_datatable.js" type="text/javascript"></script>
<script>
  loadTable("csv-table", "../../../assets/csv/REPS_en.csv", "EN");
</script>

__Ensemble products:__ 

<table id="csv-prob-table" class="display"></table>

<script>
  loadTable("csv-prob-table", "../../../assets/csv/REPS_prob_en.csv", "EN");
</script>

The files contain probability products by member counting above or below different thresholds, percentiles, means, medians and standard deviations. Note that products and thresholds are defined in the file metadata. The following products are available for each of the variables listed below.

###### HEATX

* Probability above 298.14, 303.14, 308.14, 311.14, 313.14 and 315.14 K
* Minimum (0 percentile), maximum (100th percentile), median (50th percentile), standard deviation and mean
* 10 percentile, 25 percentile, 75 percentile and 90 percentile

###### FPRATE

* Probability above 0.2, 1, 2.5, 5, 10, 15, 20, 25, 30, 40 and 50 kg/(m<sup>2</sup>*s)
* Minimum (0 percentile), maximum (100th percentile), median (50th percentile), standard deviation and mean
* 10 percentile, 25 percentile, 75 percentile and 90 percentile

###### IPRATE

* Probability above 0.2, 1, 2.5, 5, 10, 15, 20, 25, 30, 40 and 50 kg/(m<sup>2</sup>*s)
* Minimum (0 percentile), maximum (100th percentile), median (50th percentile), standard deviation and mean
* 10 percentile, 25 percentile, 75 percentile and 90 percentile

###### RPRATE

* Probability above 0.2, 1, 2.5, 5, 10, 15, 20, 25, 30, 40, 50, 75, 100 and 150 kg/(m<sup>2</sup>*s)
* Minimum (0 percentile), maximum (100th percentile), median (50th percentile), standard deviation and mean
* 10 percentile, 25 percentile, 75 percentile and 90 percentile

###### SPRATE

* Probability above 0.2, 1, 2.5, 5, 10, 15, 20, 25, 30, 40, 50, 75 and 100 kg/(m<sup>2</sup>*s)
* Minimum (0 percentile), maximum (100th percentile), median (50th percentile), standard deviation and mean
* 10 percentile, 25 percentile, 75 percentile and 90 percentile

###### TPRATE

* Probability above 0.2, 1, 2.5, 5, 10, 15, 20, 25, 30, 40, 50, 75, 100 and 150 kg/(m<sup>2</sup>*s)
* Minimum (0 percentile), maximum (100th percentile), median (50th percentile), standard deviation and mean
* 10 percentile, 25 percentile, 75 percentile and 90 percentile

###### TMP

* Probability above 243.14, 248.14, 253.14, 258.14, 263.14, 268.14, 273.14, 278.14, 283.14, 288.14, 293.14, 298.14, 303.14, 308.14 and 313.14 K
* Probability below 233.14, 238.14, 243.14, 248.14, 253.14, 258.14, 263.14, 268.14, 273.14, 278.14, 283.14, 288.14, 293.14 and 298.14 K
* Minimum (0 percentile), maximum (100th percentile), median (50th percentile), standard deviation and mean
* 10 percentile, 25 percentile, 75 percentile and 90 percentile

###### WCF

* Probability below 223.14, 228.14, 233.14, 238.14, 243.14, 248.14, 253.14, 258.14, 263.14, 268.14 and 273.14 K
* Minimum (0 percentile), maximum (100th percentile), median (50th percentile), standard deviation and mean
* 10 percentile, 25 percentile, 75 percentile and 90 percentile

###### WIND

* Probability above 5.5556, 8.3333, 10.278, 11.111, 13.889, 17.222, 18.056, 20.833, 24.444, 25, 27.778 and 32.778 m/s
* Minimum (0 percentile), maximum (100th percentile), median (50th percentile), standard deviation and mean
* 10 percentile, 25 percentile, 75 percentile and 90 percentile

A [list in XML format](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_reps/reps_element.xml) containing for all the 15km grid variables names, a description and the units in both French and English, is available.

## About the no-data mask for the polar-stereographic grid

A mask called "No-data" has been added to our GRIB2 encoding process in order to better represent the areas where data are unavailable. This mask only concerns a few grid points with no data, always the same ones, located at the edge of the domain. Note that this mask has no negative effect on the product quality.

## Support

If you have any questions about this data, please contact us at: [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).
