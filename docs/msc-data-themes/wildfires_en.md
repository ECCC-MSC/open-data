[En français](wildfires_fr.md)

![ECCC logo](../img_eccc-logo.png)

[TOC](../readme_fr.md) > [Data themes](readme_en.md) > Wildfires

# Wildfires&emsp;<i class="wi wi-fire" style="font-size: 45px; color: #4e64a6;"></i>


This page presents a list of relevant Meteorological Service of Canada datasets under the theme of wildfires, in order to guide users to the appropriate datasets. This list is not exhaustive, but provides an overview of the layers that can be used under this theme. The main data layers for this theme are air quality variables and precipitation rates. However, a number of other relevant layers can also provide additional information on the subject, such as hotspots, wind speed or wind direction, to name but a few.

Example of an interactive map featuring the Web Map Service (WMS) layers `Wildfire Hotspots`, `HRDPS-WEonG - Gust` and `RAQDPS - NO2 Concentration` (active on the map), as well as other optional layers that can be added by checking the boxes in the list in the map. The layers are served by MSC GeoMet.

Layers shown in the preview below can also be viewed on MSC AniMet via a single [permalink](https://eccc-msc.github.io/msc-animet/?layers=RAQDPS.SFC_O3;0.75;0;0;0;1,RADAR_1KM_RRAI;0.75;0;0;0;1,RAQDPS.SFC_PM2.5;0.75;0;0;0;1,RAQDPS.SFC_NO2;0.75;0;1;0;1,HRDPS-WEonG_2.5km_WindGust;0.75;0;1;0;1,WildfireHotspots;0.75;0;1;0;1) for all variables.


<div id="map" style="height: 500px; position: relative">
  <div id="legend-popup">
    <div id="legend-popup-content">
      <img id="legend-img" style="display: flex; max-height: 400px;" src="" />
    </div>
  </div>

  <div id="switch-content" style="position: absolute; z-index: 1; bottom: 40px; left: 8px;">
    <div id="switch-case">
        <label>
          <input type="checkbox" id="layer4" checked>
          <span onmouseover="updateLegend('https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=WildfireHotspots&format=image/png')">Hot spots</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer1" checked>
          <span onmouseover="updateLegend('https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=HRDPS-WEonG_2.5km_WindGust&format=image/png&STYLE=GUST_INTERV_MS2KTS')">Gust</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer2" checked>
          <span onmouseover="updateLegend('https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=RAQDPS.SFC_NO2&format=image/png&STYLE=SFC-NO2')">Concentration: NO2</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer5">
          <span onmouseover="updateLegend('https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=RAQDPS.SFC_PM2.5&format=image/png&STYLE=PM2.5_0to100ugm3_Dis')">Concentration : PM2.5</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer3">
          <span onmouseover="updateLegend('https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=RADAR_1KM_RRAI&format=image/png&STYLE=Radar-Rain_Dis-14colors_Fr')">Radar precipitation rate</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer6">
          <span onmouseover="updateLegend('https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=RAQDPS.SFC_O3&format=image/png&STYLE=SFC-O3')">Concentration: O3</span>
        </label></br>
    </div>
  </div>
</div>
</br>


## Datasets

It should be noted that the various layers presented in the list are available at different resolutions and timeframes.


##### &emsp;<span class="badge badge-info">HRDPS at surface/near-surface fields</span>
###### &emsp;[HRDPS data documentation](../msc-data/nwp_hrdps/readme_hrdps_en.md)
* Convective preciptation</br>

##### &emsp;<span class="badge badge-info">HRDPS - Weather Elements on Grid</span>
###### &emsp;[HRDPS data documentation](../msc-data/nwp_hrdps/readme_hrdps_en.md)
* Probability of thunderstorm occurence
* Wind speed
* Wind direction
* Gust
* Temperature
* Probability of precipitation</br>

##### &emsp;<span class="badge badge-info">GEPS diagnostic fields</span>
###### &emsp;[GEPS data documentation](../msc-data/nwp_geps/readme_geps_en.md)
* Probability of quantity of precipitation over 1 mm (120 hours)
* Probability of quantity of precipitation over 5 mm (120 hours)
* Probability of quantity of precipitation over 10 mm (120 hours)</br>

##### &emsp;<span class="badge badge-info">Radar</span>
###### &emsp;[Radar data documentation](../msc-data/obs_radar/readme_radar_en.md)
* Radar precipitation rate for rain
* Radar extrapolation precipitation rate for rain
* Radar extrapolation precipitation rate</br>

##### &emsp;<span class="badge badge-info">Satellite</span>
###### &emsp;[Satellite data documentation](../msc-data/obs_satellite/readme_satellite_en.md)
* Natural colour product
* Night Microphysics product
* Fire Temperature product
* Day Land Cloud Fire product
* Smoke ABI Band1 product
* SWIR product</br>

##### &emsp;<span class="badge badge-info">RAQDPS</span>
###### &emsp;[RAQDPS data documentation](../msc-data/nwp_raqdps/readme_raqdps_en.md)
* Wildfire hotspots ingested by RAQDPS
* Concentration : surface NO2
* Concentration : surface O3
* Concentration : surface PM2.5</br>

##### &emsp;<span class="badge badge-info">Others</span>

* [Weather Alerts](../msc-data/alerts/readme_alerts_en.md)
* [Current Conditions](../msc-data/citypage-weather/readme_citypageweather_en.md)
* [Lightning Flash Density over Canada](../msc-data/lightning/readme_lightning_en.md)


<style>
  #legend-img {
    margin: 0px;
  }
  #legend-popup {
    position: absolute;
    top: 40px;
    right: 8px;
    z-index: 2;
  }
  .legend-switch{
    top: 8px;
    right: .5em;
  }
  .ol-touch .legend-switch {
    top: 80px;
  }
 #switch-content {
  background-color: white;
  border-radius: 6px;
  padding: 7px;
 }
 label {
  font-size: 14px;
  margin-bottom: 0px;
 }
 input[type="checkbox"] {
  width: 14px;
  height: 14px;
 }
</style>

<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/ol@v7.3.0/ol.css" type="text/css"/>
<link rel="stylesheet" href="../../css/weather-icons-master/css/weather-icons.min.css">
<script src="https://cdn.polyfill.io/v2/polyfill.min.js?features=requestAnimationFrame,Element.prototype.classList,URL"></script>
<script src="https://cdn.jsdelivr.net/npm/ol@v7.3.0/dist/ol.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/FileSaver.js/1.3.3/FileSaver.min.js"></script>
<script>
    function isIE() {
      return window.navigator.userAgent.match(/(MSIE|Trident)/);
    }
    var head = document.getElementsByTagName('head')[0];
    var js = document.createElement("script");
    js.type = "text/javascript";
    if (isIE())
    {
        js.src = "../../js/wildfires_theme_ie.js";
        document.getElementById("controller").setAttribute("hidden", true);
    }
    else
    {
        js.src = "../../js/wildfires_theme.js";
    }
    head.appendChild(js);
</script>