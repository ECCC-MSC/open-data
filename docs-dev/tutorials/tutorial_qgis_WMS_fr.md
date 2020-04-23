[In English](readme_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > Usage overview


# Logiciel de bureau (QGIS) - Travailler avec le WMS


Dans les prochaines sections, des exemples de manipulation des données des services web géospatiaux [GeoMet du SMC](../msc-geomet/readme_fr.md) sont présentés en détails à l'aide de GIF animés.


* [Ajout de données WMS dans QGIS](#ajout-de-données-wms-dans-qgis)
* [Interaction possible avec les données WMS dans QGIS](#interaction-possible-avec-les-donnéees-wms-dans-qgis)
* [Manipulation de la composante de temps du WMS](#manipulation-de-la-composante-de-temps-du-wms)

## Ajout de données WMS dans QGIS

L'utilisation de couches WMS (Web Map Service) permet de facilement ajouter des données géospatiales à un projet QGIS sans devoir télécharger et créer soi-même les styles des couches.

Pour cette exemple, nous voudrons afficher la couche de température de l'air du système de prévision global déterministe du SMC (SGPD) à partir de [GeoMet du SMC](../msc-geomet/readme_fr.md).

### Procédure

1. Ouvrir l'explorateur de QGIS
    * Clic-droit dans la barre d'outil
    * Cochez <img src="http://iweb.cmc.ec.gc.ca/~afsslor/tmp/image/fr/qgis_panneau_explorateur.png" width="20%">
2. Ajouter un service WMS
    * Dans l'explorateur, clic-droit sur `WMS/WMTS` : <img src="http://iweb.cmc.ec.gc.ca/~afsslor/tmp/image/fr/qgis_wms_nouvelle_connection.png" width="20%">
    * Choisir un nom pour le service et lécrire dans la case `Nom`
    * Entrer l'URL du service web géospatial : [https://geo.weather.gc.ca/geomet?](https://geo.weather.gc.ca/geomet?) dans la case `URL`
    * Cliquer sur `OK`
3. Ajouter une couche WMS au projet
    * Retourner dans l'explorateur sous `WMS/WMTS` et naviguer dans l'arborescence pour atteindre la couche désirée

### Exemple de GIF animé

![Ajout d'une couche WMS](http://iweb.cmc.ec.gc.ca/~afsslor/tmp/gif/french_add_wms.gif)

## Interaction possible avec les données WMS dans QGIS

Dans la prochaine section, seront présenté les interactions de bases possibles avec une couche WMS.

### Manipulations de base avec une couche WMS

* Pour se déplacer sur la carte : <img src="http://iweb.cmc.ec.gc.ca/~afsslor/tmp/image/fr/qgis_button_pan.png">
* Pour zoomer sur un endroit sur la carte : <img src="http://iweb.cmc.ec.gc.ca/~afsslor/tmp/image/fr/qgis_button_zoom_in.png">
* Pour faire un zoom arrière sur la carte : <img src="http://iweb.cmc.ec.gc.ca/~afsslor/tmp/image/fr/qgis_button_zoom_out.png">
* Pour faire un "GetFeatureInfo" et obtenir la valeur brute d'un pixel ou d'un élément géospatial d'une couche WMS : <img src="http://iweb.cmc.ec.gc.ca/~afsslor/tmp/image/fr/qgis_button_getfeatureinfo.png">

### Exemple de GIF animé

![Exemple d'intéractions avec les données WMS](http://iweb.cmc.ec.gc.ca/~afsslor/tmp/gif/french_wms_pan_zoom_GFI.gif)


## Manipulation de la composante de temps du WMS

Exemple de manipulation de la dimensions temporelle d'une couche WMS

### Procédure

1. Ajouter une couche WMS avec au moins une dimension temporelle en utilisant le panneau explorateur (se référer à : [Ajout de données WMS dans QGIS](#ajout-de-données-wms-dans-qgis))
2. Après avoir ajouté une couche WMS, double-cliquer sur la petite horloge à côté du nom de la couche dans le panneau "couche" : <img src="http://iweb.cmc.ec.gc.ca/~afsslor/tmp/image/fr/qgis_button_temporal.png">
3. S'assurer que les propriétés temporelles de la couches sont reconnues
    * "Temporal" doit être coché
    * "Specify time range" doit être choisi
    * Vérifier que "Start date" et que "End date" correspondent bien aux valeurs temporelles de la couches dans le "GetCapabilities"
    * Quitter l'interface des propriétés de la couche
4. Ouvrir le panneau de control temporel dans la barre d'outil : cliquer sur <img src="http://iweb.cmc.ec.gc.ca/~afsslor/tmp/image/fr/qgis_button_temporal.png">
    * Mettre les valeurs temporelles à jour en cliquant sur le bouton : <img src="http://iweb.cmc.ec.gc.ca/~afsslor/tmp/image/fr/qgis_button_temporal_reset.png" width="5%">
    * Ajuster le pas de temps ("Step") en fonction de l'interval de la dimension temporelle de la couche WMS. Cette information est disponible dans le "GetCapabilities" de la couche
    * Utiliser les outils d'animation pour manipuler ou animer la couche WMS

### Exemple de GIF animé

![Manipulation de la composante de temps du WMS](http://iweb.cmc.ec.gc.ca/~afsslor/tmp/gif/french_wms_temporal.gif)
