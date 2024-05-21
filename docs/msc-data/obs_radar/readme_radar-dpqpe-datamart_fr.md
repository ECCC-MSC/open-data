[In English](readme_radar-dpqpe-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [Données EQPDP)](readme_radar_fr.md) > Estimation quantitative des précipitations à double polarisation (EQPDP) sur le Datamart du SMC

# Imagerie radar

Cette page décrit les données d'Estimation quantitative des précipitations à double polarisation (EQPDP)en format GeoTIFF disponibles sur le Datamart du SMC.

Ce produit est exclusivement disponible pour tous les radars canadiens en bande S et offre une représentation bidimensionnelle du taux de précipitation, en s'appuyant sur les données de balayage à une élévation de 0.4 degré des radars en bande S. Par conséquent, il fournit une estimation du taux de précipitation aussi proche que possible de la surface de la Terre.

Le produit EQPDP est construit, entre autres, sur la base d'une série d'étapes de traitement polarimétrique, qui servent principalement de mesures de contrôle qualité pour éliminer les artefacts non météorologiques des données brutes. De plus, il existe une option hybride dans le produit EQPDP conçue pour combler les lacunes dans les données de précipitations résultant du signal radar ou du traitement des données polarimétriques. Cette option hybride utilise les deux balayages d'élévation supérieurs adjacents au-dessus de 0.4 degré pour aider à combler ces lacunes de données.

Les taux de précipitation sont calculés en équivalent liquide en MM/HR et convertis en CM/HR pour les chutes de neige sur une portée maximale de couverture de 240 km. 

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le Protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier GeoTIFF.

Les images radar se trouvent à l'adresse :

[https://hpfx.collab.science.gc.ca/{YYYMMDD}/radar/dpqpe/{RADAR_ID}](https://hpfx.collab.science.gc.ca/)

où :

* __YYYYMMDD__ : Année, mois et jour
* __RADAR_ID__ : Identifiant du radar, code de 5 lettres en lettres majuscules (voir la liste ci-dessous).

Un historique de plusieurs semaines est conservé dans ce répertoire.

__Notes__: 

* Une [liste des sites radar](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_radar/radars_list.pdf) est disponible. Cette liste sera mise à jour régulièrement.

## Nomenclature des noms de fichiers 

Les fichiers ont la nomenclature suivante:

`{YYYYMMDD}T{HHmm}Z_MSC_Radar-DPQPE_{RADAR_ID}_{SCALE}_{res}.hdf5`

où :

* __YYYYMMDD__ : Année, mois et jour de l'émission des données
* __T__ : Délimiteur temporel selon les normes ISO8601
* __HHmm__ : Heure et  minute à laquelle les données sont émises
* __Z__ : Fuseau horaire (heure UTC)
* __MSC__ : Chaîne de caractères constante pour Meteorological Service of Canada, la source des données
* __Radar-DPQPE__ : Chaîne de caractères constante indiquant que les données contiennent le produit DPQPE
* __RADAR_ID__ : Code de 5 lettres majuscules représentant l'identifiant du radar
* __SCALE__ : Échelle de conversion utilisée pour mesurer les précipitations, peut être en millimètre par heure (MMHR) ou en centimètre par heure (CMHR)
* __res__ : Résolution horizontale [1km]
* __hdf5__ : Chaîne de caractères constante indiquant que le format est HDF5

Exemple:

* 20240429T0030Z_MSC_Radar-DPQPE_CASFM_CMHR_1km.tif

## Support

Pour toute question relative à ces données, merci de [nous contacter](https://weather.gc.ca/mainmenu/contact_us_f.html).

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).
