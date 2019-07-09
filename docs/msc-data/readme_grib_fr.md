[In English](readme_grib_fr.md)

![ECCC logo](../img_eccc-logo.png)

[TdM](../readme_fr.md) > [Données du SMC](readme_fr.md) > GRIB

# Données GRIB

## A propos du format GRIB

Le format GRIB est un format de fichier utilisé pour le stockage et la transmission de données météorologiques sur des points de grilles, tel que les sorties de modèle de prévision numérique du temps. Il est conçu afin d’être autodescripteur, compact et utilisable tel quel, d’une architecture informatique à une autre. Le [standard GRIB](https://www.wmo.int/pages/prog/www/WDM/Guides/Guide-binary-2.html) a été conçu et est maintenu par l’Organisation météorologique mondiale (OMM).

Les données GRIB sont utilisées par des personnes, des institutions et des entreprises qui veulent accéder aux données brutes provenant de modèles de prévision numérique du temps. Une fois décodées, les données peuvent être post-traitées pour être visualisées ou utilisées comme point de départ pour des applications de prévision du temps qui nécessitent des données sur des points de grilles.

Le format [GRIB2](https://www.nco.ncep.noaa.gov/pmb/docs/grib2/grib2_doc/) représente une diversification et une modernisation significatives du standard GRIB. Il n’est pas compatible avec le format GRIB1. Il entre progressivement en fonction au Centre européen de prévision à moyen terme et dans quelques centres nationaux de prévision numérique du temps, notamment aux États-Unis et en Europe.

Avant 2010, le Centre Météorologique Canadien (CMC) n’offrait ses données que dans le format GRIB1. Depuis 2011, le CMC n’offre ses données que dans le format GRIB2.

Chaque enregistrement commence par un en-tête suivi de données binaires sommairement compressées. L’en-tête est composé de nombres de 8 bits, sans signe (appelés octets). Il contient de l’information concernant :

* L’en-tête lui-même (méta données sur la longueur de l’en-tête, usage particulier des octets,  présence de sous-en-têtes optionnels)
* La nature qualitative des données (champ, niveau, date de production, temps de validité, etc.)
* La méthode et les paramètres à utiliser pour restaurer les données compressées
* Les propriétés et les caractéristiques géographiques de la grille sur laquelle les données doivent être pointées

## Logiciels pour utiliser les données en format GRIB2

Le Service météorologique du Canada ne distribue pas publiquement de logiciel de décodage ou de visualisation du format GRIB2. Voici une liste, non exhaustive, de liens (en anglais) vers des logiciels de traitement des données GRIB2.

Décodage et manipulation :

* [wgrib2](https://www.cpc.ncep.noaa.gov/products/wesley/wgrib2/)
* [Tricks for wgrib2](https://ftp.cpc.ncep.noaa.gov/wd51we/wgrib2/tricks.wgrib2)
* [GDAL](https://gdal.org/drivers/raster/grib.html)
    
Visualisation et interpolation :

* [INGRIDDS](http://winweather.org/)
* [OpenGRADS Bundle pour GRIB2](http://opengrads.org/doc/bundle/grads/)
* [GEMPAK](https://www.unidata.ucar.edu/software/gempak/)
* [NCAR NCL](http://ngwww.ucar.edu/ncl/)
