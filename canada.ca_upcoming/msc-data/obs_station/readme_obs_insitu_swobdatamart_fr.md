[In English](readme_swob-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données ouvertes publiques du SMC](../readme_fr.md) > Observations par station

# Données XML du langage de balisage des observations météorologiques au sol et marines (SWOB Met-ML) par station

Cette page décrit les données des [observations](readme_obs_insitu_fr.md) météorologiques au sol et marines disponibles en format XML.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le Protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage-overview/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTP. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier XML. Nous vous recommandons d’automatiser le téléchargement en le scriptant avec wget (lien externe, anglais) ou un programme équivalent. Pour plus d’information sur wget, consultez les notes d’utilisation.

Les données sont disponibles aux adresses suivantes:

* __Observations terrestres :__

https://dd.meteo.gc.ca/observations/swob-ml/AAAAMMJJ/XXXX/

où :

* AAAAMMJJ: date des observations, UTC
* XXXX: identificateur de station (identifiant OMM)

De plus, un répertoire spécial contient les dernières observations reçues pour chaque station:

https://dd.meteo.gc.ca/observations/swob-ml/latest/

__Note__: Une [liste des stations d'observations](https://dd.meteo.gc.ca/observations/doc/swob-xml_station_list.csv) est disponible et mise à jour quotidiennement.

* __Observations marines :__

https://dd.meteo.gc.ca/observations/swob-ml/marine/moored-buoys/YYYMMDD/XXXXXXX

où: 

* AAAAMMJJ: date des observations, UTC
* XXXXXXX: identificateur de station (identifiant OMM), peut être 5 ou 7 chiffres

__Note__: Une [liste des stations marines d'observation](https://dd.meteo.gc.ca/observations/doc/swob-xml_marine_station_list.csv) est disponible.

* __Observations des partenaires__ :
  
https://dd.meteo.gc.ca/observations/swob-ml/partners/NETWORK/YYYMMDD/MSC-ID

où: 

* NETWORK: acronyme du réseau des partenaires
* YYYYMMDD: date des observations, UTC
* MSC-ID: identifiant unique des stations des partenaires

__Note__: Une [liste des stations des partenaires](https://dd.meteo.gc.ca/observations/doc/swob-xml_partner_station_list.csv) est disponible

## Nomenclature

NOTE: TOUTES LES HEURES SONT EN UTC.

* __La nomenclature pour les fichiers SWOB est la suivante :__

AAAA-MM-JJ-hhmm-XXXX-TYPE-CCz-swob.xml

où:

- AAAA-MM-JJ-hhmm: date d'observation (UTC)
- XXXX: identificateur de station (identifiant OMM)
- TYPE: AUTO ou MANNED (station automatique ou manuelle) 
- CCz: optionnel. 'Cor' signifie Correction et z est une indication alphabétique du nombre de corrections ('A' signifiant la première, 'B' la seconde, etc.). Par défaut ce champ est absent pour la première observation.
- swob.xml: chaîne de caractères constante indiquant le produit et le format

Dans le répertoire 'latest', les noms des fichiers sont statiques pour chaque station et prend la forme:
 
latest_XXXX_TYPE_swob.xml

où:

- latest: chaîne de caractères constante indiquant que c'est la dernière observation
- XXXX: identificateur de station 
- TYPE:  AUTO ou MANNED (station automatique ou manuelle)
- swob.xml: chaîne de caractères constante indiquant le produit et le format

Exemple:

2013-09-20-1300-CYAZ-MAN-swob.xml 

Ce fichier contient les observations manuelles pour le 20 septembre 2013 à 13:00 UTC pour la station CYAZ (Tofino).

* __La nomenclature pour les fichiers SWOB de données marines est la suivante :__

YYYY-MM-DD-hhmm-XXXXX-TYPE-swob.xml

où:

- YYYY-MM-DD-hhmm: date d'observation (UTC)
- XXXXX: identificateur de station (identifiant OMM), peut être 5 ou 7 chiffres
- TYPE: AUTO - station automatique 
- swob.xml: chaîne de caractères constante indiquant le produit et le format

Exemple:

2019-01-27-0000-4400488-AUTO-swob.xml

* __La nomenclature pour les fichiers SWOB des partenaires est la suivante :__
  
YYYY-MM-DD-hhmm-network-ID-AUTO-swob.xml

où:

- YYYY-MM-DD-hhmm: date d'observation (UTC)
- network: réseau du partenaire
- ID: identifiant unique de station du partenaire 
- swob.xml: chaîne de caractères constante indiquant le produit et le format
  
Exemple:

2018-01-06-1400-bc-env-aq-138-AUTO-swob.xml  

## Note

Une spécification du format de données est disponible dans le [guide des produits SWOB-ML](http://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_station/SWOB-ML_Product_User_Guide_v8.2_f.pdf).

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : ec.dps-client.ec@canada.ca

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).


