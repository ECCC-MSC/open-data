[In English](readme_satellite_Himawari-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [Observations satellite](readme_satellite_fr.md) > Observations du satellite Himawari sur le Datamart du SMC

# Données et produits du satellite Himawari (JMA)

Cette page décrit des données et produits dérivés des [instruments satellitaires Himawari-8/9](https://www.jma.go.jp/jma/jma-eng/satellite/materials/Himawari89/himawari89_leaflet/201703_leaflet89.pdf) en format GeoTIFF disponibles sur le Datamart du SMC toutes les 10 minutes couvrant l'Asie, le Pacifique occidental et l'Australie ainsi qu'une portion partielle des régions américaines du Pacifique.

Ces produits sont dérivés d'images [RVB](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_satellite/what_is_an_rgb_fr.pdf) (rouge/vert/bleu), une technique de traitement satellitaire qui utilise une combinaison de bandes de capteurs satellitaires (également appelées canaux) et les applique chacune à un filtre rouge/vert/bleu (RVB). Il en résulte une image en fausses couleurs, c'est-à-dire une image qui ne correspond pas à ce que verrait l'œil humain, mais qui offre un contraste élevé entre les différents types de nuages et les caractéristiques de la surface. Le capteur embarqué à bord d'un satellite météorologique obtient deux types d'informations de base : les données de la lumière visible (lumière réfléchie) se reflétant sur les nuages et les différents types de surface, aussi appelée « réflectance », et les données infrarouges (radiation émise) qui sont des radiations à ondes longues et courtes émises par les nuages et les caractéristiques de surface. Les RVB sont spécialement conçus pour combiner ce type de données satellitaires, ce qui permet d'obtenir un produit final riche en informations.

Les autres produits résultent d’un rehaussement des données d’un canal pour une longueur d’onde unique, visant aussi à mettre en évidence des caractéristiques météorologiques de la surface ou des nuages observés, mais de manière plus simple puisque ne mettant en jeu qu’une seule longueur d’onde. Cette façon de faire plus ancienne est toujours utile parce que sa simplicité facilite dans certains cas l’interprétation de l’image.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le Protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier GeoTIFF.

Les produits de la série GOES-R se trouvent à l'adresse :

* [https://dd.meteo.gc.ca/today/satellite/himawari/{HH}/](https://dd.meteo.gc.ca/today/satellite/himawari/)

où :

* __HH__ : Heure en UTC de validité de l'image [00, 01, .., 23]

## Nomenclature des noms de fichiers 

Les noms de fichiers suivent la nomenclature ci-dessous:

`{YYYYMMDD}T{HHmm}Z_MSC_Himawari-North_{Product}_{resolution}.tif`

où :

* __YYYYMMDD__ : Année, mois et jour de validité de l'image
* __T__ : Délimiteur temporel selon les normes ISO8601
* __HHmm__ : Heure et minute en UTC du temps de validité de l'image [00, 01, 02, ...., 22, 23] 
* __Z__ : Fuseau horaire (heure UTC)
* __MSC__ : Chaîne de caractères constante pour Meteorological Service of Canada, la source des données
* __Himawari-North__ : Chaîne de caractères indiquant que les données sont dérivées à partir du satellite Himawari sur l'hémisphère nord
* __Product__ : Chaîne de caractères indiquant le type de produit satellitaire généré [Ash, Channel03, Channel13, Channel15, Dust, NaturalColor, SO2]. Voir la section sur le contenu des fichiers
* __resolution__ : Résolution horizontale des données [2km]
* __tif__ : Chaîne de caractères constante indiquant que le format est GeoTIFF 

Examples: 

* 20260713T0020Z_MSC_Himawari-North_Dust_2km.tif
* 20260713T0110Z_MSC_Himawari-North_Channel13_2km.tif

## Contenu des fichiers

Les données Himawari complètent les observations fournies par les satellites GOES en offrant :

* Une cadence d’observation équivalente: imagerie toutes les 10 minutes  
* Des caractéristiques spectrales et radiométriques comparables  
* Une extension géographique stratégique vers :  
    * L’ouest du Pacifique  
    * Les régions cycloniques de l’Asie et de l’Océanie  

Cette complémentarité permet d'assurer une meilleure continuité globale des observations géostationnaires. 

| Caractéristiques | Himawari | GOES | 
| ------ | ------ | ------ | 
| Opérateur | Agence météorologique du Japon (JMA) | Administration nationale des océans et de l'atmosphère (NOAA) |
| Position orbitale | 140°E (orbite géostationnaire) | 75°O (GOES-Est), 137°O (GOES-Ouest) |
| Couverture | Asie-Pacifique, Australie | Amérique du Nord, Amérique centrale, Atlantique |
| Fréquence d'observation | Toutes les 10 minutes | Toutes les 5 à 10 minutes (selon la position du satellite GOES)|
| Résolution | 0,5 km (visible), 2 km (infrarouge) | 0,5 km (visible), 2 km (infrarouge) |
| Instrument principal / Produits météorologiques | AHI (Advanced Himawari Imager) – 16 bandes spectrales (VIS, NIR, SWIR, MWIR, TIR). Fournit des produits de température de surface de la mer, de couverture nuageuse et de précipitations | ABI (Advanced Baseline Imager) – capacités similaires, avec des instruments supplémentaires (p. ex. GLM). Fournit des produits de température de surface de la mer, de couverture nuageuse, de précipitations et de vent |
| Date de mise en service | 2015 (Himawari-8), 2022 (Himawari-9) | 2017 (GOES-16), 2019 (GOES-17), 2023 (GOES-18), 2025 (GOES-19)  |

## Support

Pour toute question relative à ces données, merci de [nous contacter](https://weather.gc.ca/mainmenu/contact_us_f.html).

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).
