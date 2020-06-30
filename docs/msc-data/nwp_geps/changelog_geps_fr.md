[In English](changelog_geps_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [SGPE](readme_geps_fr.md) > Changements au SGPE

# Chronologie des changements apportés au Système global de prévision d'ensemble (SGPE)

## Le vendredi 26 juin 2020

### Ajout des observations GPSRO des satellites COSMIC-II

Le vendredi 26 juin 2020, à compter de la passe de 0000 UTC, le Centre météorologique canadien (CMC) du service météorologique du Canada (SMC) a procédé à une mise à jour de la version 6.1.0 de son système global de prévision d'ensemble (SGPE).

Seulement la composante de l'assimilation des données a été modifiée afin d'inclure les observations suivantes:

Ajout des observations GPSRO (Global Positioning System Radio Occultation) des satellites COSMIC II.

## Le mercredi 29 avril 2020

### Ajout des observations GPSRO des satellites PAZ et KOMPSAT-5

Le mercredi 29 avril 2020, à compter de la passe de 0000 UTC, le Centre météorologique canadien (CMC) du service météorologique du Canada (SMC) a procédé à une mise à jour de la version 6.1.0 de son système global de prévision d'ensemble (SGPE).

Seulement la composante de l'assimilation des données a été modifiée afin d'inclure les observations suivantes:

Ajout des observations GPSRO (Global Positioning System Radio Occultation) des satellites PAZ et KOMPSAT-5.

## Le mardi 28 avril 2020

### Ajout des observations AMV du satellite MetOp-3/C

Le mardi 28 avril 2020, à compter de la passe de 0600 UTC, le Centre météorologique canadien (CMC) du service météorologique du Canada (SMC) a procédé à une mise à jour de la version 6.1.0 de son système global de prévision d'ensemble (SGPE).

Seulement la composante de l'assimilation des données a été modifiée afin d'inclure les observations suivantes:

Ajout des observations AMV (Atmospheric Motion Vector) du satellite MetOp-3/C.

## Le mardi 21 janvier 2020

### Mise à jours du SGPE à la version 6.1.0 suite à la nouvelle infrastructure de calcul haute performance. 

Voir les détails via [ce lien](../changelog_multisystems_fr.md).

## Le mardi 23 juillet 2019

### Ajout d'observations satellitaires dans les systèmes de prévision suivants du Centre météorologique canadien (CMC): Le système global de prévision d'ensemble (SGPE)

Le mardi 23 juillet 2019, à compter de la passe de 0600 UTC, le Centre météorologique canadien (CMC) a procédé à une mise à jour du système global de prévision d'ensemble (SGPE).

Les composantes d'assimilation de données du SGPE ont été modifiées pour utiliser des observations supplémentaires dans sept familles d'observations. Toutes ces familles étaient déjà utilisées, ces ajouts observations visent principalement à augmenter la robustesse des systèmes d'assimilation.

Les détails de cette mise à jour sont disponibles dans la copie de la note officielle annonçant ce changement [via ce lien](http://dd.meteo.gc.ca/doc/genots/2019/07/23/NOCN03_CWAO_231247___30255).

* Le document des spécifications techniques pour le SGPE 6.0.0 est disponible [via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_GEPS_6.0.0_f.pdf).

## Le mercredi 3 juillet 2019

#### Mise à jour majeure du système global de prévision d'ensemble (SGPE version 6.0.0) du Centre météorologique canadien (CMC)

Le mercredi 3 juillet 2019, à compter de la passe de 1200 UTC, le Centre météorologique canadien (CMC) va procéder à la mise en œuvre opérationnelle de la version 6.0.0 de son système global de prévision d'ensemble (SGPE). Résumé des éléments majeurs que comporte cette mise à jour :

* Changements à la composante composante de prévision :
    * Le modèle atmosphérique est mis à niveau vers la version GEM 4.8-LTS.16
    * Le modèle atmosphérique est couplé avec le modèle océanique NEMO 3.6
    * Les conditions initiales de l'océan et de la glace de mer proviennent de l'analyse du [SGPOG (mise à jour à la version 3.0.0 au même moment)](../nwp_giops/changelog_giops_fr.md) du CMC
    * Conditions initiales de la surface terrestre proviennent d'une pseudo-analyse de surface qui est réalisée à une résolution de 25 km et avec des forçages de GEM 4.8
* Changements à la composante d'assimilation :
    * La présente version intègre une configuration de gain hybride-cepmmt, qui recentre tous les membres d'ensemble autour de la moyenne des analyses FKEN et 4DENVAR
    * On utilise une nouvelle analyse de la température de surface de la mer et de couverture de la glace de mer
    * Le nouveau FKEN assimile maintenant les données sur la dépression du point de rosée (t-td) obtenues par radiosonde jusqu'à 100 hpa au lieu de 200 hpa


Une copie de la note officielle annonçant ce changement [est disponible via ce lien](http://dd.meteo.gc.ca/doc/genots/2019/06/28/NOCN03_CWAO_281715___16589).

Une note technique à ce sujet [est disponible via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_geps-600_f.pdf).

Le document des spécifications techniques du SGPE 6.0.0 [est disponible ici](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_GEPS_6.0.0_f.pdf).


## Le mardi 18 septembre 2018

#### Mise à jour majeure du système global de prévision d'ensemble (SGPE version 5.0.0) du Centre météorologique canadien (CMC)

Le mardi 18 septembre 2018, à compter de la passe de 1200 UTC, le Centre météorologique canadien (CMC) va procéder à la mise en œuvre opérationnelle de la version 5.0.0 de son système global de prévision d'ensemble (SGPE). Résumé des éléments majeurs que comporte cette mise à jour :

* Changements communs entre la composante d'assimilation et prévision
    * Mise à jour de la version du modèle GEM de la version 4.6.10 à 4.8.lts13:
    * La grille globale gaussienne 800x400 est remplaçée par une grille Yin-Yang grid à 39 km de résolution
    * Les champs géophysiques sont maintenant générés par le logiciel genphysX au lieu de GENESIS.
* Changements à la composante assimilation
    * Introduction de l'approche incrémentale 4D de mise à jour de l'analyse (IAU:Incremental Analysis Update).
    * Le modèle a un toit plus élevé (de 2 hpa jusqu'a 0.1 hpa) avec 81 niveaux verticaux au lieu de 74.
    * Ajout d'observations infrarouge (AIRS, IASI and CrIS).
    * Amélioration du triage aux observations des vents satellitaires, des radiance, des aeronef et des diffusiomètre.
    * Le modèle rapide de transfert radiatif pour l'assimilation de la radiance RTTOV a été mis à niveau de la version 10 à la version 12.
* Changements à la composante Prévision uniquement
    * Le modèle a un toit plus élevé (de 2 hpa jusqu'a 0.1) avec 45 niveaux verticaux au lieu de 41.
    * Une nouvelle méthode est utilisée pour générer les chaînes de Markov.
* La période des reprévision est maintenant de 1998 à 2017 plutôt que 1995 à 2014.
* Les sorties sont dorénavant disponibles sur une grille "usager" avec une résolution de 25 km.


Une copie de la note officielle annonçant ce changement [est disponible via ce lien](http://dd.meteo.gc.ca/doc/genots/2018/09/17/NOCN03_CWAO_171242___10232).

Une note technique à ce sujet [est disponible via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_geps-500_20180918_f.pdf).

Le document des spécifications techniques du SGPE 5.0.0 [est disponible ici](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_GEPS_5.0.0_f.pdf).


## Le mardi 15 décembre 2015

#### Mise à jour du système global de prévision d'ensemble (SGPE version 4.1.1) du Centre météorologique canadien (CMC)

Le mardi 15 décembre 2015, à compter de la passe de 1200 UTC, le Centre météorologique canadien (CMC) va procéder à la mise en œuvre opérationnelle de la version 4.1.1 de son système global de prévision d'ensemble (SGPE).

Résumé des éléments majeurs que comporte cette mise à jour :

* La diffusion numérique du champ de la temperature potentielle est maintenant appliquées à chaque membre de l'ensemble (au lieu de seulement la moitie des membres).
* L'ajout d'un gradient d'amortissement qui limite la diffusion près des poles.
* Nouvelles statistiques d'erreurs d'observations pour les données de radiance et les observations de type "GPS-RO" (GPS Radio-Occultation).
* De nouvelles observations de radiance du Advanced Microwave Sounding Unit (ATMS).
* L'ajout d'observations GPS-RO des satellites TanDEM et GRACE-B.
* La période de reprévision est allongée de 18 à 20 ans.

La note officielle annonçant ce changement [est disponible en cliquant ici](http://dd.meteo.gc.ca/doc/genots/2015/12/14/NOCN03_CWAO_142245___00047).

Une note technique à ce sujet [est disponible via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/lib/technote_geps-411_20151215_f.pdf).

Le document des spécifications techniques du GEPS 4.1.1 [est disponible ici](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_GEPS_4.1.1_f.pdf).


## Le mardi 18 novembre 2014

#### Mise à jour majeure du système global de prévision d'ensemble (SGPE version 4.0.0) du Centre météorologique canadien (CMC)

Le mardi 18 novembre 2014, à compter de la passe de 1200 UTC, le Centre météorologique canadien (CMC) va procéder à la mise en œuvre opérationnelle de la version 4.0.0 de son système global de prévision d'ensemble (SGPE).

Résumé des éléments majeurs que comporte cette mise à jour :

* Couplage avec le 4D-EnVAR pour fournir les covariances d'erreur de prévisions
* La taille de l'ensemble du FKEn augmente de 192 à 256 membres
* La résolution horizontale du FKEn et de la prévision passe de 66km à 50 km
* Le pas de temps du modèle GEM passe de 20 à 15 minutes
* Le toit est plus haut à environ 1.45 hPa (1.78 hPa avant)
* Changements à la correction de biais des observations et à l'opérateur RTTOV

La note officielle annonçant ce changement [est disponible en cliquant ici](http://dd.meteo.gc.ca/doc/genots/2014/11/14/NOCN03_CWAO_141746___01238).

Une note technique à ce sujet [est disponible via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/lib/technote_geps-400_20141118_f.pdf).

Une note technique à propos des améliorations au système de re-prévisions [est disponible via ce lien (en anglais seulement pour le moment)](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/lib/Tech_Note_GEPS400_reforecast_v1.1_E.pdf).


## Le mercredi 4 décembre 2013

#### Mise à jour majeure du système global de prévision d'ensemble (SGPE version 3.1.0) du Centre météorologique canadien (CMC)

Le mercredi 4 décembre 2013, à compter de la passe de 1200 UTC, le Centre météorologique canadien (CMC) va procéder à la mise en œuvre opérationnelle de la version 3.1.0 de son système global de prévision d'ensemble (SGPE).

Dans cette nouvelle version du SGPE, une nouvelle version du modèle gem (de 4.4.1 vers 4.4.5) sera utilisée contenant des options additionnelles.  Ce changement de nature purement technique n’engendre aucune différence dans les prévisions du SGPE, mais permet un entretien plus facile du système et une plus grande cohérence avec les autres systèmes de prévisions du CMC.

Du coté de l’assimilation, les données de radiances ATOV et les vents polaires avhrr d’un satellite additionnel, METOP-B, sont maintenant assimilés.  Également, il y a eu une mise à jour des coefficients spectroscopiques utilisés par le modèle de transfert radiatif RTTOV pour calculer les observations simulées des instruments AMSUB et MHS pour tous les satellites. Quoique l’impact de ces changements sur les prévisions soit neutre, ils permettent d’améliorer la  robustesse de la composante d’assimilation du système. 

Pour la prévision, le changement le plus important est dans le traitement de la température de surface de la mer (Tm). Dans le nouveau GEPS,  Tm  évoluera avec l’échéance temporelle de prévision en utilisant la méthode de la persistance de l’anomalie (écart avec la climatologie).  La valeur de Tm changera donc linéairement avec le temps (interpolation journalière) à partir de la valeur initiale de l’analyse du CMC vers la prochaine valeur de la climatologie de Tm à la moitié du mois, plus l'anomalie de Tm calculée initialement.

Aussi, des prévisions mensuelles (32 jours) seront produites une fois par semaine chaque jeudi à 00z.  Bien que les données de ces prévisions seront disponibles avec cette mise en œuvre, l’introduction de produits spécifiques aux prévisions mensuelles n’est planifiée que pour plus tard en 2014.

Un autre élément nouveau dans le SGPE 3.1.0 est l’ajout de prévisions d’ensemble historiques pour les derniers 18 ans qui seront produites à chaque semaine avec un ensemble réduit de 4 membres (au lieu de 20).  Les sorties de cette base de données de re-prévisions seront utilisées pour générer les statistiques du climat du modèle pour les prévisions mensuelles et,  éventuellement, pour calculer l’indice de prévision extrême (IPE, acronyme anglais EFI) ainsi que pour calibrer les prévisions probabilistes.

La note officielle annonçant ce changement [est disponible en cliquant ici](http://dd.meteo.gc.ca/doc/genots/2013/12/03/NOCN03_CWAO_032255___01160).

Une note technique à ce sujet [est disponible via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/lib/technote_geps310_20131204_f.pdf).


## Le mercredi, 13 février 2013

#### Mise à jour majeure du système global de prévision d'ensemble (SGPE version 3.0.0) du Centre météorologique canadien (CMC)

Le mercredi 13 février 2013, à compter de la passe de 1200 UTC, le Centre météorologique canadien (CMC) va procéder à la mise en œuvre opérationnelle de la version 3.0.0 de son système global de prévision d'ensemble (SGPE).

Des changements majeurs sont faits tant à la portion d'assimilation de données (filtre kalman d'ensemble ou FKEn) qu'à celle de pévision du système.

Les changements communs aux composantes d'assimilation et de prévision incluent: nouvelle version du modèle GEM (soit la version version 4.4.1) avec une physique améliorée, réduction du pas de temps du modèle de 30 à 20 minutes, l'utilisation d'un filtre pour lisser le champ topographique, utilisation d'un seul schème de surface (ISBA) au lieu de deux.

Les changements à la composante d'assimilation de données FKEn seulement incluent: augmentation avec l'altitude de la longueur de localisation horizontale au lieu d'etre une constante, la résolution horizontale a été accrue passant de 400x200 points (environ 100 km) vers 600x300 points (environ 66km), le nombre de niveaux verticaux est augmenté à 74 et le toit du modele demeure à 2 hPa, l'assimilation d'un plus grand volume d'observations de radiance AMSU: les données sont sélectionnées à chaque 150 km au lieu de chaque 250 km, amélioration de la correction de biais des observations, par le partage de celle venant de la nouvelle [version 3.0.0 du système global de prévision déterministe (SGPD), mise en œuvre simultanement](../nwp_gdps/changelog_gdps_fr.md).

Les changements à la composante de prévisions seulement incluent: changement à la manière de perturber les tendances physiques pour les précipitations convectives, l'enveloppe latitudinale tropicale de limitation des perturbations est enlevée, les perturbations des tendances physiques sont appliquées à chaque niveau vertical sauf au dernier niveau près du sol, de la diffusion a été ajoutée dans le schème d'advection, une perturbation du coefficient de trainée du blocage orographique a été ajoutée, le facteur d'ajustement alpha du schème de rétroaction d'énergie cinétique stochastique est maintenant 0.8 pour mieux s'ajuster au nouveau pas de temps de 20 minutes.

Des tests approfondis du SPGE-3.0.0 ont été faits lors de la phase finale de developpement (juillet-aout 2011 et fevrier-mars 2011) ainsi que durant une passe parallèle de novembre 2012 à janvier 2013. Le nouveau FKEn inclus dans cette implantation produit généralement des impacts positifs importants pour les analyses et les champs d'essai des vents et des températures pour presque toute la colonne atmosphérique.

Le SGPE-3.0.0 apporte une amélioration majeure des prévisions de 16 jours des champs atmospheriques dans les regions extra-tropicales.

Les prévisions atmosphériques du système régional de prévision d'ensemble (SRPE) bénéficieront grandement d'avoir de meilleures conditions initiales et aux frontières latérales de la part du SGPE-3.0.0.

Les prévisions pour les échéances du jour 1 à 10 des champs atmospheriques du système de prevision d'ensemble nord-americain (SPENA) seront grandement améliorées par l'utilisation du SGPE-3.0.0.

Grâace à des améliorations d'équipement ordinateur qui coincident avec cette implantation, certains produits du SGPE devraient maintenant être prêts entre dix (10) et cent vingt (120) minutes plus tôt que les temps de production actuels.

La note officielle annonçant ce changement [est disponible en cliquant ici](http://dd.weatheroffice.ec.gc.ca/doc/genots/2013/02/08/NOCN03_CWAO_081505___00885).

Une note technique à ce sujet [est disponible via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/lib/op_systems/doc_opchanges/technote_geps300_20130213_f.pdf).
