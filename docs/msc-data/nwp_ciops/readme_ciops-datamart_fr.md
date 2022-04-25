[In English](readme_ciops-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [SPCOG](readme_ciops_fr.md) > SPCOG prévision océanique sur le Datamart du SMC

# Données du Système de prévision côtier océan-glace (SPCOG) en format NetCDF 

Les prévisions océan-glace horaires sont disponibles en format NetCDF sur une grille latitude-longitude, correspondant à une résolution d'environ 2km (0.03 x 0.02 degrées) pour le domaine Est couvrant le Fleuve Saint-Laurent, le Golfe du Saint-Laurent et une région Nord-Ouest de l'océan Atlantique. Le domaine Ouest inclue la côte Ouest du Canada et le Nord-Est de l'océan Pacifique à une résolution d'environ 2km (0.03 x 0.02 degrées). Un sous-domaine couvrant la mer de Salish est aussi disponible à plus haute résolution (500m ou 0.008 x 0.005 degrées).

## Adresse des données 

Les données hébergées sur HPFX, le [serveur alternatif du Datamart du SMC](../../msc-datamart/readme_fr) peuvent être [automatiquement récupérées avec le Protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier NetCDF.

Les données sont accessibles aux adresses suivantes :

* [https://hpfx.collab.science.gc.ca/{YYYMMDD}/WXO-DD/model_ciops/east/2km/{HH}/{hhh}/](https://hpfx.collab.science.gc.ca/)
* [https://hpfx.collab.science.gc.ca/{YYYMMDD}/WXO-DD/model_ciops/west/2km/{HH}/{hhh}/](https://hpfx.collab.science.gc.ca/)
* [https://hpfx.collab.science.gc.ca/{YYYMMDD}/WXO-DD/model_ciops/salish-sea/500m/{HH}/{hhh}/](https://hpfx.collab.science.gc.ca/) 

où :

* __YYYYMMDD__ : Année, mois et jour 
* __HH__ : Heure en UTC du début de la simulation [00, 06, 12, 18]
* __hhh__ : Heure de la prévision [001, 002, 003, ..., 048] 

Un historique de 24h de prévision est stocké dans ces répertoires.

## Spécification technique des grilles

### Domaine océanique Est

![Image du domain océanique SPCOG - Est](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_ciops/grille_ciops-east.png)

| Paramètre | Valeur |
| ------ | ------ |
| ni | 1333 | 
| nj | 980 | 
| nk | 99 | 
| résolution | 2km |

### Domaine océanique Ouest

![Image du domain océanique SPCOG - Ouest](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_ciops/grille_ciops-west.png)

| Paramètre | Valeur |
| ------ | ------ |
| ni | 600 |
| nj | 785 |
| nk | 68 |
| résolution | 2km |

### Domaine océanique sur la mer de Salish

![Image du domain océanique CIOPS - Salish Sea](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_ciops/grille_ciops-salishsea.png)

| Paramètre | Valeur |
| ------ | ------ |
| ni | 629 |
| nj | 888 |
| nk | 39 |
| résolution | 500m |

## Nomenclature des noms de fichiers 

NOTE: TOUTES LES HEURES SONT EN UTC.

La nomenclature des noms des fichiers est la suivante :

`{YYYYMMDD}T{HH}Z_MSC_CIOPS-{Domain}_{Var}_{LVLTYPE}-{LVL}_{Grille}{resolution}_PT{hhh}H.nc`

où :

* __YYYYMMDD__ : Année, mois et jour du début de la prévision
* __T__ : Délimiteur temporel selon les normes ISO8601
* __HH__ : Heure UTC de la passe [00, 12]
* __Z__ : Fuseau horaire (heure UTC)
* __MSC__ : Chaîne de caractères constante pour Meteorological Service of Canada, la source des données
* __CIOPS__ : Chaîne de caractères constante indiquant le modèle source : SPCOG (CIOPS en anglais)
* __Domain__ : Chaîne de caractères constante indiquant le domaine [East, West, SalishSea]
* __Var__ : Variables contenues dans le fichier 
* __LVLTYPE__ : Type de niveau vertical [Sfc pour la surface, DBS pour la profondeur sous la surface]
* __LVL__ : Valeur du niveau vertical [0.5m, `all` pour tous les niveaux disponibles]. Ce paramètre est absent pour la surface
* __Grille__ : Grille horizontale [LatLon]
* __resolution__ : Indique la résolution en degré dans les directions longitudinale et latitudinale [0.03x0.02, 0.008x0.005]
* __PT{hhh}H__ : Echéance temporelle selon la norme [ISO8601](https://en.wikipedia.org/wiki/ISO_8601). P, T et H sont des caractères constants désignant Période, Temps et Heure. "hhh" représente l’heure de prévision  [001, 002, 003, ..., 048]
* __nc__ : Chaîne de caractères constante indiquant que le format est NetCDF

Exemples :

* 20220225T00Z_MSC_CIOPS-East_SeaIceDivergence_Sfc_LatLon0.03x0.02_PT002H.nc
* 20220301T00Z_MSC_CIOPS-West_SeaWaterSalinity_DBS-0.5m_LatLon0.03x0.02_PT002H.nc
* 20220301T00Z_MSC_CIOPS-SalishSea_SeaWaterPotentialTemp_DBS-all_LatLon0.008x0.005_PT002H.nc

## Liste des variables

Liste des variables 3D océaniques disponibles dans les fichiers:

* __SeaWaterSalinity__ : Salinité de l'eau de mer (psu) 
* __SeaWaterPotentialTemp__ : Température potentielle de l'eau de mer (K)
* __SeaWaterVelocityX__ : Composante X de la vitesse de l'eau (m/s)
* __SeaWaterVelocityY__ : Composante Y de la vitesse de l'eau (m/s)

Liste des variables 2D océaniques disponibles dans les fichiers:

* __SeaWaterSalinity__ : Salinité de l'eau de mer au premier niveau du modèle (per 1000) 
* __SeaWaterPotentialTemp__ : Température potentielle de l'eau de mer au premier niveau du modèle (K)
* __SeaWaterVelocityX__ : Composante X de la vitesse de l'eau au premier niveau du modèle (m/s)
* __SeaWaterVelocityY__ : Composante Y de la vitesse de l'eau au premier niveau du modèle (m/s)
* __SeaSfcHeight__ : Hauteur de la surface de la mer par rapport au géoïde (m)
* __MixedLayerThickness__ : Profondeur de la couche de mélange d'après le critère de densité (m)
* __TurboclineDepth__ : Profondeur de la turbocline (m)

Liste des variables 2D de glace disponibles dans les fichiers:

* __SeaIceVelocityX__ : Composante X de la vitesse de la glace de mer (m/s)
* __SeaIceVelocityY__ : Composante Y de la vitesse de la glace de mer (m/s)
* __SeaIceAreaFraction__ : Fraction de la glace de mer (fraction)
* __SeaIceVol__ : Volume de glace de mer par unité de surface de cellule de grille (m)
* __SeaIceSnowTemp__ : Température de surface de la neige sur la glace de mer ou la glace de mer nue (K)
* __SeaIceSnowVol__ : Volume de la neige de mer par unité de surface de cellule de grille (m)
* __SeaIceCompressiveStrength__ : Résistance à la compression de la glace, intégrée verticalement (N/m)
* __SeaIceDivergence__ : Divergence de la glace de mer (%/day)
* __SeaIceInternalPressure__ : Pression interne de la glace, intégrée verticalement (N/m)
* __SeaIceShear__ : Cisaillement de la glace de mer (%/day)

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).

