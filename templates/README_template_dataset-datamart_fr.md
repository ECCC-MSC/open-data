# Gabarit pour les pages d'un jeu de données sur le Datamart du SMC

Ce gabarit est utilisé pour les pages des jeux de données sous `/msc-data/`. Ajouter le lien vers la version anglaise, le logo et le fil d'Ariane


## Données *indiquer le format* du *nom du jeu de données -tout au long pour les NWP-* (*acronyme si pertinent*)

*Une ligne de présentation tirée des README ou de [WxO](https://meteo.gc.ca/grib/index_f.html)*

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le Protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage-overview/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTP. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier *indiquer le format des données*.

Les données sont disponibles à l'adresse : https://dd.meteo.gc.ca.../HH/hhh/  (pour les données de modèle)

où :

    HH : Heure UTC du début de la passe du modèle [00,]
    hhh : Heure de prévision [000, ]

## Spécification technique de la grille - *(pour les NWP seulement)*

*Si pertinent, donner les desciptions des grilles sour forme de tableau, via WxO et au besoin des images des domaines. Les images devont être rassemblées sur [Collaboration](http://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc) et seulement référées ici via ![](adresse)*

## Nomenclature des noms de fichiers 

NOTE: TOUTES LES HEURES SONT EN UTC.

Les noms des fichiers ont la forme: 
YYYYYYYYYYYYYYYYYYYYYYYYYYY

où:

* ...
* ...

Exemple: 
*Donner un exemple de noms de fichier typique*

*Au besoin, décrire la nomenclature des éventuels multiples répertoires dans lesquels les fichiers pourraient se trouver (ex: https://dd.weatheroffice.gc.ca/ensemble/naefs/xml/AAAAMMJJ/ZZ/VARIABLE/TYPE)*

## Niveaux  

*Décrire la liste des niveaux disponibles, si pertinent (ne s’applique qu’aux jeux de données 3D)*

## Contenu des fichiers - *vérifier si pertinent avec les README*
 
*A confirmer si pertinent ou si l’info peut se retrouver egrainée ailleurs*

*Décrire le contenu du fichier avec le plus de détails possible (ex: dans le cas des fichiers XML, décrire les en-têtes, les sections et les éléments).*

*Lorsque s'applique, indiquer si les fichiers ont été compressés et avec quel utilitaire (ex: bzip2). Indiquer comment les décompresser.*

*Lorsque s'applique, indiquer si les fichiers ont été encodés ou non, dans quel format et dans quel standard d'encodage (ex: UTF-8).*

*Au besoin, indiquer la précision des données.*

*Inclure un lien vers la documentation du format si pertinent (ex: format GRIB).*

## Liste des variables

Les variables disponibles de XXXXXX sont:

* VAR_1 : Définition
* VAR_2 : Définition
* ...
* ...
*

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : ec.dps-client.ec@canada.ca

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).

