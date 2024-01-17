[En français](readme_satellite_geomet_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [GOES satellite](readme_satellite_en.md) > GOES data on MSC GeoMet

# GOES satellite data available on MSC GeoMet

MSC GeoMet provides access to the weather satellites layers. Users can build mobile apps, create interactive web maps, and display and animate weather satellites layers in desktop software.


## Access to the geospatial web services

The GOES data is available on GeoMet-Weather via the [Web Map Service (WMS)](../../msc-geomet/wms_en.md) and [Web Coverage Service (WCS)](../../msc-geomet/wcs_en.md) standards.

Example of a web map configured to display the Satellite Imagery in natural color [(GOES-East_1km_NaturalColor)](https://geo.weather.gc.ca/geomet?service=WMS&version=1.3.0&request=GetCapabilities&layer=GOES-East_1km_NaturalColor) layer served by MSC GeoMet:

<div id="map" style="height: 400px; position: relative">
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

</br>

## Usage

The [usage overview page](../../usage/readme_en.md) provides generic information on using OGC services with desktop software, mobile apps, interactive web maps and direct access. Please refer to the [tutorials](../../usage/tutorials_en.md) and [technical documentation for MSC GeoMet geospatial web services](../../msc-geomet/readme_en.md#available-ogc-standards) for detailed information. See also the [main weather satellite data page](readme_satellite_en.md) which links to additional information on weather satellite layers.

### Available layers

Weather satellite layers are updated every 10 minutes.

East :

* GOES-East Day visibility / Day Cloud Convection [1 km], ID: `GOES-East_1km_DayVis`
* GOES-East Natural Color [1 km], ID: `GOES-East_1km_NaturalColor`
* GOES-East Night IR [2 km], ID: `GOES-East_2km_NightIR`
* GOES-East Night Microphysics [2 km], ID: `GOES-East_2km_NightMicrophysics`

West :

* GOES-West Day visibility / Day Cloud Convection [1 km], ID: `GOES-West_1km_DayVis`
* GOES-West Natural Color [1 km], ID: `GOES-West_1km_NaturalColor`
* GOES-West Night IR [2 km], ID: `GOES-West_2km_NightIR`
* GOES-West Night Microphysics [2 km], ID: `GOES-West_2km_NightMicrophysics`

### Usage tips

Retrieving the list of latest satellite layer timesteps available:

* Users can use the `layer` query parameter in WMS GetCapabilities requests to point to a specific layer and retrieve a smaller XML payload with up-to-date temporal dimensions. Example for the 1km satellite natural color layer: [https://geo.weather.gc.ca/geomet?service=WMS&version=1.3.0&request=GetCapabilities&layer=GOES-East_1km_NaturalColor](https://geo.weather.gc.ca/geomet?service=WMS&version=1.3.0&request=GetCapabilities&layer=GOES-East_1km_NaturalColor)
* Additional information is available in the [handling time with WMS section](../../../msc-geomet/wms_en#handling-time)

WMS styles:

* In addition to the default WMS style, several alternative WMS styles with different color scales are available. The list of available WMS styles is provided in the WMS GetCapabilities response
* Furthermore, users can request layers with their own custom styles with the Styled Layer Descriptor (SLD) standard, please refer to the [SLD technical documentation](../../../msc-geomet/wms_en#handling-styles)

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
  .distinguish-switch{
    top: 8px;
    right: 1em;
    width: 10rem;
    position: relative;
  }
  .ol-touch .distinguish-switch{
    top: 80px;
  }
  .distinguish-switch.ol-unselectable.ol-control button{
    width: 10rem;
  }

  .distinguish-switch::before {
    content: "Daytime data only"; /* Ajoute le texte que tu veux ici */
    position: absolute;
    top: 50%; /* Ajuste la position verticale si nécessaire */
    left: 50%; /* Ajuste la position horizontale si nécessaire */
    transform: translate(-50%, -50%); /* Centre le texte */
    white-space: nowrap; /* Empêche le texte de passer à la ligne */
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
        js.src = "../../../js/satellite_ie.js";
        document.getElementById("controller").setAttribute("hidden", true);
    }
    else
    {
        js.src = "../../../js/satellite.js";
    }
    head.appendChild(js);
</script>