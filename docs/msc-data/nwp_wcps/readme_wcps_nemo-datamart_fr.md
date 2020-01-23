[In English](readme_wcps-nemo-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [SPCE](readme_wcps_fr.md) > SPCE-NEMO sur le Datamart du SMC

# Système de prévision du cycle de l'eau (SPCE) NEMO données en format NetCDF des Grands Lacs et du Saint-Laurent 

Les données du NEMO en Netcdf du Système de prévision du cycle de l'eau des Grands Lacs et du Saint-laurent (SPCE) sont disponibles sur une grlle de latitude et de longitude de 1681x3181 points comparable à une résolution de 1 km (0.009 x 0.009 degrés)

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le Protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTP. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier netCDF. Nous vous recommandons d’automatiser le téléchargement en le scriptant avec wget (lien externe, anglais) ou un programme équivalent. Pour plus d’information sur wget, consultez les notes d’utilisation.

Les données sont accessibles à l'adresses suivante :

* [https://dd.meteo.gc.ca/model_wcps/nemo/netcdf/lat_lon/{nd}/{HH}/{hhh}/ ](https://dd.meteo.gc.ca/model_wcps/nemo/netcdf/lat_lon)                  

où :

* __nd__ : Dimension spatiale, latitude et longitude [2d]
* __HH__ : Heure en UTC du début de la simulation [00,12]
* __hhh__ : Heure de la prévision [001, ..., 084] 

Un historique de 30 jours de prévision est stocké dans ce répertoire.

## Spécification technique de la grille  
![](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_wcps/grille_wcps_nemo.png)

Dans le domaine complet indiqué par le rectangle noir, le domaine de données valide, qui couvre les lacs, est en couleur. 

| Paramètre | Valeur |
| ------ | ------ |
| ni | 1681 |
| nj | 3181 | 
| résolution à 45° N | 1km |


## Nomenclature des noms de fichiers 

NOTE: TOUTES LES HEURES SONT EN UTC.

La nomenclature des noms des fichiers est la suivante :

CMC_wcps-nemo_Variable_TypedeNiveau_Niveau_ProjectionResolution_YYYYMMDDHH_Phhh.nc

où :

* __CMC__ : Chaîne de caractères constante indiquant que le Centre météorologique canadien (CMC) émet les prévisions
* __wcps_nemo__ : Chaîne de caractères constante indiquant le système de prévision qui génère les données
* __Variable__ : Nom de la variable contenue dans le fichier
* __TypedeNiveau__ : Type de niveau [sfc, depth, tgl]
* __Niveau__ : Valeur du niveau, 0 pour sfc (surface), soit 0.5 pour la profondeur (profondeur des lacs en mètres), soit 40 pour l'altitude (l'altitude en mètres)
* __Projection__ : Projection cartographique [latlon]
* __Résolution__ : 0.009x0.009. Signifie une résolution de 0.009°(environ 1km) dans les directions longitudinale et latitudinale
* __YYYYMMDD__ : Année, mois et jour du début de la prévision
* __HH__ : Heure en UTC du début de la simulation [00,12]
* __Phhh__ : P caractère constant, hhh l'heure de prévision [001, ..., 084] 
* __nc__ : Chaîne de caractères constante indiquant le format NetCDF

Exemple :

* CMC_wcps_nemo_vomecrty_depth_0.5_latlon0.009x0.009_2019011100_P036.nc

## Liste des variables

Liste des variables disponibles dans les fichiers contenant des champs 2D :

* __tairsurf__ : Température de l'air à environ 40 mètres en altitude
* __uwindsurf__ : Composante X de la vitesse du vent à 40 mètres en altitude
* __vwindsurf__ : Composante Y de la vitesse du vent à 40 mètres en altitude
* __vozocrtx__ : Composante X de la vitesse de l'eau au premier niveau du modèle 
* __vomecrty__ : Composante Y de la vitesse de l'eau au premier niveau du modèle
* __votemper__ : Température potentielle de l'eau de mer au premier niveau du modèle
* __vosaline__ : Salinité de l'eau de mer 
* __sossheig__ : Hauteur de la surface de la mer par rapport au géoïde
* __sokaraml__ : Profondeur de la couche de mélange d'après le critère de densité
* __iiceconc__ : Fraction de la glace de mer
* __iicevol__ : Volume de glace de mer par unité de surface de cellule de grille
* __itzocrtx__ : Composante X de la vitesse de la glace de mer
* __itmecrty__ : Composante Y de la vitesse de la glace de mer
* __iicepressure__ : Pression interne de la glace, intégrée verticalement
* __iicestrength__ : Résistance à la compression de la glace, intégrée verticalement

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).

