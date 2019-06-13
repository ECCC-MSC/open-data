[In English](readme_hrdpawatershed_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données ouvertes publiques du SMC](../readme_fr.md) > Données de précipitations moyennes par bassin-versant AHRDP

# Données et Produits de précipitations moyennes par bassin-versant de l'Analyse à haute résolution déterministe de précipitation (AHRDP)

L'Analyse canadienne des précipitations (CaPA) produit un estimé optimal des quantités de précipitations sur des périodes d'accumulation de 6 et 24 heures. Cette analyse objective intègre des données provenant d'appareils de mesure au sol, de QPE radar et d'un champ d’essai fourni par un système de prévision numérique du temps. Pour produire l'Analyse à haute résolution déterministe des précipitations (AHRDP) à une résolution de 2.5 km, CaPA est connecté au système à haute résolution de prévision déterministe (SHRPD) qui fournit le champ d'essai.

CaPA-AHRDP produit quatre analyses de 6 heures par jour, valides aux heures synoptiques (00, 06, 12 et 18 UTC) et une analyse de 24 heures valide à 12 UTC. Une production préliminaire est démarrée une heure après l'heure de validité et une production finale est démarrée six heures plus tard. Ceci se traduit en une production quotidienne de 10 analyses. Le domaine de l'analyse AHRDP est le même que celui du modèle SHRPD.

Le débit des rivières à un endroit précis évolue en fonction des précipitations qui se produisent en amont.

Afin de mieux interpréter les changements observés dans ces débits, il est utile de calculer les précipitations moyennes pour les bassins-versants définis par la position des stations de mesure du débit.

En collaboration avec toutes les provinces et territoires, le SMC opère un réseau étendu de stations de jaugeage mesurant le débit des rivières. Des données historiques et temps réel sont disponibles ici:
https://eau.ec.gc.ca/

De plus, Environnement et Changement climatique Canada a publié les Polygones des bassins du Réseau hydrométrique national, qui proposent des limites de bassins-versants à l'amont de stations hydrométriques actives et rapportant des observations de débit:
https://ouvert.canada.ca/data/fr/dataset/0c121878-ac23-46f5-95df-eb9960753375

En combinant ces polygones avec l’AHRDP, il est possible d'obtenir des précipitations moyennes par bassin-versant.

## Accès

### Comment accéder aux données

Ces données sont respectivement disponibles sur les services serveur de données [Datamart du SMC](../../msc-datamart/readme_fr.md) et les services web [GeoMet du SMC](../../msc-geomet/readme_fr.md) :

* [Données GRIB2 disponibles sur le Datamart du SMC](readme_hrdpawatershed-datamart_fr.md) 
* Lien vers la sous-page du jeu de données pour GeoMet [exemple](../../msc-geomet/giops_fr.md), si la sous-page existe. 
	* NOTE: n'existe pas pour le SGPD

Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage-overview/readme_fr.md) est disponible.

### Licence

La [Licence d’utilisation finale pour les serveurs de données d’Environnement et Changement climatique Canada](../../licence/readme_fr.md) précise les conditions d'utilisation de ces données.

### Métadonnées

_À venir._

## Documentation technique

* [Note technique](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/lib/technote_capa_hrdpa-450_f.pdf)
* [Feuillet d'information décrivant le système CaPA](http://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/lib/capa_feuillet_information_f.pdf)

## Registre des changements 

La chronologie des changements apportés aux systèmes opérationnels est disponible [ici](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/changes_f.html).
