[In English](readme_raqdps-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [SRPDQA](readme_raqdps_fr.md) > Système régional de prévision déterministe de la qualité de l’air sur le Datamart du SMC

# Données GRIB2 du Système régional de prévision déterministe de la qualité de l’air (SRPDQA)

Cette page décrit les données du [Système régional de prévision déterministe de la qualité de l’air (SRPDQA)](readme_raqdps_fr.md) en format GRIB2, exécuté deux fois par jour afin de produire des prévisions horaires de 72 heures pour certains polluants tels que l’ozone (O3), le dioxyde d’azote (NO2) ou encore les matières particulaires dont le diamètre aérodynamique est inférieur à 2.5 μm (PM2.5), sur une grille nord-américaine.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le Protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont accessibles à l'adresse suivante :

* [https://dd.meteo.gc.ca/model_raqdps/10km/grib2/{HH}/{hhh}](https://dd.meteo.gc.ca/model_raqdps/10km/grib2)         

où :

* __HH__ : Heure UTC du début de la passe du modèle [00, 12]
* __hhh__ : Heure de prévision [000, 001, 002, ..., 072] 

Un historique de 24 heures est conservé dans ce répertoire.

## Spécification technique de la grille  

![Image du domaine RAQDPS](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_raqdps-fw/grille_raqdps-fw.png)

Valeurs données aux paramètres de la grille lat-lon tournée :

| Paramètre | Valeur |
| ------ | ------ |
| ni | 729 |
| nj | 599 | 
| résolution à 60° N | 10km |
| coordonnées du premier point de grille (relatives à la grille utilisée) | 32 ° S ; 39.5 ° W | 

__Note__ : Les [versions les plus récentes de wgrib2](https://www.cpc.ncep.noaa.gov/products/wesley/wgrib2/update_2.0.8.html) et [GDAL](https://gdal.org/) supportent ces grilles tournées. 

## Nomenclature des noms de fichiers 

NOTE: TOUTES LES HEURES SONT EN UTC.

La nomenclature des noms des fichiers est la suivante :

`{YYYYMMDD}T{HH}Z_MSC_RAQDPS_{VAR}_{LVL}_{Grille}(resolution}_PT{hhh}H.grib2`

où :

* __YYYYMMDD__ : Année, mois et jour du début de la prévision
* __T__ : Délimiteur temporel selon les normes ISO8601
* __HH__ : Heure UTC de la passe [00, 12]
* __Z__ : Fuseau horaire (heure UTC)
* __MSC__ : Chaîne de caractères constante pour Meteorological Service of Canada, la source des données 
* __RAQDPS__ : Chaîne de caractères constante indiquant que les données proviennent du Système régional de prévision déterministe de la qualité de l’air
* __VAR__ : Type de variable contenu dans le fichier [PM2.5, PM10, O3, NO, NO2, SO2]
* __LVL__ : Niveau vertical [Sfc pour la surface, EAtm pour l’intégrale de la colonne]
* __Grille__ : Grille horizontale lat-lon tournée [RLatLon] 
* __resolution__ : Indique la résolution en degré, ici 0.09°x0.09° (environ 10km) dans les directions longitudinale et latitudinale [0.09]
* __PT{hhh}H__ : Echéance temporelle selon la norme [ISO8601](https://en.wikipedia.org/wiki/ISO_8601). P, T et H sont des caractères constants désignant Période, Temps et Heure. "hhh" représente l’heure de prévision  [000, 001, 002, ..., 072]
* __grib2__ : Chaîne de caractères constante indiquant que le format est GRIB2

Exemple de noms de fichier :

* 20200521T00Z_MSC_RAQDPS_PM2.5-Sfc_RLatLon0.09_PT003H.grib2

## Liste des variables

Liste des variables 2D disponibles dans les fichiers:

<table id="csv-table" class="display"></table>

<link href="https://cdn.jsdelivr.net/npm/simple-datatables@latest/dist/style.css" rel="stylesheet" type="text/css">
<script src="https://cdn.jsdelivr.net/npm/simple-datatables@latest"></script>
<script src="../../../js/variables_datatable.js" type="text/javascript"></script>
<script>
  loadTable("csv-table", "../../../assets/csv/RAQDPS_fr.csv", "FR");
</script>

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).

