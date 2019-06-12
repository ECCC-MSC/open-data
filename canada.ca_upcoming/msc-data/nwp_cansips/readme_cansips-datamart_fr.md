[In English](readme_cansips-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données ouvertes publiques du SMC](../readme_fr.md) > SPISCan sur le Datamart du SMC

# Données GRIB2 du Système de Prévision Interannuelle et Saisonnière Canadien (SPISCan)

Le [Système de prévision interannuelle et saisonnière canadien (SPISCan)](readme_cansips_fr.md) est un système de prévision à long terme dont l’objectif est de prévoir l’évolution des conditions climatiques à l’échelle globale. SPISCan est un système d’ensemble multi-modèle (Multi-Model Ensemble [MME]) utilisant deux modèles climatiques développés au Centre canadien de la modélisation et de l’analyse climatique (CCmaC). Ce système de prévision est entièrement couplé atmosphère-océan-glace-sol. SPISCan utilise l’infrastructure d’assimilation en place pour les autres systèmes de prévision afin d’obtenir les conditions initiales de l’atmosphère, de la température de la surface de la mer et de glace marine. Pour plus de détails sur ce système, vous pouvez vous référer à la note technique.

## Les principales composantes de SPISCan

* __Mode assimilation__ : SPISCan utilise un cycle d’assimilation continue pour les variables atmosphériques suivantes : la température, le vent et l’humidité. La température de la surface de la mer et la glace marine sont aussi assimilées par le système. Les données assimilées sont fournies par les analyses atmosphériques globales finales disponibles aux 6 heures ainsi que les analyses quotidiennes de la température de la surface de la mer et de la glace marine. De plus une analyse de l’océan 3D est assimilée dans le champ d’essai du modèle océanique de SPISCan avant de déclencher l’intégration des prévisions.
* __Mode prévision__ : Les prévisions de SPISCan sont basées sur un ensemble de 10 prévisions produites par chacun des deux modèles climatiques du CCmaC pour un ensemble total de 20 membres. Des prévisions mensuelles et multi-saisons (jusqu’à 12 mois) sont émises le premier jour de chaque mois.
* __Mode prévisions rétrospectives (hindcast)__ : La climatologie du SPISCan est basée sur des prévisions rétrospectives couvrant la période 1981-2010. Cette climatologie est nécessaire pour l’utilisation des prévisions à long terme puisque l’interprétation des prévisions de SIPSCan se fait généralement du point de vue des anomalies prévues par le système.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le Protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../how-to/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTP. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier GRIB2.

Les données sont accessibles aux adresses suivantes :

* https://dd.meteo.gc.ca/ensemble/cansips/grib2/forecast/raw/YYYY/MM/
* https://dd.meteo.gc.ca/ensemble/cansips/grib2/hindcast/raw/YYYY/MM/

où :

* __forecast__ : Chaîne de caractères constante indiquant que ce fichier contient des données provenant de la partie prévision du système SIPSCan, en opposition à la partie prévision rétrospective (hindcast).
* __hindcast__ : Chaîne de caractères constante indiquant que ce fichier contient des données provenant de la partie prévision rétrospective du système SIPSCan, en opposition à la partie prévision (forecast).
* __MM__ : Le mois du début de la prévision [01, 02, 03, ..., 12]
* __YYYY__: L’année du début de la prévision [2012, 2013, ...]

## Spécification technique de la grille

Valeurs données aux paramètres de la grille latitude-longitude pour SPISCan.

| Paramètre | Valeur |
| ------ | ------ |
| ni | 145 |
| nj | 73 | 
| résolution | 2.5° |
| coordonnées du premier point de grille | 90° S  0° E | 

## Nomenclature des noms de fichiers 

NOTE: TOUTES LES HEURES SONT EN UTC.

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

Exemple de nom de fichier : cansips_forecast_raw_latlon2.5x2.5_HGT_ISBL_0500_2012-10_allmembers.grib2

Ce fichier de format GRIB2 (.grib2) a été généré par la composante prévision système SPISCan sur une grille latitude-longitude à 2.5 x 2.5 degrés de résolution. La prévision a été produite pour le mois d’octobre 2012 (2012-10). Ce fichier contient les moyennes mensuelles de tous les membres du système (allmembers) pour la variable « hauteur géopotentielle (HGT) » au niveau isobarique 500hpa (ISBL_0500).

## Niveaux

Ces données sont disponibles pour la surface et pour certains niveaux isobariques.

## Liste des variables

Attention : les tableaux ci-dessous ne sont pas à jour (à venir), certaines variables sont manquantes. N'hésitez pas à [nous contacter](mailto:ec.dps-client.ec@canada.ca) pour plus d'information.

* [Prévision pour l’échéance zéro](https://meteo.gc.ca/grib/CANSIPS/CANSIPS_latlon2.5x2.5_ALL_VAR_Lead-time-month-ZERO_hindcast_f.html)
* [Prévision pour les autres échéances](https://meteo.gc.ca/grib/CANSIPS/CANSIPS_latlon2.5x2.5_ALL_VAR_Lead-time-month-NONZERO_hindcast_f.html)

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : ec.dps-client.ec@canada.ca

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).
