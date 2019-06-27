[In English](readme_marineweather-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données ouvertes publiques du SMC](../readme_fr.md) > Prévisions météorologiques maritimes sur le Datamart du SMC

# Données des prévisions météorologiques maritimes

Cette page décrit les données des [prévisions météorologiques maritimes](readme_marineweather_fr.md).

Les fichiers XML sont mis à jour de deux à quatre fois par jour, ou plus
souvent dans le cas d'émission d'amendements, d'alertes météorologiques
marines (alerte ou veille) ou d'avertissements de glace.

Le guide des prévisions météorologiques marines
d'Environnement et Changement Climatiques Canada fournit des renseignements sur les bulletins de prévisions :
heure d'émission de la prévision, période de temps couverte par la
prévision, régions, terminologie relative àla période de prévision,
renseignements fournis dans la prévision et révision des prévisions.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le Protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage-overview/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTP. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier XML.

Les fichiers XML de prévisions météorologiques marines sont
disponibles à l'adresse :

* https://dd.meteo.gc.ca/marine_weather/xml/


## Nomenclature des répertoires et noms de fichiers

NOTE: TOUTES LES HEURES SONT EN UTC.

Les fichiers XML de prévisions météorologiques marines sont organisés
dans une arborescence en fonction des régions de prévisions marines du Canada.

__1- Les dossiers ont un nom de la forme :__

 /marine_weather/xml/REGION

où :
* __REGION__ : nom de a région couverte par la prévision marine. Cette région peut
 prendre une de ces 8 valeurs:
    * arctic
    * atlantic
    * great_lakes
    * hudson
    * mackenzie
    * pacific
    * prairies
    * st_lawrence

__2- Les fichiers ont la nomenclature suivante :__

CodeDeSite_L.xml

où:
* __CodeDeSite__ : code du site pour la région marine ( voir l'URL plus bas )
* __L__ : lettre indiquant la langue du fichier : f (français) ou e (anglais).

Exemple de nom de fichier :

* m0000001_e.xml - fichier XML de prévision météorologique marine pour
Tuktoyaktuk, en anglais

* m0000001_f.xml - fichier XML de prévision météorologique marine pour
Tuktoyaktuk, en français

Des listes de noms d'emplacements et de codes de sites, groupés selon
diverses valeurs, sont disponibles aux adresses suivantes :

* https://dd.meteo.gc.ca/marine_weather/docs/region_list_fr.csv
* https://dd.meteo.gc.ca/marine_weather/docs/region_list_regions_fr.csv
* https://dd.meteo.gc.ca/marine_weather/docs/region_list_areas_fr.csv

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : ec.dps-client.ec@canada.ca

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).
























