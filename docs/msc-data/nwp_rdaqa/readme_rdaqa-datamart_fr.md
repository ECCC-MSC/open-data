[In English](readme_rdaqa-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [ARDQA](readme_rdaqa_fr.md) > Analyse régionale déterministe de la qualité de l'air sur le Datamart du SMC

# Données GRIB2 de l'Analyse régionale déterministe de la qualité de l'air (ARDQA)

Cette page décrit les données de l'[Analyse régionale déterministe de la qualité de l'air (ARDQA)](readme_rdaqa_fr.md) en format GRIB2 sur le Datamart du SMC. Ce système est exécuté aux heures afin de produire des analyses pour certains polluants tels que l’ozone (O3), le dioxyde d’azote (NO2) ou encore les matières particulaires dont le diamètre aérodynamique est inférieur à 2.5 μm (PM2.5), sur une grille nord-américaine.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le Protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont accessibles à l'adresse suivante :

* [https://dd.meteo.gc.ca/model_rdaqa/10km/{HH}](https://dd.meteo.gc.ca/model_rdaqa/10km)

où :

* __HH__ : Heure en UTC du temps de validité de l'analyse [00, 01, 02, ..., 20, 21]

Un historique de 24 heures est conservé dans ce répertoire.

## Spécification technique de la grille  

![Image du domaine RDAQA](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_raqdps-fw/grille_raqdps-fw.png)

Valeurs données aux paramètres de la grille lat-lon tournée :

| Paramètre | Valeur |
| ------ | ------ |
| ni | 729 |
| nj | 599 | 
| résolution à 60° N | 10km |
| coordonnées du premier point de grille (relatives à la grille utilisée) | 32 ° S ; 39.5 ° W | 

__Note__ : Les [versions les plus récentes de wgrib2](https://www.cpc.ncep.noaa.gov/products/wesley/wgrib2/update_2.0.8.html) et [GDAL](https://gdal.org/) supportent ces grilles tournées. 

## Nomenclature des noms de fichiers 

La nomenclature des noms des fichiers est la suivante :

`{YYYYMMDD}T{HH}Z_MSC_{SYSTEM}_{VAR}_{LVLTYPE}_{grille}{resolution}_PT0H.grib2`

où :

* __YYYYMMDD__ : Année, mois et jour du début de la prévision
* __T__ : Délimiteur temporel selon les normes ISO8601
* __HH__ : Heure en UTC du temps de validité de l'analyse [00, 01, 02, ...., 20, 21] 
* __Z__ : Fuseau horaire (heure UTC)
* __MSC__ : Chaîne de caractères constante pour Meteorological Service of Canada, la source des données
* __SYSTEM__ : Chaîne de caractères constante indiquant le système à partir duquel l'analyse a été générée [RDAQA; RDAQA-Prelim pour le temps de coupure des observations à l'intérieur d'une heure après l'heure YYYYMMDDHH, indiquant que toutes les observations n'ont possiblement pas été recueillies; RDAQA-FW pour l'analyse générée à partir du système SRPDQA-FW]
* __VAR__ : Variables contenues dans le fichier (voir section ci-dessous).
* __LVLTYPE__ : Type de niveau vertical [Sfc pour la surface]
* __grille__ : Grille horizontale [RLatLon]
* __resolution__ : Indique la résolution en degré dans les directions longitudinale et latitudinale soit ici 0.09 (environ 10km) dans les deux directions
* __PT0H__ : Echéance temporelle selon la norme [ISO8601](https://en.wikipedia.org/wiki/ISO_8601). P, T et H sont des caractères constants désignant Période, Temps et Heure. Ici,PT0H indique une analyse.
* __grib2__ : Chaîne de caractères constante indiquant que le format est GRIB2

Exemples :

* 20230808T04Z_MSC_RDAQA-Prelim_PM10_Sfc_RLatLon0.09_PT0H.grib2
* 20230808T04Z_MSC_RDAQA_PM10_Sfc_RLatLon0.09_PT0H.grib2
* 20230808T04Z_MSC_RDAQA-FW_PM10_Sfc_RLatLon0.09_PT0H.grib2

## Liste des variables

Liste des variables 2D disponibles dans les fichiers:

* PM2.5 : Concentration des PM2.5 (&mu;g.m-3)
* PM10 : Concentration des PM10 (&mu;g.m-3)
* NO : Monoxyde d'azote (ppb)
* NO2 : Dioxyde d'azote (ppb)
* O3 : Ozone (ppb)
* SO2 : Dioxyde de sulfure (ppb)

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).

