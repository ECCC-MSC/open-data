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
        params: {'LAYERS': 'GDPS.ETA_RT', 'TILED': true},
    })
  }),
  new ol.layer.Tile({
    source: new ol.source.TileWMS({
        format: 'image/png',
        url: 'https://geo.weather.gc.ca/geomet/',
        params: {'LAYERS': 'HURRICANE_RESPONSE_ZONE', 'TILED': true},
    })
  }),
      new ol.layer.Tile({
      source: new ol.source.TileWMS({
        format: 'image/png',
        url: 'https://geo.weather.gc.ca/geomet/',
        params: {'LAYERS': 'HURRICANE_ERR', 'TILED': true},
        transition: 0
      })
    }),
    new ol.layer.Tile({
      source: new ol.source.TileWMS({
        format: 'image/png',
        url: 'https://geo.weather.gc.ca/geomet/',
        params: {'LAYERS': 'HURRICANE_RAD', 'TILED': true},
        transition: 0
      })
    }),
    new ol.layer.Tile({
      source: new ol.source.TileWMS({
        format: 'image/png',
        url: 'https://geo.weather.gc.ca/geomet/',
        params: {'LAYERS': 'HURRICANE_LINE', 'TILED': true},
        transition: 0
      })
    }),
    new ol.layer.Tile({
      source: new ol.source.TileWMS({
        format: 'image/png',
        url: 'https://geo.weather.gc.ca/geomet/',
        params: {'LAYERS': 'HURRICANE_CENTRE', 'TILED': true},
        transition: 0
      })
    }),
    new ol.layer.Tile({
	  opacity: 0.7,
      source: new ol.source.TileWMS({
        format: 'image/png',
        url: 'https://geo.weather.gc.ca/geomet/',
        params: {'LAYERS': 'ALERTS', 'TILED': true},
        transition: 0
      })
    })
],
view: new ol.View({
  center: ol.proj.fromLonLat([-97, 57]),
  zoom: 3
})
});