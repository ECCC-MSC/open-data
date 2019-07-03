[In English](readme_reps-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données ouvertes publiques du SMC](../readme_fr.md) > SRPE sur le Datamart du SMC

# Données GRIB2 du Système régional de prévision d'ensemble (SRPE)

Cette page décrit les données du [système régional de prévision d'ensemble](readme_reps_fr.md) disponibles en format GRIB2.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTP. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier GRIB2. Nous vous recommandons d’automatiser le téléchargement en le scriptant avec wget (lien externe, anglais) ou un programme équivalent. Pour plus d’information sur wget, consultez les notes d’utilisation.

Les données sont accessibles aux adresses suivantes :

https://dd.meteo.gc.ca/ensemble/reps/15km/grib2/EnsembleTypeDonnee/HH/hhh

où :
* __EnsembleTypeDonnee__ : Peut être "raw" pour les sorties brutes des membres individuels ou "prob" pour les produits probabilistes générés à partir de tous les membres
* __HH__ : Heure de la passe du modèle en TU
* __hhh__ : Heure de la prévision

## Spécification technique de la grille

![](http://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_reps/grille_reps.png)

Valeurs données aux paramètres de la grille polaire stéréographique à haute résolution.

| Paramètre | Valeur |
| ------ | ------ |
| ni | 600 |
| nj | 610 | 
| résolution à 60° N | 10km |
| coordonnées du premier point de grille | 19.3206° N ; 141.5411° W | 
| orientation de la grille (par rapport à l’axe des j) | -110.0° | 

## Nomenclature des noms de fichiers 

NOTE : TOUTES LES HEURES SONT EN UTC.

Les fichiers ont la nomenclature suivante :

CMC-reps-srpe-EnsembleTypeDonnee_ChampMeteo_TypeNiveau_Niveau_Résolution_YYYYMMDDHH_Phhh_Contenu.grib2

où :

* __EnsembleTypeDonnee__ : Peut être "raw" pour les sorties brutes des membres individuels ou "prob" pour les produits probabilistes générés à partir de tous les membres
* __ChampMeteo__ : Nom du champ météo (ex: WIND pour les vents) 
* __TypeNiveau__ : Description du type du niveau (ex: TGL pour au-dessus du niveau du sol)
* __Niveau__ : Valeur du niveau (ex: 10m pour 10 mètres)
* __Résolution__: Résolution de la grille (ex: ps15km)
* __YYYYMMDDHH__: Date de la passe du modèle en TU
* __Phhh__ : Heure de la prévision
* __Contenu__ : Peut être "all-products" ou "allmbrs" pour indiquer que tous les membres ou tous les produits probabilistes pour cette variable sont regroupés dans ce fichier

## Liste des variables

Les variables pour les produits d'ensemble disponibles dans les fichiers GRIB2 sont décrites ci-dessous. Pour chaque variable, la définition, la période et la fréquence de disponibilité sont mentionnées.

* __FPRATE-Accum-6h_SFC_0__ :    Pluie verglaçante accumulée sur une période de 6h : 6-72h à chaque 6h
* __FPRATE-Accum-12h_SFC_0__ :   Pluie verglaçante accumulée sur une période de 12h : 12-72h à chaque 6h
* __FPRATE-Accum-24h_SFC_0__ :   Pluie verglaçante accumulée sur une période de 24h : 24-72h à chaque 6h
* __HEATX-Max-24h_TGL_2m__ :     Humidex 2m au-dessus du sol - Maximum sur une période de 24h : 24-72h à chaque 12h
* __HEATX_TGL_2m__ :             Humidex 2m au-dessus du sol : 3-72h à chaque 3h
* __IPRATE-Accum-6h_SFC_0__ :    Grésil (équivalent en eau) accumulé sur une période de 6h : 6-72h à chaque 6h
* __IPRATE-Accum-12h_SFC_0__ :   Grésil (équivalent en eau) accumulé sur une période de 12h : 12-72h à chaque 6h
* __IPRATE-Accum-24h_SFC_0__ :   Grésil (équivalent en eau) accumulé sur une période de 24h : 24-72h à chaque 6h
* __RPRATE-Accum-6h_SFC_0__ :    Pluie accumulée sur une période de 6h : 6-72h à chaque 6h
* __RPRATE-Accum-12h_SFC_0__ :   Pluie accumulée sur une période de 12h : 12-72h à chaque 6h
* __RPRATE-Accum-24h_SFC_0__ :   Pluie accumulée sur une période de 24h : 24-72h à chaque 6h
* __SPRATE-Accum-6h_SFC_0__ :    Neige (équivalent en eau) accumulée sur une période de 6h : 6-72h à chaque 6h
* __SPRATE-Accum-12h_SFC_0__ :   Neige (équivalent en eau) accumulée sur une période de 12h : 12-72h à chaque 6h
* __SPRATE-Accum-24h_SFC_0__ :   Neige (équivalent en eau) accumulée sur une période de 24h : 24-72h à chaque 6h
* __TEMP-Max-24h_TGL_2m__ :      Température 2m au-dessus du sol - Maximum sur une période de 24h : 24-72h à chaque 12h
* __TEMP-Min-24h_TGL_2m__ :      Température 2m au-dessus du sol - Minimum sur une période de 24h : 24-72h à chaque 12h
* __TEMP_TGL_2m__ :              Température 2m au-dessus du sol : 3-72h à chaque 3h
* __TPRATE-Accum-3h_SFC_0__ :    Précipitations totales accumulées sur une période de 3h : 3-72h à chaque 3h
* __TPRATE-Accum-6h_SFC_0__ :    Précipitations totales accumulées sur une période de 6h : 6-72h à chaque 6h
* __TPRATE-Accum-12h_SFC_0__ :   Précipitations totales accumulées sur une période de 12h : 12-72h à chaque 6h
* __TPRATE-Accum-24h_SFC_0__ :   Précipitations totales accumulées sur une période de 24h : 24-72h à chaque 6h
* __TPRATE-Accum-48h_SFC_0__ :   Précipitations totales accumulées sur une période de 48h : 48-72h à chaque 24h
* __TPRATE-Accum-72h_SFC_0__ :   Précipitations totales accumulées sur une période de 72h : 72-72h à chaque 72h
* __WCF-Min-24h_TGL_2m__ :       Facteur éolien 2m au-dessus du sol - Minimum sur une période de 24h : 24-72h à chaque 12h
* __WCF_TGL_2m__ :               Facteur éolien 2m au-dessus du sol : 3-72h à chaque 3h
* __WIND-Max-12h_TGL_10m__ :     Vitesse du vent 10m au-dessus du sol - Maximum sur une période de 12h : 12-72h à chaque 12h
* __WIND_TGL_10m__ :             Vitesse du vent 10m au-dessus du sol : 3-72h à chaque 3h


Les variables pour les membres individuels dans les fichiers GRIB2 sont les suivantes. Les variables sont disponibles de 0 à 72h à chaque 3h :

* __AFRAIN_SFC_0__ :      Précipitations accumulées sous forme de pluie verglaçante 
* __ARAIN_SFC_0__ :       Précipitations accumulées sous forme de pluie 
* __AICEP_SFC_0__ :       Précipitations accumulées sous forme de grésil 
* __ASNOW_SFC_0__ :       Précipitations accumulées sous forme de neige 
* __APCP_SFC_0__ :        Précipitations accumulées sous toutes les formes 
* __SNOD_SFC_0__ :        Épaisseur de la neige au sol 
* __WEASD_SFC_0__ :       Équivalent en eau de l'épaisseur de la neige au sol 
* __HGT_ISBL_PPPP__ :     Hauteur géopotentielle à différents niveaux où PPPP est le niveau de pression en hPa
* __RH_ISBL_PPPP__ :      Humidité relative à différents niveaux où PPPP est le niveau de pression en hPa
* __UGRD_ISBL_PPPP__ :    Composante U du vent à différents niveaux où PPPP est le niveau de pression en hPa
* __VGRD_ISBL_PPPP__ :    Composante V du vent à différents niveaux où PPPP est le niveau de pression en hPa
* __TMP_ISBL_PPPP__ :     Température à différents niveaux où PPPP est le niveau de pression en hPa
* __RH_TGL_2m__ :         Humidité relative à 2m 
* __TMP_TGL_2m__ :        Température à 2m 
* __TCDC_SFC_0__ :        Couverture nuageuse totale 
* __PRES_SFC_0__ :        Pression à la surface 
* __MSL_0__ :             Pression au niveau moyen de la mer 
* __TSOIL_DBLL_10cm__ :   Température du sol. 10cm sous la surface 
* __VSOILM_DBLL_10cm__ :  Humidité volumétrique du sol. 10cm sous la surface 
* __LHTFL_SFC__ :         Flux net de chaleur latente à la surface 
* __SHTFL_SFC_0__ :       Flux net de chaleur sensible à la surface 
* __ULWRF_NTAT_0__ :      Flux ascendant de radiation d'ondes longues au sommet nominal de l'atmosphère 
* __DLWRF_SFC_0__ :       Flux descendant de radiation d'ondes longues à la surface 
* __DSWRF_SFC_0__ :       Flux descendant de radiation d'ondes courtes à la surface

Une [liste en format XML](http://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_reps/reps_element.xml) contenant l'information pour toutes les variables, y compris les descriptions et les unités, en français et en anglais est disponible.

## À propos du masque No-Data

Un masque pour mieux représenter les zones où les données ne sont pas disponibles, appelées aussi "No-Data" a été ajouté dans notre procédure d’encodage GRIB2. Ce masque vise uniquement quelques points de grille non-valides (données non-disponibles), toujours les mêmes et qui se situent en périphérie du domaine. Notons que ces points masqués n’ont aucun effet négatif sur la qualité du produit.

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : ec.dps-client.ec@canada.ca

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).
