[In English](readme_obs_insitu_xmldatamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données ouvertes publiques du SMC](../readme_fr.md) > Sommaires d'observations

# Données XML des sommaires d'observations par province ou territoire

Cette page décrit les données d'[observations](readme_obs_insitu_fr.md) disponibles en format XML.

Les fichiers des sommaires d'observations contiennent les observations de toutes les stations météorologiques du Canada disponibles, regroupées par province ou territoire. Les données sont obtenues de plusieurs manières et peuvent ne pas avoir subi de contrôle de qualité.

Les fichiers sont dans le format XML et suivent un schéma défini par Environnement et Changement climatique Canada.

Il y a 6 types de fichiers pour chaque province ou territoire:

* Sommaire horaire en anglais et en français;
* Sommaire de la journée courante en anglais et en français;
* Sommaire d'hier en anglais et en français.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le Protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTP. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier XML. Nous vous recommandons d’automatiser le téléchargement en le scriptant avec wget (lien externe, anglais) ou un programme équivalent. Pour plus d’information sur wget, consultez les notes d’utilisation.

Les fichiers XML du sommaire des observations des provinces ou des territoires sont regroupés dans une structure de répertoires basée sur la province/territoire et le type de sommaire.

Les données sont disponibles à cette adresse:

https://dd.weather.gc.ca/observations/xml/PC/TYPE

où:
* **PC**: code de 2 lettres pour la province ou le territoire couvert par ces observations. Ce code peut prendre une de ces 13 valeurs:

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

* __TYPE__ : chaîne de caractères indiquant le type de sommaire. Peut prendre l'une de ces 3 valeurs [hourly | today | yesterday]. Voir ci-dessous pour une description de chaque type.

Un historique des données (30 jours) est conservé dans ce répertoire.

## Nomenclature

NOTE: TOUTES LES HEURES SONT EN UTC.

Les noms de fichiers suivant cette nomenclature:

TYPE_PC_YYYYMMDD_L.xml

où:

* TYPE:  chaîne de caractères indiquant le type de sommaire. Peut prendre l'une de ces 3 valeurs [hourly | today | yesterday]. Voir ci-dessous pour une description de chaque type.
* PC: code de 2 lettres pour la indiquant la province ou le territoire couvert par ces observations. Voir ci-dessus pour les valeurs possibles.
* YYYYMMDDHH: Date des observations. L'heure représentée par 'HH' n'est présente que dans le cas des fichiers horaires ('hourly').
* L: 1 lettre indiquant la langue du fichier. Peut-être une de ces valeurs:
    * f (français)
    * e (anglais)

Exemples de nom de fichier :

* hourly_ab_2010030517_e.xml
* today_mb_20100306_e.xml
* yesterday_qc_20100306_f.xml

## Description

__1- Sommaire horaire ('hourly')__

Le sommaire horaire contient les observations les plus récentes qui sont disponibles.

Ce fichier est créé aux minutes 8, 11, 14, 25, 35 et 50, après 'heure. Le fichier du sommaire horaire est écrasé par une nouvelle ersion à chaque fois qu'un nouveau est créé pendant cette heure. Celui ui demeure sur le serveur a été le dernier créé dans l'heure inscrite ans le nom de fichier, soit celui à 50 minutes. Chaque fichier horaire st par la suite conservé pour 30 jours sur le serveur.

Lorsque les données sont manquantes, les observations de la dernière heure sont utilisées. Les champs horaires sont laissés vides s'il n'y a eu aucune mise à jour durant 2 heures 15 minutes.                                                                                                
Ces données d'observations font l'objet d'un contrôle de qualité. Toute valeur qui ne passe pas pas le contrôle de qualité est supprimée.  Ceci inclus les valeurs qui sont catégorisées comme douteuses. 

Ce fichier contient pour la province ou le territoire:

* L'endroit et la température la plus froide au Canada pour cette heure;
* L'endroit et la température la plus chaude au Canada pour cette heure;
* L'endroit et la température la plus froide dans la province ou le territoire pour cette heure;
* L'endroit et la température la plus chaude dans la province pour le territoire pour cette heure;
* Les observations et les records des stations disponibles dans cette province:
    * Condition présente (expression)
    * Pression au niveau de la mer (kPa)
    * Valeur de la tendance de pression (kPa)
    * Tendance de pression (à la hausse, à la baisse, ou stable)
    * Visibilité (km)
    * Température de l'air (°C)
    * Point de rosée (°C)
    * Humidité relative (%)
    * Vitesse du vent (km/h)
    * Direction du vent (code)
    * Vitesse de rafale (km/h)
    * Couverture nuageuse
    * Refroidissement éolien
    * Humidex

__2- Sommaire pour aujourd'hui ('today')__

Le sommaire pour aujourd'hui est produit aux minutes 8, 11, 14, 25, 35 et 50 après chaque heure. Le fichier est écrasé par la nouvelle version jusqu'à ce que le dernier fichier soir créé. Le dernier demeurant sur le serveur est celui créé pendant le jour inscrit dans le nom de fichier. 

Pour chaque jour, le dernier fichier créé est conservé pour les 30 prochains jours.

Selon la période de la journée, les données sont obtenues soit à partir des données horaires, soit à partir des données synoptiques. Si obtenu à partir des données horaires, un contrôle de qualité est appliqué. Si obtenu à partir des données synoptiques, aucun contrôle de qualité n'est appliqué. 

Par exemple, le 9 mars à 14:40 UTC, le fichier pour les observations d'aujourd'hui contiendrait les observations débutant le 9 mars à 06 UTC et terminant à 14:40 UTC.

Le sommaire pour aujourd'hui commence à accumuler les max/min pour chaque station au début de la journée climatologique (06 UTC). Comme à 06Z de chaque jour un nouveau fichier est créé, les min/max de ce fichier sont réinitialisés et, pendant les heures suivantes, les données sont accumulées pour générer les min/max pour cette journée climatique.                                          

Comme certaines stations ne rapportent que pendant certaines heures de la journée, les valeurs pour ces stations sont parfois vides au début de la journée climatique. 

Ce fichier contient pour la province ou le territoire:
* L'endroit et la température la plus froide au Canada jusqu'à maintenant pour ce jour climatique;
* L'endroit et la température la plus chaude au Canada jusqu'à maintenant pour ce jour climatique;
* L'endroit et la température la plus froide dans la province ou le territoire jusqu'à maintenant pour ce jour climatique;
* L'endroit et la température la plus chaude dans la province ou le territoire le territoire jusqu'à maintenant pour ce jour climatique;
* Les observations des stations disponibles dans cette province ou ce territoire. Les observations contiennent pour chaque station:
    * Température de l'air maximale pour aujourd'hui (°C)
    * Température de l'air minimale pour aujourd'hui (°C)
    * Direction du vent (code)
    * Vitesse de rafale (km/h)
    * Température de l'air maximale record (°C)
    * Année du record pour la température de l'air maximale
    * Température de l'air minimale record (°C)
    * Année du record pour la température de l'air minimale
    * Précipitation record de pluie (mm)
    * Année de la précipitation record de pluie
    * Précipitation record de neige (cm)
    * Année de la précipitation record de neige
    * Année à partir de laquelle la station à des données de température
    * Année à partir de laquelle la station à des données de précipitation

__3- Sommaire pour hier ('yesterday')__

Les observations pour la journée d'hier sont définies comme celles faites pendant la dernière journée climatique complète, soit de 06 UTC à 06 UTC.

Ce produit est basé sur les bulletins syoptiques à 06h UTC produits pour chaque station. Ces données ne subissent pas de contrôle de qualité. 

Veuillez alors consulter les [jeux de données climatologiques officiels](http://climat.meteo.gc.ca/index_f.html).

Certaines stations ont des observations mais n'ont pas de bulletins SYNO. Ces stations seront incluses dans les sommaires horaires ('hourly') et les sommaires pour la journée d'aujourd'hui ('today') mais pas dans ceux de la journée d'hier ('yesterday')

Le sommaire de la journée d'hier est produit aux minutes 8, 11, 14, 25, 35 et 50 après chaque heure. Le fichier est écrasé par la nouvelle version jusqu'à ce que le dernier fichier soir créé. Le dernier demeurant sur le serveur est le dernier créé pendant le jour inscrit dans le nom de fichier. Pour chaque jour, le dernier fichier créé est conservé pour les 30 prochains jours.

* L'endroit et la température la plus froide au Canada pour la journée climatique d'hier; 
* L'endroit et la température la plus chaude au Canada pour la journée climatique d'hier;
* L'endroit et la température la plus froide dans la province ou le territoire pour la journée climatique d'hier;
* L'endroit et la température la plus chaude dans la province ou dans le territoire pour la journée climatique d'hier;
* Les observations des stations disponibles dans cette province ou ce territoire pour la journée climatique d'hier. Les observations contiennent pour chaque station:
    * Température de l'air maximale (°C)
    * Température de l'air minimale (°C)
    * Direction du vent maximal (code)
    * Vitesse de vent maximale (km/h) (certaines stations seulement)
    * Température de l'air maximale record (°C)
    * Année du record pour la température de l'air maximale
    * Température de l'air minimale record (°C)
    * Année du record pour la température de l'air minimale
    * Précipitation record de pluie (mm)
    * Année de la précipitation record de pluie
    * Précipitation record de neige (cm)
    * Année de la précipitation record de neige
    * Année à partir de laquelle la station à des données de température
    * Année à partir de laquelle la station à des données de précipitation

### Stations

Pour chaque station, les informations suivantes sont inscrites:

* Nom de la station
* Latitude (degré décimal)
* Longitude (degré décimal)
* Numéro d'identification de Transport Canada
* Les heures des observations sont en temps UTC et en heure locale
* Numéro de station climatique
* Numéro de station OMM

Il y a plus de 500 stations d'observation au Canada. Cependant, ce nombre est en constante évolution. Les stations sont présentes dans les fichiers seulement si des données d'observations sont disponibles.

## Notes

* Une [documentation complète pour la description XML de point d'observation météorologique](http://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_station/Met-ML-SchemaDescriptionV2_f.pdf) est disponible. 
* Pour qu'un record soit affiché, il doit y avoir au moins 15 années de données dans la base de données des archives climatiques tel que  mentionné sur leur site: http://www.climate.weatheroffice.gc.ca/Welcome_f.html
* Les métadonnées des stations sont fournies en anglais ou en français.
* Toute valeur inférieure à 0,05 est arrondie à 0,0
* Toute valeur entre 0,05 et 0,1 est arrondie à 0,1
* La date de création est inscrite dans l'en-tête de chaque fichier
* Le standard ISO 8601 est utilisé pour toutes les dates et les heures
* Toutes les dates et les heures sont données en heure UTC et locale
* Les données historiques (les records) ont toutes subi un contrôle de qualité.

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : ec.dps-client.ec@canada.ca

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).


