[In English](readme_hydrometric-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données ouvertes publiques du SMC](../readme_fr.md) > Données hydrométriques sur le Datamart du SMC

# Données hydrométriques en temps réel en format CSV

Cette page décrit les données [hydrométriques en temps réel](readme_hydrometric_fr.md) disponibles en format CSV.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage-overview/readme_fr.md) est également disponible.
Les données sont disponibles via le protocole HTTP. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier CSV. Nous vous recommandons d’automatiser le téléchargement en le scriptant avec wget (lien externe, anglais) ou un programme équivalent. Pour plus d’information sur wget, consultez les notes d’utilisation.

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

* __PROVTERR__ : Code de la province ou du territoire à 2 lettres.

* __ID__ : Identifiant de la station.

* __MAJ__ : "daily" ou "hourly" pour la fréquence de mise à jour.

Exemple : 

"AB_05AA004_hourly_hydrometric.csv" pour les données d'observations mises à 
jour chaque heure pour la station "05AA004" située en Alberta (AB) en format 
CSV.

__Fichier de province__

Un fichier contenant toutes les stations d'une province est disponible pour 
faciliter l'usage. Il a un nom statique qui obéit aux règle suivantes :

[PROVTERR]_[MAJ]_hydrometric.csv

où :

* __PROVTERR__ : Code de la province ou du territoire à 2 lettres.

* __MAJ__ : "daily" ou "hourly" pour la fréquence de mise à jour.

Exemple:

"ON_daily_hydrometric.csv" pour les données d'observations mises à jour chaque 
jour pour toutes les stations situées en Ontario (ON) en format CSV.

## Description des données

### Fichier de données

Les données hydrométriques en temps réel sont présentées dans un format CSV pour la distribution par Environnement et Changement climatique Canada.

Les fichiers mis à jour sur une base horaire contiennent les 2 derniers jours complets en plus du jour courant incomplet. Les fichiers mis à jour sur une base quotidienne contiennent les 30 derniers jours complets en plus du jour courant incomplet.

La première ligne est une entête bilingue suivie des enregistrements. Voici la description des titres français des colonnes : 

ID,Date,Niveau d'eau (m),Grade,Symbole,QA/QC,Débit (cms),Grade,Symbole,QA/QC

où : 
*  __ID__ : Identifiant de la station. Les deux premiers chiffres indiquent le 
bassin hydrographique principal dans lequel se trouve la station. Les 
deux prochains caractères indiquent le sous-bassin et le 
sous-sous-bassin. Les trois derniers chiffres indiquent la station 
spécifique dans le sous-sous-bassin.

* __Date__ : Date de l'observation au format ISO 8601, heure normale locale (HNL).

* __Niveau d'eau (m)__ : Niveau d'eau en mètres.

* __Grade__ : Usage futur.

* __Symbole__ : Usage futur.

* __QA/QC__ : Drapeau de l'assurance de la qualité/contrôle de la qualité pour le 
niveau d'eau (1 = préliminaire, 2 = révisé, 3 = vérifié, 4 = approuvé).

* __Débit (cms)__ : Débit en mètres cube par seconde.

* __Grade__ : Usage futur.

* __Symbol__ : Usage futur.

* __QA/QC__ : Drapeau de l'assurance de la qualité/contrôle de la qualité pour le 
          débit (1 = préliminaire, 2 = révisé, 3 = vérifié, 4 = approuvé).

Veuillez prendre note que les dates des données sont toujours en HNL à chaque station. Les dates affichent l'écart avec le temps universel coordonné (UTC).


### Liste des stations

Une [liste des stations hydrométriques en temps réel](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_hydrometric/hydrometric_StationList.geojson), en format GeoJSON, est disponible.

La première ligne est une entête bilingue suivie des métadonnées des stations. Voici la description des titres français des colonnes : 

ID,Nom,Latitude,Longitude,Prov/Terr,Timezone

où :
*  __ID__ : Identifiant de la station.

* __Nom__ : Nom de la station. Le nom est soit en anglais ou en français dépendamment de l'emplacement de la station.

* __Latitude__ : Latitude en format décimal.

* __Longitude__ : Longitude en format décimal.

* __Prov/Terr__ : Code de la province ou du territoire à 2 lettres.

* __Fuseau horaire__ : Différence entre HNL et UTC.

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : ec.dps-client.ec@canada.ca

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).
