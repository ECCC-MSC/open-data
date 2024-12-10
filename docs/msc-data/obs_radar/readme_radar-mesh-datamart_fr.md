[In English](readme_radar-mesh-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [Données et produits radar](readme_radar_fr.md) > Produit DMG sur le Datamart du SMC

# Produit radar de diamètre maximal de grêle (DMG)

Le produit DMG (Diamètre Maximal de Grêle) est déterminé comme suit : Le volume de la réflectivité radar à un emplacement de pixel donné est intégré verticalement depuis le balayage à l'élévation la plus basse jusqu'à la hauteur du niveau de température de -20°C. Le niveau de température est déterminé par le [Système à haute résolution de prévision déterministe (SHRPD)](../nwp_hrdps/readme_hrdps_fr.md). La réflectivité pondérée est traitée à travers plusieurs étapes intermédiaires et une relation empirique est utilisée pour estimer les tailles maximales de grêle. Les estimations résultantes de la taille de la grêle sont affichées sous forme de champ bidimensionnel ou de PPI (Plan Position Indicator). L'unité du produit DMG est en millimètres. 

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le Protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier GeoTIFF.

Les données sont disponibles à l'adresse :

[https://hpfx.collab.science.gc.ca/{YYYYMMDD}/radar/mesh/{RADAR_ID}](https://hpfx.collab.science.gc.ca/)

où :

* __YYYYMMDD__ : Année, mois et jour
* __RADAR_ID__ : Identifiant du radar, code de 5 lettres en lettres majuscules (voir la liste ci-dessous).

__Notes__: 

* Une [liste des sites radar](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_radar/radars_list.pdf) est disponible. Cette liste sera mise à jour régulièrement.

## Nomenclature des noms de fichiers

Les fichiers suivent la nomenclature suivante :

`{YYYYMMDD}T{HHmm}Z_MSC_Radar-MESH_{RADAR_ID}_{res}.tif`

où :

* __YYYYMMDD__ : Année, mois et jour de l'émission des données
* __T__ : Délimiteur temporel selon les normes ISO8601
* __HHmm__ : Heure et  minute à laquelle les données sont émises
* __Z__ : Fuseau horaire (heure UTC)
* __MSC__ : Chaîne de caractères constante pour Meteorological Service of Canada, la source des données
* __Radar-MESH__ : Chaîne de caractères constante indiquant que les données contiennent le produit DMG (MESH en anglais)
* __RADAR_ID__ : Code de 5 lettres majuscules représentant l'identifiant du radar
* __res__ : résolution horizontale [1km]
* __tif__ : Chaîne de caractères constante indiquant que le format est GeoTIFF

Exemple:

* 20240110T0030Z_MSC_Radar-MESH_CASBV_1km.tif

## Support

Pour toute question relative à ces données, [merci de nous contacter](https://meteo.gc.ca/mainmenu/contact_us_f.html)

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).
