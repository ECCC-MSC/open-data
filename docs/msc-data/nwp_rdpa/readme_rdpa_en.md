[En français](readme_rdpa_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > RDPA


# Data and products of the Regional Deterministic Precipitation Analysis

The Regional Deterministic Precipitation Analysis (RDPA) produces a best estimate of the amount of precipitation that occurred over recent past periods of 6 or 24 hours. The estimate integrates data from in situ precipitation gauge measurements, weather radar and numerical weather prediction models. Geographic coverage is North America (Canada, United States and Mexico). Data is available at horizontal resolution of 10 km. Data is only available for the surface level. Analysis data is made available four times a day for 6h intervals and once a day for the 24h interval. A preliminary estimate is available approximately 1h after the end of the accumulation period, and revised 6h after in order to assimilate gauge data arriving later.

## Access

### How to access the data

This data is available on the [MSC Datamart](../../msc-datamart/readme_en.md) data server service as well as [MSC GeoMet](../../msc-geomet/readme_en.md):

* [Current data and archives available via geospatial web services GeoMet-Weather](readme_rdpa-geomet_en.md)
* [Current GRIB2 data available on the MSC Datamart](readme_rdpa-datamart_en.md) 

An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is available. Example of a web map configured to display the quantity of precipitation [mm] over the past period of 24 hours using a Regional Deterministic Precipitation Analysis (RDPA) WMS layer served by MSC GeoMet:

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

The [metadata of the Regional Deterministic Precipitation Analysis are available on the Open Government Portal](https://open.canada.ca/data/en/dataset/fdd3446a-dc20-5bad-9755-0855e3ec9b19)

## Products

List and links to the products available for this dataset :

### Analysis charts 

6-hour cumulative [analysis charts](https://weather.gc.ca/analysis/index_e.html) valid at synoptic times (00, 06, 12 and 18 UTC) and a 24-hour analysis valid at 12 UTC are available for western and eastern Canada and for the entire country.

## Technical documentation

* Current version of the Regional Deterministic Precipitation Analysis - _Upcoming_
* [Technical note](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/lib/technote_capa_rdpa_e.pdf)
* [Information sheet describing the CaPA system](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/lib/capa_information_leaflet_e.pdf)

## Changelog

The chronology of changes to the Regional Deterministic Precipitation Analysis (RDPA) is available [here](changelog_rdpa_en.md).

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
        js.src = "../../../js/rdpa_ie.js";
        document.getElementById("controller").setAttribute("hidden", true);
    }
    else
    {
        js.src = "../../../js/rdpa.js";
    }
    head.appendChild(js);
</script>
