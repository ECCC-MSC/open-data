[In English](readme_rdps-statpostproc-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [SRPD](readme_rdps_fr.md) > Post-traitement statistique SRPD sur le Datamart du SMC


# Données GeoJSON du Système régional de prévision déterministe statistiquement post-traitées

Le système Updatable Model Output Statistics (UMOS) est un progiciel développé par Environnement et Changement climatique Canada permettant de post-traiter les prévisions brutes des modèles numériques du temps et de l'environnement, incluant le [Système régional de prévision déterministe (SRPD)](../readme_rdps_fr.md), en établissant des relations statistiques optimisées entre les observations enregistrées aux stations et les sorties de modèles numériques. Ces relations sont bâties par l'entremise de la méthode Model Output Statistics (MOS) et par régression linéaire multiple (RLM). Les variables du temps et de l'environnement post-traitées statistiquement incluent la température de l'air et le point de rosée à 1.5 mètres au-dessus de la surface de la terre ou de l'eau ainsi que la vitesse et la direction du vent à 10 mètres au-dessus de la surface de la terre ou de l'eau. La région géographique couverte par ces données inclut le territoire couvert par les stations météorologiques du Canada et quelques bouées américaines. Les prévisions issues du post-traitement statistique sont disponibles à la même fréquence d'émission et au même pas de temps que les modèles numériques produisant les prévisions brutes.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier GeoJSON.

Les données sont accessibles à l’adresse suivante : 

[https://dd.meteo.gc.ca/model_gem_regional/stat-post-processing/{HH}/{hhh}/](https://dd.meteo.gc.ca/model_gem_regional/stat-post-processing)

où :

* __HH__ : Heure UTC du début de la passe du modèle [00, 06, 12, 18]
* __hhh__ : Heure de prévision [000, 003, 006, ..., 084] 

Un historique de 24 heures est conservé dans ce répertoire.

## Spécifications techniques

* Les prévisions UMOS sont offertes aux stations d’observation situées en Amérique du Nord à l’intérieur de délimitations géographiques suivantes : 141⁰W, 40⁰N, 42⁰W, 88⁰N
* Le datum et la projection géographique sont les suivantes: WGS84, latlon
* Les données sont bilingues
* Les donnees sont conformes aux normes ISO8601.

## Nomenclature des noms de fichiers 

NOTE: TOUTES LES HEURES SONT EN UTC.

Les fichiers ont la nomenclature suivante :

`{YYYYMMDD}T{HH}Z_MSC_RDPS-{PRODUCT}-{METHOD}_{Var}_{LVLTYPE}-{LVL}_PT{hhh}H.json`

où :

* __YYYYMMDD__ : Année, mois et jour du début de la prévision
* __T__ : Délimiteur temporel selon les normes ISO8601
* __HH__ : Heure UTC de la passe [00, 06, 12, 18]
* __Z__ : Fuseau horaire (heure UTC)
* __MSC__ : Chaîne de caractères constante pour Meteorological Service of Canada, la source des données
* __RDPS__ : Chaîne de caractères constante indiquant des données post-traitées à partir du Système régional de prévision déterministe
* __PRODUCT__ : Chaîne de caractères constante indiquant le produit de post-traitement statistique [UMOS]
* __METHOD__ : Chaîne de caractères constante indiquant la méthode statistique utilisée [MLR pour Multiple Linear Regression]
* __Var__ : Variables contenues dans le fichier [AirTemp, Dewpoint, WindSpeed, WindDir]
* __LVLTYPE__ : Type de niveau vertical [Sfc pour la surface, AGL pour le niveau au-dessus du sol (Above Ground Level)]
* __LVL__ : Valeur du niveau vertical [1.5m, 10m]. Ce paramètre est absent pour la surface
* __PT{hhh}H__ : Echéance temporelle selon la norme [ISO8601](https://en.wikipedia.org/wiki/ISO_8601). P, T et H sont des caractères constants désignant Période, Temps et Heure. "hhh" représente l’heure de prévision  [000, 003, 006, ..., 084]
* __json__ : Chaîne de caractères constante indiquant que le format est GeoJSON

Exemple de nom de fichier: 20220128T00Z_MSC_RDPS-UMOS-MLR_AirTemp_AGL-1.5m_PT072H.json

## Liste des variables

* AirTemp: Température de l'air du thermomètre sec à la surface (K)
* Dewpoint: Température du point de rosée à la surface (K)
* WindSpeed: Vitesse du vent à la surface (km/h)
* WindDir: Direction du vent à la surface (°)

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).
