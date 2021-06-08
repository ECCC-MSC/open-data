[En français](readme_raqdps_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > RAQDPS

# Data and Products of the Regional Air Quality Deterministic Prediction System 

The Regional Air Quality Deterministic Prediction System (RAQDPS) carries out physics and chemistry calculations to arrive at deterministic predictions of chemical species concentration of interest to air quality. Chemical constituents include O3, SO2, NO and NO2, gases as well as fine particulate matter PM2.5 (2.5 micrometers in diameter or less) and coarse particulate matter PM10 (10 micrometers in diameter or less). Predictions are available from the current day out to 72 hours into the future. Geographical coverage is the North American domain. Data is available at a horizontal resolution of 10 km. While the system encompasses 84 vertical levels, data is available only for the surface level. Predictions are performed twice a day. 

## Access

### How to access the data

This data is available from the [MSC GeoMet](../../msc-geomet/readme_en.md) API / web services and the [MSC Datamart](../../msc-datamart/readme_en.md) data server:

* [Data available via the GeoMet-Weather geospatial web services](readme_raqdps-geomet_en.md)
* [GRIB2 data available on the MSC Datamart](readme_raqdps-datamart_en.md) 

An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is available. Example of a web map configured to display the `RAQDPS.EATM_PM2.5` layer served by MSC GeoMet:

<div id="map" style="height: 400px;"></div>
<div id="controller" role="group" aria-label="Animation controls" style="background: #ececec; padding: 0.5rem;">
  <button id="play" class="btn btn-primary btn-sm" type="button"><i class="fa fa-play" style="padding: 0rem 1rem"></i></button>
  <button id="pause" class="btn btn-primary btn-sm" type="button"><i class="fa fa-pause" style="padding: 0rem 1rem"></i></button>
  <button id="exportmap" class="btn btn-primary btn-sm" type="button"><i class="fa fa-download" style="padding: 0rem 1rem"></i></button>
  <span id="info" style="padding-left: 0.5rem;"></span>
</div>

### Licence

The [end-user licence for Environment and Climate Change Canada's data servers](../../licence/readme_en.md) specifies the conditions of use of this data.

### Metadata

Upcoming.

## Products

* [Maps of 48 hours forecasts](https://weather.gc.ca/aqfm/index_e.html) for tropospheric ozone near the surface and at altitudes of 50 metres and 500 metres, and for PM2.5 and PM10 near the surface. 
* [For-panels maps](https://weather.gc.ca/aqfm/index_e.html) forecasts for PM2.5, PM10, and ozone near the surface and for ozone at 500 metres.

## Technical documentation

* [Technical note](http://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_notes/technote_raqdps_e.pdf)

## Changelog

The chronology of changes to operational systems is available [in the changelog](changelog_raqdps_en.md).

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
        js.src = "../../../js/raqdps_ie.js";
        document.getElementById("controller").setAttribute("hidden", true);
    }
    else
    {
        js.src = "../../../js/raqdps.js";
    }
    head.appendChild(js);
</script>
