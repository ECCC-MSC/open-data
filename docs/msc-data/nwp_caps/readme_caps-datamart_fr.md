[In English](readme_caps-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [SCPA](readme_caps_fr.md) > Données GRIB2 de SCPA sur le Datamart du SMC

# Données GRIB2 du Système canadien de prévision de l'Arctique (SCPA)

Cette page décrit les données du [Système canadien de prévision de l'Arctique (SCPA)](./readme_caps_fr.md). 

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTP. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier GRIB2.

Les données sont accessibles aux adresses suivantes :

* [https://dd.alpha.meteo.gc.ca/yopp/model_caps/grib2/polar_stereographic/{YYYY}}/{MM}/{DD}/{HH}/{Phhh}](https://dd.alpha.meteo.gc.ca/yopp/model_caps/grib2/polar_stereographic/)

où :

* __Phhh__ : P est un caractère constant. hhh est l'heure de prévision [000, 001, 002, ..., 048]
* __HH__ : Heure en UTC du début de la simulation [00, 12]
* __DD__ : Le jour du début de la prévision [01, 02, 03, ..., 31]
* __MM__ : Le mois du début de la prévision [01, 02, 03, ..., 12]
* __YYYY__: L’année du début de la prévision [2018, 2019, ...]

Un historique de 2 ans est conservé dans ce répertoire.

## Nomenclature des noms de fichiers 

NOTE : TOUTES LES HEURES SONT EN UTC.

Les fichiers ont la nomenclature suivante :

* CMC_caps_Variable_LevelType_Level_ProjectionResolution_YYYYMMDDHH_Phhh.grib2

où :

* __CMC__ : Chaîne de caractères constante indiquant que le Centre météorologique canadien (CMC) émet les prévisions
* __caps__ : Chaîne de caractères constante indiquant le système de prévision qui génère les données (CAPS)
* __Variable__ : Nom de la variable contenue dans le fichier
* __TypedeNiveau__ : Type de niveau : sfc ou depth
* __Niveau__ : Valeur du niveau
* __Projection__ : Projection cartographique, prend juste une valeur : ps pour polaire stéréographique
* __Résolution__ : prend juste une valeur: 3km
* __YYYYMMDD__ : Année, mois et jour du début de la prévision
* __HH__ : Heure en UTC du début de la simulation [00, 12]
* __Phhh__ : P est un caractère constant. hhh est l'heure de prévision [000, 001, 002, ..., 048]
* __grib2__ : Chaîne de caractères constante indiquant le format GRIB2

Exemples de noms de fichier : 

* CMC_caps_HGT_ISBL_0500_ps3km_2018011200_P024.grib2

Le fichier a été créé par le CMC et contient une prévision du SCPA. Il contient l'altitude géopotentielle (HGT), au niveau isobarique 500 mb (ISBL_0500), sur une grille polaire stéréographique à une résolution de 3 km (ps3km). Il débute le 12 janvier 2018 à 00Z (2018011200). Il contient l?heure de prévision 24 (P024) en format GRIB2 (.grib2).

## Niveaux

Ces données sont disponibles pour la surface et pour certains niveaux isobariques.

## Liste des variables

Pour le moment, les variables sont les mêmes que celles produites par le SHRPD.

Ainsi, pour les variables du modèle SCPA à 000h d'échéance, consultez la liste ici :
* https://meteo.gc.ca/grib/HRDPS_HR/HRDPS_nat_ps2p5km_P000_deterministic_f.html

Concernant les variables aux heures suivantes, consultez la liste ici :
* https://meteo.gc.ca/grib/HRDPS_HR/HRDPS_ps2p5km_PNONZERO_deterministic_f.html

La couverture verticale des champs tridimensionnels peut atteindre jusqu'à 28 niveaux isobariques (hPa) :
1015, 1000, 0985, 0970, 0950, 0925, 0900, 0850, 0800, 0750, 0700, 0650, 0600, 0550, 0500, 0450, 0400, 0350, 0300, 0275, 0250, 0225, 0200, 0175, 0150, 0100, 0050.

Certains champs ont une couverture verticale limitée à 4 niveaux isobariques (ex: vorticité absolue) :
0850, 0700, 0500, 0250.

Finalement, d'autres types de niveaux pourraient être applicables à certains champs :

* Surface
* Hauteur fixe au-dessus du sol
* Profondeur fixe sous le sol
* Épaisseur entre niveaux isobariques
* Sommet théorique de l'atmosphère
* Colonne atmosphérique entière

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).
