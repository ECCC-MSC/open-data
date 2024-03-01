[En français](transportation_logistics_fr.md)

![ECCC logo](../img_eccc-logo.png)

[TOC](../readme_en.md) > [Data themes](readme_en.md) > Ground transportation logistics

# Ground transportation logistics&emsp;<i class="wi wi-train" style="font-size: 45px; color: #4e64a6;"></i>


This page presents a list of relevant Meteorological Service of Canada datasets under the Land Transport Logistics theme, in order to guide users to the appropriate datasets. This list is not exhaustive, but provides an overview of the layers that can be used under this theme. The main data layers for this theme are the precipitation rate variables. However, a number of other relevant layers can also provide additional information on the subject, such as wind gusts, visibility or the possibility of blowing snow on routes, to name but a few examples.

Example of an interactive map featuring the Web Map Service (WMS) layers `Weather Alert`, `HRDPS.CONTINENTAL` (Maximum wind gusts) and `GDPS-WEonG` (Visibility: liquid fog) (active on the map), plus other optional layers that can be added by checking the boxes in the list in the map. The layers are served by MSC GeoMet :

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
          <span onmouseover="updateLegend('https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=HRDPS.CONTINENTAL_WGX&format=image/png')">Maximum wind gusts</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer2" checked>
          <span onmouseover="updateLegend('https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=HRDPS-WEonG_2.5km_LiquidFogVisibility&format=image/png')">Visibility: liquid fog</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer5">
          <span onmouseover="updateLegend('https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=HRDPS-WEonG_2.5km_BlowingSnowPresence&format=image/png')">Presence of blowing snow</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer3">
          <span onmouseover="updateLegend('https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=RDPS-WEonG_10km_FreezingPrecip-Prob&format=image/png')">Probability of freezing rain</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer6">
          <span onmouseover="updateLegend('https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=RADAR_1KM_RSNO&format=image/png')">Snow radar</span>
        </label></br>
    </div>
  </div>
</div>
</br>



## Datasets

It should be noted that the various layers presented in the list are available at different resolutions and timeframes.
The layers in the following list can also be viewed on MSC AniMet with a single [permalink](https://eccc-msc.github.io/msc-animet/?layers=ALERTS;0.75;0;1;0,Radar_1km_SfcPrecipType;0.75;0;1;0,Radar_1km_RainPrecipRate-Extrapolation;0.75;0;1;0,Radar_1km_SnowPrecipRate-Extrapolation;0.75;0;1;0,HRDPS-WEonG_2.5km_WindSpeed;0.75;0;1;0,HRDPS-WEonG_2.5km_WindGust;0.75;0;1;0,HRDPS-WEonG_2.5km_FreezingPrecip-Prob;0.75;0;1;0,RDPS-WEonG_10km_FreezingPrecip-Prob;0.75;0;1;0,GDPS-WEonG_15km_BlowingSnow-Prob;0.75;0;1;0,HRDPS-WEonG_2.5km_BlowingSnowPresence;0.75;0;1;0,RDPS-WEonG_10km_BlowingSnowPresence;0.75;0;1;0,RADAR_1KM_RSNO;0.75;0;1;0,GDPS-WEonG_15km_FreezingDrizzle-Prob;0.75;0;1;0,GDPS-WEonG_15km_IcePellets-Prob;0.75;0;1;0,GDPS-WEonG_15km_WindGust;0.75;0;1;0,HRDPS.CONTINENTAL_WGX;0.75;0;1;0,CURRENT_CONDITIONS;0.75;0;1;0,GOES-East_1km_DayVis;0.75;0;0;0,GOES-West_1km_DayVis;0.75;0;0;0,GDPS-WEonG_15km_IceFogVisibility;0.75;0;1;0,GDPS-WEonG_15km_LiquidFogVisibility;0.75;0;1;0,HRDPS-WEonG_2.5km_IceFogVisibility;0.75;0;1;0,HRDPS-WEonG_2.5km_LiquidFogVisibility;0.75;0;1;0,HRDPS.CONTINENTAL_FR;0.75;0;1;0,HRDPS.CONTINENTAL_NO;0.75;0;1;0,HRDPS.CONTINENTAL_WSPD;0.75;0;1;0&extent=-18847435,1845742,1190074,11911533) for all variables.

##### &emsp;<span class="badge badge-info">HRDPS at surface/near-surface fields</span>
###### &emsp;[HRDPS data documentation](../msc-data/nwp_hrdps/readme_hrdps_en.md)
* Wind gust maximum
* Wind speed at 10m above surface
* Water runoff accumulation
* Freezing rain accumulation</br>
       &emsp;&emsp;[HRDPS data documentation](../msc-data/nwp_hrdps/readme_hrdps_en.md)</br>

##### &emsp;<span class="badge badge-info">HRDPS - Weather Elements on Grid</span>
###### &emsp;[HRDPS data documentation](../msc-data/nwp_hrdps/readme_hrdps_en.md)
* Visibility through liquid fog
* Visibility through ice fog
* Presence of blowing snow
* Probability of freezing precipitation
* Gust
* Wind speed</br>

##### &emsp;<span class="badge badge-info">GDPS - Weather Elements on Grid</span>
###### &emsp;[GDPS data documentation](../msc-data/nwp_gdps/readme_gdps_en.md)
* Visibility through liquid fog
* Visibility through ice fog
* Gust
* Probability of ice pellets
* Probability of freezing drizzle
* Probability of blowing snow</br>


##### &emsp;<span class="badge badge-info">RDPS - Weather Elements on Grid</span>
###### &emsp;[RPDS data documentation](../msc-data/nwp_rdps/readme_rdps_en.md)
* Presence of blowing snow
* Probability of freezing precipitation</br>

##### &emsp;<span class="badge badge-info">Radar</span>
###### &emsp;[Radar data documentation](../msc-data/obs_radar/readme_radar_en.md)
* Radar surface precipitation type (experimental)
* Radar extrapolation precipitation rate for rain (experimental)
* Radar extrapolation precipitation rate for snow (experimental)
* Radar precipitation rate for snow</br>

##### &emsp;<span class="badge badge-info">GOES Satellite</span>
###### &emsp;[Satellite data documentation](../msc-data/obs_satellite/readme_satellite_en.md)
* Day visibility / Day Cloud Convection (West)
* Day visibility / Day Cloud Convection (East)</br>

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
        js.src = "../../../js/transportation_logistics_theme_ie.js";
        document.getElementById("controller").setAttribute("hidden", true);
    }
    else
    {
        js.src = "../../../js/transportation_logistics_theme.js";
    }
    head.appendChild(js);
</script>