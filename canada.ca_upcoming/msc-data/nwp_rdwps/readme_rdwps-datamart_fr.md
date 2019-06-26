[In English](readme_rdwps-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données ouvertes publiques du SMC](../readme_fr.md) > SRPDV sur le Datamart du SMC


# Données GRIB2 du Système Régional de Prévision Déterministe de Vague (SRPDV)

## Grands Lacs

Le [Système Régional de Prévision Déterministe de Vague (SRPDV)](readme_rdwps_fr.md) produit les prévisions de vagues pour les Grands Lacs en utilisant le modèle spectral de prévision de vague de troisième génération WaveWatch III ® (WW3). Le modèle est forcé par les vents à une élévation de 10 mètres du Système à haute résolution de prévision déterministe (SHRPD). Une analyse de glace est utilisée par le modèle pour atténuer ou supprimer la croissance des vagues dans les zones couvertes par respectivement 25% à 75% et plus de 75% de glace.

Le WW3 (Tolman et le WAVEWATCH III® Development Group 2014) est un modèle spectral de prévision de vague de troisième génération qui résout l’évolution de l’équation du bilan énergétique pour le spectre de vague 2D d’énergie. Le modèle WW3 a été adopté par de nombreux centres nationaux de prévision au cours des dernières années. 

## Golfe du Saint-Laurent

Le [Système Régional de Prévision Déterministe de Vague (SRPDV)](readme_rdwps_fr.md) produit les prévisions de vagues pour le golfe du Saint-Laurent en utilisant le modèle spectral de prévision de vague de troisième génération WAM. Le modèle est forcé par les vents à une altitude 10 mètres du Système régional de prévision déterministe (SRPD). En outre, une analyse de la glace de mer est utilisée par le modèle pour supprimer la croissance des vagues dans les zones couvertes par plus de 50 % de glace.

Le WAM (modèle de vague) (WAMDI Groupe 1988, Komen et al. 1994) est un modèle spectral de prévision de vague de troisième génération qui résout l’évolution de l’équation du bilan énergétique pour le spectre de vague 2D d’énergie, sans hypothèse préalable sur la forme du spectre. Le modèle WAM est utilisé opérationnellement par la communauté internationale depuis le début des années 1990, après une longue période de développement dans le cadre du WAMDIG (modèle de vague et de développement du Groupe de mise en œuvre).

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le Protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTP. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier GRIB2.

Les données sont accessibles aux adresses suivantes :
* https://dd.meteo.gc.ca/model_wave/great_lakes/erie/grib2/HH/
* https://dd.meteo.gc.ca/model_wave/great_lakes/huron-michigan/grib2/HH/
* https://dd.meteo.gc.ca/model_wave/great_lakes/ontario/grib2/HH/
* https://dd.meteo.gc.ca/model_wave/great_lakes/superior/grib2/HH/
* https://dd.meteo.gc.ca/model_wave/ocean/gulf-st-lawrence/grib2/HH/

où :

* __HH__ : Heure UTC du début de la passe du modèle [00, 06, 12, 18].

## Spécification technique de chacune des grilles

### Lac Supérieur

Ce tableau répertorie les valeurs de divers paramètres de la grille du lac Supérieur :

| Paramètre | Valeur |
| ------ | ------ |
| ni | 658 |
| nj | 318 | 
| résolution | 0.0090° x 0.0124° |
| coordonnées du premier point de grille | 46.2590° N  92.3116° O | 

### Lac Huron et Lac Michigan

Ce tableau répertorie les valeurs de divers paramètres de la grille des lacs Huron et Michigan :

| Paramètre | Valeur |
| ------ | ------ |
| ni | 698 |
| nj | 573 | 
| résolution | 0.0090° x 0.0124° |
| coordonnées du premier point de grille | 41.4260° N  88.1452° O | 

### Lac Érié

Ce tableau répertorie les valeurs de divers paramètres de la grille du lac Érié :

| Paramètre | Valeur |
| ------ | ------ |
| ni | 398 |
| nj | 210 | 
| résolution | 0.0090° x 0.0124° |
| coordonnées du premier point de grille | 41.2190° N  83.6068° O | 

### Lac Ontario

Ce tableau répertorie les valeurs de divers paramètres de la grille du lac Ontario :

| Paramètre | Valeur |
| ------ | ------ |
| ni | 348 |
| nj | 158 | 
| résolution | 0.0090° x 0.0124° |
| coordonnées du premier point de grille | 43.0640° N  79.9736° O | 

### Golfe du Saint-Laurent

Ce tableau répertorie les valeurs de divers paramètres de la grille du Golfe du Saint-Laurent :

| Paramètre | Valeur |
| ------ | ------ |
| ni | 331 |
| nj | 160 | 
| résolution | 0.05° x 0.05° |
| coordonnées du premier point de grille | 44.075° N  70.925° O | 

## Nomenclature des noms de fichiers 

NOTE: TOUTES LES HEURES SONT EN UTC.

Les fichiers ont la nomenclature suivante :

CMC_rdwps_domain_Variable_LevelType_level_latlondddxddd_YYYYMMDDHH_Phhh.grib2

où :

* __CMC__ : Chaîne de caractères constante indiquant que le Centre météorologique canadien (CMC) émet les prévisions.
* __rdwps__ : Chaîne de caractères constante indiquant que les données proviennent du Système régional de prévision déterministe des vagues.
* __domain__ : Chaîne de caractères constante indiquant le domaine.
* __Variable__ : Type de variable contenu dans le fichier (ex. : UGRD).
* __LevelType__ : Type de niveau
* __Level__ : Valeur du niveau
* __latlondddxddd__ : Chaîne de caractères constante indiquant que la projection utilisée est lat/long à une résolution de ddd x ddd degré.
* __YYYYMMDD__ : Année, mois et jour du début de la prévision.
* __HH__ : UTC de la passe [00, 06, 12, 18].
* __Phhh__ : « P » est un caractère constant. « hhh » représente l’heure de prévision [000, 001, 002, ..., 048].
* __grib2__ : Chaîne de caractères constante indiquant que le format est GRIB2.

Exemple de fichier :
CMC_rdwps_lake-ontario_HTSGW_SFC_0_latlon0.0090x0.0124_2017092606_P042.grib2

Le fichier a été créé par le CMC et contient une prévision du Système régional de prévision déterministe de vague. Il contient la hauteur significative des vagues (HTSGW) du lac Ontario au niveau de la surface sur une grille lat/long à une résolution de 0,0090 degré par 0,0124 degré. Il débute le 26 septembre 2017 à 06Z (2017092606). Il contient l’heure de prévision 42 (P042) en format GRIB2 (.grib2).

## Niveaux  

Niveaux qui pourraient être applicables à certains champs :

* surface
* hauteur fixe au-dessus du sol
* niveau de la mer

## Liste des variables

|GRIB2 |  Description courte                   |      Abr.  | Niveau | Unités  |
|------|---------------------------------------|------------|--------|---------|
|10/2/0|  Couverture de glace                  |      ICEC  | SFC_0 | fraction |
|0/2/2 |  Composante U du vent                 |      UGRD  | TGL_10 | m/s |
|0/2/3 |  Composante V du vent                 |      VGRD  | TGL_10 | m/s |
|10/0/3|  Hauteur significative des vagues de vent et de la houle combinées |  HTSGW | SFC_0 | m |
|10/0/34| Période pic des vagues               |      PWPER | SFC_0 | s |
|10/0/28| Période moyenne centrée des vagues   |      MZWPER | SFC_0 |  s |
|10/0/4 | Direction des vagues de la mer du vent |    WVDIR | SFC_0 | degré vrai |
|10/0/5 | Hauteur significative des vagues de la mer du vent |   WVHGT | SFC_0 | m |
|10/0/6 | Période moyenne des vagues de la mer du vent |   WVPER | SFC_0 | s |
|10/0/7 | Direction de la première houle       |      SWDIR | SFC_0 | degré vrai |
|10/0/8 | Hauteur significative de la première houle | SWELL | SFC_0 | m |
|10/0/9 | Période pic de la première houle     |      SWPER | SFC_0 | s |

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : ec.dps-client.ec@canada.ca

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).
