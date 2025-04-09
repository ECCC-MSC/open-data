[In English](readme_cansips-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [SPISCan](readme_cansips_fr.md) > Données GRIB2 de SPISCan sur le Datamart du SMC

# Données GRIB2 du Système de Prévision Interannuelle et Saisonnière Canadien (SPISCan)

Le [Système de prévision interannuelle et saisonnière canadien (SPISCan)](readme_cansips_fr.md) est un système de prévision à long terme dont l’objectif est de prévoir l’évolution des conditions climatiques à l’échelle globale. SPISCan est un système d’ensemble multi-modèle (Multi-Model Ensemble [MME]) utilisant deux modèles couplés atmosphère-océan-terre (CanESM5 et GEM5.2-NEMO) développés au Centre canadien de la modélisation et de l'analyse climatique (CCmaC), à la Division de la recherche météorologique (DRM) et au Centre de prévision météorologique et environnementale du Canada (CPMEC). Ce système de prévision est entièrement couplé atmosphère-océan-glace-sol. SPISCan utilise l'infrastructure d'assimilation en place pour les autres systèmes de prévision afin d'obtenir les conditions initiales de l'atmosphère, de la température de la surface de la mer et de glace marine. Pour plus de détails sur ce système, vous pouvez vous référer à la note technique.

## Les principales composantes de SPISCan

* __Mode assimilation__ :

     * CanESM5 : Les conditions atmosphériques et océaniques initiales sont obtenues en exécutant un processus d'assimilation couplé atmosphère-océan-glace de mer contraint par l'analyse atmosphérique du CMC (SGPD) et l'analyse océanique de GIOPS à travers la même procédure de nudging. L'épaisseur modélisée de la glace de mer dans l'hémisphère nord est contrainte par des valeurs proches du modèle statistique SMv3. La concentration modélisée de la glace de mer et la température de surface de la mer sont contraintes à des valeurs proches de celles du GDPS G6. Les variables terrestres sont initialisées par la réponse de CLASS/CTEM à la composante atmosphérique assimilée.
     * GEM5.2-NEMO : Les conditions initiales atmosphériques de GEM5.2-NEMO proviennent de celles du Global Ensemble Prediction System (SGPE). Les conditions initiales de l'océan et de la glace de mer dans les prévisions proviennent de l'analyse GIOPS du CMC, tandis que les conditions initiales de la surface terrestre proviennent de l'analyse du CMC (SGPD) après ajustement à la climatologie des prévisions rétrospectives.

* __Mode prévision__ : Le système SPIScan est composé de 20 membres d’ensemble provenant de chaque modèle pour un total de 40 membres d’ensemble. Les prévisions mensuelles et les prévisions multi-saisonnières (jusqu’au 12 mois) sont générées en combinant les prévisions produites le dernier jour de chaque mois (membres de l'ensemble 1-10) avec les prévisions émises quatre jours avant (membres de l'ensemble 11-20).

* __Mode prévisions rétrospectives (hindcast)__ : La climatologie de SPIScan est basée sur un série de prévisions en mode rétrograde (ex. prévisions historiques) couvrant la période de 1990 à 2020. Cette climatologie est très utile pour l’interprétation des prévisions réalistes car les anomalies de prévision en temps réel sont générées à la place des prévisions brutes.

* __Mode vérification__ : Afin d'évaluer la performance des prévisions historiques de SPISCan, des prévisions déterministes d'anomalies de température et de précipitations normalisées (au-dessus, en dessous et proches de la normale) sont évaluées globalement, sur une période de trois mois, en les comparant aux anomalies observées (catégories terciles) sur la base des données ERA5 du CEPMMT (ECMWF) pour la même période climatologique.

## Configuration des prévisions SPISCan 

Dans SIPSCanv3, la taille de l'ensemble des prévisions a été augmentée de 20 à 40 membres (20 membres GEM-NEMO + 20 membres CanESM5). Pour ce faire, on combine les prévisions initialisées le dernier jour du mois avec les prévisions initialisées quatre jours auparavant.  Pour chaque modèle, une prévision à 12 mois est produite avec les 10 premiers membres de chaque modèle obtenus à partir du dernier jour du mois et le deuxième ensemble de 10 membres provenant des prévisions initialisées quatre jours auparavant.  Lorsque les prévisions d'ensemble sont terminées, nous construisons des anomalies saisonnières moyennes par rapport aux prévisions rétrospectives sur 30 ans pour chaque membre de l'ensemble. Ensuite, nous mettons en œuvre des approches déterministes (moyenne de l'ensemble) et probabilistes (différentes catégories en fonction de la taille de l'ensemble) pour prévoir les saisons à venir.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier GRIB2.

Les données sont accessibles aux adresses suivantes :

* [https://dd.meteo.gc.ca/ensemble/cansips/grib2/forecast/raw/{YYYY}/{MM}/](https://dd.meteo.gc.ca/ensemble/cansips/grib2/forecast/raw) (membres et produits de prévision à 2.5 degrés)
* [https://dd.meteo.gc.ca/model_cansips/100km/forecast/{YYYY}/{MM}/](https://dd.meteo.gc.ca/model_cansips/100km/forecast) (membres et produits de prévision à 1 degré)
* [https://dd.meteo.gc.ca/model_cansips/100km/hindcast/{YYYY}/{MM}/](https://dd.meteo.gc.ca/model_cansips/100km/hindcast) (prévisions rétrospectives)
* [https://dd.meteo.gc.ca/model_cansips/100km/verification/{YYYY}](https://dd.meteo.gc.ca/model_cansips/100km/verification) (produits de vérification à 1 degré)

où :

* __forecast__ : Chaîne de caractères constante indiquant que ce fichier contient des données provenant de la partie prévision du système SIPSCan, en opposition à la partie prévision rétrospective (hindcast).
* __hindcast__ : Chaîne de caractères constante indiquant que ce fichier contient des données provenant de la partie prévision rétrospective du système SIPSCan, en opposition à la partie prévision (forecast).
* __verification__ : Chaîne de caractères constante indiquant que ce fichier contient des données de vérification contre observations ou réanalyses 
* __100km__ : Indique une résolution de 1 degré (environ 100km)
* __MM__ : Le mois du début de la prévision [01, 02, 03, ..., 12]
* __YYYY__: L’année du début de la prévision [Ex: 2012, 2013, ...]


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

    * Membres individuels : `cansips_forecast_raw_latlon2.5x2.5_{VAR}_{LVLTYPE}_{LVL}_{YYYY}-{MM}_allmembers.grib2`
    * Produits probabilistes: `cansips_forecast_prob-{StatProcess}_latlon2.5x2.5_{VAR}_{LVLTYPE}_{LVL}_{YYYY}-{MM}_{PPP}.grib2`

* Membres et produits de prévision à 1 degré:

    * Membres individuels : `{YYYYMM}_MSC_CanSIPS_{Var}_{Level}_LatLon1.0_P{Month}M.grib2` 
    * Produits probabilistes: `{YYYYMM}_MSC_CanSIPS_{Var}-{StatProcess}_{Level}_LatLon1.0_P{Month}M.grib2`

* Prévisions rétrospectives:

    * `{YYYYMM}_MSC_CanSIPS-Hindcast_{Var}_{Level}_LatLon1.0_P{Month}M.grib2`

* Produits de vérification:

    * `{YYYYMM}_MSC_CanSIPS_{Var-Anomaly}-ERA5_{Level}_LatLon1.0_P{Month}M-P{Month}M.grib2`

où :

* __cansips|CanSIPS__ : Chaîne de caractères constante indiquant que les données proviennent du système SIPSCan (CanSIPS an anglais)
* __MSC__ : Chaîne de caractères constante pour Meteorological Service of Canada, la source des données
* __forecast__ : Chaîne de caractères constante indiquant que le fichier contient des données provenant de la partie prévision du système SIPSCan, en opposition à la partie prévision rétrospective (hindcast)
* __CanSIPS-hindcast__ : Chaîne de caractères constante indiquant que ce fichier contient des données provenant de la partie prévision rétrospective du système SIPSCan, en opposition à la partie prévision (forecast)
* __raw__ : Chaîne de caractères constante indiquant que ce fichier contient des données brutes ou que le biais n’est pas corrigé
* __VAR__ : Variables contenues dans les fichiers à 2 degrés [TMP, HGT, PRATE, SSHG, PRMSL, UGRD, VGRD]
* __Var__ : Variables contenues dans les fichiers à 1 degré [AirTemp, GeopotentialHeight, PrecipRate, SeaSfcHeight-Geoid, Pressure, WindU, WindV]
* __Var-Anomaly__ : Variables d'anomalie contenues dans les fichiers à 1 degré [AirTempAnomaly, PrecipAccumAnomaly]
* __StatProcess__ : Processus statistique [prob-near-normal, prob-below-normal, prob-above-normal, ProbNearNormal, ProbBelowNormal, ProbAboveNormal]
* __ERA5__ : Chaîne de caractères constante indiquant que les produits de vérification sont générés à partir des reanalyses ERA5 du CEPMMT (ECMWF)
* __LVLTYPE__ : Type de niveau vertical [SFC pour la surface, TGL pour la hauteur au-dessus du sol, ISBL pour le niveau de pression, MSL pour le niveau moyen de la mer]
* __LVL__ : Valeur du niveau vertical
* __Level__ : Niveau vertical [Sfc pour la surface, AGL-2m pour 2m au-dessus du sol]
* __MM__ : Le mois du début de la prévision [01, 02, 03, ..., 12]
* __YYYY__ : L’année du début de la prévision 
* __allmembers__ : Chaîne de caractères constante indiquant que tous les membres [01, 02, 03, ..., 20] de l’ensemble sont regroupés dans ce fichier
* __PPP__: Durée du produit (ex: P3M indique un produit pour une prévision d'une période de 3 mois)
* __Month__ : Mois concernés à partir du début de la prévision, soit 1 mois [ex : P07M pour décembre si le début de la prévision est le mois de mai] ou plusieurs mois à partir du début de la prévision [ex : P01M-P03M pour juin à août si le début de la prévision est le mois de mai]
* __P{Month}M-P{Month}M__ : Période de 3 mois couverte pour la vérification
* __grib2__ : Chaîne de caractères constante indiquant que le format est GRIB2

Exemples de noms de fichier : 

* cansips_forecast_raw_latlon2.5x2.5_HGT_ISBL_0500_2012-10_allmembers.grib2
* cansips_forecast_prob-below-normal_latlon2.5x2.5_TMP_TGL_2m_P3M_2018-12.grib2
* 202309_MSC_CanSIPS_AirTemp_AGL-2m_LatLon1.0_P00M.grib2
* 202305_MSC_CanSIPS_AirTemp-ProbBelowNormal_AGL-2m_LatLon1.0_P06M-P09M.grib2
* 202010_MSC_CanSIPS-Hindcast_WaterTemp_Sfc_LatLon1.0_P10M.grib2
* 202503_MSC_CanSIPS_AirTempAnomaly-ERA5_AGL-2m_LatLon1.0_P12M-P02M.grib2
* 202504_MSC_CanSIPS_PrecipAccumAnomaly-ERA5_Sfc_LatLon1.0_P01M-P03M.grib2

## Structure interne des fichiers

La structure interne des fichiers des prévisions et prévisions rétrospectives (hindcast) est décrite ci-dessous. 

Chaque fichier contient 40 enregistrements (correspondant aux 40 membres de l'ensemble), les 20 premiers membres de l'ensemble appartiennent à GEM5.2-NEMO tandis que les 20 derniers membres de l'ensemble proviennent de CanESM5.

Voici la classification détaillée des membres de l'ensemble par rapport au modèle et à la date de début:

* ensemble 1-10 : de GEM5.2-NEMO avec des prévisions initialisées le dernier jour du mois
* ensemble 11-20 : de GEM5.2-NEMO avec des prévisions initialisées quatre jours avant le dernier jour du mois
* ensemble 21-30 : de CanESM5 avec des prévisions initialisées le dernier jour du mois
* ensemble 31-40 : de CanESM5 avec des prévisions initialisées quatre jours avant le dernier jour du mois

## Liste des variables

__Membres individuels:__

<table id="csv-table" class="display"></table>

<link href="https://cdn.jsdelivr.net/npm/simple-datatables@latest/dist/style.css" rel="stylesheet" type="text/css">
<script src="https://cdn.jsdelivr.net/npm/simple-datatables@latest"></script>
<script src="../../../js/variables_datatable.js" type="text/javascript"></script>
<script>
  loadTable("csv-table", "../../../assets/csv/CanSIPS_Variables-List_fr.csv");
</script>

__Produits d'ensemble:__

<table id="csv-prob-table" class="display"></table>

<script>
  loadTable("csv-prob-table", "../../../assets/csv/CanSIPS-Products_Variables-List_fr.csv");
</script>

__Produits de probabilité terciles__ :

Les fichiers contiennent des probabilité de terciles pour les catégories supérieures, proches ou inférieures à la normale.  Les variables considérées sont les précipitations et la température. Pour chacune des deux variables, il existe trois fichiers pour représenter les trois probabilités de terciles, décrits ci-dessous.

* APCP

    * Probabilité supérieure au seuil du 66.7e centile (sans unité) - souvent appelée probabilité de précipitations supérieures à la normale
    * Minimum (0 %), maximum (100 %)
    * Probabilité inférieure au seuil du 33.3e centile (sans unité) - souvent appelée probabilité de précipitations inférieures à la normale
    * Minimum (0 %), maximum (100 %)
    * Probabilité comprise entre 33.3 et 66.7e centiles (sans unité) - souvent appelée probabilité de précipitations proches de la normale/climatologie
    * Minimum (0 %), maximum (100 %)

* TMP

    * Probabilité supérieure au seuil du 66.7e centile (sans unité) - souvent appelée probabilité que la température soit supérieure à la normale
    * Minimum (0 %), maximum (100 %)
    * Probabilité inférieure au seuil du 33,3e centile (sans unité) - souvent appelée Probabilité que la température soit inférieure à la normale
    * Minimum (0 %), maximum (100 %)
    * Probabilité entre les percentiles 33,3 et 66,7 (sans unité) – souvent appelée Probabilité que la température soit proche de la normale/climatologie
    * Minimum (0 %), maximum (100 %)

__Produits de probabilité de dépassement :__

Ces fichiers contiennent les probabilités de dépassement et sont disponibles en fonction de neuf seuils, soit:

1. Probabilité que la température/précipitation soit supérieure au 10e percentile
2. Probabilité que la température/précipitation soit supérieure au 20e percentile
3. Probabilité que la température/précipitation soit supérieure au 30e percentile
…….
8. Probabilité que la température/précipitation soit supérieure au 80e percentile
9. Probabilité que la température/précipitation soit supérieure au 90e percentile

## Conseils pour calculer les prévisions d'anomalies 

Il est recommandé d'utiliser directement les prévisions d'anomalies plutôt que les prévisions de données brutes. Les prévisions d'anomalies pour certains mois ou saisons peuvent être obtenues par la soustraction de la climatologie modélisée pour ce mois ou saison. La recette suivante peut être utilisée pour calculer la prévision d'anomalie :

Pour la prévision d'un mois en particulier (ex. 2016-02) on commence par la création d'un fichier de moyenne d'ensemble, et pour cet exemple, on peut nommer ce fichier ensm_for_02_2016. Ce fichier contient maintenant 12 enregistrements temporels car la moyenne de 40 ensembles a été calculée. L'enregistrement temporel de ce fichier commence le mois 02 de l'année 2016 et va jusqu'au mois 01 de l'année 2017.
 
Ensuite, la même procédure est répétée pour les prévisions rétrospectives mais séparément pour chaque année, commençant en 1981 et finissant l'année 2010. Chaque année de la période rétrospective aura donc sa moyenne d'ensemble, par exemple pour le mois 02, ce sera ensm_hin_02_YYYY (YYYY représente chaque année de la période-rétrospective). La moyenne des 30 fichiers de ensm_hin_02_YYYY permettra d'obtenir la climatologie de la moyenne d'ensemble pour les prévisions débutant en  février, qui pourra alors être nommée ensm_hinclim_02, dans cet exemple.

La soustraction de ensm_hinclim_02 à ensm_for_02_2016, permet d'obtenir  la prévision d'anomalie pour le mois 02 de l'année 2016. Puisque cette prévision d'anomalie contient 12 enregistrements temporels, débutant en février 2016, on peut dire que la prévision d'anomalie pour le mois de février c'est une prévision à zéro mois de préavis, celle du mois de mars 2016, une prévision à un mois de préavis, et ainsi de suite jusqu'en janvier 2017 (la dernière de 12 enregistrements) où on a une prévision de 11 mois de préavis.

Une approche très similaire peut être appliquée avec les prévisions saisonnières mais en utilisant les moyennes saisonnières (ex. DJF, JFM, MAM, etc.) qui sont construites avant que l'anomalie de moyenne saisonnière ait été calculée.

## Support

Pour toute question relative à ces données, merci de [nous contacter](https://meteo.gc.ca/mainmenu/contact_us_f.html).

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).
