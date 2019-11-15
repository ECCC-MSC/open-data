[En français](readme_radar-geomet_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [Radar](readme_radar_en.md) > Radar data on MSC GeoMet

# Available weather radar data on MSC GeoMet

MSC GeoMet provides access to several popular North American weather radar composite layers. Users can build mobile apps, create interactive web maps, or display and animate weather radar layers in desktop software.

## Access to the geospatial web services

The weather radar layers are available on GeoMet-Weather via the Web Map Service (WMS) standard:

* [Access to GeoMet-Weather](../../msc-geomet/readme_en.md)
* [Technical documentation on MSC GeoMet geospatial web services](../../msc-geomet/web-services_en.md)

Example of OpenLayers web map configured to display weather radar composite using WMS layers served by MSC GeoMet:

<div id="map" style="height: 400px"></div>

MSC GeoMet's North American weather radar composite layers can be seen in action in ECCC's [WeatherCAN mobile app](https://www.canada.ca/en/environment-climate-change/services/weather-general-tools-resources/weathercan.html).

## Available layers

Weather radar layers are updated every 10 minutes. The last 3 hours of data is available on MSC GeoMet. 

North-American weather radar composite at 1 km:

* Radar precipitation rate (Rain) (1 km) [mm/hr], ID: `RADAR_1KM_RRAI`
* Radar precipitation rate (Snow) (1 km) [cm/hr], ID: `RADAR_1KM_RSNO`
* Radar reflectivity (Rain) (1 km) [dBZ], ID: `RADAR_1KM_RDBR`
* Corresponding dynamic radar coverage layers:
    * Coverage for Rain, ID: `RADAR_COVERAGE_RRAI`. ID for inverted style: `RADAR_COVERAGE_RRAI.INV`
    * Coverage for Snow, ID: `RADAR_COVERAGE_RSNO`. ID for inverted style: `RADAR_COVERAGE_RSNO.INV`

North-American weather radar composite at 4 km:

* Radar precipitation rate (Rain) (4 km) [mm/hr], ID: `RADAR_RRAI`
* Radar precipitation rate (Snow) (4 km) [cm/hr], ID: `RADAR_RSNO`
* Radar reflectivity (Rain) (4 km) [dBZ], ID: `RADAR_RDBR`
* Radar reflectivity (Snow) (4 km) [dBZ], ID: `RADAR_RDBS`

## Usage

Please refer to the [technical documentation on MSC GeoMet geospatial web services](../../msc-geomet/web-services_en.md) for detailed information.

Retrieving the list of latest timesteps available:

* Users can use `&layer=` in WMS GetCapabilities requests to point to a specific layer and retrieve a smaller XML payload with up-to-date temporal dimensions. Example for the 1km radar snow layer: [https://geo.weather.gc.ca/geomet?service=WMS&version=1.3.0&request=GetCapabilities&layer=RADAR_1KM_RSNO](https://geo.weather.gc.ca/geomet?service=WMS&version=1.3.0&request=GetCapabilities&layer=RADAR_1KM_RSNO)
* Additional information is available in the [handling time with WMS section](../../msc-geomet/web-services_en/#handling-time)

WMS styles:

* In addition to the default WMS style, several alternative WMS styles with different color scales are available. The list of available WMS styles is provided in the WMS GetCapabilities response
* Users can request layers with their own custom styles with the Styled Layer Descriptor (SLD) standard, please refer to the [SLD technical documentation](../../msc-geomet/web-services_en/#handling-styles)

Legends:

* Legends are available for every WMS style. Details are provided in [the WMS style technical documentation](../../msc-geomet/web-services_en/#wms-getlegendgraphic)
* Legend retrieval request example: `https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=RADAR_1KM_RRAI&format=image/png&STYLE=RADARURPPRECIPR14-LINEAR`

![The RADARURPPRECIPR14-LINEAR WMS legend](https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=RADAR_1KM_RRAI&format=image/png&STYLE=RADARURPPRECIPR14-LINEAR)

## Support

The MSC GeoMet services are operational 24/7. User support is provided on a best-effort basis during normal business hours. If you have any questions about these services, please [contact us](https://weather.gc.ca/mainmenu/contact_us_e.html).


## Announcement mailing list

We encourage users to subscribe to the [GeoMet-Info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/geomet-info) announcement mailing list to be informed of enhancements and changes to the MSC GeoMet services.

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/openlayers/4.6.5/ol.css" integrity="sha256-rQq4Fxpq3LlPQ8yP11i6Z2lAo82b6ACDgd35CKyNEBw=" crossorigin="anonymous" />
<script src="https://cdnjs.cloudflare.com/ajax/libs/openlayers/4.6.5/ol.js" integrity="sha256-77IKwU93jwIX7zmgEBfYGHcmeO0Fx2MoWB/ooh9QkBA=" crossorigin="anonymous"></script>
<script type="text/javascript">
      var map = new ol.Map({
        target: 'map',
        layers: [
          new ol.layer.Tile({
            source: new ol.source.OSM()
          }),
          new ol.layer.Tile({
            source: new ol.source.TileWMS({
                format: 'image/png',
                url: 'https://geo.weather.gc.ca/geomet/',
                params: {'LAYERS': 'RADAR_1KM_RSNO', 'TILED': true},
            })
          new ol.layer.Tile({
            source: new ol.source.TileWMS({
                format: 'image/png',
                url: 'https://geo.weather.gc.ca/geomet/',
                params: {'LAYERS': 'RADAR_COVERAGE_RSNO.INV', 'TILED': true},
            })
          })
        ],
        view: new ol.View({
          center: ol.proj.fromLonLat([-97, 57]),
          zoom: 3
        })
      });
</script>