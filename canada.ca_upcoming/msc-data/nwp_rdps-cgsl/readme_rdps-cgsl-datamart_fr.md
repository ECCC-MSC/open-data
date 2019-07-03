[In English](readme_rdps-cgsl-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données ouvertes publiques du SMC](../readme_fr.md) > SRPD couplé au Golfe du Saint-Laurent sur le Datamart du SMC

# Données GRIB2 système régional de prévision déterministe couplé au Golfe du Saint-Laurent

Cette page décrit les données [système régional de prévision déterministe couplé au Golfe du Saint-Laurent](readme_rdps-cgsl_fr.md) disponibles en format GRIB2.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTP. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier GRIB2. Nous vous recommandons d’automatiser le téléchargement en le scriptant avec wget (lien externe, anglais) ou un programme équivalent. Pour plus d’information sur wget, consultez les notes d’utilisation.

Les données sont accessibles aux adresses suivantes :

* https://dd.meteo.gc.ca/model_gem_regional/coupled/gulf_st-lawrence/grib2/HH/hhh

où :

* __HH__ : Heure UTC du début de la passe du modèle [00, 06, 12, 18]
* __hhh__ : Heure de prévision [001, 002, 003, ..., 048]

## Spécification technique de la grille

![](http://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_rdps-cgsl/grille_rdwps-gsl.png)

Valeurs données aux paramètres de la grille latitude-longitude :

| Paramètre | Valeur |
| ------ | ------ |
| ni | 500 |
| nj | 325 | 
| résolution | 0.02° x 0.03° |
| coordonnées du premier point de grille | 45° 30' N  71° W |

## Spécifications relatives aux données

Les champs du jeu de données GRIB2 pour les deux composantes du système sont disponibles sur une grille latitude-longitude de 500 x 325, à 0,02 x 0,03 degrés de résolution. Ces données concernent les prévisions des variables répertoriées dans le tableau ci-dessous :

|Variable   |                     Description                                   |          Composante du système      |
|-----------|-------------------------------------------------------------------|-------------------------------------|
|UGRD       | Composante zonale du vent à la surface en [m/s]                   | Atmosphérique                       |
|VGRD       | Composante méridienne du vent à la surface en [m/s]               | Atmosphérique                       |
|TMP        | Température de surface (entre 0 et 5m) en [Kelvin]                | Océanique                           |
|ICEC       | Fraction de glace                                                 | Océanique                           |  
|ICETK      | Épaisseur de la glace en [m]                                      | Océanique                           |
|UICE       | Composante zonale du vecteur vitesse de glace [m/s]               | Océanique                           |
|VICE       | Composante méridienne du vecteur vitesse de glace [m/s]           | Océanique                           |
|UOGRD      | Composante zonale du vecteur du courant océanique de surface [m/s]| Océanique                           |
|VORGD      | Composante méridienne du vecteur du courant océanique de surface [m/s] | Océanique                      |
|WTMP       | Température de surface de la mer [Kelvin]                         | Océanique                           |
|ICET       | Température de surface de glace [Kelvin]                          | Océanique                           |
|ICEPRS     | Intégrale verticale de la pression interne [N/m ou Pa x m]        | Océanique                           |
|ICESTG     | Intégrale verticale de la force de compression de glace [N/m ou Pa x m] | Océanique                     |

## Nomenclature des noms de fichiers 

NOTE : TOUTES LES HEURES SONT EN UTC.

Les fichiers ont la nomenclature suivante :

* __Nom du fichier pour les données atmosphèriques__ : CMC_coupled-rdps-stlawrence-atmosphere_latlon0.02x0.03_AAAAMMJJHH_P0hh.grib2
* __Nom du fichier pour les données océaniques__ : CMC_coupled-rdps-stlawrence-ocean_latlon0.02x0.03_AAAAMMJJHH_P0hh.grib2

où :

* __CMC__ : Chaîne de caractères constante indiquant le centre météorologique (CMC) émetteur des prévisions.
* __coupled-rdps-stlawrence-ocean__ : Chaîne de caractères constante indiquant que les données proviennent de la composante océanique Système régional de prévision déterministe couplé au Golfe du Saint-Laurent.
* __latlon0.02x0.03__ : Chaîne de caractères constante indiquant que la projection utilisée est latitude-longitude à 0,02 x 0,03 degrés de résolution.
* __YYYYMMDD__ : Année (YYYY), mois (MM) et jour (DD) du début de la prévision.
* __HH__ : Heure UTC des passes [00, 06, 12, 18].
* __Phhh__ : « P » est un caractère constant qui indique le mot  « Prévision » . « hhh » représente l’heure de prévision [001, 002, 003, ..., 048].
* __grib2__ : Chaîne de caractères constante indiquant que le format est GRIB2.

Exemple de nom de fichier :

* __Données atmosphériques__ : CMC_coupled-rdps-stlawrence-atmosphere_latlon0.02x0.03_2015011200_P048.grib2
* __Données océaniques__ : CMC_coupled-rdps-stlawrence-ocean_latlon0.02x0.03_2015011200_P048.grib2

Les fichiers ont été créés par le Centre Météorologique Canadien (CMC) et contiennent la composante atmosphérique (océanique) du Système régional de prévision déterministe couplé au Golfe du Saint-Laurent sur une grille latitude-longitude de 500 x 325 points de grille à 0,02 x 0,03 degrés de résolution. La prévision a été produite le 12 janvier 2015 à 00Z (2015011200). Il contient l’heure de prévision 48 (P048) en format GRIB2 (.grib2). 

## Niveaux

Les données sont disponibles pour la surface seulement.

## Liste des variables

Attention : les tableaux ci-dessous ne sont pas à jour (à venir), certaines variables sont manquantes. N'hésitez pas à [nous contacter](mailto:ec.dps-client.ec@canada.ca) pour plus d'information.

* [Composante atmosphérique](https://meteo.gc.ca/grib/GF_COUPLED/GULF-ST-LAWRENCE-ATMOSPHERE_latlon0.02x0.03_NONZERO_coupled_f.html)
* [Composante océanique](https://meteo.gc.ca/grib/GF_COUPLED/GULF-ST-LAWRENCE-OCEAN_latlon0.02x0.03_NONZERO_coupled_f.html)

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : ec.dps-client.ec@canada.ca

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).
