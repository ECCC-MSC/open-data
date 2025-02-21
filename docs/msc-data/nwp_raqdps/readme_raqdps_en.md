[En français](readme_raqdps_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > RAQDPS

# Data and Products of the Regional Air Quality Deterministic Prediction System 

The Regional Air Quality Deterministic Prediction System (RAQDPS) takes into account physical and chemical processes to produce deterministic forecasts of the concentration of chemical species of interest to air quality. These chemical constituents include gases such as O3, SO2, NO, and NO2, in addition to fine particles PM2.5 (diameter of 2.5 micrometers or less) and coarse particles PM10 (diameter of 10 micrometers or less). The PM2.5 and PM10 now include the contribution of wildfire emissions as well as anthropogenic and biogenic emission sources. The forecasts are available for the present up to 72 hours in the future twice a day (run 00 UTC and 12 UTC). The geographic domain of the RAQDPS covers most of North America with a horizontal resolution of 10km.

## Access

### How to access the data

This data is available from the [MSC GeoMet](../../msc-geomet/readme_en.md) API / web services and the [MSC Datamart](../../msc-datamart/readme_en.md) data server:

* [Data available via the GeoMet-Weather geospatial web services](readme_raqdps-geomet_en.md)
* [GRIB2 data available on the MSC Datamart](readme_raqdps-datamart_en.md) 

An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is available. Example of a web map configured to display the `RAQDPS.SFC_NO2` layer served by MSC GeoMet:

<div id="map" style="height: 400px; position: relative">
  <div id="legend-popup">
  <div id="legend-popup-content">
    <img id="legend-img" src="https://geo.weather.gc.ca/geomet?SERVICE=WMS&VERSION=1.3.0&SLD_VERSION=1.1.0&REQUEST=GetLegendGraphic&FORMAT=image/png&LAYER=RAQDPS.SFC_NO2&STYLE=SFC-NO2_PPBV"/>
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

### Metadata

Upcoming.

## Products

* [Maps of 48 hours forecasts](https://weather.gc.ca/aqfm/index_e.html) for tropospheric ozone near the surface and at altitudes of 50 metres and 500 metres, and for PM2.5 and PM10 near the surface. 
* [For-panels maps](https://weather.gc.ca/aqfm/index_e.html) forecasts for PM2.5, PM10, and ozone near the surface and for ozone at 500 metres.

## Technical documentation

* [Actual version of the Regional Air Quality Deterministic Prediction System](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_RAQDPS_e.pdf)
* [Technical note](http://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_notes/technote_raqdps_e.pdf)
* [Diagram of dependencies](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwep-dependency-diagrams/system_RAQDPS_FW_en.svg)
* [Factsheet associated with the latest innovation cycle](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/fact_sheets/factsheet_raqdps_e.pdf)

## Changelog

The chronology of changes to operational systems is available [in the changelog](changelog_raqdps_en.md).

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
        js.src = "../../../js/raqdps_ie.js";
        document.getElementById("controller").setAttribute("hidden", true);
    }
    else
    {
        js.src = "../../../js/raqdps.js";
    }
    head.appendChild(js);
</script>
