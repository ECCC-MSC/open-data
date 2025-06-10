[En français](ice_storms_fr.md)

![ECCC logo](../img_eccc-logo.png)

[TOC](../readme_en.md) > [Data themes](readme_en.md) > Ice storms

# Ice storms&emsp;<i class="wi wi-rain-mix" style="font-size: 45px; color: #4e64a6;"></i>

This page presents a list of relevant Meteorological Service of Canada datasets under the theme of ice storms, in order to guide users to the appropriate datasets. This list is not exhaustive, but provides an overview of the layers that can be used under this theme. The main data layers for this theme are the freezing precipitation variables. However, a number of other relevant layers can also provide additional information on the subject, such as wind factors, winter precipitation types or temperature, to name but a few.

Example of an interactive map featuring the Web Map Service (WMS) layers `Weather Warnings`, `HRDPS-WEonG` (Dominant Precipitation Type) and `HRDPS-WEonG` (Probability of Freezing Rain) (active on the map), as well as other optional layers that can be added by checking the boxes in the list in the map. The layers are served by MSC GeoMet :

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
          <span onmouseover="updateLegend('https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=ALERTS&format=image/png')">Weather Alerts</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer1" checked>
          <span onmouseover="updateLegend('https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=GDPS-WEonG_15km_DominantPrecipType&format=image/png&STYLE=DominantPrecipType_Dis')">Dominant precipitation type</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer2" checked>
          <span onmouseover="updateLegend('https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=GDPS-WEonG_15km_FreezingRain-Prob&format=image/png&STYLE=FreezingRain-Prob')">Probability of freezing rain</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer5">
          <span onmouseover="updateLegend('https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=REPS.DIAG.6_PRMM.ERMEAN&format=image/png&STYLE=REPS_PRMM-LINEAR')">Quantity of precipitation</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer3">
          <span onmouseover="updateLegend('https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=GDPS-WEonG_15km_WindGust&format=image/png&STYLE=GUST_INTERV_MS2KTS')">Gust</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer6">
          <span onmouseover="updateLegend('https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=Radar_1km_SfcPrecipType&format=image/png&STYLE=SfcPrecipType_Dis')">Radar - precipitation type</span>
        </label></br>
    </div>
  </div>
</div>
</br>

## Datasets

It should be noted that the various layers presented in the list are available at different resolutions and timeframes.
The layers in the following list can also be viewed on MSC AniMet with a single [permalink](https://eccc-msc.github.io/msc-animet/?layers=GEPS.DIAG.12_FRMM.ERGE5;0.75;1;1;0,GEPS.DIAG.12_FRMM.ERGE15;0.75;0;1;0,GEPS.DIAG.12_FRMM.ERGE30;0.75;0;1;0,GEPS.DIAG.12_FRMM.ERMEAN;0.75;0;1;0,GEPS.DIAG.12_PEMM.ERGE5;0.75;0;1;0,GEPS.DIAG.12_PEMM.ERGE15;0.75;0;1;0,GEPS.DIAG.12_PEMM.ERGE30;0.75;0;1;0,GEPS.DIAG.12_PEMM.ERMEAN;0.75;0;1;0,GEPS.DIAG.12_PRMM.ERGE5;0.75;0;1;0,GEPS.DIAG.12_PRMM.ERGE15;0.75;0;1;0,GEPS.DIAG.12_PRMM.ERGE30;0.75;0;1;0,REPS.DIAG.6_FRMM.ERGE5;0.75;0;1;0,REPS.DIAG.6_FRMM.ERGE15;0.75;0;1;0,REPS.DIAG.6_FRMM.ERGE30;0.75;0;1;0,REPS.DIAG.6_FRMM.ERMEAN;0.75;0;1;0,REPS.DIAG.6_PEMM.ERGE5;0.75;0;1;0,REPS.DIAG.6_PEMM.ERGE15;0.75;0;1;0,REPS.DIAG.6_PEMM.ERGE30;0.75;0;1;0,REPS.DIAG.6_PEMM.ERMEAN;0.75;0;1;0,REPS.DIAG.6_PRMM.ERGE5;0.75;0;1;0,REPS.DIAG.6_PRMM.ERGE15;0.75;0;1;0,REPS.DIAG.6_PRMM.ERGE30;0.75;0;1;0,REPS.DIAG.6_PRMM.ERMEAN;0.75;0;1;0,GDPS-WEonG_15km_WindSpeed;0.75;0;1;0,GDPS-WEonG_15km_WindGust;0.75;0;1;0,GDPS-WEonG_15km_WindDir;0.75;0;1;0,GDPS-WEonG_15km_Precip-Prob;0.75;0;1;0,GDPS-WEonG_15km_InstantPrecipType;0.75;0;1;0,GDPS-WEonG_15km_IcePellets-Prob;0.75;0;1;0,GDPS-WEonG_15km_FreezingRain-Prob;0.75;0;1;0,GDPS-WEonG_15km_FreezingPrecip-Prob;0.75;0;1;0,GDPS-WEonG_15km_DominantPrecipType;0.75;0;1;0,GDPS-WEonG_15km_DewPointTemp;0.75;0;1;0,GDPS-WEonG_15km_AirTemp;0.75;0;1;0,CURRENT_CONDITIONS;0.75;0;1;0,ALERTS;0.75;0;1;0,Radar_1km_SfcPrecipType;0.75;0;1;0,Radar-Coverage_SfcPrecipType;0.75;0;1;0,Radar_1km_dBZ-Extrapolation;0.75;0;1;0&extent=-17028947,1084196,-370327,9328911) for all variables.

##### &emsp;<span class="badge badge-info">HRDPS - Weather Elements on Grid</span>
###### &emsp;[HRDPS data documentation](../msc-data/nwp_hrdps/readme_hrdps_en.md)
* Temperature
* Dew point temperature
* Dominant precipitation type
* Probability of freezing precipitation
* Probability of freezing rain
* Probability of ice pellets
* Instantaneous precipitation type
* Probability of precipitation
* Wind direction
* Gust
* Wind speed</br>

##### &emsp;<span class="badge badge-info">GEPS - diagnostic fields</span>
###### &emsp;[GEPS data documentation](../msc-data/nwp_geps/readme_geps_en.md)
* Probability of quantity of ice pellets over 5 mm (12 hours)
* Probability of quantity of ice pellets over 15 mm (12 hours)
* Probability of quantity of ice pellets over 30 mm (12 hours)
* Ice pellets (12 hours - mean)
* Probability of quantity of freezing rain over 5 mm (12 hours)
* Probability of quantity of freezing rain over 15 mm (12 hours)
* Probability of quantity of freezing rain over 30 mm (12 hours)
* Freezing rain (12 hours - mean)
* Probability of quantity of precipitation over 5 mm (12 hours)
* Probability of quantity of precipitation over 15 mm (12 hours)
* Probability of quantity of precipitation over 30 mm (12 hours)</br>

##### &emsp;<span class="badge badge-info">REPS - diagnostic fields</span>
###### &emsp;[REPS data documentation](../msc-data/nwp_reps/readme_reps_en.md)
* Probability of quantity of ice pellets over 5 mm (6 hours)
* Probability of quantity of ice pellets over 15 mm (6 hours)
* Probability of quantity of ice pellets over 30 mm (6 hours)
* Ice pellets (6 hours - mean)
* Probability of quantity of freezing rain over 5 mm (6 hours)
* Probability of quantity of freezing rain over 15 mm (6 hours)
* Probability of quantity of freezing rain over 30 mm (6 hours)
* Freezing rain (6 hours - mean)
* Probability of quantity of precipitation over 5 mm (6 hours)
* Probability of quantity of precipitation over 15 mm (6 hours)
* Probability of quantity of precipitation over 30 mm (6 hours)
* Quantity of precipitation (6 hours - mean)</br>

##### &emsp;<span class="badge badge-info">Radar</span>
###### &emsp;[Radar data documentation](../msc-data/obs_radar/readme_radar_en.md)
* Radar surface precipitation type (experimental)
* Radar extrapolation precipitation rate (experimental)
* Dynamic radar coverage for surface precipitation type (expérimental)</br>

##### &emsp;<span class="badge badge-info">Others</span>

* [Weather Alerts](../msc-data/alerts/readme_alerts_en.md)
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
        js.src = "../../js/ice_storms_theme_ie.js";
        document.getElementById("controller").setAttribute("hidden", true);
    }
    else
    {
        js.src = "../../js/ice_storms_theme.js";
    }
    head.appendChild(js);
</script>