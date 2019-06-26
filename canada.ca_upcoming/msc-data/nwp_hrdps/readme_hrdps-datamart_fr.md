[In English](readme_hrdps-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données ouvertes publiques du SMC](../readme_fr.md) > SHRPD sur le Datamart du SMC


# Données GRIB2 du Système à Haute Résolution de Prévision Déterministe (SHRPD)

Le [Système à haute résolution de prévision déterministe ou SHRPD](readme_hrdps_fr.md) est une série de grilles emboitées pour les prévisions à aire limitée (LAM). Les grilles proviennent du SRPD et ont une résolution horizontale de 2,5 km à l’intérieur du domaine, sur une région principale Pancanadienne et sur une région Nord couvrant l'archipel arctique et le Groenland. Le modèle pilote du SHRPD est le Système régional de prévision déterministe ou SRPD. Le SHRPD est opérationnel pour tous les domaines sauf le domaine Nord qui demeure expérimental. Les champs du jeu de données GRIB2 du SHRPD sont disponibles quatre fois par jour (sauf pour le domaine Nord). Des prévisions de 48 heures sont produites pour le domaine Pancanadien.

Les utilisateurs qui tireront le plus avantage des données sont ceux qui ont besoin de prévisions plus détaillées sur la température et sur les vents à la surface pour la journée même. Les prévisions à 2,5 km sont grandement utiles lors des changements de saisons et en hiver lorsque des changements rapides de température et de vents provoquent des changements de phase des précipitations (neige à pluie verglaçante à pluie, par exemple). Elles sont aussi utiles pour les prévisions à court terme aux endroits avec des reliefs accidentés et le long des rivages, car l’influence des changements d’altitude, de topographie ou de nature du terrain sera mieux décrite pour les phénomènes à cette échelle (brises de lacs ou de mer, circulation locale dans des vallées, changements de phase, etc.). Même en terrain moins accidenté ou loin de l’eau du rivage, la justesse de ces prévisions pourrait s’avérer utile à long terme. Le SHRPD devrait également être pris en compte pour des prévisions hydrologiques sur de plus petits bassins.

Le SHRPD n’étant pas équipé de son propre système d’assimilation de données, sa qualité dépend en grande partie du SRPD, qui lui fournit les conditions initiales et aux frontières, ainsi que du système global d’assimilation de données qui opère en amont. Donc, si la prévision du système régional sur la région d’intérêt est discutable, il est probable que la prévision à plus haute résolution magnifie les problèmes de la prévision à l’échelle régionale. Par contre, les conditions initiales de nuages et de surface sont maintenant fournies par le cycle continu d’un système couplé SHRPD-Caldas (Canadian Land Data Assimilation System), ce qui améliore les prévisions des nuages, des précipitations et des champs de surface. De plus, pour les prévisions avec une échéance au-delà de 24 heures, nous aurons toujours recours aux prévisions régionales ou globales.


## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le Protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTP. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier GRIB2. Nous vous recommandons d’automatiser le téléchargement en le scriptant avec wget (lien externe, anglais) ou un programme équivalent. Pour plus d’information sur wget, consultez les notes d’utilisation.

Les données sont accessibles aux adresses suivantes :

* https://dd.meteo.gc.ca/model_hrdps/continental/grib2/HH/hhh/
* https://dd.meteo.gc.ca/model_hrdps/north/grib2/HH/hhh/
* https://dd.meteo.gc.ca/model_hrdps/east/grib2/HH/hhh/
* https://dd.meteo.gc.ca/model_hrdps/prairies/grib2/HH/hhh/
* https://dd.meteo.gc.ca/model_hrdps/west/grib2/HH/hhh/
* https://dd.meteo.gc.ca/model_hrdps/maritimes/grib2/HH/hhh/

où :

* __HH__ : Heure UTC du début de la passe du modèle [00, 06, 12, 18]
* __hhh__ : Heure de prévision [000, 001, 002, ..., 024] de l’Est et des Maritimes
* __hhh__ : Heure de prévision [000, 001, 002, ..., 042] de l’Ouest
* __hhh__ : Heure de prévision [000, 001, 002, ..., 048] du Continental
* __hhh__ : Heure de prévision [000, 001, 002, ..., 048] du Nord à 00Z et 12Z

## Domaines disponibles

### Spécification technique de la grille continentale

![Image de la grille du domaine continental du SHRPD](http://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_hrdps/grille_hrdps_cont.png)

Valeurs données aux paramètres de la grille polaire stéréographique à haute résolution.

| Paramètre | Valeur |
| ------ | ------ |
| ni | 2576 |
| nj | 1456 | 
| résolution à 60° N | 2.5 km |
| coordonnées du premier point de grille | 35.6073° N  128.0813° W |
| coordonnées (i; j) du Pôle Nord | (840.0, 2296.0) |
| orientation de la grille (par rapport à l’axe des j) | -108.0° |

### Spécification technique de la grille nord (expérimental)

![Image de la grille du domaine nord du SHRPD](http://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_hrdps/grille_hrdps_north.png)

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

![Image de la grille du domaine est du SHRPD](http://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_hrdps/grille_hrdps_east.png)

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

![Image de la grille du domaine Prairies du SHRPD](http://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_hrdps/grille_hrdps_prairies.png)

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

![Image de la grille du domaine ouest du SHRPD](http://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_hrdps/grille_hrdps_west.png)

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

![Image de la grille du domaine Maritimes du SHRPD](http://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_hrdps/grille_hrdps_marit.png)

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

NOTE: TOUTES LES HEURES SONT EN UTC.

Les fichiers ont la nomenclature suivante :

CMC_hrdps_domain_Variable_TypedeNiveau_Niveau_ps2.5km_YYYYMMDDHH_Phhh-mm.grib2

où :

__CMC__ : Chaîne de caractères constante indiquant que le Centre météorologique canadien (CMC) émet les prévisions.
__hrdps__ : Chaîne de caractères constante indiquant que les données proviennent du Système haute résolution de prévision déterministe.
__domain__ : Chaîne de caractères constante indiquant le domaine.
__Variable__ : Type de variable contenu dans le fichier (ex. : UGRD).
__TypedeNiveau__ : Type de niveau.
__Niveau__ : Valeur du niveau.
__ps2.5km__ : Chaîne de caractères constante indiquant que la projection utilisée est polaire stéréographique à une résolution de 2.5 km.
__YYYYMMDD__ : Année, mois et jour du début de la prévision.
__HH__ : Heure UTC de la passe [00, 06, 12, 18].
__Phhh__ : « P » est un caractère constant. « hhh » représente l’heure de prévision [000, 001, 002, ..., 024/030/042/048].
__mm__ : « mm » représente les minutes de prévision [Codé en dur à 00 pour l’instant. Les pas de temps de 30 minutes seront disponibles éventuellement.].
__grib2__ : Chaîne de caractères constante indiquant que le format est GRIB2.

Exemple de nom de fichier :
CMC_hrdps_east_DEPR_ISBL_0175_ps2.5km_2011092412_P003-00.grib2

Le fichier a été créé par le CMC et contient une prévision du Système haute résolution de prévision déterministe. Il contient les dépressions du point de rosée (DEPR), au niveau isobarique 175 mb (ISBL_0175), sur une grille polaire stéréographique à une résolution de 2,5 km (ps2.5km). Il débute le 24 septembre 2011 à 12Z (2011092412). Il contient l’heure de prévision 03 (P003) et les minutes de prévision (00) en format GRIB2 (.grib2).


## Niveaux

La couverture verticale des champs tridimensionnels peut atteindre jusqu’à 28 niveaux isobariques.

Niveaux isobariques (hPa) : 1015, 1000, 0985, 0970, 0950, 0925, 0900, 0850, 0800, 0750, 0700, 0650, 0600, 0550, 0500, 0450, 0400, 0350, 0300, 0275, 0250, 0225, 0200, 0175, 0150, 0100, 0050.

Certains champs reçoivent une couverture verticale limitée à quatre niveaux isobariques.

Niveaux isobariques (couverture réduite, hPa) : 0850, 0700, 0500, 0250.

Autres types de niveaux qui pourraient être applicables à certains champs :

* surface
* hauteur fixe au-dessus du sol
* profondeur fixe sous le sol
* épaisseur entre niveaux isobariques
* sommet théorique de l’atmosphère
* colonne atmosphérique entière

## Liste des variables

Attention : les tableaux ci-dessous ne sont pas à jour (à venir), certaines variables sont manquantes. N'hésitez pas à [nous contacter](mailto:ec.dps-client.ec@canada.ca) pour plus d'information.

* [Prévisions à 000h](https://meteo.gc.ca/grib/HRDPS_HR/HRDPS_nat_ps2p5km_P000_deterministic_f.html)
* [Prévisions pour les heures suivant 000h](https://meteo.gc.ca/grib/HRDPS_HR/HRDPS_ps2p5km_PNONZERO_deterministic_f.html)

## À propos du masque No-Data

Depuis le 18 octobre 2016, un masque pour mieux représenter les zones où les données ne sont pas disponibles, appelées aussi "No-Data" a été ajouté dans notre procédure d’encodage GRIB2. Ce masque vise uniquement quelques points de grille non-valides (données non-disponibles), toujours les mêmes et qui se situent en périphérie du domaine. Notons que ces points masqués n’ont aucun effet négatif sur la qualité du produit.

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : ec.dps-client.ec@canada.ca


## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).




