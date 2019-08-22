[In English](readme_hrdps-datamart-alpha_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [SHRPD](readme_hrdps_fr.md) > SHRPD sur le Datamart du SMC

# Données GRIB2 expérimentales à 1km du Système à Haute Résolution de Prévision Déterministe (SHRPD) sur la fenêtre ouest

Au cours de l'été 2017, la Colombie-Britannique a connu de graves incendies de forêt.  Afin de fournir des informations météorologiques plus détaillées et de piloter les modèles de qualité de l'air, le domaine SHRPD 1km ouest a été implémenté en mode expériemtal le 31 juillet 2018. 

Ce système de prévision utilise le Modèle environnemental global multi-échelle (GEM). La résolution horizontale de la grille est d'environ 1.0 km et possède 62 niveaux verticaux avec pilotage par le toit. 

Le niveau de momentum le plus bas se situe à une altitude d'environ 40m. Ce système est piloté par le domaine continental [SHRPD à 2.5 km](readme_hrdps_fr.md), qui fournit les conditions initiales, latérales et aux limites supérieures des champs atmosphériques.  Les conditions de surface initiales sont fournies par le Système canadien d'assimilation des données à la surface (CaLDAS) à 2.5 km qui est couplé au SHRPD à 2.5 km. Les champs hydrométéorologiques initiaux sont "recyclés" à partir de la prévision de 6 heures de l'intégration à 2.5 km du SHRPD. 

Depuis la mise en œuvre initiale du SHRPD 1km ouest, le système fonctionn 2 fois par jour, initialisé à 00 et 12 UTC et est intégré pendant 36 heures. La couverture géographique du système est la plus grande partie de la Colombie-Britannique et de l'Ouest de l'Alberta. Les données sont disponibles à une résolution horizontale de 1.0 km sur 62 niveaux verticaux.

## Adresse des données 

Les données du site web d'essai de données DD-Alpha du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTP. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier GRIB2. Nous vous recommandons d’automatiser le téléchargement en le scriptant avec wget (lien externe, anglais) ou un programme équivalent. Pour plus d’information sur wget, consultez les notes d’utilisation.

Les données sont accessibles à l'adresse suivante :

http://dd.alpha.meteo.gc.ca/model_hrdps/west/1km/grib2/HH/hhh/

où :

* __HH__ : Heure UTC du début de la passe du modèle [00, 12].
* __hhh__ : Heure de prévision [000, 001, 002, ..., 036] 

Un historique de 24 heures est conservé dans ce répertoire.

## Domaine disponible

### Spécification technique de la grille ouest

![Image de la grille du ouest 1km du SHRPD](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_hrdps/grille_hrdps1km_west.png)

Valeurs données aux paramètres de la grille polaire stéréographique ouest.

| Paramètre | Valeur |
| ------ | ------ |
| ni | 1465 |
| nj | 825 | 
| résolution à 60° N | 1.0 km |
| coordonnées du premier point de grille | ° N  ° W |
| coordonnées (i; j) du Pôle Nord | (, ) |
| orientation de la grille (par rapport à l’axe des j) | ° |

## Nomenclature des noms de fichiers 

NOTE: TOUTES LES HEURES SONT EN UTC.

Les fichiers ont la nomenclature suivante :

CMC_hrdps_west_Variable_TypedeNiveau_Niveau_ps1.0km_YYYYMMDDHH_Phhh-mm.grib2

où :

* __CMC__ : Chaîne de caractères constante indiquant que le Centre météorologique canadien (CMC) émet les prévisions.
* __hrdps__ : Chaîne de caractères constante indiquant que les données proviennent du Système haute résolution de prévision déterministe.
* __west__ : Chaîne de caractères constante indiquant le domaine ouest.
* __Variable__ : Type de variable contenu dans le fichier (ex. : UGRD).
* __TypedeNiveau__ : Type de niveau.
* __Niveau__ : Valeur du niveau.
* __ps1.0km__ : Chaîne de caractères constante indiquant que la projection utilisée est polaire stéréographique à une résolution de 1.0km.
* __YYYYMMDD__ : Année, mois et jour du début de la prévision.
* __HH__ : Heure UTC de la passe [00, 06, 12, 18].
* __Phhh__ : « P » est un caractère constant. « hhh » représente l’heure de prévision [000, 001, 002, ..., 024/030/042/048].
* __mm__ : « mm » représente les minutes de prévision [Codé en dur à 00 pour l’instant. Les pas de temps de 30 minutes seront disponibles éventuellement.].
* __grib2__ : Chaîne de caractères constante indiquant que le format est GRIB2.

Exemple de nom de fichier :
CMC_hrdps_west_DEPR_ISBL_0175_ps2.5km_2019082512_P003-00.grib2

Le fichier a été créé par le CMC et contient une prévision du Système haute résolution de prévision déterministe expérimental sur le domaine ouest. Il contient les dépressions du point de rosée (DEPR), au niveau isobarique 175 mb (ISBL_0175), sur une grille polaire stéréographique à une résolution de 1.0 km (ps1.0km). Il débute le 25 août 2019 à 12Z (2019082512). Il contient l’heure de prévision 03 (P003) et les minutes de prévision (00) en format GRIB2 (.grib2).

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

Attention : les tableaux ci-dessous ne sont pas à jour (à venir), certaines variables sont manquantes. N'hésitez pas à [nous contacter](mailto:ec.dps-client.ec@canada.ca) pour plus d'information.

* [Prévisions à 000h](https://meteo.gc.ca/grib/HRDPS_HR/HRDPS_nat_ps2p5km_P000_deterministic_f.html)
* [Prévisions pour les heures suivant 000h](https://meteo.gc.ca/grib/HRDPS_HR/HRDPS_ps2p5km_PNONZERO_deterministic_f.html)

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : ec.dps-client.ec@canada.ca

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).




