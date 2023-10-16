[In English](readme_hrdps-datamart-alpha_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [SHRPD](readme_hrdps_fr.md) > SHRPD expérimental sur DD-Alpha

# Données GRIB2 expérimentales à 1 km du Système à Haute Résolution de Prévision Déterministe (SHRPD) sur la fenêtre ouest

Au cours de l'été 2017, la Colombie-Britannique a connu de graves incendies de forêt.  Afin de fournir des informations météorologiques plus détaillées et de piloter les modèles de qualité de l'air, le domaine SHRPD 1 km ouest a été implémenté en **mode expérimental** le 31 juillet 2018. 

Ce système de prévision utilise le Modèle environnemental global multi-échelle (GEM). La résolution horizontale de la grille est d'environ 1 km et possède 62 niveaux verticaux avec pilotage par le toit. 

Le niveau de momentum le plus bas se situe à une altitude d'environ 40 m. Ce système est piloté par le domaine continental [SHRPD à 2.5 km](readme_hrdps_fr.md), qui fournit les conditions initiales, latérales et aux limites supérieures des champs atmosphériques.  Les conditions de surface initiales sont fournies par le Système canadien d'assimilation des données à la surface (CaLDAS) à 2.5 km qui est couplé au SHRPD à 2.5 km. Les champs hydrométéorologiques initiaux sont "recyclés" à partir de la prévision de 6 heures de l'intégration à 2.5 km du SHRPD. 

Depuis la mise en œuvre initiale du SHRPD 1 km ouest, le système fonctionne 2 fois par jour, initialisé à 00 et 12 UTC et est intégré pendant 48 heures. La couverture géographique du système est la plus grande partie de la Colombie-Britannique et de l'Ouest de l'Alberta. Les données sont disponibles à une résolution horizontale de 1 km sur 62 niveaux verticaux.

## Adresse des données 

Les données du site web d'essai de données DD-Alpha du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTP. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier GRIB2.

Les données sont accessibles à l'adresse suivante :

* [https://dd.alpha.meteo.gc.ca/model_hrdps/west/1km/grib2/{HH}/{hhh}/](https://dd.alpha.meteo.gc.ca/model_hrdps/west/1km/grib2)

où :

* __HH__ : Heure UTC du début de la passe du modèle [00, 12].
* __hhh__ : Heure de prévision [000, 001, 002, ..., 048] 

Un historique de 24 heures est conservé dans ce répertoire.

## Domaine disponible

### Spécification technique de la grille ouest

![Image de la grille du ouest 1 km du SHRPD](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_hrdps/grille_hrdps1km_west.png)

Valeurs données aux paramètres de la grille lat-lon tournée sur le domaine ouest.

| Paramètre | Valeur |
| ------ | ------ |
| ni | 1330 |
| nj | 1180 | 
| résolution à 60° N | 1.0 km |
| coordonnées du premier point de grille (rélatives à la grille utilisée) | 5°S  23°W |

__Note__ : Les [versions les plus récentes de wgrib2](https://www.cpc.ncep.noaa.gov/products/wesley/wgrib2/update_2.0.8.html) et [GDAL](https://gdal.org/) supportent ces grilles tournées.

## Nomenclature des noms de fichiers 

NOTE: TOUTES LES HEURES SONT EN UTC.

Les fichiers ont la nomenclature suivante :

CMC_hrdps_west_Variable_TypedeNiveau_Niveau_GrilleResolution_YYYYMMDDTHHZ_Phhh-mm.grib2

où :

* __CMC__ : Chaîne de caractères constante indiquant que le Centre météorologique canadien (CMC) émet les prévisions.
* __hrdps__ : Chaîne de caractères constante indiquant que les données proviennent du Système haute résolution de prévision déterministe.
* __west__ : Chaîne de caractères constante indiquant le domaine ouest.
* __Variable__ : Type de variable contenu dans le fichier (ex. : UGRD).
* __TypedeNiveau__ : Type de niveau.
* __Niveau__ : Valeur du niveau.
* __Grille__ : Grille horizontale [rotated_latlon] 
* __Resolution__ : 0.009x0.009. Signifie une résolution de 0.009°(environ 1km) dans les directions longitudinale et latitudinale
* __YYYYMMDD__ : Année, mois et jour du début de la prévision.
* __T__ : Délimiteur temporel selon les normes ISO8601
* __HH__ : Heure UTC de la passe [00, 06, 12, 18].
* __Z__ : Fuseau horaire (heure UTC)
* __Phhh__ : « P » est un caractère constant. « hhh » représente l’heure de prévision [000, 001, 002, ..., 035/036].
* __mm__ : « mm » représente les minutes de prévision [Codé en dur à 00 pour l’instant. Les pas de temps de 30 minutes seront disponibles éventuellement.].
* __grib2__ : Chaîne de caractères constante indiquant que le format est GRIB2.

Exemple de nom de fichier :

CMC_hrdps_west_DEPR_ISBL_0175_rotated_latlon0.009x0.009_20190825T12Z_P003-00.grib2

Le fichier a été créé par le CMC et contient une prévision du Système haute résolution de prévision déterministe expérimental sur le domaine ouest. Il contient les dépressions du point de rosée (DEPR), au niveau isobarique 175 mb (ISBL_0175), sur une grille lat-lon tournée à une résolution d'environ 1 km (rotated_latlon_0.009x0.009). Il débute le 25 août 2019 à 12Z (20190825T12Z). Il contient l’heure de prévision 03 (P003) et les minutes de prévision (00) en format GRIB2 (.grib2).

## Niveaux

La couverture verticale des champs tridimensionnels peut atteindre jusqu’à 28 niveaux isobariques.

Niveaux isobariques (hPa) : 1015, 1000, 0985, 0970, 0950, 0925, 0900, 0850, 0800, 0750, 0700, 0650, 0600, 0550, 0500, 0450, 0400, 0350, 0300, 0275, 0250, 0225, 0200, 0175, 0150, 0100, 0050.

Certains champs reçoivent une couverture verticale limitée à quatre niveaux isobariques.

Niveaux isobariques (couverture réduite, hPa) : 0850, 0700, 0500, 0250.

Autres types de niveaux qui pourraient être applicables à certains champs :

* Surface
* Hauteur fixe au-dessus du sol
* Profondeur fixe sous le sol
* Épaisseur entre niveaux isobariques
* Sommet théorique de l’atmosphère
* Colonne atmosphérique entière

## Liste des variables

Cette liste contient à la fois les paramètres générés à partir des sorties du SHRPD mais aussi les éléments du temps sur grille (*HRDPS-WEonG*) calculés en post-traitement qui seront bientôt disponibles.

<table id="csv-table" class="display"></table>

<link href="https://cdn.jsdelivr.net/npm/simple-datatables@latest/dist/style.css" rel="stylesheet" type="text/css">
<script src="https://cdn.jsdelivr.net/npm/simple-datatables@latest"></script>
<script src="../../../js/variables_datatable.js" type="text/javascript"></script>
<script>
  loadTable("csv-table", "../../../assets/csv/HRDPS_Variables-List_fr.csv");
</script>

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).




