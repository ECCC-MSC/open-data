[In English](readme_cansips-datamartcsv_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [SPISCan](readme_cansips_fr.md) > Données CSV de SPISCan sur le Datamart du SMC

# Données CSV du Système de Prévision Interannuelle et Saisonnière Canadien (SPISCan)

Le [Système de prévision interannuelle et saisonnière canadien (SPISCan)](readme_cansips_fr.md) est un système de prévision à long terme dont l’objectif est de prévoir l’évolution des conditions climatiques à l’échelle globale. SPISCan est un système d’ensemble multi-modèle (Multi-Model Ensemble [MME]) utilisant CanCM4 et GEM-NEMO, deux modèles climatiques développés au Centre canadien de la modélisation et de l'analyse climatique (CCmaC) et au Centre météorologique canadien (CMC). Ce système de prévision est entièrement couplé atmosphère-océan-glace-sol. SPISCan utilise l’infrastructure d’assimilation en place pour les autres systèmes de prévision afin d’obtenir les conditions initiales de l’atmosphère, de la température de la surface de la mer et de glace marine. Pour plus de détails sur ce système, vous pouvez vous référer à la note technique.

## Les principales composantes de SPISCan

* __Mode assimilation__ : CanCM4 utilise le mode continu comme un cycle d’assimilation pour les variables atmosphériques en 3D, soit la  température, les vents et l’humidité. Les variables océaniques comme la  température de surface de mer et le glace marine sont aussi assimilées par le système. Les données atmosphériques, assimilées, proviennent des analyses globales avec un intervalle temporaire de 6 heures tandis que l’intervalle des données océaniques est un jour. Les analyses des températures d’océan en 3D sont aussi intégrées dans le système SPIScan. Les conditions initiales utilisées par GEM-NEMO proviennent du Système global de prévision d’ensemble (SGPE) qui sont générées a partir de la procédure de Filtre de Kalman d’ensemble (EnKf). Dans cette procédure de filtrage, on applique une procédure du ‘contrôle de la qualité sur un champs d’essai’ sur les observations et on corrige les biais avec  le Système global de prévision déterministe (SGPD). Les analyses du Système global de prévision océan-glace (SGPOG) font partie des données utilisées pour initialiser l’océan et la glace marine. Pour initialiser les champs de surface, le système de prévision de surface (SPS) du SMC  est utilisé. SPS est utilisé dans le mode non-couplé (offline) forcé par les champs atmosphériques provenant des analyses du SMC. 

* __Mode prévision__ : Le système SPIScan est composé de 10 membres d’ensemble provenant de chaque modèle pour un total de 20 membres d’ensemble. Les prévisions mensuelles et les prévisions multi-saisonnières (jusqu’au 12 mois) sont publiées au début de chaque mois.

* __Mode prévisions rétrospectives (hindcast)__ : La climatologie de SPIScan est basée sur un série de prévisions en mode rétrograde (ex. prévisions historiques) couvrant la période de 1981 à 2010. Cette climatologie est très utile pour l’interprétation des prévisions réalistes car les anomalies de prévision en temps réel sont générées à la place des prévisions brutes.   

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Le système SPISCan calcule plusieurs indices climatiques de l'atmosphère et l'océan (ex. les indices de la mousson, du PNA, du NAO, de El Nino, etc.) qui peuvent être calculés à partir des prévisions saisonnières ainsi qu'à partir de l'observation de certaines variables à l'échelle saisonnière. 

Une [description plus détaillée des indices](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_cansips/indices_SPISCAN_f.pdf) est disponible.

Pour accéder aux indices atmosphériques et océaniques calculés par le SPISCan veuillez suivre les liens ci-dessous :

__Prévisions__ :

* [https://dd.weather.gc.ca/ensemble/cansips/csv/indices/forecast/seasonal](https://dd.weather.gc.ca/ensemble/cansips/csv/indices/forecast/seasonal)
* [https://dd.weather.gc.ca/ensemble/cansips/csv/indices/forecast/monthly](https://dd.weather.gc.ca/ensemble/cansips/csv/indices/forecast/monthly)

__Prévisions historiques__ : 

* [https://dd.weather.gc.ca/ensemble/cansips/csv/indices/hindcast/seasonal](https://dd.weather.gc.ca/ensemble/cansips/csv/indices/hindcast/seasonal)
* [https://dd.weather.gc.ca/ensemble/cansips/csv/indices/hindcast/monthly](https://dd.weather.gc.ca/ensemble/cansips/csv/indices/hindcast/monthly)

__Observations__ : 

* [https://dd.weather.gc.ca/ensemble/cansips/csv/indices/observation/seasonal](https://dd.weather.gc.ca/ensemble/cansips/csv/indices/observation/seasonal)
* [https://dd.weather.gc.ca/ensemble/cansips/csv/indices/observation/seasonal](https://dd.weather.gc.ca/ensemble/cansips/csv/indices/observation/monthly)

## Nomenclature des noms de fichiers 

NOTE : TOUTES LES HEURES SONT EN UTC.

La nomenclature des fichiers de prévision est la suivante :

* YYYYMMDD00_indices_month_YYYY1MM1-YYYY2MM2.csv
* YYYYMMDD00_indices_season_YYYY1MM1-YYYY2MM2.csv

Avec:

* __YYYY__ : L'année d'initialisation de la prévision
* __MMDD__ : Le mois et le jour d'initialisation de la prévision
* __YYYY1MM1__ : L'année et mois du début de la prévision
* __YYYY2MM2__ : L'année et mois de la fin de la prévision

La nomenclature des fichiers d'observations est la suivante :

* observed_indices_month_YYYY1MM1-YYYY2MM2.csv

Avec :

* __YYYY1MM1__ : L'année et mois du début du calcul
* __YYYY2MM2__ : L'année et mois de la fin du calcul

Les indices calculés à partir des observations, sont basés sur les anomalies de la température à la surface de la mer, et utilisent l' « optimal interpolation SST dataset » produit par Reynolds et al. en 2002, tandis que les autres indices utilisent les données provenant d'ERA-interim (Dee et al. 2011) comme base de données.

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info.comm.collab.science.gc.ca/).


