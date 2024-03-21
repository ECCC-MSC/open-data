[In English](readme_riops-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [SRPOG](readme_riops_fr.md) > Données NetCDF du SRPOG

# Données NetCDF du Système régional de prévision océan-glace (SRPOG)

Le Centre de prévision météorologique et environnementale du Canada (CPMEC) fournit des prévisions instantanées horaires de champs de glace et de champs océaniques produits par son Système régional de prévision océan-glace (SRPOG) opérationnel et interpolés sur une grille en projection polaire stéréographique nord d'une résolution de 5 km à une latitude de 60°N.

Les fichiers des données sont en format NetCDF (NetCDF-4 modèle classique), conformes aux conventions CF liées au climat et aux prévisions (Climate and Forecast Conventions).

Le SRPOG utilise le modèle océan-glace NEMO-CICE et fournit des analyses et prévisions globales de 2 jours de l'océan et de la glace marine, quotidiennement à partir de [00, 06, 12, 18] UTC.

Le SRPOG comprend une analyse 3DVar de la concentration de la glace (assimilant des observations satellitaires et des cartes de glace du service canadien des glaces) alors que les larges échelles de l'analyse océanique sont constraintes en rappelant spectralement les champs de température et de salinité vers ceux du Système global de prévision océan-glace du CCMEP (qui lui inclut un système d'assimilation multivarié qui ingère des observations satellitaires ainsi que des observations in-situ).

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTP. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier GRIB2.

Les données sont accessibles aux adresses suivantes :

* [https://dd.meteo.gc.ca/model_riops/netcdf/forecast/polar_stereographic/nd/HH/hhh/](https://dd.meteo.gc.ca/model_riops/netcdf/forecast/polar_stereographic/)

où :

* __nd__ : Numéro de la dimension spatiale des champs de prévision [2d ou 3d] 
* __HH__ : Heure en UTC du début de la passe du modèle[00, 06, 12, 18]
* __hhh__ : Heure de la prévision [000, 001, 002, ..., 084]

Un historique de 2 jours de prévision est disponible dans ce répertoire.

## Nomenclature des noms de fichiers 

NOTE : TOUTES LES HEURES SONT EN UTC.

Les fichiers ont la nomenclature suivante :

* {YYYYMMDD}T{HH}Z_MSC_RIOPS_VAR_LVL_{Grille}{resolution}_P{hhh}.nc

où :

* __YYYYMMDD__ : Année, mois et jour du début de la prévision
* __T__ : Délimiteur temporel selon les normes ISO8601
* __HH__ : Heure en UTC du début de la passe du modèle [00, 06, 12, 18]
* __Z__ : Fuseau horaire (heure UTC)
* __MSC__ : Chaîne de caractères constante pour Meteorological Service of Canada, la source des données 
* __RIOPS__ : Chaîne de caractères constante indiquant que les données proviennent du Système régional de prévision océan-glace
* __VAR__ : Nom de la variable contenue dans le fichier
* __LVL__ : Niveau vertical [SFC, DBS-0.5m, DBS-all]; SFC pour surface, DBS pour la profondeur sous la surface (Depth Below Surface), 0.5m pour 0.5 mètres de profondeur sous la surface et 'all' pour toutes les profondeurs
* __Grille__ : Projection cartographique [PS], PS pour polaire stéréographique 
* __resolution__ : Résolution horizontale [5km], signifie une résolution de 5 km à une latitude 60°N
* __Phhh__ : « P » est un caractère constant. « hhh » représente l’heure de prévision [000, 001, 002, ..., 084]
* __nc__ : Chaîne de caractères constante indiquant le format NetCDF

Exemples de noms de fichier : 

* 20200913T06Z_MSC_RIOPS_IICEVOL_SFC_PS5km_P012.nc 
* 20200913T12Z_MSC_RIOPS_VOSALINE_DBS-all_PS5km_P046.nc
* 20201014T00Z_MSC_RIOPS_VOTEMPER_DBS-0.5m_PS5km_P022.nc

## Niveaux

Les champs tridimensionnels sont disponibles sur 50 niveaux de profondeur, qui sont les niveaux du modèle océanique utilisé par SRPOG.

__Niveaux de profondeur (m)__ : 0.494025, 1.54138, 2.64567, 3.81949, 5.07822, 6.44061, 7.92956, 9.573, 11.405, 13.4671, 15.8101, 18.4956, 21.5988, 25.2114, 29.4447, 34.4342, 40.3441, 47.3737, 55.7643, 65.8073, 77.8539, 92.3261, 109.729, 130.666, 155.851, 186.126, 222.475, 266.04, 318.127, 380.213, 453.938, 541.089, 643.567, 763.333, 902.339, 1062.44, 1245.29, 1452.25, 1684.28, 1941.89, 2225.08, 2533.34, 2865.7, 3220.82, 3597.03, 3992.48, 4405.22, 4833.29, 5274.78, 5727.92.

Une partie des variables représentent des quantités au premier niveau du modèle, tandis que les autres sont définies à la surface de l'océan (ex. variables de la glace marine).

La visualisation des champs contenus dans les fichiers NetCDF produits par SRPOG a été testée avec succès avec les outils suivants : Panoply (version 4.2.2) et IDV (version 5.2).

## Liste des variables

<table id="csv-table" class="display"></table>

<link href="https://cdn.jsdelivr.net/npm/simple-datatables@latest/dist/style.css" rel="stylesheet" type="text/css">
<script src="https://cdn.jsdelivr.net/npm/simple-datatables@latest"></script>
<script src="../../../js/variables_datatable.js" type="text/javascript"></script>
<script>
  loadTable("csv-table", "../../../assets/csv/RIOPS_Variables-List_fr.csv");
</script>

Note: L'unité `PSU` (Practical Salinity Unit) est équivalente à g/kg ou pour mille (‰). Elle est basée sur les propriétés de la conductivité de l'eau de mer.

## Support

Pour toute question relative à ces données, merci de [nous contacter](https://weather.gc.ca/mainmenu/contact_us_f.html).

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).