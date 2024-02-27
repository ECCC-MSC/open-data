[In English](readme_climateobs-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [Données climatiques (normales, données quotidiennes et horaires, sommaires mensuels)](readme_climateobs_fr.md) > Données climatiques (normales, données quotidiennes et horaires, sommaires mensuels) sur le Datamart du SMC

# Données climatiques (normales, données quotidiennes et horaires, sommaires mensuels) en format CSV

Ce document décrit les quatre jeux de données climatiques, normales climatiques, observations quotidiennes et horaires ainsi que les sommaires mensuels disponibles, en format CSV.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données climatiques sont disponibles via le protocole HTTPS. Il est possible de les télécharger avec un fureteur standard.

Les fichiers se trouvent à l'adresse suivante :

* [https://dd.meteo.gc.ca/climate/observations/normals/csv/1981-2010/{[AB,BC,MB,NB,NL,NS,NT,NU,ON,PE,QC,SK,YT]}](https://dd.meteo.gc.ca/climate/observations/normals/csv/1981-2010)
* [https://dd.meteo.gc.ca/climate/observations/daily/csv/{[AB,BC,MB,NB,NL,NS,NT,NU,ON,PE,QC,SK,YT]}](https://dd.meteo.gc.ca/climate/observations/daily/csv)
* [https://dd.meteo.gc.ca/climate/observations/hourly/csv/{[AB,BC,MB,NB,NL,NS,NT,NU,ON,PE,QC,SK,YT]}](https://dd.meteo.gc.ca/climate/observations/hourly/csv)
* [https://dd.meteo.gc.ca/climate/observations/monthly/csv/{[AB,BC,MB,NB,NL,NS,NT,NU,ON,PE,QC,SK,YT]}](https://dd.meteo.gc.ca/climate/observations/monthly/csv)

avec :

* __normals__ : Les normales et moyennes climatiques servent à résumer ou à décrire les conditions climatiques moyennes d'un endroit donné, basées sur au moins 15 années de données entre 1981 à 2010.
* __daily__ : Données quotidiennes provenant de stations climatiques quotidiennes et de stations horaires.
* __hourly__ : Données horaires provenant de stations horaires.
* __monthly__ : Sommaire transcanadien des moyennes et des extrêmes pour le mois, y compris les précipitations totales, les températures maximales et minimales et les degrés-jours. Ces données sont disponibles qui produisent des données quotidiennes.
* __(AB,BC,MB,NB,NL,NS,NT,NU,ON,PE,QC,SK,YT)__ : liste des 13 provinces/territoires.

## Nomenclature des noms de fichiers

* climate_normals_PROVTERR_XXXXXXX_YYY1-YYY2.csv
* climate_daily_PROVTERR_XXXXXXX_YYYY-MM_P1D.csv
* climate_hourly_PROVTERR_XXXXXXX_YYYY_P1H.csv
* climate_monthly_PROVTERR_XXXXXXX_YYYY_P1M.csv

avec :
 
* __climate__ : Chaîne constante indiquant la source des données, soit les données climatiques
* __normals__ : Chaîne constante indiquant les données climatiques qui contribuent de façon critique à la caractérisation du climat de la Terre
* __daily__ : Chaîne constante indiquant les données climatiques quotidiennes
* __hourly__ : Chaîne constante indiquant les données climatiques horaires
* __monthly__ : Chaîne constante indiquant les données climatiques mensuelles
* __PROVTERR__ : Code de 2 lettres pour les provinces et territoires et une chaîne de caractères pour la couverture nationale. Le code prend l’une des 13 valeurs suivantes :
    * AB (Alberta)
    * BC (Colombie britannique)
    * MB (Manitoba)
    * NB (Nouveau Brunswick)
    * NL (Terre-Neuve et Labrador)
    * NS (Nouvelle Ecosse)
    * NT (Territoires du nord-ouest)
    * NU (Nunavut)
    * ON (Ontario)
    * PE (Île-du-Prince-Édouard)
    * QC (Québec)
    * SK (Saskatchewan)
    * YT (Yukon)
* __XXXXXXX__ :  Climate_ID (identifiants) des stations climatiques (voir note)
* __YYY1__ : Année du début de la période climatique d’intérêt : [1981]
* __YYY2__ : Année de la fin de la période climatique d’intérêt : [2010]
* __YYYY__ : Année des données climatiques quotidiennes/mensuelles 
* __MM__ : Mois des données climatiques quotidiennes 
* __P1D__ : Chaîne constante indiquant un pas de temps de 1 jour (standard ISO8601)
* __P1H__ : Chaîne constante indiquant un pas de temps de 1 heure (standard ISO8601)
* __P1M__ : Chaîne constante indiquant un pas de temps de 1 mois (standard ISO8601)
* __csv__ : Chaîne constante indiquant le format CSV


Exemples :

* climate_normals_QC_7040446_1981-2010.csv 
* climate_daily_QC_7025280_1993-03_P1D.csv
* climate_hourly_MB_5010480_1977_P1H.csv
* Climate_monthly_QC_7025280_2001_P1M.csv

Note : La liste des codes de stations est disponible à l'adresse https://drive.google.com/drive/folders/1WJCDEU34c60IfOnG4rv5EPZ4IhhW9vZH

## Liste des variables

La liste des variables disponibles et leurs unités sont disponibles ici :

* [Normales climatiques](https://www.canada.ca/fr/environnement-changement-climatique/services/changements-climatiques/centre-canadien-services-climatiques/afficher-telecharger/documentation-technique-normales-climatiques.html#toc1)
* [Données quotidiennes](https://www.canada.ca/fr/environnement-changement-climatique/services/changements-climatiques/centre-canadien-services-climatiques/afficher-telecharger/documentation-technique-donnees-quotidiennes.html#toc0)
* [Données horaires](https://www.canada.ca/fr/environnement-changement-climatique/services/changements-climatiques/centre-canadien-services-climatiques/afficher-telecharger/documentation-technique-donnees-horaires.html#toc0)
* [Sommaires climatiques mensuels](https://www.canada.ca/fr/environnement-changement-climatique/services/changements-climatiques/centre-canadien-services-climatiques/afficher-telecharger/documentation-technique-sommaires-climatologiques-mensuels.html#toc0)

## Contenu des fichiers

* __Normales climatiques__

Les normales climatiques, moyennes et extrêmes climatiques, offertes ici reposent sur les stations climatologiques canadiennes ayant au moins 15 années de données entre 1981 à 2010.

Les expressions « moyennes climatiques » ou « normales climatiques » sont interchangeables. Elles désignent le résultat de calculs arithmétiques fondés sur les valeurs de paramètres climatiques observées à un endroit donné au cours d'une période spécifique.

L'Organisation météorologique mondiale (OMM) recommande que les pays préparent des normales climatiques sur des périodes officielles de 30 ans se terminant en 1930, 1960 et 1990, pour lesquelles les normales climatiques mondiales de l'OMM sont publiées. En outre, l'OMM recommande une mise à jour des normales climatiques à la fin de chaque décennie, comme cela est fait ici pour la période de 1981 à 2010.

Voir la documentation détaillée ici :

[ttps://www.canada.ca/fr/environnement-changement-climatique/services/changements-climatiques/centre-canadien-services-climatiques/afficher-telecharger/documentation-technique-normales-climatiques.html](https://www.canada.ca/fr/environnement-changement-climatique/services/changements-climatiques/centre-canadien-services-climatiques/afficher-telecharger/documentation-technique-normales-climatiques.html)

* __Données quotidiennes__

Les données quotidiennes proviennent de deux sources de données.  Les premières sont les stations climatiques quotidiennes produisant une ou deux observations par jour de température et de précipitations.  Les secondes sont les stations horaires (voir les séries de données horaires) qui produisent généralement plus d'éléments météorologiques, par ex. vent ou neige au sol.

Les données sont disponibles pour les stations actuellement opérationnelles avec de longues périodes d’enregistrement.

Voir la documentation détaillée ici :

[https://www.canada.ca/fr/environnement-changement-climatique/services/changements-climatiques/centre-canadien-services-climatiques/afficher-telecharger/documentation-technique-donnees-quotidiennes.html](https://www.canada.ca/fr/environnement-changement-climatique/services/changements-climatiques/centre-canadien-services-climatiques/afficher-telecharger/documentation-technique-donnees-quotidiennes.html)

* __Données horaires__

Les données horaires proviennent des stations horaires (voir les séries de données horaires) qui produisent généralement plusieurs éléments météorologiques, par ex. vent ou neige au sol.

Les données sont disponibles pour les stations actuellement opérationnelles avec de longues périodes d’enregistrement.

Voir la documentation détaillée ici :

[https://www.canada.ca/fr/environnement-changement-climatique/services/changements-climatiques/centre-canadien-services-climatiques/afficher-telecharger/documentation-technique-donnees-horaires.html](https://www.canada.ca/fr/environnement-changement-climatique/services/changements-climatiques/centre-canadien-services-climatiques/afficher-telecharger/documentation-technique-donnees-horaires.html)

* __Données mensuelles__

Un sommaire transcanadien des moyennes et des extrêmes pour le mois, y compris les précipitations totales, les températures maximales et minimales et les degrés-jours.

Voir la documentation détaillée ici :

[https://www.canada.ca/fr/environnement-changement-climatique/services/changements-climatiques/centre-canadien-services-climatiques/afficher-telecharger/documentation-technique-sommaires-climatologiques-mensuels.html](https://www.canada.ca/fr/environnement-changement-climatique/services/changements-climatiques/centre-canadien-services-climatiques/afficher-telecharger/documentation-technique-sommaires-climatologiques-mensuels.html)

## Support

Pour toute question relative à ces données, merci de [nous contacter](https://weather.gc.ca/mainmenu/contact_us_f.html).

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).


