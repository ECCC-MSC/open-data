[In English](readme_spei-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [IPEN](readme_spei_fr.md) > IPEN sur le Datamart du SMC

# Données climatiques IPEN en format NetCDF

Ce document décrit le contenu des fichiers de [données IPEN](readme_spei_fr.md) en format NetCDF.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTP. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier NetCDF.

Les fichiers IPEN se trouvent à l'adresse suivante :

* [https://dd.meteo.gc.ca/climate/spei/netcdf/historical/{[SPEI-1, SPEI-3, SPEI-12]}](https://dd.meteo.gc.ca/climate/spei/netcdf/historical)
* [https://dd.meteo.gc.ca/climate/spei/netcdf/scenarios/{[RCP2.6,RCP4.5,RCP8.5]}/{[SPEI-1, SPEI-3, SPEI-12]}](https://dd.meteo.gc.ca/climate/spei/netcdf/scenarios)

où :

* __historical__ : Simulations historiques de 1900 à 2005.
* __scenarios__ : Réfère à différents scénarios d'émissions [RCP2.6, RCP4.5, RCP8.5] de 2006-2100.
* __SPEI__ : Fait référence à l'échelle de temps en mois pour laquelle IPEN a été calculé. SPEI-1 correspond à IPEN d'un mois ; SPEI-3 correspond à IPEN d'un mois et des 2 mois précédents, et SPEI-12 correspond à IPEN d'un mois et des 11 mois précédents. 

## Nomenclature des noms de fichiers

NOTE : TOUTES LES HEURES SONT EN UTC.

* CMIP5_hist_TimeScale_Value_ProjectionResolution_Variable_pctlPP.nc
* CMIP5_rcpx.y_TimeScale_Value_ProjectionResolution_Variable_pctlPP.nc

avec :

* __rcpx.y__ : Scénarios RCP, en prenant l'une des valeurs suivantes : [rcp2.6, rcp4.5, rcp8.5]
* __Time-Scale__ : SPEI-1, SPEI-3 and SPEI-12. SPEI-1 correspond à IPEN d'un mois ; SPEI-3 correspond à IPEN d'un mois et des 2 mois précédents, et SPEI-12 correspond à IPEN d'un mois et des 11 mois précédents. 
* __Value__ : Catégorie de valeurs représentant la période de temps de l'ensemble de données, en prenant l'une de ces deux valeurs :  [RCP= 2006-2100. Historique= 1900-2005]
* __Projection__ : Mappage de la grille (projection) en prenant la valeur : [latlon]
* __Resolution__ : Résolution de la grille en prenant une des valeurs suivantes : [1x1]; 1 représente une résolution de 1 degré dans le sens de la latitude et dans le sens longitudinal.
* __Variable__ : Nom de la variable disponible dans le fichier : Toujours IPEN, ce qui signifie 'Indice de précipitations et d’évapotranspiration normalisé'.
* __PctlPP__ : Nombre percentile de l'ensemble, en prenant l'une des valeurs suivantes : [pctl25, pctl50, pctl75]

Exemples :

* CMIP5_RCP8.5_SPEI-12_2006-2100_latlon1x1_SPEI_pctl50.nc


## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).



