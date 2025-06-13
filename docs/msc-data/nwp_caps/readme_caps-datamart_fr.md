[In English](readme_caps-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [SCPA](readme_caps_fr.md) > SCPA sur le Datamart du SMC

# Données du Système canadien de prévision de l'Arctique (SCPA) expérimental

Cette page décrit les données expérimentales atmosphériques en format GRIB2 et océaniques en format NetCDF du [Système canadien de prévision de l'Arctique (SCPA)](./readme_caps_fr.md) disponibles sur le Datamart du SMC.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à des fichiers GRIB2 et NetCDF.

Les données sont accessibles à l’adresse suivante :

* [https://dd.meteo.gc.ca/model_caps/3km/{HH}/{hhh}](https://dd.meteo.gc.ca/model_caps/3km/) 

où :

* __HH__ : Heure UTC du début de la passe du modèle [00, 12] 
* __hhh__ : Heure de prévision [000, 001, 002, ..., 048]

## Spécification technique de la grille

![Image de la grille lat-lon tournée du domaine SCPA](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_hrdps-north/grilleRLatLon_hrdps-north.png)

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

`{YYYYMMDD}T{HH}Z_MSC_CAPS_{VAR}_{LVLTYPE-LVL}_ {Grille}(resolution)_PT{hhh}H.{format}`

où :

* __YYYYMMDD__ : Année, mois et jour du début de la prévision
* __T__ : Délimiteur temporel selon les normes ISO8601
* __HH__ : Heure UTC de la passe [00, 12]
* __Z__ : Fuseau horaire (heure UTC)
* __MSC__ : Chaîne de caractères constante pour Meteorological Service of Canada, la source des données
* __CAPS__ : Chaîne de caractères constante indiquant que les données proviennent du Système canadien de prévision de l'Arctique (CAPS en anglais) 
* __VAR__ : Variable atmosphérique/océanique contenue dans le fichier (ex: AirTemp).
* __LVLTYPE-LVL__ : Niveau vertical et hauteur [ex: Sfc pour la surface, EAtm pour l’intégrale de la colonne, AGL-10m pour la hauteur de 10m au-dessus du sol]
* __Grille__ : Grille horizontale [RLatLon]
* __resolution__ : 0.03. Signifie une résolution de 0.03°(environ 3km) dans les directions longitudinale et latitudinale
* __PT{hhh}H__ : Echéance temporelle selon la norme [ISO8601](https://en.wikipedia.org/wiki/ISO_8601). P, T et H sont des caractères constants désignant Période, Temps et Heure. "hhh" représente l’heure de prévision [000, 001, 002, ..., 048]
* __format__ : Chaîne de caractères constante indiquant le format des données  contenues dans le fichier format [`grib2`, pour les variables atmosphériques en format GRIB2; `nc`, pour les variables océaniques en format NetCDF]

Exemples de noms de fichier : 

* 20250530T00Z_MSC_CAPS_SnowDepth_Sfc_RLatLon0.03_PT012H.grib2
* 20250603T12Z_MSC_CAPS_SeaIceDivergence_Sfc_RLatLon0.03_PT012H.nc

## Liste des variables

* Liste des variables atmosphériques :

<table id="csv-table" class="display"></table>

<link href="https://cdn.jsdelivr.net/npm/simple-datatables@latest/dist/style.css" rel="stylesheet" type="text/css">
<script src="https://cdn.jsdelivr.net/npm/simple-datatables@latest"></script>
<script src="../../../js/variables_datatable.js" type="text/javascript"></script>
<script>
  loadTable("csv-table", "../../../assets/csv/HRDPS-North_Variables-List_fr.csv");
</script>

* Liste des variables océaniques :

<table id="csv-table-netcdf" class="display"></table>

<link href="https://cdn.jsdelivr.net/npm/simple-datatables@latest/dist/style.css" rel="stylesheet" type="text/css">
<script src="https://cdn.jsdelivr.net/npm/simple-datatables@latest"></script>
<script src="../../../js/variables_datatable.js" type="text/javascript"></script>
<script>
  loadTable("csv-table-netcdf", "../../../assets/csv/RIOPS_Variables-List_fr.csv");
</script>

## Support

Pour toute question relative à ces données, merci de [nous contacter](https://meteo.gc.ca/mainmenu/contact_us_f.html).

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).

