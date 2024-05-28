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
          params: {'LAYERS': 'HRDPS-WEonG_2.5km_TotalPrecipIntensityIndex', 'TILED': true},
      }),
      opacity: 0.7,
    }),
    // *** 2
    new ol.layer.Tile({
      source: new ol.source.TileWMS({
          format: 'image/png',
          url: 'https://geo.weather.gc.ca/geomet/',
          params: {'LAYERS': 'HRDPS-WEonG_2.5km_WindGust', 'TILED': true},
      })
    }),
    // *** 3
    new ol.layer.Tile({
      source: new ol.source.TileWMS({
          format: 'image/png',
          url: 'https://geo.weather.gc.ca/geomet/',
          params: {'LAYERS': 'HRDPS-WEonG_2.5km_Thunderstorm-Prob', 'TILED': true},
      })
    }),
  // *** 4
  new ol.layer.Tile({
    source: new ol.source.TileWMS({
        format: 'image/png',
        url: 'https://geo.weather.gc.ca/geomet/',
        params: {'LAYERS': 'CURRENT_CONDITIONS', 'TILED': true},
    })
  }),
 // *** 5
  new ol.layer.Image({
    source: new ol.source.ImageWMS({
      format: 'image/png',
      url: 'https://geo.weather.gc.ca/geomet/',
      params: {'LAYERS': 'HURRICANE_RESPONSE_ZONE', 'TILED': true},
      transition: 0,
      crossOrigin: 'Anonymous'
    })
  }),
  // *** 6
  new ol.layer.Image({
    source: new ol.source.ImageWMS({
      format: 'image/png',
      url: 'https://geo.weather.gc.ca/geomet/',
      params: {'LAYERS': 'ALERTS', 'TILED': true},
      transition: 0,
      crossOrigin: 'Anonymous'
    })
  }),

   ],
    view: new ol.View({
      center: ol.proj.fromLonLat([-90, 48]),
      zoom: 3.5
    })
    });