# Données GRIB du système régional de prévision déterministe (SRPD)

Sous le Système régional de prévision déterministe (SRPD), le modèle de prévision numérique du temps tourne sur une grille de résolution de 10 km au cœur de la grille. Les champs du jeu de données GRIB2 à haute résolution sont disponibles sur une grille polaire stéréographique de 935 x 824 points couvrant l’Amérique du Nord et les eaux environnantes avec une résolution de 10 km à 60 degrés nord.

## Adresse des données 

Les données sont disponibles via le protocole HTTP. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier GRIB2. Nous vous recommandons d’automatiser le téléchargement en le scriptant avec wget (lien externe, anglais) ou un programme équivalent. Pour plus d’information sur wget, consultez les notes d’utilisation.

Les données sont accessibles à l’adresse suivante : https://dd.meteo.gc.ca/model_gem_regional/10km/grib2/HH/hhh/

où :

* HH : Heure UTC du début de la passe du modèle [00, 12]
* hhh : Heure de prévision [000, 001, 002, ..., 048]

## Spécification technique de la grille

*A compléter (image, tableau des spécifications de la grille et fichier des coordonnées géographiques de chaque point de grille*

## Nomenclature des noms de fichiers 

NOTE: TOUTES LES HEURES SONT EN UTC.

Les fichiers ont la nomenclature suivante :

CMC_reg_Variable_TypedeNiveau_Niveau_ps10km_YYYYMMDDHH_Phhh.grib2

où :

* CMC : Chaîne de caractères constante indiquant que le Centre météorologique canadien (CMC) émet les prévisions.
* reg : Chaîne de caractères constante indiquant que les données proviennent du SRPD.
* Variable : Type de variable contenue dans le fichier (ex : UGRD). Pour voir la liste complète, consultez la section « Liste des variables ».
* TypedeNiveau : Type de niveau. Pour voir la liste complète, consultez la section « Liste des variables ».
* Niveau : Valeur du niveau. Pour consulter la liste complète, consultez la section « Liste des variables ».
* ps10km : Chaîne de caractères constante indiquant que la projection utilisée est polaire stéréographique à une résolution de 10 km.
* YYYYMMDD : Année, mois et jour du début de la prévision.
* HH : Heure UTC de la passe [00, 12].
* Phhh : « P » est un caractère constant. « hhh » représente l’heure de prévision [000, 001, 002,...,048]
* grib2 : Chaîne de caractères constante indiquant que le format est GRIB2.

Exemple de nom de fichier : CMC_reg_DEPR_ISBL_1015_ps10km_2010091306_P027.grib2

Le fichier a été créé par le CMC et contient une prévision du SRPD. Il contient les dépressions du point de rosée (DEPR), au niveau isobarique 1015 mb (ISBL_1015), sur une grille polaire stéréographique à une résolution de 10 km (ps10km). Il débute le 13 septembre 2010 à 06Z (22010091306). Il contient l’heure de prévision 27 (P027) en format GRIB2 (.grib2).

## Niveaux  

La couverture verticale des champs tridimensionnels peut atteindre jusqu’à 28 niveaux isobariques.

Niveaux isobariques (hPa) : 1015, 1000, 985, 970, 950, 925, 900, 850, 800, 750, 700, 650, 600, 550, 500, 450, 400, 350, 300, 275, 250, 225, 200, 175, 150, 100, 50.

Certains champs reçoivent une couverture verticale limitée à quatre niveaux isobariques.

Niveaux isobariques (couverture réduite, hPa) : 850, 700, 500, 250.

Autres types de niveaux qui pourraient être applicables à certains champs :

* surface
* hauteur fixe au-dessus du sol
* profondeur fixe sous le sol
* épaisseur entre niveaux isobariques
* sommet théorique de l’atmosphère
* colonne atmosphérique entière

## Liste des variables

Attention: les tableaux ci-dessous ne sont pas à jour (à venir), certaines variables sont manquantes. N'hésitez pas à [nous contacter](mailto:ec.dps-client.ec@canada.ca) pour plus d'information.
    
* [Variables disponibles à 00h](https://meteo.gc.ca/grib/REG_HR/REGIONAL_ps10km_P000_deterministic_f.html)
* [Variables disponibles pour les heures suivant 00h](https://meteo.gc.ca/grib/REG_HR/REGIONAL_ps10km_PNONZERO_deterministic_f.html) 

**Notes** :

* La direction des composantes u (UGRD) et v (VGRD) du vecteur vent doit être résolue selon les composantes i, j de la grille définie et dans la direction croissante des coordonnées i, j. Veuillez vous référer à la table de code 7 du standard GRIB pour de plus amples informations.
* Les paramètres NLWRS_SFC, DSWRF_NTAT, DLWRF_NTAT sont donnés en quantités accumulées. L’intervalle temporel d’accumulation est spécifié selon la valeur numéro 4 de la table de code 5 du standard GRIB. En raison de l’accumulation sur une période, les unités d’origine (watts par mètre carré) deviennent des joules par mètre carré.
* Le paramètre représentant l’humidité dans le modèle est l’humidité spécifique (SPFH). C’est ce paramètre qui devrait être utilisé pour toute application de PNT. La dépression du point de rosée (DEPR) est un paramètre diagnostique déconseillé pour les applications de haute précision.

## À propos du masque No-Data

Depuis le 7 septembre 2016, un masque pour mieux représenter les zones où les données ne sont pas disponibles, appelées aussi "No-Data" a été ajouté dans notre procédure d’encodage GRIB2. Ce masque vise uniquement quelques points de grille non-valides (données non-disponibles), toujours les mêmes et qui se situent en périphérie du domaine. Notons que ces points masqués n’ont aucun effet négatif sur la qualité du produit.

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse: ec.dps-client.ec@canada.ca

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via [ICI](https://www.google.ca/search?q=rdps%20site%3Alists.ec.gc.ca%2Fpipermail%2Fdd_info%2F&safe=active&gws_rd=ssl_) 