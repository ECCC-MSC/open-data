[En français](readme_geps_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > GEPS

# Data and Products of the Global Ensemble Prediction System (GEPS)

The Global Ensemble Prediction System (GEPS) carries out physics calculations to arrive at probabilistic predictions of atmospheric elements from the current day out to 16 days into the future (up to 32 days once a week on Thursdays at 00UTC). The GEPS produces different outlooks (scenarios) to estimate the forecast uncertainties due the nonlinear (chaotic) behaviour of the atmosphere. The probabilistic predictions are based on an ensemble of 20 scenarios that differ in their initial conditions, choice of physics parametrization as well as stochastic perturbations (physical tendencies and kinetic energy). A control member that is not perturbed is also available. Weather elements include temperature, precipitation, cloud cover, wind speed and direction, humidity and others. This product contains raw numerical results of these calculations. Geographical coverage is global. The horizontal resolution of the system is 0.35 degree (about 39 km at equator). The system has 45 vertical levels for the forecasts and 81 vertical levels for the analyses. Predictions are performed twice a day.

## Access

### How to access the data

This data is available on the [MSC GeoMet](../../msc-geomet/readme_en.md) API / web services and the [MSC Datamart](../../msc-datamart/readme_en.md) data server:

* [Data available via the GeoMet-Weather API / geospatial web services](readme_geps-geomet_en.md)
* [GRIB2 data available on the MSC Datamart](readme_geps-datamart_en.md) 

An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is available. Example of a web map configured to display the `GEPS.DIAG.12_PRMM.ERGE10` layer served by MSC GeoMet:

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

## Technical documentation

* [Current version of the Global Ensemble Prediction System](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_GEPS_e.pdf)
* [Technical Note](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_geps-600_e.pdf)

## Changelog

The chronology of changes to the Global Ensemble Prediction System (GEPS) is available [in the changelog](changelog_geps_en.md).

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
        js.src = "../../../js/geps_ie.js";
        document.getElementById("controller").setAttribute("hidden", true);
    }
    else
    {
        js.src = "../../../js/geps.js";
    }
    head.appendChild(js);
</script>
