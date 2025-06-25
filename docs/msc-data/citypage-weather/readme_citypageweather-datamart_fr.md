[In English](readme_citypageweather-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [Prévisions météorologiques par ville](readme_citypageweather_fr.md) > Prévisions météorologiques par ville sur le Datamart du SMC

# Données XML des prévisions météorologiques par ville

Cette page décrit les données XML des [prévisions météorologiques par ville](readme_citypageweather_fr.md) disponibles sur le Datamart du SMC.

Les fichiers XML sont mis à jour au moins une fois par heure, ou plus souvent dans le cas d'avertissements, d'avis ou de modifications de veille météorologique.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier XML.

Les données de prévision météorologique par ville, distribuées dans des fichiers datés (fichiers uniques) sont disponibles à cette adresse:

  [https://dd.meteo.gc.ca/citypage_weather/{PROV}/{HH}](https://dd.meteo.gc.ca/citypage_weather/)

  où:
  
    * __PROV__ : Code de 2 lettres pour la province ou le territoire couvert par ces prévisions
    * __HH__ : Heure UTC d'émission des prévisions  

  Ce code peut prendre une de ces 13 valeurs :

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

  Note: le répertoire `HEF` contient des données de haute altitude alimentant des bulletins de prévisions saisonnières publiés seulement pour la Colombie-Britannique

## Nomenclature des noms de fichiers 

Les fichiers suivent la nomenclature suivante :

  `{YYYYMMDD}T{HHmmss.sss}Z_MSC_CitypageWeather_{SiteCode}_{L}.xml`

  où :

    * __SiteCode__ : Code de la ville (voir plus bas)
    * __L__ : Lettre indiquant la langue du fichier : fr (français) ou en (anglais)

  Exemples de noms de fichier :

    * 20240815T154059.89Z_MSC_CitypageWeather_s0000011_fr.xml
    * 20240815T154059.89Z_MSC_CitypageWeather_s0000011_en.xml

Une [liste de noms d'emplacements et de codes de sites](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/citypage-weather/site_list_fr.geojson), en format GeoJSON est disponible.


## Balises et schémas XML 

* Une [description des balises et des attributs XML des pages de prévisions météorologiques par ville](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/citypage-weather/citypage_tags_table_f.csv) est disponible.

* Les schémas XML des fichiers de données météorologiques par ville sont disponibles à l'adresse suivante :

  [https://dd.meteo.gc.ca/citypage_weather/schema/](https://dd.meteo.gc.ca/citypage_weather/schema/)

## Icônes du produit XML 

* Les fichiers XML de prévisions météorologiques par ville contiennent des renseignements __codés__ sur les conditions actuelles et prévues. Ces codes définissent l'icône à afficher sur les pages par ville du site Web du bureau des prévisions météorologiques. Vous pouvez consulter la description des conditions météorologiques qui correspond aux codes ici :

     * [Conditions météorologiques actuelles](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/citypage-weather/current_conditions_icon_code_descriptions_f.csv)
     * [Prévisions météorologiques](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/citypage-weather/forecast_conditions_icon_code_descriptions_f.csv)

* Ces icônes sont distribuées sous les [conditions générales standards d'Environnement et Changement climatique Canada](https://www.canada.ca/fr/transparence/avis.html). Pour faire un usage commercial de ces icônes, vous devez obtenir un consentement explicite préalable.

* Vous pouvez également créer vos propres icônes en utilisant les symboles météorologiques mondiaux de l'Organisation météorologique mondiale (OMM). Voir un ensemble complet de symboles météorologiques de l'OMM à cette adresse : [https://github.com/OGCMetOceanDWG/WorldWeatherSymbols](https://github.com/OGCMetOceanDWG/WorldWeatherSymbols)

## Support

Pour toute question relative à ces données, merci de [nous contacter](https://weather.gc.ca/mainmenu/contact_us_f.html).

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).






