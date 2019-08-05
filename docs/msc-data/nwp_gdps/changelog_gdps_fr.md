[In English](changelog_gdps_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [SGPD](readme_gdps_fr.md) > Changements au SGPD

# Chronologie des changements apportés au Système global de prévision déterministe (SGPD)

## Le mercredi 3 juillet 2019

### Mise à jour du Système global de prévision déterministe (SGPD) 7.0.0 du Centre météorologique canadien (CMC)

Le mercredi 3 juillet 2019, à compter de la passe de 1200 UTC, le Centre météorologique canadien (CMC) va procéder à la mise en œuvre opérationnelle de la version 7.0.0 de son Système global de prévision déterministe (SGPD).
Résumé des éléments majeurs que comporte cette mise à jour :

* Changements à la composante atmosphérique du modèle de prévision :
    * Le SGPD-7.0.0 utilise la version 5.0.0 du modèle GEM. Pour plus d'informations sur GEM-5, [veuillez consulter ce document (en anglais)](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/GEM5_paper_submitted_JAMES_20190614.pdf).
    * La résolution horizontale passe de 25 km à 15 km.
    * Le nombre de niveaux verticaux passe de 80 à 84.
    * Le schéma de surface ISBA est amélioré.
* Changements à la composante océanique du modèle de prévision :
    * Mise à jour du modèle océanique NEMO de la version 3.1 à 3.6.
* Changements à la composante d'assimilation de données :
    * Mise à jour vers le SGPOG version 3.0.0.
    * Mise à jour vers SAM2 (Système d'Assimilation Mercator).
    * La nouvelle analyse de température de surface de la mer et de glace marine a une plus haute résolution (0.10 degré).


Une copie de la note officielle annonçant ce changement [est disponible via ce lien](http://dd.meteo.gc.ca/doc/genots/2019/06/28/NOCN03_CWAO_281732___16257).

Une note technique à ce sujet [est disponible via ce lien (en anglais)](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_gdps-700_e.pdf). La version française sera disponible bientôt.

Le document des spécifications techniques du SGPD 7.0.0 [est disponible ici en anglais seulement](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_GDPS_f.pdf).

## Le mardi 18 septembre 2018

### Mise à jour du Système global de prévision déterministe (SGPD) 6.1.0 du Centre météorologique canadien (CMC)

Le mardi 18 septembre 2018, à compter de la passe de 1200 UTC, le Centre météorologique canadien (CMC) va procéder à la mise en œuvre opérationnelle de la version 6.1.0 de son Système global de prévision déterministe (SGPD).
Résumé des éléments majeurs que comporte cette mise à jour :

* Changements au modèle de prévision:
    * Dans cette mise à jour, aucun changement significatif n'a été fait dans la composante de prévision.
* Changements à la composante assimilation:
    * Amélioration du traitement de certaines observations(RAOBS, AMV, GB-GPS, Avions).
    * Ajout d'observations: augmentation de ~1.7%, principalement des données CSR de vapeur d'eau.
    * Le modèle de transfert radiatif RTTOV servant d'opérateur d'observation des radiances a été mis à jour de la version 10 à la version 12.1.
    * Augmentation de la résolution de l'incrément d'analyse dans le 4D-EnVar (de 50 à 37 km).

La note officielle annonçant ce changement [est disponible en cliquant ici](http://dd.meteo.gc.ca/doc/genots/2018/09/14/NOCN03_CWAO_142116___45455).

Une note technique à ce sujet [est disponible via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_gdps-610_20180918_f.pdf).

Le document des spécifications techniques du SGPD 6.1.0 [est disponible ici](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_GDPS_6.1.0_f.pdf).


## Le mercredi 1er novembre 2017

### Mise à jour majeure du Système global de prévision déterministe (SGPD) 6.0.0 du Centre météorologique canadien (CMC)

Le mercredi 1er novembre 2017, à compter de la passe de 1200 UTC, le Centre météorologique canadien (CMC) va procéder à la mise en œuvre opérationnelle de la version 6.0.0 de son Système global de prévision déterministe (SGPD).
Résumé des éléments majeurs que comporte cette mise à jour :

* Changements au modèle de prévision:
    * Couplage bi-directionnel avec un modèle océan-glace. Avec le nouveau SGPD 6.0.0, les conditions de surface marine évolue dans le temps du au couplace avec la composante prévision du Système global de prévision océan-glace (SGPOG). [Cliquez ici pour les détails de SGPOG](../nwp_giops/changelog_giops_fr.md).
    * Utilisation de la version 4.8.2 du modèle GEM. Les changements principaux sont associés avec l’interface à la surface, avec seulement des changements mineurs à la physique et la dynamique du modèle.
* Dans cette mise à jour, aucun changement n'a été fait au système d'assimilation, ni aux observations qui sont utilisés par le SGPD.

La note officielle annonçant ce changement [est disponible en cliquant ici](http://dd.meteo.gc.ca/doc/genots/2017/10/31/NOCN03_CWAO_311927___01741).

Une note technique à ce sujet [est disponible via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_gdps-600_20171101_f.pdf).

Le document des spécifications techniques du SGPD 6.0.0 (en anglais) [est disponible ici](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_GDPS_6.0.0_e.pdf).


## Le mardi 15 décembre 2015

### Mise à jour majeure du système global de prévision déterministe (SGPD) 5.0.0 du Centre météorologique canadien (CMC)

Le mardi 15 décembre 2015, à compter de la passe de 1200 UTC, le Centre météorologique canadien (CMC) va procéder à la mise en œuvre opérationnelle de la version 5.0.0 de son système global de prévision déterministe (SGPD).
Résumé des éléments majeurs que comporte cette mise à jour :

* Changements au modèle de prévision:
    * Une grille de type uniforme latitude-longitude est remplacée par une grille de type "Yin-Yang", composée de deux sous-grilles se chevauchant.
    * L'application de la méthode trapézoidale combiné à un schème d'interpolation cubique pour les calculs des trajectoires.
    * L'ajout d'un niveau de "momentum" au-dessus de 10 hPa à la coordonnée verticale pour améliorer l'efficience des calculs.
    * Un changement fait au taux d'applatissement de la coordonée verticale.
    * L'ajout des deux niveaux diagnostiques au 1.5 m et 10 m au-dessus de sol du modèle.
* Changements au système d'assimilation:
    * L'introduction de la même coordonée verticale qui est utilisé par le modèle.
* Changements aux observations:
    * Ajout des observations de radiance de 17 canaux de l'instrument satellitaire Advanced Microwave Sounding Unit (ATMS).
    * Ajout de 103 canaux de l'instrument satellitaire Cross-track Infrared Sounder (CrIS).
    * Ajout des observations de plus de 600 récepteurs GPS au sol - la plupart en Europe.
    * L'application des corrélations inter-canaux pour toutes les données de radiance infrarouge et micro-onde.

La note officielle annonçant ce changement [est disponible en cliquant ici](http://dd.meteo.gc.ca/doc/genots/2015/12/14/NOCN03_CWAO_142128___00043).

Une note technique à ce sujet [est disponible via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/lib/technote_gdps-500_20151215_f.pdf).

Le document des spécifications techniques du SGPD 5.0.0 [est disponible ici](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_GDPS_5.0.0_f.pdf).


## Le mardi 18 novembre 2014

### Mise à jour majeure du système global de prévision déterministe (SGPD version 4.0.0) du Centre météorologique canadien (CMC)

Le mardi 18 novembre 2014, à compter de la passe de 1200 UTC, le Centre météorologique canadien (CMC) va procéder à la mise en œuvre opérationnelle de la version 4.0.0 de son système global de prévision déterministe (SGPD).
Résumé des éléments majeurs que comporte cette mise à jour :

* La méthode d'assimilation 4D-EnVAR remplace le 4D-VAR.
    * Couplage avec le filtre de kalman d'ensemble (FKEn) pour recevoir les covariances d'erreur de prévisions.
* Changement aux observations
    * Amélioration au traitement des observations de radiosondes et d'avions.
    * Assimilation des observations de récepteurs GPS au sol.
    * Amélioration de la procédure de correction de biais des radiances satellitaires.
    * Canaux additionnels de données AIRS/IASI assimilées.
* Changements au modèle de prévision
    * Approche incrémentale 4D de mise à jour de l'analyse (IAU:Incremental Analysis Update).
    * Recyclage de plusieurs variables pronostiques.
* Nouvelle analyse de la concentration de la glace de mer.

Une copie de la note officielle annonçant ce changement [est disponible via ce lien](http://dd.meteo.gc.ca/doc/genots/2014/11/14/NOCN03_CWAO_141442___00930).

Une note technique à ce sujet [est disponible via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/lib/technote_gdps-400_20141118_f.pdf).


## Le mercredi, 13 février 2013

### Mise à jour majeure du système global de prévision déterministe (SGPD) version 3.0.0 du Centre météorologique canadien (CMC)

Le mercredi 13 février 2013, à compter de la passe de 1200 UTC, le Centre météorologique canadien (CMC) va procéder à la mise en œuvre opérationnelle de la version 3.0.0 de son système global de prévision déterministe (SGPD). Cette nouvelle version amène une augmentation de la résolution de 33 à 25 km, incorpore un système d'assimilation 4D-VAR. Ceci résulte en une amélioration notable des prévisions, notamment pour l'hiver.

Dans cette version une coordonnée vertical hybride décalée est utilisée. De l'information au sujet de cette coordonnée [est disponible dans cette courte note](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/lib/op_systems/doc_opchanges/HybridVerticalCoordinateDefinitions_20130213.pdf) ainsi que sur cette [image au lien suivant](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/lib/op_systems/doc_opchanges/VerticalCoordinatesDiagram_afsysed_20130213.jpg).

Notez aussi que lors de cette implantation le temps de coupure associé à la collecte d'observations a été réduit et est maintenant [00,12]Z+3:05

La vérification objective des champs en altitude et en surface contre des données de radiosondage montre une amélioration significative à toutes les écheances de prévision.

Une copie de la note officielle annonçant ce changement [est disponible via ce lien](http://dd.weatheroffice.ec.gc.ca/doc/genots/2013/02/07/NOCN03_CWAO_071820___00197).

Une note technique à ce sujet [est disponible via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/lib/op_systems/doc_opchanges/technote_gdps300_20130213_f.pdf).

