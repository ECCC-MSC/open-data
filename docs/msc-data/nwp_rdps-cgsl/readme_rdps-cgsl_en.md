[En français](readme_rdps-cgsl_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > Atmosphere-Ocean-Ice forecast system for the Gulf of St. Lawrence

# Data and products of the Atmosphere-Ocean-Ice forecast system for the Gulf of St. Lawrence

## Description of the system

The Regional Deterministic Prediction System - Coupled to Gulf of St. Lawrence (RDPS-CGSL) carries out physics calculations to arrive at deterministic analyses of sea ice and ocean elements for the current day. The Ocean-Ice forecast system for the Gulf of St. Lawrence is a circulation model to provide an estimate of current conditions over the gulf. Sea ice and ocean elements include ocean temperature, salinity, currents, sea surface height, sea ice concentration and thickness, ice drift and others. This product contains raw numerical results of these calculations. Geographical coverage is centered on the Gulf of the St. Lawrence. Data is available at a horizontal resolution of 5 km. Data is only available for the surface level. Predictions are performed up to four times a day.

### Technical Native Grid Specifications (Computational Domain)

The atmospheric component is a limited area configuration (LAM) of the Regional Deterministic Prediction System (RDPS) centered over the Gulf of St. Lawrence (GSL). This grid has 360 x 400 points in the horizontal with a spacing of 10 km (0.09 degrees) on a rectangular latitude-longitude projection. The required lateral boundary conditions for this model configuration are taken at every hour from the operational RDPS forecasts at the same resolution (0.09 degrees).

For the oceanic component, the system uses the NEMO model (Nucleus fro European Modeling of the Ocean) 
which includes a 3D oceanic circulation model taking into account the tides and freshwater inflows of 
rivers. The CICE (Community of Ice CodE) model is used for the sea-ice component. The NEMO-CICE 
domain consists of a 149 x 236 grid in the horizontal direction and extends from the Cabot Strait 
and Belle Isle Strait to Quebec City and to the head of the Saguenay Fjord near Tadoussac. A 
one-dimensional hydrological model is used from Montreal to Quebec City to absorb tides. The 
horizontal resolution is 5 km on a rotated-Mercator projection. The ocean is layered in the vertical 
with a uniform resolution of 5 m down to 300 m depth and 10 m further below. The surface and bottom 
layers are adjusted to the water level and local depth respectively. The boundary conditions for 
river runoffs, temperature and salinity are taken from climatological data and tides are implicitly 
calculated (Saucier et al. [2003]). 

## Access

### How to access the data

This data is available on the [MSC Datamart](../../msc-datamart/readme_en.md) data server service as well as [MSC GeoMet](../../msc-geomet/readme_en.md):

* [GRIB2 data available on the MSC Datamart](readme_rdps-cgsl-datamart_en.md) 
* [Data available via geospatial web services GeoMet-Weather](../../msc-geomet/readme_en.md)

An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is available.

### Licence

The [end-user licence for Environment and Climate Change Canada's data servers](../../licence/readme_en.md) specifies the conditions of use of this data.

### MSC Open Data Service Usage Policy

The [MSC Open Data Service Usage Policy](../../usage-policy/readme_en.md) determines what constitutes an acceptable use of MSC Open Data services and provides users best practices for optimal use.

### Metadata

Upcoming.

## Technical documentation

* [Technical Note](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/lib/technote_rdps-cgsl_e.pdf)

## Changelog

The chronology of changes to the Atmosphere-Ocean-Ice forecast system for the Gulf of St. Lawrence (RDPS-CGSL) is available [here](changelog_rdps-cgsl_en.md).
