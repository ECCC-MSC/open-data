[In English](readme_spei-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [IPEN](readme_spei_fr.md) > IPEN sur le Datamart du SMC

# Données climatiques de l’Indice de précipitations et d’évapotranspiration normalisé (IPEN) en format NetCDF

[Données IPEN](readme_spei_fr.md) en format NetCDF, un indice climatique utilisé pour évaluer l'influence des changements climatiques sur la sécheresse.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTP. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier NetCDF.

Les fichiers IPEN se trouvent à l'adresse suivante :

* [https://dd.meteo.gc.ca/climate/spei/netcdf/historical/{[SPEI-1, SPEI-3, SPEI-12]}](https://dd.meteo.gc.ca/climate/spei/netcdf/historical)
* [https://dd.meteo.gc.ca/climate/spei/netcdf/scenarios/{[RCP2.6,RCP4.5,RCP8.5]}/{[SPEI-1, SPEI-3, SPEI-12]}](https://dd.meteo.gc.ca/climate/spei/netcdf/scenarios)

où :

* __historical__ : Simulations historiques de 1900 à 2005 de l'Indice de précipitations et d’évapotranspiration normalisé. SPEI-1 correspond à IPEN d'un mois ; SPEI-3 correspond à IPEN d'un mois et des 2 mois précédents, et SPEI-12 correspond à IPEN d'un mois et des 11 mois précédents. 
* __scenarios__ : Réfère à différents scénarios d'émissions [RCP2.6, RCP4.5, RCP8.5] pour la période de 2006-2100.

## Nomenclature des noms de fichiers

NOTE : TOUTES LES HEURES SONT EN UTC.

* CMIP5_hist_TemporalResolution_Value_ProjectionResolution_Variable_pctlPP.nc
* CMIP5_rcpx.y_TemporalResolution_Value_ProjectionResolution_Variable_pctlPP.nc

avec :

* __CMIP5__ : Chaîne constante indiquant les ensembles de données de la phase 5 du projet d'intercomparaison de modèles couplés.
* __hist__ : Chaîne constante indiquant les simulations historiques.
* __rcpx.y__ : Profils représentatifs d’évolution de concentration (scénarios d'émissions), prenant l'une des valeurs : [rcp2.6, rcp4.5, rcp8.5].
* __TemporalResolution__ : Résolution temporelle, prenant l'une des valeurs : [SPEI-1, SPEI-3, SPEI-12]. SPEI-1 correspond à IPEN d'un mois ; SPEI-3 correspond à IPEN d'un mois et des 2 mois précédents, et SPEI-12 correspond à IPEN d'un mois et des 11 mois précédents. 
* __Value__ : Catégorie de valeurs représentant la période de temps de l'ensemble de données, en prenant l'une de ces deux valeurs : [2006-2100] pour les scénarios et [1900-2005] pour les simulations historiques.
* __Projection__ : Projection de la grille (projection), prenant la valeur : [latlon]
* __Resolution__ : Résolution de la grille prenant la valeur : [1x1]; 1x1 représente une résolution de grille de 1 degré dans les directions latitudinale et longitudinale.
* __Variable__ : Nom de la variable disponible dans le fichier, prenant uniquement la valeur [SPEI], pour l'Indice de précipitations et d’évapotranspiration normalisé.
* __PctlPP__ : Percentile d'ensemble, prenant l'une des valeurs : [pctl25, pctl50, pctl75]; pctl25 représente le 25e percentile de l'ensemble ; pctl50 représente le 50e percentile, également appelé médiane de l'ensemble ; pctl75 représente le 75e percentile de l'ensemble.
* __nc__ : Chaîne de caractères constante indiquant le format NetCDF

Exemples :

* CMIP5_rcp8.5_SPEI-12_2006-2100_latlon1x1_SPEI_pctl50.nc

Le fichier représente le 50e percentile de l'indice de précipitations et d’évapotranspiration normalisé d'un mois et des 11 mois précédents pour la période 2006-2100 considérant le scénario d'émissions rcp8.5.

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).



