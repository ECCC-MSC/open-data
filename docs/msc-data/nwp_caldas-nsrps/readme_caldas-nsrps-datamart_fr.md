[In English](readme_caldas-nsrps-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [SCanADS-SNPSR](readme_caldas-nsrps_fr.md) > SCanADS-SNPSR sur le Datamart du SMC

# Données du Système canadien d'assimilation de données de surface dans le Système national de prévision de surface et de rivières (SCanADS-SNPSR) en format NetCDF

Cette page décrit les données expérimentales du [Système canadien d'assimilation de données de surface](./readme_caldas-nsrps_fr.md) disponibles en format NetCDF sur le serveur DD-Alpha, le site Web d'essai de données du Datamart du SMC.

## Adresse des données 

Les données du serveur DD-Alpha, le site Web d'essai de données du Datamart du SMC, peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier netCDF. 

Les données sont accessibles à l'adresse suivante :

* [https://dd.alpha.meteo.gc.ca/model_nsrps-caldas/2.5km/{HH}/](https://dd.alpha.meteo.gc.ca/model_nsrps-caldas/2.5km)                  

où :

* __HH__ : Heure en UTC du temps de validité de l'analyse [00, 03, 06, 09, 12, 15, 18, 21]

Un historique de 24h de prévision est stocké dans ce répertoire.

## Spécification technique de la grille  

![Image du domaine SCanADS-SNPSRS](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_caldas-nsrps/grille_caldas-nsrps.png)

Valeurs données aux paramètres de la grille lat-lon tournée à 2.5km de résolution:

| Paramètre | Valeur |
| ------ | ------ |
| ni | _2578_ | 
| nj | _1328_ | 
| résolution le long de l'équateur tourné | 2.5km |


## Nomenclature des noms de fichiers 

La nomenclature des noms des fichiers est la suivante :

`{YYYYMMDD}T{HH}Z_MSC_NSRPS-CaLDAS_{VAR}_{LVLTYPE}-{LVL}_{grille}{resolution}_PT0H.nc`

où :

* __YYYYMMDD__ : Année, mois et jour du début de la prévision
* __T__ : Délimiteur temporel selon les normes ISO8601
* __HH__ : Heure en UTC du temps de validité de l'analyse [00, 03, 06, 09, 12, 15, 18, 21]
* __Z__ : Fuseau horaire (heure UTC)
* __MSC__ : Chaîne de caractères constante pour Meteorological Service of Canada, la source des données
* __NSRPS-CaLDAS__ : Chaîne de caractères constante indiquant que les données proviennent du Système canadien d'assimilation de données de surface dans le Système national de prévision de surface et de rivières (SCanADS-SNPSR)
* __VAR__ : Variables contenues dans le fichier (voir section ci-dessous).
* __LVLTYPE__ : Type de niveau vertical [Sfc pour la surface, DBS pour la profondeur sous la surface, AGL pour la hauteur au-dessus du sol]
* __LVL__ : Valeur du niveau vertical [`1.5m`; `all` regroupe tous les niveaux `0.025m, 0.075m, 0.15m, 0.3m, 0.7m, 1.5m, 2.5m`]. Ce paramètre est absent pour la surface
* __grille__ : Grille horizontale [RLatLon]
* __resolution__ : Indique la résolution en degré dans les directions longitudinale et latitudinale soit ici 0.0225(environ 2.5km) dans les deux directions
* __PT0H__ : Echéance temporelle selon la norme [ISO8601](https://en.wikipedia.org/wiki/ISO_8601). P, T et H sont des caractères constants désignant Période, Temps et Heure. Ici,PT0H indique une analyse.
* __nc__ : Chaîne de caractères constante indiquant que le format est NetCDF

Exemples :

* 20220307T00Z_MSC_NSRPS-CaLDAS_AirTemp_AGL-1.5m_RLatLon0.0225_PT0H.nc
* 20220307T00Z_MSC_NSRPS-CaLDAS_Dewpoint_AGL-1.5m_RLatLon0.0225_PT0H.nc
* 20220307T00Z_MSC_NSRPS-CaLDAS_RadiativeTemp_Sfc_RLatLon0.0225_PT0H.nc
* 20220307T00Z_MSC_NSRPS-CaLDAS_SoilLiquidWaterCont_DBS-all_RLatLon0.0225_PT0H.nc
* 20230220T00Z_MSC_NSRPS-CaLDAS_SnowDepth_Sfc_RLatLon0.0225_PT0H.nc
* 20230220T00Z_MSC_NSRPS-CaLDAS_SnowWaterEquiv_Sfc_RLatLon0.0225_PT0H.nc

## Liste des variables

Liste des variables pour chaque heure de validité de:

|Nom   | Description|  Niveau|  Unité|
|---------|---------------|----------|----------|
|tt     |Température de l'air                           |   AGL|    K|
|td      |Température du point de rosée au niveau de l'abri |   AGL|    K|
|tg      |Température radiative agrégée à la surface |   Sfc|    K|
|wsol      |Contenu volumique d'eau liquide dans le sol |   DBS|   m<sup>3</sup>/m<sup>3</sup>|
|swe      |Équivalent en eau de la neige (à la surface terrestre) |   Sfc|   kg/m<sup>2</sup>|
|sd      |Épaisseur de neige (à la surface terrestre) |   Sfc|    m|


## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).

