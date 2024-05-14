[In English](wildfires_en.md)

![ECCC logo](../img_eccc-logo.png)

[TOC](../readme_fr.md) > [Thèmes des données](readme_fr.md) > Incendies de forêt

# Incendies de forêt&emsp;<i class="wi wi-fire" style="font-size: 45px; color: #4e64a6;"></i>

Cette page présente une liste de jeux de données pertinents du Service météorologique du Canada sous le thème des incendies de forêt, afin de guider les utilisateurs vers les jeux de données appropriés. Cette liste n'est pas exhaustive, mais donne un aperçu des couches qui peuvent être utilisées sous ce thème. Les principales couches de données pour ce thème sont les variables de qualité de l'air et les taux de précipitations. Cependant, un certain nombre d'autres couches pertinentes peuvent également fournir des informations supplémentaires sur le sujet, telles que les points chauds, la vitesse des vents ou la direction des vents, pour ne citer que ces quelques exemples.

Exemple de carte interactive comportant les couches du Service de cartographie Web (WMS) des `Points chauds`, de `HRDPS-WEonG` (Rafale de vents) et de `Concentration de NO2` (actives sur la carte), ainsi que d'autres couches optionnelles qui peuvent être ajoutées en cochant les cases de la liste dans la carte. Les couches sont desservies par GeoMet du SMC :

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
          <span onmouseover="updateLegend('https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=FIREWORK.HOTSPOTS&format=image/png')">Points chauds</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer1" checked>
          <span onmouseover="updateLegend('https://geo.wxod-dev.cmc.ec.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=HRDPS-WEonG_2.5km_WindGust&format=image/png&STYLE=GUST_INTERV_MS2KTS')">Rafale de vents</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer2" checked>
          <span onmouseover="updateLegend('https://geo.wxod-dev.cmc.ec.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=RAQDPS.SFC_NO2&format=image/png&STYLE=SFC-NO2')">Concentration: NO2</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer5">
          <span onmouseover="updateLegend('https://geo.wxod-dev.cmc.ec.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=RAQDPS.SFC_PM2.5&format=image/png&STYLE=RAQDPS-SFC-PM_UGM3_BCAQHI')">Concentration : PM2.5</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer3">
          <span onmouseover="updateLegend('https://geo.wxod-dev.cmc.ec.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=RADAR_1KM_RRAI&format=image/png&STYLE=Radar-Rain_Dis-14colors_Fr')">Taux de précipitation radar</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer6">
          <span onmouseover="updateLegend('https://geo.wxod-dev.cmc.ec.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=RAQDPS.SFC_O3&format=image/png&STYLE=SFC-O3')">Concentration: O3</span>
        </label></br>
    </div>
  </div>
</div>
</br>


## Jeux de données

Il est à noter que les différentes couches présentées dans la liste qui suit, sont disponibles à différentes résolutions et différentes échéances temporelles.
Les couches de la liste suivante peuvent être également visualisées sur AniMet du SMC avec un [permalien](https://eccc-msc.github.io/msc-animet/?layers=ALERTS;0.75;0;1;0,CURRENT_CONDITIONS;0.75;0;1;0,Lightning_2.5km_Density;0.75;1;1;0,FIREWORK.HOTSPOTS;0.75;0;1;0,RAQDPS.SFC_NO2;0.75;0;1;0,RAQDPS.SFC_O3;0.75;0;1;0,RAQDPS.SFC_PM2.5;0.75;0;1;0,RADAR_1KM_RRAI;0.75;0;1;0,Radar_1km_RainPrecipRate-Extrapolation;0.75;0;1;0,Radar_1km_dBZ-Extrapolation;0.75;0;1;0,HRDPS-WEonG_2.5km_AirTemp;0.75;0;1;0,HRDPS-WEonG_2.5km_Precip-Prob;0.75;0;1;0,HRDPS-WEonG_2.5km_Thunderstorm-Prob;0.75;0;1;0,HRDPS-WEonG_2.5km_WindDir;0.75;0;1;0,HRDPS-WEonG_2.5km_WindGust;0.75;0;1;0,HRDPS-WEonG_2.5km_WindSpeed;0.75;0;1;0,HRDPS.CONTINENTAL_PC;0.75;0;1;0,GEPS.DIAG.120_PRMM.ERGE1;0.75;0;1;0,GEPS.DIAG.120_PRMM.ERGE10;0.75;0;1;0,GEPS.DIAG.120_PRMM.ERGE5;0.75;0;1;0&extent=-23473981,634482,2187623,13334971) unique pour l'ensemble des variables.

##### &emsp;<span class="badge badge-info">SHRPD à la surface ou à proximité de la surface</span>
###### &emsp;[Documentation des données SHRPD](../msc-data/nwp_hrdps/readme_hrdps_fr.md)
* Précipitations convectives</br>

##### &emsp;<span class="badge badge-info">SHRPD Continental - Éléments du temps sur grille</span>
###### &emsp;[Documentation des données SHRPD](../msc-data/nwp_hrdps/readme_hrdps_fr.md)
* Probabilité d'occurence d'orage
* Vitesse du vent
* Direction du vent
* Rafale de vents
* Température
* Probabilité de précipitation</br>


##### &emsp;<span class="badge badge-info">SPGE - champs diagnostiques</span>
###### &emsp;[Documentation des données SGPE](../msc-data/nwp_geps/readme_geps_fr.md)
* Probabilité de quantité de précipitations supérieures à 1 mm (120 heures)
* Probabilité de quantité de précipitations supérieures à 5 mm (120 heures)
* Probabilité de quantité de précipitations supérieures à 10 mm (120 heures)</br>

##### &emsp;<span class="badge badge-info">Radar</span>
###### &emsp;[Documentation des données radar](http://geomet-dev-22.cmc.ec.gc.ca:8082/msc-data/obs_radar/readme_radar_fr/)
* Taux de précipitation radar pour la pluie
* Taux de précipitation radar extrapolé pour la pluie
* Taux de précipitation radar extrapolé</br>
       &emsp;&emsp;[Documentation des données radar](../msc-data/nwp_raqdps-fw/readme_raqdps-fw_fr.md)</br>

##### &emsp;<span class="badge badge-info">Qualité de l'air</span>
###### &emsp;[Documentation des données SRPDQA](../msc-data/nwp_raqdps/readme_raqdps_fr.md)
* Points chauds considérés par SRPDQA-FireWork</br>
* Concentration : surface NO2
* Concentration : surface O3
* Concentration : surface PM2.5</br>

##### &emsp;<span class="badge badge-info">Autres</span>

* [Alertes météo (experimental)](../msc-data/alerts/readme_alerts_fr.md)
* [Conditions actuelles](../msc-data/citypage-weather/readme_citypageweather_fr.md)
* [Densité de foudre sur le Canada](../msc-data/lightning/readme_lightning_fr.md)


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
 }label {
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
        js.src = "../../../js/wildfires_theme_ie.js";
        document.getElementById("controller").setAttribute("hidden", true);
    }
    else
    {
        js.src = "../../../js/wildfires_theme.js";
    }
    head.appendChild(js);
</script>