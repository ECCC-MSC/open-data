[In English](readme_dcs-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données ouvertes publiques du SMC](../readme_fr.md) > Résultats statistiquement réduits à  l'échelle sur le Datamart du SMC

# Données de scénarios climatiques, basés sur un ensemble de projections de modèles climatiques globaux de la phase 5 du projet d’intercomparaison de modèles couplés (CMIP5) en format netCDF

Ce document présente les scénarios climatiques à réduction d’échelle statistique basés sur les projections des modèles du climat mondial, d’après la phase 5 du Projet d’intercomparaison des modèles couplés (CMIP5). Des résultats et des changements projetés obtenus par des ensembles multimodèles à réduction d’échelle statistique sont disponibles pour les simulations historiques et trois scénarios d’émissions, RCP 2.6, RCP 4.5 et RCP 8.5, à une résolution de 10 km. Les changements projetés sont exprimés sous forme d’anomalies par rapport à la période de référence de 1986 à 2005. Une plage de centiles couvrant les ensembles multimodèles est disponible en téléchargement.

Les projections peuvent varier d’un modèle climatique à l’autre, car ces modèles représentent de façon différente les processus du système terrestre. La littérature scientifique récente montre qu’il est probable que l’utilisation d’une approche s’appuyant sur des ensembles multimodèles permette de mieux décrire les changements climatiques projetés.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le Protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage-overview/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTP. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier netCDF.

Les fichiers CMIP5 se trouvent à l'adresse suivante:

* /climate/dcs/netcdf/historical/annual/[anomaly,absolute]
* /climate/dcs/netcdf/historical/seasonal/[DJF,MAM,JJA,SON]/[anomaly,absolute]
* /climate/dcs/netcdf/historical/monthly_ens/absolute
* /climate/dcs/netcdf/scenarios/[RCP2.6,RCP4.5,RCP8.5]/annual/[anomaly,absolute,avg_20years]   
* /climate/dcs/netcdf/scenarios/[RCP2.6,RCP4.5,RCP8.5]/seasonal/[DJF,MAM,JJA,SON]/[anomaly,absolute,avg_20years]                                                                             
* /climate/dcs/netcdf/scenarios/[RCP2.6,RCP4.5,RCP8.5]/monthly_ens/absolute

Où :

* __historical__ : Simulations historiques sur la période 1950-2005
* __scenarios__ : Réfère à différents scénarios d’émission [RCP2.6, RCP4.5,RCP8.5] pour la période 2006-2100
* __seasonal__ : Les saisons météorologiques standards sont utilisées: mars à mai (MAM, printemps), juin à août (JJA, été), septembre à novembre (SON, automne), et décembre à février (DJF, hiver)
* __avg_20year__ : Moyennes de 20 ans de changements projetés, disponibles pour quatre périodes : 2021-2040; 2041-2060; 2061-2080; 2081-2100
* __Anomaly__ : Représente les changements projetés par rapport à la période de référence 1986-2005
* __Absolute__ : Représente les projections d’ensembles multi-modèles (valeurs actuelles)

## Nomenclature des noms de fichiers

NOTE: TOUTES LES HEURES SONT EN UTC.

DCS_hist_TemporalResolution_Value_ProjectionResolution_Variable_pctlPP_TimeStep.nc
DCS_rcpx.y_TemporalResolution_Value_ProjectionResolution_Variable_pctlPP_TimeStep.nc

Avec :

* __DCS__ : chaîne constante indiquant une abréviation (acronyme non officiel) pour ce document en référence aux scénarios climatiques statistiquement réduits à l'échelle.
* __hist__ : chaîne constante indiquant les simulations historiques.
* __rcpx.y__ : profils représentatifs d’évolution de concentration (scénarios d'émissions), prenant l'une des valeurs : [rcp2.6, rcp4.5, rcp8.5]
* __TemporalResolution__ : résolution temporelle, prenant l'une des valeurs : [annual, monthly, DJF, MAM, JJA, SON]
* __Value__ : catégorie de valeurs, prenant l'une des valeurs :  [abs, anom, 2021-2040, 2041-2060, 2061-2080, 2081-2100] ; abs représente les valeurs absolues (valeurs réelles / projections modélisées) ; anom représente les anomalies.
* __Projection__ : projection de la grille (projection), prenant la valeur :[latlon].
* __Resolution__ : résolution de la grille, prenant l'une des valeurs : [1x1] ; 1x1 représente une résolution de grille de 1 degré dans les directions latitudinale et longitudinale
* __Variable__ : nom de la variable climatique disponible dans le fichier, prenant l'une des valeurs :[ PCP, TEMP, SICETHKN, SICETHKN, SICECONC, SNDPT, SFCWND] ; PCP représente les précipitations moyennes, TEMP représente la température moyenne, SICETHKN représente l'épaisseur de la glace de mer, SICECONC représente la concentration de glace de mer, SNDPT représente la profondeur de la neige, SFCWND représente la vitesse du vent de surface.
* __PctlPP__ : percentile d'ensemble, prenant l'une des valeurs : [pctl5, pctl25, pctl50, pctl75, pctl95] ; pctl5 représente le 5e percentile de l'ensemble ; pctl25 représente le 25e percentile de l'ensemble ; pctl50 représente le 50e percentile, également appelé médiane de l'ensemble ; pctl75 représente le 75e percentile de l'ensemble ; pctl95 représente le 95e percentile de l'ensemble.
* __TimeStep__ : pas de temps, prenant l'une des valeurs : [P1Y, P1M] ; P1Y représente un pas de temps d'un an et P1M représente un pas de temps d'un mois.
* __nc__ : chaîne de caractères constante indiquant le format NetCDF

Exemple :   DCS_rcp4.5_DJF_2021-2040_latlon0.086x0.086_PCP_pctl50_P1Y.nc

Le fichier représente le 50e percentile de l'ensemble multimodèle statistiquement réduit à l'échelle des changements relatifs projetés sur la période 2021-2040 de la précipitation totale (c.-à -d. anomalies) par rapport à la période de référence de 1986-2005, en hiver (moyenne sur 3 mois en décembre, janvier, février), exprimés en pourcentage de changement. Les bandes du fichier NetCDF sont des pas de temps annuels.

## Liste des variables

Attention : les tableaux ci-dessous ne sont pas à jour (à venir), certaines variables sont manquantes. N'hésitez pas à [nous contacter](mailto:ec.dps-client.ec@canada.ca) pour plus d'information.

Les variables et unités disponibles pour les ensembles de données CMIP5 sur Datamart sont :

* Projections des changements de température moyenne basées sur les multimodèles d'ensemble statistiquement réduits (°C)
* Projections des changements de température minimale basées sur les multimodèles d'ensemble statistiquement réduits (°C)
* Projections des changements de température maximale basées sur les multimodèles d'ensemble statistiquement réduits (°C)
* Projections des changements de précipitation totale basées sur les multimodèles d'ensemble statistiquement réduits (%)
* Variation moyenne projetée des précipitations, basée sur des multimodèles d'ensemble statistiquement réduits (mm/jour)
* Variation moyenne projetée de la température moyenne, basée sur des multimodèles d'ensemble statistiquement réduits (%)
* Variation moyenne projetée de la température maximale, basée sur des multimodèles d'ensemble statistiquement réduits (%)
* Variation moyenne projetée de la température minimale, basée sur des multimodèles d'ensemble statistiquement réduits (%)

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : ec.dps-client.ec@canada.ca

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).


