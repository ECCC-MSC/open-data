[In English](changelog_wcps_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [SPCE](readme_wcps_fr.md) > Changements au SPCE

# Chronologie des changements apportés au Système de prévision du cycle de l'eau (SPCE)

## Le jeudi 24 février 2022

### Mise à jour du Système de prévision du cycle de l'eau (SPCE) 3.1.0 du Centre météorologique canadien

En date du jeudi 24 février 2021, le Centre météorologique canadien (CMC) va procéder à la mise à jour du Système de prévision du cycle de l'eau (SPCE) vers la version 3.1.0.

Les modifications au SPCE v3.1.0 comparativement au précédent système opérationnel sont résumées comme suit:

* Pour les composantes pseudo-analyse/prévision :
    * La charge de glace sur les Grands Lacs est correctement implantée dans la pseudo-analyse
    * Les connecteurs de rivière entre les lacs Huron et St-Claire ont été révisés pour corriger certains débits manquants
    * Les régions de mélange artificiellement augmenté ont été révisés pour améliorer le mélange devant les sorties de lac
    * Les régions d'assimilation de données bogus (zéro) de concentration de glace ont été élargies pour éviter l'instabilité numérique à la sortie du lac (c'est en lien avec l'option de charge de glace) lorsque la glace s'empile.
* Pour la composante de rivière:
    * Aucun changement

Pour plus d'informations, veuillez consulter le document des spécifications techniques pour le SPCE 3.1.0 qui est disponible [via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_specifications/tech_specifications_WCPS_3.1.0_f.pdf).

Une note technique avec plus de détails sur ces changements est disponible [sur cette page](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_notes/technote_wcps-310_f.pdf).

## Le mercredi 1er décembre 2021

### Mise à jour du Système de prévision du cycle de l'eau (SPCE) 3.0.0 du Centre météorologique canadien

En date du mercredi 1er décembre 2021, le Centre météorologique canadien (CMC) va procéder à la mise à jour du Système de prévision du cycle de l'eau (SPCE) vers la version 3.0.0.

Les modifications au SPCE v3.0.0 comparativement au précédent système opérationnel sont résumées comme suit:

* Le [SRPD v8.0.0](../nwp_rdps/changelog_rdps_fr.md) remplace le SRPD v7.1.0 comme modèle pilote
* Nouveau domaine plus grand couvrant le Golfe du Saint-Laurent (ainsi que les Grands Lacs)
* Pour les composantes pseudo-analyse/prévision :
    * Résolution améliorée de 2km/5km (intérieur/côtier) à 1km/2km
    * Charge de glace sur les Grands Lacs
    * Forçage du gradient de pression atmosphérique (effet du baromètre inverse pour les ondes de tempête)
* Pour la composante hydrologique :
    * Nouvelles stations d’observation de débit de rivière: Québec, United States Geologicial Survey (USGS)
    * Propagation en amont de l’information dérivée des observations de débit des rivières
    * Nouveaux champs climatologiques de drainage
    * Implantation du modèle “Dynamically Zoned Target Release (DZTR)” pour représenter les règles de gestion des réservoirs régulés individuels
    * Un nouveau solveur numérique dans WATROUTE

La note officielle annoncant cette implantation est disponible en cliquant [via ce lien](https://dd.meteo.gc.ca/doc/genots/2021/11/26/NOCN03_CWAO_262118___50159).

Pour plus d'informations, veuillez consulter le document des spécifications techniques pour le SPCE 3.0.0 qui est disponible [via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_specifications/tech_specifications_WCPS_3.0.0_f.pdf).

Une note technique avec plus de détails sur ces changements est disponible [sur cette page](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_notes/technote_wcps-300_f.pdf).

## Le mardi 21 janvier 2020

### Mise à jours du SPCE à la version 2.2.1 suite à la nouvelle infrastructure de calcul haute performance. 

Voir les détails via [ce lien](../changelog_multisystems_fr.md).

## Le mercredi 3 juillet 2019

### Mise à jour du Système de prévision du cycle de l'eau (SPCE) 2.1.0 du Centre météorologique canadien

En date du mercredi 3 juillet 2019, le Centre météorologique canadien (CMC) va procéder à la mise à jour du Système de prévision du cycle de l'eau (SPCE) vers la version 2.1.0.

Les modifications au SPCE v2.1.0 comparativement au précédent système opérationnel sont résumées comme suit:

* Le [SRPD v7.0.0](../nwp_rdps/changelog_rdps_fr.md) remplace le SRPD v6.0.0 comme modèle pilote.

Pour plus d'informations, veuillez consulter le document des spécifications techniques pour le SPCE 2.1.0 qui est disponible [via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_specifications/tech_specifications_WCPS_2.1.0_f.pdf).

Une note technique avec plus de détails sur ces changements est disponible [sur cette page](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_notes/technote_wcps-210_f.pdf).

## Le lundi 4 mars 2019

### Nouveau Système de prévision du cycle de l’eau (SPCE) déclaré opérationnel au Centre météorologique canadien (CMC)

Le lundi 4 mars 2019, le Centre météorologique canadien (CMC) du Service météorologique du Canada (SMC) déclare opérationnel le nouveau Système de prévision du cycle de l’eau (SPCE v2.0.0), après avoir exécuté en mode expérimental pendant près de 3 ans.

La note officielle annonçant cette implantation importante est disponible [via ce lien](http://dd.meteo.gc.ca/doc/genots/2019/03/04/NOCN03_CWAO_041525___40141).

Une note technique avec plus de détails sur ce système est disponible [via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_notes/technote_wcps-200_20190304_f.pdf).

Le document des spécifications techniques pour le SPCE 2.0.0 est disponible [via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_specifications/tech_specifications_WCPS_2.0.0_f.pdf).