var map = new ol.Map({
  target: 'map',
  layers: [
    new ol.layer.Tile({
      source: new ol.source.OSM()
    }),
    new ol.layer.Tile({
      source: new ol.source.TileWMS({
          format: 'image/png',
          url: 'https://geo.weather.gc.ca/geomet-climate/',
          params: {'LAYERS': 'CanDCSU6-SSP585_AirTempAnomaly-Pct50_2071-2100_P0Y', 'TILED': true},
      })
    })
  ],
  view: new ol.View({
    center: ol.proj.fromLonLat([-97, 57]),
    zoom: 3
  })
  });
