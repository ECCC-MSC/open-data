[In English](readme_geps-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [SGPE](readme_geps_fr.md) > SGPE sur le Datamart du SMC

# Données GRIB2 du Système global de prévision d'ensemble (SGPE)

Cette page décrit les données du [Système global de prévision d'ensemble](readme_geps_fr.md) disponibles en format GRIB2.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le Protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier GRIB2. 

Les données sont accessibles aux adresses suivantes :

* [https://dd.meteo.gc.ca/ensemble/geps/grib2/{TYPE}/{HH}/{hhh}/](https://dd.meteo.gc.ca/ensemble/geps/grib2)

où :

* __TYPE__ : Chaîne de caractères indiquant les membres individuels issus des sorties directes de modèle (pas de traitement) ou les produits probabilistes créés à partir des membres individuels [raw, products]
* __raw__ : Chaîne de caractères constante indiquant les sorties brutes du modèle
* __HH__ : Heure UTC du début de la passe du modèle [00, 12]
* __hhh__ : Heure de prévision [000, 003, 006, ..., 192, 198, 204, ..., 378, 384] et [000, 003, …, 192, 198, 204, ..., 762, 768] chaque jeudi à 000UTC

## Spécification technique de la grille

Ce tableau décrit des paramètres de la grille latitude-longitude sur laquelle les variables en format GRIB sont disponibles.

| Paramètre de la grille                                          | Valeur du paramètre      |
|-----------------------------------------------------------------|--------------------------|
| ni                                                              | 720 points               |
| nj                                                              | 361 points               |
| résolution                                                      | 0,5°                     |
| coordonnées du premier point de grille                          | 90° S  000° E            |

## Nomenclature des noms de fichiers 

NOTE : TOUTES LES HEURES SONT EN UTC.

Les fichiers ont la nomenclature suivante :

* CMC_geps-raw_Variable_TypedeNiveau_Niveau_latlonResolution_YYYYMMDDHH_Phhh_allmbrs.grib2
* CMC_geps-prob_Variable_TypedeNiveau_Niveau_latlonResolution_YYYYMMDDHH_Phhh_all-products.grib2

où :

* __CMC_geps__ : Chaîne de caractères constante indiquant que le Centre météorologique canadien (CMC) émet les prévisions, le modèle (geps : Global Ensemble Prediction System).
* __raw__ : sorties brutes des membres individuels 
* __prob__ : produits probabilistes générés à partir de tous les membres
* __Resolution__ : Chaîne de caractères constante indiquant la résolution des données (0p5x0p5).
* __Variable__ : Type de variable contenu dans le fichier. Pour voir la liste complète, consultez la section « Description des variables ».
* __TypedeNiveau__ : Type de niveau. Pour voir la liste complète, consultez la section « Description des variables ».
* __Niveau__ : Valeur du niveau. Pour voir la liste complète, consultez la section « Description des variables ».
* __YYYYMMDD__ : Année, mois et jour du début de la prévision.
* __HH__ : Heure UTC de la passe [00, 12].
* __Phhh__ : « P » est un caractère constant. « hhh » représente l’heure de prévision [000, 003, …, 192, 198, 204, ..., 378, 384], ou [000, 003, …, 192, 198, 204, ..., 762, 768] chaque jeudi à 000UTC.
* __allmbrs__ : Chaîne de caractères constante indiquant que tous les membres sont inclus dans le fichier.
* __all-products__ : Indique que tous les produits probabilistes pour cette variable sont regroupés dans ce fichier
* __grib2__ : Chaîne de caractères constante indiquant que le format est GRIB2.

Exemple de nom de fichier :

CMC_geps-raw_UGRD_ISBL_0925_latlon0p5x0p5_2010090100_P078_allmbrs.grib2

Les données dans le fichier débutent le 1 septembre 2010 à 00Z (2010090100). Il a été créé par le CMC et contient les données brutes du Système global de prévision d'ensemble (CMC_geps-raw). Il contient les composantes du vent selon U (UGRD), au niveau isobarique 925 mb (ISBL_0925), à l’heure de prévision 78 (P078), pour tous les membres de l’ensemble (allmbrs), le tout en format GRIB2 (.grib2).

## Liste des variables

__Membres individuels__:

<table id="csv-table" class="display"></table>

<link href="https://cdn.jsdelivr.net/npm/simple-datatables@latest/dist/style.css" rel="stylesheet" type="text/css">
<script src="https://cdn.jsdelivr.net/npm/simple-datatables@latest"></script>
<script src="../../../js/variables_datatable.js" type="text/javascript"></script>
<script>
  loadTable("csv-table", "../../../assets/csv/GEPS_fr.csv", "FR");
</script>

__Produits d'ensemble__:

<table id="csv-prob-table" class="display"></table>

<script>
  loadTable("csv-prob-table", "../../../assets/csv/GEPS_prob_fr.csv", "FR");
</script>

Les fichiers contiennent des produits de probabilité par comptage de membre au-dessus ou au-dessous de différents seuils, des percentiles , moyennes, médianes et écarts-types. Notez que les produits et les seuils sont définis dans la méta-information des fichiers. Les produits suivants sont disponibles pour chacune des variables mentionnées ci-dessous.

###### HGT

* Minimum (percentile 0), maximum (100e percentile), écart-type et moyenne

###### HEATX

* Probabilité au-dessus de 298,14, 303,14, 308,14, 311,14, 313,14 et 315,14 K
* Minimum (percentile 0), maximum (100e percentile), médiane (50e percentile), écart-type et moyenne
* Percentile 10, percentile 25, percentile 75 et percentile 90

###### FPRATE

* Probabilité au-dessus de 1, 2,5, 5, 10, 15, 20, 25, 30, 40 et 50 kg/(m<sup>2</sup>*s)
* Minimum (percentile 0), maximum (100e percentile), médiane (50e percentile), écart-type et moyenne
* Percentile 10, percentile 25, percentile 75 et percentile 90

###### IPRATE

* Probabilité au-dessus de 1, 2,5, 5, 10, 15, 20, 25, 30, 40 et 50 kg/(m<sup>2</sup>*s)
* Minimum (percentile 0), maximum (100e percentile), médiane (50e percentile), écart-type et moyenne
* Percentile 10, percentile 25, percentile 75 et percentile 90

###### RPRATE

* Probabilité au-dessus de 1, 2,5, 5, 10, 15, 20, 25, 30, 40, 50, 75, 100 et 150 kg/(m<sup>2</sup>*s)
* Minimum (percentile 0), maximum (100e percentile), médiane (50e percentile), écart-type et moyenne
* Percentile 10, percentile 25, percentile 75 et percentile 90

###### SPRATE

* Probabilité au-dessus de 1, 2,5, 5, 10, 15, 20, 25, 30, 40, 50 et 75 kg/(m<sup>2</sup>*s)
* Minimum (percentile 0), maximum (100e percentile), médiane (50e percentile), écart-type et moyenne
* Percentile 10, percentile 25, percentile 75 et percentile 90

###### TPRATE

* Probabilité au-dessus de 1, 2,5, 5, 10, 15, 20, 25, 30, 40, 50, 75, 100 et 150 kg/(m<sup>2</sup>*s)
* Minimum (percentile 0), maximum (100e percentile), médiane (50e percentile), écart-type et moyenne
* Percentile 10, percentile 25, percentile 75 et percentile 90

###### PRMSL

* Minimum (percentile 0), maximum (100e percentile), écart-type et moyenne

###### TMP

* Probabilité au-dessus de 243,14, 248,14, 253,14, 258,14, 263,14, 268,14, 273,14, 278,14, 283,14, 288,14, 293,14, 298,14, 303,14, 308,14 et 313,14 K
* Probabilité au-dessous de 238,14, 243,14, 248,14, 253,14, 258,14, 263,14, 268,14, 273,14, 278,14, 283,14, 288,14, 293,14 and 298,14 K
* Minimum (percentile 0), maximum (100e percentile), médiane (50e percentile), écart-type et moyenne
* Percentile 10, percentile 25, percentile 75 et percentile 90

###### TCDC

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

Note: Une [liste en format XML](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_geps/geps_element.xml) contenant l'information pour toutes les variables, y compris les descriptions et les unités, en français et en anglais est disponible.

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).




























