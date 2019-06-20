[In English](readme_aqhi-datamartxml_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données ouvertes publiques du SMC](../readme_fr.md) > CAS sur le Datamart du SMC

# Données XML d'observations et prévisions qui sont générés pour le programme Cote Air Santé (CAS)

La [cote air santé CAS](readme_aqhi_fr.md) est une échelle conçue pour quantifier la qualité de l'air dans une région donnée, sur une échelle de 1 à 10. La cote 10+ indique que la pollution de l'air est très élevée. La cote air santé comprend également une catégorie décrivant le risque pour la santé correspondant au nombre indiqué risque faible, modéré, élevé ou très élevé . La cote air santé est calculée en fonction des risques relatifs que représente une combinaison de polluants atmosphériques courants connus pour leurs effets néfastes sur la santé humaine, tels que l'ozone troposphérique, les matières particulaires et le dioxyde d'azote. La formulation de la cote air santé rend uniquement compte du risque pour la santé aigu ou à court terme contact en heures ou en jours au maximum .
Cette formulation pourrait changer avec le temps, pour rendre compte d'une nouvelle compréhension des effets de la pollution atmosphérique sur la santé. La cote air santé est calculée à partir de données observées en temps réel, sans vérification contrôle de la qualité.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le Protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage-overview/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTP. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier XML.

Les données sont accessibles à adresse suivante :
* https://dd.meteo.gc.ca/air_quality/aqhi/

où :

![Description de la structure des répertoires](https://dd.meteo.gc.ca/air_quality/doc/aqhi_structure.png)

## Nomenclature des noms de fichiers 

NOTE: TOUTES LES HEURES SONT EN UTC.

__1. Les fichiers XML :__

    1.1  Observations (Noter: les fichiers « MONTHLY » ne sont pas disponibles encore):
       Fichier horaire: AQ_OBS_CGNDBcode_AAAAMMJJhhmm.xml
                        AQ_OBS_CGNDBcode_CURRENT.xml (copie du fichier d'observation le plus récent)
       Position: https://dd.meteo.gc.ca/air_quality/aqhi/[atl|ont|pnr|pyr|que]/observation/realtime/xml

où:

* **'AQ_OBS_'** : le préfixe du nom de fichier. Chaîne de caractères constante.
* __CGNDBcode__ : un code de 5-caractères qui identifie chaque communauté CAS. Une liste des codes
CGNDB est données à la fin de ce fichier.
* __AAAA__  : année de l'observation, 4 chiffres;
* __MM__    : mois de l'observation, 2 chiffres (janvier = 01);
* __JJ__    : jour de l'observation, 2 chiffres;
* __hh__ : heure de l'observation, 2 chiffres;
* __mm__ : minute de l'observation, 2 chiffres;


__1.2  Prévisions publiques (Noter: les fichiers « MONTHLY » ne sont pas disponibles encore) :__

       Standard:        AQ_FCST_CGNDBcode_AAAAMMJJhhmm.xml
       Amendements:     AQ_FCST_CGNDBcode_AAAAMMJJhhmm_AMD.xml
                        AQ_FCST_CGNDBcode_CURRENT.xml (copie du fichier de prévision le plus récent)
       Position: https://dd.meteo.gc.ca/air_quality/aqhi/[atl|ont|pnr|pyr|que]/forecast/realtime/xml

où:

* **'AQ_FCST_'** : le préfixe du nom de fichier. Chaîne de caractères constante.
* __CGNDBcode__ : un code de 5-caractères qui identifie chaque communauté CAS. Une liste des codes
CGNDB est données à la fin de ce fichier.
* __AAAA__  : année de l'émission, 4 chiffres;
* __MM__    : mois de l'émission, 2 chiffres (janvier = 01);
* __JJ__    : jour de l'émission, 2 chiffres;
* __hh__ : heure de l'émission, 2 chiffres;
* __mm__ : minute de l'émission, 2 chiffres;
* __'AMD'__ :  suffixe indiquant que le fichier est un amendement.

Note : Les fichiers XML pour observations sont produits aux heures, environ 40 minutes après l'heure.
Ils sont disponibles sur le Datamart pour une période de 48 heures. Les fichiers XML pour les
prévisions publiques sont emisent deux fois par jour vers 06:00h et 17:00h heure locale. Ils sont
disponibles sur le Datamart pour une période de 48 heures.

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : ec.dps-client.ec@canada.ca

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).

















