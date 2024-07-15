[In English](readme_hurricanes-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [Trajectoires d'ouragans](readme_hurricanes_fr.md) > Trajectoires d'ouragans sur le Datamart du SMC

# Données des trajectoires d'ouragans

Cette page décrit les données des [trajectoires d'ouragans](readme_hurricanes_fr.md) disponibles sur le Datamart du SMC en format shapefile et GeoJSON.

Il y a quatre formats shapefiles (*.shp) qui sont produits et comportent chacun un bulletin de prévisions sur 6 heures lorsque des tempêtes d'origine tropicale menace ou risque de menacer le territoire canadien.

Veuillez noter que les données en format GeoJSON remplaceront à terme les données en format shapefile. Une annonce sera communiquée à cet effet via la liste de diffusion [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier shapefile ou GeoJSON, selon le format choisi.

* Les données en format shapefile sont disponibles à cette adresse :

     * [https://dd.meteo.gc.ca/trajectoires/hurricane/shapefile/{nom-tempête}/](https://dd.meteo.gc.ca/trajectoires/hurricane/shapefile)

où :

     * __nom-tempête__ : nom de la tempête en lettres majuscules (p. ex. « BERTHA »)

* Les données en format GeoJSON sont disponibles sur le site web d'essai de données DD-Alpha du Datamart du SMC à cette adresse :

     * [https://dd.alpha.meteo.gc.ca/hurricanes/](https://dd.alpha.meteo.gc.ca/hurricanes)

Note: L'historique est effacé le 30 avril pour ces 2 jeux de données.

## Nomenclature des noms de fichiers

* __Données en format shapefile__

La convention régissant les noms de fichiers est la suivante :

YYYYMMDD_HHMMZ_STORM-NAME.TYPE.shp

où :

* __YYYYMMDD__HHMM__ : Date d'émission de la prévision (UTC).
* __Z__ : Chaîne de caractère constante indiquant le fuseau horaire Zulu (code pour UTC).
* __STORM-NAME__ : Nom de la tempête (p. ex. BERTHA - ouragan, post-tropical, etc.).
* __TYPE__ : Type de fichier shapefile :

    * « pts » pour points, qui contient majoritairement des données/attributs
    * « lin » pour les segments de ligne qui relient les points de suivi de la prévision
    * « rad » pour les informations des rayons de prévisions de vent (quadrants)
    * « err » pour les informations sur l'erreur de prévision de trajectoire (« cône d'erreur »)

__Notes__:

Il y a 2 types de fichiers, point et ligne.

Lorsque l'utilisateur interroge le fichier shapefile par points, le contenu de chaque colonne est donné comme suit :

| Élément   |  Définition    |
|------------|----------------|
|ADVDATE |	heure d'émission de la prévision en format YYMMDD/HHMM (UTC) |
|BASIN |	Région - 'al' pour l'Atlantique (toujours 'al' pour Centre canadien des ouragans)|
|DATELBL |	Étiquette à utiliser sur une carte|
|ERRCT |	Rayon d'erreur de suivi de la prévision en miles nautiques qui, lorsque cartographié, représente la zone/le cône d'incertitude moyenne dans la prévision de suivi (centre de la tempête) |
|LAT |		Latitude de la position du centre de la tempête|
|LON |		Longitude de la position du centre de la tempête|
|MAXWND |	Intensité - vitesse maximale soutenue des vents en noeuds (miles nautiques à l'heure).  Pour obtenir des km/h, multiplier par 1,84 |
|MSLP |		Pression minimale au centre, en hectopascals
|RXXYY Columns |	douze colonnes représentent les rayons du vent (R) en milles nautiques pour 3 catégories primaires de prévisions : 34 (coups de vent de 34 noeuds),  48 (force de vents de tempête de 48 noeuds) et 64 (force du vent d'ouragans de 64 noeuds). NE, SE, SO, NO représentent les 4 principaux quadrants géographiques entourant la tempête. |
|STORMNAME |	Nom de la tempête - p. ex., BERTHA|
|STORMTYPE |	Type de tempête au moment de l'émission de la prévision : DT = dépression tropicale; TT = tempête tropicale; OU = ouragan; PT = post-tropicale |
|TAU |		Heure prévue à partir de l'heure d'émission, p. ex., 48 = 48 heures/2 jours|
|TCDVLP	|	État de la tempête au moment de l'heure de prévision TAU (DT, TT, OU, PT)|
|TIMEZONE |	fuseau horaire local reflétant la région géographique d'une tempête active|
|VALIDTIME |	Temps pendant lequel la prévision à l'heure TAU est valide. En format DD/HHMM (UTC)|
|TIMESTAMP |     Format ISO pour le paramètre VALIDTIME. Format:  YYYY-MM-DDTHH:MMZ|

Les éléments des fichiers shapefile 'lin' ont les mêmes définitions que les éléments des fichiers 'pts'.

* __Données en format GeoJSON__

Les fichiers ont la nomenclature suivante :

`{YYYYMMDD}T{HHmm}Z_MSC_Hurricane_{Nom}.json`

* __YYYYMMDD__ : Année, mois et jour de l'émission des données
* __T__ : Délimiteur temporel selon les normes ISO8601
* __HHmm__ : Heure et minute à laquelle les données sont émises
* __Z__ : Fuseau horaire (heure UTC)
* __MSC__ : Chaîne de caractères constante pour Meteorological Service of Canada, la source des données
* __ Hurricane__ : Chaîne de caractères constante indiquant le nom du produit contenu dans les fichiers, soit les trajectoires d'ouragans
* __Nom__ :  Chaîne de caractères constante indiquant le nom de l'ouragan
* __json__ : Chaîne de caractères constante indiquant le format GeoJSON

Ex: `20240708T2100Z_MSC_Hurricane_Beryl.json`

## Support

Pour toute question relative à ces données, merci de [nous contacter](https://weather.gc.ca/mainmenu/contact_us_f.html).

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).
