let activeCitypage = 1;
/**
 * Elements that make up the popup.
 */
let container = document.getElementById("popup");
let content = document.getElementById("popup-content");
let closer = document.getElementById("popup-closer");
let nav = document.getElementById("nav");
let navText = document.getElementById("nav-text")
let navLeftBtn = document.getElementById("left-btn")
let navRightBtn = document.getElementById("right-btn")

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

navLeftBtn.onclick = () => {
  let citypages = document.querySelectorAll(`[id^="citypage-"]`);
  if (activeCitypage > 1) {
    activeCitypage--
  }
  if (activeCitypage === 1) {
    navLeftBtn.disabled = true;
    navRightBtn.disabled = false;
  } else {
    navLeftBtn.disabled = false;
    navRightBtn.disabled = false;
  }
  for (citypage_ of citypages) {
    citypage_num = parseInt(citypage_.id.split("-")[1])
    if (citypage_num !== activeCitypage) {
      citypage_.style.display = "none";
    } else {
      citypage_.style.display = "";
    }
  }
  navText.innerText = `${activeCitypage} of ${citypages.length}`
}

navRightBtn.onclick = () => {
  let citypages = document.querySelectorAll(`[id^="citypage-"]`);
  if (activeCitypage < citypages.length) {
    activeCitypage++
  }
  if (activeCitypage === citypages.length) {
    navRightBtn.disabled = true;
    navLeftBtn.disabled = false;
  } else {
    navRightBtn.disabled = false;
    navLeftBtn.disabled = false;
  }
  for (citypage_ of citypages) {
    citypage_num = parseInt(citypage_.id.split("-")[1])
    if (citypage_num !== activeCitypage) {
      citypage_.style.display = "none";
    } else {
      citypage_.style.display = "";
    }
  }
  navText.innerText = `${activeCitypage} of ${citypages.length}`
}

let layers = [
  new ol.layer.Tile({
    source: new ol.source.OSM()
  }),
  new ol.layer.Tile({
    source: new ol.source.TileWMS({
      url: "https://geo.weather.gc.ca/geomet",
      params: {
        LAYERS: "CURRENT_CONDITIONS",
        TILED: true
      },
      transition: 0
    })
  })
];

let map = new ol.Map({
  controls: ol.control.defaults.defaults().extend([new ol.control.ScaleLine()]),
  target: "map",
  layers: layers,
  overlays: [overlay],
  view: new ol.View({
    center: ol.proj.fromLonLat([-97, 57]),
    zoom: 3
  })
});

map.on("singleclick", function (evt) {
  // reset state
  nav.style.display = 'none'
  navLeftBtn.disabled = true;
  navRightBtn.disabled = false;
  activeCitypage = 1;
  overlay.setPosition(undefined);
  // get coordinates
  let coordinate = evt.coordinate;
  let viewResolution = map.getView().getResolution();
  let wms_source = map.getLayers().item(1).getSource();
  let url = wms_source.getFeatureInfoUrl(
    coordinate,
    viewResolution,
    "EPSG:3857", {
    INFO_FORMAT: "application/json",
    FEATURE_COUNT: 10
  }
  );
  if (url) {
    fetch(url)
      .then(function (response) {
        return response.json();
      })
      .then(function (json) {
        if (json.features.length > 0) {
          // only display citypage with actual observed current
          let features_filtered = json.features.filter(
            e => e.properties.station_en !== ''
          )
          if (features_filtered.length > 0) {
            overlay.setPosition(evt.coordinate);
          }
          let citypages = features_filtered.map((e, i) => {
            let citypage_name = e.properties.name;
            let station_en = e.properties.station_en;
            let temperature = e.properties.temp;
            let cond_en = e.properties.cond_en;
            let speed = e.properties.speed;
            let wind_direction = e.properties.direction;
            let dewpoint = e.properties.dewpoint;
            let pres_en = e.properties.pres_en;
            let rel_hum = e.properties.rel_hum;
            return `
            <div id=citypage-${i + 1} ${i > 0 ? "style='display: none;'" : ""}>
              <b>${citypage_name}</b><br><br>
              Station name: ${station_en}<br><br>
              ${cond_en !== '' ? `Condition: ${cond_en}<br>` : ''}
              Air temperature: ${temperature} °C<br>
              Wind: ${wind_direction} ${speed} km/h<br>
              Relative humidity: ${rel_hum} %<br>
              Dew point: ${dewpoint} °C<br>
              Pressure: ${pres_en} kPa<br>

           </div>
          `;
          });
          if (features_filtered.length > 1) {
            navText.innerText = `${activeCitypage} of ${features_filtered.length}`
            nav.style.display = 'flex';
            nav.style.justifyContent = 'center';
            nav.style.flexDirection = 'column';
            nav.style.alignItems = 'center';
          }
          let citypages_join = citypages.join("");
          content.innerHTML = citypages_join;
        }
      });
  }
});