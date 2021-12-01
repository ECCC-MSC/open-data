[In English](readme_rdsps_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > SRPDOT

# Données et Produits du Système régional de prévision déterministe d'onde de tempête (SRPDOT)

Le Système régional de prévision déterministe d'onde de tempête (SRPDOT) produit les prévisions de niveaux d'eau en utilisant le modèle d'océan DalCoast. DalCoast (Bernier and Thompson 2015) est un sytème de prévision d'onde de tempête pour la côte est du Canada basé sur la version moyennée en profondeur, barotrope et linéarisée du Modèle d'Océan de Princeton (POM). Le modèle est forcé par les vents à une élévation de 10 mètres et la pression au niveau de la mer du [Système global de prévision déterministe (SGPD)](../nwp_gdps/readme_gdps_fr.md).

Lors du post-traitement, le niveau d'eau associé à la marée est prévu en utilisant Webtide (Dupont et al., 2002). Le niveau d'eau associé à la marée (SSHT) de Webtide et le niveau d'eau associé à l'onde de tempête (ETAS) de Dalcoast sont additionnés pour obtenir un estimé du niveau d'eau total (SSH).

## Accès

### Comment accéder aux données

Ces données sont disponibles sur le serveur de données [Datamart du SMC](../../msc-datamart/readme_fr.md):

* [Données NetCDF disponibles sur le Datamart du SMC](readme_rdsps-datamart_fr.md)

Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est disponible.

### Licence

La [licence d’utilisation finale pour les serveurs de données d’Environnement et Changement climatique Canada](../../licence/readme_fr.md) précise les conditions d'utilisation de ces données.

### Métadonnées

À venir.

## Documentation technique

* [Version actuelle du Système régional de prévision déterministe d'onde de tempête](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_specifications/tech_specifications_RDSPS_f.pdf)
* [Note technique](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_notes/technote_rdsps_f.pdf)

## Registre des changements

La chronologie des changements apportés au Système régional de prévision déterministe d'onde de tempête (SRPDOT) est disponible [ici](changelog_rdsps_fr.md).
