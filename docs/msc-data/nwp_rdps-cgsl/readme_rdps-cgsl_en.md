[En français](readme_rdps-cgsl_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > Atmosphere-Ocean-Ice forecast system for the Gulf of St. Lawrence

# Data and products of the Atmosphere-Ocean-Ice forecast system for the Gulf of St. Lawrence

## Description of the system

The Atmosphere-Ocean-Ice forecast system for the Gulf of St. Lawrence is a circulation model to better understand Canadian inland seas. This system includes two main parts:

* An oceanic pseudo-analysis cycle (Smith et al., 2012) including a superimposed sea ice analysis based on direct insertion of Radarsat image analyses (Smith et al., 2012).
* A coupled forecast cycle.

Note that the coupled forecast cycle is a 48 hour simulation based on 00, 06, 12 and 18 UTC data where both of its models (LAM and OCEAN-ICE) run at the same time. It provides 00-48 hour weather, sea ice and ocean forecasts.

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

These data are available on the data server services [MSC Datamart](../../msc-datamart/readme_en.md) and the web services [MSC GeoMet](../../msc-geomet/readme_en.md) respectively :

* [GRIB2 data available on the MSC Datamart](readme_rdps-cgsl-datamart_en.md) 
* [Data available via geospatial web services GeoMet-Weather](../../msc-geomet/readme_en.md)

An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is available.

### Licence

The [end-user licence for Environment and Climate Change Canada's data servers](../../licence/readme_en.md) specifies the conditions of use of these data.


### Metadata

Upcoming.

## Technical documentation

* [Technical Note](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/lib/technote_rdps-cgsl-300_20141118_e.pdf)

## Change log

The chronology of changes to operational systems is available [here](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/changes_e.html).
