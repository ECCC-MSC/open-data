[In English](drought_en.md)

![ECCC logo](../img_eccc-logo.png)

[TOC](../readme_fr.md) > [Thèmes des données](readme_fr.md)> Vagues de chaleur

# Vagues de chaleur&emsp;<i class="wi wi-hot" style="font-size: 45px; color: #4e64a6;"></i>

Cette page présente une liste de jeux de données pertinents du Service météorologique du Canada sous le thème des vagues de chaleur, afin de guider les utilisateurs vers les jeux de données appropriés. Cette liste n'est pas exhaustive, mais donne un aperçu des couches qui peuvent être utilisées sous ce thème. Les principales couches de données pour ce thème sont les quantités de précipitations et de température. Cependant, un certain nombre d'autres couches pertinentes peuvent également fournir des informations supplémentaires sur le sujet, telles que le ruissellement ou l'eau précipitable contenue dans les nuages, pour ne citer que deux exemples.

Exemple de carte interactive comportant les couches du Service de cartographie Web (WMS) `HRDPS-WEonG` (Température), `Alertes météo` et `Conditions actuelles` (actives sur la carte), ainsi que d'autres couches optionnelles qui peuvent être ajoutées en cochant les cases de la liste dans la carte. Les couches sont desservies par GeoMet du SMC :

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
          <span onmouseover="updateLegend('https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=HRDPS-WEonG_2.5km_AirTemp&format=image/png')">Température</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer2" checked>
          <span onmouseover="updateLegend('https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=ALERTS&format=image/png&STYLE=ALERTES')">Alertes météo</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer4" checked>
          <span onmouseover="updateLegend('https://geo.weather.gc.ca/geomet?lang=fr&version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=CURRENT_CONDITIONS&format=image/png&STYLE=default')">Conditions actuelles</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer3">
          <span onmouseover="updateLegend('https://geo.wxod-dev.cmc.ec.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=HRDPS-WEonG_2.5km_Precip-Prob&format=image/png&STYLE=Precip-Prob')">Probabilité de précipitation</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer6">
          <span onmouseover="updateLegend('https://geo.wxod-dev.cmc.ec.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=REPS.DIAG.3_HMXX.ERMEAN&format=image/png&STYLE=REPS_TT')">Humidex de surface</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer5">
          <span onmouseover="updateLegend('https://geo.wxod-dev.cmc.ec.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=HRDPS.CONTINENTAL_UTCI&format=image/png&STYLE=UTCI-FR')">Indice Climatique Thermique Universel</span>
        </label></br>
    </div>
  </div>
</div>
</br>


## Jeux de données

Il est à noter que les différentes couches présentées dans la liste qui suit, sont disponibles à différentes résolutions et différentes échéances temporelles.
Les couches de la liste suivante peuvent être également visualisées sur AniMet du SMC avec un [permalien](https://eccc-msc.github.io/msc-animet/?layers=HRDPS-WEonG_2.5km_AirTemp;0.75;1;1;0,HRDPS-WEonG_2.5km_DewPointTemp;0.75;0;1;0,HRDPS-WEonG_2.5km_Precip-Prob;0.75;0;1;0,HRDPS-WEonG_2.5km_SkyState;0.75;0;1;0,HRDPS.CONTINENTAL_HU;0.75;0;1;0,HRDPS.CONTINENTAL_IH;0.75;0;1;0,HRDPS.CONTINENTAL_NT;0.75;0;1;0,REPS.DIAG.3_HMXX.ERMEAN;0.75;0;1;0,HRDPS.CONTINENTAL_I0;0.75;0;1;0,CURRENT_CONDITIONS;0.75;0;1;0,ALERTS;0.75;0;1;0,HRDPS.CONTINENTAL_UTCI;0.75;0;1;0,HRDPS-WEonG_2.5km_WindSpeed;0.75;0;1;0,REPS.DIAG.6_RNMM.ERMEAN;0.75;0;1;0&extent=-22417283,465184,1337032,12221714) unique pour l'ensemble des variables.

##### &emsp;<span class="badge badge-info">SHRPD à la surface ou à proximité de la surface</span>
###### &emsp;[Documentation des données SHRPD](../msc-data/nwp_hrdps/readme_hrdps_fr.md)
* Température de la surface et du sol (Superficielle)
* Couverture nuageuse
* Eau précipitable
* Humidité spécifique à la surface
* Indice Climatique Thermique Universel (ICTU)</br>
       &emsp;&emsp;[Documentation des données SHRPD](../msc-data/nwp_hrdps/readme_hrdps_fr.md)</br>

##### &emsp;<span class="badge badge-info">SHRPD Continental - Éléments du temps sur grille</span>
###### &emsp;[Documentation des données SHRPD](../msc-data/nwp_hrdps/readme_hrdps_fr.md)
* Vitesse du vent
* Etat du ciel jour/nuit (couverture et opacité nuageuse combinées)
* Probabilité de précipitation
* Température du point de rosée
* Température</br>

##### &emsp;<span class="badge badge-info">SRPE - champs diagnostiques</span>
###### &emsp;[Documentation des données SRPE](../msc-data/nwp_reps/readme_reps_fr.md)
* Humidex à 2 m au-dessus du sol (moyenne)
* Pluie (moyenne)</br>

##### &emsp;<span class="badge badge-info">Autres</span>

* [Alertes météo](../msc-data/alerts/readme_alerts_fr.md)
* [Conditions actuelles](../msc-data/citypage-weather/readme_citypageweather_fr.md)


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
        js.src = "../../js/drought_theme_ie.js";
        document.getElementById("controller").setAttribute("hidden", true);
    }
    else
    {
        js.src = "../../js/drought_theme.js";
    }
    head.appendChild(js);
</script>