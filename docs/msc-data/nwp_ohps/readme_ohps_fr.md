[In English](readme_ohps_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > SHOP

# Données et Produits du Système de simulation hydrodynamique opérationnelle (SHOP)

Le Système de simulation hydrodynamique opérationnelle (SHOP) est un système de prévision hydrodynamique 2D pour le fleuve Saint-Laurent et son estuaire fluvial. Il permet de mieux comprendre les flux ayant un impact sur l'écosystème du Saint-Laurent et sert d'outil d'aide à la décision pour la gestion intégrée du Saint-Laurent. Trois composantes sont intégrées au système SHOP. La première, "steadysol", effectue des analyses quotidiennes de l'écoulement en régime permanent, 4 fois par jour à 00Z, 06Z, 12Z et 18Z respectivement, sur un domaine de simulation s'étendant de Montréal à Trois-Rivières. Les deuxième et troisième composantes, soit "analysis" et "forecast", fournissent des analyses continues et des prévisions sur 48 heures, respectivement, pour les écoulements instationnaires sur un domaine étendu du Saint-Laurent dont les limites amont se situent à Carillon et Beauharnois alors que la limite de marée aval est près de Saint-Joseph-de-la-Rive, respectivement, 4 fois par jour à 00Z, 06Z, 12Z et 18Z. Le système fournit des résultats à haute résolution pour divers paramètres tels que les niveaux d'eau, les vitesses moyennées sur la profondeur et les attributs dérivés, sur les domaines simulés. Les produits sont disponibles au format NetCDF, qui fournit des ensembles de données. Les jeux de données publiés de la composante "steadysol" sont sur un maillage triangulaire irrégulier, tandis que les jeux de données des composantes  "analysis" et "forecast" sont sur une grille stéréographique polaire.

## Accès

### Comment accéder aux données

Ces données sont disponibles sur les services du serveur de données [Datamart du SMC](../../msc-datamart/readme_fr.md):

* [Données NetCDF disponibles sur le Datamart du SMC](readme_ohps-datamart_fr.md) 

Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est disponible.

### Licence

La [licence d’utilisation finale pour les serveurs de données d’Environnement et Changement climatique Canada](../../licence/readme_fr.md) précise les conditions d'utilisation de ces données.

### Politique d'utilisation des services de données ouvertes du SMC

La [Politique d'utilisation des services de données ouvertes du SMC](../../usage-policy/readme_fr.md) détermine ce qui constitue une utilisation appropriée des services de données ouvertes du SMC et fournit aux utilisateurs les pratiques exemplaires pour une utilisation optimale.

### Métadonnées de découverte

A venir

## Documentation technique

* [Version actuelle du Système de simulation hydrodynamique opérationnelle (SHOP)](http://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_specifications/tech_specifications_SHOP_f.pdf)
* [Note technique](http://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_notes/technote_shop_f.pdf)
* [Diagramme de dépendances](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwep-dependency-diagrams/system_NSRPS-OHPS_fr.svg)
* [Fiche d'information associée au dernier cycle d'innovation](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/fact_sheets/factsheet_shop_f.pdf)

## Registre des changements 

La chronologie des changements apportés au Système de simulation hydrodynamique opérationnelle (SHOP) est disponible [ici](changelog_ohps_fr.md).
