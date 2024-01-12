const parser = new DOMParser();

// Async function used to retrieve start, end, and default time from GDPS.DIAG_NW_PT1H layer GetCapabilities document
async function getRadarStartEndTime() {
  let response = await fetch('https://geo.weather.gc.ca/geomet?service=WMS&version=1.3.0&request=GetCapabilities&layer=AQHI-OBS&t=' + new Date().getTime())
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
        params: {'LAYERS': 'AQHI-OBS', 'TILED': true},
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