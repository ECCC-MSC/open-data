[In English](readme_riops-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [SRPOG](readme_riops_fr.md) > Données NetCDF du SRPOG

# Données NetCDF du Système Régional de Prévision Océan-Glace (SRPOG)

Le Centre de prévision météorologique et environnementale du Canada (CPMEC) fournit des prévisions instantanées horaires de champs de glace et de champs océaniques produits par son système régional de prévision océan-glace (SRPOG) opérationnel et interpolés sur une grille en projection polaire stéréographique nord d'une résolution de 5 km à une latitude de 60°N.

Les fichiers des données sont en format NetCDF (NetCDF-4 modèle classique), conformes aux conventions CF liées au climat et aux prévisions (Climate and Forecast Conventions).

Le SRPOG utilise le modèle océan-glace NEMO-CICE et fournit des analyses et prévisions globales de 2 jours de l'océan et de la glace marine, quotidiennement à partir de [00, 06, 12, 18] UTC.

Le SRPOG comprend une analyse 3DVar de la concentration de la glace (assimilant des observations satellitaires et des cartes de glace du service canadien des glaces) alors que les larges échelles de l'analyse océanique sont constraintes en rappelant spectralement les champs de température et de salinité vers ceux du système global de prévision océan-glace du CCMEP (qui lui inclut un système d'assimilation multivarié qui ingère des observations satellitaires ainsi que des observations in-situ).

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTP. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier GRIB2.

Les données sont accessibles aux adresses suivantes :

* [https://dd.meteo.gc.ca/model_riops/netcdf/forecast/polar_stereographic/nd/HH/hhh/](https://dd.meteo.gc.ca/model_riops/netcdf/forecast/polar_stereographic/)

où :

* __nd__ : Numéro de la dimension spatiale des champs de prévision [2d ou 3d] 
* __HH__ : Heure en UTC du début de la passe du modèle[00, 06, 12, 18]
* __hhh__ : Heure de la prévision [000, 001, 002, ..., 048]

Un historique de 2 jours de prévision est disponible dans ce répertoire.

## Nomenclature des noms de fichiers 

NOTE : TOUTES LES HEURES SONT EN UTC.

Les fichiers ont la nomenclature suivante :

* {YYYYMMDD}T{HH}Z_MSC_RIOPS_VAR_LVL_{Grille}{resolution}_P{hhh}.nc

où :

* __YYYYMMDD__ : Année, mois et jour du début de la prévision
* __T__ : Délimiteur temporel selon les normes ISO8601
* __HH__ : Heure en UTC du début de la passe du modèle [00, 06, 12, 18]
* __Z__ : Fuseau horaire (heure UTC)
* __MSC__ : Chaîne de caractères constante pour Meteorological Service of Canada, la source des données 
* __RIOPS__ : Chaîne de caractères constante indiquant que les données proviennent du Système régional de prévision océan-glace
* __VAR__ : Nom de la variable contenue dans le fichier
* __LVL__ : Niveau vertical [SFC, DBS-0.5m, DBS-all]; SFC pour surface, DBS pour la profondeur sous la surface (Depth Below Surface), 0.5m pour 0.5 mètres de profondeur sous la surface et 'all' pour toutes les profondeurs
* __Grille__ : Projection cartographique [PS], PS pour polaire stéréographique 
* __resolution__ : Résolution horizontale [5km], signifie une résolution de 5 km à une latitude 60°N
* __Phhh__ : « P » est un caractère constant. « hhh » représente l’heure de prévision [000, 001, 002, ..., 048]
* __nc__ : Chaîne de caractères constante indiquant le format NetCDF

Exemples de noms de fichier : 

* 20200913T06Z_MSC_RIOPS_IICEVOL_SFC_PS5km_P012.nc 
* 20200913T12Z_MSC_RIOPS_VOSALINE_DBS-all_PS5km_P046.nc
* 20201014T00Z_MSC_RIOPS_VOTEMPER_DBS-0.5m_PS5km_P022.nc

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