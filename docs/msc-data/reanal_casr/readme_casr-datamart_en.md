[En français](readme_casr-datamart_fr.md)

! [ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [Canadian Surface Reanalysis](readme_casr_en.md) > CaSR Derived Products on the MSC Datamart

# Products derived from the Canadian Surface Reanalysis (CaSR)

This page describes the gridded statistical products in NetCDF format as well as the aggregate statistical products by watershed in GeoJSON format, derived from the Canadian Surface Reanalysis (CaSR) available on the MSC Datamart.

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples for accessing and using the Meteorological Service of Canada's open data] (../../usage/readme_en.md) is also available.

The data is available via the HTTPS protocol. It is possible to access ir with a standard browser. In this case, you obtain a list of links to a NetCDF or GeoJON file, depending on the product.

Gridded statistical products derived from the Canadian Surface Reanalysis (CaSR) can be found at:

* [https://dd.weather.gc.ca/today/reanalysis_casr/casr/{Version}/post-processing/grid](https://dd.version.gc.ca/today/reanalysis_casr/casr/)

Aggregate statistical products by watershed, derived from the Canadian Surface Reanalysis (CaSR), can be found at:

* [https://dd.weather.gc.ca/today/reanalysis_casr/casr/{Version}/post-processing/watersheds/{polygon_dataset}/area{nb}](https://dd.weather.gc.ca/today/reanalysis_casr/casr/)

where:

* __Version__: [CaSR version](https://hpfx.collab.science.gc.ca/~scar700/rcas-casr/dataset_specifics.html#diff_casr_versions) of the Canadian Surface Reanalysis (e.g., v3.2)
* __polygon_dataset__: Name of the watershed polygon set (`nhn` for "National Hydrographic Network", `nhs` for "National Hydrological Service")
* __nb__: Main drainage basins according to:
    * 01: Maritime Provinces 
    * 02: St. Lawrence 
    * 03: Northern Quebec and Labrador 
    * 04: Southwest Hudson Bay 
    * 05: Nelson River 
    * 06: Western and Northern Hudson Bay 
    * 07: Great Slave Lake 
    * 08 : Pacific 
    * 09: Yukon River 
    * 10: Arctic 
    * 11: Mississippi River

## File name nomenclature 

The file names follow the nomenclature below:

__Gridded products in NetCDF format__

The forecast files follow the nomenclature below:

'{YYY1-YYY2}_MSC_CaSR-{version}_{Var}_Sfc_{Grid}{resolution}_{TimeStep}.nc'

The analysis files follow the nomenclature below:

'{YYY1-YYY2}_MSC_CaSR-{version}-Analysis_{Var}_Sfc_{Grid}{resolution}_{TimeStep}.nc'

where:

* __YYY1-YYY2__: Period covered by the reanalysis according to the version [1968–2024]
* __MSC__: Constant string for Meteorological Service of Canada, the data source
* __CaSR__: A string indicating that the data is derived from Canadian Surface Reanalysis (CaSR)
* __version__: [Version](https://hpfx.collab.science.gc.ca/~scar700/rcas-casr/dataset_specifics.html#diff_casr_versions) of the retest [v3.2]
* __Analysis__: A string indicating that the data are analyses, not forecasts
* __Var__: Name of variable
* __Sfc__: A string indicating that the vertical level is the surface
* __Grid__ : Horizontal rotated lat-lon grid [Rlatlon]
* __resolution__: Resolution of 0.09° (about 10km) in the longitudinal and latitudinal directions [0.09]
* __TimeStep__: No time, taking one of the values [P1Y, P1M]; `P1Y` represents a one-year time step and `P1M` represents a one-month time step
* __nc__: Constant string indicating that the format is NetCDF

Examples: 

* 1968-2024_MSC_CaSR-v3.2_Precip-Accum12h-MMin_Sfc_RLatLon0.09_P1M.nc
* 1968-2024_MSC_CaSR-v3.2-Analysis_DewPoint-YAvg_AGL-1.5m_RLatLon0.09_P1Y.nc

__Aggregate products by watershed in GeoJSON format__

The forecast files follow the nomenclature below:

'{YYY1-YYY2}_MSC_CaSR-{version}_DrainageArea{nb}_{Var}_Sfc_{TimeStep}.json'

The analysis files follow the nomenclature below:

'{YYY1-YYY2}_MSC_CaSR-{version}-Analysis_DrainageArea{nb}_{Var}_Sfc_{TimeStep}.json'

where:

* __YYY1-YYY2__: Period covered by the reanalysis according to the version [1968–2024]
* __MSC__: Constant string for Meteorological Service of Canada, the data source
* __CaSR__: A string indicating that the data is derived from Canadian Surface Reanalysis (CaSR)
* __version__: [Version](https://hpfx.collab.science.gc.ca/~scar700/rcas-casr/dataset_specifics.html#diff_casr_versions) of the retest [v3.2]
* __Analysis__: A string indicating that the data are analyses, not forecasts
* __DrainageArea__: Constant string of characters to specify the watershed  
* __nb__: Drainage basin number [01, 02, .., 11]
* __Var__: Name of variable
* __Sfc__: A string indicating that the vertical level is the surface
* __TimeStep__: No time, taking one of the values [P1Y, P1M]; `P1Y` represents a one-year time step and `P1M` represents a one-month time step
* __json__: A constant string indicating that the format is GeoJSON

Examples:

* 1968-2024_MSC_CaSR-v3.2-Analysis_DrainageArea02_Precip-Accum1h-MMin_Sfc_P1M.json
* 1968-2024_MSC_CaSR-v3.2_DrainageArea11_SnowDepth-YMax_Sfc_P1Y.json

## List of variables

* Precipitation quantity (m)
* Snow depth, aggregate (cm) 
* Water equivalent of the snow cover, aggregate (kg/m²) 
* Air Temperature (°C)
* Dew point temperature (°C)

## Support

If you have any questions about this data, please [contact us](https://weather.gc.ca/mainmenu/contact_us_e.html).

## Announcements from the dd_info mailing list

Announcements related to this dataset are available via the [dd_info list](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).


















[En français](readme_casr-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)


## Support

If you have any questions about these data, [please contact us](https://weather.gc.ca/mainmenu/contact_us_e.html).
## dd_info mailing list announcements 

Announcements related to this dataset are available via the [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/) list.
