[In English](changelog_raqdps_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > Changements au SRPDQA

# Chronologie des changements apportés au Système régional de prévision déterministe de la qualité de l'air (SRPDQA)

## Le mardi 21 janvier 2020

### Mise à jours de SRPDQA à la version 22.0.0 suite à la nouvelle infrastructure de calcul haute performance. 

Voir les détails via [ce lien](../changelog_multisystems_fr.md).

## Le mercredi 3 juillet 2019

### Mise à jour du système régional de prévision déterministe de la qualité de l'air (SRPDQA)

Le mercredi 3 juillet 2019, à compter de la passe de 1200 UTC, le Centre météorologique canadien (CMC) mettra à jour le système régional de prévision déterministe de la qualité de l'air (SRPDQA) en remplaçant la version 020 par la version 021.

Résumé des éléments que comporte cette mise à jour :

* Les analyses météorologiques et le modèle pilote proviennent maintenant du [SRPD v7.0.0](/../nwp_rdps/changelog_rdps_fr.md#le-mercredi-3-juillet-2019) plutôt que du SRPD v6.0.0.
* Mise à jour de GEM de la version v4.8-LTS.16 à la version GEM v5.0.0. Pour plus d'informations sur GEM-5, veuillez consulter ce [document (en anglais)](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_notes/GEM5_paper_submitted_JAMES_20190614.pdf).
* Amélioration dans le calcul de la chimie du modèle.

Une copie de la note officielle annonçant ce changement dans SRPDQA est disponible [via ce lien](https://dd.meteo.gc.ca/doc/genots/2019/06/28/NOCN03_CWAO_281933___34219).

Une note technique pour SRPDQA avec plus de détails sur ces changements est disponible [sur cette page](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_notes/technote_raqdps-021_20190703_f.pdf).

## Le mardi 18 septembre, 2018

### Mise à jour du système régional de prévision déterministe de la qualité de l'air (SRPDQA) et du système de prévision FireWork

Le mardi 18 septembre 2018, à compter de la passe de 1200 UTC, le Centre météorologique canadien (CMC) mettra à jour le système régional de prévision déterministe de la qualité de l'air (SRPDQA) et le système complémentaire FireWork en remplaçant la version 019 par la version 020.

Résumé des éléments que comporte cette mise à jour :
* Les analyses météorologiques et le modèle pilote proviennent maintenant du [SRPD v6.0.0](/../nwp_rdps/changelog_rdps_fr.md#le-mardi-18-septembre-2018) plutôt que du SRPD v5.1.0.
* Adoption de la configuration SRPD v6.0.0, comprenant le recyclage des principales variables physiques et l'approche incrémentale 4D de mise à jour de l'analyse (IAU:Incremental Analysis Update).
* L'implementation de la nouvelle version du code du modèle (v2.3.1), pour améliorer la vitesse de traitement et augmenter la robustesse, ainsi que l'amélioration de la chimie (dépôt sec en phase gazeuse sur les surfaces enneigées et la glace marine).
* Introduction d’un nouvel ensemble d'émissions basé sur des inventaires nationaux d’émissions plus récents.

La note officielle annonçant ce changement est disponible [en cliquant ici](https://dd.meteo.gc.ca/doc/genots/2018/09/17/NOCN03_CWAO_171403___42412).

Une note technique avec plus de détails sur ces changements est disponible [sur cette page](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_notes/technote_raqdps-v20_20180918_f.pdf).

## Le mercredi 7 septembre 2016

### Mise à jour majeure du système régional de prévision déterministe de la qualité de l'air (SRPDQA)

Le mercredi 7 septembre 2016, à compter de la passe de 1200 UTC, le Centre météorologique canadien (CMC) mettra à jour le système régional de prévision déterministe de la qualité de l'air (SRPDQA) en remplaçant la version 015 par la version 016.

Résumé des éléments majeurs que comporte cette mise à jour :

* Le modèle GEM utilisé par le SRPDQA change d'une version modifiée de v4.6.2 à v4.8.0.

* Les analyses météorologiques et le modèle pilote sont dorénavant liés au SRPD 5.0.0 plutôt qu'au SRPD 4.2.0.

* La grille a été tournée pour correspondre à la nouvelle grille du SRPD 5.0.0 (voir la [description du SRPD 5.0.0¸](/../nwp_rdps/changelog_rdps_fr.md#le-mercredi-7-septembre-2016)).

* Un changement important à été fait dans l'utilisation du paramètre de Monin-Obukov.

* Quelques autres corrections mineures.

La note officielle annonçant ce changement est disponible [en cliquant ici](https://dd.meteo.gc.ca/doc/genots/2016/09/02/NOCN03_CWAO_022109___00871).

Une note technique avec plus de détails sur ces changements reste à venir sur cette page.

## Le jeudi 7 avril 2016

### Mise à jour majeure du système régional de prévision déterministe de la qualité de l'air (SRPDQA)

Le jeudi 7 avril 2016, à compter de la passe de 1200 UTC, le Centre météorologique canadien (CMC) du service météorologique du Canada (SMC) mettra à jour le système régional de prévision déterministe de la qualité de l'air (SRPDQA) en remplaçant la version 013 (antérieurement version 1.5.4) par la version 015.

Résumé des éléments majeurs que comporte cette mise à jour :

* Légère modification de la taille de la grille du modèle, mais la résolution horizontale (10 km) et l'orientation de la grille restent inchangées.

* Le modèle GEM utilisé par le SRPDQA change de la version 3.3.8.2 à la version 4.6.2.

* Nouvelles conditions latérales chimiques aux frontières.

* Mises à jour du module de la chimie, y compris deux corrections de bogues importants.

La note officielle annonçant ce changement est disponible [en cliquant ici](https://dd.meteo.gc.ca/doc/genots/2016/04/05/NOCN03_CWAO_051925___00885).

Une note technique avec plus de détails sur ces changements reste à venir sur cette page.

## Le jeudi 11 juin 2015

### Mise à jour du système régional de prévision déterministe de la qualité de l'air (SRPDQA) au Centre météorologique canadien (CMC)

Le Centre météorologique canadien (CMC) a implémenté un nouveau jeu de fichiers d'émissions pour le système régional de prévision déterministe de la qualité de l'air (SRPDQA). Les nouvelles émissions sont basé sur l'inventaire national 2010 du Canada / l'inventaire national 2011 des États-Unis, ce qui est une mise à jour de l'inventaire national 2006 du Canada / l'inventaire national 2005 des États-Unis.

Une copie de la note officielle annonçant ce changement est disponible [via ce lien](https://dd.meteo.gc.ca/doc/genots/2015/06/10/NOCN03_CWAO_101245___00612).

Plus d'information technique/scientifique sur ce système est disponible [via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/lib/op_systems/doc_opchanges/Technical_Note_GEM-MACH10_v1.5.3+SET2.1.1_Emissions_9Nov2015.pdf).

## Le mardi 18 novembre 2014

### Mise à jour mineure du Système régional de prévision déterministe qualité de l'air (SRPDQA) 1.5.3 au Centre météorologique Canadien (CMC)

Le mardi 18 novembre 2014, à compter de la passe de 1200 UTC, le Centre météorologique canadien (CMC) va procéder à une mise à jour mineure Système régional de prévision déterministe qualité de l'air. La version du système passe de 1.5.2 à 1.5.3. Ci-dessous les changements inclus dans cette mise à jour:

1. Le système s'alimente maintenant du système régional de prévision déterministe (SRPD) 4.0.0.

2. Le modèle GEM utilisé dans le SRPDQA est passé de la version 3.3.8.1 à 3.3.8.2.

## Le mardi 26 février 2013

### Mise à jour du système régional de prévision déterministe de la qualité de l'air (SRPDQA - version 1.5.1) au Centre météorologique canadien (CMC)

Le mardi 26 février 2013 débutant a partir de l'intégration de 1200 UTC, le Centre météorologique canadien (cmc) mettra en opération la version 1.5.1 du SRPDQA celle-ci remplace la version 1.5.0 (SRPDQA-1.5.0). La nouvelle version contient trois correctifs à la chimie qui apportent une amélioration significative au système opérationnel de prévision de la qualité de l'air.

Durant l'été 2012, trois bogues ont été découverts dans le SRPDQA, ceux-ci étaient présents depuis l'implantation opérationnelle de 2009. Ces bogues affectaient le dépôt humide des espèces chimiques par la précipitation convective, ainsi que le mélange vertical. Ce dernier se manifestant particulièrement lors de conditions atmosphériques stables.

La performance du SRPDQA-1.5.1 a été mesurée durant l'été et l'hiver 2012. Les statistiques utilisées pour l'évaluation objective indiquent une amélioration des prévisions du SRPDQA-1.5.1 comparativement à celles du SRPDQA-1.5.0 pour les trois polluants principaux: ozone (O3), particules fines (PM2.5) et dioxyde d'azote (NO2). L'amélioration la plus significative avec le SRPDQA-151 est observée pour la prévision des concentrations des PM2.5 en hiver, surtout en ce qui concerne les maximums quotidiens prévus. Le nouveau système représente mieux les valeurs observées avec une importante réduction du maximum quotidien dans les cas de sur-prévisions des PM2.5. Les scores catégoriques, tels que le pourcentage correct, l'indice de succès critique et le ratio de fausses alertes du nouveau système affichent une amélioration avec le SRPDQA-1.5.1, tant en été qu'en hiver, pour les trois polluants: O3, NO2 et PM2.5.

Pour environ 90% des stations de mesure, UMOS-AQ se comporte de façon similaire autant l'été que l'hiver. Lorsque les sorties du modèle SRPDQA-1.5.0 et du SRPDQA-1.5.1 sont comparées. pour la majorité des autres stations, la performance d'UMOS-AQ est améliorée avec le SRPDQA-1.5.1.

Il n'y aura aucun changement sur la disponibilité des produits résultant de cette implantation.

Une copie de la note officielle annonçant ce changement est disponible [via ce lien](https://dd.weather.gc.ca/doc/genots/2013/02/26/NOCN03_CWAO_262210___00308).

Une note technique à ce sujet est disponible [via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/lib/op_systems/doc_opchanges/technote_raqdps_20130226_f.pdf).

## Le mercredi 3 octobre 2012

### Le Centre Météorologique Canadien améliore son système régional de prévision déterministe de qualité de l'air (SRPDQA-version 1.5.0)

Le mercredi 3 octobre 2012, débutant avec l'integration de 1200 UTC, le Centre météorologique canadien (CMC) mettra en operation la version 1.5.0 du système régional de prévision déterministe de qualité de l'air (SRPDQA-150). Des changements dans l'espacement horizontal (de 15 à 10 km de résolution) et vertical des points de grille, une mise à jour de la version du modèle GEM, ainsi que des fichiers d'émissions améliorés, s'allient pour améliorer le système de prévision de la qualité de l'air.

En résumé, les changements principaux sont: SRPDQA-150 utilise la version GEM 3.3.8 dévelopée au CMC, le modèle a maintenent un espacement horizontal de 10 km entre les points de grille, le nombre de niveaux verticaux du augmente de 58 à 80 et le nouveau système incorpore un nouveau jeu de fichiers d'émissions anthropogéniques horaires.

Des informations additionnelles sur les changements et sur les évaluations objectives et subjectives sont disponibles dans les notes ci-dessous.

Les produits du SRPDQA-150 seront disponibles quelques minutes plus tard que les produits actuels étant donne le temps d'execution accru d'un système à plus haute résolution.

Une copie de la note officielle annoncant ce changement est disponible [via ce lien](https://dd.weather.gc.ca/doc/genots/2012/10/02/NOCN03_CWAO_022004___00099).

Une note technique à incluant des détails sur la version 1.5.0 et la version 1.5.1 est disponible [en cliquant ici](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/lib/op_systems/doc_opchanges/technote_raqdps_20121003_f.pdf).

Finalement, notez que cette mise à jour du SRPDQA est nécessaire à cause des changements majeurs qu'on apporte au système régional de prévision déterministe (SRPD) qui fournit les conditions initiales au SRPDQA. Des informations sur les changements au SRPD sont disponibles via ce lien [en cliquant ici](/../nwp_rdps/changelog_rdps_fr.md).

## Le jeudi 22 décembre 2011

### Le Centre Météorologique Canadien implante un correctif à GEM-MACH15

À partir de la passe 12 UTC du 22 décembre 2011, une mise à jour a été installée dans GEM-MACH15 afin de mieux traiter l'humidité et l'information des nuages dans les hauts niveaux de l'atmosphère perçus par ce modèle. Avec ce correctif la version de GEM-MACH15 est maintenant la version 1.4.5.