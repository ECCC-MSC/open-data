[En français](readme_caps_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > CAPS experimental

# Data and Products of the experimental Canadian Arctic Prediction System (CAPS)

The Canadian Arctic Prediction System (CAPS) is an experimental coupled atmosphere-ocean-ice prediction system based on a limited-area configuration (LAM) of the Global Environmental Multiscale (GEM) model, coupled with the Nucleus of European Modeling of the Ocean (NEMO) and the Community ICe Code (CICE). It covers the entire Arctic basin with a horizontal grid resolution of approximately 3 km. The system CAPS is driven by ECCC's [Global Deterministic Prediction System (GDPS)](../nwp_gdps/readme_gdps_en.md), which provides initial and lateral boundary conditions for atmospheric fields. Initial hydrometeorological fields are recycled from the 12-hour forecast of the previous CAPS integration. In addition, the GDPS is used to force the ocean-ice model outside the coupled regions. Initial conditions for ocean-ice fields are taken from the [Regional Ocean-Ice Prediction System (RIOPS)](../nwp_riops/readme_riops_en.md). Ocean boundary conditions in the North Atlantic and North Pacific come from the GDPS. The system CAPS runs twice a day and is initialized at 00 and 12 UTC, respectively, with a 48-hour integration.

## Access

### How to access the data

This experimental data is available from the [MSC GeoMet](../../msc-geomet/readme_en.md) API / web services and on the [MSC Datamart](../../msc-datamart/readme_en.md) data server respectively:

* [Data available via the GeoMet-Weather geospatial web services](https://eccc-msc.github.io/open-data/msc-geomet/readme_en/)
* [GRIB2 and NetCDF data available on the MSC Datamart](readme_caps-datamart_en.md)
* [GRIB2 weather elements on the grid data available on the MSC testing data repository DD-Alpha](readme_caps-weong-datamart_en.md)

An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is available.

### Licence

The [end-user licence for Environment and Climate Change Canada's data servers](../../licence/readme_en.md) specifies the conditions of use of this data.

### MSC Open Data Service Usage Policy

The [MSC Open Data Service Usage Policy](../../usage-policy/readme_en.md) determines what constitutes an acceptable use of MSC Open Data services and provides users best practices for optimal use.

### Metadata

Upcoming.

## Technical documentation

* [Current version of the Canadian Arctic Prediction System](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_CAPS_e.pdf)
* [Diagram of dependencies](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwep-dependency-diagrams/system_CAPS_en.svg)
* [Technical Note](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_caps_e.pdf)
* [Weather elements on the grid (WEonG) technical Note](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_weong-hrdps_e.pdf)

## Changelog

The chronology of changes to the Regional Canadian Arctic Prediction System (CAPS) is available [here](changelog_caps_en.md).
