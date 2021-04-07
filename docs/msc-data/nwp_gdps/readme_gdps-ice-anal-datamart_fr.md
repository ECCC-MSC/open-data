[In English](readme_gdps-ice-anal-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [SGPD](readme_gdps_fr.md) > SGPD sur le Datamart du SMC

# Données NetCDF de l'analyse globale de glace 

Les champs du jeu de données GRIB2 du [Système global de prévision déterministe (SGPD)](readme_gdps_fr.md) sont disponibles sur une grille latitude-longitude à une résolution effective d’environ 15 km et 25 km.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier NetCDF.

Les données sont accessibles à adresse suivante :

[https://dd.meteo.gc.ca/model_gem_global/{RES}/netcdf/{HH}](https://dd.meteo.gc.ca/model_gem_global/10km/netcdf)

où :

* __RES__ : Résolution horizontale [10km]
* __HH__ : Heure UTC du début de la passe du modèle [00, 12]

Un historique de 20 heures est conservé dans ce répertoire.

## Spécification technique des grilles

Valeurs données aux différents paramètres de la grille latitude-longitude selon la résolution.

### Données à 10km de résolution

| Paramètre | Valeur |
| ------ | ------ |
| ni | 2400 |
| nj | 1201 | 
| résolution | 0.15° |
| coordonnées du premier point de grille | 90° S  180° W | 

## Nomenclature des noms de fichiers 

NOTE: TOUTES LES HEURES SONT EN UTC.

Les fichiers ont la nomenclature suivante :

```
{YYYYMMDD}T{HH}Z_MSC_GDPS-Analysis_{VAR}_{LVLTYPE-LVL}_{Grille}{resolution}_PT{hhh}H.nc
```

où :

* __YYYYMMDD__ : Année, mois et jour du début de la prévision
* __T__ : Délimiteur temporel selon les normes ISO8601
* __HH__ : Heure UTC de la passe [00, 12]
* __Z__ : Fuseau horaire (heure UTC)
* __MSC__ : Chaîne de caractères constante pour Meteorological Service of Canada, la source des données
* __GDPS-Analysis__ : Chaîne de caractères constante indiquant que les données proviennent de l'analyse de glace du Système global de prévision déterministe
* __VAR__ : Variables contenues dans le fichier [IICECONC]. Voir la section des variables ci-dessous
* __LVLTYPE-LVL__ : Niveau vertical et hauteur [SFC]
* __Grille__ : Grille horizontale [RLatLon]
* __resolution__ : 0.09. Signifie une résolution de 0.09°(environ 10km) dans les directions longitudinale et latitudinale
* __PT{hhh}H__ : Echéance temporelle selon la norme [ISO8601](https://en.wikipedia.org/wiki/ISO_8601). P, T et H sont des caractères constants désignant Période, Temps et Heure. "hhh" représente l’heure de prévision [000 pour l'analyse]
* __nc__ : Chaîne de caractères constante indiquant que le format est NetCDF

Exemple de nom de fichier : 20210111T00Z_MSC_GDPS-Analysis_IICECONC_SFC_RLatLon0.09x0.09_PT000H.nc

## Liste des variables

Cette table indique le nom de la variable, le niveau, l'abbréviation et l'unité du paramètre encodé en format NetCDF.

| Abbréviation | Description courte       |  Niveau |	Unité  |
|--------------|--------------------------|---------|----------|
|  iiceconc    | fraction de glace de mer | surface |    1     |

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).

















