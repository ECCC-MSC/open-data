[En français](readme_rdaqa_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > RDAQA

# Data and Products of the Regional Deterministic Air Quality Analysis 

Regional Deterministic Air Quality Analysis (RDAQA) is an objective analysis of surface pollutants that combines numerical forecasts from the Regional Air Quality Deterministic Prediction System (RAQDPS) with hourly observations from various monitoring networks in North America, including the Canadian measurement networks operated by the provinces, territories and certain cities, as well as the various American networks in the context of the AIRNow program administered by US/EPA (US Environmental Protection Agency). RDAQA analysis provides the best description of current air quality conditions, and is used to inform the public, meteorologists in the various Environment and Climate Change Canada forecasting offices, Health Canada and other users about the distribution of air pollutants near the ground, and the performance of forecasting models.

Each hour, a preliminary product is available approximately one hour after the observation measurement time, while final and Firework products are available approximately two hours after the measurement time. The preliminary and final products contain analysis of the chemical constituents O3, SO2, NO, NO2, PM2.5 (fine particles with diameters of 2.5 micrometers or less) and PM10 (coarse particles with diameters of 10 micrometers or less), while the Firework product contains analysis of PM2.5 and PM10.

## Access

### How to access the data

This data is available from the [MSC Datamart](../../msc-datamart/readme_en.md) raw data server and the [MSC GeoMet web services](../../msc-geomet/readme_en.md):

* [GRIB2 data available on the MSC Datamart](readme_rdaqa-datamart_en.md)
* [Data available via the GeoMet-Weather geospatial web services](readme_rdaqa-geomet_en.md)


An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is available. Example of a web map configured to display the [RDAQA_10km_PM10](https://geo.weather.gc.ca/geomet?service=WMS&version=1.3.0&request=GetCapabilities&layer=RDAQA_10km_PM10) layer served by MSC GeoMet:


<div id="map" style="height: 400px; position: relative">
  <div id="legend-popup">
  <div id="legend-popup-content">
    <img id="legend-img" style="display: flex; max-width: 85px;" src="https://geo.weather.gc.ca/geomet?lang=en&version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=RDAQA_10km_PM10&format=image/png&STYLE="/>
  </div>
</div>
</div>
<div id="controller" role="group" aria-label="Animation controls" style="background: #ececec; padding: 0.5rem;">
  <button id="fast-backward" class="btn btn-primary btn-sm" type="button"><i class="fa fa-fast-backward" style="padding: 0rem 1rem"></i></button>
  <button id="step-backward" class="btn btn-primary btn-sm" type="button"><i class="fa fa-step-backward" style="padding: 0rem 1rem"></i></button>
  <button id="play-pause" class="btn btn-primary btn-sm" type="button"><i class="fa fa-play" style="padding: 0rem 1rem"></i></button>
  <button id="step-forward" class="btn btn-primary btn-sm" type="button"><i class="fa fa-step-forward" style="padding: 0rem 1rem"></i></button>
  <button id="fast-forward" class="btn btn-primary btn-sm" type="button"><i class="fa fa-fast-forward" style="padding: 0rem 1rem"></i></button>
  <button id="exportmap" class="btn btn-primary btn-sm" type="button"><i class="fa fa-download" style="padding: 0rem 1rem"></i></button>
  <a id="image-download" download="msc-geomet_web-map_export.png"></a>
  <span id="info" style="padding-left: 0.5rem;cursor: pointer;"></span>
</div>


### Licence

The [end-user licence for Environment and Climate Change Canada's data servers](../../licence/readme_en.md) specifies the conditions of use of this data.

### MSC Open Data Service Usage Policy

The [MSC Open Data Service Usage Policy](../../usage-policy/readme_en.md) determines what constitutes an acceptable use of MSC Open Data services and provides users best practices for optimal use.

### Discovery metadata

The [metadata of the Regional Deterministic Air Quality Analysis is available on the Open Government Portal](https://open.canada.ca/data/en/dataset/1f11ed9f-b13d-497b-853a-997b991195a1)

## Technical documentation

* [Actual version of the Regional Deterministic Air Quality Analysis](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_RDAQA_e.pdf)
* [Technical note](http://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_notes/technote_rdaqa_e.pdf)
* [Diagram of dependencies](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwep-dependency-diagrams/system_RDAQA_FW_en.svg) 
* [Factsheet associated with the latest innovation cycle](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/fact_sheets/factsheet_rdaqa_e.pdf)

## Changelog

The chronology of changes to operational systems is available [in the changelog](changelog_rdaqa_en.md).



<style>
  #legend-img {
    margin: 0px;
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
        js.src = "../../../js/rdaqa_ie.js";
        document.getElementById("controller").setAttribute("hidden", true);
    }
    else
    {
        js.src = "../../../js/rdaqa.js";
    }
    head.appendChild(js);
</script>
