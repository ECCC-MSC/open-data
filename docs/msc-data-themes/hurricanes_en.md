[En français](hurricanes_fr.md)

![ECCC logo](../img_eccc-logo.png)

[TOC](../readme_en.md) > [Data themes](readme_en.md) > Hurricanes

# Hurricanes&emsp;<i class="wi wi-hurricane" style="font-size: 45px; color: #4e64a6;"></i>

This page presents a list of relevant Meteorological Service of Canada datasets under the hurricane theme, in order to guide users to the appropriate datasets. This list is not exhaustive, but provides an overview of the layers that can be used under this theme. The main data layers are the hurricane tracks and hurricane reaction zone issued by the Canadian Hurricane Centre, as part of their regular hurricane season forecasts. However, a number of other relevant layers can also provide complementary information on the subject, such as wind speed, rainfall amounts or coastal waves, to give just a few examples.
</br>

Example of an interactive map featuring the Web Map Service (WMS) layers `Hurricane Response Zone`, `Weather Alerts` and `HRDPS-WeonG`(Gust) (active on the map), plus a number of optional layers that can be added by checking the boxes in the list in the map. The layers are served by MSC GeoMet :

<div id="map" style="height: 500px; position: relative">
  <div id="legend-popup">
    <div id="legend-popup-content">
      <img id="legend-img" src="" />
    </div>
  </div>

  <div id="switch-content" style="position: absolute; z-index: 1; bottom: 40px; left: 8px;">
    <div id="switch-case">
        <label>
          <input type="checkbox" id="layer5" checked>
          <span onmouseover="updateLegend('https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=HURRICANE_RESPONSE_ZONE&format=image/png')">Hurricane zone</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer6" checked>
          <span onmouseover="updateLegend('https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=ALERTS&format=image/png')">Weather Alerts</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer2" checked>
          <span onmouseover="updateLegend('https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=HRDPS-WEonG_2.5km_WindGust&format=image/png')">Gust</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer1">
          <span onmouseover="updateLegend('https://geo.wxod-dev.cmc.ec.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=HRDPS-WEonG_2.5km_TotalPrecipIntensityIndex&format=image/png&STYLE=TotalPrecipIntensityIndex_Dis')">Total precipitation</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer3">
          <span onmouseover="updateLegend('https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=HRDPS-WEonG_2.5km_Thunderstorm-Prob&format=image/png')">Thunderstorm</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer4">
          <span onmouseover="updateLegend('https://geo.weather.gc.ca/geomet?lang=fr&version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=CURRENT_CONDITIONS&format=image/png&STYLE=default')">Current Conditions</span>
        </label></br>
    </div>
  </div>
</div>
</br>

## Datasets

It should be noted that the various layers presented in the list are available at different resolutions and timeframes.
The layers in the following list can also be viewed on MSC AniMet with a single [permalink](https://eccc-msc.github.io/msc-animet/?layers=Radar-Coverage_SfcPrecipType%3B0.75%3B1%3B1%3B0,RDPS.CONV_SFC-CAPE%3B0.75%3B0%3B1%3B0,HURRICANE_CENTRE%3B0.75%3B0%3B1%3B0,HURRICANE_RAD%3B0.75%3B0%3B1%3B0,HURRICANE_RESPONSE_ZONE%3B0.75%3B0%3B1%3B0,RDPA-Prelim_10km_Precip-Accum24h%3B0.75%3B0%3B1%3B0,RDPS.CONV_TOTALX.PT3H%3B0.75%3B0%3B1%3B0,RDWPS_2.5km_WindWavesSignificantHeight%3B0.75%3B0%3B1%3B0,RADAR_1KM_RRAI%3B0.75%3B0%3B1%3B0,Radar_1km_RainPrecipRate-Extrapolation%3B0.75%3B0%3B1%3B0,HRDPS.CONTINENTAL_P0%3B0.75%3B0%3B1%3B0,HRDPS.CONTINENTAL_PN%3B0.75%3B0%3B1%3B0,HRDPS.CONTINENTAL_RN%3B0.75%3B0%3B1%3B0,HRDPS.CONTINENTAL_WGX%3B0.75%3B0%3B1%3B0,HRDPS-WEonG_2.5km_Thunderstorm-Prob%3B0.75%3B0%3B1%3B0,HRDPS-WEonG_2.5km_TotalPrecipIntensityIndex%3B0.75%3B0%3B1%3B0,HRDPS-WEonG_2.5km_WindGust%3B0.75%3B0%3B1%3B0,HRDPS-WEonG_2.5km_WindSpeed%3B0.75%3B0%3B1%3B0,ALERTS%3B0.75%3B0%3B1%3B0,CURRENT_CONDITIONS%3B0.75%3B0%3B1%3B0,Lightning_2.5km_Density%3B0.75%3B0%3B1%3B0,METNOTES%3B0.75%3B0%3B1%3B0&extent=-22088883,-731482,1411752,11074002) for all variables.

##### &emsp;<span class="badge badge-info">Hurricanes</span>
###### &emsp;[Hurricanes data documentation page](../msc-data/hurricanes/readme_hurricanes_en.md)
* Hurricane Response Zone
* Hurricane Wind Forecast Wind Radii
* Hurricane Forecast Location</br>

##### &emsp;<span class="badge badge-info">HRDPS - Weather Elements on Grid</span>
###### &emsp;[HRDPS data documentation](../msc-data/nwp_hrdps/readme_hrdps_en.md)
* Wind speed
* Gust
* Total precipitation intensity index
* Probability of thunderstorm occurence</br>

##### &emsp;<span class="badge badge-info">HRDPS at surface/near-surface fields</span>
###### &emsp;[HRDPS data documentation](../msc-data/nwp_hrdps/readme_hrdps_en.md)
* Wind gust maximum
* Rain accumulation
* Sea level pressure (contour)
* Surface pressure</br>

##### &emsp;<span class="badge badge-info">RESPS</span>
###### &emsp;[RESPS data documentation](../msc-data/nwp_resps/readme_resps_en.md)
* Storm surge - Atlantic North West (1)
* Storm surge - Atlantic North West (2)
* Storm surge - Atlantic North West (3)
* Storm surge - Atlantic North West (4)
* Storm surge - Atlantic North West (5)
* Storm surge - Atlantic North West (6)</br>


##### &emsp;<span class="badge badge-info">Radar</span>
###### &emsp;[Radar data documentation](../msc-data/obs_radar/readme_radar_en.md)
* Radar extrapolation precipitation rate for rain (experimental)
* Radar precipitation rate for rain
* Dynamic radar coverage for surface precipitation type (experimental)</br>

##### &emsp;<span class="badge badge-info">RDPS - convective fields</span>
###### &emsp;[RDPS data documentation](../msc-data/nwp_rdps/readme_rdps_en.md)
* CAPE for a surface based parcel
* Thunderstorm potential index total</br>

##### &emsp;<span class="badge badge-info">Autres</span>

* [Weather Alerts (experimental)](../msc-data/alerts/readme_alerts_en.md)
* [Lightning Flash Density over Canada (2.5 km)](../msc-data/lightning/readme_lightning_en.md)
* [MetNotes](../msc-data/metnotes/readme_metnotes_en.md)
* [Current Conditions](../msc-data/citypage-weather/readme_citypageweather_en.md)
* [RDWPS - Significant height of wind waves](../msc-data/nwp_rdwps/readme_rdwps_en.md)
* [GDSPS - Storm surge](../msc-data/nwp_gdsps/readme_gdsps_en.md)
* [RDPA - Quantity of precipitation over a 24h hour interval (preliminary)](../msc-data/nwp_rdpa/readme_rdpa_en.md)


<style>
  #legend-img {
    margin: 0px;
  }
  #legend-popup {
    position: absolute;
    top: 8px;
    right: 40px;
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
        js.src = "../../js/hurricane_theme_ie.js";
        document.getElementById("controller").setAttribute("hidden", true);
    }
    else
    {
        js.src = "../../js/hurricane_theme.js";
    }
    head.appendChild(js);
</script>