const parser = new DOMParser();

let legendContainer = document.getElementById("legend-popup");
let legendContent = document.getElementById("legend-popup-content");

let layers = [
  new ol.layer.Tile({
    source: new ol.source.OSM()
  }),
  new ol.layer.Tile({
    source: new ol.source.TileWMS({
      format: 'image/png',
      url: 'https://geo.weather.gc.ca/geomet-climate',
      params: { 'LAYERS': 'INDICES.PREP1.RCP26_PCTL25', 'TILED': true },
      crossOrigin: 'Anonymous'
    })
  }),
]

// **************************** Add legend button control **************************************
class LegendSwitchControl extends ol.control.Control {

  constructor(opt_options) {
    const options = opt_options || {};

    const button = document.createElement('button');
    button.innerHTML = '<i class="fa fa-paint-brush"></i>';

    const element = document.createElement('div');
    element.className = 'legend-switch ol-unselectable ol-control';
    element.appendChild(button);

    super({
      element: element,
      target: options.target,
    });
    button.addEventListener('click', this.handleLegendSwitch.bind(this), false);
  }

  handleLegendSwitch() {
    legendContainer.hidden = !legendContainer.hidden;
  }
}
// **************************** Add legend button control end ***********************************

let map = new ol.Map({
  controls: ol.control.defaults.defaults().extend([new LegendSwitchControl(), new ol.control.ScaleLine()]),
  target: 'map',
  layers: layers,
  view: new ol.View({
    center: ol.proj.fromLonLat([-97, 57]),
    zoom: 3
  })
});

function exportMapFunction(e) {
  map.once('rendercomplete', function () {
    const mapCanvas = document.createElement('canvas');
    const size = map.getSize();
    mapCanvas.width = size[0];
    mapCanvas.height = size[1];
    const mapContext = mapCanvas.getContext('2d');
    Array.prototype.forEach.call(
      map.getViewport().querySelectorAll('.ol-layer canvas, canvas.ol-layer'),
      function (canvas) {
        if (canvas.width > 0) {
          const opacity = canvas.parentNode.style.opacity || canvas.style.opacity;
          mapContext.globalAlpha = opacity === '' ? 1 : Number(opacity);
          let matrix;
          const transform = canvas.style.transform;
          if (transform) {
            // Get the transform parameters from the style's transform matrix
            matrix = transform
              .match(/^matrix\(([^\(]*)\)$/)[1]
              .split(',')
              .map(Number);
          } else {
            matrix = [
              parseFloat(canvas.style.width) / canvas.width,
              0,
              0,
              parseFloat(canvas.style.height) / canvas.height,
              0,
              0,
            ];
          }
          // Apply the transform to the export map context
          CanvasRenderingContext2D.prototype.setTransform.apply(
            mapContext,
            matrix
          );
          const backgroundColor = canvas.parentNode.style.backgroundColor;
          if (backgroundColor) {
            mapContext.fillStyle = backgroundColor;
            mapContext.fillRect(0, 0, canvas.width, canvas.height);
          }
          mapContext.drawImage(canvas, 0, 0);
        }
      }
    );
    mapContext.globalAlpha = 1;
    mapContext.setTransform(1, 0, 0, 1, 0, 0);
    const link = document.getElementById('image-download');
    link.href = mapCanvas.toDataURL();
    link.click();
  });
  map.renderSync();
};

let exportButton = document.getElementById('exportmap');
exportButton.addEventListener('click', exportMapFunction, false);
