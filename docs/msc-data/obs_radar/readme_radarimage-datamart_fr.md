[In English](readme_radarimage-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [Observations radar](readme_radar_fr.md) > Observations radar sur le Datamart du SMC

# Imagerie radar

Cette page décrit les images [radar](readme_radar_fr.md) en format GIF disponibles sur le Datamart du SMC.

Ces images servent à alimenter le site web des prévisions publiques :

[https://meteo.gc.ca/radar/index_f.html](https://meteo.gc.ca/radar/index_f.html)

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le Protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTP. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier GIF.

Les images radar se trouvent à l'adresse:

https://dd.meteo.gc.ca/radar/PRODUIT/FORMAT/RADAR/nom_du_fichier.extension

où :

* PRODUIT = [24_HR_ACCUM | CAPPI | PRECIPET]
* FORMAT  = [GIF] (d'autres formats peuvent apparaître dans le futur)
* RADAR   = [WKR, XAM, ...]  code de 3 lettres du radar, en lettres majuscules. Pour les nouveaux radars S-band, code de 5 lettres (voir section ci-dessous).

Un historique de 48 heures des données est conservé dans chaque répertoire.

__Notes__: 

* Chacun de ces produits est détaillé dans la documentation d'Environnement et changement climatique Canada à l'adresse suivante :

http://www.ec.gc.ca/meteo-weather/default.asp?lang=Fr&n=2B931828-1 

* Une [liste des sites radar](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_radar/liste_radars_2019.pdf) est disponible. Cette liste sera mise à jour régulièrement.

## Nomenclature des noms de fichiers 

NOTE: TOUTES LES HEURES SONT EN UTC.

Les noms de fichiers ont le format suivant, avec XXX, code de 3 lettres du radar, en lettres majuscules. Pour les nouveaux radars S-band, code de 5 lettres.

* __PRECIPET__
     
Des images pour des composites régionales (5 régions du Canada) et pour les radars individuels sont disponibles. Pour chaque image, deux échelles d'intensité sont disponibles. 

Composites avec une échelle d'intensité de 14 couleurs : 

* YYYMMDDHHmm_XXX_PRECIPET_RAIN_WT.gif 
* YYYMMDDHHmm_XXX_PRECIPET_SNOW_WT.gif 

   ex: 201409201350_ATL_PRECIPET_RAIN_WT.gif

Composites avec une échelle d'intensité de 8 couleurs :

* YYYMMDDHHmm_XXX_PRECIPET_RAIN_A11Y.gif 
* YYYMMDDHHmm_XXX_PRECIPET_SNOW_A11Y.gif 
 
   ex: 201409201350_ATL_PRECIPET_RAIN_A11Y.gif

Radar individuel avec une échelle d'intensité de 14 couleurs :

* YYYMMDDHHmm_XXX_PRECIPET_RAIN.gif 
* YYYMMDDHHmm_XXX_PRECIPET_SNOW.gif (14 colors for Snow)
 
   ex: 201409201400_XFT_PRECIPET_RAIN.gif

Radar individuel avec une échelle d'intensité de 14 couleurs :

* YYYMMDDHHmm_XXX_PRECIPET_RAIN_A11Y.gif 
* YYYMMDDHHmm_XXX_PRECIPET_SNOW_A11Y.gif (14 colors for Snow)
 
   ex: 201409201400_XFT_PRECIPET_RAIN_A11Y.gif

* __Produits de contingence PRECIPET__ 

Quand un radar canadien tombe en panne, un produit alternatif PRECIPET est disponible pour des fins de contingence. Il s'agit d'un produit composite généré à partir des radars voisins, qui peut contenir des radars américains. Il est également important de noter que pour certaines régions, les radars avoisinants peuvent ne pas couvrir tout le domaine du radar qui est en panne ou en entretien. À cet effet et pour aider l’usager à mieux identifier ces zones non-couvertes, des cercles de couleur rouge ont été ajoutés pour montrer les radars contributeurs qui ont servi à construire cette composite.

Ce produit contient les lettres "COMP" dans le nom de fichier, soit :

YYYMMDDHHmm_XXX_COMP_PRECIPET_RAIN.gif

ex: 201511271400_XWL_COMP_PRECIPET_RAIN.gif

Cette image composite peut être différenciée de celle du radar d'origine grâce à l'inscription "Composite" dans la légende à droite de l'image. Pour savoir comment utiliser ces images composites, vous pouvez consulter la documentation en ligne:
[http://meteo.gc.ca/radar/how-to-use_f.html#display](http://meteo.gc.ca/radar/how-to-use_f.html#display)

* __CAPPI__
  
La nomenclature des fichiers CAPPI est la suivante :

* YYYMMDDHHmm_XXX_CAPPI_1.5_RAIN_AGL.gif
* YYYMMDDHHmm_XXX_CAPPI_1.0_SNOW_AGL.gif

   ex: 200806191550_WHK_CAPPI_1.5_RAIN_AGL.gif

* __24_HR_ACCUM__ (basées sur le produit PRECIPET)

Représente l'accumulation de précipitation en mm tel qu'observée par le radar au cours des 24 dernières heures.
  
* YYYMMDDHHmm_XXX_24_HR_ACCUM_MM.gif

   ex: 200806161900_WBI_24_HR_ACCUM_MM.gif

## Au sujet des nouveaux radars à double polarisation S-Band

ECCC est en cours de remplacement de ses anciens radars C-Band avec de nouveaux radars à double polarisation S-Band. Ce projet de renouvellement des radars s'étendra sur plusieurs années et l'installation des nouveaux radars se fera progressivement(pour davantage d'information, voir la section de documentation des produits ci-dessous).

Le 1er radar a déjà été installé à Radisson (Saskatchewan) et quelques produits sont déjà disponibles. Plusieurs changements affectant les produits/usagers sont planifiés dans ce projet. Ci-dessous figurent les plus importants :

* Les produits actuels (PRECIPET, CAPPI, ...) restent les mêmes mais sont de meilleure qualité
* la résolution temporelle a été augmentée et les produits sont disponibles toutes les 6 minutes au lieu de toutes les 10 minutes (impact sur les noms de fichiers)
* L'identifiant radar (ID) de 3 lettres est remplacé par un identifiant de 5 lettres (exemple: le ID actuel du radar Radisson C-band est XRA, il est remaplcé par CASRA pour le nouveau radar)
* D'autres nouveaux produits seront développés dans le futur et rendus disponibles à l'externe

Comment va se faire la transition et quels seront les impacts sur les usagers ?

* Pour une certaine période, les produits (PRECIPET, CAPPI, ...) seront générés avec le même ID de 3 lettres (mêmes noms de fichiers) et la même fréquence (aux 10 minutes). Durant cette période, les produits seront déposés dans les mêmes répertoires (ex: [http://dd.meteo.gc.ca/radar/PRECIPET/GIF/XRA](http://dd.meteo.gc.ca/radar/PRECIPET/GIF/XRA)). Cela facilitera la transition.
* En parallèle, les nouveaux produits avec le nouvel ID de 5 lettres seront disponibles aux 6 minutes dans les nouveaux répertoires respectifs (ex: http://dd.meteo.gc.ca/radar/PRECIPET/GIF/CASRA).
* Les usagers seront informés lorsque les nouveaux radars seront installés et leurs produits disponibles selon le processus décrit ci-dessus.

Exemple (cas du radar Radisson) :

* __Produit avec l'ID de 3 lettres aux 10 minutes (temporaire)__ : [https://dd.meteo.gc.ca/radar/PRECIPET/GIF/XRA](https://dd.meteo.gc.ca/radar/PRECIPET/GIF/XRA)
* __Produit avec l'ID de 5 lettres aux 6 minutes (permanent)__ : [https://dd.meteo.gc.ca/radar/PRECIPET/GIF/CASRA](https://dd.meteo.gc.ca/radar/PRECIPET/GIF/CASRA)

## Archive des images radar

Les images radar historiques nationales, régionales et locales du réseau de stations radar à travers le Canada sont disponibles, sans frais, à travers le site web des données climatiques historiques, à cette adresse:

http://climate.weather.gc.ca/radar/index_f.html

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).






