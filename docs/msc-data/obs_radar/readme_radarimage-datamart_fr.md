[In English](readme_radarimage-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [Observations radar](readme_radar_fr.md) > Observations radar sur le Datamart du SMC

# Imagerie radar

Cette page décrit les images [radar](readme_radar_fr.md) en format GIF disponibles sur le Datamart du SMC.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le Protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier GIF.

Les images radar se trouvent à l'adresse :

* [https://dd.meteo.gc.ca/radar/{PRODUIT}/{FORMAT}/{STATION_RADAR}](https://dd.meteo.gc.ca/radar/)

où :

* PRODUIT = [24_HR_ACCUM | CAPPI | DPQPE]
* FORMAT  = [GIF] 
* STATION_RADAR   = [CASBV, CASRA, ...]  code de 5 lettres du radar, en lettres majuscules. 

Un historique de 48 heures des données est conservé dans chaque répertoire.

__Notes__: 

* Chacun de ces produits est détaillé dans la [documentation](https://www.ec.gc.ca/meteo-weather/default.asp?lang=Fr&n=2B931828-1) d'Environnement et Changement climatique Canada.
* Le produit d'estimation quantitative des précipitations à double polarisation (DPQPE) est une représentation bidimensionnelle du taux de précipitation estimé par le plus bas du balayage du radar (angle d’élévation de 0.4 degré pour la majorité des radars en bande S). Ainsi, le taux de précipitation estimé est aussi proche que possible de la surface de la terre. Le produit DPQPE est basé, entre autres, sur une série d'étapes de traitement polarimétrique (contrôle qualité) pour éliminer les artefacts non météorologiques des données brutes (balayages volumétriques). Il est fourni en mm/h pour la pluie et cm/h pour la neige. Ce produit est utilisé dans notre composite radar nord-américaine haute résolution disponible dans [MétéoCan](https://www.canada.ca/fr/environnement-changement-climatique/services/conditions-meteorologiques-ressources-outils-generaux/meteocan.html), l'application mobile officielle d'ECCC.
* Une [liste des sites radar](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_radar/radars_list.pdf) est disponible. Cette liste sera mise à jour régulièrement.

## Nomenclature des noms de fichiers 

Les noms de fichiers ont le format suivant, avec XXXXX, code de 5 lettres du radar, en lettres majuscules.

* __CAPPI__
  
La nomenclature des fichiers CAPPI est la suivante :

* `YYYMMDDHHmm_XXXXX_CAPPI_1.0_SNOW.gif`
* `YYYMMDDHHmm_XXXXX_CAPPI_1.5_RAIN.gif`
* `YYYMMDDHHmm_XXXXX_CAPPI_1.0_SNOW_A11Y.gif`
* `YYYMMDDHHmm_XXXXX_CAPPI_1.5_RAIN_A11Y.gif`

ex: 200806191550_CASFT_CAPPI_1.5_RAIN.gif

* __DPQPE__
  
La nomenclature des fichiers DPQPE est la suivante :

* `YYYYMMDDTHHmmZ_MSC_Radar-DPQPE_XXXXX_[Rain,Snow].gif`

ex: 20201106T1050Z_MSC_Radar-DPQPE_CASBE_Rain.gif

* __Produits de contingence__ 

Quand un radar canadien tombe en panne, un produit alternatif est disponible pour des fins de contingence. Il s'agit d'un produit composite généré à partir des radars voisins, qui peut contenir des radars américains. Il est également important de noter que pour certaines régions, les radars avoisinants peuvent ne pas couvrir tout le domaine du radar qui est en panne ou en entretien. À cet effet et pour aider l’usager à mieux identifier ces zones non-couvertes, des cercles de couleur rouge ont été ajoutés pour montrer les radars contributeurs qui ont servi à construire cette composite.

Ces produits sont identifiés grâce à la mention "Contingency" dans les noms de fichies pour les produits de contingence basés sur le produit DPQPE, soit:

* `YYYYMMDDTHHmmZ_MSC_Radar-DPQPE_XXXXX_[Rain,Snow]-Contingency.gif`

ex: 20240112T1636Z_MSC_Radar-DPQPE_CASET_Snow-Contingency.gif

Cette image composite peut être différenciée de celle du radar d'origine grâce à l'inscription "Composite" dans la légende à droite de l'image.

* __24_HR_ACCUM__ 

Représente l'accumulation de précipitation en mm tel qu'observée par le radar au cours des 24 dernières heures. Ce produit est disponible toutes les 6 minutes pour les radars de bande S.

* `YYYYMMDDTHHmmZ_MSC_Radar-DPQPE_XXXXX_Accum24h.gif`

ex: 20201106T1050Z_MSC_Radar-DPQPE_CASBE_Accum24h.gif

## Archive des images radar

Les images radar historiques nationales, régionales et locales du réseau de stations radar à travers le Canada sont disponibles, sans frais, à travers le site web des données climatiques historiques, à cette adresse :

[https://climate.weather.gc.ca/radar/index_f.html](https://climate.weather.gc.ca/radar/index_f.html)

## Support

Pour toute question relative à ces données, merci de [nous contacter](https://weather.gc.ca/mainmenu/contact_us_f.html).

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).
