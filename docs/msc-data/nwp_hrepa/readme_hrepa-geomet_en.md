# Données de l'Analyse à Haute Résolution Ensembliste de Précipitation (AHREP) sur GeoMet du SMC

GeoMet du SMC donne accès à plusieurs couches de Système global de l'Analyse à Haute Résolution Ensembliste de Précipitation (AHREP). Les usagers peuvent développer des applications mobiles, créer des cartes interactives en ligne, ainsi que visualiser et animer les données du SMC dans des logiciels de bureau.

## Accès aux services web géospatiaux
Les couches du SPGE sont disponibles sur [GeoMet-Météo par le biais des standards WMS (Web Map Service) et WCS (Web Coverage Service).](https://gccode.ssc-spc.gc.ca/afsgdod/public-doc/-/blob/dhps/docs/msc-geomet/readme_fr.md)

Exemple de carte interactive présentant la couche Precip-Accum06h-Pct25 du AHREP provenant de GeoMet du SMC :

## Utilisation

La page de l'[aperçu de l'utilisation](https://gccode.ssc-spc.gc.ca/afsgdod/public-doc/-/blob/dhps/docs/usage/readme_fr.md) présente l'information de base sur l'utilisation de ces services avec des logiciels de bureau, des applications mobiles, les cartes interactives en ligne ainsi que l'accès direct. Veuillez vous référer aux [tutoriels et à la documentation technique sur les services web géospatiaux GeoMet du SMC](https://gccode.ssc-spc.gc.ca/afsgdod/public-doc/-/blob/dhps/docs/msc-geomet/web-services_fr.md) pour de l'information détaillée.

### Couches disponibles

Trois couches sont disponibles pour AHREP:
* Precip-Accum06h [mm]: accumulations de précipitation sur une période de 6h
* Precip-Accum06h-Pct25 [mm]: percentile 25 estimé sur l'ensemble de 25 membres des accumulations de précipitation 6h
* Precip-Accum06h-Pct75 [mm]: percentile 75 estimé sur l'ensemble de 25 membres des accumulations de précipitation 6h

Les fichiers netCDFs ont la nomemclature suivante:
* `<AAAAMMJJ>T<HH>_MSC_HREPA_<nom_couche>_Sfc_<grille><resolution_deg>.nc`, où: 
    * `<AAAAMMJJ>`: représente la date au format année, mois et jour, p.ex. `20220214`
    * `<HH>`: représente l'heure de validité de l'analyse, ici les heures synoptiques, *i.e* 00, 06, 12 et 18.
    * `<nom_couche>`: correspond au nom de la couche, ici Precip-Accum06, Precip-Accum06h-Pct25 ou Precip-Accum06h-Pct75.
    * `<grille>`: correspond à la grille utilisée pour le système, ici une grille tournée (*rotated grid*) d'ou le *RLatLon*
    * `resolution_deg`: donne une information sur la résolution de la grille, ici 0.0225 soit environ 2.5km.

Ainsi, pour récuperer les ensembles des accumulations de précipitions sur 6h valides à 12Z (heure UTC) pour le 14 février 2022, il faudrat récupérer le fichier netcdf suivant:
* `20220214T06Z_MSC_HREPA_Precip-Accum06h_Sfc_RLatLon0.0225.nc`


### Conseils d'utilisation

Récupération de la liste des derniers pas de temps disponibles :

* Les utilisateurs peuvent ajouter le paramètre `layer` à une requête WMS GetCapabilities afin de pointer à une couche spécifique et obtenir une réponse XML plus simple avec les dimensions temporelles à jour. 
    - Exemple pour la couche 20220214T06Z_MSC_HREPA_Precip-Accum06h-Pct25_Sfc_RLatLon0.0225.nc - 25eme percentile de précipitations issue de l'ensemble à 25 membres [mm] : https://geo.weather.gc.ca/geomet?lang=fr&service=WMS&version=1.3.0&request=GetCapabilities&layer=20220214T06Z_MSC_HREPA_Precip-Accum06h-Pct25_Sfc_RLatLon0.0225.nc
* Davantage d'information est disponible dans la section sur la spécification du temps avec les services WMS


Styles WMS :

* En plus du style WMS par défaut, plusieurs styles WMS alternatifs avec des échelles de couleurs différentes sont disponibles. La liste des styles WMS est fournie dans la réponse d'une requête WMS GetCapabilities
* Par ailleurs, les utilisateurs peuvent visualiser les couches avec leurs propres styles en utilisant le standard *Styled Layer Descriptor* (SLD). Veuillez vous référer à la documentation technique sur le SLD


## Support

Les services GeoMet du SMC sont opérationnels 24/7. Le support aux usagers est offert sur la base du meilleur effort durant les heures de travail normales. Les usagers désirant du support sont invités à communiquer avec nous.

## Liste d'information
Nous encourageons les usagers à s'abonner à la liste d'information GeoMet-Info afin d'être informés des améliorations et changements aux services GeoMet du SMC.