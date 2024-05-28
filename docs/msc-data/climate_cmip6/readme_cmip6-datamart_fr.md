[In English](readme_cmip6-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [CMIP6](readme_cmip6_fr.md) > CMIP6 sur le Datamart du SMC

# Données de scénarios climatiques, basés sur un ensemble de projections de modèles climatiques globaux de la phase 6 du projet d’intercomparaison de modèles couplés (CMIP6) en format NetCDF

Des ensembles multimodèles pour une série de variables basées sur les projections des modèles climatiques mondiaux (MCM) de la phase 6 du Projet d’intercomparaison des modèles couplés (CMIP6) sont disponibles pour 1900 à 2100 sur une grille mondiale commune de 1 x 1 degré.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier NetCDF.

Les fichiers CMIP6 se trouvent à l'adresse suivante :

* [https://dd.meteo.gc.ca/climate/cmip6/100km/historical/](https://dd.meteo.gc.ca/climate/cmip6/100km/historical)
* [https://dd.meteo.gc.ca/climate/cmip6/100km/scenarios/{ssp126,ssp245,ssp370,ssp585}](https://dd.meteo.gc.ca/climate/cmip6/100km/scenarios)                                                         

où :

* __historical__ : Simulations historiques sur la période 1900-2014
* __scenarios__ : Réfère à différents profils socioéconomiques partagés [ssp126, ssp245, ssp370, ssp585] pour plusieurs périodes de 20ans, soit court terme [2021-2040], moyen terme [2041-2060 et 2061-2080] et fin du siècle [2081-2100]

## Nomenclature des noms de fichiers

La nomenclature des noms des fichiers est la suivante :

* `{period}_ECCC_CMIP6_{variable}-Pct{percentile}_Sfc_LatLon1.0_{timestep}.nc`
* `{period}_ECCC_CMIP6-{scenario}_{variable}-Pct{percentile}_Sfc_LatLon1.0_{timestep}.nc`

avec :

* __period__ : Période associée à chaque ensemble de données, sous format {année du début de la période}-{année de la fin de la période} : [1900-2014; 2015-2100; etc.]
 * __ECCC__ : Chaîne de caractères constante pour Environnement et Changement climatique Canada, la source des données
* __CMIP6__ : Chaîne de caractères constante indiquant les ensembles de données de la phase 6 du projet d'intercomparaison de modèles couplés
* __variable__ : Nom de la variable climatique disponible dans le fichier, prenant l'une des valeurs : [AirTemp, Precip, SeaIceConcentration, SeaIceThickness, Wind, SnowDepth]. Pour les anomalies : [AirTempAnomaly, PrecipAnomaly, SeaIceConcentrationAnomaly, SeaIceThicknessAnomaly, WindAnomaly, SnowDepthAnomaly]
* __scenario__ : Profils socioéconomiques partagés (SSP), prenant l'une des valeurs : [SSP126, SSP245, SSP370, SSP585]
* __percentile__ : Percentile d'ensemble, prenant l'une des valeurs : [Pct5, Pct25, Pct50, Pct75, Pct95] ; Pct5 représente le 5e percentile de l'ensemble ; Pct25 représente le 25e percentile de l'ensemble, etc.
* __Sfc__ : Chaîne de caractères constante indiquant que les données sont disponibles à la surface
* __LatLon__ : Chaîne de caractères constante indiquant la projection lat-lon de la grille 
* __1.0__ : Résolution de grille de 1 degré dans les directions latitudinale et longitudinale
* __timeStep__ : Pas de temps, prenant l'une des valeurs : [P1Y, P1M] ; P1Y représente un pas de temps d'un an, P1M représente un pas de temps de un mois ; [P1Y-{DJF, MAM, JJA, SON}] représente la période saisonnière (ex: DJF: décembre-janvier-février) annuelle ; [P0Y-{DJF, MAM, JJA, SON}] représente la moyenne sur 20 ans, P0Y indique une seule période de temps dans le fichier
* __nc__ : Chaîne de caractères constante indiquant le format NetCDF

Exemples :

* 1900-2014_ECCC_CMIP6_AirTempAnomaly-Pct50_Sfc_LatLon1.0_P1M.nc
* 1900-2014_ECCC_CMIP6_SeaIceThickness-Pct25_Sfc_LatLon1.0_P1Y-SON.nc
* 2015-2100_ECCC_CMIP6-SSP370_Precip-Pct05_Sfc_LatLon1.0_P1M.nc
* 2015-2100_ECCC_CMIP6-SSP126_PrecipAnomaly-Pct50_Sfc_LatLon1.0_P1Y-JJA.nc

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



