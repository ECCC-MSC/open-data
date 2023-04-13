[En français](readme_gdps_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > GDPS


# Data and Products of the Global Deterministic Prediction System

The Global Deterministic Prediction System (GDPS) performs physical calculations to produce deterministic forecasts of atmospheric elements from the present day to 10 days in the future. Elements of the atmosphere include temperature, precipitation, cloud cover, wind speed and direction, and humidity. This product contains the raw numerical results of these calculations. The geographical coverage is global. The horizontal spatial resolution of the data is 15 km. Data is available for 33 vertical levels. The forecasts are carried out twice a day.

## Access

### How to access the data

This data is available from the [MSC GeoMet](../../msc-geomet/readme_en.md) API / web services and on the [MSC Datamart](../../msc-datamart/readme_en.md) data server respectively:

* [Data available via the GeoMet-Weather geospatial web services](readme_gdps-geomet_en.md)
* [GRIB2 data available on the MSC Datamart](readme_gdps-datamart_en.md)
* [Experimental GRIB2 weather elements on the grid data available on the MSC testing data repository DD-Alpha](readme_gdps-datamart-alpha_en.md)
* [NetCDF global ice analysis on the MSC Datamart](readme_gdps-ice-anal-datamart_en.md)

An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is available. Example of a web map configured to display the `GDPS.DIAG_NW_PT1H` layer served by MSC GeoMet:

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

The [end-user licence for Environment and Climate Change Canada's data servers](../../licence/readme_en.md) specifies the conditions of use of this data.

### MSC Open Data Service Usage Policy

The [MSC Open Data Service Usage Policy](../../usage-policy/readme_en.md) determines what constitutes an acceptable use of MSC Open Data services and provides users best practices for optimal use.

### Metadata

The [metadata of the Global Deterministic Forecasting System are available on the Open Government Portal](https://open.canada.ca/data/en/dataset/c041e79a-914a-5a4e-a485-9cbc506195df).

## Products

List and links to the products available for this dataset:

### Forecast maps

* [4-panel cards](https://meteo.gc.ca/model_forecast/global_e.html)

### Analysis maps

* [Sea Surface Temperature](https://weather.gc.ca/data/analysis/351_100.gif)
* [Sea Ice Cover](https://weather.gc.ca/data/analysis/350_100.gif)
* [Snow Depth](https://weather.gc.ca/data/analysis/352_100.gif)
* [Stratospheric Ozone](https://woudc.org/data/products/)

## Technical documentation

* [Current version of the Global Deterministic Prediction System](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_GDPS_e.pdf)
* [Technical note](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_gdps_e.pdf)


## Changelog

The chronology of changes to the Global Deterministic Prediction System (GDPS) is available [in the changelog](changelog_gdps_en.md).

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
        js.src = "../../../js/gdps_ie.js";
        document.getElementById("controller").setAttribute("hidden", true);
    }
    else
    {
        js.src = "../../../js/gdps.js";
    }
    head.appendChild(js);
</script>
