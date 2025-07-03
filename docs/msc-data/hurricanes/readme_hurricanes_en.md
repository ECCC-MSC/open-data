[En français](readme_hurricanes_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > Hurricanes

# Hurricane prediction data and products

Hurricane tracks and the hurricane response zone are issued by the [Canadian Hurricane Centre](https://www.canada.ca/en/environment-climate-change/services/hurricane-forecasts-facts/products.html), which provides track forecasts for tropical and post-tropical cyclones that pose a threat to Canada during the hurricane season, from June to November.

## Access

### How to access the data

This data is available on the [MSC GeoMet](../../msc-geomet/readme_en.md) API and on the [MSC Datamart](../../msc-datamart/readme_en.md) data server:

* [Hurricane response zone and trajectories available on the GeoMet-Weather web services](readme_hurricanes_geomet_en.md)
* [Trajectories data available on the MSC Datamart](readme_hurricanes-datamart_en.md)

An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is available.

Example of a web map displaying the hurricane response zone and active hurricanes Web Map Service (WMS) layers, along with weather alerts and precipitation layers, served by MSC GeoMet:

<div id="map" style="height: 400px; position: relative">
  <div id="legend-popup">
  <div id="legend-popup-content">
    <img id="legend-img" src="https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=HURRICANE_RESPONSE_ZONE&format=image/png&STYLE=HURRICANE_LINE_BLACK_DASHED"/>
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

Upcoming.

## Products

* [Hurricane track maps](https://weather.gc.ca/hurricane/track_e.html)
* [Canadian Hurricane Centre: forecasts and products](https://www.canada.ca/en/environment-climate-change/services/hurricane-forecasts-facts/products.html)

## Technical documentation

* [Canadian Hurricane Centre](https://www.ec.gc.ca/ouragans-hurricanes/)

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
        js.src = "../../../js/hurricane_ie.js";
        document.getElementById("controller").setAttribute("hidden", true);
    }
    else
    {
        js.src = "../../../js/hurricane.js";
    }
    head.appendChild(js);
</script>
