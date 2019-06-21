[In English](readme_citypageweather-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données ouvertes publiques du SMC](../readme_fr.md) > Prévisions météorologiques par ville sur le Datamart du SMC

# Données XML des prévisions météorologiques par ville

Cette page décrit les données XML des [prévisions météorologiques par ville](readme_citypageweather_fr.md).

Les fichiers XML sont mis à jour au moins une fois par heure, ou plus
souvent dans le cas d'avertissements, d'avis ou de modifications de veille
météorologique.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le Protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage-overview/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTP. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier XML.

Les données sont accessibles à adresse suivante :

* https://dd.meteo.gc.ca/citypage_weather/xml/

## Nomenclature des noms de fichiers 

NOTE: TOUTES LES HEURES SONT EN UTC.

Les fichiers XML de prévisions météorologiques par ville sont organisés
dans une arborescence en fonction de la province, du territoire ou des
prévisions en haute altitude.

1- Les dossiers ont un nom de la forme:

 /citypage_weather/xml/XX

où :

* __XX__ :  code de 2 lettres pour la province ou le territoire couvert par ces
observations. 
Ce code peut prendre une de ces 13 valeurs:

* AB (Alberta)
* BC (Colombie-Britannique)
* MB (Manitoba)
* NB (Nouveau-Brunswick)
* NL (Terre-Neuve-et-Labrador)
* NS (Nouvelle-Écosse)
* NT (Territoires du Nord-Ouest)
* NU (Nunavut)
* ON (Ontario)
* PE (Île-du-Prince-Édouard)
* QC (Québec)
* SK (Saskatchewan)
* YT (Yukon)

De plus, le dossier /citypage_weather/xml/HEF contient les prévisions en
haute altitude. Il s'agit de bulletins de prévisions saisonnières publiés
seulement pour la Colombie-Britannique.

2- Les fichiers ont un nom de la forme :

CodeDeSite_L.xml

où:

* __CodeDeSite__ : code de la ville ( voir l'URL plus bas )
* __L__ : lettre indiquant la langue du fichier : f (français) ou e (anglais).

Exemple de nom de fichier :
* s0000001_e.xml - fichier XML de prévisions météorologiques pour
Athabasca, en anglais
* s0000001_f.xml - fichier XML de prévisions météorologiques pour
Athabasca, en français

Des listes de noms d'emplacements et de codes de sites, groupés selon
diverses valeurs, sont disponibles ici :
* [Codes de sites](site_list_fr.csv)
* [Liste des provinces](site_list_provinces_fr.csv)
* [Nom des villes](site_list_towns_fr.csv)

## Balises, schémas XML et icônes

Vous pouvez consulter [la description des balises et des attributs XML des
pages de prévisions météorologiques par ville](tags_table_f.csv).

Les schémas XML des fichiers de données météorologiques par ville sont
disponibles à l'adresse :
https://dd.meteo.gc.ca/citypage_weather/schema/

Les fichiers XML de prévisions météorologiques par ville contiennent des
renseignements CODÉS sur les conditions actuelles et prévues. Ces codes
définissent l'icône à afficher sur les pages par ville du site Web du
bureau des prévisions météorologiques. Vous pouvez consulter la
description des conditions météorologiques qui correspond aux codes ici :
* [Conditions météorologiques actuelles](current_conditions_icon_code_descriptions_f.csv)
* [Prévisions météorologiques](forecast_conditions_icon_code_descriptions_f.csv)

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : ec.dps-client.ec@canada.ca

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).






