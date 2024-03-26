[In English](readme_ciops_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > SPCOG

# Données et Produits du Système de prévision côtier océan-glace (SPCOG)

Le Système de prévision côtier océan-glace (SPCOG) effectue des prévisions de 48 heures pour l'océan et la glace marine pour différents domaines (Est, Ouest, mer de Salish) quatre fois par jour à une résolution de 1/36°. La composante de pseudo-analyse est forcée aux frontières océaniques par le [Système régional de prévision océan-glace (SRPOG)](../msc-riops/readme_ciops_fr.md) et utilise une méthode de pilotage spectral dans l'océan profond pour corriger les grandes échelles vers la solution du SRPOG. Les champs de la pseudo-analyse sont utilisés afin d'initialiser la prévision de 00Z, les prévisions des passes 06, 12 et 18Z sont initialisées à partir de fichier de redémarrage à l'heure 6 de la prévision précédente. Le forçage atmosphérique pour les deux compostantes est fourni par le [Système à haute résolution de prévision déterministe (SHRPD)](../msc-hrdpps/readme_hrdps_fr.md) combiné spatialement et temporellement avec le [Système régional de prévision déterministe (SRPD)](../msc-rdps/readme_rdps_fr.md) (pour SPCOG-Ouest) ou le [Système global de prévision déterministe (SGPD)](../msc-gdps/readme_gdps_fr.md) (pour SPCOG-Est) pour les régions qui ne sont pas couvertes par le SHRPD.

## Accès

### Comment accéder aux données

Ces données sont disponibles sur les services du serveur de données [Datamart du SMC](../../msc-datamart/readme_fr.md)  :

* [Données disponibles via les services web géospatiaux GeoMet-Météo](readme_ciops-geomet_fr.md)
* [Données NetCDF disponibles sur HPFX, le serveur alternatif du Datamart du SMC](readme_ciops-datamart_fr.md)

Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est disponible.

### Licence

La [licence d’utilisation finale pour les serveurs de données d’Environnement et Changement climatique Canada](../../licence/readme_fr.md) précise les conditions d'utilisation de ces données.

### Politique d'utilisation des services de données ouvertes du SMC

La [Politique d'utilisation des services de données ouvertes du SMC](../../usage-policy/readme_fr.md) détermine ce qui constitue une utilisation appropriée des services de données ouvertes du SMC et fournit aux utilisateurs les pratiques exemplaires pour une utilisation optimale.

### Métadonnées

* Les [métadonnées du Système de prévision côtier océan-glace pour la Côte Est du Canada (SPCOG-Est) sont accessibles sur le portail du gouvernement ouvert](https://open.canada.ca/data/fr/dataset/bfe44cce-a9c4-467f-9172-c8800b32e4ec).
* Les [métadonnées du Système de prévision côtier océan-glace pour la Côte Ouest du Canada (SPCOG-Ouest) sont accessibles sur le portail du gouvernement ouvert](https://open.canada.ca/data/fr/dataset/390abee6-4ba0-4d6e-ae79-25753d1c43f3).
* Les [métadonnées du Système de prévision côtier océan-glace pour la région de la mer des Salish (SPCOG-MerDesSalish) sont accessibles sur le portail du gouvernement ouvert](https://open.canada.ca/data/fr/dataset/cccb0064-5ab3-416a-a4f0-566b54f466f3).

## Documentation technique

* [Version actuelle du Système de prévision côtier océan-glace sur le domaine est (SPCOG-Est)](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_specifications/tech_specifications_CIOPS-EAST_f.pdf)
* [Note technique du SPCOG-Est](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_notes/technote_ciops-east_f.pdf)
* [Diagramme de dépendances du SPCOG-Est](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwep-dependency-diagrams/system_CIOPS-E_fr.svg)
* [Version actuelle du Système de prévision côtier océan-glace sur le domaine ouest (SPCOG-Ouest)](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_specifications/tech_specifications_CIOPS-WEST_f.pdf)
* [Note technique du SPCOG-Ouest](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_notes/technote_ciops-west_f.pdf)
* [Diagramme de dépendances du SPCOG-Ouest](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwep-dependency-diagrams/system_CIOPS-W_fr.svg)

## Registre des changements

La [chronologie des changements apportés au SPCOG](changelog_ciops_fr.md) est disponible.

