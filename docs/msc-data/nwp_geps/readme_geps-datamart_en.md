[En français](readme_geps-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [GEPS](readme_geps_en.md) > GEPS on MSC Datamart

# Global Ensemble Prediction System (GEPS) Data in GRIB2 Format

This page describes the [Global Ensemble Prediction System](readme_geps_en.md) data available in GRIB2 format.

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available using the HTTP protocol and resides in a directory that is plainly accessible to a web browser. Visiting that directory with an interactive browser will yield a raw listing of links, each link being a downloadable GRIB2 file. In practice, we recommend writing your own script to automate the downloading of the desired data (using wget or equivalent). If you are unsure of how to proceed, you might like to take a look at our brief wget usage guide.

The data can be accessed at the following URLs :

* https://dd.weather.gc.ca/ensemble/geps/grib2/raw/HH/hhh/

where :

* __raw__ : Constant string indicating model data is raw (not processed)
* __HH__ : Model run start, in UTC [00,12]
* __hhh__ : Forecast hour [000, 003, …, 192, 198, 204, ..., 378, 384] and [000, 003, …, 192, 198, 204, ..., 762, 768] each Thursday at 000UTC

## Grid specifications

This table lists details of the latitude-longitude grid used in the encoding of the GRIB variables.

| Grid Parameter          | Value of Parameter       |
|-------------------------|--------------------------|
| ni                      | 720 points               |
| nj                      | 361 points               |
| resolution              | 0.5°                     |
| first gris point coordinate | 90° S 000° E         |

## File name nomenclature 

NOTE : ALL HOURS ARE IN UTC.

The files have the following nomenclature :

* CMC_geps-raw_Variable_LevelType_Level_latlonResolution_YYYYMMDDHH_Phhh_allmbrs.grib2
* CMC-geps-prob_Variable_LevelType_Level_Resolution_YYYYMMDDHH_Phhh_all-products.grib2


where :

* __CMC_geps__ : Constant string indicating that the data is from the Canadian Meteorological Centre (CMC), the model used (geps: Global Ensemble Prediction System).
* __raw__ : individual members direct model output
* __prob__ : probabilistic products created from all members
* __Resolution__ : Constant string indicating the data resolution (0p5x0p5)
* __Variable__ : Variable type included in this file. To consult a complete list, refer to the variables section.
* __LevelType__ : Level type. To consult a complete list, refer to the variables section.
* __Level__ : Level value. To consult a complete list, refer to the variables section.
* __YYYYMMDD__ : Year, month and day of the beginning of the forecast.
* __HH__ : UTC run time [00,12]
* __Phhh__ : P is a constant character. hhh is the forecast hour [000, 003, …, 192, 198, 204, ..., 378, 384] or [000, 003, …, 192, 198, 204, ..., 762, 768] each Thursday at 000UTC
* __allmbrs__ : Constant string indicating that all the members of the ensemble are included in this file
* __all-products__ : indicating that all probabilistic products for this variable are contain in the file
* __grib2__ : Constant string indicating the GRIB2 format is used

Example of file name :

CMC_geps-raw_UGRD_ISBL_0925_latlon0p5x0p5_2010090100_P078_allmbrs.grib2

This file originates from the Canadian Meteorological Center (CMC) and contains the raw data of the Global Ensemble Prediction System (CMC_geps-raw). The data in the file start on September 1st 2010 at 00Z (2010090100). It contains the U-component wind (UGRD) at the isobaric level 925 mb (ISBL_0925) for the forecast hour 78 (P078), for all members (allmbrs) in GRIB2 format (.grib2).

## List of variables
      
The variables for the ensemble products available in the GRIB2 files are listed below. For each variable, the definition, period and frequency are mentioned.

For ensemble products:

* __FPRATE-Accum-12h_SFC_0__    : Freezing rain accumulated over a 12h period : 12h-384h every 12h
* __FPRATE-Accum-24h_SFC_0__    : Freezing rain accumulated over a 24h period : 24h-384h every 24h
* __HEATX-Max-24h_TGL_2m__      : Humidex 2m above ground - Maximum over a 24h period : 24h-384h every 24h
* __HEATX_TGL_2m__              : Humidex 2m above ground : 3-384h every 3h
* __HGT_ISBL_0500__               : Geopotential height 500 hPa : 3-384h every 3h
* __IPRATE-Accum-12h_SFC_0__    : Ice pellet accumulated over a 12h period : 12h-384h every 12h
* __IPRATE-Accum-24h_SFC_0__    : Ice pellet accumulated over a 24h period : 24h-384h every 24h
* __PRMSL_MSL_0__               : Mean sea level pressure : 3-384h every 3h
* __RPRATE-Accum-12h_SFC_0__    : Rain accumulated over a 12h period : 12h-384h every 12h
* __RPRATE-Accum-24h_SFC_0__    : Rain accumulated over a 24h period : 24h-384h every 24h
* __SPRATE-Accum-12h_SFC_0__    : Snow (water equivalent) accumulated over a 12h period : 12h-384h every 12h
* __SPRATE-Accum-24h_SFC_0__    : Snow (water equivalent) accumulated over a 24h period : 24h-384h every 24h
* __TCDC_SFC_0__                : Cloud cover : 3-384h every 3h
* __TEMP-Max-24h_TGL_2m__       : Temperature 2m above ground - Maximum over a 24h period : 24h-384h every 24h
* __TEMP-Min-24h_TGL_2m__       : Temperature 2m above ground - Minimum over a 24h period : 24h-384h every 24h
* __TEMP_TGL_2m__               : Temperature 2m above ground : 3-384h every 3h
* __TPRATE-Accum-120h_SFC_0__   : Total precipitation accumulated over a 120h period : 120h-384h every 120h
* __TPRATE-Accum-12h_SFC_0__    : Total precipitation accumulated over a 12h period : 12h-384h every 12h
* __TPRATE-Accum-24h_SFC_0__   : Total precipitation accumulated over a 24h period : 24h-384h every 24h
* __TPRATE-Accum-48h_SFC_0__    : Total precipitation accumulated over a 48h period : 48h-384h every 48h
* __TPRATE-Accum-72h_SFC_0__    : Total precipitation accumulated over a 72h period : 72h-384h every 72h
* __TPRATE-Accum-96h_SFC_0__    : Total precipitation accumulated over a 96h period : 96h-384h every 96h
* __WCF-Min-24h_TGL_2m__        : Wind chill factor 2m above ground - Minimum over a 24h period : 24h-384h every 24h
* __WCF_TGL_2m__               : Wind chill factor 2m above ground : 3-384h every 3h
* __WIND-Max-12h_TGL_10m__      : Wind speed 10m above ground - Maximum over a 12h period : 12h-384h every 12h
* __WIND_TGL_10m__              : Wind speed 10m above ground : 3-384h every 3h
                                                                                  
For individual members:

* __AFRAIN_SFC_0__              : Freezing rain accumulation : 0-384h every 3h
* __AICEP_SFC_0__               : Ice pellet accumulation : 0-384h every 3h
* __APCP_SFC_0__                : Total precipitation accumulation : 0-384h every 3h
* __ARAIN_SFC_0__               : Rainfall : 0-384h every 3h
* __ASNOW_SFC_0__               : Snowfall : 0-384h every 3h
* __CAPE_SFC_0__                : Convective available potential energy : 0-384h every 3h
* __CIN_SFC_0__                 : Convective inhibition : 0-384h every 3h
* __DLWRF_SFC_0__               : Downward long wave rad. flux : 0-384h every 3h
* __DSWRF_SFC_0__               : Downward short wave rad. flux : 0-384h every 3h
* __HGT_ISBL_XXXX__            : Geopotential height at XXXX hPa : 0-384h every 3h
* __HGT_SFC_0__                 : Geopotential height at surface : 0-384h every 3h
* __ICETK_SFC_0__               : Ice thickness : 0-384h every 3h
* __LHTFL_SFC_0__               : Latent heat flux at surface : 0-384h every 3h
* __OLR_NTAT_0__                : Outgoing Long wave flux at the top of the atmosphere : 0-384h every 3h
* __PRES_SFC_0__                : Surface pression : 0-384h every 3h
* __PRMSL_MSL_0__               : Mean sea level pressure : 0-384h every 3h
* __PWAT_EATM_0__               : Precipitation water over entire column : 0-384h every 3h
* __RH_ISBL_XXXX__              : Relative humidity at XXXX hPa : 0-384h every 3h
* __RH_TGL_2m__                 : Relative humidity 2m above ground : 0-384h every 3h
* __SHTFL_SFC_0__               : Latent heat flux at surface : 0-384h every 3h
* __SNOD_SFC_0__                : Snow depth at surface : 0-384h every 3h
* __SWAT_DBLL_10cm__            : Soil volumetric water content 0-10cm below surface : 0-384h every 3h
* __VSOILM_DBLL_10cm__          : Soil volumetric water content 0-10cm below surface : 0-384h every 3h
* __TCDC_SFC_0__                : Cloud cover : 0-384h every 3h
* __TMAX_TGL_2m__               : Maximum temprature 2m above ground : 0-384h every 3h
* __TMIN_TGL_2m__               : Minimum temprature 2m above ground : 0-384h every 3h
* __TMP_ISBL_XXXX__             : Temperature at XXXX hPa : 0-384h every 3h
* __TMP_TGL_2m__                : Temperature 2m above ground : 0-384h every 3h
* __TSOIL_DBLL_10cm__           : Soil temperature 0-10cm below surface : 0-384h every 3h
* __UGRD_ISBL_XXXX__            : U wind component at XXXX hPa : 0-384h every 3h
* __UGRD_TGL_10m__              : U wind component 10m above ground : 0-384h every 3h
* __ULWRF_SFC_0__               : Upward long wave radiative flux at surface : 0-384h every 3h
* __USWRF_SFC_0__               : Upward short wave radiative flux at surface : 0-384h every 3h
* __VGRD_ISBL_XXXX__            : V wind component at XXXX hPa : 0-384h every 3h
* __VGRD_TGL_10m__              : V wind component 10m above ground : 0-384h every 3h
* __VVEL_ISBL_XXXX__            : Vertical velocity at XXXX hPa : 0-384h every 3h
* __WEASD_SFC_0__               : Snow water equivalent at the surface : 0-384h every 3h

## Support

If you have any questions about these data, please contact us at: [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).
