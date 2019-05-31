# Gabarit pour les pages d'un jeu de données sur le Datamart du SMC

Ce gabarit est utilisé pour les pages des jeux de données sous `/msc-datamart/`


## Nom du jeu de données

Les données du [`nom de jeu de données` sont décrites sur la page sommaire](../msc-data/NOM_fr.md). Cette page fournit la documentation technique de ces données disponibles sur le [Datamart du SMC](msc-datamart_fr.md). Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../how-to/readme_fr.md) est disponible.

## Adresse des données 

Les données sont disponibles à l'adresse : http://dd.meteo.gc.ca.../HH/hhh/  (pour les données de modèle)

où :

    HH : Heure UTC du début de la passe du modèle [00,]
    hhh : Heure de prévision [000, ]

## Grille(s) disponible(s)

Si pertinent, donner les desciptions des grilles et au besoin des images des domaines 

## Nomenclature des noms de fichiers 

NOTE: TOUTES LES HEURES SONT EN UTC.

Les noms des fichiers ont la forme: 
YYYYYYYYYYYYYYYYYYYYYYYYYYY

où:

* ...
* ...

Exemple: 
Donner un exemple de noms de fichier typique

Au besoin, décrire la nomenclature des éventuels multiples répertoires dans lesquels les fichiers pourraient se trouver (ex: http://dd.weatheroffice.gc.ca/ensemble/naefs/xml/AAAAMMJJ/ZZ/VARIABLE/TYPE)

## Niveaux  

Décrire la liste des niveaux disponibles, si pertinent (ne s’applique qu’aux jeux de données 3D)

## Contenu des fichiers
 
à confirmer si pertinent ou si l’info peut se retrouver egrainée ailleurs

Décrire le contenu du fichier avec le plus de détails possible (ex: dans le cas des fichiers XML, décrire les en-têtes, les sections et les éléments).

Lorsque s'applique, indiquer si les fichiers ont été compressés et avec quel utilitaire (ex: bzip2). Indiquer comment les décompresser.

Lorsque s'applique, indiquer si les fichiers ont été encodés ou non, dans quel format et dans quel standard d'encodage (ex: UTF-8).

Au besoin, indiquer la précision des données.

Inclure un lien vers la documentation du format si pertinent (ex: format GRIB).

## Liste des variables

Les variables disponibles de XXXXXX sont:

* VAR_1 : Définition
* VAR_2 : Définition
* ...
* ...
