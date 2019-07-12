[In English](readme_cansips_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > SPISCan

# Données et Produits du Système de Prévision Interannuelle et Saisonnière Canadien (SPISCan)

Le Système de Prévision Interannuelle et Saisonnière Canadien (SPISCan) procède à des calculs physiques afin de produire des prévisions probabilistes d'éléments de l'atmosphère du début d'un mois jusqu'à 12 mois dans le futur. Les éléments de l'atmosphère incluent notamment la température, la précipitation, la vitesse et direction des vents. Ce produit contient les résultats numériques bruts de ces calculs. La couverture géographique est mondiale. Les données sont disponibles pour quelques niveaux verticaux choisis et sur une grille de résolution spatiale de 2.5 degrées. Ces prévisions ainsi que les rétro-prévision correspondantes sont disponibles mensuellement.

## Description du système

SPISCan est un système d'ensemble multi-modèle (Multi-Model Ensemble [MME]) utilisant deux modèles climatiques développés au Centre canadien de la modélisation et de l'analyse climatique (CCmaC). Ce système de prévision est entièrement couplé atmosphère-océan-glace-sol. SPISCan utilise l'infrastructure d'assimilation en place pour les autres systèmes de prévision afin d'obtenir les conditions initiales de l'atmosphère, de la température de la surface de la mer et de glace marine.

Pour plus de détails sur ce système, consultez :

https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/lib/op_systems/doc_opchanges/technote_spiscan_20111220_f.pdf

__Modèles__ :
 
* CanCM3 and CanCM4 - les modèles couplés atmosphère-océan
* CanAM3 and CanAM4 - les composantes atmosphériques 
* CanOM4 - la composante océanique

Les modèles atmosphériques, CanAM3 et CanAM4, sont couplés avec le modèle océanique CanOM4 et forment les modèles couplés du climat CanCM3 et CanCM4 respectivement.

Pour une description plus détaillée de ces modèles svp voir le lien :  

http://www.ec.gc.ca/ccmac-cccma/default.asp?lang=Fr&n=4A642EDE-1

__Configuration des prévisions SPISCan__ :
 
SPISCan est composé de 20 membres, 10 membres du modèle CanCM3 et 10 membres du modèle CanCM4. Le dernier jour de chaque mois on exécute une prévision de 12 mois et chaque membre est initialisé avec des conditions initiales valides au même moment, mais légèrement différentes. Les conditions initiales sont produites par la méthode IAU (Incremental Analyses Update), où les valeurs provenantes des analyses atmosphériques du CMC sont incrémentées de six heures en utilisant les modèles CanCM3 et CanCM4.

Lorsque la prévision de l'ensemble est terminée, on construit une moyenne saisonnière de l'anomalie, en soustrayant la moyenne climatologique de 30 ans de ces modèles. Ensuite, on calcule la moyenne d'ensemble pour une prévision déterministe, et les probabilités de chaque catégorie, calculées en calibrant le comptage des membres, pour une prévision probabiliste.

## Accès

### Comment accéder aux données

Ces données sont respectivement disponibles sur les services serveur de données [Datamart du SMC](../../msc-datamart/readme_fr.md) et les services web [GeoMet du SMC](../../msc-geomet/readme_fr.md) :

* [Données GRIB2 disponibles sur le Datamart du SMC](readme_cansips-datamart_fr.md) 
* [Indices en format CSV disponibles sur le Datamart du SMC](readme_cansips-datamartcsv_fr.md)
* [Données disponibles via les services web géospatiaux](../../msc-geomet/readme_fr.md)

Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est disponible.

### Licence

La [licence d’utilisation finale pour les serveurs de données d’Environnement et Changement climatique Canada](../../licence/readme_fr.md) précise les conditions d'utilisation de ces données.

### Métadonnées

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

* [Note technique](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_cansips-v2_20190703_e.pdf)
* [Arcticle scientifique - Version anglaise seulement](https://journals.ametsoc.org/doi/abs/10.1175/MWR-D-12-00216.1)

## Registre des changements 

La chronologie des changements apportés aux systèmes opérationnels est disponible [ici](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/changes_f.html).
