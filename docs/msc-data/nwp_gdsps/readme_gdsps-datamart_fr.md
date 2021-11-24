[In English](readme_gdsps-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../../readme_fr.md) > [SGPDOT](readme_gdsps_fr.md) > SGPDOT sur le Datamart du SMC

# Données NetCDF du Système global de prévision déterministe d'onde de tempête (SGPDOT)

Cette page décrit les données du [Système global de prévision déterministe d'onde de tempête (SGPDOT)](readme_gdsps_fr.md) disponibles en format NetCDF.

## Adresse des données

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTP. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier NetCDF.

Les données sont accessibles à adresse suivante :

* [https://dd.meteo.gc.ca/model_gdsps/15km/{HH}/](https://dd.meteo.gc.ca/model_gdsps/15km)

où :

* __HH__ : Heure UTC du début de la passe du modèle [00, 12]

Un historique de 24 heures est conservé dans ce répertoire.

## Domaine disponible

Grille latitude-logitude globale

| Paramètre | Valeur |
| ------ | ------ |
| ni | 1801 |
| nj | 1251 |
| résolution | 0.144° x 0.200° |

## Nomenclature des noms de fichiers

NOTE: TOUTES LES HEURES SONT EN UTC.

Les noms de fichiers ont la nomenclature suivante :

```
{YYYYMMDD}T{HH}Z_MSC_GDSPS_{VAR}_{LVL}_{grille}{resolution}_PT{hhh}H.nc
```

où :

* __YYYYMMDD__ : Année, mois et jour du début de la prévision
* __T__ : Délimiteur temporel selon les normes ISO8601
* __HH__ : Heure UTC de la passe [00, 12]
* __Z__ : Fuseau horaire (heure UTC)
* __MSC__ : Chaîne de caractères constante pour Meteorological Service of Canada, la source des données
* __GDSPS__ : Chaîne de caractères constante indiquant que les données proviennent du Système global de prévision déterministe d'onde de tempête 
* __VAR__ : Variables contenues dans le fichier [ETAS, SSH]
* __LVL__ : Niveau vertical [Sfc pour la surface]
* __grille__ : Grille horizontale lat-lon [LatLon]
* __resolution__ : Indique la résolution en degré dans les directions longitudinale et latitudinale [0.144x0.200]
* __PT{hhh}H__ : Echéance temporelle selon la norme [ISO8601](https://en.wikipedia.org/wiki/ISO_8601). P, T et H sont des caractères constants désignant Période, Temps et Heure. "hhh" représente l’heure de prévision  [000, 001, 002, ..., 240]
* __nc__ : Chaîne de caractères constante indiquant que le format est NetCDF

Exemple de fichier :

20180417T12Z_MSC_GDSPS_ETAS_Sfc_LatLon0.144x0.200_PT024H.nc

##   Liste de variables

La liste ci-dessous fournit pour chaque identifieur de paramètre NetCDF: une brève description, une abréviation alphabétique, les niveaux pour lesquels ce paramètre est disponible et les unités de mesure.


|  NetCDF  |   Description courte |                        Abr.|   Niveau | Unités|
|----------|--------|--------|--------|--------|
| etas     |  Onde de tempête                 |         ETAS  |  Sfc | m |
| zos      |  Hauteur de la surface de la mer  |          SSH  |  Sfc | m |

NOTE:

* Expliquer comment est calulé ETAS (cf: https://gitlab.science.gc.ca/CMOA/Datamart/issues/53#note_366328; https://lists.ec.gc.ca/pipermail/dd_info/2021-November/000497.html)

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Annonces de la liste de diffusion dd_info

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).
