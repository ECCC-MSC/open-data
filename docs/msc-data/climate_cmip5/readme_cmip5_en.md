[En français](readme_cmip5_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > CMIP5

# Data and products of the climate scenarios datasets based on an ensemble of global climate model projections from the Coupled Model Intercomparison Project Phase 5 (CMIP5)  

The Global climate model scenarios dataset is based on an ensemble of global climate model projections from the Coupled Model Intercomparison Project Phase 5 (CMIP5) are provided. Multi-model ensembles of modelled output (actual value) and projected change (anomaly) are available for historical simulations and three emission scenarios at a 1x1 degree grid resolution. Projected changes are expressed as anomalies with respect to the reference period of 1986-2005. A range of percentiles across the multi-model ensembles are available for download.

## Access

### How to access the data

This data is available from the [MSC GeoMet](../../msc-geomet/readme_en.md) API / web services and on the [MSC Datamart](../../msc-datamart/readme_en.md) data server:

* [Data available from the GeoMet-Climate API / geospatial web services](readme_cmip5-geomet_en.md)
* [NetCDF data available on the MSC Datamart](readme_cmip5-datamart_en.md)

An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is available. Example of a web map configured to display the [CMIP5.TT.HISTO.SUMMER.ABS_PCTL50](https://geo.weather.gc.ca/geomet-climate?service=WMS&version=1.3.0&request=GetCapabilities&layer=CMIP5.TT.HISTO.SUMMER.ABS_PCTL50) layer served by MSC GeoMet:

<div id="map" style="height: 400px;"></div>
<div id="controller" role="group" aria-label="Animation controls" style="background: #ececec; padding: 0.5rem;">
  <button id="exportmap" class="btn btn-primary btn-sm" type="button"><i class="fa fa-download" style="padding: 0rem 1rem"></i></button>
</div>

### Licence

The [end-user licence for Environment and Climate Change Canada's data servers](../../licence/readme_en.md) specifies the conditions of use of this data.

### Metadata

* The [metadata of the projected temperature change based on CMIP5 multi-model ensembles are available on the Open Government Portal](https://open.canada.ca/data/en/dataset/1e86f4f7-da88-403e-bd44-92065c0fd568)
* The [metadata of the projected precipitation change based on CMIP5 multi-model ensembles are available on the Open Government Portal](https://open.canada.ca/data/en/dataset/eddd6eaf-34d7-4452-a994-3d928115a68b)
* The [metadata of the projected Snow Depth change based on CMIP5 multi-model ensembles are available on the Open Government Portal](https://open.canada.ca/data/en/dataset/0933f0dc-3625-4583-828a-86d032e4b737)
* The [metadata of the projected sea ice thickness change based on CMIP5 multi-model ensembles are available on the Open Government Portal](https://open.canada.ca/data/en/dataset/b6a68b05-58f3-4d71-89d8-25b5a5277796)
* The [metadata of the projected sea ice concentration change based on CMIP5 multi-model ensembles are available on the Open Government Portal](https://open.canada.ca/data/en/dataset/78f9e3e0-3a12-4321-99dd-eed047c31e5e)
* The [metadata of the projected surface wind speed change based on CMIP5 multi-model ensembles are available on the Open Government Portal](https://open.canada.ca/data/en/dataset/e0c71149-db7a-4700-acfd-1c8f9d778354)

## Technical documentation

* [Technical note](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/climate_cmip5/CMIP5_Technical_Documentation_en.pdf)
* [Information on Representative Concentration Pathways](http://climate-scenarios.canada.ca/?page=scen-rcp )
* [Introduction to climate scenarios](http://climate-scenarios.canada.ca/?page=cmip5-intro)
* This data is also available through the [Canadian Climate Services Centre](https://www.canada.ca/en/environment-climate-change/services/climate-change/canadian-centre-climate-services/about.html)


<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/openlayers/4.6.5/ol.css" integrity="sha256-rQq4Fxpq3LlPQ8yP11i6Z2lAo82b6ACDgd35CKyNEBw=" crossorigin="anonymous" />
<script src="https://cdn.polyfill.io/v2/polyfill.min.js?features=requestAnimationFrame,Element.prototype.classList,URL"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/openlayers/4.6.5/ol.js" integrity="sha256-77IKwU93jwIX7zmgEBfYGHcmeO0Fx2MoWB/ooh9QkBA=" crossorigin="anonymous"></script>
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
        js.src = "../../../js/cmip5_ie.js";
        document.getElementById("controller").setAttribute("hidden", true);
    }
    else
    {
        js.src = "../../../js/cmip5.js";
    }
    head.appendChild(js);
</script>
