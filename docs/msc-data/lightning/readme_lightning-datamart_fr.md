[In English](readme_lightning-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [Foudre](readme_lightning_fr.md) > Données de foudre sur le Datamart du SMC

# Données de densité de foudre

Cette page décrit les données de densité de [foudre](readme_lightning_fr.md) en format GeoTIFF disponibles sur le Datamart du SMC.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le Protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier GeoTIFF.

Les données de foudre se trouvent à l'adresse :

[https://hpfx.collab.science.gc.ca/{YYYYMMDD}/WXO-DD/lightning](https://hpfx.collab.science.gc.ca/)

où :

* __YYYYMMDD__ : Année, mois et jour 

Un historique de plusieurs semaines est conservé dans ce répertoire.

## Nomenclature des noms de fichiers 

La nomenclature des noms des fichiers est la suivante :

`{YYYYMMDD}T{HHmm}Z_MSC_Lightning_2.5km.tif`

où :

* __YYYYMMDD__ : Année, mois et jour de l'émission des données
* __T__ : Délimiteur temporel selon les normes ISO8601
* __HHmm__ : Heure et  minute à laquelle les données sont émises
* __Z__ : Fuseau horaire (heure UTC)
* __MSC__ : Chaîne de caractères constante pour Meteorological Service of Canada, la source des données
* __Lightning__ : Chaîne de caractères constante indiquant que les données contiennent une densité d'éclairs observés (km-2.min-1)
* __2.5km__ : Chaîne de caractères constante indiquant la résolution horizontale des données
* __tif__ : Chaîne de caractères constante indiquant que le format est GeoTIFF

Exemple:

* 20220322T2350Z_MSC_Lightning_2.5km.tif

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).
