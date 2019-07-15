[In English](readme_aqhi-datamartxml_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [CAS](readme_aqhi_fr.md) > Données XML de CAS sur le Datamart du SMC

# Données XML d'observations et prévisions qui sont générés pour le programme Cote Air Santé (CAS)

Cette page décrit les données d'observations et de prévisions disponibles en format XML pour la [cote air santé CAS](readme_aqhi_fr.md) qui sont aussi disponibles sur le [site web d'Environnement et Changement climatique Canada](https://meteo.gc.ca/airquality/pages/index_f.html). 

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTP. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier XML.

Les données sont accessibles à adresse suivante :

* Observations : 

    * Région de l'Atlantique : [https://dd.meteo.gc.ca/air_quality/aqhi/atl/observation/realtime/xml](https://dd.meteo.gc.ca/air_quality/aqhi/atl/observation/realtime/xml)
    * Région de l'Ontario : [https://dd.meteo.gc.ca/air_quality/aqhi/ont/observation/realtime/xml](https://dd.meteo.gc.ca/air_quality/aqhi/ont/observation/realtime/xml)
    * Région des Prairies et du Nord : [https://dd.meteo.gc.ca/air_quality/aqhi/pnr/observation/realtime/xml](https://dd.meteo.gc.ca/air_quality/aqhi/pnr/observation/realtime/xml)
    * Région du Pacifique et Yukon : [https://dd.meteo.gc.ca/air_quality/aqhi/pyr/observation/realtime/xml](https://dd.meteo.gc.ca/air_quality/aqhi/pyr/observation/realtime/xml)
    * Région du Québec : [https://dd.meteo.gc.ca/air_quality/aqhi/que/observation/realtime/xml](https://dd.meteo.gc.ca/air_quality/aqhi/que/observation/realtime/xml)
    
* Prévisions publiques : 
  
    * Région de l'Atlantique : [https://dd.meteo.gc.ca/air_quality/aqhi/atl/forecast/realtime/xml](https://dd.meteo.gc.ca/air_quality/aqhi/atl/forecast/realtime/xml)
    * Région de l'Ontario : [https://dd.meteo.gc.ca/air_quality/aqhi/ont/forecast/realtime/xml](https://dd.meteo.gc.ca/air_quality/aqhi/ont/forecast/realtime/xml)
    * Région des Prairies et du Nord : [https://dd.meteo.gc.ca/air_quality/aqhi/pnr/forecast/realtime/xml](https://dd.meteo.gc.ca/air_quality/aqhi/pnr/forecast/realtime/xml)
    * Région du Pacifique et Yukon : [https://dd.meteo.gc.ca/air_quality/aqhi/pyr/forecast/realtime/xml](https://dd.meteo.gc.ca/air_quality/aqhi/pyr/forecast/realtime/xml)
    * Région du Québec : [https://dd.meteo.gc.ca/air_quality/aqhi/que/forecast/realtime/xml](https://dd.meteo.gc.ca/air_quality/aqhi/que/forecast/realtime/xml)

Les fichiers XML en temps réel sont conservés sur le Datamart du SMC pendant 48 heures.

Un fichier qui permet aux systèmes automatisés d'accèder plus facilement aux [données mises à jour en temps-réel](https://dd.meteo.gc.ca/air_quality/doc/AQHI_XML_File_List.xml) est disponible. 

Une [liste complète des villes](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/aqhi/aqhi_station.geojson), avec les codes de [CGNDB](http://www4.rncan.gc.ca/recherche-de-noms-de-lieux/unique), données toponymiques du Canada maintenues par Ressources naturelles Canada, est disponible en format GeoJSON.

## Nomenclature des noms de fichiers 

NOTE : TOUTES LES HEURES SONT EN UTC.

* **Observations** (Noter: les fichiers « MONTHLY » ne sont pas disponibles encore) :
       
    * __Fichier horaire__ : AQ_OBS_CGNDBcode_AAAAMMJJhhmm.xml
    * __Copie du fichier d'observation le plus récent__ : AQ_OBS_CGNDBcode_CURRENT.xml
    
    où :
        
    * __'AQ_OBS'__ : Le préfixe du nom de fichier. Chaîne de caractères constante.
    * __CGNDBcode__ : Un [code de 5-caractères](http://www4.rncan.gc.ca/recherche-de-noms-de-lieux/unique) qui identifie chaque [communauté](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/aqhi/aqhi_community.geojson) CAS. 
    * __AAAA__ : Année de l'observation, 4 chiffres.
    * __MM__ : Mois de l'observation, 2 chiffres (janvier = 01).
    * __JJ__ : Jour de l'observation, 2 chiffres.
    * __hh__ : Heure de l'observation, 2 chiffres.
    * __mm__ : Minute de l'observation, 2 chiffres.

* **Prévisions publiques** (Noter: les fichiers « MONTHLY » ne sont pas disponibles encore) :

    * __Standard__:        AQ_FCST_CGNDBcode_AAAAMMJJhhmm.xml
    * __Amendements__ :     AQ_FCST_CGNDBcode_AAAAMMJJhhmm_AMD.xml
    * Copie du fichier de prévision le plus récent: AQ_FCST_CGNDBcode_CURRENT.xml )

    où :

    * __'AQ_FCST'__ : Le préfixe du nom de fichier. Chaîne de caractères constante.
    * __CGNDBcode__ : Un [code de 5-caractères](http://www4.rncan.gc.ca/recherche-de-noms-de-lieux/unique) qui identifie chaque [communauté](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/aqhi/aqhi_community.geojson) CAS. 
    * __AAAA__ : Année de l'émission, 4 chiffres.
    * __MM__ : Mois de l'émission, 2 chiffres (janvier = 01).
    * __JJ__ : Jour de l'émission, 2 chiffres.
    * __hh__ : Heure de l'émission, 2 chiffres.
    * __mm__ : Minute de l'émission, 2 chiffres.
    * __'AMD'__ :  Suffixe indiquant que le fichier est un amendement.

## Notes

* Les fichiers XML pour observations sont produits aux heures, environ 40 minutes après l'heure.
Ils sont disponibles sur le Datamart du SMC pour une période de 48 heures. Les fichiers XML pour les
prévisions publiques sont emisent deux fois par jour vers 06:00h et 17:00h heure locale. Ils sont
disponibles sur le Datamart du SMC pour une période de 48 heures.

* Les observations de qualité de l'air sont distribuées par les provinces et municipalités. Les juridictions provinciales contrôlent la façon dont les observations sont communiquées au public. Le Québec n'a pas autorisé la publication des données de qualité de l'air sous la forme de côte air santé (CAS). Ceci explique pourquoi on ne retrouve pas d'observation sous le répertoire : [https://dd.meteo.gc.ca/air_quality/aqhi/que/observation/](https://dd.meteo.gc.ca/air_quality/aqhi/que/observation/) . Cependant, le Minsitère du Développement durable, de l'Environnement et de lutte contre les Changements climatiques ainsi que la ville de Montréal distribuent aussi certaines de leurs données sur le portail américain AirNow: [https://www.airnowtech.org/index.cfm?page=login](https://www.airnowtech.org/index.cfm?page=login).

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : ec.dps-client.ec@canada.ca

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).
