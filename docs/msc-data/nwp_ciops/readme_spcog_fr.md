[In English](readme_ciops_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > SPCOG

# Données et Produits du Système de prévision océan-glace côtier (SPCOG)

Les Systèmes de prévision côtière océan-glace (SPCOG) effectuent des prévisions de 48 heure pour l'océan et la glace marine (uniquement pour SPCOG-Est) quatre fois par jour à une résolution de 1/36°. La composante de pseudo-analyse est forcée aux frontières océaniques par le système régional de prévision océan-glace (SRPOG) et utilise une méthode de pilotage spectral dans l'océan profond pour corriger les grandes échelles vers la solution du SRPOG. Les champs de la pseudo-analyse sont utilisés afin d'initialiser la prévision de 00Z, les prévision des 06, 12 et 18Z sont initialisées à partir de fichier de redémarrage à l'heure 6 de la prévision précédente. Le forçage atmosphérique pour les deux compostantes est fourni par le système à haute résolution de prévision déterministe (SHRPD) combiné spatialement et temporellement avec le système régional de prévision déterministe (pour SPCOG-Ouest) ou le système global de prévision déterministe (pour SPCOG-Est) pour les région qui ne sont pas couvertes par le SHRDP.    

## Accès

### Comment accéder aux données

Ces données sont disponibles sur les services du serveur de données [Datamart du SMC](../../msc-datamart/readme_fr.md)  :

* [Données NEMO du système de prévision cotière océan-glace (SPCOG) en format NetCDF disponibles sur le Datamart du SMC](readme_spcog-datamart_fr.md)

Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est disponible.

### Licence

La [licence d’utilisation finale pour les serveurs de données d’Environnement et Changement climatique Canada](../../licence/readme_fr.md) précise les conditions d'utilisation de ces données.

### Politique d'utilisation des services de données ouvertes du SMC

La [Politique d'utilisation des services de données ouvertes du SMC](../../usage-policy/readme_fr.md) détermine ce qui constitue une utilisation appropriée des services de données ouvertes du SMC et fournit aux utilisateurs les pratiques exemplaires pour une utilisation optimale.

### Métadonnées

À venir.

## Documentation technique

* [Version actuelle du SPCOG-Est](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_specifications/tech_specifications_CIOPS-EAST_f.pdf)
* [Version actuelle su SPCOG-Ouest](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_specifications/tech_specifications_CIOPS-WEST_f.pdf)
* [Note technique du SPCOG-Est](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_notes/technote_ciops-east_f.pdf)
* [Note technique du SPCOG-Ouest](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_notes/technote_ciops-west_f.pdf)

## Registre des changements 

La [chronologie des changements apportés au SPCOG)](changelog_ciops_fr.md) est disponible.

