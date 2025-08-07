[In English](readme_gdps-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [SGPD](readme_gdps_fr.md) > SGPD sur le Datamart du SMC

# Données GRIB2 du Système global de prévision déterministe (SGPD)

Les champs du jeu de données GRIB2 du [Système global de prévision déterministe (SGPD)](readme_gdps_fr.md) sont disponibles sur une grille latitude-longitude à une résolution effective d’environ 15 km.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier GRIB2.

Les données sont accessibles à l'adresse suivante :

[https://dd.meteo.gc.ca/today/model_gem_global/{RES}/grib2/lat_lon/{HH}/{hhh}/](https://dd.meteo.gc.ca/today/model_gem_global)

où :

* __RES__ : Résolution horizontale [15km]
* __HH__ : Heure UTC du début de la passe du modèle [00, 12]
* __hhh__ : Heure de prévision [000, 003, 006, ..., 240]

## Spécification technique de la grille

Valeurs données aux différents paramètres de la grille latitude-longitude à 15km de résolution

| Paramètre | Valeur |
| ------ | ------ |
| ni | 2400 |
| nj | 1201 | 
| résolution | 0.15° |
| coordonnées du premier point de grille | 90° S  180° W | 

## Nomenclature des noms de fichiers 

Les fichiers ont la nomenclature suivante :

CMC_glb_Variable_TypedeNiveau_Niveau_ProjectionResolution_YYYYMMDDHH_Phhh.grib2

où :

* __CMC__ : Chaîne de caractères constante indiquant le Centre météorologique canadien (CMC) émet les prévisions.
* __glb__ : Chaîne de caractères constante indiquant que les données proviennent du SGPD.
* __Variable__ : Type de variable contenu dans le fichier (ex. : UGRD). Pour voir la liste complète, consultez la section « Description des variables disponibles ».
* __TypedeNiveau__ : Type de niveau. Pour voir la liste complète, consultez la section « Description des variables disponibles ».
* __Niveau__ : Valeur du niveau. Pour voir la liste complète, consultez la section « Description des variables disponibles ».
* __Projection__ : Représente le type de projection utilisée pour les données. Peut prendre les valeurs [latlon, ps].
* __Resolution__ : Chaîne de caractères constante indiquant la résolution des données [.15x.15].
* __YYYYMMDD__ : Année, mois et jour du début de la prévision.
* __HH__ : Heure UTC de la passe [00, 12].
* __Phhh__ : « P » est un caractère constant. « hhh » représente l’heure de prévision [000, 003, 006, ..., 240].
* __grib2__ : Chaîne de caractères constante indiquant que le format est GRIB2.

Exemple de nom de fichier :
CMC_glb_TMP_ISBL_925_latlon.15x.15_2019101512_P042.grib2

Le fichier débute le 15 octobre 2019 à 12Z (2019101512). Il a été créé par le CMC et contient une prévision du SGPD. Il contient les composantes de la température (TMP), au niveau isobarique 925 mb (ISBL_925), pour l’heure de prévision 42 (P042) en format GRIB2 (.grib2).

# Données GRIB2 du Système global de prévision déterministe (SGPD) expérimental

Les champs du jeu de données GRIB2 du [Système global de prévision déterministe expérimental (SGPD)](readme_gdps_fr.md#données-du-système-global-de-prévision-déterministe-expérimental) sont disponibles sur une grille latitude-longitude à une résolution effective d’environ 15 km.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier GRIB2.

Les données sont accessibles à l'adresse suivante :

[https://dd.meteo.gc.ca/today/model_gdps/{RES}/{HH}/{hhh}/](https://dd.meteo.gc.ca/today/model_gdps)

où :

* __RES__ : Résolution horizontale [15km]
* __HH__ : Heure UTC du début de la passe du modèle [00, 12]
* __hhh__ : Heure de prévision [000, 001, 002, ..., 084, 087, 090, …, 240]

## Spécification technique de la grille

Valeurs données aux différents paramètres de la grille latitude-longitude à 15km de résolution

| Paramètre | Valeur |
| ------ | ------ |
| ni | 2400 |
| nj | 1201 | 
| résolution | 0.15° |
| orientation de la grille | 0° W  359.85° E | 

## Nomenclature des noms de fichiers 

Les fichiers ont la nomenclature suivante :

{YYYYMMDD}T{HH}Z_MSC_GDPS_{VAR}_{LVLTYPE-LVL}_{Grille}{resolution}_PT{hhh}H.grib2

où :

* __YYYYMMDD__ : Année, mois et jour du début de la prévision
* __T__ : Délimiteur temporel selon les normes ISO8601
* __HH__ : Heure UTC de la passe [00, 12]
* __Z__ : Fuseau horaire (heure UTC)
* __MSC__ : Chaîne de caractères constante pour Meteorological Service of Canada, la source des données
* __GDPS__ : Chaîne de caractères constante indiquant que les données proviennent du Système global de prévision déterministe (version expérimentale)
* __VAR__ : Type de variable contenu dans le fichier (ex: AirTemp).
* __LVLTYPE-LVL__ : Niveau vertical et hauteur [ex: Sfc pour la surface, EAtm pour l’intégrale de la colonne, DBS-10to20cm couche entre 10 et 20cm sous la surface, AGL-10m pour la hauteur de 10m au-dessus du sol]
* __Grille__ : Grille horizontale [LatLon]
* __resolution__ : 0.15. Signifie une résolution de 0.15°(environ 15km) dans les directions longitudinale et latitudinale
* __PT{hhh}H__ : Echéance temporelle selon la norme [ISO8601](https://en.wikipedia.org/wiki/ISO_8601). P, T et H sont des caractères constants désignant Période, Temps et Heure. "hhh" représente l’heure de prévision [000, 001, 002, ..., 084, 087, 090, …, 240]
* __grib2__ : Chaîne de caractères constante indiquant que le format est GRIB2.

Exemples de noms de fichiers :

* 20250529T12Z_MSC_GDPS_GeopotentialHeight_IsbL-0350_LatLon0.15_PT018H.grib2
* 20250529T12Z_MSC_GDPS_SoilTemp_Sfc_LatLon0.15_PT018H.grib2

# Niveaux  

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

# Liste des variables

<table id="csv-table" class="display"></table>

<link href="https://cdn.jsdelivr.net/npm/simple-datatables@latest/dist/style.css" rel="stylesheet" type="text/css">
<script src="https://cdn.jsdelivr.net/npm/simple-datatables@latest"></script>
<script src="../../../js/variables_datatable.js" type="text/javascript"></script>
<script>
  loadTable("csv-table", "../../../assets/csv/GDPS_Variables-List_fr.csv");
</script>

Notes :

* La direction des composantes u (UGRD) et v (VGRD) du vecteur vent doit être résolue selon les composantes i, j de la grille définie et dans la direction croissante des coordonnées i, j. Veuillez vous rérérer à la table de code 7 du standard GRIB pour de plus amples informations. 
* Les paramètres NLWRS_SFC, DSWRF_NTAT, DLWRF_NTAT sont donnés en quantités accumulées. L’intervalle temporel d’accumulation est spécifié selon la valeur numéro 4 de la table de code 5 du standard GRIB. En raison de l’accumulation sur une période, les unités d’origine (watts par mètre carré) deviennent des joules par mètre carré.   
* Le paramètre représentant l’humidité dans le modèle est l’humidité spécifique (SPFH). C’est ce paramètre qui devrait être utilisé pour toute application de PNT. La dépression du point de rosée (DEPR) est un paramètre diagnostique déconseillé pour les applications de haute précision.
* La topographie (altitude géopotentielle de surface, HGT) est disponible à l'heure de prévision 00h de chacune des passes du modèle.
* Les maximums d'indice UV sont les maximums journaliers basés sur l'heure courante et les 23 heures précédentes (s'applique aussi à l'indice UV par temps clair). Ils sont disponibles aux échéances suivantes selon les passes du système:
    * Passe de 00Z: 18h à 234h, toutes les 3 heures
    * Passe de 12Z: 6h à 222h, toutes les 3 heures

# Support

Pour toute question relative à ces données, merci de [nous contacter](https://meteo.gc.ca/mainmenu/contact_us_f.html). 

# Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).

















