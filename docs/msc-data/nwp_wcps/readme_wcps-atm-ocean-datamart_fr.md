[In English](readme_wcps-atm-ocean-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [SPCE](readme_wcps_fr.md) > SPCE couplées océan-atmosphère sur le Datamart du SMC

# Données des prévisions couplées atmosphère-océan-glace de mer du système de prévision du cycle de l’eau (SPCE) en format NetCDF 

Les prévisions couplées atmosphère-océan-glace de mer de GEM-LAM avec NEMO-CICE sont disponibles aux heures au format NetCDF sur une grille latitude-longitude, correspondant à une résolution d'environ 1km (0.008 x 0.008 degré), sur le domaine des Grands Lacs, du fleuve Saint-Laurent et du Golfe du Saint-Laurent. 

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le Protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier netCDF.

Les données sont accessibles à l'adresse suivante :

* [https://dd.meteo.gc.ca/model_wcps/ocean-atmosphere/1km/{HH}/{hhh}/](https://dd.meteo.gc.ca/model_wcps/ocean-atmosphere/1km)                  

où :

* __HH__ : Heure en UTC du début de la simulation [00,06,12,18]
* __hhh__ : Heure de la prévision [001, ..., 084] 

Un historique de 24h de prévision est stocké dans ce répertoire.

## Spécification technique de la grille  

![Image du domaine SPCE ocean-atmosphere](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_wcps/grille_wcps_ocean-atm.png)

Dans le domaine complet indiqué en blanc, l'ensemble des données valides qui couvrent les lacs et les océans, est en couleur. Dans le reste du domaine, un masque "no-data" est utilisé pour spécifier l'abscence de donnée.

| Paramètre | Valeur |
| ------ | ------ |
| ni | 6675 | 
| nj | 2364 | 
| résolution à 45° N | 1km |


## Nomenclature des noms de fichiers 

NOTE: TOUTES LES HEURES SONT EN UTC.

La nomenclature des noms des fichiers est la suivante :

`{YYYYMMDD}T{HH}Z_MSC_WCPS_{VAR}_{LVLTYPE}-{LVL}_{grille}{resolution}_PT{hhh}H.nc`

où :

* __YYYYMMDD__ : Année, mois et jour du début de la prévision
* __T__ : Délimiteur temporel selon les normes ISO8601
* __HH__ : Heure UTC de la passe [00, 06, 12, 18]
* __Z__ : Fuseau horaire (heure UTC)
* __MSC__ : Chaîne de caractères constante pour Meteorological Service of Canada, la source des données
* __WCPS__ : Chaîne de caractères constante indiquant que les données proviennent du Système de prévision du cycle de l'eau 
* __VAR__ : Variables contenues dans le fichier 
* __LVLTYPE__ : Type de niveau vertical [Sfc pour la surface, DBS pour la profondeur sous la surface, AGL pour la hauteur au-dessus du sol]
* __LVL__ : Valeur du niveau vertical [10m, 0.5m, 1.5m, `0-2m` de la surface à 2 mètres, `all` pour tous les niveaux disponibles]. Ce paramètre est absent pour la surface
* __grille__ : Grille horizontale [LatLon]
* __resolution__ : Indique la résolution en degré dans les directions longitudinale et latitudinale soit ici 0.008°(environ 1km) dans les deux directions
* __PT{hhh}H__ : Echéance temporelle selon la norme [ISO8601](https://en.wikipedia.org/wiki/ISO_8601). P, T et H sont des caractères constants désignant Période, Temps et Heure. "hhh" représente l’heure de prévision  [001, 002, ..., 084]
* __nc__ : Chaîne de caractères constante indiquant que le format est NetCDF

Exemples :

* 20211208T12Z_MSC_WCPS_SeaIceSnowVol_Sfc_LatLon0.008_PT001H.nc
* 20211208T12Z_MSC_WCPS_SeaWaterPotentialTemp_DBS-0.5m_LatLon0.008_PT001H.nc

## Liste des variables

Liste des variables 2D disponibles dans les fichiers:

* __AirTemp__ : Température de l'air à 1.5 mètres en altitude (K)
* __WindU__: Composante X de la vitesse du vent à 10 mètres en altitude (m/s)
* __WindV__: Composante Y de la vitesse du vent à 10 mètres en altitude (m/s)
* __Runoff__ : Ruissellement (mm)
* __SeaSfcHeight__ : Hauteur de la surface de la mer par rapport au géoïde (m). Pour les Grands Lacs, la référence est IGLD85
* __SeaWaterSalinity__ : Salinité de l'eau de mer au premier niveau du modèle (per 1000) 
* __SeaWaterPotentialTemp__ : Température potentielle de l'eau de mer au premier niveau du modèle (K)
* __SeaWaterVelocityX__ : Composante X de la vitesse de l'eau au premier niveau du modèle (m/s)
* __SeaWaterVelocityY__ : Composante Y de la vitesse de l'eau au premier niveau du modèle (m/s)
* __MixedLayerThickness__ : Profondeur de la couche de mélange d'après le critère de densité (m)
* __TurboclineDepth__ : Profondeur de la turbocline (m)
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

Les variables `AirTemp`, `WindU`, `WindV` et `Runoff_Sfc` (ruissellement de surface) sont issues de GEM-LAM et les autres variables sont issues de NEMO-CICE.

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).

