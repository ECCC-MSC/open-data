[In English](readme_hrdlps-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [HRDLPS](readme_hrdlps_fr.md) > SPDHRS sur le Datamart du SMC

# Données du Système de prévision déterministe à haute résolution de la surface terrestre (SPDHRS) en format NetCDF

Cette page décrit les données expérimentales du [Système de prévision déterministe à haute résolution de la surface](./readme_hrdlps_fr.md) disponibles en format NetCDF sur le serveur DD-Alpha, le site Web d'essai de données du Datamart du SMC.

## Adresse des données 

Les données du serveur DD-Alpha, le site Web d'essai de données du Datamart du SMC, peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier netCDF. 

Les données sont accessibles à l'adresse suivante :

* [https://dd.alpha.meteo.gc.ca/model_hrdlps/2.5km/{HH}/{hhh}/](https://dd.alpha.meteo.gc.ca/model_hrdlps/2.5km)                  

où :

* __HH__ : Heure en UTC du début de la simulation [00,12]
* __hhh__ : Heure de la prévision [000,001, ...,144] 

Un historique de 24h de prévision est stocké dans ce répertoire.

## Spécification technique de la grille  

![Image du domaine HRDLPS](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_hrdlps/grille_hrdlps.png) ... _To be completed_ ...

Valeurs données aux paramètres de la grille lat-lon tournée à 2.5km de résolution:

| Paramètre | Valeur |
| ------ | ------ |
| ni | _To be completed_ | 
| nj | _To be completed_ | 
| résolution à 45° N | 2.5km |


## Nomenclature des noms de fichiers 

NOTE: TOUTES LES HEURES SONT EN UTC.

La nomenclature des noms des fichiers est la suivante :

`{YYYYMMDD}T{HH}Z_MSC_HRDLPS_{VAR}_{LVLTYPE}-{LVL}_{grille}{resolution}_PT{hhh}H.nc`

où :

* __YYYYMMDD__ : Année, mois et jour du début de la prévision
* __T__ : Délimiteur temporel selon les normes ISO8601
* __HH__ : Heure UTC de la passe [00,12]
* __Z__ : Fuseau horaire (heure UTC)
* __MSC__ : Chaîne de caractères constante pour Meteorological Service of Canada, la source des données
* __HRDLPS__ : Chaîne de caractères constante indiquant que les données proviennent du Système de prévision déterministe à haute résolution de la surface
* __VAR__ : Variables contenues dans le fichier (voir section ci-dessous). Ce paramètre comprend aussi le processus statistique associé si pertinent (ex: Accum143h pour une accumulation sur 143 heures)
* __LVLTYPE__ : Type de niveau vertical [Sfc pour la surface, DBS pour la profondeur sous la surface, AGL pour la hauteur au-dessus du sol]
* __LVL__ : Valeur du niveau vertical [10m, 0.5m, 1.5m, 2m, `0-2m` de la surface à 2 mètres]. Ce paramètre est absent pour la surface
* __grille__ : Grille horizontale [RLatLon]
* __resolution__ : Indique la résolution en degré dans les directions longitudinale et latitudinale soit ici 0.0225(environ 2.5km) dans les deux directions
* __PT{hhh}H__ : Echéance temporelle selon la norme [ISO8601](https://en.wikipedia.org/wiki/ISO_8601). P, T et H sont des caractères constants désignant Période, Temps et Heure. "hhh" représente l’heure de prévision  [000,001, ...,144]
* __nc__ : Chaîne de caractères constante indiquant que le format est NetCDF

Exemples :

* 20210927T00Z_MSC_HRDLPS_AirTemp_AGL-1.5m_RLatLon0.0225_PT143H.nc
* 20210927T00Z_MSC_HRDLPS_Runoff-Accum143h_DBS-0-2m_RLatLon0.0225_PT143H.nc

## Liste des variables

Liste des variables disponibles dans les fichiers:

* __AirTemp__ : Température de l'air à 1.5 mètres en altitude (K)
* __WindU__: Composante X de la vitesse du vent à 10 mètres en altitude (m/s)
* __WindV__: Composante Y de la vitesse du vent à 10 mètres en altitude (m/s)
* __Runoff__ : Ruissellement (mm)
* ETC.... _To be completed_... See: https://eccc-msc.github.io/open-data/msc-data/nwp_wcps/readme_wcps-atm-ocean-datamart_fr/#liste-des-variables

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).
