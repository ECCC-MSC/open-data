[In English](readme_vertical-profiles-obs-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [Observations des profils verticaux](readme_vertical-profiles-obs_fr.md) > Observations des profils verticaux sur le Datamart du SMC

# Données d'observations des profils verticaux

Cette page décrit les données de [profils verticaux d'observations](readme_vertical-profiles-obs_fr.md) disponibles sur le Datamart du SMC. Les données observées (ObsTephi) contiennent les données réelles à tous les niveaux mesurées par le ballon de sondage.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le Protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier CSV.

Les profils verticaux observés sont disponibles à cette adresse :

[https://dd.meteo.gc.ca/vertical_profile/observation/csv/](https://dd.meteo.gc.ca/vertical_profile/observation/csv/)

Un historique de 24 heures des données est conservé dans ce répertoire.

## Nomenclature des noms de fichiers 

NOTE: TOUTES LES HEURES SONT EN UTC.
 
Les noms de fichiers suivent la nomenclature suivante :

ObsTephi_HH_AAAA.csv

où :

* __HH__ : Heure  de la passe. Peut être "00" ou "12".
* __AAAA__ : Code de la station de 4 lettres. La [liste complète des stations](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/prev_vertical-profiles/station_list_for_vertical_profile.geojson) est disponible.

Exemple :

ObsTephi_12_WASA.csv

## Description des données

Les données fournies, ainsi que les unités de mesure sont les suivantes :

* __TT__ : Température  (°C)
* __ES__ : Dépression du point de rosée (°C)
* __WD__ : Direction du vent  (degrés vrais)
* __UV__ : Vitesse du vent (noeuds)
* __HR__ : Humidité relative (fraction décimale; ex.  .58 = 58%) 
* __GZ__ : Hauteur géopotentielle (decamètres avec 2 décimales)
* __WW__ : Mouvement vertical (Pa/sec)

Ces données sont disponibles sur les niveaux de pression suivants :

* Niveau de surface
* GZ, ES, UV, WD, HR et TT disponibles à: SFC 1000 985 970 950 925 900 875 850 800 750 700 650 600 550 500 450 400 350 300 275 250 225 200175  150 100  70  50  30  20  10 mb
* WW disponibles pour 29 niveaux (pas à 70, 30 ou 20 mb)

__Note__ : Certains des niveaux de pression peuvent être sous l'élévation de la station.

## Note 

Bien que Environnement et Changement climatique Canada ne fournisse pas de logiciels d'affichage afin de visualiser les données de façon graphique (style téphigramme), certains usagers utilisent les logiciels suivants :

* [Buffkit](https://training.weather.gov/wdtd/tools/BUFKIT/index.php)
* [RAOB de la compganie Environmental Research Services](https://www.raob.com/)
* [NCAR Command Language](https://www.ncl.ucar.edu/get_started.shtml)

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).