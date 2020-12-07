[In English](readme_cmip5-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [CMIP5](readme_cmip5_fr.md) > CMIP5 sur le Datamart du SMC

# Données de scénarios climatiques, basés sur un ensemble de projections de modèles climatiques globaux de la phase 5 du projet d’intercomparaison de modèles couplés (CMIP5) en format NetCDF

Des ensembles multimodèles de sorties de modèles et de changements projetés sur grille sont disponibles pour les simulations historiques et trois scénarios d'émissions, RCP2.6, RCP4.5 et RCP8.5, à une résolution de de 1x1 degré. Les changements projetés sont exprimés sous forme d'anomalies par rapport à la période de référence 1986-2005.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier NetCDF.

Les fichiers CMIP5 se trouvent à l'adresse suivante :

* https://dd.meteo.gc.ca/climate/cmip5/netcdf/historical/annual/{[anomaly,absolute]}
* https://dd.meteo.gc.ca/climate/cmip5/netcdf/historical/seasonal/{[DJF,MAM,JJA,SON]}/{[anomaly,absolute]}
* https://dd.meteo.gc.ca/climate/cmip5/netcdf/historical/monthly_ens/absolute
* https://dd.meteo.gc.ca/climate/cmip5/netcdf/scenarios/{[RCP2.6,RCP4.5,RCP8.5]}/annual/{[anomaly,absolute,avg_20years]}                                                                  
* https://dd.meteo.gc.ca/climate/cmip5/netcdf/scenarios/{[RCP2.6,RCP4.5,RCP8.5]}/seasonal/{[DJF,MAM,JJA,SON]}/{[anomaly,absolute,avg_20years]}                                                                             
* https://dd.meteo.gc.ca/climate/cmip5/netcdf/scenarios/{[RCP2.6,RCP4.5,RCP8.5]}/monthly_ens/absolute

où :

* __historical__ : Simulations historiques sur la période 1950-2005
* __scenarios__ : Réfère à différents scénarios d’émission [RCP2.6, RCP4.5,RCP8.5] pour la période 2006-2100
* __seasonal__ : Les saisons météorologiques standards sont utilisées: mars à mai (MAM, printemps), juin à août (JJA, été), septembre à novembre (SON, automne), et décembre à février (DJF, hiver)
* __avg_20year__ : Moyennes de 20 ans de changements projetés, disponibles pour quatre périodes : 2021-2040; 2041-2060; 2061-2080; 2081-2100
* __Anomaly__ : Représente les changements projetés par rapport à la période de référence 1986-2005
* __Absolute__ : Représente les projections d’ensembles multi-modèles (valeurs actuelles)

## Nomenclature des noms de fichiers

NOTE : TOUTES LES HEURES SONT EN UTC.

* CMIP5_hist_TemporalResolution_Value_ProjectionResolution_Variable_pctlPP_TimeStep.nc
* CMIP5_rcpx.y_TemporalResolution_Value_ProjectionResolution_Variable_pctlPP_TimeStep.nc

avec :

* __CMIP5__ : Chaîne constante indiquant les ensembles de données de la phase 5 du projet d'intercomparaison de modèles couplés.
* __hist__ : Chaîne constante indiquant les simulations historiques.
* __rcpx.y__ : Profils représentatifs d’évolution de concentration (scénarios d'émissions), prenant l'une des valeurs : [rcp2.6, rcp4.5, rcp8.5].
* __TemporalResolution__ : Résolution temporelle, prenant l'une des valeurs : [annual, monthly, DJF, MAM, JJA, SON].
* __Value__ : Catégorie de valeurs, prenant l'une des valeurs :  [abs, anom, 2021-2040, 2041-2060, 2061-2080, 2081-2100] ; abs représente les valeurs absolues (valeurs réelles / projections modélisées) ; anom représente les anomalies.
* __Projection__ : Projection de la grille (projection), prenant la valeur :[latlon].
* __Resolution__ : Résolution de la grille, prenant l'une des valeurs : [1x1] ; 1x1 représente une résolution de grille de 1 degré dans les directions latitudinale et longitudinale.
* __Variable__ : Nom de la variable climatique disponible dans le fichier, prenant l'une des valeurs :[ PCP, TEMP, SICETHKN, SICETHKN, SICECONC, SNDPT, SFCWND] ; PCP représente les précipitations moyennes, TEMP représente la température moyenne, SICETHKN représente l'épaisseur de la glace de mer, SICECONC représente la concentration de glace de mer, SNDPT représente la profondeur de la neige, SFCWND représente la vitesse du vent de surface.
* __PctlPP__ : Percentile d'ensemble, prenant l'une des valeurs : [pctl5, pctl25, pctl50, pctl75, pctl95] ; pctl5 représente le 5e percentile de l'ensemble ; pctl25 représente le 25e percentile de l'ensemble ; pctl50 représente le 50e percentile, également appelé médiane de l'ensemble ; pctl75 représente le 75e percentile de l'ensemble ; pctl95 représente le 95e percentile de l'ensemble.
* __TimeStep__ : Pas de temps, prenant l'une des valeurs : [P1Y, P1M] ; P1Y représente un pas de temps d'un an et P1M représente un pas de temps d'un mois.
* __nc__ : Chaîne de caractères constante indiquant le format NetCDF

Exemple :   CMIP5_rcp4.5_DJF_2021-2040_latlon1x1_PCP_pctl50_P1Y.nc

Le fichier représente le 50e percentile de l'ensemble multimodèle CMIP5 de changements relatifs projetés sur la période 2021-2040 des précipitations moyennes (c.-à-d. anomalies) par rapport à la période de référence de 1986-2005, en hiver (moyenne sur 3 mois en décembre, janvier, février), exprimés en pourcentage de changement. Les bandes du fichier NetCDF sont des pas de temps annuels.

## Liste des variables

Les variables et unités disponibles pour les ensembles de données CMIP5 sur le Datamart du SMC sont :

* Projection des précipitations moyennes des multi-modèles d’ensemble CMIP5 (mm/jour)
* Projections de la concentration de glace de mer des multi-modèles d’ensemble CMIP5 (pourcentage, %, de la surface de la cellule de la grille)
* Projections de l'épaisseur de la glace de mer des multi-modèles d’ensemble CMIP5 (m)
* Projections d'épaisseur de neige des multi-modèles d’ensemble CMIP5 (m)
* Projections de la vitesse du vent de surface des multi-modèles d’ensemble CMIP5 (m/s)
* Projections de température moyenne des multi-modèles d’ensemble CMIP5 (°C)
* Variation moyenne projetée des précipitations, basée sur des ensembles multimodèles CMIP5 (%)
* Changement projeté de la concentration de la glace de mer d'après les ensembles multimodèles CMIP5 (%) 
* Variation projetée de l'épaisseur de la glace de mer d'après les ensembles multimodèles CMIP5 (%)
* Variation projetée de l'épaisseur de neige selon les ensembles multimodèles CMIP5 (%)
* Variation projetée de la vitesse du vent de surface basée sur des ensembles multimodèles CMIP5 (%)
* Changement de température moyenne projetée basée sur des ensembles multimodèles CMIP5 (°C)

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).



