[In English](changelog_riops_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [SRPOG](readme_riops_fr.md) > Changements au SRPOG

# Chronologie des changements apportés au Système Régional de Prévision Océan-Glace (SRPOG)

# Le mardi 28 juin 2022

### Mise à jour du SRPOG à la version 2.3.0 suite à la nouvelle infrastructure de calcul haute performance. 

Voir les détails via [ce lien](../changelog_multisystems_fr.md).

## Le mercredi 1er décembre 2021

### Mise à jour du Système régional de prévision océan-glace (SRPOG) 2.2.0 du Centre météorologique canadien (CMC)

Le mercredi 1er décembre 2021, le Centre météorologique canadien (CMC) va procéder à la mise en œuvre opérationnelle de la version 2.2.0 de son Système régional de prévision océan-glace (SRPOG).

Les changements majeurs de cette mise à jour se résument ainsi:

* Introduction d'un nouveau schema pour le mélange vertical 
* Correction de Biais des profils de température et de salinité - 3DVar
* Réduction de la turbulence par le déferlement des vagues 
* Augmentation de la rugosité atm-glace
* Ajout du cycle diurne 
* Ajout d’un module de monitoring


Une copie de la note officielle annonçant ce changement [est disponible via ce lien](http://dd.meteo.gc.ca/doc/genots/2021/11/26/NOCN03_CWAO_262118___50159).

Le document des spécifications techniques du SRPOG 2.2.0 [est disponible ici](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_RIOPS_2.2.0_f.pdf).

Une note technique à ce sujet [est disponible via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_riops-220_f.pdf).


## Le mardi 21 janvier 2020

### Mise à jours du SRPOG à la version 2.1.0 suite à la nouvelle infrastructure de calcul haute performance. 

Voir les détails via [ce lien](../changelog_multisystems_fr.md).

## Le mercredi 3 juillet 2019

### Implémentation du Système Régional de Prévision Océan-Glace (SRPOG) 2.0.0 du Centre météorologique canadien (CMC)

Le mercredi 3 juillet 2019, le Centre météorologique canadien (CMC) va procéder à l'implémentation de la version 2.0.0 de son Système Régional de Prévision Océan-Glace (SRPOG). Avec cette implémentation, SRPOG changera aussi son statut de système en mode expérimental à mode opérationnel.

Résumé des éléments majeurs que comporte cette mise à jour :
* Ajout d'une composante indépendante d'assimilation de données océaniques.
* Extension du domaine SRPOG dans le pacifique nord.

Une copie de la note officielle annonçant ce changement est disponible [via ce lien](https://dd.meteo.gc.ca/doc/genots/2019/06/28/NOCN03_CWAO_281850___63233).
Le document des spécifications techniques du SRPOG 2.0.0 [est disponible ici en anglais seulement](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_specifications/tech_specifications_RIOPS_2.0.0_e.pdf).

Une note technique à ce sujet est disponible [via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_notes/technote_riops-200_f.pdf).

## Le mardi 21 juin 2016
### Implémentation du Système Régional de Prévision Océan-Glace (SRPOG) 1.1 du Centre météorologique canadien (CMC)

Le mardi 21 juin 2016, le Centre météorologique canadien (CMC) va procéder à l'implémentation opérationnelle en mode expérimental de la version 1.1 de son Système Régional de Prévision Océan-Glace (SRPOG).

Résumé des éléments majeurs que comporte cette implémentation par rapport au Système Régional de Prévision de Glace (SRPG) antérieur et aussi expérimental:

* Ajout d'une composante océanique 3D (NEMO-CICE) avec marée
    * Rappel pour les larges échelles spatiales vers les analyses océaniques du Système Global de Prévision Océan-Glace (SGPOG) durant la phase de pseudo-analyse qui précède celle de la prévision à 00 UTC.
    * La prévision démarre de la pseudo-analyse à 00 UTC et insére la dernière analyse de concentration de glace.
* Ajout des données AVHRR dans l'analyse de concentration de glace.

Une note technique à ce sujet (en anglais) est disponible [via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_notes/technote_riops-110_e.pdf).
