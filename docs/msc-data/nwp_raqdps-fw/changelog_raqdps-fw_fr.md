[In English](changelog_raqdps-fw_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [SRPDQA-FW](readme_raqdps-fw_fr.md) > Changements au Système régional de prévision déterministe de la qualité de l'air FireWork

# Chronologie des changements apportés au Système régional de prévision déterministe de la qualité de l'air FireWork (SRPDQA-FW)

## Le mardi 11 juin 2024

### Fusion du Système régional de prévision déterministe de la qualité de l'air FireWork avec le Système régional de prévision déterministe de la qualité de l'air.

Le mardi 11 juin 2024, à compter de la passe de 1200 UTC, le Centre météorologique canadien (CMC) cessera de tourner un système séparé pour la prévision de la qualité de l'air avec émissions de feux de forêt en temps quasi réel. Le Système régional de prévision déterministe de la qualité de l'air (SRPDQA) incluera désormais les contributions de feux de forêt, à partir de la version 25 de ce système.

Toute la documentation reliée à la mise à jour du Système régional de prévision déterministe de la qualité de l'air (SRPDQA) version 25 est [disponible ici](../nwp_raqdps/changelog_raqdps_fr.md#mardi-11-juin-2024).

## Le mardi 28 juin 2022

### Mise à jour de SRPDQA-FW à la version 24 suite à la nouvelle infrastructure de calcul haute performance. 

Voir les détails via [ce lien](../changelog_multisystems_fr.md).

## Le mercredi 1er décembre 2021

### Mise à jour du Système régional de prévision déterministe de la qualité de l'air FireWork

Le mercredi 1er décembre 2021, à compter de la passe de 1200 UTC, le Centre météorologique canadien (CMC) mettra à jour le Système régional de prévision déterministe de la qualité de l'air avec émissions de feux de forêt en temps quasi réel FireWork en remplaçant la version 22 par la version 23.

Résumé des éléments que comporte cette mise à jour:

* Les analyses météorologiques et le modèle pilote proviennent maintenant du [SRPD v8.0.0](https://eccc-msc.github.io/open-data/msc-data/nwp_rdps/changelog_rdps_en/) plutôt que du SRPD v7.1.0.
* Nouveaux inventaires d'émission anthropogéniques:
    * Canada:  De la version 2013 de l'inventaire des émission de polluants atmosprériques (IEPA) à la version projetée 2020.
    * U.S.:    de la version 2017 de l'inventaire national des émissions à la version projetée 2023.
    * Mexique: de la version 2008 de l'inventaire national des émissions à la version projetée 2023.
* Représentation de la sédimentation des particules améliorée.
* Nouvelles librairies météorologique et chimique 
    * Météo:  GEM 5.0.2 => GEM 5.1.0
    * Chimie:    GEM-MACH 3.0.0.2 => GEM-MACH 3.1.0.0
* Mise à jour du Système canadien de prévision des émissions des feux de forêt (SCPEFF), de la version 2.06 à la version 4. 

Un résumé des innovations incluses dans cette mise à jour ainsi que de leurs impacts sur la performance du système [est disponible ici](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/fact_sheets/factsheet_raqdps023_f.pdf ).

Une copie de la note officielle annonçant ce changement dans FireWork est disponible [via ce lien](http://dd.meteo.gc.ca/doc/genots/2021/11/26/NOCN03_CWAO_262118___50159).

Le document des spécifications techniques du SRPDQA-FW version 23 [est disponible ici](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_RAQDPS_023_f.pdf).

Une note technique pour FireWork avec plus de détails sur ces changements est disponible [via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_raqdps023fw_f.pdf).


## Le mercredi 1 avril 2020

### Mise en œuvre du système de prévision FireWork pour la saison d'été 2020

Le mercredi 1 avril 2020, à compter de la passe de 00 UTC, le Centre météorologique canadien (CMC) du Service météorologique du Canada (SMC) mettra en œuvre le système de prévision FireWork pour la saison d'été 2020. FireWork est un système de prévision saisonnier qui est basé sur le système régionale de prévision déterministe de la qualité de l'air (SRPDQA) et qui incorpore des émissions provenant des feux de forêts en Amérique du Nord.

Pour plus d'information, s'il vous plait consulter la note officielle annonçant l'implantation du FireWork pour l'été 2020 [en cliquant ici]( https://dd.meteo.gc.ca/doc/genots/2020/04/03/NOCN03_CWAO_031510___44016).

Une note technique de FireWork est disponible [via ce lien](http://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_notes/technote_raqdpsfw_f.pdf).

## Le mardi 21 janvier 2020

### Mise à jour de FireWork suite à la nouvelle infrastructure de calcul haute performance. 

Voir les détails via [ce lien](../changelog_multisystems_fr.md).

## Le mercredi 3 juillet 2019

### Mise à jour du système régional de prévision déterministe de la qualité de l'air FireWork

Le mercredi 3 juillet 2019, à compter de la passe de 1200 UTC, le Centre météorologique canadien (CMC) mettra à jour le système régional de prévision déterministe de la qualité de l'air complémentaire FireWork en remplaçant la version 020 par la version 021.

Résumé des éléments que comporte cette mise à jour:

* Les analyses météorologiques et le modèle pilote proviennent maintenant du [SRPD v7.0.0](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/changes_f.html#20190703_rdps_7.0.0) plutôt que du SRPD v6.0.0.
* Mise à jour de GEM de la version v4.8-LTS.16 à la version GEM v5.0.0. Pour plus d'informations sur GEM-5, veillez consulter ce [document (en anglais)](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_notes/GEM5_paper_submitted_JAMES_20190614.pdf).
* Amélioration dans le calcul de la chimie du modèle.

Une copie de la note officielle annonçant ce changement dans FireWork [est disponible via ce lien](http://dd.meteo.gc.ca/doc/genots/2019/06/28/NOCN03_CWAO_281935___12903).

Une note technique pour FireWork avec plus de détails sur ces changements sera disponible bientôt.

## Le lundi 15 avril 2019

### Mise en œuvre du système de prévision FireWork pour la saison d'été 2019

Le lundi 15 avril 2019, à compter de la passe de 00 UTC, le Centre météorologique canadien (CMC) du Service météorologique du Canada (SMC) mettra en œuvre le système de prévision FireWork pour la saison d'été 2019. FireWork est un système de prévision saisonnier qui est basé sur le système régionale de prévision déterministe de la qualité de l'air (SRPDQA) et qui incorpore des émissions provenant des feux de forêts en Amérique du Nord.

Pour plus d'information, s'il vous plait consulter la note officielle annonçant l'implantation du FireWork pour l'été 2019 [en cliquant ici](https://dd.meteo.gc.ca/doc/genots/2019/04/15/NOCN03_CWAO_151930___14392).

Une note technique avec plus de détails sera bientôt disponible en français.

En attendant, une note technique en anglais de FireWork est disponible [via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_notes/technote_raqdps020.2fw_20190415_e.pdf).

## Le mardi 18 septembre, 2018

### Mise à jour du système régional de prévision déterministe de la qualité de l'air FireWork

Le mardi 18 septembre 2018, à compter de la passe de 1200 UTC, le Centre météorologique canadien (CMC) mettra à jour le système régional de prévision déterministe de la qualité de l'air FireWork en remplaçant la version 019 par la version 020.

Résumé des éléments que comporte cette mise à jour :

* Les analyses météorologiques et le modèle pilote proviennent maintenant du [SRPD v6.0.0](/../nwp_rdps/changelog_rdps_fr.md#le-mardi-18-septembre-2018) plutôt que du SRPD v5.1.0.
* Adoption de la configuration SRPD v6.0.0, comprenant le recyclage des principales variables physiques et l'approche incrémentale 4D de mise à jour de l'analyse (IAU:Incremental Analysis Update).
* L'implementation de la nouvelle version du code du modèle (v2.3.1), pour améliorer la vitesse de traitement et augmenter la robustesse, ainsi que l'amélioration de la chimie (dépôt sec en phase gazeuse sur les surfaces enneigées et la glace marine).
* Introduction d’un nouvel ensemble d'émissions basé sur des inventaires nationaux d’émissions plus récents.

La note officielle annonçant ce changement est disponible [en cliquant ici](https://dd.meteo.gc.ca/doc/genots/2018/09/17/NOCN03_CWAO_171403___42412).

Une note technique avec plus de détails sur ces changements est disponible [sur cette page](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_notes/technote_raqdps-v20_20180918_f.pdf).

## Le mardi 3 avril 2018

### Mise en œuvre du système de prévision FireWork pour la saison d'été 2018

Le mardi 3 avril 2018, à compter de la passe de 1200 UTC, le Centre météorologique canadien (CMC) du Service météorologique du Canada (SMC) mettra en œuvre le système de prévision FireWork pour la saison d'été 2018. FireWork est un système de prévision saisonnier qui est basé sur le système régionale de prévision déterministe de la qualité de l'air (SRPDQA) et qui incorpore des émissions provenant des feux de forêts en Amérique du Nord.

Pour plus d'information, s'il vous plait consulter la note officielle annonçant l'implantation du FireWork pour l'été 2018 [en cliquant ici](https://dd.meteo.gc.ca/doc/genots/2018/04/03/NOCN03_CWAO_031838___00001).

Une note technique avec plus de détails est disponible [via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_notes/technote_raqdps015fw_20160428_f.pdf).

## Le mardi 18 septembre, 2018

### Mise à jour du  système de prévision FireWork

Le mardi 18 septembre 2018, à compter de la passe de 1200 UTC, le Centre météorologique canadien (CMC) mettra à jour le système régional de prévision déterministe de la qualité de l'air (SRPDQA) et le système complémentaire FireWork en remplaçant la version 019 par la version 020.

Résumé des éléments que comporte cette mise à jour :

* Les analyses météorologiques et le modèle pilote proviennent maintenant du SRPD v6.0.0 plutôt que du SRPD v5.1.0.
* Adoption de la configuration SRPD v6.0.0, comprenant le recyclage des principales variables physiques et l'approche incrémentale 4D de mise à jour de l'analyse (IAU:Incremental Analysis Update).
* L'implementation de la nouvelle version du code du modèle (v2.3.1), pour améliorer la vitesse de traitement et augmenter la robustesse, ainsi que l'amélioration de la chimie (dépôt sec en phase gazeuse sur les surfaces enneigées et la glace marine).
* Introduction d’un nouvel ensemble d'émissions basé sur des inventaires nationaux d’émissions plus récents.

La note officielle annonçant ce changement est disponible [en cliquant ici](https://dd.meteo.gc.ca/doc/genots/2018/09/17/NOCN03_CWAO_171403___42412).

## Le mercredi 7 septembre 2016

### Mise à jour majeure du système de prévision FireWork

Le mercredi 7 septembre 2016, à compter de la passe de 1200 UTC, le Centre météorologique canadien (CMC) mettra à jour le système de prévision FireWork. FireWork est un système de prévision saisonnier qui est basé sur le système régional de prévision déterministe de la qualité de l'air (SRPDQA) qui incorpore des émissions provenant des feux de forêts en Amérique du Nord. Il est en fonction durant la saison des feux de forêts en Amérique du Nord, qui se termine normalement à la fin du mois d'octobre.

Les changements inclus dans cette mise en œuvre sont équivalent à ceux décrit pour le [SRPDQA016](/../nwp_raqdps/changelog_raqdps_fr.md).

La note officielle annonçant ce changement est disponible [en cliquant ici](https://dd.meteo.gc.ca/doc/genots/2016/04/13/NOCN03_CWAO_131900___00844).

## Le jeudi 14 avril 2016

### Mise en œuvre du système de prévision FireWork pour la saison d'été 2016

Le jeudi 14 avril 2016, à compter de la passe de 1200 UTC, le Centre météorologique canadien (CMC) du Service météorologique du Canada (SMC) mettra en œuvre le système de prévision FireWork pour la saison d'été 2016. FireWork est un système de prévision saisonnier qui est basé sur le système régionale de prévision déterministe de la qualité de l'air (SRPDQA) et qui incorpore des émissions provenant des feux de forêts en Amérique du Nord.

Pour plus d'information, s'il vous plait consulter la note officielle annonçant l'implantation du FireWork pour l'été 2016 [en cliquant ici](https://dd.meteo.gc.ca/doc/genots/2016/04/13/NOCN03_CWAO_131900___00844).

Une note technique à ce sujet est disponible [via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_notes/technote_raqdps015fw_20160428_f.pdf).
