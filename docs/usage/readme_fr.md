[In English](readme_en.md)

![ECCC logo](../img_eccc-logo.png)

[TdM](../readme_fr.md) > Aperçu de l'utilisation

# Aperçu de l'utilisation

Aperçu de l'utilisation et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada (SMC).

* [Connaître quelles sont les données disponibles](#connaitre-quelles-sont-les-donnees-disponibles)
* [Comment visualiser les données](#comment-visualiser-les-donnees)
    * [Logiciel de bureau](#logiciel-de-bureau)
    * [Cartes interactives en-ligne et applications mobiles](#cartes-interactives-en-ligne-et-applications-mobiles)
    * [Images sur demande](#images-sur-demande)
* [Comment accéder aux données brutes](#comment-acceder-aux-donnees-brutes)
    * [Services web de données brutes](#services-web-de-donnees-brutes)
    * [Téléchargement de données brutes](#telechargement-de-donnees-brutes)
    * [Manipuler les données brutes à partir de la ligne de commandes](#manipuler-les-donnees-brutes-a-partir-de-la-ligne-de-commandes)

## Connaître quelles sont les données disponibles

Le Service météorologique du Canada rend disponible de l'information sur les conditions météorologiques, hydriques et environnementales passées, présentes et futures pour le Canada et le monde. [La liste des données disponibles est disponible ici](../msc-data/readme_fr.md).

## Comment visualiser les données

### AniMet du SMC

[AniMet du SMC](../msc-animet/readme_fr.md) est un outil simple permettant aux utilisateurs d'interagir avec les données météorologiques ouvertes du SMC et de créer des animations météorologiques personnalisées pour n'importe quelle région du monde. Les animations résultantes peuvent être téléchargées et partagées avec un permalien.

### Logiciel de bureau 

Les données ouvertes du SMC dans des logiciels de bureau soit (A) en se connectant au service Web Map Service (WMS) de [GeoMet du SMC](../msc-geomet/readme_fr.md) ou (B) en téléchargeant les données brutes du [Datamart du SMC](../msc-datamart/readme_fr.md) ou via le service Web Coverage Service (WCS) ou OGC API - Features (WFS 3) de GeoMet du SMC et en chargeant les données brutes dans l'application.

Les données ouvertes du SMC peuvent être visualisées interactivement dans les logiciels qui supportent le standard Web Map Service (WMS) de l'Open Geospatial Consortium (OGC), tel que le logiciel libre [QGIS](https://qgis.org) ainsi que ArcGIS d'Esri. Les instructions pour ajouter les couches WMS de GeoMet du SMC dans [QGIS](https://docs.qgis.org/3.4/en/docs/training_manual/online_resources/wms.html) et [ArcGIS](https://desktop.arcgis.com/en/arcmap/latest/map/web-maps-and-services/adding-wms-services.htm) sont disponibles. Les logiciels de bureau peuvent permettre aux usagers de changer les couleurs des couches (styles WMS) ainsi qu'animer les couches pour les pas de temps disponibles. Les détails techniques sur les paramètres WMS disponibles sont documentés dans la [section sur les services web](../msc-geomet/wms_fr.md). Pour télécharger des données brutes, veuillez vous référer à la section [Comment accéder aux données brutes](#comment-acceder-aux-donnees-brutes).

Les tutoriels suivants sont disponibles pour le logiciel de bureau QGIS : [ajouter, effectuer des requêtes et animer des couches WMS](tutorial_WMS_QGIS_fr.md), [ajouter et effectuer des requêtes aux couches OGC API Features](tutorial_OAFeat_QGIS_fr.md) et [ajouter des données brutes](tutorial_raw-data_QGIS_fr.md). L'image suivante présente la racine de l'arborescence des couches de GeoMet-Météo dans QGIS :

![L'arborescence des couches de GeoMet-Météo dans QGIS](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/usage/GeoMet-Weather_QGIS_Layer-tree_fr.jpg)

### Cartes interactives en-ligne et applications mobiles

Les données ouvertes du SMC peuvent également être aisément intégrées dans des cartes interactives en-ligne ainsi que dans des applications mobiles.

#### Dans un fureteur web

En utilisant des librairies JavaScript telles que [Leaflet](https://leafletjs.com/) et [Openlayers](https://openlayers.org/), parmi d'autres, les utilisateurs peuvent intégrer les couches disponibles de GeoMet du SMC dans leurs propres cartes interactives en-ligne.

Le [tutoriel suivant est disponible pour la création de cartes interactives sur le web avec OpenLayers et Leaflet](tutorial_web-maps_fr.md), démontrant comment ajouter des couches, afficher des boîtes de dialogue, ainsi que d'animer des couches temporelles.

Ci-après est un exemple de carte interactive configurée avec OpenLayers et présentant des [couches WMS de la composite radar météo servies par GeoMet du SMC](../msc-data/obs_radar/readme_radar_geomet_fr.md).

<div id="map" style="height: 400px; position: relative">
  <div id="legend-popup">
  <div id="legend-popup-content">
    <img id="legend-img" src="https://geo.weather.gc.ca/geomet?lang=fr&version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=RADAR_1KM_RRAI&format=image/png&STYLE=Radar-Rain_Dis-14colors_Fr"/>
  </div>
</div>
</div>
<div id="controller" role="group" aria-label="Animation controls" style="background: #ececec; padding: 0.5rem;">
  <button id="fast-backward" class="btn btn-primary btn-sm" type="button"><i class="fa fa-fast-backward" style="padding: 0rem 1rem"></i></button>
  <button id="step-backward" class="btn btn-primary btn-sm" type="button"><i class="fa fa-step-backward" style="padding: 0rem 1rem"></i></button>
  <button id="play-pause" class="btn btn-primary btn-sm" type="button"><i class="fa fa-play" style="padding: 0rem 1rem"></i></button>
  <button id="step-forward" class="btn btn-primary btn-sm" type="button"><i class="fa fa-step-forward" style="padding: 0rem 1rem"></i></button>
  <button id="fast-forward" class="btn btn-primary btn-sm" type="button"><i class="fa fa-fast-forward" style="padding: 0rem 1rem"></i></button>
  <button id="exportmap" class="btn btn-primary btn-sm" type="button"><i class="fa fa-download" style="padding: 0rem 1rem"></i></button>
  <a id="image-download" download="msc-geomet_web-map_export.png"></a>
  <span id="info" style="padding-left: 0.5rem;cursor: pointer;"></span>
</div>

#### Dans une application mobile

Les services WMS de GeoMet du SMC peuvent également être intégrées dans des applications mobiles, par exemple avec des librairies JavaScript telles que [Leaflet](https://leafletjs.com/) et [Openlayers](https://openlayers.org/). Ceci est démontré dans [l'application MétéoCAN](https://www.canada.ca/fr/environnement-changement-climatique/services/conditions-meteorologiques-ressources-outils-generaux/meteocan.html) d'Environnement et Changement climatique Canada, disponible pour iOS et Android, qui utilise GeoMet du SMC pour afficher les données radar météo à haute résolution sur une carte interactive :

![Exemple de couche radar dans MeteoCAN](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/usage/WeatherCan_MSC-GeoMet_weather-radar_20200207_fr.jpg)

Pour de l'information additionnelle sur les capacités et les paramètres des services web WMS, WFS et WCS de GeoMet du SMC, veuillez vous référer à la section sur la [documentation technique des services web GeoMet du SMC](../../msc-geomet/readme_fr/#standards-disponibles).

### Images sur demande

GeoMet du SMC peut également servir des images sur demande par le biais d'une requête WMS GetMap. Voici des exemples.

#### Exemple 1 - Température de surface du Système global de prévision déterministe (SGPD)

La requête WMS GetMap suivante retourne une image de la couche de température de l'air du Système global de prévision déterministe (SGPD). Cette image est générée sur demande au moment de la requête.

```
https://geo.weather.gc.ca/geomet?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&BBOX=-90,-180,90,180
&CRS=EPSG:4326&WIDTH=600&HEIGHT=301&LAYERS=GDPS.ETA_TT&FORMAT=image/png
```
Retourne :

![Température de surface du Système global de prévision déterministe (SGPD)](https://geo.weather.gc.ca/geomet?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&BBOX=-90,-180,90,180&CRS=EPSG:4326&WIDTH=600&HEIGHT=301&LAYERS=GDPS.ETA_TT&FORMAT=image/png)

#### Exemple 2 - Salinité de l'eau de la mer du Système Global de Prévision Océan-Glace (SGPOG)

La requête WMS GetMap suivante retourne une image de la couche de salinité de l'eau de la mer du Système Global de Prévision Océan-Glace (SGPOG). Cette image est générée sur demande au moment de la requête.

```
https://geo.weather.gc.ca/geomet?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&BBOX=-90,-180,90,180
&CRS=EPSG:4326&WIDTH=600&HEIGHT=301&LAYERS=OCEAN.GIOPS.2D_SALW&FORMAT=image/png
```
Retourne :

![Salinité de l'eau de la mer du Système Global de Prévision Océan-Glace (SGPOG)](https://geo.weather.gc.ca/geomet?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&BBOX=-90,-180,90,180&CRS=EPSG:4326&WIDTH=600&HEIGHT=301&LAYERS=OCEAN.GIOPS.2D_SALW&FORMAT=image/png)

#### Survol des paramètres WMS GetMap utilisés dans ces exemples

Les exemples ci-dessus précisent certains paramètres et envoient une requête WMS GetMap à GeoMet du SMC. Voici une courte explication de chacun de ces paramètres :

* **SERVICE** - le nom du service web de l'Open Geospatial Consortium utilisé dans la requête. Dans les deux exemples, le standard Web Map Service (WMS) est utilisé
* **VERSION** - la version du service, dans ce cas, `1.3.0`
* **REQUEST** - le type de requête spécifié. Le service WMS rend disponible plusieurs types de requêtes. Dans le cas présent, une requête GetMap est spécifiée, ce qui retourne une image
* **BBOX** - l'étendue géographique associée à l'image désirée. Dans ce cas, la requête couvre l'ensemble de la surface de la planète. Les coordonnées sont fournies dans les unités du système de coordonnées cartographiques spécifié dans le paramètre qui suit
* **CRS** - le système de coordonnées cartographiques utilisé pour créer l'image désirée. Dans les deux exemples, le CRS est `EPSG:4326` (i.e. WGS 84), le système de coordonnées cartographiques utilisé notamment par le Système mondial de positionnement (GPS)
* **WIDTH** - la largeur en pixels de l'image retournée
* **HEIGHT** - la hauteur en pixels de l'image retournée
* **LAYERS** - le nom de la couche à utiliser pour la création de l'image. Pour de meilleures performances, il est recommandé de demander une couche par requête WMS. La liste et le nom des couches disponibles peut être récupérée via une requête WMS GetCapabilities
* **FORMAT** - le format de l'image retournée par la requête WMS GetMap. Dans les deux exemples, l'image retournée est dans le format PNG

Pour de l'information additionnelle sur les paramètres WMS GetMap, veuillez vous référer à la section sur la [documentation technique des services web GeoMet du SMC](../msc-geomet/wms_fr.md).

## Comment accéder aux données brutes

### Services web de données brutes

Les données brutes du SMC peuvent être récupérées par les [services web GeoMet du SMC](../msc-geomet/readme_fr.md). Ces services web permettent aux usagers de récupérer les données brutes en spécifiant les coordonnées géographiques, la projection cartographique, les dimensions temporelles et en choisissant parmi les formats de données disponibles. Les détails sur les paramètres à spécifier sont disponibles dans la section de la documentation technique sur les [services web](../../msc-geomet/readme_fr.md#standards-disponibles).

Les exemples de cas d'utilisation suivants sont disponibles :

* [Arthur : profits anticipés selon la probabilité de précipitation](../use-case_arthur/use-case_arthur_fr/):
    * Accéder et utiliser l'API GeoMet du SMC directement dans un script Python, spécifiquement le standard OGC Web Map Service (WMS) pour créer des tables et graphiques
* [Cathy : suivre les niveaux d'eau aux stations hydrométriques](../use-case_oafeat/use-case_oafeat-script_fr/):
    * Accéder et utiliser l'API GeoMet du SMC directement dans un script Python, spécifiquement le standard OGC API - Features (OAFeat) pour créer des séries temporelles et cartes interactives
* [Gerald : profil thermique de l'atmosphère pour voyager sécuritairement](../use-case_skewt/use-case_skewt_fr/):
    * Accéder et utiliser l'API GeoMet du SMC directement dans un script Python, spécifiquement le standard OGC API - Process (OAProc) pour créer des tables et graphiques

Les données brutes à des lieux géographiques spécifiques peuvent être récupérées par une requête Web Map Service (WMS) GetFeatureInfo. Les détails sont disponibles dans [la documentation technique](../msc-geomet/wms_fr.md#wms-getfeatureinfo). Voici un exemple de [requête WMS GetFeatureInfo pour la temperature du Système global de prévision déterministe (SGPD) pour Montréal, Canada](https://geo.weather.gc.ca/geomet/?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetFeatureInfo&QUERY_LAYERS=GDPS.ETA_TT&INFO_FORMAT=application/json&i=5&j=5&EXCEPTIONS=xml&LAYERS=GDPS.ETA_TT&CRS=EPSG:4326&BBOX=45.50,-73.56,45.51,-73.55&WIDTH=10&HEIGHT=10).

Les données brutes pour des données vectorielles peuvent être récupérées par une requête OGC API - Features (WFS 3). Exemple d'une [requête WFS 3 pour les données des moyennes quotidiennes hydrométriques à la station Winnipeg River](https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=05PF049) qui retourne les données correspondantes en tant que fichier GeoJSON.

Les données brutes pour des données matricielles peuvent être récupérées par une requête Web Coverage Service (WCS). Exemple d'une [requête WCS 2 pour l'Analyse régionale de déterministe de précipitation (ARPD) au format netCDF à un pas de temps spécifié](https://geo.weather.gc.ca/geomet?SERVICE=WCS&VERSION=2.0.1&REQUEST=GetCoverage&COVERAGEID=RDPA.6F_PR&SUBSETTINGCRS=EPSG:4326&FORMAT=image/netcdf&TIME=2019-05-14T12:00:00Z). [Un tutoriel est disponible pour sauvegarder la sortie d'une requête WCS sur le disque](../tutorial_gdal/tutorial_gdal_fr/). Une astuce pour construire des requêtes WCS est d'utiliser [l'Outil d'extraction de données climatiques du Centre canadien des services climatiques pour la couche ARPD](https://changements-climatiques.canada.ca/donnees-climatiques/#/analyse-regionale-deterministe-precipitation) et remplacer la valeur COVERAGEID de RDPA.* pour une autre couche disponible.

### Téléchargement de données brutes

Les données brutes du SMC peuvent être [automatiquement récupérées du Datamart du SMC dès quelles deviennent disponibles par le biais du protocol Advanced Message Queuing Protocol (AMQP)](../msc-datamart/amqp_fr.md). Alternativement, les données brutes peuvent également être téléchargées directement sur le web sur le serveur [Datamart du SMC](../msc-datamart/readme_fr.md).

### Manipuler les données brutes à partir de la ligne de commandes

Les données peuvent être manipulées en utilisant des commandes de la librairie logicielle GDAL. Un [tutoriel démontrant les commandes les plus communes de la librairie logicielle GDAL](../tutorial_gdal/tutorial_gdal_fr/) est disponible.

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
  .distinguish-switch{
    top: 8px;
    right: 2.25em;
    width: 10rem;
  }
  .ol-touch .distinguish-switch{
    top: 80px;
  }
  .distinguish-switch.ol-unselectable.ol-control button{
    width: 10rem;
  }
</style>

<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/ol@v7.3.0/ol.css" type="text/css"/>
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
        js.src = "../../js/radar_ie.js";
        document.getElementById("controller").setAttribute("hidden", true);
    }
    else
    {
        js.src = "../../js/radar.js";
    }
    head.appendChild(js);
</script>