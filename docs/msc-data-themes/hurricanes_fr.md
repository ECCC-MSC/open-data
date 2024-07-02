[In English](hurricanes_en.md)

![ECCC logo](../img_eccc-logo.png)

[TOC](../readme_fr.md) > [Thèmes des données](readme_fr.md) > Ouragans

# Ouragans&emsp;<i class="wi wi-hurricane" style="font-size: 45px; color: #4e64a6;"></i>

Cette page présente une liste de jeux de données pertinentes du Service Météorologique du Canada sous le thème des ouragans, afin de guider les usagers vers les jeux de données appropriés. Cette liste n'est pas exhaustive mais, donne un aperçu des couches pouvant être utilisées sous cette thématique. Les principales couches de données sont les trajectoires d'ouragans et la zone de réaction aux ouragans qui sont émises par le Centre canadien de prévision des ouragans, dans le cadre des prévisions régulières lors de la saison des ouragans. Cependant, plusieurs autres couches pertinentes peuvent également apporter une complémentarité sur le sujet telles; la vitesse des vents, les quantités de pluie ou les vagues cotiêres, pour ne donner ici, que queques exemples.
</br> 

Exemple de carte interactive comportant les couches `Zone de réaction aux ouragans`, `Alertes météorologiques` et `HRDPS-WeonG`(Rafale de vents) (actives sur la carte) du Service de cartographie Web (WMS), ainsi qu'un certain nombre de couches optionnelles qui peuvent être ajoutées en cochant les cases de la liste dans la carte. Les couches sont desservies par GeoMet du SMC :

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
          <span onmouseover="updateLegend('https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=HURRICANE_RESPONSE_ZONE&format=image/png')">Zone d'ouragans</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer6" checked>
          <span onmouseover="updateLegend('https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=ALERTS&format=image/png&STYLE=ALERTES')">Alertes météo</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer2" checked>
          <span onmouseover="updateLegend('https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=HRDPS-WEonG_2.5km_WindGust&format=image/png')">Rafale de vents</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer1">
          <span onmouseover="updateLegend('https://geo.weather.gc.ca/geomet?lang=fr&version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=HRDPS-WEonG_2.5km_TotalPrecipIntensityIndex&format=image/png&STYLE=TotalPrecipIntensityIndex_Dis_Fr')">Précipitations totales</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer3">
          <span onmouseover="updateLegend('https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=HRDPS-WEonG_2.5km_Thunderstorm-Prob&format=image/png')">Probabilité d'orages</span>
        </label></br>
        <label>
          <input type="checkbox" id="layer4">
          <span onmouseover="updateLegend('https://geo.weather.gc.ca/geomet?lang=fr&version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=CURRENT_CONDITIONS&format=image/png&STYLE=default')">Conditions actuelles</span>
        </label></br>
    </div>
  </div>
</div>
</br>

## Jeux de données

Il est à noter que les différentes couches présentées dans la liste qui suit, sont disponibles à différentes résolutions et différentes échéances temporelles.
Les couches de la liste suivante peuvent être également visualisées sur AniMet du SMC avec un [permalien](https://eccc-msc.github.io/msc-animet/?layers=Radar-Coverage_SfcPrecipType%3B0.75%3B1%3B1%3B0,RDPS.CONV_SFC-CAPE%3B0.75%3B0%3B1%3B0,HURRICANE_CENTRE%3B0.75%3B0%3B1%3B0,HURRICANE_RAD%3B0.75%3B0%3B1%3B0,HURRICANE_RESPONSE_ZONE%3B0.75%3B0%3B1%3B0,RDPA-Prelim_10km_Precip-Accum24h%3B0.75%3B0%3B1%3B0,RDPS.CONV_TOTALX.PT3H%3B0.75%3B0%3B1%3B0,RDWPS_2.5km_WindWavesSignificantHeight%3B0.75%3B0%3B1%3B0,RADAR_1KM_RRAI%3B0.75%3B0%3B1%3B0,Radar_1km_RainPrecipRate-Extrapolation%3B0.75%3B0%3B1%3B0,HRDPS.CONTINENTAL_P0%3B0.75%3B0%3B1%3B0,HRDPS.CONTINENTAL_PN%3B0.75%3B0%3B1%3B0,HRDPS.CONTINENTAL_RN%3B0.75%3B0%3B1%3B0,HRDPS.CONTINENTAL_WGX%3B0.75%3B0%3B1%3B0,HRDPS-WEonG_2.5km_Thunderstorm-Prob%3B0.75%3B0%3B1%3B0,HRDPS-WEonG_2.5km_TotalPrecipIntensityIndex%3B0.75%3B0%3B1%3B0,HRDPS-WEonG_2.5km_WindGust%3B0.75%3B0%3B1%3B0,HRDPS-WEonG_2.5km_WindSpeed%3B0.75%3B0%3B1%3B0,ALERTS%3B0.75%3B0%3B1%3B0,CURRENT_CONDITIONS%3B0.75%3B0%3B1%3B0,Lightning_2.5km_Density%3B0.75%3B0%3B1%3B0,METNOTES%3B0.75%3B0%3B1%3B0&extent=-22088883,-731482,1411752,11074002) unique pour l'ensemble des variables.

##### &emsp;<span class="badge badge-info">Ouragans</span>
###### &emsp;[Documentation des données sur les ouragans](../msc-data/hurricanes/readme_hurricanes_fr.md)
* Rayons de prévisions de vent (quadrants)
* Points de prévision</br>

##### &emsp;<span class="badge badge-info">SHRPD Continental - Éléments du temps sur grille</span>
###### &emsp;[Documentation des données SHRPD](../msc-data/nwp_hrdps/readme_hrdps_fr.md)
* Rafale de vents
* Indice d'intensité des précipitations totales
* Probabilité d'occurence d'orage</br>

##### &emsp;<span class="badge badge-info">SHRPD à la surface ou à proximité de la surface</span>
###### &emsp;[Documentation des données SHRPD](../msc-data/nwp_hrdps/readme_hrdps_fr.md)
* Maximum des rafales de vent
* Pluie accumulée
* Pression au niveau de la mer (contour)
* Pression au niveau de la mer</br>

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
###### &emsp;[Documentation des données radar](../msc-data/obs_radar/readme_radar_fr.md)
* Taux de précipitation radar extrapolé pour la pluie (expérimental)
* Taux de précipitation radar pour la pluie
* Couverture radar dynamique pour le type de précipitation à la surface (expérimental)</br>

##### &emsp;<span class="badge badge-info">SRPD - champs convectifs</span>
###### &emsp;[Documentation des données SRPD](../msc-data/nwp_rdps/readme_rdps_fr.md)
* EPCD pour une parcelle de la surface
* Indice du potentiel d'orages total</br>

##### &emsp;<span class="badge badge-info">Autres</span>

* [Alertes météo](../msc-data/alerts/readme_alerts_fr.md)
* [Densité de foudre sur le Canada (2.5 km)](../msc-data/lightning/readme_lightning_fr.md)
* [MetNotes](../msc-data/metnotes/readme_metnotes_fr.md)
* [Conditions actuelles](../msc-data/citypage-weather/readme_citypageweather_fr.md)
* [SRPDV - Hauteur significative des vagues de la mer du vent](../msc-data/nwp_rdwps/readme_rdwps_fr.md)
* [SGPDOT - Onde de tempête](../msc-data/nwp_gdsps/readme_gdsps_fr.md)
* [ARDP - Quantité de précipitations sur un intervalle de 24 heures (préliminaire)](../msc-data/nwp_rdpa/readme_rdpa_fr.md)


<style>
  #legend-img {
    margin: 0px;
  }
  #legend-popup {
    position: absolute;
    top: 8px;
    right: 40px;
    z-index: 2
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