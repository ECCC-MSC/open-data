[In English](tutorial_raw-data_QGIS_en.md)

![ECCC logo](../img_eccc-logo.png)

[TOC](../readme_fr.md) > [Aperçu de l'utilisation](readme_fr.md) > Fichier brut dans QGIS

# Tutoriel : ajout de fichier brut géospatial dans QGIS

[QGIS](https://qgis.org) est un logiciel de système d'information géographique (SIG) et permet la visualisation et la manipulation des données géospatiales de type vectorielles (Shapefile, GeoJSON, GeoPackage, etc) ou matricielles (GRIB2, GeoTIFF, NetCDF, etc). Pour ajouter un fichier brut géospatial dans QGIS :

1. Dans la barre de menu, choisir : <b>Couche - Ajouter une couche - Ajouter une couche vecteur / raster</b><br> <img src="https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/usage/images_QGIS/qgis_add-layer_fr.png" width=60%>
2. Naviguer jusqu'au fichier géospatial à ajouter
3. Cliquer sur <img src="https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/usage/images_QGIS/qgis_button-add_fr.png" width=5%> pour afficher la couche

Exemple animé d'ajout de fichier géospatial dans QGIS :

![Ajout d'une donnée géospatiale](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/usage/images_QGIS/qgis_add-raw-file_fr.gif)

Il est possible d'ajouter directement des fichiers géospatiaux du [Datamart du SMC](../msc-datamart/readme_fr.md) dans QGIS en glissant et déposant un fichier dans l'interface cartographique de QGIS :

1. Aller sur le [site web du Datamart du SMC](https://dd.meteo.gc.ca) et naviguer jusqu'au fichier à ajouter
2. Glisser et déposer le fichier dans l'interface cartographique de QGIS

Voici des exemples de formats de fichiers géospatiaux disponibles sur le Datamart du SMC qui peuvent être directement ajoutés dans QGIS :

* Donnée matricielle :
    * GRIB2 (.grib2)
    * NetCDF (.nc)
    * GeoTIFF (.tif)
* Donnée vectorielle :
    * GeoJSON (.geojson)
    * Shapefile (.shp) : notez que pour ajouter un fichier Shapefile dans QGIS, il faut également avoir téléchargé les autres extensions : .prj, .dbf et .shx et que ces fichiers se retrouvent dans le même répertoire

La même approche fonctionne également pour ajouter les fichiers bruts récupérés par les services web WCS et OGC API - Features de [GeoMet du SMC](../msc-geomet/readme_fr.md).

Exemple animé d'ajout de fichier géospatial du Datamart du SMC dans QGIS via Firefox :

![Ajout d'une donnée géospatiale du Datamart](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/usage/images_QGIS/qgis_add-raw-file-from-dd_fr.gif)
