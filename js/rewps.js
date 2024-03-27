const parser = new DOMParser();

// Async function used to retrieve start, end, and default time from RESPS-Atlantic-North-West_9km_StormSurge_01 layer GetCapabilities document
async function getRadarStartEndTime() {
  let response = await fetch('https://geo.weather.gc.ca/geomet/?lang=en&service=WMS&request=GetCapabilities&version=1.3.0&LAYERS=REWPS-Great-Lakes_2.5km_PeakWaveDir_01&t=' + new Date().getTime())
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
    new ol.layer.Image({
      source: new ol.source.ImageWMS({
        format: 'image/png',
        url: 'https://geo.weather.gc.ca/geomet',
        params: {'LAYERS': 'REWPS-Great-Lakes_2.5km_PeakWaveDir_01', 'TILED': true},
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
    center: ol.proj.fromLonLat([-83, 46]),
    zoom: 5.3
  })
});

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

// Disable/enable buttons depending on the state of the map
function updateButtons() {
  if (animationId !== null) {
    disableButtons([fastBackwardButton, stepBackwardButton, stepForwardButton, fastForwardButton, exportButton]);
    enableButtons([playPauseButton]);
  } else {
    if (currentTime <= startTime) {
      disableButtons([fastBackwardButton, stepBackwardButton]);
      enableButtons([playPauseButton, stepForwardButton, fastForwardButton, exportButton]);
    } else if (currentTime >= endTime) {
      disableButtons([playPauseButton, stepForwardButton, fastForwardButton]);
      enableButtons([fastBackwardButton, stepBackwardButton, exportButton]);
    } else {
      enableButtons([fastBackwardButton, stepBackwardButton, playPauseButton, stepForwardButton, fastForwardButton, exportButton]);
    }
  }
}

function disableButtons(buttons) {
  for (var i = 0; i < buttons.length; i++){
    buttons[i].disabled = true;
  }
}

function enableButtons(buttons) {
  for (var i = 0; i < buttons.length; i++){
    buttons[i].disabled = false;
  }
}

function setTime() {
  if (currentTime >= endTime) {
    currentTime = endTime;
    togglePlayPause();
  } else {
    currentTime = new Date(currentTime);
    currentTime.setUTCMinutes(currentTime.getUTCMinutes() + 180);
  }
  updateLayers();
  updateInfo();
}

function togglePlayPause() {
  if (animationId !== null) {
    playPauseButton.firstElementChild.className = "fa fa-play"
    window.clearInterval(animationId);
    animationId = null;
    updateButtons();
  } else {
    playPauseButton.firstElementChild.className = "fa fa-pause"
    animationId = window.setInterval(setTime, 1000 / frameRate);
    updateButtons();
  }
}

function fastBackward() {
  if (animationId == null && currentTime > startTime) {
    getRadarStartEndTime().then(data => {
      currentTime = startTime = data[0];
      endTime = data[1];
      defaultTime = data[2];
      updateLayers();
      updateInfo();
      updateButtons();
    })
  }
}

function stepBackward() {
  if (animationId == null && currentTime > startTime) {
    currentTime = new Date(currentTime);
    currentTime.setUTCMinutes(currentTime.getUTCMinutes() - 180);
    if (currentTime.getTime() === startTime.getTime()) {
      getRadarStartEndTime().then(data => {
        currentTime = startTime = data[0];
        endTime = data[1];
        defaultTime = data[2];
        updateLayers();
        updateInfo();
        updateButtons();
      })
    }
    else {
      updateLayers();
      updateInfo();
      updateButtons();
    }
  }
}

function stepForward() {
  if (animationId == null && currentTime < endTime) {
    currentTime = new Date(currentTime);
    currentTime.setUTCMinutes(currentTime.getUTCMinutes() + 180);
    updateLayers();
    updateInfo();
    updateButtons();
  }
}

function fastForward() {
  if (animationId == null && currentTime < endTime) {
    currentTime = new Date(endTime);
    updateLayers();
    updateInfo();
    updateButtons();
  }
}

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

function switchDateFormat(e) {
  dateIsLocal = !dateIsLocal
  updateInfo()
}

let fastBackwardButton = document.getElementById('fast-backward');
fastBackwardButton.addEventListener('click', fastBackward, false);

let stepBackwardButton = document.getElementById('step-backward');
stepBackwardButton.addEventListener('click', stepBackward, false);

let playPauseButton = document.getElementById('play-pause');
playPauseButton.addEventListener('click', togglePlayPause, false);

let stepForwardButton = document.getElementById('step-forward');
stepForwardButton.addEventListener('click', stepForward, false);

let fastForwardButton = document.getElementById('fast-forward');
fastForwardButton.addEventListener('click', fastForward, false);

let exportButton = document.getElementById('exportmap');
exportButton.addEventListener('click', exportMapFunction, false);

let dateInfo = document.getElementById('info');
dateInfo.addEventListener('click', switchDateFormat, false);

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