[In English](changelog_ohps_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > Changements au SHOP

# Chronologie des changements apportés au Système de simulation hydrodynamique opérationnelle (SHOP)

## Le mardi 11 juin 2024

### Mise à jour du Système de simulation hydrodynamique opérationnelle (SHOP) 3.4.0 du Centre météorologique canadien (CMC)

Le mardi 11 juin 2024, le Centre météorologique canadien (CMC) va procéder à la mise en œuvre opérationnelle de la version 3.4.0 de son Système de simulation hydrodynamique opérationnelle (SHOP).

Principaux changements :

*  Remplacement de la prévision actuelle de l'onde de tempête basée sur l'ajustement sinusoïdal par un signal d'onde de tempête plus réaliste prévu par le Système régional de prévision d'ensemble d'ondes de tempête (SRPEOT) pour calculer la condition limite en aval 
*  Mise à jour du traitement des observations manquantes pour garantir l'utilisation des données au moment approprié de leur validité

Un résumé des innovations incluses dans cette mise à jour ainsi que de leurs impacts sur la performance du système est [disponible ici](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/fact_sheets/factsheet_shop-340_f.pdf).

Une copie de la note officielle annonçant ce changement est disponible [via ce lien](http://dd.meteo.gc.ca/doc/genots/2024/06/11/NOCN03_CWAO_262118___xxxxx).

Le document des spécifications techniques du SHOP 3.4.0 est disponible [via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_SHOP_3.4.0_f.pdf).

Une note technique à ce sujet est disponible [via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_shop-340_f.pdf).

## Le mercredi 20 septembre 2023

### Le Système de simulation hydrodynamique opérationnelle (SHOP) 3.3.0 est déclaré opérationnel au Centre météorologique canadien

À compter du 20 septembre 2023, le Centre météorologique canadien (CMC) d'Environnement et Changement climatique Canada déclare opérationnel le Système de simulation hydrodynamique opérationnelle (SHOP v3.3.0), suite à sa période de statut expérimental depuis 2013.

Une copie de la note officielle annonçant la mise en œuvre de ces changements est disponible [via ce lien](https://dd.meteo.gc.ca/doc/genots/2023/09/19/NOCN03_CWAO_191340___27844)

## Le jeudi 3 août 2023

### Passage à la version 3.3.0 du Système de simulation hydrodynamique opérationnelle (SHOP) au Centre météorologique canadien

À compter du 3 août 2023, le Centre météorologique canadien (CMC) d'Environnement et Changement climatique Canada met à jour le Système de simulation hydrodynamique opérationnelle (SHOP) à la version 3.3.0.

Afin de préparer la demande de statut opérationnel de SHOP, les deux changements scientifiques suivants sont mis en œuvre dans cette version :

* Remplacement des sources de décharge SPHD (expérimental) par SPCE (opérationnel) pour générer des conditions limites de décharge prévisionnelles pour SHOP.
* Remplacement des dépendances sur SCanADS-SNPSR (expérimental) et SNPSR-SPDHRS (expérimental) par les dépendances sur le SHRPD (opérationnel) dans le module Précipitation-Evaporation de SHOP.

Une note technique contenant plus de détails sur la version 3.3.0 de ce système est disponible [via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_shop-330_e.pdf).

Le diagramme de dépendance mis à jour est disponible [via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwep-dependency-diagrams/system_NSRPS-OHPS_fr.svg).

## Le mardi 28 juin 2022

### Mise à jour de SHOP à la version 3.1.0 suite à la nouvelle infrastructure de calcul haute performance 

Voir les détails via [ce lien](../changelog_multisystems_fr.md).

## Le mercredi 1er décembre 2021

### Mise à jour du Système de simulation hydrodynamique opérationnelle (SHOP) 3.0.0 du Centre météorologique canadien

En date du mercredi 1er décembre 2021, le Centre météorologique canadien (CMC) va procéder à la mise à jour du Système de simulation hydrodynamique opérationnelle (SHOP) vers la version 3.0.0.

Les modifications au SHOP v3.0.0 comparativement au précédent système opérationnel sont résumées comme suit:

* Nouvelles conditions aux frontières harmoniques
* Le débit provient maintenant du SPHD (Système de prévision hydrologique déterministe)
   * Auparavant, il provenait du Système de prévision du cycle de l'eau (SPCE)
* La correction du biais du débit a été retirée
* La température de surface provient maintenant du Système canadien d'assimilation de données de surface (CaLDAS), plutôt que de l'Analyse régionale déterministe de précipitation (ARDP-CaPA)

La note officielle annoncant cette implantation est disponible en cliquant [via ce lien](https://dd.meteo.gc.ca/doc/genots/2021/11/26/NOCN03_CWAO_262118___50159).

## Le lundi 13 mai 2013

### Le CMC implante version 1.0.0 du Système de simulation hydrodynamique opérationnel (SHOP)

Le lundi 13 mai 2013, le CMC a implanté le système de simulation hydrodynamique opérationnel (SHOP) version 1.0.0 qui produira une fois par jour une analyse de la portion du fleuve St-Laurent entre le port de Montréal et Trois-Rivières. Vous pouvez consulter la page d'information de SHOP dans le guide de produits du CMC [via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/submenus/shop_f.html) pour plus d'informations.
