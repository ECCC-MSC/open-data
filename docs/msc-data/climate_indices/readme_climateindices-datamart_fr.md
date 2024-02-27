[In English](readme_climateindices-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [Indices climatiques](readme_climateindices_fr.md) > Indices climatiques sur le Datamart du SMC

# Données des indices climatiques mis à l’échelle de manière statistique en format NetCDF

Des [données d'indices climatiques](readme_climateindices_fr.md) en format NetCDF, mis à l’échelle de manière statistique pour des simulations historiques, ainsi que pour trois scénarios d’émissions, RCP 2.6, RCP 4.5 et RCP 8.5, sont disponibles sur une grille à une résolution de 10 km x 10 km.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier NetCDF.

Les fichiers se trouvent à l'adresse suivante :

* [https://dd.meteo.gc.ca/climate/indices/netcdf/historical](https://dd.meteo.gc.ca/climate/indices/netcdf/historical)
* [https://dd.meteo.gc.ca/climate/indices/netcdf/scenarios/[RCP2.6,RCP4.5,RCP8.5]](https://dd.meteo.gc.ca/climate/indices/netcdf/scenarios/)

où :

* __historical__ : Simulations historiques de 1951 à 2005
* __scenarios__ : Réfère à différents scénarios d'émissions [RCP2.6, RCP4.5, RCP8.5] de 2006-2100
* __absolute__ : Représente les projections des ensembles multimodélisés (valeur réelle)

## Nomenclature des noms de fichiers

NOTE : TOUTES LES HEURES SONT EN UTC.

* INDICES_hist_Value_ProjectionResolution_Variable_pctlPP.nc
* INDICES_rcpx.y_Value_ProjectionResolution_Variable_pctlPP.nc

avec :

* __INDICES__: Chaîne constante indiquant que les ensembles de données sont des indices climatiques mis à l’échelle de manière statistique
* __hist__: Chaîne constante indiquant des données historiques
* __rcpx.y__: Version des profils représentatifs d’évolution de concentration (expériences au moyen de scénario), adoptant l’une des valeurs : [rcp2.6, rcp4.5, rcp8.5]
* __Value__: Catégorie de valeurs prenant l’une de ces deux valeurs: [2006-2100] pour les scénarios et [1951-2005] pour les simulations historiques
* __Projection__: Projection de la grille (projection) prenant la valeur : [latlon]
* __Resolution__: Résolution de grille prenant la valeurs: [0.086x0.086]; 0,086 représente une résolution de 0,086 degré dans les sens latitudinal et longitudinal (environ 10 km)
* __Variable__: Nom de la variable disponible dans le fichier prenant l’une des valeurs : [CDD, GSC, GSO, GSW, HDD, TX30, TN20, PREP1]; CDD signifie degrés-jours de refroidissement, GSC signifie durée de la saison de croissance des cultures de saison fraîche, GSO signifie durée de la saison de croissance des cultures d’hiver, GSW signifie durée de la saison de croissance des cultures de saison chaude, HDD signifie degrés-jours de chauffage, TX30 signifie journées chaudes (nombre de jours affichant des températures maximales supérieures à 30 °C), TN20 signifie nuits chaudes (nombre de nuits affichant des températures minimales supérieures à 20 °C), PREP1 signifie nombre de jours au cours desquels les précipitations ont été supérieures à 1 mm.
* __PctlPP__: Nombre de centiles de l’ensemble, adoptant l’une des valeurs : [pctl5, pctl25, pctl50, pctl75, pctl95]
* __nc__: Chaîne constante indiquant le format NetCDF

Exemples :

* INDICES_rcp4.5_2006-2100_latlon0.086x0.086_GSO_pctl50.nc

Le fichier représente le 50e centile de l’ensemble multimodèle mis à l’échelle de manière statistique de la durée prévue de la saison de croissance des cultures d’hiver (GSO) de 2006 à 2100 dans le scénario d’émission de RCP4.5, exprimée en nombre de jours. Les bandes dans le fichier NetCDF sont des étapes temporelles annuelles.

## Liste de variables

Les variables et unités disponibles pour les ensembles de données multimodèles des indices climatiques mis à l’échelle de manière statistique sont :

* __CDD__ : Degrés-jours de refroidissement (°C-jour)
* __HDD__ : Degrés-jours de chauffage (°C-jour)
* __GSC__ : Durée de la saison de croissance des cultures de saison fraîche (jours)
* __GSO__ : Durée de la saison de croissance des cultures d’hiver (jours)
* __GSW__ : Durée de la saison de croissance des cultures de saison chaude (jours)
* __PREP1__ : Nombre de jours au cours desquels les précipitations ont été > 1 mm (jours)
* __TN20__ : Nuits chaudes (nombre de jours où la température minimale a dépassé 20°C) (jours)
* __TX30__ : Journées chaudes (nombre de jours où la température maximale a dépassé 30°C) (jours)

## Support

Pour toute question relative à ces données, merci de [nous contacter](https://weather.gc.ca/mainmenu/contact_us_f.html).

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).
