[In English](readme_geps-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [SGPE](readme_geps_fr.md) > SGPE sur le Datamart du SMC

# Données GRIB2 du Système global de prévision d'ensemble (SGPE)

Cette page décrit les données du [Système global de prévision d'ensemble](readme_geps_fr.md) disponibles en format GRIB2.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le Protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTP. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier GRIB2. Nous vous recommandons d’automatiser le téléchargement en le scriptant avec wget (lien externe, anglais) ou un programme équivalent. Pour plus d’information sur wget, consultez les notes d’utilisation.

Les données sont accessibles aux adresses suivantes :

* https://dd.meteo.gc.ca/ensemble/geps/grib2/TYPE/HH/hhh/

où :

* __TYPE__ : Chaîne de caractères indiquant les membres individuels issus des sorties directes de modèle (pas de traitement) ou les produits probabilistes créés à partir des membres individuels [raw, products]
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

* CMC_geps-raw_Variable_TypedeNiveau_Niveau_latlonResolution_YYYYMMDDHH_Phhh_allmbrs.grib2
* CMC_geps-prob_Variable_TypedeNiveau_Niveau_latlonResolution_YYYYMMDDHH_Phhh_all-products.grib2

où :

* __CMC_geps__ : Chaîne de caractères constante indiquant que le Centre météorologique canadien (CMC) émet les prévisions, le modèle (geps : Global Ensemble Prediction System).
* __raw__ : sorties brutes des membres individuels 
* __prob__ : produits probabilistes générés à partir de tous les membres
* __Resolution__ : Chaîne de caractères constante indiquant la résolution des données (0p5x0p5).
* __Variable__ : Type de variable contenu dans le fichier. Pour voir la liste complète, consultez la section « Description des variables ».
* __TypedeNiveau__ : Type de niveau. Pour voir la liste complète, consultez la section « Description des variables ».
* __Niveau__ : Valeur du niveau. Pour voir la liste complète, consultez la section « Description des variables ».
* __YYYYMMDD__ : Année, mois et jour du début de la prévision.
* __HH__ : Heure UTC de la passe [00, 12].
* __Phhh__ : « P » est un caractère constant. « hhh » représente l’heure de prévision [000, 003, …, 192, 198, 204, ..., 378, 384], ou [000, 003, …, 192, 198, 204, ..., 762, 768] chaque jeudi à 000UTC.
* __allmbrs__ : Chaîne de caractères constante indiquant que tous les membres sont inclus dans le fichier.
* __all-products__ : Indique que tous les produits probabilistes pour cette variable sont regroupés dans ce fichier
* __grib2__ : Chaîne de caractères constante indiquant que le format est GRIB2.

Exemple de nom de fichier :

CMC_geps-raw_UGRD_ISBL_0925_latlon0p5x0p5_2010090100_P078_allmbrs.grib2

Les données dans le fichier débutent le 1 septembre 2010 à 00Z (2010090100). Il a été créé par le CMC et contient les données brutes du Système global de prévision d'ensemble (CMC_geps-raw). Il contient les composantes du vent selon U (UGRD), au niveau isobarique 925 mb (ISBL_0925), à l’heure de prévision 78 (P078), pour tous les membres de l’ensemble (allmbrs), le tout en format GRIB2 (.grib2).

## Liste des variables

Les variables pour les produits d'ensemble disponibles dans les fichiers GRIB2 sont décrites ci-dessous. Pour chaque variable, la définition, la période et la fréquence de disponibilité sont mentionnées.

Pour les membres individuels:

* __AFRAIN_SFC_0__              : Accumulation de pluie verglaçante : 0-384h à chaque 3h
* __AICEP_SFC_0__               : Accumulation de grésil : 0-384h à chaque 3h
* __APCP_SFC_0__                : Accumulation de précipitations totales : 0-384h à chaque 3h
* __ARAIN_SFC_0__               : Accumulation de pluie : 0-384h à chaque 3h
* __ASNOW_SFC_0__               : Accumulation de neige : 0-384h à chaque 3h
* __CAPE_SFC_0__                : Énergie potentielle convective disponible : 0-384h à chaque 3h
* __CIN_SFC_0__                 : Énergie d'inhibition de la convection : 0-384h à chaque 3h
* __DLWRF_SFC_0__               : Flux radiatif d'ondes longues descendant : 0-384h à chaque 3h
* __DSWRF_SFC_0__               : Flux radiatif d'ondes courtes descendant  : 0-384h à chaque 3h
* __HGT_ISBL_XXXX__             : Hauteur du géopotentiel à XXXX hPa : 0-384h à chaque 3h
* __HGT_SFC_0__                 : Hauteur du géopotentiel à la surface : 0-384h à chaque 3h
* __ICETK_SFC_0__               : Épaisseur de la glace : 0-384h à chaque 3h
* __LHTFL_SFC_0__               : Flux de chaleur latente à la surface : 0-384h à chaque 3h
* __OLR_NTAT_0__                : Flux a ondes longues sortant au sommet de l'atmosphère : 0-384h à chaque 3h
* __PRES_SFC_0__                : Pression à la surface : 0-384h à chaque 3h
* __PRMSL_MSL_0__               : Pression au niveau de la mer : 0-384h à chaque 3h
* __PWAT_EATM_0__               : Eau précipitable sur la colonne entière : 0-384h à chaque 3h
* __RH_ISBL_XXXX__              : Humidité relative à XXXX hPa : 0-384h à chaque 3h
* __RH_TGL_2m__                 : Humidité relative 2m au-dessus du sol : 0-384h à chaque 3h
* __SHTFL_SFC_0__               : Flux de chaleur latente à la surface : 0-384h à chaque 3h
* __SNOD_SFC_0__                : Épaisseur de neige à la surface : 0-384h à chaque 3h
* __SWAT_DBLL_10cm__            : Contenu d'eau volumétrique au sol 0-10cm sous la surface : 0-384h à chaque 3h
* __VSOILM_DBLL_10cm__          : Contenu d'eau volumétrique au sol 0-10cm sous la surface : 0-384h à chaque 3h
* __TCDC_SFC_0__                : Couverture nuageuse : 0-384h à chaque 3h
* __TMAX_TGL_2m__               : Température maximale 2m au-dessus du sol : 0-384h à chaque 3h
* __TMIN_TGL_2m__               : Température minimale 2m au-dessus du sol : 0-384h à chaque 3h
* __TMP_ISBL_XXXX__             : Température à XXXX hPa : 0-384h à chaque 3h
* __TMP_TGL_2m__                : Température 2m au-dessus du sol : 0-384h à chaque 3h
* __TSOIL_DBLL_10cm__           : Température du sol 0-10cm sous la surface : 0-384h à chaque 3h
* __UGRD_ISBL_XXXX__            : Composante U du vent à XXXX hPa : 0-384h à chaque 3h
* __UGRD_TGL_10m__              : Composante U du vent 10m au-dessus du sol : 0-384h à chaque 3h
* __ULWRF_SFC_0__               : Flux d'ondes longues vers le haut à la surface : 0-384h à chaque 3h
* __USWRF_SFC_0__               : Flux d'ondes courtes vers le haut à la surface : 0-384h à chaque 3h
* __VGRD_ISBL_XXXX__            : Composante V du vent à XXXX hPa : 0-384h à chaque 3h
* __VGRD_TGL_10m__              : Composante V du vent 10m au-dessus du sol : 0-384h à chaque 3h
* __VVEL_ISBL_XXXX__            : Mouvement vertical at XXXX hPa : 0-384h à chaque 3h
* __WEASD_SFC_0__               : Neige en équivalent eau à la surface : 0-384h à chaque 3h

Pour les produits probabilistes:

* __FPRATE-Accum-12h_SFC_0__    : Pluie verglaçante accumulée sur une période de 12h : 12h-384h à chaque 12h
* __FPRATE-Accum-24h_SFC_0__    : Pluie verglaçante accumulée sur une période de 24h : 24h-384h à chaque 24h
* __HEATX-Max-24h_TGL_2m__      : Humidex 2m au-dessus du sol - Maximum sur une période de 24h : 24h-384h à chaque 24h
* __HEATX_TGL_2m__              : Humidex 2m au-dessus du sol : 3-384h à chaque 3h
* __HGT_ISBL_0500__               : Hauteur du géopotentiel 500 hPa : 3-384h à chaque 12h
* __IPRATE-Accum-12h_SFC_0__    : Grésil accumulé sur une période de 12h : 12h-384h à chaque 12h
* __IPRATE-Accum-24h_SFC_0__    : Grésil accumulé sur une période de 24h : 24h-384h à chaque 24h
* __PRMSL_MSL_0__              : Pression au niveau de la mer : 3-384h à chaque 12h
* __RATE-Accum-12h_SFC_0__    : Pluie accumulée sur une période de 12h : 12h-384h à chaque 12h
* __RATE-Accum-24h_SFC_0__    : Pluie accumulée sur une période de 24h : 24h-384h à chaque 24h
* __PRATE-Accum-12h_SFC_0__    : Neige (équivalent en eau) accumulée sur une période de 12h : 12h-384h à chaque 12h
* __SPRATE-Accum-24h_SFC_0__    : Neige (équivalent en eau) accumulée sur une période de 24h : 24h-384h à chaque 24h
* __TCDC_SFC_0__                : Couverture nuageuse : 3-384h à chaque 3h
* __TEMP-Max-24h_TGL_2m__       : Température 2m au-dessus du sol - Maximum sur une période de 24h : 24h-384h à chaque 24h
* __TEMP-Min-24h_TGL_2m__       : Température 2m au-dessus du sol - Minimum sur une période de 24h : 24h-384h à chaque 24h
* __TEMP_TGL_2m__               : Température 2m au-dessus du sol : 3-384h à chaque 3h
* __TPRATE-Accum-120h_SFC_0__   : Précipitations totales accumulées sur une période de 120h : 120h-384h à chaque 120h
* __TPRATE-Accum-12h_SFC_0__    : Précipitations totales accumulées sur une période de 12h : 12h-384h à chaque 12h
* __TPRATE-Accum-24h_SFC_0__    : Précipitations totales accumulées sur une période de 24h : 24h-384h à chaque 24h
* __TPRATE-Accum-48h_SFC_0__    : Précipitations totales accumulées sur une période de 48h : 48h-384h à chaque 48h
* __TPRATE-Accum-72h_SFC_0__    : Précipitations totales accumulées sur une période de 72h : 72h-384h à chaque 72h
* __TPRATE-Accum-96h_SFC_0__    : Précipitations totales accumulées sur une période de 96h : 96h-384h à chaque 96h
* __WCF-Min-24h_TGL_2m__        : Facteur éolien 2m au-dessus du sol - Minimum sur une période de 24h : 24h-384h à chaque 24h
* __WCF_TGL_2m__                : Facteur éolien 2m au-dessus du sol : 3-384h à chaque 3h
* __WIND-Max-12h_TGL_10m__      : Vitesse du vent 10m au-dessus du sol - Maximum sur une période de 12h : 12h-384h à chaque 12h
* __WIND_TGL_10m__              : Vitesse du vent 10m au-dessus du sol : 3-384h à chaque 3h

Les fichiers contiennent des produits de probabilité par comptage de membre au-dessus ou au-dessous de différents seuils, des percentiles , moyennes, médianes et écarts-types. Notez que les produits et les seuils sont définis dans la méta-information des fichiers.

Par exemple, pour l’accumulation de précipitation totale sur une période de 12h (TPRATE-Accum-12h), on retrouve les produits suivants :

* Probabilité au-dessus de 2,5,  5,  10 , 15,  20,  25,  30, 40, 50, 75, 100 et 150 mm
* Minimum (percentile 0), maximum (100e percentile), médiane (50e percentile), écart-type et moyenne
* Percentiles additionnels: 10,25,75 et 90 

Note: Une [liste en format XML](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_geps/geps_element.xml) contenant l'information pour toutes les variables, y compris les descriptions et les unités, en français et en anglais est disponible.

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).




























