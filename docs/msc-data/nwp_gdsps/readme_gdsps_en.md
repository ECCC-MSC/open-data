[En français](readme_gdsps_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > GDSPS

# Data and Products of the Global Deterministic Storm Surge Prediction System (GDSPS)

The Global Deterministic storm Surge Prediction System (GDSPS) produces water level forecasts using a modified version of the NEMO ocean model (Wang et al. 2021, 2022, 2023). It provides 240 hours forecasts twice per day on a 1/12° resolution grid (3-9 km). The model is forced by the 10 meters winds, sea level pressure, ice concentration, ice velocity and surface currents from the [Global Deterministic Prediction System (GDPS)](../nwp_gdps/readme_gdps_en.md). The three dimensionnal ocean temperature and salinity fields of the model are nudged to values provided by the [Global Ice-Ocean Prediction System (GIOPS)](../nwp_giops/readme_giops_en.md) and the GDPS. During the post-processing phase, storm surge elevation (ETAS) is derived from total water level (SSH) by harmonic analysis using t_tide (Foreman et al. 2009).

## Access

### How to access the data

This data is available on the [MSC Datamart](../../msc-datamart/readme_en.md) data server service:

* [Data available via the GeoMet-Weather geospatial web services](readme_gdsps-geomet_en.md)
* [NetCDF data available on the MSC Datamart](readme_gdsps-datamart_en.md)

An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is available.

### Licence

The [end-user licence for Environment and Climate Change Canada's data servers](../../licence/readme_en.md) specifies the conditions of use of this data.

### MSC Open Data Service Usage Policy

The [MSC Open Data Service Usage Policy](../../usage-policy/readme_en.md) determines what constitutes an acceptable use of MSC Open Data services and provides users best practices for optimal use.

### Metadata

* The [metadata of the Global Deterministic Storm Surge Prediction System is available on the Open Government Portal](https://open.canada.ca/data/en/dataset/d244c9fa-776f-446f-9ccf-1d575cc21a5c).

## Technical documentation

* [Current version of the Global Deterministic Storm Surge Prediction System](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_specifications/tech_specifications_GDSPS_e.pdf)
* [Technical Note](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_notes/technote_gdsps_e.pdf)
* [Diagram of dependencies](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwep-dependency-diagrams/system_GDSPS_en.svg)

## Changelog

The chronology of changes to the Global Deterministic Storm Surge Prediction System (GDSPS) is available [here](changelog_gdsps_en.md).
