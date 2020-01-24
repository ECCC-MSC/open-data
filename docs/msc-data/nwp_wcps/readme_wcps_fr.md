[In English](readme_wcps_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > SPCE

# Données et Produits du Système de prévision du cycle de l'eau (SPCE)

Le Système de prévision du cycle de l'eau (SPCE) simule le cycle complet de l’eau, suivant l’eau qui se déplace de l’atmosphère à la surface, par les réseaux fluviaux et vers les lacs, puis qui retourne dans l’atmosphère. Le SPCE couplé au Golfe du Saint-Laurent a été mis en place pour le bassin versant des Grands Lacs Laurentiens et du fleuve Saint-Laurent à l’appui des obligations du Canada en vertu du Traité relatif aux eaux limitrophes (Commission
Mixte Internationale, 2016).

Le SPCE consiste en une chaîne de modèles inter-reliés. Les modèles représentent les processus dans l’atmosphère, à la surface du sol et dans le sol (à une résolution de 10 km), dans les vastes plans d’eau et la glace marine (à une résolution de 2 km) et dans les rivieres (à une résolution de 1 km). Le SPCE-GLS produit deux prévisions par jour pour les trois jours et demi suivants (84 heures). 

Le Système Régional de Prévision Déterministe (SRPD) fournit les conditions initiales et latérales à une version du modele numérique GEM-LAM couvrant l’est de l’Amérique du Nord. Toutes les 7 minutes, il communique avec le modèle océan-glace, NEMO-CICE, configuré sur les Grands Lacs, soit les lacs Supérieur, Michigan-Huron, Sainte Claire, Érié et Ontario. GEM-LAM informe NEMO des précipitations qui sont tombées à la surface des lacs et des conditions de l’atmosphère près de la surface. NEMO informe GEM-LAM de la température des eaux de surface, de la couverture de glace ainsi que des flux de chaleur sensible et latente et de quantité de mouvement. GEM-LAM fournit aussi des estimations horaires du ruissellement de surface au modèle de routage de rivière, WATROUTE. À son tour, WATROUTE informe NEMO à propos du ruissellement terrestre. 

## Accès

### Comment accéder aux données

Ces données sont respectivement disponibles sur les services du serveur de données [Datamart du SMC](../../msc-datamart/readme_fr.md) et les services web [GeoMet du SMC](../../msc-geomet/readme_fr.md) :

* [Données couplées de prévision WCPS-NEMO en format NetCDF, disponibles sur le Datamart du SMC](readme_wcps_nemo-datamart_fr.md) 
* [Données disponibles via les services web géospatiaux GeoMet-Météo](../../msc-geomet/readme_fr.md)

Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est disponible.

### Licence

La [licence d’utilisation finale pour les serveurs de données d’Environnement et Changement climatique Canada](../../licence/readme_fr.md) précise les conditions d'utilisation de ces données.

### Métadonnées

À venir.

## Documentation technique

* [Version actuelle du Système de prévision du cycle de l'eau (SPCE)](http://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_specifications/tech_specifications_WCPS_f.pdf)
* [Note technique](http://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_notes/technote_wcps_f.pdf)

## Registre des changements 

A venir
