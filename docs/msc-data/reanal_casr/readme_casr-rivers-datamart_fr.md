[In English](readme_casr-rivers-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [Réanalyse canadienne de surface](readme_casr_fr.md) > Produits dérivés de RCaS rivières sur le  Datamart du SMC

# Produits dérivés de la Réanalyse canadienne de surface - Rivières (RCaS-Rivières)

Cette page décrit des produits statistiques sur grille en format NetCDF dérivés de la composante rivières de la [Réanalyse canadienne de surface](https://hpfx.collab.science.gc.ca/~scar700/rcas-casr/overview_subproducts_fr.html) disponibles sur le Datamart du SMC. 

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le Protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier NetCDF.

Les produits statistiques sur grille, dérivés de la composante rivières de la Réanalyse canadienne de surface (RCaS-Rivières) se trouvent à l'adresse :

* [https://dd.meteo.gc.ca/today/reanalysis_casr/casr-rivers/{Version}/post-processing/grid](https://dd.meteo.gc.ca/today/reanalysis_casr/casr-rivers/)

où :

* __Version__ : [Version de CaSR](https://hpfx.collab.science.gc.ca/~scar700/rcas-casr/dataset_specifics_fr.html#diff_casr_versions) de la Réanalyse canadienne de surface (ex: v3.2)

## Nomenclature des noms de fichiers 

Les fichiers de prévisions suivent la nomenclature ci-dessous:

`{YYY1-YYY2}_MSC_CaSR-Rivers-{version}_{Var}_{Level}_{Grille}{resolution}_{TimeStep}.nc`

où :

* __YYY1-YYY2__ : Période couverte par la réanalyse selon la version [1968-2024]
* __MSC__ : Chaîne de caractères constante pour Meteorological Service of Canada, la source des données
* __CaSR-Rivers__ : Chaîne de caractères indiquant que les données sont dérivées de la composante rivières de la Réanalyse canadienne de surface (CaSR-Rivers en anglais)
* __version__ : [Version](https://hpfx.collab.science.gc.ca/~scar700/rcas-casr/dataset_specifics_fr.html#diff_casr_versions) de la réanalyse [v2.1, v3.2]
* __Var__ : Nom de la variable et statistique associée (voir la section ci-dessous)
* __Level__ : Chaîne de caractères indiquant le niveau vertical [`Sfc` pour la surface]
* __Grille__ : Grille horizontale lat-lon tournée [Rlatlon]
* __resolution__ : Résolution de 0.09°(environ 10km) dans les directions longitudinale et latitudinale [0.09]
* __TimeStep__ : Pas de temps, prenant l'une des valeurs [P1Y, P1M]; `P1Y` représente un pas de temps d'un an et `P1M` représente un pas de temps d'un mois
* __nc__ : Chaîne de caractères constante indiquant que le format est NetCDF

Exemples: 

* 1968-2024_MSC_CaSR-Rivers-v3.2_RiverDischarge-MMax_Sfc_RLatLon0.09_P1M.nc
* 1968-2024_MSC_CaSR-Rivers-v3.2_DeepReservoirStorage-YMin_Sfc_RLatLon0.09_P1Y.nc

## Liste des variables

* Débit de rivière, débit moyen sortant du canal de rivière pendant l'heure terminant à la date indiquée (m³/s)
* Eau retenue dans le canal de rivière (m³)
* Réservoir profond, épaisseur de la couche d'eau contenue dans le réservoir profond (kg/m²)

À chaque variable est associée une statistique, soit la moyenne annuelle/mensuelle (`YAvg/MAvg`), le minimum annuel/mensuel (`YMin/MMin`) ou le maximum annuel/mensuel(`YMax/MMax`)

Exemples:

* `RiverDischarge-YAvg`
* `DeepReservoirStorage-MMin`

## Support

Pour toute question relative à ces données, merci de [nous contacter](https://weather.gc.ca/mainmenu/contact_us_f.html).

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).
