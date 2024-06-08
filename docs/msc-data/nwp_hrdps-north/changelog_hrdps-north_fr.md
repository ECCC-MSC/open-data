[In English](changelog_hrdps-north_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [SHRPD-Nord](readme_hrdps-north_fr.md) > Changements au SHRPD Nord

# Chronologie des changements apportés au Système à haute résolution de prévision déterministe nord (SHRPD-Nord)

## Le mardi 11 juin 2024

### Mise à jour vers la version 2.1.0 du Système à haute résolution de prévision déterministe nord (SHRPD-Nord) au Centre météorologique canadien (CMC)

 
Le mardi 11 juin 2024, à compter de la passe de 1200 UTC, le Centre météorologique canadien (CMC) mettra à jour le Système à haute résolution de prévision déterministe ouest (SHRPD-Nord) à la version 2.1.0.

Principaux changements :

* Mise à jour vers la version 5.2.1 de GEM, améliorant la physique atmosphérique et les performances du modèle. 
* Approche de Bourgouin pour partitionner la phase des précipitations en surface.  
* Améliorations aux conditions initiales et frontières provenant du [SGPD à 10 km](../nwp_gdps/readme_gdps_fr.md). 
* Mise à jour des conditions initiales de la glace de mer à partir du SRPOG, fournissant des données plus précises sur la glace de mer. 
* Mise en œuvre du système de coordonnées verticales SLEVE

Un résumé des innovations incluses dans cette mise à jour ainsi que de leurs impacts sur la performance du système est disponible ici: [SHRPD-Nord_2.1.0_innovations](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/fact_sheets/factsheet_hrdps-north-210_f.pdf).

La note officielle annonçant ce changement est disponible [via ce lien](http://dd.meteo.gc.ca/doc/genots/2024/06/11/NOCN03_CWAO_262118___xxxxx).

Une note technique à ce sujet est disponible [via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_hrdps-north-210_f.pdf).

Le document des spécifications techniques du SHRPD-Nord 1.0.0 est disponible [via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_HRDPS-NORTH_2.1.0_f.pdf).



## Le mercredi 30 août 2023

### Mise à jour à la version 2.0.0 du Système à haute résolution de prévision déterministe pour le nord (SHRPD-N) au Centre météorologique canadien

Le mercredi 30 août 2023, à partir de la passe de 1200 UTC, le Centre météorologique canadien (CMC) mettra à jour le Système à haute résolution de prévision déterministe pour le nord (SHRPD-N) à la version 2.0.0.

Les principaux changements inclus dans cette mise à jour sont résumés ci-dessous :

* Champs calculés sur un domaine beaucoup plus large
* Les conditions initiales et de frontières latérales pour l'atmosphère proviennent de la dernière version opérationnelle du Système global de prévision déterministe (SGPD) dont les détails sont disponibles [via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_GDPS_8.0.0_f.pdf) 
* Les conditions initiales océaniques sont fournies par le Système régional de prévision océan-glace (SRPOG) dont les détails sont disponibles [via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_RIOPS_2.2.0_f.pdf)

La note officielle annonçant la mise en place de ces changements est disponible [via ce lien](https://dd.meteo.gc.ca/doc/genots/2023/08/29/NOCN03_CWAO_292016___46915). 

Une note technique avec plus de détails sur le SHRPD-N 2.0.0 est disponible [via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_notes/technote_hrdps-north-200_f.pdf).

Le document de spécifications techniques du SHRPD-N 2.0.0 est disponible [via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_specifications/tech_specifications_HRDPS-NORTH_2.0.0_f.pdf).

## Le mardi 28 juin 2022

### Mise à jour du SHRPD-N à la version 1.2.0 suite à la nouvelle infrastructure de calcul haute performance. 

Voir les détails via [ce lien](../changelog_multisystems_fr.md).

## Le mercredi 1er décembre 2021

### Mise à jour vers la version 1.0.0 du Système à haute résolution de prévision déterministe nord (SHRPD-N) au Centre météorologique canadien (CMC)

Le mercredi 1er décembre 2021, à compter de la passe de 1200 UTC, le Centre météorologique canadien (CMC) retirera le Système canadien de prévision de l'Artique ([SCPA](../nwp_caps/readme_caps_fr.md)) qui sera remplacé par le Système à haute résolution de prévision déterministe nord (SHRPD-N) version 1.0.0.

Voici un résumé des innovations:

* Retrait du couplage océan-glace (le SCPA était couplé).
* Migration à GEM 5.1 avec retro physique.
* Configuration similaire au SHRPD National.
* Mise à jour des champs géophysiques.
* Nouveau modèle pilote: SRPD National [version 8.0.0](../nwp_rdps/changelog_rdps_fr.md#le-mercredi-1er-decembre-2021).

La note officielle annonçant ce changement est disponible [via ce lien](http://dd.meteo.gc.ca/doc/genots/2021/11/26/NOCN03_CWAO_262118___50159).

Une note technique à ce sujet est disponible [via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_hrdps-north-100_f.pdf).

Le document des spécifications techniques du SHRPD-N 1.0.0 est disponible [via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_HRDPS-NORTH_1.0.0_f.pdf).

