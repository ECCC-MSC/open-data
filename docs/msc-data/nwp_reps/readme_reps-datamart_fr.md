[In English](readme_reps-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [SRPE](readme_reps_fr.md) > SRPE sur le Datamart du SMC

# Données GRIB2 du Système régional de prévision d'ensemble (SRPE)

Cette page décrit les données du [système régional de prévision d'ensemble](readme_reps_fr.md) disponibles en format GRIB2.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier GRIB2.

Les données sont accessibles aux adresses suivantes :

* Données à 15km sur grille polaire stéréographique : [https://dd.meteo.gc.ca/ensemble/reps/15km/grib2/{EnsembleTypeDonnee}/{HH}/{hhh}](https://dd.meteo.gc.ca/ensemble/reps/15km/grib2)
* Données à 10km sur grille lat-lon tournée : [https://dd.meteo.gc.ca/ensemble/reps/10km/grib2/{HH}/{hhh}](https://dd.meteo.gc.ca/ensemble/reps/10km/grib2)

où :

* __EnsembleTypeDonnee__ : Peut être "raw" pour les sorties brutes des membres individuels ou "prob" pour les produits probabilistes générés à partir de tous les membres
* __HH__ : Heure de la passe du modèle en TU
* __hhh__ : Heure de la prévision

Un historique de 24 heures est conservé dans ce répertoire.

## Spécification technique des grilles

* __Grille polaire stéréographique__

![Grille du SRPE ps](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_reps/grille_reps_ps.png)

Valeurs données aux paramètres de la grille polaire stéréographique à 15km de résolution:

| Paramètre | Valeur |
| ------ | ------ |
| ni | 600 |
| nj | 510 | 
| résolution à 60° N | 15km |
| coordonnées du premier point de grille | 19.3206° N ; 141.5411° W | 
| orientation de la grille (par rapport à l’axe des j) | -110.0° | 

* __Grille lat-lon tournée__

![Grille du SRPE Rlatlon](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_reps/grille_reps_rlatlon.png)

Valeurs données aux paramètres de la grille lat-lon tournée à 10km de résolution:

| Paramètre | Valeur |
| ------ | ------ |
| ni | 908 |
| nj | 960 | 
| résolution à 60° N | 10km |
| coordonnées du premier point de grille | 50.76° N ; 20.81° W | 

__Note__ : Les [versions les plus récentes de wgrib2](https://www.cpc.ncep.noaa.gov/products/wesley/wgrib2/update_2.0.8.html) et [GDAL](https://gdal.org/) supportent ces grilles tournées. 

## Nomenclature des noms de fichiers 

NOTE : TOUTES LES HEURES SONT EN UTC.

### Grille polaire stéréographique à 15km de résolution

Les fichiers ont la nomenclature suivante :

```
CMC-reps-srpe-{datatype}_{VAR}_{LVLTYPE}_{LVL}_{resolution}_{YYYYMMDDHH}_P{hhh}_{content}.grib2
```

où :

* __datatype__ : Peut être "raw" pour les sorties brutes des membres individuels ou "prob" pour les produits probabilistes générés à partir de tous les membres
* __VAR__ : Type de variable contenu dans le fichier (ex: UGRD)
* __LVLTYPE__ :  Niveau vertical (ex: SFC pour la surface, NTAT pour le haut de l'atmosphère, DBLL_10cm couche 10cm sous la surface, TGL pour au-dessus de la surface)
* __LVL__ : Valeur du niveau (ex: 10m pour 10 mètres)
* __resolution__: Résolution de la grille (ex: ps15km) 
* __YYYYMMDDHH__: Année, mois, jour du début de la prévision et heure UTC de la passe [00, 12]
* __P{hhh}__ :  « P » est un caractère constant. « hhh » représente l’heure de prévision [000, 003, 006, ..., 072]
* __content__ : Peut être "all-products" ou "allmbrs" pour indiquer que tous les membres ou tous les produits probabilistes pour cette variable sont regroupés dans ce fichier
* __grib2__ : Chaîne de caractères constante indiquant que le format est GRIB2.

Exemple de nom de fichier : CMC-reps-srpe-prob_TEMP_TGL_2m_ps15km_2021012700_P009_all-products.grib2

### Grille lat-lon tournée à 10km de résolution

Les fichiers ont la nomenclature suivante :

```
{YYYYMMDD}T{HH}Z_MSC_REPS_{VAR}_{LVLTYPE-LVL}_{Grille}{resolution}_PT{hhh}H.grib2
```

où :

* __YYYYMMDD__ : Année, mois et jour du début de la prévision
* __T__ : Délimiteur temporel selon les normes ISO8601
* __HH__ : Heure UTC de la passe [00, 06, 12, 18]
* __Z__ : Fuseau horaire (heure UTC)
* __MSC__ : Chaîne de caractères constante pour Meteorological Service of Canada, la source des données
* __REPS__ : Chaîne de caractères constante indiquant que les données proviennent du Système régional de prévision d'ensemble
* __VAR__ : Type de variable contenu dans le fichier (ex: UGRD). Ce paramètre comprend aussi le processus statistique associé si pertinent (ex: Accum, Max, Min). 
* __LVLTYPE-LVL__ : Niveau vertical et hauteur [ex: SFC pour la surface, AGL-10m pour 10m au-dessus du sol]
* __Grille__ : Grille horizontale [RLatLon]
* __resolution__ : 0.09. Signifie une résolution de 0.09°(environ 10km) dans les directions longitudinale et latitudinale
* __PT{hhh}H__ : Echéance temporelle selon la norme [ISO8601](https://en.wikipedia.org/wiki/ISO_8601). P, T et H sont des caractères constants désignant Période, Temps et Heure. "hhh" représente l’heure de prévision [000, 003, 006, ..., 072]
* __grib2__ : Chaîne de caractères constante indiquant que le format est GRIB2

Exemple de nom de fichier : 20201007T00Z_MSC_REPS_TPRATE-Accum24h_SFC_RLatLon0.09x0.09_PT024H.grib2

Note: Les fichiers contiennent par défaut tous les membres d'ensembles. Les fichiers contenant les produits probabilistes sont identifiés via le paramètre '-prob' attaché à la variable (ex: 20201007T00Z_MSC_REPS_TPRATE-Accum24h-prob_SFC_RLatLon0.09x0.09_PT024H.grib2)

## Liste des variables

Les variables pour les produits d'ensemble disponibles dans les fichiers GRIB2 sont décrites ci-dessous. Des exemples sont indiqués pour la grille lat-lon tournée à 10km.

* __FPRATE__ : Pluie verglaçante accumulée sur une période. Ex: FPRATE-Accum24h 
* __HEATX__ : Humidex à 2m au-dessus du sol. Ex: HEATX_AGL-2m; HEATX-Max24h_AGL-2m (humidex maximum à 2m au-dessus du sol sur une période de 24h) 
* __IPRATE__ : Grésil (équivalent en eau) accumulé sur une période. Ex: IPRATE-Accum12h
* __RPRATE__ : Pluie accumulée sur une période. Ex: RPRATE-Accum6h 
* __SPRATE__ : Neige (équivalent en eau) accumulée sur une période. Ex: SPRATE-Accum24h 
* __TEMP__ / __TMP__ : Température à 2m au-dessus du sol. Ex: TMP_AGL-2m; TMP-Max24h_AGL-2m (température maximum à 2m au-dessus du sol sur une période de 24h)
* __TPRATE__ : Précipitations totales accumulées sur une période. Ex: TPRATE-Max48h
* __WCF__ : Facteur éolien à 2m au-dessus du sol. Ex: WCF_AGL-2m; WCF-Min24h_AGL-2m (facteur éolien minimum à 2m au-dessus du sol sur une période de 24h)
* __WIND__ : Vitesse du vent à 10m au-dessus du sol. Ex: WIND_AGL-10m; WIND-Max12h_AGL-10m (vitesse du vent maximum à 10m au-dessus du sol sur une période de 12h)

Les variables pour les membres individuels dans les fichiers GRIB2 sont décrites ci-dessous. Les variables sont disponibles de 0 à 72h chaque 3h. Des exemples sont indiqués pour la grille lat-lon tournée à 10km.

* __AFRAIN__ : Précipitations accumulées sous forme de pluie verglaçante 
* __ARAIN__ : Précipitations accumulées sous forme de pluie 
* __AICEP__ : Précipitations accumulées sous forme de grésil 
* __ASNOW__ : Précipitations accumulées sous forme de neige 
* __APCP0__ : Précipitations accumulées sous toutes les formes 
* __SNOD__ : Épaisseur de la neige au sol 
* __WEASD__ : Équivalent en eau de l'épaisseur de la neige au sol 
* __HGT__ : Hauteur géopotentielle à différents niveaux. Ex: HGT_ISBL-500, hauteur géopotentielle à 500hPa
* __RH__ : Humidité relative à différents niveaux. Ex: RH_ISBL-10, humidité relative à 10hPa; RH_AGL-2m, humidité relative à 2m au-dessus du sol
* __UGRD__ : Composante U du vent à différents niveaux. Ex: UGRD_ISBL-700, composante U du vent à 700hPa 
* __VGRD__ : Composante V du vent à différents niveaux. Ex: VGRD_ISBL-700, composante V du vent à 700hPa 
* __TMP__ : Température à différents niveaux. Ex: TMP_AGL-2m, température à 2m au-dessus du sol; TMP_ISBL-50, température à 50hPa
* __TCDC__ : Couverture nuageuse totale 
* __PRES__ : Pression à la surface 
* __MSL__ : Pression au niveau moyen de la mer 
* __TSOIL__ : Température du sol 10cm sous la surface. Ex: TSOIL_DBS-10cm 
* __VSOILM__ : Humidité volumétrique du sol 10cm sous la surface. Ex: VOISLM_DBS-10cm 
* __LHTFL__ : Flux net de chaleur latente à la surface 
* __SHTFL__ : Flux net de chaleur sensible à la surface 
* __ULWRF__ : Flux ascendant de radiation d'ondes longues au sommet nominal de l'atmosphère. Ex: ULWRF_NTAT
* __DLWRF__ : Flux descendant de radiation d'ondes longues à la surface 
* __DSWR__ : Flux descendant de radiation d'ondes courtes à la surface

Une [liste en format XML](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_reps/reps_element.xml) contenant l'information pour toutes les variables de la grille 15km, y compris les descriptions et les unités, en français et en anglais est disponible.

## À propos du masque No-Data sur la grille polaire stéréographique 

Un masque pour mieux représenter les zones où les données ne sont pas disponibles, appelées aussi "No-Data" a été ajouté dans notre procédure d’encodage GRIB2. Ce masque vise uniquement quelques points de grille non-valides (données non-disponibles), toujours les mêmes et qui se situent en périphérie du domaine. Notons que ces points masqués n’ont aucun effet négatif sur la qualité du produit.

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).
