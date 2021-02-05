[In English](readme_rewps-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [SRPEV](readme_rewps_fr.md) > SRPEV sur le Datamart du SMC

# Données GRIB2 du Système Régional de Prévision d'Ensemble de Vague (SRPEV)

Cette page décrit les données [Système Régional de Prévision d'Ensemble de Vague (SRPEV)](readme_rewps_fr.md) disponibles en format GRIB2.

## Adresse des données

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier GRIB2.

Les données sont accessibles à adresse suivante :

* [https://dd.weather.gc.ca/model_rewps/great-lakes/grib2/{HH}/](https://dd.weather.gc.ca/model_rewps/great-lakes/grib2)

où :

* __HH__ : Heure UTC du début de la passe du modèle [00, 12].

Un historique de 24 heures est conservé dans ce répertoire.

## Domaines disponibles

### Grands Lacs

| Paramètre | Valeur |
| ------ | ------ |
| ni | 550 |
| nj | 365 |
| résolution | 0.0225° x 0.0310° |
| coordonnées du premier point de grille | 41.0984° N  92.4790° O |

## Nomenclature des noms de fichiers

NOTE: TOUTES LES HEURES SONT EN UTC.

Les fichiers ont la nomenclature suivante :

{YYYYMMDD}T{HH}Z_MSC_REWPS-DOMAIN_VAR_LVL_{grille}{resolution}_PT{h}H.grib2

où :

* __YYYYMMDD__ : Année, mois et jour du début de la prévision.
* __T__ : Séparateur de temps selon les normes ISO8601.
* __HH__ : Heure UTC de la passe [00, 12].
* __MSC__ : Chaîne de caractères constante indiquant que le Service Météorologique Canadien émet les prévisions.
* __REWPS__ : Chaîne de caractères constante indiquant que les données proviennent du Système régional de prévision d'ensemble des vagues.
* __DOMAIN__ : Chaîne de caractères indiquant le domaine.
* __VAR__ : Type de variable contenu dans le fichier
* __LVL__ : Type de niveau vertical [SFC pour la surface]
* __grille__ : Type de grille horizontale [LatLon]
* __resolution__ : Indique la résolution en degré dans les directions longitudinale et latitudinale [0.0225x0.0310]
* __PThH__ : P, T et H sont des caractères constants désigannt Période, Temps et Heure. h représente l’heure de prévision [0, 3, 6, 9, 12, ..., 72].
* __grib2__ : Chaîne de caractères constante indiquant que le format est GRIB2.

Exemple de fichier :

20210202T12Z_MSC_REWPS-Great-Lakes_HTSGW_SFC_LatLon0.0225x0.0310_PT66H.grib2

## Liste des variables

Pour chaque numéro de paramètre GRIB, ce tableau fournit une brève description, une abréviation alphabétique conventionnelle, les niveaux pour lesquels ce paramètre est disponible et les unités de mesure

|discipline/catégorie/numéro de paramètre GRIB2 |	Description du paramètre            |	Abréviation 	         | Niveaux       |	Unités       |
|-----------------------------------------------|---------------------------------------|----------------------------|---------------|---------------|
|10/0/3 |	Hauteur significative des vagues de vent et de la houle combinés |	HTSGW |	SFC |	m |
|10/0/34 |	Période pic des vagues |	PWPER |	SFC |	s |
|10/0/28 |	Période moyenne centrée des vagues |	MZWPER |	SFC |	s |
|10/0/46 |	Direction pic des vagues |	PWAVEDIR |	SFC |	degrees true|
|10/0/4 |	Direction des vagues de la mer du vent |	WVDIR |	SFC |	degré vrai |
|10/0/5 |	Hauteur significative des vagues de la mer du vent |	WVHGT |	SFC |	m |
|10/0/35 |	Période pic des vagues de la mer du vent |	WVPER |	SFC |	s |
|10/0/53 |	Direction moyenne de la première houle |	MWDFSWEL |	SFC |	degré vrai |
|10/0/47 |	Hauteur significative de la première houle |	SWHFSWEL |	SFC |	m |
|10/0/65 |	Période pic de la première houle |	PWPFSWEL |	SFC |	s |

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Annonces de la liste de diffusion dd_info

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).


