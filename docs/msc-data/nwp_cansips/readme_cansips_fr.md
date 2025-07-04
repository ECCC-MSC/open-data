[In English](readme_cansips_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > SPISCan

# Données et Produits du Système de Prévision Interannuelle et Saisonnière Canadien (SPISCan)

Le Système de Prévision Interannuelle et Saisonnière Canadien (SPISCan) procède à des calculs physiques afin de produire des prévisions probabilistes d'éléments de l'atmosphère du début d'un mois jusqu'à 12 mois dans le futur. Ceci permet d'établir des prévisions saisonnières. Les éléments de l'atmosphère incluent notamment la température, la précipitation, la vitesse et direction des vents. Ce produit contient les résultats numériques bruts de ces calculs. La couverture géographique est mondiale. Les données sont disponibles pour quelques niveaux verticaux choisis et sur une grille de résolution spatiale de 2.5 degrées et 1 degrée. De plus, les prévisions probabilistes des températures et des précipitations sous la normale, près de la normale, et au-dessus de la normale sont disponibles aux deux résolutions. Ces prévisions ainsi que les rétro-prévisions correspondantes sont disponibles mensuellement.

## Accès

### Comment accéder aux données

Ces données sont respectivement disponibles sur les services web [GeoMet du SMC](../../msc-geomet/readme_fr.md) et les services du serveur de données [Datamart du SMC](../../msc-datamart/readme_fr.md) :

* [Données disponibles via les services web géospatiaux GeoMet-Météo](readme_cansips-geomet_fr.md)
* [Données disponibles sur les services web géospatiaux GeoMet-OGC-API](https://api.meteo.gc.ca/) :
    * [SPISCan - membres à 250 km](https://api.meteo.gc.ca/collections/weather:cansips:250km:forecast:members)
* [Les données en GRIB2 des membres et des produits disponibles sur le Datamart du SMC](readme_cansips-datamart_fr.md)
* [Indices en format CSV disponibles sur le Datamart du SMC](readme_cansips-datamartcsv_fr.md)

Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est disponible.

### Licence

La [licence d’utilisation finale pour les serveurs de données d’Environnement et Changement climatique Canada](../../licence/readme_fr.md) précise les conditions d'utilisation de ces données.

### Politique d'utilisation des services de données ouvertes du SMC

La [Politique d'utilisation des services de données ouvertes du SMC](../../usage-policy/readme_fr.md) détermine ce qui constitue une utilisation appropriée des services de données ouvertes du SMC et fournit aux utilisateurs les pratiques exemplaires pour une utilisation optimale.

### Métadonnées de découverte

Les [métadonnées du Système de Prévision Interannuelle et Saisonnière Canadien sont accessibles sur le portail du gouvernement ouvert](https://ouvert.canada.ca/data/fr/dataset/922781a9-bfef-56b9-a438-493ada629d47)

## Produits

Liste et liens vers les produits disponibles pour ce jeu de données :

### Cartes de prévisions déterministes

* [Prévisions déterministes de la température](https://meteo.gc.ca/saisons/det_f.html)
* [Prévisions déterministes des précipitations](https://meteo.gc.ca/saisons/det_f.html)
* [Prévisions déterministes courantes de la température](https://meteo.gc.ca/saisons/image_f.html?img=sfe1t_s&bc=det)
* [Prévisions déterministes courantes des précipitations](https://meteo.gc.ca/saisons/image_f.html?img=sfe1p_s&bc=det)
* [Prévisions déterministes de la température émises au début du mois dernier](https://meteo.gc.ca/saisons/image_f.html?img=sfe1tm1_s&bc=det)
* [Prévisions déterministes des précipitations émises au début du mois dernier](https://meteo.gc.ca/saisons/image_f.html?img=sfe1pm1_s&bc=det)
* [Prévisions déterministes de la température émises il y a deux mois](https://meteo.gc.ca/saisons/image_f.html?img=sfe1tm2_s&bc=det)
* [Prévisions déterministes des précipitations émises il y a deux mois](https://meteo.gc.ca/saisons/image_f.html?img=sfe1pm2_s&bc=det)

### Cartes de prévisions probabilistes

* [Prévisions probabilistes de la température et des précipitations](https://meteo.gc.ca/saisons/prob_f.html)

### Prévisions Saisonnières

* [Habileté du système de prévisions déterministes](https://meteo.gc.ca/saisons/skill_f.html)
* [Vérification des prévisions passées](https://meteo.gc.ca/saisons/ver_f.html)
* [Climatologie de la température et des précipitations](https://meteo.gc.ca/saisons/clim_f.html)

### Analyses des anomalies de la température de surface de la mer, de la glace et de la neige

* [Analyse de surface](https://meteo.gc.ca/saisons/sea-snow_f.html)
* [Analyse de surface - Quotidienne ](https://meteo.gc.ca/saisons/image_f.html?id=daily&img=2019061000_054_G6_global_I_SEASON_tm@lg@sd_000&bc=sea)
* [Analyse de surface - Animation une année](https://meteo.gc.ca/saisons/animation_f.html?id=year&bc=sea)
* [Analyse de surface - Moyenne de 30 jours](https://meteo.gc.ca/saisons/image_f.html?id=average&img=2019061000_054_G6_global_I_SEASON_avg@tm@lg@sd@720_000&bc=sea)
* [Analyse de surface - Animation de 30 jours](https://meteo.gc.ca/saisons/animation_f.html?id=month&bc=sea)

## Documentation technique

* [Version actuelle du Système de Prévision Interannuelle et Saisonnière Canadien](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_CANSIPS_f.pdf)
* [Note technique](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_cansips_e.pdf)
* [Arcticle scientifique - Version anglaise seulement](https://journals.ametsoc.org/doi/abs/10.1175/MWR-D-12-00216.1)
* [Diagramme de dépendances](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwep-dependency-diagrams/system_CanSIPS_fr.svg)
* [Fiche d'information associée au dernier cycle d'innovation](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/fact_sheets/factsheet_cansips_f.pdf)

## Registre des changements 

La chronologie des changements apportés au Système de Prévision Interannuelle et Saisonnière Canadien (SPISCan) est disponible [ici](changelog_cansips_fr.md).
