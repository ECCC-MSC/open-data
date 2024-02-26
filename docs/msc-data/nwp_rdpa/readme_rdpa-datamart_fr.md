[In English](readme_rdpa-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [ARDP](readme_rdpa_fr.md) > ARDP sur le Datamart du SMC

# Données GRIB2 de l'Analyse Régionale Déterministe de Précipitation (ARDP - CaPA)

Cette page décrit les données de L’[Analyse régionale déterministe de précipitation (ARDP)](readme_rdpa_fr.md), fondée sur le système CaPA (Canadian Precipitation Analysis).

# Adresse des données

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier GRIB2.

Les données sur une grille lat-lon tournée sont accessibles à l'adresse suivante :

* [https://dd.meteo.gc.ca/model_rdpa/10km/{HH}/](https://dd.meteo.gc.ca/model_rdpa/10km)

où :

* __hh__ : Heure finale d’accumulation de précipitation [06, 24]
* __HH__ : Heure UTC de la passe [00, 06, 12, 18]

Un historique de 30 jours est conservé sur le Datamart du SMC.

## Spécification technique de la grille

![Grille RDPA Rlatlon](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_rdpa/grille_rdpa_rlatlon.png)

Valeurs données aux paramètres de la grille lat-lon tournée:

| Paramètre | Valeur |
| ------ | ------ |
| ni | 1102 |
| nj | 1076 | 
| résolution à 60° N | 10km |
| coordonnées du premier point de grille | -31.76° N ; 92.40° W |

__Note__ : Les [versions les plus récentes de wgrib2](https://www.cpc.ncep.noaa.gov/products/wesley/wgrib2/update_2.0.8.html) et [GDAL](https://gdal.org/) supportent ces grilles tournées.

## Nomenclature des noms de fichiers 

Les fichiers ont une des nomenclatures suivantes :

* `{YYYYMMDD}T{HH}Z_MSC_RDPA_{VAR}_Sfc_RLatLon0.09_PT0H.grib2`
* `{YYYYMMDD}T{HH}Z_MSC_RDPA-Prelim_{VAR}_Sfc_RLatLon0.09_PT0H.grib2`

où :

* __YYYYMMDD__: Année, mois et jour du début de la prévision 
* __T__ : Délimiteur temporel selon les normes ISO8601
* __HH__: Heure UTC de la passe [00, 06, 12, 18]
* __Z__ : Fuseau horaire (heure UTC)
* __MSC__ : Chaîne de caractères constante pour Meteorological Service of Canada, la source des données
* __RDPA__ : Chaîne de caractères constante indiquant le modèle source Analyse régionale de prévision déterministe. Temps de coupure de 7 heures pour les observations après l'heure YYYYMMDDHH, indiquant qu'un maximum d'observations a probablement été recueilli
* __RDPA-Prelim__: Chaîne de caractères constante indiquant le modèle source Analyse régionale de prévision déterministe. Temps de coupure des observations à l'intérieur d'une heure après l'heure YYYYMMDDHH, indiquant que toutes les observations n'ont possiblement pas été recueillies
* __VAR__ : Chaîne de caractères constante donnant le nom de la variable contenue dans le fichier. Ici, il s’agit de l’analyse de précipitation accumulée sur une certaine période [APCP-Accum6h, APCP-Accum24h]
* __Sfc__ : Indique que le type de niveau est la surface
* __RLatLon0.09__: Chaîne de caractères constante indiquant une grille lat-lon tournée à 0.09deg de résolution (environ 10km)
* __PT0H__: Basé sur les normes ISO8601. P, T et H sont des caractères constants indiquant respectivement la période, le temps et l'heure. Ici, PT0H indique qu'il s'agit d'une analyse
* __grib2__:  Indique que les données sont en format GRIB2

Exemples de noms de fichiers :

* 20220301T00Z_MSC_RDPA-Prelim_APCP-Accum6h_Sfc_RLatLon0.09_PT0H.grib2

Le fichier a été créé par le Service météorologique canadien (MSC) et contient une analyse régionale déterministe de précipitation (RDPA). Il contient une analyse préliminaire d’accumulation de précipitation représentée par la variable APCP et ce sur un intervalle de 6 heures. Les données sont sur une grille tournée lat-lon à une résolution de 10 km (RLatLon0.09). L’analyse a été produite le 01 mars 2022 à 00Z (20220301T00Z). L’intervalle de 006 heures dans lequel les précipitations sont analysées est de 2022030100 à 2022030106.

* 20220302T12Z_MSC_RDPA_APCP-Accum24h_Sfc_RLatLon0.09_PT0H.grib2

Le fichier a été créé par le Service météorologique canadien (MSC) et contient une analyse régionale déterministe de précipitation (RDPA). Il contient une analyse finale d’accumulation de précipitation représentée par la variable APCP et ce sur un intervalle de 24 heures. Les données sont sur une grille lat-lon tournée à une résolution de 10 km (RLatLon0.09). L’analyse a été produite le 02 mars 2022 à 12Z (2022030212). L’intervalle de 24 heures dans lequel les précipitations sont analysées est de 2022030212 à 2022030312.

__NOTE__ : Même si ce n’est pas indiqué dans le nom du fichier, le fichier contiendra aussi l’indice de confiance de l’analyse (CFIA) associé à l’analyse de précipitation.

## Liste des variables

<table id="csv-table" class="display"></table>

<link href="https://cdn.jsdelivr.net/npm/simple-datatables@latest/dist/style.css" rel="stylesheet" type="text/css">
<script src="https://cdn.jsdelivr.net/npm/simple-datatables@latest"></script>
<script src="../../../js/variables_datatable.js" type="text/javascript"></script>
<script>
  loadTable("csv-table", "../../../assets/csv/RDPA_Variables-List_fr.csv");
</script>

## Archives en ligne

* Une [archive des données de l'ARDP](https://collaboration.cmc.ec.gc.ca/science/outgoing/capa.grib/) depuis le 6 avril 2011 jusqu'au 24 septembre 2023 est disponible en ligne, en format GRIB2.

* Une [archive des ré-analyses](https://collaboration.cmc.ec.gc.ca/science/outgoing/capa.grib/hindcast/), couvrant la période de janvier 2002 à juin 2012, est disponible en ligne, en format GRIB2.

## Support

Pour toute question relative à ces données, merci de [nous contacter](https://meteo.gc.ca/mainmenu/contact_us_f.html).

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).
