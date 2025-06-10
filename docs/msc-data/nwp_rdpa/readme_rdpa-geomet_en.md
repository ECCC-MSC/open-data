[En français](readme_rdpa-geomet_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [RDPA](readme_rdpa_en.md) > RDPA data on MSC GeoMet


# Regional Deterministic Precipitation Analysis data available on MSC GeoMet

MSC GeoMet provides access to several Regional Deterministic Precipitation Analysis (RDPA) layers. Users can build mobile apps, create interactive web maps, and display and animate RDPA layers in desktop software.

## Access to the geospatial web services

The RDPA data are available

* [on GeoMet-Weather via the Web Map Service (WMS) and Web Coverage Service (WCS) standards](../../msc-geomet/readme_en.md#available-ogc-standards).
* [on the GeoMet-OGC-API geospatial web services](https://api.weather.gc.ca/):
    * [RDPA - 24 hours accumulation](https://api.weather.gc.ca/collections/weather:rdpa:10km:24f)
    * [RDPA - 6 hours accumulation](https://api.weather.gc.ca/collections/weather:rdpa:10km:6f)
    * [RDPA - 24 hours accumulation (preliminary)](https://api.weather.gc.ca/collections/weather:rdpa:10km:24p)
    * [RDPA - 6 hours accumulation (preliminary)](https://api.weather.gc.ca/collections/weather:rdpa:10km:6p)
    * [RDPA - 24 hours accumulation at 15 km](https://api.weather.gc.ca/collections/weather:rdpa:15km:24f)
    * [RDPA - 6 hours accumulation at 15 km](https://api.weather.gc.ca/collections/weather:rdpa:15km:6f)

Example of a web map configured to display the quantity of precipitation [mm] over the past period of 24 hours using a Regional Deterministic Precipitation Analysis (RDPA) WMS layer served by MSC GeoMet:

<div id="map" style="height: 400px; position: relative">
  <div id="legend-popup">
  <div id="legend-popup-content">
    <img id="legend-img" style="display: flex; max-width: 85px;" src="https://geo.weather.gc.ca/geomet?SERVICE=WMS&VERSION=1.3.0&SLD_VERSION=1.1.0&REQUEST=GetLegendGraphic&FORMAT=image/png&LAYER=RDPA.24F_PR&STYLE=&TRANSPARENT=true"/>
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
  <span id="info" style="padding-left: 0.5rem;cursor: pointer;"></span>
</div>


## Usage

The [usage overview page](../../usage/readme_en.md) provides generic information on using these services with desktop software, mobile apps, interactive web maps and direct access. Please refer to the [tutorials](../../usage/tutorials_en.md) and [technical documentation for MSC GeoMet geospatial web services](../../msc-geomet/readme_en.md#available-ogc-standards) for detailed information. See also the [main RDPA data page](readme_rdpa_en.md) which links to additional information on RDPA.


### Available layers

Amount of precipitation that occurred over past periods of 24 hours:

* Available at a resolution of 10 km from 2012-10-03 12:00 Coordinated Universal Time (UTC) up until today:
    * Quantity of precipitation [mm]: `RDPA.24F_PR`
* Available at a resolution of 15 km from 2011-04-06 12:00 UTC to 2012-10-02 12:00 UTC:
    * Quantity of precipitation [mm]: `RDPA.ARC_15km.24F_PR`
*  Available at a resolution of 10 km for the last 30 days:
    * Quantity of precipitation (preliminary) [mm]: `RDPA.24P_PR`

Amount of precipitation that occurred over past periods of 6 hours:

* Available at a resolution of 10 km from 2012-10-03 06:00 Coordinated Universal Time (UTC) up until today:
    * Quantity of precipitation [mm]: `RDPA.6F_PR`
* Available at a resolution of 15 km from 2011-04-06 00:00 UTC to 2012-10-03 00:00 UTC:
    * Quantity of precipitation [mm]: `RDPA.ARC_15km.6F_PR`
*  Available at a resolution of 10 km for the last 30 days:
    * Quantity of precipitation (preliminary) [mm]: `RDPA.6P_PR`


### Usage tips

Retrieving the list of latest RDPA layers timesteps available:

* Users can use the `layer` query parameter in WMS GetCapabilities requests to point to a specific layer and retrieve a smaller XML payload with up-to-date temporal dimensions. Example for the RDPA.24F - Quantity of precipitation [mm]  layer: [https://geo.weather.gc.ca/geomet?service=WMS&version=1.3.0&request=GetCapabilities&layer=RDPA.24F_PR](https://geo.weather.gc.ca/geomet?service=WMS&version=1.3.0&request=GetCapabilities&layer=RDPA.24F_PR)
* Additional information is available in the [handling time with WMS section](../../../msc-geomet/wms_en#handling-time)

WMS styles:

* In addition to the default WMS style, several alternative WMS styles with different color scales are available. The list of available WMS styles is provided in the WMS GetCapabilities response
* Furthermore, users can request layers with their own custom styles with the Styled Layer Descriptor (SLD) standard, please refer to the [SLD technical documentation](../../../msc-geomet/wms_en#handling-styles)

Legends:

* Legends are available for every WMS style. Details are provided in [the WMS legend technical documentation](../../../msc-geomet/wms_en#wms-getlegendgraphic)
* Legend retrieval request example: `https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=RDPA.24F_PR&format=image/png&STYLE=CAPA24-LINEAR`

![The CAPA24-LINEAR WMS legend](https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=RDPA.24F_PR&format=image/png&STYLE=CAPA24-LINEAR)


## Support

The MSC GeoMet services are operational 24/7. User support is provided on a best-effort basis during normal business hours. If you have any questions about these services, please [contact us](https://weather.gc.ca/mainmenu/contact_us_e.html).


## Announcement mailing list

We encourage users to subscribe to the [GeoMet-Info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/geomet-info/) announcement mailing list to be informed of enhancements and changes to the MSC GeoMet services.

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
