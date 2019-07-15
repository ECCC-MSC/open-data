[In English](readme_cansips-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [SPISCan](readme_cansips_fr.md) > Données GRIB2 de SPISCan sur le Datamart du SMC

# Données GRIB2 du Système de Prévision Interannuelle et Saisonnière Canadien (SPISCan)

Le [Système de prévision interannuelle et saisonnière canadien (SPISCan)](readme_cansips_fr.md) est un système de prévision à long terme dont l’objectif est de prévoir l’évolution des conditions climatiques à l’échelle globale. SPISCan est un système d’ensemble multi-modèle (Multi-Model Ensemble [MME]) utilisant deux modèles climatiques développés au Centre canadien de la modélisation et de l’analyse climatique (CCmaC). Ce système de prévision est entièrement couplé atmosphère-océan-glace-sol. SPISCan utilise l’infrastructure d’assimilation en place pour les autres systèmes de prévision afin d’obtenir les conditions initiales de l’atmosphère, de la température de la surface de la mer et de glace marine. Pour plus de détails sur ce système, vous pouvez vous référer à la note technique.

## Les principales composantes de SPISCan

* __Mode assimilation__ : SPISCan utilise un cycle d’assimilation continue pour les variables atmosphériques suivantes : la température, le vent et l’humidité. La température de la surface de la mer et la glace marine sont aussi assimilées par le système. Les données assimilées sont fournies par les analyses atmosphériques globales finales disponibles aux 6 heures ainsi que les analyses quotidiennes de la température de la surface de la mer et de la glace marine. De plus une analyse de l’océan 3D est assimilée dans le champ d’essai du modèle océanique de SPISCan avant de déclencher l’intégration des prévisions.
* __Mode prévision__ : Les prévisions de SPISCan sont basées sur un ensemble de 10 prévisions produites par chacun des deux modèles climatiques du CCmaC pour un ensemble total de 20 membres. Des prévisions mensuelles et multi-saisons (jusqu’à 12 mois) sont émises le premier jour de chaque mois.
* __Mode prévisions rétrospectives (hindcast)__ : La climatologie du SPISCan est basée sur des prévisions rétrospectives couvrant la période 1981-2010. Cette climatologie est nécessaire pour l’utilisation des prévisions à long terme puisque l’interprétation des prévisions de SIPSCan se fait généralement du point de vue des anomalies prévues par le système.

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

Valeurs données aux paramètres de la grille latitude-longitude pour SPISCan.

| Paramètre | Valeur |
| ------ | ------ |
| ni | 145 |
| nj | 73 | 
| résolution | 2.5° |
| coordonnées du premier point de grille | 90° S  0° E | 

## Nomenclature des noms de fichiers 

NOTE : TOUTES LES HEURES SONT EN UTC.

Les fichiers ont la nomenclature suivante :

* Nom fichier pour les prévisions en cours : cansips_forecast_raw_latlon2.5x2.5_VAR_YYYY-MM_allmembers.grib2
* Nom fichier pour les prévisions rétrospectives : cansips_hindcast_raw_latlon2.5x2.5_VAR_YYYY-MM_allmembers.grib2

où :

* __cansips__ : Chaîne de caractères constante indiquant le nom du système émetteur des prévisions.
* __forecast__ : Chaîne de caractères constante indiquant que ce fichier contient des données provenant de la partie prévision du système SIPSCan, en opposition à la partie prévision rétrospective (hindcast).
* __hindcast__ : Chaîne de caractères constante indiquant que ce fichier contient des données provenant de la partie prévision rétrospective du système SIPSCan, en opposition à la partie prévision (forecast).
* __raw__ : Chaîne de caractères constante indiquant que ce fichier contient des données brutes ou que le biais n’est pas corrigé.
* __latlon2.5x2.5__ : Chaîne de caractères constante indiquant que la projection utilisée est latitude-longitude à 2.5 x 2.5 degrés de résolution.
* __VAR__ : Code de la variables contenu dans le fichier, voir la liste des variables.
* __MM__ : Le mois du début de la prévision [01, 02, 03, ..., 12]
* __YYYY__ : L’année du début de la prévision [2012, 2013, ...]
* __allmembers__ : Chaîne de caractères constante indiquant que tous les membres [01, 02, 03, ..., 20] de l’ensemble sont regroupés dans ce fichier.
* __grib2__ : Chaîne de caractères constante indiquant que le format est GRIB2.

Exemple de nom de fichier : 

cansips_forecast_raw_latlon2.5x2.5_HGT_ISBL_0500_2012-10_allmembers.grib2

Ce fichier de format GRIB2 (.grib2) a été généré par la composante prévision système SPISCan sur une grille latitude-longitude à 2.5 x 2.5 degrés de résolution. La prévision a été produite pour le mois d’octobre 2012 (2012-10). Ce fichier contient les moyennes mensuelles de tous les membres du système (allmembers) pour la variable « hauteur géopotentielle (HGT) » au niveau isobarique 500hpa (ISBL_0500).

## Structure interne des fichiers

La structure interne des fichiers des prévisions et celle des prévisions rétrospectives (hindcast) est la suivante : 

Chaque fichier contient 240 enregistrements temporels (12 mois fois 20 membres d'ensemble) et commence par le premier membre d'ensemble. Dans les fichiers SPISCan, les membres d'ensemble sont enregistrés de façon croissante du premier au dernier.

Chaque fichier de la prévision ou de la prévision-rétrospective débute avec une prévision à zéro mois de préavis (en réalité, un jour de préavis pour les prévisions en temps réel). Cela signifie que par exemple, si on a le fichier de SPISCan daté de 2016-02 (ex. cansips_forecast_raw_latlon-1x1_PRATE_SFC_0_2016-02_allmembers.grib2), les données  commencent à partir du 1er février de l'année 2016 et se terminent le 31 janvier de l'année 2017.  À la suite de l'enregistrement pour le mois 01 de l'année 2017, un deuxième membre de l'ensemble SPISCan apparaît pour le mois 02 de l'année 2016, en suivant la même logique décrite plus haut.


## Niveaux

Ces données sont disponibles pour la surface et pour certains niveaux isobariques.

## Liste des variables

Attention : les tableaux ci-dessous ne sont pas à jour (à venir), certaines variables sont manquantes. N'hésitez pas à [nous contacter](mailto:ec.dps-client.ec@canada.ca) pour plus d'information.

* [Prévision pour l’échéance zéro](https://meteo.gc.ca/grib/CANSIPS/CANSIPS_latlon2.5x2.5_ALL_VAR_Lead-time-month-ZERO_hindcast_f.html)
* [Prévision pour les autres échéances](https://meteo.gc.ca/grib/CANSIPS/CANSIPS_latlon2.5x2.5_ALL_VAR_Lead-time-month-NONZERO_hindcast_f.html)

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
