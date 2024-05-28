const parser = new DOMParser();

// Async function used to retrieve start, end, and default time from GDPS.ETA_RT layer GetCapabilities document
async function getRadarStartEndTime() {
  let response = await fetch('https://geo.weather.gc.ca/geomet/?lang=en&service=WMS&request=GetCapabilities&version=1.3.0&GDPS-WEonG_15km_DominantPrecipType&t=' + new Date().getTime())
  let data = await response.text().then(
    data => {
      let xml = parser.parseFromString(data, 'text/xml')
      let [start, end] = xml.getElementsByTagName('Dimension')[0].innerHTML.split('/')
      /* overwrite end date and set to 48 hours from start data */
      end = new Date(start)
      end.setUTCHours(end.getUTCHours() + 48)
      let default_ = xml.getElementsByTagName('Dimension')[0].getAttribute('default')
      return [start, end, default_]
    }
  )
  return [new Date(data[0]), new Date(data[1]), new Date(data[2])]
}

let legendContainer = document.getElementById("legend-popup");
let legendContent = document.getElementById("legend-popup-content");
let frameRate = 1.0; // frames per second
let animationId = null;
let startTime = null
let endTime = null
let defaultTime = null
let currentTime = null;
let dateIsLocal = true;
const dateOptions = {
  year: 'numeric',
  month: '2-digit',
  day: '2-digit',
  hour: '2-digit',
  minute: '2-digit',
  timeZoneName: 'short'
};

let layers = [
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
  handleLegendSwitch() {
    legendContent.hidden = !legendContent.hidden;
  }
}

function updateLegend(imageUrl) {
  var imageElement = document.getElementById('legend-img');
  imageElement.src = imageUrl;
}

// **************************** Add legend button control end ***********************************
let map = new ol.Map({
  controls: ol.control.defaults.defaults().extend([new LegendSwitchControl(), new ol.control.ScaleLine()]),
  target: 'map',
  layers: layers,
  view: new ol.View({
    center: ol.proj.fromLonLat([-90, 55]),
    zoom: 3.3
  })
});

// **************************** Layers - cases à cocher ***********************************
// Récupérez les éléments de case à cocher
const layer1Checkbox = document.getElementById('layer1');
const layer2Checkbox = document.getElementById('layer2');
const layer3Checkbox = document.getElementById('layer3');
const layer4Checkbox = document.getElementById('layer4');
const layer5Checkbox = document.getElementById('layer5');
const layer6Checkbox = document.getElementById('layer6');


// Récupérez les couches correspondantes à partir de votre tableau de couches
const layer1 = layers[1];
const layer2 = layers[2];
const layer3 = layers[3];
const layer4 = layers[4];
const layer5 = layers[5];
const layer6 = layers[6];


layer1.setVisible(true);
layer2.setVisible(true);
layer3.setVisible(false);
layer4.setVisible(true);
layer5.setVisible(false);
layer6.setVisible(false);


// Écoutez les changements dans les cases à cocher
layer1Checkbox.addEventListener('change', function() {
    layer1.setVisible(layer1Checkbox.checked);
});

layer2Checkbox.addEventListener('change', function() {
    layer2.setVisible(layer2Checkbox.checked);
});

layer3Checkbox.addEventListener('change', function() {
    layer3.setVisible(layer3Checkbox.checked);
});

layer4Checkbox.addEventListener('change', function() {
    layer4.setVisible(layer4Checkbox.checked);
});

layer5Checkbox.addEventListener('change', function() {
    layer5.setVisible(layer5Checkbox.checked);
});

layer6Checkbox.addEventListener('change', function() {
  layer6.setVisible(layer6Checkbox.checked);
});

// **************************** Layers - cases à cocher fin ***********************************

// If the image couldn't load due to the timelapse updating, get the new timelapse
layers[1].getSource().on("imageloaderror", () => {
  getRadarStartEndTime().then(data => {
    currentTime = startTime = data[0];
    endTime = data[1];
    defaultTime = data[2];
    updateLayers();
    updateInfo();
    updateButtons();
  })
});

function updateLayers() {
  layers[1].getSource().updateParams({'TIME': currentTime.toISOString().split('.')[0]+"Z"});
}

// Dispalying current map time
function updateInfo() {
  let el = document.getElementById('info');
  if (dateIsLocal) {
    el.innerHTML = `Time/Heure: ${currentTime.toLocaleString(navigator.local, dateOptions)}`
  } else {
    el.innerHTML = `Time/Heure: ${currentTime.toISOString().substr(0, 16)+"Z"}`
  }
}

// Initialize the map
function initMap() {
  getRadarStartEndTime().then(data => {
    startTime = data[0];
    endTime = data[1];
    currentTime = defaultTime = data[2];
    updateLayers();
    updateInfo();
    updateButtons();
  })
}

initMap();