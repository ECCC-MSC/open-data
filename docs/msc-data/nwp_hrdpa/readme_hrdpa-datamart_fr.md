[In English](readme_hrdpa-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [AHRDP](readme_hrdpa_fr.md) > AHRDP sur le Datamart du SMC

# Données GRIB2 de l'Analyse à haute résolution déterministe de précipitation (AHRDP)

Cette page décrit les données de l'[Analyse à haute résolution déterministe de précipitation](./readme_hrdpa-datamart_fr.md) disponibles en format GRIB2.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier GRIB2.

Les données sont accessibles aux adresses suivantes :

* Données sur grille polaire stéréographique:[https://dd.meteo.gc.ca/analysis/precip/hrdpa/grib2/polar_stereographic/{hh}](https://dd.meteo.gc.ca/analysis/precip/hrdpa/grib2/polar_stereographic)
* Données sur grille lat-lon tournée: [https://dd.meteo.gc.ca/model_hrdpa/2.5km/{HH}/](https://dd.meteo.gc.ca/model_hrdpa/2.5km)

où :

* __polar_stereographic__ :  Projection de la grille
* __hh__ : Heure finale d’accumulation de précipitation [06, 24]
* __HH__ : Heure UTC de la passe [00, 06, 12, 18]

Un historique de 30 jours est conservé dans ces répertoires.

## Spécification technique des grilles

* __Grille polaire stéréographique__

![image de la spécification technique de la grille AHRDP](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_hrdpa/grille_hrdpa.png)

Valeurs données aux paramètres de la grille polaire stéréographique à haute résolution.

| Paramètre | Valeur |
| ------ | ------ |
| ni | 2500 |
| nj | 1222 | 
| résolution à 60° N | 2.5 km |
| coordonnées du premier point de grille | 42.2504° N ; 131.0928° W | 
| orientation de la grille (par rapport à l’axe des j) | -115,0° |

* __Grille lat-lon tournée__

![Grille HRDPA Rlatlon](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_hrdpa/grille_hrdpa_rlatlon.png)

Valeurs données aux paramètres de la grille lat-lon tournée:

| Paramètre | Valeur |
| ------ | ------ |
| ni | 2538 |
| nj | 1288 | 
| résolution à 60° N | 2.5km |
| coordonnées du premier point de grille | -36.09° N ; 114.70° W |

__Note__ : Les [versions les plus récentes de wgrib2](https://www.cpc.ncep.noaa.gov/products/wesley/wgrib2/update_2.0.8.html) et [GDAL](https://gdal.org/) supportent ces grilles tournées.

## Nomenclature des noms de fichiers 

### Grille polaire stéréographique

Les fichiers ont la nomenclature suivante :

CMC_HRDPA_APCP-TotalPrecipAmount-HHMMcutoff_SFC_0_ps2.5km_YYYYMMDDHH_000.grib2

où :

* __CMC__ : Les données sont produites par le Centre Météorologique Canadien (Chaîne constante)
* __HRDPA__ : Analyse à Haute Résolution Déterministe de Précipitation (Chaîne constante)
* __APCP__ : Analyse de Précipitation (Chaîne constante)
* __AccumTotalePrecipPeriode__ : La quantité de précipitation totale sur une période de temps définie en nombre d'heures (006 ou 024)
* __HHMMcutoff__ : Le temps de coupure des observations en nombre d'heures et minutes après l'heure de validité. (0100cutoff ou 0700cutoff)
* __SFC_0__ : Le type de niveau est Surface et son type de valeur est 0 (Chaîne constante)
* __ps2.5km__: Le type de projection est polaire-stéréographique à une résolution de 2.5 km (Chaîne constante)
* __YYYYMMDDHH__: Heure de validité de l'analyse en UTC. YYYY=Année, MM=Mois, DD=Jour, HH=Heure (ex: 2018020912)
* __000__: Le temps de projection en nombre d'heures. Toujours 000 pour une analyse (Chaîne constante)

Exemple :

CMC_HRDPA_APCP-006-0100cutoff_SFC_0_ps2.5km_2018020912_000.grib2

Ce fichier provient du Centre Météorologique Canadien (CMC) et contient des données de l'Analyse à Haute Résolution Déterministe de Précipitation (HRDPA). C'est une analyse de précipitation (APCP) sur des cumuls de 6 heures (006) dont la période de cumul débute à 2018020906 et se termine à 2018020912. Elle est considérée préliminaire parce que la collecte des observations s'est faite jusqu'à 2018020913, soit 1 heure après l'heure de validité (0100cutoff). Les données sont sur une grille stéréographique polaire à une résolution de 2.5 km (ps2.5km). L'heure de validité de l'analyse est 2018020912_000 où le suffixe _000 signifie que le temps de projection dans le future est nulle, ce qui est toujours le cas pour une analyse. Les données de ce fichier sont encodées en format GRIB2 (.grib2).

À noter qu'une deuxième variable est également incluse dans ce fichier, soit l'indice de confiance de l'analyse (CFIA).

### Grille lat-lon tournée

Les fichiers ont une des nomenclatures suivantes :

* {YYYYMMDD}T{HH}Z_MSC_HRDPA_{VAR}_Sfc_RLatLon0.0225_PT0H.grib2
* {YYYYMMDD}T{HH}Z_MSC_HRDPA-Prelim_{VAR}_Sfc_RLatLon0.0225_PT0H.grib2

où :

* __YYYYMMDD__: Année, mois et jour du début de la prévision 
* __T__ : Délimiteur temporel selon les normes ISO8601
* __HH__: Heure UTC de la passe [00, 06, 12, 18]
* __Z__ : Fuseau horaire (heure UTC)
* __MSC__ : Chaîne de caractères constante pour Meteorological Service of Canada, la source des données
* __HRDPA__ : Chaîne de caractères constante indiquant le modèle source Analyse à haute résolution de prévision déterministe. Temps de coupure de 7 heures pour les observations après l'heure YYYYMMDDHH, indiquant qu'un maximum d'observations a probablement été recueilli
* __HRDPA-Prelim__: Chaîne de caractères constante indiquant le modèle source Analyse à haute résolution de prévision déterministe. Temps de coupure des observations à l'intérieur d'une heure après l'heure YYYYMMDDHH, indiquant que toutes les observations n'ont possiblement pas été recueillies
* __VAR__ : Chaîne de caractères constante donnant le nom de la variable contenue dans le fichier. Ici, il s’agit de l’analyse de précipitation accumulée sur une certaine période [APCP-Accum6h, APCP-Accum24h]
* __Sfc__ : Indique que le type de niveau est la surface
* __RLatLon0.0225__: Chaîne de caractères constante indiquant une grille lat-lon tournée à 0.0225deg de résolution (environ 2.5km)
* __PT0H__: Basé sur les normes ISO8601. P, T et H sont des caractères constants indiquant respectivement la période, le temps et l'heure. Ici, PT0H indique qu'il s'agit d'une analyse
* __grib2__:  Indique que les données sont en format GRIB2

Exemples de noms de fichiers :

* 20231106T00Z_MSC_HRDPA-Prelim_APCP-Accum6h_Sfc_RLatLon0.0225_PT0H.grib2

Le fichier a été créé par le Service météorologique canadien (MSC) et contient une analyse à haute résolution déterministe de précipitation (HRDPA). Il contient une analyse préliminaire d’accumulation de précipitation représentée par la variable APCP et ce sur un intervalle de 6 heures. Les données sont sur une grille tournée lat-lon à une résolution de 2.5 km (RLatLon0.0225). L’analyse a été produite le 06 novembre 2023 à 00Z (20230306T00Z). L’intervalle de 006 heures dans lequel les précipitations sont analysées est de 2023110600 à 2023110606.

* 20231106T12Z_MSC_HRDPA_APCP-Accum24h_Sfc_RLatLon0.0225_PT0H.grib2

Le fichier a été créé par le Service météorologique canadien (MSC) et contient une analyse à haute résolution déterministe de précipitation (HRDPA). Il contient une analyse finale d’accumulation de précipitation représentée par la variable APCP et ce sur un intervalle de 24 heures. Les données sont sur une grille lat-lon tournée à une résolution de 2.5 km (RLatLon0.0225). L’analyse a été produite le 06 novembre 2023 à 12Z (2023110612). L’intervalle de 24 heures dans lequel les précipitations sont analysées est de 2023110612 à 2023110712.

__NOTE__ : Même si ce n’est pas indiqué dans le nom du fichier, le fichier contiendra aussi l’indice de confiance de l’analyse (CFIA) associé à l’analyse de précipitation.

## Liste des variables

<table id="csv-table" class="display"></table>

<link href="https://cdn.jsdelivr.net/npm/simple-datatables@latest/dist/style.css" rel="stylesheet" type="text/css">
<script src="https://cdn.jsdelivr.net/npm/simple-datatables@latest"></script>
<script src="../../../js/variables_datatable.js" type="text/javascript"></script>
<script>
  loadTable("csv-table", "../../../assets/csv/HRDPA_Variables-List_fr.csv");
</script>

## À propos du masque No-Data de la grille polaire stéréographique

Un masque pour mieux représenter les zones où les données ne sont pas disponibles, appelées aussi "No-Data" a été ajouté dans notre procédure d’encodage GRIB2. Ce masque vise uniquement quelques points de grille non-valides (données non-disponibles), toujours les mêmes et qui se situent en périphérie du domaine. Notons que ces points masqués n’ont aucun effet négatif sur la qualité du produit.

## Support

Pour toute question relative à ces données, merci de [nous contacter]( https://meteo.gc.ca/mainmenu/contact_us_f.html)

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).

