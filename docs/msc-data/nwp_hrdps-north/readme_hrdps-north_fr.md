[In English](readme_hrdps-north_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > SHRPD-Nord

# Données et Produits du Système à haute résolution de prévision déterministe Nord

Le Système expérimental à haute résolution de prévision déterministe Nord (SHRDP-Nord) est un système de prévision expérimental basé sur une configuration à aire limitée (LAM) du modèle Global Environmental Multiscale (GEM). Il couvre l'ensemble du bassin arctique et la baie d'Hudson. La résolution de la grille horizontale est d'environ 3km avec 2250 x 1850 points de grille et 62 niveaux verticaux. Le niveau momentum le plus bas se situe à une altitude d'environ 40m. Le SHRPD-Nord 3km est piloté par le [Système global de prévision déterministe global (SGPD)](../nwp_gdps/readme_gdps_fr.md) de ECCC, qui fournit des conditions initiales et latérales pour les champs atmosphériques. Les champs hydrométéorologiques initiaux sont recyclés à partir de la prévision à 12 heures de l'intégration précédente du HRDPS-Nord. Les champs de surface pour la glace de mer et la température sont fournis par le [Système régional de prévision océan-glace (SRPOG)](../nwp_riops/readme_riops_fr.md). Le SHRPD-Nord tourne deux fois par jour sur une grille lat-lon tournée et est initialisé à 00 et 12 UTC respectivement avec une intégration de 48 heures.

Dans le cadre d’un plan de modernisation du Service Météorologique Canadien (SMC), des éléments du temps sur grille ("WEonG") cohérents, fusionnant les sorties brutes du modèle et post-traitées à l’aide de diverses approches diagnostiques sont également disponibles pour servir les différents programmes de prévision (public, maritime, aviation, qualité de l’air, etc.). Des concepts horaires sont ainsi produits à partir de différents algorithmes en utilisant des sorties provenant du SHRPD-Nord. Ces données sont également disponibles sur la grille lat-lon tournée. 

## Accès

### Comment accéder aux données

Ces données sont respectivement disponibles sur les services serveur de données [Datamart du SMC](../../msc-datamart/readme_fr.md) et les services web [GeoMet du SMC](../../msc-geomet/readme_fr.md) :

* [Données GRIB2 disponibles sur le Datamart du SMC](readme_hrdps-north-datamart_fr.md) 
* [Données disponibles via les services web géospatiaux GeoMet-Météo](../../msc-geomet/readme_fr.md)

Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est disponible.

### Licence

La [licence d’utilisation finale pour les serveurs de données d’Environnement et Changement climatique Canada](../../licence/readme_fr.md) précise les conditions d'utilisation de ces données.

### Politique d'utilisation des services de données ouvertes du SMC

La [Politique d'utilisation des services de données ouvertes du SMC](../../usage-policy/readme_fr.md) détermine ce qui constitue une utilisation appropriée des services de données ouvertes du SMC et fournit aux utilisateurs les pratiques exemplaires pour une utilisation optimale.

### Métadonnées

* A venir.
* Les [métadonnées des Éléments du temps sur grille dérivés du Système à haute résolution de prévision déterministe sont accessibles sur le portail du gouvernement ouvert](https://open.canada.ca/data/fr/dataset/9eaf8b65-a734-432e-925c-7fbe8fc65670).

## Documentation technique

* [Fiche d'information associée au dernier cycle d'innovation](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/fact_sheets/factsheet_hrdps-north_f.pdf)
* [Version actuelle du Système à haute résolution de prévision déterministe Nord](http://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_specifications/tech_specifications_HRDPS-NORTH_f.pdf)
* [Diagramme de dépendances](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwep-dependency-diagrams/system_HRDPS-N_fr.svg)
* [Note technique](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_hrdps-north_f.pdf)
* [Note technique des éléments du temps sur grille (WEonG)](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_weong-hrdps_f.pdf)

## Registre des changements 

La chronologie des changements apportés au Système à haute résolution de prévision déterministe (SHRPD) est disponible [ici](changelog_hrdps-north_fr.md).


