[En français](tutorial_web-maps_fr.md)

![ECCC logo](../img_eccc-logo.png)

[TOC](../readme_en.md) > [Usage overview](readme_en.md) > Create interactive web maps

# Tutorial: building interactive web maps with OpenLayers and Leaflet

[MSC GeoMet](../msc-geomet/readme_en.md) geospatial web services are easily integrated into free and open source web mapping libraries such as [OpenLayers](https://openlayers.org/) and [Leaflet](https://leafletjs.com/) to build interactive maps for web pages and mobile apps. This tutorial will show you how to work with a Web Map Service (WMS) using both libraries. By the end of it, you will be able to display any MSC GeoMet WMS layer on an interactive map, query the layer for data, and animate time-enabled layers.

- [Displaying a WMS layer](#displaying-a-wms-layer)
    * [OpenLayer example](#openlayers-example)
    * [Leaflet example](#leaflet-example)
- [Building interactive popups with OpenLayers](#building-interactive-popups-with-openlayers)
- [Animating time-enabled WMS layers with OpenLayers](#animating-time-enabled-wms-layers-with-openlayers)

## Displaying a WMS layer

The following steps will show how to create a simple web map with OpenLayers and Leaflet. The map will display the Global Deterministic Prediction System (GDPS) air surface temperature data (`GPDS.ETA_TT`) over an [OpenStreetMap](https://www.openstreetmap.org/) basemap. An example is given for the both OpenLayers and Leaflet.

### OpenLayers example

#### HTML

```html
<html lang="en">
<head>
  <meta charset="utf-8">
  <style>
    #map {
      width: 100%;
      height: 400px;
    }
  </style>

  <title>MSC GeoMet OpenLayers Example</title>
  <meta name="description" content="MSC GeoMet OpenLayers Example">
  <meta name="author" content="CCMEP">

  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/ol@v7.3.0/ol.css" type="text/css"/>
  <script src="https://cdn.jsdelivr.net/npm/ol@v7.3.0/dist/ol.js"></script>
</head>

<body>
    <div id="map"></div>

    <script src="./tutorial.js"></script>
</body>
</html>
```

In order to use OpenLayers, we must import the required JS and CSS libraries. A `<div>` element is added in the body of our HTML document and assigned an `id` attribute with a value of `map`. The `id` value will be referred to in the JavaScript code in order to specify where to render the interactive map in the HTML document.
A `<script>` tag is also included in the body of the HTML document, to link the JavaScript file to our HTML.
A small amount of CSS is also added in the `<head>` tag in order to define the width and height of the map container.

#### JavaScript

With the HTML code now complete, let's turn our attention to writing the JavaScript code required to create our web map.

```javascript
/* Name of the file: tutorial.js */

let layers_to_add = [
    new ol.layer.Tile({
      source: new ol.source.OSM()
    }),
    new ol.layer.Tile({
      opacity: 0.4,
      source: new ol.source.TileWMS({
        url: 'https://geo.weather.gc.ca/geomet/',
        params: {'LAYERS': 'GDPS.ETA_TT', 'TILED': true},
        transition: 0
      })
    })
  ];

let map = new ol.Map({
  target: 'map',
  layers: layers_to_add,
  view: new ol.View({
    center: ol.proj.fromLonLat([-97, 57]),
    zoom: 0
  })
});
```

To keep things a little tidy, we create an `layers_to_add` array that contains a list of layers we want to add to our map. Each item is a layer that is linked to a source. In this case two layers are added to the map: (1) the OpenStreetMap layer for our basemap and (2) the GeoMet-Weather WMS for the Global Deterministic Prediction System (GDPS) air surface temperature layer. The GDPS air surface temperature source also has some additional properties:

 * `url`: WMS service URL
 * `params`: WMS request parameters. The `LAYERS` parameter is required
 * `transition`: duration of the opacity transition for rendering. We disable this here since we are setting an opacity and want it to be applied prior to displaying each tile

Then we create a new variable called `map` and use the `ol.Map` constructor to define the map that will be rendered in our HTML document. In the object passed to the constructor, define a `target` for our map (e.g the `id` value of the HTML container, in this case `map`). The `layers_to_add` array is then passed to the `layers` property and the `ol.View` constructor is used to define the initial view of our map. In our case, we set the  initial zoom level and center the view on a specific lon/lat coordinate. 

Below is a a live example of the above code. Try modifying the JavaScript code to display another layer, changing the opacity, and the initial zoom and centre coordinates of the map.

<iframe height="300" style="width: 100%;" scrolling="no" title="GeoMet Simple WMS  OpenLayers" src="https://codepen.io/eccc-msc/embed/jObyoPw?height=281&theme-id=light&default-tab=js,result" frameborder="no" allowtransparency="true" allowfullscreen="true" loading="lazy">
  See the Pen <a href='https://codepen.io/eccc-msc/pen/jObyoPw'>GeoMet Simple WMS  OpenLayers</a> by ECCC-MSC
  (<a href='https://codepen.io/eccc-msc'>@eccc-msc</a>) on <a href='https://codepen.io'>CodePen</a>.
</iframe>

### Leaflet example

#### HTML

```html
<html lang="en">
<head>
  <meta charset="utf-8">
  <style>
    #map {
      width: 100%;
      height: 400px;
    }
  </style>
  <title>MSC GeoMet Simple WMS Leaflet Example</title>
  <meta name="description" content="MSC GeoMet OpenLayers Example">
  <meta name="author" content="CCMEP">

  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.3/dist/leaflet.css" integrity="sha256-kLaT2GOSpHechhsozzB+flnD+zUyjE2LlfWPgU04xyI=" crossorigin="" />
  <script src="https://unpkg.com/leaflet@1.9.3/dist/leaflet.js" integrity="sha256-WBkoXOwTeyKclOHuWtc+i2uENFpDZ9YPdf5Hf+D7ewM=" crossorigin=""></script>
</head>

<body>
  <div id="map"></div>

  <script src="./tutorial.js"></script>
</body>
</html>
```

First, in order to use Leaflet, we must import the required JS and CSS libraries. A `<div>` element is added in the body of our HTML document and assigned an `id` attribute with a value of `map`. The `id` value will be referred to in the JavaScript code in order to specify where to render the interactive map in the HTML document.
A `<script>` tag is also included in the body of the HTML document, to link the JavaScript file to our HTML.
A small amount of CSS is also added in the `<head>` tag in order to define the width and height of the map container.

#### JavaScript

With the HTML code now complete, let's turn our attention to writing the JavaScript code required to create our web map.

```javascript
/* Name of the file: tutorial.js */

let map = L.map("map").setView([0,0], 3);

let OpenStreetMap_Mapnik = L.tileLayer(
  "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
  {
    maxZoom: 19,
    attribution:
      '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  }
).addTo(map);

let wmsLayer = L.tileLayer.wms('https://geo.weather.gc.ca/geomet?', {
    layers: 'GDPS.ETA_TT',
    version: '1.3.0',
    opacity: 0.5,
}).addTo(map);
```

The above code instantiates a [map object](https://leafletjs.com/reference-1.6.0.html#map) using the Leaflet API and sets the initial map view with the [<code>setView</code>](https://leafletjs.com/reference-1.6.0.html#map-setview) method.

Following the instantiation of the map, two layers are defined and added to the map instance. For each layer, a base URL is passed as well as parameters/options object used to define in further detail. For example, when instantiating the `wmsLayer` variable we define the opacity of the `GDPS.ETA_TT` layer and the WMS version to use when a request is made within the parameters object.

See the live example below:

<iframe height="300" style="width: 100%;" scrolling="no" title="GeoMet Simple WMS Leaflet" src="https://codepen.io/eccc-msc/embed/GRpragg?height=265&theme-id=light&default-tab=js,result" frameborder="no" allowtransparency="true" allowfullscreen="true" loading="lazy">
  See the Pen <a href='https://codepen.io/eccc-msc/pen/GRpragg'>GeoMet Simple WMS Leaflet</a> by ECCC-MSC
  (<a href='https://codepen.io/eccc-msc'>@eccc-msc</a>) on <a href='https://codepen.io'>CodePen</a>.
</iframe>

## Building interactive popups with OpenLayers

Let's now query a WMS layer to access the underlying data via a popup. Web Map Services (WMS) allow a user to make a [GetFeatureInfo](../msc-geomet/web-services_en.md#wms-getfeatureinfo) request to extract raw data associated to a coordinate on the map. Using the OpenLayers API, we will create a popup when a user clicks on the map that will display the coordinates of the clicked point and the corresponding data. This implementation is heavily inspired by the [popup](https://openlayers.org/en/latest/examples/popup.html?q=popup) and [WMS GetFeatureInfo](https://openlayers.org/en/latest/examples/getfeatureinfo-tile.html?q=popup) examples provided by OpenLayers.

### HTML

Some additional HTML and CSS will need to be added to our initial HTML document.

```html
<html lang="en">
<head>
  <meta charset="utf-8">
  <style>
    #map {
      width: 100%;
      height: 800px;
    }
    /* Add in CSS required for popup*/
    .ol-popup {
      position: absolute;
      background-color: white;
      box-shadow: 0 1px 4px rgba(0, 0, 0, 0.2);
      padding: 15px;
      border-radius: 10px;
      border: 1px solid #cccccc;
      bottom: 12px;
      left: -50px;
      min-width: 300px;
    }

    .ol-popup:after,
    .ol-popup:before {
      top: 100%;
      border: solid transparent;
      content: " ";
      height: 0;
      width: 0;
      position: absolute;
      pointer-events: none;
    }

    .ol-popup:after {
      border-top-color: white;
      border-width: 10px;
      left: 48px;
      margin-left: -10px;
    }

    .ol-popup:before {
      border-top-color: #cccccc;
      border-width: 11px;
      left: 48px;
      margin-left: -11px;
    }

    .ol-popup-closer {
      text-decoration: none;
      position: absolute;
      top: 5px;
      right: 8px;
    }

    .ol-popup-closer:after {
      content: "✖";
      color: #A9A9A9;
    }
  </style>

  <title>GeoMet OpenLayers Popup Example</title>
  <meta name="description" content="GeoMet OpenLayers Popup Example">
  <meta name="author" content="CCMEP">

  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/ol@v7.3.0/ol.css" type="text/css"/>
  <script src="https://cdn.jsdelivr.net/npm/ol@v7.3.0/dist/ol.js"></script>
</head>

<body>
  <div id="map"></div>
  <div id="popup" class="ol-popup">
    <a href="#" id="popup-closer" class="ol-popup-closer"></a>
    <div id="popup-content"></div>
  </div>

  <script src="./tutorial.js"></script>
</body>
</html>
```

To create the popup, a new `div` element is added. Within this new element, an anchor tag is added to allow for closing the popup when displayed on the map. An empty `div` will contain the results of the GetFeatureInfo and the coordinates of the clicked map point. The additional CSS is used to define the look and feel of the popup as well as displaying/hiding the popup when the user clicks on the map.

### JavaScript

```javascript
/* Name of the file: tutorial.js */

/**
 * Elements that make up the popup.
 */
let container = document.getElementById("popup");
let content = document.getElementById("popup-content");
let closer = document.getElementById("popup-closer");

/**
 * Create an overlay to anchor the popup to the map.
 */
let overlay = new ol.Overlay({
  element: container,
  autoPan: true,
  autoPanAnimation: {
    duration: 250
  }
});

/**
 * Add a click handler to hide the popup.
 * @return {boolean} Don't follow the href.
 */
closer.onclick = function () {
  overlay.setPosition(undefined);
  closer.blur();
  return false;
};

let layers = [
  new ol.layer.Tile({
    source: new ol.source.OSM()
  }),
  new ol.layer.Tile({
    opacity: 0.4,
    source: new ol.source.TileWMS({
      url: "https://geo.weather.gc.ca/geomet",
      params: { LAYERS: "GDPS.ETA_TT", TILED: true },
      transition: 0
    })
  })
];

let map = new ol.Map({
  target: "map",
  layers: layers,
  overlays: [overlay],
  view: new ol.View({
    center: ol.proj.fromLonLat([-97, 57]),
    zoom: 0
  })
});

map.on("singleclick", function (evt) {
  let coordinate = evt.coordinate;
  let xy_coordinates = ol.coordinate.toStringXY(
    ol.proj.toLonLat(evt.coordinate),
    4
  );
  let viewResolution = map.getView().getResolution();
  let wms_source = map.getLayers().item(1).getSource();
  let url = wms_source.getFeatureInfoUrl(
    coordinate,
    viewResolution,
    "EPSG:3857",
    { INFO_FORMAT: "application/json" }
  );
  content.innerHTML = '<p align="center">Fetching data...</p>';
  overlay.setPosition(evt.coordinate);
  if (url) {
    fetch(url)
      .then(function (response) {
        return response.json();
      })
      .then(function (json) {
        content.innerHTML = `
Air surface temperature<br>
Coordinates (Lon/Lat): </> <code>${xy_coordinates}</code><br>
Value: </b><code>${Math.round(json.features[0].properties.value)} °C</code>`;
      });
  }
});
```

There are four main additions to the JavaScript code.

First, we create references to the three HTML elements that are used by the popup( `container`, `content`, and `closer`). 

The [<code>ol.Overlay()</code>](https://openlayers.org/en/latest/apidoc/module-ol_Overlay-Overlay.html) constructor is then used to create a new overlay which will be used to anchor the popup to the map. Note that `container` (i.e. our popup) is associated to the `element` property of the object passed to the Overlay
constructor. The overlay is then passed as an array item to the `overlays` property when constructing the map.

An inline `onclick` event is then added to the `closer` (i.e the `<a>` tag in the popup), that sets the overlay position to `undefined`, effectively hiding the overlay when the anchor tag contained in the popup is clicked.

Finally, our map will take advantage of the [<code>ol.Map.on()</code>](https://openlayers.org/en/latest/apidoc/module-ol_Map-Map.html#on) method to listen for `singleclick` events on the map. The callback function
that is triggered by the event does the following:

* Fetches the coordinates of the clicked map point, then reprojects the coordinates to EPSG:4326 (WSG 84). The `ol.coordinate.toStringXY` method transforms the coordinates into a comma delimited string
* Retrieves the resolution of the map view
* Retrieves the source of the `GDPS.ETA_TT` layer
* Uses the `ol.source.TileWMS.getFeatureInfoUrl()` method to create a WMS GetFeatureInfo request. Passed as arguments are the click event coordinates, view resolution, map projection, and an object containing any GetFeatureInfo parameters (`INFO_FORMAT` should at least be provided)
* Sets the overlay position to the coordinates of the initial click event
* If the GetFeatureInfo URL is properly constructed, submits the GetFeatureInfo request using the JavaScript API. Upon receiving a response, the JSON is retrieved and the popup content is updated with additional HTML that includes the coordinates and the value property of the first GeoJSON feature retrieved by the GetFeatureInfo request


See the live example below:

<iframe height="300" style="width: 100%;" scrolling="no" title="GeoMet GetFeatureInfo OpenLayers English" src="https://codepen.io/eccc-msc/embed/yLOyvXa?height=300&theme-id=light&default-tab=js,result" frameborder="no" loading="lazy" allowtransparency="true" allowfullscreen="true">
  See the Pen <a href='https://codepen.io/eccc-msc/pen/yLOyvXa'>GeoMet GetFeatureInfo OpenLayers English</a> by ECCC-MSC
  (<a href='https://codepen.io/eccc-msc'>@eccc-msc</a>) on <a href='https://codepen.io'>CodePen</a>.
</iframe>

## Animating time-enabled WMS layers with OpenLayers

A significant amount of data served by MSC GeoMet has one or more temporal dimensions. The following section will dive into how OpenLayers can help us visualize and animate the various time slices of such layers, in this case weather radar data, served as a WMS via GeoMet-Weather.

Two GeoMet-Weather layers are used to create this animation: `RADAR_1KM_RRAI` and `RADAR_COVERAGE_RRAI.INV`. These layers are available over a moving 3-hour window, every 6 minutes.

### HTML

```html
<html lang="en">
<head>
  <meta charset="utf-8">
  <style>
    #map {
      width: 100%;
      height: 400px;
    }
  </style>
  <title>GeoMet Animated WMS Time OpenLayers Example</title>
  <meta name="description" content="GeoMet OpenLayers Example">
  <meta name="author" content="CCMEP">

  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
  <link href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet" integrity="sha384-wvfXpqpZZVQGK6TAh5PVlGOfQNHSoD2xbE+QkPxCAFlNEevoEH3Sl0sibVcOQVnN" crossorigin="anonymous">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/ol@v7.3.0/ol.css" type="text/css"/>
  <script src="https://cdn.jsdelivr.net/npm/ol@v7.3.0/dist/ol.js"></script>
</head>

<body>
  <div id="map"></div>
  <div id="controller" role="group" aria-label="Animation controls" style="background: #ececec; padding: 0.5rem;">
    <button id="fast-backward" class="btn btn-primary btn-sm" type="button"><i class="fa fa-fast-backward" style="padding: 0rem 1rem"></i></button>
    <button id="step-backward" class="btn btn-primary btn-sm" type="button"><i class="fa fa-step-backward" style="padding: 0rem 1rem"></i></button>
    <button id="play-pause" class="btn btn-primary btn-sm" type="button"><i class="fa fa-play" style="padding: 0rem 1rem"></i></button>
    <button id="step-forward" class="btn btn-primary btn-sm" type="button"><i class="fa fa-step-forward" style="padding: 0rem 1rem"></i></button>
    <button id="fast-forward" class="btn btn-primary btn-sm" type="button"><i class="fa fa-fast-forward" style="padding: 0rem 1rem"></i></button>
    <span id="info" style="padding-left: 0.5rem;"></span>
  </div>

  <script src="./tutorial.js"></script>
</body>
</html>
```

Much like the previous examples, the above HTML loads the OpenLayers JavaScript and CSS libraries, as well as the Bootstrap and Font Awesome CSS used to display the different buttons in the animation controller. An additional `#controller` container is created below the map and contains the fast-backward, step-backward, play-pause, step-forward, and fast-forward buttons, as well as a `<span>` element used to display the currently displayed timestep.

### JavaScript

```javascript
/* Name of the file: tutorial.js */

const parser = new DOMParser();

// Async function used to retrieve start and end time from RADAR_1KM_RRAI layer GetCapabilities document
async function getRadarStartEndTime() {
  let response = await fetch('https://geo.weather.gc.ca/geomet/?lang=en&service=WMS&request=GetCapabilities&version=1.3.0&LAYERS=RADAR_1KM_RRAI&t=' + new Date().getTime())
  let data = await response.text().then(
    data => {
      let xml = parser.parseFromString(data, 'text/xml');
      let [start, end] = xml.getElementsByTagName('Dimension')[0].innerHTML.split('/');
      let default_ = xml.getElementsByTagName('Dimension')[0].getAttribute('default');
      return [start, end, default_];
    }
  )
  return [new Date(data[0]), new Date(data[1]), new Date(data[2])];
}

let frameRate = 1.0;
let animationId = null;
let startTime = null;
let endTime = null;
let defaultTime = null;
let currentTime = null;

let layers = [
  new ol.layer.Tile({
    source: new ol.source.OSM()
  }),
  new ol.layer.Image({
    source: new ol.source.ImageWMS({
      format: 'image/png',
      url: 'https://geo.weather.gc.ca/geomet/',
      params: {'LAYERS': 'RADAR_1KM_RRAI', 'TILED': true},
      crossOrigin: 'Anonymous'
    })
  }),
  new ol.layer.Image({
    source: new ol.source.ImageWMS({
      format: 'image/png',
      url: 'https://geo.weather.gc.ca/geomet/',
      params: {'LAYERS': 'RADAR_COVERAGE_RRAI.INV', 'TILED': true},
      transition: 0,
      crossOrigin: 'Anonymous'
    })
  })
];

let map = new ol.Map({
  target: 'map',
  layers: layers,
  view: new ol.View({
    center: ol.proj.fromLonLat([-97, 57]),
    zoom: 3
  })
});

// If the image couldn't load due to a change in the time extent, get the new time extent
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
  layers[2].getSource().updateParams({'TIME': currentTime.toISOString().split('.')[0]+"Z"});
}

function updateInfo() {
  let el = document.getElementById('info');
  el.innerHTML = `Time / Heure: ${currentTime.toISOString().substr(0, 16)+"Z"}`
}

// Disable/enable buttons depending on the state of the map
function updateButtons() {
  if (animationId !== null) {
    disableButtons([fastBackwardButton, stepBackwardButton, stepForwardButton, fastForwardButton]);
    enableButtons([playPauseButton]);
  } else {
    if (currentTime <= startTime) {
      disableButtons([fastBackwardButton, stepBackwardButton]);
      enableButtons([playPauseButton, stepForwardButton, fastForwardButton]);
    } else if (currentTime >= endTime) {
      disableButtons([playPauseButton, stepForwardButton, fastForwardButton]);
      enableButtons([fastBackwardButton, stepBackwardButton]);
    } else {
      enableButtons([fastBackwardButton, stepBackwardButton, playPauseButton, stepForwardButton, fastForwardButton]);
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
    currentTime.setUTCMinutes(currentTime.getUTCMinutes() + 6);
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
    currentTime = new Date(startTime);
    updateLayers();
    updateInfo();
    updateButtons();
  }
}

function stepBackward() {
  if (animationId == null && currentTime > startTime) {
    currentTime = new Date(currentTime);
    currentTime.setUTCMinutes(currentTime.getUTCMinutes() - 6);
    updateLayers();
    updateInfo();
    updateButtons();
  }
}

function stepForward() {
  if (animationId == null && currentTime < endTime) {
    currentTime = new Date(currentTime);
    currentTime.setUTCMinutes(currentTime.getUTCMinutes() + 6);
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
```

In the JavaScript code, an async function is created to retrieve the start, end, and default time currently available for the weather radar data (`RADAR_1KM_RRAI`). When a response is received, the `DOMParser()` is used to retrieve the content of the GetCapabilities `<Dimension>` tag and returns an array containing three datetime objects representing the start, end, and default time of the available weather radar data.

Much like the other OpenLayers above, an array of layers is defined and passed to the `ol.Map` constructor.

The time extent (i.e start and end time) of the layers is regularly updated, which means some images will not be able to load since data for an expired time step is no longer available. This situation is identified when a layer fires an `imageloaderror` event, and the async function is called once again to retrieve the updated start, end, and default time. 

The `updateButtons()` function modifies the HTML tags of the buttons in order to deactivate/reactivate them depending on the state of the map. As an example, the fast-backward, step-backward, step-forward, and fast-forward buttons are deactivated whenever the map animation is active.

The `setTime()` function is used to increase the current time by 6 minutes, in order to retrieve the next available timestep. If the current time is greater than or equal to the retrieved end time, the `togglePlayPause()` function is called to stop the animation.

The `togglePlayPause()` function allows to switch between the play and pause buttons depending on the state of the map. When the map animation is active, the button shows a pause sign which allows the user to deactivate the animation. When the map animation is inactive, the button shows a play sign which, when pressed, calls the `setTime()` function at a regular interval in order to constantly increase the timestep.

The `fastBackward()`, `stepBackward()`, `stepForward()`, and `fastForward()` functions respectively allow the user to go the start of the time extent, to the previous timestep, to the next timestep, and to the end of the time extent. They all call the `updateLayers()`, `updateInfo()`, and `updateButtons()` functions which updates the layers and the displayed timestep, as well as deactivates the appropriate buttons. The buttons in the HTML are then associated to their respective function with click Event Listeners.

Finally, the map is initialized by calling `getRadarStartEndTime()` to set the startTime, endTime, defaultTime, and currentTime variables.

See the live example below:

<iframe height="300" style="width: 100%;" scrolling="no" title="GeoMet WMS Time Openlayers Example" src="https://codepen.io/eccc-msc/embed/NWGdVRp?height=265&theme-id=light&default-tab=js,result" frameborder="no" allowtransparency="true" allowfullscreen="true" loading="lazy">
  See the Pen <a href='https://codepen.io/eccc-msc/pen/NWGdVRp'>GeoMet WMS Time Openlayers Example</a> by ECCC-MSC
  (<a href='https://codepen.io/eccc-msc'>@eccc-msc</a>) on <a href='https://codepen.io'>CodePen</a>.
</iframe>
