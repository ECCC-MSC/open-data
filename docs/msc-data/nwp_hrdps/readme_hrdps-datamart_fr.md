[In English](readme_hrdps-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [SHRPD](readme_hrdps_fr.md) > SHRPD sur le Datamart du SMC

# Données GRIB2 du Système à Haute Résolution de Prévision Déterministe (SHRPD)

Le [Système à haute résolution de prévision déterministe ou SHRPD](readme_hrdps_fr.md) est une série de grilles emboitées pour les prévisions à aire limitée (LAM). Les grilles proviennent du SRPD et ont une résolution horizontale de 2.5 km à l’intérieur du domaine, sur une région principale Pancanadienne et sur une région Nord couvrant l'archipel arctique et le Groenland. Le modèle pilote du SHRPD est le Système régional de prévision déterministe ou SRPD. Le SHRPD est opérationnel pour tous les domaines sauf le domaine Nord qui demeure expérimental. Les champs du jeu de données GRIB2 du SHRPD sont disponibles quatre fois par jour (sauf pour le domaine Nord). Des prévisions de 48 heures sont produites pour le domaine Pancanadien.

Les utilisateurs qui tireront le plus avantage des données sont ceux qui ont besoin de prévisions plus détaillées sur la température et sur les vents à la surface pour la journée même. Les prévisions à 2.5 km sont grandement utiles lors des changements de saisons et en hiver lorsque des changements rapides de température et de vents provoquent des changements de phase des précipitations (neige à pluie verglaçante à pluie, par exemple). Elles sont aussi utiles pour les prévisions à court terme aux endroits avec des reliefs accidentés et le long des rivages, car l’influence des changements d’altitude, de topographie ou de nature du terrain sera mieux décrite pour les phénomènes à cette échelle (brises de lacs ou de mer, circulation locale dans des vallées, changements de phase, etc.). Même en terrain moins accidenté ou loin de l’eau du rivage, la justesse de ces prévisions pourrait s’avérer utile à long terme. Le SHRPD devrait également être pris en compte pour des prévisions hydrologiques sur de plus petits bassins.

Dans le cadre d’un plan de modernisation du Service Météorologique Canadien (SMC), des [éléments du temps sur grille](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_weong-hrdps_f.pdf) ("WEonG") cohérents, fusionnant les sorties brutes du modèle et post-traitées à l’aide de diverses approches diagnostiques sont également disponibles pour servir les différents programmes de prévision (public, maritime, aviation, qualité de l’air, etc.). Ces données sont disponibles sur une grille lat-lon tournée.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier GRIB2.

Les données sont accessibles aux adresses suivantes :

* Grilles polaires stéréographiques : [https://dd.meteo.gc.ca/model_hrdps/{domain}/grib2/{HH}/{hhh}/](https://dd.meteo.gc.ca/model_hrdps)
* Grille lat-lon tournée : [https://dd.meteo.gc.ca/model_hrdps/continental/{res}/grib2/{HH}/{hhh}/](https://dd.meteo.gc.ca/model_hrdps/continental/2.5km/grib2)

où :

* __domain__ : Chaîne de caractères indiquant le domaine représenté [continental, north, east, prairies, west, maritimes]
* __res__ : Résolution horizontale [2.5km]
* __HH__ : Heure UTC du début de la passe du modèle [00, 06, 12, 18], pour tous les domaines sauf le domaine Nord [00, 12]
* __hhh__ : Heure de prévision [000, 001, 002, ..., 048]

Un historique de 24 heures est conservé dans ce répertoire.

## Domaines disponibles

### Spécification technique des grilles continentales

* __Grille polaire stéréographique__

![Image de la grille du domaine continental du SHRPD](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_hrdps/grille_hrdps_cont.png)

Valeurs données aux paramètres de la grille polaire stéréographique à haute résolution.

| Paramètre | Valeur |
| ------ | ------ |
| ni | 2576 |
| nj | 1456 | 
| résolution à 60° N | 2.5 km |
| coordonnées du premier point de grille | 35.6073° N  128.0813° W |
| coordonnées (i; j) du Pôle Nord | (840.0, 2296.0) |
| orientation de la grille (par rapport à l’axe des j) | -108.0° |

* __Grille lat-lon tournée__

![Image de la grille du domaine continental lat-lon tournée du SHRPD](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_hrdps/grille_hrdps_Rlatlon.png)

Valeurs données aux paramètres de la grille lat-lon tournée à haute résolution.

| Paramètre | Valeur |
| ------ | ------ |
| ni | 2540 |
| nj | 1290 | 
| résolution à 60° N | 2.5 km |
| coordonnées du premier point de grille | 12°S 15°W |

__Note__ : Les [versions les plus récentes de wgrib2](https://www.cpc.ncep.noaa.gov/products/wesley/wgrib2/update_2.0.8.html) et [GDAL](https://gdal.org/) supportent ces grilles tournées. 

### Spécification technique de la grille nord (expérimental)

![Image de la grille du domaine nord du SHRPD](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_hrdps/grille_hrdps_north.png)

Valeurs données aux paramètres de la grille polaire stéréographique à haute résolution.

| Paramètre | Valeur |
| ------ | ------ |
| ni | 1465 |
| nj | 825 | 
| résolution à 60° N | 2.5 km |
| coordonnées du premier point de grille | 67.9601° N  140.7611° W |
| coordonnées (i; j) du Pôle Nord | (389.0, 842.0) |
| orientation de la grille (par rapport à l’axe des j) | -116.0° |

### Spécification technique de la grille est

![Image de la grille du domaine est du SHRPD](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_hrdps/grille_hrdps_east.png)

Valeurs données aux paramètres de la grille polaire stéréographique à haute résolution.

| Paramètre | Valeur |
| ------ | ------ |
| ni | 765 |
| nj | 570 | 
| résolution à 60° N | 2.5 km |
| coordonnées du premier point de grille | 38.6985° N  91.3395° W |
| coordonnées (i; j) du Pôle Nord | (450.0, 2240.0) |
| orientation de la grille (par rapport à l’axe des j) | -80.0° |


### Spécification technique de la grille prairies

![Image de la grille du domaine Prairies du SHRPD](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_hrdps/grille_hrdps_prairies.png)

Valeurs données aux paramètres de la grille polaire stéréographique à haute résolution.

| Paramètre | Valeur |
| ------ | ------ |
| ni | 655 |
| nj | 570 | 
| résolution à 60° N | 2.5 km |
| coordonnées du premier point de grille | 41.8344° N  108.4943° W |
| coordonnées (i; j) du Pôle Nord | (1015.0, 1869.0) |
| orientation de la grille (par rapport à l’axe des j) | -80.0° |

### Spécification technique de la grille ouest

![Image de la grille du domaine ouest du SHRPD](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_hrdps/grille_hrdps_west.png)

Valeurs données aux paramètres de la grille polaire stéréographique à haute résolution.

| Paramètre | Valeur |
| ------ | ------ |
| ni | 685 |
| nj | 485 | 
| résolution à 60° N | 2.5 km |
| coordonnées du premier point de grille | 44.6922° N  129.9011° W |
| coordonnées (i; j) du Pôle Nord | (578.0, 1900.0) |
| orientation de la grille (par rapport à l’axe des j) | -113.0° |


### Spécification technique de la grille maritimes

![Image de la grille du domaine Maritimes du SHRPD](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_hrdps/grille_hrdps_marit.png)

Valeurs données aux paramètres de la grille polaire stéréographique à haute résolution.

| Paramètre | Valeur |
| ------ | ------ |
| ni | 595 |
| nj | 451 | 
| résolution à 60° N | 2.5 km |
| coordonnées du premier point de grille | 41.2405° N  66.1830° W |
| coordonnées (i; j) du Pôle Nord | (1078.0, 1867.7) |
| orientation de la grille (par rapport à l’axe des j) | -36.2° |


## Nomenclature des noms de fichiers 

### Grille polaire stéréographique

Les fichiers ont la nomenclature suivante :

CMC_hrdps_domain_Variable_TypedeNiveau_Niveau_ps2.5km_YYYYMMDDHH_Phhh-mm.grib2

où :

* __CMC__ : Chaîne de caractères constante indiquant que le Centre météorologique canadien (CMC) émet les prévisions.
* __hrdps__ : Chaîne de caractères constante indiquant que les données proviennent du Système haute résolution de prévision déterministe.
* __domain__ : Chaîne de caractères constante indiquant le domaine.
* __Variable__ : Type de variable contenu dans le fichier (ex. : UGRD).
* __TypedeNiveau__ : Type de niveau.
* __Niveau__ : Valeur du niveau.
* __ps2.5km__ : Chaîne de caractères constante indiquant que la projection utilisée est polaire stéréographique à une résolution de 2.5 km.
* __YYYYMMDD__ : Année, mois et jour du début de la prévision.
* __HH__ : Heure UTC de la passe [00, 06, 12, 18].
* __Phhh__ : « P » est un caractère constant. « hhh » représente l’heure de prévision [000, 001, 002, ..., 048].
* __mm__ : « mm » représente les minutes de prévision [Codé en dur à 00 pour l’instant. Les pas de temps de 30 minutes seront disponibles éventuellement.].
* __grib2__ : Chaîne de caractères constante indiquant que le format est GRIB2.

Exemple de nom de fichier :
CMC_hrdps_east_DEPR_ISBL_0175_ps2.5km_2011092412_P003-00.grib2

Le fichier a été créé par le CMC et contient une prévision du Système haute résolution de prévision déterministe. Il contient les dépressions du point de rosée (DEPR), au niveau isobarique 175 mb (ISBL_0175), sur une grille polaire stéréographique à une résolution de 2,5 km (ps2.5km). Il débute le 24 septembre 2011 à 12Z (2011092412). Il contient l’heure de prévision 03 (P003) et les minutes de prévision (00) en format GRIB2 (.grib2).

### Grille lat-lon tournée 

Les fichiers ont la nomenclature suivante :

* {YYYYMMDD}T{HH}Z_MSC_HRDPS_{VAR}_{LVLTYPE-LVL}_{Grille}{resolution}_P{hhh}.grib2
* {YYYYMMDD}T{HH}Z_MSC_HRDPS-WEonG_{VAR}_{LVLTYPE-LVL}_{Grille}{resolution}_PT{hhh}H.grib2

où :

* __YYYYMMDD__ : Année, mois et jour du début de la prévision
* __T__ : Délimiteur temporel selon les normes ISO8601
* __HH__ : Heure UTC de la passe [00, 12]
* __Z__ : Fuseau horaire (heure UTC)
* __MSC__ : Chaîne de caractères constante pour Meteorological Service of Canada, la source des données
* __HRDPS__ : Chaîne de caractères constante indiquant que les données proviennent du Système haute résolution de prévision déterministe
* __HRDPS-WEonG__ : Chaîne de caractères constante indiquant que les données proviennent des éléments du temps sur grille ("WEonG") du Système haute résolution de prévision déterministe
* __VAR__ : Type de variable contenu dans le fichier (ex: UGRD).
* __LVLTYPE-LVL__ : Niveau vertical et hauteur [ex: SFC ou Sfc pour la surface, EATM pour l’intégrale de la colonne, DBS-10-20cm couche entre 10 et 20cm sous la surface, AGL-10m pour la hauteur de 10m au-dessus du sol]
* __Grille__ : Grille horizontale [RLatLon]
* __resolution__ : 0.0225. Signifie une résolution de 0.0225°(environ 2.5km) dans les directions longitudinale et latitudinale
* __P{hhh}__ : « P » est un caractère constant. « hhh » représente l’heure de prévision [000, 001, 002, ..., 048]
* __PT{hhh}H__ : Echéance temporelle selon la norme [ISO8601](https://en.wikipedia.org/wiki/ISO_8601). P, T et H sont des caractères constants désignant Période, Temps et Heure. "hhh" représente l’heure de prévision [000, 001, 002, ..., 048]
* __grib2__ : Chaîne de caractères constante indiquant que le format est GRIB2.

Exemples de nom de fichier :
* 20201123T00Z_MSC_HRDPS_GUST_AGL-10m_RLatLon0.0225_P012.grib2
* 20220821T12Z_MSC_HRDPS-WEonG_VISIFOG_Sfc_RLatLon0.0225_PT024H.grib2

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

Attention : les tableaux ci-dessous ne sont pas à jour (à venir), certaines variables sont manquantes. N'hésitez pas à [nous contacter](mailto:ec.dps-client.ec@canada.ca) pour plus d'information.

* [Prévisions à 000h](https://meteo.gc.ca/grib/HRDPS_HR/HRDPS_nat_ps2p5km_P000_deterministic_f.html)
* [Prévisions pour les heures suivant 000h](https://meteo.gc.ca/grib/HRDPS_HR/HRDPS_ps2p5km_PNONZERO_deterministic_f.html)

Liste des éléments du temps sur grille à la surface (*HRDPS-WEonG*):

| Abréviation du paramètre GRIB2 | Description | Unités   |
|------------------------|-------------|----------|
| BSNOW | Présence de poudrerie | ICEC | binaire (0/1) |
| CFRZR | Probabilité de pluie verglaçante	| %|
| CICEP | Probabilité de grésil | %|
| CONDARAIN | Quantité conditionnelle de précipitation liquide | m |
| CONDICEP | Quantité conditionnelle de granulés de glace solide  | m |
| CP |	Caractère de la précipitation | 0=aucune; 1=averse; 2=intermittente; 3=continue |
| CRAIN | Probabilité de pluie | % |
| CSNOW | Probabilité de neige | % |
| DIST | Orographie du modèle |m |
| DPT |	Température du point de rosée |	C |
| DPTYPE | Type dominant de précipitation | 101=pluie; 110=grêle; 111=bruine; 203=pluie verglaçante; 212=bruine verglaçante; 308=grésil; 405=neige; 409=granulés de neige; 413=cristaux de glace; 414=grains de neige |
| FZPRATE | Quantité conditionnelle de précipitation verglaçante | kg*m-2*m-1 |
| GUST | Rafale de vents | m*s-1 |
| HSNOWL | Hauteur du niveau de la neige | m |
| LAND | Masque terre/eau | fraction |
| PARAIN | Probabilité de précipitation liquide | % |
| PBSNOW | Probabilité de poudrerie | % |
| PDZ |	Probabilité de bruine |	% |
| PFRDZ | Probabilité de bruine verglaçante | % |
| PFRZR | Probabilité de précipitation verglaçante | % |
| POP |	Probabilité de précipitation | % |
| PRATE | Quantité conditionnelle de précipitation | m |
| PSNOWS | Probabilité de bourrasque de neige |	% |
| PTYPE | Type de précipitation instantanée | 1=pluie; 2=pluie/neige; 3=pluie verglaçante; 4=grésil; 5=neige; 6=aucune; 7=bruine; 8=bruine verglaçante; 9=précipitation verglaçante/grésil  |
| SCNDPTYPE | Type de précipitation secondaire | 101=pluie; 110=grêle; 111=bruine; 203=pluie verglaçante; 212=bruine verglaçante; 308=grésil; 405=neige; 409=granulés de neige; 413=cristaux de glace; 414=grains de neige|
| SK | Etat du ciel jour/nuit (couverture et opacité nuageuse combinées) | 0-1=ensoleillé/dégagé; 2-3=généralement ensoleillé/quelques nuages; 4-5-6=alternance de soleil et de nuages/partiellement nuageux; 7-8=généralement nuageux/généralement nuageux; 9=nuageux/nuageux; 10=nuageux/couvert |
| TMP |	Température | C |
| TPII | Indice d'intensité des précipitations totales | 0=aucune intensité; 1=faible; 2=modéré; 3=fort	|
| TSTM | Probabilité d'occurence d'orage | % |
| VISIFOG | Visibilité dans le brouillard glacé | m |
| VISLFOG | Visibilité à travers le brouillard liquide | m |
| WDIR | Direction du vent | Degré vrai |
| WIND | Vitesse du vent | m*s-1 |


## À propos du masque No-Data sur la grille polaire stéréographique continentale

Depuis le 18 octobre 2016, un masque pour mieux représenter les zones où les données ne sont pas disponibles, appelées aussi "No-Data" a été ajouté dans notre procédure d’encodage GRIB2. Ce masque vise uniquement quelques points de grille non-valides (données non-disponibles), toujours les mêmes et qui se situent en périphérie du domaine. Notons que ces points masqués n’ont aucun effet négatif sur la qualité du produit.

## Support

Pour toute question relative à ces données, merci de [communiquer avec nous](https://meteo.gc.ca/mainmenu/contact_us_f.html).

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).




