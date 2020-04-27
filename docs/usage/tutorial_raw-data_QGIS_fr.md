[In English](readme_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > Usage overview


# Logiciel de bureau (QGIS) - Manipualtion de fichiers géospatiaux


Dans les prochaines sections, des exemples d'ajout de données géospatiales sont présentés en détails à l'aide de GIF animés.


## Ajout de fichiers géospatiaux dans QGIS

QGIS est un logiciel de système d'information géographique (SIG) et permet la visualisation et la manipulation des données géospatiales de type vectorielles (Shapefile, GeoJSON, GeoPackage, etc) ou matricielles (GRIB2, GeoTIFF, NetCDF, etc).

### Procédure

1. Dans la barre de menu, choisir : <b>Couche - Ajouter une couche - Ajouter une couche vecteur | raster</b> <br> <img src="http://iweb.cmc.ec.gc.ca/~afsslor/tmp/image/fr/qgis_ajouter_couche.png" width=60%>
2. Cliquer sur <img src="http://iweb.cmc.ec.gc.ca/~afsslor/tmp/image/fr/qgis_menu_couche.png" width=3%> puis naviguer jusqu'au fichier géospatial à ajouter
3. Cliquer sur <img src="http://iweb.cmc.ec.gc.ca/~afsslor/tmp/image/fr/qgis_button_ajouter.png" width=5%> pour afficher la couche

### Exemple de GIF animé

![Ajout d'une donnée géosptiale](http://iweb.cmc.ec.gc.ca/~afsslor/tmp/gif/french_add_GRIB2.gif)

## Ajout de fichiers géospatiaux du Datamart dans QGIS

Il est possible d'ajouter directement des fichiers géospatiaux du Datamart dans QGIS en glissant et déposant un fichier dans l'interface cartographique de QGIS.

Voici la liste des formats de fichiers géospatiaux du Datamart qui peuvent être directement ajouter dans QGIS :

* Matriciel
    * GRIB2 (.grib2)
    * NetCDF (.nc)
    * GeoTIFF (.tif)
* Vectoriel
    * Shapefile (.shp : il est a noter que pour ajouter un fichier Shapfile dans QGIS, il faut aussi avoir télécharger les autres extensions :.prj, .dbf et .shx et que ces fichiers se trouvent dans le même dossier)
    * GeoJSON (.geojson)

### Procédure

1. Aller sur le site web du [Datamart](https://dd.meteo.gc.ca) et naviguer jusqu'au fichier à ajouter
2. Glisser et déposer le fichier dans l'interface cartographique de QGIS

### Exemple de GIF animé

![Ajout d'une donnée géospatiale du Datamart](http://iweb.cmc.ec.gc.ca/~afsslor/tmp/gif/french_add_GRIB2_from_DD.gif)
