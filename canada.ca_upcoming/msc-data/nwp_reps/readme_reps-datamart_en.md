[En Français](readme_reps-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC Open Public Data](../readme_en.md) > REPS

# Regional Ensemble Prediction System (REPS) Data in GRIB2 Format

This page describes the [regional ensemble prediction system](readme_reps_en.md) data available in GRIB2 format.

# Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](.../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](.../../usage/readme_en.md) is also available.

The data is available using the HTTP protocol and resides in a directory that is plainly accessible to a web browser. Visiting that directory with an interactive browser will yield a raw listing of links, each link being a downloadable GRIB2 file. In practice, we recommend writing your own script to automate the downloading of the desired data (using wget or equivalent). If you are unsure of how to proceed, you might like to take a look at our brief wget usage guide.

The data can be accessed at the following URLs:

https://dd.meteo.gc.ca/ensemble/reps/15km/grib2/EnsembleDataType/HH/hhh

where:
* __EnsembleDataType__ : Can be raw for individual members direct model output or prob for probabilistic products created from all members.
* __HH__ : Forecast run hour in UTC
* __hhh__ : Forecast time

## File name nomenclature 

NOTE: ALL HOURS ARE IN UTC.

The files have the following nomenclature:

CMC-reps-srpe-EnsembleDataType_Variable_LevelType_Level_Resolution_YYYYMMDDHH_Phhh_FileContent.grib2

where:

* __EnsembleDataType__ : Can be raw for individual members direct model output or prob for probabilistic products created from all members.
* __Variable__ : Variable name (ex: WIND) 
* __LevelType__ : Level type (ex: TGL for above ground level)
* __Level__ : Level value (ex: 10m for 10 meters)
* __Resolution__ : Grid resolution (ex: ps15km)
* __YYYYMMDDHH__ : Date of the model run in UTC
* __Phhh__ : Forecast hour
* __FileContent__ : can be all-products or allmbrs, indicating that all the members or all the probabilistic products for this variable are contain in the file 

## List of variables


The variables for the ensemble products available in the GRIB2 files are listed below. For each variable, the definition, period and frequency are mentioned.

* __FPRATE-Accum-6h_SFC_0__ :  Freezing rain accumulated over a 6h period : 6-72h every 6h
* __FPRATE-Accum-12h_SFC_0__ : Freezing rain accumulated over a 12h period : 12-72h every 6h
* __FPRATE-Accum-24h_SFC_0__ : Freezing rain accumulated over a 24h period : 24-72h every 6h
* __HEATX-Max-24h_TGL_2m__ :   Humidex 2m above ground - Maximum over 24h period : 24-72h every 12h
* __HEATX_TGL_2m__ :           Humidex 2m above ground : 3-72h every 3h
* __IPRATE-Accum-6h_SFC_0__ :  Ice pellets (water equivalent) accumulated over a 6h period : 6-72h every 6h
* __IPRATE-Accum-12h_SFC_0__ : Ice pellets (water equivalent) accumulated over a 12h period : 12-72h every 6h
* __IPRATE-Accum-24h_SFC_0__ : Ice pellets (water equivalent) accumulated over a 24h period : 24-72h every 6h
* __RPRATE-Accum-6h_SFC_0__ :  Rain accumulated over a 6h period : 6-72h every 6h
* __RPRATE-Accum-12h_SFC_0__ : Rain accumulated over a 12h period : 12-72h every 6h
* __RPRATE-Accum-24h_SFC_0__ : Rain accumulated over a 24h period : 24-72h every 6h
* __SPRATE-Accum-6h_SFC_0__ :  Snow (water equivalent) accumulated over a 6h period : 6-72h every 6h
* __SPRATE-Accum-12h_SFC_0__ : Snow (water equivalent) accumulated over a 12h period : 12-72h every 6h
* __SPRATE-Accum-24h_SFC_0__ : Snow (water equivalent) accumulated over a 24h period : 24-72h every 6h
* __TEMP-Max-24h_TGL_2m__ :    Temperature 2m above ground - Maximum over 24h period : 24-72h every 12h
* __TEMP-Min-24h_TGL_2m__ :    Temperature 2m above ground - Minimum over 24h period : 24-72h every 12h
* __TEMP_TGL_2m__ :            Temperature 2m above ground : 3-72h every 3h
* __TPRATE-Accum-3h_SFC_0__ :  Total precipitation accumulated over a 3h period : 3-72h every 3h
* __TPRATE-Accum-6h_SFC_0__ :  Total precipitation accumulated over a 6h period : 6-72h every 6h
* __TPRATE-Accum-12h_SFC_0__ : Total precipitation accumulated over a 12h period : 12-72h every 6h
* __TPRATE-Accum-24h_SFC_0__ : Total precipitation accumulated over a 24h period : 24-72h every 6h
* __TPRATE-Accum-48h_SFC_0__ : Total precipitation accumulated over a 48h period : 48-72h every 24h
* __TPRATE-Accum-72h_SFC_0__ : Total precipitation accumulated over a 72h period : 72-72h every 72h
* __WCF-Min-24h_TGL_2m__ :     Wind chill factor 2m above ground - Minimum over 24h period : 24-72h every 12h
* __WCF_TGL_2m__ :             Wind chill 2m above ground : 3-72h every 3h
* __WIND-Max-12h_TGL_10m__ :   Wind speed 10m above ground - Maximum over 12h period : 12-72h every 12h
* __WIND_TGL_10m__ :           Wind speed 10m above ground : 3-72h every 3h
                                                                                  
The GRIB2 files variables for individual members are the following. The variables are avialable from 0 to 72h every 3h:

* __AFRAIN_SFC_0__ :     Accumulated precipitation in the form of freezing rain
* __ARAIN_SFC_0__ :      Accumulated precipitation in the form of rain 
* __AICEP_SFC_0__ :      Accumulated precipitation in the form of ice 
* __ASNOW_SFC_0__ :      Accumulated precipitation in the form of snow 
* __APCP_SFC_0__ :       Accumulated precipitation, total of all forms
* __SNOD_SFC_0__ :       Snow depth 
* __WEASD_SFC_0__ :      Water equivalent of accumulated Snow Depth 
* __HGT_ISBL_PPPP__ :    Geopotential height for different level pressure levels where PPPP is the level in hPa
* __RH_ISBL_PPPP__ :     Relative humidity at different pressure levels where PPPP is the level in hPa
* __UGRD_ISBL_PPPP__ :   Winds. U-component at different pressure levelwhere PPPP is the level in hPa
* __VGRD_ISBL_PPPP__ :   Winds. V-component at different pressure levelwhere PPPP is the level in hPa
* __TMP_ISBL_PPPP__ :    Temperature at different pressure levels where PPPP is the level in hPa
* __RH_TGL_2m__ :        Relative humidity at 2m 
* __TMP_TGL_2m__ :       Temperature at 2m 
* __TCDC_SFC_0__ :       Total cloud cover
* __PRES_SFC_0__ :       Pressure at surface 
* __MSL_0__ :            Mean sea level pressure at surface 
* __TSOIL_DBLL_10cm__ :  Soil temperature. 10cm below surface 
* __VSOILM_DBLL_10cm__ : Volumetric soil moisture. 10cm below the surface 
* __LHTFL_SFC__ :        Latent heat net flux at surface 
* __SHTFL_SFC_0__ :      Sensible heat net flux at surface 
* __ULWRF_NTAT_0__ :     Upward long-wave radiation flux at the nominal top of the atmosphere 
* __DLWRF_SFC_0__ :      Downward long-wave radiation flux at surface 
* __DSWRF_SFC_0__ :      Downward short-wave radiation flux at surface 

You can find a list in XML format cont.

A [list in XML format](http://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_reps/reps_element.xml) containing for all the variables names, a description and the units in both French and English, is available.

## Support

If you have any questions about these data, please contact us at: ec.dps-client.ec@canada.ca

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).
