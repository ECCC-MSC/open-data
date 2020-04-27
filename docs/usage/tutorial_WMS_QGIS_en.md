[En français](tutorial_WMS_QGIS_fr.md)

![ECCC logo](../img_eccc-logo.png)

[TOC](../readme_en.md) > [Usage overview](readme_en.md) > WMS layers in QGIS 

# Tutorial: display, interact and animate WMS layers in QGIS

Usage examples of [MSC GeoMet](../msc-geomet/readme_en.md) geospatial web services in the [free and open source QGIS desktop software](https://qgis.org):

RENDU ICI

* [Ajout de données WMS dans QGIS](#ajout-de-données-wms-dans-qgis)
* [Interaction possible avec les données WMS dans QGIS](#interactions-possibles-avec-les-donnéees-wms-dans-qgis)
* [Manipulation de la composante de temps du WMS](#manipulation-de-la-composante-de-temps-du-wms)

## Ajout de couches WMS dans QGIS

L'utilisation de couches WMS (Web Map Service) permet de facilement ajouter des données géospatiales à un projet QGIS sans devoir télécharger et créer soi-même les styles des couches.

Dans l'exemple suivant, la couche de température de l'air du système de prévision global déterministe du SMC (SGPD) est affichée à partir de [GeoMet du SMC](../msc-geomet/readme_fr.md) :

https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/usage/WeatherCan_MSC-GeoMet_weather-radar_20200207_fr.jpg

1. Ouvrir l'explorateur de QGIS
    * Clic-droit dans la barre d'outil
    * Cochez <img src="https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/usage/images_QGIS/qgis_panneau-explorateur_fr.png" width="20%">
2. Ajouter un service WMS
    * Dans l'explorateur, clic-droit sur `WMS/WMTS` : <img src="https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/usage/images_QGIS/qgis_wms-nouvelle-connection_fr.png" width="20%">
    * Choisir un nom pour le service et l'écrire dans la case `Nom`
    * Entrer l'URL du service web géospatial : [https://geo.weather.gc.ca/geomet?lang=fr&service=WMS&version=1.3.0&request=GetCapabilities](https://geo.weather.gc.ca/geomet?lang=fr&service=WMS&version=1.3.0&request=GetCapabilities) dans la case `URL`
    * Cliquer sur `OK`
3. Ajouter une couche WMS au projet
    * Retourner dans l'explorateur sous `WMS/WMTS` et naviguer dans l'arborescence pour atteindre la couche désirée

Exemple animé de la procédure :

![Ajout d'une couche WMS dans QGIS](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/usage/images_QGIS/qgis_add-wms_fr.gif)

## Interactions possibles avec les données WMS dans QGIS

Voici les manipulations de base d'une couche WMS :

* Pour se déplacer sur la carte : <img src="https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/usage/images_QGIS/qgis_button-pan.png">
* Pour zoomer sur un endroit sur la carte : <img src="https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/usage/images_QGIS/qgis_button-zoom-in.png">
* Pour faire un zoom arrière sur la carte : <img src="https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/usage/images_QGIS/qgis_button-zoom-out.png">
* Pour faire un "GetFeatureInfo" et obtenir la valeur brute d'un pixel ou d'un élément géospatial d'une couche WMS : <img src="https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/usage/images_QGIS/qgis_button-getfeatureinfo.png">

Exemple animé de ces manipulations :

![Exemple d'intéractions avec les données WMS](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/usage/images_QGIS/qgis_wms-pan-zoom-gfi_fr.gif)

## Manipulation de la composante temporelle du WMS

Exemple de manipulation de la dimensions temporelle d'une couche WMS :

1. Ajouter une couche WMS avec au moins une dimension temporelle en utilisant le panneau explorateur (se référer à la section [ajout de données WMS dans QGIS](#ajout-de-données-wms-dans-qgis))
2. Après avoir ajouté une couche WMS, double-cliquer sur la petite horloge à côté du nom de la couche dans le panneau "couche" : <img src="https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/usage/images_QGIS/qgis_button-temporal.png">
3. S'assurer que les propriétés temporelles de la couches sont reconnues
    * "Temporal" doit être coché
    * "Specify time range" doit être choisi
    * Vérifier que "Start date" et que "End date" correspondent bien aux valeurs temporelles de la couches dans le "GetCapabilities"
    * Fermer la fenêtre des propriétés de la couche
4. Ouvrir le panneau de control temporel dans la barre d'outil : cliquer sur <img src="https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/usage/images_QGIS/qgis_button-temporal.png">
    * Mettre les valeurs temporelles à jour en cliquant sur le bouton : <img src="https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/usage/images_QGIS/qgis_button-temporal-refresh.png" width="5%">
    * Ajuster le pas de temps ("Step") en fonction de l'interval de la dimension temporelle de la couche WMS. Cette information est disponible dans le "GetCapabilities" de la couche
    * Utiliser les outils d'animation pour manipuler ou animer la couche WMS

Exemple animé de manipulation temporelle de couche WMS :

![Manipulation de la composante de temps du WMS](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/usage/images_QGIS/qgis_wms-temporal_fr.gif)
