[En français](readme_climateobs_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > Climate  data (normals, daily, monthly)

# Data and products of the climate data (normals, daily, monthly)  

__Climate normals__

Climate Normals and Averages are used to summarize or describe the average climatic conditions of a particular location. At the completion of each decade, Environment and Climate Change Canada updates its Climate Normals for as many locations and as many climatic characteristics as possible. The Climate Normals, Averages and Extremes offered here are based on Canadian climate stations with at least 15 years of data between 1981 to 2010.

__Climate daily__

Daily climate observations are derived from two sources of data. The first are Daily Climate Stations producing one or two observations per day of temperature, precipitation. The second are hourly stations that typically produce more weather elements e.g. wind or snow on ground. Only a subset of the total stations is shown due to size limitations. The criteria for station selection are listed as below. The priorities for inclusion are as follows: (1) Station is currently operational, (2) Stations with long periods of record, (3) Stations that are co-located with the categories above and supplement the period of record.

__Climate monthly__

A cross-country summary of the averages and extremes for the month, including precipitation totals, max-min temperatures, and degree days.  This data is available from stations that produce daily data.

## Access

### How to access the data

This data is available from the [MSC GeoMet](../../msc-geomet/readme_en.md) API / web services and on the [MSC Datamart](../../msc-datamart/readme_en.md) data server:

* [Data available from the GeoMet-Climate API / geospatial web services](readme_climateobs-geomet_en.md)
* [CSV data available on the MSC Datamart](readme_climateobs-datamart_en.md)

An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is available. Example of a web map configured to display the [DCS.TX.RCP85.YEAR.2081-2100_PCTL50](https://geo.weather.gc.ca/geomet-climate?service=WMS&version=1.3.0&request=GetCapabilities&layer=DCS.TX.RCP85.YEAR.2081-2100_PCTL50) layer served by MSC GeoMet:

<div id="map" style="height: 400px;"></div>
<div id="controller" role="group" aria-label="Animation controls" style="background: #ececec; padding: 0.5rem;">
  <button id="exportmap" class="btn btn-primary btn-sm" type="button"><i class="fa fa-download" style="padding: 0rem 1rem"></i></button>
</div>

### Licence

The [end-user licence for Environment and Climate Change Canada's data servers](../../licence/readme_en.md) specifies the conditions of use of this data.

### Metadata

* The [metadata of the climate normals are available on the Open Government Portal](https://open.canada.ca/data/en/dataset/746f9469-ab78-5dcc-b165-4b51e8ab8652).
* The [metadata of the climate daily are available on the Open Government Portal](https://open.canada.ca/data/en/dataset/5f963c2d-d4ed-5a79-8a31-c9c582ca5098).
* The [metadata of the climate monthly are available on the Open Government Portal](https://open.canada.ca/data/en/dataset/b24efb37-11b6-5d03-ab19-5759f83db546).

## Products 

* [Real-Time Weather Statistics Maps](https://collaboration.cmc.ec.gc.ca/cmc/wtoftpa/www/)

## Technical documentation

* [Technical note](https://climate.weather.gc.ca/doc/Technical_Documentation.pdf)
* [Climate data web site](http://climat.meteo.gc.ca/historical_data/search_historic_data_e.html)
* [Canadian Centre for Climate Services](https://www.canada.ca/en/environment-climate-change/services/climate-change/canadian-centre-climate-services.html)


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
        js.src = "../../../js/climateobs_ie.js";
        document.getElementById("controller").setAttribute("hidden", true);
    }
    else
    {
        js.src = "../../../js/climateobs.js";
    }
    head.appendChild(js);
</script>
