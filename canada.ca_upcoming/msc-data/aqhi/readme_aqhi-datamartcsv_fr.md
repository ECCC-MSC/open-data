[In English](readme_aqhi-datamartcsv_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données ouvertes publiques du SMC](../readme_fr.md) > CAS sur le Datamart du SMC

# Données CSV d'observations et prévisions qui sont générés pour le programme Cote Air Santé (CAS)

Cette page décrit les données d'observations et de prévisions disponibles en format CSV pour la [cote air santé CAS](readme_aqhi_fr.md) qui sont aussi disponibles sur le [site web d'Environnement et Changement climatique Canada](https://meteo.gc.ca/airquality/pages/index_f.html). 

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le Protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage-overview/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTP. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier CSV.

Les données sont accessibles à adresse suivante:

* **Observations**: 

  * Fichiers en temps réel: 
    https://dd.meteo.gc.ca/air_quality/aqhi/[atl|ont|pnr|pyr|que]/observation/realtime/csv
  
  * Fichiers mensuels :  
    https://dd.meteo.gc.ca/air_quality/aqhi/[atl|ont|pnr|pyr|que]/observation/monthly/csv

* **Prévisions publiques**:

  * Fichiers mensuels:
    https://dd.meteo.gc.ca/air_quality/aqhi/[atl|ont|pnr|pyr|que]/forecast/monthly/csv
    
* **Données des modèles numériques**:

  * https://dd.weather.gc.ca/air_quality/aqhi/[atl|ont|pnr|pyr|que]/forecast/model/csv

Note: Les fichiers CSV « real-time » sont produits aux heures et ils contiennent les données pour les dernières 7 jours. Ils sont disponibles sur le Datamart du SMC pour une période de 8 jours. Les fichiers CSV « MONTHLY » sont produits à la fin de chaque mois. Ils sont disponibles sur le Datamart du SMC pour une période de 12 mois.
    
## Nomenclature des noms de fichiers 

NOTE: TOUTES LES HEURES SONT EN UTC.

* **Observations**: 
  
  * Fichiers en temps réel: AAAAMMJJhh_AQHI_REGION_OBSTYPE.csv
  * Fichiers mensuels: AAAAMM_MONTHLY_AQHI_REGION_OBSTYPE.csv
  * Fichiers mensuels avec données remblayées :  AAAAMM_MONTHLY_AQHI_REGION_OBSTYPE_BACKFILLED.csv
  
où: 

* AAAA: année de l'observation, 4 chiffres;
* MM: mois de l'observation, 2 chiffres (janvier = 01);
* JJ: jour de l'observation, 2 chiffres;
* hh: heure de l'observation, 2 chiffres;
* mm: minute de l'observation, 2 chiffres;
* 'MONTHLY': symbole qui est présent lorsque le fichier contient des données pour le mois;
* REGION: Nom de la région d'Environnement et Changement climatique Canada  où les observations sont situées. Les valeurs
possibles sont les suivantes:
    * 'ATL'= Région de l'Atlantique,
    * 'ON'= Région de l'Ontario,
    * 'PNR'= Région des prairies et du nord,
    * 'PYR'=Région du Pacifique et Yukon,
    * 'QC'= Région du Québec;
* OBSTYPE: type d'observation dans le fichier. Les options possibles sont les suivants:
    * 'SiteObs'=le fichier contient les observations de CAS pour les communautés,
    * 'StationObs'= le fichier contient les observations de CAS pour les stations d'observation associées
    aux communautés (non disponible au mois de janvier 2012).
    * 'BACKFILLED': symbole qui est présent lorsque le fichier contient des observations de CAS qui
    ne sont pas calculées en temps-réel, mais qui sont calculées à partir des donnèes remblayées ou
    corrigées (reçues dans les 48 heures qui suivent l'heure de validité).

* **Prévisions publiques**: 

  * AAAAMM_MONTHLY_AQHI_CGNDBcode_SiteFcst.csv

où: 

* AAAA: année des prévisions, 4 chiffres;
* MM: mois des prévisions, 2 chiffres (janvier = 01);
* 'MONTHLY': symbole qui est présent lorsque le fichier contient des données pour le mois;
* CGNDB_code: un [code de 5-caractères](http://www4.rncan.gc.ca/recherche-de-noms-de-lieux/unique) qui identifie chaque communauté de la CAS. 
* 'SiteFcst': symbole qui est présent pour indiqué que le fichier contient prévisions de CAS pour une communauté.

Une [liste complète des villes](aqhi.geojson), avec les codes de [CGNDB](http://www4.rncan.gc.ca/recherche-de-noms-de-lieux/unique), données toponymiques du Canada maintenues par Ressources naturelles Canada, est disponible en format GeoJSON.

* **Données des modèles numériques**:

  * AAAAMMDDhh_SPECIES_REGION_MODELTYPE.csv
    
où:

* AAAA: année pour laquelle les données ont été générées, 4 chiffres;
* MM: mois pour lequel les données ont été générées, 2 chiffres (January = 01);
* DD: jour pour lequel les données ont été générées, 2 chiffres;
* hh: heure pour laquelle les données ont été générées, 2 chiffres (00 ou 12 UTC);
* 'SPECIES': nom de l'espèce chimique dans le fichier. Les options possibles sont les suivants:
    * 'O3'=ozone,
    * 'NO2'=dioxyde d'azote,
    * 'PM2.5'=particules d'un diamètre de moins de 2.5 um,
    * 'PM10'=particules d'un diamètre de moins de 10 um,
    * 'AQHI'=Cote air santé,
* REGION: Nom de la région d'Environnement et Changement climatique Canada  pour laquelle les données sont valides. Les valeurs
possibles sont les suivantes:
    * 'ATL'= Région de l'Atlantique,
    * 'ON'= Région de l'Ontario,
    * 'PNR'= Région des prairies et du nord,
    * 'PYR'=Région du Pacifique et Yukon,
    * 'QC'= Région du Québec;
* MODELTYPE: Indique le système utilisé pour générer les données. Les options possibles sont les suivants:
    * 'AQFM'=modèle de prévision de la qualité de l'air,
    * 'UMOSAQ'=le système de post-traitement "Updateable Model Output Statistics" appliqué aux sorties bruts de l'AQFM,
    * 'UMOSAQMIST'=les données combinées des systèmes AQFM et UMOSAQ; générées à fournir des informations additionelles
    aux météorologues car les données d'UMOSAQ ne sont pas toujours disponibles directement aux points d'observation.

## Contenu des fichiers

* **Fichiers CSV avec observations de CAS calculées à partir des donnèes sur les polluants reçus en 
temps-réel** (pour les fichiers en format « real-time » et « MONTHLY »):

  * **En tête**
  
   L'en-tête est donnée sur la première ligne et il contient les informations suivantes:
   
   Date,Hour,CGNDB_Site1,CGNDB_Site2,...,CGNDB_SiteN
   
    où:
    
      * 'Date': étiquette statique
      * 'Hour': étiquette statique
      * CGNDB_Site#: un code de 5-caractères qui identifie chaque communauté CAS. 

  * **Bloc de données**
  
   Les observations sont fournit avec une précision de deux décimales.
   
   Chaque ligne d'un bloc de données contient les informations suivantes:

    AAAA-MM-JJ,hh,CAS_Site1,CAS_Site2,...,CAS_SiteN

    où:
    
      * AAAA: l'année de l'observation.
      * MM: le mois de l'observation.
      * JJ: le jour de l'observation.
      * hh: L'heure de l'observation.
      * CAS_Site#: Les observations de la CAS pour toutes les communautés dans la région.

    Note: Pour les fichiers "real-time", les observations de CAS couvrent les dernières
sept jours avec l'observation le plus recente au première ligne. Ils sont disponibles
sur le Datamart du SMC pour une période de 48 heures. Pour les fichiers « MONTHLY », les
observations de CAS couvrent la période de la fin du mois (au première ligne) au
début du mois (au dernière ligne). Ils sont disponibles sur le Datamart du SMC pour une période
de 12 mois.

* **Fichiers CSV avec observations de CAS calculées à partir des donnèes remblayées ou corrigées**
(uniquement fichiers en format « MONTHLY »):

  Ces produits ont une description identique que pour les fichiers « MONTHLY » fourni dans 2.1.1. Cependant, le
contenu est différent en ce que les valeurs de CAS sont calculées 48 heures après l'heure de validité pour
permettre l'arrivée des données manquantes et des corrections pour les polluants. 

* **Fichiers CSV avec prévisions publiques de CAS** (uniquement fichiers « MONTHLY »):

  * **En tête**
  
   L'en-tête est donnée sur la première ligne et il contient les informations suivantes:

   cgndb code,community name,issue date,issue time,period,value,amended

   où les valeurs sont tous les symboles qui décrivent le contenu des lignes qui suivent.

  * **Bloc de données**
  
   Les prévisions publiques sont fournit en nombres entiers.
   
   CGNDBcode,CommunityName,IssueDate,IssueTime,ForecastPeriod,Value,AmendmentFlag

   où:
   
      * CGNDBcode: un code de 5-caractères qui identifie chaque communauté CAS. 
      * CommunityName: le nom utilisé pour identifier la communauté associée au code CGNDB, et pour laquelle la prévision est valide,
      * IssueDate: le jour pour lequel la prévision a été émise (AAAA-MM-JJ),
      * IssueTime: le moment précis où la prévision a été émise (hh:mm:ss),
      * ForecastPeriod: entier avec une valeur de 1, 2, ou 3, qui répresente la période de prévision ("Aujourd'hui", "Ce soir et cette nuit", ou "Demain", respectivement),
        - pour les prévisions émises à 06h00 (heure locale): 1=Aujourd'hui, 2=Ce soir et cette nuit, 3=Demain
        - pour les prévisions émises à 17h00 (heure locale): 2=Ce soir et cette nuit, 3=Demain
      * Value: valeur de la prévision de CAS pour la période de prévision en question,
      * AmendmentFlag: entier avec un valeur de 0 pour la première émission de la prévision et qui s'incrémente par +1 pour chaque ammendement qui suit.

    Note: Dans ces fichiers « MONTHLY », les prévisions publiques de CAS sont écrites avec l'émission le plus récente
(à la fin du mois) au première ligne et ils procèdent à reculer dans le temps jusqu'au première émission (au début
du mois) au dernière ligne. Ils sont disponibles sur le Datamart du SMC pour une période de 12 mois.
  
* **Fichiers CSV qui contiennent des données des modèles**:
 
  * **En-tête**
  
   L'en-tête est donnée sur la première ligne et il contient les informations suivantes:

    1) Pour les fichiers qui contiennent des données de polluant (O3, NO2, PM2.5, PM10):
stationId,date de prévision (heure0),date de prévision (heure1), ... , date de prévision (heure48)

    2) Pour les fichiers qui contiennent des données de CAS:
cgndb,forecast date (hour0),forecast date (hour1), ... , forecast date (hour47),forecast date (hour48)

    où:
    
      * "stationId" est un symbol qui déclare que les valeurs dans la première colonne identifient les stations dans la région d'intérêt;
      * "cgndb" est un symbol qui déclare que les valeurs dans la première colonne identifient les communautés dans la région d'intérêt;
      * les 49 valeurs qui suivent le stationId sont les dates (format=AAAMMJJhh) qui définissent l'heure de prévision (de H+000 à H+048) du modèle et qui sont applicables à toutes les stations.
  
 * **Bloc de données**
 
   Les données des modèles pour toutes les espèces sont fournit avec 2 décimales.
   
   Chaque ligne d'un bloc de données contient les informations suivantes:

   1) Pour les fichiers qui contiennent des données de polluant (O3, NO2, PM2.5, PM10):
StationID, Valeur (H+000), Valeur (H+001), ... , Valeur (H+047), Valeur (H+048)

   2) Pour les fichiers qui contiennent des données de CAS:
StationID, Valeur (H+000), Valeur (H+001), ... , Valeur (H+047), Valeur (H+048)

   où:
   
       * StationID: code de NAPS qui identifie la station d'observation à laquelle les données de modèle sont fournies.
       * CGNDBcode: un code de 5-caractères qui identifie chaque communauté CAS. Une liste des codes CGNDB est données à la fin de ce fichier.
       * Valeur (H+000 à H+048): valeur du modèle dérivée à la station d'observation (pour UMOSAQ) ou interpolées à la station d'observation (pour AQFM, UMOSAQMIST). 
  
## Notes

* Les fichiers CSV « real-time » sont produits aux heures et ils contiennent les données pour les dernières 7 jours. Ils sont disponibles sur le Datamart pour une période de 8 jours. Les fichiers CSV « MONTHLY » sont produits à la fin de chaque mois. Ils sont disponibles sur le Datamart du SMC pour une période de 12 mois.

* Dans les fichiers CSV pour la CAS, la valeur de la première heure est toujours manquante parce que la formule de la CAS nécessite un minimum de deux heures au cours des dernières 3 heures pour calculer les moyennes mobiles.

* Dans les fichiers CSV pour UMOSAQ, il est possible que certaines valeurs soient manquantes en raison de prévisions manquantes. La disponibilité des prévisions de UMOS pour une heure spécifique dépend de l'existence de données historiques suffisantes pour être en mesure de générer des équations statistiques/prédictifs qui sont fiables.

* Les observations de qualité de l'air sont distribuées par les provinces et municipalités. Les juridictions provinciales contrôlent la façon dont les observations sont communiquées au public. Le Québec n'a pas autorisé la publication des données de qualité de l'air sous la forme de côte air santé (CAS). Ceci explique pourquoi on ne retrouve pas d'observation sous le répertoire : http://dd.meteo.gc.ca/air_quality/aqhi/que/observation/ . Cependant, le Minsitère du Développement durable, de l'Environnement et de lutte contre les Changements climatiques ainsi que la ville de Montréal distribuent aussi certaines de leurs données sur le portail américain AirNow: https://www.airnowtech.org/index.cfm?page=login.

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : ec.dps-client.ec@canada.ca

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).

















