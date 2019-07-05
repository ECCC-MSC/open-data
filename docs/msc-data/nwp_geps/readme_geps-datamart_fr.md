[In English](readme_geps-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données ouvertes publiques du SMC](../readme_fr.md) > SGPE sur le Datamart du SMC

# Données GRIB2 du Système global de prévision d'ensemble (SGPE)

Cette page décrit les données du [Système global de prévision d'ensemble](readme_geps_fr.md) disponibles en format GRIB2.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le Protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTP. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier GRIB2. Nous vous recommandons d’automatiser le téléchargement en le scriptant avec wget (lien externe, anglais) ou un programme équivalent. Pour plus d’information sur wget, consultez les notes d’utilisation.

Les données sont accessibles aux adresses suivantes :

* https://dd.meteo.gc.ca/ensemble/geps/grib2/raw/HH/hhh/

où :

* __raw__ : Chaîne de caractères constante indiquant les sorties brutes du modèle
* __HH__ : Heure UTC du début de la passe du modèle [00, 12]
* __hhh__ : Heure de prévision [000, 003, 006, ..., 192, 198, 204, ..., 378, 384] et [000, 003, …, 192, 198, 204, ..., 762, 768] chaque jeudi à 000UTC

## Spécification technique de la grille

Ce tableau décrit des paramètres de la grille latitude-longitude sur laquelle les variables en format GRIB sont disponibles.

| Paramètre de la grille                                          | Valeur du paramètre      |
|-----------------------------------------------------------------|--------------------------|
| ni                                                              | 720 points               |
| nj                                                              | 361 points               |
| résolution                                                      | 0,5°                     |
| coordonnées du premier point de grille                          | 90° S  000° E            |

## Nomenclature des noms de fichiers 

NOTE : TOUTES LES HEURES SONT EN UTC.

Les fichiers ont la nomenclature suivante :

CMC_geps-raw_Variable_LevelType_Level_latlonResolution_YYYYMMDDHH_Phhh_allmbrs.grib2

où :

* __CMC_geps-raw__ : Chaîne de caractères constante indiquant que le Centre météorologique canadien (CMC) émet les prévisions, le modèle (geps : Global Ensemble Prediction System) et le type de données (brutes, raw).
* __Résolution__ : Chaîne de caractères constante indiquant la résolution des données (0p5x0p5).
* __Variable__ : Type de variable contenu dans le fichier. Pour voir la liste complète, consultez la section « Description des variables ».
* __TypedeNiveau__ : Type de niveau. Pour voir la liste complète, consultez la section « Description des variables ».
* __Niveau__ : Valeur du niveau. Pour voir la liste complète, consultez la section « Description des variables ».
* __YYYYMMDD__ : Année, mois et jour du début de la prévision.
* __HH__ : Heure UTC de la passe [00, 12].
* __Phhh__ : « P » est un caractère constant. « hhh » représente l’heure de prévision [000, 003, …, 192, 198, 204, ..., 378, 384], ou [000, 003, …, 192, 198, 204, ..., 762, 768] chaque jeudi à 000UTC.
* __allmbrs__ : Chaîne de caractères constante indiquant que tous les membres sont inclus dans le fichier.
* __grib2__ : Chaîne de caractères constante indiquant que le format est GRIB2.

Exemple de nom de fichier :

CMC_geps-raw_UGRD_ISBL_0925_latlon0p5x0p5_2010090100_P078_allmbrs.grib2

Les données dans le fichier débutent le 1 septembre 2010 à 00Z (2010090100). Il a été créé par le CMC et contient les données brutes du Système global de prévision d'ensemble (CMC_geps-raw). Il contient les composantes du vent selon U (UGRD), au niveau isobarique 925 mb (ISBL_0925), à l’heure de prévision 78 (P078), pour tous les membres de l’ensemble (allmbrs), le tout en format GRIB2 (.grib2).

## Liste des variables

Attention : les tableaux ci-dessous ne sont pas à jour (à venir), certaines variables sont manquantes. N'hésitez pas à [nous contacter](mailto:ec.dps-client.ec@canada.ca) pour plus d'information.

| Membre des ensembles                    | Heure de prévision                      |
|-----------------------------------------|-----------------------------------------|
| Membre contrôle (membre 0)              | [Prévisions à 0h](https://meteo.gc.ca/grib/GEPS_HR/GEPS_latlon0p5x0p5_P000_MBRZERO_f.html) ; [Autres heures de prévisions](https://meteo.gc.ca/grib/GEPS_HR/GEPS_latlon0p5x0p5_PNONZERO_MBRZERO_f.html) |
| Membres perturbés                       | [Prévisions à 0h](https://meteo.gc.ca/grib/GEPS_HR/GEPS_latlon0p5x0p5_P000_MBRNONZERO_f.html) ; [Autres heures de prévisions](https://meteo.gc.ca/grib/GEPS_HR/GEPS_latlon0p5x0p5_PNONZERO_MBRNONZERO_f.html)|       

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : ec.dps-client.ec@canada.ca

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).




























