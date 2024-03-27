// Initiate the right layers depending on the time of year
let layers = [];
let today = new Date();
let april = new Date(new Date().getFullYear(), 3, 1);
let november = new Date(new Date().getFullYear(), 10, 1);

if (today < april || today >= november) {
  // Snow coverage
  layers.push(
    new ol.layer.Tile({
      source: new ol.source.OSM()
    })
  );
  layers.push(
    new ol.layer.Tile({
      source: new ol.source.TileWMS({
        format: 'image/png',
        url: 'https://geo.weather.gc.ca/geomet/',
        params: {'LAYERS': 'RADAR_1KM_RSNO', 'TILED': true},
      })
    })
  );
  layers.push(
    new ol.layer.Tile({
      source: new ol.source.TileWMS({
        format: 'image/png',
        url: 'https://geo.weather.gc.ca/geomet/',
        params: {'LAYERS': 'RADAR_COVERAGE_RSNO.INV', 'TILED': true},
      })
    })
  );
} else {
  // Rain coverage
  layers.push(
    new ol.layer.Tile({
      source: new ol.source.OSM()
    })
  );
  layers.push(
    new ol.layer.Tile({
      source: new ol.source.TileWMS({
        format: 'image/png',
        url: 'https://geo.weather.gc.ca/geomet/',
        params: {'LAYERS': 'RADAR_1KM_RRAI', 'TILED': true},
      })
    })
  );
  layers.push(
    new ol.layer.Tile({
      source: new ol.source.TileWMS({
        format: 'image/png',
        url: 'https://geo.weather.gc.ca/geomet/',
        params: {'LAYERS': 'RADAR_COVERAGE_RRAI.INV', 'TILED': true},
      })
    })
  );
}

let map = new ol.Map({
  target: 'map',
  layers: layers,
  view: new ol.View({
    center: ol.proj.fromLonLat([-97, 57]),
    zoom: 3
  })
});
