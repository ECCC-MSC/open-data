[In English](readme_wcps-atm-ocean-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [SPCE](readme_wcps_fr.md) > SPCE couplées océan-atmosphère sur le Datamart du SMC

# Données des prévisions couplées atmosphère-océan-glace de mer du Système de prévision du cycle de l’eau (SPCE) en format NetCDF 

SPCE-prévision couplée est la composante du Système de prévision du cycle de l'eau (SPCE) qui fournit les prévisions couplées atmosphère-océan-glace de mer, correspondant à une résolution d'environ 1km (0.008 x 0.008 degré), sur le domaine des Grand Lacs, de fleuve Saint-Laurent de du Golfe de Saint-Laurent. Elle est lancée quatre fois par jour à 00, 06, 12 et 18 UTC et produit des prévisions sur 84 heures, basé sur le modèle atmosphérique GEM, couplé au modèle océan-glace NEMO-CICE. Les produits de la SPCE-prévision couplée sont (1) GEM : températures de l'air en surface, vitesses du vent en surface et ruissellement en surface (2) NEMO-CICE : variété de variables  des lacs/océan et de la glace de mer, par exemple les niveaux et les températures des lacs. Ells sont conçues pour aider les prévisionnistes à émettre des bulletins et des avertissements dans les eaux envahies par la glace pour la navigation, l'alerte sur les niveaux d'eau, les interventions d'urgence, la recherche et le sauvetage, et la prévision de la glace de mer du CIS.

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

<table id="csv-table" class="display"></table>

<link href="https://cdn.jsdelivr.net/npm/simple-datatables@latest/dist/style.css" rel="stylesheet" type="text/css">
<script src="https://cdn.jsdelivr.net/npm/simple-datatables@latest"></script>
<script src="../../../js/variables_datatable.js" type="text/javascript"></script>
<script>
  loadTable("csv-table", "../../../assets/csv/WCPS_Variables-List_fr.csv");
</script>

Notes:

* La variable `sossheig` est générée par rapport à une géoide arbitraire sur l'océan et par rapport à IGLD85 sur les Grands Lacs laurentiens. Pour autant, les niveaux d’eau dans tous les Grands Lacs présentent des biais importants du fait de la construction même du SPCE qui ne bénéficie pas d’assimilation des niveaux d’eau et reste dépendant des précipitations sur lacs, des apports des rivières et des échanges interlacs pour son bilan hydrique. **Nous encourageons donc les usagers à utiliser la variable `sossheig` dans la région des Grands Lacs avec circonspection.**
* L'unité `PSU` (Practical Salinity Unit) est équivalente à g/kg ou pour mille (‰). Elle est basée sur les propriétés de la conductivité de l'eau de mer.
* Les variables `tairsurf`, `uwindsurf`, `vwindsurf` et `runoffsurf` (ruissellement de surface) sont issues de GEM-LAM et les autres variables sont issues de NEMO-CICE.

## Support

Pour toute question relative à ces données, merci de [nous contacter](https://weather.gc.ca/mainmenu/contact_us_f.html).

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).

