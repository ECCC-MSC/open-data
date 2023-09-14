[En français](readme_cmip5-geomet_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [CMIP5](readme_cmip5_en.md) > CMIP5 on MSC GeoMet

# CMIP5 data available on MSC GeoMet

MSC GeoMet-Climate provides access to data and products of the climate scenarios datasets based on an ensemble of global climate model projections from the Coupled Model Intercomparison Project Phase 5 (CMIP5). Users can build mobile apps, create interactive web maps, and display and animate climate data layers in desktop software.

## Access to the geospatial web services

The CMIP5 data is available

* [on GeoMet-Climate via the Web Map Service (WMS) and Web Coverage Service (WCS) standards](../../msc-geomet/readme_en.md).
* [on the GeoMet-OGC-API geospatial web services](https://api.weather.gc.ca/):
    * [CMIP5 - Projected annual](https://api.weather.gc.ca/collections/climate:cmip5:projected:annual:absolute)
    * [CMIP5 - Projected seasonal](https://api.weather.gc.ca/collections/climate:cmip5:projected:seasonal:absolute)
    * [CMIP5 - Projected monthly](https://api.weather.gc.ca/collections/climate:cmip5:projected:monthly:absolute)
    * [CMIP5 - Projected annual anomaly](https://api.weather.gc.ca/collections/climate:cmip5:projected:annual:anomaly)
    * [CMIP5 - Projected seasonal anomaly](https://api.weather.gc.ca/collections/climate:cmip5:projected:seasonal:anomaly)
    * [CMIP5 - Projected monthly anomaly](https://api.weather.gc.ca/collections/climate:cmip5:projected:monthly:anomaly)
    * [CMIP5 - Projected annual anomaly for 20 years average](https://api.weather.gc.ca/collections/climate:cmip5:projected:annual:P20Y-Avg)
    * [CMIP5 - Projected seasonal anomaly for 20 years average](https://api.weather.gc.ca/collections/climate:cmip5:projected:seasonal:P20Y-Avg)
    * [CMIP5 - Historical annual](https://api.weather.gc.ca/collections/climate:cmip5:historical:annual:absolute)
    * [CMIP5 - Historical seasonal](https://api.weather.gc.ca/collections/climate:cmip5:historical:seasonal:absolute)
    * [CMIP5 - Historical monthly](https://api.weather.gc.ca/collections/climate:cmip5:historical:monthly:absolute)
    * [CMIP5 - Historical annual anomaly](https://api.weather.gc.ca/collections/climate:cmip5:historical:annual:anomaly)
    * [CMIP5 - Historical seasonal anomaly](https://api.weather.gc.ca/collections/climate:cmip5:historical:seasonal:anomaly)
    * [CMIP5 - Historical monthly anomaly](https://api.weather.gc.ca/collections/climate:cmip5:historical:monthly:anomaly)

Example of a web map configured to display the [CMIP5.TT.HISTO.SUMMER.ABS_PCTL50](https://geo.weather.gc.ca/geomet-climate?service=WMS&version=1.3.0&request=GetCapabilities&layer=CMIP5.TT.HISTO.SUMMER.ABS_PCTL50) layer served by MSC GeoMet:

<div id="map" style="height: 400px; position: relative">
  <div id="legend-popup">
  <div id="legend-popup-content">
    <img id="legend-img" src="https://geo.weather.gc.ca/geomet-climate?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=CMIP5.TT.HISTO.SUMMER.ABS_PCTL50&format=image/png&STYLE=TEMP-ABSOLUTE"/>
  </div>
</div>
</div>
<div id="controller" role="group" aria-label="Animation controls" style="background: #ececec; padding: 0.5rem;">
  <button id="exportmap" class="btn btn-primary btn-sm" type="button"><i class="fa fa-download" style="padding: 0rem 1rem"></i></button>
  <a id="image-download" download="msc-geomet_web-map_export.png"></a>
</div>

## Usage

The [usage overview page](../../usage/readme_en.md) provides generic information on using OGC services with desktop software, mobile apps, interactive web maps and direct access. Please refer to the [tutorials and technical documentation on MSC GeoMet geospatial web services](../../msc-geomet/readme_en.md) for detailed information.

### Available layers

To see which CMIP5 layers are served via MSC GeoMet consult the service's [WMS GetCapabilities document](https://geo.weather.gc.ca/geomet-climate?service=WMS&version=1.3.0&request=GetCapabilities). 

Desktop GIS software such as QGIS also makes it easy to [navigate the WMS Get Capabilities document as a layer tree](../../usage/tutorial_WMS_QGIS_en.md).

### Usage tips

Retrieving the available model runs and forecast hours available for a given CMIP5 layer:

* Users can use the `layer` query parameter in WMS GetCapabilities requests to point to a specific layer and retrieve a smaller XML payload with up-to-date temporal dimensions (see the `<Dimension>` tags). Example: [https://geo.weather.gc.ca/geomet-climate?service=WMS&version=1.3.0&request=GetCapabilities&layer=CMIP5.TT.HISTO.SUMMER.ABS_PCTL50](https://geo.weather.gc.ca/geomet-climate?service=WMS&version=1.3.0&request=GetCapabilities&layer=CMIP5.TT.HISTO.SUMMER.ABS_PCTL50)
* Additional information is available in the [handling time with WMS section](../../../msc-geomet/web-services_en#handling-time)

WMS styles:

* In addition to the default WMS style, several alternative WMS styles with different color scales are available. The list of available WMS styles is provided in the WMS GetCapabilities response.
* Furthermore, users can request layers with their own custom styles with the Styled Layer Descriptor (SLD) standard, please refer to the [SLD technical documentation](../../../msc-geomet/web-services_en#handling-styles).

Legends:

* Legends are available for every WMS style. Details are provided in [the WMS legend technical documentation](../../../msc-geomet/web-services_en#wms-getlegendgraphic).
* Example of retrieving a layer's legend via a GetLegendGraphic request: [https://geo.weather.gc.ca/geomet-climate?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=CMIP5.TT.HISTO.SUMMER.ABS_PCTL50&format=image/png&STYLE=TEMP-ABSOLUTE](https://geo.weather.gc.ca/geomet-climate?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=CMIP5.TT.HISTO.SUMMER.ABS_PCTL50&format=image/png&STYLE=TEMP-ABSOLUTE).

![The CMIP5.TT.HISTO.SUMMER.ABS_PCTL50 TEMP-ABSOLUTE WMS legend](https://geo.weather.gc.ca/geomet-climate?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=CMIP5.TT.HISTO.SUMMER.ABS_PCTL50&format=image/png&STYLE=TEMP-ABSOLUTE)


## Support

The MSC GeoMet services are operational 24/7. User support is provided on a best-effort basis during normal business hours. If you have any questions about these services, please [contact us](https://weather.gc.ca/mainmenu/contact_us_e.html).


## Announcement mailing list

We encourage users to subscribe to the [GeoMet-Info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/geomet-info/) announcement mailing list to be informed of enhancements and changes to the MSC GeoMet services.

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
        js.src = "../../../js/cmip5_ie.js";
        document.getElementById("controller").setAttribute("hidden", true);
    }
    else
    {
        js.src = "../../../js/cmip5.js";
    }
    head.appendChild(js);
</script>