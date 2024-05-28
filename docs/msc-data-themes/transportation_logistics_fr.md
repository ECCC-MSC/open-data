[In English](transportation_logistics_en.md)

![ECCC logo](../img_eccc-logo.png)

[TOC](../readme_fr.md) > [Thèmes des données](readme_fr.md) > Logistique de transport terrestre

# Logistique de transport terrestre&emsp;<i class="wi wi-train" style="font-size: 45px; color: #4e64a6;"></i>

Cette page présente une liste de jeux de données pertinents du Service météorologique du Canada sous le thème de la logistique de transport terrestre, afin de guider les utilisateurs vers les jeux de données appropriés. Cette liste n'est pas exhaustive, mais donne un aperçu des couches qui peuvent être utilisées sous ce thème. Les principales couches de données pour ce thème sont les variables des taux de précipitations. Cependant, un certain nombre d'autres couches pertinentes peuvent également fournir des informations supplémentaires sur le sujet, telles que les rafales de vent, la visibilité ou possibilité de poudrerie sur les trajets, pour ne citer que ces quelques exemples.

Exemple de carte interactive comportant les couches du Service de cartographie Web (WMS) des `Alerte météo`, de `HRDPS.CONTINENTAL` (Maximum des rafales de vent) et de `GDPS-WEonG`(Visibilité: brouillard liquide) (actives sur la carte), ainsi que d'autres couches optionnelles qui peuvent être ajoutées en cochant les cases de la liste dans la carte. Les couches sont desservies par GeoMet du SMC :

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
          <span onmouseover="updateLegend('https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=HRDPS.CONTINENTAL_WGX&format=image/png')">Maximum des rafales de vent</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer2" checked>
          <span onmouseover="updateLegend('https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=HRDPS-WEonG_2.5km_LiquidFogVisibility&format=image/png')">Visibilité: brouillard liquide</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer5">
          <span onmouseover="updateLegend('https://geo.weather.gc.ca/geomet?lang=fr&version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=HRDPS-WEonG_2.5km_BlowingSnowPresence&format=image/png&STYLE=BlowingSnowPresence_Dis_Fr')">Présence de poudrerie</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer3">
          <span onmouseover="updateLegend('https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=RDPS-WEonG_10km_FreezingPrecip-Prob&format=image/png')">Possibilité de pluie verglaçante</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer6">
          <span onmouseover="updateLegend('https://geo.weather.gc.ca/geomet?lang=fr&version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=RADAR_1KM_RSNO&format=image/png&STYLE=Radar-Snow_Dis-14colors_Fr')">Radar pour la neige</span>
        </label></br>
    </div>
  </div>
</div>
</br>

## Jeux de données

Il est à noter que les différentes couches présentées dans la liste qui suit, sont disponibles à différentes résolutions et différentes échéances temporelles.
Les couches de la liste suivante peuvent être également visualisées sur AniMet du SMC avec un [permalien](https://eccc-msc.github.io/msc-animet/?layers=ALERTS;0.75;0;1;0,Radar_1km_SfcPrecipType;0.75;0;1;0,Radar_1km_RainPrecipRate-Extrapolation;0.75;0;1;0,Radar_1km_SnowPrecipRate-Extrapolation;0.75;0;1;0,HRDPS-WEonG_2.5km_WindSpeed;0.75;0;1;0,HRDPS-WEonG_2.5km_WindGust;0.75;0;1;0,HRDPS-WEonG_2.5km_FreezingPrecip-Prob;0.75;0;1;0,RDPS-WEonG_10km_FreezingPrecip-Prob;0.75;0;1;0,GDPS-WEonG_15km_BlowingSnow-Prob;0.75;0;1;0,HRDPS-WEonG_2.5km_BlowingSnowPresence;0.75;0;1;0,RDPS-WEonG_10km_BlowingSnowPresence;0.75;0;1;0,RADAR_1KM_RSNO;0.75;0;1;0,GDPS-WEonG_15km_FreezingDrizzle-Prob;0.75;0;1;0,GDPS-WEonG_15km_IcePellets-Prob;0.75;0;1;0,GDPS-WEonG_15km_WindGust;0.75;0;1;0,HRDPS.CONTINENTAL_WGX;0.75;0;1;0,CURRENT_CONDITIONS;0.75;0;1;0,GOES-East_1km_DayVis;0.75;0;0;0,GOES-West_1km_DayVis;0.75;0;0;0,GDPS-WEonG_15km_IceFogVisibility;0.75;0;1;0,GDPS-WEonG_15km_LiquidFogVisibility;0.75;0;1;0,HRDPS-WEonG_2.5km_IceFogVisibility;0.75;0;1;0,HRDPS-WEonG_2.5km_LiquidFogVisibility;0.75;0;1;0,HRDPS.CONTINENTAL_FR;0.75;0;1;0,HRDPS.CONTINENTAL_NO;0.75;0;1;0,HRDPS.CONTINENTAL_WSPD;0.75;0;1;0&extent=-18847435,1845742,1190074,11911533) unique pour l'ensemble des variables.

##### &emsp;<span class="badge badge-info">SHRPD à la surface ou à proximité de la surface</span>
###### &emsp;[Documentation des données SHRPD](../msc-data/nwp_hrdps/readme_hrdps_fr.md)
* Maximum des rafales de vent
* Vitesse du vent à 10m au dessus de la surface
* Accumulation de ruissellement
* Pluie verglaçante accumulée</br>

##### &emsp;<span class="badge badge-info">SHRPD Continental - Éléments du temps sur grille</span>
###### &emsp;[Documentation des données SHRPD](../msc-data/nwp_hrdps/readme_hrdps_fr.md)
* Visibilité à travers le brouillard liquide
* Visibilité dans le brouillard glacé
* Présence de poudrerie
* Probabilité de précipitation verglaçante
* Rafale de vents
* Vitesse du vent</br>

##### &emsp;<span class="badge badge-info">SGPD - Éléments du temps sur grille</span>
###### &emsp;[Documentation des données SGPD](../msc-data/nwp_gdps/readme_gdps_fr.md)
* Visibilité à travers le brouillard liquide
* Visibilité dans le brouillard glacé
* Rafale de vents
* Probabilité de grésil
* Probabilité de bruine verglaçante
* Probabilité de poudrerie</br>

##### &emsp;<span class="badge badge-info">SRPD - Éléments du temps sur grille</span>
###### &emsp;[Documentation des données SRPD](../msc-data/nwp_rdps/readme_rdps_fr.md)
* Présence de poudrerie
* Probabilité de précipitation verglaçante</br>


##### &emsp;<span class="badge badge-info">Radar</span>
###### &emsp;[Documentation des données radar](../msc-data/obs_radar/readme_radar_fr.md)
* Type de précipitation à la surface du radar (expérimental)
* Taux de précipitation radar extrapolé pour la pluie (expérimental)
* Taux de précipitation radar extrapolé pour la neige (expérimental)
* Taux de précipitation radar pour la neige</br>

##### &emsp;<span class="badge badge-info">Satellite GOES</span>
###### &emsp;[Documentation des données satellite](../msc-data/obs_satellite/readme_satellite_fr.md)
* Visibilité de jour / Convection nuageuse de jour (Ouest)
* Visibilité de jour / Convection nuageuse de jour (Est)</br>

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
        js.src = "../../js/transportation_logistics_theme_ie.js";
        document.getElementById("controller").setAttribute("hidden", true);
    }
    else
    {
        js.src = "../../js/transportation_logistics_theme.js";
    }
    head.appendChild(js);
</script>