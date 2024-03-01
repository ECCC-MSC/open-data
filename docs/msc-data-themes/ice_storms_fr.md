[In English](ice_storms_en.md)

![ECCC logo](../img_eccc-logo.png)

[TOC](../readme_fr.md) > [Thèmes des données](readme_fr.md) > Tempêtes de verglas

# Tempêtes de verglas&emsp;<i class="wi wi-rain-mix" style="font-size: 45px; color: #4e64a6;"></i>

Cette page présente une liste de jeux de données pertinents du Service météorologique du Canada sous le thème des tempêtes de verglas, afin de guider les utilisateurs vers les jeux de données appropriés. Cette liste n'est pas exhaustive, mais donne un aperçu des couches qui peuvent être utilisées sous ce thème. Les principales couches de données pour ce thème sont les variables de précipitations verglaçantes. Cependant, un certain nombre d'autres couches pertinentes peuvent également fournir des informations supplémentaires sur le sujet, telles que les facteurs de vent, les types de précipitations hivernales ou la température, pour ne citer que ces quelques exemples.

Exemple de carte interactive comportant les couches du Service de cartographie Web (WMS) des `Alertes météo`, de `HRDPS-WEonG` (Type dominant de précipitation) et de `HRDPS-WEonG` (Probabilité de pluie verglaçante) (actives sur la carte), ainsi que d'autres couches optionnelles qui peuvent être ajoutées en cochant les cases de la liste dans la carte. Les couches sont desservies par GeoMet du SMC :

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
          <span onmouseover="updateLegend('https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=ALERTS&format=image/png&STYLE=ALERTES')">Alertes météo</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer1" checked>
          <span onmouseover="updateLegend('https://geo.wxod-dev.cmc.ec.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=GDPS-WEonG_15km_DominantPrecipType&format=image/png&STYLE=DominantPrecipType_Dis_Fr')">Type dominant de précipitation</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer2" checked>
          <span onmouseover="updateLegend('https://geo.wxod-dev.cmc.ec.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=GDPS-WEonG_15km_FreezingRain-Prob&format=image/png&STYLE=FreezingRain-Prob')">Probabilité de pluie verglaçante</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer5">
          <span onmouseover="updateLegend('https://geo.wxod-dev.cmc.ec.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=REPS.DIAG.6_PRMM.ERMEAN&format=image/png&STYLE=REPS_PRMM-LINEAR')">Quantité de préciptations</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer3">
          <span onmouseover="updateLegend('https://geo.wxod-dev.cmc.ec.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=GDPS-WEonG_15km_WindGust&format=image/png&STYLE=GUST_INTERV_MS2KTS')">Rafales de vents</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer6">
          <span onmouseover="updateLegend('https://geo.wxod-dev.cmc.ec.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=Radar_1km_SfcPrecipType&format=image/png&STYLE=SfcPrecipType_Dis_Fr')">Radar - type de précipitation</span>
        </label></br>
    </div>
  </div>
</div>
</br>


## Jeux de données

Il est à noter que les différentes couches présentées dans la liste qui suit, sont disponibles à différentes résolutions et différentes échéances temporelles.
Les couches de la liste suivante peuvent être également visualisées sur AniMet du SMC avec un [permalien](https://eccc-msc.github.io/msc-animet/?layers=GEPS.DIAG.12_FRMM.ERGE5;0.75;1;1;0,GEPS.DIAG.12_FRMM.ERGE15;0.75;0;1;0,GEPS.DIAG.12_FRMM.ERGE30;0.75;0;1;0,GEPS.DIAG.12_FRMM.ERMEAN;0.75;0;1;0,GEPS.DIAG.12_PEMM.ERGE5;0.75;0;1;0,GEPS.DIAG.12_PEMM.ERGE15;0.75;0;1;0,GEPS.DIAG.12_PEMM.ERGE30;0.75;0;1;0,GEPS.DIAG.12_PEMM.ERMEAN;0.75;0;1;0,GEPS.DIAG.12_PRMM.ERGE5;0.75;0;1;0,GEPS.DIAG.12_PRMM.ERGE15;0.75;0;1;0,GEPS.DIAG.12_PRMM.ERGE30;0.75;0;1;0,REPS.DIAG.6_FRMM.ERGE5;0.75;0;1;0,REPS.DIAG.6_FRMM.ERGE15;0.75;0;1;0,REPS.DIAG.6_FRMM.ERGE30;0.75;0;1;0,REPS.DIAG.6_FRMM.ERMEAN;0.75;0;1;0,REPS.DIAG.6_PEMM.ERGE5;0.75;0;1;0,REPS.DIAG.6_PEMM.ERGE15;0.75;0;1;0,REPS.DIAG.6_PEMM.ERGE30;0.75;0;1;0,REPS.DIAG.6_PEMM.ERMEAN;0.75;0;1;0,REPS.DIAG.6_PRMM.ERGE5;0.75;0;1;0,REPS.DIAG.6_PRMM.ERGE15;0.75;0;1;0,REPS.DIAG.6_PRMM.ERGE30;0.75;0;1;0,REPS.DIAG.6_PRMM.ERMEAN;0.75;0;1;0,GDPS-WEonG_15km_WindSpeed;0.75;0;1;0,GDPS-WEonG_15km_WindGust;0.75;0;1;0,GDPS-WEonG_15km_WindDir;0.75;0;1;0,GDPS-WEonG_15km_Precip-Prob;0.75;0;1;0,GDPS-WEonG_15km_InstantPrecipType;0.75;0;1;0,GDPS-WEonG_15km_IcePellets-Prob;0.75;0;1;0,GDPS-WEonG_15km_FreezingRain-Prob;0.75;0;1;0,GDPS-WEonG_15km_FreezingPrecip-Prob;0.75;0;1;0,GDPS-WEonG_15km_DominantPrecipType;0.75;0;1;0,GDPS-WEonG_15km_DewPointTemp;0.75;0;1;0,GDPS-WEonG_15km_AirTemp;0.75;0;1;0,CURRENT_CONDITIONS;0.75;0;1;0,ALERTS;0.75;0;1;0,Radar_1km_SfcPrecipType;0.75;0;1;0,Radar-Coverage_SfcPrecipType;0.75;0;1;0,Radar_1km_dBZ-Extrapolation;0.75;0;1;0&extent=-17028947,1084196,-370327,93289111) unique pour l'ensemble des variables.

##### &emsp;<span class="badge badge-info">SHRPD Continental - Éléments du temps sur grille</span>
###### &emsp;[Documentation des données SHRPD](../msc-data/nwp_hrdps/readme_hrdps_fr.md)
* Température
* Température du point de rosée
* Type dominant de précipitation
* Probabilité de précipitation verglaçante
* Probabilité de pluie verglaçante
* Probabilité de grésil
* Type de précipitation instantanée
* Probabilité de précipitation
* Direction du vent
* Rafale de vents
* Vitesse du vent</br>

##### &emsp;<span class="badge badge-info">SGPE - champs diagnostiques</span>
###### &emsp;[Documentation des données SGPE](../msc-data/nwp_geps/readme_geps_fr.md)
* Probabilité de quantité de granules de glace supérieure à 5 mm (12 heures)
* Probabilité de quantité de granules de glace supérieure à 15 mm (12 heures)
* Probabilité de quantité de granules de glace supérieure à 30 mm (12 heures)
* Granules de glace (12 heures - moyenne)
* Probabilité de quantité de pluie verglaçante supérieure à 5 mm (12 heures)
* Probabilité de quantité de pluie verglaçante supérieure à 15 mm (12 heures)
* Probabilité de quantité de pluie verglaçante supérieure à 30 mm (12 heures)
* Pluie verglaçante (12 heures - moyenne)
* Probabilité de quantité de précipitations supérieures à 5 mm (12 heures)
* Probabilité de quantité de précipitations supérieures à 15 mm (12 heures)
* Probabilité de quantité de précipitations supérieures à 30 mm (12 heures)</br>

##### &emsp;<span class="badge badge-info">SRPE - champs diagnostiques</span>
###### &emsp;[Documentation des données SRPE](../msc-data/nwp_reps/readme_reps_fr.md)
* Probabilité de quantité de granules de glace supérieure à 5 mm (6 heures)
* Probabilité de quantité de granules de glace supérieure à 15 mm (6 heures)
* Probabilité de quantité de granules de glace supérieure à 30 mm (6 heures)
* Granules de glace (6 heures - moyenne)
* Probabilité de quantité de pluie verglaçante supérieure à 5 mm (6 heures)
* Probabilité de quantité de pluie verglaçante supérieure à 15 mm (6 heures)
* Probabilité de quantité de pluie verglaçante supérieure à 30 mm (6 heures)
* Pluie verglaçante (6 heures - moyenne)
* Probabilité de quantité de précipitations supérieures à 5 mm (6 heures)
* Probabilité de quantité de précipitations supérieures à 15 mm (6 heures)
* Probabilité de quantité de précipitations supérieures à 30 mm (6 heures)
* Quantité de précipitations (6 heures - moyenne)</br>

##### &emsp;<span class="badge badge-info">Radar</span>
###### &emsp;[Documentation des données radar](http://geomet-dev-22.cmc.ec.gc.ca:8082/msc-data/obs_radar/readme_radar_fr/)
* Type de précipitation à la surface du radar (expérimental)
* Taux de précipitation radar extrapolé (expérimental)
* Couverture radar dynamique pour le type de précipitation à la surface (expérimental)</br>

##### &emsp;<span class="badge badge-info">Autres</span>

* [Alertes météo (experimental)](../msc-data/alerts/readme_alerts_fr.md)
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
        js.src = "../../../js/ice_storms_theme_ie.js";
        document.getElementById("controller").setAttribute("hidden", true);
    }
    else
    {
        js.src = "../../../js/ice_storms_theme.js";
    }
    head.appendChild(js);
</script>