[In English](readme_rdps_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > SRPD

# Données et produits du Système régional de prévision déterministe

Le Système régional de prévision déterministe (SRPD) procède à des calculs physiques afin de produire des prévisions déterministes d'éléments de l'atmosphère du jour présent jusqu'à 84 heures dans le futur. Les éléments de l'atmosphère incluent notamment la température, les précipitations, la couverture nuageuse, la vitesse et direction des vents et l'humidité. Ce produit contient les résultats numériques bruts de ces calculs. La couverture géographique inclut le Canada et les États-Unis. La résolution spatiale horizontale des données est d'environ 10 km distribuées sur au plus 33 niveaux verticaux. Les prévisions sont exécutées quatre fois par jour.

Note: Le Système régional de prévision déterministe est désormais une composante du [Système global de prévision déterministe (SGPD)](../nwp_gdps/readme_gdps_fr.md) à 10 km de résolution, sur un domaine nord-américain.

## Accès

### Comment accéder aux données

Ces données sont respectivement disponibles sur les services du serveur de données [Datamart du SMC](../../msc-datamart/readme_fr.md) et les services web [GeoMet du SMC](../../msc-geomet/readme_fr.md) :

* [Données disponibles via les services web géospatiaux GeoMet-Météo](../../msc-geomet/readme_fr.md)
* [Données GRIB2 disponibles sur le Datamart du SMC](readme_rdps-datamart_fr.md)
* [Données GeoJSON statistiquement post-traitées sur le Datamart du SMC](readme_rdps-statpostproc-datamart_fr.md)
* [Données expérimentales GRIB2 d'éléments du temps sur grille disponibles sur DD-Alpha, le site Web d'essai de données du Datamart du SMC](readme_rdps-datamart-alpha_fr.md) 
* [Produits GRIB2 d'astronomie disponibles sur DD-Alpha, le site Web d'essai de données du Datamart du SMC](readme_astro-rdps-datamart-alpha_fr.md)

Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est disponible.

### Licence

La [licence d’utilisation finale pour les serveurs de données d’Environnement et Changement climatique Canada](../../licence/readme_fr.md) précise les conditions d'utilisation de ces données.

### Politique d'utilisation des services de données ouvertes du SMC

La [Politique d'utilisation des services de données ouvertes du SMC](../../usage-policy/readme_fr.md) détermine ce qui constitue une utilisation appropriée des services de données ouvertes du SMC et fournit aux utilisateurs les pratiques exemplaires pour une utilisation optimale.

### Métadonnées de découverte

* Les [métadonnées du Système régional de prévision déterministe sont accessibles sur le portail du gouvernement ouvert](https://ouvert.canada.ca/data/fr/dataset/a9f2828c-0d78-5eb6-a4c7-1fc1219f1e3d)
* Les [métadonnées de la Prévision du système régional de prévision déterministe statistiquement post-traité par UMOS sont accessibles sur le portail du gouvernement ouvert](https://ouvert.canada.ca/data/fr/dataset/bb0d1eeb-0e11-49e0-a5e3-6d99d4decb31)


## Produits

Liste et liens vers les produits disponibles pour ce jeu de données :

### Cartes de prévision

* [Cartes 4 panneaux classiques](https://meteo.gc.ca/model_forecast/index_f.html)
* [Produits de prévision du temps violent](https://meteo.gc.ca/model_forecast/severe_weather_f.html)

### Cartes d'analyse aerologique

* [250hPa: Hauteur géopotentielle, vitesse du vent](https://meteo.gc.ca/data/analysis/sah_100.gif)
* [500 hPa: Hauteur géopotentielle, épaisseurs 1000-500hPa](https://meteo.gc.ca/data/analysis/sai_100.gif)
* [700 hPa: Hauteur géopotentielle, température, écart du point de rosée](https://meteo.gc.ca/data/analysis/saj_100.gif)
* [850 hPa: Hauteur géopotentielle, température ](https://meteo.gc.ca/data/analysis/saa_100.gif)

### Produits pour l'aviation

* [Turbulence et givrage](https://meteo.gc.ca/model_forecast/turb_f.html)
* [Documentation - Prévision aéronautique en 4 panneaux](aviation-package_fr.md)
* [Documentation - Prévisions de plafond en 4 paneaux](ceiling_fr.md)

### Produits pour l'astronomie

* [Prévision des nuages](https://meteo.gc.ca/astro/clds_vis_f.html)
* [Prévision de la scintillation des étoiles](https://meteo.gc.ca/astro/seeing_f.html)
* [Prévision de la transparence du ciel](https://meteo.gc.ca/astro/transparence_f.html)
* [Prévison près de la surface](https://meteo.gc.ca/astro/meteo_f.html)

## Documentation technique

* [Version actuelle du Système régional de prévision déterministe](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_RDPS_f.pdf)
* [Version actuelle du prologiciel de post-traitement statistique du Système régional de prévision déterministe](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/not_available.pdf)
* [Note technique](http://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_notes/technote_rdps_f.pdf)
* [Note technique du prologiciel de post-traitement statistique du Système régional de prévision déterministe](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/not_available.pdf)
* [Diagramme de dépendances](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwep-dependency-diagrams/system_RDPS_fr.svg)
* [Fiche d'information associée au dernier cycle d'innovation](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/fact_sheets/factsheet_rdps_f.pdf)

## Registre des changements 

La chronologie des changements apportés au Système régional de prévision déterministe (SRPD) est disponible [ici](changelog_rdps_fr.md).

