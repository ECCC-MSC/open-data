[In English](readme_wcps_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > SPCE

# Données et Produits du Système de prévision du cycle de l'eau (SPCE)

Le Système de prévision du cycle de l'eau (SPCE) simule le cycle complet de l’eau, suivant l’eau qui se déplace de l’atmosphère à la surface, par les réseaux fluviaux et vers les lacs, puis qui retourne dans l’atmosphère. Il fournit des analyses et des prévisions à court terme des flux atmosphère-océan-glace et des flux fluviaux. Le SPCE a été initialement mis en place pour le bassin versant des Grands Lacs Laurentiens et du fleuve Saint-Laurent à l’appui des obligations du Canada en vertu du Traité relatif aux eaux limitrophes (Commission Mixte Internationale, 2016). Depuis la version v3.0.0 du SPCE, le domaine est étendu pour couvrir également la région océanique du golfe du Saint-Laurent.

Le SPCE se compose de trois composantes : La composante Pseudo-analyse avec le modèle d'océan-glace NEMO-CICE, La composante de prévision avec la version à zone limitée du modèle atmosphérique GEM (GEM-LAM) couplé à NEMO-CICE et la composante de Rivières avec le modèle de routage de rivière WATROUTE. Ces composantes sont couplées les unes aux autres et représentent les processus dans l'atmosphère, à la surface de la terre et dans le sol (à une résolution de 10 km), dans les grandes masses d'eau et la glace marine (à une résolution de 1 km), et dans les rivières (à une résolution de 1 km).

Le Système global de prévision déterministe (SGPD) fournit les conditions initiales et latérales à une version du modèle numérique GEM-LAM couvrant l’est de l’Amérique du Nord, ce qui inclut la zone océanique entourant le golfe du Saint-Laurent. Toutes les 6 minutes, GEM-LAM communique à NEMO-CICE les précipitations qui se sont déposées à la surface des lacs et l'état de l'atmosphère proche de la surface au-dessus des Grands Lacs (lacs Supérieur, Michigan-Huron, Sainte-Claire, Érié et Ontario) et de la région du golfe du Saint-Laurent. NEMO informe le GEM-LAM de la température de l'eau de surface, de l'étendue de la couverture de glace et des flux de chaleur et de quantité de mouvement latents et sensibles. GEM-LAM fournit également des estimations horaires du ruissellement de surface à WATROUTE. À son tour, WATROUTE informe NEMO du ruissellement terrestre.

## Accès

### Comment accéder aux données

Ces données sont respectivement disponibles via l'API / les services web [GeoMet du SMC](../../msc-geomet/readme_fr.md) ainsi que sur le serveur de données [Datamart du SMC](../../msc-datamart/readme_fr.md)  :

* [Données disponibles via l'API / les services web géospatiaux GeoMet-Météo](../../msc-geomet/readme_fr.md)
* [Données des prévisions couplées atmosphère-océan-glace de mer du Système de prévision du cycle de l'eau (SPCE) en format NetCDF  disponibles sur le Datamart du SMC](readme_wcps-atm-ocean-datamart_fr.md)  

Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est disponible.

### Licence

La [licence d’utilisation finale pour les serveurs de données d’Environnement et Changement climatique Canada](../../licence/readme_fr.md) précise les conditions d'utilisation de ces données.

### Politique d'utilisation des services de données ouvertes du SMC

La [Politique d'utilisation des services de données ouvertes du SMC](../../usage-policy/readme_fr.md) détermine ce qui constitue une utilisation appropriée des services de données ouvertes du SMC et fournit aux utilisateurs les pratiques exemplaires pour une utilisation optimale.

### Métadonnées

Les [métadonnées du Système de prévision du cycle de l'eau - Océan-Atmosphère sont accessibles sur le portail du gouvernement ouvert](https://open.canada.ca/data/fr/dataset/36129cbc-3997-4b8e-a8bf-5fb44492134d).

## Documentation technique

* [Version actuelle du Système de prévision du cycle de l'eau (SPCE)](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_specifications/tech_specifications_WCPS_f.pdf)
* [Note technique](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_notes/technote_wcps_f.pdf)
* [Diagramme de dépendances](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwep-dependency-diagrams/system_WCPS_fr.svg)

## Registre des changements 

La [chronologie des changements apportés au Système de prévision du cycle de l'eau (SPCE)](changelog_wcps_fr.md) est disponible.

