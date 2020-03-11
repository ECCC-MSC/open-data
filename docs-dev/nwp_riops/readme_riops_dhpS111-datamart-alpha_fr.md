[in english](readme_riops_S111-datamart-alpha_en.md)

![ECCC logo](../../docs/img_eccc-logo.png)


# Produits hydrographiques dynamiques (PHD-DHP) S-111 (format HDF5) utilisant les données de courants de surface du modèle océanographique RIOPS (Regional Ice Ocean Prediction System).

Cet ensemble de données tuilées de produits hydrographiques dynamiques (PHD-DHP) S-111 utilise les courants de surface du modèle océanographique opérationnel RIOPS d'ECCC. Les données S-111 tuilées utilisent un format standard et ouvert de fichier [HDF5](ttps://www.hdfgroup.org/solutions/hdf5/) avec une spécification très détaillée fournie par [l'Organisation hydrographique internationale (OHI)](https://iho.int/fr/) . Tous les intervenants du domaine de la navigation maritime qui sont intéressés par les courants océaniques de surface des eaux côtières canadiennes du modèle RIOPS peuvent utiliser cet ensemble de données tuilées S-111 géoréférencées dans la représentation SIG [EPSG:4326](https://epsg.io/4326) commune.

# Emplacement des données

Toutes les données environnementales qui sont présentes sur le serveur DD-Alpha du Service Météorologique du Canada(SMC) d'ECCC peuvent être [récupérées automatiquement avec le Protocole avancé de mise en file d'attente des messages (AMQP: Advanced Message Queuing Protocol)](../../docs/msc-datamart/amqp_fr.md) dès qu'elles sont disponibles. Un aperçu et des [exemples d'accès et d'utilisation des données ouvertes du SMC](../../docs/usage/readme_fr.md)  sont également disponibles.

On peut accéder aux données avec un navigateur Web interactif à l'adresse suivante:

* [http://dd.alpha.weather.gc.ca/model_riops/dynamic_hydrographic_products/hdf5/{HH}/](http://dd.alpha.weather.gc.ca/model_riops/dynamic_hydrographic_products/hdf5/)

* __HH__: Model run start, in UTC [00, 06, 12, 18]

L'accès HTTP à ce répertoire avec un navigateur interactif Web produira une liste brute de liens, chaque lien étant un fichier HDF5 téléchargeable. En pratique, nous vous recommandons d'écrire votre propre script pour automatiser le téléchargement des données souhaitées (en utilisant wget ou curl). Si vous ne savez pas comment procéder, vous pouvez consulter [notre guide succint d'utilisation de l'utilitaire wget](../../docs/msc-datamart/readme_wget-datamart_fr.md).

À noter que ces données S-111 sont renouvelées quatre fois par jour à la fin de chaque cycle de prévision synoptique quotidienne du modèle opérationnel RIOPS.

# Nomenclature des noms de fichiers

NOTE: TOUTES LES HEURES SONT EN TEMPS UNIVERSEL(TU, UNIVERSAL TIME COORDINATE: UTC)

Les fichiers PHD-DHP S-111 tuilés utilsent la nomenclature suivante:

CMC_riops_111CA002{nnnn}N{wwwww}W_{YYYYYMMDD}T{HH}Z.h5

* __CMC__ : Identifiant du Centre Météorologique Canadien (CMC).
* __riops__: Identifiant du modèle RIOPS.
* __111__: Identifiant des données S-111.
* __CA__: Identifiant représentant le Canada.
* __002__: Identififiant pour les tuiles PHD-DHP 1x1 degrés.
* __nnnn__: Balise de quatre caractères numériques pour représenter la latitude en degrés décimaux(Hémisphère Nord) du coin Sud-Ouest de la délimitation de chaque tuile de 1x1 degrés.
* __wwwww__: Balise de cinq caractères numériques pour représenter la longitude en degrés décimaux(Hémisphère Ouest) du coin Sud-Ouest de la délimitation de chaque tuile de 1x1 degrés.
* __YYYYYMMDD__: Année, Mois, Jour du début de la prévision du modèle RIOPS.
* __T__: Caractère de séparation temporel de la norme ISO8601 .
* __HH__: Heure zéro du cycle de prévision synoptique du modèle RIOPS, en TU(UTC) [00, 06, 12, 18].
* __Z__: Caractère identifiant le fuseau horaire TU(UTC).
* __h5__: Extension officielle de nom de fichier pour le format HDF5.

Exemple d'un fichier tuile réel PHD-DHP S-111:

__CMC_riops_111CA0024200N06900W_20200129T18Z.h5__

Ce fichier provient du Centre Météorologique Canadien (CMC) et contient les courants de surface du modèle RIOPS à l'intérieur d'une tuile PHD-DHP S-111 d'étendue 1x1 degré dont le coin sud-ouest est situé à la latitude 42,00N  et à la longitude 69,00W. Ce fichier tuilé S-111 a été produit par le post-traitement des résultats du modèle RIOPS provenant de son cycle de prévision synoptique du 29 janvier 2020 à 18TU(UTC).

# Liste des variables utilisées pour les courants de surface S-111 .

* 1). __"Speed"__(en noeud) pour chacun des points de grille du modèle RIOPS.
* 2). __"Direction"__(angle de navigation 0°-360°) pour chacun des points de grille du modèle RIOPS.