[In English](readme_gdps-ice-anal-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [SGPD](readme_gdps_fr.md) > SGPD sur le Datamart du SMC

# Données NetCDF de l'analyse globale de glace 

Environnement et Changement climatique Canada fournit des champs d'analyse des glaces de mer à l'échelle mondiale produits par son [Système global de prévision déterministe (SGPD)](readme_gdps_fr.md) et interpolés sur une grille latitude-longitude tournée avec une résolution de 0.09 x 0.09 degré.
Les fichiers de données sont au format NetCDF (modèle classique NetCDF-4) et sont conformes aux conventions sur le climat et les prévisions.
 
Le système d'analyse global de la glace de mer est un système d'analyse basé sur une assimilation 3D-Var couvrant toutes les étendues d'eau (océans et lacs) à une résolution horizontale de 10km sur une grille YIN-YANG et utilisant une prévision de persistance de 6 heures pour l'état de base. Cette analyse assimile 4 fois par jour les données de télédétection par satellite et les cartes des glaces du [Service canadien des glaces](https://www.canada.ca/fr/environnement-changement-climatique/services/previsions-observations-glaces/conditions-glaces-plus-recentes.html). 

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier NetCDF.

Les données sont accessibles à adresse suivante :

[https://dd.meteo.gc.ca/model_gem_global/{RES}/{HH}](https://dd.meteo.gc.ca/model_gem_global/10km)

où :

* __RES__ : Résolution horizontale [10km]
* __HH__ : Heure UTC du début de la passe du modèle [00, 06, 12, 18]

Un historique de 7 jours est conservé dans ce répertoire.

## Spécification technique de la grille

Valeurs données aux différents paramètres de la grille latitude-longitude selon la résolution.

| Paramètre | Valeur |
| ------ | ------ |
| ni | 4000 |
| nj | 2000 | 
| résolution | 0.09° x 0.09° |

## Nomenclature des noms de fichiers 

NOTE: TOUTES LES HEURES SONT EN UTC.

Les fichiers ont la nomenclature suivante :

```
{YYYYMMDD}T{HH}Z_MSC_GDPS-Analysis_{VAR}_{LVLTYPE-LVL}_{Grille}{resolution}_PT{hhh}H.nc
```

où :

* __YYYYMMDD__ : Année, mois et jour du début de la prévision
* __T__ : Délimiteur temporel selon les normes ISO8601
* __HH__ : Heure UTC de la passe [00, 06, 12, 18]
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

<table id="csv-table" class="display"></table>

<link href="https://cdn.jsdelivr.net/npm/simple-datatables@latest/dist/style.css" rel="stylesheet" type="text/css">
<script src="https://cdn.jsdelivr.net/npm/simple-datatables@latest"></script>
<script src="../../../js/variables_datatable.js" type="text/javascript"></script>
<script>
  loadTable("csv-table", "../../../assets/csv/GDPS-Ice-Analysis_fr.csv");
</script>

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info.comm.collab.science.gc.ca/).

















