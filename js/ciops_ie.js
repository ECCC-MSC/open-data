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
            params: {'LAYERS': 'CIOPS-East_2km_SeaWaterSalinity_0.5m', 'STYLES': 'SeaWaterSalinity_Dis', 'TILED': true}
        })
      })
    ],
    view: new ol.View({
      center: ol.proj.fromLonLat([-60, 49.6]),
      zoom: 5.5
    })
    });