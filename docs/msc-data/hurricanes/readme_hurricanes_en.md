[En français](readme_hurricanes_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > Hurricanes

# Hurricane prediction data and products

Hurricane tracks and response zone are issued by the [Canadian Hurricane Centre](https://www.canada.ca/en/environment-climate-change/services/hurricane-forecasts-facts/products.html) as part of the regular hurricane season forecast.

## Access

### How to access the data

This data is available on the [MSC GeoMet](../../msc-geomet/readme_en.md) API and on the [MSC Datamart](../../msc-datamart/readme_en.md) data server:

* [Hurricane response zone and trajectories available on the GeoMet-Weather web services](readme_hurricanes_geomet_en.md)
* [Trajectories data available on the MSC Datamart](readme_hurricanes-datamart_en.md)

An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is available.

Example of a web map displaying the hurricane response zone and active hurricanes Web Map Service (WMS) layers, along with weather alerts (beta) and precipitation layers, served by MSC GeoMet:

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

* [Hurricane track maps](https://weather.gc.ca/hurricane/track_e.html)
* [Canadian Hurricane Centre : forecasts and products](https://www.canada.ca/en/environment-climate-change/services/hurricane-forecasts-facts/products.html)

## Technical documentation

* [Canadian Hurricane Centre](https://www.ec.gc.ca/ouragans-hurricanes/)


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
        js.src = "../../../js/hurricane_ie.js";
        document.getElementById("controller").setAttribute("hidden", true);
    }
    else
    {
        js.src = "../../../js/hurricane.js";
    }
    head.appendChild(js);
</script>
