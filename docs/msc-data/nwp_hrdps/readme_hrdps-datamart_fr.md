[In English](readme_hrdps-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [SHRPD](readme_hrdps_fr.md) > SHRPD sur le Datamart du SMC

# Données GRIB2 du Système à Haute Résolution de Prévision Déterministe (SHRPD)

Le [Système à haute résolution de prévision déterministe (SHRPD)](readme_hrdps_fr.md) opérationnel est une série de grilles emboitées pour les prévisions à aire limitée (LAM). La grille principale a une résolution horizontale de 2.5 km sur une région pancanadienne. Le modèle pilote du SHRPD est une composante du [Système global de prévision déterministe (SGPD)](../nwp_gdps/readme_gdps_fr.md) à 10km de résolution horizontale. Les champs du jeu de données GRIB2 du SHRPD sont disponibles quatre fois par jour. Des prévisions de 48 heures sont produites pour le domaine pancanadien.

Les utilisateurs qui tireront le plus avantage des données sont ceux qui ont besoin de prévisions plus détaillées sur la température et sur les vents à la surface pour la journée même. Les prévisions à 2.5 km sont grandement utiles lors des changements de saisons et en hiver lorsque des changements rapides de température et de vents provoquent des changements de phase des précipitations (neige à pluie verglaçante à pluie, par exemple). Elles sont aussi utiles pour les prévisions à court terme aux endroits avec des reliefs accidentés et le long des rivages, car l’influence des changements d’altitude, de topographie ou de nature du terrain sera mieux décrite pour les phénomènes à cette échelle (brises de lacs ou de mer, circulation locale dans des vallées, changements de phase, etc.). Même en terrain moins accidenté ou loin de l’eau du rivage, la justesse de ces prévisions pourrait s’avérer utile à long terme. Le SHRPD devrait également être pris en compte pour des prévisions hydrologiques sur de plus petits bassins.

Dans le cadre d’un plan de modernisation du Service Météorologique Canadien (SMC), des [éléments du temps sur grille](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_weong-hrdps_f.pdf) ("WEonG") cohérents, fusionnant les sorties brutes du modèle et post-traitées à l’aide de diverses approches diagnostiques sont également disponibles pour servir les différents programmes de prévision (public, maritime, aviation, qualité de l’air, etc.). Des concepts horaires sont ainsi produits à partir de différents algorithmes en utilisant des sorties provenant du SHRPD sur le domaine pancanadien. Ces données sont disponibles sur une grille lat-lon tournée. 

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier GRIB2.

Les données sont accessibles aux adresses suivantes :

* [https://dd.meteo.gc.ca/model_hrdps/continental/{res}/{HH}/{hhh}/](https://dd.meteo.gc.ca/model_hrdps/continental/2.5km)

où :

* __res__ : Résolution horizontale [2.5km]
* __HH__ : Heure UTC du début de la passe du modèle [00, 06, 12, 18]
* __hhh__ : Heure de prévision [000, 001, 002, ..., 048]

Note: Certains algorithmes des éléments du temps sur grille ("WEonG") ont besoin des valeurs des variables à `t-1`, afin d'uniformiser l'offre de données, les heures de prévision débutent à 001h.

## Spécification technique de la grille

Valeurs données aux paramètres de la grille lat-lon tournée à haute résolution.

| Paramètre | Valeur |
| ------ | ------ |
| ni | 2540 |
| nj | 1290 | 
| résolution à 60° N | 2.5 km |
| coordonnées du premier point de grille | 39°N 134°W |

__Note__ : Les [versions les plus récentes de wgrib2](https://www.cpc.ncep.noaa.gov/products/wesley/wgrib2/update_2.0.8.html) et [GDAL](https://gdal.org/) supportent ces grilles tournées. 

## Nomenclature des noms de fichiers

Les fichiers ont la nomenclature suivante :

* `{YYYYMMDD}T{HH}Z_MSC_HRDPS_{VAR}_{LVLTYPE-LVL}_{Grille}{resolution}_PT{hhh}H.grib2`
* `{YYYYMMDD}T{HH}Z_MSC_HRDPS-WEonG_{VAR}_{LVLTYPE-LVL}_{Grille}{resolution}_PT{hhh}H.grib2`

où :

* __YYYYMMDD__ : Année, mois et jour du début de la prévision
* __T__ : Délimiteur temporel selon les normes ISO8601
* __HH__ : Heure UTC de la passe [00, 06, 12, 18]
* __Z__ : Fuseau horaire (heure UTC)
* __MSC__ : Chaîne de caractères constante pour Meteorological Service of Canada, la source des données
* __HRDPS__ : Chaîne de caractères constante indiquant que les données proviennent du Système haute résolution de prévision déterministe
* __HRDPS-WEonG__ : Chaîne de caractères constante indiquant que les données proviennent des éléments du temps sur grille ("WEonG") du Système haute résolution de prévision déterministe
* __VAR__ : Type de variable contenu dans le fichier (ex: UGRD).
* __LVLTYPE-LVL__ : Niveau vertical et hauteur [ex: Sfc pour la surface, EATM pour l’intégrale de la colonne, DBS-10-20cm couche entre 10 et 20cm sous la surface, AGL-10m pour la hauteur de 10m au-dessus du sol]
* __Grille__ : Grille horizontale [RLatLon]
* __resolution__ : 0.0225. Signifie une résolution de 0.0225°(environ 2.5km) dans les directions longitudinale et latitudinale
* __PT{hhh}H__ : Echéance temporelle selon la norme [ISO8601](https://en.wikipedia.org/wiki/ISO_8601). P, T et H sont des caractères constants désignant Période, Temps et Heure. "hhh" représente l’heure de prévision [000, 001, 002, ..., 048]
* __grib2__ : Chaîne de caractères constante indiquant que le format est GRIB2.

Exemples de noms de fichier :

* 20201123T00Z_MSC_HRDPS_GUST_AGL-10m_RLatLon0.0225_PT012H.grib2
* 20220821T12Z_MSC_HRDPS-WEonG_VISIFG_Sfc_RLatLon0.0225_PT024H.grib2

## Niveaux

La couverture verticale des champs tridimensionnels peut atteindre jusqu’à 31 niveaux isobariques.

Niveaux isobariques (hPa) : 1015, 1000, 985, 970, 950, 925, 900, 850, 800, 750, 700, 650, 600, 550, 500, 450, 400, 350, 300, 275, 250, 225, 200, 175, 150, 100, 50.

Niveaux additionnels 30, 20 et 10 hPa pour les variables TMP, HGT, UGRD, VGRD, WIND, WDIR, SPFH, RH et DEPR

Certains champs reçoivent une couverture verticale limitée à quatre niveaux isobariques.

Niveaux isobariques (couverture réduite, hPa) : 850, 700, 500, 250.

Autres types de niveaux qui pourraient être applicables à certains champs :

* Surface
* Hauteur fixe au-dessus du sol
* Profondeur fixe sous le sol
* Épaisseur entre niveaux isobariques
* Sommet théorique de l’atmosphère
* Colonne atmosphérique entière

## Liste des variables

Cette liste contient à la fois les paramètres générés à partir des sorties du SHRPD mais aussi les éléments du temps sur grille (*HRDPS-WEonG*) calculés en post-traitement.

<table id="csv-table" class="display"></table>

<link href="https://cdn.jsdelivr.net/npm/simple-datatables@latest/dist/style.css" rel="stylesheet" type="text/css">
<script src="https://cdn.jsdelivr.net/npm/simple-datatables@latest"></script>
<script src="../../../js/variables_datatable.js" type="text/javascript"></script>
<script>
  loadTable("csv-table", "../../../assets/csv/HRDPS_Variables-List_fr.csv");
</script>

Note:

* Les maximums d'indice UV sont les maximums journaliers basés sur l'heure courante et les 23 heures précédentes (s'applique aussi à l'indice UV par temps clair). Ils sont disponibles aux échéances suivantes selon les passes du système:
    * Passe de 00Z: 18h et 42h
    * Passe de 06Z: 12h et 36h
    * Passe de 12Z: 6h et 30h
    * Passe de 18Z: 0h et 24h

## Support

Pour toute question relative à ces données, merci de [communiquer avec nous](https://meteo.gc.ca/mainmenu/contact_us_f.html).

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).




