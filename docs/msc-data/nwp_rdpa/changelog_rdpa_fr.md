[In English](changelog_rdpa_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [ARDP](readme_rdpa_fr.md) > Changements au ARDP

# Chronologie des changements apportés à l'Analyse régionale déterministe de précipitation (CaPA-ARDP)

## Le mardi 11 juin 2024

### Mise à jour de l'Analyse régionale déterministe de précipitation (ARDP) 6.0.0 du Centre météorologique canadien (CMC)

Le mardi 11 juin 2024, le Centre météorologique canadien (CMC) va procéder à la mise en œuvre opérationnelle de la version 6.0.0 de son Analyse régionale déterministe de précipitation (ARDP).

Principaux changements :

* Ajout de 86 stations supplémentaires du réseau partenaire Saskatchewan Fire Weather Network (SKForestry) permettant d'améliorer les analyses pour cette province.
* Assimilation des données radar à double polarisation pour 32 radars canadiens bande S (DPQPE) et 65 radars américains NEXRAD (DAA). Ajout de 3 radars américains.
* Ces changements entrainent une amélioration significative des scores d’habileté pour une majorité de seuils de précipitation.

Une copie de la note officielle annonçant ce changement est disponible [via ce lien](http://dd.meteo.gc.ca/doc/genots/2024/06/11/NOCN03_CWAO_262118___xxxxx).

Le document des spécifications techniques de ARDP 6.0.0 est disponible [via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_RDPA_6.0.0_f.pdf).

Une note technique à ce sujet est disponible [via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_rdpa-600_f.pdf).

## Le mercredi 3 mai 2023

### Mise à jour de ARDP suite au remplacement de GOES-17 par GOES-18

Depuis le 4 janvier 2023 à 18Z, le satellite GOES-18 a pris le relais du satellite GOES-17 en tant que satellite occidental opérationnel. Au sein du système opérationnel ARDP, les observations du satellite GOES sont utilisées pour effectuer une partie du post-traitement des estimés de précipitation radar. En particulier, les données GOES sont utilisées pour créer un masque de nuages afin de nettoyer les données radar.

Depuis la disparition du satellite GOES-17 le 4 janvier, le système ARDP s'est appuyé sur le champ NT du modèle de prévision SRPD pour construire le masque de nuages. Cette solution de contingence a permis d'effectuer le post-traitement des estimés de précipitation radar, mais avec une fiabilité moindre qu'avec les données GOES.

Afin d'optimiser de nouveau le post-traitement des estimés de précipitation radar, le système ARDP a été mis à jour le 3 mai 2023 pour assimiler les données GOES-18 en plus des données GOES-16 déjà assimilées.

## Le mardi 28 juin 2022

### Mise à jour de ARDP à la version 5.3.0 suite à la nouvelle infrastructure de calcul haute performance. 

Voir les détails via [ce lien](../changelog_multisystems_fr.md).

## Le mercredi 1er décembre 2021

### Mise à jour vers la version 5.2.0 du système d'Analyse régionale déterministe de précipitation (CaPA-ARDP) au Centre météorologique canadien

Le mercredi 1er décembre 2021, le Centre météorologique canadien (CMC) mettra à jour son système d'Analyse régionale déterministe de précipitation (CaPA-ARDP (10km)) à la version 5.2.0.

Les modifications incluses dans cette mise à jour sont résumées comme suit :

* CaPA-ARDP construit maintenant ses champs d'essai à partir du [SRPD v8.0.0](../nwp_rdps/changelog_rdps_fr.md)
* Ajout de 14 radars canadiens de bande S
* Assimilation des stations du réseau du Ministère des ressources naturelles de l'Ontario (MNR)
* Mise à jour de masques statiques de contrôle de qualité pour 8 radars
* Agrandissement de la grille afin de couvrir le domaine du [SRPD](../nwp_rdps/readme_rdps_fr.md)

La note officielle annoncant cette implantation est disponible en cliquant [via ce lien](https://dd.meteo.gc.ca/doc/genots/2021/11/26/NOCN03_CWAO_262118___50159).

Une note technique avec plus de détails sur ces changements est disponible [via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_capa_rdpa-520_f.pdf).

Le document des spécifications techniques du ARDP v5.2.0 est disponible [via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_RDPA_5.2.0_f.pdf).

## Le mercredi 9 juin 2021

### Mise à jour vers la version 5.0.0 du système d'Analyse régionale déterministe de précipitation (CaPA-ARDP) au Centre météorologique canadien (CMC)

Le mercredi 9 juin 2021, à compter de la passe de 1200 UTC, le Centre météorologique canadien (CMC) mettra à jour son système d'Analyse régionale déterministe de précipitation (CaPA-ARDP) à la version 5.0.0.

Les modifications incluses dans cette mise à jour sont résumées comme suit :

* Assimilation de trois nouveaux réseaux d’observation de précipitations:
     * Manitoba Agriculture (MBAG),
     * Grand River Conservation Authority (GRCA),
     * Toronto River Conservation Authority (TRCA).
* Changement dans la composite Radar:
     * 5 radars Canadiens de type S-band remplacent les radars obsolètes de type C-band correspondants. 
     * Ajout de 29 nouveaux radars américains de type S-band. 
* Assimilation des données satellitaires “Integrated Multi-SatellitE Retrievals for GPM” (IMERG) dans l’analyse finale.

Une copie de la note officielle annoncant cette implantation est disponible en cliquant sur le lien : [Annonce officielle de CaPA-ARDP 5.0.0](https://dd.meteo.gc.ca/doc/genots/2021/06/08/NOCN03_CWAO_081408___31851)

Une note technique avec plus de détails sur ces changements est disponible via le lien : [Note technique du CaPA-ARDP 5.0.0](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_capa_rdpa-500_f.pdf)

## Le mardi 21 janvier 2020

### Mise à jours de CaPA-ARDP à la version 4.7.0 suite à la nouvelle infrastructure de calcul haute performance. 

Voir les détails via [ce lien](../changelog_multisystems_fr.md).

## Le mercredi 3 juillet 2019

### Mise en œuvre de la version 4.6.0 du système d'Analyse Régionale Déterministe de Précipitation (CaPA-ARDP) au Centre météorologique canadien (CMC)

Le mercredi 3 juillet 2019, à compter de la passe de 1200 UTC, le Centre météorologique canadien (CMC) du Service météorologique du Canada (SMC) mettra à jour le système d'Analyse Régionale Déterministe de Précipitation (CaPA-ARDP) en le faisant passer à la version 4.6.0.

Résumé des changements :

* Branchement au [SRPD v7.0.0](../nwp_rdps/changelog_rdps_fr.md) pour obtenir son champ d'essai.
* Utilisation des échéances 6 et 12 heures du champ prévu de la précipitation totale (PR) au lieu de 0 et 6 heures comme dans la version précédente.

Une copie de la note officielle annonçant ce changement [est disponible via ce lien](http://dd.meteo.gc.ca/doc/genots/2019/07/03/NOCN03_CWAO_031225___18175).


## Le mardi 18 septembre, 2018

### Mise à jour vers la version 4.5.0 du système d'analyse régionale déterministe de précipitation (CaPA-ARDP) au Centre météorologique canadien (CMC)

Le mardi 18 septembre 2018,  à compter de la passe de 1200 UTC, le Centre météorologique canadien (CMC) mettra à jour son système d'analyses régionales déterministes de précipitation (CaPA-ARDP) à la version 4.5.0.

Les modifications incluses dans cette mise à jour sont résumées comme suit :

* Les champs d'essai de ces analyses de précipitation sont issus de la nouvelle version du système implantée le 18 septembre 2018
    * CaPA-ARDP construit maintenant ses champs d'essai à partir du [SRPD v6.0.0](../nwp_rdps/changelog_rdps_fr.md).
* Assimilation des observations du réseau CoCoRaHS. (CaPA-ARDP)
* Nouvelle analyse 24h valide à 06h00 UTC alignée avec la journée climatologique. (CaPA-ARDP)
* CaPA-ARDP v4.5.0 utilisera les échéances de 0 et 6 heure de précipitation totale au lieu des 6 et 12 heures. Ceci est rendu possible parce que le SRPD 6.0.0 peut maintenant générer des précipitations dès le début de l'intégration.

Une copie de la note officielle annoncant cette implantation est disponible en cliquant sur le lien :

* [Annonce officielle de CaPA-ARDP 4.5.0](http://dd.meteo.gc.ca/doc/genots/2018/09/17/NOCN03_CWAO_171415___18584)

Une note technique avec plus de détails sur ces changements est disponible via le lien :

* [Note technique du CaPA-ARDP 4.5.0](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_capa_rdpa-450_20180918_f.pdf)


## Le mercredi 9 novembre 2016

### Mise à jour du système d'analyse régionale déterministe de précipitation (CaPA-ARDP version 4.0.0) au Centre météorologique canadien (CMC)

Le mercredi 09 novembre 2016 à compter de la passe de 1200 UTC, le Centre météorologique canadien (CMC) mettra à jour son système d'analyse régionale déterministe de précipitation (CaPA-ARDP) en remplaçant la version CaPA-ARDP-3.2.0 par la version 4.0.0. Cette nouvelle version assimile des observations de précipitation provenant de deux réseaux de stations nouvellement disponibles au CMC. Des pseudo-observations de 0 mm déduites du réseau METAR américain sont ajoutées au jeu d'observations soumis au système. Cette nouvelle version assimile aussi 33 radars météorologiques américains ajoutés à la présente composite des quantités de précipitation estimées (QPE). Toutes ces modifications permettent de produire une meilleure analyse de précipitation.

Une copie de la note officielle annonçant ce changement [est disponible via ce lien](http://dd.meteo.gc.ca/doc/genots/2016/11/09/NOCN03_CWAO_091420___00557).

Une note technique à ce sujet [est disponible via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/lib/technote_capa-400_20161109_f.pdf).


## Le mardi 15 décembre 2015

### Mise à jour du système d'analyse régionale déterministe de précipitation (CaPA-ARDP version 3.2.0) au Centre météorologique canadien (CMC)

Le mardi 15 décembre 2015,  à compter de la passe de 1200 UTC, le Centre météorologique canadien (CMC) mettra à jour son système d'analyse régionale déterministe de précipitation (CaPA-ARDP) en remplaçant la version CaPA-ARDP-3.1.0 par la version 3.2.0. Cette nouvelle version corrigera deux problèmes mineurs : Un au niveau du traitement des relevès de précipitation et un second qui affecte l'encodage en GRIB2 en ajoutant un masque pour bien représenter les zones "No-Data".

Une copie de la note officielle annonçant ce changement [est disponible via ce lien](http://dd.meteo.gc.ca/doc/genots/2015/12/10/NOCN03_CWAO_102100___00779).

Un feuillet d'information à ce sujet [est disponible via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/lib/capa_feuillet_information_20141118_f.pdf).


## Le mercredi 03 juin 2015

### Mise à jour du système d'analyse régionale déterministe de précipitation (ARDP version 3.1.0) au Centre météorologique canadien (CMC)

Le mercredi 03 juin 2015,  à compter de la passe de 1200 UTC, le Centre météorologique canadien (CMC) mettra à jour son système d'analyse régionale déterministe de précipitation (ARDP) en remplaçant la version CaPA-ARDP-3.0.0 par la version 3.1.0. Cette nouvelle version favorisera principalement l'assimilation d'un nombre accru d'observations de précipitation solide.

Une copie de la note officielle annonçant ce changement [est disponible via ce lien](http://dd.meteo.gc.ca/doc/genots/2015/06/03/NOCN03_CWAO_031904___00791).

Un feuillet d'information à ce sujet [est disponible via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/lib/capa_feuillet_information_20141118_f.pdf).


## Le mardi 18 novembre 2014

### Mise à jour majeure du système d'analyse régionale déterministe de précipitations (ARDP version 3.0.0) au Centre météorologique Canadien (CMC)

Le mardi 18 novembre 2014, à compter de la passe de 1200 UTC, le Centre météorologique canadien (CMC) va procéder à la mise en œuvre opérationnelle de la version 3.0.0 de son système d'analyse régionale déterministe de précipitations (ARDP). Ci-dessous les changements les plus importants:

* Cette version assimilera une source importante d'information supplémentaire, soit les quantités de précipitation estimées (QPE) par les radars météorologiques canadiens.
* Le système régional déterministe de prévision (SRPD) qui fournit le champ d'essai sera aussi mis à jour pour passer à la version 4.0.0
* Le nombre d'analyses produites quotidiennement passera de 9 à 10.

Une copie de la note officielle annonçant ce changement [est disponible via ce lien](http://dd.meteo.gc.ca/doc/genots/2014/11/14/NOCN03_CWAO_141846___00708).

Un feuillet d'information à ce sujet [est disponible via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/lib/capa_feuillet_information_20141118_fr.pdf).

## Le mardi 20 août 2013

### Mise en place de la version 2.4 de CaPA (ARDP)

## Le mercredi 3 octobre 2012

### Améliorations au système d'analyse régionale déterministe de précipitations (ARDP version 2.3.0) au Centre météorologique Canadien (CMC)

Le mercredi 3 octobre 2012, débutant avec la passe de 1200 UTC, le Centre météorologique Canadien (CMC) mettra à jour son système d'analyse régionale déterministe de précipitations avec la version 2.3.0 (ARDP-230).

Cette mise à jour se fait conjointement avec celle du nouveau système régional de prévision déterministe version 3.0.0 qui fournira au système ARDP un champ d'essai à plus haute résolution. [Des informations sur les changements au SRPD-300 sont disponibles via ce lien en cliquant ici](../nwp_rdps/changelog_rdps_fr.md).

Une copie de la note officielle annoncant ce changement [est disponible via ce lien](http://dd.weatheroffice.ec.gc.ca/doc/genots/2012/10/02/NOCN03_CWAO_022155___00170).

Une note technique à ce sujet [est disponible en cliquant ici](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/lib/op_systems/doc_opchanges/technote_rdpa_20121018_f.pdf).








