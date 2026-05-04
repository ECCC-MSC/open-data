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
          params: {'LAYERS': 'RDPS.CONTINENTAL_WGX', 'TILED': true},
      })
    }),
    // *** 2
    new ol.layer.Tile({
      source: new ol.source.TileWMS({
          format: 'image/png',
          url: 'https://geo.weather.gc.ca/geomet/',
          params: {'LAYERS': 'HRDPS-WEonG_2.5km_LiquidFogVisibility', 'TILED': true},
      })
    }),
    // *** 3
    new ol.layer.Tile({
      source: new ol.source.TileWMS({
          format: 'image/png',
          url: 'https://geo.weather.gc.ca/geomet/',
          params: {'LAYERS': 'RDPS-WEonG_10km_FreezingPrecip-Prob', 'TILED': true},
      })
    }),
  // *** 4
  new ol.layer.Tile({
    source: new ol.source.TileWMS({
        format: 'image/png',
        url: 'https://geo.weather.gc.ca/geomet/',
        params: {'LAYERS': 'Current-Alerts', 'TILED': true},
    })
  }),
 // *** 5
  new ol.layer.Image({
    source: new ol.source.ImageWMS({
      format: 'image/png',
      url: 'https://geo.weather.gc.ca/geomet/',
      params: {'LAYERS': 'HRDPS-WEonG_2.5km_BlowingSnowPresence', 'TILED': true},
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