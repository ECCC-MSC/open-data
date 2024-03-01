[En français](drought_fr.md)

![ECCC logo](../img_eccc-logo.png)

[TOC](../readme_en.md) > [Data themes](readme_en.md) > Drought

# Drought&emsp;<i class="wi wi-hot" style="font-size: 45px; color: #4e64a6;"></i>

This page presents a list of relevant Meteorological Service of Canada datasets under the Heat Waves theme, in order to guide users to the appropriate datasets. This list is not exhaustive, but provides an overview of the layers that can be used under this theme. The main data layers for this theme are temperature and precipitation quantities. However, a number of other relevant layers can also provide additional information on the subject, such as runoff or precipitable water contained in clouds, to name but two examples.

Example of an interactive map featuring the Web Map Service (WMS) layers `HRDPS-WEonG` (Temperature), `Weather Alerts` and `Current Conditions` (active on the map), as well as other optional layers that can be added by checking the boxes in the list in the map. The layers are served by MSC GeoMet :

<div id="map" style="height: 500px; position: relative">
  <div id="legend-popup">
    <div id="legend-popup-content">
      <img id="legend-img" src="" />
    </div>
  </div>

  <div id="switch-content" style="position: absolute; z-index: 1; bottom: 40px; left: 8px;">
    <div id="switch-case">
        <label>
          <input type="checkbox" id="layer1" checked>
          <span onmouseover="updateLegend('https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=HRDPS-WEonG_2.5km_AirTemp&format=image/png')">Temperature</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer2" checked>
          <span onmouseover="updateLegend('https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=ALERTS&format=image/png')">Weather Alerts</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer4" checked>
          <span onmouseover="updateLegend('https://geo.weather.gc.ca/geomet?lang=fr&version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=CURRENT_CONDITIONS&format=image/png&STYLE=default')">Current Conditions</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer3">
          <span onmouseover="updateLegend('https://geo.wxod-dev.cmc.ec.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=HRDPS-WEonG_2.5km_Precip-Prob&format=image/png&STYLE=Precip-Prob')">Probability of precipitation</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer6">
          <span onmouseover="updateLegend('https://geo.wxod-dev.cmc.ec.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=REPS.DIAG.3_HMXX.ERMEAN&format=image/png&STYLE=REPS_TT')">Humidex at surface</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer5">
          <span onmouseover="updateLegend('https://geo.wxod-dev.cmc.ec.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=HRDPS.CONTINENTAL_UTCI&format=image/png&STYLE=UTCI-EN')">Universal Thermal Climate Index</span>
        </label></br>
    </div>
  </div>
</div>
</br>

## Datasets

It should be noted that the various layers presented in the list are available at different resolutions and timeframes.
The layers in the following list can also be viewed on MSC AniMet with a single [permalink](https://eccc-msc.github.io/msc-animet/?layers=HRDPS-WEonG_2.5km_AirTemp;0.75;1;1;0,HRDPS-WEonG_2.5km_DewPointTemp;0.75;0;1;0,HRDPS-WEonG_2.5km_Precip-Prob;0.75;0;1;0,HRDPS-WEonG_2.5km_SkyState;0.75;0;1;0,HRDPS.CONTINENTAL_HU;0.75;0;1;0,HRDPS.CONTINENTAL_IH;0.75;0;1;0,HRDPS.CONTINENTAL_NT;0.75;0;1;0,REPS.DIAG.3_HMXX.ERMEAN;0.75;0;1;0,HRDPS.CONTINENTAL_I0;0.75;0;1;0,CURRENT_CONDITIONS;0.75;0;1;0,ALERTS;0.75;0;1;0,HRDPS.CONTINENTAL_UTCI;0.75;0;1;0,HRDPS-WEonG_2.5km_WindSpeed;0.75;0;1;0,REPS.DIAG.6_RNMM.ERMEAN;0.75;0;1;0&extent=-22417283,465184,1337032,12221714) for all variables.

##### &emsp;<span class="badge badge-info">HRDPS at surface/near-surface fields</span>
###### &emsp;[HRDPS data documentation](../msc-data/nwp_hrdps/readme_hrdps_en.md)
* Surface and soil temperatures (Superficial)
* Total cloud cover
* Cloud water
* Specific Humidity at the surface
* Universal Thermal Climate Index (UTCI)</br>

##### &emsp;<span class="badge badge-info">HRDPS - Weather Elements on Grid</span>
###### &emsp;[HRDPS data documentation](../msc-data/nwp_hrdps/readme_hrdps_en.md)
* Wind speed
* Sky state day/night (combined cloud cover and opacity)
* Probability of precipitation
* Dew point temperature
* Temperature</br>

##### &emsp;<span class="badge badge-info">REPS - diagnostic fields</span>
###### &emsp;[REPS data documentation](../msc-data/nwp_reps/readme_reps_en.md)
* Humidex at surface (mean)
* Rain (mean)</br>

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
        js.src = "../../../js/drought_theme_ie.js";
        document.getElementById("controller").setAttribute("hidden", true);
    }
    else
    {
        js.src = "../../../js/drought_theme.js";
    }
    head.appendChild(js);
</script>