[En français](readme_rdpa_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > RDPA


# Data and products of the Regional Deterministic Precipitation Analysis

The Regional Deterministic Precipitation Analysis (RDPA) produces a best estimate of the amount of precipitation that occurred over recent past periods of 6 or 24 hours. The estimate integrates data from in situ precipitation gauge measurements, weather radar, satellite imagery and numerical weather prediction models. Geographic coverage is North America (Canada, United States and Mexico). Data is available at horizontal resolution of 10 km. Data is only available for the surface level. Analysis data is made available four times a day for 6h intervals and twice a day for the 24h interval. A preliminary estimate is available approximately 1h after the end of the accumulation period, and revised 7h after in order to assimilate gauge data arriving later.

## Access

### How to access the data

This data is available on the [MSC GeoMet](../../msc-geomet/readme_en.md) web service as well as [MSC Datamart](../../msc-datamart/readme_en.md) data server service:

* [Current data and archives available on the GeoMet-Weather geospatial web services](readme_rdpa-geomet_en.md)
* [Current data and archives available on the GeoMet-OGC-API geospatial web services](https://api.weather.gc.ca/):
    * [RDPA - 24 hours accumulation](https://api.weather.gc.ca/collections/weather:rdpa:10km:24f)
    * [RDPA - 6 hours accumulation](https://api.weather.gc.ca/collections/weather:rdpa:10km:6f)
    * [RDPA - 24 hours accumulation (preliminary)](https://api.weather.gc.ca/collections/weather:rdpa:10km:24p)
    * [RDPA - 6 hours accumulation (preliminary)](https://api.weather.gc.ca/collections/weather:rdpa:10km:6p)
    * [RDPA - 24 hours accumulation at 15 km](https://api.weather.gc.ca/collections/weather:rdpa:15km:24f)
    * [RDPA - 6 hours accumulation at 15 km](https://api.weather.gc.ca/collections/weather:rdpa:15km:6f)
* [Current GRIB2 data available on the MSC Datamart](readme_rdpa-datamart_en.md) 

An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is available. Example of a web map configured to display the quantity of precipitation [mm] over the past period of 24 hours using a Regional Deterministic Precipitation Analysis (RDPA) WMS layer served by MSC GeoMet:

<div id="map" style="height: 400px; position: relative">
  <div id="legend-popup">
  <div id="legend-popup-content">
    <img id="legend-img" src="https://geo.weather.gc.ca/geomet?SERVICE=WMS&VERSION=1.3.0&SLD_VERSION=1.1.0&REQUEST=GetLegendGraphic&FORMAT=image/png&LAYER=RDPA.24F_PR&STYLE=&TRANSPARENT=true"/>
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
  <span id="info" style="padding-left: 0.5rem;"></span>
</div>

### Licence

The [end-user licence for Environment and Climate Change Canada's data servers](../../licence/readme_en.md) specifies the conditions of use of this data.

### MSC Open Data Service Usage Policy

The [MSC Open Data Service Usage Policy](../../usage-policy/readme_en.md) determines what constitutes an acceptable use of MSC Open Data services and provides users best practices for optimal use.

### Metadata

The [metadata of the Regional Deterministic Precipitation Analysis is available on the Open Government Portal](https://open.canada.ca/data/en/dataset/fdd3446a-dc20-5bad-9755-0855e3ec9b19).

## Products

List and links to the products available for this dataset :

### Analysis charts 

6-hour cumulative [analysis charts](https://weather.gc.ca/analysis/index_e.html) valid at synoptic times (00, 06, 12 and 18 UTC) and a 24-hour analysis valid at 12 UTC are available for western and eastern Canada and for the entire country.

## Technical documentation

* [Current version of the Regional Deterministic Precipitation Analysis](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_RDPA_e.pdf)
* [Technical note](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/lib/technote_capa_rdpa_e.pdf)
* [Diagram of dependencies](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwep-dependency-diagrams/system_RDPA_en.svg)

## Changelog

The chronology of changes to the Regional Deterministic Precipitation Analysis (RDPA) is available [here](changelog_rdpa_en.md).

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
        js.src = "../../../js/rdpa_ie.js";
        document.getElementById("controller").setAttribute("hidden", true);
    }
    else
    {
        js.src = "../../../js/rdpa.js";
    }
    head.appendChild(js);
</script>
