[In English](thunderstorms_en.md)

![ECCC logo](../img_eccc-logo.png)

[TOC](../readme_fr.md) > [Thèmes des données](readme_fr.md) > Orages

# Orages&emsp;<i class="wi wi-lightning" style="font-size: 45px; color: #4e64a6;"></i>

Cette page présente une liste de jeux de données pertinents du Service météorologique du Canada sous le thème des orages, afin de guider les utilisateurs vers les jeux de données appropriés. Cette liste n'est pas exhaustive, mais donne un aperçu des couches qui peuvent être utilisées sous ce thème. Les principales couches de données pour ce thème sont les variables de vents et les quantités de précipitations. Cependant, un certain nombre d'autres couches pertinentes peuvent également fournir des informations supplémentaires sur le sujet, telles que la probabilité d'occurence d'orage, les indice de Showalter ou de soulèvement de parcelle instable, pour ne citer que ces quelques exemples.

Exemple de carte interactive comportant les couches du Service de cartographie Web (WMS) `HRDPS.CONTINENTAL` (Taux de précipitation instantané), `Alertes météo` et `HRDPS.CONTINENTAL` (Indice de Showalter) (actives sur la carte), ainsi que d'autres couches optionnelles qui peuvent être ajoutées en cochant les cases de la liste dans la carte. Les couches sont desservies par GeoMet du SMC :

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
          <span onmouseover="updateLegend('https://geo.wxod-dev.cmc.ec.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=HRDPS.CONTINENTAL_RT&format=image/png&STYLE=PRECIPPRTMMH')">Taux de précipitation instantané</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer4" checked>
          <span onmouseover="updateLegend('https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=ALERTS&format=image/png&STYLE=ALERTES')">Alertes météo</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer1" checked>
          <span onmouseover="updateLegend('https://geo.wxod-dev.cmc.ec.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=HRDPS.CONTINENTAL.CONV_SHWINX.500&format=image/png&STYLE=LIFTED_INDEX-LINEAR')">Indice de Showalter</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer3">
          <span onmouseover="updateLegend('https://geo.wxod-dev.cmc.ec.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=HRDPS-WEonG_2.5km_Precip-Prob&format=image/png&STYLE=Precip-Prob')">Probabilité de précipitation</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer5">
          <span onmouseover="updateLegend('https://geo.wxod-dev.cmc.ec.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=HRDPS-WEonG_2.5km_WindGust&format=image/png&STYLE=GUST_INTERV_MS2KTS')">Rafale de vents</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer6">
          <span onmouseover="updateLegend('https://geo.wxod-dev.cmc.ec.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=HRDPS-WEonG_2.5km_Thunderstorm-Prob&format=image/png&STYLE=Thunderstorm-Prob')">Probabilité d'orages</span>
        </label></br>
    </div>
  </div>
</div>
</br>

## Jeux de données

Il est à noter que les différentes couches présentées dans la liste qui suit, sont disponibles à différentes résolutions et différentes échéances temporelles.
Les couches de la liste suivante peuvent être également visualisées sur AniMet du SMC avec un [permalien](https://eccc-msc.github.io/msc-animet/?layers=ALERTS;0.75;0;1;0,CURRENT_CONDITIONS;0.75;0;1;0,Lightning_2.5km_Density;0.75;1;1;0,RADAR_1KM_RRAI;0.75;0;1;0,Radar_1km_dBZ-Extrapolation;0.75;0;1;0,HRDPS-WEonG_2.5km_AirTemp;0.75;0;1;0,HRDPS-WEonG_2.5km_DewPointTemp;0.75;0;1;0,HRDPS-WEonG_2.5km_Precip-Prob;0.75;0;1;0,HRDPS-WEonG_2.5km_WindGust;0.75;0;1;0,HRDPS-WEonG_2.5km_WindDir;0.75;0;1;0,HRDPS-WEonG_2.5km_WindSpeed;0.75;0;1;0,HRDPS.CONTINENTAL.CONV_MU-VT-LI.500;0.75;0;1;0,HRDPS.CONTINENTAL.CONV_SHWINX.500;0.75;0;1;0,HRDPS.CONTINENTAL_IH;0.75;0;1;0,HRDPS.CONTINENTAL_PC;0.75;0;1;0,HRDPS.CONTINENTAL_RT;0.75;0;1;0,HRDPS-WEonG_2.5km_Thunderstorm-Prob;0.75;0;1;0&extent=-19347716,1946579,-535293,11257258) unique pour l'ensemble des variables.

##### &emsp;<span class="badge badge-info">SHRPD à la surface ou à proximité de la surface</span>
###### &emsp;[Documentation des données SHRPD](../msc-data/nwp_hrdps/readme_hrdps_fr.md)

* Taux de précipitation instantané
* Précipitations convectives
* Eau précipitable
* Indice de Showalter, au niveau de référence 500.0 mb
* Indice de soulèvement pour la parcelle la plus instable</br>

##### &emsp;<span class="badge badge-info">SHRPD Continental - Éléments du temps sur grille</span>
###### &emsp;[Documentation des données SHRPD](../msc-data/nwp_hrdps/readme_hrdps_fr.md)
* Probabilité d'occurence d'orage
* Vitesse du vent
* Direction du vent
* Rafale de vents
* Température
* Probabilité de précipitation
* Température du point de rosée</br>

##### &emsp;<span class="badge badge-info">SRPEOT</span>
###### &emsp;[Documentation des données SRPEOT](../msc-data/nwp_resps/readme_resps_fr.md)
* Onde de tempête  - Atlantique nord-ouest (membre de contrôle)
* Onde de tempête  - Atlantique nord-ouest (1)
* Onde de tempête  - Atlantique nord-ouest (2)
* Onde de tempête  - Atlantique nord-ouest (3)
* Onde de tempête  - Atlantique nord-ouest (4)
* Onde de tempête  - Atlantique nord-ouest (5)
* Onde de tempête  - Atlantique nord-ouest (6)</br>

##### &emsp;<span class="badge badge-info">Radar</span>
###### &emsp;[Documentation des données radar](../msc-data/nwp_reps/readme_radar_fr.md)
* Taux de précipitation radar pour la pluie
* Taux de précipitation radar extrapolé</br>

##### &emsp;<span class="badge badge-info">Autres</span>

* [Alertes météo (experimental)](../msc-data/alerts/readme_alerts_fr.md)
* [Conditions actuelles](../msc-data/citypage-weather/readme_citypageweather_fr.md)
* [Densité de foudre sur le Canada](../msc-data/lightning/readme_lightning_fr.md)
* [SGPDOT - Onde de tempête](../msc-data/nwp_gdsps/readme_gdsps_fr.md)


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
        js.src = "../../js/thunderstorms_theme_ie.js";
        document.getElementById("controller").setAttribute("hidden", true);
    }
    else
    {
        js.src = "../../js/thunderstorms_theme.js";
    }
    head.appendChild(js);
</script>