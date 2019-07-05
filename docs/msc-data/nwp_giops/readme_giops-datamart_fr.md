[In English](readme_giops-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données ouvertes publiques du SMC](../readme_fr.md) > SGPOG sur le Datamart du SMC

# Données NetCDF du Système global de prévision océan-glace (SGPOG)

Le Centre de prévision météorologique et environnementale du Canada (CPMEC) fournit des champs prévisionnels produits par son [Système global
de prévision océan-glace (SGPOG)](readme_giops_fr.md) et interpolées sur deux grilles usagers : une grille régulière latitude-longitude de 0.2° de résolution (latlon0.2x0.2) et une grille en projection polaire stéréographique nord d'une résolution de 5 km à une latitude de 60°N (ps5km60N).  À 00Z, Les champs fournis à l'échéance 0-heure correspondent à l'analyse SGPOG et sont valides à 00Z.  À toutes les autres échéances les champs correspondent à la prévision et sont moyennés dans le temps.  Les fichiers des données sont en format NetCDF (NetCDF-4 modèle classique), conformes aux conventions CF liées au climat et aux prévisions (Climate and Forecast Conventions).

Les fichiers des données sont en format NetCDF (NetCDF-4 modèle classique), conformes aux conventions CF liées au
climat et aux prévisions (Climate and Forecast Conventions).  Un fichier NetCDF se décrit lui-même à l'aide des
métadonnées décrivant les données contenues.  Les fichiers contiennent des moyennes temporelles des champs de
prévision de l'état de la glace marine et de l'océan.  La période de calcul de la moyenne a une longueur de 3 heures
pour les champs bidimensionnels et de 24 heures pour les champs tridimensionnels, les deux périodes finissant au
temps de validité des champs respectifs.
À 00Z, pour l'heure de prévision 0, les fichiers contiennent des champs analyses, considérés valides à 00Z.
Le temps dans le fichier est encodé comme le temps en secondes écoulé depuis le 1er Janvier 1950 à 0h00 UTC.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le Protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTP. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier netCDF. Nous vous recommandons d’automatiser le téléchargement en le scriptant avec wget (lien externe, anglais) ou un programme équivalent. Pour plus d’information sur wget, consultez les notes d’utilisation.

Les données sont accessibles à l'adresses suivante :

* [https://dd.meteo.gc.ca/model_giops/netcdf](https://dd.meteo.gc.ca/model_giops/netcdf)                  

Un historique de 5 jours de prévision est stocké dans ce répertoire.

* Les fichiers contenant les données sur la grille latlon0.2x0.2 se trouvent à l'adresse suivante :

https://dd.meteo.gc.ca/model_giops/netcdf/lat_lon/nd/HH/hhh/  

* Les fichiers contenant les données sur la grille ps5km60N se trouvent à l'adresse suivante :

https://dd.meteo.gc.ca/model_giops/netcdf/polar_stereographic/nd/HH/hhh/

où :

* __n__ : Numéro de la dimension spatiale des champs de prévision [2 ou 3]. 
* __HH__ : Heure en UTC du début de la simulation [00,12].
* __hhh__ : Heure de la prévision ; chaque 3 heures [000, 003, ..., 240] pour N=2 et chaque 24 heures
[024, 048, ..., 240] pour N=3.

À noter que, puisque les fichiers à l'heure de prévision 0, à 00Z, sont basés sur l'analyse et non la prévision, un
sous-ensemble de variables est fourni à cette échéance, contrairement aux autres échéances.

## Nomenclature des noms de fichiers 

NOTE: TOUTES LES HEURES SONT EN UTC.

La nomenclature des noms des fichiers suivante :

CMC_giops_Variable_TypedeNiveau_Niveau_ProjectionResolution_MoyenneTemporelle_YYYYMMDDHH_Phhh.nc

où :

* __CMC__ : Chaîne de caractères constante indiquant que le Centre météorologique canadien (CMC) émet les prévisions.
* __giops__ : Chaîne de caractères constante indiquant le système de prévision qui génère les données.
* __Variable__ : Nom de la variable contenue dans le fichier.
* __TypedeNiveau__ : Type de niveau : sfc ou depth.
* __Niveau__ : Valeur du niveau: 0 pour niveau sfc (surface) et soit 0.5 (mètres) soit "all" (toutes les profondeurs)
pour le niveau type depth.
* __Projection__ : Projection cartographique : latlon ou ps.
* __Résolution__ : 0.2x0.2 ou 5km60N.  0.2x0.2 signifie une résolution de 0.2° dans les directions longitudinale et
latitudinale, tandis que 5km60N signifie une résolution de 5 km à une latitude 60°N.
* __MoyenneTemporelle__ : Pour des échéances au-delà de 0 heures, cette chaîne prend la valeur 3h-mean ou 24h-mean,
indiquant que la variable est une moyenne temporelle calculée sur la période de temps spécifiée (3 heures pour 3h
et 24 heures pour 24h).  À noter que le temps de validité de la variable de prévision est fixé à la fin de la
période de calcul de la moyenne. À 00Z, pour l'échéance 0-heure cette chaîne est vide (c.-à.d. les champs fournis ne sont
pas moyennés et sont considérés valides à 00Z).
* __YYYYMMDD__ : Année, mois et jour du début de la prévision.
* __HH__ : Heure en UTC du début de la simulation [00,12].
* __TypeDeFichierhhh__ : Pour des échéances au-delà de 0 heures, TypeDeFichier est égale à P et hhh est l'heure de
prévision [003, 006, ..., 240]. Pour l'échéance 0-heure à 00Z, TypeDeFichier est égale à Anal et hhh est égale à 000.
* __nc__ : Chaîne de caractères constante indiquant le format NetCDF.

Exemple de nom de fichier de prévision :
* CMC_giops_votemper_depth_0.5_latlon0.2x0.2_3h-mean_2016020800_P036.nc

Exemple de nom de fichier analyse :
* CMC_giops_votemper_depth_all_latlon0.2x0.2_2016120700_Anal000.nc

## Niveaux

Les champs tridimensionnels sont disponibles sur 50 niveaux de profondeur, qui sont les niveaux du modèle océanique
utilisé par SGPOG.

__Niveaux de profondeur (m)__ : 0.494025, 1.54138, 2.64567, 3.81949, 5.07822, 6.44061, 7.92956, 9.573, 11.405, 13.4671,
15.8101, 18.4956, 21.5988, 25.2114, 29.4447, 34.4342, 40.3441, 47.3737, 55.7643, 65.8073, 77.8539, 92.3261, 109.729,
130.666, 155.851, 186.126, 222.475, 266.04, 318.127, 380.213, 453.938, 541.089, 643.567, 763.333, 902.339, 1062.44,
1245.29, 1452.25, 1684.28, 1941.89, 2225.08, 2533.34, 2865.7, 3220.82, 3597.03, 3992.48, 4405.22, 4833.29, 5274.78,
5727.92.

Une partie des variables représentent des quantités au premier niveau du modèle, tandis que les autres sont définies
à la surface de l'océan (ex. variables de la glace marine).

La visualisation des champs contenus dans les fichiers NetCDF produits par SGPOG a été testée avec succès avec les
outils suivants: Panoply (version 4.2.2) et IDV (version 5.2).

## Liste des variables

Liste des variables (champs de prévision) disponibles dans les fichiers contenant des champs 2D :

* __votemper__ : Température potentielle de l'eau de mer au premier niveau du modèle.
* __vosaline__ : Salinité de l'eau de mer au premier niveau du modèle.
* __vozocrtx__ : Composante X de la vitesse de l'eau au premier niveau du modèle.
* __vomecrty__ : Composante Y de la vitesse de l'eau au premier niveau du modèle.
* __sossheig__ : Hauteur de la surface de la mer par rapport au géoïde.
* __somixhgt__ : Profondeur de la turbocline.
* __sokaraml__ : Profondeur de la couche de mélange d'après le critère de densité.
* __iiceconc__ : Fraction de la glace de mer.
* __iicevol__ : Volume de glace de mer par unité de surface de cellule de grille.
* __itzocrtx__ : Composante X de la vitesse de la glace de mer.
* __itmecrty__ : Composante Y de la vitesse de la glace de mer.
* __isnowvol__ : Volume de neige sur la glace de mer par unité de surface de cellule de grille.
* __iicesurftemp__ : Température de la surface de la neige/glace de mer.
* __iicepressure__ : Pression interne de la glace, intégrée verticalement.
* __iicestrength__ : Résistance à la compression de la glace, intégrée verticalement.

Liste des variables (champs de prévision) disponibles dans les fichiers contenant des champs 3D :

* __votemper__ : Température potentielle de l'eau de mer.
* __vosaline__ : Salinité de l'eau de mer.
* __vozocrtx__ : Composante X de la vitesse de l'eau. 
* __vomecrty__ : Composante Y de la vitesse de l'eau.

Notez que puisque les champs à l'heure de prévision 0 ne sont pas moyennés dans le temps, on peut simplement extraire le niveau de surface des champs votemper, vosaline, vozocrtx et vomecrty des champs 3D pour obtenir les champs 2D correspondants. 

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : ec.dps-client.ec@canada.ca

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).




