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
          params: {'LAYERS': 'GDPS-WEonG_15km_DominantPrecipType', 'TILED': true},
      }),
      opacity: 0.7
    }),
    // *** 2
    new ol.layer.Tile({
      source: new ol.source.TileWMS({
          format: 'image/png',
          url: 'https://geo.weather.gc.ca/geomet/',
          params: {'LAYERS': 'GDPS-WEonG_15km_FreezingRain-Prob', 'TILED': true},
      })
    }),
    // *** 3
    new ol.layer.Tile({
      source: new ol.source.TileWMS({
          format: 'image/png',
          url: 'https://geo.weather.gc.ca/geomet/',
          params: {'LAYERS': 'GDPS-WEonG_15km_WindGust', 'TILED': true},
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
      params: {'LAYERS': 'REPS.DIAG.6_PRMM.ERMEAN', 'TILED': true},
      transition: 0,
      crossOrigin: 'Anonymous'
    })
  }),
  // *** 6
  new ol.layer.Image({
    source: new ol.source.ImageWMS({
      format: 'image/png',
      url: 'https://geo.weather.gc.ca/geomet/',
      params: {'LAYERS': 'Radar_1km_SfcPrecipType', 'TILED': true},
      transition: 0,
      crossOrigin: 'Anonymous'
    })
  }),
    ],
    view: new ol.View({
      center: ol.proj.fromLonLat([-95, 42]),
      zoom: 3.3
    })
    });