[En français](readme_radar_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > Radar imagery

# Data and products for weather radar observations

This page describes the data and products available for Environment and Climate Change Canada's weather radar network. The network is comprised of 33 sites concentrated in the most populated parts of Canada, and provides radar coverage to more than 95 per cent of Canadians. The network’s primary purpose is the early detection of developing thunderstorms and high impact weather, as well the tracking of precipitation.

## Access

### How to access the data

Weather radar data is available from the MSC GeoMet API and web services as well as static GIF images on the MSC Datamart:

* [Radar layers available via geospatial web services on GeoMet-Weather](readme_radar_geomet_en.md):
    * North American radar composite
    * North American radar surface precipitation type [experimental]
    * North American radar extrapolation [experimental]
* [GIF radar imagery available on the MSC Datamart](readme_radarimage-datamart_en.md) 

An [overview and examples on how to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is available. Example of a web map configured to display weather radar composite and extrapolation Web Map Service (WMS) layers served by MSC GeoMet:

<div id="map" style="height: 400px;"></div>
<div id="controller" role="group" aria-label="Animation controls" style="background: #ececec; padding: 0.5rem;">
  <button id="fast-backward" class="btn btn-primary btn-sm" type="button"><i class="fa fa-fast-backward" style="padding: 0rem 1rem"></i></button>
  <button id="step-backward" class="btn btn-primary btn-sm" type="button"><i class="fa fa-step-backward" style="padding: 0rem 1rem"></i></button>
  <button id="play-pause" class="btn btn-primary btn-sm" type="button"><i class="fa fa-play" style="padding: 0rem 1rem"></i></button>
  <button id="step-forward" class="btn btn-primary btn-sm" type="button"><i class="fa fa-step-forward" style="padding: 0rem 1rem"></i></button>
  <button id="fast-forward" class="btn btn-primary btn-sm" type="button"><i class="fa fa-fast-forward" style="padding: 0rem 1rem"></i></button>
  <button id="exportmap" class="btn btn-primary btn-sm" type="button"><i class="fa fa-download" style="padding: 0rem 1rem"></i></button>
  <a id="image-download" download="msc-geomet_web-map_export.png"></a>
  <span id="info" style="padding-left: 0.5rem;"></span>
</div>

### Licence

The [end-user licence for Environment and Climate Change Canada's data servers](../../licence/readme_en.md) specifies the conditions of use for this data.

### MSC Open Data Service Usage Policy

The [MSC Open Data Service Usage Policy](../../usage-policy/readme_en.md) determines what constitutes an acceptable use of MSC Open Data services and provides users best practices for optimal use.

### Metadata

Upcoming.

## Technical documentation

* [About radar](https://www.canada.ca/en/environment-climate-change/services/weather-general-tools-resources/radar-overview/about.html)
* [Modernizing Canada's weather-radar network](https://www.canada.ca/en/environment-climate-change/services/weather-general-tools-resources/radar-overview/modernizing-network.html)
* [Radar outages and maintenance](https://www.canada.ca/en/environment-climate-change/services/weather-general-tools-resources/radar-overview/outages-maintenance.html)
* Radar product guide - __to come__

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
        js.src = "../../../js/radar_ie.js";
        document.getElementById("controller").setAttribute("hidden", true);
    }
    else
    {
        js.src = "../../../js/radar.js";
    }
    head.appendChild(js);
</script>