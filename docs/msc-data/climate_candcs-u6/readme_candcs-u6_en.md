[En français](readme_candcs-u6_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > CanDCS-U6

# Data and products of the Statistically downscaled climate scenarios from CMIP6 global climate models (CanDCS-U6)  

Environment and Climate Change Canada’s (ECCC) Climate Research Division (CRD) and the Pacific Climate Impacts Consortium (PCIC) previously produced statistically downscaled climate scenarios based on simulations from climate models that participated in the Coupled Model Intercomparison Project phase 5 (CMIP5) in 2015. ECCC and PCIC have now updated the CMIP5-based downscaled scenarios with two new sets of downscaled scenarios based on the next generation of climate projections from the Coupled Model Intercomparison Project phase 6 (CMIP6). The scenarios are named Canadian Downscaled Climate Scenarios–Univariate method from CMIP6 (CanDCS-U6) and Canadian Downscaled Climate Scenarios–Multivariate method from CMIP6 (CanDCS-M6).

CMIP6 climate projections are based on both updated global climate models and new emissions scenarios called “Shared Socioeconomic Pathways” (SSPs). Statistically downscaled datasets have been produced from 26 CMIP6 global climate models (GCMs) under three different emission scenarios (i.e., SSP1-2.6, SSP2-4.5, and SSP5-8.5). The CanDCS-U6 was downscaled using the Bias Correction/Constructed Analogues with Quantile mapping version 2 (BCCAQv2) procedure, and the CanDCS-M6 was downscaled using the N-dimensional Multivariate Bias Correction (MBCn) method. The CanDCS-U6 dataset was produced using the same downscaling target data (NRCANmet) as the CMIP5-based downscaled scenarios, while the CanDCS-M6 dataset implements a new target dataset (ANUSPLIN and PNWNAmet blended dataset).

Statistically downscaled individual model output are available for download. Downscaled climate indices are available across Canada at 10km grid spatial resolution for the 1950-2014 historical period and for the 2015-2100 period following each of the three emission scenarios.

Note: projected future changes by statistically downscaled products are not necessarily more credible than those by the underlying climate model outputs. In many cases, especially for absolute threshold-based indices, projections based on downscaled data have a smaller spread because of the removal of model biases. However, this is not the case for all indices. Downscaling from GCM resolution to the fine resolution needed for impacts assessment increases the level of spatial detail and temporal variability to better match observations. Since these adjustments are GCM dependent, the resulting indices could have a wider spread when computed from downscaled data as compared to those directly computed from GCM output. In the latter case, it is not the downscaling procedure that makes future projection more uncertain; rather, it is indicative of higher variability associated with finer spatial scale.

Individual model datasets and all related derived products are subject to the terms of use (https://pcmdi.llnl.gov/CMIP6/TermsOfUse/TermsOfUse6-1.html) of the source organization.

## Access

### How to access the data

This data is available from the [MSC GeoMet](../../msc-geomet/readme_en.md) API / web services and on the [MSC Datamart](../../msc-datamart/readme_en.md) data server:

* [Data available on the GeoMet-Climate geospatial web services](readme_candcs-u6-geomet_en.md)
* [NetCDF data available on the MSC Datamart](readme_candcs-u6-datamart_en.md)

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

### Metadata

* The [statistically downscaled climate scenarios from CMIP6 global climate models metadata is available on the Open Government Portal](https://catalogue.ec.gc.ca/geonetwork/srv/eng/catalog.search#/metadata/f73d6939-912a-4add-a291-c233fc5d1946)

## Technical documentation

* [Technical note](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/climate_candcsu6/CanDCS-U6_Technical_Documentation_en.pdf)
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
