[En français](floods_fr.md)

![ECCC logo](../img_eccc-logo.png)

[TOC](../readme_en.md) > [Data themes](readme_en.md) > Floods

# Floods&emsp;<i class="wi wi-flood" style="font-size: 45px; color: #4e64a6;"></i>

This page presents a list of relevant Meteorological Service of Canada datasets under the theme of flooding, in order to guide users to the appropriate datasets. This list is not exhaustive, but provides an overview of the layers that can be used under this theme. The main data layers for this theme are precipitation quantities. However, a number of other relevant layers can also provide additional information on the subject, such as runoff or precipitable water contained in clouds, to name but two examples.

Example of an interactive map featuring the Web Map Service (WMS) layers `HRDPA.24F_PR` (Quantity of precipitation), `Weather Alerts` and `Current Conditions` (active on the map), plus other optional layers that can be added by checking the boxes in the list in the map. The layers are served by MSC GeoMet :

<div id="map" style="height: 500px; position: relative">
  <div id="legend-popup">
    <div id="legend-popup-content">
      <img id="legend-img" style="display: flex; max-height: 400px;" src="" />
    </div>
  </div>

  <div id="switch-content" style="position: absolute; z-index: 1; bottom: 40px; left: 8px;">
    <div id="switch-case">
        <label>
          <input type="checkbox" id="layer1" checked>
          <span onmouseover="updateLegend('https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=HRDPA.24F_PR&format=image/png&STYLE=CAPA24-LINEAR')">Quantity of precipitation</span>
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
          <input type="checkbox" id="layer6">
          <span onmouseover="updateLegend('https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=HRDPS.CONTINENTAL_PC&format=image/png&STYLE=CAPA24-LINEAR')">Convective precipitation</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer3">
          <span onmouseover="updateLegend('https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=RADAR_1KM_RRAI&format=image/png&STYLE=Radar-Rain_14colors')">Radar precipitation</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer5">
          <span onmouseover="updateLegend('https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=HRDPS.CONTINENTAL_IH&format=image/png&STYLE=CAPA24-LINEAR')">Cloud water</span>
        </label></br>
    </div>
  </div>
</div>
</br>

## Datasets

It should be noted that the various layers presented in the list are available at different resolutions and timeframes.
The layers in the following list can also be viewed on MSC AniMet with a single [permalink](https://eccc-msc.github.io/msc-animet/?layers=HRDPA.6F_PR;0.75;0;1;0,HRDPA.24F_PR;0.75;1;1;0,ALERTS;0.75;0;1;0,CURRENT_CONDITIONS;0.75;0;1;0,RADAR_1KM_RRAI;0.75;0;1;0,Radar_1km_RainPrecipRate-Extrapolation;0.75;0;1;0,HRDPS.CONTINENTAL_IH;0.75;0;1;0,HRDPS.CONTINENTAL_PC;0.75;0;1;0,HRDPS.CONTINENTAL_RN;0.75;0;1;0,GEPS.DIAG.96_PRMM.ERGE100;0.75;0;1;0,GEPS.DIAG.96_PRMM.ERGE150;0.75;0;1;0,GEPS.DIAG.96_PRMM.ERGE200;0.75;0;1;0,GEPS.DIAG.120_PRMM.ERGE100;0.75;0;1;0,GEPS.DIAG.120_PRMM.ERGE150;0.75;0;1;0,GEPS.DIAG.120_PRMM.ERGE200;0.75;0;1;0,GDPS.ETA_NO.3h;0.75;0;1;0,HRDPS.CONTINENTAL_NO;0.75;0;1;0,RDPS.ETA_NO;0.75;0;1;0&extent=-14583377,2738020,-2263679,8926788) for all variables.

##### &emsp;<span class="badge badge-info">HRDPS at surface/near-surface fields</span>
###### &emsp;[HRDPS data documentation](../msc-data/nwp_hrdps/readme_hrdps_en.md)
* Water runoff accumulation
* Rain accumulation
* Convective precipitation
* Cloud water</br>

##### &emsp;<span class="badge badge-info">HRDPA</span>
###### &emsp;[HRDPA data documentation](../msc-data/nwp_hrdpa/readme_hrdpa_en.md)
* Quantity of precipitation (6 hours)
* Quantity of precipitation (24 hours)</br>

##### &emsp;<span class="badge badge-info">Radar</span>
###### &emsp;[Radar data documentation](../msc-data/obs_radar/readme_radar_en.md)
* Radar precipitation rate for rain
* Radar extrapolation precipitation rate for rain (experimental)</br>

##### &emsp;<span class="badge badge-info">GEPS - diagnostic fields</span>
###### &emsp;[GEPS data documentation](../msc-data/nwp_geps/readme_geps_en.md)
* Probability of quantity of precipitation over 100 mm (96 hours)
* Probability of quantity of precipitation over 150 mm (96 hours)
* Probability of quantity of precipitation over 200 mm (96 hours)
* Probability of quantity of precipitation over 100 mm (120 hours)
* Probability of quantity of precipitation over 150 mm (120 hours)
* Probability of quantity of precipitation over 200 mm (120 hours)</br>

##### &emsp;<span class="badge badge-info">Others</span>

* [Weather Alerts](../msc-data/alerts/readme_alerts_en.md)
* [Current Conditions](../msc-data/citypage-weather/readme_citypageweather_en.md)
* [Water runoff accumulation (RDPS)](../msc-data/nwp_rdps/readme_rdps_en.md)
* [Coastal flooding risk index](../msc-data/coastal-flooding/readme_coastal-flooding_en.md)


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
        js.src = "../../js/floods_theme_ie.js";
        document.getElementById("controller").setAttribute("hidden", true);
    }
    else
    {
        js.src = "../../js/floods_theme.js";
    }
    head.appendChild(js);
</script>