[En français](readme_raqdps-fw_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > RAQDPS-FW

# Data and Products of the Regional Air Quality Deterministic Prediction System FireWork

Smoke from wildfires in forests and grasslands can be a major source of air pollution for Canadians. The fine particles in the smoke can be a serious risk to health, particularly for children, seniors and those with heart or lung disease. Because smoke may be carried thousands of kilometres downwind, distant locations can be affected almost as severely as areas close to the fire. To help Canadians be better prepared, wildfire smoke forecast maps are available through the Government of Canada’s FireWork system. FireWork is an air quality prediction system that indicates how smoke from wildfires is expected to move across North America over the next 72 hours.

## Access

### How to access the data

This data is available from the [MSC GeoMet](../../msc-geomet/readme_en.md) API / web services and the [MSC Datamart](../../msc-datamart/readme_en.md) data server:

* [Data available via the GeoMet-Weather geospatial web services](readme_raqdps-fw-geomet_en.md)
* [GRIB2 data available on the MSC Datamart](readme_raqdps-fw-datamart_en.md) 

An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is available. Example of a web map configured to display the `RAQDPS-FW.EATM_PM2.5-DIFF` layer served by MSC GeoMet:

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

* [Daily smoke forecast maps](https://weather.gc.ca/firework/index_e.html)

## Technical documentation

* [Technical note](http://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_notes/technote_raqdpsfw_e.pdf)

## Changelog

The chronology of changes to operational systems is available [in the changelog](changelog_raqdps-fw_en.md).

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
        js.src = "../../../js/raqdps-fw_ie.js";
        document.getElementById("controller").setAttribute("hidden", true);
    }
    else
    {
        js.src = "../../../js/raqdps-fw.js";
    }
    head.appendChild(js);
</script>
