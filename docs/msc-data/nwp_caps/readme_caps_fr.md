[In English](readme_caps_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > SCPA expérimental

# Données et Produits du Système canadien de prévision de l'Arctique (SCPA) expérimental

Le Système canadien de prévision de l'Arctique (SCPA) est un système de prévision couplé experimental atmosphère-océan-glace basé sur une configuration à aire limitée (LAM) du modèle Global Environmental Multiscale (GEM), couplé au Nucleus of European Modeling of the Ocean (NEMO) et le Community ICe Code (CICE). Il couvre l'ensemble du bassin arctique avec une résolution de la grille horizontale d'environ 3km. Le SCPA est piloté par le [Système global de prévision déterministe (SGPD)](../nwp_gdps/readme_gdps_fr.md) de ECCC, qui fournit des conditions initiales et latérales pour les champs atmosphériques. Les champs hydrométéorologiques initiaux sont recyclés à partir de la prévision à 12 heures de l'intégration précédente du SCPA. De plus, le SGPD est utilisé pour forcer le modèle océan-glace en dehors des régions couplées. Les conditions initiales pour les champs océan-glace sont pris du [Système Régional de Prévision Océan-Glace (SRPOG)](../nwp_riops/readme_riops_fr.md). Les conditions frontières océaniques dans l'Atlantique Nord et le Pacifique Nord viennent du SGPD. Le SCPA tourne deux fois par jour et est initialisé à 00 et 12 UTC respectivement avec une intégration de 48 heures

## Accès

### Comment accéder aux données

Ces données expérimentales sont respectivement disponibles via l'API / les services web [GeoMet du SMC](../../msc-geomet/readme_fr.md) et le serveur de données [Datamart du SMC](../../msc-datamart/readme_fr.md) :

* [Données disponibles via les services web géospatiaux GeoMet-Météo](https://eccc-msc.github.io/open-data/msc-geomet/readme_fr/)
* [Données GRIB2 et NetCDF disponibles sur le Datamart du SMC](readme_caps-datamart_fr.md)
* [Données GRIB2 d'éléments du temps sur grille disponibles sur DD-Alpha, le site Web d'essai de données du Datamart du SMC](readme_caps-weong-datamart_fr.md)

Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est disponible.

### Licence

La [licence d’utilisation finale pour les serveurs de données d’Environnement et Changement climatique Canada](../../licence/readme_fr.md) précise les conditions d'utilisation de ces données.

### Politique d'utilisation des services de données ouvertes du SMC

La [Politique d'utilisation des services de données ouvertes du SMC](../../usage-policy/readme_fr.md) détermine ce qui constitue une utilisation appropriée des services de données ouvertes du SMC et fournit aux utilisateurs les pratiques exemplaires pour une utilisation optimale.

### Métadonnées

À venir.

## Documentation technique

* [Version actuelle du Système canadien de prévision de l'Arctique](http://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_specifications/tech_specifications_CAPS_f.pdf)
* [Diagramme de dépendances](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwep-dependency-diagrams/system_CAPS_fr.svg)
* [Note technique](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_caps_f.pdf)
* [Note technique des éléments du temps sur grille (WEonG)](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_weong-hrdps_f.pdf)

## Registre des changements 

La chronologie des changements apportés au Système canadien de prévision de l'Arctique (SCPA) est disponible [ici](changelog_caps_fr.md).

