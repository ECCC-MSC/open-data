[En français](readme_ahccd_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > AHCCD


# Data and products of the Adjusted and Homogenized Canadian Climate Data (AHCCD) 

The data consist of monthly, seasonal and annual means of homogenized daily maximum, minimum and mean surface air temperatures for more than 330 locations in Canada; monthly, seasonal and annual totals of adjusted daily rainfall, snowfall and total precipitation for more than 460 locations; homogenized monthly, seasonal and annual means of hourly surface wind speed at more than 110 locations; monthly, seasonal and annual means of hourly station and sea level pressure adjusted for more than 630 locations. The data are given for the entire period of observation. Please refer to the papers below for detailed information regarding the procedures for homogenization and adjustment. 

## Access

### How to access the data

This data is available from the [MSC GeoMet](../../msc-geomet/readme_en.md) API / web services and on the [MSC Datamart](../../msc-datamart/readme_en.md) data server:

* [Data available from the GeoMet-Climate API / geospatial web services](readme_ahccd-geomet_en.md)
* [GeoJSON data available on the MSC Datamart](readme_ahccd-datamart_en.md)

An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is available. Example of a web map configured to display the [AHCCD.STATIONS](https://geo.weather.gc.ca/geomet-climate?service=WMS&version=1.3.0&request=GetCapabilities&layer=AHCCD.STATIONS) layer served by MSC GeoMet:

<div id="map" style="height: 400px;"></div>
<div id="controller" role="group" aria-label="Animation controls" style="background: #ececec; padding: 0.5rem;">
  <button id="exportmap" class="btn btn-primary btn-sm" type="button"><i class="fa fa-download" style="padding: 0rem 1rem"></i></button>
</div>
### Licence

The [end-user licence for Environment and Climate Change Canada's Data Servers](../../licence/readme_en.md) specifies the conditions of use of this data.

### Metadata

The [metadata of the Adjusted and Homogenized Canadian Climate Data are available on the Open Government Portal](https://open.canada.ca/data/en/dataset/9c4ebc00-3ea4-4fe0-8bf2-66cfe1cddd1d)

## Technical documentation

* [Technical note](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/climate_ahccd/AHCCD_Technical_Documentation_en.pdf)
* This data is also available through the [Canadian Climate Services Centre](https://www.canada.ca/en/environment-climate-change/services/climate-change/canadian-centre-climate-services/about.html)


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
        js.src = "../../../js/ahccd_ie.js";
        document.getElementById("controller").setAttribute("hidden", true);
    }
    else
    {
        js.src = "../../../js/ahccd.js";
    }
    head.appendChild(js);
</script>
