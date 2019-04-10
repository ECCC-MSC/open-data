Gabarit de documentation d'un jeu de données publiques
==========================================================

Courte description. Exemple inspiré du HRDPA : "Documentation des données de l'Analyse à haute résolution déterministe de précipitation (AHRDP) produites par le Environnement et changement climatique Canada."

## Table des matières

* [Description](#Description)
* Accès
  * License
  * Métadonnées
  * [Accès aux données brutes](#acces-aux-donnees-brutes)
  * Accès par service web
* Produits
* Documentation technique
* Registre des changements

## Description

Quelques lignes décrivant sommairement les données (pour les systèmes NWP, donner l'acronyme), inspirées de la section "A propos" des README sur le Datamart du SMC.

> *Exemple pour le SRPD*:

> *Données du Système régional de prévision déterministe (SRPD). Le modèle de prévision numérique du temps tourne sur une grille de résolution de 10 km au cœur de la grille. Les champs du jeu de données GRIB2 à haute résolution sont disponibles 4 fois par jour, sur une grille polaire stéréographique de 935 x 824 points couvrant l’Amérique du Nord et les eaux environnantes avec une résolution de 10 km à 60 degrés nord.*

* NOTE : la description utilisée ici devrait être la même que celle utilisée dans les métadonnées ? Oui ! [Source des descriptions](https://gccode.ssc-spc.gc.ca/ec-msc/discovery-metadata/tree/master/mcf)

## Accès

### Licence

Rappel de la licence et lien vers celle-ci

### Métadonnées

Lien vers les métadonnées de ce jeu de données sur open.canada.ca

> *Exemple pour le SRPD*: [*Métadonnées des Prévisions Numériques du Temps (PNT)*](http://donnees-data.intranet.ec.gc.ca/geonetwork/metadata/fre/692e7cc2-e545-45bb-bf7e-e1b725250b7a)

### Accès aux données brutes

* Liens vers la page de doc du Datamart ../msc-datamart/readme.md
* Lien vers une sous-page décrivant les fichiers (nomenclature, contenu, grilles et niveaux pour les systèmes NWP, descriptions des variables, format de données, période de rétention sur le Datamart, etc.). Reprendre les descriptions des README. Lien vers le Datamart du SMC. Accès AMQP et lien vers page AMQP ../msc-datamart/amqp_en.md

### Service web GeoMet du SMC

* Lien vers d'accueil de GeoMet du SMC ../msc-geomet/readme.md
* Lien vers la sous-page de l'accès à ces données via GeoMet, incluant la liste des couches disponibles pour les données en question


## Produits

Liste et liens vers les produits disponibles pour ce jeu de données.

>*Exemples pour le SRPD*:
>- *Prévisions à l'aviation*
>  - [*Carte 4 panneaux*](http://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/product-pages/difax_reg_prog_aviation-package_avn_f.html)
>  - [*Plafond nuageux*](http://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/product-pages/difax_reg_prog_4-panel-ceilings_avn_f.html)
>  - *Etc.*
>- *Temps violent*
>  - [*Indices Showalter et SWEAT*](http://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/product-pages/difax_reg_prog_showalter-sweat-indices_ssw_f.html)
>  - [*Aide à la prévision de précipitation verglaçante*](http://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/product-pages/difax_reg_prog_low-level-thickness-msl-precip_wsw_f.html)
>  - *Etc.*

## Documentation technique

- Liens vers les documents techniques des données
- Liens vers articles scientifiques

>*Exemple pour le SRPD*:
>- [*Version 5.0.0 du Système régional de prévision déterministe du SMC*](http://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_RDPS_f.pdf)
>- [*Note technique*](http://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/lib/technote_rdps-500_20160907_f.pdf)

## Registre des changements

Lien vers a page du journal des changements (actuellement dans le Guide des produits du CMC)

>*Exemple pour le SRPD*: [*Chronologie des changements au SRPD*](http://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/submenus/rdps_f.html#chronologychanges)

Autre option : ajouter des liens vers les annonces de dd-info qui détaillent ces changements ?
