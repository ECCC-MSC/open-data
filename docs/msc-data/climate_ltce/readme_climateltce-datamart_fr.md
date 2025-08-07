[En Anglais](readme_climateltce-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [ECLT](readme_climateltce_fr.md) > Records des Extrêmes Quotidiens sur le Datamart du SMC

# Extrêmes climatiques quotidiens à long terme au format CSV

Cette page décrit les données d'[extrêmes climatiques quotidiennes (Extrêmes climatiques à long terme)](readme_climateltce_fr.md) au format CSV. Veuillez noter que ces données ne doivent pas être utilisées pour répondre à des questions sur les tendances climatiques. Pour ces analyses, veuillez consulter les [Données climatiques canadiennes ajustées et homogénéisées](../climate_ahccd/readme_ahccd_fr.md).

## Localisation des données

Les données du Datamart du SMC peuvent être [récupérées automatiquement avec le protocole AMQP (Advanced Message Queuing Protocol)](../../msc-datamart/amqp_en.md) dès qu'elles sont disponibles. Un [aperçu et exemples d'accès et d'utilisation des données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d'y accéder avec un navigateur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier CSV.

Les données sont accessibles aux URL suivantes :

* [https://dd.meteo.gc.ca/today/climate/ltce/daily/{Variable}/{PROVINCE}](https://dd.meteo.gc.ca/today/climate/ltce/daily)
* [https://dd.meteo.gc.ca/today/climate/ltce/stations](https://dd.meteo.gc.ca/today/climate/ltce/stations)

où :

* __Variable__ : Prend l'une des valeurs [Temperature, Precipitation, Snowfall]
* __PROVINCE__ : Chaîne de caractères de deux lettres identifiant la province dans laquelle se trouve la station [ex : AB, BC, MB, etc.]

## Nomenclature des noms de fichiers 

Les noms de fichiers ont la forme suivante :

* `climate_LTCE_{Variable}-Records_{PROVINCE}_{STATION-ID}.csv`

Les listes de stations virtuelles ont la forme suivante

* `climate_LTCE_{Variable}_Virtual-Stations.csv`

où :

* __climate__ : Chaîne de caractères constante indiquant l'ensemble de données climatiques
* __LTCE__ : Chaîne de caractères constante indiquant le nom de l'ensemble de données sur les extrêmes climatiques à long terme
* __Variable__ : Nom de la variable disponible dans le fichier, prenant l'une des valeurs suivantes : [Temperature, Precipitation, Snowfall]
* __Records__ : Chaîne de caractères constante indiquant que les données sont des records d'extrêmes quotidiens
* __PROVINCE__ : Chaîne de caractères de deux lettres identifiant la province dans laquelle se trouve la station, prenant l'une des valeurs suivantes : [AB, BC, MB, NB, NL, NS, NT, NU, ON, PE, QC, SK, YT]
* __STATION-ID__ : Identifiant unique de la station concernée
* __Virtual-Stations__ : Chaîne de caractères constante indiquant que le fichier est une liste de stations virtuelles
* __csv__ : Chaîne de caractères constante indiquant le format CSV

Exemples :

* climate_LTCE_Precipitation-Records_ON_VSON104.csv
* climate_LTCE_Temperature_Virtual-Stations.csv

## Liste des variables

Les variables et unités disponibles pour les records des extrêmes quotidiens (Extrêmes climatiques à long terme) sont les suivantes :

* High Max Temp : Température journalière la plus élevée (°C)
* High Min Temp : Température minimale quotidienne la plus élevée (°C)
* Low Max Temp : Température quotidienne maximale la plus froide (°C)
* Low Min Temp: Température quotidienne la plus froide (°C)
* Precipitation : Précipitations maximales quotidiennes (mm)
* Snowfall : Chute de neige journalière maximale (cm)

## Support

Si vous avez des questions concernant ces données, veuillez [nous contacter](mailto:info.cccs-ccsc@canada.ca).

## Annonces de la liste de diffusion dd_info 

Les annonces relatives à ce jeu de données sont disponibles sur la [liste dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).
