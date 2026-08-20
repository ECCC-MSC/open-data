[En français](readme_casr-rivers-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [Canadian Surface Reanalysis](readme_casr_en.md) > CaSR-Rivers derived products on the MSC Datamart

# Products derived from the Canadian Surface Reanalysis - Rivers (CaSR-Rivers)

This page describes the gridded statistical products in NetCDF format derived from the [Canadian Surface Reanalysis-Land (CaSR-Land)](https://hpfx.collab.science.gc.ca/~scar700/rcas-casr/overview_subproducts.html) available on the MSC Datamart.

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples for accessing and using the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available via the HTTPS protocol. It is possible to access ir with a standard browser. In this case, you obtain a list of links to a NetCDF.

Gridded statistical products derived from the Canadian Surface Reanalysis - Rivers (CaSR-Rivers) can be found at:

* [https://dd.weather.gc.ca/today/reanalysis_casr/casr-land/{Version}/post-processing/grid](https://dd.version.gc.ca/today/reanalysis_casr/casr-land/)

where:

* __Version__: [CaSR version](https://hpfx.collab.science.gc.ca/~scar700/rcas-casr/dataset_specifics.html#diff_casr_versions) of the Canadian Surface Reanalysis (e.g., v3.2)

## File name nomenclature 

The forecast files follow the nomenclature below:

`{YYY1-YYY2}_MSC_CaSR-Rivers-{version}_{Var}_{Level}_{Grid}{resolution}_{TimeStep}.nc`

where:

* __YYY1-YYY2__: Period covered by the reanalysis according to the version [1968–2024]
* __MSC__: Constant string for Meteorological Service of Canada, the data source
* __CaSR-Rivers__: A string indicating that the data is derived from Canadian Surface Reanalysis - Rivers
* __version__: [Version](https://hpfx.collab.science.gc.ca/~scar700/rcas-casr/dataset_specifics.html#diff_casr_versions) of the retest [v2.1, v3.2]
* __Var__: Variable name and associated statistics (see section below)
* __Level__: A string indicating the vertical level [`Sfc` for the surface]
* __Grille__ : Horizontal rotated lat-lon grid [Rlatlon]
* __resolution__: Resolution of 0.09° (about 10km) in the longitudinal and latitudinal directions [0.09]
* __TimeStep__: No time, taking one of the values [P1Y, P1M]; `P1Y` represents a one-year time step and `P1M` represents a one-month time step
* __nc__: Constant string indicating that the format is NetCDF

Examples:

* 1968-2024_MSC_CaSR-Rivers-v3.2_RiverDischarge-MMax_Sfc_RLatLon0.09_P1M.nc
* 1968-2024_MSC_CaSR-Rivers-v3.2_DeepReservoirStorage-YMin_Sfc_RLatLon0.09_P1Y.nc

## List of variables

* Streamflow discharge, Mean discharge value exiting the river channel over the hour ending at the indicated time (m³/s)
* Water stored in the river channelwater stored in the river channel (m³)
* Lower zone storage, depth of water contained in the lower zone storage (kg/m²)

Each variable is associated with a statistic, i.e. the annual/monthly average (`YAvg/MAvg)`, the annual/monthly minimum (`YMin/MMin`) or the annual/monthly maximum (`YMax/MMax`)

Examples:

* `RiverDischargeYAvg`
* `DeepReservoirStorage-MMin`

## Support

If you have any questions about this data, please [contact us](https://weather.gc.ca/mainmenu/contact_us_e.html).

## Announcements from the dd_info mailing list

Announcements related to this dataset are available via the [dd_info list](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).














