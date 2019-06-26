[In English](readme_hydrometric-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données ouvertes publiques du SMC](../readme_fr.md) > Données hydrométriques sur le Datamart du SMC

# Données hydrométriques en temps réel en format CSV

Cette page décrit les données [hydrométriques en temps réel](readme_hydrometric_fr.md) disponibles en format CSV.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le Protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage-overview/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTP. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier GRIB2. Nous vous recommandons d’automatiser le téléchargement en le scriptant avec wget (lien externe, anglais) ou un programme équivalent. Pour plus d’information sur wget, consultez les notes d’utilisation.

Les fichiers pour ces données se trouvent à l'adresse :
* https://dd.meteo.gc.ca/hydrometric/[PROVTERR]/[MAJ]/

où :
* __[PROVTERR]__ : code de la province ou du territoire à 2 lettres. Le code est 
l'une des 13 valeurs suivantes :
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

* __[MAJ]__ : "daily" ou "hourly" pour la fréquence de mise à jour

## Nomenclature des noms de fichiers 

NOTE: TOUTES LES HEURES SONT EN UTC.

__Fichier de station__

Chaque fichier de données hydrométriques en temps réel a un nom statique qui
obéit aux règles suivantes :

[PROVTERR]_[ID]_[MAJ]_hydrometric.csv

où :

* __PROVTERR__ : code de la province ou du territoire à 2 lettres

* __ID__ : identifiant de la station

* __MAJ__ : "daily" ou "hourly" pour la fréquence de mise à jour

Exemple: 

"AB_05AA004_hourly_hydrometric.csv" pour les données d'observations mises à 
jour chaque heure pour la station "05AA004" située en Alberta (AB) en format 
CSV.

__Fichier de province__

Un fichier contenant toutes les stations d'une province est disponible pour 
faciliter l'usage. Il a un nom statique qui obéit aux règle suivantes :

[PROVTERR]_[MAJ]_hydrometric.csv

où :

* __PROVTERR__ : code de la province ou du territoire à 2 lettres

* __MAJ__ : "daily" ou "hourly" pour la fréquence de mise à jour

Exemple:

"ON_daily_hydrometric.csv" pour les données d'observations mises à jour chaque 
jour pour toutes les stations situées en Ontario (ON) en format CSV.

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : ec.dps-client.ec@canada.ca

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).
