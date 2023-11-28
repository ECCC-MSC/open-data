[In English](readme_ohps-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [SHOP](readme_ohps_fr.md) > SHOP sur le Datamart du SMC

# Données NetCDF du Système de simulation hydrodynamique opérationnelle (SHOP)

Cette page décrit les données d'analyses et de prévisions du [Système de simulation hydrodynamique opérationnelle](./readme_ohps_fr.md) disponibles en format NetCDF.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier NetCDF.

Les données sont accessibles à L'adresse suivante :

* [https://dd.meteo.gc.ca/model_ohps/slfe/100m/{HH}/{hhh}](https://dd.meteo.gc.ca/model_ohps/slfe/100m)

où :

* __HH__ : Heure UTC de référence [00, 01, 02, ..., 23]
* __hhh__ : Heure de prévision [001, 002, 003, ..., 048]

Les analyses sont disponibles aux heures dans chaque répertoire d'heures de référence [00, 01, ..., 23], sous l'échéance `000` des heures de prévision. Les prévisions sont disponibles pour chaque heure synoptique dans les répertoires [00, 06, 12, 18]

Un historique de 24 heures est conservé dans ce répertoire.

## Spécification technique de la grille

![](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_ohps/grille_ohps.png)

| Paramètre | Valeur |
| ------ | ------ |
| ni | 3600 |
| nj | 2700 | 
| résolution à 60° N | 100m |
| Angle (entre 0 et 360, dans le sens inverse des aiguilles d'une montre) entre le méridien de Greenwich et l'axe horizontal de la grille.e | 343° | 

## Nomenclature des noms de fichiers 

Les fichiers ont la nomenclature suivante :

* Prévisions : `{YYYYMMDD}T{HH}Z_MSC_OHPS-{DOMAIN}_{VAR}_{LVL}_{Grille}{resolution}_PT{hhh}H.nc`
* Analyses : `{YYYYMMDD}T{HH}Z_MSC_OHPS-{DOMAIN}_{VAR}_{LVL}_{Grille}{resolution}_PT0H.nc`

où :

* __YYYYMMDD__ : Année, mois et jour du début de la prévision
* __T__ : Séparateur de temps selon les normes ISO8601
* __HH__ : Heure UTC de référence [00, 01, 02, ..., 23]
* __MSC__ : Chaîne de caractères constante indiquant que le Service Météorologique Canadien émet les prévisions
* __OHPS__ : Chaîne de caractères constante indiquant que les données proviennent du Système de simulation hydrodynamique opérationnelle
* __DOMAIN__ : Chaîne de caractères constante indiquant le domaine [SLFE, pour "Saint Lawrence Fluvial Estuary"]
* __VAR__ : Type de variable contenue dans le fichier
* __LVL__ : Type de niveau vertical [Sfc pour la surface, DBS-Avg pour la moyenne sous la surface de l'eau]
* __Grille__ : Type de grille horizontale [PS pour grille polaire stéréographique]
* __resolution__ : Indique la résolution [100m]
* __PT{hhh}H__ : Echéance temporelle selon la norme [ISO8601](https://en.wikipedia.org/wiki/ISO_8601). P, T et H sont des caractères constants désignant la période, le temps et l'heure. "hhh" représente l’heure de prévision  [001, 002, ..., 048]
* __PT0H__ : Chaîne de caractères constante indiquant une analyse, basée sur les normes ISO8601. P, T et H sont des caractères constants désignant la période, le temps et l'heure.
* __nc__ : Chaîne de caractères constante indiquant que le format est NetCDF

Exemples de fichier :

* 20230911T18Z_MSC_OHPS-SLFE_WaterLvlRiver_Sfc_PS100m_PT029H.nc
* 20230911T18Z_MSC_OPHS-SLFE_RiverVelocityY_DBS-Avg_PS100m_PT005H.nc
* 20231009T07Z_MSC_OHPS-SLFE_WaterLvlRiver_Sfc_PS100m_PT0H.nc

## Liste des variables

<table id="csv-table" class="display"></table>

<link href="https://cdn.jsdelivr.net/npm/simple-datatables@latest/dist/style.css" rel="stylesheet" type="text/css">
<script src="https://cdn.jsdelivr.net/npm/simple-datatables@latest"></script>
<script src="../../../js/variables_datatable.js" type="text/javascript"></script>
<script>
  loadTable("csv-table", "../../../assets/csv/OHPS_Variables-List_fr.csv");
</script>

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).
