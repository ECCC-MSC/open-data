[In English](readme_gdwps-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [SGPDV](readme_gdwps_fr.md) > SGPDV sur le Datamart du SMC

# Données GRIB2 du Système Global de Prévision Déterministe de Vague (SGPDV)

Cette page décrit les données [Système Global de Prévision Déterministe de Vague (SGPDV)](readme_gdwps_fr.md) disponibles en format GRIB2.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier GRIB2.

Les données sont accessibles à adresse suivante :

* [https://dd.meteo.gc.ca/model_gdwps/25km/{HH}/](https://dd.meteo.gc.ca/model_gdwps/25km/)

où :

* __HH__ : Heure UTC du début de la passe du modèle [00, 12].

Un historique de 24 heures est conservé dans ce répertoire.

## Domaines disponibles

Grille latitude-longitude globale.

| Paramètre | Valeur |
| ------ | ------ |
| ni | 1440 |
| nj | 721 | 
| résolution | 0.25° |
| coordonnées du premier point de grille | 90° S  0° E | 

## Nomenclature des noms de fichiers 

NOTE: TOUTES LES HEURES SONT EN UTC.

Les fichiers ont la nomenclature suivante :

`{YYYYMMDD}T{HH}Z_MSC_GDWPS_{VAR}_{LVL}_{Grille}{resolution}_PT{hhh}H.grib2`

où :

* __YYYYMMDD__ : Année, mois et jour du début de la prévision
* __T__ : Séparateur de temps selon les normes ISO8601
* __HH__ : Heure UTC de la passe [00, 12]
* __MSC__ : Chaîne de caractères constante indiquant que le Service Météorologique Canadien émet les prévisions
* __GDWPS__ : Chaîne de caractères constante indiquant que les données proviennent du Système global de prévision déterministe des vagues
* __VAR__ : Type de variable contenu dans le fichier
* __LVL__ : Type de niveau vertical [Sfc pour la surface, AGL pour hauteur fixe au-dessus du sol]
* __Grille__ : Type de grille horizontale [LatLon]
* __resolution__ : Indique la résolution en degré dans les directions longitudinale et latitudinale [0.25]
* __PT{hhh}H__ : Echéance temporelle selon la norme [ISO8601](https://en.wikipedia.org/wiki/ISO_8601). P, T et H sont des caractères constants désignant Période, Temps et Heure. "hhh" représente l’heure de prévision  [000, 001, 002, ..., 048, 051, ..., 120]
* __grib2__ : Chaîne de caractères constante indiquant que le format est GRIB2.

Exemple de fichier :

20211007T00Z_MSC_GDWPS_HTSGW_Sfc_LatLon0.25_PT051H.grib2

Le fichier a été créé par le SMC et contient une prévision du Système global de prévision déterministe des vagues. Il contient la hauteur significative des vagues (HTSGW) pour le monde au niveau de la surface sur une grille lat/long à une résolution de 0.25 degré par 0.25 degré. Il débute le 7 octobre 2021 à 00Z (2021100700). Il contient l’heure de prévision 51 (PT051H) en format GRIB2 (.grib2).

## Liste des variables

<table id="csv-table" class="display"></table>

<link href="https://cdn.jsdelivr.net/npm/simple-datatables@latest/dist/style.css" rel="stylesheet" type="text/css">
<script src="https://cdn.jsdelivr.net/npm/simple-datatables@latest"></script>
<script src="../../../js/variables_datatable.js" type="text/javascript"></script>
<script>
  loadTable("csv-table", "../../../assets/csv/GDWPS_fr.csv");
</script>

### Notes

* La direction des composantes u et v du vecteur vent doit être résolue selon les composantes i, j de la grille définie et dans la direction croissante des coordonnées i, j.

* À chaque point du domaine, le spectre d’énergie des vagues peut être divisé entre la mer de vent et un certain nombre de houles. Les deux houles qui contiennent le plus d’énergie sont désignées dans l’ordre comme la première et la deuxième houle. Les paramètres de mer de vent et ceux de houles peuvent être indéfinis à certains points du domaine, pour les premiers s’il y a peu de vent et pour les seconds s’il n’y a que des vagues générées localement.

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).




