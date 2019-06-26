[In English](readme_rdps-cgsl_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données ouvertes publiques du SMC](../readme_fr.md) > SRPD couplé au Golfe du Saint-Laurent

# Données et produits du Système Régional de Prévision Déterministe couplé au Golfe du Saint-Laurent

## Description du système

Le système régional de prévision déterministe couplé au Golfe du Saint-Laurent est un modèle de circulation dont l’objectif est de mieux comprendre les régions marines côtières canadiennes. Ce système comprend deux composantes :

* Le cycle de pseudo-analyse océanique, incluant une analyse de glace basée sur l’insertion directe d’analyses d’images Radarsat (Smith et al., 2012),
* Le cycle de prévision atmosphérique couplé.

Notons que le cycle de prévision du modèle couplé est une simulation de 48 heures basée sur les données de 00, 06, 12 et 18 UTC où les deux modèles de ce système (soit le LAM et le modèle Océan-Glace) tournent en même temps. Le système prévoit des conditions atmosphériques, l’état de la glace de mer et des prévisions océaniques pour une période de prévision de 0 à 48 heures.

### Spécifications techniques de la grille native (domaine de calcul)

La composante atmosphérique comprend le système régional de prévision déterministe opérationnel (SRPD) configuré pour rouler sur une grille à aire limitée (LAM) qui est centrée sur le golfe du Saint-Laurent (GSL). Cette grille contient 360 par 400 points de grille dans l’horizontal avec un espacement de 10 km (0,09 degré) avec une projection latitude-longitude rectangulaire. Les conditions nécessaires aux frontières sont fournies aux heures par les prévisions du modèle régional opérationnel SRPD à la même résolution (0,09 degré).

Pour la composante océanique, le système utilise le modèle glace-océan NEMO 
(Nucleus fro European Modeling of the Ocean) qui inclut un modèle de circulation 
océanique 3D en tenant compte des marées et des apports d’eau douce des rivières aux frontières. 
Le modèle CICE (Community Ice CodE) est utilisé pour la composante des glaces de mer. Le domaine de 
calcul de NEMO-CICE consiste en une grille de 149 par 236 points dans l’horizontale, s’étendant du 
détroit de Cabot à la ville de Québec et au fjord du Saguenay près de Tadoussac. Un modèle 
hydrologique à une dimension est utilisé pour le tronçon de Montréal à Québec pour absorber les 
marées à Québec. La résolution horizontale est de 5 km sur une projection Mercator tournée. Le 
domaine océanique est discrétisé en couches verticales avec résolution uniforme de 5 m jusqu’à 
300 m puis de 10 m en deçà de 300 m de profondeur. Les couches de surface et de fond sont ajustées 
au niveau de l’eau et à la profondeur du milieu respectivement. Les conditions aux frontières pour 
l’apport des rivières, pour la température et la salinité de l’eau sont prises de données 
climatologiques et les marées sont prescrites comme dans Saucier et al. (2003). 
 
## Accès

### Comment accéder aux données

Ces données sont respectivement disponibles sur les services serveur de données [Datamart du SMC](../../msc-datamart/readme_fr.md) et les services web [GeoMet du SMC](../../msc-geomet/readme_fr.md) :

* [Données GRIB2 disponibles sur le Datamart du SMC](readme_rdps-cgsl-datamart_fr.md) 
* Lien vers la sous-page du jeu de données pour GeoMet [exemple](../../msc-geomet/giops_fr.md), si la sous-page existe. 
	* NOTE: n'existe pas pour le SGPD

Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage-overview/readme_fr.md) est disponible.

### Licence

La [Licence d’utilisation finale pour les serveurs de données d’Environnement et Changement climatique Canada](../../licence/readme_fr.md) précise les conditions d'utilisation de ces données.

### Métadonnées

_À venir._

## Documentation technique

* [Note technique](http://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/lib/technote_rdps-cgsl-300_20141118_f.pdf)

## Registre des changements 

La chronologie des changements apportés aux systèmes opérationnels est disponible [ici](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/changes_f.html).
