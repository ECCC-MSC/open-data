[In English](readme_metnotes-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [MetNotes](readme_metnotes_fr.md) > MetNotes sur le Datamart du SMC

# Données MetNotes 

Cette page décrit les MetNotes [MetNotes](readme_metnotes_fr.md) en format GeoJSON disponibles sur le Datamart du SMC.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le Protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier GeoJSON.

Les données MetNotes se trouvent à l'adresse :

[https://hpfx.collab.science.gc.ca/{YYYYMMDD}/WXO-DD/metnotes](https://hpfx.collab.science.gc.ca/)

où :

* __YYYYMMDD__ : Année, mois et jour 

Un historique de plusieurs semaines est conservé dans ce répertoire.

## Nomenclature des noms de fichiers 

NOTE: TOUTES LES HEURES SONT EN UTC.

La nomenclature des noms des fichiers est la suivante :

`{YYYYMMDD}T{hhmmss.mss}Z_MSC_MetNotes.json`

où :

* __YYYYMMDD__ : Année, mois et jour de l'émission des données
* __T__ : Délimiteur temporel selon les normes ISO8601
* __hhmmss.mss__ : Heure, minute, seconde et milliseconde à laquelle les données sont émises
* __Z__ : Fuseau horaire (heure UTC)
* __MSC__ : Chaîne de caractères constante pour Meteorological Service of Canada, la source des données
* __MetNotes__ : Chaîne de caractères constante indiquant le modèle source : SPCOG (CIOPS en anglais)
* __json__ : Chaîne de caractères constante indiquant que le format est GeoJSON

Exemple :

* 20220207T000000.123Z_MSC_MetNotes.json

__Note__ : L'utilisation des millisecondes est requise pour assurer l'unicité des notes émises 

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).
