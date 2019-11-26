[En français](readme_radar_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > Radar imagery

# Data and products for weather radar observations

This page describes the data and products available for Environment and Climate Change Canada's weather radar network. The network is comprised of 31 sites concentrated in the most populated parts of Canada, and provides radar coverage to more than 95 per cent of Canadians. The network’s primary purpose is the early detection of developing thunderstorms and high impact weather, as well the tracking of precipitation.

## Access

### How to access the data

Weather radar data is available as georeferenced images on the [MSC GeoMet](../../msc-geomet/readme_en.md) web map services as well as static GIF images on the [MSC Datamart](../../msc-datamart/readme_en.md):

* [North-American radar composite layers](readme_radar_geomet_en.md) available via geospatial web services on GeoMet-Weather
* [GIF radar imagery](readme_radarimage-datamart_en.md) available on the MSC Datamart 

An [overview and examples on how to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is available. Example of a web map configured to display weather radar composite Web Map Service (WMS) layers served by MSC GeoMet:

<div id="map" style="height: 400px"></div>

### Licence

The [end-user licence for Environment and Climate Change Canada's data servers](../../licence/readme_en.md) specifies the conditions of use for this data.

### Metadata

Not yet available.

## Technical documentation

* [About radar](https://www.canada.ca/en/environment-climate-change/services/weather-general-tools-resources/radar-overview/about.html)
* [Weather radars: how to use](https://weather.gc.ca/radar/how-to-use_e.html)
* [Modernizing Canada's weather-radar network](https://www.canada.ca/en/environment-climate-change/services/weather-general-tools-resources/radar-overview/modernizing-network.html)
* [Radar outages and maintenance](https://www.canada.ca/en/environment-climate-change/services/weather-general-tools-resources/radar-overview/outages-maintenance.html)

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
            }),
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