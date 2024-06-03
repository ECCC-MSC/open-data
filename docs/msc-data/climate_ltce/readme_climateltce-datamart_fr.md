[En Anglais](readme_climateltce-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [ECLT](readme_climateltce_fr.md) > Records des Extrêmes Quotidiens sur le Datamart du SMC

# Extrêmes climatiques quotidiens à long terme au format CSV

Cette page décrit les données d'extrêmes climatiques quotidiennes (Extrêmes climatiques à long terme)(readme_climateltce_fr.md) au format CSV. Veuillez noter que ces données ne doivent pas être utilisées pour répondre à des questions sur les tendances climatiques. Pour ces analyses, veuillez consulter les [Données climatiques canadiennes ajustées et homogénéisées](../climate_ahccd/readme_ahccd_fr.md).

## Localisation des données

Les données du Datamart du SMC peuvent être [récupérées automatiquement avec le protocole AMQP (Advanced Message Queuing Protocol)](../../msc-datamart/amqp_en.md) dès qu'elles sont disponibles. Un [aperçu et exemples d'accès et d'utilisation des données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d'y accéder avec un navigateur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier CSV.

Les données sont accessibles aux URL suivantes :

* [https://dd.meteo.gc.ca/climate/ltce/daily/{Variable}]/{PROVINCE}](https://dd.meteo.gc.ca/climate/ltce/daily)
* [https://dd.meteo.gc.ca/climate/ltce/stations](https://dd.meteo.gc.ca/climate/ltce/stations)

où :

* __Variable__ : Prend l'une des valeurs [Temperature, Precipitation, Snowfall]
* __PROVINCE__ : Chaîne de deux lettres identifiant la province dans laquelle se trouve la station [ex : AB, BC, MB, etc.]

## Nomenclature des noms de fichiers 

Les noms de fichiers ont la forme suivante :

* `climate_LTCE_{Variable}-Records_{PROVINCE}_{STATION-ID}.csv`

Les listes de stations virtuelles ont la forme suivante

* `climate_LTCE_{Variable}_Virtual-Stations.csv`

où :

* __climate__ : Chaîne de caractères constante indiquant l'ensemble de données climatiques
* __LTCE__ : Chaîne de caractères constante indiquant le nom de l'ensemble de données sur les extrêmes climatiques à long terme
* __Variable__ : Nom de la variable disponible dans le fichier, prenant l'une des valeurs suivantes : [Temperature, Precipitation, Snowfall]
* __Records__ : Chaîne de caractères constante indiquant que les données sont des records d'extrêmes quotidiens
* __PROVINCE__ : Chaîne de deux lettres identifiant la province dans laquelle se trouve la station, prenant l'une des valeurs suivantes : [AB, BC, MB, NB, NL, NS, NT, NU, ON, PE, QC, SK, YT]
* __STATION-ID__ : Identifiant unique de la station concernée
* __Virtual-Stations__ : Chaîne constante indiquant que le fichier est une liste de stations virtuelles
* __csv__ : Chaîne de caractères constante indiquant le format CSV

Exemples :

* climate_LTCE_Precipitation-Records_ON_VSON104.csv
* climate_LTCE_Temperature_Virtual-Stations.csv

## Liste des variables

Les variables et unités disponibles pour les records des extrêmes quotidiens (Extrêmes climatiques à long terme) sont les suivantes :

* High Max Temp : Température journalière la plus élevée (°C)
* High Min Temp : Température minimale quotidienne la plus élevée (°C)
* Low Max Temp : Température quotidienne maximale la plus froide (°C)
* Low Min Temp: Température quotidienne la plus froide (°C)
* Precipitation : Précipitations maximales quotidiennes (mm)
* Snowfall : Chute de neige journalière maximale (cm)

## Support

Si vous avez des questions concernant ces données, veuillez [nous contacter] (mailto:info.cccs-ccsc@canada.ca).

## Annonces de la liste de diffusion dd_info 

Les annonces relatives à ce jeu de données sont disponibles sur la [liste dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).


























[In English](readme_climateltce-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_fr.md) > [LTCE](readme_climateltce_fr.md) > Climate Climate Records on MSC Datamart

# Daily Long Term Climate Extremes in CSV format

This page describes the Daily Climate Records (Long Term Climate Extremes)(readme_climateltce_en.md) data in CSV format. Please note that these data should not be used to answer questions about climate trends. For these analyses, please consult the [Adjusted and Homogenized Canadian Climate Data](../climate_ahccd/readme_ahccd_en.md).

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available via the HTTPS protocol. It is possible to access it with a standard browser. In this case, we obtain a list of links giving access to a CSV file.

The data can be accessed at the following URLs:

* [https://dd.weather.gc.ca/climate/ltce/daily/{Variable}]/{PROVINCE}](https://dd.weather.gc.ca/climate/ltce/daily)
* [https://dd.weather.gc.ca/climate/ltce/stations](https://dd.weather.gc.ca/climate/ltce/stations)

where:

* __Variable__: Taking one of the values [Temperature, Precipitation,Snowfall]
* __PROVINCE__: Two letter string identifying the province that the station resides in [ex: AB, BC, MB, etc.]

## File name nomenclature 

File names have the form:

* `climate_LTCE_{Variable}-Records_{PROVINCE}_{STATION-ID}.csv`

The lists of virtual stations have the form:

* `climate_LTCE_{Variable}_Virtual-Stations.csv`

where:

* __climate__: Constant string indicating climate dataset
* __LTCE__: Constant string indicating the name of the dataset that is long term climate extremes
* __Variable__: Name of variable available in the file, taking one of the values : [Temperature, Precipitation, Snowfall]
* __Records__: Constant string indicating that the data are records
* __PROVINCE__: Two letter string identifying the province that the station resides in, taking one the values : [AB, BC, MB, NB, NL, NS, NT, NU, ON, PE, QC, SK, YT]
* __STATION-ID__: Unique identifier for the station of interest
* __Virtual-Stations__: Constant string indicating that the file is a list of virtual stations
* __csv__: Constant string indicating the CSV format

Examples :

* climate_LTCE_Precipitation-Records_ON_VSON104.csv
* climate_LTCE_Temperature_Virtual-Stations.csv

## Variable list

The available variables and units for the Long Term Climate Extremes of climate indices are:

* High Max Temp: Highest daily temperature (°C)
* High Min Temp: Highest minimum daily temperature (°C)
* Low Max Temp: Coldest maximum daily temperature (°C)
* Low Min Temp: Coldest daily temperature (°C)
* Precipitation: Maximum daily precipitation (mm)
* Snowfall: Maximum daily snowfall (cm)

## Support

If you have any questions about this data, please [contact us](mailto:info.cccs-ccsc@canada.ca).

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).




















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

Pour toute question relative à ces données, merci de [nous contacter](mailto:info.cccs-ccsc@canada.ca).

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).
