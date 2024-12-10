[In English](readme_radar-sptp-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [Données et produits radar](readme_radar_fr.md) > SPTP sur le Datamart du SMC

# Produit radar de type de précipitation à la surface (SPTP)

Ce produit est un composite à une résolution de 1km sur le domaine nord-américain, qui, pour les zones avec une couverture radar, peut distinguer l'occurrence, le type de précipitation et son niveau d'intensité. Ce produit utilise en entrée deux composites radar à 1km, soit un composite nord-américain nettoyé à l'aide de la technologie de double polarisation, un autre composite radar de classification des particules (précipitations) ainsi que la température de surface provenant du [Système à haute résolution de prévision déterministe (SHRPD)](../nwp_hrdps/readme_hrdps_fr.md). Le produit est généré toutes les 6 minutes.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le Protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier GeoTIFF.

Les données sont disponibles à l'adresse :

[https://hpfx.collab.science.gc.ca/{YYYYMMDD}/radar/sptp](https://hpfx.collab.science.gc.ca/)

où :

* __YYYYMMDD__ : Année, mois et jour

__Notes__: 

* Une [liste des sites radar](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_radar/radars_list.pdf) est disponible. Cette liste sera mise à jour régulièrement.

## Spécifications techniques

Les valeurs du type de précipitation à la surface sont encodées selon le tableau suivant :

| Type de précipitation | Valeur |
| ------ | ------ |
| Neige légère | 110 |
| Neige modérée | 120 | 
| Neige forte | 130 |
| Mélange pluie/neige faible | 210 |
| Mélange pluie/neige modéré | 220 |
| Mélange pluie/neige intense | 230 |
| Pluie légère | 310 | 
| Pluie modérée | 320 | 
| Pluie forte | 330 |
| Grêle ou pluie | 410 |
| Pluie verglaçante légère | 510 |   
| Pluie verglaçante modérée/intense | 520 |

## Nomenclature des noms de fichiers

Les fichiers suivent la nomenclature suivante :

`{YYYYMMDD}T{HHmm}Z_MSC_Radar-Composite_SfcPrecipType_{res}.tif`

où :

* __YYYYMMDD__ : Année, mois et jour de l'émission des données
* __T__ : Délimiteur temporel selon les normes ISO8601
* __HHmm__ : Heure et  minute à laquelle les données sont émises
* __Z__ : Fuseau horaire (heure UTC)
* __MSC__ : Chaîne de caractères constante pour Meteorological Service of Canada, la source des données
* __Radar-Composite__ : Chaîne de caractères constante indiquant que les données contiennent un produit radar qui un composite
* __SfcPrecipType__ : Chaîne de caractères constante indiquant que les données contiennent le produit de type de précipitation à la surface (SPTP)
* __res__ : résolution horizontale [1km]
* __tif__ : Chaîne de caractères constante indiquant que le format est GeoTIFF

Exemple:

* 20240214T1550Z_MSC_Radar-Composite_SfcPrecipType_1km.tif

## Support

Pour toute question relative à ces données, [merci de nous contacter](https://meteo.gc.ca/mainmenu/contact_us_f.html)

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).
