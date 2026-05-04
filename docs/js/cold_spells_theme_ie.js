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
            params: {'LAYERS': 'HRDPS-WEonG_2.5km_AirTemp', 'TILED': true},
        })
      }),
      // *** 2
      new ol.layer.Tile({
        source: new ol.source.TileWMS({
            format: 'image/png',
            url: 'https://geo.weather.gc.ca/geomet/',
            params: {'LAYERS': 'Current-Alerts', 'TILED': true},
        })
      }),
      // *** 3
      new ol.layer.Tile({
        source: new ol.source.TileWMS({
            format: 'image/png',
            url: 'https://geo.weather.gc.ca/geomet/',
            params: {'LAYERS': 'REPS.DIAG.3_WCF.ERMEAN', 'TILED': true, 'STYLES': 'WindChill_Dis'},
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
        params: {'LAYERS': 'HRDPS.CONTINENTAL_UTCI', 'TILED': true},
        transition: 0,
        crossOrigin: 'Anonymous'
      })
    }),
    // *** 6
    new ol.layer.Image({
      source: new ol.source.ImageWMS({
        format: 'image/png',
        url: 'https://geo.weather.gc.ca/geomet/',
        params: {'LAYERS': 'RDPS-WEonG_10km_DominantPrecipType', 'TILED': true},
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