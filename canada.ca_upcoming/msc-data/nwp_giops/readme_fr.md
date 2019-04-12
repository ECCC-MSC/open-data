# Table des matières

* [Description](#Description)
* Accès
  * License
  * Métadonnées
  * [Accès aux données brutes](#acces-aux-donnees-brutes)
  * Accès par service web
* Produits
* Documentation technique
* Registre des changements

# Description

Fichier README pour les fichiers du Système global de prévision océan-glace (SGPOG) disponibles sur le Datamart du Service météorologique du Canada (SMC).

Ce document décrit les  données SGPOG en format NetCDF disponibles sur le serveur de données HTTP du SMC dans le répertoire :
http://dd.meteo.gc.ca/model_giops/netcdf

Le Centre de prévision météorologique et environnementale du Canada (CPMEC) fournit des champs prévisionnels produits par son Système global 
de prévision océan-glace (SGPOG) et interpolées sur deux grilles usagers : une grille régulière latitude-longitude de 0.2° de résolution (latlon0.2x0.2) et une grille en projection polaire stéréographique nord d'une résolution de 5 km à une latitude de 60°N (ps5km60N).  À 00Z, Les champs fournis à l'échéance 0-heure correspondent à l'analyse SGPOG et sont valides à 00Z.  À toutes les autres échéances les champs correspondent à la prévision et sont moyennés dans le temps.  Les fichiers des données sont en format NetCDF (NetCDF-4 modèle classique), conformes aux conventions CF liées au climat et aux prévisions (Climate and Forecast Conventions).

Le SGPOG utilise le modèle océan-glace NEMO-CICE et fournit des analyses et prévisions globales de 10 jours de l'océan et de la glace marine, quotidiennement à partir de 0000 UTC sur une grille tripolaire (ORCA025) avec une résolution de 1/4°.  Le SGPOG comprend un système d'assimilation océanique qui ingère les observations satellitaires de l'anomalie du niveau de la mer et de sa température de surface (SST), ainsi que des observations in-situ de la température et de la salinité.  Les observations in-situ proviennent de plusieurs sources dont: le réseau de flotteurs profileurs autonomes ARGO, des amarres, des navires opportuns, mammifères marins et expéditions de recherche.  Les analyses océanographiques sont fusionnées avec les analyses de glace marine produites par le système d'analyse de glace globale opérationnel du CMC.  Les flux atmosphériques servant aux champs d'essai et aux prévisions de 10 jours sont calculés à partir des prévisions atmosphériques issues du système global de prévision déterministe du CMC.


# Accès

* Fichier README pour les fichiers du Système global de prévision océan-glace (SGPOG) disponibles sur le Datamart du Service météorologique du Canada (SMC).

* Pour consulter ce fichier en ligne, allez à :
  http://dd.meteo.gc.ca/model_giops/doc/README_GIOPS.txt

* Les fichiers sont produits par Environnement et Changement climatique Canada :
  http://ec.gc.ca/

## Licence

* Pour les conditions d'utilisation des données SGPOG, veuillez consulter les conditions générales d'utilisation des données du Datamart du SMC :
  http://dd.meteo.gc.ca/doc/LICENCE_GENERAL.txt

## Métadonnées

 * https://open.canada.ca/data/en/dataset

## Accès aux données brutes

 * Les fichiers SGPOG  se trouvent à l'adresse suivante :
   http://dd.meteo.gc.ca/model_giops/netcdf                    

   Un historique de 5 jours de prévision est stocké dans ce répertoire. Liens vers la page de doc du Datamart ../msc-datamart/readme.md

## Service web GeoMet du SMC

- Afin d'accommoder les utilisateurs des données du Service météorologique du Canada (SMC), ces données sont également accessibles au standard Web Map Service (WMS) par le biais des services web GeoMet.  Ce standard est particulièrement approprié pour visualiser ces données sur des cartes interactives sur le web ainsi que sur des applications mobiles (ex: téléphone intelligents), ou tout logiciel qui supporte le standard WMS.  Les données sont affichées à la demande et pour la région d'intérêt déterminée par l'utilisateur, ceci sans aucun téléchargement de fichiers.

* La documentation de ce service est disponible ici :
  http://www.ec.gc.ca/meteo-weather/default.asp?lang=Fr&n=C0D9B3D8-1


# Produits

## Liste des variables (champs de prévision) disponibles dans les fichiers contenant des champs 2D :

- votemper	Température potentielle de l'eau de mer au premier niveau du modèle
- vosaline	Salinité de l'eau de mer au premier niveau ##du modèle
- vozocrtx	Composante X de la vitesse de l'eau au premier niveau du modèle
- vomecrty	Composante Y de la vitesse de l'eau au premier niveau du modèle
- Hauteur de la surface de la mer par rapport au géoïde
- somixhgt	Profondeur de la turbocline 
- sokaraml	Profondeur de la couche de mélange d'après le critère de densité
- iiceconc	Fraction de la glace de mer
- iicevol		Volume de glace de mer par unité de surface de cellule de grille
- itzocrtx	Composante X de la vitesse de la glace de mer
- itmecrty	Composante Y de la vitesse de la glace de mer 
- isnowvol	Volume de neige sur la glace de mer par unité de surface de cellule de grille
- iicesurftemp	Température de la surface de la neige/glace de mer
- iicepressure	Pression interne de la glace, intégrée verticalement
- iicestrength	Résistance à la compression de la glace, intégrée verticalement

## Liste des variables (champs de prévision) disponibles dans les fichiers contenant des champs 3D :

- votemper	Température potentielle de l'eau de mer
- vosaline	Salinité de l'eau de mer 
- vozocrtx	Composante X de la vitesse de l'eau 
- vomecrty	Composante Y de la vitesse de l'eau 

Notez que puisque les champs à l'heure de prévision 0 ne sont pas moyennés dans le temps, on peut simplement extraire le niveau de surface des champs votemper, vosaline, vozocrtx et vomecrty des champs 3D pour obtenir les champs 2D correspondants. 

# Documentation technique

## Nom de fichier
Les noms des fichiers ont la forme :
CMC_giops_Variable_TypedeNiveau_Niveau_ProjectionResolution_MoyenneTemporelle_YYYYMMDDHH_Phhh.nc
où :
- CMC : Chaîne de caractères constante indiquant que le Centre météorologique canadien (CMC) émet les prévisions
- giops : Chaîne de caractères constante indiquant le système de prévision qui génère les données
- Variable : Nom de la variable contenue dans le fichier
- TypedeNiveau : Type de niveau : sfc ou depth
- Niveau : Valeur du niveau: 0 pour niveau sfc (surface) et soit 0.5 (mètres) soit "all" (toutes les profondeurs) pour le niveau type depth
- Projection : Projection cartographique : latlon ou ps
- Résolution : 0.2x0.2 ou 5km60N.  0.2x0.2 signifie une résolution de 0.2° dans les directions longitudinale et latitudinale, tandis que 5km60N signifie une résolution de 5 km à une latitude 60°N
- MoyenneTemporelle: Pour des échéances au-delà de 0 heures, cette chaîne prend la valeur 3h-mean ou 24h-mean, indiquant que la variable est une moyenne temporelle calculée sur la période de temps spécifiée (3 heures pour 3h et 24 heures pour 24h).  À noter que le temps de validité de la variable de prévision est fixé à la fin de la période de calcul de la moyenne. À 00Z, pour l'échéance 0-heure cette chaîne est vide (c.-à.d. les champs fournis ne sont pas moyennés et sont considérés valides à 00Z).
- YYYYMMDD : Année, mois et jour du début de la prévision
- HH : Heure en UTC du début de la simulation [00,12]
- TypeDeFichierhhh : Pour des échéances au-delà de 0 heures, TypeDeFichier est égale à P et hhh est l'heure de prévision [003, 006, ..., 240]. Pour l'échéance 0-heure à 00Z, TypeDeFichier est égale à Anal et hhh est égale à 000.
- nc : Chaîne de caractères constante indiquant le format NetCDF

Exemple de nom de fichier de prévision :
CMC_giops_votemper_depth_0.5_latlon0.2x0.2_3h-mean_2016020800_P036.nc

Exemple de nom de fichier analyse :
CMC_giops_votemper_depth_all_latlon0.2x0.2_2016120700_Anal000.nc

Les fichiers contenant les données sur la grille latlon0.2x0.2 se trouvent à l'adresse suivante :
http://dd.meteo.gc.ca/model_giops/netcdf/lat_lon/nd/HH/hhh/  

Les fichiers contenant les données sur la grille ps5km60N se trouvent à l'adresse suivante :
http://dd.meteo.gc.ca/model_giops/netcdf/polar_stereographic/nd/HH/hhh/

où :
- n : Numéro de la dimension spatiale des champs de prévision [2 ou 3]
- HH : Heure en UTC du début de la simulation [00,12]
- hhh : Heure de la prévision ; chaque 3 heures [000, 003, ..., 240] pour N=2 et chaque 24 heures [024, 048, ..., 240] pour N=3

À noter que, puisque les fichiers à l'heure de prévision 0, à 00Z, sont basés sur l'analyse et non la prévision, un sous-ensemble de variables est fourni à cette échéance, contrairement aux autres échéances.

## Format

- Les fichiers des données sont en format NetCDF (NetCDF-4 modèle classique), conformes aux conventions CF liées au climat et aux prévisions (Climate and Forecast Conventions).  Un fichier NetCDF se décrit lui-même à l'aide des métadonnées décrivant les données contenues.  Les fichiers contiennent des moyennes temporelles des champs de prévision de l'état de la glace marine et de l'océan.  La période de calcul de la moyenne a une longueur de 3 heures pour les champs bidimensionnels et de 24 heures pour les champs tridimensionnels, les deux périodes finissant au temps de validité des champs respectifs. À 00Z, pour l'heure de prévision 0, les fichiers contiennent des champs analyses, considérés valides à 00Z. Le temps dans le fichier est encodé comme le temps en secondes écoulé depuis le 1er Janvier 1950 à 0h00 UTC.

## Niveaux

- Les champs tridimensionnels sont disponibles sur 50 niveaux de profondeur, qui sont les niveaux du modèle océanique utilisé par SGPOG. Niveaux de profondeur (m): 0.494025, 1.54138, 2.64567, 3.81949, 5.07822, 6.44061, 7.92956, 9.573, 11.405, 13.4671, 15.8101, 18.4956, 21.5988, 25.2114, 29.4447, 34.4342, 40.3441, 47.3737, 55.7643, 65.8073, 77.8539, 92.3261, 109.729, 130.666, 155.851, 186.126, 222.475, 266.04, 318.127, 380.213, 453.938, 541.089, 643.567, 763.333, 902.339, 1062.44, 1245.29, 1452.25, 1684.28, 1941.89, 2225.08, 2533.34, 2865.7, 3220.82, 3597.03, 3992.48, 4405.22, 4833.29, 5274.78, 5727.92.

- Une partie des variables représentent des quantités au premier niveau du modèle, tandis que les autres sont définies à la surface de l'océan (ex. variables de la glace marine).

- La visualisation des champs contenus dans les fichiers NetCDF produits par SGPOG a été testée avec succès avec les outils suivants : Panoply (version 4.2.2) et IDV (version 5.2).

- Des informations sur le format de fichier NetCDF et sur les conventions CF liées au climat et aux prévisions peuvent être trouvées aux adresses ci-dessous :

- Network Common Data Form (NetCDF) :
    http://www.unidata.ucar.edu/software/netcdf/

- Les conventions CF liées au climat et aux prévisions :
    http://cfconventions.org/

## Liens vers articles scientifiques

- Network Common Data Form (NetCDF) :
- http://www.unidata.ucar.edu/software/netcdf/

- Les conventions CF liées au climat et aux prévisions :
- http://cfconventions.org/

- Outil Integrated Data Viewer (IDV) pour l'analyse et la visualisation de données géoscientifiques :
- http://www.unidata.ucar.edu/software/idv/

- Outil pour visualiser les sorties de modèles en format NetCDF
- http://www.giss.nasa.gov/tools/panoply
- http://www.geo.uni-bremen.de/Interdynamik/images/stories/pdf/visualizing_netcdf_panoply.pdf

# Registre des changements

Lien vers a page du journal des changements (actuellement dans le Guide des produits du CMC)

- [*Système global de prévision océean-glace *](http://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/changes_f.html)

- [*Annonces dd info *](https://lists.ec.gc.ca/pipermail/dd_info/2019-March/subject.html#325)