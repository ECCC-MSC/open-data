[En français](readme_cmip6_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > CMIP6

# Data and products of the climate scenarios datasets based on an ensemble of global climate model projections from the Coupled Model Intercomparison Project Phase 6 (CMIP6)  

Multi-model ensembles for a suite of variables based on projections from Coupled Model Intercomparison Project Phase 6 (CMIP6) global climate models (GCMs) are available for 1850-2100 on a common 1x1 degree global grid.

Climate projections vary across GCMs due to differences in the representation and approximation of earth systems and processes, and natural variability and uncertainty regarding future climate drivers. Thus, there is no single best climate model. Rather, using results from an ensemble of models (e.g., taking the average) is best practice, as an ensemble takes model uncertainty into account and provides more reliable climate projections.

Provided on Canadian Climate Data and Scenarios (CCDS) are four types of products based on the CMIP6 multi-model ensembles: time series datasets and plots, maps and associated datasets, tabular datasets, and global gridded datasets. Monthly, seasonal, and annual ensembles are available for up to six Shared Socioeconomic Pathways (SSPs) (SSP1-1.9, SSP1-2.6, SSP2-4.5, SSP3-7.0, SSP4-6.0, and SSP5-8.5), four future periods (near-term (2021-2040), mid-term (2041-2060 and 2061-2080), end of century (2081-2100)), and up to five percentiles (5th, 25th, 50th (median), 75th, and 95th) of the CMIP6 ensemble distribution.

The number of models in each ensemble differs according to model availability for each SSP and variable, see the model list resource for details on the models included in each ensemble. The majority of products show projected changes expressed as anomalies according to a historical reference period of 1995-2014. The products provided include global, national, and provincial/territorial datasets and graphics. For more information on the CMIP6 multi-model ensembles, see the technical documentation resource. 

## Access
### How to access the data

This data is available from the [MSC GeoMet](../../msc-geomet/readme_en.md) API / web services and on the [MSC Datamart](../../msc-datamart/readme_en.md) data server:

* [Data available on the GeoMet-Climate geospatial web services](readme_cmip6-geomet_en.md)
* [NetCDF data available on the MSC Datamart](readme_cmip6-datamart_en.md)

An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is available. Example of a web map configured to display the [CMIP6-SSP585_AirTempAnomaly-Pct50_2081-2100_P0Y](https://geo.weather.gc.ca/geomet-climate?service=WMS&version=1.3.0&request=GetCapabilities&layer=CMIP6-SSP585_AirTempAnomaly-Pct50_2081-2100_P0Y) layer served by MSC GeoMet:

<div id="map" style="height: 400px; position: relative">
  <div id="legend-popup">
  <div id="legend-popup-content">
    <img id="legend-img" src="https://geo.weather.gc.ca/geomet-climate?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=CMIP6-SSP585_AirTempAnomaly-Pct50_2081-2100_P0Y&format=image/png&STYLE=TEMP-ANOMALIES"/>
  </div>
</div>
</div>
<div id="controller" role="group" aria-label="Animation controls" style="background: #ececec; padding: 0.5rem;">
  <button id="exportmap" class="btn btn-primary btn-sm" type="button"><i class="fa fa-download" style="padding: 0rem 1rem"></i></button>
  <a id="image-download" download="msc-geomet_web-map_export.png"></a>
</div>

### Licence

The [end-user licence for Environment and Climate Change Canada's data servers](../../licence/readme_en.md) specifies the conditions of use of this data.

### MSC Open Data Service Usage Policy

The [MSC Open Data Service Usage Policy](../../usage-policy/readme_en.md) determines what constitutes an acceptable use of MSC Open Data services and provides users best practices for optimal use.

### Discovery metadata

* The [CMIP6 multi-model ensembles metadata is available on the Open Government Portal](https://catalogue.ec.gc.ca/geonetwork/srv/eng/catalog.search#/metadata/7e7337b7-d36c-4486-a8df-16609a6b99bd)

## Technical documentation

* [Technical note](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/climate_cmip6/CMIP6_Technical_Documentation_en.pdf)
* [Information on Representative Concentration Pathways](http://climate-scenarios.canada.ca/?page=scen-rcp )
* [Introduction to climate scenarios](http://climate-scenarios.canada.ca/?page=cmip6-scenarios)
* This data is also available through the [Canadian Climate Services Centre](https://www.canada.ca/en/environment-climate-change/services/climate-change/canadian-centre-climate-services/about.html)


<style>
  #legend-img {
    margin: 0px;
    height:280px;
  }
  #legend-popup {
    position: absolute;
    top: 40px;
    right: 8px;
    z-index: 2;
  }
  .legend-switch{
    top: 8px;
    right: .5em;
  }
  .ol-touch .legend-switch {
    top: 80px;
  }
</style>

<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/ol@v7.3.0/ol.css" type="text/css"/>
<script src="https://cdn.polyfill.io/v2/polyfill.min.js?features=requestAnimationFrame,Element.prototype.classList,URL"></script>
<script src="https://cdn.jsdelivr.net/npm/ol@v7.3.0/dist/ol.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/FileSaver.js/1.3.3/FileSaver.min.js"></script>
<script>
    function isIE() {
      return window.navigator.userAgent.match(/(MSIE|Trident)/);
    }
    var head = document.getElementsByTagName('head')[0];
    var js = document.createElement("script");
    js.type = "text/javascript";
    if (isIE())
    {
        js.src = "../../../js/cmip6_ie.js";
        document.getElementById("controller").setAttribute("hidden", true);
    }
    else
    {
        js.src = "../../../js/cmip6.js";
    }
    head.appendChild(js);
</script>
