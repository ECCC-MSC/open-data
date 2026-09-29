[En français](readme_casr-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [Canadian Surface Reanalysis](readme_casr_en.md) > CaSR Derived Products on the MSC Datamart

# Products derived from the Canadian Surface Reanalysis (CaSR)

This page describes the gridded statistical products in NetCDF format as well as the aggregate statistical products by watershed in GeoJSON format, derived from the Canadian Surface Reanalysis (CaSR) available on the MSC Datamart.

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples for accessing and using the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available via the HTTPS protocol. It is possible to access ir with a standard browser. In this case, you obtain a list of links to a NetCDF or GeoJON file, depending on the product.

__Gridded statistical products__ derived from the Canadian Surface Reanalysis (CaSR) can be found at:

* [https://dd.weather.gc.ca/today/reanalysis_casr/casr/{Version}/post-processing/grid](https://dd.version.gc.ca/today/reanalysis_casr/casr/)

__Aggregate statistical products by watershed__, derived from the Canadian Surface Reanalysis (CaSR), can be found at:

* [https://dd.weather.gc.ca/today/reanalysis_casr/casr/{Version}/post-processing/watersheds/{polygon_dataset}/area{nb}](https://dd.weather.gc.ca/today/reanalysis_casr/casr/)

where:

* __Version__: [CaSR version](https://hpfx.collab.science.gc.ca/~scar700/rcas-casr/dataset_specifics.html#diff_casr_versions) of the Canadian Surface Reanalysis (v2.1, v3.2)
* __polygon_dataset__: Name of the watershed polygon set (`nhn` for "National Hydro Network", `nhs` for "National Hydrological Service")
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

__Gridded products in NetCDF format__

The forecast files follow the nomenclature below:

`{YYY1-YYY2}_MSC_CaSR-{version}_{Var}_Sfc_{Grid}{resolution}_{TimeStep}.nc`

The analysis files follow the nomenclature below:

`{YYY1-YYY2}_MSC_CaSR-{version}-Analysis_{Var}_Sfc_{Grid}{resolution}_{TimeStep}.nc`

where:

* __YYY1-YYY2__: Period covered by the reanalysis according to the version [1980-2018 for version 2.1, 1968-2024 for version 3.2]
* __MSC__: Constant string for Meteorological Service of Canada, the data source
* __CaSR__: A string indicating that the data is derived from Canadian Surface Reanalysis (CaSR)
* __version__: [Version](https://hpfx.collab.science.gc.ca/~scar700/rcas-casr/dataset_specifics.html#diff_casr_versions) of the retest [v2.1, v3.2]
* __Analysis__: A string indicating that data are analyses, not forecasts
* __Var__: Variable name and associated statistics (see section below)
* __Sfc__: A string indicating that the vertical level is the surface
* __Grid__ : Horizontal rotated lat-lon grid [Rlatlon]
* __resolution__: Resolution of 0.09° (about 10km) in the longitudinal and latitudinal directions [0.09]
* __TimeStep__: No time, taking one of the values [P1Y, P1M]; `P1Y` represents a one-year time step and `P1M` represents a one-month time step
* __nc__: Constant string indicating that the format is NetCDF

Examples: 

* 1980-2018_MSC_CaSR-v2.1_AirTemp-YAvg_AGL-1.5m_RLatLon0.09_P1Y.nc
* 1968-2024_MSC_CaSR-v3.2-Analysis_Precip-Accum2h-MMax_Sfc_RLatLon0.09_P1M.nc

__Aggregate products by watershed in GeoJSON format__

The forecast files follow the nomenclature below:

'{YYY1-YYY2}_MSC_CaSR-{version}_DrainageArea{nb}_{Var}_Sfc_{TimeStep}.json'

The analysis files follow the nomenclature below:

'{YYY1-YYY2}_MSC_CaSR-{version}-Analysis_DrainageArea{nb}_{Var}_Sfc_{TimeStep}.json'

where:

* __YYY1-YYY2__: Period covered by the reanalysis according to the version [1980-2018 for version 2.1, 1968-2024 for version 3.2]
* __MSC__: Constant string for Meteorological Service of Canada, the data source
* __CaSR__: A string indicating that the data is derived from Canadian Surface Reanalysis (CaSR)
* __version__: [Version](https://hpfx.collab.science.gc.ca/~scar700/rcas-casr/dataset_specifics.html#diff_casr_versions) of the retest [v2.1, v3.2]
* __Analysis__: A string indicating that data are analyses, not forecasts
* __DrainageArea__: Constant string of characters to specify the watershed  
* __nb__: Drainage basin number [01, 02, .., 11]
* __Var__: Variable name and associated statistics (see section below)
* __Sfc__: A string indicating that the vertical level is the surface
* __TimeStep__: No time, taking one of the values [P1Y, P1M]; `P1Y` represents a one-year time step and `P1M` represents a one-month time step
* __json__: A constant string indicating that the format is GeoJSON

Examples:

* 1980-2018_MSC_CaSR-v2.1-Analysis_DrainageArea02_Precip-Accum1h-MMax_Sfc_P1M.json
* 1968-2024_MSC_CaSR-v3.2_DrainageArea02_SnowWaterEquiv-YAvg_Sfc_P1Y.json

## List of variables

* Quantity of accumulated precipitation (m) over a given period (1h, 2h, 6h, 12h, 24h)
* Snow depth at ground level (cm) 
* Water equivalent of the snow cover at ground level (kg/m²) 
* Air temperature (°C)
* Dew point temperature (°C)

__Notes__:

* Each variable is associated with a statistic, i.e. the annual/monthly average ('YAvg/MAvg'), the annual/monthly minimum ('YMin/MMin') or the annual/monthly maximum ('YMax/MMax'). Examples:
    * 'SnowWaterEquiv-YAvg'
    * 'DewPoint-MMin'
* The following analysis fields are available according to the version:
     * Version 2.1: quantity of accumulated precipitation
     * Version 3.2: quantity of accumulated precipitation, Air temperature, dew point temperature

## Support

If you have any questions about this data, please [contact us](https://weather.gc.ca/mainmenu/contact_us_e.html).

## Announcements from the dd_info mailing list

Announcements related to this dataset are available via the [dd_info list](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).
