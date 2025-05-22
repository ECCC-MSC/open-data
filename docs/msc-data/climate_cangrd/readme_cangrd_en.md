[En français](readme_cangrd_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > CanGRD

# Data and products of the Canadian Gridded Temperature and Precipitation Anomalies (CANGRD)  

CANGRD is a set of Canadian gridded annual, seasonal, and monthly temperature and precipitation anomalies, which were interpolated from stations in the Adjusted and Homogenized Canadian Climate Data (AHCCD); it is used to produce the Climate Trends and Variations Bulletin (CTVB).

## Access

### How to access the data

This data is available on [MSC GeoMet](../../msc-geomet/readme_en.md) API / web services and on the [MSC Datamart](../../msc-datamart/readme_en.md) data server service.

* [Data available on the GeoMet-Climate geospatial web services](readme_cangrd-geomet_en.md)
* [Data available on the GeoMet-OGC-API geospatial web services](https://api.weather.gc.ca/):
    * [CanGRD - Historical annual trend](https://api.weather.gc.ca/collections/climate:cangrd:historical:annual:trend)
    * [CanGRD - Historical seasonal trend](https://api.weather.gc.ca/collections/climate:cangrd:historical:seasonal:trend)
    * [CanGRD - Historical annual anomaly](https://api.weather.gc.ca/collections/climate:cangrd:historical:annual:anomaly)
    * [CanGRD - Historical seasonal anomaly](https://api.weather.gc.ca/collections/climate:cangrd:historical:seasonal:anomaly)
    * [CanGRD - Historical monthly anomaly](https://api.weather.gc.ca/collections/climate:cangrd:historical:monthly:anomaly)
* [GeoTIFF data available on the MSC Datamart](readme_cangrd-datamart_en.md)

An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is available. Example of a web map configured to display the [CANGRD.ANO.TX_ANNUAL](https://geo.weather.gc.ca/geomet-climate?service=WMS&version=1.3.0&request=GetCapabilities&layer=CANGRD.ANO.TX_ANNUAL) layer served by MSC GeoMet:

<div id="map" style="height: 400px; position: relative">
  <div id="legend-popup">
  <div id="legend-popup-content">
    <img id="legend-img" src="https://geo.weather.gc.ca/geomet-climate?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=CANGRD.ANO.TX_ANNUAL&format=image/png&STYLE=TEMP-ANOMALIES"/>
  </div>
</div>
</div>
<div id="controller" role="group" aria-label="Animation controls" style="background: #ececec; padding: 0.5rem;">
  <button id="exportmap" class="btn btn-primary btn-sm" type="button"><i class="fa fa-download" style="padding: 0rem 1rem"></i></button>
  <a id="image-download" download="msc-geomet_web-map_export.png"></a>
</div>

### Licence

The [end-user licence for Environment and Climate Change Canada's data servers](../../licence/readme_en.md) specifies the conditions of use of this data.

### MSC Open Data Service Usage Policy

The [MSC Open Data Service Usage Policy](../../usage-policy/readme_en.md) determines what constitutes an acceptable use of MSC Open Data services and provides users best practices for optimal use.

### Discovery metadata

The [metadata of the Canadian Gridded Temperature and Precipitation Anomalies are available on the Open Government Portal](https://open.canada.ca/data/en/dataset/3d4b68a5-13bc-48bb-ad10-801128aa6604)

## Technical documentation

* [Technical note](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/climate_cangrd/CANGRD_Technical_Documentation_en.pdf)
* This data is also available through the [Canadian Climate Services Centre](https://www.canada.ca/en/environment-climate-change/services/climate-change/canadian-centre-climate-services/about.html)

<style>
  #legend-img {
    margin: 0px;
    height:280px;
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
        js.src = "../../../js/cangrd_ie.js";
        document.getElementById("controller").setAttribute("hidden", true);
    }
    else
    {
        js.src = "../../../js/cangrd.js";
    }
    head.appendChild(js);
</script>
