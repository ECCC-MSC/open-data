[In English](readme_resps-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../../readme_fr.md) > [SRPEOT](readme_resps_fr.md) > SRPEOT sur le Datamart du SMC

# Données NetCDF du Système régional de prévision d'ensemble d'onde de tempête (SRPEOT)

Cette page décrit les données du [Système régional de prévision d'ensemble d'onde de tempête (SRPEOT)](readme_resps_fr.md) disponibles en format NetCDF.

## Adresse des données

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier NetCDF.

Les données sont accessibles à l'adresse suivante :

* [https://dd.meteo.gc.ca/model_resps/atlantic-nw/9km/{HH}/](https://dd.meteo.gc.ca/model_resps/atlantic-nw/9km)

où :

* __HH__ : Heure UTC du début de la passe du modèle [00, 12]

Un historique de 24 heures est conservé dans ce répertoire.

## Spécification technique de la grille

![Image de la grille du SRPEOT](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_resps/grille_resps.png)

Ce tableau répertorie les valeurs de divers paramètres de la grille :

| Paramètre | Valeur |
| ------ | ------ |
| ni | 333 |
| nj | 217 |
| résolution | 0.083° x 0.083° |

## Nomenclature des noms de fichiers

NOTE: TOUTES LES HEURES SONT EN UTC.

Les noms de fichiers ont la nomenclature suivante :

`{YYYYMMDD}T{HH}Z_MSC_RESPS-Atlantic-North-West_{VAR}_{LVL}_{Grille}{resolution}_PT{hhh}H.nc` 

où :

* __YYYYMMDD__ : Année, mois et jour du début de la prévision
* __T__ : Délimiteur temporel selon les normes ISO8601
* __HH__ : Heure UTC de la passe [00, 12]
* __Z__ : Fuseau horaire (heure UTC)
* __MSC__ : Chaîne de caractères constante pour Meteorological Service of Canada, la source des données 
* __RESPS-Atlantic-North-West__ : Chaîne de caractères constante indiquant que les données proviennent du Système régional de prévision d'ensemble d'onde de tempête sur le domaine nord ouest
* __VAR__ : Type de variable contenue dans le fichier [ETAS, SSH]
* __LVL__ : Niveau vertical [Sfc pour la surface]
* __Grille__ : Grille horizontale lat-lon [LatLon]
* __resolution__ : Indique la résolution en degré dans les directions longitudinale et latitudinale [0.083]
* __PT{hhh}H__ : Echéance temporelle selon la norme [ISO8601](https://en.wikipedia.org/wiki/ISO_8601). P, T et H sont des caractères constants désignant Période, Temps et Heure. "hhh" représente l’heure de prévision  [000, 001, 002, ..., 240]
* __nc__ : Chaîne de caractères constante indiquant que le format est NetCDF

Exemple de fichier :

20180417T12Z_MSC_RESPS-Atlantic-North-West_ETAS_Sfc_LatLon0.083_PT024H.nc

##   Liste de variables

<table id="csv-table" class="display"></table>

<link href="https://cdn.jsdelivr.net/npm/simple-datatables@latest/dist/style.css" rel="stylesheet" type="text/css">
<script src="https://cdn.jsdelivr.net/npm/simple-datatables@latest"></script>
<script src="../../../js/variables_datatable.js" type="text/javascript"></script>
<script>
  loadTable("csv-table", "../../../assets/csv/RESPS_fr.csv");
</script>

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Annonces de la liste de diffusion dd_info

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info.comm.collab.science.gc.ca/).
