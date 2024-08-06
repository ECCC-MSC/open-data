[In English](changelog_ciops_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [SCPOG](readme_ciops_fr.md) > Changements au SCPOG

# Chronologie des changements apportés au Système de prévision côtier océan-glace (SPCOG)

## Le mardi 11 juin 2024

### Mise à jour du Système de prévision côtier océan-glace est (SPCOG-Est) et west (SPCOG-Ouest) du Centre météorologique canadien (CMC)

Le mardi 11 juin 2024, à compter de la passe 1200 UTC, le Centre météorologique canadien (CMC) va procéder à la mise en œuvre opérationnelle de la version 2.3.0 de ses deux Systèmes de prévision côtiers océan-glace: la fenêtre est (SPCOG-Est) et la fenêtre ouest (SPCOG-Ouest). 


**Principaux changements au système SPCOG-Est**:

* Nouvelle région de la zone de mélange dans l'estuaire supérieur
* Mise à jour de la climatologie des températures du fleuve Saint-Laurent 
* Passage au modèle CICE6
* Utilisation du schéma de rayonnement Delta Eddington 

Un résumé des innovations incluses dans cette mise à jour ainsi que leurs impacts sur la performance du système est [disponible ici](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/fact_sheets/factsheet_ciops-east-230_f.pdf). 

**Principaux changements au système SPCOG-Ouest**:

* Forcages atmosphériques provenant d'une composante du [Système global de prévision déterministe (SGPD)](../nwp_gdps/readme_gdps_en.md) à 10km de résolution horizontale.
* Passage au modèle CICE6
* Utilisation du schéma de rayonnement Delta Eddington 

Un résumé des innovations incluses dans cette mise à jour ainsi que leurs impacts sur la performance du système est [disponible ici](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/fact_sheets/factsheet_ciops-west-230_f.pdf). 


**Documents associés**:

* Une copie de la note officielle annonçant ce changement [est disponible via ce lien](https://dd.meteo.gc.ca/doc/genots/2024/06/10/NOCN03_CWAO_101857___46443).
* Le document des spécifications techniques du SPCOG-Est 2.3.0 [est disponible ici](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_CIOPS-EAST_2.3.0_f.pdf).
* Le document des spécifications techniques du SPCOG-Ouest 2.3.0 [est disponible ici](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_CIOPS-WEST_2.3.0_f.pdf).
* La note technique du SPCOG-E 2.3.0 [est disponible via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_ciops-east-230_f.pdf).
* La note technique du SPCOG-O 2.3.0 [est disponible via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_ciops-west-230_f.pdf).


## Le mardi 28 juin 2022

### Mise à jour de SPCOG à la version 2.1.0 suite à la nouvelle infrastructure de calcul haute performance. 

Voir les détails via [ce lien](../changelog_multisystems_fr.md).

## Le mercredi 1er décembre 2022

### Mise à jour du Système de prévision côtier océan-glace (SPCOG) 2.0.0 du Centre météorologique canadien (CMC)

Le mercredi 1er décembre 2021, le Centre météorologique canadien (CMC) va procéder à la mise en œuvre opérationnelle de la version 2.0.0 de ses deux Systèmes de prévision côtier océan-glace: la fenêtre est (SPCOG-E) et la fenêtre ouest (SPCOG-O). À partir de cette mise à jour, les deux systèmes SPCOG-E et SPCOG-O obtiennent le statut opérationnel.

Les changements majeurs du SPCOG-E dans cette mise à jour se résument ainsi:

* Statut opérationnel
* Réduction de la rugosité du fond marin
* Augmentation de la résolution verticale dans le haut de la colonne d'eau (de 75 à 100 niveaux)
* Réduction du paramètre de rugosité des vagues.
* Nouvelle formulation de la rugosité dû aux vagues dans le calcul de la tension de vent.
* Augmentation de la diffusivité dans l'estuaire du Saint-Laurent (à l'ouest de Tadoussac)

Le changement majeur dans SPCOG-O est l'ajout d'un sous-domaine couvrant la région de Salish Sea à 500m de résolution.

Documents associés:

* Une copie de la note officielle annonçant ce changement [est disponible via ce lien](http://dd.meteo.gc.ca/doc/genots/2021/11/26/NOCN03_CWAO_262118___50159).
* Le document des spécifications techniques du SPCOG-E 2.0.0 [est disponible ici](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_CIOPS-EAST_2.0.0_f.pdf).
* Le document des spécifications techniques du SPCOG-O 2.0.0 [est disponible ici](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_CIOPS-WEST_2.0.0_f.pdf).
* La note technique du SPCOG-E 2.0.0 [est disponible via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_ciops-east-200_f.pdf).
* La note technique du SPCOG-O 2.0.0 [est disponible via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_ciops-west-200_f.pdf).
