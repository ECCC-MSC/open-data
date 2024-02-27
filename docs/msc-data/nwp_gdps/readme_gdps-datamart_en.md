[En français](readme_gdps-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [GDPS](readme_gdps_en.md) > GDPS on MSC Datamart

# Global Deterministic Prediction System (GDPS) data in GRIB2 format

The fields in the GRIB2 dataset of the [Global Deterministic Prediction System (GDPS)](readme_gdps_en.md) are available on a latitude-longitude grid corresponding to an effective resolution of about 15 km.

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available via the HTTPS protocol. It is possible to access it with a standard browser. In this case, we obtain a list of links giving access to a GRIB2 file.

The data can be accessed at the following address :

[https://dd.weather.gc.ca/model_gem_global/{RES}/grib2/lat_lon/{HH}/{hhh}/](https://dd.weather.gc.ca/model_gem_global)

where :

* __RES__ : Horizontal resolution [15km]
* __HHH__ : UTC time of the beginning of the model run[00, 12]
* __hhhh__ : Forecast time[000, 003, 006, ..., 240]

A 20-hour history is kept in this directory.

## Technical specification of the grid

Values given to the parameters of the 15km latitude-longitude grid:

| Parameter | Value |
| ------ | ------ |
| ni | 2400 |
| nj | 1201 | 
| resolution | 0.15° |
| coordinates of the first grid point | 90° S  180° W | 

## File name nomenclature 

NOTE: ALL HOURS ARE IN UTC.

The files have the following nomenclature:

CMC_glb_Variable_LevelType_Level_ProjectionResolution_YYYYMMDDHH_Phhh.grib2

where :

* __CMC__ : constant string indicating that the data is from the Canadian Meteorological Centre
* __glb__ : constant string indicating that the data is from the GDPS
* __Variable__ : Variable type included in this file. To consult a complete list, refer to the Data in GRIB2 format section.
* __LevelType__ : Level type. To consult a complete list, refer to the Data in GRIB2 format section.
* __Level__ : Level value. To consult a complete list, refer to the Data in GRIB2 format section.
* __Projection__ : projection used for the data. Can take the values [latlon, ps]
* __Resolution__ : constant string indicating the data resolution [.15x.15].
* __YYYYMMDD__ : Year, month and day of the beginning of the forecast.
* __HH__ : UTC run time [00, 12]
* __Phhh__ : P is a constant character. hhh is the forecast hour [000, 003, 006, ..., 240]
* __grib2__ : constant string indicating the GRIB2 format is used

Example of file name :

CMC_glb_TMP_ISBL_925_latlon.15x.15_2019101512_P042.grib2

This file originates from the Canadian Meteorological Center (CMC) and contains the data of the GDPS. The data in the file start on October 15th 2019 at 12Z (2019101512). It contains the temperature component (TMP) at the isobaric level 925 mb (ISBL_0925) for the forecast hour 42 (P042) in GRIB2 format (.grib2).

## Levels

Vertical coverage of three-dimensional fields is provided by up to 33 isobaric levels.

* Isobaric levels (hPa): 1015, 1000, 985, 970, 950, 925, 900, 850, 800, 750, 700, 650, 600, 550, 500, 450, 400, 350, 300, 275, 250, 225, 200, 175, 150, 100, 50.

    * Additional levels 30, 20, 10, 5 et 1 hPa for the variables TMP, HGT, UGRD, VGRD, WIND, WDIR, SPFH

    * Additional levels 30, 20 et 10 hPa for the variables RH et DEPR

* Some fields receive limited three-dimensional coverage of five levels in the vertical, namely 850, 700, 600, 500, 250 hPa.

Additional levels that may be applicable to a given parameter are :

* Surface
* Fixed height above ground
* Fixed height below ground
* Thickness between two isobaric levels
* Nominal top of the atmosphere
* Entire atmospheric column

## List of variables

<table id="csv-table" class="display"></table>

<link href="https://cdn.jsdelivr.net/npm/simple-datatables@latest/dist/style.css" rel="stylesheet" type="text/css">
<script src="https://cdn.jsdelivr.net/npm/simple-datatables@latest"></script>
<script src="../../../js/variables_datatable.js" type="text/javascript"></script>
<script>
  loadTable("csv-table", "../../../assets/csv/GDPS_Variables-List_en.csv");
</script>

Notes :

* u (UGRD) and v (VGRD) components of the wind vector are to be resolved relative to the defined grid, in the direction of increasing i and j coordinates. Please refer to Code Table 7 of the GRIB standard for further details.
    
* Radiation fluxes parameters NLWRS_SFC, DSWRF_NTAT, and DLWRF_NTAT are encoded as accumulated values, as per value 4 of the Time Range Indicator (Code Table 5 of the GRIB format standard). This changes the unit from Watts per square metre to Joules per square meter.
    
* Specific Humidity (SPFH) is the model's native moisture variable. It should be used in all NWP applications. Dew point depression (DEPR) is a diagnostic parameter and is not meant for use in high-precision applications.

## Support

If you have any questions about this data, please [contact us](https://weather.gc.ca/mainmenu/contact_us_e.html).

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).

