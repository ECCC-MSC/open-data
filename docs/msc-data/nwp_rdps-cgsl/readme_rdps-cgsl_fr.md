[In English](readme_rdps-cgsl_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > SRPD couplé au Golfe du Saint-Laurent

# Données et produits du Système Régional de Prévision Déterministe couplé au Golfe du Saint-Laurent

## Description du système

Le Système régional de prévision déterministe - couplé au Golfe du Saint-Laurent (SRDP-CGSL) effectue des calculs physiques pour arriver à des analyses déterministes des glaces de mer et des éléments océaniques pour la journée en cours. Le système de prévision Océan-glace pour le golfe du Saint-Laurent est un modèle de circulation qui fournit une estimation des conditions actuelles sur le golfe. La glace de mer et les éléments océaniques comprennent la température de l'océan, la salinité, les courants, la hauteur de la surface de la mer, la concentration et l'épaisseur de la glace de mer, la dérive des glaces et autres. Ce produit contient les résultats numériques bruts de ces calculs. La couverture géographique est centrée sur le golfe du Saint-Laurent. Les données sont disponibles à une résolution horizontale de 5 km. Les données ne sont disponibles que pour le niveau de la surface. Les prévisions sont effectuées jusqu'à quatre fois par jour.

### Spécifications techniques de la grille native (domaine de calcul)

La composante atmosphérique comprend le Système régional de prévision déterministe opérationnel (SRPD) configuré pour rouler sur une grille à aire limitée (LAM) qui est centrée sur le golfe du Saint-Laurent (GSL). Cette grille contient 360 par 400 points de grille dans l’horizontal avec un espacement de 10 km (0,09 degré) avec une projection latitude-longitude rectangulaire. Les conditions nécessaires aux frontières sont fournies aux heures par les prévisions du modèle régional opérationnel SRPD à la même résolution (0,09 degré).

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
* [Données disponibles via les services web géospatiaux GeoMet-Météo](../../msc-geomet/readme_fr.md)

Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est disponible.

### Licence

La [licence d’utilisation finale pour les serveurs de données d’Environnement et Changement climatique Canada](../../licence/readme_fr.md) précise les conditions d'utilisation de ces données.

### Politique d'utilisation des services de données ouvertes du SMC

La [Politique d'utilisation des services de données ouvertes du SMC](../../usage-policy/readme_fr.md) détermine ce qui constitue une utilisation appropriée des services de données ouvertes du SMC et fournit aux utilisateurs les pratiques exemplaires pour une utilisation optimale.

### Métadonnées

À venir.

## Documentation technique

* [Note technique](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/lib/technote_rdps-cgsl_f.pdf)

## Registre des changements 

La chronologie des changements apportés au Système Régional de Prévision Déterministe couplé au Golfe du Saint-Laurent (SRPD-CGSL) est disponible [ici](changelog_rdps-cgsl_fr.md).
