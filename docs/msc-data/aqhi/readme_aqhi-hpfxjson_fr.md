[In English](readme_aqhi-hpfxjson_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [CAS](readme_aqhi_fr.md) > Données GeoJSON de CAS sur HPFX

# Données GeoJSON d'observations et prévisions qui sont générées pour le programme Cote Air Santé (CAS)

Cette page décrit les données d'observations et de prévisions disponibles en format GeoJSON pour la [cote air santé CAS](readme_aqhi_fr.md) qui sont aussi disponibles sur le [site web d'Environnement et Changement climatique Canada](https://meteo.gc.ca/airquality/pages/index_f.html). 

## Adresse des données 

Les données hébergées sur HPFX, le [serveur alternatif du Datamart du SMC](../../msc-datamart/readme_fr) peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier GeoJSON.

Les données sont accessibles pour les différentes provinces aux adresses suivantes :

* __Observations__ : [http://hpfx.collab.science.gc.ca/YYYMMDD/WXO-DD/air_quality/aqhi/[atl,ont,pnr,pyr,que]/observation/realtime/json](http://hpfx.collab.science.gc.ca/)
    
* __Prévisions publiques__ : [http://hpfx.collab.science.gc.ca/YYYMMDD/WXO-DD/air_quality/aqhi/[atl,ont,pnr,pyr,que]/forecast/realtime/json](http://hpfx.collab.science.gc.ca/)

Avec:

    * atl: région de l'Atlantique
    * ont: région de l'Ontario
    * pnr: région des Prairies et du Nord
    * pyr: région du Pacifique et Yukon
    * que: région du Québec

Une [liste complète des villes](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/aqhi/aqhi_station.geojson), avec les codes de [CGNDB](http://www4.rncan.gc.ca/recherche-de-noms-de-lieux/unique), données toponymiques du Canada maintenues par Ressources naturelles Canada, est disponible en format GeoJSON.

## Nomenclature des noms de fichiers 

NOTE : TOUTES LES HEURES SONT EN UTC.

Les noms de fichiers ont la nomenclature suivante :

* __Observations__ :
       
    {YYYYMMDD}T{HH}{mm}Z_MSC_AQHI-Observation_{CGNDBcode}.json
    
Avec :

    * YYYYMMDD : Année, mois et jour de l'observation
    * T : Délimiteur temporel selon les normes ISO8601
    * H : Heure UTC de l'observation
    * mm : minute de l'observation
    * Z : Fuseau horaire (heure UTC)     
    * MSC : Chaîne de caractères constante pour Meteorological Service of Canada, la source des données 
    * AQHI : Chaîne de caractères constante pour "Air Quality Health Index"
    * Observation : Chaîne de caractères constante pour observations de la Côte Air Santé
    * CGNDBcode : Un [code de 5-caractères](http://www4.rncan.gc.ca/recherche-de-noms-de-lieux/unique) qui identifie chaque [communauté](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/aqhi/aqhi_community.geojson) CAS. 
    * json : Chaîne de caractères constante indiquant que le format est GeoJSON

* __Prévisions publiques__

    {YYYYMMDD}T{HH}{mm}Z_MSC_AQHI-Forecasts_{CGNDBcode}.json     
    
Avec :

 * YYYYMMDD : Année, mois et jour du début de l'émission
 * T : Délimiteur temporel selon les normes ISO8601
 * HH : Heure UTC de l'émission  
 * mm : Minute de l'émission
 * Z : Fuseau horaire (heure UTC)
 * MSC : Chaîne de caractères constante pour Meteorological Service of Canada, la source des données       
 * AQHI : Chaîne de caractères constante pour "Air Quality Health Index"
 * Forecasts : Chaîne de caractères constante pour prévisions de la Côte Air Santé
 * CGNDBcode : Un [code de 5-caractères](http://www4.rncan.gc.ca/recherche-de-noms-de-lieux/unique) qui identifie chaque [communauté](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/aqhi/aqhi_community.geojson) CAS. 
 * json : Chaîne de caractères constante indiquant que le format est GeoJSON

## Notes

* Les fichiers d'observations GeoJSON sont produits aux heures, environ 40 minutes après l'heure. Les fichiers GeoJSON pour les prévisions publiques sont emis deux fois par jour vers 06:00h et 17:00h heure locale.

* Lorsque les données de prévision sont amendées, un paramètre associé au statut du fichier est mis à jour en conséquence dans le fichier GeoJSON.

* Les observations de qualité de l'air sont distribuées par les provinces et municipalités. Les juridictions provinciales contrôlent la façon dont les observations sont communiquées au public. Le Québec n'a pas autorisé la publication des données de qualité de l'air sous la forme de côte air santé (CAS). Ceci explique pourquoi on ne retrouve pas d'observation sous le répertoire : [http://hpfx.collab.science.gc.ca/YYYMMDD/WXO-DD/air_quality/aqhi/que/observation/realtime/json](http://hpfx.collab.science.gc.ca). Cependant, le Ministère du Développement durable, de l'Environnement et de lutte contre les Changements climatiques ainsi que la ville de Montréal distribuent aussi certaines de leurs données sur [le portail américain AirNow](https://www.epa.gov/outdoor-air-quality-data/download-daily-data).

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).
