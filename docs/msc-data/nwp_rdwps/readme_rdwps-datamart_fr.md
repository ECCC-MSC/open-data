[In English](readme_rdwps-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [SRPDV](readme_rdwps_fr.md) > SRPDV sur le Datamart du SMC

# Données GRIB2 du Système Régional de Prévision Déterministe de Vague (SRPDV)

Cette page décrit les données du [Système Régional de Prévision Déterministe de Vague](./readme_rdwps_fr.md) disponible en format GRIB2.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier GRIB2.

Les données sont accessibles aux adresses suivantes :

* [https://dd.meteo.gc.ca/model_wave/great_lakes/erie/grib2/{HH}/](https://dd.meteo.gc.ca/model_wave/great_lakes/erie/grib2)
* [https://dd.meteo.gc.ca/model_wave/great_lakes/huron-michigan/grib2/{HH}/](https://dd.meteo.gc.ca/model_wave/great_lakes/huron-michigan/grib2)
* [https://dd.meteo.gc.ca/model_wave/great_lakes/ontario/grib2/{HH}/](https://dd.meteo.gc.ca/model_wave/great_lakes/ontario/grib2)
* [https://dd.meteo.gc.ca/model_wave/great_lakes/superior/grib2/{HH}/](https://dd.meteo.gc.ca/model_wave/great_lakes/superior/grib2)
* [https://dd.meteo.gc.ca/model_wave/ocean/gulf-st-lawrence/grib2/{HH}/](https://dd.meteo.gc.ca/model_wave/ocean/gulf-st-lawrence/grib2)

où :

* __HH__ : Heure UTC du début de la passe du modèle [00, 06, 12, 18].

Un historique de 24 heures est conservé dans ce répertoire.

## Domaines disponibles

### Lac Supérieur

![](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_rdwps/grille_rdwps_sup.png)

| Paramètre | Valeur |
| ------ | ------ |
| ni | 658 |
| nj | 318 | 
| résolution | 0.0090° x 0.0124° |
| coordonnées du premier point de grille | 46.2590° N  92.3116° O | 

### Lac Huron et Lac Michigan

![](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_rdwps/grille_rdwps_hum.png)

| Paramètre | Valeur |
| ------ | ------ |
| ni | 698 |
| nj | 573 | 
| résolution | 0.0090° x 0.0124° |
| coordonnées du premier point de grille | 41.4260° N  88.1452° O | 

### Lac Érié

![](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_rdwps/grille_rdwps_erie.png)

| Paramètre | Valeur |
| ------ | ------ |
| ni | 398 |
| nj | 210 | 
| résolution | 0.0090° x 0.0124° |
| coordonnées du premier point de grille | 41.2190° N  83.6068° O | 

### Lac Ontario

![](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_rdwps/grille_rdwps_ont.png)

| Paramètre | Valeur |
| ------ | ------ |
| ni | 348 |
| nj | 158 | 
| résolution | 0.0090° x 0.0124° |
| coordonnées du premier point de grille | 43.0640° N  79.9736° O | 

### Golfe du Saint-Laurent

![](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_rdwps/grille_rdwps-gsl.png)

| Paramètre | Valeur |
| ------ | ------ |
| ni | 331 |
| nj | 160 | 
| résolution | 0.05° x 0.05° |
| coordonnées du premier point de grille | 44.075° N  70.925° O | 

## Nomenclature des noms de fichiers 

NOTE: TOUTES LES HEURES SONT EN UTC.

Les fichiers ont la nomenclature suivante :

CMC_rdwps_DOMAIN_VAR_LVL_LVLVAL_{grille}{resolution}_YYYYMMDDHH_P{hhh}.grib2

où :

* __CMC__ : Chaîne de caractères constante indiquant que le Centre météorologique canadien (CMC) émet les prévisions.
* __rdwps__ : Chaîne de caractères constante indiquant que les données proviennent du Système régional de prévision déterministe des vagues.
* __DOMAIN__ : Chaîne de caractères indiquant le domaine.
* __VAR__ : Type de variable contenu dans le fichier
* __LVL__ : Type de niveau
* __LVLVAL__ : Valeur du niveau
* __grille__ : Type de grille horizontale [LatLon]
* __resolution__ : Indique la résolution en degré dans les directions longitudinale et latitudinale [par ex.: 0.0090x0.0124]
* __YYYYMMDD__ : Année, mois et jour du début de la prévision.
* __HH__ : Heure UTC de la passe [00, 06, 12, 18].
* __Phhh__ : « P » est un caractère constant. « hhh » représente l’heure de prévision [000, 001, 002, ..., 048].
* __grib2__ : Chaîne de caractères constante indiquant que le format est GRIB2.

Exemple de fichier :

CMC_rdwps_lake-ontario_HTSGW_SFC_0_latlon0.0090x0.0124_2017092606_P042.grib2

Le fichier a été créé par le CMC et contient une prévision du Système régional de prévision déterministe de vague. Il contient la hauteur significative des vagues (HTSGW) du lac Ontario au niveau de la surface sur une grille lat/long à une résolution de 0,0090 degré par 0,0124 degré. Il débute le 26 septembre 2017 à 06Z (2017092606). Il contient l’heure de prévision 42 (P042) en format GRIB2 (.grib2).

## Niveaux  

Niveaux qui pourraient être applicables à certains champs :

* Surface [SFC]
* Hauteur fixe au-dessus du sol [TGL]
* Niveau de la mer [MSL]

## Liste des variables

Pour chaque numéro de paramètre GRIB, ce tableau fournit une brève description, une abréviation alphabétique conventionnelle, les niveaux pour lesquels ce paramètre est disponible et les unités de mesure

|discipline/catégorie/numéro de paramètre GRIB2 |	Description du paramètre            |	Abréviation 	         | Niveaux       |	Unités       |
|------|---------------------------------------|------------|--------|---------|
|10/2/0|  Couverture de glace                  |      ICEC  | SFC_0 | fraction |
|0/2/2 |  Composante U du vent                 |      UGRD  | TGL_10 | m/s |
|0/2/3 |  Composante V du vent                 |      VGRD  | TGL_10 | m/s |
|0/3/1 |  Pression réduite au niveau de la mer |             PRMSL  | MSL_0 | Pa  |
|10/0/3|  Hauteur significative des vagues de vent et de la houle combinées |  HTSGW | SFC_0 | m |
|10/0/34| Période pic des vagues               |      PWPER | SFC_0 | s |
|10/0/28| Période moyenne centrée des vagues   |      MZWPER | SFC_0 |  s |
|10/0/4 | Direction des vagues de la mer du vent |    WVDIR | SFC_0 | degré vrai |
|10/0/5 | Hauteur significative des vagues de la mer du vent |   WVHGT | SFC_0 | m |
|10/0/6 | Période moyenne des vagues de la mer du vent |   WVPER | SFC_0 | s |
|10/0/7 | Direction de la première houle       |      SWDIR | SFC_0 | degré vrai |
|10/0/8 | Hauteur significative de la première houle | SWELL | SFC_0 | m |
|10/0/9 | Période pic de la première houle     |      SWPER | SFC_0 | s |

### Notes

* La direction des composantes u et v du vecteur vent doit être résolue selon les composantes i, j de la grille définie et dans la direction croissante des coordonnées i, j.

* Golfe du Saint-Laurent période pic: le nom de fichier utilise __VAR__ PKPER et __LVL__ TGL.

* La pression réduite au niveau de la mer est disponible seulement pour le Golfe du Saint-Laurent

* La période moyenne centrée des vagues est disponible seulement pour les Grands Lacs

* Les paramètres de houle du Golfe du Saint-Laurent représentent la houle totale

* Les paramètres de houle des Grands Lacs représentent la première houle. À chaque point du domaine, le spectre d’énergie des vagues peut être divisé entre la mer de vent et un certain nombre de houles. Les deux houles qui contiennent le plus d’énergie sont désignées dans l’ordre comme la première et la deuxième houle. Les paramètres de mer de vent et ceux de houles peuvent être indéfinis à certains points du domaine, pour les premiers s’il y a peu de vent et pour les seconds s’il n’y a que des vagues générées localement.

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).
