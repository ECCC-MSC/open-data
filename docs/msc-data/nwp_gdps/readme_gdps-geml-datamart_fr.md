[In English](readme_gdps-geml-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [SGPD](readme_gdps_fr.md) > SGPD-GEML sur le Datamart du SMC

# Données expérimentales GRIB2 du Global Environnemental éMuLateur (SGPD-GEML)

Le Global Environnemental éMuLateur (GEML) est un composant du [Système global de prévision déterministe expérimental (SGPD)](readme_gdps_fr.md#données-du-système-global-de-prévision-déterministe-expérimental). Il s'agit d'un émulateur météorologique basé sur l'intelligence artificielle (IA) et entraîné sur des états atmosphériques passés. Les prévisions sont effectuées deux fois par jour et vont jusqu'à 10 jours dans le futur. Il génère les champs de référence de température et de vent horizontal à grande échelle vers lesquels les prévisions de GEM dans le SGPD sont pilotées spectralement. La couverture géographique est globale avec une résolution horizontale de 28 km. Les données sont offertes sur 13 niveaux verticaux et sur une grille latitude-longitude uniforme globale avec une résolution horizontale de 0.25 degré. Six variables atmosphériques définies sur les 13 niveaux de pression, ainsi que 4 variables de surface sont disponibles toutes les 6 heures.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier GRIB2.

Les données sont accessibles à l'adresse suivante :

[https://dd.meteo.gc.ca/model_gdps-geml/{RES}/{HH}/{hhh}/](https://dd.meteo.gc.ca/model_gdps-geml)

où :

* __RES__ : Résolution horizontale [25km]
* __HH__ : Heure UTC du début de la passe du modèle [00, 12]
* __hhh__ : Heure de prévision [000, 006, ..., 240]

## Spécification technique de la grille

Valeurs données aux différents paramètres de la grille latitude-longitude à 25km de résolution

| Paramètre | Valeur |
| ------ | ------ |
| ni | A COMPLÉTER |
| nj | A COMPLÉTER | 
| résolution | 0.25° |
| orientation de la grille | A COMPLÉTER | 

## Nomenclature des noms de fichiers 

Les fichiers ont la nomenclature suivante :

{YYYYMMDD}T{HH}Z_MSC_GDPS-GEML_{VAR}_{LVLTYPE-LVL}_{Grille}{resolution}_PT{hhh}H.grib2

où :

* __YYYYMMDD__ : Année, mois et jour du début de la prévision
* __T__ : Délimiteur temporel selon les normes ISO8601
* __HH__ : Heure UTC de la passe [00, 12]
* __Z__ : Fuseau horaire (heure UTC)
* __MSC__ : Chaîne de caractères constante pour Meteorological Service of Canada, la source des données
* __GDPS-GEML__ : Chaîne de caractères constante indiquant que les données proviennent du Global Environnemental éMuLateur (GEML) expérimental, une composante du Système global de prévision déterministe expérimental (SGPD)
* __VAR__ : Type de variable contenu dans le fichier (ex: AirTemp).
* __LVLTYPE-LVL__ : Niveau vertical et hauteur [ex: Sfc pour la surface, AGL-2m pour la hauteur de 2m au-dessus du sol, Isbl-0850 pour l'altitude géopotentielle à 850mb]
* __Grille__ : Grille horizontale [LatLon]
* __resolution__ : 0.25. Signifie une résolution de 0.25°(environ 25km) dans les directions longitudinale et latitudinale
* __PT{hhh}H__ : Echéance temporelle selon la norme [ISO8601](https://en.wikipedia.org/wiki/ISO_8601). P, T et H sont des caractères constants désignant Période, Temps et Heure. "hhh" représente l’heure de prévision [000, 006, 012, ..., 240]
* __grib2__ : Chaîne de caractères constante indiquant que le format est GRIB2.

Exemples de noms de fichiers :

* 20250529T12Z_MSC_GDPS-GEML_SpecificHumidity_AGL-2m_LatLon0.25_PT012H.grib2
* 20250529T00Z_MSC_GDPS-GEML_WindU_Isbl-0050_LatLon0.25_PT234H.grib2

## Liste des variables

<table id="csv-table" class="display"></table>

<link href="https://cdn.jsdelivr.net/npm/simple-datatables@latest/dist/style.css" rel="stylesheet" type="text/css">
<script src="https://cdn.jsdelivr.net/npm/simple-datatables@latest"></script>
<script src="../../../js/variables_datatable.js" type="text/javascript"></script>
<script>
  loadTable("csv-table", "../../../assets/csv/GDPS-GEML_Variables-List_fr.csv");
</script>

Notes :

* La direction des composantes u (UGRD) et v (VGRD) du vecteur vent doit être résolue selon les composantes i, j de la grille définie et dans la direction croissante des coordonnées i, j. Veuillez vous rérérer à la table de code 7 du standard GRIB pour de plus amples informations. 

## Support

Pour toute question relative à ces données, merci de [nous contacter](https://meteo.gc.ca/mainmenu/contact_us_f.html). 

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).

















