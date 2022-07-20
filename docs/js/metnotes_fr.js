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
    zoom: 0
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
      INFO_FORMAT: "text/plain",
      FEATURE_COUNT: 10
    }
  );
  content.innerHTML = '<p align="center">Chargement...</p>';
  overlay.setPosition(evt.coordinate);
  if (url) {
    fetch(url)
      .then(function (response) {
        return response.text();
      })
      .then(function (text) {
        let features = text.match(/Feature\s.*/g);
        if (features === null) {
          content.innerHTML = `<p align="center">Aucun MetNote disponible...</p>`;
        } else {
          let metnotes = features.map((e, i) => {
            let metnote_status = text
              .match(/metnote_status.*\n/g)[i].split(" = ")[1]
              .replace(/'/g, "");
            let content_en = text
              .match(/content_en.*\n/g)[i].split(" = ")[1]
              .replace(/'/g, "");
            let start_datetime = luxon.DateTime.fromFormat(
                text
                .match(/start_datetime.*\n/g)[i].split(" = ")[1]
                .replace(/'/g, "")
                .trim(),
                "yyyy/mm/dd HH:mm:ssZ"
              )
              .toUTC()
              .toISO({
                suppressMilliseconds: true
              });
            let end_datetime = luxon.DateTime.fromFormat(
                text
                .match(/end_datetime.*\n/g)[i].split(" = ")[1]
                .replace(/'/g, "")
                .trim(),
                "yyyy/mm/dd HH:mm:ssZ"
              )
              .toUTC()
              .toISO({
                suppressMilliseconds: true
              });
            return `
            <div id=metnote-${i + 1} ${i > 0 ? "style='display: none;'" : ""}>
              ${features.length > 1 ? `<b>MetNote #${i + 1}</b> <br><br>` : ``}
              Statut: <span style="text-transform: capitalize;">${metnote_status}</span><br>
              <br>
              Début: ${start_datetime}<br>
              Fin: ${end_datetime}<br>
              <br>
              ${content_en}
           </div>
          `;
          });
          if (features.length > 1) {
            navText.innerText = `${activeMetNote} of ${features.length}`
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