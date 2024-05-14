[En français](thunderstorms_fr.md)

![ECCC logo](../img_eccc-logo.png)

[TOC](../readme_en.md) > [Data themes](readme_en.md) > Thunderstorms

# Thunderstorms&emsp;<i class="wi wi-lightning" style="font-size: 45px; color: #4e64a6;"></i>

This page presents a list of relevant Meteorological Service of Canada datasets under the thunderstroms theme, in order to guide users to the appropriate datasets. This list is not exhaustive, but provides an overview of the layers that can be used under this theme. The main data layers for this theme are wind variables and precipitation quantities. However, a number of other relevant layers can also provide additional information on the subject, such as thunderstorm occurrence probability, showalter or unstable parcel uplift indices, to name but a few examples.

Example of an interactive map featuring the Web Map Service (WMS) layers `HRDPS.CONTINENTAL` (Instantaneous Precipitation Rate), `Weather Warnings` and `HRDPS.CONTINENTAL` (Showalter Index) (active on the map), as well as other optional layers that can be added by checking the boxes in the list in the map. The layers are served by MSC GeoMet :

<div id="map" style="height: 500px; position: relative">
  <div id="legend-popup">
    <div id="legend-popup-content">
      <img id="legend-img" src="" />
    </div>
  </div>

  <div id="switch-content" style="position: absolute; z-index: 1; bottom: 40px; left: 8px;">
    <div id="switch-case">
        <label>
          <input type="checkbox" id="layer2" checked>
          <span onmouseover="updateLegend('https://geo.wxod-dev.cmc.ec.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=HRDPS.CONTINENTAL_RT&format=image/png&STYLE=PRECIPPRTMMH')">Instantaneous precipitation rate</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer4" checked>
          <span onmouseover="updateLegend('https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=ALERTS&format=image/png')">Weather Alerts</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer1" checked>
          <span onmouseover="updateLegend('https://geo.wxod-dev.cmc.ec.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=HRDPS.CONTINENTAL.CONV_SHWINX.500&format=image/png&STYLE=LIFTED_INDEX-LINEAR')">Showalter index</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer3">
          <span onmouseover="updateLegend('https://geo.wxod-dev.cmc.ec.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=HRDPS-WEonG_2.5km_Precip-Prob&format=image/png&STYLE=Precip-Prob')">Probability of precipitation</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer5">
          <span onmouseover="updateLegend('https://geo.wxod-dev.cmc.ec.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=HRDPS-WEonG_2.5km_WindGust&format=image/png&STYLE=GUST_INTERV_MS2KTS')">Gust</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer6">
          <span onmouseover="updateLegend('https://geo.wxod-dev.cmc.ec.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=HRDPS-WEonG_2.5km_Thunderstorm-Prob&format=image/png&STYLE=Thunderstorm-Prob')">Probability of thunderstorm</span>
        </label></br>
    </div>
  </div>
</div>
</br>

## Datasets

It should be noted that the various layers presented in the list are available at different resolutions and timeframes.
The layers in the following list can also be viewed on MSC AniMet with a single [permalink](https://eccc-msc.github.io/msc-animet/?layers=ALERTS;0.75;0;1;0,CURRENT_CONDITIONS;0.75;0;1;0,Lightning_2.5km_Density;0.75;1;1;0,RADAR_1KM_RRAI;0.75;0;1;0,Radar_1km_dBZ-Extrapolation;0.75;0;1;0,HRDPS-WEonG_2.5km_AirTemp;0.75;0;1;0,HRDPS-WEonG_2.5km_DewPointTemp;0.75;0;1;0,HRDPS-WEonG_2.5km_Precip-Prob;0.75;0;1;0,HRDPS-WEonG_2.5km_WindGust;0.75;0;1;0,HRDPS-WEonG_2.5km_WindDir;0.75;0;1;0,HRDPS-WEonG_2.5km_WindSpeed;0.75;0;1;0,HRDPS.CONTINENTAL.CONV_MU-VT-LI.500;0.75;0;1;0,HRDPS.CONTINENTAL.CONV_SHWINX.500;0.75;0;1;0,HRDPS.CONTINENTAL_IH;0.75;0;1;0,HRDPS.CONTINENTAL_PC;0.75;0;1;0,HRDPS.CONTINENTAL_RT;0.75;0;1;0,HRDPS-WEonG_2.5km_Thunderstorm-Prob;0.75;0;1;0&extent=-19347716,1946579,-535293,11257258) for all variables.

##### &emsp;<span class="badge badge-info">HRDPS at surface/near-surface fields</span>
###### &emsp;[HRDPS data documentation](../msc-data/nwp_hrdps/readme_hrdps_en.md)
* Instantaneous precipitation rate
* Convective precipitation
* Cloud water
* Showalter Index, with reference level 500.0 mb
* Lifted index for the most unstable parcel</br>

##### &emsp;<span class="badge badge-info">HRDPS - Weather Elements on Grid</span>
###### &emsp;[HRDPS data documentation](../msc-data/nwp_hrdps/readme_hrdps_en.md)
* Probability of thunderstorm occurence
* Wind speed
* Wind direction
* Gust
* Temperature
* Probability of precipitation
* Dew point temperature</br>

##### &emsp;<span class="badge badge-info">RESPS</span>
###### &emsp;[RESPS data documentation](../msc-data/nwp_resps/readme_resps_en.md)
* Storm surge - Atlantic North West (control member)
* Storm surge - Atlantic North West (1)
* Storm surge - Atlantic North West (2)
* Storm surge - Atlantic North West (3)
* Storm surge - Atlantic North West (4)
* Storm surge - Atlantic North West (5)
* Storm surge - Atlantic North West (6)</br>

##### &emsp;<span class="badge badge-info">Radar</span>
###### &emsp;[Radar data documentation](../msc-data/obs_radar/readme_radar_en.md)
* Radar precipitation rate for rain
* Radar extrapolation precipitation rate</br>

##### &emsp;<span class="badge badge-info">Others</span>

* [Weather Alerts (experimental)](../msc-data/alerts/readme_alerts_en.md)
* [Current Conditions](../msc-data/citypage-weather/readme_citypageweather_en.md)
* [Lightning Flash Density over Canada](../msc-data/lightning/readme_lightning_en.md)
* [GDSPS - Storm surge](../msc-data/nwp_gdsps/readme_gdsps_en.md)


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
        js.src = "../../../js/thunderstorms_theme_ie.js";
        document.getElementById("controller").setAttribute("hidden", true);
    }
    else
    {
        js.src = "../../../js/thunderstorms_theme.js";
    }
    head.appendChild(js);
</script>