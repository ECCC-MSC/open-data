
![ECCC logo](../../../docs/img_eccc-logo.png)

-------------------------------------------------------

ENVIRONNEMENT ET CHANGEMENT CLIMATIQUE CANADA

Fichier README décrivant les données du Système régional de prévision déterministe d'onde de tempête (SRPDOT) pour la région de l'Atlantique nord-ouest disponibles sur le Datamart du Service météorologique du Canada (SMC).

Pour consulter ce fichier en ligne, allez à:
http://dd.meteo.gc.ca/model_surge/doc/rdsps/README_RDSPS.txt

Les fichiers sont produits par Environnement et Changement climatique Canada:
http://ec.gc.ca/

-------------------------------------------------------

# Version du 2019-02-13

Dans ce fichier:

* A propos
* Licence
* Téléchargement
* Fil de données
* Description
* Noms des fichiers
* Contenu des fichiers
* Liste des variables
* Pour nous joindre


##  À propos

Ce document décrit les données du modèle régional d'onde de tempête disponibles sur le serveur de données HTTP du SMC dans le répertoire:
http://dd.meteo.gc.ca/model_surge/nw_atlantic

Le fichier README global pour le Datamart du SMC peut être trouvé ici:
http://dd.meteo.gc.ca/about_dd_apropos.txt


##   Licence

Pour les conditions d'utilisation des données du SRPDOT, veuillez consulter les conditions générales d'utilisation des données du Datamart du SMC:
http://dd.meteo.gc.ca/doc/LICENCE_GENERAL.txt


##   Téléchargement

Les fichiers du SRPDOT se trouvent à l'adresse suivante:
http://dd.meteo.gc.ca/model_surge/nw_atlantic

Les prévisions des 24 dernières heures sont conservées dans ce répertoire.


##     Fil de données

Afin de faciliter l'obtention en temps opportun des données du Datamart, le
Service météorologique du Canada (SMC) a mis en place un fil de données
annonçant les fichiers disponibles sur le Datamart. Ce fil de données utilise le
protocole ''Advanced Message Queuing Protocol'' (AMQP). Il devient ainsi
possible non seulement d'être avisé de la disponibilité des produits sur le
Datamart lorsque ceux-ci sont publiés, mais aussi de les recevoir
automatiquement. Le service peut s'appliquer à une série spécifique de fichiers
(alertes météorologiques, observations, données de modèle, etc.) et ainsi viser
seulement les produits d'intérêt pour l'usager.

La documentation de ce service est disponible ici:
http://dd.weather.gc.ca/doc/README_AMQP.txt


##   Description

Le Système Régional de Prévision Déterministe d'Onde de Tempête (SRPDOT) produit
les prévisions de niveaux d'eau en utilisant le modèle d'océan DalCoast.
DalCoast (Bernier and Thompson 2015) est un sytème de prévision d'onde de
têmpete pour la côte est du Canada basé sur la version moyennée en profondeur,
barotrope et linéarisée du Modèle d'Océan de Princeton (POM). Le modèle est
forcé par les vents à une élévation de 10 mètres et la pression au niveau de la mer du Système Global de Prévision
Déterministe (SGPD).

Pour plus de détails, vous pouvez consulter le guide des produits du CMC sur Collaboration:
http://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/changes_f.html


##  Noms des fichiers

NOTE: TOUTES LES HEURES SONT EN UTC.

Les noms de fichiers ont la nomenclature suivante :

CMC_rdsps_domain_Variable_LevelType_level_latlond.dddxd.ddd_YYYYMMDDTHHZ_Phhh.nc

où :

* CMC : Chaîne de caractères constante indiquant que le Centre météorologique canadien (CMC) émet les prévisions
* rdsps : Chaîne de caractères constante indiquant que les données proviennent du Système régional de prévision déterministe d'onde de tempête
* domain : Chaîne de caractères constante indiquant le domaine
* Variable : Type de variable contenue dans le fichier
* LevelType : Type de niveau
* Level : Valeur du niveau
* latlond.dddxd.ddd : Chaîne de caractères constante indiquant que la projection utilisée est lat/long à une résolution de d.ddd x d.ddd degré
* YYYYMMDD : Année, mois et jour du début de la prévision
* HH : heure UTC du début de la passe `[00, 06, 12, 18]`
* Phhh : P est un caractère constant. hhh représente l’heure de prévision `[000, 001, 002, ..., 240]`
* nc : Chaîne de caractères constante indiquant que le format est NetCDF
* T: séparateur entre la date et l'heure
* Z: indicateur du fuseau horaire

Exemple de fichier :

CMC_rdsps_nw-atlantic_etas_SFC_0_latlon0.033x0.033_20180417T12Z_P024.nc

Le fichier a été créé par le CMC et contient une prévision du Système régional
de prévision déterministe d'onde de tempête. Il contient la hauteur d'onde de tempête (etas) pour le nord-ouest de l'océan Atlantique au niveau de la surface sur une grille
lat/long à une résolution de 0.033 degré par 0.033 degré. Il débute le 17
avril 2018 à 12Z (2018041712). Il contient l’heure de prévision 24 (P024) en
format NetCDF (.nc).


##   Contenu des fichiers

Les données dans les fichiers sont en format NetCDF conformes aux conventions CF liées au
climat et aux prévisions (Climate and Forecast Conventions) pour faciliter la distribution et la manipulation.

NetCDF est un format de fichier pour l’entreposage et la transmission de données
météorologiques sur grille telles que des sorties de modèles de prévision
numérique du temps. Il a été conçu pour être autodescriptif, compact et portable
entre les architectures informatiques. Le standard NetCDF a été conçu et est
maintenu par  University Corporation for Atmospheric Research (UCAR).

Des informations à propos de ce format et des logiciels pour le manipuler et le visualiser sont disponibles ici:
https://www.unidata.ucar.edu/software/netcdf/docs/index.html

Conventions CF:
http://cfconventions.org/


##   Liste de variables

La liste ci-dessous fournit pour chaque identifieur de paramètre NetCDF: une
brève description, une abréviation alphabétique, les niveaux pour lesquels ce
paramètre est disponible et les unités de mesure.


| NetCDF |   Description courte |                        Abr.|   Niveau | Unités|
|--------|--------|--------|--------|--------|
| etas   |  Onde de tempête     |                      ETAS  |  SFC_0 | m |


### Niveaux

Niveaux qui pourraient être applicables à certains champs :

* SFC : surface



##  Pour nous joindre

Si vous utilisez les données disponibles sur le Datamart du SMC, vous êtes
invités à vous inscrire à la liste de diffusion du Datamart du SMC afin d'être
avertis de tout changement ou mise à jour sur les données disponibles.

Vous pouvez vous inscrire ici:
http://lists.cmc.ec.gc.ca/mailman/listinfo/dd_info

Veuillez utiliser l'adresse courriel suivante pour nous contacter afin de nous faire part de tout commentaire ou question:
ec.dps-client.ec@canada.ca
