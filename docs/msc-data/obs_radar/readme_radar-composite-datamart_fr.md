[In English](readme_radar-composite-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [Données et produits radar](readme_radar_fr.md) > Composite radar sur le Datamart du SMC

# Composite radar nord-américaine

La composite est calculée sur le domaine nord-américain avec une résolution spatiale horizontale de 1 km. Cette mosaïque inclut donc tous les radars canadiens et américains disponibles dans le réseau et qui peuvent atteindre un maximum de 200 radars contributeurs.

Afin de mieux représenter les précipitations pendant les différentes saisons, cette composite est disponible en mm/h pour représenter la pluie et en cm/h pour représenter la neige. Pour les deux types de précipitations (pluie et neige), nous utilisons deux relations mathématiques différentes pour convertir la réflectivité en taux de précipitations (mm/h pour pluie et cm/h pour neige).

Il s’agit d’une mosaïque basée sur le produit EQPDP (estimation quantitative des précipitations à double polarisation, DPQPE en anglais) qui est disponible uniquement pour les radars en bande S. Pour les radars américains Nexrad, ECCC utilise le produit le plus similaire du service météorologique américain (NOAA). Ce produit est la réflectivité radar, qui est convertie en taux de précipitation en utilisant les mêmes formules que celles utilisées pour les radars canadiens.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le Protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier GeoTIFF.

Les données sont disponibles à l'adresse :

[https://hpfx.collab.science.gc.ca/{YYYYMMDD}/radar/composite](https://hpfx.collab.science.gc.ca/)

où :

* __YYYYMMDD__ : Année, mois et jour

__Notes__: 

* Une [liste des sites radar](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_radar/radars_list.pdf) est disponible. Cette liste sera mise à jour régulièrement.

## Spécifications techniques

Voici davantage de détails sur ces deux produits utilisés pour générer la composite:

* __Produit EQPDP__ : Il s'agit d'une représentation bidimensionnelle du taux de précipitation estimé à partir du balayage radar le plus bas (angle d'élévation de 0,4 degré pour la plupart des radars en bande S). Ainsi, le taux de précipitation estimé est le plus proche possible de la surface de la Terre. Le produit EQPDP est basé, entre autres, sur une série d'étapes de traitement polarimétrique (contrôle de qualité basé sur la technologie de double polarisation) pour éliminer les artefacts non météorologiques des données brutes (balayages volumétriques). Il est fourni en mm/h pour la pluie et en cm/h pour la neige. Ce produit est calculé avec une portée de couverture maximale de 240 km.

* __Produit américain__ : ECCC utilise des mosaïques de réflectivité de base provenant du système Multi-Radar-Multi-Sensor (MRMS) de la NOAA (National Oceanic and Atmospheric Administration), avec un contrôle de qualité pour éliminer les échos de sol et les échos non météorologiques. Ces mosaïques couvrent l'ensemble des États-Unis contigus, ainsi que les domaines de l'Alaska et d'Hawaï. Ce produit est calculé avec une portée maximale de 460 km pour la plupart des radars américains. Nous avons adapté cette composition à nos besoins spécifiques afin de nous assurer qu'elle est cohérente et compatible avec les données radar canadiennes, garantissant ainsi une intégration harmonieuse entre les deux réseaux.

## Nomenclature des noms de fichiers 

Les fichiers suivent la nomenclature suivante :

`{YYYYMMDD}T{HHmm}Z_MSC_Radar-Composite_{UNIT}_{res}.tif`

où :

* __YYYYMMDD__ : Année, mois et jour de l'émission des données
* __T__ : Délimiteur temporel selon les normes ISO8601
* __HHmm__ : Heure et  minute à laquelle les données sont émises
* __Z__ : Fuseau horaire (heure UTC)
* __MSC__ : Chaîne de caractères constante pour Meteorological Service of Canada, la source des données
* __Radar-Composite__ : Chaîne de caractères constante indiquant que les données contiennent la composite radar nord-américaine
* __UNIT__ : Chaîne de caractères indiquant l'unité [MMHR,CMHR] selon le type de précipitation (pluie, neige)
* __res__ : résolution horizontale [1km]
* __tif__ : Chaîne de caractères constante indiquant que le format est GeoTIFF

Exemple:

* 20240214T1550Z_MSC_Radar-Composite_MMHR_1km.tif

## Support

Pour toute question relative à ces données, merci de [nous contacter](https://weather.gc.ca/mainmenu/contact_us_f.html).

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).
