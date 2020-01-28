[In French](readme_wcps_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > WCPS

# Data and products of the Water Cycle Prediction System (WCPS)

The Water Cycle Prediction System (WCPS) simulates the complete water cycle, following water as it moves from the atmosphere to the surface, through the river network and into lakes, and back to the atmosphere. WCPS was implemented over the Laurentian Great Lakes and St. Lawrence River watershed in support of Canada's obligations under the Boundary Waters Treaty (International Joint Commission 2016). 

WCPS is a chaine of interconnected models.  The models represent processes in the atmopshere, at the land surface and in the soil (at 10-km resolution), in large bodies of water and marine ice (at 2-km resolution), and in rivers (at 1-km resolution). WCPS produces two forecasts per day for the next three and a half days (84 hours)

The Reginal Deterministic Prediction System (RDPS) provides initial and boundary conditions to a limited area version of GEM-LAM covering eastern North America. Every 7 minutes, GEM-LAM communicates with the ocean-ice model, NEMO-CICE, wihich is set up on the Great Lakes, namely Lakes Superior, Michigan-Huron, St. Claire, Erie, and Ontario. GEM-LAM informs NEMO of the precipitation that has landed on the surface of the lakes and of the state of the near-surface atmosphere. NEMO informs GEM-LAM of the surface water temperature, the extent of the ice cover, and the fluxes of latent and sensible heat and momentum. GEM-LAM also provides hourly estimates of surface runoff to the river routing model, WATROUTE. In turn, WATROUTE informes NEMO of the terrestrial runoff. 

## Access

### How to access the data 

These data are available on the data server services [MSC Datamart](../../msc-datamart/readme_en.md) and the web services [MSC GeoMet](../../msc-geomet/readme_en.md) respectively :

* [WCPS NEMO NetCDF data available on the MSC Datamart](readme_wcps_nemo-datamart_en.md) 
* [Data available via geospatial web services GeoMet-Weather](../../msc-geomet/readme_en.md)

An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is available.

### Licence

The [end-user licence for Environment and Climate Change Canada's data servers](../../licence/readme_en.md) specifies the conditions of use of these data.


### Metadata

To come.

## Technical documentation

* [Current version of the Water Cycle Prediction System (WCPS)](http://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_specifications/tech_specifications_WCPS_e.pdf)
* [Technical note](http://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_notes/technote_wcps_e.pdf)

## Change log 

The chronology of changes to the Water Cycle Prediction System (WCPS) is available [here](changelog_wcps_en.md).

