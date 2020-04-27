[In English](tutorial_OAFeat_QGIS_en.md)

![ECCC logo](../img_eccc-logo.png)

[TOC](../readme_fr.md) > [Aperçu de l'utilisation](readme_fr.md) > Couches OGC API - Features dans QGIS

# Tutoriel : utilisation de données OGC API - Features dans QGIS

Ajout de données OGC API - Features dans QGIS :

1. Dans la barre de menu, choisir : <b>Couche - Ajouter une couche - Ajouter une couche WFS</b> <br> <img src="https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/usage/images_QGIS/qgis_ajouter-wfs_fr.png" width=60%> 
2. Ajouter une nouvelle connexion
    * Cliquer sur <img src="https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/usage/images_QGIS/qgis_button-new_fr.png" width=7%> pour ajouter une nouvelle connexion
    * Choisir un nom pour le service et l'écrire dans la case `Nom`
    * Entrer l'URL du service web géospatial : [https://geo.weather.gc.ca/geomet/features](https://geo.weather.gc.ca/geomet/features) dans la case `URL`
    * Dans la boite `Option WFS` à la ligne `Version`, sélectionner <img src="https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/usage/images_QGIS/qgis_button-ogc-api-features.png" width=15%> 
    * Cliquer sur `OK`
3. Cliquer sur <img src="https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/usage/images_QGIS/qgis_button-connexion_fr.png" width=7%> pour obtenir la liste des couches disponibles
4. Construire une requête (étape optionnelle)
    * Cliquer sur <img src="https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/usage/images_QGIS/qgis_button-construire-requete_fr.png" width=15%> pour construire une requête et filtrer les données à afficher
    * Construire une requête à l'aide des tableaux `Champs`, `Valeurs` et `Opérateurs`
    * Valider la requête en appuyant sur <img src="https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/usage/images_QGIS/qgis_button-test_fr.png" width=5%>
    * Cliquer sur `OK` 
5. Cliquer sur <img src="https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/usage/images_QGIS/qgis_button-add_fr.png" width=5%> pour afficher la couche

Veuillez vous référer à la section [OGC API - Features](../msc-geomet/web-services_fr/#ogc-api-features) pour de davantage de détails sur ce standard.

Exemple animé de couche OGC API - Features dans QGIS :

![Ajout de données OGC API Features](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/usage/images_QGIS/qgis_ogc-api-features-add-filters_fr.gif)
