[In English](snowstorms_en.md)

![ECCC logo](../img_eccc-logo.png)

[TOC](../readme_fr.md) > [Thèmes des données](readme_fr.md) > Tempêtes de neige

# Tempêtes de neige&emsp;<i class="wi wi-snow-wind" style="font-size: 45px; color: #4e64a6;"></i>

Cette page présente une liste de jeux de données pertinents du Service météorologique du Canada sous le thème des tempêtes de neige, afin de guider les utilisateurs vers les jeux de données appropriés. Cette liste n'est pas exhaustive, mais donne un aperçu des couches qui peuvent être utilisées sous ce thème. Les principales couches de données pour ce thème sont les variables de quantité de neige. Cependant, un certain nombre d'autres couches pertinentes peuvent également fournir des informations supplémentaires sur le sujet, telles que les facteurs de vent, les types de précipitations hivernales ou la température, pour ne citer que ces quelques exemples.

Exemple de carte interactive comportant les couches du Service de cartographie Web (WMS) des `Alertes météo`, de `RDPS.ETA` (Neige accumulée) et de `Conditions actuelles` (actives sur la carte), ainsi que d'autres couches optionnelles qui peuvent être ajoutées en cochant les cases de la liste dans la carte. Les couches sont desservies par GeoMet du SMC :

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
          <span onmouseover="updateLegend('https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=ALERTS&format=image/png&STYLE=ALERTES')">Alertes météo</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer1" checked>
          <span onmouseover="updateLegend('https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=RDPS.ETA_SN&format=image/png&STYLE=PRECIPSNOW')">Neige accumulée</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer2" checked>
          <span onmouseover="updateLegend('https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=CURRENT_CONDITIONS&format=image/png&STYLE=default')">Conditions actuelles</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer5">
          <span onmouseover="updateLegend('https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=RDPS-WEonG_10km_BlowingSnow-Prob&format=image/png&STYLE=BlowingSnow-Prob')">Probabilité de poudredrie</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer3">
          <span onmouseover="updateLegend('https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=RDPS-WEonG_10km_AirTemp&format=image/png&STYLE=TEMPERATURE-LINEAR')">Température</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer6">
          <span onmouseover="updateLegend('https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=RADAR_1KM_RSNO&format=image/png&STYLE=Radar-Snow_Dis-14colors_Fr')">Radar pour la neige</span>
        </label></br>
    </div>
  </div>
</div>
</br>

## Jeux de données

Il est à noter que les différentes couches présentées dans la liste qui suit, sont disponibles à différentes résolutions et différentes échéances temporelles.
Les couches de la liste suivante peuvent être également visualisées sur AniMet du SMC avec un [permalien](https://eccc-msc.github.io/msc-animet/?layers=CURRENT_CONDITIONS;0.75;0;1;0,Radar_1km_SnowPrecipRate-Extrapolation;0.75;1;1;0,RDPS.ETA_TT;0.75;0;1;0,RDPS.ETA_SN;0.75;0;1;0,RDPS.ETA_WD;0.75;0;1;0,RDPS.ETA_WGE;0.75;0;1;0,ALERTS;0.75;0;1;0,RDPS.ETA_WSPD;0.75;0;1;WindSpeed_30-210Knots_Dis,RDPS-WEonG_10km_AirTemp;0.75;0;1;0,RDPS-WEonG_10km_BlowingSnowPresence;0.75;0;1;0,RDPS-WEonG_10km_BlowingSnow-Prob;0.75;0;1;0,RDPS-WEonG_10km_Snow-Prob;0.75;0;1;0,RDPS-WEonG_10km_SnowSqualls-Prob;0.75;0;1;0,RDPS-WEonG_10km_SnowHeight;0.75;0;1;0,RADAR_1KM_RSNO;0.75;0;1;0,REPS.DIAG.12_SNMM.ERGE30;0.75;0;1;0,REPS.DIAG.12_SNMM.ERGE15;0.75;0;1;0,REPS.DIAG.12_PRMM.ERGE15;0.75;0;1;0,REPS.DIAG.12_PRMM.ERGE30;0.75;0;1;0,REPS.DIAG.3_PRMM.ERGE15;0.75;0;1;0,REPS.DIAG.3_PRMM.ERMEAN;0.75;0;1;0,REPS.DIAG.24_SNMM.ERGE20;0.75;0;1;0,REPS.DIAG.24_SNMM.ERGE25;0.75;0;1;0,REPS.DIAG.24_PEMM.ERGE20;0.75;0;1;0,GEPS.DIAG.12_PEMM.ERGE30;0.75;0;1;0,GEPS.DIAG.24_SNMM.ERGE20;0.75;0;1;0,GEPS.DIAG.24_SNMM.ERGE25;0.75;0;1;0,GEPS.DIAG.24_PEMM.ERGE20;0.75;0;1;0,GEPS.DIAG.24_PEMM.ERGE30;0.75;0;1;0,REPS.DIAG.12_PEMM.ERGE30;0.75;0;1;0,REPS.DIAG.12_PEMM.ERGE15;0.75;0;1;0,REPS.DIAG.12_PEMM.ERGE5;0.75;0;1;0,GEPS.DIAG.12_PEMM.ERGE15;0.75;0;1;0,GEPS.DIAG.12_PEMM.ERGE5;0.75;0;1;0&extent=-17412813,2741278,-274277,11223514) unique pour l'ensemble des variables.

##### &emsp;<span class="badge badge-info">SHRPD Continental - Éléments du temps sur grille</span>
###### &emsp;[Documentation des données SHRPD](../msc-data/nwp_hrdps/readme_hrdps_fr.md)
* Hauteur du niveau de la neige
* Probabilité de bourrasque de neige
* Probabilité de neige
* Probabilité de poudrerie
* Présence de poudrerie
* Température</br>

##### &emsp;<span class="badge badge-info">SRPD - champs diagnostiques</span>
###### &emsp;[Documentation des données SRPD](../msc-data/nwp_rdps/readme_rdps_fr.md)
* Vitesse du vent
* Estimation des rafales de vent
* Direction du vent
* Neige accumulée
* Température de l'air</br>

##### &emsp;<span class="badge badge-info">SGPE - champs diagnostiques</span>
###### &emsp;[Documentation des données SGPE](../msc-data/nwp_geps/readme_geps_fr.md)
* Probabilité de quantité de granules de glace supérieure à 5 mm (12 heures)
* Probabilité de quantité de granules de glace supérieure à 15 mm (12 heures)
* Probabilité de quantité de granules de glace supérieure à 30 mm (12 heures)
* Probabilité de quantité de granules de glace supérieure à 20 mm (24 heures)
* Probabilité de quantité de granules de glace supérieure à 30 mm (24 heures)
* Probabilité de quantité de neige supérieure à 20 mm (24 heures)
* Probabilité de quantité de neige supérieure à 25 mm (24 heures)</br>

##### &emsp;<span class="badge badge-info">SRPE - champs diagnostiques</span>
###### &emsp;[Documentation des données SRPE](../msc-data/nwp_reps/readme_reps_fr.md)
* Quantité de précipitations (moyenne)
* Probabilité de quantité de précipitations supérieure à 15 mm (3 heures)
* Probabilité de quantité de précipitations supérieure à 15 mm (12 heures)
* Probabilité de quantité de précipitations supérieure à 30 mm (12 heures)
* Probabilité de quantité de neige supérieure à 15 mm (12 heures)
* Probabilité de quantité de neige supérieure à 30 mm (12 heures)
* Probabilité de quantité de neige supérieure à 20 mm (24 heures)
* Probabilité de quantité de neige supérieure à 25 mm (24 heures)
* Probabilité de quantité de granules de glace supérieure à 5 mm (12 heures)
* Probabilité de quantité de granules de glace supérieure à 15 mm (12 heures)
* Probabilité de quantité de granules de glace supérieure à 30 mm (12 heures)
* Probabilité de quantité de granules de glace supérieure à 20 mm (24 heures)
* Probabilité de quantité de granules de glace supérieure à 35 mm (24 heures)</br>

##### &emsp;<span class="badge badge-info">Radar</span>
###### &emsp;[Documentation des données radar](http://geomet-dev-22.cmc.ec.gc.ca:8082/msc-data/obs_radar/readme_radar_fr/)
* Taux de précipitation radar pour la neige
* Taux de précipitation radar extrapolé pour la neige</br>

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
        js.src = "../../js/snowstorms_theme_ie.js";
        document.getElementById("controller").setAttribute("hidden", true);
    }
    else
    {
        js.src = "../../js/snowstorms_theme.js";
    }
    head.appendChild(js);
</script>