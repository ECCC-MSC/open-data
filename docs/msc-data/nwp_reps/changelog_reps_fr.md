[In English](changelog_reps_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [SRPE](readme_reps_fr.md) > Changements au SRPE

# Chronologie des changements apportés au Système régional de prévision d'ensemble (SRPE)

## Le mercredi 1er décembre 2021

### Mise à jour du Système régional de prévision d'ensemble (SRPE) 4.0.0 du Centre météorologique canadien (CMC)

Le mercredi 1er décembre 2021, à compter de la passe de 1200 UTC, le Centre météorologique canadien (CMC) va procéder à la mise en œuvre opérationnelle de la version 4.0.0 de son Système régional de prévision d'ensemble (SRPE).

Un résumé des innovations incluses dans cette mise à jour ainsi que de leurs impacts sur la performance du système est disponible ici: [SRPE_4.0.0_innovations](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/fact_sheets/factsheet_reps-400_e.pdf). Pour une description complète veuillez consulter la [Note technique](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_reps-400_f.pdf).


Notes :

* [Note officielle](http://dd.meteo.gc.ca/doc/genots/2021/11/26/NOCN03_CWAO_262118___50159).
* [Note technique](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_reps-400_f.pdf).
* [Spécifications techniques du SRPE 4.0.0](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_REPS_4.0.0_f.pdf).


## Le mardi 21 janvier 2020

### Mise à jour du SRPE à la version 3.1.0 suite à la nouvelle infrastructure de calcul haute performance. 

Voir les détails via [ce lien](../changelog_multisystems_fr.md).

## Le mercredi 3 juillet 2019

### Mise à jour du Système régional de prévision d'ensemble (SRPE) 3.0.0 du Centre météorologique canadien (CMC)

Le mercredi 3 juillet 2019, à compter de la passe de 1200 UTC, le Centre météorologique canadien (CMC) va procéder à la mise en œuvre opérationnelle de la version 3.0.0 de son Système régional de prévision d'ensemble (SRPE).
Résumé des éléments majeurs que comporte cette mise à jour:

* Le [SGPE v6.0.0](../nwp_geps/changelog_geps_fr.md) remplace le SGPE v5.0.0 comme modèle pilote.
* Mise à jour de GEM de la version v4.8-LTS.16 à la version GEM v5.0.0. Pour plus d'informations sur GEM-5, veuillez consulter [ce document (en anglais)](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/GEM5_paper_submitted_JAMES_20190614.pdf).
* Résolution horizontale du système augmenté, passant de 15 à 10 km.
* Résolution verticale du système augmenté, passant de 48 to 84.
* Toit du modèle plus haut, passant de 16 hPa à 0.1 hPa.
* Fréquence des passes améliorée, passant de 2 passes par jour (00 et 12 UTC) à 4 passes par jour (00, 06, 12, et 18 UTC).
* Recentrage des membres de l'ensemble autour de l'analyse du SRPD.
* Chacun des membres est maintenant configuré comme le [SRPD v7.0.0](../nwp_rdps/changelog_rdps_fr.md).

Une copie de la note officielle annonçant ce changement [est disponible via ce lien](http://dd.meteo.gc.ca/doc/genots/2019/06/28/NOCN03_CWAO_281735___13093).

Une note technique à ce sujet [est disponible via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_reps-300_20190703_f.pdf).

Le document des spécifications techniques du SRPE 3.0.0 [est disponible ici](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_REPS_3.0.0_f.pdf).


## Le mardi 18 septembre 2018

### Mise à jour du système régional de prévision d'ensemble (SRPE) 2.4.0 du Centre météorologique canadien (CMC)

Le mardi 18 septembre 2018, à compter de la passe de 1200 UTC, le Centre météorologique canadien (CMC) va procéder à la mise en œuvre opérationnelle de la version 2.4.0 de son Système régional de prévision d'ensemble (SRPE).
Résumé des éléments majeurs que comporte cette mise à jour:

* Le système est maintennat piloté par le SGPE 5.0.0 (voir [ici](../nwp_geps/changelog_geps_fr.md) pour plus de détails).
* Mise à jour de la version du modèle (GEM) de v4.6 à v4.8.
* L'application de la méthode trapézoidale combiné à un schème d'interpolation cubique pour les calculs des trajectoires dans le semi-lagrangien.

Une copie de la note officielle annonçant ce changement [est disponible via ce lien](http://dd.meteo.gc.ca/doc/genots/2018/09/17/NOCN03_CWAO_171325___27325).

Une note technique à ce sujet [est disponible via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_reps-240_f.pdf).


## Le mardi 15 décembre 2015

### Mise à jour du système régional de prévision d'ensemble (SRPE version 2.2.0) du Centre météorologique canadien (CMC)

Le mardi 15 décembre 2015, à compter de la passe de 1200 UTC, le Centre météorologique canadien (CMC) va procéder à la mise en œuvre opérationnelle de la version 2.2.0 de son système régional de prévision d'ensemble (SRPE).

La seule modification au SRPE est que maintenant il est piloté par le SGPE 4.1.1 (voir [ici](../nwp_geps/changelog_geps_fr.md) pour plus de détails), plutôt que par la version précedente du SGPE 4.0.0.

Le document des spécifications techniques du SRPE 2.2.0 [est disponible ici](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_REPS_2.2.0_f.pdf).


## Le mercredi, 4 décembre 2013

### Mise à jour majeure du système régional de prévision d'ensemble (SRPE version 2.0.1) du Centre météorologique canadien (CMC)

Le mercredi 4 décembre 2013, à compter de la passe de 1200 UTC, le Centre météorologique canadien (CMC) va procéder à la mise en œuvre opérationnelle de la version 2.0.1 de son système régional de prévision d'ensemble (SRPE).

D'important changements ont été apportés à la dynamique du modèle utilisé dans le REPS 2.0.1.
La version du modèle GEM passe de 4.2.1 à 4.5.1. La résolution horizontale a été accrue passant de 0.3 degré (environ 33 km) à 0.1375 degré (environ 15 km). Le nombre de niveaux verticaux a été augmenté et passe de 28 à 48. Le pas de temps a été réduit de 15 à 7.5 minutes.

La configuration de la physique à aussi été modifiée:
le nouveau SRPE utilise la même suite physique que le système global de prévisions déterministes (SGPD), dont la résolution horizontale est de 25km.
Le changement le plus important que cela apporte par rapport au système précédent est l'introduction d'un effet d'hystérésis dans le shéma de mélange turbulant qui améliore surtout la prévision du type de précipitation. (Voir la note technique pour plus de détails)

Le nouveau SRPE continue d'avoir 20 membres perturbés de manière stochastique, ainsi qu'un membre de contrôle non perturbé. Les perturbations stochastiques des tendances de la physique (PTP) sont toujours appliquées à chaque pas de temps dans le nouveau SRPE. Toutefois, les PTP ne sont plus appliquées aux endroits pour lesquels de la convection est présente, ou lorsque la vitesse verticale est supérieure à 0,5 m/s. Ces modifications ont permis d'éliminer la présence de précipitations trop intenses et irréalistes qui se trouvaient occasionellement dans les prévision du SRPE précédent.

Le temps de décorrelation des perturbations stochastiques a été réduit de 24 à 6 heures.

La note officielle annonçant ce changement [est disponible en cliquant ici](http://dd.meteo.gc.ca/doc/genots/2013/12/03/NOCN03_CWAO_032208___00939).

Une note technique à ce sujet [est disponible via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/lib/technote_reps201_20131204_f.pdf).

## Le jeudi 22 septembre, 2011

Mise en Opération du Système Régional de Prévision d'Ensemble (SRPE 1.0.0) au Centre Météorologique Canadien

Le jeudi 22 septembre 2011 (cycle de 12 UTC) le Centre Météorologique Canadien a procédé à la mise en opération de son Système Régional de Prévision d'Ensemble (SRPE 1.0.0).

Pour l'instant les produits du SRPE ne sont disponibles que sur les réseaux á l'interne d'Environnement Canada mais des plans sont en cours pour rendre ces produits disponibles aux usagers externes.

Une copie de la note officielle est [disponible en cliquant ici](http://dd.weather.gc.ca/doc/genots/2011/09/26/NOCN03_CWAO_261345_CCA__98441).

Pour plus de détails [vous pouvez accéder à une note technique disponible au lien suivant](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/lib/op_systems/doc_opchanges/technote_srpe_20111004_f.pdf).






