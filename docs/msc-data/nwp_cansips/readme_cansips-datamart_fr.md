[In English](readme_cansips-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [SPISCan](readme_cansips_fr.md) > Données GRIB2 de SPISCan sur le Datamart du SMC

# Données GRIB2 du Système de Prévision Interannuelle et Saisonnière Canadien (SPISCan)

Le [Système de prévision interannuelle et saisonnière canadien (SPISCan)](readme_cansips_fr.md) est un système de prévision à long terme dont l’objectif est de prévoir l’évolution des conditions climatiques à l’échelle globale. SPISCan est un système d’ensemble multi-modèle (Multi-Model Ensemble [MME]) utilisant CanCM4 et GEM-NEMO, deux modèles climatiques développés au Centre canadien de la modélisation et de l'analyse climatique (CCmaC) et au Centre météorologique canadien (CMC). Ce système de prévision est entièrement couplé atmosphère-océan-glace-sol. SPISCan utilise l'infrastructure d'assimilation en place pour les autres systèmes de prévision afin d'obtenir les conditions initiales de l'atmosphère, de la température de la surface de la mer et de glace marine. Pour plus de détails sur ce système, vous pouvez vous référer à la note technique.

## Les principales composantes de SPISCan

* __Mode assimilation__ : CanCM4 utilise le mode continu comme un cycle d’assimilation pour les variables atmosphériques en 3D, soit la  température, les vents et l’humidité. Les variables océaniques comme la  température de surface de mer et le glace marine sont aussi assimilées par le système. Les données atmosphériques, assimilées, proviennent des analyses globales avec un intervalle temporaire de 6 heures tandis que l’intervalle des données océaniques est un jour. Les analyses des températures d’océan en 3D sont aussi intégrées dans le système SPIScan. Les conditions initiales utilisées par GEM-NEMO proviennent du Système global de prévision d’ensemble (SGPE) qui sont générées a partir de la procédure de Filtre de Kalman d’ensemble (EnKf). Dans cette procédure de filtrage, on applique une procédure du ‘contrôle de la qualité sur un champs d’essai’ sur les observations et on corrige les biais avec  le Système global de prévision déterministe (SGPD). Les analyses du Système global de prévision océan-glace (SGPOG) font partie des données utilisées pour initialiser l’océan et la glace marine. Pour initialiser les champs de surface, le système de prévision de surface (SPS) du SMC  est utilisé. SPS est utilisé dans le mode non-couplé (offline) forcé par les champs atmosphériques provenant des analyses du SMC. 
* __Mode prévision__ : Le système SPIScan est composé de 10 membres d’ensemble provenant de chaque modèle pour un total de 20 membres d’ensemble. Les prévisions mensuelles et les prévisions multi-saisonnières (jusqu’au 12 mois) sont publiées au début de chaque mois.
* __Mode prévisions rétrospectives (hindcast)__ : La climatologie de SPIScan est basée sur un série de prévisions en mode rétrograde (ex. prévisions historiques) couvrant la période de 1980 à 2020. Cette climatologie est très utile pour l’interprétation des prévisions réalistes car les anomalies de prévision en temps réel sont générées à la place des prévisions brutes.   

## Configuration des prévisions SPISCan 

SPISCan est composé de 20 membres, 10 membres du modèle GEM-NEMO et 10 membres du modèle CanCM4. Le dernier jour de chaque mois on exécute une prévision de 12 mois et chaque membre est initialisé avec des conditions initiales valides au même moment, mais légèrement différentes. Lorsque la prévision de l’ensemble est terminée, on construit une moyenne saisonnière de l’anomalie, en soustrayant la moyenne climatologique de 30 ans de ces modèles. Ensuite, on calcule la moyenne d’ensemble pour une prévision déterministe, et les probabilités de chaque catégorie, calculées en calibrant le comptage des membres, pour une prévision probabiliste. 

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier GRIB2.

Les données sont accessibles aux adresses suivantes :

* [https://dd.meteo.gc.ca/ensemble/cansips/grib2/forecast/raw/{YYYY}/{MM}/](https://dd.meteo.gc.ca/ensemble/cansips/grib2/forecast/raw) (membres et produits de prévision à 2.5 degrés, membres à 1 degré)
* [https://dd.meteo.gc.ca/model_cansips/100km/forecast/{YYYY}/{MM}/](https://dd.meteo.gc.ca/model_cansips/100km/forecast) (produits de prévision à 1 degré)
* [https://dd.meteo.gc.ca/ensemble/cansips/grib2/hindcast/raw/{YYYY}/{MM}/](https://dd.meteo.gc.ca/ensemble/cansips/grib2/hindcast/raw) (prévisions rétrospectives)

où :

* __forecast__ : Chaîne de caractères constante indiquant que ce fichier contient des données provenant de la partie prévision du système SIPSCan, en opposition à la partie prévision rétrospective (hindcast).
* __hindcast__ : Chaîne de caractères constante indiquant que ce fichier contient des données provenant de la partie prévision rétrospective du système SIPSCan, en opposition à la partie prévision (forecast).
* __100km__ : Indique une résolution de 1 degré (environ 100km)
* __MM__ : Le mois du début de la prévision [01, 02, 03, ..., 12]
* __YYYY__: L’année du début de la prévision [2012, 2013, ...]

Un historique de 1 mois est conservé dans ces répertoires (sauf pour les prévisions rétrospectives)

## Spécification technique de la grille

Valeurs données aux paramètres de la grille latitude-longitude pour SPISCan, selon la résolution.

### Données à 2.5 degrés de résolution

| Paramètre | Valeur |
| ------ | ------ |
| ni | 145 |
| nj | 73 | 
| résolution | 2.5° |
| coordonnées du premier point de grille | 90° S  0° E | 

### Données à 1 degré de résolution

| Paramètre | Valeur |
| ------ | ------ |
| ni | 360 |
| nj | 180 | 
| résolution | 1.0° |
| coordonnées du premier point de grille | 89.5° S  0.5° E | 

## Nomenclature des noms de fichiers 

 La nomenclature des fichiers est la suivante :

* Membres et produits de prévision à 2.5 degrés:

    * Prévisions en cours : `cansips_forecast_raw_latlon2.5x2.5_{VAR}_{LVLTYPE}_{LVL}_{YYYY}-{MM}_allmembers.grib2`
    * Produits probabilistes: `cansips_forecast_prob-{StatProcess}_latlon2.5x2.5_{VAR}_{LVLTYPE}_{LVL}_{YYYY}-{MM}_{PPP}.grib2`

* Membres et produits de prévision à 1 degré:

    * Prévisions en cours : `cansips_forecast_raw_latlon1.0x1.0_{VAR}_{LVLTYPE}_{LVL}_{YYYY}-{MM}_allmembers.grib2`
    * Produits probabilistes: `{YYYYMM}_MSC_CanSIPS_{Var}-{StatProcess}_{Level}_LatLon1.0_{Month}.grib2`

* Prévisions rétrospectives:

    * `cansips_hindcast_raw_latlon1.0x1.0_{VAR}_{YYYY}-{MM}_allmembers.grib2`

où :

* __cansips|CanSIPS__ : Chaîne de caractères constante indiquant que les données proviennent du système SIPSCan (CanSIPS an anglais)
* __MSC__ : Chaîne de caractères constante pour Meteorological Service of Canada, la source des données
* __forecast__ : Chaîne de caractères constante indiquant que le fichier contient des données provenant de la partie prévision du système SIPSCan, en opposition à la partie prévision rétrospective (hindcast)
* __hindcast__ : Chaîne de caractères constante indiquant que ce fichier contient des données provenant de la partie prévision rétrospective du système SIPSCan, en opposition à la partie prévision (forecast)
* __raw__ : Chaîne de caractères constante indiquant que ce fichier contient des données brutes ou que le biais n’est pas corrigé
* __VAR__ : Variables contenues dans les fichiers, voir la section des variables
* __Var__ : Variables contenues dans les fichiers [PrecipRate, AirTemp]
* __StatProcess__ : Processus statistique [prob-near-normal, prob-below-normal, prob-above-normal, ProbNearNormal, ProbBelowNormal, ProbAboveNormal]
* __LVLTYPE__ : Type de niveau vertical [SFC pour la surface, TGL pour la hauteur au-dessus du sol, ISBL pour le niveau de pression, MSL pour le niveau moyen de la mer]
* __LVL__ : Valeur du niveau vertical
* __Level__ : Niveau vertical [Sfc pour la surface, AGL-2m pour 2m au-dessus du sol]
* __MM__ : Le mois du début de la prévision [01, 02, 03, ..., 12]
* __YYYY__ : L’année du début de la prévision [2012, 2013, ...]
* __allmembers__ : Chaîne de caractères constante indiquant que tous les membres [01, 02, 03, ..., 20] de l’ensemble sont regroupés dans ce fichier
* __PPP__: Durée du produit (ex: P3M indique un produit pour une prévision d'une période de 3 mois)
* __Month__ : Mois concernés à partir du début de la prévision, soit 1 mois [ex : P07M pour décembre si le début de la prévision est le mois de mai] ou plusieurs mois à partir du début de la prévision [ex : P01M-P03M pour juin à août si le début de la prévision est le mois de mai]
* __grib2__ : Chaîne de caractères constante indiquant que le format est GRIB2

Exemples de noms de fichier : 

* cansips_forecast_raw_latlon2.5x2.5_HGT_ISBL_0500_2012-10_allmembers.grib2
* cansips_forecast_raw_latlon1.0x1.0_PRATE_SFC_0_2019-08_allmembers.grib2
* cansips_forecast_prob-below-normal_latlon2.5x2.5_TMP_TGL_2m_P3M_2018-12.grib2
* 202305_MSC_CanSIPS_AirTemp-ProbBelowNormal_AGL-2m_LatLon1.0_P06M-P09M.grib2
* cansips_hindcast_raw_latlon2.5x2.5_HGT_ISBL_0500_1990-11_allmembers.grib2


## Structure interne des fichiers

La structure interne des fichiers des prévisions et celle des prévisions rétrospectives (hindcast) est la suivante : 

Chaque fichier contient 240 enregistrements temporels (12 mois fois 20 membres d'ensemble) et commence par le premier membre d'ensemble. Dans les fichiers SPISCan, les membres d'ensemble sont enregistrés de façon croissante du premier au dernier.

Chaque fichier de la prévision ou de la prévision-rétrospective débute avec une prévision à zéro mois de préavis (en réalité, un jour de préavis pour les prévisions en temps réel). Cela signifie que par exemple, si on a le fichier de SPISCan daté de 2016-02 (ex. cansips_forecast_raw_latlon-1x1_PRATE_SFC_0_2016-02_allmembers.grib2), les données  commencent à partir du 1er février de l'année 2016 et se terminent le 31 janvier de l'année 2017.  À la suite de l'enregistrement pour le mois 01 de l'année 2017, un deuxième membre de l'ensemble SPISCan apparaît pour le mois 02 de l'année 2016, en suivant la même logique décrite plus haut.

## Liste des variables

La liste des variables disponibles de SPISCan est : 

<table id="csv-table" class="display"></table>

<link href="https://cdn.jsdelivr.net/npm/simple-datatables@latest/dist/style.css" rel="stylesheet" type="text/css">
<script src="https://cdn.jsdelivr.net/npm/simple-datatables@latest"></script>
<script src="../../../js/variables_datatable.js" type="text/javascript"></script>
<script>
  loadTable("csv-table", "../../../assets/csv/CanSIPS_fr.csv", "FR");
</script>

La liste des variables pour les produits de probabilité près,sous et au-dessus des normales disponibles de SPISCan est : 

<table id="csv-prob-table" class="display"></table>

<script>
  loadTable("csv-prob-table", "../../../assets/csv/CanSIPS_prob_fr.csv", "FR");
</script>

### Produits d'ensemble

Les fichiers contiennent des produits de probabilité par comptage de membre au-dessus ou au-dessous de différents seuils, des percentiles , moyennes, médianes et écarts-types. Notez que les produits et les seuils sont définis dans la méta-information des fichiers. Les produits suivants sont disponibles pour chacune des variables mentionnées ci-dessous.

###### APCP

* Probabilité au-dessus de 0 kg/(m^2)
* Minimum (percentile 0), maximum (100e percentile), écart-type et moyenne

###### TMP

* Probabilité au-dessus de 0 K
* Minimum (percentile 0), maximum (100e percentile), écart-type et moyenne

## Conseils pour calculer les prévisions d'anomalies 

Il est recommandé d'utiliser directement les prévisions d'anomalies plutôt que les prévisions de données brutes. Les prévisions d'anomalies pour certains mois ou saisons peuvent être obtenues par la soustraction de la climatologie modélisée pour ce mois ou saison. La recette suivante peut être utilisée pour calculer la prévision d'anomalie :

Pour la prévision d'un mois en particulier (ex. 2016-02) on commence par la création d'un fichier de moyenne d'ensemble, et pour cet exemple, on peut nommer ce fichier ensm_for_02_2016. Ce fichier contient maintenant 12 enregistrements temporels car la moyenne de 20 ensembles a été calculée. L'enregistrement temporel de ce fichier commence le mois 02 de l'année 2016 et va jusqu'au mois 01 de l'année 2017.
 
Ensuite, la même procédure est répétée pour les prévisions rétrospectives mais séparément pour chaque année, commençant en 1981 et finissant l'année 2010. Chaque année de la période rétrospective aura donc sa moyenne d'ensemble, par exemple pour le mois 02, ce sera ensm_hin_02_YYYY (YYYY représente chaque année de la période-rétrospective). La moyenne des 30 fichiers de ensm_hin_02_YYYY permettra d'obtenir la climatologie de la moyenne d'ensemble pour les prévisions débutant en  février, qui pourra alors être nommée ensm_hinclim_02, dans cet exemple.

La soustraction de ensm_hinclim_02 à ensm_for_02_2016, permet d'obtenir  la prévision d'anomalie pour le mois 02 de l'année 2016. Puisque cette prévision d'anomalie contient 12 enregistrements temporels, débutant en février 2016, on peut dire que la prévision d'anomalie pour le mois de février c'est une prévision à zéro mois de préavis, celle du mois de mars 2016, une prévision à un mois de préavis, et ainsi de suite jusqu'en janvier 2017 (la dernière de 12 enregistrements) où on a une prévision de 11 mois de préavis.

Une approche très similaire peut être appliquée avec les prévisions saisonnières mais en utilisant les moyennes saisonnières (ex. DJF, JFM, MAM, etc.) qui sont construites avant que l'anomalie de moyenne saisonnière ait été calculée.

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@ec.gc.ca)

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).
