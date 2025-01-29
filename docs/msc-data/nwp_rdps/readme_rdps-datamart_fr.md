[In English](readme_rdps-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [SRPD](readme_rdps_fr.md) > SRPD sur le Datamart du SMC


# Données GRIB2 du Système régional de prévision déterministe (SRPD)

Les champs du jeu de données GRIB2 du [Système régional de prévision déterministe (SRPD)](readme_rdps_fr.md) sont disponibles sur une grille polaire stéréographique de 935 x 824 points couvrant l’Amérique du Nord et les eaux environnantes avec une résolution de 10 km à 60 degrés nord.


## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier GRIB2.

Les données sont accessibles à l’adresse suivante : 

[https://dd.meteo.gc.ca/model_gem_regional/10km/grib2/{HH}/{hhh}/](https://dd.meteo.gc.ca/model_gem_regional/10km/grib2)

où :

* __HH__ : Heure UTC du début de la passe du modèle [00, 06, 12, 18]
* __hhh__ : Heure de prévision [000, 001, 002, ..., 084] 

## Spécification technique de la grille

![Image de la grille du Système régional de prévision déterministe](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_rdps/grille_RDPS.png)

Valeurs données aux paramètres de la grille polaire stéréographique :

| Paramètre | Valeur |
| ------ | ------ |
| ni | 935 |
| nj | 824 | 
| résolution à 60° N | 10km |
| coordonnées du premier point de grille | 18.1429° N ; 142.8968° W | 
| coordonnées (i; j) du Pôle Nord | (456.2; 732.4) |
| orientation de la grille (par rapport à l’axe des j) | -111,0° | 

## Nomenclature des noms de fichiers 

NOTE: TOUTES LES HEURES SONT EN UTC.

Les fichiers ont la nomenclature suivante :

CMC_reg_Variable_TypedeNiveau_Niveau_ps10km_YYYYMMDDHH_Phhh.grib2

où :

* __CMC__ : Chaîne de caractères constante indiquant que le Centre météorologique canadien (CMC) émet les prévisions.
* __reg__ : Chaîne de caractères constante indiquant que les données proviennent du SRPD.
* __Variable__ : Type de variable contenue dans le fichier (ex : UGRD). Pour voir la liste complète, consultez la section « Liste des variables ».
* __TypedeNiveau__ : Type de niveau. Pour voir la liste complète, consultez la section « Liste des variables ».
* __Niveau__ : Valeur du niveau. Pour consulter la liste complète, consultez la section « Liste des variables ».
* __ps10km__ : Chaîne de caractères constante indiquant que la projection utilisée est polaire stéréographique à une résolution de 10 km.
* __YYYYMMDD__ : Année, mois et jour du début de la prévision.
* __HH__ : Heure UTC de la passe [00, 06, 12, 18].
* __Phhh__ : « P » est un caractère constant. « hhh » représente l’heure de prévision [000, 001, 002,...,084]
* __grib2__ : Chaîne de caractères constante indiquant que le format est GRIB2.

Exemple de nom de fichier : CMC_reg_DEPR_ISBL_1015_ps10km_2010091306_P027.grib2

Le fichier a été créé par le CMC et contient une prévision du SRPD. Il contient les dépressions du point de rosée (DEPR), au niveau isobarique 1015 mb (ISBL_1015), sur une grille polaire stéréographique à une résolution de 10 km (ps10km). Il débute le 13 septembre 2010 à 06Z (22010091306). Il contient l’heure de prévision 27 (P027) en format GRIB2 (.grib2).

## Niveaux  

La couverture verticale des champs tridimensionnels peut atteindre jusqu’à 33 niveaux isobariques.

* Niveaux isobariques (hPa) : 1015, 1000, 985, 970, 950, 925, 900, 850, 800, 750, 700, 650, 600, 550, 500, 450, 400, 350, 300, 275, 250, 225, 200, 175, 150, 100, 50.

    * Niveaux additionnels 30, 20, 10, 5 et 1 hPa pour les variables TMP, HGT, UGRD, VGRD, WIND, WDIR, SPFH

    * Niveaux additionnels 30, 20 et 10 hPa pour les variables RH et DEPR

* Certains champs reçoivent une couverture verticale limitée à cinq niveaux isobariques, soit 850, 700, 600, 500, 250 hPa.

Autres types de niveaux qui pourraient être applicables à certains champs :

* Surface
* Hauteur fixe au-dessus du sol
* Profondeur fixe sous le sol
* Épaisseur entre niveaux isobariques
* Sommet théorique de l’atmosphère
* Colonne atmosphérique entière

## Liste des variables

<table id="csv-table" class="display"></table>

<link href="https://cdn.jsdelivr.net/npm/simple-datatables@latest/dist/style.css" rel="stylesheet" type="text/css">
<script src="https://cdn.jsdelivr.net/npm/simple-datatables@latest"></script>
<script src="../../../js/variables_datatable.js" type="text/javascript"></script>
<script>
  loadTable("csv-table", "../../../assets/csv/RDPS_Variables-List_fr.csv");
</script>

Notes :

* La direction des composantes u (UGRD) et v (VGRD) du vecteur vent doit être résolue selon les composantes i, j de la grille définie et dans la direction croissante des coordonnées i, j. Veuillez vous référer à la table de code 7 du standard GRIB pour de plus amples informations.
* Les paramètres NLWRS_SFC, DSWRF_NTAT, DLWRF_NTAT sont donnés en quantités accumulées. L’intervalle temporel d’accumulation est spécifié selon la valeur numéro 4 de la table de code 5 du standard GRIB. En raison de l’accumulation sur une période, les unités d’origine (watts par mètre carré) deviennent des joules par mètre carré.
* Le paramètre représentant l’humidité dans le modèle est l’humidité spécifique (SPFH). C’est ce paramètre qui devrait être utilisé pour toute application de PNT. La dépression du point de rosée (DEPR) est un paramètre diagnostique déconseillé pour les applications de haute précision.
* L'indice d'orages violents ([SSI](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_rdps/SSI_fr.png)) a été développé par ECCC à la fin des années 1980.
* Les maximums d'indice UV sont les maximums journaliers basés sur l'heure courante et les 23 heures précédentes (s'applique aussi à l'indice UV par temps clair). Ils sont disponibles aux échéances suivantes selon les passes du système:
    * Passe de 00Z: 18h, 42h et 66h
    * Passe de 06Z: 12h, 36h et 60h
    * Passe de 12Z: 6h , 30h et 54h
    * Passe de 18Z: 0h , 24h et 48h

## Support

Pour toute question relative à ces données, merci de [nous contacter](https://meteo.gc.ca/mainmenu/contact_us_f.html).

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).
