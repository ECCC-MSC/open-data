[In English](readme_hrepa-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [AHREP](readme_hrepa_fr.md) > AHREP sur DD-Alpha du SMC

# Données NetCDF de l'Analyse à haute résolution ensembliste de précipitation (AHREP)

Cette page décrit les données expérimentales de l'[Analyse à haute résolution ensembliste de précipitation (AHREP)](readme_hrepa_fr.md) disponibles en format NetCDF sur le serveur DD-Alpha, le site Web d'essai de données du Datamart du SMC.

## Adresse des données 

Les données du serveur DD-Alpha, le site Web d'essai de données du Datamart du SMC, peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier netCDF. 

Les données sont accessibles à l'adresse suivante:

* [https://dd.alpha.meteo.gc.ca/model_hrepa/2.5km/{HH}](https://dd.alpha.meteo.gc.ca/model_hrepa/2.5km)

où :

* __HH__ : Heure de validité de l'analyse, en UTC [00, 06, 12, 18]

## Spécification technique de la grille

![image de la grille HREPA](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_hrepa/grille_hrepa.png)

Ce tableau décrit des paramètres de la grille latitude-longitude sur laquelle les variables en format netCDF sont disponibles.

| Paramètre de la grille                                          | Valeur du paramètre      |
|-----------------------------------------------------------------|--------------------------|
| ni                                                              | 2438                     |
| nj                                                              | 1188                     |
| résolution                                                      | 0.0225°                  |
| coordonnées du premier point de grille                          | 41.0269° N ; 132.5993° W |
| orientation de la grille (par rapport à l’axe des j)            | -115.0°                  |

## Nomenclature des noms de fichiers 

NOTE : TOUTES LES HEURES SONT EN UTC.

Les fichiers ont la nomenclature suivante :

`{AAAAMMJJ}T{HH}Z_MSC_HREPA_{Var}_Sfc_{Grille}{resolution}_PT0H.nc`

où : 

* __AAAAMMJJ__ : Année (AAAA), mois (MM) et jour (JJ) de validité de l'analyse (ex: 20220214)
* __T__ : Délimiteur de temps selon les normes ISO8601
* __HH__ : heure de validité de l'analyse en UTC [00, 06, 12, 18]
* __Z__ : Fuseau horaire (UTC hour)
* __MSC__: Chaîne constante indiquant que les données proviennent du Service météorologique du Canada 
* __HREPA__: Chaîne constante indiquant que les données provient du système d'Analyse à haute résolution ensembliste de précipitation
* __Var__ : Variable contenu dans le fichier. Voir la liste ci-dessous
* __Sfc__: Chaîne constante indiquant que le type de niveau est la surface
* __Grille__ : Chaîne constante indiquant une grille lat-lon tournée
* __resolution__ : Chaîne constante indiquant une résolution en degré de 0.0225° (environ 2.5 km) dans les directions de la latitude et de la longitude
* __PT0H__: Chaîne de caractères constante indiquant une analyse, basée sur les normes ISO8601. P, T et H sont des caractères constants désignant la période, le temps et l'heure.
* __nc__ : Chaîne de caractères constante indiquant que le format est NetCDF

Exemple de fichier :

20220214T06Z_MSC_HREPA_Precip-Accum06h_Sfc_RLatLon0.0225_PT0H.nc

Ce fichier provient du Service météorologique du Canada et contient des données de l'Analyse à haute résolution ensembliste de précipitation (AHREP). C'est une analyse de précipitation sur des cumuls de 6 heures dont la période de cumul débute le 20220214 à 00UTC et se termine le 20220214 à 6UTC. Ce fichier contient 25 membres, le premier membre est le controle et correspondant à une analyse déterministe (sans perturbation) alors que les 24 autres membres sont les analyses obtenues après perturbations des intrants.

À noter qu'une deuxième variable est également incluse dans ce fichier, soit l'indice de confiance de l'analyse (CFIA).

## Liste des variables

Trois type de fichiers existent pour chaque heure de validité de AHREP, et chaque fichier contient des variables spécifiques, décrites ci-dessous, pour les produits d'ensemble disponibles. Pour chaque type de fichier, les variables, la définition, la période et la fréquence de disponibilité sont mentionnées.

* Pour les fichiers de type "Precip-Accum06h"

    * __pr__ : Ensemble des 25 membres d'analyse de précipitation , accumulées sur une période de 6 heures et disponibles aux heures synoptiques (mm)
    * __cfia__ : Indice de Confiance de l'Analyse du membre controle de l'ensemble. Plage de valeurs de 0 à 1 (sans unité), disponible aux heures synoptiques (mm)
    
* Pour les fichiers de type "Precip-Accum06h-Pct25"

    * __q025__ : 25ème percentile estimé sur l'ensemble des analyses de précipitation accumulées sur une période de 6 heures, disponible aux heures synoptiques (mm)
    
* Pour les fichiers de type "Precip-Accum06h-Pct75"

    * __q075__ : 75ème percentile estimé sur l'ensemble des analyses de précipitation accumulées sur une période de 6 heures, disponible aux heures synoptiques (mm)


## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).




























