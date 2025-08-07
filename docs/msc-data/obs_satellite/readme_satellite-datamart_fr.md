[In English](readme_satellite-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [Observations satellite](readme_satellite_fr.md) > Observations satellite sur le Datamart du SMC

# Données et produits satellitaires

Cette page décrit des données et produits dérivés des instruments [satellitaires](readme_satellite_fr.md) GOES-Ouest et GOES-Est en format GeoTIFF disponibles sur le Datamart du SMC. 

Ces produits sont dérivés d'images [RVB](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_satellite/what_is_an_rgb_fr.pdf) (rouge/vert/bleu), une technique de traitement satellitaire qui utilise une combinaison de bandes de capteurs satellitaires (également appelées canaux) et les applique chacune à un filtre rouge/vert/bleu (RVB). Il en résulte une image en fausses couleurs, c'est-à-dire une image qui ne correspond pas à ce que verrait l'œil humain, mais qui offre un contraste élevé entre les différents types de nuages et les caractéristiques de la surface. Le capteur embarqué à bord d'un satellite météorologique obtient deux types d'informations de base : les données de la lumière visible (lumière réfléchie) se reflétant sur les nuages et les différents types de surface, aussi appelée « réflectance », et les données infrarouges (radiation émise) qui sont des radiations à ondes longues et courtes émises par les nuages et les caractéristiques de surface. Les RVB sont spécialement conçus pour combiner ce type de données satellitaires, ce qui permet d'obtenir un produit final riche en informations.

Les autres produits résultent d’un rehaussement des données d’un canal pour une longueur d’onde unique, visant aussi à mettre en évidence des caractéristiques météorologiques de la surface ou des nuages observés, mais de manière plus simple puisque ne mettant en jeu qu’une seule longueur d’onde. Cette façon de faire plus ancienne est toujours utile parce que sa simplicité facilite dans certains cas l’interprétation de l’image.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le Protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier GeoTIFF.

Les produits de la série GOES-R se trouvent à l'adresse :

* [https://dd.meteo.gc.ca/today/satellite/goes/[west|east]/{HH}/](https://dd.meteo.gc.ca/today/satellite/goes/)

où :

* __HH__ : Heure en UTC de validité de l'image [00, 01, .., 23]

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
* __Product__ : Chaîne de caractères indiquant le type de produit satellitaire généré [Ash, FireTemperature, etc.]. Voir la section sur le contenu des fichiers
* __resolution__ : Résolution horizontale des données [1km, 2km]
* __tif__ : Chaîne de caractères constante indiquant que le format est GeoTIFF 

Examples: 

* 20231109T0800Z_MSC_GOES-East_NaturalColor_1km.tif
* 20231109T0510Z_MSC_GOES-West_SnowFog-NightMicrophysics_1km.tif

## Contenu des fichiers

Il est important de noter que les produits utilisant les canaux de lumière visible ne peuvent être générés durant les heures de la nuit où aucune portion du disque terrestre vu par le satellite n’est éclairée directement par le soleil. Ces produits ont une résolution nominale de 1km. Leur plus haute résolution rendent ces derniers produits plus populaires, mais lorsque générés individuellement ils ne sont pas disponibles durant la majeure partie de la nuit (entre 02UTC et 07UTC pour GOES-Est, et entre 06UTC et 11UTC pour GOES-Ouest). Par contre les produits n’utilisant que des canaux infrarouges sont générés de jour comme de nuit et donc disponibles 24h/24 à une résolution nominale de 2km.
 
En combinant des produits n’utilisant que le rayonnement infrarouge avec des produits utilisant la lumière réfléchie du soleil on obtient des produits combinés générés 24h/24 où la partie éclairée de jour utilise des canaux de lumière visible, et la partie nocturne utilise que des canaux de rayonnement infrarouge.
 
Quinze types de produits sont actuellement générés à partir des satellites GOES-Ouest et GOES-Est. Ils sont décrits ci-dessous en détails selon le type de produits individuels et/ou combinés "jour-nuit" (voir les liens dans les tableaux et la liste des combinaisons disponibles): 

### Produits individuels : 

| Produits individuels | Résolution | Application | Note | 
| ------ | ------ | ------ | ------ | 
| [Couleur naturelle](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_satellite/natural_colour_fr.pdf) | 1km | Applications variées (ex: aspect naturel des surfaces, suivi de la fumée de feux de forêts, saison chaude) | Disponible seulement le jour | 
| [Cendre](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_satellite/ash_fr.pdf) | 2km | Détection des cendres volcaniques | Disponible 24h/24 avec des canaux infrarouges donc visibles la nuit comme le jour | 
| [SO2](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_satellite/so2_fr.pdf) | 2km | Détection du dioxyde de soufre, un gaz volcanique qui peut poser une menace à l'environnement et la santé humaine à des concentrations élevées | Disponible 24h/24 avec des canaux infrarouges donc visible la nuit comme le jour | 
| [Poussière](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_satellite/dust_fr.pdf) | 2km | Détection des nuages de poussière et des fronts d’humidité | Disponible 24h/24 avec des canaux infrarouges donc visible la nuit comme le jour |

### Produits individuels ou combinés «jour-nuit» :

| Produits individuels ou combinés «jour-nuit» | Résolution | Application | Note | 
| ------ | ------ | ------ | ------ | 
| [Convection nuageuse de jour](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_satellite/day_cloud_convection_fr.pdf) | 1km | Création d’un contraste entre les nuages hauts et bas, détection des nuages convectifs causant les orages | Disponible que le jour si pris isolément ou en combinaison «jour-nuit» avec d’autres produits | 
| [IR de nuit](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_satellite/night_ir_fr.pdf) | 2km | Surveillance nocturne des nuages, aspect similaire au RVB « Convection nuageuse de jour »  | Disponible 24h/24 ou en combinaison «jour-nuit» avec d’autres produits, avec des canaux infrarouges donc visible la nuit comme le jour | 
| [Microphysique de nuit](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_satellite/night_microphysics_fr.pdf) | 2km | Analyse contrastée entre les nuages hauts et bas, et le brouillard. Permet d'identifier les points chauds des incendies  | Disponible 24h/24 ou en combinaison «jour-nuit» avec d’autres produits, avec des canaux infrarouges donc visible la nuit comme le jour | 

### Produits combinés «jour-nuit» : 

| Produits combinés «jour-nuit» | Résolution | Application | Note | 
| ------ | ------ | ------ | ------ | 
| [Température des feux](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_satellite/firetemperature_fr.pdf) | 1km | Détection des feux de forêts | Utilise la lumière visible et n’apparait que dans la portion jour d’une combinaison | 
| [Type de nuage de jour](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_satellite/daycloudtype_fr.pdf) | 1km | Distinction des nuages élevés des nuages bas, permet de révéler le stade de développement vertical des nuages convectifs  | Utilise la lumière visible et n’apparait que dans la portion jour d’une combinaison | 
| [Détection des feux de jour](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_satellite/daylandcloudfire_fr.pdf) | 1km | Détection de points chauds d'incendie, de la fumée, des cicatrices de brûlures  | Utilise la lumière visible et n’apparait que dans la portion jour d’une combinaison | 
| [Neige-brouillard](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_satellite/snowfog_fr.pdf) | 1km | Distinction de  la neige au sol, du brouillard et des nuages bas | Utilise la lumière visible et n’apparait que dans la portion jour d’une combinaison | 
| [Sandwich Visible et IR](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_satellite/visibleirsandwich_fr.pdf) | 1km | Surveillance de la convection profonde, des caractéristiques du sommet des nuages convectifs matures qui causent du temps violent  | Utilise la lumière visible et n’apparait que dans la portion jour d’une combinaison | 
| [Fumée Bande 1 ABI](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_satellite/smokeabiband1_fr.pdf) | 1km | Détection de fumée, tempêtes de poussière | Utilise la lumière visible et n’apparait que dans la portion jour d’une combinaison | 
| [SWIR](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_satellite/swir_fr.pdf) | 2km | Surveillance des points chauds des incendies de forêt | N'apparait que dans la portion nuit d’une combinaison de produits | 
| [Microphysique de nuit et IR](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_satellite/nightmicrophysicsir_fr.pdf) | 2km | Surveillance des tempêtes convectives nocturnes  | N'apparait que dans la portion nuit d’une combinaison de produits |

Voici la liste des combinaisons «jour-nuit» disponibles:

* Convection nuageuse de jour (ou Visibilité de jour) / IR de nuit
* Type de nuage de jour / Microphysique de nuit 
* Neige-brouillard / Microphysique de nuit
* Sandwich Visible et IR / Microphysique de nuit et IR
* Fumée Bande 1 ABI / SWIR
* Température des feux / SWIR
* Détection des feux de jour /SWIR

D’autres produits RVB s’ajouteront graduellement dans le futur pour servir une plus grande diversité de besoins.

## Support

Pour toute question relative à ces données, merci de [nous contacter](https://weather.gc.ca/mainmenu/contact_us_f.html).

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).
