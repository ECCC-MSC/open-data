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

## Spécification technique de la grille

Les données du SRPEV sont disponibles sur le domaine des Grands Lacs.

![Image de la grille du SRPEV](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_rewps/grille_rewps_grl.png)

Ce tableau répertorie les valeurs de divers paramètres de la grille :

| Paramètre | Valeur |
| ------ | ------ |
| ni | 550 |
| nj | 365 |
| résolution | 0.0224° x 0.0310° |
| coordonnées du premier point de grille | 41.0984° N  92.4790° O |

## Nomenclature des noms de fichiers

NOTE: TOUTES LES HEURES SONT EN UTC.

Les fichiers ont la nomenclature suivante :

`{YYYYMMDD}T{HH}Z_MSC_REWPS-{DOMAIN}_{VAR}_{LVL}_{Grille}{resolution}_PT{hhh}H.grib2`

où :

* __YYYYMMDD__ : Année, mois et jour du début de la prévision
* __T__ : Séparateur de temps selon les normes ISO8601
* __HH__ : Heure UTC de la passe [00, 12]
* __Z__ : Fuseau horaire (heure UTC)
* __MSC__ : Chaîne de caractères constante indiquant que le Service Météorologique Canadien émet les prévisions.
* __REWPS__ : Chaîne de caractères constante indiquant que les données proviennent du Système régional de prévision d'ensemble des vagues
* __DOMAIN__ : Chaîne de caractères indiquant le domaine [Great-Lakes]
* __VAR__ : Type de variable contenu dans le fichier
* __LVL__ : Type de niveau vertical [Sfc pour la surface]
* __Grille__ : Type de grille horizontale [LatLon]
* __resolution__ : Indique la résolution en degré dans les directions longitudinale et latitudinale [0.022x0.031]
* __PT{hhh}H__ : Echéance temporelle selon la norme [ISO8601](https://en.wikipedia.org/wiki/ISO_8601). P, T et H sont des caractères constants désignant Période, Temps et Heure. "hhh" représente l’heure de prévision [000, 003, 006, ..., 072]
* __grib2__ : Chaîne de caractères constante indiquant que le format est GRIB2

Exemple de fichier :

20210202T12Z_MSC_REWPS-Great-Lakes_HTSGW_Sfc_LatLon0.022x0.031_PT066H.grib2

## Liste des variables

<table id="csv-table" class="display"></table>

<link href="https://cdn.jsdelivr.net/npm/simple-datatables@latest/dist/style.css" rel="stylesheet" type="text/css">
<script src="https://cdn.jsdelivr.net/npm/simple-datatables@latest"></script>
<script src="../../../js/variables_datatable.js" type="text/javascript"></script>
<script>
  loadTable("csv-table", "../../../assets/csv/REWPS_fr.csv", "FR");
</script>

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Annonces de la liste de diffusion dd_info

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).


