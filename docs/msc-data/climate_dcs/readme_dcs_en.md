[En français](readme_dcs_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > DCS

# Data and products of statistically downscaled climate scenarios datasets based on an ensemble of global climate model projections from the Coupled Model Intercomparison Project Phase 5 (CMIP5)  

The Statistically downscaled climate scenarios dataset provides projected changes in temperature and precipitation, with respect to the reference period of 1986-2005, for three emission scenarios, RCP2.6, RCP4.5, RCP8.5, at a 10km resolution. Downscaled data are based on global climate model projections from the Coupled Model Intercomparison Project Phase 5 (CMIP5). The median projected changes across the downscaled multi-model ensemble are shown.

## Access

### How to access the data

This data is available from the [MSC GeoMet](../../msc-geomet/readme_en.md) API / web services and on the [MSC Datamart](../../msc-datamart/readme_en.md) data server:

* [Data available from the GeoMet-Climate API / geospatial web services](readme_dcs-geomet_en.md)
* [NetCDF data available on the MSC Datamart](readme_dcs-datamart_en.md)

An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is available. Example of a web map configured to display the [DCS.PR.RCP26.YEAR.2021-2040_PCTL50](https://geo.weather.gc.ca/geomet-climate?service=WMS&version=1.3.0&request=GetCapabilities&layer=DCS.PR.RCP26.YEAR.2021-2040_PCTL50) layer served by MSC GeoMet:

<div id="map" style="height: 400px;"></div>
<div id="controller" role="group" aria-label="Animation controls" style="background: #ececec; padding: 0.5rem;">
  <button id="exportmap" class="btn btn-primary btn-sm" type="button"><i class="fa fa-download" style="padding: 0rem 1rem"></i></button>
</div>

### Licence

The [end-user licence for Environment and Climate Change Canada's data servers](../../licence/readme_en.md) specifies the conditions of use of this data.

### Metadata

* The [metadata of the statistically downscaled scenarios of projected mean temperature change are available on the Open Government Portal](https://open.canada.ca/data/en/dataset/958b8357-3690-414d-8bec-d65951041636).
* The [metadata of the statistically downscaled scenarios of projected maximum temperature change are available on the Open Government Portal](https://open.canada.ca/data/en/dataset/57fee0af-40ec-4aad-89da-6c0d39a6424d).
* The [metadata of the statistically downscaled scenarios of projected minimum temperature change are available on the Open Government Portal](https://open.canada.ca/data/en/dataset/3156e7bf-6f11-46f7-b70a-51b6d4e3835b).
* The [metadata of the statistically downscaled scenarios of projected total precipitation change are available on the Open Government Portal](https://open.canada.ca/data/en/dataset/286dd106-b507-472a-9a26-f72dceffb475).

## Technical documentation

* [Technical note](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/climate_dcs/DCS_Technical_Documentation_en.pdf)
* [Statistically downscaled climate scenarios](http://climate-scenarios.canada.ca/?page=statistical-downscaling)
* [Introduction to climate scenarios](http://climate-scenarios.canada.ca/index.php?page=cmip5-intro)
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
        js.src = "../../../js/dcs_ie.js";
        document.getElementById("controller").setAttribute("hidden", true);
    }
    else
    {
        js.src = "../../../js/dcs.js";
    }
    head.appendChild(js);
</script>
