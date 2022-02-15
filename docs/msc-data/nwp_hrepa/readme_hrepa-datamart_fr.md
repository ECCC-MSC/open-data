[In English](readme_hrepa-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [AHREP](readme_geps_fr.md) > AHREP sur le Datamart du SMC

# Données netCDF de l'Analyse à Haute Résolution Ensembliste de Précipitation (AHREP)

Cette page décrit les données de l'[Analyse à Haute Résolution Ensembliste de Précipitation (AHREP)](readme_hrepa_fr.md) disponibles en format netCDF.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le Protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier netCDF. 

Les données sont accessibles aux adresses suivantes :

* [https://dd.meteo.gc.ca/model_hrepa/{AC}](https://dd.meteo.gc.ca/model_hrepa/)

où :
* __AC_ : Période d'accumulation en heure: 06

## Spécification technique de la grille

Ce tableau décrit des paramètres de la grille latitude-longitude sur laquelle les variables en format netCDF sont disponibles.

| Paramètre de la grille                                          | Valeur du paramètre      |
|-----------------------------------------------------------------|--------------------------|
| ni                                                              | 2560 points              |
| nj                                                              | 1310 points              |
| résolution                                                      | 0,0225°                  |
| coordonnées du premier point de grille                          | 42.2504° N ; 131.0928° W |
| orientation de la grille (par rapport à l’axe des j)            | -115.0°                  |

## Nomenclature des noms de fichiers 

NOTE : TOUTES LES HEURES SONT EN UTC.

Les fichiers ont la nomenclature suivante :
* `<AAAAMMJJ>T<HH>_MSC_HREPA_<Variable>_Sfc_<grille>RLatLon0.0225.nc`

où : 

* __AAAAMMJJ__ : Date de validité de l'analyse: AAAA=Année, MM=Mois, JJ=Jour (ex: 20220214)
* __HH__ : heure de validité de l'analyse en UTC
* __MSC__: Les données sont produites par le *Meteorological Service of Canada* (Chaîne constante)
* __HREPA__: Analyse ensembliste de précipitation Chaîne constante)
* __Variable__ : Type de variable contenu dans le fichier. Pour voir la liste complète, consultez la section « Description des variables »
* __Sfc__: Variable de surface (Chaîne constante)
* __RLatLon__ :Le type de projection est polaire-stéréographique (Chaîne constante)
* __0.0225__ : Chaîne de caractères constante indiquant la résolution des données en degrée
* __nc__ : Chaîne de caractères constante indiquant que le format est netCDF (Chaîne constante)


Exemple de nom de fichier :
20220214T06Z_MSC_HREPA_Precip-Accum06h_Sfc_RLatLon0.0225.nc

Ce fichier provient du Service météorologique du Canada et contient des données de l'Analyse à Haute Résolution Ensembliste de Précipitation (AHREP). C'est une analyse de précipitation sur des cumuls de 6 heures dont la période de cumul débute le 20220214 à 00UTC et se termine le 20220214 à 6UTC. Ce fichier contient 25 membres, le premier membre est le controle et correspondant à une analyse déterministe (sans perturbations) alors que les 24 autres membres sont les analyses obtenues après perturbations des intrants.

À noter qu'une deuxième variable est également incluse dans ce fichier, soit l'indice de confiance de l'analyse (CFIA).

## Liste des variables
Les variables pour les produits d'ensemble disponibles dans les fichiers netCDFs sont décrites ci-dessous. Pour chaque variable, la définition, la période et la fréquence de disponibilité sont mentionnées.

Pour la variable Precip-Accum06h
* __pr__ : Ensemble des analyse de la quantité totale de précipitation , disponible aux heures synoptiques (mm)
* __cfia__ : Indice de Confiance de l'Analyse. Plage de valeurs de 0 à 1 (sans unité), disponible aux heures synoptiques (mm)

Pour la variable Precip-Accum06h-Pct25
* __q025__ : 25eme percentile de l'ensemble des analyse de la quantité totale de précipitation , disponible aux heures synoptiques (mm)

Pour la variable Precip-Accum06h-Pct75
* __q075__ : 75eme percentile de l'ensemble des analyse de la quantité totale de précipitation , disponible aux heures synoptiques (mm)


## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).




























