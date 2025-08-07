[In English](readme_hrdps-statpostproc-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [SHRPD](readme_hrdps_fr.md) > Post-traitement statistique SHRPD sur le Datamart du SMC


# Données GeoJSON du Système à haute résolution de prévision déterministe (SHRPD) statistiquement post-traitées

Le post-traitement statistique des prévisions des modèles numériques du temps et de l'environnement, incluant le [Système à haute résolution de prévision déterministe (SHRPD)](readme_hrdps_fr.md), permet de réduire les biais systématiques et la variance de l'erreur des prévisions brutes. Pour ce faire, des relations statistiques optimisées entre les observations enregistrées aux stations et les sorties des modèles numériques aux points de grilles à proximité sont établies. 

Le système **PROGNOS** est un progiciel développé par Environnement et Changement climatique Canada permettant cela. Les relations sont bâties par l'entremise de la méthode "Model Output Statistics" (MOS) et par régression linéaire multiple (RLM).

À l'heure actuelle, seule la température de l'air à 1.5 mètres au-dessus de la surface de la Terre est post-traitée statistiquement.

L'absence de prévisions statistiquement post-traitées peut être dûe à l'indisponibilité d'un modèle statistique causé par une qualité ou quantité insuffisantes d'observations. 

La région géographique couverte par ces données inclut le territoire couvert par les stations météorologiques du Canada et quelques bouées américaines. 

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier GeoJSON.

Les données sont accessibles à l’adresse suivante : 

* [https://dd.meteo.gc.ca/today/model_hrdps/stat-post-processing/{HH}/{hhh}/](https://dd.meteo.gc.ca/today/model_hrdps/stat-post-processing)

où :

* __HH__ : Heure UTC du début de la passe du modèle [00, 06, 12, 18]
* __hhh__ : Heure de prévision [000, 001, 002, ..., 048] selon les stations d'observations

## Spécifications techniques

* Les prévisions PROGNOS sont offertes aux stations d’observation situées en Amérique du Nord à l’intérieur des limites géographiques suivantes : 149⁰W, 40⁰N, 42⁰W, 88⁰N
* Le datum et la projection géographique sont les suivantes: WGS84, latlon
* Les données sont bilingues
* Les données sont conformes aux normes ISO8601.

## Nomenclature des noms de fichiers 

Les fichiers ont la nomenclature suivante :

`{YYYYMMDD}T{HH}Z_MSC_HRDPS-{PRODUCT}-{METHOD}_{Var}_{LVLTYPE}-{LVL}_PT{hhh}H.json`

où :

* __YYYYMMDD__ : Année, mois et jour du début de l'émission de la prévision
* __T__ : Délimiteur temporel selon les normes ISO8601
* __HH__ : Heure d’émission des prévisions du modèle numérique en UTC [00, 12]
* __Z__ : Fuseau horaire (heure UTC)
* __MSC__ : Chaîne de caractères constante pour Meteorological Service of Canada, la source des données
* __HRDPS__ : Chaîne de caractères constante indiquant des données post-traitées à partir du Système à haute résolution de prévision déterministe
* __PRODUCT__ : Chaîne de caractères constante indiquant le produit de post-traitement statistique [PROGNOS]
* __METHOD__ : Chaîne de caractères constante indiquant la méthode statistique utilisée [MLR pour Multiple Linear Regression]
* __Var__ : Variables contenues dans le fichier [AirTemp]
* __LVLTYPE__ : Type de niveau vertical [Sfc pour la surface, AGL pour le niveau au-dessus du sol (Above Ground Level)]
* __LVL__ : Valeur du niveau vertical [1.5m]. Ce paramètre est absent pour la surface
* __PT{hhh}H__ : Echéance temporelle selon la norme [ISO8601](https://en.wikipedia.org/wiki/ISO_8601). P, T et H sont des caractères constants désignant Période, Temps et Heure. "hhh" représente l’heure d'échéance de la prévision [000, 001, 002, ..., 048] selon les stations d'observations 
* __json__ : Chaîne de caractères constante indiquant que le format est GeoJSON

Exemple de nom de fichier: 

* 20250703T06Z_MSC_HRDPS-PROGNOS-_AirTemp_AGL-1.5m_PT024H.json

## Liste des variables

* AirTemp: Température de l'air du thermomètre sec à la surface (K)

## Support

Pour toutes questions relative à ces données, merci de [nous contacter](https://meteo.gc.ca/mainmenu/contact_us_f.html).

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).
