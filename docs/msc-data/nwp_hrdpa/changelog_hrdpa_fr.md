[In English](changelog_hrdpa_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [AHRDP](readme_hrdpa_fr.md) > Changements au AHRDP

# Chronologie des changements apportés au Système d'analyse à haute résolution déterministe de précipitation (CaPA-AHRDP)

## Le mardi 11 juin 2024

### Mise à jour de l'Analyse à haute résolution déterministe de précipitation (AHRDP) 6.0.0 du Centre météorologique canadien (CMC)

Le mardi 11 juin 2024, le Centre météorologique canadien (CMC) va procéder à la mise en œuvre opérationnelle de la version 6.6.0 de son Analyse à haute résolution déterministe de précipitation (AHRDP).

Principaux changements :

* Ajout de 86 stations supplémentaires du réseau partenaire Saskatchewan Fire Weather Network (SKForestry) permettant d'améliorer les analyses pour cette province.
* Assimilation des données radar à double polarisation pour 25 radars canadiens bande S (DPQPE) et 65 radars américains NEXRAD (DAA). Ajout de 3 radars américains.
* Ces changements entrainent une amélioration significative des scores d’habileté pour une majorité de seuils de précipitation.

Une copie de la note officielle annonçant ce changement est disponible [via ce lien](http://dd.meteo.gc.ca/doc/genots/2024/06/11/NOCN03_CWAO_262118___xxxxx).

Le document des spécifications techniques de AHRDP 6.0.0 est disponible [via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_HRDPA_6.0.0_f.pdf).

## Le mercredi 3 mai 2023

### Mise à jour de AHRDP suite au remplacement de GOES-17 par GOES-18

Depuis le 4 janvier 2023 à 18Z, le satellite GOES-18 a pris le relais du satellite GOES-17 en tant que satellite occidental opérationnel. Au sein du système opérationnel AHRDP, les observations du satellite GOES sont utilisées pour effectuer une partie du post-traitement des estimés de précipitation radar. En particulier, les données GOES sont utilisées pour créer un masque de nuages afin de nettoyer les données radar.

Depuis la disparition du satellite GOES-17 le 4 janvier, le système AHRDP s'est appuyé sur le champ NT du modèle de prévision SHRPD pour construire le masque de nuages. Cette solution de contingence a permis d'effectuer le post-traitement des estimés de précipitation radar, mais avec une fiabilité moindre qu'avec les données GOES.

Afin d'optimiser de nouveau le post-traitement des estimés de précipitation radar, le système AHRDP a été mis à jour le 3 mai 2023 pour assimiler les données GOES-18 en plus des données GOES-16 déjà assimilées.

## Le mardi 28 juin 2022

### Mise à jour du AHRDP à la version 5.2.0 suite à la nouvelle infrastructure de calcul haute performance. 

Voir les détails via [ce lien](../changelog_multisystems_fr.md).

## Le mercredi 1er décembre 2021

### Mise à jour vers la version 5.1.0 du Système d'analyse à haute résolution déterministe de précipitation (CaPA-AHRDP) au Centre météorologique canadien

Le mercredi 1er décembre 2021, le Centre météorologique canadien (CMC) mettra à jour son Système d'analyse à haute résolution déterministe de précipitation (CaPA-AHRDP (2.5km)) à la version 5.1.0.

Les modifications incluses dans cette mise à jour sont résumées comme suit :

* CaPA-AHRDP construit maintenant ses champs d'essai à partir du [SHRPD v6.0.0](../nwp_hrdps/changelog_hrdps_fr.md)
   * Utilisation des échéances 00-06H du SHRPD-6.0.0 pour la production du champ d’essai
* Ajout de 29 radars américains et remplacement de 19 radars de bande C canadiens par autant de radars de bande S
* Ajout de trois réseaux partenaires de stations de surface
* Mise à jour de masques statiques de contrôle de qualité pour 8 radars
* Utilisation des champs de nuage des satellites GOES 16/17 pour le nettoyage des QPE radars

La note officielle annoncant cette implantation est disponible en cliquant [via ce lien](https://dd.meteo.gc.ca/doc/genots/2021/11/26/NOCN03_CWAO_262118___50159).

Une note technique avec plus de détails sur ces changements est disponible [via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_capa_hrdpa-510_f.pdf).

Le document des spécifications techniques du AHRDP v5.1.0 est disponible [via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_HRDPA_5.1.0_f.pdf).

## Le mardi 21 janvier 2020

### Mise à jours de CaPA-AHRDP à la version 4.7.0 suite à la nouvelle infrastructure de calcul haute performance. 

Voir les détails via [ce lien](../changelog_multisystems_fr.md).

## Le mercredi 3 juillet 2019

### Mise en œuvre de la version 4.6.0 du Système d'analyse à haute résolution déterministe de précipitation (CaPA-AHRDP) au Centre météorologique canadien (CMC)

Le mercredi 3 juillet 2019, à compter de la passe de 1200 UTC, le Centre météorologique canadien (CMC) du Service météorologique du Canada (SMC) mettra à jour le Système d'analyse à haute régionale déterministe de précipitation (CaPA-AHRDP) en le faisant passer à la version 4.6.0.

Résumé des changements :

* Branchement au [SHRPD v5.1.0](../nwp_hrdps/changelog_hrdps_fr.md) pour obtenir son champ d'essai.

Une copie de la note officielle annonçant ce changement [est disponible via ce lien](http://dd.meteo.gc.ca/doc/genots/2019/07/03/NOCN03_CWAO_031240___43184).

## Le mardi 18 septembre, 2018

### Mise à jour vers la version 4.5.0 du Système d'analyse à haute résolution déterministe de précipitation (CaPA-AHRDP) au Centre météorologique canadien

Le mardi 18 septembre 2018, à compter de la passe de 1200 UTC, le Centre météorologique canadien (CMC) mettra à jour son système d'analyse à haute résolution déterministe de précipitation (CaPA-AHRDP) à la version 4.5.0.

Les modifications incluses dans cette mise à jour sont résumées comme suit :

* Les champs d'essai de ces analyses de précipitation sont issus des nouvelles versions des systèmes implantées le 18 septembre 2018
    * CaPA-AHRDP construit maintenant ses champs d'essai à partir du [SHRPD v5.0.0](../nwp_hrdps/changelog_hrdps_fr.md).
* Assimilation des observations du réseau CoCoRaHS
* Nouvelle analyse 24h valide à 06h00 UTC alignée avec la journée climatologique

Une copie de la note officielle annoncant cette implantation est disponible en cliquant sur le lien :

* [Annonce officielle de CaPA-AHRDP 4.5.0](http://dd.meteo.gc.ca/doc/genots/2018/09/17/NOCN03_CWAO_171416___54417)

Une note technique avec plus de détails sur ces changements est disponible via le lien :

* [Note technique du CaPA-AHRDP 4.5.0](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_capa_hrdpa-450_20180918_f.pdf)

## Le vendredi 2 mars 2018

### Mise en oeuvre du Système d'analyse à haute résolution déterministe de précipitation (CaPA-AHRDP version 4.1.0) au Centre météorologique canadien (CMC)

Le vendredi 2 mars 2018 à compter de la passe de 1200 UTC, le Centre météorologique canadien (CMC) mettra à jour son Système d'analyse régionale déterministe de précipitation (CaPA-ARDP) en ajoutant une nouvelle configuration des analyses à plus haute résolution (CAPA-AHRDP). Cette nouvelle version aura desormais 2.5km de resolution et ces analyses s'ajoutent à celles déjà produites en mode operationnel depuis 2011 à 15km de résolution et depuis octobre 2012 à celles de 10km de resolution.

Une copie de la note officielle annonçant ce changement [est disponible via ce lien](http://dd.meteo.gc.ca/doc/genots/2018/03/02/NOCN03_CWAO_022008___00002).

Une note technique à ce sujet [est disponible via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/CAPA-HRDPA_4_1_0_Tech_note_f.pdf).







