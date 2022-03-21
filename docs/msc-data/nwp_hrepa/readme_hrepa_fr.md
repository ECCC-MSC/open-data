[In English](readme_hrepa_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > AHREP

# Données et Produits Système d’analyse à haute résolution ensembliste de précipitation (CaPA-AHREP)

Le Système canadien d'analyse de précipitation (CaPA) produit une estimation optimale de la précipitation sur des périodes de cumuls de 6 et 24 heures. Cet estimé objectif intègre des relevés pluviométriques provenant de capteurs de précipitation, de QPE radars et d'un champ d'essai généré par un système de prévision numérique du temps. Actuellement, il existe deux configurations détermistes de l'analyse qui produisent quatre analyses de cumuls 6 heures valides aux heures synoptiques (00, 06, 12 et 18 UTC) et deux analyses 24 heures valide à 06 et 12 UTC. Les deux configurations diffèrent par leur domaine et résolution spatiale, l'Analyse régionale déterministe de précipitation (ARDP) est branchée sur le Système régional de prévision déterministe (SRPD) pour en tirer son champ d'essai avec une résolution de 10km alors que l'Analyse à haute résolution déterministe de précipitation (AHRDP) est branchée sur le Système à haute résolution de prévision déterministe (SHRPD) national pour le sien avec une résolution de 2.5km.

CaPA-AHREP est la version ensembliste de CaPA-AHRDP et fournit un ensemble de 25 membres d'analyse de cumuls 6 heures. Le premier membre de CaPA-AHREP, appelé membre contrôle, est équivalent à une analyse déterministe (i.e. sans perturbations des données) et utilise la même approche d'assimilation que CaPA-AHRDP. Les 24 autres membres suivent également la même approche d'assimilation de données mais utilisent des données d'entrée perturbées aléatoirement à chaque heure de validité de l'analyse. Ainsi, chaque observation aux stations est perturbée aléatoirement en y ajoutant une erreur distribuée normalement de moyenne nulle et de variance, estimée durant le processus d'assimilation, égale à la variance des erreurs d'observation. De même, les QPE radar sont perturbées en ajoutant une erreur (constante sur toute la couverture spatiale d'un radar donnée) échantillonnée à partir d'une loi normale de moyenne nulle et de variance, estimée durant le processus d'assimilation, égale à la variance des erreurs des QPEs radars. Enfin, les champs d'essai perturbés sont fournis par le système CaLDAS-National (*Canadian Land Data Assimilation System*) et suivent une pertubation aléatoire dans l'espace sans modification aux cumuls de ces derniers.


## Accès

### Comment accéder aux données

Ces données sont respectivement disponibles sur les services du serveur de données [Datamart du SMC](../../msc-datamart/readme_fr.md) et les services web [GeoMet du SMC](../../msc-geomet/readme_fr.md) :

* [Données NetCDF expérimentales disponibles sur DD-Alpha, le site web d'essai du Datamart du SMC](readme_hrepa-datamart_fr.md) 

Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est disponible.

### Licence

La [licence d’utilisation finale pour les serveurs de données d’Environnement et Changement climatique Canada](../../licence/readme_fr.md) précise les conditions d'utilisation de ces données.

### Politique d'utilisation des services de données ouvertes du SMC

La [Politique d'utilisation des services de données ouvertes du SMC](../../usage-policy/readme_fr.md) détermine ce qui constitue une utilisation appropriée des services de données ouvertes du SMC et fournit aux utilisateurs les pratiques exemplaires pour une utilisation optimale.

### Métadonnées
 
À venir.

## Documentation technique

* [Version actuelle du Système d’analyse à haute résolution ensembliste de précipitation](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_specifications/tech_specifications_HREPA_f.pdf)
* [Note technique](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_notes/technote_capa_hrepa_f.pdf)

## Registre des changements 

La chronologie des changements apportés à la version ensembliste à haute résolution du Système Canadien d'Analyse de Précipitation (CaPA-AHREP) est disponible [ici](changelog_hrepa_fr.md).
