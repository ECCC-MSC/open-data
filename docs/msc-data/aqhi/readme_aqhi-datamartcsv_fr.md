[In English](readme_aqhi-datamartcsv_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [CAS](readme_aqhi_fr.md) > Données CSV de CAS sur le Datamart du SMC

# Données CSV d'observations et prévisions qui sont générées pour le programme Cote Air Santé (CAS)

Cette page décrit les données d'observations et de prévisions disponibles en format CSV pour la [cote air santé CAS](readme_aqhi_fr.md) qui sont aussi disponibles sur le [site web d'Environnement et Changement climatique Canada](https://meteo.gc.ca/airquality/pages/index_f.html). 

## Adresses des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTP. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier CSV.

Les données sont accessibles aux adresses suivantes :

* **Observations** : 

    * Fichiers en temps réel : 
        * Région de l'Atlantique : [https://dd.meteo.gc.ca/air_quality/aqhi/atl/observation/realtime/csv](https://dd.meteo.gc.ca/air_quality/aqhi/atl/observation/realtime/csv)
        * Région de l'Ontario : [https://dd.meteo.gc.ca/air_quality/aqhi/ont/observation/realtime/csv](https://dd.meteo.gc.ca/air_quality/aqhi/ont/observation/realtime/csv)
        * Région des Prairies et du Nord : [https://dd.meteo.gc.ca/air_quality/aqhi/pnr/observation/realtime/csv](https://dd.meteo.gc.ca/air_quality/aqhi/pnr/observation/realtime/csv)
        * Région du Pacifique et Yukon : [https://dd.meteo.gc.ca/air_quality/aqhi/pyr/observation/realtime/csv](https://dd.meteo.gc.ca/air_quality/aqhi/pyr/observation/realtime/csv)
        * Région du Québec : [https://dd.meteo.gc.ca/air_quality/aqhi/que/observation/realtime/csv](https://dd.meteo.gc.ca/air_quality/aqhi/que/observation/realtime/csv)
    
    * Fichiers mensuels :
        * Région de l'Atlantique : [https://dd.meteo.gc.ca/air_quality/aqhi/atl/observation/monthly/csv](https://dd.meteo.gc.ca/air_quality/aqhi/atl/observation/monthly/csv)
        * Région de l'Ontario : [https://dd.meteo.gc.ca/air_quality/aqhi/ont/observation/monthly/csv](https://dd.meteo.gc.ca/air_quality/aqhi/ont/observation/monthly/csv)
        * Région des Prairies et du Nord : [https://dd.meteo.gc.ca/air_quality/aqhi/pnr/observation/monthly/csv](https://dd.meteo.gc.ca/air_quality/aqhi/pnr/observation/monthly/csv)
        * Région du Pacifique et Yukon : [https://dd.meteo.gc.ca/air_quality/aqhi/pyr/observation/monthly/csv](https://dd.meteo.gc.ca/air_quality/aqhi/pyr/observation/monthly/csv)
        * Région du Québec : [https://dd.meteo.gc.ca/air_quality/aqhi/que/observation/monthly/csv](https://dd.meteo.gc.ca/air_quality/aqhi/que/observation/monthly/csv)

* **Prévisions publiques** :
    * Fichiers mensuels : 
        * Région de l'Atlantique : [https://dd.meteo.gc.ca/air_quality/aqhi/atl/forecast/monthly/csv](https://dd.meteo.gc.ca/air_quality/aqhi/atl/forecast/monthly/csv)
        * Région de l'Ontario : [https://dd.meteo.gc.ca/air_quality/aqhi/ont/forecast/monthly/csv](https://dd.meteo.gc.ca/air_quality/aqhi/ont/forecast/monthly/csv)
        * Région des Prairies et du Nord : [https://dd.meteo.gc.ca/air_quality/aqhi/pnr/forecast/monthly/csv](https://dd.meteo.gc.ca/air_quality/aqhi/pnr/forecast/monthly/csv)
        * Région du Pacifique et Yukon : [https://dd.meteo.gc.ca/air_quality/aqhi/pyr/forecast/monthly/csv](https://dd.meteo.gc.ca/air_quality/aqhi/pyr/forecast/monthly/csv)
        * Région du Québec : [https://dd.meteo.gc.ca/air_quality/aqhi/que/forecast/monthly/csv](https://dd.meteo.gc.ca/air_quality/aqhi/que/forecast/monthly/csv)


* **Données des modèles numériques** :

    * Région de l'Atlantique : [https://dd.meteo.gc.ca/air_quality/aqhi/atl/forecast/model/csv](https://dd.meteo.gc.ca/air_quality/aqhi/atl/forecast/model/csv)
    * Région de l'Ontario : [https://dd.meteo.gc.ca/air_quality/aqhi/ont/forecast/model/csv](https://dd.meteo.gc.ca/air_quality/aqhi/ont/forecast/model/csv)
    * Région des Prairies et du Nord : [https://dd.meteo.gc.ca/air_quality/aqhi/pnr/forecast/model/csv](https://dd.meteo.gc.ca/air_quality/aqhi/pnr/forecast/model/csv)
    * Région du Pacifique et Yukon : [https://dd.meteo.gc.ca/air_quality/aqhi/pyr/forecast/model/csv](https://dd.meteo.gc.ca/air_quality/aqhi/pyr/forecast/model/csv)
    * Région du Québec : [https://dd.meteo.gc.ca/air_quality/aqhi/que/forecast/model/csv](https://dd.meteo.gc.ca/air_quality/aqhi/que/forecast/model/csv)
  

## Rétention des données 

Les fichiers CSV en temps réel sont produits aux heures et ils contiennent les données pour les 7 derniers jours. Ils sont disponibles sur le Datamart du SMC pour une période de 8 jours. Les fichiers CSV mensuels sont produits à la fin de chaque mois. Ils sont disponibles sur le Datamart du SMC pour une période de 12 mois.
    
## Nomenclature des noms de fichiers 

NOTE: TOUTES LES HEURES SONT EN UTC.

* **Observations**: 
  
    * Fichiers en temps réel: AAAAMMJJhh_AQHI_REGION_OBSTYPE.csv
    * Fichiers mensuels: AAAAMM_MONTHLY_AQHI_REGION_OBSTYPE.csv
    * Fichiers mensuels avec données remblayées :  AAAAMM_MONTHLY_AQHI_REGION_OBSTYPE_BACKFILLED.csv

* où : 
    
    * __AAAA__ : Année de l'observation, 4 chiffres.
    * __MM__ : Mois de l'observation, 2 chiffres (janvier = 01).
    * __JJ__ : Jour de l'observation, 2 chiffres.
    * __hh__ : Heure de l'observation, 2 chiffres.
    * __mm__ : Minute de l'observation, 2 chiffres.
    * __'MONTHLY'__ : Symbole présent lorsque le fichier contient des données mensuelles.
    * __REGION__ : Nom de la région d'Environnement et Changement climatique Canada  où les observations sont situées. Les valeurs possibles sont les suivantes :
        * 'ATL'= Région de l'Atlantique
        * 'ON'= Région de l'Ontario
        * 'PNR'= Région des Prairies et du Nord
        * 'PYR'= Région du Pacifique et du Yukon
        * 'QC'= Région du Québec
    * __OBSTYPE__ : Type d'observation dans le fichier. Les options possibles sont les suivantes :
        * 'SiteObs' = Le fichier contient les observations de CAS pour les [communautés](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/aqhi/aqhi_community.geojson),
        * 'StationObs' = Le fichier contient les observations de CAS pour les stations d'observation associées aux communautés (non disponible au mois de janvier 2012).
        * __'BACKFILLED'__ : Symbole présent lorsque le fichier contient des observations de CAS qui ne sont pas calculées en temps-réel, mais qui sont calculées à partir des données remblayées ou corrigées (reçues dans les 48 heures suivant l'heure de validité).

* **Prévisions publiques** : 

   * AAAAMM_MONTHLY_AQHI_CGNDB_SiteFcst.csv

* où : 
    
    * __AAAA__ : Année des prévisions, 4 chiffres.
    * __MM__ : Mois des prévisions, 2 chiffres (janvier = 01).
    * __'MONTHLY'__ : Symbole présent lorsque le fichier contient des données pour le mois.
    * __CGNDB__ : Un [code de 5-caractères](http://www4.rncan.gc.ca/recherche-de-noms-de-lieux/unique) identifiant chaque [communauté de la CAS](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/aqhi/aqhi_community.geojson). 
    * __'SiteFcst'__ : Symbole indiquant que le fichier contient des prévisions de CAS pour une [communauté](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/aqhi/aqhi_community.geojson).

Une [liste complète des communautés](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/aqhi/aqhi_community.geojson), avec les codes de [CGNDB](http://www4.rncan.gc.ca/recherche-de-noms-de-lieux/unique), données toponymiques du Canada maintenues par Ressources naturelles Canada, est disponible en format GeoJSON.

* **Données des modèles numériques**:

    * AAAAMMDDhh_SPECIE_REGION_MODELTYPE.csv

* où :
    
    * __AAAA__ : année pour laquelle les données ont été générées, 4 chiffres;
    * __MM__ : mois pour lequel les données ont été générées, 2 chiffres (Janvier = 01);
    * __DD__ : jour pour lequel les données ont été générées, 2 chiffres;
    * __hh__ : heure pour laquelle les données ont été générées, 2 chiffres (00 ou 12 UTC);
    * __'SPECIE'__ : nom de l'espèce chimique. Les options possibles sont les suivantes :
        * 'O3' = Ozone
        * 'NO2' = Dioxyde d'azote
        * 'PM2.5' = Particules d'un diamètre de moins de 2.5 um
        * 'PM10' = Particules d'un diamètre de moins de 10 um
        * 'AQHI' = Cote Air Santé
    * __REGION__ : Nom de la région d'Environnement et Changement climatique Canada  pour laquelle les données sont valides. Les valeurs possibles sont les suivantes :
        * 'ATL' = Région de l'Atlantique
        * 'ON' = Région de l'Ontario
        * 'PNR' = Région des Prairies et du Nord
        * 'PYR' = Région du Pacifique et du Yukon
        * 'QC' = Région du Québec
    * __MODELTYPE__ : Système utilisé pour générer les données. Les options possibles sont les suivantes :
        * 'AQFM' = Modèle de prévision de la qualité de l'air,
        * 'UMOSAQ' = Le système de post-traitement "Updateable Model Output Statistics" appliqué aux sorties bruts de l'AQFM,
        * 'UMOSAQMIST' = Données combinées des systèmes AQFM et UMOSAQ générées à fournir des informations additionelles aux météorologues car les données d'UMOSAQ ne sont pas toujours disponibles directement aux points d'observation.

## Contenu des fichiers

* **Fichiers CSV des observations de CAS calculées à partir des donnèes sur les polluants reçus en temps-réel** (pour les fichiers en temps réels et mensuels) :

    * **En-tête**
  
L'en-tête présent sur la première ligne contient les informations suivantes :
   
|Date | Hour | CGNDB_Site1 | CGNDB_Site2 | ... | CGNDB_SiteN |
|-----|------|-------------|-------------|-----|-------------|
   
* où:
    
    * 'Date' : Étiquette statique
    * 'Hour' : Étiquette statique
    * CGNDB_Site# : Code de 5 caractères identifiant chaque [communauté CAS](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/aqhi/aqhi_community.geojson). 

* **Bloc de données**
  
Les observations sont fournit avec une précision de deux décimales.
   
Chaque ligne d'un bloc de données contient les informations suivantes :

|AAAA-MM-JJ | hh | CAS_Site1 | CAS_Site2 | ... | CAS_SiteN |
|-----------|----|-----------|-----------|-----|-----------|

* où :

    * AAAA : Année de l'observation
    * MM : Mois de l'observation
    * JJ : Jour de l'observation
    * hh : L'heure de l'observation
    * CAS_Site# : Observations de la CAS pour toutes les [communautés](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/aqhi/aqhi_community.geojson) dans la région.

Note : Les fichiers en temps réels contiennent les 7 derniers jours d’observations de la CAS, avec les observations les plus récentes en premier. Ils sont disponibles sur le Datamart du SMC pour une période de 48 heures. Les fichiers mensuels sont également ordonnés en ordre décroissant avec les observations les plus récentes en premier. Ceux-ci sont disponibles sur le Datamart du SMC pour une période de 12 mois.

* **Fichiers CSV des observations de CAS calculées à partir des donnèes remblayées ou corrigées** (uniquement disponible dans les fichiers mensuels) :

Ces fichiers ont la même structure que les fichiers mensuels décrits précédemment, mais son contenu en diffère. En effet, ce fichier présente les valeurs de la CAS calculées 48 heures suivant l’heure de validité à partir des données corrigées et remblayées. 

* **Fichiers CSV des prévisions publiques de CAS** (uniquement disponible dans le fichiers mensuels) :

    * **En-tête**
  
L'en-tête présent sur la première ligne de chaque fichier contient les informations suivantes :

| cgndb code | community name | issue date | issue time | period | value | amended |
|------------|----------------|------------|------------|--------|-------|---------|

* **Bloc de données**
  
Les prévisions publiques sont fournit en nombres entiers.
   
| CGNDBcode | CommunityName | IssueDate | IssueTime | ForecastPeriod | Value | AmendmentFlag |
|-----------|---------------|-----------|-----------|----------------|-------|---------------|

* où :
   
    * CGNDBcode : Code de 5-caractères qui identifie chaque [communauté CAS](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/aqhi/aqhi_community.geojson). 
    * CommunityName : Nom utilisé de la [communauté](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/aqhi/aqhi_community.geojson) associée au code CGNDB, et pour laquelle la prévision est valide,
    * IssueDate : Date d'émission de la prévision (AAAA-MM-JJ),
    * IssueTime : Heure d'émission de la prévision (hh:mm:ss),
    * ForecastPeriod : Période de prévision représentée par un entier entre 1 et 3 ("Aujourd'hui", "Ce soir et cette nuit", ou "Demain", respectivement),
        - pour les prévisions émises à 06h00 (heure locale): 1 = Aujourd'hui, 2 = Ce soir et cette nuit, 3 = Demain
        - pour les prévisions émises à 17h00 (heure locale): 2 = Ce soir et cette nuit, 3 = Demain
    * Value : valeur de la prévision de CAS pour la période de prévision en question,
    * AmendmentFlag : Entier représentant le nombre d’amendements effectués à la prévision. La première émission de la prévision indique toujours une valeur de zéro, puis celle-ci est incrémentée de 1 à chaque ammendement. 


Note : Les fichiers mensuels de prévisions publiques de la CAS sont ordonnés en ordre décroissant avec les prévisions les plus récentes en premier. Ceux-ci sont disponibles sur le Datamart du SMC pour une période de 12 mois.
  
* **Fichiers CSV qui contiennent les données des modèles** :
 
    * **En-tête**
  
L'en-tête présent sur la première ligne de chaque fichier contient les informations suivantes :
   
1) Pour les fichiers qui contiennent des données de polluants (O3, NO2, PM2.5, PM10) :
     
| stationId | YYYYMMDDhh +0 | YYYYMMDDhh+1 | ... | YYYYMMDDhh+48 |
|-----------|---------------|--------------|-----|---------------|

* où:
    
    *  "stationId" identifiant NAPS unique de la station d’observation. 
    * YYYYMMDDhh+# date (YYYYMMDD) et heure de la prévision (hh) du modèle, jusqu’à 48 heures (de H+000 à H+048).

2) Pour les fichiers qui contiennent des données de CAS :
   
| cgndb | forecast date (hour0) | forecast date (hour1) | ... | forecast date (hour47),forecast date (hour48) |
|-------|-----------------------|-----------------------|-----|-----------------------------------------------|

* où:
    
    * "cgndb" identifiant CGNDB de la [communauté](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/aqhi/aqhi_community.geojson) pour laquelle la prévision est effectuée. 
    * YYYYMMDDhh+# date (YYYYMMDD) et heure de la prévision (hh) du modèle, jusqu’à 48 heures (de H+000 à H+048).
     
* **Bloc de données**
 
Les données des modèles pour toutes les espèces sont fournit avec 2 décimales.
   
Chaque ligne d'un bloc de données contient les informations suivantes :

1) Pour les fichiers qui contiennent des données de polluants (O3, NO2, PM2.5, PM10) :

| StationID | Valeur (H+000) | Valeur (H+001) | ... | Valeur (H+047) | Valeur (H+048) |
|-----------|----------------|----------------|-----|----------------|----------------|

2) Pour les fichiers qui contiennent des données de CAS :
   
| StationID | Valeur (H+000) | Valeur (H+001) | ... | Valeur (H+047) | Valeur (H+048) |
|-----------|----------------|----------------|-----|----------------|----------------|

* où :
   
    * StationID : Identifiant NAPS unique de la station d’observation.
    * CGNDBcode : un code de 5-caractères qui identifie chaque [communauté CAS](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/aqhi/aqhi_community.geojson).
    * Valeur (H+000 à H+048) : valeur du modèle dérivée à la station d'observation (pour UMOSAQ) ou interpolées à la station d'observation (pour AQFM, UMOSAQMIST). 
  
## Notes

* Les fichiers CSV « real-time » sont produits aux heures et ils contiennent les données pour les dernières 7 jours. Ils sont disponibles sur le Datamart pour une période de 8 jours. Les fichiers CSV « MONTHLY » sont produits à la fin de chaque mois. Ils sont disponibles sur le Datamart du SMC pour une période de 12 mois.

* Dans les fichiers CSV pour la CAS, la valeur de la première heure est toujours manquante parce que la formule de la CAS nécessite un minimum de deux heures au cours des dernières 3 heures pour calculer les moyennes mobiles.

* Dans les fichiers CSV pour UMOSAQ, il est possible que certaines valeurs soient manquantes en raison de prévisions manquantes. La disponibilité des prévisions de UMOS pour une heure spécifique dépend de l'existence de données historiques suffisantes pour être en mesure de générer des équations statistiques/prédictifs qui sont fiables.

* Les observations de qualité de l'air sont distribuées par les provinces et municipalités. Les juridictions provinciales contrôlent la façon dont les observations sont communiquées au public. Le Québec n'a pas autorisé la publication des données de qualité de l'air sous la forme de côte air santé (CAS). Ceci explique pourquoi on ne retrouve pas d'observation sous le répertoire : [https://dd.meteo.gc.ca/air_quality/aqhi/que/observation/](https://dd.meteo.gc.ca/air_quality/aqhi/que/observation/). Cependant, le Ministère du Développement durable, de l'Environnement et de lutte contre les Changements climatiques ainsi que la ville de Montréal distribuent aussi certaines de leurs données sur le portail américain AirNow: [https://www.airnowtech.org/index.cfm?page=login](https://www.airnowtech.org/index.cfm?page=login).

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).
