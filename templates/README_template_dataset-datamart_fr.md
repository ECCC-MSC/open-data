# Gabarit pour les pages d'un jeu de données sur le Datamart du SMC

Ce gabarit est utilisé pour les pages des jeux de données sous `/msc-data/`. Ajouter le lien vers la version anglaise, le logo et le fil d'Ariane


## Données *indiquer le format* du *nom du jeu de données -tout au long pour les NWP-* (*acronyme si pertinent*)

Une ligne de présentation qui fait référence à la page principale.

> Exemple pour le SPDHRS:

> Cette page décrit les données expérimentales du [Système de prévision déterministe à haute résolution de la surface](https://eccc-msc.github.io/open-data/msc-data/nwp_hrdlps/readme_hrdlps_fr/) disponibles en format NetCDF sur le serveur DD-Alpha, le site Web d'essai de données du Datamart du SMC.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le Protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage-overview/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier *indiquer le format des données*.

Les données sont disponibles à l'adresse : https://dd.meteo.gc.ca.../HH/hhh/  (pour les données de modèle)

* où :

    * HH : Heure UTC du début de la passe du modèle [00,]
    * hhh : Heure de prévision [000, ]

Un historique de _XX_ jours est disponible dans ce répertoire _(note: cette phrase peut-être caduque pour les données uniquement dsponibles sur HPFX Collab puisque le temps de rétention varie en fonction de l'espace disponible)_

## Spécification technique de la grille - *(pour les NWP seulement)*

Si pertinent, donner les descriptions de la grille sous forme de tableau et au besoin une image du domaine. Les images devont être rassemblées sur [Collaboration](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc) et seulement référées ici via ![](adresse)

Exemple: https://eccc-msc.github.io/open-data/msc-data/nwp_wcps/readme_wcps-atm-ocean-datamart_fr/#specification-technique-de-la-grille

## Nomenclature des noms de fichiers 

Les fichiers suivent la nomenclature suivante : 

`YYYYYYYYYYYYYYYYYYYYYYYYYYY`

où :

* ...
* ...

Exemple : https://eccc-msc.github.io/open-data/msc-data/nwp_wcps/readme_wcps-atm-ocean-datamart_fr/#nomenclature-des-noms-de-fichiers

## Niveaux  - *vérifier si pertinent*

Décrire la liste des niveaux disponibles, si pertinent (ne s’applique qu’aux jeux de données 3D)*

## Contenu des fichiers - *vérifier si pertinent*
 
* A confirmer si pertinent ou si l’info peut se retrouver egrainée ailleurs*

* Décrire le contenu du fichier avec le plus de détails possible (ex: dans le cas des fichiers XML, décrire les en-têtes, les sections et les éléments).*

* Lorsque s'applique, indiquer si les fichiers ont été compressés et avec quel utilitaire (ex: bzip2). Indiquer comment les décompresser.*

* Lorsque s'applique, indiquer si les fichiers ont été encodés ou non, dans quel format et dans quel standard d'encodage (ex: UTF-8).*

* Au besoin, indiquer la précision des données.*

* Inclure un lien vers la documentation du format si pertinent (ex: format GRIB).*

## Liste des variables

Les variables disponibles de XXXXXX sont :

* VAR_1 : Définition
* VAR_2 : Définition
* ...
* ...

NOTE: Un tableau produit via un script automatisé sera inséré ici, coordonner avec dps.client@ec.gc.ca

## Support

Pour toute question relative à ces données, [merci de nous contacter](https://meteo.gc.ca/mainmenu/contact_us_f.html).

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info.comm.collab.science.gc.ca/).
