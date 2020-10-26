const parser = new DOMParser();

async function getRadarStartEndTime() {
  let response = await fetch('https://geo.weather.gc.ca/geomet/?lang=en&service=WMS&request=GetCapabilities&version=1.3.0&LAYERS=RAQDPS-FW.EATM_PM2.5-DIFF')
  let data = await response.text().then(
    data => {
      let xml = parser.parseFromString(data, 'text/xml')
      let [start, end] = xml.getElementsByTagName('Dimension')[0].innerHTML.split('/')
      let default_ = xml.getElementsByTagName('Dimension')[0].getAttribute('default')
      return [start, end, default_]
    }
  )
  return [new Date(data[0]), new Date(data[1]), new Date(data[2])]
}

let frameRate = 1.0; // frames per second
let animationId = null;
let startTime = null
let endTime = null
let defaultTime = null
let current_time = null;

let layers = [
    new ol.layer.Tile({
      source: new ol.source.OSM()
    }),
    new ol.layer.Image({
      source: new ol.source.ImageWMS({
        format: 'image/png',
        url: 'https://geo.weather.gc.ca/geomet',
        params: {'LAYERS': 'RAQDPS-FW.EATM_PM2.5-DIFF', 'TILED': true},
      })
    }),
  ]

let map = new ol.Map({
  target: 'map',
  layers: layers,
  view: new ol.View({
    center: ol.proj.fromLonLat([-97, 57]),
    zoom: 3
  })
});

function updateInfo(current_time) {
  let el = document.getElementById('info');
  el.innerHTML = `Time / Heure (UTC): ${current_time.toISOString()}`
}

function setTime() {
  current_time = current_time
    if (current_time === null) {
      current_time = defaultTime;
    } else if (current_time >= endTime) {
      current_time = startTime
    } else {
      current_time = new Date(current_time.setUTCMinutes(current_time.getUTCMinutes() + 60));
    }
    layers[1].getSource().updateParams({'TIME': current_time.toISOString().split('.')[0]+"Z"});
    updateInfo(current_time)
}

getRadarStartEndTime().then(data => {
    startTime = data[0]
    endTime = data[1]
    defaultTime = data[2]
    setTime();
})


let stop = function() {
  if (animationId !== null) {
    window.clearInterval(animationId);
    animationId = null;
  }
};

let play = function() {
  stop();
  animationId = window.setInterval(setTime, 1000 / frameRate);
};

let startButton = document.getElementById('play');
startButton.addEventListener('click', play, false);

let stopButton = document.getElementById('pause');
stopButton.addEventListener('click', stop, false);
