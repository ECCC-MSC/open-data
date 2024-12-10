[En français](readme_rdsps-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [RDSPS](readme_rdsps_en.md) > RDSPS on MSC Datamart

# Regional Deterministic Storm Surge Prediction System (RDSPS) data in NetCDF format

This page describes the [Regional Deterministic Storm Surge Prediction System](readme_rdsps_en.md) data available in NetCDF format.

## Grid technical specification

![RDSPS grid image](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_rdsps/grille_rdsps.png)

This table lists the values of different parameters of the RDSPS grid:

| Parameter | Value |
| ------ | ------ |
| ni | 841 |
| nj | 541 |
| resolution | 0.033° x 0.033° |


##    Nomenclature of file directories

File names have the form:

```
{YYYYMMDD}T{HH}Z_MSC_RDSPS-Atlantic-North-West_{VAR}_{LVL}_{grille}{resolution}_P{hhh}.nc 
```

Where:

* __YYYYMMDD__: Year, month and day of the beginning of the forecast
* __T__ : Time delimiter according to ISO8601 norms
* __HH__: UTC run time [00, 12]
* __Z__ : Time zone (UTC hour)
* __MSC__ : Constant string indicating the Meteorological Service of Canada, source of data
* __RDSPS-Atlantic-North-West__ : Constant string indicating that data is from the Regional Deterministic Storm Surge Prediction System over the North-West domain
* __VAR__ : Variable type included in the file [ETAS, SSHT, SSH]
* __LVL__ : Vertical level [SFC for the surface]
* __grille__ : Horizontal grid lat-lon [LatLon]
* __resolution__ : 0.033x0.033. Indicating resolution in degreee 0.033x0.033 in latitude and longitude directions
* __Phhh__: P is a constant character. hhh is the forecast hour [000, 001, 002, ..., 240]
* __nc__: constant string indicating the NetCDF format is used

Example of file name:

20180417T12Z_MSC_RDSPS-Atlantic-North-West_ETAS_SFC_LatLon0.033x0.033_P024.nc

##    Variable list

The list below provides, for each variable: a short description, an alphabetical abbreviation, the levels available for the parameter, and measurement units.

|NetCDF   | Short description|                          Abbr.|  Level|  Units|
|---------|---------------|----------|----------|----------|
|etas     |Storm surge                            |    ETAS|   SFC|    m|
|ssh_tide |Tidal heights                          |    SSHT|   SFC|    m|
|zos      |Total Water Level (Sea surface height) |     SSH|   SFC|    m|

## Support

If you have any questions about this data, please [contact us](https://weather.gc.ca/mainmenu/contact_us_e.html).

## Announcements from the dd_info mailing list

Announcements related to this dataset are available in the [dd_info list](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).
