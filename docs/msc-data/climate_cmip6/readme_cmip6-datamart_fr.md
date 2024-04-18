[In English](readme_cmip5-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [CMIP6](readme_cmip6_fr.md) > CMIP6 sur le Datamart du SMC

# Données de scénarios climatiques, basés sur un ensemble de projections de modèles climatiques globaux de la phase 6 du projet d’intercomparaison de modèles couplés (CMIP6) en format NetCDF

Des ensembles multimodèles pour une série de variables basées sur les projections des modèles climatiques mondiaux (MCM) de la phase 6 du Projet d’intercomparaison des modèles couplés (CMIP6) sont disponibles pour 1850 à 2100 sur une grille mondiale commune de 1 x 1 degré.

Les projections climatiques varient entre les MCM en raison des différences dans la représentation et l’approximation des systèmes et des processus terrestres, ainsi que de la variabilité naturelle et de l’incertitude concernant les futurs facteurs climatiques. Ainsi, aucun modèle climatique n’est meilleur que les autres. À la place, l’utilisation des résultats d’un ensemble de modèles (p. ex. en utilisant la moyenne) constitue une pratique exemplaire puisqu’un ensemble tient compte de l’incertitude dans les projections des modèles et offre des projections climatiques plus fiables.

Le site Données et scénarios climatiques canadiens (DSCC) offre quatre types de produits basés sur les ensembles multimodèles du CMIP6 : des ensembles de données et des graphiques de séries chronologiques, des cartes et des ensembles de données connexes, des ensembles de données tabulaires et des ensembles de données maillées à l’échelle mondiale. Des ensembles mensuels, saisonniers et annuels sont disponibles pour un maximum de six profils socioéconomiques partagés (SSP) [SSP1 1.9, SSP1 2.6, SSP2 4.5, SSP3 7.0, SSP4 6.0 et SSP5 8. 5], quatre périodes futures (court terme [2021-2040], moyen terme [2041-2060 et 2061-2080], fin du siècle [2081-2100]) et un maximum de cinq percentiles (5e, 25e, 50e [médiane], 75e et 95e) de la distribution de l’ensemble du CMIP6.

Le nombre de modèles dans chaque ensemble diffère selon la disponibilité des modèles pour chaque SSP et variable; consultez la liste des modèles pour plus de détails sur les modèles inclus dans chaque ensemble. La majorité des produits indiquent les changements prévus sous forme d’anomalies selon une période de référence historique (1995 à 2014). Les produits fournis comprennent des ensembles de données et des graphiques à l’échelle mondiale, nationale, provinciale et territoriale. Pour de plus amples renseignements sur les ensembles multimodèles du CMIP6, veuillez consulter la documentation technique.



## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier NetCDF.

Les fichiers CMIP6 se trouvent à l'adresse suivante :

* https://dd.meteo.gc.ca/climate/cmip6/netcdf/historical/annual/{[anomaly,absolute]}
* https://dd.meteo.gc.ca/climate/cmip6/netcdf/historical/seasonal/{[DJF,MAM,JJA,SON]}/{[anomaly,absolute]}
* https://dd.meteo.gc.ca/climate/cmip6/netcdf/historical/monthly_ens/absolute
* https://dd.meteo.gc.ca/climate/cmip6/netcdf/scenarios/{[RCP2.6,RCP4.5,RCP8.5]}/annual/{[anomaly,absolute,avg_20years]}                                                                  
* https://dd.meteo.gc.ca/climate/cmip6/netcdf/scenarios/{[RCP2.6,RCP4.5,RCP8.5]}/seasonal/{[DJF,MAM,JJA,SON]}/{[anomaly,absolute,avg_20years]}                                                                             
* https://dd.meteo.gc.ca/climate/cmip6/netcdf/scenarios/{[RCP2.6,RCP4.5,RCP8.5]}/monthly_ens/absolute

où :

* __historical__ : Simulations historiques sur la période 1950-2005
* __scenarios__ : Réfère à différents scénarios d’émission [RCP2.6, RCP4.5,RCP8.5] pour la période 2006-2100
* __seasonal__ : Les saisons météorologiques standards sont utilisées: mars à mai (MAM, printemps), juin à août (JJA, été), septembre à novembre (SON, automne), et décembre à février (DJF, hiver)
* __avg_20year__ : Moyennes de 20 ans de changements projetés, disponibles pour quatre périodes : 2021-2040; 2041-2060; 2061-2080; 2081-2100
* __Anomaly__ : Représente les changements projetés par rapport à la période de référence 1986-2005
* __Absolute__ : Représente les projections d’ensembles multi-modèles (valeurs actuelles)

## Nomenclature des noms de fichiers

NOTE : TOUTES LES HEURES SONT EN UTC.

* CMIP6_hist_TemporalResolution_Value_ProjectionResolution_Variable_pctlPP_TimeStep.nc
* CMIP6_rcpx.y_TemporalResolution_Value_ProjectionResolution_Variable_pctlPP_TimeStep.nc

avec :

* __CMIP6__ : Chaîne constante indiquant les ensembles de données de la phase 6 du projet d'intercomparaison de modèles couplés.
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

Exemple :   CMIP6_rcp4.5_DJF_2021-2040_latlon1x1_PCP_pctl50_P1Y.nc

Le fichier représente le 50e percentile de l'ensemble multimodèle CMIP6 de changements relatifs projetés sur la période 2021-2040 des précipitations moyennes (c.-à-d. anomalies) par rapport à la période de référence de 1986-2005, en hiver (moyenne sur 3 mois en décembre, janvier, février), exprimés en pourcentage de changement. Les bandes du fichier NetCDF sont des pas de temps annuels.

## Liste des variables

Les variables et unités disponibles pour les ensembles de données CMIP6 sur le Datamart du SMC sont :

* Projection des précipitations moyennes des multi-modèles d’ensemble CMIP6 (mm/jour)
* Projections de la concentration de glace de mer des multi-modèles d’ensemble CMIP6 (pourcentage, %, de la surface de la cellule de la grille)
* Projections de l'épaisseur de la glace de mer des multi-modèles d’ensemble CMIP6 (m)
* Projections d'épaisseur de neige des multi-modèles d’ensemble CMIP6 (m)
* Projections de la vitesse du vent de surface des multi-modèles d’ensemble CMIP6 (m/s)
* Projections de température moyenne des multi-modèles d’ensemble CMIP6 (°C)
* Variation moyenne projetée des précipitations, basée sur des ensembles multimodèles CMIP6 (%)
* Changement projeté de la concentration de la glace de mer d'après les ensembles multimodèles CMIP6 (%) 
* Variation projetée de l'épaisseur de la glace de mer d'après les ensembles multimodèles CMIP6 (%)
* Variation projetée de l'épaisseur de neige selon les ensembles multimodèles CMIP6 (%)
* Variation projetée de la vitesse du vent de surface basée sur des ensembles multimodèles CMIP6 (%)
* Changement de température moyenne projetée basée sur des ensembles multimodèles CMIP6 (°C)

## Support

Pour toute question relative à ces données, merci de [nous contacter](mailto:info.cccs-ccsc@canada.ca).

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).



