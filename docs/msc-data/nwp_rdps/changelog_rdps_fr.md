[In English](changelog_rdps_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [SRPD](readme_rdps_fr.md) > Changements au SRPD

# Chronologie des changements apportés au Système régional de prévision déterministe (SRPD)

## Le mercredi 3 juillet 2019

### Mise à jour majeure du système régional de prévision déterministe (SRPD) 7.0.0 du Centre météorologique canadien (CMC)

Le mercredi 3 juillet 2019, à compter de la passe de 1200 UTC, le Centre météorologique canadien (CMC) va procéder à la mise en œuvre opérationnelle de la version 7.0.0 de son Système régional de prévision déterministe (SRPD).
Résumé des éléments majeurs que comporte cette mise à jour :

* Changements au modèle de prévision :
    * Le [SGPD v7.0.0](../nwp_gdps/changelog_gdps_fr.md) remplace le SGPD v6.1.0 comme modèle pilote.
    * Mise à jour de GEM de la version v4.8-LTS.16 à la version GEM v5.0.0. Pour plus d'informations sur GEM-5, veillez consulter ce document (en anglais).
    * Augmentation de la résolution verticale, passant de 80 à 84 niveaux.
    * Amélioration su schéma de surface ISBA
* Changements au système d'assimilation:
    * Temps de coupure uniforme de T+7h pour chaque passes de la journée
    * Utilisation de la nouvelle analyse de température de mer à 0.1 deg de résolution plutot que 0.2 deg de résolution avant.


Une copie de la note officielle annonçant ce changement [est disponible via ce lien](http://dd.meteo.gc.ca/doc/genots/2019/06/28/NOCN03_CWAO_281756___39189).

Une note technique à ce sujet [est disponible via ce lien](http://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_rdps-700_f.pdf).

Le document des spécifications techniques pour le SRPD 7.0.0 est disponible [via ce lien](http://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_RDPS_7.0.0_f.pdf).


## Le mardi 18 septembre 2018

### Mise à jour majeure du système régional de prévision déterministe (SRPD) 6.0.0 du Centre météorologique canadien (CMC)

Le mardi 18 septembre 2018, à compter de la passe de 1200 UTC, le Centre météorologique canadien (CMC) va procéder à la mise en œuvre opérationnelle de la version 6.0.0 de son Système régional de prévision déterministe (SRPD).
Résumé des éléments majeurs que comporte cette mise à jour :

* Changements au modèle de prévision :
    * Il n'y a pas de changement significatif dans la composante modèle de prévision.
* Changements au système d'assimilation :
    * Introduction d'une stratégie de cyclage continu (comme le SGPD), en remplacement du cyclage intermittent utilisé précedemment.
    * Augmentation de la résolution de l'incrément d'analyse dans le 4D-EnVar (de 50 à 37 km).
    * Introduction de l'approche incrémentale 4D de mise à jour de l'analyse (IAU:Incremental Analysis Update).
    * Le modèle rapide de transfert radiatif pour l'assimilation de la radiance RTTOV a été mis à niveau, de la version 10.2 à la version 12.
    * Ajustement des poids d'erreur de covariance pour donner plus de poids aux champs d'essai du SGPE.
* Changements aux observations :
    * Plusieurs améliorations dans le traitement des observations radiosonde, AMV, des récepteurs GPS au sol et d'avions.
    * Ajout des observations de surface du réseau METAR ainsi que des autres partenaires du SMC.
    * Ajout de plusieurs canneaux de radiances CSR (radiance en ciel clair), principalement pour la vapeur d'eau.


La note officielle annonçant ce changement [est disponible via ce lien](http://dd.meteo.gc.ca/doc/genots/2018/09/17/NOCN03_CWAO_171331___27584).

Une note technique avec plus de détails sur la version 6.0.0 de ce système [est disponible en cliquant ici](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_rdps-600_20180918_f.pdf).

Le document des spécifications techniques pour le SRPD 6.0.0 est disponible [via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_RDPS_6.0.0_f.pdf).


Le mercredi 7 septembre 2016
Mise à jour du système régional de prévision déterministe (SRPD) 5.0.0 du Centre météorologique canadien (CMC)

Le mercredi 7 septembre 2016, à compter de la passe de 1200 UTC, le Centre météorologique canadien (CMC) va procéder à la mise en œuvre opérationnelle de la version 5.0.0 de son système régional de prévision déterministe (SRPD).
Résumé des éléments majeurs que comporte cette mise à jour:

* Changements au modèle de prévision:
    * La version de GEM est mise à jour de v3.3.8.2-isba (niveaux verticales non décallés) à v4.8.2 (niveaux verticales décallés).
    * Le système global de prévision déterministe (SGPD) remplace le "pilote" précédant grâce à l'introduction d'une nouvelle passe (la G0) qui a un temps de coupure de 120 minutes.
    * Une nouvelle grille basée sur la grille Yin du SGPD remplace la grille lat-lon existante.
    * La représentation des sorties du modèle à la surface a été modifiée.
    * Le séquenceur de tâches OCM a été remplacé par le nouveau séquenceur Maestro.
* Changements au système d'assimilation:
    * Aucune.
* Changements aux observations:
    * Aucune.

La note officielle annonçant ce changement [est disponible en cliquant ici](http://dd.meteo.gc.ca/doc/genots/2016/09/02/NOCN03_CWAO_022052___00869).

Une note technique à ce sujet [est disponible via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/lib/technote_rdps-500_20160907_f.pdf).

Le document des spécifications techniques du SRPD 5.0.0 [est disponible ici](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_RDPS_5.0.0_f.pdf).


## Le mardi 15 décembre 2015

### Mise à jour du système régional de prévision déterministe (SRPD) 4.1.0 du Centre météorologique canadien (CMC)

Le mardi 15 décembre 2015, à compter de la passe de 1200 UTC, le Centre météorologique canadien (CMC) va procéder à la mise en œuvre opérationnelle de la version 4.1.0 de son système régional de prévision déterministe (SRPD).

Résumé des éléments majeurs que comporte cette mise à jour :

* Changements au modèle de prévision:
    * L'espacement horizontal entre les points de grille du modèle pilote global est réduite de 33 km à 25 km.
    * Les conditions latérales aux frontières du modèle pilote sont maintenant livrées à toutes les 30 minutes plutôt qu'aux 60 minutes.
* Changements aux observations:
    * Ajout des observations de radiance de 17 canaux de l'instrument satellitaire Advanced Microwave Sounding Unit (ATMS).
    * Ajout de 103 canaux de l'instrument satellitaire Cross-track Infrared Sounder (CrIS).
    * Ajout des observations de plus de 600 récepteurs GPS au sol - la plupart en Europe.
    * L'application des corrélations inter-canaux pour toutes les données de radiance infrarouge et micro-onde.

La note officielle annonçant ce changement [est disponible en cliquant ici](http://dd.meteo.gc.ca/doc/genots/2015/12/14/NOCN03_CWAO_142134___00045).

Une note technique à ce sujet [est disponible via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/lib/technote_rdps-410_20151215_f.pdf).

Le document des spécifications techniques du SRPD 4.1.0 [est disponible ici](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_RDPS_4.1.0_e.pdf). (en anglais)


## Le mardi 18 novembre 2014

### Mise à jour majeure du système régional de prévision déterministe (SRPD version 4.0.0) du Centre météorologique canadien (CMC)

Le mardi 18 novembre 2014, à compter de la passe de 1200 UTC, le Centre météorologique canadien (CMC) va procéder à la mise en œuvre opérationnelle de la version 4.0.0 de son système régional de prévision déterministe (SGPD).

Résumé des éléments majeurs que comporte cette mise à jour :

* La méthode d'assimilation 4D-EnVAR remplace le 4D-VAR.
    * Couplage avec le filtre de kalman d'ensemble (FKEn) pour recevoir les covariances d'erreur de prévisions.
* Changement aux observations
    * Amélioration au traitement des observations de radiosondes et d'avions.
    * Assimilation des observations de récepteurs GPS au sol.
    * Amélioration de la procédure de correction de biais des radiances satellitaires.
    * Canaux additionnels de données AIRS/IASI assimilées.
* Nouvelle analyse de la concentration de la glace de mer.

Une copie de la note officielle annonçant ce changement [est disponible via ce lien](http://dd.meteo.gc.ca/doc/genots/2014/11/14/NOCN03_CWAO_141824___00706).

Une note technique à ce sujet [est disponible via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/lib/technote_rdps-400_20141118_f.pdf).

## Le mardi 3 juillet 2012

### Mise à jour au binaire RDPS (pour la production de la variable PX)

## Mercredi le 13 février, 2013

### Mise à jour du système régional de prévision déterministe (SRPD version 3.1.0) du Centre météorologique canadien (CMC)

Le mercredi 13 février 2013, à compter de la passe de 1200 UTC, le Centre météorologique canadien (CMC) va procéder à la mise en œuvre opérationnelle de la version 3.1.0 de son système régional de prévision déterministe (SRPD)

Ce changement ce fait en conjonction avec la [mise en œuvre opérationnelle de son SGPD 3.0.0 qui aura lieu le même jour](../nwp_gdps/changelog_gdps_fr.md).

Grâce à ces changements, les prévisions du SRPD sont améliorées.

Veuillez consulter la documentation [à ce lien pour plus d'information à ce sujet](../nwp_gdps/changelog_gdps_fr.md).


## Mercredi, le 19 octobre, 2012

### Cinq minutes ajoutées au temps de coupure du système régional de prévision déterministe (SRPD version 3.0.0)

Le mercredi 19 octobre 2012, à compter de la passe de 1800 UTC, les passes [00,06,12,18]Z du SRPD debuteront à [00,06,12,18]Z+2:00 respectivement, ce qui permettra à ces passes de collecter 5 minutes additionnelles d'observations.

## Le mercredi, 3 octobre 2012

### Mise à jour majeure du système régional de prévision déterministe (SRPD version 3.0.0) du Centre météorologique canadien (CMC)

Le mercredi 3 octobre 2012, à compter de la passe de 1200 UTC, le Centre météorologique canadien (CMC) va procéder à la mise en œuvre opérationnelle de la version 3.0.0 de son système régional de prévision déterministe (SRPD), ci-après le SRPD-300. Cette nouvelle version amène une augmentation de la résolution de 15 à 10 km, incorpore un système d'assimilation 4D-VAR pour l'analyse en remplacement du schème 3D-VAR précédent, et apporte d'importants changements à la physique du modèle GEM. Ceci résulte en une amélioration notable des prévisions, notamment pour l'hiver.

Lors de cette implantation le temps de coupure a été réduit de 10 minutes et il est maintenant [00,06,12,18]Z+1:55

La verification objective de champs en altitude et en surface contre des données de radiosondage montre une amélioration significative à toutes les écheances de prévision. Ceci s'avère en général pour toutes les saisons évaluées, sur toutes les régions pour toutes les variables.

D'autres systèmes de prévision qui sont alimentés par le SRPD-300 ont tous été adaptés. Les changements dont ces autres systèmes ont fait l'objet ainsi que leur performance suite a ces changements sont décrits dans des bulletins GENOT et notes techniques à part qui sont aussi disponibles en cliquant sur le lien a la fin de ce message.

Une copie de la note officielle annonçant ce changement [est disponible via ce lien](http://dd.weatheroffice.ec.gc.ca/doc/genots/2012/10/02/NOCN03_CWAO_021702___00109).

Une note technique à ce sujet [est disponible via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/lib/op_systems/doc_opchanges/technote_rdps300_20121003_f.pdf).






