
[In English](readme_rdsps-datamart_en.md)

![ECCC logo](../../../docs/img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [SRPDOT](readme_rdsps_fr.md) > SRPDOT sur le Datamart du SMC

# Données NetCDF du Système Régional de Prévision Déterministe d'Onde de Tempête (SRPDOT)

Cette page décrit les données [Système Régional de Prévision Déterministe d'Onde de Tempête (SRPDOT)](readme_rdsps_fr.md) disponibles en format NetCDF.

## Adresse des données

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTP. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier NetCDF.

Les données sont accessibles à adresse suivante :

* [https://dd.weather.gc.ca/model_surge/nw-atlantic/netcdf/{HH}/](https://dd.weather.gc.ca/model_surge/nw-atlantic/netcdf)

where :

* __HH__ : Model run start, in UTC [00 or 12]

Un historique de 24 heures est conservé dans ce répertoire.

## Spécification technique de la grille

Ce tableau répertorie les valeurs de divers paramètres de la grille globale SGPDV :

| Paramètre | Valeur |
| ------ | ------ |
| ni | 841 |
| nj | 541 |
| résolution | 0.033° x 0.033° |

## Nomenclature des noms de fichiers
NOTE: TOUTES LES HEURES SONT EN UTC.

Les noms de fichiers ont la nomenclature suivante :

CMC_rdsps_domain_Variable_LevelType_level_latlond.dddxd.ddd_YYYYMMDDTHHZ_Phhh.nc

où :

* CMC : Chaîne de caractères constante indiquant que le Centre météorologique canadien (CMC) émet les prévisions
* rdsps : Chaîne de caractères constante indiquant que les données proviennent du Système régional de prévision déterministe d'onde de tempête
* domain : Chaîne de caractères constante indiquant le domaine
* Variable : Type de variable contenue dans le fichier
* LevelType : Type de niveau
* Level : Valeur du niveau
* latlond.dddxd.ddd : Chaîne de caractères constante indiquant que la projection utilisée est lat/long à une résolution de d.ddd x d.ddd degré
* YYYYMMDD : Année, mois et jour du début de la prévision
* HH : heure UTC du début de la passe `[00, 06, 12, 18]`
* Phhh : P est un caractère constant. hhh représente l’heure de prévision `[000, 001, 002, ..., 240]`
* nc : Chaîne de caractères constante indiquant que le format est NetCDF
* T: séparateur entre la date et l'heure
* Z: indicateur du fuseau horaire

Exemple de fichier :

CMC_rdsps_nw-atlantic_etas_sfc_0_latlon0.033x0.033_20180417T12Z_P024.nc

Le fichier a été créé par le CMC et contient une prévision du Système régional
de prévision déterministe d'onde de tempête. Il contient la hauteur d'onde de tempête (etas) pour le nord-ouest de l'océan Atlantique au niveau de la surface sur une grille
lat/long à une résolution de 0.033 degré par 0.033 degré. Il débute le 17
avril 2018 à 12Z (2018041712). Il contient l’heure de prévision 24 (P024) en
format NetCDF (.nc).


## Niveaux

Niveaux qui pourraient être applicables à certains champs :

* sfc : surface


##   Liste de variables

La liste ci-dessous fournit pour chaque identifieur de paramètre NetCDF: une
brève description, une abréviation alphabétique, les niveaux pour lesquels ce
paramètre est disponible et les unités de mesure.


| NetCDF |   Description courte |                        Abr.|   Niveau | Unités|
|--------|--------|--------|--------|--------|
| etas   |  Onde de tempête     |                      ETAS  |  sfc_0 | m |


##   Contenu des fichiers

Les données dans les fichiers sont en format NetCDF conformes aux conventions CF liées au
climat et aux prévisions (Climate and Forecast Conventions) pour faciliter la distribution et la manipulation.

NetCDF est un format de fichier pour l’entreposage et la transmission de données
météorologiques sur grille telles que des sorties de modèles de prévision
numérique du temps. Il a été conçu pour être autodescriptif, compact et portable
entre les architectures informatiques. Le standard NetCDF a été conçu et est
maintenu par  University Corporation for Atmospheric Research (UCAR).

Des informations à propos de ce format et des logiciels pour le manipuler et le visualiser sont disponibles ici:
https://www.unidata.ucar.edu/software/netcdf/docs/index.html

Conventions CF:
http://cfconventions.org/



## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Annonces de la liste de diffusion dd_info

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).
