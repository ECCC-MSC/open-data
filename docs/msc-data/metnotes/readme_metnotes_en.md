[En français](readme_metnotes_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > MetNotes

# MetNotes data

This page describes the MetNotes which are short notes written by meteorologists that provide additional context to Environment and Climate Change Canada (ECCC)-produced weather forecasts. These brief messages may include possible impacts due to weather, an early heads-up on severe weather, or information to prepare people attending outdoor events affected by weather.

These notes are also available on [WeatherCAN](https://www.canada.ca/en/environment-climate-change/services/weather-general-tools-resources/weathercan.html) app.

## Access

### How to access the data

This data is available on the [MSC Datamart](../../msc-datamart/readme_en.md) data server services as well as [MSC GeoMet](../../msc-geomet/readme_en.md):

* [Data available via geospatial web services GeoMet-Weather](../../msc-geomet/readme_en.md)
* [GeoJSON data available on HPFX, the alternative server of the MSC Datamart](readme_metnotes-datamart_en.md)

An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is available.

Example of a web map configured to display the `METNOTES` layer served by MSC GeoMet:
<div id="map" style="height: 400px; margin-bottom: 1rem;"></div>
<div id="popup" class="ol-popup">
    <a href="#" id="popup-closer" class="ol-popup-closer"></a>
    <div id="popup-content"></div>
    <div id="nav" style="margin-top: 0.5rem">
        <div id="nav-btns">
            <button id="left-btn" class="btn btn-outline-primary btn-sm">
              <i class="fa fa-arrow-left" aria-hidden="true"></i>
            </button>
            <span style="width: 20px; height: auto; display:inline-block;"></span>
            <button type="button" id="right-btn" class="btn btn-outline-primary btn-sm">
              <i class="fa fa-arrow-right" aria-hidden="true"></i>
            </button>
        </div>
        <div style="margin-top: 0.25rem; font-size: 0.8rem;">
          <p id="nav-text" style="margin-bottom: 0rem;"></p>
        </div>
    </div>
</div>

### Licence

The [end-user licence for Environment and Climate Change Canada's data servers](../../licence/readme_en.md) specifies the conditions of use for this data.

### MSC Open Data Service Usage Policy

The [MSC Open Data Service Usage Policy](../../usage-policy/readme_en.md) determines what constitutes an acceptable use of MSC Open Data services and provides users best practices for optimal use.

### Metadata

Upcoming.

## Technical documentation

[FAQ](https://www.canada.ca/en/environment-climate-change/services/weather-general-tools-resources/weathercan/metnotes.html)

<style>
    .ol-popup {
      position: absolute;
      background-color: white;
      box-shadow: 0 1px 4px rgba(0, 0, 0, 0.2);
      padding: 15px;
      border-radius: 10px;
      border: 1px solid #cccccc;
      bottom: 12px;
      left: -50px;
      min-width: 300px;
      font-size: 0.8rem;
      line-height: 0.9rem;
    }

    .ol-popup:after,
    .ol-popup:before {
      top: 100%;
      border: solid transparent;
      content: " ";
      height: 0;
      width: 0;
      position: absolute;
      pointer-events: none;
    }

    .ol-popup:after {
      border-top-color: white;
      border-width: 10px;
      left: 48px;
      margin-left: -10px;
    }

    .ol-popup:before {
      border-top-color: #cccccc;
      border-width: 11px;
      left: 48px;
      margin-left: -11px;
    }

    .ol-popup-closer {
      text-decoration: none;
      position: absolute;
      top: 5px;
      right: 8px;
    }

    .ol-popup-closer:after {
      content: "✖";
      color: #A9A9A9;
    }

    .arrow {
      border: solid #2fa4e7;
      border-width: 0 3px 3px 0;
      display: inline-block;
      padding: 3px;
    }

    .right {
      transform: rotate(-45deg);
      -webkit-transform: rotate(-45deg);
    }

    .left {
      transform: rotate(135deg);
      -webkit-transform: rotate(135deg);
    }
</style>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/openlayers/openlayers.github.io@master/en/v6.14.1/css/ol.css" type="text/css"></link>
<script src="https://cdn.polyfill.io/v2/polyfill.min.js?features=requestAnimationFrame,Element.prototype.classList,URL"></script>
<script src="https://cdn.jsdelivr.net/gh/openlayers/openlayers.github.io@master/en/v6.14.1/build/ol.js"></script>
<script src="https://cdn.jsdelivr.net/npm/luxon@3.0.1/build/global/luxon.min.js" integrity="sha256-uQ0RrcqAQ8NxzNqZH11eXx3qFLAgwEgSQN1V0N1+UlM=" crossorigin="anonymous"></script>
<script src="../../../js/metnotes_en.js" type="text/javascript"></script>