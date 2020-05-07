[In English](readme_riops-datamart-alpha_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [SRPOG](readme_riops_fr.md) > Données GRIB2 de SRPOG sur DD-Alpha

# Données GRIB2 du Système Régional de Prévision Océan-Glace (SRPOG) expérimental

Cette page décrit les données du [Système Régional de Prévision Océan-Glace (SRPOG)](./readme_riops_fr.md) disponibles sur DD-Alpha, le site Web d'essai de données du Datamart du SMC.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTP. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier GRIB2.

Les données sont accessibles aux adresses suivantes :

* [https://dd.alpha.meteo.gc.ca/model_riops/netcdf](https://dd.alpha.meteo.gc.ca/model_riops/netcdf)

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

Les fichiers contenant les données sur la grille ps5km60N se trouvent à l'adresse suivante :

* [https://dd.alpha.meteo.gc.ca/yopp/model_riops/netcdf/forecast/polar_stereographic/nd/YYYY/MM/DD/HH/hhh/](https://dd.alpha.meteo.gc.ca/yopp/model_riops/netcdf/forecast/polar_stereographic/nd/YYYY/MM/DD/HH/hhh/)

où :

* __n__ : Numéro de la dimension spatiale des champs de prévision [2 ou 3]   
* __HH__ : Heure en UTC du début de la simulation [00, 12]
* __hhh__ : Heure de la prévision ; chaque 3 heures en commençant par l'heure 0 [000, 003, ..., 048] pour n=2 et l'heure 3 [003, 006, ..., 048] pour n=3


## Liste des variables

Liste des variables (champs de prévision) disponibles dans les fichiers contenant des champs 2D :

* votemper :	Température potentielle de l'eau de mer au premier niveau du modèle
* vosaline :	Salinité de l'eau de mer au premier niveau du modèle
* vozocrtx :	Composante X de la vitesse de l'eau au premier niveau du modèle
* vomecrty :	Composante Y de la vitesse de l'eau au premier niveau du modèle
* sossheig :	Hauteur de la surface de la mer
* somixhgt :	Profondeur de la turbocline 
* sokaraml :	Profondeur de la couche de mélange d'après le critère de densité
* iiceconc :	Fraction de la glace de mer
* iicevol :		Volume de glace de mer par unité de surface de cellule de grille
* itzocrtx :	Composante X de la vitesse de la glace de mer
* itmecrty :	Composante Y de la vitesse de la glace de mer 
* isnowvol :	Volume de neige sur la glace de mer par unité de surface de cellule de grille
* iicesurftemp :	Température de la surface de la neige/glace de mer
* iicepressure :	Pression interne de la glace, intégrée verticalement
* iicestrength :	Résistance à la compression de la glace, intégrée verticalement

Liste des variables (champs de prévision) disponibles dans les fichiers contenant des champs 3D :

* votemper : 	Température potentielle de l'eau de mer
* vosaline :	Salinité de l'eau de mer 
* vozocrtx :	Composante X de la vitesse de l'eau 
* vomecrty :	Composante Y de la vitesse de l'eau 

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).