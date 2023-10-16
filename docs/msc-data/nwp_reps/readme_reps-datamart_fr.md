[In English](readme_reps-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [SRPE](readme_reps_fr.md) > SRPE sur le Datamart du SMC

# Données GRIB2 du Système régional de prévision d'ensemble (SRPE)

Cette page décrit les données du [système régional de prévision d'ensemble](readme_reps_fr.md) disponibles en format GRIB2.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier GRIB2.

Les données sont accessibles à l'adresse suivante :

* [https://dd.meteo.gc.ca/ensemble/reps/10km/grib2/{HH}/{hhh}](https://dd.meteo.gc.ca/ensemble/reps/10km/grib2)

où :

* __HH__ : Heure de la passe du modèle en UTC [00, 06, 12, 18]
* __hhh__ : Heure de la prévision [000, 003, 006, ..., 048]

Un historique de 24 heures est conservé dans ce répertoire.

## Spécification technique de la grille

![Grille du SRPE Rlatlon](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_reps/grille_reps_rlatlon.png)

Valeurs données aux paramètres de la grille lat-lon tournée à 10km de résolution:

| Paramètre | Valeur |
| ------ | ------ |
| ni | 908 |
| nj | 960 | 
| résolution à 60° N | 10km |
| coordonnées du premier point de grille | 50.76° N ; 20.81° W | 

__Note__ : Les [versions les plus récentes de wgrib2](https://www.cpc.ncep.noaa.gov/products/wesley/wgrib2/update_2.0.8.html) et [GDAL](https://gdal.org/) supportent ces grilles tournées. 

## Nomenclature des noms de fichiers 

Les fichiers ont la nomenclature suivante :

```
{YYYYMMDD}T{HH}Z_MSC_REPS_{VAR}_{LVLTYPE-LVL}_{Grille}{resolution}_PT{hhh}H.grib2
```

où :

* __YYYYMMDD__ : Année, mois et jour du début de la prévision
* __T__ : Délimiteur temporel selon les normes ISO8601
* __HH__ : Heure UTC de la passe [00, 06, 12, 18]
* __Z__ : Fuseau horaire (heure UTC)
* __MSC__ : Chaîne de caractères constante pour Meteorological Service of Canada, la source des données
* __REPS__ : Chaîne de caractères constante indiquant que les données proviennent du Système régional de prévision d'ensemble
* __VAR__ : Type de variable contenu dans le fichier (ex: UGRD). Ce paramètre comprend aussi le processus statistique associé si pertinent (ex: Accum, Max, Min). Voir aussi la note ci-dessous.
* __LVLTYPE-LVL__ : Niveau vertical et hauteur [ex: SFC pour la surface, AGL-10m pour 10m au-dessus du sol]
* __Grille__ : Grille horizontale [RLatLon]
* __resolution__ : 0.09. Signifie une résolution de 0.09°(environ 10km) dans les directions longitudinale et latitudinale
* __PT{hhh}H__ : Echéance temporelle selon la norme [ISO8601](https://en.wikipedia.org/wiki/ISO_8601). P, T et H sont des caractères constants désignant Période, Temps et Heure. "hhh" représente l’heure de prévision [000, 003, 006, ..., 072]
* __grib2__ : Chaîne de caractères constante indiquant que le format est GRIB2

Exemple de nom de fichier : 20201007T00Z_MSC_REPS_TPRATE-Accum24h_SFC_RLatLon0.09x0.09_PT024H.grib2

__Note__: Les fichiers contiennent par défaut tous les membres d'ensemble. Les fichiers contenant les __produits probabilistes__ sont identifiés via le paramètre '-Prob' attaché à la variable (ex: 20201007T00Z_MSC_REPS_TPRATE-Accum24h-Prob_SFC_RLatLon0.09x0.09_PT024H.grib2)

## Liste des variables

__Membres individuels:__ 

<table id="csv-table" class="display"></table>

<link href="https://cdn.jsdelivr.net/npm/simple-datatables@latest/dist/style.css" rel="stylesheet" type="text/css">
<script src="https://cdn.jsdelivr.net/npm/simple-datatables@latest"></script>
<script src="../../../js/variables_datatable.js" type="text/javascript"></script>
<script>
  loadTable("csv-table", "../../../assets/csv/REPS_fr.csv");
</script>

__Produits d'ensemble:__ 

<table id="csv-prob-table" class="display"></table>

<script>
  loadTable("csv-prob-table", "../../../assets/csv/REPS_prob_fr.csv");
</script>

Les fichiers contiennent des produits de probabilité par comptage de membre au-dessus ou au-dessous de différents seuils, des percentiles , moyennes, médianes et écarts-types. Notez que les produits et les seuils sont définis dans la méta-information des fichiers. Les produits suivants sont disponibles pour chacune des variables mentionnées ci-dessous.

###### HEATX

* Probabilité au-dessus de 298,14, 303,14, 308,14, 311,14, 313,14 and 315,14 K
* Minimum (percentile 0), maximum (100e percentile), médiane (50e percentile), écart-type et moyenne
* Percentile 10, percentile 25, percentile 75 et percentile 90

###### FPRATE

* Probabilité au-dessus de 0,2, 1, 2,5, 5, 10, 15, 20, 25, 30, 40 et 50 kg/(m<sup>2</sup>*s)
* Minimum (percentile 0), maximum (100e percentile), médiane (50e percentile), écart-type et moyenne
* Percentile 10, percentile 25, percentile 75 et percentile 90

###### IPRATE

* Probabilité au-dessus de 0,2, 1, 2,5, 5, 10, 15, 20, 25, 30, 40 et 50 kg/(m<sup>2</sup>*s)
* Minimum (percentile 0), maximum (100e percentile), médiane (50e percentile), écart-type et moyenne
* Percentile 10, percentile 25, percentile 75 et percentile 90

###### RPRATE

* Probabilité au-dessus de 0,2, 1, 2,5, 5, 10, 15, 20, 25, 30, 40, 50, 75, 100 et 150 kg/(m<sup>2</sup>*s)
* Minimum (percentile 0), maximum (100e percentile), médiane (50e percentile), écart-type et moyenne
* Percentile 10, percentile 25, percentile 75 et percentile 90

###### SPRATE

* Probabilité au-dessus de 0,2, 1, 2,5, 5, 10, 15, 20, 25, 30, 40, 50, 75 et 100 kg/(m<sup>2</sup>*s)
* Minimum (percentile 0), maximum (100e percentile), médiane (50e percentile), écart-type et moyenne
* Percentile 10, percentile 25, percentile 75 et percentile 90

###### TPRATE

* Probabilité au-dessus de 0,2, 1, 2,5, 5, 10, 15, 20, 25, 30, 40, 50, 75, 100 et 150 kg/(m<sup>2</sup>*s)
* Minimum (percentile 0), maximum (100e percentile), médiane (50e percentile), écart-type et moyenne
* Percentile 10, percentile 25, percentile 75 et percentile 90

###### TMP

* Probabilité au-dessus de 243,14, 248,14, 253,14, 258,14, 263,14, 268,14, 273,14, 278,14, 283,14, 288,14, 293,14, 298,14, 303,14, 308,14 et 313,14 K
* Probabilité au-dessous de 233,14, 238,14, 243,14, 248,14, 253,14, 258,14, 263,14, 268,14, 273,14, 278,14, 283,14, 288,14, 293,14 et 298,14 K
* Minimum (percentile 0), maximum (100e percentile), médiane (50e percentile), écart-type et moyenne
* Percentile 10, percentile 25, percentile 75 et percentile 90

###### WCF

* Probabilité au-dessous de 223,14, 228,14, 233,14, 238,14, 243,14, 248,14, 253,14, 258,14, 263,14, 268,14 et 273,14 K
* Minimum (percentile 0), maximum (100e percentile), médiane (50e percentile), écart-type et moyenne
* Percentile 10, percentile 25, percentile 75 et percentile 90

###### WIND

* Probabilité au-dessus de 5,5556, 8,3333, 10,278, 11,111, 13,889, 17,222, 18,056, 20,833, 24,444, 25, 27,778 et 32,778 m/s
* Minimum (percentile 0), maximum (100e percentile), médiane (50e percentile), écart-type et moyenne
* Percentile 10, percentile 25, percentile 75 et percentile 90

Une [liste en format XML](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_reps/reps_element.xml) contenant l'information pour toutes les variables de la grille 15km, y compris les descriptions et les unités, en français et en anglais est disponible.

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).
