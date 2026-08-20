[En français](readme_casr-land-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [Canadian Surface Reanalysis](readme_casr_en.md) > CaSR-Land derived products on the MSC Datamart

# Products derived from the Canadian Surface Reanalysis - Land (CaSR-Land)

This page describes the gridded statistical products in NetCDF format as well as the aggregate statistical products by watershed in GeoJSON format, derived from the [Canadian Surface Reanalysis-Land (CaSR-Land)](https://hpfx.collab.science.gc.ca/~scar700/rcas-casr/overview_subproducts.html) available on the MSC Datamart.

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples for accessing and using the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available via the HTTPS protocol. It is possible to access ir with a standard browser. In this case, you obtain a list of links to a NetCDF or GeoJON file, depending on the product.

__Gridded statistical products__ derived from the Canadian Surface Reanalysis - Land (CaSR-Land) can be found at:

* [https://dd.weather.gc.ca/today/reanalysis_casr/casr-land/{Version}/post-processing/grid](https://dd.version.gc.ca/today/reanalysis_casr/casr-land/)

__Aggregate statistical products by watershed__, derived from the Canadian Surface Reanalysis - Land (CaSR-Land), can be found at:

* [https://dd.weather.gc.ca/today/reanalysis_casr/casr-land/{Version}/post-processing/watersheds/{polygon_dataset}/area{nb}](https://dd.weather.gc.ca/today/reanalysis_casr/casr-land/)

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

__Gridded products in NetCDF format__

The forecast files follow the nomenclature below:

`{YYY1-YYY2}_MSC_CaSR-Land-{version}_{Var}_{Level}_{Grid}{resolution}_{TimeStep}.nc`

where:

* __YYY1-YYY2__: Period covered by the reanalysis according to the version [1968–2024]
* __MSC__: Constant string for Meteorological Service of Canada, the data source
* __CaSR-Land__: A string indicating that the data is derived from Canadian Surface Reanalysis-Land
* __version__: [Version](https://hpfx.collab.science.gc.ca/~scar700/rcas-casr/dataset_specifics.html#diff_casr_versions) of the retest [v3.2]
* __Var__: Variable name and associated statistics (see section below)
* __Level__: A string indicating the vertical level [`Sfc` for the surface, `AGL` for "Above Ground Level", `DBS` for "Depth Below Surface"]
* __Grille__ : Horizontal rotated lat-lon grid [Rlatlon]
* __resolution__: Resolution of 0.09° (about 10km) in the longitudinal and latitudinal directions [0.09]
* __TimeStep__: No time, taking one of the values [P1Y, P1M]; `P1Y` represents a one-year time step and `P1M` represents a one-month time step
* __nc__: Constant string indicating that the format is NetCDF

Examples:

* 1968-2024_MSC_CaSR-Land-v3.2_DewPoint-MMax_AGL-1.5m_RLatLon0.09_P1M.nc
* 1968-2024_MSC_CaSR-Land-v3.2_SoilLiquidWaterContent-YMin_DBS-200to300cm_RLatLon0.09_P1Y.nc

__Aggregate products by watershed in GeoJSON format__

The forecast files follow the nomenclature below:

`{YYY1-YYY2}_MSC_CaSR-Land-{version}_DrainageArea{nb}_{Var}_{Level}_{TimeStep}.json`

where:

* __YYY1-YYY2__: Period covered by the reanalysis according to the version [1968–2024]
* __MSC__: Constant string for Meteorological Service of Canada, the data source
* __CaSR-Land__: A string indicating that the data is derived from Canadian Surface Reanalysis-Land 
* __version__: [Version](https://hpfx.collab.science.gc.ca/~scar700/rcas-casr/dataset_specifics.html#diff_casr_versions) of the retest [v3.2]
* __DrainageArea__: Constant string of characters to specify the watershed  
* __nb__: Drainage basin number [01, 02, .., 11]
* __Var__: Variable name and associated statistics (see section below)
* __Sfc__: A string indicating the vertical level [`Sfc` for the surface, `AGL` for "Above Ground Level", `DBS` for "Depth Below Surface"]
* __TimeStep__: No time, taking one of the values [P1Y, P1M]; `P1Y` represents a one-year time step and `P1M` represents a one-month time step
* __json__: A constant string indicating that the format is GeoJSON

Examples:

* 1968-2024_MSC_CaSR-Land-v3.2_DrainageArea03_Drainage-Accum1h-YMax_DBS_P1Y.json
* 1968-2024_MSC_CaSR-Land-v3.2_DrainageArea10_SoilLiquidWaterContent-MMin_DBS-040to100cm_P1M.json

## List of variables

* Accumulation of quick response flux, runoff (kg/m²)
* Drainage accumulation, i.e., the vertical flow at the base of the deepest soil layer considered for routing (kg/m²)
* Snow depth at ground level (cm) 
* Water equivalent of the snow cover at ground level (kg/m²)
* Soil liquid water content (m³/m³)
* Air Temperature (°C)
* Dew point temperature (°C)

Each variable is associated with a statistic, i.e. the annual/monthly average (`YAvg/MAvg)`, the annual/monthly minimum (`YMin/MMin`) or the annual/monthly maximum (`YMax/MMax`)

Examples:

* `SnowWaterEquiv-YAvg`
* `DewPoint-MMin`

## Support

If you have any questions about this data, please [contact us](https://weather.gc.ca/mainmenu/contact_us_e.html).

## Announcements from the dd_info mailing list

Announcements related to this dataset are available via the [dd_info list](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).














