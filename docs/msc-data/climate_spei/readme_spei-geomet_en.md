[En français](readme_spei-geomet_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [SPEI](readme_spei_en.md) > SPEI on MSC GeoMet

# SPEI data available on MSC GeoMet

MSC GeoMet-Climate provides access to data and products of the Standardized Precipitation Evapotranspiration Index (SPEI). Users can build mobile apps, create interactive web maps, and display and animate climate data layers in desktop software.

## Access to the geospatial web services

The SPEI data is [available on GeoMet-Climate via the Web Map Service (WMS) and Web Coverage Service (WCS) standards](../../msc-geomet/readme_en.md).

Example of a web map configured to display the [SPEI-1.RCP2.6.ENS_PCTL50](https://geo.weather.gc.ca/geomet-climate?service=WMS&version=1.3.0&request=GetCapabilities&layer=SPEI-1.RCP2.6.ENS_PCTL50) layer served by MSC GeoMet:

<div id="map" style="height: 400px;"></div>
<div id="controller" role="group" aria-label="Animation controls" style="background: #ececec; padding: 0.5rem;">
  <button id="exportmap" class="btn btn-primary btn-sm" type="button"><i class="fa fa-download" style="padding: 0rem 1rem"></i></button>
</div>

## Usage

The [usage overview page](../../usage/readme_en.md) provides generic information on using OGC services with desktop software, mobile apps, interactive web maps and direct access. Please refer to the [tutorials and technical documentation on MSC GeoMet geospatial web services](../../msc-geomet/readme_en.md) for detailed information.

### Available layers

To see which SPEI layers are served via MSC GeoMet consult the service's [WMS GetCapabilities document](https://geo.weather.gc.ca/geomet-climate?service=WMS&version=1.3.0&request=GetCapabilities). 

Desktop GIS software such as QGIS also makes it easy to [navigate the WMS Get Capabilities document as a layer tree](../../usage/tutorial_WMS_QGIS_en.md).

### Usage tips

Retrieving the available model runs and forecast hours available for a given SPEI layer:

* Users can use the `layer` query parameter in WMS GetCapabilities requests to point to a specific layer and retrieve a smaller XML payload with up-to-date temporal dimensions (see the `<Dimension>` tags). Example: [https://geo.weather.gc.ca/geomet-climate?service=WMS&version=1.3.0&request=GetCapabilities&layer=SPEI-1.RCP2.6.ENS_PCTL50](https://geo.weather.gc.ca/geomet-climate?service=WMS&version=1.3.0&request=GetCapabilities&layer=SPEI-1.RCP2.6.ENS_PCTL50)
* Additional information is available in the [handling time with WMS section](../../../msc-geomet/web-services_en#handling-time)

WMS styles:

* In addition to the default WMS style, several alternative WMS styles with different color scales are available. The list of available WMS styles is provided in the WMS GetCapabilities response.
* Furthermore, users can request layers with their own custom styles with the Styled Layer Descriptor (SLD) standard, please refer to the [SLD technical documentation](../../../msc-geomet/web-services_en#handling-styles).

Legends:

* Legends are available for every WMS style. Details are provided in [the WMS legend technical documentation](../../../msc-geomet/web-services_en#wms-getlegendgraphic).
* Example of retrieving a layer's legend via a GetLegendGraphic request: [https://geo.weather.gc.ca/geomet-climate?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=SPEI-1.RCP2.6.ENS_PCTL50&format=image/png&STYLE=SPEI](https://geo.weather.gc.ca/geomet-climate?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=SPEI-1.RCP2.6.ENS_PCTL50&format=image/png&STYLE=SPEI).

![The SPEI-1.RCP2.6.ENS_PCTL50 SPEI WMS legend](https://geo.weather.gc.ca/geomet-climate?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=SPEI-1.RCP2.6.ENS_PCTL50&format=image/png&STYLE=SPEI)


## Support

The MSC GeoMet services are operational 24/7. User support is provided on a best-effort basis during normal business hours. If you have any questions about these services, please [contact us](https://weather.gc.ca/mainmenu/contact_us_e.html).


## Announcement mailing list

We encourage users to subscribe to the [GeoMet-Info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/geomet-info) announcement mailing list to be informed of enhancements and changes to the MSC GeoMet services.

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
        js.src = "../../../js/spei_ie.js";
        document.getElementById("controller").setAttribute("hidden", true);
    }
    else
    {
        js.src = "../../../js/spei.js";
    }
    head.appendChild(js);
</script>