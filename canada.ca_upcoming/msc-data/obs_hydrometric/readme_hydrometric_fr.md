[In English](readme_hydrometric_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données ouvertes publiques du SMC](../readme_fr.md) > Données hydrométriques

# Données et produits hydrométriques en temps réel

## Description du système

### Fichier de données

Les données hydrométriques en temps réel sont présentées dans un format CSV 
pour la distribution par Environnement et Changement climatique Canada.

Les fichiers mis à jour sur une base horaire contiennent les 2 derniers jours 
complets en plus du jour courant incomplet. Les fichiers mis à jour sur une 
base quotidienne contiennent les 30 derniers jours complets en plus du jour 
courant incomplet.

La première ligne est une entête bilingue suivie des enregistrements. Voici la 
description des titres français des colonnes : 

ID,Date,Niveau d'eau (m),Grade,Symbole,QA/QC,Débit (cms),Grade,Symbole,QA/QC

où : 
*  __ID__ : identifiant de la station. Les deux premiers chiffres indiquent le 
        bassin hydrographique principal dans lequel se trouve la station. Les 
        deux prochains caractères indiquent le sous-bassin et le 
        sous-sous-bassin. Les trois derniers chiffres indiquent la station 
        spécifique dans le sous-sous-bassin.

* __Date__ : date de l'observation au format ISO 8601, heure normale locale (HNL)

* __Niveau d'eau (m)__ : Niveau d'eau en mètres

* __Grade__ : usage futur

* __Symbole__ : usage futur

* __QA/QC__ : drapeau de l'assurance de la qualité/contrôle de la qualité pour le 
          niveau d'eau (1 = préliminaire, 2 = révisé, 3 = vérifié, 
          4 = approuvé)

* __Débit (cms)__ : débit en mètres cube par seconde

* __Grade__ : usage futur

* __Symbol__ : usage futur

* __QA/QC__ : drapeau de l'assurance de la qualité/contrôle de la qualité pour le 
          débit (1 = préliminaire, 2 = révisé, 3 = vérifié, 4 = approuvé)

Veuillez prendre note que les dates des données sont toujours en HNL à chaque 
station. Les dates affichent l'écart avec le temps universel coordonné (UTC).


### Liste des stations

La liste des stations hydrométriques en temps réel est disponible ici :

https://dd.meteo.gc.ca/hydrometric/doc/hydrometric_StationList.csv

La première ligne est une entête bilingue suivie des métadonnées des stations. 
Voici la description des titres français des colonnes : 

ID,Nom,Latitude,Longitude,Prov/Terr,Timezone

où :
*  __ID__ : identifiant de la station

* __Nom__ : nom de la station. Le nom est soit en anglais ou en français 
       dépendamment de l'emplacement de la station

* __Latitude__ : latitude en format décimal

* __Longitude__ : longitude en format décimal

* __Prov/Terr__ : code de la province ou du territoire à 2 lettres

* __Fuseau horaire__ : différence entre HNL et UTC

## Accès

### Comment accéder aux données

Ces données sont respectivement disponibles sur les services serveur de données [Datamart du SMC](../../msc-datamart/readme_fr.md) et les services web [GeoMet du SMC](../../msc-geomet/readme_fr.md) :

* [Données CSV disponibles sur le Datamart du SMC](readme_hydrometric-datamart_fr.md) 
* Lien vers la sous-page du jeu de données pour GeoMet [exemple](../../msc-geomet/giops_fr.md), si la sous-page existe. 
	* NOTE: n'existe pas pour le SGPD

Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage-overview/readme_fr.md) est disponible.

### Licence

La [Licence d’utilisation finale pour les serveurs de données d’Environnement et Changement climatique Canada](../../licence/readme_fr.md) précise les conditions d'utilisation de ces données.

### Métadonnées

* Les [métadonnées en application de données hydrométriques en temps réel  sont accessibles sur le portail du gouvernement ouvert](https://ouvert.canada.ca/data/fr/dataset/ef2161a8-b01d-4dfb-ad00-1a70f7c4073b)

## Documentation technique

* [Relevés hydrologiques du Canada](https://www.canada.ca/fr/environnement-changement-climatique/services/eau-apercu/volume/surveillance/releves.html)
* [Données de niveau d'eau et de débit en temps réel et historiques](http://eau.ec.gc.ca/)

## Registre des changements 

_Ne s'applique pas._



