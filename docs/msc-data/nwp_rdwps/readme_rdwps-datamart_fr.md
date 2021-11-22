[In English](readme_rdwps-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [SRPDV](readme_rdwps_fr.md) > SRPDV sur le Datamart du SMC

# Données GRIB2 du Système Régional de Prévision Déterministe de Vague (SRPDV)

Cette page décrit les données du [Système Régional de Prévision Déterministe de Vague](./readme_rdwps_fr.md) disponible en format GRIB2.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier GRIB2.

Les données sont accessibles aux adresses suivantes :

* [https://dd.meteo.gc.ca/model_rdwps/erie/1km/{HH}/](https://dd.meteo.gc.ca/model_rdwps/erie/1km)
* [https://dd.meteo.gc.ca/model_rdwps/huron-michigan/1km/{HH}/](https://dd.meteo.gc.ca/model_rdwps/huron-michigan/1km)
* [https://dd.meteo.gc.ca/model_rdwps/ontario/1km/{HH}/](https://dd.meteo.gc.ca/model_rdwps/ontario/1km)
* [https://dd.meteo.gc.ca/model_rdwps/superior/1km/{HH}/](https://dd.meteo.gc.ca/model_rdwps/superior/1km)
* [https://dd.meteo.gc.ca/model_rdwps/atlantic-nw/5km/{HH}/](https://dd.meteo.gc.ca/model_rdwps/atlantic-nw/5km)

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

### Nord-ouest Atlantique

![](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_rdwps/grille_rdwps-nwa.png)

| Paramètre | Valeur |
| ------ | ------ |
| ni | 762 |
| nj | 643 | 
| résolution | 0.045° x 0.045° |
| coordonnées du premier point de grille | 41.065° N  255.718° O | 

## Nomenclature des noms de fichiers 

NOTE: TOUTES LES HEURES SONT EN UTC.

Les fichiers ont la nomenclature suivante :

{YYYYMMDD}T{HH}Z_MSC_RDWPS-{DOMAIN}_VAR_LVL_{grille}{resolution}_PT{hhh}H.grib2

où :

* __YYYYMMDD__ : Année, mois et jour du début de la prévision
* __T__ : Séparateur de temps selon les normes ISO8601
* __HH__ : Heure UTC de la passe [00, 12]
* __MSC__ : Chaîne de caractères constante indiquant que le Service Météorologique Canadien émet les prévisions
* __RDWPS__ : Chaîne de caractères constante indiquant que les données proviennent du Système régional de prévision déterministe des vagues
* __DOMAIN__ : Chaîne de caractères constante indiquant le domaine [erie, huron-michigan, ontario, superior, atlantic-nw]
* __VAR__ : Type de variable contenu dans le fichier
* __LVL__ : Type de niveau vertical [Sfc pour la surface, AGL pour hauteur fixe au-dessus du sol]
* __grille__ : Type de grille horizontale [LatLon, RLatLon]
* __resolution__ : Indique la résolution en degré dans les directions longitudinale et latitudinale [0.009x0.012, 0.045]
* __PT{hhh}H__ : Echéance temporelle selon la norme [ISO8601](https://en.wikipedia.org/wiki/ISO_8601). P, T et H sont des caractères constants désignant Période, Temps et Heure. "hhh" représente l’heure de prévision  [000, 001, 002, ..., 048]
* __grib2__ : Chaîne de caractères constante indiquant que le format est GRIB2.

Exemples de fichier :

* 20211014T00Z_MSC_RDWPS-Lake-Erie_HTSGW_Sfc_LatLon0.009x0.012_PT003H.grib2
* 20211014T00Z_MSC_RDWPS-Atlantic-North-West_ICEC_Sfc_RLatLon0.045_PT037H.grib2

## Niveaux  

Niveaux qui pourraient être applicables à certains champs :

* Surface [Sfc]
* Hauteur fixe au-dessus du sol [AGL]

## Liste des variables

Pour chaque numéro de paramètre GRIB, ce tableau fournit une brève description, une abréviation alphabétique conventionnelle, les niveaux pour lesquels ce paramètre est disponible et les unités de mesure

|discipline/catégorie/numéro de paramètre GRIB2 |	Description du paramètre            |	Abréviation 	         | Niveaux       |	Unités       |
|------|---------------------------------------|------------|--------|---------|
|10/2/0|  Couverture de glace                  |      ICEC  | Sfc | fraction |
|0/2/2 |  Composante U du vent                 |      UGRD  | AGL-10 | m/s |
|0/2/3 |  Composante V du vent                 |      VGRD  | AGL-10 | m/s |
|10/0/3 |	Hauteur significative des vagues de vent et de la houle combinés |	HTSGW |	Sfc |	m |
|10/0/34 |	Période pic des vagues |	PWPER |	Sfc |	s |
|10/0/28 |	Période moyenne centrée des vagues |	MZWPER |	Sfc |	s |
|10/0/46 |	Direction pic des vagues |	PWAVEDIR |	Sfc |	degrees true|
|10/0/4 |	Direction des vagues de la mer du vent |	WVDIR |	Sfc |	degré vrai |
|10/0/5 |	Hauteur significative des vagues de la mer du vent |	WVHGT |	Sfc |	m |
|10/0/35 |	Période pic des vagues de la mer du vent |	PPERWW |	Sfc |	s |
|10/0/53 |	Direction moyenne de la première houle |	MWDFSWEL |	Sfc |	degré vrai |
|10/0/47 |	Hauteur significative de la première houle |	SWHFSWEL |	Sfc |	m |
|10/0/65 |	Période pic de la première houle |	PWPFSWEL |	Sfc |	s |
|10/0/54 |	Direction moyenne de la deuxième houle |	MWDSSWEL |	Sfc |	degré vrai |
|10/0/48 |	Hauteur significative de la deuxième houle |	SWHSSWEL |	Sfc |	m |
|10/0/66 |	Période pic de la deuxième houle |	PWPSSWEL |	Sfc |	s |


### Notes

* La direction des composantes u et v du vecteur vent doit être résolue selon les composantes i, j de la grille définie et dans la direction croissante des coordonnées i, j.

* À chaque point du domaine, le spectre d’énergie des vagues peut être divisé entre la mer de vent et un certain nombre de houles. Les deux houles qui contiennent le plus d’énergie sont désignées dans l’ordre comme la première et la deuxième houle. Les paramètres de mer de vent et ceux de houles peuvent être indéfinis à certains points du domaine, pour les premiers s’il y a peu de vent et pour les seconds s’il n’y a que des vagues générées localement.

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).
