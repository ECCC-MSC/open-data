[In English](readme_lightning_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > Lightning

# Données de densité de foudre

Le [Réseau Canadien de Détection de la Foudre](https://www.canada.ca/fr/environnement-changement-climatique/services/foudre/reseau-canadien-detection.html) assure la surveillance de la foudre presque partout au Canada. Les données distribuées ici représentent une agrégation spatio-temporelle des observations de ce réseau ayant une précision de quelques centaines de mètres. Plus précisément, toutes les 10 minutes, les observations rapportées sont traitées de la façon suivante:

* L'emplacement des éclairs observés (nuage-sol et intra-nuageux) dans les 10 dernières minutes est extrait.
* A l'aide d'une grille horizontale régulière d'environ 2.5km par 2.5km, le nombre d'éclairs observés à l'intérieur de chacune des cellules de cette grille est calculé.
* Ces données sur grille sont normalisées par la surface exacte de chacune des cellules (en km2) et par la période d'accumulation (10min) pour obtenir une densité d'éclairs observés exprimée en km-2 et min-1
* Un masque est appliqué afin de retirer les données situées à plus de 250km des frontières terrestres ou maritimes canadiennes.

## Accès

### Comment accéder aux données

Ces données sont respectivement disponibles sur les services du serveur de données [Datamart du SMC](../../msc-datamart/readme_fr.md) et les services web [GeoMet du SMC](../../msc-geomet/readme_fr.md) :

* [Données GeoTIFF disponibles sur HPFX, le serveur alternatif Datamart du SMC](readme_lightning-datamart_fr.md) 

Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est disponible.

### Licence

La [licence d’utilisation finale pour les serveurs de données d’Environnement et Changement climatique Canada](../../licence/readme_fr.md) précise les conditions d'utilisation de ces données.

### Politique d'utilisation des services de données ouvertes du SMC

La [Politique d'utilisation des services de données ouvertes du SMC](../../usage-policy/readme_fr.md) détermine ce qui constitue une utilisation appropriée des services de données ouvertes du SMC et fournit aux utilisateurs les pratiques exemplaires pour une utilisation optimale.

### Métadonnées

À venir.

## Documentation technique

[La foudre: carte du risque de foudre, sécurité, statistiques, science, foire aux questions](https://www.canada.ca/fr/environnement-changement-climatique/services/foudre.html)