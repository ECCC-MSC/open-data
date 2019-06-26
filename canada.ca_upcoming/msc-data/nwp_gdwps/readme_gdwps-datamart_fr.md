[In English](readme_gdwps-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données ouvertes publiques du SMC](../readme_fr.md) > SGPDV sur le Datamart du SMC

# Données GRIB2 du Système Global de Prévision Déterministe de Vague (SGPDV)

Cette page décrit les données [Système Global de Prévision Déterministe de Vague (SGPDV)](readme_gdwps_fr.md) disponibles en format GRIB2.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le Protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTP. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier GRIB2.

Les données sont accessibles à adresse suivante :

* https://dd.weather.gc.ca/model_wave/ocean/global/grib2/HH/

where:

* __HH__ : model run start, in UTC [00 or 12]

Un historique de 24 heures est conservé dans ce répertoire.

## Spécification technique de la grille

Ce tableau répertorie les valeurs de divers paramètres de la grille globale SGPDV

| Paramètre | Valeur |
| ------ | ------ |
| ni | 1441 |
| nj | 721 | 
| résolution | 0.25° x 0.25° |
| coordonnées du premier point de grille | 90° S  0° E | 

## Nomenclature des noms de fichiers 

NOTE: TOUTES LES HEURES SONT EN UTC.

Les fichiers ont la nomenclature suivante :

CMC_gdwps_domain_Variable_LevelType_level_latlondddxddd_YYYYMMDDHH_Phhh.grib2

où :

* __CMC__ : Chaîne de caractères constante indiquant que le Centre météorologique canadien (CMC) émet les prévisions.
* __gdwps__ : Chaîne de caractères constante indiquant que les données proviennent du Système global de prévision déterministe des vagues.
* __domain__ : Chaîne de caractères constante indiquant le domaine.
* __Variable__ : Type de variable contenu dans le fichier (ex. : UGRD).
* __LevelType__ : Type de niveau
* __Level__ : Valeur du niveau
* __latlon0.ddx0.dd__ : Chaîne de caractères constante indiquant que la projection utilisée est lat/long à une résolution de 0.dd x 0.dd degré.
* __YYYYMMDD__ : Année, mois et jour du début de la prévision.
* __HH__ : UTC de la passe [00, 12].
* __Phhh__ : « P » est un caractère constant. « hhh » représente l’heure de prévision [000, 001, 002, ..., 048, 051, ..., 120].
* __grib2__ : Chaîne de caractères constante indiquant que le format est GRIB2.

Exemple de fichier :
CMC_gdwps_global_HTSGW_SFC_0_latlon0.25x0.25_2017092112_P096.grib2

Le fichier a été créé par le CMC et contient une prévision du Système global de prévision déterministe des vagues. Il contient la hauteur significative des vagues (HTSGW) pour le monde au niveau de la surface sur une grille lat/long à une résolution de 0,25 degré par 0,25 degré. Il débute le 21 septembre 2017 à 12Z (2017092112). Il contient l’heure de prévision 96 (P096) en format GRIB2 (.grib2).

## Niveaux

Niveaux qui pourraient être applicables à certains champs :

* surface
* hauteur fixe au-dessus du sol

Note : Les paramètres de houle ne réfèrent plus à la houle totale mais à la première houle. À chaque point du domaine, le spectre d’énergie des vagues peut être divisé entre la mer de vent et un certain nombre de houles. Les deux houles qui contiennent le plus d’énergie sont désignées dans l’ordre comme la première et la deuxième houle. Les paramètres de mer de vent et ceux de houles peuvent être indéfinis à certains points du domaine, pour les premiers s’il y a peu de vent et pour les seconds s’il n’y a que des vagues générées localement. 

## Liste des variables

__Champs disponibles : Numéros des paramètres et unités__
__Pour chaque numéro de paramètre GRIB, ce tableau fournit une brève description, une abréviation alphabétique conventionnelle, les niveaux pour lesquels ce paramètre est disponible et les unités de mesure__

|discipline/catégorie/numéro de paramètre GRIB2 |	Description du paramètre            |	Abréviation 	         | Niveaux       |	Unités       |
|-----------------------------------------------|---------------------------------------|----------------------------|---------------|---------------|
|10/0/2 	                                    | Couverture de glace 	                | ICEC 	                     | SFC_0 	     | proportion    |
|0/2/2 	                                        | Composante U du vent 	                | UGRD 	                     | TGL_10 (10m au-dessus du sol) 	|m/s|
|0/2/3 |	Composante V du vent |	VGRD |	TGL_10 (10m au-dessus du sol) |	m/s |
|10/0/3 |	Hauteur significative des vagues de vent et de la houle combinés |	HTSGW |	SFC_0 |	m |
|10/0/34 |	Période pic des vagues |	PWPER |	SFC_0 |	s |
|10/0/28 |	Période moyenne centrée des vagues |	MZWPER |	SFC_0 |	s |
|10/0/4 |	Direction des vagues de la mer du vent |	WVDIR |	SFC_0 |	degré vrai |
|10/0/5 |	Hauteur significative des vagues de la mer du vent |	WVHGT |	SFC_0 |	m |
|10/0/6 |	Période moyenne des vagues de la mer du vent |	WVPER |	SFC_0 |	s |
|10/0/7 |	Direction de la première houle |	SWDIR |	SFC_0 |	degré vrai |
|10/0/8 |	Hauteur significative de la première houle |	SWELL |	SFC_0 |	m |
|10/0/9 |	Période pic de la première houle |	SWPER |	SFC_0 |	s |

NOTES :

* La direction des composantes u et v du vecteur vent doit être résolue selon les composantes i, j de la grille définie et dans la direction croissante des coordonnées i, j.

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : ec.dps-client.ec@canada.ca

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).




