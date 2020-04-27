[In English](readme_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > Usage overview


# Logiciel de bureau (QGIS) - Travailler avec l'OGC API - Feature

## Ajout de données OGC API - Features dans QGIS

Veuillez vous référer à la page [OGC API - Features](https://eccc-msc.github.io/open-data/msc-geomet/web-services_fr/#ogc-api-features) de la documentation publique du SMC pour plus d'informations sur ce standard web géospatial.

### Procédure

1. Dans la barre de menu, choisir : <b>Couche - Ajouter une couche - Ajouter une couche WFS</b> <br> <img src="http://iweb.cmc.ec.gc.ca/~afsslor/tmp/image/fr/qgis_ajouter_wfs.png" width=60%> 
2. Ajouter une nouvelle connexion
    * Cliquer sur <img src="http://iweb.cmc.ec.gc.ca/~afsslor/tmp/image/fr/qgis_button_nouveau.png" width=7%> pour ajouter une nouvelle connexion
    * Choisir un nom pour le service et lécrire dans la case `Nom`
    * Entrer l'URL du service web géospatial : [https://geo.weather.gc.ca/geomet/features](https://geo.weather.gc.ca/geomet/features) dans la case `URL`
    * Dans la boite `Option WFS` à la ligne `Version` sélectionner <img src="http://iweb.cmc.ec.gc.ca/~afsslor/tmp/image/fr/qgis_wfs_OGC_API-Features.png" width=15%> 
    * Cliquer sur `OK`
3. Cliquer sur <img src="http://iweb.cmc.ec.gc.ca/~afsslor/tmp/image/fr/qgis_button_connexion.png" width=7%> voir la liste des couches disponibles
4. ***Étape Optionnelle*** : Construire une requête
    * Cliquer sur <img src="http://iweb.cmc.ec.gc.ca/~afsslor/tmp/image/fr/qgis_button_construire_requete.png" width=15%> pour construire une requête et filtrer les données à afficher
    * Construire une requête à l'aide des tableaux `Champs`, `Valeurs` et `Opérateur`
    * Valider la requête en appuyant sur <img src="http://iweb.cmc.ec.gc.ca/~afsslor/tmp/image/fr/qgis_button_tester.png" width=5%>
    * Cliquer sur `OK` 
5. Cliquer sur <img src="http://iweb.cmc.ec.gc.ca/~afsslor/tmp/image/fr/qgis_button_ajouter.png" width=5%> pour afficher la couche
### Exemple de GIF animé

![Ajout de données WFS3](http://iweb.cmc.ec.gc.ca/~afsslor/tmp/gif/french_OGC_API_FEATURES_addfilters.gif)
