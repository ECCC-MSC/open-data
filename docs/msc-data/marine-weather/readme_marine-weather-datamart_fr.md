[In English](readme_marine-weather-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [Prévisions météorologiques marines](readme_marine-weather_fr.md) > Prévisions météorologiques marines sur le Datamart du SMC

# Données des prévisions météorologiques marines

Cette page décrit les données des [prévisions météorologiques marines](readme_marine-weather_fr.md) disponibles sur le Datamart du SMC.

Les fichiers XML contiennent la prévision des conditions, les alertes météorlogiques marines (avertissement et veille), les alertes de glace et l'annonce de la fin de la saison. Ils sont mis à jour de deux à quatre fois par jour, ou plus souvent dans le cas d'émission d'amendements, d'alertes météorologiques marines (alerte ou veille) ou d'avertissements de glace.

Le [guide des prévisions météorologiques marines](https://www.canada.ca/fr/environnement-changement-climatique/services/renseignements-generaux-conditions-maritimes/publications/guide-previsions.html) d'Environnement et Changement climatique Canada fournit des renseignements sur les bulletins de prévisions: heure d'émission de la prévision, période de temps couverte par la prévision, régions, terminologie relative à la période de prévision, renseignements fournis dans la prévision et révision des prévisions.

__Notes__: 

* Les fichiers XML n'incluent pas l'information sur les prévisions de glace, mais incluent l'information sur les [avertissements de glace](https://www.canada.ca/fr/environnement-changement-climatique/services/previsions-observations-glaces/conditions-glaces-plus-recentes/guide-produits/apercu-bulletin-icebergs.html#averts).

* Les prévisions de glace peuvent être trouvées sur le [site web d'Environnement et Changement climatique Canada](https://www.canada.ca/fr/environnement-changement-climatique/services/previsions-observations-glaces.html) ou sur le site du [Service canadien des glaces](https://www.canada.ca/fr/environnement-changement-climatique/services/previsions-observations-glaces/conditions-glaces-plus-recentes.html).

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier XML.

Les données de prévisions météorologiques marines, distribuées dans des fichiers datés (fichiers uniques) sont disponibles à cette adresse:

  [https://dd.meteo.gc.ca/marine_weather/{DOMAIN}/{HH}](https://dd.meteo.gc.ca/marine_weather/)

  où:
  
    * __DOMAIN__ : Nom du domaine couvert par la prévision marine
    * __HH__ : Heure UTC d'émission des prévisions  

  Ce domaine peut prendre une de ces 8 valeurs :

    * arctic
    * atlantic
    * great_lakes
    * hudson
    * mackenzie
    * pacific
    * prairies
    * st_lawrence

Une [__description des balises et des attributs XML__](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/marine-weather/marine_tags_table_f.csv) des pages de prévisions météorologiques marines est disponible.

Les __schémas XML__ des fichiers de données météorologiques marines sont également disponibles à l'adresse suivante :

https://dd.meteo.gc.ca/today/marine_weather/schema/

## Nomenclature des noms de fichiers

Les fichiers ont la nomenclature suivante:

  `{YYYYMMDD}T{HHmmss.sss}Z_MSC_MarineWeather_{SiteCode}_{L}.xml`

  où :

    * __SiteCode__ : Code de la région marine (voir plus bas)
    * __L__ : Lettre indiquant la langue du fichier : fr (français) ou en (anglais)

  Exemples de noms de fichier :

    * 20250219T070026.074Z_MSC_MarineWeather_m0000109_en.xml
    * 20250219T070026.074Z_MSC_MarineWeather_m0000109_fr.xml

Une [__liste de noms d'emplacements et de codes de sites__](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/marine-weather/marine_region_list_fr.csv) est disponible.

## Support

Pour toute question relative à ces données, merci de [nous contacter](https://weather.gc.ca/mainmenu/contact_us_f.html).

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).
























