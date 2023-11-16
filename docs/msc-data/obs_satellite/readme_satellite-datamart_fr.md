[In English](readme_satellite-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [Observations satellite](readme_satellite_fr.md) > Observations satellite sur le Datamart du SMC

# Données et produits satellitaires

Cette page décrit des données et produits dérivés des instruments [satellitaires](readme_satellite_fr.md) GOES-Ouest et GOES-Est en format GeoTIFF disponibles sur le Datamart du SMC. 

Ces produits sont dérivés d'images [RVB](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_satellite/what_is_an_rgb_fr.pdf) (rouge/vert/bleu), une technique de traitement satellitaire qui utilise une combinaison de bandes de capteurs satellitaires (également appelées canaux) et les applique chacune à un filtre rouge/vert/bleu (RVB). Il en résulte une image en fausses couleurs, c'est-à-dire une image qui ne correspond pas à ce que verrait l'œil humain, mais qui offre un contraste élevé entre les différents types de nuages et les caractéristiques de la surface. Le capteur embarqué à bord d'un satellite météorologique obtient deux types d'informations de base : les données de la lumière visible (lumière réfléchie) se reflétant sur les nuages et les différents types de surface, aussi appelée « réflectance », et les données infrarouges (radiation émise) qui sont des radiations à ondes longues émises par les nuages et les caractéristiques de surface. Les RVB sont spécialement conçus pour combiner ce type de données satellitaires, ce qui permet d'obtenir un produit final riche en informations.

Quatre types de produits sont actuellement générés à partir des satellites GOES-Ouest et GOES-Est: ["NightIR"](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_satellite/night_ir_fr.pdf) et ["NightMicrophysics"](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_satellite/night_microphysics_fr.pdf), à 2km de résolution, sont générés 24h/24 avec des canaux infrarouges donc visibles la nuit comme le jour, et des produits ["NaturalColour"](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_satellite/natural_colour_fr.pdf)  et ["DayCloudConvection"](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_satellite/day_cloud_convection_fr.pdf), à 1km de résolution, qui combinent des canaux dans la lumière visible à des  canaux infrarouges; leur plus haute résolution rendent ces deux derniers produits plus populaires, mais ils ne sont pas disponibles durant la majeure partie de la nuit (entre 02UTC et 07UTC pour GOES-Est, et entre 06UTC et 11UTC pour GOES-Ouest) étant donnée l’absence de lumière réfléchie du soleil. D’autres produits RVB devraient s’ajouter graduellement dans le futur pour combler différents besoins. 

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le Protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier GeoTIFF.

Les produits de la série GOES-R se trouvent à l'adresse :

* [https://dd.meteo.gc.ca/satellite/goes/[west|east]/{HH}/](https://dd.meteo.gc.ca/satellite/goes/)

où :

* __HH__ : Heure en UTC de validité de l'image [00, 01, .., 23]

Un historique de 54 heures des données est conservé dans chaque répertoire.

## Nomenclature des noms de fichiers 

Les noms de fichiers suivent la nomenclature ci-dessous:

`{YYYYMMDD}T{HHmm}Z_MSC_{GOES-Sat}_{Product}_{resolution}.tif`

où :

* __YYYYMMDD__ : Année, mois et jour de validité de l'image
* __T__ : Délimiteur temporel selon les normes ISO8601
* __HHmm__ : Heure et minute en UTC du temps de validité de l'image [00, 01, 02, ...., 22, 23] 
* __Z__ : Fuseau horaire (heure UTC)
* __MSC__ : Chaîne de caractères constante pour Meteorological Service of Canada, la source des données
* __GOES-Sat__ : Chaîne de caractères indiquant que les données sont dérivées à partir des satellites GOES [GOES-East, GOES-West] 
* __Product__ : Chaîne de caractères indiquant le type de produit satellitaire généré [NaturalColor, DayVis, NighIR, NightMicrophysics]
* __resolution__ : Résolution horizontale des données [1km, 2km]
* __tif__ : Chaîne de caractères constante indiquant que le format est GeoTIFF 

Examples: 

* 20231109T0800Z_MSC_GOES-East_NaturalColor_1km.tif
* 20231109T0510Z_MSC_GOES-West_NightMicrophysics_2km.tif

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : [dps-client@ec.gc.ca](mailto:ec.dps-client.ec@canada.ca)

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).
