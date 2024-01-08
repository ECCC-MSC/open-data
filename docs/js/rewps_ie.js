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
            params: {'LAYERS': 'REWPS-Great-Lakes_2.5km_PeakWaveDir_01', 'TILED': true},
        })
      })
    ],
    view: new ol.View({
      center: ol.proj.fromLonLat([-83, 46]),
      zoom: 5.2
    })
    });