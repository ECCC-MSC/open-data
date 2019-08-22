[In English](readme_cansips-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [SPISCan](readme_cansips_fr.md) > Données GRIB2 de SPISCan sur le Datamart du SMC

# Données GRIB2 du Système de Prévision Interannuelle et Saisonnière Canadien (SPISCan)

Le [Système de prévision interannuelle et saisonnière canadien (SPISCan)](readme_cansips_fr.md) est un système de prévision à long terme dont l’objectif est de prévoir l’évolution des conditions climatiques à l’échelle globale. SPISCan est un système d’ensemble multi-modèle (Multi-Model Ensemble [MME]) utilisant CanCM4 et GEM-NEMO, deux modèles climatiques développés au Centre canadien de la modélisation et de l'analyse climatique (CCmaC) et au Centre météorologique canadien (CMC). Ce système de prévision est entièrement couplé atmosphère-océan-glace-sol. SPISCan utilise l'infrastructure d'assimilation en place pour les autres systèmes de prévision afin d'obtenir les conditions initiales de l'atmosphère, de la température de la surface de la mer et de glace marine. Pour plus de détails sur ce système, vous pouvez vous référer à la note technique.

## Les principales composantes de SPISCan

* __Mode assimilation__ : CanCM4 utilise le mode continu comme un cycle d’assimilation pour les variables atmosphériques en 3D, soit la  température, les vents et l’humidité. Les variables océaniques comme la  température de surface de mer et le glace marine sont aussi assimilées par le système. Les données atmosphériques, assimilées, proviennent des analyses globales avec un intervalle temporaire de 6 heures tandis que l’intervalle des données océaniques est un jour. Les analyses des températures d’océan en 3D sont aussi intégrées dans le système SPIScan. Les conditions initiales utilisées par GEM-NEMO proviennent du Système global de prévision d’ensemble (SGPE) qui sont générées a partir de la procédure de Filtre de Kalman d’ensemble (EnKf). Dans cette procédure de filtrage, on applique une procédure du ‘contrôle de la qualité sur un champs d’essai’ sur les observations et on corrige les biais avec  le Système global de prévision déterministe (SGPD). Les analyses du Système global de prévision océan-glace (SGPOG) font partie des données utilisées pour initialiser l’océan et la glace marine. Pour initialiser les champs de surface, le système de prévision de surface (SPS) du SMC  est utilisé. SPS est utilisé dans le mode non-couplé (offline) forcé par les champs atmosphériques provenant des analyses du SMC. 
* __Mode prévision__ : Le système SPIScan est composé de 10 membres d’ensemble provenant de chaque modèle pour un total de 20 membres d’ensemble. Les prévisions mensuelles et les prévisions multi-saisonnières (jusqu’au 12 mois) sont publiées au début de chaque mois.
* __Mode prévisions rétrospectives (hindcast)__ : La climatologie de SPIScan est basée sur un série de prévisions en mode rétrograde (ex. prévisions historiques) couvrant la période de 1981 à 2010. Cette climatologie est très utile pour l’interprétation des prévisions réalistes car les anomalies de prévision en temps réel sont générées à la place des prévisions brutes.   

## Configuration des prévisions SPISCan 

SPISCan est composé de 20 membres, 10 membres du modèle GEM-NEMO et 10 membres du modèle CanCM4. Le dernier jour de chaque mois on exécute une prévision de 12 mois et chaque membre est initialisé avec des conditions initiales valides au même moment, mais légèrement différentes. Lorsque la prévision de l’ensemble est terminée, on construit une moyenne saisonnière de l’anomalie, en soustrayant la moyenne climatologique de 30 ans de ces modèles. Ensuite, on calcule la moyenne d’ensemble pour une prévision déterministe, et les probabilités de chaque catégorie, calculées en calibrant le comptage des membres, pour une prévision probabiliste. 

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTP. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier GRIB2.

Les données sont accessibles aux adresses suivantes :

* https://dd.meteo.gc.ca/ensemble/cansips/grib2/forecast/raw/YYYY/MM/
* https://dd.meteo.gc.ca/ensemble/cansips/grib2/hindcast/raw/YYYY/MM/

où :

* __forecast__ : Chaîne de caractères constante indiquant que ce fichier contient des données provenant de la partie prévision du système SIPSCan, en opposition à la partie prévision rétrospective (hindcast).
* __hindcast__ : Chaîne de caractères constante indiquant que ce fichier contient des données provenant de la partie prévision rétrospective du système SIPSCan, en opposition à la partie prévision (forecast).
* __MM__ : Le mois du début de la prévision [01, 02, 03, ..., 12]
* __YYYY__: L’année du début de la prévision [2012, 2013, ...]

Un historique de 2 mois est conservé dans ce répertoire.

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

NOTE : TOUTES LES HEURES SONT EN UTC.

Les fichiers ont la nomenclature suivante :

* Nom fichier pour les prévisions en cours : cansips_forecast_raw_projection_VAR_YYYY-MM_allmembers.grib2
* Nom fichier pour les prévisions rétrospectives : cansips_hindcast_raw_projection_VAR_YYYY-MM_allmembers.grib2
* Nom fichiers pour les produits probabilistes: cansips_forecast_prob-produit_projection_VAR_PPP_YYYY-MM.grib2

où :

* __cansips__ : Chaîne de caractères constante indiquant le nom du système émetteur des prévisions.
* __forecast__ : Chaîne de caractères constante indiquant que ce fichier contient des données provenant de la partie prévision du système SIPSCan, en opposition à la partie prévision rétrospective (hindcast).
* __hindcast__ : Chaîne de caractères constante indiquant que ce fichier contient des données provenant de la partie prévision rétrospective du système SIPSCan, en opposition à la partie prévision (forecast).
* __raw__ : Chaîne de caractères constante indiquant que ce fichier contient des données brutes ou que le biais n’est pas corrigé.
* __projection__ : Chaîne de caractères indiquant la projection utilisée [latlon] et la résolution [2.5x2.5, 1.0x1.0].
* __VAR__ : Code de la variables contenu dans le fichier, voir la liste des variables.
* __MM__ : Le mois du début de la prévision [01, 02, 03, ..., 12]
* __YYYY__ : L’année du début de la prévision [2012, 2013, ...]
* __allmembers__ : Chaîne de caractères constante indiquant que tous les membres [01, 02, 03, ..., 20] de l’ensemble sont regroupés dans ce fichier.
* __grib2__ : Chaîne de caractères constante indiquant que le format est GRIB2.
* __produit__: Description du produit (ex: près,sous ou au-dessus des normales)
* __PPP__: Durée du produit ex: P3M indique un produit pour une prévision d'une période de 3 mois

Exemples de noms de fichier : 

* cansips_forecast_raw_latlon2.5x2.5_HGT_ISBL_0500_2012-10_allmembers.grib2
* cansips_forecast_raw_latlon1.0x1.0_PRATE_SFC_0_2019-08_allmembers.grib2
* cansips_forecast_prob-below-normal_latlon2.5x2.5_TMP_TGL_2m_P3M_2018-12.grib2

## Structure interne des fichiers

La structure interne des fichiers des prévisions et celle des prévisions rétrospectives (hindcast) est la suivante : 

Chaque fichier contient 240 enregistrements temporels (12 mois fois 20 membres d'ensemble) et commence par le premier membre d'ensemble. Dans les fichiers SPISCan, les membres d'ensemble sont enregistrés de façon croissante du premier au dernier.

Chaque fichier de la prévision ou de la prévision-rétrospective débute avec une prévision à zéro mois de préavis (en réalité, un jour de préavis pour les prévisions en temps réel). Cela signifie que par exemple, si on a le fichier de SPISCan daté de 2016-02 (ex. cansips_forecast_raw_latlon-1x1_PRATE_SFC_0_2016-02_allmembers.grib2), les données  commencent à partir du 1er février de l'année 2016 et se terminent le 31 janvier de l'année 2017.  À la suite de l'enregistrement pour le mois 01 de l'année 2017, un deuxième membre de l'ensemble SPISCan apparaît pour le mois 02 de l'année 2016, en suivant la même logique décrite plus haut.

## Niveaux

Ces données sont disponibles pour la surface et pour certains niveaux isobariques.

## Liste des variables

La liste des variables disponibles de SPISCan est : 

* Température de l'eau (WTMP_SFC_0)
* Taux de précipitations (PRATE_SFC_0)
* Température à 2m (TMP_TGL_2m)
* Température à 850 hPa (TMP_ISBL_850)
* Pression au niveau moyen de la mer (PRMSL_MSL_0)
* Hauteur géopotentielle à 500 hPa (HGT_ISBL_500)
* Composante U du vent à 200 hPa (UGRD_ISBL_200)
* Composante U du vent à 850 hPa (UGRD_ISBL_850)
* Composante V du vent à 200 hPa (VGRD_ISBL_200)
* Composante V du vent à 850 hPa (VGRD_ISBL_200)

La liste des variables pour les produits de probabilité près,sous et au-dessus des normales disponibles de SPISCan est : 

* Température à 2m (TMP_TGL_2m)
* Taux de précipitations (PRATE_SFC_0)

## Conseils pour calculer les prévisions d'anomalies 

Il est recommandé d'utiliser directement les prévisions d'anomalies plutôt que les prévisions de données brutes. Les prévisions d'anomalies pour certains mois ou saisons peuvent être obtenues par la soustraction de la climatologie modélisée pour ce mois ou saison. La recette suivante peut être utilisée pour calculer la prévision d'anomalie :

Pour la prévision d'un mois en particulier (ex. 2016-02) on commence par la création d'un fichier de moyenne d'ensemble, et pour cet exemple, on peut nommer ce fichier ensm_for_02_2016. Ce fichier contient maintenant 12 enregistrements temporels car la moyenne de 20 ensembles a été calculée. L'enregistrement temporel de ce fichier commence le mois 02 de l'année 2016 et va jusqu'au mois 01 de l'année 2017.
 
Ensuite, la même procédure est répétée pour les prévisions rétrospectives mais séparément pour chaque année, commençant en 1981 et finissant l'année 2010. Chaque année de la période rétrospective aura donc sa moyenne d'ensemble, par exemple pour le mois 02, ce sera ensm_hin_02_YYYY (YYYY représente chaque année de la période-rétrospective). La moyenne des 30 fichiers de ensm_hin_02_YYYY permettra d'obtenir la climatologie de la moyenne d'ensemble pour les prévisions débutant en  février, qui pourra alors être nommée ensm_hinclim_02, dans cet exemple.

La soustraction de ensm_hinclim_02 à ensm_for_02_2016, permet d'obtenir  la prévision d'anomalie pour le mois 02 de l'année 2016. Puisque cette prévision d'anomalie contient 12 enregistrements temporels, débutant en février 2016, on peut dire que la prévision d'anomalie pour le mois de février c'est une prévision à zéro mois de préavis, celle du mois de mars 2016, une prévision à un mois de préavis, et ainsi de suite jusqu'en janvier 2017 (la dernière de 12 enregistrements) où on a une prévision de 11 mois de préavis.

Une approche très similaire peut être appliquée avec les prévisions saisonnières mais en utilisant les moyennes saisonnières (ex. DJF, JFM, MAM, etc.) qui sont construites avant que l'anomalie de moyenne saisonnière ait été calculée.

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : ec.dps-client.ec@canada.ca

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).
