[En français](readme_radar_geomet_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [Radar](readme_radar_en.md) > Radar data on MSC GeoMet

# Weather radar data available on MSC GeoMet

MSC GeoMet provides access to several popular North American weather radar composite and extrapolation layers. Users can build mobile apps, create interactive web maps, and display and animate weather radar layers in desktop software.


## Access to the geospatial web services

The weather radar layers are [available on GeoMet-Weather via the Web Map Service (WMS) standard](../../msc-geomet/readme_en.md).

Example of a web map configured to display the weather radar composite and extrapolation using WMS layers served by MSC GeoMet:

<div id="map" style="height: 400px; position: relative">
  <div id="legend-popup">
  <div id="legend-popup-content">
    <img id="legend-img" src="https://geo.weather.gc.ca/geomet?SERVICE=WMS&VERSION=1.3.0&SLD_VERSION=1.1.0&REQUEST=GetLegendGraphic&FORMAT=image/png&LAYER=RADAR_1KM_RRAI&STYLE=&TRANSPARENT=true"/>
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
MSC GeoMet's North American weather radar composite and extrapolation layers can be seen in action in ECCC's [WeatherCAN mobile app](https://www.canada.ca/en/environment-climate-change/services/weather-general-tools-resources/weathercan.html).


## Usage

The [usage overview page](../../usage/readme_en.md) provides generic information on using these services with desktop software, mobile apps, interactive web maps and direct access. Please refer to the [tutorials and technical documentation on MSC GeoMet geospatial web services](../../msc-geomet/readme_en.md) for detailed information. See also the [main weather radar data page](readme_radar_en.md) which links to additional information on weather radar.

### Available layers

Weather radar layers are updated every 6 minutes. The last 3 hours of data is available on MSC GeoMet. 

North American radar composite [1 km]:

* Radar precipitation rate for rain [mm/hr], ID: `RADAR_1KM_RRAI`
* Radar precipitation rate for snow [cm/hr], ID: `RADAR_1KM_RSNO`
* Corresponding dynamic radar coverage layers:
    * Coverage for Rain, ID: `RADAR_COVERAGE_RRAI`. ID for inverted style: `RADAR_COVERAGE_RRAI.INV`
    * Coverage for Snow, ID: `RADAR_COVERAGE_RSNO`. ID for inverted style: `RADAR_COVERAGE_RSNO.INV`

North American radar surface precipitation type [1 km]:

* Radar surface precipitation type [experimental], ID: `Radar_1km_SfcPrecipType`
* Corresponding dynamic radar coverage layer [experimental]:
    * Coverage, ID: `Radar-Coverage_SfcPrecipType`. ID for inverted style: `Radar-Coverage_SfcPrecipType-Inverted`

North American radar extrapolation [1 km]:

* Radar extrapolation precipitation rate for rain [mm/h] [experimental], ID: `Radar_1km_RainPrecipRate-Extrapolation`
* Radar extrapolation precipitation rate for snow [mm/h] [experimental], ID: `Radar_1km_SnowPrecipRate-Extrapolation`
* Radar extrapolation precipitation rate [dBZ] [experimental], ID: `Radar_1km_dBZ-Extrapolation`

### Usage tips

Retrieving the list of latest radar layer timesteps available:

* Users can use the `layer` query parameter in WMS GetCapabilities requests to point to a specific layer and retrieve a smaller XML payload with up-to-date temporal dimensions. Example for the 1km radar snow layer: [https://geo.weather.gc.ca/geomet?service=WMS&version=1.3.0&request=GetCapabilities&layer=RADAR_1KM_RSNO](https://geo.weather.gc.ca/geomet?service=WMS&version=1.3.0&request=GetCapabilities&layer=RADAR_1KM_RSNO)
* Additional information is available in the [handling time with WMS section](../../../msc-geomet/web-services_en#handling-time)

WMS styles:

* In addition to the default WMS style, several alternative WMS styles with different color scales are available. The list of available WMS styles is provided in the WMS GetCapabilities response
* Furthermore, users can request layers with their own custom styles with the Styled Layer Descriptor (SLD) standard, please refer to the [SLD technical documentation](../../../msc-geomet/web-services_en#handling-styles)

Legends:

* Legends are available for every WMS style. Details are provided in [the WMS legend technical documentation](../../../msc-geomet/web-services_en#wms-getlegendgraphic)
* Legend retrieval request example: `https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=RADAR_1KM_RRAI&format=image/png&STYLE=RADARURPPRECIPR14-LINEAR`

![The RADARURPPRECIPR14-LINEAR WMS legend](https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=RADAR_1KM_RRAI&format=image/png&STYLE=RADARURPPRECIPR14-LINEAR)


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
    right: 2.25em;
    width: 10rem;
  }
  .ol-touch .distinguish-switch{
    top: 80px;
  }
  .distinguish-switch.ol-unselectable.ol-control button{
    width: 10rem;
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
        js.src = "../../../js/radar_ie.js";
        document.getElementById("controller").setAttribute("hidden", true);
    }
    else
    {
        js.src = "../../../js/radar.js";
    }
    head.appendChild(js);
</script>