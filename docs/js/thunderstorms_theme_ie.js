var map = new ol.Map({
    target: 'map',
    layers: [
      new ol.layer.Tile({
        source: new ol.source.OSM()
      }),
     // *** 1
    new ol.layer.Tile({
      source: new ol.source.TileWMS({
          format: 'image/png',
          url: 'https://geo.weather.gc.ca/geomet/',
          params: {'LAYERS': 'HRDPS.CONTINENTAL.CONV_SHWINX.500', 'TILED': true},
      })
    }),
    // *** 2
    new ol.layer.Tile({
      source: new ol.source.TileWMS({
          format: 'image/png',
          url: 'https://geo.weather.gc.ca/geomet/',
          params: {'LAYERS': 'HRDPS.CONTINENTAL_RT', 'TILED': true},
      })
    }),
    // *** 3
    new ol.layer.Tile({
      source: new ol.source.TileWMS({
          format: 'image/png',
          url: 'https://geo.weather.gc.ca/geomet/',
          params: {'LAYERS': 'HRDPS-WEonG_2.5km_Precip-Prob', 'TILED': true},
      })
    }),
  // *** 4
  new ol.layer.Tile({
    source: new ol.source.TileWMS({
        format: 'image/png',
        url: 'https://geo.weather.gc.ca/geomet/',
        params: {'LAYERS': 'ALERTS', 'TILED': true},
    })
  }),
 // *** 5
  new ol.layer.Image({
    source: new ol.source.ImageWMS({
      format: 'image/png',
      url: 'https://geo.weather.gc.ca/geomet/',
      params: {'LAYERS': 'HRDPS-WEonG_2.5km_WindGust', 'TILED': true},
      transition: 0,
      crossOrigin: 'Anonymous'
    })
  }),
  // *** 6
  new ol.layer.Image({
    source: new ol.source.ImageWMS({
      format: 'image/png',
      url: 'https://geo.weather.gc.ca/geomet/',
      params: {'LAYERS': 'HRDPS-WEonG_2.5km_Thunderstorm-Prob', 'TILED': true},
      transition: 0,
      crossOrigin: 'Anonymous'
    })
  }),
    ],
    view: new ol.View({
      center: ol.proj.fromLonLat([-95, 49]),
      zoom: 3.4
    })
    });