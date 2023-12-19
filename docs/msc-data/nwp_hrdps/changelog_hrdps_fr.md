[In English](changelog_hrdps_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [SHRPD](readme_hrdps_fr.md) > Changements au SHRPD

# Chronologie des changements apportés au Système à haute résolution de prévision déterministe (SHRPD)

## Le mardi 19 décembre 2023

### Mise à jour vers la version 2.2.0 des éléments du temps sur grille (WEonG) du Système à haute résolution de prévision déterministe (SHRPD) au Centre météorologique canadien

Le mardi 19 décembre 2023, à compter de la passe de 1200 UTC, le Centre météorologique canadien (CMC) a mis à jour les éléments du temps sur grille (WEonG) du Système à haute résolution de prévision déterministe (SHRPD) à la version 2.2.0.

Résumé des modifications que comporte cette mise à jour :

* Interpoler sur la grille les valeurs corrigées statistiquement des températures de surface aux points, fournis par UMOS en utilisant l'outil d'interpolation MIDAS
* Production des concepts intégrés sur des périodes de trois heures 
* Ajout du type de précipitation significative
* Modifications de l'algorithme de probabilité de détection des bourrasques de neige
* Activation du “Garry Morning Patch“ pour prolonger la présence du brouillard de rayonnement matinal jusqu'à ce que l'angle solaire atteigne un seuil spécifique

La note officielle annonçant ce changement est disponible [via ce lien](https://dd.meteo.gc.ca/doc/genots/2023/12/19/NOCN03_CWAO_191614___49612).

Une note technique à ce sujet est disponible [via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_notes/technote_weong-hrdps-220_f.pdf).

## Le jeudi 14 septembre 2023

### Ajout d’observations commerciales GNSS-RO de PlanetIQ dans le SHRPD

Le jeudi 14 septembre 2023, à compter de la passe de 0000 UTC, le Centre météorologique canadien (CMC) du service météorologique du Canada (SMC) a procédé à une mise à jour de la version 6.1.0 de son Système à haute résolution de prévision déterministe (SHRPD).

Seulement la composante de l'assimilation des données a été modifiée afin d'inclure les observations suivantes:

Ajout des observations commerciales GNSS-RO (Global Navigation Satellite System Radio Occultation) de la constellation de petits satellites GNOMES de PlanetIQ.

## Le mercredi 5 juillet 2023

### Ajout d’observations commerciales GNSS-RO de Spire dans le SHRPD

Le mercredi 5 juillet 2023, à compter de la passe de 0000 UTC, le Centre météorologique canadien (CMC) du service météorologique du Canada (SMC) a procédé à une mise à jour de la version 6.1.0 de son Système à haute résolution de prévision déterministe (SHRPD).

Seulement la composante de l'assimilation des données a été modifiée afin d'inclure les observations suivantes:

Ajout des observations commerciales GNSS-RO (Global Navigation Satellite System Radio Occultation) de la constellation de nanosatellites LEMUR de Spire.

### Le mercredi 15 février 2023

### Ajout des observations GPSRO du satellite Sentinel-6A dans le SHRPD

Le mercredi 15 février 2023, à compter de la passe de 0000 UTC, le Centre météorologique canadien (CMC) du service météorologique du Canada (SMC) a procédé à une mise à jour de la version 6.1.0 de son Système à haute résolution de prévision déterministe (SHRPD).

Seulement la composante de l'assimilation des données a été modifiée afin d'inclure les observations suivantes:

Ajout des observations GPSRO (Global Positioning System Radio Occultation) du satellite Sentinel-6A.

## Le jeudi 4 janvier 2023

### Remplacement des vecteurs vents dérivés à partir d’images satellites (Atmospheric Motion wind Vector) de GOES-17 par ceux de GOES-18 dans le SHRPD

Le mercredi 4 janvier 2023, à compter de la passe de 1800 UTC, le centre météorologique canadien (CMC) du service météorologique du Canada (SMC) a procédé à une mise à jour de la version 6.1.0 de son Système à haute résolution de prévision déterministe (SHRPD).

Seulement la composante de l'assimilation des données a été modifiée afin d'inclure les observations suivantes:

Remplacement des vecteurs vents dérivés à partir d’images satellites provenant du satellite GOES-17 par ceux de GOES-18.

## Le jeudi 3 novembre 2022

### Ajout des observations de surface provenant des bateaux en format BUFR dans le SHRPD

Le jeudi 3 novembre 2022, à compter de la passe de 0600 UTC, le Centre météorologique canadien (CMC) du service météorologique du Canada (SMC) a procédé à une mise à jour de la version 6.1.0 de son Système à haute résolution de prévision déterministe (SHRPD).

Seulement la composante de l'assimilation des données a été modifiée afin d'inclure les observations suivantes:

Ajout des observations de surface provenant des bateaux en format BUFR (Binary Universal Form for the Representation of meteorological data). Des observations TAC (Traditional Alphanumeric Codes) étaient déjà assimilées précédemment.

## Le mardi 28 juin 2022

### Mise à jour du SHRPD à la version 6.1.0 suite à la nouvelle infrastructure de calcul haute performance. 

Voir les détails via [ce lien](../changelog_multisystems_fr.md).

## Le mercredi 16 février 2022

### Ajout des observations GPSRO des satellites GRACE-C et GRACE-D dans le SHRPD

Le mercredi 16 février 2022, à compter de la passe de 0000 UTC, le Centre météorologique canadien (CMC) du service météorologique du Canada (SMC) a procédé à une mise à jour de la version 6.0.0 de son système à haute résolution de prévision déterministe (SHRPD).

Seulement la composante de l'assimilation des données a été modifiée afin d'inclure les observations suivantes:

Ajout des observations GPSRO (Global Positioning System Radio Occultation) des satellites GRACE-C et GRACE-D.

## Le mercredi 1er décembre 2021

### Mise à jour majeure vers la version 6.0.0 du Système à haute résolution de prévision déterministe (SHRPD) au Centre météorologique canadien

Le mercredi 1er décembre 2021, à compter de la passe de 1200 UTC, le Centre météorologique canadien (CMC) mettra à jour le Système à haute résolution de prévision déterministe (SHRPD) à la version 6.0.0.

Un résumé des innovations incluses dans cette mise à jour ainsi que de leurs impacts sur la performance du système [est disponible ici](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/fact_sheets/factsheet_hrdps-600_f.pdf).

La note officielle annonçant ce changement est disponible [via ce lien](http://dd.meteo.gc.ca/doc/genots/2021/11/26/NOCN03_CWAO_262118___50159).

Une note technique à ce sujet est disponible [via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_hrdps-600_f.pdf).

Le document des spécifications techniques du SHRPD v6.0.0 est disponible [via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_HRDPS_6.0.0_f.pdf).

## Le mardi 21 janvier 2020

### Mise à jours du SHRPD à la version 5.2.0 suite à la nouvelle infrastructure de calcul haute performance 

Voir les détails via [ce lien](../changelog_multisystems_fr.md).

## Le mercredi 3 juillet 2019

### Mise à jour majeure vers la version 5.1.0 du Système à haute résolution de prévision déterministe (SHRPD) au Centre météorologique canadien

Le mercredi 3 juillet 2019, à compter de la passe de 1200 UTC, le Centre météorologique canadien (CMC) mettra à jour le Système à haute résolution de prévision déterministe (SHRPD) à la version 5.1.0.

Résumé des modifications que comporte cette mise à jour :

* Les conditions initiales et latérales aux frontières proviennent maintenant du SRPD v7.0.0 au lieu du SRPD v6.0.0.
* Mise à jour du modèle GEM de v4.9.4 à v4.9.8
* Le SRPD-CGSL v3.4.0 remplace la version v3.3.0 comme modèle pilote pour le domaine du golfe du Saint-Laurent.

Une copie de la note officielle annonçant ce changement [est disponible via ce lien](http://dd.meteo.gc.ca/doc/genots/2019/06/28/NOCN03_CWAO_281830___34641).

Le document des spécifications techniques du SHRPD 5.1.0 [est disponible ici](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_HRDPS_5.1.0_f.pdf).

Une note technique à ce sujet [est disponible via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_hrdps-510_20190703_f.pdf).


## Le mardi 18 septembre 2018

### Mise à jour majeure vers la version 5.0.0 du Système à haute résolution de prévision déterministe (SHRPD) au Centre météorologique canadien

Le mardi 18 septembre 2018, à compter de la passe de 1200 UTC, le Centre météorologique canadien (CMC) mettra à jour le Système à haute résolution de prévision déterministe (SHRPD) à la version 5.0.0.
Résumé des modifications que comporte cette mise à jour:

* Les conditions initiales et laterales aux frontieres proviennent maintenant du [SRPD v6.0.0](../nwp_rdps/changelog_rdps_fr.md) au lieu du SRPD v5.1.0.
* Mise à jour du modèle GEM de v4.8-LTS.13 à v4.9.4.
* Nouveau schème de microphysique "Predicted Particle Properties (P3)" qui remplace celui de Milbrandt-Yau (MY2).
* Inclusion du schème de paramétrisation urbain Town Energy Balance (TEB)

Une copie de la note officielle annonçant l'implementation de ces modifications [est disponible via ce lien](http://dd.meteo.gc.ca/doc/genots/2018/09/17/NOCN03_CWAO_171332___49260).

Une note technique avec plus de détails sur SHRPD 5.0.0 est disponible [via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_hrdps-500_20180918_e.pdf) (en anglais pour l'instant).


## Le jeudi 14 décembre 2017

### Le Système à haute résolution de prévision déterministe (SHRPD) est déclaré opérationnel au Centre météorologique canadien

En date du 14 décembre 2017, suite à plusieurs ans d’exécution en mode expérimental, le Centre météorologique canadien (CMC) déclare opérationnel le Système à haute résolution de prévision déterministe (SHRPD v4.4.0).

La note officielle annonçant ce changement [est disponible via ce lien](http://dd.meteo.gc.ca/doc/genots/2017/12/13/NOCN03_CWAO_132058___00004).

Une note technique avec plus de détails sur la version 4.2.0 de ce système (en anglais) [est disponible en cliquant ici](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_hrdps-420_20160907_e.pdf).


## Le mercredi 7 septembre 2016

### Mise à jour du Système à haute résolution de prévision déterministe (SHRPD) 4.2.0 du Centre météorologique canadien

Le mercredi 7 septembre 2016, à compter de la passe de 1200 UTC, le Centre météorologique canadien (CMC) va procéder à la mise en œuvre opérationnelle de la version 4.2.0 de son Système à haute résolution de prévision déterministe (SHRPD).

Résumé des éléments majeurs que comporte cette mise à jour :

* Changements au modèle de prévision :
    * Le modèle GEM utilisé par le SHRPD change de la version 4.7.3 à la version 4.8.2.
    * Introduction d'un effet d'hystérésis dans le shéma de mélange turbulant qui améliore surtout la prévision du type de précipitation.
    * Modification de la diffusion horizontale pour les variables de quantité de mouvement (opérateur del-2 au lieu de del-4) pour rendre le champ de précipitation moins bruyant.
    * Changements mineurs à la composante d'assimilation des données de surface (CaLDAS).
* Changements à la configuration des grilles :
    * Un nouveau domaine de prévision a été ajouté au SHRPD. Ce domaine qui est appelé 'Nord' couvre les régions arctiques du Canada.
    * En conséquence les prévisions sur les domaines dits 'Arctique' et 'Lancaster', seront discontinuées.
    * Voir [cette image](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/hrdps/hrdps_4.2.0_grids_snapshot.png) qui illustre ces changements.

La note officielle annonçant ce changement [est disponible en cliquant ici](http://dd.meteo.gc.ca/doc/genots/2016/09/02/NOCN03_CWAO_022101___00743).

Une note technique à ce sujet (en anglais) [est disponible en cliquant ici](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/lib/technote_hrdps-420_20160907_e.pdf).


## Le mardi 15 décembre 2015

### Mise à jour du Système à haute résolution de prévision déterministe (SHRPD) 4.1.0 du Centre météorologique canadien

Le mardi 15 décembre 2015, à compter de la passe de 1200 UTC, le Centre météorologique canadien (CMC) va procéder à la mise en œuvre opérationnelle de la version 4.1.0 de son Système à haute résolution de prévision déterministe (SHRPD).

Résumé des éléments majeurs que comporte cette mise à jour :

* L'utilisation du schéma de convection implicite Kain & Fritsch,
* Une correction pour les évènements de précipitation verglacante qui étaient largement sous-estimés dans le SHRPD-4.0.0

La note officielle annonçant ce changement [est disponible en cliquant ici](http://dd.meteo.gc.ca/doc/genots/2015/12/12/NOCN03_CWAO_122240___00075).

Une note technique à ce sujet (en anglais) [est disponible en cliquant ici](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/lib/technote_hrdps-410_20151215_e.pdf).


## Le mardi 18 novembre 2014

### Mise à jour majeure du Système à haute résolution de prévision déterministe (SHRPD) 4.0.0 au Centre météorologique Canadien

Le mardi 18 novembre 2014, à compter de la passe de 1200 UTC, le Centre météorologique canadien (CMC) va procéder à une mise à jour majeure de son système expérimental à haute résolution de prévision déterministe (SHRPD) version 4.0.0.

Une copie de la note officielle annonçant ce changement [est disponible via ce lien](http://dd.meteo.gc.ca/doc/genots/2014/11/17/NOCN03_CWAO_171924___00922).

Une note technique à ce sujet [est disponible via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/lib/technote_hrdps-400_20141118_f.pdf).


## Le vendredi, 12 juillet 2013

### Ajustements au cacul du temps violent d'été et au domaine arctique du Système à haute résolution de prévision déterministe (SHRPD - version 3.0.1) au Centre meteorologique canadien

Le CMC a récemment implanté 2 ajustements au SHRPD. Avec ces changements la version est maintenant 3.0.1

Le premier ajustement à partir de 18Z le 21 juin 2013, est une correction au code utilisé par tous les domaines SHRPD pour le calcul des paramètres de temps violent d`été.

Le deuxième ajustement s`applique seulement au domaine du lam arctique et est un agrandissement et un léger déplacement du domaine lam arctique. Ce changement à la grille du lam arctique a été implanté à partir de la passe 06Z du 12 juillet 2013.

L'image : [au lien en cliquant ici](http://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/hrdps/20130710_HRDPSArcticGrid_BluePrevious_BlackNew.jpg) compare la grille originale du domaine arctique en carré bleu avec la nouvelle grille étendue implantée le 12 juillet.

Ce changement au domaine SHRPD arctique fait suite à des demandes des météorologues de certains bureaux régionaux (PNR, CIS) qui demandaient que la grille du domaine arctique soit ajustée pour pouvoir offrir des prévisions qui pourraient mieux servir les clients dans la baie d'Ungava et dans les portions est de la baie d'Hudson, surtout pendant la période estivale importante.

Les utilisateurs de la station de travail Ninjo doivent être bien conscients qu'ils continueront de recevoir la même configuration de fichiers grib2 pour le SHRPD arctique. Cela signifie qu'à partir du 12 juillet 2013, les utilisateurs de Ninjo ne devraient pas utiliser les données SHRPD arctique qui seraient disponibles à l'est de la longitude 60 ouest dans les fichiers grib2 du SHRPD arctique.

Le CMC a ajusté le contenu des fichiers grib2 de données SHRPD arctique qui sont envoyées au datamart. Ces fichiers grib2 afficheront des données couvrant le nouveau domaine du SHRPD arctique. La documentation associée à ces fichiers grib2 ne pourra être mise à jour qu`à une date ultérieure.

Une copie de la note officielle annoncant ce changement [est disponible via ce lien](http://dd.weatheroffice.ec.gc.ca/doc/genots/2013/07/12/NOCN03_CWAO_122020___01071).


## Le mercredi, 3 octobre 2012

### Mise à jour du Système à haute résolution de prévision déterministe (SHRPD - version 3.0.0) au Centre meteorologique canadien

Le mercredi 3 octobre 2012, debutant avec le lancement d'une nouvelle passe de 1800 UTC pour le domaine ouest, le Centre météorologique Canadien (CMC) effectuera une mise à jour du Système à haute résolution de prévision détérministe (SHRPD) à 2.5 km de résolution.

Ces modifications impliquent un changement de version du modèle GEM pour tous les domaines de prévision du SHRPD. Pour le domaine ouest, la configuration de pilotage, la frequence des passes et la periode de prevision sont aussi modifiées.

Cette mise à jour du SHRPD est fait conjointement avec les changements majeurs qu'on apporte au système régional de prévision dététerministe dans sa version 3.0.0 (SRPD-v3) qui fournit les conditions initiales et laterales aux frontieres pour le SHRPD. Pour des informations detaillées sur les changements au SRPD-300 s.v.p. [vous référer à l'info en cliquant ici](../nwp_rdps/changelog_rdps_fr.md).

Pour le domaine ouest, il y a maintenant 2 cycles de prévision par jour, couvrant chacun une période de 42 heures á haute résolution. Le cycle du matin utilise des donnees plus tôt et ce cycle sera indiqué par 06 UTC dans son nom (plutôt que 12 UTC auparavant). Le nouveau cycle pour le domaine ouest de l'après midi affiche 18 UTC dans son nom.

Tous les domaines SHRPD continuent avec leur statut expérimental. Nous prévoyons déclarer un support pleinement opérationnel pour le domaine ouest dans un futur rapproché et une note suivra pour annoncer ce changement.

Tous les produits demeurent disponibles sans délai additionnel. Pour le domaine ouest, l'ajout d'une deuxième passe à 1800 UTC ajoute une série de produits semblables aux produits de la passe de 0600 UTC. Cependant, pour un certain temps, malgré le prolongement de la durée de prévision jusqu'à 42 heures pour le domaine ouest, les champs météorologiques ne seront visibles dans l'outil de visualisation ninjo que jusqu'à 24 heures de prévision

Une copie de la note officielle annoncant ce changement [est disponible via ce lien](http://dd.weatheroffice.ec.gc.ca/doc/genots/2012/10/02/NOCN03_CWAO_021952___00094).

Une note technique à ce sujet [sera disponible sous peu en cliquant ici](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/lib/op_systems/doc_opchanges/technote_hrdps_20121003_f.pdf).


## Le jeudi 22 décembre 2011

### Le Centre Météorologique Canadien corrige l'analyse de neige du SHRPD

Un correctif à la grille de l'analyse de neige du Système à haute résolution de prévision déterministe (SHRPD) a été fait commencant avec l'analyse de 06 UTC du 22 décembre 2011.

Avec ce correctif, le SHRPD sera maintenant identifié comme la version 2.2.1



