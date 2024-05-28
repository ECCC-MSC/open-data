[In English](readme_candcs-u6-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [CanDCS-U6](readme_candcs-u6_fr.md) > CanDCS-U6 sur le Datamart du SMC

# Données scénarios climatiques mis à l’échelle statistique des modèles climatiques mondiaux du CMIP6 (CanDCS-U6) en format NetCDF

Des ensembles multimodèles de sorties de modèles et de changements projetés sur grille sont disponibles pour les simulations historiques et quatre scénarios d'émissions, SSP126, SSP245 et SSP585, à une résolution de 1/10è de degré. Les changements projetés sont exprimés sous forme d'anomalies par rapport aux périodes de référence 1950-2014 et 1971-2000.
.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier NetCDF.

Les fichiers CanDCS-U6 se trouvent à l'adresse suivante :

* [https://dd.meteo.gc.ca/climate/candcsu6/10km/historical/](https://dd.meteo.gc.ca/climate/candcsu6/10km/historical)
* [https://dd.meteo.gc.ca/climate/candcsu6/10km/scenarios/{ssp126,ssp245,ssp585}](https://dd.meteo.gc.ca/climate/candcsu6/10km/scenarios)

où :

* __historical__ : Simulations historiques sur les périodes 1950-2014 et 1971-2000
* __scenarios__ : Réfère à différents scénarios d'émissions futurs [ssp126, ssp245, ssp585] pour plusieurs périodes, soit 2015-2100, 2021-2050 et 2041-2070 et 2071-2100

## Nomenclature des noms de fichiers

* `{period}_ECCC_CanDCSU6_{variable}-Pct{percentile}_Sfc_LatLon0.86_{timestep}.nc`
* `{period}_ECCC_CanDCSU6-{scenario}_{variable}-Pct{percentile}_Sfc_LatLon0.86_{timestep}.nc`

avec :

* __period__ : Période associée à chaque ensemble de données, sous format {année du début de la période}-{année de la fin de la période} : [1900-2014; 2015-2100; etc.]
 * __ECCC__ : Chaîne de caractères constante pour Environnement et Changement climatique Canada, la source des données
* __CanDCSU6__ : Chaîne de caractères constante indiquant les données de scénarios climatiques mis à l’échelle statistique des modèles climatiques mondiaux du CMIP6
* __variable__ : Nom de la variable climatique disponible dans le fichier, prenant l'une des valeurs : [AirTemp, AirTempMin, AirTempMax, Precip]. Pour les anomalies : [AirTempAnomaly, AirTempMinAnomaly, AirTempMaxAnomaly, PrecipAnomaly]
* __scenario__ : Scénarios d'émissions, prenant l'une des valeurs : [SSP126, SSP245, SSP585]
* __percentile__ : Percentile d'ensemble, prenant l'une des valeurs : [Pct5, Pct25, Pct50, Pct75, Pct95] ; Pct5 représente le 5e percentile de l'ensemble ; Pct25 représente le 25e percentile de l'ensemble, etc.
* __Sfc__ : Chaîne de caractères constante indiquant que les données sont disponibles à la surface
* __LatLon__ : Chaîne de caractères constante indiquant la projection lat-lon de la grille 
* __0.86__ : Résolution horizontale de la grille de 0.86 degré 
* __timeStep__ : Pas de temps, prenant l'une des valeurs : [P1Y, P1M] ; P1Y représente un pas de temps d'un an, P1M représente un pas de temps de un mois ; [P1Y-{DJF, MAM, JJA, SON}] représente la période saisonnière (ex: DJF: décembre-janvier-février) annuelle ; [P0Y-{DJF, MAM, JJA, SON}] représente la moyenne sur 30 ans, P0Y indique une seule période de temps dans le fichier
* __nc__ : Chaîne de caractères constante indiquant le format NetCDF

Exemples :

* 1950-2014_ECCC_CanDCSU6_AirTemp-Pct50_Sfc_LatLon0.86_P1M.nc
* 1971-2000_ECCC_CanDCSU6_Precip-Pct25_Sfc_LatLon0.86_P1Y-SON.nc
* 2041-2070_ECCC_CanDCSU6-SSP126_PrecipAnomaly-Pct50_Sfc_LatLon0.86_P1Y-JJA.nc

## Liste des variables

Les variables et unités disponibles pour les ensembles de données CanDCS-U6 sur le Datamart du SMC sont :

* Température moyenne (°C)
* Changement projeté de la température moyenne (°C)
* Température minimale (°C)
* Changement projeté de la température minimale (°C)
* Température maximale (°C)
* Changement projeté de la température maximale (°C)
* Précipitations totales (mm)
* Changement relatif projeté des précipitations totales (mm)

## Support

Pour toute question relative à ces données, merci de [nous contacter](mailto:info.cccs-ccsc@canada.ca).

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).



