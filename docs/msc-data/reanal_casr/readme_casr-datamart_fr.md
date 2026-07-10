[In English](readme_casr-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [Réanalyse canadienne de surface](readme_casr_fr.md) > Produits dérivés de RCaS sur le Datamart du SMC

# Produits dérivés de la Réanalyse canadienne de surface

Cette page décrit des produits statistiques sur grille en format NetCDF ainsi que les produits statistiques agrégés par bassin versant hydrologiqueen format GeoJSON, dérivés de la Réanalyse canadienne de surface (RCaS) disponibles sur le Datamart du SMC.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le Protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier NetCDF ou GeoJON selon le produit.

Les produits statistiques sur grille, dérivés de la Réanalyse canadienne de surface (RCaS) se trouvent à l'adresse :

* [https://dd.meteo.gc.ca/today/reanalysis_casr/casr/{Version}/post-processing/grid](https://dd.meteo.gc.ca/today/reanalysis_casr/casr/)

Les produits statistiques agrégés par bassin versant hydrologique, dérivés de la Réanalyse canadienne de surface (RCaS) se trouvent à l'adresse :

* [https://dd.meteo.gc.ca/today/reanalysis_casr/casr/{Version}/post-processing/watersheds/{polygon_dataset}/area{nb}](https://dd.meteo.gc.ca/today/reanalysis_casr/casr/)

où :

* __Version__ : [Version de CaSR](https://hpfx.collab.science.gc.ca/~scar700/rcas-casr/dataset_specifics_fr.html#diff_casr_versions de la Réanalyse canadienne de surface) (ex: v3.2)
* __polygon_dataset__ : Nom du jeu de polygones de bassins versants (`nhn` pour National Hydrographic Network, `nhs` pour National hydrometric basin polygon)
* __nb__ : Principaux bassins de drainage selon:
    * 01 : Provinces maritimes 
    * 02 : Saint-Laurent 
    * 03 : Nord du Québec et du Labrador 
    * 04 : Sud-ouest de la baie d’Hudson 
    * 05 : Fleuve Nelson 
    * 06 : Ouest et nord de la baie d’Hudson 
    * 07 : Grand lac des Esclaves 
    * 08 : Pacifique 
    * 09 : Fleuve Yukon 
    * 10 : Arctique 
    * 11 : Fleuve Mississippi

## Nomenclature des noms de fichiers 

Les noms de fichiers suivent la nomenclature ci-dessous:

* __Produits sur grille en format NetCDF__

Les noms de fichiers de prévisions suivent la nomenclature ci-dessous:

`{YYY1-YYY2}_MSC_CaSR-{version}_{Var}_Sfc_{Grille}{resolution}_{TimeStep}.nc`

Les noms de fichiers d'analyses suivent la nomenclature ci-dessous:

`{YYY1-YYY2}_MSC_CaSR-{version}-Analysis_{Var}_Sfc_{Grille}{resolution}_{TimeStep}.nc`

où :

* __YYY1-YYY2__ : Période couverte par la réanalyse selon la version [1980-2024]
* __MSC__ : Chaîne de caractères constante pour Meteorological Service of Canada, la source des données
* __CaSR__ : Chaîne de caractères indiquant que les données sont dérivées de la Réanalyse canadienne de surface (CaSR en anglais)
* __version__ : [Version](https://hpfx.collab.science.gc.ca/~scar700/rcas-casr/dataset_specifics_fr.html#diff_casr_versions) de la réanalyse [v3.2]
* __Analysis__ : Chaîne de caractères indiquant que les données sont des analyses et non des prévisions
* __Var__ : Nom de la variable
* __Sfc__ : Chaîne de caractères indiquant que le niveau vertical est la surface
* __Grille__ : Grille horizontale lat-lon tournée [Rlatlon]
* __resolution__ : Résolution de 0.09°(environ 10km) dans les directions longitudinale et latitudinale [0.09]
* __TimeStep__ : Pas de temps, prenant l'une des valeurs [P1Y, P1M] ; P1Y représente un pas de temps d'un an et P1M représente un pas de temps d'un mois.
* __nc__ : Chaîne de caractères constante indiquant que le format est NetCDF

Exemples: 

* 1980-2024_MSC_CaSR-v3.2_Precip-Accum12h-MMin_Sfc_RLatLon0.09_P1M.nc
* 1980-2024_MSC_CaSR-v3.2-Analysis_DewPoint-YAvg_AGL-1.5m_RLatLon0.09_P1Y.nc

* __Produits agrégés par bassin versant hydrologique en format GeoJSON__

`{YYY1-YYY2}_MSC_CaSR-{version}_DrainageArea{nb}_{Var}_Sfc_{TimeStep}.json`

où :

* __YYY1-YYY2__ : Période couverte par la réanalyse selon la version [1980-2024]
* __MSC__ : Chaîne de caractères constante pour Meteorological Service of Canada, la source des données
* __CaSR__ : Chaîne de caractères indiquant que les données sont dérivées de la Réanalyse canadienne de surface (CaSR en anglais)
* __version__ : [Version](https://hpfx.collab.science.gc.ca/~scar700/rcas-casr/dataset_specifics_fr.html#diff_casr_versions) de la réanalyse [v3.2]
* __DrainageArea__ : Chaîne de caractères constante pour spécifier le bassin versant  
* __nb__ : Numéro du bassin de drainage [01, 02, .., 11]
* __Var__ : Nom de la variable
* __Sfc__ : Chaîne de caractères indiquant que le niveau vertical est la surface
* __TimeStep__ : Pas de temps, prenant l'une des valeurs [P1Y, P1M] ; P1Y représente un pas de temps d'un an et P1M représente un pas de temps d'un mois.
* __json__ : Chaîne de caractères constante indiquant que le format est GeoJSON

Exemples:

* 1980-2024_MSC_CaSR-v3.2-Analysis_DrainageArea02_Precip-Accum1h-MMin_Sfc_P1M.json
* 1980-2024_MSC_CaSR-v3.2_DrainageArea11_SnowDepth-YMax_Sfc_P1Y.json

## Liste des variables

* Accumulation des flux à réponse rapide, ruissellement (kg/m²)
* Quantité de précipitations (m)
* Accumulation du drainage soit l'écoulement vertical à la base de la couche de sol la plus profonde considérée pour le routage (kg/m²)
* Profondeur de neige, agrégée (cm) 
* Equivalent en eau de la couverture neigeuse, agrégée (kg/m²)
* Contenu volumique d'eau liquide dans le sol (m³/m³) 
* Température de l'air (°C)
* Température du point de rosée (°C)

## Support

Pour toute question relative à ces données, merci de [nous contacter](https://weather.gc.ca/mainmenu/contact_us_f.html).

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).
