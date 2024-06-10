[In English](changelog_cansips_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [SPISCAN](readme_cansips_fr.md) > Changements au SPISCan

# Chronologie des changements apportés au Système de prévision interannuelle et saisonnière canadien (SPISCan)

## Le mardi 30 novembre 2021

### Mise à jour vers la version 2.1 du Système de prévision interannuelle et saisonnière canadien (SPISCan) du Centre météorologique canadien (CMC)

En date du mardi 30 novembre 2021, le Centre météorologique canadien (CMC) va procéder à la mise à jour du Système de prévision interannuelle et saisonnière canadien (SPISCan) vers la version 3.0.0

Principaux changements :
* Le modèle climatique couplé CanCM4i remplacé par le modèle  CanESM5.1 Earth system model
* Le modèle couplé GEM-NEMO 5.1 est remplacé par GEM-NEMO 5.2
* La taille de l'ensemble de la prévision est doublé (de 20 à 40 membres) en utilisant une combinaison des prévisions usuelles et des prévision initialisées quatre jours avant.
* Dans CanESM5, Une nouvelle correction de biais à été introduite.
* L'initialisation de conditions de surface de GEM-NEMO provient maintenant du [système global de prévision déterministe (SGPD)](./nwp_gdps/readme_gdps_fr.md) après un ajustement vers la climatologie du modèle. Dans la version précédente, l'initialisation provenait des processus hors-ligne. 



Un résumé des innovations incluses dans cette mise à jour ainsi que de leurs impacts sur la performance du système est [disponible ici](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/fact_sheets/factsheet_cansips-300_f.pdf).

La note officielle annonçant ce changement est disponible [via ce lien](http://dd.meteo.gc.ca/doc/genots/2024/06/11/NOCN03_CWAO_262118___xxxxx).

Une note technique à ce sujet est disponible [via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/cansips-300_f.pdf).

Le document des spécifications techniques du SPISCan 3.0.0 est disponible [via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_CanSIPS_3.0.0_f.pdf).




## Le mardi 28 juin 2022

### Mise à jour de SPISCan à la version 2.2.0 suite à la nouvelle infrastructure de calcul haute performance. 

Voir les détails via [ce lien](../changelog_multisystems_fr.md).

## Le mardi 30 novembre 2021

### Mise à jour vers la version 2.1 du Système de prévision interannuelle et saisonnière canadien (SPISCan) du Centre météorologique canadien (CMC)

En date du mardi 30 novembre 2021, le Centre météorologique canadien (CMC) va procéder à la mise à jour du Système de prévision interannuelle et saisonnière canadien (SPISCan) vers la version 2.1.

Les modifications majeures du SPISCan dans cette mise à jour sont: 

* Mise à jour du modèle GEM-NEMO vers la version 5.1.
* Les modèles intrants de SPISCan ont été mis à jour: SGPD 8.0.0, SGPE 7.0.0 et SGPOG 3.3.0.

Une note technique avec plus de détails sur ces changements [est disponible sur cette page](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_cansips-210_f.pdf).

Le document des spécifications techniques du SPISCan version 2.1 [est disponible sur cette page](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_CANSIPS_2.1.0_f.pdf).

## Le mardi 21 janvier 2020

### Mise à jour de SPISCan suite à la nouvelle infrastructure de calcul haute performance. 

Voir les détails via [ce lien](../changelog_multisystems_fr.md).

## Le mercredi 3 juillet 2019

### Mise à jour vers la version 2 du Système de prévision interannuelle et saisonnière canadien (SPISCan) du Centre météorologique canadien (CMC)

En date du mercredi 3 juillet 2019, le Centre météorologique canadien (CMC) va procéder à la mise à jour du Système de prévision interannuelle et saisonnière canadien (SPISCan) vers la version 2.

Les modifications majeures du SPISCan dans cette mise à jour sont dans la composante prévision

* Remplacement du modèle CANCM3 par le nouveau modèle couplé GEM-NEMO.
* Mise à jour du modèle CANCM4 par une version améliorée CANCM4I.

Une note technique avec plus de détails sur ces changements [est disponible sur cette page en anglais seulement](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_cansips-v2_20190703_e.pdf).


## Le mardi 21 juin 2016

### Mise à jour du Système de prévision interannuelle et saisonnière canadien (SPISCan) du Centre météorologique canadien (CMC)

Le mardi 21 juin 2016, le Centre météorologique canadien (CMC) va procéder à une mise à jour de son Système de prévision interannuelle et saisonnière canadien (SPISCan).

Dans cette mise à jour les analyses océaniques 3D utilisées par le modèle océanique de SPISCan proviendront du Système global de prévision océan-glace (SGPOG) 2.1. Les analyses de SGPOG remplacent les analyses GODAS provenant du centre NCEP qui étaient utilisées auparavant.

La note officielle annonçant ce changement est disponible [en cliquant ici](http://dd.meteo.gc.ca/doc/genots/2016/06/21/NOCN03_CWAO_211910___00716). 


## Le mardi 23 juillet 2013

### Ajustement à l'analyse de température de la mer (GODAS) utilisée par SPISCan

Le mardi 23 juillet 2013 le CMC a apporté un ajustement à l'analyse GODAS de la temperature de la mer utilisée par SPISCan. Cela a été rendu nécessaire car le 16 juillet 2013, les données GODAS arrivant à SPISCan avaient été interrompues. Un certain nombre de mesures ont été prises pour rétablir ce flux de donnees GODAS. En conséquence, l'accès à l'analyse de GODAS quotidien a été corrigé et rétabli le 23 Juillet 2013, avec la mise en place des analyses corrigées du 17-21 Juillet 2013. Il était prévu qu'à partir du 23 Juillet 2013, que la séquence normale pour l'importation et l'assimilation des données GODAS sera de retour à la normal à partir du 24 Juillet 2013.


## Le jeudi 1er décembre 2011

### Le CMC introduit le système SPSICan de prévision mensuelle et saisonnière

Le 1er décembre 2011, le Centre Météorologique Canadien a commencé à émettre des produits avec son nouveau système couplé de prévision multi-saison globale pour produire ses prévisions mensuelles et saisonnières de conditions climatiques.

Ce nouveau système s'appelle SPISCan (Système de Prévision Interannuelle et Saisonnière Canadien).

Avec SPISCan, Environnement Canada sera en mesure d'émettre des prévisions saisonnières couvrant une année complète grâce a un système de prévision dynamique unique; ceci représente un progrès notable par rapport aux systèmes antérieurs. spiscan peut prévoir correctement le phénomène ENSO (El Niño-La Niña / Oscillation Australe) et son influence sur le climat jusqu'a un an en avance.

Le développement et l'implantation de ce système de prévision multi-saisons est le fruit de la collaboration étroite entre le CMC et le CCmaC (Centre canadien de la modélisation et d'analyse climatique)

Des détails complets décrivant le fonctionnement de ce systeme, comment il a été évalué sont disponibles aux liens dessous.

Même si aucun nouveau produit ne sera disponible sur le site des prévisions mensuelles et saisonnières du SMC la qualité des produits existants sera améliorée avec ce nouveau système. De nouveaux produits seront ultérieurement affiches dans une prochaine phase du projet.

Les produits provenant des prévisions multi-saisons seront disponibles le premier jour de chaque mois au site web du SMC.

Une copie de la note officielle annonçant l'utilisation opérationnelle de SPISCan [est disponible en cliquant ici](http://dd.weatheroffice.ec.gc.ca/doc/genots/2011/11/28/NOCN03_CWAO_281935___35518).

Une note technique sur SPISCan [est disponible en cliquant ici](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/lib/op_systems/doc_opchanges/technote_spiscan_20111220_f.pdf).

De l'information sur SPISCan et ses produits est aussi [disponible sur la page web publique de prévisions mensuelles et saisonnières du SMC en cliquant ici](https://meteo.gc.ca/saisons/index_f.html).

De l'information est aussi disponible dans le guide de produits du CMC aux liens suivant: [page sur les prévisions mensuelles](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/product-pages/image_ens_prog_monthly-temperature-anomalies_gen_f.html) et aussi à la [page sur les prévisions saisonnières](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/product-pages/image_ens_prog_seasonal-forecasts_gen_f.html).


