[In English](readme_hrdps-north-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [SHRPD-Nord](readme_hrdps-north_fr.md) > SHRPD-Nord sur le Datamart du SMC

# Données GRIB2 du Système à Haute Résolution de Prévision Déterministe Nord (SHRPD-Nord)

Cette page décrit toutes les données du [Système à Haute Résolution de Prévision Déterministe Nord (SHRPD-Nord)](readme_hrdps-north_fr.md) expérimental disponibles en format GRIB2 sur une grille lat-lon tournée à 3km de résolution sur un domaine étendu.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier GRIB2.

Les données sont accessibles aux adresses suivantes :

* [https://dd.meteo.gc.ca/model_hrdps/north/3km/{HH}/{hhh}/](https://dd.meteo.gc.ca/model_hrdps/north/3km/)

où :

* __HH__ : Heure UTC du début de la passe du modèle [00, 12] 
* __hhh__ : Heure de prévision [000, 001, 002, ..., 048]

Note: Certains algorithmes des éléments du temps sur grille ("WEonG") ont besoin des valeurs des variables à `t-1`, afin d'uniformiser l'offre de données, les heures de prévision débutent à 001h.

## Spécification technique de la grille 

![Image de la grille lat-lon tournée du domaine nord du SHRPD](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_hrdps-north/grilleRLatLon_hrdps-north.png)

Valeurs données aux paramètres de la grille lat-lon tournée à 3km de résolution:

| Paramètre | Valeur |
| ------ | ------ |
| ni | 2230 |
| nj | 1830 | 
| résolution à 60° N | 3 km |
| coordonnées du premier point de grille | 0°N ; 97°W |

__Note__ : Les [versions les plus récentes de wgrib2](https://www.cpc.ncep.noaa.gov/products/wesley/wgrib2/update_2.0.8.html) et [GDAL](https://gdal.org/) supportent ces grilles tournées. 

## Nomenclature des noms de fichiers

Les fichiers ont la nomenclature suivante :

* `{YYYYMMDD}T{HH}Z_MSC_HRDPS-North_{VAR}_{LVLTYPE-LVL}_{Grille}{resolution}_PT{hhh}H.grib2`
* `{YYYYMMDD}T{HH}Z_MSC_HRDPS-North-WEonG_{VAR}_{LVLTYPE-LVL}_{Grille}{resolution}_PT{hhh}H.grib2`

où :

* __YYYYMMDD__ : Année, mois et jour du début de la prévision
* __T__ : Délimiteur temporel selon les normes ISO8601
* __HH__ : Heure UTC de la passe [00, 12]
* __Z__ : Fuseau horaire (heure UTC)
* __MSC__ : Chaîne de caractères constante pour Meteorological Service of Canada, la source des données
* __HRDPS-North__ : Chaîne de caractères constante indiquant que les données proviennent du Système haute résolution de prévision déterministe Nord
* __HRDPS-WEonG__ : Chaîne de caractères constante indiquant que les données proviennent des éléments du temps sur grille ("WEonG") du Système haute résolution de prévision déterministe Nord
* __VAR__ : Type de variable contenu dans le fichier (ex: UGRD).
* __LVLTYPE-LVL__ : Niveau vertical et hauteur [ex: Sfc pour la surface, EATM pour l’intégrale de la colonne, DBS-10-20cm couche entre 10 et 20cm sous la surface, AGL-10m pour la hauteur de 10m au-dessus du sol]
* __Grille__ : Grille horizontale [RLatLon]
* __resolution__ : 0.03. Signifie une résolution de 0.03°(environ 3km) dans les directions longitudinale et latitudinale
* __PT{hhh}H__ : Echéance temporelle selon la norme [ISO8601](https://en.wikipedia.org/wiki/ISO_8601). P, T et H sont des caractères constants désignant Période, Temps et Heure. "hhh" représente l’heure de prévision [000, 001, 002, ..., 048]
* __grib2__ : Chaîne de caractères constante indiquant que le format est GRIB2.

Exemples de noms de fichier :

* 20231210T00Z_MSC_HRDPS-North_GUST_AGL-10m_RLatLon0.03_PT012H.grib2
* 20231211T12Z_MSC_HRDPS-North-WEonG_VISIFG_Sfc_RLatLon0.03_PT024H.grib2

## Liste des variables

Cette liste contient à la fois les paramètres générés à partir des sorties du SHRPD-Nord mais aussi les éléments du temps sur grille (*HRDPS-WEonG*) calculés en post-traitement. 

<table id="csv-table" class="display"></table>

<link href="https://cdn.jsdelivr.net/npm/simple-datatables@latest/dist/style.css" rel="stylesheet" type="text/css">
<script src="https://cdn.jsdelivr.net/npm/simple-datatables@latest"></script>
<script src="../../../js/variables_datatable.js" type="text/javascript"></script>
<script>
  loadTable("csv-table", "../../../assets/csv/HRDPS-North_Variables-List_fr.csv");
</script>

## Support

Pour toute question relative à ces données, merci de [communiquer avec nous](https://meteo.gc.ca/mainmenu/contact_us_f.html).

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).




