[In English](readme_rdpa-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [ARDP](readme_rdpa_fr.md) > ARDP sur le Datamart du SMC

# Données GRIB2 de l'Analyse Régionale Déterministe de Précipitation (ARDP - CaPA)

Cette page décrit les données de L’[Analyse régionale déterministe de précipitation (ARDP)](readme_rdpa_fr.md), fondée sur le système CaPA (Canadian Precipitation Analysis).

# Adresse des données

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier GRIB2.

Les données sont accessibles aux adresses suivantes :

* Données sur grille polaire stéréographique: [https://dd.meteo.gc.ca/analysis/precip/rdpa/grib2/polar_stereographic/{hh}](https://dd.meteo.gc.ca/analysis/precip/rdpa/grib2/polar_stereographic)
* Données sur grille lat-lon tournée: [https://dd.meteo.gc.ca/model_rdpa/10km/{hh}/](https://dd.meteo.gc.ca/model_rdpa/10km/{hh})

où :

* __hh__ : Heure finale d’accumulation de précipitation [06, 24]

Un historique de 30 jours est conservé dans ce répertoire.

## Spécification technique des grilles

* __Grille polaire stéréographique__

![](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_rdpa/grille_rdpa.png)

Valeurs données aux paramètres de la grille polaire stéréographique à haute résolution :

| Paramètre | Valeur |
| ------ | ------ |
| ni | 935 |
| nj | 824 | 
| résolution à 60° N | 10km |
| coordonnées du premier point de grille | 18.1429° N ; 142.8968° W | 
| coordonnées (i; j) du Pôle Nord | (456.2; 732.4) |
| orientation de la grille (par rapport à l’axe des j) | -111,0° |

* __Grille lat-lon tournée__

![Grille RDPA Rlatlon](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_rdpa/grille_rdpa_rlatlon.png)

| Paramètre | Valeur |
| ------ | ------ |
| ni | 1102 |
| nj | 1076 | 
| résolution à 60° N | 10km |
| coordonnées du premier point de grille | -31.76° N ; 92.40° W |

__Note__ : Les [versions les plus récentes de wgrib2](https://www.cpc.ncep.noaa.gov/products/wesley/wgrib2/update_2.0.8.html) et [GDAL](https://gdal.org/) supportent ces grilles tournées. __Note__ : Les [versions les plus récentes de wgrib2](https://www.cpc.ncep.noaa.gov/products/wesley/wgrib2/update_2.0.8.html) et [GDAL](https://gdal.org/) supportent ces grilles tournées. 

## Nomenclature des noms de fichiers 

NOTE: TOUTES LES HEURES SONT EN UTC.

### Grille polaire stéréographique

Les fichiers ont une des nomenclatures suivantes :

* CMC_RDPA_APCP-006-0100cutoff_SFC_0_ps10km_AAAAMMJJHH_000.grib2
* CMC_RDPA_APCP-006-0700cutoff_SFC_0_ps10km_AAAAMMJJHH_000.grib2
* CMC_RDPA_APCP-024-0100cutoff_SFC_0_ps10km_AAAAMMJJHH_000.grib2
* CMC_RDPA_APCP-024-0700cutoff_SFC_0_ps10km_AAAAMMJJHH_000.grib2

où :

* __CMC__ : Chaîne de caractères constante indiquant que le Centre météorologique canadien (CMC) émet ces prévisions.
* __RDPA__ : Chaîne de caractères constante indiquant que les données proviennent de l’Analyse régionale déterministe de précipitation (que l’on connaît aussi comme CaPA).
* __APCP__ : Chaîne de caractères constante donnant le nom de la variable contenue dans le fichier. Dans cet exemple, il s’agit de l’analyse de précipitation.
* __006__ : Intervalle d'accumulation de précipitation, soit sur 006 heures.
* __024__ : Intervalle d’accumulation de précipitation, soit sur 024 heures.
* __0100cutoff__ : Temps de coupure des observations à l'intérieur d'une heure indiquant que possiblement pas toutes les observations qui ont été recueillies.
* __0700cutoff__ : Temps de coupure de 7 heures pour les observations, indiquant qu'un maximum d'observations a probablement été recueilli.
* __SFC__ : Indique que le type de niveau est la surface.
* __0__ : Valeur du niveau. Dans cet exemple, 0 indique aussi la surface.
* __ps10km__ : Indique que la projection utilisée est polaire stéréographique à une résolution de 10 km.
* __YYYYMMDDHH__ : Année, mois, jour et heure de la date de validité de l'analyse.
* __HH__ : Heure UTC de la passe [00, 06, 12, 18].
* __000__ : Indique que l’analyse est valide exactement à YYYYMMDDHH.
* __grib2__ : Indique que les données sont en format GRIB2.

Exemple de nom de fichier :

CMC_RDPA_APCP-006-0100cutoff_SFC_0_ps10km_2015011212_000.grib2

Le fichier a été créé par le Centre météorologique canadien (CMC) et contient une analyse régionale déterministe de précipitation (RDPA). Il contient une analyse préliminaire d’accumulation de précipitation représentée par la variable APCP et ce sur un intervalle de 006 heures. Les données sont sur une grille polaire stéréographique à une résolution de 10 km (ps10km). L’analyse a été produite le 12 janvier 2015 à 12Z (2015011212) et le champ (000) confirme l’heure de validité. L’intervalle de 006 heures dans lequel les précipitations sont analysées est de 2015011206 à 2015011212.

### Grille lat-lon tournée

Les fichiers ont une des nomenclatures suivantes :

* {YYYYMMDD}T{HH}Z_MSC_RDPA_{VAR}_Sfc_RLatLon0.09_PT0H.grib2
* {YYYYMMDD}T{HH}Z_MSC_RDPA-Prelim_{VAR}_Sfc_RLatLon0.09_PT0H.grib2

où :

* __YYYYMMDD__: Année, mois et jour du début de la prévision 
* __T__ : Délimiteur temporel selon les normes ISO8601
* __HH__: Heure UTC de la passe [00, 12]
* __Z__ : Fuseau horaire (heure UTC)
* __MSC__ : Chaîne de caractères constante pour Meteorological Service of Canada, la source des données
* __RDPA__ : Chaîne de caractères constante indiquant le modèle source Analyse régionale de prévision déterministe. Temps de coupure de 7 heures pour les observations après l'heure YYYYMMDDHH, indiquant qu'un maximum d'observations a probablement été recueilli
* __RDPA-Prelim__: Chaîne de caractères constante indiquant le modèle source Analyse régionale de prévision déterministe. Temps de coupure des observations à l'intérieur d'une heure après l'heure YYYYMMDDHH, indiquant que toutes les observations n'ont possiblement pas été recueillies
* __Sfc__ : Indique que le type de niveau est la surface
* __RLatLon0.09__: Chaîne de caractères constante indiquant une grille lat-lon tournée à 0.09deg de résolution (environ 10km)
* __PT0H__: Basé sur les normes ISO8601. P, T et H sont des caractères constants indiquant respectivement la période, le temps et l'heure. Ici, PT0H indique qu'il s'agit d'une analyse
* __grib2__:  Indique que les données sont en format GRIB2

Exemples de noms de fichiers :

* 20220301T00Z_MSC_RDPA-Prelim_APCP-Accum6h_Sfc_RLatLon0.09_PT0H.grib2

Le fichier a été créé par le Service météorologique canadien (MSC) et contient une analyse régionale déterministe de précipitation (RDPA). Il contient une analyse préliminaire d’accumulation de précipitation représentée par la variable APCP et ce sur un intervalle de 6 heures. Les données sont sur une grille tournée lat-lon à une résolution de 10 km (RLatLon0.09). L’analyse a été produite le 01 mars 2022 à 00Z (20220301T00Z). L’intervalle de 006 heures dans lequel les précipitations sont analysées est de 2022030100 à 2022030106.

* 20220302T12Z_MSC_RDPA_APCP-Accum24h_Sfc_RLatLon0.09_PT0H.grib2

Le fichier a été créé par le Service météorologique canadien (MSC) et contient une analyse régionale déterministe de précipitation (RDPA). Il contient une analyse finale d’accumulation de précipitation représentée par la variable APCP et ce sur un intervalle de 24 heures. Les données sont sur une grille lat-lon tournée à une résolution de 10 km (RLatLon0.09). L’analyse a été produite le 02 mars 2022 à 12Z (2022030212). L’intervalle de 24 heures dans lequel les précipitations sont analysées est de 2022030212 à 2022030312.

NOTE: Même si ce n’est pas indiqué dans le nom du fichier, le fichier contiendra aussi l’indice de confiance de l’analyse (CFIA) associé à l’analyse de précipitation.

## Liste des variables

Cette table indique le nom de la variable, le niveau, l'abbréviation, les unités et un lien envers de l'information d'encodage grib2 pour chaque paramètre encodé en format GRIB2.

|Numéro  |	                  Variable                                |	Niveau      | 	Abbréviation    | 	Unités        | 	Encodage    |
|--------|------------------------------------------------------------|-------------|-------------------|-----------------|-----------------|
|   0 	 | Analyse de précipitations accumulées sur intervalle de 06hr ou 24hr|Surface|APCP| kg m-2          | [Sections 0 à 6](https://meteo.gc.ca/grib/display_f.html?type=rdpa&res=ps10km&hour=A000&desc=analysis&nombre=0)  |
|   1 	 | Indice de confiance de l'analyse 	                      | Surface     |CFIA|varie de 0 à 1, sans unité |[Sections 0 à 6](https://meteo.gc.ca/grib/display_f.html?type=rdpa&res=ps10km&hour=A000&desc=analysis&nombre=1) |

## À propos du masque No-Data de la grille polaire stéréographique

Depuis le 13 janvier 2016, un masque pour mieux représenter les zones où les données ne sont pas disponibles, appelées aussi "No-Data" a été ajouté dans notre procédure d’encodage GRIB2. Ce masque vise uniquement quelques points de grille non-valides (données non-disponibles), toujours les mêmes et qui se situent en périphérie du domaine. Notons que ces points masqués n’ont aucun effet négatif sur la qualité du produit.

## Archives en ligne

* Une [archive des données de l'ARDP](https://collaboration.cmc.ec.gc.ca/science/outgoing/capa.grib/) depuis le 6 avril 2011 est disponible en ligne, en format GRIB2. Notez que contrairement à ce qui est indiqué dans la section «A propos du masque No-Data» ci-dessus, les données disponibles ici ont été encodées avec le masque sur toute la période, et non à partir du 13 janvier 2016.

* Une [archive des ré-analyses](https://collaboration.cmc.ec.gc.ca/science/outgoing/capa.grib/hindcast/), couvrant la période de janvier 2002 à juin 2012, est disponible en ligne, en format GRIB2.

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).
