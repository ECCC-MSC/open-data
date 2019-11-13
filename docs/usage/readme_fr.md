[In English](readme_en.md)

![ECCC logo](../img_eccc-logo.png)

[TdM](../readme_fr.md) > Aperçu de l'utilisation

# Aperçu de l'utilisation

Aperçu de l'utilisation et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada (SMC).

* [Connaître quelles sont les données disponibles](#connaitre-quelles-sont-les-donnees-disponibles)
* [Comment visualiser les données](#comment-visualiser-les-donnees)
    * [Logiciel de bureau](#logiciel-de-bureau)
    * [Cartes interactives en-ligne et applications mobiles](#cartes-interactives-en-ligne-et-applications-mobiles)
    * [Images à la volée](#images-a-la-volee)
* [Comment accéder aux données brutes](#comment-acceder-aux-donnees-brutes)
    * [Téléchargement de données brutes](#telechargement-de-donnees-brutes)
    * [Services web de données brutes](#services-web-de-donnees-brutes)


## Connaître quelles sont les données disponibles

Le Service météorologique du Canada rend disponible de l'information sur les conditions météorologiques, hydriques et environnementales passées, présentes et futures pour le Canada et le monde. [La liste des données disponibles est disponible ici](../msc-data/readme_fr.md).

## Comment visualiser les données

### Logiciel de bureau 

Les données ouvertes du SMC dans des logiciel de bureau soit (A) en se connectant au service Web Map Service (WMS) de [GeoMet du SMC](../msc-geomet/readme_fr.md) ou (B) en téléchargeant les données brutes du [Datamart du SMC](../msc-datamart/readme_fr.md) ou via le service Web Coverage Service (WCS) ou OGC API - Features (WFS 3) de GeoMet du SMC et en chargeant les données brutes dans l'application.

Les données ouvertes du SMC peuvent être visualisées interactivement dans les logiciels qui supportent le standard Web Map Service (WMS) de l'Open Geospatial Consortium (OGC), tel que le logiciel libre [QGIS](https://qgis.org) ainsi que ArcGIS d'Esri. Les instructions pour ajouter les couches WMS de GeoMet du SMC dans [QGIS](https://docs.qgis.org/3.4/en/docs/training_manual/online_resources/wms.html) et [ArcGIS](https://desktop.arcgis.com/en/arcmap/latest/map/web-maps-and-services/adding-wms-services.htm) sont disponibles. Les logiciels de bureau peuvent permettre aux usagers de changer les couleurs des couches (styles WMS) ainsi qu'animer les couches pour les pas de temps disponibles. Les détails techniques sur les paramètres WMS disponibles sont documentés dans la [section sur les services web](../msc-geomet/web-services_fr.md).

Pour télécharger des données brutes, veuillez vous référer à la section [Comment accéder aux données brutes](#comment-acceder-aux-donnees-brutes).

### Cartes interactives en-ligne et applications mobiles

Les données ouvertes du SMC peuvent également être aisément intégrées dans des cartes interactives en-ligne ainsi que dans des applications mobiles.

#### Dans un fureteur web

En utilisant des librairies JavaScript telles que [Leaflet](https://leafletjs.com/) et [Openlayers](https://openlayers.org/), parmi d'autres, les utilisateurs peuvent intégrer les couches disponibles de GeoMet du SMC dans leurs propres cartes interactives en-ligne.

Ci-après est un exemple de carte interactive configurée avec OpenLayers et présentant la couche WMS de composite radar météo services par GeoMet du SMC.

<div id="map" style="height: 400px"></div>

#### Dans une application mobile

Les services WMS de GeoMet du SMC peuvent également être intégrées dans des applications mobiles. Ceci est démontré dans [l'application MétéoCAN](https://www.canada.ca/fr/environnement-changement-climatique/services/conditions-meteorologiques-ressources-outils-generaux/meteocan.html) d'Environnement et Changement climatique Canada, disponible pour iOS et Android, qui utilise GeoMet du SMC pour afficher les données radar météo à haute résolution sur une carte interactive :

![Exemple de couche radar dans MeteoCAN](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/usage/WeatherCAN_GeoMet_Radar_Hurricane_Michael_20181010_162830.png)

Pour de l'information additionnelle sur les capacités et les paramètres des services web WMS, WFS et WCS de GeoMet du SMC, veuillez vous référer à la section sur la [documentation technique des services web GeoMet du SMC](../msc-geomet/web-services_fr.md).

### Images à la volée

GeoMet du SMC peut également servir des images à la volée par le biais d'une requête WMS GetMap. Voici des exemples.

#### Exemple 1 - Température de surface du Système global de prévision déterministe (SGPD)

La requête WMS GetMap suivante retourne une image de la couche de température de l'air du Système global de prévision déterministe (SGPD). Cette image est générée à la volée au moment de la requête.

```
https://geo.weather.gc.ca/geomet?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&BBOX=-90,-180,90,180
&CRS=EPSG:4326&WIDTH=600&HEIGHT=301&LAYERS=GDPS.ETA_TT&FORMAT=image/png
```
Retourne :

![Température de surface du Système global de prévision déterministe (SGPD)](https://geo.weather.gc.ca/geomet?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&BBOX=-90,-180,90,180&CRS=EPSG:4326&WIDTH=600&HEIGHT=301&LAYERS=GDPS.ETA_TT&FORMAT=image/png)

#### Exemple 2 - Salinité de l'eau de la mer du Système Global de Prévision Océan-Glace (SGPOG)

La requête WMS GetMap suivante retourne une image de la couche de salinité de l'eau de la mer du Système Global de Prévision Océan-Glace (SGPOG). Cette image est générée à la volée au moment de la requête.

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

Pour de l'information additionnelle sur les paramètres WMS GetMap, veuillez vous référer à la section sur la [documentation technique des services web GeoMet du SMC](../msc-geomet/web-services_fr.md).

## Comment accéder aux données brutes

### Téléchargement de données brutes

Les données brutes du SMC peuvent être [automatiquement récupérées dès quelles deveinnent disponibles par le biais du protocol Advanced Message Queuing Protocol (AMQP)](../msc-datamart/amqp_fr.md).

Les données brutes peuvent également être téléchargées directement sur le web sur le serveur [Datamart du SMC](../msc-datamart/readme_fr.md).

### Services web de données brutes

Les données brutes du SMC peuvent être récupérées par les services web GeoMet du SMC. Ces services web permettent aux usagers de récupérer les données brutes en spécifiant les coordonnées géographiques, la projection cartographique, les dimensions temporelles et en choisissant parmi les formats de données disponibles. Les détails sur les paramètres à spécifier sont disponibles dans la section sur les [services web](../msc-geomet/web-services_fr.md).

Les données brutes à des lieux géographiques spécifiques peuvent être récupérées par une requête Web Map Service (WMS) GetFeatureInfo. Voici un exemple de [requête WMS GetFeatureInfo pour la temperature du Système global de prévision déterministe (SGPD) pour Montréal, Canada](https://geo.weather.gc.ca/geomet/?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetFeatureInfo&QUERY_LAYERS=GDPS.ETA_TT&INFO_FORMAT=text/plain&i=5&j=5&EXCEPTIONS=xml&LAYERS=GDPS.ETA_TT&CRS=EPSG:4326&BBOX=45.50,-73.56,45.51,-73.55&WIDTH=10&HEIGHT=10).

Les données brutes pour des données vectorielles peuvent être récupérées par une requête OGC API - Features (WFS 3). Exemple d'une [requête WFS 3 pour les données des moyennes quotidiennes hydrométriques à la station Winnipeg River](https://geo.weather.gc.ca/geomet/features/collections/hydrometric-daily-mean/items?STATION_NUMBER=05PF049) qui retourne les données correspondantes en tant que fichier GeoJSON.

Les données brutes pour des données matricielles peuvent être récupérées par une requête Web Coverage Service (WCS). Exemple d'une [requête WCS 2 pour l'Analyse régionale de déterministe de précipitation (ARPD) au format netCDF à un pas de temps spécifié](https://geo.weather.gc.ca/geomet?SERVICE=WCS&VERSION=2.0.1&REQUEST=GetCoverage&COVERAGEID=RDPA.6F_PR&SUBSETTINGCRS=EPSG:4326&FORMAT=image/netcdf&TIME=2019-05-14T12:00:00Z). Une astuce pour construire des requêtes WCS est d'utiliser [l'Outil d'extraction de données climatiques du Centre canadien des services climatiques pour la couche ARPD](https://changements-climatiques.canada.ca/donnees-climatiques/#/analyse-regionale-deterministe-precipitation) et remplacer la valeur COVERAGEID de RDPA.* pour une autre couche disponible.

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/openlayers/4.6.5/ol.css" integrity="sha256-rQq4Fxpq3LlPQ8yP11i6Z2lAo82b6ACDgd35CKyNEBw=" crossorigin="anonymous" />
<script src="https://cdnjs.cloudflare.com/ajax/libs/openlayers/4.6.5/ol.js" integrity="sha256-77IKwU93jwIX7zmgEBfYGHcmeO0Fx2MoWB/ooh9QkBA=" crossorigin="anonymous"></script>
<script type="text/javascript">
      var map = new ol.Map({
        target: 'map',
        layers: [
          new ol.layer.Tile({
            source: new ol.source.OSM()
          }),
          new ol.layer.Tile({
            source: new ol.source.TileWMS({
                format: 'image/png',
                url: 'https://geo.weather.gc.ca/geomet/',
                params: {'LAYERS': 'RADAR_1KM_RSNO', 'TILED': true},
            })
          })
          new ol.layer.Tile({
            source: new ol.source.TileWMS({
                format: 'image/png',
                url: 'https://geo.weather.gc.ca/geomet/',
                params: {'LAYERS': 'RADAR_COVERAGE_RSNO.INV', 'TILED': true},
            })
        ],
        view: new ol.View({
          center: ol.proj.fromLonLat([-97, 57]),
          zoom: 3
        })
      });
</script>
