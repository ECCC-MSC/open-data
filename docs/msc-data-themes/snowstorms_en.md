[En français](snowstorms_fr.md)

![ECCC logo](../img_eccc-logo.png)

[TOC](../readme_en.md) > [Data themes](readme_en.md) > Snowstorms

# Snowstorms&emsp;<i class="wi wi-snow-wind" style="font-size: 45px; color: #4e64a6;"></i>

This page presents a list of relevant Meteorological Service of Canada datasets under the theme of snowstorms, in order to guide users to the appropriate datasets. This list is not exhaustive, but provides an overview of the layers that can be used under this theme. The main data layers for this theme are the snow quantity variables. However, a number of other relevant layers can also provide additional information on the subject, such as wind factors, winter precipitation types or temperature, to name but a few.

Example of an interactive map featuring the Web Map Service (WMS) layers `Weather Warnings`, `RDPS.ETA` (Accumulated Snow) and `Current Conditions` (active on the map), as well as other optional layers that can be added by checking the boxes in the list in the map. The layers are served by MSC GeoMet:

<div id="map" style="height: 500px; position: relative">
  <div id="legend-popup">
    <div id="legend-popup-content">
      <img id="legend-img" src="" />
    </div>
  </div>

  <div id="switch-content" style="position: absolute; z-index: 1; bottom: 40px; left: 8px;">
    <div id="switch-case">
        <label>
          <input type="checkbox" id="layer4" checked>
          <span onmouseover="updateLegend('https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=ALERTS&format=image/png')">Weather Alerts</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer1" checked>
          <span onmouseover="updateLegend('https://geo.wxod-dev.cmc.ec.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=RDPS.ETA_SN&format=image/png&STYLE=PRECIPSNOW')">Snow accumulation</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer2" checked>
          <span onmouseover="updateLegend('https://geo.wxod-dev.cmc.ec.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=CURRENT_CONDITIONS&format=image/png&STYLE=default')">Current Conditions</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer5">
          <span onmouseover="updateLegend('https://geo.wxod-dev.cmc.ec.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=RDPS-WEonG_10km_BlowingSnow-Prob&format=image/png&STYLE=BlowingSnow-Prob')">Probability of blowing snow</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer3">
          <span onmouseover="updateLegend('https://geo.wxod-dev.cmc.ec.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=RDPS-WEonG_10km_AirTemp&format=image/png&STYLE=TEMPERATURE-LINEAR')">Temperature</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer6">
          <span onmouseover="updateLegend('https://geo.wxod-dev.cmc.ec.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=RADAR_1KM_RSNO&format=image/png&STYLE=Radar-Snow_Dis-14colors')">Radar for snow</span>
        </label></br>
    </div>
  </div>
</div>
</br>

## Datasets

It should be noted that the various layers presented in the list are available at different resolutions and timeframes.
The layers in the following list can also be viewed on MSC AniMet with a single [permalink](https://eccc-msc.github.io/msc-animet/?layers=CURRENT_CONDITIONS;0.75;0;1;0,Radar_1km_SnowPrecipRate-Extrapolation;0.75;1;1;0,RDPS.ETA_TT;0.75;0;1;0,RDPS.ETA_SN;0.75;0;1;0,RDPS.ETA_WD;0.75;0;1;0,RDPS.ETA_WGE;0.75;0;1;0,ALERTS;0.75;0;1;0,RDPS.ETA_WSPD;0.75;0;1;WindSpeed_30-210Knots_Dis,RDPS-WEonG_10km_AirTemp;0.75;0;1;0,RDPS-WEonG_10km_BlowingSnowPresence;0.75;0;1;0,RDPS-WEonG_10km_BlowingSnow-Prob;0.75;0;1;0,RDPS-WEonG_10km_Snow-Prob;0.75;0;1;0,RDPS-WEonG_10km_SnowSqualls-Prob;0.75;0;1;0,RDPS-WEonG_10km_SnowHeight;0.75;0;1;0,RADAR_1KM_RSNO;0.75;0;1;0,REPS.DIAG.12_SNMM.ERGE30;0.75;0;1;0,REPS.DIAG.12_SNMM.ERGE15;0.75;0;1;0,REPS.DIAG.12_PRMM.ERGE15;0.75;0;1;0,REPS.DIAG.12_PRMM.ERGE30;0.75;0;1;0,REPS.DIAG.3_PRMM.ERGE15;0.75;0;1;0,REPS.DIAG.3_PRMM.ERMEAN;0.75;0;1;0,REPS.DIAG.24_SNMM.ERGE20;0.75;0;1;0,REPS.DIAG.24_SNMM.ERGE25;0.75;0;1;0,REPS.DIAG.24_PEMM.ERGE20;0.75;0;1;0,GEPS.DIAG.12_PEMM.ERGE30;0.75;0;1;0,GEPS.DIAG.24_SNMM.ERGE20;0.75;0;1;0,GEPS.DIAG.24_SNMM.ERGE25;0.75;0;1;0,GEPS.DIAG.24_PEMM.ERGE20;0.75;0;1;0,GEPS.DIAG.24_PEMM.ERGE30;0.75;0;1;0,REPS.DIAG.12_PEMM.ERGE30;0.75;0;1;0,REPS.DIAG.12_PEMM.ERGE15;0.75;0;1;0,REPS.DIAG.12_PEMM.ERGE5;0.75;0;1;0,GEPS.DIAG.12_PEMM.ERGE15;0.75;0;1;0,GEPS.DIAG.12_PEMM.ERGE5;0.75;0;1;0&extent=-17412813,2741278,-274277,11223514) for all variables.

##### &emsp;<span class="badge badge-info">HRDPS - Weather Elements on Grid</span>
###### &emsp;[HRDPS data documentation](../msc-data/nwp_hrdps/readme_hrdps_en.md)
* Height of snow level
* Probability of quantity of snow squalls
* Probability of quantity of snow
* Probability of blowing snow
* Presence of blowing snow
* Temperature</br>

##### &emsp;<span class="badge badge-info">RDPS at surface/near-surface fields</span>
###### &emsp;[RDPS data documentation](../msc-data/nwp_rdps/readme_rdps_en.md)
* Wind speed
* Wind gust estimate
* Wind direction
* Snow accumulation
* Air temperature</br>

##### &emsp;<span class="badge badge-info">GEPS - diagnostic fields</span>
###### &emsp;[GEPS data documentation](../msc-data/nwp_geps/readme_geps_en.md)
* Probability of quantity of ice pellets over 5 mm (12 hours)
* Probability of quantity of ice pellets over 15 mm (12 hours)
* Probability of quantity of ice pellets over 30 mm (12 hours)
* Probability of quantity of ice pellets over 20 mm (24 hours)
* Probability of quantity of ice pellets over 30 mm (24 hours)
* Probability of quantity of snow over 20 mm (24 hours)
* Probability of quantity of snow over 25 mm (24 hours)</br>

##### &emsp;<span class="badge badge-info">REPS - diagnostic fields</span>
###### &emsp;[REPS data documentation](../msc-data/nwp_reps/readme_reps_en.md)
* Quantity of precipitation (mean)
* Probability of quantity of precipitation over 15 mm (3 hours)
* Probability of quantity of precipitation over 15 mm (12 hours)
* Probability of quantity of precipitation over 30 mm (12 hours)
* Probability of quantity of snow over 15 mm (12 hours)
* Probability of quantity of snow over 30 mm (12 hours)
* Probability of quantity of snow over 20 mm (24 hours)
* Probability of quantity of snow over 25 mm (24 hours)
* Probability of quantity of ice pellets over 5 mm (12 hours)
* Probability of quantity of ice pellets over 15 mm (12 hours)
* Probability of quantity of ice pellets over 30 mm (12 hours)
* Probability of quantity of ice pellets over 20 mm (24 hours)
* Probability of quantity of ice pellets over 35 mm (24 hours)</br>

##### &emsp;<span class="badge badge-info">Radar</span>
###### &emsp;[Radar data documentation](../msc-data/obs_radar/readme_radar_en.md)
* Radar precipitation rate for snow
* Radar extrapolation precipitation rate for snow</br>

##### &emsp;<span class="badge badge-info">Others</span>

* [Weather Alerts (experimental)](../msc-data/alerts/readme_alerts_en.md)
* [Current Conditions](../msc-data/citypage-weather/readme_citypageweather_en.md)

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
        js.src = "../../js/snowstorms_theme_ie.js";
        document.getElementById("controller").setAttribute("hidden", true);
    }
    else
    {
        js.src = "../../js/snowstorms_theme.js";
    }
    head.appendChild(js);
</script>