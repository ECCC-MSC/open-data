let activeMetNote = 1;
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
  let metnotes = document.querySelectorAll(`[id^="metnote-"]`);
  if (activeMetNote > 1) {
    activeMetNote--
  }
  if (activeMetNote === 1) {
    navLeftBtn.disabled = true;
    navRightBtn.disabled = false;
  } else {
    navLeftBtn.disabled = true;
    navRightBtn.disabled = true;
  }
  for (metnote of metnotes) {
    metnote_num = parseInt(metnote.id.split("-")[1])
    if (metnote_num !== activeMetNote) {
      metnote.style.display = "none";
    } else {
      metnote.style.display = "";
    }
  }
  navText.innerText = `${activeMetNote} of ${metnotes.length}`
}

navRightBtn.onclick = () => {
  let metnotes = document.querySelectorAll(`[id^="metnote-"]`);
  if (activeMetNote < metnotes.length) {
    activeMetNote++
  }
  if (activeMetNote === metnotes.length) {
    navRightBtn.disabled = true;
    navLeftBtn.disabled = false;
  } else {
    navRightBtn.disabled = true;
    navLeftBtn.disabled = true;
  }
  for (metnote of metnotes) {
    metnote_num = parseInt(metnote.id.split("-")[1])
    if (metnote_num !== activeMetNote) {
      metnote.style.display = "none";
    } else {
      metnote.style.display = "";
    }
  }
  navText.innerText = `${activeMetNote} of ${metnotes.length}`
}

let layers = [
  new ol.layer.Tile({
    source: new ol.source.OSM()
  }),
  new ol.layer.Tile({
    opacity: 0.4,
    source: new ol.source.TileWMS({
      url: "https://geo.weather.gc.ca/geomet",
      params: {
        LAYERS: "METNOTES",
        TILED: true
      },
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
    zoom: 3
  })
});

map.on("singleclick", function (evt) {
  // reset state
  nav.style.display = 'none'
  navLeftBtn.disabled = true;
  navRightBtn.disabled = false;
  activeMetNote = 1
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
  content.innerHTML = '<p align="center">Loading...</p>';
  overlay.setPosition(evt.coordinate);
  if (url) {
    fetch(url)
      .then(function (response) {
        return response.json();
      })
      .then(function (json) {
        if (json.features.length === 0) {
          content.innerHTML = `<p align="center">No MetNote available...</p>`;
        } else {
          let metnotes = json.features.map((e, i) => {
            let metnote_status = e.properties.metnote_status;
            let content_en = e.properties.content_en;
            let start_datetime = luxon.DateTime.fromISO(e.properties.start_datetime)
              .toUTC()
              .toISO({ suppressMilliseconds: true })
            let end_datetime = luxon.DateTime.fromISO(e.properties.end_datetime)
              .toUTC()
              .toISO({ suppressMilliseconds: true })
            return `
            <div id=metnote-${i + 1} ${i > 0 ? "style='display: none;'" : ""}>
              ${json.features.length > 1 ? `<b>MetNote #${i + 1}</b> <br><br>` : ``}
              Status: <span style="text-transform: capitalize;">${metnote_status}</span><br>
              <br>
              Start: ${start_datetime}<br>
              End: ${end_datetime}<br>
              <br>
              ${content_en}
           </div>
          `;
          });
          if (json.features.length > 1) {
            navText.innerText = `${activeMetNote} of ${json.features.length}`
            nav.style.display = 'flex';
            nav.style.justifyContent = 'center';
            nav.style.flexDirection = 'column';
            nav.style.alignItems = 'center';
          }
          content.innerHTML = `
            ${metnotes.join("")}
          `;
        }
      });
  }
});