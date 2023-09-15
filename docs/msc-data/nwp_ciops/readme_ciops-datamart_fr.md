[In English](readme_ciops-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [SPCOG](readme_ciops_fr.md) > SPCOG prévision océanique sur le Datamart du SMC

# Données du Système de prévision côtier océan-glace (SPCOG) en format NetCDF 

Les prévisions océan-glace horaires sont disponibles en format NetCDF sur une grille latitude-longitude, correspondant à une résolution d'environ 2km (0.03 x 0.02 degrées) pour le domaine Est couvrant le Fleuve Saint-Laurent, le Golfe du Saint-Laurent et une région Nord-Ouest de l'océan Atlantique. Le domaine Ouest inclue la côte Ouest du Canada et le Nord-Est de l'océan Pacifique à une résolution d'environ 2km (0.03 x 0.02 degrées). Un sous-domaine couvrant la mer de Salish est aussi disponible à plus haute résolution (500m ou 0.008 x 0.005 degrées).

## Adresse des données 

Les données hébergées sur HPFX, le [serveur alternatif du Datamart du SMC](../../msc-datamart/readme_fr) peuvent être [automatiquement récupérées avec le Protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier NetCDF.

Les données sont accessibles aux adresses suivantes :

* [https://hpfx.collab.science.gc.ca/{YYYMMDD}/WXO-DD/model_ciops/east/2km/{HH}/{hhh}/](https://hpfx.collab.science.gc.ca/)
* [https://hpfx.collab.science.gc.ca/{YYYMMDD}/WXO-DD/model_ciops/west/2km/{HH}/{hhh}/](https://hpfx.collab.science.gc.ca/)
* [https://hpfx.collab.science.gc.ca/{YYYMMDD}/WXO-DD/model_ciops/salish-sea/500m/{HH}/{hhh}/](https://hpfx.collab.science.gc.ca/) 

où :

* __YYYYMMDD__ : Année, mois et jour 
* __HH__ : Heure en UTC du début de la simulation [00, 06, 12, 18]
* __hhh__ : Heure de la prévision [000, 001, 002, ..., 048] 

Un historique de plusieurs semaines est conservé dans ces répertoires.

## Spécification technique des grilles

### Domaine océanique Est

![Image du domain océanique SPCOG - Est](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_ciops/grille_ciops-east.png)

| Paramètre | Valeur |
| ------ | ------ |
| ni | 1333 | 
| nj | 980 | 
| nk | 99 | 
| résolution | 2km |

### Domaine océanique Ouest

![Image du domain océanique SPCOG - Ouest](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_ciops/grille_ciops-west.png)

| Paramètre | Valeur |
| ------ | ------ |
| ni | 600 |
| nj | 785 |
| nk | 68 |
| résolution | 2km |

### Domaine océanique sur la mer de Salish

![Image du domain océanique CIOPS - Salish Sea](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_ciops/grille_ciops-salishsea.png)

| Paramètre | Valeur |
| ------ | ------ |
| ni | 629 |
| nj | 888 |
| nk | 39 |
| résolution | 500m |

## Nomenclature des noms de fichiers 

NOTE: TOUTES LES HEURES SONT EN UTC.

La nomenclature des noms des fichiers est la suivante :

`{YYYYMMDD}T{HH}Z_MSC_CIOPS-{Domain}_{Var}_{LVLTYPE}-{LVL}_{Grille}{resolution}_PT{hhh}H.nc`

où :

* __YYYYMMDD__ : Année, mois et jour du début de la prévision
* __T__ : Délimiteur temporel selon les normes ISO8601
* __HH__ : Heure UTC de la passe [00, 12]
* __Z__ : Fuseau horaire (heure UTC)
* __MSC__ : Chaîne de caractères constante pour Meteorological Service of Canada, la source des données
* __CIOPS__ : Chaîne de caractères constante indiquant le modèle source : SPCOG (CIOPS en anglais)
* __Domain__ : Chaîne de caractères constante indiquant le domaine [East, West, SalishSea]
* __Var__ : Variables contenues dans le fichier 
* __LVLTYPE__ : Type de niveau vertical [Sfc pour la surface, DBS pour la profondeur sous la surface]
* __LVL__ : Valeur du niveau vertical [0.5m, `all` pour tous les niveaux disponibles]. Ce paramètre est absent pour la surface
* __Grille__ : Grille horizontale [LatLon]
* __resolution__ : Indique la résolution en degré dans les directions longitudinale et latitudinale [0.03x0.02, 0.008x0.005]
* __PT{hhh}H__ : Echéance temporelle selon la norme [ISO8601](https://en.wikipedia.org/wiki/ISO_8601). P, T et H sont des caractères constants désignant Période, Temps et Heure. "hhh" représente l’heure de prévision  [000, 001, 002, ..., 048]
* __nc__ : Chaîne de caractères constante indiquant que le format est NetCDF

Exemples :

* 20220225T00Z_MSC_CIOPS-East_SeaIceDivergence_Sfc_LatLon0.03x0.02_PT002H.nc
* 20220301T00Z_MSC_CIOPS-West_SeaWaterSalinity_DBS-0.5m_LatLon0.03x0.02_PT002H.nc
* 20220301T00Z_MSC_CIOPS-SalishSea_SeaWaterPotentialTemp_DBS-all_LatLon0.008x0.005_PT002H.nc

## Niveaux

### Domaine océanique Est

Les champs tridimensionnels sont disponibles sur 99 niveaux de profondeur dans le domaine océanique Est.

__Niveaux de profondeur (m)__ :0,50594902, 1,55457, 2,65451, 3,8087499, 5,0204301, 6,29286, 7,62957, 9,0342503, 10,5108, 12,0634, 13,6964, 15,4145, 17,222401, 19,125401, 21,128799, 23,238501, 25,4604, 27,801001, 30,266899, 32,865299, 35,603699, 38,490002, 41,532398, 44,7397, 48,121201, 51,686501, 55,445999, 59,410198 63,590698, 67,9991, 72,648102, 77,550697, 82,720802, 88,172798, 93,921799, 99,983803, 106,375, 113,114 120,218, 127,707, 135,60001, 143,918, 152,68201, 161,91701, 171,645, 181,89, 192,679, 204,037, 215,993 228,57401, 241,81, 255,73199, 270,37201, 285,76001, 301,93201, 318,92001, 336,76099, 355,48901, 375,14301, 395,76001, 417,37799, 440,039, 463,78699, 488,681, 514,80499, 542,32397, 571,61401, 603,60602, 640,60901, 687,87701, 754,76501, 850,67902, 975,659, 1120,37, 1275,53, 1435,96, 1599,4301, 1765,0699, 1932,58, 2101,8501, 2272,8701, 2445,6499, 2620,1799, 2796,5, 2974,6201, 3154,54, 3336,27, 3519,8301, 3705,2, 3892,3999, 4081,4199, 4272,2598, 4464,8999, 4659,3301, 4855,54, 5053,52, 5253,2402, 5454,6699, 5657,8101.

### Domaine océanique Ouest

Les champs tridimensionnels sont disponibles sur 68 niveaux de profondeur dans le domaine océanique Ouest.

__Niveaux de profondeur (m)__ : 0,50752997, 1,55757, 2,6693399, 3,8578801, 5,1419101, 6,5445399, 8,0939703, 9,8241596, 11,775, 13,9924, 16,5266, 19,431101, 22,7589, 26,5595, 30,875799, 35,741402, 41,181301, 47,2131, 53,851898, 61,114101, 69,023003, 77,612503, 86,930801, 97,042702, 108,032, 120,001, 133,077, 147,408, 163,166, 180,552, 199,79201, 221,14301, 244,892, 271,358, 300,88901, 333,86499, 370,69, 411,79599, 457,62799, 508,642, 565,29401, 628,02802, 697,26099, 773,37, 856,68103, 947,45001, 1045,86, 1151,99, 1265,86, 1387,38, 1516,37, 1652,5699, 1795,67, 1945,3, 2101,03, 2262,4199, 2429,03, 2600,3799, 2776,04, 2955,5701, 3138,5701,3324,6399, 3513,45, 3704,6599, 3897,98, 4093,1599, 4289,96, 4488,1602.

### Domaine océanique sur la mer de Salish

Les champs tridimensionnels sont disponibles sur 39 niveaux de profondeur dans le domaine océanique sur la mer de Salish.

__Niveaux de profondeur (m)__ : 0,5, 1,5, 2,50001, 3,50003, 4,5000701, 5,5001502, 6,5003099, 7,5006199, 8,5012398, 9,50243, 10,5048, 11,5093, 12,5182, 13,5354, 14,569, 15,6343, 16,7612, 18,007099, 19,4818, 21,389999, 24,1003, 28,2299, 34,685799, 44,5177, 58,484299, 76,585602, 98,063004, 121,867, 147,089, 173,114, 199,573, 226,25999, 253,067, 279,935, 306,83401, 333,75, 360,67499, 387,603, 414,534.

## Liste des variables

<table id="csv-table" class="display"></table>

<link href="https://cdn.jsdelivr.net/npm/simple-datatables@latest/dist/style.css" rel="stylesheet" type="text/css">
<script src="https://cdn.jsdelivr.net/npm/simple-datatables@latest"></script>
<script src="../../../js/variables_datatable.js" type="text/javascript"></script>
<script>
  loadTable("csv-table", "../../../assets/csv/CIOPS_fr.csv");
</script>

Note: L'unité `PSU` (Practical Salinity Unit) est équivalente à g/kg ou pour mille (‰). Elle est basée sur les propriétés de la conductivité de l'eau de mer.

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).

