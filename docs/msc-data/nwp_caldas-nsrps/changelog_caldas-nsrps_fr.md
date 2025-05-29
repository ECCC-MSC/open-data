[In English](changelog_caldas-nsrps_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [SCanADS-SNPSR](readme_caldas-nsrps_fr.md) > Changements au SCanADS-SNPSR

# Chronologie des changements apportés au Système canadien d'assimilation de données de surface dans le Système national de prévision de surface et de rivières (SCanADS-SNPSR)

## Le jeudi 1er mai 2025

### Le Système canadien d'assimilation de données de surface dans le Système national de prévision de surface et de rivières (SCanADS-SNPSR) est déclaré opérationnel au Centre météorologique canadien (CMC)

En date du 1er mai 2025, le Centre météorologique canadien (CMC) du Service météorologique du Canada déclare opérationnel le Système national de prévision de surface et de rivières (SCanADS-SNPSR, v4.0.1).

## Le lundi 7 avril 2025

### Transition vers GOES19 pour les observations de la température des premiers micromètres de la couche de surface (terrestre) dans le Système national de prévision de surface et de rivières (SCanADS-SNPSR) 

Depuis le 7 avril 2025, le satellite GOES19 est opérationnel en tant que GOES-Est, remplaçant GOES16 à cette position orbitale. Suite à cette transition, CaLDAS utilise désormais les observations de GOES19 à la place de celles de GOES16. Ces observations sont assimilées à l'aide d'un filtre de Kalman d'ensemble (EnKF) afin de produire des analyses de la température des premiers micromètres de la couche de surface (terrestre).

## Le mardi 7 janvier 2025

### Introduction d'une passe de temps de coupure court dans le Système national de prévision de surface et de rivières (SCanADS-SNPSR) 

Le 7 janvier 2025, à compter de la passe 06Z, une passe de temps de coupure court a été introduite parallèlement à la passe de temps de coupure long existante. Cette amélioration permet de fournir les conditions de surface initiales plus tôt dans la journée, ce qui facilite les prévisions terrestres et hydrologiques pour les clients. La passe ajoutée utilise une coupure de données plus courte de 3 heures et est initialisée à partir de l'analyse précédente de 6 heures générée par la passe de temps de coupure long, qui fonctionne avec un délai de 7 heures (par exemple, le cycle 00 UTC commence à 07 UTC). Les évaluations montrent que cette mise à jour n'a pas d'impact sur les résultats.

## Le mardi 11 juin 2024

### Mise à jour du Système canadien d'assimilation de données de surface dans le Système national de prévision de surface et de rivières (SCanADS-SNPSR) 4.0.0 du Centre métérologique canadien

Le mardi 11 juin 2024, à compter de la passe 1200UTC, le Centre météorologique canadien (CMC) va procéder à la mise en œuvre opérationnelle de la version 4.0.0 du Système canadien d'assimilation de données de surface dans le Système national de prévision de surface et de rivières (SCanADS-SNPSR).

Principaux changements :

* Amélioration de la mise à l'échelle des données IMS
* Amélioration de la séparation entre les phases de précipitation
* Utilisation des données d'humidité relative du SHRPD plutôt que d'effectuer les calculs dans SCanADS
* Utilisation des forçages du SHRPD pour la récupération de la température de la surface (Tskin)
* Correction de biais froid pendant l’été à la surface de l'eau

Un bref résumé des innovations incluses dans cette mise à niveau et leurs impacts sur les performances se trouve [disponible ici](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/fact_sheets/factsheet_caldas-nsrps-400_f.pdf).

La note officielle annoncant cette implantation est disponible en cliquant [via ce lien](https://dd.meteo.gc.ca/doc/genots/2024/06/10/NOCN03_CWAO_101857___46443).

Le document des spécifications techniques du SCanADS-SNPSR 4.0.0 est disponible [via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_specifications/tech_specifications_CALDAS-NSRPS_4.0.0_f.pdf).

Une note technique à ce sujet est disponiblee [via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_notes/technote_caldas-nsrps-400_f.pdf).

## Le mardi 28 juin 2022

### Mise à jour du SCanADS-SNPSR à la version 3.2.0 suite à la nouvelle infrastructure de calcul haute performance. 

Voir les détails via [ce lien](../changelog_multisystems_fr.md).

## Le mercredi 1er décembre 2021

### Mise à jour du Système canadien d'assimilation de données de surface dans le Système national de prévision de surface et de rivières (SCanADS-SNPSR) 3.1.0 du Centre métérologique canadien

En date du mercredi 1er décembre 2021, le Centre météorologique canadien (CMC) va procéder à la mise à jour du Système canadien d'assimilation de données de surface dans le Système national de prévision de surface et de rivières (SCanADS-SNPSR) vers la version 3.1.0.

Un bref résumé des innovations incluses dans cette mise à niveau et de leur impact sur les performances se trouve [dans ce document](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/fact_sheets/factsheet_caldas-nsrps-310_f.pdf).

La note officielle annoncant cette implantation est disponible en cliquant [via ce lien](https://dd.meteo.gc.ca/doc/genots/2021/11/26/NOCN03_CWAO_262118___50159).






