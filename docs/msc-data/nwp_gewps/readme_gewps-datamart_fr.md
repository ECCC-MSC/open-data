[In English](readme_gewps-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [SGPEV](readme_gewps_fr.md) > SGPEV sur le Datamart du SMC

# Données GRIB2 du Système Global de Prévision d'Ensemble de Vague (SGPEV)

Cette page décrit les données du [Système Global de Prévision d'Ensemble de Vague (SGPEV)](readme_gewps_fr.md) disponibles en format GRIB2.

## Adresse des données

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier GRIB2.

Les données sont accessibles à adresse suivante :

* [https://dd.meteo.gc.ca/model_gewps/25km/{HH}/](https://dd.meteo.gc.ca/model_gewps/25km)

où :

* __HH__ : Heure UTC du début de la passe du modèle [00, 12].

Un historique de 24 heures est conservé dans ce répertoire.

## Domaine disponible

Grille latitude-longitude globale

| Paramètre | Valeur |
| ------ | ------ |
| ni | 1440 |
| nj | 721 |
| résolution | 0.25° |
| coordonnées du premier point de grille | 90° S  0° E |

## Nomenclature des noms de fichiers

NOTE: TOUTES LES HEURES SONT EN UTC.

Les fichiers ont la nomenclature suivante :

{YYYYMMDD}T{HH}Z_MSC_GEWPS_VAR_LVL_{grille}{resolution}_PT{hhh}H.grib2

où :

* __YYYYMMDD__ : Année, mois et jour du début de la prévision
* __T__ : Séparateur de temps selon les normes ISO8601
* __HH__ : Heure UTC de la passe [00, 12]
* __MSC__ : Chaîne de caractères constante indiquant que le Service Météorologique Canadien émet les prévisions
* __GEWPS__ : Chaîne de caractères constante indiquant que les données proviennent du Système global de prévision d'ensemble de vague
* __VAR__ : Type de variable contenu dans le fichier
* __LVL__ : Type de niveau vertical [Sfc pour la surface]
* __grille__ : Type de grille horizontale [LatLon]
* __resolution__ : Indique la résolution en degré dans les directions longitudinale et latitudinale [0.25]
* __PT{hhh}H__ : Echéance temporelle selon la norme [ISO8601](https://en.wikipedia.org/wiki/ISO_8601). P, T et H sont des caractères constants désignant Période, Temps et Heure. "hhh" représente l’heure de prévision [000, 003, 006, ..., 384]
* __grib2__ : Chaîne de caractères constante indiquant que le format est GRIB2.

Exemple de fichier :

20210225T12Z_MSC_GEWPS_HTSGW_Sfc_LatLon0.25_PT015H.grib2

## Liste des variables

Pour chaque numéro de paramètre GRIB, ce tableau fournit une brève description, une abréviation alphabétique conventionnelle, les niveaux pour lesquels ce paramètre est disponible et les unités de mesure

|discipline/catégorie/numéro de paramètre GRIB2 |	Description du paramètre            |	Abréviation 	         | Niveaux       |	Unités       |
|-----------------------------------------------|---------------------------------------|----------------------------|---------------|---------------|
|10/0/3 |	Hauteur significative des vagues de vent et de la houle combinés |	HTSGW |	Sfc |	m |
|10/0/34 |	Période pic des vagues |	PWPER |	Sfc |	s |
|10/0/28 |	Période moyenne centrée des vagues |	MZWPER |	Sfc |	s |
|10/0/46 |	Direction pic des vagues |	PWAVEDIR |	Sfc |	degrees true|
|10/0/4 |	Direction des vagues de la mer du vent |	WVDIR |	Sfc |	degré vrai |
|10/0/5 |	Hauteur significative des vagues de la mer du vent |	WVHGT |	Sfc |	m |
|10/0/35 |	Période pic des vagues de la mer du vent |	PPERWW |	Sfc |	s |
|10/0/53 |	Direction moyenne de la première houle |	MWDFSWEL |	Sfc |	degré vrai |
|10/0/47 |	Hauteur significative de la première houle |	SWHFSWEL |	Sfc |	m |
|10/0/65 |	Période pic de la première houle |	PWPFSWEL |	SFfc|	s |
|10/0/54 |	Direction moyenne de la deuxième houle |	MWDSSWEL |	Sfc |	degré vrai |
|10/0/48 |	Hauteur significative de la deuxième houle |	SWHSSWEL |	Sfc |	m |
|10/0/68 |	Période pic de la deuxième houle |	PWPSSWEL |	Sfc |	s |

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Annonces de la liste de diffusion dd_info

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).


