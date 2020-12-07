[In English](readme_riops-datamart-alpha_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [SRPOG](readme_riops_fr.md) > Données NetCDF du SRPOG sur DD-Alpha

# Données NetCDF du Système Régional de Prévision Océan-Glace (SRPOG)

Le Centre de prévision météorologique et environnementale du Canada (CPMEC) fournit des instantanés de champs prévisionnels de glace et des moyennes temporelles des champs océaniques prévisionnels produits par son système régional de prévision océan-glace (SRPOG) expérimental et interpolées sur une grille en projection polaire stéréographique nord d'une résolution de 5 km à une latitude de 60°N (ps5km60N).

Les fichiers des données sont en format NetCDF (NetCDF-4 modèle classique), conformes aux conventions CF liées au climat et aux prévisions (Climate and Forecast Conventions).

Le SRPOG utilise le modèle océan-glace NEMO-CICE et fournit des analyses et prévisions globales de 2 jours de l'océan et de la glace marine, quotidiennement à partir de [00, 12] UTC.

Le SRPOG comprend une analyse 3DVar de la concentration de la glace (assimilant des observations satellitaires et des cartes de glace du service canadien des glaces) alors que les larges échelles de l'analyse océanique sont constraintes en rappelant spectralement les champs de température et de salinité vers ceux du système global de prévision océan-glace du CCMEP (qui lui inclut un système d'assimilation multivarié qui ingère des observations satellitaires ainsi que des observations in-situ).

Les flux atmosphériques servant aux prévisions de 2 jours sont calculés par couplage entre NEMO-CICE et le modèle atmosphérique du système canadien de prévision de l'Arctique SCPA. Comme tel, les prévisions du SRPOG décrites ici sont maintenant générées directement dans le [SCPA](../nwp_caps/readme_caps_fr.md).

Ce système contribue de façon importante à diverses expériences scientifiques qui font partie de l'[année de la prévision polaire (YOPP)](https://www.polarprediction.net/) en fournissant des prévisions numériques du temps à l'échelle kilométrique dans l'Arctique canadien.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier GRIB2.

Les données sont accessibles aux adresses suivantes :

* [https://dd.alpha.meteo.gc.ca/yopp/model_riops/netcdf/forecast/polar_stereographic/nd/YYYY/MM/DD/HH/hhh/](https://dd.alpha.meteo.gc.ca/yopp/model_riops/netcdf/forecast/polar_stereographic/)

* __nd__ : Numéro de la dimension spatiale des champs de prévision [2d ou 3d]. 
* __YYYY__: L’année du début de la prévision [2012, 2013, ...].
* __MM__ : Le mois du début de la prévision [01, 02, 03, ..., 12].
* __DD__ : Jour du début de la prévision.
* __HH__ : Heure en UTC du début de la simulation [00,12].
* __hhh__ : Heure de la prévision.

Une archive en ligne est disponible durant toute la durée du projet YOPP.

## Nomenclature des noms de fichiers 

NOTE : TOUTES LES HEURES SONT EN UTC.

Les fichiers ont la nomenclature suivante :

* CMC_riops_Variable_TypedeNiveau_Niveau_ProjectionResolution_MoyenneTemporelle_YYYYMMDDHH_Phhh.nc

où :

* __CMC__ : Chaîne de caractères constante indiquant que le Centre météorologique canadien (CMC) émet les prévisions
* __riops__ : Chaîne de caractères constante indiquant le système de prévision qui génère les données
* __Variable__ : Nom de la variable contenue dans le fichier
* __TypedeNiveau__ : Type de niveau : sfc ou depth
* __Niveau__ : Valeur du niveau: 0 pour niveau sfc (surface) et soit 0.5 (mètres) soit 'all' (toutes les profondeurs) pour le niveau type depth
* __Projection__ : Projection cartographique, prend juste une valeur : ps
* __Résolution__ : prend juste une valeur: 5km60N. 5km60N signifie une résolution de 5 km à une latitude 60°N
* __MoyenneTemporelle__ : Cette chaîne prend la valeur 3h-mean, indiquant que la variable et une moyenne temporelle calculée sur la période de temps spécifiée (3 heures pour 3h). À noter que le temps de validité de la variable de prévision est fixé à la fin de la période de calcul de la moyenne. Notez aussi l'exception suivante: les variables de glace sont en fait des instantanées.
* __YYYYMMDD__ : Année, mois et jour du début de la prévision
* __HH__ : Heure en UTC du début de la simulation [00, 12]
* __Phhh__ : P est un caractère constant. hhh est l'heure de prévision [000, 003, 006, ..., 240]
* __nc__ : Chaîne de caractères constante indiquant le format NetCDF

Exemples de noms de fichier : 

* CMC_riops_iiceconc_sfc_0_ps5km60N_3h-mean_2016020312_P003.nc

## Liste des variables

Liste des variables (champs de prévision) disponibles dans les fichiers contenant des champs 2D :

* __votemper__ :	Température potentielle de l'eau de mer au premier niveau du modèle
* __vosaline__ :	Salinité de l'eau de mer au premier niveau du modèle
* __vozocrtx__ :	Composante X de la vitesse de l'eau au premier niveau du modèle
* __vomecrty__ :	Composante Y de la vitesse de l'eau au premier niveau du modèle
* __sossheig__ :	Hauteur de la surface de la mer
* __somixhgt__ :	Profondeur de la turbocline 
* __sokaraml__ :	Profondeur de la couche de mélange d'après le critère de densité
* __iiceconc__ :	Fraction de la glace de mer
* __iicevol__ :		Volume de glace de mer par unité de surface de cellule de grille
* __itzocrtx__ :	Composante X de la vitesse de la glace de mer
* __itmecrty__ :	Composante Y de la vitesse de la glace de mer 
* __isnowvol__ :	Volume de neige sur la glace de mer par unité de surface de cellule de grille
* __iicesurftemp__ :	Température de la surface de la neige/glace de mer
* __iicepressure__ :	Pression interne de la glace, intégrée verticalement
* __iicestrength__ :	Résistance à la compression de la glace, intégrée verticalement

Liste des variables (champs de prévision) disponibles dans les fichiers contenant des champs 3D :

* __votemper__ : 	Température potentielle de l'eau de mer
* __vosaline__ :	Salinité de l'eau de mer 
* __vozocrtx__ :	Composante X de la vitesse de l'eau 
* __vomecrty__ :	Composante Y de la vitesse de l'eau 

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).