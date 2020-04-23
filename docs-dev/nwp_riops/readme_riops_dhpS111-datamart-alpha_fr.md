[in english](readme_riops_dhpS111-datamart-alpha_en.md )

![ECCC logo](../../docs/img_eccc-logo.png)


# Produits hydrographiques dynamiques (PHD-DHP) S-111 (format HDF5) utilisant les données de courants de surface du modèle océanographique SRPOG (Système Régional de Prévision Océan-Glace).

Cet ensemble de données tuilées de produits hydrographiques dynamiques (PHD-DHP) S-111 utilise les courants de surface du modèle océanographique opérationnel SRPOG d'ECCC. Les données S-111 tuilées utilisent un format standard et ouvert de fichier [HDF5](https://www.hdfgroup.org/solutions/hdf5/) avec une spécification très détaillée fournie par [l'Organisation hydrographique internationale (OHI)](https://iho.int/fr/). Tous les intervenants du domaine de la navigation maritime qui sont intéressés par les courants océaniques de surface des eaux côtières canadiennes du modèle SRPOG peuvent utiliser cet ensemble de données tuilées S-111 géoréférencées dans la représentation SIG [EPSG:4326](https://epsg.io/4326).

# Emplacement des données

Toutes les données environnementales qui sont présentes sur le serveur DD-Alpha du Service Météorologique du Canada(SMC) d'ECCC peuvent être [récupérées automatiquement avec le Protocole avancé de mise en file d'attente des messages (AMQP: Advanced Message Queuing Protocol)](../../docs/msc-datamart/amqp_fr.md) dès qu'elles sont disponibles. Un aperçu et des [exemples d'accès et d'utilisation des données ouvertes du SMC](../../docs/usage/readme_fr.md)  sont également disponibles.

On peut accéder aux données S-111 tuilées de courants de surface du modèle SRPOG avec un navigateur Web interactif à l'adresse suivante:

* [http://dd.alpha.weather.gc.ca/model_riops/dynamic_hydrographic_products/hdf5/{HH}/](http://dd.alpha.weather.gc.ca/model_riops/dynamic_hydrographic_products/hdf5/)

* __HH__: Heure zéro du début d'une instance de prévision synoptique du modèle SRPOG, en TU(UTC) [00, 06, 12, 18]

À noter que ces données S-111 sont renouvelées quatre fois par jour à la fin de chaque instance de prévision synoptique quotidienne du modèle opérationnel SRPOG.

# Nomenclature des noms de fichiers

NOTE: TOUTES LES HEURES SONT EN TEMPS UNIVERSEL(TU, UNIVERSAL TIME COORDINATE: UTC)

Les fichiers PHD-DHP S-111 tuilés utilsent la nomenclature suivante:

{YYYYYMMDD}T{HH}Z_MSC_RIOPS_111CA002{nnnn}N{wwwww}W.h5

* __YYYYYMMDD__: Année, Mois, Jour du début d'une instance de prévision synoptique du modèle SRPOG.
* __T__: Caractère de séparation temporel de la norme ISO8601 .
* __HH__: Heure zéro du début d'une instance de prévision synoptique du modèle SRPOG, en TU(UTC) [00, 06, 12, 18].
* __Z__: Caractère identifiant le fuseau horaire TU(UTC).
* __MSC__ : Identifiant pour le Service météorologique du Canada (Meteorological Service of Canada), le fournisseur de données.
* __RIOPS__: Identifiant du modèle SRPOG.
* __111__: Identifiant des données S-111.
* __CA__: Identifiant représentant le Canada.
* __002__: Identifiant pour les tuiles PHD-DHP de niveau 2 d'étendue régulière 1°x1° degrés(2°x1° degrés au Nord de la latitude 69° N).
* __nnnn__: Balise de quatre caractères numériques pour représenter la latitude en degrés décimaux(Hémisphère Nord) du coin Sud-Ouest de la délimitation de chaque tuile.
* __wwwww__: Balise de cinq caractères numériques pour représenter la longitude en degrés décimaux(Hémisphère Ouest) du coin Sud-Ouest de la délimitation de chaque tuile.
* __h5__: Extension officielle de nom de fichier pour le format HDF5.

Exemple d'un fichier tuile réel PHD-DHP S-111 tuilé:

20200129T18Z_MSC_RIOPS_111CA0024200N06900W.h5

Ce fichier provient du Service météorologique du Canada (MSC) et contient un sous-ensemble de courants de surface du modèle SRPOG délimité par une tuile PHD-DHP S-111 d'étendue 1°x1° degrés dont le coin sud-ouest est situé à la latitude 42,00N  et à la longitude 69,00W. Ce fichier tuilé S-111 a été produit par le post-traitement des résultats du modèle SRPOG provenant de son cycle de prévision synoptique du 29 janvier 2020 à 18TU(UTC).

# Liste des variables utilisées pour les courants de surface S-111

* __surfaceCurrentSpeed__ : Velocité [noeuds]
* __surfaceCurrentDirection__ : Angle de navigation [degrés décimaux: 0°-360°]

Ces deux variables sont regroupées dans une structure de données de type [HDF5 H5T_COMPOUND type](https://bitbucket.hdfgroup.org/pages/HDFFV/hdf5doc/master/browse/html/cpplus_RM/class_h5_1_1_comp_type.html) et ce pour chaque point de grille du modèle SRPOG et pour chaque pas de temps.

Chaque fichier PHD-DHP S-111 contient également une liste très complète de métadonnées. Vous pouvez obtenir tous les détails de ces métadonnées en consultant le document offciel des PHD-DHP S-111(version 1.0.1) [sur le site web de l'OHI](http://registry.iho.int/beta/productspec/view.do?idx=168&product_ID=S-111&statusS=5&domainS=ALL&category=product_ID&searchValue=).

# Système de référence spatiale commune pour les applications SIG

* Les fichiers HDF5 S-111 utilisent le [EPSG:4326](https://epsg.io/4326) en tant que système de référence spatiale(Coordinate Reference System) [CRS](https://docs.qgis.org/2.8/en/docs/gentle_gis_introduction/coordinate_reference_systems.html) officiel pour localiser les points de grille du modèle SRPOG en tant que couche dans une application SIG graphique.

# Structures internes de données des fichiers S-111

* Chaque fichier S-111 est une tuile d'étendue régulière 1°x1° degrés (2°x1° degrés au Nord de la latitude 69° N) qui contient un sous-ensemble de données de courants de surface qui proviennent du modèle SRPOG.
 
* L'utilisation du système de référence spatiale commune EPSG:4326 ainsi que du format de codage no.3(équivalent à une grille non-structurée) de la specification PHD-DHP S-111(version 1.0.1) de l'OHI permet l'utilisation directe, sans aucune interpolation, des données de courants de surface du modèle SRPOG qui lui-même utilise une grille polaire stéréographique à résolution de 5km resolution centrée à la latitude 60° N.

* Chaque fichier S-111 tuilé contient 55 structures(HDF5 GROUP) de données à référence temporelle appelée __"timePoint"__ qui elles mêmes contiennent plusieurs données(points de grille) de courants de surface sous forme d'objets de type HDF5 H5T_COMPOUND. Les 6 premières de ces structures de données à référence temporelles __"timePoint"__ contiennent les données des 6 premiers pas de temps des courants de surface de l'avant dernière instance de prévision synoptique du modèle SRPOG et les 49 dernières de ces structures de données à référence temporelle __"timePoint"__ contiennent les données de courants de surface de la dernière instance de pévision synoptique du modèle SRPOG.

# Exemples de domaines tuilés des eaux côtières canadiennes pour les courants de surface de SRPOG.
 
## Tuiles 1°x1° degrés: Baie de Fundy, plate-forme néo-écossaise et détroit de Northumberland.

![PNG Scotian shelf L2 tiles](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_riops/dynamic_hydrographic_products/ScotianShelfL2_tiles.png)

## Tuiles 1°x1° degrés: Golfe du Saint-Laurent

![PNG GStl L2 tiles](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_riops/dynamic_hydrographic_products/GSTLL2Tiles.png)

## Tuiles 1°x1° degrés: Côte-Ouest (secteur Sud)

![PNG West-Coast L2 tiles](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_riops/dynamic_hydrographic_products/WCoastL2Tiles.png)

## Tuiles 1°x1° degrés: Côte-Ouest (secteur Nord)

![PNG GStl L2 tiles](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_riops/dynamic_hydrographic_products/WCoastNL2Tiles.png)


