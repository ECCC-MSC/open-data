[In English](floods_en.md)

![ECCC logo](../img_eccc-logo.png)

[TOC](../readme_fr.md) > [Thèmes des données](readme_fr.md) > Inondations

# Inondations&emsp;<i class="wi wi-flood" style="font-size: 45px; color: #4e64a6;"></i>

Cette page présente une liste de jeux de données pertinents du Service météorologique du Canada sous le thème des inondations, afin de guider les utilisateurs vers les jeux de données appropriés. Cette liste n'est pas exhaustive, mais donne un aperçu des couches qui peuvent être utilisées sous ce thème. Les principales couches de données pour ce thème sont les quantités de précipitations. Cependant, un certain nombre d'autres couches pertinentes peuvent également fournir des informations supplémentaires sur le sujet, telles que le ruissellement ou l'eau précipitable contenue dans les nuages, pour ne citer que quelques exemples.

Exemple de carte interactive comportant les couches du Service de cartographie Web (WMS) `HRDPA.24F_PR` (Quantité de précipitations), `Alertes météo` et `Conditions actuelles` (actives sur la carte), ainsi que d'autres couches optionnelles qui peuvent être ajoutées en cochant les cases de la liste dans la carte. Les couches sont desservies par GeoMet du SMC :

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
          <span onmouseover="updateLegend('https://geo.wxod-dev.cmc.ec.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=HRDPA.24F_PR&format=image/png&STYLE=CAPA24-LINEAR')">Quantité de précipitations</span>
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
          <input type="checkbox" id="layer6">
          <span onmouseover="updateLegend('https://geo.wxod-dev.cmc.ec.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=HRDPS.CONTINENTAL_PC&format=image/png&STYLE=CAPA24-LINEAR')">Précipitations convectives</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer3">
          <span onmouseover="updateLegend('https://geo.wxod-dev.cmc.ec.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=RADAR_1KM_RRAI&format=image/png&STYLE=Radar-Rain_Dis-14colors_Fr')">Précipitations par radar</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer5">
          <span onmouseover="updateLegend('https://geo.wxod-dev.cmc.ec.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=HRDPS.CONTINENTAL_IH&format=image/png&STYLE=CAPA24-LINEAR')">Eau précipitable</span>
        </label></br>
    </div>
  </div>
</div>
</br>

## Jeux de données

Il est à noter que les différentes couches présentées dans la liste qui suit, sont disponibles à différentes résolutions et différentes échéances temporelles.
Les couches de la liste suivante peuvent être également visualisées sur AniMet du SMC avec un [permalien](https://eccc-msc.github.io/msc-animet/?layers=HRDPA.6F_PR;0.75;0;1;0,HRDPA.24F_PR;0.75;1;1;0,ALERTS;0.75;0;1;0,CURRENT_CONDITIONS;0.75;0;1;0,RADAR_1KM_RRAI;0.75;0;1;0,Radar_1km_RainPrecipRate-Extrapolation;0.75;0;1;0,HRDPS.CONTINENTAL_IH;0.75;0;1;0,HRDPS.CONTINENTAL_PC;0.75;0;1;0,HRDPS.CONTINENTAL_RN;0.75;0;1;0,GEPS.DIAG.96_PRMM.ERGE100;0.75;0;1;0,GEPS.DIAG.96_PRMM.ERGE150;0.75;0;1;0,GEPS.DIAG.96_PRMM.ERGE200;0.75;0;1;0,GEPS.DIAG.120_PRMM.ERGE100;0.75;0;1;0,GEPS.DIAG.120_PRMM.ERGE150;0.75;0;1;0,GEPS.DIAG.120_PRMM.ERGE200;0.75;0;1;0,GDPS.ETA_NO.3h;0.75;0;1;0,HRDPS.CONTINENTAL_NO;0.75;0;1;0,RDPS.ETA_NO;0.75;0;1;0&extent=-14583377,2738020,-2263679,8926788) unique pour l'ensemble des variables.

##### &emsp;<span class="badge badge-info">SHRPD à la surface ou à proximité de la surface</span>
###### &emsp;[Documentation des données SHRPD](../msc-data/nwp_hrdps/readme_hrdps_fr.md)
* Accumulation de ruissellement
* Pluie accumulée
* Précipitations convectives
* Eau précipitable</br>

##### &emsp;<span class="badge badge-info">AHRDP</span>
###### &emsp;[Documentation des données AHRDP](../msc-data/nwp_hrdpa/readme_hrdpa_fr.md)
* Quantité de précipitations (6 heures)
* Quantité de précipitations (24 heures)</br>

##### &emsp;<span class="badge badge-info">Radar</span>
###### &emsp;[Documentation des données radar](../msc-data/obs_radar/readme_radar_fr.md)
* Taux de précipitation radar pour la pluie
* Taux de précipitation radar extrapolé pour la pluie (expérimental)</br>

##### &emsp;<span class="badge badge-info">SGPE - champs diagnostiques</span>
###### &emsp;[Documentation des données SGPE](../msc-data/nwp_geps/readme_geps_fr.md)
* Probabilité de quantité de précipitations supérieures à 100 mm (96 heures)
* Probabilité de quantité de précipitations supérieures à 150 mm (96 heures)
* Probabilité de quantité de précipitations supérieures à 200 mm (96 heures)
* Probabilité de quantité de précipitations supérieures à 100 mm (120 heures)
* Probabilité de quantité de précipitations supérieures à 150 mm (120 heures)
* Probabilité de quantité de précipitations supérieures à 200 mm (120 heures)</br>

##### &emsp;<span class="badge badge-info">Autres</span>

* [Alertes météo](../msc-data/alerts/readme_alerts_fr.md)
* [Conditions actuelles](../msc-data/citypage-weather/readme_citypageweather_fr.md)
* [Accumulation de ruissellement (SRDP)](../msc-data/nwp_rdps/readme_rdps_fr.md)


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