[In English](readme_gdsps_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > SGPDOT

# Données et Produits du Système global de prévision déterministe d'onde de tempête (SGPDOT)

Le Système global de prévision déterministe d'onde de tempête (SGPDOT) produit les prévisions de niveaux d'eau en utilisant une version barotrope du modèle d'océan NEMO (Wang et al. 2021). Il fournit des prévisions de 240 heures, 2 fois par jour, sur une grille de 1/12° de degré (3-9 km). Le modèle est forcé par les vents à une élévation de 10 mètres et la pression au niveau de la mer du [Système global de prévision déterministe (SGPD)](../nwp_gdps/readme_gdps_fr.md).

En post-traitement, le niveau d'eau associé à l'onde de tempête est dérivé à partir du niveau d’eau total par analyse harmonique en utilisant t_tide (Pawlowicz et al. 2002).

## Accès

### Comment accéder aux données

Ces données sont disponibles sur le serveur de données [Datamart du SMC](../../msc-datamart/readme_fr.md):

* [Données NetCDF disponibles sur le Datamart du SMC](readme_gdsps-datamart_fr.md)

Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est disponible.

### Licence

La [licence d’utilisation finale pour les serveurs de données d’Environnement et Changement climatique Canada](../../licence/readme_fr.md) précise les conditions d'utilisation de ces données.

### Politique d'utilisation des services de données ouvertes du SMC

La [Politique d'utilisation des services de données ouvertes du SMC](../../usage-policy/readme_fr.md) détermine ce qui constitue une utilisation appropriée des services de données ouvertes du SMC et fournit aux utilisateurs les pratiques exemplaires pour une utilisation optimale.

### Métadonnées

À venir.

## Documentation technique

* [Version actuelle du Système global de prévision déterministe d'onde de tempête](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_specifications/tech_specifications_GDSPS_f.pdf)
* [Note technique](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_notes/technote_gdsps_f.pdf)
* [Diagramme de dépendance](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwep-dependency-diagrams/system_GDSPS_fr.svg)

## Registre des changements

La chronologie des changements apportés au Système global de prévision déterministe d'onde de tempête (SGPDOT) est disponible [ici](changelog_gdsps_fr.md).
