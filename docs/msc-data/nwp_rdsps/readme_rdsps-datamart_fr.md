[In English](readme_rdsps-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../../readme_fr.md) > [SRPDOT](readme_rdsps_fr.md) > SRPDOT sur le Datamart du SMC

# Données NetCDF du Système régional de prévision déterministe d'onde de tempête (SRPDOT)

Cette page décrit les données [Système régional de prévision déterministe d'onde de tempête (SRPDOT)](readme_rdsps_fr.md) disponibles en format NetCDF.

## Spécification technique de la grille

![Image de la grille du SRPDOT](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_rdsps/grille_rdsps.png)

Ce tableau répertorie les valeurs de divers paramètres de la grille :

| Paramètre | Valeur |
| ------ | ------ |
| ni | 841 |
| nj | 541 |
| résolution | 0.033° x 0.033° |

## Nomenclature des noms de fichiers

Les noms de fichiers ont la nomenclature suivante :

```
{YYYYMMDD}T{HH}Z_MSC_RDSPS-Atlantic-North-West_{VAR}_{LVL}_{grille}{resolution}_P{hhh}.nc
```

où :

* __YYYYMMDD__ : Année, mois et jour du début de la prévision
* __T__ : Délimiteur temporel selon les normes ISO8601
* __HH__ : Heure UTC de la passe [00, 12]
* __Z__ : Fuseau horaire (heure UTC)
* __MSC__ : Chaîne de caractères constante pour Meteorological Service of Canada, la source des données
* __RDSPS-Atlantic-North-West__ : Chaîne de caractères constante indiquant que les données proviennent du Système régional de prévision déterministe d'onde de tempête sur le domaine nord ouest
* __VAR__ : Variables contenues dans le fichier [ETAS, SSHT, SSH]
* __LVL__ : Niveau vertical [SFC, pour la surface]
* __grille__ : Grille horizontale lat-lon [LatLon]
* __resolution__ : 0.033x0.033. Signifie une résolution de 0.033° dans les directions longitudinale et latitudinale
* __Phhh__ : « P » est un caractère constant. « hhh » représente l’heure de prévision [000, 001, 002, ..., 240]
* __nc__ : Chaîne de caractères constante indiquant que le format est NetCDF

Exemple de fichier :

20180417T12Z_MSC_RDSPS-Atlantic-North-West_ETAS_SFC_LatLon0.033x0.033_P024.nc

##   Liste de variables

La liste ci-dessous fournit pour chaque identifieur de paramètre NetCDF: une brève description, une abréviation alphabétique, les niveaux pour lesquels ce paramètre est disponible et les unités de mesure.


|  NetCDF  |   Description courte |                        Abr.|   Niveau | Unités|
|----------|--------|--------|--------|--------|
| etas     |  Onde de tempête                 |         ETAS  |  SFC | m |
| ssh_tide |  Hauteur d'eau associée à la marée            |         SSHT  |  SFC | m |
| zos      |  Hauteur de la surface de la mer  |          SSH  |  SFC | m |

## Support

Pour toute question relative à ces données, merci de [nous contacter](https://meteo.gc.ca/mainmenu/contact_us_f.html).

## Annonces de la liste de diffusion dd_info

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).
