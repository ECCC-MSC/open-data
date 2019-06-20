[In English](readme_aqhi-datamartcsv_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données ouvertes publiques du SMC](../readme_fr.md) > CAS sur le Datamart du SMC

# Données CSV d'observations et prévisions qui sont générés pour le programme Cote Air Santé (CAS)

La [cote air santé CAS](readme_aqhi_fr.md) est une échelle conçue pour quantifier la qualité de l'air dans une région donnée, sur une échelle de 1 à 10. La cote 10+ indique que la pollution de l'air est très élevée. La cote air santé comprend également une catégorie décrivant le risque pour la santé correspondant au nombre indiqué risque faible, modéré, élevé ou très élevé . La cote air santé est calculée en fonction des risques relatifs que représente une combinaison de polluants atmosphériques courants connus pour leurs effets néfastes sur la santé humaine, tels que l'ozone troposphérique, les matières particulaires et le dioxyde d'azote. La formulation de la cote air santé rend uniquement compte du risque pour la santé aigu ou à court terme contact en heures ou en jours au maximum .
Cette formulation pourrait changer avec le temps, pour rendre compte d'une nouvelle compréhension des effets de la pollution atmosphérique sur la santé. La cote air santé est calculée à partir de données observées en temps réel, sans vérification contrôle de la qualité.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le Protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage-overview/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTP. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier CSV.

Les données sont accessibles à adresse suivante :
* https://dd.meteo.gc.ca/air_quality/aqhi/

où :

![Description de la structure des répertoires](https://dd.meteo.gc.ca/air_quality/doc/aqhi_structure.png)

## Nomenclature des noms de fichiers 

NOTE: TOUTES LES HEURES SONT EN UTC.

__1. Les fichiers CSV :__

    1.1  Observations :
    
      Les fichiers « real-time » :                        AAAAMMJJhh_AQHI_REGION_OBSTYPE.csv
      Position: https://dd.meteo.gc.ca/air_quality/aqhi/[atl|ont|pnr|pyr|que]/observation/realtime/csv

      Les fichiers « MONTHLY » :                          AAAAMM_MONTHLY_AQHI_REGION_OBSTYPE.csv
      Position: https://dd.meteo.gc.ca/air_quality/aqhi/[atl|ont|pnr|pyr|que]/observation/monthly/csv

      Les fichiers « MONTHLY » avec données remblayées :  AAAAMM_MONTHLY_AQHI_REGION_OBSTYPE_BACKFILLED.csv
      Position: https://dd.meteo.gc.ca/air_quality/aqhi/[atl|ont|pnr|pyr|que]/observation/monthly/csv

où: 

* __AAAA__  : année de l'observation, 4 chiffres;
* __MM__    : mois de l'observation, 2 chiffres (janvier = 01);
* __JJ__    : jour de l'observation, 2 chiffres;
* __hh__ : heure de l'observation, 2 chiffres;
* __mm__ : minute de l'observation, 2 chiffres;
* __'MONTHLY'__ : symbole qui est présent lorsque le fichier contient des données pour le mois;
* __REGION__ : Nom de la région d'Environnement et Changement climatique Canada  où les observations sont situées. Les valeurs
possibles sont les suivantes:
    * 'ATL'= Région de l'Atlantique,
    * 'ON'= Région de l'Ontario,
    * 'PNR'= Région des prairies et du nord,
    * 'PYR'=Région du Pacifique et Yukon,
    * 'QC'= Région du Québec;
* __OBSTYPE__ : type d'observation dans le fichier. Les options possibles sont les suivants:
    * 'SiteObs'=le fichier contient les observations de CAS pour les communautés,
    * 'StationObs'= le fichier contient les observations de CAS pour les stations d'observation associées
    aux communautés (non disponible au mois de janvier 2012).
    * 'BACKFILLED': symbole qui est présent lorsque le fichier contient des observations de CAS qui
    ne sont pas calculées en temps-réel, mais qui sont calculées à partir des donnèes remblayées ou
    corrigées (reçues dans les 48 heures qui suivent l'heure de validité).

Note: Les fichiers CSV « real-time » sont produits aux heures et ils contiennent les données
pour les dernières 7 jours. Ils sont disponibles sur le Datamart pour une période de 8 jours.
Les fichiers CSV « MONTHLY » sont produits à la fin de chaque mois. Ils sont disponibles sur
le Datamart pour une période de 12 mois.

__1.2  Prévisions publiques :__
      
      Les fichiers mensuels :                             AAAAMM_MONTHLY_AQHI_CGNDBcode_SiteFcst.csv
      Position: https://dd.meteo.gc.ca/air_quality/aqhi/[atl|ont|pnr|pyr|que]/forecast/monthly/csv

where:

* __AAAA__ : année des prévisions, 4 chiffres;
* __MM__ : mois des prévisions, 2 chiffres (janvier = 01);
* __'MONTHLY'__ : symbole qui est présent lorsque le fichier contient des données pour le mois;
* __CGNDB_code__ : un code de 5-caractères qui identifie chaque communauté de la CAS. Une liste des codes
CGNDB est données à la fin de ce fichier.
* __'SiteFcst'__ : symbole qui est présent pour indiqué que le fichier contient prévisions de CAS pour une communauté.

__1.3  Données des modèles numériques :__

       CSV files :                               AAAAMMDDhh_SPECIES_REGION_MODELTYPE.csv
       Position : https://dd.weather.gc.ca/air_quality/aqhi/[atl|ont|pnr|pyr|que]/forecast/model/csv

where :

* __AAAA__ : année pour laquelle les données ont été générées, 4 chiffres;
* __MM__ : mois pour lequel les données ont été générées, 2 chiffres (January = 01);
* __DD__ : jour pour lequel les données ont été générées, 2 chiffres;
* __hh__ : heure pour laquelle les données ont été générées, 2 chiffres (00 ou 12 UTC);
* __'SPECIES'__ : nom de l'espèce chimique dans le fichier. Les options possibles sont les suivants:
    * 'O3'=ozone,
    * 'NO2'=dioxyde d'azote,
    * 'PM2.5'=particules d'un diamètre de moins de 2.5 um,
    * 'PM10'=particules d'un diamètre de moins de 10 um,
    * 'AQHI'=Cote air santé,
* __REGION__ : Nom de la région d'Environnement et Changement climatique Canada  pour laquelle les données sont valides. Les valeurs
possibles sont les suivantes:
    * 'ATL'= Région de l'Atlantique,
    * 'ON'= Région de l'Ontario,
    * 'PNR'= Région des prairies et du nord,
    * 'PYR'=Région du Pacifique et Yukon,
    * 'QC'= Région du Québec;
* __MODELTYPE__ : Indique le système utilisé pour générer les données. Les options possibles sont les suivants:
    * 'AQFM'=modèle de prévision de la qualité de l'air,
    * 'UMOSAQ'=le système de post-traitement "Updateable Model Output Statistics" appliqué aux sorties bruts de l'AQFM,
    * 'UMOSAQMIST'=les données combinées des systèmes AQFM et UMOSAQ; générées à fournir des informations additionelles
    aux météorologues car les données d'UMOSAQ ne sont pas toujours disponibles directement aux points d'observation.

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : ec.dps-client.ec@canada.ca

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).

















