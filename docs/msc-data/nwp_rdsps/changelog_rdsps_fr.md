[In English](changelog_rdsps_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [SRPDOT](readme_rdsps_fr.md) > Changements au SRPDOT

# Chronologie des changements apportés au Système régional de prévision déterministe d’onde de tempête (SRPDOT)

## Le jeudi 31 mars 2022

### Fin du service pour le Système régional de prévision déterministe d'onde de tempête (SRPDOT)

Le jeudi 31 mars, le Système régional de prévision déterministe d'onde de tempête (SRPDOT), opérationnel depuis novembre 2017, est retiré de la production opérationnelle du Centre météorologique canadien (CMC). Tel qu'annoncé en décembre 2021, ce système est remplacé par le [Systeme global de prévision déterministe d'onde de tempête (SGPDOT)](/../nwp_gdsps/readme_gdsps_fr.md).

[Note officielle](https://dd.meteo.gc.ca/doc/genots/2022/03/29/NOCN03_CWAO_291746___07122) 

## Le mercredi 1er décembre 2021

### Remplacement du Système régional de prévision déterministe d’onde de tempête (SRPDOT) du Centre météorologique canadien (CMC)

Le mercredi 1er décembre 2021, à compter de la passe de 1200 UTC, le Centre météorologique canadien (CMC) va remplacer le Système régional de prévision déterministe d'onde de tempête (SRPDOT) par le nouveau Systeme global de prévision déterministe d'onde de tempête (SGPDOT). SRPDOT va passer a sa version 1.9.0 et cette mise à jour va inclure l'utilisation de la version v8.0.0 de SGPD.

Notes :

* [Note officielle](http://dd.meteo.gc.ca/doc/genots/2021/11/26/NOCN03_CWAO_262118___50159).
* [Spécifications techniques du RDSPS 1.9.0](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_RDSPS_1.9.0_f.pdf).

## Le mardi 12 janvier 2021

### Mise à jour vers la version 1.8.0 du Système régional de prévision déterministe d’onde de tempête (SRPDOT) au Centre météorologique canadien (CMC)

Ajout d'une composante de post-traitement pour fournir une prévision de niveau d'eau associé à la marée produits par Webtide.

Pour plus d'informations, veuillez consulter le document des spécifications techniques pour le SRPDOT 1.8.0 qui est disponible [via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_specifications/tech_specifications_RDSPS_1.8.0_f.pdf).

## Le mardi 21 janvier 2020

### Mise à jour du SRPDOT à la version 1.7.0 suite à la nouvelle infrastructure de calcul haute performance.

Voir les détails via [ce lien](../changelog_multisystems_fr.md).

## Le mercredi 3 juillet 2019

### Mise à jour vers la version 1.6.0 du Système régional de prévision déterministe d’onde de tempête (SRPDOT) au Centre météorologique canadien (CMC)

En date du mercredi 3 juillet 2019, le Centre météorologique canadien (CMC) va procéder à la mise en œuvre opérationnelle du Système régional de prévision déterministe d’onde de tempête (SRPDOT) vers la version 1.6.0.

Les modifications au SRPDOT v1.6.0 comparativement au précédent système opérationnel sont résumées comme suit :

* Le [SGPD v7.0.0](/../nwp_gdps/changelog_gdps_fr.md) remplace le SGPD v6.0.0 comme modèle pilote.

Pour plus d'informations, veuillez consulter le document des spécifications techniques pour le SRPDOT 1.6.0 qui est disponible [via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_specifications/tech_specifications_RDSPS_1.6.0_f.pdf).

Une note technique avec plus de détails sur ces changements est disponible [sur cette page](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_notes/technote_rdsps-160_f.pdf).

## Le mercredi 30 janvier 2019

### Mise à jour du Système régional de prévision déterministe d’onde de tempête (SRPDOT) au Centre météorologique canadien (CMC)

En date du 30 janvier, le Centre météorologique canadien (CMC) va procéder à la mise en œuvre opérationnelle de la version 1.5.0 de son Système régional de prévision déterministe d’onde de tempête (SRPDOT).

Les modifications au SRPDOT v1.5.0 comparativement au précédent système opérationnel sont résumées comme suit :

* La remplacement de la pression de surface comme variable d'entrée par la pression moyenne au niveau de la mer.
* L'inclusion d'un processus correctif pour mettre à niveau la prévision d'onde de tempête qui est sortie directement par le modèle.

Pour plus d'informations, veuillez consulter le document des spécifications techniques pour le SRPDOT 1.5.0 qui est disponible [via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_specifications/tech_specifications_RDSPS_1.5.0_f.pdf).

## Le mercredi 1er novembre 2017

### Le Système régional de prévision déterministe d’onde de tempête (SRPDOT) est déclaré opérationnel au Centre météorologique canadien (CMC)

En date du 1er novembre 2017, suite à deux ans d’exécution en mode expérimental, le CMC a déclaré opérationnel le Système régional de prévision déterministe d’onde de tempête (SRPDOT v1.3.0).

Le SRPDOT fournit des prévisions d’onde de tempête le long du littoral Atlantique du Canada. Les prévisions sont émises deux fois par jour à 00 et 12 UTC et couvrent une période de 10 jours. Des vents et la pression de surface horaires pour la prévision sont fournis par le Système global de prévision déterministe (SGPD). Les produits du SRPDOT sont générés sur une grille latitude-longitude de 1/30 degrés de résolution couvrant de 42N à 60N et de 72W à 44W.

Le SRPDOT a été développé en partenariat avec Dalhousie University. Il est basé sur le modèle d’onde de tempête Dalcoast5.

Un article scientifique (en anglais) qui contient plus de détails est [disponible ici](https://www.sciencedirect.com/science/article/pii/S1463500314001772).

Le document des spécifications techniques du SRPDOT 1.3.0 est [disponible ici](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_specifications/tech_specifications_RDSPS_1.3.0_f.pdf).
