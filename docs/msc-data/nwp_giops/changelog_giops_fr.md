[In English](changelog_giops_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [SGPOG](readme_giops_fr.md) > Changements au SGPOG

# Chronologie des changements apportés au Système global de prévision océan-glace (SGPOG)

## Le mardi 28 novembre 2023

### Mise à jour du Système global de prévision océan-glace (SGPOG) 3.4.1 du Centre météorologique canadien (CMC)

Le mardi 28 novembre 2023, le Centre météorologique canadien (CMC) va procéder à la mise en œuvre opérationnelle de la version 3.4.1 de son Système global de prévision océan-glace (SGPOG).

Le seul changement inclus dans cette version est l’ajout d’un volet de contrôle de la qualité pour les observations "in situ" utilisées dans l’assimilation de données.

Une copie de la note officielle documentant ce changement est disponible [via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_giops-341_f.pdf).

Le document des spécifications techniques du SGPOG 3.4.1 est disponible [via ce lien]()https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_GIOPS_3.4.1_f.pdf.

## Le mardi 28 juin 2022

### Mise à jour du SGPOG à la version 3.4.0 suite à la nouvelle infrastructure de calcul haute performance. 

Voir les détails via [ce lien](../changelog_multisystems_fr.md).

## Le mercredi 1er décembre 2021

### Mise à jour du Système global de prévision océan-glace (SGPOG) 3.3.0 du Centre météorologique canadien (CMC)

Le mercredi 1er décembre 2021, le Centre météorologique canadien (CMC) va procéder à la mise en œuvre opérationnelle de la version 3.3.0 de son Système global de prévision océan-glace (SGPOG).

Les changements majeurs de cette mise à jour se résument ainsi:

* Inclusion du cycle diurne.
* Paramétrage de la rigidité de la glace.
* Coefficient de rugosité de la glace pour ajuster à la valeur utilisée dans GEM.
* Utilisation des forçages atmosphériques provenant de l'assimilation plutôt que de la prévision.
* Introduction d’un nouveau système de monitoring.


Une copie de la note officielle annonçant ce changement [est disponible via ce lien](http://dd.meteo.gc.ca/doc/genots/2021/11/26/NOCN03_CWAO_262118___50159).

Le document des spécifications techniques du SGPOG 3.3.0 [est disponible ici](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_GIOPS_3.3.0_f.pdf).

Une note technique à ce sujet [est disponible via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_giops-330_f.pdf).

## Le mardi 21 janvier 2020

### Mise à jours du SGPOG à la version 3.2.1 suite à la nouvelle infrastructure de calcul haute performance. 

Voir les détails via [ce lien](../changelog_multisystems_fr.md).

## Mercredi 3 juillet, 2019

### Mise à jour du Système global de prévision océan-glace (SGPOG) 3.0.0 du Centre météorologique canadien (CMC)

Le mercredi 3 juillet 2019, le Centre météorologique canadien (CMC) va procéder à la mise en œuvre opérationnelle de la version 3.0.0 de son Système global de prévision océan-glace (SGPOG).
Les changements majeurs de cette mise à jour se situent principalement dans la composante prévision.

* Mise à jour vers SAM2 (Système d'Assimilation Mercator).
* La nouvelle analyse de température de surface de la mer et de glace marine a une plus haute résolution (0.10 degré).


Une copie de la note officielle annonçant ce changement [est disponible via ce lien](http://dd.meteo.gc.ca/doc/genots/2019/06/28/NOCN03_CWAO_281844___55878).

Le document des spécifications techniques du SGPOG 3.0.0 [est disponible ici](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_GIOPS_3.0.0_f.pdf).

Une note technique à ce sujet [est disponible via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_giops-300_f.pdf).


## Le mercredi 1 novembre 2017

### Mise à jour du Système global de prévision océan-glace (SGPOG) 2.3 du Centre météorologique canadien (CMC)

Le mercredi 1er novembre 2017, le Centre météorologique canadien (CMC) va procéder à la mise en œuvre opérationnelle de la version 2.3 de son Système global de prévision océan-glace (SGPOG).

Les changements majeurs de cette mise à jour se situent principalement dans la composante prévision:

* Introduction d'un couplage bi-directionnel entre les composante de prévision du SGPD et du SGPOG. Ce couplage permet une interaction bi-directionnel entre le modèle atmosphérique et le modèle océan-glace, de telle sorte que l'évolution des conditions marines influence l'atmosphère dans le SGPD qui en retour influence la prévision des champs océan-glace du SGPOG.

La composante de assimilation de SGPOG n'est pas modifié de façon significative dans cette mise à jour.

L'announce officielle pour l'implantation de ces changements est incluse dans le GENOT émis pour le [SGPD 6.0.0](../nwp_gdps/changelog_gdps_fr.md).

Une note technique à ce sujet (en anglais) [est disponible via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_giops-230_e.pdf).


## Le mardi 21 juin 2016

### Mise à jour du Système Global de Prévision Océan-Glace (SGPOG) 2.1 du Centre météorologique canadien (CMC)

Le mardi 21 juin 2016, le Centre météorologique canadien (CMC) va procéder à la mise en œuvre opérationnelle de la version 2.1 de son Système Global de Prévision Océan-Glace (SGPOG).

Résumé des éléments majeurs que comporte cette mise à jour pour la composante assimilation de ce système:

* Le code source du système d'assimilation Mercator (SAM) est mis à jour à la version utilisé par le centre Mercator-Océan depuis juin 2015:
    * Approche incrémentale 4D de mise à jour de l'analyse (IAU:Incremental Analysis Update).
    * Plusieurs raffinements dans le kernel d'analyse.
* L'introduction d'une topographie dynamique moyenne (MDT) ameliorée.
* L'utilisation des observations bogus de température et de salinité dans des régions cles comme dans les eaux sous la glace marine.
* Raffinement dans l'utilisation de l'erreur d'observation de la température de la surface de la mer (sst).

La composante de prévision de SGPOG n'est pas modifié de façon significative.

La note officielle annonçant ce changement [est disponible en cliquant ici](http://dd.meteo.gc.ca/doc/genots/2016/06/21/NOCN03_CWAO_211410___00536).

Une note technique à ce sujet (en anglais) [est disponible via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_giops-210_e.pdf).


## Le jeudi 20 août 2015

### Le Centre Météorologique Canadien déclare le statut opérationnel pour le SGPOG version 1.1.1

Le jeudi 20 août 2015, le Centre Météorologique Canadien (CMC) à déclaré le statut opérationnel pour son Système Global de Prévision Océan-Glace (SGPOG) version 1.1.1.

Une copie de la note officielle annoncant ce changement [est disponible en cliquant ici](http://dd.weatheroffice.ec.gc.ca/doc/genots/2015/07/08/NOCN03_CWAO_081635___00168).

La documentation technique du système SGPOG est disponible [via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/lib/technote_giops-111_e.pdf) (en anglais, version française disponible sous peu).

Un manuel des produits du SGPOG qui contient la description des sorties du système est aussi disponible [via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/lib/product_manual_giops-111_f.pdf).



