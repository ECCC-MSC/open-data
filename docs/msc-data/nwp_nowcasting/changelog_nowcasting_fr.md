[In English](changelog_nowcasting_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [Prévision immédiate](readme_nowcasting_fr.md) > Changements au système SIPI

# Chronologie des changements apportés au Système intégré de prévision immédiate (SIPI)

## Le mardi 11 juin 2024

### Mise à jour du Système intégré de prévision immédiate (SIPI) 2.3.0 du Centre météorologique canadien (CMC)

Le mardi 11 juin 2024, à compter de la passe de 1200 UTC, le Centre météorologique canadien (CMC) va procéder à la mise en œuvre opérationnelle de la version 2.3.0 de son Système intégré de prévision immédiate (SIPI).

Principaux changements :

* Fraction nuageuse CF générée à partir des données GOES (Geostationary Operational Environmental Satellite) et du Système global de prévision déterministe (SGPD) en remplacement du Système régional de prévision déterministe (SRPD) 
* Utilisation des données radar en bande S post-traitées 
* Les données du modèle SGPD remplacent les données du modèle SRPD utilisées dans les versions précédentes du SIPI 
* Les données UMOS-SGPD remplacent les données UMOS-SRPD utilisées dans les versions précédentes du SIPI 

La note officielle annonçant ce changement [est disponible via ce lien](https://dd.meteo.gc.ca/doc/genots/2024/06/10/NOCN03_CWAO_101857___46443).

Un document avec des détails techniques à ce sujet [est disponible via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_rdps-incs-230_f.pdf).

Le document des spécifications techniques du SIPI 2.3.0 [est disponible ici](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_RDPS-INCS_2.3.0_f.pdf).

## Le lundi 19 février 2024

### Mise à jour du Système intégré de prévisions immédiates (SIPI) 2.2.0 du Centre météorologique canadien (CMC)

Le lundi 19 février 2024, à compter de la passe de 1200 UTC, le Centre météorologique canadien (CMC) du Service météorologique du Canada (SMC) a procédé à une mise à jour de la version 2.2.0 de son Système intégré de prévisions immédiates (SIPI).

Les modifications incluses dans cette mise à jour se résument comme suit :

* Correctif dans le SIPI opérationnel pour mieux gérer les cas rares de données radars manquantes.


## Le jeudi 23 mars 2023

### Mise à jour de SIPI à la version 2.1.0 pour introduire le traitement des données radars de bande-S du Canada

Le jeudi 23 mars 2023, à compter de la passe de 1200 UTC, le Centre météorologique canadien (CMC) du Service météorologique du Canada (SMC) a procédé à une mise à jour de la version 2.1.0 de son Système intégré de prévisions immédiates (SIPI).

Les modifications incluses dans cette mise à jour se résument comme suit :

* Introduction et traitement des données des nouveaux radars de bande-S
* Ajustement du code pour assurer une plus grande fiabilité d’accès aux données radars
* Modification de l’approche pour la production du fichier interne  comporad  qui dépend moins du module qperad de CaPA et qui peut plutôt maintenant être produit à partir de nouvelles données radars sur grille
* Depuis le 4 janvier 2023 le système utilise les informations des nuages calculées à partir des données satellitaires GOES 18 (GOES ouest). Les données des nuages calculées à partir des données du satellite GOES 16 (GOES est) demeurent toujours présentes

La note officielle annonçant ce changement est disponible via [ce lien](https://dd.meteo.gc.ca/doc/genots/2023/03/23/NOCN03_CWAO_231325___11843)

Une note technique à ce sujet est disponible via [ce lien](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_rdps-incs-210_f.pdf)

## Le mardi 28 juin 2022

### Mise à jour de SIPI à la version 1.10.0 suite à la nouvelle infrastructure de calcul haute performance. 

Voir les détails via [ce lien](../changelog_multisystems_fr.md).

## Le mercredi 1er décembre 2021

### Mise à jour du Système intégré de prévisions immédiates (SIPI) 1.9.0 du Centre météorologique canadien (CMC)

Le mercredi 1er décembre 2021, à compter de la passe de 1200 UTC, le Centre météorologique canadien (CMC) va procéder à la mise en œuvre opérationnelle de la version 1.9.0 de son Système intégré de prévisions immédiates (SIPI).

Les modifications incluses dans cette mise à jour sont résumées comme suit :

* Les mécanismes de SRPD SIPI utilisent les données du SRPD 8.0.0 ainsi que les données UMOS SRPD
* Les nuages modélisés sont améliorés  en utilisant les données de nuages de GOES 16/17
* Le système utilise maintenant la fraction de nuage totale (CF)

La note officielle annonçant ce changement est disponible [via ce lien](http://dd.meteo.gc.ca/doc/genots/2021/11/26/NOCN03_CWAO_262118___50159).

Une note technique à ce sujet est disponible [via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_rdps-incs-190_f.pdf).

Le document des spécifications techniques du SIPI v1.9.0 est disponible [via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_RDPS-INCS_1.9.0_f.pdf).

## Le mardi 21 janvier 2020

### Mise à jours de SIPI suite à la nouvelle infrastructure de calcul haute performance. 

Voir les détails via [ce lien](../changelog_multisystems_fr.md).

## Le jeudi 9 juillet 2015

### Le Centre Météorologique Canadien améliore son système SIPI à version 1.5

Le jeudi 09 juillet 2015 à partir de 1400 UTC, le Centre Météorologique Canadien (CMC) a procédé à une mise à jour son système intégré de prévisions immédiates (SIPI). Ce système fournit à la fois des données d'observations ainsi que des prévisions à très court terme au système de production des prévisions Scribe. Cette mise à jour, amèliore, entre autres, principalement la qualité de la composante qui traite les données radar de ce système.

Une copie de la note officielle annoncant ce changement [est disponible en cliquant ici](http://dd.weather.gc.ca/doc/genots/2015/07/08/NOCN03_CWAO_081635___00168).

Une note technique à ce sujet sera disponible sous peu.

## Le mercredi 20 novembre 2013

### Le Centre Météorologique Canadien améliore son système SIPI à version 1.4

Le mercredi 20 novembre 2013 à partir de 1400 UTC le Centre Météorologique Canadien (CMC) a procédé à une mise à jour son système intégré de prévisions immédiates (SIPI). Ce système fournit à la fois des données d'observations ainsi que des prévisions à très court terme au système de production des prévisions Scribe. Cette mise à jour, qui amène entre autres, l'intégration des observations radar dans le SIPI, fait passer la version du système de 1.1. à la version 1.4.

Les modifications suivantes ont été faites au système :

1) Intégration des observations radar sous la forme d'une composite nord-américaine provenant du système URP de résolution de 4 km et basée sur le produit PRECIP-ET

2) Nettoyage des données radar à l'aide d'un masque de nuage (satellite et champ NT du système régional de prévisions déterministes ou SRPD) et d'un traitement statistique

3) Extrapolation des données radar observées avec l'algorithme MAPLE (McGill Algorithm for Precipitation langrangian Extrapolation, REF. McGill University's Research center on Atmospheric Remote Sensing)

4) Remplacement de l'algorithme d'extrapolation de la foudre (Ouellet-Price) par le champ vectoriel de déplacement Maple

5) Utilisation du champ de probabilité de précipitations prévu par Maple à 4 km

6) Application d'une méthode d'échantillonnage pour produire un champ de probabilité de foudre à partir du champ de densité de coups de foudre observé et prévu.

7) Utilisation d'un champ de probabilité de précipitations généré à partir d'une méthode d'échantillonnage appliquée au champ des QPF horaire  du système régional de prévisions déterministes - SRPD.

Avec toutes ces modification, globalement, les résultats de vérification ont montré clairement une amélioration pour les 6 premières heures de projection.

Une copie de la note officielle annoncant ce changement [est disponible en cliquant ici](http://dd.weather.gc.ca/doc/genots/2013/11/15/NOCN03_CWAO_151902___00907).

Une note technique à ce sujet est disponible via le lien suivant : [Note Technique du SIPI 1.4](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/lib/technote_sipi_20140502_f.pdf)

## Le mardi 7 août 2012

### Le Centre Météorologique Canadien améliore son système SIPI à version 1.1

Le mardi 7 août 2012 à partir de 1400 UTC le Centre Météorologique Canadien (CMC) a mis à jour son système intégré de prévisions immédiates (SIPI). Ce système fournit à la fois des données d'observations ainsi que des prévisions à très court terme au système de production des prévisions Scribe. Avec cette mise à jour le numéro de version du système SIPI passe de 1.0. à 1.1.

Les modifications suivantes ont été faites au système:

1) Les prévisions de la température du point de rosée produites par le système statistique UMOS ont été intégrées au SIPI.

2) Le système de règles gouvernant la prévision de l'opacité nuageuse et de la visibilité a connu des améliorations.

Les règles qui génèrent la prévision du point de rosée utiliseront le point de rosée umos au lieu du point de rosée du système régional de prévision déterministe (SRPD), pour toutes les stations pour lesquelles le point de rosée umos est disponible. les résultats de vérification du point de rosée ont montre une performance supérieure de la version 1.1 par rapport à la version 1.0. avec ce changement nous anticipons notamment un impact positif sur la capacité à prévoir le brouillard.

Des modifications apportées aux règles de prévision de l'opacité nuageuse ont amélioré les performances du système pour cet élément du temps, particulièrement pour la période de 4 à 12 heures apres l'heure de début de la passe.

Enfin, des ajustements aux règles de prévision de la visibilité ont permis par exemple d'améliorer la visibilité prévue sous la neige.

Une copie de la note officielle annoncant ce changement [est disponible en cliquant ici](http://dd.weather.gc.ca/doc/genots/2012/07/31/NOCN03_CWAO_312128___01022).


